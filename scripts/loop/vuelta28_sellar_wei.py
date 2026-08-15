"""Vuelta 28: sella el plan de OP-F-04-WEI en docs/loop/PLAN_V28_OPF04_WEI.json.

Solo entran los cortes cuyo DESTINO esta leido contra la nomina viva de la familia
Traction medida HOY. Los bloques de la tanda cuyo destino todavia no se leyo NO
entran: se declaran en el reporte con su frontera y sin destino.

Los prefijos y las huellas se leen del grafo de hoy, no se escriben a mano, y el
script PARA si una huella no esta en el origen o si YA esta en el destino (una
huella que ya vive en el destino no probaria nada).

Uso: python scripts/loop/vuelta28_sellar_wei.py
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop", "PLAN_V28_OPF04_WEI.json")

TRACTION = "Traction - Gabriel Weinberg"


def nodo(nid):
    with open(os.path.join(NODOS, nid + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


def pasos(nid):
    return nodo(nid)["pasos_accionables"]


# origen, indices que salen, fuente_queda, destino, huella (trozo del bloque), motivo
CORTES = [
    ("plan_de_adquisicion_acquire", [8, 9, 10, 11, 12],
     "The Startup Owner's Manual - Blank, Steve",
     "bullseye_framework",
     "contactar a diez blogs de tu nicho",
     "El bloque es el proceso Bullseye entero, paso por paso: listar los 19 canales "
     "sin descartar (su paso 1), disenar una prueba barata y corta para cada canal que "
     "haga sentido (sus pasos 2 y 3), correrlas en paralelo o por lotes midiendo "
     "resultados concretos (sus pasos 3 y 4), y comparar entre canales para elegir "
     "donde invertir mas (su paso 5). El miembro que solo cubre el anillo medio "
     "(middle_ring_testing) NO tiene el paso de listar los 19, que es el anillo "
     "exterior y es el primer paso del bloque: por eso el objeto coincide con la diana "
     "entera y no con una de sus fases."),

    ("earned_vs_paid_media", [5, 6, 7, 8],
     "The Startup Owner's Manual - Steve Blank",
     "publicidad_offline_pruebas_locales",
     "prospecto de audiencia",
     "El bloque es el canal de anuncios fuera de internet: preguntar a los clientes que "
     "medios consumen fuera de internet, pedir a cada medio su prospecto de audiencia, "
     "comparar alcance y precio, y empezar por pruebas pequenas y baratas en radio, "
     "prensa y vallas LOCALES. El objeto del miembro es exactamente ese: prueba barato "
     "en un mercado local antes de escalar, y busca espacios sobrantes para conseguir "
     "descuentos, que es la misma cuenta de precio contra alcance del bloque. Los otros "
     "dos nodos offline de la familia no coinciden: tracking_publicidad_offline MIDE lo "
     "ya lanzado y el bloque no mide, elige; publicidad_remanente_remnant_ads es una "
     "tactica de compra, no la eleccion del medio."),

    ("fit_problema_solucion", [4, 5, 6],
     "Value Proposition Design",
     "fases_traccion_producto",
     "canales de tracci",
     "Calce paso por paso, y es el mas literal de los cinco: identificar en que fase "
     "esta el negocio (su paso 1), en Fase I enviar un flujo pequeno y constante de "
     "clientes para detectar por donde se fuga el producto (su paso 2), y escalar "
     "marketing solo cuando la fuga baja, o sea al confirmar el ajuste producto mercado "
     "(su paso 4). El miembro se llama Las Tres Fases de Traccion y el bloque nombra las "
     "tres fases I, II y III."),

    ("sales_funnel_get_keep_grow", [5, 6, 7, 8, 9],
     "The Startup Owner's Manual - Blank, Steve",
     "clasificacion_leads_abc",
     "leads tipo C a marketing",
     "El bloque clasifica los leads en A, B y C por tiempo de cierre, reparte el tiempo "
     "de venta (66 a 75 por ciento a los A) y pasa los C a marketing para que los "
     "cultive. Ese es el objeto del miembro dicho con las mismas cifras y las mismas "
     "categorias. El paso de generar leads por marketing antes de vender y el de "
     "coordinar el collateral con marketing son la misma tuberia: quien nutre a los C "
     "es marketing."),

    ("sales_funnel_get_keep_grow", [10],
     "The Startup Owner's Manual - Blank, Steve",
     "compromiso_linea_tiempo_cliente",
     "timeline claro de compra",
     "SE SEPARA DEL ANTERIOR, y se dice por que: el paso 10 no clasifica ni reparte "
     "tiempo, PACTA UN PLAZO. Establecer un timeline claro de compra y pedir un "
     "compromiso explicito de si o no al prospecto es, palabra por palabra, el objeto "
     "del miembro (su entregable es el acuerdo con fecha y condiciones claras de "
     "decision, y sus pasos 2 y 3 son comunicar el cronograma y pedir el si o no). "
     "Meterlo en la clasificacion A B C seria forzar un encaje que la lectura no "
     "sostiene, y P.18 punto 3 lo prohibe."),
]


def main():
    cortes = []
    fallos = []
    for origen, idx, fuente_queda, destino, huella, motivo in CORTES:
        po = pasos(origen)
        pd = pasos(destino)
        texto_origen = " || ".join(po).lower()
        texto_destino = " || ".join(pd).lower()
        if huella.lower() not in texto_origen:
            fallos.append("%s: la huella %r NO esta en el origen" % (origen, huella))
        if huella.lower() in texto_destino:
            fallos.append("%s: la huella %r YA esta en el destino %s, no probaria nada"
                          % (origen, huella, destino))
        d = nodo(origen)
        cortes.append({
            "origen": origen,
            "frontera": "1 a %d / %s" % (min(idx) - 1, " y ".join(str(i) for i in idx)),
            "pasos_totales": len(po),
            "pasos_que_salen": idx,
            "prefijos": [po[i - 1][:45] for i in idx],
            "pasos_que_salen_texto": [po[i - 1] for i in idx],
            "fuente_esperada": d["fuente"],
            "fuente_queda": fuente_queda,
            "huella": huella,
            "destino": {
                "tipo": "miembro",
                "nodo": destino,
                "fuente_esperada_destino": TRACTION,
                "motivo_p18": motivo,
            },
        })

    if fallos:
        print("PARADA: no se sella nada.")
        for f in fallos:
            print("  - %s" % f)
        return 1

    plan = {
        "operacion": "OP-F-04-WEI",
        "clase": ("TANDA DE INJERTOS, grupo WEINBERG. CINCO cortes sobre CUATRO nodos, "
                  "los unicos de la tanda cuyo destino esta LEIDO contra la nomina viva "
                  "de la familia Traction medida hoy (80 nodos vivos, 67 con fuente unica)."),
        "regla": ("P.3 manda REPARTO OBLIGATORIO porque el tema coincide (el bloque habla "
                  "de canal y el nodo tambien). El miembro receptor se decide por P.18, "
                  "leido sobre la nomina vigente al dia de la operacion."),
        "fecha_corte": "2026-08-14",
        "cortes": cortes,
    }
    with open(SALIDA, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
    print("SELLADO: %s  (%d cortes)" % (SALIDA, len(cortes)))
    for c in cortes:
        print("\n%s  pasos %s -> %s" % (c["origen"], c["pasos_que_salen"], c["destino"]["nodo"]))
        print("  fuente: %r -> %r" % (c["fuente_esperada"], c["fuente_queda"]))
        print("  huella: %r" % c["huella"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
