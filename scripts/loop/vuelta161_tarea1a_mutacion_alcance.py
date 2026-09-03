# -*- coding: utf-8 -*-
"""vuelta161_tarea1a_mutacion_alcance.py . TAREA 1.a DE LA VUELTA 161, EL CASO
ROJO POR MUTACION DE LA VARA DE CONTENIDO.

POR QUE EXISTE, CON SU REGLA DELANTE. `EJECUTOR.md` 1, "EL CASO ROJO SE PRUEBA
POR MUTACION" (29 ago 2026): ningun assert ni guarda se publica como prueba sin
haber corrido antes su prueba de mutacion; se cambia el valor esperado y se
comprueba que el caso CAE. Y la caida que la escribio es exactamente la de un
veredicto que era una CONSTANTE LITERAL comparada consigo misma.

POR ESO AQUI SE MUTA SOBRE VARIABLE COMPUTADA Y NO SOBRE UN LITERAL: la decision
vive en `clasificar(texto)`, que es PURA (recibe el TEXTO del fichero, no su ruta
ni su nombre, y no toca el disco). Se le da el texto REAL leido de git y COPIAS
MUTADAS EN MEMORIA de ese mismo texto, y se comprueba que el veredicto se mueve
en la direccion que toca.

LOS CINCO CASOS:

  CASO 1, VERDE DE CONTROL. El texto real de uno de los doce clasifica ALCANCE,
  y el de un buscador clasifica SOLO_CITA. Sin esto, los cuatro rojos de abajo
  no distinguirian una vara que funciona de una que dice ALCANCE a todo.

  CASO 2, ROJO: SE LE QUITA LA MARCA DEL COMENTARIO A UNO DE LOS DOCE. Tiene que
  dejar de ser ALCANCE y caer a SOLO_CITA, y la cuenta del directorio tiene que
  bajar a ONCE.

  CASO 3, ROJO: SE LE PONE LA MARCA EN UN COMENTARIO A UNO QUE NO LA TIENE
  (`vuelta160_tarea3b_caso_positivo.py`). Tiene que subir a ALCANCE y la cuenta
  a TRECE. Este es el caso que prueba que la vara NO esta mirando el nombre: el
  fichero se llama igual antes y despues.

  CASO 4, ROJO: LA MARCA SE MUEVE DEL COMENTARIO A UNA CONSTANTE DE CADENA. Tiene
  que caer a ESCRIBE_EL_REMEDIO. Es la distincion entera de la vara (el que la
  LLEVA contra el que la ESCRIBE EN OTROS) puesta a prueba.

  CASO 5, MUTACION DEL VALOR ESPERADO. Con la cuenta real de hoy, se cambia
  ESPERADO_FICHEROS de 12 a 13 y se comprueba que el cotejo CAE. Sin este caso,
  el cotejo del instrumento podria estar comparando algo consigo mismo.

LOS FICHEROS REALES NO SE TOCAN, Y NO SE PROMETE: se toma el sha256 de los tres
ficheros implicados ANTES y DESPUES de la corrida y se publican los seis.

USO:  python scripts/loop/vuelta161_tarea1a_mutacion_alcance.py
"""
import hashlib
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
sys.path.insert(0, LOOP)

import vuelta159_tarea5_alcance_p16 as A  # noqa: E402

UNO_DE_LOS_DOCE = "vuelta89_tarea4_guarda_op_c05.py"
EL_QUE_NO_LA_TIENE = "vuelta160_tarea3b_caso_positivo.py"
EL_QUE_LA_ESCRIBE = "vuelta160_tarea3_remedio_p16.py"


def leer(nombre):
    return io.open(os.path.join(LOOP, nombre), encoding="utf-8").read()


def sha(nombre):
    with open(os.path.join(LOOP, nombre), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def cuenta(textos):
    """CIFRA de ficheros en la clase ALCANCE sobre un diccionario {nombre:
    texto}. Variable computada: no hay ninguna cifra escrita a mano aqui."""
    return len([n for n, t in textos.items() if A.clasificar(t) == "ALCANCE"])


def textos_del_directorio():
    fuera = {}
    for nombre in sorted(os.listdir(LOOP)):
        if not nombre.endswith(".py"):
            continue
        try:
            fuera[nombre] = leer(nombre)
        except (IOError, UnicodeDecodeError):
            continue
    return fuera


def quitar_marca_del_comentario(texto):
    """Mutacion 2: borra la marca alli donde vive en un COMENTARIO REAL, y solo
    ahi. Devuelve (texto_mutado, cuantas veces se quito)."""
    salida = []
    quitadas = 0
    for linea in texto.split("\n"):
        pelada = linea.lstrip()
        if pelada.startswith("#") and A.MARCA_DEL_REMEDIO in linea:
            salida.append(linea.replace(A.MARCA_DEL_REMEDIO, "BLOQUE SIN MARCA"))
            quitadas += 1
        else:
            salida.append(linea)
    return "\n".join(salida), quitadas


def poner_marca_en_comentario(texto):
    """Mutacion 3: anade una linea de comentario con la marca al final."""
    return texto + "\n# --- %s, TAREA 3.a) ---\n" % A.MARCA_DEL_REMEDIO


def mover_marca_a_una_cadena(texto):
    """Mutacion 4: sobre el texto ya mutado por la 2 (sin marca en comentario),
    mete la marca dentro de una constante de cadena."""
    return texto + '\nMARCA_QUE_ESCRIBO = "%s, TAREA 3.a) ---"\n' % A.MARCA_DEL_REMEDIO


def main():
    print("=" * 78)
    print("VUELTA 161, TAREA 1.a: CASO ROJO POR MUTACION DE LA VARA DE CONTENIDO")
    print("=" * 78)
    print("")

    implicados = [UNO_DE_LOS_DOCE, EL_QUE_NO_LA_TIENE, EL_QUE_LA_ESCRIBE]
    antes = dict((n, sha(n)) for n in implicados)
    print("SHA256 DE LOS TRES FICHEROS REALES, ANTES:")
    for n in implicados:
        print("   %-46s %s" % (n, antes[n]))
    print("")

    textos = textos_del_directorio()
    resultados = []

    # CASO 1
    c_doce = A.clasificar(textos[UNO_DE_LOS_DOCE])
    c_busc = A.clasificar(textos["vuelta160_tarea1_registrar_adjudicaciones.py"])
    n_real = cuenta(textos)
    print("CASO 1, VERDE DE CONTROL")
    print("   clasificar(%s) = %s" % (UNO_DE_LOS_DOCE, c_doce))
    print("   clasificar(vuelta160_tarea1_registrar_adjudicaciones.py) = %s" % c_busc)
    print("   CIFRA en la clase ALCANCE, sin mutar nada: %d" % n_real)
    ok1 = (c_doce == "ALCANCE" and c_busc == "SOLO_CITA"
           and n_real == A.ESPERADO_FICHEROS)
    print("   VERDE: %s" % ok1)
    resultados.append(("CASO 1, verde de control", ok1))
    print("")

    # CASO 2
    mut2, quitadas = quitar_marca_del_comentario(textos[UNO_DE_LOS_DOCE])
    t2 = dict(textos)
    t2[UNO_DE_LOS_DOCE] = mut2
    c2 = A.clasificar(mut2)
    n2 = cuenta(t2)
    print("CASO 2, ROJO: se le quita la marca del comentario a uno de los doce")
    print("   CIFRA comentarios con la marca que se le quitaron: %d" % quitadas)
    print("   clasificar(mutado) = %s   (antes: %s)" % (c2, c_doce))
    print("   CIFRA en la clase ALCANCE con la mutacion puesta: %d (antes %d)"
          % (n2, n_real))
    ok2 = quitadas > 0 and c2 == "SOLO_CITA" and n2 == n_real - 1
    print("   EL CASO CAE COMO TIENE QUE CAER: %s" % ok2)
    resultados.append(("CASO 2, quitar la marca del comentario", ok2))
    print("")

    # CASO 3
    mut3 = poner_marca_en_comentario(textos[EL_QUE_NO_LA_TIENE])
    t3 = dict(textos)
    t3[EL_QUE_NO_LA_TIENE] = mut3
    c3_antes = A.clasificar(textos[EL_QUE_NO_LA_TIENE])
    c3 = A.clasificar(mut3)
    n3 = cuenta(t3)
    print("CASO 3, ROJO: se le pone la marca en un comentario a uno que no la tiene")
    print("   fichero: %s (el nombre no cambia)" % EL_QUE_NO_LA_TIENE)
    print("   clasificar(real) = %s ; clasificar(mutado) = %s" % (c3_antes, c3))
    print("   CIFRA en la clase ALCANCE con la mutacion puesta: %d (antes %d)"
          % (n3, n_real))
    ok3 = c3_antes == "SOLO_CITA" and c3 == "ALCANCE" and n3 == n_real + 1
    print("   EL CASO CAE COMO TIENE QUE CAER: %s" % ok3)
    resultados.append(("CASO 3, poner la marca en un comentario", ok3))
    print("")

    # CASO 4
    mut4 = mover_marca_a_una_cadena(mut2)
    c4 = A.clasificar(mut4)
    print("CASO 4, ROJO: la marca se mueve del comentario a una constante de cadena")
    print("   clasificar(mutado) = %s   (esperado ESCRIBE_EL_REMEDIO)" % c4)
    ok4 = c4 == "ESCRIBE_EL_REMEDIO"
    print("   EL CASO CAE COMO TIENE QUE CAER: %s" % ok4)
    resultados.append(("CASO 4, mover la marca a una cadena", ok4))
    print("")

    # CASO 5
    esperado_mutado = A.ESPERADO_FICHEROS + 1
    cotejo_real = (n_real == A.ESPERADO_FICHEROS)
    cotejo_mutado = (n_real == esperado_mutado)
    print("CASO 5, MUTACION DEL VALOR ESPERADO")
    print("   ESPERADO_FICHEROS real: %d ; mutado: %d" % (A.ESPERADO_FICHEROS,
                                                          esperado_mutado))
    print("   cotejo con el esperado real:   %s" % cotejo_real)
    print("   cotejo con el esperado mutado: %s" % cotejo_mutado)
    ok5 = cotejo_real and not cotejo_mutado
    print("   EL COTEJO CAE AL MUTAR EL VALOR ESPERADO: %s" % ok5)
    resultados.append(("CASO 5, mutacion del valor esperado", ok5))
    print("")

    despues = dict((n, sha(n)) for n in implicados)
    print("SHA256 DE LOS TRES FICHEROS REALES, DESPUES:")
    intactos = True
    for n in implicados:
        igual = antes[n] == despues[n]
        intactos = intactos and igual
        print("   %-46s %s  intacto=%s" % (n, despues[n], igual))
    resultados.append(("LOS TRES FICHEROS REALES QUEDAN INTACTOS", intactos))
    print("")

    print("RESUMEN")
    for nombre, ok in resultados:
        print("   %-46s %s" % (nombre, "VERDE" if ok else "ROJO"))
    todos = all(ok for _n, ok in resultados)
    print("")
    print("CIFRA casos: %d" % len(resultados))
    print("CIFRA en verde: %d" % len([1 for _n, ok in resultados if ok]))
    print("VEREDICTO: %s" % ("VERDE" if todos else "ROJO"))
    print("FIN")
    return 0 if todos else 1


if __name__ == "__main__":
    raise SystemExit(main())
