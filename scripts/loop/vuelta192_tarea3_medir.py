# -*- coding: utf-8 -*-
r"""vuelta192_tarea3_medir.py . LA GUARDA DEL SUJETO CONGELADO, CORRIDA POR EL
EJECUTOR SOBRE LOS DOCE ARNESES DE LA 191, CON SUS TRES LISTAS Y SUS NOMBRES.

ES LA PIEZA `a` Y LA PIEZA `c` DE LA TAREA 3. El encargo dice, con esas palabras,
que si mi medicion no da 2 y 6, la mia manda y la del auditor se declara
equivocada, **y que para eso se publica el comando**. Aqui se publica el comando
y lo que salga.

Y AQUI SE MIDE ADEMAS UNA COSA QUE EL ENCARGO NO PIDE Y QUE CAMBIA SU PREMISA:
**CUALES DE LOS DOCE RECLAMA DE VERDAD LA REGLA DE ENTRADA DEL PROPIO FICHERO.**
El hallazgo `5.1` del acta 192 dice en su titulo que los dos `SUJETO VIVO`
*"ENTRAN EN LA NOMINA DE LA BATERIA A LA VUELTA SIGUIENTE"*. Eso **no se cree: se
corre**. La regla de entrada es `PATRON_ARNES` de
`verificar_mutaciones_viejas.py`, que exige que el NOMBRE del fichero contenga
`mutacion`, `caso_positivo` o `simular`, y **ninguno de los dos `SUJETO VIVO` lo
contiene**. Lo que salga se publica al lado de lo que el acta dice, y **ninguna
de las dos cifras se resuelve copiando**.

LO QUE ESTE FICHERO NO HACE: no toca la nomina (no se poda, no se adelanta y no
se le anaden entradas: la opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue
rechazada), no corre ningun arnes, no corre la bateria y no arregla ningun
`sin_motivo`: el encargo dice EXPRESAMENTE que no se arreglen a ciegas.

USO:
  python scripts/loop/vuelta192_tarea3_medir.py
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as VMV   # noqa: E402
import guarda_de_entrada_a_la_nomina as PUERTA   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
DIR = os.path.join(RAIZ, "scripts", "loop")
NL = chr(10)
SALIDA = os.path.join(LOOP, "SALIDA_V192_T3_GUARDA.txt")
PAT_191 = re.compile(r"^vuelta191_.*\.py$")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 192, TAREA 3.a y 3.c: LA GUARDA DEL SUJETO CONGELADO SOBRE LOS")
    w("ARNESES DE LA 191, CORRIDA POR EL EJECUTOR")
    w("=" * 78)
    w("")
    w("EL COMANDO, PUBLICADO PARA QUE SE PUEDA CONTRADECIR:")
    w("   VMV.guarda_del_sujeto_congelado_separada(nomina=[(n, True) for n in")
    w("                                            los_ficheros_vuelta191])")
    w("   con VMV = scripts/loop/verificar_mutaciones_viejas.py, importado y no")
    w("   copiado, y la nomina pasada POR PARAMETRO sin tocar `VIEJAS`.")
    w("")

    w("A) LOS ARNESES DE LA 191, DESCUBIERTOS POR PATRON Y NO TECLEADOS")
    doce = sorted(n for n in os.listdir(DIR) if PAT_191.match(n))
    w("   patron: %r" % PAT_191.pattern)
    w("   CIFRA ficheros que casan: %d (el acta 192 dice DOCE)" % len(doce))
    for n in doce:
        w("      %-52s %8d bytes" % (n, os.path.getsize(os.path.join(DIR, n))))
    w("")

    w("B) LA NOMINA DE HOY, QUE ESTA VUELTA NO TOCA")
    w("   CIFRA entradas de VMV.VIEJAS: %d (el acta 192 dice 127)" % len(VMV.VIEJAS))
    sep_hoy = VMV.guarda_del_sujeto_congelado_separada()
    for clave in ("sujeto_vivo", "con_motivo", "sin_motivo"):
        val = sep_hoy.get(clave, [])
        w("   nomina de hoy -> %-12s %d" % (clave, len(val)))
        for fila in val:
            w("      %s   %s" % (fila[0], fila[1]))
    w("   el acta 192 dice `sujeto_vivo 0` y `sin_motivo 0` sobre la nomina: %s"
      % ("CALZA" if (not sep_hoy["sujeto_vivo"] and not sep_hoy["sin_motivo"])
         else "NO CALZA, y la discrepancia se declara"))
    w("")

    w("C) LAS TRES LISTAS SOBRE LOS DOCE ARNESES DE LA 191, CON SUS NOMBRES")
    sep = VMV.guarda_del_sujeto_congelado_separada(
        nomina=[(n, True) for n in doce])
    for clave, etiqueta in (
            ("sujeto_vivo", "SUJETO VIVO (es FALLO, no deuda: 4.4 del acta 191)"),
            ("con_motivo", "NO DECIDIBLE CON MOTIVO ESCRITO (deuda declarada)"),
            ("sin_motivo", "NO DECIDIBLE SIN MOTIVO ESCRITO (deuda sin declarar)")):
        val = sep[clave]
        w("   CIFRA %s: %d" % (etiqueta, len(val)))
        for nombre, _v, vive, evidencia in val:
            w("      %s" % nombre)
            w("         huellas de vivo: %s" % (", ".join(vive) or "(ninguna)"))
            for ln, h, marcas in evidencia:
                w("         linea %-5d huella %-28s marcas: %s"
                  % (ln, h, ", ".join(marcas) or "(NINGUNA)"))
        if not val:
            w("      (ninguna, y el cero va escrito)")
    w("")
    w("   LO QUE EL ACTA 192 DICE Y LO QUE ESTA CORRIDA DA, LAS DOS CIFRAS:")
    w("      sujeto_vivo: el acta dice 2, esta corrida da %d"
      % len(sep["sujeto_vivo"]))
    w("      sin_motivo:  el acta dice 6, esta corrida da %d"
      % len(sep["sin_motivo"]))
    w("   (esta corrida es POSTERIOR a la pieza `b`, que declaro los dos sujetos")
    w("    por sus carriles. La cifra de ANTES, medida en el bloque H.4 del sello")
    w("    de apertura de esta vuelta y ANTES de la primera operacion, fue")
    w("    `sujeto_vivo 2` y `sin_motivo 6`, o sea que el acta CALZABA)")
    w("")

    w("D) LA MEDICION QUE EL ENCARGO NO PIDE Y QUE CAMBIA SU PREMISA:")
    w("   CUALES DE LOS DOCE RECLAMA DE VERDAD LA REGLA DE ENTRADA")
    w("   la regla es VMV.PATRON_ARNES, leida del fichero y no tecleada:")
    w("      %r" % VMV.PATRON_ARNES.pattern)
    w("      familias que exige en el NOMBRE: %s" % ", ".join(VMV.FAMILIAS_DE_ARNES))
    w("      vara del censo: %s" % VMV.VARA_DEL_CENSO)
    censo = VMV.arneses_del_directorio()
    w("   CIFRA ficheros en el censo entero: %d" % len(censo))
    dentro = [n for n in doce if n in set(censo)]
    w("   CIFRA de los DOCE que el censo ve: %d" % len(dentro))
    for n in doce:
        w("      %-52s en el censo: %s" % (n, "SI" if n in set(censo) else "no"))
    _ult, faltan = VMV.arneses_que_faltan()
    w("   Y LOS QUE `arneses_que_faltan()` RECLAMA HOY: %d" % len(faltan))
    for n in faltan:
        w("      %s" % n)
    vivos = [f[0] for f in sep["sujeto_vivo"]]
    w("")
    w("   EL CRUCE, QUE ES LA CIFRA QUE IMPORTA:")
    w("      arneses de la 191 con SUJETO VIVO: %d (%s)"
      % (len(vivos), ", ".join(vivos) or "ninguno"))
    w("      de esos, RECLAMADOS por el censo: %d (%s)"
      % (len(set(vivos) & set(faltan)),
         ", ".join(sorted(set(vivos) & set(faltan))) or "ninguno"))
    w("")

    w("E) LA GUARDA DE LA PUERTA, QUE ES LA PIEZA `e`, CORRIDA AQUI")
    v = PUERTA.veredicto_de_entrada()
    for l in PUERTA.informe(v):
        w("   " + l)
    w("")

    w("F) LO QUE NO SE TOCA, DICHO CON SUS CIFRAS")
    w("   la nomina sigue en %d entradas: no se poda, no se adelanta y no se le"
      % len(VMV.VIEJAS))
    w("   anade nada. La opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue")
    w("   rechazada, y quien mete a alguien en la nomina es la regla del fichero.")
    w("   Los `sin_motivo` NO SE ARREGLAN AQUI: el encargo lo prohibe con esas")
    w("   palabras, y su diagnostico uno a uno va en el reporte.")
    w("")
    w("FIN")

    t = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V192_T3_GUARDA.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
