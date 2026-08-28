# -*- coding: utf-8 -*-
"""_v103_tarea2_correccion.py . Aplica correccion_v103 (campo direccion_leida
-> null) a los puestos 28 y 40 de docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl,
TAREA 2 de la vuelta 103 (relectura conjunta con el auditor, acta 102).
Script de un solo uso, no se re-corre."""
import json
import io

RUTA = "docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl"

with io.open(RUTA, encoding="utf-8") as f:
    lineas = [json.loads(l) for l in f if l.strip()]

razon_28 = (
    "CORRECCION DECLARADA (vuelta 103, TAREA 2, relectura conjunta con el auditor, "
    "acta de la vuelta 102, caso escrito sobre el par 28). El texto viejo de razon y "
    "direccion_leida NO SE BORRA. Leidos hoy dataset/nodos/timing_solicitud_referidos.json "
    "y dataset/nodos/fase_adopt_ciclo_cliente.json, y 9.6.2 y 9.6.3 del banco enteros: el "
    "test de reconocimiento del 9.6.2 falla en su PRIMER BRAZO. El paso 5 de la madre "
    "('Comunica el programa en momentos clave del ciclo de vida (ej: fase Adopt/Advocate)') "
    "tiene como OBJETO del imperativo 'el programa' (de referidos/testimonios); 'fase Adopt' "
    "entra solo como EJEMPLO PARENTETICO de CUANDO comunicarlo, no como lo que se comunica. "
    "Los cuatro pasos del hijo (definir metricas de adopcion, disenar interacciones para seis "
    "canales, implementar encuesta de exito, establecer ritual de hitos) no comunican ningun "
    "programa de referidos en ningun paso: el hijo NO cabe entero dentro del paso 5. La senal "
    "de los entregables (9.6.2) lo confirma: la madre entrega 'definicion documentada del "
    "punto de activacion optimo... con automatizacion configurada'; el hijo entrega 'mapa de "
    "touchpoints de la fase Adopt con al menos una accion por canal', que no es parte de "
    "aquello ni es 'el primero de dos productos' como en el ejemplar del 2.215. Y el 9.6.3 "
    "(que queda fuera del solape, en que lado) muestra PROCEDIMIENTO EN LOS DOS LADOS: la "
    "madre conserva entero el suyo (identificar punto de logro, configurar disparador "
    "automatizado, evitar solicitud inmediata, validar con datos) y el hijo el suyo (metricas "
    "de adopcion, seis canales, encuesta, ritual de hitos), sin que ninguno toque al otro: "
    "'procedimiento en los dos lados, el par es SANO'. SE SOSTIENE EL CASO DEL AUDITOR (acta "
    "102): el par 28 pasa de DIRECCION AFIRMADA a NO RESUELTA. Clase D no cambia (banco 9.6.1 "
    "rama contenido, tercera fila del 9.22: CONTINUA)."
)
cita_28 = (
    "banco 9.6.2 (primer brazo del test de reconocimiento: el hijo no cabe entero en el paso "
    "5, 'fase Adopt' es ejemplo de CUANDO, no objeto del imperativo) y banco 9.6.3 "
    "(procedimiento en los dos lados: el par es SANO), no la mencion literal de 'fase Adopt' "
    "dentro del paso 5"
)

razon_40 = (
    "CORRECCION DECLARADA (vuelta 103, TAREA 2, relectura conjunta con el auditor, acta de la "
    "vuelta 102, caso escrito sobre el par 40). El texto viejo de razon y direccion_leida NO "
    "SE BORRA, incluida su SALVEDAD ya declarada. Leidos hoy dataset/nodos/analisis_valor.json "
    "y dataset/nodos/customer_needs_spreadsheet.json, y 9.6.2 y 9.6.3 del banco enteros: el "
    "test de reconocimiento del 9.6.2 falla en su PRIMER BRAZO, por una via distinta a la del "
    "28. El paso 1 de la madre pide una hoja que cruce COSTOS con necesidades del cliente por "
    "prioridad; los seis pasos del hijo construyen una matriz que cruza CLIENTES (internos y "
    "externos, por prioridad) con necesidades, correlacionada por evidencia y fuerza de "
    "relacion: en ningun paso del hijo aparece un costo. La propia razon original ya concedia "
    "esto como SALVEDAD ('la matriz del hijo cruza clientes contra necesidades y la de la "
    "madre cruza costos contra necesidades, asi que el artefacto no es identico') pero "
    "sostuvo la direccion igual; releida contra el 9.6.2, esa salvedad ES la falla del primer "
    "brazo, no un detalle aparte: el hijo no cabe entero dentro de un paso cuyo eje es el "
    "costo. La senal de los entregables lo confirma: la madre entrega 'hoja de analisis de "
    "valor con costos por necesidad y decisiones de reasignacion de recursos'; el hijo entrega "
    "'matriz de clientes vs necesidades, correlacionadas con evidencia y priorizadas', un "
    "producto distinto que alimenta un tramo distinto del proceso (customer_needs_spreadsheet "
    "es fase_proyecto planificacion y sigue a traduccion_necesidades_cliente/"
    "product_design_spreadsheet; analisis_valor es fase_proyecto validacion y sigue a "
    "establecer_diseno_final_producto). El 9.6.3 muestra PROCEDIMIENTO EN LOS DOS LADOS: la "
    "madre conserva su procedimiento de identificar necesidades de baja prioridad y alto "
    "costo, verificar recursos en las de alta prioridad y evitar gasto en funciones de bajo "
    "valor; el hijo conserva el suyo, de construir la hoja multicolumna, listar clientes por "
    "prioridad, listar necesidades, correlacionar con evidencia y priorizar. Ninguno toca al "
    "otro: SANO. SE SOSTIENE EL CASO DEL AUDITOR (acta 102), pese a la salvedad ya puesta: el "
    "par 40 pasa de DIRECCION AFIRMADA a NO RESUELTA. Clase D no cambia (banco 9.6.1 rama "
    "contenido, tercera fila del 9.22: CONTINUA)."
)
cita_40 = (
    "banco 9.6.2 (primer brazo del test de reconocimiento: el hijo no cruza costos en ningun "
    "paso, la salvedad ya declarada ERA la falla) y banco 9.6.3 (procedimiento en los dos "
    "lados: el par es SANO), no la coincidencia de patron 'hoja de calculo que relaciona X "
    "con necesidades'"
)

for fila in lineas:
    if fila["puesto_tramo"] == 28:
        fila["correccion_v103"] = {
            "campo_corregido": "direccion_leida",
            "valor_anterior": fila["direccion_leida"],
            "valor_nuevo": None,
            "cita_corregida": cita_28,
            "razon": razon_28,
        }
    elif fila["puesto_tramo"] == 40:
        fila["correccion_v103"] = {
            "campo_corregido": "direccion_leida",
            "valor_anterior": fila["direccion_leida"],
            "valor_nuevo": None,
            "cita_corregida": cita_40,
            "razon": razon_40,
        }

with io.open(RUTA, "w", encoding="utf-8", newline="\n") as f:
    for fila in lineas:
        f.write(json.dumps(fila, ensure_ascii=False) + "\n")

print("hecho: correccion_v103 aplicada a puestos 28 y 40")
