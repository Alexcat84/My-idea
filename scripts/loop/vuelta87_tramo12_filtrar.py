# -*- coding: utf-8 -*-
"""VUELTA 87, TAREA 3: filtro de elegibilidad P.9.1 ENSANCHADO CON LA VARA DE
LOS A, MAS LA GUARDA DEL PAR NO DIRIGIDO, MAS LA VARA DE LA CADENA, corrido
sobre la bolsa RECALIBRADA FRESCA de esta vuelta
(docs/plan/PASO_NODO_CALIBRADO.jsonl, recorrido con
scripts/plan/paso_contra_nodo_calibrado.py --umbral-titulo 72
--umbral-contencion 0.45 --min-tokens 4, DESPUES de que el grafo se moviera
ocho aristas en la vuelta 86), y LEYENDO EL REGISTRO YA HORNEADO CON EL
TRAMO 11 (TAREA 2.b de esta vuelta, horneado PRE FILTRO propio).

MISMO INSTRUMENTO que scripts/loop/vuelta86_tramo11_filtrar.py, SIN CAMBIOS DE
MAQUINA en el filtro, la guarda del par no dirigido ni la vara de la cadena:
la unidad de lectura son las primeras 30 unidades de la bolsa filtrada SIN
decision registrada en docs/plan/OP_E_01_DECIDIDAS.jsonl (adjudicacion 5.1
del acta 82). Esta vuelta la cabeza sin decidir trae SOLO CUATRO unidades: es
la cola de OP-E-01, no un tramo de treinta (acta 86, adjudicacion 5.8).

TAREA 2.a DE ESTA VUELTA (adjudicacion 5.3 del acta 86), LA UNICA PIEZA NUEVA
DE MAQUINA: al lado de la bolsa filtrada, el filtro imprime cuantas unidades
de la bolsa de HOY (PASO_NODO_CALIBRADO_FILTRADO_V87.jsonl) NO estaban en la
bolsa de la vuelta ANTERIOR (PASO_NODO_CALIBRADO_FILTRADO_V86.jsonl), y las
nombra si son pocas (scripts/loop/vuelta87_unidades_nuevas_recalibracion.py).
No decide nada: es una cifra tallada para que la frase del reporte se pegue
de aqui y no se teclee (EJECUTOR.md regla 1).
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BOLSA = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO.jsonl"
OPERACIONES = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"
VEREDICTOS = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"
REGISTRO = RAIZ / "docs" / "plan" / "OP_E_01_DECIDIDAS.jsonl"
BOLSA_ANTERIOR = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO_FILTRADO_V86.jsonl"
BOLSA_HOY = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO_FILTRADO_V87.jsonl"

sys.path.insert(0, str(RAIZ / "scripts" / "loop"))
from vuelta78_filtro_p91_vara_a import filtrar_candidatos, cargar_vivos  # noqa: E402
from vuelta79_guarda_par_no_dirigido import agrupar_por_par_no_dirigido  # noqa: E402
from vuelta80_vara_cadena import marcar_alcanzables  # noqa: E402
from vuelta86_aviso_paso_vecino import aviso_paso_vecino  # noqa: E402
from vuelta87_unidades_nuevas_recalibracion import unidades_nuevas  # noqa: E402


def unidades_en_orden_de_fichero(limpios):
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


def cargar_decididas():
    decididas = set()
    if not REGISTRO.exists():
        return decididas
    for l in REGISTRO.read_text(encoding="utf-8").splitlines():
        l = l.strip()
        if not l:
            continue
        fila = json.loads(l)
        if fila.get("decision") == "NO SE ENLAZA":
            decididas.add((fila["madre"], fila["hijo"]))
    return decididas


def unidad_decidida(tipo, grupo, decididas):
    return any((f["madre"], f["hijo"]) in decididas for f in grupo)


def aviso_de(f):
    """TAREA 2.d (vuelta 86): aviso del paso vecino, cadena vacia si no hay
    caveat. NO decide nada."""
    r = aviso_paso_vecino(f["madre"], f["hijo"], f.get("paso"), f.get("titulo_ratio"))
    return (" || " + r) if r else ""


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
    print(f"  de esos, SOLO por operacion: {len(apartados_por_op)}")
    print(f"  de esos, con al menos un motivo de la vara de los A: {len(apartados_por_a)}")
    avisos_apartados = 0
    for f, motivos in apartados:
        av = aviso_de(f)
        if av:
            avisos_apartados += 1
    print(f"  TAREA 2.d, apartados con caveat de paso vecino (informativo, no decide): {avisos_apartados}")
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

    with open(BOLSA_HOY, "w", encoding="utf-8") as f:
        for fila in limpios:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")
    print(f"ESCRITO: {BOLSA_HOY.relative_to(RAIZ)} ({len(limpios)} filas, orden de fichero)")

    # TAREA 2.a (adjudicacion 5.3 del acta 86): unidades nuevas por recalibracion.
    if BOLSA_ANTERIOR.exists():
        nuevas, n_hoy, n_ant = unidades_nuevas(BOLSA_HOY, BOLSA_ANTERIOR)
        print()
        print(f"UNIDADES NUEVAS EN LA BOLSA DE HOY QUE NO ESTABAN EN LA BOLSA ANTERIOR "
              f"({BOLSA_ANTERIOR.name}, {n_ant} filas): {len(nuevas)}")
        if 0 < len(nuevas) <= 10:
            for madre, hijo in nuevas:
                print(f"  {madre} -> {hijo}")
    else:
        print()
        print(f"UNIDADES NUEVAS EN LA BOLSA DE HOY: no se puede medir, falta {BOLSA_ANTERIOR.name}")

    decididas = cargar_decididas()
    print()
    print(f"REGISTRO DE DECIDIDAS LEIDO: docs/plan/OP_E_01_DECIDIDAS.jsonl ({len(decididas)} pares NO SE ENLAZA)")

    saltadas = []
    frescas = []
    for pos, tipo, grupo in unidades:
        if unidad_decidida(tipo, grupo, decididas):
            saltadas.append((pos, tipo, grupo))
        else:
            frescas.append((pos, tipo, grupo))
            if len(frescas) == 30:
                break

    print()
    print(f"UNIDADES YA DECIDIDAS EN LA CABEZA, SALTADAS (no se vuelven a leer): {len(saltadas)}")
    for pos, tipo, grupo in saltadas:
        if tipo == "SUELTA":
            f = grupo[0]
            print(f"  {pos}: {f['madre']} -> {f['hijo']} (paso {f['paso']}, dominio {f['dominio']})")
        else:
            desc = " | ".join(f"{f['madre']} -> {f['hijo']} (paso {f['paso']})" for f in grupo)
            print(f"  {pos}: PAREJA: {desc}")

    print()
    print(f"CABEZA DE LA BOLSA FILTRADA, PRIMERAS {len(frescas)} UNIDADES SIN DECISION REGISTRADA,")
    print("en orden de fichero (indice verdadero de la bolsa, no renumerado),")
    print("CON LA VARA DE LA CADENA (alcanzabilidad previa, no aparta por si sola)")
    print("Y CON EL AVISO DEL PASO VECINO (informativo, no decide):")
    candidatos_cabeza = []
    for _, tipo, grupo in frescas:
        candidatos_cabeza.extend({"madre": f["madre"], "hijo": f["hijo"]} for f in grupo)
    alcanzables = marcar_alcanzables(candidatos_cabeza)
    n_alcanzables = 0
    n_avisos_cabeza = 0
    for pos, tipo, grupo in frescas:
        if tipo == "SUELTA":
            f = grupo[0]
            camino = alcanzables.get((f["madre"], f["hijo"]))
            marca = ("YA ALCANZABLE (%d saltos): %s" % (len(camino) - 1, " -> ".join(camino))) if camino else "sin camino previo"
            if camino:
                n_alcanzables += 1
            av = aviso_de(f)
            if av:
                n_avisos_cabeza += 1
            print(f"  {pos}: {f['madre']} -> {f['hijo']} (paso {f['paso']}, dominio {f['dominio']}) | {marca}{av}")
        else:
            desc = " | ".join(f"{f['madre']} -> {f['hijo']} (paso {f['paso']})" for f in grupo)
            print(f"  {pos}: PAREJA: {desc}")
    print()
    print(f"DE LAS {len(frescas)} UNIDADES FRESCAS DE CABEZA, CON CAMINO PREVIO YA ALCANZABLE: {n_alcanzables}")
    print(f"DE LAS {len(frescas)} UNIDADES FRESCAS DE CABEZA, CON CAVEAT DE PASO VECINO: {n_avisos_cabeza}")
    print(f"UNIDADES SIN DECIDIR RESTANTES TRAS ESTA CABEZA: {len(unidades) - len(saltadas) - len(frescas)}")


if __name__ == "__main__":
    main()
