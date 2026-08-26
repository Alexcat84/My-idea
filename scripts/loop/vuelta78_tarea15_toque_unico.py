"""VUELTA 78, TAREA 1.5: el tercer caso de EL TOQUE UNICO (banco 9.4).

Medido por el auditor en la vuelta 77 (acta seccion 5 punto 9): 2 de los 69
ids de la nomina de OP-S-09 (estructura_de_gates, estructura_gates) estan en
el campo eliminar de OP-M-01-FUSION, que corre antes (fase 03_FUSIONES,
orden 5) que OP-S-09 (fase 05_SANEO, orden 8). Verificado de nuevo aqui,
por corrida propia, contra docs/plan/OPERACIONES.jsonl.

Los dos forman por si solos la familia [PARTICULAS]
('estructura_de_gates', 'estructura_gates') de
docs/loop/SALIDA_V77_OP_S09_NOMINA.txt linea 42: al remitir los dos a
OP-M-01-FUSION, la familia entera desaparece de la nomina de OP-S-09 (0
miembros vivos que renombrar: el toque unico ya los resuelve la fusion).

Re-mide la nomina de 69 quitando los 2 ids remitidos, sin volver a correr el
barrido lexico completo (el metodo no cambia, solo se resta el toque
unico ya adjudicado).
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
OPS_PATH = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"

TOQUE_UNICO = {"estructura_de_gates", "estructura_gates"}


def cargar_ops():
    ops = []
    with open(OPS_PATH, encoding="utf-8") as f:
        for l in f:
            if l.strip():
                ops.append(json.loads(l))
    return ops


def main():
    ops = cargar_ops()
    by_id = {o["id_op"]: o for o in ops}
    fusion = by_id["OP-M-01-FUSION"]
    s09 = by_id["OP-S-09"]

    overlap = set(fusion.get("eliminar") or []) & set(s09.get("nodos") or [])
    print(f"OP-M-01-FUSION orden={fusion.get('orden')} fase={fusion.get('fase')}")
    print(f"OP-S-09 orden={s09.get('orden')} fase={s09.get('fase')}")
    print(f"overlap eliminar x nodos: {sorted(overlap)}")
    assert overlap == TOQUE_UNICO, f"el overlap no coincide con lo adjudicado: {overlap}"
    assert fusion["orden"] < s09["orden"], "OP-M-01-FUSION no corre antes: PARAR"

    nomina_vieja = s09.get("nodos") or []
    assert len(nomina_vieja) == 69, f"la nomina no tiene 69, tiene {len(nomina_vieja)}"
    nomina_nueva = [n for n in nomina_vieja if n not in TOQUE_UNICO]
    print(f"nomina antes del toque unico: {len(nomina_vieja)}")
    print(f"nomina despues de remitir el toque unico a OP-M-01-FUSION: {len(nomina_nueva)}")

    familias_afectadas = TOQUE_UNICO <= set(nomina_vieja)
    print(f"los dos ids estaban en la nomina vieja: {familias_afectadas}")
    print("familia [PARTICULAS] (estructura_de_gates, estructura_gates) desaparece entera: "
          "0 de sus 2 miembros quedan en OP-S-09 tras el toque unico")

    print(f"NOMINA_NUEVA_JSON_START")
    print(json.dumps(nomina_nueva, ensure_ascii=False))
    print(f"NOMINA_NUEVA_JSON_END")
    print(f"familias: 28 (29 menos la familia [PARTICULAS] de los dos remitidos, entera)")
    print(f"nodos vivos en familia: {len(nomina_nueva)} (69 menos los 2 remitidos)")


if __name__ == "__main__":
    main()
