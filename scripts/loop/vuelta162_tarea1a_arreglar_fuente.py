# -*- coding: utf-8 -*-
r"""vuelta162_tarea1a_arreglar_fuente.py . TAREA 1.a de la vuelta 162.

ARREGLA LA CAUSA EN LA FUENTE, que es lo que el encargo pide con esas palabras:
`scripts/loop/vuelta161_tarea1_0_registros.py` llevaba el ultimo numero de la
serie TECLEADO en su cabecera y en su constante `MARCA`, y su idempotencia
miraba UN SOLO fichero. Las dos cosas juntas son la caida de la `R.29`.

QUE CAMBIA, Y TODO POR ADICION CON LO VIEJO TACHADO Y LEGIBLE:
  (i)   la frase tecleada de la cabecera queda tachada y con su correccion al lado;
  (ii)  `MARCA` deja de ser el titulo con el numero dentro y pasa a ser el
        TITULO SIN NUMERO, que es lo unico estable;
  (iii) la idempotencia pasa por `scripts/loop/serie_de_registros.py` y mira LAS
        DOS SEDES;
  (iv)  el numero se COMPUTA con `siguiente_libre()` en vez de venir en el texto.

Parche de una sola pasada, con anclas literales: si un ancla no aparece
exactamente una vez, PARA sin escribir.

USO:  python scripts/loop/vuelta162_tarea1a_arreglar_fuente.py
"""
import io

RUTA = "scripts/loop/vuelta161_tarea1_0_registros.py"

ANCLA_CABECERA = '''LA SEDE, ELEGIDA Y DECLARADA EN VEZ DE SUPUESTA. Va a `docs/PENDIENTES.md` como
entrada `R.29`, que es la forma que la casa ya usa desde `R.9`: "Registro de
correcciones y adjudicaciones declaradas de la vuelta N", con la ultima escrita
siendo `R.28` (vuelta 146, escrita en la 147, TAREA 1.a). Es el unico sitio del
repo donde las caidas y las adjudicaciones de una vuelta se registran como
REGISTRO y no como prosa de acta. VA MARCADO COMO DISCUTIBLE en el reporte: el
encargo dice "LOS REGISTROS" sin nombrar fichero.
'''

NUEVA_CABECERA = '''LA SEDE, ELEGIDA Y DECLARADA EN VEZ DE SUPUESTA. Va a `docs/PENDIENTES.md`, que
es la forma que la casa ya usa desde `R.9`: "Registro de correcciones y
adjudicaciones declaradas de la vuelta N". Es el unico sitio del repo donde las
caidas y las adjudicaciones de una vuelta se registran como REGISTRO y no como
prosa de acta. VA MARCADO COMO DISCUTIBLE en el reporte: el encargo dice "LOS
REGISTROS" sin nombrar fichero.

--- CORRECCION DECLARADA (vuelta 162, TAREA 1.a; acta 161, seccion 5.1 y
adjudicacion 6.8). LO VIEJO NO SE BORRA Y QUEDA TACHADO Y LEGIBLE ---

    ~~"Va a `docs/PENDIENTES.md` como entrada `R.29` ... con la ultima escrita
    siendo `R.28` (vuelta 146, escrita en la 147, TAREA 1.a)."~~

LA CAIDA: `R.29` YA ESTABA ASIGNADA desde la vuelta 150 y vive en
`docs/plan/CORRECCIONES_A_APLICAR.md:2127`. La prueba estaba en el mismo fichero
que este script abrio: `docs/PENDIENTES.md:10389` dice literal que `R.29` NO esta
en esa pagina y que su fuente unica es la otra. LAS DOS CAUSAS SON DE ESTE
FICHERO: el ultimo numero venia TECLEADO aqui arriba, y la idempotencia de abajo
miraba UNA sola sede. LA SERIE `R.N` ES GLOBAL A LOS DOS FICHEROS.

EL REMEDIO, Y ES EL QUE HACE QUE NO PUEDA REPETIRSE: EL NUMERO NO SE TECLEA
NUNCA MAS. Lo computa `scripts/loop/serie_de_registros.py`, que lee LAS DOS
sedes, imprime la serie entera con su sede y devuelve `siguiente_libre()`. La
entrada que este script escribio se renumero a `R.30` en la vuelta 162 con
`scripts/loop/vuelta162_tarea1a_renumerar_r29.py`, sin borrar una linea.
'''

ANCLA_IMPORTS = '''import io
import json
import os
import subprocess
'''

NUEVOS_IMPORTS = '''import io
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402
'''

ANCLA_MARCA = '''MARCA = "## R.29. Registro de las caidas de clase de las dos tandas"
'''

NUEVA_MARCA = '''# CORRECCION DECLARADA (vuelta 162, TAREA 1.a). LA LINEA VIEJA, TACHADA Y
# LEGIBLE, porque con ella se escribio la entrada de la vuelta 161:
#     ~~MARCA = "## R.29. Registro de las caidas de clase de las dos tandas"~~
# EL DEFECTO: el numero estaba DENTRO de la marca, asi que la idempotencia
# dependia de acertar el numero, y ademas solo se buscaba en docs/PENDIENTES.md.
# LO NUEVO: la marca es el TITULO SIN NUMERO (lo unico estable de la entrada) y
# se busca en LAS DOS SEDES de la serie.
TITULO_SIN_NUMERO = "Registro de las caidas de clase de las dos tandas"
'''

ANCLA_IDEMPOTENCIA = '''    pend = io.open(PENDIENTES, encoding="utf-8").read()
    if MARCA in pend:
        print("YA ESTABA: R.29 vive en docs/PENDIENTES.md. No se toca.")
        print("CIFRA entradas escritas: 0")
        return 0
'''

NUEVA_IDEMPOTENCIA = '''    pend = io.open(PENDIENTES, encoding="utf-8").read()
    # CORRECCION DECLARADA (vuelta 162, TAREA 1.a). LAS LINEAS VIEJAS, TACHADAS Y
    # LEGIBLES, porque el veredicto de la vuelta 161 se dio con ellas:
    #     ~~if MARCA in pend:~~
    #     ~~    print("YA ESTABA: R.29 vive en docs/PENDIENTES.md. No se toca.")~~
    # LA SERIE SE RECOMPUTA DE LAS DOS SEDES ANTES DE MIRAR NADA, y la entrada se
    # busca POR SU TITULO, no por su numero.
    serie = SERIE.entradas()
    print("A0) LA SERIE R.N, RECOMPUTADA DE SUS DOS SEDES ANTES DE ESCRIBIR")
    for numero, rel, linea, titulo in serie:
        print("   R.%-3d %s:%-6d %s" % (numero, rel, linea, titulo[:88]))
    print("   CIFRA entradas: %d" % len(serie))
    print("   CIFRA colisiones: %d" % len(SERIE.colisiones(serie)))
    print("   SIGUIENTE LIBRE, computado y no tecleado: R.%d" % SERIE.siguiente_libre(serie))
    print("")
    ya = [(n, rel, ln) for n, rel, ln, t in serie if TITULO_SIN_NUMERO in t]
    if ya:
        n, rel, ln = ya[0]
        print("YA ESTABA: la entrada vive como R.%d en %s:%d. No se toca." % (n, rel, ln))
        print("CIFRA entradas escritas: 0")
        return 0
    numero_nuevo = SERIE.siguiente_libre(serie)
'''

PARCHES = [
    ("cabecera tecleada", ANCLA_CABECERA, NUEVA_CABECERA),
    ("imports", ANCLA_IMPORTS, NUEVOS_IMPORTS),
    ("constante MARCA", ANCLA_MARCA, NUEVA_MARCA),
    ("idempotencia de un solo fichero", ANCLA_IDEMPOTENCIA, NUEVA_IDEMPOTENCIA),
]


def main():
    s = io.open(RUTA, encoding="utf-8").read()
    for nombre, ancla, nuevo in PARCHES:
        n = s.count(ancla)
        if n != 1:
            raise SystemExit("ROJO: el ancla %r aparece %d veces (se esperaba 1)" % (nombre, n))
        s = s.replace(ancla, nuevo, 1)
        print("  aplicado: %s" % nombre)
    if "MARCA" in s.replace("TITULO_SIN_NUMERO", "").replace("~~MARCA", "").replace("MARCA_", ""):
        # aviso, no rojo: puede quedar la palabra dentro de un comentario tachado
        print("  AVISO: la palabra MARCA sigue apareciendo (se espera solo tachada).")
    io.open(RUTA, "w", encoding="utf-8", newline="\n").write(s)
    print("VERDE: %d parches aplicados sobre %s" % (len(PARCHES), RUTA))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
