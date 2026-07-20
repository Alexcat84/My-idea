# My Idea, Reglas y tokens del paquete visual (lote 4: cuenta, dos pasos y catálogo)

Referencia de handoff que viaja junto a los mockups. Todo lo que diga este
archivo manda sobre cualquier residuo visual. Este es el canon WEB; el caparazón
nativo de la APK es un encargo aparte. Este documento REEMPLAZA al
`REGLAS_Y_TOKENS.md` del lote 3.

## 1. Paleta y regla de color: EL AZUL PIENSA, EL VERDE EJECUTA

| Token | Valor | Uso |
|---|---|---|
| Azul primario | `#4D7CFE` | Exploración, planeación, navegación, el anillo "pensando", el chip de saldo, los precios en créditos, el 402, el modo lectura de Tus Números, el foco de los campos de código y el botón "Ya los guardé". Etapas 1 a 4 del stepper. |
| Verde ejecución | `#3FB950` | Acción sobre el mundo real: etapa 5, progreso del checklist, chip "Completado", chip "Activo · n/m", margen sano, la cortesía de bienvenida y el estado "Activada" de la verificación en dos pasos. |
| Ámbar guardián | `#E0A64A` | El guardián de datos (GIGO), las tardías, la pérdida en Tus Números, el código vencido del login, y TODO lo destructivo o de fricción de seguridad: borrar una idea, borrar la cuenta, el código que no coincide y el candado de demasiados intentos. Espejo, nunca rojo, nunca regaño. |
| Matiz de los mundos | `#3A9B8F` | Identidad de un mundo (punto y borde de su sección). Ni azul ni verde. |
| Fondo base | `#0A0A0C` / `#000000` | Lienzo y frames. |
| Superficie 1 | `#101013` | Tarjetas y el botón de Google. |
| Superficie 2 | `#17171B` / `#141419` | Campos, hover de tarjetas, filas de ideas, códigos de rescate. |
| Texto | `#F5F6F8` | Principal. |
| Texto dim | `#A6A7AD` | Secundario. |
| Hairline | `rgba(255,255,255,0.08)` | Bordes. |

Lo destructivo JAMÁS va en rojo: va en ámbar con palabras claras ("Sí, borrar",
"Borrar mi cuenta para siempre") y con fricción proporcional (confirmación
inline para una idea; escribir ELIMINAR para la cuenta). El 402 sigue en azul
informativo. Mono (`ui-monospace`) queda reservado a material de seguridad y
confirmación literal: códigos de rescate, el input de rescate y ELIMINAR.

## 2. Los 5 nombres canónicos de etapa

1. La Chispa
2. Claridad
3. La Exploración
4. Tu Plan
5. Manos a la Obra

## 3. Créditos: la ley comercial (decidida 2026-07-19)

**Un crédito es un dólar, siempre.** Sin descuentos por volumen: los packs se
dimensionan por lo que compras con ellos, no por matemática de rebaja. La
compra con dinero aún no está activa (beta con cortesía): precio a la vista,
sin botón de compra.

| Pack | Precio | En palabras de persona |
|---|---|---|
| 5 créditos | $4.99 | tu plan completo |
| 15 créditos | $14.99 | el viaje completo de una idea (destacado: "el más elegido") |
| 30 créditos | $29.99 | dos ideas trabajadas |

Los precios por concepto siguen vivos en `web/lib/precios.ts` (el canon los
refleja, jamás los define): Claridad gratis, La Exploración 5, plan de un mundo
3 (su preview gratis), seguimientos 2 y 2, Tus Números 2 (una vez por idea),
registrar avance gratis. Cortesía de la beta: 20 créditos una sola vez.

## 4. Identidad y seguridad (nuevo en lote 4)

- La moneda del lenguaje es "verificación en dos pasos". "2FA", "TOTP" y
  "OTP" no existen en pantalla.
- Dos puertas al login: código por correo y Google (glifo oficial multicolor,
  borde hairline, fondo superficie 1). La lista de invitados es una sola.
- Métodos del segundo paso: app de autenticación o código por correo. El
  rescate es un código mono de 12 caracteres que abre la cuenta UNA vez; los
  8 se muestran una sola vez, con "Ya los guardé".
- El candado (423) y el código que no coincide hablan en ámbar espejo, con la
  espera dicha en palabras ("Espera 15 minutos") y sin perder nada del usuario.
- Los botones dormidos existen: el CTA despierta cuando el código está
  completo o cuando se escribió ELIMINAR. Dormido se dice con opacidad y tono,
  nunca desapareciendo el botón.
- El centro de créditos SIGUE siendo /potenciadores: en /cuenta el saldo solo
  se asoma con su puerta ("Ver mi centro de créditos").

## 5. Voz (obligatoria en toda salida al usuario)

- Cero guiones largos o medios. Coma, dos puntos o punto.
- Acentos correctos, siempre. La unidad es "idea"; "proyecto" se gana al final.
- Espejo, jamás regaño. A quien eligió ir a su ritmo no se le habla de
  calendario. Lo destructivo se dice completo: "No hay papelera", "No hay
  vuelta atrás".
- El mundo se nombra como el usuario lo conoce, jamás por su clave técnica.

## 6. Formato de los mockups (para el instrumento)

- Un HTML autocontenido por pantalla, abre por file sin red, sin CDNs ni
  frameworks. CSS y JS inline; tokens en `:root`; clases semánticas en español;
  2 espacios de indentación; comentario índice de labels al inicio.
- Cada pantalla, siempre en sus dos viewports: desktop `1240px` y móvil `380px`.
- `data-screen-label` únicos y disjuntos: ninguno prefijo de otro.
- Texto de prueba largo y feo, el del producto real.
- El QR del 23 es utilería determinística dibujada en canvas: patrón con los
  tres buscadores, solo para el mockup.

## 7. Pantallas del lote 4

Nuevas (PILA 1):

23. `23_centro_de_cuenta.html`, /cuenta: identidad, verificación en dos pasos
    (reposo, QR, código no coincide, candado 423, rescates, activada con app,
    activada con correo), créditos que se asoman, ideas con borrado inline y
    borrar cuenta con ELIMINAR.
24. `24_desafio_dos_pasos.html`, el paso 2 del login: app, correo (con
    reenvío) y rescate, con el alternador inferior.

Actualizadas (PILA 2):

15. `15_login.html` v2, REEMPLAZA al 15 del lote 3: divisor "o" + Continuar
    con Google; el no invitado recibe a las dos puertas.
7. `07_potenciadores_y_creditos.html` v3, REEMPLAZA al 07 del lote 3: packs
   5 · 15 · 30 a $4.99 / $14.99 / $29.99 y la ley "Un crédito es un dólar,
   siempre".

El resto del canon (01 a 06, 08 a 14, 16 a 22) sigue vigente sin cambios.

Ver `NOTAS_DE_DECISIONES_LOTE4.md` (criterio pantalla por pantalla) y
`HALLAZGOS_PILA_3.md` (la cacería sobre las capturas de la app viva).
