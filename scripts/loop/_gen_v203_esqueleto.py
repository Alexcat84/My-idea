# -*- coding: utf-8 -*-
r"""_gen_v203_esqueleto.py . GENERA scripts/loop/vuelta203_esqueleto_reporte.py
COMO CLON DECLARADO DE LA 202, COPIANDO TODO LO DEMAS BYTE A BYTE.

Fichero de computo con PREFIJO DE GUION BAJO: fuera del censo y fuera de la
nomina, que es lo que el `4.5` del acta 199 llama COMPUTO DE UNA VUELTA y lo que
el encargo de esta vuelta autoriza por su nombre. Cambia EXACTAMENTE cuatro
cosas y las imprime una a una: el docstring, la constante `VUELTA`, la lista
`TAREAS` y el bloque de prosa del encabezado del reporte. TODO LO DEMAS,
incluidas las cinco funciones puras y las guardas del PASO 0, se copia sin
tocar, y al final se COTEJA cuantas lineas vinieron sin tocar y cuantas son
nuevas, contadas con `difflib` y no a ojo, que es como la 202 lo hizo en su
TAREA 4.
"""
import difflib
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FUENTE = os.path.join(RAIZ, "scripts", "loop", "vuelta202_esqueleto_reporte.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop", "vuelta203_esqueleto_reporte.py")

DOCSTRING = 'r' + chr(34) * 3 + '''vuelta203_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 203,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta202_esqueleto_reporte.py, generado de el
programaticamente con `scripts/loop/_gen_v203_esqueleto.py`. Cambia el numero de
vuelta, la lista TAREAS, este docstring y el bloque de prosa del encabezado. EL
CODIGO DE LAS FUNCIONES VA IGUAL, byte a byte, porque se copio y no se re
escribio.

POR QUE CUATRO TAREAS, Y LA CIFRA NO SE TECLEA: la racha de cierres, contada del
instrumento en el bloque `E` del sello de apertura de ESTA vuelta, vale 4, con
las vueltas 199, 200, 201 y 202. `AUDITOR.md` 6.2 apaga el regimen temporal de
dos sub-tareas cuando DOS VUELTAS SEGUIDAS cierran su propio reporte con
`cerrar_reporte.py`, y con racha 4 SE APAGA y vuelve el tope de CINCO. El encargo
trae CUATRO. LA CIFRA SE LEE DEL SELLO, con `racha_del_sello()`, y si el sello no
la trae este esqueleto CAE EN ROJO y no escribe nada.

Y ESTA NO ES VUELTA DE BATERIA: la 200 lo fue y cerro entera, y por la cadencia
de `AUDITOR.md` 6.1 le toca a la 205. La seccion 9 cierra con el HUECO DECLARADO
Y MEDIDO por el carril de `cerrar_reporte.py`. El trabajo de esta vuelta es EL
PLAN, que es lo que la moratoria 6.3 manda.

EL DESFASE DE `PATRONES_ACTA` NO APARECE EN ESTA VUELTA, Y ESO SE MIDE EN VEZ DE
SUPONERSE: `PATRONES_ACTA` pide el acta de `VUELTA - 1`, o sea la 202, y el acta
que ORDENA esta vuelta ES la 202. El literal `DESFASE DECLARADO` se sigue
CONTANDO de los reportes archivados, con su fecha de corte, porque esa cifra es
de inventario y envejece sola.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

USO:
  python scripts/loop/vuelta203_esqueleto_reporte.py
''' + chr(34) * 3

T1 = ('LOS REGISTROS. LA CORRECCION DECLARADA DE `R.63` Y `R.64`, Y SU REPARTO '
      'REAL, que es el remedio de la `C.E1` de la 202 y va PRIMERA porque '
      '`AUDITOR.md` 1.4 pone los registros en la TAREA 1. **LO QUE SE CORRIGE '
      'ES UNA FRASE FALSA**: las dos entradas dicen que las adjudicaciones de '
      'las actas 173 y 174 viven en la **seccion 6 sin clave numerada**, y el '
      'acta 202 midio en su `4.1` que **SI estan numeradas** (la 173 de `6.1` a '
      '`6.5` y la 174 de `6.1` a `6.10`), y que lo unico que les falta son las '
      'comillas inversas. **Las dos lineas se miden aqui y no se copian del '
      'encargo.** **EL CARRIL ES EL DE `OP-L-03` DE LA 202**: banco `9.10`, '
      '**POR ADICION**, con el texto viejo **entero, sin tachar y sin borrar**, '
      'y la correccion fechada debajo. **Y EN LA MISMA ADICION VA EL REPARTO '
      'REAL** de las dos actas por la vara adjudicada en el `4.1`: **el numeral '
      'se toma de la seccion cuyo PROPIO TITULO lo nombra, nunca del numero de '
      'seccion**, y dentro de ella las claves se cuentan por su propia '
      'numeracion `N.M`, **lleve o no comillas inversas**; y **cada entrada '
      'declara que uso esa vara**. **EL COMPUTO VA EN UN `_v203_*`**, fuera del '
      'censo y de la nomina; **los lectores heredados se IMPORTAN** y lo unico '
      'que se ensancha es el patron de clave, **con parametro opcional para que '
      'los llamantes viejos no se toquen**. **LAS DOS LECTURAS SE PUBLICAN '
      'JUNTAS** (el `0` del heredado, que es cierto, y lo que da la vara '
      'adjudicada) y **la discrepancia se declara**. **GUARDA OBLIGATORIA Y '
      'CORRIDA DOS VECES**, con **crecimiento 0** la segunda')

T2 = ('LA CORRECCION DECLARADA DE LA `verificacion` DE `OP-L-01`, EN SU SEDE, '
      'adjudicada por el acta 202 en su `4.4`. **EL CARRIL, IDENTICO AL DE '
      '`OP-L-03` DE LA 202**: banco `9.10`, **POR ADICION**, un elemento mas de '
      'la misma lista, **sin clave nueva de esquema** y **sin tocar ni tachar '
      'el texto viejo**. La ficha vive en la **linea 41** y se cita por **linea '
      'mas indice**. **TRES COSAS OBLIGATORIAS, MEDIDAS HOY**: que `las_once()` '
      '**no devuelve once** sino toda cabecera `LD` que haya hoy en '
      '`docs/plan/LECTURAS_DIRIGIDAS.md`, con **la cifra de hoy y la del corte '
      '2026-09-04 y sus dos fechas**; la **comparacion resuelta** de hoy contra '
      'la congelada y **los puestos implicados**, cada cifra con su corte; y '
      '**la que no puede faltar**, que en comparacion **LITERAL** siguen '
      'apareciendo **0**, o sea que **la clausula 1 NO se cae** y lo que '
      'envejecio es la cifra de la excepcion. **LA PROMESA VIEJA NO SE RETIRA Y '
      'NO ES UNA MENTIRA**: con su corte era cierta. **`OP-L-01` NO SE CIERRA** '
      'y su `estado` no se toca. **GUARDA OBLIGATORIA**: **1 sola linea** de '
      '`OPERACIONES.jsonl` distinta (la **41**), **1 sola clave** '
      '(`verificacion`), los **6** elementos viejos **identicos y en su orden**, '
      'su `estado` igual al entrar y al salir, y **0 de las 71 fichas** moviendo '
      '`estado`. **CORRIDA DOS VECES**, con **crecimiento 0** la segunda')

T3 = ('`OP-I-01` CONTRA EL CRITERIO DE HECHO, LA CUARTA FICHA REAL: **la unica '
      'de las cuatro que la vara del plan da como trabajo real y que nadie ha '
      'medido contra el criterio de HECHO**. La 201 le corrigio la `evidencia`; '
      '**nadie le ha mirado la `verificacion`.** Se mide contra el criterio de '
      'hecho de `docs/plan/08_VERIFICACION.md` **citado por linea**, con su '
      '`verificacion` citada por **linea 44 mas indice** (**se comprueba la '
      'linea, no se supone**). **Y EL CRITERIO SE APLICA COMO EL ACTA 202 LO '
      'APLICO EN SU `4.3`**: no basta con que las clausulas salgan cumplidas '
      'hoy, se pregunta **clausula por clausula si SE CAERIA SI EL FALLO '
      'VOLVIERA**, y si alguna solo pasa porque alguien la remide a mano, **se '
      'dice, y esa ficha no se cierra**. **Si hay instrumentos suyos se '
      'IMPORTAN y se corren tal cual**, comprobando **ANTES** que no escriben, '
      'y **comprobandolo de verdad**, que es la caida `C.2` del auditor de la '
      '202. **PROPONE, NO CIERRA**')

T4 = ('LA DEUDA. `R.65` Y `R.66`, LAS ACTAS 175 Y 176, por el `4.9` del acta '
      '201: la deuda son las **175 a 180**, **DOS POR VUELTA**, de la mas vieja '
      'a la mas nueva. Va **DETRAS** del trabajo de plan y nunca delante. '
      '**Eran 8 y quedan 6.** `R.65` para el **acta 175** y `R.66` para el '
      '**acta 176**, en `docs/PENDIENTES.md`. **LAS DOS SON DE LA CONVENCION '
      'VIEJA**, asi que usan **la vara adjudicada en el `4.1` del acta 202**, '
      'la misma que la TAREA 1, y **cada entrada declara que la uso**. **SE '
      'REUTILIZA EL COMPUTO DE LA TAREA 1: no se escribe un segundo.** **Cada '
      'acta se acota EN ESTA VUELTA** por linea de inicio y fin, con su reparto '
      'entero. **SI EL REPORTE ARCHIVADO NO EXISTE, NO SE FABRICA**: se declara '
      'la ausencia con `os.path.isfile` y `os.path.getsize` y se usa la vara '
      'del `4.7` del acta 201, **declarandolo**. **CIERRA CON LA SERIE '
      'MEDIDA**: entradas, colisiones, huecos y siguiente libre')

TAREAS_TXT = ("TAREAS = [" + NL
              + "".join("    (%r, %r)," % (n, t) + NL
                        for n, t in (('1', T1), ('2', T2), ('3', T3), ('4', T4)))
              + "]")

PROSA = '''> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta%(v)d_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA.** La
> 200 lo fue y cerro entera; `AUDITOR.md` 6.1 dice que la bateria corre **cada
> cinco vueltas**, en vuelta propia, y por esa cadencia **le toca a la 205**. Aqui
> la **seccion 9 cierra igual**, con el **HUECO DECLARADO Y MEDIDO** por el carril
> de `cerrar_reporte.py`, que lleva **su nombre, sus bytes medidos y su atribucion,
> las tres juntas, o no vale**. El bloque `I` del sello de apertura ya lo midio:
> **0 ficheros `SALIDA_V%(v)d_BATERIA_TRAMO_N.txt`** y
> **`docs/loop/SALIDA_V%(v)d_BATERIA.txt` NO EXISTE**.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3, decision del fundador
> del 7 sep 2026), **con su linea exacta ya adjudicada, asi que aqui no se vuelve a
> discutir**: el `4.5` del acta 199 dice que la moratoria prohibe **arneses, guardas
> y lectores QUE SE QUEDEN VIGILANDO**, y que **un computo de una vuelta que muere
> con ella no es eso**. Por eso todo lo que esta vuelta escribe son ficheros
> `_v203_*` **con prefijo de guion bajo, fuera del censo y fuera de la nomina**, y
> los lectores que hacen falta **se IMPORTAN**. **La nomina queda CONGELADA EN
> 135**, y el bloque `F` del sello de apertura la midio contra ese congelado sin
> tocarla. **EL TRABAJO ES EL PLAN**, que es para lo que el bucle existe.
>
> **EL TOPE DE SUB-TAREAS ES CINCO, Y LA CIFRA QUE LO MANDA NO SE TECLEA.**
> El bloque `E` del sello de apertura de esta vuelta corrio el instrumento de la
> racha sobre el inventario ENTERO y **la racha de cierres vale %(racha)s**, con las
> vueltas **%(cuales)s**. `AUDITOR.md` 6.2 apaga el regimen temporal de dos
> sub-tareas cuando **DOS vueltas seguidas** cierran su propio reporte con
> `cerrar_reporte.py`, y con **%(racha)s** **SE APAGA**. **Este encargo trae CUATRO,
> y cabe.** **Y ese mismo bloque corrio el instrumento de la racha COMPROBANDO ANTES
> SI ESCRIBE**, que es la caida `C.2` del auditor de la 202: pisa su propia salida
> sellada, asi que se midio antes, se corrio, y la sellada se **RESTAURO con
> `git checkout --` y se REMIDIO IDENTICA**.
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. **El desfase de calibrado se midio
> DENTRO del bloque de apertura y ANTES de la primera operacion.** Y su bloque `F`
> publica la cifra de arneses del censo fuera de la nomina **con su vara al lado y
> las dos medidas**: con vara **%(vara)s** salen **%(conv)s** y sin vara salen
> **%(sinv)s**. **Esas son las cifras de HOY.**
>
> **LO QUE EL ACTA 202 ADJUDICO NO SE VUELVE A LEVANTAR AQUI.** Su `4.1` disuelve
> la parada que la TAREA 4 de la 202 levanto, y por dos sitios a la vez: **no hay
> nada que decidir**, porque **cada acta titula sus propias secciones** y **leer el
> titulo que el documento escribe es medir**; y **las adjudicaciones de las actas
> viejas SI estan numeradas**, lo unico que les falta son las comillas inversas. De
> ahi sale **la vara obligatoria de las actas anteriores a la 184**, que las TAREAS
> 1 y 4 usan y declaran. Su `4.3` deja **`OP-L-02` en 3 de 3 y aun asi sin cerrar**,
> porque mientras el instrumento siga diffeando contra `46208790` la clausula 2
> **daria `NO CUMPLIDA` con el fallo o sin el**: **aqui no se levanta y no se le
> toca el `estado`**. Y su `4.4` adjudica la correccion de la `verificacion` de
> `OP-L-01`, que es la TAREA 2.
>
> **LA CIFRA QUE EL ACTA 202 MIDIO EN SU `5.2` Y AQUI SE OBEDECE:** el inventario de
> salidas **se mide a si mismo y envejece dentro de la propia vuelta**. La 202
> publico **37** y al cierre habia **41**, y los cuatro de mas nacieron DESPUES del
> bloque que los conto. **No es caida, le faltaba media linea**, y esa media linea
> va escrita en el bloque `J` del sello de apertura: **junto al corte se declaran
> los ficheros que nacen despues de medirlo**, con sus nombres, y **el cierre remide
> la cifra en vez de heredarla** (banco `9.21`).
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni **podar la nomina**, ni **mover
> un solo campo `estado`** (la vara del trabajo pendiente es
> `scripts/loop/vuelta150_3_relectura_expediente.py`, nunca el campo, por el
> recuadro de `AUDITOR.md` 0), ni **mover una clase ni un veredicto**, ni **cerrar
> ninguna ficha por cuenta del ejecutor**: lo que estas tareas producen es **lectura
> medida**, y si de ella sale que una ficha esta cumplida, **se propone con su
> evidencia y lo adjudica el auditor**. **Y siguen fuera, nombradas para que la 204
> no las redescubra:** la **operacion de codigo de la escalada** (acta 202, `4.6`),
> **encargada y con su ejecucion SUSPENDIDA** porque `AUDITOR.md` 1.2 obliga a
> encargarla y la moratoria `6.3` prohibe fabricarla, ya que **es una guarda que se
> queda vigilando**; la **reparacion del HEAD envejecido** de
> `vuelta170_tarea5b_veredicto_op_l_02.py`; el **cierre del turno del auditor que se
> reabre despues de declarar las clases**; los **dos arneses que el censo ve y la
> nomina congelada no tiene**; **anadir `docs/PENDIENTES.md` como quinta sede de
> cifra publicada**; y **QUE HACER CON LAS FILAS `B` DEL ARCHIVO**. **Las de codigo
> van a la auditoria integral: la moratoria las prohibe hoy.**
>
> **NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor,
> y **las dos convenciones se publican**. **Y no se toca `dataset/` a mano**: el
> `numstat` de `dataset/`, `web/`, `engine/` y `docs/plan/` se mide al entrar y al
> salir y **las dos cifras se publican**.'''

src = io.open(FUENTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
L = src.split(NL)
n_antes = len(L)

# 1. EL DOCSTRING: la linea 1 es el coding, el docstring va de la 2 hasta su
#    cierre, localizado CONTANDO y no tecleado.
assert L[0].startswith("# -*- coding"), L[0][:60]
assert L[1].startswith('r' + chr(34) * 3 + 'vuelta202_esqueleto_reporte.py'), L[1][:60]
cierres = [i for i in range(2, len(L)) if L[i] == chr(34) * 3]
assert cierres, "no se encuentra el cierre del docstring"
fin_doc = cierres[0]
doc_viejo = NL.join(L[1:fin_doc + 1])
texto = L[0] + NL + DOCSTRING + NL + NL.join(L[fin_doc + 1:])
print("1) DOCSTRING: %d lineas viejas -> %d lineas nuevas"
      % (doc_viejo.count(NL) + 1, DOCSTRING.count(NL) + 1))

# 2. LA CONSTANTE.
assert texto.count("VUELTA = 202") == 1, texto.count("VUELTA = 202")
texto = texto.replace("VUELTA = 202", "VUELTA = 203")
print("2) CONSTANTE: VUELTA = 202 -> VUELTA = 203, 1 sola aparicion")

# 3. LA LISTA TAREAS: del marcador de apertura al primer ']' en columna 0.
i = texto.index("TAREAS = [")
j = texto.index(NL + "]" + NL, i) + len(NL + "]")
tareas_viejo = texto[i:j]
texto = texto[:i] + TAREAS_TXT + texto[j:]
print("3) TAREAS: %d bytes viejos -> %d bytes nuevos, %d entradas"
      % (len(tareas_viejo), len(TAREAS_TXT), 4))

# 4. EL BLOQUE DE PROSA: del primer '> **ESTE REPORTE SE ABRIO' hasta la linea
#    que cierra la prosa, justo antes del veredicto sin escribir.
ini = texto.index("> **ESTE REPORTE SE ABRIO")
fin = texto.index(NL + NL + "**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**")
prosa_vieja = texto[ini:fin]
texto = texto[:ini] + PROSA + texto[fin:]
print("4) PROSA: %d bytes viejos -> %d bytes nuevos"
      % (len(prosa_vieja), len(PROSA)))

# LA CIFRA QUE CONVIERTE "CLON DECLARADO" EN UNA MEDICION Y NO EN UNA PALABRA:
# cuantas lineas vienen SIN TOCAR de la fuente y cuantas son nuevas, contadas
# con difflib.
nuevas = texto.split(NL)
sm = difflib.SequenceMatcher(None, L, nuevas, autojunk=False)
iguales = sum(b.size for b in sm.get_matching_blocks())
print("")
print("EL CLON, MEDIDO Y NO AFIRMADO (difflib.SequenceMatcher):")
print("   CIFRA lineas de la fuente %s: %d"
      % (os.path.basename(FUENTE), n_antes))
print("   CIFRA lineas del destino %s: %d"
      % (os.path.basename(DESTINO), len(nuevas)))
print("   CIFRA lineas que vienen SIN TOCAR de la fuente: %d" % iguales)
print("   CIFRA lineas nuevas o cambiadas en el destino: %d" % (len(nuevas) - iguales))

io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
print("")
print("ESCRITO: scripts/loop/vuelta203_esqueleto_reporte.py (%d bytes)"
      % len(texto.encode("utf-8")))
