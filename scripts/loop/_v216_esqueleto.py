# -*- coding: utf-8 -*-
r"""_v216_esqueleto.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 216, TALLADO EN LA
APERTURA Y ANTES DE LA PRIMERA TAREA, PARA QUE UNA VUELTA CORTADA DEJE REPORTE
PARCIAL Y NO VACIO (EJECUTOR.md 1, EL REPORTE ABRE CON LA VUELTA).

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3).

SE MANTIENE LA FORMA DE LA 209 A LA 215: las cuatro marcas del anexo NACEN CON
EL ESQUELETO y NO SE TECLEAN, se IMPORTAN de anexar_tarea_al_reporte.py; y EL
TEXTO SE COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE ESCRIBE SI EL JUICIO DA
CERO FALLOS.

NO CLONA NINGUN INSTRUMENTO: importa paso0_archivar_anterior y las marcas de
anexar_tarea_al_reporte. IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5).

LA 216 NO ES VUELTA DE BATERIA Y LLEVA CUATRO TAREAS: CUATRO FILAS. El tope es
de CINCO (acta 212, adjudicacion 6.8, linea 75168 de ACTA_AUDITOR.md, leida en
esta vuelta) y estas cuatro no lo agotan porque el encargo dice que no hacen
falta mas.

Y LA C.1 DE LA 213 NO SE REPITE: esta prosa NO nombra ningun directorio de dos
tramos entre comillas inversas, porque vuelta186_rutas_del_reporte.py los lee
como rutas y revienta. La guarda esta abajo y cuenta.
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
    ('1', 'LOS REGISTROS, Y VA PRIMERA PORQUE LAS DEMAS SE APOYAN EN ELLA. Leer el acta '
          'de la vuelta 215 en `docs/loop/ACTA_AUDITOR.md`, sus secciones 3, 5 y 6, y '
          'REGISTRAR LAS OCHO ADJUDICACIONES DE LA 5.1 A LA 5.8 CON LA LINEA DE DONDE '
          'SALE CADA UNA, leida con un instrumento y no tecleada; las cuatro que obligan '
          'van con DOS COLUMNAS SEPARADAS, el titulo VERBATIM y la lectura mia. Y '
          'registrar las DOS CORRECCIONES DECLARADAS del auditor con su cifra, y su '
          'UNICA CIFRA MALA, que es suya y se escribe igual'),
    ('2', 'LA RE-MEDICION QUE EL FUNDADOR ORDENO EL 9 SEP 2026, Y ES EL CORAZON DE ESTA '
          'VUELTA Y ES BLOQUEANTE. Sacar CON UN INSTRUMENTO las clausulas de las CATORCE '
          'filas de derivacion de `docs/plan/08_VERIFICACION.md`, publicar cuantas filas '
          'se armaron y cuantas deberia haber EN LA MISMA LINEA, y medir cada una con su '
          'busqueda corrida y su cifra delante, incluidas las que dan cero. La ficha '
          'OP-V-01 tiene trato propio por la DECISION 2: su prueba va POR CITA DE LA '
          'CORRIDA K YA ESCRITA, y si no aparece, ESO TAMBIEN ES UN RESULTADO. Y el caso '
          'rojo se prueba POR MUTACION, en memoria y sin escribir en ninguna ficha'),
    ('3', 'LA CONSECUENCIA, MEDIDA Y SIN TOCAR UN SOLO CAMPO DE ESTADO. Publicar ficha '
          'por ficha cuantas clausulas quedan en CUBRE para las CINCO; volver a correr '
          'la vara `scripts/loop/vuelta150_3_relectura_expediente.py` con el hash de MI '
          'apertura y publicar MI cifra sin copiar la del auditor; PUBLICAR LAS DOS '
          'VARAS LADO A LADO sin maquillar que miden cosas distintas; y PROPONER, no '
          'declarar, si la campana queda consumada en lo que el bucle puede consumar'),
    ('4', 'EL CIERRE INTEGRAL Y EL REPORTE. El ciclo entero de Gate 0 por los dos lados '
          'con su consola SELLADA desde dentro del propio instrumento, manteniendo el '
          'remedio de la 215 y sin aflojarlo; las tres suites solas con su exitcode y '
          'sus bytes; marcador y censo recomputados cada uno con su comando; las rutas '
          'con `scripts/loop/vuelta186_rutas_del_reporte.py` corrido DESPUES de cerrar '
          'el reporte; la cabecera con su tallador y su comparacion; y el cierre con '
          '`scripts/loop/cerrar_reporte.py`, que con la 215 hacen dos seguidas'),
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
print("   existe AHORA, antes del PASO 0.c: %s"
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
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO DE LA 209 A LA 215.**
> No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el
> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **CUATRO TAREAS, Y LA %(v)d NO ES VUELTA DE BATERIA Y NO LA CORRE.** La 215 la
> corrio entera y el auditor la declaro CORRIDA en su adjudicacion 5.1; la
> cadencia de cinco de `AUDITOR.md` 6.1 pone la siguiente en la **220**. La
> seccion 9 de este reporte cierra por tanto con el **HUECO DECLARADO Y MEDIDO**
> por el carril de la TAREA 1.b de la vuelta 173, que es lo que la 6.1 manda en
> las vueltas intermedias. **El tope de sub-tareas es CINCO** (acta 212,
> adjudicacion 6.8, **linea 75168** de `docs/loop/ACTA_AUDITOR.md`, leida en esta
> vuelta), y **estas cuatro no lo agotan porque el encargo dice que no hacen
> falta mas**.
>
> **ESTA VUELTA CORRE LA UNICA COSA QUE LE QUEDA AL PLAN, Y NO ES DEL AUDITOR: LA
> ORDENO EL FUNDADOR.** Su sede es
> `docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md`, DECISION 2, y su letra
> verbatim es *"las cinco fichas SIN EJECUTAR se re-miden contra esas filas
> (OP-V-01 con su prueba por cita de la corrida K ya escrita)"*. **La re-medicion
> es la TAREA 2 y es bloqueante.**
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo, y ninguno reparado: **las cuatro tareas son MEDICION y
> VERIFICACION**, que es lo que la moratoria protege. Todo lo que esta vuelta
> escribe en el arbol scripts/loop (**sin comillas inversas, por la obligacion del
> 6.2 del acta 212**) son ficheros `_v%(v)d_*` **con prefijo de guion bajo, fuera
> del censo y fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se
> poda.
>
> **Y RIGE LA PROHIBICION QUE NO SE NEGOCIA: NINGUNA TAREA DE ESTA VUELTA MUEVE EL
> CAMPO DE ESTADO DE NINGUNA FICHA.** La vara del trabajo pendiente es el
> instrumento y nunca ese campo (recuadro de `AUDITOR.md` 0, decision del fundador
> del 4 sep 2026). Se mide, se publica y se dice. **No se escribe.**
>
> **RIGE LA OBLIGACION DE DICTADO DEL 6.6 DEL ACTA 210:** toda cita de un acta
> anterior lleva **LA LINEA** de `docs/loop/ACTA_AUDITOR.md` donde vive el texto
> citado, **y la linea se LEE, no se recuerda**.
>
> **RIGE LA OBLIGACION DE LAS FILAS:** toda tabla que un compositor arme leyendo
> filas de una salida publica, EN LA MISMA LINEA, cuantas filas armo; y si al lado
> va una cifra de cuantas deberia haber, LAS DOS SE ESCRIBEN JUNTAS.
>
> **Y RIGEN LAS TRES OBLIGACIONES DE DICTADO DEL ACTA 212, LAS TRES SIN CODIGO:**
> ningun reporte cita un directorio a secas como ruta entre comillas inversas
> (adjudicacion 6.2); una seccion suplementaria va detras de la que amplia y nunca
> detras de una mayor (hallazgo 7.1); y el tallador de cabecera corrido en la
> apertura escribe en un nombre con `_RECHAZO`, no en el del cierre.
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**
> `docs/loop/SALIDA_V%(v)d_APERTURA.txt`,
> `docs/loop/SALIDA_V%(v)d_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre. **Y el remedio de la
> 215 se mantiene y no se afloja: el ciclo SELLA SU PROPIA CONSOLA en
> `docs/loop/SALIDA_V%(v)d_CICLO_GATE0_APERTURA_CONSOLA.txt`, que es el nombre
> exacto que el compositor busca, y cae en rojo por sus dos puertas, la del
> fichero ausente y la del fichero de cero bytes.**

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

%(abre_cab)s
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta %(v)d`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
%(fin_cab)s

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

%(abre_tabla)s
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
%(filas)s
%(fin_tabla)s

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

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
print("LA GUARDA DE LA C.1 DE LA 213: DIRECTORIOS DE DOS TRAMOS ENTRE COMILLAS INVERSAS")
sospechosos = [c for c in re.findall(r"`([^`]+)`", texto)
               if c.endswith("/") and c.count("/") >= 2]
print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
      % len(sospechosos))
for s in sospechosos:
    print("   sospechoso> %s" % s)
if sospechosos:
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
