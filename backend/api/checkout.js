const mercadopago = require('mercadopago');

mercadopago.configure({
  access_token: process.env.MP_ACCESS_TOKEN,
});

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Método no permitido' });

  try {
    const { items, envio } = req.body;

    if (!items || !items.length) {
      return res.status(400).json({ error: 'No hay productos en el carrito' });
    }

    const mpItems = items.map(function(item) {
      var mpItem = {
        id: item.id,
        title: item.title,
        quantity: Number(item.qty),
        unit_price: Number(item.priceNum),
        currency_id: 'ARS',
      };
      if (item.img) {
        mpItem.picture_url = 'https://superimprimibles.github.io/catalogo-chapeando/' + item.img;
      }
      return mpItem;
    });

    const preference = await mercadopago.preferences.create({
      items: mpItems,
      external_reference: envio || '',
      back_urls: {
        success:  'https://superimprimibles.github.io/catalogo-chapeando/?pago=ok',
        failure:  'https://superimprimibles.github.io/catalogo-chapeando/?pago=error',
        pending:  'https://superimprimibles.github.io/catalogo-chapeando/?pago=pendiente',
      },
      auto_return: 'approved',
      statement_descriptor: 'Chapeando VM',
      notification_url: 'https://catalogo-chapeando-backend.vercel.app/api/webhook',
    });

    return res.status(200).json({ init_point: preference.body.init_point });

  } catch (err) {
    console.error(err);
    return res.status(500).json({ error: err.message || 'Error generando el pago' });
  }
};
