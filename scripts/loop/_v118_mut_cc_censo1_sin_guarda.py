# -*- coding: utf-8 -*-
r"""vuelta118_tarea2_1_censo_tres_superficies_reparado.py . TAREA 2 de la
vuelta 118 (encargo del auditor, acta de la vuelta 117, caida E.1: "EL CENSO
DE LA TAREA 3.2 CUENTA UNA NEGACION COMO UN SI"). REPARA
vuelta117_tarea3_2_registro_cierre_tres_superficies.py, que es HISTORIA y NO
SE TOCA: este es un fichero NUEVO.

LA CAIDA QUE REPARA. La superficie (C) de aquel censo buscaba la subcadena
"REGISTRO DE OPERACION HECHA" con `if FRASE_C in l` y publicaba SI para
OP-D-07 citando docs/plan/02_DESTEJIDOS.md:4461, cuya linea real dice, literal,
"Por eso este registro NO dice `REGISTRO DE OPERACION HECHA`.": una negacion,
no una afirmacion. El instrumento imprimia el ENCABEZADO atribuido, nunca la
linea casada: si la hubiera pegado, la negacion habria saltado sola.

EL REMEDIO, EN TRES PIEZAS (TAREA 2.1/2.2/2.3 del encargo de la 118).
(2.1) EL CRITERIO SE IMPRIME EN LA SALIDA: FRASE_A, PALABRAS_CIERRE_B y
FRASE_C, mas MARCAS_NEGACION, se imprimen con %s desde las constantes, nunca
tecleados en prosa aparte.
(2.2) LA LINEA CASADA SE PEGA ENTERA: para cada SI de cualquier superficie, se
pega la linea (o, para la superficie A, el renglon de OPERACIONES.jsonl con su
numero) que caso, ademas del encabezado o cita a la que se atribuye.
(2.3) LA NEGACION NO CUENTA COMO SI: si una marca de negacion de
MARCAS_NEGACION aparece en la ventana de texto INMEDIATAMENTE ANTERIOR al
patron casado (dentro de la misma linea), la superficie no cuenta como SI: se
publica como DESCARTADA POR NEGACION, con la linea completa delante.

MUTACION CC (scripts/loop/vuelta118_tarea2_5_mutacion_cc.py) prueba el
remedio (2.3) por el LADO ROJO: una copia de este fichero SIN la guarda de
negacion tiene que volver a dar SI en OP-D-07 superficie (C).

USO:
  python scripts/loop/vuelta118_tarea2_1_censo_tres_superficies_reparado.py
"""
import json
import re

RUTA_OPS = "docs/plan/OPERACIONES.jsonl"
DEPENDENCIAS = [
    ("OP-D-01", "docs/plan/02_DESTEJIDOS.md"),
    ("OP-D-02", "docs/plan/02_DESTEJIDOS.md"),
    ("OP-D-03", "docs/plan/02_DESTEJIDOS.md"),
    ("OP-D-04", "docs/plan/02_DESTEJIDOS.md"),
    ("OP-D-05", "docs/plan/02_DESTEJIDOS.md"),
    ("OP-D-06", "docs/plan/02_DESTEJIDOS.md"),
    ("OP-D-07", "docs/plan/02_DESTEJIDOS.md"),
    ("OP-F-02", "docs/plan/01_FUENTES.md"),
    ("OP-F-03", "docs/plan/01_FUENTES.md"),
]
FRASE_A = "REGISTRO DE CIERRE"
FRASE_C = "REGISTRO DE OPERACION HECHA"
PALABRAS_CIERRE_B = ("CERRADA", "SELLADA", "EJECUTADA ENTERA")
# MARCAS_NEGACION (TAREA 2.3 del encargo, declaradas EXACTAS como el encargo
# las nombra: "NO dice", "no dice", "NO lleva", "sin"). Se comparan en
# minusculas contra una ventana de texto anterior al patron, asi que "NO dice"
# y "no dice" son la MISMA marca ("no dice") comparada sin distinguir mayus/minus.
MARCAS_NEGACION = ("no dice", "no lleva", "sin")
VENTANA_NEGACION = 40


def cargar_ops_con_linea():
    """Devuelve {id_op: (dict, numero_de_linea_1_indexado)} de OPERACIONES.jsonl,
    para poder pegar la linea entera cuando la superficie A casa (TAREA 2.2)."""
    out = {}
    with open(RUTA_OPS, encoding="utf-8") as f:
        for i, l in enumerate(f, start=1):
            if not l.strip():
                continue
            o = json.loads(l)
            out[o["id_op"]] = (o, i, l.rstrip("\n"))
    return out


def cargar_lineas(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.readlines()


def encabezados(lineas):
    out = []
    for i, l in enumerate(lineas, start=1):
        if re.match(r"^#{1,4}\s", l):
            out.append((i, l.rstrip("\n")))
    return out


SEPARADORES_DE_ORACION = (". ", ".\n", "! ", "? ")


def negacion_delante(texto, idx):
    """MUTACION CC: guarda de negacion DESACTIVADA a proposito, sin tocar nada mas."""
    return None

    contexto = texto[max(0, idx - VENTANA_NEGACION):idx]
    for sep in SEPARADORES_DE_ORACION:
        pos = contexto.rfind(sep)
        if pos != -1:
            contexto = contexto[pos + len(sep):]
    contexto = contexto.lower()
    for marca in MARCAS_NEGACION:
        if marca in contexto:
            return marca
    return None


def superficie_a_nota(oid, by_id):
    o, num, linea_jsonl = by_id.get(oid, (None, None, None))
    nota = (o.get("nota") or "") if o else ""
    idx = nota.find(FRASE_A)
    if idx == -1:
        return {"si": False}
    neg = negacion_delante(nota, idx)
    fragmento = nota[max(0, idx - VENTANA_NEGACION):idx + 300].strip()
    if neg:
        return {"si": False, "descartada_por_negacion": neg, "linea": linea_jsonl,
                "num": num, "fragmento": fragmento}
    return {"si": True, "linea": linea_jsonl, "num": num, "fragmento": fragmento}


def superficie_b_encabezado(oid, ruta_pagina, lineas_encab):
    hallados = []
    descartadas = []
    for num, texto in lineas_encab:
        if oid not in texto:
            continue
        for p in PALABRAS_CIERRE_B:
            idx = texto.find(p)
            if idx == -1:
                continue
            neg = negacion_delante(texto, idx)
            if neg:
                descartadas.append((num, texto, neg))
            else:
                hallados.append((num, texto))
            break
    return hallados, descartadas


def superficie_c_frase_operacion_hecha(oid, ruta_pagina, lineas, lineas_encab):
    hallados = []
    descartadas = []
    for i, l in enumerate(lineas, start=1):
        idx = l.find(FRASE_C)
        if idx == -1:
            continue
        candidatos = [h for h in lineas_encab if h[0] <= i]
        encab = candidatos[-1] if candidatos else None
        if not (encab and oid in encab[1]):
            continue
        neg = negacion_delante(l, idx)
        if neg:
            descartadas.append((i, l.rstrip("\n"), encab, neg))
        else:
            hallados.append((i, l.rstrip("\n"), encab))
    return hallados, descartadas


def main():
    by_id = cargar_ops_con_linea()
    print("REGISTRO DE CIERRE EN TRES SUPERFICIES, REPARADO, TAREA 2 VUELTA 118.")
    print("=" * 100)
    print("CRITERIO IMPRESO (TAREA 2.1):")
    print("  (A) campo `nota` de %s -- frase %r" % (RUTA_OPS, FRASE_A))
    print("  (B) encabezado de seccion en la pagina de la fase -- cita el id Y una palabra de %s" % (PALABRAS_CIERRE_B,))
    print("  (C) frase literal %r en la pagina de la fase, atribuida al encabezado mas cercano por arriba" % FRASE_C)
    print("  MARCAS_NEGACION (TAREA 2.3, comparadas en minusculas, ventana de %d caracteres antes del patron): %s"
          % (VENTANA_NEGACION, MARCAS_NEGACION))
    print()

    cache_lineas = {}
    cache_encabezados = {}
    resumen = {}

    for oid, ruta_pagina in DEPENDENCIAS:
        if ruta_pagina not in cache_lineas:
            cache_lineas[ruta_pagina] = cargar_lineas(ruta_pagina)
            cache_encabezados[ruta_pagina] = encabezados(cache_lineas[ruta_pagina])
        lineas = cache_lineas[ruta_pagina]
        lineas_encab = cache_encabezados[ruta_pagina]

        print("--- %s (pagina %s) ---" % (oid, ruta_pagina))

        a = superficie_a_nota(oid, by_id)
        if a["si"]:
            print("(A) nota: SI -- %s:%d -- %s" % (RUTA_OPS, a["num"], a["fragmento"]))
        elif a.get("descartada_por_negacion"):
            print("(A) nota: DESCARTADA POR NEGACION (marca %r) -- %s:%d -- %s"
                  % (a["descartada_por_negacion"], RUTA_OPS, a["num"], a["fragmento"]))
        else:
            print("(A) nota: NO")

        b, b_desc = superficie_b_encabezado(oid, ruta_pagina, lineas_encab)
        if b:
            print("(B) encabezado: SI, %d cita(s):" % len(b))
            for num, texto in b:
                print("    %s:%d -- %s" % (ruta_pagina, num, texto.strip()))
        else:
            print("(B) encabezado: NO")
        for num, texto, neg in b_desc:
            print("    DESCARTADA POR NEGACION (marca %r): %s:%d -- %s" % (neg, ruta_pagina, num, texto.strip()))

        c, c_desc = superficie_c_frase_operacion_hecha(oid, ruta_pagina, lineas, lineas_encab)
        if c:
            print("(C) frase %r: SI, %d cita(s):" % (FRASE_C, len(c)))
            for num_frase, texto_linea, encab in c:
                print("    %s:%d -- %s  (bajo encabezado %s:%d -- %s)"
                      % (ruta_pagina, num_frase, texto_linea.strip(), ruta_pagina, encab[0], encab[1].strip()))
        else:
            print("(C) frase %r: NO" % FRASE_C)
        for num_frase, texto_linea, encab, neg in c_desc:
            print("    DESCARTADA POR NEGACION (marca %r): %s:%d -- %s  (bajo encabezado %s:%d -- %s)"
                  % (neg, ruta_pagina, num_frase, texto_linea.strip(), ruta_pagina, encab[0], encab[1].strip()))

        resumen[oid] = {"A": a["si"], "B": bool(b), "C": bool(c)}
        print()

    print("--- RESUMEN, alguna de las tres superficies ---")
    con_alguna = [oid for oid, r in resumen.items() if any(r.values())]
    sin_ninguna = [oid for oid, r in resumen.items() if not any(r.values())]
    print("con AL MENOS UNA superficie de registro de cierre: %d de %d: %s"
          % (len(con_alguna), len(resumen), con_alguna))
    print("SIN NINGUNA superficie de registro de cierre: %d: %s" % (len(sin_ninguna), sin_ninguna))
    print()
    print("| operacion | (A) nota | (B) encabezado | (C) frase OPERACION HECHA |")
    print("|---|---|---|---|")
    for oid, _ruta in DEPENDENCIAS:
        r = resumen[oid]
        print("| %s | %s | %s | %s |" % (oid, "SI" if r["A"] else "NO",
                                          "SI" if r["B"] else "NO", "SI" if r["C"] else "NO"))


if __name__ == "__main__":
    main()
