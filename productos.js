// ============================================================
//  PRODUCTOS — editá este archivo para cambiar nombres,
//  tamaños, precios y materiales.
// ============================================================

const items = [

  // ── ILUSTRACIONES ──────────────────────────────────────────
  // 736x920  ratio 0.8 → vertical estándar → 19x27
  {id:"ILU-01", title:"Monstera Acuarela",          cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/1020135753088033663.jpg"},
  // 736x1104 ratio 0.67 → vertical → 19x27
  {id:"ILU-02", title:"Plantas en Macetas",          cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/1086845322608525041.jpg"},
  // 736x1308 ratio 0.56 → vertical alta → 19x27
  {id:"ILU-03", title:"Utensilios de Cocina",        cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/358458451615405470.jpg"},
  // 736x1308 ratio 0.56 → vertical alta → 19x27
  {id:"ILU-04", title:"Puerta Griega",               cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/493214596717288546.jpg"},
  // 668x1175 ratio 0.57 → vertical → 19x27
  {id:"ILU-05", title:"Abstracto Boho",              cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/536702480617538331.jpg"},
  // 736x738  ratio ~1:1 → cuadrada → 19x13,5
  {id:"ILU-06", title:"Home Sweet Home",             cat:"ilustraciones", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Ilustraciones/565131453256664327.jpg"},
  // 736x1104 ratio 0.67 → vertical → 19x27
  {id:"ILU-07", title:"Casas Coloridas",             cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/592364157279093917.jpg"},
  // 736x1104 ratio 0.67 → vertical → 19x27
  {id:"ILU-08", title:"Mate Café Té",                cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/677369600242559565.jpg"},
  // 675x1200 ratio 0.56 → vertical alta → 19x27
  {id:"ILU-09", title:"Limones Tablero",             cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/714524297181267724.jpg"},
  // 736x1104 ratio 0.67 → vertical → 19x27
  {id:"ILU-10", title:"Flores Línea Rosa",           cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/728246202290644519.jpg"},
  // 675x1200 ratio 0.56 → muy vertical → 9,5x27,5
  {id:"ILU-11", title:"HOME Letras Botánicas",       cat:"ilustraciones", size:"9,5 x 27,5 cm",mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Ilustraciones/748090188164412187.jpg"},
  // 736x1050 ratio 0.70 → vertical → 19x27
  {id:"ILU-12", title:"Margarita Retro",             cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/796785359111590823.jpg"},
  // 736x1308 ratio 0.56 → vertical → 19x27
  {id:"ILU-13", title:"Gatos Sol y Luna",            cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/813322014000491564.jpg"},
  // 736x1308 ratio 0.56 → vertical → 19x27
  {id:"ILU-14", title:"Bouquet Floral",              cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/859835753923146306.jpg"},
  // 303x415  ratio 0.73 → vertical → 19x27
  {id:"ILU-15", title:"Gato en la Bañera",           cat:"ilustraciones", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Ilustraciones/86454ea017a48fb06beef47c1a4e895a.jpg"},
  // 736x1288 ratio 0.57 → vertical → 19x27
  {id:"ILU-16", title:"Planta de Ajíes",             cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/872079915370304934.jpg"},
  {id:"ILU-17", title:"Argentinidad",                cat:"ilustraciones", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Ilustraciones/argentinidad.jpg"},
  {id:"ILU-18", title:"Bolsas con Frases",           cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/bolsas-con-frases.jpg"},
  {id:"ILU-19", title:"Cat 11",                      cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/cat-11.jpg"},
  {id:"ILU-20", title:"Cuadros Hojas",               cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/cuadros-hojas.jpg"},
  // 736x1040 ratio 0.71 → vertical → 19x27
  {id:"ILU-21", title:"Cerezas Tablero",             cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/download (1).jpg"},
  // 736x968  ratio 0.76 → vertical → 19x27
  {id:"ILU-22", title:"Home Sweet Home Rosas",       cat:"ilustraciones", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Ilustraciones/download (2).jpg"},
  // 735x1268 ratio 0.58 → vertical → 19x27
  {id:"ILU-23", title:"Monstera 1763",               cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/download (3).jpg"},
  // 736x1308 ratio 0.56 → vertical → 19x27
  {id:"ILU-24", title:"Pasta Italia",                cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/download (4).jpg"},
  // 735x1040 ratio 0.71 → vertical → 19x27
  {id:"ILU-25", title:"Limoncello",                  cat:"ilustraciones", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Ilustraciones/download.jpg"},
  // 556x791  ratio 0.70 → vertical → 19x27
  {id:"ILU-26", title:"Lavanda y Vino",              cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/ebbf07f604398c3793ace513cfd973cc.jpg"},
  {id:"ILU-27", title:"Es todo lo que voy a decir",  cat:"ilustraciones", size:"9,5 x 27,5 cm",mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Ilustraciones/es-todo-lo-que-voy-a-decir.jpg"},
  {id:"ILU-28", title:"Floral Typography",           cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/floral-typography.jpg"},
  {id:"ILU-29", title:"Acuarela Otoñal",             cat:"ilustraciones", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Ilustraciones/acuarela-otonal.jpg"},
  {id:"ILU-30", title:"Colores y Relatos",           cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/colores-relatos.jpg"},
  {id:"ILU-31", title:"Lemon Vase",                  cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/lemon-vase.jpg"},
  {id:"ILU-32", title:"Botanical",                   cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/botanical.jpg"},
  {id:"ILU-33", title:"Sun",                         cat:"ilustraciones", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Ilustraciones/sun.jpg"},
  {id:"ILU-34", title:"Van Gogh",                    cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/van-gogh.jpg"},
  {id:"ILU-35", title:"Ilustración W",               cat:"ilustraciones", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Ilustraciones/W.jpg"},

  // ── IMANES ────────────────────────────────────────────────
  // {id:"IMA-01", title:"Imán Pequeño",      cat:"imanes", size:"9,5 x 27,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Imanes/ima-01.jpg"},
  // {id:"IMA-02", title:"Imán Mediano",      cat:"imanes", size:"19 x 9,5 cm",   mat:"Aluminio", unit:"1 pieza", price:"$4.000", img:"Imanes/ima-02.jpg"},
  // {id:"IMA-03", title:"Imán Mediano Plus", cat:"imanes", size:"19 x 13,5 cm",  mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Imanes/ima-03.jpg"},
  // {id:"IMA-04", title:"Imán Grande",       cat:"imanes", size:"19 x 27 cm",    mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Imanes/ima-04.jpg"},

  // ── LETREROS ──────────────────────────────────────────────
  // 720x1040 ratio 0.69 → vertical → 19x27
  {id:"LET-01", title:"Número de Casa",              cat:"letreros", size:"9,5 x 27,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Letreros/011.jpg"},
  // 1670x3477 ratio 0.48 → muy vertical angosta → 9,5x27,5
  {id:"LET-02", title:"Prohibido Estacionar 24hs",   cat:"letreros", size:"9,5 x 27,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Letreros/016.jpg"},
  // 540x540 ratio 1:1 → cuadrada → 19x13,5
  {id:"LET-03", title:"Baños Dama y Caballero",      cat:"letreros", size:"19 x 13,5 cm",  mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Letreros/021.jpg"},
  // 777x478 ratio 1.6 → horizontal → 19x9,5
  {id:"LET-04", title:"STOP Vintage",                cat:"letreros", size:"19 x 13,5 cm",  mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Letreros/024.jpg"},
  // 700x1043 ratio 0.67 → vertical → 19x27
  {id:"LET-05", title:"Wi-Fi Vintage",               cat:"letreros", size:"19 x 13,5 cm",  mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Letreros/5fcb721bf443a38e4c2bcad2f650a497.jpg"},

  // ── VINTAGES ──────────────────────────────────────────────
  // 863x1248 ratio 0.69 → vertical → 19x27
  {id:"VIN-01", title:"Las Malvinas Son Argentinas", cat:"vintages", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Vintages/001.jpg"},
  // 1200x895 ratio 1.34 → horizontal → 19x13,5
  {id:"VIN-02", title:"Argentina 3 Estrellas",       cat:"vintages", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/002.jpg"},
  // 540x674 ratio 0.80 → vertical → 19x27
  {id:"VIN-03", title:"La Renga Ruta 73",            cat:"vintages", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Vintages/003.jpg"},
  // 1044x204 ratio 5.1 → muy horizontal → 19x9,5
  {id:"VIN-04", title:"A Brillar Mi Amor",           cat:"vintages", size:"19 x 9,5 cm",  mat:"Aluminio", unit:"1 pieza", price:"$4.000", img:"Vintages/004.jpg"},
  // 1039x279 ratio 3.7 → muy horizontal → 19x9,5
  {id:"VIN-05", title:"Corona Extra",                cat:"vintages", size:"19 x 9,5 cm",  mat:"Aluminio", unit:"1 pieza", price:"$4.000", img:"Vintages/005.jpg"},
  // 996x720 ratio 1.38 → horizontal → 19x13,5
  {id:"VIN-06", title:"Ford Authorized Service",     cat:"vintages", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/006.jpg"},
  // 720x730 ratio ~1:1 → cuadrada → 19x13,5
  {id:"VIN-07", title:"Intoxicados Planeta Tierra",  cat:"vintages", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/007.jpg"},
  // 554x1041 ratio 0.53 → vertical → 19x27
  {id:"VIN-08", title:"Jack Daniel's Whiskey",       cat:"vintages", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Vintages/008.jpg"},
  // 720x1040 ratio 0.69 → vertical → 19x27
  {id:"VIN-09", title:"República Argentina",         cat:"vintages", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Vintages/012.jpg"},
  // 1040x512 ratio 2.03 → horizontal → 19x9,5
  {id:"VIN-10", title:"California Outatime",         cat:"vintages", size:"19 x 9,5 cm",  mat:"Aluminio", unit:"1 pieza", price:"$4.000", img:"Vintages/013.jpg"},
  // 932x720 ratio 1.29 → horizontal → 19x13,5
  {id:"VIN-11", title:"Las Malvinas Son Argentinas (mapa)", cat:"vintages", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/014.jpg"},
  // 1000x720 ratio 1.39 → horizontal → 19x13,5
  {id:"VIN-12", title:"Junta Nacional de Carnes",    cat:"vintages", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/015.jpg"},
  // 1040x384 ratio 2.7 → muy horizontal → 19x9,5
  {id:"VIN-13", title:"Toilette",                    cat:"vintages", size:"19 x 9,5 cm",  mat:"Aluminio", unit:"1 pieza", price:"$4.000", img:"Vintages/017.jpg"},
  // 502x1024 ratio 0.49 → vertical alta → 19x27
  {id:"VIN-14", title:"Ningún Mar en Calma",         cat:"vintages", size:"19 x 9,5 cm",  mat:"Aluminio", unit:"1 pieza", price:"$4.000", img:"Vintages/019.jpg"},
  // 1040x283 ratio 3.67 → muy horizontal → 19x9,5
  {id:"VIN-15", title:"No Hay Nada Mejor que Casa",  cat:"vintages", size:"9,5 x 27,5 cm",mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/025.jpg"},
  // 738x375 ratio 1.97 → horizontal → 19x9,5
  {id:"VIN-16", title:"Mantenga Hidratado al Parrillero", cat:"vintages", size:"19 x 9,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$4.000", img:"Vintages/026.jpg"},
  // 720x723 ratio ~1:1 → cuadrada → 19x13,5
  {id:"VIN-17", title:"Baño Floral",                 cat:"vintages", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/32.jpg"},
  // 720x726 ratio ~1:1 → cuadrada → 19x13,5
  {id:"VIN-18", title:"Bagno",                       cat:"vintages", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/33.jpg"},
  // 257x1037 ratio 0.25 → muy angosta → 9,5x27,5
  {id:"VIN-19", title:"Ginebra Bols",                cat:"vintages", size:"9,5 x 27,5 cm",mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/34.jpg"},
  // 724x542 ratio 1.34 → horizontal → 19x13,5
  {id:"VIN-20", title:"Un Aplauso para el Asador",   cat:"vintages", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/35.jpg"},
  // 722x539 ratio 1.34 → horizontal → 19x13,5
  {id:"VIN-21", title:"El Mejor Asado Se Come Acá",  cat:"vintages", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/37.jpg"},
  // 720x956 ratio 0.75 → vertical → 19x27
  {id:"VIN-22", title:"Tome Coca-Cola",              cat:"vintages", size:"19 x 27 cm",   mat:"Aluminio", unit:"1 pieza", price:"$8.000", img:"Vintages/38.jpg"},
  // 721x541 ratio 1.33 → horizontal → 19x13,5
  {id:"VIN-23", title:"Indian Motorcycle 1934",      cat:"vintages", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/Imagen27.jpg"},
  // 780x540 ratio 1.44 → horizontal → 19x13,5
  {id:"VIN-24", title:"Open 24 Hours",               cat:"vintages", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/Imagen28.jpg"},
  // 1044x698 ratio 1.50 → horizontal → 19x13,5
  {id:"VIN-25", title:"Barra",                       cat:"vintages", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/Imagen29.jpg"},
  // 1040x724 ratio 1.44 → horizontal → 19x13,5
  {id:"VIN-26", title:"Asado Vino y Amigos",         cat:"vintages", size:"19 x 13,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Vintages/Imagen30.jpg"},

];
