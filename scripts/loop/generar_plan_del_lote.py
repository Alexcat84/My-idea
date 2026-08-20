# -*- coding: utf-8 -*-
"""generar_plan_del_lote.py . EL GENERADOR DEL PLAN DE UN LOTE DE UN TRAMO DE
OP-U-01, CON LA PERDIDA SELLADA EN CAMPO PROPIO.

NOMBRE ESTABLE, Y NO LLEVA NUMERO NI DE VUELTA NI DE TRAMO NI DE LOTE: los tres
entran por argumento (--vuelta, --tramo, --lote) y el contenido editorial por
--contenido. Es la vara del acta 58, pregunta 4, la misma con la que nacieron
abrir_tramo_de_opu01.py y tallar_perdidas_del_plan.py.

SUCESOR DECLARADO de scripts/loop/vuelta59_planes.py (sha1 del ancestro
fda28294196f, medido hoy), AL QUE NO REEMPLAZA: el ancestro queda entero y
re-corrible, y los planes sellados de los tramos 2 a 5 lo siguen citando. Es la
via del acta 54, pregunta 3.

LA MAQUINA SE COPIA LITERAL Y NO SE RETECLEA: cargar_jsonl, puertas, sin_acentos,
extraer_verbatim y main entero salen del ancestro POR EXTRACCION de sus lineas
387 a 621 con scripts/loop/_v62_construir_generador.py, que lleva un assert por
cada cambio. Sobre ESA copia se aplican los CUATRO cambios de abajo, y cada uno
queda marcado en el sitio donde muerde.

LO QUE CAMBIA, Y ES SOLO ESTO:

  1. EL CONTENIDO EDITORIAL NO VIVE AQUI. El ancestro llevaba el lote A del tramo
     5 escrito dentro y los otros dos por import TALLADO (_v60_lote_b y
     _v60_lote_c). Aqui el modulo entra por --contenido, asi que este fichero no
     conoce ningun tramo ni ningun lote. NO ES ARITMETICA: es de donde se lee el
     texto.
  2. EL CAMPO perdidas VA EN CADA ACTO, SIEMPRE, AUNQUE VACIO. Es el contrato
     CAMPO PROPIO v1 (seccion 2.4 del reporte de la vuelta 61, y el docstring de
     scripts/loop/tallar_perdidas_del_plan.py): LISTA VACIA es una DECLARACION de
     cero perdidas y CAMPO AUSENTE es que el plan NO LO DICE, que es ROJO.
  3. LAS PERDIDAS SE VALIDAN AL SELLAR, no solo al tallar. Especie fuera de las
     TRES escritas, o clave que falta, es ROJO y el plan NO SE ESCRIBE. ES UNA
     GUARDA QUE CRECE, y por eso va enumerada aqui y MARCADA DISCUTIBLE en el
     reporte: son las dos condiciones que el acta 61 (D2 y pregunta 2) pone para
     que una guarda pueda crecer dentro de un sucesor declarado.
  4. LA RAIZ DEL PLAN DECLARA EL CONTRATO en contrato_de_perdidas. Sin esa linea
     el tallador nuevo se niega a leer por campo y exige --por-token con todas
     sus letras: el modo no se elige en silencio.

LO DEMAS ES COPIA: la guarda 1B, la cobertura exacta con marca UNICA por indice,
los indices CUBIERTO comprobados contra el superviviente real, la extraccion del
INCISO desde el nodo comparando sin tildes con su comprobacion verbatim, la
guarda de la juntura, el campo declarados_y_no_fundidos, y el numero de tramo
leido de la clave del ordinal del propio fichero medido.

  5. LA CABECERA SE ARMA DEL INSUMO O DECLARA SU FALTA, y ya no es un dict
     constante con las cifras de un tramo talladas dentro. Es la CORRECCION
     DECLARADA de la vuelta 63 (20 ago 2026, TAREA 1.b del encargo), nacida del
     censo scripts/loop/censo_de_plantillas_talladas.py, que dio UN solo TALLADO
     en los quince instrumentos de nombre estable y era este fichero. El texto
     viejo queda citado ENTERO en el comentario que hay justo encima de
     VARA_DEL_SUPERVIVIENTE. Lo que trae consigo, y va enumerado aqui porque es
     UNA GUARDA QUE CRECE y por eso va tambien MARCADA DISCUTIBLE en el reporte
     (acta 61, D2 y pregunta 2, que pone esas dos condiciones):
       - --operacion pasa a ser REQUERIDO. Un generador de nombre estable que da
         OP-U-01 por supuesto miente en cuanto se use para otra operacion.
       - --nomina, --dossier, --varas-impresas y --colisiones-esperadas son
         opcionales, y su AUSENCIA SE DECLARA dentro del plan sellado.
       - el cotejo del insumo contra los nodos de hoy se MIDE al sellar, sobre
         el tramo entero, en vez de citar la salida de otra corrida.
     LA ARITMETICA NO SE TOCA: guardas, cobertura, INCISOS, juntura, validacion
     de perdidas y el campo actos del plan salen exactamente igual que antes.

DE ESCRITURA SOLO SOBRE docs/loop/PLAN_V<N>_*.json. No toca ni un nodo.

Uso:
  python scripts/loop/generar_plan_del_lote.py --lote A --vuelta 62
      --operacion OP-U-01 --tramo docs/loop/TRAMO6_V61.jsonl
      --contenido _v62_lote_a [--nomina ...] [--dossier ...]
      [--varas-impresas ...] [--colisiones-esperadas ...] [--simular]
"""
import argparse
import datetime
import io
import json
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop")

# EL CONTRATO Y SUS TRES ESPECIES, copiados de scripts/loop/tallar_perdidas_del_plan.py
# para que el que SELLA y el que TALLA no puedan discrepar en silencio.
CONTRATO_DE_PERDIDAS = "CAMPO PROPIO v1"
CLAVES_DE_PERDIDA = ("especie", "que", "donde", "enrutada_a")
ESPECIES_DE_PERDIDA = ("DE PARAMETRO DE PASO", "DE CONDICIONES", "DE NOMBRE")

# ======================================================================
# CORRECCION DECLARADA (20 ago 2026, vuelta 63, TAREA 1.b del encargo).
# LA CABECERA DE ESTE GENERADOR ERA UN dict CONSTANTE CON LAS CIFRAS DEL
# TRAMO 6 TALLADAS DENTRO, y este fichero es de NOMBRE ESTABLE: corrido
# sobre cualquier otro tramo habria SELLADO un plan cuya cabecera afirma
# 21 actos, 42 combinaciones y 848 lineas de dossier sin haber medido
# ninguna de las tres. Es la misma especie que la vuelta 62 cazo en
# registrar_cierre_de_tramo.py, y aqui la caza el censo de esta vuelta:
# scripts/loop/censo_de_plantillas_talladas.py da UN solo TALLADO en los
# quince instrumentos de nombre estable, y es este fichero, con NUEVE
# cantidades talladas en las lineas 78, 79, 80 y 82
# (docs/loop/SALIDA_V63_CENSO_PLANTILLAS.txt).
#
# LA VARA QUE MANDA ES LA REGLA 1 DEL EJECUTOR LEIDA ENTERA, y el acta 62
# pregunta 1 (linea 16171) la aplica a este caso con todas sus letras: una
# plantilla con cifras talladas hace decir al instrumento cifras que NO
# midio, o sea viola EL INSTRUMENTO MANDA cada vez que corre. La forma
# debida, que es la que queda abajo: EL BLOQUE SE ARMA DEL INSUMO O
# DECLARA SU FALTA.
#
# EL TEXTO VIEJO SE QUEDA ESCRITO ENTERO AQUI, que es lo que hace
# auditable la correccion. Decia, literal:
#
#   CABERERA = {
#     "operacion": "OP-U-01",
#     "fecha": datetime.date.today().isoformat(),
#     "estado": "SELLADO",
#     "nomina": "docs/loop/_v62_componentes.jsonl, el recomputo corrido ANTES de la primera operacion de la vuelta 62",
#     "tramo_definido_en": "docs/loop/TRAMO6_V61.jsonl, abierto con scripts/loop/abrir_tramo_de_opu01.py en la vuelta 61 y FIJADO ahi. EL INSUMO NO SE RE-MIDE: 21 actos, puestos 30 a 50 de hoy y 250 a 270 en la nomina de la 48, todos PURO A y fusion pura, solape con los tramos 1 a 5 CERO. ES UN TRAMO CORTO POR AGOTAMIENTO Y ES EL ULTIMO DE OP-U-01: la vara del tramo es un PREFIJO CON TOPE de cincuenta y no un minimo (acta 61, D1 y pregunta 1, registrada en docs/plan/03_FUSIONES.md). COTEJADO CONTRA LOS NODOS DE HOY antes de escribir una linea de este plan: 21 actos mirados, 21 vivos, 0 ya fundidos, DESCALCES 0 (docs/loop/SALIDA_V62_COTEJO_INSUMO.txt).",
#     "dossier": "docs/loop/SALIDA_V61_DOSSIER_TRAMO6.txt (P.5, el acto leido entero con su razon entera pegada, 848 lineas) mas docs/loop/SALIDA_V61_VARAS_TRAMO6.txt",
#     "vara": "LOS 21 ACTOS DEL TRAMO 6 SON DE FUSION PURA (medido por la vuelta 61: tamano 2 y PURO A, 21 de 21): un acto de dos miembros con UN par A directo y ningun mixto. No hay lectura P.12 que hacer. El superviviente lo elige el CONTENIDO como P.8 lo define; UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4); si TODAS las varas de contenido concuerdan se funde a su lado; si el contenido EMPATA ENTERO, EL CABLEADO DECIDE SOLO (P.8); si dos varas de contenido CHOCAN decide la pieza DECLARADA (acta 53 pregunta 3, y tambien contra DOS conteos por acta 59 pregunta 2), y si la declarada esta a los dos lados se DECLARA (acto 29 del tramo 5). Y LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO (acta 54, pregunta 1, registrada en 03_FUSIONES.md): en un acto de dos donde el unico candidato limpio es la puerta, LA PUERTA SOBREVIVE y el choque se registra en el motivo. EL ROTULO SOLO (LINEA contra PASOS) NUNCA DECIDE, y LA RAMA DE LA CANTIDAD COMO VARA SIGUE NO ADOPTADA y no se usa en ningun acto de este plan.",
#     "varas_impresas": "docs/loop/SALIDA_V61_VARAS_TRAMO6.txt, una fila por acto con pasos, condiciones y cableado contados por maquina y la FORMA del veredicto impresa: 12 de UNA SOLA VARA, 5 de TODAS DE ACUERDO y 4 de CONTENIDO EMPATA. NI UN CHOCAN Y NI UN EMPATE SIN VARA en el tramo entero, que es lo que lo hace, por forma, el tramo mas limpio de la campana. El auditor lo re-corrio en la vuelta 61 y dio diff VACIO (acta 61, seccion 1). Ninguna cifra de este plan esta tecleada. LA FORMA IMPRESA ES MEDICION DE LOS TRES CONTEOS Y NO ADJUDICACION: no conoce la pieza declarada ni la guarda 1B, y por eso un acto puede salir de la tabla apuntando a un lado y decidirse al otro, que es exactamente lo que pasa en el acto 20.",
#     "colisiones_esperadas": "docs/loop/SALIDA_V61_COLISIONES_ESPERADAS_TRAMO6.txt, medidas por la vuelta 61 ANTES de tocar un nodo sobre EL ARCHIVO ENTERO, por PAR RESUELTO: 42 combinaciones simuladas y CERO que fabriquen colision, con cualquiera de los dos supervivientes en cualquiera de los 21 actos. El censo esperado de cada lote es CERO y una colision real DETIENE.",
#     "vara_de_las_puertas": "GUARDA 1B: ningun absorbido de este plan es semilla de entrada ni extremo de puente aprobado, comprobado por el generador y otra vez por el ejecutor. EN EL TRAMO 6 HAY UN SOLO ACTO CON MIEMBRO PUERTA, EL 20 (mantenimiento_sistema_cui, leido del dossier y de la columna puerta del cuadro de varas), Y AHI LA PUERTA NO ES LA QUE EL CONTENIDO ELIGE: el choque se registra en el motivo por acta 54, pregunta 1.",
#     "politica_del_reparto": "LA HEREDADA Y CITADA, no reinventada (acta 51 D3; acta 52 D5 y D10; acta 54 pregunta 5; acta 55 preguntas 3, 4 y 5; registros de las vueltas 53 a 57 y 60): una pieza del absorbido cuyo unico contenido propio es un PARAMETRO CONCRETO de un gesto que el superviviente ya tiene va de INCISO ADOSADO cuando el paso resultante se lee limpio, y de CUBIERTO con la perdida NOMBRADA cuando no. Una pieza que es un GESTO DISTINTO va de APPEND, y una pieza mitad propia mitad ya dicha va de APPEND ENTERO con el solape declarado para la poda de la fase 04. CUANDO LA RAZON DECLARA COMPARTIDO UN GESTO QUE EL TEXTO NO DICE, PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3). LAS PERDIDAS DE CONDICIONES NO VAN DE APPEND POR DEFECTO: se NOMBRAN mientras el INCISO de condiciones no exista (acta 55, pregunta 5), y solo van de APPEND cuando la condicion es un DISPARADOR DISTINTO y no un matiz del que el superviviente ya tiene. El INCISO es siempre TROZO VERBATIM del paso que muere, y se EXTRAE del nodo en vez de teclearse. Y LA NOVEDAD DE ESTE TRAMO: TODA perdida nombrada va ADEMAS sellada en el campo perdidas de su acto, con su especie, donde vive y a quien se enruta.",
#   }
#
# LO QUE NO CAMBIA, Y SE DICE PARA QUE NADIE LO BUSQUE EN EL DIFF: LA
# ARITMETICA NO SE TOCA. Las guardas, la cobertura, los INCISOS extraidos
# del nodo, la juntura, la validacion de las perdidas y el campo actos del
# plan salen exactamente igual que antes. LO UNICO QUE CAMBIA ES DE DONDE
# SALEN LAS CIFRAS Y LOS NOMBRES DE LA CABECERA.
# ======================================================================

# LA DOCTRINA CITADA, que NO lleva cifra medida de ningun tramo y por eso
# si puede vivir en una constante: son citas de actas y de puntos del
# banco, no cuentas de la corrida.
VARA_DEL_SUPERVIVIENTE = (
    "El superviviente lo elige el CONTENIDO como P.8 lo define; UNA SOLA VARA DE CONTENIDO "
    "NO EMPATADA BASTA (acta 53, pregunta 4); si TODAS las varas de contenido concuerdan se "
    "funde a su lado; si el contenido EMPATA ENTERO, EL CABLEADO DECIDE SOLO (P.8); si dos "
    "varas de contenido CHOCAN decide la pieza DECLARADA (acta 53 pregunta 3, y tambien "
    "contra DOS conteos por acta 59 pregunta 2), y si la declarada esta a los dos lados se "
    "DECLARA. Y LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE ENTRE LO PERMITIDO (acta 54, "
    "pregunta 1, registrada en docs/plan/03_FUSIONES.md): en un acto de dos donde el unico "
    "candidato limpio es la puerta, LA PUERTA SOBREVIVE y el choque se registra en el motivo. "
    "EL ROTULO SOLO (LINEA contra PASOS) NUNCA DECIDE, y LA RAMA DE LA CANTIDAD COMO VARA "
    "SIGUE NO ADOPTADA."
)
POLITICA_DEL_REPARTO = (
    "LA HEREDADA Y CITADA, no reinventada (acta 51 D3; acta 52 D5 y D10; acta 54 pregunta 5; "
    "acta 55 preguntas 3, 4 y 5; registros de las vueltas 53 a 57 y 60): una pieza del "
    "absorbido cuyo unico contenido propio es un PARAMETRO CONCRETO de un gesto que el "
    "superviviente ya tiene va de INCISO ADOSADO cuando el paso resultante se lee limpio, y "
    "de CUBIERTO con la perdida NOMBRADA cuando no. Una pieza que es un GESTO DISTINTO va de "
    "APPEND, y una pieza mitad propia mitad ya dicha va de APPEND ENTERO con el solape "
    "declarado para la poda de la fase 04. CUANDO LA RAZON DECLARA COMPARTIDO UN GESTO QUE EL "
    "TEXTO NO DICE, PARA EL REPARTO MANDA EL TEXTO (acta 55, pregunta 3). LAS PERDIDAS DE "
    "CONDICIONES NO VAN DE APPEND POR DEFECTO: se NOMBRAN mientras el INCISO de condiciones no "
    "exista (acta 55, pregunta 5), y solo van de APPEND cuando la condicion es un DISPARADOR "
    "DISTINTO y no un matiz del que el superviviente ya tiene. El INCISO es siempre TROZO "
    "VERBATIM del paso que muere, y se EXTRAE del nodo en vez de teclearse. Y BAJO EL CONTRATO "
    "CAMPO PROPIO v1: TODA perdida nombrada va ADEMAS sellada en el campo perdidas de su acto, "
    "con su especie, donde vive y a quien se enruta."
)


def insumo(ruta, que, para_que):
    """UN BLOQUE DE CABECERA QUE VIENE DE FUERA: o se arma del fichero que entra
    por argumento, con su tamano MEDIDO, o DECLARA su falta con todas las letras.
    Ninguna de las dos ramas teclea una cifra."""
    if not ruta:
        return ("NO ENTRO NINGUN FICHERO DE %s A ESTE GENERADOR, y por eso este plan NO LO "
                "DECLARA en vez de suponerlo. %s" % (que, para_que))
    completa = os.path.join(RAIZ, ruta.replace("/", os.sep))
    if not os.path.exists(completa):
        return ("SE PASO %s COMO FICHERO DE %s Y NO EXISTE EN EL ARBOL DE HOY: el plan lo dice "
                "en vez de callarlo. %s" % (ruta, que, para_que))
    n = len(io.open(completa, encoding="utf-8").read().split(chr(10)))
    return "%s (%d lineas, medidas al sellar). %s" % (ruta, n, para_que)


def cotejo_del_insumo(filas):
    """EL COTEJO DEL TRAMO ENTERO CONTRA LOS NODOS DE HOY, MEDIDO AL SELLAR. El
    texto viejo de la cabecera lo traia tallado (21 actos mirados, 21 vivos, 0 ya
    fundidos, DESCALCES 0) y apuntaba a la salida de otra corrida. Aqui se
    cuenta, y se cuenta sobre TODAS las filas del tramo, no solo sobre el lote."""
    mirados = len(filas)
    vivos = fundidos = descalces = 0
    for f in filas:
        estados = []
        for x in f["miembros"]:
            p = os.path.join(NODOS, x + ".json")
            if not os.path.exists(p):
                estados.append("falta")
            else:
                d = json.load(io.open(p, encoding="utf-8"))
                estados.append("deprecado" if (d.get("deprecado") or d.get("deprecated")) else "vivo")
        if "falta" in estados:
            descalces += 1
        elif "deprecado" in estados:
            fundidos += 1
        else:
            vivos += 1
    return ("%d actos mirados, %d vivos, %d ya fundidos, DESCALCES %d, contados al sellar "
            "sobre dataset/nodos" % (mirados, vivos, fundidos, descalces))


def cabecera(a, filas, ORD, num_tramo, prot, cotejo):
    """ARMA LA CABECERA DEL PLAN DESDE EL INSUMO. Cada cifra sale de filas (el
    fichero del tramo que entra por --tramo), de los nodos que el propio
    generador acaba de leer, o de un fichero que entra por argumento. La que no
    tenga de donde salir NO SE ESCRIBE: se declara ausente."""
    n = len(filas)
    puestos_hoy = sorted(f["puesto_hoy"] for f in filas if "puesto_hoy" in f)
    puestos_v48 = sorted(f["puesto_v48"] for f in filas if f.get("puesto_v48") is not None)
    puros = sum(1 for f in filas if f.get("figura") == "PURO A")
    dedos = sum(1 for f in filas if f.get("tamano") == 2)
    con_puerta = sorted(f[ORD] for f in filas if any(x in prot for x in f["miembros"]))
    combinaciones = sum(len(f["miembros"]) for f in filas)

    rango_hoy = ("puestos %d a %d de hoy" % (puestos_hoy[0], puestos_hoy[-1])
                 if puestos_hoy else "el fichero del tramo no trae puesto_hoy y este plan no lo inventa")
    rango_v48 = ("y %d a %d en la nomina previa" % (puestos_v48[0], puestos_v48[-1])
                 if puestos_v48 else "y el fichero del tramo no trae puesto de nomina previa")

    if con_puerta:
        puerta_txt = ("EN ESTE TRAMO HAY %d ACTO(S) CON MIEMBRO PUERTA, MEDIDO AL SELLAR CONTRA "
                      "entry_seeds.json Y LOS PUENTES APROBADOS: %s. Donde la puerta no sea la "
                      "que el contenido elige, el choque se registra en el motivo por acta 54, "
                      "pregunta 1."
                      % (len(con_puerta), ", ".join("acto %d" % x for x in con_puerta)))
    else:
        puerta_txt = ("NINGUN MIEMBRO DE ESTE TRAMO ES PUERTA, medido al sellar contra "
                      "entry_seeds.json y los puentes aprobados.")

    return {
        "operacion": a.operacion,
        # LA FECHA SE MIDE, NO SE TECLEA (correccion nacida de la caida de la vuelta 59).
        "fecha": datetime.date.today().isoformat(),
        "estado": "SELLADO",
        "nomina": insumo(a.nomina, "NOMINA (el recomputo de componentes)",
                         "Es el recomputo del que sale la nomina de los actos."),
        "tramo_definido_en": (
            "%s. EL INSUMO NO SE RE-MIDE, SE COTEJA: %d actos, %s %s, %d de figura PURO A y %d "
            "de tamano dos, TODO MEDIDO AL SELLAR sobre ese mismo fichero. La vara del tramo es "
            "un PREFIJO CON TOPE y no un minimo (acta 61, D1 y pregunta 1, registrada en "
            "docs/plan/03_FUSIONES.md). COTEJADO CONTRA LOS NODOS DE HOY antes de escribir una "
            "linea de este plan: %s."
            % (a.tramo, n, rango_hoy, rango_v48, puros, dedos, cotejo)),
        "dossier": insumo(a.dossier, "DOSSIER",
                          "Es la lectura P.5, el acto leido entero con su razon entera pegada."),
        "vara": ("DE LOS %d ACTOS DEL TRAMO, %d SON DE FUSION PURA, medido al sellar sobre el "
                 "fichero del tramo (figura PURO A y tamano dos): un acto de dos miembros con "
                 "UN par A directo y ningun mixto. %s"
                 % (n, min(puros, dedos), VARA_DEL_SUPERVIVIENTE)),
        "varas_impresas": insumo(
            a.varas_impresas, "CUADRO DE VARAS",
            "Es una fila por acto con pasos, condiciones y cableado contados por maquina y la "
            "FORMA del veredicto impresa. ESTE GENERADOR NO RE-CUENTA ESA FORMA Y POR ESO NO "
            "PUBLICA SU REPARTO: quien la quiera, la lee de ese fichero. LA FORMA IMPRESA ES "
            "MEDICION DE LOS TRES CONTEOS Y NO ADJUDICACION: no conoce la pieza declarada ni la "
            "guarda 1B, y por eso un acto puede salir de la tabla apuntando a un lado y "
            "decidirse al otro."),
        "colisiones_esperadas": (
            "%s COMBINACIONES POSIBLES DE SUPERVIVIENTE EN ESTE TRAMO: %d, contadas al sellar "
            "como la suma de los miembros de los %d actos. El censo esperado de cada lote lo "
            "fija ese fichero y una colision real DETIENE."
            % (insumo(a.colisiones_esperadas, "COLISIONES ESPERADAS",
                      "Es el censo por PAR RESUELTO sobre el archivo entero, medido ANTES de "
                      "tocar un nodo."), combinaciones, n)),
        "vara_de_las_puertas": (
            "GUARDA 1B: ningun absorbido de este plan es semilla de entrada ni extremo de puente "
            "aprobado, comprobado por el generador y otra vez por el ejecutor. %s" % puerta_txt),
        "politica_del_reparto": POLITICA_DEL_REPARTO,
    }


def cargar_jsonl(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def puertas():
    """MISMA fuente que scripts/loop/vuelta48_puertas_en_el_lote.py."""
    out = set()
    p = os.path.join(RAIZ, "dataset", "metadata", "entry_seeds.json")
    if os.path.exists(p):
        out.update(json.load(io.open(p, encoding="utf-8")).get("seeds", []))
    packs = os.path.join(RAIZ, "packs")
    if os.path.isdir(packs):
        for d in sorted(os.listdir(packs)):
            q = os.path.join(packs, d, "metadata", "entry_seeds.json")
            if os.path.exists(q):
                out.update(json.load(io.open(q, encoding="utf-8")))
            q = os.path.join(packs, d, "metadata", "bridges_aprobados.json")
            if os.path.exists(q):
                for x in json.load(io.open(q, encoding="utf-8")).get("aprobados", []):
                    for extremo in ("core", "dominio"):
                        if x.get(extremo):
                            out.add(x[extremo])
    return out


def sin_acentos(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def extraer_verbatim(texto, trozo_ascii):
    """Recibe el trozo escrito EN ASCII, lo casa contra el paso REAL comparando
    las dos cadenas sin tildes, y devuelve LA SUBCADENA REAL del paso, con sus
    acentos. Una extraccion ambigua no es una extraccion."""
    plano_texto = sin_acentos(texto)
    plano_trozo = sin_acentos(trozo_ascii)
    if len(plano_texto) != len(texto):
        return None, "la normalizacion cambio la longitud del paso y las posiciones no son fiables"
    veces = plano_texto.count(plano_trozo)
    if veces == 0:
        return None, "el trozo no casa dentro del paso ni comparando sin tildes"
    if veces > 1:
        return None, "el trozo casa %d veces dentro del paso: extraccion ambigua" % veces
    i = plano_texto.index(plano_trozo)
    return texto[i:i + len(plano_trozo)], None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lote", required=True)
    ap.add_argument("--contenido", required=True,
                    help="modulo del contenido editorial del lote, por ejemplo _v62_lote_a")
    ap.add_argument("--vuelta", type=int, required=True)
    ap.add_argument("--tramo", default="docs/loop/TRAMO5_V58.jsonl")
    # CORRECCION DECLARADA (20 ago 2026, vuelta 63): LOS CINCO NOMBRES Y FICHEROS
    # QUE LA CABECERA CITABA TALLADOS AHORA ENTRAN POR ARGUMENTO. --operacion es
    # REQUERIDO porque un generador de nombre estable que da OP-U-01 por supuesto
    # miente en cuanto se use para otra operacion; los otros cuatro son
    # opcionales y su ausencia se DECLARA en el plan en vez de suponerse.
    ap.add_argument("--operacion", required=True,
                    help="id de la operacion que este plan ejecuta, por ejemplo OP-U-01")
    ap.add_argument("--nomina", default=None,
                    help="jsonl del recomputo de componentes del que sale la nomina")
    ap.add_argument("--dossier", default=None, help="salida de la lectura P.5 del tramo")
    ap.add_argument("--varas-impresas", dest="varas_impresas", default=None,
                    help="salida del cuadro de varas del tramo")
    ap.add_argument("--colisiones-esperadas", dest="colisiones_esperadas", default=None,
                    help="salida del censo de colisiones esperadas del tramo")
    ap.add_argument("--prefijo", default=None,
                    help="prefijo del plan; por defecto PLAN_V<vuelta>_OPU01_LOTE_")
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    filas = cargar_jsonl(os.path.join(RAIZ, a.tramo.replace("/", os.sep)))
    claves = sorted({k for k in filas[0] if k.startswith("orden_tramo")}) if filas else []
    if len(claves) != 1:
        print("ROJO: el fichero del tramo tiene %d claves de ordinal (%s). PARADA."
              % (len(claves), claves))
        return 1
    ORD = claves[0]
    # EL NUMERO DE TRAMO SALE DEL FICHERO MEDIDO Y NO DE UNA CONSTANTE, que es la
    # correccion que la TAREA 1.1 de esta vuelta manda: orden_tramo5 dice tramo 5.
    m = re.search(r"(\d+)$", ORD)
    num_tramo = m.group(1) if m else "SIN NUMERO EN LA CLAVE %s" % ORD

    tramo = {r[ORD]: r for r in filas}
    prot = puertas()
    cotejo_txt = cotejo_del_insumo(filas)
    # CAMBIO 1 DECLARADO: EL CONTENIDO EDITORIAL NO VIVE EN ESTE FICHERO. El
    # ancestro llevaba el lote A del tramo 5 escrito dentro y los otros dos por
    # import TALLADO. Aqui el modulo entra por --contenido y este generador no
    # conoce ningun tramo ni ningun lote: un cambio de TEXTO y uno de ARITMETICA
    # no se pueden pisar en el mismo diff.
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    mod = __import__(a.contenido)
    lotes = {k[len("LOTE_"):]: getattr(mod, k) for k in dir(mod) if k.startswith("LOTE_")}
    if a.lote not in lotes:
        print("ROJO: el modulo %s no trae el lote %s (trae %s). PARADA."
              % (a.contenido, a.lote, sorted(lotes)))
        return 1
    lote = lotes[a.lote]
    prefijo = a.prefijo or ("PLAN_V%d_OPU01_LOTE_" % a.vuelta)

    print("=" * 78)
    print("GENERADOR DEL PLAN DEL LOTE %s DEL TRAMO %s (vuelta %d)"
          % (a.lote, num_tramo, a.vuelta))
    print("  fichero del tramo: %s" % a.tramo)
    print("=" * 78)
    print()

    fallos = []
    actos = []
    for spec in lote["actos"]:
        n = spec["orden"]
        if n not in tramo:
            fallos.append("acto %d: no esta en el tramo vivo %s" % (n, a.tramo))
            continue
        act = tramo[n]
        mi = sorted(act["miembros"])
        sup = spec["superviviente"]
        if sup not in mi:
            fallos.append("acto %d: el superviviente %s no es miembro" % (n, sup))
            continue
        ab = [x for x in mi if x != sup][0]
        if ab in prot:
            fallos.append("acto %d: GUARDA 1B EN ROJO, el absorbido %s es puerta" % (n, ab))
        oa = json.load(io.open(os.path.join(NODOS, ab + ".json"), encoding="utf-8"))
        os_ = json.load(io.open(os.path.join(NODOS, sup + ".json"), encoding="utf-8"))
        if oa.get("deprecado") or os_.get("deprecado"):
            fallos.append("acto %d: alguno de los dos miembros YA esta deprecado" % n)
        pa = oa.get("pasos_accionables") or []
        ca = oa.get("condiciones_activacion") or []
        ps = os_.get("pasos_accionables") or []
        cs = os_.get("condiciones_activacion") or []

        marcas_p, marcas_c = {}, {}
        for i, texto in enumerate(pa, 1):
            m2 = spec["pasos"].get(str(i))
            if not m2:
                fallos.append("acto %d: el paso %d de %s no tiene marca" % (n, i, ab))
                continue
            if m2[0] == "APPEND":
                marcas_p[str(i)] = "APPEND"
            elif m2[0] == "CUBIERTO":
                if not (1 <= m2[1] <= len(ps)):
                    fallos.append("acto %d: CUBIERTO:%d y el superviviente tiene %d pasos"
                                  % (n, m2[1], len(ps)))
                marcas_p[str(i)] = "CUBIERTO:%d" % m2[1]
            elif m2[0] == "CUBIERTO_COND":
                if not (1 <= m2[1] <= len(cs)):
                    fallos.append("acto %d: CUBIERTO_COND:%d y el superviviente tiene %d condiciones"
                                  % (n, m2[1], len(cs)))
                marcas_p[str(i)] = "CUBIERTO_COND:%d" % m2[1]
            elif m2[0] == "INCISO":
                _, k, ascii_trozo, nexo = m2
                trozo, motivo = extraer_verbatim(texto, ascii_trozo)
                if trozo is None:
                    fallos.append("acto %d, paso %d de %s: INCISO %r, %s"
                                  % (n, i, ab, ascii_trozo, motivo))
                    continue
                if trozo not in texto:
                    fallos.append("acto %d: el INCISO extraido %r NO es trozo verbatim del paso %d de %s"
                                  % (n, trozo, i, ab))
                if "|" in trozo or "|" in nexo:
                    fallos.append("acto %d: el INCISO o su nexo llevan la barra vertical, que es el separador de la marca" % n)
                if not (1 <= k <= len(ps)):
                    fallos.append("acto %d: INCISO al paso %d y el superviviente tiene %d"
                                  % (n, k, len(ps)))
                else:
                    resultante = ps[k - 1] + nexo + trozo
                    if (ps[k - 1].rstrip().endswith((".", "!", "?"))
                            and nexo.lstrip().startswith((",", ";"))):
                        fallos.append(
                            "acto %d, paso %d de %s: JUNTURA ROTA, el paso del "
                            "superviviente acaba en punto y el nexo abre con coma: %r"
                            % (n, i, ab, resultante[max(0, len(ps[k - 1]) - 30):][:80]))
                    print("  acto %-3d INCISO al paso %d" % (n, k))
                    print("      trozo pedido en ASCII : %r" % ascii_trozo)
                    print("      trozo EXTRAIDO del nodo: %r" % trozo)
                    print("      paso resultante        : %s" % (ps[k - 1] + nexo + trozo))
                marcas_p[str(i)] = "INCISO:%d|%s|%s" % (k, trozo, nexo)
            else:
                fallos.append("acto %d: marca desconocida %r" % (n, m2))
        for i, texto in enumerate(ca, 1):
            m2 = spec["condiciones"].get(str(i))
            if not m2:
                fallos.append("acto %d: la condicion %d de %s no tiene marca" % (n, i, ab))
                continue
            if m2[0] == "APPEND":
                marcas_c[str(i)] = "APPEND"
            elif m2[0] == "CUBIERTO":
                if not (1 <= m2[1] <= len(cs)):
                    fallos.append("acto %d: CUBIERTO:%d y el superviviente tiene %d condiciones"
                                  % (n, m2[1], len(cs)))
                marcas_c[str(i)] = "CUBIERTO:%d" % m2[1]
            else:
                fallos.append("acto %d: marca de condicion desconocida %r" % (n, m2))
        # CAMBIO 3 DECLARADO, GUARDA QUE CRECE Y VA MARCADA DISCUTIBLE (acta 61,
        # D2 y pregunta 2: una guarda puede crecer en un sucesor declarado SI va
        # enumerada en el docstring y marcada discutible). Las perdidas se validan
        # AQUI, al SELLAR, y no solo despues en el tallador: especie fuera de las
        # tres escritas, o clave que falta, es ROJO y el plan NO SE ESCRIBE.
        for p_ in (spec.get("perdidas") or []):
            faltan_ = [k for k in CLAVES_DE_PERDIDA if k not in p_]
            if faltan_:
                fallos.append("acto %d: a una perdida le faltan las claves %s"
                              % (n, ", ".join(faltan_)))
            elif p_["especie"] not in ESPECIES_DE_PERDIDA:
                fallos.append("acto %d: especie de perdida desconocida %r. Las escritas son: %s"
                              % (n, p_["especie"], ", ".join(ESPECIES_DE_PERDIDA)))
        sobra_p = set(spec["pasos"]) - {str(i) for i in range(1, len(pa) + 1)}
        sobra_c = set(spec["condiciones"]) - {str(i) for i in range(1, len(ca) + 1)}
        if sobra_p or sobra_c:
            fallos.append("acto %d: marcas que sobran, pasos %s condiciones %s"
                          % (n, sorted(sobra_p), sorted(sobra_c)))

        actos.append({
            "orden": n,
            "miembros": [sup, ab],
            "miembros_del_acto_entero": mi,
            "figura": "FUSION PURA, un solo par A directo y ningun mixto",
            "superviviente": sup,
            "motivo": spec["motivo"],
            "absorbidos": [ab],
            "pasos": {ab: marcas_p},
            "condiciones": {ab: marcas_c},
            "nota_del_reparto": spec["nota"],
            # CAMBIO 2 DECLARADO: EL CAMPO perdidas VA SIEMPRE, aunque vacio.
            # Es la mitad util del contrato CAMPO PROPIO v1: LISTA VACIA es una
            # DECLARACION de cero perdidas y CAMPO AUSENTE es que el plan NO LO
            # DICE. El ancestro no tenia campo y la perdida vivia solo en la
            # prosa, que es la averia que el acta 60 dejo nombrada.
            "perdidas": list(spec.get("perdidas") or []),
        })

    print()
    if fallos:
        print("  ROJO, %d fallos y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("     %s" % f)
        return 1
    print("  las %d fichas del lote %s: TODAS en verde" % (len(actos), a.lote))
    print("  guarda 1B: ningun absorbido es puerta")
    print("  cobertura: cada paso y cada condicion de cada absorbido con marca UNICA")
    print("  incisos: todos EXTRAIDOS del nodo y comprobados VERBATIM dentro del paso")
    print()
    print("  RESUMEN DEL REPARTO POR ACTO:")
    tot = {"APPEND": 0, "CUBIERTO": 0, "INCISO": 0}
    for x in actos:
        c = {"APPEND": 0, "CUBIERTO": 0, "INCISO": 0}
        for d in (x["pasos"], x["condiciones"]):
            for marcas in d.values():
                for m2 in marcas.values():
                    k = "APPEND" if m2 == "APPEND" else ("INCISO" if m2.startswith("INCISO") else "CUBIERTO")
                    c[k] += 1
                    tot[k] += 1
        print("     acto %-3d sobrevive %-46s piezas %2d (enteras %d, ya dichas %d, de INCISO %d)"
              % (x["orden"], x["superviviente"], sum(c.values()),
                 c["APPEND"], c["CUBIERTO"], c["INCISO"]))
    print("     TOTAL del lote %s: piezas %d (enteras %d, ya dichas %d, de INCISO %d)"
          % (a.lote, sum(tot.values()), tot["APPEND"], tot["CUBIERTO"], tot["INCISO"]))
    per_tot = sum(len(x["perdidas"]) for x in actos)
    con_per = len([x for x in actos if x["perdidas"]])
    print()
    print("  LAS PERDIDAS SELLADAS EN CAMPO PROPIO (contrato %s):" % CONTRATO_DE_PERDIDAS)
    print("     actos con el campo perdidas presente: %d de %d (el campo va SIEMPRE)"
          % (len(actos), len(actos)))
    print("     actos que DECLARAN cero perdidas    : %d" % (len(actos) - con_per))
    print("     actos con al menos una perdida      : %d" % con_per)
    print("     perdidas selladas, en total         : %d" % per_tot)
    for x in actos:
        for p_ in x["perdidas"]:
            print("        acto %-3d %-22s %s" % (x["orden"], p_["especie"], p_["que"]))

    plan = cabecera(a, filas, ORD, num_tramo, prot, cotejo_txt)
    # CAMBIO 4 DECLARADO: LA RAIZ DECLARA EL CONTRATO. Sin esta linea el tallador
    # nuevo se niega a leer por campo y exige --por-token con todas sus letras:
    # el modo no se elige en silencio.
    plan["contrato_de_perdidas"] = CONTRATO_DE_PERDIDAS
    plan["vuelta"] = a.vuelta
    plan["tramo"] = "%s, %s" % (num_tramo, lote["titulo"])
    plan["actos"] = actos
    plan["declarados_y_no_fundidos"] = lote.get("declarados", [])
    destino = os.path.join(SALIDA, "%s%s.json" % (prefijo, a.lote))
    if not a.simular:
        io.open(destino, "w", encoding="utf-8", newline=chr(10)).write(
            json.dumps(plan, ensure_ascii=False, indent=1) + chr(10))
        print()
        print("  plan escrito: %s" % os.path.relpath(destino, RAIZ))
    else:
        print()
        print("  MODO SIMULAR: no se escribe el plan.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
