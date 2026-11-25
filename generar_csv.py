"""
generar_csv.py
Genera productos.csv como fuente única de datos para todos los canales:
  Tienda web, MercadoLibre, Instagram/Facebook, WhatsApp Business, Temu, Shopee.

Para actualizar: python generar_csv.py
"""

import os, re, csv

ROOT     = os.path.dirname(os.path.abspath(__file__))
CAT_ROOT = os.path.join(ROOT, "Tienda (Imagenes)", "Categorias")
IMG_EXTS = {'.jpg', '.jpeg', '.png', '.webp'}
SKIP     = {'Fondo, Ilustracion, Imanes.jpg', 'Marco para imanes.png',
            'tercera imagen para la galeria de imanes.jpg',
            'README.txt', 'Detalles.txt'}

SITE_BASE = "https://superimprimibles.github.io/catalogo-chapeando"

CAT_META = {
    "Argentina":            {"slug":"argentina",     "label":"Argentina",             "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Calendarios Perpetuos":{"slug":"calendarios",   "label":"Calendarios Perpetuos", "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Cine":                 {"slug":"cine",           "label":"Cine",                  "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Deco":                 {"slug":"deco",           "label":"Deco",                  "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Deportes":             {"slug":"deportes",       "label":"Deportes",              "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Dias Especiales":      {"slug":"dias-especiales","label":"Días Especiales",       "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Ilustraciones":        {"slug":"ilustraciones",  "label":"Ilustraciones",         "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Imanes":               {"slug":"imanes",         "label":"Imanes",                "precio":2500,  "material":"Aluminio imantado","tamaño":"9 x 9 cm"},
    "Infantil y Juvenil":   {"slug":"infantil",       "label":"Infantil y Juvenil",    "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Musica":               {"slug":"musica",         "label":"Música",                "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Numeracion":           {"slug":"numeracion",     "label":"Numeración",            "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Parrilla y Asado":     {"slug":"parrilla",       "label":"Parrilla y Asado",      "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Personalizados":       {"slug":"personalizados", "label":"Personalizados",        "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Publicidades Vintage": {"slug":"publicidades",   "label":"Publicidades Vintage",  "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Rutas y Señales":      {"slug":"rutas",          "label":"Rutas y Señales",       "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Señalitica":           {"slug":"señalitica",     "label":"Señalítica",            "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Vehiculos":            {"slug":"vehiculos",      "label":"Vehículos",             "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
    "Vintages":             {"slug":"vintages",       "label":"Vintages",              "precio":14900, "material":"Aluminio","tamaño":"20 x 30 cm"},
}

DESCRIPCIONES = {
    "imanes":       "Imán decorativo de aluminio imantado con impresión de alta definición. Ideal para heladera, pizarrones y superficies metálicas. Colores vibrantes y resistentes.",
    "señalitica":   "Cartel de señalítica en chapa de aluminio con impresión UV de alta definición. Resistente a la intemperie, con 4 perforaciones para colgar.",
    "personalizados":"Chapa de aluminio 100% personalizada con tu foto, frase o diseño. Ideal para regalos y decoración. Consultá por diseños a medida.",
    "calendarios":  "Calendario perpetuo en chapa de aluminio decorativa. Reutilizable año a año. Diseño único para decorar cualquier espacio.",
    "default":      "Chapa decorativa de aluminio con impresión UV de alta definición. Colores vibrantes y resistentes al tiempo. Con 4 perforaciones para colgar. Ideal para decorar hogares, bares, talleres y locales.",
}

def to_title(filename, cat_label=''):
    name = os.path.splitext(filename)[0]
    if re.match(r'^luna-[a-z]+-(\d+)$', name, re.IGNORECASE):
        m = re.match(r'^luna-[a-z]+-(\d+)$', name, re.IGNORECASE)
        return f"{cat_label} {int(m.group(1))}"
    if re.match(r'^IMA-0*(\d+)$', name, re.IGNORECASE):
        m = re.match(r'^IMA-0*(\d+)$', name, re.IGNORECASE)
        return f"Imán {int(m.group(1))}"
    if re.match(r'^ima-(.+)$', name, re.IGNORECASE):
        m = re.match(r'^ima-(.+)$', name, re.IGNORECASE)
        return m.group(1).replace('-',' ').replace('_',' ').strip().title()
    if re.match(r'^D_NQ|^[A-Z]{2,}_[A-Z]{2,}', name):
        return cat_label or 'Producto'
    if re.match(r'^\d{6,}$', name):
        return cat_label or 'Producto'
    m = re.match(r'^(.+?)\s*[\-_ ]\s*\d{5,}$', name)
    if m:
        clean = m.group(1).replace('-',' ').replace('_',' ').strip()
        return clean.title() if clean == clean.lower() else clean
    if re.match(r'^([a-z]+)-(\d+)$', name, re.IGNORECASE):
        m = re.match(r'^([a-z]+)-(\d+)$', name, re.IGNORECASE)
        return f"{m.group(1).capitalize()} {int(m.group(2))}"
    if re.match(r'^(\d+)$', name):
        m = re.match(r'^(\d+)$', name)
        return f"{cat_label} {int(m.group(1))}" if cat_label else name
    name = re.sub(r'\s*[\(\-]\s*[Ii]lustracion\s*2?\s*[\)\-]?\s*$', '', name).strip()
    name = re.sub(r'[-_]', ' ', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name.title() if name == name.lower() else name

def rel(path):
    return os.path.relpath(path, ROOT).replace('\\', '/')

def collect():
    rows = []
    for folder_name in sorted(os.listdir(CAT_ROOT)):
        folder_path = os.path.join(CAT_ROOT, folder_name)
        if not os.path.isdir(folder_path):
            continue
        meta = CAT_META.get(folder_name)
        if not meta:
            continue

        slug    = meta['slug']
        label   = meta['label']
        precio  = meta['precio']
        mat     = meta['material']
        tamaño  = meta['tamaño']
        desc    = DESCRIPCIONES.get(slug, DESCRIPCIONES['default'])
        prefix  = slug[:3].upper()

        # Recopilar archivos
        all_files = []
        for dirpath, _, filenames in os.walk(folder_path):
            for fname in sorted(filenames):
                if fname in SKIP:
                    continue
                if os.path.splitext(fname)[1].lower() in IMG_EXTS:
                    all_files.append((fname, dirpath))

        # Separar ilustraciones de fotos reales
        ilust_map  = {}
        normal_map = {}
        for fname, dirpath in all_files:
            name_no_ext = os.path.splitext(fname)[0]
            clean = re.sub(r'\s*[\(\-]\s*[Ii]lustracion\s*[\)\-]?\s*\d*$', '', name_no_ext).strip()
            is_ilust = clean != name_no_ext
            ruta = rel(os.path.join(dirpath, fname))
            if is_ilust:
                ilust_map[clean.lower()] = ruta
            else:
                normal_map[name_no_ext.lower()] = (fname, dirpath, ruta)

        idx = 1
        used = set()

        for key, (fname, dirpath, ruta) in sorted(normal_map.items()):
            img2 = ilust_map.get(key, '')
            if img2:
                used.add(key)
            titulo = to_title(fname, label)
            sku    = f"CHP-{prefix}-{idx:03d}"
            rows.append({
                "sku":          sku,
                "titulo":       titulo,
                "descripcion":  desc,
                "categoria":    label,
                "precio":       precio,
                "material":     mat,
                "tamaño":       tamaño,
                "imagen_1":     ruta,
                "imagen_2":     img2,
                "stock":        99,
                "url_tienda":   f"{SITE_BASE}/#{sku}",
            })
            idx += 1

        for key, ruta in sorted(ilust_map.items()):
            if key in used:
                continue
            fname  = os.path.basename(ruta)
            titulo = to_title(fname, label)
            sku    = f"CHP-{prefix}-{idx:03d}"
            rows.append({
                "sku":          sku,
                "titulo":       titulo,
                "descripcion":  desc,
                "categoria":    label,
                "precio":       precio,
                "material":     mat,
                "tamaño":       tamaño,
                "imagen_1":     ruta,
                "imagen_2":     '',
                "stock":        99,
                "url_tienda":   f"{SITE_BASE}/#{sku}",
            })
            idx += 1

    return rows

def main():
    rows = collect()
    out  = os.path.join(ROOT, 'productos.csv')
    campos = ["sku","titulo","descripcion","categoria","precio","material","tamaño","imagen_1","imagen_2","stock","url_tienda"]
    with open(out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(rows)
    print(f"Productos: {len(rows)}")
    print(f"Escrito:   {out}")

if __name__ == '__main__':
    main()
