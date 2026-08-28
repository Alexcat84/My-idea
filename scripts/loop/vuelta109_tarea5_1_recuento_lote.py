# -*- coding: utf-8 -*-
"""vuelta109_tarea5_1_recuento_lote.py . TAREA 5.1 de la vuelta 109.

Recuenta, ANTES de correr nada mas, los puestos que alguna vez recibieron un
veredicto SATELITE en cualquiera de los seis ficheros de
verificar_cobertura_bolsa_tres_vias.FICHEROS_VEREDICTO (reusada, no
retecleada) y que siguen RESUELTA vivos hoy (verificar_cobertura_bolsa_tres_vias.vivas_de_hoy,
la misma fuente que contar_cierre_efectivo.cifras). El encargo (PROMPT_SIGUIENTE.md,
5.1) cita 6 puestos (87, 91, 109, 123, 145, 154) contados por el auditor: este
script es la medicion independiente, para declarar coincidencia o discrepancia
en vez de copiar la cifra.

USO: python scripts/loop/vuelta109_tarea5_1_recuento_lote.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import verificar_vuelco_de_veredicto as v  # noqa: E402
import verificar_cobertura_bolsa_tres_vias as c  # noqa: E402


def main():
    fallos = []
    lados = v.leer_ficheros(v.FICHEROS_VEREDICTO, None, fallos)
    if fallos:
        print("ROJO:", fallos)
        return 1

    historia = {}
    for nombre, vuelta, _texto, veredictos in lados:
        for puesto, veredicto in veredictos.items():
            historia.setdefault(puesto, []).append((nombre, vuelta, veredicto))

    alguna_vez_satelite = sorted(p for p, h in historia.items() if any(x[2] == "SATELITE" for x in h))
    print("puestos que alguna vez fueron SATELITE en algun barrido (%d): %s"
          % (len(alguna_vez_satelite), alguna_vez_satelite))

    fallos_vivas = []
    vivas = c.vivas_de_hoy(fallos_vivas)
    if fallos_vivas:
        print("ROJO (vivas_de_hoy):", fallos_vivas)
        return 1

    lote = sorted(p for p in alguna_vez_satelite if p in vivas)
    print("LOTE (alguna vez SATELITE Y sigue RESUELTA/vivo hoy, %d): %s" % (len(lote), lote))

    esperado = [87, 91, 109, 123, 145, 154]
    if lote == esperado:
        print("\nCALZA con la cifra del auditor (PROMPT_SIGUIENTE.md, 5.1): %s" % esperado)
    else:
        print("\nDISCREPANCIA DECLARADA contra la cifra del auditor (%s): mi recuento da %s"
              % (esperado, lote))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
