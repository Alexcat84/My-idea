# -*- coding: utf-8 -*-
r"""_v220_gen_esqueleto.py . COMPONE scripts/loop/_v220_esqueleto.py A PARTIR
DEL DE LA 219.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). No es arnes ni guarda: es el compositor
del esqueleto de esta vuelta, y muere con ella.

QUE CONSERVA Y QUE CAMBIA, DICHO PARA QUE SE PUEDA AUDITAR: se conserva ENTERA
la mitad mecanica del esqueleto de la 219 (las guardas de las cuatro marcas, el
juicio en memoria, la guarda de directorios entre comillas inversas, la de
guiones largos y medios, la escritura y la relectura del disco). Se reescriben
SOLO tres piezas, que son las tres que cambian de vuelta en vuelta: el
docstring, la lista TAREAS y la prosa de cabecera del reporte.
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AQUI = os.path.dirname(os.path.abspath(__file__))

src = io.open(os.path.join(AQUI, "_v219_esqueleto.py"), encoding="utf-8").read()
src = src.replace(chr(13) + chr(10), chr(10))

# --- 1. el docstring ------------------------------------------------------
i0 = src.index('r"""')
i1 = src.index('"""', i0 + 4) + 3
DOC = chr(10).join([
    'r"""_v220_esqueleto.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 220, TALLADO EN LA',
    'APERTURA Y ANTES DE LA PRIMERA TAREA, PARA QUE UNA VUELTA CORTADA DEJE REPORTE',
    'PARCIAL Y NO VACIO (EJECUTOR.md 1, EL REPORTE ABRE CON LA VUELTA).',
    '',
    'COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la',
    'nomina (moratoria de AUDITOR.md 6.3).',
    '',
    'SE MANTIENE LA FORMA DE LA 209 A LA 219: las cuatro marcas del anexo NACEN CON',
    'EL ESQUELETO y NO SE TECLEAN, se IMPORTAN de anexar_tarea_al_reporte.py; y EL',
    'TEXTO SE COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE ESCRIBE SI EL JUICIO DA',
    'CERO FALLOS.',
    '',
    'NO CLONA NINGUN INSTRUMENTO: importa paso0_archivar_anterior y las marcas de',
    'anexar_tarea_al_reporte. IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5,',
    'linea 72517 de docs/loop/ACTA_AUDITOR.md, leida en esta vuelta).',
    '',
    'LA 220 SI ES VUELTA DE BATERIA Y LLEVA DOS TAREAS: DOS FILAS. La primera es el',
    'registro que el formato fijo obliga y la segunda es la bateria entera y sola,',
    'que es lo que AUDITOR.md 6.1 manda. El tope es de CINCO (acta 212, adjudicacion',
    '6.8, linea 75168 de docs/loop/ACTA_AUDITOR.md, leida hoy del fichero).',
    '',
    'Y LA C.1 DE LA 213 NO SE REPITE: esta prosa NO nombra ningun directorio de dos',
    'tramos entre comillas inversas, porque vuelta186_rutas_del_reporte.py los lee',
    'como rutas y revienta. La guarda esta abajo y cuenta.',
    '"""',
])
src = src[:i0] + DOC + src[i1:]

# --- 2. la lista TAREAS ---------------------------------------------------
j0 = src.index("TAREAS = [")
j1 = src.index("]" + chr(10), j0) + 2
T1 = (
    "LOS REGISTROS, Y ES BLOQUEANTE. Anotar las SEIS adjudicaciones del acta 219, "
    "cada una con su rotulo, su numero de adjudicacion y SU LINEA LEIDA DEL "
    "FICHERO; escribir el recuento nuevo de las diecisiete clausulas publicando "
    "LAS DOS CIFRAS JUNTAS, la que el lector mide hoy SIN la adjudicacion 4.5 y la "
    "que la adjudicacion deja, diciendo cual es cual y sin tocar la pagina 08 del "
    "plan; y anotar las SIETE cosas que suben nombradas a la auditoria integral "
    "con su cifra, la primera con SUS TRES OPCIONES, sin resolver ninguna. Cero "
    "escrituras en el plan"
)
T2 = (
    "LA BATERIA DE MUTACIONES, ENTERA Y SOLA. Correr los ONCE TRAMOS "
    "EXPLICITAMENTE, uno por uno, con el lanzador estable "
    "scripts/loop/vuelta183_bateria_por_tramos.py y SIN clonarlo, commiteando cada "
    "tramo con su salida sellada al terminar; sin usar el carril que dice cual "
    "toca como vara de lo que falta en esta vuelta, que es la caida 5.1 del acta "
    "219; con la doble corrida y el reloj intactos; componiendo la salida unica "
    "SOLO cuando los once tengan salida sellada, con su nombre, sus bytes por las "
    "dos convenciones y su atribucion, LAS TRES JUNTAS, y diciendo las dos cosas "
    "del rotulo; publicando CIFRA tramos con salida sellada no vacia y CIFRA "
    "tramos que faltan medidas sobre las salidas que ESCRIBI YO en esta vuelta; y "
    "parando y trayendo cualquier tramo que salga en rojo, sin arreglarlo"
)
TAREAS = ("TAREAS = [" + chr(10) + "    ('1', %r)," + chr(10)
          + "    ('2', %r)," + chr(10) + "]" + chr(10)) % (T1, T2)
src = src[:j0] + TAREAS + src[j1:]

# --- 3. la prosa de cabecera del reporte ----------------------------------
k0 = src.index('texto = """# REPORTE DE LA VUELTA')
k1 = src.index("## 0. LA IDENTIDAD Y LA CABECERA", k0)
PROSA = chr(10).join([
    'texto = """# REPORTE DE LA VUELTA %(v)d (ejecutor). FASE III, EJECUCION. Rama `%(rama)s`.',
    '',
    '> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`',
    '> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo',
    '> `scripts/loop/_v%(v)d_esqueleto.py` **antes de la primera tarea**; cada tarea',
    '> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el',
    '> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se',
    '> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**',
    '>',
    '> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO DE LA 209 A LA 219.**',
    '> No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el',
    '> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese',
    '> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a',
    '> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa',
    '> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE',
    '> ESCRIBE SI EL JUICIO DA CERO FALLOS.**',
    '>',
    '> **LA OBLIGACION QUE ESTE REPORTE CUMPLIO 17 DE 18 EN LA VUELTA ANTERIOR, Y LA',
    '> UNICA QUE FALLO ESTABA EN ESTE MISMO PARRAFO.** Es el `6.6` del acta 210, que',
    '> vive en la **linea 74203** de `docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero',
    '> y no recordada: **toda cita de un acta anterior lleva SU NUMERO DE ACTA Y LA',
    '> LINEA donde vive el texto citado, y la linea se lee del fichero**. **Mi reporte',
    '> de la 219 escribio aqui `linea 77463` y el texto de las once citas vive en la',
    '> `77461`**: es la caida `2.1` del acta 219 (**linea 77808**), y la unica de sus',
    '> dieciocho referencias de linea que no calzo. **En este reporte cada linea se ha',
    '> leido del fichero antes de escribirla, empezando por las de este parrafo.**',
    '>',
    '> **DOS TAREAS, Y LA %(v)d SI ES VUELTA DE BATERIA.** La cadencia de cinco de',
    '> `AUDITOR.md` 6.1 la pone aqui: la 215 fue la ultima que la corrio. **La bateria',
    '> VA SOLA y no lleva trabajo de plan al lado**, y la TAREA 1 es el registro que el',
    '> formato fijo de `AUDITOR.md` 1.4 obliga a poner en todo encargo, no un segundo',
    '> trabajo. La seccion 9 de este reporte cierra por tanto **CON LA BATERIA DENTRO**',
    '> y no con el hueco declarado.',
    '>',
    '> **EL TOPE DE SUB-TAREAS ES CINCO** (acta 212, adjudicacion `6.8`, **linea',
    '> 75168** de `docs/loop/ACTA_AUDITOR.md`), y el encargo me da **DOS**.',
    '>',
    '> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni',
    '> lector nuevo, y ninguno reparado. **En particular NO SE REPARA EL CARRIL DEL',
    '> LANZADOR DE LA BATERIA QUE DICE CUAL TRAMO TOCA**, que el acta 219 midio',
    '> mintiendo (caida `5.1`, **linea 77991**): la moratoria lo prohibe y no hay caida',
    '> de dato que lo exija. Todo lo que esta vuelta escribe en el arbol scripts/loop',
    '> (**sin comillas inversas, por la obligacion del `6.2` del acta 212**) son',
    '> ficheros `_v%(v)d_*` **con prefijo de guion bajo, fuera del censo y fuera de la',
    '> nomina**. La nomina sigue **CONGELADA EN 135** y no se poda.',
    '>',
    '> **Y RIGE LA PROHIBICION QUE NO SE NEGOCIA: NINGUNA TAREA DE ESTA VUELTA MUEVE EL',
    '> CAMPO DE ESTADO DE NINGUNA FICHA**, ni toca `docs/plan/08_VERIFICACION.md`, ni',
    '> el inventario, ni el expediente, ni `docs/plan/07_ADUANA.md`, **cuyas celdas son',
    '> sede del fundador**. Se lee, se mide, se publica y se dice. **No se escribe.**',
    '> Los `sha256` se publican al entrar y al salir **por las dos convenciones**, y',
    '> tienen que coincidir.',
    '>',
    '> **RIGE LA OBLIGACION DE LA PAREJA DE BYTES, Y CON EL REMEDIO DE MI PROPIA `C.4`',
    '> DE LA 219 DELANTE** (acta 219, seccion 6 punto 7, **linea 78062**), con mis',
    '> palabras: **la pareja de bytes no es una regla de RUTAS, es una regla de CIFRAS',
    '> DE BYTES, vengan de una ruta o de un campo de texto de un registro**. Cada cifra',
    '> de bytes con sus dos convenciones **EN SU MISMA LINEA**, los bytes exactos y',
    '> nunca redondeados, y los KB solo entre parentesis y detras del byte (`P.2`).',
    '>',
    '> **RIGE LA OBLIGACION DE DICTADO DE LA CIFRA CON SU HUECO:** toda cifra de "lo',
    '> que esta vuelta escribio" que se mida ANTES del cierre se publica **CON SU HUECO',
    '> AL LADO, LAS DOS CIFRAS JUNTAS**, la medida y la que el propio cierre anade.',
    '>',
    '> **RIGE LA OBLIGACION DE LAS FILAS:** toda tabla que un compositor arme leyendo',
    '> filas de una salida publica, EN LA MISMA LINEA, cuantas filas armo; y si al lado',
    '> va una cifra de cuantas deberia haber, LAS DOS SE ESCRIBEN JUNTAS.',
    '>',
    '> **Y RIGEN LAS TRES OBLIGACIONES DE DICTADO DEL ACTA 212, LAS TRES SIN CODIGO:**',
    '> ningun reporte cita un directorio a secas como ruta entre comillas inversas',
    '> (adjudicacion `6.2`); una seccion suplementaria va detras de la que amplia y',
    '> nunca detras de una mayor (hallazgo `7.1`); y el tallador de cabecera corrido en',
    '> la apertura escribe en un nombre con `_RECHAZO`, no en el del cierre.',
    '>',
    '> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**',
    '> `docs/loop/SALIDA_V%(v)d_APERTURA.txt`,',
    '> `docs/loop/SALIDA_V%(v)d_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de',
    '> Gate 0 nacen **antes de la primera tarea**, no al cierre. **Y la apertura sella',
    '> ademas, una a una, LAS ONCE SALIDAS DE TRAMO QUE YA ESTABAN EN DISCO**, que son',
    '> las de la 215, para que la cifra de lo que ESTA vuelta escribio se pueda medir',
    '> contra algo y no contra un recuerdo. **El remedio de la 215 se mantiene y no se',
    '> afloja: el ciclo SELLA SU PROPIA CONSOLA en',
    '> `docs/loop/SALIDA_V%(v)d_CICLO_GATE0_APERTURA_CONSOLA.txt`, que es el nombre',
    '> exacto que el compositor busca, y cae en rojo por sus dos puertas, la del',
    '> fichero ausente y la del fichero de cero bytes.**',
    '>',
    '> **Y NO SE REPARA `scripts/loop/vuelta150_4_tabla_por_fase.py`.** Sigue saliendo',
    '> con exitcode 1 y `AssertionError` porque la tabla no trae ocho filas, trae 11,',
    '> y la moratoria `6.3` lo cubre por su propia letra. **Sube nombrado y sin',
    '> reparar, otra vez** (acta 219, seccion 6 punto 4, **linea 78049**).',
    '',
    '',
])
src = src[:k0] + PROSA + src[k1:]

destino = os.path.join(AQUI, "_v220_esqueleto.py")
io.open(destino, "w", encoding="utf-8", newline=chr(10)).write(src)
print("COMPUESTO %s -> %d bytes" % (os.path.basename(destino),
                                    len(src.encode("utf-8"))))
print("CIFRA guiones largos en el compuesto: %d | CIFRA guiones medios: %d"
      % (src.count(chr(8212)), src.count(chr(8211))))
