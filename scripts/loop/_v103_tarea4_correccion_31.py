# -*- coding: utf-8 -*-
"""_v103_tarea4_correccion_31.py . Aplica correccion_v103 (campo
direccion_leida -> null) al puesto 31 de
docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl, TAREA 4 de la vuelta 103 (unica
discrepancia de la relectura ciega por el centro, sin marcar previamente).
Script de un solo uso, no se re-corre."""
import json
import io

RUTA = "docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl"

with io.open(RUTA, encoding="utf-8") as f:
    lineas = [json.loads(l) for l in f if l.strip()]

razon_31 = (
    "CORRECCION DECLARADA (vuelta 103, TAREA 4, relectura ciega al doble del "
    "tramo 1 por el centro, discutible NUEVO, fuera de lo marcado). El texto "
    "viejo de razon y direccion_leida NO SE BORRA. Leido a ciegas hoy (sin "
    "clase, direccion, razon ni paso casado) el par control_estadistico_del_"
    "proceso contra causas_comunes_vs_especiales: el hijo trae QUINCE pasos, "
    "y de ellos NUEVE (documentar hallazgos, comunicar enfocandose en 'el "
    "problema' y no en 'quien', dar seguimiento a la moral del equipo y la "
    "tasa de errores, comunicar que el objetivo es identificar problemas no "
    "culpables, dar seguimiento y apoyo a quienes caen fuera de tolerancias, "
    "fomentar la colaboracion entre turnos y departamentos, analizar la "
    "distribucion de errores entre personas) son territorio de CULTURA DE "
    "COMUNICACION SIN CULPA Y MORAL DE EQUIPO que control_estadistico_del_"
    "proceso NO TIENE EN NINGUNO de sus siete pasos. Ademas el hijo no cabe "
    "en el paso 3 casado ('identificar y eliminar causas especiales'): "
    "tambien trata las causas COMUNES (pasos 5 a 7 del hijo), que en la "
    "madre viven en un paso DISTINTO, el 6 ('iniciar intervencion en el "
    "sistema... para reducir el nivel de defectos'). El test del 9.6.2 falla "
    "POR EXCESO DE GENERO, la misma especie que movio los pares 172 y 161 "
    "(acta 99, vuelta 100), y NO la especie que el puesto 5 dejo a salvo "
    "(desplegar en varios pasos lo que la madre nombra en uno solo, sin "
    "anadir genero nuevo): aqui SI hay genero nuevo (comunicacion sin culpa, "
    "moral, colaboracion entre turnos) en ningun paso de la madre. SE MUEVE: "
    "el par 31 pasa de DIRECCION AFIRMADA a NO RESUELTA. Clase D no cambia "
    "(banco 9.6.1 rama contenido, tercera fila del 9.22: CONTINUA)."
)
cita_31 = (
    "banco 9.6.2 (exceso de genero: comunicacion sin culpa, moral de equipo y "
    "colaboracion entre turnos no estan en ningun paso de la madre; ademas el "
    "hijo cubre pasos 3 Y 6 de la madre, no uno solo), no el titulo compartido "
    "'causas especiales/comunes'"
)

for fila in lineas:
    if fila["puesto_tramo"] == 31:
        fila["correccion_v103"] = {
            "campo_corregido": "direccion_leida",
            "valor_anterior": fila["direccion_leida"],
            "valor_nuevo": None,
            "cita_corregida": cita_31,
            "razon": razon_31,
        }

with io.open(RUTA, "w", encoding="utf-8", newline="\n") as f:
    for fila in lineas:
        f.write(json.dumps(fila, ensure_ascii=False) + "\n")

print("hecho: correccion_v103 aplicada al puesto 31")
