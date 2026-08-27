# -*- coding: utf-8 -*-
"""VUELTA 80, TAREA 3: relectura conjunta de LOS DOS discutibles del acta de
la vuelta 79 que fueron a relectura conjunta (acta 79, seccion 2, D2 y D3;
seccion 5, puntos 2 y 3), con el caso del auditor VERIFICADO CONTRA EL GRAFO
en esta vuelta (dataset/nodos/*.json) antes de decidir.

D2: producto_mercado_fit_motores -> afinar_motor_crecimiento.
  Verificado: pasos_accionables de producto_mercado_fit_motores, paso 4
  ("Usa la contabilidad de la innovacion...") apunta al nodo
  contabilidad_innovacion, YA enlazado en nodos_siguientes de la madre.
  contabilidad_innovacion.nodos_siguientes incluye establecer_linea_base_mvp
  ("Este es el primer paso..."). establecer_linea_base_mvp.nodos_siguientes
  es EXACTAMENTE ['afinar_motor_crecimiento'] ("Es el segundo paso...").
  LA CADENA COMPLETA YA EXISTIA en el grafo de la apertura: producto_mercado
  _fit_motores -> contabilidad_innovacion -> establecer_linea_base_mvp ->
  afinar_motor_crecimiento, en el orden exacto que los propios resumenes
  declaran. Es el CAVEAT MEDIDO de la 9.6.1 ("la familia ENCADENADA no se
  cuenta por radios"): afinar_motor_crecimiento NO es contenido huerfano de
  camino (banco 9.6), esta a tres saltos por el camino que el paso 4 nombra.
  La arista escrita en el tramo 5 de la vuelta 79 es un radio sobre un
  cableado ya establecido. SE REVIERTE, mismo precedente que la correccion
  del primer ejemplar de la 9.6 (proceso_diseno_modelo_negocio_5_fases).

D3: terminologia_clave_breakthrough -> analisis_sintomas.
  Verificado: pasos_accionables de terminologia_clave_breakthrough, paso 2,
  es literalmente "Diferenciar sintomas de causas en cada problema
  detectado". pasos_accionables de analisis_sintomas: recolectar datos de
  ocurrencia, ubicar la falla con diagramas de flujo, aplicar Pareto y
  estratificacion, documentar frecuencia/severidad/tipo. NINGUNO de los
  cuatro DIFERENCIA sintoma de causa: los cuatro CARACTERIZAN el sintoma. El
  entregable de la madre ("Glosario de terminos de diagnostico [...] y lista
  de teorias a probar") no coincide con el del hijo ("analisis documentado
  de sintomas"), que es la senal de verificacion que 9.6.2 declara mas
  fiable que los pasos. Por 9.6.2 ("la vara tiene direccion": el hijo debe
  EJECUTAR el paso, no precederlo), el hijo PRECEDE la accion del paso 2, no
  la ejecuta. SE REVIERTE.

Simetrizado: las dos se quitan de LAS DOS VISTAS a la vez (nodos_siguientes
de la madre Y nodos_previos del hijo), leccion de la vuelta 78 seccion 3.2 y
aplicada de nuevo en la vuelta 79 TAREA 3.1.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

PARES_A_REVERTIR = [
    ("producto_mercado_fit_motores", "afinar_motor_crecimiento"),
    ("terminologia_clave_breakthrough", "analisis_sintomas"),
]


def cargar(nid):
    ruta = NODOS / (nid + ".json")
    return json.loads(ruta.read_text(encoding="utf-8")), ruta


def guardar(nodo, ruta):
    ruta.write_text(json.dumps(nodo, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    ok_total = True
    for madre_id, hijo_id in PARES_A_REVERTIR:
        madre, ruta_madre = cargar(madre_id)
        hijo, ruta_hijo = cargar(hijo_id)

        antes_madre = hijo_id in (madre.get("nodos_siguientes") or [])
        antes_hijo = madre_id in (hijo.get("nodos_previos") or [])
        print("=== %s -> %s ===" % (madre_id, hijo_id))
        print("ANTES: %s en nodos_siguientes de la madre: %s" % (hijo_id, antes_madre))
        print("ANTES: %s en nodos_previos del hijo: %s" % (madre_id, antes_hijo))

        if antes_madre:
            madre["nodos_siguientes"] = [n for n in madre["nodos_siguientes"] if n != hijo_id]
            guardar(madre, ruta_madre)
        if antes_hijo:
            hijo["nodos_previos"] = [n for n in hijo["nodos_previos"] if n != madre_id]
            guardar(hijo, ruta_hijo)

        madre2, _ = cargar(madre_id)
        hijo2, _ = cargar(hijo_id)
        despues_madre = hijo_id in (madre2.get("nodos_siguientes") or [])
        despues_hijo = madre_id in (hijo2.get("nodos_previos") or [])
        print("DESPUES: %s en nodos_siguientes de la madre: %s" % (hijo_id, despues_madre))
        print("DESPUES: %s en nodos_previos del hijo: %s" % (madre_id, despues_hijo))

        ok = antes_madre and antes_hijo and not despues_madre and not despues_hijo
        print("REVERSION SIMETRIZADA CORRECTA: %s" % ok)
        print()
        ok_total = ok_total and ok

    print("LAS DOS REVERSIONES CORRECTAS: %s" % ok_total)
    return 0 if ok_total else 1


if __name__ == "__main__":
    raise SystemExit(main())
