"""
calcular_precios.py
===================
Recorre todas las imágenes de productos, calcula el tamaño óptimo de impresión
para cada zona (Grande / Mediano / Chico) y actualiza el campo `sizes` de cada
item en productos.js.

Uso:
    python calcular_precios.py

Requisitos:
    pip install Pillow
"""

from PIL import Image
import os, json, re

# ══════════════════════════════════════════════════════════════
#  CONFIGURACIÓN — ajustá estos valores cuando necesites
# ══════════════════════════════════════════════════════════════

# Área de impresión de cada zona en mm (ancho x alto)
# Basado en Epson L1250, A4 con márgenes de 3 mm cada lado
ZONAS = [
    # nombre   ancho  alto   precio_min  precio_max
    ("Grande",  204,   291,   11990,      17990),
    ("Mediano", 204,   142,    5990,      10990),
    ("Chico",    99,   291,    3490,       6990),
]

# Precio promedio objetivo para el tamaño Grande (ancla de la fórmula)
PRECIO_PROMEDIO_GRANDE = 14990

# Redondeo de precios (en pesos). 100 = redondea a centenas.
REDONDEO = 100

# ══════════════════════════════════════════════════════════════
#  RUTAS — no hace falta tocar esto normalmente
# ══════════════════════════════════════════════════════════════

BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
IMAGENES_DIR  = os.path.join(BASE_DIR, "Tienda (Imagenes)", "Categorias")
PRODUCTOS_JS  = os.path.join(BASE_DIR, "productos.js")

# ══════════════════════════════════════════════════════════════
#  LÓGICA
# ══════════════════════════════════════════════════════════════

def mejor_encaje(w_px, h_px, area_w_mm, area_h_mm):
    """
    Devuelve (ancho_cm, alto_cm, area_cm2) del encaje óptimo
    probando orientación normal y rotada del área de impresión.
    """
    best_rw = best_rh = best_area = 0
    for pa, pb in [(area_w_mm, area_h_mm), (area_h_mm, area_w_mm)]:
        scale = min(pa / w_px, pb / h_px)
        rw = round(w_px * scale / 10, 1)
        rh = round(h_px * scale / 10, 1)
        a  = rw * rh
        if a > best_area:
            best_area = a
            best_rw, best_rh = rw, rh
    return best_rw, best_rh, best_area


def calcular_precio_x_cm2():
    """
    Calcula el precio por cm² usando el área promedio de todos los
    productos en tamaño Grande y el precio promedio objetivo.
    """
    nombre_grande, aw, ah, _, _ = ZONAS[0]
    areas = []
    for root, _, files in os.walk(IMAGENES_DIR):
        for f in files:
            if "(Ilustracion)" in f:
                continue
            if not f.lower().endswith((".webp", ".png", ".jpg", ".jpeg")):
                continue
            path = os.path.join(root, f)
            try:
                with Image.open(path) as img:
                    w, h = img.size
                _, _, area = mejor_encaje(w, h, aw, ah)
                areas.append(area)
            except Exception:
                pass
    if not areas:
        raise RuntimeError("No se encontraron imágenes en " + IMAGENES_DIR)
    promedio = sum(areas) / len(areas)
    precio_x_cm2 = PRECIO_PROMEDIO_GRANDE / promedio
    return precio_x_cm2, len(areas), round(promedio, 1)


def calcular_sizes_por_imagen(precio_x_cm2):
    """
    Recorre todas las imágenes y devuelve un dict:
        { "ruta/relativa.webp": [ {label, dims, price}, ... ] }
    """
    img_sizes = {}
    errores = []

    for root, _, files in os.walk(IMAGENES_DIR):
        for f in files:
            if "(Ilustracion)" in f:
                continue
            if not f.lower().endswith((".webp", ".png", ".jpg", ".jpeg")):
                continue
            path = os.path.join(root, f)
            try:
                with Image.open(path) as img:
                    w, h = img.size
                rel = os.path.relpath(path, BASE_DIR).replace("\\", "/")
                sizes = []
                for label, aw, ah, min_p, max_p in ZONAS:
                    rw, rh, area = mejor_encaje(w, h, aw, ah)
                    raw   = area * precio_x_cm2
                    price = max(min_p, min(max_p, round(raw / REDONDEO) * REDONDEO))
                    sizes.append({
                        "label": label,
                        "dims":  str(rw) + " x " + str(rh) + " cm",
                        "price": price,
                    })
                img_sizes[rel] = sizes
            except Exception as e:
                errores.append(path + " — " + str(e))

    return img_sizes, errores


def actualizar_productos_js(img_sizes):
    """
    Lee productos.js, agrega/actualiza el campo `sizes` en cada item
    y sobreescribe el archivo.
    """
    with open(PRODUCTOS_JS, encoding="utf-8") as f:
        content = f.read()

    match = re.search(r"const items\s*=\s*(\[.*\])\s*;?\s*$", content, re.DOTALL)
    if not match:
        raise RuntimeError("No se encontró el array 'items' en productos.js")

    items = json.loads(match.group(1))

    actualizados = 0
    sin_imagen   = []

    for item in items:
        img_key = item.get("img", "").replace("\\", "/")
        if img_key in img_sizes:
            item["sizes"] = img_sizes[img_key]
            actualizados += 1
        else:
            sin_imagen.append(item.get("id", "?") + " — " + img_key)

    header      = content[: match.start()]
    new_content = header + "const items = " + json.dumps(items, ensure_ascii=False, indent=2) + ";\n"

    with open(PRODUCTOS_JS, "w", encoding="utf-8") as f:
        f.write(new_content)

    return actualizados, sin_imagen


# ══════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 55)
    print("  calcular_precios.py")
    print("=" * 55)

    print("\n1. Calculando precio por cm²...")
    precio_x_cm2, total_imgs, area_prom = calcular_precio_x_cm2()
    print("   Imágenes analizadas : " + str(total_imgs))
    print("   Área promedio Grande: " + str(area_prom) + " cm²")
    print("   Precio por cm²      : $" + str(round(precio_x_cm2, 4)))

    print("\n2. Calculando tamaños y precios por producto...")
    img_sizes, errores = calcular_sizes_por_imagen(precio_x_cm2)
    print("   Imágenes mapeadas   : " + str(len(img_sizes)))
    if errores:
        print("   Errores             : " + str(len(errores)))
        for e in errores[:5]:
            print("     " + e)

    print("\n3. Actualizando productos.js...")
    actualizados, sin_imagen = actualizar_productos_js(img_sizes)
    print("   Items actualizados  : " + str(actualizados))
    if sin_imagen:
        print("   Sin imagen mapeada  : " + str(len(sin_imagen)))
        for s in sin_imagen[:5]:
            print("     " + s)

    print("\n4. Muestra de resultados:")
    muestra_keys = list(img_sizes.keys())
    for key in [muestra_keys[0], muestra_keys[100], muestra_keys[500]]:
        print("   " + key)
        for s in img_sizes[key]:
            print("     " + s["label"] + ": " + s["dims"] + " — $" + str(s["price"]))

    print("\n✓ productos.js actualizado correctamente.")
    print("=" * 55)
