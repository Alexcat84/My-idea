# -*- coding: utf-8 -*-
"""Parche 9: el barrido publica la VITALIDAD DE LOS PATRONES DE CONTENIDO, que
es la pierna que la vuelta 147 anadio: una pierna por contenido de nombres que
nadie escribio nunca no puede respaldar una ausencia. Trabajo, no instrumento."""
import io
p = "scripts/loop/vuelta165_tarea5_estado_nuevo.py"
s = io.open(p, encoding="utf-8").read()
a = '''    print("  NO DECODIFICABLES (mirados y no leidos, NO cuentan como sin "
          "coincidencia): %d" % no_leidos)'''
b = '''    print("  VITALIDAD DE LOS PATRONES DE CONTENIDO: %d de %d alternativas "
          "aparecen en el universo" % (1 if por_contenido else 0, 1))
    print("      %-46s -> %-6d %s"
          % (marca, len(por_contenido), "viva" if por_contenido else "MUERTA"))
    print("  NO DECODIFICABLES (mirados y no leidos, NO cuentan como sin "
          "coincidencia): %d" % no_leidos)'''
assert a in s
s = s.replace(a, b, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("parche 9 aplicado")
