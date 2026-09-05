# -*- coding: utf-8 -*-
r"""vuelta178_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 178, ENTERO.

CLON DECLARADO de scripts/loop/vuelta177_apertura.py. Cambia el numero de
vuelta, el prefijo de las salidas, la lista RUTAS_DEL_ENCARGO y el bloque H, que
aqui mide lo que ESTE encargo promete y nada mas.

Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA. Desde la vuelta 178 ningun
reporte escribe "CLON DECLARADO" sin pegar la salida de
scripts/loop/cotejar_clon_declarado.py (ultima linea del docstring de ese
fichero antes del USO). Este docstring NO afirma que el diff salga vacio: la
vuelta 176 cayo por eso, y el cotejo de este clon se pega en el reporte.

ESTA VUELTA NO ES DE BATERIA. La cadencia esta adjudicada en el acta 176 punto
7.8 y reconfirmada por el encargo de esta vuelta: la proxima vuelta de bateria es
la 181. Por eso la seccion 9 del reporte cerrara con el HUECO DECLARADO Y MEDIDO,
y el bloque H de esta apertura NO mide la nomina como sujeto de bateria: mide LOS
SUJETOS DE LAS CINCO TAREAS.

EL TOPE VUELVE A CINCO SUB-TAREAS, Y NO LO DECIDE NADIE: LO DISPARA LA LETRA DE
AUDITOR.md 6.2, que dice que el regimen de dos dura HASTA QUE DOS VUELTAS
SEGUIDAS CIERREN SU PROPIO REPORTE con cerrar_reporte.py. El bloque B.1 de abajo
LOCALIZA EN GIT esos cuatro commits en vez de teclearlos, porque EJECUTOR.md 1
dice que todo hash que el reporte publique se lee de git en esa vuelta.

EL BLOQUE H NO TECLEA NINGUN HASH NI NINGUNA CIFRA. Todo se localiza y se imprime
lo que salga. Las cifras vivas de la nomina y del censo NO se copian del encargo
ni del acta: se recomputan llamando a las funciones puras del propio sujeto, que
es la unica fuente que la casa reconoce (EJECUTOR.md 2, EL INSTRUMENTO MANDA). El
encargo dice que el censo ve 154 y que faltaban tres; aqui no se copia ninguno de
los dos numeros, se corren las funciones.

LA CIFRA DE BYTES SE PUBLICA POR LAS DOS CONVENCIONES mientras la convencion no
este fijada (acta 177 punto 7.11): disco (os.path.getsize) y git (git cat-file
-s), las dos a la vez.

POR QUE SE CORRE AQUI: EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION". Este fichero NO toca REPORTE.md, NO toca la nomina, NO corre
la bateria y NO escribe en docs/plan/: sus salidas son SALIDA_V178_*.txt.

Y LA MEDICION DE DESFASE DEL CALIBRADO SE TOMA AQUI, EN SU SITIO. El encargo lo
dice con dientes: con el remedio puesto en la 177 (la linea que corre el medidor
dentro de vuelta177_apertura.py), la columna de apertura medida al cierre pasa a
ser CAIDA QUE ACUMULA. Aqui corre dentro del bloque B, antes de toda operacion.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

LO QUE ESTA VUELTA SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano al abrir la vuelta, dio CERO
lineas, y scripts/loop/guarda_commit_dataset.py salio VERDE con 0 filas de
numstat, 0 ficheros nombrados y 0 blobs divergentes. La prediccion se escribe
AQUI, antes de correr, y los bloques C/D/E/F de abajo la miden sin saber lo que
hay escrito.

USO:
  python scripts/loop/vuelta178_apertura.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
VUELTA = 178

# LOS SUJETOS DE CODIGO DE LAS CINCO TAREAS, nombrados aqui para que el bloque H
# no los pueda elegir despues de ver el resultado.
SUJETOS = [
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/cotejar_clon_declarado.py",
    "scripts/loop/aislador_de_ciega.py",
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/_auditor_v178_ciega.py",
    "scripts/loop/backlog_l03_vuelta14.py",
    "scripts/loop/vuelta166_tarea2_correccion_op_l_01.py",
    "scripts/loop/vuelta150_3_relectura_expediente.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/reportes/REPORTE_V177.md",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/OP_L_03_LECTURAS.jsonl",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "scripts/loop/guarda_commit_dataset.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/anexar_tarea_al_reporte.py",
    "scripts/loop/tallar_cabecera_reporte.py",
] + SUJETOS


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
    """Los bytes que git guarda para esa ruta en HEAD, o None si no esta.
    LA SEGUNDA CONVENCION del hallazgo 4.1 del acta 174, medida y no supuesta."""
    c, o = git(["cat-file", "-s", "HEAD:" + ruta])
    o = o.strip()
    return int(o) if c == 0 and o.isdigit() else None


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V%d_%s_APERTURA.txt" % (VUELTA, nombre))
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("ESCRITO: %s (%d bytes)" % (os.path.basename(ruta), len(texto.encode("utf-8"))))


# ---------------------------------------------------------------- A. EL SELLO
lineas = []
w = lineas.append
NL = chr(10)
w("SELLO DE APERTURA DE LA VUELTA %d, escrito ANTES de la primera operacion" % VUELTA)
w("instrumento: scripts/loop/vuelta%d_apertura.py" % VUELTA)
w("regimen: VUELTA NORMAL, NO DE BATERIA (la proxima es la 181).")
w("         CINCO sub-tareas: el regimen temporal de AUDITOR.md 6.2 queda")
w("         CUMPLIDO por dos vueltas seguidas que cerraron su reporte, y el")
w("         bloque B.1 de abajo lo LOCALIZA EN GIT en vez de teclearlo.")
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
w("adelante/atras contra el remoto (HEAD...upstream): " + (ahead.strip() if c == 0 else "(no medible)"))
w("")

w("=== B.1 LOS CUATRO COMMITS QUE DEVUELVEN EL TOPE A CINCO, LOCALIZADOS EN GIT ===")
w("(AUDITOR.md 6.2: el regimen de dos dura HASTA QUE DOS VUELTAS SEGUIDAS")
w(" CIERREN SU PROPIO REPORTE con cerrar_reporte.py. No se teclea ningun hash:")
w(" se busca en el log el commit de CIERRE y el de ARCHIVO de la 176 y de la 177)")
c, logtodo = git(["log", "--format=%h%x09%s", "-40"])
for etiqueta, aguja in (("176 cierre", "REPORTE DE LA 176"),
                        ("176 archivo", "REPORTE_V176.md"),
                        ("177 cierre", "REPORTE DE LA 177"),
                        ("177 archivo", "REPORTE_V177.md")):
    hits = [l for l in logtodo.splitlines() if aguja.upper() in l.upper()]
    w("   %-12s -> %s" % (etiqueta, (hits[0][:150] if hits else "NO LOCALIZADO EN LOS 40 ULTIMOS")))
c, n_cerrar = git(["log", "--format=%h", "-40", "--", "scripts/loop/cerrar_reporte.py"])
w("   commits que tocan cerrar_reporte.py en los 40 ultimos: %d"
  % len([l for l in n_cerrar.splitlines() if l.strip()]))
w("")

w("=== C. git status --porcelain ENTERO ===")
c, st = git(["status", "--porcelain"])
for l in st.splitlines():
    w(l)
w("CIFRA lineas de status: %d" % len([l for l in st.splitlines() if l.strip()]))
w("")

w("=== D. BYTES DE CADA RUTA QUE EL ENCARGO NOMBRA, POR LAS DOS CONVENCIONES ===")
w("(disco = os.path.getsize; git = git cat-file -s HEAD:<ruta>. Acta 177 punto")
w(" 7.11: mientras la convencion no este fijada, SE PUBLICAN LAS DOS)")
for ruta in RUTAS_DEL_ENCARGO:
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    g = bytes_de_git(ruta)
    if os.path.exists(p):
        w("%s -> disco %d bytes | git %s"
          % (ruta, os.path.getsize(p), ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
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
    w("   %s -> git diff --numstat: %d filas" % (ruta, len([l for l in dn.splitlines() if l.strip()])))
w("CIFRA ficheros modificados: %d" % n_mod)
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
c, rep = git(["show", "HEAD:docs/loop/REPORTE.md"])
w("primera linea: %s" % (rep.split(NL, 1)[0].strip() if rep else "(vacio)"))
w("lineas (saltos de linea contados): %d" % rep.count(NL))
w("bytes en git: %d" % len(rep.encode("utf-8")))
MARCAS = ["SIN ESCRIBIR TODAVIA", "PENDIENTE DE TALLAR AL CIERRE",
          "ABIERTA, SIN CERRAR", "HUECO DECLARADO Y MEDIDO"]
MARCAS = MARCAS + [NL + "## %d." % k for k in range(3, 10)]
for marca in MARCAS:
    w("   contiene %-34s -> %s" % (repr(marca), "SI" if marca in rep else "NO"))
w("")

w("=== H.1 EL REPORTE DEL ARBOL, QUE ES EL QUE EL ESQUELETO DE LA 178 PISARA ===")
RUTA_REP = os.path.join(LOOP, "REPORTE.md")
arbol = io.open(RUTA_REP, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("primera linea: %s" % arbol.split(NL, 1)[0].strip())
w("bytes en disco (normalizado a LF): %d | saltos de linea: %d"
  % (len(arbol.encode("utf-8")), arbol.count(NL)))
w("bytes en disco (crudos, os.path.getsize): %d" % os.path.getsize(RUTA_REP))
w("identico byte a byte al de HEAD: %s"
  % ("SI" if arbol == rep.replace(chr(13) + NL, NL) else "NO"))
for marca in MARCAS:
    w("   contiene %-34s -> %s" % (repr(marca), "SI" if marca in arbol else "NO"))
w("")

w("=== H.2 EL COMMIT QUE DE VERDAD TOCA REPORTE.md POR ULTIMA VEZ ===")
w("(no se teclea ningun hash: se localiza con git log y se imprime lo que salga)")
c, cual = git(["log", "--format=%h%x09%s", "-8"])
w("los ocho ultimos commits:")
for l in cual.splitlines():
    w("   " + l[:150])
c, ult = git(["log", "-1", "--format=%h", "--", "docs/loop/REPORTE.md"])
w("ultimo commit que TOCA docs/loop/REPORTE.md: %s" % ult.strip())
c, asu = git(["log", "-1", "--format=%s", ult.strip()])
w("   su asunto: %s" % asu.strip()[:150])
w("")

w("=== H.3 LAS PIEZAS QUE cerrar_reporte.py PEDIRA PARA CERRAR LA 178 ===")
w("(al abrir NO EXISTE NINGUNA, y eso es lo correcto: las produce esta vuelta.")
w(" La de bateria NO SE VA A PRODUCIR: esta vuelta no es de bateria y la seccion")
w(" 9 cierra con el HUECO DECLARADO Y MEDIDO)")
for r in ["docs/loop/SALIDA_V178_TALLADOR_CABECERA.txt",
          "scripts/loop/_v178_cierre_texto.md",
          "docs/loop/SALIDA_V178_BATERIA.txt"]:
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        w("%s -> %d bytes" % (r, os.path.getsize(p)))
    else:
        w("%s -> NO EXISTE" % r)
w("")

w("=== H.4 QUE REPORTES ESTAN YA ARCHIVADOS EN docs/loop/reportes/ ===")
DIRA = os.path.join(LOOP, "reportes")
arch = sorted(os.listdir(DIRA)) if os.path.isdir(DIRA) else []
for n in arch:
    g = bytes_de_git("docs/loop/reportes/" + n)
    w("   %s -> disco %d bytes | git %s"
      % (n, os.path.getsize(os.path.join(DIRA, n)),
         ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("CIFRA reportes archivados: %d" % len(arch))
w("REPORTE_V177.md archivado: %s" % ("SI" if "REPORTE_V177.md" in arch else "NO"))
w("")

w("=== H.5 LA CUENTA DE LA NOMINA Y DEL CENSO, RECOMPUTADA (TAREA 1.a) ===")
w("(el encargo dice que el censo ve 154 y que la nomina va de 88 a 92. NI UNO")
w(" NI OTRO SE COPIAN: se llaman las funciones puras del propio sujeto)")
try:
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_mutaciones_viejas as VMV   # noqa: E402
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _a in VMV.VIEJAS]
    invis = VMV.nomina_invisible_al_censo()
    fuera = sorted(set(censo) - set(nomina))
    w("CIFRA arneses que ve arneses_del_directorio(): %d" % len(censo))
    w("CIFRA entradas de VIEJAS (la nomina): %d" % len(nomina))
    w("CIFRA entradas de la nomina que el censo NO ve (nomina_invisible_al_censo): %d"
      % len(invis))
    for n in invis:
        w("     %s" % n)
    w("CIFRA del censo que estan FUERA de la nomina: %d" % len(fuera))
    w("LA RESTA COMPROBADA: censo %d menos nomina %d = %d, y fuera de nomina = %d. CALZAN: %s"
      % (len(censo), len(nomina), len(censo) - len(nomina), len(fuera),
         "SI" if (len(censo) - len(nomina)) == len(fuera) else "NO"))
    ultima, faltan = VMV.arneses_que_faltan()
    w("arneses_que_faltan() HOY, CON LA FUNCION VIEJA:")
    w("   ultima vuelta de la nomina: %s" % ultima)
    w("   CIFRA que dice que faltan: %d" % len(faltan))
    for n in faltan:
        w("      %s" % n)
    w("   CIFRA que la funcion NO VE y el censo SI (fuera de nomina menos los que dice): %d"
      % len(set(fuera) - set(faltan)))
except Exception as e:
    w("NO SE PUDO RECOMPUTAR: %r" % (e,))
w("")

w("=== H.6 EL CUARTO VEREDICTO DEL COTEJO DE CLONES, MEDIDO ANTES (TAREA 1.c) ===")
COT = os.path.join(RAIZ, "scripts", "loop", "cotejar_clon_declarado.py")
t_cot = io.open(COT, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("scripts/loop/cotejar_clon_declarado.py: %d lineas" % t_cot.count(NL))
for aguja in ("EL ARBOL DE SINTAXIS", "ast_identico", "ast.dump", "TRES VEREDICTOS",
              "CUATRO VEREDICTOS"):
    w("   nombra %-24s -> %s" % (repr(aguja), "SI" if aguja in t_cot else "NO"))
w("")

w("=== H.7 EL --puestos DEL AISLADOR, MEDIDO ANTES (TAREA 1.d) ===")
AIS = os.path.join(RAIZ, "scripts", "loop", "aislador_de_ciega.py")
t_ais = io.open(AIS, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("scripts/loop/aislador_de_ciega.py: %d lineas" % t_ais.count(NL))
for aguja in ("--puestos", "--excluir", "puestos=", "excluir="):
    w("   nombra %-14s -> %s" % (repr(aguja), "SI" if aguja in t_ais else "NO"))
MUL = os.path.join(RAIZ, "scripts", "loop", "_auditor_v178_ciega.py")
w("la muleta del auditor scripts/loop/_auditor_v178_ciega.py existe: %s"
  % ("SI" if os.path.exists(MUL) else "NO"))
if os.path.exists(MUL):
    g = bytes_de_git("scripts/loop/_auditor_v178_ciega.py")
    w("   disco %d bytes | git %s"
      % (os.path.getsize(MUL), ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
    t_mul = io.open(MUL, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("   importa aislador_de_ciega (no copia sus funciones): %s"
      % ("SI" if "aislador_de_ciega" in t_mul else "NO"))
w("")

w("=== H.8 LA GUARDA DE LA PAREJA DE BYTES Y SHA, MEDIDA ANTES (TAREA 1.e) ===")
CER = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
t_cer = io.open(CER, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("scripts/loop/cerrar_reporte.py: %d lineas" % t_cer.count(NL))
for aguja in ("PATRON_BYTES", "normalizado a LF", "cifras_sin_pareja", "sha sin su pareja"):
    w("   nombra %-22s -> %s" % (repr(aguja), "SI" if aguja in t_cer else "NO"))
w("")

w("=== H.9 LA GUARDA DEL SUJETO CONGELADO, MEDIDA ANTES (TAREA 1.e) ===")
BAT = os.path.join(RAIZ, "scripts", "loop", "verificar_mutaciones_viejas.py")
t_bat = io.open(BAT, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("scripts/loop/verificar_mutaciones_viejas.py: %d lineas" % t_bat.count(NL))
w("CIFRA veces que dice 'SUJETO CONGELADO': %d" % t_bat.count("SUJETO CONGELADO"))
for aguja in ("def sujeto_congelado", "def anclaje_de", "CASOS_DECLARADOS",
              "--sujeto-congelado"):
    w("   nombra %-24s -> %s" % (repr(aguja), "SI" if aguja in t_bat else "NO"))
w("")

w("=== H.10 EL UNIVERSO DE OP-L-03, RECOMPUTADO Y NO COPIADO DE SU NOTA (TAREA 2) ===")
w("(la cifra adjudicada en la vuelta 15 es 40 actos y 73 pares, al corte 3.388.")
w(" Se corre el instrumento que la propia nota cita y se imprime lo que salga)")
c, o = correr([PY, "scripts/loop/backlog_l03_vuelta14.py"])
w("comando: python scripts/loop/backlog_l03_vuelta14.py -> exit %d" % c)
for l in o.split(NL):
    if l.strip():
        w("   " + l.rstrip()[:160])
w("")

w("=== H.11 LOS SEIS ACTOS YA LEIDOS, CONTADOS DE SU REGISTRO ===")
REG = os.path.join(RAIZ, "docs", "plan", "OP_L_03_LECTURAS.jsonl")
if os.path.exists(REG):
    ls_reg = [l for l in io.open(REG, encoding="utf-8").read().split(NL) if l.strip()]
    w("docs/plan/OP_L_03_LECTURAS.jsonl -> %d filas, disco %d bytes"
      % (len(ls_reg), os.path.getsize(REG)))
else:
    w("docs/plan/OP_L_03_LECTURAS.jsonl -> NO EXISTE")
w("")

w("=== H.12 LA VARA DEL TRABAJO PENDIENTE, CORRIDA EN ESTA VUELTA (TAREA 4) ===")
w("(la vara es scripts/loop/vuelta150_3_relectura_expediente.py y NUNCA el campo")
w(" estado, decision del fundador del 4 sep 2026)")
c, o = correr([PY, "scripts/loop/vuelta150_3_relectura_expediente.py", "--corte", head])
w("comando: vuelta150_3_relectura_expediente.py --corte %s -> exit %d" % (head[:8], c))
for l in o.split(NL):
    if ("LISTA" in l or "CIFRA" in l or "OP-L-03" in l or "OP-M-02" in l
            or "CONSUMIDA" in l):
        w("   " + l.rstrip()[:160])
VAR = os.path.join(RAIZ, "scripts", "loop", "vuelta150_3_relectura_expediente.py")
t_var = io.open(VAR, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("la vara nombra CONSUMIDA hoy: %s" % ("SI" if "CONSUMIDA" in t_var.upper() else "NO"))
w("")

w("=== H.13 LOS CINCO TRIANGULOS, LOCALIZADOS EN EL REPORTE DE LA 177 (TAREA 3) ===")
c, r177 = git(["show", "HEAD:docs/loop/reportes/REPORTE_V177.md"])
for i, l in enumerate(r177.split(NL), 1):
    if "triangulo" in l.lower() and l.strip().startswith("|"):
        w("   LINEA %d: %s" % (i, l.strip()[:180]))
w("CIFRA veces que el reporte 177 dice 'triangulo': %d" % r177.lower().count("triangulo"))
w("")

w("FIN DEL SELLO DE APERTURA")

texto = NL.join(lineas) + NL
io.open(os.path.join(LOOP, "SALIDA_V%d_APERTURA.txt" % VUELTA), "w",
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

# EL DESFASE DEL CALIBRADO, EN SU SITIO Y NO AL CIERRE. El encargo de la 178 lo
# dice con dientes: con el remedio de la 177 puesto y verificado, la columna de
# apertura medida al cierre pasa a ser CAIDA QUE ACUMULA. Aqui corre en la
# apertura, antes de la primera operacion, que es donde EJECUTOR.md 1 la manda.
c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + "\nEXITCODE: %d\n" % c)

c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d\n" % c)

c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + "\nEXITCODE: %d\n" % c)

print("BLOQUE DE APERTURA COMPLETO")
