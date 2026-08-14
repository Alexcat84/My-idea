# -*- coding: utf-8 -*-
"""VUELTA 21: los sitios de la FASE 0 DE CODIGO, medidos. SOLO LECTURA.

La TAREA 2 de esta vuelta quedo en PARADA por la linea base (el Gate 0 corrido
tal cual mueve `dataset/`), asi que NINGUNA operacion se ejecuta. Lo que si se
puede hacer sin decidir nada es MEDIR: las notas de `OP-C-01` a `OP-C-03`
nombran sitios con archivo y numero de linea, y esas lineas se escribieron el 11
ago 2026. Antes de que nadie las edite conviene saber si siguen donde dicen.

Este instrumento imprime, para cada sitio, la linea que hay HOY en ese numero,
si el archivo existe, y si la linea menciona el resolutor. No juzga el arreglo:
pone la linea delante. Y mide el estado de las dependencias de las cinco
operaciones, porque `OP-C-05` declara `depende_de` una operacion de otra fase.

No escribe nada.
"""
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[2]
OPS = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"

# Los sitios, transcritos UNO A UNO del campo `nota` de cada operacion, sin
# reinterpretarlos. La forma es (operacion, ruta, linea, que dice la nota).
SITIOS = [
    ("OP-C-01", "web/lib/engine/planRedactor.ts", 53, "aMaterial"),
    ("OP-C-01", "web/lib/engine/planRedactor.ts", 183, "llamada a aMaterial"),
    ("OP-C-01", "web/lib/engine/planRedactor.ts", 194, "llamada a aMaterial"),
    ("OP-C-01", "web/app/api/organizer/route.ts", 66, "entry seeds"),
    ("OP-C-01", "web/app/api/organizer/route.ts", 67, "entry seeds"),
    ("OP-C-01", "web/app/api/organizer/route.ts", 68, "entry seeds"),
    ("OP-C-01", "web/app/api/organizer/stream/route.ts", 87, "entry seeds"),
    ("OP-C-01", "web/app/api/organizer/stream/route.ts", 88, "entry seeds"),
    ("OP-C-01", "web/app/api/organizer/stream/route.ts", 89, "entry seeds"),
    ("OP-C-01", "web/lib/compass.ts", 153, "el hueco al reves: un id desconocido PASA"),
    ("OP-C-01", "web/lib/engine/interprete.ts", 331, "hereda de compass"),
    ("OP-C-01", "web/lib/engine/interprete.ts", 332, "hereda de compass"),
    ("OP-C-01", "web/lib/engine/interprete.ts", 333, "hereda de compass"),
    ("OP-C-02", "web/app/api/session/[id]/plan/route.ts", 267, "filtra con nid in graph"),
    ("OP-C-02", "web/app/api/session/[id]/plan/route.ts", 405, "cae al ?? ideacion"),
    ("OP-C-03", "web/lib/engine/graph.ts", 244, "resumenNodo"),
    ("OP-C-03", "web/lib/engine/recorrido.ts", 271, "antes de obtenerPregunta"),
    ("OP-C-03", "web/lib/engine/recorrido.ts", 649, "antes de obtenerPregunta"),
    ("OP-C-03", "web/lib/engine/clasificar.ts", 34, "seeds sin puerta unica"),
    ("OP-C-03", "web/lib/engine/clasificar.ts", 35, "seeds sin puerta unica"),
    ("OP-C-03", "web/lib/engine/clasificar.ts", 36, "seeds sin puerta unica"),
    ("OP-C-03", "web/app/api/project/[id]/world/[pack]/start/route.ts", 149,
     "la guarda que existe, con console.warn"),
    ("OP-C-03", "web/app/api/project/[id]/world/[pack]/start/route.ts", 255,
     "el acceso guardado por la 149"),
    ("OP-C-03", "web/lib/engine/graph.ts", 131, "resolverId, la puerta unica"),
]


def titulo(t):
    print()
    print("=" * 98)
    print(t)
    print("=" * 98)


def main():
    ops = [json.loads(l) for l in open(OPS, encoding="utf-8") if l.strip()]
    por_id = {o["id_op"]: o for o in ops}
    fase0 = [o for o in ops if o["fase"] == "00_CODIGO"]

    titulo("1. LAS CINCO OPERACIONES DE LA FASE 0, con su estado y sus dependencias")
    print("  operaciones de fase 00_CODIGO: %d" % len(fase0))
    for o in sorted(fase0, key=lambda x: x["orden"]):
        print()
        print("  %s  orden %d  tipo %s  estado %s  corte %s" % (
            o["id_op"], o["orden"], o["tipo"], o["estado"], o["fecha_corte"]))
        print("     depende_de: %s" % (o["depende_de"] or "nada"))
        for dep in o["depende_de"]:
            d = por_id.get(dep)
            print("        %s vive en la fase %s, estado %s  <-- NO es de la fase 0" % (
                dep, d["fase"] if d else "?", d["estado"] if d else "?"))
        print("     bloquea_a:  %s" % (o["bloquea_a"] or "nada"))
        print("     criterios de verificacion escritos: %d" % len(o["verificacion"]))
        for v in o["verificacion"]:
            print("        - %s" % v[:150])

    titulo("2. LOS SITIOS DE LA NOTA, medidos contra el codigo de HOY")
    print("  Las notas se escribieron el 11 ago 2026 con archivo y numero de linea.")
    print("  Aqui va la linea que hay HOY en ese numero. El instrumento no juzga:")
    print("  pone la linea delante.")
    cache = {}
    faltan = 0
    for op, ruta, n, glosa in SITIOS:
        p = RAIZ / ruta
        if ruta not in cache:
            cache[ruta] = p.read_text(encoding="utf-8").split("\n") if p.exists() else None
        lineas = cache[ruta]
        print()
        print("  %s  %s:%d   (%s)" % (op, ruta, n, glosa))
        if lineas is None:
            print("      EL ARCHIVO NO EXISTE HOY")
            faltan += 1
            continue
        if n > len(lineas):
            print("      EL ARCHIVO TIENE SOLO %d LINEAS" % len(lineas))
            faltan += 1
            continue
        texto = lineas[n - 1].strip()
        print("      %s" % (texto if texto else "(linea en blanco)"))
        if "resolverId" in texto or "resolver" in texto.lower():
            print("      [ya menciona el resolutor]")

    titulo("3. EL RESOLUTOR, la puerta unica: donde esta y quien lo llama")
    for ruta in ["web/lib/engine/graph.ts"]:
        p = RAIZ / ruta
        if not p.exists():
            print("  %s NO EXISTE" % ruta)
            continue
        lineas = p.read_text(encoding="utf-8").split("\n")
        for i, l in enumerate(lineas, 1):
            if "export function resolverId" in l or "export const resolverId" in l:
                print("  %s:%d  %s" % (ruta, i, l.strip()))
    total = 0
    for p in sorted((RAIZ / "web").rglob("*.ts")):
        if "node_modules" in str(p):
            continue
        try:
            t = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        c = t.count("resolverId(")
        if c:
            total += c
    print("  llamadas a resolverId( en web/**/*.ts (sin node_modules): %d" % total)

    titulo("4. SALDO")
    print("  sitios transcritos de las notas: %d" % len(SITIOS))
    print("  sitios que hoy no se pueden leer (archivo o linea ausente): %d" % faltan)
    print("  NINGUNA operacion se ejecuta en esta vuelta: la TAREA 2 quedo en PARADA")
    print("  por la linea base del Gate 0. Esto es medicion, no ejecucion.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
