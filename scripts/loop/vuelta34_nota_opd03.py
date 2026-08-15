# -*- coding: utf-8 -*-
"""vuelta34_nota_opd03.py - la nota de OP-D-03 queda READJUDICADA.

CORRECCION DECLARADA, y el texto viejo se queda ENTERO delante (EJECUTOR.md regla
8). El campo `nota` no se reescribe: se le anade el bloque de correccion al final.
Misma forma que scripts/loop/vuelta32_registros.py hizo con OP-D-02.

Uso:
  python scripts/loop/vuelta34_nota_opd03.py            (simulacion)
  python scripts/loop/vuelta34_nota_opd03.py --aplicar
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

MARCA = "CORRECCION DECLARADA (2026-08-15, vuelta 34"

CORRECCION = (
    " " + MARCA + "; el texto viejo se queda entero arriba): EL ORDEN INTERNO VA POR EL PASO 2. "
    "PASO 1 (destejer las TRES costuras) HECHO, y de las tres SOLO UNA necesitaba operacion: "
    "optimizacion_embudo_get_customers y split_testing_experimentos_ab ya estaban CONSUMIDAS por "
    "la fase 01 (OP-F-04-WEI se llevo el bloque 6 a 10 del primero y OP-F-04-RAC el 6 a 9 del "
    "segundo), medido hoy contra el arbol por la huella del bloque ido y no copiado de un acta; y "
    "ab_testing_optimizacion se destejio en esta vuelta, de DIEZ pasos a CINCO, por la frontera "
    "que 01_FUENTES.md linea 947 ya tenia escrita (los pasos 1 a 5 y 6 a 10 dicen la misma prueba "
    "A/B dos veces). El campo preservar se comprobo DONDE VIVE HOY y no se perdio nada: la "
    "significancia del 95 por ciento en split_testing, y el cambio porcentual y el grupo de "
    "control de desempeno similar en metodologia_evaluacion_entrenamiento_ventas. PASO 3 (releer "
    "738 y 1061) HECHO Y VOLCADO por el carril del banco 9.10, con su barrido de tablas derivadas "
    "en el mismo acto: el 738 pasa de B a D y el 1061 de A a D, y el marcador queda en n 3388, A "
    "581, B 83, C 8, D 2716. LOS QUINCE PARES DEL ACTO ESTAN LEIDOS: los siete que faltaban se "
    "leyeron como LECTURAS DIRIGIDAS LD-75 a LD-81 por P.5 y por la decision 3 del fundador (se "
    "leen DESPUES del destejido), los siete D, sin mover n. LA RESPUESTA DE P.5: el acto NO es "
    "una familia de seis, son DOS FAMILIAS CERRADAS, y el 1061 era el unico hilo que las cosia; "
    "el recomputo de la casa lo confirma pasando de 334 a 335 componentes y de 279 a 281 "
    "cerradas. LO QUE QUEDA: el PASO 2, decidir sobre los seis, que es la fusion y NO la toma "
    "esta vuelta. El campo superviviente sigue en null a proposito."
)


def main():
    aplicar = "--aplicar" in sys.argv
    for nid, esperado in (("ab_testing_optimizacion", 5),
                          ("optimizacion_embudo_get_customers", 5),
                          ("split_testing_experimentos_ab", 5)):
        d = json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))
        real = len(d.get("pasos_accionables") or [])
        print("  medicion del dia: %-38s %d pasos %s"
              % (nid, real, "OK" if real == esperado else "ABORTA"))
        if real != esperado:
            return 1

    lineas = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    encontrada = False
    for o in lineas:
        if o["id_op"] != "OP-D-03":
            continue
        encontrada = True
        if MARCA in (o.get("nota") or ""):
            print("YA APLICADA")
            return 0
        print("\n--- NOTA VIEJA (se queda entera) ---")
        print(o["nota"])
        o["nota"] = (o.get("nota") or "") + CORRECCION
    if not encontrada:
        print("ERROR: OP-D-03 no esta en %s" % OPS)
        return 1

    if not aplicar:
        print("\n(simulacion: sin --aplicar no se escribe nada)")
        return 0

    with io.open(OPS, "w", encoding="utf-8") as fh:
        for o in lineas:
            fh.write(json.dumps(o, ensure_ascii=False) + "\n")

    de_vuelta = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    ids = [o["id_op"] for o in de_vuelta]
    rotas = sum(1 for o in de_vuelta
                for d in (o.get("depende_de") or []) + (o.get("bloquea_a") or [])
                if d not in set(ids))
    print("\nVERIFICADO TRAS ESCRIBIR: %d lineas JSON validas, %d ids unicos, %d dependencias rotas"
          % (len(de_vuelta), len(set(ids)), rotas))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
