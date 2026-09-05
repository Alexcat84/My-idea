# -*- coding: utf-8 -*-
r"""vuelta170_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA
VUELTA 170, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS CINCO TAREAS ENCARGADAS.

POR QUE NACE: EJECUTOR.md regla 1, "EL REPORTE ABRE CON LA VUELTA" (decision
del fundador, 4 sep 2026). Clon declarado de
scripts/loop/vuelta169_esqueleto_reporte.py, con las cinco filas de ESTE
encargo y con UNA DIFERENCIA QUE SE DICE EN VEZ DE CALLARSE: el hueco de la
cabecera ya no declara un rojo del lado APERTURA, porque esta vuelta SI corrio
el bloque de apertura entero (scripts/loop/vuelta170_apertura.py), asi que la
mitad izquierda de la tabla ya se puede leer y solo falta la del cierre. La
cifra de celdas ilegibles que el hueco publica la LEE el instrumento de la
salida del tallador corrida en el momento, no se teclea.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 170 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
`git rev-parse --abbrev-ref HEAD`; commit del acta de la vuelta anterior
buscando en `git log` el asunto que EMPIEZA por "ACTA DE LA VUELTA 169 DEL
AUDITOR"; HEAD de apertura leido de docs/loop/SALIDA_V170_HEAD_APERTURA.txt,
sellado antes de la primera operacion; commit de nacimiento del bloque de
apertura por `git log --diff-filter=A`. Si alguno no se puede leer o es
ambiguo, el esqueleto CAE EN ROJO y no escribe nada: no inventa un hash.

USO:
  python scripts/loop/vuelta170_esqueleto_reporte.py
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = 170
PATRON_ACTA = "ACTA DE LA VUELTA %d DEL AUDITOR" % (VUELTA - 1)

TAREAS = [
    ("1", "BLOQUEANTE. LOS REGISTROS Y LA CAIDA DE CIFRA PUBLICADA (1.a el acta 169 al `R.39`, 1.b la adjudicacion 6.2 corregida por 9.10 con su tabla de commits medida, 1.c el arnes gana el caso que ANCLA POR MEDICION el nacimiento de la decimotercera tachada)"),
    ("2", "LOS DOS INSTRUMENTOS DE PROCESO (2.a el AISLADOR DE LA CIEGA, 2.b el ARCHIVADOR DE REPORTES y el archivado hacia atras del de la 168)"),
    ("3", "LAS DEUDAS DE CORTE, por 9.21 mas 9.10 (3.a las '53 familias' de `OP-I-01` y su aritmetica de 671, 3.b la fecha de corte del '2.117' en la clausula 2 de `OP-L-01` y de `OP-L-02`)"),
    ("4", "LOS NUMEROS QUE FALTAN (4.a las lecturas dirigidas de la segunda tanda ganan numero `LD` por adicion pura, 4.b los cinco nodos puente del sales roadmap se registran MEDIDOS y NO se ejecutan)"),
    ("5", "EL TRABAJO DE VERDAD: CERRAR `OP-L-02` (5.a la FORMA de cada nomina afectada re escrita por 9.26, con su cobertura al lado y el resolutor delante; 5.b el veredicto de las tres clausulas y, solo entonces, la apertura de `OP-L-03`)"),
]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


fallos = []

c, rama = git(["rev-parse", "--abbrev-ref", "HEAD"])
if c != 0 or not rama:
    fallos.append("no se pudo leer la rama de git")

c, log = git(["log", "--format=%H%x09%s", "-400"])
actas = [l for l in log.splitlines() if l.split("\t", 1)[-1].startswith(PATRON_ACTA)]
if len(actas) != 1:
    fallos.append("commits que empiezan por %r en git log: %d (se necesita exactamente 1)"
                  % (PATRON_ACTA, len(actas)))
    acta_hash, acta_asunto = "", ""
else:
    acta_hash, acta_asunto = actas[0].split("\t", 1)

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
> `scripts/loop/vuelta%(v)d_esqueleto_reporte.py` **antes de la primera tarea**;
> cada tarea ANEXA SU FILA AL CERRARSE, no al final; y el cierre talla la
> cabecera. **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se
> hizo, y las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se
> hicieron.** Tope de cinco tareas, y el encargo trae exactamente cinco.

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
vuelta SI corrio el bloque de apertura entero**, asi que la mitad izquierda ya
se puede leer: corrido en la apertura, el tallador dice **"ROJO, %(celdas)s
celdas no se pudieron leer"** y de esas lineas de rojo, **%(n_ap)d mencionan
APERTURA**. Son todas del lado CIERRE, que en la apertura todavia no existe.
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
