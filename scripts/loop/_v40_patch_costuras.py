# -*- coding: utf-8 -*-
"""Parche de la vuelta 40 sobre scripts/costuras_internas.py. Se corre UNA vez."""
import io

P = "scripts/costuras_internas.py"
s = io.open(P, encoding="utf-8").read()
n_orig = len(s)

# ---------------------------------------------------------------- EDIT 1
viejo = '''QUEDA COMO PENDIENTE DE DOCTRINA, no como arreglo silencioso: que umbral
acompana a `MIN_BLOQUE = 2`, o contra que nodos se recalibra la puerta, es
doctrina de medicion y la decide el fundador. Lo que esta vuelta hace es
aplicar la letra, medir el efecto y publicarlo.

Uso:'''
nuevo = '''QUEDA COMO PENDIENTE DE DOCTRINA, no como arreglo silencioso: que umbral
acompana a `MIN_BLOQUE = 2`, o contra que nodos se recalibra la puerta, es
doctrina de medicion y la decide el fundador. Lo que esta vuelta hace es
aplicar la letra, medir el efecto y publicarlo.

===========================================================================
LA PUERTA REPARADA (19 ago 2026, vuelta 40, encargo del acta del auditor 39)
===========================================================================

NADA DE LO DE ARRIBA SE BORRA, por lo mismo de siempre: una correccion que tapa
lo que corrige no se puede auditar. La RECALIBRACION DECLARADA de la vuelta 34
dejo la puerta EN ROJO y lo dijo en su punto 1. Siguio en rojo desde entonces, y
la vuelta 39 la volvio a declarar sin tocarla. Esta seccion la repara.

LA AVERIA, MEDIDA Y NO RECORDADA. `plan_mejora_procesos`, uno de los dos
fixtures, daba 43,1 contra un umbral de 44 y el instrumento se negaba entero
(exit 1, cero entregas). EL MOTIVO NO ERA EL INSTRUMENTO: era el fixture. El
ultimo commit que toco `dataset/nodos/plan_mejora_procesos.json` es `2bd8dd76`
(*OP-F-04-HOR ejecutada en casi todo: doce nodos en trece cortes*), medido con
`git log --follow` en la vuelta 40, y ese nodo esta EN LA NOMINA de
`OP-F-04-HOR`, medido contra `docs/plan/OPERACIONES.jsonl` en la misma vuelta.
O sea: LA PROPIA CAMPANA RECORTO SU FIXTURE POR UNA OPERACION LEGITIMA, y la
puerta confundio "mi fixture quedo rancio" con "el instrumento esta roto".

QUE SE REPARA Y QUE NO SE TOCA:

  * LOS UMBRALES NO SE TOCAN. Pareja 80 y bloque 44 se quedan donde estaban.
    Aflojar el umbral para que el fixture entre seria arreglar la vara en vez
    de la pieza, y esta casa ya lo adjudico dos veces.
  * NINGUN NODO SE TOCA. La reparacion vive entera en `scripts/`. `dataset/`
    no se abre para escribir.
  * LA SEMANTICA DE LA PUERTA NO SE AFLOJA: los fixtures siguen teniendo que
    entrar TODOS, y si falta uno el instrumento sigue negandose a entregar con
    codigo 1. Lo que cambia es CONTRA QUE NODOS se comprueba, y que ahora hay
    un criterio escrito para elegirlos y un camino escrito para retirarlos.
  * LO QUE SE ANADE: un AVISO DE BORDE. En su corrida normal el instrumento
    imprime el margen de cada fixture y AVISA si alguno esta a menos de un
    punto del umbral. La averia de hoy se vio por un exit 1 a destiempo; con
    el aviso, la siguiente se ve venir. Un instrumento que puede advertir y
    calla es la degradacion silenciosa contra la que existe la propia puerta.

LO QUE ESTA REPARACION **NO** ARREGLA, y va escrito por la misma razon que lo
de arriba: LA COLA SIGUE EN EL 42,3 POR CIENTO DEL CATALOGO. Medido en la
vuelta 40 sobre el grafo de ese dia
(`scripts/loop/vuelta40_calibrar_costuras.py`, salida en
`docs/loop/SALIDA_V40_CALIBRACION.txt`): 1.496 nodos en la cola sobre 3.534
activos, y 1.494 de esos entran por la senal de bloque. ES EXACTAMENTE EL COSTO
QUE LA VUELTA 34 MIDIO Y PUBLICO (1.497 sobre el grafo de aquel dia), o sea que
el pendiente de doctrina del punto 2 de arriba SIGUE ENTERO Y SIGUE ABIERTO:
que umbral acompana a `MIN_BLOQUE = 2` lo decide el fundador, y la vuelta 40 NO
lo decide. Reparar la puerta no era arreglar la escala, y no se disfraza de eso.

Uso:'''
assert s.count(viejo) == 1, "EDIT 1 no ancla"
s = s.replace(viejo, nuevo)

# ---------------------------------------------------------------- EDIT 2
viejo = '''# Los dos nodos que dieron origen a la clase. Si el instrumento no los caza, no
# sirve para lo que se construyo y no entrega nada.
CALIBRACION = ("plan_mejora_procesos", "economia_circular_como_modelo_de_negocio")
'''
nuevo = '''# ===========================================================================
# LA CALIBRACION. EL CRITERIO VA ESCRITO ARRIBA DE LA LISTA, para que quien la
# toque despues no tenga que adivinarlo ni deducirlo de los ids.
# ===========================================================================
#
# QUE ES ESTA LISTA. Los nodos contra los que el instrumento comprueba QUE
# SIGUE CAZANDO LA CLASE PARA LA QUE SE CONSTRUYO. Si alguno no aparece en la
# cola, no entrega nada y sale con codigo 1. Tienen que entrar TODOS: la puerta
# no se aflojo, se le cambio el fixture.
#
# EL CRITERIO, y cada punto se MIDIO en la vuelta 40 antes de escribirse
# (salida entera en `docs/loop/SALIDA_V40_CALIBRACION.txt`):
#
#   1. DISPARA HOY con los umbrales VIGENTES, y su medicion va impresa al lado.
#      El umbral no se mueve nunca para que un fixture entre.
#   2. ENTRA POR LA SENAL DE BLOQUE, que es la senal de la que nacio la clase.
#      Los dos fundadores entraron por bloque y no por pareja, y el propio
#      encabezado mide por que la pareja sola no calibra nada.
#   3. MAS DE UNO, Y AL MENOS UNO CON MARGEN AMPLIO. La averia que esta lista
#      repara es justo lo contrario: el fixture era uno de dos, una operacion
#      legitima recorto su nodo, y el instrumento entero se nego a entregar por
#      0,9 puntos.
#   4. SE PREFIERE EL QUE NO ESTE EN LA NOMINA DE NINGUNA OPERACION del plan,
#      medido contra `docs/plan/OPERACIONES.jsonl`. Ese es el nodo que la
#      propia campana no tiene previsto recortar, y es el que ancla la puerta.
#   5. CUANDO UN FIXTURE QUEDA RANCIO SE RETIRA DECLARADO, con su motivo y su
#      commit de origen, y se queda escrito abajo en `CALIBRACION_RETIRADA`.
#      NUNCA se afloja el umbral y nunca se borra el fixture viejo.
#
# LOS TRES DE HOY, con su medicion del 19 ago 2026 al lado (umbral de bloque
# 44, o sea que el margen es lo que sobra):
#
#   fases_traccion_producto                   bloque 72,6 corte tras 4  margen +28,6
#       EL ANCLA. El bloque mas alto del catalogo activo medido ese dia, y el
#       UNICO de los tres que NO esta en la nomina de ninguna operacion del
#       plan: la campana no tiene previsto recortarlo. Criterios 1 a 4.
#   reglas_brainstorming                      bloque 50,6 corte tras 2  margen  +6,6
#       El candidato que el acta del auditor de la vuelta 39 propuso, VERIFICADO
#       AQUI con el instrumento y no citado de aquella pagina. Su operacion
#       (OP-D-04) ya esta CERRADA, asi que no le queda corte pendiente. AVISO
#       DECLARADO: la misma acta lo mando a la cola de lectura como cualquier
#       citado, y si una lectura futura lo desteje, este fixture se retira por
#       el punto 5 igual que el anterior.
#   economia_circular_como_modelo_de_negocio  bloque 44,2 corte tras 3  margen  +0,2
#       EL FUNDADOR SUPERVIVIENTE. De los dos nodos que dieron origen a la
#       clase, es el que HOY sigue disparando, y se queda por eso. VA
#       DECLARADO FRAGIL: dos decimas de margen. No se retira mientras cumpla
#       el criterio 1 (retirar un fixture que SI dispara seria acomodar la
#       puerta), pero el aviso de borde lo va a nombrar en cada corrida.
CALIBRACION = ("fases_traccion_producto",
               "reglas_brainstorming",
               "economia_circular_como_modelo_de_negocio")

# LOS RETIRADOS, QUE NO SE BORRAN. No gobiernan la puerta, pero el instrumento
# LOS SIGUE MIDIENDO Y LOS IMPRIME en cada corrida: un fixture retirado en
# silencio es una calibracion que nadie puede auditar. Si alguno vuelve a
# disparar, el instrumento lo dice, y reincorporarlo es decision de quien lea,
# no del script.
CALIBRACION_RETIRADA = (
    {
        "node_id": "plan_mejora_procesos",
        "retirado": "19 ago 2026, vuelta 40",
        "motivo": ("fixture RANCIO: la propia campana recorto el nodo por una "
                   "operacion legitima y dejo de disparar (bloque 43,1 contra "
                   "umbral 44, por 0,9 puntos), con lo que el instrumento se "
                   "nego a entregar entero desde la vuelta 34"),
        "commit_de_origen": "2bd8dd76",
        "operacion": "OP-F-04-HOR, que lo lleva en su nomina",
        "medicion_al_retirarlo": "5 pasos, pareja 47,1, bloque 43,1 corte tras 2",
    },
)

# A cuantos puntos del umbral un fixture se considera AL BORDE y el instrumento
# lo avisa en su corrida normal, sin fallar. No es un umbral de decision: es un
# aviso, y por eso no entra en ninguna comparacion de disparo.
MARGEN_DE_AVISO = 1.0
'''
assert s.count(viejo) == 1, "EDIT 2 no ancla"
s = s.replace(viejo, nuevo)

io.open(P, "w", encoding="utf-8", newline="\n").write(s)
print("EDITS 1 y 2 aplicados. %d -> %d caracteres" % (n_orig, len(s)))
