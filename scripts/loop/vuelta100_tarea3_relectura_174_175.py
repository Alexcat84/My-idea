# -*- coding: utf-8 -*-
r"""vuelta100_tarea3_relectura_174_175.py . VUELTA 100, TAREA 3: LAS DOS
RELECTURAS CONJUNTAS del encargo de la vuelta 99 (acta 99, TAREA 3, puntos
3.1 y 3.2), sobre los pares 175 y 174 de OP-E-03.

EL JUICIO, LEIDO HOY CONTRA EL GRAFO (dataset/nodos/*.json), no supuesto:

PAR 175 (`validar_modelo_financiero` -> `valor_de_vida_del_cliente`, paso 2).
El paso 2 de la madre es "Calcular costos de adquisicion de clientes, tasas
de conversion y Customer Lifetime Value (LTV)": un paso de CALCULO. El hijo
tiene CUATRO pasos y SOLO EL PRIMERO calcula ("Calcular el LTV actual de los
clientes"); el segundo monitorea, y el tercero y el cuarto son INTERVENCION
OPERATIVA ("Implementar nuevos programas y ofertas que incrementen el LTV",
"Mejorar la eficiencia de los procesos de retencion y crecimiento"). Subir
el LTV no es un sub-paso de calcularlo. El test del 9.6.2 falla POR EXCESO
DE GENERO: el nombre literal "Customer Lifetime Value" en el paso 2 es real,
pero el 9.6.2 dice EXPRESAMENTE que la prueba lexica no sirve (34 de 46
marcados por vocabulario, 3% de precision).

PAR 174 (`desarrollo_value_proposition_usp` -> `posicionamiento_vs_competidores`,
paso 1). El paso 1 de la madre es "Identificar que hace unico al negocio
frente a competidores directos": analisis interno. Los CUATRO pasos del
hijo son movimientos de una CONVERSACION DE VENTA con un candidato a
franquiciado (preguntar que otras franquicias considera, comparar, responder
destacando diferencias, redirigir si el competidor es de otra industria), y
su propio entregable lo dice: "listo para usar en cualquier conversacion con
un candidato". El hijo no IDENTIFICA lo que hace unico al negocio: PRESUPONE
que ya esta identificado y lo despliega contra un prospecto. Es el mismo
patron que el propio ejecutor nombro CASADO POR OBJETO Y NO POR ACCION (par
163 de este mismo tramo: "los dos hablan de X, pero la madre distingue Y y
el hijo distingue Z").

EN LAS DOS: SE SOSTIENE EL CASO DEL AUDITOR. Los dos pares pasan de
DIRECCION AFIRMADA a NO RESUELTA. La clase D no cambia (banco 9.6.1 rama
contenido, tercera fila del 9.22: CONTINUA). AUDITOR.md 1.3: la decision es
del ejecutor, no de la lectura ciega; esta es esa decision, con su caso
escrito.

MECANICA DE ROJO, y no escribe nada si salta: (i) TRAMO4_V99.jsonl no trae
exactamente 33 filas; (ii) el conteo de partida (direccion afirmada/NO
RESUELTA del tramo) no reproduce EXACTO 13/20 (60,6%), la cifra publicada en
docs/plan/04_ENLACES.md:417; (iii) las filas 174 o 175 no existen, no tienen
`direccion_leida` puesta, o ya traen un `correccion_v100`; (iv) los nodos
citados no existen en dataset/nodos/.

USO:
  python scripts/loop/vuelta100_tarea3_relectura_174_175.py --simular
  python scripts/loop/vuelta100_tarea3_relectura_174_175.py --aplicar
"""
import argparse
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMO4 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO4_V99.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

BASE_TOTAL = 33
BASE_AFIRMADA = 13
BASE_NO_RESUELTA = 20

CORRECCIONES = {
    174: {
        "campo_corregido": "direccion_leida",
        "valor_anterior": "desarrollo_value_proposition_usp -> posicionamiento_vs_competidores",
        "valor_nuevo": None,
        "cita_corregida": "banco 9.6.2 (test de reconocimiento: el hijo cabe entero dentro de UN "
                           "paso de la madre; la prueba lexica no sirve, 34/46 marcados por "
                           "vocabulario, 3% de precision), no el nombre literal del paso",
        "razon": (
            "CORRECCION DECLARADA (vuelta 100, TAREA 3, relectura conjunta con el auditor, "
            "encargo de la vuelta 99 seccion 3.2, discutible fuera de lo marcado por el "
            "ejecutor). El texto viejo de razon y direccion_leida NO SE BORRA. Leidos hoy "
            "dataset/nodos/desarrollo_value_proposition_usp.json y "
            "dataset/nodos/posicionamiento_vs_competidores.json: el paso 1 de la madre es "
            "'Identificar que hace unico al negocio frente a competidores directos' (analisis "
            "interno). Los CUATRO pasos del hijo son movimientos de una CONVERSACION DE VENTA "
            "con un candidato a franquiciado (preguntar que otras franquicias considera, "
            "comparar en detalle, responder destacando diferencias incluyendo desventajas "
            "propias, redirigir si el competidor es de otra industria), y su propio entregable "
            "lo declara: 'listo para usar en cualquier conversacion con un candidato'. TRES de "
            "los cuatro pasos son movimientos que el paso 1 de la madre no contempla: el hijo "
            "no IDENTIFICA lo que hace unico al negocio, PRESUPONE que ya esta identificado y "
            "lo despliega contra las objeciones de un prospecto. La razon original concede el "
            "punto sin verlo ('la conversacion APLICADA de ese analisis'): aplicar un analisis "
            "en una venta no es ejecutar el analisis, es el mismo patron que el propio "
            "ejecutor nombro CASADO POR OBJETO Y NO POR ACCION (par 163 de este mismo tramo). "
            "SE SOSTIENE EL CASO DEL AUDITOR: el par 174 pasa de DIRECCION AFIRMADA a NO "
            "RESUELTA. Clase D no cambia (banco 9.6.1 rama contenido, tercera fila del 9.22: "
            "CONTINUA)."
        ),
    },
    175: {
        "campo_corregido": "direccion_leida",
        "valor_anterior": "validar_modelo_financiero -> valor_de_vida_del_cliente",
        "valor_nuevo": None,
        "cita_corregida": "banco 9.6.2 (test de reconocimiento: el hijo cabe entero dentro de "
                           "UN paso de la madre), no la coincidencia lexica del termino "
                           "'Customer Lifetime Value'",
        "razon": (
            "CORRECCION DECLARADA (vuelta 100, TAREA 3, relectura conjunta con el auditor, "
            "encargo de la vuelta 99 seccion 3.1, discutible marcado 4 del acta 99). El texto "
            "viejo de razon y direccion_leida NO SE BORRA. Leidos hoy "
            "dataset/nodos/validar_modelo_financiero.json y "
            "dataset/nodos/valor_de_vida_del_cliente.json: el paso 2 de la madre es 'Calcular "
            "costos de adquisicion de clientes, tasas de conversion y Customer Lifetime Value "
            "(LTV)', un paso de CALCULO. El hijo tiene CUATRO pasos y SOLO EL PRIMERO calcula "
            "('Calcular el LTV actual de los clientes'); el segundo monitorea, y el tercero y "
            "el cuarto son INTERVENCION OPERATIVA ('Implementar nuevos programas y ofertas que "
            "incrementen el LTV', 'Mejorar la eficiencia de los procesos de retencion y "
            "crecimiento'). Subir el LTV con programas nuevos no es un sub-paso de calcularlo: "
            "es otra actividad que el paso 2 de la madre no contempla; la madre no interviene "
            "sobre nada en ningun paso, solo mide y proyecta hasta el P&L. El test del 9.6.2 "
            "falla POR EXCESO DE GENERO: el nombre literal 'Customer Lifetime Value' en el "
            "paso 2 es real, pero el 9.6.2 dice EXPRESAMENTE que la prueba lexica no sirve (34 "
            "de 46 marcados por vocabulario y solo 1 lo era, 3% de precision): coincidir el "
            "termino no es caber dentro del paso. SE SOSTIENE EL CASO DEL AUDITOR: el par 175 "
            "pasa de DIRECCION AFIRMADA a NO RESUELTA. Clase D no cambia (banco 9.6.1 rama "
            "contenido, tercera fila del 9.22: CONTINUA)."
        ),
    },
}

NODOS_CITADOS = [
    "desarrollo_value_proposition_usp", "posicionamiento_vs_competidores",
    "validar_modelo_financiero", "valor_de_vida_del_cliente",
]

VUELTA = 100


def cargar():
    with io.open(TRAMO4, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--simular", action="store_true")
    g.add_argument("--aplicar", action="store_true")
    a = ap.parse_args()

    fallos = []
    for n in NODOS_CITADOS:
        if not os.path.exists(os.path.join(NODOS, n + ".json")):
            fallos.append("no existe dataset/nodos/%s.json" % n)

    filas = cargar()
    if len(filas) != BASE_TOTAL:
        fallos.append("%s trae %d filas, se esperaban %d"
                      % (os.path.basename(TRAMO4), len(filas), BASE_TOTAL))

    afirmada_antes = sum(1 for f in filas if f.get("direccion_leida"))
    no_resuelta_antes = len(filas) - afirmada_antes
    if afirmada_antes != BASE_AFIRMADA or no_resuelta_antes != BASE_NO_RESUELTA:
        fallos.append("conteo de partida da afirmada=%d no_resuelta=%d, se esperaba %d/%d "
                      "(04_ENLACES.md:417)" % (afirmada_antes, no_resuelta_antes,
                                                BASE_AFIRMADA, BASE_NO_RESUELTA))

    objetivo = {}
    for p in (174, 175):
        fila = next((f for f in filas if f.get("puesto_tramo") == p), None)
        if fila is None:
            fallos.append("no existe la fila puesto_tramo=%d" % p)
            continue
        if not fila.get("direccion_leida"):
            fallos.append("la fila %d ya esta sin direccion_leida" % p)
        if "correccion_v100" in fila:
            fallos.append("la fila %d ya trae correccion_v100" % p)
        objetivo[p] = fila

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("=" * 100)
    print("RELECTURA CONJUNTA DE LOS PARES 174 Y 175 (vuelta 100, TAREA 3, %s)"
          % ("SIMULACION" if a.simular else "APLICADO"))
    print("=" * 100)
    print("ANTES: direccion afirmada %d, NO RESUELTA %d, total %d (%.1f%%)"
          % (afirmada_antes, no_resuelta_antes, len(filas),
             100.0 * no_resuelta_antes / len(filas)))
    afirmada_desp = afirmada_antes - 2
    no_resuelta_desp = no_resuelta_antes + 2
    print("DESPUES (los dos pares se mueven): direccion afirmada %d, NO RESUELTA %d, total %d (%.1f%%)"
          % (afirmada_desp, no_resuelta_desp, len(filas),
             100.0 * no_resuelta_desp / len(filas)))
    print()
    for p in (174, 175):
        print("--- par %d, valor_anterior=%r ---" % (p, CORRECCIONES[p]["valor_anterior"]))

    if a.simular:
        print()
        print("SIMULACION: no se escribio nada.")
        return 0

    for p in (174, 175):
        objetivo[p]["correccion_v100"] = CORRECCIONES[p]

    with io.open(TRAMO4, "w", encoding="utf-8", newline="\n") as f:
        for fila in filas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

    filas2 = cargar()
    bien = (len(filas2) == BASE_TOTAL
            and all("correccion_v100" in f for f in filas2 if f.get("puesto_tramo") in (174, 175))
            and all(f.get("direccion_leida") == CORRECCIONES[f["puesto_tramo"]]["valor_anterior"]
                    for f in filas2 if f.get("puesto_tramo") in (174, 175)))
    print()
    print("APLICADO. Re-lectura: %d filas, correccion_v100 presente en 174 y 175, "
          "direccion_leida vieja intacta: %s" % (len(filas2), "SI" if bien else "NO"))
    return 0 if bien else 1


if __name__ == "__main__":
    raise SystemExit(main())
