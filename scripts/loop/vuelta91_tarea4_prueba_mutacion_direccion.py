# -*- coding: utf-8 -*-
"""vuelta91_tarea4_prueba_mutacion_direccion.py . VUELTA 91, TAREA 4: el caso
rojo del criterio automatico de direccion de OP-E-07
(scripts/loop/vuelta91_tarea4_direccion_ope07.py) NO SE PUBLICA sin correr
antes su prueba de mutacion (EJECUTOR.md regla 1, "EL CASO ROJO SE PRUEBA
POR MUTACION").

QUE PRUEBA: `extraer_direccion_automatica(razon, id_a, id_b)`, LA UNICA
PIEZA DE JUICIO AUTOMATICA del instrumento (las 80 direcciones automaticas
de las 88 de la bolsa salen todas de esta funcion; las 8 restantes son
lectura manual citada, declarada como tal, no una segunda cuenta paralela
que compita con esta).

  entrada normal: una razon fabricada donde SOLO el segundo id trae la
  marca de hijo ("... nodo_b trae el procedimiento de esa linea").
  veredicto esperado: "B_HIJO".
  entrada MUTADA: LA MISMA razon con la marca de hijo movida al PRIMER id
  ("... nodo_a trae el procedimiento de esa linea ... nodo_b no trae
  nada"). Es una mutacion sobre EL TEXTO QUE EL CODIGO LEE (la razon real
  que se le pasa), no sobre una constante escrita a mano. veredicto
  esperado tras mutar: "A_HIJO".

Si `extraer_direccion_automatica` no dependiera de verdad de la razon que
recibe, esta prueba caeria en ROJO, y NO se publicaria el caso como prueba.

USO:
  python scripts/loop/vuelta91_tarea4_prueba_mutacion_direccion.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

from verificar_caso_rojo_por_mutacion import probar_por_mutacion
from vuelta91_tarea4_direccion_ope07 import extraer_direccion_automatica


def main():
    id_a, id_b = "nodo_prueba_a", "nodo_prueba_b"
    razon_normal = ("%s dice en su paso 2, en UNA LINEA, algo breve; y %s trae el "
                     "procedimiento de esa linea, entero." % (id_a, id_b))
    razon_mutada = ("%s trae el procedimiento de esa linea, entero; y %s dice en su "
                     "paso 2, en UNA LINEA, algo breve, sin traer nada mas." % (id_a, id_b))

    ok = probar_por_mutacion(
        nombre="extraer_direccion_automatica() de scripts/loop/vuelta91_tarea4_direccion_ope07.py",
        criterio=lambda razon: extraer_direccion_automatica(razon, id_a, id_b),
        entrada=razon_normal, veredicto_esperado="B_HIJO",
        entrada_mutada=razon_mutada, veredicto_tras_mutar="A_HIJO",
    )
    if ok is not True:
        print("ROJO: probar_por_mutacion no devolvio True (no deberia llegar aqui: "
              "habria caido con SystemExit antes).")
        return 1

    print("EL CASO ROJO DEL CRITERIO AUTOMATICO DE DIRECCION DE OP-E-07 ESTA PROBADO POR "
          "MUTACION: extraer_direccion_automatica() SI depende de la razon que recibe, y "
          "los dos veredictos (B_HIJO con la marca en el segundo id, A_HIJO con la marca "
          "movida al primero) calzan con lo esperado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
