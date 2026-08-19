# -*- coding: utf-8 -*-
"""vuelta45_plan_opd08.py - EL PLAN SELLADO DE OP-D-08, CONSTRUIDO CONTRA EL GRAFO.

ESTRICTAMENTE DE SOLO LECTURA sobre dataset/nodos: escribe UN fichero, el plan,
en docs/loop/PLAN_V45_OPD08.json. No toca un solo nodo.

LO UNICO TECLEADO AQUI son los GRUPOS (destino <- origenes), el texto del
resultado y el motivo de cada uno. TODO LO DEMAS SE MIDE del grafo: los prefijos
de guarda, los conteos, la fuente y la cobertura. Es la forma asentada de los
actos de OP-D-06 (scripts/loop/vuelta41_plan_acto.py con scripts/loop/v41_actos/)
aplicada a un DESTEJIDO SOLO, que tiene un solo nodo y ningun superviviente que
elegir.

El plan lo ejecuta scripts/loop/vuelta32_podar.py, que es el destejedor de la
casa para una costura interna de fuente unica, con sus guardas: conteo, fuente,
prefijo de TODOS los pasos, cobertura exacta 1..N sin huecos ni repetidos,
procedencia completa y el final de fichero tal cual.

Uso: python scripts/loop/vuelta45_plan_opd08.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
DESTINO = os.path.join(RAIZ, "docs", "loop", "PLAN_V45_OPD08.json")

NODO = "lienzo_modelo_negocio"
FUENTE = "Business Model Generation - Osterwalder"

OPERACION = ("OP-D-08: el destejido de lienzo_modelo_negocio, DESTEJIDO SOLO, "
             "sin fusion acoplada y sin superviviente que elegir")

REGLA = (
    "OP-D-08 de docs/plan/OPERACIONES.jsonl, leida ENTERA hoy antes de tocar nada. "
    "REMEDIO: REPARTO Y NO PODA, por P.3, porque las CUATRO narraciones del Canvas "
    "son del MISMO tema. COLUMNA VERTEBRAL: la enumeracion de los pasos 13 a 17, y "
    "no se elige por gusto: la senala la simulacion de la vuelta 17, que tumbo las "
    "otras tres (tres de las cuatro rompen el veredicto 1434). REGLA DE REPARTO de "
    "la fase: cada perdida al bloque del que proviene, y la que no tenga bloque al "
    "superviviente, que en un destejido solo es el propio nodo.")

MOTIVO = (
    "LA PREGUNTA PENDIENTE DE LA OPERACION SE RESUELVE EN LA LECTURA, que es lo que "
    "el acta de la vuelta 44 adjudico (seccion 4 punto 2, linea 9672): su "
    "pregunta_pendiente es un CONDICIONAL CON LAS DOS RAMAS YA LEGISLADAS y su "
    "propio texto dice que decidirla exige leer el nodo con el ojo puesto en esa "
    "frase. LEIDO HOY DE CERO (docs/loop/SALIDA_V45_OPD08_LECTURA.txt), CON LA CITA "
    "DELANTE. El paso 5 dice, literal: 'Completar cada uno de los 9 bloques del "
    "canvas para la solucion disenada'. LA RESOLUCION ES: ES UN MARCO PROPIO, y por "
    "tanto es material propio del bloque 2 y SE REPARTE COMO EL RESTO, no se va con "
    "su bloque. LA PRUEBA NO ES DE GUSTO, ES DEL PROPIO TEXTO DEL NODO Y ESTA "
    "MEDIDA: la condicion_activacion 3 del nodo dice, con sus palabras, 'Cuando una "
    "solucion de diseno necesita convertirse en un modelo de negocio viable', y la "
    "4 dice 'Al pasar de idea a implementacion'. O sea que el nodo YA LEGISLA ese "
    "momento como una de sus SIETE puertas, y la frase del paso 5 nombra "
    "exactamente esa puerta. Y LA CONTRAPRUEBA, tambien del texto: NINGUNA de las "
    "otras tres narraciones trae acotacion de momento (la 1 es una sesion "
    "colaborativa generica, la 3 es una sesion de equipo que acepta vacios, la 4 es "
    "el recorrido bloque por bloque); la del paso 5 es la UNICA que dice PARA QUE "
    "estado del proyecto se completa el lienzo. La vara que la propia operacion "
    "escribio es 'aplicar el lienzo a una solucion ya disenada, QUE ES UN MOMENTO "
    "DISTINTO DEL PROYECTO', y el nodo lo declara distinto por su cuenta. "
    "DONDE ATERRIZA, y tambien por regla y no por gusto: su bloque (el 2) "
    "desaparece entero, asi que la pieza NO TIENE BLOQUE y por la regla de reparto "
    "va AL SUPERVIVIENTE. Dentro del superviviente se adosa al paso 4, que es el "
    "unico cuyo objeto ES PARA QUE SE USA EL LIENZO ('usar el lienzo como base para "
    "pivotar o validar hipotesis'): adosarla ahi NO le cambia el objeto a ningun "
    "paso, que es la condicion que OP-D-02 dejo escrita para decidir entre adosar y "
    "abrir paso nuevo (02_DESTEJIDOS.md linea 514). VA COMO DISCUTIBLE MARCADO. "
    "EL RESTO DEL REPARTO EJECUTA LO ESCRITO, sin margen: sobrevive UNA SOLA orden "
    "de completar los nueve bloques, la enumeracion de 13 a 17, conservada ENTERA, "
    "CONTIGUA y EN ORDEN como columna vertebral; se van como linea los pasos 5, 6, "
    "7 y 8 (el bloque 2) y el 9 en su forma actual (se funde con el 1 en una sola "
    "linea con sus dos formatos, que es lo que preservar manda); y de las otras dos "
    "narraciones sobrevive TODA su practica propia (la clausula de las notas "
    "post-it del paso 2, que es el ancla del veredicto 1136; el iterar en grupo del "
    "3; el usar para pivotar del 4; el reunirse aceptando vacios del 10; el pausar "
    "para investigar del 11; y el publicar y actualizar del 12), despojadas de la "
    "orden repetida que cada una arrastraba. NINGUNA LINEA DE CONTENIDO PROPIO SE "
    "ELIMINA, y cada una se comprueba EN SU CASA antes de quitarla y no despues: "
    "los tres pasos de contenido del bloque 2 (6 socios y actividades, 7 canales y "
    "relaciones y segmentos, 8 costos e ingresos) viajan cada uno CON el paso de la "
    "enumeracion que ya los dice, y eso se ve en el mapa, que es donde una "
    "comprobacion se puede auditar. "
    "LAS CONDICIONES NO SE TOCAN, y se dice por que en vez de callarlo: esta "
    "operacion legisla PASOS y solo pasos (su eliminar y su preservar nombran pasos "
    "en todas sus lineas), asi que tocar el campo condiciones_activacion seria hacer "
    "trabajo que la operacion no ordena. Y ademas la condicion 3 es LA EVIDENCIA de "
    "la resolucion de arriba: moverla seria destruir la prueba que sostiene el "
    "reparto. Las 7 se quedan tal cual. "
    "LA FUENTE NO SE TOCA: es UNICA (Osterwalder) y ningun bloque sale del nodo, "
    "porque este destejido no tiene destino, solo repetido que colapsar.")

# ---------------------------------------------------------------------------
# LOS GRUPOS: (destino, [origenes], texto del resultado, motivo).
# El texto de los VERBATIM se lee del grafo en vez de teclearse: se marcan con
# None y el constructor los copia del origen que se indica.
# ---------------------------------------------------------------------------
GRUPOS = [
    ([1, 9], None, None,
     "LAS DOS ORDENES DE IMPRIMIR SE FUNDEN EN UNA SOLA LINEA CON SUS DOS FORMATOS, "
     "que es literalmente lo que preservar manda: 'imprimir un canvas para CADA "
     "MIEMBRO del equipo (paso 9), que es la SEGUNDA orden de imprimir del nodo y se "
     "funde con la del paso 1 en una sola linea con sus dos formatos'. Separarlas "
     "dejaria dos pasos que mandan imprimir lo mismo, que es lo que este destejido "
     "existe para quitar; fundirlas no pierde ninguno de los dos formatos, porque los "
     "dos quedan nombrados."),
    ([10], None, None,
     "LA SESION DE EQUIPO, PRACTICA PROPIA DE LA TERCERA NARRACION Y DE NINGUNA OTRA, "
     "despojada de la orden repetida que arrastraba. El original decia 'Reunirse con "
     "el equipo PARA COMPLETAR LAS SECCIONES DEL CANVAS, aceptando que habra vacios "
     "en la primera version': la mitad de completar las secciones es la TERCERA copia "
     "sobrante de la orden y se va; lo que se conserva entero es lo unico que ninguna "
     "otra narracion dice, ACEPTAR QUE HABRA VACIOS EN LA PRIMERA VERSION, que es la "
     "linea que da permiso para empezar sin saberlo todo. Va la segunda porque es la "
     "sesion dentro de la cual se llena el lienzo."),
    ([2], None, None,
     "LA CLAUSULA DE LAS NOTAS POST-IT, QUE ES EL ANCLA DEL VEREDICTO 1136 y por eso "
     "preservar la nombra una por una. El original decia 'COMPLETAR CADA UNO DE LOS 9 "
     "BLOQUES usando notas post-it': la primera mitad es la PRIMERA copia sobrante de "
     "la orden y se va con las otras dos; la segunda mitad es el FORMATO de trabajo, "
     "que no lo dice ninguna otra narracion, y se queda. Queda como paso de formato y "
     "no de orden, que es exactamente el reparto que P.3 manda cuando el bloque "
     "pegado es del mismo tema: se reparte la practica propia y se quita la "
     "repeticion."),
    ([13], None, 13,
     "COLUMNA VERTEBRAL, PRIMERA DE CINCO, VERBATIM. La enumeracion de 13 a 17 es la "
     "UNICA orden de completar los nueve bloques que sobrevive, y la eleccion no es "
     "de esta vuelta: la senalo la simulacion de la vuelta 17, que probo las cuatro "
     "narraciones conservadas solas y tumbo tres. Se conserva ENTERA, CONTIGUA y EN "
     "ORDEN, porque una columna vertebral partida deja de serlo."),
    ([14], None, 14,
     "COLUMNA VERTEBRAL, SEGUNDA DE CINCO, VERBATIM, Y EL PASO INTOCABLE DE LA "
     "OPERACION: 'definir la propuesta de valor para cada segmento' es el ancla del "
     "veredicto 1434 (D contra value_proposition_canvas), y es el UNICO de los tres "
     "veredictos que citan pasos de este nodo cuya razon NO se declara invariante. Si "
     "el destejido se lo llevara, el 1434 dejaria de sostenerse. No se toca ni una "
     "palabra."),
    ([7, 15], None, 15,
     "COLUMNA VERTEBRAL, TERCERA DE CINCO, VERBATIM, Y AQUI VIAJA UNO DE LOS TRES "
     "PASOS DE CONTENIDO DEL BLOQUE 2, comprobado EN SU CASA antes de quitarlo. El "
     "paso 7 decia 'Especificar canales, relaciones y segmentos de clientes' y sus "
     "tres piezas estan las tres dichas por la enumeracion mas fina: canales y "
     "relaciones aqui, en el 15, y segmentos en el 13, que es el destino anterior. Se "
     "asigna a este grupo porque es donde calzan DOS de sus tres piezas, y la tercera "
     "queda comprobada en el destino de al lado, a la vista en este mismo mapa."),
    ([6, 16], None, 16,
     "COLUMNA VERTEBRAL, CUARTA DE CINCO, VERBATIM, CON EL SEGUNDO PASO DE CONTENIDO "
     "DEL BLOQUE 2 COMPROBADO EN SU CASA. El paso 6 decia 'Definir socios clave y "
     "actividades necesarias para entregar la propuesta de valor' y el 16 manda "
     "'Mapear recursos, actividades y asociaciones clave': socios son las "
     "asociaciones y actividades son las actividades, o sea que el 16 dice lo del 6 y "
     "ademas los recursos, que el 6 no tenia. La propuesta de valor a la que el 6 "
     "apunta la define el destino anterior, el del paso 14."),
    ([8, 17], None, 17,
     "COLUMNA VERTEBRAL, QUINTA DE CINCO, VERBATIM, CON EL TERCER Y ULTIMO PASO DE "
     "CONTENIDO DEL BLOQUE 2 COMPROBADO EN SU CASA. El paso 8 decia 'Estimar "
     "estructura de costos y fuentes de ingresos': los costos los manda calcular este "
     "mismo 17 y las fuentes de ingresos las mapea el 15, dos destinos mas arriba. "
     "Con esto los TRES pasos de contenido del bloque 2 quedan comprobados uno a uno "
     "en su casa, que es lo que el eliminar de la operacion exige ANTES de quitarlos "
     "y no despues."),
    ([11], None, 11,
     "PRACTICA PROPIA DE LA TERCERA NARRACION, VERBATIM, y no la dice ninguna otra: "
     "PAUSAR PARA INVESTIGAR donde haya vacios importantes. Es la contrapartida de "
     "aceptar los vacios: sin ella el permiso para empezar incompleto se queda en "
     "permiso para quedarse incompleto."),
    ([3], None, 3,
     "PRACTICA PROPIA DE LA PRIMERA NARRACION, VERBATIM: iterar y discutir EN GRUPO "
     "hasta lograr COHERENCIA ENTRE LOS BLOQUES. Es la linea que sostiene la segunda "
     "mitad del entregable del nodo ('los 9 bloques definidos Y COHERENTES ENTRE SI'), "
     "asi que quitarla dejaria el entregable diciendo algo que ningun paso produce."),
    ([12], None, 12,
     "PRACTICA PROPIA DE LA TERCERA NARRACION, VERBATIM, y la unica linea del nodo "
     "que habla de DESPUES de la sesion: publicar el canvas en el espacio de trabajo "
     "y ACTUALIZARLO conforme avanza el proyecto. Va cerca del final porque es lo que "
     "sigue vivo cuando la reunion termina."),
    ([4, 5], None, None,
     "PRACTICA PROPIA DE LA PRIMERA NARRACION MAS EL MARCO RESUELTO DE LA SEGUNDA, y "
     "es el unico grupo del acto donde la pregunta_pendiente aterriza. El paso 4 "
     "('usar el lienzo como base para pivotar o validar hipotesis del negocio') es el "
     "UNICO paso del nodo cuyo objeto es PARA QUE SE USA EL LIENZO, asi que el marco "
     "del paso 5 (aplicarlo a una solucion ya disenada) entra aqui SIN CAMBIARLE EL "
     "OBJETO a nada, que es la condicion escrita para adosar en vez de abrir paso "
     "nuevo. El vocabulario del anadido no se inventa: sale de la condicion_activacion "
     "3 del propio nodo, 'cuando una solucion de diseno necesita convertirse en un "
     "modelo de negocio viable'. Va el ultimo porque es el paso que dice para que "
     "sirvio todo lo anterior."),
]

# Los textos que NO son verbatim, tecleados aparte para que se vean solos.
TEXTOS = {
    1: u"Imprimir el lienzo en tamaño grande para trabajo colaborativo y un "
       u"Business Model Canvas para cada miembro del equipo",
    2: u"Escribir cada bloque en notas post-it sobre el lienzo",
    10: u"Reunirse con el equipo aceptando que habrá vacíos en la primera "
        u"versión",
}
TEXTO_MARCO = (u"Usar el lienzo como base para pivotar o validar hipótesis del "
               u"negocio, y también para llevar una solución ya "
               u"diseñada a un modelo de negocio viable")


def main():
    d = json.loads(io.open(os.path.join(NODOS, NODO + ".json"), encoding="utf-8").read())
    pasos = list(d.get("pasos_accionables") or [])
    cond = list(d.get("condiciones_activacion") or [])

    assert d.get("fuente") == FUENTE, "la fuente de hoy no es la esperada"

    mapa = {}
    finales = []
    filas = []
    for i, (origenes, _, verbatim_de, motivo) in enumerate(GRUPOS, 1):
        if verbatim_de is not None:
            texto = pasos[verbatim_de - 1]
            marca = "VERBATIM del paso %d" % verbatim_de
        elif origenes == [4, 5]:
            texto = TEXTO_MARCO
            marca = "con remedio (el marco resuelto)"
        else:
            texto = TEXTOS[origenes[0]]
            marca = "con remedio"
        mapa[str(i)] = list(origenes)
        finales.append(texto)
        filas.append((i, origenes, marca, texto, motivo))

    # GUARDA DEL CONSTRUCTOR: cobertura exacta 1..17, sin huecos ni repetidos.
    todos = []
    for v in mapa.values():
        todos.extend(v)
    faltan = sorted(set(range(1, len(pasos) + 1)) - set(todos))
    repes = sorted({x for x in todos if todos.count(x) > 1})
    sobran = sorted(set(todos) - set(range(1, len(pasos) + 1)))

    plan = {
        "operacion": OPERACION,
        "regla": REGLA,
        "motivo": MOTIVO,
        "fecha_corte": "2026-08-19",
        "correcciones_declaradas": [
            "LA CIFRA DE ARISTAS QUE LA OPERACION TRAE ESCRITA ES DE OTRO CORTE Y SE "
            "DECLARA EN VEZ DE COPIARSE (EJECUTOR.md regla 2): su campo verificacion "
            "dice 'el grafo entero tiene 16.866 entradas de arista antes y tiene que "
            "tener 16.866 despues', y esa cifra es del corte de la vuelta 17 (14 ago "
            "2026), ANTES de las ocho fusiones de OP-D-06. MEDIDO HOY, ANTES DEL "
            "ACTO: el grafo tiene 16.898 entradas. La guarda que la operacion exige "
            "es CERO MOVIMIENTO, o sea que la cifra de HOY sea la MISMA antes y "
            "despues del acto, y asi se comprueba. La cifra escrita se cita como "
            "contraste y NO se reescribe.",
            "LA CIFRA DE VECINOS DEL NODO SI CALZA AL DIGITO: la operacion dice 91 y "
            "hoy son 91 (25 previos mas 66 siguientes), medido antes del acto.",
        ],
        "nodos": [{
            "nodo": NODO,
            "fuente_esperada": FUENTE,
            "pasos_totales": len(pasos),
            "condiciones_totales": len(cond),
            "prefijos_pasos": [p[:34] for p in pasos],
            "prefijos_condiciones": [c[:34] for c in cond],
            "pasos_originales": pasos,
            "condiciones_originales": cond,
            "mapa_pasos": mapa,
            "pasos_finales": finales,
            "condiciones_finales": None,
            "mapa_condiciones": None,
            "procedencia": [{"pasos_del_resultado": list(range(1, len(finales) + 1)),
                             "libro": FUENTE}],
            "motivos_por_destino": dict((str(i), m) for i, o, k, t, m in filas),
        }],
    }

    print("=" * 78)
    print("EL PLAN DE OP-D-08, CONSTRUIDO CONTRA EL GRAFO (vuelta 45)")
    print("=" * 78)
    print()
    print("  nodo   : %s" % NODO)
    print("  fuente : %s  (UNICA, sin cambio)" % d.get("fuente"))
    print("  pasos  : %d  ->  %d" % (len(pasos), len(finales)))
    print("  condiciones: %d  ->  %d  (NO SE TOCAN, ver el motivo del plan)"
          % (len(cond), len(cond)))
    print()
    print("  EL MAPA DEL REPARTO, destino <- origenes:")
    print()
    print("  %-4s %-12s %-30s %s" % ("dst", "origenes", "que es", "texto del resultado"))
    for i, origenes, marca, texto, motivo in filas:
        print("  %-4d %-12s %-30s %s" % (i, origenes, marca, texto))
    print()
    print("  GUARDA DEL CONSTRUCTOR, cobertura exacta de 1 a %d:" % len(pasos))
    print("    origenes cubiertos : %d" % len(todos))
    print("    faltan             : %s" % (faltan or "ninguno"))
    print("    repetidos          : %s" % (repes or "ninguno"))
    print("    sobran             : %s" % (sobran or "ninguno"))
    if faltan or repes or sobran:
        print("\n  PARADA: la cobertura no cierra. NO se sella el plan.")
        return 1

    print()
    print("  LA COLUMNA VERTEBRAL, comprobada CONTIGUA Y EN ORDEN en el resultado:")
    col = [i for i, o, k, t, m in filas if set(o) & {13, 14, 15, 16, 17}]
    print("    destinos que la llevan: %s" % col)
    print("    contigua: %s | en orden de origen: %s"
          % (col == list(range(min(col), max(col) + 1)),
             [sorted(set(o) & {13, 14, 15, 16, 17})[0] for i, o, k, t, m in filas
              if set(o) & {13, 14, 15, 16, 17}] == [13, 14, 15, 16, 17]))
    print()
    print("  LOS NUEVE BLOQUES DEL CANVAS, contados sobre la columna que sobrevive:")
    textos_col = [t for i, o, k, t, m in filas if set(o) & {13, 14, 15, 16, 17}]
    vivos = 0
    for b in (u"segmento", u"propuesta de valor", u"canales", u"relaciones",
              u"ingresos", u"recursos", u"actividades", u"asociaciones", u"costos"):
        vivo = any(b in t.lower() for t in textos_col)
        vivos += 1 if vivo else 0
        print("    %-20s en la columna que sobrevive: %s" % (b, vivo))
    print("    LOS NUEVE BLOQUES VIVOS EN LA COLUMNA: %d de 9" % vivos)

    with io.open(DESTINO, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(plan, ensure_ascii=False, indent=1) + u"\n")
    print()
    print("  PLAN SELLADO en %s" % os.path.relpath(DESTINO, RAIZ))
    print("=" * 78)
    return 0


raise SystemExit(main())
