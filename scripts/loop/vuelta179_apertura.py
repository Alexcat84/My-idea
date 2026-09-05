# -*- coding: utf-8 -*-
r"""vuelta179_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 179, ENTERO.

CLON DECLARADO de scripts/loop/vuelta178_apertura.py. Cambia el numero de
vuelta, el prefijo de las salidas, la lista RUTAS_DEL_ENCARGO y el bloque H, que
aqui mide lo que ESTE encargo promete y nada mas.

Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA. Desde la vuelta 178 ningun
reporte escribe "CLON DECLARADO" sin pegar la salida de
scripts/loop/cotejar_clon_declarado.py (ultima linea del docstring de ese
fichero antes del USO). Este docstring NO afirma que el diff salga vacio: la
vuelta 176 cayo por eso, y el cotejo de este clon se pega en el reporte.

ESTA VUELTA NO ES DE BATERIA. La cadencia esta adjudicada en el acta 176 punto
7.8 y reconfirmada en el acta 178 punto 11 y por el encargo de esta vuelta: la proxima
vuelta de bateria es la 181. Por eso la seccion 9 del reporte cerrara con el HUECO
DECLARADO Y MEDIDO, y el bloque H de esta apertura NO mide la nomina como sujeto
de bateria: mide LOS SUJETOS DE LAS CINCO TAREAS.

EL TOPE SIGUE EN CINCO SUB-TAREAS: el disparador de AUDITOR.md 6.2 se cumplio en
la 177 y la 178 confirmo entregando cinco. El bloque B.1 de abajo LOCALIZA EN GIT
los commits de cierre y de archivo de la 177 y de la 178 en vez de teclearlos,
porque EJECUTOR.md 1 dice que todo hash que el reporte publique se lee de git en
esa vuelta.

EL BLOQUE H NO TECLEA NINGUN HASH NI NINGUNA CIFRA. Todo se localiza y se imprime
lo que salga. Las cifras vivas de la nomina y del censo NO se copian del encargo
ni del acta: se recomputan llamando a las funciones puras del propio sujeto, que
es la unica fuente que la casa reconoce (EJECUTOR.md 2, EL INSTRUMENTO MANDA). El
encargo no da cifra de censo ni de nomina para esta vuelta; aqui no se copiaria
aunque la diera: se corren las funciones y se imprime lo que salga.

LA CIFRA DE BYTES SE PUBLICA POR LAS DOS CONVENCIONES mientras la convencion no
este fijada (acta 177 punto 7.11, y sigue sin fijar: TAREA 5 punto 5): disco (os.path.getsize) y git (git cat-file
-s), las dos a la vez.

POR QUE SE CORRE AQUI: EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION". Este fichero NO toca REPORTE.md, NO toca la nomina, NO corre
la bateria y NO escribe en docs/plan/: sus salidas son SALIDA_V179_*.txt.

Y LA MEDICION DE DESFASE DEL CALIBRADO SE TOMA AQUI, EN SU SITIO. El encargo de la 179 lo
repite con dientes: desde la 178 una columna de apertura medida al cierre es
CAIDA QUE ACUMULA. Aqui corre dentro del bloque B, antes de toda operacion.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

LO QUE ESTA VUELTA SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano al abrir la vuelta, dio CERO
lineas, y scripts/loop/guarda_commit_dataset.py salio VERDE con 0 filas de
numstat, 0 ficheros nombrados y 0 blobs divergentes. La prediccion se escribe
AQUI, antes de correr, y los bloques C/D/E/F de abajo la miden sin saber lo que
hay escrito.

USO:
  python scripts/loop/vuelta179_apertura.py
"""
import hashlib
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
VUELTA = 179

# LOS SUJETOS DE CODIGO DE LAS CINCO TAREAS, nombrados aqui para que el bloque H
# no los pueda elegir despues de ver el resultado.
SUJETOS = [
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/vuelta178_tarea1e_mutacion_higiene.py",
    "scripts/loop/vuelta178_tarea3_anotar_triangulos.py",
    "scripts/loop/vuelta150_2d_simular_op_c_05.py",
    "scripts/loop/vuelta160_tarea3b_caso_positivo.py",
    "scripts/loop/backlog_l03_resuelto.py",
    "scripts/loop/backlog_l03_vuelta14.py",
    "scripts/loop/paso0_archivar_anterior.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/reportes/REPORTE_V178.md",
    "docs/plan/OP_L_03_TRIANGULOS.jsonl",
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
w("         CINCO sub-tareas, la 1 BLOQUEANTE. El tope de cinco de")
w("         AUDITOR.md 6.2 sigue vigente, y el bloque B.1 de abajo lo")
w("         LOCALIZA EN GIT en vez de teclearlo.")
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

w("=== B.1 LOS CUATRO COMMITS QUE SOSTIENEN EL TOPE DE CINCO, LOCALIZADOS EN GIT ===")
w("(AUDITOR.md 6.2: el regimen de dos dura HASTA QUE DOS VUELTAS SEGUIDAS")
w(" CIERREN SU PROPIO REPORTE con cerrar_reporte.py. No se teclea ningun hash:")
w(" se busca en el log el commit de CIERRE y el de ARCHIVO de la 176 y de la 177)")
c, logtodo = git(["log", "--format=%h%x09%s", "-40"])
for etiqueta, aguja in (("177 cierre", "REPORTE DE LA 177"),
                        ("177 archivo", "REPORTE_V177.md"),
                        ("178 cierre", "REPORTE DE LA 178"),
                        ("178 archivo", "REPORTE_V178.md")):
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

w("=== H.1 EL REPORTE DEL ARBOL, QUE ES EL QUE EL ESQUELETO DE LA 179 PISARA ===")
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

w("=== H.3 LAS PIEZAS QUE cerrar_reporte.py PEDIRA PARA CERRAR LA 179 ===")
w("(al abrir NO EXISTE NINGUNA, y eso es lo correcto: las produce esta vuelta.")
w(" La de bateria NO SE VA A PRODUCIR: esta vuelta no es de bateria y la seccion")
w(" 9 cierra con el HUECO DECLARADO Y MEDIDO)")
for r in ["docs/loop/SALIDA_V179_TALLADOR_CABECERA.txt",
          "scripts/loop/_v179_cierre_texto.md",
          "docs/loop/SALIDA_V179_BATERIA.txt"]:
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
w("REPORTE_V178.md archivado: %s" % ("SI" if "REPORTE_V178.md" in arch else "NO"))
w("")

w("=== H.5 LA NOMINA Y EL CENSO, RECOMPUTADOS Y CON SU CORTE (TAREA 1.c y 1.d) ===")
w("(el encargo NO da cifra de nomina ni de censo para esta vuelta, y aunque la")
w(" diera no se copiaria: se llaman las funciones puras del propio sujeto.")
w(" EL CORTE VA AL LADO por adjudicacion 7.2 del acta 178, porque el")
w(" denominador crece DENTRO de la propia vuelta: la 178 publico 15 de 92")
w(" siendo verdad y al cerrar eran 15 de 98)")
w("CORTE DE ESTA MEDICION: HEAD %s, APERTURA de la vuelta %d, antes de la" % (head[:12], VUELTA))
w("                        primera operacion de esta vuelta.")
try:
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_mutaciones_viejas as VMV   # noqa: E402
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _a in VMV.VIEJAS]
    invis = VMV.nomina_invisible_al_censo()
    fuera = sorted(set(censo) - set(nomina))
    w("CIFRA arneses que ve arneses_del_directorio(): %d" % len(censo))
    w("CIFRA entradas de VIEJAS (la nomina): %d" % len(nomina))
    w("CIFRA entradas de la nomina que el censo NO ve: %d" % len(invis))
    w("CIFRA del censo que estan FUERA de la nomina: %d" % len(fuera))
    for n in fuera:
        w("     FUERA: %s" % n)
    w("LA RESTA COMPROBADA: censo %d menos nomina %d = %d, y fuera de nomina = %d. CALZAN: %s"
      % (len(censo), len(nomina), len(censo) - len(nomina), len(fuera),
         "SI" if (len(censo) - len(nomina)) == len(fuera) else "NO"))
    ultima, faltan = VMV.arneses_que_faltan()
    w("arneses_que_faltan() HOY: ultima vuelta de la nomina %s, y dice que faltan %d"
      % (ultima, len(faltan)))
    for n in faltan:
        w("      FALTA: %s" % n)
    for r in ("scripts/loop/vuelta150_2d_simular_op_c_05.py",
              "scripts/loop/vuelta160_tarea3b_caso_positivo.py"):
        b = os.path.basename(r)
        w("   LOS DOS DESTAPADOS DE LA 178: %-46s en la nomina HOY: %s | existe en disco: %s"
          % (b, "SI" if b in nomina else "NO",
             "SI" if os.path.exists(os.path.join(RAIZ, r.replace("/", os.sep))) else "NO"))
except Exception as e:
    w("NO SE PUDO RECOMPUTAR: %r" % (e,))
w("")

w("=== H.6 LA CAIDA DE LA 178, MEDIDA ANTES DE CORREGIRLA (TAREA 1.a) ===")
w("(el encargo dice que el reporte de la 178 publica 16 donde su propio fichero")
w(" dice 18. NI UNO NI OTRO SE COPIAN: se buscan los dos y se imprime lo que salga)")
RUTA_178 = os.path.join(LOOP, "reportes", "REPORTE_V178.md")
if os.path.exists(RUTA_178):
    t178 = io.open(RUTA_178, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("docs/loop/reportes/REPORTE_V178.md -> disco %d bytes | LF %d bytes"
      % (os.path.getsize(RUTA_178), len(t178.encode("utf-8"))))
    for i, l in enumerate(t178.split(NL), 1):
        if "SALIDA_V178_T1E_MUTACION" in l or ("casos, los" in l and "pasan" in l):
            w("   LINEA %d: %s" % (i, l.strip()[:180]))
else:
    w("docs/loop/reportes/REPORTE_V178.md -> NO EXISTE")
RUTA_T1E = os.path.join(LOOP, "SALIDA_V178_T1E_MUTACION.txt")
if os.path.exists(RUTA_T1E):
    tT1E = io.open(RUTA_T1E, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("docs/loop/SALIDA_V178_T1E_MUTACION.txt -> disco %d bytes | LF %d bytes"
      % (os.path.getsize(RUTA_T1E), len(tT1E.encode("utf-8"))))
    for l in tT1E.split(NL):
        if l.strip().startswith("CIFRA") or l.strip().startswith("VERDE DE LA MUTACION"):
            w("   %s" % l.strip()[:200])
    w("   CIFRA lineas del fichero que terminan en CAE: %d"
      % len([l for l in tT1E.split(NL) if l.rstrip().endswith("CAE")]))
else:
    w("docs/loop/SALIDA_V178_T1E_MUTACION.txt -> NO EXISTE")
w("")

w("=== H.7 cerrar_reporte.py MEDIDO ANTES DE LA GUARDA NUEVA (TAREA 1.b) ===")
CER = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")
t_cer = io.open(CER, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("scripts/loop/cerrar_reporte.py: %d lineas, disco %d bytes | LF %d bytes"
  % (t_cer.count(NL), os.path.getsize(CER), len(t_cer.encode("utf-8"))))
for aguja in ("def cifras_sin_pareja", "def piezas_que_faltan",
              "def hueco_declarado_que_falta", "def citas_de_arnes_que_no_calzan",
              "SALIDA_V", "CIFRA casos que CAEN"):
    w("   nombra %-36s -> %s" % (repr(aguja), "SI" if aguja in t_cer else "NO"))
w("CIFRA funciones def de nivel cero: %d"
  % len([l for l in t_cer.split(NL) if l.startswith("def ")]))
w("")

w("=== H.8 EL UNIVERSO DE OP-L-03, RECOMPUTADO Y NO COPIADO (TAREA 2) ===")
w("(el encargo dice 73 pares del instrumento, 18 reales, 8 leidos por la 177 y 10")
w(" por leer. NINGUNO SE COPIA: se corre el filtro y se imprime lo que salga)")
c, o = correr([PY, "scripts/loop/backlog_l03_resuelto.py"])
w("comando: python scripts/loop/backlog_l03_resuelto.py -> exit %d" % c)
for l in o.split(NL):
    if l.strip() and ("CIFRA" in l or "VERDE" in l or "ROJO" in l or "TOTAL" in l):
        w("   " + l.rstrip()[:180])
REG = os.path.join(RAIZ, "docs", "plan", "OP_L_03_LECTURAS.jsonl")
if os.path.exists(REG):
    filas = [l for l in io.open(REG, encoding="utf-8").read().split(NL) if l.strip()]
    w("docs/plan/OP_L_03_LECTURAS.jsonl -> %d filas, disco %d bytes"
      % (len(filas), os.path.getsize(REG)))
    con_clases = 0
    for f in filas:
        try:
            d = json.loads(f)
        except Exception:
            continue
        if d.get("clases_de_los_pares_por_leer"):
            con_clases += 1
    w("   CIFRA filas con clases_de_los_pares_por_leer: %d" % con_clases)
else:
    w("docs/plan/OP_L_03_LECTURAS.jsonl -> NO EXISTE")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
if os.path.exists(VER):
    fv = [l for l in io.open(VER, encoding="utf-8").read().split(NL) if l.strip()]
    w("docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> %d filas, disco %d bytes"
      % (len(fv), os.path.getsize(VER)))
w("")

w("=== H.9 LOS TRIANGULOS, MEDIDOS Y SELLADOS ANTES DE TOCARLOS (TAREA 3) ===")
w("(el encargo da 38 lados del archivo, 10 del registro de la 177, 8 triangulos")
w(" enteros, 8 con un lado fuera y 6 en que ese lado es el D. Ninguno se copia)")
TRI = os.path.join(RAIZ, "docs", "plan", "OP_L_03_TRIANGULOS.jsonl")
if os.path.exists(TRI):
    ttri = io.open(TRI, encoding="utf-8").read().replace(chr(13) + NL, NL)
    ftri = [l for l in ttri.split(NL) if l.strip()]
    w("docs/plan/OP_L_03_TRIANGULOS.jsonl -> %d filas, disco %d bytes | LF %d bytes"
      % (len(ftri), os.path.getsize(TRI), len(ttri.encode("utf-8"))))
    w("   sha256 del fichero normalizado a LF: %s"
      % hashlib.sha256(ttri.encode("utf-8")).hexdigest()[:32])
    fuentes = {}
    tiene_campo = 0
    for l in ftri:
        try:
            d = json.loads(l)
        except Exception:
            continue
        if "recomputable_entero_del_archivo" in d:
            tiene_campo += 1
        mapa = d.get("fuente_de_la_clase") or {}
        for lado in sorted(mapa):
            v = mapa[lado]
            if v:
                fuentes[v] = fuentes.get(v, 0) + 1
    w("   CIFRA filas que YA traen recomputable_entero_del_archivo: %d" % tiene_campo)
    for k in sorted(fuentes):
        w("   fuente_de_la_clase %-58s -> %d lados" % (k[:58], fuentes[k]))
else:
    w("docs/plan/OP_L_03_TRIANGULOS.jsonl -> NO EXISTE")
w("EL SELLO DE LOS VEREDICTOS, PARA PODER PROBAR DESPUES QUE NO SE MOVIO NINGUNO:")
for r in ("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", "docs/plan/OP_L_03_LECTURAS.jsonl"):
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        t = io.open(p, encoding="utf-8").read().replace(chr(13) + NL, NL)
        w("   %-42s sha256 LF %s | disco %d bytes | LF %d bytes"
          % (r, hashlib.sha256(t.encode("utf-8")).hexdigest()[:32],
             os.path.getsize(p), len(t.encode("utf-8"))))
w("")

w("=== H.10 LA GUARDA DEL SUJETO CONGELADO, CORRIDA ANTES (TAREA 4) ===")
w("(el encargo dice 15 entradas, 7 SUJETO VIVO y 8 NO DECIDIBLE. No se copian:")
w(" se corre la guarda y se cuenta su propia salida)")
c, o = correr([PY, "scripts/loop/verificar_mutaciones_viejas.py", "--sujeto-congelado"])
w("comando: verificar_mutaciones_viejas.py --sujeto-congelado -> exit %d" % c)
w("   CIFRA lineas no vacias de la salida: %d" % len([l for l in o.split(NL) if l.strip()]))
for etiqueta in ("SUJETO VIVO", "NO DECIDIBLE", "CASO DECLARADO", "CONGELADO"):
    w("   CIFRA lineas que dicen %-18s: %d"
      % (repr(etiqueta), len([l for l in o.split(NL) if etiqueta in l])))
for l in o.split(NL):
    if l.strip() and ("CIFRA" in l or "ROJO" in l or "VERDE" in l):
        w("   " + l.rstrip()[:180])
REG_SC = os.path.join(RAIZ, "docs", "plan", "SUJETO_CONGELADO_VEREDICTOS.jsonl")
w("docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl existe al abrir: %s (lo escribe esta vuelta)"
  % ("SI" if os.path.exists(REG_SC) else "NO"))
w("")

w("=== H.11 LAS CINCO DE LA TAREA 5, MEDIDAS Y NO AFIRMADAS ===")
CINCO = [
    ("1. segunda sede de la clausula 4.4", "docs/loop/reportes/REPORTE_V172.md"),
    ("2. docstring del paso 0", "scripts/loop/paso0_archivar_anterior.py"),
    ("3. dependencia del D.4 de la 174", "scripts/loop/vuelta174_esqueleto_reporte.py"),
    ("4. grano del tope de 10 minutos", "scripts/loop/verificar_mutaciones_viejas.py"),
    ("5. convencion de bytes", "docs/loop/AUDITOR.md"),
]
for etiqueta, ruta in CINCO:
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    if os.path.exists(p):
        t = io.open(p, encoding="utf-8").read().replace(chr(13) + NL, NL)
        w("%-36s %-52s disco %d bytes | LF %d bytes"
          % (etiqueta, ruta, os.path.getsize(p), len(t.encode("utf-8"))))
    else:
        w("%-36s %-52s NO EXISTE" % (etiqueta, ruta))
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

# EL DESFASE DEL CALIBRADO, EN SU SITIO Y NO AL CIERRE. El encargo de la 179 lo
# dice con dientes: con el remedio de la 177 puesto y verificado en la 178, la columna de
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
