# -*- coding: utf-8 -*-
r"""vuelta190_apertura.py . EL SELLO DE APERTURA DE LA VUELTA 190, QUE NO ES
VUELTA DE BATERIA Y LLEVA CINCO SUB-TAREAS.

POR QUE EXISTE: `EJECUTOR.md` 1, "LA APERTURA SE MIDE ANTES DE LA PRIMERA
OPERACION". Este fichero corre ANTES de tocar nada y deja escrito en disco el
estado del arbol, de las rutas que el encargo nombra y de los sujetos que las
CINCO tareas van a mover. Ninguna cifra del encargo se copia: TODAS se computan
aqui y se comparan con lo que el encargo dice, publicando LAS DOS.

CLON DECLARADO de scripts/loop/vuelta189_apertura.py. Cambia el numero de vuelta,
la lista de SUJETOS y de RUTAS_DEL_ENCARGO, los bloques H.n (que miden lo que
ESTA vuelta va a mover y no lo que movia la 189) y este docstring. El cotejo del
clon lo hace scripts/loop/cotejar_clon_declarado.py y su salida se pega en el
reporte con lo que salga: AQUI NO SE AFIRMA QUE NINGUN DIFF SALGA VACIO.

EL SELLO DEL AUDITOR DE ESTA VUELTA ES `V190` Y NO SE DEDUCE A OJO: el acta 190
lo declara en su propia cabecera (`SELLO_APERTURA_AUDITOR_V190.json`, prefijo
`_auditor_v190_*`). Aqui se mide, no se cree.

Y ESTE FICHERO MIDE EL DESFASE DEL CALIBRADO EN LA APERTURA, no al cierre: una
columna de apertura medida al cierre es caida que ACUMULA (`EJECUTOR.md` 1).

LO QUE ESTE FICHERO NO HACE: no escribe el reporte, no toca `dataset/` a mano, no
toca ningun veredicto, NO CORRE NINGUN ARNES, NO CORRE LA BATERIA (la 190 NO es
vuelta de bateria: la siguiente cae en la 194) y no registra ninguna acta. Mide y
escribe SALIDA_V190_*.txt.

USO:
  python scripts/loop/vuelta190_apertura.py
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
SELLO_POR_REGLA = "V%d" % VUELTA

sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

SUJETOS = [
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/vuelta189_bateria_por_tramos.py",
    "scripts/loop/vuelta189_tarea2_nomina.py",
    "scripts/loop/vuelta189_tarea1a_registrar_acta189.py",
    "scripts/loop/aislador_de_ciega.py",
    "scripts/loop/vuelta182_tarea1c_relectura_al_doble.py",
    "scripts/loop/serie_de_registros.py",
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/tallar_cabecera_reporte.py",
    "scripts/loop/anexar_tarea_al_reporte.py",
    "scripts/loop/cotejar_clon_declarado.py",
    "scripts/loop/vuelta150_3_relectura_expediente.py",
]

# LAS TRES SALIDAS SELLADAS AJENAS QUE LA BATERIA DE LA 189 PISO. El acta 190 las
# nombra en su `4.9` y esta vuelta las mide AL ENTRAR para poder decir despues si
# la restauracion a mano dejo el disco donde tenia que dejarlo.
SELLADAS_PISADAS = [
    "docs/loop/SALIDA_V184_T1C_MUTACION_ESTIMACION.txt",
    "docs/loop/SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt",
    "docs/loop/SALIDA_V188_T4_MUTACION_COBERTURA_PAREJAS.txt",
]

# LAS TRES ENTRADAS QUE LA GUARDA DEL SUJETO CONGELADO SACA HOY. El encargo las
# nombra y dice EXPRESAMENTE que se mida cuantas traen motivo escrito, no que se
# suponga.
LAS_TRES_SIN_CONGELAR = [
    "vuelta186_tarea2c_mutacion_cierre_tardio.py",
    "vuelta187_tarea4_mutacion_dos_convenciones.py",
    "vuelta188_tarea4_mutacion_cobertura_parejas.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/SELLO_APERTURA_AUDITOR_V190.json",
    "docs/loop/_auditor_v190_ciega_blind.txt",
    "docs/loop/_auditor_v190_ciega_reveal.txt",
    "docs/loop/_auditor_v190_mis_clases.txt",
    "docs/loop/_auditor_v190_exclusion.txt",
    "docs/loop/_auditor_v190_vara.txt",
    "docs/loop/_auditor_v189b_ciega_blind.txt",
    "docs/loop/_auditor_v189b_exclusion.txt",
    "docs/loop/SALIDA_V189_APERTURA.txt",
    "docs/loop/SALIDA_V189_CERRAR_REPORTE.txt",
    "docs/loop/SALIDA_V189_TALLADOR_CABECERA.txt",
    "docs/loop/SALIDA_V189_BATERIA.txt",
    "docs/loop/SALIDA_V189_T2_NOMINA.txt",
    "docs/loop/ROJOS_DE_LA_VUELTA_189.txt",
    "docs/loop/reportes/REPORTE_V187.md",
    "docs/loop/reportes/REPORTE_V188.md",
    "docs/loop/reportes/REPORTE_V189.md",
    "docs/PENDIENTES.md",
    "docs/plan/CORRECCIONES_A_APLICAR.md",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/BANCO_DEL_PLAN.md",
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "docs/BANCO_DE_TEXTOS.md",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
] + SELLADAS_PISADAS + SUJETOS


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
w("regimen: NO ES VUELTA DE BATERIA (AUDITOR.md 6.1). La 189 la corrio entera y")
w("         la siguiente cae en la 194. La seccion 9 del reporte cierra con el")
w("         HUECO DECLARADO Y MEDIDO por su carril. CINCO SUB-TAREAS, porque el")
w("         tope temporal de la 6.2 caduco por la adjudicacion 4.10 del acta 190.")
w("         Sello del auditor por la regla V(N+1): %s" % SELLO_POR_REGLA)
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

w("=== B.1 LA CADENA DE LA VUELTA 189, LOCALIZADA EN GIT Y NO TECLEADA ===")
c, logtodo = git(["log", "--format=%h%x09%s", "-160"])
for etiqueta, aguja in (("acta 189", "ACTA DEL AUDITOR, VUELTA 189"),
                        ("acta 190", "ACTA DEL AUDITOR, VUELTA 190"),
                        ("tarea 1 de la 189", "VUELTA 189, TAREA 1"),
                        ("tarea 2 de la 189", "VUELTA 189, TAREA 2"),
                        ("cierre de la 189", "VUELTA 189 CERRADA")):
    hits = [l for l in logtodo.splitlines() if aguja.upper() in l.upper()]
    w("   %-20s -> %s"
      % (etiqueta, (hits[0][:150] if hits else "NO LOCALIZADO EN LOS 160 ULTIMOS")))
w("")

w("=== B.2 LAS TRES VUELTAS QUE CIERRAN SU PROPIO REPORTE, QUE SON EL")
w("       DISPARADOR DE SALIDA DE LA 6.2. MEDIDAS EN GIT Y NO RECORDADAS ===")
w("(el acta 190 nombra 56ec2696, 7302573f y f973b0bd como los cierres, y")
w(" 9a06b7c8, 564a82f9 y 63d0c5b4 como los archivados. AQUI NO SE COPIAN:")
w(" se buscan por su asunto y se publica el hash que salga)")
for etiqueta, aguja in (("cierre 187", "VUELTA 187, EL REPORTE CERRADO"),
                        ("cierre 188", "VUELTA 188, EL REPORTE CERRADO"),
                        ("cierre 189", "VUELTA 189, EL REPORTE CERRADO"),
                        ("archivado 187", "VUELTA 187 CERRADA"),
                        ("archivado 188", "VUELTA 188 CERRADA"),
                        ("archivado 189", "VUELTA 189 CERRADA")):
    hits = [l for l in logtodo.splitlines() if aguja.upper() in l.upper()]
    w("   %-16s -> %s"
      % (etiqueta, (hits[0][:120] if hits else "NO LOCALIZADO")))
for r in ("docs/loop/SALIDA_V187_CERRAR_REPORTE.txt",
          "docs/loop/SALIDA_V188_CERRAR_REPORTE.txt",
          "docs/loop/SALIDA_V189_CERRAR_REPORTE.txt"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if not os.path.exists(p):
        w("   %s -> NO EXISTE" % r)
        continue
    sd, sl, bd, bl = sha_de(p)
    w("   %s -> disco %d bytes | LF %d bytes" % (r, bd, bl))
    for i, l in enumerate(io.open(p, encoding="utf-8").read()
                          .replace(chr(13) + NL, NL).split(NL), 1):
        if "CIFRA piezas que faltan" in l or l.startswith("EXITCODE"):
            w("      LINEA %d: %s" % (i, l.strip()))
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

w("=== G. EL SELLO DEL AUDITOR, MEDIDO Y NO CREIDO ===")
w("(el acta 190 publica 765 / 41948 / 37856 y 411 puestos excluidos. AQUI NO SE")
w(" COPIA NINGUNA: se computan y se comparan, y se publican LAS DOS)")
ruta_sello = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_%s.json" % SELLO_POR_REGLA)
if not os.path.exists(ruta_sello):
    w("   NO EXISTE %s" % ruta_sello)
else:
    sd, sl, bd, bl = sha_de(ruta_sello)
    w("   docs/loop/SELLO_APERTURA_AUDITOR_%s.json -> disco %d bytes | LF %d bytes"
      % (SELLO_POR_REGLA, bd, bl))
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


ciega190 = puestos_de("docs/loop/_auditor_v190_ciega_blind.txt")
destape190 = puestos_de("docs/loop/_auditor_v190_ciega_reveal.txt")
ciega189b = puestos_de("docs/loop/_auditor_v189b_ciega_blind.txt")
w("   ciega del acta 190 (_auditor_v190_ciega_blind.txt): %d puestos distintos"
  % len(ciega190))
w("      %s" % ", ".join(str(x) for x in ciega190))
w("   destape del acta 190: %d puestos distintos" % len(destape190))
w("   CIEGA DEL ACTA 189 (_auditor_v189b_ciega_blind.txt), QUE ES EL TRAMO QUE")
w("   LA TAREA 4 TIENE QUE RELEER AL DOBLE: %d puestos distintos" % len(ciega189b))
w("      %s" % ", ".join(str(x) for x in ciega189b))
w("   EL PUESTO 2422, QUE EL ACTA 189 ENCONTRO DISCREPANTE FUERA DE SUS DUDOSOS:")
w("      %s de la ciega del acta 189" % ("DENTRO" if 2422 in ciega189b else "FUERA"))
w("      %s de la ciega del acta 190" % ("DENTRO" if 2422 in ciega190 else "FUERA"))
for etiqueta, ruta_x in (("exclusion del acta 190",
                          "docs/loop/_auditor_v190_exclusion.txt"),
                         ("exclusion del acta 189",
                          "docs/loop/_auditor_v189b_exclusion.txt")):
    p = os.path.join(RAIZ, ruta_x.replace("/", os.sep))
    if not os.path.exists(p):
        w("   %s: NO EXISTE (%s)" % (etiqueta, ruta_x))
        continue
    crudo = io.open(p, encoding="utf-8").read()
    ex = sorted(set(int(x) for x in re.findall(r"\d+", crudo)))
    w("   %s: %d puestos distintos (%s)" % (etiqueta, len(ex), ruta_x))
    w("      SOLAPE con la ciega del acta 190: %d" % len(set(ciega190) & set(ex)))
    w("      SOLAPE con la ciega del acta 189: %d" % len(set(ciega189b) & set(ex)))
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

w("=== H.1 LA SERIE DE REGISTROS, LLAMADA Y NO TECLEADA (TAREA 1) ===")
w("(el encargo dice que HOY el siguiente libre es R.52, y dice tambien que lo")
w(" diga el instrumento y no el encargo. Aqui se llama al instrumento)")
try:
    import serie_de_registros as SER
    halladas = SER.entradas()
    w("   CIFRA entradas de la serie: %d" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SER.colisiones(halladas)), len(SER.huecos(halladas))))
    w("   SIGUIENTE LIBRE, LLAMADO Y NO TECLEADO: R.%d"
      % SER.siguiente_libre(halladas))
    w("   el encargo dice R.52 -> %s"
      % ("CALZA" if SER.siguiente_libre(halladas) == 52 else "NO CALZA"))
    for numero, rel_, linea, titulo in halladas[-3:]:
        w("   ULTIMOS: R.%s en %s:%d -> %s" % (numero, rel_, linea, titulo[:110]))
except Exception as e:
    w("   NO SE PUDO RECOMPUTAR LA SERIE: %r" % (e,))
w("")

w("=== H.2 EL ACTA 190, ACOTADA, Y SUS SECCIONES ===")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
t_acta = io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
lin_acta = t_acta.split(NL)
CAB = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA
cab = [i for i, l in enumerate(lin_acta, 1) if l.startswith(CAB)]
w("   docs/loop/ACTA_AUDITOR.md -> %d lineas por split | %d saltos de linea | "
  "disco %d bytes" % (len(lin_acta), t_acta.count(NL), os.path.getsize(ACTA)))
w("   (LAS DOS CONVENCIONES DE `lineas`, QUE ES EL HALLAZGO 5.1 DEL ACTA 190:")
w("    len(texto.split(NL)) da %d y texto.count(NL) da %d. Se publican LAS DOS)"
  % (len(lin_acta), t_acta.count(NL)))
w("   CIFRA cabeceras %r: %d (lineas %s)"
  % (CAB, len(cab), ", ".join(str(x) for x in cab) or "ninguna"))
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
    w("   LAS CLAVES `5.n` DE LA SECCION 5, CON LOS DOS PATRONES:")
    p5_con = re.compile(r"^\s*\*\*`5\.(\d+)`")
    p5_sin = re.compile(r"^\s*\*\*5\.(\d+)\b")
    for nombre, pat in (("CON comillas inversas", p5_con),
                        ("SIN comillas inversas", p5_sin)):
        hits = [(i, pat.match(lin_acta[i - 1]).group(1))
                for i in range(ini, fin + 1) if pat.match(lin_acta[i - 1])]
        w("      %s -> %d (%s)"
          % (nombre, len(hits), ", ".join("5.%s@%d" % (n, i) for i, n in hits)))
    w("   LAS MARCAS DE SENTIDO EN LOS TITULOS `4.n`, CONTADAS Y NO SUPUESTAS:")
    w("   (el encargo dice CINCO A FAVOR y UNO EN CONTRA. Aqui se cuenta)")
    for i in range(ini, fin + 1):
        if p_sin.match(lin_acta[i - 1]):
            l = lin_acta[i - 1].strip()
            marcas = []
            if "EN CONTRA" in l:
                marcas.append("EN CONTRA")
            if re.search(r"\bA FAVOR\b", l):
                marcas.append("A FAVOR")
            w("      LINEA %-6d %s" % (i, l[:118]))
            w("               marcas literales: %s" % (", ".join(marcas) or "(ninguna)"))
    w("   LAS CAIDAS `C.n`, CON LA CABECERA DE SU SECCION:")
    p_c = re.compile(r"^\s*(?:-\s+)?\*\*`?C\.(\d+)`?[,.\s]")
    n_c = 0
    for i in range(ini, fin + 1):
        m = p_c.match(lin_acta[i - 1])
        if not m:
            continue
        n_c += 1
        cabec = ""
        for j in range(i, ini - 1, -1):
            if lin_acta[j - 1].startswith("## "):
                cabec = lin_acta[j - 1]
                break
        w("      LINEA %-6d C.%s bajo %r" % (i, m.group(1), cabec[:90]))
    w("      CIFRA C.n con patron de cabeza de linea: %d" % n_c)
    w("   LAS FRASES DE CERO Y DE ATRIBUCION DE LA SECCION 6, LITERALES:")
    for i in range(ini, fin + 1):
        l = lin_acta[i - 1]
        if ("DEL EJECUTOR" in l.upper() or "MIAS: CERO" in l.upper()
                or l.startswith("## 6.")):
            w("      LINEA %-6d %s" % (i, l.strip()[:118]))
w("")

w("=== H.3 LA GUARDA DEL SUJETO CONGELADO, MEDIDA AL ENTRAR (TAREA 2) ===")
w("(el encargo nombra TRES entradas y dice EXPRESAMENTE: mide cuantas de las tres")
w(" traen motivo escrito, no lo supongas. Aqui se mide el estado DE ENTRADA)")
try:
    import verificar_mutaciones_viejas as VMV
    malas = VMV.guarda_del_sujeto_congelado()
    w("   CIFRA len(VMV.VIEJAS) (la nomina): %d" % len(VMV.VIEJAS))
    w("   VARA_DEL_CENSO: %d" % VMV.VARA_DEL_CENSO)
    w("   guarda_del_sujeto_congelado(): %d entradas sin congelar" % len(malas))
    for nombre, veredicto, vive in malas:
        w("      %-14s %-52s abre: %s"
          % (veredicto, nombre, ", ".join(vive) or "(nada)"))
    w("   LAS TRES QUE EL ENCARGO NOMBRA, COTEJADAS UNA A UNA CONTRA LA MEDICION:")
    nombres_medidos = [n for n, _v, _vv in malas]
    for n in LAS_TRES_SIN_CONGELAR:
        w("      %-52s en la medicion de hoy: %s"
          % (n, "SI" if n in nombres_medidos else "NO"))
    w("   CIFRA de las tres del encargo que la medicion de hoy confirma: %d de %d"
      % (len([n for n in LAS_TRES_SIN_CONGELAR if n in nombres_medidos]),
         len(LAS_TRES_SIN_CONGELAR)))
    w("   Y LA FIRMA DE guarda_del_sujeto_congelado() HOY, para que se vea que NO")
    w("   SEPARA NADA todavia: devuelve tuplas de %d campos (nombre, veredicto,"
      % (len(malas[0]) if malas else -1))
    w("   vive), sin ninguna cifra de motivo escrito.")
    w("   arneses_que_faltan() HOY: %s" % (VMV.arneses_que_faltan(),))
    w("   nomina_invisible_al_censo() HOY: %s" % (VMV.nomina_invisible_al_censo(),))
except Exception as e:
    w("   NO SE PUDO LLAMAR: %r" % (e,))
w("")

w("=== H.4 LAS TRES SALIDAS SELLADAS QUE LA BATERIA DE LA 189 PISO (TAREA 3) ===")
w("(el acta 190 dice en su 4.9 que las restauro una persona a mano, en dos")
w(" vueltas distintas y a dos personas distintas. Aqui se mide como estan HOY)")
for r in SELLADAS_PISADAS:
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    g = bytes_de_git(r)
    if not os.path.exists(p):
        w("   %s -> NO EXISTE EN DISCO | git %s"
          % (r, ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
        continue
    sd, sl, bd, bl = sha_de(p)
    w("   %s" % r)
    w("      disco %d bytes | LF %d bytes | git %s | sha256 LF %s"
      % (bd, bl, ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD", sl[:16]))
    w("      LOS RETORNOS DE CARRO: %d (la casa escribe en LF en disco)"
      % (bd - bl))
w("")

w("=== H.5 EL LANZADOR DE LA BATERIA DE LA 189, MEDIDO SIN CORRERLO (TAREA 3) ===")
w("(ESTA VUELTA NO CORRE LA BATERIA. Aqui NO se llama a --plan ni a --siguiente")
w(" ni a --componer: se mide el fichero, que es lo que se puede medir sin correr")
w(" un solo arnes. La 189 corrio y sello sus diez tramos; la siguiente es la 194)")
LANZ = os.path.join(RAIZ, "scripts", "loop", "vuelta189_bateria_por_tramos.py")
if os.path.exists(LANZ):
    sd, sl, bd, bl = sha_de(LANZ)
    t_l = io.open(LANZ, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("   scripts/loop/vuelta189_bateria_por_tramos.py -> disco %d bytes | "
      "LF %d bytes | saltos de linea %d" % (bd, bl, t_l.count(NL)))
    w("   sha256 LF: %s" % sl)
    for i, l in enumerate(t_l.split(NL), 1):
        if ("sys.exit" in l or "return 1" in l or "returncode" in l
                or "RESTAURA" in l.upper()):
            w("      LINEA %-5d %s" % (i, l.strip()[:112]))
w("   LOS DIEZ TRAMOS DE LA 189, EN DISCO, MEDIDOS Y NO CREIDOS:")
n_tr = 0
for i in range(1, 21):
    r = "docs/loop/SALIDA_V189_BATERIA_TRAMO_%d.txt" % i
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if not os.path.exists(p):
        continue
    n_tr += 1
    sd, sl, bd, bl = sha_de(p)
    w("      %s -> disco %d bytes | LF %d bytes | sha256 LF %s" % (r, bd, bl, sl[:16]))
w("      CIFRA tramos de la 189 en disco: %d" % n_tr)
w("   EL EXITCODE QUE EL ACTA 190 DICE QUE SALIO EN LOS DIEZ, BUSCADO EN SUS")
w("   PROPIAS SALIDAS SELLADAS (no se copia del acta, se cuenta del fichero):")
con_exit1 = 0
con_no_mordio = 0
for i in range(1, n_tr + 1):
    p = os.path.join(LOOP, "SALIDA_V189_BATERIA_TRAMO_%d.txt" % i)
    if not os.path.exists(p):
        continue
    t = io.open(p, encoding="utf-8", errors="replace").read()
    e1 = bool(re.search(r"EXITCODE:\s*1\b", t))
    nm = bool(re.search(r"CIFRA NO MORDIO:\s*([1-9]\d*)", t))
    con_exit1 += 1 if e1 else 0
    con_no_mordio += 1 if nm else 0
    w("      tramo %-2d -> `EXITCODE: 1`: %-3s | `CIFRA NO MORDIO:` mayor que 0: %s"
      % (i, "SI" if e1 else "no", "SI" if nm else "no"))
w("      CIFRA tramos con `EXITCODE: 1`: %d de %d" % (con_exit1, n_tr))
w("      CIFRA tramos con algun NO MORDIO: %d de %d" % (con_no_mordio, n_tr))
w("")

w("=== H.6 EL ARCHIVO DE VEREDICTOS, QUE ESTA VUELTA NO MUEVE ===")
w("(el acta 190 da 0a77b5a35a962621 como sha256 LF. NO SE COPIA)")
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
w("   LA FILA DEL PUESTO 2422, QUE ES EL SUJETO DE LA TAREA 4, SIN ABRIR SU")
w("   CLASE: solo se dice que existe y cuantas veces aparece.")
w("      CIFRA filas con puesto_intra 2422: %d"
  % len([f for f in filas_v if f.get("puesto_intra") == 2422]))
w("")

w("=== H.7 LA FICHA OP-L-02, LOCALIZADA SIN INTERPRETARLA (TAREA 5) ===")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
if os.path.exists(OPS):
    sd, sl, bd, bl = sha_de(OPS)
    w("   docs/plan/OPERACIONES.jsonl -> disco %d bytes | LF %d bytes" % (bd, bl))
    fichas = []
    for i, l in enumerate(io.open(OPS, encoding="utf-8"), 1):
        if not l.strip():
            continue
        try:
            d = json.loads(l)
        except Exception:
            continue
        fichas.append((i, d))
    w("   CIFRA fichas: %d" % len(fichas))
    hit = [(i, d) for i, d in fichas
           if str(d.get("id") or d.get("operacion") or "") == "OP-L-02"]
    w("   CIFRA fichas con id OP-L-02: %d" % len(hit))
    for i, d in hit:
        w("      LINEA %d del fichero" % i)
        for k in sorted(d):
            v = d[k]
            v = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
            w("         %-16s %s" % (k, v[:600]))
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
