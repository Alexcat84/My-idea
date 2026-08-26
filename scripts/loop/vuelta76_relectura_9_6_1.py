"""VUELTA 76, TAREA 2.1: relectura al doble del tramo 1, vara 9.6.1 completa
(la mayoria de la madre) par a par, sobre las 25 aristas que quedan tras la
reversion de 1.3.a. Ademas, el chequeo de escalera (P.9.1 esta en script
aparte).

METODO, declarado porque no es lectura semantica plena de cada nodo hermano
(eso ya lo hizo la lectura 9.6.2 al escribir el tramo 1, puesto/razon citada
en PARES_SANOS): para cada madre se mide N = numero de pasos_accionables y
L = numero de nodos_siguientes VIVOS que tiene HOY (post reversión, post
tramo 1). Si L es MAYORIA ESTRICTA de N, la silueta CONFIRMA la jerarquia
establecida (9.6.1 mayoria manda) y el par queda respaldado dos veces. Si L
es la mitad o menos, la silueta ni exculpa ni acusa y el veredicto sigue
descansando en 9.6.2 (contenido), que es la lectura ya hecha al escribir el
par: eso se marca DEJA IGUAL, NO CONFIRMA NI VOLTEA. Ninguna de las dos
lecturas revierte una arista por si sola: 9.6.1 es un respaldo o un silencio,
nunca un veto en solitario contra 9.6.2 ya leido linea a linea.

Chequeo de escalera, exacto y barato: para cada par (madre, hijo), si el
hijo ya trae a la madre en su nodos_siguientes, hay ciclo de dos.

CORRECCION DECLARADA (vuelta 77, parada del 26 ago 2026,
docs/loop/paradas/2026-08-26-racha-tramo-mecanico-DECISION.md): la version
original de este script NO filtraba deprecado en ninguna linea. La linea
vieja era:
    siguientes = [s for s in (madre.get("nodos_siguientes") or [])]
o sea que L contaba TODOS los nodos_siguientes de la madre, vivos o no,
mientras el docstring y el reporte de la vuelta 76 publicaban la cifra como
si fuera solo de hijos VIVOS. La funcion cargar_siguientes_vivos() de abajo
sustituye esa linea: ahora L es de verdad el numero de nodos_siguientes con
deprecado distinto de True. El texto viejo de este parrafo no se borra.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

PARES = [
    ("adaptar_empaque_segun_tipo_de_articulo", "proteger_fragiles_caja_dentro_de_caja"),
    ("adn_de_innovacion_organizacional", "espacios_fisicos_de_innovacion"),
    ("analisis_capacidad_proceso", "capacidad_del_proceso"),
    ("brecha_de_calidad_cuatro_gaps", "capacidad_del_proceso"),
    ("contractor_status_report", "project_performance_report"),
    ("cultura_justa_2", "justicia_restaurativa"),
    ("customer_creation", "determinar_tipo_de_mercado"),
    ("definiciones_operacionales_de_calidad", "ctq_caracteristicas_criticas"),
    ("desarrollo_de_controles_de_proceso", "decision_conformidad_producto"),
    ("dmadv_fase_verificacion", "analisis_de_sistemas_de_medicion_msa"),
    ("evitar_pseudociencia_producto", "metricas_accionables"),
    ("franquicia_unidad_individual", "proceso_venta_franquicias"),
    ("funnel_get_customers_optimizacion", "disenar_tests_pass_fail"),
    ("identificar_caracteristicas_metas_proceso", "diseno_de_procesos_por_caracteristicas"),
    ("marco_analisis_mercado_cadena_suministro", "ciclo_de_conversion_de_efectivo"),
    ("mobilizar_empleados_cultura_ecologica", "evaluacion_actitudes_empleados"),
    ("pivot_post_ventas", "value_proposition_startup"),
    ("plan_cambio_climatico", "establecer_metas_reduccion_emisiones"),
    ("planificacion_estrategica_despliegue", "definir_mision_organizacional"),
    ("planificacion_inicial_calidad", "analisis_flujo_proceso"),
    ("project_close_out", "project_charter"),
    ("recursos_apoyo_gubernamental_exportacion", "programas_ex_im_bank"),
    ("resumen_de_datos_graficos", "medidas_tendencia_dispersion"),
    ("six_sigma_dmaic", "replicar_resultados"),
    ("verificar_clientes_y_canales", "dia_en_la_vida_del_cliente"),
]


def cargar(node_id):
    with open(NODOS / f"{node_id}.json", encoding="utf-8") as f:
        return json.load(f)


def cargar_siguientes_vivos(madre):
    """L de verdad: solo los nodos_siguientes cuyo propio nodo NO esta deprecado."""
    vivos = []
    for s in (madre.get("nodos_siguientes") or []):
        sd = cargar(s)
        if not sd.get("deprecado"):
            vivos.append(s)
    return vivos


def main():
    escalera_rota = []
    for madre_id, hijo_id in PARES:
        madre = cargar(madre_id)
        hijo = cargar(hijo_id)

        n_pasos = len(madre.get("pasos_accionables") or [])
        siguientes = cargar_siguientes_vivos(madre)
        l_ligados = len(siguientes)
        mayoria = l_ligados > n_pasos / 2

        # escalera: el hijo ya apunta a la madre?
        ciclo = madre_id in (hijo.get("nodos_siguientes") or [])
        if ciclo:
            escalera_rota.append((madre_id, hijo_id))

        veredicto = "9.6.1 CONFIRMA (mayoria establecida)" if mayoria else "9.6.1 DEJA IGUAL (mitad o menos, manda 9.6.2 ya leida)"
        print(f"{madre_id} -> {hijo_id}")
        print(f"    N pasos={n_pasos}, L ligados={l_ligados}, mayoria={'SI' if mayoria else 'NO'} -> {veredicto}")
        print(f"    escalera (hijo ya apunta a madre)={'SI - ROTA' if ciclo else 'NO'}")

    print()
    print(f"TOTAL PARES: {len(PARES)}")
    print(f"ESCALERA ROTA (ciclo de dos): {len(escalera_rota)} de {len(PARES)}")
    if escalera_rota:
        for m, h in escalera_rota:
            print(f"  {m} -> {h}")


if __name__ == "__main__":
    main()
