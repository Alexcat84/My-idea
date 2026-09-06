# -*- coding: utf-8 -*-
r"""vuelta188_apertura.py . EL SELLO DE APERTURA DE LA VUELTA 188.

POR QUE EXISTE: `EJECUTOR.md` 1, "LA APERTURA SE MIDE ANTES DE LA PRIMERA
OPERACION". Este fichero corre ANTES de tocar nada y deja escrito en disco el
estado del arbol, de las rutas que el encargo nombra y de los sujetos que las
cinco tareas van a mover. Ninguna cifra del encargo se copia: TODAS se computan
aqui y se comparan con lo que el encargo dice, publicando LAS DOS.

EL SELLO DEL AUDITOR DE ESTA VUELTA SE LLAMA V189 Y NO SE DEDUCE DEL NUMERO DE
VUELTA A OJO: la casa nombra el sello del acta N como V(N+1), y esta es el acta
188. El V186 no existe y no se fabrica.

LO QUE ESTE FICHERO NO HACE: no escribe el reporte, no toca `dataset/`, no toca
ningun veredicto y no corre la bateria. Mide y escribe SALIDA_V188_*.txt.

USO:
  python scripts/loop/vuelta188_apertura.py
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
SELLO_AUDITOR = "V%d" % (VUELTA + 1)

sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

SUJETOS = [
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/tallar_cabecera_reporte.py",
    "scripts/loop/serie_de_registros.py",
    "scripts/loop/anexar_tarea_al_reporte.py",
    "scripts/loop/cotejar_clon_declarado.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/vuelta150_3_relectura_expediente.py",
    "scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py",
    "scripts/loop/vuelta186_tarea2a_mutacion_pieza4.py",
    "scripts/loop/vuelta186_tarea2b_mutacion_pieza2_cercas.py",
    "scripts/loop/vuelta186_tarea2d_mutacion_seccion4.py",
    "scripts/loop/vuelta187_tarea4_mutacion_dos_convenciones.py",
    "scripts/loop/vuelta187_tarea5b_mutacion_seccion4_tardio.py",
    "scripts/loop/vuelta182_tarea1c_relectura_al_doble.py",
    "scripts/loop/vuelta187_tarea1a_registrar_acta187.py",
    "scripts/loop/vuelta187_esqueleto_reporte.py",
    "scripts/loop/vuelta186_rutas_del_reporte.py",
    "scripts/loop/vuelta187_tarea5a_nomina.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/SELLO_APERTURA_AUDITOR_V189.json",
    "docs/loop/_auditor_v189_ciega_blind.txt",
    "docs/loop/_auditor_v189_ciega_reveal.txt",
    "docs/loop/_auditor_v189_mis_clases.txt",
    "docs/loop/_auditor_v189_exclusion.txt",
    "docs/loop/_auditor_v188_ciega_blind.txt",
    "docs/loop/SALIDA_V187_APERTURA.txt",
    "docs/loop/SALIDA_V187_CERRAR_REPORTE.txt",
    "docs/loop/SALIDA_V187_TALLADOR_CABECERA.txt",
    "docs/loop/SALIDA_V187_T5B_ARNES_SELLADO_186_2C_EN_ROJO.txt",
    "docs/loop/SALIDA_V187_T4_MUTACION_EN_ROJO.txt",
    "docs/loop/SALIDA_V183_BATERIA.txt",
    "docs/loop/reportes/REPORTE_V185.md",
    "docs/loop/reportes/REPORTE_V186.md",
    "docs/loop/reportes/REPORTE_V187.md",
    "docs/PENDIENTES.md",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "docs/plan/INVENTARIO.jsonl",
    "docs/plan/10_INVENTARIO.md",
    "docs/plan/INTRA_DOMINIO_INFORME.md",
    "docs/plan/08_VERIFICACION.md",
    "docs/plan/BANCO_DEL_PLAN.md",
    "docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl",
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
w("El sello del auditor se llama %s: la casa nombra el sello del acta N como"
  % SELLO_AUDITOR)
w("V(N+1) y esta es el acta %d. NO se deduce del numero de vuelta a ojo." % VUELTA)
w("regimen: NO ES VUELTA DE BATERIA. AUDITOR.md 6.1: corre cada cinco vueltas y")
w("         cerro entera en la 184, asi que la siguiente es la 189. La seccion 9")
w("         de este reporte cierra CON EL HUECO DECLARADO Y MEDIDO: nombre,")
w("         bytes y atribucion, las tres juntas o no vale.")
w("         TOPE DE CINCO TAREAS. El regimen temporal de AUDITOR.md 6.2 quedo")
w("         cumplido y apagado; aqui no se da por bueno porque lo diga el")
w("         encargo: el bloque H.0 mide las tres salidas de cierre.")
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

w("=== B.1 LA CADENA DE LA VUELTA 187, LOCALIZADA EN GIT Y NO TECLEADA ===")
c, logtodo = git(["log", "--format=%h%x09%s", "-160"])
for etiqueta, aguja in (("acta 187", "ACTA DEL AUDITOR, VUELTA 187"),
                        ("acta 188", "ACTA DEL AUDITOR, VUELTA 188"),
                        ("tarea 1 de la 187", "VUELTA 187, TAREA 1"),
                        ("tarea 3 de la 187", "VUELTA 187, TAREA 3"),
                        ("tarea 4 de la 187", "VUELTA 187, TAREA 4"),
                        ("tarea 5 de la 187", "VUELTA 187, TAREA 5"),
                        ("cierre de la 187", "VUELTA 187 CERRADA")):
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

w("=== G. EL SELLO DEL AUDITOR %s Y SU COTEJO, COMPUTADO Y NO COPIADO ===" % SELLO_AUDITOR)
w("(el encargo publica 651 / 41098 / 34030 / 6457 / 1648 y 351 puestos. AQUI NO")
w(" SE COPIA NINGUNA: se computan y se comparan, y se publican LAS DOS)")
SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_%s.json" % SELLO_AUDITOR)
ESPERADO_ENCARGO = {
    "docs/loop/SELLO_APERTURA_AUDITOR_%s.json" % SELLO_AUDITOR: 651,
    "docs/loop/_auditor_v%d_ciega_blind.txt" % (VUELTA + 1): 41098,
    "docs/loop/_auditor_v%d_ciega_reveal.txt" % (VUELTA + 1): 34030,
    "docs/loop/_auditor_v%d_mis_clases.txt" % (VUELTA + 1): 6457,
    "docs/loop/_auditor_v%d_exclusion.txt" % (VUELTA + 1): 1648,
}
sello = None
if os.path.exists(SELLO):
    sello = json.load(io.open(SELLO, encoding="utf-8"))
    w("   EL SELLO ENTERO, PEGADO Y NO RESUMIDO:")
    for l in io.open(SELLO, encoding="utf-8").read().replace(chr(13) + NL, NL).split(NL):
        w("      | " + l)
else:
    w("   PARADA POSIBLE: %s NO EXISTE" % SELLO)
w("")
w("   LAS CINCO RUTAS DEL SELLO, MEDIDAS POR LAS DOS CONVENCIONES:")
for r, esperado in sorted(ESPERADO_ENCARGO.items()):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if not os.path.exists(p):
        w("      %s -> NO EXISTE" % r)
        continue
    sd, sl, bd, bl = sha_de(p)
    w("      %s" % r)
    w("         disco %d bytes | LF %d bytes | sha256 LF %s" % (bd, bl, sl))
    w("         el encargo dice %d -> %s (disco) / %s (LF)"
      % (esperado, "CALZA" if bd == esperado else "NO CALZA",
         "CALZA" if bl == esperado else "NO CALZA"))
if sello:
    w("   EL COTEJO CONTRA EL SELLO, COMPUTADO:")
    for clave_r, clave_b, clave_s in (("ciega", "bytes_ciega", "sha256_ciega"),
                                      ("destape", "bytes_destape", "sha256_destape")):
        r = sello[clave_r]
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        sd, sl, bd, bl = sha_de(p)
        w("      %-8s %s" % (clave_r, r))
        w("         bytes: sello %d | disco medido %d -> %s"
          % (sello[clave_b], bd, "CALZA" if sello[clave_b] == bd else "NO CALZA"))
        w("         sha256: sello %s" % sello[clave_s])
        w("                 LF     %s" % sl)
        w("                 -> %s" % ("CALZA" if sello[clave_s] == sl else "NO CALZA"))
w("")

w("=== G.1 LOS PUESTOS DE LA CIEGA Y DE LA EXCLUSION, CONTADOS DE SU FICHERO ===")
PAT_PUESTO = re.compile(r"puesto_intra[^0-9]{0,12}(\d+)")


def puestos_de(ruta):
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    if not os.path.exists(p):
        return []
    t = io.open(p, encoding="utf-8", errors="replace").read()
    return sorted(set(int(x) for x in PAT_PUESTO.findall(t)))


ciega = puestos_de("docs/loop/_auditor_v%d_ciega_blind.txt" % (VUELTA + 1))
destape = puestos_de("docs/loop/_auditor_v%d_ciega_reveal.txt" % (VUELTA + 1))
ciega188 = puestos_de("docs/loop/_auditor_v%d_ciega_blind.txt" % VUELTA)
w("   ciega de hoy: %d puestos distintos" % len(ciega))
w("      %s" % ", ".join(str(x) for x in ciega))
w("   destape de hoy: %d puestos distintos" % len(destape))
w("   ciega de la vuelta anterior (_auditor_v%d_ciega_blind.txt): %d puestos"
  % (VUELTA, len(ciega188)))
EXCL = os.path.join(LOOP, "_auditor_v%d_exclusion.txt" % (VUELTA + 1))
excl = []
if os.path.exists(EXCL):
    crudo = io.open(EXCL, encoding="utf-8").read()
    excl = sorted(set(int(x) for x in re.findall(r"\d+", crudo)))
w("   exclusion: %d puestos distintos (el encargo dice 351 -> %s)"
  % (len(excl), "CALZA" if len(excl) == 351 else "NO CALZA"))
w("   SOLAPE ciega de hoy con la exclusion: %d" % len(set(ciega) & set(excl)))
w("   SOLAPE ciega de hoy con la ciega de la 188: %d" % len(set(ciega) & set(ciega188)))
w("   EL PUESTO 1202, QUE EL ACTA NOMBRA: %s de la ciega de hoy"
  % ("DENTRO" if 1202 in ciega else "FUERA"))
w("")

w("=== H. EL REPORTE EN HEAD, MEDIDO SIN CREERLE AL ENCARGO ===")
REP = os.path.join(LOOP, "REPORTE.md")
if os.path.exists(REP):
    sd, sl, bd, bl = sha_de(REP)
    t_rep = io.open(REP, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("   primera linea: %s" % t_rep.split(NL)[0])
    w("   disco %d bytes | LF %d bytes | saltos de linea %d | sha256 LF %s"
      % (bd, bl, t_rep.count(NL), sl))
    w("   LAS CABECERAS `## ` DEL REPORTE, CON SU LINEA (la C.4 del acta 188):")
    for i, l in enumerate(t_rep.split(NL), 1):
        if l.startswith("## "):
            w("      LINEA %-5d %s" % (i, l[:110]))
    n9 = [i for i, l in enumerate(t_rep.split(NL), 1) if l.startswith("## 9.")]
    w("   CIFRA secciones `## 9.`: %d, en las lineas %s"
      % (len(n9), ", ".join(str(x) for x in n9) or "(ninguna)"))
w("")

w("=== H.0 LAS TRES VUELTAS QUE CIERRAN SU PROPIO REPORTE, MEDIDAS ===")
for r in ("docs/loop/SALIDA_V185_CERRAR_REPORTE.txt",
          "docs/loop/SALIDA_V186_CERRAR_REPORTE.txt",
          "docs/loop/SALIDA_V187_CERRAR_REPORTE.txt"):
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

w("=== H.1 LA VARA DEL PLAN, CORRIDA CON MI PROPIO CORTE (TAREA 2) ===")
w("(el acta 188 punto 12 publica su corrida con --corte 9a06b7c8. AQUI SE VUELVE")
w(" A CORRER con el HEAD de apertura de esta vuelta y NO se copia su cifra)")
c_vara, o_vara = correr([PY, "scripts/loop/vuelta150_3_relectura_expediente.py",
                         "--corte", head])
escribir("T2_VARA", o_vara + NL + "EXITCODE: %d" % c_vara + NL)
for l in o_vara.split(NL):
    if l.startswith("CIFRA ") or "en LISTA sin prueba, de las cuales" in l:
        w("   " + l.strip())
w("   exitcode de la vara: %d" % c_vara)
w("   salida entera en docs/loop/SALIDA_V%s_T2_VARA_APERTURA.txt" % SUFIJO)
w("")

w("=== H.2 LAS CUATRO FICHAS QUE LA VARA NOMBRA, ENTERAS Y CITADAS ===")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
fichas = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
CUATRO = ("OP-L-01", "OP-L-02", "OP-L-03", "OP-I-01")
w("   CIFRA fichas del expediente: %d" % len(fichas))
for f in fichas:
    if f.get("id_op") not in CUATRO:
        continue
    w("   " + "-" * 70)
    for k in ("id_op", "fase", "tipo", "estado", "fecha_corte", "orden"):
        w("   %-18s %s" % (k, f.get(k)))
    for k in ("depende_de", "bloquea_a", "verificacion", "evidencia"):
        v = f.get(k) or []
        w("   %-18s [%d elemento(s)]" % (k, len(v)))
        for j, e in enumerate(v):
            w("      [%d] %s" % (j, str(e)))
    for k in ("adjudicacion", "nota", "pregunta_pendiente"):
        w("   %-18s %s" % (k, f.get(k)))
w("   CIFRA de las cuatro cuyo `tipo` es MESA: %d"
  % len([f for f in fichas if f.get("id_op") in CUATRO and f.get("tipo") == "MESA"]))
w("")

w("=== H.3 LOS PRODUCTOS DOCUMENTALES DE LAS CUATRO, MEDIDOS EN DISCO ===")
PRODUCTOS = [
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "docs/plan/INVENTARIO.jsonl",
    "docs/plan/10_INVENTARIO.md",
    "docs/plan/INTRA_DOMINIO_INFORME.md",
    "docs/plan/BANCO_DEL_PLAN.md",
    "docs/BANCO_DE_TEXTOS.md",
]
for r in PRODUCTOS:
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if not os.path.exists(p):
        w("   %s -> NO EXISTE" % r)
        continue
    sd, sl, bd, bl = sha_de(p)
    t = io.open(p, encoding="utf-8", errors="replace").read().replace(chr(13) + NL, NL)
    w("   %s -> disco %d bytes | LF %d bytes | lineas %d" % (r, bd, bl, t.count(NL)))
LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
if os.path.exists(LD):
    t = io.open(LD, encoding="utf-8", errors="replace").read()
    etiquetas = sorted(set(re.findall(r"\bLD-(\d+)\b", t)), key=int)
    w("   ETIQUETAS `LD-nn` DISTINTAS EN LECTURAS_DIRIGIDAS.md: %d" % len(etiquetas))
    w("      de LD-%s a LD-%s"
      % (etiquetas[0] if etiquetas else "?", etiquetas[-1] if etiquetas else "?"))
INV = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
if os.path.exists(INV):
    lin = [l for l in io.open(INV, encoding="utf-8") if l.strip()]
    w("   ENTRADAS NO VACIAS DE INVENTARIO.jsonl: %d" % len(lin))
    ok = 0
    for l in lin:
        try:
            json.loads(l)
            ok += 1
        except Exception:
            pass
    w("   de esas, filas JSON validas: %d" % ok)
w("")

w("=== H.4 EL CASO E Y LAS DOS APARICIONES DE `not tardio` (TAREA 3) ===")
CR_RUTA = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
t_cr = io.open(CR_RUTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
sd, sl, bd, bl = sha_de(CR_RUTA)
w("   scripts/loop/cerrar_reporte.py -> disco %d bytes | LF %d bytes | lineas %d"
  % (bd, bl, t_cr.count(NL)))
w("   sha256 LF DEL SUJETO: %s" % sl)
w("   CIFRA apariciones de `not tardio`: %d" % t_cr.count("not tardio"))
for i, l in enumerate(t_cr.split(NL), 1):
    if "not tardio" in l:
        w("      LINEA %-5d %s" % (i, l.strip()[:110]))
for aguja in ("if not dentro or sin_declarar", "MARCA_TARDIO_S4",
              "def piezas_que_faltan", "def parejas_publicadas",
              "def cifras_sin_pareja"):
    hits = [i for i, l in enumerate(t_cr.split(NL), 1) if aguja in l]
    w("   %-34s -> lineas %s"
      % (repr(aguja), ", ".join(str(x) for x in hits) or "(ninguna)"))
w("   LA CORRIDA DE HOY DEL CASO E, EN EL ESTADO EN QUE ABRE LA VUELTA:")
c_e, o_e = correr([PY, "scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py"])
escribir("T3_CASO_E_ANTES", o_e + NL + "EXITCODE: %d" % c_e + NL)
for l in o_e.split(NL):
    if l.startswith("CIFRA ") or l.startswith("VEREDICTO"):
        w("      " + l.strip())
w("      exitcode: %d" % c_e)
w("")

w("=== H.5 LA COBERTURA DE parejas_publicadas() SOBRE EL REPORTE DE LA 187 ===")
try:
    import cerrar_reporte as CR
    c_show, t187 = git(["show", "9a06b7c8:docs/loop/REPORTE.md"])
    if c_show == 0:
        t187 = t187.replace(chr(13) + NL, NL)
        w("   git show 9a06b7c8:docs/loop/REPORTE.md -> %d bytes | %d lineas"
          % (len(t187.encode("utf-8")), t187.count(NL)))
        pares = CR.parejas_publicadas(t187)
        w("   CIFRA parejas que la guarda VE HOY: %d" % len(pares))
        for n, ruta, pd_, pl_, forma in pares:
            w("      linea %-5d %-52s %s / %s   [%s]" % (n, ruta, pd_, pl_, forma))
        med = CR.mediciones_de_las_rutas(t187)
        rojas = CR.convenciones_que_no_calzan(t187, med)
        w("   CIFRA parejas que NO calzan: %d" % len(rojas))
        for fila in rojas:
            w("      %s" % (fila,))
        rutas_con_bytes = set()
        for n, linea in CR.renglones_fuera_de_cerca(t187):
            if CR.PATRON_BYTES.search(linea):
                for mm in CR.PATRON_RUTA_PUBLICADA.finditer(linea):
                    rutas_con_bytes.add((n, mm.group(1)))
        w("   CIFRA (linea, ruta) con alguna cifra de bytes en su misma linea: %d"
          % len(rutas_con_bytes))
    else:
        w("   NO SE PUDO LEER 9a06b7c8:docs/loop/REPORTE.md")
except Exception as e:
    w("   NO SE PUDO CORRER LA GUARDA: %r" % (e,))
w("")

w("=== H.6 LAS SECCIONES DEL REPORTE DE LA 187, UNICAS O NO (LA C.4) ===")
try:
    c_show, t187b = git(["show", "9a06b7c8:docs/loop/REPORTE.md"])
    t187b = t187b.replace(chr(13) + NL, NL)
    cuenta = {}
    for i, l in enumerate(t187b.split(NL), 1):
        m = re.match(r"^## (\d+)\.", l)
        if m:
            cuenta.setdefault(int(m.group(1)), []).append(i)
    for k in sorted(cuenta):
        w("   seccion `## %d.` -> %d aparicion(es), lineas %s"
          % (k, len(cuenta[k]), ", ".join(str(x) for x in cuenta[k])))
    dup = [k for k in cuenta if len(cuenta[k]) > 1]
    w("   CIFRA secciones DUPLICADAS: %d (%s)"
      % (len(dup), ", ".join(str(x) for x in sorted(dup)) or "ninguna"))
    orden = [k for k, _v in sorted(
        [(k, v[0]) for k, v in cuenta.items()], key=lambda x: x[1])]
    w("   ORDEN EN QUE APARECEN: %s" % ", ".join(str(x) for x in orden))
    w("   ESTAN EN ORDEN CRECIENTE: %s"
      % ("SI" if orden == sorted(orden) else "NO"))
    for r in ("docs/loop/reportes/REPORTE_V184.md",
              "docs/loop/reportes/REPORTE_V185.md",
              "docs/loop/reportes/REPORTE_V186.md"):
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        if not os.path.exists(p):
            w("   %s -> NO EXISTE" % r)
            continue
        tt = io.open(p, encoding="utf-8").read().replace(chr(13) + NL, NL)
        n9 = len([1 for l in tt.split(NL) if l.startswith("## 9.")])
        w("   %s -> %d seccion(es) `## 9.`" % (r, n9))
except Exception as e:
    w("   NO SE PUDO MEDIR: %r" % (e,))
w("")

w("=== H.7 LA NOMINA Y LOS ARNESES QUE FALTAN (guarda del encargo) ===")
try:
    import verificar_mutaciones_viejas as VM
    w("   CIFRA nomina ANTES de meter nada: %d" % len(VM.VIEJAS))
    w("   VARA_DEL_CENSO: %s" % VM.VARA_DEL_CENSO)
    faltan_a = VM.arneses_que_faltan()
    w("   arneses_que_faltan() HOY: %s" % (faltan_a,))
except Exception as e:
    w("   NO SE PUDO LLAMAR: %r" % (e,))
w("")

w("=== H.8 LA SERIE DE REGISTROS, LLAMADA Y NO TECLEADA (TAREA 1) ===")
try:
    import serie_de_registros as SER
    halladas = SER.entradas()
    w("   CIFRA entradas de la serie: %d" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SER.colisiones(halladas)), len(SER.huecos(halladas))))
    w("   SIGUIENTE LIBRE, LLAMADO Y NO TECLEADO: R.%d"
      % SER.siguiente_libre(halladas))
    for numero, rel_, linea, titulo in halladas[-4:]:
        w("   ULTIMOS: R.%s en %s:%d -> %s" % (numero, rel_, linea, titulo[:100]))
except Exception as e:
    w("   NO SE PUDO RECOMPUTAR LA SERIE: %r" % (e,))
w("")

w("=== H.9 EL ACTA 188, ACOTADA, Y SUS SECCIONES ===")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
t_acta = io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
lin_acta = t_acta.split(NL)
cab = [i for i, l in enumerate(lin_acta, 1)
       if l.startswith("# ACTA DEL AUDITOR, VUELTA %d" % VUELTA)]
w("   docs/loop/ACTA_AUDITOR.md -> %d lineas | disco %d bytes"
  % (len(lin_acta), os.path.getsize(ACTA)))
w("   CIFRA cabeceras del acta %d: %d (lineas %s)"
  % (VUELTA, len(cab), ", ".join(str(x) for x in cab) or "ninguna"))
if len(cab) == 1:
    ini = cab[0]
    w("   el acta %d empieza en la linea %d y llega al final del fichero" % (VUELTA, ini))
    for i in range(ini, len(lin_acta) + 1):
        if lin_acta[i - 1].startswith("## "):
            w("      LINEA %-6d %s" % (i, lin_acta[i - 1][:100]))
w("")

w("=== H.10 EL ARCHIVO DE VEREDICTOS, QUE ESTA VUELTA NO MUEVE ===")
w("(el encargo da 0a77b5a35a962621 como sha256 LF de apertura. NO SE COPIA)")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
sd, sl, bd, bl = sha_de(VER)
w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> disco %d bytes | LF %d bytes" % (bd, bl))
w("   sha256 (disco): %s" % sd)
w("   sha256 (LF)   : %s" % sl)
w("   los 16 primeros del sha256 LF: %s -> el encargo dice 0a77b5a35a962621: %s"
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
w("   CIFRA campos distintos en la primera fila: %d (%s)"
  % (len(filas_v[0]), ", ".join(sorted(filas_v[0].keys()))))
w("")

w("=== H.11 LA BATERIA, QUE ESTA VUELTA NO CORRE, Y SU HUECO ===")
for r in ("docs/loop/SALIDA_V188_BATERIA.txt", "docs/loop/SALIDA_V187_BATERIA.txt",
          "docs/loop/SALIDA_V186_BATERIA.txt", "docs/loop/SALIDA_V185_BATERIA.txt",
          "docs/loop/SALIDA_V184_BATERIA.txt", "docs/loop/SALIDA_V183_BATERIA.txt"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        sd, sl, bd, bl = sha_de(p)
        w("   %s -> disco %d bytes | LF %d bytes | sha256 LF %s" % (r, bd, bl, sl))
    else:
        w("   %s -> NO EXISTE, y por eso mide 0 bytes por las dos convenciones:"
          " el cero sale de que el fichero no esta" % r)
w("")
w("FIN DEL SELLO DE APERTURA")

texto = NL.join(L) + NL
io.open(os.path.join(LOOP, "SALIDA_V%s_APERTURA.txt" % SUFIJO), "w",
        encoding="utf-8", newline=NL).write(texto)
print(texto)
escribir("HEAD", head + NL)

# ------------------------------------------------- EL BLOQUE DE MEDICIONES
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
