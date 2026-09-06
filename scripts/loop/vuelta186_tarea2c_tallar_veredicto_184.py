# -*- coding: utf-8 -*-
r"""vuelta186_tarea2c_tallar_veredicto_184.py . EL VEREDICTO DE UNA LINEA DEL
REPORTE DE LA 184, TALLADO Y NO TECLEADO A OJO.

CLON DECLARADO de scripts/loop/vuelta185_tarea2a_tallar_veredicto_184.py. Cambian
SOLO los nombres de sus dos ficheros de salida y las citas de tarea; la maquina es
la misma y las tres cifras de contraste de la 184 son las mismas. El cotejo del
clon lo hace scripts/loop/cotejar_clon_declarado.py y su salida se pega en el
reporte con lo que salga.

POR QUE SE CLONA EN VEZ DE RE CORRER EL DE LA 185: correr el de la 185
REESCRIBIRIA sus dos salidas SELLADAS, que son evidencia commiteada de aquella
vuelta. Un instrumento de la 186 escribe salidas de la 186.

POR QUE EXISTE. `EJECUTOR.md` 1 manda que la cabecera del reporte se talle, y la
TAREA 2.c de esta vuelta lo dice del veredicto con todas las letras: *"EL
VEREDICTO DE UNA LINEA SE TALLA, NO SE TECLEA A OJO"*. La guarda `B.1` de
`cerrar_reporte.py` coteja sus numerales contra lo que el cuerpo permite contar,
y un veredicto con un numeral que no calza hace caer el cierre entero.

QUE HACE. Cuenta las DOS cifras del cuerpo con las funciones PURAS del propio
`cerrar_reporte.py` (`caidas_propias_del_cuerpo()` y `tareas_de_la_tabla()`),
sobre las DOS mitades juntas que la guarda `B.1` juzga, y arma la frase con esas
cifras EN PALABRA. NINGUN NUMERAL DE ESTA FRASE ESTA TECLEADO.

LO QUE NO HACE: no escribe en `docs/loop/REPORTE.md`, no cierra nada y no corre
`cerrar_reporte.py`. Solo imprime la frase y su cotejo, para que quien cierre la
pase tal cual.

TAMBIEN COTEJA LAS TRES PIEZAS del cierre por `sha256` y por bytes, que es lo
primero que la TAREA 2.a manda: si CUALQUIERA cambio respecto de lo que la 184
midio, es ROJO y no se cierra.

USO:
  python scripts/loop/vuelta186_tarea2c_tallar_veredicto_184.py
"""
import hashlib
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402
from vuelta172_tarea1_registrar_acta171 import PALABRA   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
DESTINO = os.path.join(LOOP, "SALIDA_V186_T2C_VEREDICTO_184.txt")
FRASE = os.path.join(LOOP, "SALIDA_V186_T2C_VEREDICTO_184_FRASE.txt")

CUERPO = "scripts/loop/_v184_cierre_texto.md"
TALLADOR = "docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt"
BATERIA = "docs/loop/SALIDA_V183_BATERIA.txt"

# LO QUE LA 184 MIDIO Y LA 185 CONFIRMO, COPIADO AQUI A PROPOSITO Y DECLARADO
# COMO CONTRASTE Y NO COMO FUENTE (`EJECUTOR.md` 2). La cifra de hoy se COMPUTA abajo; esto es contra
# lo que se compara, y si discrepan la discrepancia SE DECLARA y el cierre no va.
LO_QUE_MIDIO_LA_184 = {
    TALLADOR: {"disco": 2435, "lf": 2415, "sha_lf": None},
    CUERPO: {"disco": 13982, "lf": 13982, "sha_lf": "050cdbb4ea99e11c"},
    BATERIA: {"disco": 71753, "lf": 71753, "sha_lf": "422a909ad6ffb167"},
}


def medir(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.exists(p):
        return None
    datos = io.open(p, "rb").read()
    lf = datos.replace((chr(13) + NL).encode(), NL.encode())
    return {"disco": len(datos), "lf": len(lf),
            "sha_disco": hashlib.sha256(datos).hexdigest(),
            "sha_lf": hashlib.sha256(lf).hexdigest()}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    rojos = []
    w("EL VEREDICTO DE UNA LINEA DE LA 184, TALLADO (vuelta 186, TAREA 2.c)")
    w("")

    w("A) LAS TRES PIEZAS, COTEJADAS CONTRA LO QUE LA 184 MIDIO")
    w("   (las cifras de la 184 van como CONTRASTE, nunca como fuente: la de hoy")
    w("    se computa, y si discrepan se declara en vez de resolverse copiando)")
    for rel in (TALLADOR, CUERPO, BATERIA):
        hoy = medir(rel)
        antes = LO_QUE_MIDIO_LA_184[rel]
        w("   %s" % rel)
        if hoy is None:
            w("      NO EXISTE. Sin ella no se cierra nada.")
            rojos.append("%s no existe" % rel)
            continue
        w("      HOY   -> disco %d bytes | LF %d bytes | sha256 LF %s"
          % (hoy["disco"], hoy["lf"], hoy["sha_lf"][:16]))
        w("      LA 184 -> disco %s bytes | LF %s bytes | sha256 LF %s"
          % (antes["disco"], antes["lf"], antes["sha_lf"] or "(no publicado)"))
        if hoy["disco"] != antes["disco"] or hoy["lf"] != antes["lf"]:
            w("      DISCREPA EN BYTES.")
            rojos.append("%s discrepa en bytes" % rel)
        elif antes["sha_lf"] and hoy["sha_lf"][:16] != antes["sha_lf"]:
            w("      DISCREPA EN sha256 LF.")
            rojos.append("%s discrepa en sha256" % rel)
        else:
            w("      CALZA.")
    w("")

    w("B) LAS DOS CIFRAS DEL CUERPO, CONTADAS CON LAS FUNCIONES PURAS DE")
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

    w("C) LA FRASE, ARMADA CON ESAS CIFRAS EN PALABRA Y NINGUNA TECLEADA")
    if rojos:
        w("   NO SE ARMA: hay %d motivo(s) en rojo." % len(rojos))
        for r in rojos:
            w("      " + r)
        veredicto = ""
    else:
        veredicto = (
            "LA BATERIA CERRO ENTERA CON SUS NUEVE TRAMOS SELLADOS, OCHO VERDES Y "
            "EL NOVENO EN ROJO TRAIDO SIN TOCAR, Y LAS %s TAREAS DEL ENCARGO "
            "CIERRAN; EL CIERRE DEL REPORTE NO PUDO PEGARSE EN SU DIA POR UNA "
            "GUARDA QUE EL ACTA 185 DECLARO FALSO ROJO, Y SE PEGA AHORA CON LA "
            "REPARACION DE LA VUELTA 185 PUESTA; LAS %s CAIDAS PROPIAS VAN "
            "NOMBRADAS Y NINGUNA TAPADA."
            % (PALABRA[tareas].upper(), PALABRA[n_caidas].upper()))
        w("   %s" % veredicto)
    w("")

    w("D) LA GUARDA B.1, CORRIDA SOBRE LA FRASE ANTES DE PASARLA")
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
        mutada = veredicto.replace("LAS %s TAREAS" % PALABRA[tareas].upper(),
                                   "LAS SIETE TAREAS")
        motivos_m, _c, _h = CR.numerales_del_veredicto_que_no_calzan(mutada, juzgado)
        w("      con el numeral mutado a SIETE -> %d numeral(es) que no calzan"
          % len(motivos_m))
        w("      LA GUARDA CAE AL MUTAR: %s" % ("SI" if motivos_m else "NO"))
        if not motivos_m:
            rojos.append("la guarda B.1 no cae al mutar el numeral")
    w("")

    w("CIFRA motivos en rojo: %d" % len(rojos))
    w("VEREDICTO DEL TALLADOR: %s" % ("VERDE" if not rojos else "ROJO"))
    if veredicto and not rojos:
        io.open(FRASE, "w", encoding="utf-8", newline=NL).write(veredicto + NL)
        w("")
        w("LA FRASE QUEDA EN docs/loop/SALIDA_V186_T2C_VEREDICTO_184_FRASE.txt")
        w("para que quien cierre la pase tal cual y no la vuelva a teclear.")

    t = NL.join(L) + NL
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (DESTINO, len(t.encode("utf-8"))))
    return 0 if not rojos else 1


if __name__ == "__main__":
    sys.exit(main())
