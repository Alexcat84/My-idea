# -*- coding: utf-8 -*-
"""vuelta54_planes.py . EL GENERADOR DE LOS PLANES DEL TRAMO 2 DE OP-U-01.

POR QUE EXISTE: el plan que come scripts/loop/vuelta49_fundir_tramo.py es un
json con una marca por CADA paso y CADA condicion de CADA absorbido. Escribirlo
a mano es teclear indices, y ademas las marcas INCISO llevan un TROZO VERBATIM
del paso del que muere: un acento mal copiado tumba la guarda del inciso DESPUES
de haber leido el acto entero. Aqui el inciso se declara como SUBCADENA y el
generador COMPRUEBA que este dentro del paso ANTES de escribir el plan; si no
esta, cae en rojo y no escribe nada.

TAMBIEN COMPRUEBA, antes de escribir:
  - que el superviviente y el absorbido sean los miembros del acto;
  - que cada paso y cada condicion del absorbido tenga marca, exactamente una;
  - que los indices CUBIERTO apunten a un paso o condicion que exista;
  - que ningun absorbido sea PUERTA (guarda 1B), con la misma fuente que
    scripts/loop/vuelta48_puertas_en_el_lote.py.

DE ESCRITURA SOLO SOBRE docs/loop/PLAN_V54_*.json. No toca ni un nodo.

Uso:
  python scripts/loop/vuelta54_planes.py --lote A [--simular]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
TRAMO = os.path.join(RAIZ, "docs", "loop", "TRAMO2_V54.jsonl")
SALIDA = os.path.join(RAIZ, "docs", "loop")

CABECERA = {
    "operacion": "OP-U-01",
    "fecha": "2026-08-20",
    "vuelta": 54,
    "estado": "SELLADO",
    "nomina": "docs/loop/RECOMPUTO_V54_APERTURA.jsonl",
    "tramo_definido_en": "docs/loop/SALIDA_V54_TRAMO2_NOMINA.txt, con las DOS lecturas de 'los 50 siguientes' calzando en el mismo tramo y el mismo orden",
    "dossier": "docs/loop/SALIDA_V54_DOSSIER_TRAMO2.txt (P.5, el acto leido entero) mas docs/loop/SALIDA_V54_MESA_TRAMO2.txt y docs/loop/SALIDA_V54_VARAS_TRAMO2.txt",
    "vara": "TODOS los actos del tramo 2 son de FUSION PURA (50 de 50, medido): un acto de dos miembros con UN par A directo y ningun mixto. No hay lectura P.12 que hacer, porque no hay mixto que quede fuera. El superviviente lo elige el CONTENIDO como P.8 lo define (pasos y condiciones, material propio y padre declarado EN LAS RAZONES); UNA SOLA VARA DE CONTENIDO NO EMPATADA BASTA (acta 53, pregunta 4); si dos varas de contenido CHOCAN decide la pieza DECLARADA de mayor peso en las razones y si no hay ninguna se PARA (acta 53, pregunta 3); si el contenido calla entero, EL CABLEADO DECIDE SOLO; si tambien empata, se DECLARA empate sin vara.",
    "varas_impresas": "docs/loop/SALIDA_V54_VARAS_TRAMO2.txt, una fila por acto con pasos, condiciones y cableado contados por maquina y la FORMA del veredicto impresa. Ninguna cifra de este plan esta tecleada.",
    "colisiones_esperadas": "docs/loop/SALIDA_V54_COLISIONES_ESPERADAS_TRAMO2.txt, medidas ANTES de tocar un nodo sobre EL ARCHIVO ENTERO, por PAR RESUELTO, con scripts/loop/vuelta54_colisiones_esperadas.py (sucesor declarado del de la vuelta 51, que salta la fusion pura y por eso no imprimia ni uno de estos 50). Una colision real fuera de esa prediccion detiene.",
    "vara_de_las_puertas": "docs/loop/SALIDA_V54_PUERTAS_APERTURA.txt (30 actos con puerta dentro: 25 salvables, 2 imposibles por nomina, 3 por estructura, 0 sin receta). GUARDA 1B: ningun absorbido de este plan es semilla de entrada ni extremo de puente aprobado, comprobado por el generador y otra vez por el ejecutor.",
    "politica_del_reparto": "LA HEREDADA Y CITADA, no reinventada (acta 51 D3; acta 52 D5 y D10; registro de la vuelta 53): una pieza del absorbido cuyo unico contenido propio es un PARAMETRO CONCRETO de un gesto que el superviviente ya tiene va de INCISO ADOSADO cuando el paso resultante se lee limpio, y de CUBIERTO con la perdida NOMBRADA cuando no. Una pieza que es un GESTO DISTINTO va de APPEND. El INCISO es siempre TROZO VERBATIM del paso que muere.",
}

# --------------------------------------------------------------------------
# LOS LOTES. Cada acto: ordinal del tramo 2, superviviente, motivo, y el
# reparto pieza a pieza. En INCISO el segundo campo es la SUBCADENA VERBATIM
# y el tercero el NEXO que la une al paso del superviviente.
# --------------------------------------------------------------------------
LOTES = {
    "A": {
        "titulo": "2, LOTE A DE LA VUELTA 54: los actos 2, 3, 5, 7, 8, 9, 10, 11, 12, 13 y 14 del tramo 2 (los ONCE primeros del tramo cuyo superviviente elige el contenido sin choque, sin puerta en juego y sin colision prevista)",
        "actos": [
            {
                "orden": 2,
                "superviviente": "diseno_de_desafios_de_innovacion",
                "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA Y BASTA (acta 53, pregunta 4): los pasos EMPATAN 5 contra 5 y las CONDICIONES apuntan a diseno_de_desafios_de_innovacion, 3 contra 2. El cableado esta de acuerdo (5 contra 3) y no hace falta que hable. El puesto 237 no escribe la formula Sobrevive X, asi que aqui no hay choque de letra contra aritmetica.",
                "pasos": {
                    "1": ["INCISO", 1, "técnico o social", ", sea "],
                    "2": ["CUBIERTO", 2],
                    "3": ["APPEND"],
                    "4": ["APPEND"],
                    "5": ["INCISO", 5, "el impacto posterior en inversión e innovación del sector", ", y también "],
                },
                "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
                "nota": "EL PASO 3 DEL QUE MUERE VA DE APPEND Y LA RAZON DEL 237 DICE QUE LOS DOS MANDAN CONVOCAR EQUIPOS: la razon resume, y medido paso a paso el superviviente NO TIENE paso de convocatoria (sus cinco son definir el reto, reglas y premio, comunicar el progreso, aprovechar medios y evaluar). Se dice en vez de callarse, y la pieza viaja entera. EL PASO 4 TAMBIEN VA DE APPEND aunque su segunda mitad (publicitar para narrativa) la dice el paso 4 del superviviente: su primera mitad, DOCUMENTAR el proceso, no la dice nadie, y esta operacion mueve piezas enteras y no parte pasos. El solape que eso fabrica es de los que recoge la poda de la fase 04. CERO perdidas nombradas.",
            },
            {
                "orden": 3,
                "superviviente": "innovacion_abierta",
                "motivo": "CONTENIDO, Y LO DECIDE LA CONTENCION DECLARADA EN LA RAZON, que P.8 pesa por encima de cualquier conteo: el puesto 244 escribe que CINCO DE LOS SEIS PASOS DEL SEGUNDO SON LOS PASOS 2 A 6 DEL PRIMERO, uno por uno, y los nombra. Los pasos apuntan al mismo lado (7 contra 6) y las condiciones empatan. EL CABLEADO APUNTA AL OTRO (10 contra 3) y no manda, porque el contenido no calla.",
                "pasos": {
                    "1": ["INCISO", 2, "conferencias, ferias", ", y que visiten "],
                    "2": ["CUBIERTO", 3],
                    "3": ["CUBIERTO", 4],
                    "4": ["CUBIERTO", 5],
                    "5": ["CUBIERTO", 6],
                    "6": ["APPEND"],
                },
                "condiciones": {"1": ["CUBIERTO", 3], "2": ["CUBIERTO", 2], "3": ["APPEND"]},
                "nota": "EL PASO 6 DEL QUE MUERE (adaptar el Stage-Gate para manejar ideas, IP y tecnologias externas) ES EL UNICO GESTO QUE EL SUPERVIVIENTE NO TIENE y viaja entero. PERDIDA NOMBRADA, UNA: la condicion 2 del que muere dice 'de consumo relativamente simple O CREATIVO' y la condicion 2 del superviviente dice 'B2C con productos de tecnologia relativamente simple': el 'o creativo' se pierde y se nombra aqui.",
            },
            {
                "orden": 5,
                "superviviente": "customer_appreciation_pr",
                "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA: los pasos apuntan a customer_appreciation_pr (5 contra 4) y las condiciones empatan 2 contra 2. El cableado esta de acuerdo (6 contra 2). El puesto 262 no nombra superviviente.",
                "pasos": {
                    "1": ["CUBIERTO", 4],
                    "2": ["APPEND"],
                    "3": ["INCISO", 2, "resolución de problemas fuera del alcance normal", ", además de la "],
                    "4": ["CUBIERTO", 5],
                },
                "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
                "nota": "EL PASO 2 DEL QUE MUERE VA DE APPEND porque es un GESTO DISTINTO: poner POLITICAS que prioricen la satisfaccion sobre la eficiencia operativa (envios y devoluciones gratis) no es ninguno de los cinco gestos del superviviente. Su paso 3 va de INCISO porque su unico contenido propio es un PARAMETRO del gesto que el paso 2 del superviviente ya manda. CERO perdidas nombradas.",
            },
            {
                "orden": 7,
                "superviviente": "analisis_varianza_financiera",
                "motivo": "CONTENIDO, LAS DOS VARAS DE ACUERDO: pasos 4 contra 3 y condiciones 2 contra 1, las dos hacia analisis_varianza_financiera. El cableado empata 3 contra 3 y no hace falta. La razon del 273 llama a los dos gestos propios del elegido DETALLE DE EJECUCION sobre la misma instruccion, y aun asi son suyos y estan escritos.",
                "pasos": {
                    "1": ["INCISO", 1, "cada mes", ", y hacerlo "],
                    "2": ["CUBIERTO", 1],
                    "3": ["APPEND"],
                },
                "condiciones": {"1": ["CUBIERTO", 1]},
                "nota": "PERDIDA NOMBRADA, UNA: el paso 2 del que muere ofrece comparar TAMBIEN CONTRA EL PERIODO ANTERIOR como alternativa al presupuesto, y el superviviente solo calcula contra presupuesto. Va de CUBIERTO y no de INCISO porque el paso resultante NO se leia limpio con los dos incisos encadenados sobre el mismo paso 1 (habria quedado 'hacerlo cada mes o contra el periodo anterior', que dice otra cosa). LA PERDIDA QUEDA NOMBRADA AQUI, que es el carril de la tabla de los seis motivos. El paso 3 va de APPEND porque ANOTAR LA CAUSA es un gesto que el superviviente no tiene.",
            },
            {
                "orden": 8,
                "superviviente": "stage_gate_system",
                "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA: los pasos apuntan a stage_gate_system (5 contra 4) y las condiciones empatan 2 contra 2. El cableado esta de acuerdo (11 contra 10). La razon del 275 dice que cada uno anade lo suyo, asi que el material propio declarado NO desempata, y el conteo si.",
                "pasos": {
                    "1": ["INCISO", 1, "Discovery, Scoping, Business Case, Development, Testing, Launch", ", por ejemplo "],
                    "2": ["CUBIERTO", 2],
                    "3": ["APPEND"],
                    "4": ["APPEND"],
                },
                "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
                "nota": "LOS DOS GESTOS PROPIOS QUE LA RAZON LE RECONOCE AL QUE MUERE VIAJAN ENTEROS: el equipo multifuncional en paralelo (paso 3) y la logica de compra de opciones incrementales (paso 4). Su paso 1 va de INCISO porque el gesto (definir las etapas) ya esta y lo propio es LA LISTA DE ETAPAS, que es un parametro concreto. CERO perdidas nombradas.",
            },
            {
                "orden": 9,
                "superviviente": "antigoals_framework",
                "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO, que es el carril escrito: pasos 5 contra 5, condiciones 3 contra 3, y la razon del 282 dice EL MISMO FRAMEWORK DICHO DOS VECES, con un cierre propio para cada uno (revisitar contra compartir). El cableado apunta a antigoals_framework, 5 contra 3. NO es empate sin vara, porque el empate sin vara exige que TAMBIEN el cableado empate (acta 53, pregunta 4).",
                "pasos": {
                    "1": ["CUBIERTO", 1],
                    "2": ["CUBIERTO", 2],
                    "3": ["CUBIERTO", 3],
                    "4": ["CUBIERTO", 4],
                    "5": ["APPEND"],
                },
                "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 3], "3": ["CUBIERTO", 2]},
                "nota": "EL PASO 5 DEL QUE MUERE (compartir la lista con el equipo) VIAJA ENTERO: el superviviente cierra REVISITANDO las listas, que es otro gesto. Los ejemplos de antimeta del que muere (no confundir al usuario, no excluir personas con discapacidad) son parametros de un gesto que el paso 3 del superviviente ya trae con sus propios ejemplos, y van de CUBIERTO. CERO perdidas nombradas.",
            },
            {
                "orden": 10,
                "superviviente": "arquetipos_de_cliente",
                "motivo": "CONTENIDO, LAS DOS VARAS DE ACUERDO Y ADEMAS LA CONTENCION DECLARADA: pasos 8 contra 4 y condiciones 3 contra 2, las dos hacia arquetipos_de_cliente, y el puesto 288 escribe que el primero DESARROLLA MUCHO MAS el trabajo previo y que EL SEGUNDO ES LA VERSION CORTA DEL MISMO GESTO. EL CABLEADO APUNTA AL OTRO Y CON MARGEN ANCHO (20 contra 5) y no manda, porque el contenido no calla.",
                "pasos": {
                    "1": ["CUBIERTO", 4],
                    "2": ["INCISO", 5, "demográfico y psicográfico", ", con su perfil "],
                    "3": ["CUBIERTO", 3],
                    "4": ["CUBIERTO", 7],
                },
                "condiciones": {"1": ["CUBIERTO", 3], "2": ["APPEND"]},
                "nota": "EL PASO 1 DEL QUE MUERE (dibujar al usuario final Y al decisor clave) LO DICEN LOS PASOS 3 Y 4 DEL SUPERVIVIENTE JUNTOS, y la marca apunta al 4 porque es el que nombra al decisor y lo separa de quien usa. PERDIDA NOMBRADA, UNA: el ejemplo HOGAR del contexto fisico del paso 3 del que muere, que el paso 3 del superviviente no lista (dice oficina, planta, cubiculo).",
            },
            {
                "orden": 11,
                "superviviente": "assumption_constraint_log",
                "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA: los pasos empatan 5 contra 5 y las condiciones apuntan a assumption_constraint_log, 2 contra 1. La razon del 289 dice que los cinco pasos coinciden uno a uno y que lo unico que los separa es que el segundo PRECISA DE DONDE VIENEN (charter, cliente, reguladores), que es del elegido. EL CABLEADO APUNTA AL OTRO (4 contra 3) y no manda.",
                "pasos": {
                    "1": ["INCISO", 1, "categorizar cada supuesto o restricción", ", y "],
                    "2": ["CUBIERTO", 3],
                    "3": ["CUBIERTO", 3],
                    "4": ["CUBIERTO", 4],
                    "5": ["INCISO", 4, "activo, pendiente, cerrado", ", que puede ser "],
                },
                "condiciones": {"1": ["CUBIERTO", 1]},
                "nota": "DOS PIEZAS DEL QUE MUERE VAN DE INCISO Y NINGUNA DE APPEND: CATEGORIZAR (su paso 1) es un gesto adosado al identificar que el superviviente ya manda, y LOS TRES ESTADOS (activo, pendiente, cerrado) son el parametro del estado que su paso 4 ya registra. Los dos pasos resultantes se leen limpios. CERO perdidas nombradas.",
            },
            {
                "orden": 12,
                "superviviente": "embudo_get_keep_grow",
                "motivo": "CONTENIDO, LAS DOS VARAS DE ACUERDO: pasos 6 contra 5 y condiciones 3 contra 2, las dos hacia embudo_get_keep_grow, con el cableado de acuerdo (12 contra 8). La razon del 292 le reconoce al elegido la etapa GROW entera y la actualizacion del lienzo.",
                "pasos": {
                    "1": ["INCISO", 2, "conciencia, interés, consideración, compra", ", con sus etapas de "],
                    "2": ["APPEND"],
                    "3": ["CUBIERTO", 6],
                    "4": ["INCISO", 3, "llamadas de seguimiento, encuestas de satisfacción, programas de lealtad", ", con tácticas como "],
                    "5": ["APPEND"],
                },
                "condiciones": {"1": ["CUBIERTO", 1], "2": ["APPEND"]},
                "nota": "DOS GESTOS DISTINTOS VIAJAN ENTEROS: elegir tacticas de medios ganados y pagados (paso 2) y medir el CAC contra el margen por venta (paso 5), que la razon nombra como el desglose propio del que muere. Sus pasos 1 y 4 van de INCISO porque lo propio son LAS ETAPAS DEL EMBUDO y LA LISTA DE TACTICAS, parametros de gestos que el superviviente ya manda. CERO perdidas nombradas.",
            },
            {
                "orden": 13,
                "superviviente": "analisis_motivaciones_fundador",
                "motivo": "CONTENIDO, UNA SOLA VARA NO EMPATADA: los pasos apuntan a analisis_motivaciones_fundador (4 contra 3) y las condiciones empatan 2 contra 2. El cableado esta de acuerdo (4 contra 2). La razon del 301 dice que el primero NOMBRA LAS TRECE MOTIVACIONES Y LOS PERFILES TIPICOS y que el segundo SE QUEDA EN LA TENSION ENTRE CONTROL Y RIQUEZA: el mismo ejercicio con distinto grado de detalle.",
                "pasos": {
                    "1": ["CUBIERTO", 1],
                    "2": ["INCISO", 2, "con una herramienta tipo CareerLeader", ", por ejemplo "],
                    "3": ["APPEND"],
                },
                "condiciones": {"1": ["APPEND"], "2": ["APPEND"]},
                "nota": "EL PASO 3 DEL QUE MUERE VIAJA ENTERO porque es su gesto propio declarado: el eje CONTROL CONTRA RIQUEZA y lo que pesa despues al repartir participacion y decidir quien manda. Las dos condiciones tambien viajan enteras: ninguna de las dos del superviviente habla de no tener claro POR QUE emprender ni de los roces con la familia. CERO perdidas nombradas.",
            },
            {
                "orden": 14,
                "superviviente": "asignacion_recursos_en_gates",
                "motivo": "EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO: pasos 4 contra 4, condiciones 2 contra 2, y la razon del 302 dice LA MISMA INSTRUCCION CON LOS MISMOS CUATRO GESTOS. El cableado apunta a asignacion_recursos_en_gates, 8 contra 4. NO es empate sin vara porque el cableado no empata.",
                "pasos": {
                    "1": ["INCISO", 2, "lista manual, hoja de cálculo o algún programa especializado", ", o bien "],
                    "2": ["CUBIERTO", 3],
                    "3": ["CUBIERTO", 1],
                    "4": ["APPEND"],
                },
                "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2]},
                "nota": "EL PASO 4 DEL QUE MUERE VIAJA ENTERO: comprometerse EN LA REUNION de forma explicita a asignar personas y presupuesto para la siguiente etapa es un gesto que los cuatro del superviviente no tienen (el suyo es EVITAR agregar proyectos sin resolver las implicaciones, que es la cara negativa). Su paso 1 va de INCISO porque lo propio son OTRAS TRES OPCIONES del mismo metodo. CERO perdidas nombradas.",
            },
        ],
    },
}


def cargar_jsonl(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def puertas():
    sem = set(json.load(io.open(os.path.join(RAIZ, "dataset", "metadata",
                                             "entry_seeds.json"),
                                encoding="utf-8")).get("seeds", []))
    packs = os.path.join(RAIZ, "packs")
    for d in sorted(os.listdir(packs)):
        q = os.path.join(packs, d, "metadata", "entry_seeds.json")
        if os.path.exists(q):
            sem.update(json.load(io.open(q, encoding="utf-8")))
    for d in sorted(os.listdir(packs)):
        q = os.path.join(packs, d, "metadata", "bridges_aprobados.json")
        if not os.path.exists(q):
            continue
        for x in json.load(io.open(q, encoding="utf-8")).get("aprobados", []):
            for extremo in ("core", "dominio"):
                if x.get(extremo):
                    sem.add(x[extremo])
    return sem


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lote", required=True)
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    tramo = {r["orden_tramo2"]: r for r in cargar_jsonl(TRAMO)}
    prot = puertas()
    lote = LOTES[a.lote]

    print("=" * 78)
    print("GENERADOR DEL PLAN DEL LOTE %s DEL TRAMO 2 (vuelta 54)" % a.lote)
    print("=" * 78)
    print()

    fallos = []
    actos = []
    for spec in lote["actos"]:
        n = spec["orden"]
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
        pa = oa.get("pasos_accionables") or []
        ca = oa.get("condiciones_activacion") or []
        ps = os_.get("pasos_accionables") or []
        cs = os_.get("condiciones_activacion") or []

        marcas_p, marcas_c = {}, {}
        for i, texto in enumerate(pa, 1):
            m = spec["pasos"].get(str(i))
            if not m:
                fallos.append("acto %d: el paso %d de %s no tiene marca" % (n, i, ab))
                continue
            if m[0] == "APPEND":
                marcas_p[str(i)] = "APPEND"
            elif m[0] == "CUBIERTO":
                if not (1 <= m[1] <= len(ps)):
                    fallos.append("acto %d: CUBIERTO:%d y el superviviente tiene %d pasos"
                                  % (n, m[1], len(ps)))
                marcas_p[str(i)] = "CUBIERTO:%d" % m[1]
            elif m[0] == "CUBIERTO_COND":
                marcas_p[str(i)] = "CUBIERTO_COND:%d" % m[1]
            elif m[0] == "INCISO":
                _, k, trozo, nexo = m
                if trozo not in texto:
                    fallos.append("acto %d: el INCISO %r NO es trozo verbatim del paso %d de %s"
                                  % (n, trozo, i, ab))
                if not (1 <= k <= len(ps)):
                    fallos.append("acto %d: INCISO al paso %d y el superviviente tiene %d"
                                  % (n, k, len(ps)))
                else:
                    print("  acto %-3d INCISO al paso %d, resultado:" % (n, k))
                    print("      %s" % (ps[k - 1] + nexo + trozo))
                marcas_p[str(i)] = "INCISO:%d|%s|%s" % (k, trozo, nexo)
            else:
                fallos.append("acto %d: marca desconocida %r" % (n, m))
        for i, texto in enumerate(ca, 1):
            m = spec["condiciones"].get(str(i))
            if not m:
                fallos.append("acto %d: la condicion %d de %s no tiene marca" % (n, i, ab))
                continue
            if m[0] == "APPEND":
                marcas_c[str(i)] = "APPEND"
            elif m[0] == "CUBIERTO":
                if not (1 <= m[1] <= len(cs)):
                    fallos.append("acto %d: CUBIERTO:%d y el superviviente tiene %d condiciones"
                                  % (n, m[1], len(cs)))
                marcas_c[str(i)] = "CUBIERTO:%d" % m[1]
            else:
                fallos.append("acto %d: marca de condicion desconocida %r" % (n, m))
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
    print("  incisos: todos VERBATIM dentro del paso que muere")

    plan = dict(CABECERA)
    plan["tramo"] = lote["titulo"]
    plan["actos"] = actos
    # EL CAMPO QUE EL EJECUTOR IMPRIME AL CERRAR Y QUE NO ES OPCIONAL: sin el,
    # vuelta49_fundir_tramo.py cae con KeyError DESPUES de haber hecho todas
    # las guardas en verde (le paso igual a la vuelta 53, correccion 1 de su
    # reporte). Aqui va SIEMPRE, aunque el lote no declare ninguno.
    plan["declarados_y_no_fundidos"] = lote.get("declarados", [])
    destino = os.path.join(SALIDA, "PLAN_V54_OPU01_LOTE_%s.json" % a.lote)
    if not a.simular:
        io.open(destino, "w", encoding="utf-8", newline=chr(10)).write(
            json.dumps(plan, ensure_ascii=False, indent=1) + chr(10))
        print("  escrito: %s" % destino)
    else:
        print("  SIMULACION: no se escribe")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
