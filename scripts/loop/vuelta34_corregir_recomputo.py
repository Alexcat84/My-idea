# -*- coding: utf-8 -*-
"""vuelta34_corregir_recomputo.py - las celdas de RECOMPUTO_3388.md que el volteo
de la vuelta 34 envejece, corregidas SIN BORRAR la cifra vieja (regla 8).

Cada sustitucion lleva su vieja tachada dentro. El script ABORTA si alguna celda
no esta tal cual se espera: prefiere no tocar nada a tocar la linea equivocada.

Uso: python scripts/loop/vuelta34_corregir_recomputo.py [--aplicar]
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388.md")

CAMBIOS = [
    ("| A crudas en el archivo (`clase == 'A'`), corte 3.388 | ~~**583**~~ **582** "
     "**[CORREGIDA 15 ago 2026, ver la correccion declarada al principio del documento]** |",
     "| A crudas en el archivo (`clase == 'A'`), corte 3.388 | ~~**583**~~ ~~**582**~~ **581** "
     "**[CORREGIDA DOS VECES el 15 ago 2026, ver las correcciones declaradas al principio del "
     "documento]** |"),
    ("| pares distintos en el retrato tras resolver y deduplicar | ~~**583**~~ **582** "
     "**[CORREGIDA 15 ago 2026, ver la correccion declarada al principio del documento]** |",
     "| pares distintos en el retrato tras resolver y deduplicar | ~~**583**~~ ~~**582**~~ "
     "**580** **[CORREGIDA DOS VECES el 15 ago 2026, ver las correcciones declaradas al "
     "principio del documento]** |"),
    ("| **total** | **3.388** | ~~**583**~~ **582** | **17,2 %** |",
     "| **total** | **3.388** | ~~**583**~~ ~~**582**~~ **581** | ~~**17,2 %**~~ **17,1 %** |"),
    ("| A crudas en el archivo | **583** | **582** | **menos 1** |",
     "| A crudas en el archivo | **583** | ~~**582**~~ **581** al cierre de la vuelta 34 | "
     "**menos 2** |"),
    ("| **ii** | A vigentes resueltas del retrato (~~583~~ **582**) == suma de aristas A "
     "internas de las componentes (~~583~~ **582**) | **OK**, recomprobado el 15 ago 2026 con "
     "las cifras nuevas |",
     "| **ii** | A vigentes resueltas del retrato (~~583~~ ~~582~~ **580**) == suma de aristas A "
     "internas de las componentes (~~583~~ ~~582~~ **580**) | **OK**, recomprobado el 15 ago "
     "2026 con las cifras nuevas, DOS veces |"),
    ("| **A / B / C / D** | ~~**583 / 89 / 7 / 2.709**~~ **582 / 87 / 8 / 2.711** "
     "**[CORREGIDA 15 ago 2026, ver la correccion declarada al principio del documento]** |",
     "| **A / B / C / D** | ~~**583 / 89 / 7 / 2.709**~~ ~~**582 / 87 / 8 / 2.711**~~ "
     "**581 / 83 / 8 / 2.716** **[CORREGIDA VARIAS VECES el 15 ago 2026, ver las correcciones "
     "declaradas al principio del documento]** |"),
    ("| **A / B / C / D** | ~~**583 / 89 / 7 / 2.709**~~ **582 / 87 / 8 / 2.711** "
     "(17,2 / 2,6 / 0,2 / 80,0 por ciento) **[CORREGIDA 15 ago 2026, ver la correccion declarada "
     "al principio del documento]** |",
     "| **A / B / C / D** | ~~**583 / 89 / 7 / 2.709**~~ ~~**582 / 87 / 8 / 2.711**~~ "
     "**581 / 83 / 8 / 2.716** (17,1 / 2,4 / 0,2 / 80,2 por ciento) **[CORREGIDA VARIAS VECES el "
     "15 ago 2026, ver las correcciones declaradas al principio del documento]** |"),
]


def main():
    aplicar = "--aplicar" in sys.argv
    s = io.open(P, encoding="utf-8").read()
    faltan = [v for v, _n in CAMBIOS if v not in s]
    if faltan:
        print("ABORTA: %d celda(s) no estan tal cual se esperaban. No se toca nada." % len(faltan))
        for v in faltan:
            print("  falta: %s" % v[:110])
        return 1
    for viejo, nuevo in CAMBIOS:
        print("  OK  %s" % viejo[:96])
        s = s.replace(viejo, nuevo, 1)
    if not aplicar:
        print("\n(simulacion: sin --aplicar no se escribe nada)")
        return 0
    io.open(P, "w", encoding="utf-8").write(s)
    print("\nESCRITO: %d celdas corregidas con su cifra vieja tachada dentro" % len(CAMBIOS))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
