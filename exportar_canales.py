"""
exportar_canales.py
Lee productos.csv y genera archivos listos para importar en cada canal:

  export/mercadolibre.csv   → MercadoLibre (formato flex)
  export/meta.csv           → Instagram Shopping / Facebook Shop
  export/whatsapp.csv       → WhatsApp Business Catalog
  export/temu_shopee.csv    → Temu / Shopee

Para ejecutar: python exportar_canales.py
"""

import csv, os, re

ROOT   = os.path.dirname(os.path.abspath(__file__))
SRC    = os.path.join(ROOT, 'productos.csv')
OUTDIR = os.path.join(ROOT, 'export')
os.makedirs(OUTDIR, exist_ok=True)

SITE = "https://superimprimibles.github.io/catalogo-chapeando"

# ── URL pública de imagen ────────────────────────────────────────────────────
# Las imágenes están en GitHub Pages, misma URL base que la tienda
def img_url(rel_path):
    if not rel_path:
        return ''
    # Reemplazar espacios y caracteres especiales
    encoded = rel_path.replace(' ', '%20')
    return f"{SITE}/{encoded}"

def load():
    with open(SRC, encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

# ── MERCADOLIBRE ─────────────────────────────────────────────────────────────
def export_ml(rows):
    """
    Formato CSV para carga masiva de MercadoLibre Argentina.
    Referencia: https://vendedores.mercadolibre.com.ar/nota/carga-masiva
    """
    campos = [
        "ID","Título","Descripción","Categoría ML","Precio","Moneda",
        "Stock","Condición","Imagen 1","Imagen 2","SKU vendedor",
        "Dimensiones (cm)","Material","URL",
    ]
    # Mapeo de categorías propias → categorías ML Argentina
    cat_ml = {
        "Argentina":           "Decoración > Cuadros y Pósters",
        "Calendarios Perpetuos":"Decoración > Cuadros y Pósters",
        "Cine":                "Decoración > Cuadros y Pósters",
        "Deco":                "Decoración > Cuadros y Pósters",
        "Deportes":            "Decoración > Cuadros y Pósters",
        "Días Especiales":     "Decoración > Cuadros y Pósters",
        "Ilustraciones":       "Decoración > Cuadros y Pósters",
        "Imanes":              "Decoración > Imanes Decorativos",
        "Infantil y Juvenil":  "Decoración > Cuadros y Pósters",
        "Música":              "Decoración > Cuadros y Pósters",
        "Numeración":          "Decoración > Letreros y Señales",
        "Parrilla y Asado":    "Decoración > Cuadros y Pósters",
        "Personalizados":      "Decoración > Cuadros y Pósters",
        "Publicidades Vintage":"Decoración > Cuadros y Pósters",
        "Rutas y Señales":     "Decoración > Letreros y Señales",
        "Señalítica":          "Decoración > Letreros y Señales",
        "Vehículos":           "Decoración > Cuadros y Pósters",
        "Vintages":            "Decoración > Cuadros y Pósters",
    }
    out = os.path.join(OUTDIR, 'mercadolibre.csv')
    with open(out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for r in rows:
            w.writerow({
                "ID":               '',
                "Título":           f"Chapa decorativa {r['titulo']} - {r['tamaño']} - Aluminio",
                "Descripción":      r['descripcion'],
                "Categoría ML":     cat_ml.get(r['categoria'], "Decoración > Cuadros y Pósters"),
                "Precio":           r['precio'],
                "Moneda":           "ARS",
                "Stock":            r['stock'],
                "Condición":        "Nuevo",
                "Imagen 1":         img_url(r['imagen_1']),
                "Imagen 2":         img_url(r['imagen_2']),
                "SKU vendedor":     r['sku'],
                "Dimensiones (cm)": r['tamaño'],
                "Material":         r['material'],
                "URL":              r['url_tienda'],
            })
    print(f"✅ MercadoLibre  → {out} ({len(rows)} filas)")

# ── META (Instagram / Facebook Shop) ────────────────────────────────────────
def export_meta(rows):
    """
    Formato Facebook Product Catalog (CSV).
    Referencia: https://www.facebook.com/business/help/120325381656392
    """
    campos = [
        "id","title","description","availability","condition","price",
        "link","image_link","additional_image_link","brand","google_product_category",
        "custom_label_0","custom_label_1","item_group_id",
    ]
    out = os.path.join(OUTDIR, 'meta.csv')
    with open(out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for r in rows:
            w.writerow({
                "id":                     r['sku'],
                "title":                  f"Chapa decorativa {r['titulo']}",
                "description":            r['descripcion'],
                "availability":           "in stock",
                "condition":              "new",
                "price":                  f"{r['precio']} ARS",
                "link":                   r['url_tienda'],
                "image_link":             img_url(r['imagen_1']),
                "additional_image_link":  img_url(r['imagen_2']),
                "brand":                  "Chapeando",
                "google_product_category":"Home & Garden > Decor > Picture Frames & Displays",
                "custom_label_0":         r['categoria'],
                "custom_label_1":         r['material'],
                "item_group_id":          re.sub(r'-\d+$', '', r['sku']),
            })
    print(f"✅ Meta (IG/FB)  → {out} ({len(rows)} filas)")

# ── WHATSAPP BUSINESS CATALOG ────────────────────────────────────────────────
def export_wa(rows):
    """
    Formato para catálogo de WhatsApp Business (vía Meta Commerce Manager).
    Mismo formato que Meta pero con campos simplificados.
    """
    campos = ["id","title","description","price","currency","image_link","link"]
    out = os.path.join(OUTDIR, 'whatsapp.csv')
    with open(out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for r in rows:
            w.writerow({
                "id":          r['sku'],
                "title":       f"Chapa {r['titulo']}",
                "description": r['descripcion'],
                "price":       r['precio'],
                "currency":    "ARS",
                "image_link":  img_url(r['imagen_1']),
                "link":        r['url_tienda'],
            })
    print(f"✅ WhatsApp Biz  → {out} ({len(rows)} filas)")

# ── TEMU / SHOPEE ────────────────────────────────────────────────────────────
def export_temu_shopee(rows):
    """
    Formato genérico compatible con Temu y Shopee.
    """
    campos = [
        "seller_sku","product_name","category","description",
        "price","currency","stock","condition",
        "image_1","image_2","material","dimensions","brand",
    ]
    out = os.path.join(OUTDIR, 'temu_shopee.csv')
    with open(out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for r in rows:
            w.writerow({
                "seller_sku":   r['sku'],
                "product_name": f"Decorative Metal Sign - {r['titulo']} - {r['tamaño']}",
                "category":     r['categoria'],
                "description":  r['descripcion'],
                "price":        r['precio'],
                "currency":     "ARS",
                "stock":        r['stock'],
                "condition":    "New",
                "image_1":      img_url(r['imagen_1']),
                "image_2":      img_url(r['imagen_2']),
                "material":     r['material'],
                "dimensions":   r['tamaño'],
                "brand":        "Chapeando",
            })
    print(f"✅ Temu/Shopee   → {out} ({len(rows)} filas)")

# ── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    if not os.path.exists(SRC):
        print("❌ productos.csv no encontrado. Ejecutá primero: python generar_csv.py")
        return
    rows = load()
    print(f"Cargados {len(rows)} productos desde productos.csv\n")
    export_ml(rows)
    export_meta(rows)
    export_wa(rows)
    export_temu_shopee(rows)
    print(f"\nTodos los archivos están en: {OUTDIR}")

if __name__ == '__main__':
    main()
