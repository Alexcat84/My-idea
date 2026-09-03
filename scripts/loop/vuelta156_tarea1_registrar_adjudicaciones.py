# -*- coding: utf-8 -*-
"""vuelta156_tarea1_registrar_adjudicaciones.py . TAREA 1 DE LA VUELTA 156.

DEJA ESCRITAS EN EL REPO LAS DIEZ ADJUDICACIONES DE LA SECCION 6 DEL ACTA 155,
CADA UNA DONDE VIVE, TODAS POR ADICION Y CON CORRECCION DECLARADA. No borra una
sola linea del texto viejo: cada bloque se ANADE al final del docstring, al
final del comentario o al final del campo, con su fecha, su fuente citada y su
motivo.

EL REPARTO, que es el que el encargo nombra:
  6.1 y 6.2  docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl (el registro de citas) Y
             scripts/loop/vuelta152_registro_de_citas_opc05.py (el instrumento
             que lo lee y donde vive la doctrina de vias y clases)
  6.3 y 6.4  docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl (el registro)
  6.5, 6.6   scripts/loop/vuelta150_3_relectura_expediente.py (el instrumento
  y 6.7      de la relectura del expediente: la P3, la P3b y declara_su_estado)
  6.8        scripts/loop/verificar_apertura_sellada.py (la guarda del corredor)
  6.9        scripts/run_phase1.py (los comentarios de la guarda de OP-C-05)
  6.10       scripts/loop/tallar_estado_de_fase.py

LA ADITIVIDAD SE MIDE, NO SE PROMETE (encargo de la vuelta 156, TAREA 1, y es
lo mismo que se hizo en la 154): para los .py se corre `git diff --numstat` y
se exige BORRADOS 0; para el JSONL se comprueba POR ASSERT que el texto viejo
de cada campo tocado sigue siendo PREFIJO LITERAL del texto nuevo.

ES IDEMPOTENTE: si el bloque ya esta escrito (se busca su marca literal), no lo
duplica y lo dice. Asi se puede re correr sin ensuciar el fichero.

USO:  python scripts/loop/vuelta156_tarea1_registrar_adjudicaciones.py
"""
import io
import json
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")

MARCA = "ADJUDICACION %s DEL ACTA 155"

PY_TOCADOS = [
    "scripts/loop/vuelta152_registro_de_citas_opc05.py",
    "scripts/loop/vuelta150_3_relectura_expediente.py",
    "scripts/loop/verificar_apertura_sellada.py",
    "scripts/run_phase1.py",
    "scripts/loop/tallar_estado_de_fase.py",
]


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)


def insertar_en_docstring(ruta_rel, bloque, marca):
    """Inserta BLOQUE justo antes del cierre del docstring de modulo. El texto
    viejo no se toca: el bloque queda al final, detras de todo lo anterior."""
    ruta = os.path.join(RAIZ, ruta_rel)
    texto = leer(ruta)
    if marca in texto:
        return "YA ESTABA", 0
    ini = texto.index('"""')
    fin = texto.index('"""', ini + 3)
    nuevo = texto[:fin] + bloque + texto[fin:]
    escribir(ruta, nuevo)
    return "ANADIDO", len(bloque.splitlines())


def insertar_antes_de(ruta_rel, ancla, bloque, marca):
    """Inserta BLOQUE justo antes de la linea ANCLA. Para los comentarios de la
    guarda de OP-C-05, que no viven en un docstring sino dentro de la funcion."""
    ruta = os.path.join(RAIZ, ruta_rel)
    texto = leer(ruta)
    if marca in texto:
        return "YA ESTABA", 0
    i = texto.index(ancla)
    nuevo = texto[:i] + bloque + texto[i:]
    escribir(ruta, nuevo)
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
# 6.1 y 6.2, EL INSTRUMENTO QUE LEE EL REGISTRO
# --------------------------------------------------------------------------

B61_DOC = """
--- ADJUDICACION 6.1 DEL ACTA 155 (3 sep 2026): `LD-OPC05-097` VA A RELECTURA
CONJUNTA, Y LA C ESCRITA NO SE SOSTIENE POR SI SOLA ---

REGISTRO POR ADICION. NADA DE LO ESCRITO ARRIBA SE BORRA.

EL CASO DEL AUDITOR, QUE LEYO EL PAR A CIEGAS (sin ver la clase, la via, la
cita ni la razon) Y LLEGO A LA MISMA CLASE A QUE EL EJECUTOR MARCO COMO
DISCUTIBLE, con tres reglas escritas empujando al mismo sitio:
  (i)   el perfil de MADRE E HIJO del 9.6.2 NO se cumple, porque el hijo
        tendria que caber ENTERO DENTRO DE UN PASO de la madre y
        `viaje_diagnostico_remedial` se reparte entre los pasos 2, 3 y 4 de
        `juran_rcca_metodo`;
  (ii)  el 9.6.3 manda pesar LO QUE QUEDA FUERA DEL SOLAPE, y fuera quedan el
        paso 1 de juran (esporadico contra cronico, y el enunciado) y el paso 7
        del viaje (gestionar la resistencia), los dos LINEA por la regla
        practica del informe 67.6, sin procedimiento en ningun lado;
  (iii) con LINEA en los dos sentidos, el SEGUNDO POLO del 9.22 dice que
        REPITEN y prescribe FUSION.

Y LA RAZON ESCRITA SE DELATA SOLA: nombra la diferencia de granularidad y las
dos apostillas, que es la definicion literal del segundo polo, y NO nombra una
sola LINEA DISTINTA EN CADA NODO, que es lo que la C exige.

EL LIMITE, ESCRITO ANTES DE QUE SE CRUCE: si la clase pasa a A, se cambia LA
CLASE con su correccion declarada y el par se registra como CANDIDATO A FUSION.
LA FUSION NO SE EJECUTA en una vuelta de lectura ni sin su ficha, su
superviviente y su ruta.
"""

B62_DOC = """
--- ADJUDICACION 6.2 DEL ACTA 155 (3 sep 2026): PARA REGISTRAR C, LA RAZON
TIENE QUE NOMBRAR LAS DOS LINEAS. DONDE NO PUEDA NOMBRARLAS, LA CLASE ES D ---

CORRECCION DECLARADA POR ADICION, y no es doctrina nueva: es extension citable
del 9.22, que lo dice el mismo en su comprobacion separadora, "LA FIGURA EXIGE
DOS LINEAS DISTINTAS, UNA EN CADA NODO", siendo la C sano CON FIGURA.

LO QUE CAMBIA AL REGISTRAR: una entrada en clase C cuya razon NO pueda nombrar
una linea distinta en cada uno de los dos nodos NO es C. Es D, sano y distinto.
El ejemplar que la obliga es `LD-OPC05-040` (`cost_management_plan` contra
`stakeholder_register`): el dinero y las personas, sin una sola linea de uno
que el otro expanda.

LA FRONTERA, MEDIDA PARA QUE NADIE SE ASUSTE: la guarda de `OP-C-05` de
`scripts/run_phase1.py` mete en `_citados` el campo `par` de TODA linea del
registro, SIN MIRAR LA CLASE, asi que RECLASIFICAR DE C A D NO PONE GATE 0 EN
ROJO. Lo que la clase mueve es la lectura, no la cobertura del registro.
"""

# --------------------------------------------------------------------------
# 6.1, 6.2, 6.3 y 6.4 EN EL REGISTRO, POR ADICION AL CAMPO `razon`
# --------------------------------------------------------------------------

B61_REG = (
    "  [ADJUDICACION 6.1 DEL ACTA 155 (2026-09-03), ANADIDA SIN BORRAR NADA DE "
    "LO ANTERIOR: este par va a RELECTURA CONJUNTA. El auditor lo leyo A CIEGAS "
    "y llego a la misma clase A que el ejecutor marco como discutible, con el "
    "9.6.2 (el hijo no cabe entero dentro de UN paso de la madre: el viaje se "
    "reparte entre los pasos 2, 3 y 4 de juran), el 9.6.3 (fuera del solape "
    "quedan el paso 1 de juran y el paso 7 del viaje, los dos LINEA por la regla "
    "practica del informe 67.6) y el segundo polo del 9.22 (linea en los dos "
    "sentidos: REPITEN, y prescribe fusion). La razon escrita de arriba nombra la "
    "granularidad y las dos apostillas, que es la definicion literal del segundo "
    "polo, y no nombra una sola linea distinta en cada nodo, que es lo que la C "
    "exige. SI LA CLASE PASA A A, EL PAR SE REGISTRA COMO CANDIDATO A FUSION Y "
    "AHI PARA: la fusion no se ejecuta en una vuelta de lectura.]")

B62_REG = (
    "  [ADJUDICACION 6.2 DEL ACTA 155 (2026-09-03), ANADIDA SIN BORRAR NADA DE "
    "LO ANTERIOR: la C del 9.22 es sano CON FIGURA, y la figura EXIGE DOS LINEAS "
    "DISTINTAS, UNA EN CADA NODO. Para registrar C la razon tiene que NOMBRARLAS; "
    "donde no pueda nombrarlas, la clase es D. Esta razon no las nombra: dice el "
    "plan de costos contra el registro de interesados, que son el dinero y las "
    "personas sin una linea de uno que el otro expanda. La relectura por P.5 y su "
    "adjudicacion van en la TAREA 3.b de la vuelta 156.]")

B63_REG = (
    "  [ADJUDICACION 6.3 DEL ACTA 155 (2026-09-03), ANADIDA SIN BORRAR NADA DE "
    "LO ANTERIOR: LA C SE SOSTIENE, Y CON UN MOTIVO MEJOR QUE EL ESCRITO ARRIBA. "
    "No decide el tamano del solape sino EL RESTO (9.6.3): fuera del solape (el "
    "sistema que recolecta, analiza y difunde) cultura_de_seguridad_componentes "
    "conserva la evaluacion de los cuatro subcomponentes, los indicadores y el "
    "escrito de por que invertir, y cultura_de_aprendizaje conserva los procesos "
    "de decision, la medicion de efectividad y la revision periodica "
    "institucionalizada. Procedimiento en los dos lados: sano. La incomodidad con "
    "que se marco venia de pesar el solape en vez del resto.]")

B64_REG = (
    "  [ADJUDICACION 6.4 DEL ACTA 155 (2026-09-03), ANADIDA SIN BORRAR NADA DE "
    "LO ANTERIOR: LA C SE SOSTIENE. El auditor lo leyo a ciegas y dio C, y la "
    "razon escrita arriba SI nombra las dos lineas distintas, una en cada nodo "
    "(el paso 6 de 6S y el paso 4 de error proofing), que es lo que la figura del "
    "9.22 exige. La objecion del residuo de un colapso no la alcanza: el 9.22 "
    "pregunta por LINEAS y no por intenciones, y las dos lineas estan.]")

# --------------------------------------------------------------------------
# 6.5, 6.6 y 6.7, EL INSTRUMENTO DE LA RELECTURA DEL EXPEDIENTE
# --------------------------------------------------------------------------

B65 = """
--- ADJUDICACION 6.5 DEL ACTA 155 (3 sep 2026): "EN LA NOMINA DE LA FICHA" SE
LEE COMO "EL MENSAJE DEL COMMIT NOMBRA EL id_op", Y LA AMBIGUEDAD ERA DEL ACTA ---

REGISTRO POR ADICION, y no cambia una sola linea de codigo: confirma la lectura
con la que la P3 ya corre desde la vuelta 154.

QUE SE PREGUNTO Y QUE SE CONTESTA. La adjudicacion 6.1 del acta 153 escribio
"commits que tocan dataset/, web/ o engine/ EN LA NOMINA DE LA FICHA", y el
ejecutor de la vuelta 154 declaro que lo leia como "el mensaje del commit
nombra el id_op de la ficha", marcandolo como discutible. EL ACTA 155 LO
ADJUDICA A FAVOR DE ESA LECTURA y registra la ambiguedad COMO SUYA: la 6.1
venia a quitar la prueba POR MENCION SOLA, no a redefinir como se atribuye un
commit a una ficha.

LA CONDICION QUE LA P3 YA TENIA Y QUE LA 6.1 NO TOCO sigue siendo la vigente:
`p3_huella_en_git` busca por `git log --grep` con frontera de palabra sobre el
id_op, y ademas exige que el commit toque `RUTAS_NUEVA`. Las dos condiciones,
no una.
"""

B66 = """
--- ADJUDICACION 6.6 DEL ACTA 155 (3 sep 2026): LA P3b SE QUEDA COMO PROXY
DECLARADO, SU RESPALDO ES `verificar_mutaciones_viejas.py`, Y SU HUECO SE
CUENTA ---

REGISTRO POR ADICION. El limite de la P3b que ya esta escrito arriba, en el
docstring de `p3b_caso_positivo`, NO SE BORRA NI SE SUAVIZA: sigue siendo lo
que este instrumento mide.

LO QUE EL ACTA CONCEDE: re correr 71 mutaciones por vuelta no cabe, y el limite
ya iba declarado junto a la funcion, que era la condicion. La P3b se queda.

LO QUE EL ACTA ANADE, Y ES LO QUE CONVIERTE UN PROXY EN UN PROXY CON SU AGUJERO
CONTADO: "cita un artefacto que existe" es mas flojo que el criterio de HECHO
de `docs/plan/08_VERIFICACION.md`, y la casa ya tiene lo que cierra ese hueco.
`scripts/loop/verificar_mutaciones_viejas.py` corre 23 mutaciones, las hace
MORDER (comprueba que caen en rojo) y comprueba que su salida sellada se
repite, y corre CADA VUELTA AL CIERRE. ESE ES EL RESPALDO DECLARADO DE LA P3b.

Y EL HUECO SE NOMBRA EN VEZ DE CALLARSE (banco 9, fallar ruidoso): CUANTAS DE
LAS FICHAS QUE SE APOYAN EN LA P3b CITAN UN CASO POSITIVO QUE LA BATERIA DE 23
NO CUBRE. Se mide en la TAREA 7 de la vuelta 156 y su nomina se publica.
"""

B67 = """
--- ADJUDICACION 6.7 DEL ACTA 155 (3 sep 2026): `declara_su_estado` LEE `nota` Y
`adjudicacion` DEL CORTE, COMO LA P3 ---

CORRECCION DECLARADA POR ADICION. NADA DEL TEXTO ANTERIOR SE BORRA, Y EN
PARTICULAR NO SE BORRA EL BLOQUE DE LA ADJUDICACION 6.2 DEL ACTA 153 (la
asimetria P2 contra P3), del que esta adjudicacion es una EXTENSION y no una
enmienda.

LA PARTICION QUE LA 6.2 DEL ACTA 153 DEJO ESCRITA: lo que mide EXISTENCIA DE UN
CONTROL EN EL CODIGO VIVO lee el arbol de trabajo; lo que mide EJECUCION va
congelado en `--corte`.

DONDE CAE `declara_su_estado`: EN NINGUNA DE LAS DOS. No mide existencia de un
control ni un acto fechado: mide LO QUE LA FICHA DICE DE SI MISMA. Y el dano
esta demostrado al digito por la vuelta 154, que lo marco como su discutible 8:
SUS PROPIAS NOTAS MOVIERON CUATRO FICHAS de "congelado en silencio" a
"congelado declarado" DENTRO DE LA MISMA VUELTA que publicaba la cifra. UNA
CIFRA QUE EL TEXTO DE LA VUELTA MUEVE ES UNA CIFRA QUE MIDE LA VUELTA, NO EL
REPO.

LO QUE CAMBIA: `declara_su_estado` deja de leer la ficha del arbol de trabajo y
pasa a leer `nota` y `adjudicacion` DEL CORTE (`git show <corte>` sobre
docs/plan/OPERACIONES.jsonl), igual que la P3. Una ficha que no existia al
corte no declara nada, porque al corte no habia nada que declarar.

LO QUE ESTO CUESTA, DICHO EN VOZ ALTA: la cifra publicada de congeladas
declaradas y de congeladas en silencio SE MUEVE, y se mueve exactamente por las
notas que la propia vuelta escribe. Por eso va con LA SERIE RE MEDIDA EN LOS DOS
CORTES y la diferencia ATRIBUIDA, como ya se hizo en la vuelta 154 con el 26/22
contra el 30/18.
"""

# --------------------------------------------------------------------------
# 6.8, LA GUARDA DEL CORREDOR
# --------------------------------------------------------------------------

B68 = """
--- ADJUDICACION 6.8 DEL ACTA 155 (3 sep 2026): LA PUERTA SE ESTRECHA A LO QUE
LA 6.7 DEL ACTA 153 CONCEDIO, Y LA VARA SE FIJA ---

CORRECCION DECLARADA POR ADICION. EL BLOQUE DE LA ADJUDICACION 6.7 DEL ACTA 153
QUE ESTA JUSTO ENCIMA NO SE BORRA: describe con exactitud lo que la puerta hizo
entre la vuelta 154 y hoy, y taparlo impediria auditar por que fue mas ancha de
lo concedido.

LAS DOS COSAS QUE EL AUDITOR MIDIO LLAMANDO A LA PROPIA FUNCION DE ESTA GUARDA:
  (i)  LA PUERTA ERA MAS ANCHA QUE LA CONCESION. La 6.7 del acta 153 concedio
       admitir EL COMMIT DE LA DECISION DEL FUNDADOR que el encargo cite por su
       hash. La implementacion admitia CUALQUIER hash que el encargo citara,
       sea de quien sea: medido el 3 sep 2026, los hashes admitidos eran
       `6f695db6` y `c9c6ea40`, LOS DOS COMMITS DEL EJECUTOR. Hoy no hacia dano
       (ninguno cae dentro de un corredor), pero la puerta concedida era otra.
  (ii) LA VARA ESTABA ANCLADA A ALGO QUE SE MUEVE. `hashes_citados_por_el_encargo`
       leia `docs/loop/PROMPT_SIGUIENTE.md` DEL ARBOL DE TRABAJO, asi que el
       veredicto del corredor de una vuelta YA JUZGADA podia cambiar cuando se
       escribiera un encargo posterior. Es LA MISMA ESPECIE que las caidas 5 y 6
       que el ejecutor declaro en la vuelta 154, una vara anclada a algo que se
       mueve, viviendo dentro de una guarda escrita en esa misma vuelta.

LO QUE SE ADJUDICA, Y NO ES DOCTRINA NUEVA (es la letra de la 6.7 mas la vara
que el propio ejecutor ya se aplico a si mismo):
  (a) SOLO ENTRA LO MARCADO. El encargo declara sus hashes admitidos con un
      LITERAL EXPLICITO, y la guarda admite unicamente los marcados. Un hash
      citado de paso NO entra. La cabecera del encargo de la vuelta 156 ya trae
      el literal, y dice NINGUNO.
  (b) LA VARA SE FIJA. El encargo se lee DEL COMMIT DEL ACTA de la vuelta que se
      comprueba (`git show` del acta sobre docs/loop/PROMPT_SIGUIENTE.md), no
      del arbol de trabajo. El acta ya se localiza aqui con `commit_acta`, asi
      que la vara es la misma que la guarda ya usa para todo lo demas.
  (c) LA GUARDA LOS SIGUE NOMBRANDO APARTE, nunca en silencio.
  (d) EL ROJO POR UN COMMIT DEL PROPIO EJECUTOR DENTRO DEL CORREDOR SE QUEDA
      INTACTO. Esa mitad no se toca.
"""

# --------------------------------------------------------------------------
# 6.9, LOS COMENTARIOS DE LA GUARDA DE OP-C-05
# --------------------------------------------------------------------------

ANCLA_69 = "    # ── FIN OP-C-05 ─"

B69 = """    # CORRECCION DECLARADA POR ADICION (2026-09-03, vuelta 156, TAREA 1,
    # ADJUDICACION 6.9 DEL ACTA 155). NADA DE LOS COMENTARIOS DE ARRIBA SE
    # BORRA: siguen describiendo con exactitud lo que esta guarda mira y lo que
    # deja fuera.
    #
    # LA PREGUNTA QUE SE CONTESTA (pregunta 4 de la vuelta 154): si los TRES
    # pares que solo existen admitiendo como declarante a un nodo DEPRECADO
    # habia que leerlos y meterlos en el registro.
    #
    # LA ADJUDICACION: NO SE LEEN. Quedan fuera por la DECISION DEL FUNDADOR DEL
    # 14 AGO 2026, CAMINO A, que no es del bucle para revocarla, y leerlos
    # meteria en el registro veredictos de pares que la vara declarada no mira.
    # SE QUEDAN FUERA Y SE QUEDAN NOMBRADOS AQUI DENTRO, que es lo minimo que el
    # banco 9 pide, y SU CUENTA SE PUBLICA CADA VEZ QUE ESTA GUARDA HABLE: no
    # solo en este comentario, sino en la linea de detalle del check, para que
    # el universo que la vara deja fuera no sea nunca invisible desde la salida.
    # Los tres pares son los ya nombrados arriba, y la cuenta es 157 menos 154.
    #
    # COMO SE CUENTA, Y SE COMPUTA, NO SE TECLEA: el mismo recorrido de arriba
    # pero SIN exigir que el nodo de partida este vivo (vara 4 de la tabla del
    # acta 153, seccion 4.1, medida en la vuelta 154 con
    # scripts/loop/vuelta154_tarea2a_universo_bidireccionales.py). Los dos
    # EXTREMOS siguen teniendo que resolver a nodos VIVOS: lo unico que se
    # afloja para contar el hueco es QUIEN declara la arista.
"""

# --------------------------------------------------------------------------
# 6.10, EL TALLADOR DEL ESTADO DE FASE
# --------------------------------------------------------------------------

B610 = """
--- ADJUDICACION 6.10 DEL ACTA 155 (3 sep 2026): UN `--fase` QUE NO CALCE
EXACTAMENTE ES ROJO Y EXIT DISTINTO DE CERO ---

CORRECCION DECLARADA POR ADICION. NADA DEL TEXTO ANTERIOR SE BORRA.

EL HALLAZGO, MEDIDO POR EL AUDITOR EL 3 SEP 2026 Y SIN TUBERIA (la tuberia fue
su propia caida 2 y la declara): `--fase 06_MESAS` daba 16 del catalogo, 16
cumplidas, 0 sin cumplir y EXIT 0; `--fase 06` daba 11 DEL CATALOGO, 11
cumplidas, 0 sin cumplir, EXIT 0 Y NI UNA QUEJA (cero propias, once recogidas
por remision, porque `leer_remisiones` recorta el nombre de fase a su NUMERO y
ese numero si casa). EL CATALOGO COMPLETAMENTE VACIO SI ESTABA CAZADO
(`--fase NO_EXISTE`: ROJO y EXIT 1, por el fallo de `medir`); EL CATALOGO
PARCIAL POR UN NOMBRE QUE NO EXISTE, NO.

POR QUE IMPORTA Y NO ES TEORICO: es UN VERDE SOBRE UN UNIVERSO INCOMPLETO, la
misma especie exacta del hallazgo de OP-C-05 del acta 153. Y este instrumento
es el que midio el disparador que movio cinco fichas a HECHA, el que mide la
celda de la fila 03 de la tabla por fase y el muro de la fase 08, y es contra
el que `scripts/loop/verificar_cifras_del_reporte.py` coteja las afirmaciones
de cierre del reporte.

LO QUE SE ADJUDICA, POR EXTENSION DEL BANCO 9 (FALLAR RUIDOSO) Y SIN DOCTRINA
NUEVA: es la misma regla que ya caza el catalogo vacio, aplicada al catalogo
MUTILADO. `--fase X` donde X no sea EXACTAMENTE uno de los nombres de fase que
`docs/plan/OPERACIONES.jsonl` trae es ROJO Y EXIT DISTINTO DE CERO, con la
nomina de los nombres validos impresa al lado para que el rojo se pueda
arreglar sin adivinar.
"""


def main():
    print("=" * 78)
    print("VUELTA 156, TAREA 1: LAS DIEZ ADJUDICACIONES DE LA SECCION 6 DEL ACTA 155,")
    print("ESCRITAS DONDE CADA UNA VIVE, TODAS POR ADICION.")
    print("=" * 78)
    print("")

    hechas = 0
    print("A) LOS CINCO FICHEROS .py")
    docs = [
        ("6.1", "scripts/loop/vuelta152_registro_de_citas_opc05.py", B61_DOC),
        ("6.2", "scripts/loop/vuelta152_registro_de_citas_opc05.py", B62_DOC),
        ("6.5", "scripts/loop/vuelta150_3_relectura_expediente.py", B65),
        ("6.6", "scripts/loop/vuelta150_3_relectura_expediente.py", B66),
        ("6.7", "scripts/loop/vuelta150_3_relectura_expediente.py", B67),
        ("6.8", "scripts/loop/verificar_apertura_sellada.py", B68),
        ("6.10", "scripts/loop/tallar_estado_de_fase.py", B610),
    ]
    for num, ruta, bloque in docs:
        estado, n = insertar_en_docstring(ruta, bloque, MARCA % num)
        print("  %-4s %-56s %s (%d lineas)" % (num, ruta, estado, n))
        if estado == "ANADIDO":
            hechas += 1
    estado, n = insertar_antes_de("scripts/run_phase1.py", ANCLA_69, B69, MARCA % "6.9")
    print("  %-4s %-56s %s (%d lineas)" % ("6.9", "scripts/run_phase1.py", estado, n))
    if estado == "ANADIDO":
        hechas += 1

    print("")
    print("B) EL REGISTRO DE CITAS, POR ADICION AL CAMPO `razon`")
    E = entradas()
    antes = {e["cita"].split(",")[0]: e["razon"] for e in E}
    reparto = {
        "LD-OPC05-097": ("6.1", B61_REG),
        "LD-OPC05-040": ("6.2", B62_REG),
        "LD-OPC05-046": ("6.3", B63_REG),
        "LD-OPC05-122": ("6.4", B64_REG),
    }
    for e in E:
        ld = e["cita"].split(",")[0]
        if ld in reparto:
            num, bloque = reparto[ld]
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
    print("     BORRADOS TOTALES EN LOS CINCO .py: %d" % total_borrados)

    print("")
    print("C.2) EL JSONL, POR ASSERT DE PREFIJO LITERAL sobre el campo `razon`:")
    D = entradas()
    assert len(D) == len(E), "el numero de lineas del registro se movio"
    comprobados = 0
    for d in D:
        ld = d["cita"].split(",")[0]
        viejo = antes[ld]
        assert d["razon"].startswith(viejo), (
            "%s: el texto viejo de `razon` YA NO ES PREFIJO del nuevo" % ld)
        comprobados += 1
    print("     %d entrada(s) del registro comprobadas: el texto viejo de `razon` sigue" % comprobados)
    print("     siendo PREFIJO LITERAL del nuevo en TODAS, no solo en las cuatro tocadas.")
    tocadas = sum(1 for d in D if d["cita"].split(",")[0] in reparto
                  and len(d["razon"]) > len(antes[d["cita"].split(",")[0]]))
    print("     entradas cuyo `razon` CRECIO: %d" % tocadas)

    claves_antes = sorted({k for e in E for k in e})
    claves_despues = sorted({k for d in D for k in d})
    assert claves_antes == claves_despues, "el esquema del registro se movio"
    clases_antes = [e["clase"] for e in E]
    clases_despues = [d["clase"] for d in D]
    assert clases_antes == clases_despues, "esta tarea NO mueve ninguna clase"
    pares_antes = {tuple(sorted(e["par"])) for e in E}
    pares_despues = {tuple(sorted(d["par"])) for d in D}
    assert pares_antes == pares_despues, "esta tarea NO mueve ningun par"
    print("     esquema IGUAL (%d claves), clases IGUALES, pares IGUALES (%d)."
          % (len(claves_despues), len(pares_despues)))

    print("")
    print("CIFRA adjudicaciones escritas: %d operaciones" % hechas)
    print("CIFRA lineas del registro de citas: %d linea(s)" % len(D))
    print("CIFRA ficheros de codigo tocados: %d fichero(s)" % len(PY_TOCADOS))
    print("")
    print("NADA SE BORRA: los siete bloques de docstring se insertan al FINAL del")
    print("docstring, el bloque de la 6.9 se inserta DELANTE del cierre del comentario")
    print("de OP-C-05, y las cuatro razones se CONCATENAN detras del texto viejo.")


main()
