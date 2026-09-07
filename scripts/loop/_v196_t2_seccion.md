### TAREA 2. LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. **CERRADA.**

**EL SUJETO NO SE ELIGIO AQUI Y ADEMAS SE RECOMPUTO.** El tramo son los 60 puestos
de `docs/loop/_auditor_v196_ciega_blind.txt` y el doble sus 60 vecinos
deterministas, cerrados por el auditor en
`docs/loop/_auditor_v196_doble_para_la_197.txt` antes de que yo mirara nada.
`vecinos()` **se IMPORTA** de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`
y no se copia. **Mi recomputacion y la sellada son EL MISMO CONJUNTO**, y el solape
del doble con el tramo y con el universo sale **0 y 0 POR CONSTRUCCION**, porque
`evitar` va dentro de la llamada y no comprobado despues
(`docs/loop/SALIDA_V196_T2_SUJETO.txt`, 12038 bytes).

**EL UNIVERSO CONSUMIDO, CONTADO DE SUS CATORCE FICHEROS: 621.** Calza con el
encargo. **Y el `561 sin el tramo` se mide POR LAS DOS LECTURAS, porque no
significan lo mismo**: la **diferencia de conjuntos** da **561** y calza; la **union
de los otros trece ficheros** da **621**. **La causa esta medida y no supuesta:**
los 60 del tramo del auditor **son los mismos 60** de la tanda del ejecutor de la
195, y estan **enteros dentro de `SALIDA_V195_T2_CIEGA.txt`** (60 de 60 medidos),
asi que quitar su fichero no los quita del universo. **Lo que manda para
`vecinos()` es la union entera.**

**EL COTEJO, POR LAS CUATRO VARAS** (fichero:
`docs/loop/SALIDA_V196_T2_COTEJO.txt`, 13981 bytes, contado antes de publicar esta
tabla):

| sobre que se mide | coinciden | discrepan |
|---|---:|---:|
| los **120** enteros | **113 de 120** | **7** |
| los **114** sin los quemados | **108 de 114** | **6** |
| **el DOBLE (60), la unica mitad ciega de verdad** | **55 de 60** | **5** |
| el TRAMO (60), con el reparto filtrado | 58 de 60 | 2 |

**Y LA CUENTA QUE MANDA ES LA DEL DOBLE, 55 DE 60, QUE ES LA QUE ME BAJA EL
RESULTADO.** Las otras tres se publican porque la casa publica lo que mide, no lo
que le conviene.

**LA CONTAMINACION SE DECLARO ANTES DE LEER, NO DESPUES DE COTEJAR, Y NO ES SOLO LA
DE LOS SEIS QUEMADOS.** La lista de quemados vive sellada en
`scripts/loop/vuelta196_tarea2_relectura_al_doble.py` y el cotejo la **importa** en
vez de reteclearla: **976, 2428, 2662 y 3173** porque la seccion 4 del acta 196
publica su clase de archivo, y **654 y 719** porque su hallazgo `5.1` declara que el
encargo de la 195 publico la suya. **Y LA GRANDE ES OTRA, Y LA DECLARO CONTRA MI
MISMO:** la seccion 2 del acta 196 publica **el REPARTO DEL ARCHIVO sobre los 60 del
tramo** (`A 8, B 1, C 0, D 51`). **Eso no es la clase de un puesto: es la
distribucion de la mitad del sujeto**, y la TAREA 1 de esta misma vuelta es
BLOQUEANTE y obliga a leer el acta entera. **Mi reparto sobre el tramo salio
exactamente ese**, asi que **no reclamo ceguera sobre el tramo** y su 58 de 60 no se
puede leer como una lectura limpia.

**MI REPARTO CONTRA EL DEL ARCHIVO, LOS DOS CONTADOS:**

| | mio | del archivo |
|---|---|---|
| sobre los 120 | A 16, B 2, C 0, D 102 | A 17, B 1, C 0, D 102 |
| sobre el DOBLE | A 8, B 1, C 0, D 51 | A 9, B 0, C 0, D 51 |

**LA `B` NO SE SALTO Y SE SOBRE EMITIO POR UNA.** Emiti 2 donde el archivo tiene 1,
y la de mas es el `207`. **El sesgo cambia de signo respecto de la 195**, que emitio
4 donde habia 1: sigue siendo sobre emision, pero de una y no de tres. La que si
acerte es el `654`, y esa esta quemada.

**LAS SIETE DISCREPANCIAS, CON SU MARCADO PUESTO ANTES:**

| puesto | mia | archivo | marcado antes |
|---:|---|---|---|
| `207` | B | A | **DISCUTIBLE** |
| `880` | D | A | **DISCUTIBLE** |
| `2429` | A | D | **DISCUTIBLE** |
| `2430` | A | D | **DISCUTIBLE** |
| `2917` | D | A | **DISCUTIBLE** |
| `616` | D | A | **sin marcar** |
| `2662` | A | D | **QUEMADO E INALCANZABLE** |

**CINCO DENTRO DE MI MARCADO Y DOS FUERA, Y DE LAS DOS DE FUERA UNA ESTA QUEMADA:
QUEDA UNA SOLA FUERA Y LIMPIA, EL `616`.** Marque **15 discutibles antes de saber si
acertaba** y cinco de las siete cayeron dentro. **Esa `616` dispara `AUDITOR.md`
1.2 sobre mi propia tanda**, y lo escribo yo en vez de esperar a que me lo cuenten.

**LOS DOS ERRORES QUE EL AUDITOR Y YO COMPARTIAMOS FUERON LOS DOS PUESTOS Y LOS DOS
SIRVIERON**, y va medido y no dicho: **la vara es el suelo y no el techo** hizo que
el `976` saliera `A` por la regla de familia del sub-puro, y **la semejanza de los
ids no decide** (`9.6.3`) hizo que el `1807`, el `2427` y el `1808` salieran `D` a
pesar de tener ids casi identicos. **Los tres calzan.**

**Y UN HALLAZGO MIO, MEDIDO SOBRE LOS 120 Y NO SOBRE UNA IMPRESION: TRES DE MIS
SIETE DISCREPANCIAS SE APOYAN EN EVIDENCIA QUE LA CIEGA NO PUEDE ENSENAR.** El
`616` lleva en su razon `FAMILIA DECLARADA: los dos son miembros del racimo censado
Portafolio, asi que no se pelea la clase`; el `207` cierra con `FIGURA: el racimo de
estrategia de innovacion de producto`; y el `2662` es una `CORRECCION DECLARADA`
sobre una fusion **planeada y no aplicada al grafo**, que es exactamente el hallazgo
`5.3` del acta 196. **Contado sobre los 120: seis razones citan un RACIMO y tres
citan una CORRECCION DECLARADA.** La ciega entrega `puesto_intra`, `nodo_a`, `nodo_b`
y los pasos, y **la pertenencia a un racimo censado no esta en esa lista blanca**.
**No lo arreglo, que no es de esta vuelta**, y lo dejo nombrado con su cifra: es la
generalizacion del `5.3`, y no vale solo para las fusiones no aplicadas.

**EL `2662` SE DECLARA INALCANZABLE Y SALE DEL CREDITO**, que es la pieza (f) del
encargo: a ciegas los dos nodos son la misma constitucion del consejo de calidad, y
la clase `D` del archivo se apoya en que el par **resuelve a otro par** tras un
alias que **no esta aplicado al grafo**. **Ningun lector a ciegas puede alcanzarlo**,
y no lo arreglo por mi cuenta.

**EL ARCHIVO NO SE MOVIO NI UN BYTE:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` mide
**4054129 bytes** por las dos convenciones y **`sha256` LF `0a77b5a35a962621`** al
entrar al aislador, al salir de el y al cerrar el cotejo. **Ninguna clase se toco.**
