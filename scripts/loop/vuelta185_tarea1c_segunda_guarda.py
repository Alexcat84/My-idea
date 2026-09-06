# -*- coding: utf-8 -*-
r"""vuelta185_tarea1c_segunda_guarda.py . LA MEDICION QUE LEVANTA LA PARADA DE LA
TAREA 1.c, HECHA ANTES DE CORRER LA TAREA 2.a Y SIN ESCRIBIR NADA.

POR QUE EXISTE. El encargo de la 1.c dice, con todas las letras: *"no se toca
ninguna otra guarda. Si al escribir esto ves que hace falta cambiar algo mas,
paras y lo traes"*. AL ESCRIBIR LA 1.c SE VE. `scripts/loop/cerrar_reporte.py`
lleva la regla de la vuelta ajena DOS VECES, en dos funciones distintas:

  1. En `rama_de_la_seccion9()`, que es la que el encargo manda reparar y la que
     esta reparada.
  2. En la PIEZA (4) de `piezas_que_faltan()`, que tiene su PROPIA copia de la
     misma regla y NO recibe el cuarto parametro. El encargo no la nombra.

CONSECUENCIA, DICHA ANTES DE MEDIRLA PARA QUE LA MEDICION NO PUEDA MAQUILLARSE:
`cerrar_reporte.py --vuelta 184` va a decidir la rama como `CORRIDA` (rama nueva),
va a ESCRIBIR el reporte en su bloque C, y despues, en su bloque D, la pieza (4)
va a caer, asi que el instrumento va a devolver exitcode 1.

ESTE FICHERO NO REPARA NADA Y NO ESCRIBE EN NINGUN SITIO SALVO SU PROPIA SALIDA.
Llama a `piezas_que_faltan()` sobre un texto de reporte FABRICADO, nunca sobre
`docs/loop/REPORTE.md`, y publica lo que salga.

USO:
  python scripts/loop/vuelta185_tarea1c_segunda_guarda.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
DESTINO = os.path.join(LOOP, "SALIDA_V185_T1C_SEGUNDA_GUARDA.txt")
FUENTE = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")


def reporte_fabricado():
    """UN REPORTE DE MENTIRA CON SUS CUATRO PIEZAS PUESTAS. No se toca
    `docs/loop/REPORTE.md` en ninguna linea."""
    filas = ["| celda %d | otra |" % k for k in range(1, 10)]
    lineas_bat = ["linea de bateria de mentira %d" % k for k in range(1, 6)]
    texto = ("# REPORTE DE LA VUELTA 184 (fabricado)" + NL
             + "**EL VEREDICTO DE UNA LINEA: un veredicto de mentira.**" + NL
             + NL.join(filas) + NL)
    for k in range(3, 10):
        texto += NL + "## %d. una seccion de mentira" % k + NL
    texto += NL.join(lineas_bat) + NL
    return texto, filas, lineas_bat


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("LA SEGUNDA GUARDA DE LA VUELTA AJENA, LOCALIZADA Y MEDIDA (vuelta 185,")
    w("TAREA 1.c). ESTE FICHERO NO REPARA NADA.")
    w("")
    w("A) LAS DOS SEDES DE LA MISMA REGLA, LOCALIZADAS EN EL FICHERO VIVO")
    fuente = io.open(FUENTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    lineas = fuente.split(NL)
    for i, l in enumerate(lineas, 1):
        if "ajena != vuelta" in l or "NO SATISFACE ESTA PIEZA" in l:
            w("   LINEA %d: %s" % (i, l.rstrip()[:140]))
    w("   CIFRA apariciones de 'ajena != vuelta' en cerrar_reporte.py: %d"
      % fuente.count("ajena != vuelta"))
    w("   CIFRA veces que aparece 'tramos_sellados_en_esta_vuelta': %d, y NINGUNA"
      % fuente.count("tramos_sellados_en_esta_vuelta"))
    w("   esta dentro de piezas_que_faltan(): esa funcion no recibe la evidencia.")
    w("")

    w("B) LA FUNCION DE VERDAD, LLAMADA SOBRE UN REPORTE FABRICADO")
    texto, filas, lineas_bat = reporte_fabricado()
    w("   el texto fabricado mide %d bytes y trae sus cuatro piezas puestas"
      % len(texto.encode("utf-8")))
    casos = [
        ("la bateria de la 183 pegada en un reporte de la 184 (EL CASO DE HOY)",
         "docs/loop/SALIDA_V183_BATERIA.txt", 184),
        ("la bateria de la 184 pegada en un reporte de la 184 (el caso normal)",
         "docs/loop/SALIDA_V184_BATERIA.txt", 184),
    ]
    for que, fichero, vuelta in casos:
        faltan = CR.piezas_que_faltan(texto, filas, lineas_bat, vuelta=vuelta,
                                      nombre_bateria=fichero)
        w("   %s" % que)
        w("      piezas_que_faltan() -> %d" % len(faltan))
        for f in faltan:
            w("         %s" % f[:150])
    w("")

    w("C) Y LA RAMA, PARA QUE SE VEA QUE LAS DOS NO DICEN LO MISMO")
    rama, motivo = CR.rama_de_la_seccion9(lineas_bat,
                                          "docs/loop/SALIDA_V183_BATERIA.txt",
                                          184, [5, 6, 7, 8, 9])
    w("   rama_de_la_seccion9() con la evidencia de tramos -> %s" % rama)
    w("   motivo: %s" % motivo[:200])
    faltan = CR.piezas_que_faltan(texto, filas, lineas_bat, vuelta=184,
                                  nombre_bateria="docs/loop/SALIDA_V183_BATERIA.txt")
    w("   piezas_que_faltan() sobre el mismo caso -> %d pieza(s) que faltan"
      % len(faltan))
    w("")
    w("D) LO QUE ESTO SIGNIFICA, DICHO SIN ADORNAR Y SIN ARREGLARLO")
    w("   La rama nueva dice CORRIDA y la pieza (4) dice que falta. LAS DOS SON")
    w("   LA MISMA REGLA ESCRITA DOS VECES, y el encargo de la 1.c solo nombra")
    w("   una. Reparar la otra seria tocar una guarda que el encargo prohibe")
    w("   tocar, asi que NO SE TOCA: se para y se trae, que es lo que el propio")
    w("   encargo manda con esas palabras.")
    w("   PREDICCION, ESCRITA ANTES DE CORRER LA TAREA 2.a: cerrar_reporte.py")
    w("   --vuelta 184 dara la rama CORRIDA, ESCRIBIRA el reporte en su bloque C,")
    w("   y devolvera exitcode 1 por la pieza (4) en su bloque D.")
    dice_corrida = (rama == "CORRIDA")
    dice_falta = bool(faltan)
    w("   LAS DOS CONDICIONES DE LA PREDICCION, MEDIDAS AQUI:")
    w("      la rama sale CORRIDA:          %s" % ("SI" if dice_corrida else "NO"))
    w("      la pieza (4) dice que falta:   %s" % ("SI" if dice_falta else "NO"))

    t = NL.join(L) + NL
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (DESTINO, len(t.encode("utf-8"))))
    # ESTE FICHERO NO ES UN ARNES: NO JUZGA, MIDE. Sale 0 siempre y el juicio lo
    # hace el reporte, que es donde vive la PARADA.
    return 0


if __name__ == "__main__":
    sys.exit(main())
