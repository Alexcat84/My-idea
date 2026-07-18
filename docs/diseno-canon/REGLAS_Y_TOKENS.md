# My Idea, Reglas y tokens del paquete visual (canon web, refresco)

Referencia de handoff que viaja junto a los mockups. Todo lo que diga este
archivo manda sobre cualquier residuo visual. Este es el canon WEB; el caparazón
nativo de la APK es un encargo aparte.

## 1. Paleta y regla de color: EL AZUL PIENSA, EL VERDE EJECUTA

| Token | Valor | Uso |
|---|---|---|
| Azul primario | `#4D7CFE` | Exploración, planeación, navegación, el anillo "pensando", y toda acción que dispara al motor a pensar (incluido "Contar qué pasó", que regenera el plan). Etapas 1 a 4 del stepper. |
| Verde ejecución | `#3FB950` | Acción sobre el mundo real: etapa 5 del stepper, progreso del checklist (contadores X/N, barras, ítems hechos, "marcar hecho"), cajas "esta semana", "marcar como realizada", chip "Completado". |
| Ámbar guardián | `#E0A64A` | El guardián de datos (GIGO) de Tus Números, las tardías del cumplimiento, y la pérdida en Tus Números (margen negativo, escenarios en rojo). Espejo, nunca rojo, nunca regaño: una pérdida es un dato que se muestra, no una falta que se reprocha. |
| Matiz de los mundos | `#3A9B8F` | Identidad de un mundo (punto y borde de su sección) y su hito en la Celebración. Ni azul ni verde. |
| Fondo base | `#0A0A0C` / `#000000` | Lienzo y frames. |
| Superficie 1 | `#101013` | Tarjetas. |
| Superficie 2 | `#17171B` / `#141419` | Campos, hover de tarjetas. |
| Texto | `#F5F6F8` | Principal. |
| Texto dim | `#A6A7AD` | Secundario. |
| Hairline | `rgba(255,255,255,0.08)` | Bordes. |

Los estados completados se distinguen también por FORMA (check lleno, texto
tachado), nunca solo por color.

## 2. Los 5 nombres canónicos de etapa

1. La Chispa
2. Claridad
3. La Exploración
4. Tu Plan
5. Manos a la Obra

"Manos a la Obra" es el único nombre válido de la etapa 5 en todas las
superficies. No existe "En marcha".

## 3. Créditos (la moneda se llama créditos, jamás tokens)

Durante la beta, cada potenciador es "Activar · beta": gratis, con su precio de
catálogo tachado. El candado se retiró.

| Item | Costo de catálogo (tachado en beta) |
|---|---|
| El organizador (Claridad) | Gratis, siempre |
| La Exploración (entrevista + plan) | 5 créditos |
| Activar un mundo | 3 créditos (gratis en beta) |
| Seguimiento core | 2 créditos (gratis en beta) |
| Seguimiento de mundo | 2 créditos (gratis en beta) |
| Tus Números | 2 créditos |

> **Corregido en adopción (2026-07-17):** la entrega de Design ponía
> "Seguimiento core: Gratis (es el bucle del viaje principal)". Eso **no** es una
> decisión del fundador — nadie autorizó ese cambio de política. La **fuente de
> verdad de los precios es `web/lib/precios.ts`** (`seguimiento: 2`) + el canon de
> cobro de `docs/FLUJO_TRACKING.md §5` ("2 core / 2 mundo"). El canon visual
> **refleja** los precios, jamás los define. Se corrigió aquí a **2 créditos**.

Los packs del centro de créditos (10, 30, 75) son estructura, no precio: el
precio en dinero está por definir. Sin suscripción: créditos consumibles, y el
usuario nunca pierde créditos por un fallo del sistema.

## 4. Voz (obligatoria en toda salida al usuario)

- Cero guiones largos o medios. Coma, dos puntos o punto.
- Acentos correctos, siempre. La unidad es "idea"; "proyecto" se gana al final.
- Espejo, jamás regaño: las tardías en ámbar, nunca rojo; el plan de seguimiento
  asume la desviación, no la reprocha. A quien eligió ir a su ritmo no se le
  habla de calendario.
- El mundo se nombra como el usuario lo conoce ("Calidad y Confianza"), jamás
  por su clave técnica.

## 5. Formato de los mockups (para el instrumento)

- Un HTML autocontenido por pantalla, abre por file sin red, sin CDNs ni
  frameworks. CSS y JS inline; tokens en `:root`; clases semánticas en español;
  2 espacios de indentación; comentarios de sección; comentario índice de labels
  al inicio de cada archivo.
- Cada pantalla, siempre en sus dos viewports: desktop `1240px` y móvil `380px`.
- `data-screen-label` únicos y disjuntos: ninguno prefijo de otro (el estado va
  antes del sufijo de viewport, no después).
- Texto de prueba largo y feo, el del producto real.

## 6. Pantallas incluidas (11 refrescadas + 2 nuevas)

1. `01_home_mis_ideas.html`, Home / Mis ideas (sello de fecha, realizadas al final con Proyecto)
2. `02_la_chispa.html`, La Chispa (captura, momento sagrado)
3. `03_claridad.html`, Claridad (organizador: frase, lo que tienes, lo que asumes)
4. `04_la_exploracion.html`, La Exploración (riel, oferta honesta, plan en camino, recorrido abierto en móvil)
5. `05_tu_plan.html`, Tu Plan (documento con esta semana en verde, procedencia, Activar beta)
6. `06_manos_a_la_obra.html`, Manos a la Obra (checklist verde plegable, replanteo del 380, contar qué pasó)
7. `07_potenciadores_y_creditos.html`, Potenciadores y Créditos (Activar beta, centro de créditos, guardián ámbar)
8. `08_mundos_activos.html`, Mundos Activos (subproyecto con follow y acta de cierre)
9. `09_la_celebracion.html`, La Celebración (timeline azul a verde, dos variantes, hito de mundo)
10. `10_modo_y_fechas.html`, Modo y Fechas (elección de modo y ritual de fechas)
11. `11_analisis_del_proyecto.html`, Análisis del Proyecto (capa universal, cumplimiento modo fechas, cumplimiento por mundo)
12. `12_el_cierre_honesto.html`, El cierre honesto (NUEVO: camino sin salida y mundo que no encaja, con reembolso)
13. `13_detalle_de_actividad.html`, Explorar actividad (NUEVO: detalle de ítem, cajón lateral y hoja inferior)
14. `14_tus_numeros.html`, Tus Números (NUEVO: réplica financiera del análisis; veredicto de una frase, tiles, barra de la verdad, palancas calculadas, escenarios, faltantes, guardián; estados pérdida y sano)

Cada archivo incluye desktop 1240 y móvil 380, y estados extra donde el producto
los tiene. Ver `NOTAS_DE_DECISIONES.md` (pantallas 1 a 13) y `NOTAS_TUS_NUMEROS.md`
(pantalla 14) para el criterio pantalla por pantalla.
