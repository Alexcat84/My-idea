# -*- coding: utf-8 -*-
"""vuelta35_relecturas.py - LAS CINCO RELECTURAS DE P.5 DEL ACTO DE OP-D-03.

CONSTRUYE UNA PROPUESTA SELLADA Y NO ESCRIBE EN EL ARCHIVO. Y eso ultimo no es
timidez, es la regla 5 de EJECUTOR.md: la medicion de esta vuelta contradice una
cifra publicada con su corte (la vuelta 34 publico que los pares emitidos contra
texto muerto eran DOS, el 452 y el 1575; medidos hoy son CINCO y los cinco son A),
y lo que contradice una cifra publicada se declara como PARADA y no lo arregla el
ejecutor. La propuesta queda lista para que UN solo comando la vuelque el dia que
el fundador lo diga.

QUE HACE CADA GUARDA, y las seis estan escritas para caer:

  1. los seis nodos del acto tienen HOY los pasos que las razones nuevas dicen
     que tienen. Si no, aborta.
  2. cada par sigue registrado en el archivo y sigue en la clase que la propuesta
     espera. Si no, aborta.
  3. la razon vieja se copia DEL ARCHIVO POR MAQUINA, nunca se transcribe.
  4. la razon vieja queda LITERAL dentro de la nueva, y si no, aborta.
  5. las aristas internas se buscan EN LOS DOS SENTIDOS contra el grafo, y el
     resultado medido tiene que coincidir con lo que la razon nueva afirma.
  6. el marcador esperado tras el volcado se imprime ANTES de que nadie vuelque,
     con orden de parar si el instrumento diera otra cosa.

Uso: python scripts/loop/vuelta35_relecturas.py
Salida: docs/loop/PROPUESTA_V35_RELECTURAS.json (propuesta, NO lote aplicado)
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
PROPUESTA = os.path.join(RAIZ, "docs", "loop", "PROPUESTA_V35_RELECTURAS.json")

FECHA = "15 ago 2026"

PASOS_HOY = {
    "ab_testing_optimizacion": 5,
    "optimizacion_embudo_get_customers": 5,
    "split_testing_experimentos_ab": 5,
    "funnel_get_customers_optimizacion": 7,
    "split_testing": 4,
    "test_ab_precio": 5,
}

CABECERA = (
    "REESCRITA EL %s POR P.5, y la clase pasa de A a D. CORRECCION DECLARADA, con el texto "
    "viejo entero debajo. P.5 manda que cada acto se lea ENTERO DESPUES de su destejido y "
    "ANTES de su fusion, y escribe su motivo: leer un par cuyo nodo va a perder la mitad de "
    "sus pasos es leer algo que va a dejar de existir. Este par se leyo ANTES, y medido hoy "
    "con dos varas independientes (fecha de lectura contra fecha de cambio del fichero, y "
    "comparacion del texto de los pasos en el commit de la lectura contra el de hoy) resulta "
    "que %s. La relectura va contra el texto de hoy, con los dos nodos impresos ENTEROS "
    "delante y las aristas buscadas en LOS DOS SENTIDOS contra el grafo. " % (FECHA, "%s")
)

# El criterio se cita UNA vez y se nombra en las cinco, en vez de reescribirlo
# cinco veces distintas. Es el mismo que esta casa aplico al 738 el 15 ago 2026.
CRITERIO = (
    "EL CRITERIO NO SE INVENTA AQUI: es el que esta misma casa escribio en el 738 el 15 ago "
    "2026, sobre uno de estos mismos nodos, y dice que la MECANICA COMPARTIDA no basta y que "
    "el OBJETO decide. Alli se escribio asi: lo compartido es la mecanica, partir en dos, "
    "medir con las mismas metricas y comparar; uno optimiza una pagina y el otro decide si "
    "una funcionalidad merece existir; CONTINUA, D, los dos sanos. "
)

RELECTURAS = {
    452: {
        "clase_vieja": "A",
        "clase_nueva": "D",
        "rancio": ("ab_testing_optimizacion se leyo con QUINCE pasos y hoy tiene CINCO, "
                   "porque OP-F-04-WEI se llevo el bloque 11 a 15 al anillo interior y "
                   "OP-D-03 colapso la repeticion del 1 a 5 contra el 6 a 10"),
        "sin_arista": ("ab_testing_optimizacion", "split_testing"),
        "cuerpo": (
            "LO QUE LA RAZON VIEJA DABA POR COMPARTIDO Y HOY YA NO LO ESTA, medido paso por "
            "paso: aquella listaba cinco gestos comunes y el quinto era exigir confianza "
            "estadistica antes de concluir. ESE PASO YA NO EXISTE EN ab_testing_optimizacion. "
            "Vivia en el bloque 11 a 15 que OP-F-04-WEI se llevo, y hoy la exigencia de "
            "significancia por encima del 95 por ciento es del OTRO nodo y solo del otro. La "
            "razon vieja tambien describia el nodo como quince pasos partidos en tres "
            "narraciones del mismo test: esa descripcion ya no describe nada. "
            "LO QUE QUEDA COMPARTIDO, LEIDO HOY: definir las variaciones, repartir el trafico "
            "entre las dos versiones y medir la conversion de cada una. TRES gestos, y son la "
            "mecanica generica de cualquier prueba A/B. "
            "LO PROPIO DE ab_testing_optimizacion: el catalogo de elementos de la landing page "
            "que se prueban (botones, titulares, imagenes, ofertas, ubicacion de la llamada a "
            "la accion, texto, prueba social y numero de campos de formulario), elegir antes la "
            "metrica clave, cambiar un solo elemento a la vez, generar las hipotesis de cambios "
            "grandes antes que los ajustes pequenos, el reparto ochenta veinte en paginas de "
            "alto trafico, dejar correr durante semanas con una sola metrica a la vez, y cerrar "
            "el ciclo implementando la ganadora y pasando a la siguiente metrica cuando se "
            "agoten las ideas. "
            "LO PROPIO DE split_testing: el objeto, que no es la pagina sino la PROPUESTA DE "
            "VALOR (precio, texto, funcionalidades, empaquetado), la conversion medida sobre la "
            "llamada a la accion, y la significancia estadistica por encima del 95 por ciento. "
            "Y LOS ENTREGABLES LO DICEN, leidos hoy en los dos ficheros: plan de pruebas A/B con "
            "elementos priorizados y decision sobre la version ganadora, contra resultados "
            "comparativos de conversion entre variantes con significancia estadistica. "
            + CRITERIO +
            "AQUI: uno optimiza los elementos de una pagina para subir la activacion, el otro "
            "compara alternativas de propuesta de valor para decidir cual se ofrece. CONTINUA: "
            "D, los dos sanos. "
            "ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS CONTRA EL GRAFO: NO HAY NINGUNA. Y NO SE "
            "DECLARA ARISTA QUE FALTA, por el criterio escrito el 15 ago 2026 en "
            "02_DESTEJIDOS.md: la arista se declara donde lo compartido es un BLOQUE que uno "
            "expande de una LINEA del otro, y aqui es LINEA CONTRA LINEA, dos procedimientos "
            "completos de cinco y cuatro pasos que comparten una mecanica generica. "
            "DISCUTIBLE MARCADO: quien lea los dos titulos vera dos nodos que ensenan A/B "
            "testing, y dira que el catalogo no deberia tener dos. Lo que sostengo es que el "
            "objeto los separa, y es el mismo corte que el 738 aplico entre estos mismos "
            "vecinos. Pero es una lectura, y va marcada."
        ),
    },
    1575: {
        "clase_vieja": "A",
        "clase_nueva": "D",
        "rancio": ("ab_testing_optimizacion se leyo con QUINCE pasos y hoy tiene CINCO"),
        "sin_arista": ("ab_testing_optimizacion", "test_ab_precio"),
        "cuerpo": (
            "LA RAZON VIEJA SE APOYA EN UNA FRASE QUE HOY ES FALSA, y por eso el par se relee: "
            "decia que los cinco pasos de test_ab_precio tienen su correspondiente DENTRO DE LOS "
            "QUINCE de ab_testing_optimizacion. No hay quince. Y de las perdidas que aquella "
            "razon proponia por el lado de ab_testing_optimizacion, DOS YA NO ESTAN EN EL NODO, "
            "medidas hoy sobre el fichero: MEDIR CON CONFIANZA ESTADISTICA antes de concluir, y "
            "documentar las tacticas exitosas para escalarlas HASTA LA SATURACION. Las dos "
            "vivian en el bloque que OP-F-04-WEI se llevo al anillo interior. Una razon que "
            "propone perder material que el nodo ya no tiene no esta midiendo el nodo. "
            "LO QUE QUEDA COMPARTIDO, LEIDO HOY: definir las variantes, llevarlas a un canal "
            "real, medir cual convierte mas y quedarse con la ganadora. Cuatro gestos que son la "
            "mecanica generica de la prueba A/B. "
            "LO PROPIO DE test_ab_precio, y es lo que decide: el OBJETO ES LA FORMA DE COBRAR, "
            "precio de venta contra modelo de renta, y el procedimiento es una BUSQUEDA "
            "ITERATIVA DE UN VALOR OPTIMO por multiples rondas, no un duelo entre dos versiones. "
            "Su entregable, leido hoy: un precio o modelo de monetizacion validado con datos de "
            "conversion reales. "
            "LO PROPIO DE ab_testing_optimizacion: los elementos de la landing page, un solo "
            "elemento a la vez, el reparto del trafico, las semanas con una sola metrica, y el "
            "paso a la metrica siguiente. Su entregable: plan de pruebas A/B con elementos "
            "priorizados. "
            + CRITERIO +
            "AQUI: uno optimiza los elementos de una pagina, el otro decide CUANTO Y COMO SE "
            "COBRA. CONTINUA: D, los dos sanos. "
            "ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS CONTRA EL GRAFO: NO HAY NINGUNA, y no se "
            "declara arista que falta: es linea contra linea, no un bloque que expande una "
            "linea. "
            "DISCUTIBLE MARCADO: test_ab_precio se puede leer como la prueba A/B general "
            "aplicada al precio, y quien la lea asi dira madre e hijo y pedira A o arista. Lo "
            "que lo impide es que ab_testing_optimizacion no es la prueba general: es la prueba "
            "aplicada a OTRO objeto, la pagina. Dos hijos de una misma madre no son madre e hijo "
            "entre si."
        ),
    },
    1571: {
        "clase_vieja": "A",
        "clase_nueva": "D",
        "rancio": ("split_testing_experimentos_ab se leyo con NUEVE pasos y hoy tiene CINCO, "
                   "porque OP-F-04-RAC se llevo su bloque 6 a 9 a "
                   "metodologia_evaluacion_entrenamiento_ventas"),
        "sin_arista": ("split_testing_experimentos_ab", "test_ab_precio"),
        "cuerpo": (
            "ESTA ES LA RELECTURA MAS CLARA DE LAS CINCO, porque la razon vieja nombro con "
            "detalle un material que hoy no esta en el nodo. Decia: de "
            "split_testing_experimentos_ab se perderia el RIGOR ESTADISTICO ENTERO, elegir un "
            "grupo de control con desempeno inicial similar, medir en el mismo periodo bajo las "
            "mismas condiciones de mercado, comparar el cambio porcentual y no los valores "
            "absolutos, y reportar la diferencia neta entre grupos. MEDIDO HOY SOBRE EL FICHERO: "
            "NINGUNA DE LAS CUATRO ESTA. Las cuatro salieron con OP-F-04-RAC hacia "
            "metodologia_evaluacion_entrenamiento_ventas, y el propio campo preservar de OP-D-03 "
            "lo tiene escrito. La razon vieja estaba pesando en un platillo material que el nodo "
            "ya entrego a otra ficha. "
            "LO QUE QUEDA COMPARTIDO, LEIDO HOY: definir la variante, partir en dos grupos, "
            "medir los dos y comparar. La mecanica generica, otra vez. "
            "LO PROPIO DE split_testing_experimentos_ab: la HIPOTESIS SOBRE EL IMPACTO DE UNA "
            "FUNCIONALIDAD NUEVA, partir LA BASE DE CLIENTES y no el trafico, dejar al grupo A "
            "con la version estandar, y concluir si la funcionalidad tuvo impacto real en el "
            "comportamiento. Su entregable, leido hoy: reporte de un experimento A/B con "
            "conclusiones sobre el impacto de una funcionalidad. "
            "LO PROPIO DE test_ab_precio: el precio contra el modelo de renta, el canal real, "
            "las multiples rondas para afinar el valor optimo, y el precio validado como "
            "entregable. "
            + CRITERIO +
            "AQUI: uno decide si una funcionalidad merece existir, el otro decide cuanto se "
            "cobra. Es literalmente el mismo corte del 738, con el mismo nodo de un lado. "
            "CONTINUA: D, los dos sanos. "
            "ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS CONTRA EL GRAFO: NO HAY NINGUNA, y no se "
            "declara arista que falta: linea contra linea. "
            "DISCUTIBLE MARCADO: la razon vieja cerraba diciendo que esta A reforzaba al 643. Al "
            "voltear esta, el 643 se queda sin ese refuerzo y sigue en A sin haber sido releido, "
            "porque sus dos nodos no cambiaron de texto y P.5 no lo alcanza. Queda dicho."
        ),
    },
    374: {
        "clase_vieja": "A",
        "clase_nueva": "D",
        "rancio": ("split_testing_experimentos_ab se leyo con NUEVE pasos y hoy tiene CINCO"),
        "sin_arista": ("split_testing", "split_testing_experimentos_ab"),
        "cuerpo": (
            "LA RAZON VIEJA SOSTENIA LA A EN UNA SIMETRIA QUE HOY ESTA ROTA POR UN LADO. Decia: "
            "el primero exige significancia estadistica por encima del 95 por ciento y el "
            "segundo insiste en comparar el cambio porcentual y no los valores absolutos, que "
            "son dos maneras de pedir lo mismo. MEDIDO HOY: la primera mitad sigue en pie y LA "
            "SEGUNDA NO ESTA EN EL NODO. El cambio porcentual salio con OP-F-04-RAC. Tambien "
            "decia que el segundo tiene nueve pasos y se parte por la mitad, del 6 al 9 "
            "repitiendo lo del 2 al 5: esa costura ya se destejio y el nodo tiene cinco pasos. "
            "La razon vieja se apoyaba en las dos cosas que la fase 01 se llevo. "
            "LO QUE QUEDA COMPARTIDO, LEIDO HOY: definir la variacion, partir en dos, medir con "
            "las mismas metricas y comparar. La mecanica generica. "
            "LO PROPIO DE split_testing: el objeto son las ALTERNATIVAS DE PROPUESTA DE VALOR "
            "(precio, texto, funcionalidades, empaquetado), la conversion se mide sobre la "
            "llamada a la accion, y la conclusion exige significancia por encima del 95 por "
            "ciento. "
            "LO PROPIO DE split_testing_experimentos_ab: la hipotesis sobre una FUNCIONALIDAD "
            "NUEVA, partir la BASE DE CLIENTES y no el trafico, y concluir sobre el impacto en "
            "el comportamiento. "
            + CRITERIO +
            "AQUI: uno compara alternativas de oferta, el otro decide si una funcionalidad nueva "
            "merece existir. CONTINUA: D, los dos sanos. "
            "ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS CONTRA EL GRAFO: NO HAY NINGUNA, y no se "
            "declara arista que falta: linea contra linea, y los dos tienen cableado propio. "
            "DISCUTIBLE MARCADO: es el par de titulos mas parecidos del acto, Split Testing "
            "contra Split-Testing (Pruebas A/B), y el parecido de nombre empuja a la A. Lo que "
            "sostengo es que el nombre no es la vara, y que tras las dos cirugias el texto ya no "
            "repite."
        ),
    },
    277: {
        "clase_vieja": "A",
        "clase_nueva": "D",
        "rancio": ("optimizacion_embudo_get_customers se leyo con DIEZ pasos y hoy tiene "
                   "CINCO, porque OP-F-04-WEI se llevo su bloque 6 a 10"),
        "sin_arista": ("funnel_get_customers_optimizacion", "optimizacion_embudo_get_customers"),
        "cuerpo": (
            "Y ESTE ES EL CASO EXTREMO DE LA TANDA, porque la razon vieja listaba CINCO gestos "
            "compartidos y HOY NINGUNO DE LOS CINCO ESTA EN LOS DOS NODOS. Medidos uno por uno "
            "sobre los ficheros de hoy: revisar los programas ya corriendo es el paso 1 de "
            "funnel_get_customers_optimizacion y NO ESTA en optimizacion_embudo_get_customers; "
            "escalar primero el mas productivo es su paso 2 y TAMPOCO ESTA; ejecutar pruebas A/B "
            "controladas cambiando no mas de dos variables es el paso 3 de "
            "optimizacion_embudo_get_customers y NO ESTA en funnel, cuyo paso 3 manda otra cosa, "
            "disenar tests pass fail para los programas mas decepcionantes; comparar LTV contra "
            "el costo de adquisicion antes de escalar es el paso 4 de "
            "optimizacion_embudo_get_customers, mientras que el paso 4 de funnel es un gesto "
            "distinto, identificar el comportamiento de los clientes de alto LTV para buscar "
            "mas parecidos; e iterar es el paso 5 de optimizacion_embudo_get_customers y funnel "
            "no lo manda, su cierre es no optimizar demasiados programas a la vez. LA "
            "COINCIDENCIA QUE SOSTENIA LA A VIVIA EN EL BLOQUE 6 A 10 QUE OP-F-04-WEI SE LLEVO. "
            "Y LA NOTA LATERAL DE LA RAZON VIEJA TAMBIEN ENVEJECIO: decia que el segundo es el "
            "nodo que nombra Visual Website Optimizer, marca muerta. Medido hoy sobre los cinco "
            "pasos, esa mencion YA NO ESTA en el nodo. "
            "LO QUE HOY SON, LEIDOS ENTEROS: funnel_get_customers_optimizacion es un TRIAJE "
            "PROGRAMA POR PROGRAMA sobre los canales de adquisicion, revisar cada programa get, "
            "escalar el mas productivo, poner pass fail a los peores, buscar parecidos a los "
            "clientes de alto LTV, probar ofertas e incentivos, revisar a diario las diez o doce "
            "metricas con el jefe de datos, y no tocar demasiados programas a la vez. "
            "optimizacion_embudo_get_customers es un LAZO DE OPTIMIZACION CON PUERTA ECONOMICA, "
            "exigir el MVP de alta fidelidad y el dashboard antes de empezar, definir las "
            "metricas segun el tipo de negocio web, correr las pruebas A/B controladas, "
            "comprobar que el LTV supera al CAQ antes de escalar la inversion, e iterar. "
            "MISMO OBJETO, DOS PROCEDIMIENTOS DISTINTOS Y COMPLEMENTARIOS. Eso es CONTINUA, no "
            "repite. D, los dos sanos. "
            "ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS CONTRA EL GRAFO: NO HAY NINGUNA. Y NO SE "
            "DECLARA ARISTA QUE FALTA: no hay un bloque que expanda una linea del otro, hay dos "
            "mitades que se tocan por el objeto y no por el texto. "
            "PENDIENTE DE DOCTRINA MARCADO EN LA PROPIA RAZON, por la regla 5 de EJECUTOR.md: "
            "estos dos ids son el mismo nombre en dos idiomas, Optimizacion del Embudo Get "
            "Customers y Optimizacion del Embudo Conseguir Clientes, y quedan los dos vivos en "
            "el catalogo sin repeticion de texto que los funda. NINGUNA PAGINA DICE QUE EL "
            "NOMBRE SOLO FUNDA. Si el catalogo no quiere dos nodos con el mismo nombre, eso es "
            "una decision de nomenclatura y no un veredicto de repeticion, y no la tomo yo. "
            "DISCUTIBLE MARCADO, Y ES EL MAS FUERTE DE LA TANDA: es el unico par donde el objeto "
            "SI coincide, y donde lo que separa es el procedimiento. En los otros cuatro pasa al "
            "reves. Quien sostenga que el objeto manda sobre el procedimiento dira que este "
            "sigue siendo A, y no tendra que forzar nada para decirlo."
        ),
    },
}


def leer_nodo(nid):
    return json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))


def main():
    print("=" * 78)
    print("GUARDA 1: los pasos de hoy, contra lo que las razones nuevas afirman")
    print("=" * 78)
    G = {}
    for nid, esperado in sorted(PASOS_HOY.items()):
        d = leer_nodo(nid)
        G[nid] = d
        real = len(d.get("pasos_accionables") or [])
        print("  %-38s %2d pasos (la razon dice %d)  %s"
              % (nid, real, esperado, "OK" if real == esperado else "ABORTA"))
        if real != esperado:
            return 1

    print("\n" + "=" * 78)
    print("GUARDA 5: las aristas internas, buscadas EN LOS DOS SENTIDOS")
    print("=" * 78)
    for puesto, r in sorted(RELECTURAS.items()):
        a, b = r["sin_arista"]
        da, db = G[a], G[b]
        hay = (b in (da.get("nodos_siguientes") or []) or b in (da.get("nodos_previos") or [])
               or a in (db.get("nodos_siguientes") or []) or a in (db.get("nodos_previos") or []))
        print("  %-5d %-36s contra %-36s arista: %s  %s"
              % (puesto, a, b, "SI" if hay else "NO", "ABORTA" if hay else "OK"))
        if hay:
            print("       la razon nueva afirma que NO hay ninguna, y el grafo dice que si.")
            return 1

    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_puesto = {v["puesto_intra"]: v for v in V}

    print("\n" + "=" * 78)
    print("GUARDAS 2, 3 y 4: clase esperada, razon vieja copiada por maquina y literal dentro")
    print("=" * 78)
    filas = []
    for puesto in sorted(RELECTURAS):
        r = RELECTURAS[puesto]
        v = por_puesto.get(puesto)
        if v is None:
            print("ABORTA: el puesto %d no esta registrado en el archivo" % puesto)
            return 1
        if v["clase"] != r["clase_vieja"]:
            print("ABORTA: el puesto %d esta en %r y la propuesta esperaba %r"
                  % (puesto, v["clase"], r["clase_vieja"]))
            return 1
        razon_vieja = v["razon"]
        razon = (CABECERA % r["rancio"]
                 + "LO QUE DECIA LA RAZON VIEJA, y se deja escrita ENTERA para que la correccion "
                   "se pueda auditar (copiada del archivo por maquina, no transcrita): "
                 + razon_vieja + " FIN DE LA RAZON VIEJA. "
                 + r["cuerpo"])
        if razon_vieja not in razon:
            print("ABORTA: la razon vieja del %d no queda literal dentro de la nueva" % puesto)
            return 1
        filas.append({"puesto": puesto, "clase": r["clase_nueva"], "razon": razon})
        print("  %-5d %s -> %s   razon vieja %5d caracteres, literal dentro de %5d  OK"
              % (puesto, r["clase_vieja"], r["clase_nueva"], len(razon_vieja), len(razon)))

    with io.open(PROPUESTA, "w", encoding="utf-8") as fh:
        json.dump({
            "vuelta": 35,
            "fecha": FECHA,
            "estado": "PROPUESTA NO VOLCADA. Espera decision del fundador (PARADA de la vuelta 35).",
            "regla": "P.5 del BANCO_DEL_PLAN, con la regla 5 de EJECUTOR.md para no volcarla solo",
            "filas": filas,
        }, fh, ensure_ascii=False, indent=2)
    print("\nESCRITA LA PROPUESTA: %s (%d filas). NO SE VOLCO NADA."
          % (os.path.relpath(PROPUESTA, RAIZ), len(filas)))

    print("\n" + "=" * 78)
    print("GUARDA 6: el marcador de hoy y el que quedaria, escrito ANTES de que nadie vuelque")
    print("=" * 78)
    conteo = {}
    for v in V:
        conteo[v["clase"]] = conteo.get(v["clase"], 0) + 1
    print("  MARCADOR DE HOY, contado aqui:      n %d, A %d, B %d, C %d, D %d"
          % (len(V), conteo.get("A", 0), conteo.get("B", 0), conteo.get("C", 0), conteo.get("D", 0)))
    print("  MARCADOR SI SE VOLCARAN LAS CINCO:  n %d, A %d, B %d, C %d, D %d"
          % (len(V), conteo.get("A", 0) - 5, conteo.get("B", 0), conteo.get("C", 0),
             conteo.get("D", 0) + 5))
    print("  Si el dia del volcado el instrumento diera otra cosa, SE PARA.")

    print("\n" + "=" * 78)
    print("LA FORMA DEL ACTO SI LAS CINCO SE VOLCARAN, computada y no dibujada")
    print("=" * 78)
    a_vivas = []
    for v in V:
        if v["clase"] != "A":
            continue
        if v["nodo_a"] in PASOS_HOY and v["nodo_b"] in PASOS_HOY:
            if v["puesto_intra"] not in RELECTURAS:
                a_vivas.append((v["puesto_intra"], v["nodo_a"], v["nodo_b"]))
    print("  pares A que quedarian DENTRO del acto: %d" % len(a_vivas))
    for p, a, b in sorted(a_vivas):
        print("    %-5d %s contra %s" % (p, a, b))
    dentro = set()
    for _, a, b in a_vivas:
        dentro.add(a)
        dentro.add(b)
    fuera = sorted(set(PASOS_HOY) - dentro)
    print("  nodos que seguirian en el cierre transitivo: %d -> %s" % (len(dentro), sorted(dentro)))
    print("  nodos que SALDRIAN del acto: %d -> %s" % (len(fuera), fuera))
    print("\n  P.6 manda que la nomina de ACTO se COMPUTA y no admite gusto: si las cinco se")
    print("  vuelcan, el acto de SEIS deja de existir y queda un acto de DOS. El paso 2 del")
    print("  orden interno de OP-D-03, decidir sobre los seis, se quedaria sin los seis.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
