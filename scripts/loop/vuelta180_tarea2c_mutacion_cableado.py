# -*- coding: utf-8 -*-
r"""vuelta180_tarea2c_mutacion_cableado.py . EL CASO POSITIVO POR MUTACION DEL
CABLEADO: SI LA GUARDA DEL SUJETO CONGELADO SE DESENCHUFA DEL ROJO GLOBAL, ESTE
CASO CAE.

TAREA 2.c de la vuelta 180. Sujetos: `hay_rojo_al_cierre()` y
`guarda_del_sujeto_congelado()` de `scripts/loop/verificar_mutaciones_viejas.py`.

SUJETO CONGELADO, y se dice como: este arnes fabrica un directorio de arneses de
mentira en un TEMPORAL y una nomina de mentira, y se los pasa por parametro a las
dos funciones. **No lee ni un fichero de la campana**, no corre la bateria y no
toca `scripts/loop/`. El temporal se retira al terminar (`P.16`).

QUE PRUEBA, Y POR QUE HACIA FALTA EXTRAER LA CONDICION. Hasta esta vuelta la
condicion del rojo global vivia dentro de un `if` de `main()`: la unica forma de
comprobar que una guarda estaba ENCHUFADA era correr la bateria entera y mirar el
color, que es justo lo que la 181 va a hacer y lo que aqui hay que garantizar
ANTES. Con la condicion en una funcion pura, se le quita una pieza a la vez.

LOS CASOS, Y TODOS CORREN:

  (A) `guarda_del_sujeto_congelado()` sobre un directorio fabricado:
      A1, un arnes que ABRE un fichero vivo y no lo declara sale senalado;
      A2, el MISMO arnes con la linea de declaracion anadida deja de salir.
      **Es exactamente el delta de la TAREA 2.a**, medido sobre mentira.
  (B) `hay_rojo_al_cierre()` con las seis piezas vacias: NO hay rojo.
  (C) `hay_rojo_al_cierre()` con SOLO la pieza del sujeto congelado llena:
      **HAY ROJO**. Este es el caso que prueba el cableado: si alguien
      desenchufa esa pieza, este caso CAE.
  (D) LA MUTACION, con la condicion VIEJA reproducida aqui (la de antes de esta
      vuelta, sin la pieza del sujeto congelado): sobre el MISMO escenario del
      caso (C) **NO hay rojo**. Sin esto, (C) no distinguiria una condicion que
      mira la pieza de una que se pone roja siempre.
  (E) Y una por una, las otras cinco piezas siguen encendiendo el rojo solas:
      cablear una pieza nueva no puede haber apagado ninguna vieja.

USO:
  python scripts/loop/vuelta180_tarea2c_mutacion_cableado.py
"""
import io
import os
import shutil
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import verificar_mutaciones_viejas as V   # noqa: E402

NL = chr(10)

# UN ARNES DE MENTIRA QUE ABRE UN FICHERO QUE LA CAMPANA MUEVE. Su docstring NO
# trae la marca de declaracion: por eso tiene que salir senalado.
ARNES_SIN_DECLARAR = (
    '# -*- coding: utf-8 -*-' + NL +
    'r"""arnes de mentira: abre un fichero vivo y no lo declara."""' + NL +
    'import io' + NL +
    'texto = io.open("docs/loop/REPORTE.md", encoding="utf-8").read()' + NL +
    'print(len(texto))' + NL)

# LA LINEA QUE LA TAREA 2.a ANADE, con el literal que la guarda busca.
LINEA_DECLARADA = ('r"""arnes de mentira: abre un fichero vivo. SUJETO CONGELADO: '
                   'declarado a mano en este caso de mentira."""')


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline=NL) as f:
        f.write(texto)


def condicion_vieja(perdidas, no_mordio, no_reprod, faltan, invisibles, _malas):
    """LA CONDICION DEL ROJO TAL COMO ESTABA ANTES DE LA VUELTA 180, reproducida
    aqui para la mutacion del caso (D). NO mira la pieza del sujeto congelado.
    Se conserva escrita y no se borra: es lo que esta tarea vino a cambiar."""
    return bool(perdidas or no_mordio or no_reprod or faltan or invisibles)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    fallos = []
    carpeta = tempfile.mkdtemp(prefix="v180_t2c_")

    def marcar(etiqueta, ok):
        p("   %-70s %s" % (etiqueta, "SI" if ok else "NO"))
        if not ok:
            fallos.append(etiqueta)

    try:
        p("=" * 78)
        p("CASO POSITIVO POR MUTACION DEL CABLEADO DE LA GUARDA (vuelta 180, 2.c)")
        p("=" * 78)
        p("")

        nombre = "vuelta999_tarea1_mutacion_de_mentira.py"
        ruta = os.path.join(carpeta, nombre)
        nomina = [(nombre, False)]

        p("(A) LA GUARDA, SOBRE UN DIRECTORIO Y UNA NOMINA FABRICADOS")
        p("   directorio de mentira: %s" % carpeta)
        p("   nomina de mentira: %s" % [n for n, _a in nomina])
        escribir(ruta, ARNES_SIN_DECLARAR)
        malas = V.guarda_del_sujeto_congelado(nomina=nomina, directorio=carpeta)
        p("   A1, sin declarar -> la guarda senala %d entrada(s): %s"
          % (len(malas), ", ".join("%s (%s)" % (n, v) for n, v, _vv in malas) or "ninguna"))
        marcar("A1: un arnes que abre un fichero vivo y no lo declara SALE senalado",
               len(malas) == 1)

        escribir(ruta, ARNES_SIN_DECLARAR.replace(
            'r"""arnes de mentira: abre un fichero vivo y no lo declara."""',
            LINEA_DECLARADA))
        malas_declarado = V.guarda_del_sujeto_congelado(nomina=nomina, directorio=carpeta)
        p("   A2, ya declarado -> la guarda senala %d entrada(s)" % len(malas_declarado))
        marcar("A2: el MISMO arnes, con la linea de declaracion, DEJA de salir",
               len(malas_declarado) == 0)
        p("")

        p("(B) hay_rojo_al_cierre() CON LAS SEIS PIEZAS VACIAS")
        b = V.hay_rojo_al_cierre([], [], [], [], [], [])
        p("   devuelve: %r" % b)
        marcar("B: sin ninguna pieza llena NO hay rojo", b is False)
        p("")

        p("(C) hay_rojo_al_cierre() CON SOLO LA PIEZA DEL SUJETO CONGELADO LLENA")
        pieza = [("vuelta999_tarea1_mutacion_de_mentira.py", "SUJETO VIVO", ["REPORTE.md"])]
        c = V.hay_rojo_al_cierre([], [], [], [], [], pieza)
        p("   pieza: %r" % (pieza,))
        p("   devuelve: %r" % c)
        marcar("C: la pieza del sujeto congelado SOLA enciende el rojo", c is True)
        p("")

        p("(D) LA MUTACION: LA CONDICION VIEJA, LA DE ANTES DE ESTA VUELTA")
        d = condicion_vieja([], [], [], [], [], pieza)
        p("   sobre el MISMO escenario del caso (C), devuelve: %r" % d)
        marcar("D: con la pieza desenchufada el rojo NO se enciende, o sea que CAE",
               d is False)
        p("")

        p("(E) LAS OTRAS CINCO PIEZAS SIGUEN ENCENDIENDO EL ROJO, UNA POR UNA")
        for i, etiqueta in enumerate(("ANCLA PERDIDA", "NO MORDIO", "NO REPRODUCIBLE",
                                      "FUERA DE LA NOMINA", "INVISIBLE AL CENSO")):
            piezas = [[], [], [], [], [], []]
            piezas[i] = ["algo"]
            r = V.hay_rojo_al_cierre(*piezas)
            marcar("E: la pieza %-20s sola enciende el rojo -> %r" % (etiqueta, r),
                   r is True)
        p("")
    finally:
        shutil.rmtree(carpeta, ignore_errors=True)
        p("EL TEMPORAL, RETIRADO (P.16): existe todavia: %s"
          % ("SI" if os.path.exists(carpeta) else "NO"))
        p("")

    p("CIFRA comprobaciones: 10 | fallan: %d" % len(fallos))
    if fallos:
        p("ROJO: %d comprobacion(es) no se comportan." % len(fallos))
        for f in fallos:
            p("   " + f)
        p("FIN")
        return 1
    p("VERDE: la guarda del sujeto congelado esta ENCHUFADA al rojo global y se "
      "demuestra por mutacion, no por afirmacion: su pieza sola enciende el rojo, "
      "la condicion vieja sobre el mismo escenario NO lo enciende, y las otras "
      "cinco piezas siguen encendiendolo cada una por su cuenta.")
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
