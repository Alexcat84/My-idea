# -*- coding: utf-8 -*-
"""vuelta90_tarea3_prueba_mutacion_tallador.py . VUELTA 90, TAREA 3.b APLICADA
A LA TAREA 3.a: el caso rojo del tallador nuevo (scripts/loop/
tallar_conteo_campo.py) NO SE PUBLICA sin correr antes su prueba de mutacion
(EJECUTOR.md regla 1, "EL CASO ROJO SE PRUEBA POR MUTACION").

QUE PRUEBA: `clasifica_longitud(fila, campo, n)`, LA UNICA PIEZA DE JUICIO del
tallador (la funcion de la que salen las tres cifras de la tabla Y el cotejo
de --verificar-puestos: no hay una segunda cuenta paralela). Usa el mismo
arnes generico de la TAREA 3.b
(scripts/loop/verificar_caso_rojo_por_mutacion.probar_por_mutacion):

  entrada normal: una fila fabricada con `frase` de exactamente 200
  caracteres. veredicto esperado: "IGUAL".
  entrada MUTADA: LA MISMA fila con la `frase` estirada a 305 caracteres (el
  largo real del puesto 2023 de la vuelta 89, el ejemplar de la caida). Es
  una mutacion sobre LO QUE EL CODIGO COMPUTE (la longitud real del campo),
  no sobre una constante escrita a mano: `clasifica_longitud` lee `len(fila
  [campo])` de la fila que se le pase, y la fila mutada tiene un campo
  distinto de verdad. veredicto esperado tras mutar: "MAYOR".

Si `clasifica_longitud` no dependiera de verdad de la fila que recibe (el
defecto de la vuelta 89, reproducido en `scripts/loop/
verificar_caso_rojo_por_mutacion.py` sobre un criterio de juguete), esta
prueba caeria en ROJO, y NO se publicaria el caso como prueba.

USO:
  python scripts/loop/vuelta90_tarea3_prueba_mutacion_tallador.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

from verificar_caso_rojo_por_mutacion import probar_por_mutacion
from tallar_conteo_campo import clasifica_longitud


def main():
    fila_200 = {"frase": "x" * 200}
    fila_305 = {"frase": "x" * 305}  # el largo REAL del puesto 2023 de la vuelta 89

    ok = probar_por_mutacion(
        nombre="clasifica_longitud() de scripts/loop/tallar_conteo_campo.py",
        criterio=lambda fila: clasifica_longitud(fila, "frase", 200),
        entrada=fila_200, veredicto_esperado="IGUAL",
        entrada_mutada=fila_305, veredicto_tras_mutar="MAYOR",
    )
    if ok is not True:
        print("ROJO: probar_por_mutacion no devolvio True (no deberia llegar aqui: "
              "habria caido con SystemExit antes).")
        return 1

    print("EL CASO ROJO DEL TALLADOR NUEVO (TAREA 3.a) ESTA PROBADO POR MUTACION (TAREA "
          "3.b): clasifica_longitud() SI depende de la fila que recibe, y los dos "
          "veredictos (IGUAL con 200 caracteres, MAYOR con 305) calzan con lo esperado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
