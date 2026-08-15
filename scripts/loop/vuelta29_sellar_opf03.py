"""Vuelta 29: sella el plan de los CINCO BLOQUES DE `OP-F-03` CON DESTINO NODO
PROPIO que el muro tenia presos, menos el de economia circular, que ya venia
sellado desde la vuelta 28 en docs/loop/PLAN_V28_RELECTURA.json.

Los destinos NO se deciden aqui: estan LEIDOS Y PUBLICADOS en
docs/plan/01_FUENTES.md, seccion LOS CUATRO QUE NO SE PUDIERON EJECUTAR, con el
motivo por P.18 escrito nodo a nodo. Este script escribe el plan ejecutable de
esa lectura: los prefijos y las huellas se leen DEL GRAFO DE HOY, no se
escriben a mano, y el script PARA si una huella no esta en el origen o si YA
esta en el grafo fuera de el.

LA ADJUDICACION 3 DEL ACTA 27, aplicada: `analisis_tco_roi_b2b` (5 a 9) y
`criterios_seleccion_proveedores` (7 a 10) van a UN SOLO nodo propio con las dos
procedencias declaradas, nunca dos gemelos. El segundo corte entra al nodo que el
primero acaba de crear.

Uso: python scripts/loop/vuelta29_sellar_opf03.py
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop", "PLAN_V29_OPF03_PROPIOS.json")

HUGOS = "Essentials of Supply Chain Management - Michael H. Hugos"


def nodo(nid):
    with open(os.path.join(NODOS, nid + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


def todos():
    fuera = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.load(open(os.path.join(NODOS, nombre), encoding="utf-8"))
            fuera[d["node_id"]] = d
    return fuera


PROVEEDORES = {
    "node_id": "seleccion_de_proveedores_por_costo_total",
    "fase_proyecto": "planificacion",
    "dominio": "core",
    "titulo_concepto": "Seleccion de Proveedores por Costo Total Ponderado",
    "fuente": HUGOS,
    "resumen_teorico": (
        "Elegir proveedor por el precio unitario mas bajo es decidir con la mitad de la "
        "informacion. Lo que de verdad cuesta trabajar con un proveedor incluye la calidad "
        "que entrega, su cumplimiento y el control que tiene sobre sus procesos, y esos "
        "criterios no pesan igual en todos los negocios. El acto propio es armar la "
        "comparacion antes de firmar: definir que criterios cualitativos importan, repartir "
        "el peso entre el costo monetario y esos criterios, calcular el costo total "
        "ponderado de cada proveedor y compararlos con esa cifra en vez de con el precio de "
        "lista. Y hay una decision que va con la misma logica: concentrar el volumen en "
        "menos proveedores da poder de negociacion, asi que la lista de preferidos se arma "
        "a proposito y no por acumulacion."
    ),
    "entregable_esperado": (
        "La comparacion ponderada de tus proveedores por costo total, con los criterios y "
        "sus pesos escritos, y la lista de proveedores preferidos que sale de ella"
    ),
    "nodos_previos": ["analisis_tco_roi_b2b", "criterios_seleccion_proveedores"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando tienes varias propuestas de proveedor sobre la mesa y el precio unitario no "
        "alcanza para decidir",
        "Cuando quieres reducir el numero de proveedores para concentrar volumen de compra y "
        "ganar poder de negociacion",
    ],
    "etiqueta_arbol": "Elige por Costo Total",
}

INVENTARIO = {
    "node_id": "driver_de_inventario",
    "fase_proyecto": "ejecucion",
    "dominio": "core",
    "titulo_concepto": "Driver de Inventario: Ciclico, de Seguridad y Estacional",
    "fuente": HUGOS,
    "resumen_teorico": (
        "El inventario es uno de los drivers de la cadena de suministro, y se dimensiona en "
        "tres partes que responden a preguntas distintas. El inventario ciclico sale de "
        "balancear lo que cuesta ordenar contra lo que cuesta mantener: pedir mas seguido "
        "encarece las ordenes y pedir de mas encarece el almacen. El inventario de seguridad "
        "no depende del promedio de la demanda sino de su variabilidad y de lo que te cuesta "
        "quedarte sin stock. Y el estacional obliga a una eleccion de fondo: acumular antes "
        "del pico o invertir en flexibilidad de produccion para no acumular. Las tres se "
        "sostienen sobre los puntos de reorden, y esos se ajustan con datos reales de "
        "demanda, no con los del plan original."
    ),
    "entregable_esperado": (
        "Los tres niveles de inventario dimensionados, ciclico, de seguridad y estacional, "
        "con sus puntos de reorden y la fecha en que se vuelven a revisar con demanda real"
    ),
    "nodos_previos": ["gestion_inventario"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando ya sabes cuanto inventario tienes y hay que decidir cuanto DEBERIAS tener",
        "Cuando la demanda varia o tiene estacionalidad y el nivel unico de stock deja de "
        "servir",
    ],
    "etiqueta_arbol": "Dimensiona tu Inventario",
}

ACCESO = {
    "node_id": "producto_como_servicio_de_acceso",
    "fase_proyecto": "planificacion",
    "dominio": "core",
    "titulo_concepto": "Del Producto Vendido al Servicio de Acceso",
    "fuente": HUGOS,
    "resumen_teorico": (
        "Hay una pregunta que no es de diseno de experiencia sino de modelo: si lo que hoy "
        "vendes como bien podria entregarse como acceso a un servicio. No se contesta con "
        "una opinion. Se evalua si el producto se puede reformular asi, se identifican las "
        "barreras concretas que el cliente pone (confianza, disponibilidad, conveniencia y "
        "costo, y sobre todo la de propiedad contra renta), y se prueba con un piloto que "
        "mida uso y retencion en vez de unidades vendidas. Y hay una cuenta que solo aparece "
        "cuando el modelo cambia: pasar a acceso mueve la cadena de suministro entera, "
        "porque aparecen el mantenimiento, la redistribucion y la recoleccion que la venta "
        "de propiedad no tenia."
    ),
    "entregable_esperado": (
        "La evaluacion de tu producto como servicio de acceso, con las barreras de adopcion "
        "identificadas, el piloto disenado con sus metricas de uso y retencion, y el impacto "
        "medido sobre tu cadena de suministro"
    ),
    "nodos_previos": ["transicion_producto_a_experiencia"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando te preguntas si tu producto se vende mejor como acceso o suscripcion que "
        "como propiedad",
        "Antes de comprometer la cadena de suministro a un modelo de acceso, porque el "
        "mantenimiento, la redistribucion y la recoleccion no estaban en el de venta",
    ],
    "etiqueta_arbol": "Evalua Vender Acceso",
}

# origen, indices que salen, fuente_queda, destino(tipo, cuerpo o id), huella, motivo
CORTES = [
    ("analisis_tco_roi_b2b", [5, 6, 7, 8, 9],
     "The Startup Owner's Manual - Steve Blank",
     ("nodo_propio", PROVEEDORES),
     "costo total ponderado",
     "Destino LEIDO Y PUBLICADO en 01_FUENTES.md (vuelta 27): la subfamilia Hugos tiene el "
     "consumo (gestion_procurement_consumo), la negociacion (negociacion_contratos_proveedores) "
     "y el desempeno (gestion_contratos_desempeno), pero NO tiene la SELECCION. El bloque "
     "pondera criterios cualitativos contra costo monetario y compara proveedores por costo "
     "total, que es un acto que ningun miembro de la familia tiene por objeto. P.18 punto 3: "
     "nodo propio dentro de la familia."),

    ("criterios_seleccion_proveedores", [7, 8, 9, 10],
     "A Project Manager's Book of Forms",
     ("miembro", "seleccion_de_proveedores_por_costo_total"),
     "concentrar tu volumen de compra",
     "MISMO destino que el corte anterior, por la ADJUDICACION 3 DEL ACTA DE LA VUELTA 27, "
     "ratificada por extension citada de P.18 y de la vara madre de la campana: dos bloques "
     "que caen en el mismo nodo propio se funden en UNO, con las dos procedencias declaradas, "
     "NUNCA dos gemelos. Fabricar dos nodos con el mismo material de Hugos el dia de su "
     "creacion seria fabricar el par que la campana existe para deshacer. El material es el "
     "mismo: mirar mas alla del precio y concentrar volumen reduciendo la base de proveedores."),

    ("gestion_inventario", [6, 7, 8, 9],
     "Financial Intelligence for Entrepreneurs",
     ("nodo_propio", INVENTARIO),
     "inventario de seguridad",
     "Destino LEIDO Y PUBLICADO en 01_FUENTES.md (vuelta 27): la familia tiene los drivers de "
     "produccion, transporte, ubicacion e informacion, y le FALTA el de inventario. El bloque "
     "es ese driver entero: ciclico, de seguridad y estacional, con su punto de reorden. "
     "P.18 punto 3: nodo propio dentro de la familia."),

    ("transicion_producto_a_experiencia", [5, 6, 7, 8],
     "Change by Design",
     ("nodo_propio", ACCESO),
     "Product-as-a-Service",
     "Destino LEIDO Y PUBLICADO en 01_FUENTES.md (vuelta 27): ningun miembro tiene por objeto "
     "convertir el producto en servicio de acceso. P.18 punto 3: nodo propio dentro de la "
     "familia."),

    ("transicion_producto_a_experiencia", [9, 10, 11, 12],
     "Change by Design",
     ("miembro", "producto_como_servicio_de_acceso"),
     "tres interfaces de usuario",
     "MISMO destino que el corte anterior, por la ADJUDICACION 3 DEL ACTA DE LA VUELTA 27: los "
     "dos bloques salen del MISMO nodo, declaran al MISMO libro (Hugos, con las dos grafias que "
     "el nodo trae) y dicen casi lo mismo (su paso 9 repite al 5 y su paso 10 al 6). Partirlos "
     "en dos nodos propios seria fabricar el gemelo. La repeticion que esto crea DENTRO del "
     "nodo nuevo NO se desteje aqui: entra a la cola de relectura de la fase 02, como manda el "
     "registro de 08_VERIFICACION.md."),
]


def main():
    grafo = todos()
    cortes = []
    fallos = []
    creados = set()
    for origen, idx, fuente_queda, (tipo, destino), huella, motivo in CORTES:
        d = grafo[origen]
        pasos = d["pasos_accionables"]
        for i in idx:
            if i < 1 or i > len(pasos):
                fallos.append("%s: paso %d fuera de rango (%d pasos)" % (origen, i, len(pasos)))
        if fallos:
            break
        salen = [pasos[i - 1] for i in idx]

        # GUARDA DE HUELLA: tiene que estar en el bloque que sale, y NO puede
        # vivir ya en ningun otro nodo del grafo (una huella que ya vive fuera
        # no probaria nada en el caso positivo).
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
                fallos.append("%s: el miembro destino %s no existe ni lo crea este plan"
                              % (origen, destino_id))
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
        print("SELLADO: %-38s %s -> %s" % (origen, idx, destino_id))

    if fallos:
        print("\nPARADA: %d guarda(s) en rojo. No se sella nada." % len(fallos))
        for f in fallos:
            print("  - %s" % f)
        return 1

    plan = {
        "operacion": "OP-F-03, LOS BLOQUES CON DESTINO NODO PROPIO que el muro tenia presos",
        "fecha_corte": "2026-08-14",
        "regla": (
            "Los destinos NO se deciden en este plan: estan leidos y publicados en "
            "docs/plan/01_FUENTES.md desde la vuelta 27 (seccion LOS CUATRO QUE NO SE "
            "PUDIERON EJECUTAR), con su motivo por P.18 nodo a nodo. Lo que este plan "
            "anade es el CUERPO de los nodos propios, escrito por lectura de los pasos que "
            "viajan, y la aplicacion de la adjudicacion 3 del acta de la vuelta 27 (dos "
            "bloques al mismo nodo propio se funden en UNO). El quinto bloque de la cuenta, "
            "economia_circular_como_modelo_de_negocio, venia sellado aparte desde la vuelta "
            "28 en docs/loop/PLAN_V28_RELECTURA.json y se aplico antes que este."
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
