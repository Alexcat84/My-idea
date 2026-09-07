# -*- coding: utf-8 -*-
"""GENERADOR DE UN SOLO USO de la TAREA 3 de la vuelta 195: anade a los CUATRO
arneses que la guarda ve como `NO DECIDIBLE` la DECLARACION de sujeto congelado
que la propia regla pide, con el MOTIVO MEDIDO de cada uno y no con un sello de
goma.

LA REGLA, LEIDA DE `verificar_mutaciones_viejas.py` Y NO DE MEMORIA: un arnes que
trae huellas de LAS DOS especies sale `NO DECIDIBLE` a menos que **el propio arnes
lo declare** con el literal `SUJETO CONGELADO`. Ese es el carril, y la alternativa
que la regla ofrece es `CASO DECLARADO`.

Y LA DECLARACION NO ES UN SELLO DE GOMA: los cuatro se miraron uno a uno ANTES de
escribir nada, y en los cuatro **la huella de vivo NO es una apertura del fichero
vivo**. Lo que cada uno hace de verdad va escrito en su propia declaracion.

Se borra al cerrar la vuelta; su producto son los cuatro ficheros parcheados."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)

# (fichero, ancla tras la que se inserta, texto de la declaracion)
DECLARACIONES = [
    ("scripts/loop/vuelta193_tarea4e_mutacion_sello_entre_procesos.py",
     '''
--- SUJETO CONGELADO, DECLARADO EN LA VUELTA 195 (TAREA 3.c) ---

**LA HUELLA DE VIVO QUE LA GUARDA VE AQUI ES `REPORTE.md`, Y NO ES UNA APERTURA
DE ESE FICHERO.** Es el argumento de `AP.apuntar("REPORTE.md")` dentro del
programa hijo que este arnes lanza: **una CADENA que se mete en la bitacora del
turno para poder comprobar si sobrevive entre procesos**. `apuntar()` escribe un
nombre en una lista; no abre, no lee y no toca `docs/loop/REPORTE.md`.

**LO QUE ESTE ARNES SI TOCA, Y ESO SI ES SU SUJETO:** un directorio temporal de
`mkdtemp` donde redirige `AP.RUTA_DEL_TURNO` y donde escribe sus sellos y su
turno de mentira. **Todo lo que abre en escritura vive dentro de ese temporal**, y
`P.16` (quien fabrica limpia) lo retira al salir.

**POR ESO SU SUJETO ESTA CONGELADO** y esta declaracion lo dice con el literal que
la regla de la vuelta 148 pide. **La cadena que la guarda confunde con un fichero
no se cambia**: cambiarla para contentar a la guarda seria falsear la prueba, que
es justamente comprobar que ESE nombre viaja entre procesos.'''),

    ("scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py",
     '''
--- SUJETO CONGELADO, DECLARADO EN LA VUELTA 195 (TAREA 3.c) ---

**LA HUELLA DE VIVO QUE LA GUARDA VE AQUI ES `REPORTE.md`, Y ES UNA LINEA QUE
ESTE ARNES IMPRIME PARA DECIR QUE NO LO TOCA:** *"Aqui no se escribe ningun
reporte y no se toca docs/loop/REPORTE.md."* La guarda mira la maquina (el fichero
sin su docstring de modulo) y ahi esa frase es un `w(...)`, no una apertura.

**CUAL ES SU SUJETO DE DATOS, DICHO SIN ADORNARLO: CADENAS FABRICADAS EN
MEMORIA.** Todas las llamadas a las funciones PURAS de `cerrar_reporte.py` van
sobre textos que este proceso construye, y **no lee ningun fichero de datos de la
campana**.

**Y LO UNICO QUE SI LEE DEL DISCO SE DICE EN VEZ DE CALLARLO:** abre
`scripts/loop/cerrar_reporte.py`, que es **el codigo bajo prueba**, y publica su
`sha256` como procedencia. Eso no es un sujeto que se mueva por debajo: es la
identidad del modulo que se esta probando, y **todo arnes importa el codigo que
prueba**. La huella `sha256` que la guarda ya le ve sale precisamente de ahi.

**POR ESO SU SUJETO ESTA CONGELADO** y esta declaracion lo dice con el literal que
la regla de la vuelta 148 pide.'''),

    ("scripts/loop/vuelta187_tarea4_mutacion_dos_convenciones.py",
     '''
--- SUJETO CONGELADO, DECLARADO EN LA VUELTA 195 (TAREA 3.c) ---

**LA HUELLA DE VIVO QUE LA GUARDA VE AQUI ES `REPORTE.md`, Y NUNCA ES EL FICHERO
DEL ARBOL DE TRABAJO:** todas sus apariciones en la maquina son parte de
`git show bb3aaad3:docs/loop/REPORTE.md`, o sea **el BLOB de un commit fijo**, con
el hash escrito en la constante `COMMIT_DE_LA_C1` de este mismo fichero.

**UN BLOB DE GIT NO SE MUEVE.** Es exactamente la especie de sujeto que
`HUELLAS_DE_CONGELADO` ya reconoce por `git show`, y el arnes la trae. Lo que le
faltaba era la DECLARACION que la regla pide cuando un texto trae huellas de las
dos especies, y va aqui.

**NO SE TOCA `docs/loop/REPORTE.md`** ni en lectura del arbol ni en escritura: la
ruta solo aparece detras de un `git show` con su commit delante.'''),

    ("scripts/loop/vuelta188_tarea4_mutacion_cobertura_parejas.py",
     '''
--- SUJETO CONGELADO, DECLARADO EN LA VUELTA 195 (TAREA 3.c) ---

**LA HUELLA DE VIVO QUE LA GUARDA VE AQUI ES `REPORTE.md`, Y ES EL VALOR DE LA
CONSTANTE `RUTA_DEL_187`, QUE SOLO SE USA DETRAS DE UN `git show`:** las dos
llamadas que la usan son `git_show("%s:%s" % (COMMIT_DEL_187, RUTA_DEL_187))`, con
`COMMIT_DEL_187` fijo en este mismo fichero. O sea **el BLOB de un commit fijo**,
que no se mueve.

**EL FICHERO DEL ARBOL DE TRABAJO NO SE ABRE EN NINGUN MOMENTO** para ese sujeto:
lo que el arnes abre en escritura es su propia salida sellada, y lo que abre en
lectura son textos fabricados y el blob de arriba.

**POR ESO SU SUJETO ESTA CONGELADO** y esta declaracion lo dice con el literal que
la regla de la vuelta 148 pide.'''),
]

MARCA = "SUJETO CONGELADO, DECLARADO EN LA VUELTA 195"

for rel, decl in DECLARACIONES:
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    t = io.open(ruta, encoding="utf-8").read()
    if MARCA in t:
        print("YA DECLARADO, no se toca: %s" % rel)
        continue
    # EL DOCSTRING DE MODULO ES EL SITIO, Y SE DICE POR QUE: la huella de
    # congelado se busca en el TEXTO ENTERO, asi que la declaracion vale ahi; y
    # el docstring es donde esta casa escribe lo que un fichero declara de si
    # mismo. NO se toca ni una linea de maquina.
    ini = t.index('r"""') if t.startswith("# -*- coding: utf-8 -*-" + NL + 'r"""') \
        else t.index('"""')
    cierre = t.index('"""', ini + 4)
    nuevo = t[:cierre] + decl.rstrip() + NL + NL + t[cierre:]
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(nuevo)
    print("DECLARADO: %-58s %d -> %d bytes"
          % (rel, len(t.encode("utf-8")), len(nuevo.encode("utf-8"))))
