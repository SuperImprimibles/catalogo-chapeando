const { MercadoPagoConfig, Preference } = require('mercadopago');

const client = new MercadoPagoConfig({
  accessToken: process.env.MP_ACCESS_TOKEN,
});

module.exports = async function handler(req, res) {
  // Permitir CORS desde tu tienda
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Método no permitido' });

  try {
    const { items } = req.body;

    if (!items || !items.length) {
      return res.status(400).json({ error: 'No hay productos en el carrito' });
    }

    // Convertir los items del carrito al formato de MercadoPago
    const mpItems = items.map(function(item) {
      return {
        id: item.id,
        title: item.title,
        quantity: item.qty,
        unit_price: item.priceNum,
        currency_id: 'ARS',
      };
    });

    const preference = new Preference(client);
    const response = await preference.create({
      body: {
        items: mpItems,
        back_urls: {
          success: 'https://superimprimibles.github.io/catalogo-chapeando/Index%20Tienda.html?pago=ok',
          failure: 'https://superimprimibles.github.io/catalogo-chapeando/Index%20Tienda.html?pago=error',
          pending: 'https://superimprimibles.github.io/catalogo-chapeando/Index%20Tienda.html?pago=pendiente',
        },
        auto_return: 'approved',
        statement_descriptor: 'Chapeando VM',
        payment_methods: {
          excluded_payment_types: [],
          installments: 1,
        },
      },
    });

    return res.status(200).json({ init_point: response.init_point });

  } catch (err) {
    console.error(err);
    return res.status(500).json({ error: 'Error generando el pago' });
  }
};
