# -*- coding: utf-8 -*-
r"""verificar_cifras_del_reporte.py . LA SEGUNDA MITAD DE LA ESCALADA (TAREA
2.e de la vuelta 133, encargada por AUDITOR.md 1.2 al llegar la racha de
reporte a DOS tandas seguidas, acta de la vuelta 132). EJECUTOR.md 1 la nombra
literal: "la extension del tallador a las fases mecanicas", "TODA TABLA DEL
REPORTE TALLADA DE FICHEROS DE SALIDA".

POR QUE NACE. La racha de las vueltas 74, 75 y 76 (EJECUTOR.md, "LA TABLA SE
CUENTA DE SU FICHERO") mostro que en el tramo mecanico las cifras del reporte
se volvieron a teclear, porque `tallar_cabecera_reporte.py` solo cubre LA
CABECERA (censo, Gate 0, aristas, motor, web, tsc, marcador) y
`tallar_identidad_reporte.py` (2.a) solo cubre EL PARRAFO DE IDENTIDAD: el
CUERPO del reporte, con sus tablas de adjudicaciones y sus cifras de prosa,
sigue sin ningun instrumento que lo muerda.

CONTRATO (cerrado, para no tener que decidir nada al correrla):
  - Recorre docs/loop/REPORTE.md SALTANDO la cabecera tallada Y NADA MAS.
    CORREGIDO EN LA VUELTA 139 (2.b), y el texto viejo de este punto decia,
    VERBATIM: "SALTANDO la tabla tallada de la cabecera (delimitada por las
    lineas que `tallar_cabecera_reporte.py --comparar` reconoce: se salta
    desde la primera fila de tabla markdown hasta la ultima fila de tabla
    consecutiva del bloque de cabecera)". NO ERA LO QUE EL CODIGO HACIA: el
    codigo descartaba TODA linea que empezara por barra vertical, viviera
    donde viviera, y por eso no veia NI UNA cifra que viviera en una tabla
    (acta de la vuelta 138, caida 4.5: 26 cifras en el fichero, 10 vistas,
    16 perdidas). DESDE LA VUELTA 139 la cabecera tallada se DELIMITA con
    dos marcas literales, `<!-- CABECERA TALLADA -->` y
    `<!-- FIN CABECERA TALLADA -->`, y se quita SOLO lo que hay entre ellas;
    si las marcas NO estan, no se quita nada y se recorren TODAS las filas.
    Se sigue quitando el parrafo de identidad (las lineas de rotulo que
    empiezan por "HEAD sellado" o "commit de nacimiento").
  - Busca pares (numero, unidad) con VOCABULARIO CERRADO de unidades:
    fichero/ficheros, par/pares, grupo/grupos, grafia/grafias,
    colapso/colapsos, nodo/nodos, linea/lineas, arista/aristas (singular o
    plural, sin distinguir mayusculas).
  - Para cada par, busca en la MISMA frase o en las DOS SIGUIENTES una cita
    de docs/loop/SALIDA_V<N>_*.txt: MISMA doctrina de ventana que
    `verificar_cifras_del_plan.py` (se REUSA `dividir_frases` de ese modulo,
    no se reinventa).
  - Si hay cita, CUENTA la cifra EN ESE FICHERO (nunca confia en un total ya
    impreso por el instrumento: se recuentan las instancias, "la tabla se
    cuenta de su fichero"). LA UNIDAD MANDA COMO SE CUENTA (ramal xvii):
      * fichero/ficheros: tokens DISTINTOS que parecen ruta de fichero (con
        extension conocida), deduplicados por cadena literal.
      * par/pares: tokens DISTINTOS `<ruta>:<numero>` (fichero:linea).
      * arista/aristas: lineas que traen `IZQUIERDA -> DERECHA` (el formato
        que ya usan `vuelta83_conteo_aristas.py`, `verificar_aristas_vivas.py`
        y `verificar_huerfanas_por_fusion.py`).
      * linea/lineas: lineas no vacias del fichero.
      * grupo/grupos, grafia/grafias, colapso/colapsos, nodo/nodos: no hay
        una convencion mecanica establecida todavia en ningun instrumento de
        esta campana para estas cuatro unidades (ninguna de ellas imprime,
        hoy, un listado de una linea por entidad con un separador fijo). Se
        cuenta con la MISMA convencion generica declarada aqui (lineas no
        vacias con sangria de lista, es decir que empiezan por dos o mas
        espacios y NO son una linea de arista ni de par), documentada para
        que sea auditable, PERO cuando esa cuenta no permita distinguir con
        confianza la unidad pedida, la guarda prefiere no inventar: si el
        fichero citado no tiene NINGUNA linea de ese tipo, se trata como
        "cifra sin fichero que contar" en vez de fabricar un cero espurio.
    Si las dos cuentas posibles del mismo bloque (ficheros vs pares) dan
    numeros distintos y la cifra escrita coincide con la que NO corresponde a
    su unidad, ROJO nombrando las dos cuentas (ramal xvii hecho codigo).
  - Si no cuadra, ROJO EXIT 1 con la linea, el numero escrito, el numero
    contado y el fichero.
  - LA SALIDA DE EMERGENCIA, ESTRECHADA EN LA VUELTA 134 (acta 133, 4.4: la
    version vieja de esta regla se tragaba 7 de 8 cifras del reporte y la
    escalada nacio ciega). Una cifra (numero, unidad) SIN fichero de salida
    en su ventana (ni citado, ni citado-pero-incontable) es ROJO EXIT 1
    nombrando la linea y la cifra, SALVO que caiga en una de estas TRES
    exenciones, cerradas y todas:
      (i) las cifras del parrafo de identidad y de la tabla tallada de la
          cabecera: ya quedan fuera porque quitar_bloques_cubiertos() las
          retira antes de parsear, asi que nunca llegan a esta funcion.
      (ii) la cifra del tope de 1.k, que habla del propio REPORTE.md (frase
          que trae "wc -l" y "REPORTE.md" con unidad linea/lineas): se
          coteja con el conteo EN VIVO de lineas del propio fichero del
          reporte, no con un SALIDA_V*.txt. Si cuadra, CUENTA COMO COTEJADA.
      (iii) una cifra que el reporte marque explicitamente con el literal
          `(sin instrumento)` PEGADO justo detras del numero y su unidad:
          se LISTA APARTE, en su propia lista de "exentas por (sin
          instrumento)", y CUENTA en la linea de COBERTURA, pero no se
          verifica contra nada.
    NINGUNA OTRA EXENCION.

LO QUE ESTA GUARDA NO CUBRE, DICHO EN VEZ DE CALLADO: los headline de
`docs/plan/OP_S_11_MAPEO_PROPUESTO.md` (105 grupos, 104, 39 grafias, etc.) NO
citan un `SALIDA_V<N>_*.txt` a su lado (citan la tabla del plan, que
`verificar_cifras_del_plan.py` ya declara, por contrato propio, que NUNCA
puede mirar): esas cifras caen, por diseno, en "cifra sin fichero que contar",
no en rojo ni en verde. Esta guarda solo puede cotejar lo que un
`SALIDA_V<N>_*.txt` mecanico realmente contiene.

USO:
  python scripts/loop/verificar_cifras_del_reporte.py
  python scripts/loop/verificar_cifras_del_reporte.py --reporte RUTA

PRUEBA DE MUTACION (obligatoria, EJECUTOR.md 1 "EL CASO ROJO SE PRUEBA POR
MUTACION"): scripts/loop/vuelta133_tarea2e_mutacion_cifras.py, salida a
docs/loop/SALIDA_V133_2E_MUTACION.txt.

--- LA PUERTA DE SERVICIO SE TAPIA (TAREA 2 de la vuelta 135, acta 134,
4.1) ---

POR QUE NACE. La exencion (iii) de arriba eximia una cifra con SOLO el
literal `(sin instrumento)` pegado, escrito por EL AUDITADO, sin que la
guarda comprobara nada por si misma. El auditor lo probo con tres
mutaciones sobre el reporte real de la 134: `118 grafias` a `999 grafias`
dio VERDE EXIT 0, `54 grupos` a `77 grupos` dio VERDE EXIT 0, y solo una
cifra nueva SIN marca y sin fichero dio ROJO. Las dos primeras cifras SI
tenian fichero de instrumento commiteado cerca (`SALIDA_V134_4A_CENSO_
COLA.txt` y `SALIDA_V134_4B_EFECTO_CAP.txt`) y la exencion las dejaba
pasar de todos modos: "una exencion que escribe el auditado no es una
exencion, es un interruptor" (ramal xix).

LA CONDICION NUEVA (2.b). El literal `(sin instrumento)` exime una cifra
SOLO SI la guarda comprueba, ELLA MISMA, que en la VENTANA AMPLIA de esa
cifra (`ventana_amplia()`: la propia frase mas HASTA DOS frases ANTES y
HASTA DOS frases DESPUES, bidireccional) no hay ningun `SALIDA_V<N>_*.txt`
existente citado. Se ensancha la ventana SOLO para esta pregunta binaria
(hay o no hay UN fichero cerca): en la prosa de este reporte la cita casi
siempre PRECEDE al numero que introduce (patron "4.a (`FICHERO`, ...): ...
<numero> ...") y el wrap de linea de `dividir_frases` corta la frase justo
ahi, así que una ventana solo-adelante (la que sigue usando, SIN TOCAR, el
cotejo normal de mas abajo, MISMA doctrina que `verificar_cifras_del_
plan.py`) no la veria nunca. Si la ventana amplia SI trae un fichero
citado, el literal es ILEGAL: ROJO EXIT 1 nombrando la linea, la cifra y
el fichero, motivo "hay instrumento en la ventana: la cifra se coteja, no
se exime". Las exenciones (i) y (ii) NO cambian. NINGUNA CUARTA EXENCION.

LA LINEA `CIFRA` (2.c). Para que tapiar la puerta no deje al auditado sin
salida honesta, un instrumento puede imprimir una linea
`CIFRA <etiqueta>: <n> <unidad>` (unidad del vocabulario cerrado de
arriba). Cuando una cifra del reporte cita un fichero, la guarda busca
PRIMERO una linea `CIFRA` de esa MISMA familia de unidad en ese fichero y
coteja contra ella; solo si no la encuentra cae a la convencion generica
de recuento (`contar_por_familia`) que ya tenia. Si no puede contar de
ninguna de las dos maneras, sigue siendo ROJO nombrando el fichero.

PRUEBA DE MUTACION (obligatoria): scripts/loop/vuelta135_2e_mutacion_1.py,
_2.py y _3.py, salidas a docs/loop/SALIDA_V135_2E_MUTACION_1.txt, _2.txt y
_3.txt: (1) `118 grafias` a `999 grafias` sobre copia del reporte real de
la 134, ROJO; (2) `54 grupos` a `77 grupos`, ROJO; (3) caso negativo, una
cifra con fichero citado, linea `CIFRA` puesta y numero CORRECTO, VERDE.

--- LA ASIMETRIA DE LAS DOS VENTANAS, ADJUDICADA COMO DOCTRINA (TAREA 2.c
de la vuelta 136, acta 135, 3.1) ---

Esta guarda usa DOS ventanas distintas a proposito y NO SE UNIFICAN NUNCA:
  - VENTANA AMPLIA (`ventana_amplia()`, mas menos 2 frases, bidireccional):
    decide si la exencion (iii) de arriba es LEGAL, es decir si hay o no
    hay UN `SALIDA_V<N>_*.txt` existente cerca del literal `(sin
    instrumento)`. Aqui ensanchar solo puede ENCONTRAR MAS instrumentos,
    nunca menos, asi que ensanchar hace la exencion MAS dificil de ganar,
    nunca mas facil: es la direccion segura.
  - VENTANA FORWARD-ONLY (la del cotejo normal, mas abajo, MISMA doctrina
    que `verificar_cifras_del_plan.py`): COTEJA la cifra contra el fichero
    que la sigue, nunca contra el que la precede.
Por que no se unifican: ensanchar el COTEJO (no solo la pregunta de la
exencion) dejaria que una cifra cuadrara contra el fichero DEL VECINO, que
es exactamente el error que la ventana forward-only comete cuando eximia
sin comprobar (el ejemplar: `SALIDA_V135_2A_DIAGNOSTICO.txt`, corrido con
forward-only, empareja `118 grafias` con `SALIDA_V134_4B_EFECTO_CAP.txt`,
el fichero del vecino, cuando la pareja correcta es `SALIDA_V134_4A_
CENSO_COLA.txt`). AMPLIA para decidir si la exencion es legal,
FORWARD-ONLY para cotejar la cifra: nunca una ventana sola para las dos
preguntas.

--- LAS DOS REPARACIONES DE LA VUELTA 137 (TAREA 1.c, parada del 29 ago
2026 punto 4, acta 136) ---

Las nombro el auditor al medir POR QUE el reporte de la vuelta 136 publico
COBERTURA 0/0/0: el ejecutor cambio las palabras de la casa hasta que esta
guarda no encontro nada que morder. Su diagnostico era CIERTO (la guarda
caia ROJO sobre cifras CORRECTAS); el remedio no lo era. Los dos defectos
se reprodujeron con ficheros REALES antes de tocar nada
(vuelta137_1c_diagnostico.py, SALIDA_V137_1C_DIAGNOSTICO.txt).

PRIMERA, QUE APRENDA A CONTAR LA UNIDAD `grafia`. Un fichero de salida
puede traer VARIAS lineas `CIFRA` de la MISMA unidad y se tomaba la
PRIMERA. Ahora se recogen todas con su ETIQUETA y se elige por la
etiqueta (camino FUERTE); si hay empate o ninguna palabra en comun con la
frase, se acepta cualquiera de las candidatas y se marca POR CONJUNTO
(camino DEBIL, declarado en el codigo y en la salida, no escondido).

SEGUNDA, QUE EMPAREJE CADA CIFRA CON SU FICHERO. Habia un `sorted(set())`
y un `citas[0]`: de todas las citas de la ventana se tomaba la
ALFABETICAMENTE primera. Ahora se ordenan por PROXIMIDAD TEXTUAL a la
cifra. LA VENTANA NO CAMBIA: sigue siendo la forward-only, porque la
asimetria de arriba esta adjudicada como doctrina; lo que cambia es CUAL
de las citas de esa misma ventana se elige.

Y UN HALLAZGO QUE EL DEFECTO SEGUNDO ESCONDIA: no solo tiraba cifras
correctas, tambien DEJABA PASAR incorrectas. Medido corriendo la version
vieja sacada de git (vuelta137_1c_mutacion.py, mutacion C): "2 grafias en
grupo" citando un fichero que dice 92 salia VERDE EXIT 0, porque cuadraba
contra el recuento generico del fichero del VECINO.

PRUEBA DE MUTACION (obligatoria): scripts/loop/vuelta137_1c_mutacion.py,
salida a docs/loop/SALIDA_V137_1C_MUTACION.txt. Cuatro casos: cifra
equivocada por uno, cifra de la etiqueta VECINA del mismo fichero (prueba
que el camino fuerte no se degrada al debil), el falso verde de arriba, y
las mutaciones viejas recorridas.

--- LA GUARDA APRENDE A LEER LAS AFIRMACIONES DE CIERRE (VUELTA 140, 2.b) ---

POR QUE NACE. Es la caida 4.1 del acta 139 puesta donde ocurrio. El reporte
de la vuelta 139 publico "LA FASE 06 CIERRA SU CATALOGO" en su cabecera y
"hoy cierra" en su conclusion, y sobre esa frase pidio disparar el pase de
estado de seis operaciones. No cerraba: cinco operaciones remitidas por la
fase 04 en la vuelta 118 tenian once aristas sin escribir. Esta guarda no
podia verlo porque solo miraba CIFRAS con unidad, y "la fase 06 cierra su
catalogo" no lleva ninguna. Una frase de cierre SIN INSTRUMENTO DETRAS es
la especie exacta que la racha de reporte castiga.

QUE COMPRUEBA, DE MAS, y son DOS cosas, las dos objetivas (la guarda NO intenta
distinguir una afirmacion de una negacion: eso seria leerle la mente al que
escribe). Toda frase que hable del cierre o de la completitud de una FASE o de un
CATALOGO tiene que:
  (1) CITAR, en su ventana, un fichero de salida de `tallar_estado_de_fase.py`.
      Sin cita, ROJO.
  (2) si el fichero citado dice `sin cumplir: N` con N distinto de cero, NOMBRAR
      EN SU VENTANA LAS N. Si calla alguna, ROJO nombrando las que callo.

POR QUE ESA SEGUNDA Y NO "el fichero tiene que decir cero". La primera version de
esta guarda exigia `sin cumplir: 0` a secas, y con esa regla EL REPORTE QUE DICE
LA VERDAD CAIA EN ROJO: "la fase 06 NO cierra", citando el instrumento que dice
`sin cumplir: 3`, era tan rojo como "la fase 06 cierra" sin citar nada. Se hallo
corriendo la guarda contra el reporte de la vuelta 140. La caida 4.1 no fue decir
"cierra": fue decirlo CALLANDO las cinco remitidas que faltaban. Bajo esta regla
esa frase da ROJO nombrandolas una a una, y un reporte que dice "no cierra,
faltan estas tres" pasa, porque hizo lo que se le pide.

LO QUE ESTA REGLA SIGUE PERMITIENDO, dicho para que nadie la lea de mas: un texto
que escriba "cierra" Y ADEMAS nombre las que faltan pasaria. Es prosa que se
contradice sola y que salta a la vista de cualquier lector; lo que la guarda
impide es lo que NO salta a la vista, que es afirmar el cierre callando la lista.

EL VOCABULARIO DE DISPARO ES CERRADO, Y SE DICE AQUI PARA QUE LA PROXIMA
AMPLIACION NO SEA UNA SORPRESA. Dispara una frase que traiga a la vez un
SUJETO de `SUJETOS_DE_CIERRE` (`fase`, `catalogo`) y un VERBO de
`VERBOS_DE_CIERRE` (`cierra`, `cierre`, `catalogo completo`,
`queda completa`, `queda completo`, `esta entera`, `esta entero`,
`sin pendientes`). Ni una palabra mas: si manana hace falta cazar otra
formula, se ANADE AQUI y se dice en el reporte, nunca se deja que la guarda
la adivine.

LA GUARDA DISPARA DE MAS A PROPOSITO, Y EL REMEDIO NO ES REESCRIBIR. Con ese
vocabulario cerrado caen tambien frases condicionales ("cuando la fase 06
cierre") y frases sobre el cierre de una vuelta. Es deliberado: el coste de
un disparo de mas es UNA CITA, y el coste de un disparo de menos fue la
caida 4.1. **El remedio de un ROJO de esta clase es CITAR EL INSTRUMENTO,
jamas reescribir la prosa hasta que la guarda no encuentre nada**, que es el
ramal (xxi) del acta 136 ("una cobertura de cero no es un verde, es un plato
vacio").

LA LISTA DE COMMITS QUEDA FUERA, Y SE DICE POR QUE (vuelta 140, tercera
reparacion de esta operacion, hallada corriendo la guarda contra el reporte ya
con su lista pegada). El bloque de commits es un TALLADO DE GIT: sus lineas son
ASUNTOS DE COMMIT, no prosa del reporte, y uno de los asuntos de esta vuelta
empieza por "LA FASE 06 NO CIERRA". Dentro de una lista de commits no hay donde
poner la cita, porque la ventana es forward-only por doctrina adjudicada y detras
solo hay mas commits. Se le da el MISMO trato que a la cabecera tallada, con las
MISMAS tres reglas de delimitador (`<!-- COMMITS TALLADOS -->` y su cierre): con
las dos marcas se quita lo delimitado, SIN NINGUNA marca no se quita nada y se
recorre todo, y con UNA SOLA es ROJO.

COMO RECONOCE UN FICHERO DE `tallar_estado_de_fase.py`: POR SU CONTENIDO, no
por su nombre. Tiene que traer la cabecera `ESTADO DE LA FASE` y una linea
`CIFRA:` con `sin cumplir: <n>`. Un fichero citado que no las traiga NO
cuenta como cita valida, y se dice cual era.

--- LA GUARDA DEJA DE SER CIEGA (TAREA 2.a, VUELTA 142) ---

POR QUE NACE. Es la caida 4.5 del acta 141, y es del auditor, hallada
CORRIENDO esta guarda y no leyendola. Corrida contra el reporte de la vuelta
141 daba `VERDE EXIT 0: 0 cifra(s) cotejadas` con
`COBERTURA: 0 cotejadas / 0 exentas / 0 cifras`. La causa, medida en el
codigo: `UNIDADES` era un vocabulario cerrado (fichero, par, grupo, grafia,
colapso, nodo, linea, arista) y el reporte publica sus cifras en DIRECCIONES,
filas y comprobaciones, ninguna dentro. Y `direccion` es justamente LA UNIDAD
QUE EL ACTA 140 ADJUDICO como unidad publicada (adjudicacion 3.4): la unidad
oficial de la campana era la unica que la guarda no sabia leer. Peor: en la
vuelta 140 esa misma salida se firmo como verde con su COBERTURA en ceros
delante. Es P.14: un control que solo encuentra fallos ajenos no es un control.

LAS DOS PIEZAS, Y LAS DOS VAN.

(i) EL VOCABULARIO CRECE CON LA UNIDAD ADJUDICADA, Y NO SE TECLEA DE MEMORIA.
    Entran `direccion(es)`, `fila(s)`, `comprobacion(es)` y `operacion(es)`.
    Las tres primeras salen MEDIDAS de docs/loop/REPORTE.md con
    scripts/loop/vuelta142_2a_nomina_unidades.py (direcciones 5 veces,
    comprobaciones 2, filas 1 sobre el reporte de la vuelta 141); `operacion`
    entra por el encargo. NINGUNA HEREDA CONVENCION MECANICA: ver el comentario
    de `UNIDAD_A_FAMILIA`, familia `sin convencion`. Una cifra de estas ocho
    unidades SOLO coteja contra una linea `CIFRA <etiqueta>: <n> <unidad>` del
    fichero citado; si el fichero no la trae, es ROJO diciendolo con esas
    palabras, en vez de contar lineas que no son la unidad pedida.

    Y LA SEGUNDA MITAD, QUE ES LA QUE IMPIDE QUE VUELVA A PASAR: la guarda
    PUBLICA EN CADA CORRIDA, en su linea COBERTURA, LA NOMINA DE UNIDADES
    VISTAS DETRAS DE UN NUMERO QUE NO ESTAN EN SU VOCABULARIO
    (`unidades_vistas_fuera_del_vocabulario`). No las juzga y no falla por
    ellas: las hace VISIBLES. Una unidad nueva ya no puede colarse en silencio
    porque aparece nombrada en la salida el primer dia que se usa.
    `RUIDO` es SOLO gramatica y verbos: ningun sustantivo contable entra ahi,
    porque esconder una palabra en RUIDO seria la misma ceguera por otra puerta.

(ii) CERO CIFRAS COTEJADAS DEJA DE SER VERDE. Si la guarda recorre el reporte y
    no llega a cotejar NINGUNA cifra, no es que todo cuadre: es que no midio.
    Sale ROJO diciendo cuantas cifras vio, cuantas cotejo, cuantas eximio y con
    que unidades se quedo fuera. Es banco 9 (fallar ruidoso) y es el ramal
    (xxi) del acta 136 escrito en el codigo: "una cobertura de cero no es un
    verde, es un plato vacio".

PRUEBA DE MUTACION (obligatoria, EJECUTOR.md 1: sobre variable COMPUTADA,
nunca sobre un literal): scripts/loop/vuelta142_2a_mutaciones.py, salida a
docs/loop/SALIDA_V142_2A_MUTACIONES.txt. Cuatro casos, dos por pieza:
  (i.a)  sobre una COPIA del reporte, se cambia el NUMERO de una cifra en
         `direcciones` que SI cita su fichero: ROJO nombrando la linea.
  (i.b)  contraprueba: la misma copia sin mutar, esa cifra COTEJADA y VERDE.
  (ii.a) reporte de prueba SIN ninguna cifra cotejable: ROJO por cobertura
         cero.
  (ii.b) contraprueba: el mismo reporte de prueba con UNA cifra cotejable:
         ya no cae por cobertura cero.
Los sujetos fabricados se retiran al terminar (P.16, quien fabrica limpia).

PRUEBA DE MUTACION (obligatoria): scripts/loop/vuelta140_2b_mutaciones.py,
salida a docs/loop/SALIDA_V140_2B_MUTACIONES.txt. Cinco casos sobre sujeto
fabricado y retirado por P.16 (quien fabrica, limpia): (a) frase de cierre SIN
cita, ROJO; (b) frase de cierre con cita a un fichero que dice `sin cumplir: 3`
y SIN nombrarlas, ROJO nombrando las tres; (b bis) la misma frase NOMBRANDO las
tres, VERDE (es el caso que la primera version tiraba); (c) sin la frase, VERDE;
(c bis) frase con cita a un fichero que dice `sin cumplir: 0`, VERDE y cotejada.
"""
import argparse
import glob
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
RUTA_REPORTE = os.path.join(LOOP, "REPORTE.md")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verificar_cifras_del_plan import dividir_frases  # noqa: E402

UNIDADES = ["fichero", "ficheros", "par", "pares", "grupo", "grupos",
            "grafia", "grafias", "colapso", "colapsos", "nodo", "nodos",
            "linea", "lineas", "arista", "aristas",
            # TAREA 2.a.i, vuelta 142. LAS OCHO QUE ENTRAN, y de donde salen:
            # el encargo las nombra una a una, y la medicion de
            # vuelta142_2a_nomina_unidades.py sobre docs/loop/REPORTE.md de la
            # vuelta 141 las halla usadas (direcciones 5 veces, comprobaciones
            # 2, filas 1). `direccion` es ademas LA UNIDAD ADJUDICADA por el
            # acta 140, adjudicacion 3.4. Ver el bloque
            # "LA GUARDA DEJA DE SER CIEGA" del docstring.
            "direccion", "direcciones", "fila", "filas",
            "comprobacion", "comprobaciones", "operacion", "operaciones"]
PATRON_NUMERO_UNIDAD = re.compile(
    r"\b(\d+(?:[.,]\d+)?)\s+(%s)\b" % "|".join(UNIDADES), re.IGNORECASE)

# --- EL PATRON ANCHO Y LA NOMINA DE RUIDO (TAREA 2.a.i, vuelta 142) ---
# Viven AQUI y no en el instrumento de medicion porque son la misma pregunta y
# no puede haber dos versiones de la misma cosa: `PATRON_NUMERO_UNIDAD` solo ve
# las palabras que el vocabulario ya trae, asi que por construccion NO PUEDE
# descubrir la que falta. Este patron ve CUALQUIER palabra detras de un numero,
# y `RUIDO` separa los conectores y verbos que siguen a un numero sin ser nunca
# una unidad. scripts/loop/vuelta142_2a_nomina_unidades.py los IMPORTA de aqui.
#
# RUIDO ES SOLO GRAMATICA, NUNCA UN SUSTANTIVO CONTABLE, y se dice por que: lo
# que entra en RUIDO deja de aparecer en la nomina, y una palabra que nombra
# algo contable escondida ahi seria la misma ceguera de la 4.5 por otra puerta.
# Por eso "cumplidas", "presentes", "verdes" o "comprobaciones" NO estan aqui
# aunque hoy no esten en UNIDADES: se publican cada corrida en la nomina de
# unidades vistas y fuera del vocabulario, para que se vean y se decidan.
PATRON_NUMERO_PALABRA = re.compile(r"\b(\d+(?:[.,]\d+)?)\s+([^\W\d_]{3,})\b", re.UNICODE)
RUIDO = set(u"""de del la las los una uno con por para que sin sobre mas menos
como cuando donde entre desde hasta tras segun sus era eran son fue fueron
esta estan este estos estas ese esa esos esas cada todo toda todos todas
otro otra otros otras solo solamente casi tambien pero aunque porque
dice dicen dijo queda quedan quedo caen cae cayo lee leen leyo pide piden
ordena ordenan dejo dejan deja defiende defienden sigue siguen siguio
tiene tienen tuvo hace hacen hizo dan daba salen sale salio trae traen trajo
ago sep jul jun may abr mar feb ene oct nov dic""".split())
PATRON_CITA_SALIDA = re.compile(r"SALIDA_V\d+_[A-Za-z0-9_]+\.txt")
PATRON_RUTA_FICHERO = re.compile(
    r"[A-Za-z0-9_./\\-]+\.(?:py|md|ts|tsx|js|jsx|json|jsonl|txt)\b")
PATRON_PAR_FICHERO_LINEA = re.compile(
    r"[A-Za-z0-9_./\\-]+\.(?:py|md|ts|tsx|js|jsx|json|jsonl|txt):\d+\b")
PATRON_ARISTA = re.compile(r"^\s*\S+\s*->\s*\S+", re.MULTILINE)
PATRON_CIFRA_ETIQUETA = re.compile(
    r"^CIFRA\s+[^:\n]+:\s*(\d+(?:[.,]\d+)?)\s+(%s)\b" % "|".join(UNIDADES),
    re.IGNORECASE | re.MULTILINE)

# --- VOCABULARIO CERRADO DE LAS AFIRMACIONES DE CIERRE (vuelta 140, 2.b) ---
# Ver el docstring del modulo, seccion "LA GUARDA APRENDE A LEER LAS
# AFIRMACIONES DE CIERRE": esta lista es CERRADA por contrato. Ampliarla es un
# acto declarado, no una adivinanza del instrumento.
SUJETOS_DE_CIERRE = ("fase", "catalogo")
VERBOS_DE_CIERRE = ("cierra", "cierre", "catalogo completo", "queda completa",
                    "queda completo", "esta entera", "esta entero", "sin pendientes")
PATRON_SIN_CUMPLIR = re.compile(r"sin cumplir:\s*(\d+)", re.IGNORECASE)
PATRON_LISTA_SIN_CUMPLIR = re.compile(r"^SIN CUMPLIR \(\d+\):\s*(.+)$", re.MULTILINE)
MARCA_ESTADO_DE_FASE = "ESTADO DE LA FASE"


def leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


# LOS FICHEROS CITADOS QUE NO SON UTF-8 (vuelta 145, TAREA 4.c). Hallado al
# correr esta guarda sobre el REPORTE.md de la vuelta 145: reventaba con
# UnicodeDecodeError y una traza de pila, sin decir de que fichero hablaba mas
# que en el stack. La causa no es el reporte: es que
# `docs/loop/SALIDA_V<N>_CICLO_ETIQUETAS_*.txt` se captura con la codificacion
# de la consola de Windows (cp1252), y lleva asi desde al menos la vuelta 144
# (medido: el fichero de la 144 tampoco decodifica). Nadie lo habia visto
# porque hasta hoy ningun reporte lo habia CITADO.
#
# LA DECISION, DECLARADA: se cuenta igual, porque ninguna de las cuatro
# unidades que esta guarda cuenta (ficheros, pares, aristas, lineas) depende de
# un acento; PERO NO SE CALLA. Se decodifica con `errors="replace"` y se ANOTA
# el fichero en `NO_UTF8`, que la linea de COBERTURA publica siempre. Degradar
# en silencio seria justo lo que el banco 9 prohibe; reventar con una traza
# tampoco sirve, porque no distingue "el reporte esta mal" de "la guarda no
# pudo leer".
NO_UTF8 = []


def leer_citado(ruta):
    """El contenido de un fichero de salida CITADO por el reporte. Intenta
    UTF-8 estricto; si el fichero no lo es, lo decodifica con reemplazo Y LO
    ANOTA para que la cobertura lo diga con su nombre."""
    try:
        return leer(ruta)
    except UnicodeDecodeError:
        nombre = os.path.basename(ruta)
        if nombre not in NO_UTF8:
            NO_UTF8.append(nombre)
        with io.open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()


MARCA_CABECERA_ABRE = "<!-- CABECERA TALLADA -->"
MARCA_CABECERA_CIERRA = "<!-- FIN CABECERA TALLADA -->"
# LA LISTA DE COMMITS, TALLADA DE GIT (vuelta 140, tercera reparacion de la 2.b).
# Mismo trato y mismas reglas de delimitador que la cabecera tallada: es un
# bloque con su propio tallador, y sus lineas son ASUNTOS DE COMMIT, no prosa del
# reporte. Ver el docstring del modulo.
MARCA_COMMITS_ABRE = "<!-- COMMITS TALLADOS -->"
MARCA_COMMITS_CIERRA = "<!-- FIN COMMITS TALLADOS -->"
# LA SALIDA DE ESTA MISMA GUARDA, PEGADA EN EL REPORTE (TAREA 2.d, vuelta 144;
# acta 143, adjudicacion 3.10 y caida 4.1 del ejecutor).
#
# POR QUE NACE, Y ES UNA CIFRA MEDIDA: el reporte de la vuelta 143 publico
# "unidades vistas FUERA del vocabulario: 18 palabra(s)". Re-corrida la misma
# guarda sobre el REPORTE.md ya commiteado, la cifra dio 30. Las doce nuevas
# eran TODAS del propio bloque que el reporte habia pegado (cotejadas, exentas,
# commit, bloque, cabecera, cifra, cifras, asunto, asuntos, palabra, viven,
# contra). PEGAR LA SALIDA DENTRO DEL FICHERO QUE LA SALIDA MIDE CAMBIA LA
# MEDIDA: la cola de vocabulario no es un punto fijo, y el ejecutor no puede
# publicar una cifra que deja de ser cierta en el momento de commitearla.
#
# EL ARREGLO NO INVENTA NADA: es el MISMO mecanismo que esta funcion ya usa con
# la cabecera tallada y con los commits tallados, con sus MISMAS TRES REGLAS de
# delimitador (las dos marcas quitan lo delimitado; ninguna no quita nada y se
# recorre todo, que es fallar ruidoso; una sola es ROJO con ValueError). Lo
# unico que cambia es el bloque que delimita.
#
# MUTACION: scripts/loop/vuelta144_2d_mutacion_cobertura.py.
MARCA_COBERTURA_ABRE = "<!-- COBERTURA DE LA GUARDA -->"
MARCA_COBERTURA_CIERRA = "<!-- FIN COBERTURA DE LA GUARDA -->"


# LAS SEIS MARCAS DE BLOQUE, en una sola nomina para que la regla del ancla
# unica (vuelta 145, TAREA 2.a) no pueda quedarse corta de una: cada pareja que
# se anada aqui queda cubierta sin tocar `_exigir_ancla_unica`.
MARCAS_DE_BLOQUE = (
    ("CABECERA TALLADA, apertura", MARCA_CABECERA_ABRE),
    ("CABECERA TALLADA, cierre", MARCA_CABECERA_CIERRA),
    ("COMMITS TALLADOS, apertura", MARCA_COMMITS_ABRE),
    ("COMMITS TALLADOS, cierre", MARCA_COMMITS_CIERRA),
    ("COBERTURA DE LA GUARDA, apertura", MARCA_COBERTURA_ABRE),
    ("COBERTURA DE LA GUARDA, cierre", MARCA_COBERTURA_CIERRA),
)


def _posiciones(texto, marca):
    """TODAS las posiciones de `marca`, cada una como (offset, linea). Es lo
    contrario de `texto.find`, que devuelve solo la primera y por eso pudo
    anclar en el bloque equivocado durante toda la vuelta 144."""
    fuera = []
    i = texto.find(marca)
    while i != -1:
        fuera.append((i, texto.count("\n", 0, i) + 1))
        i = texto.find(marca, i + 1)
    return fuera


def _exigir_ancla_unica(texto):
    """LA CUARTA REGLA DE DELIMITADOR (vuelta 145, TAREA 2.a; acta 144, 4.3).

    Ninguna de las SEIS marcas puede aparecer mas de una vez. Si alguna se
    repite, ROJO POR AMBIGUA con ValueError, nombrando LA MARCA y TODAS sus
    posiciones (linea y offset), nunca tomando la primera. Se nombran TODAS las
    marcas repetidas de una corrida, no solo la primera que se encuentre: una
    guarda que solo canta el primer defecto obliga a correrla en bucle."""
    ambiguas = []
    for rotulo, marca in MARCAS_DE_BLOQUE:
        pos = _posiciones(texto, marca)
        if len(pos) > 1:
            ambiguas.append("%s (%r) aparece %d veces, en %s"
                            % (rotulo, marca, len(pos),
                               ", ".join("linea %d (offset %d)" % (l, o) for o, l in pos)))
    if ambiguas:
        raise ValueError(
            "ROJO POR AMBIGUA: %d marca(s) de bloque repetida(s) en el reporte, y con la "
            "marca repetida el recorte iria de la PRIMERA apertura al PRIMER cierre "
            "dejando el resto SIN RECORTAR. No se toma la primera. %s. LA REGLA: la pareja "
            "de marcas aparece EXACTAMENTE UNA VEZ; para citar el mecanismo en prosa se usa "
            "OTRO literal, no la marca de verdad" % (len(ambiguas), "; ".join(ambiguas)))


def quitar_bloques_cubiertos(texto):
    """Quita LA CABECERA TALLADA DELIMITADA y el parrafo de identidad (tallado
    por tallar_identidad_reporte.py, 2.a). Esos dos bloques tienen su propio
    tallador y no se recorren aqui.

    --- LA GUARDA DEJA DE SER CIEGA A LAS TABLAS (VUELTA 139, OPERACION 2.b) ---

    CORRECCION DECLARADA, y el texto viejo de esta funcion se cita entero abajo
    porque una correccion que tapa lo que corrige no se puede auditar.

    EL DEFECTO, MEDIDO POR EL AUDITOR Y NO OPINADO (acta de la vuelta 138,
    caida 4.5): el docstring prometia quitar "la tabla de cabecera", en
    singular, y el codigo hacia esto:

        es_fila_tabla = l.strip().startswith("|")
        ...
        if es_fila_tabla:
            en_tabla_cabecera = True
            continue

    o sea que DESCARTABA TODA LINEA QUE EMPEZARA POR BARRA VERTICAL, viviera
    donde viviera. Medido sobre el reporte de la vuelta 138: 26 cifras de
    numero mas unidad en el fichero entero, 10 que la guarda llegaba a ver, 16
    que se perdian por vivir en una fila de tabla, entre ellas las CINCO cifras
    en `grupos` de la tabla de la fase 06, la de la caida 4.2 incluida. Y la
    linea que se publicaba, `COBERTURA: 10 cotejadas / 0 exentas / 10 cifras`,
    SE LEE COMO COBERTURA LLENA. Es la peor combinacion posible con la letra
    del 27 ago 2026 ("TODA TABLA O CIFRA DEL REPORTE CITA EL FICHERO DE SALIDA
    DEL QUE SALE"): la guarda era ciega exactamente donde la doctrina es mas
    dura.

    EL ARREGLO, fijado por el auditor en el encargo de la vuelta 139: la
    cabecera tallada se DELIMITA en el reporte con dos marcas literales,

        <!-- CABECERA TALLADA -->  ...  <!-- FIN CABECERA TALLADA -->

    y esta funcion quita SOLO lo que esta entre ellas (las marcas incluidas),
    mas el parrafo de identidad que ya quitaba. TODAS LAS DEMAS FILAS DE TABLA
    SE RECORREN.

    SI LAS MARCAS NO ESTAN, NO SE QUITA NADA Y SE RECORRE TODO, incluidas las
    filas de la cabecera: fallar ruidoso, nunca degradar en silencio (banco 9).
    Un reporte sin marcas dara mas trabajo, y probablemente ROJO, que es
    justamente el sintoma que la degradacion silenciosa no dejaba.

    SI SOLO ESTA UNA DE LAS DOS MARCAS es ROJO tambien, y por la misma razon:
    se levanta ValueError con el nombre de la que falta, en vez de adivinar
    donde acaba el bloque.

    --- LA ANCLA UNICA, Y ES DE LAS TRES (VUELTA 145, TAREA 2.a; acta 144,
    adjudicacion 4.3 del auditor) ---

    CORRECCION DECLARADA. EL TEXTO VIEJO DE LA REGLA NO SE BORRA (EJECUTOR.md
    8): las TRES reglas de delimitador de arriba (las dos marcas recortan,
    ninguna no recorta nada, una sola es ROJO) SIGUEN VIGENTES TAL CUAL. Lo
    que se anade es una CUARTA, y va ANTES que las otras tres.

    EL DEFECTO, MEDIDO Y NO OPINADO. Esta funcion resolvia cada uno de sus
    TRES pares con `texto.find(MARCA)`, y `find` DEVUELVE LA PRIMERA
    OCURRENCIA: con la marca repetida, el recorte iba de la PRIMERA apertura
    al PRIMER cierre y EL SEGUNDO BLOQUE SE PARSEABA ENTERO, en silencio y
    con VERDE EXIT 0. Medido en la vuelta 145 con
    scripts/loop/vuelta145_1b_censo_de_marcas.py sobre el REPORTE.md de la
    vuelta 144 ya commiteado (`b7f07648:docs/loop/REPORTE.md`, sujeto
    congelado por ref de git y no por arbol vivo), salida en
    docs/loop/SALIDA_V145_1B_CENSO_DE_MARCAS.txt: la marca de COBERTURA
    aparece DOS VECES (lineas 274 y 278, y otra vez 632 y 638) y las otras
    cuatro UNA sola; la funcion recorta las lineas 274 a 278 y deja fuera las
    632 a 638. Pegada la linea real de COBERTURA dentro de ESE segundo
    bloque, que es justo donde el propio reporte de la 144 anuncia "(pegada
    abajo tras la segunda corrida)", la guarda pasa de VERDE EXIT 0 a ROJO
    EXIT 1 y las unidades fuera del vocabulario suben de 29 a 34. Es decir:
    la reparacion de la vuelta 144 (TAREA 2.d) protegia EL BLOQUE QUE EL
    ORDEN DEL FICHERO ELIGE, no el que el reporte designa.

    LA CUARTA REGLA. SI CUALQUIERA DE LAS SEIS MARCAS (apertura y cierre de
    CABECERA TALLADA, de COMMITS TALLADOS y de COBERTURA DE LA GUARDA)
    APARECE MAS DE UNA VEZ, ES ROJO POR AMBIGUA: ValueError nombrando LA
    MARCA y TODAS SUS POSICIONES (linea y offset). NO SE TOMA LA PRIMERA.
    Es la misma regla (iii) que la TAREA 2.a de la vuelta 144 escribio para
    la formula canonica de la excepcion del 9.22, el ancla unica, que la 2.d
    de esa misma vuelta no heredo. Vale para las TRES parejas y no solo para
    la nueva, porque el defecto es de `find`, no del bloque.

    POR QUE ROJO Y NO "RECORTAR LOS DOS": porque un reporte con la marca
    repetida es AMBIGUO sobre cual bloque es el bloque, y elegir por el
    ejecutor seria adivinar, que es exactamente lo que esta funcion dejo de
    hacer en la vuelta 139. La salida honesta la da la regla nueva de la
    TAREA 4.c: LA PAREJA DE MARCAS APARECE EXACTAMENTE UNA VEZ EN EL
    REPORTE, y quien necesite citar el mecanismo en prosa lo cita con OTRO
    literal.

    MUTACIONES: scripts/loop/vuelta145_2a_mutacion_ancla_unica.py.
    """
    # LA CUARTA REGLA, EL ANCLA UNICA (vuelta 145, TAREA 2.a; acta 144, 4.3).
    # VA LA PRIMERA DE TODAS, antes de cualquier recorte: si una marca esta
    # repetida, no hay nada que anclar y `find` mentiria tomando la primera.
    # Las SEIS a la vez, porque el defecto es de `find` y no de un bloque.
    _exigir_ancla_unica(texto)

    # Los COMMITS TALLADOS, con las mismas tres reglas de delimitador que la
    # cabecera (vuelta 140): las dos marcas quitan lo delimitado, ninguna no
    # quita nada, una sola es ROJO.
    # LA SALIDA DE ESTA MISMA GUARDA, pegada en el reporte (vuelta 144, TAREA
    # 2.d): mismas tres reglas de delimitador que la cabecera y que los
    # commits. Va la PRIMERA porque es el bloque que la propia guarda escribe,
    # y porque el orden no cambia el resultado: los tres son disjuntos.
    g_abre = texto.find(MARCA_COBERTURA_ABRE)
    g_cierra = texto.find(MARCA_COBERTURA_CIERRA)
    if (g_abre == -1) != (g_cierra == -1):
        falta = MARCA_COBERTURA_CIERRA if g_cierra == -1 else MARCA_COBERTURA_ABRE
        raise ValueError(
            "el reporte trae UNA SOLA de las dos marcas del bloque de cobertura pegado: "
            "falta %r" % falta)
    if g_abre != -1 and g_cierra < g_abre:
        raise ValueError("el reporte trae %r ANTES de %r"
                         % (MARCA_COBERTURA_CIERRA, MARCA_COBERTURA_ABRE))
    if g_abre != -1:
        texto = texto[:g_abre] + texto[g_cierra + len(MARCA_COBERTURA_CIERRA):]

    c_abre = texto.find(MARCA_COMMITS_ABRE)
    c_cierra = texto.find(MARCA_COMMITS_CIERRA)
    if (c_abre == -1) != (c_cierra == -1):
        falta = MARCA_COMMITS_CIERRA if c_cierra == -1 else MARCA_COMMITS_ABRE
        raise ValueError(
            "el reporte trae UNA SOLA de las dos marcas de los commits tallados: falta %r"
            % falta)
    if c_abre != -1 and c_cierra < c_abre:
        raise ValueError("el reporte trae %r ANTES de %r"
                         % (MARCA_COMMITS_CIERRA, MARCA_COMMITS_ABRE))
    if c_abre != -1:
        texto = texto[:c_abre] + texto[c_cierra + len(MARCA_COMMITS_CIERRA):]

    abre = texto.find(MARCA_CABECERA_ABRE)
    cierra = texto.find(MARCA_CABECERA_CIERRA)
    if (abre == -1) != (cierra == -1):
        falta = MARCA_CABECERA_CIERRA if cierra == -1 else MARCA_CABECERA_ABRE
        raise ValueError(
            "el reporte trae UNA sola de las dos marcas de la cabecera tallada: falta %r. "
            "O van las dos o no va ninguna; adivinar donde acaba el bloque es justo lo que "
            "esta guarda dejo de hacer en la vuelta 139" % falta)
    if abre != -1 and cierra < abre:
        raise ValueError("el reporte trae %r ANTES de %r"
                         % (MARCA_CABECERA_CIERRA, MARCA_CABECERA_ABRE))

    if abre == -1:
        # NI UNA MARCA: no se quita ningun bloque de tabla. Se recorre todo.
        cuerpo = texto
    else:
        cuerpo = texto[:abre] + texto[cierra + len(MARCA_CABECERA_CIERRA):]

    fuera = []
    for l in cuerpo.split("\n"):
        es_rotulo_identidad = (l.startswith("HEAD sellado") or
                               l.startswith("commit de nacimiento") or
                               "HEAD sellado de apertura" in l or
                               "HEAD sellado de cierre" in l or
                               "commit de nacimiento de las salidas de apertura" in l)
        if es_rotulo_identidad:
            continue
        fuera.append(l)
    return "\n".join(fuera)


def frases_con_bandera_de_tabla(texto):
    """Las MISMAS frases que `dividir_frases`, cada una con la bandera de si la
    LINEA de la que sale es una fila de tabla (vuelta 139, 2.b).

    NO SE REIMPLEMENTA EL PARTIDO: `dividir_frases` parte primero por linea, asi
    que una frase nunca cruza dos lineas, y llamarla linea a linea da EXACTAMENTE
    la misma lista en el mismo orden. Eso se comprueba en `verificar()` con una
    guarda que cae si algun dia dejara de ser cierto, en vez de confiarlo a este
    comentario.

    Para que sirve: la linea COBERTURA publica ademas CUANTAS de las cotejadas
    viven en una fila de tabla, que son precisamente las que la guarda no veia
    hasta esta vuelta.
    """
    salida = []
    for linea in texto.split("\n"):
        es_tabla = linea.strip().startswith("|")
        for f in dividir_frases(linea):
            salida.append((f, es_tabla))
    return salida


def contar_ficheros(contenido):
    return len(set(PATRON_RUTA_FICHERO.findall(contenido)))


def contar_pares(contenido):
    return len(set(PATRON_PAR_FICHERO_LINEA.findall(contenido)))


def contar_aristas(contenido):
    return len(PATRON_ARISTA.findall(contenido))


def contar_lineas(contenido):
    return len([l for l in contenido.split("\n") if l.strip()])


# REPARACION 1.c DE LA VUELTA 137, PRIMERA: QUE APRENDA A CONTAR LA UNIDAD
# `grafia` (parada del 29 ago 2026, punto 4; acta 136).
#
# EL DEFECTO, MEDIDO (SALIDA_V137_1C_DIAGNOSTICO.txt, corrido antes de esta
# reparacion): un fichero de salida puede traer VARIAS lineas `CIFRA` de la
# MISMA unidad, y esto devolvia la PRIMERA y solo la primera.
# docs/loop/SALIDA_V135_4B_PELDANOS.txt trae dos de unidad `grafias` ("grafias
# en grupo: 92" y "grafias sin agrupar: 37"), asi que la cifra CORRECTA "37
# grafias sin agrupar" se cotejaba contra 92 y caia ROJO. La prueba de que el
# defecto ya deformaba el trabajo esta en la cabecera de ese mismo fichero, que
# explica que el peldano 6 va PRIMERO "porque el cotejo toma la PRIMERA linea
# CIFRA de la unidad pedida": un instrumento doblado alrededor del defecto.
#
# LA REPARACION: se recogen TODAS las lineas `CIFRA` de esa unidad canonica, con
# su ETIQUETA, y se elige por la ETIQUETA, que es justamente el dato que el
# instrumento imprime para distinguirlas. Dos caminos, y el segundo se declara
# porque es mas debil:
#   CAMINO FUERTE, POR ETIQUETA. Se puntua cada etiqueta por cuantas de sus
#   palabras de contenido aparecen en la frase del reporte. Si UNA sola etiqueta
#   saca la puntuacion mas alta y esa puntuacion no es cero, ESA es la linea
#   contra la que se coteja, y se coteja ESTRICTO: si no cuadra, ROJO.
#   CAMINO DEBIL, POR CONJUNTO (DISCUTIBLE, declarado). Si hay empate o ninguna
#   palabra en comun, la guarda no puede saber a cual de las etiquetas se
#   referia la prosa. Entonces acepta que la cifra escrita sea CUALQUIERA de las
#   candidatas, nombrando cual caso, y lo dice en la salida con la marca POR
#   CONJUNTO. Es mas debil que el camino fuerte (una cifra podria cuadrar contra
#   la etiqueta equivocada del mismo fichero) y por eso se marca en vez de
#   callarse; sigue siendo mas estricto que el estado anterior, donde una cifra
#   correcta caia ROJA y el ejecutor aprendia a evitar el vocabulario.
PALABRAS_VACIAS = set("""de del la las el los un una y o en con por para que a al
mas sin sobre su sus lo se es son como entre tras hasta desde no ni""".split())


def _palabras(texto):
    return set(w for w in re.findall(r"[a-z0-9]+", texto.lower())
               if len(w) >= 4 and w not in PALABRAS_VACIAS)


def cifras_etiquetadas(contenido, unidad):
    """Devuelve la lista de (etiqueta, valor) de TODAS las lineas
    `CIFRA <etiqueta>: <n> <unidad>` de la MISMA unidad CANONICA
    (singular/plural de la MISMA palabra: "grafia" no coteja contra una linea
    CIFRA de "grupo" solo por compartir familia generica). Lista vacia si no hay
    ninguna (el llamador cae a `contar_por_familia`)."""
    canonica = UNIDAD_CANONICA[unidad]
    out = []
    for m in PATRON_CIFRA_ETIQUETA.finditer(contenido):
        numero_txt = m.group(1).replace(".", "").replace(",", "")
        u = m.group(2).lower()
        if UNIDAD_CANONICA.get(u) == canonica and numero_txt.isdigit():
            etiqueta = m.group(0).split(":")[0][len("CIFRA"):].strip()
            out.append((etiqueta, int(numero_txt)))
    return out


def elegir_cifra_etiquetada(candidatas, frase, numero):
    """Devuelve (valor, etiqueta, modo) o None si no hay candidatas. `modo` es
    'ETIQUETA' (camino fuerte) o 'CONJUNTO' (camino debil, declarado)."""
    if not candidatas:
        return None
    if len(candidatas) == 1:
        return candidatas[0][1], candidatas[0][0], "ETIQUETA"
    pal_frase = _palabras(frase)
    puntuadas = [(len(_palabras(et) & pal_frase), et, val) for et, val in candidatas]
    mejor = max(p for p, _e, _v in puntuadas)
    empatadas = [(et, val) for p, et, val in puntuadas if p == mejor]
    if mejor > 0 and len(empatadas) == 1:
        return empatadas[0][1], empatadas[0][0], "ETIQUETA"
    for et, val in candidatas:
        if val == numero:
            return val, et, "CONJUNTO"
    return candidatas[0][1], candidatas[0][0], "CONJUNTO"


def ventana_amplia(frases, i):
    """2.b: ventana BIDIRECCIONAL (+/-2), SOLO para decidir la LEGALIDAD de
    la exencion (iii). La cita casi siempre PRECEDE al numero en la prosa
    de este reporte; la ventana forward-only del cotejo normal (sin tocar,
    mas abajo) no la veria. Ver docstring del modulo."""
    return frases[max(0, i - 2):i + 3]


def contar_generico_bullets(contenido):
    """Convencion generica para grupo/grafia/colapso/nodo (docstring del
    modulo): lineas con sangria de lista (2+ espacios) que no son ya una
    arista ni un par fichero:linea. Devuelve None si no hay ninguna (para que
    el llamador prefiera 'sin fichero que contar' antes que fabricar un
    cero)."""
    n = 0
    for l in contenido.split("\n"):
        if not re.match(r"^\s{2,}\S", l):
            continue
        if PATRON_ARISTA.match(l) or PATRON_PAR_FICHERO_LINEA.search(l):
            continue
        n += 1
    return n if n > 0 else None


UNIDAD_A_FAMILIA = {
    "fichero": "fichero", "ficheros": "fichero",
    "par": "par", "pares": "par",
    "arista": "arista", "aristas": "arista",
    "linea": "linea", "lineas": "linea",
    "grupo": "generico", "grupos": "generico",
    "grafia": "generico", "grafias": "generico",
    "colapso": "generico", "colapsos": "generico",
    "nodo": "generico", "nodos": "generico",
    # TAREA 2.a.i (vuelta 142). LAS OCHO NUEVAS NO HEREDAN NINGUNA CONVENCION
    # MECANICA, Y ESO SE DECLARA EN VEZ DE INVENTARSE UNA. Un `18 direcciones`
    # NO se puede contar con `contar_aristas` (que cuenta TODA linea con `->`,
    # y las salidas de esta campana imprimen la misma direccion en la tabla y
    # otra vez en la lista de abajo: cotejar asi tiraria en ROJO cifras
    # CORRECTAS, que es exactamente el defecto que la reparacion 1.c de la
    # vuelta 137 quito), ni con `contar_generico_bullets` (que cuenta lineas
    # con sangria, sean lo que sean). LA CONSECUENCIA, ESCRITA: una cifra de
    # estas ocho unidades SOLO coteja contra una linea `CIFRA <etiqueta>: <n>
    # <unidad>` del fichero citado. Si el fichero no la publica, es ROJO
    # diciendolo con esas palabras. Eso es EJECUTOR.md 1 ("LA TABLA SE CUENTA
    # DE SU FICHERO... Si no existe fichero que contar, LA TABLA NO SE
    # PUBLICA") puesto en el instrumento.
    "direccion": "sin convencion", "direcciones": "sin convencion",
    "fila": "sin convencion", "filas": "sin convencion",
    "comprobacion": "sin convencion", "comprobaciones": "sin convencion",
    "operacion": "sin convencion", "operaciones": "sin convencion",
}

# Canonica SINGULAR de cada unidad (2.c): la familia de arriba agrupa
# grupo/grafia/colapso/nodo en un solo "generico" para el CONTEO GENERICO
# (ninguno tiene convencion mecanica propia), pero la linea `CIFRA` SI
# distingue entre ellas: "118 grafias" y "54 grupos" son unidades
# DISTINTAS y no pueden cotejar contra la misma linea `CIFRA` solo porque
# comparten familia generica.
UNIDAD_CANONICA = {
    "fichero": "fichero", "ficheros": "fichero",
    "par": "par", "pares": "par",
    "grupo": "grupo", "grupos": "grupo",
    "grafia": "grafia", "grafias": "grafia",
    "colapso": "colapso", "colapsos": "colapso",
    "nodo": "nodo", "nodos": "nodo",
    "linea": "linea", "lineas": "linea",
    "arista": "arista", "aristas": "arista",
    # Las ocho de la TAREA 2.a.i (vuelta 142): cada una es su propia canonica,
    # para que "18 direcciones" NUNCA coteje contra una linea CIFRA de "filas"
    # del mismo fichero. Es la misma doctrina que separo grafia de grupo en la
    # vuelta 137.
    "direccion": "direccion", "direcciones": "direccion",
    "fila": "fila", "filas": "fila",
    "comprobacion": "comprobacion", "comprobaciones": "comprobacion",
    "operacion": "operacion", "operaciones": "operacion",
}


def contar_por_familia(familia, contenido):
    if familia == "fichero":
        return contar_ficheros(contenido)
    if familia == "par":
        return contar_pares(contenido)
    if familia == "arista":
        return contar_aristas(contenido)
    if familia == "linea":
        return contar_lineas(contenido)
    if familia == "sin convencion":
        # No hay convencion mecanica para esta unidad: se devuelve None a
        # proposito para que el llamador lo diga con su nombre, en vez de
        # fabricar un numero contando lineas que no son la unidad pedida.
        return None
    return contar_generico_bullets(contenido)


def unidades_vistas_fuera_del_vocabulario(texto):
    """TAREA 2.a.i (vuelta 142). LA NOMINA QUE LA GUARDA PUBLICA EN CADA
    CORRIDA, para que la proxima unidad nueva no se cuele como se colo
    `direcciones` (acta 141, caida 4.5 del auditor).

    Recorre el reporte con `PATRON_NUMERO_PALABRA`, que ve CUALQUIER palabra
    detras de un numero, y devuelve {palabra: veces} de las que NO estan en
    `UNIDADES` y NO estan en la nomina declarada de `RUIDO`. NO decide nada: no
    es un fallo, es una LISTA VISIBLE. Quien decide que una palabra entre al
    vocabulario es el encargo, y la entrada queda escrita en `UNIDADES` con su
    motivo."""
    vocabulario = set(u.lower() for u in UNIDADES)
    vistas = {}
    for m in PATRON_NUMERO_PALABRA.finditer(texto):
        numero_txt = m.group(1).replace(".", "").replace(",", "")
        if not numero_txt.isdigit():
            continue
        palabra = m.group(2).lower()
        if palabra in vocabulario or palabra in RUIDO:
            continue
        vistas[palabra] = vistas.get(palabra, 0) + 1
    return vistas


def ficheros_salida_existentes():
    return set(os.path.basename(p) for p in glob.glob(os.path.join(LOOP, "SALIDA_V*.txt")))


def contar_lineas_del_propio_reporte(ruta_reporte):
    """Replica `wc -l`: cuenta caracteres de nueva linea, no lineas con
    contenido (wc -l no distingue lineas en blanco)."""
    with io.open(ruta_reporte, "rb") as f:
        return f.read().count(b"\n")


def clasificar_exencion(frase, m, unidad):
    """Devuelve 'ii', 'iii' o None. (i) no llega aqui: ya la quito
    quitar_bloques_cubiertos() antes de parsear."""
    resto = frase[m.end():].lstrip()
    if resto.startswith("(sin instrumento)"):
        return "iii"
    if unidad in ("linea", "lineas") and "wc -l" in frase and "REPORTE.md" in frase:
        return "ii"
    return None


def _sin_tildes(texto):
    """Las frases del reporte llevan tildes y el vocabulario de disparo esta
    escrito sin ellas (esta casa escribe sus instrumentos sin tildes). Se
    igualan los dos lados antes de comparar, que es la misma reparacion que la
    correccion 1 de la vuelta 139 (una busqueda de "vision general" dio 0
    contra un texto que la lleva con tilde)."""
    pares = {"\u00e1": "a", "\u00e9": "e", "\u00ed": "i", "\u00f3": "o", "\u00fa": "u",
             "\u00c1": "A", "\u00c9": "E", "\u00cd": "I", "\u00d3": "O", "\u00da": "U",
             "\u00fc": "u", "\u00dc": "U"}
    return "".join(pares.get(c, c) for c in texto)


def es_afirmacion_de_cierre(frase):
    """VOCABULARIO CERRADO (ver docstring del modulo). Dispara si la frase trae
    a la vez un SUJETO y un VERBO de las dos nominas literales."""
    plana = _sin_tildes(frase).lower()
    sujeto = next((s for s in SUJETOS_DE_CIERRE if s in plana), None)
    verbo = next((v for v in VERBOS_DE_CIERRE if v in plana), None)
    if sujeto and verbo:
        return sujeto, verbo
    return None


def leer_estado_de_fase(contenido):
    """Reconoce una salida de tallar_estado_de_fase.py POR SU CONTENIDO, no por
    su nombre. Devuelve (sin_cumplir, nombres) o None si no lo es."""
    if MARCA_ESTADO_DE_FASE not in contenido:
        return None
    m = PATRON_SIN_CUMPLIR.search(contenido)
    if m is None:
        return None
    nombres = []
    ml = PATRON_LISTA_SIN_CUMPLIR.search(contenido)
    if ml:
        crudo = ml.group(1).strip()
        if crudo.lower() != "ninguna":
            nombres = [x.strip() for x in crudo.split(",") if x.strip()]
    return int(m.group(1)), nombres


def comprobar_afirmaciones_de_cierre(frases, existentes):
    """TAREA 2.b de la vuelta 140. Devuelve (fallos, cotejadas). Una frase de
    cierre sin cita de tallar_estado_de_fase.py en su ventana es ROJO; con cita
    a un fichero que no diga "sin cumplir: 0", ROJO NOMBRANDO las que faltan.

    LA VENTANA ES LA MISMA QUE LA DEL COTEJO DE CIFRAS, frases[i:i+3], y por el
    mismo motivo: la asimetria de ventanas de esta guarda esta adjudicada como
    doctrina en el docstring del modulo y no se ensancha por comodidad."""
    fallos = []
    cotejadas = []
    for i, frase in enumerate(frases):
        disparo = es_afirmacion_de_cierre(frase)
        if disparo is None:
            continue
        sujeto, verbo = disparo
        ventana_txt = " ".join(frases[i:i + 3])
        citas = [c for c in PATRON_CITA_SALIDA.findall(ventana_txt) if c in existentes]
        estados = []
        no_validas = []
        for c in dict.fromkeys(citas):
            leido = leer_estado_de_fase(leer(os.path.join(LOOP, c)))
            if leido is None:
                no_validas.append(c)
            else:
                estados.append((c, leido))
        if not estados:
            msg = ("linea %d: AFIRMACION DE CIERRE (sujeto '%s', verbo '%s') SIN cita de "
                   "tallar_estado_de_fase.py en su ventana: %r"
                   % (i, sujeto, verbo, frase.strip()))
            if no_validas:
                msg += (" [citas de la ventana que NO son salidas de estado de fase: %s]"
                        % ", ".join(no_validas))
            fallos.append(msg)
            continue
        for fichero, (sin_cumplir, nombres) in estados:
            if sin_cumplir == 0:
                cotejadas.append((i, sujeto, verbo, fichero, "sin cumplir: 0"))
                continue
            # LA FASE NO ESTA CUMPLIDA: la ventana TIENE QUE NOMBRAR las que
            # faltan. Ver el docstring del modulo: la caida 4.1 no fue decir
            # "cierra", fue decirlo CALLANDO LA LISTA.
            sin_nombrar = [x for x in nombres if x not in ventana_txt]
            if sin_nombrar:
                fallos.append(
                    "linea %d: AFIRMACION DE CIERRE (sujeto '%s', verbo '%s') citando `%s`, "
                    "que dice sin cumplir: %d, y su ventana NO NOMBRA %d de ellas: %s. "
                    "Frase: %r"
                    % (i, sujeto, verbo, fichero, sin_cumplir, len(sin_nombrar),
                       ", ".join(sin_nombrar) or "el fichero no las nombra", frase.strip()))
            else:
                cotejadas.append((i, sujeto, verbo, fichero,
                                  "sin cumplir: %d, y la ventana las nombra todas"
                                  % sin_cumplir))
    return fallos, cotejadas


def verificar(ruta_reporte, cierres_out=None, nomina_out=None):
    """LA ARIDAD NO SE TOCA (vuelta 140, 2.b): sigue devolviendo CUATRO valores
    porque scripts/loop/vuelta135_2a_diagnostico.py y
    scripts/loop/vuelta139_2b_mutaciones.py, los dos sellados en otras vueltas,
    desempaquetan cuatro. Las afirmaciones de cierre cotejadas se recogen en la
    lista `cierres_out` si el llamador la pasa, y la nomina de unidades vistas
    fuera del vocabulario en el dict `nomina_out` (TAREA 2.a.i, vuelta 142), por
    la misma razon: anadir un quinto valor de retorno romperia los dos scripts
    sellados."""
    texto_completo = leer(ruta_reporte)
    texto = quitar_bloques_cubiertos(texto_completo)
    if nomina_out is not None:
        nomina_out.update(unidades_vistas_fuera_del_vocabulario(texto))
    # LA BANDERA DE TABLA (vuelta 139, 2.b), con su guarda de que no se ha
    # inventado un partido distinto del de la casa: si algun dia
    # frases_con_bandera_de_tabla dejara de dar la MISMA lista que
    # dividir_frases, esto cae en vez de medir otra cosa en silencio.
    con_bandera = frases_con_bandera_de_tabla(texto)
    frases = dividir_frases(texto)
    if [f for f, _ in con_bandera] != frases:
        raise ValueError(
            "frases_con_bandera_de_tabla dio %d frase(s) y dividir_frases %d, o en otro "
            "orden: el partido de frases de esta guarda ya no es el de la casa"
            % (len(con_bandera), len(frases)))
    es_de_tabla = [b for _, b in con_bandera]
    existentes = ficheros_salida_existentes()

    fallos = []
    cotejados = []
    exentas_sin_instrumento = []
    total_cifras = 0

    # TAREA 2.b de la vuelta 140: las AFIRMACIONES DE CIERRE, antes que las
    # cifras, porque una fase que no cierra invalida el parrafo entero y no
    # una celda. Ver el docstring del modulo.
    fallos_cierre, cierres_cotejados = comprobar_afirmaciones_de_cierre(frases, existentes)
    fallos.extend(fallos_cierre)
    if cierres_out is not None:
        cierres_out.extend(cierres_cotejados)

    for i, frase in enumerate(frases):
        for m in PATRON_NUMERO_UNIDAD.finditer(frase):
            numero_txt = m.group(1)
            unidad = m.group(2).lower()
            if "," in numero_txt or "." in numero_txt:
                numero_txt_norm = numero_txt.replace(".", "").replace(",", "")
            else:
                numero_txt_norm = numero_txt
            if not numero_txt_norm.isdigit():
                continue
            numero = int(numero_txt_norm)
            total_cifras += 1

            exencion = clasificar_exencion(frase, m, unidad)
            if exencion == "iii":
                ventana_ilegal = ventana_amplia(frases, i)
                ventana_ilegal_txt = " ".join(ventana_ilegal)
                citas_cercanas = sorted(set(PATRON_CITA_SALIDA.findall(ventana_ilegal_txt)))
                citas_cercanas = [c for c in citas_cercanas if c in existentes]
                if citas_cercanas:
                    fallos.append(
                        "linea %d: \"%d %s\" marca (sin instrumento) pero su ventana amplia "
                        "SI cita `%s`: la cifra se coteja, no se exime (hay instrumento en la "
                        "ventana)" % (i, numero, unidad, citas_cercanas[0]))
                    continue
                exentas_sin_instrumento.append((numero, unidad, frase.strip()))
                continue
            if exencion == "ii":
                contado_vivo = contar_lineas_del_propio_reporte(ruta_reporte)
                if contado_vivo != numero:
                    fallos.append(
                        "linea %d: tope 1.k \"%d %s\" <-> `wc -l %s`: contado %d" %
                        (i, numero, unidad, os.path.basename(ruta_reporte), contado_vivo))
                else:
                    cotejados.append((numero, unidad, "wc -l %s" % os.path.basename(ruta_reporte), contado_vivo, es_de_tabla[i]))
                continue

            ventana = frases[i:i + 3]
            ventana_txt = " ".join(ventana)
            # REPARACION 1.c DE LA VUELTA 137, SEGUNDA: QUE EMPAREJE CADA CIFRA
            # CON SU FICHERO (parada del 29 ago 2026, punto 4; acta 136).
            # EL DEFECTO, MEDIDO (SALIDA_V137_1C_DIAGNOSTICO.txt): aqui habia un
            # `sorted(set(...))` y mas abajo un `citas[0]`, o sea que de todas
            # las citas de la ventana se tomaba LA ALFABETICAMENTE PRIMERA, no
            # la que corresponde a esa cifra. Reproducido con ficheros reales:
            # "92 grafias en grupo (`SALIDA_V135_4B_PELDANOS.txt`)" seguido de
            # una frase que cita `SALIDA_V133_2E_MUTACION.txt` se cotejaba
            # contra el del VECINO (V133 < V135 alfabeticamente) y caia ROJO
            # contando 2.
            # LA REPARACION: las citas se ordenan por PROXIMIDAD TEXTUAL a la
            # cifra dentro de la ventana, no por alfabeto, y se toma la mas
            # cercana. LA VENTANA NO SE TOCA: sigue siendo la FORWARD-ONLY de
            # siempre (frases[i:i+3]), porque la asimetria de las dos ventanas
            # esta adjudicada como doctrina en el docstring de este modulo y
            # ensanchar el COTEJO es justamente lo que dejaria cuadrar una cifra
            # contra el fichero del vecino. Lo que se corrige es CUAL de las
            # citas de esa misma ventana se elige.
            pos_cifra = m.start()
            vistos = {}
            for mc in PATRON_CITA_SALIDA.finditer(ventana_txt):
                nombre = mc.group(0)
                if nombre not in existentes:
                    continue
                distancia = abs(mc.start() - pos_cifra)
                if nombre not in vistos or distancia < vistos[nombre]:
                    vistos[nombre] = distancia
            citas = [n for n, _d in sorted(vistos.items(), key=lambda kv: (kv[1], kv[0]))]
            if not citas:
                fallos.append(
                    "linea %d: \"%d %s\" SIN fichero de salida en su ventana (ni exenta): %r" %
                    (i, numero, unidad, frase.strip()))
                continue
            fichero_cita = citas[0]
            ruta_cita = os.path.join(LOOP, fichero_cita)
            contenido_cita = leer_citado(ruta_cita)
            familia = UNIDAD_A_FAMILIA[unidad]
            etiqueta_usada = None
            modo_cifra = None
            elegida = elegir_cifra_etiquetada(
                cifras_etiquetadas(contenido_cita, unidad), frase, numero)
            if elegida is not None:
                contado, etiqueta_usada, modo_cifra = elegida
            else:
                contado = contar_por_familia(familia, contenido_cita)
            if contado is None:
                if familia == "sin convencion":
                    fallos.append(
                        "linea %d: \"%d %s\" cita `%s`, pero la unidad `%s` NO TIENE "
                        "CONVENCION MECANICA DE CONTEO: el fichero citado tiene que "
                        "publicar una linea `CIFRA <etiqueta>: <n> %s` y no la trae "
                        "(EJECUTOR.md 1: si no existe fichero que contar, la cifra no "
                        "se publica)" % (i, numero, unidad, fichero_cita, unidad, unidad))
                else:
                    fallos.append(
                        "linea %d: \"%d %s\" cita `%s` pero no se pudo CONTAR en el (ni exenta)" %
                        (i, numero, unidad, fichero_cita))
                continue
            if contado != numero:
                # ramal (xvii): si la otra familia cotejable (fichero vs par)
                # SI cuadra, se nombra para que se vea que la unidad escrita
                # es la que esta mal, no la cifra.
                otra = None
                if familia == "fichero":
                    otra = ("par", contar_pares(contenido_cita))
                elif familia == "par":
                    otra = ("fichero", contar_ficheros(contenido_cita))
                msg = ("linea %d: \"%d %s\" <-> `%s`: contado %d" %
                       (i, numero, unidad, fichero_cita, contado))
                if etiqueta_usada is not None:
                    msg += " (linea CIFRA '%s', elegida POR %s)" % (etiqueta_usada, modo_cifra)
                    todas = cifras_etiquetadas(contenido_cita, unidad)
                    if len(todas) > 1:
                        msg += " [candidatas de esa unidad en el fichero: %s]" % ", ".join(
                            "'%s'=%d" % (e, v) for e, v in todas)
                if otra and otra[1] == numero:
                    msg += (" (NO CUADRA como %s, pero SI cuadra como %s: %d; "
                            "la unidad escrita no corresponde a la cifra)" %
                            (unidad, otra[0], otra[1]))
                fallos.append(msg)
            else:
                detalle = fichero_cita
                if etiqueta_usada is not None:
                    detalle += " (CIFRA '%s', POR %s)" % (etiqueta_usada, modo_cifra)
                cotejados.append((numero, unidad, detalle, contado, es_de_tabla[i]))

    return fallos, cotejados, exentas_sin_instrumento, total_cifras


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reporte", default=RUTA_REPORTE)
    a = ap.parse_args()

    cierres = []
    nomina = {}
    fallos, cotejados, exentas, total_cifras = verificar(
        a.reporte, cierres_out=cierres, nomina_out=nomina)

    # --- (ii) CERO CIFRAS COTEJADAS DEJA DE SER VERDE (TAREA 2.a.ii, vuelta
    # 142; acta 141, caida 4.5 del auditor). Si la guarda recorre el reporte
    # entero y no llega a cotejar NINGUNA cifra, eso NO es cobertura llena: es
    # que no midio, y publicarlo como VERDE EXIT 0 es una firma, no un control
    # (banco 9, fallar ruidoso; P.14). El fallo se ANADE a la lista, no la
    # sustituye, para que un reporte que ademas tenga cifras malas siga
    # nombrandolas todas.
    if not cotejados:
        detalle = ", ".join("%s (%d)" % (p, n) for p, n in
                            sorted(nomina.items(), key=lambda kv: (-kv[1], kv[0]))) or "ninguna"
        fallos.append(
            "COBERTURA CERO: la guarda vio %d cifra(s) con unidad del vocabulario, "
            "cotejo 0 y eximio %d. UN VERDE SOBRE CERO NO ES UN VERDE. Unidades vistas "
            "detras de un numero y FUERA del vocabulario (%d palabra(s)): %s"
            % (total_cifras, len(exentas), len(nomina), detalle))
    # EL REPARTO POR ETIQUETA CONTRA POR CONJUNTO es condicion viva del acta 137
    # (3.1): una cobertura tiene que decir DE QUE esta llena. Y desde la vuelta
    # 139 (2.b) dice ademas CUANTAS de las cotejadas viven en una FILA DE TABLA,
    # que son exactamente las que esta guarda no veia hasta que se reparo.
    por_etiqueta = len([c for c in cotejados if "POR ETIQUETA" in c[2]])
    por_conjunto = len([c for c in cotejados if "POR CONJUNTO" in c[2]])
    en_tabla = len([c for c in cotejados if c[4]])
    cobertura = ("COBERTURA: %d cotejadas / %d exentas / %d cifras"
                 " | reparto: %d POR ETIQUETA, %d POR CONJUNTO, %d sin linea CIFRA"
                 " | de las cotejadas, %d viven en una FILA DE TABLA" % (
                     len(cotejados), len(exentas), total_cifras,
                     por_etiqueta, por_conjunto,
                     len(cotejados) - por_etiqueta - por_conjunto, en_tabla))
    cobertura += (" | afirmaciones de CIERRE cotejadas contra tallar_estado_de_fase.py: %d"
                  % len(cierres))
    # LA NOMINA VA EN LA MISMA LINEA QUE LA COBERTURA, siempre, verde o rojo
    # (TAREA 2.a.i, vuelta 142): una cobertura que no dice QUE SE QUEDO FUERA es
    # la que dejo colarse a `direcciones` durante dos vueltas.
    cobertura += (" | ficheros citados que NO son UTF-8: %d [%s]"
                  % (len(NO_UTF8), ", ".join(sorted(NO_UTF8)) or "ninguno"))
    cobertura += (" | unidades vistas FUERA del vocabulario: %d palabra(s) [%s]"
                  % (len(nomina),
                     ", ".join("%s x%d" % (p, n) for p, n in
                               sorted(nomina.items(), key=lambda kv: (-kv[1], kv[0])))
                     or "ninguna"))

    if fallos:
        print("ROJO, %d cifra(s) no cuadran:" % len(fallos))
        for f in fallos:
            print("  %s" % f)
        if exentas:
            print("cifra(s) exentas por (sin instrumento) (%d):" % len(exentas))
            for numero, unidad, frase in exentas:
                print("  %d %s: %r" % (numero, unidad, frase))
        print(cobertura)
        return 1

    print("VERDE EXIT 0: %d cifra(s) cotejadas contra su fichero de salida o wc -l, todas cuadran:" %
          len(cotejados))
    for numero, unidad, fichero, contado, en_fila in cotejados:
        print("  %d %s == %d contados en `%s`%s"
              % (numero, unidad, contado, fichero, "  [FILA DE TABLA]" if en_fila else ""))
    if exentas:
        print("cifra(s) exentas por (sin instrumento) (%d):" % len(exentas))
        for numero, unidad, frase in exentas:
            print("  %d %s: %r" % (numero, unidad, frase))
    if cierres:
        print("afirmacion(es) de CIERRE cotejadas (%d), cada una con LO QUE SU FICHERO "
              "DICE (computado, no tecleado):" % len(cierres))
        for i, sujeto, verbo, fichero, estado in cierres:
            print("  linea %d (sujeto '%s', verbo '%s') <-> `%s`: %s"
                  % (i, sujeto, verbo, fichero, estado))
    print(cobertura)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
