# -*- coding: utf-8 -*-
"""vuelta150_3_relectura_expediente.py . LA RELECTURA AL DOBLE DEL TRAMO DEL
EXPEDIENTE (TAREA 3 de la vuelta 150), encargada por el acta 149 seccion 5 al
amparo de AUDITOR.md 1.2.

RECORRE LAS 71 FICHAS DE docs/plan/OPERACIONES.jsonl y coteja el campo `estado`
contra LO QUE EL REPO DICE QUE SE EJECUTO. Publica la tabla de las que NO CALZAN
y CERO de las que si: la tabla corta es la que se lee.

EL CRITERIO (TAREA 3.b), DECLARADO AQUI Y MEDIBLE CONTRA EL REPO, NUNCA CONTRA
UN ACTA. Una operacion cuenta como EJECUTADA si al menos una de estas tres
pruebas da positivo, y SIEMPRE se dice cual:

  (P1) VARA DE GRAFO. `scripts/loop/tallar_estado_de_fase.py` dice DESTINO
       CUMPLIDO para esa operacion. Es la unica de las tres que mira el DATO.
       Fuente escrita: acta 139, TAREA 2.a, y sus afinados de las vueltas 141 y
       142. No se reimplementa aqui: se invoca el instrumento y se lee su
       tabla, que es lo contrario de tener dos varas divergentes.

  (P2) VARA DE CODIGO, MITAD DE PRESENCIA. El `id_op` aparece hoy en el codigo
       vivo (`scripts/`, `engine/`, `web/lib/`), excluyendo `scripts/loop/`, que
       es el cuaderno del bucle y no el producto. Fuente escrita: adjudicacion
       3.9 del acta 144, "una operacion que no deja huella en el grafo... se
       mide contra LO QUE INSTALA, y para un control eso significa dos cosas y
       solo dos: que el control EXISTA en el codigo y que MUERDA por mutacion".
       AQUI SE MIDE SOLO LA PRIMERA MITAD Y SE DICE: la segunda (que muerda) se
       prueba por mutacion una a una y no se puede barrer para 71 fichas en una
       vuelta. Una P2 sola NO es prueba de que el control funcione; es prueba de
       que esta instalado.

  (P3) HUELLA EN GIT. Existe al menos un commit de la rama activa cuyo MENSAJE
       nombra el `id_op` Y que ademas toca `dataset/`, `scripts/`, `engine/` o
       `web/`. La segunda condicion es la que separa una EJECUCION de un
       REGISTRO: un commit que solo mueve `docs/` esta anotando el plan, no
       corriendolo. Es el registro que el repo lleva de si mismo, leido con
       `git log`, no una memoria.

NO CALZA cuando:
  - `estado` dice `LISTA` y alguna prueba dice ejecutada, SIN que la ficha
    declare por que sigue congelada; o
  - `estado` dice `HECHA` y NINGUNA prueba dice ejecutada.

UN ESTADO CONGELADO A PROPOSITO ES LEGITIMO SI LO DICE (acta 149, 4.2). Aqui se
mide si lo dice: se busca en el campo `nota` o `adjudicacion` de la propia ficha
una mencion explicita a su `estado`. Si la trae, la fila sale como CONGELADO
DECLARADO y no como incumplimiento; si no la trae, sale como CONGELADO EN
SILENCIO, que es exactamente la caida 4.2 del acta 149.

TAREA 3.c: al final lista las operaciones DESBLOQUEADAS, o sea con `estado`
LISTA y TODAS sus `depende_de` en `HECHA`, con su `depende_de` medido al lado.

CORRECCION DECLARADA (2026-09-02, vuelta 152, TAREA 1; hallazgo del acta 151,
seccion de hallazgos fuera de lo marcado. NADA DEL TEXTO ANTERIOR SE BORRA,
estas lineas se anaden). LA P3 SE CONTABA A SI MISMA: pedia "un commit que
NOMBRA el id_op y ademas toca dataset/, scripts/, engine/ o web/", y el commit
con el que la PROPIA VUELTA publica que una ficha no tiene prueba de ejecucion
nombra esa ficha y toca scripts/, asi que el papeleo de la vuelta se convertia
en la prueba del trabajo de la vuelta. Medido por el auditor: las dos fichas
que la vuelta 150 declaro SIN NINGUNA PRUEBA (OP-V-01 y OP-L-01) tenian una al
dia siguiente, y era el commit que dijo que no la tenian.

LA REPARACION: EL RELOJ DE GIT SE CONGELA. `git log` va cortado en `--corte`,
que es OBLIGATORIO y que por regla es EL HEAD DE APERTURA DE LA VUELTA, o sea
el commit anterior al primero que la vuelta escribe. Y no basta con congelar:
una GUARDA compara dos conjuntos COMPUTADOS, los commits que la P3 cuenta y los
commits del rango `--apertura`..HEAD, y CAE si se cruzan. Su prueba de mutacion
esta en scripts/loop/_v152_tarea1_mutacion_reloj.py.

USO:
  python scripts/loop/vuelta150_3_relectura_expediente.py --corte <REF> [--apertura <REF>]

  --corte     ref donde se para el reloj de git. Obligatorio: sin el la vara
              vuelve a contarse a si misma, y una vara que se cuenta a si misma
              en silencio es peor que una que no corre.
  --apertura  HEAD de apertura de la vuelta, que define el rango prohibido para
              la guarda. Por defecto, el mismo valor de --corte.

--- ADJUDICACION 6.1 DEL ACTA 153 (2 sep 2026): LA P3 DEJA DE CONTAR MENCIONES ---

CORRECCION DECLARADA. NADA DE LO ESCRITO ARRIBA SE BORRA: este bloque se anade
debajo y describe lo que cambia a partir de hoy.

LA VARA YA EXISTIA Y NO ES DOCTRINA NUEVA. Es el CRITERIO DE HECHO de
docs/plan/08_VERIFICACION.md: "UNA FASE ESTA HECHA CUANDO SU VERIFICACION SE
CAERIA SI EL FALLO VOLVIERA. No cuando pasa verde: cuando se CAERIA." Un commit
que NOMBRA una operacion no hace que ninguna verificacion se caiga.

LO QUE CAMBIA: la P3 pasa a contar SOLO commits que tocan `dataset/`, `web/` o
`engine/`. `scripts/` SALE de la lista de rutas. El ejemplar que lo obliga, y es
el que el acta manda usar como caso de mutacion: `c9c6ea40` (el commit que
publica que OP-V-01 y OP-L-01 NO tienen prueba) toca `docs/loop/` y
`scripts/loop/`, y con la vara vieja contaba como PRUEBA DE EJECUCION de esas
dos fichas por la sola ruta `scripts/`. Con la vara nueva deja de contar.

Y LA SEGUNDA VIA, escrita porque la adjudicacion la nombra: tambien cuenta "el
caso positivo de la ficha corriendo en rojo antes y en verde despues". Esa via
se mide aqui como P3b y su alcance esta declarado junto a la funcion que la
implementa: NO se re corre un caso positivo por ficha en cada corrida (serian 71
mutaciones por vuelta), se exige que la ficha CITE una salida de caso positivo o
de mutacion que EXISTA en el arbol del corte.

LO QUE ESTA LECTURA SUPONE Y SE DECLARA EN VEZ DE CALLARSE: la adjudicacion dice
"commits que tocan dataset/, web/ o engine/ EN LA NOMINA DE LA FICHA". Se lee
"la nomina de la ficha" como "el mensaje del commit nombra el id_op de la
ficha", que es la condicion que la P3 ya tenia y que la adjudicacion no toca.
Queda marcado como discutible en el reporte de la vuelta 154.

--- ADJUDICACION 6.2 DEL ACTA 153 (2 sep 2026): LA ASIMETRIA P2 CONTRA P3 SE
QUEDA, Y SE ESCRIBE AQUI DENTRO PORQUE LA ADJUDICACION LO EXIGE ---

CORRECCION DECLARADA POR ADICION. La condicion literal del acta es que la
asimetria quede escrita DENTRO DEL INSTRUMENTO y no solo en el reporte, "para
que la lea quien venga detras". Esta es esa escritura.

LA ASIMETRIA: la P3 corre con el reloj de git CONGELADO en `--corte`, y la P2
NO se congela: lee el ARBOL DE TRABAJO de hoy.

POR QUE NO ES UNA INCOHERENCIA:
  - La P2 mide EXISTENCIA de un control en el codigo vivo. Existencia es un
    ESTADO, no una ejecucion, y el estado de hoy se mide en el arbol de hoy. Un
    control instalado hoy esta instalado, lo instalara quien lo instalara y el
    dia que fuera.
  - La P3 mide EJECUCION, o sea un ACTO fechado. Un acto que la propia vuelta
    acaba de cometer no puede ser la prueba de que la vuelta hizo el trabajo:
    ahi es donde la vara se cuenta a si misma, y por eso solo esta va congelada.

LO QUE LA ASIMETRIA CUESTA, DICHO EN VOZ ALTA: si la propia vuelta INSTALA el
id_op en `scripts/`, `engine/` o `web/lib/`, la P2 lo vera en la misma corrida.
Eso NO es la caida que el acta 151 hallo (aquella era la P3 comiendose su propio
papeleo), pero es su vecina, y por eso se nombra aqui en vez de esconderse.

--- ADJUDICACION 6.5 DEL ACTA 153 (2 sep 2026): EL CORTE ES EL HEAD DE APERTURA,
EN ESTRICTO ---

CORRECCION DECLARADA POR ADICION, y la caida es del auditor, no de este
instrumento. El acta 151 congelo el reloj en `c9c6ea40~1` (`fb3c0c75`), que cae
DENTRO de la vuelta 150; la regla escrita en el bloque de arriba pide EL HEAD DE
APERTURA DE LA VUELTA, o sea el commit anterior al primero que la vuelta
escribe, que para la 150 era `fe98cf97`. El acta 153, seccion 2, tercer parrafo,
se lo concede entero al ejecutor y lo registra como caida de vara DEL AUDITOR.

NO CAMBIO UN DIGITO en aquella medicion (los dos cortes dan 58/13/30/67), pero
la vara laxa no se hereda: `--corte` es el HEAD DE APERTURA y no un ancestro
cualquiera cercano.

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
import argparse
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
FASES = ["00_CODIGO", "01_FUENTES", "02_DESTEJIDOS", "03_FUSIONES", "04_ENLACES",
         "05_SANEO", "06_MESAS", "07_ADUANA", "08_VERIFICACION",
         "09_LECTURAS_DIRIGIDAS", "10_INVENTARIO"]


def fichas():
    return [json.loads(x) for x in io.open(OPS, encoding="utf-8").read().splitlines() if x.strip()]


def p1_vara_de_grafo():
    """Invoca tallar_estado_de_fase.py para cada fase y lee su tabla. Devuelve
    {id_op: (veredicto, fase_en_que_salio)}."""
    out = {}
    for fase in FASES:
        r = subprocess.run(["python", os.path.join("scripts", "loop", "tallar_estado_de_fase.py"),
                            "--fase", fase], capture_output=True, cwd=RAIZ)
        texto = r.stdout.decode("utf-8", "replace")
        for linea in texto.splitlines():
            if not linea.strip().startswith("|"):
                continue
            celdas = [c.strip().strip("`*") for c in linea.strip().strip("|").split("|")]
            if not celdas or not re.match(r"^OP-[A-Z]+-\d", celdas[0]):
                continue
            idop = celdas[0]
            cumplido = "CUMPLIDO" in linea.upper() and "NO CUMPLIDO" not in linea.upper()
            if idop not in out or cumplido:
                out[idop] = (cumplido, fase, linea.strip())
    return out


def p2_vara_de_codigo(ids):
    """El id_op aparece en el codigo vivo. scripts/loop/ queda FUERA: es el
    cuaderno del bucle, no el producto."""
    hits = {i: [] for i in ids}
    for base in ("scripts", "engine", os.path.join("web", "lib")):
        raiz = os.path.join(RAIZ, base)
        for dirpath, dirnames, filenames in os.walk(raiz):
            dirnames[:] = [d for d in dirnames
                           if d not in ("__pycache__", "node_modules", "loop")]
            for nombre in filenames:
                if not nombre.endswith((".py", ".ts", ".tsx", ".js", ".json")):
                    continue
                ruta = os.path.join(dirpath, nombre)
                try:
                    texto = io.open(ruta, encoding="utf-8", errors="replace").read()
                except OSError:
                    continue
                for i in ids:
                    # FRONTERA DE PALABRA, y no es cosmetica: `OP-M-01` es
                    # PREFIJO LITERAL de `OP-M-01-FUSION` y de
                    # `OP-M-01-ESLABONES`, asi que un `in` crudo le regalaria a
                    # la madre la huella de sus hijas. Se exige que detras del
                    # id no venga otro segmento del mismo id.
                    if re.search(re.escape(i) + r"(?![A-Za-z0-9_-])", texto):
                        hits[i].append(os.path.relpath(ruta, RAIZ).replace("\\", "/"))
    return hits


# --- LAS DOS NOMINAS DE RUTAS DE LA P3 (vuelta 154, TAREA 4.a) ---
# RUTAS_NUEVA es la vara vigente desde la adjudicacion 6.1 del acta 153.
# RUTAS_VIEJA se conserva ENTERA y no por nostalgia: es la unica forma de
# ENSENAR LAS DOS SALIDAS sobre el mismo corte, que es lo que el encargo pide
# como caso de mutacion. Una vara vieja borrada no se puede contrastar.
RUTAS_VIEJA = ("dataset/", "scripts/", "engine/", "web/")
RUTAS_NUEVA = ("dataset/", "web/", "engine/")

# Palabras RESERVADAS para las salidas de caso positivo y de mutacion. La
# convencion no se inventa aqui: `verificar_apertura_sellada.py` ya declara
# `MUTACION` como palabra reservada de las salidas de prueba, "por convencion
# desde esta vuelta en adelante" (vuelta 102).
PATRON_CASO_POSITIVO = re.compile(
    r"SALIDA_V\d+_[A-Za-z0-9_]*(?:MUTACION|CASO_POSITIVO)[A-Za-z0-9_]*\.txt")


def p3b_caso_positivo(F, corte):
    """LA SEGUNDA VIA DE LA P3 (adjudicacion 6.1 del acta 153): "o el caso
    positivo de la ficha corriendo en rojo antes y en verde despues".

    QUE SE MIDE, Y QUE NO. NO se re corre un caso positivo por ficha en cada
    corrida: serian 71 mutaciones por vuelta y ninguna vuelta cabria. Se mide
    que la ficha CITE una salida de caso positivo o de mutacion Y que esa salida
    EXISTA EN EL ARBOL DEL CORTE (`git ls-tree`, no el arbol de trabajo, por la
    misma razon que la P3a va congelada).

    EL LIMITE SE DECLARA EN VEZ DE CALLARSE: esto prueba que el artefacto de la
    prueba EXISTE al corte, no que la prueba se haya vuelto a correr hoy. Es una
    prueba mas debil que correr la mutacion, y por eso se dice SIEMPRE cual de
    las dos vias sostiene cada fila (P3a o P3b) en vez de fundirlas en una.

    --- EL HUECO DE ESTE PROXY, CONTADO Y NOMBRADO (vuelta 156, TAREA 7,
    adjudicacion 6.6 del acta 155) ---

    REGISTRO POR ADICION. Nada de lo de arriba se borra ni se suaviza.

    LO QUE EL ACTA CONCEDE: la P3b se queda como proxy declarado, porque re
    correr 71 mutaciones por vuelta no cabe y el limite ya iba escrito aqui.
    LO QUE EL ACTA MANDA: nombrar el hueco, para que un proxy sea un proxy CON SU
    AGUJERO CONTADO. El respaldo que el acta nombra es
    `scripts/loop/verificar_mutaciones_viejas.py`, que corre su bateria cada
    vuelta al cierre, la hace MORDER y comprueba que su salida sellada se repite.

    EL HUECO, MEDIDO EL 3 SEP 2026 CON
    `scripts/loop/vuelta156_tarea7_hueco_p3b.py` (salida
    `docs/loop/SALIDA_V156_T7_HUECO_P3B.txt`), Y SALE PEOR DE LO QUE LA
    ADJUDICACION SUPONIA. De las 71 fichas del expediente, SOLO CUATRO se apoyan
    en la P3b, y LAS CUATRO CITAN ARTEFACTOS QUE LA BATERIA NO RE CORRE: la
    interseccion entre las 9 salidas citadas y los 23 scripts de la bateria es
    VACIA.

      OP-C-05   SALIDA_V154_T2D_MUTACION.txt
      OP-E-03   SALIDA_V96_TAREA3_MUTACION.txt, SALIDA_V97_TAREA2_MUTACION.txt,
                SALIDA_V98_TAREA4_MUTACION.txt, SALIDA_V99_TAREA3_MUTACION.txt,
                SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt
      OP-E-07   SALIDA_V93_TAREA3_MUTACION.txt, SALIDA_V94_TAREA2B_MUTACION.txt
      OP-S-11   SALIDA_V136_3D_MUTACION.txt

    POR QUE PASA, Y NO ES UN FALLO DE LA BATERIA: la bateria vigila LAS GUARDAS
    DEL BUCLE (talladores, guardas de cifras, arneses), que es para lo que nacio;
    las citas de la P3b son mutaciones DE OPERACIONES DEL PLAN. Son dos universos
    distintos y hasta hoy nadie los habia cruzado.

    LO QUE ESTO SIGNIFICA, SIN ADORNO: para esas cuatro fichas la P3b sostiene
    que la prueba EXISTE, y nadie la vuelve a correr. La bateria NO es hoy su
    respaldo efectivo, por mucho que corra cada vuelta. LA CIFRA DEL AGUJERO ES
    4 DE 4, y queda escrita aqui para que el que venga detras no tenga que
    volver a medirla para saber que existe.

    LO QUE ESTA VUELTA NO HACE, Y SE DICE: NO mete esas nueve salidas en la
    bateria. Meterlas es una decision de tamano y de coste por vuelta que no es
    del ejecutor, y va al reporte como pregunta."""
    # --- ADJUDICACION 6.7 DEL ACTA 157 (3 sep 2026): MIENTRAS LAS NUEVE
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
    r = subprocess.run(["git", "ls-tree", "-r", "--name-only", corte, "docs/loop/"],
                       capture_output=True, cwd=RAIZ)
    en_el_corte = {x.strip().split("/")[-1] for x in r.stdout.decode("utf-8", "replace").splitlines()
                   if x.strip()}
    out = {}
    for f in F:
        partes = []
        for k in ("verificacion", "evidencia"):
            v = f.get(k)
            partes += v if isinstance(v, list) else [str(v or "")]
        for k in ("nota", "adjudicacion"):
            partes.append(str(f.get(k) or ""))
        citadas = sorted(set(PATRON_CASO_POSITIVO.findall(" ".join(partes))))
        out[f["id_op"]] = [c for c in citadas if c in en_el_corte]
    return out


def p3_huella_en_git(ids, corte, rutas=RUTAS_NUEVA):
    """Commits de la rama activa cuyo mensaje nombra el id_op Y que tocan las
    rutas de `rutas`.

    CON EL RELOJ PARADO EN `corte` (correccion declarada de la vuelta 152): el
    `git log` no ve un solo commit posterior, asi que ningun commit de la propia
    vuelta puede servirle de prueba a la propia vuelta.

    CORRECCION DECLARADA (2026-09-02, vuelta 154, TAREA 4.a, adjudicacion 6.1
    del acta 153; la firma vieja no se borra, se conserva bajo `RUTAS_VIEJA`):
    ~~dataset/, scripts/, engine/ o web/~~ pasa a dataset/, web/ o engine/.
    `scripts/` SALE. Un commit que NOMBRA una operacion y solo mueve el cuaderno
    del bucle no hace que ninguna verificacion se caiga, y el criterio de HECHO
    de docs/plan/08_VERIFICACION.md dice que eso es justo lo que separa una
    ejecucion de un registro."""
    hits = {}
    for i in ids:
        # MISMA FRONTERA DE PALABRA que en P2, por el mismo motivo: sin ella
        # `OP-M-01` heredaria los commits de `OP-M-01-FUSION`.
        r = subprocess.run(["git", "log", corte, "--format=%H", "-E", "--grep",
                            re.escape(i) + "([^A-Za-z0-9_-]|$)"], capture_output=True, cwd=RAIZ)
        commits = [c for c in r.stdout.decode().split() if c]
        con_codigo = []
        for c in commits:
            n = subprocess.run(["git", "show", "--name-only", "--format=", c],
                               capture_output=True, cwd=RAIZ).stdout.decode("utf-8", "replace")
            tocadas = [x for x in n.splitlines() if x.strip()]
            if any(x.startswith(rutas) for x in tocadas):
                con_codigo.append(c[:8])
        hits[i] = (len(commits), con_codigo)
    return hits


def guarda_reloj_congelado(v3, apertura):
    """LA GUARDA DEL RELOJ. Compara DOS CONJUNTOS COMPUTADOS y no una constante:

      `contados`  los commits que la P3 esta usando como prueba, sacados de su
                  propia salida.
      `propios`   los commits del rango `apertura`..HEAD, o sea LOS QUE LA
                  PROPIA VUELTA HA ESCRITO, sacados de git rev-list.

    Si se cruzan, la vara se esta contando a si misma y la guarda CAE. Los dos
    lados se calculan en esta corrida: no hay un literal esperado que comparar
    consigo mismo (EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION)."""
    r = subprocess.run(["git", "rev-list", "%s..HEAD" % apertura],
                       capture_output=True, cwd=RAIZ)
    propios = {c[:8] for c in r.stdout.decode().split() if c}
    contados = set()
    for i in v3:
        contados.update(v3[i][1])
    intrusos = sorted(contados & propios)
    return propios, contados, intrusos


MARCAS_DE_DECLARACION = ("ESTADO", "DIFERIDA", "CONGELAD", "SIGUE EN LISTA", "NO SE MUEVE")


def declara_su_estado(f):
    """La ficha dice algo explicito sobre su propio campo estado.

    --- ESTA FIRMA QUEDA SUSTITUIDA COMO VARA VIGENTE (vuelta 156, TAREA 6,
    adjudicacion 6.7 del acta 155). NO SE BORRA: se conserva entera porque es la
    unica forma de MEDIR LA SERIE EN LOS DOS CORTES y atribuir la diferencia, que
    es justo lo que la adjudicacion exige. Se llega a ella con --declara-arbol. ---

    LO QUE HACIA MAL, DEMOSTRADO AL DIGITO POR LA VUELTA 154 (su discutible 8):
    lee la ficha DEL ARBOL DE TRABAJO, asi que las notas que la PROPIA VUELTA
    escribe mueven la cifra que la propia vuelta publica. En la 154 fueron CUATRO
    fichas que pasaron de "congelado en silencio" a "congelado declarado" dentro
    de la misma corrida. UNA CIFRA QUE EL TEXTO DE LA VUELTA MUEVE ES UNA CIFRA
    QUE MIDE LA VUELTA, NO EL REPO."""
    texto = " ".join(str(f.get(k) or "") for k in ("nota", "adjudicacion"))
    t = texto.upper()
    for marca in MARCAS_DE_DECLARACION:
        if marca in t:
            return True, marca
    return False, None


def fichas_del_corte(corte):
    """`docs/plan/OPERACIONES.jsonl` TAL COMO ESTABA EN `--corte`, indexado por
    id_op. Es `git show <corte>:...`, la misma mecanica con que la P3 congela su
    reloj (adjudicacion 6.7 del acta 155)."""
    r = subprocess.run(["git", "show", "%s:docs/plan/OPERACIONES.jsonl" % corte],
                       capture_output=True, cwd=RAIZ)
    if r.returncode != 0:
        raise SystemExit("ROJO: no se pudo leer OPERACIONES.jsonl en el corte %s" % corte)
    texto = r.stdout.decode("utf-8", "replace")
    out = {}
    for linea in texto.splitlines():
        if linea.strip():
            d = json.loads(linea)
            out[d["id_op"]] = d
    return out


def declara_su_estado_del_corte(f, en_el_corte):
    """LA VARA VIGENTE DESDE LA VUELTA 156 (adjudicacion 6.7 del acta 155):
    `nota` y `adjudicacion` SE LEEN DEL CORTE, como la P3.

    UNA FICHA QUE NO EXISTIA AL CORTE NO DECLARA NADA, y es lo correcto: al corte
    no habia nada que declarar. Se devuelve la marca NO EXISTIA AL CORTE para que
    ese caso se vea en la salida en vez de confundirse con un silencio.

    LA ASIMETRIA CON LA P2 SIGUE VALIENDO Y SIGUE ESCRITA ARRIBA (adjudicacion 6.2
    del acta 153): la P2 mide EXISTENCIA de un control en el codigo vivo y lee el
    arbol; esto mide LO QUE LA FICHA DICE DE SI MISMA, que no es existencia de un
    control sino texto de la vuelta, y por eso va congelado."""
    d = en_el_corte.get(f["id_op"])
    if d is None:
        return False, "NO EXISTIA AL CORTE"
    return declara_su_estado(d)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corte", required=True)
    ap.add_argument("--apertura", default=None)
    ap.add_argument("--declara-arbol", action="store_true",
                    help="lee `nota` y `adjudicacion` del ARBOL DE TRABAJO para decidir si "
                         "una ficha declara su estado, o sea la vara ANTERIOR a la "
                         "adjudicacion 6.7 del acta 155. Solo para el contraste de la "
                         "vuelta 156: NO es la vara vigente.")
    ap.add_argument("--vara-vieja", action="store_true",
                    help="corre la P3 con la nomina de rutas ANTERIOR a la adjudicacion "
                         "6.1 del acta 153 (con scripts/ dentro). Solo para el contraste "
                         "de la vuelta 154: NO es la vara vigente.")
    args = ap.parse_args()
    corte = args.corte
    apertura = args.apertura or corte
    rutas = RUTAS_VIEJA if args.vara_vieja else RUTAS_NUEVA
    corte_h = subprocess.run(["git", "rev-parse", "--short=8", corte],
                             capture_output=True, cwd=RAIZ).stdout.decode().strip()
    apertura_h = subprocess.run(["git", "rev-parse", "--short=8", apertura],
                                capture_output=True, cwd=RAIZ).stdout.decode().strip()
    print("RELOJ DE GIT CONGELADO EN --corte %s (%s). RANGO PROPIO DE LA VUELTA: %s..HEAD (%s)"
          % (corte, corte_h, apertura, apertura_h))
    print("VARA DE LA P3: %s (rutas: %s)"
          % ("VIEJA, anterior a la adjudicacion 6.1 del acta 153" if args.vara_vieja
             else "VIGENTE, adjudicacion 6.1 del acta 153", ", ".join(rutas)))
    print("LA ASIMETRIA P2 CONTRA P3 ESTA ESCRITA DENTRO DE ESTE INSTRUMENTO (adjudicacion")
    print("6.2 del acta 153): la P3 va con el reloj congelado porque mide un ACTO fechado;")
    print("la P2 lee el arbol de trabajo porque mide la EXISTENCIA de un control, que es un")
    print("estado y no una ejecucion. Ver el docstring, bloque de la adjudicacion 6.2.")

    F = fichas()
    ids = [f["id_op"] for f in F]
    print("FICHAS EN docs/plan/OPERACIONES.jsonl: %d" % len(F))
    assert len(set(ids)) == len(ids), "hay ids duplicados"

    print("")
    print("CRITERIO (TAREA 3.b): las tres pruebas estan escritas en el docstring de")
    print("este fichero, cada una con la fuente que la autoriza. Se dice SIEMPRE cual")
    print("de las tres sostiene cada fila.")
    print("")

    en_el_corte = fichas_del_corte(corte)
    print("")
    print("EL TEXTO DE LA FICHA VA CONGELADO EN --corte (adjudicacion 6.7 del acta 155):")
    print("  fichas en OPERACIONES.jsonl AL CORTE %s: %d" % (corte_h, len(en_el_corte)))
    print("  fichas en el ARBOL DE TRABAJO: %d" % len(F))
    print("  VARA DE `declara_su_estado`: %s"
          % ("ARBOL DE TRABAJO, la ANTERIOR a la adjudicacion 6.7 del acta 155 (contraste)"
             if args.declara_arbol else "DEL CORTE, la vigente"))
    print("")

    v1 = p1_vara_de_grafo()
    v2 = p2_vara_de_codigo(ids)
    v3 = p3_huella_en_git(ids, corte, rutas)
    v3b = p3b_caso_positivo(F, corte)

    propios, contados, intrusos = guarda_reloj_congelado(v3, apertura)
    print("GUARDA DEL RELOJ: commits propios de la vuelta %d | commits contados por P3 %d | INTRUSOS %d"
          % (len(propios), len(contados), len(intrusos)))
    if intrusos:
        print("  INTRUSOS: %s" % ", ".join(intrusos))
    assert not intrusos, (
        "LA VARA SE CUENTA A SI MISMA: la P3 esta usando como prueba %d commit(s) "
        "escritos por la propia vuelta (%s)" % (len(intrusos), ", ".join(intrusos)))

    print("COBERTURA DE CADA PRUEBA, CONTADA:")
    print("  P1 vara de grafo: %d ficha(s) con veredicto computable, %d con DESTINO CUMPLIDO"
          % (len(v1), sum(1 for k in v1 if v1[k][0])))
    print("  P2 vara de codigo (presencia): %d ficha(s) con el id_op en codigo vivo"
          % sum(1 for i in ids if v2[i]))
    print("  P3a huella en git (mensaje + rutas %s): %d ficha(s)"
          % ("/".join(x.strip("/") for x in rutas), sum(1 for i in ids if v3[i][1])))
    print("  P3b caso positivo o mutacion citado y presente en el arbol del corte: %d ficha(s)"
          % sum(1 for i in ids if v3b.get(i)))
    for i in ids:
        if v3b.get(i):
            print("      %-18s %s" % (i, ", ".join(v3b[i])))
    print("")

    filas_malas = []
    congelados_declarados = 0
    calzan = 0
    for f in F:
        i = f["id_op"]
        estado = f["estado"]
        pruebas = []
        if v1.get(i, (False,))[0]:
            pruebas.append("P1")
        if v2[i]:
            pruebas.append("P2")
        if v3[i][1]:
            pruebas.append("P3a")
        if v3b.get(i):
            pruebas.append("P3b")
        ejecutada = bool(pruebas)
        if estado == "HECHA" and ejecutada:
            calzan += 1
            continue
        if estado == "LISTA" and not ejecutada:
            calzan += 1
            continue
        if estado == "LISTA" and ejecutada:
            if args.declara_arbol:
                dice, marca = declara_su_estado(f)
            else:
                dice, marca = declara_su_estado_del_corte(f, en_el_corte)
            if dice:
                congelados_declarados += 1
                filas_malas.append((i, f["fase"], estado, "+".join(pruebas),
                                    "CONGELADO DECLARADO (la ficha habla de su estado: %s)" % marca,
                                    v2[i][:2], v3[i][1][:3]))
            else:
                filas_malas.append((i, f["fase"], estado, "+".join(pruebas),
                                    "CONGELADO EN SILENCIO: la ficha no dice nada de su estado",
                                    v2[i][:2], v3[i][1][:3]))
        elif estado == "HECHA" and not ejecutada:
            filas_malas.append((i, f["fase"], estado, "ninguna",
                                "HECHA SIN NINGUNA PRUEBA: el estado afirma mas que el repo",
                                v2[i][:2], v3[i][1][:3]))

    print("=" * 100)
    print("TABLA DE LAS QUE NO CALZAN (%d de %d). Las %d que calzan NO se imprimen."
          % (len(filas_malas), len(F), calzan))
    print("=" * 100)
    print("| id_op | fase | estado | pruebas | motivo |")
    print("|---|---|---|---|---|")
    for i, fase, estado, pr, motivo, _c, _g in filas_malas:
        print("| `%s` | %s | %s | %s | %s |" % (i, fase, estado, pr, motivo))
    print("")
    print("DESGLOSE, con la evidencia de cada fila:")
    for i, fase, estado, pr, motivo, cod, gits in filas_malas:
        print("  %s (%s, estado %s)" % (i, fase, estado))
        print("    pruebas que dan positivo: %s" % (pr or "ninguna"))
        if cod:
            print("    P2, en codigo vivo: %s" % ", ".join(cod))
        if gits:
            print("    P3, commits con codigo o dato: %s" % ", ".join(gits))
    print("")
    print("CONTADO: no calzan %d | de ellas, congeladas DECLARADAS %d | congeladas EN SILENCIO %d | HECHA sin prueba %d"
          % (len(filas_malas), congelados_declarados,
             sum(1 for x in filas_malas if "SILENCIO" in x[4]),
             sum(1 for x in filas_malas if "HECHA SIN" in x[4])))

    print("")
    print("=" * 100)
    print("TAREA 3.c: OPERACIONES DESBLOQUEADAS, con su depende_de MEDIDO")
    print("=" * 100)
    por_id = {f["id_op"]: f for f in F}
    desbloqueadas = []
    for f in F:
        if f["estado"] != "LISTA":
            continue
        dep = f.get("depende_de") or []
        estados_dep = [(d, por_id[d]["estado"] if d in por_id else "NO EXISTE") for d in dep]
        if all(e == "HECHA" for _d, e in estados_dep) and dep:
            desbloqueadas.append((f, estados_dep))
    print("Criterio: estado LISTA y TODAS sus depende_de en HECHA. Las de depende_de VACIO")
    print("no entran: nunca estuvieron bloqueadas y contarlas aqui seria ruido.")
    print("")
    print("| id_op | fase | tipo | depende_de medido |")
    print("|---|---|---|---|")
    for f, ed in desbloqueadas:
        print("| `%s` | %s | %s | %s |"
              % (f["id_op"], f["fase"], f["tipo"],
                 ", ".join("%s=%s" % (d, e) for d, e in ed)))
    print("")
    print("CONTADO: %d operacion(es) LISTA con todas sus dependencias en HECHA." % len(desbloqueadas))
    sin_dep = [f for f in F if f["estado"] == "LISTA" and not (f.get("depende_de") or [])]
    print("CONTRASTE: %d operacion(es) LISTA con depende_de VACIO (nunca bloqueadas)." % len(sin_dep))

    print("")
    print("Y LO QUE DE VERDAD QUEDA POR CORRER: las fichas en LISTA SIN NINGUNA de las")
    print("tres pruebas. Son las unicas cuyo estado LISTA calza con el repo, o sea las")
    print("unicas que el expediente y el arbol dicen a la vez que no se han ejecutado.")
    print("")
    print("| id_op | fase | tipo | depende_de medido |")
    print("|---|---|---|---|")
    pendientes = 0
    for f in F:
        i = f["id_op"]
        if f["estado"] != "LISTA":
            continue
        if v1.get(i, (False,))[0] or v2[i] or v3[i][1] or v3b.get(i):
            continue
        pendientes += 1
        dep = f.get("depende_de") or []
        medido = ", ".join("%s=%s" % (d, por_id[d]["estado"] if d in por_id else "NO EXISTE")
                           for d in dep) or "(vacio)"
        print("| `%s` | %s | %s | %s |" % (i, f["fase"], f["tipo"], medido))
    print("")
    print("CONTADO: %d ficha(s) en LISTA sin ninguna prueba de ejecucion." % pendientes)

    print("")
    print("CIFRA fichas del expediente: %d operaciones" % len(F))
    print("CIFRA fichas que no calzan: %d operaciones" % len(filas_malas))
    print("CIFRA fichas congeladas declaradas: %d operaciones" % congelados_declarados)
    print("CIFRA fichas congeladas en silencio: %d operaciones"
          % sum(1 for x in filas_malas if "SILENCIO" in x[4]))
    print("CIFRA fichas HECHA sin ninguna prueba: %d operaciones"
          % sum(1 for x in filas_malas if "HECHA SIN" in x[4]))
    print("CIFRA fichas en LISTA sin ninguna prueba: %d operaciones" % pendientes)


main()
