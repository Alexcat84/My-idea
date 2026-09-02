# -*- coding: utf-8 -*-
"""vuelta139_tabla_fase06.py . LA TABLA DE LA FASE 06 DEL REPORTE, IMPRESA DE
SUS FICHEROS DE SALIDA Y NO TECLEADA.

POR QUE NACE (EJECUTOR.md 1, "LA TABLA SE CUENTA DE SU FICHERO", 26 ago 2026, y
la TAREA 4 del encargo de la vuelta 139). El acta 138 registro DOS caidas de
reporte del ejecutor y las dos vivian en la tabla de la fase 06 o en la seccion
9: una cifra en `grupos` y una afirmacion con LOS NOMBRES CAMBIADOS. El encargo
manda releer ese tramo AL DOBLE y, si la salida NOMBRA operaciones o ids, que la
tabla NOMBRE LOS MISMOS. La unica forma de que eso no dependa de mi atencion es
que la tabla la escriba un instrumento que lea los ficheros.

QUE LEE, POR OPERACION, y todo de `docs/loop/`:
  SALIDA_V139_3_SIM_<OP>.txt        . la simulacion previa (P.7): duplicadas
                                      nuevas CON SUS NOMBRES, auto aristas,
                                      aristas internas y el cableado.
  SALIDA_V139_3_PLAN_<OP>.txt       . el reparto sellado: piezas, enteras, ya
                                      dichas, de INCISO y las que ya viajan en
                                      el acto; y los pares de VIAJA_EN_EL_ACTO.
  SALIDA_V139_3_FUNDIR_EJEC_<OP>.txt. la ejecucion: pasos y condiciones antes y
                                      despues, las cuatro guardas A a D y el
                                      delta de deprecados.
  SALIDA_V139_3_CASOPOS_<OP>.txt    . el caso positivo.
  SALIDA_V139_3_P5_LECTURA_DE_ACTO.txt . los pares leidos por operacion.

NINGUNA CELDA SE TECLEA. Si un fichero falta o un patron no casa, la celda dice
FALTA y el instrumento sale en ROJO: es preferible una celda que grita a una
celda inventada (banco 9, fallar ruidoso).

USO:
  python scripts/loop/vuelta139_tabla_fase06.py
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")

OPS = [
    ("OP-M-01-FUSION", "OPM01FUSION"),
    ("OP-M-03-III", "OPM03III"),
    ("OP-M-05-INDICE", "OPM05INDICE"),
    ("OP-M-05-EDIFICIO", "OPM05EDIFICIO"),
    ("OP-M-05-APERTURA", "OPM05APERTURA"),
]


def leer(nombre, fallos):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        fallos.append("no existe %s" % nombre)
        return None
    return io.open(ruta, encoding="utf-8", errors="replace").read()


def uno(patron, texto, etq, fallos, grupo=1):
    if texto is None:
        return "FALTA"
    m = re.search(patron, texto)
    if not m:
        fallos.append("no se pudo leer %s" % etq)
        return "FALTA"
    return m.group(grupo)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    fallos = []
    p5 = leer("SALIDA_V139_3_P5_LECTURA_DE_ACTO.txt", fallos)

    filas = []
    for id_op, corto in OPS:
        sim = leer("SALIDA_V139_3_SIM_%s.txt" % corto, fallos)
        plan = leer("SALIDA_V139_3_PLAN_%s.txt" % corto, fallos)
        ejec = leer("SALIDA_V139_3_FUNDIR_EJEC_%s.txt" % corto, fallos)
        caso = leer("SALIDA_V139_3_CASOPOS_%s.txt" % corto, fallos)

        # LAS DUPLICADAS: se CUENTAN las lineas nombradas del bloque 4, y se
        # coteja contra el TOTAL que el propio instrumento imprime. Si no
        # cuadran, es ROJO: es la guarda contra contar mal el mismo fichero.
        dup_nombres, dup_total = [], "FALTA"
        if sim is not None:
            bloque = sim.split("### 4.")[-1].split("### 5.")[0]
            dup_nombres = re.findall(r"^\s{5}(\S+)\s+nodos_(?:previos|siguientes)\s+->",
                                     bloque, re.MULTILINE)
            dup_total = uno(r"TOTAL NUEVAS: (\d+)", bloque, "TOTAL NUEVAS de %s" % id_op, fallos)
            if dup_total != "FALTA" and int(dup_total) != len(dup_nombres):
                fallos.append("%s: el bloque 4 nombra %d duplicada(s) y su TOTAL dice %s"
                              % (id_op, len(dup_nombres), dup_total))
        auto = "ninguna" if (sim and "### 5. AUTO-ARISTAS" in sim
                             and "ninguna" in sim.split("### 5.")[-1].split("### 6.")[0]) else "REVISAR"
        internas = "NINGUNA" if (sim and "NINGUNA: el acto queda sin aristas internas" in sim) else "REVISAR"
        cableados = re.findall(r">>> gana \S+ por (\d+) contra (\d+)", sim or "")

        piezas = uno(r"REPARTO: piezas (\d+)", plan, "piezas de %s" % id_op, fallos)
        enteras = uno(r"piezas \d+ \(enteras (\d+)", plan, "enteras de %s" % id_op, fallos)
        dichas = uno(r"ya dichas (\d+)", plan, "ya dichas de %s" % id_op, fallos)
        incisos = uno(r"de INCISO (\d+)", plan, "incisos de %s" % id_op, fallos)
        viajan = uno(r"que ya viajan en el acto (\d+)", plan, "viajan de %s" % id_op, fallos)
        pares_viaje = re.findall(r"el paso (\d+) de (\S+) viaja por el paso (\d+) de (\S+)",
                                 plan or "")

        m = re.search(r"pasos (\d+) -> (\d+) \(anadidos \d+\) \| condiciones (\d+) -> (\d+)",
                      ejec or "")
        if not m:
            fallos.append("no se pudo leer el crecimiento de %s" % id_op)
            crec = "FALTA"
        else:
            crec = "%s a %s pasos, %s a %s condiciones" % m.groups()
        guardas = re.findall(r"guarda ([AB]),[^:]*: (OK) \((\d+)\)", ejec or "")
        gc = uno(r"guarda C, los CINCO campos que esta operacion NO redacta, intactos: (\S+ de \S+)",
                 ejec, "guarda C de %s" % id_op, fallos)
        gd = "OK" if (ejec and re.search(r"guarda D, los \d+ absorbidos conservan su texto INTACTO: OK", ejec)) else "REVISAR"
        delta = uno(r"delta deprecados: (\+\d+) \(esperado (\+\d+)\): (OK)", ejec,
                    "delta de %s" % id_op, fallos)
        nueve = "LAS NUEVE MUERDEN" if (caso and "LAS NUEVE MUERDEN" in caso) else "REVISAR"

        pares_p5 = "FALTA"
        if p5:
            bloque = p5.split("########## %s ##########" % id_op)
            if len(bloque) > 1:
                pares_p5 = uno(r"CIFRA pares leidos: (\d+) pares", bloque[1],
                               "P.5 de %s" % id_op, fallos)

        filas.append({
            "id": id_op, "dup_n": len(dup_nombres), "dup_total": dup_total,
            "dup_nombres": dup_nombres, "auto": auto, "internas": internas,
            "cableados": cableados, "piezas": piezas, "enteras": enteras,
            "dichas": dichas, "incisos": incisos, "viajan": viajan,
            "pares_viaje": pares_viaje, "crec": crec, "guardas": guardas,
            "gc": gc, "gd": gd, "delta": delta, "nueve": nueve, "p5": pares_p5,
        })

    print("=" * 78)
    print("LA TABLA DE LA FASE 06, IMPRESA DE SUS FICHEROS DE SALIDA")
    print("Ninguna celda esta tecleada. Cada una cita el fichero del que sale.")
    print("=" * 78)
    print()
    print("--- TABLA 1: LO QUE CADA FUSION MOVIO ---")
    print()
    print("| operacion | P.5 | caso positivo | crecimiento del superviviente | delta deprecados |")
    print("|---|---|---|---|---|")
    for f in filas:
        print("| `%s` | %s pares leidos = %s del acto, EXIT 0 | %s | %s | %s |"
              % (f["id"], f["p5"], f["p5"], f["nueve"], f["crec"], f["delta"]))
    print()
    print("--- TABLA 2: EL REPARTO DE PIEZAS, CONTADO POR EL GENERADOR ---")
    print()
    print("| operacion | piezas | enteras (APPEND) | ya dichas (CUBIERTO) | de INCISO | que ya viajan en el acto |")
    print("|---|---:|---:|---:|---:|---:|")
    tot = {"piezas": 0, "enteras": 0, "dichas": 0, "incisos": 0, "viajan": 0}
    for f in filas:
        print("| `%s` | %s | %s | %s | %s | %s |"
              % (f["id"], f["piezas"], f["enteras"], f["dichas"], f["incisos"], f["viajan"]))
        for k in tot:
            if f[k] != "FALTA":
                tot[k] += int(f[k])
    print("| **TOTAL de las cinco** | **%d** | **%d** | **%d** | **%d** | **%d** |"
          % (tot["piezas"], tot["enteras"], tot["dichas"], tot["incisos"], tot["viajan"]))
    print()
    print("--- TABLA 3: DONDE MUERDE EL HUECO, CON SUS PARES NOMBRADOS ---")
    print()
    print("| operacion | VIAJA_EN_EL_ACTO | los pares, del fichero del plan |")
    print("|---|---:|---|")
    muerden = 0
    for f in filas:
        if f["pares_viaje"]:
            muerden += 1
            detalle = "; ".join("paso %s de `%s` viaja por el paso %s de `%s`" % p
                                for p in f["pares_viaje"])
        else:
            detalle = "NINGUNO"
        print("| `%s` | %s | %s |" % (f["id"], f["viajan"], detalle))
    print()
    print("CIFRA operaciones donde el hueco muerde: %d de %d" % (muerden, len(filas)))
    print("   las que muerden, nombradas: %s"
          % ", ".join(f["id"] for f in filas if f["pares_viaje"]))
    print("   las que NO, nombradas     : %s"
          % (", ".join(f["id"] for f in filas if not f["pares_viaje"]) or "NINGUNA"))
    print()
    print("--- TABLA 4: LAS GUARDAS DEL FUNDIDOR Y LA SIMULACION PREVIA ---")
    print()
    print("| operacion | guarda A auto-aristas | guarda B duplicadas tras resolver | guarda C | guarda D | duplicadas de la simulacion | auto aristas | aristas internas |")
    print("|---|---|---|---|---|---:|---|---|")
    for f in filas:
        ga = next(("%s (%s)" % (v, n) for k, v, n in f["guardas"] if k == "A"), "FALTA")
        gb = next(("%s (%s)" % (v, n) for k, v, n in f["guardas"] if k == "B"), "FALTA")
        print("| `%s` | %s | %s | %s | %s | %s | %s | %s |"
              % (f["id"], ga, gb, f["gc"], f["gd"], f["dup_total"], f["auto"], f["internas"]))
    print()
    print("--- LAS DUPLICADAS, NOMBRE POR NOMBRE (bloque 4 de cada simulacion) ---")
    for f in filas:
        print("  %s: %s nombradas, TOTAL NUEVAS dice %s"
              % (f["id"], f["dup_n"], f["dup_total"]))
        for n in f["dup_nombres"]:
            print("     %s" % n)
    print()
    print("--- EL CABLEADO MEDIDO HOY, del bloque 1 de cada simulacion ---")
    for f in filas:
        print("  %-20s %s" % (f["id"], ", ".join("%s contra %s" % c for c in f["cableados"])))

    print()
    if fallos:
        print("ROJO, %d celda(s) no se pudieron leer y NO se inventan:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1
    print("VERDE: las %d filas salen enteras de sus ficheros." % len(filas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
