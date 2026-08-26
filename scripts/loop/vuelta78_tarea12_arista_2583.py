"""VUELTA 78, TAREA 1.2: escribe la arista que el tramo 3 (vuelta 77) dejo
sin escribir por una razon FALSA sobre docs/RACIMOS_MIEMBROS.jsonl.

Verificado de nuevo en esta vuelta, por corrida propia, ANTES de escribir
(EJECUTOR.md regla 11, no adivinar):
- mejora_calidad_crosby NO aparece en ninguno de los 32 racimos de
  docs/RACIMOS_MIEMBROS.jsonl (busqueda negativa confirmada sobre
  miembros[].node_id de los 32 registros). Solo el hijo,
  programa_mejora_calidad_14_pasos, esta en el racimo "Programa de catorce
  pasos de Crosby" (quality, 3 miembros: concepto_programa_catorce_pasos,
  programa_mejora_calidad_14_pasos, crosby_programa_14_pasos_introduccion).
- El par TIENE veredicto propio en docs/INTRA_DOMINIO_VEREDICTOS.jsonl,
  puesto_intra 2583, dominio quality, clase D: "mejora_calidad_crosby
  literalmente REMITE al de catorce pasos como su contenido".
- Los dos nodos estan vivos hoy (deprecado=None en ambos) y la arista no
  existe todavia (mejora_calidad_crosby.nodos_siguientes no trae al hijo,
  y el hijo no apunta de vuelta a la madre: cero escalera rota).

Criterio: veredicto del cribado primero (acta 76, repetido en el encargo de
la 77 y de la 78); con D, se escribe (banco 9.6.2, la madre remite al hijo
como su contenido). Adjudicado por el auditor en el acta 77, seccion 3 (D5,
segundo par) y seccion 5 punto 7.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

MADRE = "mejora_calidad_crosby"
HIJO = "programa_mejora_calidad_14_pasos"


def cargar(node_id):
    p = NODOS / f"{node_id}.json"
    with open(p, encoding="utf-8") as f:
        return json.load(f), p


def main():
    racimos = [json.loads(l) for l in open(RAIZ / "docs" / "RACIMOS_MIEMBROS.jsonl", encoding="utf-8") if l.strip()]
    madre_en_racimo = [r.get("nombre") or r.get("id") for r in racimos
                        if MADRE in [m.get("node_id") for m in r.get("miembros", [])]]
    print(f"racimos totales: {len(racimos)}")
    print(f"{MADRE} en racimos: {madre_en_racimo} (esperado: [])")
    assert madre_en_racimo == [], "la madre SI aparece en un racimo, contradice la correccion: PARAR"

    veredicto = None
    with open(RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") as f:
        for l in f:
            if not l.strip():
                continue
            d = json.loads(l)
            if d.get("puesto_intra") == 2583:
                veredicto = d
                break
    print(f"veredicto puesto_intra 2583: clase={veredicto.get('clase')} nodo_a={veredicto.get('nodo_a')} nodo_b={veredicto.get('nodo_b')}")
    assert veredicto is not None, "no hay veredicto 2583: PARAR"
    assert veredicto.get("clase") == "D", "el veredicto no es D: PARAR"
    assert {veredicto.get("nodo_a"), veredicto.get("nodo_b")} == {MADRE, HIJO}, "el veredicto no es de este par: PARAR"

    madre_data, madre_path = cargar(MADRE)
    hijo_data, _ = cargar(HIJO)
    assert not madre_data.get("deprecado"), "madre deprecada: PARAR"
    assert not hijo_data.get("deprecado"), "hijo deprecado: PARAR"

    escalera_rota = MADRE in (hijo_data.get("nodos_siguientes") or [])
    print(f"escalera rota (hijo ya apuntaba a la madre): {escalera_rota}")
    assert not escalera_rota, "ciclo de dos: PARAR"

    sig = madre_data.get("nodos_siguientes") or []
    ya_estaba = HIJO in sig
    print(f"la arista ya existia: {ya_estaba}")
    if not ya_estaba:
        sig.append(HIJO)
        madre_data["nodos_siguientes"] = sig
        with open(madre_path, "w", encoding="utf-8") as f:
            json.dump(madre_data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"ARISTA ESCRITA: {MADRE} -> {HIJO}")
    else:
        print("NADA QUE ESCRIBIR: la arista ya estaba")


if __name__ == "__main__":
    main()
