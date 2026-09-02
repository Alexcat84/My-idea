# -*- coding: utf-8 -*-
r"""vuelta145_2a_mutacion_ancla_unica.py . LAS MUTACIONES DE LA TAREA 2.a,
VUELTA 145: EL ANCLA UNICA EN LOS TRES PARES DE MARCAS.

QUE PRUEBA. Que `quitar_bloques_cubiertos()` de
scripts/loop/verificar_cifras_del_reporte.py deja de anclar en la PRIMERA
ocurrencia de una marca repetida (acta 144, adjudicacion 4.3 del auditor) y cae
en ROJO POR AMBIGUA nombrando la marca y sus posiciones.

EL SUJETO ES UN REF DE GIT, CONGELADO, NUNCA EL ARBOL VIVO. Se lee con
`git show b7f07648:docs/loop/REPORTE.md`, que es el REPORTE.md de la vuelta 144
tal como quedo commiteado, el mismo sujeto que midio la TAREA 1.b. La
enfermedad del sujeto vivo (acta 144, 4.8 y 4.9) es justo lo que dejo la
bateria VIEJAS en rojo, y esta mutacion nace ya curada.

EL SUJETO SE ELIGE POR COMPUTO, NO POR GUSTO: de los candidatos de
`CANDIDATOS`, se toma el PRIMERO que cumple la condicion QUE EL CASO NECESITA
(que traiga la marca de COBERTURA REPETIDA), condicion que se evalua LEYENDO
el texto, no afirmandola. Si ninguno la cumple, ROJO PREVIO y no se inventa un
sujeto.

CUATRO COMPROBACIONES, las cuatro sobre variables que el codigo COMPUTA (nunca
un literal comparado consigo mismo, EJECUTOR.md regla 1):
  (i)   sobre el sujeto TAL CUAL, que HOY trae la marca de COBERTURA dos veces,
        la guarda sale ROJO POR AMBIGUA nombrando esa marca. Y se mide ADEMAS
        el contraste que hace que la mutacion valga: con el codigo de ayer
        (recorte anclado en la primera ocurrencia, reproducido aqui) el mismo
        sujeto sale en VERDE y en silencio.
  (ii)  quitado el SEGUNDO par de marcas de COBERTURA, VERDE, y la cifra de
        unidades fuera del vocabulario es LA MISMA que la de ayer sobre el
        sujeto entero: la regla nueva no cambia lo que se mide, solo cuando se
        niega a medir.
  (iii) duplicada la marca de CABECERA TALLADA sobre ese mismo sujeto ya
        saneado, ROJO por ambigua tambien: la regla es DE LAS TRES parejas y no
        solo de la nueva.
  (iv)  CONTRAPRUEBA: un reporte con UN SOLO par de cada una de las tres,
        VERDE. Sin ella, (i) y (iii) podrian estar saliendo rojo por cualquier
        otra causa.

USO:
  python scripts/loop/vuelta145_2a_mutacion_ancla_unica.py
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import verificar_cifras_del_reporte as C  # noqa: E402

# Candidatos, en orden de preferencia. El elegido es el PRIMERO que CUMPLE la
# condicion MEDIDA, no el primero de la lista.
CANDIDATOS = [
    "b7f07648:docs/loop/REPORTE.md",
    "c02b9fad:docs/loop/REPORTE.md",
]


def leer_ref(ref):
    r = subprocess.run(["git", "show", ref], cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8")


def elegir_sujeto():
    """POR COMPUTO: el primer candidato cuya marca de COBERTURA aparece MAS DE
    UNA VEZ, que es la condicion que el caso (i) necesita. Se devuelve tambien
    el censo medido de cada candidato, para que la eleccion sea auditable."""
    censo = []
    elegido = None
    for ref in CANDIDATOS:
        texto = leer_ref(ref)
        if texto is None:
            censo.append((ref, None, None))
            continue
        n_cob = texto.count(C.MARCA_COBERTURA_ABRE)
        n_cab = texto.count(C.MARCA_CABECERA_ABRE)
        censo.append((ref, n_cob, n_cab))
        if elegido is None and n_cob > 1:
            elegido = (ref, texto)
    return elegido, censo


def recorte_de_ayer(texto):
    """EL CODIGO DE AYER, reproducido aqui y SOLO aqui: anclar en la PRIMERA
    ocurrencia de cada marca con `find`, sin mirar si hay mas. Es el contraste
    que hace visible lo que la regla nueva repara; NO se llama desde la guarda."""
    for abre, cierra in ((C.MARCA_COBERTURA_ABRE, C.MARCA_COBERTURA_CIERRA),
                         (C.MARCA_COMMITS_ABRE, C.MARCA_COMMITS_CIERRA),
                         (C.MARCA_CABECERA_ABRE, C.MARCA_CABECERA_CIERRA)):
        a = texto.find(abre)
        b = texto.find(cierra)
        if a != -1 and b != -1 and b > a:
            texto = texto[:a] + texto[b + len(cierra):]
    return texto


def quitar_segundo_par(texto, abre, cierra):
    """Quita el SEGUNDO bloque delimitado por (abre, cierra), marcas incluidas.
    Devuelve None si no hay segundo bloque."""
    a2 = texto.find(abre, texto.find(abre) + 1)
    c2 = texto.find(cierra, texto.find(cierra) + 1)
    if a2 == -1 or c2 == -1 or c2 < a2:
        return None
    return texto[:a2] + texto[c2 + len(cierra):]


def corre_la_funcion(texto):
    """Devuelve (veredicto, detalle, unidades_fuera). El veredicto sale de que
    la funcion levante o no ValueError, nunca de un literal; unidades_fuera es
    None cuando cae en rojo."""
    try:
        cuerpo = C.quitar_bloques_cubiertos(texto)
    except ValueError as e:
        return "ROJO", str(e), None
    return "VERDE", "", len(C.unidades_vistas_fuera_del_vocabulario(cuerpo))


def main():
    elegido, censo = elegir_sujeto()
    print("MUTACIONES DE LA TAREA 2.a | vuelta 145 | EL ANCLA UNICA")
    print("Todo EN MEMORIA, cero escrituras. Sujeto CONGELADO por ref de git.")
    print("=" * 78)
    print("ELECCION DEL SUJETO POR COMPUTO (condicion: marca de COBERTURA repetida):")
    for ref, n_cob, n_cab in censo:
        if n_cob is None:
            print("  %-34s NO SE PUDO LEER" % ref)
        else:
            print("  %-34s COBERTURA abre x%d | CABECERA abre x%d %s"
                  % (ref, n_cob, n_cab,
                     "<- ELEGIDO" if elegido and ref == elegido[0] else ""))
    if elegido is None:
        print("")
        print("ROJO PREVIO: ningun candidato trae la marca de COBERTURA repetida; "
              "no hay sujeto que pruebe el caso (i) y no se inventa uno")
        return 1
    ref, base = elegido
    print("")

    resultados = []

    # ---- (i) EL SUJETO TAL CUAL: ROJO POR AMBIGUA -------------------------
    v_hoy, detalle_hoy, _ = corre_la_funcion(base)
    nombra = C.MARCA_COBERTURA_ABRE in detalle_hoy
    ok_i = (v_hoy == "ROJO") and nombra
    cuerpo_ayer = recorte_de_ayer(base)
    fuera_ayer = len(C.unidades_vistas_fuera_del_vocabulario(cuerpo_ayer))
    print("(i) EL SUJETO TAL CUAL (%s)" % ref)
    print("     CON EL CODIGO DE AYER (ancla en la primera ocurrencia): VERDE en silencio, "
          "%d unidad(es) fuera del vocabulario" % fuera_ayer)
    print("     CON LA REGLA NUEVA: %s" % v_hoy)
    print("     nombra la marca de COBERTURA: %s" % nombra)
    print("     %s" % detalle_hoy[:400])
    print("     VEREDICTO: %s" % ("OK" if ok_i else "ROJO"))
    resultados.append(("(i) marca de COBERTURA repetida -> ROJO POR AMBIGUA", ok_i))
    print("")

    # ---- (ii) QUITADO EL SEGUNDO PAR: VERDE Y MISMA CIFRA -----------------
    saneado = quitar_segundo_par(base, C.MARCA_COBERTURA_ABRE, C.MARCA_COBERTURA_CIERRA)
    if saneado is None:
        print("(ii) ROJO PREVIO: no se pudo quitar el segundo par")
        return 1
    v_ii, _detalle_ii, fuera_ii = corre_la_funcion(saneado)
    ok_ii = (v_ii == "VERDE") and (fuera_ii == fuera_ayer)
    print("(ii) QUITADO EL SEGUNDO PAR DE MARCAS DE COBERTURA: %s" % v_ii)
    print("     unidades fuera del vocabulario: %s (ayer, sobre el sujeto entero: %d)"
          % (fuera_ii, fuera_ayer))
    print("     la regla nueva NO cambia lo que se mide: %s" % (fuera_ii == fuera_ayer))
    print("     VEREDICTO: %s" % ("OK" if ok_ii else "ROJO"))
    resultados.append(("(ii) sin el 2.o par, VERDE y la MISMA cifra de ayer", ok_ii))
    print("")

    # ---- (iii) DUPLICADA LA MARCA DE CABECERA: ROJO TAMBIEN ---------------
    i_cab = saneado.find(C.MARCA_CABECERA_ABRE)
    if i_cab == -1:
        print("(iii) ROJO PREVIO: el sujeto saneado no trae la marca de CABECERA TALLADA")
        return 1
    con_cabecera_doble = saneado[:i_cab] + C.MARCA_CABECERA_ABRE + "\n" + saneado[i_cab:]
    v_iii, detalle_iii, _ = corre_la_funcion(con_cabecera_doble)
    nombra_cab = C.MARCA_CABECERA_ABRE in detalle_iii
    ok_iii = (v_iii == "ROJO") and nombra_cab
    print("(iii) DUPLICADA LA MARCA DE CABECERA TALLADA sobre el sujeto ya saneado: %s" % v_iii)
    print("     nombra la marca de CABECERA: %s" % nombra_cab)
    print("     %s" % detalle_iii[:400])
    print("     VEREDICTO: %s" % ("OK" if ok_iii else "ROJO"))
    resultados.append(("(iii) la regla es DE LAS TRES parejas, no solo de la nueva", ok_iii))
    print("")

    # ---- (iv) CONTRAPRUEBA: un solo par de cada una, VERDE ----------------
    uno_de_cada = ("cabecera\n%s\n| a | b |\n%s\ncuerpo con 3 nodos\n%s\n  x\n%s\n"
                   "final\n%s\nCOBERTURA: 0 cotejadas\n%s\n"
                   % (C.MARCA_CABECERA_ABRE, C.MARCA_CABECERA_CIERRA,
                      C.MARCA_COMMITS_ABRE, C.MARCA_COMMITS_CIERRA,
                      C.MARCA_COBERTURA_ABRE, C.MARCA_COBERTURA_CIERRA))
    v_iv, detalle_iv, fuera_iv = corre_la_funcion(uno_de_cada)
    ok_iv = v_iv == "VERDE"
    print("(iv) CONTRAPRUEBA, UN SOLO PAR DE CADA UNA DE LAS TRES: %s" % v_iv)
    print("     unidades fuera del vocabulario: %s" % fuera_iv)
    print("     %s" % detalle_iv[:300])
    print("     VEREDICTO: %s" % ("OK" if ok_iv else "ROJO"))
    resultados.append(("(iv) un solo par de cada una -> VERDE", ok_iv))
    print("")

    print("=" * 78)
    buenas = sum(1 for _, ok in resultados if ok)
    for nombre, ok in resultados:
        print("  %-58s %s" % (nombre, "OK" if ok else "ROJO"))
    print("")
    print("COMPROBACIONES QUE MUERDEN: %d de %d" % (buenas, len(resultados)))
    return 0 if buenas == len(resultados) else 1


if __name__ == "__main__":
    raise SystemExit(main())
