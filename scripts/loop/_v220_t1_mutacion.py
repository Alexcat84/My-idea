# -*- coding: utf-8 -*-
r"""_v220_t1_mutacion.py . LA PRUEBA DE MUTACION DEL CASO ROJO DE LA TAREA 1
DE LA VUELTA 220.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). No es guarda nueva que se quede
vigilando: es la prueba obligatoria de EJECUTOR.md 1, EL CASO ROJO SE PRUEBA
POR MUTACION, y muere con la vuelta.

QUE PRUEBA, Y POR QUE HACE FALTA. La TAREA 1 publica como prueba el juicio
juicio_del_movimiento() de scripts/loop/_v220_t1_registros.py, que decide que
de lo que se movio al re-correr el lector de la 219 es ROJO. Ese juicio salio
en VERDE en la corrida real. UN CASO QUE SOLO SE HA VISTO EN VERDE NO ES UNA
PRUEBA: aqui se le cambia el valor esperado, caso por caso, y se comprueba que
CAE.

LOS CUATRO CASOS, Y CADA UNO MUEVE UNA COSA SOLA:
  1. VERDE DE CONTROL: se movio solo la salida propia del lector y la unica
     linea que difiere es la del conteo del acta. Tiene que dar CERO motivos.
  2. ROJO POR FICHERO AJENO: se movio ademas una sede del plan. Tiene que caer.
  3. ROJO POR DOS LINEAS: la salida propia difiere en dos lineas. Tiene que caer.
  4. ROJO POR OTRA LINEA: la salida propia difiere en una sola linea, pero no
     es la del conteo del acta. Tiene que caer.

IMPORTAR NO ES CLONAR: el juicio se IMPORTA de _v220_t1_registros y aqui no se
copia ni una linea de el.

USO:  python scripts/loop/_v220_t1_mutacion.py
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import _v220_t1_registros as T  # noqa: E402

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = int(re.search(r"_v(\d+)_",
                       os.path.basename(os.path.abspath(__file__))).group(1))

PROPIA = T.SALIDA_LECTOR_219
AJENA = "docs/plan/08_VERIFICACION.md"

LINEA_BUENA_VIEJA = ("   LOS DOS FICHEROS DE LAS CITAS, MEDIDOS HOY: "
                     "docs/loop/ACTA_AUDITOR.md con 77726 lineas.")
LINEA_BUENA_NUEVA = ("   LOS DOS FICHEROS DE LAS CITAS, MEDIDOS HOY: "
                     "docs/loop/ACTA_AUDITOR.md con 78126 lineas.")
LINEA_CUALQUIERA_A = "   CIFRA clausulas en CUBRE AL CIERRE DE LA TAREA 2: 14 de 17"
LINEA_CUALQUIERA_B = "   CIFRA clausulas en CUBRE AL CIERRE DE LA TAREA 2: 17 de 17"

CASOS = [
    ("1 VERDE DE CONTROL: solo la salida propia, y solo la linea del conteo "
     "del acta",
     [PROPIA],
     [(157, LINEA_BUENA_VIEJA, LINEA_BUENA_NUEVA)],
     0),
    ("2 ROJO POR FICHERO AJENO: se movio ademas una sede del plan",
     [PROPIA, AJENA],
     [(157, LINEA_BUENA_VIEJA, LINEA_BUENA_NUEVA)],
     1),
    ("3 ROJO POR DOS LINEAS: la salida propia difiere en dos",
     [PROPIA],
     [(157, LINEA_BUENA_VIEJA, LINEA_BUENA_NUEVA),
      (240, LINEA_CUALQUIERA_A, LINEA_CUALQUIERA_B)],
     1),
    ("4 ROJO POR OTRA LINEA: una sola, pero no la del conteo del acta",
     [PROPIA],
     [(240, LINEA_CUALQUIERA_A, LINEA_CUALQUIERA_B)],
     1),
]


def main():
    out = []
    fallos = 0

    def w(s=""):
        out.append(s)

    w("=" * 78)
    w("PRUEBA DE MUTACION DEL CASO ROJO DE LA TAREA 1 DE LA VUELTA %d" % VUELTA)
    w("=" * 78)
    w("")
    w("EL JUICIO SE IMPORTA, NO SE CLONA: juicio_del_movimiento() de %s"
      % os.path.basename(T.__file__))
    w("LA MARCA QUE EL JUICIO USA, LEIDA DEL MODULO Y NO TECLEADA AQUI: %r"
      % T.MARCA_CONTEO_DEL_ACTA)
    w("")
    for nombre, movidos, difs, motivos_esperados in CASOS:
        motivos = T.juicio_del_movimiento(movidos, difs, PROPIA)
        cae = len(motivos) > 0
        esperado_cae = motivos_esperados > 0
        ok = cae == esperado_cae
        w("CASO %s" % nombre)
        w("   ficheros movidos que se le pasan: %s" % ", ".join(movidos))
        w("   CIFRA lineas que difieren que se le pasan: %d" % len(difs))
        w("   CIFRA motivos de ROJO que devuelve: %d | CIFRA que el caso "
          "espera: %s" % (len(motivos), "0" if not esperado_cae else "1 o mas"))
        for m in motivos:
            w("      motivo> %s" % m)
        w("   EL CASO %s: %s" % ("CAE" if cae else "NO CAE",
                                 "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos += 1
        w("")
    w("Y LA MUTACION SOBRE EL VALOR ESPERADO, QUE ES LA QUE PRUEBA QUE ESTO NO")
    w("SE APRUEBA SOLO: si al caso 1 se le exigiera CAER, el arnes tendria que")
    w("decir NO CALZA. Se comprueba aqui mismo:")
    motivos_1 = T.juicio_del_movimiento(CASOS[0][1], CASOS[0][2], PROPIA)
    mutado_calza = (len(motivos_1) > 0) == True
    w("   con el valor esperado MUTADO a CAE, el caso 1 %s"
      % ("CALZARIA, y eso seria un arnes que se aprueba solo"
         if mutado_calza else "NO CALZA, que es lo que se exige"))
    if mutado_calza:
        fallos += 1
    w("")
    w("CIFRA casos que CAEN: %d de %d"
      % (len([c for c in CASOS if c[3] > 0]), len(CASOS)))
    w("CIFRA comprobaciones que fallan: %d" % fallos)
    w("VERDE: los cuatro casos se comportan." if not fallos
      else "ROJO: la prueba de mutacion no se sostiene.")

    texto = NL.join(out) + NL
    destino = os.path.join(LOOP, "SALIDA_V%d_T1_MUTACION.txt" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    sys.stdout.write(NL + "SELLADO EN %s, %d bytes%s"
                     % (os.path.basename(destino), os.path.getsize(destino), NL))
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
