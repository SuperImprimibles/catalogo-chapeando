CÓMO AGREGAR UN PRODUCTO
========================

1. Ir a la carpeta de la categoría correspondiente, por ejemplo: Vintages, Ilustraciones, Deco, etc.

2. Dentro de esa carpeta agregar las fotos del producto:
   - nombre-del-producto.jpg         → foto principal (producto solo, fondo limpio)
   - nombre-del-producto-escena.jpg  → producto en ambientes/escenarios
   - nombre-del-producto-escena2.jpg → (opcional, más escenas)

3. En productos.js agregar el artículo así:

   {
     id: "VIN-50",
     title: "Nombre del producto",
     cat: "vintages",
     size: "-",
     mat: "Metal",
     unit: "1 pieza",
     price: "$9.990",
     img: "Tienda (Imagenes)/Productos/Vintages/nombre-del-producto.jpg",
     gallery: [
       "Tienda (Imagenes)/Productos/Vintages/nombre-del-producto.jpg",
       "Tienda (Imagenes)/Productos/Vintages/nombre-del-producto-escena.jpg",
       "Tienda (Imagenes)/Productos/Vintages/nombre-del-producto-escena2.jpg"
     ]
   },

NOTAS:
- Las imágenes pueden ser .jpg o .png
- El campo gallery[] es opcional; si no lo ponés solo se muestra la imagen principal
- El ID debe ser único y seguir la secuencia de cada categoría
