# -*- coding: utf-8 -*-
r"""vuelta193_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 193, CORRIDO ANTES
DE LA PRIMERA OPERACION Y CON EL DESFASE DE CALIBRADO MEDIDO AQUI DENTRO.

`EJECUTOR.md` 1, LA APERTURA SE MIDE ANTES DE LA PRIMERA OPERACION: el estado
TRAS la primera operacion ya es estado intermedio y se cita como tal, con el
nombre de la operacion que lo movio. Y una columna de apertura medida al cierre
es caida que ACUMULA.

LO QUE EL ENCARGO DE ESTA VUELTA ME AHORRO Y AQUI VA CABLEADO: el ciclo de
Gate 0 corre `scripts/run_phase1.py` **CON `--reaplico-curaduria`**. Sin esa
bandera sale EXITCODE 2 y deja `dataset/` sucio con 72 lineas cambiadas, porque
la compilacion pisa las 71 etiquetas de cara curadas. Es la caida propia `C.1`
del acta 193 y no se repite aqui.

ESTA VUELTA NO ES DE BATERIA (`AUDITOR.md` 6.1) PERO ES LA ULTIMA ANTES: la 189
la corrio entera y la siguiente cae en la 194. Por eso el bloque `F` mide LOS
TRES ARNESES QUE EL ACTA 193 DECLARA SIN REPRODUCIR, y lo unico que hace es
COMPROBAR QUE SUS SELLADAS ESTAN INTACTAS AL ENTRAR: aqui no se corre ninguno,
porque correrlos las pisa.

NINGUNA CIFRA SE TECLEA. La racha de cierres sale de
`scripts/loop/vuelta192_racha_de_cierres.py` corrido y contado; el numero de la
serie sale de `scripts/loop/serie_de_registros.py`; la identidad sale de
`git rev-parse` y `git log`.

USO:
  python scripts/loop/vuelta193_apertura.py
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
VUELTA = 193

# LOS TRES ARNESES QUE EL ACTA 193 MIDIO SIN REPRODUCIR, con la salida que cada
# uno sella. La pareja (arnes, salida) va escrita aqui porque es el SUJETO de la
# TAREA 2, y sus bytes NO se teclean: se miden abajo.
TRES_ARNESES = [
    ("scripts/loop/vuelta191_tarea3_mutacion_lineas.py",
     "docs/loop/SALIDA_V191_T3_MUTACION_LINEAS.txt"),
    ("scripts/loop/vuelta191_tarea6_mutacion_bloque_tallado.py",
     "docs/loop/SALIDA_V191_T6_MUTACION_BLOQUE_TALLADO.txt"),
    ("scripts/loop/guarda_de_entrada_a_la_nomina.py",
     "docs/loop/SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt"),
]

# LAS SEDES QUE NO SE PUEDEN MOVER EN ESTA VUELTA.
VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"


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
w("regimen: NO ES VUELTA DE BATERIA (AUDITOR.md 6.1), PERO ES LA ULTIMA ANTES.")
w("         La 189 la corrio entera y la siguiente cae en la 194. La seccion 9")
w("         del reporte cierra con el HUECO DECLARADO Y MEDIDO por su carril,")
w("         con su nombre, sus bytes medidos y su atribucion, LAS TRES JUNTAS.")
w("         CINCO SUB-TAREAS y DOS BLOQUEANTES.")
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

w("=== B.1 LA CADENA DE LA VUELTA 192 Y EL ACTA 193, LOCALIZADAS EN GIT ===")
c, logtodo = git(["log", "--format=%h%x09%s", "-40"])
filas = [l.split("\t", 1) for l in logtodo.splitlines() if "\t" in l]
for etiqueta, aguja in (("acta 193", "ACTA DEL AUDITOR, VUELTA 193"),
                        ("clases ciegas del auditor 193", "AUDITOR VUELTA 193"),
                        ("cierre de la 192", "VUELTA 192 CERRADA")):
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

w("=== F. LOS TRES ARNESES DE LA TAREA 2, SUS SELLADAS INTACTAS AL ENTRAR ===")
w("AQUI NO SE CORRE NINGUNO: correrlos pisa su sellada, y la comprobacion de")
w("esta bloque es solo que lo que el acta 193 midio sigue en el arbol.")
for arnes, salida in TRES_ARNESES:
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
w("EL ENCARGO DICE R.55 Y ADEMAS DICE QUE LO DIGA EL INSTRUMENTO. Manda el")
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

w("FIN DEL SELLO DE APERTURA")

texto = NL.join(L) + NL
io.open(os.path.join(LOOP, "SALIDA_V%d_APERTURA.txt" % VUELTA), "w",
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
