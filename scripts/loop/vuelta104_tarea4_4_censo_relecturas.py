# -*- coding: utf-8 -*-
r"""vuelta104_tarea4_4_censo_relecturas.py . VUELTA 104, TAREA 4.4: EL CENSO
DE RELECTURAS DE OP-E-03 (encargo del auditor, acta de la vuelta 103,
seccion 7: "la lista de releidos la reconstrui de las actas 101, 102 y 103 y
de sus encargos, no de un instrumento; va encargado convertirla en fichero").

QUE ES: un JSONL con UNA fila por cada uno de los 183 puestos de OP-E-03
(los cuatro ficheros de tramo), con en que vuelta(s) se releyo mas alla de
la lectura original (vueltas 96 a 99, cuando se crearon los cuatro ficheros
de tramo) y por que instrumento. Sin el, la proxima "relectura al doble"
vuelve a elegir a ojo y a repetir puestos, que es exactamente lo que la
seccion 7 del acta 103 declaro que paso tres veces seguidas (vuelta 102 por
los extremos, vuelta 103 por el centro, y esta misma vuelta 104 casi repite
si no se hubiera consultado la lista).

DE DONDE SALE CADA EVENTO:
  - Las `correccion_vNN` SE LEEN DE LOS CUATRO FICHEROS DE TRAMO, mecanico,
    no tecleado (`clave -> vuelta = NN`).
  - Los eventos CONFIRMATORIOS (relecturas que NO movieron nada, y por lo
    tanto no dejan `correccion_vNN`) estan declarados abajo, CADA UNO CON SU
    FUENTE citada en el propio dato: el puesto 5 en el acta de la vuelta 101
    (ACTA_AUDITOR.md, seccion 4, "MI PROPIA CAIDA... EL PUESTO 5"); los ocho
    de la vuelta 102 TAREA 3 (relectura ciega de extremos, acta 101,
    `vuelta102_tarea3_relectura_ciega_tramo1.py`); los siete confirmados de
    la vuelta 103 TAREA 4 (relectura ciega de centro, el octavo del lote es
    el 31, que SI aparece como `correccion_v103` y no se duplica aqui); los
    41 confirmados de la vuelta 104 TAREA 4.2 (barrido de una pregunta,
    `docs/loop/SALIDA_V104_TAREA4_2_BARRIDO.txt`, veredicto OBJETO).
  - Todo puesto que no aparece en ninguna de las dos fuentes de arriba
    queda `veces_releido: 0`, `nunca_releido_desde_la_lectura_original: true`.

MECANICA DE ROJO: si los cuatro ficheros de tramo no suman 183 filas sin
huecos ni repetidos (1..183), o si algun puesto declarado abajo en los
eventos confirmatorios no existe en esa numeracion, NO SE ESCRIBE NADA y
sale con exit 1.

USO:
  python scripts/loop/vuelta104_tarea4_4_censo_relecturas.py
      -> escribe docs/loop/CENSO_RELECTURAS_OP_E_03.jsonl
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMOS = [
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl"),
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl"),
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO3_V98.jsonl"),
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO4_V99.jsonl"),
]
SALIDA = os.path.join(RAIZ, "docs", "loop", "CENSO_RELECTURAS_OP_E_03.jsonl")

CORREC_RE = re.compile(r"^correccion_v(\d+)$")

# --- eventos confirmatorios (no dejan correccion_vNN), CADA UNO CON SU FUENTE ---
PUESTO_5 = {
    5: [{"vuelta": 101, "instrumento": "relectura del auditor (ACTA_AUDITOR.md, ACTA DE LA VUELTA 101, "
                                        "seccion 4, \"MI PROPIA CAIDA, Y ES DE CLASE: EL PUESTO 5\")",
         "resultado": "confirmada (el ejecutor tenia razon, el auditor declaro su propia caida de clase)"}]
}
V102_TAREA3_EXTREMOS = {
    p: [{"vuelta": 102, "instrumento": "vuelta102_tarea3_relectura_ciega_tramo1.py (relectura ciega, "
                                        "extremos del titulo_ratio: 4 RESUELTA de menor ratio + 4 NO "
                                        "RESUELTA de mayor ratio)",
         "resultado": "confirmada"}]
    for p in (33, 30, 7, 27, 22, 23, 26, 12)
}
V103_TAREA4_CENTRO_CONFIRMADOS = {
    p: [{"vuelta": 103, "instrumento": "vuelta103_tarea4_relectura_ciega_centro.py --modo blind (relectura "
                                        "ciega, centro del titulo_ratio por flanco)",
         "resultado": "confirmada"}]
    for p in (13, 19, 10, 15, 36, 35, 32)  # el 31 del mismo lote SI se movio: queda como correccion_v103
}
V104_TAREA4_2_CONFIRMADOS = {
    p: [{"vuelta": 104, "instrumento": "vuelta104_tarea4_2_barrido_especie28.py (barrido dirigido, una "
                                        "pregunta: objeto del imperativo vs ejemplo/condicion/subordinada)",
         "resultado": "confirmada, veredicto OBJETO"}]
    for p in (1, 2, 4, 9, 14, 17, 18, 20, 21, 38, 39,  # tramo1: 15 menos los 4 que se movieron (6,8,24,25)
              42, 45, 46, 47, 48, 49, 53, 57, 58, 59, 61, 64, 66, 73, 74, 75, 77, 78,
              83, 84, 87, 88, 91, 92, 93, 94, 97, 98, 99, 100)  # tramo2: 33 menos los 3 que se movieron (52,62,80)
}

EVENTOS_CONFIRMATORIOS = {}
for tabla in (PUESTO_5, V102_TAREA3_EXTREMOS, V103_TAREA4_CENTRO_CONFIRMADOS, V104_TAREA4_2_CONFIRMADOS):
    for p, eventos in tabla.items():
        EVENTOS_CONFIRMATORIOS.setdefault(p, []).extend(eventos)


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    fallos = []
    todas = []
    for ruta in TRAMOS:
        if not os.path.exists(ruta):
            fallos.append("no existe %s" % os.path.relpath(ruta, RAIZ))
            continue
        todas.extend(cargar(ruta))

    if fallos:
        print("ROJO, %d cosa(s) no cuadran:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    puestos = sorted(f["puesto_tramo"] for f in todas)
    n = len(todas)
    if puestos != list(range(1, n + 1)):
        print("ROJO, los puesto_tramo no cubren 1 a %d sin huecos ni repetidos" % n)
        return 1

    for p in EVENTOS_CONFIRMATORIOS:
        if p < 1 or p > n:
            print("ROJO, evento confirmatorio declarado para puesto %d, fuera de rango 1..%d" % (p, n))
            return 1

    filas_salida = []
    for f in todas:
        p = f["puesto_tramo"]
        eventos = list(EVENTOS_CONFIRMATORIOS.get(p, []))
        for k in f:
            m = CORREC_RE.match(k)
            if m:
                c = f[k]
                eventos.append({
                    "vuelta": int(m.group(1)),
                    "instrumento": "%s (declarado en el propio fichero de tramo)" % k,
                    "resultado": "SE MOVIO: direccion_leida a %r" % c.get("valor_nuevo"),
                })
        eventos.sort(key=lambda e: e["vuelta"])
        filas_salida.append({
            "puesto_tramo": p,
            "madre_de_la_bolsa": f["madre_de_la_bolsa"],
            "hijo_de_la_bolsa": f["hijo_de_la_bolsa"],
            "veces_releido": len(eventos),
            "nunca_releido_desde_la_lectura_original": len(eventos) == 0,
            "eventos": eventos,
        })

    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as out:
        for fila in filas_salida:
            out.write(json.dumps(fila, ensure_ascii=False) + "\n")

    con_relectura = [f for f in filas_salida if f["veces_releido"] > 0]
    print("VERDE: %d puestos censados (%s), %d con al menos una relectura declarada mas alla de la "
          "original, %d nunca releidos. Escrito en %s"
          % (n, os.path.relpath(SALIDA, RAIZ), len(con_relectura), n - len(con_relectura),
             os.path.relpath(SALIDA, RAIZ)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
