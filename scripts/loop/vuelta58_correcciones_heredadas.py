# -*- coding: utf-8 -*-
"""vuelta58_correcciones_heredadas.py . LA TAREA 1.2 DE LA VUELTA 58: VACIAR EL
ATRASO DE LAS ONCE CITAS HEREDADAS, UNA A UNA Y CON TRIAGE.

SUCESOR DECLARADO de scripts/loop/vuelta57_correcciones_tarea1.py en su maquina:
ANCLA LITERAL UNICA (rojo si falta o si aparece mas de una vez), IDEMPOTENTE (la
segunda corrida dice YA ESTABA y no escribe), final de linea POR FICHERO (medido
hoy: docs/ va con LF y docs/plan/02_DESTEJIDOS.md va con CRLF, que es la trampa
que la vuelta 57 declaro en su correccion 3).

EL TRIAGE NO SE ADIVINA: sale de scripts/loop/vuelta58_triage_heredadas.py, que
mide POR GIT el commit exacto en el que cada puesto cambio de clase y busca un
CORTE DECLARADO en las veinte lineas de arriba de cada cita. La salida esta en
docs/loop/SALIDA_V58_TRIAGE_HEREDADAS.txt y es la que sostiene cada decision de
abajo.

LAS DOS VIAS, Y LA VARA QUE LAS SEPARA. El acta 57 (pregunta 6) las escribe:
retrato con corte declarado se ROTULA, envejecida se CORRIGE. La vara con la que
aqui se reparten las once, dicha con todas sus letras para que se pueda discutir:

  SE CORRIGE cuando la letra es UNA AFIRMACION SOBRE EL PAR que hoy es falsa y
  cuya correccion NO rompe la frase de alrededor. Son las OCHO citas de tabla:
  siete en INTRA_DOMINIO_INFORME.md y una en BANCO_DE_TEXTOS.md. La forma es la
  del precedente ratificado de la vuelta 57 (linea 4169 del informe, discutible
  D1 y D2 A FAVOR en el acta 57): tachado DENTRO de la celda, que conserva la
  letra vieja, y NOTA FECHADA en bloque de cita DEBAJO de la tabla. Y la nota
  dice ademas, en las cuatro tablas de doctrina, LO QUE NO SE MUEVE: el
  argumento de la tabla queda intacto y lo unico que cambia es el veredicto de
  esa fila, que es literalmente lo que la nota del 203 escribio.

  SE ROTULA cuando reescribir la letra HARIA MENTIR A LA PAGINA. Son las TRES
  citas de docs/plan/02_DESTEJIDOS.md, y las tres por el mismo motivo medido: la
  clase que citan es la de ANTES de una relectura que la propia pagina anuncia o
  que el propio commit de esa pagina ejecuto. Escribir D en el 599 dejaria la
  frase diciendo "es clase D, asi que se relee al cierre del acto", cuando la
  relectura del cierre es EXACTAMENTE lo que la volvio D; y el 784 vive dentro de
  un bloque de codigo que es una salida de instrumento pegada verbatim, donde
  editar una letra es maquillar la foto.

EL ROTULO SE VERIFICA SOLO, y por eso vale como pago del atraso: lleva su
`vigente=` dentro, y scripts/loop/vuelta58_puestos_volteados.py lo coteja contra
el archivo en cada corrida y cae en ROJO si no calza o si el rotulo no cubre
ninguna cita. Un rotulo que envejece grita; no es una excusa que se archiva.

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.

Uso: python scripts/loop/vuelta58_correcciones_heredadas.py [--ejecutar]
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

INF = "docs/INTRA_DOMINIO_INFORME.md"
BAN = "docs/BANCO_DE_TEXTOS.md"
DES = "docs/plan/02_DESTEJIDOS.md"

FECHA = "20 ago 2026"
SELLO = ("**CORRECCION DECLARADA (%s, vuelta 58, TAREA 1.2, por el carril del "
         "banco `9.10`).**" % FECHA)
CITA = ("Medido HOY con `python scripts/loop/vuelta58_triage_heredadas.py` "
        "([`loop/SALIDA_V58_TRIAGE_HEREDADAS.txt`](loop/SALIDA_V58_TRIAGE_HEREDADAS.txt)) "
        "y cotejado con `python scripts/loop/vuelta58_puestos_volteados.py --base 06b89c74`: "
        "[`loop/SALIDA_V58_PUESTOS_VOLTEADOS_ANTES.txt`](loop/SALIDA_V58_PUESTOS_VOLTEADOS_ANTES.txt) "
        "da esta celda envejecida y "
        "[`loop/SALIDA_V58_PUESTOS_VOLTEADOS_DESPUES.txt`](loop/SALIDA_V58_PUESTOS_VOLTEADOS_DESPUES.txt) "
        "la da VERDE.")

NO_SE_MUEVE = ("**LO QUE LA TABLA ARGUMENTA NO CAMBIA Y POR ESO NO SE REESCRIBE**: "
               "lo unico que se mueve es el veredicto de esa fila, igual que en la "
               "correccion del **203** de la vuelta 57.")


def rotulo(puesto, cita, vigente, corte, commit, prosa):
    return ("> **RETRATO CON CORTE DECLARADO (9.10), rotulado el %s en la vuelta 58 "
            "(TAREA 1.2).** `ROTULO puesto=%d cita=%s vigente=%s corte=%s commit=%s` . "
            "%s Este rotulo lo coteja `scripts/loop/vuelta58_puestos_volteados.py` "
            "contra el archivo en cada corrida y cae en ROJO si deja de calzar."
            % (FECHA, puesto, cita, vigente, corte, commit, prosa))


# Cada sitio: (fichero, ancla literal unica, texto nuevo, nombre).
# Los REEMPLAZOS cambian la linea entera. Las INSERCIONES meten un bloque
# DESPUES de la linea ancla, con una linea en blanco por delante.
REEMPLAZOS = [
    (INF,
     "| 393 | `evaluacion_capital_para_cofundadores` | `busqueda_cofundador_complementario` | 1 | **NO** | **A**, duplicacion |",
     "| 393 | `evaluacion_capital_para_cofundadores` | `busqueda_cofundador_complementario` | 1 | **NO** | ~~**A**~~ **D**, duplicacion |",
     "informe 393"),
    (INF,
     "| 395 | `proceso_ideacion_modelo_negocio` | `proceso_diseno_modelo_negocio_5_fases` | 3 | **NO** | **A**, duplicacion |",
     "| 395 | `proceso_ideacion_modelo_negocio` | `proceso_diseno_modelo_negocio_5_fases` | 3 | **NO** | ~~**A**~~ **D**, duplicacion |",
     "informe 395"),
    (INF,
     "| 396 | `elevator_pitch_inversion` | `preparacion_materiales_fundraising` | 1 | **NO** | **A**, duplicacion |",
     "| 396 | `elevator_pitch_inversion` | `preparacion_materiales_fundraising` | 1 | **NO** | ~~**A**~~ **D**, duplicacion |",
     "informe 396"),
    (INF,
     "| **658**, **678** | dos madres distintas | 6 y 3 | **0** | **la figura no aplica** | **A** |",
     "| **658**, **678** | dos madres distintas | 6 y 3 | **0** | **la figura no aplica** | ~~**A**~~ **D** |",
     "informe 658 y 678"),
    (INF,
     "| **1222** | los **dos primeros pasos enteros**: definir que informacion guardar y meterla en el sistema de clientes. **Es el acto que los dos titulos nombran** | **A** | lo compartido **es el acto** |",
     "| **1222** | los **dos primeros pasos enteros**: definir que informacion guardar y meterla en el sistema de clientes. **Es el acto que los dos titulos nombran** | ~~**A**~~ **D** | lo compartido **es el acto** |",
     "informe 1222"),
    (INF,
     "| **1865** | `huella_carbono_empresarial` | **A** | ese nodo **si los tiene**, con las mismas palabras |",
     "| **1865** | `huella_carbono_empresarial` | ~~**A**~~ **D** | ese nodo **si los tiene**, con las mismas palabras |",
     "informe 1865"),
    # EL UNICO SITIO DONDE LA CORRECCION PARTE UNA FILA EN DOS, y el motivo esta
    # medido: la fila publica UNA letra para DOS puestos y hoy los dos no dan la
    # misma. El 2.477 sigue en A (medido) y el 2.488 esta en D. Dejar una sola
    # celda obligaria a poner dos letras en ella, que es exactamente lo que el
    # barrido llama AMBIGUO y lo que no se puede cotejar por maquina. La fila
    # vieja queda ENTERA y TACHADA, que es lo que la regla 8 pide.
    (BAN,
     "| **2.477 / 2.488** | gestion por objetivos (en el titulo) | **MBO**, el acronimo | A |",
     "| ~~**2.477 / 2.488**~~ | ~~gestion por objetivos (en el titulo)~~ | ~~**MBO**, el acronimo~~ | ~~A~~ |\n"
     "| **2.477** | gestion por objetivos (en el titulo) | **MBO**, el acronimo | A |\n"
     "| **2.488** | gestion por objetivos (en el titulo) | **MBO**, el acronimo | **D** |",
     "banco 2.477 y 2.488"),
]

INSERCIONES = [
    (INF,
     "| 402 | `acuerdo_de_co_venta_y_votacion` | `co_sale_drag_along_agreements` | 6 | **SI** | **D**, jerarquia sana |",
     "> %s **LAS TRES CELDAS DE `393`, `395` Y `396` ESTABAN ENVEJECIDAS, y no por"
     " un teclado: envejecieron solas.** Los tres pares se releyeron despues de"
     " escribirse esta tabla y los tres pasaron de `A` a `D`: el **393** y el"
     " **396** el 10 ago 2026 en el commit `3e2e2d32` (*la medicion de los"
     " veinte*), y el **395** el 11 ago 2026 en el commit `3896c57c` (*R22 con la"
     " primera discrepancia*). %s La regla de la arista sigue diciendo lo que"
     " dice y sigue repartiendo en los dos sentidos; lo que cambio es la clase de"
     " esos tres pares, no la regla. %s" % (SELLO, NO_SE_MUEVE, CITA),
     "nota informe 393-396"),
    (INF,
     "| **658**, **678** | dos madres distintas | 6 y 3 | **0** | **la figura no aplica** | ~~**A**~~ **D** |",
     "> %s **LA CELDA DEL `658` Y EL `678` ESTABA ENVEJECIDA.** Los dos pares"
     " pasaron de `A` a `D` el 10 ago 2026 en el commit `59414fc7` (*la vara"
     " ejecutada: diecinueve de veintitres caen*). %s **El limite que la seccion"
     " declara debajo no se toca**: cuando la madre enlaza a CERO hijos la figura"
     " sigue sin aplicar, y esa es la frase que esta tabla existe para sostener."
     " %s" % (SELLO, NO_SE_MUEVE, CITA),
     "nota informe 658-678"),
    (INF,
     "| **1224** | **un solo paso**: limitar cuantos directores ponen los inversionistas. Todo lo que cuelga de el es distinto en cada uno | **D** | lo compartido **es por donde se entra** |",
     "> %s **LA CELDA DEL `1222` ESTABA ENVEJECIDA.** El par paso de `A` a `D` el"
     " 20 ago 2026 en el commit `90bb930c`, el lote C de la vuelta 53. %s **La"
     " regla que esta seccion deja escrita sigue en pie**: cuando lo compartido es"
     " el acto es `A` y cuando es solo el marco de entrada es sano. Lo que este"
     " par ya no es, es su ejemplar del lado `A`. %s" % (SELLO, NO_SE_MUEVE, CITA),
     "nota informe 1222"),
    (INF,
     "| **1865** | `huella_carbono_empresarial` | ~~**A**~~ **D** | ese nodo **si los tiene**, con las mismas palabras |",
     "> %s **LA CELDA DEL `1865` ESTABA ENVEJECIDA.** El par paso de `A` a `D` el"
     " 20 ago 2026 en el commit `cadc9977`, el lote A de la vuelta 53. %s **La"
     " discriminacion medida sigue siendo cierta como lectura**: los dos nodos de"
     " huella difieren en la frontera organizacional y el ano base, y por eso el"
     " tercero se lee distinto contra cada uno. Lo que cambio es donde acabo el"
     " veredicto del `1865`. %s" % (SELLO, NO_SE_MUEVE, CITA),
     "nota informe 1865"),
    (BAN,
     "| **2.548** | voz del cliente (vive: `design_for_six_sigma_dfss` la nombra) | **VOC**, el acronimo | A |",
     "> %s **LA FILA DEL `2.477 / 2.488` PUBLICABA UNA SOLA LETRA PARA DOS PUESTOS"
     " QUE HOY YA NO LA COMPARTEN, y por eso se parte en dos en vez de"
     " corregirse en su sitio.** Medido hoy sobre el archivo: el **2.477** sigue"
     " en `A` y el **2.488** esta en `D` desde el 20 ago 2026, commit `04bd56de`,"
     " el lote B de la vuelta 53. La fila vieja queda entera y tachada. **El"
     " ejemplar de la doctrina no se cae**: el `2.477` lo sostiene con las mismas"
     " palabras, y el acta 53 (pregunta 7) ya dejo dicho que las razones del"
     " `2.477` y del `2.488` eran ciertas contra su par y no se tocan. Lo que el"
     " `2.488` ya no es, es ejemplar de una fusion. %s" % (SELLO, CITA),
     "nota banco 2.477 y 2.488"),
    (DES,
     "**Y AQUI SI VUELVE UN PAR A LA COLA, el primero de esta vuelta:** el puesto **599**, `asociaciones_clave` con `key_partners_hypothesis`, es **clase B**, y su nodo **cambia de texto al absorber**, asi que **se relee al cierre del acto** como manda `08_VERIFICACION`. Los cuatro actos anteriores de la vuelta (331, 341, 344 y el propio 285 de la vuelta 42 aparte) salieron todos en **CERO**; este no.",
     rotulo(599, "B", "D", "2026-08-19", "76c9fadc",
            "La linea de arriba dice `clase B` porque esa ERA la clase cuando el acto"
            " se planeo, y la misma linea declara su propio corte al anunciar que el"
            " par **se relee al cierre del acto**. Esa relectura se ejecuto, y es"
            " justo la que lo dejo en `D`: el commit `76c9fadc` del 19 ago 2026 se"
            " titula *LA RELECTURA DEL 599 de B a D*. Escribir `D` arriba dejaria la"
            " frase diciendo que un par ya releido se relee, que es al reves de lo"
            " que paso."),
     "rotulo 599"),
    (DES,
     "**Y AQUI SI VUELVE UN PAR A LA COLA, el segundo de toda la operacion despues del 599:** el puesto **233**, `analisis_de_cohortes` con `retention_metrics`, es **clase B** y su nodo **cambia de texto al absorber**, asi que **se relee al cierre del acto** como manda `08_VERIFICACION`. Los actos **392** y **711** de esta misma vuelta salieron los dos en **CERO**; este no.",
     rotulo(233, "B", "D", "2026-08-19", "15d42eef",
            "Mismo caso que el del **599**, tres secciones mas arriba: la linea declara"
            " su corte al anunciar la relectura del cierre, y esa relectura es la que"
            " lo dejo en `D`, en el commit `15d42eef` del 19 ago 2026, titulado *LA"
            " RELECTURA DEL 233 de B a D*."),
     "rotulo 233"),
    (DES,
     "```",
     None,  # este se resuelve por posicion; ver ROTULO_784
     "rotulo 784"),
]

# EL 784 VA APARTE porque su ancla no es una linea suya sino EL CIERRE DEL BLOQUE
# DE CODIGO que lo contiene: el rotulo tiene que quedar FUERA del bloque, o el
# propio rotulo entraria en la salida pegada y la falsificaria.
ROTULO_784 = (
    DES,
    "    puesto 784    clase B   lienzo_modelo_negocio con swot_business_model_canvas",
    rotulo(784, "B", "D", "2026-08-19", "c8172126",
           "La cita vive DENTRO de un bloque de codigo que es una salida de"
           " instrumento pegada verbatim, con su propio corte medido dentro (*pares"
           " de clase A vigentes en el archivo hoy: 575*, *nodos 3853, vivos 3524*)."
           " Editar una letra ahi seria maquillar la foto, que es lo mismo que el"
           " discutible D6 de la vuelta 57 dejo adjudicado A FAVOR para la seccion"
           " PASO 3 de `RECOMPUTO_3388.md`. El par paso de `B` a `D` el 19 ago 2026"
           " en el commit `c8172126`, titulado *LA RELECTURA DEL 784 de B a D*. El"
           " rotulo va DESPUES del cierre del bloque, para no entrar en la salida."),
    "rotulo 784")


def fin_de_linea(crudo):
    return "\r\n" if crudo.count("\r\n") > crudo.count("\n") // 2 else "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("TAREA 1.2 . LAS ONCE HEREDADAS, CON TRIAGE . MODO %s"
          % ("EJECUTAR" if a.ejecutar else "SIMULAR"))
    print("=" * 78)
    print()

    # las tres vias, en una sola lista de operaciones sobre lineas
    ops = []
    for ruta, ancla, nuevo, nombre in REEMPLAZOS:
        ops.append(dict(ruta=ruta, ancla=ancla, nuevo=nuevo, nombre=nombre,
                        modo="REEMPLAZO"))
    for ruta, ancla, nuevo, nombre in INSERCIONES:
        if nuevo is None:
            continue
        ops.append(dict(ruta=ruta, ancla=ancla, nuevo=nuevo, nombre=nombre,
                        modo="INSERCION"))
    ops.append(dict(ruta=ROTULO_784[0], ancla=ROTULO_784[1], nuevo=ROTULO_784[2],
                    nombre=ROTULO_784[3], modo="INSERCION-TRAS-BLOQUE"))

    fallos, hechos, ya = [], [], []
    textos = {}
    for ruta in sorted(set(o["ruta"] for o in ops)):
        crudo = io.open(os.path.join(RAIZ, ruta), encoding="utf-8", newline="").read()
        textos[ruta] = dict(fin=fin_de_linea(crudo),
                            lineas=crudo.replace("\r\n", "\n").split("\n"))
        print("  %-34s final de linea %s, %d lineas"
              % (ruta, "CRLF" if textos[ruta]["fin"] == "\r\n" else "LF",
                 len(textos[ruta]["lineas"])))
    print()

    for o in ops:
        L = textos[o["ruta"]]["lineas"]
        # IDEMPOTENCIA: si lo nuevo ya esta, no se toca. Para la insercion se
        # busca el bloque entero; para el reemplazo, la primera linea nueva.
        marca = o["nuevo"].split("\n")[0]
        if marca in L:
            ya.append(o["nombre"])
            print("  YA ESTABA   %-26s %s" % (o["nombre"], o["ruta"]))
            continue
        cuantas = L.count(o["ancla"])
        if cuantas != 1:
            fallos.append("%s: el ancla aparece %d veces en %s"
                          % (o["nombre"], cuantas, o["ruta"]))
            print("  ROJO        %-26s el ancla aparece %d veces"
                  % (o["nombre"], cuantas))
            continue
        k = L.index(o["ancla"])
        if o["modo"] == "REEMPLAZO":
            nuevas = o["nuevo"].split("\n")
            L[k:k + 1] = nuevas
        elif o["modo"] == "INSERCION":
            L[k + 1:k + 1] = ["", o["nuevo"]]
        else:
            # INSERCION-TRAS-BLOQUE: se camina hasta el cierre ``` del bloque
            j = k
            while j < len(L) and L[j].strip() != "```":
                j += 1
            if j >= len(L):
                fallos.append("%s: no se encontro el cierre del bloque de codigo"
                              % o["nombre"])
                print("  ROJO        %-26s sin cierre de bloque" % o["nombre"])
                continue
            L[j + 1:j + 1] = ["", o["nuevo"]]
        hechos.append(o["nombre"])
        print("  ESCRIBE     %-26s %s (%s)" % (o["nombre"], o["ruta"], o["modo"]))

    print()
    if fallos:
        print("  ROJO, %d fallos y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("     %s" % f)
        return 1

    print("  resumen: %d a escribir, %d YA ESTABAN" % (len(hechos), len(ya)))
    print()
    if not a.ejecutar:
        print("  MODO SIMULAR: no se escribe nada.")
        print("FIN")
        return 0
    if not hechos:
        print("  nada que escribir: los %d sitios YA ESTABAN. Idempotente." % len(ya))
        print("FIN")
        return 0

    for ruta, d in textos.items():
        io.open(os.path.join(RAIZ, ruta), "w", encoding="utf-8", newline="").write(
            d["fin"].join(d["lineas"]))
        print("  escrito: %s" % ruta)
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
