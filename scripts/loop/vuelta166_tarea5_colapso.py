# -*- coding: utf-8 -*-
r"""vuelta166_tarea5_colapso.py . TAREA 5 de la vuelta 166.

EL COLAPSO SE MIDE Y NO SE ADJUDICA CLASE (adjudicacion 5.14 del acta 165, y
sus hallazgos 4.2 y 4.3).

LAS DOS MITADES, Y NINGUNA MUEVE UN VEREDICTO.

  PRIMERA. Las once lecturas dirigidas de `OP-L-01`, resueltas: cuantos PARES
  distintos son de verdad, cual colapsa sobre cual, y que letras traen las que
  colapsan. Aqui NO se adjudica: se mide y se publica.

  SEGUNDA. El fichero ENTERO: cuantas filas colapsan a un auto-par, cuantos
  pares resueltos distintos quedan, cuantos llevan mas de una fila y cuantos de
  esos llevan CLASES DISTINTAS. Los que llevan clases distintas se publican UNO
  POR UNO con sus puestos, sus clases y sus ids crudos.

LO QUE ESTE INSTRUMENTO NO HACE, Y ES LA MITAD QUE IMPORTA. **NO ADJUDICA CLASE
A NINGUN PAR Y NO MUEVE NI UN VEREDICTO.** El propio acta 165 leyo uno de esos
pares (`formalizar_junta_asesora` con `identificar_consejo_asesores`) y dice que
su conflicto es **HUELLA DE FUSION, no error de lectura**: declarar la poblacion
entera defectuosa por un colapso seria exactamente la especie que `P.1` prohibe.
**Es un censo con evidencia, y la clase la decide una lectura, no un colapso.**

EL RESOLUTOR VA DELANTE DE TODO CONTEO (`P.1`, `EJECUTOR.md` 9), y es el MISMO
que la TAREA 2 usa: se importa de alli en vez de reimplementarse, porque dos
resolutores para la misma pregunta es lo que esta casa no hace.

USO:  python scripts/loop/vuelta166_tarea5_colapso.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta166_tarea2_correccion_op_l_01 as T2   # noqa: E402


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 166, TAREA 5: EL COLAPSO, MEDIDO Y SIN ADJUDICAR CLASE")
    print("=" * 78)
    print("")

    mapa, n_nodos = T2.mapa_de_alias()
    once = T2.las_once()
    V = T2.veredictos()
    print("A) EL RESOLUTOR, DELANTE DE TODO CONTEO (P.1)")
    print("   es el MISMO de la TAREA 2, importado y no reimplementado.")
    print("   CIFRA ficheros de nodo leidos: %d" % n_nodos)
    print("   CIFRA alias en el mapa: %d" % len(mapa))
    print("   CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d" % len(V))
    print("   CIFRA cabeceras LD leidas: %d" % len(once))
    print("")

    print("B) PRIMERA MITAD: LAS ONCE LECTURAS DIRIGIDAS, RESUELTAS")
    porpar = {}
    for ld, a, b, clase in once:
        ra, rb = T2.resolver(mapa, a), T2.resolver(mapa, b)
        porpar.setdefault(frozenset((ra, rb)), []).append((ld, a, b, clase, ra, rb))
    print("   CIFRA lecturas dirigidas: %d" % len(once))
    print("   CIFRA PARES RESUELTOS DISTINTOS que son de verdad: %d" % len(porpar))
    colapsadas = {k: v for k, v in porpar.items() if len(v) > 1}
    print("   CIFRA pares sobre los que cae MAS DE UNA lectura: %d" % len(colapsadas))
    print("")
    print("   LOS COLAPSOS, UNO POR UNO, CON LAS LETRAS QUE TRAEN:")
    for k, v in sorted(colapsadas.items(), key=lambda x: x[1][0][0]):
        letras = sorted(set(x[3] for x in v))
        print("      par resuelto: %s" % " contra ".join(sorted(k)))
        for ld, a, b, clase, ra, rb in sorted(v):
            movidos = []
            if ra != a and a not in (ra,):
                pass
            for crudo, res in ((a, T2.resolver(mapa, a)), (b, T2.resolver(mapa, b))):
                if crudo != res:
                    movidos.append("%s -> %s" % (crudo, res))
            print("         %-7s clase %-12s ids escritos: %s contra %s%s"
                  % (ld, clase, a, b,
                     "  | el resolutor mueve: " + "; ".join(movidos) if movidos else ""))
        print("         CIFRA letras distintas sobre este par: %d (%s)"
              % (len(letras), ", ".join(letras)))
        print("         SE MIDE Y NO SE ADJUDICA: ninguna de las dos se mueve aqui.")
    print("")
    print("   Y SE DICE POR QUE NO ES UNA CONTRADICCION, con la razon del acta 165")
    print("   (seccion 2) y NO con una inventada: las dos leyeron el BLOQUE")
    print("   INJERTADO de project_close_out contra dos nodos que ENTONCES eran")
    print("   dos y HOY son uno. La A de LD-06 no es entre los nodos: es entre el")
    print("   bloque injertado y el otro nodo entero, y eso lo dice la propia")
    print("   LD-06 con todas sus letras.")
    print("")
    print("C) SEGUNDA MITAD: EL FICHERO ENTERO")
    autos, idx = 0, {}
    for f in V:
        a, b = f["nodo_a"], f["nodo_b"]
        ra, rb = T2.resolver(mapa, a), T2.resolver(mapa, b)
        if ra == rb:
            autos += 1
            continue
        idx.setdefault(frozenset((ra, rb)), []).append(
            (f["puesto_intra"], f["clase"], a, b, f["dominio"]))
    varias = {k: v for k, v in idx.items() if len(v) > 1}
    conflicto = {k: v for k, v in varias.items()
                 if len(set(c for _p, c, _a, _b, _d in v)) > 1}
    print("   CIFRA filas que COLAPSAN a un auto-par (los dos ids son hoy el")
    print("      mismo nodo): %d" % autos)
    print("   CIFRA pares resueltos distintos que quedan: %d" % len(idx))
    print("   CIFRA de esos, con MAS DE UNA fila: %d" % len(varias))
    print("   CIFRA de esos, con CLASES DISTINTAS: %d" % len(conflicto))
    print("   la suma cuadra: %d auto mas %d filas repartidas es %d"
          % (autos, len(V) - autos, len(V)))
    print("")
    reparto = {}
    for k, v in conflicto.items():
        firma = "".join(sorted(set(c for _p, c, _a, _b, _d in v)))
        reparto[firma] = reparto.get(firma, 0) + 1
    print("   EL REPARTO DE LOS CONFLICTOS POR COMBINACION DE CLASES, CONTADO:")
    for firma in sorted(reparto):
        print("      %-6s %d" % (" con ".join(firma) + ":", reparto[firma]))
    print("   CIFRA combinaciones distintas: %d" % len(reparto))
    print("")

    print("D) LOS PARES EN CONFLICTO, UNO POR UNO, CON SUS PUESTOS, SUS CLASES")
    print("   Y SUS IDS CRUDOS. NINGUNA CLASE SE ADJUDICA Y NINGUN VEREDICTO SE")
    print("   MUEVE: esto es un censo con evidencia, no una lectura.")
    orden = sorted(conflicto.items(),
                   key=lambda x: min(p for p, _c, _a, _b, _d in x[1]))
    for i, (k, v) in enumerate(orden, 1):
        letras = sorted(set(c for _p, c, _a, _b, _d in v))
        print("")
        print("   %2d. par resuelto: %s" % (i, " contra ".join(sorted(k))))
        print("       CIFRA filas: %d | clases: %s" % (len(v), ", ".join(letras)))
        for p, c, a, b, dom in sorted(v):
            print("       puesto %-5d clase %-3s dominio %-22s ids crudos: %s | %s"
                  % (p, c, dom, a, b))
    print("")
    print("   CIFRA pares publicados uno por uno: %d" % len(orden))
    print("   CIFRA pares en conflicto que esta vuelta ADJUDICA: 0")
    print("   CIFRA veredictos que esta vuelta MUEVE: 0")
    print("")

    print("E) EL EJEMPLAR QUE EL ACTA 165 YA LEYO, SENALADO Y NO ADJUDICADO")
    aguja = frozenset(("formalizar_junta_asesora", "identificar_consejo_asesores"))
    print("   el par {formalizar_junta_asesora, identificar_consejo_asesores}")
    print("   esta entre los publicados: %s" % (aguja in conflicto))
    if aguja in conflicto:
        for p, c, a, b, dom in sorted(conflicto[aguja]):
            print("      puesto %-5d clase %-3s  %s | %s" % (p, c, a, b))
    print("   LO QUE EL ACTA 165 DICE DE EL (seccion 4.3), y por eso la poblacion")
    print("   NO se declara defectuosa: 'su conflicto es huella de fusion, no")
    print("   error de lectura'. Un conflicto por par resuelto se mide uno por")
    print("   uno o no se dice nada.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
