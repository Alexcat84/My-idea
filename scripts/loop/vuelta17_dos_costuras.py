"""VUELTA 17, TAREA 2. Instrumento propio, SOLO LECTURA.

Reune y VERIFICA contra el grafo la evidencia ya medida sobre las dos costuras
que la decision del fundador del 14 ago 2026 saca de "sin dueno":
`lienzo_modelo_negocio` y `planificacion_recoleccion_datos`.

No relee los nodos: mide lo que se puede medir de los archivos mecanicos, que es
lo que la operacion necesita para escribirse (nomina de pares, clases, si hay
gemelo vigente, y si algun otro nodo la nombra en su cableado).

  1. la ficha mecanica de la costura (docs/COSTURAS_INTERNAS.jsonl)
  2. todos los pares del cribado donde aparece, con su clase y su puesto
  3. si tiene alguna A vigente (o sea gemelo con quien fundirse hoy)
  4. si aparece en la nomina `nodos` de alguna de las 69 operaciones
  5. el estado del cribado de su dominio, porque un "sin A vigente" en un
     dominio sin cribar no vale lo mismo que en uno cribado
  6. las aristas paso a nodo ya calibradas que la tocan

Uso: python scripts/loop/vuelta17_dos_costuras.py
"""

import json
import os
import collections

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = lambda *p: os.path.join(RAIZ, *p)

OBJETIVO = ["lienzo_modelo_negocio", "planificacion_recoleccion_datos"]


def jsonl(ruta):
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                yield json.loads(linea)


def main():
    veredictos = list(jsonl(D("docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")))
    costuras = list(jsonl(D("docs", "COSTURAS_INTERNAS.jsonl")))
    operaciones = list(jsonl(D("docs", "plan", "OPERACIONES.jsonl")))
    calibrado = list(jsonl(D("docs", "plan", "PASO_NODO_CALIBRADO.jsonl")))

    print("MATERIA PRIMA: veredictos", len(veredictos), "| costuras", len(costuras),
          "| operaciones", len(operaciones), "| paso a nodo calibrado", len(calibrado))
    print("cribado por dominio (pares con veredicto):",
          dict(sorted(collections.Counter(v["dominio"] for v in veredictos).items())))
    print("clases del archivo entero:",
          dict(sorted(collections.Counter(v["clase"] for v in veredictos).items())))
    print()

    for nodo in OBJETIVO:
        print("=" * 78)
        print(nodo)
        print("=" * 78)

        ficha = [c for c in costuras if c["node_id"] == nodo]
        for c in ficha:
            print("  FICHA MECANICA DE COSTURA: dominio", c["dominio"], "| pasos", c["pasos"],
                  "| corte", c["corte"], "| senal de bloque", c["sim_bloque"],
                  "| senal de pareja", c["sim_pareja"], "| disparo por bloque", c["disparo_bloque"])
            print("    titulo:", c["titulo"])
            print("    la pareja que disparo:", c["pareja"], "->", c["paso_a"], "//", c["paso_b"])
        if not ficha:
            print("  NO tiene ficha en COSTURAS_INTERNAS.jsonl")

        pares = [v for v in veredictos if nodo in (v["nodo_a"], v["nodo_b"])]
        print("  PARES DEL CRIBADO donde aparece:", len(pares))
        for v in sorted(pares, key=lambda x: x["puesto_intra"]):
            otro = v["nodo_b"] if v["nodo_a"] == nodo else v["nodo_a"]
            print("    puesto", v["puesto_intra"], "| clase", v["clase"], "| contra", otro)
        aes = [v for v in pares if v["clase"] == "A"]
        print("  A VIGENTES (gemelos con quien fundirse hoy):", len(aes),
              [v["puesto_intra"] for v in aes])

        dom = ficha[0]["dominio"] if ficha else "?"
        del_dom = [v for v in veredictos if v["dominio"] == dom]
        print("  ESTADO DEL CRIBADO DE SU DOMINIO:", dom, "->", len(del_dom),
              "pares con veredicto, clases",
              dict(sorted(collections.Counter(v["clase"] for v in del_dom).items())))

        duenos = [o["id_op"] for o in operaciones if nodo in (o.get("nodos") or [])]
        print("  APARECE EN LA NOMINA `nodos` DE:", duenos if duenos else "NINGUNA operacion")

        como_madre = [c for c in calibrado if c["madre"] == nodo]
        como_hijo = [c for c in calibrado if c["hijo"] == nodo]
        print("  PASO A NODO CALIBRADO: como madre", len(como_madre), "| como hijo", len(como_hijo))
        for c in como_madre:
            print("    madre, paso", c["paso"], "->", c["hijo"], "| arista ya escrita:", c["arista"])
        for c in como_hijo:
            print("    hijo de", c["madre"], "paso", c["paso"], "| arista ya escrita:", c["arista"])
        print()


if __name__ == "__main__":
    main()
