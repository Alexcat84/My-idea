# -*- coding: utf-8 -*-
"""Script de un solo uso, TAREA 4.3 vuelta 104: aplica correccion_v104 a los
siete pares NO_OBJETO de la TAREA 4.2 (6, 8, 24, 25, 52, 62, 80), tras la
lectura a ciegas propia registrada en
docs/loop/SALIDA_V104_TAREA4_3_CIEGA_BLIND.txt / ..._REVEAL.txt."""
import json
import io

CORRECCIONES = {
    6: {
        "valor_anterior": "issue_spotting_ambiental -> triple_bottom_line_2",
        "cita_corregida": (
            "banco 9.6.2 (primer brazo: el hijo no cabe entero en el paso 2, que es una DECISION de "
            "alcance, no un procedimiento de deteccion social; 'triple bottom line' es etiqueta "
            "parentetica de una de las dos alternativas de esa decision) y banco 9.6.3 (procedimiento "
            "en los dos lados: el par es SANO), no la mencion literal de 'triple bottom line'"
        ),
        "razon": (
            "CORRECCION DECLARADA (vuelta 104, TAREA 4.3, barrido dirigido por la especie del 28, "
            "lectura a ciegas propia). El texto viejo de razon y direccion_leida NO SE BORRA. Leidos "
            "hoy enteros dataset/nodos/issue_spotting_ambiental.json y "
            "dataset/nodos/triple_bottom_line_2.json y 9.6.2/9.6.3 del banco enteros: el paso 2 de la "
            "madre ('Decide si tu enfoque sera solo ambiental o si vas a incluir tambien lo social y "
            "economico') es una DECISION binaria de alcance; su objeto es la eleccion misma, no un "
            "procedimiento de deteccion social. Los tres pasos del hijo (identificar issues sociales, "
            "evaluar practicas laborales/diversidad/derechos humanos, integrar metricas sociales) no "
            "aparecen en ningun paso de la madre: los pasos 3 y 4 de la madre son especificamente "
            "AMBIENTALES (inside-out/outside-in de recursos naturales y toxicos), nunca sociales. La "
            "senal de los entregables no salva la direccion: el entregable de la madre pide una lista "
            "'segun si el impacto viene de adentro hacia afuera o de afuera hacia adentro' (ejes "
            "ambientales), no menciona practicas laborales ni cadena de valor. El 9.6.3 muestra "
            "PROCEDIMIENTO EN LOS DOS LADOS: la madre conserva el suyo (revisar los 12 problemas, "
            "inside-out, outside-in, anotar y priorizar) y el hijo el suyo (identificar issues "
            "sociales, evaluar practicas, integrar metricas), sin que ninguno toque al otro: SANO. SE "
            "MUEVE: el par 6 pasa de DIRECCION AFIRMADA a NO RESUELTA. Clase D no cambia."
        ),
    },
    8: {
        "valor_anterior": "analisis_de_sistemas_de_medicion_msa -> capacidad_de_proceso_2",
        "cita_corregida": (
            "banco 9.6.2 (primer brazo: 'capacidad de proceso' NO aparece en el paso 3 en ninguna "
            "forma, ni como objeto ni como ejemplo/condicion; el paso verifica el control estadistico "
            "del SISTEMA DE MEDICION, un topico distinto de la capacidad del PROCESO DE PRODUCCION) y "
            "banco 9.6.3 (procedimiento en los dos lados: SANO), no el vocabulario compartido 'control "
            "estadistico'/'carta de control'"
        ),
        "razon": (
            "CORRECCION DECLARADA (vuelta 104, TAREA 4.3, barrido dirigido por la especie del 28, "
            "lectura a ciegas propia). El texto viejo NO SE BORRA. Leidos hoy enteros "
            "dataset/nodos/analisis_de_sistemas_de_medicion_msa.json y "
            "dataset/nodos/capacidad_de_proceso_2.json y 9.6.2/9.6.3 enteros: la madre es un estudio "
            "MSA/Gauge R&R (validar que el INSTRUMENTO DE MEDICION es confiable); el paso 3 verifica "
            "que el PROCESO DE MEDICION este en control ANTES de confiar en el Gauge R&R, un paso "
            "interno de esa validacion. El hijo es un estudio de CAPACIDAD DEL PROCESO DE PRODUCCION "
            "(seleccionar unidad, recolectar ~3 meses de datos, construir cartas, decidir limites, "
            "intervenir sobre el sistema): un topico distinto (el proceso productivo, no el sistema de "
            "medicion) que ningun paso de la madre desarrolla. La senal de los entregables lo confirma: "
            "la madre entrega un 'informe de estudio MSA/Gauge R&R con repetibilidad, reproducibilidad "
            "y aceptabilidad del sistema de medicion'; el hijo entrega una 'carta de control con "
            "limites de capacidad del proceso', un producto distinto que la madre nunca pide. El 9.6.3 "
            "muestra PROCEDIMIENTO EN LOS DOS LADOS: la madre conserva el suyo entero (metodo de "
            "prueba, fuentes de variabilidad, Gauge R&R, 5,15 sigma, calibracion) y el hijo el suyo "
            "(seleccion de unidad, recoleccion, cartas, limites, intervencion): SANO. SE MUEVE: el par "
            "8 pasa de DIRECCION AFIRMADA a NO RESUELTA. Clase D no cambia."
        ),
    },
    24: {
        "valor_anterior": "preparacion_preguntas_problema_precall -> preguntas_situacion",
        "cita_corregida": (
            "banco 9.6.2 (primer brazo: el hijo vive DENTRO de una subordinada de finalidad 'para "
            "minimizar X', no como objeto de 'usar'; el objeto real de 'usar' son las preguntas de "
            "PROBLEMA, tema propio de la madre) y banco 9.6.3 (procedimiento en los dos lados: SANO), "
            "no la palabra compartida 'preguntas de situacion'"
        ),
        "razon": (
            "CORRECCION DECLARADA (vuelta 104, TAREA 4.3, barrido dirigido por la especie del 28, "
            "lectura a ciegas propia). El texto viejo NO SE BORRA. Leidos hoy enteros "
            "dataset/nodos/preparacion_preguntas_problema_precall.json y "
            "dataset/nodos/preguntas_situacion.json y 9.6.2/9.6.3 enteros: el paso 4 de la madre ('Usar "
            "estas preguntas para minimizar preguntas de situacion irrelevantes') tiene como OBJETO "
            "'estas preguntas' (las preguntas de PROBLEMA, tema entero de la madre); 'preguntas de "
            "situacion' aparece solo dentro de una subordinada de FINALIDAD ('para minimizar X'), no "
            "como lo que el paso manda construir. Los tres pasos del hijo (investigar al cliente antes, "
            "limitar preguntas de situacion a lo necesario, usarlas como apertura breve) no aparecen en "
            "ningun otro paso de la madre, que trata solo preguntas de problema (listar problemas, "
            "redactar preguntas de problema, revisar antes de la llamada, identificar problemas "
            "tipicos, formular preguntas de insatisfaccion, escuchar). La senal de los entregables lo "
            "confirma: el entregable de la madre es una 'lista de problemas con preguntas de PROBLEMA "
            "asociadas'; el del hijo es una 'lista corta y priorizada de preguntas de SITUACION', "
            "producto distinto. El 9.6.3 muestra PROCEDIMIENTO EN LOS DOS LADOS: SANO. SE MUEVE: el "
            "par 24 pasa de DIRECCION AFIRMADA a NO RESUELTA. Clase D no cambia."
        ),
    },
    25: {
        "valor_anterior": "histograma_calidad -> capacidad_del_proceso",
        "cita_corregida": (
            "banco 9.6.2 (primer brazo: 'capacidad del proceso' vive DENTRO de una subordinada de "
            "finalidad 'para determinar X', no como objeto de 'evaluar'; ademas el hijo usa un metodo "
            "DISTINTO al de la madre, formulas de control estadistico contra lectura visual de "
            "histograma) y banco 9.6.3 (procedimiento en los dos lados: SANO), no la meta compartida "
            "'capacidad del proceso'"
        ),
        "razon": (
            "CORRECCION DECLARADA (vuelta 104, TAREA 4.3, barrido dirigido por la especie del 28, "
            "lectura a ciegas propia). El texto viejo NO SE BORRA (incluida la nota vieja 'mismo hijo "
            "que el par 18 con otra madre', que ya admitia que 'ninguna lo desarrolla', sintoma que "
            "esta correccion resuelve). Leidos hoy enteros dataset/nodos/histograma_calidad.json y "
            "dataset/nodos/capacidad_del_proceso.json y 9.6.2/9.6.3 enteros: el paso 4 de la madre "
            "('Evaluar el centrado, ancho y forma del histograma para determinar capacidad del "
            "proceso') tiene como OBJETO 'el centrado, ancho y forma del histograma'; 'capacidad del "
            "proceso' aparece solo dentro de una subordinada de FINALIDAD. Ademas el METODO es "
            "distinto: la madre evalua capacidad LEYENDO LA FORMA DE UN HISTOGRAMA (visual/grafico); "
            "el hijo la calcula con formulas de control estadistico (constantes d2, A2) sobre un "
            "proceso YA verificado en control via graficos de corrida o X-barra/R, un metodo "
            "cuantitativo distinto que ningun paso de la madre desarrolla. La senal de los entregables "
            "lo confirma: la madre entrega 'histograma graficado ... y analisis de capacidad DEL "
            "PROCESO', autosuficiente por su propio metodo; el hijo entrega un 'informe de capacidad "
            "con limites naturales calculados a partir de datos en control estadistico', metodo "
            "paralelo, no un desarrollo del histograma. El 9.6.3 muestra PROCEDIMIENTO EN LOS DOS "
            "LADOS: la madre conserva construir la distribucion, graficar barras y agregar limites de "
            "especificacion; el hijo conserva verificar control, calcular media/rango, aplicar formulas "
            "y comunicar a diseno: SANO. SE MUEVE: el par 25 pasa de DIRECCION AFIRMADA a NO RESUELTA. "
            "Clase D no cambia. NOTA: el par 18 (dmaic_fase_measure -> capacidad_del_proceso) no se "
            "toca aqui, ya fue evaluado por separado en la TAREA 4.2 de esta misma vuelta y dio OBJETO "
            "(objeto directo del segundo verbo coordinado 'medir su capacidad', sin subordinada)."
        ),
    },
    52: {
        "valor_anterior": "posicionamiento_por_tipo_de_mercado -> resegmentacion_mercado_nicho_bajo_costo",
        "cita_corregida": (
            "banco 9.6.2 (primer brazo: el paso 5 es CONDICIONAL explicito ('Si es re-segmentacion:'), "
            "una de cuatro ramas paralelas de un mismo paso-menu; el hijo excede ampliamente esa rama, "
            "seis pasos contra una linea) y banco 9.6.3 (procedimiento en los dos lados: SANO), no la "
            "palabra compartida 're-segmentacion'"
        ),
        "razon": (
            "CORRECCION DECLARADA (vuelta 104, TAREA 4.3, barrido dirigido por la especie del 28, "
            "lectura a ciegas propia). El texto viejo NO SE BORRA. Leidos hoy enteros "
            "dataset/nodos/posicionamiento_por_tipo_de_mercado.json y "
            "dataset/nodos/resegmentacion_mercado_nicho_bajo_costo.json y 9.6.2/9.6.3 enteros: el paso "
            "5 de la madre ('Si es re-segmentacion: comunicar comprension unica de un nicho o ventaja "
            "de bajo costo') es UNA RAMA CONDICIONAL EXPLICITA, una de cuatro alternativas paralelas "
            "(pasos 2 a 5, cada una 'Si es mercado X: ...') para distintos tipos de mercado; su "
            "imperativo real, dentro de esa rama, es 'comunicar', no ejecutar el metodo de "
            "re-segmentacion. Los seis pasos del hijo (identificar de que mercados vendrian los "
            "clientes desatendidos, evaluar disposicion a pagar, definir caracteristicas unicas, "
            "determinar que los haria cambiar de proveedor, dibujar mapa de mercado, probar "
            "cuantitativamente el costo de cambio) exceden ampliamente 'comunicar': son la metodologia "
            "ENTERA para llegar a esa comprension, que la madre no desarrolla en ningun paso. La senal "
            "de los entregables lo confirma: la madre entrega un 'posicionamiento ajustado y coherente "
            "con el tipo de mercado elegido', generico para los cuatro tipos; el hijo entrega 'un mapa "
            "de mercado y un brief de re-segmentacion con hipotesis validables', producto especifico "
            "que el paso 5 no menciona. El 9.6.3 muestra PROCEDIMIENTO EN LOS DOS LADOS: la madre "
            "conserva enteras las otras tres ramas (mercado existente, nuevo y clon) mas la "
            "identificacion del tipo; el hijo conserva su metodologia de seis pasos: SANO. SE MUEVE: "
            "el par 52 pasa de DIRECCION AFIRMADA a NO RESUELTA. Clase D no cambia."
        ),
    },
    62: {
        "valor_anterior": "preservar_efectivo_buscar_modelo -> validar_modelo_negocio_hechos",
        "cita_corregida": (
            "banco 9.6.2 (primer brazo: el hijo vive DENTRO de una subordinada TEMPORAL 'hasta + "
            "infinitivo', limite de cuando dejar de aplicar la orden principal 'no contrates', no su "
            "objeto; los entregables son productos distintos, plan de gasto contra canvas actualizado) "
            "y banco 9.6.3 (procedimiento en los dos lados: SANO), no la palabra compartida 'validar'"
        ),
        "razon": (
            "CORRECCION DECLARADA (vuelta 104, TAREA 4.3, barrido dirigido por la especie del 28, "
            "lectura a ciegas propia, misma especie exacta que el par 29 y el 28 de esta campana: "
            "subordinada temporal en vez de objeto). El texto viejo NO SE BORRA. Leidos hoy enteros "
            "dataset/nodos/preservar_efectivo_buscar_modelo.json y "
            "dataset/nodos/validar_modelo_negocio_hechos.json y 9.6.2/9.6.3 enteros: el paso 1 de la "
            "madre ('No contrates equipo de ventas ni marketing HASTA validar el modelo con hechos, no "
            "hipotesis') tiene como OBJETO del imperativo 'equipo de ventas ni marketing' (no "
            "contratarlo); 'validar el modelo con hechos' entra como SUBORDINADA TEMPORAL ('hasta + "
            "infinitivo'), el limite de cuando se levanta la prohibicion, no lo que el paso manda "
            "hacer. Los cinco pasos del hijo (reunir snapshots del canvas, revisar cada componente "
            "buscando respuestas facticas, usar el checklist, identificar pruebas pass/fail, "
            "determinar si se cumplen objetivos) no aparecen en ningun otro paso de la madre. La senal "
            "de los entregables lo confirma: la madre entrega un 'plan de gasto condicionado a hitos de "
            "validacion, CON UN CRITERIO EXPLICITO Y DOCUMENTADO' (que coincide con su propio paso 4, "
            "'documenta tu propio criterio explicito'); el hijo entrega un 'Business Model Canvas "
            "actualizado con cada componente respaldado por datos facticos', un artefacto distinto que "
            "la madre no pide. El 9.6.3 muestra PROCEDIMIENTO EN LOS DOS LADOS: la madre conserva "
            "buscar patrones repetibles, el test de escalabilidad con burn rate, su propio criterio "
            "documentado, invertir tras el fit, retrasar infraestructura, presupuesto por experimento y "
            "reserva de caja; el hijo conserva su metodologia de canvas: SANO. SE MUEVE: el par 62 pasa "
            "de DIRECCION AFIRMADA a NO RESUELTA. Clase D no cambia."
        ),
    },
    80: {
        "valor_anterior": "estudio_desempeno_run_charts_servicios -> causas_comunes_vs_especiales",
        "cita_corregida": (
            "banco 9.6.2 (primer brazo: el hijo vive DENTRO de una subordinada de finalidad 'para "
            "detectar X', y solo nombra 'especiales', nunca 'comunes'; exceso de genero de la misma "
            "especie que movio el par 31, con el MISMO hijo) y banco 9.6.3 (procedimiento en los dos "
            "lados: SANO), no el vocabulario compartido 'causas especiales'"
        ),
        "razon": (
            "CORRECCION DECLARADA (vuelta 104, TAREA 4.3, barrido dirigido por la especie del 28, "
            "lectura a ciegas propia). El texto viejo NO SE BORRA. Leidos hoy enteros "
            "dataset/nodos/estudio_desempeno_run_charts_servicios.json y "
            "dataset/nodos/causas_comunes_vs_especiales.json y 9.6.2/9.6.3 enteros: causas_comunes_vs_"
            "especiales es el MISMO hijo que el par 31 de la vuelta 103 (alli movido a NO RESUELTA "
            "contra otra madre, control_estadistico_del_proceso, por exceso de genero). Aqui el paso 3 "
            "de la madre ('Construir graficos de corrida o distribuciones para detectar causas "
            "especiales de variacion') tiene como OBJETO 'graficos de corrida o distribuciones'; "
            "'causas especiales' vive DENTRO de una subordinada de FINALIDAD ('para detectar X'), y "
            "SOLO nombra especiales, nunca comunes. Los quince pasos del hijo cubren AMBAS clases "
            "(comunes Y especiales) mas material de CULTURA (comunicar sin culpar, dar seguimiento a la "
            "moral del equipo, fomentar colaboracion entre turnos) que la madre no toca en ningun paso: "
            "sus cuatro pasos son identificar variables criticas del servicio, recolectar datos, "
            "construir graficos y dirigir recursos de capacitacion a areas fuera de control, nada de "
            "cultura ni de causas comunes. La senal de los entregables lo confirma: la madre entrega un "
            "'tablero de indicadores con graficos de corrida', un producto de monitoreo; el hijo entrega "
            "un 'grafico ... con los puntos clasificados como causa comun o especial y un plan de "
            "accion diferenciado para cada tipo', que cubre ambas clases y excede lo que la madre pide. "
            "El 9.6.3 muestra PROCEDIMIENTO EN LOS DOS LADOS: SANO. SE MUEVE: el par 80 pasa de "
            "DIRECCION AFIRMADA a NO RESUELTA. Clase D no cambia."
        ),
    },
}


def actualizar(ruta, puestos):
    with io.open(ruta, encoding="utf-8") as f:
        lineas = [l.rstrip("\n") for l in f if l.strip()]
    tocados = []
    for i, l in enumerate(lineas):
        d = json.loads(l)
        p = d.get("puesto_tramo")
        if p in puestos:
            assert "correccion_v104" not in d, p
            c = CORRECCIONES[p]
            d["correccion_v104"] = {
                "campo_corregido": "direccion_leida",
                "valor_anterior": c["valor_anterior"],
                "valor_nuevo": None,
                "cita_corregida": c["cita_corregida"],
                "razon": c["razon"],
            }
            lineas[i] = json.dumps(d, ensure_ascii=False)
            tocados.append(p)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        for l in lineas:
            f.write(l + "\n")
    return tocados


if __name__ == "__main__":
    t1_tocados = actualizar("docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl", {6, 8, 24, 25})
    t2_tocados = actualizar("docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl", {52, 62, 80})
    print("tramo1 tocados:", t1_tocados)
    print("tramo2 tocados:", t2_tocados)
