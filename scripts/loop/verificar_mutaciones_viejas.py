# -*- coding: utf-8 -*-
"""verificar_mutaciones_viejas.py . LAS MUTACIONES VIEJAS, EN EL CICLO DE
CIERRE DE CADA VUELTA, Y ANCLA PERDIDA CUENTA COMO ROJO.

LA NOMINA VIVE EN `VIEJAS` Y CRECE: nacio con CUATRO, en la vuelta 140 paso a
CINCO con `vuelta139_2b_mutaciones.py` (cuyo bloque (iii) tenia un ancla movil,
TAREA 2.c, acta 139 caida 4.2) y en la vuelta 142 pasa a SIETE con
`vuelta140_2a_mutaciones.py` y `vuelta141_2_mutaciones.py` (TAREA 2.d; acta 141
caida 4.3: "VIEJAS sigue en cinco y no incluye ni las de la 140 ni las de la
141, cuando su propio docstring dice que una mutacion sin sujeto es ROJO"). La
cifra del rotulo se computa de `VIEJAS`, no se teclea, para que anadir una no
deje una frase mintiendo detras; su prueba de mutacion es
scripts/loop/vuelta142_2d_mutacion_bateria.py, que quita un script de la nomina
EN MEMORIA y exige que la cifra del rotulo baje sola.

CASO DECLARADO (vuelta 142, TAREA 2.d): un exit distinto de cero CONOCIDO,
MEDIDO Y PUBLICADO en su vuelta deja de contarse como NO MORDIO, pero se imprime
con su motivo entero y SOLO si la salida trae su MARCA OBLIGATORIA. Ver
`CASOS_DECLARADOS`. Es lo contrario de una lista de exclusiones: la exencion es
de UN fallo concreto, y el dia que el script falle por otra cosa vuelve a caer
en ROJO.

NOMBRE ESTABLE, SIN NUMERO DE VUELTA, como verificar_apertura_sellada.py y
tallar_cabecera_reporte.py: se corre igual en toda vuelta y no se clona.

POR QUE NACE (encargo de la vuelta 138, TAREA 2.b, ultimo parrafo: "LA GUARDA
PARA QUE NO VUELVA A PASAR: las cuatro mutaciones viejas entran en el ciclo de
cierre de cada vuelta, y a partir de que esten re-ancladas, ANCLA PERDIDA cuenta
como ROJO"). Tres de las cuatro (vuelta135_2e_mutacion_1, _2 y _3) estaban
ancladas a un literal de docs/loop/REPORTE.md, que se sobreescribe cada vuelta:
desde la 135 caian con "ROJO PREVIO" sin llegar a probar nada, y nadie lo
midio hasta la mutacion D de la vuelta 137. La 2.b de la vuelta 138 las
re-anclo a docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md, un sujeto propio y
congelado que ellas mismas cotejan contra el blob del acta 134 en cada corrida.

LA DIFERENCIA CON LA MUTACION D DE LA VUELTA 137, dicha con todas sus letras:
aquella distinguia LA GUARDA NO MORDIO (fallo de verdad) de ANCLA PERDIDA (la
mutacion no llega a correr), y hacia BIEN en distinguirlas, porque entonces las
tres estaban desancladas y contarlo como fallo de la guarda habria sido mentir
en la otra direccion. DESDE QUE ESTAN RE-ANCLADAS ESA DISTINCION SE ACABA: una
mutacion que no encuentra su sujeto es una guarda que no mide, y aqui es ROJO.

QUE COMPRUEBA. Corre las SIETE (la cifra sale de len(VIEJAS)) y exige EXIT 0 de
cada una, salvo los CASOS DECLARADOS de arriba. Clasifica:
  OK             . exit 0, la mutacion corrio y mordio.
  ANCLA PERDIDA  . la salida trae "ROJO PREVIO": el sujeto no esta o no es el
                   que la mutacion espera. ROJO.
  NO MORDIO      . exit distinto de 0 sin "ROJO PREVIO": la guarda que la
                   mutacion prueba dejo de morder. ROJO.
  CASO DECLARADO . (TAREA 2.d, vuelta 142) exit distinto de 0 QUE COINCIDE con el
                   declarado en CASOS_DECLARADOS Y cuya salida trae la marca
                   obligatoria de esa entrada. NO es rojo, y se imprime con su
                   motivo entero para que se vea.
  NO REPRODUCIBLE. (TAREA 2.f, vuelta 141) la mutacion se corre DOS VECES
                   seguidas y alguna de las salidas selladas que escribe sale
                   DISTINTA entre las dos. ROJO, nombrando el fichero y la
                   primera linea que cambia. Una salida sellada que no se
                   repite no prueba nada.

PRUEBA DE MUTACION (EJECUTOR regla 1, sobre una variable QUE EL CODIGO COMPUTA):
--mutar-ancla fabrica una copia del sujeto fijo CON EL ANCLA ARRANCADA en un
directorio temporal, apunta alli las tres re-ancladas con --sujeto, y exige que
las tres salgan clasificadas como ANCLA PERDIDA y que el veredicto sea ROJO. La
variable del veredicto es la lista `perdidas`, construida leyendo la salida real
de cada proceso; no hay ningun literal comparado consigo mismo. P.16, QUIEN
FABRICA LIMPIA: la copia temporal se retira siempre.

USO:
  python scripts/loop/verificar_mutaciones_viejas.py
  python scripts/loop/verificar_mutaciones_viejas.py --mutar-ancla
  python scripts/loop/verificar_mutaciones_viejas.py --mutar-reproducibilidad
"""
import argparse
import hashlib
import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
DOCS_LOOP = os.path.join(RAIZ, "docs", "loop")
SUJETO_FIJO = os.path.join(DOCS_LOOP, "SUJETO_FIJO_V135_2E_REPORTE_134.md")

# Las CUATRO. La primera fabrica su propio reporte y nunca estuvo anclada a
# REPORTE.md, por eso no admite --sujeto y no entra en la prueba del ancla.
VIEJAS = [
    ("vuelta133_tarea2e_mutacion_cifras.py", False),
    ("vuelta135_2e_mutacion_1.py", True),
    ("vuelta135_2e_mutacion_2.py", True),
    ("vuelta135_2e_mutacion_3.py", True),
    # QUINTA, ANADIDA EN LA VUELTA 140 (TAREA 2.c, acta 139 caida 4.2). Su
    # bloque (iii) tenia un ANCLA MOVIL (`git log -1 -- REPORTE.md`) y la
    # reparacion la clava por hash con su sha256. Entra en esta bateria
    # justamente para que, SI EL ANCLA SE VUELVE A PERDER, salga como ANCLA
    # PERDIDA y no como verde. No admite --sujeto: fabrica los suyos.
    ("vuelta139_2b_mutaciones.py", False),
    # SEXTA Y SEPTIMA, ANADIDAS EN LA VUELTA 142 (TAREA 2.d; acta 141, caida
    # 4.3 de la casa: "VIEJAS sigue en cinco y no incluye ni las de la 140 ni
    # las de la 141, cuando su propio docstring dice que una mutacion sin
    # sujeto es ROJO"). Ninguna admite --sujeto: las dos fabrican los suyos EN
    # MEMORIA. La cifra del rotulo se sigue computando de len(VIEJAS).
    ("vuelta140_2a_mutaciones.py", False),
    ("vuelta141_2_mutaciones.py", False),
]

# CASOS DECLARADOS: exit distinto de 0 QUE NO ES UN FALLO DE LA GUARDA, con su
# motivo escrito y su fecha. Se separan de NO MORDIO porque son cosas
# CONOCIDAS, MEDIDAS Y PUBLICADAS en su vuelta, no sorpresas; pero NO se
# esconden: la bateria los imprime uno a uno con su motivo entero, y si alguno
# dejara de dar su codigo declarado, vuelve a caer como NO MORDIO.
#
# EL LIMITE, DICHO PARA QUE NO SE ABUSE: aqui SOLO entra un caso cuyo diagnostico
# esta escrito y medido en su acta o su reporte. Un rojo sin acta detras no se
# declara: se arregla o se trae como PARADA.
#
# CADA ENTRADA ES (exit_declarado, motivo, MARCA_OBLIGATORIA). La exencion solo
# vale si la salida del script TRAE ESA MARCA: si el script empieza a fallar por
# OTRA razon, la marca no aparece y vuelve a caer como NO MORDIO. La exencion es
# de UN fallo concreto, nunca del script.
CASOS_DECLARADOS = {
    "vuelta140_2a_mutaciones.py": (
        2,
        "su bloque (iii), el caso positivo sobre la fase 05, sale NO CALZA y esta "
        "DECLARADO desde la vuelta 140: el auditor lo reconocio como caida SUYA de "
        "encargo (acta 140, 4.5, 'EL AUDITOR ELIGIO MAL EL SUJETO CONGELADO'). "
        "OP-S-05, OP-S-08, OP-S-11 y OP-S-12 tienen HUELLA DE GRAFO IDENTICA (los "
        "cuatro campos vacios) y lo unico que las separa es `estado`, que el encargo "
        "prohibe mirar: NINGUNA VARA DE GRAFO PUEDE SEPARARLAS. Los bloques (i) y "
        "(ii) SI muerden y son los que esta bateria vigila.",
        "VEREDICTO (iii): NO CALZA"),
    "vuelta135_2e_mutacion_3.py": (
        1,
        "su SUJETO FIJO es el REPORTE.md de la vuelta 134, congelado por banco 9.10, y "
        "ES ANTERIOR A LOS DELIMITADORES DE CABECERA TALLADA. Medido en esta vuelta: "
        "grep -c 'CABECERA TALLADA' docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md da 0, y "
        "sobre docs/loop/REPORTE.md da 3. La ampliacion del vocabulario de la TAREA 2.a "
        "(vuelta 142) hace que la guarda vea ahora la celda '3 fila(s)' del desfase del "
        "calibrado, que EN UN REPORTE MODERNO vive DENTRO de la cabecera delimitada y "
        "queda recortada antes de parsear, y en este sujeto no, porque las marcas no "
        "existian aun. LAS DOS CIFRAS QUE ESTA MUTACION PRUEBA SI COTEJAN (la salida "
        "publica '2 POR ETIQUETA'): lo que cae es una tercera, ajena al caso. El sujeto "
        "NO se retoca, porque su valor es estar congelado.",
        "NO TIENE CONVENCION MECANICA DE CONTEO"),
}

# EL ANCLA QUE SE ARRANCA en --mutar-ancla. Es el literal que las tres buscan.
ANCLAS = ["118 grafias (sin instrumento)", "54 grupos (sin instrumento)"]


# EL CORTACIRCUITOS (vuelta 140, 2.c). Ver el docstring: `vuelta139_2b_mutaciones.py`
# corre esta bateria dentro de su bloque (ii), y esta bateria corre ese script
# desde la vuelta 140. Sin esta marca los dos se llaman sin fondo. Es ruidosa:
# el hijo DICE en su salida que omite el sub-caso por recursion.
MARCA_RECURSION = "LOOP_BATERIA_EN_CURSO"


def correr(script, sujeto=None, base=None):
    cmd = [sys.executable, os.path.join(base or LOOP, script)]
    if sujeto:
        cmd += ["--sujeto", sujeto]
    entorno = dict(os.environ)
    entorno[MARCA_RECURSION] = "1"
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=RAIZ, env=entorno)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


# ------------- LA SALIDA SELLADA TIENE QUE REPETIRSE (TAREA 2.f, vuelta 141)
#
# POR QUE NACE (acta de la vuelta 140, caida 4.2 del ejecutor). El auditor
# corrio esta bateria y `docs/loop/SALIDA_V135_2E_MUTACION_3.txt`, que es una
# SALIDA SELLADA y commiteada, CAMBIO SOLO: traia el nombre de un fichero
# temporal con sufijo aleatorio (`REPORTE_134_MUTACION3_xffen9vd.md` paso a
# `_xv7o8hyj`). Una salida sellada que no se repite no prueba nada, y esta
# bateria la daba por VERDE porque solo miraba el exit code.
#
# QUE COMPRUEBA DE MAS: cada mutacion vieja se corre DOS VECES SEGUIDAS y se
# comparan los ficheros que ESCRIBE. Los ficheros escritos NO SE TECLEAN: se
# computan mirando cuales cambiaron de sha256 respecto del estado de partida.
# Si alguno difiere entre la primera y la segunda corrida, es ROJO nombrandolo
# y nombrando la primera linea que difiere.


def estado_de(directorio):
    """Por cada .txt del directorio, (mtime_ns, sha256 NORMALIZADO).

    EL FICHERO ESCRITO SE DETECTA POR mtime, NO POR HASH, y el motivo importa:
    una salida sellada que se reescribe con el MISMO contenido no cambia de
    hash, y detectarla por hash la dejaria fuera de la lista de "las que
    escribe". Eso convertiria la lista en una que solo ve los ficheros rotos,
    justo al reves de lo que hace falta. El hash se guarda al lado, que es lo
    que decide si es reproducible.

    El sha256 va NORMALIZADO (CRLF y CR sueltos a LF): este repo tiene
    core.autocrlf=true y la convencion de fin de linea del sistema operativo no
    es un cambio de contenido."""
    salida = {}
    for nombre in sorted(os.listdir(directorio)):
        if not nombre.endswith(".txt"):
            continue
        ruta = os.path.join(directorio, nombre)
        if not os.path.isfile(ruta):
            continue
        with io.open(ruta, "rb") as f:
            datos = f.read().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        salida[nombre] = (os.stat(ruta).st_mtime_ns, hashlib.sha256(datos).hexdigest())
    return salida


def primera_linea_distinta(ruta_a_texto_1, ruta_a_texto_2):
    a = ruta_a_texto_1.splitlines()
    b = ruta_a_texto_2.splitlines()
    for i in range(max(len(a), len(b))):
        la = a[i] if i < len(a) else "(no hay linea)"
        lb = b[i] if i < len(b) else "(no hay linea)"
        if la != lb:
            return i + 1, la[:160], lb[:160]
    return None, None, None


def correr_dos_veces(script, directorio, sujeto=None, base=None):
    """Devuelve (codigo, salida, escritos, inestables). Las dos listas se
    COMPUTAN del directorio, nunca se teclean: `escritos` son los .txt cuyo
    mtime se movio en la primera corrida, `inestables` los que cambiaron de
    CONTENIDO entre la primera y la segunda."""
    antes = estado_de(directorio)
    codigo, salida = correr(script, sujeto, base)
    tras1 = estado_de(directorio)
    escritos, textos1 = [], {}
    for n, (mt, _sha) in sorted(tras1.items()):
        if n not in antes or antes[n][0] != mt:
            escritos.append(n)
            with io.open(os.path.join(directorio, n), encoding="utf-8", errors="replace") as f:
                textos1[n] = f.read()
    correr(script, sujeto, base)
    tras2 = estado_de(directorio)
    inestables = []
    for n in sorted(set(tras1) | set(tras2)):
        sha1 = tras1.get(n, (None, None))[1]
        sha2 = tras2.get(n, (None, None))[1]
        if sha1 == sha2:
            continue
        texto2 = ""
        ruta = os.path.join(directorio, n)
        if os.path.isfile(ruta):
            with io.open(ruta, encoding="utf-8", errors="replace") as f:
                texto2 = f.read()
        num, la, lb = primera_linea_distinta(textos1.get(n, ""), texto2)
        inestables.append((n, num, la, lb))
    return codigo, salida, escritos, inestables


def clasificar(codigo, salida):
    if codigo == 0:
        return "OK"
    if "ROJO PREVIO" in salida:
        return "ANCLA PERDIDA"
    return "NO MORDIO"


def primera_linea_util(salida):
    for l in salida.splitlines():
        if l.strip():
            return l.strip()[:150]
    return "(sin salida)"


# LA PRUEBA DE MUTACION DEL COTEJO DE REPRODUCIBILIDAD (TAREA 2.f, vuelta 141).
# Fabrica DOS scripts de mentira en un directorio temporal: uno que escribe una
# salida con un valor ALEATORIO dentro y otro que escribe una salida FIJA. El
# cotejo tiene que marcar el primero como inestable y el segundo como estable.
# Ninguno de los dos toca docs/loop: escriben en el mismo directorio temporal,
# que es el que se vigila. P.16, QUIEN FABRICA LIMPIA.
SCRIPT_INESTABLE = r"""# -*- coding: utf-8 -*-
import io, os, uuid
d = os.path.dirname(os.path.abspath(__file__))
io.open(os.path.join(d, "SALIDA_DE_MENTIRA.txt"), "w", encoding="utf-8", newline="\n").write(
    "linea estable\nsufijo aleatorio: %s\n" % uuid.uuid4().hex)
"""

SCRIPT_ESTABLE = r"""# -*- coding: utf-8 -*-
import io, os
d = os.path.dirname(os.path.abspath(__file__))
io.open(os.path.join(d, "SALIDA_DE_MENTIRA.txt"), "w", encoding="utf-8", newline="\n").write(
    "linea estable\nsufijo fijo: siempre el mismo\n")
"""


def prueba_de_reproducibilidad():
    """Devuelve el exit code. Cada comprobacion compara una variable COMPUTADA
    por correr_dos_veces (la lista `inestables`), nunca un literal."""
    print("=" * 78)
    print("PRUEBA DE MUTACION DEL COTEJO DE REPRODUCIBILIDAD (TAREA 2.f, vuelta 141)")
    print("=" * 78)
    tmp = tempfile.mkdtemp(prefix="v141_2f_")
    resultados = []
    try:
        for nombre, fuente, esperado_inestable in (
                ("script_inestable.py", SCRIPT_INESTABLE, True),
                ("script_estable.py", SCRIPT_ESTABLE, False)):
            io.open(os.path.join(tmp, nombre), "w", encoding="utf-8").write(fuente)
            _c, _s, escritos, inestables = correr_dos_veces(nombre, tmp, base=tmp)
            hay = bool(inestables)
            ok = (hay == esperado_inestable)
            resultados.append((nombre, hay, esperado_inestable, ok))
            print("  %-22s escribe %s | inestable=%s (esperado %s)  %s"
                  % (nombre, ", ".join(escritos) or "nada", hay, esperado_inestable,
                     "VERDE" if ok else "ROJO"))
            for n, num, la, lb in inestables:
                print("       %s, linea %s" % (n, num))
                print("          corrida 1: %s" % la)
                print("          corrida 2: %s" % lb)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print("  P.16: el directorio temporal se retira. Existe todavia: %s" % os.path.exists(tmp))

    print("")
    print("  Y AHORA SE MUTA EL ESPERADO DE CADA UNA y se re-evalua contra el MISMO")
    print("  valor obtenido: la que siga verde no puede fallar nunca.")
    no_caen = [n for n, hay, esp, _ok in resultados if hay == (not esp)]
    print("  comprobaciones: %d | verdes: %d | caen con el esperado mutado: %d"
          % (len(resultados), sum(1 for r in resultados if r[3]),
             len(resultados) - len(no_caen)))
    for n in no_caen:
        print("     NO CAE con el esperado mutado: %s" % n)
    print("")
    if all(r[3] for r in resultados) and not no_caen:
        print("VERDE DE LA MUTACION: el cotejo marca la salida aleatoria como NO")
        print("REPRODUCIBLE y deja pasar la fija, y las dos comprobaciones caen al")
        print("mutarles el esperado.")
        print("FIN")
        return 0
    print("ROJO DE LA MUTACION: el cotejo de reproducibilidad no se comporta.")
    print("FIN")
    return 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutar-ancla", dest="mutar", action="store_true")
    ap.add_argument("--mutar-reproducibilidad", dest="mutar_repro", action="store_true",
                    help="TAREA 2.f (vuelta 141): prueba de mutacion del cotejo de "
                         "reproducibilidad, sobre dos scripts de mentira fabricados")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    if a.mutar_repro:
        return prueba_de_reproducibilidad()

    print("=" * 78)
    print("LAS %d MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO." % len(VIEJAS))
    if a.mutar:
        print("MODO MUTACION: sujeto con el ancla arrancada. TIENE QUE DAR ROJO.")
    print("=" * 78)

    sujeto = None
    tmp = None
    try:
        if a.mutar:
            if not os.path.exists(SUJETO_FIJO):
                print("ROJO: no existe el sujeto fijo %s." % SUJETO_FIJO)
                return 1
            tmp = tempfile.mkdtemp(prefix="ancla_arrancada_")
            texto = io.open(SUJETO_FIJO, encoding="utf-8").read()
            arrancadas = 0
            for ancla in ANCLAS:
                if ancla in texto:
                    texto = texto.replace(ancla, "CIFRA ARRANCADA POR LA PRUEBA DE MUTACION")
                    arrancadas += 1
            print("  anclas arrancadas de la copia: %d de %d" % (arrancadas, len(ANCLAS)))
            if arrancadas != len(ANCLAS):
                print("ROJO: el sujeto fijo no traia las %d anclas. PARADA." % len(ANCLAS))
                return 1
            sujeto = os.path.join(tmp, "SUJETO_CON_EL_ANCLA_ARRANCADA.md")
            io.open(sujeto, "w", encoding="utf-8", newline="\n").write(texto)
            print("  copia con el ancla arrancada: %s" % sujeto)

        filas = []
        inestables_todas = []
        for script, admite_sujeto in VIEJAS:
            usar = sujeto if (a.mutar and admite_sujeto) else None
            if a.mutar:
                # En modo mutacion el sujeto es una copia con el ancla arrancada:
                # lo que se prueba es el ANCLA, no la reproducibilidad.
                codigo, salida = correr(script, usar)
                escritos, inestables = [], []
            else:
                codigo, salida, escritos, inestables = correr_dos_veces(script, DOCS_LOOP, usar)
            estado = clasificar(codigo, salida)
            # CASO DECLARADO (TAREA 2.d, vuelta 142): un exit conocido, medido y
            # publicado en su vuelta deja de contarse como NO MORDIO, PERO SE
            # IMPRIME CON SU MOTIVO ENTERO. Si el codigo deja de ser el
            # declarado, vuelve a caer como NO MORDIO: la exencion es de UN
            # codigo concreto, no del script.
            declarado = CASOS_DECLARADOS.get(script)
            if (declarado and codigo == declarado[0] and estado == "NO MORDIO"
                    and declarado[2] in salida):
                estado = "CASO DECLARADO"
            if inestables:
                estado = "NO REPRODUCIBLE"
                for nombre, num, la, lb in inestables:
                    inestables_todas.append((script, nombre, num, la, lb))
            filas.append((script, codigo, estado, primera_linea_util(salida), escritos))
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)
            print("  P.16: la copia temporal se retira. Existe todavia: %s" % os.path.exists(tmp))

    print("")
    for script, codigo, estado, prim, escritos in filas:
        print("  %-38s exit %d  %-16s" % (script, codigo, estado))
        if not a.mutar:
            print("      salidas selladas que escribe (computadas, no tecleadas): %s"
                  % (", ".join(escritos) or "ninguna"))
        if estado not in ("OK",):
            print("      %s" % prim)

    perdidas = [s for s, _, e, _, _ in filas if e == "ANCLA PERDIDA"]
    no_mordio = [s for s, _, e, _, _ in filas if e == "NO MORDIO"]
    no_reprod = [s for s, _, e, _, _ in filas if e == "NO REPRODUCIBLE"]
    print("")
    print("  ANCLA PERDIDA  : %d (%s)" % (len(perdidas), ", ".join(perdidas) or "ninguna"))
    print("  NO MORDIO      : %d (%s)" % (len(no_mordio), ", ".join(no_mordio) or "ninguna"))
    print("  NO REPRODUCIBLE: %d (%s)" % (len(no_reprod), ", ".join(no_reprod) or "ninguna"))
    declarados = [s for s, _, e, _, _ in filas if e == "CASO DECLARADO"]
    print("  CASO DECLARADO : %d (%s)" % (len(declarados), ", ".join(declarados) or "ninguna"))
    for s in declarados:
        print("      %s, exit declarado %d, marca obligatoria %r:"
              % (s, CASOS_DECLARADOS[s][0], CASOS_DECLARADOS[s][2]))
        print("         %s" % CASOS_DECLARADOS[s][1])
    for script, nombre, num, la, lb in inestables_todas:
        print("      %s: %s cambia SOLO entre dos corridas, linea %s" % (script, nombre, num))
        print("         corrida 1: %s" % la)
        print("         corrida 2: %s" % lb)

    if a.mutar:
        esperadas = [s for s, admite in VIEJAS if admite]
        bien = sorted(perdidas) == sorted(esperadas)
        print("")
        if bien:
            print("VERDE DE LA MUTACION: las %d re-ancladas caen como ANCLA PERDIDA cuando se"
                  % len(esperadas))
            print("les arranca el ancla, y el veredicto de esta guarda seria ROJO.")
            print("FIN")
            return 0
        print("ROJO DE LA MUTACION: se esperaban %d ANCLA PERDIDA (%s) y salieron %d (%s)."
              % (len(esperadas), ", ".join(esperadas), len(perdidas), ", ".join(perdidas)))
        print("FIN")
        return 1

    if perdidas or no_mordio or no_reprod:
        print("")
        print("ROJO: %d con el ancla perdida, %d que no mordieron y %d cuya salida "
              "sellada NO SE REPITE." % (len(perdidas), len(no_mordio), len(no_reprod)))
        print("FIN")
        return 1
    print("")
    print("VERDE: las %d mutaciones viejas corren, muerden, y sus salidas selladas "
          "salen IDENTICAS en dos corridas seguidas." % len(filas))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
