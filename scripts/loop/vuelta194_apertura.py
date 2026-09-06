# -*- coding: utf-8 -*-
r"""vuelta194_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 194, CORRIDO ANTES
DE LA PRIMERA OPERACION Y CON EL DESFASE DE CALIBRADO MEDIDO AQUI DENTRO.

CLON DECLARADO de scripts/loop/vuelta193_apertura.py. Cambia el numero de vuelta,
el regimen (esta SI es vuelta de bateria), el bloque F (que pasa de los TRES
arneses que no reproducian a los DOS que se contradicen sobre la sede del turno)
y anade el bloque I, que mide el estado de la bateria AL ENTRAR.

`EJECUTOR.md` 1, LA APERTURA SE MIDE ANTES DE LA PRIMERA OPERACION: el estado
TRAS la primera operacion ya es estado intermedio y se cita como tal, con el
nombre de la operacion que lo movio. Y una columna de apertura medida al cierre
es caida que ACUMULA: fue la `C.1` que el acta 194 le puso al reporte de la 193.

EL CICLO DE GATE 0 CORRE ENTERO Y VA CABLEADO ABAJO: `scripts/run_phase1.py`
**CON `--reaplico-curaduria`** Y DESPUES `scripts/etiquetas_de_cara.py --aplicar`.
Solo con el primero quedan 72 lineas cambiadas en
`dataset/metadata/master_graph.json`, y es el segundo quien las repone. Medido
por el auditor de la 194 y traido en el encargo.

ESTA VUELTA SI ES DE BATERIA (`AUDITOR.md` 6.1): la 189 la corrio entera y por la
cadencia de cada cinco toca aqui. Por eso el bloque F mide LOS DOS ARNESES DE LA
CUARTA PUERTA QUE SE CONTRADICEN, que son la PRECONDICION de la bateria, y lo
unico que hace es COMPROBAR QUE SUS SELLADAS ESTAN INTACTAS AL ENTRAR: aqui no se
corre ninguno, porque correrlos las pisa Y porque uno de los dos BORRA el fichero
del turno del auditor en su sede de verdad.

NINGUNA CIFRA SE TECLEA. La racha de cierres sale de
`scripts/loop/vuelta192_racha_de_cierres.py` corrido y contado; el numero de la
serie sale de `scripts/loop/serie_de_registros.py`; la identidad sale de
`git rev-parse` y `git log`.

USO:
  python scripts/loop/vuelta194_apertura.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
NL = chr(10)
VUELTA = 194

# LOS DOS ARNESES DE LA CUARTA PUERTA QUE SE CONTRADICEN EN LA SEDE DE VERDAD,
# con la salida que cada uno sella. La pareja (arnes, salida) va escrita aqui
# porque es el SUJETO de la TAREA 2, y sus bytes NO se teclean: se miden abajo.
DOS_ARNESES = [
    ("scripts/loop/vuelta192_tarea4_mutacion_cuarta_puerta.py",
     "docs/loop/SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt"),
    ("scripts/loop/vuelta193_tarea4e_mutacion_sello_entre_procesos.py",
     "docs/loop/SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt"),
]

# LAS SEDES QUE NO SE PUEDEN MOVER EN ESTA VUELTA.
VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
TURNO = "docs/loop/_TURNO_DEL_AUDITOR.json"


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env,
                       shell=shell)
    out = (r.stdout.decode("utf-8", errors="replace")
           + r.stderr.decode("utf-8", errors="replace"))
    return r.returncode, out


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def sha_de(rel):
    """LAS DOS CONVENCIONES, MEDIDAS Y NO SUPUESTAS. Devuelve
    (sha_disco, sha_lf, bytes_disco, bytes_lf) o None si el fichero no esta."""
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(ruta):
        return None
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (hashlib.sha256(datos).hexdigest(), hashlib.sha256(lf).hexdigest(),
            len(datos), len(lf))


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V%d_%s_APERTURA.txt" % (VUELTA, nombre))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITO: %s (%d bytes)"
          % (os.path.basename(ruta), len(texto.encode("utf-8"))))


L = []
w = L.append
w("SELLO DE APERTURA DE LA VUELTA %d, escrito ANTES de la primera operacion."
  % VUELTA)
w("regimen: ESTA SI ES VUELTA DE BATERIA (AUDITOR.md 6.1, decision del fundador")
w("         del 5 sep 2026). La bateria corre CADA CINCO VUELTAS en una vuelta")
w("         propia QUE NO LLEVA NADA MAS; la 189 la corrio entera y por esa")
w("         cadencia toca aqui. La seccion 9 del reporte NO cierra con hueco")
w("         declarado: cierra con la bateria corrida.")
w("         TRES SUB-TAREAS y DOS BLOQUEANTES.")
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
c, est = git(["status", "--porcelain"])
sucios = [l for l in est.splitlines() if l.strip()]
w("git status --porcelain al entrar: %d linea(s)" % len(sucios))
for l in sucios[:20]:
    w("   " + l)
w("")

w("=== B.1 LA CADENA DE LA VUELTA 193 Y EL ACTA 194, LOCALIZADAS EN GIT ===")
c, logtodo = git(["log", "--format=%h%x09%s", "-40"])
filas = [l.split("\t", 1) for l in logtodo.splitlines() if "\t" in l]
for etiqueta, aguja in (("acta 194", "ACTA DEL AUDITOR, VUELTA 194"),
                        ("clases ciegas del auditor 194", "AUDITOR VUELTA 194"),
                        ("cierre de la 193", "VUELTA 193 CERRADA")):
    hits = [(h, s) for h, s in filas if s.startswith(aguja)]
    w("%-32s %d acierto(s): %s"
      % (etiqueta, len(hits), ", ".join(h for h, _s in hits) or "(ninguno)"))
w("")

w("=== C. LA SEDE DE LOS VEREDICTOS, QUE NO SE PUEDE MOVER EN ESTA VUELTA ===")
m = sha_de(VEREDICTOS)
if m is None:
    w("ROJO: no existe %s" % VEREDICTOS)
else:
    w("%s" % VEREDICTOS)
    w("   disco %d bytes | sha256 disco %s" % (m[2], m[0][:16]))
    w("   LF    %d bytes | sha256 LF    %s" % (m[3], m[1][:16]))
    w("   LAS DOS CONVENCIONES SE PUBLICAN. La LF es la que el encargo clava.")
w("")

w("=== D. dataset/ AL ENTRAR (git diff --numstat, medido y no supuesto) ===")
c, numstat = git(["diff", "--numstat", "--", "dataset/"])
lineas_ns = [l for l in numstat.splitlines() if l.strip()]
w("CIFRA ficheros de dataset/ con diff al entrar: %d" % len(lineas_ns))
for l in lineas_ns[:20]:
    w("   " + l)
if not lineas_ns:
    w("   (ninguno: dataset/ entra limpio)")
w("")

w("=== E. LA RACHA DE CIERRES, CONTADA DEL INSTRUMENTO Y NO HEREDADA ===")
w("comando: python scripts/loop/vuelta192_racha_de_cierres.py")
w("NOTA MEDIDA Y DECLARADA: este instrumento PISA su propia salida sellada")
w("   docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt, porque su sujeto es el")
w("   inventario de cierres y ese inventario CRECIO desde que la 192 lo sello.")
w("   Aqui se corre, se lee la cifra, y la sellada se RESTAURA con")
w("   git checkout -- y se REMIDE antes de darla por restaurada.")
antes = sha_de("docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt")
c, salida_racha = correr([PY, "scripts/loop/vuelta192_racha_de_cierres.py"])
mrac = re.search(r"CIFRA vueltas CONSECUTIVAS en verde hacia atras:\s*(\d+)",
                 salida_racha)
mlas = re.search(r"las vueltas de la racha:\s*(.+)", salida_racha)
racha = mrac.group(1) if mrac else None
if racha is None:
    w("ROJO: el instrumento no imprime la cifra de la racha. NO SE TECLEA una.")
else:
    w("CIFRA racha de cierres, contada del inventario ENTERO: %s" % racha)
    w("las vueltas de la racha: %s" % (mlas.group(1).strip() if mlas else "(no impresa)"))
    w("EL ENCARGO DE LA 194 DICE 9 Y ADEMAS DICE QUE LA CUENTE YO DEL")
    w("   INSTRUMENTO. Manda el instrumento: lo de arriba es lo corrido HOY.")
    w("EL TOPE DE CINCO SUB-TAREAS ESTA GANADO: el regimen temporal de")
    w("   AUDITOR.md 6.2 pedia DOS vueltas seguidas cerrando su propio reporte.")
w("nuevo corte, medido antes de restaurar:")
despues = sha_de("docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt")
if despues:
    w("   %d bytes LF | sha256 LF %s" % (despues[3], despues[1][:16]))
git(["checkout", "--", "docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt"])
rest = sha_de("docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt")
if antes and rest:
    w("SELLADA ANTES:     %d bytes LF | sha256 LF %s" % (antes[3], antes[1][:16]))
    w("SELLADA RESTAURADA:%d bytes LF | sha256 LF %s" % (rest[3], rest[1][:16]))
    w("RESTAURADA IDENTICA A LA SELLADA DE ENTRADA: %s"
      % ("SI" if antes[1] == rest[1] else "NO"))
w("")

w("=== F. LOS DOS ARNESES DE LA TAREA 2, Y LA SEDE DEL TURNO DEL AUDITOR ===")
w("AQUI NO SE CORRE NINGUNO, POR DOS MOTIVOS Y LOS DOS MEDIDOS POR EL AUDITOR")
w("en docs/loop/_auditor_v194_cuarta_puerta_rota.txt: correrlos pisa su sellada,")
w("y el de la 192 BORRA docs/loop/_TURNO_DEL_AUDITOR.json en su sede de verdad.")
for arnes, salida in DOS_ARNESES:
    med = sha_de(salida)
    c2, blob = git(["cat-file", "-s", "HEAD:" + salida])
    w("%s" % arnes)
    if med is None:
        w("   ROJO: su salida %s NO EXISTE" % salida)
        continue
    w("   %s" % salida)
    w("      disco %d bytes | LF %d bytes | sha256 LF %s"
      % (med[2], med[3], med[1][:16]))
    w("      bytes del blob de HEAD: %s"
      % (blob.strip() if c2 == 0 else "(no legible)"))
    w("      LA RUTA QUE PROMETE PRUEBA ES CIFRA: existe y no esta vacia: %s"
      % ("SI" if med[2] > 0 else "NO, CERO BYTES"))
w("LA SEDE DEL TURNO DEL AUDITOR, %s:" % TURNO)
mt = sha_de(TURNO)
w("   en el arbol de trabajo: %s"
  % ("EXISTE, %d bytes en disco" % mt[2] if mt else "NO EXISTE"))
c3, seguido = git(["ls-files", "--", TURNO])
w("   seguido por git (git ls-files): %s"
  % (seguido.strip() if seguido.strip() else "(no, no esta en el indice)"))
c4, ignorado = git(["check-ignore", "-v", "--", TURNO])
w("   cubierto por .gitignore (git check-ignore -v): %s"
  % (ignorado.strip() if c4 == 0 and ignorado.strip() else "NO, sin cubrir"))
c5, hist = git(["log", "--format=%h", "-5", "--", TURNO])
w("   commits que lo tocan en el historial: %s"
  % (", ".join(hist.split()) if hist.strip() else "(ninguno)"))
w("")

w("=== G. EL NUMERO DE LA SERIE, COMPUTADO Y NO TECLEADO ===")
w("comando: python scripts/loop/serie_de_registros.py")
c, salida_serie = correr([PY, "scripts/loop/serie_de_registros.py"])
mser = re.search(r"SIGUIENTE LIBRE:\s*(R\.\d+)", salida_serie)
mcol = re.search(r"CIFRA colisiones \(un numero escrito mas de una vez\):\s*(\d+)",
                 salida_serie)
mtot = re.search(r"CIFRA entradas en total:\s*(\d+)", salida_serie)
w("SIGUIENTE LIBRE de la serie: %s" % (mser.group(1) if mser else "(no impreso)"))
w("CIFRA entradas en total: %s" % (mtot.group(1) if mtot else "(no impresa)"))
w("CIFRA colisiones: %s" % (mcol.group(1) if mcol else "(no impresa)"))
w("EL ENCARGO DICE R.56 Y ADEMAS DICE QUE LO DIGA EL INSTRUMENTO. Manda el")
w("instrumento: lo de arriba es lo que salio corrido HOY.")
w("")

w("=== H. LA NOMINA, LEIDA Y NO TOCADA ===")
w("La opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue rechazada: la")
w("nomina no se poda, no se adelanta y no se le meten entradas nuevas.")
try:
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_mutaciones_viejas as VMV   # noqa: E402
    w("CIFRA entradas de la nomina, leidas de VMV.VIEJAS: %d" % len(VMV.VIEJAS))
    w("CIFRA casos declarados: %d" % len(VMV.CASOS_DECLARADOS))
except Exception as e:                                   # noqa: BLE001
    w("NO SE PUDO LEER LA NOMINA: %r" % (e,))
w("")

w("=== I. EL ESTADO DE LA BATERIA AL ENTRAR, Y LA TRAMPA DE LAS SELLADAS ===")
w("LA TRAMPA, TRAIDA POR EL ENCARGO Y REMEDIDA AQUI: las salidas selladas que")
w("el lanzador de la 183 encuentra NO son de esta vuelta. Cada una se fecha con")
w("git log --diff-filter=A, que es quien dice en que commit NACIO.")
selladas = sorted(n for n in os.listdir(LOOP)
                  if re.match(r"^SALIDA_V\d+_BATERIA_TRAMO_\d+\.txt$", n))
w("CIFRA ficheros SALIDA_V*_BATERIA_TRAMO_N.txt en docs/loop/: %d" % len(selladas))
por_vuelta = {}
for n in selladas:
    v = re.match(r"^SALIDA_V(\d+)_", n).group(1)
    por_vuelta.setdefault(v, []).append(n)
for v in sorted(por_vuelta, key=int):
    w("   V%s: %d fichero(s)" % (v, len(por_vuelta[v])))
w("LOS DE LA 183, QUE SON LOS QUE SU LANZADOR CUENTA, CON SU COMMIT DE ORIGEN:")
for n in por_vuelta.get("183", []):
    c6, nace = git(["log", "--diff-filter=A", "--format=%h%x09%s", "--",
                    "docs/loop/" + n])
    prim = nace.splitlines()[0] if nace.strip() else "(sin commit de alta)"
    med = sha_de("docs/loop/" + n)
    w("   %-34s %s" % (n, prim[:100]))
    w("      %s"
      % ("%d bytes en disco" % med[2] if med else "NO EXISTE"))
w("CIFRA ficheros SALIDA_V194_BATERIA_TRAMO_N.txt al entrar: %d"
  % len(por_vuelta.get("194", [])))
w("EL LANZADOR DE LA 194 AL ENTRAR: %s"
  % ("no existe todavia"
     if not os.path.exists(os.path.join(RAIZ, "scripts", "loop",
                                        "vuelta194_bateria_por_tramos.py"))
     else "YA EXISTE, y eso hay que explicarlo"))
w("")

w("FIN DEL SELLO DE APERTURA")

texto = NL.join(L) + NL
io.open(os.path.join(LOOP, "SALIDA_V%d_APERTURA.txt" % VUELTA), "w",
        encoding="utf-8", newline=NL).write(texto)
print(texto)
escribir("HEAD", head + NL)

# ------------------------------------------------- EL BLOQUE DE MEDICIONES
# NINGUNA GUARDA SE TOCA (MODO AUSTERO 4): el ciclo de Gate 0 corre ENTERO, y el
# DESFASE DEL CALIBRADO SE MIDE AQUI, EN LA APERTURA, y no al cierre.
c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
escribir("GATE0_CMD1", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
escribir("CICLO_ETIQUETAS", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/sync_assets_web.py"])
escribir("CICLO_SYNC", o + "\nEXITCODE: %d\n" % c)

c, o = correr(["git", "diff", "HEAD", "--numstat", "--", "dataset/", "web/",
               "engine/"])
escribir("CICLO_NUMSTAT", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
escribir("CONTEO", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + "\nEXITCODE: %d\n" % c)

print("BLOQUE DE APERTURA COMPLETO")
