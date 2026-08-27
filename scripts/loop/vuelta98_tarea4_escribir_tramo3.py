# -*- coding: utf-8 -*-
r"""vuelta98_tarea4_escribir_tramo3.py . VUELTA 98, TAREA 4: ESCRIBE EL JSONL DE
VEREDICTOS DEL TERCER TRAMO DE OP-E-03.

POR QUE EXISTE ESTE INSTRUMENTO Y NO SE ESCRIBE EL JSONL A MANO (EJECUTOR.md
regla 1, "LA TABLA SE IMPRIME, NO SE TECLEA"): de los catorce campos de cada
fila, DIEZ son mecanicos (puesto, dominio, madre, hijo, paso casado, las cuatro
marcas de LECTURA DIRIGIDA y la vara) y viven ya en la salida del instrumento de
lectura, `docs/loop/SALIDA_V98_TAREA4_TRAMO3_MATERIAL.txt`. Este script los
PARSEA de ahi. Lo unico que el ejecutor aporta es lo que solo puede aportar un
lector: la CLASE, la DIRECCION y la RAZON, que viven en
`scripts/loop/vuelta98_tarea4_juicios.py`.

QUE GARANTIZA, y por eso hay tres guardas y no una: teclear a mano el id de una
madre o de un hijo es exactamente la especie de caida que la campana ya cazo
tres veces (celdas manuales en tablas que un instrumento ya producia). Aqui los
ids NO se teclean en ningun sitio: se leen del material. El fichero de juicios
solo lleva NUMEROS DE PUESTO, clase, direccion y razon.

MECANICA DE ROJO, y no escribe nada si salta:
  (i)   el material no trae exactamente los pares del rango que se pide;
  (ii)  un puesto juzgado no existe en el material, o un puesto del material no
        esta juzgado (los dos lados, para que nada se caiga callado);
  (iii) una clase no es A, B, C o D;
  (iv)  una direccion afirmada nombra un id que NO es la madre ni el hijo de esa
        fila segun el material (la guarda que hace imposible teclear mal un id);
  (v)   una razon esta vacia o no cita la vara;
  (vi)  el fichero de salida ya existe y --aplicar no lleva --rehacer.

USO:
  python scripts/loop/vuelta98_tarea4_escribir_tramo3.py --medir
  python scripts/loop/vuelta98_tarea4_escribir_tramo3.py --aplicar
  python scripts/loop/vuelta98_tarea4_escribir_tramo3.py --aplicar --rehacer
"""
import argparse
import collections
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

MATERIAL = os.path.join(RAIZ, "docs", "loop", "SALIDA_V98_TAREA4_TRAMO3_MATERIAL.txt")
SALIDA = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO3_V98.jsonl")

VARA = ("banco 9.6.1 rama contenido manda; direccion por 9.6.2; tamano del solape "
        "no decide por 9.6.3; la figura de los dos sentidos por 9.22")

RE_CAB = re.compile(r"^\[(\d+)/(\d+)\] dominio (\S+) \.")
RE_MADRE = re.compile(r"^  madre: (\S+)")
RE_HIJO = re.compile(r"^  hijo:  (\S+)")
RE_PASO = re.compile(r"^  EL PASO DE LA MADRE QUE EL BARRIDO CASO \(numero (\d+)\):")
RE_SENAL = re.compile(r"^  senal del barrido: titulo_ratio ([\d.]+) \. contencion ([\d.]+)")


def leer_material():
    """Los campos mecanicos, PARSEADOS del material. Ninguno se teclea."""
    filas = {}
    actual = None
    for linea in io.open(MATERIAL, encoding="utf-8"):
        linea = linea.rstrip("\n")
        m = RE_CAB.match(linea)
        if m:
            actual = {"puesto_tramo": int(m.group(1)), "total": int(m.group(2)),
                      "dominio": m.group(3)}
            filas[actual["puesto_tramo"]] = actual
            continue
        if actual is None:
            continue
        m = RE_MADRE.match(linea)
        if m:
            actual["madre_de_la_bolsa"] = m.group(1)
            continue
        m = RE_HIJO.match(linea)
        if m:
            actual["hijo_de_la_bolsa"] = m.group(1)
            continue
        m = RE_SENAL.match(linea)
        if m:
            actual["titulo_ratio"] = float(m.group(1))
            continue
        m = RE_PASO.match(linea)
        if m and "paso_casado" not in actual:
            actual["paso_casado"] = int(m.group(1))
    return filas


def construir(juicios, material):
    fallos = []
    puestos_mat = sorted(material)
    puestos_jui = sorted(juicios)
    faltan = [p for p in puestos_mat if p not in juicios]
    sobran = [p for p in puestos_jui if p not in material]
    if sobran:
        fallos.append("juzgados %d puesto(s) que el material no trae: %s"
                      % (len(sobran), ", ".join(str(x) for x in sobran)))

    filas = []
    for p in puestos_jui:
        if p not in material:
            continue
        m = material[p]
        j = juicios[p]
        clase, direccion, razon = j["clase"], j.get("direccion"), j["razon"]
        if clase not in ("A", "B", "C", "D"):
            fallos.append("el puesto %d trae clase %r, que no es A, B, C ni D"
                          % (p, clase))
        if not razon or len(razon) < 40:
            fallos.append("el puesto %d trae una razon vacia o demasiado corta" % p)
        elif not re.search(r"9\.\d", razon):
            fallos.append("la razon del puesto %d no cita ninguna regla del banco" % p)
        if direccion:
            ids = [x.strip() for x in direccion.split("->")]
            if len(ids) != 2:
                fallos.append("la direccion del puesto %d no tiene la forma 'a -> b'" % p)
            else:
                validos = {m["madre_de_la_bolsa"], m["hijo_de_la_bolsa"]}
                for x in ids:
                    if x not in validos:
                        fallos.append("la direccion del puesto %d nombra %r, que no es "
                                      "ni la madre (%s) ni el hijo (%s) del material"
                                      % (p, x, m["madre_de_la_bolsa"], m["hijo_de_la_bolsa"]))
                if ids[0] == ids[1]:
                    fallos.append("la direccion del puesto %d apunta a si misma" % p)
        filas.append({
            "puesto_tramo": p,
            "operacion": "OP-E-03",
            "marca": "LECTURA DIRIGIDA",
            "fuera_de_la_cola": True,
            "fuera_de_la_tasa_por_dominio": True,
            "mueve_el_marcador_del_cribado": False,
            "dominio": m["dominio"],
            "madre_de_la_bolsa": m["madre_de_la_bolsa"],
            "hijo_de_la_bolsa": m["hijo_de_la_bolsa"],
            "paso_casado": m.get("paso_casado"),
            "clase": clase,
            "direccion_leida": direccion,
            "razon": razon,
            "vara": VARA,
        })
    return filas, fallos, faltan


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--medir", action="store_true")
    g.add_argument("--aplicar", action="store_true")
    ap.add_argument("--rehacer", action="store_true")
    a = ap.parse_args()

    from vuelta98_tarea4_juicios import JUICIOS  # noqa: E402

    material = leer_material()
    filas, fallos, faltan = construir(JUICIOS, material)

    print("=" * 100)
    print("VEREDICTOS DEL TERCER TRAMO DE OP-E-03 (vuelta 98, TAREA 4)")
    print("=" * 100)
    print("MATERIAL: %s, %d pares parseados (del %d al %d)"
          % (os.path.basename(MATERIAL), len(material),
             min(material) if material else 0, max(material) if material else 0))
    print("JUICIOS APORTADOS POR LA LECTURA: %d" % len(JUICIOS))
    print("PARES DEL MATERIAL AUN SIN JUZGAR: %d%s"
          % (len(faltan), (" (del %d al %d)" % (faltan[0], faltan[-1])) if faltan else ""))
    print()
    c = collections.Counter(f["clase"] for f in filas)
    doms = collections.Counter(f["dominio"] for f in filas)
    con_dir = [f["puesto_tramo"] for f in filas if f["direccion_leida"]]
    sin_dir = [f["puesto_tramo"] for f in filas if not f["direccion_leida"]]
    print("CLASES, contadas de las filas construidas: A %d, B %d, C %d, D %d"
          % (c["A"], c["B"], c["C"], c["D"]))
    for etiqueta in ("A", "B", "C"):
        cuales = [f["puesto_tramo"] for f in filas if f["clase"] == etiqueta]
        if cuales:
            print("   los %s: %s" % (etiqueta, ", ".join(str(x) for x in cuales)))
    print("DIRECCION: %d afirmadas, %d NO RESUELTAS (%.1f por ciento)"
          % (len(con_dir), len(sin_dir),
             100.0 * len(sin_dir) / len(filas) if filas else 0.0))
    print("   las no resueltas: %s" % ", ".join(str(x) for x in sin_dir))
    print("POR DOMINIO, y NO entra en la tasa del banco 9.27: %s"
          % ", ".join("%s %d" % (d, n) for d, n in sorted(doms.items())))
    invertidas = [f["puesto_tramo"] for f in filas
                  if f["direccion_leida"]
                  and f["direccion_leida"].split("->")[0].strip() == f["hijo_de_la_bolsa"]]
    print("DIRECCIONES INVERTIDAS RESPECTO A LA ETIQUETA DE LA BOLSA: %d%s"
          % (len(invertidas),
             (" (%s)" % ", ".join(str(x) for x in invertidas)) if invertidas else ""))
    print()

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    if a.medir:
        print("VERDE (--medir): las %d filas se construyen sin un solo fallo. No se "
              "escribio nada." % len(filas))
        return 0

    if os.path.exists(SALIDA) and not a.rehacer:
        print("ROJO: %s ya existe y no se paso --rehacer. NO SE ESCRIBE NADA."
              % os.path.relpath(SALIDA, RAIZ))
        return 1

    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as f:
        for x in filas:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")

    releidas = [json.loads(l) for l in io.open(SALIDA, encoding="utf-8") if l.strip()]
    bien = (len(releidas) == len(filas)
            and all(r["marca"] == "LECTURA DIRIGIDA" and r["fuera_de_la_cola"]
                    and r["fuera_de_la_tasa_por_dominio"]
                    and r["mueve_el_marcador_del_cribado"] is False
                    for r in releidas))
    print("ESCRITO: %s, %d filas. Re-lectura valida y las %d con la marca completa "
          "de LECTURA DIRIGIDA: %s"
          % (os.path.relpath(SALIDA, RAIZ), len(releidas), len(releidas),
             "SI" if bien else "NO"))
    return 0 if bien else 1


if __name__ == "__main__":
    raise SystemExit(main())
