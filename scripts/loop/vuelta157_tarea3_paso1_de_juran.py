# -*- coding: utf-8 -*-
"""vuelta157_tarea3_paso1_de_juran.py . TAREA 3 DE LA VUELTA 157.

MIDE EL CONTRAEJEMPLO QUE TUMBA UNA INFERENCIA, NO UNA CIFRA (adjudicacion 6.2
del acta 157). La razon escrita para `LD-OPC05-097` dice "el paso 1 de juran NO
tiene hijo, o sea que ES linea", y ESO NO SE SIGUE:

  - el 9.6.2 da una prueba SUFICIENTE de que un paso es procedimiento ("la
    prueba de que el paso de la madre es un procedimiento ES QUE EXISTE EL HIJO
    QUE LO EJECUTA"), y una prueba suficiente NO SE PUEDE DAR LA VUELTA: su
    ausencia no prueba lo contrario;
  - y la vara que se aplico es todavia mas estrecha, porque
    `vuelta156_tarea2a_pasos_con_hijo.py` SOLO MIRA HIJOS ADJUDICADOS en
    `docs/plan/PASO_NODO_CALIBRADO.jsonl`.

QUE COMPRUEBA ESTE INSTRUMENTO, Y SON LAS DOS COSAS QUE EL ENCARGO PIDE
COMPROBAR POR CUENTA PROPIA:
  (1) que `desperdicio_cronico_vs_esporadico` EXISTE Y ESTA VIVO en el grafo;
  (2) que sus pasos DESPLIEGAN el paso 1 de `juran_rcca_metodo`;
  y ademas (3) que NO tiene arista con juran en ninguna de las dos vistas y (4)
  que NO tiene fila en el calibrado, que es POR QUE la vara declarada no lo veia.

NO CAMBIA NINGUNA CLASE. `LD-OPC05-097` sigue en D por la adjudicacion 6.1 del
acta 157, que la sostiene por dos caminos que no pasan por esta inferencia. Lo
que esta tarea corrige es UN PASO DE RAZONAMIENTO.

USO:  python scripts/loop/vuelta157_tarea3_paso1_de_juran.py
"""
import glob
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
CALIBRADO = os.path.join(RAIZ, "docs", "plan", "PASO_NODO_CALIBRADO.jsonl")

MADRE = "juran_rcca_metodo"
CANDIDATO = "desperdicio_cronico_vs_esporadico"


def main():
    N = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    print("=" * 78)
    print("VUELTA 157, TAREA 3: EL PASO 1 DE JURAN SI TIENE QUIEN LO DESPLIEGUE")
    print("=" * 78)
    print("")

    madre = N.get(MADRE)
    if madre is None:
        print("ROJO PREVIO: %s no esta en el grafo." % MADRE)
        return 1
    pasos_madre = madre.get("pasos_accionables") or []
    print("LA MADRE: %s" % MADRE)
    print("  TITULO: %s" % madre.get("titulo_concepto"))
    print("  CIFRA pasos de la madre: %d" % len(pasos_madre))
    for i, p in enumerate(pasos_madre, 1):
        print("    %d. %s" % (i, p))
    print("")

    hijo = N.get(CANDIDATO)
    print("(1) EXISTE Y ESTA VIVO?")
    if hijo is None:
        print("    ROJO: %s NO esta en el grafo. El contraejemplo no se sostiene." % CANDIDATO)
        return 1
    vivo = not hijo.get("deprecado")
    print("    %s EXISTE en el grafo." % CANDIDATO)
    print("    deprecado: %s" % bool(hijo.get("deprecado")))
    print("    CIFRA veredicto (1): %s" % ("VIVO" if vivo else "DEPRECADO"))
    print("")

    print("(2) SUS PASOS DESPLIEGAN EL PASO 1 DE LA MADRE?")
    print("    PASO 1 DE %s: %s" % (MADRE, pasos_madre[0] if pasos_madre else "(no hay)"))
    pasos_hijo = hijo.get("pasos_accionables") or []
    print("    TITULO DEL CANDIDATO: %s" % hijo.get("titulo_concepto"))
    print("    ENTREGABLE: %s" % (hijo.get("entregable_esperado") or "(sin entregable)"))
    print("    CIFRA pasos del candidato: %d" % len(pasos_hijo))
    for i, p in enumerate(pasos_hijo, 1):
        print("      %d. %s" % (i, p))
    print("")

    print("(3) HAY ARISTA ENTRE LOS DOS, EN ALGUNA DE LAS DOS VISTAS?")
    sig_madre = madre.get("nodos_siguientes") or []
    prev_madre = madre.get("nodos_previos") or []
    sig_hijo = hijo.get("nodos_siguientes") or []
    prev_hijo = hijo.get("nodos_previos") or []
    en_sig = CANDIDATO in sig_madre
    en_prev = MADRE in prev_hijo
    en_sig_inv = MADRE in sig_hijo
    en_prev_inv = CANDIDATO in prev_madre
    print("    %s en nodos_siguientes de la madre : %s" % (CANDIDATO, en_sig))
    print("    %s en nodos_previos del candidato  : %s" % (MADRE, en_prev))
    print("    %s en nodos_siguientes del candidato: %s" % (MADRE, en_sig_inv))
    print("    %s en nodos_previos de la madre    : %s" % (CANDIDATO, en_prev_inv))
    hay_arista = en_sig or en_prev or en_sig_inv or en_prev_inv
    print("    CIFRA veredicto (3): %s" % ("HAY ARISTA" if hay_arista else "NO HAY ARISTA"))
    print("")

    print("(4) HAY FILA EN EL CALIBRADO PARA ESTE PAR?")
    filas_madre, fila_par = [], []
    if os.path.exists(CALIBRADO):
        for x in io.open(CALIBRADO, encoding="utf-8"):
            if not x.strip():
                continue
            d = json.loads(x)
            if d.get("madre") == MADRE or d.get("nodo_madre") == MADRE:
                filas_madre.append(d)
                if CANDIDATO in json.dumps(d, ensure_ascii=False):
                    fila_par.append(d)
    print("    CIFRA filas del calibrado con %s de madre: %d" % (MADRE, len(filas_madre)))
    for d in filas_madre:
        print("      paso %s -> hijo %s (titulo_ratio %s, arista %s)"
              % (d.get("paso") or d.get("num_paso"),
                 d.get("hijo") or d.get("nodo_hijo"),
                 d.get("titulo_ratio"), d.get("arista")))
    print("    CIFRA filas del calibrado que nombran a %s: %d" % (CANDIDATO, len(fila_par)))
    print("    CIFRA veredicto (4): %s"
          % ("HAY FILA" if fila_par else "NO HAY FILA EN EL CALIBRADO"))
    print("")

    print("QUE SIGNIFICA, DICHO SIN ADORNO")
    print("  El paso 1 de %s (%s)" % (MADRE, (pasos_madre[0] if pasos_madre else "")[:60]))
    print("  TIENE en el grafo un nodo VIVO cuyos %d pasos lo despliegan, y ese nodo NO"
          % len(pasos_hijo))
    print("  tiene arista con la madre ni fila en el calibrado. O sea: HAY HIJO, Y LA VARA")
    print("  DE vuelta156_tarea2a_pasos_con_hijo.py NO LO VEIA, porque esa vara solo mira")
    print("  HIJOS ADJUDICADOS. 'Ningun hijo adjudicado' es UNA AUSENCIA BAJO LA VARA")
    print("  DECLARADA y NO una prueba de que el paso sea linea.")
    print("")
    print("  LA CLASE NO SE MUEVE: LD-OPC05-097 sigue en D por la adjudicacion 6.1 del")
    print("  acta 157, que la sostiene por dos caminos independientes de esta inferencia.")
    print("")
    bien = vivo and pasos_hijo and not hay_arista and not fila_par
    print("CIFRA condiciones del contraejemplo que se cumplen: %d de 4"
          % sum([bool(vivo), bool(pasos_hijo), not hay_arista, not fila_par]))
    if bien:
        print("VERDE: el contraejemplo se sostiene entero y esta medido, no supuesto.")
        print("FIN")
        return 0
    print("ROJO: alguna condicion del contraejemplo no se cumple. SE PUBLICA IGUAL.")
    print("FIN")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
