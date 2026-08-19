# -*- coding: utf-8 -*-
"""Tercer parche de la vuelta 40: la correccion declarada dentro del resumen
generado, para que el lector del .md vea lo mismo que el lector del codigo."""
import io

P = "scripts/costuras_internas.py"
s = io.open(P, encoding="utf-8").read()
n_orig = len(s)

viejo = '''      "la herede**. Detalle entero, con el costo medido, en el encabezado de "
      "`scripts/costuras_internas.py`.")
    A("")
'''
nuevo = '''      "la herede**. Detalle entero, con el costo medido, en el encabezado de "
      "`scripts/costuras_internas.py`.")
    A("")
    A("> **SEGUNDA CORRECCION DECLARADA (19 ago 2026, vuelta 40).** La puerta de "
      "arriba **quedo EN ROJO desde aquella recalibracion**: `plan_mejora_procesos` "
      "daba **43,1 contra 44** y el instrumento **no entregaba nada** (exit 1). **El "
      "roto no era el instrumento: era el fixture.** La propia campaña recorto ese "
      "nodo por una operacion legitima (`OP-F-04-HOR`, commit `2bd8dd76`), que es lo "
      "que lo dejo rancio. **La puerta se reparo cambiandole el fixture, con criterio "
      "escrito, y SIN TOCAR NI UN UMBRAL NI UN NODO**: el retirado se queda declarado "
      "abajo con su motivo. **Lo que la reparacion NO arregla y no se disfraza: la "
      "cola sigue en el 42,3 por ciento del catalogo**, que es el pendiente de "
      "doctrina del `MIN_BLOQUE = 2` y **lo decide el fundador**.")
    A("")
'''
assert s.count(viejo) == 1, "EDIT 8 no ancla"
s = s.replace(viejo, nuevo)

io.open(P, "w", encoding="utf-8", newline="\n").write(s)
print("EDIT 8 aplicado. %d -> %d caracteres" % (n_orig, len(s)))
