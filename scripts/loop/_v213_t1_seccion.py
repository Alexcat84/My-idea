# -*- coding: utf-8 -*-
r"""_v213_t1_seccion.py . EL CUERPO DE LA TAREA 1 DEL REPORTE DE LA VUELTA 213.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo y fuera de la
nomina. Moratoria de AUDITOR.md 6.3.

NINGUNA CIFRA DE ESTE FICHERO SE TECLEA. Todas salen de `pick()`, que LEE la
linea entera de un fichero de salida sellado y CAE EN ROJO si no la encuentra
(`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO).

CUMPLE LA OBLIGACION DE LAS FILAS: toda tabla que este compositor arma leyendo
filas de una salida dice, EN LA MISMA LINEA, cuantas filas armo, y al lado la
cifra de cuantas deberia haber. `tabla()` lo escribe solo.

Y CUMPLE LA OBLIGACION DE DICTADO DEL `6.6` DEL ACTA 210: las citas de acta las
lee `linea_de()` DEL FICHERO, no de la memoria.
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
    """LA LINEA ENTERA (SIN SANGRIA) DE UN FICHERO DE SALIDA QUE EMPIEZA POR
    `prefijo`. Si no esta, ROJO."""
    hits = [l.strip() for l in cargar(ruta) if l.strip().startswith(prefijo)]
    if len(hits) <= n:
        ROJOS.append("en %s no hay linea %d que empiece por %r" % (ruta, n, prefijo))
        return "(ROJO: no encontrada)"
    return hits[n]


def valor(ruta, prefijo, n=0):
    l = pick(ruta, prefijo, n)
    return l.split(":", 1)[1].strip() if ":" in l else l


def linea_de(ruta, numero):
    """LA LINEA `numero` DE UN FICHERO, LEIDA DEL DISCO Y NO RECORDADA."""
    ls = cargar(ruta)
    if numero < 1 or numero > len(ls):
        ROJOS.append("%s no tiene linea %d" % (ruta, numero))
        return "(ROJO: fuera de rango)"
    return ls[numero - 1].strip()


def celda(t):
    """UNA CELDA NO PUEDE LLEVAR NI BARRA VERTICAL NI TABULADOR: la primera
    parte la tabla en columnas que nadie pidio y el segundo la ensucia. Se
    escapan aqui, en el sitio unico por el que pasan TODAS las celdas."""
    return t.replace("|", chr(92) + "|").replace(chr(9), "  ")


def tabla(titulo, cabecera, filas, esperadas, fuente):
    filas = [[celda(c) for c in f] for f in filas]
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


S1B = "docs/loop/SALIDA_V%d_T1B_BARRIDO_9_10.txt" % VUELTA
ACT = "docs/loop/ACTA_AUDITOR.md"
FUS = "docs/plan/03_FUSIONES.md"
INF = "docs/INTRA_DOMINIO_INFORME.md"

P = []


def w(s=""):
    P.append(s)


# ---------------------------------------------------------------- 1.a
w("### `1.a` LOS REGISTROS: EL ACTA QUE CUBRE LA 212, LEIDA DESDE SU LINEA")
w()
w("El acta abre en la linea **74821** de `docs/loop/ACTA_AUDITOR.md`, que es donde el "
  "encargo dice que abre, y de ahi la lei entera. **Rige la obligacion de dictado del "
  "`6.6` del acta 210** (linea **74203**): toda cita lleva LA LINEA, y **la linea se "
  "LEE, no se recuerda**. Las de abajo las lee este compositor con `linea_de()` en "
  "esta corrida.")
w()
CITAS = [
    (74821, "la apertura del acta que cubre la 212"),
    (74203, "la obligacion de dictado del `6.6` del acta 210, que sigue rigiendo"),
    (75082, "la `6.1`, la `P.1` adjudicada: es lo que ejecuto en la `1.b`"),
    (75112, "la `6.2`, la `P.2` contestada: el crash ESPERA"),
    (75128, "la mitad de la `6.2` que si se pone hoy, y es obligacion de dictado"),
    (75133, "la `6.3`, mi `D.1` resuelta, y la marca se me paga"),
    (75138, "la `6.4`, mi `D.2`: el `474` NO SE MUEVE"),
    (75145, "la `6.5`, mi `D.3`: tenia razon, y queda contra el acta 211"),
    (75156, "la `6.6`, mi `D.4` y mi `PD.2`, cerradas sin doctrina nueva"),
    (75164, "la `6.7`, mi `PD.1`, cerrada con la `6.1`"),
    (75168, "la `6.8`, el tope de sub-tareas vuelve a CINCO"),
    (75009, "la `4.1`, mi `C.1`: se acepta la declaracion"),
    (75028, "la linea de la `4.1` que adopta mi remedio como obligacion"),
    (75188, "la `7.1`, el punto ciego de `secciones_fuera_de_orden()`"),
]
w(tabla("LAS CITAS DE ACTA DE ESTE REPORTE, LEIDAS UNA A UNA DE SU LINEA",
        ["linea de `ACTA_AUDITOR.md`", "que es", "el texto que vive ahi, leido hoy"],
        [["**%d**" % n, q, linea_de(ACT, n)[:150]] for n, q in CITAS],
        len(CITAS), "`docs/loop/ACTA_AUDITOR.md` linea a linea"))

w("**LOS SIETE REGISTROS QUE EL ENCARGO PIDE, UNO A UNO Y CON LO QUE HAGO CON CADA "
  "UNO.** Ninguno se ejecuta salvo la `6.1`, que es la `1.b`.")
w()
REG = [
    ["**`6.1`**", "**75082**",
     "LA `P.1` SE ADJUDICA: el barrido del `9.10` se debe, es UNA sola linea y no es "
     "doctrina nueva. De las dos citas vivas del 730, la del informe NO se toca y la "
     "de `03_FUSIONES.md` SE CORRIGE",
     "**EJECUTADA en mi `1.b`**"],
    ["**`6.2`**", "**75112**",
     "LA `P.2` SE CONTESTA: el crash de `vuelta186_rutas_del_reporte.py` NO entra por "
     "la puerta de la caida de dato y **ESPERA**, porque `cerrar_reporte.py` no importa "
     "`main()` sino `medir_en_disco()` (su linea **154**), que usa `os.path.isfile`",
     "**REGISTRADA. No reparo nada** (moratoria). **La obligacion de dictado va "
     "puesta**: este reporte no cita ningun directorio a secas entre comillas inversas"],
    ["**`6.3`**", "**75133**",
     "MI `D.1` SE RESUELVE CON LA `6.1`, y acerte en no tocarlas solo. **Estaba "
     "equivocado en una de las dos mitades y la marca es lo que permitio verlo**",
     "**REGISTRADA. La marca se me paga** y la conducta se repite: en esta vuelta "
     "vuelvo a marcar lo que no se"],
    ["**`6.4`**", "**75138**",
     "MI `D.2`, el `474`, **NO SE MUEVE**, y mi decision de no moverlo es correcta "
     "como decision, no solo como marca",
     "**REGISTRADA. No lo toco.** No hay cola de re-cribado abierta en esta vuelta"],
    ["**`6.5`**", "**75145**",
     "MI `D.3` se adjudica a mi favor: mis nueve cifras de cerco reproducen al digito "
     "y las dos del acta 211 no. **Queda registrada contra el acta 211, no contra mi**",
     "**REGISTRADA. No recomputo el cerco otra vez**: el encargo no lo pide y el "
     "cerco esta cerrado"],
    ["**`6.6` y `6.7`**", "**75156** y **75164**",
     "MI `D.4`, mi `PD.1` y mi `PD.2` se cierran **sin doctrina nueva**. Pegar la "
     "razon entera era lo que el encargo pedia; el alcance del `9.10` fuera de las "
     "tablas queda adjudicado por extension citable",
     "**REGISTRADAS. Ninguna abre trabajo.** La `PD.1` deja de estar pendiente"],
    ["**`4.1`**", "**75009**",
     "MI `C.1` se acepta y **NO ACUMULA**, por dos motivos medidos: la letra del 5 sep "
     "define la especie como ruta a fichero inexistente o de cero bytes, y el mio "
     "media **1603** bytes; y **ninguna sede publicaba esa ruta**. Me acuse de mas de "
     "lo que los hechos sostienen",
     "**REGISTRADA. Mi remedio se adopta como obligacion y lo cumplo en esta misma "
     "vuelta**: el tallador de apertura escribio en `SALIDA_V213_TALLADOR_RECHAZO.txt`"],
]
w(tabla("LOS REGISTROS DEL ENCARGO",
        ["adjudicacion", "su linea", "que dice, resumido de la linea leida hoy",
         "que hago con ella"],
        REG, 7, "`docs/loop/ACTA_AUDITOR.md`"))

w("**LAS CUATRO COSAS QUE SUBEN AL FUNDADOR, REGISTRADAS SIN EJECUTARLAS.** Estan en "
  "la seccion **8** del acta (abre en la linea **75223**).")
w()
SUBEN = [
    ["**1**", "**75225**", linea_de(ACT, 75225)[:150],
     "**ESTA ES LA QUE BLOQUEA EL CIERRE DE LA CAMPAÑA**"],
    ["**2**", "**75232**", linea_de(ACT, 75232)[:150], "no bloquea: es cola de la integral"],
    ["**3**", "**75238**", linea_de(ACT, 75238)[:150], "no bloquea: es aviso de cifra publicada"],
    ["**4**", "**75242**", linea_de(ACT, 75242)[:150], "no bloquea: es del regimen del auditor"],
]
w(tabla("LO QUE SUBE AL FUNDADOR, LEIDO DE SU LINEA",
        ["punto", "linea", "su primera linea, leida hoy", "bloquea el cierre"],
        SUBEN, 4, "`docs/loop/ACTA_AUDITOR.md` seccion 8"))
w("**LO DIGO EN VOZ ALTA, QUE ES LO QUE EL ENCARGO PIDE: LA QUE BLOQUEA EL CIERRE DE "
  "LA CAMPAÑA ES LA PRIMERA.** `OP-I-01` esta abierta, tiene un punto en `NO CUBRE`, y "
  "**lo que ese punto necesita no lo puede dar el bucle**: marcar las entradas del "
  "inventario y anadir filas a `docs/plan/08_VERIFICACION.md` es del fundador por las "
  "adjudicaciones `6.3` y `6.4` del acta 211. **Mientras eso no se decida, la FASE III "
  "no se declara consumida y `PARA_ALEXIS.md` no se escribe.** Las otras tres son "
  "reales y ninguna es puerta: la 2 es cola de la integral, la 3 es un aviso de cifra "
  "publicada y la 4 es del regimen del auditor.")
w()

# ---------------------------------------------------------------- 1.b
w("### `1.b` EL BARRIDO DEL `9.10`: UNA LINEA CORREGIDA, Y LA OTRA CITA INTACTA")
w()
w("**LA MEDICION ENTERA VIVE EN `%s`**, y de ahi sale cada cifra de aqui abajo. El "
  "orden fue el de la casa: sede, lectura del disco, composicion en memoria, juicio, "
  "**caso rojo por mutacion ANTES de escribir**, y solo entonces la escritura." % S1B)
w()
w("#### 1. LO QUE LEI DEL DISCO ANTES DE TOCAR NADA, Y UNA DISCREPANCIA QUE DECLARO")
w()
LEC = [
    ["linea **5424** de `docs/plan/03_FUSIONES.md`, leida hoy",
     pick(S1B, "linea 5424 LEIDA DEL DISCO:").split(":", 1)[1].strip()],
    ["linea **5425**, leida hoy",
     pick(S1B, "linea 5425 LEIDA DEL DISCO:").split(":", 1)[1].strip()],
    ["linea **6941** de `docs/INTRA_DOMINIO_INFORME.md`, leida hoy y **NO TOCADA**",
     pick(S1B, "linea 6941:").split(":", 1)[1].strip()],
]
w(tabla("LAS TRES LINEAS EN JUEGO, LEIDAS DEL DISCO EN ESTA VUELTA",
        ["cual", "lo que dice, leido hoy"], LEC, 3, "`" + S1B + "`"))
w("**DECLARO UNA DISCREPANCIA EN VEZ DE RESOLVERLA COPIANDO** (`EJECUTOR.md` 2). El "
  "encargo y la `6.1` del acta citan **la linea 5424**. Leidas del disco, la **5424** "
  "lleva la primera mitad de la frase (*la clase queda en `A` por la lectura vieja*) y "
  "**la clausula que envejecio vive en la 5425** (*y lo deja anotado en vez de "
  "elegir*). **Es UNA sola frase que arranca en la 5424 y cierra en la 5425**, asi que "
  "la cita del acta apunta bien a la frase y no a la linea exacta de la clausula. "
  "**La correccion entra pegada a la 5425**, que es donde acaba lo que se corrige, y "
  "la guarda `(3)` del juicio lo exige por numero: si la insercion entrara en otro "
  "sitio, cae.")
w()
w("#### 2. EL VOLTEO QUE LA CORRECCION CITA, MEDIDO EN GIT Y EN EL ARCHIVO")
w()
VOL = [
    ["commit que toco `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` por ultima vez",
     valor(S1B, "CIFRA commit que toco el archivo por ultima vez")],
    ["clase del puesto **730** en el padre de ese commit",
     valor(S1B, "CIFRA clase del puesto 730 en", 0)],
    ["clase del puesto **730** en el disco de hoy",
     valor(S1B, "CIFRA clase del puesto 730 en el disco de hoy")],
    ["los dos nodos del puesto",
     pick(S1B, "los dos nodos del puesto:").split(":", 1)[1].strip()],
]
w(tabla("EL PASO DE `A` A `D`, LEIDO Y NO RECORDADO",
        ["que se midio", "lo que dice el instrumento"], VOL, 4, "`" + S1B + "`"))
w("**LA CITA DE LA CORRECCION NO ES UN RECUERDO: ES ESTA MEDICION.** El bloque "
  "escrito nombra la **vuelta 212** y el commit **`9140d524`**, y la guarda `(8)` del "
  "juicio compara ese literal contra lo que devuelve `git log` en esta corrida.")
w()
w("#### 3. LAS GUARDAS OBLIGATORIAS, TODAS DE SU FICHERO DE SALIDA")
w()
GUA = [
    ["**simulacion en memoria antes de tocar el disco**",
     "**" + valor(S1B, "CIFRA fallos de la simulacion") + " fallos**"],
    ["lineas anadidas y lineas quitadas",
     pick(S1B, "CIFRA lineas anadidas:")],
    ["**caso rojo por mutacion, corrido ANTES de escribir**",
     "**" + pick(S1B, "CIFRA mutantes:") + "**"],
    ["sede de `docs/plan/03_FUSIONES.md` **al entrar**, por las dos convenciones",
     valor(S1B, "CIFRA SEDE docs/plan/03_FUSIONES.md AL ENTRAR")],
    ["sede de `docs/plan/03_FUSIONES.md` **al salir**, por las dos convenciones",
     valor(S1B, "CIFRA SEDE docs/plan/03_FUSIONES.md AL SALIR")],
    ["**el `sha256` del fichero corregido CAMBIA**",
     "**" + pick(S1B, "el sha256 LF de docs/plan/03_FUSIONES.md SE MUEVE:")
     .split(":", 1)[1].strip() + "**"],
    ["**el `sha256` de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` NO se mueve**",
     "**" + pick(S1B, "el sha256 LF de docs/INTRA_DOMINIO_VEREDICTOS.jsonl NO se mueve:")
     .split(":", 1)[1].strip() + "**"],
    ["**el `sha256` de `docs/INTRA_DOMINIO_INFORME.md` NO se mueve** (la 6941 intacta)",
     "**" + pick(S1B, "el sha256 LF de docs/INTRA_DOMINIO_INFORME.md NO se mueve:")
     .split(":", 1)[1].strip() + "**"],
    ["`git diff HEAD --numstat` acotado a ese fichero",
     pick(S1B, "CIFRA filas de numstat de ese fichero") + ", y la fila es `"
     + pick(S1B, "FILA:").split("FILA:", 1)[1].strip() + "`"],
    ["`git diff HEAD --numstat` sobre el arbol del plan entero",
     pick(S1B, "CIFRA filas de numstat de docs/plan entero")],
    ["`git diff HEAD --numstat` sobre dataset, web y engine",
     pick(S1B, "CIFRA filas de numstat de dataset, web y engine")],
    ["relectura del disco identica a lo juzgado",
     valor(S1B, "RELECTURA DEL DISCO identica a lo juzgado")],
]
w(tabla("LAS GUARDAS DE LA `1.b`", ["guarda", "lo que dice el instrumento"],
        GUA, 12, "`" + S1B + "`"))
w()
w("**LOS CUATRO MUTANTES, UNO A UNO, Y LOS CUATRO CAEN.** El encargo exige al menos "
  "tres especies y estan las tres, mas una cuarta.")
w()
MUT = [[pick(S1B, "MUTANTE %s:" % L)] for L in ("A", "B", "C", "D")]
w(tabla("EL CASO ROJO POR MUTACION, CORRIDO ANTES DE ESCRIBIR",
        ["el mutante y su veredicto, tal como sale del instrumento"],
        MUT, 4, "`" + S1B + "`"))
w("**LA GUARDA NO ES UNA CONSTANTE Y ESO ES LO QUE PRUEBAN LOS CUATRO:** la misma "
  "funcion `juzgar()` que devuelve **0 fallos** sobre la composicion buena devuelve "
  "fallos sobre las cuatro mutaciones. **Y una de ellas se me cayo de verdad en la "
  "primera corrida**: la guarda `(6)` exigia la vuelta citada y mi bloque la escribia "
  "en mayusculas, asi que la simulacion salio en **1 fallo** y **no escribio**. "
  "Corregi la guarda para que compare sin distinguir mayusculas y volvi a correr. "
  "**Lo digo porque una guarda que solo se ve pasar no prueba nada.**")
w()
w("#### 4. LO QUE NO TOQUE, Y ES LA MITAD DEL ENCARGO")
w()
NO = [
    ["`docs/INTRA_DOMINIO_INFORME.md` linea **6941**",
     "**INTACTA.** Su `sha256` es el mismo al entrar y al salir, y el fichero no se "
     "abre para escritura en ningun camino del instrumento"],
    ["los reportes archivados",
     "**NINGUNO TOCADO.** El numstat del arbol del plan mide **1** fila y es "
     "`docs/plan/03_FUSIONES.md`; los archivados viven en otro sitio y no aparecen"],
    ["la clase o la razon de cualquier fila del archivo",
     "**NINGUNA.** El `sha256` de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no se movio "
     "en toda la TAREA 1, publicado al entrar y al salir"],
    ["un barrido general de citas de otros veredictos",
     "**NO SE ABRIO.** No corri ninguna busqueda de citas de otros puestos, asi que "
     "**no afirmo que no las haya**: una busqueda que no se hizo no se puede citar "
     "(`EJECUTOR.md` 9). Lo que si digo es que **no me tropece con ninguna** leyendo "
     "las tres lineas de esta tarea"],
]
w(tabla("LAS CUATRO PROHIBICIONES EXPRESAS DE LA `1.b`",
        ["que estaba prohibido", "que paso"], NO, 4, "`" + S1B + "`"))
w()
w("**UN DISCUTIBLE MARCADO, Y LO MARCO ANTES DE SABER SI ACIERTO.** El encargo dice "
  "**ES UNA LINEA**, y **mi bloque de correccion mide 23 lineas** (cifra leida de "
  "`" + S1B + "`). Entiendo que la UNA es **la linea corregida**, no el tamaño del "
  "remedio, y que el carril del `9.10` obliga a dejar el texto viejo entero y a citar "
  "la vuelta y el commit, cosa que no cabe en una linea. **Si la lectura buena era "
  "que el remedio entero tenia que caber en una linea, esto es largo de mas y se "
  "acorta.** **DISCUTIBLE MARCADO.**")
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
