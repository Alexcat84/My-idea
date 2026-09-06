# -*- coding: utf-8 -*-
r"""vuelta186_tallar_veredicto.py . EL VEREDICTO DE UNA LINEA DEL REPORTE DE LA
186, TALLADO Y NO TECLEADO A OJO.

CLON DECLARADO de scripts/loop/vuelta186_tarea2c_tallar_veredicto_184.py en su
forma, no en su contenido: cambia el sujeto (la 186 en vez de la 184), cae el
bloque de las tres piezas, que era propio del cierre de la 184, y la frase es
otra. El cotejo del clon lo hace scripts/loop/cotejar_clon_declarado.py y su
salida se pega en el reporte con lo que salga.

POR QUE EXISTE. `EJECUTOR.md` 1: la cabecera del reporte se talla, y el veredicto
lleva numerales que la guarda `B.1` de `cerrar_reporte.py` coteja contra lo que el
cuerpo permite contar. NINGUN NUMERAL DE ESTA FRASE ESTA TECLEADO: los dos salen
de las funciones puras del propio instrumento, sobre las DOS mitades juntas que la
guarda `B.1` juzga.

EL CERO ENTRA EN PALABRA, y hace falta decirlo: esta vuelta no levanta ninguna
caida propia, asi que el numeral de las caidas es CERO, y un veredicto que se
callara ese campo no seria lo mismo que uno que lo cuenta.

USO:
  python scripts/loop/vuelta186_tallar_veredicto.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
DESTINO = os.path.join(LOOP, "SALIDA_V186_VEREDICTO.txt")
FRASE = os.path.join(LOOP, "SALIDA_V186_VEREDICTO_FRASE.txt")
CUERPO = "scripts/loop/_v186_cierre_texto.md"

# LA TABLA DE NUMERALES EN PALABRA, CON EL CERO DENTRO. Se lee del propio
# instrumento para no tener dos tablas distintas del mismo dato: `cerrar_reporte`
# ya lleva la suya y esta la invierte.
NUMERO_A_PALABRA = {}
for _p, _n in CR.PALABRA_A_NUMERO.items():
    NUMERO_A_PALABRA.setdefault(_n, _p)
NUMERO_A_PALABRA[1] = "una"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    rojos = []
    w("EL VEREDICTO DE UNA LINEA DE LA 186, TALLADO (vuelta 186, TAREA 2.e)")
    w("")

    w("A) LAS DOS CIFRAS DEL CUERPO, CONTADAS CON LAS FUNCIONES PURAS DE")
    w("   cerrar_reporte.py SOBRE LAS DOS MITADES QUE LA GUARDA B.1 JUZGA")
    texto = CR.leer(CR.REPORTE)
    cuerpo = CR.leer(os.path.join(RAIZ, CUERPO.replace("/", os.sep)))
    juzgado = texto + NL + cuerpo
    caidas = CR.caidas_propias_del_cuerpo(juzgado)
    tareas = CR.tareas_de_la_tabla(juzgado)
    w("   docs/loop/REPORTE.md -> %d bytes | %s -> %d bytes"
      % (len(texto.encode("utf-8")), CUERPO, len(cuerpo.encode("utf-8"))))
    w("   caidas_propias_del_cuerpo() -> %s"
      % (sorted(caidas) if caidas is not None else "(el cuerpo no permite contarlo)"))
    w("   tareas_de_la_tabla()        -> %s" % tareas)
    n_caidas = len(caidas) if caidas is not None else None
    if n_caidas is None or tareas is None:
        rojos.append("el cuerpo no permite contar una de las dos especies")
    w("")

    w("B) LA FRASE, ARMADA CON ESAS CIFRAS EN PALABRA Y NINGUNA TECLEADA")
    if rojos:
        w("   NO SE ARMA: hay %d motivo(s) en rojo." % len(rojos))
        for r in rojos:
            w("      " + r)
        veredicto = ""
    else:
        # LA CONCORDANCIA DEL SEGUNDO NUMERAL VA DENTRO DEL COMPUTO, no fuera:
        # con una caida el sustantivo es singular y la coda dice que se levanta,
        # y con cero es plural y la coda dice que el cero va contado. Escribirlo
        # a mano seria teclear una cifra por la puerta de atras.
        if n_caidas == 1:
            coda = "UNA CAIDA PROPIA, LEVANTADA POR MI ANTES DE QUE LA MIDA NADIE"
        else:
            coda = ("%s CAIDAS PROPIAS, Y EL CERO VA CONTADO Y NO OMITIDO"
                    % NUMERO_A_PALABRA[n_caidas].upper())
        veredicto = (
            "LAS %s TAREAS DEL ENCARGO CIERRAN Y ESTA VUELTA CIERRA SU PROPIO "
            "REPORTE, QUE ES LA SEGUNDA SEGUIDA Y DEVUELVE EL TOPE A CINCO; LAS "
            "DOS ADJUDICACIONES DEL ACTA 186 QUEDAN APLICADAS CON UN ARNES CADA "
            "UNA, EL REPORTE DE LA 184 CIERRA EN VERDE POR EL CARRIL DE CIERRE "
            "TARDIO CON SUS DIEZ CIFRAS SIN PAREJA DECLARADAS, Y LA ESCALADA DE "
            "LA SECCION 4 CAZA LA CAIDA QUE LA TRAJO; %s."
            % (NUMERO_A_PALABRA[tareas].upper(), coda))
        w("   %s" % veredicto)
    w("")

    w("C) LA GUARDA B.1, CORRIDA SOBRE LA FRASE ANTES DE PASARLA")
    if veredicto:
        motivos, cuentas, hallados = CR.numerales_del_veredicto_que_no_calzan(
            veredicto, juzgado)
        w("   CIFRA numerales hallados en el veredicto: %d" % len(hallados))
        for crudo, valor, especie in hallados:
            w("      %-10r -> %d %s" % (crudo, valor, especie))
        w("   LAS CUENTAS DEL CUERPO:")
        for especie in sorted(cuentas):
            w("      %-8s -> %s" % (especie, cuentas[especie]))
        w("   CIFRA numerales que NO calzan: %d" % len(motivos))
        for m in motivos:
            w("      " + m)
        if motivos:
            rojos.extend(motivos)
        w("")
        w("   LA MUTACION, QUE ES LO QUE PRUEBA QUE ESTA GUARDA MUERDE: se cambia")
        w("   un numeral de la frase por otro y se comprueba que CAE.")
        mutada = veredicto.replace("LAS %s TAREAS" % NUMERO_A_PALABRA[tareas].upper(),
                                   "LAS SIETE TAREAS")
        motivos_m, _c, _h = CR.numerales_del_veredicto_que_no_calzan(mutada, juzgado)
        w("      con el numeral mutado a SIETE -> %d numeral(es) que no calzan"
          % len(motivos_m))
        w("      LA GUARDA CAE AL MUTAR: %s" % ("SI" if motivos_m else "NO"))
        if not motivos_m:
            rojos.append("la guarda B.1 no cae al mutar el numeral de tareas")
        mutada2 = veredicto.replace("; %s CAIDA" % coda.split(" CAIDA")[0],
                                    "; TRES CAIDAS")
        motivos_m2, _c2, _h2 = CR.numerales_del_veredicto_que_no_calzan(
            mutada2, juzgado)
        w("      con el numeral de caidas mutado a TRES -> %d que no calzan"
          % len(motivos_m2))
        w("      LA GUARDA CAE AL MUTAR EL SEGUNDO: %s"
          % ("SI" if motivos_m2 else "NO"))
        if not motivos_m2:
            rojos.append("la guarda B.1 no cae al mutar el numeral de caidas")
    w("")

    w("CIFRA motivos en rojo: %d" % len(rojos))
    w("VEREDICTO DEL TALLADOR: %s" % ("VERDE" if not rojos else "ROJO"))
    if veredicto and not rojos:
        io.open(FRASE, "w", encoding="utf-8", newline=NL).write(veredicto + NL)
        w("")
        w("LA FRASE QUEDA EN docs/loop/SALIDA_V186_VEREDICTO_FRASE.txt")
        w("para que quien cierre la pase tal cual y no la vuelva a teclear.")

    t = NL.join(L) + NL
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (DESTINO, len(t.encode("utf-8"))))
    return 0 if not rojos else 1


if __name__ == "__main__":
    sys.exit(main())
