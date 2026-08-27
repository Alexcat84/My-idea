# -*- coding: utf-8 -*-
"""VUELTA 80, TAREA 5: OP-E-01, TRAMO 6. Escribe en dataset/nodos/<madre>.json
las aristas nuevas confirmadas por lectura par a par (9.6.2 contenido, con la
vara nueva de la cadena y la escalera chequeadas), leidas contra la cabeza de
la bolsa recalibrada FRESCA de esta vuelta, filtrada por P.9.1 ENSANCHADO CON
LA VARA DE LOS A MAS LA GUARDA DEL PAR NO DIRIGIDO
(docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V80.jsonl,
docs/loop/SALIDA_V80_TRAMO6_FILTRO_P91_GUARDA_CADENA.txt) sobre el grafo YA
MOVIDO por la TAREA 3 de esta misma vuelta (reversion de D2 y D3).

CRITERIO ADJUDICADO (sin cambio sobre tramos anteriores): veredicto del
cribado PRIMERO; el sufijo numerico y el racimo solo opinan cuando NO hay
veredicto; cuando el paso que el calibrador senala no es el que calza, manda
la lectura (acta 77, D1); cuando el paso solo NOMBRA un objeto en vez de
mandar una accion sobre el, no hay jerarquia (acta 78, D3, banco 9.6.2); y
LA VARA NUEVA DE LA CADENA (acta 79, seccion 5 punto 6): si el hijo ya
cuelga de la cadena PROPIA de la madre (sus pasos enumerados, en el orden
que la madre declara), la arista es un radio sobre cableado ya establecido
y NO se escribe, aunque el contenido por si solo pasara 9.6.2 (leccion de
D2, revertida en la TAREA 3 de esta misma vuelta).

De las 30 primeras UNIDADES de lectura (guarda del par no dirigido
aplicada; 0 parejas esta vuelta), VEINTE (indices 0 a 19) YA ESTABAN
DECIDIDAS por vueltas anteriores de esta misma campana: las siete del tramo
4/D5 ya citadas en el tramo 5, las once PARES_DESCARTADOS_NUEVOS del tramo 5
(vuelta 79), y las DOS revertidas en la TAREA 3 de esta misma vuelta (D2 y
D3). Se citan sin re-derivar. Las DIEZ restantes (indices 20 a 29) son
lectura fresca de esta vuelta.

De esas diez: DOS se enlazan, SIETE no se enlazan con razon, y UNA
(descubrir_necesidades_del_cliente -> traduccion_necesidades_cliente) queda
DISCUTIBLE Y NO SE ESCRIBE, por el mismo patron de "redirect de paso" que la
TAREA 3 de esta misma vuelta acaba de revertir en D2: el paso que calza de
verdad no es el que el calibrador senalo, y aunque el contenido encaja, la
familia ya tiene un camino establecido mas especifico
(identificar_clientes_externos_e_internos -> customer_needs_spreadsheet ->
traduccion_necesidades_cliente) para la misma transicion. Se prefiere la
cautela inmediatamente despues de D2 a repetir el mismo error.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

# Las DOS aristas SANAS, con su razon.
PARES_SANOS = [
    ("curva_caracteristica_operativa", "distribucion_binomial",
     "paso 2 nombra LITERALMENTE la distribucion binomial como uno de los tres metodos "
     "(Poisson, binomial, hipergeometrica) para calcular la probabilidad de aceptacion; el "
     "hijo ES el procedimiento completo de esa distribucion especifica (definir n y p, calcular "
     "q, aplicar la formula o software, usar los resultados para disenar el plan de muestreo). "
     "La madre conserva materia propia en los otros 4 pasos (definir el plan, graficar la curva "
     "OC, analizar riesgos alfa/beta, ajustar el plan). Sin camino previo (huerfano de camino, "
     "banco 9.6). No hay hoy un nodo hermano de Poisson o hipergeometrica enlazado desde esta "
     "misma madre, asi que no hay patron de familia que contradiga esta especializacion."),
    ("desarrollo_de_controles_de_proceso", "bucle_retroalimentacion_control",
     "paso 2 es la linea literal ('Disenar el bucle de retroalimentacion y definir puntos de "
     "control en el diagrama de flujo'); el hijo ES ese bucle de retroalimentacion completo, con "
     "procedimiento propio de 5 pasos (sensor, unidad de medida/estandar, arbitro que compara, "
     "actuador que corrige, registro para trazabilidad). La madre conserva materia propia en los "
     "otros 5 pasos (identificar controles, establecer estandares y acciones correctivas, "
     "entrenar trabajadores, planificar la transferencia, planificar la auditoria). Sin camino "
     "previo (huerfano de camino, banco 9.6)."),
]

# Los SIETE pares leidos y NO escritos de esta lectura fresca, con su razon.
PARES_DESCARTADOS_NUEVOS = [
    ("control_calidad_operaciones_servicio", "descubrir_necesidades_del_cliente",
     "el paso 1 senalado ('Identificar el proceso principal, su objetivo, y las necesidades del "
     "cliente') es una linea de identificacion breve dentro de un ciclo de CONTROL de calidad de "
     "un proceso ya existente; el hijo es el procedimiento ENTERO de descubrimiento de "
     "necesidades del paso 3 de un framework DISTINTO (Diseno para la Calidad, por su propio "
     "resumen). MISMA FUENTE (Juran's Quality Handbook) pero procesos distintos del libro. Y el "
     "hijo YA TIENE su madre real y establecida en la propia cadena de ese framework "
     "(identificar_clientes_externos_e_internos -> descubrir_necesidades_del_cliente, ya "
     "enlazada en las dos vistas): coincidencia lexica sobre 'necesidades del cliente', no "
     "jerarquia. No se enlaza."),
    ("el_riesgo_nunca_se_acaba_se_administra", "cuando_el_riesgo_se_vuelve_realidad",
     "el paso 2 senalado manda convertir la gestion de riesgo en un HABITO PERMANENTE; el hijo "
     "es el procedimiento de RESPUESTA A CRISIS cuando un riesgo ya se materializo, tema "
     "distinto (prevencion continua contra reaccion puntual). La madre es un nodo ancla de tono "
     "(sintesis de DeMarco y Lister) con 4 pasos filosoficos breves, no un procedimiento del que "
     "el hijo sea una etapa. No se enlaza."),
    ("abolir_inspeccion_masiva", "eliminacion_inspeccion_masiva_por_control_estadistico",
     "VEREDICTO DEL CRIBADO: puesto 2560, clase D: 'la estrategia ancha contra el mecanismo "
     "estrecho, MISMA FUENTE, Deming, y SIN ARISTA [...] Sano: cada uno trae lo que al otro le "
     "falta, no es un subconjunto.' Mandato expreso del archivo. No se enlaza."),
    ("recursos_apoyo_gubernamental_exportacion", "trabajo_con_bancos_comerciales",
     "el paso 3 senalado es sobre financiamiento GUBERNAMENTAL (SBA, Ex-Im Bank); el hijo es "
     "sobre relacion con BANCOS COMERCIALES privados, institucion de naturaleza distinta pese al "
     "tema comun de 'financiamiento de exportacion'. Ningun paso de la madre manda trabajar con "
     "banca comercial. No se enlaza."),
    ("definiciones_operacionales_de_calidad", "optimizacion_caracteristicas_diseno",
     "el paso 1 senalado es sobre IDENTIFICAR caracteristicas criticas de calidad segun el "
     "cliente; el hijo es sobre OPTIMIZAR un diseno YA COMPLETO mediante revision y negociacion "
     "estructurada, etapa posterior y accion distinta (optimizar/negociar, no identificar). "
     "Fuentes distintas (Deming contra Juran). No se enlaza."),
    ("qfd_matriz", "identificar_clientes_externos_e_internos",
     "DIRECCION EQUIVOCADA. El paso 2 de qfd_matriz solo NOMBRA la accion "
     "('identifica tus clientes... y descubre sus necesidades') que YA ejecutan otros nodos "
     "establecidos en el orden CONTRARIO: identificar_clientes_externos_e_internos ya enlaza a "
     "descubrir_necesidades_del_cliente, que ya enlaza a qfd_matriz (la propia madre de este "
     "candidato). Escribir qfd_matriz -> identificar_clientes_externos_e_internos crearia un "
     "ciclo contra una cadena ya establecida en sentido opuesto. No se enlaza."),
    ("analisis_variacion_desempeno_servicio", "pre_control_estadistico",
     "el paso 4 senalado manda REVISAR EL DISENO O LA ESPECIFICACION cuando el sistema esta en "
     "control pero fuera de especificacion; el hijo es una tecnica de monitoreo estadistico "
     "DISTINTA (zonas de PRE-Control, muestras de tres piezas), no la accion de revision que el "
     "paso manda. Fuentes distintas (Deming contra Juran). No se enlaza."),
]

# El DISCUTIBLE, leido y NO escrito por cautela (paso-redirect, mismo dia que D2).
DISCUTIBLE_NO_ESCRITO = (
    "descubrir_necesidades_del_cliente", "traduccion_necesidades_cliente",
    "el paso senalado por el calibrador (paso 2, 'recopilar la lista de necesidades') NO es el "
    "que calza: el que calza es el paso 6 de la MISMA madre ('traducir las necesidades "
    "priorizadas al lenguaje tecnico de la organizacion'), que coincide casi palabra por palabra "
    "con el proposito entero del hijo. PERO es un redirect de paso, la MISMA especie que "
    "produjo D2 en esta misma vuelta (producto_mercado_fit_motores -> afinar_motor_crecimiento, "
    "revertido en la TAREA 3), y la familia YA TIENE un camino establecido mas especifico para "
    "esta misma transicion: identificar_clientes_externos_e_internos -> customer_needs_spreadsheet "
    "-> traduccion_necesidades_cliente (las dos aristas ya en el grafo). No es la CADENA PROPIA "
    "de esta madre (customer_needs_spreadsheet no es paso de descubrir_necesidades_del_cliente), "
    "asi que la vara nueva de la cadena no lo descarta por si sola; pero anadir una segunda via "
    "directa a la misma transicion, justo tras revertir un redirect de paso por el mismo motivo, "
    "pide mas ojos que los mios. NO SE ESCRIBE: queda discutible para la relectura del auditor."
)

# Los SIETE ya decididos en tramos anteriores, citados sin re-derivar.
PARES_YA_DECIDIDOS_ANTERIORES = [
    ("clasificacion_tipos_activos", "tipos_de_pasivos"),
    ("proceso_llamada_inicial_venta", "proceso_venta_franquicias"),
    ("equipo_customer_development", "customer_development_team"),
    ("preparacion_preguntas_problema_precall", "preguntas_situacion"),
    ("timing_solicitud_referidos", "fase_adopt_ciclo_cliente"),
    ("requisitos_numericos_calidad_lotes", "critica_acceptable_quality_level"),
]
# El septimo es la reversion de la TAREA 3.1 de la vuelta 79:
# extraer_priorizar_hipotesis -> value_proposition_startup.
# Los ONCE del tramo 5 de la vuelta 79 (PARES_DESCARTADOS_NUEVOS de vuelta79_tramo5_escribir.py).
PARES_TRAMO5_NO_ESCRITOS = [
    ("hipotesis_relacion_clientes_web", "mvp_alta_fidelidad"),
    ("valor_intangible_sostenibilidad", "compromiso_cliente_sostenibilidad"),
    ("analisis_valor", "customer_needs_spreadsheet"),
    ("posicionamiento_vs_competidores", "analisis_competencia_franquicias"),
    ("organizacion_interna_exportacion", "estructura_plan_exportacion"),
    ("errores_comunes_fundraising", "confidencialidad_nda_adquisicion"),
    ("mvp_catalogo_tecnicas", "mvp_tipo_video"),
    ("reporte_estado_miembro_equipo", "variance_analysis"),
    ("evaluacion_actitudes_empleados", "identificar_oportunidades_sostenibilidad"),
    ("pre_control_estadistico", "limites_de_especificacion_vs_limites_de_control"),
    ("posicionamiento_por_tipo_de_mercado", "resegmentacion_mercado_nicho_bajo_costo"),
]
# Las DOS de esta misma vuelta, revertidas en la TAREA 3 (D2 y D3).
PARES_REVERTIDOS_TAREA3 = [
    ("producto_mercado_fit_motores", "afinar_motor_crecimiento"),
    ("terminologia_clave_breakthrough", "analisis_sintomas"),
]


def cargar(node_id):
    p = NODOS / f"{node_id}.json"
    with open(p, encoding="utf-8") as f:
        return json.load(f), p


def main():
    tocados = []
    ya_estaban = []
    escalera_rota = []

    for madre_id, hijo_id, _razon in PARES_SANOS:
        madre, ruta_m = cargar(madre_id)
        hijo, ruta_h = cargar(hijo_id)

        if hijo_id in (madre.get("nodos_siguientes") or []):
            ya_estaban.append((madre_id, hijo_id))
            continue
        if hijo_id in (madre.get("nodos_previos") or []):
            escalera_rota.append((madre_id, hijo_id, "hijo ya en nodos_previos de la madre"))
            continue
        if madre_id in (hijo.get("nodos_siguientes") or []):
            escalera_rota.append((madre_id, hijo_id, "madre ya en nodos_siguientes del hijo (invertida)"))
            continue

        madre.setdefault("nodos_siguientes", [])
        if hijo_id not in madre["nodos_siguientes"]:
            madre["nodos_siguientes"].append(hijo_id)
        hijo.setdefault("nodos_previos", [])
        if madre_id not in hijo["nodos_previos"]:
            hijo["nodos_previos"].append(madre_id)

        with open(ruta_m, "w", encoding="utf-8") as f:
            json.dump(madre, f, ensure_ascii=False, indent=2)
            f.write("\n")
        with open(ruta_h, "w", encoding="utf-8") as f:
            json.dump(hijo, f, ensure_ascii=False, indent=2)
            f.write("\n")
        tocados.append((madre_id, hijo_id))

    print(f"ARISTAS ESCRITAS (nodos_siguientes Y nodos_previos): {len(tocados)}")
    for m, h in tocados:
        print(f"  {m} -> {h}")
    print(f"YA ESTABAN (no se toco nada): {len(ya_estaban)}")
    for m, h in ya_estaban:
        print(f"  {m} -> {h}")
    print(f"ESCALERA ROTA (no se escribio, ya habia arista inversa): {len(escalera_rota)}")
    for m, h, motivo in escalera_rota:
        print(f"  {m} -> {h}: {motivo}")

    print()
    print(f"NO ESCRITOS ESTA LECTURA FRESCA, con razon: {len(PARES_DESCARTADOS_NUEVOS)}")
    for m, h, _r in PARES_DESCARTADOS_NUEVOS:
        print(f"  {m} -> {h}")
    print(f"DISCUTIBLE, NO ESCRITO POR CAUTELA (redirect de paso, mismo dia que D2): 1")
    print(f"  {DISCUTIBLE_NO_ESCRITO[0]} -> {DISCUTIBLE_NO_ESCRITO[1]}")
    total_decididos_anteriores = len(PARES_YA_DECIDIDOS_ANTERIORES) + 1 + len(PARES_TRAMO5_NO_ESCRITOS) + len(PARES_REVERTIDOS_TAREA3)
    print(f"YA DECIDIDOS EN VUELTAS ANTERIORES (citados, no re-derivados): {total_decididos_anteriores}")

    total_30 = (len(PARES_SANOS) + len(PARES_DESCARTADOS_NUEVOS) + 1
                + total_decididos_anteriores)
    print()
    print(f"TOTAL DE LA CABEZA LEIDA: {total_30} (se esperan 30)")


if __name__ == "__main__":
    main()
