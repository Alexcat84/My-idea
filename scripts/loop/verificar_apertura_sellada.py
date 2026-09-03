# -*- coding: utf-8 -*-
r"""verificar_apertura_sellada.py . LA GUARDA DE LA APERTURA (TAREA 1.2 de la
vuelta 101, acta de la vuelta 100, seccion "SEGUNDA CAIDA, DE INCUMPLIMIENTO
DE ENCARGO"). Nombre estable, SIN numero de vuelta (como
tallar_cabecera_reporte.py y contar_cierre_efectivo.py): se invoca con
--vuelta N y no se clona cada vuelta.

POR QUE NACE. EJECUTOR.md 1 dice, desde el 14 ago 2026, "LA APERTURA SE MIDE
ANTES DE LA PRIMERA OPERACION". La vuelta 99 ya habia caido en esto una vez
(acta 99). La vuelta 100 volvio a caer, y peor: SALIDA_V100_HEAD_APERTURA.txt
SI nacio en el primer commit de la vuelta (300802d1, hijo directo de
c8827ef7, el acta de la vuelta 99), pero los OCHO ficheros
SALIDA_V100_*_APERTURA.txt restantes (GATE0_CMD1, CONTEO, DESFASE_CALIBRADO,
ETIQUETAS, MOTOR, SYNC, TSC, WEB) nacieron TODOS en 592cf8bc, el ULTIMO
commit de la vuelta, junto con el reporte final. Nadie lo habia comprobado
con una guarda: el auditor tuvo que medirlo a mano con `git log
--diff-filter=A` sobre cada fichero. Esta guarda automatiza esa medicion.

QUE COMPRUEBA. La vara la da git, no se inventa (EJECUTOR.md, "LA IDENTIDAD
SE LEE DE GIT"): el COMMIT DE NACIMIENTO de cada
`docs/loop/SALIDA_V<vuelta>_*_APERTURA.txt` (el commit que lo ANADE, via
`git log --diff-filter=A`) tiene que ser el PRIMER commit de la vuelta, es
decir, el HIJO DIRECTO del commit del acta de la vuelta anterior (el commit
cuyo mensaje empieza por "ACTA DE LA VUELTA <vuelta-1> DEL AUDITOR", el mismo
patron que ya usa `tallar_cabecera_reporte.py`). Cae en ROJO si:
  - no hay ningun commit "ACTA DE LA VUELTA <vuelta-1> DEL AUDITOR" en la
    rama, o hay mas de uno (ambiguo);
  - algun `SALIDA_V<vuelta>_*_APERTURA.txt` no existe en el arbol de trabajo;
  - algun fichero de apertura no tiene EXACTAMENTE un commit que lo anada
    (cero o mas de uno: ambiguo o no versionado);
  - el PADRE del commit que anade un fichero de apertura NO es el commit del
    acta (nacio despues del primer commit, a mitad o al final de la vuelta).

Nunca inventa un hash ni asume una fecha: todo se lee de `git log` de la rama
actual (`git rev-parse --abbrev-ref HEAD`).

USO:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 101
  python scripts/loop/verificar_apertura_sellada.py --vuelta 100

PRUEBA DE MUTACION (con su salida commiteada,
docs/loop/SALIDA_V101_TAREA1_2_MUTACION_APERTURA.txt): (a) VERDE sobre la
vuelta 101 (bien sellada, con TODOS sus `*_APERTURA.txt` en el primer commit
de la vuelta); (b) ROJO sobre la vuelta 100, el caso negativo real, sin
inventar nada: nombra los ocho ficheros que nacieron en 592cf8bc en vez de en
300802d1.

--- LA GUARDA QUE SE ENVENENA SOLA (TAREA 1.3 de la vuelta 102, acta de la
vuelta 101, "PRIMERA, DE REPORTE, Y ACUMULA") ---

POR QUE NACE. `ficheros_apertura()` hacia glob de
`SALIDA_V<vuelta>_*_APERTURA.txt` sobre el arbol de trabajo, y ese patron
CASA CON SU PROPIA SALIDA: la prueba de mutacion de esta guarda escribe
`docs/loop/SALIDA_V<vuelta>_TAREA1_2_MUTACION_APERTURA.txt`, que empieza por
`SALIDA_V<vuelta>_` y termina en `_APERTURA.txt` igual que cualquier
medicion real. El dia que nace no esta commiteada (glob solo ve el arbol de
trabajo, "ningun commit lo anade"), y desde el commit siguiente nace en el
SEGUNDO commit de la vuelta, nunca en el primero: una guarda que no puede
estar VERDE ni el dia que nace ni ningun dia despues, y que se prueba a si
misma como si fuera una medicion de apertura.

LA DECISION (declarada aqui, con su motivo): `ficheros_apertura()` DESCARTA
todo `SALIDA_V<vuelta>_*_APERTURA.txt` cuyo segmento intermedio (el `*` del
patron) contenga la palabra `MUTACION`. Ninguna medicion de apertura real
(HEAD, GATE0_CMD1, ETIQUETAS, SYNC, MOTOR, WEB, TSC, CONTEO,
DESFASE_CALIBRADO, y las que se sumen despues) lleva `MUTACION` en su
nombre: es una palabra reservada para las propias salidas de prueba de esta
guarda, por convencion desde esta vuelta en adelante. NO SE USO UNA NOMINA
CERRADA de nombres de medicion porque esa lista ha crecido de verdad entre
vueltas (ETIQUETAS y SYNC no existian antes de la vuelta 100) y una nomina
fija se volveria ciega a una medicion nueva y legitima que alguien olvide
anadir a la lista; excluir por la palabra `MUTACION` no tiene ese defecto,
porque una medicion real nunca la necesita para nombrarse.

LA GUARDA NO SE VUELVE CIEGA A UN FICHERO DE APERTURA QUE LLEGUE TARDE DE
VERDAD: la exclusion es por el NOMBRE (contener `MUTACION`), no por cuando
nacio el fichero; cualquier `SALIDA_V<vuelta>_<KIND>_APERTURA.txt` real,
nazca en el primer commit o mas tarde, se sigue viendo y comprobando igual
que antes. Lo unico que deja de verse es la prueba de esta misma guarda.

PRUEBA DE MUTACION (con su salida commiteada,
docs/loop/SALIDA_V102_TAREA1_3_MUTACION_APERTURA.txt): (a) VERDE sobre la
vuelta 101 DESPUES del arreglo (con `SALIDA_V101_TAREA1_2_MUTACION_APERTURA.txt`
todavia presente en el arbol de trabajo, la guarda ya no se la come); (b)
ROJO sobre la vuelta 100, que sigue siendo el caso negativo real, sin
cambios; (c) ROJO si se mueve a mano un fichero de apertura real al SEGUNDO
commit, sobre una copia temporal de repositorio (nunca sobre el repo real):
ver scripts/loop/vuelta102_tarea1_prueba_mutacion_apertura.py, caso (c).

--- EL SELLO FIJA CONTENIDO, NO SOLO NACIMIENTO (TAREA 4, vuelta 108) ---

POR QUE NACE (acta de la vuelta 107, seccion 1.7). Esta guarda comprobaba EN
QUE COMMIT NACIO cada salida de apertura, pero nunca si su CONTENIDO DE HOY
seguia siendo el mismo con el que nacio. La vuelta 107 lo demostro sin
querer: el commit 87b4753d reescribio SALIDA_V107_TSC_APERTURA.txt (nacida
en fcb90afc con la linea "EXIT=0", hoy vacia) y la guarda siguio VERDE
porque solo miraba el commit de nacimiento, nunca el contenido de hoy.

QUE COMPRUEBA, DE MAS. Para cada `SALIDA_V<vuelta>_*_APERTURA.txt`, el
sha256 NORMALIZADO (CRLF y CR sueltos igualados a LF antes de hashear: el
repo tiene `core.autocrlf=true`, asi que el blob de git siempre trae LF
mientras el arbol de trabajo en Windows trae CRLF, y esa diferencia de
sistema operativo NO es un cambio de contenido) del blob del commit de
nacimiento (`git show <nacido_en>:docs/loop/<nombre>`) contra el sha256
NORMALIZADO del fichero de HOY en el arbol de trabajo. Si difieren, ROJO,
nombrando el fichero y los dos hashes completos: nunca se calla cual
cambio ni se resume "algo no cuadra".

Que sea legitimo corregir un artefacto (como la vuelta 107 corrigio el
`EXIT=0` espurio del tsc) no quita que tenga que VERSE: si hay que
reescribir una salida de apertura, se reescribe y esta guarda lo canta, y
el reporte lo explica. Es lo contrario de degradarse en silencio (banco
9, "fallar ruidoso").

--- EL CORREDOR DE LA PARADA (TAREA 0.d, vuelta 148) ---

POR QUE NACE. Esta guarda medía el fin ("la apertura se sello ANTES de la
primera operacion de la vuelta") con un PROXY: "el padre del commit de
nacimiento es el commit del acta de la vuelta anterior". El proxy vale
mientras el bucle encadena vuelta tras vuelta sin interrupcion, y se rompe
la primera vez que el bucle SE PARA y el fundador contesta la parada en un
commit propio, que es exactamente la forma de la vuelta 148: entre el acta
de la 147 (84b64cd0) y el bloque de apertura de la 148 (5567cdc8) vive
68db6230, "Decision del fundador", que escribe la decision y el encargo. La
guarda vieja, corrida por mi en esta vuelta, dio ROJO con los diez ficheros
dentro y el motivo literal "cuyo padre es 68db6230 (no el commit del acta
84b64cd0)", y su salida esta commiteada en
docs/loop/SALIDA_V148_0D_APERTURA_SELLADA_GUARDA_VIEJA.txt. Ninguna
apertura se habia medido tarde: lo que fallaba era la vara. Y la caida es
ESTRUCTURAL, no un accidente: toda vuelta que reanude tras una parada de
decision del fundador nace con ese commit en medio.

QUE COMPRUEBA AHORA, Y NO ES MAS LAXO SINO MAS PRECISO. Si el padre del
commit de nacimiento NO es el commit del acta, la guarda ya no se rinde: mide
EL CORREDOR, o sea todos los commits que van del acta (exclusive) al commit
de nacimiento (exclusive), y exige DOS cosas:
  - que el acta sea ANTEPASADO del commit de nacimiento (`git merge-base
    --is-ancestor`); si el bloque de apertura cuelga de otra rama, ROJO;
  - que TODO commit del corredor toque UNICAMENTE papeles de la parada:
    `docs/loop/PROMPT_SIGUIENTE.md`, `docs/loop/PARA_ALEXIS.md` y cualquier
    cosa bajo `docs/loop/paradas/`. Son los tres sitios donde se escribe una
    parada y su respuesta, y NINGUNO de ellos puede mover una sola de las
    cifras que la apertura mide (censo, Gate 0, aristas, motor, web, tsc,
    desfase del calibrado). Un commit del corredor que toque cualquier otra
    ruta ES una operacion, y entonces la apertura se midio tarde de verdad:
    ROJO nombrando el commit y las rutas ajenas, una a una, sin resumir.

EL CORREDOR ACEPTADO NO SE CALLA (banco 9, "fallar ruidoso"): cuando la
guarda sale VERDE con corredor, lo IMPRIME entero, con el hash y el asunto de
cada commit que dejo pasar. Un corredor invisible seria la misma degradacion
silenciosa que esta guarda existe para impedir.

CASO ROJO POR MUTACION, SOBRE VARIABLE COMPUTADA (EJECUTOR 1, "EL CASO ROJO
SE PRUEBA POR MUTACION"): la decision vive en `intrusos_del_corredor`, que es
PURA (recibe el corredor ya leido de git y no vuelve a tocar el disco), asi
que se le puede dar el corredor REAL leido de git y una copia mutada del
mismo. Ver scripts/loop/vuelta148_0d_mutacion_corredor.py y su salida
docs/loop/SALIDA_V148_0D_MUTACION_CORREDOR.txt.

CASO POSITIVO OBLIGATORIO (vuelta 108): `--vuelta 107` da ROJO nombrando
`SALIDA_V107_TSC_APERTURA.txt` con sus dos sha256 (docs/loop/
SALIDA_V108_TAREA4_3_CASO_VUELTA107_ROJO.txt, el caso real que lo produjo);
`--vuelta 108`, corrida al cierre de esta misma vuelta, da VERDE.

--- ADJUDICACION 6.7 DEL ACTA 153 (2 sep 2026): EL CORREDOR ADMITE EL COMMIT DE
LA DECISION DEL FUNDADOR, Y LO NOMBRA APARTE ---

CORRECCION DECLARADA POR ADICION. NADA DEL TEXTO ANTERIOR SE BORRA.

EL CASO REAL QUE LA OBLIGA (vuelta 152): el corredor traia DOS commits, el del
ejecutor (`6f419952`) y `d9fa886b`, LA DECISION DEL FUNDADOR, que toca
`docs/loop/AUDITOR.md` y `docs/plan/OPERACIONES.jsonl` porque el encargo manda
aplicar las respuestas donde viven. La guarda fallaba por los dos por igual.

LO QUE EL ACTA ADJUDICA: `AUDITOR.md` seccion 4 trata la decision del fundador
como una CATEGORIA PROPIA, ajena al trabajo del bucle; un commit de decision NO
es el ejecutor tocando nada. El corredor ADMITE el commit de la decision del
fundador QUE `docs/loop/PROMPT_SIGUIENTE.md` CITA POR SU HASH, y la guarda lo
NOMBRA APARTE en vez de fallar por el.

Y LA MITAD QUE NO SE TOCA, dicha con todas sus letras: EL ROJO POR UN COMMIT DEL
PROPIO EJECUTOR DENTRO DEL CORREDOR SE QUEDA INTACTO. Esa mitad del rojo de la
vuelta 152 era legitima. La admision es por HASH CITADO EN EL ENCARGO, no por
autor adivinado ni por ruta: un hash que el encargo no cite no entra.

--- ADJUDICACION 6.8 DEL ACTA 155 (3 sep 2026): LA PUERTA SE ESTRECHA A LO QUE
LA 6.7 DEL ACTA 153 CONCEDIO, Y LA VARA SE FIJA ---

CORRECCION DECLARADA POR ADICION. EL BLOQUE DE LA ADJUDICACION 6.7 DEL ACTA 153
QUE ESTA JUSTO ENCIMA NO SE BORRA: describe con exactitud lo que la puerta hizo
entre la vuelta 154 y hoy, y taparlo impediria auditar por que fue mas ancha de
lo concedido.

LAS DOS COSAS QUE EL AUDITOR MIDIO LLAMANDO A LA PROPIA FUNCION DE ESTA GUARDA:
  (i)  LA PUERTA ERA MAS ANCHA QUE LA CONCESION. La 6.7 del acta 153 concedio
       admitir EL COMMIT DE LA DECISION DEL FUNDADOR que el encargo cite por su
       hash. La implementacion admitia CUALQUIER hash que el encargo citara,
       sea de quien sea: medido el 3 sep 2026, los hashes admitidos eran
       `6f695db6` y `c9c6ea40`, LOS DOS COMMITS DEL EJECUTOR. Hoy no hacia dano
       (ninguno cae dentro de un corredor), pero la puerta concedida era otra.
  (ii) LA VARA ESTABA ANCLADA A ALGO QUE SE MUEVE. `hashes_citados_por_el_encargo`
       leia `docs/loop/PROMPT_SIGUIENTE.md` DEL ARBOL DE TRABAJO, asi que el
       veredicto del corredor de una vuelta YA JUZGADA podia cambiar cuando se
       escribiera un encargo posterior. Es LA MISMA ESPECIE que las caidas 5 y 6
       que el ejecutor declaro en la vuelta 154, una vara anclada a algo que se
       mueve, viviendo dentro de una guarda escrita en esa misma vuelta.

LO QUE SE ADJUDICA, Y NO ES DOCTRINA NUEVA (es la letra de la 6.7 mas la vara
que el propio ejecutor ya se aplico a si mismo):
  (a) SOLO ENTRA LO MARCADO. El encargo declara sus hashes admitidos con un
      LITERAL EXPLICITO, y la guarda admite unicamente los marcados. Un hash
      citado de paso NO entra. La cabecera del encargo de la vuelta 156 ya trae
      el literal, y dice NINGUNO.
  (b) LA VARA SE FIJA. El encargo se lee DEL COMMIT DEL ACTA de la vuelta que se
      comprueba (`git show` del acta sobre docs/loop/PROMPT_SIGUIENTE.md), no
      del arbol de trabajo. El acta ya se localiza aqui con `commit_acta`, asi
      que la vara es la misma que la guarda ya usa para todo lo demas.
  (c) LA GUARDA LOS SIGUE NOMBRANDO APARTE, nunca en silencio.
  (d) EL ROJO POR UN COMMIT DEL PROPIO EJECUTOR DENTRO DEL CORREDOR SE QUEDA
      INTACTO. Esa mitad no se toca.
"""
import argparse
import glob
import hashlib
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")


def _git(args, fallos, contexto):
    try:
        r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True, text=True, check=True)
        return r.stdout
    except Exception as e:
        fallos.append("no se pudo correr git %s (%s): %s" % (" ".join(args), contexto, e))
        return None


def rama_actual(fallos):
    out = _git(["rev-parse", "--abbrev-ref", "HEAD"], fallos, "rama actual")
    return out.strip() if out is not None else None


def commit_acta(vuelta, rama, fallos):
    """Commit cuyo mensaje empieza por 'ACTA DE LA VUELTA <vuelta-1> DEL
    AUDITOR' O por 'ACTA DEL AUDITOR, VUELTA <vuelta-1>', igual que
    tallar_cabecera_reporte.py:commit_apertura_desde_git.

    LA SEGUNDA FORMA SE SUMA EN LA VUELTA 106 (guarda envejecida, hallada al
    sellar la apertura: verificar_apertura_sellada.py --vuelta 106 daba ROJO
    pese a que los diez SALIDA_V106_*_APERTURA.txt nacieron todos, medido a
    mano, como hijos directos de fc504151). El acta de la vuelta 105
    (fc504151) titula su commit 'ACTA DEL AUDITOR, VUELTA 105, mas el
    encargo de la 106.', que rompe por primera vez el patron literal
    'ACTA DE LA VUELTA N DEL AUDITOR' vigente sin excepcion desde la vuelta
    92 (ver git log: 92 a 104 usan la forma vieja). Las dos formas nombran
    lo mismo (el commit del acta que cierra la vuelta N-1); se aceptan las
    dos en vez de renombrar el commit ya publicado."""
    out = _git(["log", rama, "--pretty=format:%H\x01%s"], fallos, "git log de la rama")
    if out is None:
        return None
    patrones = [
        re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR\b" % (vuelta - 1)),
        re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA %d\b" % (vuelta - 1)),
    ]
    hallados = []
    for linea in out.splitlines():
        if "\x01" not in linea:
            continue
        h, s = linea.split("\x01", 1)
        if any(p.match(s) for p in patrones):
            hallados.append(h)
    if not hallados:
        fallos.append("git log de la rama %s no trae ningun commit 'ACTA DE LA VUELTA %d "
                      "DEL AUDITOR': no se puede fijar el commit de referencia" % (rama, vuelta - 1))
        return None
    if len(hallados) > 1:
        fallos.append("git log de la rama %s trae %d commits 'ACTA DE LA VUELTA %d DEL "
                      "AUDITOR' (%s): ambiguo" % (rama, len(hallados), vuelta - 1,
                                                    ", ".join(h[:8] for h in hallados)))
        return None
    return hallados[0]


def es_prueba_de_esta_guarda(nombre, vuelta):
    """Descarta las propias salidas de la prueba de mutacion de esta guarda
    (ver docstring, 'LA GUARDA QUE SE ENVENENA SOLA'): el segmento intermedio
    del nombre (entre el prefijo SALIDA_V<vuelta>_ y el sufijo _APERTURA.txt)
    contiene la palabra MUTACION, que ninguna medicion real usa."""
    prefijo = "SALIDA_V%d_" % vuelta
    sufijo = "_APERTURA.txt"
    medio = nombre[len(prefijo):-len(sufijo)]
    return "MUTACION" in medio


def ficheros_apertura(vuelta):
    patron = os.path.join(LOOP, "SALIDA_V%d_*_APERTURA.txt" % vuelta)
    candidatos = sorted(os.path.basename(p) for p in glob.glob(patron))
    return [n for n in candidatos if not es_prueba_de_esta_guarda(n, vuelta)]


def commit_de_nacimiento(nombre, rama, fallos):
    rel = "docs/loop/%s" % nombre
    out = _git(["log", rama, "--diff-filter=A", "--pretty=format:%H", "--", rel],
               fallos, "nacimiento de %s" % nombre)
    if out is None:
        return None
    hallados = [h for h in out.splitlines() if h.strip()]
    if not hallados:
        fallos.append("%s: ningun commit lo anade (no versionado)" % nombre)
        return None
    if len(hallados) > 1:
        fallos.append("%s: %d commits lo anaden (%s): ambiguo" %
                      (nombre, len(hallados), ", ".join(h[:8] for h in hallados)))
        return None
    return hallados[0]


PAPELES_DE_LA_PARADA = (
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/PARA_ALEXIS.md",
)
CARPETA_DE_PARADAS = "docs/loop/paradas/"


def es_papel_de_la_parada(ruta):
    """Una ruta que solo puede llevar la parada o su respuesta. Ninguna de
    ellas entra en el censo, en Gate 0, en las aristas, en las suites, en el
    tsc ni en el desfase del calibrado, o sea que ninguna puede mover una
    cifra de la apertura."""
    return ruta in PAPELES_DE_LA_PARADA or ruta.startswith(CARPETA_DE_PARADAS)


PATRON_HASH = re.compile(r"\b[0-9a-f]{7,40}\b")


def hashes_citados_por_el_encargo():
    """LOS HASHES QUE `docs/loop/PROMPT_SIGUIENTE.md` CITA, resueltos con git a
    su forma completa. Devuelve (conjunto de hashes completos, lista de los
    literales que se leyeron), y nunca inventa: un literal que `git rev-parse`
    no resuelve a un commit de este repo NO entra.

    ES LA UNICA PUERTA DE ADMISION DEL CORREDOR (adjudicacion 6.7 del acta
    153). Por HASH CITADO EN EL ENCARGO, no por autor adivinado, no por asunto
    y no por ruta: si el encargo no lo cita, no entra.

    --- ESTA FUNCION QUEDA SUSTITUIDA (vuelta 156, TAREA 5, adjudicacion 6.8 del
    acta 155). NO SE BORRA: se conserva entera porque es la unica forma de
    ENSENAR LAS DOS PUERTAS sobre la misma entrada, que es lo que el caso por
    mutacion necesita. Una puerta vieja borrada no se puede contrastar. ---

    LOS DOS DEFECTOS QUE EL AUDITOR MIDIO LLAMANDO A ESTA MISMA FUNCION:
      (i)  ADMITIA CUALQUIER HASH QUE EL ENCARGO CITARA, sea de quien sea. La
           6.7 concedio EL COMMIT DE LA DECISION DEL FUNDADOR, no cualquier hash
           citado de paso. Medido el 3 sep 2026: admitia `6f695db6` y
           `c9c6ea40`, los dos commits del EJECUTOR.
      (ii) LEIA EL ARBOL DE TRABAJO, asi que el veredicto del corredor de una
           vuelta YA JUZGADA podia cambiar cuando se escribiera un encargo
           posterior. Vara anclada a algo que se mueve.

    La sustituta es `hashes_admitidos_por_el_encargo(vuelta, acta)`."""
    ruta = os.path.join(LOOP, "PROMPT_SIGUIENTE.md")
    if not os.path.exists(ruta):
        return set(), []
    with open(ruta, encoding="utf-8", errors="replace") as fh:
        texto = fh.read()
    literales, completos = [], set()
    for lit in sorted(set(PATRON_HASH.findall(texto))):
        try:
            r = subprocess.run(["git", "rev-parse", "--verify", "%s^{commit}" % lit],
                               cwd=RAIZ, capture_output=True, check=True)
        except Exception:
            continue
        completos.add(r.stdout.decode().strip())
        literales.append(lit)
    return completos, literales


# --- LA PUERTA ESTRECHA Y LA VARA FIJA (vuelta 156, TAREA 5, adjudicacion 6.8
# del acta 155) -------------------------------------------------------------
#
# EL LITERAL QUE EL ENCARGO TIENE QUE ESCRIBIR PARA ADMITIR ALGO. Sin este
# rotulo no hay admision posible: un hash citado de paso NO entra, por mucho que
# aparezca en el encargo. El rotulo se busca en el encargo LEIDO DEL COMMIT DEL
# ACTA de la vuelta que se comprueba, no del arbol de trabajo.
ROTULO_ADMITIDOS = "HASHES ADMITIDOS EN EL CORREDOR DE ESTA VUELTA:"
# La palabra con la que el encargo dice "ninguno" de forma explicita. Se exige
# que lo DIGA: un rotulo con la lista vacia y sin palabra seria ambiguo.
PALABRA_NINGUNO = "NINGUNO"


def texto_del_encargo_en_el_acta(acta, fallos=None):
    """EL ENCARGO SE LEE DEL COMMIT DEL ACTA, CON git show, NO DEL ARBOL DE
    TRABAJO (adjudicacion 6.8 del acta 155, punto ii).

    POR QUE: el veredicto del corredor de la vuelta N tiene que ser el mismo
    hoy y dentro de diez vueltas. Leyendo el arbol de trabajo, el encargo de la
    vuelta N+3 cambiaba el veredicto de la vuelta N. Es la misma especie que el
    ejecutor declaro como sus caidas 5 y 6 en la vuelta 154, y el remedio es el
    suyo: anclar la vara a un commit.

    Devuelve None si el encargo no existe en ese commit (y lo registra), que es
    lo mismo que "ese encargo no admitio nada"."""
    r = subprocess.run(["git", "show", "%s:docs/loop/PROMPT_SIGUIENTE.md" % acta],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        if fallos is not None:
            fallos.append("el commit del acta %s no trae docs/loop/PROMPT_SIGUIENTE.md: "
                          "no hay encargo del que leer hashes admitidos" % acta[:8])
        return None
    return r.stdout.decode("utf-8", "replace")


def hashes_admitidos_por_el_encargo(texto, fallos=None):
    """SOLO ENTRA LO MARCADO (adjudicacion 6.8 del acta 155, punto i).

    Devuelve (conjunto de hashes completos, lista de literales leidos, rotulo
    hallado si o no). La admision exige LAS TRES COSAS:
      1. que el encargo traiga el rotulo literal `ROTULO_ADMITIDOS`;
      2. que detras del rotulo, y HASTA EL FINAL DE ESA LINEA LOGICA (el
         parrafo), venga o la palabra NINGUNO o una lista de hashes;
      3. que cada hash resuelva con `git rev-parse` a un commit de este repo.

    UN ENCARGO SIN EL ROTULO NO ADMITE NADA. Eso hace la regla PROSPECTIVA: los
    encargos viejos, que no lo traen, admiten el conjunto vacio, que es
    exactamente lo que la guarda hacia antes de la adjudicacion 6.7. NINGUN
    VEREDICTO VIEJO CAMBIA POR ESTO.

    PURA A PROPOSITO salvo por `git rev-parse`: recibe el TEXTO ya leido, para
    que el caso por mutacion pueda darle un encargo fabricado sin tocar el disco
    ni el arbol de trabajo."""
    if texto is None:
        return set(), [], False
    i = texto.find(ROTULO_ADMITIDOS)
    if i < 0:
        return set(), [], False
    # el parrafo que sigue al rotulo: hasta la primera linea en blanco
    resto = texto[i + len(ROTULO_ADMITIDOS):]
    corte = resto.find(chr(10) + chr(10))
    parrafo = resto if corte < 0 else resto[:corte]
    if PALABRA_NINGUNO in parrafo.upper().split(".")[0]:
        return set(), [], True
    literales, completos = [], set()
    for lit in sorted(set(PATRON_HASH.findall(parrafo))):
        try:
            r = subprocess.run(["git", "rev-parse", "--verify", "%s^{commit}" % lit],
                               cwd=RAIZ, capture_output=True, check=True)
        except Exception:
            if fallos is not None:
                fallos.append("el encargo MARCA como admitido el literal %r y git no lo "
                              "resuelve a un commit de este repo: no entra" % lit)
            continue
        completos.add(r.stdout.decode().strip())
        literales.append(lit)
    return completos, literales, True


def intrusos_del_corredor(corredor, admitidos=()):
    """PURA A PROPOSITO (para que el caso rojo se pueda probar por mutacion
    sin tocar git ni el disco): recibe el corredor ya leido,
    [(hash, asunto, [rutas])], y devuelve DOS listas,
    (intrusos, admitidos_por_el_encargo), cada una [(hash, asunto, [rutas
    ajenas])]. Lista de intrusos vacia significa corredor limpio.

    --- ADJUDICACION 6.7 DEL ACTA 153, APLICADA AQUI (vuelta 154, TAREA 6) ---

    CORRECCION DECLARADA POR ADICION. La firma vieja recibia solo `corredor` y
    devolvia UNA lista; ahora recibe ademas `admitidos` (hashes completos que el
    encargo cita) y devuelve DOS. `admitidos` VACIO reproduce exactamente el
    comportamiento anterior, asi que ninguna corrida vieja cambia de veredicto
    por esta ampliacion sola.

    UN COMMIT DEL CORREDOR QUE ESTE EN `admitidos` NO ES INTRUSO: sale por la
    segunda lista, para que la guarda LO NOMBRE APARTE en vez de fallar por el.
    NO SE CALLA NUNCA (banco 9, fallar ruidoso): un commit admitido en silencio
    seria peor que el rojo que sustituye, porque el corredor volveria a ser
    invisible.

    Y LA MITAD QUE NO SE TOCA: el rojo por un commit del PROPIO EJECUTOR sigue
    intacto. La admision es POR HASH CITADO EN EL ENCARGO, y un commit que el
    ejecutor escribe a mitad de vuelta no puede estar citado en el encargo que
    se escribio antes de que existiera."""
    intrusos, admitidos_vistos = [], []
    admitidos = set(admitidos or ())
    for h, asunto, rutas in corredor:
        ajenas = sorted(r for r in rutas if not es_papel_de_la_parada(r))
        if not ajenas:
            continue
        if h in admitidos:
            admitidos_vistos.append((h, asunto, ajenas))
        else:
            intrusos.append((h, asunto, ajenas))
    return intrusos, admitidos_vistos


def corredor_desde_git(acta, nacido_en, fallos):
    """Los commits que van del acta (exclusive) al commit de nacimiento
    (exclusive), cada uno con TODAS las rutas que toca. Devuelve None si el
    acta no es antepasado del commit de nacimiento (fallo registrado)."""
    try:
        subprocess.run(["git", "merge-base", "--is-ancestor", acta, nacido_en],
                       cwd=RAIZ, capture_output=True, check=True)
    except Exception:
        fallos.append("el commit del acta %s NO es antepasado de %s: el bloque de "
                      "apertura no cuelga de la vuelta anterior" % (acta[:8], nacido_en[:8]))
        return None
    out = _git(["log", "--format=%H%s", "%s..%s^" % (acta, nacido_en)],
               fallos, "corredor entre el acta y la apertura")
    if out is None:
        return None
    corredor = []
    for linea in out.splitlines():
        if "" not in linea:
            continue
        h, asunto = linea.split("", 1)
        rutas_out = _git(["show", "--name-only", "--format=", "-M", h],
                         fallos, "rutas de %s" % h[:8])
        if rutas_out is None:
            return None
        rutas = [r.strip() for r in rutas_out.splitlines() if r.strip()]
        corredor.append((h, asunto, rutas))
    return corredor


def _normalizar_finales_de_linea(datos):
    """CRLF/LF no es cambio de CONTENIDO (TAREA 4, vuelta 108): este repo
    tiene core.autocrlf=true, asi que el arbol de trabajo en Windows trae
    CRLF mientras que el blob de git (lo que `git show <commit>:ruta`
    devuelve) siempre trae LF. Comparar los bytes crudos daria ROJO en
    TODO fichero de mas de una linea, sin que nadie lo haya tocado de
    verdad. Se normaliza CRLF y CR sueltos a LF en los dos lados antes de
    hashear, para que la guarda mida CONTENIDO y no la convencion de fin de
    linea del sistema operativo."""
    return datos.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def sha256_normalizado(datos):
    return hashlib.sha256(_normalizar_finales_de_linea(datos)).hexdigest()


def blob_de_nacimiento(nombre, nacido_en, fallos):
    """El contenido del fichero TAL COMO QUEDO en el commit que lo anadio
    (TAREA 4.1, vuelta 108): `git show <nacido_en>:docs/loop/<nombre>`."""
    rel = "docs/loop/%s" % nombre
    try:
        r = subprocess.run(["git", "show", "%s:%s" % (nacido_en, rel)], cwd=RAIZ,
                           capture_output=True, check=True)
        return r.stdout
    except Exception as e:
        fallos.append("no se pudo leer el blob de nacimiento de %s en %s: %s"
                      % (nombre, nacido_en[:8], e))
        return None


def contenido_igual_al_nacer(nombre, nacido_en, fallos):
    """TAREA 4 de la vuelta 108 (encargo del auditor, acta de la vuelta 107,
    seccion 1.7: "LA GUARDA DEL SELLO QUE NO ALCANZA"). El sello de
    verificar_apertura_sellada.py comprobaba EN QUE COMMIT NACIO cada salida
    de apertura, pero nunca si su CONTENIDO DE HOY seguia siendo el mismo con
    el que nacio. La vuelta 107 lo demostro sin querer: el commit 87b4753d
    reescribio SALIDA_V107_TSC_APERTURA.txt (nacida en fcb90afc con la linea
    "EXIT=0", hoy vacia) y la guarda siguio VERDE.

    Compara el sha256 NORMALIZADO (ver _normalizar_finales_de_linea) del blob
    del commit de nacimiento contra el sha256 NORMALIZADO del fichero de HOY
    en el arbol de trabajo. Devuelve (iguales, hash_nacimiento, hash_hoy);
    (None, None, None) si el fichero de hoy no existe o el blob no se pudo
    leer (fallo ya registrado en `fallos` por el llamador)."""
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        fallos.append("%s no existe en el arbol de trabajo (no se puede comparar contenido)" % nombre)
        return None, None, None
    blob = blob_de_nacimiento(nombre, nacido_en, fallos)
    if blob is None:
        return None, None, None
    with open(ruta, "rb") as f:
        hoy = f.read()
    h_nac = sha256_normalizado(blob)
    h_hoy = sha256_normalizado(hoy)
    return h_nac == h_hoy, h_nac, h_hoy


def verificar(vuelta):
    # CORRECCION DECLARADA (vuelta 156, TAREA 5). LAS TRES SALIDAS TEMPRANAS
    # DEVOLVIAN UNA TUPLA DE TRES Y `main` DESEMPAQUETA CINCO: cualquiera de las
    # tres reventaba con ValueError en vez de imprimir el ROJO que ya tenia
    # escrito en `fallos`. Nunca se disparo porque las tres piden un repo raro
    # (sin rama, sin acta, sin ficheros de apertura), pero un rojo que revienta
    # en vez de hablar es lo contrario de fallar ruidoso (banco 9). Las tres
    # devuelven ahora la tupla completa, con los tres huecos vacios.
    fallos = []
    vacio = ([], {}, {}, [], False, None)
    rama = rama_actual(fallos)
    if rama is None:
        return (fallos,) + vacio
    acta = commit_acta(vuelta, rama, fallos)
    if acta is None:
        return (fallos,) + vacio

    nombres = ficheros_apertura(vuelta)
    if not nombres:
        fallos.append("no existe ningun docs/loop/SALIDA_V%d_*_APERTURA.txt en el arbol de trabajo" % vuelta)
        return (fallos,) + vacio

    detalle = []
    corredores = {}   # cache: un corredor por commit de nacimiento, no uno por fichero
    declarados = {}   # corredores ACEPTADOS, que se imprimen y nunca se callan
    # ADJUDICACION 6.7 DEL ACTA 153 (vuelta 154): la puerta de admision del
    # corredor son LOS HASHES QUE EL ENCARGO CITA, leidos de git y no tecleados.
    # ~~admitidos, literales_citados = hashes_citados_por_el_encargo()~~
    #
    # CORRECCION DECLARADA POR ADICION (vuelta 156, TAREA 5, adjudicacion 6.8 del
    # acta 155). LA LINEA VIEJA QUEDA ARRIBA, TACHADA Y LEGIBLE, porque el
    # veredicto de las vueltas 154 y 155 se dio con ella y taparla impediria
    # auditarlo. LO QUE CAMBIA, Y SON LAS DOS COSAS QUE EL ACTA MANDA:
    #   (i)  SOLO ENTRA LO MARCADO: el encargo tiene que traer el rotulo literal
    #        `HASHES ADMITIDOS EN EL CORREDOR DE ESTA VUELTA:` y decir ahi lo
    #        que admite. Un hash citado de paso ya NO entra.
    #   (ii) LA VARA SE FIJA: el encargo se lee DEL COMMIT DEL ACTA de la vuelta
    #        que se comprueba, no del arbol de trabajo, para que el veredicto de
    #        una vuelta ya juzgada no pueda cambiar cuando se escriba un encargo
    #        posterior.
    # UN ENCARGO SIN EL ROTULO ADMITE EL CONJUNTO VACIO, que es lo que la guarda
    # hacia antes de la 6.7: la regla es PROSPECTIVA y ningun veredicto viejo se
    # mueve por ella.
    texto_encargo = texto_del_encargo_en_el_acta(acta)
    admitidos, literales_citados, hay_rotulo = hashes_admitidos_por_el_encargo(
        texto_encargo, fallos=None)
    admitidos_del_corredor = {}
    for nombre in nombres:
        nacido_en = commit_de_nacimiento(nombre, rama, fallos)
        if nacido_en is None:
            continue
        padre_out = _git(["rev-parse", "%s^" % nacido_en], fallos, "padre de %s" % nacido_en)
        padre = padre_out.strip() if padre_out is not None else None
        if padre is None:
            continue
        if padre != acta:
            # EL CORREDOR DE LA PARADA (vuelta 148): el padre puede no ser el
            # acta sin que la apertura se haya medido tarde, y el caso real es
            # el commit con que el fundador contesta una parada. Se mide el
            # corredor en vez de rendirse, y solo se acepta si NADA de lo que
            # toca puede mover una cifra de la apertura.
            if nacido_en not in corredores:
                corredores[nacido_en] = corredor_desde_git(acta, nacido_en, fallos)
            corredor = corredores[nacido_en]
            if corredor is None:
                fallos.append("%s nacio en %s, cuyo padre es %s (no el commit del acta %s) "
                              "y el corredor no se pudo medir" %
                              (nombre, nacido_en[:8], padre[:8], acta[:8]))
            else:
                intrusos, admitidos_aqui = intrusos_del_corredor(corredor, admitidos)
                if admitidos_aqui:
                    admitidos_del_corredor[nacido_en] = admitidos_aqui
                if intrusos:
                    for h, asunto, ajenas in intrusos:
                        fallos.append("%s nacio en %s, y entre el acta %s y ese commit vive %s "
                                      "('%s') que toca %d ruta(s) que NO son papel de parada "
                                      "(%s): la apertura se midio DESPUES de una operacion" %
                                      (nombre, nacido_en[:8], acta[:8], h[:8], asunto[:60],
                                       len(ajenas), ", ".join(ajenas)))
                else:
                    declarados[nacido_en] = corredor

        # TAREA 4 (vuelta 108): el sello fija CONTENIDO, no solo nacimiento.
        iguales, h_nac, h_hoy = contenido_igual_al_nacer(nombre, nacido_en, fallos)
        if iguales is False:
            fallos.append("%s CAMBIO DE CONTENIDO despues de nacer en %s: sha256 de nacimiento "
                          "%s, sha256 de hoy %s" % (nombre, nacido_en[:8], h_nac, h_hoy))

        detalle.append((nombre, nacido_en[:8], padre[:8] if padre else "?", padre == acta))
    return (fallos, detalle, declarados, admitidos_del_corredor, literales_citados,
            hay_rotulo, acta)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, required=True)
    a = ap.parse_args()

    (fallos, detalle, declarados, admitidos_corredor, literales,
     hay_rotulo, acta) = verificar(a.vuelta)
    # LA PUERTA HABLA SIEMPRE, salga verde o rojo (banco 9, fallar ruidoso): se
    # dice DE DONDE se leyo el encargo, SI traia el rotulo y QUE admitio.
    print("PUERTA DEL CORREDOR (adjudicacion 6.8 del acta 155): el encargo se lee del "
          "COMMIT DEL ACTA %s, no del arbol de trabajo." % (acta[:8] if acta else "(no hallado)"))
    print("   rotulo %r en ese encargo: %s" % (ROTULO_ADMITIDOS, "SI" if hay_rotulo else "NO"))
    print("   HASHES ADMITIDOS (solo los MARCADOS, y solo si el rotulo esta): %d (%s)"
          % (len(literales), ", ".join(literales) or "ninguno"))
    if not hay_rotulo:
        print("   SIN ROTULO NO SE ADMITE NADA. Es lo que la guarda hacia antes de la "
              "adjudicacion 6.7 del acta 153, asi que ningun veredicto viejo se mueve.")
    for nacido_en, adms in sorted(admitidos_corredor.items()):
        for h, asunto, ajenas in adms:
            print("   ADMITIDO POR HASH MARCADO EN EL ENCARGO, y se nombra aparte en vez "
                  "de tumbar la guarda: %s ('%s') toca %d ruta(s) fuera de los papeles "
                  "de parada (%s), delante de la apertura nacida en %s"
                  % (h[:8], asunto[:70], len(ajenas), ", ".join(ajenas), nacido_en[:8]))
    if fallos:
        print("ROJO, apertura de la vuelta %d NO sellada antes de la 1.a operacion "
              "(%d cosa(s) no cuadran):" % (a.vuelta, len(fallos)))
        for x in fallos:
            print("   %s" % x)
        return 1

    # La cabecera dice lo que de verdad se midio: "hijo directo del acta" seria
    # FALSO en cuanto hay corredor de parada aceptado (vuelta 148), y una
    # cabecera que miente es justo la especie que esta guarda persigue.
    cola = ("hijo directo del acta" if not declarados
            else "primer commit de la vuelta TRAS el corredor de la parada, declarado abajo")
    print("VERDE: los %d ficheros SALIDA_V%d_*_APERTURA.txt nacieron todos en el "
          "primer commit de la vuelta (%s):" % (len(detalle), a.vuelta, cola))
    for nombre, nacido_en, padre, ok in detalle:
        print("   %s -- nacido en %s, padre %s" % (nombre, nacido_en, padre))
    # EL CORREDOR ACEPTADO NO SE CALLA (vuelta 148): si el padre no era el acta
    # y aun asi la guarda dejo pasar, se dice QUE dejo pasar y por que.
    for nacido_en, corredor in sorted(declarados.items()):
        print("   CORREDOR DE LA PARADA aceptado ante %s: %d commit(s) entre el acta y la "
              "apertura, y ninguno toca nada fuera de los papeles de parada:"
              % (nacido_en[:8], len(corredor)))
        for h, asunto, rutas in corredor:
            print("      %s '%s' -- %d ruta(s): %s" % (h[:8], asunto[:70], len(rutas), ", ".join(rutas)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
