# -*- coding: utf-8 -*-
"""caso_positivo_cuenta_agregada.py . EL CASO POSITIVO DE
scripts/loop/cuenta_agregada_de_perdidas.py.

POR QUE EXISTE. La regla del acta 68 dice que toda cuenta agregada se cuente por
maquina y que TODA EXCLUSION VAYA DICHA. La mitad que de verdad importa de ese
instrumento no es la cuenta (esa se ve a ojo), sino LA EXCLUSION: la fila que
DESCRIBE un atenuante en su prosa y NO lleva la frase sellada tiene que quedar
FUERA de la cifra y NOMBRADA aparte. Esa mitad no se ejerce en un lote donde
todas las filas van selladas, y una guarda que nunca se ejerce se pudre en
silencio. Este caso positivo la ejerce a proposito.

QUE PRUEBA, Y LAS TRES MITADES:
  1. QUE CUENTA LO SELLADO: un plan de mentira con TRES perdidas, de las cuales
     DOS llevan la frase ATENUANTE DECLARADO, tiene que dar 2 y no 3.
  2. QUE LA EXCLUSION SE DICE: la tercera DESCRIBE el mecanismo en su prosa (dice
     que la pieza LLEGA ENTERA POR el APPEND del hermano) pero NO lleva la frase
     sellada. Tiene que quedar FUERA de la cuenta y aparecer NOMBRADA bajo LA
     EXCLUSION, DICHA. Es exactamente la fila 5 de la vuelta 69.
  3. QUE LA LECTURA CONTRARIA SE PUBLICA: la fila con DOS SEDES cuenta UNA vez
     (acta 67, D10) y el instrumento tiene que decir cuanto daria la otra lectura.

NO TOCA NI UN NODO NI NINGUN PLAN REAL: escribe su plan de mentira en docs/loop/,
lo corre y lo borra.

Uso: python scripts/loop/caso_positivo_cuenta_agregada.py
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FALSO = os.path.join(RAIZ, "docs", "loop", "_caso_positivo_cuenta_agregada.json")
REL = "docs/loop/_caso_positivo_cuenta_agregada.json"

PLAN = {
    "operacion": "OP-DE-MENTIRA",
    "contrato_de_perdidas": "CAMPO PROPIO v1",
    "actos": [
        {"orden": 1, "superviviente": "nodo_de_mentira", "absorbidos": ["otro_de_mentira"],
         "perdidas": [
             {"especie": "DE PARAMETRO DE PASO",
              "que": ("una pieza cualquiera. ATENUANTE DECLARADO: el paso 2 del superviviente "
                      "ya dice la mitad"),
              "donde": "paso 1 de otro_de_mentira",
              "enrutada_a": "la fase 04"},
             {"especie": "DE CONDICIONES",
              "que": ("otra pieza con DOS sedes. ATENUANTE DECLARADO Y MEDIDO: el INCISO de "
                      "este mismo acto la repone"),
              "donde": "paso 3 de otro_de_mentira y condicion 1 de otro_de_mentira",
              "enrutada_a": "la fase 04"},
             {"especie": "DE PARAMETRO DE PASO",
              "que": ("LA FILA QUE EL CASO POSITIVO PERSIGUE: describe el mecanismo en su "
                      "prosa, porque dice que la mitad de la pieza llega entera por el APPEND "
                      "del hermano, pero NO lleva la frase sellada"),
              "donde": "paso 4 de otro_de_mentira",
              "enrutada_a": "la fase 04"},
         ]},
    ],
}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("CASO POSITIVO DE LA CUENTA AGREGADA DE PERDIDAS")
    print("  la mitad que se prueba es LA EXCLUSION, que un lote sellado entero")
    print("  no ejerce nunca")
    print("=" * 78)
    io.open(FALSO, "w", encoding="utf-8", newline=chr(10)).write(
        json.dumps(PLAN, ensure_ascii=False, indent=2))
    try:
        r = subprocess.run(
            [sys.executable, os.path.join(RAIZ, "scripts", "loop", "cuenta_agregada_de_perdidas.py"),
             "--plan", REL],
            capture_output=True, text=True, encoding="utf-8", cwd=RAIZ)
        salida = r.stdout + r.stderr
    finally:
        if os.path.exists(FALSO):
            os.remove(FALSO)

    print()
    for l in salida.splitlines():
        print("     %s" % l)

    pruebas = [
        ("1. cuenta SOLO lo sellado (2 y no 3)",
         "filas con ATENUANTE DECLARADO      : 2" in salida),
        ("2. la fila SIN la frase sellada NO entra en la cuenta",
         "fila  3" not in salida.split("LA EXCLUSION, DICHA")[0].split(
             "filas con ATENUANTE DECLARADO")[-1].split("de la ESPECIE")[0]),
        ("3. LA EXCLUSION va DICHA y nombra esa fila",
         "LA EXCLUSION, DICHA" in salida
         and "fila  3" in salida.split("LA EXCLUSION, DICHA")[1]),
        ("4. la fila de DOS SEDES cuenta UNA vez y la contraria se publica",
         "filas con DOS SEDES en el campo donde : 1" in salida
         and "seria 4 y no 3" in salida),
        ("5. el total es 3 y no 4",
         "perdidas selladas, en total        : 3" in salida),
    ]
    print()
    print("  LAS MITADES:")
    malas = 0
    for nombre, ok in pruebas:
        print("     %-58s %s" % (nombre, "VERDE" if ok else "ROJO"))
        malas += 0 if ok else 1
    print()
    if malas:
        print("ROJO: %d de %d mitades fallan." % (malas, len(pruebas)))
        return 1
    print("VERDE: LAS %d MITADES MUERDEN. La exclusion se mide, no se cree." % len(pruebas))
    return 0


if __name__ == "__main__":
    sys.exit(main())
