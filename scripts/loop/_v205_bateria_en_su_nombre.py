# -*- coding: utf-8 -*-
r"""_v205_bateria_en_su_nombre.py . LA BATERIA DE LA VUELTA 205, CORRIDA CON EL
LANZADOR QUE YA EXISTE Y SELLADA EN EL NOMBRE DE ESTA VUELTA.

QUE ES Y QUE NO ES. NO ES UN LANZADOR NUEVO Y NO ES UN CLON. No copia ni una
linea del lanzador: LO IMPORTA. Todo lo que corre (la guarda del commit sobre
`dataset/`, la restauracion, el reloj, el sellado, la medicion, `--componer`) es
el codigo de `scripts/loop/vuelta183_bateria_por_tramos.py` tal como esta, sin
tocar. Lo unico que este fichero hace es CORREGIRLE EL NUMERO DE VUELTA que ese
lanzador computa de su PROPIO nombre de fichero.

POR QUE EXISTE, Y LA CAUSA ESTA MEDIDA Y NO SUPUESTA (encargo de la vuelta 205).
El encargo manda DOS cosas que, con el codigo de hoy, no pueden valer las dos:

  (1) "EL LANZADOR YA ESTA ESCRITO Y NO SE CLONA NI SE ESCRIBE OTRO:
      scripts/loop/vuelta183_bateria_por_tramos.py"
  (2) "LAS SALIDAS SELLADAS VAN EN EL NOMBRE DE ESTA VUELTA:
      SALIDA_V205_BATERIA_TRAMO_N.txt"

Y el propio cerrador lo remacha por tercer sitio: `cerrar_reporte.py`, en su
pieza (4), rechaza como bateria una salida de otra vuelta, "se mira el numero de
vuelta del fichero que se pega".

EL HECHO, CON SU LINEA DE CODIGO DELANTE, que es lo que el encargo manda medir y
declarar. En `scripts/loop/vuelta183_bateria_por_tramos.py`:

    linea  91  LANZADOR = os.path.basename(os.path.abspath(__file__))
    linea  92  _M_VUELTA = re.match(r"^vuelta(\d+)_", LANZADOR)
    linea  96  VUELTA = int(_M_VUELTA.group(1))
    linea 287  return "SALIDA_V%d_BATERIA_TRAMO_%d.txt" % (VUELTA, n)
    linea 293  return "SALIDA_V%d_BATERIA.txt" % VUELTA

El numero sale del NOMBRE DEL FICHERO y de ningun otro sitio: no hay ni un
argumento de linea de ordenes que lo mueva (`main()`, lineas 675 a 682, admite
`--tramo`, `--componer`, `--plan` y `--siguiente`, y ninguno mas). Corrido hoy,
`--siguiente` dice `vuelta (computada del nombre, no tecleada): 183` y da los
ONCE tramos de la 183 por sellados, con CERO que faltan. O sea que ese lanzador,
invocado por su nombre, NO PUEDE escribir una salida de la 205: escribiria encima
de las once salidas selladas de la 183.

LA SALIDA ELEGIDA, Y VA MARCADA COMO DISCUTIBLE EN EL REPORTE. El propio encargo
deja escrito el carril: "Un fichero `_v205_*` con prefijo de guion bajo, fuera del
censo y fuera de la nomina, es un computo de una vuelta y no roza la moratoria"
(acta 199 `4.5`, acta 203 `4.6`). Este es ese fichero. No anade guarda, no anade
lector, no anade arnes, no entra en la nomina (que sigue en 135) y no entra en el
censo (prefijo de guion bajo). Muere con la vuelta.

EL NUMERO TAMPOCO SE TECLEA AQUI, por la misma medicina de la caida `E.1` del
acta 183: sale de `os.path.basename(__file__)` de ESTE fichero con el patron
`^_v(\d+)_`, de modo que un computo de otra vuelta llamado `_v210_...` diria 210
sin que nadie se acuerde de nada.

USO:
  python scripts/loop/_v205_bateria_en_su_nombre.py --siguiente
  python scripts/loop/_v205_bateria_en_su_nombre.py --tramo 1
  python scripts/loop/_v205_bateria_en_su_nombre.py --componer
"""
import argparse
import io
import os
import re
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import vuelta183_bateria_por_tramos as L   # noqa: E402
import verificar_mutaciones_viejas as B    # noqa: E402

# EL NUMERO DE VUELTA DE ESTE COMPUTO, COMPUTADO DE SU PROPIO NOMBRE.
YO = os.path.basename(os.path.abspath(__file__))
_M = re.match(r"^_v(\d+)_", YO)
if not _M:
    raise SystemExit("ROJO: el nombre %r no dice de que vuelta es este computo, "
                     "y el numero NO SE ADIVINA." % YO)
MI_VUELTA = int(_M.group(1))

# LA UNICA CORRECCION QUE ESTE FICHERO HACE, Y SE DICE EN VOZ ALTA. El lanzador
# heredado computa 183 de su propio nombre; la corrida es de la 205. Se corrige
# EL DATO, no el codigo: ni una linea del lanzador se toca.
VUELTA_HEREDADA = L.VUELTA
L.VUELTA = MI_VUELTA


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramo", type=int, default=None)
    ap.add_argument("--componer", action="store_true")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--siguiente", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    # LA GUARDA DE LA ATRIBUCION DEL LANZADOR, CORRIDA SOBRE SU FUENTE Y NO SOBRE
    # EL MIO: es la suya, y sigue mordiendo igual.
    fuente = io.open(os.path.abspath(L.__file__), encoding="utf-8").read()
    clavados = L.literales_de_vuelta_clavados(fuente)
    print("GUARDA DE LA ATRIBUCION DEL LANZADOR, CORRIDA SOBRE SU PROPIO FUENTE")
    print("  computo de una vuelta (os.path.basename, no tecleado): %s" % YO)
    print("  vuelta de ESTA corrida (computada de mi nombre, no tecleada): %d"
          % MI_VUELTA)
    print("  lanzador importado, no clonado: %s" % L.LANZADOR)
    print("  vuelta que ESE lanzador computa de SU nombre: %d" % VUELTA_HEREDADA)
    print("  CIFRA literales de vuelta clavados en lineas que escriben: %d"
          % len(clavados))
    for i, linea, num in clavados:
        print("      LINEA %d clava %s: %s" % (i, num, linea[:120]))
    if clavados:
        print("ROJO: el lanzador importado clava numeros de vuelta. No arranca.")
        return 1
    print("  VERDE: ninguna linea que escribe clava un numero de vuelta.")
    print("")

    tramos = B.reparto_en_tramos(B.VIEJAS, L.TAMANO)
    print("  CIFRA nomina (leida del modulo, no tecleada): %d" % len(B.VIEJAS))
    print("  CIFRA tamano de tramo (leido del lanzador): %d" % L.TAMANO)
    print("  CIFRA tramos del reparto (computada): %d" % len(tramos))
    print("  CIFRA suma de las entradas de todos los tramos: %d"
          % sum(len(t) for t in tramos))
    print("")

    if a.siguiente:
        return L.siguiente(tramos)
    if a.plan:
        return L.plan(tramos)
    if a.componer:
        return L.componer(tramos)
    if a.tramo is None:
        print("ROJO: hace falta --tramo N, --componer, --plan o --siguiente.")
        return 1
    if not (1 <= a.tramo <= len(tramos)):
        print("ROJO: se pidio el tramo %d y el reparto solo tiene %d."
              % (a.tramo, len(tramos)))
        return 1

    # LA TRANSCRIPCION FUERA DE docs/loop/ Y COPIADA DENTRO AL FINAL, con la
    # clase del lanzador y por su mismo motivo (vuelta 177, TAREA 1.e).
    tmpdir = tempfile.mkdtemp(prefix="c%d_lanzador%d_" % (MI_VUELTA, a.tramo))
    fuera = os.path.join(tmpdir, "lanzador_en_curso.txt")
    original = sys.stdout
    doble = L.Desdoble(fuera, original)
    sys.stdout = doble
    try:
        print("LA TRANSCRIPCION DE ESTE COMPUTO SE ESTA ESCRIBIENDO FUERA DE")
        print("docs/loop/, y se copiara dentro AL TERMINAR: %s" % fuera)
        codigo = L.correr_tramo(a.tramo, tramos)
    finally:
        sys.stdout = original
        doble.cerrar()
        dentro = os.path.join(L.LOOP, L.nombre_transcripcion(a.tramo))
        datos = io.open(fuera, "rb").read()
        io.open(dentro, "wb").write(datos)
        print("TRANSCRIPCION COPIADA A docs/loop/%s (%d bytes), ESCRITA FUERA "
              "MIENTRAS LA BATERIA CORRIA"
              % (L.nombre_transcripcion(a.tramo), len(datos)))
    return codigo


if __name__ == "__main__":
    raise SystemExit(main())
