"""Vuelta 32, fase 02: EL DESTEJIDO DE UNA COSTURA INTERNA DE FUENTE UNICA.

SUCESOR DECLARADO de scripts/loop/vuelta30_fundir.py, con el cambio y su motivo
dentro (EJECUTOR.md regla 2). Todo lo que aquel guardaba se guarda igual: conteo,
fuente, prefijo de TODOS los pasos, cero perdida con cobertura exacta de 1..N sin
huecos ni repetidos, procedencia, el final de fichero tal cual, y la simulacion
sobre copia en memoria por defecto.

LO QUE SE ANADE, Y NADA MAS QUE ESO: EL CAMPO condiciones_activacion. El motivo,
con la medicion que lo levanto: la ficha de este nodo (docs/FICHA_SUBFUSION_GRADIENTE.md,
seccion a, medicion del 10 ago 2026) no mide solo los pasos, mide tambien las
condiciones, y su cifra es 'veintidos pasos y DIEZ CONDICIONES para cinco cosas'.
El veredicto congelado del puesto 592 repite esa cifra con esas palabras. Un
instrumento que solo tocara pasos dejaria la mitad de la costura medida en pie y
publicaria el nodo como destejido. Las condiciones pasan por las MISMAS guardas
que los pasos: conteo, prefijo, cobertura exacta y mapa.

Uso:
    python scripts/loop/vuelta32_podar.py <plan.json> --simular
    python scripts/loop/vuelta32_podar.py <plan.json> --ejecutar
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def leer_crudo(nid):
    with open(ruta(nid), encoding="utf-8", newline="") as fh:
        crudo = fh.read()
    return json.loads(crudo), ("\n" if crudo.endswith("\n") else "")


def escribir(nid, datos, cola):
    with open(ruta(nid), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def cobertura(mapa, n):
    """Devuelve (repetidos, faltan, sobran) de un mapa destino <- origenes."""
    todos = []
    for v in mapa.values():
        todos.extend(v)
    esperados = set(range(1, n + 1))
    repetidos = sorted({i for i in todos if todos.count(i) > 1})
    faltan = sorted(esperados - set(todos))
    sobran = sorted(set(todos) - esperados)
    return repetidos, faltan, sobran


def revisar_campo(nombre, actual, f, clave_mapa, clave_finales, clave_prefijos, fallos, nid):
    """Guardas comunes a pasos_accionables y a condiciones_activacion."""
    esperado = f.get("%s_totales" % nombre)
    if esperado is not None and len(actual) != esperado:
        fallos.append("%s: %s tiene %d y el plan esperaba %d"
                      % (nid, nombre, len(actual), esperado))
        print("  [ROJO] %s: %d, esperados %d" % (nombre, len(actual), esperado))
        return None
    prefijos = f.get(clave_prefijos) or []
    if len(prefijos) != len(actual):
        fallos.append("%s: %d prefijos para %d %s" % (nid, len(prefijos), len(actual), nombre))
        print("  [ROJO] prefijos %d, %s %d" % (len(prefijos), nombre, len(actual)))
        return None
    malos = [(i + 1, actual[i][:60]) for i, p in enumerate(prefijos)
             if not actual[i].startswith(p)]
    if malos:
        fallos.append("%s: %d %s no calzan con su prefijo" % (nid, len(malos), nombre))
        print("  [ROJO] no calzan: %s" % malos)
        return None
    print("  guarda de texto sobre %s: %d de %d calzan" % (nombre, len(actual), len(actual)))

    mapa = {int(k): list(v) for k, v in f[clave_mapa].items()}
    finales = f[clave_finales]
    if sorted(mapa) != list(range(1, len(finales) + 1)):
        fallos.append("%s: el mapa de %s no indexa 1..%d" % (nid, nombre, len(finales)))
        print("  [ROJO] el mapa de %s no indexa 1..%d" % (nombre, len(finales)))
        return None
    rep, fal, sob = cobertura(mapa, len(actual))
    print("  cero perdida en %s: %d origenes cubiertos de %d"
          % (nombre, sum(len(v) for v in mapa.values()), len(actual)))
    if rep or fal or sob:
        fallos.append("%s: cobertura rota en %s (repetidos %s, faltan %s, sobran %s)"
                      % (nid, nombre, rep, fal, sob))
        print("  [ROJO] repetidos %s, faltan %s, sobran %s" % (rep, fal, sob))
        return None

    print("  EL MAPA DE %s, destino <- origenes:" % nombre.upper())
    for k in sorted(mapa):
        marca = "  (VERBATIM)" if finales[k - 1] == actual[mapa[k][0] - 1] else "  (con remedio)"
        print("    %2d <- %-16s %s%s" % (k, mapa[k], finales[k - 1][:80], marca))
    return finales


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    plan_path = sys.argv[1]
    modo = sys.argv[2] if len(sys.argv) > 2 else "--simular"
    if modo not in ("--simular", "--ejecutar"):
        print(__doc__)
        return 2

    plan = json.load(open(plan_path, encoding="utf-8"))
    print("PLAN     : %s" % plan_path)
    print("OPERACION: %s" % plan["operacion"])
    print("REGLA    : %s" % plan.get("regla", "?"))
    print("MODO     : %s" % modo)
    print("=" * 78)

    fallos = []
    memoria = {}

    for f in plan["nodos"]:
        nid = f["nodo"]
        print("\n" + "-" * 78)
        print("NODO: %s" % nid)
        if not os.path.exists(ruta(nid)):
            fallos.append("%s: no existe en el dataset" % nid)
            print("  [ROJO] no existe")
            continue
        d, cola = leer_crudo(nid)

        if d.get("fuente") != f["fuente_esperada"]:
            fallos.append("%s: fuente inesperada" % nid)
            print("  [ROJO] fuente de hoy : %r" % d.get("fuente"))
            print("         fuente esperada: %r" % f["fuente_esperada"])
            continue

        pasos = list(d.get("pasos_accionables") or [])
        finales = revisar_campo("pasos", pasos, f, "mapa_pasos", "pasos_finales",
                                "prefijos_pasos", fallos, nid)
        if finales is None:
            continue

        cond_finales = None
        if f.get("mapa_condiciones"):
            cond = list(d.get("condiciones_activacion") or [])
            cond_finales = revisar_campo("condiciones", cond, f, "mapa_condiciones",
                                         "condiciones_finales", "prefijos_condiciones",
                                         fallos, nid)
            if cond_finales is None:
                continue

        proc = f.get("procedencia") or []
        cubiertos = set()
        for p in proc:
            cubiertos |= set(p["pasos_del_resultado"])
        if cubiertos != set(range(1, len(finales) + 1)):
            fallos.append("%s: la procedencia no cubre los %d pasos del resultado"
                          % (nid, len(finales)))
            print("  [ROJO] procedencia incompleta: %s" % sorted(cubiertos))
            continue
        for p in proc:
            print("    procedencia: pasos %s del resultado <- %s"
                  % (p["pasos_del_resultado"], p["libro"]))

        print("  pasos %d -> %d" % (len(pasos), len(finales)))
        if cond_finales is not None:
            print("  condiciones %d -> %d" % (len(d.get("condiciones_activacion") or []),
                                              len(cond_finales)))
        print("  fuente: %r  (SIN CAMBIO)" % d.get("fuente"))

        d["pasos_accionables"] = finales
        if cond_finales is not None:
            d["condiciones_activacion"] = cond_finales
        memoria[nid] = (d, cola)

    print("\n" + "=" * 78)
    print("RESUMEN")
    print("  ficheros que se tocarian: %d" % len(memoria))
    if fallos:
        print("\nPARADA: %d guarda(s) en rojo. NO se escribe nada." % len(fallos))
        for x in fallos:
            print("  - %s" % x)
        return 1

    if modo == "--simular":
        print("\nSIMULACION: cero escrituras.")
        return 0

    for nid, (datos, cola) in memoria.items():
        escribir(nid, datos, cola)
    print("\nESCRITO: %d fichero(s) en dataset/nodos/." % len(memoria))
    for nid in sorted(memoria):
        print("  - %s" % nid)
    return 0


if __name__ == "__main__":
    sys.exit(main())
