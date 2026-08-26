# -*- coding: utf-8 -*-
"""VUELTA 79, TAREA 5 punto 2: filtro de elegibilidad P.9.1 ENSANCHADO CON LA
VARA DE LOS A, MAS LA GUARDA DEL PAR NO DIRIGIDO (TAREA 4), corrido ANTES de
leer nada, sobre la bolsa RECALIBRADA FRESCA de esta vuelta
(docs/plan/PASO_NODO_CALIBRADO.jsonl, recorrido con
scripts/plan/paso_contra_nodo_calibrado.py --umbral-titulo 72
--umbral-contencion 0.45 --min-tokens 4, salida en
docs/loop/SALIDA_V79_CALIBRADO_FRESCO.txt). Reusa
scripts/loop/vuelta78_filtro_p91_vara_a.py (eliminar + superviviente + nodos
de RENOMBRE_CON_ALIAS, mas veredictos A vivos) y anade
scripts/loop/vuelta79_guarda_par_no_dirigido.py (agrupa por par no dirigido
ANTES de definir el orden de lectura).
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BOLSA = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO.jsonl"
OPERACIONES = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"
VEREDICTOS = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"

sys.path.insert(0, str(RAIZ / "scripts" / "loop"))
from vuelta78_filtro_p91_vara_a import filtrar_candidatos, cargar_vivos  # noqa: E402
from vuelta79_guarda_par_no_dirigido import agrupar_por_par_no_dirigido  # noqa: E402


def unidades_en_orden_de_fichero(limpios):
    """Agrupa LIMPIOS (ya en orden de fichero) en UNIDADES DE LECTURA: una
    pareja (2 filas, mismo par, direcciones distintas) cuenta como UNA
    unidad, ubicada en la posicion de la fila que aparece PRIMERO en el
    fichero; una fila suelta es su propia unidad."""
    parejas, sueltas = agrupar_por_par_no_dirigido(limpios)
    pos = {id(f): i for i, f in enumerate(limpios)}
    unidades = []
    for grupo in parejas:
        primera_pos = min(pos[id(f)] for f in grupo)
        unidades.append((primera_pos, "PAREJA", grupo))
    for f in sueltas:
        unidades.append((pos[id(f)], "SUELTA", [f]))
    unidades.sort(key=lambda u: u[0])
    return unidades


def main():
    filas = [json.loads(l) for l in BOLSA.read_text(encoding="utf-8").splitlines() if l.strip()]
    sin_arista = [f for f in filas if not f["arista"]]
    print(f"BOLSA REDUCIDA TOTAL: {len(filas)}")
    print(f"SIN ARISTA (candidatos): {len(sin_arista)}")

    ops = [json.loads(l) for l in OPERACIONES.read_text(encoding="utf-8").splitlines() if l.strip()]
    veredictos = [json.loads(l) for l in VEREDICTOS.read_text(encoding="utf-8").splitlines() if l.strip()]
    vivos = cargar_vivos()

    candidatos = [{"madre": f["madre"], "hijo": f["hijo"]} for f in sin_arista]
    limpios_c, apartados_c = filtrar_candidatos(candidatos, ops, veredictos, vivos)
    apartado_keys = {(c["madre"], c["hijo"]): motivos for c, motivos in apartados_c}

    apartados = [(f, apartado_keys[(f["madre"], f["hijo"])]) for f in sin_arista
                 if (f["madre"], f["hijo"]) in apartado_keys]
    limpios = [f for f in sin_arista if (f["madre"], f["hijo"]) not in apartado_keys]

    apartados_por_op = [f for f, m in apartados if any("operacion" in x for x in m) and not any("veredicto A" in x for x in m)]
    apartados_por_a = [f for f, m in apartados if any("veredicto A" in x for x in m)]

    print(f"APARTADOS POR P.9.1 ENSANCHADO (operaciones + vara de los A): {len(apartados)}")
    print(f"  de esos, SOLO por operacion (eliminar/superviviente/nodos): {len(apartados_por_op)}")
    print(f"  de esos, con al menos un motivo de la vara de los A: {len(apartados_por_a)}")
    print(f"LIMPIOS TRAS P.9.1 ENSANCHADO (antes de la guarda del par no dirigido): {len(limpios)}")

    unidades = unidades_en_orden_de_fichero(limpios)
    parejas = [u for u in unidades if u[1] == "PAREJA"]
    sueltas = [u for u in unidades if u[1] == "SUELTA"]
    print()
    print(f"GUARDA DEL PAR NO DIRIGIDO: {len(parejas)} pareja(s) detectada(s) (mismo par, dos direcciones)")
    for _, _, grupo in parejas:
        print(f"  PAREJA: {[(f['madre'], '->', f['hijo'], 'paso', f['paso']) for f in grupo]}")
    print(f"CANDIDATOS (unidades de lectura) TRAS LA GUARDA: {len(unidades)} "
          f"({len(parejas)} parejas + {len(sueltas)} sueltas, de {len(limpios)} filas)")

    salida = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO_FILTRADO_V79.jsonl"
    with open(salida, "w", encoding="utf-8") as f:
        for fila in limpios:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")
    print(f"ESCRITO: {salida.relative_to(RAIZ)} ({len(limpios)} filas, orden de fichero)")

    print()
    print("CABEZA DE LA BOLSA FILTRADA, primeras 30 UNIDADES, en orden de fichero:")
    for i, (_, tipo, grupo) in enumerate(unidades[:30]):
        if tipo == "SUELTA":
            f = grupo[0]
            print(f"  {i}: {f['madre']} -> {f['hijo']} (paso {f['paso']}, dominio {f['dominio']})")
        else:
            desc = " | ".join(f"{f['madre']} -> {f['hijo']} (paso {f['paso']})" for f in grupo)
            print(f"  {i}: PAREJA: {desc}")


if __name__ == "__main__":
    main()
