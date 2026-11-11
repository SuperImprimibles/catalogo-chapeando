// ============================================================
//  PRODUCTOS
//  - Ilustraciones y Vintages: size:"-" â†’ el tamaÃ±o se calcula
//    automÃ¡ticamente segÃºn proporciÃ³n real de la imagen
//  - Letreros e Imanes: size fijo
// ============================================================

const items = [

  // â”€â”€ ILUSTRACIONES â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  {id:"ILU-01", title:"Monstera Acuarela",          cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/monstera-acuarela.jpg"},
  {id:"ILU-02", title:"Plantas en Macetas",          cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/plantas-en-macetas.jpg"},
  {id:"ILU-03", title:"Utensilios de Cocina",        cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/utensilios-de-cocina.jpg"},
  {id:"ILU-04", title:"Puerta Griega",               cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/puerta-griega.jpg"},
  {id:"ILU-05", title:"Abstracto Boho",              cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/abstracto-boho.jpg"},
  {id:"ILU-06", title:"Home Sweet Home",             cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/home-sweet-home.jpg"},
  {id:"ILU-07", title:"Casas Coloridas",             cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/casas-coloridas.jpg"},
  {id:"ILU-08", title:"Mate CafÃ© TÃ©",                cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/mate-cafe-te.jpg"},
  {id:"ILU-09", title:"Limones Tablero",             cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/limones-tablero.jpg"},
  {id:"ILU-10", title:"Flores LÃ­nea Rosa",           cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/flores-linea-rosa.jpg"},
  {id:"ILU-11", title:"HOME Letras BotÃ¡nicas",       cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/home-letras-botanicas.jpg"},
  {id:"ILU-12", title:"Margarita Retro",             cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/margarita-retro.jpg"},
  {id:"ILU-13", title:"Gatos Sol y Luna",            cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/gatos-sol-luna.jpg"},
  {id:"ILU-14", title:"Bouquet Floral",              cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/bouquet-floral.jpg"},
  {id:"ILU-15", title:"Gato en la BaÃ±era",           cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/gato-en-banera.jpg"},
  {id:"ILU-16", title:"Planta de AjÃ­es",             cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/planta-de-ajies.jpg"},
  {id:"ILU-17", title:"Argentinidad",                cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/argentinidad.jpg"},
  {id:"ILU-18", title:"Bolsas con Frases",           cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/bolsas-con-frases.jpg"},
  {id:"ILU-19", title:"Cat 11",                      cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/cat-11.jpg"},
  {id:"ILU-20", title:"Cuadros Hojas",               cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/cuadros-hojas.jpg"},
  {id:"ILU-21", title:"Cerezas Tablero",             cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/cerezas-tablero.jpg"},
  {id:"ILU-22", title:"Home Sweet Home Rosas",       cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/home-sweet-home-rosas.jpg"},
  {id:"ILU-23", title:"Monstera 1763",               cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/monstera-1763.jpg"},
  {id:"ILU-24", title:"Pasta Italia",                cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/pasta-italia.jpg"},
  {id:"ILU-25", title:"Limoncello",                  cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/limoncello.jpg"},
  {id:"ILU-26", title:"Lavanda y Vino",              cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/lavanda-y-vino.jpg"},
  {id:"ILU-27", title:"Es todo lo que voy a decir",  cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/es-todo-lo-que-voy-a-decir.jpg"},
  {id:"ILU-28", title:"Floral Typography",           cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/floral-typography.jpg"},
  {id:"ILU-29", title:"Acuarela OtoÃ±al",             cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/acuarela-otonal.jpg"},
  {id:"ILU-30", title:"Colores y Relatos",           cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/colores-relatos.jpg"},
  {id:"ILU-31", title:"Lemon Vase",                  cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/lemon-vase.jpg"},
  {id:"ILU-32", title:"Botanical",                   cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/botanical.jpg"},
  {id:"ILU-33", title:"Sun",                         cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/sun.jpg"},
  {id:"ILU-34", title:"Van Gogh",                    cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/van-gogh.jpg"},
  {id:"ILU-35", title:"IlustraciÃ³n W",               cat:"ilustraciones", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Ilustraciones/W.jpg"},

  // â”€â”€ IMANES â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  // TamaÃ±o calculado automÃ¡ticamente (mÃ¡x 8cm de alto)


  // â”€â”€ LETREROS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  {id:"LET-01", title:"NÃºmero de Casa",              cat:"letreros", size:"9,5 x 27,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Letreros/numero-de-casa.jpg"},
  {id:"LET-02", title:"Prohibido Estacionar 24hs",   cat:"letreros", size:"9,5 x 27,5 cm", mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Letreros/prohibido-estacionar.jpg"},
  {id:"LET-03", title:"BaÃ±os Dama y Caballero",      cat:"letreros", size:"19 x 13,5 cm",  mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Letreros/banos-dama-caballero.jpg"},
  {id:"LET-04", title:"STOP Vintage",                cat:"letreros", size:"19 x 13,5 cm",  mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Letreros/stop-vintage.jpg"},
  {id:"LET-05", title:"Wi-Fi Vintage",               cat:"letreros", size:"19 x 13,5 cm",  mat:"Aluminio", unit:"1 pieza", price:"$5.000", img:"Letreros/wifi-vintage.jpg"},

  // â”€â”€ VINTAGES â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  {id:"VIN-01", title:"Las Malvinas Son Argentinas", cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/malvinas-son-argentinas-texto.jpg"},
  {id:"VIN-02", title:"Argentina 3 Estrellas",       cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/argentina-3-estrellas.jpg"},
  {id:"VIN-03", title:"La Renga Ruta 73",            cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/la-renga-ruta-73.jpg"},
  {id:"VIN-04", title:"A Brillar Mi Amor",           cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/a-brillar-mi-amor.jpg"},
  {id:"VIN-05", title:"Corona Extra",                cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/corona-extra.jpg"},
  {id:"VIN-06", title:"Ford Authorized Service",     cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/ford-authorized-service.jpg"},
  {id:"VIN-07", title:"Intoxicados Planeta Tierra",  cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/intoxicados-planeta-tierra.jpg"},
  {id:"VIN-08", title:"Jack Daniel's Whiskey",       cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/jack-daniels-whiskey.jpg"},
  {id:"VIN-09", title:"RepÃºblica Argentina",         cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/republica-argentina.jpg"},
  {id:"VIN-10", title:"California Outatime",         cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/california-outatime.jpg"},
  {id:"VIN-11", title:"Las Malvinas Son Argentinas (mapa)", cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/malvinas-son-argentinas-mapa.jpg"},
  {id:"VIN-12", title:"Junta Nacional de Carnes",    cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/junta-nacional-de-carnes.jpg"},
  {id:"VIN-13", title:"Toilette",                    cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/toilette.jpg"},
  {id:"VIN-14", title:"NingÃºn Mar en Calma",         cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/ningun-mar-en-calma.jpg"},
  {id:"VIN-15", title:"No Hay Nada Mejor que Casa",  cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/no-hay-nada-mejor-que-casa.jpg"},
  {id:"VIN-16", title:"Mantenga Hidratado al Parrillero", cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/mantenga-hidratado-al-parrillero.jpg"},
  {id:"VIN-17", title:"BaÃ±o Floral",                 cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/bano-floral.jpg"},
  {id:"VIN-18", title:"Bagno",                       cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/bagno.jpg"},
  {id:"VIN-19", title:"Ginebra Bols",                cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/ginebra-bols.jpg"},
  {id:"VIN-20", title:"Un Aplauso para el Asador",   cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/un-aplauso-para-el-asador.jpg"},
  {id:"VIN-21", title:"El Mejor Asado Se Come AcÃ¡",  cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/el-mejor-asado-se-come-aca.jpg"},
  {id:"VIN-22", title:"Tome Coca-Cola",              cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/tome-coca-cola.jpg"},
  {id:"VIN-23", title:"Indian Motorcycle 1934",      cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/indian-motorcycle-1934.jpg"},
  {id:"VIN-24", title:"Open 24 Hours",               cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/open-24-hours.jpg"},
  {id:"VIN-25", title:"Barra",                       cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/barra.jpg"},
  {id:"VIN-26", title:"Asado Vino y Amigos",         cat:"vintages", size:"-", mat:"Aluminio", unit:"1 pieza", price:"-", img:"Vintages/asado-vino-y-amigos.jpg"},

];

