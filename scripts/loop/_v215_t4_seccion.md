### TAREA 4. LOS DOS PUNTOS DE `OP-I-01` QUE QUEDARON A MEDIAS

**LO PRIMERO, PORQUE ES LO QUE LA `4.c` PROHIBE:** esta tarea **NO ESCRIBE NI UNA
LINEA EN NINGUNA FICHA**, y no lo prometo, lo mido. **`sha256` LF de
`docs/plan/OPERACIONES.jsonl` a los dos lados: CALZAN SI.** **Filas
de `numstat` sobre el expediente: 0. Sobre el inventario: 0.**
**CERO campos `estado` movidos, en `OP-I-01` y en las demas.**

#### 4.a. EL PUNTO 3, POR SU NEGATIVA, QUE SI SE PUEDE CITAR

**ME LO ADJUDICARON EN CONTRA Y TENIAN RAZON** (`5.4`, linea **76174**). Dije que
una busqueda negativa no se puede citar, y lo que se prohibe es **AFIRMAR UNA
BUSQUEDA NO CORRIDA**, no publicar la que da cero. **Aqui esta corrida.**

**EL COMANDO, ESCRITO ANTES DE SU RESULTADO:** por cada una de las
**672** entradas de `docs/plan/INVENTARIO.jsonl` y por cada uno de sus
**4704** campos de texto, se pregunta si el campo **ENTERO**, en minusculas
y sin espacios de los bordes, **es** una de 23 palabras de relleno, y aparte si
esta **VACIO**. **Se compara el campo COMPLETO, NUNCA por subcadena**, que es la
laxitud que me cazo la `D.7` en la 214.

**EL VOCABULARIO ES MIO Y VA ESCRITO ENTERO EN EL INSTRUMENTO PARA QUE SE PUEDA
DISCUTIR.** Una lista que nadie puede leer no se puede auditar. **Lo marco como
discutible.**

**LA MITAD AFIRMATIVA, CON SUS DOS CONVENCIONES, PORQUE UNA SOLA NO SE PUEDE
COTEJAR CON LA CIFRA DE LA 214:** entradas que nombran la marca **tal cual, en
mayusculas: 5**; entradas que la nombran **sin mirar mayusculas:
119**. **La 214 publico 119 con la segunda**, y lo se porque
lei su convencion en la **linea 133** de `scripts/loop/_v214_t1c_op_i_01.py`, no
porque me acuerde.

**LA MITAD NEGATIVA, QUE ES LA QUE ESTABA PENDIENTE, CON SU CERO DELANTE:**

- **CIFRA campos SOSPECHOSOS de relleno, antes de mirar el vocabulario del
  campo: 6.**
- **CIFRA DESCARTADOS porque el campo los usa como estado: 6.**
- **CIFRA campos RELLENADOS DE VERDAD: 0.**
- **CIFRA campos VACIOS, que no estan nombrados ni rellenados: 0.**

**LOS 6 DESCARTES NO SE ESCONDEN: VAN CON SU NOMBRE Y CON LA CIFRA
QUE LOS DESCARTA.** Son mi caida `D.2` de esta vuelta, cazada por mi antes de
publicar el veredicto.

| entrada | sujeto | campo | valor | la forma LARGA que el MISMO campo trae |
|---:|---|---|---|---|
| **7** | health_safety | `estado` | 'pendiente' | 'pendiente, BOLSA RECALIBRADA y tasa MEDIDA' |
| **8** | quality | `estado` | 'pendiente' | 'pendiente, BOLSA RECALIBRADA y tasa MEDIDA' |
| **9** | risk_management | `estado` | 'pendiente' | 'pendiente, BOLSA RECALIBRADA y tasa MEDIDA' |
| **10** | seguridad_digital | `estado` | 'pendiente' | 'pendiente, BOLSA RECALIBRADA y tasa MEDIDA' |
| **320** | costuras internas confirmadas | `estado` | 'pendiente' | 'pendiente, BOLSA RECALIBRADA y tasa MEDIDA' |
| **322** | racimos con miembro de otro dominio | `estado` | 'pendiente' | 'pendiente, BOLSA RECALIBRADA y tasa MEDIDA' |

**LA REGLA DEL DESCARTE ES MECANICA Y NO SE ENSANCHA PARA QUE TRAGUE:** una
palabra sospechosa en el campo `F` se descarta **solo si el propio campo `F`
tiene, en otra entrada, un valor que empieza por esa palabra y sigue con mas
texto**. Pide la forma larga **en el mismo campo**, no en cualquiera. **Su caso
positivo lo prueba:** `pendiente` tiene formas largas en `estado` (**4**) y
**ninguna** en `forma` (**0**), asi que en `forma` seguiria contando como
relleno.

**VEREDICTO MEDIDO HOY DEL PUNTO 3: CUBRE** (la 214 lo dejo en **A MEDIAS**).
**SE MUEVE.**

#### 4.b. EL PUNTO 4, MIDIENDO ANTES DE DECIDIR Y SIN INVENTAR LA SEDE

**LA VISTA HUMANA DECLARA DE SI MISMA QUE AHI NO SE REGENERA, Y LO DICE EN TRES
SITIOS**, no en uno: `docs/plan/10_INVENTARIO.md` **lineas 19, 121 y 182**,
pegadas enteras en la salida sellada. **Eso es lo que el encargo ya sabia. Lo que
faltaba era saber DONDE SI.**

**LA BUSQUEDA, CON SU COMANDO ESCRITO ANTES DE SU RESULTADO:** se recorre **todo
el arbol de scripts**, no solo el del bucle, y por cada fichero de Python se
pregunta si **nombra** la vista humana y si ademas tiene, en la misma linea o en
las tres siguientes, **una apertura en modo escritura o una llamada de escritura
sobre esa ruta**.

- **CIFRA ficheros que la NOMBRAN: 27.**
- **CIFRA ficheros que la ESCRIBEN: 0.**

**Y LA SEGUNDA MITAD DE LA BUSQUEDA, PORQUE UN FICHERO PUEDE ESCRIBIRSE SIN QUE
NINGUN SCRIPT LO NOMBRE:** de que commits sale la vista humana, leido de
`git log` sobre su ruta. **CIFRA commits en toda su historia: 19**, y el
**ultimo es 6b8fd72b 2026-08-14**. **Sus 34258 bytes de hoy son de esa fecha.**

**LA SEDE QUE REGENERARIA LA VISTA HUMANA NO EXISTE EN EL REPO, Y ESO TAMBIEN ES
UN RESULTADO, QUE ES LO QUE EL ENCARGO PIDE QUE DIGA SI PASA.** Los
**27** ficheros que la nombran **la LEEN o la CITAN**; ninguno la
escribe. **Su ultima escritura fue A MANO**, en un commit de agosto.

**VEREDICTO MEDIDO HOY DEL PUNTO 4: A MEDIAS**, y **no por pereza de esta vuelta**:
la mitad que falta **no tiene instrumento que la haga**, y fabricarlo **es
maquinaria nueva bajo la moratoria** (`AUDITOR.md` 6.3). **NO LA FABRICO Y NO ME
LA ADJUDICO: SE SUBE NOMBRADA.**

#### 4.c. LO QUE ESTO DEJA, DICHO SIN ADORNO

**`OP-I-01` QUEDA HOY EN 3 PUNTOS EN CUBRE Y 1 EN A MEDIAS**, contra los 2 y 2
que la 214 midio. **El que se mueve es el 3**, y se mueve porque **se corrio la
busqueda que faltaba**, no porque nadie cambiara de opinion. **El 4 sigue donde
estaba, y ahora se sabe POR QUE: le falta una sede que no existe.**

**CIFRA comprobaciones del instrumento que fallan: 0.**
