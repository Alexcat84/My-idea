# -*- coding: utf-8 -*-
r"""vuelta169_tarea1c_notas_al_reporte_168.py . TAREA 1.b y 1.c de la vuelta 169.

ADOSA AL REPORTE DE LA VUELTA 168 LAS TRES CORRECCIONES QUE EL ACTA 168 ENCARGA,
LAS TRES POR EL CARRIL DEL BANCO 9.10 Y NINGUNA BORRANDO UNA PALABRA:

  (6.1) al pie de la seccion 3.c, la NOTA FECHADA que dice que la tabla se
        publico ANTES que su fuente, que la celda `72` era una prediccion
        correcta y no una medicion, y que HOY la fuente existe y esta commiteada.
  (6.3) al parrafo "LA CAUSA, MEDIDA", la medicion del acta: el arnes del retrato
        NACIO ROJO en su PROPIO commit `33fe1380`, de la vuelta 166, y la vuelta
        167 NO movio esa fila. La frase que culpaba a la 167 se queda ENTERA.
  (6.9) a la traza del fichero de componentes, la subida que falta (`801c59f9`
        con 335) y el cambio de "trazada commit a commit" por lo que de verdad
        es, TACHANDO la frase vieja y dejandola visible.

DONDE VIVE EL REPORTE DE LA 168, Y SE DICE PORQUE NO ES OBVIO. `docs/loop/REPORTE.md`
se SOBRESCRIBE cada vuelta (`EJECUTOR.md` 7), asi que el reporte de la 168 es hoy
el contenido de ese fichero y manana sera el de la 169. Estas tres notas se
escriben EN EL FICHERO mientras todavia es el de la 168 y se commitean SOLAS, en
su propio commit, para que el objeto anotado quede en git. Y ademas se REPRODUCEN
en el reporte de la 169, porque quien audite la 169 lee `REPORTE.md` y no el
arbol de un commit intermedio. Que el reporte de una vuelta pasada no tenga sede
durable es una PREGUNTA que el reporte de esta vuelta sube, no algo que este
instrumento decida.

CADA ANCLA SE BUSCA Y TIENE QUE APARECER EXACTAMENTE UNA VEZ. Si una no aparece,
NO SE ESCRIBE NADA: un parche que no encuentra su sujeto es justamente la
enfermedad que la 6.2 de esta misma acta manda curar en otro sitio.

USO:
  python scripts/loop/vuelta169_tarea1c_notas_al_reporte_168.py
  python scripts/loop/vuelta169_tarea1c_notas_al_reporte_168.py --comprobar
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
BATERIA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V168_T3_BATERIA_CIERRE.txt")

ANCLA_6_1 = "### TAREA 4, `OP-V-01` POR LA DECISION 5"
ANCLA_6_3 = "algo cierto: que la campana movio su sujeto. No esta rota.**\n"
ANCLA_6_9_VIEJA = "dice de donde viene, trazada commit a commit con `git show` sobre ese fichero:"
ANCLA_6_9_FIN = "**5.a `OP-L-01`, ABIERTA Y MEDIDA CLAUSULA A CLAUSULA.**"

NOTA_6_1 = """
**NOTA FECHADA ADOSADA EL 4 sep 2026 (vuelta 169, TAREA 1.b), POR EL CARRIL DEL
BANCO 9.10 Y POR LA ADJUDICACION 6.1 DEL ACTA 168. NINGUNA PALABRA DE ARRIBA SE
BORRA.** La tabla de esta seccion 3.c encabeza *"Cifras contadas de
`docs/loop/SALIDA_V168_T3_BATERIA_CIERRE.txt`"* y **se publico ANTES de que ese
fichero existiera**: el commit que la escribe es `fdc46ad2`, de las 18:03:30, y
el fichero nacio a las 18:04, **sin commitear y con CERO BYTES**. Medido y
sellado al abrir la vuelta 169, antes de la primera operacion, en
`docs/loop/SALIDA_V169_APERTURA.txt` secciones D y F: **0 bytes** y **NO ESTA EN
EL ARBOL DE HEAD**.

**LA CELDA QUE NO ERA UNA MEDICION, DICHA CON SU NOMBRE:** de las ocho celdas,
siete si estaban en `SALIDA_V168_BATERIA.txt`, que si estaba commiteada. **La
primera no: `arneses cronometrados 72`.** El fichero commiteado decia **71**, y
el **72** salia de contar la nomina de HOY, que la propia TAREA 4 de la 168 habia
hecho crecer en el mismo commit. **Era una prediccion correcta, no una medicion**,
y una prediccion correcta publicada como medicion sigue siendo la especie que
esta campana persigue, porque la siguiente puede no serlo y se leera igual.

**HOY LA FUENTE EXISTE, Y EL FICHERO NO SE BORRO NI SE RELLENO A MANO: SE
SOBRESCRIBIO CON LA CORRIDA DE VERDAD.** La bateria se re corrio entera en la
vuelta 169 (`python scripts/loop/verificar_mutaciones_viejas.py`), tardo **1.548,4
segundos, 25,8 minutos** por su propio cronometro, y su salida vive commiteada en
`docs/loop/SALIDA_V168_T3_BATERIA_CIERRE.txt`, **15.212 bytes**, commit
`07446f2a`. **LAS OCHO CELDAS REPRODUCEN AL DIGITO**, incluida la que era una
prediccion: `arneses cronometrados` **72**, `ANCLA PERDIDA` **0**, `NO MORDIO`
**1**, `NO REPRODUCIBLE` **0**, `CASO DECLARADO` **2**, `arneses posteriores
FUERA` **0**, `invisibles al censo` **0**, `RUIDO DE CONCURRENCIA` **0**.

**LO QUE ESTA NOTA NO HACE:** no cambia ni una celda de la tabla de arriba, que
resulto ser correcta entera; no borra el encabezado que cito un fichero vacio; y
no convierte la caida en un malentendido. **La caida fue publicar como contado lo
que no se habia contado, y esa sigue escrita.**

"""

NOTA_6_3 = """
**MEDICION ADOSADA EL 4 sep 2026 (vuelta 169, TAREA 1.c), POR LA ADJUDICACION 6.3
DEL ACTA 168, Y EL PARRAFO DE ARRIBA SE QUEDA ENTERO.** El diagnostico de arriba
culpa a la vuelta 167 de haber movido el sujeto, y **eso esta mal atribuido**. La
medicion del auditor, con seis arboles mirados uno a uno: **el arnes
`vuelta166_tarea3_mutacion_retrato.py` NACIO ROJO EN SU PROPIO COMMIT
`33fe1380`, de la vuelta 166**, y **la vuelta 167 NO movio esa fila**: trece
tachadas antes y trece despues. La constante `"TRECE VECES"` ya discrepaba de su
propio computo el dia que se escribio.

**Y EL SEGUNDO DEFECTO ES PEOR QUE EL PRIMERO, PORQUE ES UNA GUARDA QUE DEJO DE
MORDER SIN AVISAR:** desde `33fe1380` la celda ya no contiene el literal
`DOCE VECES,` (dice `~~DOCE~~ TRECE VECES,`), asi que el `replace` no encontraba
nada, el documento **no se mutaba**, y `todos_cuadran` devolvia `True` donde el
caso espera `False`. **Un caso que no muta no prueba nada, y nadie se entera.**

**LA LECCION, QUE ES MAS GRANDE QUE ESTE ARNES Y POR ESO VIAJA AL `R.38`:** un
arnes que se escribe contra el documento de ANTES de la correccion, y se commitea
JUNTO CON la correccion, **nace muerto**. La unica forma de cazarlo es
**correrlo DESPUES de escribir, en el mismo acto**. Aqui no se cazo porque la
bateria no se corrio en dos vueltas.

**LO QUE NO CAMBIA:** la tabla de los tres casos que caen, con su real y su
esperado, **es correcta al digito** y el auditor la reprodujo. Lo que estaba mal
era **de quien era la culpa y desde cuando**. Y la decision de no arreglarlo sin
orden **fue la correcta**: el acta 168 lo adjudico a favor del ejecutor en su
4.5 (c) y lo encargo por nombre en su 6.2, ejecutado en la TAREA 2 de la vuelta
169.

"""

NOTA_6_9 = """

**PRECISION ADOSADA EL 4 sep 2026 (vuelta 169, TAREA 1.c), POR LA ADJUDICACION
6.9 DEL ACTA 168. NO MUEVE NINGUNA CIFRA Y NINGUNA PALABRA DE ARRIBA SE BORRA.**
Los cuatro puntos listados **son ciertos los cuatro**, comprobados por el auditor
con `git show` sobre cada arbol. Lo que la lista no dice es que **entre el segundo
y el tercero la cifra SUBIO**: `78ea7799` **334**, **`801c59f9` 335**, `c8c4e0b3`
**334**. Por eso *"commit a commit"* queda tachado arriba: **prometia
exhaustividad y lo entregado es una seleccion**, y quien la reuse creeria que la
fila solo bajo. **La conclusion no se mueve** (*"la cifra de la nota no es falsa:
es de su corte"*): sigue siendo cierta, y por eso esto es precision y no caida.

"""


def main():
    solo_medir = "--comprobar" in sys.argv
    texto = io.open(REPORTE, encoding="utf-8", newline="").read()
    print("=" * 78)
    print("VUELTA 169, TAREA 1.b y 1.c: LAS TRES NOTAS AL REPORTE DE LA 168")
    print("=" * 78)
    print("")

    print("A) EL SUJETO, MEDIDO ANTES DE TOCARLO")
    print("   ruta: docs/loop/REPORTE.md")
    print("   CIFRA bytes antes: %d" % len(texto.encode("utf-8")))
    print("   CIFRA lineas antes: %d" % texto.count("\n"))
    primera = texto.split("\n", 1)[0]
    print("   primera linea, leida y no supuesta: %s" % primera)
    if "VUELTA 168" not in primera:
        print("   PARADA: este fichero YA NO es el reporte de la 168. No se escribe.")
        return 1
    print("")

    print("B) LAS CUATRO ANCLAS, BUSCADAS UNA A UNA")
    anclas = [("6.1 (pie de la 3.c)", ANCLA_6_1),
              ("6.3 (LA CAUSA, MEDIDA)", ANCLA_6_3),
              ("6.9 (frase vieja de la traza)", ANCLA_6_9_VIEJA),
              ("6.9 (cabecera de la 5.a, donde acaba la traza)", ANCLA_6_9_FIN)]
    fallos = []
    for rotulo, ancla in anclas:
        n = texto.count(ancla)
        print("   %-46s apariciones: %d" % (rotulo, n))
        if n != 1:
            fallos.append("%s aparece %d veces" % (rotulo, n))
    if fallos:
        print("")
        print("ROJO, NO SE ESCRIBE NADA:")
        for f in fallos:
            print("   " + f)
        return 1
    print("")

    print("C) LAS CIFRAS DE LA NOTA 6.1 SE COMPRUEBAN CONTRA EL FICHERO Y CONTRA GIT")
    print("   (relectura al doble, ordenada por el acta 168 en su metrica de credito)")
    bat = io.open(BATERIA, encoding="utf-8", newline="").read()
    bytes_bat = os.path.getsize(BATERIA)
    r = subprocess.run(["git", "ls-tree", "-r", "HEAD", "--",
                        "docs/loop/SALIDA_V168_T3_BATERIA_CIERRE.txt"],
                       cwd=RAIZ, capture_output=True)
    en_arbol = r.stdout.decode("utf-8", "replace").strip()
    print("   bytes del fichero en disco: %d" % bytes_bat)
    print("   git ls-tree -r HEAD lo ve: %s" % ("SI" if en_arbol else "NO"))
    if not en_arbol:
        print("   PARADA: la nota diria que la fuente existe commiteada y NO lo esta.")
        return 1
    comprobaciones = [
        ("15.212", "%d" % bytes_bat == "15212"),
        ("1.548,4 segundos", "1548.4" in bat),
        ("25,8 minutos", "25.8" in bat),
        ("arneses cronometrados 72", "CIFRA arneses cronometrados: 72" in bat),
        ("ANCLA PERDIDA 0", "ANCLA PERDIDA  : 0" in bat),
        ("NO MORDIO 1", "NO MORDIO      : 1" in bat),
        ("NO REPRODUCIBLE 0", "NO REPRODUCIBLE: 0" in bat),
        ("CASO DECLARADO 2", "CASO DECLARADO : 2" in bat),
        ("posteriores FUERA 0",
         "arneses POSTERIORES a la nomina que se quedan FUERA (recomputado al cierre): 0" in bat),
        ("invisibles al censo 0",
         "entradas de la nomina que el censo NO VE (recomputado al cierre): 0" in bat),
        ("RUIDO 0", "RUIDO DE CONCURRENCIA: 0" in bat),
    ]
    malas = [n for n, ok in comprobaciones if not ok]
    for n, ok in comprobaciones:
        print("   la nota dira %-28s y el fichero lo dice: %s" % (n, ok))
    if malas:
        print("   PARADA: la nota publicaria cifras que su fichero no dice: %s" % malas)
        return 1
    print("   CIFRA celdas comprobadas contra el fichero: %d de %d"
          % (len(comprobaciones) - len(malas), len(comprobaciones)))
    print("")

    nuevo = texto
    nuevo = nuevo.replace(ANCLA_6_3, ANCLA_6_3 + NOTA_6_3, 1)
    nuevo = nuevo.replace(
        ANCLA_6_9_VIEJA,
        "dice de donde viene, ~~trazada commit a commit~~ **trazada en LOS CUATRO\n"
        "PUNTOS EN QUE LA CIFRA BAJA** con `git show` sobre ese fichero:", 1)
    nuevo = nuevo.replace(ANCLA_6_9_FIN, NOTA_6_9.lstrip("\n") + ANCLA_6_9_FIN, 1)
    nuevo = nuevo.replace(ANCLA_6_1, NOTA_6_1 + ANCLA_6_1, 1)

    print("D) EL FICHERO SOLO CRECE, Y LO VIEJO SIGUE DENTRO")
    print("   CIFRA bytes despues: %d" % len(nuevo.encode("utf-8")))
    print("   CIFRA lineas despues: %d" % nuevo.count("\n"))
    print("   crece y no encoge: %s" % (len(nuevo) > len(texto)))
    viejas = ["trazada commit a commit",
              "La vuelta 167, en su TAREA 4, anadio una tachada mas",
              "Cifras contadas de",
              "**Marcado como DISCUTIBLE.**"]
    for v in viejas:
        print("   sigue dentro %-52s: %s" % ("'" + v[:48] + "'", v in nuevo))
    perdidas = [v for v in viejas if v not in nuevo]
    if perdidas:
        print("   ROJO: se perdio texto viejo: %s" % perdidas)
        return 1
    print("")

    if solo_medir:
        print("MODO --comprobar: NO se escribe.")
        return 0

    io.open(REPORTE, "w", encoding="utf-8", newline="").write(nuevo)
    print("ESCRITO: docs/loop/REPORTE.md (el de la vuelta 168, anotado por adicion)")
    print("VERDE: las tres notas adosadas, cero palabras viejas borradas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
