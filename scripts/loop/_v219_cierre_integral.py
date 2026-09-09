# -*- coding: utf-8 -*-
r"""_v219_cierre_integral.py . EL CIERRE INTEGRAL DE LA VUELTA 219, MEDIDO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

NO ES UNA TAREA DEL ENCARGO: el encargo de esta vuelta trae DOS tareas y las dos
son lectura. Esto es el cierre que EJECUTOR.md exige de toda vuelta, y por eso
sus cifras van en la seccion 3 del reporte y no en la tabla de tareas.

QUE MIDE, Y TODO SE LEE DE FICHEROS DE SALIDA QUE YA EXISTEN EN DISCO:
  . el ciclo entero de Gate 0 por los DOS lados, con sus DIECIOCHO salidas
    selladas y sus dos consolas, que el propio ciclo escribio;
  . las TRES suites solas, cada una con su exitcode y sus bytes;
  . el marcador y el censo, recomputados cada uno con su comando;
  . las sedes que la vuelta pudo mover, cotejadas por sha256 entre la apertura
    y el cierre;
  . la moratoria: cuantos ficheros escribio esta vuelta en el arbol de scripts
    y cuantos llevan el prefijo que le toca.

LA DIFERENCIA CON LA 218, DICHA ANTES DE MEDIR Y NO DESCUBIERTA DESPUES. Aquella
vuelta movia DOS cifras del marcador y UNA sede a proposito, y las declaraba por
adelantado. ESTA VUELTA NO MUEVE NINGUNA: sus dos tareas son lectura, medicion y
registro, y no escriben ni en el plan ni en el grafo ni en el registro del
cribado. Por eso MOVIDA_A_PROPOSITO va VACIO y las trece cifras del contraste van
SIN movimiento esperado: CUALQUIERA que se mueva es ROJO.

Y LA COLUMNA DE CONTRASTE ES LO QUE LA 218 PUBLICO, no lo que mi encargo dice: mi
encargo de esta vuelta NO trae cifras de marcador ni de censo (EJECUTOR.md 2, el
instrumento manda y una cifra vieja se cita como contraste, nunca como fuente).

USO:  python scripts/loop/_v219_cierre_integral.py
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
    "docs/plan/07_ADUANA.md",
    "docs/plan/01_FUENTES.md",
    "docs/plan/02_DESTEJIDOS.md",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "docs/INTRA_DOMINIO_INFORME.md",
    "docs/BANCO_DE_TEXTOS.md",
    "docs/plan/BANCO_DEL_PLAN.md",
    "dataset/metadata/master_graph.json",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
]

# LA SEDE QUE ESTA VUELTA MUEVE A PROPOSITO, NOMBRADA ANTES DE MEDIRLA.
MOVIDA_A_PROPOSITO = {
    # VACIO A PROPOSITO Y DECLARADO: las dos tareas de la 219 son
    # LECTURA, MEDICION y REGISTRO. Ninguna escribe en el plan, ni en
    # el grafo, ni en docs/INTRA_DOMINIO_VEREDICTOS.jsonl. CUALQUIER
    # sede que se mueva es ROJO, sin excepcion declarada.
}

# LOS FICHEROS QUE EL PROPIO CIERRE ANADE DESPUES DE ESTA MEDICION.
HUECO_DEL_CIERRE = [
    "scripts/loop/_v%d_cierre_texto.py" % VUELTA,
    "scripts/loop/_v%d_cierre_texto.md" % VUELTA,
]

# LO QUE LA 218 PUBLICO, CITADO COMO CONTRASTE Y NO COMO FUENTE (EJECUTOR.md 2).
# NINGUNA lleva movimiento esperado, porque esta vuelta no mueve ninguna.
CONTRASTE_218 = [
    ("marcador n", "3388", None),
    ("marcador A", "550", None),
    ("marcador B", "71", None),
    ("marcador C", "5", None),
    ("marcador D", "2762", None),
    ("marcador huecos", "0", None),
    ("censo nodos", "3853", None),
    ("censo vivos", "3169", None),
    ("censo deprecados", "684", None),
    ("aristas siguientes", "8780", None),
    ("aristas previos", "8740", None),
    ("aristas suma", "17520", None),
    ("aristas union", "9914", None),
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
    w("VUELTA %d. EL CIERRE INTEGRAL, MEDIDO DE SUS FICHEROS" % VUELTA)
    w("=" * 78)
    w("")

    w("3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, CON SUS SALIDAS SELLADAS")
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

    w("3.2. LAS DOS CONSOLAS DEL CICLO, SELLADAS POR EL PROPIO INSTRUMENTO")
    consolas = []
    for lado in ("APERTURA", "CIERRE"):
        rel = "docs/loop/SALIDA_V%d_CICLO_GATE0_%s_CONSOLA.txt" % (VUELTA, lado)
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(p):
            w("   CONSOLA %s: AUSENTE. ESO ES ROJO: es la caida 3.1 del acta "
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

    w("3.3. LAS TRES SUITES SOLAS, CADA UNA CON SU EXITCODE Y SUS BYTES")
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

    w("3.4. EL MARCADOR Y EL CENSO, RECOMPUTADOS CADA UNO CON SU COMANDO")
    rel_mar = "docs/loop/SALIDA_V%d_T2_MARCADOR.txt" % VUELTA
    rel_ari = "docs/loop/SALIDA_V%d_T2_ARISTAS.txt" % VUELTA
    mar = leer(rel_mar)
    ari = leer(rel_ari)
    w("   COMANDO 1: python scripts/recomputar_marcador.py 3388 -> %s" % rel_mar)
    w("   COMANDO 2: python scripts/loop/vuelta83_conteo_aristas.py WORK -> %s"
      % rel_ari)
    clases, dentro = {}, False
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
    n = re.search(r"n = (\d+)", mar).group(1)
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

    w("3.5. LAS CIFRAS, COTEJADAS CONTRA LAS QUE LA 218 PUBLICO, Y NO COPIADAS")
    w("   LA COLUMNA DE LA DERECHA NO ES DE MI ENCARGO: mi encargo de esta "
      "vuelta NO trae cifras de marcador ni de censo. Es LO QUE LA 218 PUBLICO, "
      "citado como CONTRASTE (EJECUTOR.md 2).")
    w("   Y ESTA VUELTA NO DECLARA NINGUN MOVIMIENTO ESPERADO, porque no mueve "
      "nada: las TRECE tienen que quedarse quietas y cualquiera que se mueva es "
      "ROJO.")
    mias = {
        "marcador n": n, "marcador A": clases.get("A"),
        "marcador B": clases.get("B"), "marcador C": clases.get("C"),
        "marcador D": clases.get("D"), "marcador huecos": huecos,
        "censo nodos": censo[0], "censo vivos": censo[1],
        "censo deprecados": censo[2], "aristas siguientes": censo[3],
        "aristas previos": censo[4], "aristas suma": censo[5],
        "aristas union": censo[6],
    }
    quietas_ok, movidas_ok, descuadres = 0, 0, 0
    filas_cotejo = []
    for etiqueta, suya, movimiento in CONTRASTE_218:
        mia = str(mias[etiqueta])
        if movimiento is None:
            calza = (mia == suya)
            veredicto = "QUIETA Y CALZA" if calza else "DESCUADRE"
            quietas_ok += 1 if calza else 0
        else:
            delta = int(movimiento.split(":")[0])
            calza = (mia == str(int(suya) + delta))
            veredicto = ("SE MOVIO LO QUE SE DIJO" if calza
                         else "NO SE MOVIO LO QUE SE DIJO")
            movidas_ok += 1 if calza else 0
        if not calza:
            descuadres += 1
        filas_cotejo.append((etiqueta, mia, suya, movimiento or "quieta",
                             veredicto))
        w("   COTEJO %-22s | LA MIA %-8s | la 218 %-8s | esperado %-46s | %s"
          % (etiqueta, mia, suya, movimiento or "quieta, sin movimiento",
             veredicto))
    w("CIFRA cifras cotejadas: %d | CIFRA que NO calzan: %d"
      % (len(CONTRASTE_218), descuadres))
    w("CIFRA cifras que debian quedarse quietas y se quedaron: %d | CIFRA que "
      "debian moverse y se movieron: %d" % (quietas_ok, movidas_ok))
    if descuadres:
        fallos += 1
    w("")

    w("3.6. LAS SEDES QUE LA VUELTA PUDO MOVER, COTEJADAS POR SU sha256")
    ap = leer("docs/loop/SALIDA_V%d_APERTURA.txt" % VUELTA)
    filas_sede, movidas, movidas_mal = [], 0, 0
    for rel in SEDES:
        antes = None
        for l in ap.split(NL):
            if l.startswith("CIFRA " + rel + ":") and "sha256 LF " in l:
                antes = l.split("sha256 LF ", 1)[1].strip()
        ahora = sha_lf(rel)
        d, lf = dos_convenciones(rel)
        if antes is None:
            _, ns = git(["diff", "--numstat", "HEAD", "--", rel])
            filas = [x for x in ns.split(NL) if x.strip()]
            quieta = not filas
            via = ("NO MEDIDA AL ABRIR: su quietud se mide con git diff "
                   "--numstat HEAD, %d filas" % len(filas))
        else:
            quieta = (antes == ahora)
            via = "cotejo de los dos sha256"
        esperada = rel in MOVIDA_A_PROPOSITO
        if not quieta:
            movidas += 1
            if not esperada:
                movidas_mal += 1
        estado = ("QUIETA" if quieta else
                  ("MOVIDA A PROPOSITO" if esperada else "SE MOVIO SIN AVISO"))
        if quieta and esperada:
            estado = "SE DIJO QUE SE MOVERIA Y NO SE MOVIO"
            movidas_mal += 1
        filas_sede.append((rel, antes, ahora, estado, d, lf))
        w("   SEDE %-42s | al abrir %s | al cerrar %s | %s | %d / %d bytes | %s"
          % (rel, antes if antes is not None else "NO_MEDIDA_AL_ABRIR",
             ahora, estado, d, lf, via))
        if esperada:
            w("      MOTIVO DECLARADO ANTES DE MEDIR: %s" % MOVIDA_A_PROPOSITO[rel])
    w("CIFRA sedes cotejadas: %d | CIFRA que se movieron: %d" % (len(filas_sede),
                                                                 movidas))
    w("CIFRA sedes que se movieron A PROPOSITO y estaban declaradas: %d | CIFRA "
      "que se movieron SIN AVISO: %d" % (movidas - movidas_mal, movidas_mal))
    if movidas_mal:
        fallos += 1
    w("")

    w("3.7. LA MORATORIA: LO QUE ESTA VUELTA ESCRIBIO EN EL ARBOL DE SCRIPTS")
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
    w("")
    w("3.7.bis. EL HUECO DE ESTA MISMA CIFRA, DECLARADO Y NOMBRADO")
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
    if any(not os.path.basename(x).startswith("_v%d_" % VUELTA) for x in faltan):
        fallos += 1
    w("")

    w("3.8. LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA")
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
    destino = os.path.join(LOOP, "SALIDA_V%d_CIERRE_INTEGRAL.txt" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    sys.stdout.write(NL + "SELLADO EN %s, %d bytes%s"
                     % (os.path.basename(destino), os.path.getsize(destino), NL))
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
