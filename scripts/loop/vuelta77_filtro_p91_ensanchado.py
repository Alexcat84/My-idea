"""VUELTA 77, TAREA 1.5 (donde escribirlos): ensancha el FILTRO DE
ELEGIBILIDAD P.9.1 para que lea tambien el campo `nodos` de las operaciones
de tipo RENOMBRE_CON_ALIAS, no solo `eliminar` y `superviviente`.

POR QUE. OP-S-09 es RENOMBRE_CON_ALIAS: sus nodos no van en `eliminar` (no
se eliminan, se renombran conservando alias), asi que el filtro de la
vuelta 76 (que solo cruzaba `eliminar` y `superviviente`) no podia verla
nunca aunque su nomina estuviera escrita. Desde la TAREA 1.5 de esta vuelta
OP-S-09.nodos trae 69 ids: el filtro tiene que cruzar tambien ese campo
para las operaciones RENOMBRE_CON_ALIAS, en las dos direcciones (madre o
hijo del candidato).

Expone `condenados_por_operacion(ops)` -> dict nid -> [id_op, ...], y
`caso_positivo()` que verifica con datos SINTETICOS (no tocan el grafo real)
que un candidato cae apartado tanto si la MADRE como si el HIJO estan en
`nodos` de una operacion RENOMBRE_CON_ALIAS no ejecutada.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
OPERACIONES = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"


def condenados_por_operacion(ops):
    """P.9.1 ensanchado: eliminar + superviviente (todas las operaciones NO
    EJECUTADAS) MAS nodos (solo para tipo RENOMBRE_CON_ALIAS, tambien NO
    EJECUTADAS)."""
    condenado_por = {}
    for op in ops:
        if op.get("estado") == "HECHA":
            continue
        for nid in op.get("eliminar") or []:
            condenado_por.setdefault(nid, []).append(op["id_op"])
        if op.get("superviviente"):
            condenado_por.setdefault(op["superviviente"], []).append(op["id_op"])
        if op.get("tipo") == "RENOMBRE_CON_ALIAS":
            for nid in op.get("nodos") or []:
                condenado_por.setdefault(nid, []).append(op["id_op"])
    return condenado_por


def filtrar_candidatos(candidatos, ops):
    """candidatos: lista de dicts con al menos 'madre' e 'hijo'."""
    condenado_por = condenados_por_operacion(ops)
    apartados, limpios = [], []
    for c in candidatos:
        motivos = []
        if c["madre"] in condenado_por:
            motivos.append(f"madre condenada por {condenado_por[c['madre']]}")
        if c["hijo"] in condenado_por:
            motivos.append(f"hijo condenado por {condenado_por[c['hijo']]}")
        if motivos:
            apartados.append((c, motivos))
        else:
            limpios.append(c)
    return limpios, apartados


def caso_positivo():
    """Datos sinteticos, NO el grafo real: prueba las DOS direcciones."""
    ops_sinteticas = [
        {
            "id_op": "OP-TEST-RENOMBRE",
            "tipo": "RENOMBRE_CON_ALIAS",
            "estado": "LISTA",
            "eliminar": [],
            "superviviente": None,
            "nodos": ["id_condenado_como_madre", "id_condenado_como_hijo"],
        },
        {
            "id_op": "OP-TEST-FUSION",
            "tipo": "FUSION",
            "estado": "LISTA",
            "eliminar": ["id_eliminado_clasico"],
            "superviviente": "id_superviviente_clasico",
            "nodos": [],
        },
    ]
    candidatos = [
        {"madre": "id_condenado_como_madre", "hijo": "id_sano_1"},
        {"madre": "id_sano_2", "hijo": "id_condenado_como_hijo"},
        {"madre": "id_sano_3", "hijo": "id_sano_4"},
        {"madre": "id_eliminado_clasico", "hijo": "id_sano_5"},
    ]
    limpios, apartados = filtrar_candidatos(candidatos, ops_sinteticas)

    assert len(apartados) == 3, f"esperaba 3 apartados, dio {len(apartados)}"
    assert len(limpios) == 1, f"esperaba 1 limpio, dio {len(limpios)}"
    assert limpios[0] == {"madre": "id_sano_3", "hijo": "id_sano_4"}

    apartados_por_madre = [a for a in apartados if "madre condenada" in a[1][0]]
    assert any(a[0]["madre"] == "id_condenado_como_madre" for a in apartados_por_madre), \
        "el filtro NO aparto un candidato cuya MADRE esta en nodos de un RENOMBRE_CON_ALIAS"

    apartados_por_hijo = [a for a in apartados if any("hijo condenado" in m for m in a[1])]
    assert any(a[0]["hijo"] == "id_condenado_como_hijo" for a in apartados_por_hijo), \
        "el filtro NO aparto un candidato cuyo HIJO esta en nodos de un RENOMBRE_CON_ALIAS"

    print("CASO POSITIVO OK: RENOMBRE_CON_ALIAS aparta por madre Y por hijo via campo nodos")
    print("CASO POSITIVO OK: FUSION clasica sigue apartando por eliminar (sin romper lo viejo)")


if __name__ == "__main__":
    caso_positivo()

    print()
    ops = [json.loads(l) for l in OPERACIONES.read_text(encoding="utf-8").splitlines() if l.strip()]
    condenado_por = condenados_por_operacion(ops)
    op_s09_nodos = [op for op in ops if op["id_op"] == "OP-S-09"][0].get("nodos") or []
    cubiertos = [nid for nid in op_s09_nodos if nid in condenado_por]
    print(f"OP-S-09.nodos: {len(op_s09_nodos)} ids")
    print(f"De esos, ahora SI aparecen en condenado_por (el filtro los ve): {len(cubiertos)}")
    assert len(cubiertos) == len(op_s09_nodos), "el filtro sigue sin ver algun id de OP-S-09"
    print("CONFIRMADO: el filtro ensanchado ve los 69 ids de OP-S-09 desde esta vuelta.")
