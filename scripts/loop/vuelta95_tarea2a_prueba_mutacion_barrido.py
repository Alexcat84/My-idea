# -*- coding: utf-8 -*-
"""vuelta95_tarea2a_prueba_mutacion_barrido.py . VUELTA 95, TAREA 2.a: el
caso rojo del tallador nuevo (scripts/loop/tallar_barrido_cifras.py) NO SE
PUBLICA sin correr antes su prueba de mutacion (EJECUTOR.md regla 1, "EL
CASO ROJO SE PRUEBA POR MUTACION").

QUE PRUEBA: `tiene_salvedad(contexto, patron_salvedad)`, LA UNICA PIEZA DE
JUICIO del tallador nuevo (el conteo con/sin salvedad y las dos
enumeraciones llaman todos a esta misma funcion; no hay una segunda cuenta
paralela). Usa el mismo arnes generico que ya prueba a
`tallar_composicion_salida.clasifica_fila`
(scripts/loop/vuelta91_tarea3_prueba_mutacion_composicion.py):
`scripts/loop/verificar_caso_rojo_por_mutacion.probar_por_mutacion`.

  entrada normal: un CONTEXTO real, tomado de docs/plan/04_ENLACES.md fila 9
  ("cifra vigente de `OP-E-07` hasta la vuelta 92"). veredicto esperado:
  True (la marca de salvedad SI esta).
  entrada MUTADA: LA MISMA cadena, con la frase de salvedad ("hasta la
  vuelta 92") quitada de verdad (no un literal aparte: es la misma cadena
  base con .replace() sobre la frase que la hace salvedad). veredicto
  esperado tras mutar: False.

Es una mutacion sobre EL CONTENIDO del contexto que la funcion recibe, no
sobre un literal booleano al lado del assert: si `tiene_salvedad` no
dependiera de verdad de su entrada (el defecto de la vuelta 89, reproducido
en `verificar_caso_rojo_por_mutacion.py`), esta prueba caeria en ROJO y NO se
publicaria el caso como prueba.

USO:
  python scripts/loop/vuelta95_tarea2a_prueba_mutacion_barrido.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

from verificar_caso_rojo_por_mutacion import probar_por_mutacion
from tallar_barrido_cifras import tiene_salvedad, PATRON_SALVEDAD_DEFECTO
import re


def main():
    patron = re.compile(PATRON_SALVEDAD_DEFECTO)

    contexto_normal = "declaradas quedan ratificadas enteras. La cifra vigente de `OP-E-07` hasta la vuelta 92 y no antes."
    contexto_mutado = contexto_normal.replace("hasta la vuelta 92", "en este momento")

    ok = probar_por_mutacion(
        nombre="tiene_salvedad() de scripts/loop/tallar_barrido_cifras.py",
        criterio=lambda contexto: tiene_salvedad(contexto, patron),
        entrada=contexto_normal, veredicto_esperado=True,
        entrada_mutada=contexto_mutado, veredicto_tras_mutar=False,
    )
    if ok is not True:
        print("ROJO: probar_por_mutacion no devolvio True (no deberia llegar aqui: "
              "habria caido con SystemExit antes).")
        return 1

    print("EL CASO ROJO DEL TALLADOR DE BARRIDO (TAREA 2.a de la vuelta 95) ESTA PROBADO "
          "POR MUTACION: tiene_salvedad() SI depende del contexto que recibe, y los dos "
          "veredictos (True con la salvedad presente, False con la misma cadena sin ella) "
          "calzan con lo esperado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
