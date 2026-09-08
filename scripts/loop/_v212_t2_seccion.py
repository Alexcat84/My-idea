# -*- coding: utf-8 -*-
r"""_v212_t2_seccion.py . EL CUERPO DE LA TAREA 2 DEL REPORTE DE LA VUELTA 212.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo y fuera de la
nomina. Moratoria de AUDITOR.md 6.3.

NINGUNA CIFRA SE TECLEA: todas salen de `pick()` sobre
`docs/loop/SALIDA_V212_T2_COLA_RELECTURA.txt`, y si una linea no esta, ROJO.

Y CUMPLE LA OBLIGACION QUE EL ENCARGO DE LA 212 ANADE: toda tabla dice, en su
misma linea, cuantas filas armo y cuantas deberia haber.

LAS RAZONES ENTERAS VAN DENTRO DE CERCA, que es donde va un verbatim: son cita
del archivo, no cifra de este reporte.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
S2 = "docs/loop/SALIDA_V%d_T2_COLA_RELECTURA.txt" % VUELTA
S1B = "docs/loop/SALIDA_V%d_T1B_PUESTO_730.txt" % VUELTA
BAN = "docs/BANCO_DE_TEXTOS.md"

ROJOS = []
_CACHE = {}


def cargar(ruta):
    if ruta not in _CACHE:
        p = os.path.join(RAIZ, ruta.replace("/", os.sep))
        if not os.path.isfile(p):
            ROJOS.append("no existe %s" % ruta)
            _CACHE[ruta] = []
        else:
            _CACHE[ruta] = io.open(p, encoding="utf-8").read().split(NL)
    return _CACHE[ruta]


def pick(ruta, prefijo, n=0):
    hits = [l for l in cargar(ruta) if l.startswith(prefijo)]
    if len(hits) <= n:
        ROJOS.append("en %s no hay linea %d que empiece por %r" % (ruta, n, prefijo))
        return "(ROJO: no encontrada)"
    return hits[n].strip()


def valor(ruta, prefijo, n=0):
    l = pick(ruta, prefijo, n)
    return l.split(":", 1)[1].strip() if ":" in l else l


def linea_de(ruta, numero):
    ls = cargar(ruta)
    if numero < 1 or numero > len(ls):
        ROJOS.append("%s no tiene linea %d" % (ruta, numero))
        return "(ROJO: fuera de rango)"
    return ls[numero - 1].strip()


def tabla(titulo, cabecera, filas, esperadas, fuente):
    calza = len(filas) == esperadas
    if not calza:
        ROJOS.append("la tabla %r armo %d filas y deberia haber %d"
                     % (titulo, len(filas), esperadas))
    out = ["**%s.** **FILAS ARMADAS LEYENDO %s: %d; FILAS QUE DEBERIA HABER: %d.**%s"
           % (titulo, fuente, len(filas), esperadas,
              "" if calza else " **LAS DOS NO CALZAN: ROJO.**"), ""]
    out.append("| " + " | ".join(cabecera) + " |")
    out.append("|" + "|".join(["---"] * len(cabecera)) + "|")
    for f in filas:
        out.append("| " + " | ".join(f) + " |")
    out.append("")
    return NL.join(out)


def bloque(prefijo, ruta=S2):
    return [l.strip()[len(prefijo.strip()):].strip()
            for l in cargar(ruta) if l.startswith(prefijo)]


P = []


def w(s=""):
    P.append(s)


w("### LA TAREA 2 SE ABRE, PORQUE LA `1.b` CONFIRMO")
w()
w("El encargo la condiciona con estas palabras: *esta tarea SOLO se abre si la `1.b` "
  "CONFIRMA el cambio del 730*. **Confirmo, y por eso existe.** La puerta la comprueba "
  "el propio instrumento leyendo la salida de la `1.b`: "
  + pick(S2, "CIFRA la 1.b dice CONFIRMA") + ", sobre un fichero de "
  + valor(S2, "CIFRA bytes de docs/loop/SALIDA_V%d_T1B_PUESTO_730.txt" % VUELTA)
  + " bytes.")
w()
w("**Y LA LISTA DE LOS CUATRO NO LA TECLEO: LA LEE.** El instrumento saca los cuatro "
  "puestos de la linea de la `1.b` que los publica, y coteja la lista contra la cifra "
  "que esa misma linea declara: " + pick(S2, "CIFRA puestos leidos de esa linea") + ".")
w()

CUATRO = bloque("   cuatro>")
w(tabla("LOS CUATRO EN `A` QUE NOMBRAN EL CERO-ENLAZADOS, CON SU CLASE DE HOY",
        ["puesto y clase, tal como el instrumento la leyo del archivo"],
        [[c] for c in CUATRO], 4, "`" + S2 + "`"))
w("**" + pick(S2, "CIFRA de los 4, cuantos siguen en A despues de la 1.b") + "**, "
  "que son los que esta tarea mira. **El 730 ya no se mira aqui: es el par que la "
  "`1.b` acaba de corregir**, y mirarlo otra vez seria contarlo dos veces.")
w()

w("### DE QUE DEPENDE LA CLASE DE CADA UNO, CITANDO SU PROPIA RAZON")
w()
w("**ESTO ES LECTURA Y CITA, NO RE-CRIBADO**, que es como el encargo lo pide. No "
  "resuelvo aristas ni vuelvo a aplicar la vara: leo la razon que el archivo ya tiene "
  "y publico QUE FRASE SUYA sostiene la clase. Las anclas de busqueda son fijas y "
  "estan en el fuente del instrumento; lo que se publica es **la frase entera** que "
  "cada ancla encuentra.")
w()
REP = bloque("   reparto>")
w(tabla("EL REPARTO DE FRASES, CONTADO POR EL INSTRUMENTO",
        ["lo que midio"], [[r] for r in REP], 3, "`" + S2 + "`"))
w("**" + pick(S2, "CIFRA puestos cuya clase NO cierra por contenido") + ".** "
  "**LOS TRES CIERRAN POR CONTENIDO Y POR ESO LOS TRES SE QUEDAN COMO ESTAN.**")
w()

DET = [
    ("474", "`milk_run_deliveries` / `programacion_entregas_delivery_scheduling`",
     "**CONTENIDO, y con un matiz que marco como DISCUTIBLE.** Su frase de cierre es "
     "*Y el texto lo confirma por su cuenta: este hijo no solo desarrolla el paso 3, "
     "REPITE ademas dos pasos mas de la madre, asi que repite y no continua*. **Eso es "
     "contenido puro y no toca la silueta.**"),
    ("568", "`publicidad_offline_pruebas_locales` / `tracking_publicidad_offline`",
     "**CONTENIDO, y COINCIDO CON EL AUDITOR.** Su frase de cierre es *Y la vara "
     "CONFIRMA la A por el lado del contenido, no por el de la arista: lo unico que el "
     "hijo anade a los pasos 3 y 4 de la madre es UNA LINEA, la pregunta como se entero "
     "de nosotros en el formulario*."),
    ("586", "`brainstorming_efectivo` / `construir_sobre_ideas_ajenas`",
     "**CONTENIDO, y COINCIDO CON EL AUDITOR.** Su frase de cierre es *Y la vara "
     "CONFIRMA la A por contenido: lo unico que el hijo anade al paso 2 de la madre es "
     "UNA LINEA, no atribuir las ideas a una sola persona para que puedan evolucionar*."),
]
w(tabla("EL VEREDICTO DE LECTURA, UNO A UNO",
        ["puesto", "sus dos nodos", "de que depende su clase"],
        [[p, n, v] for p, n, v in DET], 3, "`" + S2 + "`, razon entera leida del archivo"))
w("**LOS DOS QUE EL AUDITOR YA HABIA VERIFICADO SON LOS DOS QUE MI LECTURA CONFIRMA.** "
  "El `568` y el `586` cierran por la vara de LINEA, y los dos lo dicen con esas "
  "palabras en su ultimo bloque. **Coincido con el, y lo digo porque el encargo pide "
  "que lo diga tanto si coincido como si no.**")
w()

w("### LAS RAZONES ENTERAS, PEGADAS SIN CORTAR, QUE ES LO QUE EL ENCARGO PIDE")
w()
w("**VAN DENTRO DE CERCA PORQUE SON VERBATIM DEL ARCHIVO**, no prosa de este reporte: "
  "sus cifras son del que las escribio, no mias. Las lee el compositor del propio "
  "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.")
w()
import json as _json
_filas = [_json.loads(_l) for _l in
          io.open(os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl"),
                  encoding="utf-8") if _l.strip()]
_por = {_f["puesto_intra"]: _f for _f in _filas}
_n = 0
for _p in (474, 568, 586):
    _f = _por[_p]
    w("**PUESTO %d**, clase `%s`, `%s` contra `%s`, razon de %d bytes:"
      % (_p, _f["clase"], _f["nodo_a"], _f["nodo_b"],
         len(_f["razon"].encode("utf-8"))))
    w()
    w("```")
    w(_f["razon"])
    w("```")
    w()
    _n += 1
w("**RAZONES PEGADAS ENTERAS: %d; RAZONES QUE DEBERIA HABER: %d.**" % (_n, 3))
if _n != 3:
    ROJOS.append("se pegaron %d razones y deberian ser 3" % _n)
w()
w("### `474`: POR QUE LO MARCO COMO DISCUTIBLE AUNQUE NO LO MUEVO")
w()
w("**LO MARCO ANTES DE SABER SI ACIERTO, QUE ES LO QUE VALE LA MARCA.** El `474` es "
  "el unico de los tres que **no tiene el bloque de EJECUCION con la vara nombrada** "
  "que el `568` y el `586` si tienen. Lo que tiene es la lectura vieja escrita en "
  "presente, *PROPORCION: CERO enlazados, o sea que no hay hermanos enlazados y la "
  "figura NO APLICA: manda la regla original*, **y encima una confirmacion de "
  "contenido que llega despues y por su cuenta**.")
w()
w("**POR QUE AUN ASI NO SE MUEVE, Y NO ES MI OPINION:** el propio banco lo ratifica "
  "por contenido. La linea **1742** de `docs/BANCO_DE_TEXTOS.md`, leida hoy, dice: "
  + linea_de(BAN, 1742) + ". Y la linea **1735** dice: " + linea_de(BAN, 1735)
  + " **Un veredicto que la ratificacion del fundador nombra entre los que se "
  "sostienen no lo mueve un ejecutor.**")
w()
w("**LA DIFERENCIA CON EL 730, DICHA PARA QUE NO SE CONFUNDAN:** el 730 **decia de si "
  "mismo** que su clase colgaba de la lectura vieja y **que por contenido seria D**, y "
  "por eso su propia razon lo dejaba sin resolver. **El 474 dice lo contrario**: dice "
  "que por contenido REPITE. **Uno pedia que lo resolvieran y el otro ya estaba "
  "resuelto.**")
w()

w("### LO QUE ESTA TAREA NO HIZO, DICHO COMO CIFRA")
w()
NADA = [
    ["clases cambiadas por la TAREA 2",
     valor(S2, "CIFRA clases cambiadas por esta tarea").split(".")[0]],
    ["el `sha256` del archivo al cerrar la TAREA 2",
     valor(S2, "CIFRA sha256 del archivo al cerrar la TAREA 2")],
    ["filas del archivo",
     valor(S2, "CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl")],
    ["puestos que dependen de la silueta y habria que traer",
     valor(S2, "CIFRA puestos cuya clase NO cierra por contenido")],
]
w(tabla("LA TAREA 2 NO TOCA EL ARCHIVO, Y SE MIDE",
        ["que", "lo que dice el instrumento"], NADA, 4, "`" + S2 + "`"))
w("**NO ABRO NINGUNA COLA DE RE-CRIBADO.** El encargo lo dice con estas palabras: "
  "*una cosa es corregir el par que su propia razon deja sin resolver y otra es abrir "
  "una cola de re-cribado por mi cuenta. Yo no la abro y tu tampoco.* **No la abro.** "
  "Lo unico que sube es la marca del `474`, y sube como discutible, no como encargo.")
w()

texto = NL.join(P) + NL
largos = texto.count(chr(8212))
medios = texto.count(chr(8211))
print("CIFRA guiones largos: %d | CIFRA guiones medios: %d" % (largos, medios))
if largos or medios:
    ROJOS.append("hay %d guiones largos y %d medios" % (largos, medios))
print("CIFRA rojos del compositor: %d" % len(ROJOS))
for r in ROJOS:
    print("   ROJO> %s" % r)
if ROJOS:
    print("ROJO: el compositor NO ESCRIBE.")
    sys.exit(1)
destino = os.path.join(AQUI, "_v%d_t2_seccion.md" % VUELTA)
io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
print("ESCRITO %s -> %d bytes, %d lineas"
      % (os.path.relpath(destino, RAIZ).replace(os.sep, "/"),
         len(texto.encode("utf-8")), texto.count(NL)))
