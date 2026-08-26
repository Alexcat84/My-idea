"""VUELTA 76, TAREA 1.4: de los 168 nodos distintos de los 32 racimos de
docs/RACIMOS_MIEMBROS.jsonl, cuenta cuantos NO son nombrados por NINGUNA
operacion de docs/plan/OPERACIONES.jsonl en sus campos `nodos`, `eliminar` o
`superviviente`.

EL CRUCE ES POR MEMBRESIA EXACTA DE LISTA JSON, no por texto ni por grep: cada
campo es un array de ids y se compara elemento a elemento. Eso es MAS estricto
que una frontera de palabra sobre texto plano (no puede haber falso positivo
por substring, porque no se busca substring: se busca igualdad de string
dentro de una lista ya parseada), y evita el modo de fallo que la vuelta 75
declaro para el D9 (grep -F contando OP-M-03-I dentro de OP-M-03-II).

`superviviente` es un string o null, no una lista: se trata aparte.
"""
import json
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]

RACIMOS = RAIZ / "docs" / "RACIMOS_MIEMBROS.jsonl"
OPERACIONES = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"

# Mapeo racimo -> grupo/decision de docs/MESA_RACIMOS.md, leido a mano de las
# tres tablas (GRUPO 1 seccion 2, GRUPO 2 seccion 3, GRUPO 3 seccion 4). Las
# 6 + 13 + 13 = 32 nombres cubren los 32 racimos de RACIMOS_MIEMBROS.jsonl
# sin resto y sin solape.
GRUPO_1 = {
    "Accion correctiva",
    "Los puntos de Deming en el titulo",
    "Eliminacion de causas de error",
    "Consejo de calidad",
    "Metas de calidad",
    "Programa de catorce pasos de Crosby",
}
GRUPO_2 = {
    "No culpar a la persona, arreglar el sistema",
    "Causas comunes y responsabilidad del sistema",
    "La estructura de cinturones de Six Sigma",
    "Auditoria de calidad",
    "Benchmarking",
    "Ciclo de mejora PDCA / PDSA",
    "Clasificacion de defectos",
    "Analisis de causa raiz",
    "Fitness for purpose",
    "Costo de calidad",
    "Plan y matriz de control",
    "Poka yoke",
    "Diversidad en el diseno",
}
GRUPO_3 = {
    "Cradle to cradle",
    "Portafolio: revisar, podar, reasignar",
    "Customer discovery: salir a hablar con el cliente",
    "Los cinco porques",
    "Pivotar o proceder",
    "El avance y el compromiso en la venta",
    "Encuadre del problema (How Might We)",
    "Mapeo del flujo de valor",
    "Las reglas del brainstorming",
    "El efectivo contra la ganancia",
    "La etapa de investigacion en la venta",
    "Estrategia de innovacion de producto",
    "Obtencion de compromiso",
}


def decision_de(racimo):
    if racimo in GRUPO_1:
        return "DECISION 1 (grupo 1, programas desmontados)"
    if racimo in GRUPO_2:
        return "DECISION 2 (grupo 2, doctrina-columna de mundo)"
    if racimo in GRUPO_3:
        return "DECISION 3 (grupo 3, trece racimos del nucleo)"
    return "SIN GRUPO EN MESA_RACIMOS.md (a verificar)"


def cargar_jsonl(ruta):
    return [json.loads(l) for l in ruta.read_text(encoding="utf-8").splitlines() if l.strip()]


def main():
    racimos = cargar_jsonl(RACIMOS)
    operaciones = cargar_jsonl(OPERACIONES)

    nombrados = set()
    for op in operaciones:
        for nid in op.get("nodos") or []:
            nombrados.add(nid)
        for nid in op.get("eliminar") or []:
            nombrados.add(nid)
        sup = op.get("superviviente")
        if sup:
            nombrados.add(sup)

    tabla = []
    total_nodos = 0
    total_sin_op = 0
    for r in racimos:
        ids_racimo = [m["node_id"] for m in r["miembros"]]
        sin_op = [nid for nid in ids_racimo if nid not in nombrados]
        total_nodos += len(ids_racimo)
        total_sin_op += len(sin_op)
        tabla.append({
            "racimo": r["racimo"],
            "dominio_censado": r["dominio_censado"],
            "tamano": len(ids_racimo),
            "sin_operacion": len(sin_op),
            "ids_sin_operacion": sin_op,
            "decision": decision_de(r["racimo"]),
        })

    print(f"TOTAL DE NODOS EN LOS 32 RACIMOS (con repeticion entre racimos): {total_nodos}")
    print(f"TOTAL SIN NINGUNA OPERACION QUE LOS NOMBRE (con repeticion): {total_sin_op}")
    print()

    # Tambien la cifra sobre nodos DISTINTOS (168), porque 3 nodos se
    # comparten entre dos racimos (declarado en el commit d4d2652f).
    distintos = set()
    for r in racimos:
        for m in r["miembros"]:
            distintos.add(m["node_id"])
    distintos_sin_op = sorted(n for n in distintos if n not in nombrados)
    print(f"NODOS DISTINTOS EN LOS 32 RACIMOS: {len(distintos)}")
    print(f"NODOS DISTINTOS SIN NINGUNA OPERACION QUE LOS NOMBRE: {len(distintos_sin_op)}")
    print()

    print("TABLA POR RACIMO Y POR DECISION DE MESA_RACIMOS (tamano censado / sin operacion):")
    sin_grupo = 0
    for fila in tabla:
        marca = "  <-- TIENE SUELTOS SIN OPERACION" if fila["sin_operacion"] else ""
        if fila["decision"].startswith("SIN GRUPO"):
            sin_grupo += 1
        print(f"  [{fila['decision']}] {fila['racimo']} ({fila['dominio_censado']}): {fila['tamano']} miembros, {fila['sin_operacion']} sin operacion{marca}")
        if fila["sin_operacion"]:
            for nid in fila["ids_sin_operacion"]:
                print(f"      - {nid}")

    print()
    print(f"RACIMOS SIN GRUPO ASIGNADO EN MESA_RACIMOS.md: {sin_grupo} de {len(tabla)}")

    print()
    print("RESUMEN POR DECISION:")
    por_decision = defaultdict(lambda: [0, 0])
    for fila in tabla:
        por_decision[fila["decision"]][0] += fila["tamano"]
        por_decision[fila["decision"]][1] += fila["sin_operacion"]
    for dec, (tam, sinop) in sorted(por_decision.items()):
        print(f"  {dec}: {tam} nodos (con repeticion), {sinop} sin operacion")

    print()
    print("CIFRA CONOCIDA A REPRODUCIR: Programa de catorce pasos de Crosby, 3 de 3 sin operacion")
    crosby = next((f for f in tabla if "catorce pasos" in f["racimo"].lower() or "crosby" in f["racimo"].lower()), None)
    if crosby:
        print(f"  MEDIDO: {crosby['racimo']}: {crosby['sin_operacion']} de {crosby['tamano']} sin operacion -> {crosby['ids_sin_operacion']}")
    else:
        print("  RACIMO NO ENCONTRADO POR NOMBRE, listar todos los nombres de racimo:")
        for f in tabla:
            print(f"    - {f['racimo']}")


if __name__ == "__main__":
    main()
