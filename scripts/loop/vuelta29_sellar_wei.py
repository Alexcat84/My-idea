"""Vuelta 29: sella los bloques restantes de OP-F-04-WEI cuyo DESTINO se pudo
leer contra la nomina viva de la familia Traction medida HOY.

Las fronteras NO se deciden aqui: estan leidas y publicadas en
docs/plan/01_FUENTES.md desde la vuelta 28 (tabla LO QUE DE OP-F-04-WEI NO SE
EJECUTO). Lo que esta vuelta anade es el DESTINO de cada bloque por P.18, leido
sobre la nomina de hoy, y el cuerpo de los nodos propios que la lectura obliga.

LOS DOS DE TOQUE UNICO NO ENTRAN: coeficiente_viral y viral_loop_marketing se
traen como PARADA en el reporte, con su lectura escrita y sin ejecutar.

Los prefijos y las huellas se leen del grafo de hoy, no se escriben a mano, y el
script PARA si una huella no esta en el bloque o si YA vive fuera del origen.

Uso: python scripts/loop/vuelta29_sellar_wei.py
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop", "PLAN_V29_OPF04_WEI.json")

TRACTION = "Traction - Gabriel Weinberg"


def todos():
    fuera = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.load(open(os.path.join(NODOS, nombre), encoding="utf-8"))
            fuera[d["node_id"]] = d
    return fuera


ANILLO = {
    "node_id": "anillo_interior_explotar_el_canal_nucleo",
    "fase_proyecto": "ejecucion",
    "dominio": "core",
    "titulo_concepto": "El Anillo Interior del Bullseye: Explotar tu Canal Nucleo",
    "fuente": TRACTION,
    "resumen_teorico": (
        "La diana de traccion tiene tres anillos y el ultimo no es elegir: es exprimir. "
        "Cuando las pruebas del anillo medio ya dijeron cual canal funciona, el trabajo "
        "cambia de forma. Deja de ser abrir frentes y pasa a ser concentrar: todos los "
        "recursos de marketing van al canal que gano, y los canales secundarios que dieron "
        "resultados apenas moderados se sueltan, por prometedores que parezcan. Dentro de ese "
        "canal unico el metodo es la prueba continua, con grupo de control y confianza "
        "estadistica antes de sacar conclusiones, sobre las variables que el canal permite "
        "mover. Las tacticas que ganan se documentan y se escalan hasta que el canal se "
        "satura, y ese es el momento, y no antes, de volver a correr la diana entera para "
        "encontrar el siguiente."
    ),
    "entregable_esperado": (
        "Tu canal nucleo con todos los recursos concentrados en el, un calendario de pruebas "
        "sobre sus variables clave con sus resultados documentados, y el criterio escrito de "
        "cuando lo consideras saturado para repetir el Bullseye"
    ),
    "nodos_previos": ["middle_ring_testing", "bullseye_framework"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando las pruebas del anillo medio ya senalaron un canal ganador y hay que decidir "
        "cuanto le pones encima",
        "Cuando tu canal principal empieza a dar rendimientos decrecientes y hay que decidir "
        "si se sigue optimizando o se vuelve a la diana",
    ],
    "etiqueta_arbol": "Exprime tu Canal Ganador",
}

ESPIA = {
    "node_id": "inteligencia_de_anuncios_de_la_competencia",
    "fase_proyecto": "validacion",
    "dominio": "core",
    "titulo_concepto": "Que Anuncios Corre tu Competencia, y Donde",
    "fuente": TRACTION,
    "resumen_teorico": (
        "Los anuncios que tu competencia paga son informacion publica, y son la unica pista "
        "gratis de que le esta funcionando a alguien que vende a tu mismo cliente. Se pueden "
        "ver con herramientas de inteligencia publicitaria, que dicen que anuncios corre cada "
        "empresa y en que sitios los coloca. La lectura no termina en el anuncio: hay que "
        "mirar el perfil de audiencia de esos sitios y preguntarse si esa gente es de verdad "
        "tu cliente, porque un buen sitio para el competidor puede ser un mal sitio para ti. "
        "Y lo que sale de ahi no es una conclusion sino una lista de hipotesis: los angulos y "
        "los mensajes que la competencia ya paga se convierten en tus propias pruebas A/B, en "
        "vez de inventarlas desde cero."
    ),
    "entregable_esperado": (
        "El inventario de los anuncios y los sitios que corre tu competencia, con el perfil de "
        "audiencia de cada sitio y tu veredicto de encaje, y la lista de pruebas A/B que sacas "
        "de esos anuncios"
    ),
    "nodos_previos": ["analisis_trafico_competitivo"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando quieres saber donde anunciarte y prefieres partir de lo que ya le funciona a "
        "alguien que vende a tu mismo cliente",
        "Cuando se te acabaron las ideas propias de mensaje y necesitas hipotesis de prueba "
        "que no salgan de tu cabeza",
    ],
    "etiqueta_arbol": "Mira los Anuncios de tu Competencia",
}

BRILLANTES = {
    "node_id": "puntos_brillantes_antes_del_pivote",
    "fase_proyecto": "validacion",
    "dominio": "core",
    "titulo_concepto": "Buscar los Puntos Brillantes Antes de Pivotar",
    "fuente": TRACTION,
    "resumen_teorico": (
        "Antes de cambiar de rumbo hay una busqueda que casi nadie hace: mirar si en medio de "
        "los malos numeros hay clientes de verdad comprometidos, aunque sean poquisimos. Si "
        "los hay, la pregunta siguiente no es cuantos son sino que tienen en comun, porque de "
        "ese parecido sale la unica pista util. Y ahi hay una bifurcacion que decide el "
        "destino del negocio: esos pocos pueden ser adoptadores tempranos de un mercado "
        "grande que todavia no llego, o pueden ser valores atipicos que no representan a "
        "nadie. La misma duda tiene una tercera cara, que es el momento: a veces el producto "
        "esta bien y lo que fallo fue llegar temprano. Solo cuando la busqueda no encuentra un "
        "solo punto brillante, el pivote deja de ser una salida y pasa a ser la decision."
    ),
    "entregable_esperado": (
        "El analisis de tus clientes mas comprometidos con lo que tienen en comun, tu veredicto "
        "escrito de si son adoptadores tempranos o valores atipicos, y la decision de pivotar o "
        "perseverar que sale de el"
    ),
    "nodos_previos": ["decision_pivote_perseverar"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando las metricas no acompanan y el pivote esta sobre la mesa, antes de decidirlo",
        "Cuando tienes unos pocos clientes muy fieles y no sabes si son la punta de un mercado "
        "o una casualidad",
    ],
    "etiqueta_arbol": "Busca tus Puntos Brillantes",
}

# origen, indices, fuente_queda, (tipo, destino), huella, motivo P.18
CORTES = [
    ("enfoque_motor_unico_crecimiento", [5, 6, 7, 8, 9],
     "The Lean Startup - Eric Ries",
     ("nodo_propio", ANILLO),
     "anillo medio (Bullseye)",
     "P.18 PUNTO 3. La familia Traction tiene el anillo EXTERIOR (canales_de_traccion_19, "
     "listar los 19) y el anillo MEDIO (middle_ring_testing, probar los candidatos y comparar "
     "costo, volumen y calidad), y tiene la diana entera (bullseye_framework), pero NO TIENE "
     "EL ANILLO INTERIOR: que se hace con el canal una vez que gano. El bloque es exactamente "
     "ese acto: identificar el canal que gana en el anillo medio, redirigir todos los recursos "
     "hacia el, no distraerse con los secundarios, y repetir la diana cuando se sature."),

    ("optimizacion_embudo_get_customers", [6, 7, 8, 9, 10],
     "The Startup Owner's Manual - Steve Blank",
     ("miembro", "anillo_interior_explotar_el_canal_nucleo"),
     "Optimizely",
     "MISMO destino que el corte anterior, por la ADJUDICACION 3 DEL ACTA DE LA VUELTA 27: dos "
     "bloques que caen en el mismo nodo propio se funden en UNO, nunca dos gemelos. El objeto "
     "es el mismo anillo interior paso por paso: dedicar recursos SOLO al canal validado en el "
     "anillo medio, pruebas A/B continuas dentro de el, herramientas para correrlas, tacticas "
     "nuevas dentro del canal principal, y otros canales solo si lo alimentan."),

    ("ab_testing_optimizacion", [11, 12, 13, 14, 15],
     "The Startup Owner's Manual - Steve Blank",
     ("miembro", "anillo_interior_explotar_el_canal_nucleo"),
     "confianza estad",
     "MISMO destino que los dos cortes anteriores, por la ADJUDICACION 3. El bloque no es una "
     "prueba A/B cualquiera: dice DENTRO DE TU CANAL NUCLEO en su primer paso, y cierra "
     "documentando las tacticas ganadoras para escalarlas HASTA EL PUNTO DE SATURACION, que es "
     "la senal con la que el mismo anillo interior manda repetir la diana. Es el metodo de "
     "prueba del anillo interior, no del embudo en general."),

    ("analisis_trafico_competitivo", [5, 6, 7, 8],
     "The Startup Owner's Manual - Steve Blank",
     ("nodo_propio", ESPIA),
     "Quantcast",
     "P.18 PUNTO 3. Barrida la nomina de hoy, ningun miembro tiene por objeto MIRAR LOS "
     "ANUNCIOS QUE PAGA LA COMPETENCIA para decidir donde anunciarse: seleccion_plataforma_"
     "social_ads decide plataforma social por audiencia propia y objetivo propio; "
     "retargeting_display y quality_score_optimizacion son de campana propia ya corriendo; "
     "sem_estrategia_ejecucion es el lanzamiento de la campana de busqueda. El bloque parte de "
     "los anuncios AJENOS, mide el perfil de audiencia de los sitios donde corren, juzga el "
     "encaje y saca de ahi sus propias pruebas A/B."),

    ("decision_pivote_perseverar", [5, 6, 7, 8, 9],
     "The Lean Startup - Eric Ries",
     ("nodo_propio", BRILLANTES),
     "punto brillante",
     "P.18 PUNTO 3. Barrida la nomina de hoy, ningun miembro tiene por objeto BUSCAR LOS "
     "CLIENTES COMPROMETIDOS QUE QUEDAN ANTES DE PIVOTAR: identificacion_bolsas_virales "
     "segmenta por COEFICIENTE VIRAL y el bloque no habla de viralidad; leaky_bucket_metaphor "
     "y fases_traccion_producto miran por donde se FUGAN los clientes, no quienes se quedaron; "
     "traccion_como_metrica_clave define la metrica. El bloque hace la pregunta contraria a la "
     "fuga: quienes se quedaron, que tienen en comun, y si son adoptadores tempranos o valores "
     "atipicos."),

    ("key_partners_hypothesis", [6, 7, 8, 9, 10],
     "The Startup Owner's Manual - Steve Blank",
     ("miembro", "alineacion_bd_metricas_core"),
     "capacidad de mover la m",
     "P.18: el objeto coincide y el entregable del miembro lo dice con las mismas palabras "
     "(checklist de evaluacion de partnerships basado en METRICAS CORE del negocio). El bloque "
     "define el objetivo de traccion y sus metricas clave, elige el tipo de alianza que se "
     "alinea con ese objetivo, evalua a los socios POR SU CAPACIDAD DE MOVER LA METRICA y no "
     "por su tamano o prestigio, y rechaza los acuerdos atractivos que no esten alineados: es "
     "el mismo acto de filtrar alianzas contra la metrica."),

    ("key_partners_hypothesis", [11, 12, 13, 14],
     "The Startup Owner's Manual - Steve Blank",
     ("miembro", "pipeline_alianzas_bd"),
     "supply partnerships",
     "P.18, Y SE SEPARA DEL ANTERIOR A PROPOSITO: el acta de la vuelta 28 dejo SOSTENIDA la "
     "lectura de que el tramo de cola trae DOS sub bloques distinguibles, y leidos hoy se "
     "distinguen. Este no filtra por metrica: CLASIFICA POR TIPO segun el cuello de botella "
     "(marca, distribucion o inventario), y recorre licensing, socios de distribucion con "
     "acceso al cliente objetivo y supply partnerships. El entregable del miembro es "
     "exactamente esa tabla: el pipeline de partners CON CATEGORIZACION y prioridad."),

    ("metricas_de_adquisicion_activacion", [6, 7, 8, 9],
     "The Startup Owner's Manual",
     ("miembro", "sem_estrategia_ejecucion"),
     "CTR, CPC y CPA",
     "P.18: el bloque entero es la cuenta de una campana de anuncios de busqueda, y su ultimo "
     "paso nombra el canal (usa la publicidad en buscadores para aprender el mensaje). Define "
     "que cuenta como conversion ANTES de lanzar, calcula CTR, CPC y CPA por campana de prueba "
     "y compara el costo de adquisicion contra el valor de vida. El entregable del miembro es "
     "la campana activa con sus variantes, sus paginas de destino y EL SEGUIMIENTO DE "
     "CONVERSIONES: el bloque es la definicion y la lectura de ese seguimiento."),
]


def main():
    grafo = todos()
    cortes = []
    fallos = []
    creados = set()
    for origen, idx, fuente_queda, (tipo, destino), huella, motivo in CORTES:
        d = grafo[origen]
        pasos = d["pasos_accionables"]
        fuera = [i for i in idx if i < 1 or i > len(pasos)]
        if fuera:
            fallos.append("%s: pasos fuera de rango %s (%d pasos)" % (origen, fuera, len(pasos)))
            continue
        salen = [pasos[i - 1] for i in idx]

        if not any(huella in p for p in salen):
            fallos.append("%s: la huella %r NO esta en el bloque que sale" % (origen, huella))
            continue
        portadores = [nid for nid, dd in grafo.items()
                      if nid != origen and any(huella in p for p in dd.get("pasos_accionables") or [])]
        if portadores:
            fallos.append("%s: la huella %r ya vive fuera del origen, en %s"
                          % (origen, huella, portadores))
            continue

        destino_id = destino["node_id"] if tipo == "nodo_propio" else destino
        if tipo == "nodo_propio":
            if destino_id in grafo:
                fallos.append("%s: el nodo propio %s YA EXISTE" % (origen, destino_id))
                continue
            creados.add(destino_id)
            dest = {"tipo": "nodo_propio", "motivo_p18": motivo, "nuevo": destino}
        else:
            if destino_id not in grafo and destino_id not in creados:
                fallos.append("%s: el destino %s no existe ni lo crea este plan" % (origen, destino_id))
                continue
            dest = {"tipo": "miembro", "nodo": destino_id, "motivo_p18": motivo}
            if destino_id in creados:
                dest["creado_por_este_plan"] = True
            else:
                dest["fuente_esperada_destino"] = grafo[destino_id]["fuente"]

        cortes.append({
            "origen": origen,
            "frontera": "los pasos %s de %d" % (idx, len(pasos)),
            "pasos_que_salen": idx,
            "fuente_queda": fuente_queda,
            "destino": dest,
            "pasos_totales": len(pasos),
            "fuente_esperada": d["fuente"],
            "huella": huella,
            "prefijos": [p[:34] for p in salen],
            "pasos_que_salen_texto": salen,
        })
        print("SELLADO: %-38s %-18s -> %s" % (origen, idx, destino_id))

    if fallos:
        print("\nPARADA: %d guarda(s) en rojo. No se sella nada." % len(fallos))
        for f in fallos:
            print("  - %s" % f)
        return 1

    plan = {
        "operacion": "OP-F-04-WEI, los bloques con destino leido (los dos de TOQUE UNICO NO entran)",
        "fecha_corte": "2026-08-14",
        "nomina_de_la_familia": (
            "Medida HOY, no copiada: 76 nodos vivos declaran Traction y 67 lo declaran como "
            "fuente UNICA (docs/loop/SALIDA_V29_FAMILIA_WEINBERG.txt). Coincide con la "
            "medicion de cierre del auditor en el acta de la vuelta 28, y NO con la de "
            "apertura de esa vuelta (80 y 67), que es la caida de reporte que el acta nombro."
        ),
        "lo_que_no_entra": (
            "coeficiente_viral y viral_loop_marketing, los dos de TOQUE UNICO. Van al reporte "
            "como PARADA con su lectura escrita: su texto no alcanza para ejecutarse sin "
            "decidir lo que ninguna pagina escribio."
        ),
        "cortes": cortes,
    }
    with open(SALIDA, "w", encoding="utf-8") as fh:
        json.dump(plan, fh, ensure_ascii=False, indent=2)
    print("\nESCRITO: %s  (%d cortes, %d nodos propios nuevos)"
          % (SALIDA, len(cortes), len(creados)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
