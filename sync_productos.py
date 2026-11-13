#!/usr/bin/env python3
"""
sync_productos.py
-----------------
Escanea las carpetas de imágenes y sincroniza productos.js.

- Las entradas que ya existen NO se tocan (precio, título, tamaño, etc. se respetan).
- Las imágenes nuevas se agregan al final de cada categoría con valores por defecto.
- Las imágenes que fueron borradas se eliminan de la lista automáticamente.

Uso:
    python sync_productos.py

Categorías y carpetas:
    ilustraciones  →  Ilustraciones/
    imanes         →  Imanes/
    letreros       →  Letreros/
    vintages       →  Vintages/
"""

import os
import re
import sys

# ── Configuración ────────────────────────────────────────────────────────────

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

CATEGORIES = [
    {
        "cat":    "ilustraciones",
        "folder": "Ilustraciones",
        "prefix": "ILU",
        "price":  "$9.990",
        "mat":    "Aluminio",
        "unit":   "1 pieza",
        "size":   "- x - cm",
    },
    {
        "cat":    "imanes",
        "folder": "Imanes",
        "prefix": "IMA",
        "price":  "$2.490",
        "mat":    "Aluminio",
        "unit":   "1 pieza",
        "size":   "- x - cm",
    },
    {
        "cat":    "letreros",
        "folder": "Letreros",
        "prefix": "LET",
        "price":  "$9.990",
        "mat":    "Aluminio",
        "unit":   "1 pieza",
        "size":   "- x - cm",
    },
    {
        "cat":    "vintages",
        "folder": "Vintages",
        "prefix": "VIN",
        "price":  "$9.990",
        "mat":    "Aluminio",
        "unit":   "1 pieza",
        "size":   "- x - cm",
    },
]

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"}

# Archivos a ignorar dentro de las carpetas (fondos, ilustraciones de apoyo, etc.)
IGNORE_PATTERNS = [
    r"(?i)fondo",
    r"(?i)ilustracion",
    r"(?i)- Ilustracion",
    r"(?i)-Ilustracion",
]

PRODUCTOS_JS = os.path.join(SCRIPT_DIR, "productos.js")

# ── Helpers ──────────────────────────────────────────────────────────────────

def should_ignore(filename):
    for pat in IGNORE_PATTERNS:
        if re.search(pat, filename):
            return True
    return False


def title_from_filename(filename):
    """Convierte 'mi-foto-bonita.jpg' → 'Mi Foto Bonita'."""
    name = os.path.splitext(filename)[0]
    name = re.sub(r"[-_]", " ", name)
    return name.title()


def parse_existing_entries(js_text):
    """
    Extrae todas las entradas del array items como dicts {img: ..., raw_line: ...}.
    Devuelve (entries_by_img, full_text).
    """
    # Extrae cada objeto {...} del array
    # Patrón: línea que contenga img:"..."
    pattern = re.compile(
        r'\{[^{}]*?img\s*:\s*"([^"]+)"[^{}]*?\}',
        re.DOTALL,
    )
    entries = {}
    for m in pattern.finditer(js_text):
        img_val = m.group(1)
        # Normalizar separadores
        img_key = img_val.replace("\\", "/")
        entries[img_key] = m.group(0)
    return entries


def next_id(prefix, existing_ids):
    """Genera el siguiente ID correlativo para un prefijo dado."""
    nums = []
    for eid in existing_ids:
        m = re.match(rf"^{re.escape(prefix)}-0*(\d+)$", eid)
        if m:
            nums.append(int(m.group(1)))
    next_num = max(nums, default=0) + 1
    # Formato: ILU-01, ILU-02 … ILU-99, ILU-100
    if next_num < 100:
        return f"{prefix}-{next_num:02d}"
    return f"{prefix}-{next_num}"


def build_new_entry(cfg, img_path, new_id, title):
    """Construye la línea JS para un producto nuevo."""
    img_js = img_path.replace("\\", "/")
    return (
        f'  {{id:"{new_id}", title:"{title}", cat:"{cfg["cat"]}", '
        f'size:"{cfg["size"]}", mat:"{cfg["mat"]}", unit:"{cfg["unit"]}", '
        f'price:"{cfg["price"]}", img:"{img_js}"}}, // AUTO'
    )


def get_images_in_folder(folder_path):
    """Lista imágenes en la carpeta (sin subdirectorios) que no están ignoradas."""
    images = []
    if not os.path.isdir(folder_path):
        return images
    for fname in sorted(os.listdir(folder_path)):
        ext = os.path.splitext(fname)[1].lower()
        if ext not in IMAGE_EXTENSIONS:
            continue
        if should_ignore(fname):
            continue
        images.append(fname)
    return images


# ── Lectura del archivo actual ───────────────────────────────────────────────

def read_js():
    if not os.path.exists(PRODUCTOS_JS):
        return "// PRODUCTOS\nconst items = [\n\n];\n"
    with open(PRODUCTOS_JS, "r", encoding="utf-8") as f:
        return f.read()


def write_js(text):
    with open(PRODUCTOS_JS, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


# ── Lógica principal ─────────────────────────────────────────────────────────

def sync():
    js_text = read_js()
    existing = parse_existing_entries(js_text)

    # Recolectar todas las imágenes vigentes en disco
    valid_imgs = set()
    new_lines_by_cat = {}  # cat → list of new JS lines

    # Recolectar IDs existentes para generar los nuevos correlativamente
    all_ids = re.findall(r'id\s*:\s*"([^"]+)"', js_text)

    for cfg in CATEGORIES:
        folder_path = os.path.join(SCRIPT_DIR, cfg["folder"])
        images = get_images_in_folder(folder_path)
        new_lines_by_cat[cfg["cat"]] = []

        for fname in images:
            img_key = f"{cfg['folder']}/{fname}"
            valid_imgs.add(img_key)

            if img_key not in existing:
                # Imagen nueva → generar entrada
                new_id = next_id(cfg["prefix"], all_ids)
                all_ids.append(new_id)
                title = title_from_filename(fname)
                line = build_new_entry(cfg, img_key, new_id, title)
                new_lines_by_cat[cfg["cat"]].append(line)
                print(f"  + {new_id}  {img_key}")

    # Eliminar entradas cuya imagen ya no existe
    removed = [img for img in existing if img not in valid_imgs]
    for img in removed:
        print(f"  - Eliminado (imagen no encontrada): {img}")

    if not any(new_lines_by_cat.values()) and not removed:
        print("Sin cambios. productos.js está actualizado.")
        return

    # Reconstruir el JS: eliminar entradas obsoletas y agregar las nuevas
    # 1. Remover líneas de imágenes eliminadas
    for img in removed:
        raw = existing[img]
        # Elimina la entrada completa (incluyendo coma y posible comentario al final)
        js_text = js_text.replace(raw + ",", "", 1)
        js_text = js_text.replace(raw, "", 1)

    # 2. Agregar nuevas entradas agrupadas por categoría
    for cfg in CATEGORIES:
        cat = cfg["cat"]
        new_lines = new_lines_by_cat.get(cat, [])
        if not new_lines:
            continue

        # Busca el comentario de sección, e.g. // ── LETREROS
        section_comment = f"// ── {cfg['folder'].upper()}"
        alt_comment     = f"// ── {cat.upper()}"

        # Encuentra la última entrada de esta categoría para insertar justo después
        # Busca todas las ocurrencias de cat:"<cat>" y ubica la última
        cat_pattern = re.compile(rf'cat\s*:\s*"{re.escape(cat)}"')
        last_match = None
        for m in cat_pattern.finditer(js_text):
            last_match = m

        if last_match:
            # Encuentra el cierre } de esa entrada
            close_pos = js_text.find("}", last_match.end())
            if close_pos == -1:
                close_pos = len(js_text) - 1
            insert_pos = close_pos + 1
            # Incluye una coma si no hay una después
            tail = js_text[insert_pos:insert_pos + 3].lstrip()
            insertion = ",\n" + "\n".join(new_lines)
            js_text = js_text[:insert_pos] + insertion + js_text[insert_pos:]
        else:
            # No hay entradas de esta categoría todavía: busca la sección o inserta al final
            section_pos = js_text.find(section_comment)
            if section_pos == -1:
                section_pos = js_text.find(alt_comment)

            if section_pos != -1:
                # Inserta después del comentario de sección
                eol = js_text.find("\n", section_pos)
                insert_pos = eol + 1 if eol != -1 else section_pos + len(section_comment)
                insertion = "\n".join(new_lines) + "\n"
                js_text = js_text[:insert_pos] + insertion + js_text[insert_pos:]
            else:
                # No hay sección: agrega antes del cierre del array
                close_bracket = js_text.rfind("];")
                if close_bracket == -1:
                    close_bracket = js_text.rfind("]")
                header = f"\n  // ── {cfg['folder'].upper()}\n"
                insertion = header + "\n".join(new_lines) + "\n\n"
                js_text = js_text[:close_bracket] + insertion + js_text[close_bracket:]

    write_js(js_text)
    total_new = sum(len(v) for v in new_lines_by_cat.values())
    print(f"\nproductos.js actualizado: {total_new} producto(s) nuevo(s), {len(removed)} eliminado(s).")


if __name__ == "__main__":
    print("Sincronizando productos.js con las carpetas de imágenes...\n")
    sync()
