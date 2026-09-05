# -*- coding: utf-8 -*-
r"""vuelta172_tarea2a_mutacion_exclusion.py . CASO POSITIVO POR MUTACION DE LA
EXCLUSION DEL ARCHIVO DE REPORTES (TAREA 2.a de la vuelta 172), CON NOMBRE DE
ARNES.

POR QUE EXISTE ESTE FICHERO Y NO UN FLAG: la bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS.

QUE PRUEBA. La adjudicacion 6.1 del acta 171 manda que
`docs/loop/reportes/REPORTE_V<N>.md` entre en los narrativos del bucle de
`vuelta48_contar_ld.py`, **POR PATRON de la carpeta de archivo y no por el
nombre de una vuelta**, y con un caso positivo que **tiene que CAER si alguien
la estrecha o si el archivo vuelve a contar**. Eso es literalmente lo que se
prueba aqui, y en tres frentes:

  A. QUE EL ARCHIVO NO CUENTA. Cualquier `REPORTE_V<N>.md` de la carpeta de
     archivo sale con motivo NARRATIVO, para numeros de vuelta que hoy no
     existen (`REPORTE_V9999.md`) y para los que si.
  B. QUE LA REGLA NO SE ENSANCHA. Un fichero cualquiera dentro de la misma
     carpeta que NO sea un reporte archivado (`notas.md`, `REPORTE_VX.md`,
     `REPORTE_V12.txt`) SIGUE CONTANDO. Una exclusion que se come la carpeta
     entera seria un agujero, no una guarda.
  C. QUE ESTRECHARLA LA TUMBA. Se fabrica la version ESTRECHA de la regla (la
     que nombra una vuelta concreta, `REPORTE_V171.md`) y se comprueba que
     **deja de ver** los demas. Ese es el caso que el encargo pide con esas
     palabras.

Y ADEMAS, PARA QUE ESTO NO SE VUELVA UN CENSO CIEGO: se comprueba que las TRES
exclusiones viejas (`SALIDA_*`, los tres narrativos y los registros del arnes)
siguen mordiendo, y que un fichero normal del plan NO se excluye.

SUJETO CONGELADO (condicion de la vuelta 148): todos los sujetos son CADENAS
literales de este proceso. NO se lee el disco, NO se escribe nada, y el
resultado no depende de que ficheros existan hoy.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: los reales salen de llamar a
`motivo_de_exclusion` y a los patrones, y la pasada 2 muta cada esperado y exige
que el caso CAIGA.

USO:  python scripts/loop/vuelta172_tarea2a_mutacion_exclusion.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta48_contar_ld as C   # noqa: E402

# LA VERSION ESTRECHA DE LA REGLA, FABRICADA AQUI PARA PODER TUMBARLA. Es la que
# alguien escribiria si nombrara una vuelta en vez de la carpeta.
RE_ESTRECHA = re.compile(r"^docs/loop/reportes/REPORTE_V171\.md$")


def motivo_con_patron(rel, patron):
    """La MISMA decision que `motivo_de_exclusion`, pero con el patron del
    archivo por parametro, para poder correrla con la version estrecha sin
    tocar el instrumento."""
    nombre = rel.rsplit("/", 1)[-1]
    if nombre.startswith("SALIDA_"):
        return "SALIDA"
    if rel in C.NARRATIVOS_DEL_BUCLE:
        return "NARRATIVO"
    if patron.match(rel):
        return "NARRATIVO"
    if C.RE_ARNES.match(rel):
        return "ARNES"
    return None


def main():
    print("=" * 78)
    print("VUELTA 172, TAREA 2.a: CASO POSITIVO POR MUTACION DE LA EXCLUSION DEL")
    print("ARCHIVO DE REPORTES EN vuelta48_contar_ld.py")
    print("=" * 78)
    print("")
    casos = []

    print("A) EL ARCHIVO DE REPORTES NO CUENTA, Y NO POR SU NUMERO DE VUELTA")
    for rel in ("docs/loop/reportes/REPORTE_V168.md",
                "docs/loop/reportes/REPORTE_V170.md",
                "docs/loop/reportes/REPORTE_V171.md",
                "docs/loop/reportes/REPORTE_V172.md",
                "docs/loop/reportes/REPORTE_V9999.md",
                "docs/loop/reportes/REPORTE_V1.md"):
        m = C.motivo_de_exclusion(rel)
        print("   %-44s -> %s" % (rel, m))
        casos.append(("A_%s_es_NARRATIVO" % rel.rsplit("/", 1)[-1], m, "NARRATIVO"))
    print("")

    print("B) LA REGLA NO SE ENSANCHA: LO QUE NO ES UN REPORTE ARCHIVADO SI CUENTA")
    for rel, esperado in (("docs/loop/reportes/notas.md", None),
                          ("docs/loop/reportes/REPORTE_VX.md", None),
                          ("docs/loop/reportes/REPORTE_V12.txt", None),
                          ("docs/loop/reportes/REPORTE_V12.md.bak", None),
                          ("docs/loop/reportes/sub/REPORTE_V12.md", None),
                          ("docs/loop/REPORTE_V12.md", None)):
        m = C.motivo_de_exclusion(rel)
        print("   %-44s -> %s" % (rel, m))
        casos.append(("B_%s_sigue_contando" % rel.replace("/", "_"), m, esperado))
    print("")

    print("C) SI SE ESTRECHA LA REGLA, EL CASO CAE. ES LO QUE EL ENCARGO PIDE.")
    anchos = ["docs/loop/reportes/REPORTE_V168.md",
              "docs/loop/reportes/REPORTE_V170.md",
              "docs/loop/reportes/REPORTE_V172.md",
              "docs/loop/reportes/REPORTE_V9999.md"]
    con_ancha = [r for r in anchos
                 if motivo_con_patron(r, C.RE_ARCHIVO_DEL_REPORTE) == "NARRATIVO"]
    con_estrecha = [r for r in anchos
                    if motivo_con_patron(r, RE_ESTRECHA) == "NARRATIVO"]
    print("   con la regla POR PATRON:   %d de %d excluidos" % (len(con_ancha), len(anchos)))
    print("   con la regla ESTRECHA:     %d de %d excluidos" % (len(con_estrecha), len(anchos)))
    casos.append(("C_la_regla_por_patron_los_ve_todos", len(con_ancha), 4))
    casos.append(("C_la_estrecha_no_ve_ninguno_de_esos", len(con_estrecha), 0))
    casos.append(("C_pero_la_estrecha_si_ve_el_suyo",
                  motivo_con_patron("docs/loop/reportes/REPORTE_V171.md", RE_ESTRECHA),
                  "NARRATIVO"))
    print("")

    print("D) SI EL ARCHIVO VUELVE A CONTAR, EL CASO CAE")
    nunca = re.compile(r"^ESTO NO CASA CON NADA$")
    vuelve = [r for r in anchos if motivo_con_patron(r, nunca) == "NARRATIVO"]
    print("   con el patron desactivado: %d de %d excluidos" % (len(vuelve), len(anchos)))
    casos.append(("D_sin_patron_el_archivo_vuelve_a_contar", len(vuelve), 0))
    casos.append(("D_y_con_patron_no_cuenta_ninguno", len(con_ancha), len(anchos)))
    print("")

    print("E) LAS TRES EXCLUSIONES VIEJAS SIGUEN MORDIENDO, Y UNA NORMAL NO")
    for rel, esperado in (("docs/loop/SALIDA_V171_APERTURA.txt", "SALIDA"),
                          ("docs/loop/reportes/SALIDA_V1_X.txt", "SALIDA"),
                          ("docs/loop/REPORTE.md", "NARRATIVO"),
                          ("docs/loop/ACTA_AUDITOR.md", "NARRATIVO"),
                          ("docs/loop/PROMPT_SIGUIENTE.md", "NARRATIVO"),
                          ("docs/loop/ultimo_ejecutor.json", "ARNES"),
                          ("docs/loop/ultimo_auditor.json", "ARNES"),
                          ("docs/plan/LECTURAS_DIRIGIDAS.md", None),
                          ("docs/PENDIENTES.md", None),
                          ("docs/plan/00_INDICE.md", None)):
        m = C.motivo_de_exclusion(rel)
        print("   %-44s -> %-10s (se esperaba %s)" % (rel, m, esperado))
        casos.append(("E_%s" % rel.replace("/", "_"), m, esperado))
    print("")

    print("F) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-54s %s   (real=%r esperado=%r)"
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
        elif esperado is None:
            mutado = "NARRATIVO"
        else:
            mutado = str(esperado) + "_mutado"
        cae = (real != mutado)
        print("   %-54s %s   (esperado mutado=%r)"
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
