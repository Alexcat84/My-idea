Cuando entregues, empaqueta TODO en un solo ZIP con este formato exacto. Es el formato que ya funcionó en las entregas del calendario y de los lotes beta; no lo cambies.

## El ZIP

- Un solo ZIP con UNA carpeta raiz: `entrega-tiempo-y-proteccion/`.
- Dentro, en esta vuelta (A, B, C), dos artefactos:

```
entrega-tiempo-y-proteccion/
  00_calibracion_lado_a_lado.html      <- las opciones comparables, para elegir
  A_capacidad/
    A_opcion1_1240.html
    A_opcion2_1240.html
    notas.md
  B_esfuerzo/
    B_opcion1_1240.html
    B_opcion2_1240.html
    notas.md
  C_registro/
    C_opcion1_1240.html
    C_opcion2_1240.html
    notas.md
  NOTAS_DE_DECISIONES.md               <- indice general: que propone cada opcion y por que
```

- Cuando se elija la ganadora de cada pieza, la entrega de cierre añade su `_380.html` y las notas finales. Ninguna pieza cierra sin sus dos viewports (1240 y 380).

## Reglas de archivo (no negociables)

1. **HTML autocontenido de verdad**: CSS y JS inline, tipografia del sistema, abre con doble clic por `file://` sin red, sin CDNs, sin imports.
2. **PROHIBIDO incrustar imagenes** (base64 / blobs / data:image). Fue el problema de una entrega pasada: archivos ilegibles e inutilizables. Todo lo grafico va en SVG inline de paths (como los iconos de la casa) o en CSS puro.
3. **Nombres de archivo**: minusculas, snake_case, sin acentos, sin espacios, con el sufijo de viewport (`_1240` / `_380`).
4. **Peso**: cada HTML debe poder leerse como codigo fuente. Si un archivo pasa de ~150 KB, algo sobra.
5. El `00_calibracion_lado_a_lado.html` muestra las opciones de las tres piezas en una sola pagina desplazable, cada opcion rotulada (pieza + numero), para elegir sin abrir diez archivos.

## Las notas.md por pieza (el handoff)

Mismo molde de las entregas del calendario, con estas secciones exactas:

- **Titulo**: pieza y opcion.
- **Medidas**: paddings, radios, gaps y tamaños de fuente por viewport, en px.
- **Colores por token**: tabla `| Elemento | Valor |` con los rgba/hex exactos usados y a que token de la casa corresponden.
- **Estados**: cada estado visible de la pieza (vacio, con datos, corrigiendo, aviso) con su copy exacto.

## Reglas de voz (aplican tambien dentro de las notas y los HTML)

- Nada de guiones en texto visible: ni largos, ni medios, ni cortos usados como puntuacion o separador. Comas, dos puntos o parentesis.
- El copy del brief es exacto: se compone, no se reescribe.
- Sin jerga tecnica en nada que el usuario leeria.
