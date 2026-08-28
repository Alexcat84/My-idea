# -*- coding: utf-8 -*-
r"""vuelta99_tarea2_relectura147.py . VUELTA 99, TAREA 2: LA RELECTURA CONJUNTA
DEL PAR 147 (acta 98, seccion 3.2 y TAREA 2 del encargo).

QUE DECIDE: si `consortium_benchmarking` cabe ENTERO dentro del paso 2 de
`clasificacion_benchmarking` ("decidir el tipo de participantes: internos,
externos, competidores o no competidores"), que es el test de reconocimiento
del banco 9.6.2 ("el hijo cabe entero dentro de UN paso de la madre, y la
madre conserva materia propia que el hijo no toca en ningun paso").

EL JUICIO LITERAL, paso por paso del hijo contra el paso 2 de la madre:
  1. identificar organizaciones interesadas: prepara la decision, no es ella.
  2. acordar alcance, metricas, definiciones y cronograma: es diseno del
     estudio, no tipo de participantes (eso lo cubren otros pasos de la
     madre, el 1 y el 3, no el 2).
  3. designar un facilitador: logistica de ejecucion.
  4. fijar criterios de validacion de datos: gobierno de datos, ejecucion.
  5. ejecutar el estudio y compartir hallazgos: ejecucion pura, aguas abajo
     de cualquier decision.
El entregable de la madre es una DECISION documentada ("que oriente el
diseno"); el entregable del hijo es un CONSORCIO FORMALIZADO, con acuerdo de
alcance, metricas y cronograma ya definidos: eso ya es la ejecucion que la
decision de la madre solo orienta, no la propia decision.

VEREDICTO DE ESTA VUELTA: el test del 9.6.2 FALLA. El hijo no cabe entero
dentro del paso 2 (ni de ningun otro paso de la madre): los pasos 2 a 5 del
hijo son diseno y ejecucion, aguas abajo de la taxonomia que la madre fija.
SE SOSTIENE EL CASO DEL AUDITOR: el par 147 pasa de DIRECCION AFIRMADA a NO
RESUELTA. Correccion declarada, sin borrar el texto viejo: este script lee
el campo `correccion_v99` si existe (no toca `direccion_leida` ni `razon`
originales) y recomputa la tabla del tramo con esa correccion aplicada.

MECANICA DE ROJO: si el conteo de partida (antes de la correccion) no
reproduce EXACTO 20 direccion afirmada / 30 NO RESUELTA / 50 filas del acta
98, no se talla nada (la cifra de referencia no cuadra y aplicar la
correccion sobre ella seria construir sobre un numero no verificado).

USO:
  python scripts/loop/vuelta99_tarea2_relectura147.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMO3 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO3_V98.jsonl")

BASE_AFIRMADA = 20
BASE_NO_RESUELTA = 30
BASE_TOTAL = 50


def cargar():
    with io.open(TRAMO3, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    filas = cargar()
    if len(filas) != BASE_TOTAL:
        print("ROJO: %s trae %d filas, se esperaban %d. NO SE TALLA NADA."
              % (os.path.basename(TRAMO3), len(filas), BASE_TOTAL))
        return 1

    afirmada_antes = sum(1 for f in filas if f.get("direccion_leida"))
    no_resuelta_antes = len(filas) - afirmada_antes
    if afirmada_antes != BASE_AFIRMADA or no_resuelta_antes != BASE_NO_RESUELTA:
        print("ROJO: el conteo de partida da afirmada=%d, no_resuelta=%d; "
              "el acta 98 dice %d y %d. NO SE TALLA NADA."
              % (afirmada_antes, no_resuelta_antes, BASE_AFIRMADA, BASE_NO_RESUELTA))
        return 1

    fila_147 = next((f for f in filas if f.get("puesto_tramo") == 147), None)
    if fila_147 is None:
        print("ROJO: no existe la fila puesto_tramo=147 en %s. NO SE TALLA NADA."
              % os.path.basename(TRAMO3))
        return 1
    if not fila_147.get("direccion_leida"):
        print("ROJO: la fila 147 ya esta sin direccion antes de aplicar nada. NO SE TALLA NADA.")
        return 1

    correccion = fila_147.get("correccion_v99")
    print("=" * 90)
    print("RELECTURA CONJUNTA DEL PAR 147 (vuelta 99, TAREA 2). Fichero: %s"
          % os.path.basename(TRAMO3))
    print("=" * 90)
    print()
    print("ANTES (texto viejo, SIN TOCAR): direccion_leida = %r" % fila_147["direccion_leida"])
    print("  clase (SIN TOCAR, no cambia): %r" % fila_147["clase"])
    print()
    if correccion is None:
        print("correccion_v99: AUSENTE. Se talla el ANTES solamente.")
        print("afirmada ANTES: %d . no_resuelta ANTES: %d . total %d . proporcion NO RESUELTA: %.1f%%"
              % (afirmada_antes, no_resuelta_antes, len(filas),
                 100.0 * no_resuelta_antes / len(filas)))
        return 0

    print("correccion_v99 (anadida, campo viejo intacto): %r" % correccion)
    afirmada_despues = afirmada_antes - 1
    no_resuelta_despues = no_resuelta_antes + 1
    print()
    print("| medida | antes | despues |")
    print("|---|---:|---:|")
    print("| direccion leida y afirmada | %d | %d |" % (afirmada_antes, afirmada_despues))
    print("| direccion NO RESUELTA | %d | %d |" % (no_resuelta_antes, no_resuelta_despues))
    print("| proporcion NO RESUELTA | %.1f%% | %.1f%% |"
          % (100.0 * no_resuelta_antes / len(filas), 100.0 * no_resuelta_despues / len(filas)))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
