# My Idea, Reglas y tokens del paquete visual (lote 3: la beta viva)

Referencia de handoff que viaja junto a los mockups. Todo lo que diga este
archivo manda sobre cualquier residuo visual. Este es el canon WEB; el caparazón
nativo de la APK es un encargo aparte. Este documento REEMPLAZA al
`REGLAS_Y_TOKENS.md` del canon 2.0.

## 1. Paleta y regla de color: EL AZUL PIENSA, EL VERDE EJECUTA

| Token | Valor | Uso |
|---|---|---|
| Azul primario | `#4D7CFE` | Exploración, planeación, navegación, el anillo "pensando", toda acción que dispara al motor a pensar, el chip de saldo, los precios en créditos, el estado 402 y el modo lectura de Tus Números. Etapas 1 a 4 del stepper. |
| Verde ejecución | `#3FB950` | Acción sobre el mundo real: etapa 5 del stepper, progreso del checklist (contadores X/N, barras, ítems hechos), cajas "esta semana", chip "Completado", chip "Activo · n/m", margen sano y la cortesía de bienvenida. |
| Ámbar guardián | `#E0A64A` | El guardián de datos (GIGO), las tardías del cumplimiento, la PÉRDIDA en Tus Números (margen negativo, escenarios en pérdida, versiones con pérdida) y el error de código vencido del login. Espejo, nunca rojo, nunca regaño. |
| Matiz de los mundos | `#3A9B8F` | Identidad de un mundo (punto y borde de su sección) y su hito en la Celebración. Ni azul ni verde. |
| Fondo base | `#0A0A0C` / `#000000` | Lienzo y frames. |
| Superficie 1 | `#101013` | Tarjetas. |
| Superficie 2 | `#17171B` / `#141419` | Campos, hover de tarjetas. |
| Texto | `#F5F6F8` | Principal. |
| Texto dim | `#A6A7AD` | Secundario. |
| Hairline | `rgba(255,255,255,0.08)` | Bordes. |

Los estados completados se distinguen también por FORMA (check lleno, texto
tachado), nunca solo por color. El 402 (saldo insuficiente) va en AZUL
informativo, no en ámbar: el ámbar es de los datos del negocio del usuario
(pérdida, tardías, GIGO); quedarse sin créditos es un hecho del sistema con
una puerta al frente. Ver `NOTAS_DE_DECISIONES_LOTE3.md`.

## 2. Los 5 nombres canónicos de etapa

1. La Chispa
2. Claridad
3. La Exploración
4. Tu Plan
5. Manos a la Obra

"Manos a la Obra" es el único nombre válido de la etapa 5 en todas las
superficies. No existe "En marcha".

## 3. Créditos (la moneda se llama créditos, jamás tokens)

Los precios son VIVOS: los define `web/lib/precios.ts` y el canon los REFLEJA,
jamás los define. El tachado "gratis en beta" murió; el candado murió. Los
mundos se prueban gratis (preview: entrevista + diagnóstico) y lo que se compra
es su plan, a la entrega.

| Item | Costo vigente (refleja precios.ts) |
|---|---|
| El organizador (Claridad) | Gratis, siempre |
| La Exploración (entrevista + plan) | 5 créditos |
| El plan de un mundo (su preview es gratis) | 3 créditos |
| Seguimiento core (viaje principal) | 2 créditos |
| Seguimiento de mundo | 2 créditos |
| Tus Números (una vez por idea; corregir y recalcular, gratis siempre) | 2 créditos |
| Registrar avance (marcar hecho, notas, progreso) | Gratis, siempre |

Cortesía de la beta: 20 créditos al primer inicio de sesión. Los packs del
centro de créditos (10, 30, 75) son estructura, no precio: el dinero se muestra
"$ —" por definir. Sin suscripción: créditos consumibles, y el usuario nunca
pierde créditos por un fallo del sistema (se verifica al inicio, se descuenta a
la entrega).

## 4. Voz (obligatoria en toda salida al usuario)

- Cero guiones largos o medios. Coma, dos puntos o punto.
- Acentos correctos, siempre. La unidad es "idea"; "proyecto" se gana al final.
- Espejo, jamás regaño: las tardías y la pérdida en ámbar, nunca rojo; los
  errores en palabras de persona ("Te quedan 2 créditos; esto cuesta 3. Tu
  trabajo queda guardado tal como está."). A quien eligió ir a su ritmo no se
  le habla de calendario.
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

## 6. Pantallas del lote 3 (la beta viva)

Nuevas (PILA 1):

15. `15_login.html`, Login por código: paso correo, paso código, no invitado, código vencido
16. `16_fila_potenciadores.html`, La fila de mundos en sus 4 estados (bloqueada y mixta)
17. `17_escaparate_del_mundo.html`, El diagnóstico persistido con sello híbrido y CTA de plan
18. `18_compuerta_tus_numeros.html`, La activación de Tus Números (2 créditos, una vez por idea)
19. `19_tablero_vivo_tus_numeros.html`, El tablero vivo: sello HOY, ciclo de caja, versiones, modo lectura, recolector
20. `20_chip_saldo_y_402.html`, El chip de saldo (3 caras) y el saldo insuficiente
21. `21_landing_con_sesion.html`, El nav con y sin sesión + la tarjeta de regreso (propuesta)
22. `22_riel_de_redaccion.html`, El riel mientras el plan se escribe

Actualizadas (PILA 2):

7. `07_potenciadores_y_creditos.html`, REEMPLAZA al 07 del canon 2.0: precios
   vivos, saldo real con cortesía, tabla "lo que cuesta cada cosa", fila con el
   modelo del preview.

El resto del canon 2.0 (01 a 06, 08 a 13) sigue vigente sin cambios. El 14
(Tus Números pérdida/sano) sigue siendo la vara de los dos veredictos; el 19 lo
extiende con las piezas del tablero vivo, no lo reemplaza.

Ver `NOTAS_DE_DECISIONES_LOTE3.md` (criterio pantalla por pantalla) y
`HALLAZGOS_PILA_3.md` (verificación contra la app viva, sin rediseños).
