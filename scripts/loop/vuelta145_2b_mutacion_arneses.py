# -*- coding: utf-8 -*-
r"""vuelta145_2b_mutacion_arneses.py . LA MUTACION DE LA TAREA 2.b, VUELTA 145:
UN ARNES CONGELADO QUE YA NO MUERDE ES PEOR QUE UNO ROJO.

POR QUE NACE. La TAREA 2.b de la vuelta 145 congela el sujeto de dos arneses
(`vuelta144_2d_mutacion_cobertura.py`, que pasa a un sujeto commiteado, y
`vuelta144_3b_mutacion_negativa.py`, que pasa a un pre-estado montado de un ref
de git). Congelar un sujeto es facil y peligroso: un arnes puede quedarse VERDE
para siempre PORQUE YA NO MIRA NADA. El encargo lo dice con todas sus letras:
"comprueba que SIGUE MORDIENDO sobre el sujeto congelado (que su caso rojo cae)
y no solo que sale verde".

QUE HACE. Por cada arnes congelado, se RELAJA LA GUARDA QUE EL ARNES PRUEBA
(no el arnes, y no su sujeto) y se exige que el arnes CAIGA. Despues se
restaura y se exige que vuelva a salir VERDE. Las dos mitades son necesarias:
sin la segunda, un arnes roto por el propio parche pasaria por mordedor.

  (1) vuelta144_2d_mutacion_cobertura.py. La guarda que prueba es
      `quitar_bloques_cubiertos()`. Se sustituye por la IDENTIDAD, o sea una
      que no recorta nada: entonces pegar la linea de COBERTURA dentro de los
      delimitadores SI mueve la cifra y el caso (B) del arnes tiene que caer.
  (2) vuelta144_3b_mutacion_negativa.py. La guarda que prueba en su caso (A) es
      la GUARDA 5 del sellador, el emparejamiento. Se sustituye
      `emparejamiento_declarado_de` por una que devuelve SIEMPRE el reparto que
      el contenido diga, o sea una guarda que se aprueba sola: entonces el caso
      (A) del arnes tiene que caer.

Todo EN MEMORIA. Los parches se deshacen siempre, salga por donde salga.

USO:
  python scripts/loop/vuelta145_2b_mutacion_arneses.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
sys.path.insert(0, LOOP)

import verificar_cifras_del_reporte as C  # noqa: E402
import vuelta144_3a_mutaciones as M  # noqa: E402
import vuelta144_2d_mutacion_cobertura as A2D  # noqa: E402
import vuelta144_3b_mutacion_negativa as A3B  # noqa: E402


class Capturada(object):
    def __init__(self):
        self.trozos = []

    def write(self, s):
        self.trozos.append(s)
        return len(s)

    def flush(self):
        pass

    def reconfigure(self, **kw):
        return None

    def valor(self):
        return "".join(self.trozos)


def correr(mod):
    real_out = sys.stdout
    buf = Capturada()
    try:
        sys.stdout = buf
        try:
            codigo = mod.main()
        except SystemExit as e:
            codigo = e.code if isinstance(e.code, int) else 1
        except Exception as e:  # noqa: BLE001
            buf.write("EXCEPCION: %r\n" % (e,))
            codigo = 1
    finally:
        sys.stdout = real_out
    return codigo, buf.valor()


def caso_2d():
    """La guarda relajada: `quitar_bloques_cubiertos` que no recorta nada."""
    real = C.quitar_bloques_cubiertos
    try:
        C.quitar_bloques_cubiertos = lambda texto: texto
        cod_relajado, sal_relajado = correr(A2D)
    finally:
        C.quitar_bloques_cubiertos = real
    cod_normal, _sal_normal = correr(A2D)
    return cod_relajado, sal_relajado, cod_normal


def caso_3b():
    """La guarda relajada: `emparejamiento_declarado_de` que devuelve el
    reparto DEL CONTENIDO, o sea una guarda 5 que se aprueba sola."""
    import _v144_opm04_328 as C328
    import _v144_opm04_367 as C367

    def complaciente(op):
        reparto = {}
        for spec in (C367.FUSION, C328.FUSION):
            reparto[spec["superviviente"]] = sorted(spec["absorbidos"])
        return reparto, "(guarda relajada por la mutacion de la vuelta 145)"

    real = M.emparejamiento_declarado_de
    try:
        M.emparejamiento_declarado_de = complaciente
        cod_relajado, sal_relajado = correr(A3B)
    finally:
        M.emparejamiento_declarado_de = real
    cod_normal, _sal_normal = correr(A3B)
    return cod_relajado, sal_relajado, cod_normal


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("MUTACION DE LA TAREA 2.b | vuelta 145 | LOS ARNESES CONGELADOS SIGUEN MORDIENDO")
    print("Todo EN MEMORIA. Se relaja LA GUARDA, nunca el arnes ni su sujeto.")
    print("=" * 78)

    resultados = []
    for nombre, fn, que_cae in (
            ("vuelta144_2d_mutacion_cobertura.py", caso_2d,
             "(B) dentro de los delimitadores, la cifra NO se mueve"),
            ("vuelta144_3b_mutacion_negativa.py", caso_3b,
             "(A) emparejamiento cambiado, cae la guarda 5")):
        cod_relajado, sal_relajado, cod_normal = fn()
        cae = cod_relajado != 0
        vuelve = cod_normal == 0
        ok = cae and vuelve
        print("ARNES %s" % nombre)
        print("  con la guarda RELAJADA: codigo %r | el arnes CAE: %s" % (cod_relajado, cae))
        for ln in sal_relajado.splitlines():
            if que_cae in ln:
                print("       %s" % ln.strip()[:150])
        print("  con la guarda ENTERA  : codigo %r | el arnes vuelve a VERDE: %s"
              % (cod_normal, vuelve))
        print("  VEREDICTO: %s" % ("OK" if ok else "ROJO"))
        print("")
        resultados.append((nombre, ok))

    print("=" * 78)
    buenas = sum(1 for _, ok in resultados if ok)
    for nombre, ok in resultados:
        print("  %-42s %s" % (nombre, "OK" if ok else "ROJO"))
    print("")
    print("ARNESES CONGELADOS QUE SIGUEN MORDIENDO: %d de %d" % (buenas, len(resultados)))
    return 0 if buenas == len(resultados) else 1


if __name__ == "__main__":
    raise SystemExit(main())
