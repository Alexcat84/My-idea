# -*- coding: utf-8 -*-
"""vuelta157_tarea1_registrar_adjudicaciones.py . TAREA 1 DE LA VUELTA 157.

DEJA ESCRITAS EN EL REPO LAS DIEZ ADJUDICACIONES DE LA SECCION 6 DEL ACTA 157,
CADA UNA DONDE VIVE, TODAS POR ADICION Y CON CORRECCION DECLARADA. No borra una
sola linea del texto viejo: cada bloque se ANADE al final del docstring, al
final del comentario o al final del campo, con su fecha, su fuente citada y su
motivo.

EL REPARTO ES EL QUE EL ENCARGO NOMBRA, LITERAL:
  6.1 y 6.2   la razon de `LD-OPC05-097` del registro de citas Y
              scripts/loop/vuelta156_tarea2a_pasos_con_hijo.py
  6.3 y 6.4   scripts/loop/vuelta152_registro_de_citas_opc05.py, que es donde
              vive la doctrina de vias y clases
  6.5         la guarda de OP-C-05 de scripts/run_phase1.py
  6.6         el registro (la razon de `LD-OPC05-097`, que es la D cuyo motivo
              es "madre e hijo") Y el instrumento que lo lee
              (vuelta152_registro_de_citas_opc05.py)
  6.7         la funcion de la P3b de
              scripts/loop/vuelta150_3_relectura_expediente.py
  6.8         scripts/loop/vuelta152_registro_de_citas_opc05.py
  6.9         scripts/loop/verificar_mutaciones_viejas.py
  6.10        scripts/loop/verificar_cifras_del_reporte.py

LA ADITIVIDAD SE MIDE, NO SE PROMETE (encargo de la vuelta 157, TAREA 1, y es
lo mismo que se hizo en la 154 y en la 156): para los .py se corre
`git diff --numstat` y se exige BORRADOS 0; para el JSONL se comprueba POR
ASSERT que el texto viejo de cada campo tocado sigue siendo PREFIJO LITERAL del
texto nuevo.

ES IDEMPOTENTE: si el bloque ya esta escrito (se busca su marca literal), no lo
duplica y lo dice.

USO:  python scripts/loop/vuelta157_tarea1_registrar_adjudicaciones.py
"""
import io
import json
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")

MARCA = "ADJUDICACION %s DEL ACTA 157"

PY_TOCADOS = [
    "scripts/loop/vuelta156_tarea2a_pasos_con_hijo.py",
    "scripts/loop/vuelta152_registro_de_citas_opc05.py",
    "scripts/run_phase1.py",
    "scripts/loop/vuelta150_3_relectura_expediente.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/verificar_cifras_del_reporte.py",
]


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)


def insertar_en_docstring(ruta_rel, bloque, marca):
    """Inserta BLOQUE justo antes del cierre del docstring DE MODULO. El texto
    viejo no se toca: el bloque queda al final, detras de todo lo anterior."""
    ruta = os.path.join(RAIZ, ruta_rel)
    texto = leer(ruta)
    if marca in texto:
        return "YA ESTABA", 0
    ini = texto.index('"""')
    fin = texto.index('"""', ini + 3)
    escribir(ruta, texto[:fin] + bloque + texto[fin:])
    return "ANADIDO", len(bloque.splitlines())


def insertar_tras_docstring_de_funcion(ruta_rel, nombre_def, bloque, marca):
    """Inserta BLOQUE justo DESPUES del docstring de UNA FUNCION concreta, que
    es donde el encargo manda la 6.7: "en la funcion de la P3b".

    POR QUE DESPUES DEL DOCSTRING Y NO DENTRO, Y ES UNA CORRECCION DE ESTA MISMA
    VUELTA CAZADA POR LA PROPIA GUARDA DE ADITIVIDAD: el docstring de
    `p3b_caso_positivo` cierra con TRES COMILLAS PEGADAS AL FINAL DE SU ULTIMA
    LINEA DE TEXTO, no en una linea propia como los docstring de modulo. Insertar dentro
    obligaba a re escribir esa ultima linea, y `git diff --numstat` lo canto con
    UN BORRADO. Una linea modificada es una linea borrada, y la regla dice CERO.
    Asi que el bloque va como comentario INMEDIATAMENTE DEBAJO del docstring,
    dentro de la funcion: mismo sitio a efectos de quien lee la P3b, y CERO
    lineas viejas tocadas. La primera version de esta funcion queda descrita
    aqui en vez de borrada."""
    ruta = os.path.join(RAIZ, ruta_rel)
    texto = leer(ruta)
    if marca in texto:
        return "YA ESTABA", 0
    i = texto.index("def %s(" % nombre_def)
    ini = texto.index('"""', i)
    fin = texto.index('"""', ini + 3) + 3
    salto = texto.index("\n", fin) + 1
    escribir(ruta, texto[:salto] + bloque + texto[salto:])
    return "ANADIDO", len(bloque.splitlines())


def insertar_antes_de(ruta_rel, ancla, bloque, marca):
    """Inserta BLOQUE justo antes de la linea ANCLA. Para los comentarios de la
    guarda de OP-C-05, que no viven en un docstring sino dentro de la funcion.
    Como la insercion es ANTES del ancla, el bloque de la vuelta 156 que ya esta
    ahi queda ENCIMA y no se toca."""
    ruta = os.path.join(RAIZ, ruta_rel)
    texto = leer(ruta)
    if marca in texto:
        return "YA ESTABA", 0
    i = texto.index(ancla)
    escribir(ruta, texto[:i] + bloque + texto[i:])
    return "ANADIDO", len(bloque.splitlines())


def entradas():
    return [json.loads(x) for x in leer(REGISTRO).splitlines() if x.strip()]


def guardar_entradas(E):
    with io.open(REGISTRO, "w", encoding="utf-8", newline="\n") as fh:
        for e in E:
            fh.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")


def numstat(ruta_rel):
    r = subprocess.run(["git", "diff", "--numstat", "--", ruta_rel],
                       cwd=RAIZ, capture_output=True)
    linea = r.stdout.decode("utf-8", "replace").strip()
    if not linea:
        return 0, 0
    campos = linea.split("\t")
    return int(campos[0]), int(campos[1])


# --------------------------------------------------------------------------
# 6.1 y 6.2, EN EL INSTRUMENTO QUE MIDIO LOS PASOS CON HIJO
# --------------------------------------------------------------------------

B61_DOC = """
--- ADJUDICACION 6.1 DEL ACTA 157 (3 sep 2026): `LD-OPC05-097` ES D, Y LA
ADJUDICACION 6.1 DEL ACTA 155 QUEDA REVOCADA POR SU PROPIO AUTOR ---

REGISTRO POR ADICION. NADA DE LO ESCRITO ARRIBA SE BORRA, Y EN PARTICULAR NO SE
BORRA EL BLOQUE DE LA 6.1 DEL ACTA 155, QUE PEDIA A Y FUSION: taparlo impediria
auditar por que la lectura conjunta existe.

QUE MIDIO ESTE INSTRUMENTO Y COMO ACABO. La medicion que este fichero publico
en la vuelta 156 (el paso 7 del viaje SI tiene hijo vivo con arista puesta) fue
la que decidio la clase, y el auditor la re verifico con instrumento propio
(acta 157, seccion 3.1, salida `_auditor_v157_097_grafo.txt`) y la dio por
CIERTA. Las tres mediciones del auditor, escritas aqui para que no haya que ir
al acta:
  (i)   `docs/plan/PASO_NODO_CALIBRADO.jsonl` YA TRATA A `juran_rcca_metodo`
        COMO MADRE, con DOS filas propias: su paso 2 con hijo
        `prueba_teorias_causa_raiz` y su paso 3 con hijo
        `diseno_implementacion_remedio`. Los pasos de juran son procedimientos
        nombrados en una linea, que es la definicion literal del 9.6.2, y no lo
        dice una lectura: lo dice un fichero del plan anterior a la discusion.
  (ii)  `resistencia_al_cambio` esta VIVO, la arista esta en LAS DOS VISTAS y
        sus cuatro pasos despliegan el paso 7 del viaje. La medicion de la
        vuelta 156 es cierta.
  (iii) POR LOS DOS CAMINOS POSIBLES LA CLASE ES D. Si el paso 7 es
        procedimiento, el par es madre e hijo y CONTINUA (tercer caso del 9.22).
        Y si alguien insistiera en que los dos restos son procedimiento, el
        propio banco ya resolvio ese caso en el PUESTO 2091, CLASE D.

EL LIMITE QUE SIGUE VIGENTE Y QUE NO CAE CON LA 6.1 DEL ACTA 155: la que salga A
NO SE VOLTEA en una vuelta de lectura. Se marca como discutible, se publica su
caso y NO SE EJECUTA NINGUNA FUSION, porque una fusion necesita su ficha, su
superviviente y su ruta.
"""

B62_DOC = """
--- ADJUDICACION 6.2 DEL ACTA 157 (3 sep 2026): "NINGUN HIJO ADJUDICADO" ES UNA
AUSENCIA BAJO LA VARA DECLARADA, NO UNA PRUEBA DE QUE EL PASO SEA LINEA ---

CORRECCION DECLARADA POR ADICION, Y CORRIGE UN PASO DE RAZONAMIENTO DE ESTE
INSTRUMENTO, NO UNA CIFRA SUYA. La cifra que este fichero midio era cierta; lo
que falla es lo que se dedujo de ella.

LA INFERENCIA QUE NO SE SIGUE. La razon escrita para `LD-OPC05-097` dice "el
paso 1 de juran NO tiene hijo, o sea que ES linea". EL 9.6.2 DA UNA PRUEBA
SUFICIENTE DE QUE UN PASO ES PROCEDIMIENTO ("la prueba de que el paso de la
madre es un procedimiento ES QUE EXISTE EL HIJO QUE LO EJECUTA"), Y UNA PRUEBA
SUFICIENTE NO SE PUEDE DAR LA VUELTA: su ausencia no prueba lo contrario. Y aqui
la ausencia es todavia mas estrecha, porque LA VARA DE ESTE INSTRUMENTO SOLO
MIRA HIJOS ADJUDICADOS EN `docs/plan/PASO_NODO_CALIBRADO.jsonl`: un hijo que
exista en el grafo y que nadie haya adjudicado a ese paso no lo ve.

Y EL CONTRAEJEMPLO ESTA MEDIDO, NO SUPUESTO (auditor, acta 157 seccion 6.2, y re
medido por el ejecutor en la TAREA 3 de la vuelta 157 con
`scripts/loop/vuelta157_tarea3_paso1_de_juran.py`, salida
`docs/loop/SALIDA_V157_T3_PASO1_JURAN.txt`):
`desperdicio_cronico_vs_esporadico` esta VIVO y sus cuatro pasos despliegan
justo el paso 1 de juran (monitorear, diferenciar el pico esporadico del nivel
cronico, accion correctiva, proyecto de mejora), AUNQUE SIN ARISTA Y SIN FILA EN
EL CALIBRADO. O sea: hay hijo, y esta vara no lo veia.

COMO SE LEE DESDE HOY LA SALIDA DE ESTE INSTRUMENTO: "ningun hijo adjudicado"
significa NO HAY HIJO BAJO LA VARA DECLARADA (calibrado mas arista), y NO
significa "el paso es linea". Para afirmar que un paso es linea hace falta una
lectura del grafo que no encuentre quien lo despliegue, y esa lectura este
instrumento NO la hace.

LA CLASE NO SE MUEVE: `LD-OPC05-097` sigue siendo D por la 6.1 del acta 157, que
la sostiene por dos caminos independientes de esta inferencia.
"""

# --------------------------------------------------------------------------
# 6.3, 6.4, 6.6 y 6.8, EN EL INSTRUMENTO DONDE VIVE LA DOCTRINA DE VIAS Y CLASES
# --------------------------------------------------------------------------

B63_DOC = """
--- ADJUDICACION 6.3 DEL ACTA 157 (3 sep 2026): EL SACO DE LAS C SIN FIGURA SE
VACIA LEYENDO, EN LOTES, Y NO EN BLOQUE ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

EL HECHO QUE LO OBLIGA, MEDIDO Y NO SOSPECHADO (auditor, acta 157 seccion 5.1,
salida `_auditor_v157_figura.txt`, con vara propia mas estrecha que la del
ejecutor y coincidiendo en el numero que importa):

    en los 3.388 veredictos del cribado la C aparece 5 veces  : 0,15 por ciento
    en este mismo registro, la via CRIBADO tiene 32 entradas  : CERO en C
    en este mismo registro, la via LECTURA_DIRIGIDA tiene 122 : 119 en C, o sea
                                                                97,5 por ciento
    y el 9.22 dice de su figura: "Primera aparicion en 1.100 pares leidos. Es
    rara".

UNA FIGURA QUE EL BANCO LLAMA RARA NO PUEDE SER EL 97,5 POR CIENTO DE UNA VIA.
LA C DE LA VIA DE LECTURAS DIRIGIDAS Y LA C DEL ARCHIVO NO SON LA MISMA LETRA, y
eso no es una sospecha de redaccion: es una divergencia medida entre dos vias
del mismo fichero.

LAS TRES SALIDAS Y POR QUE SE ELIGE LA SEGUNDA. Reclasificar 116 clases EN
BLOQUE seria mover 116 cifras publicadas sin una lectura detras, que es la
especie exacta de caida que esta campana persigue. Ajustar la vara para que no
las alcance seria dejar escrita como figura rara una letra que el 97,5 por
ciento de una via lleva puesta. SE ADJUDICA LEER: LA CLASE ES UN HECHO SOBRE LOS
NODOS Y SOLO UNA LECTURA LA FIJA. Se lee EN LOTES, una a una.

LAS GUARDAS DEL LOTE, QUE NO SE AFLOJAN: correccion declarada y aditiva en cada
una; `n` NO SE MUEVE; assert de frontera con sha256 de `dataset/` y conteo de
censo y aristas antes y despues (el registro cambia, EL GRAFO NO); Gate 0 al
terminar el lote; y LA QUE SALGA A NO SE VOLTEA, se marca como discutible y no
se ejecuta ninguna fusion.
"""

B64_DOC = """
--- ADJUDICACION 6.4 DEL ACTA 157 (3 sep 2026): NOMBRAR DOS PASOS NO BASTA. LA
FIGURA PIDE DOS LINEAS DISTINTAS Y QUE CADA NODO EXPANDA LA DEL OTRO ---

CORRECCION DECLARADA POR ADICION, y NO ES DOCTRINA NUEVA: es cita literal del
9.22, que escribe su propia comprobacion separadora.

LA VARA, EN UNA SOLA PREGUNTA ESTRECHA Y BINARIA, que es la que se aplica a cada
lectura dirigida en clase C:

    SE PUEDEN NOMBRAR DOS LINEAS DISTINTAS, UNA EN CADA NODO, Y DECIR QUE
    PROCEDIMIENTO DEL OTRO NODO EXPANDE CADA UNA?

  - Si SI: la C se sostiene, y la razon LAS NOMBRA.
  - Si NO: la clase es D.
  - Y si la razon describe que CADA NODO EXPANDE LO SUYO, eso es el PUESTO 2091
    del banco y la clase es D. Dos nodos sanos que no se tocan son D, no C.

LO QUE EL 9.22 DICE Y QUE ESTA VARA SOLO REPITE: "Si las dos direcciones apuntan
a la misma linea, no es esta figura". O sea que ni siquiera nombrar dos punteros
de paso basta si los dos punteros van a la misma linea. `LD-OPC05-031` se
delataba solo diciendo de si mismo que las dos son "casi la misma linea" y
sosteniendose "porque el sujeto es distinto": SUJETO DISTINTO ES LA DEFINICION
DE D, NO DE C.

ESTA VARA ALCANZA AL SACO PEQUENO IGUAL QUE AL GRANDE: traer puntero de paso NO
protege. Y no protege tampoco ser SANO: la 6.3 del acta 155 sostuvo
`LD-OPC05-046` en C por el 9.6.3, o sea POR SER SANO, y bajo esta vara SANO SIN
FIGURA ES D. Esa parte de la 6.3 del acta 155 queda revocada por el acta 157.
"""

B66_DOC = """
--- ADJUDICACION 6.6 DEL ACTA 157 (3 sep 2026): LA D SE QUEDA, EL MOTIVO LO
LLEVA LA RAZON, Y ANTES DE PROPONER UNA LETRA NUEVA SE MIDE LA CUENTA ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

LA OBJECION, QUE EL ACTA CONCEDE: la etiqueta D se lee en el archivo como SANO Y
DISTINTO, y hay pares registrados en D cuyo motivo real es MADRE E HIJO, EL PAR
CONTINUA (tercer caso del 9.22). La etiqueta no miente sobre la clase, pero no
cubre uno de sus dos motivos.

POR QUE NO ES PARADA Y NO SE INVENTA LETRA: EL ARCHIVO YA RESOLVIO ESA ESPECIE
EN D DESDE HACE TIEMPO, y el auditor lo midio en el registro del cribado el 3
sep 2026: los PUESTOS 316 ("la eleccion del metodo de estimacion contra la hoja
que lo calcula"), 478 ("EL HIJO CON CASA PROPIA"), 1424, 1494 y 2066 son todos
madre e hijo REGISTRADOS EN D. No hay contradiccion que resolver ni regla nueva
que escribir. UNA LETRA NUEVA SI SERIA DOCTRINA NUEVA Y ESO SI SERIA PARADA: no
se abre sin la cuenta delante.

LO QUE SE ENCARGA ANTES DE QUE NADIE PROPONGA NADA, Y ES SOLO MEDIR: repartir
las D de este registro en MADRE E HIJO (el par continua) contra SANO Y DISTINTO,
por lectura de su razon, publicar los dos conteos y la nomina de cada saco, y
declarar la vara con sus limites. Se hace en la TAREA 8 de la vuelta 157 con
`scripts/loop/vuelta157_tarea8_dos_especies_de_d.py`, salida
`docs/loop/SALIDA_V157_T8_DOS_ESPECIES_D.txt`. ESA TAREA MIDE: no reclasifica
nada y no toca una clase.
"""

B68_DOC = """
--- ADJUDICACION 6.8 DEL ACTA 157 (3 sep 2026): EL LECTOR SE ENSANCHA PARA
ACEPTAR LA CELDA TACHADA Y TOMAR LA ULTIMA CLASE ESCRITA ---

CORRECCION DECLARADA POR ADICION, y toca `citas_de_lectura_dirigida`, que es la
funcion de este fichero que lee `docs/plan/LECTURAS_DIRIGIDAS.md`.

EL CHOQUE QUE LA ORIGINA, Y LAS DOS REGLAS QUE CHOCABAN. La costumbre de la casa
es NO TAPAR LO QUE SE CORRIGE, y en el `.md` eso se escribe tachando la clase
vieja (`~~C~~ D`). Pero el patron de esta funcion pedia `([A-Z]+)` en la celda
de clase, asi que una celda tachada NO CASABA Y LA FILA DESAPARECIA DEL
REGISTRO. Medido por mutacion por el auditor (acta 157, seccion 5.4, salida
`_auditor_v157_tachado.txt`) sobre la fila 97: como estaba, 1 coincidencia; con
`~~C~~ D`, 0 COINCIDENCIAS. La vuelta 156 eligio bien al dejar la celda limpia,
porque lo otro tumbaba Gate 0.

LO QUE SE ADJUDICA: LA GUARDA SE ADAPTA AL REGISTRO HONESTO, NO AL REVES (banco
9, por extension). El patron acepta una celda con una o mas clases tachadas
seguidas de la clase vigente, Y TOMA LA ULTIMA CLASE ESCRITA. Con su caso
positivo por mutacion (`scripts/loop/vuelta157_tarea4b_mutacion_tachado.py`,
salida `docs/loop/SALIDA_V157_T4B_MUTACION_TACHADO.txt`), que exige las tres
cosas: que el lector VIEJO pierda la fila tachada, que el NUEVO la recupere con
la clase buena, Y que el conteo de pares del registro salga IDENTICO antes y
despues sobre el fichero SIN tachar.
"""

# --------------------------------------------------------------------------
# 6.1, 6.2 y 6.6 EN EL REGISTRO, POR ADICION AL CAMPO `razon` DE LD-OPC05-097
# --------------------------------------------------------------------------

B61_REG = (
    "  [ADJUDICACION 6.1 DEL ACTA 157 (2026-09-03), ANADIDA SIN BORRAR NADA DE "
    "LO ANTERIOR: LA CLASE D QUEDA CONFIRMADA POR EL AUDITOR Y SU PROPIA "
    "ADJUDICACION 6.1 DEL ACTA 155, QUE PEDIA A Y FUSION, QUEDA REVOCADA POR SU "
    "AUTOR Y REGISTRADA COMO CAIDA SUYA. Tres mediciones propias del auditor "
    "(acta 157, seccion 3.1): (i) docs/plan/PASO_NODO_CALIBRADO.jsonl ya trata a "
    "juran_rcca_metodo como MADRE, con dos filas propias, su paso 2 con "
    "prueba_teorias_causa_raiz y su paso 3 con diseno_implementacion_remedio, o "
    "sea que los pasos de juran son procedimientos nombrados en una linea por la "
    "definicion literal del 9.6.2; (ii) resistencia_al_cambio esta VIVO, la "
    "arista esta en las dos vistas y sus cuatro pasos despliegan el paso 7 del "
    "viaje, con lo que la medicion de la vuelta 156 es cierta; (iii) por los dos "
    "caminos posibles la clase es D, porque si el paso 7 es procedimiento el par "
    "es madre e hijo y CONTINUA por el tercer caso del 9.22, y si los dos restos "
    "fueran procedimiento el propio banco ya resolvio ese caso en el PUESTO 2091, "
    "CLASE D. NO HAY CANDIDATO A FUSION, NO SE TOCA UNA ARISTA Y n NO SE MUEVE.]")

B62_REG = (
    "  [ADJUDICACION 6.2 DEL ACTA 157 (2026-09-03), ANADIDA SIN BORRAR NADA DE "
    "LO ANTERIOR, Y CORRIGE UN PASO DE RAZONAMIENTO DE ESTA MISMA RAZON, NO SU "
    "CLASE NI UNA CIFRA SUYA: donde arriba se escribe que el paso 1 de juran no "
    "tiene hijo O SEA QUE ES LINEA, esa inferencia NO SE SIGUE. El 9.6.2 da una "
    "prueba SUFICIENTE de que un paso es procedimiento (existe el hijo que lo "
    "ejecuta) y una prueba suficiente no se puede dar la vuelta: su ausencia no "
    "prueba lo contrario. Y la vara que se aplico es todavia mas estrecha, porque "
    "solo mira HIJOS ADJUDICADOS en docs/plan/PASO_NODO_CALIBRADO.jsonl. EL "
    "CONTRAEJEMPLO ESTA MEDIDO: desperdicio_cronico_vs_esporadico esta VIVO y sus "
    "cuatro pasos despliegan justo el paso 1 de juran (monitorear, diferenciar el "
    "pico esporadico del nivel cronico, accion correctiva, proyecto de mejora), "
    "aunque SIN ARISTA Y SIN FILA EN EL CALIBRADO. DESDE HOY 'ningun hijo "
    "adjudicado' se lee como AUSENCIA BAJO LA VARA DECLARADA y no como prueba de "
    "linea. LA CLASE SIGUE SIENDO D por la 6.1 del acta 157, que la sostiene por "
    "dos caminos que no pasan por esta inferencia. Medicion en "
    "docs/loop/SALIDA_V157_T3_PASO1_JURAN.txt.]")

B66_REG = (
    "  [ADJUDICACION 6.6 DEL ACTA 157 (2026-09-03), ANADIDA SIN BORRAR NADA DE "
    "LO ANTERIOR: LA D DE ESTE PAR SE QUEDA, Y SU MOTIVO NO ES 'SANO Y DISTINTO' "
    "SINO 'MADRE E HIJO, EL PAR CONTINUA', QUE ES EL TERCER CASO DEL 9.22. No se "
    "inventa letra nueva: eso seria doctrina nueva y seria PARADA, y ademas el "
    "archivo ya registra esa especie en D desde hace tiempo, en los puestos 316, "
    "478, 1424, 1494 y 2066 del propio registro del cribado, medidos por el "
    "auditor el 3 sep 2026. LA ETIQUETA NO MIENTE SOBRE LA CLASE: lo que no cubre "
    "es uno de sus dos motivos, y por eso el motivo lo lleva esta razon. La "
    "cuenta de las dos especies, que es lo que hay que tener delante ANTES de que "
    "nadie proponga una letra, se mide en la TAREA 8 de la vuelta 157 y se "
    "publica en docs/loop/SALIDA_V157_T8_DOS_ESPECIES_D.txt.]")

# --------------------------------------------------------------------------
# 6.5, EN LA GUARDA DE OP-C-05 DE run_phase1.py
# --------------------------------------------------------------------------

ANCLA_65 = "    # ── FIN OP-C-05 ─"

B65 = """    # CORRECCION DECLARADA POR ADICION (2026-09-03, vuelta 157, TAREA 1,
    # ADJUDICACION 6.5 DEL ACTA 157). NADA DE LOS COMENTARIOS DE ARRIBA SE
    # BORRA, Y EN PARTICULAR NO SE BORRA EL BLOQUE DE LA 6.9 DEL ACTA 155 QUE
    # ESTA JUSTO ENCIMA: esta adjudicacion lo CONFIRMA, no lo enmienda.
    #
    # QUE SE PREGUNTO. El ejecutor de la vuelta 156 marco como DISCUTIBLE 2 la
    # segunda mitad de aquella 6.9: el encargo mandaba la adjudicacion A LOS
    # COMENTARIOS, y el ejecutor ademas cambio LA LINEA DE DETALLE DEL CHECK
    # para que publicara el hueco, leyendo que "su cuenta se publica cada vez
    # que la guarda hable" no lo puede cumplir un comentario, porque un
    # comentario no habla cada vez. Lo marco por si sobraba.
    #
    # LA ADJUDICACION: SE QUEDA, Y NO SOBRA. El ejecutor leyo bien la letra: esa
    # frase es LA LINEA DEL CHECK y no el comentario. El auditor lo comprobo en
    # su propia corrida de Gate 0 del 3 sep 2026: la linea publica 154 pares,
    # 154 con cita y 0 sin cita, y nombra LOS TRES excluidos y el 157 del
    # universo ensanchado, TODO COMPUTADO Y NADA TECLEADO. NO SE REVIERTE.
    #
    # LO QUE ESTO DEJA ESCRITO PARA EL QUE VENGA DETRAS: cuando una adjudicacion
    # mande "publicar" una cuenta, la sede es LA SALIDA DE LA GUARDA y no su
    # comentario. Un comentario deja constancia; solo la salida publica.
"""

# --------------------------------------------------------------------------
# 6.7, EN LA FUNCION DE LA P3b
# --------------------------------------------------------------------------

B67 = """    # --- ADJUDICACION 6.7 DEL ACTA 157 (3 sep 2026): MIENTRAS LAS NUEVE
    # SALIDAS NO ENTREN EN LA BATERIA, ESTA P3b ES UN PROXY SIN RESPALDO
    # EFECTIVO ---
    #
    # REGISTRO POR ADICION, Y VA AQUI Y NO DENTRO DEL DOCSTRING POR UNA RAZON
    # MEDIDA: el docstring de arriba cierra con TRES COMILLAS pegadas a su ultima
    # de texto, y meter el bloque dentro obligaba a re escribir esa linea, lo
    # que `git diff --numstat` canta como UN BORRADO. La regla de aditividad de
    # esta vuelta dice CERO borrados, asi que el bloque baja un renglon. Nada de
    # lo escrito arriba se borra, y en particular no se borra el bloque de la
    # 6.6 del acta 155, que nombraba `verificar_mutaciones_viejas.py` como
    # respaldo: esta adjudicacion dice exactamente por que ESE RESPALDO ERA
    # NOMINAL, y la culpa es de aquella adjudicacion, que lo dio por bueno SIN
    # CRUZARLO.
    #
    # LO QUE EL AUDITOR CERRO, Y NO POR NOMBRE (acta 157, seccion 5.4, salida
    # `_auditor_v157_p3b.txt`): busco cada una de las NUEVE salidas citadas
    # DENTRO DEL TEXTO de los VEINTITRES scripts de la bateria, y NINGUNO
    # ESCRIBE NINGUNA. El hueco de 4 DE 4 medido por la vuelta 156 NO ESTA
    # INFLADO, y el discutible 4 de aquel reporte (que declaraba que la
    # correspondencia era por nombre y podia sobre estimar) queda cerrado A
    # FAVOR DE LA CIFRA.
    #
    # LO QUE FALTABA ERA EL COSTE, Y SE MIDE EN VEZ DE ADIVINARSE. Meter nueve
    # scripts mas en cada cierre es una decision de coste por vuelta que no es
    # del ejecutor. La vuelta 157 corre las nueve UNA VEZ, cronometradas por
    # script y con su salida sellada, y publica si cada una todavia MUERDE
    # (`scripts/loop/vuelta157_tarea7_coste_p3b.py`, salida
    # `docs/loop/SALIDA_V157_T7_COSTE_P3B.txt`). CON ESA CIFRA DELANTE se dice
    # cuanto anadirian al cierre de cada vuelta, Y AHI PARA: no se meten en la
    # bateria por cuenta del ejecutor.
    #
    # LA LETRA QUE ESTA FUNCION LLEVA MIENTRAS TANTO, Y ES LA QUE EL ACTA MANDA
    # ESCRIBIR AQUI: LA P3b DE ESAS CUATRO FICHAS (OP-C-05, OP-E-03, OP-E-07 y
    # OP-S-11) ES UN PROXY SIN RESPALDO EFECTIVO. Sostiene que el artefacto de
    # la prueba EXISTE al corte, y NADIE LA VUELVE A CORRER. Un proxy con su
    # agujero contado es aceptable; un respaldo que no respalda, no.
"""

# --------------------------------------------------------------------------
# 6.9, EN LA BATERIA DE MUTACIONES VIEJAS
# --------------------------------------------------------------------------

B69 = """
--- ADJUDICACION 6.9 DEL ACTA 157 (3 sep 2026): ESTA GUARDA ATRIBUIA SUS ROJOS
AL SCRIPT EQUIVOCADO, Y SE CINE A LOS FICHEROS QUE CADA SCRIPT ESCRIBE ---

CORRECCION DECLARADA POR ADICION. Nada de lo escrito arriba se borra: el cotejo
de reproducibilidad de la TAREA 2.f de la vuelta 141 sigue siendo lo que esta
bateria hace, y sigue siendo necesario.

COMO SE DESCUBRIO, Y LO DESCUBRIO EL AUDITOR CAYENDO EL (acta 157, caida 2 y
seccion 5.3). Corrio esta bateria CON SUS PROPIOS INSTRUMENTOS CORRIENDO AL
LADO, despues de haberle escrito al ejecutor que se corre SOLA. Salio ROJO
exit 1 con DOS "salidas selladas que NO SE REPITEN", acusando a
`vuelta144_2b_mutacion_giro.py` y a `vuelta147_2c_mutacion_vitalidad.py` por
`_auditor_v157_p3b.txt` y `_auditor_v157_tachado.txt`, DOS FICHEROS SUYOS QUE
NINGUNO DE LOS DOS SCRIPTS ESCRIBE: la propia salida decia de los dos "salidas
selladas que escribe: ninguna". Re corrida sola: VERDE. Las dos corridas quedan
selladas en `docs/loop/_auditor_v157_mutaciones.txt` (la roja) y
`_auditor_v157_mutaciones2.txt` (la verde) para poder reproducir el escenario.

EL DEFECTO, EN UNA LINEA: `correr_dos_veces` computaba `inestables` sobre
`set(tras1) | set(tras2)`, o sea SOBRE EL DIRECTORIO ENTERO, y le colgaba a un
script cualquier fichero que apareciera o cambiara mientras el corria. FALLA
RUIDOSO, QUE ESTA BIEN, PERO NOMBRA AL CULPABLE EQUIVOCADO, Y UN ROJO QUE NOMBRA
AL SCRIPT EQUIVOCADO ES UN ROJO QUE NO SE PUEDE SEGUIR: eso es media guarda.

LO QUE SE ADJUDICA, POR EXTENSION DEL BANCO 9 Y SIN DOCTRINA NUEVA:
  (a) LA COMPROBACION DE REPRODUCIBILIDAD SE CINE A `escritos`, que es la lista
      de ficheros que ESE script escribio en su primera corrida, y que esta
      guarda YA COMPUTA Y YA PUBLICA ("salidas selladas que escribe (computadas,
      no tecleadas)"). Ningun fichero fuera de esa lista puede poner a un script
      en NO REPRODUCIBLE.
  (b) LO QUE APAREZCA O CAMBIE EN `docs/loop/` Y NO SEA DE NADIE NO SE CALLA: se
      reporta APARTE, con su nombre, bajo el rotulo RUIDO DE CONCURRENCIA, y NO
      ENCIENDE EL ROJO DE NINGUN SCRIPT. Callarlo seria la caida contraria.
  (c) EL ROJO SE QUEDA INTACTO PARA LO QUE SI ES SUYO: si un fichero que el
      script escribe cambia entre dos corridas, sigue siendo NO REPRODUCIBLE y
      sigue siendo exit 1.

SU CASO POSITIVO POR MUTACION YA EXISTIA ANTES QUE LA CORRECCION, que es lo mas
limpio que le puede pasar a una guarda: es la corrida roja del auditor. Se
reproduce con `scripts/loop/vuelta157_tarea5c_mutacion_ruido.py`, salida
`docs/loop/SALIDA_V157_T5C_MUTACION_RUIDO.txt`, que exige las dos mitades: que
la version VIEJA de `correr_dos_veces` siga saliendo ROJA sobre ese escenario y
que la NUEVA salga VERDE nombrando el ruido aparte. Y LAS 23 SIGUEN SIENDO 23.
"""

# --------------------------------------------------------------------------
# 6.10, EN LA GUARDA DE CIFRAS DEL REPORTE
# --------------------------------------------------------------------------

B610 = """
--- ADJUDICACION 6.10 DEL ACTA 157 (3 sep 2026): UNA SALIDA SELLADA QUE SE RE
ESCRIBE DESPUES DEL COMMIT DE SU TAREA SE DECLARA. NO SE PROHIBE RE SELLAR: SE
PROHIBE RE SELLAR EN SILENCIO ---

CORRECCION DECLARADA POR ADICION. Nada de lo escrito arriba se borra.

DE DONDE NACE, Y NACE DE UNA CAIDA DE REPORTE DEL EJECUTOR (acta 157, seccion
4). La caida 4 del reporte de la vuelta 156 remataba con "las cifras no
cambiaron: lo que cambio fue la columna", y el auditor lo desmintio con
`git diff 92d29d23^ 92d29d23` sobre los propios ficheros del ejecutor: el re
sellado movio `SALIDA_V156_T4C_CIFRAS.txt` de "salidas selladas 52" a 55 y de
"con un nombre de fase que CALZA: 50" a 53, y
`SALIDA_V156_T3A_FIGURA_DELGADA.txt` de {"C": 121, "D": 1} a {"C": 119, "D": 3}.
NINGUNA CIFRA PUBLICADA ERA FALSA, porque el reporte pega las lineas FINALES y
el auditor las verifico todas. LO FALSO ERA LA AFIRMACION SOBRE EL EFECTO DE LA
PROPIA CORRECCION: lo que no movio cifras fue DEDENTAR, lo que las movio fue RE
CORRER MAS TARDE, y la frase juntaba las dos cosas. Vive en prosa y NO ACUMULA,
pero la especie si es estructural: una vara anclada a algo que se mueve.

LO QUE SE ADJUDICA, Y ES POR CONSTRUCCION, NO POR PROMESA: para cada `SALIDA_*`
que el reporte cite, se compara SU VERSION EN EL COMMIT DE SU TAREA contra la de
HEAD, y si cambio, EL REPORTE TIENE QUE DECLARARLO, con el `numstat` y con LA
LISTA DE LINEAS `CIFRA` CUYO VALOR CAMBIO, COMPUTADOS Y NO NARRADOS. Si cambio y
el reporte no lo declara, es ROJO con su nombre.

DONDE VIVE LA GUARDA: `scripts/loop/verificar_re_sellado.py`, con su caso por
mutacion `scripts/loop/vuelta157_tarea6b_mutacion_re_sellado.py` (salida
`docs/loop/SALIDA_V157_T6B_MUTACION_RE_SELLADO.txt`). Se corre en el ciclo de
cierre, al lado de esta guarda.
"""


def main():
    print("=" * 78)
    print("VUELTA 157, TAREA 1: LAS DIEZ ADJUDICACIONES DE LA SECCION 6 DEL ACTA 157,")
    print("ESCRITAS DONDE CADA UNA VIVE, TODAS POR ADICION.")
    print("=" * 78)
    print("")

    hechas = 0
    print("A) LOS SEIS FICHEROS .py")
    docs = [
        ("6.1", "scripts/loop/vuelta156_tarea2a_pasos_con_hijo.py", B61_DOC),
        ("6.2", "scripts/loop/vuelta156_tarea2a_pasos_con_hijo.py", B62_DOC),
        ("6.3", "scripts/loop/vuelta152_registro_de_citas_opc05.py", B63_DOC),
        ("6.4", "scripts/loop/vuelta152_registro_de_citas_opc05.py", B64_DOC),
        ("6.6", "scripts/loop/vuelta152_registro_de_citas_opc05.py", B66_DOC),
        ("6.8", "scripts/loop/vuelta152_registro_de_citas_opc05.py", B68_DOC),
        ("6.9", "scripts/loop/verificar_mutaciones_viejas.py", B69),
        ("6.10", "scripts/loop/verificar_cifras_del_reporte.py", B610),
    ]
    for num, ruta, bloque in docs:
        estado, n = insertar_en_docstring(ruta, bloque, MARCA % num)
        print("  %-4s %-56s %s (%d lineas)" % (num, ruta, estado, n))
        if estado == "ANADIDO":
            hechas += 1

    estado, n = insertar_antes_de("scripts/run_phase1.py", ANCLA_65, B65, MARCA % "6.5")
    print("  %-4s %-56s %s (%d lineas)"
          % ("6.5", "scripts/run_phase1.py (guarda OP-C-05)", estado, n))
    if estado == "ANADIDO":
        hechas += 1

    estado, n = insertar_tras_docstring_de_funcion(
        "scripts/loop/vuelta150_3_relectura_expediente.py", "p3b_caso_positivo",
        B67, MARCA % "6.7")
    print("  %-4s %-56s %s (%d lineas)"
          % ("6.7", "vuelta150_3_relectura_expediente.py (p3b)", estado, n))
    if estado == "ANADIDO":
        hechas += 1

    print("")
    print("B) EL REGISTRO DE CITAS, POR ADICION AL CAMPO `razon` DE LD-OPC05-097")
    E = entradas()
    antes = {e["cita"].split(",")[0]: e["razon"] for e in E}
    reparto = {"LD-OPC05-097": [("6.1", B61_REG), ("6.2", B62_REG), ("6.6", B66_REG)]}
    for e in E:
        ld = e["cita"].split(",")[0]
        for num, bloque in reparto.get(ld, []):
            if (MARCA % num) not in e["razon"]:
                e["razon"] = e["razon"] + bloque
                print("  %-4s %-16s razon ampliada (+%d caracteres)" % (num, ld, len(bloque)))
                hechas += 1
            else:
                print("  %-4s %-16s YA ESTABA" % (num, ld))
    guardar_entradas(E)

    print("")
    print("C) LA ADITIVIDAD SE MIDE, NO SE PROMETE")
    print("")
    print("C.1) LOS .py, POR numstat DE GIT (se exige BORRADOS 0):")
    total_borrados = 0
    for ruta in PY_TOCADOS:
        mas, menos = numstat(ruta)
        total_borrados += menos
        print("     %-56s +%-4d -%d" % (ruta, mas, menos))
        assert menos == 0, "%s tiene %d borrado(s): la escritura NO fue aditiva" % (ruta, menos)
    print("     CIFRA borrados totales en los seis .py: %d" % total_borrados)

    print("")
    print("C.2) EL JSONL, POR ASSERT DE PREFIJO LITERAL sobre el campo `razon`:")
    D = entradas()
    assert len(D) == len(E), "el numero de lineas del registro se movio"
    for d in D:
        ld = d["cita"].split(",")[0]
        assert d["razon"].startswith(antes[ld]), (
            "%s: el texto viejo de `razon` YA NO ES PREFIJO del nuevo" % ld)
    print("     CIFRA entradas del registro con el texto viejo comprobado como PREFIJO: %d"
          % len(D))
    crecio = [d["cita"].split(",")[0] for d in D
              if len(d["razon"]) > len(antes[d["cita"].split(",")[0]])]
    print("     CIFRA entradas cuya `razon` CRECIO: %d (%s)" % (len(crecio), ", ".join(crecio)))

    claves_antes = sorted({k for e in E for k in e})
    claves_despues = sorted({k for d in D for k in d})
    assert claves_antes == claves_despues, "el esquema del registro se movio"
    assert [e["clase"] for e in E] == [d["clase"] for d in D], "esta tarea NO mueve ninguna clase"
    pares_antes = {tuple(sorted(e["par"])) for e in E}
    pares_despues = {tuple(sorted(d["par"])) for d in D}
    assert pares_antes == pares_despues, "esta tarea NO mueve ningun par"
    print("     esquema IGUAL (%d claves), clases IGUALES, pares IGUALES (%d)."
          % (len(claves_despues), len(pares_despues)))

    print("")
    print("CIFRA adjudicaciones escritas en esta corrida: %d operaciones" % hechas)
    print("CIFRA lineas del registro de citas: %d linea(s)" % len(D))
    print("CIFRA ficheros de codigo tocados: %d fichero(s)" % len(PY_TOCADOS))
    print("")
    print("NADA SE BORRA: los ocho bloques de docstring de modulo se insertan al FINAL")
    print("del docstring, el de la 6.7 al final del docstring de `p3b_caso_positivo`, el")
    print("de la 6.5 DELANTE del cierre del comentario de OP-C-05 (o sea DEBAJO del")
    print("bloque de la vuelta 156, que no se toca), y las tres adiciones del registro se")
    print("CONCATENAN detras del texto viejo de la razon de LD-OPC05-097.")


main()
