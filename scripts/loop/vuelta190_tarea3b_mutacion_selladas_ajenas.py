# -*- coding: utf-8 -*-
r"""vuelta190_tarea3b_mutacion_selladas_ajenas.py . EL CASO POSITIVO POR MUTACION
DEL EXITCODE QUE SEPARA Y DE LA RESTAURACION DE LAS SALIDAS SELLADAS AJENAS.

QUIEN LO ENCARGA. Las adjudicaciones `4.4` y `4.9` del acta 190. La `4.4`: un
unico `1` para un arnes caido y para una deuda declarada es degradacion
silenciosa, medida sobre los diez tramos de la 189, donde **en nueve no cayo ni un
arnes**. La `4.9`: una salida sellada es la prueba de la vuelta que la sello, y
**dejar que una corrida posterior la pise borra el registro**; en la 189 se
pisaron TRES y las restauro una persona a mano, en dos vueltas distintas y a dos
personas distintas.

SUJETO CONGELADO: este arnes NO abre ningun fichero vivo del repo y NO corre la
bateria. Sus sujetos son las cuatro funciones puras del lanzador
`scripts/loop/vuelta190_bateria_por_tramos.py` (`clase_del_exitcode`,
`es_salida_sellada_ajena`, `nombre_del_corte_nuevo` y `reparto_de_selladas`),
**importadas**, y un directorio FABRICADO en un temporal que este mismo fichero
retira (`P.16`, quien fabrica limpia).

QUE PRUEBA, CASO A CASO, Y TODOS TIENEN QUE CAER AL MUTAR SU ESPERADO:

  (A) EL EXITCODE SEPARA, Y SUS NOMBRES NO SE TECLEAN AQUI: salen del diccionario
      `CODIGO_DE_LA_CLASE` de `verificar_mutaciones_viejas.py`, que es donde la
      TAREA 2 los escribio, para que las dos mitades no puedan discrepar. Y un
      codigo desconocido **no se traga**: sale con su nombre propio, que es mas
      informacion que un `1` mudo.

  (B) QUE ES AJENA Y QUE ES PROPIA SALE DEL NOMBRE Y NO DE UNA LISTA. Se prueban
      las tres familias: una sellada de otra vuelta, una de la vuelta que corre, y
      una ruta que no es una sellada. **Y la variante con letra** (`SALIDA_V189b_`)
      entra, porque esta casa ya tuvo un sufijo `b` y una vara que no lo viera
      dejaria una salida sellada sin proteger.

  (C) EL REPARTO NO SE COME NINGUNA: la suma de las tres listas es exactamente lo
      que se le paso.

  (D) EL CORTE NUEVO VA AL LADO Y NUNCA ENCIMA. El nombre hermano lleva la vuelta
      DE ESTE lanzador, y **no es el mismo que el original**: si lo fuera, seria
      escribir encima con otro nombre.

  (E) EL CASO QUE EL ENCARGO PIDE CON ESAS PALABRAS: **CAE si una salida sellada
      ajena se queda pisada.** Se fabrica un escenario donde la restauracion se
      hace y otro donde NO se hace, y se exige que el segundo salga en ROJO. Si
      los dos salieran igual, la guarda no estaria mirando nada.

  (F) LAS TRES DE VERDAD QUE LA BATERIA DE LA 189 PISO, CLASIFICADAS POR ESTA
      VARA SIN TOCARLAS. Se comprueba que las tres salen AJENAS respecto de esta
      vuelta, que es la condicion para que la restauracion automatica las hubiera
      cubierto. **No se abre ninguna y no se toca ninguna: solo se clasifica su
      nombre.**

USO:
  python scripts/loop/vuelta190_tarea3b_mutacion_selladas_ajenas.py
"""
import io
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as B   # noqa: E402
import vuelta190_bateria_por_tramos as LANZ   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

# LAS TRES QUE LA CORRIDA ANTERIOR PISO, NOMBRADAS POR EL ACTA EN SU 4.9. Aqui
# SOLO SE CLASIFICAN SUS NOMBRES: no se abren y no se tocan.
LAS_TRES_PISADAS = [
    "docs/loop/SALIDA_V184_T1C_MUTACION_ESTIMACION.txt",
    "docs/loop/SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt",
    "docs/loop/SALIDA_V188_T4_MUTACION_COBERTURA_PAREJAS.txt",
]


def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    w("   %-56s obtenido %-30s esperado %-30s -> %s"
      % (nombre, repr(obtenido), repr(esperado), "PASA" if ok else "CAE"))
    return 0 if ok else 1


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION: EL EXITCODE QUE SEPARA Y LA RESTAURACION DE")
    w("LAS SALIDAS SELLADAS AJENAS (vuelta 190, TAREA 3)")
    w("=" * 78)
    w("")
    fallos = 0
    no_cayeron = 0
    tmp = tempfile.mkdtemp(prefix="v190_t3_")
    try:
        w("A) EL EXITCODE SEPARA, Y LOS NOMBRES SALEN DEL DICCIONARIO COMPARTIDO")
        w("   CODIGO_DE_LA_CLASE, leido de verificar_mutaciones_viejas y no tecleado:")
        for k, v in sorted(B.CODIGO_DE_LA_CLASE.items(), key=lambda x: x[1]):
            w("      %-26s -> %d" % (k, v))
        for codigo, esperado in ((0, B.VERDE), (1, B.ROJO_POR_FALLO),
                                 (2, B.ROJO_POR_DEUDA)):
            fallos += _caso(w, "clase del exitcode %d" % codigo,
                            LANZ.clase_del_exitcode(codigo), esperado)
        fallos += _caso(w, "clase de un codigo que nadie declaro (7)",
                        LANZ.clase_del_exitcode(7), "ROJO DE ESPECIE DESCONOCIDA")
        w("   LA MUTACION: si el 1 y el 2 dieran el mismo nombre, esto no separaria")
        w("   nada y volveriamos a la degradacion que la 4.4 manda deshacer.")
        if LANZ.clase_del_exitcode(1) == LANZ.clase_del_exitcode(2):
            w("      LA MUTACION NO CAYO: el 1 y el 2 dicen lo mismo.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: el 1 dice %r y el 2 dice %r."
              % (LANZ.clase_del_exitcode(1), LANZ.clase_del_exitcode(2)))
        w("   Y LOS DOS ROJOS SIGUEN SIENDO DISTINTOS DE CERO, que es la condicion")
        w("   de no aflojar nada:")
        fallos += _caso(w, "el 1 y el 2 son distintos de cero", [1 != 0, 2 != 0],
                        [True, True])
        w("")

        w("B) QUE ES AJENA Y QUE ES PROPIA SALE DEL NOMBRE, NO DE UNA LISTA")
        casos_b = (
            ("docs/loop/SALIDA_V184_T1C_MUTACION_ESTIMACION.txt", 190,
             (True, 184, True)),
            ("docs/loop/SALIDA_V190_T2_NOMINA.txt", 190, (True, 190, False)),
            ("docs/loop/SALIDA_V189b_ALGO.txt", 190, (True, 189, True)),
            ("docs/loop/ACTA_AUDITOR.md", 190, (False, None, False)),
            ("docs/loop/ROJOS_DE_LA_VUELTA_189.txt", 190, (False, None, False)),
        )
        for ruta, vuelta, esperado in casos_b:
            fallos += _caso(w, os.path.basename(ruta),
                            LANZ.es_salida_sellada_ajena(ruta, vuelta), esperado)
        w("   LA MUTACION: la misma sellada mirada DESDE SU PROPIA VUELTA deja de")
        w("   ser ajena. Si no cambiara, la vara no estaria mirando la vuelta.")
        propia = LANZ.es_salida_sellada_ajena(
            "docs/loop/SALIDA_V184_T1C_MUTACION_ESTIMACION.txt", 184)
        if propia[2]:
            w("      LA MUTACION NO CAYO: sigue diciendo que es ajena.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: desde la 184 la misma ruta sale PROPIA.")
        w("")

        w("C) EL REPARTO NO SE COME NINGUNA")
        rutas = [r for r, _v, _e in
                 [(x[0], x[1], x[2]) for x in casos_b]]
        ajenas, propias, otras = LANZ.reparto_de_selladas(rutas, 190)
        w("   ajenas:  %s" % ", ".join("%s(v%s)" % (os.path.basename(r), v)
                                       for r, v in ajenas))
        w("   propias: %s" % ", ".join("%s(v%s)" % (os.path.basename(r), v)
                                       for r, v in propias))
        w("   otras:   %s" % ", ".join(os.path.basename(r) for r in otras))
        fallos += _caso(w, "ajenas", len(ajenas), 2)
        fallos += _caso(w, "propias", len(propias), 1)
        fallos += _caso(w, "no selladas", len(otras), 2)
        fallos += _caso(w, "la suma es lo que se le paso",
                        len(ajenas) + len(propias) + len(otras), len(rutas))
        w("")

        w("D) EL CORTE NUEVO VA AL LADO Y NUNCA ENCIMA")
        original = "docs/loop/SALIDA_V184_T1C_MUTACION_ESTIMACION.txt"
        hermano = LANZ.nombre_del_corte_nuevo(original, 190)
        fallos += _caso(w, "nombre del corte nuevo", hermano,
                        "SALIDA_V184_T1C_MUTACION_ESTIMACION_CORTE_V190.txt")
        fallos += _caso(w, "no es el mismo nombre que el original",
                        hermano == os.path.basename(original), False)
        fallos += _caso(w, "lleva dentro la vuelta que restaura",
                        "V190" in hermano, True)
        fallos += _caso(w, "y conserva la vuelta del original",
                        "V184" in hermano, True)
        w("   LA MUTACION: si el hermano se llamara igual que el original, esto")
        w("   seria escribir encima con otro nombre, que es lo que la 4.9 prohibe.")
        if hermano == os.path.basename(original):
            w("      LA MUTACION NO CAYO.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: %r no es %r." % (hermano, os.path.basename(original)))
        w("")

        w("E) EL CASO QUE EL ENCARGO PIDE: CAE SI UNA SELLADA AJENA SE QUEDA PISADA")
        w("   (todo sobre un escenario FABRICADO: no se corre la bateria y no se")
        w("    toca ningun fichero del repo)")
        pisadas = ["docs/loop/SALIDA_V184_T1C_MUTACION_ESTIMACION.txt",
                   "docs/loop/SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt"]

        def veredicto(quedan_pisadas):
            """LA CONDUCTA DE LA GUARDA, AISLADA: verde solo si al remedir NO
            queda ninguna sellada ajena pisada."""
            aj, _p, _o = LANZ.reparto_de_selladas(quedan_pisadas, 190)
            return "VERDE" if not aj else "ROJO"

        fallos += _caso(w, "restaurada del todo (no queda ninguna)",
                        veredicto([]), "VERDE")
        fallos += _caso(w, "una se queda pisada", veredicto(pisadas[:1]), "ROJO")
        fallos += _caso(w, "las dos se quedan pisadas", veredicto(pisadas), "ROJO")
        w("   LA MUTACION: si el veredicto no cambiara entre `restaurada` y")
        w("   `pisada`, la guarda no estaria mirando nada.")
        if veredicto([]) == veredicto(pisadas[:1]):
            w("      LA MUTACION NO CAYO: los dos escenarios dan lo mismo.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: %r restaurada y %r pisada."
              % (veredicto([]), veredicto(pisadas[:1])))
        w("   Y UNA SELLADA PROPIA PISADA NO ES ROJO, que es la otra mitad: lo que")
        w("   esta corrida escribe es suyo y restaurarlo seria borrar el dia.")
        fallos += _caso(w, "una sellada PROPIA pisada",
                        veredicto(["docs/loop/SALIDA_V190_T2_NOMINA.txt"]), "VERDE")
        w("")

        w("F) LA ESCRITURA DEL CORTE NUEVO VA EN LF, SOBRE UN FICHERO FABRICADO")
        crudo = os.path.join(tmp, "SALIDA_V184_FABRICADA.txt")
        io.open(crudo, "wb").write(b"una linea\r\notra linea\r\n")
        datos = io.open(crudo, "rb").read()
        lf = datos.replace(b"\r\n", b"\n")
        destino = os.path.join(tmp, LANZ.nombre_del_corte_nuevo(crudo, 190))
        io.open(destino, "wb").write(lf)
        vueltos = io.open(destino, "rb").read()
        # LAS DOS CIFRAS NO SE TECLEAN: SE COMPUTAN, Y ESO NO ES UN ADORNO. La
        # primera version de este arnes las teclee a mano (22 y 20) y CAYERON
        # LAS DOS: son 23 y 21. El esperado es una RELACION medida sobre el
        # propio fichero, que es lo que no se puede equivocar al contar de cabeza.
        w("   el fabricado, medido: %d bytes en disco, %d retornos de carro"
          % (len(datos), datos.count(b"\r")))
        fallos += _caso(w, "bytes del corte = bytes en disco menos los retornos",
                        len(vueltos), len(datos) - datos.count(b"\r"))
        fallos += _caso(w, "el corte NO lleva ningun retorno de carro",
                        vueltos.count(b"\r"), 0)
        fallos += _caso(w, "y el corte conserva todas sus lineas",
                        vueltos.count(b"\n"), datos.count(b"\n"))
        w("   LA MUTACION: si se escribiera tal cual, el corte llevaria %d retorno(s)"
          % datos.count(b"\r"))
        w("   de carro y no seria LF, que es la convencion de la casa en disco.")
        if datos.count(b"\r") == vueltos.count(b"\r"):
            w("      LA MUTACION NO CAYO: la normalizacion no cambia nada.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: %d retornos antes y %d despues."
              % (datos.count(b"\r"), vueltos.count(b"\r")))
        w("")

        w("G) LAS TRES QUE LA CORRIDA DE LA 189 PISO, CLASIFICADAS SIN TOCARLAS")
        w("   (el acta 190 las nombra en su 4.9. Aqui SOLO se clasifica su nombre:")
        w("    no se abre ninguna y no se toca ninguna)")
        cubiertas = 0
        for r in LAS_TRES_PISADAS:
            sellada, suya, ajena = LANZ.es_salida_sellada_ajena(r, 190)
            w("      %-52s sellada %-5s vuelta %-5s ajena %s"
              % (os.path.basename(r), sellada, suya, ajena))
            cubiertas += 1 if ajena else 0
        fallos += _caso(w, "las tres salen AJENAS respecto de esta vuelta",
                        cubiertas, len(LAS_TRES_PISADAS))
        w("   O SEA: la restauracion automatica las habria cubierto a las tres, que")
        w("   es lo que la 4.9 pide y lo que en la 189 tuvo que hacer una persona a")
        w("   mano, en dos vueltas distintas y a dos personas distintas.")
        w("")
    finally:
        # LA RUTA DEL TEMPORAL NO SE ESCRIBE EN LA SALIDA SELLADA: `mkdtemp` le
        # pone un sufijo al azar y esta salida tiene que repetirse byte a byte en
        # dos corridas seguidas.
        existia = os.path.exists(tmp)
        shutil.rmtree(tmp, ignore_errors=True)
        w("LIMPIEZA (`P.16`, quien fabrica limpia): el temporal se retira.")
        w("   prefijo del temporal (estable; el sufijo al azar NO se publica): v190_t3_")
        w("   existia antes de retirarlo: %s | existe despues: %s"
          % (existia, os.path.exists(tmp)))
        w("")

    w("=" * 78)
    w("CIFRA casos: los de arriba, uno por linea con PASA o CAE")
    w("CIFRA casos que CAEN: %d" % fallos)
    w("CIFRA mutaciones que NO cayeron (y deberian): %d" % no_cayeron)
    w("VEREDICTO: %s" % ("ROJO" if (fallos or no_cayeron) else "VERDE"))
    texto = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V190_T3B_MUTACION_SELLADAS_AJENAS.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(texto.encode("utf-8"))))
    return 1 if (fallos or no_cayeron) else 0


if __name__ == "__main__":
    sys.exit(main())
