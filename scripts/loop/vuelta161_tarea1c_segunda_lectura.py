# -*- coding: utf-8 -*-
"""vuelta161_tarea1c_segunda_lectura.py . TAREA 1.c DE LA VUELTA 161.

CUENTA LAS SEGUNDAS LECTURAS INDEPENDIENTES DEL REGISTRO
`docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl` POR LA DEFINICION QUE ESTA VUELTA
ESCRIBE EN `docs/plan/BANCO_DEL_PLAN.md`, P.5.2.

POR QUE EXISTE. La deuda la midio el auditor en la parada del 3 sep 2026: *"La
definicion de SEGUNDA LECTURA INDEPENDIENTE no esta escrita en ningun sitio. Yo
mido hoy 120 de 122 con marca de segunda lectura y 82 con dos marcas; el acta
158 publico 84 con otra definicion. No copio esa cifra ni la mia encima de la
suya: LO QUE FALTA ES LA DEFINICION, NO EL NUMERO."*

LAS TRES COSAS QUE LA DEFINICION DICE, Y ESTE INSTRUMENTO LAS COMPUTA LAS TRES:

  (1) QUE MARCA CUENTA. Cuenta la marca escrita en el campo `razon` de la fila
      que dice DOS cosas: que es una RELECTURA (no la lectura que abrio la fila)
      y EN QUE VUELTA se hizo. Las formas literales que el registro trae hoy van
      en FORMAS_QUE_CUENTAN, y las que NO cuentan van en FORMAS_QUE_NO_CUENTAN
      con su motivo: la lectura que ABRE la fila no es una relectura, y una
      edicion de mantenimiento (unificar el campo `cita`, registrar una
      adjudicacion) no vuelve a los nodos.

  (2) QUIEN PUEDE FIRMARLA. La firma la da LA VUELTA, no la persona: cuenta la
      relectura hecha en una vuelta POSTERIOR a la que publico la clase. Pueden
      firmarla las dos plumas. Pero SOLO CUENTA LA QUE DEJA SU MARCA AQUI: una
      lectura que no deja marca en el registro no es contable, y esa es la
      diferencia medida que hace bailar las cifras. Se mide y se publica:
      cuantas razones NOMBRAN al auditor en prosa sin marca contable.

  (3) UNA RELECTURA CONJUNTA CUENTA UNA SOLA VEZ. Se computa metiendo los actos
      en un CONJUNTO de pares (tipo, vuelta): dos marcas del mismo acto sobre la
      misma fila colapsan solas, sin ninguna regla aparte.

LA CIFRA NO SE COPIA DE NADIE. Las dos cifras viejas (el 84 del acta 158 y el 82
del acta 160) se imprimen TACHADAS AL LADO, con su autor, su corte y su linea, y
NINGUNA se escribe encima de la otra (EJECUTOR.md 8).

USO:  python scripts/loop/vuelta161_tarea1c_segunda_lectura.py
"""
import collections
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")

FORMAS_QUE_CUENTAN = [
    # ANADIDA EN LA TAREA 2 DE ESTA MISMA VUELTA, Y SE DECLARA POR QUE: la
    # relectura de las catorce en C escribe su marca con esta forma, y una
    # definicion escrita hoy que no contara la lectura de hoy seria una
    # definicion que nace desfasada. La forma cumple las dos condiciones de
    # P.5.2: dice que es una RELECTURA y dice EN QUE VUELTA.
    (r"RELECTURA DEL TRAMO DE LAS CATORCE EN C, VUELTA (\d+)", "TRAMO_DE_LAS_C"),
    (r"SEGUNDA PASADA DEL TRAMO AL DOBLE, VUELTA (\d+)", "TRAMO_AL_DOBLE"),
    (r"SEGUNDA PASADA DE LA VUELTA (\d+)", "SEGUNDA_PASADA"),
    (r"RELECTURA CONJUNTA DE LA VUELTA (\d+)", "RELECTURA_CONJUNTA"),
    (r"vuelta (\d+), TAREA [^,]*, RELECTURA CONJUNTA", "RELECTURA_CONJUNTA"),
    (r"vuelta (\d+), TAREA [^,]*, RELECTURA POR", "RELECTURA"),
]

FORMAS_QUE_NO_CUENTAN = [
    ("LECTURA DEL LOTE 1 DE LA VUELTA", "es la lectura que ABRE la fila"),
    ("LOTE 1 DE LA VUELTA 157", "es la lectura que ABRE la fila"),
    ("LOTE 2 DE LA VUELTA 159", "es la lectura que ABRE la fila"),
    ("UNIFICACION DEL CAMPO cita", "mantenimiento: no vuelve a los nodos"),
    ("ADJUDICACION 6.", "registro de una adjudicacion: no vuelve a los nodos"),
]

# LAS DOS CIFRAS VIEJAS, CITADAS CON SU LINEA Y NO COPIADAS COMO PROPIAS.
VIEJAS = [
    (84, "acta 158", "auditor", "docs/loop/ACTA_AUDITOR.md:52411",
     "3 sep 2026",
     "cuenta acumulada de segundas lecturas independientes: 65 heredadas de las "
     "actas mas las 19 ciegas del propio auditor de aquella vuelta"),
    (82, "acta 160", "auditor", "docs/loop/ACTA_AUDITOR.md:53172",
     "3 sep 2026",
     "pares cuya razon lleva DOS MARCAS DISTINTAS, contando como marca cualquier "
     "bloque anadido, incluidos los de mantenimiento"),
]


def linea_del_acta(numero):
    """Lee del fichero la linea que la cita nombra, para que la cita vaya con su
    linea leida HOY y no con la que alguien recuerde (EJECUTOR.md 1)."""
    try:
        lineas = io.open(ACTA, encoding="utf-8").read().split("\n")
        return lineas[numero - 1].strip()
    except (IOError, IndexError):
        return "(no se pudo leer)"


def main():
    print("=" * 78)
    print("VUELTA 161, TAREA 1.c: SEGUNDA LECTURA INDEPENDIENTE, CONTADA POR SU")
    print("DEFINICION (banco del plan, P.5.2)")
    print("=" * 78)
    print("")

    filas = [json.loads(l) for l in io.open(REGISTRO, encoding="utf-8") if l.strip()]
    ld = [f for f in filas if f.get("via") == "LECTURA_DIRIGIDA"]
    print("A) EL UNIVERSO, CONTADO DEL FICHERO")
    print("   fuente: docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl")
    print("   CIFRA filas del registro: %d" % len(filas))
    print("   CIFRA filas de LECTURA_DIRIGIDA: %d" % len(ld))
    print("   CIFRA filas de CRIBADO: %d"
          % len([f for f in filas if f.get("via") == "CRIBADO"]))
    print("")

    print("B) LAS FORMAS QUE CUENTAN Y LAS QUE NO, DECLARADAS ANTES DE CONTAR")
    for patron, tipo in FORMAS_QUE_CUENTAN:
        print("   CUENTA    %-20s %s" % (tipo, patron))
    for literal, motivo in FORMAS_QUE_NO_CUENTAN:
        print("   NO CUENTA %-40s %s" % (literal, motivo))
    print("")

    actos_por_fila = {}
    actos_tot = collections.Counter()
    for f in ld:
        actos = set()
        for patron, tipo in FORMAS_QUE_CUENTAN:
            for m in re.finditer(patron, f["razon"]):
                actos.add((tipo, int(m.group(1))))
        actos_por_fila[f["cita"].split(",")[0]] = actos
        for a in actos:
            actos_tot[a] += 1

    dist = collections.Counter(len(a) for a in actos_por_fila.values())
    con_al_menos_una = sum(v for k, v in dist.items() if k >= 1)
    con_dos_o_mas = sum(v for k, v in dist.items() if k >= 2)
    sin_ninguna = dist[0]

    print("C) LOS ACTOS DE RELECTURA, POR TIPO Y VUELTA (regla 3 ya aplicada: el")
    print("   conjunto colapsa dos marcas del mismo acto sobre la misma fila)")
    for (tipo, vuelta), n in sorted(actos_tot.items()):
        print("   %-20s vuelta %-4d %d fila(s)" % (tipo, vuelta, n))
    print("   CIFRA actos distintos (tipo, vuelta): %d" % len(actos_tot))
    print("   CIFRA total de actos sobre filas: %d" % sum(actos_tot.values()))
    print("")

    print("D) LA CIFRA, RECOMPUTADA HOY POR ESTA DEFINICION")
    print("   CIFRA pares de LECTURA_DIRIGIDA: %d" % len(ld))
    print("   CIFRA con AL MENOS UNA segunda lectura independiente: %d"
          % con_al_menos_una)
    print("   CIFRA con DOS O MAS: %d" % con_dos_o_mas)
    print("   CIFRA con NINGUNA: %d" % sin_ninguna)
    print("   reparto por numero de actos:")
    for k in sorted(dist):
        print("      %d acto(s): %d par(es)" % (k, dist[k]))
    print("")

    print("E) LAS DOS CIFRAS VIEJAS, TACHADAS AL LADO Y NO COPIADAS (EJECUTOR.md 8)")
    for valor, acta, autor, cita, corte, que_media in VIEJAS:
        print("   ~~%d~~  autor: %s (%s), corte %s" % (valor, autor, acta, corte))
        print("      cita: %s" % cita)
        print("      linea leida HOY: %s" % linea_del_acta(int(cita.split(":")[-1]))[:150])
        print("      lo que media: %s" % que_media)
    print("   NINGUNA de las dos se borra y NINGUNA se escribe encima de la otra.")
    print("   Y NO MIDEN LO MISMO QUE ESTA: la de hoy cuenta ACTOS DE RELECTURA con")
    print("   marca contable en el registro; la del acta 158 sumaba dos libros (las")
    print("   heredadas de las actas mas las ciegas del auditor); la del acta 160")
    print("   contaba BLOQUES ANADIDOS, que incluyen los de mantenimiento.")
    print("")

    print("F) LO QUE ESTA CIFRA NO VE, MEDIDO Y NO ALEGADO")
    nombran_auditor = [f for f in ld if "auditor" in f["razon"].lower()]
    con_marca = [f for f in nombran_auditor if actos_por_fila[f["cita"].split(",")[0]]]
    print("   CIFRA razones que NOMBRAN al auditor en prosa: %d" % len(nombran_auditor))
    print("   CIFRA de esas que ademas llevan marca contable: %d" % len(con_marca))
    print("   La relectura CIEGA del auditor es una segunda lectura real y no deja")
    print("   marca uniforme aqui: vive en su acta y en docs/loop/_auditor_v*_ciega*.")
    print("   Por eso esta cifra la pierde, y por eso las cifras bailaban. EL REMEDIO")
    print("   QUE LA DEFINICION IMPONE: quien relee, escribe su marca en el registro.")
    print("   Mientras no este escrita, una lectura no es contable, y una cifra que no")
    print("   se puede recomputar de un fichero no es cifra (EJECUTOR.md 2).")
    print("")

    print("G) LOS QUE NO LLEVAN NINGUNA, UNO A UNO Y SIN RESUMIR")
    for cita in sorted(c for c, a in actos_por_fila.items() if not a):
        print("   %s" % cita)
    print("")

    print("H) LA ADITIVIDAD DEL REGISTRO EN ESTA TAREA: ESTE INSTRUMENTO NO ESCRIBE")
    r = subprocess.run(["git", "diff", "--numstat", "--",
                        "docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl"],
                       cwd=RAIZ, capture_output=True, text=True)
    print("   git diff --numstat del registro: %r" % r.stdout.strip())
    print("")
    print("CIFRA PUBLICADA POR LA DEFINICION DE P.5.2: %d de %d"
          % (con_al_menos_una, len(ld)))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
