# -*- coding: utf-8 -*-
"""vuelta144_3b_giro_sin_flecha.py . LA MEDICION QUE JUSTIFICA LA ADICION A
`aristas_nuevas` DE OP-M-04 (TAREA 3.b, vuelta 144).

QUE MIDE. Que SIN la entrada legible por maquina, el giro de esta operacion
ABORTA en su guarda 4 sin escribir nada, aunque la ficha describa la arista con
todas sus letras en prosa. Es la medicion que la propia adicion cita, y se deja
REPRODUCIBLE en vez de pegar una salida de una corrida que ya no se puede
repetir: la entrada anadida se quita EN MEMORIA y el giro se corre con la ficha
tal como estaba.

EL GRAFO TAMBIEN VA SIMULADO, Y SE DICE POR QUE: la guarda 4 es la CUARTA, y para
llegar a ella hay que pasar la 3, que exige FORMA DE GIRO (la vuelta puesta y la
ida ausente). Ese era el estado del grafo el dia que esta medicion se tomo, pero
la propia vuelta 144 ejecuta el giro justo despues, asi que leer el grafo de hoy
haria caer la medicion por la guarda 3 y no por la 4, y esta salida dejaria de
reproducir. Se fabrica EN MEMORIA el estado de partida (la vuelta puesta, la ida
ausente) para que la medicion siga diciendo lo mismo dentro de cien vueltas. Es
el mismo patron que vuelta144_2b_mutacion_giro.py, aprobado en la adjudicacion
3.7 del acta 143.

CERO ESCRITURAS: el giro va en modo SIMULAR, y ni la ficha ni el grafo del disco
se tocan.
"""
import copy
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import tallar_estado_de_fase as T  # noqa: E402
import vuelta143_3c_girar_arista as G  # noqa: E402

ID_OP = "OP-M-04"


class Capturada(io.StringIO):
    def reconfigure(self, **kw):
        return None


def main():
    ops = T.cargar_ops("WORK")
    sin_flecha = copy.deepcopy(ops)
    quitadas = 0
    for o in sin_flecha:
        if o.get("id_op") == ID_OP:
            antes = list(o.get("aristas_nuevas") or [])
            o["aristas_nuevas"] = [x for x in antes if "->" not in x]
            quitadas = len(antes) - len(o["aristas_nuevas"])
    print("MEDICION DE LA TAREA 3.b | vuelta 144 | %s" % ID_OP)
    print("Entradas de aristas_nuevas con flecha QUITADAS EN MEMORIA: %d" % quitadas)
    print("=" * 78)
    if quitadas != 1:
        print("ROJO PREVIO: se esperaba quitar EXACTAMENTE UNA entrada con flecha y se "
              "quitaron %d. Sin ese sujeto la medicion no dice nada." % quitadas)
        return 1

    # EL GRAFO DE PARTIDA, FABRICADO EN MEMORIA: la vuelta puesta y la ida ausente.
    nodos = T.cargar_grafo("WORK")
    grafo = copy.deepcopy(nodos)
    res = T.resolver_de(grafo)
    MADRE, HIJO = "identificar_consejo_asesores", "formalizar_junta_asesora"
    grafo[MADRE]["nodos_siguientes"] = [y for y in (grafo[MADRE].get("nodos_siguientes") or [])
                                        if res(y) != HIJO]
    grafo[HIJO]["nodos_previos"] = [y for y in (grafo[HIJO].get("nodos_previos") or [])
                                    if res(y) != MADRE]
    if MADRE not in [res(y) for y in (grafo[HIJO].get("nodos_siguientes") or [])]:
        grafo[HIJO].setdefault("nodos_siguientes", []).append(MADRE)
    if HIJO not in [res(y) for y in (grafo[MADRE].get("nodos_previos") or [])]:
        grafo[MADRE].setdefault("nodos_previos", []).append(HIJO)
    print("GRAFO DE PARTIDA FABRICADO EN MEMORIA: la VUELTA %s -> %s puesta: %s | la IDA "
          "%s -> %s puesta: %s"
          % (HIJO, MADRE, T.arista_presente(grafo, T.resolver_de(grafo), HIJO, MADRE)[0],
             MADRE, HIJO, T.arista_presente(grafo, T.resolver_de(grafo), MADRE, HIJO)[0]))
    print("")

    antes_disco = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                                 cwd=RAIZ, capture_output=True, text=True).stdout
    real_ops, real_grafo = T.cargar_ops, T.cargar_grafo
    real_argv, real_out = sys.argv, sys.stdout
    buf = Capturada()
    try:
        T.cargar_ops = lambda ref="WORK": copy.deepcopy(sin_flecha)
        T.cargar_grafo = lambda ref="WORK": copy.deepcopy(grafo)
        sys.argv = ["vuelta143_3c_girar_arista.py",
                    "--retirar-de", "formalizar_junta_asesora",
                    "--retirar-a", "identificar_consejo_asesores",
                    "--por-la-op", ID_OP]
        sys.stdout = buf
        try:
            codigo = G.main()
        except SystemExit as e:
            codigo = e.code if isinstance(e.code, int) else 1
    finally:
        T.cargar_ops, T.cargar_grafo = real_ops, real_grafo
        sys.argv, sys.stdout = real_argv, real_out
    salida = buf.getvalue()
    despues_disco = subprocess.run(["git", "status", "--porcelain", "--", "dataset/"],
                                   cwd=RAIZ, capture_output=True, text=True).stdout

    for ln in salida.splitlines():
        print(ln)
    print("=" * 78)
    cae_guarda4 = "guarda 4, la ficha PROHIBE la vuelta y NOMBRA el par: ROJO" in salida
    nombra = "NO NOMBRA este par en sus aristas_nuevas" in salida
    sin_escrituras = antes_disco == despues_disco
    print("codigo de salida: %r (distinto de cero: %s)" % (codigo, codigo != 0))
    print("cae la guarda 4: %s | y nombra el motivo: %s" % (cae_guarda4, nombra))
    print("CERO ESCRITURAS en dataset/: %s" % sin_escrituras)
    ok = codigo != 0 and cae_guarda4 and nombra and sin_escrituras
    print("VEREDICTO: %s" % ("OK, la adicion era necesaria" if ok else "ROJO"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
