# -*- coding: utf-8 -*-
r"""_v210_esqueleto.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 210, TALLADO EN LA
APERTURA Y ANTES DE LA PRIMERA TAREA, PARA QUE UNA VUELTA CORTADA DEJE REPORTE
PARCIAL Y NO VACIO (EJECUTOR.md 1, EL REPORTE ABRE CON LA VUELTA).

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3).

SE MANTIENE LA FORMA DE LA 208 Y LA 209: las cuatro marcas del anexo NACEN CON EL
ESQUELETO y NO SE TECLEAN, se IMPORTAN de `anexar_tarea_al_reporte.py`; y EL
TEXTO SE COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE ESCRIBE SI EL JUICIO DA
CERO FALLOS.

NO CLONA NINGUN INSTRUMENTO: importa paso0_archivar_anterior y las marcas de
anexar_tarea_al_reporte. IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5).

ESTA ES LA VUELTA DE BATERIA Y NO LLEVA NADA MAS: UNA SOLA FILA DE TAREA.
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paso0_archivar_anterior as PASO0  # noqa: E402
from anexar_tarea_al_reporte import (  # noqa: E402
    ABRE_TABLA, FIN_TABLA, ABRE_ANEXO, FIN_ANEXO, VACIO)

sys.stdout.reconfigure(encoding="utf-8")

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

TAREAS = [
    ('1', 'LA BATERIA DE MUTACIONES, ENTERA, POR SUS ONCE TRAMOS, con el lanzador '
          '`scripts/loop/vuelta183_bateria_por_tramos.py` corrido SIN CLONARLO Y SIN '
          'TOCARLO (moratoria). El reparto recomputado de la nomina; los once tramos '
          'corridos empezando por el 1, cada uno committeado con su salida sellada al '
          'terminar y esa lista de commits publicada como VARA DE FRESCURA; las tres '
          'guardas del regimen sin ablandar (doble corrida, cero bytes no cuenta, mismo '
          'calibre); y `--componer` al final. **El `--siguiente` se usa SOLO para leer el '
          'reparto y NUNCA para saber que falta**'),
]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


def vuelta_del_reporte_del_arbol(texto):
    """EL NUMERO DE VUELTA DEL REPORTE QUE SE VA A PISAR, LEIDO DE SU PROPIA
    CABECERA. PURA: recibe el texto y no lee ni escribe nada."""
    if not texto:
        return None
    primera = texto.replace(chr(13) + chr(10), chr(10)).split(chr(10), 1)[0]
    m = re.match(r"^#\s*REPORTE DE LA VUELTA\s+(\d+)\b", primera)
    return int(m.group(1)) if m else None


ruta = os.path.join(LOOP, "REPORTE.md")
texto_a_pisar = io.open(ruta, encoding="utf-8").read() if os.path.exists(ruta) else ""
n_arbol = vuelta_del_reporte_del_arbol(texto_a_pisar)
print("PASO 0.a. QUE REPORTE HAY EN EL ARBOL, LEIDO DE SU PROPIA CABECERA")
print("   docs/loop/REPORTE.md -> %d bytes" % len(texto_a_pisar.encode("utf-8")))
print("   primera linea: %s" % texto_a_pisar.split(NL, 1)[0][:88])
print("   vuelta LEIDA (no tecleada): %s" % n_arbol)
if n_arbol is None:
    print("ROJO: el REPORTE.md del arbol no lleva cabecera de reporte.")
    sys.exit(1)
print("   coincide con VUELTA menos 1 (%d): %s"
      % (VUELTA - 1, "SI" if n_arbol == VUELTA - 1 else "NO"))
print("")

destino_ant = os.path.join(LOOP, "reportes", "REPORTE_V%d.md" % n_arbol)
print("PASO 0.b. LO QUE MI APERTURA MIDIO SOBRE EL ARCHIVO DEL REPORTE ANTERIOR")
print("   mi sello dice: CIFRA docs/loop/reportes/REPORTE_V%d.md existe al entrar: NO"
      % n_arbol)
print("   existe AHORA, tras el PASO 0 de archivado: %s"
      % ("SI" if os.path.exists(destino_ant) else "NO"))
print("")

print("PASO 0.c. LA GUARDA SOBRE EL REPORTE QUE DE VERDAD SE VA A PISAR (%d)"
      % n_arbol)
ok, informe = PASO0.exigir_archivado(n_arbol)
for l in informe:
    print("   " + l)
print("")
if not ok:
    print("ROJO: el esqueleto NO escribe. El reporte anterior no esta a salvo.")
    sys.exit(1)

c, rama = git(["rev-parse", "--abbrev-ref", "HEAD"])
c2, head_ap = git(["rev-parse", "HEAD"])
if c != 0 or not rama or c2 != 0 or len(head_ap) != 40:
    print("ROJO: no se pudo leer la identidad de git.")
    sys.exit(1)
c3, asunto_ap = git(["log", "-1", "--format=%s"])
print("LA IDENTIDAD, LEIDA DE GIT Y NO TECLEADA (EJECUTOR.md 1):")
print("   rama: %s" % rama)
print("   HEAD en el momento del esqueleto: %s" % head_ap)
print("   asunto (primeros 90): %s" % asunto_ap[:90])
print("")

filas = NL.join(
    "| **TAREA %s** | %s | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |"
    % (n, t) for n, t in TAREAS)

texto = """# REPORTE DE LA VUELTA %(v)d (ejecutor). FASE III, EJECUCION. Rama `%(rama)s`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v%(v)d_esqueleto.py` **antes de la primera tarea**; la tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO EN LA 208 Y EN LA
> 209.** No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el
> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **UNA SOLA TAREA, Y ESO NO ES UN RECORTE SINO LA LETRA.** `AUDITOR.md` 6.1 dice
> que la bateria corre **en una VUELTA DE BATERIA propia que NO LLEVA NADA MAS**,
> y la cadencia de cinco pone la 210 detras de la 205. El trabajo de plan que el
> acta 209 deja adjudicado (los dos campos `estado` de `OP-L-02` y `OP-L-03`, y la
> ficha `OP-I-01`) **espera a la 211** y no se toca aqui.
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo. Todo lo que esta vuelta escribe son ficheros `_v%(v)d_*` **con
> prefijo de guion bajo, fuera del censo y fuera de la nomina**. La nomina sigue
> **CONGELADA EN 135** y no se poda. **El lanzador de la bateria NO SE CLONA NI SE
> TOCA.**
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR, Y ESO ES LA `C.5` DE LA 209
> REMEDIADA.** `docs/loop/SALIDA_V%(v)d_APERTURA.txt`,
> `docs/loop/SALIDA_V%(v)d_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes del primer tramo**, no al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

%(abre_cab)s
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta %(v)d`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
%(fin_cab)s

## 1. LA TAREA DEL ENCARGO, Y SU ESTADO

%(abre_tabla)s
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
%(filas)s
%(fin_tabla)s

## 2. LA TAREA, AL DETALLE (la seccion se ANEXA al cerrarse su tarea)

%(abre_anexo)s
%(vacio)s
%(fin_anexo)s

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

""" % {"v": VUELTA, "rama": rama, "filas": filas,
       "abre_cab": "<!-- CABECERA TALLADA -->",
       "fin_cab": "<!-- FIN CABECERA TALLADA -->",
       "abre_tabla": ABRE_TABLA, "fin_tabla": FIN_TABLA,
       "abre_anexo": ABRE_ANEXO, "fin_anexo": FIN_ANEXO, "vacio": VACIO}

fallos = 0
print("LO QUE anexar_tarea_al_reporte.py EXIGE, COMPROBADO SOBRE LO COMPUESTO:")
for marca in (ABRE_TABLA, FIN_TABLA, ABRE_ANEXO, FIN_ANEXO):
    n = texto.count(marca)
    print("   marca %-32s aparece %d vez(ces) (se exige 1)" % (marca, n))
    if n != 1:
        fallos += 1
tabla = texto[texto.index(ABRE_TABLA):texto.index(FIN_TABLA)]
for n_t, _ in TAREAS:
    ancla = "| **TAREA %s** |" % n_t
    filas_t = [l for l in tabla.split(NL) if l.startswith(ancla)]
    celdas = filas_t[0].split(" | ") if len(filas_t) == 1 else []
    abierta = len(celdas) == 4 and "ABIERTA, SIN CERRAR" in celdas[2]
    print("   fila de la TAREA %-4s aparece %d vez(ces), celdas %d (se exigen 4), 3.a celda ABIERTA: %s"
          % (n_t, len(filas_t), len(celdas), "SI" if abierta else "NO"))
    if len(filas_t) != 1 or len(celdas) != 4 or not abierta:
        fallos += 1
bloque = texto[texto.index(ABRE_ANEXO) + len(ABRE_ANEXO):texto.index(FIN_ANEXO)]
hay_vacio = VACIO in bloque
print("   el literal del vacio esta dentro del bloque del anexo: %s"
      % ("SI" if hay_vacio else "NO"))
if not hay_vacio:
    fallos += 1
print("")
print("LAS MARCAS QUE cerrar_reporte.py EXIGE EN UN REPORTE SIN CERRAR:")
for marca, esperado in (("**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**", True),
                        ("PENDIENTE DE TALLAR AL CIERRE", True),
                        ("<!-- CABECERA TALLADA -->", True),
                        ("<!-- FIN CABECERA TALLADA -->", True),
                        (NL + "## 3.", False),
                        (NL + "## 9.", False)):
    hay = marca in texto
    print("   %-56r -> %s (se esperaba %s)"
          % (marca[:54], "SI" if hay else "NO", "SI" if esperado else "NO"))
    if hay != esperado:
        fallos += 1
print("")
print("CIFRA guiones largos: %d | CIFRA guiones medios: %d"
      % (texto.count(chr(8212)), texto.count(chr(8211))))
if texto.count(chr(8212)) or texto.count(chr(8211)):
    fallos += 1
print("CIFRA comprobaciones que fallan: %d" % fallos)
if fallos:
    print("ROJO: el esqueleto NO ESCRIBE. docs/loop/REPORTE.md queda intacto.")
    sys.exit(1)
io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
print("ESCRITO docs/loop/REPORTE.md -> %d bytes, %d lineas"
      % (len(texto.encode("utf-8")), texto.count(NL)))
de_nuevo = io.open(ruta, encoding="utf-8").read()
print("RELECTURA DEL DISCO: identico a lo juzgado: %s"
      % ("SI" if de_nuevo == texto else "NO"))
print("VERDE: el esqueleto queda tallado." if de_nuevo == texto
      else "ROJO: lo escrito no es lo juzgado.")
sys.exit(0 if de_nuevo == texto else 1)
