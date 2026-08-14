# REPORTE, vuelta 15 del ejecutor (Sonnet 5)

**FASE II, RECOMPUTO. MODO DE CIERRE: cero reparaciones de nodos, cero operaciones ejecutadas, cero
pares nuevos leidos.** `dataset/` intacto. `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` intacto (sigue en
3.388 lineas). La FASE III no se abre y la rama `pasada-unica` no se crea.

**Hash final: `8f919610`** (push confirmado a `origin/bucle`). Commits de esta vuelta:
`3bf9c5f9` (TAREA 1) y `8f919610` (TAREA 2).

**Rutas tocadas en la vuelta** (`git diff --stat a4929ead HEAD`): `docs/plan/10_INVENTARIO.md`,
`docs/plan/INVENTARIO.jsonl`, `docs/plan/OPERACIONES.jsonl`, `docs/plan/RECOMPUTO_3388.md`. Cuatro
rutas, ninguna en `dataset/`, ninguna en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (verificado con
`git diff --name-only a4929ead HEAD -- dataset/ docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, vacio).

---

## TAREA 1: registro y tres correcciones (encargo de la vuelta 15, puntos 1 a 3)

### 1. `OP-L-03` adjudicado en CUARENTA actos y SETENTA Y TRES pares

El discutible 1 de la vuelta 14 se cierra a favor de la lectura literal, **no por preferencia**: el
auditor reconstruyo el corte 2.117 corriendo `scripts/plan/recomputo_3388.py` sobre el blob viejo
(`git show c16a24f5`) con el mismo metodo de `OP-L-03` sin cambiarle nada, y obtuvo **29 actos y 55
pares, el reparto exacto de la nota vieja**, con **los mismos cuatro actos en disputa** (`OP-S-07`,
`OP-M-03-III`/`OP-M-03-ENLACES`, `OP-S-04`/`OP-F-04-WEI`) **ya dentro de ese 55**. El criterio ancho
habria dado 25 y 51 en ese mismo corte, que contradice el banco. Registrado con tachado (sin borrar el
discutible) en la nota de `OP-L-03` (`docs/plan/OPERACIONES.jsonl`) y en
`docs/plan/RECOMPUTO_3388.md`.

### 2. La cobertura del racimo de la supervision de la IA se corrige a DIECIOCHO de CUARENTA Y CINCO

La frase "10 de 45, los 35 restantes sin leer" era FALSA (caida propia del auditor en la vuelta 14, no
del ejecutor). **Remedida en esta vuelta con instrumento propio**, sin copiar la cifra del auditor:
sobre la nomina de diez (`docs/INTRA_DOMINIO_INFORME.md` secciones 11.bis.1 y 11.bis.3: bloque humano
5, bloque del mapa 4, suelto 1), **15 de los 45 pares posibles estan en
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`** (puestos 166, 177, 293, 456, 692, 792, 993, 1.041, 1.211,
1.239, 1.339, 1.451, 1.496, 1.517, 1.541; 8 A, 7 D), **mas 3 lecturas dirigidas del bloque humano fuera
de cola** (`docs/plan/LECTURAS_DIRIGIDAS.md` lineas 437 a 468, verificadas por busqueda directa que no
estan en el archivo de veredictos), todas D. **COBERTURA REAL: 18 de 45 (8 A, 10 D). Sin leer: 27, no
35.** Con tachado sin borrar, arrastrado a: la nota de `OP-F-02` ("14 de 45 al puesto 1.517" tachado,
"18 de 45 al corte 3.388" nuevo), la entrada de racimo en `docs/plan/INVENTARIO.jsonl` (nomina de OCHO
miembros corregida a DIEZ, con `invitar_ia_a_todo` y `principio_invitar_ia_siempre` agregados) y la
fila del racimo en `docs/plan/10_INVENTARIO.md`.

### 3. La etiqueta "PENDIENTE DE DOCTRINA" de `OP-I-01` se corrige

El acta de la vuelta 13, adjudicacion 6.4, ya dice que `OP-I-01` **no es pendiente de doctrina: es un
encargo propio de recomputo de inventario**. Corregido con tachado en la nota de `OP-I-01`
(`OPERACIONES.jsonl`) y en `docs/plan/RECOMPUTO_3388.md`. No mueve cifra ni clase: es correccion de
etiqueta, no de medicion.

---

## TAREA 2: recomputo del inventario de `OP-I-01` al corte 3.388

### El archivo vivo, medido primero

**`docs/plan/INVENTARIO.jsonl` tiene HOY 336 entradas** (10 dominio, 221 acto, 13 racimo, 53
familia_de_ids, **20 figura**, **19 defecto**), no las 323 que la nota vieja declaraba (que traia 14
defectos y 12 figuras). Desfasada por DOS vias: por el corte (221 actos contra 335 componentes) y por
el propio archivo (323 contra 336).

### Los seis sumandos, recomputados al 3.388

**a. Dominios (diez), pares leidos y tasa de A**, de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`:

| dominio | pares leidos | A | tasa de A |
|---|---:|---:|---:|
| core | 1.445 | 344 | 23,8 % |
| quality | 844 | 126 | 14,9 % |
| health_safety | 192 | 45 | 23,4 % |
| entrega | 171 | 2 | 1,2 % |
| environmental | 170 | 29 | 17,1 % |
| compras | 155 | 1 | 0,6 % |
| franquicias | 148 | 18 | 12,2 % |
| risk_management | 106 | 0 | 0,0 % |
| exportacion | 130 | 15 | 11,5 % |
| seguridad_digital | 27 | 3 | 11,1 % |
| **total** | **3.388** | **583** | **17,2 %** |

Cuadra cifra a cifra con el marcador de la vuelta 14 (A 583, B 89, C 7, D 2.709; 3.388 lineas).

**b. Actos: 335** (280 CERRADOS, 55 ABIERTOS), citado de la vuelta 14 con su corte, no remedido de
nuevo: mismo instrumento y mismo archivo.

**c. Racimos: los trece, nomina y cobertura remedida.** Metodo: pares posibles (C(n,2)) sobre la
nomina vigente, cruzados contra la cola; donde la cobertura declarada no calzaba solo con la cola, se
busco la lectura dirigida y se verifico que esta fuera de cola.

| racimo | nomina | posibles | cobertura remedida | cambio |
|---|---:|---:|---|---|
| el efectivo contra la ganancia | 3 | 3 | 3 de 3 | identico |
| la ecuacion de valor | 5 | 10 | 10 de 10 (6 A, 4 D) | identico |
| el sales roadmap | 6 | 15 | 10 de 15 | identico |
| la competencia entre inversores | 5 | 10 | 7 de 10 | identico |
| la junta asesora | 4 | 6 | 6 de 6 (4 A, 2 D) | identico |
| los cuadrantes de mercado | 6 | 15 | 15 de 15 (8 A, 7 D) | identico |
| build, measure, learn | 8 | 28 | 9 de 28 | identico |
| el compromiso contado tres veces | 3 | 3 | 3 de 3 | identico |
| la seleccion de canal | 5 | 10 | 10 de 10 (9 A, 1 D) | identico |
| **la supervision de la IA** | 10 | 45 | **18 de 45** (8 A, 10 D) | **CORREGIDO, TAREA 1** |
| la mesa unida de puertas y portafolio | 17 | 136 | 49 de 136 | identico |
| el racimo del pivote | 7 | 21 | 13 de 21 | identico |
| la serie de Coleman | 28 | 378 | 45 de 378 | identico |

**DOCE de trece verifican identicos a lo ya declarado; el unico corregido es supervision de la IA
(TAREA 1). El numero de racimos sigue en TRECE.**

**d. El conteo de familias de ids (53) y de defectos (19): NO depende del corte del cribado**, declarado
con motivo (clusters de ids y defectos de estructura de catalogo, medibles sobre el grafo sin abrir
veredictos). **El ESTADO de fusion de cada familia SI depende del corte, y mi primera version de esta
seccion daba por sentado, sin comprobarlo, que ya estaba cubierto por el recomputo de actos (b). Lo
comprobe (interseccion de miembros contra las 335 componentes) y es FALSO para la mayoria**: solo
**23 de 53** familias son, literal, el mismo objeto que un componente; **14** tienen a sus miembros
partidos entre varios componentes distintos, y **16** no tienen ningun miembro en ningun componente (sin
arista A registrada hoy). Para esas 30, el estado de fusion queda **SIN REMEDIR**, discutible marcado
abajo, no falsamente dado por cubierto.

**Figuras (20): SI dependen del corte, y NO se remidieron esta vuelta.** Probe un barrido mecanico
(grep del nombre de cada figura sobre el campo `razon` de las 3.388 lineas) y lo descarte como cifra
publicable: no calza de forma fiable con los "ejemplares" declarados (ESTRELLA da 17 menciones contra 9
ejemplares; TRIANGULO ABIERTO da 0 contra 2), porque el patron se decide por si el PAR CALZA con la
forma, juicio de contenido, no por si el texto nombra la figura. Remedir las veinte con fidelidad exige
releer y clasificar los pares nuevos desde su corte contra cada patron, alcance de la misma escala que
la regeneracion de actos (punto 4). Se trae como PENDIENTE DE MEDICION.

### El total nuevo

| total | cifras | corte |
|---|---:|---|
| nota vieja de `OP-I-01` | 323 (221, 53, 14, 13, 12, 10) | 2026-08-11, puesto 2.117 |
| archivo medido hoy, sin corregir actos | 336 (221, 53, 19, 13, 20, 10) | 2026-08-13 |
| **TOTAL NUEVO al corte 3.388** | **450** (**335**, 53, 19, 13, 20, 10) | **2026-08-13, corte 3.388** |

Sustituye SOLO la cifra de actos sobre el archivo medido hoy. No incluye ejemplares internos de
figuras (no medidos). Las 335 lineas de tipo acto NO se escribieron en el archivo: el total es
recomputo, no regeneracion.

### Discutible marcado: PLAN de regenerar las 221 entradas de tipo `acto` a 335, SIN EJECUTAR

Campos (`nombre` y `operaciones` no salen directo de la fuente y hay que derivarlos), instrumento por
campo, +114 lineas netas en `INVENTARIO.jsonl`, ninguna cita textual por nombre de acto individual
encontrada que se rompa (busque "221 actos" en ocho archivos, todos citan la CIFRA, ninguno un nombre
de acto viejo), riesgo real es perder la `nota` a mano de las entradas viejas si se sobrescribe sin
copiarla, costo bajo para los campos mecanicos y alto (lectura y redaccion por acto) para `nota`.
Detalle completo en `docs/plan/RECOMPUTO_3388.md`, seccion TAREA vuelta 15 punto 4. No se decide aqui.

---

## MARCADOR (confirmado, sin cambio: cero pares leidos esta vuelta)

**A 583 (17,2 %), B 89 (2,6 %), C 7 (0,2 %), D 2.709 (80,0 %); n 3.388; cero huecos, cero duplicados**
(recomputado en la seccion de dominios arriba, coincide con la vuelta 14).

**Vara por tramo: NO APLICA esta vuelta.** No se leyo ningun par nuevo (cero operaciones ejecutadas,
cero fusiones); la ultima vara publicada sigue siendo la de checkpoints anteriores al 3.388.

---

## CORRECCIONES DECLARADAS, todas con tachado sin borrar

1. `OP-L-03`: nota puesta al dia con la adjudicacion (40 actos, 73 pares), discutible 1 no se borra.
2. Cobertura del racimo supervision de la IA: 14 de 45 (tachado) a 18 de 45, en `OP-F-02`,
   `INVENTARIO.jsonl` (nomina 8 a 10) y `10_INVENTARIO.md`.
3. Etiqueta de `OP-I-01`: "PENDIENTE DE DOCTRINA" (tachado) a "encargo propio de recomputo".
4. Cifras de figura y defecto de `OP-I-01`: 12 y 14 (nota vieja) a 20 y 19 (archivo medido hoy).
5. Total del inventario: 323 (nota vieja) a 450 (corte 3.388), con 336 (archivo sin corregir actos)
   como paso intermedio, los tres publicados juntos.
6. **Caida propia del ejecutor, atrapada dentro de la misma vuelta**: la afirmacion de que el estado de
   fusion de las 53 familias de ids "ya esta cubierto por el recomputo de actos (b)" (tachado en
   `docs/plan/RECOMPUTO_3388.md` seccion 2.d) se sostenia en un solo caso verificado; comprobada contra
   las 335 componentes, es falsa para 30 de 53 (23 si corresponden uno a uno, 14 partidas, 16 sin
   overlap). Corregida antes de commitear este tramo, ver seccion de discutibles punto 2.

## PENDIENTES DE DOCTRINA

**Ninguno nuevo esta vuelta.** Las cinco correcciones cuelgan de reglas ya escritas: banco 9.10, 9.21 y
9.26, la regla de recomputo de la FASE II, y el precedente "etiqueta mala no es caida" (acta vuelta 4
punto 3, acta vuelta 13 seccion 5, acta vuelta 14 seccion 5).

---

## DISCUTIBLES MARCADOS, para la relectura ciega del auditor

Marcados ANTES de saber si aciertan, como manda el protocolo.

1. **El metodo de cobertura de racimos (cola mas lecturas dirigidas fuera de cola) se aplico igual a
   los trece, pero solo se BUSCO activamente la lectura dirigida en los racimos donde la cola sola no
   alcanzaba la cifra ya declarada** (ecuacion de valor, junta asesora, cuadrantes de mercado,
   seleccion de canal, supervision de la IA, mesa unida, serie de Coleman). En los otros seis (efectivo
   contra la ganancia, sales roadmap, competencia entre inversores, build-measure-learn, compromiso
   contado tres veces, racimo del pivote) la cola sola YA calzaba con la cifra declarada, y no busque
   lecturas dirigidas adicionales que pudieran existir sin mover la cifra. **Riesgo**: si alguno de esos
   seis tiene lecturas dirigidas fuera de cola que el archivo simplemente no necesita para cuadrar el
   numero, no las encontraria con este metodo. No cambiaria ninguna cifra publicada (coinciden con lo
   declarado), pero la COMPLETITUD de la busqueda no es la misma en los trece.
2. **CAIDA PROPIA, atrapada y corregida en esta misma vuelta antes de cerrar el reporte.** Mi primer
   borrador de la seccion 2.d declaraba, sin comprobarlo, que el estado de fusion de las 53 familias de
   ids "ya esta cubierto por el recomputo de actos (b)" porque son el mismo tipo de objeto que las
   componentes conexas, apoyado en un solo caso verificado (`accion_correctiva`, citado en el acta de la
   vuelta 14). **Antes de escribir este reporte, cruce las 53 contra las 335 componentes con instrumento
   propio y la afirmacion es FALSA para 30 de 53**: solo 23 corresponden uno a uno con un componente
   entero; 14 tienen a sus miembros repartidos en componentes distintos y 16 no tienen ningun miembro en
   ningun componente. Corregido con tachado en `docs/plan/RECOMPUTO_3388.md` seccion 2.d antes de
   commitear. **Queda declarado aqui porque es exactamente la clase de caida que el banco 9.10 nombra**
   (dar por bueno algo copiado o supuesto en vez de recomputarlo), y la atrape yo mismo dentro de la
   misma vuelta, no el auditor. Lo que SIGUE discutible: para las 30 sin cobertura de (b), no distingui
   si las 16 sin overlap son ids sueltos genuinos o un artefacto del instrumento, ni si las 14 partidas
   son de verdad dos familias distintas o una sola con lectura incompleta; esa clasificacion es trabajo
   nuevo, no medido aqui.
3. **La decision de NO remedir las figuras se apoya en que el grep mecanico da numeros que no calzan
   con lo declarado**, pero solo probe el grep sobre DOS figuras a fondo (ESTRELLA y TRIANGULO
   ABIERTO) antes de generalizar la conclusion a las veinte. Es posible que algunas de las otras
   dieciocho si tengan un patron mas mecanico (por ejemplo "LA FIRMA POSICIONAL DEL INJERTO" ya usa un
   contador declarado en su propia nota) y que la generalizacion sea mas ancha de lo que el instrumento
   prueba.
4. **El PLAN de regeneracion de actos (punto 4 de TAREA 2) declara que ninguna cita textual se
   rompe**, basado en un solo `grep` de la frase "221 actos"/"221 componentes". No busque citas por
   NOMBRE de acto individual de la lista vieja (habria que enumerar los 221 nombres y buscar cada uno),
   que es una verificacion mas fuerte y no se hizo por alcance.
