# -*- coding: utf-8 -*-
r"""vuelta106_tarea4_4_correccion_145.py . VUELTA 106, TAREA 4.4: aplica
correccion_v106 al puesto 145 de docs/plan/OP_E_03_LECTURA_TRAMO3_V98.jsonl
(direccion_leida a null; clase D sin cambio), tras la lectura entera a
ciegas del par (paso_a_traves_de_la_accion -> proposito_como_motor_energia).
Solo esa linea se re-serializa; las demas se dejan byte a byte identicas.

USO:
  python scripts/loop/vuelta106_tarea4_4_correccion_145.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO3_V98.jsonl")

CORRECCION = {
    "campo_corregido": "direccion_leida",
    "valor_anterior": "poder_a_traves_de_la_accion -> proposito_como_motor_energia",
    "valor_nuevo": None,
    "cita_corregida": "banco 9.6.2 (test de reconocimiento); banco 9.6.3 (que queda fuera y de que lado)",
    "razon": (
        "CORRECCION DECLARADA (vuelta 106, TAREA 4.4, lectura entera a ciegas del SATELITE "
        "hallado en la TAREA 4.3, pregunta de tres vias sobre los tramos 3 y 4). El texto viejo "
        "de razon y direccion_leida NO SE BORRA: esta correccion se anade aparte. Leidos hoy los "
        "dos nodos enteros. El primer brazo del test de reconocimiento del 9.6.2 falla: el hijo "
        "(proposito_como_motor_energia) NO cabe entero dentro del paso 4 de la madre (\"Vincular "
        "conscientemente el trabajo intelectual cotidiano a un proposito o impacto mayor para "
        "sostener la energia a largo plazo\"). Los pasos 1 a 3 del hijo (articular por escrito la "
        "mision, vincular cada tarea operativa con esa narrativa, revisar la narrativa con "
        "senales de feedback) si desarrollan ese paso, pero el paso 4 propio del hijo (\"evitar "
        "sustituir el pensamiento profundo por 'mera accion fisica' como escape de la "
        "incertidumbre\") es material AJENO a ese paso 4 de la madre, y tensiona con la tesis "
        "central del propio nodo madre, titulado precisamente 'Poder a Traves de la Accion: "
        "Unificar el Pensamiento Mediante el Actuar': la madre defiende actuar como forma de "
        "pensar, y el hijo, en su ultimo paso, advierte contra sustituir el pensamiento por la "
        "accion. El hijo comparte vocabulario con el paso 4 de la madre (proposito, energia) "
        "pero no es SU ejecucion completa: es un nodo de un linaje distinto (proposito/mision "
        "como motor) que se solapa parcialmente, no que se despliega entero desde ese unico "
        "paso. SE MUEVE: el par pasa de DIRECCION AFIRMADA a NO RESUELTA. Clase D no cambia. "
        "DISCUTIBLE: marcado para la relectura ciega del auditor, la tension detectada admite "
        "lectura alternativa (los pasos 1 a 3 SI desarrollan el paso 4 entero y el paso 4 propio "
        "del hijo es solo una cautela metodologica dentro del mismo tema, no material ajeno)."
    ),
}


def main():
    with io.open(RUTA, encoding="utf-8") as f:
        lineas = f.readlines()

    tocado = False
    nuevas = []
    for linea in lineas:
        if not linea.strip():
            nuevas.append(linea)
            continue
        fila = json.loads(linea)
        if fila.get("puesto_tramo") == 145:
            if "correccion_v106" in fila:
                raise SystemExit("ROJO: el puesto 145 ya trae correccion_v106, no se duplica")
            fila["correccion_v106"] = CORRECCION
            nuevas.append(json.dumps(fila, ensure_ascii=False) + "\n")
            tocado = True
        else:
            nuevas.append(linea)

    if not tocado:
        raise SystemExit("ROJO: no se encontro el puesto 145 en %s" % RUTA)

    with io.open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.writelines(nuevas)
    print("OK: correccion_v106 anadida al puesto 145 de %s" % os.path.relpath(RUTA, RAIZ))


if __name__ == "__main__":
    main()
