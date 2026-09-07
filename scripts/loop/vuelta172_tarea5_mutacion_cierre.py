# -*- coding: utf-8 -*-
r"""vuelta172_tarea5_mutacion_cierre.py . CASO POSITIVO POR MUTACION DE LAS
CUATRO PIEZAS DE `cerrar_reporte.py` (TAREA 5 de la vuelta 172), CON NOMBRE DE
ARNES.

POR QUE EXISTE ESTE FICHERO Y NO UN FLAG: la bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS.

QUE PRUEBA, Y ES EXACTAMENTE LO QUE EL ENCARGO PIDE: que
`cerrar_reporte.piezas_que_faltan()` **CAE si el instrumento diera verde con
cualquiera de las cuatro piezas ausente**. Se fabrica un reporte cerrado DE
MENTIRA, se comprueba que con las cuatro puestas no falta ninguna, y despues se
le quita **una a una** y se exige que la que falta salga NOMBRADA por su numero.

Y ADEMAS, PORQUE UNA GUARDA QUE SOLO MIRA LA PRESENCIA DE UN ROTULO NO ES UNA
GUARDA: se prueba que la (2) no se conforma con que el hueco haya desaparecido
(hay un caso con el hueco quitado y las filas NO pegadas), y que la (4) no se
conforma con que exista la seccion 9 (hay un caso con la seccion 9 vacia y otro
con la bateria a medias).

SUJETO CONGELADO (condicion de la vuelta 148): todos los reportes de mentira son
CADENAS literales de este proceso. NO se lee el disco, NO se escribe nada, y el
resultado no depende de que haya en `docs/loop/` hoy ni dentro de diez vueltas.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: los reales salen de llamar a
`piezas_que_faltan`, y la pasada 2 muta cada esperado y exige que el caso CAIGA.

--- REPARADO EN LA VUELTA 195, Y LA CAUSA VA ESCRITA (TAREA 3.d) ---

ESTE ARNES LLEVABA SIN MORDER DESDE LA VUELTA 188, Y LAS BATERIAS DE LA 189 Y LA
194 LO PUBLICABAN COMO `NO MORDIO` SIN DIAGNOSTICARLO. La causa, medida en la
vuelta 195 corriendolo: **su propio caso verde fabricaba DOS secciones `## 9.`**,
la del bucle y la de `CR.CAB_9`. Eso era inofensivo hasta que la TAREA 4.b de la
vuelta 188 ensancho la pieza (3) de `cerrar_reporte.py` para cazar SECCIONES
DUPLICADAS; desde entonces `A_con_las_cuatro_no_falta_ninguna` daba 1 en vez de 0
y `A_y_no_nombra_ningun_codigo` devolvia `['(3)']` en vez de `[]`.

**NO ES QUE LA GUARDA ESTUVIERA MAL: ES QUE EL SUJETO DE MENTIRA DE ESTE ARNES
DEJO DE SER UN REPORTE VALIDO Y NADIE LO RE APUNTO.** Una guarda que no muerde no
es una guarda, y un arnes cuyo caso verde falla no puede probar nada de lo demas.
El arreglo esta en `reporte()` y va comentado en su sitio. **NO SE AFLOJA NINGUN
CASO:** la rama `secciones=False` sigue fabricando un reporte SIN la seccion 9 y
la pieza (3) sigue teniendo que cazarla.

USO:  python scripts/loop/vuelta172_tarea5_mutacion_cierre.py
"""
import os
import sys

NL = chr(10)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

FILAS = ["| | **apertura** | **cierre** |",
         "|---|---:|---:|",
         "| censo de mentira | 1 / 2 / 3 | **1 / 2 / 3** |",
         "| motor de mentira | 9/9 | **9/9** |"]

BATERIA = ["LAS 78 MUTACIONES DE MENTIRA.",
           "  ANCLA PERDIDA  : 0 (ninguna)",
           "  NO MORDIO      : 0 (ninguna)",
           "VERDE de mentira.",
           "FIN"]


def reporte(veredicto=True, cabecera=True, secciones=True, bateria=True,
            hueco_quitado_sin_pegar=False, bateria_a_medias=False):
    """UN REPORTE CERRADO DE MENTIRA, en memoria, con las piezas que se le
    pidan. `hueco_quitado_sin_pegar` fabrica el caso tramposo: el rotulo
    PENDIENTE ya no esta pero las filas tampoco."""
    L = ["# REPORTE DE LA VUELTA 999 (de mentira). Rama `de-mentira`.", ""]
    if veredicto:
        L.append("**EL VEREDICTO DE UNA LINEA: LA VUELTA DE MENTIRA HIZO LO SUYO.**")
    else:
        L.append(CR.VEREDICTO_VIEJO)
    L.append("")
    L.append("## 0. LA IDENTIDAD")
    L.append("")
    L.append(CR.MARCA_ABRE)
    if cabecera:
        L.extend(FILAS)
    elif hueco_quitado_sin_pegar:
        L.append("aqui iba la tabla y no esta, pero el rotulo del hueco tampoco.")
    else:
        L.append("**" + CR.HUECO_CABECERA + ", Y SE DICE EN VEZ DE RELLENARLA.**")
    L.append(CR.MARCA_CIERRA)
    L.append("")
    # LA REPARACION DE LA VUELTA 195, DECLARADA Y CON SU CAUSA MEDIDA. Aqui
    # decia `tope = 10 if secciones else 9`, o sea que con `secciones=True`
    # fabricaba `## 1.` a `## 9.` **y ADEMAS** `CAB_9`, que tambien es `## 9.`:
    # DOS secciones nueve en el mismo reporte de mentira. Eso era inofensivo
    # hasta la vuelta 188, cuando la TAREA 4.b ensancho la pieza (3) de
    # `cerrar_reporte.py` para cazar SECCIONES DUPLICADAS, y desde entonces EL
    # PROPIO CASO VERDE DE ESTE ARNES caia: `A_con_las_cuatro_no_falta_ninguna`
    # daba 1 en vez de 0, nombrando el codigo `(3)`. Un arnes cuyo caso verde
    # falla NO MUERDE, y asi lo publicaban las baterias de la 189 y la 194.
    #
    # EL TOPE PASA A 9 EN LAS DOS RAMAS, y las dos siguen midiendo lo suyo:
    #   . con `secciones=True`  -> `## 1.` a `## 8.` mas `CAB_9` = 1 a 9 UNICAS.
    #   . con `secciones=False` -> `## 1.` a `## 8.` y sin `CAB_9`, o sea sin
    #     la 9, que es lo que la pieza (3) tiene que cazar. NO SE AFLOJA NADA.
    tope = 9
    for k in range(1, tope):
        L.append("## %d. SECCION %d DE MENTIRA" % (k, k))
        L.append("")
        L.append("cuerpo de la seccion %d" % k)
        L.append("")
    if secciones:
        L.append(CR.CAB_9)
        L.append("")
        if bateria:
            L.append("```")
            L.extend(BATERIA if not bateria_a_medias else BATERIA[:2])
            L.append("```")
        else:
            L.append("aqui iba la bateria y no esta.")
        L.append("")
    return NL.join(L)


def codigos(faltan):
    """Los numeros de pieza que la guarda nombra, leidos de su lista."""
    return sorted(set(f[:3] for f in faltan))


def main():
    print("=" * 78)
    print("VUELTA 172, TAREA 5: CASO POSITIVO POR MUTACION DE LAS CUATRO PIEZAS DE")
    print("cerrar_reporte.py")
    print("=" * 78)
    print("")
    casos = []

    print("A) EL CASO VERDE: LAS CUATRO PUESTAS Y NO FALTA NINGUNA")
    entero = reporte()
    f = CR.piezas_que_faltan(entero, FILAS, BATERIA)
    print("   reporte de mentira: %d bytes -> faltan %d %s"
          % (len(entero.encode("utf-8")), len(f), codigos(f)))
    casos.append(("A_con_las_cuatro_no_falta_ninguna", len(f), 0))
    casos.append(("A_y_no_nombra_ningun_codigo", codigos(f), []))
    print("")

    print("B) SE QUITA UNA A UNA Y LA QUE FALTA TIENE QUE SALIR NOMBRADA")
    escenarios = [
        ("sin veredicto", reporte(veredicto=False), "(1)"),
        ("sin cabecera pegada", reporte(cabecera=False), "(2)"),
        ("sin secciones 3 a 9", reporte(secciones=False), "(3)"),
        ("sin la bateria dentro de la 9", reporte(bateria=False), "(4)"),
    ]
    for etiqueta, texto, codigo in escenarios:
        f = CR.piezas_que_faltan(texto, FILAS, BATERIA)
        print("   %-32s faltan %d, codigos %s" % (etiqueta, len(f), codigos(f)))
        casos.append(("B_%s_da_al_menos_una" % etiqueta.replace(" ", "_"),
                      len(f) >= 1, True))
        casos.append(("B_%s_nombra_la_pieza" % etiqueta.replace(" ", "_"),
                      codigo in codigos(f), True))
    print("")

    print("C) LOS DOS CASOS TRAMPOSOS: NO BASTA CON QUE EL ROTULO DESAPAREZCA")
    tramposo = reporte(cabecera=False, hueco_quitado_sin_pegar=True)
    f = CR.piezas_que_faltan(tramposo, FILAS, BATERIA)
    print("   hueco quitado pero filas NO pegadas -> faltan %d, codigos %s"
          % (len(f), codigos(f)))
    casos.append(("C_el_hueco_quitado_sin_pegar_sigue_siendo_falta", "(2)" in codigos(f), True))
    a_medias = reporte(bateria_a_medias=True)
    f = CR.piezas_que_faltan(a_medias, FILAS, BATERIA)
    print("   bateria a medias dentro de la 9  -> faltan %d, codigos %s"
          % (len(f), codigos(f)))
    casos.append(("C_una_bateria_recortada_sigue_siendo_falta", "(4)" in codigos(f), True))
    f = CR.piezas_que_faltan(entero, FILAS, [])
    print("   bateria de cero lineas            -> faltan %d, codigos %s"
          % (len(f), codigos(f)))
    casos.append(("C_una_bateria_vacia_es_falta", "(4)" in codigos(f), True))
    f = CR.piezas_que_faltan(entero, [], BATERIA)
    print("   tallador sin filas                -> faltan %d, codigos %s"
          % (len(f), codigos(f)))
    casos.append(("C_un_tallador_sin_filas_es_falta", "(2)" in codigos(f), True))
    print("")

    print("D) SIN NINGUNA DE LAS CUATRO, LAS CUATRO TIENEN QUE SALIR")
    nada = reporte(veredicto=False, cabecera=False, secciones=False, bateria=False)
    f = CR.piezas_que_faltan(nada, FILAS, BATERIA)
    print("   reporte sin cerrar del todo -> faltan %d, codigos %s" % (len(f), codigos(f)))
    casos.append(("D_sin_nada_faltan_las_cuatro", len(codigos(f)), 4))
    casos.append(("D_y_estan_las_cuatro_nombradas", codigos(f),
                  ["(1)", "(2)", "(3)", "(4)"]))
    print("")

    print("E) EL ESQUELETO RECIEN TALLADO, QUE ES EL CASO REAL DEL PRINCIPIO")
    esqueleto = NL.join([
        "# REPORTE DE LA VUELTA 999 (de mentira). Rama `de-mentira`.", "",
        CR.VEREDICTO_VIEJO, "", "## 0. LA IDENTIDAD", "",
        CR.MARCA_ABRE,
        "**" + CR.HUECO_CABECERA + ", Y SE DICE EN VEZ DE RELLENARLA.**",
        CR.MARCA_CIERRA, "", "## 1. LAS TAREAS", "", "## 2. UNA POR UNA", ""])
    f = CR.piezas_que_faltan(esqueleto, FILAS, BATERIA)
    print("   esqueleto sin cerrar -> faltan %d, codigos %s" % (len(f), codigos(f)))
    casos.append(("E_un_esqueleto_recien_tallado_falla_las_cuatro", len(codigos(f)), 4))
    print("   (esto es lo que las vueltas 170 y 171 dejaron commiteado: si este")
    print("    instrumento hubiera existido, habria salido ROJO en vez de callar)")
    print("")

    print("F) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-56s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("G) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, list):
            mutado = esperado + ["(9)"]
        else:
            mutado = str(esperado) + "_mutado"
        cae = (real != mutado)
        print("   %-56s %s   (esperado mutado=%r)"
              % (nombre, "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
