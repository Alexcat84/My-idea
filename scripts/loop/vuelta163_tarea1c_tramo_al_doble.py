# -*- coding: utf-8 -*-
r"""vuelta163_tarea1c_tramo_al_doble.py . TAREA 1.c de la vuelta 163.

LA RELECTURA AL DOBLE DEL TRAMO QUE LA REGLA DEL CREDITO OBLIGA (`AUDITOR.md`
1.2, acta 162 seccion 7). El tramo esta medido y es pequeno: LAS CINCO CAIDAS DE
CLASE DE LA `R.30`.

EL ENCARGO LO DICE CON TODAS SUS LETRAS: *"Cuatro ya llevan dos lecturas ciegas
independientes que coinciden (005 y 100 de mi ciega de la 161; 094 y 118 de la
mia de hoy) y ESO LO COMPRUEBAS DEL REGISTRO, NO DE MI PALABRA."*

ASI QUE SE COMPRUEBA DEL REGISTRO, Y LA NOMINA DEL TRAMO TAMPOCO SE TECLEA: se
lee de la propia `R.30` en `docs/PENDIENTES.md`, que es donde la casa la
escribio. Si lo que el registro dice no calza con lo que el encargo afirma, se
publica la diferencia MEDIDA en vez de copiar la afirmacion, que es
`EJECUTOR.md` 2.

QUE CUENTA COMO SEGUNDA LECTURA: lo que `P.5.2` (1) define, leido hoy del banco
y no tecleado aqui, y para no reimplementarlo SE IMPORTA el contador de nombre
estable (`contador_de_segundas_lecturas.py`, la TAREA 5.a de esta vuelta), que
es la ley de una sola fuente.

USO:
  python scripts/loop/vuelta163_tarea1c_tramo_al_doble.py
  python scripts/loop/vuelta163_tarea1c_tramo_al_doble.py --mutacion
"""
import argparse
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
PENDIENTES = os.path.join(RAIZ, "docs", "PENDIENTES.md")
SELLO_162 = os.path.join(RAIZ, "docs", "loop", "_auditor_v162_mis_adjudicaciones.txt")

import importlib   # noqa: E402
CONTADOR = importlib.import_module("contador_de_segundas_lecturas")


def filas():
    out = {}
    for l in io.open(REGISTRO, encoding="utf-8"):
        l = l.strip()
        if not l:
            continue
        d = json.loads(l)
        m = re.match(r"^(LD-OPC05-\d+)", d.get("cita", ""))
        if m:
            out[m.group(1)] = d
    return out


def nomina_del_tramo():
    """LAS CINCO CAIDAS DE CLASE, LEIDAS DE LA `R.30` Y NO TECLEADAS. La entrada
    trae una tabla cuya primera celda es el id de la lectura dirigida."""
    texto = io.open(PENDIENTES, encoding="utf-8").read()
    lineas = texto.split("\n")
    inicios = [i for i, l in enumerate(lineas, 1) if l.startswith("## R.30.")]
    if len(inicios) != 1:
        raise SystemExit("ROJO: `## R.30.` aparece %d veces en docs/PENDIENTES.md."
                         % len(inicios))
    inicio = inicios[0]
    siguientes = [i for i, l in enumerate(lineas, 1)
                  if i > inicio and re.match(r"^## R\.\d+\.", l)]
    fin = min(siguientes) - 1 if siguientes else len(lineas)
    vistos = []
    for i in range(inicio, fin + 1):
        for eid in re.findall(r"LD-OPC05-(\d+)", lineas[i - 1]):
            key = "LD-OPC05-%s" % eid
            if key not in vistos:
                vistos.append(key)
    return inicio, fin, vistos


def marcas_de_relectura(fila):
    """LAS MARCAS CONTABLES DE LA FILA, con el contador de P.5.2 importado y no
    reimplementado."""
    return CONTADOR.actos_de_relectura(fila.get("razon", ""))


def veredicto_sellado_162(eid):
    """La letra que el auditor sello en su ciega de la vuelta 162, parseada de su
    fichero. NO es el registro: por eso se publica APARTE y con su nombre."""
    if not os.path.exists(SELLO_162):
        return None
    txt = io.open(SELLO_162, encoding="utf-8", errors="replace").read()
    n = eid.split("-")[-1]
    m = re.search(r"^\s*%s\s+\S.*?\s([CD])\s*$" % re.escape(n), txt, re.M)
    return m.group(1) if m else None


def main():
    print("=" * 78)
    print("VUELTA 163, TAREA 1.c: LA RELECTURA AL DOBLE DEL TRAMO, CONTADA DEL REGISTRO")
    print("=" * 78)
    print("")

    print("A) LA NOMINA DEL TRAMO, LEIDA DE LA R.30 Y NO TECLEADA")
    inicio, fin, tramo = nomina_del_tramo()
    print("   docs/PENDIENTES.md, lineas %d a %d" % (inicio, fin))
    print("   CIFRA ids de lectura dirigida nombrados en la R.30: %d" % len(tramo))
    print("   NOMINA: %s" % ", ".join(tramo))
    print("")

    f = filas()
    print("B) LAS MARCAS DE SEGUNDA LECTURA, CONTADAS DEL REGISTRO FILA A FILA")
    print("   (el contador de P.5.2 se IMPORTA de contador_de_segundas_lecturas.py,")
    print("   no se reimplementa)")
    con_marca, sin_marca = [], []
    for eid in tramo:
        fila = f.get(eid)
        if not fila:
            print("   %s  NO ESTA EN EL REGISTRO" % eid)
            continue
        actos = marcas_de_relectura(fila)
        print("   %s  clase %s  |  CIFRA marcas contables: %d" % (eid, fila["clase"], len(actos)))
        for tipo, vuelta in actos:
            print("        %s, vuelta %s" % (tipo, vuelta))
        (con_marca if actos else sin_marca).append(eid)
    print("")
    print("   CIFRA del tramo con al menos una marca en el registro: %d (%s)"
          % (len(con_marca), ", ".join(con_marca) or "ninguna"))
    print("   CIFRA del tramo SIN ninguna marca en el registro: %d (%s)"
          % (len(sin_marca), ", ".join(sin_marca) or "ninguna"))
    print("")

    print("C) LA CIEGA DE LA VUELTA 162, QUE NO VIVE EN EL REGISTRO, MEDIDA APARTE")
    print("   fichero sellado: docs/loop/_auditor_v162_mis_adjudicaciones.txt")
    sellados = {}
    for eid in tramo:
        v = veredicto_sellado_162(eid)
        sellados[eid] = v
        vig = f[eid]["clase"] if eid in f else "?"
        print("   %s  letra sellada en la ciega de la 162: %-13s | clase vigente: %s"
              % (eid, v or "NO APARECE", vig))
    coinciden = [e for e in tramo if sellados[e] and e in f and sellados[e] == f[e]["clase"]]
    discrepan = [e for e in tramo if sellados[e] and e in f and sellados[e] != f[e]["clase"]]
    print("   CIFRA del tramo con letra en la ciega de la 162: %d"
          % sum(1 for e in tramo if sellados[e]))
    print("   CIFRA que coinciden con la clase vigente: %d (%s)"
          % (len(coinciden), ", ".join(coinciden) or "ninguna"))
    print("   CIFRA que discrepan: %d (%s)"
          % (len(discrepan), ", ".join(discrepan) or "ninguna"))
    print("")

    print("D) LA CUENTA QUE EL ENCARGO PIDE PUBLICAR, Y LA DIFERENCIA MEDIDA")
    print("   El encargo afirma: CUATRO del tramo ya llevan DOS LECTURAS CIEGAS")
    print("   INDEPENDIENTES QUE COINCIDEN (005 y 100 de la ciega de la 161; 094 y")
    print("   118 de la ciega de la 162), y que eso se comprueba DEL REGISTRO.")
    print("")
    print("   SE COMPRUEBA DEL REGISTRO, Y NO ES LO MISMO 'marca contable' QUE")
    print("   'lectura ciega del auditor'. Una marca de TRAMO_AL_DOBLE es la segunda")
    print("   pasada DEL PROPIO EJECUTOR sobre su tramo, no una lectura independiente")
    print("   de otra pluma. Asi que se cuentan las DOS cosas por separado.")
    print("")
    print("   D.1 MARCA CONTABLE DE CUALQUIER TIPO, EN EL REGISTRO")
    print("      CIFRA: %d de %d (%s)"
          % (len(con_marca), len(tramo), ", ".join(con_marca) or "ninguna"))
    ciegas = [e for e in tramo
              if any(t == "CIEGA_DEL_AUDITOR" for t, _v in marcas_de_relectura(f[e]))]
    sin_ciega = [e for e in tramo if e not in ciegas]
    print("")
    print("   D.2 MARCA DE LECTURA CIEGA DEL AUDITOR, EN EL REGISTRO")
    print("      CIFRA con marca de ciega en el registro: %d (%s)"
          % (len(ciegas), ", ".join(ciegas) or "ninguna"))
    print("      CIFRA SIN marca de ciega en el registro: %d (%s)"
          % (len(sin_ciega), ", ".join(sin_ciega) or "ninguna"))
    solo_sello = [e for e in sin_ciega if sellados[e]]
    print("")
    print("   D.3 LA DIFERENCIA, DECLARADA Y NO RESUELTA COPIANDO (EJECUTOR.md 2)")
    print("      La ciega de la vuelta 162 dejo su letra SELLADA en el fichero del")
    print("      auditor, y esa letra NO ESTA EN EL REGISTRO:")
    print("      CIFRA leidas por la ciega de la 162 y sin marca de ciega en el")
    print("      registro: %d (%s)" % (len(solo_sello), ", ".join(solo_sello) or "ninguna"))
    print("      POR TANTO, MEDIDO DEL REGISTRO Y NO DE LA PALABRA DE NADIE: del tramo,")
    print("      %d llevan la lectura ciega del auditor CONTABLE (%s) y %d NO la llevan"
          % (len(ciegas), ", ".join(ciegas) or "ninguna", len(sin_ciega)))
    print("      (%s), aunque de esas %d el fichero sellado si trae letra."
          % (", ".join(sin_ciega) or "ninguna", len(solo_sello)))
    print("      LA AFIRMACION DEL ENCARGO SE CUMPLE EN 005 Y 100 CONTRA EL REGISTRO;")
    print("      EN 094 Y 118 SE CUMPLE CONTRA EL FICHERO SELLADO Y NO CONTRA EL")
    print("      REGISTRO, y eso es lo que P.5.2 (1) llama no contable todavia.")
    print("      NO SE ESCRIBE LA MARCA EN ESTA VUELTA, y se dice por que: la vara de")
    print("      aceptacion de la TAREA 5.a exige que la cifra de P.5.2 salga IDENTICA")
    print("      (92 / 16 / 30 / 115 / 8), y escribir marcas nuevas la moveria. Va como")
    print("      discutible del reporte, no como decision callada.")
    print("")
    print("   CIFRA del tramo: %d" % len(tramo))
    print("   CIFRA con marca contable en el registro: %d" % len(con_marca))
    print("   CIFRA con lectura ciega del auditor CONTABLE en el registro: %d" % len(ciegas))
    print("   CIFRA con lectura ciega de la 162 SELLADA pero no contable: %d" % len(solo_sello))
    print("   CIFRA que la relectura conjunta de esta vuelta relee al doble: 1 "
          "(LD-OPC05-101, la TAREA 1.b)")
    print("")
    return 0


def prueba_de_mutacion():
    print("=" * 78)
    print("VUELTA 163, TAREA 1.c: CASO POSITIVO POR MUTACION")
    print("=" * 78)
    print("")
    f = filas()
    _i, _fin, tramo = nomina_del_tramo()
    casos = []
    casos.append(("la_R30_nombra_cinco_ids", len(tramo), 5))
    casos.append(("las_cinco_son_esas", sorted(tramo),
                  ["LD-OPC05-005", "LD-OPC05-094", "LD-OPC05-100", "LD-OPC05-101",
                   "LD-OPC05-118"]))
    con = [e for e in tramo if marcas_de_relectura(f[e])]
    casos.append(("las_cinco_llevan_alguna_marca_contable", sorted(con), sorted(tramo)))
    ciegas = sorted(e for e in tramo
                    if any(t == "CIEGA_DEL_AUDITOR" for t, _v in marcas_de_relectura(f[e])))
    casos.append(("con_ciega_del_auditor_en_el_registro", ciegas,
                  ["LD-OPC05-005", "LD-OPC05-100"]))
    sin_ciega = sorted(e for e in tramo if e not in ciegas)
    casos.append(("sin_ciega_del_auditor_en_el_registro", sin_ciega,
                  ["LD-OPC05-094", "LD-OPC05-101", "LD-OPC05-118"]))
    casos.append(("la_ciega_162_sella_094", veredicto_sellado_162("LD-OPC05-094"), "D"))
    casos.append(("la_ciega_162_sella_118", veredicto_sellado_162("LD-OPC05-118"), "D"))
    casos.append(("la_ciega_162_sella_101_en_C", veredicto_sellado_162("LD-OPC05-101"), "C"))
    # EL CASO QUE MUERDE LA CEGUERA QUE ESTA TAREA VINO A MEDIR: una lectura que
    # vive SOLO en el fichero sellado NO se vuelve contable por estar sellada.
    casos.append(("el_sello_no_hace_contable_la_ciega_de_094",
                  any(t == "CIEGA_DEL_AUDITOR"
                      for t, _v in marcas_de_relectura(f["LD-OPC05-094"])), False))
    # Y EL QUE MUERDE AL REVES: la marca que 094 SI lleva es la segunda pasada
    # del propio ejecutor, que no es una lectura independiente de otra pluma.
    casos.append(("la_marca_de_094_es_del_ejecutor_no_del_auditor",
                  sorted(t for t, _v in marcas_de_relectura(f["LD-OPC05-094"])),
                  ["TRAMO_AL_DOBLE"]))

    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-46s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("")
    print("   CIFRA casos: %d | pasan: %d | fallan: %d" % (len(casos), len(casos) - fallos, fallos))
    print("")
    print("   SEGUNDA PASADA: SE MUTA EL VALOR ESPERADO Y TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, list):
            mutado = esperado + ["LD-OPC05-999"]
        else:
            mutado = ("D" if esperado == "C" else "C") if esperado in ("C", "D") \
                else str(esperado) + "_MUTADO"
        cae = (real != mutado)
        print("   %-46s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    print("")
    print("   CIFRA casos que CAEN: %d de %d" % (caen, len(casos)))
    if fallos or caen != len(casos):
        print("ROJO: la bateria no se comporta.")
        return 1
    print("VERDE: %d casos, los %d pasan y los %d CAEN al mutarles el valor esperado."
          % (len(casos), len(casos), len(casos)))
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutacion", action="store_true")
    a = ap.parse_args()
    raise SystemExit(prueba_de_mutacion() if a.mutacion else main())
