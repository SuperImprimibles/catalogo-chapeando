const mercadopago = require('mercadopago');
const { Resend } = require('resend');

mercadopago.configure({
  access_token: process.env.MP_ACCESS_TOKEN,
});

const resend = new Resend(process.env.RESEND_API_KEY);

const NOTIFY_EMAIL = 'superimprimibles1@gmail.com';

module.exports = async function handler(req, res) {
  // MP siempre espera un 200 rápido
  res.status(200).end();

  if (req.method !== 'POST') return;

  try {
    const { type, data } = req.body;

    // Solo nos interesan los pagos aprobados
    if (type !== 'payment') return;

    const paymentId = data && data.id;
    if (!paymentId) return;

    const payment = await mercadopago.payment.get(paymentId);
    const p = payment.body;

    if (p.status !== 'approved') return;

    // Armar detalle de items
    const items = (p.additional_info && p.additional_info.items) || [];
    const itemsHtml = items.length
      ? items.map(function(i) {
          return '<li>' + i.title + ' x' + i.quantity + ' — $' + Number(i.unit_price).toLocaleString('es-AR') + '</li>';
        }).join('')
      : '<li>Sin detalle de items</li>';

    const total = '$' + Number(p.transaction_amount).toLocaleString('es-AR');
    const comprador = (p.payer && p.payer.email) ? p.payer.email : 'No disponible';
    const fecha = new Date(p.date_approved).toLocaleString('es-AR', { timeZone: 'America/Argentina/Buenos_Aires' });

    await resend.emails.send({
      from:    'Chapeando VM <onboarding@resend.dev>',
      to:      NOTIFY_EMAIL,
      subject: '✅ Nueva venta aprobada — ' + total,
      html: `
        <div style="font-family:Arial,sans-serif;max-width:520px;margin:0 auto;padding:24px;background:#f9f9f9;border-radius:12px">
          <h2 style="color:#111;margin-bottom:4px">✅ Nueva venta aprobada</h2>
          <p style="color:#555;margin-top:0">${fecha}</p>

          <div style="background:#fff;border-radius:8px;padding:16px;margin:16px 0;border:1px solid #eee">
            <p style="margin:0 0 8px"><strong>Comprador:</strong> ${comprador}</p>
            <p style="margin:0 0 8px"><strong>Total:</strong> ${total}</p>
            <p style="margin:0 0 8px"><strong>ID de pago:</strong> ${paymentId}</p>
          </div>

          <div style="background:#fff;border-radius:8px;padding:16px;border:1px solid #eee">
            <strong>Productos:</strong>
            <ul style="margin:8px 0 0;padding-left:18px;color:#333">${itemsHtml}</ul>
          </div>

          <p style="margin-top:20px;font-size:12px;color:#aaa">Chapeando VM · Notificación automática</p>
        </div>
      `,
    });

  } catch (err) {
    console.error('Webhook error:', err);
  }
};
