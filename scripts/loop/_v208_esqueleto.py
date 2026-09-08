# -*- coding: utf-8 -*-
r"""_v208_esqueleto.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 208, TALLADO EN LA
APERTURA Y ANTES DE LA PRIMERA TAREA, PARA QUE UNA VUELTA CORTADA DEJE REPORTE
PARCIAL Y NO VACIO (EJECUTOR.md 1, EL REPORTE ABRE CON LA VUELTA).

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3).

LA DIFERENCIA CON EL DE LA 207, Y ES EL ENCARGO DE ESTA VUELTA: aquel nacio SIN
las cuatro marcas del anexo y hubo que remendarlo a mano con
_v207_marcas_anexo.py, que su propio reporte declaro como caida C.1. AQUI LAS
CUATRO MARCAS NACEN CON EL ESQUELETO, y NO SE TECLEAN: se IMPORTAN de
anexar_tarea_al_reporte.py, que es el instrumento que las lee. Si aquel fichero
cambiara un literal, este esqueleto cambiaria con el; una copia tecleada no.

Y SE MIRA QUE EXIGE EL INSTRUMENTO ANTES DE TALLAR, NO DESPUES. Sus cuatro
exigencias, comprobadas al final de esta corrida sobre el texto escrito:
  (1) cada una de las cuatro marcas aparece EXACTAMENTE UNA VEZ;
  (2) cada fila con el ancla de una TAREA aparece EXACTAMENTE UNA VEZ;
  (3) esa fila, partida por el separador de celdas, da EXACTAMENTE CUATRO;
  (4) su tercera celda dice ABIERTA, SIN CERRAR, y el bloque del anexo trae el
      literal del vacio, que es el que el instrumento quita al cerrar la primera
      tarea.

NO CLONA NINGUN INSTRUMENTO: importa paso0_archivar_anterior y las marcas de
anexar_tarea_al_reporte. IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5).
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
# EL NUMERO DE VUELTA SE COMPUTA DEL NOMBRE DEL FICHERO, NO SE TECLEA.
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

TAREAS = [
    ('1', 'LOS REGISTROS DE LA VUELTA 207. Leer el acta 207 entera y REMEDIR sus '
          'cifras de crecimiento; escribir `R.72` en `docs/PENDIENTES.md` **por '
          'adicion pura y en su sede**, con el numero COMPUTADO por '
          '`scripts/loop/serie_de_registros.py` y las dos puntas publicadas; '
          'registrar **las ocho adjudicaciones** `6.1` a `6.8` por su numero y su '
          'linea, con la vara del `4.1` del acta 202 corrida por mi; y CORREGIR LA '
          'CAIDA `4.1` DEL AUDITOR CONTRA MI en el reporte ARCHIVADO de la 207, por '
          'CORRECCION DECLARADA y con el texto viejo entero encima'),
    ('2', 'LA `TABLA VIVA DE LOS PUROS` DE `docs/BANCO_DE_TEXTOS.md`, PUESTA AL DIA '
          'POR EL CARRIL DEL BANCO `9.10`. **Primero el DENOMINADOR** de las dos '
          'nominas, recomputado de su nomina de miembros y no de la tabla; despues '
          'las dos filas escritas por CORRECCION DECLARADA con el texto viejo entero '
          'encima; y la `V.3` de la vara de `OP-L-01` dejada MEDIDA con su cita. '
          '**NO SE CIERRA `OP-L-01` Y NO SE TOCA SU CAMPO `estado`**'),
    ('3', 'LA MESA `OP-L-03`, MEDIDA CONTRA LOS DOCUMENTOS QUE SU FICHA NOMBRA, POR '
          'EL MISMO METODO QUE LA `OP-L-01` DE LA 207. La vara SELLADA EN SU PROPIO '
          'COMMIT antes de abrir ningun documento, con cada cita comprobada VERBATIM '
          'y el reparto documental sellado antes de mirar; el cotejo punto por punto '
          'con CUBRE, A MEDIAS o NO CUBRE **y su cita de fichero y linea**; la '
          'cobertura MEDIDA y no narrada. **NO SE CIERRA LA FICHA Y NO SE TOCA SU '
          'CAMPO `estado`**'),
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
> `scripts/loop/_v%(v)d_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se
> hicieron.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, Y ESO ES EL REMIENDO DE MI
> `C.1` DE LA 207.** Aquella vuelta tallo su esqueleto sin la marca de apertura de
> la tabla de tareas, sin la del anexo y sin sus dos cierres, y hubo que ponerselas
> a mano despues con `_v207_marcas_anexo.py`. **Aqui no se teclean: se IMPORTAN de
> `anexar_tarea_al_reporte.py`**, que es el instrumento que las lee, y se comprueba
> ANTES de tallar que es lo que ese instrumento exige. **Las cuatro no se citan
> literalmente en esta prosa a proposito**: la guarda las cuenta sobre el fichero
> entero, y una cita en prosa las duplicaria. Es lo que esta corrida cazo en su
> primer intento, en rojo, y por eso la prosa las nombra en vez de copiarlas.
>
> **EL REPORTE DE LA 207 TAMPOCO ESTABA ARCHIVADO AL ENTRAR, Y ESO SE DECLARA EN
> VEZ DE COPIARSE** (`EJECUTOR.md` 2, EL INSTRUMENTO MANDA). Mi sello de apertura,
> `docs/loop/SALIDA_V%(v)d_APERTURA.txt`, escrito **antes de la primera operacion**,
> publica `CIFRA docs/loop/reportes/REPORTE_V207.md existe al entrar: NO`. Lo
> archiva el PASO 0, que es su sitio, y su salida va sellada en
> `docs/loop/SALIDA_V%(v)d_PASO0_ARCHIVAR.txt`.
>
> **TRES SUB-TAREAS.** El tope volvio a CINCO (`AUDITOR.md` 6.2, adjudicacion `6.5`
> del acta 207: la 206 y la 207 cerraron las dos su propio reporte con
> `cerrar_reporte.py`), y el encargo pone TRES y no cinco porque la TAREA 2 toca una
> sede sellada del banco.
>
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA**
> (`AUDITOR.md` 6.1, adjudicacion `6.7` del acta 207). La ultima fue la **205** y
> la siguiente es la **210**. La **seccion 9 cierra igual**, con el **HUECO
> DECLARADO Y MEDIDO** y sus **tres piezas juntas**: el nombre del fichero, los
> bytes medidos **distinguiendo el cero de ausencia del cero de fichero vacio**, y
> la atribucion.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Todo lo que esta vuelta
> escribe son ficheros `_v%(v)d_*` **con prefijo de guion bajo, fuera del censo y
> fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda. **EL
> TRABAJO ES EL PLAN**, y por eso las TAREAS 2 y 3 son mesas del plan.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

%(abre_cab)s
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta %(v)d`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
%(fin_cab)s

## 1. LAS TRES TAREAS DEL ENCARGO, Y SU ESTADO

%(abre_tabla)s
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
%(filas)s
%(fin_tabla)s

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

%(abre_anexo)s
%(vacio)s
%(fin_anexo)s

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

""" % {"v": VUELTA, "rama": rama, "filas": filas,
       "abre_cab": "<!-- CABECERA TALLADA -->",
       "fin_cab": "<!-- FIN CABECERA TALLADA -->",
       "abre_tabla": ABRE_TABLA, "fin_tabla": FIN_TABLA,
       "abre_anexo": ABRE_ANEXO, "fin_anexo": FIN_ANEXO, "vacio": VACIO}

# SE VALIDA ANTES DE ESCRIBIR, Y NO DESPUES. La primera corrida de este
# fichero hacia lo contrario y por eso dejo el REPORTE.md pisado en disco con
# un texto que su propia guarda declaraba ROJO: exactamente la especie de la
# C.4 de la 207 sobre cerrar_reporte.py. Aqui el texto se COMPONE en memoria,
# se juzga entero, y SOLO se escribe si el juicio sale en cero fallos.
fallos = 0
print("LO QUE anexar_tarea_al_reporte.py EXIGE, COMPROBADO SOBRE LO ESCRITO:")
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
