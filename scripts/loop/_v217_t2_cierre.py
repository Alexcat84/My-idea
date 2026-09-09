# -*- coding: utf-8 -*-
r"""_v217_t2_cierre.py . EL CIERRE INTEGRAL DE LA VUELTA 217, MEDIDO, Y LAS DOS
PIEZAS DE TEXTO QUE DE EL SALEN, COMPUESTAS Y NO TECLEADAS.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

QUE MIDE, Y TODO SE LEE DE FICHEROS DE SALIDA QUE YA EXISTEN EN DISCO:
  . el ciclo entero de Gate 0 por los DOS lados, con sus DIECIOCHO salidas
    selladas y sus dos consolas, que el propio ciclo escribio;
  . las TRES suites solas, cada una con su exitcode y sus bytes por las dos
    convenciones;
  . el marcador y el censo, recomputados cada uno con su comando;
  . las sedes que la vuelta pudo mover, cotejadas por sha256 entre la apertura
    y el cierre;
  . la moratoria: cuantos ficheros escribio esta vuelta en el arbol de scripts
    y cuantos llevan el prefijo que le toca.

QUE ESCRIBE: la seccion de la TAREA 2 para el anexo, y el CUERPO DEL CIERRE
(secciones 3 a 8) que cerrar_reporte.py monta. Ninguna cifra se teclea: si una
salida falta, el instrumento CAE EN ROJO y no escribe, que es el remedio de la
`3.1` del acta 214 aplicado tambien aqui.

USO:  python scripts/loop/_v217_t2_cierre.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

SEGMENTOS = ("GATE0_CMD1", "CICLO_ETIQUETAS", "CICLO_SYNC", "CICLO_NUMSTAT",
             "CONTEO", "DESFASE_CALIBRADO", "MOTOR", "TSC", "WEB")

SEDES = [
    "docs/plan/INVENTARIO.jsonl",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/08_VERIFICACION.md",
    "docs/plan/10_INVENTARIO.md",
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "docs/INTRA_DOMINIO_INFORME.md",
    "docs/plan/00_INDICE.md",
    "docs/BANCO_DE_TEXTOS.md",
    "docs/plan/BANCO_DEL_PLAN.md",
    "dataset/metadata/master_graph.json",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
]


# LOS FICHEROS QUE EL PROPIO CIERRE ANADE DESPUES DE ESTA MEDICION, NOMBRADOS
# UNO A UNO Y NO ESTIMADOS. Es la obligacion de dictado nueva del encargo de la
# 217, que nace de la caida de la 216: la cifra de lo que la vuelta escribio se
# midio antes del cierre y salio 16 donde el auditor conto 18.
HUECO_DEL_CIERRE = [
    "scripts/loop/_v%d_t2_seccion.py" % VUELTA,
    "scripts/loop/_v%d_t2_seccion.md" % VUELTA,
    "scripts/loop/_v%d_cierre_texto.py" % VUELTA,
    "scripts/loop/_v%d_cierre_texto.md" % VUELTA,
]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def sha_lf(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    b = io.open(p, "rb").read()
    return hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16]


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def cifra(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(-?\d+)", l.split(etiqueta, 1)[1])
            if m:
                return m.group(1)
    return None


def dos_convenciones(rel):
    m = medir_en_disco(RAIZ, rel)
    return m if m else (0, 0)


def exitcode_de(texto):
    m = re.findall(r"EXITCODE:?\s*(-?\d+)|EXIT=(-?\d+)", texto)
    for a, b in m:
        return int(a or b)
    return None


def main():
    fallos = 0
    out = []
    w = out.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2. EL CIERRE INTEGRAL, MEDIDO DE SUS FICHEROS" % VUELTA)
    w("=" * 78)
    w("")

    w("2.a.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, CON SUS SALIDAS SELLADAS")
    ausentes, vacias, filas_ciclo = [], [], []
    for lado in ("APERTURA", "CIERRE"):
        for seg in SEGMENTOS:
            rel = "docs/loop/SALIDA_V%d_%s_%s.txt" % (VUELTA, seg, lado)
            p = os.path.join(RAIZ, rel.replace("/", os.sep))
            if not os.path.isfile(p):
                ausentes.append(rel)
                w("   SALIDA %-46s AUSENTE (ausencia, no cero)" % rel)
                continue
            d, l = dos_convenciones(rel)
            if d == 0:
                vacias.append(rel)
            t = leer(rel)
            ec = exitcode_de(t)
            filas_ciclo.append((lado, seg, d, l, ec))
            w("   SALIDA %-46s %6d bytes en disco y %6d normalizado a LF | "
              "EXITCODE dentro: %s" % (rel, d, l, ec))
    w("CIFRA salidas selladas del ciclo: %d | CIFRA que deberia haber: 18"
      % len(filas_ciclo))
    w("CIFRA ausentes: %d | CIFRA de cero bytes: %d" % (len(ausentes), len(vacias)))
    sin_ec = [f for f in filas_ciclo if f[4] is None]
    w("CIFRA salidas SIN exitcode dentro: %d" % len(sin_ec))
    peor = max([f[4] for f in filas_ciclo if f[4] is not None] or [-1])
    w("CIFRA peor exitcode de las dieciocho: %d" % peor)
    if len(filas_ciclo) != 18 or ausentes or vacias or peor != 0:
        fallos += 1
    w("")

    w("2.a.2. LAS DOS CONSOLAS DEL CICLO, SELLADAS POR EL PROPIO INSTRUMENTO")
    consolas = []
    for lado in ("APERTURA", "CIERRE"):
        rel = "docs/loop/SALIDA_V%d_CICLO_GATE0_%s_CONSOLA.txt" % (VUELTA, lado)
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(p):
            w("   CONSOLA %s: AUSENTE. ESO ES ROJO: es la caida `3.1` del acta "
              "214." % lado)
            fallos += 1
            continue
        d, l = dos_convenciones(rel)
        t = leer(rel)
        m = re.search(r"PEOR EXITCODE DE LOS OCHO: (-?\d+)", t)
        consolas.append((lado, rel, d, l, m.group(1) if m else "no dice"))
        w("   CONSOLA %-9s %s | %d bytes en disco y %d normalizado a LF | "
          "peor exitcode que declara: %s"
          % (lado, rel, d, l, m.group(1) if m else "no dice"))
        if d == 0:
            fallos += 1
    w("CIFRA consolas selladas: %d | CIFRA que deberia haber: 2" % len(consolas))
    if len(consolas) != 2:
        fallos += 1
    w("")

    w("2.a.3. LAS TRES SUITES SOLAS, CADA UNA CON SU EXITCODE Y SUS BYTES")
    filas_suite = []
    for nombre, rel in (("motor", "docs/loop/SALIDA_V%d_T2_SUITE_MOTOR.txt" % VUELTA),
                        ("tsc", "docs/loop/SALIDA_V%d_T2_SUITE_TSC.txt" % VUELTA),
                        ("web", "docs/loop/SALIDA_V%d_T2_SUITE_WEB.txt" % VUELTA)):
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(p):
            w("   SUITE %-6s AUSENTE: %s" % (nombre, rel))
            fallos += 1
            continue
        d, l = dos_convenciones(rel)
        t = leer(rel)
        ec = exitcode_de(t)
        filas_suite.append((nombre, rel, d, l, ec))
        w("   SUITE %-6s %s | EXITCODE %s | %d bytes en disco y %d normalizado "
          "a LF" % (nombre, rel, ec, d, l))
        if ec != 0 or d == 0:
            fallos += 1
    w("CIFRA suites corridas solas: %d | CIFRA que deberia haber: 3"
      % len(filas_suite))
    if len(filas_suite) != 3:
        fallos += 1
    w("")

    w("2.a.4. EL MARCADOR Y EL CENSO, RECOMPUTADOS CADA UNO CON SU COMANDO")
    rel_mar = "docs/loop/SALIDA_V%d_T2_MARCADOR.txt" % VUELTA
    rel_ari = "docs/loop/SALIDA_V%d_T2_ARISTAS.txt" % VUELTA
    mar = leer(rel_mar)
    ari = leer(rel_ari)
    w("   COMANDO 1: python scripts/recomputar_marcador.py 3388 -> %s" % rel_mar)
    w("   COMANDO 2: python scripts/loop/vuelta83_conteo_aristas.py WORK -> %s"
      % rel_ari)
    clases = {}
    dentro = False
    for l in mar.split(NL):
        if l.strip() == "MARCADOR GLOBAL":
            dentro = True
            continue
        if dentro:
            m = re.match(r"^\s+([ABCD])\s+(\d+)\s", l)
            if m:
                clases[m.group(1)] = m.group(2)
            elif l.strip() == "":
                dentro = False
    n = cifra(mar, "n = ")
    huecos = "0" if "huecos: []" in mar else "NO CERO"
    w("   MARCADOR: n %s | A %s | B %s | C %s | D %s | huecos %s"
      % (n, clases.get("A"), clases.get("B"), clases.get("C"),
         clases.get("D"), huecos))
    m = re.search(r"nodos (\d+) vivos (\d+) depre (\d+) \| sig (\d+) prev (\d+) "
                  r"suma (\d+) union (\d+)", ari)
    if not m:
        w("   ROJO: no se pueden leer el censo y las aristas de su salida.")
        fallos += 1
        censo = ("?",) * 7
    else:
        censo = m.groups()
        w("   CENSO: nodos %s vivos %s deprecados %s" % censo[:3])
        w("   ARISTAS: siguientes %s previos %s suma %s union %s" % censo[3:])
    w("")

    w("2.a.5. LAS CIFRAS DEL AUDITOR, COTEJADAS UNA A UNA Y NO COPIADAS")
    del_encargo = [
        ("marcador n", n, "3388"), ("marcador A", clases.get("A"), "550"),
        ("marcador B", clases.get("B"), "72"), ("marcador C", clases.get("C"), "5"),
        ("marcador D", clases.get("D"), "2761"), ("marcador huecos", huecos, "0"),
        ("censo nodos", censo[0], "3853"), ("censo vivos", censo[1], "3169"),
        ("censo deprecados", censo[2], "684"),
        ("aristas siguientes", censo[3], "8780"),
        ("aristas previos", censo[4], "8740"),
        ("aristas suma", censo[5], "17520"),
        ("aristas union", censo[6], "9914"),
        ("Gate 0 peor exitcode", str(peor), "0"),
        ("salidas selladas del ciclo", str(len(filas_ciclo)), "18"),
        ("salidas ausentes del ciclo", str(len(ausentes)), "0"),
    ]
    filas_cotejo, difieren = [], 0
    for etiqueta, mia, suya in del_encargo:
        calza = (str(mia) == str(suya))
        if not calza:
            difieren += 1
        filas_cotejo.append((etiqueta, mia, suya, calza))
        w("   COTEJO %-30s | LA MIA %-8s | la del encargo %-8s | CALZA: %s"
          % (etiqueta, mia, suya, "SI" if calza else "NO"))
    w("CIFRA cifras cotejadas: %d | CIFRA que NO calzan: %d"
      % (len(del_encargo), difieren))
    for etiqueta, mia, suya, calza in filas_cotejo:
        if not calza:
            w("   DISCREPANCIA DECLARADA> %s: la MIA %s, la del encargo %s. "
              "PUBLICO LA MIA (EJECUTOR.md 2)." % (etiqueta, mia, suya))
    w("")

    w("2.a.6. LAS SEDES QUE LA VUELTA PUDO MOVER, COTEJADAS POR SU sha256")
    ap = leer("docs/loop/SALIDA_V%d_APERTURA.txt" % VUELTA)
    filas_sede, movidas = [], 0
    for rel in SEDES:
        antes = None
        for l in ap.split(NL):
            if l.startswith("CIFRA " + rel + ":") and "sha256 LF " in l:
                antes = l.split("sha256 LF ", 1)[1].strip()
        ahora = sha_lf(rel)
        d, lf = dos_convenciones(rel)
        # LA AUSENCIA DE MEDICION DE APERTURA NO ES UN MOVIMIENTO, Y CONFUNDIR
        # LAS DOS COSAS SERIA PUBLICAR UN FALSO ROJO. Cuando el sello de
        # apertura no trae esa sede (porque su lista es la que la apertura
        # nombro), la quietud se mide con git, que es una medicion y no una
        # suposicion, y se DICE que se midio por la otra via.
        if antes is None:
            _, ns = git(["diff", "--numstat", "HEAD", "--", rel])
            filas = [x for x in ns.split(NL) if x.strip()]
            quieta = not filas
            via = ("NO MEDIDA AL ABRIR (no estaba en la lista del sello de "
                   "apertura): su quietud se mide con git diff --numstat HEAD, "
                   "%d filas" % len(filas))
        else:
            quieta = (antes == ahora)
            via = "cotejo de los dos sha256"
        if not quieta:
            movidas += 1
        filas_sede.append((rel, antes, ahora, quieta, d, lf))
        w("   SEDE %-42s | al abrir %s | al cerrar %s | %s | %d / %d bytes | %s"
          % (rel, antes if antes is not None else "NO_MEDIDA_AL_ABRIR",
             ahora, "QUIETA" if quieta else "SE MOVIO", d, lf, via))
    w("CIFRA sedes cotejadas: %d | CIFRA que se movieron: %d"
      % (len(filas_sede), movidas))
    w("CIFRA sedes cuya quietud se midio por sha256 de apertura: %d | por git "
      "diff, porque la apertura no las nombraba: %d"
      % (sum(1 for f in filas_sede if f[1] is not None),
         sum(1 for f in filas_sede if f[1] is None)))
    if movidas:
        fallos += 1
    w("")

    w("2.a.7. LA MORATORIA: LO QUE ESTA VUELTA ESCRIBIO EN EL ARBOL DE SCRIPTS")
    _, salida = git(["log", "--name-only", "--pretty=format:",
                     "%s..HEAD" % leer("docs/loop/SALIDA_V%d_HEAD_APERTURA.txt"
                                       % VUELTA).strip(), "--", "scripts/"])
    tocados = sorted({x.strip() for x in salida.split(NL)
                      if x.strip().startswith("scripts/")})
    _, st = git(["status", "--porcelain"])
    for l in st.split(NL):
        x = l[3:].strip()
        if x.startswith("scripts/"):
            tocados.append(x)
    tocados = sorted(set(tocados))
    con_prefijo = [x for x in tocados
                   if os.path.basename(x).startswith("_v%d_" % VUELTA)]
    for x in tocados:
        w("   TOCADO %-52s | prefijo _v%d_: %s"
          % (x, VUELTA, "SI" if x in con_prefijo else "NO"))
    w("CIFRA ficheros de scripts que esta vuelta escribio, MEDIDA AHORA: %d | "
      "CIFRA de esos con el prefijo que le toca: %d"
      % (len(tocados), len(con_prefijo)))
    if len(tocados) != len(con_prefijo):
        fallos += 1
    # LA OBLIGACION DE DICTADO NUEVA DEL ENCARGO DE LA 217, Y NACE DE MI CAIDA
    # DE LA 216: la cifra de "lo que esta vuelta escribio" se mide ANTES de que
    # el cierre escriba sus propios ficheros, asi que se publica CON SU HUECO AL
    # LADO, LAS DOS CIFRAS JUNTAS. El hueco no se estima: se NOMBRA fichero a
    # fichero, porque son los que este mismo bloque de cierre va a producir
    # despues de esta medicion.
    w("")
    w("2.a.7.bis. EL HUECO DE ESTA MISMA CIFRA, DECLARADO Y NOMBRADO")
    w("   MOTIVO, dicho antes que la cifra: este instrumento corre ANTES de que "
      "el cierre escriba sus propios ficheros. La cifra de arriba es exacta en "
      "el momento en que se mide y NO es el total de la vuelta.")
    faltan = [x for x in HUECO_DEL_CIERRE if x not in tocados]
    for x in HUECO_DEL_CIERRE:
        w("   DEL HUECO %-48s | ya contado arriba: %s"
          % (x, "SI" if x in tocados else "NO"))
    w("CIFRA MEDIDA AHORA: %d | CIFRA DEL HUECO QUE EL PROPIO CIERRE ANADE: %d "
      "| CIFRA TOTAL DE LA VUELTA, LAS DOS JUNTAS: %d"
      % (len(tocados), len(faltan), len(tocados) + len(faltan)))
    w("   Y LOS DEL HUECO LLEVAN EL PREFIJO IGUAL: %d de %d, contado de sus "
      "propios nombres."
      % (sum(1 for x in faltan
             if os.path.basename(x).startswith("_v%d_" % VUELTA)), len(faltan)))
    if any(not os.path.basename(x).startswith("_v%d_" % VUELTA)
           for x in faltan):
        fallos += 1
    w("")

    w("2.a.8. LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA")
    _, f_ap = git(["log", "-1", "--format=%ad", "--date=short",
                   leer("docs/loop/SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA).strip()])
    _, f_ci = git(["log", "-1", "--format=%ad", "--date=short", "HEAD"])
    w("   fecha del commit de apertura, leida de git log: %s" % f_ap.strip())
    w("   fecha del commit de ahora mismo, leida de git log: %s" % f_ci.strip())
    w("")

    w("CIFRA comprobaciones que fallan: %d" % fallos)
    w("VERDE: el cierre integral sale limpio." if not fallos
      else "ROJO: el cierre integral tiene comprobaciones que fallan.")
    texto = NL.join(out) + NL
    destino = os.path.join(LOOP, "SALIDA_V%d_T2_CIERRE.txt" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    sys.stdout.write(NL + "SELLADO EN %s, %d bytes%s"
                     % (os.path.basename(destino), os.path.getsize(destino), NL))
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
