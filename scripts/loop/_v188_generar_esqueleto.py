# -*- coding: utf-8 -*-
"""_v188_generar_esqueleto.py . GENERA scripts/loop/vuelta188_esqueleto_reporte.py
COMO CLON DECLARADO del de la 187, cambiando solo VUELTA, TAREAS, el docstring y
el bloque de prosa del encabezado. Auxiliar de una sola vuelta: no es guarda, no
entra en la nomina y no publica ninguna cifra."""
import io

NL = chr(10)
src = io.open("scripts/loop/vuelta187_esqueleto_reporte.py",
              encoding="utf-8").read().replace(chr(13) + NL, NL)

src = src.replace("VUELTA = 187", "VUELTA = 188", 1)

ini = src.index('r"""')
fin = src.index('"""', ini + 4) + 3
doc = 'r"""vuelta188_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 188,\n\
TALLADO EN LA APERTURA PARA QUE UNA VUELTA CORTADA DEJE REPORTE PARCIAL Y NO VACIO.\n\
\n\
CLON DECLARADO de scripts/loop/vuelta187_esqueleto_reporte.py. Cambia el numero\n\
de vuelta, la lista TAREAS, este docstring y el bloque de prosa del encabezado.\n\
El cotejo del clon lo hace scripts/loop/cotejar_clon_declarado.py y su salida se\n\
pega en el reporte con lo que salga: AQUI NO SE AFIRMA QUE NINGUN DIFF SALGA\n\
VACIO.\n\
\n\
Y AQUI SE EJECUTA EL REMEDIO DE LA `C.1` DE LA VUELTA 187 (acta 188, seccion 8;\n\
encargo de la 188, TAREA 5.c). La 187 tallo su esqueleto DESPUES de la TAREA 1 y\n\
lo declaro, con una causa que el acta corrige: es cierto que el esqueleto\n\
necesita que SALIDA_V<N>_HEAD_APERTURA.txt este COMMITEADO para leer su commit de\n\
nacimiento con git log --diff-filter=A, y NO es cierto que eso obligue a esperar\n\
a la TAREA 1. La vuelta 186 lo hizo en TRES commits (793ad9a1 apertura ->\n\
88bd3216 esqueleto en su propio commit -> 456f0847 tarea 1). ESTA VUELTA HACE LO\n\
MISMO: apertura y su commit, esqueleto y SU PROPIO COMMIT, y despues las tareas.\n\
El remedio cuesta un commit y estaba en uso hace dos vueltas.\n\
\n\
ESTA VUELTA NO ES DE BATERIA (AUDITOR.md 6.1: corre cada cinco vueltas y cerro\n\
entera en la 184, asi que la siguiente es la 189), y su seccion 9 cierra CON EL\n\
HUECO DECLARADO Y MEDIDO: nombre del fichero, bytes medidos y atribucion, las\n\
tres juntas o no vale. Y ESTA VUELTA NO ESCRIBE DOS SECCIONES 9, que es la `C.4`\n\
del acta 188: la unica seccion 9 es la que talla cerrar_reporte.py.\n\
\n\
LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:\n\
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en\n\
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la\n\
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.\n\
\n\
LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla\n\
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 188 AL CIERRE.\n\
\n\
LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por\n\
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y\n\
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de\n\
docs/loop/SALIDA_V188_HEAD_APERTURA.txt, sellado antes de la primera operacion;\n\
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si\n\
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada:\n\
no inventa un hash.\n\
\n\
Y SE DECLARA EL DESFASE QUE NO SE REPARA, POR CUARTA VUELTA: PATRONES_ACTA\n\
sigue pidiendo el acta de VUELTA - 1, o sea la 187, cuando el acta que ORDENA\n\
esta vuelta es la 188. Es el `D.2` del reporte de la 184, adjudicado a favor por\n\
la `5.2` del acta 185 CON REPARACION ENCARGADA, y esta vuelta NO la ejecuta\n\
porque su encargo trae cinco tareas y ninguna es esa.\n\
\n\
USO:\n\
  python scripts/loop/vuelta188_esqueleto_reporte.py\n\
"""'
src = src[:ini] + doc + src[fin:]

T1 = ("LOS REGISTROS. BLOQUEANTE. El acta 188 entra en la serie con el numero que "
      "devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus "
      "SEIS adjudicaciones `5.1` a `5.6` todas a favor, los TRES numerales de la seccion "
      "6 (`PD.1` ABIERTA con sus cinco puestos leidos del acta, `PD.8` ABIERTA, y el "
      "`6.3` como ANOTACION), las TRES preguntas de la seccion 7 las tres CONTESTADAS, "
      "CERO caidas propias del auditor registradas COMO CERO Y NO OMITIDAS, y CUATRO "
      "caidas del ejecutor todas DE METODO y NINGUNA DE RACHA: `C.1` y `C.2` declaradas "
      "por el ejecutor y `C.3` y `C.4` levantadas por el auditor, LAS CUATRO ATRIBUIDAS "
      "AL EJECUTOR porque la atribucion la hace la cabecera de la seccion y no quien las "
      "encontro. Mas la deuda de la serie REMEDIDA en esta vuelta. Con caso positivo por "
      "mutacion sobre un acta FABRICADA y el esperado mutado cayendo, y con la PARADA "
      "conservada entera: un estado que el registrador no sepa leer sigue siendo PARADA")
T2 = ("EL PLAN: LAS CUATRO FICHAS QUE LA VARA NOMBRA, RESUELTAS CONTRA SU EVIDENCIA. "
      "`scripts/loop/vuelta150_3_relectura_expediente.py --corte <HEAD de apertura>` "
      "corrida con corte propio y no copiada del acta; las cuatro fichas `OP-L-01`, "
      "`OP-L-02`, `OP-L-03` y `OP-I-01` LEIDAS ENTERAS Y CITADAS de "
      "`docs/plan/OPERACIONES.jsonl`; el producto de cada una MEDIDO contra la "
      "`evidencia` que la propia ficha nombra, con bytes por las dos convenciones y la "
      "cuenta prometida contra la cuenta que hay; LA VARA GANA SU PATA DOCUMENTAL EN "
      "CODIGO para las fichas de tipo `MESA`, con la cifra vieja publicada entera y al "
      "lado; el estado de cada una declarado en una de las tres formas (su producto la "
      "cubre, esta pero no la cubre, o no hay evidencia y es PARADA); y el desfase de sus "
      "cortes medido y publicado. NO se toca el campo `estado`, NO se reescriben las "
      "fichas y NINGUN VEREDICTO SE MUEVE")
T3 = ("EL CASO E: EL INVENTARIO DE EXENCIONES EN VEZ DE UNA CUENTA TECLEADA. BLOQUEANTE "
      "PORQUE LA BATERIA ES LA 189. El caso E de "
      "`scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py` deja de contar un texto "
      "y pasa a COMPUTAR EL INVENTARIO de guardas eximidas en el carril tardio CON SUS "
      "NOMBRES, leido del fuente, y a cotejarlo contra una LISTA AUTORIZADA Y ESCRITA que "
      "hoy tiene DOS entradas con su vuelta y su decision al lado. Cae en rojo en TRES "
      "casos y los tres se prueban: una exencion fuera de la lista, una de la lista que "
      "desaparece, y una eximida que NO exige su declaracion. Los otros diecisiete casos "
      "no se tocan. Mas (b) el `sha256` del sujeto al lado de todo numero de linea que un "
      "arnes publique, y (c) la doble corrida de la nomina EXCLUYENDO explicitamente "
      "cualquier arnes que ya haya salido en rojo en esa misma vuelta, DICIENDOLO en su "
      "salida")
T4 = ("LA ESCALADA: LA GUARDA QUE VE LA MITAD, Y LA SECCION QUE SE DUPLICA. `AUDITOR.md` "
      "1.2, mandatorio con la racha de reporte en dos. (a) `parejas_publicadas()` "
      "ensancha sus formas para cubrir las TRES que hoy se le escapan, leidas de reportes "
      "reales; LA REGLA DE LA AMBIGUEDAD NO SE TOCA; y la guarda PUBLICA SU COBERTURA, "
      "cuantas parejas ve contra cuantas rutas con cifra de bytes hay y cuantas quedan "
      "sin atribuir POR AMBIGUAS nombradas una a una. (b) `piezas_que_faltan()` exige que "
      "las secciones sean UNICAS Y ESTEN EN ORDEN, no solo que existan, que es la `C.4`. "
      "Con arnes obligatorio que incluye un caso por cada forma nueva con su mutacion "
      "cayendo, un caso de ambiguedad que exija NO atribuir, un caso sobre el texto real "
      "de `git show 9a06b7c8` exigiendo SEIS parejas vistas y SEIS que calzan, y un caso "
      "sobre ese mismo texto que ACUSE las dos secciones 9 nombrando sus dos lineas")
T5 = ("LA RELECTURA AL DOBLE, LOS DOS REMEDIOS PEQUENOS Y EL CIERRE. (a) La relectura al "
      "doble del tramo de la ciega del acta 188, encargada por `AUDITOR.md` 1.2 porque la "
      "discrepancia del auditor (el puesto 1202) cayo FUERA del discutible de clase "
      "marcado: cotejo de `sha256` contra el sello `V189` ANTES de leer un solo puesto, "
      "30 puestos mas 30 vecinos deterministas con `vecinos()` IMPORTADA y no copiada, 60 "
      "releidos que es el doble exacto, NINGUNA CLASE SE VUELVE A DECIDIR; mas el remedio "
      "del `D.2`, que es un conjunto `evitar` OPCIONAL para `vecinos()` que deja su "
      "conducta de hoy intacta sin el, y los TRES solapes del UNIVERSO publicados; mas el "
      "puesto 1202 mirado con la misma vara; mas la cuenta de cuantos de los 60 llevan en "
      "su razon evidencia DE FAMILIA y no del par. (b) "
      "`docs/loop/DISCUTIBLES_DE_CLASE_V188.txt` con los puestos de los discutibles DE "
      "CLASE y nada mas. (c) El esqueleto tallado en la apertura y en su propio commit, "
      "que es la `C.1`. (d) El reporte se abre, se llena por anexion y se cierra con "
      "`cerrar_reporte.py --vuelta 188` y `archivar_reporte.py --vuelta 188`, con UNA "
      "SOLA SECCION 9")

t_ini = src.index("TAREAS = [")
t_fin = src.index(NL + "]" + NL, t_ini) + len(NL + "]" + NL)
bloque = ["TAREAS = ["]
for n, t in (("1", T1), ("2", T2), ("3", T3), ("4", T4), ("5", T5)):
    bloque.append('    ("%s", %r),' % (n, t))
bloque.append("]")
src = src[:t_ini] + NL.join(bloque) + NL + src[t_fin:]

PROSA = """> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que no lleva nada
> mas. **Cerro entera en la 184**, con sus nueve tramos sellados, asi que **la
> siguiente vuelta de bateria es la 189, o sea la que viene**. En las vueltas
> intermedias la seccion 9 se cierra igual, con el **nombre del fichero, sus
> bytes medidos y su atribucion**, las tres juntas o no vale.
>
> **Y ESTA VUELTA ESCRIBE UNA SOLA SECCION 9**, que es la `C.4` del acta 188: el
> reporte de la 187 llevaba **dos**, en las lineas 870 y 920, con la `## 10.` en
> medio. Lo que esta vuelta tenga que decir de la bateria va **en la que talla
> `scripts/loop/cerrar_reporte.py`**, no en una segunda escrita a mano.
>
> **EL TOPE SIGUE EN CINCO, Y ESTA MEDIDO EN VEZ DE DARSE POR BUENO.** El regimen
> temporal `AUDITOR.md` 6.2 quedo cumplido y apagado en la 187. El **bloque H.0**
> del sello de apertura de esta vuelta midio **las tres** salidas de cierre,
> `docs/loop/SALIDA_V185_CERRAR_REPORTE.txt`,
> `docs/loop/SALIDA_V186_CERRAR_REPORTE.txt` y
> `docs/loop/SALIDA_V187_CERRAR_REPORTE.txt`, y **las tres dicen `CIFRA piezas que
> faltan: 0`**. Esta vuelta lleva **CINCO tareas**.
>
> **DONDE SE TALLO ESTE ESQUELETO, Y ESTA VEZ LA RESPUESTA ES EN LA APERTURA.**
> Es el remedio de la `C.1` de la 187, escrito en la TAREA 5.c del encargo: la
> vuelta 187 lo tallo **despues de la TAREA 1**, y el acta 188 le corrigio la
> causa midiendola contra la vuelta 186, que hizo lo mismo **en tres commits**
> (`793ad9a1` apertura, `88bd3216` **esqueleto en su propio commit**, `456f0847`
> tarea 1). **Aqui va igual: apertura y su commit, esqueleto y SU PROPIO COMMIT,
> y despues las tareas.** Desde el segundo commit de esta vuelta ya hay reporte
> parcial en el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** **no se abren
> las mesas anotadas** (la del `PMF` con los puestos 338, 297 y ahora 670, la del
> **603** y la de figuras del **226**), que el `6.3` del acta 188 deja como
> ANOTACION y no encarga; **no se poda la nomina de la bateria**, que es la opcion
> `c` que el fundador RECHAZO el 5 sep; **no se anade ningun campo a
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**, que es la `PD.8` y es del fundador;
> **no se toca el campo `estado` de `docs/plan/OPERACIONES.jsonl`**, declarado
> HISTORICO el 4 sep 2026; **no se reabre `docs/loop/reportes/REPORTE_V184.md`**;
> y **no se mueve ningun veredicto**: el `sha256` LF del archivo abre y tiene que
> cerrar en el mismo valor. Y **no se toca `dataset/`**: el `numstat` se mide al
> entrar y al salir y las dos cifras se publican.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** **Una columna de apertura medida
> al cierre es caida que ACUMULA.**

"""
a = src.index("> **ESTA VUELTA NO ES DE BATERIA")
b = src.index("**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**")
src = src[:a] + PROSA + src[b:]

src = src.replace("## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO",
                  "## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO")

io.open("scripts/loop/vuelta188_esqueleto_reporte.py", "w",
        encoding="utf-8", newline=NL).write(src)
print("escrito scripts/loop/vuelta188_esqueleto_reporte.py (%d bytes)"
      % len(src.encode("utf-8")))
