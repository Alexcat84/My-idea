# -*- coding: utf-8 -*-
r"""vuelta187_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 187, ENTERO Y
ANTES DE LA PRIMERA OPERACION.

CLON DECLARADO de scripts/loop/vuelta186_apertura.py. Cambia el SUFIJO de las
salidas (187, computado del nombre del fichero), la lista RUTAS_DEL_ENCARGO, las
lineas del regimen y los bloques H, que aqui miden lo que ESTE encargo promete y
nada mas. Y LA AFIRMACION DE CLON SE MIDE: el cotejo lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte con lo
que salga. NO se afirma que el diff salga vacio.

QUE ES ESTA VUELTA Y QUE NO ES. NO ES VUELTA DE BATERIA: la bateria cerro entera
en la 184 y por AUDITOR.md 6.1 corre CADA CINCO VUELTAS, asi que la siguiente es
la 189. La seccion 9 del reporte de la 187 cierra CON EL HUECO DECLARADO Y
MEDIDO. EL TOPE VUELVE A CINCO: el regimen temporal 6.2 pedia DOS vueltas
seguidas cerrando su propio reporte, la 185 fue la primera y la 186 la segunda,
y el disparador de salida del propio regimen lo apaga solo. AQUI NO SE DA POR
BUENO: el bloque H.0 mide las dos salidas de cierre y publica lo que salga.

EL SELLO DEL AUDITOR DE ESTA VUELTA NO SE DEDUCE DEL NUMERO DE VUELTA. La casa
nombra el sello del acta N como V(N+1); siendo acta 187, el sello se llama V188.
El V186 NO EXISTE y no se fabrica. Las rutas exactas van en RUTAS_DEL_ENCARGO y
en el bloque H.5, y el sha256 se COMPUTA y se COMPARA, no se copia del encargo.

LA CIFRA DEL BLOQUE H.5 SE REPARA AQUI (TAREA 5.c). El bloque de apertura de la
186 conto los puestos de las ciegas con el patron 'PUESTO <n>' en mayusculas
cuando las ciegas los escriben como 'puesto_intra: <n>', y publico 0 puestos
para cuatro ficheros. El propio ejecutor lo declaro. Aqui el H.5 cuenta con LOS
DOS PATRONES y publica LAS DOS CIFRAS, la vieja y la nueva, para que se vea que
la nueva dejo de ser cero; y todo lo que el bloque decida despues usa la NUEVA.

EL BLOQUE H NO TECLEA NINGUN HASH NI NINGUNA CIFRA (EJECUTOR.md 2, EL
INSTRUMENTO MANDA). El encargo da cifras (802 bytes del sello, 42599 y 32894 de
la ciega y el destape, 8030 de mis clases, ea6e850d331d14f0 del archivo de
veredictos); aqui NO SE COPIA NINGUNA: se corre y se imprime lo que salga, y la
comparacion con lo que el encargo dice se hace despues, en el reporte, con las
dos al lado.

LA CIFRA DE BYTES SE PUBLICA POR LAS DOS CONVENCIONES (acta 177 punto 7.11):
disco (os.path.getsize) y git (git cat-file -s). Y la P.2 del fundador manda
BYTES EXACTOS Y NUNCA REDONDEADOS.

POR QUE SE CORRE AQUI: EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION". El encargo manda ademas commitear lo pendiente antes de
tocar nada, y un commit MUEVE HEAD: por eso este bloque corre PRIMERO.

ESTE FICHERO NO TOCA REPORTE.md, NO toca la nomina, NO corre la bateria, NO
archiva ningun reporte y NO escribe en docs/plan/: sus salidas son
SALIDA_V187_*.txt.

LO QUE ESTA SESION SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES. Al abrir la sesion, git status --porcelain corrido a mano dio CERO
lineas y git diff --numstat -- dataset/ dio CERO filas. PERO ESTE FICHERO YA
ESTA ESCRITO Y NO ESTA SEGUIDO POR GIT CUANDO EL BLOQUE C CORRE, asi que la
prediccion para el bloque C es UNA linea de interrogantes (esta misma), no cero.
La caida R.1 del acta 186 fue exactamente eso: atribuirle al bloque C una
medicion que el bloque C contradecia.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

USO:
  python scripts/loop/vuelta187_apertura.py
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

# EL SUFIJO DE LAS SALIDAS, COMPUTADO DEL NOMBRE DEL FICHERO Y NO TECLEADO.
LANZADOR = os.path.basename(os.path.abspath(__file__))
_m = re.match(r"^vuelta(\d+[a-z]?)_", LANZADOR)
if not _m:
    raise SystemExit("ROJO: el nombre %r no dice de que vuelta es. No se adivina."
                     % LANZADOR)
SUFIJO = _m.group(1).upper()
VUELTA = int(re.match(r"^(\d+)", _m.group(1)).group(1))

SUJETOS = [
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/vuelta186_rutas_del_reporte.py",
    "scripts/loop/vuelta186_tarea2d_mutacion_seccion4.py",
    "scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py",
    "scripts/loop/serie_de_registros.py",
    "scripts/loop/vuelta186_tarea1a_registrar_acta186.py",
    "scripts/loop/vuelta186_tarea1c_relectura_al_doble.py",
    "scripts/loop/vuelta182_tarea1c_relectura_al_doble.py",
    "scripts/loop/cotejar_clon_declarado.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/tallar_cabecera_reporte.py",
    "scripts/loop/vuelta186_esqueleto_reporte.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/SELLO_APERTURA_AUDITOR_V188.json",
    "docs/loop/_auditor_v188_ciega_blind.txt",
    "docs/loop/_auditor_v188_ciega_reveal.txt",
    "docs/loop/_auditor_v188_mis_clases.txt",
    "docs/loop/_auditor_v188_exclusion.txt",
    "docs/loop/_auditor_v187_ciega_blind.txt",
    "docs/loop/SALIDA_V184_APERTURA.txt",
    "docs/loop/SALIDA_V186_APERTURA.txt",
    "docs/loop/SALIDA_V186_CERRAR_REPORTE.txt",
    "docs/loop/SALIDA_V185_CERRAR_REPORTE.txt",
    "docs/loop/SALIDA_V186_RUTAS_DEL_REPORTE.txt",
    "docs/loop/SALIDA_V183_BATERIA.txt",
    "docs/loop/reportes/REPORTE_V184.md",
    "docs/loop/reportes/REPORTE_V185.md",
    "docs/loop/reportes/REPORTE_V186.md",
    "docs/PENDIENTES.md",
    "docs/plan/08_VERIFICACION.md",
    "docs/plan/BANCO_DEL_PLAN.md",
    "docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "scripts/loop/guarda_commit_dataset.py",
    "scripts/loop/anexar_tarea_al_reporte.py",
] + SUJETOS

REGISTRO_SC = os.path.join(RAIZ, "docs", "plan", "SUJETO_CONGELADO_VEREDICTOS.jsonl")


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env, shell=shell)
    out = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    return r.returncode, out


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def bytes_de_git(ruta):
    c, o = git(["cat-file", "-s", "HEAD:" + ruta])
    o = o.strip()
    return int(o) if c == 0 and o.isdigit() else None


def sha_de(ruta):
    """SHA256 POR LAS DOS CONVENCIONES: crudo de disco y normalizado a LF."""
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (hashlib.sha256(datos).hexdigest(), hashlib.sha256(lf).hexdigest(),
            len(datos), len(lf))


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V%s_%s_APERTURA.txt" % (SUFIJO, nombre))
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("ESCRITO: %s (%d bytes)" % (os.path.basename(ruta), len(texto.encode("utf-8"))))


lineas = []
w = lineas.append
NL = chr(10)
w("SELLO DE APERTURA DE LA VUELTA %d, escrito ANTES de la primera operacion." % VUELTA)
w("Sufijo de salidas: %s (computado de %s, no tecleado)" % (SUFIJO, LANZADOR))
w("regimen: NO ES VUELTA DE BATERIA. AUDITOR.md 6.1: la bateria corre CADA CINCO")
w("         vueltas y cerro entera en la 184, asi que la siguiente es la 189. La")
w("         seccion 9 del reporte de la 187 cierra CON EL HUECO DECLARADO Y")
w("         MEDIDO por el carril de cerrar_reporte.py: nombre, bytes y")
w("         atribucion, las tres juntas o no vale.")
w("         EL TOPE VUELVE A CINCO. El regimen temporal 6.2 pedia DOS vueltas")
w("         seguidas cerrando su propio reporte: la 185 fue la primera y la 186")
w("         la segunda. AQUI NO SE DA POR BUENO PORQUE EL ENCARGO LO DIGA: el")
w("         bloque H.0 mide las dos salidas de cierre y publica lo que salga.")
w("         EL SELLO DEL AUDITOR SE LLAMA V188, no V187 ni V186: la casa nombra")
w("         el sello del acta N como V(N+1) y esta es el acta 187.")
w("")

w("=== A. HEAD DE APERTURA (git rev-parse HEAD) ===")
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

w("=== B.1 LA CADENA DE LA VUELTA 186, LOCALIZADA EN GIT Y NO TECLEADA ===")
w("(no se teclea ningun hash: se busca en el log el commit de cada pieza de la")
w(" 186 y se imprime lo que salga)")
c, logtodo = git(["log", "--format=%h%x09%s", "-120"])
for etiqueta, aguja in (("acta 186", "ACTA DEL AUDITOR, VUELTA 186"),
                        ("acta 187", "ACTA DEL AUDITOR, VUELTA 187"),
                        ("tarea 1 de la 186", "VUELTA 186, TAREA 1"),
                        ("tarea 2 de la 186", "VUELTA 186, TAREA 2"),
                        ("cierre de la 186", "VUELTA 186 CERRADA")):
    hits = [l for l in logtodo.splitlines() if aguja.upper() in l.upper()]
    w("   %-18s -> %s"
      % (etiqueta, (hits[0][:150] if hits else "NO LOCALIZADO EN LOS 120 ULTIMOS")))
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
        w("%s -> disco %d bytes | git %s"
          % (ruta, os.path.getsize(p),
             ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
    else:
        w("%s -> disco NO EXISTE | git %s"
          % (ruta, ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("")

w("=== E. DIFF REAL EN BYTES DE LOS MODIFICADOS (cambio contra suciedad) ===")
c, mod = git(["ls-files", "-m"])
n_mod = 0
for ruta in [l for l in mod.splitlines() if l.strip()]:
    n_mod += 1
    c2, d = git(["diff", "--", ruta])
    w("%s -> diff de %d bytes" % (ruta, len(d.encode("utf-8"))))
    c3, dn = git(["diff", "--numstat", "--", ruta])
    w("   %s -> git diff --numstat: %d filas"
      % (ruta, len([l for l in dn.splitlines() if l.strip()])))
w("CIFRA ficheros modificados: %d" % n_mod)
c, dnd = git(["diff", "--numstat", "--", "dataset/"])
w("CIFRA filas de `git diff --numstat -- dataset/` AL ENTRAR: %d"
  % len([l for l in dnd.splitlines() if l.strip()]))
w("")

w("=== F. LO NO SEGUIDO POR GIT, FICHERO A FICHERO CON SUS BYTES ===")
c, unt = git(["status", "--porcelain", "--untracked-files=all"])
n_unt = 0
for l in unt.splitlines():
    if l.startswith("?? "):
        r = l[3:].strip().strip(chr(34))
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        tam = os.path.getsize(p) if os.path.isfile(p) else -1
        w("%s -> %s" % (r, ("%d bytes" % tam) if tam >= 0 else "(no es fichero)"))
        n_unt += 1
w("CIFRA ficheros no seguidos: %d" % n_unt)
w("")

w("=== G. git ls-tree DE HEAD SOBRE ESAS RUTAS ===")
for ruta in RUTAS_DEL_ENCARGO:
    c, t = git(["ls-tree", "HEAD", "--", ruta])
    w("%s -> %s" % (ruta, t.strip() if t.strip() else "NO ESTA EN EL ARBOL DE HEAD"))
w("")
w("=== H. EL REPORTE EN HEAD, MEDIDO SIN CREERLE AL ENCARGO ===")
w("(el encargo dice que el de la 185 ya cerro y se archivo. Aqui se mide que es")
w(" y en que estado esta, sin tocarlo y sin archivar nada)")
c, rep = git(["show", "HEAD:docs/loop/REPORTE.md"])
w("primera linea: %s" % (rep.split(NL, 1)[0].strip() if rep else "(vacio)"))
w("lineas (saltos de linea contados): %d" % rep.count(NL))
w("bytes en git: %d" % len(rep.encode("utf-8")))
MARCAS = ["SIN ESCRIBIR TODAVIA", "PENDIENTE DE TALLAR AL CIERRE",
          "ABIERTA, SIN CERRAR", "CERRADA",
          "<!-- TABLA DE TAREAS -->", "<!-- FIN TABLA DE TAREAS -->",
          "<!-- ANEXO DE TAREAS -->", "<!-- FIN ANEXO DE TAREAS -->",
          "<!-- CABECERA TALLADA -->"]
MARCAS = MARCAS + [NL + "## %d." % k for k in range(3, 10)]
for marca in MARCAS:
    w("   contiene %-40s -> %s" % (repr(marca), "SI" if marca in rep else "NO"))
RUTA_REP = os.path.join(LOOP, "REPORTE.md")
arbol = io.open(RUTA_REP, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("EL DEL ARBOL: bytes LF %d | saltos de linea %d | disco crudo %d"
  % (len(arbol.encode("utf-8")), arbol.count(NL), os.path.getsize(RUTA_REP)))
w("identico byte a byte al de HEAD: %s"
  % ("SI" if arbol == rep.replace(chr(13) + NL, NL) else "NO"))
w("FILAS DE LA TABLA DE TAREAS, CONTADAS DE SU TABLA Y NO RECORDADAS:")
dentro = False
n_filas = 0
for i, l in enumerate(arbol.split(NL), 1):
    if "<!-- TABLA DE TAREAS -->" in l:
        dentro = True
        continue
    if "<!-- FIN TABLA DE TAREAS -->" in l:
        dentro = False
        continue
    if dentro and re.search(r"TAREA\s+\d+", l) and l.strip().startswith("|"):
        n_filas += 1
        w("   LINEA %d: %s" % (i, l.strip()[:110]))
w("CIFRA filas de tarea en la tabla: %d" % n_filas)
w("")

w("=== H.0 LAS DOS VUELTAS QUE APAGAN EL REGIMEN TEMPORAL 6.2, MEDIDAS ===")
w("(el encargo dice que la 185 y la 186 cerraron su propio reporte y que por eso")
w(" el tope vuelve a CINCO. AQUI NO SE LE CREE: se miden las dos salidas de")
w(" cierre y se pega la linea de la cifra de piezas que faltan de cada una)")
for r in ("docs/loop/SALIDA_V185_CERRAR_REPORTE.txt",
          "docs/loop/SALIDA_V186_CERRAR_REPORTE.txt"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if not os.path.exists(p):
        w("   %s -> NO EXISTE. Sin ella no se afirma que esa vuelta cerrase." % r)
        continue
    sd, sl, bd, bl = sha_de(p)
    t_c = io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    w("   %s -> disco %d bytes | LF %d bytes | sha256 LF %s" % (r, bd, bl, sl))
    for i, l in enumerate(t_c.split(NL), 1):
        if ("CIFRA piezas que faltan" in l or "VEREDICTO" in l
                or l.startswith("EXITCODE")):
            w("      LINEA %d: %s" % (i, l.strip()[:150]))
w("   Y EL REPORTE DE LA 186 ARCHIVADO, MEDIDO CONTRA GIT:")
R186 = "docs/loop/reportes/REPORTE_V186.md"
P186 = os.path.join(RAIZ, R186.replace("/", os.sep))
if os.path.exists(P186):
    sd, sl, bd, bl = sha_de(P186)
    g = bytes_de_git(R186)
    w("      %s -> disco %d bytes | LF %d bytes | sha256 LF %s | git %s"
      % (R186, bd, bl, sl, ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
else:
    w("      %s -> NO EXISTE" % R186)
w("")

w("=== H.1 EL DISPARADOR ESCRITO DE LA COLA POST FUSION (TAREA 2) ===")
w("(el encargo manda LEER EL DISPARADOR ANTES DE TOCAR NADA y citarlo por")
w(" numero. Aqui no se cita de memoria: se busca en los dos ficheros que el")
w(" encargo nombra y se pega la linea con su numero de linea, sea la que sea)")
for r in ("docs/plan/08_VERIFICACION.md", "docs/plan/BANCO_DEL_PLAN.md"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if not os.path.exists(p):
        w("   %s -> NO EXISTE" % r)
        continue
    t_d = io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    w("   %s -> disco %d bytes | lineas %d" % (r, os.path.getsize(p), t_d.count(NL)))
    for aguja in ("cola post fusion", "COLA POST FUSION", "post fusion",
                  "POST FUSION", "2464", "2.464"):
        hits = [(i, l) for i, l in enumerate(t_d.split(NL), 1) if aguja in l]
        w("      %-20s -> %d aparicion(es), lineas %s"
          % (repr(aguja), len(hits),
             ", ".join(str(i) for i, _l in hits[:12]) or "(ninguna)"))
    w("      LAS LINEAS QUE NOMBRAN LA COLA, PEGADAS ENTERAS:")
    n_peg = 0
    for i, l in enumerate(t_d.split(NL), 1):
        if ("post fusion" in l.lower() or "cola" in l.lower()) and l.strip():
            w("         LINEA %d: %s" % (i, l.strip()[:170]))
            n_peg += 1
            if n_peg >= 40:
                w("         (cortado en 40 lineas; el resto se lee del fichero)")
                break
w("")

w("=== H.2 LA SEDE DE LA ESCALADA, MEDIDA ANTES DE TOCARLA (TAREA 4) ===")
w("(la guarda de la pareja comprueba que la pareja EXISTA, no que sea CIERTA.")
w(" Aqui se localiza la sede viva en cerrar_reporte.py y en el instrumento que")
w(" ya sabe medir las dos convenciones, y se pega lo que salga)")
CER = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
t_cer = io.open(CER, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_cer = t_cer.split(NL)
w("   scripts/loop/cerrar_reporte.py -> %d lineas | disco %d bytes"
  % (len(l_cer), os.path.getsize(CER)))
for aguja in ("def cifras_sin_pareja", "def piezas_que_faltan",
              "def rama_de_la_seccion9", "def es_cierre_tardio",
              "def declaracion_de_cifras_sin_pareja", "def seccion4_que_no_calza",
              "con su pareja", "def renglones_fuera_de_cerca",
              "def citas_de_arnes_que_no_calzan"):
    hits = [(i, l) for i, l in enumerate(l_cer, 1) if aguja in l]
    w("   %-40s -> %d aparicion(es), lineas %s"
      % (repr(aguja), len(hits),
         ", ".join(str(i) for i, _l in hits[:10]) or "(ninguna)"))
w("   LA LINEA DEL BLOQUE D QUE HOY DA POR BUENA LA PAREJA, PEGADA ENTERA:")
for i, l in enumerate(l_cer, 1):
    if "con su pareja" in l:
        w("      LINEA %d: %s" % (i, l.rstrip()[:170]))
RUT = os.path.join(RAIZ, "scripts", "loop", "vuelta186_rutas_del_reporte.py")
if os.path.exists(RUT):
    t_rut = io.open(RUT, encoding="utf-8").read().replace(chr(13) + NL, NL)
    l_rut = t_rut.split(NL)
    w("   scripts/loop/vuelta186_rutas_del_reporte.py -> %d lineas | disco %d bytes"
      % (len(l_rut), os.path.getsize(RUT)))
    for i, l in enumerate(l_rut, 1):
        if l.startswith("def ") or "replace(b" in l:
            w("      LINEA %d: %s" % (i, l.rstrip()[:140]))
else:
    w("   scripts/loop/vuelta186_rutas_del_reporte.py -> NO EXISTE")
w("")

w("=== H.2.1 LAS CUATRO CIFRAS DE LA C.1, EN EL TEXTO REAL QUE LAS TRAJO ===")
w("(TAREA 4. El caso que la escalada tiene que cazar vive en el reporte de la")
w(" 186 tal como lo dejo el commit bb3aaad3. Aqui se saca ese texto de git, se")
w(" buscan sus parejas de disco y LF y se mide CADA ruta en disco para ver")
w(" cuales de las dos convenciones publicadas NO son ciertas. Ninguna cifra se")
w(" copia del encargo: todas salen de aqui)")
c_bb, t_bb = git(["show", "bb3aaad3:docs/loop/REPORTE.md"])
if c_bb != 0 or not t_bb.strip():
    w("   git show bb3aaad3:docs/loop/REPORTE.md -> NO SE PUDO LEER (exit %d)" % c_bb)
else:
    t_bb = t_bb.replace(chr(13) + NL, NL)
    w("   git show bb3aaad3:docs/loop/REPORTE.md -> %d bytes | lineas %d"
      % (len(t_bb.encode("utf-8")), t_bb.count(NL)))
    PAR = re.compile(r"`([A-Za-z0-9_./-]+\.[A-Za-z0-9]+)`[^\n]{0,220}?"
                     r"disco\s+([0-9.]+)\s*bytes[^\n]{0,80}?LF\s+([0-9.]+)\s*bytes")
    n_par = n_mal_d = n_mal_l = 0
    for i, l in enumerate(t_bb.split(NL), 1):
        for m in PAR.finditer(l):
            ruta_p = m.group(1)
            try:
                pub_d = int(m.group(2).replace(".", ""))
                pub_l = int(m.group(3).replace(".", ""))
            except ValueError:
                continue
            n_par += 1
            pp = os.path.join(RAIZ, ruta_p.replace("/", os.sep))
            if not os.path.isfile(pp):
                w("      LINEA %d: %-56s publicada disco %d LF %d -> LA RUTA NO"
                  " EXISTE HOY" % (i, ruta_p, pub_d, pub_l))
                continue
            dat = io.open(pp, "rb").read()
            med_d, med_l = len(dat), len(dat.replace(b"\r\n", b"\n"))
            mal = []
            if med_d != pub_d:
                mal.append("DISCO")
                n_mal_d += 1
            if med_l != pub_l:
                mal.append("LF")
                n_mal_l += 1
            w("      LINEA %d: %-56s publicada disco %d LF %d | medida disco %d"
              " LF %d | %s"
              % (i, ruta_p, pub_d, pub_l, med_d, med_l,
                 ("FALLA " + " y ".join(mal)) if mal else "calza"))
    w("   CIFRA parejas de disco y LF halladas en el texto de bb3aaad3: %d" % n_par)
    w("   CIFRA parejas cuya cifra de DISCO no calza hoy: %d" % n_mal_d)
    w("   CIFRA parejas cuya cifra de LF no calza hoy: %d" % n_mal_l)
w("")

w("=== H.3 LA NOMINA Y LOS ARNESES QUE FALTAN (TAREA 5.a) ===")
w("(el encargo dice que arneses_que_faltan() devuelve hoy exactamente cuatro y")
w(" los nombra. Aqui no se copian: se llama a la funcion y se pega lo que")
w(" devuelva, y el tamano de la nomina se cuenta ANTES de meter nada)")
try:
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_mutaciones_viejas as VMV   # noqa: E402
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _a in VMV.VIEJAS]
    w("   CIFRA censo: %d | CIFRA nomina ANTES: %d | VARA_DEL_CENSO: %d"
      % (len(censo), len(nomina), VMV.VARA_DEL_CENSO))
    ultima, faltan = VMV.arneses_que_faltan()
    w("   arneses_que_faltan() HOY: ultima vuelta %s, faltan %d" % (ultima, len(faltan)))
    for n in faltan:
        w("      FALTA: %s" % n)
    invis = VMV.nomina_invisible_al_censo()
    w("   nomina_invisible_al_censo(): %d" % len(invis))
    for n in invis:
        w("      INVISIBLE: %s" % n)
    malas = VMV.guarda_del_sujeto_congelado()
    w("   guarda_del_sujeto_congelado(): %d entradas sin congelar" % len(malas))
    for nombre, veredicto, vive in malas:
        w("      SUJETO SIN CONGELAR: %-46s %s" % (nombre, veredicto))
except Exception as e:
    w("   NO SE PUDO RECOMPUTAR EL CENSO: %r" % (e,))
if os.path.exists(REGISTRO_SC):
    filas_sc = [json.loads(l) for l in io.open(REGISTRO_SC, encoding="utf-8") if l.strip()]
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> %d filas, disco %d bytes"
      % (len(filas_sc), os.path.getsize(REGISTRO_SC)))
else:
    w("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> NO EXISTE")
w("   LOS CUATRO ARNESES DE LA 186, MEDIDOS ANTES DE METERLOS:")
for r in ("scripts/loop/vuelta186_tarea2a_mutacion_pieza4.py",
          "scripts/loop/vuelta186_tarea2b_mutacion_pieza2_cercas.py",
          "scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py",
          "scripts/loop/vuelta186_tarea2d_mutacion_seccion4.py"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        sd, sl, bd, bl = sha_de(p)
        w("      %s -> disco %d bytes | LF %d bytes | sha256 LF %s" % (r, bd, bl, sl))
    else:
        w("      %s -> NO EXISTE" % r)
w("")

w("=== H.4 LA SECCION 4 DEL REPORTE DE LA 184 Y SU APERTURA (TAREA 5.b) ===")
w("(la P.2 del ejecutor de la 186 partia de que SALIDA_V184_APERTURA.txt no")
w(" existia. Aqui se mide si existe y cuanto mide, se pegan sus cifras de")
w(" status y numstat, y se corre seccion4_que_no_calza() sobre los ficheros")
w(" REALES para ver cuantos motivos en rojo salen. Ninguna cifra se copia)")
AP184 = os.path.join(LOOP, "SALIDA_V184_APERTURA.txt")
if os.path.exists(AP184):
    sd, sl, bd, bl = sha_de(AP184)
    t_ap = io.open(AP184, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    w("   docs/loop/SALIDA_V184_APERTURA.txt -> disco %d bytes | LF %d bytes | "
      "lineas %d" % (bd, bl, t_ap.count(NL)))
    for i, l in enumerate(t_ap.split(NL), 1):
        if "CIFRA lineas de status" in l or "AL ENTRAR" in l:
            w("      LINEA %d: %s" % (i, l.strip()[:150]))
else:
    w("   docs/loop/SALIDA_V184_APERTURA.txt -> NO EXISTE")
REP184 = os.path.join(LOOP, "reportes", "REPORTE_V184.md")
if os.path.exists(REP184):
    t_r4 = io.open(REP184, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    l_r4 = t_r4.split(NL)
    w("   docs/loop/reportes/REPORTE_V184.md -> disco %d bytes | lineas %d"
      % (os.path.getsize(REP184), t_r4.count(NL)))
    i4 = [i for i, l in enumerate(l_r4, 1) if l.startswith("## 4.")]
    i5 = [i for i, l in enumerate(l_r4, 1) if l.startswith("## 5.")]
    w("   seccion 4 empieza en la linea %s y la 5 en la %s"
      % (i4[0] if i4 else "(ninguna)", i5[0] if i5 else "(ninguna)"))
    if i4:
        fin = i5[0] if i5 else len(l_r4) + 1
        sec4 = l_r4[i4[0] - 1:fin - 1]
        w("   CIFRA lineas de la seccion 4: %d" % len(sec4))
        for k, l in enumerate(sec4, i4[0]):
            if l.strip():
                w("      LINEA %d: %s" % (k, l.strip()[:150]))
else:
    w("   docs/loop/reportes/REPORTE_V184.md -> NO EXISTE")
w("   seccion4_que_no_calza() CORRIDA HOY SOBRE LOS DOS FICHEROS REALES:")
try:
    import cerrar_reporte as CR   # noqa: E402
    if os.path.exists(REP184) and os.path.exists(AP184):
        t_r4b = io.open(REP184, encoding="utf-8", errors="replace").read().replace(
            chr(13) + NL, NL)
        t_a4b = io.open(AP184, encoding="utf-8", errors="replace").read().replace(
            chr(13) + NL, NL)
        motivos = CR.seccion4_que_no_calza(t_r4b, t_a4b, "SALIDA_V184_APERTURA.txt")
        w("      CIFRA motivos en rojo: %d" % len(motivos))
        for m in motivos:
            w("      | %s" % str(m)[:220])
    else:
        w("      NO SE PUDO: falta alguno de los dos ficheros")
except Exception as e:
    w("      NO SE PUDO CORRER seccion4_que_no_calza: %r" % (e,))
w("")

w("=== H.5 EL SELLO DEL AUDITOR V188 Y SU CIEGA (TAREA 3 Y TAREA 5.c) ===")
w("(el encargo manda cotejar el sha256 del fichero ciego contra el sello ANTES")
w(" de releer nada. AQUI NO SE COPIA EL DEL ENCARGO: se computa y se compara.")
w(" Y EL PATRON DE PUESTOS SE REPARA AQUI, TAREA 5.c: el bloque de la 186 conto")
w(" con PUESTO en mayusculas y publico 0 para cuatro ficheros; las ciegas los")
w(" escriben como puesto_intra. Se publican LAS DOS CIFRAS, la VIEJA y la")
w(" NUEVA, y lo que el bloque decida despues usa la NUEVA)")
PATRON_VIEJO = re.compile(r"PUESTO\s+(\d+)")
PATRON_NUEVO = re.compile(r"^puesto_intra:\s*(\d+)\s*$", re.M)
SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_V188.json")
sello = None
if os.path.exists(SELLO):
    w("   docs/loop/SELLO_APERTURA_AUDITOR_V188.json -> disco %d bytes"
      % os.path.getsize(SELLO))
    sello = json.loads(io.open(SELLO, encoding="utf-8").read())
    w("   CLAVES DEL SELLO: %s" % ", ".join(sorted(sello.keys())))
    w("   EL SELLO ENTERO, PEGADO Y NO RESUMIDO:")
    for l in json.dumps(sello, indent=2, ensure_ascii=False).split(NL):
        w("      | " + l[:200])
else:
    w("   EL SELLO NO EXISTE. Sin el no se relee nada, y eso se dice.")
puestos_por_fichero = {}
for nombre in ("_auditor_v188_ciega_blind.txt", "_auditor_v188_ciega_reveal.txt",
               "_auditor_v188_mis_clases.txt", "_auditor_v187_ciega_blind.txt"):
    p = os.path.join(LOOP, nombre)
    if not os.path.exists(p):
        w("   docs/loop/%s -> NO EXISTE" % nombre)
        continue
    sd, sl, bd, bl = sha_de(p)
    t_c = io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    viejos = sorted({int(x) for x in PATRON_VIEJO.findall(t_c)})
    nuevos = sorted({int(x) for x in PATRON_NUEVO.findall(t_c)})
    puestos_por_fichero[nombre] = nuevos
    w("   docs/loop/%s" % nombre)
    w("      disco %d bytes | LF %d bytes | lineas %d" % (bd, bl, t_c.count(NL)))
    w("      sha256 (disco): %s" % sd)
    w("      sha256 (LF)   : %s" % sl)
    w("      CIFRA VIEJA, patron en mayusculas (la que publico la 186): %d"
      % len(viejos))
    w("      CIFRA NUEVA, patron puesto_intra (TAREA 5.c): %d" % len(nuevos))
    w("      LOS PUESTOS (patron nuevo): %s"
      % (", ".join(str(x) for x in nuevos) or "(ninguno)"))
if sello is not None:
    w("   EL COTEJO DEL SELLO, COMPUTADO Y NO COPIADO:")
    for clave_r, clave_b, clave_s in (("ciega", "bytes_ciega", "sha256_ciega"),
                                      ("destape", "bytes_destape", "sha256_destape")):
        r_s = sello.get(clave_r)
        if not r_s:
            w("      %s -> el sello no la nombra" % clave_r)
            continue
        p_s = os.path.join(RAIZ, r_s.replace("/", os.sep))
        if not os.path.exists(p_s):
            w("      %s -> %s NO EXISTE EN DISCO" % (clave_r, r_s))
            continue
        sd, sl, bd, bl = sha_de(p_s)
        w("      %-8s %s" % (clave_r, r_s))
        w("         bytes: sello %s | disco medido %d -> %s"
          % (sello.get(clave_b), bd,
             "CALZA" if sello.get(clave_b) == bd else "NO CALZA"))
        w("         sha256: sello %s" % sello.get(clave_s))
        w("                 disco  %s" % sd)
        w("                 -> %s"
          % ("CALZA" if sello.get(clave_s) == sd else "NO CALZA"))
w("   LOS PUESTOS DE LA EXCLUSION, CONTADOS DE SU FICHERO Y NO SUPUESTOS:")
EXC = os.path.join(LOOP, "_auditor_v188_exclusion.txt")
if os.path.exists(EXC):
    t_e = io.open(EXC, encoding="utf-8", errors="replace").read()
    ex = sorted({int(x) for x in re.findall(r"\d+", t_e)})
    w("      docs/loop/_auditor_v188_exclusion.txt -> disco %d bytes | CIFRA "
      "puestos distintos: %d" % (os.path.getsize(EXC), len(ex)))
    hoy_p = set(puestos_por_fichero.get("_auditor_v188_ciega_blind.txt", []))
    ayer_p = set(puestos_por_fichero.get("_auditor_v187_ciega_blind.txt", []))
    w("      SOLAPE ciega de hoy con la exclusion: %d" % len(hoy_p & set(ex)))
    w("      SOLAPE ciega de hoy con la ciega de la 187: %d" % len(hoy_p & ayer_p))
else:
    w("      docs/loop/_auditor_v188_exclusion.txt -> NO EXISTE")
w("   LOS CUATRO PUESTOS QUE EL ENCARGO NOMBRA, BUSCADOS EN LA CIEGA DE HOY:")
hoy_p = set(puestos_por_fichero.get("_auditor_v188_ciega_blind.txt", []))
for x in (226, 603, 1612, 2448):
    w("      puesto %-5d -> %s la ciega de hoy"
      % (x, "DENTRO de" if x in hoy_p else "FUERA de"))
w("")

w("=== H.6 LA SERIE DE REGISTROS Y EL ACTA 187 (TAREA 1.a) ===")
w("(no se teclea ningun numero de registro: se llama a serie_de_registros.py y")
w(" se imprime lo que devuelva. R.49 NO se da por bueno porque lo diga el encargo)")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
t_acta = io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_acta = t_acta.split(NL)
w("docs/loop/ACTA_AUDITOR.md -> %d lineas | disco %d bytes | LF %d bytes"
  % (len(l_acta), os.path.getsize(ACTA), len(t_acta.encode("utf-8"))))
CAB187 = [i for i, l in enumerate(l_acta, 1)
          if l.startswith("# ACTA DEL AUDITOR, VUELTA 187")]
w("CIFRA cabeceras del acta 187 encontradas: %d" % len(CAB187))
if CAB187:
    base = CAB187[0]
    w("   CABECERA del acta 187 en la LINEA %d" % base)
    w("   lineas del acta 187, de su cabecera al final del fichero: %d"
      % (len(l_acta) - base + 1))
    for aguja in ("## 1. ", "## 2. ", "## 3. ", "## 4. ", "## 5. ", "## 6. ",
                  "## 7. ", "## 8. ", "## 9. ", "## 10. ", "## 11. ", "## 12. ",
                  "## 13. "):
        hits = [i for i, l in enumerate(l_acta, 1)
                if l.startswith(aguja) and i >= base]
        w("   %-10s -> lineas %s"
          % (repr(aguja), ", ".join(str(x) for x in hits) or "(ninguna)"))
    w("   LOS NUMERALES DEL ACTA 187, CONTADOS CON EL PATRON DE COMILLAS")
    w("   INVERSAS QUE LA 184 ESTRENO, Y NO DE MEMORIA:")
    for pat in (r"\*\*`5\.(\d)`", r"\*\*`6\.(\d)`", r"\*\*`7\.(\d)`",
                r"`PD\.(\d)`", r"`A\.(\d)`", r"`R\.(\d)`", r"`C\.(\d)`"):
        hits = [(i, m.group(1)) for i, l in enumerate(l_acta, 1) if i >= base
                for m in [re.search(pat, l)] if m]
        vistos = sorted({v for _i, v in hits})
        w("      %-16s -> %d aparicion(es), numerales distintos %s"
          % (pat, len(hits), ", ".join(vistos) or "(ninguno)"))
    w("   LAS CABECERAS 5.n, 6.n Y 7.n DEL ACTA 187, PEGADAS ENTERAS:")
    for i, l in enumerate(l_acta, 1):
        if i >= base and re.match(r"^\*\*`[567]\.\d`", l):
            w("      LINEA %d: %s" % (i, l.strip()[:160]))
try:
    import serie_de_registros as SER   # noqa: E402
    halladas = SER.entradas()
    w("serie_de_registros.entradas() -> %d entradas en %d sedes"
      % (len(halladas), len(SER.SEDES)))
    for s in SER.SEDES:
        w("   SEDE: %s" % os.path.relpath(s, RAIZ).replace(os.sep, "/"))
    w("CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SER.colisiones(halladas)), len(SER.huecos(halladas))))
    w("SIGUIENTE LIBRE, LLAMADO Y NO TECLEADO: R.%s"
      % SER.siguiente_libre(halladas))
    for numero, rel_, linea, titulo in halladas[-4:]:
        w("   ULTIMOS: R.%s en %s:%d -> %s" % (numero, rel_, linea, titulo[:100]))
except Exception as e:
    w("NO SE PUDO RECOMPUTAR LA SERIE: %r" % (e,))
w("")

w("=== H.7 LA BATERIA, QUE ESTA VUELTA NO CORRE, Y SU HUECO ===")
w("(AUDITOR.md 6.1: corre cada cinco vueltas y la siguiente es la 189. Aqui se")
w(" mide QUE HAY en disco para poder declarar el hueco con su nombre, sus bytes")
w(" y su atribucion, que son las tres piezas juntas o no vale)")
for r in ("docs/loop/SALIDA_V187_BATERIA.txt", "docs/loop/SALIDA_V186_BATERIA.txt",
          "docs/loop/SALIDA_V185_BATERIA.txt", "docs/loop/SALIDA_V184_BATERIA.txt",
          "docs/loop/SALIDA_V183_BATERIA.txt"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        sd, sl, bd, bl = sha_de(p)
        w("   %s -> disco %d bytes | LF %d bytes | sha256 LF %s" % (r, bd, bl, sl))
    else:
        w("   %s -> NO EXISTE" % r)
w("")

w("=== H.8 QUE REPORTES ESTAN YA ARCHIVADOS EN docs/loop/reportes/ ===")
DIRA = os.path.join(LOOP, "reportes")
arch = sorted(os.listdir(DIRA)) if os.path.isdir(DIRA) else []
for n in arch[-8:]:
    g = bytes_de_git("docs/loop/reportes/" + n)
    w("   %s -> disco %d bytes | git %s"
      % (n, os.path.getsize(os.path.join(DIRA, n)),
         ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("CIFRA reportes archivados: %d" % len(arch))
for n in ("REPORTE_V184.md", "REPORTE_V185.md", "REPORTE_V186.md",
          "REPORTE_V187.md"):
    w("%s archivado: %s" % (n, "SI" if n in arch else "NO"))
w("")

w("=== H.9 EL ARCHIVO DE VEREDICTOS, QUE LA TAREA 2 SI PUEDE MOVER ===")
w("(el encargo da ea6e850d331d14f0 como sha256 LF de apertura. AQUI NO SE COPIA:")
w(" se computa. Si la TAREA 2 mueve algo, el de cierre TIENE que ser distinto)")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
datos_ver = io.open(VER, "rb").read()
w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> disco %d bytes | LF %d bytes"
  % (os.path.getsize(VER), len(datos_ver.replace((chr(13) + NL).encode(), NL.encode()))))
w("   sha256 (disco): %s" % hashlib.sha256(datos_ver).hexdigest())
w("   sha256 (LF)   : %s"
  % hashlib.sha256(datos_ver.replace((chr(13) + NL).encode(), NL.encode())).hexdigest())
filas = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
w("   CIFRA filas: %d" % len(filas))
por_clase = {}
for f in filas:
    por_clase[f.get("clase")] = por_clase.get(f.get("clase"), 0) + 1
for k in sorted(por_clase, key=lambda x: (x is None, x)):
    w("   CIFRA clase %-6s: %d" % (repr(k), por_clase[k]))
puestos_v = [f.get("puesto_intra") for f in filas]
w("   MIN puesto %s | MAX puesto %s | HUECOS %d | DUPLICADOS %d"
  % (min(puestos_v), max(puestos_v),
     len(set(range(min(puestos_v), max(puestos_v) + 1)) - set(puestos_v)),
     len(puestos_v) - len(set(puestos_v))))
w("   EL PAR 2464, PEGADO ENTERO ANTES DE TOCARLO (TAREA 2):")
for f in filas:
    if f.get("puesto_intra") == 2464:
        for k in sorted(f.keys()):
            w("      %-22s %s" % (k, str(f[k])[:200]))
w("")
w("FIN DEL SELLO DE APERTURA")

texto = NL.join(lineas) + NL
io.open(os.path.join(LOOP, "SALIDA_V%s_APERTURA.txt" % SUFIJO), "w",
        encoding="utf-8", newline=NL).write(texto)
print(texto)
escribir("HEAD", head + NL)

# ------------------------------------------------- B. EL BLOQUE DE MEDICIONES
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

# EL DESFASE DEL CALIBRADO, EN SU SITIO Y NO AL CIERRE (EJECUTOR.md 1). Desde la
# 178, una columna de apertura medida al cierre es CAIDA QUE ACUMULA.
c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + "\nEXITCODE: %d\n" % c)

c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d\n" % c)

c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + "\nEXITCODE: %d\n" % c)

print("BLOQUE DE APERTURA COMPLETO")
