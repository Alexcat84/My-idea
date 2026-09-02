# -*- coding: utf-8 -*-
r"""vuelta141_3b_citar_lineas.py . LA VARA DEL 9.22 SOBRE LOS SEIS PARES, CON
CADA LINEA CITADA DEL NODO DE HOY (TAREA 3.b de la vuelta 141).

QUE HACE. Para cada una de las doce direcciones de los seis pares, imprime:
la lectura dirigida que la sostiene, EN QUE NODO vive la linea que expande, EL
NUMERO DE PASO EN EL NODO DE HOY, y EL TEXTO DE ESE PASO LEIDO DEL GRAFO. La
adjudicacion (MUTUO o ESCALERA) se computa aqui de una sola regla, la del banco
9.22: dos lineas distintas, una en cada nodo, es ENLACE MUTUO; la misma linea,
o una sola linea, es ESCALERA.

POR QUE EXISTE. EJECUTOR.md regla 1: la cita se imprime del nodo, no se teclea,
y el paso se cita POR SU NUMERO EN EL NODO DE HOY y no por el de la ficha del
12 ago 2026 (guarda 3.a del encargo). Si un paso se mueve de sitio, esta salida
cambia y la cita deja de calzar, en vez de envejecer en silencio.

LO QUE ESTE INSTRUMENTO NO HACE: no decide. El PAR, la DIRECCION, la LECTURA
DIRIGIDA y EL NUMERO DE PASO son la LECTURA DEL EJECUTOR, escrita en LECTURAS,
y van marcados DISCUTIBLES en el reporte. Lo que el instrumento aporta es que
el texto de cada linea salga del grafo de hoy y que la adjudicacion se compute
de la regla en vez de escribirse a mano.

USO:
  python scripts/loop/vuelta141_3b_citar_lineas.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T

SGK = "sistema_gates_go_kill"

# LA LECTURA DEL EJECUTOR, PAR POR PAR. Cada direccion trae: (origen, destino,
# lectura dirigida, nodo donde vive la linea, numero de paso EN EL NODO DE HOY).
# Nada de esto es una medicion: es la lectura, y va marcada DISCUTIBLE.
LECTURAS = [
    ("PAR 1", SGK, "gestion_portafolio_dos_niveles", [
        ("gestion_portafolio_dos_niveles", SGK, "LD-35 y LD-51 (OP-E-04) y LD-43 (OP-E-05)",
         "gestion_portafolio_dos_niveles", 1),
        (SGK, "gestion_portafolio_dos_niveles", "LD-43 (OP-E-05)", SGK, 10),
    ]),
    ("PAR 2", SGK, "gestion_portafolio_formal", [
        ("gestion_portafolio_formal", SGK, "LD-49 (OP-E-04) y LD-41 (OP-E-05)",
         "gestion_portafolio_formal", 6),
        (SGK, "gestion_portafolio_formal", "LD-41 (OP-E-05)", SGK, 10),
    ]),
    ("PAR 3", SGK, "portfolio_management", [
        (SGK, "portfolio_management", "LD-40 (OP-E-04)", SGK, 10),
        ("portfolio_management", SGK, "LD-48 (OP-E-04)", "portfolio_management", 4),
    ]),
    ("PAR 4", SGK, "gestion_portafolio_foco", [
        (SGK, "gestion_portafolio_foco", "LD-45 (OP-E-04)", SGK, 10),
        ("gestion_portafolio_foco", SGK, "LD-53 (OP-E-04)", "gestion_portafolio_foco", 2),
    ]),
    ("PAR 5", SGK, "revision_portafolio_periodica", [
        (SGK, "revision_portafolio_periodica", "LD-42 (OP-E-04)", SGK, 10),
        ("revision_portafolio_periodica", SGK,
         "SIN LECTURA QUE LA PROPONGA. La arista la fabrico la redireccion de 3f249a03 "
         "sobre revision_portafolio_periodica -> gates_go_kill_decision_points, que LD-50 "
         "leyo y declaro 'bien puesta' SIN jerarquia ('no hay jerarquia: hay dos decisiones "
         "distintas'). NINGUNA LINEA DEL SUPERVIVIENTE LA EXPANDE", None, None),
    ]),
    ("PAR 6", SGK, "asignacion_recursos_en_gates", [
        (SGK, "asignacion_recursos_en_gates", "LD-57 (OP-M-01-ESLABONES)", SGK, 5),
        ("asignacion_recursos_en_gates", SGK,
         "SIN LECTURA QUE LA PROPONGA. La arista la fabrico la misma redireccion sobre "
         "asignacion_recursos_en_gates -> estructura_de_gates. NINGUNA LINEA DEL "
         "SUPERVIVIENTE LA EXPANDE que no sea la misma del paso 5", None, None),
    ]),
]


def paso_de(nodos, nid, numero):
    n = nodos.get(nid) or {}
    pasos = n.get("pasos_accionables") or []
    if numero is None or numero < 1 or numero > len(pasos):
        return None
    p = pasos[numero - 1]
    if isinstance(p, dict):
        p = p.get("texto") or p.get("paso") or str(p)
    return p


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    nodos = T.cargar_grafo("WORK")
    resolver = T.resolver_de(nodos)

    print("=" * 78)
    print("TAREA 3.b: LA VARA DEL 9.22 SOBRE LOS SEIS PARES")
    print("La regla, literal del banco 9.22: 'La figura exige dos lineas distintas, una en")
    print("cada nodo'; 'si las dos direcciones apuntan a la misma linea, no es esta figura'.")
    print("=" * 78)

    for etiqueta, a, b, direcciones in LECTURAS:
        print("")
        print("-" * 78)
        print("%s: %s CONTRA %s" % (etiqueta, a, b))
        ida, _, _ = T.arista_presente(nodos, resolver, a, b)
        vue, _, _ = T.arista_presente(nodos, resolver, b, a)
        print("  estado medido hoy: %s -> %s %s | %s -> %s %s"
              % (a, b, "PRESENTE" if ida else "no presente",
                 b, a, "PRESENTE" if vue else "no presente"))
        print("")
        lineas = []
        for origen, destino, lectura, nodo_linea, numero in direcciones:
            print("  DIRECCION %s -> %s" % (origen, destino))
            print("     lectura dirigida: %s" % lectura)
            if nodo_linea is None:
                print("     linea que expande: NINGUNA")
                lineas.append(None)
                continue
            texto = paso_de(nodos, nodo_linea, numero)
            if texto is None:
                print("     ROJO: %s no tiene paso %s hoy" % (nodo_linea, numero))
                lineas.append(("ROJO", nodo_linea, numero))
                continue
            print("     linea que expande: %s, paso %d EN EL NODO DE HOY" % (nodo_linea, numero))
            print("     texto, LEIDO DEL GRAFO: %s" % texto)
            lineas.append((nodo_linea, numero))
        print("")
        # LA ADJUDICACION SE COMPUTA DE LA REGLA, no se escribe a mano.
        validas = [x for x in lineas if x is not None]
        distintas = len(set(validas))
        en_cada_nodo = len({x[0] for x in validas}) == 2 if len(validas) == 2 else False
        if len(validas) == 2 and distintas == 2 and en_cada_nodo:
            veredicto = "ENLACE MUTUO (dos lineas distintas, una en cada nodo)"
        elif len(validas) < 2:
            veredicto = ("ESCALERA (solo UNA direccion se apoya en una linea; la otra no "
                         "expande ninguna)")
        elif distintas == 1:
            veredicto = "ESCALERA (las dos direcciones apuntan a LA MISMA linea)"
        else:
            veredicto = ("ESCALERA (las dos lineas viven en el MISMO nodo: la figura exige "
                         "una en cada uno)")
        print("  ADJUDICACION POR LA VARA DEL 9.22: %s" % veredicto)
        print("  DISCUTIBLE, marcado antes de saber si acierto.")
    print("")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
