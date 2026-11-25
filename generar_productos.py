"""
generar_productos.py
Lee las carpetas Tienda (Imagenes)/Categorias y Sets
y genera productos.js con la estructura que espera index.html:
  const items = [{ id, title, cat, img, size, mat, price, gallery }, ...]
  const sets   = [{ id, label, thumb, images }, ...]
"""

import os
import json
import re

ROOT     = os.path.dirname(os.path.abspath(__file__))
IMG_ROOT = os.path.join(ROOT, "Tienda (Imagenes)")
CAT_ROOT = os.path.join(IMG_ROOT, "Categorias")
SET_ROOT = os.path.join(IMG_ROOT, "Sets")
IMG_EXTS = {'.jpg', '.jpeg', '.png', '.webp'}

# Archivos que no son productos
SKIP_FILES = {
    'Fondo, Ilustracion, Imanes.jpg',
    'Marco para imanes.png',
    'tercera imagen para la galeria de imanes.jpg',
    'README.txt', 'Detalles.txt',
}

# Carpeta → slug de categoría (igual que usa index.html en filterCat)
CAT_SLUG = {
    "Argentina":            "argentina",
    "Calendarios Perpetuos":"calendarios",
    "Cine":                 "cine",
    "Deco":                 "deco",
    "Deportes":             "deportes",
    "Dias Especiales":      "dias-especiales",
    "Ilustraciones":        "ilustraciones",
    "Imanes":               "imanes",
    "Infantil y Juvenil":   "infantil",
    "Musica":               "musica",
    "Numeracion":           "numeracion",
    "Parrilla y Asado":     "parrilla",
    "Personalizados":       "personalizados",
    "Publicidades Vintage": "publicidades",
    "Rutas y Señales":      "rutas",
    "Señalitica":           "señalitica",
    "Vehiculos":            "vehiculos",
    "Vintages":             "vintages",
}

def to_title(filename, cat_label=''):
    name = os.path.splitext(filename)[0]

    # luna-categoria-NNN → usa cat_label + número
    m = re.match(r'^luna-[a-z]+-(\d+)$', name, re.IGNORECASE)
    if m:
        return f"{cat_label} {int(m.group(1))}" if cat_label else name

    # IMA-006 → Imán 6
    m = re.match(r'^IMA-0*(\d+)$', name, re.IGNORECASE)
    if m:
        return f"Imán {int(m.group(1))}"

    # ima-nombre → limpiar prefijo y capitalizar
    m = re.match(r'^ima-(.+)$', name, re.IGNORECASE)
    if m:
        clean = m.group(1).replace('-', ' ').replace('_', ' ').strip()
        return clean.title()

    # Códigos tipo MercadoLibre (D_NQ_NP...) → cat_label
    if re.match(r'^D_NQ|^[A-Z]{2,}_[A-Z]{2,}', name):
        return cat_label or 'Producto'

    # nombre-numero-largo → solo el nombre
    m = re.match(r'^(.+?)\s*[\-_ ]\s*\d{5,}$', name)
    if m:
        clean = m.group(1).replace('-',' ').replace('_',' ').strip()
        return clean.title() if clean == clean.lower() else clean

    # cine-10, deco-45 → Cine 10, Deco 45
    m = re.match(r'^([a-z]+)-(\d+)$', name, re.IGNORECASE)
    if m:
        return f"{m.group(1).capitalize()} {int(m.group(2))}"

    # ID largo numérico puro (ej: 52987733111298558) → solo cat_label
    if re.match(r'^\d{6,}$', name):
        return cat_label or 'Producto'

    # Solo número corto → usa cat_label + número
    m = re.match(r'^(\d+)$', name)
    if m:
        return f"{cat_label} {int(m.group(1))}" if cat_label else name

    # Quitar sufijo " (Ilustracion)" y variantes
    name = re.sub(r'\s*[\(\-]\s*[Ii]lustracion\s*2?\s*[\)\-]?\s*$', '', name).strip()

    # Reemplazar guiones y underscores
    name = re.sub(r'[-_]', ' ', name)
    name = re.sub(r'\s+', ' ', name).strip()

    # Si ya tiene mayúsculas propias, respetar; si es todo minúsculas, titlecase
    return name.title() if name == name.lower() else name

def rel(path):
    return os.path.relpath(path, ROOT).replace('\\', '/')

def collect_items():
    items = []
    for folder_name in sorted(os.listdir(CAT_ROOT)):
        folder_path = os.path.join(CAT_ROOT, folder_name)
        if not os.path.isdir(folder_path):
            continue
        slug = CAT_SLUG.get(folder_name)
        if not slug:
            continue
        prefix = slug[:3].upper()

        # Recopilar todos los archivos de imagen
        all_files = []
        for dirpath, _, filenames in os.walk(folder_path):
            for fname in sorted(filenames):
                if fname in SKIP_FILES:
                    continue
                ext = os.path.splitext(fname)[1].lower()
                if ext in IMG_EXTS:
                    all_files.append((fname, dirpath))

        # Separar ilustraciones de fotos reales
        # Clave de emparejamiento: nombre sin " (Ilustracion)" y sin extensión
        ilust_map = {}   # clave → ruta de la ilustración
        normal_map = {}  # clave → (fname, dirpath)

        for fname, dirpath in all_files:
            name_no_ext = os.path.splitext(fname)[0]
            # Detectar si es ilustración
            clean = re.sub(r'\s*[\(\-]\s*[Ii]lustracion\s*[\)\-]?\s*\d*$', '', name_no_ext).strip()
            is_ilust = clean != name_no_ext
            ruta = rel(os.path.join(dirpath, fname))
            if is_ilust:
                ilust_map[clean.lower()] = ruta
            else:
                key = name_no_ext.lower()
                normal_map[key] = (fname, dirpath, ruta)

        idx = 1
        used_ilusts = set()

        # Primero los productos con foto real
        for key, (fname, dirpath, ruta) in sorted(normal_map.items()):
            name_no_ext = os.path.splitext(fname)[0]
            gallery = [ruta]
            # Buscar ilustración correspondiente
            if key in ilust_map:
                gallery.append(ilust_map[key])
                used_ilusts.add(key)
            item = {
                "id":    f"{prefix}-{idx:03d}",
                "title": to_title(fname, folder_name),
                "cat":   slug,
                "img":   ruta,
                "size":  "-",
                "mat":   "Metal",
                "price": "-",
            }
            if len(gallery) > 1:
                item["gallery"] = gallery
            items.append(item)
            idx += 1

        # Ilustraciones sin par (no tienen foto real)
        for key, ruta in sorted(ilust_map.items()):
            if key in used_ilusts:
                continue
            fname = os.path.basename(ruta)
            item = {
                "id":    f"{prefix}-{idx:03d}",
                "title": to_title(fname, folder_name),
                "cat":   slug,
                "img":   ruta,
                "size":  "-",
                "mat":   "Metal",
                "price": "-",
            }
            items.append(item)
            idx += 1

    return items

def collect_sets():
    sets = []
    if not os.path.isdir(SET_ROOT):
        return sets
    for folder_name in sorted(os.listdir(SET_ROOT)):
        folder_path = os.path.join(SET_ROOT, folder_name)
        if not os.path.isdir(folder_path):
            continue
        images = []
        for fname in sorted(os.listdir(folder_path)):
            if fname in SKIP_FILES:
                continue
            if os.path.splitext(fname)[1].lower() in IMG_EXTS:
                images.append(rel(os.path.join(folder_path, fname)))
        if images:
            sets.append({
                "id":     re.sub(r'[^a-z0-9]', '-', folder_name.lower()),
                "label":  folder_name,
                "thumb":  images[0],
                "images": images,
            })
    return sets

def main():
    items = collect_items()
    sets  = collect_sets()
    print(f"Productos: {len(items)}")
    print(f"Sets: {len(sets)}")

    lines = [
        "// productos.js — generado por generar_productos.py",
        "// Para actualizar: python generar_productos.py",
        "",
        "const items = " + json.dumps(items, ensure_ascii=False, indent=2) + ";",
        "",
    ]

    out = os.path.join(ROOT, "productos.js")
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"Escrito: {out}")

if __name__ == '__main__':
    main()

