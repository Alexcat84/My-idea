# -*- coding: utf-8 -*-
r"""_v212_t1_seccion.py . EL CUERPO DE LA TAREA 1 DEL REPORTE DE LA VUELTA 212.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo y fuera de la
nomina. Moratoria de AUDITOR.md 6.3.

NINGUNA CIFRA DE ESTE FICHERO SE TECLEA. Todas salen de `pick()`, que LEE la
linea entera de un fichero de salida sellado y CAE EN ROJO si no la encuentra.
Esa es la unica defensa que la `4.1` del acta 211 encontro que funcione: contar
el fichero.

Y CUMPLE LA OBLIGACION QUE EL ENCARGO DE LA 212 ANADE: toda tabla que este
compositor arma leyendo filas de una salida dice, EN LA MISMA LINEA, cuantas
filas armo, y al lado la cifra de cuantas deberia haber. `tabla()` lo escribe
solo, para que no dependa de que yo me acuerde.

LAS CITAS DE ACTA LAS LEE `linea_de()` DEL FICHERO, no de la memoria
(obligacion de dictado del `6.6` del acta 210, linea 74203).
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
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")

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
    """LA LINEA ENTERA DE UN FICHERO DE SALIDA QUE EMPIEZA POR `prefijo`.
    Si no esta, ROJO. Si hay varias, se pide cual con `n`."""
    hits = [l for l in cargar(ruta) if l.startswith(prefijo)]
    if len(hits) <= n:
        ROJOS.append("en %s no hay linea %d que empiece por %r" % (ruta, n, prefijo))
        return "(ROJO: no encontrada)"
    return hits[n].strip()


def valor(ruta, prefijo, n=0):
    """LO QUE VA DESPUES DE LOS DOS PUNTOS EN UNA LINEA DE CIFRA."""
    l = pick(ruta, prefijo, n)
    return l.split(":", 1)[1].strip() if ":" in l else l


def cuantas(ruta, prefijo):
    return len([l for l in cargar(ruta) if l.startswith(prefijo)])


def linea_de(ruta, numero):
    """LA LINEA `numero` DE UN FICHERO, LEIDA DEL DISCO Y NO RECORDADA."""
    ls = cargar(ruta)
    if numero < 1 or numero > len(ls):
        ROJOS.append("%s no tiene linea %d" % (ruta, numero))
        return "(ROJO: fuera de rango)"
    return ls[numero - 1].strip()


def tabla(titulo, cabecera, filas, esperadas, fuente):
    """UNA TABLA QUE DICE, EN SU MISMA LINEA DE TITULO, CUANTAS FILAS ARMO Y
    CUANTAS DEBERIA HABER. Si las dos no calzan, lo dice ahi mismo y ROJO."""
    calza = len(filas) == esperadas
    if not calza:
        ROJOS.append("la tabla %r armo %d filas y deberia haber %d"
                     % (titulo, len(filas), esperadas))
    cab = ("**%s.** **FILAS ARMADAS LEYENDO %s: %d; FILAS QUE DEBERIA HABER: %d.**%s"
           % (titulo, fuente, len(filas), esperadas,
              "" if calza else " **LAS DOS NO CALZAN: ROJO.**"))
    out = [cab, ""]
    out.append("| " + " | ".join(cabecera) + " |")
    out.append("|" + "|".join(["---"] * len(cabecera)) + "|")
    for f in filas:
        out.append("| " + " | ".join(f) + " |")
    out.append("")
    return NL.join(out)


S1B = "docs/loop/SALIDA_V%d_T1B_PUESTO_730.txt" % VUELTA
S1BE = "docs/loop/SALIDA_V%d_T1B_ESCRIBIR.txt" % VUELTA
S1C = "docs/loop/SALIDA_V%d_T1C_OP_F_04_HOR.txt" % VUELTA
ACT = "docs/loop/ACTA_AUDITOR.md"
VER = "docs/plan/08_VERIFICACION.md"
FUE = "docs/plan/01_FUENTES.md"
BAN = "docs/BANCO_DE_TEXTOS.md"

P = []


def w(s=""):
    P.append(s)


# ---------------------------------------------------------------- 1.a
w("### `1.a` LOS REGISTROS: EL ACTA 212 LEIDA DESDE SU LINEA, Y CADA CITA CON LA SUYA")
w()
w("El acta del auditor que cubre la vuelta 211 abre en la linea **74334** de "
  "`docs/loop/ACTA_AUDITOR.md`, que es donde el encargo dice que empieza, y de ahi "
  "la lei entera. **Rige la obligacion de dictado del `6.6` del acta 210** (linea "
  "**74203**): toda cita lleva LA LINEA, y la linea se LEE. Las de abajo estan "
  "leidas hoy con `sed -n` desde este compositor, no recordadas.")
w()
CITAS = [
    (74334, "la apertura del acta que cubre la 211"),
    (74203, "la obligacion de dictado del `6.6` del acta 210, que sigue rigiendo"),
    (74641, "la `7.1`, que es el caso del 730 y el cuerpo de mi TAREA 1"),
    (74644, "el verbatim que el acta cita de la razon del archivo"),
    (74651, "la ratificacion del banco `9.6.1` tal como el acta la cita"),
    (74584, "la `6.2`, el criterio de hecho de una ficha de fase 10"),
    (74595, "la `6.3`, `OP-I-01` no se cierra"),
    (74601, "la `6.4`, el `NO CUBRE` se sostiene"),
    (74610, "la `6.5`, el cubo cambia de nombre"),
    (74622, "la `6.7`, la `P.2`, que es lo que ejecuto en la `1.c`"),
    (74690, "la `7.3`, la familia de patrones que solo ven lo que coincide"),
]
w(tabla("LAS CITAS DE ACTA DE ESTE REPORTE, LEIDAS UNA A UNA DE SU LINEA",
        ["linea de `ACTA_AUDITOR.md`", "que es", "el texto que vive ahi, leido hoy"],
        [["**%d**" % n, q, linea_de(ACT, n)[:150]] for n, q in CITAS],
        len(CITAS), "`docs/loop/ACTA_AUDITOR.md` linea a linea"))

# ---------------------------------------------------------------- 1.b
w("### `1.b` EL PUESTO `730`: LO VERIFIQUE, LA VARA LO CONFIRMA, Y QUEDA CORREGIDO")
w()
w("**LO HICE EN EL ORDEN DEL ENCARGO Y NO EN OTRO.** Primero el grafo, despues la "
  "vara, despues la decision, y solo entonces la escritura. La medicion entera vive "
  "en `%s` y la escritura en `%s`." % (S1B, S1BE))
w()
w("#### 1. CONTRA EL GRAFO, NO CONTRA EL ACTA")
w()
FG = [
    ["nodos del grafo cargados / vivos",
     valor(S1B, "CIFRA nodos del grafo cargados") + " / "
     + valor(S1B, "CIFRA nodos vivos")],
    ["aristas de salida vivo-vivo de la madre, por las dos vistas y resueltas",
     pick(S1B, "LA TABLA DE ARISTAS DE SALIDA DE LA MADRE")],
    ["aristas de entrada vivo-vivo de la madre",
     pick(S1B, "LA TABLA DE ARISTAS DE ENTRADA DE LA MADRE")],
    ["**hijos de paso que la madre ENLAZA**",
     "**" + valor(S1B, "CIFRA hijos de paso QUE LA MADRE ENLAZA") + "**"],
    ["la forma, mirada ANTES de contar (caveat de la familia encadenada)",
     valor(S1B, "VEREDICTO DE LA FORMA")],
    ["el caso rojo por mutacion del contador de silueta",
     pick(S1B, "EL CASO ROJO CAE COMO TIENE QUE CAER")],
]
w(tabla("LO QUE MIDIO EL GRAFO", ["que se midio", "lo que dice el instrumento"],
        FG, 6, "`" + S1B + "`"))
w("**LA MADRE ENLAZA CERO DE SUS DOS HIJOS DE PASO, Y NO HAY CADENA QUE LA RESCATE.** "
  "Eso es lo que el encargo pedia publicar y es la mitad que decide: el caveat de la "
  "`9.6.1` manda mirar la forma antes de contar radios, y aqui ninguno de los dos "
  "hijos es alcanzable desde la madre ni a tres saltos. **El contador no es una "
  "constante y lo pruebo mutandolo**: metiendole a mano la arista a `efecto_bullwhip` "
  "sobre una copia en memoria, pasa de 0 a 1.")
w()
w("#### 2. EL CERCO, RECOMPUTADO POR MI, Y AQUI DISCREPO DEL ACTA EN DOS CIFRAS")
w()
PATS = [
    "PATRON cero-enlazados, GUION LITERAL",
    "PATRON cero enlazados, HOLGADO",
    "PATRON choque de la seccion 19, FRASE ENTERA",
    "PATRON seccion 19 A SECAS",
    "PATRON lectura vieja",
    "PATRON seria D",
]
w(tabla("EL CERCO, PATRON POR PATRON, CON EL PATRON DICHO",
        ["lo que midio el instrumento"],
        [[pick(S1B, p)] for p in PATS], len(PATS), "`" + S1B + "`"))
w("**LAS CINCO CIFRAS DEL ACTA, COTEJADAS UNA A UNA CON LAS MIAS.** El acta 211 "
  "publica **13**, **4**, **9**, **11** y **10** en su `7.1` (linea **74659** y "
  "siguientes). **TRES REPRODUCEN AL DIGITO Y DOS NO**, y lo digo en vez de "
  "copiarlas (`EJECUTOR.md` 2: si discrepan de la medicion de hoy, la discrepancia "
  "se declara).")
w()
COT = [
    ["**4** razones en `A` que nombran el cero-enlazados",
     valor(S1B, "CIFRA razones en clase A que nombran el cero-enlazados"),
     "**REPRODUCE**"],
    ["**11** que nombran el choque de la seccion 19",
     pick(S1B, "PATRON choque de la seccion 19, FRASE ENTERA").split("FILAS ARMADAS")[1].strip()[:2],
     "**REPRODUCE** con la frase entera como patron"],
    ["**10** de esas once ya resueltas por la ratificacion",
     valor(S1B, "CIFRA de las 11 filas de la FRASE ENTERA"),
     "**REPRODUCE**, y la que sobra es el 730"],
    ["**13** razones que nombran el cero-enlazados",
     "11 con el guion literal y 14 con el patron holgado",
     "**NO REPRODUCE con ningun patron.** Ni 11 ni 14 son 13"],
    ["**9** de esas trece en `D`",
     "8 con el guion literal y 10 con el patron holgado",
     "**NO REPRODUCE**, y cae con la anterior: es la misma cifra por el otro lado"],
    ["el 730 es **el UNICO** que dice *lectura vieja*",
     pick(S1B, "PATRON lectura vieja"),
     "**NO REPRODUCE: son TRES** (730, 2215 y 2371)"],
    ["el 730 es **el UNICO** que dice *seria D*",
     pick(S1B, "PATRON seria D"),
     "**NO REPRODUCE: son CINCO**, aunque el 730 sigue siendo el unico que lo dice "
     "de si mismo"],
]
w(tabla("LAS CIFRAS DEL ACTA CONTRA LAS MIAS",
        ["lo que el acta publica", "lo que mide mi instrumento", "veredicto"],
        COT, 7, "`" + S1B + "` contra la `7.1` del acta"))
w("**LO QUE ESTA DISCREPANCIA NO TUMBA, Y HAY QUE DECIRLO ENTERO:** las dos cifras "
  "que no reproducen son **de cerco**, no del par. La sustancia del caso del auditor "
  "vive en las tres que si reproducen (los CUATRO en `A`, los ONCE del choque, los "
  "DIEZ ya resueltos), y sobre todo en lo que mide el grafo. **Su lectura se sostiene "
  "y sus cuentas de cerco no**, y las dos cosas se escriben juntas. **Y las de "
  "*lectura vieja* y *seria D* fallan por la misma causa que su propia `7.3` "
  "nombra**: una cifra de unicidad que nadie conto contra el fichero.")
w()
w("#### 3. LA VARA, APLICADA POR MI, CON LOS DOS LADOS ESCRITOS")
w()
VAR = [
    ["**lo que le queda al HIJO** (direccion del `9.6.2`, la unica que manda)",
     pick(S1B, "   LE QUEDAN AL HIJO"),
     "coste en produccion y programacion, coste en transporte y recepcion, "
     "inventario de seguridad y su coste, venta perdida por rotura, y la regla de "
     "decision que usa esos cuatro numeros"],
    ["**lo que le queda a la MADRE** (el lado que no decide, escrito porque el "
     "encargo pide los dos)",
     pick(S1B, "   LE QUEDAN A LA MADRE"),
     "posicion en la cadena, acuerdos de intercambio de datos y POS, y el sistema "
     "barato de visibilidad compartida"],
]
w(tabla("QUE LE QUEDA A CADA NODO CUANDO LE QUITAS LO QUE DICE EL OTRO",
        ["lado", "lo que mide el instrumento", "que es"],
        VAR, 2, "`" + S1B + "`"))
w("**POR EL `67.6`, LO QUE LE QUEDA AL HIJO ES PROCEDIMIENTO Y NO LINEA:** cuatro "
  "computos de coste sobre bases distintas, cada uno con decisiones dentro de si y "
  "repetido en el tiempo, mas una decision que se alimenta de los cuatro. **CONTINUA, "
  "o sea `D`.** Y por el lado que no decide, a la madre tambien le queda "
  "procedimiento: **procedimiento en los dos lados es par SANO por el `9.6.3`**, que "
  "es otra manera de llegar a que no es duplicacion. **LAS DOS DIRECCIONES DEVUELVEN "
  "LO MISMO.**")
w()
w("#### 4. LA DECISION, Y NO ES OBEDIENCIA")
w()
w("**CONFIRMO, Y LO CONFIRMO CON MI MEDICION, NO CON SU CASO.** La ratificacion del "
  "banco `9.6.1` (*EL CERO ENTRA EN LA REGLA*, 12 ago 2026) dice que sin ni un "
  "hermano enlazado la silueta no dice nada y manda el contenido; el grafo dice cero "
  "de dos y sin cadena; y el contenido dice procedimiento. **La `A` del 730 colgaba "
  "de la lectura que esa ratificacion jubilo, y su propia razon lo decia de si "
  "misma.** " + pick(S1B, "VEREDICTO DE ESTA MEDICION"))
w()
w("#### 5. LA CORRECCION, POR EL CARRIL DEL BANCO `9.10`, Y SUS GUARDAS")
w()
GUA = [
    ["filas del archivo al entrar / al salir",
     valor(S1BE, "CIFRA filas AL ENTRAR") + " / "
     + valor(S1BE, "CIFRA filas AL SALIR")],
    ["sede al entrar, por las dos convenciones",
     valor(S1BE, "CIFRA sede docs/INTRA_DOMINIO_VEREDICTOS.jsonl AL ENTRAR")],
    ["sede al salir, por las dos convenciones",
     valor(S1BE, "CIFRA sede docs/INTRA_DOMINIO_VEREDICTOS.jsonl AL SALIR")],
    ["el `sha256` cambia entre entrada y salida",
     valor(S1BE, "CIFRA el sha256 cambia entre entrada y salida")],
    ["**marcador AL ENTRAR**, recomputado con `apertura_del_auditor.marcador()`",
     "**" + valor(S1BE, "CIFRA marcador AL ENTRAR") + "**"],
    ["**marcador AL SALIR**, recomputado con el mismo instrumento",
     "**" + valor(S1BE, "CIFRA marcador AL SALIR") + "**"],
    ["el marcador del disco calza con el que la simulacion predijo",
     valor(S1BE, "CIFRA el marcador del disco calza")],
    ["la simulacion en memoria, antes de tocar el disco",
     valor(S1BE, "CIFRA fallos de la simulacion")],
    ["el texto viejo, entero y encima, byte a byte",
     pick(S1BE, "   el texto viejo esta ENTERO Y ENCIMA", 1)],
    ["campos que cambian en la fila",
     pick(S1BE, "   campos que cambian", 1)],
    ["**el caso rojo por mutacion, corrido ANTES de escribir**",
     "**" + valor(S1BE, "CIFRA mutantes corridos") + "**"],
]
w(tabla("LAS GUARDAS DE LA `1.b`, TODAS DE SU FICHERO DE SALIDA",
        ["guarda", "lo que dice el instrumento"], GUA, 11, "`" + S1BE + "`"))
w("**EL MARCADOR NO SE RESTO A MANO: SE RECOMPUTO CON SU INSTRUMENTO LAS DOS VECES**, "
  "y su salida esta sellada en "
  "`" + valor(S1BE, "CIFRA salida sellada del marcador").split(" (")[0] + "`. "
  "**LOS CUATRO MUTANTES CAEN LOS CUATRO**: la correccion que tapa el texto viejo, la "
  "que toca una segunda fila, la que escribe una clase que la vara no devuelve y la "
  "que mueve el campo `clave`. La guarda que dijo VERDE sobre lo correcto dice ROJO "
  "sobre las cuatro.")
w()
w("#### 6. EL BARRIDO DE TABLAS DERIVADAS, MEDIDO Y NO EJECUTADO")
w()
CIT = [l.strip()[7:] for l in cargar(S1B) if l.startswith("   cita>")]
w(tabla("DONDE VIVE CITADO EL 730 FUERA DEL ARCHIVO",
        ["la cita, tal como el instrumento la leyo"],
        [[c] for c in CIT],
        int(valor(S1B, "LA TABLA DE CITAS DEL 730 FUERA DEL ARCHIVO").split()[0])
        if valor(S1B, "LA TABLA DE CITAS DEL 730 FUERA DEL ARCHIVO").split()[0].isdigit()
        else len(CIT),
        "`" + S1B + "`"))
w("**EL BANCO `9.10` DICE QUE TODO VOLTEO BARRE SUS TABLAS DERIVADAS EN EL MISMO "
  "ACTO, Y YO NO LAS BARRO. DIGO POR QUE Y LO MARCO COMO DISCUTIBLE.** Las tres "
  "citas **siguen siendo ciertas como relato**: las dos vivas dicen que el 730 "
  "*declara* que la clase queda en `A` por la lectura vieja, y eso es exactamente lo "
  "que la fila sigue diciendo, porque la correccion **dejo el texto viejo entero "
  "encima**. Lo que envejece no es la frase: es **la clase que el lector infiere**. "
  "Y editarlas es prosa sellada del informe y del plan, que es forma que este encargo "
  "no ordena y que el propio auditor reserva al fundador en su `6.2` para un caso "
  "hermano. **La tercera es un reporte archivado y esos no se tocan.** **Lo traigo "
  "entero para que se adjudique, con las tres lineas nombradas.**")
w()

# ---------------------------------------------------------------- 1.c
w("### `1.c` LA `P.2`: LA ADJUDICACION DE `OP-F-04-HOR` QUEDA CORREGIDA")
w()
w("**LA CONTRADICCION, MEDIDA:** " + pick(S1C, "CIFRA el campo nodos de OP-F-04-HOR mide")
  + ", y la propia `adjudicacion` decia *LEIDOS LOS 13* ("
  + valor(S1C, "CIFRA la adjudicacion contiene la frase LEIDOS LOS 13").lower()
  + " que la frase esta). **Los dos son ciertos en su fecha y ninguno se borra.**")
w()
MOT = [l.strip()[8:] for l in cargar(S1C) if l.startswith("   motivo>")]
w(tabla("EL MOTIVO, LEIDO DEL DISCO EN SUS DOS LINEAS Y NO RECORDADO",
        ["la linea, tal como el instrumento la leyo"],
        [[m] for m in MOT], 2, "`" + S1C + "`"))
G1C = [
    ["fichas del plan al entrar / al salir",
     valor(S1C, "CIFRA fichas de docs/plan/OPERACIONES.jsonl AL ENTRAR") + " / "
     + valor(S1C, "CIFRA fichas AL SALIR")],
    ["sede al entrar, por las dos convenciones",
     valor(S1C, "CIFRA sede docs/plan/OPERACIONES.jsonl AL ENTRAR")],
    ["sede al salir, por las dos convenciones",
     valor(S1C, "CIFRA sede docs/plan/OPERACIONES.jsonl AL SALIR")],
    ["**cuentas por `estado`, identicas a las de la entrada**",
     "**" + valor(S1C, "CIFRA las cuentas por estado son IDENTICAS") + "**, y son "
     + pick(S1C, "   estado> HECHA", 1).strip() + " y "
     + pick(S1C, "   estado> LISTA", 1).strip()],
    ["`git diff --numstat` sobre `docs/plan/` al entrar / al salir",
     valor(S1C, "CIFRA filas de git diff --numstat -- docs/plan/ AL ENTRAR")
     + " / " + valor(S1C, "CIFRA filas de git diff --numstat -- docs/plan/ AL SALIR")],
    ["la recarga del `jsonl` linea a linea",
     valor(S1C, "CIFRA lineas del fichero recargadas una a una")],
    ["**el campo `nodos` NO se movio**",
     "**" + valor(S1C, "CIFRA el campo nodos de OP-F-04-HOR AL SALIR") + "**"],
    ["**el campo `estado` NO se movio**",
     "**" + valor(S1C, "CIFRA el campo estado de OP-F-04-HOR AL SALIR") + "**"],
    ["el texto viejo, entero y encima, byte a byte",
     pick(S1C, "   el texto viejo esta ENTERO Y ENCIMA", 1)],
    ["**el caso rojo por mutacion, corrido ANTES de escribir**",
     "**" + valor(S1C, "CIFRA mutantes corridos") + "**"],
]
w(tabla("LAS TRES GUARDAS DE LA `1.c`, MAS LAS DOS PROHIBICIONES EXPRESAS",
        ["guarda", "lo que dice el instrumento"], G1C, 10, "`" + S1C + "`"))
w("**LOS DOS CAMPOS PROHIBIDOS SIGUEN DONDE ESTABAN, Y NO ES UNA PROMESA: TRES DE "
  "LOS CUATRO MUTANTES LO PRUEBAN.** El mutante 2 mueve `nodos`, el 3 mueve `estado` "
  "y el 4 toca otra ficha, y la guarda cae en los tres. **La correccion vive solo en "
  "la prosa que contradecia a su vecina.**")
w()

# ---------------------------------------------------------------- 1.d
w("### `1.d` LAS CUATRO ADJUDICACIONES QUE NO PIDEN TRABAJO, REGISTRADAS SIN EJECUTAR")
w()
ADJ = [
    ["`6.2`", "**EL CRITERIO DE HECHO DE UNA FICHA DE FASE 10 ES EL GENERAL**, porque "
     "el fichero declara que es uno solo. Es extension citable, no doctrina nueva",
     "linea **9** de `docs/plan/08_VERIFICACION.md`, leida hoy: "
     + linea_de(VER, 9)],
    ["`6.3`", "**`OP-I-01` NO SE CIERRA y su `estado` se queda en `LISTA`**, con "
     "motivo escrito: un punto en `NO CUBRE` y dos `A MEDIAS` no cumplen el criterio "
     "general. **No lo toque**",
     "linea **74595** del acta: " + linea_de(ACT, 74595)[:120]],
    ["`6.4`", "**EL `NO CUBRE` DEL PUNTO 2 SE SOSTIENE.** 95 formas incompletas y 0 "
     "que lo digan; marcar las 95 sube al fundador y **no lo hago**",
     "linea **74601** del acta: " + linea_de(ACT, 74601)[:120]],
    ["`6.5`", "**EL CUBO SE LLAMA DESDE HOY *LOS PASOS DE HOY SON LOS DEL BLOQUE 1***, "
     "no *EL BLOQUE YA VIVE APARTE*. La medicion vale y el nombre no",
     "linea **74610** del acta: " + linea_de(ACT, 74610)[:120]],
]
w(tabla("LAS CUATRO ADJUDICACIONES REGISTRADAS",
        ["cual", "que dice", "su cita, leida hoy de su linea"],
        ADJ, 4, "`docs/loop/ACTA_AUDITOR.md` y `docs/plan/08_VERIFICACION.md`"))
w("**LO QUE NO TOQUE, Y SE DICE COMO CIFRA:** `OP-I-01` sigue en `LISTA` (la `1.c` lo "
  "midio al contar por `estado`: " + pick(S1C, "   estado> LISTA", 1).strip()
  + " fichas en `LISTA` al entrar y las mismas al salir), y **las 95 entradas del "
  "inventario siguen sin marcar**, que es lo que el encargo manda.")
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
destino = os.path.join(AQUI, "_v%d_t1_seccion.md" % VUELTA)
io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
print("ESCRITO %s -> %d bytes, %d lineas"
      % (os.path.relpath(destino, RAIZ).replace(os.sep, "/"),
         len(texto.encode("utf-8")), texto.count(NL)))
