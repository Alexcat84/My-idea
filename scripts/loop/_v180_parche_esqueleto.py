# -*- coding: utf-8 -*-
r"""_v180_parche_esqueleto.py . EL PARCHE QUE CONVIERTE EL CLON EN EL ESQUELETO
DE LA 180. Auxiliar de una sola corrida: copia
scripts/loop/vuelta179_esqueleto_reporte.py y le cambia EL DOCSTRING, EL NUMERO
DE VUELTA, LAS CINCO FILAS DE TAREA y LOS PARRAFOS DE PROSA del texto que
escribe. LA MAQUINA NO SE TOCA salvo el numero de vuelta, y eso lo mide despues
scripts/loop/cotejar_clon_declarado.py, no este fichero.

USO:
  python scripts/loop/_v180_parche_esqueleto.py
"""
import io
import os
import shutil
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ORIGEN = os.path.join(AQUI, "vuelta179_esqueleto_reporte.py")
DESTINO = os.path.join(AQUI, "vuelta180_esqueleto_reporte.py")

DOC = 'r"""vuelta180_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA\n\
VUELTA 180, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS CINCO TAREAS ENCARGADAS.\n\
\n\
CLON DECLARADO de scripts/loop/vuelta179_esqueleto_reporte.py. Lo que se toca a\n\
mano son las CINCO filas de tarea, que son las de ESTE encargo, y los parrafos de\n\
prosa que hablan del estado del bucle. La maquina no se toca en ninguna linea\n\
salvo el numero de vuelta.\n\
\n\
Y LA AFIRMACION DE CLON SE MIDE, NO SE AFIRMA: el cotejo lo hace\n\
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte, que es\n\
obligatorio desde la vuelta 178 por el docstring de aquel fichero. Este texto NO\n\
publica ningun resultado de diff.\n\
\n\
DE DONDE VIENE ESA CAUTELA, Y NO SE BORRA DE QUE IBA: la CAIDA DE REPORTE 1 del\n\
acta 176 seccion 5. El esqueleto de la 176 publicaba en su docstring que el\n\
`diff` con `NNN` sustituido "SALE VACIO"; el auditor lo corrio y salieron 58\n\
lineas, 33 de ellas de la maquina, aunque de esas 33 las SENTENCIAS DE CODIGO\n\
eran 1 y los LITERALES DE TEXTO 32 medidos por el instrumento. El instrumento\n\
que lo mide, `scripts/loop/cotejar_clon_declarado.py`, NACIO EN LA TAREA 1.d DE\n\
LA VUELTA 177 y ya trae su CUARTO veredicto, EL ARBOL DE SINTAXIS, desde la 178.\n\
Su salida sobre ESTE fichero se pega en el reporte.\n\
\n\
LA MAQUINA NO CAMBIA EN NADA SALVO EL NUMERO DE VUELTA: el paso 0 endurecido que\n\
estreno la 174 se conserva entero. Esa frase SI es una afirmacion sobre la\n\
maquina, y por eso NO se publica como comprobada aqui tampoco: la comprueba el\n\
instrumento, no este texto.\n\
\n\
QUE ES ESE PASO 0 ENDURECIDO, dicho otra vez para que este fichero se entienda\n\
solo: NO PREGUNTA POR `VUELTA - 1`, PREGUNTA POR EL REPORTE QUE DE VERDAD VA A\n\
PISAR, Y ESE NUMERO SE LEE DEL PROPIO FICHERO con la funcion pura\n\
`vuelta_del_reporte_del_arbol()`. En esta vuelta las dos preguntas coinciden (el\n\
arbol trae el reporte de la 179 y `VUELTA - 1` es 179), y precisamente por eso el\n\
fichero corre LAS DOS y publica lo que salga de cada una: una guarda que solo se\n\
mira cuando difiere no se puede auditar el dia que difiera. Y LA TAREA 4.a DE\n\
ESTA MISMA VUELTA fabrica el caso donde NO coinciden, que es lo que faltaba.\n\
\n\
LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA: `vuelta_del_reporte_del_arbol`\n\
esta copiada de `vuelta174_esqueleto_reporte.py` en vez de importada. Importarla\n\
crearia una dependencia nueva sobre un fichero numerado sin nada que avise si\n\
alguien lo borra por viejo. ESO YA NO ES UN PENDIENTE: la TAREA 4.b de esta\n\
vuelta escribe la guarda que CAE EN ROJO nombrando la fuente del clon si el\n\
fichero del que se clono desaparece. Se clona, se declara, se guarda, y el arnes\n\
de la funcion original (`scripts/loop/vuelta174_tarea1b_mutacion_esqueleto.py`)\n\
sigue apuntando a su sujeto de siempre.\n\
\n\
LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla\n\
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 180 AL CIERRE.\n\
\n\
LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por\n\
`git rev-parse --abbrev-ref HEAD`; commit del acta de la vuelta anterior por las\n\
DOS formas del titulo y en las DOS pasadas de `TALLADOR.buscar_acta`; HEAD de\n\
apertura leido de docs/loop/SALIDA_V180_HEAD_APERTURA.txt, sellado antes de la\n\
primera operacion; commit de nacimiento del bloque de apertura por\n\
`git log --diff-filter=A`. Si alguno no se puede leer o es ambiguo, el esqueleto\n\
CAE EN ROJO y no escribe nada: no inventa un hash.\n\
\n\
USO:\n\
  python scripts/loop/vuelta180_esqueleto_reporte.py\n\
"""'

T1 = ("LOS REGISTROS Y LA ETIQUETA DE FUENTE, Y ES BLOQUEANTE. (a) El acta del "
      "auditor de la vuelta 179 vive en `docs/loop/ACTA_AUDITOR.md` y NO levanta "
      "ninguna caida contra la 179: la racha de reporte vuelve a CERO, la de cifra "
      "publicada sigue en CERO y no hay correccion declarada que arrastrar. (b) LA "
      "ETIQUETA DE FUENTE, ARREGLADA, y eso LEVANTA LA PARADA DE LA 3.f DE LA 179: "
      "`clases_por_par()` LEE LA VUELTA DE LA FILA DEL REGISTRO en vez del literal "
      "`docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)` clavado, con `sha256` de "
      "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y de `docs/plan/OP_L_03_LECTURAS.jsonl` "
      "ANTES y DESPUES dentro del propio instrumento y los CUATRO publicados, con "
      "`vuelta179_tarea3_etiqueta_de_fuente.py` re-corrido y las DOS mediciones al "
      "lado (la de antes y la de despues, y la de despues en CERO falsos o se para), "
      "con `vuelta178_tarea3_anotar_triangulos.py` re-corrido y el total de "
      "triangulos y de lados sin moverse, y con su caso positivo por mutacion sobre "
      "un registro fabricado de dos vueltas distintas")

T2 = ("EL SUJETO CONGELADO, RESUELTO Y CABLEADO, Y ES LA QUE LIMPIA LA PISTA DE LA "
      "181. El orden es: los trece declaran, los cuatro congelan, y SOLO ENTONCES se "
      "cablea. (a) LOS TRECE QUE NO ABREN NADA VIVO DECLARAN SU SUJETO, once `LO "
      "NOMBRA SIN ABRIRLO` y dos `ABRE UN SUJETO YA CLAVADO`, una linea por arnes "
      "con el literal que la guarda busca y NINGUNA otra linea tocada, comprobado "
      "con `git diff --numstat` sobre `scripts/loop/` publicando las lineas anadidas "
      "por fichero. (b) LOS CUATRO QUE SI ABREN, CONGELADOS DE VERDAD, cada uno con "
      "que abria, que abre ahora y la prueba de que su resultado ya no se mueve. (c) "
      "Y SOLO ENTONCES EL CABLEADO al rojo global de la bateria, con la cifra de "
      "antes y su corte pegado y la de despues, que TIENE QUE DAR 0 o no se cablea. "
      "(d) NADA SE PODA DE LA NOMINA: todo arnes que esta vuelta escriba entra en "
      "`verificar_mutaciones_viejas.py` con la cuenta entera y la resta comprobada, "
      "antes de la 181")

T3 = ("EL CORTE, CABLEADO DONDE TODAVIA FALTA. El hallazgo es del fundador y esta "
      "medido en la seccion 6 del acta 179: la tabla de tramos de la 2.a de la 179 "
      "esta contada de su fichero y sus cifras eran verdad, pero LE FALTA EL CORTE, "
      "y sin corte no hay manera de saber cual mira que. Se cablea el sello de "
      "`sello_de_corte()` DONDE SE GENERA LA TABLA DE TRAMOS de "
      "`backlog_l03_resuelto.py`, no en una frase del reporte, por `banco 9.21` y el "
      "punto 7.2 del acta 178. Y SE BARRE EL RESTO: la lista de toda cifra de ese "
      "instrumento y de `vuelta179_tarea2_cobertura_final.py` que pueda moverse "
      "dentro de una vuelta, diciendo cuales llevan corte y cuales no, y las que no "
      "lo lleven lo llevan al terminar. Con su caso positivo por mutacion: dos "
      "cortes distintos con la misma cifra no se confunden, y la misma cifra con dos "
      "cortes distintos tampoco")

T4 = ("LAS DOS PENDIENTES BARATAS QUE YA LLEVAN VUELTAS SUBIENDO, LAS DOS TEXTO QUE "
      "MIENTE SOBRE SU PROPIA MAQUINA. (a) EL DOCSTRING DE "
      "`scripts/loop/paso0_archivar_anterior.py`, que sigue hablando de LA VUELTA "
      "ANTERIOR cuando la maquina ya pregunta por EL REPORTE QUE VA A PISAR: se "
      "arregla, se publican la linea vieja y la nueva sin borrar la vieja del "
      "reporte, y SE ESCRIBE LA GUARDA QUE HACE VISIBLE LA DIFERENCIA, un caso "
      "fabricado donde las dos preguntas NO coinciden y que demuestra que la maquina "
      "responde a la buena. (b) LA GUARDA QUE FALTA EN LA DEPENDENCIA DEL `D.4` DE "
      "LA 174: el esqueleto CLONA `vuelta_del_reporte_del_arbol()` en vez de "
      "importarla y nada avisa si el fichero del que se clono desaparece; la guarda "
      "CAE EN ROJO nombrandolo, con su caso positivo por mutacion sobre una ruta "
      "fabricada que no existe")

T5 = ("EL BACKLOG DE `OP-L-02`, MEDIDO Y NO LEIDO, CON LA MISMA VARA RESUELTA QUE "
      "CERRO `OP-L-03`. Se corre el instrumento viejo de `OP-L-02` por dentro y sin "
      "citarlo de memoria y se publican LOS PARES QUE DA; se le pone encima el "
      "resolutor de `P.1` y se publican LOS PARES REALES, o sea los que no estan ya "
      "en el archivo tras resolver a nodo vivo; LAS DOS COLUMNAS VAN LAS DOS Y LA "
      "VIEJA NO SE BORRA (`banco 9.10`); el reparto por tramo va CON SU CORTE PEGADO "
      "por la TAREA 3 de este mismo encargo; y LOS DOS CAMINOS TIENEN QUE CALZAR en "
      "todos los actos medidos o se publica donde y se para. LO QUE NO SE HACE: no "
      "se lee ningun par, no se escribe ningun veredicto, no se toca el marcador, no "
      "se toca el estado de ninguna ficha (`EJECUTOR.md` 4, modo de cierre) y NO SE "
      "TOCAN LOS CINCO PARES DE SALES ROADMAP, que `docs/plan/LECTURAS_DIRIGIDAS.md` "
      "deja como decision revocable del fundador: se nombran y se dejan")

TAREAS = "TAREAS = [\n" + "".join(
    '    ("%s", %r),\n' % (n, t) for n, t in
    (("1", T1), ("2", T2), ("3", T3), ("4", T4), ("5", T5))) + "]\n"

# LOS PARRAFOS DE PROSA DEL TEXTO QUE EL ESQUELETO ESCRIBE. Se cambian por
# reemplazo EXACTO del viejo, y si alguno no se encuentra este fichero CAE EN
# ROJO: un parche que no encuentra su sujeto y sigue en silencio es justo la
# especie de degradacion que el banco 9 prohibe.
PROSA = [
 ("> **ESTA VUELTA NO ES DE BATERIA, Y LA CADENCIA NO SE ELIGE AQUI: ESTA\n"
  "> ADJUDICADA Y RECONFIRMADA DOS VECES.** El acta 176, punto 7.8, reanclo el\n"
  "> contador a la vuelta que de verdad corrio la bateria y no a la que la tenia\n"
  "> encargada; **el acta 178, punto 11, lo reconfirmo**; y el encargo de esta vuelta\n"
  "> lo repite con todas las letras: **la proxima vuelta de bateria es la 181**, y la\n"
  "> 179 y la 180 cierran su seccion 9 con el **HUECO DECLARADO Y MEDIDO**, con su\n"
  "> nombre, sus bytes medidos y su atribucion, las tres juntas. Un hueco declarado\n"
  "> no es un hueco escondido.",
  "> **ESTA VUELTA NO ES DE BATERIA Y LA SIGUIENTE SI, Y LA CADENCIA NO SE ELIGE\n"
  "> AQUI: ESTA ADJUDICADA Y RECONFIRMADA TRES VECES.** El acta 176, punto 7.8,\n"
  "> reanclo el contador a la vuelta que de verdad corrio la bateria y no a la que la\n"
  "> tenia encargada; **el acta 178, punto 11, y el acta 179, punto 11, lo\n"
  "> reconfirmaron**; y el encargo de esta vuelta lo repite con todas las letras:\n"
  "> **la proxima vuelta de bateria es la 181**. Esta es **LA ULTIMA VUELTA QUE\n"
  "> DECLARA EL HUECO**: la seccion 9 cierra con el **HUECO DECLARADO Y MEDIDO** y\n"
  "> sus TRES piezas juntas, el nombre del fichero, sus bytes por las dos\n"
  "> convenciones y la atribucion. Un hueco declarado no es un hueco escondido, y\n"
  "> **la 181 lo corre**."),

 ("> **EL TOPE SIGUE EN CINCO, Y NO LO DECIDE NADIE: LO DISPARO LA 177 Y LA 178 LO\n"
  "> CONFIRMO ENTREGANDO CINCO.** `AUDITOR.md` 6.2 dice que el regimen temporal de\n"
  "> dos sub-tareas dura **hasta que DOS vueltas seguidas cierren su propio reporte**\n"
  "> con `cerrar_reporte.py`, y eso se cumplio. **El regimen temporal queda CUMPLIDO\n"
  "> Y CITABLE, no borrado**, y los cuatro commits que lo sostienen se localizan EN\n"
  "> GIT en el bloque B.1 de `scripts/loop/vuelta179_apertura.py`, no se teclean.",
  "> **EL TOPE SIGUE EN CINCO, Y NO LO DECIDE NADIE: LO DISPARO LA 177 Y LA 178 Y LA\n"
  "> 179 LO CONFIRMARON ENTREGANDO CINCO.** `AUDITOR.md` 6.2 dice que el regimen\n"
  "> temporal de dos sub-tareas dura **hasta que DOS vueltas seguidas cierren su\n"
  "> propio reporte** con `cerrar_reporte.py`, y eso se cumplio. **El regimen\n"
  "> temporal queda CUMPLIDO Y CITABLE, no borrado**, y los cuatro commits que lo\n"
  "> sostienen se localizan EN GIT en el bloque B.1 de\n"
  "> `scripts/loop/vuelta180_apertura.py`, no se teclean."),

 ("> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE\n"
  "> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en\n"
  "> `vuelta177_apertura.py`, la 178 lo estreno y aqui se repite: el medidor corre\n"
  "> dentro del bloque de apertura. **Desde la 178, una columna de apertura medida al\n"
  "> cierre es caida que ACUMULA**, y eso lo dice el encargo, no este reporte.",
  "> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE\n"
  "> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en\n"
  "> `vuelta177_apertura.py`, la 178 lo estreno, la 179 lo repitio y aqui vuelve a\n"
  "> correr en su sitio. **Desde la 178, una columna de apertura medida al cierre es\n"
  "> caida que ACUMULA**, y eso lo dice el encargo, no este reporte."),

 ("> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR\n"
  "> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la\n"
  "> %(ant)d escribio su reporte, lo cerro y lo archivo EN SU MISMA VUELTA; el\n"
  "> fichero corre LAS DOS igualmente y publica lo que salga de cada una, porque una\n"
  "> guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.",
  "> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR\n"
  "> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la\n"
  "> %(ant)d escribio su reporte, lo cerro y lo archivo EN SU MISMA VUELTA; el\n"
  "> fichero corre LAS DOS igualmente y publica lo que salga de cada una, porque una\n"
  "> guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.\n"
  "> **Y LA TAREA 4.a DE ESTA VUELTA FABRICA EL DIA EN QUE DIFIEREN**, que es lo que\n"
  "> a esta guarda le faltaba desde la 174: hasta hoy nadie la habia visto responder\n"
  "> a la pregunta buena cuando las dos preguntas dan cosas distintas."),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    shutil.copyfile(ORIGEN, DESTINO)
    t = io.open(DESTINO, encoding="utf-8").read().replace(chr(13) + chr(10), chr(10))
    n0 = len(t)

    fin = t.index('"""', t.index('r"""') + 4) + 3
    t = DOC + t[fin:]

    i0 = t.index("TAREAS = [")
    i1 = t.index(chr(10) + "]" + chr(10), i0) + 3
    t = t[:i0] + TAREAS + t[i1:]

    t = t.replace("VUELTA = 179", "VUELTA = 180", 1)

    fallos = []
    for viejo, nuevo in PROSA:
        if viejo not in t:
            fallos.append(viejo.split(chr(10))[0][:70])
            continue
        t = t.replace(viejo, nuevo, 1)
    if fallos:
        print("ROJO: %d parrafo(s) de prosa NO se encontraron y no se toco nada:"
              % len(fallos))
        for f in fallos:
            print("   " + f)
        return 1

    io.open(DESTINO, "w", encoding="utf-8", newline=chr(10)).write(t)
    print("VERDE: %s escrito" % os.path.relpath(DESTINO, os.path.dirname(AQUI)))
    print("   bytes del origen: %d | bytes del destino: %d" % (n0, len(t)))
    print("   CIFRA apariciones de 'VUELTA = 180': %d" % t.count("VUELTA = 180"))
    print("   CIFRA apariciones de 'VUELTA = 179': %d" % t.count("VUELTA = 179"))
    print("   CIFRA filas de TAREAS: %d" % t.count('    ("'))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
