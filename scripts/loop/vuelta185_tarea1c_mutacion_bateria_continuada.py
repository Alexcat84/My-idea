# -*- coding: utf-8 -*-
r"""vuelta185_tarea1c_mutacion_bateria_continuada.py . EL ARNES DE LA RAMA DE LA
BATERIA CONTINUADA, LA REPARACION DE LA TAREA 1.c DE LA VUELTA 185.

DE DONDE VIENE, Y NO ES UNA MEJORA: es la adjudicacion `6.2` del acta 185, que
cierra la `PD.3` declarando FALSO ROJO el que `cerrar_reporte.py` daba sobre el
reporte de la 184. La guarda de la vuelta ajena nacio buena, contra PEDIR
PRESTADA la bateria terminada de otra vuelta, y ese caso sigue siendo ROJO. Lo
que faltaba era distinguir la bateria PRESTADA de la bateria CONTINUADA, que es
lo que `AUDITOR.md` 6.1 PIDE con las palabras del fundador: *"UNA VUELTA CORTADA
RETOMA EN EL TRAMO SIGUIENTE"*.

LA RAMA NUEVA EXIGE MAS QUE LA VIEJA, NO MENOS: cuatro condiciones a la vez, y si
falla cualquiera cae al ROJO de siempre con su texto palabra por palabra.

LOS SIETE CASOS QUE EL ENCARGO PIDE COMO MINIMO, MAS LOS DE `vuelta_que_sello()`
Y EL DE `tramos_por_vuelta()` SOBRE LOS NUEVE FICHEROS REALES (este ultimo es el
caso que la TAREA 1.d anade). TODOS TIENEN QUE CAER AL MUTAR SU ESPERADO, y la
mutacion se corre y se publica caso por caso.

NINGUNA COMPARACION DE AQUI ES ENTRE DOS CONSTANTES LITERALES: la rama SE COMPUTA
llamando a la funcion de verdad. Y EL MOTIVO DEL CASO B NO SE TECLEA: se exige
que sea IDENTICO al que la MISMA funcion devuelve con el cuarto parametro en su
valor por defecto, que es la conducta de hoy. Asi, si alguien reescribiera el
texto del rojo viejo, este caso caeria.

USO:
  python scripts/loop/vuelta185_tarea1c_mutacion_bateria_continuada.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
DESTINO = os.path.join(LOOP, "SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt")

CORRIDA = "docs/loop/SALIDA_V183_BATERIA.txt"
HUECO = "docs/loop/SALIDA_V183_HUECO_BATERIA.txt"
PROPIA = "docs/loop/SALIDA_V184_BATERIA.txt"
POSTERIOR = "docs/loop/SALIDA_V185_BATERIA.txt"

# LOS SIETE CASOS DEL ENCARGO. Cada uno es
# (letra, que se le pasa, n_lineas, fichero, vuelta, tramos, rama esperada).
# El esperado es lo unico escrito a mano; la rama sale de llamar a la funcion.
CASOS = [
    ("A", "bateria de la 183, cerrando la 184, CON tramos sellados en la 184",
     900, CORRIDA, 184, [5, 6, 7, 8, 9], "CORRIDA"),
    ("B", "bateria de la 183, cerrando la 184, con la lista VACIA",
     900, CORRIDA, 184, [], "ROJO"),
    ("C", "bateria de la 185 (POSTERIOR), cerrando la 184, con tramos",
     900, POSTERIOR, 184, [5, 6, 7, 8, 9], "ROJO"),
    ("D", "bateria de la 183, cerrando la 184, con tramos, nombre que NO es de "
     "corrida", 900, HUECO, 184, [5, 6, 7, 8, 9], "ROJO"),
    ("E", "bateria de la 183, cerrando la 184, con tramos, CERO lineas",
     0, CORRIDA, 184, [5, 6, 7, 8, 9], "ROJO"),
    ("F", "bateria de la 184 cerrando la 184, con lineas",
     900, PROPIA, 184, [5, 6, 7, 8, 9], "CORRIDA"),
]

# LOS CASOS DE `vuelta_que_sello()`, QUE ES PURA.
CASOS_ASUNTO = [
    ("un asunto que NOMBRA la vuelta",
     "VUELTA 184, BATERIA TRAMO 8 DE 9, SELLADO Y MEDIDO: VERDE, exitcode 0", 184),
    ("un asunto que NO la nombra",
     "ACTA DEL AUDITOR: LA 184 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA", None),
    ("un asunto que la nombra DOS VECES: se devuelve la PRIMERA",
     "VUELTA 184, TAREA 2: RETOMA LA BATERIA DE LA VUELTA 183 EN SU TRAMO 6", 184),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    fallos = 0
    w("ARNES DE LA RAMA DE LA BATERIA CONTINUADA (vuelta 185, TAREA 1.c)")
    w("sujeto vivo: scripts/loop/cerrar_reporte.py")
    w("")

    for nombre in ("rama_de_la_seccion9", "vuelta_que_sello", "tramos_por_vuelta"):
        if not hasattr(CR, nombre):
            w("ROJO: cerrar_reporte.py NO tiene %s(). La reparacion no esta puesta,"
              % nombre)
            w("      y este arnes no puede probar nada.")
            t = NL.join(L) + NL
            io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(t)
            print(t)
            return 1

    w("A) LOS SIETE CASOS, CON LA RAMA COMPUTADA Y NO ESCRITA")
    w("   (el caso G, el del cuarto parametro en su valor por defecto, va aparte")
    w("    abajo, porque compara CADA caso consigo mismo)")
    w("")
    medidos = {}
    for letra, que, n_lineas, fichero, vuelta, tramos, esperada in CASOS:
        lineas = ["x"] * n_lineas
        rama, motivo = CR.rama_de_la_seccion9(lineas, fichero, vuelta, tramos)
        medidos[letra] = (rama, motivo)
        ok = rama == esperada
        if not ok:
            fallos += 1
        w("   CASO %s. %s" % (letra, que))
        w("      lineas %-4d fichero %-40s vuelta %s tramos %s"
          % (n_lineas, os.path.basename(fichero), vuelta, tramos))
        w("      COMPUTADA -> %-8s | esperada %-8s | %s"
          % (rama, esperada, "CALZA" if ok else "NO CALZA"))
        w("      motivo: %s" % motivo[:200])
    w("")
    w("   CIFRA casos: %d" % len(CASOS))
    w("   CIFRA que CALZAN: %d" % (len(CASOS) - fallos))
    w("   CIFRA que NO CALZAN: %d" % fallos)
    w("")

    w("B) LA MUTACION DEL ESPERADO, CASO POR CASO. El esperado mutado es el otro")
    w("   valor posible, y si el caso pasara con los dos no estaria comparando")
    w("   nada.")
    n_caen = 0
    for letra, _que, _n, _f, _v, _tr, esperada in CASOS:
        rama, _m = medidos[letra]
        mutado = "ROJO" if esperada == "CORRIDA" else "CORRIDA"
        cae = rama != mutado
        if cae:
            n_caen += 1
        else:
            fallos += 1
        w("      CASO %s: esperado bueno %-8s | esperado MUTADO %-8s -> %s"
          % (letra, esperada, mutado, "CAE" if cae else "PASA, Y NO DEBERIA"))
    w("   CIFRA casos que CAEN al mutar su esperado: %d de %d" % (n_caen, len(CASOS)))
    w("")

    w("C) EL MOTIVO DEL CASO B, LITERAL E IGUAL AL DE HOY. No se teclea: se exige")
    w("   que sea IDENTICO al que la MISMA funcion devuelve con el cuarto")
    w("   parametro en su valor por defecto, que es la conducta de antes de esta")
    w("   reparacion. Si alguien reescribiera el texto del rojo viejo, esto cae.")
    rama_b, motivo_b = medidos["B"]
    rama_hoy, motivo_hoy = CR.rama_de_la_seccion9(["x"] * 900, CORRIDA, 184)
    ok_motivo = (motivo_b == motivo_hoy) and (rama_b == rama_hoy)
    w("      con la lista VACIA        -> %s | %s" % (rama_b, motivo_b[:130]))
    w("      con el defecto None       -> %s | %s" % (rama_hoy, motivo_hoy[:130]))
    w("      SON IDENTICOS: %s" % ("SI" if ok_motivo else "NO"))
    literal = "UNA CORRIDA DE OTRA VUELTA NO CIERRA ESTE REPORTE."
    w("      y el motivo lleva dentro %r: %s"
      % (literal, "SI" if literal in motivo_b else "NO"))
    if not ok_motivo or literal not in motivo_b:
        fallos += 1
    w("      con el esperado MUTADO (que NO fueran identicos): %s"
      % ("PASA" if not ok_motivo else "CAE"))
    w("")

    w("D) EL CASO G: EL CUARTO PARAMETRO EN SU VALOR POR DEFECTO `None` TIENE QUE")
    w("   COMPORTARSE EXACTAMENTE COMO HOY EN LOS CASOS A, B, C Y F. Es la")
    w("   promesa de que ningun llamador viejo cambia de conducta.")
    w("   LO QUE ERA HOY, RECONSTRUIDO SIN LA RAMA NUEVA: A, B y C son ROJO por")
    w("   vuelta ajena y F es CORRIDA. Aqui no se teclea: se llama sin el cuarto")
    w("   parametro y se publica lo que salga.")
    esperado_g = {"A": "ROJO", "B": "ROJO", "C": "ROJO", "F": "CORRIDA"}
    fallos_g = 0
    for letra in ("A", "B", "C", "F"):
        _l, _que, n_lineas, fichero, vuelta, _tr, _esp = [
            c for c in CASOS if c[0] == letra][0]
        rama_sin, motivo_sin = CR.rama_de_la_seccion9(
            ["x"] * n_lineas, fichero, vuelta)
        ok_g = rama_sin == esperado_g[letra]
        if not ok_g:
            fallos_g += 1
        w("      CASO %s sin el cuarto parametro -> %-8s | esperado %-8s | %s"
          % (letra, rama_sin, esperado_g[letra], "CALZA" if ok_g else "NO CALZA"))
        w("         motivo: %s" % motivo_sin[:130])
        mutado = "ROJO" if esperado_g[letra] == "CORRIDA" else "CORRIDA"
        if rama_sin == mutado:
            fallos_g += 1
        w("         con el esperado MUTADO %-8s -> %s"
          % (mutado, "CAE" if rama_sin != mutado else "PASA, Y NO DEBERIA"))
    w("   CIFRA fallos del caso G: %d" % fallos_g)
    fallos += fallos_g
    w("")
    w("   Y LA DIFERENCIA QUE LA REPARACION INTRODUCE, DICHA CON LAS DOS AL LADO:")
    for letra in ("A", "B", "C", "F"):
        rama_con, _m1 = medidos[letra]
        _l, _que, n_lineas, fichero, vuelta, _tr, _esp = [
            c for c in CASOS if c[0] == letra][0]
        rama_sin, _m2 = CR.rama_de_la_seccion9(["x"] * n_lineas, fichero, vuelta)
        w("      CASO %s: con tramos -> %-8s | con el defecto None -> %-8s | %s"
          % (letra, rama_con, rama_sin,
             "CAMBIA" if rama_con != rama_sin else "IGUAL"))
    w("")

    w("E) `vuelta_que_sello()`, QUE ES PURA, CON SUS TRES CASOS")
    for que, asunto, esperado in CASOS_ASUNTO:
        medido = CR.vuelta_que_sello(asunto)
        ok = medido == esperado
        if not ok:
            fallos += 1
        w("   %s" % que)
        w("      asunto: %s" % asunto[:130])
        w("      COMPUTADO -> %-6s | esperado %-6s | %s"
          % (medido, esperado, "CALZA" if ok else "NO CALZA"))
        mutado = 999 if esperado != 999 else 1
        w("      con el esperado MUTADO %-6s -> %s"
          % (mutado, "CAE" if medido != mutado else "PASA, Y NO DEBERIA"))
        if medido == mutado:
            fallos += 1
    w("")

    w("F) EL CASO QUE ANADE LA TAREA 1.d: `tramos_por_vuelta(183)` SOBRE LOS NUEVE")
    w("   FICHEROS REALES. El reparto tiene que ser 4 y 5: los tramos 1 a 4 los")
    w("   sello la vuelta 183 y los tramos 5 a 9 la vuelta 184. NO SE TECLEA")
    w("   NINGUNA CELDA: sale de leer el asunto del ultimo commit de cada fichero.")
    reparto = CR.tramos_por_vuelta(183)
    for n in sorted(reparto):
        w("      tramo %-3d -> vuelta %s" % (n, reparto[n]))
    w("   CIFRA tramos con fichero en disco: %d" % len(reparto))
    de_183 = sorted(n for n, v in reparto.items() if v == 183)
    de_184 = sorted(n for n, v in reparto.items() if v == 184)
    otras = sorted(n for n, v in reparto.items() if v not in (183, 184))
    w("   CIFRA sellados por la vuelta 183: %d %s" % (len(de_183), de_183))
    w("   CIFRA sellados por la vuelta 184: %d %s" % (len(de_184), de_184))
    w("   CIFRA sellados por otra vuelta o sin asunto: %d %s" % (len(otras), otras))
    ok_reparto = (len(de_183) == 4 and len(de_184) == 5 and not otras
                  and len(reparto) == 9)
    w("   EL REPARTO ES 4 Y 5 SOBRE NUEVE: %s" % ("SI" if ok_reparto else "NO"))
    if not ok_reparto:
        fallos += 1
    w("   con el esperado MUTADO (5 y 4): %s"
      % ("PASA" if (len(de_183) == 5 and len(de_184) == 4) else "CAE"))
    if len(de_183) == 5 and len(de_184) == 4:
        fallos += 1
    w("   con el esperado MUTADO (nueve tramos sellados por la 183): %s"
      % ("PASA" if len(de_183) == 9 else "CAE"))
    if len(de_183) == 9:
        fallos += 1
    w("")

    w("G) LO QUE ESTA REPARACION NO TOCA, DICHO PARA QUE SE PUEDA COMPROBAR:")
    w("   el fichero de la bateria no se copia ni se renombra; el rojo viejo no se")
    w("   afloja (su texto se compara literal en el bloque C); y no hay ninguna")
    w("   opcion de linea de ordenes para la lista de tramos, porque una evidencia")
    w("   que se puede teclear no es una evidencia.")
    fuente = io.open(os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py"),
                     encoding="utf-8").read()
    n_flag = fuente.count("--tramos")
    w("   CIFRA apariciones de '--tramos' en cerrar_reporte.py: %d" % n_flag)
    if n_flag:
        w("   ROJO: hay una bandera para la evidencia, y no puede haberla.")
        fallos += 1
    w("")

    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))

    t = NL.join(L) + NL
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (DESTINO, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
