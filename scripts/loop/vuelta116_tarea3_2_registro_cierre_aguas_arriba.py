# -*- coding: utf-8 -*-
r"""vuelta116_tarea3_2_registro_cierre_aguas_arriba.py . TAREA 3.2 de la
vuelta 116, encargo del auditor (acta de la vuelta 115).

QUE MIDE, SOLO LECTURA, CERO ADJUDICACION. Para las NUEVE dependencias de
aguas arriba de OP-E-06 / OP-E-07 (OP-D-01 a OP-D-07 de la fase
02_DESTEJIDOS, y OP-F-02 y OP-F-03 de la fase 01), lee el campo `nota`
ENTERO de docs/plan/OPERACIONES.jsonl y publica, para cada una, SI trae o NO
trae la frase literal "REGISTRO DE CIERRE" (el patron ya visto en OP-D-07,
citado por el auditor). Cuando la trae, publica la CITA LITERAL completa
(desde la frase hasta el punto que cierra la primera oracion larga) con su
fecha y su vuelta, leidas del propio texto.

NO ADJUDICA NADA: no decide si el registro encontrado BLOQUEA o no bloquea
la cadena OP-E-06 / OP-E-07. Esa es la adjudicacion del auditor en la 117.

USO:
  python scripts/loop/vuelta116_tarea3_2_registro_cierre_aguas_arriba.py
"""
import json
import re

RUTA_OPS = "docs/plan/OPERACIONES.jsonl"
DEPENDENCIAS = ["OP-D-01", "OP-D-02", "OP-D-03", "OP-D-04", "OP-D-05", "OP-D-06", "OP-D-07",
                "OP-F-02", "OP-F-03"]
FRASE = "REGISTRO DE CIERRE"


def cargar():
    ops = [json.loads(l) for l in open(RUTA_OPS, encoding="utf-8") if l.strip()]
    return {o["id_op"]: o for o in ops}


def citar(nota, idx):
    """Corta desde la frase hasta el final de la PRIMERA oracion larga (hasta
    el segundo punto seguido de mayuscula o salto de sentido), sin exceder
    600 caracteres, para que la cita sea leible y no arrastre todo el campo."""
    fragmento = nota[idx:idx + 600]
    # corta en el ultimo punto antes del limite si hay uno razonable
    corte = fragmento.rfind(". ")
    if corte > 200:
        fragmento = fragmento[:corte + 1]
    return fragmento.strip()


def main():
    by_id = cargar()
    print("REGISTRO DE CIERRE EN LAS NUEVE DEPENDENCIAS DE AGUAS ARRIBA, TAREA 3.2 VUELTA 116.")
    print("=" * 100)
    print("Fuente: %s, campo `nota` (leido entero, buscando la frase literal %r)." % (RUTA_OPS, FRASE))
    print()

    con_registro = []
    sin_registro = []

    for oid in DEPENDENCIAS:
        o = by_id.get(oid)
        nota = (o.get("nota") or "") if o else ""
        fase = o.get("fase") if o else "?"
        idx = nota.find(FRASE)
        print("%s (fase %s)" % (oid, fase))
        if idx == -1:
            print("  NO trae %r." % FRASE)
            sin_registro.append(oid)
        else:
            cita = citar(nota, idx)
            m = re.search(r"(\d{1,2} \w+ 2026)\s*\(vuelta (\d+)\)", cita)
            fecha_vuelta = "fecha/vuelta: %s, vuelta %s" % (m.group(1), m.group(2)) if m else "fecha/vuelta: NO PARSEADA DEL TEXTO"
            print("  SI trae %r. %s" % (FRASE, fecha_vuelta))
            print("  CITA LITERAL: \"%s\"" % cita)
            con_registro.append(oid)
        print()

    print("RESUMEN: %d de %d traen %r escrito: %s" % (len(con_registro), len(DEPENDENCIAS), FRASE, con_registro))
    print("Las otras %d NO la traen: %s" % (len(sin_registro), sin_registro))


if __name__ == "__main__":
    main()
