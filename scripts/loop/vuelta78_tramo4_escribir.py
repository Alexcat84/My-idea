"""VUELTA 78, TAREA 4: OP-E-01, TRAMO 4. Escribe en dataset/nodos/<madre>.json
las aristas nuevas confirmadas por lectura par a par (9.6.2 contenido, con
9.6.1 y escalera chequeados igual que en los tramos anteriores), leidas
contra la cabeza de la bolsa recalibrada FRESCA de esta vuelta y ya
filtrada por el P.9.1 ENSANCHADO CON LA VARA DE LOS A
(docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V78.jsonl,
docs/loop/SALIDA_V78_TRAMO4_FILTRO_P91.txt).

CRITERIO ADJUDICADO PARA ESTE TRAMO (encargo, TAREA 4, sin cambio sobre el
de tramos anteriores): veredicto del cribado PRIMERO; el sufijo numerico y
el racimo solo opinan cuando NO hay veredicto (y ya lo cubre el filtro
P.9.1); cuando el paso que el calibrador senala no es el que calza, manda
la lectura (adjudicado en el acta 77, D1).

De los 30 primeros candidatos limpios (docs/loop/SALIDA_V78_TRAMO4_DOSSIER30.txt),
DOS tenian veredicto propio: puesto 3205 (D, sujetos_de_control ->
key_process_product_characteristics: "ficha nombrada dentro del paso de
otro nodo, figura reconocida") y puesto 637 (B,
equipo_customer_development -> customer_development_team: la propia razon
del cribado dice "Sin arista entre ellos", asi que ESE par no se escribe
aunque su clase no sea A, por mandato expreso del archivo). Los otros 28
sin veredicto, decididos por 9.6.2 (contenido).

SEIS de los 30 se leen y NO se escriben:
- equipo_customer_development -> customer_development_team: veredicto
  propio B, y el archivo dice con estas palabras "Sin arista entre ellos".
- clasificacion_tipos_activos -> tipos_de_pasivos: el paso senalado
  clasifica ACTIVOS; el hijo entero es sobre PASIVOS, un objeto distinto
  con estructura de pasos parecida (mismo libro) pero sin relacion de
  procedimiento. Gemelo estructural, no jerarquia.
- proceso_llamada_inicial_venta -> proceso_venta_franquicias: el hijo es
  el proceso de venta ENTERO (mas amplio que la llamada inicial) y ningun
  paso del hijo elabora especificamente el paso 6 senalado (entender el
  proceso de decision del comprador); la relacion natural es la inversa
  (la llamada inicial es una pieza del proceso completo, no al reves).
- preparacion_preguntas_problema_precall -> preguntas_situacion: dentro
  del marco SPIN, Preguntas de Problema y Preguntas de Situacion son DOS
  categorias hermanas, no madre e hijo; el paso senalado solo menciona
  "minimizar" el otro tipo de pregunta como beneficio colateral.
- timing_solicitud_referidos -> fase_adopt_ciclo_cliente: el paso senalado
  nombra la fase Adopt solo como ejemplo parentetico ("ej: fase
  Adopt/Advocate"); el contenido del hijo (los seis canales, la encuesta
  de exito, el ritual de hitos) es la fase COMPLETA del ciclo del cliente
  de Coleman, mucho mas amplia que "cuando pedir un referido". Match
  debil, direccion de generalidad al reves.
- requisitos_numericos_calidad_lotes -> critica_acceptable_quality_level:
  el hijo (Crosby) es una CRITICA al uso del AQL que el paso de la madre
  (Juran) recomienda definir; no es un procedimiento de como hacer el
  paso, es un contrapunto de otro autor. Discutible marcado: la tension
  entre las dos fuentes es real y vale la pena, pero no es jerarquia
  9.6.2.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

PARES_SANOS = [
    ("necesidades_reales_vs_declaradas", "descubrir_necesidades_del_cliente",
     "paso 2 es la linea (traducir necesidades declaradas a reales); el hijo trae el procedimiento propio de 6 pasos que distingue declaradas/reales/percibidas/culturales. sin veredicto de cribado"),
    ("sujetos_de_control", "key_process_product_characteristics",
     "paso 3 nombra traducir la voz del cliente en KPC sin desplegar la mecanica; el hijo trae el procedimiento completo de clasificacion (critica/mayor/menor/incidental). VEREDICTO DEL CRIBADO: puesto 3205, clase D, 'ficha nombrada dentro del paso de otro nodo, figura reconocida'"),
    ("metas_desmaterializacion_energia", "establecer_metas_reduccion_emisiones",
     "paso 2 es la linea (establecer metas cuantitativas de reduccion); el hijo trae el procedimiento propio de fijacion de metas de emision (linea base, plazos, comunicacion, explicaciones). sin veredicto de cribado"),
    ("diferencia_iso9001_iso9004", "trilogia_de_juran",
     "paso 3 es la linea (incorporar metodos de planificacion, control y mejora en todos los procesos); el hijo ES esos tres metodos, con procedimiento propio de 6 pasos. DISCUTIBLE: la trilogia es un marco mas fundamental que la comparacion de normas que la nombra; se escribe porque el paso 3 la cita como el metodo a incorporar, pero la direccion de generalidad merece relectura. sin veredicto de cribado"),
    ("aprobacion_alta_direccion", "metas_negocio_calidad",
     "paso 2 es la linea (cuantificar oportunidades via costo de mala calidad); el hijo trae el procedimiento propio de traducir amenazas/oportunidades en metas del plan de negocio. sin veredicto de cribado"),
    ("seguimiento_cumplimiento_cadena_suministro", "auditorias_proveedores",
     "paso 2 es la linea (auditorias periodicas de cumplimiento a proveedores); el hijo ES ese mecanismo de auditoria con procedimiento propio de 4 pasos (GEMI). sin veredicto de cribado"),
    ("gestion_diferencias_culturales", "participacion_ferias_comerciales",
     "paso 7 nombra asistir a ferias comerciales explicitamente; el hijo ES esa participacion con procedimiento propio de 6 pasos. sin veredicto de cribado"),
    ("decision_momento_fundacion", "evaluacion_conocimiento_industria",
     "paso 3 es la linea (revisar cuanto conoces la industria); el hijo ES esa evaluacion con procedimiento propio de 4 pasos. sin veredicto de cribado"),
    ("actualizar_business_model_canvas_tuneup", "value_proposition_startup",
     "paso 1 es la linea (revisar la propuesta de valor a la luz del feedback); el hijo ES el procedimiento de definir la propuesta de valor. NODO HUB: value_proposition_startup ya tiene 17 madres y 26 hijos en el grafo, patron establecido de concepto ampliamente citado. sin veredicto de cribado"),
    ("etapa_build_business_case", "value_proposition_startup",
     "paso 1 nombra definir la propuesta de valor del producto; mismo hijo hub que el par anterior, mismo patron establecido. sin veredicto de cribado"),
    ("extraer_priorizar_hipotesis", "value_proposition_startup",
     "paso 1 nombra la propuesta de valor entre lo que hay que testear; mismo hijo hub. sin veredicto de cribado"),
    ("optimizacion_embudo_get_customers", "mvp_alta_fidelidad",
     "paso 1 nombra el MVP de alta fidelidad como precondicion sin desplegarlo; el hijo ES ese MVP con procedimiento propio de 5 pasos. sin veredicto de cribado"),
    ("producto_mercado_fit_motores", "contabilidad_innovacion",
     "paso 4 nombra la contabilidad de innovacion como la herramienta de decision; el hijo ES esa contabilidad con procedimiento propio de 7 pasos. sin veredicto de cribado"),
    ("technology_platform_evaluation", "stage_gate_td_tecnologia",
     "paso 2 nombra el proceso especial Stage-Gate-TD explicitamente; el hijo ES ese modelo con procedimiento propio de 5 pasos. sin veredicto de cribado"),
    ("ventaja_competitiva_producto", "value_proposition_startup",
     "paso 3 nombra dejar explicita la propuesta de valor; mismo hijo hub que los tres pares anteriores. sin veredicto de cribado"),
    ("conformidad_comercio_internacional", "sistema_gestion_calidad",
     "paso 4 es la linea (unificar el sistema de gestion de calidad); el hijo ES ese sistema con procedimiento propio de 4 pasos. DISCUTIBLE: el sistema de gestion de calidad es un concepto mas amplio que la conformidad de comercio internacional que lo nombra; se escribe porque el paso 4 lo cita como la accion a tomar, pero merece relectura de direccion. sin veredicto de cribado"),
    ("viaje_diagnostico_remedial", "resistencia_al_cambio",
     "paso 7 nombra gestionar la resistencia al cambio explicitamente; el hijo ES ese fenomeno con procedimiento propio de 4 pasos. sin veredicto de cribado"),
    ("breakthrough_cultural", "reconocimiento_publico_recompensas",
     "paso 3 es la linea (reforzar comportamientos con reconocimiento y recompensas); el hijo ES esa estrategia con procedimiento propio de 4 pasos. sin veredicto de cribado"),
    ("auditoria_de_proceso", "seguimiento_accion_correctiva",
     "paso 5 es la linea (dar seguimiento a la accion correctiva); el hijo ES ese seguimiento con procedimiento propio de 4 pasos. sin veredicto de cribado"),
    ("planificacion_inicial_calidad", "medicion_capacidad_servicio",
     "paso 5 es la linea (validar capacidad y sistemas de medicion); el hijo especializa esa validacion para el dominio de servicios, con procedimiento propio de 6 pasos. sin veredicto de cribado"),
    ("etapa_discovery_ideacion", "internal_idea_capture",
     "paso 1 es la linea (establecer un sistema formal de captura de ideas); el hijo ES ese sistema con procedimiento propio de 7 pasos. sin veredicto de cribado"),
    ("uso_inadecuado_computadoras", "causas_especiales_y_comunes_variacion",
     "paso 3 es la linea (distinguir causa comun de causa especial); el hijo ES esa distincion (Shewhart/Deming via Juran) con procedimiento propio de 4 pasos. sin veredicto de cribado"),
    ("diamante_de_innovacion", "asignacion_recursos_en_gates",
     "paso 2 es la linea (asegurar gestion de portafolio y asignacion de recursos); el hijo ES ese procedimiento de asignacion en gates, con 5 pasos propios. sin veredicto de cribado"),
    ("plan_cambio_climatico", "formar_consejo_asesor_sostenibilidad",
     "paso 5 es la linea (formar un consejo asesor ambiental externo); el hijo ES esa formacion de consejo con procedimiento propio de 4 pasos. sin veredicto de cribado"),
]

PARES_DESCARTADOS = [
    ("equipo_customer_development", "customer_development_team",
     "VEREDICTO DEL CRIBADO: puesto 637, clase B. El propio archivo dice, con estas palabras, "
     "'Sin arista entre ellos': comparten el paso de liderar la conversacion con clientes (paso "
     "1 de uno, paso 2 del otro) pero cada uno se abre despues por un lado distinto (diseno del "
     "equipo contra logistica de campo). No se enlaza, por mandato expreso del archivo."),
    ("clasificacion_tipos_activos", "tipos_de_pasivos",
     "el paso senalado (1) clasifica ACTIVOS; el hijo entero es sobre PASIVOS, un objeto "
     "financiero distinto con estructura de pasos parecida (mismo libro) pero sin relacion de "
     "procedimiento entre ellos. Gemelo estructural falso, no jerarquia. No se enlaza."),
    ("proceso_llamada_inicial_venta", "proceso_venta_franquicias",
     "el hijo es el proceso de venta de franquicias ENTERO, mas amplio que la llamada inicial; "
     "ningun paso del hijo elabora especificamente el paso 6 senalado (entender el proceso de "
     "decision del comprador). La relacion natural, si existe, es la inversa. No se enlaza."),
    ("preparacion_preguntas_problema_precall", "preguntas_situacion",
     "dentro del marco SPIN, Preguntas de Problema y Preguntas de Situacion son dos categorias "
     "hermanas del mismo modelo, no madre e hijo; el paso senalado solo menciona minimizar el "
     "otro tipo de pregunta como beneficio colateral, no lo desarrolla. No se enlaza."),
    ("timing_solicitud_referidos", "fase_adopt_ciclo_cliente",
     "el paso senalado nombra la fase Adopt solo como ejemplo parentetico ('ej: fase "
     "Adopt/Advocate'); el contenido del hijo es la fase COMPLETA del ciclo del cliente de "
     "Coleman (seis canales, encuesta de exito, ritual de hitos), mucho mas amplia que el "
     "momento de pedir un referido. Match debil, direccion de generalidad al reves. No se "
     "enlaza."),
    ("requisitos_numericos_calidad_lotes", "critica_acceptable_quality_level",
     "PENDIENTE DE DOCTRINA / DISCUTIBLE: el hijo (Crosby) es una CRITICA al uso del AQL que el "
     "paso de la madre (Juran) recomienda definir, no un procedimiento de como hacer ese paso. "
     "Es un contrapunto de otro autor sobre el mismo termino, no una jerarquia 9.6.2. No se "
     "enlaza."),
]


def cargar(node_id):
    p = NODOS / f"{node_id}.json"
    with open(p, encoding="utf-8") as f:
        return json.load(f), p


def main():
    tocados = []
    ya_estaban = []
    escalera_rota = []
    for madre_id, hijo_id, razon in PARES_SANOS:
        data, path = cargar(madre_id)
        hijo_data, hijo_path = cargar(hijo_id)

        if madre_id in (hijo_data.get("nodos_siguientes") or []):
            escalera_rota.append((madre_id, hijo_id))
            continue

        sig = data.get("nodos_siguientes") or []
        if hijo_id in sig:
            ya_estaban.append((madre_id, hijo_id))
            continue
        sig.append(hijo_id)
        data["nodos_siguientes"] = sig
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")

        # Reciproco explicito en el hijo (nodos_previos), para no depender
        # de que step5_symmetrize de run_phase1.py lo complete solo: como
        # ya se demostro en TAREA 3.2 de esta misma vuelta, escribir un
        # solo lado es fragil si algo lo revierte antes de correr el ciclo.
        prev = hijo_data.get("nodos_previos") or []
        if madre_id not in prev:
            prev.append(madre_id)
            hijo_data["nodos_previos"] = prev
            with open(hijo_path, "w", encoding="utf-8") as f:
                json.dump(hijo_data, f, ensure_ascii=False, indent=2)
                f.write("\n")

        tocados.append((madre_id, hijo_id))

    print(f"ARISTAS ESCRITAS: {len(tocados)}")
    for m, h in tocados:
        print(f"  {m} -> {h}")
    if ya_estaban:
        print(f"YA EXISTIAN (no tocadas, declarado): {len(ya_estaban)}")
        for m, h in ya_estaban:
            print(f"  {m} -> {h}")
    print(f"ESCALERA ROTA (ciclo de dos, hijo ya apuntaba a la madre): {len(escalera_rota)}")
    for m, h in escalera_rota:
        print(f"  {m} -> {h}")
    print(f"DESCARTADOS: {len(PARES_DESCARTADOS)}")
    for m, h, r in PARES_DESCARTADOS:
        print(f"  {m} -> {h} | {r}")


if __name__ == "__main__":
    main()
