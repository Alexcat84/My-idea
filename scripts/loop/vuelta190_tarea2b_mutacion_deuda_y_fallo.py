# -*- coding: utf-8 -*-
r"""vuelta190_tarea2b_mutacion_deuda_y_fallo.py . EL CASO POSITIVO POR MUTACION DE
LA SEPARACION DE LA DEUDA Y EL FALLO, Y DE QUE LA GUARDA ESTE ENCHUFADA AL
VEREDICTO.

QUIEN LO ENCARGA. Las adjudicaciones `4.4` y `4.6` del acta 190. La `4.6` tumba el
`D.5` de la 189, que saco `guarda_del_sujeto_congelado()` del veredicto del
instrumento de la nomina: **publicar los tres nombres arriba y cerrar en verde
deja sin sintoma al que solo mire el veredicto**. La `4.4` dice que un unico `1`
para un arnes caido y para una deuda declarada es degradacion silenciosa.

SUJETO CONGELADO: este arnes NO abre ningun fichero vivo del repo. Sus sujetos son
`motivo_del_sujeto_vivo()`, `guarda_del_sujeto_congelado_separada()` y
`clase_del_rojo()` de `scripts/loop/verificar_mutaciones_viejas.py`, **importadas**
(el modulo es codigo, no un fichero que la campana mueva cada vuelta), y corren
sobre TEXTOS FABRICADOS y sobre un DIRECTORIO FABRICADO en un temporal que este
mismo fichero retira (`P.16`, quien fabrica limpia).

QUE PRUEBA, CASO A CASO, Y TODOS TIENEN QUE CAER AL MUTAR SU ESPERADO:

  (A) LA VARA DEL MOTIVO ESCRITO DISTINGUE DE VERDAD. Un texto que abre el
      fichero vivo sin explicar nada sale SIN MOTIVO; uno que lo nombra al lado de
      un `git show` con su `COMMIT` sale CON MOTIVO. **Y la vara no se puede
      ensanchar sin que se note**: corrida con la lista de marcas VACIA, hasta el
      que si explica sale SIN MOTIVO, que es la prueba de que las marcas son las
      que deciden y no el azar.

  (B) LA REGLA DE `TODAS LAS APARICIONES` NO ES DECORATIVA. Un texto con DOS
      apariciones, una explicada y otra no, sale **SIN MOTIVO ESCRITO**. Si
      bastara con una, una apertura sin explicar se colaria detras de otra que si
      lo esta.

  (C) LA SEPARACION SUMA LO MISMO QUE LA GUARDA SIN SEPARAR. Sobre una nomina y un
      directorio fabricados, `len(sujeto_vivo) + len(con_motivo) + len(sin_motivo)`
      tiene que ser exactamente `len(guarda_del_sujeto_congelado())`. **Si la
      separacion perdiera una por el camino, la deuda se estaria escondiendo en
      vez de declarando.**

  (D) `SUJETO VIVO` CUENTA COMO FALLO Y NO COMO DEUDA. Un arnes que abre el
      fichero de hoy sin nada que lo module no mide su maquina, mide el dia, y eso
      es la guarda rota. Se prueba que cae en `sujeto_vivo` y que arrastra la
      clase a `ROJO POR FALLO` aunque no haya ninguna otra pieza de fallo.

  (E) LA PRECEDENCIA: EL FALLO GANA. Con deuda Y fallo a la vez, la clase es
      `ROJO POR FALLO`. Publicar `ROJO POR DEUDA DECLARADA` habiendo un arnes
      caido seria la misma degradacion, pero al reves.

  (F) LA GUARDA ESTA ENCHUFADA AL VEREDICTO, Y ESO SE PRUEBA QUITANDOLE LA PIEZA.
      Es el remedio del `D.5` tumbado: con la deuda dentro, la clase es
      `ROJO POR DEUDA DECLARADA` y el exitcode **2**; con la deuda fuera (que es
      lo que el `D.5` hacia), la clase es `VERDE` y el exitcode **0**. **Si las
      dos dieran lo mismo, la guarda no estaria enchufada.**

  (G) LOS TRES EXITCODES SON DISTINTOS Y LOS DOS ROJOS SIGUEN SIENDO DISTINTOS DE
      CERO. No se afloja nada: nadie que compruebe `!= 0` cambia de conducta.

USO:
  python scripts/loop/vuelta190_tarea2b_mutacion_deuda_y_fallo.py
"""
import io
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as V   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
Q3 = chr(34) * 3

# LOS TEXTOS FABRICADOS. Ninguno es un fichero del repo: se escriben en un
# temporal que este mismo arnes retira.
#
# COMO SE FABRICA UN `NO DECIDIBLE`, Y ESTO NO ES UN DETALLE: `anclaje_de()` lo
# devuelve solo cuando el TEXTO ENTERO trae huella de congelado Y LA MAQUINA trae
# huella de vivo. Por eso los tres de abajo llevan su huella de congelado EN EL
# DOCSTRING (que `sin_docstring_de_modulo()` recorta antes de buscar el motivo) y
# su huella de vivo EN LA MAQUINA. **Sin eso salen `SUJETO VIVO` y el caso no
# prueba lo que dice probar**, cosa que este arnes cazo en su primera corrida.
SIN_EXPLICAR = (Q3 + "Un arnes de mentira que clava su sujeto por sha256 y luego"
                + NL + "no explica nada de lo que abre." + Q3 + NL
                + "import io" + NL
                + "t = io.open('docs/loop/REPORTE.md').read()" + NL
                + "print(len(t))" + NL)
CON_GIT_SHOW = (Q3 + "Otro de mentira, con su sujeto congelado por git show." + Q3 + NL
                + "import subprocess" + NL
                + "COMMIT = 'abc1234'" + NL
                + "r = subprocess.run(['git', 'show', COMMIT + ':docs/loop/REPORTE.md'])" + NL)
MEDIO_EXPLICADO = (Q3 + "Uno con DOS apariciones y solo una explicada, y su sujeto"
                   + NL + "clavado por sha256." + Q3 + NL
                   + "import io, subprocess" + NL
                   + "COMMIT = 'abc1234'" + NL
                   + "r = subprocess.run(['git', 'show', COMMIT + ':docs/loop/REPORTE.md'])" + NL
                   + "x = 1" + NL
                   + "y = 2" + NL
                   + "z = 3" + NL
                   + "w = 4" + NL
                   + "t = io.open('docs/loop/REPORTE.md').read()" + NL)
# ESTE TIENE SU MOTIVO EN LA LINEA DE AL LADO Y NO EN LA SUYA, que es lo que hace
# que la VENTANA se pueda mutar de verdad: con ventana 3 lo ve y con ventana 0 no.
MOTIVO_AL_LADO = (Q3 + "Uno cuyo motivo vive en la linea de arriba, y su sujeto"
                  + NL + "clavado por sha256." + Q3 + NL
                  + "import io" + NL
                  + "# el sujeto sale de un git show, no del arbol de hoy" + NL
                  + "RUTA = 'docs/loop/REPORTE.md'" + NL
                  + "print(RUTA)" + NL)
# ESTE SALE `SUJETO VIVO` Y NO `NO DECIDIBLE`: no trae NINGUNA huella de
# congelado, asi que `anclaje_de()` no tiene nada que mezclar.
SUJETO_VIVO = (Q3 + "Uno que abre el fichero de hoy y no tiene nada que lo module." + Q3 + NL
               + "import io" + NL
               + "t = io.open('docs/INTRA_DOMINIO_VEREDICTOS.jsonl').read()" + NL)
CONGELADO = (Q3 + "Uno limpio: SUJETO CONGELADO declarado." + Q3 + NL
             + "import tempfile" + NL
             + "d = tempfile.mkdtemp()" + NL)


def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    w("   %-56s obtenido %-26s esperado %-26s -> %s"
      % (nombre, repr(obtenido), repr(esperado), "PASA" if ok else "CAE"))
    return 0 if ok else 1


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION: LA DEUDA SEPARADA DEL FALLO, Y LA GUARDA")
    w("ENCHUFADA AL VEREDICTO (vuelta 190, TAREA 2)")
    w("=" * 78)
    w("")
    fallos = 0
    no_cayeron = 0
    tmp = tempfile.mkdtemp(prefix="v190_t2_")
    try:
        w("A) LA VARA DEL MOTIVO ESCRITO, SOBRE TEXTOS FABRICADOS")
        w("   marcas de la casa (%d): %s"
          % (len(V.MARCAS_DE_MOTIVO), ", ".join(V.MARCAS_DE_MOTIVO)))
        w("   ventana: +/- %d lineas sobre la maquina" % V.VENTANA_DE_MOTIVO)
        for etiqueta, txt, esperado in (("sin explicar nada", SIN_EXPLICAR, False),
                                        ("con git show y COMMIT", CON_GIT_SHOW, True)):
            tiene, ev = V.motivo_del_sujeto_vivo(txt)
            fallos += _caso(w, "MOTIVO ESCRITO del fabricado %s" % etiqueta,
                            tiene, esperado)
            for ln, h, marcas in ev:
                w("      linea %-3d huella %-32s marcas: %s"
                  % (ln, h, ", ".join(marcas) or "(NINGUNA)"))
        w("   LA MUTACION: con la lista de marcas VACIA, hasta el que SI explica")
        w("   tiene que salir SIN MOTIVO. Si no cambiara, las marcas no deciden.")
        vacio, _ev = V.motivo_del_sujeto_vivo(CON_GIT_SHOW, marcas=())
        if vacio:
            w("      LA MUTACION NO CAYO: sin marcas sigue diciendo que hay motivo.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: sin marcas sale SIN MOTIVO, o sea que la vara")
            w("      la deciden las marcas y no el azar.")
        w("   LA MUTACION 2: el que se apoya en la linea DE AL LADO tiene que perder")
        w("   su motivo cuando la ventana se cierra a 0.")
        v3, _e3 = V.motivo_del_sujeto_vivo(MOTIVO_AL_LADO)
        v0, _e0 = V.motivo_del_sujeto_vivo(MOTIVO_AL_LADO, ventana=0)
        fallos += _caso(w, "motivo en la linea de al lado, ventana 3", v3, True)
        fallos += _caso(w, "el mismo texto con ventana 0", v0, False)
        if v3 == v0:
            w("      LA MUTACION NO CAYO: la ventana no cambia nada, o sea que no es")
            w("      la ventana la que decide.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: con ventana 3 sale SI y con ventana 0 sale NO.")
        w("")

        w("B) LA REGLA DE `TODAS LAS APARICIONES`, QUE NO ES DECORATIVA")
        tiene, ev = V.motivo_del_sujeto_vivo(MEDIO_EXPLICADO)
        w("   apariciones: %d" % len(ev))
        for ln, h, marcas in ev:
            w("      linea %-3d marcas: %s" % (ln, ", ".join(marcas) or "(NINGUNA)"))
        fallos += _caso(w, "una explicada y otra no -> SIN MOTIVO", tiene, False)
        w("   LA MUTACION: si bastara con UNA aparicion explicada, esto daria SI y")
        w("   una apertura sin explicar se colaria detras de otra que si lo esta.")
        alguna = any(bool(x) for _l, _h, x in ev)
        if not alguna:
            w("      LA MUTACION NO CAYO: no hay ninguna explicada, el caso no prueba.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: con la regla de `alguna` daria %s y con la de"
              % ("SI" if alguna else "NO"))
            w("      `todas` da %s. Las dos reglas NO dan lo mismo sobre este texto."
              % ("SI" if tiene else "NO"))
        w("")

        w("C) LA SEPARACION SUMA LO MISMO QUE LA GUARDA SIN SEPARAR")
        nomina = []
        for nombre, contenido in (("vuelta200_t1_mutacion_sin_explicar.py", SIN_EXPLICAR),
                                  ("vuelta200_t2_mutacion_con_motivo.py", CON_GIT_SHOW),
                                  ("vuelta200_t3_mutacion_medio.py", MEDIO_EXPLICADO),
                                  ("vuelta200_t4_mutacion_limpia.py", CONGELADO)):
            io.open(os.path.join(tmp, nombre), "w", encoding="utf-8").write(contenido)
            nomina.append((nombre, False))
        w("   directorio fabricado: %d ficheros" % len(os.listdir(tmp)))
        malas = V.guarda_del_sujeto_congelado(nomina, tmp)
        sep = V.guarda_del_sujeto_congelado_separada(nomina, tmp)
        w("   guarda_del_sujeto_congelado() sin separar: %d" % len(malas))
        for n, v, vv in malas:
            w("      %-14s %s" % (v, n))
        for clave in ("sujeto_vivo", "con_motivo", "sin_motivo"):
            w("   %-12s: %d (%s)"
              % (clave, len(sep[clave]),
                 ", ".join(n for n, _v, _vv, _e in sep[clave]) or "ninguna"))
        suma = sum(len(sep[k]) for k in sep)
        fallos += _caso(w, "la suma de las tres listas", suma, len(malas))
        fallos += _caso(w, "con motivo escrito", len(sep["con_motivo"]), 1)
        fallos += _caso(w, "sin motivo escrito", len(sep["sin_motivo"]), 2)
        w("   LA MUTACION: el esperado de `con motivo` se cambia a 3 y tiene que CAER")
        if len(sep["con_motivo"]) == 3:
            w("      LA MUTACION NO CAYO.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: son %d y no 3." % len(sep["con_motivo"]))
        w("")

        w("D) `SUJETO VIVO` ES FALLO Y NO DEUDA")
        io.open(os.path.join(tmp, "vuelta200_t5_mutacion_vivo.py"), "w",
                encoding="utf-8").write(SUJETO_VIVO)
        nomina_v = nomina + [("vuelta200_t5_mutacion_vivo.py", False)]
        sep_v = V.guarda_del_sujeto_congelado_separada(nomina_v, tmp)
        fallos += _caso(w, "cae en la lista de SUJETO VIVO",
                        [n for n, _v, _vv, _e in sep_v["sujeto_vivo"]],
                        ["vuelta200_t5_mutacion_vivo.py"])
        clase_v = V.clase_del_rojo([], [], [], [], [], sep_v)
        fallos += _caso(w, "y arrastra la clase a ROJO POR FALLO",
                        clase_v, V.ROJO_POR_FALLO)
        w("   LA MUTACION: sin el SUJETO VIVO, la misma nomina da otra clase")
        clase_sin = V.clase_del_rojo([], [], [], [], [], sep)
        if clase_sin == clase_v:
            w("      LA MUTACION NO CAYO: quitar el SUJETO VIVO no cambia la clase.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: con el es %r y sin el es %r."
              % (clase_v, clase_sin))
        w("")

        w("E) LA PRECEDENCIA: EL FALLO GANA")
        casos = (
            ("solo deuda", ([], [], [], [], []), sep, V.ROJO_POR_DEUDA),
            ("deuda y un arnes caido", ([], ["x.py"], [], [], []), sep, V.ROJO_POR_FALLO),
            ("deuda y un hueco de censo", ([], [], [], ["y.py"], []), sep, V.ROJO_POR_FALLO),
            ("ni deuda ni fallo", ([], [], [], [], []),
             {"sujeto_vivo": [], "con_motivo": [], "sin_motivo": []}, V.VERDE),
        )
        for etiqueta, piezas, s, esperado in casos:
            obtenido = V.clase_del_rojo(piezas[0], piezas[1], piezas[2], piezas[3],
                                        piezas[4], s)
            fallos += _caso(w, etiqueta, obtenido, esperado)
        w("   LA MUTACION: el esperado de `deuda y un arnes caido` se cambia a")
        w("   ROJO POR DEUDA DECLARADA y tiene que CAER")
        mut = V.clase_del_rojo([], ["x.py"], [], [], [], sep)
        if mut == V.ROJO_POR_DEUDA:
            w("      LA MUTACION NO CAYO: publicaria deuda habiendo un arnes caido.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: sale %r, o sea que el fallo gana." % mut)
        w("")

        w("F) LA GUARDA ESTA ENCHUFADA AL VEREDICTO, Y SE PRUEBA QUITANDOLE LA PIEZA")
        w("   (es el remedio del `D.5` que el acta 190 tumbo en su `4.6`: con la")
        w("    guarda fuera, esto cerraba en VERDE con tres entradas en deuda)")
        vacia = {"sujeto_vivo": [], "con_motivo": [], "sin_motivo": []}
        con = V.clase_del_rojo([], [], [], [], [], sep)
        sin = V.clase_del_rojo([], [], [], [], [], vacia)
        fallos += _caso(w, "CON la deuda dentro del veredicto", con, V.ROJO_POR_DEUDA)
        fallos += _caso(w, "SIN la deuda (lo que hacia el D.5)", sin, V.VERDE)
        fallos += _caso(w, "exitcode CON la deuda dentro",
                        V.CODIGO_DE_LA_CLASE[con], 2)
        fallos += _caso(w, "exitcode SIN la deuda", V.CODIGO_DE_LA_CLASE[sin], 0)
        if con == sin:
            w("      LA MUTACION NO CAYO: quitar la pieza no cambia el veredicto, o")
            w("      sea que la guarda NO estaba enchufada.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: %r con la pieza y %r sin ella. La guarda esta"
              % (con, sin))
            w("      enchufada, que es lo que la 4.6 manda.")
        w("")

        w("G) LOS TRES EXITCODES, DISTINTOS, Y LOS DOS ROJOS DISTINTOS DE CERO")
        for clase in (V.VERDE, V.ROJO_POR_FALLO, V.ROJO_POR_DEUDA):
            w("   %-26s -> exitcode %d" % (clase, V.CODIGO_DE_LA_CLASE[clase]))
        codigos = sorted(V.CODIGO_DE_LA_CLASE.values())
        fallos += _caso(w, "los tres codigos son distintos",
                        len(set(codigos)), 3)
        fallos += _caso(w, "los dos rojos son distintos de cero",
                        [V.CODIGO_DE_LA_CLASE[V.ROJO_POR_FALLO] != 0,
                         V.CODIGO_DE_LA_CLASE[V.ROJO_POR_DEUDA] != 0],
                        [True, True])
        w("   NO SE AFLOJA NADA: quien compruebe `!= 0` no cambia de conducta.")
        w("")

        w("H) Y LA GUARDA VIEJA NO SE TOCA, QUE ES LA CONDICION DE NO ROMPER NADA")
        w("   `guarda_del_sujeto_congelado()` sigue devolviendo tuplas de 3 campos,")
        w("   que es lo que llaman los tres arneses viejos que la usan.")
        fallos += _caso(w, "campos de cada tupla de la guarda vieja",
                        sorted(set(len(x) for x in malas)), [3])
        w("")
    finally:
        # LA RUTA DEL TEMPORAL NO SE ESCRIBE EN LA SALIDA SELLADA, Y LA CAUSA ESTA
        # MEDIDA, NO SUPUESTA: `tempfile.mkdtemp` le pone un sufijo al azar, y la
        # primera version de este arnes lo imprimia. Su salida sellada salia con
        # LOS MISMOS BYTES Y OTRO `sha256` en cada corrida, y la doble corrida de
        # `vuelta190_tarea2_nomina.py` lo cazo como PARADA (`esta salida CAMBIA
        # SOLA`). Aqui se publica el PREFIJO, que es estable, y el veredicto de la
        # limpieza, que es lo que de verdad hay que comprobar.
        existia = os.path.exists(tmp)
        shutil.rmtree(tmp, ignore_errors=True)
        w("LIMPIEZA (`P.16`, quien fabrica limpia): el temporal se retira.")
        w("   prefijo del temporal (estable; el sufijo al azar NO se publica, para")
        w("   que esta salida sellada se repita byte a byte): v190_t2_")
        w("   existia antes de retirarlo: %s | existe despues: %s"
          % (existia, os.path.exists(tmp)))
        w("")

    w("=" * 78)
    w("CIFRA casos: los de arriba, uno por linea con PASA o CAE")
    w("CIFRA casos que CAEN: %d" % fallos)
    w("CIFRA mutaciones que NO cayeron (y deberian): %d" % no_cayeron)
    w("VEREDICTO: %s" % ("ROJO" if (fallos or no_cayeron) else "VERDE"))
    texto = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(texto.encode("utf-8"))))
    return 1 if (fallos or no_cayeron) else 0


if __name__ == "__main__":
    sys.exit(main())
