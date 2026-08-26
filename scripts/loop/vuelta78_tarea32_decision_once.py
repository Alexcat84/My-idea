"""VUELTA 78, TAREA 3.2: decision par a par de las 11 aristas de la fase 04
que la vara de los veredictos A toca (docs/loop/SALIDA_V78_TAREA3_DOSSIER_ONCE.txt).

Criterio aplicado, uno solo para las once, sin barrido en bloque
(EJECUTOR.md regla 5, no inventar reglas: se apoya en P.9 punto 1 "los
enlaces corren DESPUES de las fusiones que tocan sus destinos" y punto 2
"el id escrito es el que estara vivo"):

  - Si el extremo ESCRITO en la arista (madre o hijo, el nodo que la arista
    usa de verdad) esta el mismo condenado por una operacion (eliminar sin
    ser el superviviente, o nodos de un RENOMBRE_CON_ALIAS): SE MUEVE
    (revierte), porque la arista quedaria huerfana cuando la operacion
    corra.
  - Si el extremo ESCRITO es el `superviviente` declarado de la operacion
    que condena a su companero de A: SE QUEDA, por cita textual de P.9
    punto 2 (el id escrito YA es el que estara vivo).
  - Si NINGUNA operacion condena al extremo escrito (solo al companero
    ajeno al par, o a nadie): SE QUEDA, porque hoy no hay plan que la
    contradiga; se registra el hallazgo si el companero SI esta en una
    nomina activa (senal de trabajo futuro, no motivo de reversion hoy).

Aplicado a las once, leido del dossier
(docs/loop/SALIDA_V78_TAREA3_DOSSIER_ONCE.txt):

1. concepto_proyecto_breakthrose -> pocos_vitales_muchos_utiles: ni madre ni
   hijo condenados; companero proyectos_vitales_pocos sin operacion, y la
   propia razon del cribado dice "el acto es POR ELEGIR" (fusion mutua sin
   ganador). SE QUEDA.
2. customer_validation -> mvp_alta_fidelidad: la madre customer_validation
   ES el `superviviente` declarado de OP-M-05-APERTURA, que condena
   (`eliminar`) a los dos companeros de sus A vivos (filosofia_customer_validation,
   introduccion_validacion_clientes). El id escrito YA es el que estara
   vivo. SE QUEDA, por P.9 punto 2.
3. customer_validation -> prueba_mvp_alta_fidelidad: mismo caso que 2, misma
   madre. SE QUEDA.
4. earlyvangelists_ventas_tempranas -> value_proposition_startup: ni madre
   ni hijo condenados por ninguna operacion (el companero de su A,
   filosofia_customer_validation, si esta condenado por OP-M-05-APERTURA,
   pero ese companero no es ni la madre ni el hijo de ESTA arista). SE
   QUEDA, con nota: earlyvangelists_ventas_tempranas repite con un nodo que
   OP-M-05-APERTURA ya va a eliminar, y ninguna operacion lo incluye
   todavia; queda para cuando esa familia se revise.
5. ecuacion_de_valor_cliente -> preguntas_need_payoff: los tres companeros
   de las tres A de la madre estan sin operacion. SE QUEDA.
6. estrategia_de_innovacion_arenas -> product_roadmap_estrategico: dos de
   los cuatro companeros SI estan en la nomina de OP-S-09, pero la propia
   razon del cribado (puesto 460) dice que esta familia de SEIS nodos "se
   decide en mesa, no aqui": no hay operacion que condene a
   estrategia_de_innovacion_arenas en si. SE QUEDA, con el hallazgo
   registrado.
7. franquicia_unidad_individual -> programa_de_referidos_de_franquiciados:
   ni madre ni hijo condenados. SE QUEDA.
8. funnel_get_customers_optimizacion -> disenar_tests_pass_fail: ni madre ni
   hijo condenados. SE QUEDA.
9. screening_mercados_potenciales -> uso_del_us_commercial_service: ni
   madre ni hijo condenados; uno de los dos companeros (consejos_distrito_exportacion_dec)
   ya esta DEPRECADO, asi que esa A ya esta resuelta por otra via y ni
   siquiera cuenta para la vara (que solo mira A con los DOS extremos
   vivos). SE QUEDA.
10. testing_process_completo -> value_proposition_canvas: ni madre ni hijo
    condenados; un companero (customer_profile_value_map) ya esta
    DEPRECADO, la otra A (design_test_repeat) sin operacion. SE QUEDA.
11. waterfall_vs_agile_development -> desarrollo_de_clientes_customer_development:
    el HIJO ESCRITO, desarrollo_de_clientes_customer_development, tiene una
    A VIVA (puesto 1052) con customer_development_modelo, que SI esta en
    la nomina de OP-S-09 (RENOMBRE_CON_ALIAS). El hijo escrito NO esta el
    mismo en esa nomina (es justo el sinonimo puro que el metodo lexico no
    detecto, seccion 1.7 del acta 77 y D4). No hay operacion que declare a
    desarrollo_de_clientes_customer_development como el id que sobrevivira
    frente a su gemelo YA anotado para renombre. SE MUEVE: la arista se
    revierte hoy y espera a que OP-S-09 (o una adjudicacion de mesa) fije
    cual de los dos ids sera el vivo.

RESULTADO: 10 SE QUEDAN, 1 SE MUEVE (revertida).
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

REVERTIR = [
    ("waterfall_vs_agile_development", "desarrollo_de_clientes_customer_development",
     "el hijo tiene un A vivo (puesto 1052) con customer_development_modelo, YA en la "
     "nomina de OP-S-09 (RENOMBRE_CON_ALIAS); el hijo mismo no esta en esa nomina "
     "(sinonimo puro no detectado por el metodo lexico, D4 acta 77) y ninguna operacion "
     "declara cual de los dos sobrevivira: se revierte y espera a OP-S-09 o a mesa."),
]

SE_QUEDAN = [
    ("concepto_proyecto_breakthrough", "pocos_vitales_muchos_utiles",
     "ni madre ni hijo condenados; companero sin operacion y la razon del cribado (2575) "
     "declara 'el acto es POR ELEGIR', fusion mutua sin ganador."),
    ("customer_validation", "mvp_alta_fidelidad",
     "la madre ES el superviviente declarado de OP-M-05-APERTURA, que condena a los dos "
     "companeros de sus A vivos: el id escrito YA es el que estara vivo (P.9 punto 2)."),
    ("customer_validation", "prueba_mvp_alta_fidelidad",
     "mismo caso: la madre es el superviviente declarado de OP-M-05-APERTURA."),
    ("earlyvangelists_ventas_tempranas", "value_proposition_startup",
     "ni madre ni hijo condenados por ninguna operacion; el companero de su A si lo esta, "
     "pero no es ni madre ni hijo de esta arista."),
    ("ecuacion_de_valor_cliente", "preguntas_need_payoff",
     "los tres companeros de sus tres A estan sin operacion que los condene."),
    ("estrategia_de_innovacion_arenas", "product_roadmap_estrategico",
     "dos companeros si estan en la nomina de OP-S-09, pero la propia razon del cribado "
     "(puesto 460) dice que esta familia de seis se decide en mesa, no por OP-S-09; la "
     "madre misma no esta condenada por ninguna operacion."),
    ("franquicia_unidad_individual", "programa_de_referidos_de_franquiciados",
     "ni madre ni hijo condenados."),
    ("funnel_get_customers_optimizacion", "disenar_tests_pass_fail",
     "ni madre ni hijo condenados."),
    ("screening_mercados_potenciales", "uso_del_us_commercial_service",
     "ni madre ni hijo condenados; uno de los companeros ya esta deprecado (A ya resuelta "
     "por otra via)."),
    ("testing_process_completo", "value_proposition_canvas",
     "ni madre ni hijo condenados; un companero ya esta deprecado, el otro sin operacion."),
]


def main():
    tocados = []
    for madre_id, hijo_id, razon in REVERTIR:
        p_madre = NODOS / f"{madre_id}.json"
        p_hijo = NODOS / f"{hijo_id}.json"
        data_madre = json.load(open(p_madre, encoding="utf-8"))
        data_hijo = json.load(open(p_hijo, encoding="utf-8"))

        sig = data_madre.get("nodos_siguientes") or []
        prev = data_hijo.get("nodos_previos") or []
        # LAS DOS VISTAS SE QUITAN A LA VEZ: run_phase1.py paso 5 reciproca
        # cualquier arista declarada por CUALQUIERA de los dos extremos, asi
        # que quitar solo un lado la deja viva por el otro y el ciclo la
        # repone sola (tropiezo cazado en esta misma vuelta, ver reporte).
        if hijo_id not in sig and madre_id not in prev:
            print(f"NO ESTABA (nada que revertir): {madre_id} -> {hijo_id}")
            continue
        if hijo_id in sig:
            sig.remove(hijo_id)
            data_madre["nodos_siguientes"] = sig
            with open(p_madre, "w", encoding="utf-8") as f:
                json.dump(data_madre, f, ensure_ascii=False, indent=2)
                f.write("\n")
        if madre_id in prev:
            prev.remove(madre_id)
            data_hijo["nodos_previos"] = prev
            with open(p_hijo, "w", encoding="utf-8") as f:
                json.dump(data_hijo, f, ensure_ascii=False, indent=2)
                f.write("\n")
        tocados.append((madre_id, hijo_id))
        print(f"REVERTIDA (las dos vistas): {madre_id} -> {hijo_id}")

    print()
    print(f"ARISTAS REVERTIDAS: {len(tocados)} de {len(REVERTIR)}")
    print(f"ARISTAS QUE SE QUEDAN: {len(SE_QUEDAN)}")
    for m, h, r in SE_QUEDAN:
        print(f"  QUEDA  {m} -> {h}")
    print()
    print(f"TOTAL DECIDIDO: {len(REVERTIR) + len(SE_QUEDAN)} de 11")


if __name__ == "__main__":
    main()
