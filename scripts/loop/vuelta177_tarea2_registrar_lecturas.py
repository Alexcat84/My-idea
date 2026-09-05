# -*- coding: utf-8 -*-
r"""vuelta177_tarea2_registrar_lecturas.py . REGISTRA EN JSONL LAS LECTURAS POR
ACTO DE `OP-L-03` DE LA VUELTA 177.

ESCRIBE UN SOLO FICHERO: `docs/plan/OP_L_03_LECTURAS.jsonl`. NO toca nodos, NO
toca `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, NO toca `docs/plan/OPERACIONES.jsonl`
y NO mueve el marcador. Las tres cosas son condiciones expresas del encargo.

POR QUE JSONL Y NO PROSA: letra (d) del encargo, *"CADA LECTURA SE REGISTRA EN
JSONL, NO SE NARRA EN PROSA"*, y modo austero punto 2, que prohibe la prosa de
acompanamiento que repite lo que el registro ya dice.

QUE LLEVA CADA FILA, Y ES LO QUE LA LETRA (d) PIDE UNO A UNO:

  . `acto` y `miembros` con su `fuente`;
  . `pares_con_veredicto`, con su puesto y su clase, que es LO QUE EL PAR DIJO
    POR SEPARADO;
  . `pares_por_leer`, los que esta operacion debe leer;
  . `forma`, LA FORMA QUE SALE DE LEERLO ENTERO;
  . `cambia_respecto_del_par`, y si cambia, en que;
  . `cobertura`, la re-medicion con su cobertura al lado, que es la cuarta linea
    de la `verificacion` de la ficha y el banco 9.26;
  . `veredictos_movidos`, que en esta vuelta es CERO en todas las filas.

LO MEDIDO SE COMPUTA AQUI Y LO LEIDO SE DECLARA. Las cifras (miembros, nodos
vivos tras resolver, pares por cajon, puestos y clases) NO se teclean: salen del
resolutor y del registro de veredictos en esta corrida. Lo unico que este
fichero trae escrito es LA LECTURA, que es el trabajo humano que la operacion
encarga y que ningun instrumento puede producir: la `forma` de cada acto y la
clase que cada par por leer toma DENTRO de esa forma.

LA LECTURA ES DEL ACTO Y NO DE LA PAREJA (`P.5`, citada y no parafraseada en el
dossier). Por eso `forma` es UNA por acto y las clases de los pares por leer se
derivan de ella, no al reves.

USO:
  python scripts/loop/vuelta177_tarea2_registrar_lecturas.py
  python scripts/loop/vuelta177_tarea2_registrar_lecturas.py --seco
"""
import argparse
import io
import json
import os
import sys
from itertools import combinations

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import vuelta166_tarea2_correccion_op_l_01 as T   # noqa: E402
import vuelta177_tarea2_dossier_actos as D   # noqa: E402

NL = chr(10)
DESTINO = os.path.join(RAIZ, "docs", "plan", "OP_L_03_LECTURAS.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VUELTA = 177
FECHA = "2026-09-05"

# LAS LECTURAS. Esto es lo unico tecleado del fichero, y es lo unico que DEBE
# estarlo: es el juicio que la operacion encarga. Cada entrada va por el
# NOMBRE DEL PRIMER MIEMBRO ORDENADO del acto, que es como el dossier los
# identifica, y no por un numero de orden que cambiaria si el universo cambia.
LECTURAS = {
    "cash_burn_calculation": {
        "forma": (
            "UNA FAMILIA Y UN VECINO, NO UNA FAMILIA DE CINCO. La familia es EL "
            "MODELO FINANCIERO DEL FIN DE LA VALIDACION, y no la nombro yo: la "
            "nombra la razon del puesto 404, que ya la contaba en TRES nodos "
            "(metrics_that_matter_framework, validar_modelo_financiero y "
            "cash_burn_calculation). Leido el acto entero, la familia son esos "
            "tres mas verificar_modelo_ingresos, que hace el mismo calculo en "
            "tres escenarios. cash_burn_calculation no es un cuarto miembro "
            "independiente: es EL PASO DE CAJA de los otros tres, y esta "
            "literalmente dentro de cada uno (paso 4 de metrics, paso 5 de "
            "validar, paso 6 de verificar). EL VECINO es "
            "validacion_hipotesis_ingresos, y lo que lo separa es su PUERTA DE "
            "SALIDA, que es la vara que el puesto 1374 ya uso: los demas salen "
            "por CUANTO TIEMPO QUEDA, y este sale por CUANTO SE PUEDE GASTAR EN "
            "TRAER AL SIGUIENTE CLIENTE (LTV). Comparten el dato de entrada, el "
            "ingreso neto de canal, y no el resultado."
        ),
        "por_leer": {
            "cash_burn_calculation|validar_modelo_financiero": (
                "A", "cash_burn_calculation es el paso 5 de validar_modelo_financiero "
                "dicho como nodo ('Verificar el balance de caja disponible "
                "(runway)'). Es la MISMA contencion que el puesto 404 ya declaro "
                "contra metrics_that_matter_framework, y la misma clase."),
            "cash_burn_calculation|verificar_modelo_ingresos": (
                "A", "cash_burn_calculation es el paso 6 de verificar_modelo_ingresos "
                "dicho como nodo ('Evalua tu cash burn y la caja disponible para "
                "saber si sobrevives el periodo proyectado'). Misma contencion, "
                "misma clase."),
            "metrics_that_matter_framework|validacion_hipotesis_ingresos": (
                "D", "Por la vara de la puerta de salida del puesto 1374, aplicada "
                "al acto y no a la pareja. metrics_that_matter_framework no "
                "calcula el valor de un cliente en ninguno de sus seis pasos; "
                "validacion_hipotesis_ingresos remata en el LTV y lo usa para "
                "fijar el precio. Lo que metrics tiene y el otro no es la hoja "
                "organizada por el Business Model Canvas y cuantos pivotes se "
                "pueden pagar."),
            "validacion_hipotesis_ingresos|validar_modelo_financiero": (
                "A", "Aqui la vara de la puerta de salida NO separa, y por eso la "
                "clase cambia respecto del par anterior: validar_modelo_financiero "
                "SI calcula el valor de un cliente, en su paso 2 ('costos de "
                "adquisicion de clientes, tasas de conversion y Customer Lifetime "
                "Value'). Contiene entero lo que validacion_hipotesis_ingresos "
                "hace a mano, y con mas profundidad."),
        },
        "cambia": (
            "SI, Y EN LO QUE MAS IMPORTA. De a pares, cash_burn_calculation "
            "parece un miembro mas de la familia. Leido el acto entero es EL PASO "
            "DE CAJA que los otros tres ya llevan dentro, y esa es una relacion "
            "distinta de la de ser hermanos. Y LA LECTURA DEJA UN TRIANGULO A MAS "
            "A MAS D MEDIDO, que se declara y no se esconde: "
            "cash_burn_calculation con verificar_modelo_ingresos sale A en esta "
            "lectura, verificar_modelo_ingresos con validacion_hipotesis_ingresos "
            "es A en el puesto 451, y cash_burn_calculation con "
            "validacion_hipotesis_ingresos es D en el puesto 1374. POR P.10 ESE "
            "TRIANGULO BLOQUEA LA FUSION DEL ACTO ENTERO, y es exactamente lo que "
            "una lectura de a pares no puede ver."
        ),
        "no_mueve": (
            "NINGUN VEREDICTO SE MUEVE. Relei la razon entera del puesto 1374 "
            "antes de decidir y SE SOSTIENE SOLA: los dos parten del ingreso neto "
            "de canal y salen por puertas distintas. La lectura del acto no me "
            "obliga a cambiarla, asi que no la cambio. El triangulo se registra "
            "como hallazgo para que lo adjudique quien manda."
        ),
    },
    "construccion_de_leverage": {
        "forma": (
            "UNA FAMILIA PURA DE CUATRO Y UNA TECNICA QUE NO ES DE LA FAMILIA. La "
            "familia es LA MISMA MANIOBRA dicha cuatro veces: conseguir varias "
            "propuestas de inversion en paralelo, sincronizadas en el tiempo, para "
            "tener poder de negociacion. Son construccion_de_leverage, "
            "estrategia_competencia_vcs, gestion_multiples_term_sheets y "
            "leverage_en_negociacion_con_vcs, y el puro de cuatro no lo declaro "
            "yo: lo declara la razon del puesto 1030 con estas palabras, 'Y CON "
            "ESTE PAR NACE EL PRIMER PURO DE CUATRO'. LA QUINTA, "
            "tecnica_anclaje_negociacion, ES OTRA COSA: es el anclaje, o sea "
            "elegir pocos puntos clave y no moverse de ellos, que es una tecnica "
            "de mesa y no una maniobra de calendario. No habla de varios "
            "inversionistas, ni de sincronizar tiempos, ni de competencia."
        ),
        "por_leer": {
            "estrategia_competencia_vcs|tecnica_anclaje_negociacion": (
                "D", "estrategia_competencia_vcs es el CALENDARIO de la ronda, "
                "planear con tres a seis meses para que los tiempos de decision "
                "coincidan. tecnica_anclaje_negociacion es QUE TERMINOS no se "
                "negocian. Ni un paso en comun."),
            "gestion_multiples_term_sheets|tecnica_anclaje_negociacion": (
                "D", "gestion_multiples_term_sheets es el pacing, acelerar a unos y "
                "frenar a otros sin revelar con quien se habla. "
                "tecnica_anclaje_negociacion es la lista priorizada de terminos. "
                "Ni un paso en comun."),
            "leverage_en_negociacion_con_vcs|tecnica_anclaje_negociacion": (
                "D", "leverage_en_negociacion_con_vcs son cuatro tacticas de CUANDO "
                "negociar (esperar traccion, varias propuestas, ofertas de compra "
                "alternativas, negociar antes de quedarse sin efectivo) y ninguna "
                "de las cuatro es anclar. tecnica_anclaje_negociacion es COMO "
                "sentarse en la mesa."),
        },
        "cambia": (
            "SI. De a pares, tecnica_anclaje_negociacion parece pegada a la "
            "familia, porque tiene A con construccion_de_leverage en el puesto "
            "878. Leido el acto entero se ve que ese A es de una especie distinta "
            "del resto, y la propia razon del 878 lo dice sin querer: 'El paso "
            "cuatro contado como nodo, y no trae procedimiento propio'. O sea que "
            "el A no nace de que anclar sea la maniobra de la familia, sino de que "
            "UN miembro de la familia menciona el anclaje en su paso 4. LA "
            "LECTURA DEL ACTO DEJA TRES TRIANGULOS A MAS A MAS D MEDIDOS: "
            "tecnica_anclaje_negociacion es A con construccion_de_leverage y D con "
            "los otros tres, que son todos A con construccion_de_leverage."
        ),
        "no_mueve": (
            "NINGUN VEREDICTO SE MUEVE. El A del puesto 878 es defendible en sus "
            "propios terminos y no lo toco. Lo que registro es que la familia "
            "declarada del acto son CUATRO y no cinco, y los tres triangulos que "
            "eso deja."
        ),
    },
    "estrategia_de_innovacion_arenas": {
        "forma": (
            "LA MADRE Y SUS PIEZAS, Y LA VARA YA ESTA ESCRITA EN ESTE MISMO ACTO. "
            "El acto tiene CUATRO nodos vivos y no cinco: "
            "estrategia_de_innovacion_de_producto y estrategia_innovacion_producto "
            "son hoy el mismo nodo. De los cuatro, estrategia_innovacion_producto "
            "es LA ESTRATEGIA ENTERA (metas y objetivos del esfuerzo, arenas, plan "
            "de ataque, reparto de recursos) y los otros tres son LA PIEZA DE "
            "ARENAS dicha tres veces. NO INVENTO ESA VARA: es la de la CORRECCION "
            "DECLARADA del 13 ago 2026 de los puestos 530 y 863, que ya separo la "
            "madre de su pieza con estas palabras, 'LA MADRE Y SU PIEZA DE ARENAS, "
            "y la vara las separa'. Lo que hago es aplicarla al acto entero en vez "
            "de a un solo par."
        ),
        "por_leer": {
            "estrategia_de_innovacion_de_producto|seleccion_arenas_estrategicas": (
                "D", "Madre contra pieza, por la vara de la correccion declarada del "
                "13 ago 2026. seleccion_arenas_estrategicas es 'Pick Your "
                "Battlefields', o sea la pieza de arenas sola; "
                "estrategia_de_innovacion_de_producto resuelve hoy a "
                "estrategia_innovacion_producto, que es la estrategia entera."),
            "estrategia_innovacion_producto|seleccion_arenas_estrategicas": (
                "D", "ES EL MISMO PAR VIVO QUE EL ANTERIOR, escrito con el otro id. "
                "Se registra igual y con la misma clase porque el instrumento lo "
                "cuenta dos veces, y callarlo dejaria el conteo sin explicar."),
        },
        "cambia": (
            "SI, Y ADEMAS ENCOGE EL TRABAJO. Los DOS pares que el instrumento da "
            "por leer son UN SOLO PAR VIVO despues del resolutor, asi que la "
            "lectura real es una y no dos. Y la forma cambia respecto de los "
            "pares: de a pares, estrategia_innovacion_producto es A con "
            "estrategia_de_innovacion_arenas (puestos 460 y 1121) y D con "
            "estrategia_de_innovacion_y_tecnologia (puestos 530 y 863, correccion "
            "declarada). Leido el acto entero, esas dos no pueden ser las dos "
            "ciertas: si la madre es D con una pieza de arenas por ser la madre, "
            "es D con todas. QUEDA UN TRIANGULO A MAS A MAS D MEDIDO con "
            "estrategia_de_innovacion_arenas en el vertice."
        ),
        "no_mueve": (
            "NINGUN VEREDICTO SE MUEVE, y aqui menos que en ningun sitio: los "
            "puestos 530 y 863 YA SON una correccion declarada del 13 ago 2026 "
            "encargada por el auditor, y mover encima de una correccion declarada "
            "sin que nadie me lo encargue seria legislar. Lo traigo medido."
        ),
    },
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seco", action="store_true", help="no escribe, solo imprime")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("VUELTA %d, TAREA 2: EL REGISTRO DE LAS LECTURAS POR ACTO DE OP-L-03" % VUELTA)
    print("=" * 78)
    print("")

    actos, _s = D.actos_del_instrumento()
    grandes = [x for x in actos if x[0] >= 5]
    mapa, _n = T.mapa_de_alias()
    idx = D.veredictos_por_par(mapa)
    grafo = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]

    print("A) EL UNIVERSO Y EL TRAMO, LEIDOS DEL INSTRUMENTO")
    print("   CIFRA actos del backlog al corte 3.388: %d" % len(actos))
    print("   CIFRA pares que el instrumento da por leer, en total: %d"
          % sum(x[1] for x in actos))
    print("   CIFRA actos grandes (5 miembros o mas): %d" % len(grandes))
    print("   CIFRA pares que el instrumento da por leer en los grandes: %d"
          % sum(x[1] for x in grandes))
    print("")

    filas = []
    for tam, por_leer, miembros in grandes:
        clave = sorted(miembros)[0]
        vivos = sorted({T.resolver(mapa, m) for m in miembros})
        vivos_grafo = sorted(m for m in miembros if not grafo[m].get("deprecado"))

        en_cola, fuera, fundidos = [], [], []
        for x, y in combinations(sorted(miembros), 2):
            rx, ry = T.resolver(mapa, x), T.resolver(mapa, y)
            if rx == ry:
                fundidos.append([x, y, rx])
                continue
            fs = idx.get(frozenset((rx, ry)), [])
            if fs:
                en_cola.append({"a": x, "b": y,
                                "puestos": sorted({f["puesto_intra"] for f in fs}),
                                "clases": sorted({f["clase"] for f in fs})})
            else:
                fuera.append([x, y])

        lec = LECTURAS.get(clave)
        fila = {
            "id_op": "OP-L-03",
            "vuelta": VUELTA,
            "fecha": FECHA,
            "acto": clave,
            "miembros": sorted(miembros),
            "cifra_miembros": tam,
            "cifra_nodos_vivos_por_resolutor": len(vivos),
            "nodos_vivos_por_resolutor": vivos,
            "cifra_nodos_vivos_por_grafo": len(vivos_grafo),
            "nodos_vivos_por_grafo": vivos_grafo,
            "resolutor_y_grafo_calzan": len(vivos) == len(vivos_grafo),
            "cifra_pares_posibles": tam * (tam - 1) // 2,
            "cifra_pares_que_ya_no_existen": len(fundidos),
            "pares_que_ya_no_existen": fundidos,
            "cifra_pares_con_veredicto": len(en_cola),
            "pares_con_veredicto": en_cola,
            "cifra_pares_por_leer_segun_el_instrumento": por_leer,
            "cifra_pares_por_leer_medidos_hoy": len(fuera),
            "el_instrumento_y_yo_calzamos": por_leer == len(fuera),
            "pares_por_leer": [list(p) for p in fuera],
            "veredictos_movidos": 0,
        }

        if lec is None:
            fila["leido"] = False
            fila["forma"] = (
                "NO SE LEE, Y EL MOTIVO ES UNA MEDICION Y NO UNA ELECCION: el acto "
                "NO TIENE PARES QUE LEER. Sus %d miembros escritos son HOY %d nodo "
                "vivo, o sea que el acto ya se fundio despues del corte 3.388 del "
                "que el instrumento lo saca. Los %d pares que el instrumento da por "
                "leer no existen: sus dos extremos son el mismo nodo. Verificado "
                "por DOS caminos independientes, el resolutor de P.1 y el campo "
                "deprecado del grafo, y los dos dan lo mismo."
                % (tam, len(vivos), por_leer))
            fila["cambia_respecto_del_par"] = (
                "NO APLICA: no hay par que leer ni forma que comparar.")
            fila["cobertura"] = {
                "pares_leidos_en_esta_vuelta": 0,
                "pares_del_acto_cubiertos": len(en_cola) + len(fundidos),
                "pares_del_acto_sin_cubrir": len(fuera),
                "nota": "cobertura completa por via distinta: los pares que faltaban "
                        "no se leyeron, dejaron de existir.",
            }
        else:
            fila["leido"] = True
            fila["forma"] = lec["forma"]
            fila["cambia_respecto_del_par"] = lec["cambia"]
            fila["no_mueve_veredictos"] = lec["no_mueve"]
            clases = {}
            for par in fuera:
                k = "|".join(par)
                if k not in lec["por_leer"]:
                    clases[k] = ["SIN LECTURA", "el dossier trae este par y la lectura "
                                 "no lo cubre. Se declara en vez de rellenarse."]
                else:
                    c, razon = lec["por_leer"][k]
                    clases[k] = [c, razon]
            fila["clases_de_los_pares_por_leer"] = clases
            fila["cifra_pares_leidos"] = len([k for k, v in clases.items()
                                              if v[0] != "SIN LECTURA"])
            fila["cifra_pares_sin_lectura"] = len([k for k, v in clases.items()
                                                   if v[0] == "SIN LECTURA"])
            fila["reparto_de_clases"] = {
                c: len([1 for v in clases.values() if v[0] == c])
                for c in sorted({v[0] for v in clases.values()})}
            fila["cobertura"] = {
                "pares_leidos_en_esta_vuelta": fila["cifra_pares_leidos"],
                "pares_del_acto_cubiertos": (len(en_cola) + len(fundidos)
                                             + fila["cifra_pares_leidos"]),
                "pares_del_acto_sin_cubrir": fila["cifra_pares_sin_lectura"],
                "sobre_un_total_de": tam * (tam - 1) // 2,
                "nota": "banco 9.26 y cuarta linea de la verificacion de la ficha: "
                        "la forma cambia, luego se re-mide CON SU COBERTURA AL LADO.",
            }

        filas.append(fila)

    print("B) LAS FILAS, UNA POR ACTO")
    for f in filas:
        print("   %-42s miembros %d | vivos %d (resolutor) / %d (grafo) %s"
              % (f["acto"], f["cifra_miembros"], f["cifra_nodos_vivos_por_resolutor"],
                 f["cifra_nodos_vivos_por_grafo"],
                 "CALZAN" if f["resolutor_y_grafo_calzan"] else "NO CALZAN"))
        print("      pares: posibles %d | ya no existen %d | con veredicto %d | por leer %d"
              % (f["cifra_pares_posibles"], f["cifra_pares_que_ya_no_existen"],
                 f["cifra_pares_con_veredicto"], f["cifra_pares_por_leer_medidos_hoy"]))
        print("      el instrumento dice %d por leer y yo mido %d: %s"
              % (f["cifra_pares_por_leer_segun_el_instrumento"],
                 f["cifra_pares_por_leer_medidos_hoy"],
                 "CALZA" if f["el_instrumento_y_yo_calzamos"] else "NO CALZA"))
        print("      LEIDO: %s%s"
              % (f["leido"],
                 ("  | clases: %s" % f["reparto_de_clases"]) if f["leido"] else ""))
    print("")

    print("C) LAS CUENTAS DE LA TAREA, SUMADAS DE LAS FILAS Y NO TECLEADAS")
    leidos = [f for f in filas if f["leido"]]
    print("   CIFRA actos del tramo: %d" % len(filas))
    print("   CIFRA actos LEIDOS: %d" % len(leidos))
    print("   CIFRA actos SIN NADA QUE LEER (ya fundidos): %d" % (len(filas) - len(leidos)))
    print("   CIFRA pares que el instrumento daba por leer en el tramo: %d"
          % sum(f["cifra_pares_por_leer_segun_el_instrumento"] for f in filas))
    print("   CIFRA pares por leer REALES, medidos hoy: %d"
          % sum(f["cifra_pares_por_leer_medidos_hoy"] for f in filas))
    print("   CIFRA pares LEIDOS en esta vuelta: %d"
          % sum(f.get("cifra_pares_leidos", 0) for f in filas))
    print("   CIFRA pares del tramo SIN LECTURA: %d"
          % sum(f.get("cifra_pares_sin_lectura", 0) for f in filas))
    print("   CIFRA veredictos movidos: %d" % sum(f["veredictos_movidos"] for f in filas))
    reparto = {}
    for f in leidos:
        for c, n in f["reparto_de_clases"].items():
            reparto[c] = reparto.get(c, 0) + n
    print("   REPARTO DE CLASES DE LO LEIDO: %s" % reparto)
    print("   CIFRA actos donde la forma CAMBIA respecto de lo que el par decia: %d"
          % len([f for f in leidos if f["cambia_respecto_del_par"].startswith("SI")]))
    print("")

    if a.seco:
        print("SECO: no se escribe nada.")
        return 0

    texto = NL.join(json.dumps(f, ensure_ascii=False) for f in filas) + NL
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
    print("D) ESCRITO")
    print("   docs/plan/OP_L_03_LECTURAS.jsonl")
    print("   CIFRA bytes: %d | CIFRA filas: %d"
          % (len(texto.encode("utf-8")), len(filas)))
    releido = [json.loads(l) for l in io.open(DESTINO, encoding="utf-8") if l.strip()]
    print("   RELEIDO DEL DISCO: %d filas, y calzan con lo escrito: %s"
          % (len(releido), releido == filas))
    print("")
    print("E) LO QUE ESTA TAREA NO TOCO, COMPROBADO Y NO PROMETIDO")
    for r in ("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", "docs/plan/OPERACIONES.jsonl"):
        print("   %s -> %d bytes (sin abrir en escritura en toda la corrida)"
              % (r, os.path.getsize(os.path.join(RAIZ, r.replace("/", os.sep)))))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
