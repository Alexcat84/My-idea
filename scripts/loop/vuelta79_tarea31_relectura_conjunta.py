# -*- coding: utf-8 -*-
"""VUELTA 79, TAREA 3.1: relectura conjunta de la unica discrepancia que la
vuelta 78 dejo para relectura (acta 78, seccion 3, D3; discutible 3 del
reporte de la vuelta 78): extraer_priorizar_hipotesis -> value_proposition_startup.

VERIFICADO CONTRA EL GRAFO EN ESTA VUELTA (dataset/nodos/*.json):
  - Paso 1 de la madre (extraer_priorizar_hipotesis): "Lista todo lo que
    tiene que ser cierto sobre tu modelo de negocio, tu propuesta de valor y
    tu cliente". La ACCION del paso es LISTAR. La propuesta de valor es uno
    de los TRES objetos sobre los que se lista (modelo de negocio, propuesta
    de valor, cliente), no la accion que se ejecuta.
  - El resumen de la propia madre lo dice con estas palabras: "A partir de tu
    mapa de propuesta de valor y tu modelo de negocio, identifica todas las
    suposiciones que tienen que ser ciertas...". La propuesta de valor es
    INSUMO que PRECEDE a este paso, no su resultado.
  - El hijo (value_proposition_startup) tiene 3 pasos: identificar problemas
    del segmento, definir que caracteristicas los resuelven, verificar el
    encaje hablando con clientes. Ninguno de los tres es "listar hipotesis":
    son los pasos que PRODUCEN la propuesta de valor que la madre da por ya
    existente ("a partir de tu mapa de propuesta de valor").
  - Banco 9.6.2, formulacion literal citada por el auditor: "la prueba de que
    el paso de la madre es un procedimiento es que existe el hijo que lo
    ejecuta". Aqui el hijo NO ejecuta "listar hipotesis": lo PRECEDE.
  - Contraste con la hermana que SI pasa la vara en el mismo hub (reporte de
    la vuelta 78, seccion 4.4 punto 3): etapa_build_business_case, paso 1
    "Definir el mercado objetivo, posicionamiento y propuesta de valor del
    producto". Ahi la ACCION del paso ES definir la propuesta de valor, y el
    hijo es como se define. Aqui la accion del paso es listar HIPOTESIS
    (sobre tres objetos), no definir ni desplegar la propuesta de valor.
  - Y el propio reporte de la vuelta 78 aplico este mismo criterio ocho
    lineas mas abajo para descartar timing_solicitud_referidos ->
    fase_adopt_ciclo_cliente ("el paso senalado nombra la fase Adopt solo
    como ejemplo parentetico"): nombrar/mencionar un objeto dentro de un paso
    no es lo mismo que el paso mandar una accion sobre ese objeto. Es la
    misma especie aplicada de forma inconsistente en la misma tanda.

DECISION: LA ARISTA SE REVIERTE. El hijo no ejecuta el paso 1 de la madre: lo
precede. No hay jerarquia 9.6.2 en este sentido. El caso del auditor se
confirma contra el grafo.

Simetrizado: se quita de LAS DOS VISTAS a la vez (nodos_siguientes de la
madre Y nodos_previos del hijo), leccion de la vuelta 78 seccion 3.2 (si solo
se quita de una vista, el paso 5 de run_phase1.py la reciproca de la vista
que queda y la arista reaparece sola).
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

MADRE = "extraer_priorizar_hipotesis"
HIJO = "value_proposition_startup"


def cargar(nid):
    ruta = NODOS / (nid + ".json")
    return json.loads(ruta.read_text(encoding="utf-8")), ruta


def guardar(nodo, ruta):
    ruta.write_text(json.dumps(nodo, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    madre, ruta_madre = cargar(MADRE)
    hijo, ruta_hijo = cargar(HIJO)

    antes_madre = HIJO in (madre.get("nodos_siguientes") or [])
    antes_hijo = MADRE in (hijo.get("nodos_previos") or [])
    print("ANTES: %s en nodos_siguientes de la madre: %s" % (HIJO, antes_madre))
    print("ANTES: %s en nodos_previos del hijo: %s" % (MADRE, antes_hijo))

    if antes_madre:
        madre["nodos_siguientes"] = [n for n in madre["nodos_siguientes"] if n != HIJO]
        guardar(madre, ruta_madre)
    if antes_hijo:
        hijo["nodos_previos"] = [n for n in hijo["nodos_previos"] if n != MADRE]
        guardar(hijo, ruta_hijo)

    madre2, _ = cargar(MADRE)
    hijo2, _ = cargar(HIJO)
    despues_madre = HIJO in (madre2.get("nodos_siguientes") or [])
    despues_hijo = MADRE in (hijo2.get("nodos_previos") or [])
    print("DESPUES: %s en nodos_siguientes de la madre: %s" % (HIJO, despues_madre))
    print("DESPUES: %s en nodos_previos del hijo: %s" % (MADRE, despues_hijo))

    ok = antes_madre and antes_hijo and not despues_madre and not despues_hijo
    print()
    print("REVERSION SIMETRIZADA CORRECTA: %s" % ok)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
