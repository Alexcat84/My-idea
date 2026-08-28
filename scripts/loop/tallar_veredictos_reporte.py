# -*- coding: utf-8 -*-
r"""tallar_veredictos_reporte.py . EL TALLADOR DE VEREDICTOS (TAREA 1.1 de la
vuelta 102, encargo del auditor, acta de la vuelta 101, "LA RACHA DE REPORTE
PASA DE UNO A DOS", escalada obligada por EJECUTOR.md 1.2).

POR QUE NACE, CON EL EJEMPLAR DELANTE. El reporte de la vuelta 101 publico,
en su parrafo de cabecera, "VERDE contra `scripts/loop/verificar_apertura_
sellada.py --vuelta 101`, `docs/loop/SALIDA_V101_TAREA1_2_MUTACION_
APERTURA.txt`", y remato en la TAREA 1 con "(1.3) usada sobre esta apertura:
VERDE". El fichero citado como evidencia, commiteado por el propio ejecutor,
imprime en su PRIMER bloque "ROJO, apertura de la vuelta 101 NO sellada
antes de la 1.a operacion ... EXIT=1". Nadie abrio el fichero citado antes
de teclear el veredicto. Este instrumento automatiza esa apertura.

QUE MIDE, EXACTO Y NADA MAS.

  (1) LOCALIZA cada palabra VERDE, ROJO, PASA o FALLA en `docs/loop/REPORTE.md`
      (linea a linea, respetando mayusculas: son las cuatro palabras que el
      reporte usa para veredictos, no cualquier "verde" de otro sentido).

  (2) PARA CADA UNA, busca el fichero `docs/loop/SALIDA_...` que la
      afirmacion CITA, DENTRO DEL MISMO PARRAFO (un parrafo es el texto
      entre dos lineas en blanco). La convencion de escritura de esta
      campana, repetida en cada acta y cada reporte, es "AFIRMACION
      (fichero)" o "AFIRMACION, `fichero`": el fichero de evidencia va
      DESPUES de la palabra de veredicto, no antes (un fichero citado ANTES,
      como el sello de un hash, suele ser contexto, no la evidencia de ESTE
      veredicto). Por eso se prefiere la PRIMERA cita que aparezca DESPUES
      de la palabra; solo si no hay ninguna despues en el mismo parrafo, se
      usa la mas cercana ANTES. Si no hay ninguna cita en el parrafo, la
      afirmacion NO CITA FICHERO y se ignora (no es lo que este tallador
      comprueba: EJECUTOR.md solo exige tallar lo que un fichero ya mide).

  (3) ABRE ese fichero y calcula SU VEREDICTO REAL: la ULTIMA linea de todo
      el fichero que empiece (tras quitar espacios) por VERDE, ROJO, PASA o
      FALLA (asi una salida con varios bloques, cada uno con su propio
      veredicto de caso, se lee por su LINEA DE CIERRE/RESUMEN, que es
      convencion de esta familia de instrumentos: "VERDE GENERAL", "TODOS
      LOS TESTS PASARON", etc. van al final). Si ninguna linea empieza asi,
      cae al ULTIMO `EXIT=N` o `EXITCODE N` del fichero (N==0 es VERDE, N!=0
      es ROJO). Si tampoco hay eso, EL VEREDICTO NO ES LEGIBLE.

  (4) COMPARA: VERDE y PASA son la misma clase (OK); ROJO y FALLA son la
      misma clase (MAL). Si la clase de la afirmacion del reporte NO
      coincide con la clase real del fichero, o si el fichero no existe, o
      si su veredicto no es legible, ES UN HALLAZGO: se imprime nombrando el
      fichero Y LA LINEA del reporte donde vive la afirmacion.

MECANICA DE ROJO: si HAY AL MENOS UN HALLAZGO, el tallador termina con
"ROJO, N hallazgo(s)" y exit 1. Si no hay ninguno (incluido el caso de que
el reporte no cite ningun fichero junto a un veredicto), termina con "VERDE"
y exit 0. Nunca corrige nada: solo mide y nombra.

USO:
  python scripts/loop/tallar_veredictos_reporte.py
  python scripts/loop/tallar_veredictos_reporte.py --reporte docs/loop/REPORTE.md

PRUEBA DE MUTACION, caso positivo OBLIGATORIO (con su salida commiteada,
docs/loop/SALIDA_V102_TAREA1_1_MUTACION_VEREDICTOS.txt):
  (a) ROJO sobre `docs/loop/REPORTE.md` de la vuelta 101 tal como esta
      commiteado en `8dfc4b48` (`git show 8dfc4b48:docs/loop/REPORTE.md`),
      que es el caso real medido por el auditor: tiene que nombrar
      `docs/loop/SALIDA_V101_TAREA1_2_MUTACION_APERTURA.txt` como el
      fichero cuyo veredicto real (ROJO) contradice la afirmacion VERDE del
      reporte.
  (b) VERDE sobre `docs/loop/REPORTE.md` de la vuelta 102, una vez escrito
      bien (cada veredicto que cite un fichero calza con lo que ese fichero
      dice de verdad).

--- TAREA 1 de la vuelta 105 (acta de la vuelta 104, "EL AGUJERO DE LA
ORACION"): LA CITA DE LA ORACION SIGUIENTE ---

POR QUE NACE, CON EL EJEMPLAR DELANTE. El auditor de la vuelta 104 escribio
tres mutaciones sobre la MISMA frase falsa (VERDE citando
`SALIDA_V104_APERTURA_NO_SELLADA.txt`, cuyo veredicto real es ROJO). Las
formas A y B (cita en la MISMA oracion que la palabra) ya daban ROJO. La
forma C, "la manera mas natural que hay de escribir un reporte" (se afirma
en una oracion y se cita en la siguiente), daba VERDE: "... salio VERDE y no
hubo nada que declarar. La evidencia esta en `SALIDA_V104_APERTURA_NO_
SELLADA.txt`, pegada entera." La palabra VERDE vive en la primera oracion;
la cita, en la segunda. El cerco de la 104 solo miraba la MISMA oracion (o,
si esa cita no era legible, el PARRAFO entero): una cita que vive en la
oracion siguiente, con la oracion de la palabra SIN NINGUNA cita, quedaba
fuera de las dos reglas y la afirmacion se ignoraba en silencio (ni hallazgo
ni cobertura): una guarda que no ve la mentira no esta contando.

LA REGLA (1.4 del encargo, la via mas corta que no ataba a otro patron): si
la oracion de la palabra NO trae ninguna cita, se prueba la ORACION
SIGUIENTE del mismo parrafo, PERO SOLO SI esa oracion siguiente no trae
NINGUNA palabra de veredicto propia. Esa condicion es la que evita que vuelva
el emparejamiento por parrafo que produjo los seis falsos de la 103: una
oracion siguiente que SI trae su propia palabra de veredicto puede ser la
narracion de OTRA afirmacion (el patron exacto de las mutaciones A y B, y de
la enumeracion "(a) VERDE ..., (b) ROJO ..." de la vuelta 102), asi que su
cita no se le presta a la palabra de antes. Si la cita de la oracion
siguiente resulta NO LEGIBLE, sigue rigiendo (d): se ensancha al parrafo
entero antes de darla por buena.

PRUEBA DE MUTACION (1.1, 1.2, 1.3 del encargo, con sus salidas commiteadas
en docs/loop/SALIDA_V105_TAREA1_*.txt): las tres mutaciones de la vuelta 104
(`docs/loop/_auditor_v104_mut_A.md`, `_B.md`, `_C.md`) DESPUES del arreglo:
A y B (misma oracion) SIGUEN dando ROJO; C (oracion siguiente, sin veredicto
propio) EMPIEZA a dar ROJO. El reporte de la vuelta 102
(`git show f253842b:docs/loop/REPORTE.md`), el caso VERDE que no puede
ensuciarse, SIGUE dando VERDE EXIT 0: ninguna de sus oraciones sin cita tiene
una oracion siguiente sin veredicto propio con una cita que contradiga.

--- TAREA 2 de la vuelta 104 (acta de la vuelta 103, "EL CERCO PASO DE CIEGO
A GRITON") ---

POR QUE NACE. El cerco ensanchado de la 103 (ver bloque de abajo) empareja
por PARRAFO, y el auditor lo corrio sobre el REPORTE.md de la vuelta 102
(`--commit f253842b`): ROJO, 6 hallazgos, LOS SEIS FALSOS. Los seis viven en
el mismo parrafo (la TAREA 1 de aquel reporte, 3 citas y 17 palabras de
veredicto) y nacen de narracion de mutacion: "la afirmacion VERDE del
reporte" describe lo que OTRO reporte afirmo, no un veredicto en vivo sobre
el fichero citado despues en el mismo parrafo.

EL EMPAREJAMIENTO AHORA ES POR ORACION, NO POR PARRAFO, MAS TRES FILTROS. Se
midieron EN ORDEN, contra el mismo caso real (REPORTE.md de la vuelta 102,
`--commit f253842b`), y cada uno se anadio SOLO porque el anterior no bastaba
(la traza queda escrita para que no haya que redescubrirla):

  (a) LA CITA TIENE QUE VIVIR EN LA MISMA ORACION que la palabra de
      veredicto (una oracion es el texto entre dos finales de oracion:
      `.`, `!` o `?` seguidos de espacio o fin de texto; un punto DENTRO de
      una cita entre comillas invertidas, por ejemplo el `.txt` de un
      nombre de fichero, se enmascara antes de buscar finales, para que no
      corte una oracion por la mitad). Si no hay ninguna cita en la
      oracion, la palabra NO CITA FICHERO: cuenta en la cobertura, no
      levanta hallazgo. MEDIDO: soluciona la enumeracion "VERDE/ROJO/PASA/
      FALLA que cite fichero" (ninguna cita SALIDA_ en esa oracion), pero
      SOLO (a) deja el reporte 102 en ROJO igual: la oracion "Mutacion:
      ROJO sobre el REPORTE.md de la 101 ..., nombrando
      `SALIDA_V101_..._txt` como el fichero cuyo veredicto real (ROJO)
      contradice la afirmacion VERDE del reporte." trae la cita Y los tres
      veredictos EN LA MISMA ORACION.

  (b) LA PALABRA NO PUEDE IR PRECEDIDA POR "la afirmacion" O "afirmacion"
      (sin distinguir mayusculas, en la palabra inmediatamente anterior,
      quitando puntuacion). Es la marca literal que el propio acta de la
      103 senala como el sintoma: "la palabra VERDE de 'contradice LA
      AFIRMACION VERDE del reporte' es NARRACION DE UNA MUTACION". Con
      (a)+(b) la oracion de arriba ya no levanta hallazgo (sus dos ROJO
      calzan de verdad con el fichero citado; el VERDE, adjetivo de
      "afirmacion", queda fuera). MEDIDO: (a)+(b) bajan el reporte 102 de 6
      a 2 hallazgos, no a cero: quedan la oracion "(a) VERDE ..., (b) ROJO
      ..., (c) ROJO ... con un fichero de apertura real movido al segundo
      commit (`SALIDA_..._txt`)." (dos hallazgos, linea 36) y la del apertura
      sellada (linea 4, un fichero citado en la misma oracion que no trae
      veredicto legible, ver (d)).

  (c) LA PALABRA NO PUEDE IR JUSTO DESPUES DE UNA ETIQUETA DE LISTA DE UN
      SOLO CARACTER ENTRE PARENTESIS, "(a)", "(b)", "(c)"... Narra UN caso
      de una enumeracion de varios (los "tres casos" de una mutacion); el
      veredicto de conjunto del fichero citado al final de la enumeracion es
      su ULTIMA linea VERDE/ROJO ("VERDE GENERAL: los tres casos ... dan el
      veredicto esperado"), que casi nunca coincide con lo que UN caso
      aislado narra. MEDIDO: con (a)+(b)+(c) el reporte 102 baja a 1
      hallazgo.

  (d) SI LA CITA ELEGIDA EN LA ORACION RESULTA NO LEGIBLE (fichero
      inexistente o sin linea VERDE/ROJO/PASA/FALLA ni EXIT=N), se ensancha
      la busqueda al PARRAFO entero antes de darla por buena: una cita de
      oracion no legible es senal de que esa cita es evidencia de OTRA cosa
      (aqui, un hash de apertura, `docs/loop/SALIDA_V102_HEAD_APERTURA.txt`
      solo trae el hash), y la evidencia real del VERDE vive al lado, en el
      mismo parrafo (`docs/loop/SALIDA_V102_CABECERA_TALLADA.txt`), que es
      la convencion de cabecera de esta campana. MEDIDO: con (a)+(b)+(c)+(d)
      el reporte 102 da VERDE, EXIT 0.

LA COBERTURA CAE, Y SE PUBLICA CON SU CIFRA EN VEZ DE ESCONDERLA (2.4 del
encargo, docs/loop/SALIDA_V104_TAREA2_COBERTURA.txt): sobre el REPORTE.md de
la vuelta 102 pasa de 14 de 17 a 3 de 17; sobre el de la vuelta 103 (HEAD) de
2 de 4 a 1 de 4. Es la exigencia de la vuelta 103: una cobertura menor y
honesta vale mas que catorce emparejamientos de los que seis mienten. La
caida del 2 a 1 en el reporte 103 tiene causa medida y declarada: el ROJO de
"Las dos variantes de la mutacion ... dan ROJO tras el arreglo." pierde su
cita porque el punto de cierre del titulo en negrita anterior ("acta
102).**") no cuenta como fin de oracion (el asterisco pegado al punto no es
espacio), asi que la cita que de verdad evidencia ese ROJO queda en la
oracion anterior. Es perdida real, no oculta: se prefiere no contar esa
afirmacion antes que arriesgar el falso positivo que el cerco griton probo.

PRUEBA DE MUTACION (2.2 del encargo, con su salida commiteada,
docs/loop/SALIDA_V104_TAREA2_MUTACION_DOSVARIANTES.txt): la MISMA mutacion de
dos variantes de la vuelta 103 (misma frase falsa, mismo fichero, nombre
pelado y con `docs/loop/` delante) SIGUE dando ROJO en las dos: el filtro (b)
no apaga el positivo real, porque en esa frase la palabra de veredicto no va
precedida de "afirmacion".

--- TAREA 1.1, 1.3 y 1.4 de la vuelta 103 (acta de la vuelta 102, "AHORA LA
CAIDA, Y NO ES DE DICTADO: ES DE GUARDA") ---

POR QUE NACE. La v102 de este tallador exigia el prefijo `docs/loop/` DENTRO
de las comillas (`RE_CITA` original: `` `([^`]*docs/loop/SALIDA_[^`]+\.(?:txt
|md))` ``). El reporte de la 102 escribe 4 de sus 6 citas con el NOMBRE
PELADO (sin `docs/loop/`), que es la convencion real de esta campana desde
siempre, y el tallador las ignoraba en silencio: de 17 palabras de veredicto,
solo vio la 1 que llevaba el prefijo. El auditor lo probo con mutacion (ver
`SALIDA_V103_TAREA1_2_MUTACION_VEREDICTOS_DOSVARIANTES.txt`): la MISMA frase
falsa sobre el MISMO fichero daba VERDE con el nombre pelado y ROJO con
`docs/loop/` delante, cuando las dos formas nombran el mismo fichero real.

(1.1) `RE_CITA` ahora reconoce las DOS formas: `` `SALIDA_..._.txt` `` (pelado)
y `` `docs/loop/SALIDA_..._.txt` `` (con prefijo). Un nombre pelado se
RESUELVE contra `docs/loop/<nombre>` antes de leerlo; si el fichero resuelto
no existe, es hallazgo igual que cualquier otro fichero inexistente citado
(la regla que este mismo docstring ya declaraba: "un veredicto sobre un
fichero que no existe").

(1.3) LA COBERTURA SE PUBLICA. La cabecera de la salida imprime, ademas de
"N afirmacion(es) citan fichero", cuantas palabras de veredicto
(VERDE/ROJO/PASA/FALLA) hay EN TOTAL en el reporte, citen fichero o no. Sin
umbral ni rojo por baja cobertura: solo que la cifra se vea, para que un "1
de 17" no dependa de que alguien lo cuente a mano.

(1.4) EL EMPAREJAMIENTO SE DECLARA. Cuando el parrafo trae MAS de una cita,
cada linea de salida (calce o hallazgo) dice CUANTAS citas hay en el parrafo
y CUAL regla escogio la que se uso (`primera cita DESPUES de la palabra` o,
si no hay ninguna despues, `cita ANTES mas cercana, unica del parrafo antes
de la palabra`). Con una sola cita en el parrafo no hace falta declarar
regla: no hay ambiguedad que resolver.

PRUEBA DE MUTACION DE DOS VARIANTES (1.2, vuelta 103, con su salida
commiteada, docs/loop/SALIDA_V103_TAREA1_2_MUTACION_VEREDICTOS_DOSVARIANTES.txt):
la MISMA frase falsa sobre el MISMO fichero (VERDE citando
`SALIDA_V101_TAREA1_2_MUTACION_APERTURA.txt`, cuyo veredicto real es ROJO),
una vez con el nombre pelado y otra con `docs/loop/` delante: DESPUES del
arreglo, LAS DOS tienen que dar ROJO.
"""
import argparse
import bisect
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CLASE = {"VERDE": "OK", "PASA": "OK", "ROJO": "MAL", "FALLA": "MAL"}
RE_VEREDICTO_PALABRA = re.compile(r"\b(VERDE|ROJO|PASA|FALLA)\b")
# (1.1) reconoce la cita CON prefijo docs/loop/ y PELADA (sin prefijo): las
# dos formas que el reporte usa de verdad (4 de las 6 citas de la vuelta 102
# iban peladas y el patron viejo, que exigia docs/loop/, no las veia).
RE_CITA = re.compile(r"`(docs/loop/SALIDA_[^`]+\.(?:txt|md)|SALIDA_[^`/]+\.(?:txt|md))`")
RE_LINEA_VEREDICTO = re.compile(r"^(VERDE|ROJO|PASA|FALLA)\b")
RE_EXIT = re.compile(r"EXIT(?:CODE)?[=: ]+(\d+)", re.IGNORECASE)
# (a) TAREA 2 v104: fin de oracion, punto/exclamacion/interrogacion seguido de
# espacio o de fin de texto (un punto pegado a un digito, como en "3.853" o
# en un nombre de fichero enmascarado, no cuenta).
RE_FIN_ORACION = re.compile(r"[.!?](?=\s|$)")
# (b) TAREA 2 v104: la palabra inmediatamente anterior a la de veredicto, tras
# quitar puntuacion, es "afirmacion" (con o sin tilde): senala que la palabra
# de veredicto es el ADJETIVO de una afirmacion ajena, no un veredicto propio.
RE_PALABRA_ANTERIOR = re.compile(r"([A-Za-zÁÉÍÓÚáéíóúÑñ]+)[^A-Za-zÁÉÍÓÚáéíóúÑñ]*$")
# (c) TAREA 2 v104: la palabra va justo despues de una etiqueta de lista de un
# solo caracter entre parentesis, "(a)", "(b)", "(c)"...: es narracion de UN
# caso entre varios de una enumeracion (los "tres casos" de una mutacion), no
# el veredicto general del fichero citado, que se lee aparte (linea de cierre
# tipo "VERDE GENERAL").
RE_ETIQUETA_LISTA = re.compile(r"\([a-zA-Z]\)\s*$")


def resolver_cita(cita):
    """(1.1) Una cita PELADA (sin docs/loop/) se resuelve contra docs/loop/,
    que es donde vive toda esta familia de ficheros SALIDA_*. Una cita que ya
    trae el prefijo se deja tal cual. Nunca se inventa otra carpeta."""
    if cita.startswith("docs/loop/"):
        return cita
    return "docs/loop/%s" % cita


def leer_texto(ruta_o_ref, fallos):
    """RUTA_O_REF es o bien una ruta real (por defecto docs/loop/REPORTE.md)
    o, con --commit, se lee de `git show <commit>:<ruta>` para poder probar
    contra un REPORTE.md historico sin tocar el arbol de trabajo."""
    ruta_abs = ruta_o_ref if os.path.isabs(ruta_o_ref) else os.path.join(RAIZ, ruta_o_ref)
    if not os.path.exists(ruta_abs):
        fallos.append("no existe %s" % ruta_o_ref)
        return None
    return io.open(ruta_abs, encoding="utf-8").read()


def leer_texto_de_commit(commit, ruta, fallos):
    try:
        r = subprocess.run(["git", "show", "%s:%s" % (commit, ruta)], cwd=RAIZ,
                           capture_output=True, text=True, check=True)
        return r.stdout
    except Exception as e:
        fallos.append("no se pudo leer %s en %s: %s" % (ruta, commit, e))
        return None


def parrafos_con_offset(texto):
    """Divide TEXTO en parrafos (separados por linea(s) en blanco) y
    devuelve, por cada parrafo, su texto y el OFFSET absoluto donde empieza
    (para poder recuperar el numero de linea real despues)."""
    partes = []
    offset = 0
    for bloque in re.split(r"(\n\s*\n)", texto):
        if bloque.strip():
            partes.append((offset, bloque))
        offset += len(bloque)
    return partes


def numero_de_linea(texto, offset):
    return texto.count("\n", 0, offset) + 1


def veredicto_real_del_fichero(ruta_rel, fallos_locales):
    ruta_abs = os.path.join(RAIZ, ruta_rel)
    if not os.path.exists(ruta_abs):
        return None, "el fichero citado no existe"
    contenido = io.open(ruta_abs, encoding="utf-8").read()
    ultima = None
    for linea in contenido.splitlines():
        m = RE_LINEA_VEREDICTO.match(linea.strip())
        if m:
            ultima = m.group(1)
    if ultima is not None:
        return CLASE[ultima], None
    codigos = RE_EXIT.findall(contenido)
    if codigos:
        return ("OK" if codigos[-1] == "0" else "MAL"), None
    return None, "el fichero no trae ninguna linea VERDE/ROJO/PASA/FALLA ni EXIT=N: veredicto no legible"


def enmascarar_citas(parrafo, spans):
    """(a) TAREA 2 v104: devuelve una copia de PARRAFO con el texto de cada
    cita (comillas invertidas incluidas) sustituido por 'x', para que un
    punto DENTRO de un nombre de fichero no se lea como fin de oracion. La
    longitud no cambia: los offsets siguen sirviendo para todo lo demas."""
    lista = list(parrafo)
    for inicio, fin in spans:
        for i in range(inicio, fin):
            if lista[i] != "\n":
                lista[i] = "x"
    return "".join(lista)


def limites_de_oracion(parrafo_enmascarado):
    return [m.start() for m in RE_FIN_ORACION.finditer(parrafo_enmascarado)]


def oracion_de(pos, limites):
    """Indice de oracion de POS: cuenta cuantos finales de oracion caen
    ANTES de POS. Una posicion que cae justo EN el punto de cierre sigue en
    la misma oracion que lo precede."""
    return bisect.bisect_left(limites, pos)


def rango_de_oracion(idx, limites, largo):
    """(TAREA 1 v105) Rango [inicio, fin) de caracteres de la oracion de
    indice IDX dentro del parrafo, con los mismos limites que usa
    oracion_de(). La oracion 0 empieza en 0; la oracion i (i>0) empieza justo
    despues del limite i-1; la ultima oracion termina en LARGO (fin del
    parrafo) aunque no haya un fin de oracion detras (parrafo sin punto
    final)."""
    inicio = 0 if idx == 0 else limites[idx - 1] + 1
    fin = limites[idx] + 1 if idx < len(limites) else largo
    return inicio, fin


def trae_veredicto_propio(parrafo, inicio, fin):
    """(TAREA 1 v105) True si el tramo parrafo[inicio:fin] trae AL MENOS una
    palabra VERDE/ROJO/PASA/FALLA propia (sin filtrar por (b) ni (c): basta
    que la palabra este ahi para que la oracion pueda ser la narracion de
    OTRA cosa, y entonces no se le presta la cita)."""
    return bool(RE_VEREDICTO_PALABRA.search(parrafo[inicio:fin]))


def es_adjetivo_de_afirmacion(parrafo, pos):
    """(b) TAREA 2 v104: True si la palabra inmediatamente anterior a la de
    veredicto (en POS) es "afirmacion" o "afirmaciones", sin distinguir
    tilde ni mayuscula. Marca que la palabra de veredicto describe una
    afirmacion AJENA (narracion), no un veredicto propio."""
    m = RE_PALABRA_ANTERIOR.search(parrafo[:pos])
    if not m:
        return False
    palabra = m.group(1).lower().replace("ó", "o")
    return palabra in ("afirmacion", "afirmaciones")


def es_etiqueta_de_lista(parrafo, pos):
    """(c) TAREA 2 v104: True si justo antes de la palabra (solo espacio de
    por medio) hay una etiqueta de un caracter entre parentesis, "(a)",
    "(b)", "(c)"... Marca que la palabra narra UN caso de una enumeracion de
    varios (p.ej. "Tres casos: (a) VERDE ..., (b) ROJO ..."), cuyo veredicto
    de conjunto se lee aparte, en la linea de cierre del fichero citado."""
    return bool(RE_ETIQUETA_LISTA.search(parrafo[:pos]))


def elegir_cita(citas, pos):
    """Preferencia declarada (1.4 de la vuelta 103): la primera cita DESPUES
    de la palabra: si no hay ninguna, la cita ANTES mas cercana."""
    despues = [c for c in citas if c[0] > pos]
    antes = [c for c in citas if c[0] <= pos]
    if despues:
        return min(despues, key=lambda c: c[0] - pos), "primera cita DESPUES de la palabra"
    return max(antes, key=lambda c: c[0]), "cita ANTES mas cercana"


def hallar_afirmaciones(texto):
    """(TAREA 2 v104) Para cada ocurrencia de VERDE/ROJO/PASA/FALLA que no
    sea adjetivo de "afirmacion" (b) ni etiqueta de lista (c), busca la cita
    de fichero mas cercana que viva EN LA MISMA ORACION (a). (e, TAREA 1
    v105) Si la ORACION de la palabra no trae ninguna cita, se prueba la
    ORACION SIGUIENTE del mismo parrafo, PERO SOLO SI esa oracion siguiente
    no trae ninguna palabra de veredicto propia (si la trajera, podria ser la
    narracion de OTRA afirmacion, no la evidencia de esta). (d) Si la cita
    elegida (de la oracion o de la siguiente) resulta NO LEGIBLE (fichero
    inexistente o sin veredicto legible), se ensancha la busqueda al PARRAFO
    entero antes de darla por buena: una cita de oracion no legible es senal
    de que esa cita es evidencia de OTRA cosa (un hash, un nombre de comando)
    y la evidencia real vive al lado, en el mismo parrafo, que es la
    convencion de cabecera de esta campana. Devuelve (linea, palabra,
    fichero_citado, regla, n_citas) SOLO para las ocurrencias que si citan un
    fichero bajo estas reglas; el resto cuenta en la cobertura total pero no
    aqui."""
    afirmaciones = []
    for offset_parrafo, parrafo in parrafos_con_offset(texto):
        citas_todas = [(m.start(), m.end(), m.group(1)) for m in RE_CITA.finditer(parrafo)]
        if not citas_todas:
            continue
        enmascarado = enmascarar_citas(parrafo, [(c[0], c[1]) for c in citas_todas])
        limites = limites_de_oracion(enmascarado)
        for m in RE_VEREDICTO_PALABRA.finditer(parrafo):
            pos = m.start()
            if es_adjetivo_de_afirmacion(parrafo, pos) or es_etiqueta_de_lista(parrafo, pos):
                continue
            oracion_palabra = oracion_de(pos, limites)
            citas_oracion = [(c[0], c[2]) for c in citas_todas if oracion_de(c[0], limites) == oracion_palabra]
            ambito = "misma oracion"
            if not citas_oracion:
                # (e) TAREA 1 v105: ensanche a la oracion SIGUIENTE, solo si
                # esa oracion no trae su propia palabra de veredicto (si la
                # trajera, seria la unidad de argumentacion de OTRA cosa).
                idx_siguiente = oracion_palabra + 1
                if idx_siguiente <= len(limites):
                    ini_sig, fin_sig = rango_de_oracion(idx_siguiente, limites, len(parrafo))
                    if not trae_veredicto_propio(parrafo, ini_sig, fin_sig):
                        citas_oracion = [(c[0], c[2]) for c in citas_todas
                                        if ini_sig <= c[0] < fin_sig]
                        if citas_oracion:
                            ambito = "oracion siguiente sin veredicto propio (e)"
            if not citas_oracion:
                continue
            mejor, regla_base = elegir_cita(citas_oracion, pos)
            n_citas = len(citas_oracion)
            _, motivo_probe = veredicto_real_del_fichero(resolver_cita(mejor[1]), [])
            if motivo_probe is not None:
                citas_parrafo = [(c[0], c[2]) for c in citas_todas]
                mejor_p, regla_p = elegir_cita(citas_parrafo, pos)
                if mejor_p[1] != mejor[1]:
                    mejor, regla_base = mejor_p, regla_p
                    ambito, n_citas = "parrafo, cita de la oracion no legible (d)", len(citas_parrafo)
            regla = "%s, %s" % (regla_base, ambito)
            linea = numero_de_linea(texto, offset_parrafo + pos)
            afirmaciones.append((linea, m.group(1), mejor[1], regla, n_citas))
    return afirmaciones


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reporte", default="docs/loop/REPORTE.md")
    ap.add_argument("--commit", default=None,
                    help="si se da, lee --reporte de `git show <commit>:<reporte>` en vez del arbol de trabajo")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    fallos = []
    if a.commit:
        texto = leer_texto_de_commit(a.commit, a.reporte, fallos)
        etiqueta_fuente = "%s:%s" % (a.commit, a.reporte)
    else:
        texto = leer_texto(a.reporte, fallos)
        etiqueta_fuente = a.reporte
    if texto is None:
        print("ROJO, no se pudo leer %s:" % etiqueta_fuente)
        for f in fallos:
            print("   %s" % f)
        return 1

    afirmaciones = hallar_afirmaciones(texto)
    total_palabras = len(RE_VEREDICTO_PALABRA.findall(texto))
    print("=" * 90)
    print("TALLA DE VEREDICTOS de %s: %d afirmacion(es) VERDE/ROJO/PASA/FALLA citan fichero, "
          "de %d palabra(s) de veredicto en total en el reporte."
          % (etiqueta_fuente, len(afirmaciones), total_palabras))
    print("=" * 90)

    hallazgos = []
    for linea, palabra, cita, regla, n_citas in afirmaciones:
        fichero = resolver_cita(cita)
        nota_resolucion = "" if fichero == cita else " (pelado, resuelto a `%s`)" % fichero
        nota_emparejamiento = (" [%d cita(s), se uso: %s]" % (n_citas, regla)
                               if n_citas > 1 or "misma oracion" not in regla else "")
        clase_afirmada = CLASE[palabra]
        clase_real, motivo = veredicto_real_del_fichero(fichero, fallos)
        if motivo is not None:
            hallazgos.append("REPORTE.md linea %d: afirma %s citando `%s`%s, pero %s%s"
                             % (linea, palabra, cita, nota_resolucion, motivo, nota_emparejamiento))
            continue
        if clase_real != clase_afirmada:
            hallazgos.append("REPORTE.md linea %d: afirma %s (clase %s) citando `%s`%s, "
                             "y el veredicto REAL de ese fichero es %s%s"
                             % (linea, palabra, clase_afirmada, cita, nota_resolucion, clase_real, nota_emparejamiento))
        else:
            print("   linea %d: %s citando `%s`%s -- calza (fichero real: %s)%s"
                  % (linea, palabra, cita, nota_resolucion, clase_real, nota_emparejamiento))

    print()
    if hallazgos:
        print("ROJO, %d hallazgo(s):" % len(hallazgos))
        for h in hallazgos:
            print("   %s" % h)
        return 1

    print("VERDE: las %d afirmacion(es) que citan fichero calzan con el veredicto real de su fichero."
          % len(afirmaciones))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
