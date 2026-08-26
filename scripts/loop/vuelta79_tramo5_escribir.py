# -*- coding: utf-8 -*-
"""VUELTA 79, TAREA 5: OP-E-01, TRAMO 5. Escribe en dataset/nodos/<madre>.json
las aristas nuevas confirmadas por lectura par a par (9.6.2 contenido, con
9.6.1 y escalera chequeados), leidas contra la cabeza de la bolsa recalibrada
FRESCA de esta vuelta, filtrada por P.9.1 ENSANCHADO CON LA VARA DE LOS A MAS
LA GUARDA DEL PAR NO DIRIGIDO (docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V79.jsonl,
docs/loop/SALIDA_V79_TRAMO5_FILTRO_P91_GUARDA.txt).

CRITERIO ADJUDICADO (sin cambio sobre tramos anteriores, encargo TAREA 5):
veredicto del cribado PRIMERO; el sufijo numerico y el racimo solo opinan
cuando NO hay veredicto; cuando el paso que el calibrador senala no es el que
calza, manda la lectura (acta 77, D1); y cuando el paso solo NOMBRA un objeto
en vez de mandar una accion sobre el, no hay jerarquia (acta 78, D3, banco
9.6.2).

De los 30 primeros candidatos (UNIDADES de lectura, guarda del par no
dirigido aplicada; 0 parejas esta vuelta), SIETE (indices 0 a 6) YA ESTABAN
DECIDIDOS por vueltas anteriores de esta misma campana (seis del tramo 4 de
la vuelta 78, PARES_DESCARTADOS; uno por la reversion de la TAREA 3.1 de esta
misma vuelta) y se citan sin re-derivar: siguen NO ENLAZADOS, misma razon ya
escrita. Los 23 restantes (indices 7 a 29) son lectura fresca de esta vuelta.

De esos 23: TRES tenian veredicto propio del cribado (puesto 2324 clase D,
"ARISTA QUE FALTA" = SI enlaza; puesto 2097 clase D, "sin arista entre
ellos" = NO enlaza; puesto 384 clase D, "no hay arista entre estos dos,
[...] la madre real es producto_minimo_viable" = NO enlaza). Los otros 20 se
deciden por 9.6.2 (contenido).

RESULTADO: DOCE se enlazan (de los 23 nuevos), ONCE no se enlazan (de los 23
nuevos), y los SIETE ya decididos se quedan como estaban. Total ESCRITAS: 12.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

# Los 12 pares SANOS, con su razon (indice del dossier entre corchetes).
PARES_SANOS = [
    ("uso_inadecuado_computadoras", "causas_comunes_vs_especiales",
     "[7] paso 3 es la linea (aprender a distinguir causa comun de causa especial); el hijo ES ese "
     "procedimiento de deteccion (Deming, Out of the Crisis) con 15 pasos propios. DISCUTIBLE: la "
     "madre YA tiene otro hijo del tramo 4 sobre el mismo concepto y el mismo paso 3 "
     "(causas_especiales_y_comunes_variacion, via Juran), y hay un TERCER nodo casi identico en el "
     "grafo (causas_comunes_causas_especiales, ya senalado por Gate 0 como similitud de titulo >=95 "
     "contra este mismo hijo). Se escribe porque el hijo pasa la prueba de 9.6.2 sola (cabe entero en "
     "el paso, lo ejecuta, la madre conserva materia propia en los pasos 1, 2 y 4), pero la posible "
     "sobre-cobertura del mismo paso con un segundo hijo casi-gemelo merece relectura."),
    ("producto_mercado_fit_motores", "afinar_motor_crecimiento",
     "el calibrador senala el paso 1 (definir la metrica), pero el que calza es el paso 4 (usar la "
     "contabilidad de la innovacion para decidir si hay encaje o hace falta pivotar): el hijo ES el "
     "segundo paso de esa misma contabilidad de la innovacion (elegir motor, formular hipotesis, "
     "experimentar, medir, descartar), nombrado por su propio resumen. DISCUTIBLE: el hijo cubre solo "
     "UNO de los pasos del framework de tres que el paso 4 invoca en bloque (establecer linea base, "
     "afinar motor, pivotar o perseverar); se escribe por el redireccionamiento de paso adjudicado en "
     "acta 77 D1, pero la cobertura parcial vale relectura."),
    ("planificacion_inicial_calidad", "identificar_caracteristicas_metas_proceso",
     "paso 2 es la linea (identificar caracteristicas clave del producto Y DEL PROCESO, KPCs); el "
     "hijo ES el procedimiento de identificar/clasificar caracteristicas de proceso, con 5 pasos "
     "propios. sin veredicto de cribado"),
    ("establecimiento_capacidad_proceso", "pruebas_destructivas",
     "paso 5 es la linea (confirmar control estadistico mediante cartas de control); el hijo "
     "especializa esa confirmacion para el caso donde la prueba DESTRUYE la muestra (no hay otra via "
     "que el control estadistico del proceso), con procedimiento propio de 4 pasos. sin veredicto de "
     "cribado"),
    ("certificacion_de_proveedores", "indice_cpk",
     "paso 3 es la linea (usar indices de capacidad de proceso como parte de la certificacion); el "
     "hijo ES uno de esos indices (Cpk) con procedimiento propio de 7 pasos, y su propio resumen se "
     "declara critico para certificacion de proveedores. sin veredicto de cribado"),
    ("mitigacion_efecto_latigo", "precios_todos_los_dias_bajos",
     "paso 4 es la linea literal (implementar precios estables 'everyday low price' para evitar "
     "compras anticipadas); el hijo ES esa politica de precios con procedimiento propio de 3 pasos. "
     "sin veredicto de cribado"),
    ("herramientas_analisis_causa_raiz", "estratificacion_datos",
     "paso 5 nombra la estratificacion explicitamente; el hijo ES esa tecnica con procedimiento "
     "propio de 7 pasos. sin veredicto de cribado"),
    ("identificacion_evaluacion_peligros", "investigacion_incidentes",
     "VEREDICTO DEL CRIBADO: puesto 2324, clase D: 'la linea contra su procedimiento, MISMA FUENTE, "
     "OSHA3885... Por la vara, CONTINUA. ARISTA QUE FALTA.' El paso 4 de la madre es la linea "
     "(investigar incidentes y casi accidentes); el hijo trae el procedimiento completo. Silueta "
     "medida por el propio cribado (banco 9.6.1): la madre ya tiene tres hijos leidos, uno de tres es "
     "mitad o menos, no acusa ni exculpa."),
    ("establecimiento_capacidad_proceso", "control_estadistico_de_procesos",
     "paso 5, la misma linea que el par anterior de esta madre (confirmar control estadistico "
     "mediante cartas de control); el hijo ES el procedimiento GENERAL de control estadistico de "
     "procesos (10 pasos propios), distinto del caso especializado de pruebas_destructivas: dos hijos "
     "legitimos para el mismo paso, uno el metodo general y otro su aplicacion a un caso limite. sin "
     "veredicto de cribado"),
    ("testear_circulo_cuadrado_rectangulo", "validar_modelo_negocio_hechos",
     "paso 3 es la linea (validar que el modelo de negocio completo, el 'rectangulo', es viable); el "
     "hijo ES el procedimiento de convertir las hipotesis del business model canvas en hechos "
     "comprobados, con checklist y pruebas pass/fail propias. sin veredicto de cribado"),
    ("terminologia_clave_breakthrough", "analisis_sintomas",
     "paso 2 es la linea (diferenciar sintomas de causas); el hijo ES la disciplina de caracterizar "
     "sintomas a fondo (frecuencia, severidad, tipo, ubicacion) antes de inferir causas, que es la "
     "aplicacion practica de mantenerlos separados. DISCUTIBLE: la accion literal del paso es "
     "'diferenciar', y el hijo no compara sintoma contra causa paso a paso, solo profundiza en el "
     "sintoma; direccion floja, vale relectura, mismo patron que los discutibles de iso9001/iso9004 y "
     "comercio-internacional de la vuelta 78."),
    ("mapa_de_canal_de_ventas", "validar_canal_distribucion",
     "paso 1 es la linea literal (enfocate en validar un solo canal de distribucion); el hijo ES el "
     "procedimiento de validacion (evidencia de demanda, presentacion de canal, reunion con "
     "distribuidores, orden inicial), con 6 pasos propios. sin veredicto de cribado"),
]

# Los 11 pares leidos y NO escritos de esta lectura fresca (indices 8, 10, 17,
# 19, 20, 21, 23, 24, 27, 28, 29), con su razon.
PARES_DESCARTADOS_NUEVOS = [
    ("hipotesis_relacion_clientes_web", "mvp_alta_fidelidad",
     "el paso 4 senalado nombra explicitamente un MVP DE BAJA FIDELIDAD ('probar tacticas a pequena "
     "escala con un MVP de baja fidelidad'); el hijo propuesto es el MVP DE ALTA FIDELIDAD, la etapa "
     "siguiente. Mismatch de fidelidad: ningun paso de la madre nombra o manda la version de alta "
     "fidelidad. No se enlaza."),
    ("valor_intangible_sostenibilidad", "compromiso_cliente_sostenibilidad",
     "el paso 1 senalado manda incorporar metricas de sostenibilidad al seguimiento general del "
     "negocio (satisfaccion de cliente, compromiso de equipo, impacto ambiental); el hijo es una "
     "tactica especifica de campanas digitales de compromiso ambiental con clientes, no una metrica "
     "de seguimiento. Tematicamente relacionado, pero ningun paso de la madre manda esa tactica "
     "concreta. No se enlaza."),
    ("analisis_valor", "customer_needs_spreadsheet",
     "el paso 1 senalado exige una hoja de calculo que relacione COSTOS con necesidades del cliente; "
     "el hijo es una matriz de clientes x necesidades que en NINGUNO de sus pasos toca costos: es una "
     "herramienta distinta (insumo de Quality by Design), no la hoja de costo-necesidad del paso 1. "
     "No se enlaza."),
    ("posicionamiento_vs_competidores", "analisis_competencia_franquicias",
     "VEREDICTO DEL CRIBADO: puesto 2097, clase D, sobre el MISMO PAR en la direccion inversa "
     "(analisis_competencia_franquicias -> posicionamiento_vs_competidores): 'sin arista entre "
     "ellos... CONTINUA en los dos sentidos, banco 9.22: uno junta la municion, el otro dispara'. "
     "Son companeros de secuencia (investigacion vs conversacion), no madre e hijo, y el archivo lo "
     "dice explicito para el par sin importar la direccion. No se enlaza."),
    ("organizacion_interna_exportacion", "estructura_plan_exportacion",
     "el paso 3 senalado ('definir la estructura de REPORTE del area de exportacion') es sobre "
     "jerarquia organizacional (quien reporta a quien); el hijo es la estructura de un DOCUMENTO de "
     "plan de exportacion (tabla de contenido, secciones). Coincidencia lexica en 'estructura', "
     "significados distintos. No se enlaza."),
    ("errores_comunes_fundraising", "confidencialidad_nda_adquisicion",
     "el paso 2 senalado manda NUNCA pedir NDA a un VC en una ronda de inversion; el hijo dice que en "
     "M&A el NDA es PRACTICAMENTE OBLIGATORIO. Son reglas para escenarios distintos (fundraising vs "
     "adquisicion) con recomendaciones opuestas sobre el mismo instrumento: un contraste, no una "
     "jerarquia 9.6.2 (el hijo no ejecuta el paso 2, lo contradice en su propio contexto). No se "
     "enlaza."),
    ("mvp_catalogo_tecnicas", "mvp_tipo_video",
     "VEREDICTO DEL CRIBADO: puesto 384, clase D: 'Ninguno repite al otro... no hay arista entre "
     "estos dos, pero el video SI tiene madre, y es producto_minimo_viable.' Mandato expreso del "
     "archivo. No se enlaza."),
    ("reporte_estado_miembro_equipo", "variance_analysis",
     "el hijo NO cabe entero dentro del paso 3 senalado (identificar causas raiz): sus cuatro pasos "
     "abarcan tambien la comparacion planificado/real (paso 2 de la madre) y la respuesta correctiva "
     "(paso 4 de la madre) a la vez. No hay UN paso que lo contenga entero; posible relacion mas "
     "ancha o invertida (variance_analysis como tecnica formal detras del reporte informal), no "
     "jerarquia limpia de un solo paso. No se enlaza."),
    ("evaluacion_actitudes_empleados", "identificar_oportunidades_sostenibilidad",
     "el paso 2 senalado es sobre reacciones INTERNAS de empleados a palabras como 'verde' o "
     "'sostenibilidad' (encuesta de clima); el hijo es analisis ESTRATEGICO de mercado (por que el "
     "cliente externo quiere una oferta mas verde, FODA por linea de producto, comparacion "
     "competitiva). Mismatch de objeto (empleados contra mercado). No se enlaza."),
    ("pre_control_estadistico", "limites_de_especificacion_vs_limites_de_control",
     "el paso 1 senalado manda centrar el proceso ENTRE LOS LIMITES DE ESPECIFICACION; el hijo es una "
     "advertencia conceptual de Deming contra ajustar el proceso usando limites de especificacion en "
     "vez de limites de control (el propio metodo que Pre-Control usa). Es un contraste critico, no "
     "un procedimiento que ejecute el paso 1: el hijo argumenta contra el tipo de ajuste que "
     "Pre-Control practica. No se enlaza."),
    ("posicionamiento_por_tipo_de_mercado", "resegmentacion_mercado_nicho_bajo_costo",
     "el paso 5 senalado manda COMUNICAR comprension de un nicho o ventaja de bajo costo (la accion "
     "es comunicar/mensaje); el hijo es el trabajo analitico PREVIO a esa comunicacion (identificar "
     "el segmento, evaluar disposicion a pagar, definir caracteristicas, mapear mercado, probar costo "
     "de cambio): ninguno de sus pasos comunica nada, todos preceden la comunicacion. Misma especie "
     "que extraer_priorizar_hipotesis (TAREA 3.1 de esta vuelta): el paso nombra el resultado, el "
     "hijo hace el trabajo previo, no la accion mandada. No se enlaza."),
]

# Los SEIS ya decididos en el tramo 4 de la vuelta 78 (PARES_DESCARTADOS de
# vuelta78_tramo4_escribir.py), citados sin re-derivar.
PARES_YA_DECIDIDOS_TRAMO4 = [
    ("clasificacion_tipos_activos", "tipos_de_pasivos"),
    ("proceso_llamada_inicial_venta", "proceso_venta_franquicias"),
    ("equipo_customer_development", "customer_development_team"),
    ("preparacion_preguntas_problema_precall", "preguntas_situacion"),
    ("timing_solicitud_referidos", "fase_adopt_ciclo_cliente"),
    ("requisitos_numericos_calidad_lotes", "critica_acceptable_quality_level"),
]
# El septimo ya decidido es la reversion de la TAREA 3.1 de esta misma vuelta:
# extraer_priorizar_hipotesis -> value_proposition_startup (NO se enlaza).


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
    print(f"YA DECIDIDOS EN VUELTAS ANTERIORES (citados, no re-derivados): {len(PARES_YA_DECIDIDOS_TRAMO4) + 1}")
    for m, h in PARES_YA_DECIDIDOS_TRAMO4:
        print(f"  {m} -> {h}")
    print("  extraer_priorizar_hipotesis -> value_proposition_startup (TAREA 3.1 de esta vuelta)")

    total_30 = len(PARES_SANOS) + len(PARES_DESCARTADOS_NUEVOS) + len(PARES_YA_DECIDIDOS_TRAMO4) + 1
    print()
    print(f"TOTAL DE LA CABEZA LEIDA: {total_30} (se esperan 30)")


if __name__ == "__main__":
    main()
