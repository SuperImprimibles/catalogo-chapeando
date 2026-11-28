const mercadopago = require('mercadopago');
const { Resend } = require('resend');
const SibApiV3Sdk = require('@getbrevo/brevo');

mercadopago.configure({
  access_token: process.env.MP_ACCESS_TOKEN,
});

const resend = new Resend(process.env.RESEND_API_KEY);

// Brevo — para email al cliente
const brevoClient = new SibApiV3Sdk.TransactionalEmailsApi();
brevoClient.authentications['api-key'].apiKey = process.env.BREVO_API_KEY;

const NOTIFY_EMAIL = 'superimprimibles1@gmail.com';

module.exports = async function handler(req, res) {
  res.status(200).end();

  if (req.method !== 'POST') return;

  try {
    const { type, data } = req.body;
    if (type !== 'payment') return;

    const paymentId = data && data.id;
    if (!paymentId) return;

    const payment = await mercadopago.payment.get(paymentId);
    const p = payment.body;
    if (p.status !== 'approved') return;

    // Datos del pago
    const items      = (p.additional_info && p.additional_info.items) || [];
    const total      = '$' + Number(p.transaction_amount).toLocaleString('es-AR');
    const comprador  = (p.payer && p.payer.email) ? p.payer.email : null;
    const fecha      = new Date(p.date_approved).toLocaleString('es-AR', { timeZone: 'America/Argentina/Buenos_Aires' });
    const envio      = p.external_reference || 'No especificado';

    const itemsHtml = items.length
      ? items.map(function(i) {
          return '<li>' + i.title + ' x' + i.quantity + ' — $' + Number(i.unit_price).toLocaleString('es-AR') + '</li>';
        }).join('')
      : '<li>Sin detalle de items</li>';

    // Envío con teléfono clickeable a WA
    const envioHtml = envio
      .replace(/\n/g, '<br>')
      .replace(/   /g, '&nbsp;&nbsp;&nbsp;')
      .replace(/📱 Tel: ([+\d\s\-().]+)/g, function(match, tel) {
        var clean = tel.replace(/[\s\-().]/g, '');
        return '📱 Tel: <a href="https://wa.me/' + clean + '" style="color:#25d366;font-weight:700">' + tel + '</a>';
      });

    // ── EMAIL A VOS (Resend) ──────────────────────────────────
    await resend.emails.send({
      from:    'Chapeando VM <onboarding@resend.dev>',
      to:      NOTIFY_EMAIL,
      subject: '✅ Nueva venta aprobada — ' + total,
      html: `
        <div style="font-family:Arial,sans-serif;max-width:520px;margin:0 auto;padding:24px;background:#f9f9f9;border-radius:12px">
          <h2 style="color:#111;margin-bottom:4px">✅ Nueva venta aprobada</h2>
          <p style="color:#555;margin-top:0">${fecha}</p>
          <div style="background:#fff;border-radius:8px;padding:16px;margin:16px 0;border:1px solid #eee">
            <p style="margin:0 0 8px"><strong>Comprador:</strong> ${comprador || 'No disponible'}</p>
            <p style="margin:0 0 8px"><strong>Total:</strong> ${total}</p>
            <p style="margin:0 0 0"><strong>ID de pago:</strong> ${paymentId}</p>
          </div>
          <div style="background:#fff;border-radius:8px;padding:16px;margin:16px 0;border:1px solid #eee">
            <strong>Entrega:</strong>
            <p style="margin:8px 0 0;color:#333;line-height:1.6">${envioHtml}</p>
          </div>
          <div style="background:#fff;border-radius:8px;padding:16px;border:1px solid #eee">
            <strong>Productos:</strong>
            <ul style="margin:8px 0 0;padding-left:18px;color:#333">${itemsHtml}</ul>
          </div>
          <p style="margin-top:20px;font-size:12px;color:#aaa">Chapeando VM · Notificación automática</p>
        </div>
      `,
    });

    // ── EMAIL AL CLIENTE (Brevo) ──────────────────────────────
    if (comprador) {
      const sendSmtpEmail = new SibApiV3Sdk.SendSmtpEmail();
      sendSmtpEmail.sender   = { name: 'Chapeando VM', email: NOTIFY_EMAIL };
      sendSmtpEmail.to       = [{ email: comprador }];
      sendSmtpEmail.subject  = '✅ ¡Tu compra en Chapeando VM fue confirmada!';
      sendSmtpEmail.htmlContent = `
        <div style="font-family:Arial,sans-serif;max-width:520px;margin:0 auto;padding:24px;background:#f9f9f9;border-radius:12px">
          <h2 style="color:#111;margin-bottom:4px">¡Gracias por tu compra! 🎉</h2>
          <p style="color:#555;margin-top:0">Tu pago fue aprobado el ${fecha}.</p>

          <div style="background:#fff;border-radius:8px;padding:16px;margin:16px 0;border:1px solid #eee">
            <strong>Resumen de tu pedido:</strong>
            <ul style="margin:8px 0 0;padding-left:18px;color:#333">${itemsHtml}</ul>
            <p style="margin:12px 0 0"><strong>Total pagado:</strong> ${total}</p>
          </div>

          <div style="background:#fff;border-radius:8px;padding:16px;margin:16px 0;border:1px solid #eee">
            <strong>Datos de entrega:</strong>
            <p style="margin:8px 0 0;color:#333;line-height:1.6">${envio.replace(/\n/g, '<br>')}</p>
          </div>

          <p style="color:#555;line-height:1.6">Nos vamos a contactar a la brevedad para coordinar la entrega. Ante cualquier consulta respondé este email o escribinos por WhatsApp.</p>

          <div style="text-align:center;margin-top:20px">
            <a href="https://wa.me/5492657663302" style="background:#25d366;color:#fff;padding:12px 28px;border-radius:999px;text-decoration:none;font-weight:700;font-size:14px">Escribinos por WhatsApp</a>
          </div>

          <p style="margin-top:24px;font-size:12px;color:#aaa;text-align:center">Chapeando VM · superimprimibles1@gmail.com</p>
        </div>
      `;
      await brevoClient.sendTransacEmail(sendSmtpEmail);
    }

  } catch (err) {
    console.error('Webhook error:', err);
  }
};
