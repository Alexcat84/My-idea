El veredicto de la vuelta 1 ya lo conoces: quedo registrado en tu propia entrega, con las tres opciones marcadas como elegidas en tu NOTAS_DE_DECISIONES. Este encargo tiene dos partes: el CIERRE de la vuelta 1 y la VUELTA 2 (piezas D, E y F del brief), que hereda el tono de las ganadoras.

## PARTE 1: el cierre de la vuelta 1

1. Los `_380.html` UNICAMENTE de las tres opciones que el fundador escogio (ya sabes cuales: las marcadas como elegidas). Nada de 380 para las descartadas. Misma opcion, mismo copy, compuesta para 380 (la APK renderiza en telefono: no es un extra).
2. Las `notas.md` finales de cada pieza: solo la opcion elegida, con Medidas de los DOS viewports, Colores por token y Estados completos.
3. Un rename menor en `B_esfuerzo/notas.md`: donde dice "alineado a la linea base del valor", di "alineado a la base tipografica del valor". Es el termino tipografico, pero "linea base" es vocabulario del producto (las fechas de referencia) y no puede aparecer con otro sentido en ningun documento de la casa.

## PARTE 2: la vuelta 2 (piezas D, E y F del brief)

Mismas condiciones que la vuelta 1: 2 opciones por pieza, bien distintas entre si; divergencia media (puedes cambiar la composicion del bloque, no la pantalla); todo a 1240 para elegir (los 380 al cerrar); bloque suelto para las opciones y una vista en contexto de la que perfiles ganadora. Las reglas duras del brief siguen enteras (sin jerga, sin guiones de ningun tipo como puntuacion, severidad en palabras jamas matriz, ambar espejo, verde solo para lo hecho, ruido cero, copy exacto).

**El tono ya esta elegido y se hereda, no se reabre:** manda por jerarquia y no por color, el azul se gasta solo en la accion o lo elegido, los datos se dicen sin encuadrarlos de mas, y lo serio se lee como documento, no como tabla fria. Es el tono de las tres elegidas de la vuelta 1.

### PIEZA D: el carril y los chips (la costura de la proteccion)

Carril: en "tus fechas de un vistazo" del nucleo, el toggle `Ver proteccion` (nace apagado; solo existe si hay protecciones). Encendido, bajo la banda de cada etapa aparece una sub fila de ROMBOS: contorno = pendiente, relleno verde = hecha; tooltip con mundo y texto. Solo lectura, jamas cuenta en las medidas.
Sobre el color del pendiente, EXPLORA LAS DOS en tus opciones: contorno azul #4D7CFE (como esta hoy) contra el matiz de mundo #3A9B8F (que ya identifica "cosa de los mundos" en el resto del producto). El verde relleno para lo hecho no se negocia.
Chips en el detalle, dos direcciones: el item del nucleo protegido lleva pildora `Protegida` + "[respuesta] · [mundo]"; la respuesta del mundo lleva SIEMPRE su deteccion + "Protege: [#N · titulo]"; si lo protegido se retiro: "la actividad que protegia fue retirada"; la sistemica: "tu negocio entero".

### PIEZA E: el aviso de no llego (ritual de fechas del mundo)

Bajo la fila de la proteccion que no alcanza, en ambar: "Esta proteccion no llega antes de [#N · actividad]: muevela o acepta el riesgo con los ojos abiertos." La fecha mostrada es la honesta. Es el momento mas delicado de tono del producto: aviso serio sin alarma; espejo, no juez. La vista en contexto aqui es obligatoria: el aviso solo se juzga dentro del ritual.

### PIEZA F: las fases visuales del diagrama de fechas

El diagrama ya es por fases (una barra = una etapa; tres vistas: riel, escalera, cintas; el mismo componente sirve al PDF). La vara: tratamiento visual de fase (titulos jerarquizados, bandas o separadores, numeracion visible) calibrado UNA VEZ y aplicado SOBRE LOS TRES ARCHIVOS EXISTENTES de tu entrega anterior, versionados (nueva version, no sobrescribir: la vara es el archivo, no el recuerdo). El carril de la pieza D vive DENTRO de esa jerarquia: vistelo sin deshacerlo.

## El formato de entrega (igual que la vuelta 1, que llego perfecta)

Un ZIP, carpeta raiz `entrega-tiempo-y-proteccion-v2/`:

```
entrega-tiempo-y-proteccion-v2/
  cierre_v1/
    (los _380.html de las tres elegidas, con su nombre de opcion real)
    (las tres notas.md finales)
  00_calibracion_lado_a_lado.html      (las opciones de D, E y F)
  D_carril_y_chips/
    D_opcion1_1240.html
    D_opcion2_1240.html
    notas.md
  E_no_llego/
    E_opcion1_1240.html
    E_opcion2_1240.html
    notas.md
  F_fases/
    riel_v2.html
    escalera_v2.html
    cintas_v2.html
    notas.md
  NOTAS_DE_DECISIONES.md
```

Mismas reglas de archivo: HTML autocontenido de verdad (CSS y JS inline, abre por file:// sin red), PROHIBIDO incrustar imagenes (base64/blobs; todo grafico en SVG inline de paths o CSS), nombres en minusculas snake_case sin acentos, cada HTML legible como codigo fuente, y las reglas de voz tambien dentro de las notas.
