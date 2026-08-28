# -*- coding: utf-8 -*-
r"""vuelta118_tarea4_1_guardas_fase0.py . TAREA 4.1 de la vuelta 118, LA
GUARDA DE ENTRADA DE LA FASE 05 (BLOQUEANTE Y PRIMERO).

QUE MIDE, SOLO LECTURA. Talla, de docs/plan/FASE_0_CODIGO.md, los
encabezados `## \`OP-C-0N\`: <titulo> . **<estado>**` (patron citado, no
tecleado a mano): son las guardas NOMBRADAS DE ESA PAGINA, no de memoria de
nadie. Imprime cuantas hay y sus nombres/estado.

NO ADJUDICA si la fase 0 esta HECHA: solo cuenta y nombra las guardas de la
pagina. La verificacion de "pasa hoy en verde" y "tiene caso positivo
localizable" para cada una se hace aparte (motor/tsc para las de codigo
TypeScript, Gate 0 para OP-C-04, y el instrumento propio para OP-C-05) y se
declara en el reporte con su cita, no en este tallador.

USO:
  python scripts/loop/vuelta118_tarea4_1_guardas_fase0.py
"""
import re

RUTA = "docs/plan/FASE_0_CODIGO.md"
PATRON = re.compile(r"^## `(OP-C-0\d)`: (.+?) \. \*\*(\w+)\*\*\s*$")


def main():
    lineas = open(RUTA, encoding="utf-8").readlines()
    hallados = []
    for i, l in enumerate(lineas, start=1):
        m = PATRON.match(l.rstrip("\n"))
        if m:
            hallados.append((i, m.group(1), m.group(2), m.group(3)))

    print("GUARDAS NOMBRADAS EN %s, patron %r" % (RUTA, PATRON.pattern))
    print("=" * 100)
    print("total: %d" % len(hallados))
    for num, oid, titulo, estado in hallados:
        print("  %s:%d -- %s: %s . %s" % (RUTA, num, oid, titulo, estado))

    if len(hallados) != 5:
        print()
        print("ALERTA: NO SON CINCO (%d). PARA Y TRAE ESTO, no se adjudica." % len(hallados))
        return 1
    print()
    print("CINCO guardas confirmadas por el tallador: %s" % ", ".join(h[1] for h in hallados))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
