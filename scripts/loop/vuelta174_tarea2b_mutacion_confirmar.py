# -*- coding: utf-8 -*-
r"""vuelta174_tarea2b_mutacion_confirmar.py . EL CASO POSITIVO POR MUTACION DE
LAS CUATRO FUNCIONES PURAS DE `vuelta172_tarea1b_confirmar_r41.py`.

POR QUE EXISTE. `EJECUTOR.md` 1, clausula del 29 ago 2026: **NINGUN assert,
GUARDA O CASO ROJO SE PUBLICA COMO PRUEBA SIN HABER CORRIDO ANTES SU PRUEBA DE
MUTACION**. El instrumento que nace en la TAREA 2.b existe justamente para que
una promesa deje de apuntar a un vacio; publicarlo con guardas que nadie ha
tumbado seria repetir la especie con otro traje.

SUJETO CONGELADO: todas las sedes de mentira son cadenas literales de este
proceso. **CERO LECTURAS DE DISCO Y CERO ESCRITURAS.** Las cuatro funciones que
se prueban (`acotar_r41`, `glosas_del_r41`, `estados_del_reporte`,
`bloque_de_confirmacion` y `anexar_al_r41`) reciben texto y devuelven texto, que
es lo que hace esto posible.

LA VARA: cada caso rojo dice que motivo espera, y se comprueba (a) que hay
motivo, (b) que el esperado sale NOMBRADO, y (c) que el texto devuelto es el
ORIGINAL sin tocar. El caso verde comprueba lo contrario, mas la adicion pura.

USO:
  python scripts/loop/vuelta174_tarea2b_mutacion_confirmar.py
"""
import os
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import vuelta172_tarea1b_confirmar_r41 as C  # noqa: E402

GLOSA_EJEC = ("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** "
              "VA A EJECUTARSE EN LA TAREA %s DE ESTA VUELTA, Y AL ESCRIBIR ESTA LINEA "
              "TODAVIA NO HA CORRIDO. Lo que sea.")
GLOSA_ACATA = ("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** "
               "SE ACATA SIN TOCAR NADA. Lo que sea.")
GLOSA_MUDA = ("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** "
              "Lo que sea, pero no dice ni tarea ni que se acate.")


def adj(clave, via, glosa):
    return ("  - **%s (`docs/loop/ACTA_AUDITOR.md:99999`, leida hoy). VIA PREVISTA: %s.** Titulo"
            % (clave, via) + NL +
            "    literal del acta: *\"lo que sea\"*" + NL + glosa)


def r41(cuerpo=None, cabecera="## R.41.", cola="", cabeza="texto de antes"):
    cuerpo = cuerpo if cuerpo is not None else (
        adj("6.1", "EJECUTADA", GLOSA_EJEC % "2.a") + NL +
        adj("6.2", "SIN TOCAR NADA", GLOSA_ACATA) + NL)
    return (cabeza + NL + NL +
            cabecera + " Registro de lo que sea" + NL + NL +
            cuerpo + NL +
            "## R.42. La siguiente" + NL + NL + "texto de despues" + NL + cola)


REPORTE = ("# REPORTE DE LA VUELTA 172" + NL +
           "| tarea | que encarga | estado | donde vive la prueba |" + NL +
           "|---|---|---|---|" + NL +
           "| **TAREA 1** | lo que sea | **CERRADA** | `X` |" + NL +
           "| **TAREA 2** | lo que sea | **CERRADA** | `X` |" + NL +
           "| **TAREA 4** | lo que sea | **ABIERTA, SIN CERRAR** | `X` |" + NL)


def correr():
    print("=" * 78)
    print("CASO POSITIVO POR MUTACION DE vuelta172_tarea1b_confirmar_r41.py")
    print("=" * 78)
    print("SUJETO CONGELADO: cero lecturas de disco, cero escrituras.")
    print("")
    verdes = 0
    rojos = 0

    def marcar(etiqueta, ok, detalle=""):
        nonlocal verdes, rojos
        print("   %-62s %s" % (etiqueta, "SI" if ok else "NO"))
        if detalle:
            print("      -> " + detalle[:100])
        if ok:
            verdes += 1
        else:
            rojos += 1

    print("-" * 78)
    print("(A) acotar_r41(): la cabecera aparece UNA vez o no hay acote")
    print("-" * 78)
    corte, m = C.acotar_r41(r41())
    marcar("acota cuando la cabecera aparece una vez", m is None and corte is not None)
    base = r41()
    marcar("y el acote PARA en la cabecera de la R.42, no se la come",
           m is None and "## R.42." not in base[corte[0]:corte[1]])
    _c, m = C.acotar_r41(r41(cabecera="## R.99."))
    marcar("cae si la cabecera del R.41 no esta", m is not None, m or "")
    _c, m = C.acotar_r41(r41(cola=NL + "## R.41. otra vez" + NL))
    marcar("cae si la cabecera del R.41 esta DOS veces", m is not None, m or "")
    print("")

    print("-" * 78)
    print("(B) glosas_del_r41() y estados_del_reporte(): se leen, no se teclean")
    print("-" * 78)
    corte, _m = C.acotar_r41(base)
    g = C.glosas_del_r41(base[corte[0]:corte[1]])
    marcar("lee las dos glosas del sujeto", len(g) == 2, str(g))
    marcar("de la primera extrae su tarea '2.a' del texto", g[0][2] == "2.a")
    marcar("de la segunda extrae None porque se acata", g[1][2] is None)
    otra = r41(cuerpo=adj("6.1", "EJECUTADA", GLOSA_EJEC % "4.b") + NL)
    c2, _m = C.acotar_r41(otra)
    g2 = C.glosas_del_r41(otra[c2[0]:c2[1]])
    marcar("con OTRA tarea escrita devuelve OTRA: no hay constante escondida",
           g2[0][2] == "4.b", str(g2[0]))
    e = C.estados_del_reporte(REPORTE)
    marcar("lee los tres estados de la tabla del reporte", len(e) == 3, str(e))
    marcar("y lee el de la TAREA 4 tal cual, sin suavizarlo",
           e["4"] == "**ABIERTA, SIN CERRAR**")
    marcar("de un reporte sin tabla no inventa ninguno",
           C.estados_del_reporte("# REPORTE DE LA VUELTA 172" + NL) == {})
    print("")

    print("-" * 78)
    print("(C) bloque_de_confirmacion(): los rojos")
    print("-" * 78)
    for etiqueta, glosas, estados, esperado in [
            ("sin ninguna glosa", [], e, "ninguna glosa"),
            ("sin ninguna fila de tabla", g, {}, "ninguna fila de la tabla"),
            ("con una glosa que no dice ni tarea ni que se acate",
             [("6.9", "EJECUTADA", "?", "x")], e, "no dicen ni su tarea")]:
        _b, motivos = C.bloque_de_confirmacion(glosas, estados, 100)
        ok = bool(motivos) and any(esperado in mm for mm in motivos)
        marcar("cae %s" % etiqueta, ok, motivos[0] if motivos else "(sin motivo)")
    print("")

    print("-" * 78)
    print("(D) anexar_al_r41(): los rojos, y el texto vuelve INTACTO")
    print("-" * 78)
    bloque, _m = C.bloque_de_confirmacion(g, e, 48851)
    casos = [
        ("si la confirmacion YA estaba anexada",
         r41(cola=NL + "**" + C.MARCA_BLOQUE + "** lo que sea" + NL), bloque,
         "YA ESTA anexada"),
        ("si el R.41 no se puede acotar", r41(cabecera="## R.99."), bloque,
         "aparece 0 veces"),
        ("si el bloque que se le pasa esta vacio", r41(), "   " + NL,
         "esta vacio"),
        ("si el bloque mete un guion largo",
         r41(), bloque + "lo que sea " + chr(8212) + NL, "guiones largos"),
        ("si el bloque mete un guion medio",
         r41(), bloque + "lo que sea " + chr(8211) + NL, "guiones medios"),
    ]
    for etiqueta, sede, blo, esperado in casos:
        nuevo, motivos = C.anexar_al_r41(sede, blo)
        ok = (bool(motivos) and any(esperado in mm for mm in motivos)
              and nuevo == sede)
        marcar("cae %s" % etiqueta, ok, motivos[0] if motivos else "(sin motivo)")
    print("")

    print("-" * 78)
    print("(E) LA GUARDA DE GUIONES MIRA EL DELTA Y NO EL TOTAL")
    print("-" * 78)
    print("   El motivo esta medido y es de la casa: la sede real es historica y")
    print("   YA trae guiones largos de 2026. Una guarda sobre el TOTAL se caeria")
    print("   por culpa de texto que nadie escribio hoy.")
    sede_sucia = r41(cabeza="texto viejo de 2026 con " + chr(8212) + " dentro")
    nuevo, motivos = C.anexar_al_r41(sede_sucia, bloque)
    marcar("PASA sobre una sede que ya traia un guion largo de antes",
           not motivos, motivos[0] if motivos else "")
    marcar("y el guion viejo sigue ahi, ni se borra ni se cuenta como nuevo",
           nuevo.count(chr(8212)) == 1)
    nuevo2, motivos2 = C.anexar_al_r41(sede_sucia, bloque + chr(8212) + NL)
    marcar("y CAE igualmente si el bloque anade UNO nuevo sobre esa misma sede",
           bool(motivos2) and nuevo2 == sede_sucia,
           motivos2[0] if motivos2 else "(sin motivo)")
    print("")

    print("-" * 78)
    print("(F) EL CASO VERDE, QUE PRUEBA QUE LOS ROJOS NO SON ROJOS SIEMPRE")
    print("-" * 78)
    base = r41()
    corte, _m = C.acotar_r41(base)
    nuevo, motivos = C.anexar_al_r41(base, bloque)
    comprobaciones = [
        ("no devuelve ningun motivo", not motivos),
        ("el texto crece: es adicion", len(nuevo) > len(base)),
        ("el texto de ANTES del R.41 no se toca",
         nuevo[:corte[0]] == base[:corte[0]]),
        ("el R.41 viejo sigue entero dentro del nuevo",
         base[corte[0]:corte[1]].rstrip(NL) in nuevo),
        ("el bloque queda DENTRO del R.41 y no detras del R.42",
         nuevo.index(C.MARCA_BLOQUE) < nuevo.index("## R.42.")),
        ("el R.42 de al lado sigue una sola vez", nuevo.count("## R.42.") == 1),
        ("la tabla del bloque trae una fila por glosa",
         nuevo.count("| `6.1` |") == 1 and nuevo.count("| `6.2` |") == 1),
        ("la fila de la 6.1 lleva el estado MEDIDO de su tarea",
         "| `6.1` | EJECUTADA | TAREA 2.a | **CERRADA** |" in nuevo),
        ("la de la 6.2, que se acata, no inventa ninguna tarea",
         "| `6.2` | SIN TOCAR NADA | (ninguna: se acata) | (no aplica) |" in nuevo),
        ("los bytes de la fuente viajan medidos dentro del bloque",
         "**48851 bytes**" in nuevo),
        ("cero guiones largos y medios nuevos",
         nuevo.count(chr(8212)) == base.count(chr(8212))
         and nuevo.count(chr(8211)) == base.count(chr(8211))),
    ]
    for etiqueta, ok in comprobaciones:
        marcar(etiqueta, ok)
    print("")

    print("-" * 78)
    print("(G) LA MUTACION DEL PROPIO ARNES")
    print("-" * 78)
    _n, motivos = C.anexar_al_r41(r41(cabecera="## R.99."), bloque)
    falso = any("un motivo que nadie devuelve jamas" in mm for mm in motivos)
    marcar("un motivo inventado NO aparece entre los devueltos", not falso)
    print("")

    total = verdes + rojos
    print("=" * 78)
    print("CIFRA casos: %d | verdes: %d | rojos: %d" % (total, verdes, rojos))
    print("=" * 78)
    if rojos:
        print("ROJO: %d comprobacion(es) no se comportan." % rojos)
        return 1
    print("VERDE: las %d comprobaciones se comportan, y cada guarda cae por su" % total)
    print("       propio motivo devolviendo el texto INTACTO.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(correr())
