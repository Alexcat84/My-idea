# -*- coding: utf-8 -*-
r"""vuelta189_apertura.py . EL SELLO DE APERTURA DE LA VUELTA 189, QUE ES VUELTA
DE BATERIA.

POR QUE EXISTE: `EJECUTOR.md` 1, "LA APERTURA SE MIDE ANTES DE LA PRIMERA
OPERACION". Este fichero corre ANTES de tocar nada y deja escrito en disco el
estado del arbol, de las rutas que el encargo nombra y de los sujetos que las DOS
tareas van a mover. Ninguna cifra del encargo se copia: TODAS se computan aqui y
se comparan con lo que el encargo dice, publicando LAS DOS.

EL SELLO DEL AUDITOR DE ESTA VUELTA SE LLAMA V189b Y NO SE DEDUCE A OJO. La casa
nombra el sello del acta N como V(N+1), pero el prefijo `_auditor_v189_*` YA
ESTABA TOMADO por el turno que escribio el acta 188, y el acta 189 lo declara en
su propia cabecera: su prefijo es `_auditor_v189b_*` y su sello
`SELLO_APERTURA_AUDITOR_V189b.json`. Aqui se miden LOS DOS y se dice cual es cual.

Y ESTE FICHERO MIDE EL DESFASE DEL CALIBRADO EN LA APERTURA, no al cierre: una
columna de apertura medida al cierre es caida que ACUMULA (`EJECUTOR.md` 1).

LO QUE ESTE FICHERO NO HACE: no escribe el reporte, no toca `dataset/` a mano, no
toca ningun veredicto, NO ESCRIBE NINGUNA SALIDA DE BATERIA y no registra ninguna
acta. Mide y escribe SALIDA_V189_*.txt. Del lanzador de la bateria de la 183 solo
corre `--plan` y `--siguiente`, que NO escriben nada y NO corren ningun arnes.

USO:
  python scripts/loop/vuelta189_apertura.py
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
NL = chr(10)
LANZADOR = os.path.basename(os.path.abspath(__file__))
VUELTA = int(re.search(r"vuelta(\d+)_", LANZADOR).group(1))
SUFIJO = str(VUELTA)
# EL SELLO DEL AUDITOR NO SE DEDUCE: el acta 189 declara su propio prefijo en su
# cabecera y aqui se leen LOS DOS candidatos, el que la regla V(N+1) da y el que
# el acta declara, y se publican los dos con sus bytes.
SELLO_POR_REGLA = "V%d" % VUELTA
SELLO_DECLARADO = "V%db" % VUELTA

sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

SUJETOS = [
    "scripts/loop/vuelta183_bateria_por_tramos.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/cotejar_clon_declarado.py",
    "scripts/loop/serie_de_registros.py",
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/tallar_cabecera_reporte.py",
    "scripts/loop/anexar_tarea_al_reporte.py",
    "scripts/loop/guarda_commit_dataset.py",
    "scripts/loop/vuelta188_tarea1a_registrar_acta188.py",
    "scripts/loop/vuelta187_tarea1a_registrar_acta187.py",
    "scripts/loop/vuelta188_esqueleto_reporte.py",
    "scripts/loop/vuelta150_3_relectura_expediente.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/SELLO_APERTURA_AUDITOR_V189.json",
    "docs/loop/SELLO_APERTURA_AUDITOR_V189b.json",
    "docs/loop/_auditor_v189b_ciega_blind.txt",
    "docs/loop/_auditor_v189b_ciega_reveal.txt",
    "docs/loop/_auditor_v189b_mis_clases.txt",
    "docs/loop/_auditor_v189b_exclusion.txt",
    "docs/loop/SALIDA_V188_APERTURA.txt",
    "docs/loop/SALIDA_V188_CERRAR_REPORTE.txt",
    "docs/loop/SALIDA_V188_TALLADOR_CABECERA.txt",
    "docs/loop/SALIDA_V183_BATERIA.txt",
    "docs/loop/reportes/REPORTE_V186.md",
    "docs/loop/reportes/REPORTE_V187.md",
    "docs/loop/reportes/REPORTE_V188.md",
    "docs/PENDIENTES.md",
    "docs/plan/CORRECCIONES_A_APLICAR.md",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/BANCO_DEL_PLAN.md",
    "docs/BANCO_DE_TEXTOS.md",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
] + SUJETOS


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env, shell=shell)
    out = (r.stdout.decode("utf-8", errors="replace")
           + r.stderr.decode("utf-8", errors="replace"))
    return r.returncode, out


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def bytes_de_git(ruta):
    c, o = git(["cat-file", "-s", "HEAD:" + ruta])
    o = o.strip()
    return int(o) if c == 0 and o.isdigit() else None


def sha_de(ruta):
    """LAS DOS CONVENCIONES, MEDIDAS Y NO SUPUESTAS."""
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (hashlib.sha256(datos).hexdigest(), hashlib.sha256(lf).hexdigest(),
            len(datos), len(lf))


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V%s_%s_APERTURA.txt" % (SUFIJO, nombre))
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("ESCRITO: %s (%d bytes)"
          % (os.path.basename(ruta), len(texto.encode("utf-8"))))


L = []
w = L.append
w("SELLO DE APERTURA DE LA VUELTA %d, escrito ANTES de la primera operacion." % VUELTA)
w("Sufijo de salidas: %s (computado de %s, no tecleado)" % (SUFIJO, LANZADOR))
w("regimen: ES VUELTA DE BATERIA (AUDITOR.md 6.1). La bateria corre cada cinco")
w("         vueltas, en una vuelta propia que NO LLEVA NADA MAS. La ultima cerro")
w("         entera en la 184, asi que la siguiente es esta. DOS TAREAS y la")
w("         segunda es la bateria.")
w("         Sello del auditor por la regla V(N+1): %s" % SELLO_POR_REGLA)
w("         Sello que el acta 189 DECLARA en su cabecera: %s" % SELLO_DECLARADO)
w("         Los dos se miden abajo; no se elige uno a ojo.")
w("")

w("=== A. HEAD DE APERTURA (git rev-parse HEAD, leido y no tecleado) ===")
c, head = git(["rev-parse", "HEAD"])
head = head.strip()
w(head)
c, asunto = git(["log", "-1", "--format=%H%x09%ad%x09%s", "--date=iso"])
w(asunto.strip()[:400])
w("")

w("=== B. RAMA Y REMOTO (leidos de git, no tecleados) ===")
c, rama = git(["rev-parse", "--abbrev-ref", "HEAD"])
w("rama: " + rama.strip())
c, up = git(["rev-parse", "--abbrev-ref", "@{u}"])
w("remoto de seguimiento: " + (up.strip() if c == 0 else "(ninguno)"))
c, ahead = git(["rev-list", "--left-right", "--count", "HEAD...@{u}"])
w("adelante/atras contra el remoto (HEAD...upstream): "
  + (ahead.strip() if c == 0 else "(no medible)"))
w("")

w("=== B.1 LA CADENA DE LA VUELTA 188, LOCALIZADA EN GIT Y NO TECLEADA ===")
c, logtodo = git(["log", "--format=%h%x09%s", "-160"])
for etiqueta, aguja in (("acta 188", "ACTA DEL AUDITOR, VUELTA 188"),
                        ("acta 189", "ACTA DEL AUDITOR, VUELTA 189"),
                        ("tarea 1 de la 188", "VUELTA 188, TAREA 1"),
                        ("tarea 5 de la 188", "VUELTA 188, TAREA 5"),
                        ("cierre de la 188", "VUELTA 188 CERRADA")):
    hits = [l for l in logtodo.splitlines() if aguja.upper() in l.upper()]
    w("   %-20s -> %s"
      % (etiqueta, (hits[0][:150] if hits else "NO LOCALIZADO EN LOS 160 ULTIMOS")))
w("")

w("=== C. git status --porcelain ENTERO ===")
c, st = git(["status", "--porcelain"])
for l in st.splitlines():
    w(l)
w("CIFRA lineas de status: %d" % len([l for l in st.splitlines() if l.strip()]))
w("")

w("=== D. BYTES DE CADA RUTA QUE EL ENCARGO NOMBRA, POR LAS DOS CONVENCIONES ===")
for ruta in RUTAS_DEL_ENCARGO:
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    g = bytes_de_git(ruta)
    if os.path.exists(p):
        _sd, _sl, bd, bl = sha_de(p)
        w("%s -> disco %d bytes | LF %d bytes | git %s"
          % (ruta, bd, bl, ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
    else:
        w("%s -> NO EXISTE EN DISCO | git %s"
          % (ruta, ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("")

w("=== E. EL NUMSTAT DE dataset/ AL ENTRAR, QUE ES LA VARA Y NO EL git status ===")
c, ns = git(["diff", "--numstat", "--", "dataset/"])
for l in ns.splitlines():
    w("   " + l)
w("CIFRA filas de `git diff --numstat -- dataset/` AL ENTRAR: %d"
  % len([l for l in ns.splitlines() if l.strip()]))
w("")

w("=== F. LO NO SEGUIDO POR GIT, FICHERO A FICHERO CON SUS BYTES ===")
c, unt = git(["ls-files", "--others", "--exclude-standard"])
nn = 0
for l in unt.splitlines():
    if not l.strip():
        continue
    nn += 1
    pp = os.path.join(RAIZ, l.replace("/", os.sep))
    w("   %s -> %d bytes" % (l, os.path.getsize(pp) if os.path.exists(pp) else -1))
w("CIFRA ficheros no seguidos: %d" % nn)
w("")

w("=== G. LOS DOS SELLOS DEL AUDITOR, MEDIDOS Y NO ELEGIDOS A OJO ===")
w("(el acta 189 publica 862 / 40517 / 29681 y 381 puestos excluidos. AQUI NO SE")
w(" COPIA NINGUNA: se computan y se comparan, y se publican LAS DOS)")
for etiqueta, sufijo_sello in (("por la regla V(N+1)", SELLO_POR_REGLA),
                               ("declarado por el acta", SELLO_DECLARADO)):
    ruta_sello = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_%s.json" % sufijo_sello)
    w("   SELLO %s (%s):" % (sufijo_sello, etiqueta))
    if not os.path.exists(ruta_sello):
        w("      NO EXISTE")
        continue
    sd, sl, bd, bl = sha_de(ruta_sello)
    w("      docs/loop/SELLO_APERTURA_AUDITOR_%s.json -> disco %d bytes | LF %d bytes"
      % (sufijo_sello, bd, bl))
    sello = json.load(io.open(ruta_sello, encoding="utf-8"))
    for l in io.open(ruta_sello, encoding="utf-8").read().replace(
            chr(13) + NL, NL).split(NL):
        w("      | " + l)
    for clave_r, clave_b, clave_s in (("ciega", "bytes_ciega", "sha256_ciega"),
                                      ("destape", "bytes_destape", "sha256_destape")):
        if clave_r not in sello:
            continue
        r = sello[clave_r]
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        if not os.path.exists(p):
            w("      %-8s %s -> NO EXISTE EN DISCO" % (clave_r, r))
            continue
        sd2, sl2, bd2, bl2 = sha_de(p)
        w("      %-8s %s" % (clave_r, r))
        w("         bytes: sello %s | disco medido %d -> %s"
          % (sello.get(clave_b), bd2,
             "CALZA" if sello.get(clave_b) == bd2 else "NO CALZA"))
        w("         sha256 sello %s" % sello.get(clave_s))
        w("         sha256 LF    %s -> %s"
          % (sl2, "CALZA" if sello.get(clave_s) == sl2 else "NO CALZA"))
w("")

w("=== G.1 LOS PUESTOS DE LA CIEGA Y DE LA EXCLUSION, CONTADOS DE SU FICHERO ===")
PAT_PUESTO = re.compile(r"puesto_intra[^0-9]{0,12}(\d+)")


def puestos_de(ruta):
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    if not os.path.exists(p):
        return []
    t = io.open(p, encoding="utf-8", errors="replace").read()
    return sorted(set(int(x) for x in PAT_PUESTO.findall(t)))


ciega = puestos_de("docs/loop/_auditor_v189b_ciega_blind.txt")
destape = puestos_de("docs/loop/_auditor_v189b_ciega_reveal.txt")
ciega_ant = puestos_de("docs/loop/_auditor_v189_ciega_blind.txt")
w("   ciega del acta 189 (_auditor_v189b_ciega_blind.txt): %d puestos distintos"
  % len(ciega))
w("      %s" % ", ".join(str(x) for x in ciega))
w("   destape del acta 189: %d puestos distintos" % len(destape))
w("   ciega del acta 188 (_auditor_v189_ciega_blind.txt): %d puestos" % len(ciega_ant))
EXCL = os.path.join(LOOP, "_auditor_v189b_exclusion.txt")
excl = []
if os.path.exists(EXCL):
    crudo = io.open(EXCL, encoding="utf-8").read()
    excl = sorted(set(int(x) for x in re.findall(r"\d+", crudo)))
w("   exclusion: %d puestos distintos (el acta dice 381 -> %s)"
  % (len(excl), "CALZA" if len(excl) == 381 else "NO CALZA"))
w("   SOLAPE ciega del acta 189 con la exclusion: %d" % len(set(ciega) & set(excl)))
w("   SOLAPE ciega del acta 189 con la del acta 188: %d"
  % len(set(ciega) & set(ciega_ant)))
w("   EL PUESTO 2422, QUE EL ACTA NOMBRA: %s de la ciega del acta 189"
  % ("DENTRO" if 2422 in ciega else "FUERA"))
w("")

w("=== H. EL REPORTE EN HEAD, MEDIDO SIN CREERLE AL ENCARGO ===")
REP = os.path.join(LOOP, "REPORTE.md")
if os.path.exists(REP):
    sd, sl, bd, bl = sha_de(REP)
    t_rep = io.open(REP, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("   primera linea: %s" % t_rep.split(NL)[0])
    w("   disco %d bytes | LF %d bytes | saltos de linea %d | sha256 LF %s"
      % (bd, bl, t_rep.count(NL), sl))
    n9 = [i for i, l in enumerate(t_rep.split(NL), 1) if l.startswith("## 9.")]
    w("   CIFRA secciones `## 9.`: %d, en las lineas %s"
      % (len(n9), ", ".join(str(x) for x in n9) or "(ninguna)"))
w("")

w("=== H.0 LAS VUELTAS QUE CIERRAN SU PROPIO REPORTE, MEDIDAS ===")
for r in ("docs/loop/SALIDA_V186_CERRAR_REPORTE.txt",
          "docs/loop/SALIDA_V187_CERRAR_REPORTE.txt",
          "docs/loop/SALIDA_V188_CERRAR_REPORTE.txt"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if not os.path.exists(p):
        w("   %s -> NO EXISTE" % r)
        continue
    sd, sl, bd, bl = sha_de(p)
    w("   %s -> disco %d bytes | LF %d bytes | sha256 LF %s" % (r, bd, bl, sl))
    for i, l in enumerate(io.open(p, encoding="utf-8").read()
                          .replace(chr(13) + NL, NL).split(NL), 1):
        if "CIFRA piezas que faltan" in l:
            w("      LINEA %d: %s" % (i, l.strip()))
w("")

w("=== H.1 LA SERIE DE REGISTROS, LLAMADA Y NO TECLEADA (TAREA 1) ===")
try:
    import serie_de_registros as SER
    halladas = SER.entradas()
    w("   CIFRA entradas de la serie: %d" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SER.colisiones(halladas)), len(SER.huecos(halladas))))
    w("   SIGUIENTE LIBRE, LLAMADO Y NO TECLEADO: R.%d"
      % SER.siguiente_libre(halladas))
    for numero, rel_, linea, titulo in halladas[-3:]:
        w("   ULTIMOS: R.%s en %s:%d -> %s" % (numero, rel_, linea, titulo[:110]))
except Exception as e:
    w("   NO SE PUDO RECOMPUTAR LA SERIE: %r" % (e,))
w("")

w("=== H.2 EL ACTA 189, ACOTADA, Y SUS SECCIONES ===")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
t_acta = io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
lin_acta = t_acta.split(NL)
CAB189 = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA
cab = [i for i, l in enumerate(lin_acta, 1) if l.startswith(CAB189)]
w("   docs/loop/ACTA_AUDITOR.md -> %d lineas | disco %d bytes"
  % (len(lin_acta), os.path.getsize(ACTA)))
w("   CIFRA cabeceras %r: %d (lineas %s)"
  % (CAB189, len(cab), ", ".join(str(x) for x in cab) or "ninguna"))
if len(cab) == 1:
    ini = cab[0]
    todas = [i for i, l in enumerate(lin_acta, 1)
             if l.startswith("# ACTA DEL AUDITOR, VUELTA ")]
    post = [i for i in todas if i > ini]
    fin = (min(post) - 1) if post else len(lin_acta)
    w("   el acta %d va de la linea %d a la %d (%d lineas)"
      % (VUELTA, ini, fin, fin - ini + 1))
    for i in range(ini, fin + 1):
        if lin_acta[i - 1].startswith("## "):
            w("      LINEA %-6d %s" % (i, lin_acta[i - 1][:110]))
    w("   LAS CLAVES `4.n` DE LA SECCION 4, CONTADAS CON LOS DOS PATRONES:")
    p_con = re.compile(r"^\s*\*\*`4\.(\d+)`")
    p_sin = re.compile(r"^\s*\*\*4\.(\d+)\b")
    for nombre, pat in (("CON comillas inversas", p_con),
                        ("SIN comillas inversas", p_sin)):
        hits = [(i, pat.match(lin_acta[i - 1]).group(1))
                for i in range(ini, fin + 1) if pat.match(lin_acta[i - 1])]
        w("      %s -> %d (%s)"
          % (nombre, len(hits), ", ".join("4.%s@%d" % (n, i) for i, n in hits)))
    w("   LAS CAIDAS `C.n`, CON LA CABECERA DE SU SECCION:")
    p_c = re.compile(r"^\s*(?:-\s+)?\*\*`?C\.(\d+)`?[,.\s]")
    for i in range(ini, fin + 1):
        m = p_c.match(lin_acta[i - 1])
        if not m:
            continue
        cabec = ""
        for j in range(i, ini - 1, -1):
            if lin_acta[j - 1].startswith("## "):
                cabec = lin_acta[j - 1]
                break
        w("      LINEA %-6d C.%s bajo %r" % (i, m.group(1), cabec[:90]))
        w("         %s" % lin_acta[i - 1].strip()[:120])
w("")

w("=== H.3 EL REGISTRADOR DE LA 188 Y SU IDEMPOTENCIA, MEDIDA SIN CORRERLO ===")
w("(la `C.2` del acta 189 dice que re correrlo escribe una entrada duplicada.")
w(" AQUI NO SE CORRE: se mide su codigo, que es lo que se puede medir sin mutar)")
REG188 = os.path.join(RAIZ, "scripts", "loop",
                      "vuelta188_tarea1a_registrar_acta188.py")
if os.path.exists(REG188):
    sd, sl, bd, bl = sha_de(REG188)
    t_reg = io.open(REG188, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("   scripts/loop/vuelta188_tarea1a_registrar_acta188.py -> disco %d bytes | "
      "LF %d bytes | lineas %d" % (bd, bl, t_reg.count(NL)))
    w("   sha256 LF: %s" % sl)
    for i, l in enumerate(t_reg.split(NL), 1):
        if ("    ya = " in l or "K) LA IDEMPOTENCIA" in l
                or "la marca %r ya esta" in l):
            w("      LINEA %-5d %s" % (i, l.strip()[:120]))
w("   Y LA ENTRADA QUE YA REGISTRA EL ACTA 188, BUSCADA EN LAS DOS SEDES:")
for sede in ("docs/PENDIENTES.md", "docs/plan/CORRECCIONES_A_APLICAR.md"):
    p = os.path.join(RAIZ, sede.replace("/", os.sep))
    t_sede = io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    for aguja in ("del acta de la vuelta 188", "del acta de la vuelta 189"):
        hits = [i for i, l in enumerate(t_sede.split(NL), 1) if aguja in l]
        w("      %s | %r -> %d linea(s) %s"
          % (sede, aguja, len(hits), ", ".join(str(x) for x in hits) or ""))
w("")

w("=== H.4 LA NOMINA Y EL REPARTO DE LA BATERIA, COMPUTADOS HOY ===")
w("(el acta 189 publica 125 entradas y 10 tramos. AQUI NO SE COPIA)")
try:
    import verificar_mutaciones_viejas as VM
    w("   CIFRA nomina (len(VM.VIEJAS)) leida del modulo: %d" % len(VM.VIEJAS))
    w("   VARA_DEL_CENSO: %s" % VM.VARA_DEL_CENSO)
    w("   arneses_que_faltan() HOY: %s" % (VM.arneses_que_faltan(),))
except Exception as e:
    w("   NO SE PUDO LLAMAR: %r" % (e,))
c_plan, o_plan = correr([PY, "scripts/loop/vuelta183_bateria_por_tramos.py", "--plan"])
escribir("T2_PLAN_183", o_plan + NL + "EXITCODE: %d" % c_plan + NL)
for l in o_plan.split(NL):
    if (l.strip().startswith("CIFRA ") or "ESTIMACION" in l
            or l.strip().startswith("TRAMO ")):
        w("   " + l.strip())
w("   exitcode de --plan del lanzador de la 183: %d" % c_plan)
c_sig, o_sig = correr([PY, "scripts/loop/vuelta183_bateria_por_tramos.py",
                       "--siguiente"])
escribir("T2_SIGUIENTE_183", o_sig + NL + "EXITCODE: %d" % c_sig + NL)
for l in o_sig.split(NL):
    if (l.strip().startswith("CIFRA ") or "EL SIGUIENTE ES" in l
            or "LOS QUE FALTAN" in l):
        w("   " + l.strip())
w("   exitcode de --siguiente del lanzador de la 183: %d" % c_sig)
w("")

w("=== H.5 LAS SALIDAS SELLADAS DE LA CORRIDA 183/184, QUE NO SE BORRAN ===")
n_tramos_183 = 0
for i in range(1, 21):
    r = "docs/loop/SALIDA_V183_BATERIA_TRAMO_%d.txt" % i
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if not os.path.exists(p):
        continue
    n_tramos_183 += 1
    sd, sl, bd, bl = sha_de(p)
    w("   %s -> disco %d bytes | LF %d bytes | sha256 LF %s" % (r, bd, bl, sl[:16]))
w("   CIFRA salidas SALIDA_V183_BATERIA_TRAMO_n.txt en disco: %d" % n_tramos_183)
propias = [i for i in range(1, 21)
           if os.path.exists(os.path.join(
               LOOP, "SALIDA_V%d_BATERIA_TRAMO_%d.txt" % (VUELTA, i)))]
for i in propias:
    r = "docs/loop/SALIDA_V%d_BATERIA_TRAMO_%d.txt" % (VUELTA, i)
    w("   YA EXISTE %s -> %d bytes"
      % (r, os.path.getsize(os.path.join(RAIZ, r.replace("/", os.sep)))))
w("   CIFRA salidas SALIDA_V%d_BATERIA_TRAMO_n.txt en disco AL ENTRAR: %d"
  % (VUELTA, len(propias)))
w("")

w("=== H.6 EL ARCHIVO DE VEREDICTOS, QUE ESTA VUELTA NO MUEVE ===")
w("(el acta 189 da 0a77b5a35a962621 como sha256 LF. NO SE COPIA)")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
sd, sl, bd, bl = sha_de(VER)
w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> disco %d bytes | LF %d bytes" % (bd, bl))
w("   sha256 (disco): %s" % sd)
w("   sha256 (LF)   : %s" % sl)
w("   los 16 primeros del sha256 LF: %s -> el acta dice 0a77b5a35a962621: %s"
  % (sl[:16], "CALZA" if sl[:16] == "0a77b5a35a962621" else "NO CALZA"))
filas_v = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
w("   CIFRA filas: %d" % len(filas_v))
por_clase = {}
for f in filas_v:
    por_clase[f.get("clase")] = por_clase.get(f.get("clase"), 0) + 1
for k in sorted(por_clase, key=lambda x: (x is None, str(x))):
    w("   CIFRA clase %-6s: %d" % (repr(k), por_clase[k]))
pv = [f.get("puesto_intra") for f in filas_v]
w("   MIN puesto %s | MAX puesto %s | HUECOS %d | DUPLICADOS %d"
  % (min(pv), max(pv), len(set(range(min(pv), max(pv) + 1)) - set(pv)),
     len(pv) - len(set(pv))))
w("")

w("FIN DEL SELLO DE APERTURA")

texto = NL.join(L) + NL
io.open(os.path.join(LOOP, "SALIDA_V%s_APERTURA.txt" % SUFIJO), "w",
        encoding="utf-8", newline=NL).write(texto)
print(texto)
escribir("HEAD", head + NL)

# ------------------------------------------------- EL BLOQUE DE MEDICIONES
# NINGUNA GUARDA SE TOCA (MODO AUSTERO 4): el ciclo de Gate 0 corre entero, y el
# DESFASE DEL CALIBRADO SE MIDE AQUI, EN LA APERTURA, y no al cierre.
c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
escribir("GATE0_CMD1", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
escribir("CICLO_ETIQUETAS", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/sync_assets_web.py"])
escribir("CICLO_SYNC", o + "\nEXITCODE: %d\n" % c)

c, o = correr(["git", "diff", "HEAD", "--numstat", "--", "dataset/", "web/", "engine/"])
escribir("CICLO_NUMSTAT", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
escribir("CONTEO", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + "\nEXITCODE: %d\n" % c)

c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True,
              cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d\n" % c)

c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + "\nEXITCODE: %d\n" % c)

print("BLOQUE DE APERTURA COMPLETO")
