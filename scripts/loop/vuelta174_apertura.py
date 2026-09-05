# -*- coding: utf-8 -*-
r"""vuelta174_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 174, ENTERO.

CLON DECLARADO de scripts/loop/vuelta173_apertura.py, que a su vez era clon
declarado de vuelta172_apertura.py. Cambia SOLO el numero de vuelta, el prefijo
de las salidas, la lista RUTAS_DEL_ENCARGO y el bloque H, que aqui mide lo que
ESTE encargo promete y nada mas: el reporte en HEAD (que el encargo dice que
sigue siendo el ESQUELETO de la 172 SIN CERRAR), el commit que de verdad toca
REPORTE.md por ultima vez, LAS TRES PIEZAS QUE cerrar_reporte.py NECESITA para
cerrar la 172 (tallador, cuerpo y bateria) con sus bytes, que reportes hay ya
archivados en docs/loop/reportes/ (el encargo dice que el de la 172 no lo
archivo nadie), si vuelta172_tarea1b_confirmar_r41.py existe (el encargo dice
que no, y por la regla nueva eso es CAIDA DE CIFRA del R.41), la nomina, la
serie R.N, y la fila de la TAREA 5 con la ruta que promete prueba sobre un
vacio (la clausula de la 4.4).

EL BLOQUE H NO TECLEA NINGUN HASH. La vuelta 79 cayo por publicar como commit
de apertura un hash escrito a mano; aqui el commit que toca REPORTE.md se
LOCALIZA con git log -1 -- docs/loop/REPORTE.md y se imprime lo que salga.

POR QUE SE CORRE AQUI: EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION". Este fichero NO toca REPORTE.md: sus salidas son
SALIDA_V174_*.txt y ninguna es REPORTE.md. El esqueleto de la 174, que si
sobrescribe REPORTE.md, va en la TAREA 1.b y NO aqui, y NO PUEDE IR ANTES,
porque la TAREA 1.a tiene que cerrar y archivar el REPORTE.md que hoy esta en
el arbol, que es el de la 172.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

LO QUE ESTA VUELTA SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano al abrir la vuelta, dio DOS
lineas: " M dataset/metadata/master_graph.json" (diff de CERO bytes medido con
git diff --numstat, que devolvio vacio: suciedad de indice por fin de linea) y
"?? node_modules/". Ninguna de las dos se commitea. Y git log origin/pasada-unica..HEAD
salio VACIO: no hay nada pendiente de empujar, que es lo que la regla 3 de
EJECUTOR.md manda comprobar antes de tocar nada. La prediccion se escribe AQUI,
antes de correr, y los bloques C/D/E/F de abajo la miden sin saber lo que hay
escrito.

USO:
  python scripts/loop/vuelta174_apertura.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
VUELTA = 174

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/SALIDA_V172_BATERIA.txt",
    "docs/loop/SALIDA_V172_TALLADOR_CABECERA.txt",
    "docs/loop/SALIDA_V172_T5_CERRAR_REPORTE.txt",
    "docs/loop/reportes/REPORTE_V172.md",
    "scripts/loop/_v172_cierre_texto.md",
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/anexar_tarea_al_reporte.py",
    "scripts/loop/paso0_archivar_anterior.py",
    "scripts/loop/tallar_cabecera_reporte.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/serie_de_registros.py",
    "scripts/loop/vuelta172_tarea1b_confirmar_r41.py",
    "docs/PENDIENTES.md",
    "docs/plan/CORRECCIONES_A_APLICAR.md",
]


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env, shell=shell)
    out = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    return r.returncode, out


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


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
w("")

w("=== A. HEAD DE APERTURA (git rev-parse HEAD) ===")
c, head = git(["rev-parse", "HEAD"])
head = head.strip()
w(head)
c, asunto = git(["log", "-1", "--format=%H%x09%ad%x09%s", "--date=iso"])
w(asunto.strip())
w("")

w("=== B. RAMA Y REMOTO (leidos de git, no tecleados) ===")
c, rama = git(["rev-parse", "--abbrev-ref", "HEAD"])
w("rama: " + rama.strip())
c, up = git(["rev-parse", "--abbrev-ref", "@{u}"])
w("remoto de seguimiento: " + (up.strip() if c == 0 else "(ninguno)"))
c, ahead = git(["rev-list", "--left-right", "--count", "HEAD...@{u}"])
w("adelante/atras contra el remoto (HEAD...upstream): " + (ahead.strip() if c == 0 else "(no medible)"))
w("")

w("=== C. git status --porcelain ENTERO ===")
c, st = git(["status", "--porcelain"])
for l in st.splitlines():
    w(l)
w("CIFRA lineas de status: %d" % len([l for l in st.splitlines() if l.strip()]))
w("")

w("=== D. BYTES DE CADA RUTA QUE EL ENCARGO NOMBRA ===")
for ruta in RUTAS_DEL_ENCARGO:
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    if os.path.exists(p):
        w("%s -> %d bytes" % (ruta, os.path.getsize(p)))
    else:
        w("%s -> NO EXISTE" % ruta)
w("")

w("=== E. DIFF REAL EN BYTES DE LOS MODIFICADOS (cambio contra suciedad) ===")
c, mod = git(["ls-files", "-m"])
for ruta in [l for l in mod.splitlines() if l.strip()]:
    c2, d = git(["diff", "--", ruta])
    w("%s -> diff de %d bytes" % (ruta, len(d.encode("utf-8"))))
    c3, dw = git(["diff", "--ignore-cr-at-eol", "--", ruta])
    w("   %s -> diff ignorando CR de fin de linea: %d bytes" % (ruta, len(dw.encode("utf-8"))))
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
w("bytes: %d" % len(rep.encode("utf-8")))
MARCAS = ["SIN ESCRIBIR TODAVIA", "PENDIENTE DE TALLAR AL CIERRE"]
MARCAS = MARCAS + [NL + "## %d." % k for k in range(3, 10)]
for marca in MARCAS:
    w("   contiene %-34s -> %s" % (repr(marca), "SI" if marca in rep else "NO"))
w("")

w("=== H.1 EL REPORTE DEL ARBOL, QUE ES EL SUJETO DE LA TAREA 1.a ===")
RUTA_REP = os.path.join(LOOP, "REPORTE.md")
arbol = io.open(RUTA_REP, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("primera linea: %s" % arbol.split(NL, 1)[0].strip())
w("bytes: %d | saltos de linea: %d" % (len(arbol.encode("utf-8")), arbol.count(NL)))
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
    w("   " + l)
c, ult = git(["log", "-1", "--format=%h", "--", "docs/loop/REPORTE.md"])
w("ultimo commit que TOCA docs/loop/REPORTE.md: %s" % ult.strip())
c, asu = git(["log", "-1", "--format=%s", ult.strip()])
w("   su asunto: %s" % asu.strip()[:110])
w("")

w("=== H.3 LAS TRES PIEZAS QUE cerrar_reporte.py PIDE PARA CERRAR LA 172 ===")
for r in ["docs/loop/SALIDA_V172_TALLADOR_CABECERA.txt",
          "scripts/loop/_v172_cierre_texto.md",
          "docs/loop/SALIDA_V172_BATERIA.txt",
          "docs/loop/SALIDA_V172_AUDITOR_BATERIA.txt"]:
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        t = io.open(p, encoding="utf-8", errors="replace").read().replace(chr(13) + NL, NL)
        filas = len([l for l in t.split(NL) if l.strip().startswith("|")])
        nov = len([l for l in t.split(NL) if l.strip()])
        w("%s -> %d bytes, %d lineas no vacias, %d filas de tabla"
          % (r, os.path.getsize(p), nov, filas))
    else:
        w("%s -> NO EXISTE" % r)
w("")

w("=== H.4 QUE REPORTES ESTAN YA ARCHIVADOS EN docs/loop/reportes/ ===")
DIRA = os.path.join(LOOP, "reportes")
arch = sorted(os.listdir(DIRA)) if os.path.isdir(DIRA) else []
for n in arch:
    w("   %s -> %d bytes" % (n, os.path.getsize(os.path.join(DIRA, n))))
w("CIFRA reportes archivados: %d" % len(arch))
w("REPORTE_V172.md archivado: %s" % ("SI" if "REPORTE_V172.md" in arch else "NO"))
w("")

w("=== H.5 LA NOMINA Y LOS QUE FALTAN, POR SU PROPIA FUNCION PURA ===")
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import verificar_mutaciones_viejas as VMV
ultima, faltan = VMV.arneses_que_faltan()
w("entradas de la nomina VIEJAS: %d" % len(VMV.VIEJAS))
w("ultima vuelta representada en la nomina: %s" % ultima)
w("arneses_que_faltan(): %d" % len(faltan))
for n in faltan:
    w("   " + n)
w("nomina_invisible_al_censo(): %d" % len(VMV.nomina_invisible_al_censo()))
w("")

w("=== H.6 LA SERIE R.N, RECOMPUTADA (no tecleada) ===")
import serie_de_registros as SDR
ent = SDR.entradas()
w("entradas de la serie: %d" % len(ent))
w("mayor: R.%d" % max(n for n, _r, _l, _t in ent))
w("siguiente libre: R.%d" % SDR.siguiente_libre(ent))
w("las cinco ultimas, con su sede y su linea:")
for n, r, l, t in ent[-5:]:
    w("   R.%d -> %s:%d" % (n, r, l))
w("")

w("=== H.7 LAS DOS RUTAS QUE PROMETEN PRUEBA SOBRE UN VACIO ===")
w("(regla nueva del 5 sep 2026: LA RUTA QUE PROMETE PRUEBA ES CIFRA)")
for quien, r in [("la fila de la TAREA 5 del reporte de la 172 (clausula 4.4)",
                  "docs/loop/SALIDA_V172_T5_CERRAR_REPORTE.txt"),
                 ("el recuadro de apertura del R.41 (clausula 4.5)",
                  "scripts/loop/vuelta172_tarea1b_confirmar_r41.py")]:
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if not os.path.exists(p):
        est = "NO EXISTE"
    elif os.path.getsize(p) == 0:
        est = "EXISTE PERO 0 BYTES"
    else:
        est = "%d bytes" % os.path.getsize(p)
    w("%s%s   -> %s -> %s" % (quien, NL, r, est))
w("")

w("=== H.8 LA PROMESA DEL R.41, LEIDA DE SU SEDE Y NO DE MEMORIA ===")
for ruta in ["docs/PENDIENTES.md", "docs/plan/CORRECCIONES_A_APLICAR.md"]:
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    txt = io.open(p, encoding="utf-8", errors="replace").read()
    for i, l in enumerate(txt.split("\n"), 1):
        if "vuelta172_tarea1b_confirmar_r41" in l or l.startswith("## R.41."):
            w("%s:%d: %s" % (ruta, i, l.strip()[:150]))
w("")

w("=== H.9 LA FILA DE LA TAREA 5 DEL REPORTE DEL ARBOL, ENTERA ===")
for i, l in enumerate(arbol.split(NL), 1):
    if l.startswith("| **TAREA 5**"):
        w("REPORTE.md:%d: %s" % (i, l.strip()))
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

c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + "\nEXITCODE: %d\n" % c)

c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d\n" % c)

c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + "\nEXITCODE: %d\n" % c)

print("BLOQUE DE APERTURA COMPLETO")
