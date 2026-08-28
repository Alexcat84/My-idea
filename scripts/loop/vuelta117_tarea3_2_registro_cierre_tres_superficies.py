# -*- coding: utf-8 -*-
r"""vuelta117_tarea3_2_registro_cierre_tres_superficies.py . TAREA 3.2 de la
vuelta 117, encargo del auditor (acta de la vuelta 116, adjudicacion (1): "EL
REGISTRO DE CIERRE CUENTA VIVA DONDE VIVA DENTRO DE docs/plan/, con su cita
localizada").

QUE MIDE, SOLO LECTURA, CERO ADJUDICACION. Para las NUEVE dependencias de
aguas arriba de OP-E-06 / OP-E-07 (OP-D-01 a OP-D-07 de docs/plan/02_DESTEJIDOS.md,
y OP-F-02 y OP-F-03 de docs/plan/01_FUENTES.md), publica, en TRES SUPERFICIES
DISTINTAS, si cada una trae registro de cierre, y CON QUE CITA:

  (A) EL CAMPO `nota` de docs/plan/OPERACIONES.jsonl: busca la frase literal
      "REGISTRO DE CIERRE" (extension de vuelta116_tarea3_2_registro_cierre_aguas_arriba.py,
      que ya media esta superficie sola).
  (B) ENCABEZADO DE SECCION en la pagina de su fase: lineas que empiezan por
      `#` o `##` (markdown), CITAN el id de la operacion Y contienen una
      palabra de cierre (CERRADA, SELLADA, o "EJECUTADA ENTERA").
  (C) LA FRASE LITERAL "REGISTRO DE OPERACION HECHA" en la pagina de su
      fase: para CADA aparicion de la frase, se busca el ENCABEZADO MAS
      CERCANO POR ARRIBA (la seccion que la contiene) y se comprueba si ESE
      encabezado nombra el id de la operacion.

Todas las lineas se miden HOY, con `grep`-equivalente en Python sobre el
fichero de la fase: NINGUNA linea se copia de un acta vieja (EJECUTOR.md,
"LA IDENTIDAD SE LEE DE GIT" / "EL INSTRUMENTO MANDA").

NO ADJUDICA NADA: no decide si el registro encontrado BLOQUEA o no bloquea
la cadena. Esa es la adjudicacion del auditor.

USO:
  python scripts/loop/vuelta117_tarea3_2_registro_cierre_tres_superficies.py
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
PALABRAS_CIERRE = ("CERRADA", "SELLADA", "EJECUTADA ENTERA")


def cargar_ops():
    ops = [json.loads(l) for l in open(RUTA_OPS, encoding="utf-8") if l.strip()]
    return {o["id_op"]: o for o in ops}


def cargar_lineas(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.readlines()


def superficie_a_nota(oid, by_id):
    o = by_id.get(oid)
    nota = (o.get("nota") or "") if o else ""
    idx = nota.find(FRASE_A)
    if idx == -1:
        return None
    fragmento = nota[idx:idx + 300].strip()
    return fragmento


def encabezados(lineas):
    """Todas las lineas que son encabezado markdown (# o ##), con su numero
    de linea (1-indexado, como grep -n)."""
    out = []
    for i, l in enumerate(lineas, start=1):
        if re.match(r"^#{1,4}\s", l):
            out.append((i, l.rstrip("\n")))
    return out


def superficie_b_encabezado(oid, lineas_encabezado):
    hallados = []
    for num, texto in lineas_encabezado:
        if oid in texto and any(p in texto for p in PALABRAS_CIERRE):
            hallados.append((num, texto))
    return hallados


def superficie_c_frase_operacion_hecha(oid, lineas, lineas_encabezado):
    hallados = []
    for i, l in enumerate(lineas, start=1):
        if FRASE_C in l:
            # encabezado mas cercano POR ARRIBA (grep -n de todos los
            # encabezados, se toma el ultimo con numero <= i)
            candidatos = [h for h in lineas_encabezado if h[0] <= i]
            encab = candidatos[-1] if candidatos else None
            if encab and oid in encab[1]:
                hallados.append((i, encab[0], encab[1]))
    return hallados


def main():
    by_id = cargar_ops()
    print("REGISTRO DE CIERRE EN TRES SUPERFICIES, TAREA 3.2 VUELTA 117.")
    print("=" * 100)
    print("(A) campo `nota` de %s -- frase %r" % (RUTA_OPS, FRASE_A))
    print("(B) encabezado de seccion en la pagina de la fase -- cita el id Y una palabra de cierre %s" % (PALABRAS_CIERRE,))
    print("(C) frase literal %r en la pagina de la fase, atribuida al encabezado mas cercano por arriba" % FRASE_C)
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
        print("(A) nota: %s" % ("SI -- \"%s\"" % a if a else "NO"))

        b = superficie_b_encabezado(oid, lineas_encab)
        if b:
            print("(B) encabezado: SI, %d cita(s):" % len(b))
            for num, texto in b:
                print("    %s:%d -- %s" % (ruta_pagina, num, texto.strip()))
        else:
            print("(B) encabezado: NO")

        c = superficie_c_frase_operacion_hecha(oid, lineas, lineas_encab)
        if c:
            print("(C) frase %r: SI, %d cita(s):" % (FRASE_C, len(c)))
            for num_frase, num_encab, texto_encab in c:
                print("    %s:%d (bajo encabezado %s:%d -- %s)"
                      % (ruta_pagina, num_frase, ruta_pagina, num_encab, texto_encab.strip()))
        else:
            print("(C) frase %r: NO" % FRASE_C)

        resumen[oid] = {"A": bool(a), "B": bool(b), "C": bool(c)}
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
