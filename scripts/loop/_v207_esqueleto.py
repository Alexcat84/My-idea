# -*- coding: utf-8 -*-
r"""_v207_esqueleto.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 207, TALLADO EN LA
APERTURA Y EN SU PROPIO COMMIT, PARA QUE UNA VUELTA CORTADA DEJE REPORTE PARCIAL
Y NO VACIO (EJECUTOR.md 1, EL REPORTE ABRE CON LA VUELTA).

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (encargo 207 punto 2.e, moratoria de AUDITOR.md 6.3). NO CLONA NINGUN
INSTRUMENTO: importa `paso0_archivar_anterior`. IMPORTAR NO ES CLONAR (acta 206,
adjudicacion 6.5).

LA GUARDA QUE PUEDE CAER Y QUE ES EL MOTIVO DE ESTE FICHERO: el PASO 0 exige que
el reporte que se va a PISAR este archivado byte a byte. Mi apertura, sellada en
docs/loop/SALIDA_V207_APERTURA.txt ANTES de la primera operacion, midio que
docs/loop/reportes/REPORTE_V206.md NO EXISTIA, contra un encargo que lo daba por
archivado. El PASO 0 lo archiva aqui y lo dice.
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paso0_archivar_anterior as PASO0  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")

NL = chr(10)
VUELTA = 207
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")

TAREAS = [
    ('1', 'LOS REGISTROS DE LA VUELTA 206. Leer el acta 206 entera y REMEDIR sus '
          'cifras de crecimiento; escribir `R.71` en `docs/PENDIENTES.md` **por '
          'adicion pura y en su sede**, con el numero COMPUTADO por '
          '`scripts/loop/serie_de_registros.py` y las dos puntas publicadas; '
          'registrar **las seis adjudicaciones** del acta 206 por su numero; y '
          'corregir **las dos caidas de reporte** (`E.1` y `E.2`) en el reporte '
          'ARCHIVADO de la 206, por CORRECCION DECLARADA y con el texto viejo '
          'entero encima'),
    ('2', 'EL PLAN. LA MESA `OP-L-01`, LEIDA CONTRA LOS TRES DOCUMENTOS QUE SU '
          'PROPIA FICHA NOMBRA. La vara se escribe ANTES de abrir ningun '
          'documento; cada punto lleva su fila con CUBRE, A MEDIAS o NO CUBRE y '
          '**su cita con fichero y linea**; la cobertura se publica MEDIDA y no '
          'narrada. **NO SE CIERRA LA FICHA Y NO SE TOCA EL CAMPO `estado`**'),
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
print("   coincide con VUELTA - 1 (%d): %s"
      % (VUELTA - 1, "SI" if n_arbol == VUELTA - 1 else "NO"))
print("")

destino_206 = os.path.join(LOOP, "reportes", "REPORTE_V%d.md" % n_arbol)
print("PASO 0.b. LO QUE MI APERTURA MIDIO, Y CONTRA LO QUE EL ENCARGO DECIA")
print("   el encargo 207 dice que el reporte de la 206 esta CERRADO Y ARCHIVADO")
print("   docs/loop/reportes/REPORTE_V%d.md existia ANTES de esta corrida: %s"
      % (n_arbol, "SI" if os.path.exists(destino_206) else "NO"))
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
print("   HEAD de apertura: %s" % head_ap)
print("   asunto (primeros 90): %s" % asunto_ap[:90])
print("")

filas = NL.join(
    "| **TAREA %s** | %s | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |"
    % (n, t) for n, t in TAREAS)

texto = """# REPORTE DE LA VUELTA %(v)d (ejecutor). FASE III, EJECUCION. Rama `%(rama)s`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v%(v)d_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE; y el cierre lo talla entero
> `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se corta, las filas que sigan
> diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VEZ EL ESQUELETO SI VA PRIMERO, Y LA 206 NO PUDO.** La `C.2` del reporte
> de la 206 y su `P.3` decian que `docs/loop/REPORTE.md` era el sujeto que su
> TAREA 1 tenia que cerrar. Aqui no lo es, asi que el esqueleto se talla antes de
> tocar nada, que es lo que la casa manda.
>
> **PERO EL REPORTE DE LA 206 NO ESTABA ARCHIVADO, CONTRA LO QUE EL ENCARGO DICE,
> Y ESO SE DECLARA EN VEZ DE COPIARSE** (`EJECUTOR.md` 2, EL INSTRUMENTO MANDA).
> Mi sello de apertura, `docs/loop/SALIDA_V%(v)d_APERTURA.txt`, escrito **antes de
> la primera operacion**, publica `CIFRA docs/loop/reportes/REPORTE_V206.md existe
> al entrar: NO`. El encargo dice *"el reporte de la 206 ya esta cerrado y
> archivado"*. **Cerrado si, archivado no.** Lo archiva el PASO 0 de este mismo
> esqueleto, que es su sitio, y la salida va sellada.
>
> **DOS SUB-TAREAS Y NINGUNA MAS** (`AUDITOR.md` 6.2, adjudicacion `6.6` del acta
> 206: la racha de cierres esta en UNA y el tope de cinco todavia no vuelve).
>
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA**
> (`AUDITOR.md` 6.1, adjudicacion `6.7` del acta 206). La ultima fue la **205** y
> la siguiente es la **210**. La **seccion 9 cierra igual**, con el **HUECO
> DECLARADO Y MEDIDO** y sus **tres piezas juntas**: el nombre del fichero, los
> bytes medidos **distinguiendo el cero de ausencia del cero de fichero vacio**, y
> la atribucion.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Todo lo que esta
> vuelta escribe son ficheros `_v%(v)d_*` **con prefijo de guion bajo, fuera del
> censo y fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda.
> **EL TRABAJO ES EL PLAN**, y por eso la TAREA 2 es una mesa del plan.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta %(v)d`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
%(filas)s

## 2. LO QUE CADA TAREA DEJO SELLADO (cada tarea ANEXA su fila al cerrarse)

| tarea | salida sellada | bytes disco | bytes LF | exitcode |
|---|---|---|---|---|
| (vacio al abrir) | (cada tarea anexa la suya al cerrarse) | | | |

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

""" % {"v": VUELTA, "rama": rama, "filas": filas}

io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
print("ESCRITO docs/loop/REPORTE.md -> %d bytes, %d lineas"
      % (len(texto.encode("utf-8")), texto.count(NL)))
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
