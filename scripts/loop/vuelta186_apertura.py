# -*- coding: utf-8 -*-
r"""vuelta186_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 186, ENTERO Y
ANTES DE LA PRIMERA OPERACION.

CLON DECLARADO de scripts/loop/vuelta185_apertura.py. Cambia el SUFIJO de las
salidas (186, computado del nombre del fichero), la lista RUTAS_DEL_ENCARGO, las
lineas del regimen y los bloques H, que aqui miden lo que ESTE encargo promete y
nada mas. Y LA AFIRMACION DE CLON SE MIDE: el cotejo lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte con lo
que salga. NO se afirma que el diff salga vacio.

QUE ES ESTA VUELTA Y QUE NO ES. NO ES VUELTA DE BATERIA: la bateria cerro entera
en la 184 y por AUDITOR.md 6.1 corre CADA CINCO VUELTAS, asi que la siguiente es
la 189. La seccion 9 del reporte de la 186 cierra CON EL HUECO DECLARADO Y
MEDIDO. El tope sigue en DOS SUB-TAREAS (AUDITOR.md 6.2), pero la cuenta YA NO
ESTA EN CERO: la 185 cerro su propio reporte y es la PRIMERA de las dos
seguidas. Si la 186 cierra el suyo, la 187 recupera el tope de CINCO.

EL SELLO DEL AUDITOR DE ESTA VUELTA NO SE DEDUCE DEL NUMERO DE VUELTA. La casa
nombra el sello del acta N como V(N+1); siendo acta 186, el sello se llama V187.
El V186 NO EXISTE y no se fabrica: es el hueco que dejo la A.1 del acta 185. Las
rutas exactas van en RUTAS_DEL_ENCARGO y en el bloque H.5, y el sha256 se
COMPUTA y se COMPARA, no se copia del encargo.

EL BLOQUE H NO TECLEA NINGUN HASH NI NINGUNA CIFRA (EJECUTOR.md 2, EL
INSTRUMENTO MANDA). El encargo da cifras (799 bytes del sello, 39911 y 37559 de
la ciega y el destape, 4804 de mis clases, 2435 del tallador de la 184, 13982
del cuerpo, 71753 de la bateria compuesta); aqui NO SE COPIA NINGUNA: se corre y
se imprime lo que salga, y la comparacion con lo que el encargo dice se hace
despues, en el reporte, con las dos al lado.

LA CIFRA DE BYTES SE PUBLICA POR LAS DOS CONVENCIONES (acta 177 punto 7.11):
disco (os.path.getsize) y git (git cat-file -s). Y la P.2 del fundador manda
BYTES EXACTOS Y NUNCA REDONDEADOS.

POR QUE SE CORRE AQUI: EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION". El encargo manda ademas commitear lo pendiente antes de
tocar nada, y un commit MUEVE HEAD: por eso este bloque corre PRIMERO.

ESTE FICHERO NO TOCA REPORTE.md, NO toca la nomina, NO corre la bateria, NO
archiva ningun reporte y NO escribe en docs/plan/: sus salidas son
SALIDA_V186_*.txt.

LO QUE ESTA SESION SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES, Y ESCRITO CON LA LECCION DE LA R.1 DEL ACTA 186 PUESTA. Al abrir la
sesion, git status --porcelain corrido a mano dio CERO lineas y
git diff --numstat -- dataset/ dio CERO filas. PERO ESTE FICHERO YA ESTA
ESCRITO Y NO ESTA SEGUIDO POR GIT CUANDO EL BLOQUE C CORRE, asi que la
prediccion para el bloque C es UNA linea de interrogantes (esta misma), no cero.
La caida R.1 del acta 186 fue exactamente eso: atribuirle al bloque C una
medicion que el bloque C contradecia. Aqui la prediccion se escribe con el
fichero ya contado, y los bloques C, D, E y F la miden sin saber lo que hay
escrito.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

USO:
  python scripts/loop/vuelta186_apertura.py
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
    "scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py",
    "scripts/loop/vuelta185_tarea1b_mutacion_sin_temporal.py",
    "scripts/loop/vuelta185_tarea1c_mutacion_bateria_continuada.py",
    "scripts/loop/serie_de_registros.py",
    "scripts/loop/vuelta185_tarea1a_registrar_acta185.py",
    "scripts/loop/vuelta185_tarea1e_relectura_al_doble.py",
    "scripts/loop/vuelta182_tarea1c_relectura_al_doble.py",
    "scripts/loop/cotejar_clon_declarado.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/tallar_cabecera_reporte.py",
    "scripts/loop/vuelta185_esqueleto_reporte.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/SELLO_APERTURA_AUDITOR_V187.json",
    "docs/loop/_auditor_v187_ciega_blind.txt",
    "docs/loop/_auditor_v187_ciega_reveal.txt",
    "docs/loop/_auditor_v187_mis_clases.txt",
    "docs/loop/_auditor_v185b_ciega_blind.txt",
    "docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt",
    "scripts/loop/_v184_cierre_texto.md",
    "docs/loop/SALIDA_V183_BATERIA.txt",
    "docs/loop/SALIDA_V185_APERTURA.txt",
    "docs/loop/SALIDA_V185_CERRAR_REPORTE.txt",
    "docs/loop/SALIDA_V185_T2A_REPORTE_184_CERRADO_EN_ROJO.md",
    "scripts/loop/_v185_cierre_texto.md",
    "docs/loop/reportes/REPORTE_V184.md",
    "docs/loop/reportes/REPORTE_V185.md",
    "docs/PENDIENTES.md",
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
w("         seccion 9 del reporte de la 186 cierra CON EL HUECO DECLARADO Y")
w("         MEDIDO por el carril de cerrar_reporte.py: nombre, bytes y")
w("         atribucion, las tres juntas o no vale.")
w("         DOS sub-tareas, que es el tope del regimen temporal 6.2, PERO LA")
w("         CUENTA YA NO ESTA EN CERO: la 185 SI cerro su propio reporte y es la")
w("         PRIMERA de las dos seguidas. Si esta vuelta cierra el suyo, la 187")
w("         recupera el tope de CINCO.")
w("         EL SELLO DEL AUDITOR SE LLAMA V187, no V186: la casa nombra el sello")
w("         del acta N como V(N+1) y esta es el acta 186. El V186 no existe.")
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

w("=== B.1 LA CADENA DE LA VUELTA 185, LOCALIZADA EN GIT Y NO TECLEADA ===")
w("(no se teclea ningun hash: se busca en el log el commit de cada pieza de la")
w(" 185 y se imprime lo que salga)")
c, logtodo = git(["log", "--format=%h%x09%s", "-120"])
for etiqueta, aguja in (("acta 185", "ACTA DEL AUDITOR, VUELTA 185"),
                        ("acta 186", "ACTA DEL AUDITOR, VUELTA 186"),
                        ("tarea 1 de la 185", "VUELTA 185, TAREA 1 CERRADA"),
                        ("tarea 2 de la 185", "VUELTA 185, TAREA 2 ANEXADA"),
                        ("cierre de la 185", "VUELTA 185 CERRADA")):
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

w("=== H.1 LAS TRES PIEZAS CON LAS QUE SE CERRARA EL REPORTE DE LA 184 ===")
w("(TAREA 2.c. El encargo da tres cifras y aqui NO SE COPIA NINGUNA: se mide")
w(" cada pieza por las dos convenciones y con su sha256, y la comparacion con lo")
w(" que la 184 midio y la 185 confirmo se hace despues, en el reporte)")
for r in ("docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt",
          "scripts/loop/_v184_cierre_texto.md",
          "docs/loop/SALIDA_V183_BATERIA.txt"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if not os.path.exists(p):
        w("   %s -> NO EXISTE. Sin ella no se cierra nada, y eso se dice." % r)
        continue
    sd, sl, bd, bl = sha_de(p)
    w("   %s" % r)
    w("      disco %d bytes | LF %d bytes" % (bd, bl))
    w("      sha256 (disco): %s" % sd)
    w("      sha256 (LF)   : %s" % sl)
    g = bytes_de_git(r)
    w("      git cat-file -s HEAD: %s"
      % (("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("")

w("=== H.2 LAS SEDES QUE HAY QUE REPARAR, MEDIDAS ANTES DE TOCARLAS ===")
w("(TAREA 2.a, 2.b y 2.c. No se teclea ninguna linea: se localiza en el fichero")
w(" vivo y se pega lo que salga, sea la linea que el encargo dice o no)")
CER = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
t_cer = io.open(CER, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_cer = t_cer.split(NL)
w("   scripts/loop/cerrar_reporte.py -> %d lineas | disco %d bytes"
  % (len(l_cer), os.path.getsize(CER)))
for aguja in ("ajena != vuelta", "HUECO_CABECERA in texto", "def cifras_sin_pareja",
              "def piezas_que_faltan", "def rama_de_la_seccion9",
              "def tramos_por_vuelta", "def vuelta_que_sello",
              "dentro_de_cerca", "def parrafos_fuera_de_cerca"):
    hits = [(i, l) for i, l in enumerate(l_cer, 1) if aguja in l]
    w("   %-34s -> %d aparicion(es), lineas %s"
      % (repr(aguja), len(hits), ", ".join(str(i) for i, _l in hits[:10]) or "(ninguna)"))
w("   LAS DOS COPIAS DE LA COMPARACION, PEGADAS ENTERAS CON SU LINEA:")
for i, l in enumerate(l_cer, 1):
    if "ajena != vuelta" in l or "HUECO_CABECERA in texto" in l:
        w("      LINEA %d: %s" % (i, l.rstrip()[:150]))
w("   EL ARNES VIEJO QUE SIGUE MANDANDO SOBRE LAS TRES, CORRIDO HOY ANTES DE")
w("   TOCAR NADA:")
RARN = "scripts/loop/vuelta182_tarea1b_arnes_rama_seccion9.py"
c_ar, o_ar = correr([PY, RARN])
w("      EXITCODE: %d" % c_ar)
for l in o_ar.replace(chr(13), "").split(NL):
    if ("CIFRA" in l or "VEREDICTO" in l or "NO CALZA" in l):
        w("      | " + l.rstrip()[:150])
w("")

w("=== H.2.1 EL CASO REAL DE LA PIEZA (2), MEDIDO ANTES DE REPARAR NADA ===")
w("(la PD.5 dice que la marca aparece UNA vez y DENTRO de un bloque cercado.")
w(" Aqui se cuenta sobre el fichero real, dentro y fuera de cerca, y se pega la")
w(" linea que salga)")
RROJO = "docs/loop/SALIDA_V185_T2A_REPORTE_184_CERRADO_EN_ROJO.md"
PROJO = os.path.join(RAIZ, RROJO.replace("/", os.sep))
if os.path.exists(PROJO):
    t_rojo = io.open(PROJO, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    w("   %s -> disco %d bytes | LF %d bytes | lineas %d"
      % (RROJO, os.path.getsize(PROJO), len(t_rojo.encode("utf-8")),
         t_rojo.count(NL)))
    dentro_c = False
    n_dentro = n_fuera = 0
    for i, l in enumerate(t_rojo.split(NL), 1):
        if l.lstrip().startswith("```"):
            dentro_c = not dentro_c
            continue
        if "PENDIENTE DE TALLAR AL CIERRE" in l:
            if dentro_c:
                n_dentro += 1
            else:
                n_fuera += 1
            w("      LINEA %d (%s cerca): %s"
              % (i, "DENTRO de" if dentro_c else "FUERA de toda", l.strip()[:120]))
    w("   CIFRA apariciones DENTRO de cerca: %d" % n_dentro)
    w("   CIFRA apariciones FUERA de cerca: %d" % n_fuera)
else:
    w("   %s -> NO EXISTE" % RROJO)
w("")
w("=== H.3 LOS DOS ARNESES QUE FALTAN EN LA NOMINA (TAREA 1.b) ===")
w("(el reporte de la 185 lo declaro en su D.4 y su P.3, y el acta 186 lo")
w(" verifico. Aqui se vuelve a medir HOY, sin creerle a ninguno de los dos)")
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
w("   LOS DOS ARNESES DE LA 185, MEDIDOS ANTES DE METERLOS:")
for r in ("scripts/loop/vuelta185_tarea1b_mutacion_sin_temporal.py",
          "scripts/loop/vuelta185_tarea1c_mutacion_bateria_continuada.py"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        sd, sl, bd, bl = sha_de(p)
        w("      %s -> disco %d bytes | LF %d bytes | sha256 LF %s" % (r, bd, bl, sl))
    else:
        w("      %s -> NO EXISTE" % r)
w("   Y SUS SALIDAS SELLADAS, QUE SON LAS QUE LA 189 VA A CORRER DOS VECES:")
for r in ("docs/loop/SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt",
          "docs/loop/SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        sd, sl, bd, bl = sha_de(p)
        w("      %s -> disco %d bytes | LF %d bytes | sha256 LF %s" % (r, bd, bl, sl))
    else:
        w("      %s -> NO EXISTE" % r)
w("")

w("=== H.4 LA SECCION 4 DE LA 185 Y SU APERTURA SELLADA (TAREA 2.d) ===")
w("(la R.1 del acta 186 dice que el reporte de la 185 publica cero lineas de")
w(" status y que su apertura sellada dice dos. Aqui se buscan las dos cifras en")
w(" el fichero de apertura y se pega lo que salga, sin copiar del acta)")
AP185 = os.path.join(LOOP, "SALIDA_V185_APERTURA.txt")
if os.path.exists(AP185):
    t_ap = io.open(AP185, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    w("   docs/loop/SALIDA_V185_APERTURA.txt -> disco %d bytes | lineas %d"
      % (os.path.getsize(AP185), t_ap.count(NL)))
    for i, l in enumerate(t_ap.split(NL), 1):
        if "CIFRA lineas de status" in l or "AL ENTRAR" in l:
            w("      LINEA %d: %s" % (i, l.strip()[:150]))
else:
    w("   docs/loop/SALIDA_V185_APERTURA.txt -> NO EXISTE")
REP185 = os.path.join(LOOP, "reportes", "REPORTE_V185.md")
if os.path.exists(REP185):
    t_r5 = io.open(REP185, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    l_r5 = t_r5.split(NL)
    w("   docs/loop/reportes/REPORTE_V185.md -> disco %d bytes | lineas %d"
      % (os.path.getsize(REP185), t_r5.count(NL)))
    i4 = [i for i, l in enumerate(l_r5, 1) if l.startswith("## 4.")]
    i5 = [i for i, l in enumerate(l_r5, 1) if l.startswith("## 5.")]
    w("   seccion 4 empieza en la linea %s y la 5 en la %s"
      % (i4[0] if i4 else "(ninguna)", i5[0] if i5 else "(ninguna)"))
    if i4:
        fin = i5[0] if i5 else len(l_r5) + 1
        sec4 = l_r5[i4[0] - 1:fin - 1]
        w("   CIFRA lineas de la seccion 4: %d" % len(sec4))
        for k, l in enumerate(sec4, i4[0]):
            if ("status" in l or "numstat" in l or "CIFRA" in l):
                w("      LINEA %d: %s" % (k, l.strip()[:150]))
else:
    w("   docs/loop/reportes/REPORTE_V185.md -> NO EXISTE")
CT185 = os.path.join(RAIZ, "scripts", "loop", "_v185_cierre_texto.md")
if os.path.exists(CT185):
    t_c5 = io.open(CT185, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    w("   scripts/loop/_v185_cierre_texto.md -> disco %d bytes | lineas %d"
      % (os.path.getsize(CT185), t_c5.count(NL)))
    for i, l in enumerate(t_c5.split(NL), 1):
        if "status" in l or "numstat" in l:
            w("      LINEA %d: %s" % (i, l.strip()[:150]))
else:
    w("   scripts/loop/_v185_cierre_texto.md -> NO EXISTE")
w("")

w("=== H.5 EL SELLO DEL AUDITOR V187 Y SU CIEGA (TAREA 1.c) ===")
w("(el encargo manda cotejar el sha256 del fichero ciego contra el sello ANTES")
w(" de releer nada. AQUI NO SE COPIA EL DEL ENCARGO: se computa y se compara.")
w(" Y el nombre del sello NO se deduce del numero de vuelta: siendo acta 186, el")
w(" sello se llama V187, y el V186 no existe)")
SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_V187.json")
if os.path.exists(SELLO):
    w("   docs/loop/SELLO_APERTURA_AUDITOR_V187.json -> disco %d bytes"
      % os.path.getsize(SELLO))
    sello = json.loads(io.open(SELLO, encoding="utf-8").read())
    w("   CLAVES DEL SELLO: %s" % ", ".join(sorted(sello.keys())))
    w("   EL SELLO ENTERO, PEGADO Y NO RESUMIDO:")
    for l in json.dumps(sello, indent=2, ensure_ascii=False).split(NL):
        w("      | " + l[:150])
else:
    w("   EL SELLO NO EXISTE. Sin el no se relee nada, y eso se dice.")
for nombre in ("_auditor_v187_ciega_blind.txt", "_auditor_v187_ciega_reveal.txt",
               "_auditor_v187_mis_clases.txt", "_auditor_v185b_ciega_blind.txt"):
    p = os.path.join(LOOP, nombre)
    if not os.path.exists(p):
        w("   docs/loop/%s -> NO EXISTE" % nombre)
        continue
    sd, sl, bd, bl = sha_de(p)
    t_c = io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    puestos = sorted({int(x) for x in re.findall(r"PUESTO\s+(\d+)", t_c)})
    w("   docs/loop/%s" % nombre)
    w("      disco %d bytes | LF %d bytes | lineas %d" % (bd, bl, t_c.count(NL)))
    w("      sha256 (disco): %s" % sd)
    w("      sha256 (LF)   : %s" % sl)
    w("      CIFRA puestos con el patron 'PUESTO <n>': %d" % len(puestos))
    w("      LOS PUESTOS: %s" % ", ".join(str(x) for x in puestos))
w("   LAS CUATRO DISCREPANCIAS QUE EL ACTA 186 NOMBRA, BUSCADAS EN LOS DOS")
w("   FICHEROS CIEGOS PARA SABER SI ESTAN DENTRO DEL UNIVERSO:")
CUATRO = [338, 491, 1775, 2599]
for nombre in ("_auditor_v187_ciega_blind.txt", "_auditor_v185b_ciega_blind.txt"):
    p = os.path.join(LOOP, nombre)
    if not os.path.exists(p):
        continue
    t_c = io.open(p, encoding="utf-8", errors="replace").read()
    puestos = {int(x) for x in re.findall(r"PUESTO\s+(\d+)", t_c)}
    dentro_cuatro = [x for x in CUATRO if x in puestos]
    w("      %s -> de las cuatro estan dentro: %s"
      % (nombre, ", ".join(str(x) for x in dentro_cuatro) or "(ninguna)"))
w("")
w("=== H.6 LA SERIE DE REGISTROS Y EL ACTA 186 (TAREA 1.a) ===")
w("(no se teclea ningun numero de registro: se llama a serie_de_registros.py y")
w(" se imprime lo que devuelva. R.48 NO se da por bueno porque lo diga el encargo)")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
t_acta = io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
l_acta = t_acta.split(NL)
w("docs/loop/ACTA_AUDITOR.md -> %d lineas | disco %d bytes | LF %d bytes"
  % (len(l_acta), os.path.getsize(ACTA), len(t_acta.encode("utf-8"))))
CAB186 = [i for i, l in enumerate(l_acta, 1)
          if l.startswith("# ACTA DEL AUDITOR, VUELTA 186")]
w("CIFRA cabeceras del acta 186 encontradas: %d" % len(CAB186))
if CAB186:
    base = CAB186[0]
    w("   CABECERA del acta 186 en la LINEA %d" % base)
    w("   lineas del acta 186, de su cabecera al final del fichero: %d"
      % (len(l_acta) - base + 1))
    for aguja in ("## 1. ", "## 2. ", "## 3. ", "## 4. ", "## 5. ", "## 6. ",
                  "## 7. ", "## 8. ", "## 9. ", "## 10. ", "## 11. ", "## 12. ",
                  "## 13. "):
        hits = [i for i, l in enumerate(l_acta, 1)
                if l.startswith(aguja) and i >= base]
        w("   %-10s -> lineas %s"
          % (repr(aguja), ", ".join(str(x) for x in hits) or "(ninguna)"))
    w("   LOS NUMERALES DEL ACTA 186, CONTADOS CON EL PATRON DE COMILLAS")
    w("   INVERSAS QUE LA 184 ESTRENO, Y NO DE MEMORIA:")
    for pat in (r"\*\*`5\.(\d)`", r"\*\*`6\.(\d)`", r"\*\*`7\.(\d)`",
                r"`PD\.(\d)`", r"`A\.(\d)`", r"`R\.(\d)`"):
        hits = [(i, m.group(1)) for i, l in enumerate(l_acta, 1) if i >= base
                for m in [re.search(pat, l)] if m]
        vistos = sorted({v for _i, v in hits})
        w("      %-16s -> %d aparicion(es), numerales distintos %s"
          % (pat, len(hits), ", ".join(vistos) or "(ninguno)"))
    w("   LAS CABECERAS 5.n, 6.n Y 7.n DEL ACTA 186, PEGADAS ENTERAS:")
    for i, l in enumerate(l_acta, 1):
        if i >= base and re.match(r"^\*\*`[567]\.\d`", l):
            w("      LINEA %d: %s" % (i, l.strip()[:140]))
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
for r in ("docs/loop/SALIDA_V186_BATERIA.txt", "docs/loop/SALIDA_V185_BATERIA.txt",
          "docs/loop/SALIDA_V184_BATERIA.txt", "docs/loop/SALIDA_V183_BATERIA.txt"):
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
for n in ("REPORTE_V183.md", "REPORTE_V184.md", "REPORTE_V185.md",
          "REPORTE_V186.md"):
    w("%s archivado: %s" % (n, "SI" if n in arch else "NO"))
w("")

w("=== H.9 EL ARCHIVO DE VEREDICTOS, QUE ESTA VUELTA NO PUEDE MOVER ===")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
datos_ver = io.open(VER, "rb").read()
w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> disco %d bytes | LF %d bytes"
  % (os.path.getsize(VER), len(datos_ver.replace(chr(13).encode(), b""))))
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
