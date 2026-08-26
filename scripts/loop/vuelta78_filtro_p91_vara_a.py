"""VUELTA 78, TAREA 3.1: ensancha el FILTRO DE ELEGIBILIDAD P.9.1 (ya
ensanchado en la vuelta 77 con el campo `nodos` de RENOMBRE_CON_ALIAS, en
scripts/loop/vuelta77_filtro_p91_ensanchado.py) con LA VARA DE LOS
VEREDICTOS A: aparta tambien el candidato cuyo extremo (madre o hijo)
participe en un veredicto clase A VIVO del cribado (docs/INTRA_DOMINIO_VEREDICTOS.jsonl),
tenga o no operacion escrita.

ADJUDICADO POR CITA por el auditor en el acta 77 (seccion 3, D4, y seccion
5 punto 5), sin doctrina nueva: P.9 punto 1 ("los enlaces corren DESPUES de
las fusiones que tocan sus destinos"), P.9 punto 2 (el id escrito es el que
estara vivo), y AUDITOR.md seccion 0 punto 3 (INTRA_DOMINIO_VEREDICTOS.jsonl
es fuente de verdad). Un veredicto A es una fusion que el plan aun no ha
citado con una operacion.

"VIVO" para esta vara: los DOS nodos del par A estan vivos hoy
(deprecado != True) en dataset/metadata/master_graph.json. Si uno de los
dos ya esta deprecado, el A ya fue resuelto por otra via y no aparta nada.

NO rompe lo que ya aparta (eliminar, superviviente, nodos de
RENOMBRE_CON_ALIAS): importa y reusa condenados_por_operacion() de la
vuelta 77 sin tocarla, y le suma un segundo mapa, condenados_por_veredicto_a().
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
OPERACIONES = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"
VEREDICTOS = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"

sys.path.insert(0, str(RAIZ / "scripts" / "loop"))
from vuelta77_filtro_p91_ensanchado import condenados_por_operacion  # noqa: E402


def cargar_vivos():
    g = json.load(open(GRAFO, encoding="utf-8"))["nodos"]
    return {nid for nid, n in g.items() if not n.get("deprecado")}


def condenados_por_veredicto_a(veredictos, vivos):
    """nid -> lista de (puesto_intra, el_otro_nodo) para cada A vivo en que participa."""
    condenado_por = {}
    for v in veredictos:
        if v.get("clase") != "A":
            continue
        a, b = v.get("nodo_a"), v.get("nodo_b")
        if a not in vivos or b not in vivos:
            continue
        condenado_por.setdefault(a, []).append((v["puesto_intra"], b))
        condenado_por.setdefault(b, []).append((v["puesto_intra"], a))
    return condenado_por


def filtrar_candidatos(candidatos, ops, veredictos, vivos):
    """candidatos: lista de dicts con al menos 'madre' e 'hijo'.
    Filtro P.9.1 ensanchado dos veces: operaciones (vuelta 77) + veredictos A vivos (vuelta 78)."""
    condenado_por_op = condenados_por_operacion(ops)
    condenado_por_a = condenados_por_veredicto_a(veredictos, vivos)
    apartados, limpios = [], []
    for c in candidatos:
        motivos = []
        if c["madre"] in condenado_por_op:
            motivos.append(f"madre condenada por operacion {condenado_por_op[c['madre']]}")
        if c["hijo"] in condenado_por_op:
            motivos.append(f"hijo condenado por operacion {condenado_por_op[c['hijo']]}")
        if c["madre"] in condenado_por_a:
            motivos.append(f"madre en veredicto A vivo {condenado_por_a[c['madre']]}")
        if c["hijo"] in condenado_por_a:
            motivos.append(f"hijo en veredicto A vivo {condenado_por_a[c['hijo']]}")
        if motivos:
            apartados.append((c, motivos))
        else:
            limpios.append(c)
    return limpios, apartados


def caso_positivo():
    """Datos SINTETICOS, no tocan el grafo real. Prueba las dos direcciones
    (madre y hijo) de la vara de los A, sin romper el caso de operaciones."""
    ops_sinteticas = [
        {"id_op": "OP-TEST-FUSION", "tipo": "FUSION", "estado": "LISTA",
         "eliminar": ["id_eliminado_clasico"], "superviviente": "id_superviviente_clasico", "nodos": []},
    ]
    veredictos_sinteticos = [
        {"puesto_intra": 90001, "nodo_a": "id_condenado_a_como_madre", "nodo_b": "id_companero_vivo_1", "clase": "A"},
        {"puesto_intra": 90002, "nodo_a": "id_companero_vivo_2", "nodo_b": "id_condenado_a_como_hijo", "clase": "A"},
        {"puesto_intra": 90003, "nodo_a": "id_deprecado_en_a", "nodo_b": "id_sano_6", "clase": "A"},
    ]
    vivos_sinteticos = {
        "id_condenado_a_como_madre", "id_companero_vivo_1", "id_companero_vivo_2",
        "id_condenado_a_como_hijo", "id_sano_6",
        "id_sano_3", "id_sano_4", "id_eliminado_clasico", "id_sano_5",
        # "id_deprecado_en_a" NO esta en vivos: su A no debe apartar nada
    }
    candidatos = [
        {"madre": "id_condenado_a_como_madre", "hijo": "id_sano_1"},
        {"madre": "id_sano_2", "hijo": "id_condenado_a_como_hijo"},
        {"madre": "id_sano_3", "hijo": "id_sano_4"},
        {"madre": "id_eliminado_clasico", "hijo": "id_sano_5"},
        {"madre": "id_deprecado_en_a", "hijo": "id_sano_6"},
    ]
    limpios, apartados = filtrar_candidatos(candidatos, ops_sinteticas, veredictos_sinteticos, vivos_sinteticos)

    assert len(apartados) == 3, f"esperaba 3 apartados, dio {len(apartados)}"
    assert len(limpios) == 2, f"esperaba 2 limpios, dio {len(limpios)}"
    limpios_set = {(c["madre"], c["hijo"]) for c in limpios}
    assert ("id_sano_3", "id_sano_4") in limpios_set
    assert ("id_deprecado_en_a", "id_sano_6") in limpios_set, \
        "el par cuyo A tiene un extremo DEPRECADO no deberia apartarse, y se aparto"

    apartados_por_madre_a = [a for a in apartados if any("madre en veredicto A" in m for m in a[1])]
    assert any(a[0]["madre"] == "id_condenado_a_como_madre" for a in apartados_por_madre_a), \
        "el filtro NO aparto un candidato cuya MADRE participa en un A vivo"

    apartados_por_hijo_a = [a for a in apartados if any("hijo en veredicto A" in m for m in a[1])]
    assert any(a[0]["hijo"] == "id_condenado_a_como_hijo" for a in apartados_por_hijo_a), \
        "el filtro NO aparto un candidato cuyo HIJO participa en un A vivo"

    apartados_por_op = [a for a in apartados if any("condenada por operacion" in m or "condenado por operacion" in m for m in a[1])]
    assert any(a[0]["madre"] == "id_eliminado_clasico" for a in apartados_por_op), \
        "el caso clasico de FUSION dejo de apartar: se rompio lo viejo"

    print("CASO POSITIVO OK: la vara de los A aparta por madre Y por hijo, en las dos direcciones")
    print("CASO POSITIVO OK: un A con un extremo DEPRECADO no aparta nada (ya resuelto por otra via)")
    print("CASO POSITIVO OK: el caso clasico de FUSION (eliminar/superviviente) sigue apartando igual")


if __name__ == "__main__":
    caso_positivo()
    print()

    ops = [json.loads(l) for l in OPERACIONES.read_text(encoding="utf-8").splitlines() if l.strip()]
    veredictos = [json.loads(l) for l in VEREDICTOS.read_text(encoding="utf-8").splitlines() if l.strip()]
    vivos = cargar_vivos()

    a_totales = sum(1 for v in veredictos if v.get("clase") == "A")
    condenado_por_a = condenados_por_veredicto_a(veredictos, vivos)
    print(f"veredictos clase A en el archivo: {a_totales}")
    print(f"nodos VIVOS que participan en al menos un A con otro nodo VIVO: {len(condenado_por_a)}")
