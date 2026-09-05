# -*- coding: utf-8 -*-
r"""vuelta172_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA
VUELTA 172, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS CINCO TAREAS ENCARGADAS.

CLON DECLARADO de scripts/loop/vuelta171_esqueleto_reporte.py, construido desde
el original por scripts/loop/_v172_construir_esqueleto.py. Cambia el numero de
vuelta, las cinco filas de tarea y LA BUSQUEDA DEL ACTA, que pasa de una sola
forma del titulo a las DOS que tallar_cabecera_reporte.py ya tenia escritas: el
asunto del commit del acta 171 empieza por "ACTA DEL AUDITOR, VUELTA 171", que
es la forma nacida en la vuelta 106, y con una sola forma esto daria cero
aciertos. NO SE ESTRENA NINGUN PATRON y la exigencia de UN SOLO acierto queda.

POR QUE NACE: EJECUTOR.md regla 1, "EL REPORTE ABRE CON LA VUELTA" (decision
del fundador, 4 sep 2026). Clon declarado de
scripts/loop/vuelta170_esqueleto_reporte.py, con las cinco filas de ESTE
encargo y con UNA DIFERENCIA QUE ES EL TRABAJO DE LA TAREA 5.a:

EL PASO 0, EL ARCHIVADOR ENCHUFADO (adjudicacion 6.6 del acta 170). El esqueleto
de la 170 SOBREESCRIBIO docs/loop/REPORTE.md sin preguntar, y esa es justo la
razon por la que el encargo de esta vuelta tuvo que invertir su orden de
apertura. A partir de aqui el esqueleto NO ESCRIBE si el reporte anterior no
esta archivado Y si lo que va a pisar no esta guardado byte a byte en el
archivo. La guarda vive en scripts/loop/paso0_archivar_anterior.py, con nombre
estable y sin numero de vuelta para que no se pierda en el siguiente clon, y su
caso positivo por mutacion en
scripts/loop/vuelta171_tarea5a_mutacion_enchufe.py.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 171 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
`git rev-parse --abbrev-ref HEAD`; commit del acta de la vuelta anterior
buscando en `git log` el asunto que EMPIEZA por "ACTA DE LA VUELTA 170 DEL
AUDITOR"; HEAD de apertura leido de docs/loop/SALIDA_V171_HEAD_APERTURA.txt,
sellado antes de la primera operacion; commit de nacimiento del bloque de
apertura por `git log --diff-filter=A`. Si alguno no se puede leer o es
ambiguo, el esqueleto CAE EN ROJO y no escribe nada: no inventa un hash.

USO:
  python scripts/loop/vuelta171_esqueleto_reporte.py
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paso0_archivar_anterior as PASO0   # noqa: E402
import tallar_cabecera_reporte as TALLADOR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = 172
# LAS DOS FORMAS DEL TITULO, COPIADAS DE tallar_cabecera_reporte.py:920-921.
PATRONES_ACTA = [
    re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR" % (VUELTA - 1)),
    re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA %d" % (VUELTA - 1)),
]
PATRON_ACTA = "ACTA DE LA VUELTA %d DEL AUDITOR o ACTA DEL AUDITOR, VUELTA %d" % (
    VUELTA - 1, VUELTA - 1)

TAREAS = [
    ("1", "BLOQUEANTE Y VA PRIMERA. EL CIERRE QUE FALTA Y LOS REGISTROS (1.a el reporte de la 171 CERRADO con la cabecera tallada pegada, sus cuatro discutibles y su caida sin suavizar, y la seccion 9 diciendo que la bateria NO corrio; 1.b el acta 171 y sus adjudicaciones 6.1 a 6.12 al `R.41` con su arnes de mutacion del registro; 1.c el archivador para la 171 y este esqueleto)"),
    ("2", "BLOQUEANTE PARA LA 3. SE DESENVENENA EL CONTADOR Y SE CORRIGE EL `R.40` (adjudicaciones 6.1 y 6.3): 2.a `docs/loop/reportes/REPORTE_V<N>.md` entra en los narrativos del bucle POR PATRON, con su caso positivo por mutacion; 2.b la afirmacion falsa del `R.40` corregida por el carril del `9.10` con el reparto recomputado; 2.c el contador otra vez, con la atribucion fichero a fichero y linea a linea"),
    ("3", "LA NUMERACION `LD`, QUE AHORA SI SE ESCRIBE (adjudicacion 6.2): las 16 filas de la segunda tanda de `docs/plan/LECTURAS_DIRIGIDAS.md` ganan `LD-139` a `LD-154` POR ADICION PURA, con los numeros COMPUTADOS y con dos guardas que tienen que caer por mutacion; y despues la fila de `docs/plan/00_INDICE.md` recibe su cifra de hoy por `9.21` (adjudicacion 6.10)"),
    ("4", "LOS TRES ARNESES Y LA BATERIA (adjudicaciones 6.4 y 6.5), Y EL ORDEN ES OBLIGATORIO: 4.a el caso `F` de `vuelta171_tarea5a_mutacion_enchufe.py` refundado sobre SUJETO CONGELADO; 4.b los tres arneses de la 171 dentro de la nomina de `verificar_mutaciones_viejas.py`; 4.c la bateria corrida ENTERA Y SOLA al cierre, con su salida en la seccion 9"),
    ("5", "EL CIERRE DEL REPORTE DEJA DE SER UN PASO A MANO (adjudicacion 6.6): nace `scripts/loop/cerrar_reporte.py`, de nombre estable y sin numero de vuelta, que pega la cabecera, anexa el cuerpo, escribe el veredicto y CAE EN ROJO si al terminar falta cualquiera de las cuatro piezas. Con su caso positivo por mutacion, y esta vuelta se cierra con el"),
]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


sys.stdout.reconfigure(encoding="utf-8")

# ------------------------------------------------------------------- PASO 0
ok, informe = PASO0.exigir_archivado(VUELTA - 1)
for l in informe:
    print(l)
print("")
if not ok:
    print("ROJO: el esqueleto NO escribe. El reporte anterior no esta a salvo.")
    sys.exit(1)

fallos = []

c, rama = git(["rev-parse", "--abbrev-ref", "HEAD"])
if c != 0 or not rama:
    fallos.append("no se pudo leer la rama de git")

c, log = git(["log", "--format=%H%x09%s", "-400"])
filas_log = [l.split("\t", 1) for l in log.splitlines() if "\t" in l]
# LA BUSQUEDA DEL ACTA NO SE COPIA AQUI: SE IMPORTA. Una sola fuente. El commit
# del acta 170 lleva ruido DELANTE de su titulo (caida 4 de la vuelta 170,
# declarada en 0caca89f), asi que el patron anclado da cero y hace falta la
# pasada suelta. La regla de las dos pasadas, con su motivo medido y con la
# exigencia de UN SOLO acierto intacta, vive en
# scripts/loop/tallar_cabecera_reporte.py:buscar_acta, y su caso positivo por
# mutacion en scripts/loop/vuelta171_mutacion_busqueda_acta.py.
# LAS DOS FORMAS DEL TITULO DEL ACTA, Y NO UNA (vuelta 172). El clon de la 171
# buscaba una sola cadena. El asunto del commit del acta 171 es "ACTA DEL
# AUDITOR, VUELTA 171: ...", que es LA OTRA forma, la nacida en la vuelta 106,
# asi que con una sola forma esto daria CERO aciertos y el esqueleto no
# abriria. Las dos formas ya estan escritas en
# tallar_cabecera_reporte.py:commit_apertura_desde_git y aqui se usan esas,
# sin estrenar ninguna. La exigencia de EXACTAMENTE UN acierto no se toca.
actas, anclado = TALLADOR.buscar_acta(filas_log, PATRONES_ACTA)
if not anclado and actas:
    print("DECLARADO: el commit del acta %d NO empieza por su titulo; se localiza"
          % (VUELTA - 1))
    print("   por busqueda NO ANCLADA, con exactamente 1 acierto. Su asunto real,")
    print("   con el ruido y todo, es el que se publica en la identidad.")
if len(actas) != 1:
    fallos.append("commits con %r en git log (anclado y suelto): %d (se necesita exactamente 1)"
                  % (PATRON_ACTA, len(actas)))
    acta_hash, acta_asunto = "", ""
else:
    acta_hash, acta_asunto = actas[0]

ruta_head = os.path.join(LOOP, "SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA)
if not os.path.exists(ruta_head):
    fallos.append("no existe el sello %s" % os.path.basename(ruta_head))
    head_ap = ""
else:
    head_ap = io.open(ruta_head, encoding="utf-8").read().strip()
    if len(head_ap) != 40:
        fallos.append("el sello %s no trae un hash de 40 caracteres" % os.path.basename(ruta_head))

c, nac = git(["log", "--diff-filter=A", "--format=%H", "--",
              "docs/loop/SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA])
nacs = [l for l in nac.splitlines() if l.strip()]
if len(nacs) != 1:
    fallos.append("commits que ANADEN el sello de apertura: %d (se necesita exactamente 1)" % len(nacs))
    nac_hash = ""
else:
    nac_hash = nacs[0]

env = dict(os.environ)
env["PYTHONIOENCODING"] = "utf-8"
r = subprocess.run([sys.executable, "scripts/loop/tallar_cabecera_reporte.py",
                    "--fase04", "--vuelta", str(VUELTA)],
                   cwd=RAIZ, capture_output=True, env=env)
sal_tallador = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
m = re.search(r"ROJO,\s+(\d+)\s+celdas no se pudieron leer", sal_tallador)
if not m:
    fallos.append("el tallador no imprime la cifra de celdas ilegibles; no se teclea una")
    celdas = ""
else:
    celdas = m.group(1)
lado_apertura_roto = [l for l in sal_tallador.splitlines()
                      if "APERTURA" in l and l.strip().startswith(("no ", "sin "))]

if fallos:
    print("ROJO, el esqueleto NO se escribe:")
    for f in fallos:
        print("   " + f)
    sys.exit(1)

filas = "\n".join(
    "| **TAREA %s** | %s | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |"
    % (n, t) for n, t in TAREAS)

texto = """# REPORTE DE LA VUELTA %(v)d (ejecutor). FASE III, EJECUCION. Rama `%(rama)s`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta%(v)d_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre talla la cabecera. **Si esta vuelta se corta,
> lo que quede aqui es lo que de verdad se hizo, y las filas que sigan diciendo
> ABIERTA, SIN CERRAR son las que no se hicieron.** Tope de cinco tareas, y el
> encargo trae exactamente cinco.
>
> **Y EL ESQUELETO YA NO PUEDE PISAR UN REPORTE SIN ARCHIVAR** (guarda nacida en
> la TAREA 5.a de la vuelta 171): su paso 0 corre el archivador y **se niega a
> escribir** si el reporte anterior no esta guardado byte a byte. **Y esa guarda
> YA MORDIO en la vuelta siguiente a la que nacio**: corrida en modo solo
> comprobacion al abrir esta vuelta, dijo ROJO por su clausula (d), porque el
> `REPORTE.md` del arbol era el de la 171 sin cerrar. Esta corrida lo paso en
> verde contra `docs/loop/reportes/REPORTE_V%(ant)d.md` **solo despues de que la
> TAREA 1.a cerrara ese reporte**.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta%(v)d_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `%(rama)s`
- commit del acta de la vuelta %(ant)d: `%(acta8)s`, asunto real leido de git log:
  %(asunto)s
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V%(v)d_HEAD_APERTURA.txt`: `%(head8)s`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `%(nac8)s`
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta %(v)d`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
%(celdas)s celdas no se pudieron leer"** y de esas lineas de rojo, **%(n_ap)d
mencionan APERTURA**. Son todas del lado CIERRE, que al abrir todavia no existe.
Este hueco se rellena con la tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
%(filas)s
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
""" % dict(v=VUELTA, ant=VUELTA - 1, rama=rama, acta8=acta_hash[:8],
           asunto=repr(acta_asunto), head8=head_ap[:8], nac8=nac_hash[:8],
           celdas=celdas, n_ap=len(lado_apertura_roto), filas=filas)

ruta = os.path.join(LOOP, "REPORTE.md")
io.open(ruta, "w", encoding="utf-8", newline="\n").write(texto)
print("ESQUELETO ESCRITO: docs/loop/REPORTE.md (%d bytes, %d lineas)"
      % (len(texto.encode("utf-8")), texto.count("\n")))
print("   rama leida de git: %s" % rama)
print("   acta %d leida de git log: %s  %s" % (VUELTA - 1, acta_hash[:8], acta_asunto[:70]))
print("   HEAD de apertura leido del sello: %s" % head_ap[:8])
print("   nacimiento del bloque de apertura, --diff-filter=A: %s" % nac_hash[:8])
print("   celdas ilegibles que el tallador imprime HOY: %s" % celdas)
print("   de ellas, del lado APERTURA: %d" % len(lado_apertura_roto))
print("   filas de tarea abiertas: %d" % len(TAREAS))
