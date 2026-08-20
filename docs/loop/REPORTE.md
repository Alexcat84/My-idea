# REPORTE DE LA VUELTA 59 (21 ago 2026, ejecutor Opus 5)

**LO QUE NO SE HIZO VA PRIMERO, como la vuelta 58 dejo encargado: DE LOS TRES LOTES DEL TRAMO 5
SOLO SE EJECUTA EL LOTE A. Los actos 18 a 50, que son 34 de los 50, NO SE TOCAN**, y el tramo 5
queda ABIERTO. Se entrega **UN LOTE ENTERO CON SUS GUARDAS EN VERDE**, que es la unidad que el acta
58 (pregunta 6) declaro minima, y no un segundo lote a medias. **LA TAREA 1 SI VA ENTERA EN SUS DOS
PARTES.** **EL HALLAZGO DE LA VUELTA VUELVE A SALIR DE CORRER UNA GUARDA Y NO DE LEERLA, y esta vez
el cazado es el propio instrumento de `P.16`: el que la vuelta 57 escribio PARA VER lo que solo se
ve por el resolutor buscaba a su culpable POR EL LITERAL**, y por eso diagnostico mal su propio
rojo. Tenia **TRES defectos, los tres medidos contra el grafo antes de tocar codigo**, y uno de
ellos le habria hecho retirar **ocho entradas que no le tocaban**.

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `a248c6a3` (el commit del acta 58), **arbol limpio y todo pusheado; la regla 3 se cumplio POR VACIO y se dice asi en vez de darla por cumplida** |
| **hash final** | el commit del cierre mas este mismo, que solo escribe esta cabecera, **pusheados a `origin/pasada-unica`** |
| **commits de la vuelta** | **4 hasta el cierre**, leidos de `git log --oneline a248c6a3..HEAD`: `c9927b19` (apertura medida), `fd7de724` (TAREA 1.1, el barrido de titulos), `956f9e3d` (TAREA 1.2, la ratificacion del 32), `39d495b2` (LOTE A del tramo 5), **mas el del cierre y este** |
| **arbol al cierre** | limpio tras el commit del cierre |

---

## 0. LA APERTURA Y EL CIERRE, LA TABLA TALLADA POR INSTRUMENTO (regla 1)

**NINGUNA CELDA ESTA TECLEADA:** sale entera de
`python scripts/loop/tallar_cabecera_reporte.py --vuelta 59`
([`SALIDA_V59_TALLAR_CABECERA.txt`](SALIDA_V59_TALLAR_CABECERA.txt)). **Las dos columnas se leen de
ficheros DISTINTOS.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.342 / 511 / 17.366 | **3.853 / 3.326 / 527 / 17.396** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 207 / 344 | **551 / 223 / 328** |
| actos (componentes) | 150 | **134** |
| actos `CERRADOS` / `ABIERTOS` | 97 / 53 | **81 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 203 / 240 | **171 / 240** |
| cola de costuras | 1.471 | **1.467** |
| colisiones de clase vigentes | 0 | **0** |
| auto-pares (los dos lados al mismo vivo) | 185 | **201** |
| duplicadas historicas: grupos / nodos | 956 / 754 | **946 / 747** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (443 igual a 443; 344 igual a 344) | **TODAS OK (411 igual a 411; 328 igual a 328)** |

**LA APERTURA CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 58 MIDIO POR CORRIDA PROPIA**, y eso es
contraste, no fuente. Instrumentos de apertura corridos **ANTES de la primera operacion y con el
arbol limpio**: [`SALIDA_V59_APERTURA.txt`](SALIDA_V59_APERTURA.txt),
[`SALIDA_V59_MARCADOR_APERTURA.txt`](SALIDA_V59_MARCADOR_APERTURA.txt),
[`SALIDA_V59_RECOMPUTO_APERTURA.txt`](SALIDA_V59_RECOMPUTO_APERTURA.txt),
[`SALIDA_V59_COLA_APERTURA.txt`](SALIDA_V59_COLA_APERTURA.txt),
[`SALIDA_V59_COLISIONES_APERTURA.txt`](SALIDA_V59_COLISIONES_APERTURA.txt) y
[`SALIDA_V59_DUPLICADAS_APERTURA.txt`](SALIDA_V59_DUPLICADAS_APERTURA.txt). **Las tres que reescriben
sus ficheros salieron IDEMPOTENTES**, verificado por `git status`, con el aviso `LF/CRLF` de
`ARISTAS_DUPLICADAS.jsonl` comprobado por `git diff` **VACIO** antes de revertir con `checkout`.

**LAS CELDAS QUE SE MUEVEN EN 16 O EN 32 SON LAS QUE EL LOTE PREDECIA**, una por acto fundido o dos
por acto: vivos bajan 16, deprecados suben 16, colapsos suben 16, pares distintos bajan 16, actos
bajan 16, `CERRADOS` bajan 16, nodos en `CERRADOS` bajan 32 y auto-pares suben 16.

**LAS TRES CELDAS QUE NO SE MUEVEN ASI, MEDIDAS Y NO SUPUESTAS:**

1. **LOS ENLACES SUBEN 30 (17.366 a 17.396).** Contado nodo a nodo contra el arbol de la apertura
   (`c9927b19`): **21 nodos cambian**, **mas 40 repartidos entre 13 supervivientes** (el mayor,
   `programa_mejora_calidad_14_pasos`, de 14 a 23) porque cada superviviente hereda los vecinos del
   que muere, **y menos 10 en terceros nodos**, que son las entradas retiradas por `P.16` mas las
   que la fusion dedupica sola.
2. **LA COLA BAJA 4 (1.471 a 1.467).** Es el efecto de los pasos que se adosan y se apilan en los
   supervivientes, que cambia su cuenta de pasos y saca a cuatro nodos del corte de la cola.
3. **LAS DUPLICADAS BAJAN 10 (956 a 946 grupos), Y EL DIFF ESTA CORRIDO, NO SUPUESTO.** **CERO
   grupos NUEVOS fabricados por esta fusion.** Desaparecen **15** y aparecen **5**, y las dos cifras
   tienen nombre: los **5** que aparecen son **LOS MISMOS 5 QUE DESAPARECEN CON OTRO ROTULO**
   (`consejo_de_calidad_3`, `consejos_de_calidad`, `eliminacion_causas_error`,
   `make_certain_programa` y `zero_defects_concepto`, que pasan de tener por destino a
   `programa_de_mejora_de_calidad` a tenerlo a `programa_mejora_calidad_14_pasos`): **duplicadas
   VIEJAS que la fusion se limita a renombrar**. Los **10** restantes desaparecen porque **el nodo
   que las alojaba murio** y el censo solo cuenta vivos.

**TASA POR DOMINIO AL CIERRE**, leida de
[`SALIDA_V59_MARCADOR_CIERRE.txt`](SALIDA_V59_MARCADOR_CIERRE.txt): compras 0,6 (n 155) | core 22,5
(n 1.445) | entrega 1,2 (n 171) | environmental 16,5 (n 170) | exportacion 11,5 (n 130) |
franquicias 10,1 (n 148) | health_safety 22,4 (n 192) | quality 14,1 (n 844) | risk_management 0,0
(n 106) | seguridad_digital 11,1 (n 27). **IDENTICA a la de la apertura al digito, y no es
casualidad: fundir no voltea veredictos.** **El diff de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` entre
la apertura y `HEAD` es VACIO**, corrido y no supuesto.

---

## 1. TAREA 1.1: **LA ESPECIE DE LOS TITULOS TALLADOS ERA UNA POBLACION DE 280, NO DE DOS**

Nace **`scripts/loop/barrido_titulos_tallados.py`**, de **SOLO LECTURA** y de **NOMBRE ESTABLE**
(la vuelta entra por `--vuelta`; **el barrido NO SALE en su propio barrido**, comprobado, que es la
prueba minima de que no es un ejemplar de lo que caza).

**CALIBRADO CONTRA LOS DOS EJEMPLARES CONOCIDOS ANTES DE CREERLE NADA**, que es lo que impide que un
detector nuevo se declare bueno solo: los dos vuelven a caer, `vuelta56_varas_tramo3.py` linea
**101** (`TRAMO 3` y `vuelta 54` con el sujeto entrando por `--tramo`) y
`vuelta57_tramo4_nomina.py` linea **193** (`TRAMO = 4` **por indireccion de un paso**, con el sujeto
entrando por `--nomina`).

**LAS TRES CLASES, cada una decidida MIDIENDO:** `ROJO`, puede mentir (el sujeto entra por argumento
y el titulo no se entera); `AMBAR`, no calza con lo que el fichero declara de si mismo; `CENSO`,
sello fijo, que **no es deuda hoy**.

**LA SALIDA ENTERA ESTA EN [`SALIDA_V59_BARRIDO_TITULOS.txt`](SALIDA_V59_BARRIDO_TITULOS.txt) (315
lineas), y su linea de RESUMEN, que es de donde salen estas cifras, dice:**

```
RESUMEN: 366 ficheros barridos, 184 con hallazgo, 182 limpios | ROJO 32, AMBAR 35, CENSO 213, ILEGIBLE 1
```

**LOS TALLADOS SUMAN 280.** **APARTE, y NO es un tallado sino otra cosa: `ILEGIBLE 1`**,
`scripts/loop/vuelta35_pares_opd03.py`, que lleva un `BOM` y no parsea. **Dicho y no callado.**

**LO QUE EL BARRIDO NO DECIDE Y LO DICE EN SU PROPIA SALIDA:** un numero que no calza **o NOMBRA UN
ANCESTRO a proposito** (procedencia, y entonces no envejece nunca) **o ES UNA CITA ENVEJECIDA**. La
maquina no las separa y **no finge separarlas**; las lista juntas para el ojo. Fingir resolverlo por
regla habria sido estrenar doctrina, que es lo que la regla 5 prohibe.

**TRES FALSOS PROPIOS, CAZADOS Y CORREGIDOS EN LA MISMA PASADA Y DECLARADOS PORQUE LA PRIMERA
CORRIDA LOS PUBLICO:** la forma corta `_vNN_` no contaba como declaracion y daba **cuatro `AMBAR`
falsos**; y la regla del *print que sigue a una banda* se tragaba el cuerpo del informe
(`vuelta54_ejemplares_estrella.py` lineas **80** y **81**, `vuelta19_fase2.py` linea **50**, que son
leyenda y no titulo). **La figura que cierra un titulo es el `print()` VACIO**, y esa es la regla que
quedo.

**NADA SE REPARO A CIEGAS.** El encargo manda reparar **solo lo que esta vuelta o la siguiente
corran**, y asi se hizo, **AL USARLO** y no antes:

| instrumento | que traia | como quedo |
|---|---|---|
| `vuelta58_tallar_planes.py` | `TRAMO 4` tallado en el titulo, planes `PLAN_V57_*` fijos, `LOTES` fijos | sucesor **`tallar_planes_del_tramo.py`**, nombre estable, `--vuelta` y `--prefijo`, **el tramo leido del campo `tramo` del plan** y los lotes **descubiertos por existencia** |
| `vuelta57_planes.py` | `TRAMO 4 (vuelta 57)` tallado en el print de titulo | sucesor **`vuelta59_planes.py`**, con el tramo leido **de la clave del ordinal del fichero medido** (`orden_tramo5`) y la vuelta por `--vuelta` |
| `vuelta57_retirar_duplicada_por_alias.py` | clon por vuelta | sucesor **`retirar_duplicada_por_resolutor.py`**, de nombre estable: **la cadena de clones muere ahi** |

**LO QUE NO SE REPARO, Y POR QUE, para que no se lea como olvido:** el **abridor de tramo**
(`vuelta58_tramo5_nomina.py`, `ROJO` con `TRAMO = 5` por indireccion) **NO se toco**, porque **esta
vuelta no lo corre**: el insumo del tramo 5 esta FIJADO y el encargo prohibe re-medirlo. El acta 58
(pregunta 4) dice que **el proximo abridor NACE estable**, y nacer es cuando se cree, no ahora.
**El registro del tramo en `03_FUSIONES.md` TAMPOCO se escribe, y tampoco es olvido: ese registro es
el del CIERRE del tramo, y el tramo 5 sigue ABIERTO con 34 actos por hacer.** Escribirlo hoy seria
publicar un cierre que no ha ocurrido.

## 2. TAREA 1.2: **LA RATIFICACION DEL ACTA 58, ANOTADA JUNTO A LA CORRECCION DEL 32**

Una linea fechada al final de la `CORRECCION DECLARADA` del acto 32 en `docs/plan/03_FUSIONES.md`,
**con las dos lineas del acta citadas y LEIDAS HOY** (regla 1): el cuadro de varas re-derivado con
codigo propio del auditor calza **50 de 50 con `DISTINTAS 0`** (`ACTA_AUDITOR.md` linea **14735**), y
el acto 32 re-medido da **5 contra 5, 2 contra 2 y 3 contra 3, `EMPATE SIN VARA`** (linea **14743**).
**Nada de lo sellado se reescribe.**

---

## 3. TAREA 2: **EL LOTE A DEL TRAMO 5, DIECISEIS ACTOS DE DIECISIETE**

**Las tablas salen enteras de** `python scripts/loop/tallar_planes_del_tramo.py --vuelta 59`
([`SALIDA_V59_TALLAR_PLANES.txt`](SALIDA_V59_TALLAR_PLANES.txt)), **que las cuenta de los
`PLAN_V59_*.json` SELLADOS y cae en ROJO con el acto nombrado si un motivo no encaja en ninguna forma
conocida** (y cayo: las cinco frases nuevas del tramo 5 hubo que ensenarselas, ninguna forma vieja se
toco ni se renombro).

| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas nombradas |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **A** | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17 | **16** | **16** | **97** | 24 | 59 | **14** | **3** |

| la forma, leida del motivo sellado | cuantos | los actos |
|---|---:|---|
| **EL CONTENIDO EMPATA y EL CABLEADO DECIDE SOLO** | **4** | 2, 5, 10, 15 |
| **TODAS LAS VARAS de contenido de acuerdo** | **4** | 8, 12, 14, 17 |
| **UNA SOLA VARA de contenido no empatada, y BASTA** | **4** | 4, 6, 9, 16 |
| **CONTEOS QUE CHOCAN CON LA PIEZA DECLARADA, y decide la declarada** | **1** | 11 |
| **LA PIEZA DECLARADA GANA A LOS DOS CONTEOS de contenido** | **1** | 3 |
| **LA PIEZA DECLARADA GANA A UN CONTEO de contenido** | **1** | 7 |
| **LA PUERTA SOBREVIVE, con el choque registrado** | **1** | 1 |
| **suma** | **16** | |

**EL UNICO DECLARADO DEL LOTE ES EL ACTO 13** (`premio_shingo` contra `shingo_prize`), **`EMPATE SIN
VARA`**, y va a **LA MESA** dentro del pendiente de doctrina 1. Los tres conteos empatan al digito
(**4 contra 4, 2 contra 2, 2 contra 2**) y **la razon del puesto 2475 declara propio A LOS DOS
LADOS**, que es la figura exacta del acto 32. **Pesar dos propios declarados para romper un empate
triple es la rama que el acta 58 dejo NO ADOPTADA al deshacer el 32**, asi que no se usa. Va
**marcado como discutible** abajo.

**LAS GUARDAS, TODAS MEDIDAS Y NINGUNA AFIRMADA:**

| guarda | resultado |
|---|---|
| plan generado, 16 fichas | **TODAS en verde**: `1B` (ningun absorbido es puerta), cobertura exacta (cada paso y condicion con marca UNICA), incisos **EXTRAIDOS del nodo** y comprobados verbatim, junturas comprobadas antes de sellar |
| `P.16` antes de fundir | retira **2** entradas (`takt_time` y su reciproca) |
| simulacion sobre copia | **verde**, cero escrituras |
| delta de deprecados | **+16 sobre +16 esperado: OK** |
| reanclar entre la fusion y `run_phase1` | **NADA QUE RE-ANCLAR** |
| censo de colisiones con esperadas | **0 esperadas, 0 medidas, `CALZA: SI`** |
| duplicadas fabricadas | **CERO**, por **diff del conjunto de grupos** contra la apertura |
| `Gate 0` | **OK**, con **el ciclo de tres completo** (`run_phase1 --reaplico-curaduria`, `etiquetas_de_cara --aplicar`, `sync_assets_web`) |
| suite del motor | **25 de 25** |
| suite web | **80 ficheros, 1.030 pasadas, 3 saltadas** |
| `tsc --noEmit` | **CERO lineas** |
| caso positivo | **LAS SEIS GUARDAS MUERDEN**, sobre el acto 37 del tramo 3, **que esta vuelta no toca** (comprobado contra la nomina del tramo 5, no supuesto) |

---

## 4. EL HALLAZGO: **EL INSTRUMENTO DE `P.16` TENIA TRES DEFECTOS, Y LOS TRES SE MIDIERON**

La simulacion del lote A cayo en **ROJO**. El instrumento de la vuelta 57 dijo que
`definicion_calidad_conformidad` era una duplicada que **este plan NO fabrica**. **Se verifico contra
el grafo antes de tocar codigo (regla 9) y era FALSO.**

1. **EL CULPABLE SE BUSCABA POR EL LITERAL.** `programa_catorce_pasos_crosby` esta deprecado y lo
   reclama como alias **el absorbido del acto 1**; su resolucion **si** cambia con la fusion. El
   ancestro **resolvia los destinos por alias pero buscaba al culpable con `x in absorbidos`**, y el
   absorbido no estaba escrito en la lista: llegaba por su propio alias. **Es la misma grieta que el
   ancestro nacio para tapar, un salto mas adentro.**
2. **LA PRUEBA DE *YA ESTABA DUPLICADA* PREGUNTABA POR EL DESTINO DE DESPUES**, que **nunca** calza
   cuando la fusion renombra el destino. **Con la prueba buena** (si las entradas **ya compartian
   resolucion hoy**), `consejo_de_calidad_3`, `consejos_de_calidad`, `make_certain_programa` y
   `zero_defects_concepto` salen como duplicadas **VIEJAS de OP-S-12**. **El ancestro las daba por
   suyas y habria retirado OCHO entradas que no le tocaban.** Este es el defecto que hacia dano.
3. **LA REGLA DE *EL EJECUTOR DEDUPLICA SOLO* SE APLICABA DE MAS.** Vale solo cuando el culpable es
   el absorbido **literal**, porque solo a ese lo sustituye el ejecutor. **Lo destapo el censo del
   cierre, no un razonamiento:** con la regla vieja,
   `definicion_calidad_conformidad | nodos_siguientes` quedo **fabricada y sin limpiar**, y aparecio
   como **grupo NUEVO** en el diff contra la apertura.

Nace **`scripts/loop/retirar_duplicada_por_resolutor.py`**, **copiado byte a byte del ancestro** y
con los tres cambios declarados en su docstring, **de nombre estable**. Y como el tercero se
descubrio **con el lote ya fundido**, y aquel instrumento solo sabe correr **antes** de fundir, nace
tambien **`scripts/loop/retirar_entrada_redundante.py`** para limpiar el caso a posteriori, con **la
guarda que lo hace legitimo**: no retira nada si **otra entrada de la misma lista no resuelve ya al
mismo destino**, porque entonces no seria redundante sino un camino. **Tras limpiarla, el diff del
censo contra la apertura da CERO grupos fabricados.**

**SE DECLARA EL COSTE:** limpiar a posteriori obligo a **re-correr el ciclo de `Gate 0` entero y las
tres suites por segunda vez**, y a **re-medir el cierre entero**, porque la primera medicion de
cierre ya estaba tomada cuando el diff destapo la duplicada. **La cabecera publicada es la SEGUNDA,
la de despues del ultimo movimiento**, que es lo que la regla 1 manda.

---

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

| | que hice | por que se puede discutir |
|---|---|---|
| **D1** | **NO EJECUTE LOS LOTES B Y C: 34 actos de 50 sin hacer.** Entregue el lote A entero con sus guardas en verde y lo digo primero | El acta 58 (pregunta 6) dice que **un lote corto pero completo vale** y que la unidad minima es el lote entero, asi que la conducta esta cubierta; pero es **la segunda vuelta seguida** en que el tramo 5 no se cierra, y un lector estricto puede decir que la TAREA 1 y la caceria del `P.16` se comieron el tiempo de dos lotes |
| **D2** | **DECLARE el acto 13 en vez de fundirlo**, por empate triple con propio declarado a los dos lados | Hay una lectura sostenible **en contra**: cuando la razon clasifica el propio de un lado como **LINEA** esta diciendo que **no lo cuenta**, y entonces el propio declarado seria **de un solo lado** y por acta 54 pregunta 4 **seria vara**, y el 13 se fundiria hacia `premio_shingo`. No la aplique porque decidirlo asi **estrena doctrina sobre un empate**, y deshacer una fusion cuesta una vuelta entera, como acaba de costarla el 32 |
| **D3** | **FUNDI el acto 3 contra los DOS conteos de contenido**, por la pieza declarada | La letra dice *si dos varas de contenido CHOCAN decide la pieza DECLARADA*, y aqui los dos conteos **no chocan entre si**: chocan **con** la declarada. Lo sostengo porque la razon dice que el paso de mas **no anade nada** (mide formato, no sustancia), pero es la primera vez que la declarada gana a **dos** conteos y no a uno |
| **D4** | **FUNDI el acto 1 hacia la PUERTA, contra lo que la razon declara** | Es el carril del acta 54 pregunta 1 y el choque queda registrado en el motivo; pero **la razon dice literalmente `Sobrevive programa_de_mejora_de_calidad`** y aqui muere. Se dice ademas que **los conteos tampoco acompanan a la razon**, para que nadie lea la guarda como coartada |
| **D5** | **NO adose la duracion de *hasta 6 semanas* en el acto 16** y la deje como perdida nombrada | La razon avisa que las dos duraciones **no cuadran** y que la fusion **tiene que resolverlo, no apilarlas**, asi que elegir era obligatorio; pero **cual de las dos vive no lo decide ninguna vara de la casa**, solo la regla de no apilar. La razon misma lo marco `DISCUTIBLE PARA LA R55` |
| **D6** | **NOMBRE la perdida del acto 4 en vez de reponerla**, siendo perdida **de nombre** (`TAGUCHI`) | La razon pide **reponer el nombre en el titulo o en la primera linea del superviviente**, y no se hizo. Mi motivo: el contrato del ejecutor **no toca `titulo_concepto`** y `TAGUCHI` **no aparece en ningun paso**, solo en titulo y entregable, asi que no hay trozo verbatim que mover. Un lector estricto puede decir que entonces **el acto no estaba listo para fundirse** |
| **D7** | **LIMPIE a posteriori una duplicada ya fabricada**, con un instrumento nuevo | `P.16` dice *quien fabrica limpia* y la limpieza esta guardada; pero **es una escritura sobre el grafo despues de que el lote estaba cerrado y sus suites en verde**, y obligo a re-correr todo. La alternativa era **declararla y dejarla al encargo siguiente** |
| **D8** | **ENMENDE el titulo de un commit propio ya hecho** (decia 281 ejemplares, y son 280 tallados mas 1 ilegible, que es otra especie) | No estaba pusheado y la enmienda **queda declarada en el propio mensaje y aqui**; pero la casa prefiere **no tapar lo que se corrige**, y una enmienda tapa el texto viejo. Lo sostengo porque un numero equivocado en un titulo de commit **se cita despues como fuente** |

---

## 6. PENDIENTES DE DOCTRINA

- **1, PARA LA MESA, con TRECE actos** (los doce heredados **mas el acto 13 de este tramo**). La
  rama de **la cantidad como vara** sigue **NO ADOPTADA** y **no se uso en ningun acto** de este
  plan.
- **2 (INCISO), 3, 4, 5 y 7: HEREDADOS SIN CAMBIO.** No se pagan hoy.
- **6: CONTESTADO por el acta 58** (pregunta 4) y **aplicado en esta vuelta** en los tres
  instrumentos de nombre estable.
- **NUEVO, y no pide doctrina sino barrido:** el `AMBAR` del barrido **junta dos especies que la
  maquina no separa** (procedencia contra cita envejecida). No propongo regla: **propongo que el ojo
  las separe** sobre los 35 listados, que es trabajo, no doctrina.

## 7. PREGUNTAS PARA EL AUDITOR

1. **El acto 13: `EMPATE SIN VARA` o `LA PIEZA DECLARADA DECIDE`?** Cuando la razon llama **LINEA**
   al propio de un lado y **PASOS** al del otro, esta **pesando dos propios** (y entonces es empate,
   como el 32) o **descartando uno** (y entonces la vara es de un solo lado)? Es el `D2` y decide
   una fusion real.
2. **La declarada gana a DOS conteos?** (`D3`.) La letra habla de varas que **chocan entre si**. Un
   conteo de pasos que la propia razon declara **inflado por formato** sigue siendo vara?
3. **Limpiar a posteriori o declarar?** (`D7`.) `P.16` dice quien fabrica limpia, pero no dice si
   *limpia* alcanza a **despues de cerrar el lote**.
4. **Un acto cuya perdida nombrada el instrumento NO PUEDE reponer, se funde igual?** (`D6`.)
5. **Enmendar un commit propio no pusheado con una cifra mala: correccion o tapadura?** (`D8`.)
6. **El reparto de la vuelta fue el correcto?** (`D1`.) La TAREA 1 pedia un instrumento nuevo y la
   caceria del `P.16` no estaba encargada: valia mas **parar el barrido a la mitad** y sacar el lote
   B, o esta bien haber cerrado la especie y entregado un solo lote?

## 8. MIS PROPIOS MANEJOS Y TROPIEZOS, declarados

- **La primera corrida del barrido publico tres falsos mios** (cuatro `AMBAR` por la forma corta
  `_vNN_`, y tres lineas de leyenda tomadas por titulo). Los cace **cotejando contra los ficheros**
  antes de creerme el numero, y quedan escritos en el docstring del instrumento **con nombre y
  linea**. Coste: dos corridas, cero cifras publicadas.
- **Enmende el titulo del commit `fd7de724`** (decia 281 y son 280). Declarado en el propio mensaje.
- **Tome la medicion de cierre dos veces** porque el diff del censo destapo la duplicada despues de
  la primera. **La publicada es la segunda.** Coste: un ciclo entero de `Gate 0` y tres suites.
- **La trampa del `vitest`, ya conocida y esquivada otra vez:** con `--reporter=basic` revienta al
  crear el servidor; sin la bandera corre limpio. **Es de entorno, no del codigo.**

## 9. LO QUE QUEDA, DICHO SIN ADORNO

**EL TRAMO 5 SIGUE ABIERTO.** Hechos **16 de 50**; faltan **los actos 18 a 50**, que son **34**, y su
insumo **sigue fijado y no hay que re-medirlo** (nomina `TRAMO5_V58.jsonl`, cuadro de varas
`SALIDA_V58_VARAS_TRAMO5.txt`, colisiones esperadas CERO, dossier de 1.979 lineas). **La vuelta
siguiente empieza por el plan del lote B, en el acto 18**, y corre `P.16` **con el instrumento ya
arreglado** antes de fundir. **El registro del tramo en `03_FUSIONES.md` se escribe cuando el tramo
CIERRE, no antes.**
