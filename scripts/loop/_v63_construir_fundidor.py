# -*- coding: utf-8 -*-
"""_v63_construir_fundidor.py . CONSTRUYE scripts/loop/fundir_por_plan.py A
PARTIR DE SU ANCESTRO scripts/loop/vuelta49_fundir_tramo.py, POR EXTRACCION Y
CON UN ASSERT POR CAMBIO.

LA MAQUINA NO SE RETECLEA. Es la misma via que la vuelta 62 uso para construir
generar_plan_del_lote.py desde vuelta59_planes.py: el cuerpo del ancestro se
copia LITERAL desde la primera linea de codigo hasta el final, y sobre esa copia
se aplican SOLO los cambios de abajo, cada uno con su assert de que muerde una
vez y solo una. Si el ancestro cambia y alguna aguja deja de existir, esto cae y
no escribe.

EL ANCESTRO QUEDA INTACTO Y RE-CORRIBLE. Los planes de los tramos 1 a 6 lo
siguen citando y siguen pudiendo re-correrse con el.

LOS CAMBIOS, Y SON SOLO ROTULOS DE SALIDA. NI UNA LINEA DE ARITMETICA, NI UNA
GUARDA, NI EL CONTRATO DE LAS MARCAS:

  1. EL TITULO SE LEE DEL PLAN. El ancestro imprime OP-U-01, TRAMO <x>, con la
     operacion TALLADA en el literal. Corrido sobre una fusion de mesa eso
     publicaria OP-U-01 en la cabecera de una operacion que no es OP-U-01. Ahora
     el titulo sale de los campos operacion y rotulo del propio plan, y si el
     plan no los trae LO DICE en vez de suponerlos.
  2. LOS CUATRO ROTULOS QUE DICEN TRAMO pasan a decir OPERACION, por el mismo
     motivo: una fusion de mesa no es un tramo, y un rotulo que la llama tramo
     invita a leer su cifra como la de un tramo.

NADA MAS. El docstring del ancestro se pega entero debajo del nuevo, que es lo
que la casa hace con los sucesores declarados.

Uso:
  python scripts/loop/_v63_construir_fundidor.py [--simular]
IDEMPOTENTE: re-corrido sobre el mismo ancestro escribe el mismo fichero.
"""
import argparse
import hashlib
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
ANCESTRO = os.path.join(LOOP, "vuelta49_fundir_tramo.py")
DESTINO = os.path.join(LOOP, "fundir_por_plan.py")
NL = chr(10)

CABECERA = '''# -*- coding: utf-8 -*-
"""fundir_por_plan.py . EJECUTA UN PLAN DE FUSION SELLADO, SEA DE LA OPERACION
QUE SEA.

NOMBRE ESTABLE, y no lleva vuelta ni tramo ni operacion: los tres los dice el
PLAN que entra por --plan. Es la vara del acta 58, pregunta 4.

SUCESOR DECLARADO de scripts/loop/vuelta49_fundir_tramo.py, AL QUE NO REEMPLAZA:
el ancestro queda entero y re-corrible, y los planes de los tramos 1 a 6 de
OP-U-01 lo siguen citando. Es la via del acta 54, pregunta 3.

LA MAQUINA SE COPIA LITERAL Y NO SE RETECLEA: sale del ancestro POR EXTRACCION
con scripts/loop/_v63_construir_fundidor.py, que lleva un assert por cambio.

POR QUE NACE, y es una averia MEDIDA y no un capricho: el ancestro imprime su
cabecera con la operacion TALLADA en el literal (OP-U-01, TRAMO %s). Corrido
sobre una FUSION DE MESA, que es lo que la fase 03 tiene por delante desde que
OP-U-01 quedo agotada, habria publicado OP-U-01 en la cabecera de una operacion
que no es OP-U-01, y habria llamado TRAMO a lo que no es un tramo. Es la misma
especie que el censo de plantillas de la vuelta 63 persigue, cazada antes de
correr en vez de despues.

LO QUE CAMBIA RESPECTO DEL ANCESTRO, Y ES SOLO ESTO:
  1. el titulo se arma de los campos operacion y rotulo del plan, y si faltan LO
     DICE en vez de suponerlos;
  2. los cuatro rotulos de salida que decian TRAMO dicen OPERACION.
NI UNA LINEA DE ARITMETICA, NI UNA GUARDA, NI EL CONTRATO DE LAS MARCAS CAMBIA.

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.

Uso:
  python scripts/loop/fundir_por_plan.py --plan docs/loop/PLAN_V63_OPM03I.json [--ejecutar]

Lo que sigue es el docstring del ancestro, entero:

'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    fuente = io.open(ANCESTRO, encoding="utf-8").read()
    print("=" * 78)
    print("CONSTRUCCION DE fundir_por_plan.py DESDE SU ANCESTRO")
    print("  ancestro: %s" % os.path.relpath(ANCESTRO, RAIZ))
    print("  sha1 del ancestro medido hoy: %s"
          % hashlib.sha1(fuente.encode("utf-8")).hexdigest()[:12])
    print("  lineas del ancestro: %d" % len(fuente.split(NL)))
    print("=" * 78)
    print()

    lineas = fuente.split(NL)
    # el docstring del ancestro va del principio de la linea 2 al cierre """ .
    cierres = [i for i, l in enumerate(lineas) if l.strip() == '"""']
    assert len(cierres) >= 1, "no se hallo el cierre del docstring del ancestro"
    fin_doc = cierres[0]
    doc_ancestro = NL.join(lineas[2:fin_doc])
    cuerpo = NL.join(lineas[fin_doc + 1:])
    print("  docstring del ancestro: lineas 2 a %d (%d lineas)" % (fin_doc, fin_doc - 2))
    print("  cuerpo copiado LITERAL: desde la linea %d hasta el final (%d lineas)"
          % (fin_doc + 2, len(lineas) - fin_doc - 1))
    print()

    cambios = [
        ('    print("OP-U-01, TRAMO %s . MODO %s" % (plan["tramo"], modo))',
         '    # CAMBIO 1 DECLARADO: EL TITULO SE LEE DEL PLAN Y NO DEL LITERAL.\n'
         '    print("%s . %s . MODO %s"\n'
         '          % (plan.get("operacion") or "SIN OPERACION DECLARADA EN EL PLAN",\n'
         '             plan.get("rotulo") or plan.get("tramo")\n'
         '             or "SIN ROTULO DECLARADO EN EL PLAN", modo))',
         "el titulo, armado del plan"),
        ('    print("  duplicadas tras resolver ANTES del tramo (pasivo historico, OP-S-12): %d"',
         '    # CAMBIO 2 DECLARADO: el rotulo dice OPERACION y no TRAMO.\n'
         '    print("  duplicadas tras resolver ANTES de la operacion (pasivo historico, OP-S-12): %d"',
         "rotulo de duplicadas ANTES"),
        ('    print("  duplicadas tras resolver DESPUES del tramo                          : %d"',
         '    print("  duplicadas tras resolver DESPUES de la operacion                       : %d"',
         "rotulo de duplicadas DESPUES"),
        ('    print("  y el tramo BAJA el pasivo historico en %d, porque P.16 limpia lo que"',
         '    print("  y la operacion BAJA el pasivo historico en %d, porque P.16 limpia lo que"',
         "rotulo de la bajada del pasivo"),
        ('    print("RESUMEN DEL TRAMO")',
         '    print("RESUMEN DE LO EJECUTADO")',
         "rotulo del resumen"),
    ]
    # LA AGUJA VA ANCLADA AL SALTO DE LINEA, y no es un detalle de estilo: el
    # ancestro lleva SU PROPIO TEXTO VIEJO citado dentro de un comentario (la
    # correccion de rotulo de la vuelta 54), asi que una aguja sin anclar muerde
    # dos veces y una de ellas es el texto que NO se debe tocar. Lo cazo el
    # propio assert de aqui en la primera corrida.
    for viejo, nuevo, etq in cambios:
        n = cuerpo.count(NL + viejo)
        print("  CAMBIO %-34s muerde %d vez(veces)" % (etq, n))
        assert n == 1, "la aguja %r muerde %d veces y tiene que morder 1" % (etq, n)
        cuerpo = cuerpo.replace(NL + viejo, NL + nuevo, 1)

    salida = CABECERA + doc_ancestro + NL + '"""' + NL + cuerpo
    print()
    if a.simular:
        print("MODO SIMULAR: no se escribe %s." % os.path.relpath(DESTINO, RAIZ))
        return 0
    ya = io.open(DESTINO, encoding="utf-8").read() if os.path.exists(DESTINO) else None
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(salida)
    print("ESCRITO: %s (%d lineas)" % (os.path.relpath(DESTINO, RAIZ), len(salida.split(NL))))
    if ya is not None:
        print("IDEMPOTENCIA: el fichero ya existia y sale %s"
              % ("IDENTICO" if ya == salida else "DISTINTO"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
