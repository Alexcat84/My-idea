"""Vuelta 28: sella el plan de la RELECTURA CONJUNTA en docs/loop/PLAN_V28_RELECTURA.json.

Los prefijos de guarda NO se escriben a mano: se leen de los pasos del grafo HOY,
que es la unica forma de que la guarda de texto pruebe algo. El script no decide
destinos: los destinos los decide la lectura del ejecutor (P.18) y estan aqui con
su motivo escrito.

Uso: python scripts/loop/vuelta28_sellar_relectura.py
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop", "PLAN_V28_RELECTURA.json")

HUGOS = "Essentials of Supply Chain Management - Michael H. Hugos"
SPIN = "SPIN Selling - Neil Rackham"


def nodo(nid):
    with open(os.path.join(NODOS, nid + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


def prefijos(nid, idx, largo=45):
    pasos = nodo(nid)["pasos_accionables"]
    return [pasos[i - 1][:largo] for i in idx]


NUEVO_CIRCULAR = {
    "node_id": "estrategia_circular_y_mecanismo_de_retorno",
    "fase_proyecto": "planificacion",
    "dominio": "core",
    "titulo_concepto": "Elección de Estrategia Circular y Diseño del Mecanismo de Retorno",
    "fuente": HUGOS,
    "resumen_teorico": (
        "Decidir que tu negocio será circular no dice todavía por dónde empieza. "
        "Antes de simular nada y antes de invertir, hay un acto propio: mirar el ciclo de "
        "vida que tu producto tiene HOY, compararlo con las cinco estrategias circulares y "
        "elegir en cuál de ellas tu negocio tiene más potencial real. Elegida la "
        "estrategia, hay que diseñar el mecanismo que la hace posible, el retorno del "
        "producto o su remanufactura, y recién entonces poner números: cuánto mejora la "
        "sostenibilidad y cuánto mueve tus costos de materiales y de logística. La "
        "elección y el mecanismo son el insumo de la simulación, no su resultado."
    ),
    "entregable_esperado": (
        "La estrategia circular elegida para tu negocio, con el mecanismo de retorno o "
        "remanufactura diseñado y el impacto calculado en sostenibilidad y en costos de "
        "materiales y logística"
    ),
    "nodos_previos": ["economia_circular_como_modelo_de_negocio"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando ya decidiste que tu modelo de negocio será circular y hay que elegir por "
        "cuál de las cinco estrategias empezar",
        "Antes de simular o dimensionar la cadena, porque la simulación necesita una "
        "estrategia y un mecanismo ya elegidos para comparar",
    ],
    "etiqueta_arbol": "Elige tu Estrategia Circular",
}


def main():
    plan = {
        "operacion": "OP-F-03 (recomputo de la relectura conjunta del acta 27)",
        "motivo": (
            "RELECTURA CONJUNTA de las dos discrepancias del acta de la vuelta 27, "
            "seccion 2. Las dos VOLTEAN. Correccion declarada en docs/plan/01_FUENTES.md: "
            "el texto de la lectura anterior se queda entero."
        ),
        "fecha_corte": "2026-08-14",
        "mudanzas": [
            {
                "caso": "d2 del acta 27",
                "huella": "cinco estrategias circulares",
                "desde": "modelo_simulacion_cadena_suministro_circular",
                "procedencia": "economia_circular_como_modelo_de_negocio",
                "pasos_totales": len(nodo("modelo_simulacion_cadena_suministro_circular")["pasos_accionables"]),
                "pasos_que_salen": [6, 7, 8, 9],
                "prefijos": prefijos("modelo_simulacion_cadena_suministro_circular", [6, 7, 8, 9]),
                "fuente_esperada_desde": HUGOS,
                "destino": {
                    "tipo": "nodo_propio",
                    "nuevo": NUEVO_CIRCULAR,
                    "motivo_p18": (
                        "MEDIDO HOY sobre los 111 nodos vivos que declaran a Hugos: "
                        "modelo_simulacion_cadena_suministro_circular es el UNICO cuyo objeto "
                        "es la cadena circular, y su objeto NO coincide con el del bloque. El "
                        "miembro SIMULA y COMPARA disenos (sus cinco pasos son definir "
                        "entidades, centro de gravedad, correr simulaciones, reportes de P y L, "
                        "comparar disenos) y su entregable es un modelo de simulacion con P y L "
                        "y KPIs para al menos dos escenarios. El bloque ELIGE la estrategia y "
                        "DISENA el mecanismo (mapear el ciclo de vida actual, identificar en "
                        "cual de las cinco estrategias hay mas potencial, disenar el retorno o "
                        "la remanufactura, calcular el impacto). Ningun paso del miembro hace "
                        "eso y ningun paso del bloque simula. Sin miembro cuyo objeto coincida, "
                        "P.18 punto 3 manda NODO PROPIO dentro de la familia."
                    ),
                },
            },
            {
                "caso": "d4 del acta 27",
                "huella": "otro posicionamiento de precio",
                "desde": "diferencia_ventaja_beneficio",
                "procedencia": "superioridad_producto_beneficios",
                "pasos_totales": len(nodo("diferencia_ventaja_beneficio")["pasos_accionables"]),
                "pasos_que_salen": [5, 6, 7, 8],
                "prefijos": prefijos("diferencia_ventaja_beneficio", [5, 6, 7, 8]),
                "fuente_esperada_desde": SPIN,
                "destino": {
                    "tipo": "miembro",
                    "nodo": "framework_caracteristicas_ventajas_beneficios",
                    "fuente_esperada_destino": SPIN,
                    "motivo_p18": (
                        "El bloque opone CARACTERISTICAS y BENEFICIOS y no nombra la Ventaja ni "
                        "una sola vez: decide de que clase de mensaje se compone tu discurso "
                        "segun tu posicionamiento de precio. Ese es el objeto de "
                        "framework_caracteristicas_ventajas_beneficios, cuyo entregable es "
                        "literalmente la guia de clasificacion de mensajes de venta aplicada a "
                        "la propuesta de valor propia, y cuyo paso 3 pide que el Beneficio "
                        "responda a una Necesidad Explicita, que es lo mismo que el paso "
                        "premium del bloque. El miembro que lo recibio, "
                        "diferencia_ventaja_beneficio, decide el MOMENTO de la conversacion (su "
                        "entregable dice con esas palabras el momento exacto de la conversacion "
                        "en que debes usar cada uno) y el bloque no decide ningun momento: "
                        "decide un estilo global. El objeto no coincide alli y si coincide aqui."
                    ),
                },
            },
        ],
    }
    with open(SALIDA, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
    print("SELLADO: %s" % SALIDA)
    for m in plan["mudanzas"]:
        print("\n%s: %s pasos %s -> %s" % (
            m["caso"], m["desde"], m["pasos_que_salen"],
            m["destino"].get("nodo") or m["destino"]["nuevo"]["node_id"]))
        for p in m["prefijos"]:
            print("   prefijo: %r" % p)


if __name__ == "__main__":
    main()
