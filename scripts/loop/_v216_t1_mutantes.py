# -*- coding: utf-8 -*-
r"""_v216_t1_mutantes.py . LA PRUEBA DE MUTACION DE LAS GUARDAS DE LA TAREA 1.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

POR QUE EXISTE: EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION. Ninguna
guarda se publica como prueba sin haber corrido antes su prueba de mutacion: se
cambia el valor esperado y se comprueba que el caso CAE.

QUE MUTA, Y NO ES EL ACTA. El acta no se toca ni un byte: lo que se muta es LA
LISTA DE ENTRADAS que el lector saca de ella, que es la entrada de juzgar().
Cada mutante rompe UNA cosa y se exige que la guarda correspondiente lo cace.

EL CASO BUENO TAMBIEN CORRE: el texto real tiene que pasar el mismo juicio en
CERO fallos, o el juicio seria un rechazo de todo y no una guarda.

USO:  python scripts/loop/_v216_t1_mutantes.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _v216_t1_registros as R  # noqa: E402


def main():
    lineas = R.lineas_del_acta()
    ini, fin = R.rango_del_acta(lineas, R.ACTA_QUE_SE_LEE)
    todas = R.entradas(lineas, ini, fin)
    adj = [e for e in todas if e[0].startswith("5.")]
    hall = [e for e in todas if e[0].startswith("3.")]
    anclados = [(etiqueta, R.anclar(lineas, ini, fin, aguja))
                for etiqueta, aguja in R.ANCLAJES]
    items6 = R.items_de_la_seccion_6(lineas, ini, fin)

    print("EL TEXTO BUENO, POR EL MISMO JUICIO QUE LOS MUTANTES")
    fallos, informe = R.juzgar(adj, hall, anclados, items6)
    for l in informe:
        print("   " + l)
    print("CIFRA fallos del texto bueno: %d (se exigen 0)" % fallos)
    if fallos != 0:
        print("ROJO: el texto bueno no pasa su propio juicio.")
        return 1
    print("")

    sin_una_ancla = [(anclados[0][0], []), anclados[1], anclados[2]]
    ancla_doble = [(anclados[0][0], anclados[0][1] * 2), anclados[1], anclados[2]]

    mutantes = [
        ("A. FALTA UNA ADJUDICACION (se quita la 5.3)",
         [e for e in adj if e[0] != "5.3"], hall, anclados, items6),
        ("B. FALTA UNA DE LAS CUATRO QUE OBLIGAN (se quita la 5.7)",
         [e for e in adj if e[0] != "5.7"], hall, anclados, items6),
        ("C. UNA ETIQUETA RENUMERADA (la 5.8 pasa a 5.9, y siguen siendo ocho)",
         [(("5.9" if e[0] == "5.8" else e[0]), e[1], e[2]) for e in adj],
         hall, anclados, items6),
        ("D. UNA ADJUDICACION DE MAS (la 5.4 duplicada, y son nueve)",
         adj + [e for e in adj if e[0] == "5.4"], hall, anclados, items6),
        ("E. FALTA UN HALLAZGO DE LA SECCION 3 (se quita el 3.1)",
         adj, [e for e in hall if e[0] != "3.1"], anclados, items6),
        ("F. UN ANCLAJE QUE NO APARECE (la correccion de las CUATRO fichas)",
         adj, hall, sin_una_ancla, items6),
        ("G. UN ANCLAJE QUE APARECE DOS VECES, QUE ES CITA AMBIGUA",
         adj, hall, ancla_doble, items6),
        ("H. LA SECCION 6 SIN NINGUN PUNTO",
         adj, hall, anclados, []),
        ("I. TODO VACIO, QUE ES EL CASO DE UN LECTOR QUE NO ENCUENTRA NADA",
         [], [], [(e[0], []) for e in anclados], []),
    ]
    caen = 0
    for nombre, m_adj, m_hall, m_anc, m_i6 in mutantes:
        f, inf = R.juzgar(m_adj, m_hall, m_anc, m_i6)
        cae = f > 0
        caen += 1 if cae else 0
        print("MUTANTE %s" % nombre)
        print("   CIFRA fallos: %d | CAE: %s (se exige CAE SI)"
              % (f, "SI" if cae else "NO"))
        for l in inf:
            print("      " + l)
    print("")
    print("CIFRA mutantes: %d | CIFRA mutantes que CAEN: %d"
          % (len(mutantes), caen))
    if caen != len(mutantes):
        print("ROJO: algun mutante PASA el juicio, o sea que la guarda no muerde.")
        return 1
    print("VERDE: el texto bueno pasa en 0 fallos y los %d mutantes caen."
          % len(mutantes))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
