# -*- coding: utf-8 -*-
"""vuelta91_tarea3_prueba_mutacion_composicion.py . VUELTA 91, TAREA 3: el
caso rojo del tallador nuevo (scripts/loop/tallar_composicion_salida.py) NO
SE PUBLICA sin correr antes su prueba de mutacion (EJECUTOR.md regla 1, "EL
CASO ROJO SE PRUEBA POR MUTACION").

QUE PRUEBA: `clasifica_fila(valores, campo_clase, valor_base, etiqueta_base,
etiqueta_otra)`, LA UNICA PIEZA DE JUICIO del tallador nuevo (el conteo, la
enumeracion y el cotejo llaman todos a esta misma funcion; no hay una segunda
cuenta paralela). Usa el mismo arnes generico de la TAREA 3.b de la vuelta 90
(scripts/loop/verificar_caso_rojo_por_mutacion.probar_por_mutacion):

  entrada normal: una fila fabricada cuyo campo 'crudo' es exactamente "sin
  alias". veredicto esperado: "sin alias" (la etiqueta_base).
  entrada MUTADA: LA MISMA fila con el campo 'crudo' cambiado a un par real
  ("pivotar_o_proceder -> pivote_o_proceder", la sustitucion mas repetida de
  la vuelta 90). Es una mutacion sobre LO QUE EL CODIGO COMPUTE (el valor
  real del campo), no sobre una constante escrita a mano: `clasifica_fila`
  lee `valores[campo_clase]` de la fila que se le pase, y la fila mutada
  trae un valor distinto de verdad. veredicto esperado tras mutar: "resuelto
  por alias" (la etiqueta_otra).

Si `clasifica_fila` no dependiera de verdad de la fila que recibe (el
defecto de la vuelta 89, reproducido en `scripts/loop/
verificar_caso_rojo_por_mutacion.py` sobre un criterio de juguete), esta
prueba caeria en ROJO, y NO se publicaria el caso como prueba.

USO:
  python scripts/loop/vuelta91_tarea3_prueba_mutacion_composicion.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

from verificar_caso_rojo_por_mutacion import probar_por_mutacion
from tallar_composicion_salida import clasifica_fila


def main():
    fila_sin_alias = {"crudo": "sin alias"}
    fila_con_alias = {"crudo": "pivotar_o_proceder -> pivote_o_proceder"}

    ok = probar_por_mutacion(
        nombre="clasifica_fila() de scripts/loop/tallar_composicion_salida.py",
        criterio=lambda fila: clasifica_fila(fila, "crudo", "sin alias", "sin alias", "resuelto por alias"),
        entrada=fila_sin_alias, veredicto_esperado="sin alias",
        entrada_mutada=fila_con_alias, veredicto_tras_mutar="resuelto por alias",
    )
    if ok is not True:
        print("ROJO: probar_por_mutacion no devolvio True (no deberia llegar aqui: "
              "habria caido con SystemExit antes).")
        return 1

    print("EL CASO ROJO DEL TALLADOR DE COMPOSICION (TAREA 3 de la vuelta 91) ESTA PROBADO "
          "POR MUTACION: clasifica_fila() SI depende de la fila que recibe, y los dos "
          "veredictos ('sin alias' con el campo base, 'resuelto por alias' con el campo "
          "mutado) calzan con lo esperado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
