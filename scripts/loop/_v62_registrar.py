# -*- coding: utf-8 -*-
"""_v62_registrar.py . LLAMA AL REGISTRADOR DEL CIERRE DEL TRAMO CON SUS
PARRAFOS DE APERTURA Y SUS NOTAS.

NO ES UN INSTRUMENTO DE MEDIDA: no lee ni un nodo. Es la lista de argumentos del
registro, en un fichero para que se pueda auditar palabra por palabra y para que
la linea de comando no se convierta en un parrafo tecleado en una terminal.
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = os.path.join(RAIZ, "scripts", "loop", "registrar_cierre_de_tramo.py")

ABRE_1 = (
    "> **TRAMO FINAL POR AGOTAMIENTO: VEINTIUNO, NO CINCUENTA. Y CON EL, EL UNIVERSO DE "
    "`OP-U-01` QUEDA AGOTADO.**\n"
    "> Este tramo no tiene cincuenta actos porque **ya no quedaban cincuenta**: fuera de los "
    "tramos 1 a 5\n"
    "> solo quedaban **VEINTIUNO** actos `CERRADOS`, y el abridor **se los llevo todos**. "
    "**Agotarse no es\n"
    "> truncar, y la diferencia es medible: truncar deja actos detras del corte y aqui no queda "
    "ninguno**\n"
    "> (21 tomados de 21, comprobado por el abridor, por la nomina de la 48 y por la corrida "
    "propia del\n"
    "> auditor, tres caminos).")

ABRE_2 = (
    "> **LA VARA NO SE ESTRENO PARA ESTO: SE LEYO ENTERA.** Que un tramo corto por agotamiento "
    "SEA un\n"
    "> tramo esta **adjudicado por el acta de la vuelta 61** (`D1` y pregunta 1, registradas al "
    "final de\n"
    "> esta misma pagina): la vara de la linea **360** define un **PREFIJO CON TOPE de "
    "cincuenta, no un\n"
    "> minimo**, y **el prefijo de una nomina de veintiuno son los veintiuno**. **Ninguna regla "
    "nueva se\n"
    "> estrena aqui.**")

NOTAS = [
    ("**EL TRAMO CIERRA CON CERO ACTOS DECLARADOS, y es el primero de la campana que lo hace.** "
     "**El motivo esta medido y no es merito:** el cuadro de varas del tramo 6 "
     "([`../loop/SALIDA_V61_VARAS_TRAMO6.txt`](../loop/SALIDA_V61_VARAS_TRAMO6.txt)) **no trae ni "
     "un `CHOCAN` ni un `EMPATE SIN VARA`** (12 de `UNA SOLA VARA`, 5 de `TODAS DE ACUERDO` y 4 de "
     "`CONTENIDO EMPATA`), y esas son **las dos unicas figuras que declaran**. **LA MESA SE QUEDA "
     "EN QUINCE ACTOS**, los mismos que el acta 60 conto, y **la rama de LA CANTIDAD COMO VARA "
     "sigue NO ADOPTADA y no se uso en ningun acto de estos dos planes.**"),

    ("**EL UNICO CHOQUE DE PUERTA DEL TRAMO, REGISTRADO EN VEZ DE TAPADO: EL ACTO 20.** "
     "`mantenimiento_sistema_cui` es **puerta** (extremo de puente aprobado, leido del dossier y de "
     "la columna `puerta` del cuadro de varas), y **las DOS vias apuntaban al otro lado**: la vara "
     "de contenido (pasos 6 contra 5) y **la razon del puesto 3364, que NOMBRA superviviente a "
     "`getting_started_maintenance` por dominancia**. **La guarda `1B` prohibe absorber una "
     "puerta**, asi que **LA PUERTA SOBREVIVE** por acta 54 pregunta 1, y **el choque queda escrito "
     "en el motivo sellado del acto**. **Y LA CONSECUENCIA VA DICHA:** el paso con el que la razon "
     "daba esa dominancia, *sanitizar o destruir equipos con CUI antes de retirarlos de las "
     "instalaciones*, **es justo el que tuvo que viajar de `APPEND`, y viajo**."),

    ("**LAS PERDIDAS DE ESTE TRAMO NO VIVEN EN LA PROSA: VIVEN EN UN CAMPO DEL PLAN.** Los dos "
     "planes nacen con el contrato **`CAMPO PROPIO v1`** (raiz con `contrato_de_perdidas`, y cada "
     "acto con su lista `perdidas`, **siempre, aunque vacia**). **LISTA VACIA es una DECLARACION de "
     "cero perdidas; CAMPO AUSENTE es que el plan no lo dice, y eso es `ROJO`.** De los **21** "
     "actos, **nueve declaran cero perdidas** y **doce sellan al menos una**. **Es el pendiente de "
     "instrumento que el acta 60 dejo escrito**, y con el, la mitad que la correccion de aquella "
     "vuelta no pudo arreglar (*sigue contando de menos las que el plan nombra con otras palabras*) "
     "**queda cerrada por contrato en vez de por heuristica**."),

    ("**CORRECCION DECLARADA SOBRE LOS INSTRUMENTOS QUE ESCRIBEN ESTE REGISTRO (20 ago 2026, vuelta "
     "62), y va aqui porque toca a las cifras de esta misma pagina.** "
     "`scripts/loop/tallar_planes_del_tramo.py` contaba las perdidas **SOLO por el token en la "
     "prosa**, y con el contrato nuevo eso habria publicado **`perdidas nombradas 0` en la TABLA 1 "
     "de arriba cuando el campo sella DIECIOCHO**. Ahora, **si el plan declara el contrato, la "
     "cuenta sale del campo**; si no lo declara, se cuenta por token como hasta ahora. **EL "
     "CONTRASTE ESTA CORRIDO Y NO AFIRMADO:** sobre los planes del tramo 5, que no declaran el "
     "contrato, esta version da **exactamente las mismas cifras que aquel registro publico (A 3, B "
     "1, C 0, los tres 4)**, y la unica diferencia del `diff` es el rotulo de la cabecera "
     "([`../loop/SALIDA_V62_CONTRASTE_TRAMO5.txt`](../loop/SALIDA_V62_CONTRASTE_TRAMO5.txt)). **Y "
     "`registrar_cierre_de_tramo.py` llevaba TRES bloques de su plantilla TALLADOS A MANO CON LAS "
     "CIFRAS DEL TRAMO 5** (*50 actos mirados, 34 vivos, 16 ya fundidos*, la casilla *0 / 50*, y la "
     "nota que afirmaba que el lote A ya estaba fundido al tomar la apertura). **Corrido tal cual, "
     "este registro habria publicado esas tres cosas, y las tres son falsas en un tramo de "
     "veintiuno que abre y cierra en la misma vuelta.** Las tres pasan a medirse; **el texto viejo "
     "queda citado entero dentro del propio instrumento**, que es lo que la regla 8 pide."),

    ("**LO QUE QUEDA DE `OP-U-01`, DICHO SIN ADORNO Y CON SU CIFRA:** **el universo esta agotado**. "
     "Los **29** actos vivos de los tramos 1 a 5 son **cosa juzgada** de los registros de sus "
     "tramos (acta 61, pregunta 4): quince siguen la via de la mesa y catorce **no tienen cola "
     "pendiente ni la necesitan**. **No se reparten, no se reabren y no entran en ningun tramo por "
     "abrir**, porque **no queda ninguno por abrir**."),
]


def main():
    argv = [sys.executable, REG,
            "--vuelta", "62",
            "--tallador", "docs/loop/SALIDA_V62_TALLAR_PLANES.txt",
            "--perdidas", "docs/loop/SALIDA_V62_TALLAR_PERDIDAS.txt",
            "--nomina", "docs/loop/SALIDA_V61_TRAMO6_ABIERTO.txt",
            "--fijado", "docs/loop/SALIDA_V62_TRAMO6_CIERRE.txt",
            "--colisiones", "docs/loop/SALIDA_V61_COLISIONES_ESPERADAS_TRAMO6.txt",
            "--cotejo", "docs/loop/SALIDA_V62_COTEJO_INSUMO.txt",
            "--cotejo", "docs/loop/SALIDA_V62_COTEJO_INSUMO_B.txt",
            "--abre", ABRE_1, "--abre", ABRE_2]
    for n in NOTAS:
        argv += ["--nota", n]
    argv += sys.argv[1:]
    return subprocess.run(argv, cwd=RAIZ).returncode


if __name__ == "__main__":
    raise SystemExit(main())
