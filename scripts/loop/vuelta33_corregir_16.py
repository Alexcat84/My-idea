# -*- coding: utf-8 -*-
"""vuelta33_corregir_16.py

TAREA 1.1 de la vuelta 33: el origen 16 pasa del grupo del paso 2 al grupo del
paso 6 en el plan sellado docs/loop/PLAN_V32_OPD01_EMBLEMA.json.

DE DONDE SALE LA CORRECCION. Es la caida de cifra publicada del acta 32: la fila
del paso 6 cita en su motivo *los pasos 14 y 16 traen la cadencia* mientras el 16
vive en el grupo de la fila del paso 2. Las dos filas no pueden ser verdad a la
vez, y el verificador de mapas nacio de este ejemplar.

QUIEN TIENE RAZON, MEDIDO Y NO SUPUESTO. El paso 16 original del nodo dice
*Desarrolla tu primera version de forma incremental, en ciclos cortos e
iterativos*: es la CADENCIA. El motivo de la fila del paso 6 estaba bien y la
celda del grupo estaba mal. Este script imprime el texto de los pasos en disputa
antes de tocar nada, para que la medicion quede en la salida y no en mi palabra.

EL TEXTO DEL NODO NO SE TOCA, y hay una razon medible: vuelta32_podar.py elige el
superviviente por el PRIMER origen del grupo (mapa[k][0]) y el texto final lo trae
`pasos_finales`, escrito aparte. min del grupo del paso 2 sigue siendo 2 y el del
paso 6 sigue siendo 8, con el 16 dentro o fuera. Este script COMPRUEBA esa
invariante y se niega a escribir si no se cumple.

TRES CAMPOS DEL MISMO FICHERO CARGAN LA MISMA PARTICION, y los tres se corrigen:
  - `grupos_pasos`   : lo que el encargo nombra y lo que el verificador compara
  - `mapa_pasos`     : el campo OPERATIVO, el que vuelta32_podar.py consume
  - `pruebas_repeticion`: el campo que vuelta32_caso_positivo.py IMPRIME al lado
    de cada huella (no lo usa para decidir: el chequeo es sobre el nodo resultante)
Corregir solo el primero dejaria el plan sellado contradiciendose consigo mismo y
al verificador en verde encima de la contradiccion. Va declarado en el reporte.

EL TEXTO VIEJO NO SE BORRA (EJECUTOR.md regla 8): entra entero en un bloque nuevo
`correcciones_declaradas` en la raiz del plan, con su fecha, su motivo y las
particiones vieja y nueva escritas enteras.

Uso: python scripts/loop/vuelta33_corregir_16.py [--aplicar]
Sin --aplicar solo mide e imprime lo que escribiria.
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "loop", "PLAN_V32_OPD01_EMBLEMA.json")

VIEJO_G2 = [2, 6, 11, 15, 16, 19]
NUEVO_G2 = [2, 6, 11, 15, 19]
VIEJO_G6 = [8, 14, 17, 22]
NUEVO_G6 = [8, 14, 16, 17, 22]

FECHA = "2026-08-15"

CORRECCION = {
    "fecha": FECHA,
    "vuelta": 33,
    "campo": "particion de origenes de producto_minimo_viable (grupos_pasos, mapa_pasos, pruebas_repeticion)",
    "que_se_corrige": (
        "EL ORIGEN 16 ESTABA EN EL GRUPO DEL PASO 2 Y PERTENECE AL DEL PASO 6. "
        "Es la caida de cifra publicada del acta 32: el motivo de la fila del paso 6 "
        "cita 'los pasos 14 y 16 traen la cadencia' mientras la celda del grupo ponia "
        "el 16 en la fila del paso 2. Las dos no pueden ser verdad a la vez."
    ),
    "quien_tenia_razon": (
        "EL MOTIVO. El paso 16 original dice 'Desarrolla tu primera version de forma "
        "incremental, en ciclos cortos e iterativos', que es la cadencia del paso 6 del "
        "resultado, no el conjunto minimo del paso 2. Medido contra pasos_originales en "
        "esta misma vuelta, no copiado de un acta."
    ),
    "efecto_sobre_el_nodo": (
        "NINGUNO, y se comprueba antes de escribir: vuelta32_podar.py toma el superviviente "
        "por el PRIMER origen del grupo y el texto por pasos_finales. min(grupo del paso 2) "
        "sigue siendo 2 y min(grupo del paso 6) sigue siendo 8 con el 16 dentro o fuera. "
        "La cobertura sigue en 22 de 22 sin huecos ni repetidos. dataset/nodos NO se toca."
    ),
    "particion_vieja_grupos_pasos": [[1, 10], VIEJO_G2, [3, 9, 13, 18], [4, 7, 12, 20], [5, 21], VIEJO_G6],
    "particion_nueva_grupos_pasos": [[1, 10], NUEVO_G2, [3, 9, 13, 18], [4, 7, 12, 20], [5, 21], NUEVO_G6],
    "mapa_pasos_viejo": {"1": [1, 10], "2": VIEJO_G2, "3": [3, 9, 13, 18], "4": [4, 7, 12, 20], "5": [5, 21], "6": VIEJO_G6},
    "pruebas_repeticion_viejas": [
        {"origenes": VIEJO_G2, "huella_repetida": "conjunto mínimo de características"},
        {"origenes": VIEJO_G6, "huella_repetida": "Itera o cambia de rumbo si nadie"},
        {"origenes": [4, 7, 12, 20], "huella_repetida": "earlyvangelists"},
        {"origenes": [3, 9, 13, 18], "huella_repetida": "Agrega funciones nuevas solo"},
    ],
    "limite_declarado": (
        "La huella de la prueba de repeticion del grupo del paso 2 es 'conjunto minimo de "
        "caracteristicas' y el paso 16 nunca la contuvo: la prueba jamas midio al 16, porque "
        "vuelta32_caso_positivo.py cuenta la huella sobre el NODO RESULTANTE y solo IMPRIME "
        "los origenes. O sea que la celda mala no falseo ningun verde: no habia instrumento "
        "que la leyera. Ese es exactamente el hueco que el verificador de mapas cierra."
    ),
}


def medir(nodo):
    print("--- MEDICION DEL DIA, los pasos en disputa, leidos del plan sellado ---")
    orig = nodo["pasos_originales"]
    for i in (2, 6, 8, 14, 15, 16, 17, 19, 22):
        print("  paso %2d: %s" % (i, orig[i - 1]))
    print()
    print("--- LA INVARIANTE QUE PROTEGE AL NODO ---")
    print("  primer origen del grupo del paso 2: viejo %d, nuevo %d" % (VIEJO_G2[0], NUEVO_G2[0]))
    print("  primer origen del grupo del paso 6: viejo %d, nuevo %d" % (VIEJO_G6[0], NUEVO_G6[0]))
    nueva = [[1, 10], NUEVO_G2, [3, 9, 13, 18], [4, 7, 12, 20], [5, 21], NUEVO_G6]
    todos = sorted(x for g in nueva for x in g)
    print("  cobertura nueva: %d origenes, rango %d a %d, repetidos %s, faltan %s"
          % (len(todos), min(todos), max(todos),
             sorted({x for x in todos if todos.count(x) > 1}),
             sorted(set(range(1, 23)) - set(todos))))
    ok = (VIEJO_G2[0] == NUEVO_G2[0] and VIEJO_G6[0] == NUEVO_G6[0]
          and todos == list(range(1, 23)))
    print("  INVARIANTE: %s" % ("SE CUMPLE" if ok else "ROTA"))
    return ok


def main():
    aplicar = "--aplicar" in sys.argv
    with open(PLAN, encoding="utf-8") as fh:
        plan = json.load(fh)
    nodo = plan["nodos"][0]

    print("PLAN  : %s" % PLAN)
    print("NODO  : %s" % nodo["nodo"])
    print("MODO  : %s" % ("--aplicar" if aplicar else "solo medir"))
    print("=" * 78)

    if [g["origenes"] for g in nodo["grupos_pasos"]][1] != VIEJO_G2:
        print("EL PLAN YA NO TIENE LA PARTICION VIEJA. Nada que corregir aqui.")
        return 1

    if not medir(nodo):
        print("SE ABORTA: la invariante no se cumple.")
        return 1

    for g in nodo["grupos_pasos"]:
        if g["origenes"] == VIEJO_G2:
            g["origenes"] = list(NUEVO_G2)
        elif g["origenes"] == VIEJO_G6:
            g["origenes"] = list(NUEVO_G6)
    nodo["mapa_pasos"]["2"] = list(NUEVO_G2)
    nodo["mapa_pasos"]["6"] = list(NUEVO_G6)
    for p in nodo.get("pruebas_repeticion") or []:
        if p["origenes"] == VIEJO_G2:
            p["origenes"] = list(NUEVO_G2)
        elif p["origenes"] == VIEJO_G6:
            p["origenes"] = list(NUEVO_G6)

    plan.setdefault("correcciones_declaradas", []).append(CORRECCION)

    print()
    print("--- LO QUE QUEDA ESCRITO ---")
    for i, g in enumerate(nodo["grupos_pasos"], 1):
        print("  grupo del paso %d: %s" % (i, g["origenes"]))
    print("  mapa_pasos: %s" % json.dumps(nodo["mapa_pasos"], ensure_ascii=False))
    print("  correcciones_declaradas: %d bloque(s)" % len(plan["correcciones_declaradas"]))

    if not aplicar:
        print("\nSIN --aplicar: cero escrituras.")
        return 0

    # El plan sellado esta escrito con fin de linea CRLF: se conserva, para que el
    # diff muestre SOLO las celdas corregidas y no el fichero entero.
    with open(PLAN, "w", encoding="utf-8", newline="\r\n") as fh:
        fh.write(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
    print("\nESCRITO: %s" % PLAN)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
