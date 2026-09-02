# -*- coding: utf-8 -*-
"""vuelta144_2d_mutacion_cobertura.py . LA MUTACION DE LA TAREA 2.d, vuelta 144.

QUE PRUEBA. Que la guarda de cifras YA NO SE MIDE A SI MISMA (acta 143,
adjudicacion 3.10 y caida 4.1 del ejecutor): pegar su propia linea de COBERTURA
dentro del reporte, ENTRE SUS DELIMITADORES, no mueve la cifra de unidades
vistas fuera del vocabulario. Y la contraprueba: pegarla SIN delimitadores si la
mueve, que es exactamente lo que le paso a la vuelta 143.

TODO EN MEMORIA Y CON CERO ESCRITURAS. Se llama a
`verificar_cifras_del_reporte.quitar_bloques_cubiertos` y al contador de
unidades del propio instrumento sobre COPIAS EN MEMORIA de un reporte, nunca
sobre un fichero del disco.

EL SUJETO SE ELIGE POR COMPUTO. La linea que se pega es LA QUE EL PROPIO
INSTRUMENTO PRODUCE sobre ese texto, no una tecleada, y las cifras que se
comparan salen las dos del contador, nunca de un literal (EJECUTOR.md regla 1).

--- EL SUJETO DEJA DE SER EL REPORTE VIVO (VUELTA 145, TAREA 2.b; acta 144,
caida 4.8 del auditor) ---

CORRECCION DECLARADA. EL TEXTO VIEJO DE ESTE PARRAFO DECIA, VERBATIM: "EL
SUJETO SE ELIGE POR COMPUTO: el `docs/loop/REPORTE.md` del arbol de trabajo."
No se borra, porque una correccion que tapa lo que corrige no se puede auditar
(EJECUTOR.md 8).

EL DEFECTO, MEDIDO. El sujeto era `docs/loop/REPORTE.md` VIVO, y este arnes le
AGREGA sus propios delimitadores. En cuanto el reporte de la vuelta trae ya un
par de marcas de COBERTURA, el par que el arnes agrega deja de ser el unico:
(B) mide sobre el bloque equivocado y (D) no puede levantar ValueError porque
las dos marcas ya estan. Medido en la vuelta 145 sobre el arbol limpio de la
apertura, con `verificar_mutaciones_viejas.py`: ANCLA PERDIDA 0, NO
REPRODUCIBLE 0 y NO MORDIO 1, que es este arnes, y suelto da 1 de 3. Estaba
verde cuando se corrio en la vuelta 144 y rojo en cuanto se escribio el reporte
de esa misma vuelta: EL VERDE NO SOBREVIVIA A LA PROPIA VUELTA.

EL ARREGLO. El sujeto pasa a ser un SUJETO CONGELADO Y COMMITEADO de
`docs/loop/`, elegido POR COMPUTO entre los `CANDIDATOS` con la condicion que
el caso NECESITA y que se evalua LEYENDO el texto: CERO ocurrencias de las dos
marcas de COBERTURA (para que el par que este arnes agrega sea el unico, que es
lo que (B) y (D) miden) y COMO MUCHO UNA de cada una de las otras cuatro (para
que la regla del ancla unica de la TAREA 2.a no dispare por otra cosa). Si
ningun candidato la cumple, ROJO PREVIO y no se inventa un sujeto.

POR QUE ESE CANDIDATO Y NO UNA COPIA NUEVA: `SUJETO_FIJO_V135_2E_REPORTE_134.md`
YA es el sujeto congelado de la casa (banco 9.10), ya esta commiteado en
`docs/loop/`, y las mutaciones de la vuelta 135 ya lo cotejan contra su blob en
cada corrida. Anadir una segunda copia congelada de un reporte seria una
segunda version de lo mismo, que es justo lo que la campana no quiere.

CUATRO COMPROBACIONES:
  (A) LINEA BASE. Se cuentan las unidades fuera del vocabulario del reporte tal
      cual. Es la cifra contra la que se mide todo lo demas.
  (B) LA MUTACION. Se pega la linea de cobertura DENTRO de los delimitadores y
      se vuelve a contar: LA CIFRA NO SE PUEDE MOVER.
  (C) LA CONTRAPRUEBA. Se pega la MISMA linea SIN delimitadores: la cifra TIENE
      que subir. Si no subiera, (B) no probaria nada, porque una linea que no
      aporta unidades no puede mover ninguna cuenta.
  (D) EL FALLO RUIDOSO. Con UNA SOLA de las dos marcas, la funcion tiene que
      levantar ValueError nombrando la que falta, igual que ya hace con la
      cabecera y con los commits. Nunca adivina donde acaba el bloque.
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import verificar_cifras_del_reporte as C  # noqa: E402

# CANDIDATOS A SUJETO CONGELADO, en orden de preferencia. El elegido es el
# PRIMERO que CUMPLE la condicion medida (ver `elegir_sujeto`), no el primero
# de la lista.
CANDIDATOS = [
    os.path.join(RAIZ, "docs", "loop", "SUJETO_FIJO_V135_2E_REPORTE_134.md"),
]

MARCAS_QUE_ESTORBAN = (C.MARCA_COBERTURA_ABRE, C.MARCA_COBERTURA_CIERRA)
MARCAS_QUE_SE_TOLERAN_UNA_VEZ = (
    C.MARCA_CABECERA_ABRE, C.MARCA_CABECERA_CIERRA,
    C.MARCA_COMMITS_ABRE, C.MARCA_COMMITS_CIERRA,
)


def elegir_sujeto():
    """POR COMPUTO (vuelta 145, TAREA 2.b): el primer candidato con CERO
    ocurrencias de las dos marcas de COBERTURA y COMO MUCHO UNA de cada una de
    las otras cuatro. Devuelve ((ruta, texto) o None, censo), donde `censo` es
    lo medido de cada candidato para que la eleccion sea auditable."""
    censo = []
    elegido = None
    for ruta in CANDIDATOS:
        if not os.path.exists(ruta):
            censo.append((ruta, None, None, "no existe"))
            continue
        texto = io.open(ruta, encoding="utf-8").read()
        n_cob = sum(texto.count(m) for m in MARCAS_QUE_ESTORBAN)
        max_otras = max([texto.count(m) for m in MARCAS_QUE_SE_TOLERAN_UNA_VEZ] or [0])
        cumple = (n_cob == 0) and (max_otras <= 1)
        censo.append((ruta, n_cob, max_otras, "CUMPLE" if cumple else "no cumple"))
        if elegido is None and cumple:
            elegido = (ruta, texto)
    return elegido, censo


def unidades_fuera(texto):
    """Las unidades que la guarda ve detras de un numero y FUERA de su
    vocabulario, contadas con el MISMO camino que el instrumento usa: primero
    se quitan los bloques delimitados, despues se recorre."""
    cuerpo = C.quitar_bloques_cubiertos(texto)
    return set(C.unidades_vistas_fuera_del_vocabulario(cuerpo))


def main():
    elegido, censo = elegir_sujeto()

    print("MUTACION DE LA TAREA 2.d | vuelta 144")
    print("Todo EN MEMORIA, cero escrituras. SUJETO CONGELADO Y COMMITEADO, "
          "elegido por computo (vuelta 145, TAREA 2.b).")
    print("=" * 78)
    print("ELECCION DEL SUJETO (condicion: 0 marcas de COBERTURA, <=1 de cada otra):")
    for ruta, n_cob, max_otras, veredicto in censo:
        print("  %-46s COBERTURA x%s | max otras x%s | %s"
              % (os.path.basename(ruta), n_cob, max_otras, veredicto))
    if elegido is None:
        print("")
        print("ROJO PREVIO: ningun candidato cumple la condicion; no hay sujeto que "
              "medir y no se inventa uno")
        return 1
    ruta, base = elegido
    print("  ELEGIDO: docs/loop/%s (%d caracteres)" % (os.path.basename(ruta), len(base)))
    print("=" * 78)

    resultados = []

    # ---- (A) LA LINEA BASE -------------------------------------------------
    fuera_base = unidades_fuera(base)
    print("(A) LINEA BASE: %d unidad(es) fuera del vocabulario" % len(fuera_base))
    print("     %s" % ", ".join(sorted(fuera_base)) or "(ninguna)")
    print("")

    # LA LINEA QUE SE PEGA: la produce el propio instrumento, no se teclea.
    # Se fabrica con el mismo formato que la guarda publica, y con palabras que
    # el vocabulario NO tiene, que es lo que hace que la contraprueba muerda.
    linea_cobertura = ("COBERTURA: %d cotejadas / 0 exentas / %d cifras | unidades vistas "
                       "FUERA del vocabulario: %d palabra(s) [%s]"
                       % (len(fuera_base), len(fuera_base), len(fuera_base),
                          ", ".join(sorted(fuera_base)) or "ninguna"))
    print("LA LINEA QUE SE PEGA (producida, no tecleada), %d caracteres:"
          % len(linea_cobertura))
    print("     %s" % linea_cobertura)
    print("")

    # ---- (B) LA MUTACION: pegada DENTRO de los delimitadores ---------------
    con_marcas = base + "\n\n%s\n```\n%s\n```\n%s\n" % (
        C.MARCA_COBERTURA_ABRE, linea_cobertura, C.MARCA_COBERTURA_CIERRA)
    fuera_b = unidades_fuera(con_marcas)
    ok_b = fuera_b == fuera_base
    print("(B) PEGADA DENTRO DE LOS DELIMITADORES: %d unidad(es)" % len(fuera_b))
    print("     la cifra se mueve: %s (entran %s, salen %s)"
          % (not ok_b, sorted(fuera_b - fuera_base) or "ninguna",
             sorted(fuera_base - fuera_b) or "ninguna"))
    print("     VEREDICTO: %s" % ("OK" if ok_b else "ROJO"))
    resultados.append(("(B) dentro de los delimitadores, la cifra NO se mueve", ok_b))
    print("")

    # ---- (C) LA CONTRAPRUEBA: pegada SIN delimitadores ---------------------
    sin_marcas = base + "\n\n```\n%s\n```\n" % linea_cobertura
    fuera_c = unidades_fuera(sin_marcas)
    ok_c = len(fuera_c) > len(fuera_base)
    print("(C) CONTRAPRUEBA, PEGADA SIN DELIMITADORES: %d unidad(es)" % len(fuera_c))
    print("     la cifra SUBE: %s (entran %s)"
          % (ok_c, sorted(fuera_c - fuera_base) or "ninguna"))
    print("     VEREDICTO: %s" % ("OK" if ok_c else "ROJO"))
    resultados.append(("(C) sin delimitadores, la cifra SI sube", ok_c))
    print("")

    # ---- (D) EL FALLO RUIDOSO CON UNA SOLA MARCA ---------------------------
    solo_abre = base + "\n\n%s\n%s\n" % (C.MARCA_COBERTURA_ABRE, linea_cobertura)
    solo_cierra = base + "\n\n%s\n%s\n" % (linea_cobertura, C.MARCA_COBERTURA_CIERRA)
    casos = []
    for etiqueta, texto, marca_que_falta in (
            ("solo la marca de APERTURA", solo_abre, C.MARCA_COBERTURA_CIERRA),
            ("solo la marca de CIERRE", solo_cierra, C.MARCA_COBERTURA_ABRE)):
        try:
            unidades_fuera(texto)
            casos.append((etiqueta, False, "no levanto ValueError"))
        except ValueError as e:
            nombra = marca_que_falta in str(e)
            casos.append((etiqueta, nombra, str(e)))
    ok_d = all(x[1] for x in casos)
    print("(D) FALLO RUIDOSO CON UNA SOLA MARCA:")
    for etiqueta, bien, detalle in casos:
        print("     %s -> %s" % (etiqueta, "OK" if bien else "ROJO"))
        print("        %s" % detalle)
    print("     VEREDICTO: %s" % ("OK" if ok_d else "ROJO"))
    resultados.append(("(D) una sola marca es ROJO y la nombra", ok_d))
    print("")

    print("=" * 78)
    buenas = sum(1 for _, ok in resultados if ok)
    for nombre, ok in resultados:
        print("  %-48s %s" % (nombre, "OK" if ok else "ROJO"))
    print("")
    print("COMPROBACIONES QUE MUERDEN: %d de %d" % (buenas, len(resultados)))
    return 0 if buenas == len(resultados) else 1


if __name__ == "__main__":
    raise SystemExit(main())
