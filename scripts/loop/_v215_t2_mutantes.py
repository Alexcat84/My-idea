# -*- coding: utf-8 -*-
r"""_v215_t2_mutantes.py . LA PRUEBA DE MUTACION DE LA GUARDA QUE ME FALTO EN EL
TRAMO 3.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

POR QUE EXISTE, Y ES MI PROPIA CAIDA. EJECUTOR.md 1 dice que ninguna guarda se
publica como prueba sin haber corrido antes su prueba de mutacion. La primera
version de _v215_mensaje_tramo.py llevaba la frase "y ninguno cae" CLAVADA en el
texto, al lado de cifras que si se leian: en los tramos 1 y 2 coincidieron y en
el 3 el medidor leyo NO MORDIO 1 mientras la prosa seguia diciendo que ninguno
cae. La guarda nueva compara LA PROSA CONTRA SUS PROPIAS CIFRAS, y esto es lo
que comprueba que muerde.

QUE MUTA: las cifras de fallo que frase_de_la_caida() recibe. Cada mutante es un
reparto distinto, y se exige que la frase DIGA lo que las cifras dicen.

USO:  python scripts/loop/_v215_t2_mutantes.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _v215_mensaje_tramo as M  # noqa: E402

CASOS = [
    ("A. LOS TRES EN CERO, QUE ES EL TRAMO 1 Y EL 2",
     {"ancla": "0", "no_mordio": "0", "no_repro": "0"}, 0, True),
    ("B. NO MORDIO 1, QUE ES EXACTAMENTE EL TRAMO 3 QUE ME CAZO",
     {"ancla": "0", "no_mordio": "1", "no_repro": "0"}, 1, False),
    ("C. ANCLA PERDIDA 1",
     {"ancla": "1", "no_mordio": "0", "no_repro": "0"}, 1, False),
    ("D. NO REPRODUCIBLE 1",
     {"ancla": "0", "no_mordio": "0", "no_repro": "1"}, 1, False),
    ("E. LOS TRES A LA VEZ, QUE TIENEN QUE SUMAR Y NO CONTARSE UNO SOLO",
     {"ancla": "2", "no_mordio": "3", "no_repro": "4"}, 9, False),
]


def main():
    fallos = 0
    for nombre, D, caidos_esperados, dice_ninguno_esperado in CASOS:
        caidos, frase = M.frase_de_la_caida(D)
        dice = "ninguno cae" in frase
        ok = (caidos == caidos_esperados and dice == dice_ninguno_esperado)
        print("CASO %s" % nombre)
        print("   CIFRA caidos computados: %d | CIFRA esperados: %d"
              % (caidos, caidos_esperados))
        print("   la frase dice 'ninguno cae': %s | se esperaba: %s"
              % ("SI" if dice else "NO", "SI" if dice_ninguno_esperado else "NO"))
        print("   frase: %s" % frase[:110])
        print("   VEREDICTO: %s" % ("CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos += 1
    print("")
    print("CIFRA casos: %d | CIFRA que NO calzan: %d" % (len(CASOS), fallos))
    print("Y LA CIFRA QUE DE VERDAD IMPORTA: casos con caidos distinto de cero "
          "en los que la frase AUN diria 'ninguno cae': %d (se exige 0)"
          % len([1 for _, D, c, _ in CASOS
                 if c != 0 and "ninguno cae" in M.frase_de_la_caida(D)[1]]))
    if fallos:
        print("ROJO: la guarda no dice lo que sus cifras dicen.")
        return 1
    print("VERDE: la frase se computa de las cifras y ninguna combinacion "
          "publica que no cae nadie cuando cae alguien.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
