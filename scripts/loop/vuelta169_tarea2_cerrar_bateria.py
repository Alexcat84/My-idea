# -*- coding: utf-8 -*-
r"""vuelta169_tarea2_cerrar_bateria.py . LOS DOS ROJOS QUE ESTA VUELTA SE CAUSO
A SI MISMA, Y NO SE ARREGLAN AFLOJANDO NADA (TAREA 2 de la vuelta 169).

QUE PASO, MEDIDO Y NO SUPUESTO. La segunda corrida de la bateria salio con el
rojo del retrato APAGADO (la TAREA 2 lo re anclo y funciono) y con DOS rojos
nuevos mas un aviso, y LOS TRES son consecuencia de escrituras de ESTA MISMA
VUELTA:

  (1) `CIFRA arneses POSTERIORES a la nomina que se quedan FUERA: 1`, y el que
      esta fuera es `vuelta169_tarea2_mutacion_reanclaje.py`, el arnes que la
      TAREA 2 acaba de escribir.
  (2) `vuelta163_tarea2_mutacion_nomina.py`, `NO MORDIO`. Ese arnes existe
      EXACTAMENTE para morder cuando (1) pasa. **Esta haciendo su trabajo**, y
      apagarlo seria lo contrario de arreglarlo: se arregla metiendo el arnes
      nuevo en la nomina, que es lo que la regla escrita en la propia bateria
      manda.
  (3) `vuelta165_tarea6_mutacion_op_l_01.py`, `NO MORDIO`. Ese arnes ancla por
      IGUALDAD EXACTA el numero de clausulas de `OP-L-01`, y la TAREA 4 de esta
      vuelta le anadio la sexta por el carril del 9.10. **Tambien esta haciendo
      su trabajo**: su comentario dice, literal, *"vuelve a caer en rojo en
      cuanto alguien anada o quite una clausula sin declararlo"*.

POR QUE ESTO NO ES AFLOJAR, Y LA DIFERENCIA IMPORTA. La vuelta 168 hizo bien en
TRAER el tercer rojo sin tocarlo, porque lo habia causado OTRA vuelta y el
encargo no lo nombraba. **Estos dos los causo ESTA sesion, hace minutos, con
escrituras suyas.** Dejarlos seria dejar mi propio escombro y publicar una
bateria rota que rompi yo. La vara es la misma que la casa uso en el 3.b de la
168 y en la 6.2 de esta: **EL NUMERO CAMBIA, EL FILO NO.**

  Para (1) y (2): el arnes nuevo entra en `VIEJAS`. La coletilla de la vuelta
  145, con la letra que la 148 le puso, dice que la condicion de entrada es
  **SUJETO CONGELADO** y que el plazo de una vuelta era el medio y no el fin.
  El sujeto de `vuelta169_tarea2_mutacion_reanclaje.py` son celdas fabricadas
  EN MEMORIA y el fichero del arnes hermano, ya commiteado: congelado. Y la
  propia bateria lo reclama diciendo *"no mas tarde"*.

  Para (3): el ancla pasa de CINCO a SEIS clausulas y de DOS a TRES correcciones
  declaradas, las dos cifras **por igualdad exacta contra el conteo real**, y el
  invariante de que las tres viejas siguen enteras **no se toca**. Vuelve a caer
  el dia que alguien anada o quite una clausula sin declararlo.

NO SE TOCA NADA MAS. Ni un caso se quita, ni una comprobacion se afloja, ni se
mete ningun arnes en `CASOS_DECLARADOS`.

USO:
  python scripts/loop/vuelta169_tarea2_cerrar_bateria.py
  python scripts/loop/vuelta169_tarea2_cerrar_bateria.py --comprobar
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BATERIA = os.path.join(RAIZ, "scripts", "loop", "verificar_mutaciones_viejas.py")
ARNES_165 = os.path.join(RAIZ, "scripts", "loop", "vuelta165_tarea6_mutacion_op_l_01.py")
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

ANCLA_VIEJAS = '    ("vuelta168_tarea4_mutacion_op_v_01.py", False),\n'
NUEVO_VIEJAS = (
    '    ("vuelta168_tarea4_mutacion_op_v_01.py", False),\n'
    '    # ANADIDO EN LA VUELTA 169 (TAREA 2). Su sujeto son celdas FABRICADAS EN\n'
    '    # MEMORIA y el fichero del arnes hermano ya commiteado: CONGELADO, que es la\n'
    '    # condicion de entrada desde la letra de la vuelta 148. La propia guarda de\n'
    '    # abajo lo reclamo en la corrida 2 de esta vuelta, con estas palabras: "1\n'
    '    # arnes(es) de mutacion nacidos despues de la vuelta 168 se quedan FUERA".\n'
    '    ("vuelta169_tarea2_mutacion_reanclaje.py", False),\n')

CAMBIOS_165 = [
    (
        '    casos.append(("C_tiene_cinco_clausulas", len(d.get("verificacion") or []), 5))\n',
        '    # RE ANCLADO OTRA VEZ EN LA VUELTA 169 (TAREA 2), Y EL MOTIVO NO SE BORRA:\n'
        '    # este caso esperaba CINCO clausulas y hoy la ficha trae SEIS. La TAREA 4 de\n'
        '    # la vuelta 169 anadio la sexta POR ADICION, por el carril del banco 9.10 y\n'
        '    # con el texto viejo entero encima, ejecutando la clausula 3 por la\n'
        '    # adjudicacion 6.5 del acta 168. ES LA MISMA ESPECIE QUE EL RE ANCLAJE DE LA\n'
        '    # VUELTA 168, Y LA DIFERENCIA SE DICE: aquella caida tardo dos vueltas en\n'
        '    # verse porque la bateria no se corrio; esta se vio EN LA MISMA SESION que la\n'
        '    # causo, corriendo la bateria despues de escribir. EL CASO NO SE AFLOJA:\n'
        '    # sigue siendo una IGUALDAD EXACTA contra el conteo real de la ficha.\n'
        '    casos.append(("C_tiene_seis_clausulas", len(d.get("verificacion") or []), 6))\n',
        "el ancla del numero de clausulas, de 5 a 6",
    ),
    (
        '    casos.append(("C_dos_de_las_cinco_son_correccion_declarada", len(declaradas), 2))\n',
        '    # MISMO RE ANCLAJE (vuelta 169): la sexta clausula tambien es una CORRECCION\n'
        '    # DECLARADA, asi que este invariante pasa de DOS a TRES. Sigue siendo el\n'
        '    # invariante que el numero solo no da: si alguien reescribiera la ficha\n'
        '    # borrando el texto viejo en vez de anadir, este caso caeria aunque el\n'
        '    # conteo siguiera dando seis.\n'
        '    casos.append(("C_tres_de_las_seis_son_correccion_declarada", len(declaradas), 3))\n',
        "el ancla de las correcciones declaradas, de 2 a 3",
    ),
]


def main():
    solo_medir = "--comprobar" in sys.argv
    print("=" * 78)
    print("VUELTA 169, TAREA 2: LOS DOS ROJOS QUE ESTA VUELTA SE CAUSO A SI MISMA")
    print("=" * 78)
    print("")

    print("A) LA CIFRA REAL DE LA FICHA, LEIDA HOY Y NO SUPUESTA")
    fichas = [json.loads(l) for l in io.open(OPERACIONES, encoding="utf-8") if l.strip()]
    f = [x for x in fichas if x.get("id_op") == "OP-L-01"]
    if len(f) != 1:
        print("   ROJO: OP-L-01 aparece %d veces." % len(f))
        return 1
    ver = f[0].get("verificacion") or []
    decl = [c for c in ver if c.startswith("CORRECCION DECLARADA")]
    viejas = [c for c in ver if not c.startswith("CORRECCION DECLARADA")]
    print("   CIFRA clausulas de OP-L-01 hoy: %d" % len(ver))
    print("   CIFRA que son CORRECCION DECLARADA: %d" % len(decl))
    print("   CIFRA viejas que siguen enteras: %d" % len(viejas))
    if (len(ver), len(decl), len(viejas)) != (6, 3, 3):
        print("   ROJO: la ficha no trae 6 clausulas con 3 declaradas y 3 viejas.")
        print("   El re anclaje se escribiria contra una cifra que no es la real.")
        return 1
    print("")

    print("B) LA NOMINA DE LA BATERIA: SE BUSCA EL ANCLA Y SE COMPRUEBA QUE NO ESTA YA")
    t_bat = io.open(BATERIA, encoding="utf-8", newline="").read()
    ya = "vuelta169_tarea2_mutacion_reanclaje.py" in t_bat
    print("   el arnes nuevo ya esta en la nomina: %s" % ya)
    print("   el ancla aparece %d veces" % t_bat.count(ANCLA_VIEJAS))
    if not ya and t_bat.count(ANCLA_VIEJAS) != 1:
        print("   ROJO: el ancla de la nomina no aparece exactamente una vez.")
        return 1
    print("")

    print("C) EL ARNES DE LA 165: SE BUSCAN SUS DOS SUSTITUCIONES")
    t_165 = io.open(ARNES_165, encoding="utf-8", newline="").read()
    fallos = []
    for viejo, _nuevo, rot in CAMBIOS_165:
        n = t_165.count(viejo)
        print("   %-46s apariciones: %d" % (rot, n))
        if n != 1:
            fallos.append(rot)
    if fallos:
        print("   ROJO, no se escribe nada: %s" % fallos)
        return 1
    print("")

    nuevo_bat = t_bat if ya else t_bat.replace(ANCLA_VIEJAS, NUEVO_VIEJAS, 1)
    nuevo_165 = t_165
    for viejo, nuevo, _rot in CAMBIOS_165:
        nuevo_165 = nuevo_165.replace(viejo, nuevo, 1)

    print("D) LOS DOS FICHEROS SOLO CRECEN, Y LO VIEJO SIGUE CITADO")
    print("   bateria: %d -> %d bytes" % (len(t_bat.encode("utf-8")),
                                          len(nuevo_bat.encode("utf-8"))))
    print("   arnes 165: %d -> %d bytes" % (len(t_165.encode("utf-8")),
                                            len(nuevo_165.encode("utf-8"))))
    for lit, rot in (("C_tiene_cinco_clausulas", "el rotulo viejo del numero"),
                     ("esperaba CINCO clausulas", "el motivo viejo escrito"),
                     ("esperaba TRES\n    # clausulas", "el motivo de la 168")):
        print("   sigue citado %-32s: %s" % (rot, lit in nuevo_165))
    if "esperaba TRES\n    # clausulas" not in nuevo_165:
        print("   ROJO: el motivo del re anclaje de la 168 desaparecio.")
        return 1
    for texto, ruta in ((nuevo_bat, BATERIA), (nuevo_165, ARNES_165)):
        try:
            compile(texto, ruta, "exec")
            print("   compile() de %s: OK" % os.path.basename(ruta))
        except SyntaxError as e:
            print("   ROJO: %s no compila: %s" % (ruta, e))
            return 1
    print("")

    if solo_medir:
        print("MODO --comprobar: NO se escribe.")
        return 0

    io.open(BATERIA, "w", encoding="utf-8", newline="").write(nuevo_bat)
    io.open(ARNES_165, "w", encoding="utf-8", newline="").write(nuevo_165)
    print("ESCRITO: scripts/loop/verificar_mutaciones_viejas.py")
    print("ESCRITO: scripts/loop/vuelta165_tarea6_mutacion_op_l_01.py")
    print("VERDE: nomina ampliada y ancla de clausulas re anclada, cero comprobaciones")
    print("       quitadas y cero CASOS_DECLARADOS nuevos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
