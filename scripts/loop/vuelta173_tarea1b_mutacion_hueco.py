# -*- coding: utf-8 -*-
r"""vuelta173_tarea1b_mutacion_hueco.py . CASO POSITIVO POR MUTACION DEL HUECO
DECLARADO Y MEDIDO de `cerrar_reporte.py` (TAREA 1.b de la vuelta 173), CON
NOMBRE DE ARNES.

POR QUE EXISTE ESTE FICHERO Y NO UN FLAG: la bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS.
Una prueba que vive detras de un `--mutar` de otro fichero no la corre nadie
desde la bateria.

POR QUE ES UN ARNES NUEVO Y NO CASOS ANADIDOS AL DE LA 172: lo manda la
adjudicacion 6.2 del acta del auditor de la vuelta 172, literal, *"los 17 casos
del arnes de la 172 se quedan como estan y tienen que seguir verdes. La conducta
nueva se prueba con casos nuevos en un arnes nuevo"*. Los 17 siguen verdes y
esta vuelta lo midio antes de escribir esto
(`docs/loop/SALIDA_V173_T1B_LOS_17_DESPUES.txt`).

QUE PRUEBA, Y ES EXACTAMENTE LO QUE EL ENCARGO PIDE QUE CAIGA:

  . que un HUECO SIN MEDICION pase,
  . que un HUECO SIN ATRIBUCION pase,
  . que UNA CORRIDA DE OTRA VUELTA pase, y se prueba por los DOS caminos por
    los que podria colarse: nombrada dentro del hueco, y pegada como bateria.

Y prueba ademas los dos extremos que dan sentido a lo anterior: que un hueco
COMPLETO si cierra, y que una AUSENCIA MUDA no.

SUJETO CONGELADO (condicion de la vuelta 148): TODOS los sujetos son cadenas
fabricadas en memoria. Ni se lee el repo, ni se escribe un solo byte. La unica
lectura del arbol vivo es `import cerrar_reporte`, que es el sujeto de la prueba.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: los esperados se comparan contra lo
que devuelven `hueco_declarado_que_falta()` y `piezas_que_faltan()`, y la pasada
2 muta cada esperado y exige que el caso CAIGA.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import cerrar_reporte as CR   # noqa: E402

NL = chr(10)
V = 172

FILAS = ["| cosa | de antes | de ahora |",
         "|---|---:|---:|",
         "| censo de mentira | 1 / 2 / 3 | **1 / 2 / 3** |",
         "| motor de mentira | 9/9 | **9/9** |"]

BATERIA = ["LAS 82 MUTACIONES DE MENTIRA.",
           "  ANCLA PERDIDA  : 0 (ninguna)",
           "  NO MORDIO      : 0 (ninguna)",
           "VERDE de mentira.",
           "FIN"]

ATRIB = "NADIE la corrio: ni el ejecutor ni el auditor, de mentira."


def hueco(nombre=True, bytes_medidos=True, atribucion=True,
          marca=True, vuelta_ajena=None, atribucion_vacia=False):
    """UNA SECCION 9 DE MENTIRA, con las piezas del hueco que se le pidan.

    `vuelta_ajena` pone el fichero de OTRA vuelta en vez del de la suya, que es
    la forma en que una corrida ajena se colaria dentro del hueco."""
    n = vuelta_ajena if vuelta_ajena is not None else V
    L = [CR.CAB_9_HUECO if marca else "## 9. LA BATERIA DE MUTACIONES", ""]
    if marca:
        L.append("**%s. LA BATERIA DE LA VUELTA %d NO CORRIO.**" % (CR.MARCA_HUECO, V))
    else:
        L.append("aqui iba la bateria y no esta.")
    L.append("")
    if nombre:
        L.append("**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V%d_BATERIA.txt`." % n)
    if bytes_medidos:
        L.append("**SUS BYTES, MEDIDOS EN ESTA CORRIDA:** **0 bytes**.")
    if atribucion:
        L.append("%s %s" % (CR.MARCA_ATRIBUCION, "" if atribucion_vacia else ATRIB))
    L.append("")
    return NL.join(L)


def reporte(seccion9):
    """UN REPORTE CERRADO DE MENTIRA con la seccion 9 que se le pase. Las otras
    tres piezas van SIEMPRE puestas, para que lo unico que se mida aqui sea la
    (4) y ninguna otra falta enturbie la lectura."""
    L = ["# REPORTE DE LA VUELTA 172 (de mentira). Rama `de-mentira`.", "",
         "**EL VEREDICTO DE UNA LINEA: LA VUELTA DE MENTIRA HIZO LO SUYO.**", "",
         "## 0. LA IDENTIDAD", "", CR.MARCA_ABRE]
    L.extend(FILAS)
    L.append(CR.MARCA_CIERRA)
    L.append("")
    for k in range(1, 9):
        L.append("## %d. SECCION %d DE MENTIRA" % (k, k))
        L.append("")
        L.append("cuerpo de la seccion %d" % k)
        L.append("")
    L.append(seccion9)
    return NL.join(L)


def seccion9_con_bateria():
    """La seccion 9 con la bateria pegada dentro, que es el camino de siempre."""
    L = [CR.CAB_9, "", "Fichero: `docs/loop/SALIDA_V172_BATERIA.txt`.", "", "```"]
    L.extend(BATERIA)
    L.append("```")
    L.append("")
    return NL.join(L)


def codigos(faltan):
    """Los numeros de pieza que la guarda nombra, leidos de su lista."""
    return sorted(set(f[:3] for f in faltan))


def main():
    print("=" * 78)
    print("VUELTA 173, TAREA 1.b: CASO POSITIVO POR MUTACION DEL HUECO DECLARADO")
    print("Y MEDIDO de cerrar_reporte.py")
    print("=" * 78)
    print("")
    casos = []

    print("A) EL HUECO COMPLETO SI CIERRA (si esto no pasara, la 1.b no serviria)")
    completo = hueco()
    motivos = CR.hueco_declarado_que_falta(completo, V)
    print("   hueco completo -> le faltan %d motivo(s): %s" % (len(motivos), motivos))
    casos.append(("A_al_hueco_completo_no_le_falta_nada", len(motivos), 0))
    f = CR.piezas_que_faltan(reporte(completo), FILAS, [], vuelta=V,
                             nombre_bateria="docs/loop/SALIDA_V172_BATERIA.txt")
    print("   reporte con hueco completo y bateria vacia -> faltan %d, codigos %s"
          % (len(f), codigos(f)))
    casos.append(("A_el_reporte_con_hueco_completo_no_falla", len(f), 0))
    casos.append(("A_y_no_nombra_la_pieza_4", "(4)" in codigos(f), False))
    print("")

    print("B) LOS TRES QUE EL ENCARGO EXIGE QUE CAIGAN")
    escenarios = [
        ("un hueco SIN MEDICION", hueco(bytes_medidos=False), "bytes medidos"),
        ("un hueco SIN ATRIBUCION", hueco(atribucion=False), "atribucion"),
        ("un hueco con la ATRIBUCION VACIA", hueco(atribucion_vacia=True), "atribucion"),
        ("una CORRIDA DE OTRA VUELTA", hueco(vuelta_ajena=171), "OTRA VUELTA"),
    ]
    for etiqueta, s9, aguja in escenarios:
        motivos = CR.hueco_declarado_que_falta(s9, V)
        f = CR.piezas_que_faltan(reporte(s9), FILAS, [], vuelta=V,
                                 nombre_bateria="docs/loop/SALIDA_V172_BATERIA.txt")
        print("   %-36s motivos %d, codigos %s" % (etiqueta, len(motivos), codigos(f)))
        print("      %s" % (motivos[0] if motivos else "(ninguno)"))
        clave = etiqueta.replace(" ", "_")
        casos.append(("B_%s_da_al_menos_un_motivo" % clave, len(motivos) >= 1, True))
        casos.append(("B_%s_nombra_su_causa" % clave,
                      any(aguja in m for m in motivos), True))
        casos.append(("B_%s_hace_fallar_la_pieza_4" % clave, "(4)" in codigos(f), True))
    print("")

    print("C) LA AUSENCIA MUDA NO ES UN HUECO DECLARADO")
    mudo = hueco(marca=False, nombre=False, bytes_medidos=False, atribucion=False)
    motivos = CR.hueco_declarado_que_falta(mudo, V)
    f = CR.piezas_que_faltan(reporte(mudo), FILAS, [], vuelta=V,
                             nombre_bateria="docs/loop/SALIDA_V172_BATERIA.txt")
    print("   seccion 9 muda -> motivos %d, codigos %s" % (len(motivos), codigos(f)))
    casos.append(("C_la_ausencia_muda_da_motivo", len(motivos) >= 1, True))
    casos.append(("C_y_la_nombra_como_muda",
                  any("MUDA" in m for m in motivos), True))
    casos.append(("C_y_hace_fallar_la_pieza_4", "(4)" in codigos(f), True))
    print("")

    print("D) UNA CORRIDA DE OTRA VUELTA PEGADA COMO BATERIA TAMPOCO PASA")
    con_bat = reporte(seccion9_con_bateria())
    f_suya = CR.piezas_que_faltan(con_bat, FILAS, BATERIA, vuelta=V,
                                  nombre_bateria="docs/loop/SALIDA_V172_BATERIA.txt")
    print("   la bateria de SU vuelta   -> faltan %d, codigos %s"
          % (len(f_suya), codigos(f_suya)))
    casos.append(("D_la_bateria_de_su_vuelta_cierra", len(f_suya), 0))
    f_ajena = CR.piezas_que_faltan(con_bat, FILAS, BATERIA, vuelta=V,
                                   nombre_bateria="docs/loop/SALIDA_V171_BATERIA.txt")
    print("   la bateria de la 171      -> faltan %d, codigos %s"
          % (len(f_ajena), codigos(f_ajena)))
    casos.append(("D_una_bateria_ajena_hace_fallar_la_4", "(4)" in codigos(f_ajena), True))
    casos.append(("D_y_dice_de_que_vuelta_es",
                  any("vuelta 171" in x for x in f_ajena), True))
    print("")

    print("E) SIN SABER DE QUE VUELTA ES EL REPORTE, UN HUECO NO SE PUEDE JUZGAR")
    motivos = CR.hueco_declarado_que_falta(completo, None)
    f = CR.piezas_que_faltan(reporte(completo), FILAS, [])
    print("   vuelta=None -> motivos %d, codigos %s" % (len(motivos), codigos(f)))
    casos.append(("E_sin_vuelta_el_hueco_no_se_juzga", len(motivos), 1))
    casos.append(("E_y_la_pieza_4_falla", "(4)" in codigos(f), True))
    print("")

    print("F) LOS 17 CASOS VIEJOS LLAMAN CON TRES ARGUMENTOS Y NO SE ROMPEN")
    f = CR.piezas_que_faltan(con_bat, FILAS, BATERIA)
    print("   piezas_que_faltan(texto, filas, bateria) -> faltan %d, codigos %s"
          % (len(f), codigos(f)))
    casos.append(("F_la_llamada_de_tres_argumentos_sigue_cerrando", len(f), 0))
    print("")

    print("G) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-56s %s" % (nombre, "PASA" if ok else "FALLA (real=%r esperado=%r)"
                               % (real, esperado)))
        if not ok:
            fallos += 1
    print("   CIFRA casos que pasan: %d de %d" % (len(casos) - fallos, len(casos)))
    print("")

    print("H) PASADA 2, SE MUTA EL ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        else:
            mutado = list(esperado) + ["(9)"]
        cayo = (real != mutado)
        print("   %-56s %s (esperado mutado=%r)"
              % (nombre, "CAE " if cayo else "NO CAE", mutado))
        if cayo:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    if fallos or caen != len(casos):
        print("ROJO: %d caso(s) fallan tal cual y %d de %d caen al mutar."
              % (fallos, caen, len(casos)))
        return 1
    print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
          % (len(casos), len(casos)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
