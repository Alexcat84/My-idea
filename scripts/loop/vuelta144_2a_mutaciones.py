# -*- coding: utf-8 -*-
"""vuelta144_2a_mutaciones.py . LAS CUATRO MUTACIONES DE LA TAREA 2.a, v144.

Prueban que la FORMULA CANONICA de la excepcion del 9.22 (CORRECCION 19) falla
RUIDOSO en sus tres extremos y no lee de mas nunca:

  (i)   quitada la marca de CIERRE   -> ROJO nombrandola y CERO pares.
        Con la lectura VIEJA daba 5 pares EN SILENCIO, y el 5.o era justo el
        par que la excepcion niega. Se mide el contraste al lado.
  (ii)  quitada la marca de APERTURA -> ROJO nombrandola y CERO pares.
        Con la lectura VIEJA daba 4 pares EN SILENCIO (anclaba en la primera
        ocurrencia de "doble linea", que no es la formula).
  (iii) DUPLICADA la marca de apertura -> ROJO POR AMBIGUA y CERO pares.
  (iv)  la ficha entera y bien formada -> los CUATRO pares de siempre y CERO
        fallos. ES LA CONTRAPRUEBA: sin ella, tres rojos no prueban nada,
        porque una funcion que siempre diga ROJO tambien los daria.

TODO EN MEMORIA Y CON CERO ESCRITURAS. El sujeto se ELIGE POR COMPUTO (la
primera ficha que dispare la excepcion con pares nombrados) y los veredictos se
comparan contra VARIABLES QUE EL CODIGO COMPUTA, nunca contra literales
(EJECUTOR.md regla 1, "EL CASO ROJO SE PRUEBA POR MUTACION").
"""
import argparse
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import tallar_estado_de_fase as T  # noqa: E402
import vuelta144_1b_medir_ventana as V  # noqa: E402  (trae la lectura VIEJA)


def clonar(op):
    return json.loads(json.dumps(op))


def sin_literal(linea, literal):
    """Quita LA PRIMERA ocurrencia del literal, respetando la caja real del
    texto. Devuelve (linea_nueva, se_quito)."""
    i = linea.lower().find(literal.lower())
    if i < 0:
        return linea, False
    return linea[:i] + linea[i + len(literal):], True


def duplicar_literal(linea, literal):
    """Inserta UNA copia mas del literal justo delante de su ocurrencia."""
    i = linea.lower().find(literal.lower())
    if i < 0:
        return linea, False
    trozo = linea[i:i + len(literal)]
    return linea[:i] + trozo + " " + linea[i:], True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fase", default="06_MESAS")
    a = ap.parse_args()

    nodos = T.cargar_grafo("WORK")
    resolver = T.resolver_de(nodos)
    ops = T.cargar_ops("WORK")

    print("MUTACIONES DE LA TAREA 2.a | vuelta 144 | FASE %s" % a.fase)
    print("Todo EN MEMORIA, cero escrituras. Sujeto y veredictos POR COMPUTO.")
    print("=" * 78)

    # ---- EL SUJETO, POR COMPUTO -------------------------------------------
    sujeto = None
    for op in ops:
        conj, cita, nomina = T.pares_exceptuados_de(op, resolver, [])
        if conj:
            sujeto, base_conj, base_cita, base_nomina = op, conj, cita, nomina
            break
    if sujeto is None:
        print("OMITIDO POR FALTA DE SUJETO: ninguna ficha dispara la excepcion con pares "
              "nombrados. ESO ES ROJO, no verde.")
        return 1

    # La linea que dispara, tambien por computo.
    idx = None
    for i, linea in enumerate(sujeto.get("verificacion") or []):
        if any(f in (linea or "").lower() for f in T.FRASES_EXCEPCION_PAR):
            idx = i
            break
    linea_base = sujeto["verificacion"][idx]

    print("SUJETO ELEGIDO POR COMPUTO: %s, verificacion %d (%d caracteres)"
          % (sujeto.get("id_op"), idx, len(linea_base)))
    print("   excepcion disparada por: %s" % base_cita)
    print("   pares que saca la ficha entera: %d" % len(base_conj))
    print("")

    resultados = []

    # ---- (iv) LA CONTRAPRUEBA, primero: la ficha entera --------------------
    fallos_iv = []
    conj_iv, _, nom_iv = T.pares_exceptuados_de(sujeto, resolver, fallos_iv)
    n_iv, f_iv = len(conj_iv), len(fallos_iv)
    ok_iv = n_iv == len(base_conj) and f_iv == 0 and n_iv > 0
    print("(iv) CONTRAPRUEBA, ficha entera y bien formada:")
    print("     pares: %d | fallos: %d" % (n_iv, f_iv))
    for x in nom_iv:
        print("       %s" % x)
    print("     VEREDICTO: %s" % ("OK" if ok_iv else "ROJO"))
    resultados.append(("(iv) contraprueba, ficha entera", ok_iv,
                       "%d pares y %d fallos" % (n_iv, f_iv)))
    print("")

    # ---- (i) SIN LA MARCA DE CIERRE ---------------------------------------
    op_i = clonar(sujeto)
    nueva, quito = sin_literal(linea_base, T.MARCA_CIERRA_EXCEPCION)
    op_i["verificacion"][idx] = nueva
    fallos_i = []
    conj_i, _, _ = T.pares_exceptuados_de(op_i, resolver, fallos_i)
    # CONTRASTE con la lectura VIEJA, sobre la MISMA mutilacion de su modo.
    op_i_viejo = clonar(sujeto)
    nueva_v, _ = sin_literal(linea_base, V.CIERRA_VIEJA)
    op_i_viejo["verificacion"][idx] = nueva_v
    fallos_i_old = []
    conj_i_viejo, _, _ = V._ventana_vieja(op_i_viejo, resolver, fallos_i_old)
    nombra_cierre = any(T.MARCA_CIERRA_EXCEPCION.upper() in f for f in fallos_i)
    ok_i = quito and len(conj_i) == 0 and len(fallos_i) == 1 and nombra_cierre
    print("(i) QUITADA LA MARCA DE CIERRE:")
    print("     literal quitado de verdad: %s" % quito)
    print("     pares: %d | fallos: %d | el fallo NOMBRA la marca de cierre: %s"
          % (len(conj_i), len(fallos_i), nombra_cierre))
    for f in fallos_i:
        print("       FALLO: %s" % f)
    print("     CONTRASTE con la lectura VIEJA sobre su propio literal de cierre: "
          "%d pares y %d fallos (EN SILENCIO)" % (len(conj_i_viejo), len(fallos_i_old)))
    print("     VEREDICTO: %s" % ("OK" if ok_i else "ROJO"))
    resultados.append(("(i) sin marca de cierre", ok_i,
                       "%d pares, %d fallos, nombra la marca: %s"
                       % (len(conj_i), len(fallos_i), nombra_cierre)))
    print("")

    # ---- (ii) SIN LA MARCA DE APERTURA ------------------------------------
    op_ii = clonar(sujeto)
    nueva2, quito2 = sin_literal(linea_base, T.MARCA_ABRE_EXCEPCION)
    op_ii["verificacion"][idx] = nueva2
    fallos_ii = []
    conj_ii, _, _ = T.pares_exceptuados_de(op_ii, resolver, fallos_ii)
    # CONTRASTE: la lectura VIEJA, sobre la ficha SIN mutar, sacaba sus pares
    # anclando en una ocurrencia que NO es la formula, y sin decir nada.
    fallos_ii_old = []
    conj_ii_viejo, _, _ = V._ventana_vieja(sujeto, resolver, fallos_ii_old)
    nombra_apertura = any(T.MARCA_ABRE_EXCEPCION.upper() in f for f in fallos_ii)
    ok_ii = quito2 and len(conj_ii) == 0 and len(fallos_ii) == 1 and nombra_apertura
    print("(ii) QUITADA LA MARCA DE APERTURA:")
    print("     literal quitado de verdad: %s" % quito2)
    print("     pares: %d | fallos: %d | el fallo NOMBRA la marca de apertura: %s"
          % (len(conj_ii), len(fallos_ii), nombra_apertura))
    for f in fallos_ii:
        print("       FALLO: %s" % f)
    print("     CONTRASTE: la lectura VIEJA, sobre la ficha SIN mutar, anclaba en la "
          "primera ocurrencia de su literal viejo y sacaba %d pares con %d fallos"
          % (len(conj_ii_viejo), len(fallos_ii_old)))
    print("     VEREDICTO: %s" % ("OK" if ok_ii else "ROJO"))
    resultados.append(("(ii) sin marca de apertura", ok_ii,
                       "%d pares, %d fallos, nombra la marca: %s"
                       % (len(conj_ii), len(fallos_ii), nombra_apertura)))
    print("")

    # ---- (iii) MARCA DE APERTURA DUPLICADA --------------------------------
    op_iii = clonar(sujeto)
    nueva3, duplico = duplicar_literal(linea_base, T.MARCA_ABRE_EXCEPCION)
    op_iii["verificacion"][idx] = nueva3
    fallos_iii = []
    conj_iii, _, _ = T.pares_exceptuados_de(op_iii, resolver, fallos_iii)
    dice_ambigua = any("AMBIGUA" in f for f in fallos_iii)
    ok_iii = duplico and len(conj_iii) == 0 and len(fallos_iii) == 1 and dice_ambigua
    print("(iii) DUPLICADA LA MARCA DE APERTURA:")
    print("     literal duplicado de verdad: %s (ocurrencias en la linea mutada: %d)"
          % (duplico, nueva3.lower().count(T.MARCA_ABRE_EXCEPCION)))
    print("     pares: %d | fallos: %d | el fallo dice AMBIGUA: %s"
          % (len(conj_iii), len(fallos_iii), dice_ambigua))
    for f in fallos_iii:
        print("       FALLO: %s" % f)
    print("     VEREDICTO: %s" % ("OK" if ok_iii else "ROJO"))
    resultados.append(("(iii) marca de apertura duplicada", ok_iii,
                       "%d pares, %d fallos, dice AMBIGUA: %s"
                       % (len(conj_iii), len(fallos_iii), dice_ambigua)))
    print("")

    print("=" * 78)
    buenas = sum(1 for _, ok, _ in resultados if ok)
    for nombre, ok, detalle in resultados:
        print("  %-38s %s   (%s)" % (nombre, "OK  " if ok else "ROJO", detalle))
    print("")
    print("MUTACIONES QUE MUERDEN: %d de %d" % (buenas, len(resultados)))
    return 0 if buenas == len(resultados) else 1


if __name__ == "__main__":
    raise SystemExit(main())
