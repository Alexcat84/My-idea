# -*- coding: utf-8 -*-
r"""vuelta168_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA
VUELTA, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS CINCO TAREAS ENCARGADAS.

POR QUE NACE (decision del fundador, 4 sep 2026, punto 3, escrita ya en
EJECUTOR.md regla 1 bajo el rotulo "EL REPORTE ABRE CON LA VUELTA"): las
vueltas 166 y 167 terminaron SIN REPORTE, dos seguidas, y docs/loop/REPORTE.md
se quedo en el de la 165. Un reporte que se escribe al final es lo primero que
se cae cuando la vuelta se corta, y cuando se cae no queda NADA, ni siquiera
las tareas que si salieron. La regla nueva: el ESQUELETO se talla en la
apertura, CADA TAREA ANEXA SU FILA AL CERRARSE, y el cierre lo talla entero.

LO QUE ESTE FICHERO NO HACE, Y SE DICE PARA QUE NO SE CONFUNDA CON EL TALLADOR
DE LA CABECERA: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 168 AL CIERRE, y no
puede tallarse antes porque su columna derecha se lee de las salidas
SALIDA_V168_*_CIERRE.txt, que en la apertura no existen: corrido hoy, el
tallador dice "ROJO, 19 celdas no se pudieron leer y NO se talla nada". Asi que
el esqueleto deja el hueco de la cabecera MARCADO Y DECLARADO entre sus dos
comentarios, y el cierre lo rellena con la tabla tallada.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
`git rev-parse --abbrev-ref HEAD`; commit del acta de la vuelta anterior
buscando en `git log` el asunto que EMPIEZA por "ACTA DE LA VUELTA 167 DEL
AUDITOR"; HEAD de apertura leido de docs/loop/SALIDA_V168_HEAD_APERTURA.txt,
que nacio sellado antes de la primera operacion. Si alguno no se puede leer, el
esqueleto CAE EN ROJO y no escribe nada: no inventa un hash.

USO:
  python scripts/loop/vuelta168_esqueleto_reporte.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = 168
PATRON_ACTA = "ACTA DE LA VUELTA %d DEL AUDITOR" % (VUELTA - 1)

TAREAS = [
    ("1", "LOS REGISTROS: el acta 167 en `R.37`, y la nota adosada al `R.36`"),
    ("2", "EL REPORTE QUE CUBRE LAS VUELTAS 166 Y 167"),
    ("3", "EL MANTENIMIENTO DE LA BATERIA (3.a nomina, 3.b re anclaje, 3.c corrida entera)"),
    ("4", "`OP-V-01` POR LA DECISION 5, VERIFICADA CONTRA GIT"),
    ("5", "ABRIR LAS SEIS POR LA VARA DEL INSTRUMENTO (5.a, 5.b valvula, 5.c depende_de)"),
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

if fallos:
    print("ROJO, el esqueleto NO se escribe:")
    for f in fallos:
        print("   " + f)
    sys.exit(1)

filas = "\n".join(
    "| **TAREA %s** | %s | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |"
    % (n, t) for n, t in TAREAS)

texto = """# REPORTE DE LA VUELTA %(v)d (ejecutor). FASE III, EJECUCION. Rama `%(rama)s`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION.** Es la
> regla nueva de `EJECUTOR.md` 1 ("EL REPORTE ABRE CON LA VUELTA", decision del
> fundador del 4 sep 2026) estrenandose sobre si misma. El esqueleto lo tallo
> `scripts/loop/vuelta%(v)d_esqueleto_reporte.py` antes de la primera tarea;
> cada tarea ANEXA SU FILA AL CERRARSE, no al final; y el cierre talla la
> cabecera. **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se
> hizo, y las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se
> hicieron.** Tope de cinco tareas por vuelta, y el encargo trae exactamente
> cinco.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar. Un veredicto escrito en la apertura seria justo la especie
que esta regla existe para matar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta%(v)d_esqueleto_reporte.py`, que la busca con
`git rev-parse --abbrev-ref HEAD` y con `git log` y CAE EN ROJO si no la
encuentra o si es ambigua:

- rama: `%(rama)s`
- commit del acta de la vuelta %(ant)d: `%(acta8)s`, asunto real leido de git log:
  '%(asunto)s'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V%(v)d_HEAD_APERTURA.txt`: `%(head8)s`
- commit de nacimiento del bloque de apertura y commit de cierre: se tallan al
  cierre. **Un reporte no puede nombrar el commit que lo lleva**, porque ese
  commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla de
comprobaciones sale de
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta %(v)d`, cuya columna
derecha se lee de las salidas `SALIDA_V%(v)d_*_CIERRE.txt`. En la apertura esas
salidas no existen, y el tallador, corrido hoy, lo dice sin adorno: **"ROJO, 19
celdas no se pudieron leer y NO se talla nada"**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
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
           asunto=acta_asunto, head8=head_ap[:8], filas=filas)

ruta = os.path.join(LOOP, "REPORTE.md")
io.open(ruta, "w", encoding="utf-8", newline="\n").write(texto)
print("ESQUELETO ESCRITO: docs/loop/REPORTE.md (%d bytes, %d lineas)"
      % (len(texto.encode("utf-8")), texto.count("\n")))
print("   rama leida de git: %s" % rama)
print("   acta %d leida de git log: %s  %s" % (VUELTA - 1, acta_hash[:8], acta_asunto[:70]))
print("   HEAD de apertura leido del sello: %s" % head_ap[:8])
print("   filas de tarea abiertas: %d" % len(TAREAS))
