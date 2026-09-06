# -*- coding: utf-8 -*-
r"""vuelta191_apertura.py . EL SELLO DE APERTURA DE LA VUELTA 191, QUE NO ES
VUELTA DE BATERIA Y LLEVA CINCO SUB-TAREAS.

POR QUE EXISTE: `EJECUTOR.md` 1, "LA APERTURA SE MIDE ANTES DE LA PRIMERA
OPERACION". Este fichero corre ANTES de tocar nada y deja escrito en disco el
estado del arbol, de las rutas que el encargo nombra y de los sujetos que las
CINCO tareas van a mover. Ninguna cifra del encargo se copia: TODAS se computan
aqui y se comparan con lo que el encargo dice, publicando LAS DOS.

CLON DECLARADO de scripts/loop/vuelta190_apertura.py. Cambia el numero de vuelta,
la lista de SUJETOS y de RUTAS_DEL_ENCARGO, los bloques H.n (que miden lo que
ESTA vuelta va a mover y no lo que movia la 190) y este docstring. El cotejo del
clon lo hace scripts/loop/cotejar_clon_declarado.py y su salida se pega en el
reporte con lo que salga: AQUI NO SE AFIRMA QUE NINGUN DIFF SALGA VACIO.

EL SELLO DEL AUDITOR DE ESTA VUELTA ES `V191` Y NO SE DEDUCE A OJO: el acta 191
lo declara en su propia cabecera (`SELLO_APERTURA_AUDITOR_V191.json`, prefijo
`_auditor_v191_*`). Aqui se mide, no se cree.

Y ESTE FICHERO MIDE EL DESFASE DEL CALIBRADO EN LA APERTURA, no al cierre: una
columna de apertura medida al cierre es caida que ACUMULA (`EJECUTOR.md` 1).

LO QUE ESTE FICHERO NO HACE: no escribe el reporte, no toca `dataset/` a mano, no
toca ningun veredicto, NO CORRE NINGUN ARNES, NO CORRE LA BATERIA (la 191 NO es
vuelta de bateria: la siguiente cae en la 194) y no registra ninguna acta. Mide y
escribe SALIDA_V191_*.txt.

USO:
  python scripts/loop/vuelta191_apertura.py
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
    "scripts/loop/serie_de_registros.py",
    "scripts/loop/vuelta190_tarea1a_registrar_acta190.py",
    "scripts/loop/vuelta189_tarea1a_registrar_acta189.py",
    "scripts/loop/aislador_de_ciega.py",
    "scripts/loop/vuelta182_tarea1c_relectura_al_doble.py",
    "scripts/loop/vuelta190_tarea4_relectura_al_doble.py",
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/tallar_cabecera_reporte.py",
    "scripts/loop/anexar_tarea_al_reporte.py",
    "scripts/loop/cotejar_clon_declarado.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/vuelta150_3_relectura_expediente.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/SELLO_APERTURA_AUDITOR_V191.json",
    "docs/loop/_auditor_v191_ciega_blind.txt",
    "docs/loop/_auditor_v191_ciega_reveal.txt",
    "docs/loop/_auditor_v191_mis_clases.txt",
    "docs/loop/_auditor_v191_cotejo_ciega.txt",
    "docs/loop/_auditor_v191_marcas.txt",
    "docs/loop/_auditor_v191_vara.txt",
    "docs/loop/_auditor_v190_ciega_blind.txt",
    "docs/loop/_auditor_v190_exclusion.txt",
    "docs/loop/_auditor_v189b_ciega_blind.txt",
    "docs/loop/_auditor_v189b_exclusion.txt",
    "docs/loop/SALIDA_V190_APERTURA.txt",
    "docs/loop/SALIDA_V190_CERRAR_REPORTE.txt",
    "docs/loop/SALIDA_V190_TALLADOR_CABECERA.txt",
    "docs/loop/SALIDA_V190_T4_CIEGA.txt",
    "docs/loop/SALIDA_V190_T4_DESTAPE.txt",
    "docs/loop/SALIDA_V190_T4_MIS_CLASES.txt",
    "docs/loop/SALIDA_V190_T4_COTEJO.txt",
    "docs/loop/reportes/REPORTE_V186.md",
    "docs/loop/reportes/REPORTE_V187.md",
    "docs/loop/reportes/REPORTE_V188.md",
    "docs/loop/reportes/REPORTE_V189.md",
    "docs/loop/reportes/REPORTE_V190.md",
    "docs/PENDIENTES.md",
    "docs/plan/CORRECCIONES_A_APLICAR.md",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/BANCO_DEL_PLAN.md",
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "docs/BANCO_DE_TEXTOS.md",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
] + SUJETOS

# LO QUE LA TAREA 2 VA A CONSUMIR, NOMBRADO POR FICHEROS Y NO POR CIFRAS. El
# encargo dice 471; aqui se cuentan de sus ficheros y se publican LAS DOS.
UNIVERSO_CONSUMIDO = [
    "docs/loop/_auditor_v190_exclusion.txt",
    "docs/loop/_auditor_v189b_exclusion.txt",
    "docs/loop/_auditor_v190_ciega_blind.txt",
    "docs/loop/_auditor_v189b_ciega_blind.txt",
    "docs/loop/SALIDA_V190_T4_CIEGA.txt",
]


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
w("         HUECO DECLARADO Y MEDIDO por su carril. CINCO SUB-TAREAS, con el tope")
w("         de cinco vigente desde la 4.10 del acta 190.")
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

w("=== B.1 LA CADENA DE LA VUELTA 190, LOCALIZADA EN GIT Y NO TECLEADA ===")
c, logtodo = git(["log", "--format=%h%x09%s", "-200"])
for etiqueta, aguja in (("acta 190", "ACTA DEL AUDITOR, VUELTA 190"),
                        ("acta 191", "ACTA DEL AUDITOR, VUELTA 191"),
                        ("clases del auditor 191", "AUDITOR V191: MIS CLASES"),
                        ("tarea 4 de la 190", "VUELTA 190, TAREA 4"),
                        ("cierre de la 190", "VUELTA 190, EL REPORTE CERRADO"),
                        ("archivado de la 190", "VUELTA 190 CERRADA")):
    hits = [l for l in logtodo.splitlines() if aguja.upper() in l.upper()]
    w("   %-24s -> %s"
      % (etiqueta, (hits[0][:150] if hits else "NO LOCALIZADO EN LOS 200 ULTIMOS")))
w("")

w("=== B.2 LAS VUELTAS QUE CIERRAN SU PROPIO REPORTE. EL ENCARGO DICE CUATRO")
w("       (187, 188, 189 Y 190). AQUI NO SE COPIA: SE BUSCAN EN GIT Y SE CUENTAN,")
w("       Y SE MIDE ADEMAS SU FICHERO DE CIERRE ===")
n_cierres = 0
for v in (186, 187, 188, 189, 190):
    aguja = "VUELTA %d, EL REPORTE CERRADO" % v
    hits = [l for l in logtodo.splitlines() if aguja.upper() in l.upper()]
    w("   cierre %d -> %s" % (v, (hits[0][:110] if hits else "NO LOCALIZADO")))
for v in (186, 187, 188, 189, 190):
    r = "docs/loop/SALIDA_V%d_CERRAR_REPORTE.txt" % v
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if not os.path.exists(p):
        w("   %s -> NO EXISTE" % r)
        continue
    sd, sl, bd, bl = sha_de(p)
    t = io.open(p, encoding="utf-8", errors="replace").read().replace(chr(13) + NL, NL)
    faltan = [l for l in t.split(NL) if "CIFRA piezas que faltan" in l]
    ex = [l for l in t.split(NL) if l.startswith("EXITCODE")]
    ok = bool(faltan) and faltan[0].strip().endswith("0")
    n_cierres += 1 if ok else 0
    w("   %s -> disco %d bytes | LF %d bytes | %s | %s"
      % (r, bd, bl, (faltan[0].strip() if faltan else "(sin la linea de piezas)"),
         (ex[0].strip() if ex else "(sin EXITCODE)")))
w("   CIFRA ficheros de cierre con `CIFRA piezas que faltan: 0`: %d" % n_cierres)
w("   el encargo dice CUATRO vueltas seguidas (187, 188, 189 y 190). Lo que este")
w("   bloque cuenta de disco son %d ficheros de cierre en verde, de los cinco" % n_cierres)
w("   mirados (186 a 190). LAS DOS CIFRAS SE PUBLICAN Y NINGUNA SE RESUELVE")
w("   COPIANDO.")
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
w("(el acta 191 publica 1003 bytes de sello, ciega 39924 y destape 32062. AQUI NO")
w(" SE COPIA NINGUNA: se computan y se comparan, y se publican LAS DOS)")
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

PAT_PUESTO = re.compile(r"puesto_intra[^0-9]{0,12}(\d+)")


def puestos_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.exists(p):
        return []
    t = io.open(p, encoding="utf-8", errors="replace").read()
    return sorted(set(int(x) for x in PAT_PUESTO.findall(t)))


def numeros_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.exists(p):
        return []
    t = io.open(p, encoding="utf-8", errors="replace").read()
    return sorted(set(int(x) for x in re.findall(r"\d+", t)))


w("=== H. EL REPORTE EN HEAD, MEDIDO SIN CREERLE AL ENCARGO ===")
REP = os.path.join(LOOP, "REPORTE.md")
if os.path.exists(REP):
    sd, sl, bd, bl = sha_de(REP)
    t_rep = io.open(REP, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("   primera linea: %s" % t_rep.split(NL)[0])
    w("   disco %d bytes | LF %d bytes | saltos de linea %d | sha256 LF %s"
      % (bd, bl, t_rep.count(NL), sl))
    w("   LAS DOS CONVENCIONES DE `lineas` SOBRE ESTE MISMO FICHERO, QUE ES LA")
    w("   TAREA 3: len(texto.split(NL)) da %d y texto.count(NL) da %d"
      % (len(t_rep.split(NL)), t_rep.count(NL)))
    n9 = [i for i, l in enumerate(t_rep.split(NL), 1) if l.startswith("## 9.")]
    w("   CIFRA secciones `## 9.`: %d, en las lineas %s"
      % (len(n9), ", ".join(str(x) for x in n9) or "(ninguna)"))
w("")

w("=== H.1 LA SERIE DE REGISTROS, LLAMADA Y NO TECLEADA (TAREA 1) ===")
w("(el encargo dice que HOY el siguiente libre es R.53, y dice tambien que lo")
w(" diga el instrumento y no el encargo. Aqui se llama al instrumento)")
try:
    import serie_de_registros as SER
    halladas = SER.entradas()
    w("   CIFRA entradas de la serie: %d" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SER.colisiones(halladas)), len(SER.huecos(halladas))))
    w("   SIGUIENTE LIBRE, LLAMADO Y NO TECLEADO: R.%d"
      % SER.siguiente_libre(halladas))
    w("   el encargo dice R.53 -> %s"
      % ("CALZA" if SER.siguiente_libre(halladas) == 53 else "NO CALZA"))
    for numero, rel_, linea, titulo in halladas[-3:]:
        w("   ULTIMOS: R.%s en %s:%d -> %s" % (numero, rel_, linea, titulo[:110]))
except Exception as e:
    w("   NO SE PUDO RECOMPUTAR LA SERIE: %r" % (e,))
w("")

w("=== H.2 EL ACTA 191, ACOTADA, Y SUS SECCIONES (TAREA 1) ===")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
t_acta = io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
lin_acta = t_acta.split(NL)
CAB = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA
cab = [i for i, l in enumerate(lin_acta, 1) if l.startswith(CAB)]
w("   docs/loop/ACTA_AUDITOR.md -> %d lineas por split | %d saltos de linea | "
  "disco %d bytes" % (len(lin_acta), t_acta.count(NL), os.path.getsize(ACTA)))
w("   (LAS DOS CONVENCIONES DE `lineas`, QUE ES LA TAREA 3 DE ESTA VUELTA:")
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
    w("   (el encargo dice NUEVE A FAVOR y CERO EN CONTRA. Aqui se cuenta, y el")
    w("    cero de EN CONTRA es justo lo que la maquina de la 190 no sabe leer")
    w("    sin romperse)")
    n_favor = n_contra = 0
    for i in range(ini, fin + 1):
        if p_sin.match(lin_acta[i - 1]):
            l = lin_acta[i - 1].strip()
            marcas = []
            if "EN CONTRA" in l:
                marcas.append("EN CONTRA")
                n_contra += 1
            if re.search(r"\bA FAVOR\b", l):
                marcas.append("A FAVOR")
                n_favor += 1
            w("      LINEA %-6d %s" % (i, l[:118]))
            w("               marcas literales: %s" % (", ".join(marcas) or "(ninguna)"))
    w("      CIFRA titulos `4.n` con A FAVOR: %d | con EN CONTRA: %d"
      % (n_favor, n_contra))
    w("   LAS CAIDAS, MEDIDAS CON LOS DOS PATRONES, PORQUE EL ACTA 191 NO USA `C.n`:")
    p_c = re.compile(r"`C\.(\d+)`")
    p_nm = re.compile(r"`(\d+\.\d+)`")
    r6 = [i for i in range(ini, fin + 1) if lin_acta[i - 1].startswith("## 6.")]
    if r6:
        ini6 = r6[0]
        tope6 = fin
        for i in range(ini6 + 1, fin + 1):
            if lin_acta[i - 1].startswith("## "):
                tope6 = i - 1
                break
        w("      la seccion 6 va de la linea %d a la %d" % (ini6, tope6))
        cs = set()
        nms = set()
        for i in range(ini6, tope6 + 1):
            cs |= set(p_c.findall(lin_acta[i - 1]))
            nms |= set(p_nm.findall(lin_acta[i - 1]))
            if lin_acta[i - 1].strip():
                w("      LINEA %-6d %s" % (i, lin_acta[i - 1].strip()[:118]))
        w("      CIFRA claves `C.n` distintas en la seccion 6: %d (%s)"
          % (len(cs), ", ".join(sorted(cs)) or "ninguna"))
        w("      CIFRA claves `N.M` distintas en la seccion 6: %d (%s)"
          % (len(nms), ", ".join(sorted(nms)) or "ninguna"))
    w("   LA TABLA DE CREDITO DE LA SECCION 7, PEGADA ENTERA (TAREA 1):")
    r7 = [i for i in range(ini, fin + 1) if lin_acta[i - 1].startswith("## 7.")]
    if r7:
        ini7 = r7[0]
        tope7 = fin
        for i in range(ini7 + 1, fin + 1):
            if lin_acta[i - 1].startswith("## "):
                tope7 = i - 1
                break
        for i in range(ini7, tope7 + 1):
            if lin_acta[i - 1].strip():
                w("      LINEA %-6d %s" % (i, lin_acta[i - 1].strip()[:150]))
w("")

w("=== H.3 EL TRAMO Y EL UNIVERSO DE LA TAREA 2, CONTADOS DE SUS FICHEROS ===")
w("(el encargo dice 30 del tramo, 441 de antes de la 190 y 471 con los 30 de la")
w(" 190 dentro. AQUI NO SE COPIA NINGUNA: se cuentan de sus ficheros)")
tramo = puestos_de("docs/loop/SALIDA_V190_T4_CIEGA.txt")
w("   TRAMO (docs/loop/SALIDA_V190_T4_CIEGA.txt): %d puestos distintos" % len(tramo))
w("      %s" % ", ".join(str(x) for x in tramo))
w("   EL PUESTO 3182, QUE ES EL QUE CAYO FUERA DE LOS DUDOSOS: %s del tramo"
  % ("DENTRO" if 3182 in tramo else "FUERA"))
ciega191 = puestos_de("docs/loop/_auditor_v191_ciega_blind.txt")
w("   LA CIEGA DEL AUDITOR EN EL ACTA 191: %d puestos distintos" % len(ciega191))
w("   ES EL MISMO CONJUNTO QUE EL TRAMO: %s"
  % ("SI" if set(ciega191) == set(tramo) else
     "NO, difieren en %d" % len(set(ciega191) ^ set(tramo))))
antes = set()
todo = set()
for rel in UNIVERSO_CONSUMIDO:
    nums = numeros_de(rel) if "exclusion" in rel else puestos_de(rel)
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    bd = os.path.getsize(p) if os.path.exists(p) else -1
    todo |= set(nums)
    if "SALIDA_V190_T4_CIEGA" not in rel:
        antes |= set(nums)
    w("   %-48s %7d bytes | %4d numeros" % (rel, bd, len(nums)))
w("   CIFRA union SIN los 30 de la tanda de la 190: %d (el encargo dice 441)"
  % len(antes))
w("   CIFRA union CON los 30 de la tanda de la 190: %d (el encargo dice 471)"
  % len(todo))
w("   SOLAPE del tramo con la union de antes: %d" % len(set(tramo) & antes))
w("")

w("=== H.4 LAS DOS CONVENCIONES DE `lineas` EN scripts/loop/, MEDIDAS AL ENTRAR")
w("       (TAREA 3). AQUI SOLO SE CUENTA: EL ARREGLO ES DE LA TAREA ===")
PAT_SPLIT = re.compile(r"len\(\s*[A-Za-z_][A-Za-z0-9_\.\[\]\(\)]*\s*\.split\(")
PAT_COUNT = re.compile(r"\.count\(\s*NL\s*\)|\.count\(\s*chr\(10\)\s*\)")
dir_loop = os.path.join(RAIZ, "scripts", "loop")
con_split = []
con_count = []
n_py = 0
for nombre in sorted(os.listdir(dir_loop)):
    if not nombre.endswith(".py"):
        continue
    n_py += 1
    t = io.open(os.path.join(dir_loop, nombre), encoding="utf-8",
                errors="replace").read()
    if PAT_SPLIT.search(t):
        con_split.append(nombre)
    if PAT_COUNT.search(t):
        con_count.append(nombre)
w("   CIFRA ficheros .py en scripts/loop/: %d" % n_py)
w("   CIFRA con el patron de `len(...split(...))`: %d" % len(con_split))
w("   CIFRA con el patron de `.count(NL)`: %d" % len(con_count))
w("   CIFRA con LOS DOS: %d" % len(set(con_split) & set(con_count)))
w("   (esta es la medicion DE ENTRADA y con un patron GRUESO: la de la tarea 3")
w("    tiene que ser mas estrecha y nombrar los ficheros uno a uno)")
w("")

w("=== H.5 LA ETIQUETA DEL VEREDICTO, MEDIDA EN LOS REPORTES ARCHIVADOS")
w("       (TAREA 4). El acta 191 dice que la 190 la trae DOS veces y que los")
w("       reportes 186 a 189 la traen UNA. AQUI SE CUENTA DE CADA FICHERO ===")
AGUJA_VER = "EL VEREDICTO DE UNA LINEA:"
for v in (186, 187, 188, 189, 190):
    r = "docs/loop/reportes/REPORTE_V%d.md" % v
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if not os.path.exists(p):
        w("   %s -> NO EXISTE" % r)
        continue
    t = io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    lineas_ver = [(i, l) for i, l in enumerate(t.split(NL), 1) if AGUJA_VER in l]
    w("   %s -> CIFRA apariciones del literal %r: %d"
      % (r, AGUJA_VER, t.count(AGUJA_VER)))
    for i, l in lineas_ver:
        w("      LINEA %-5d apariciones en la linea: %d" % (i, l.count(AGUJA_VER)))
        w("         %s" % l.strip()[:150])
CR = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
t_cr = io.open(CR, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("   scripts/loop/cerrar_reporte.py -> %d saltos de linea | disco %d bytes"
  % (t_cr.count(NL), os.path.getsize(CR)))
for i, l in enumerate(t_cr.split(NL), 1):
    if AGUJA_VER in l or "a.veredicto" in l or "VEREDICTO_VIEJO" in l:
        w("      LINEA %-5d %s" % (i, l.strip()[:130]))
w("")

w("=== H.6 EL ARCHIVO DE VEREDICTOS, QUE ESTA VUELTA NO MUEVE ===")
w("(el acta 191 da 0a77b5a35a962621 como sha256 LF. NO SE COPIA)")
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

w("=== H.7 LA MARCA `DISCUTIBLE MARCADO`, CONTADA DEL ARCHIVO (TAREA 5) ===")
w("(el acta 191 publica 427 de 3.388, el 12,6 por ciento. NO SE COPIA)")
MARCA = "DISCUTIBLE MARCADO"
con_marca = [f for f in filas_v if MARCA in str(f.get("razon", ""))]
w("   CIFRA filas con %r en su `razon`: %d de %d" % (MARCA, len(con_marca), len(filas_v)))
w("   TASA: %.4f (%.1f por ciento)"
  % (len(con_marca) / float(len(filas_v)), 100.0 * len(con_marca) / len(filas_v)))
w("   LOS OCHO QUE EL ACTA 191 NOMBRA MAS EL 3182, MIRADOS UNO A UNO SIN ABRIR")
w("   SU CLASE:")
porp = {f.get("puesto_intra"): f for f in filas_v}
for p8 in (872, 904, 963, 1201, 1366, 2423, 3067, 3086, 3182):
    f = porp.get(p8)
    w("      puesto %-5d existe: %-3s lleva la marca: %s"
      % (p8, "SI" if f else "NO",
         ("SI" if (f and MARCA in str(f.get("razon", ""))) else "no")))
w("   LOS FICHEROS DE COTEJO DE CIEGA QUE HAY EN docs/loop/, LISTADOS AL ENTRAR:")
n_cot = 0
for nombre in sorted(os.listdir(LOOP)):
    alto = nombre.upper()
    if not nombre.lower().endswith((".txt", ".md")):
        continue
    if "COTEJO" in alto:
        n_cot += 1
        w("      %-52s %8d bytes"
          % (nombre, os.path.getsize(os.path.join(LOOP, nombre))))
w("   CIFRA ficheros con COTEJO en el nombre: %d" % n_cot)
w("   (el universo de la TAREA 5 se declara EN LA TAREA, con su regla escrita")
w("    antes de contar. Esto de aqui es el inventario de entrada y nada mas)")
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
