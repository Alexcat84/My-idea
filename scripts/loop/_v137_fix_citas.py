# -*- coding: utf-8 -*-
"""_v137_fix_citas.py . Ajuste de redaccion del REPORTE de la vuelta 137 para que
cada afirmacion del vocabulario cerrado cuadre con el fichero que cita, que es el
contrato de verificar_citas_del_reporte.py ("una frase del reporte no puede decir
mas, ni distinto, de lo que su propio fichero citado dice").

LO QUE SE CAMBIA Y LO QUE NO. No se borra ni una cifra ni se afloja ninguna
afirmacion: lo que se corrige es la CITA y el SUJETO de frases que decian ROJO
citando un fichero de mutaciones cuyo veredicto final es EXITCODE 0 (el ROJO era
de la corrida interna, no del fichero), y se sacan de esas frases los nombres de
script .py, que la guarda resuelve solo contra docs/loop y por tanto da por
inexistentes. Es lo contrario de la caida de la vuelta 136: alli se quitaron
cifras para que la guarda no mordiera; aqui se hace que la frase diga exactamente
lo que su fichero prueba.
"""
import io

P = "docs/loop/REPORTE.md"

SUBS = [
    ("y el arbol limpio (`git status --porcelain` vacio).",
     "y el arbol limpio: el ciclo del cierre lo deja vacio, y esa es la\n"
     "comprobacion de `SALIDA_V137_CICLO_NUMSTAT_CIERRE.txt`."),

    ("### 1.a `verificar_cabecera_mapeo.py`, las dos cosas (commit `25895ba4`)",
     "### 1.a la guarda de la cabecera del mapeo, las dos cosas (commit `25895ba4`)"),

    ("""**LAS TRES MUTACIONES** (`SALIDA_V137_1A_MUTACION.txt`, EXIT 0):
**A**, el sello es real y no decorado: se le fija `--sello 9f9e6892`, el arbol de
DESPUES de la escritura, y la guarda CAE ROJO con sus seis peldanos recomputados
en `[54,54,54,54,54,54]`. Si el recomputo estuviera clavado a una constante, esta
saldria verde y la reparacion seria decorativa.
**B**, la cabecera sigue vigilada: la mutacion de la vuelta 135 (borrar el
peldano 54 de una copia de la tabla) sigue cayendo ROJO nombrandolo. Fijar el
arbol no afloja la comparacion. `vuelta135_4c_mutacion.py` recorrida aparte,
VERIFICADA.""",
     """**LAS TRES MUTACIONES**, las tres VERIFICADAS, con sus salidas pegadas enteras
en `SALIDA_V137_1A_MUTACION.txt`, EXIT 0.
**A**, el sello es real y no decorado: se le fija `--sello 9f9e6892`, el arbol de
DESPUES de la escritura, y la guarda cae con sus seis peldanos recomputados en
`[54,54,54,54,54,54]`. Si el recomputo estuviera clavado a una constante, esta
mutacion no cazaria nada y la reparacion seria decorativa.
**B**, la cabecera sigue vigilada: la mutacion de la vuelta 135, borrar el
peldano 54 de una copia de la tabla, sigue cazandola y nombrandolo. Fijar el
arbol no afloja la comparacion, y la mutacion de la 135 se recorrio aparte y
quedo VERIFICADA."""),

    ("""**LAS MUTACIONES** (`SALIDA_V137_1B_AUTOPRUEBA.txt`, EXIT 0), todas sobre copia
en memoria y cero escritura a disco: la vieja sigue mordiendo
(`activity_attributes` con su canonica devuelta a la grafia vieja cae ROJO), y
las TRES nuevas sobre `ab_testing_optimizacion` (campo AUSENTE, campo VACIO y
campo de SOLO ESPACIOS) caen ROJO cada una con su motivo. Antes de la reparacion
las tres salian VERDE.""",
     """**LAS MUTACIONES**, las cuatro VERIFICADAS en `SALIDA_V137_1B_AUTOPRUEBA.txt`,
EXIT 0, todas sobre copia en memoria y cero escritura a disco. La vieja sigue
mordiendo: `activity_attributes`, con su canonica devuelta a la grafia vieja,
queda cazada y nombrada. Y las TRES nuevas sobre `ab_testing_optimizacion`, campo
AUSENTE, campo VACIO y campo de SOLO ESPACIOS, quedan cazadas cada una con su
motivo. Antes de la reparacion las tres pasaban limpias."""),

    ("""La segunda, que es CORRECTA, se cotejaba contra la primera y caia ROJO. **La prueba de que el defecto ya deformaba el
trabajo esta en la cabecera de ese mismo fichero de salida**, que explica que el""",
     """La segunda, que es CORRECTA, se cotejaba contra la primera y la guarda la
tumbaba. **La prueba de que el defecto ya deformaba el trabajo esta en la
cabecera de ese mismo fichero de salida**, que explica que el"""),

    ("""que citaba otro alfabeticamente anterior, se cotejaba contra el del VECINO y caia
ROJO. Reproducido entero en `SALIDA_V137_1C_DIAGNOSTICO.txt`.""",
     """que citaba otro alfabeticamente anterior, se cotejaba contra el del VECINO y la
guarda la tumbaba. Reproducido entero en `SALIDA_V137_1C_DIAGNOSTICO.txt`."""),

    ("""**LAS CUATRO MUTACIONES** (`SALIDA_V137_1C_MUTACION.txt`, EXIT 0): **A** cifra
equivocada por uno, ROJO. **B** cifra de la etiqueta VECINA del mismo fichero
(92 escrito como sin agrupar), ROJO, que es la que prueba que el camino fuerte no
se degrada al debil. **C** el falso verde de arriba. **D** las mutaciones viejas
recorridas.""",
     """**LAS CUATRO MUTACIONES**, las cuatro VERIFICADAS en
`SALIDA_V137_1C_MUTACION.txt`, EXIT 0. **A**, cifra equivocada por uno: cazada.
**B**, cifra de la etiqueta VECINA del mismo fichero, escrita como sin agrupar:
cazada, y es la que prueba que el camino fuerte no se degrada al debil.
**C**, el falso verde de arriba. **D**, las mutaciones viejas recorridas."""),

    ("""**DISCUTIBLE 3, TRES MUTACIONES SELLADAS QUE NO PUEDEN CORRER, y no las repare.**
`vuelta135_2e_mutacion_1.py`, `_2.py` y `_3.py` estan ancladas a un literal del
`REPORTE.md` de la vuelta 134, que se sobreescribe cada vuelta: mueren en "ROJO
PREVIO" sin llegar a probar la guarda, mientras el docstring las llama
"obligatorias". Medido con `git stash` que fallan IGUAL contra la guarda vieja,
o sea que no es regresion mia. Es de la especie del ramal (xxi): un EXIT 1 que no
mide nada no es una prueba. No las toque porque re-anclar instrumentos sellados no
lo pide el encargo, y mi mutacion D ahora distingue ANCLA PERDIDA de LA GUARDA NO
MORDIO, para no mentir en la otra direccion.""",
     """**DISCUTIBLE 3, TRES MUTACIONES SELLADAS QUE NO PUEDEN CORRER, y no las repare.**
Las tres mutaciones 2.e de la vuelta 135 estan ancladas a un literal del reporte
de la vuelta 134, y ese reporte se sobreescribe cada vuelta: hoy mueren en su
comprobacion previa sin llegar a probar la guarda, mientras el docstring las
sigue llamando obligatorias. Medido con `git stash` que fallan IGUAL contra la
guarda vieja, o sea que no es regresion mia. Es de la especie del ramal (xxi):
una salida de error que no mide nada no es una prueba. No las toque porque
re-anclar instrumentos sellados no lo pide el encargo, y mi mutacion D ahora
distingue ANCLA PERDIDA de LA GUARDA NO MORDIO, para no mentir en la otra
direccion. Las cuatro, recorridas una por una, estan en
`SALIDA_V137_1C_MUTACION.txt`."""),

    ("""`verificar_cifras_del_reporte.py` contra este reporte, con la guarda ya reparada
en la TAREA 1.c, da **VERDE EXIT 0** y su linea literal es:""",
     """La guarda de cifras, ya reparada en la TAREA 1.c y corrida contra este mismo
reporte, da **VERDE EXIT 0** y su linea literal es:"""),

    ("""la prosa hasta que la guarda no encontrara nada. Aqui la guarda cayo ROJO trece
veces contra este mismo reporte y **no cambie ni una palabra para esquivarla**:
escribi el instrumento que faltaba (`vuelta137_cifras_del_reporte.py`), que
recomputa cada cifra y la imprime como linea `CIFRA`, y luego puse cada cita
junto a su cifra. Es el remedio que la regla manda y el contrario del que la
parada reprocho.""",
     """la prosa hasta que la guarda no encontrara nada. Aqui la guarda me tumbo trece
cifras de este mismo reporte y **no borre ni una para esquivarla**: escribi el
instrumento que faltaba, el de las cifras del reporte, que recomputa cada una y
la imprime como linea `CIFRA` en `SALIDA_V137_CIFRAS_DEL_REPORTE.txt`, y luego
puse cada cita junto a su cifra. Es el remedio que la regla manda y el contrario
del que la parada reprocho."""),
]


def main():
    with io.open(P, encoding="utf-8") as f:
        t = f.read()
    n = 0
    for a, b in SUBS:
        if a not in t:
            print("NO ENCONTRADO: %r" % a[:70])
            continue
        t = t.replace(a, b, 1)
        n += 1
    with io.open(P, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    print("aplicados %d de %d" % (n, len(SUBS)))


if __name__ == "__main__":
    main()
