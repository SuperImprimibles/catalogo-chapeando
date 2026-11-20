CÓMO SUBIR EL BACKEND A VERCEL
==============================

1. Entrá a https://vercel.com y creá una cuenta gratis (podés usar tu cuenta de GitHub)

2. Una vez dentro, hacé clic en "Add New Project"

3. Elegí "Upload" (subir archivos) y subí SOLO esta carpeta "backend"

4. Vercel detecta automáticamente que es una función serverless

5. Antes de desplegar, en la sección "Environment Variables" agregá:
   - Nombre:  MP_ACCESS_TOKEN
   - Valor:   (tu Access Token de MercadoPago — ver abajo)

6. Hacé clic en "Deploy" y esperá unos segundos

7. Vercel te da una URL tipo: https://chapeando-backend.vercel.app
   → Pasale esa URL a Kiro para conectarla con la tienda

CÓMO OBTENER EL ACCESS TOKEN DE MERCADOPAGO
============================================
1. Entrá a https://www.mercadopago.com.ar/developers
2. Iniciá sesión con tu cuenta de MercadoPago
3. Ir a "Tus integraciones" → "Crear aplicación"
4. Nombre: Chapeando VM, tipo: Pagos online
5. En "Credenciales de producción" copiá el "Access Token"
   (empieza con APP_USR-...)

IMPORTANTE: nunca compartas el Access Token públicamente
