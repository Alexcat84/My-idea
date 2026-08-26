"""VUELTA 76, TAREA 2.3.c: imprime, para los primeros 30 pares de
docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V76.jsonl (bolsa ya filtrada por
P.9.1, orden de archivo, sin sorteo), los textos completos de madre e hijo
para la lectura par a par (9.6.1 y 9.6.2)."""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BOLSA = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO_FILTRADO_V76.jsonl"
NODOS = RAIZ / "dataset" / "nodos"


def cargar(node_id):
    with open(NODOS / f"{node_id}.json", encoding="utf-8") as f:
        return json.load(f)


def main():
    filas = [json.loads(l) for l in BOLSA.read_text(encoding="utf-8").splitlines() if l.strip()][:30]
    for i, fila in enumerate(filas):
        madre = cargar(fila["madre"])
        hijo = cargar(fila["hijo"])
        print("=" * 100)
        print(f"PAR {i}: {fila['madre']} -> {fila['hijo']}  (paso {fila['paso']}, dominio {fila['dominio']})")
        print(f"MADRE titulo: {madre['titulo_concepto']}  | fuente: {madre.get('fuente')}")
        print(f"  paso senalado ({fila['paso']}): {fila['texto_paso']}")
        print("  TODOS LOS PASOS DE LA MADRE:")
        for j, p in enumerate(madre.get("pasos_accionables") or []):
            print(f"    [{j+1}] {p}")
        print(f"  nodos_siguientes actuales de la madre ({len(madre.get('nodos_siguientes') or [])}): {madre.get('nodos_siguientes')}")
        print()
        print(f"HIJO titulo: {hijo['titulo_concepto']}  | fuente: {hijo.get('fuente')}")
        print(f"  resumen: {hijo.get('resumen_teorico')}")
        print("  PASOS DEL HIJO:")
        for j, p in enumerate(hijo.get("pasos_accionables") or []):
            print(f"    [{j+1}] {p}")
        print(f"  nodos_previos actuales del hijo: {hijo.get('nodos_previos')}")
        print()


if __name__ == "__main__":
    main()
