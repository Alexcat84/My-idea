# -*- coding: utf-8 -*-
"""vuelta144_3c_caso_positivo_1190.py . EL CASO POSITIVO QUE LA PROPIA FICHA DE
OP-M-04 ESCRIBE (TAREA 3.c, vuelta 144).

LO QUE LA FICHA PIDE, LITERAL, en su verificacion 0:

    "CASO POSITIVO DE LA OPERACION: releido el par 1190 tras la ejecucion,
     tiene que dar D por la vara. Si diera A, la fusion 367 conservo el nodo
     equivocado"

Y EL EXPEDIENTE DICE CUAL ES LA VARA, tambien literal
(docs/plan/EXPEDIENTE_MESA_JUNTA_ASESORA.md, veredicto 1190):

    "el veredicto de este par DEPENDE de lo que sobreviva a la fusion del 367.
     Si el superviviente conserva el paso 6, formalizar sigue siendo su hijo y
     esto es D; si conserva la version de cuatro pasos, formalizar pasa a
     repetir y esto seria A"

O sea que la vara NO se inventa aqui: es la del banco 9.6.1 aplicada al par, y
su bisagra es UNA LINEA, el paso del superviviente que DIFIERE la formalizacion.
EL VEREDICTO SE COMPUTA DEL GRAFO, nunca se teclea:

  D  si el superviviente vivo del par 367 conserva el paso que difiere la
     formalizacion (madre e hijo: uno identifica y el otro formaliza), Y la
     escalera existe en UNA sola direccion tras resolver;
  A  si no lo conserva (los dos dirian lo mismo y el par seria repeticion).

LAS CUATRO COMPROBACIONES:
  (a) EL PAR 1190 RESUELVE. `formalize_advisory_board` e
      `identificar_consejo_asesores` resueltos por alias (P.1) dan los dos
      extremos vivos de hoy.
  (b) EL VEREDICTO POR LA VARA, computado del texto del superviviente.
  (c) LA ESCALERA, en una sola direccion y en la de la escalera.
  (d) LA MUTACION, que es lo que hace que (b) signifique algo (EJECUTOR.md
      regla 1, "EL CASO ROJO SE PRUEBA POR MUTACION"): sobre una COPIA EN
      MEMORIA se le quita al superviviente el paso que difiere la
      formalizacion, que es exactamente el mundo en el que la fusion 367
      hubiera conservado el nodo equivocado, y EL VEREDICTO TIENE QUE PASAR
      A A. Si no pasara, esta vara no mide nada.

SI DA A, SE PARA Y SE TRAE: es la ficha diciendo que el superviviente esta mal
elegido, y eso no se ajusta.

DE SOLO LECTURA. Cero escrituras.
"""
import copy
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import tallar_estado_de_fase as T  # noqa: E402

# LOS DOS EXTREMOS DEL PAR 1190, tal como el expediente los escribe.
PAR_1190 = ("formalize_advisory_board", "identificar_consejo_asesores")
# LA BISAGRA, LITERAL DEL PASO 6 DEL SUPERVIVIENTE Y CITADA: es la unica linea
# de los cuatro nodos que entrega el testigo.
BISAGRA = "formaliza el consejo asesor mas adelante"


def plano(s):
    return "".join(c for c in unicodedata.normalize("NFD", s or "")
                   if unicodedata.category(c) != "Mn").lower()


def paso_que_difiere(nodo):
    """El indice (1..n) del paso que DIFIERE la formalizacion, o None."""
    for i, p in enumerate(nodo.get("pasos_accionables") or [], 1):
        if BISAGRA in plano(p):
            return i
    return None


def veredicto(nodos, resolver):
    """(letra, razon) computados del grafo. Nunca un literal."""
    a, b = (resolver(x) for x in PAR_1190)
    if a == b:
        return None, ("los dos extremos del par 1190 resuelven al MISMO nodo (%s): el par ya "
                      "no existe como par y la vara no se puede aplicar" % a)
    n_a, n_b = nodos.get(a), nodos.get(b)
    if not (T.vivo(n_a) and T.vivo(n_b)):
        return None, "alguno de los dos extremos resueltos no esta vivo: %s, %s" % (a, b)
    # EL SUPERVIVIENTE DEL 367 es el extremo que identifica, o sea el que puede
    # llevar la bisagra. Se busca en LOS DOS, sin suponer cual: si la lleva uno,
    # ese es el que difiere y el otro es su hijo.
    con_bisagra = [(x, paso_que_difiere(nodos[x])) for x in (a, b)]
    con_bisagra = [(x, n) for x, n in con_bisagra if n is not None]
    if len(con_bisagra) == 1:
        x, n = con_bisagra[0]
        otro = b if x == a else a
        return "D", ("%s conserva en su paso %d la linea que DIFIERE la formalizacion, asi "
                     "que %s sigue siendo su hijo y no su gemelo: madre e hijo, CONTINUA"
                     % (x, n, otro))
    if not con_bisagra:
        return "A", ("NINGUNO de los dos extremos conserva la linea que difiere la "
                     "formalizacion: los dos dicen lo mismo al mismo grano y el par es "
                     "REPETICION")
    return None, ("LOS DOS extremos llevan la bisagra (%s): la vara no separa"
                  % ", ".join(x for x, _ in con_bisagra))


def escalera(nodos, resolver, madre, hijo):
    ida, _, _ = T.arista_presente(nodos, resolver, madre, hijo)
    vuelta, _, _ = T.arista_presente(nodos, resolver, hijo, madre)
    return ida, vuelta


def main():
    nodos = T.cargar_grafo("WORK")
    resolver = T.resolver_de(nodos)

    print("CASO POSITIVO DE LA OPERACION OP-M-04 | vuelta 144 | EL PAR 1190")
    print("De solo lectura. El veredicto se COMPUTA del grafo, no se teclea.")
    print("=" * 78)

    # ---- (a) EL PAR RESUELVE ----------------------------------------------
    a, b = (resolver(x) for x in PAR_1190)
    print("(a) EL PAR 1190, resuelto por alias (P.1):")
    for x in PAR_1190:
        print("     %-32s resuelve a %-32s vivo: %s"
              % (x, resolver(x), T.vivo(nodos.get(resolver(x)))))
    print("")

    # ---- (b) EL VEREDICTO POR LA VARA -------------------------------------
    letra, razon = veredicto(nodos, resolver)
    print("(b) EL VEREDICTO POR LA VARA: %s" % letra)
    print("     %s" % razon)
    print("")

    # ---- (c) LA ESCALERA ---------------------------------------------------
    madre, hijo = b, a
    ida, vuelta = escalera(nodos, resolver, madre, hijo)
    una_sola = ida and not vuelta
    print("(c) LA ESCALERA, tras resolver:")
    print("     la IDA    %s -> %s esta puesta: %s" % (madre, hijo, ida))
    print("     la VUELTA %s -> %s esta puesta: %s" % (hijo, madre, vuelta))
    print("     UNA SOLA ARISTA y en la direccion de la escalera: %s" % una_sola)
    print("")

    # ---- (d) LA MUTACION ---------------------------------------------------
    g = copy.deepcopy(nodos)
    quitado = None
    for x in (a, b):
        n = paso_que_difiere(g[x])
        if n is not None:
            quitado = (x, n, g[x]["pasos_accionables"][n - 1])
            g[x]["pasos_accionables"] = [p for j, p in enumerate(g[x]["pasos_accionables"], 1)
                                         if j != n]
            break
    letra_m, razon_m = (None, "no habia bisagra que quitar")
    if quitado:
        letra_m, razon_m = veredicto(g, T.resolver_de(g))
    print("(d) LA MUTACION, el mundo en que la fusion 367 hubiera conservado el nodo "
          "equivocado:")
    if quitado:
        print("     se le quita a %s su paso %d: %r" % (quitado[0], quitado[1], quitado[2][:90]))
    print("     veredicto mutado: %s" % letra_m)
    print("     %s" % razon_m)
    muerde = letra == "D" and letra_m == "A"
    print("     LA VARA MUERDE (de D pasa a A): %s" % muerde)
    print("")

    print("=" * 78)
    ok = letra == "D" and una_sola and muerde
    print("  veredicto del par 1190          : %s (tiene que ser D)" % letra)
    print("  la escalera, una sola direccion : %s" % una_sola)
    print("  la vara probada por mutacion    : %s" % muerde)
    print("")
    if letra == "A":
        print("PARADA: EL PAR 1190 DA A. Es la ficha diciendo que la fusion 367 conservo el "
              "nodo equivocado. NO SE AJUSTA: se para y se trae.")
        return 1
    print("VERDE: el caso positivo de la operacion CALZA." if ok
          else "ROJO: el caso positivo NO calza entero.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
