"""
scraper_clubdelposter.py
Descarga imágenes y nombres de productos desde Club del Poster.
Usa Selenium para renderizar el JS del sitio.

Uso:
  python scraper_clubdelposter.py <url_categoria> <carpeta_destino> [--todas]

Ejemplo — una página:
  python scraper_clubdelposter.py "https://www.clubdelposter.com/carteles-de-chapa/dias-especiales/" "Tienda (Imagenes)/Categorias/Dias Especiales"

Ejemplo — todas las páginas:
  python scraper_clubdelposter.py "https://www.clubdelposter.com/carteles-de-chapa/dias-especiales/" "Tienda (Imagenes)/Categorias/Dias Especiales" --todas
"""

import os, re, sys, time, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))

def safe_filename(name):
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name[:120]

def download_image(url, dest_path):
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
    with open(dest_path, 'wb') as f:
        f.write(data)

def scrape_with_selenium(url, out_dir):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager

    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    opts.add_argument('--window-size=1920,1080')
    opts.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

    service = Service(ChromeDriverManager().install())
    driver  = webdriver.Chrome(service=service, options=opts)

    downloaded = 0
    try:
        print(f"  Abriendo: {url}")
        driver.get(url)
        # Esperar que carguen los productos
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product, .product-item, article'))
        )
        time.sleep(2)  # dar tiempo al JS

        time.sleep(5)

        # Scroll infinito — seguir scrolleando hasta que no aparezcan más productos
        print("  Cargando todos los productos (scroll infinito)...")
        last_count = 0
        stall_count = 0
        while stall_count < 3:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            html = driver.page_source
            current = len(re.findall(r'srcset=["\'][^"\']+/products/[^"\']+["\']', html))
            print(f"    Productos detectados: {current}")
            if current == last_count:
                stall_count += 1
            else:
                stall_count = 0
            last_count = current

        html = driver.page_source

        # Buscar todos los elementos img con srcset en el HTML
        # Patrón más robusto: captura cualquier tag img completo
        img_tags = re.findall(r'<img\s[^>]+>', html, re.DOTALL | re.IGNORECASE)

        seen_names = set()
        downloaded = 0

        for tag in img_tags:
            # Extraer alt
            alt_m = re.search(r'alt=["\']([^"\']*)["\']', tag, re.IGNORECASE)
            alt   = alt_m.group(1).strip() if alt_m else ''

            # Extraer srcset
            ss_m  = re.search(r'srcset=["\']([^"\']+)["\']', tag, re.IGNORECASE)
            srcset = ss_m.group(1) if ss_m else ''

            # Extraer src como fallback
            src_m = re.search(r'\bsrc=["\']([^"\']+)["\']', tag, re.IGNORECASE)
            src   = src_m.group(1) if src_m else ''

            # Elegir mejor URL
            best = ''
            if srcset:
                urls = [u.strip().split(' ')[0] for u in srcset.split(',') if u.strip()]
                # Preferir 1024x1024
                best = next((u for u in reversed(urls) if '1024' in u), urls[-1] if urls else '')
            if not best and src and 'data:image' not in src:
                best = src

            if not best or '/products/' not in best:
                continue
            if best.startswith('//'):
                best = 'https:' + best
            if best.startswith('/') and not best.startswith('//'):
                best = 'https://acdn-us.mitiendanube.com' + best

            if not alt:
                continue

            name = safe_filename(alt)
            if name in seen_names:
                continue
            seen_names.add(name)

            ext = os.path.splitext(urllib.parse.urlparse(best).path)[1].lower()
            if ext not in ('.jpg', '.jpeg', '.png', '.webp'):
                ext = '.webp'

            dest = os.path.join(out_dir, name + ext)
            if os.path.exists(dest):
                print(f"    Ya existe: {name}{ext}")
                continue

            try:
                download_image(best, dest)
                print(f"    ✅ {name}{ext}")
                downloaded += 1
            except Exception as e:
                print(f"    ❌ {name}: {e}")
            time.sleep(0.2)

    finally:
        driver.quit()

    return downloaded

def get_total_pages(url):
    """Detecta cuántas páginas tiene la categoría leyendo el HTML inicial."""
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    driver  = webdriver.Chrome(service=service, options=opts)
    try:
        driver.get(url)
        time.sleep(3)
        html = driver.page_source
    finally:
        driver.quit()

    matches = re.findall(r'mpage=(\d+)', html)
    return max((int(m) for m in matches), default=1)

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)

    base_url = args[0].rstrip('/')
    out_dir  = os.path.join(ROOT, args[1])
    todas    = '--todas' in args

    os.makedirs(out_dir, exist_ok=True)
    print(f"Destino: {out_dir}\n")

    total = 0

    if todas:
        max_pages = get_total_pages(base_url + '/')
        print(f"Páginas detectadas: {max_pages}\n")
        for page in range(1, max_pages + 1):
            url = base_url + '/' if page == 1 else f"{base_url}/?mpage={page}"
            n   = scrape_with_selenium(url, out_dir)
            total += n
            print(f"  Página {page}/{max_pages}: {n} descargadas\n")
    else:
        total = scrape_with_selenium(base_url + '/', out_dir)

    print(f"\n{'='*50}")
    print(f"Total descargadas: {total} imágenes en '{out_dir}'")
    print("Ahora corré: python generar_productos.py")

if __name__ == '__main__':
    main()
