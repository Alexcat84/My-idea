# -*- coding: utf-8 -*-
r"""vuelta145_2c_mutacion_censo.py . LA MUTACION DE LA TAREA 2.c, VUELTA 145.

QUE PRUEBA. Que los DOS bucles que eligen sujeto por computo
(`vuelta144_2a_mutaciones.py` y `vuelta144_2b_mutacion_giro.py`) YA NO TIRAN
LOS FALLOS del parser de la excepcion: se le da a cada uno una ficha cuya
excepcion NO PARSEA y el arnes tiene que NOMBRARLA por su `id_op`, en vez de
saltarsela en silencio y seguir buscando sujeto (acta 144, caida 4.1 del
auditor; banco 9, fallar ruidoso).

COMO SE ROMPE LA FICHA, y se rompe POR COMPUTO, no a mano: se busca la PRIMERA
ficha que dispara la excepcion del 9.22 CON pares, y se le quita de su linea de
`verificacion` la MARCA DE CIERRE de la formula canonica. Ese es uno de los
tres extremos ruidosos que la TAREA 2.a de la vuelta 144 escribio: sin cierre,
`pares_exceptuados_de` devuelve conjunto vacio Y DEJA UN FALLO. La ficha rota
se cuela DELANTE de la lista de fichas EN MEMORIA, para que el bucle la vea
antes que a ninguna otra.

DOS COMPROBACIONES POR ARNES, y las dos leen la salida real del proceso, nunca
un literal comparado consigo mismo (EJECUTOR.md regla 1):
  (i)  CON LA FICHA ROTA DELANTE, la salida del arnes NOMBRA el id de la ficha
       rota bajo el rotulo de fichas cuya excepcion no parsea.
  (ii) CONTRAPRUEBA, SIN romper nada, ese rotulo NO aparece. Sin ella, (i)
       podria estar saliendo por cualquier otra causa.

TODO EN MEMORIA: se parchea `T.cargar_ops` mientras dura cada caso y se
restaura siempre. Cero escrituras.

USO:
  python scripts/loop/vuelta145_2c_mutacion_censo.py
"""
import copy
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
sys.path.insert(0, LOOP)

import tallar_estado_de_fase as T  # noqa: E402

ROTULO = "FICHAS CUYA EXCEPCION NO PARSEA"

ARNESES = [
    ("vuelta144_2a_mutaciones", ["vuelta144_2a_mutaciones.py"]),
    ("vuelta144_2b_mutacion_giro", ["vuelta144_2b_mutacion_giro.py"]),
]


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


def ficha_rota():
    """LA FICHA ROTA, POR COMPUTO: la primera que dispara la excepcion con
    pares, con la MARCA DE CIERRE de la formula quitada de su linea. Devuelve
    (ficha_rota, id_op, indice_de_linea) o (None, None, None)."""
    nodos = T.cargar_grafo("WORK")
    resolver = T.resolver_de(nodos)
    # ESTE BUCLE TAMBIEN RECOGE SUS FALLOS, y no por simetria: su propio censo
    # (vuelta145_2c_censo_de_llamadas.py) lo caza si no lo hace. Corrido sobre
    # la primera version de este fichero dio ROJO nombrando esta linea, que
    # pasaba un literal vacio. La regla vale tambien para quien la escribe.
    fallos_del_censo = []
    for op in T.cargar_ops("WORK"):
        fallos_de_esta = []
        conj, _cita, _nom = T.pares_exceptuados_de(op, resolver, fallos_de_esta)
        if fallos_de_esta:
            fallos_del_censo.append((op.get("id_op"), list(fallos_de_esta)))
        if not conj:
            continue
        if fallos_del_censo:
            print("FICHAS CUYA EXCEPCION NO PARSEA, HALLADAS AL BUSCAR SUJETO (%d):"
                  % len(fallos_del_censo))
            for id_op, fs in fallos_del_censo:
                for f in fs:
                    print("     %s: %s" % (id_op, f))
        rota = copy.deepcopy(op)
        rota["id_op"] = "%s-ROTA-V145" % op.get("id_op")
        lineas = list(rota.get("verificacion") or [])
        for i, linea in enumerate(lineas):
            bajo = (linea or "").lower()
            j = bajo.find(T.MARCA_CIERRA_EXCEPCION)
            if j >= 0:
                lineas[i] = linea[:j] + linea[j + len(T.MARCA_CIERRA_EXCEPCION):]
                rota["verificacion"] = lineas
                return rota, rota["id_op"], i
    return None, None, None


def correr(modulo, argv, ops_falsas):
    """Corre `modulo.main()` con `T.cargar_ops` devolviendo `ops_falsas` (o el
    original si es None). Devuelve (codigo, salida)."""
    mod = __import__(modulo)
    real_cargar, real_argv, real_out = T.cargar_ops, sys.argv, sys.stdout
    buf = Capturada()
    try:
        if ops_falsas is not None:
            T.cargar_ops = lambda ref: list(ops_falsas)
        sys.argv = argv
        sys.stdout = buf
        try:
            codigo = mod.main()
        except SystemExit as e:
            codigo = e.code if isinstance(e.code, int) else 1
        except Exception as e:  # noqa: BLE001
            buf.write("EXCEPCION: %r\n" % (e,))
            codigo = 1
    finally:
        T.cargar_ops, sys.argv, sys.stdout = real_cargar, real_argv, real_out
    return codigo, buf.valor()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("MUTACION DE LA TAREA 2.c | vuelta 145 | LOS FALLOS DEL PARSER SE NOMBRAN")
    print("Todo EN MEMORIA, cero escrituras.")
    print("=" * 78)

    rota, id_rota, idx = ficha_rota()
    if rota is None:
        print("ROJO PREVIO: ninguna ficha dispara la excepcion con pares; no hay nada "
              "que romper y el arnes no mide nada")
        return 1
    print("FICHA ROTA POR COMPUTO: %s (linea %d de verificacion, sin la marca de cierre %r)"
          % (id_rota, idx, T.MARCA_CIERRA_EXCEPCION))
    print("")

    ops_reales = T.cargar_ops("WORK")
    ops_con_rota = [rota] + list(ops_reales)

    resultados = []
    for modulo, argv in ARNESES:
        cod_i, sal_i = correr(modulo, argv, ops_con_rota)
        nombra = (ROTULO in sal_i) and (id_rota in sal_i)
        cod_ii, sal_ii = correr(modulo, argv, None)
        callado = ROTULO not in sal_ii
        ok = nombra and callado
        print("ARNES %s" % modulo)
        print("  (i)  con la ficha rota delante: codigo %r | nombra %s: %s"
              % (cod_i, id_rota, nombra))
        for ln in sal_i.splitlines():
            if id_rota in ln:
                print("       %s" % ln.strip()[:170])
        print("  (ii) contraprueba, sin romper nada: codigo %r | el rotulo NO aparece: %s"
              % (cod_ii, callado))
        print("  VEREDICTO: %s" % ("OK" if ok else "ROJO"))
        print("")
        resultados.append((modulo, ok))

    print("=" * 78)
    buenas = sum(1 for _, ok in resultados if ok)
    for modulo, ok in resultados:
        print("  %-40s %s" % (modulo, "OK" if ok else "ROJO"))
    print("")
    print("ARNESES QUE NOMBRAN SUS FALLOS: %d de %d" % (buenas, len(resultados)))
    return 0 if buenas == len(resultados) else 1


if __name__ == "__main__":
    raise SystemExit(main())
