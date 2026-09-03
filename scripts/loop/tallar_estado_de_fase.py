# -*- coding: utf-8 -*-
r"""tallar_estado_de_fase.py . EL ESTADO DE UNA FASE DEJA DE SER UNA FRASE Y
PASA A SER UNA CIFRA COMPUTADA (TAREA 2.a de la vuelta 140, acta de la vuelta
139, seccion 4.1 y su escalada). Nombre estable, SIN numero de vuelta (como
tallar_cabecera_reporte.py y verificar_apertura_sellada.py): se invoca con
--fase y no se clona cada vuelta.

POR QUE NACE. La vuelta 139 publico "LA FASE 06 CIERRA SU CATALOGO" en su
cabecera y "hoy cierra" en su conclusion, y sobre esa frase pidio disparar el
pase de estado de seis operaciones. El auditor lo midio y no cerraba: el
catalogo de la fase 06 no son solo las seis fusiones, son tambien las CINCO
operaciones que la fase 04 le remitio en la vuelta 118, y esas tenian ONCE
aristas sin escribir. La racha de caidas de reporte llego a DOS y AUDITOR.md
1.2 obligo a encargar la escalada en la misma acta. La escalada literal de
EJECUTOR.md regla 1 (toda tabla tallada de su fichero) ya estaba hecha; la que
faltaba es esta: LA FRASE DE CIERRE DE UNA FASE SE COMPUTA, NO SE ESCRIBE.

QUE COMPRUEBA. Para una fase del 00_INDICE imprime UNA TABLA con, por
operacion de su catalogo: el id_op, su `estado` escrito en OPERACIONES.jsonl
(que se publica COMO CONTRASTE, nunca como veredicto), su `fase`, de donde
viene si es hija remitida y a que mesa fue remitida, y su DESTINO MEDIDO
CONTRA EL GRAFO. Cierra con una linea CIFRA y la lista NOMBRADA de las que no
cumplen.

EL CATALOGO DE UNA FASE, fijado por el auditor (acta 139, TAREA 2.a) para que
el instrumento no lo decida: son las operaciones cuyo campo `fase` es esa
fase, MAS las que otra fase le remitio POR ESCRITO. Los dos registros de
remision se LEEN DE SU FICHERO, no se teclean aqui:

  - docs/plan/00_INDICE.md, la fila que dice "enrutadas a la fase <N>": de ahi
    salen las SEIS fusiones que la fase 03 enruto a la fase 06.
  - docs/plan/04_ENLACES.md, seccion "SEGUNDA MITAD, LAS CINCO REMITIDAS A LAS
    MESAS DE LA FASE 06": de ahi salen las CINCO de la vuelta 118, con su
    mesa de destino.

Si un id remitido NO existe en OPERACIONES.jsonl, o una operacion aparece a la
vez con `fase` propia y como remitida desde otra, o hay ids duplicados en
OPERACIONES.jsonl, el instrumento CAE EN ROJO NOMBRANDOLA: fallar ruidoso,
nunca degradar en silencio (banco 9).

LAS VARAS DEL DESTINO, y de donde sale cada una:

  (1) FUSION. La escribe el encargo: "superviviente vivo con los absorbidos
      deprecados y en su ids_alias". Se aplica cuando `superviviente` es un id
      de nodo resoluble (patron de id y presente en el grafo). Absorbidos =
      `nodos` menos el superviviente.

  (2) ENLACE. La escribe el encargo: "cuantas de sus aristas_nuevas estan
      presentes hoy resolviendo por alias en las dos vistas". Se aplica cuando
      `aristas_nuevas` trae al menos un par `A -> B` parseable. Una arista
      cuenta como PRESENTE si, tras resolver los dos extremos por alias, esta
      en `nodos_siguientes` del origen O en `nodos_previos` del destino.
      Si una cadena de `aristas_nuevas` contiene "->" y NO produce ningun par,
      es ROJO nombrandola (una arista que el parser no ve es peor que ninguna).
      DESDE LA VUELTA 141 ESTA VARA MIDE TAMBIEN LA VUELTA: ver el bloque
      "LA VARA DE ENLACE APRENDE A MIRAR LA VUELTA" mas abajo.

  (3) MESA. ESTA VARA NO ESTA EN EL ENCARGO Y ES LECTURA MIA, DECLARADA AQUI Y
      MARCADA COMO DISCUTIBLE EN EL REPORTE DE LA VUELTA 140. Sale de dos
      cosas escritas: la fila 6 del 00_INDICE dice que la fase 06 "no tiene
      nada que hacer el dia de la pasada. SUS OPERACIONES HIJAS VIVEN EN LAS
      FASES 3 Y 4", y el campo `bloquea_a` de cada mesa NOMBRA a esas hijas.
      Una mesa tiene destino cumplido cuando TODAS sus hijas que estan en este
      catalogo lo tienen. Si una mesa no tiene NINGUNA hija en el catalogo, el
      destino NO SE DA POR CUMPLIDO: sale NO COMPUTABLE con sus hijas y la
      fase de cada una nombradas, para que se vea por que.
      DESDE LA VUELTA 141 LA NOMINA DE UNA MESA SON SUS DOS FUENTES UNIDAS:
      ver el bloque "EL CATALOGO DE UNA MESA UNE SUS DOS FUENTES" mas abajo.

  (4) SIN VARA ESCRITA. Todo lo demas. NO HAY REGLA ESCRITA que mida contra el
      grafo el destino de una VIGENCIA, una HERRAMIENTA, un CAMPO_SUCIO, un
      RENOMBRE_CON_ALIAS, un REENCUADRE_DE_MARCO o un SANEO MECANICO, y
      EJECUTOR.md regla 5 prohibe inventarla. El instrumento NO se calla y NO
      la da por buena: sale NO COMPUTABLE, se cuenta en SIN CUMPLIR y se
      nombra en el desglose `de ellas, sin vara escrita`.

      EL PUNTERO DE LA FASE 07, Y SOLO UN PUNTERO (vuelta 145, TAREA 3.b; acta
      144, adjudicacion 3.9). Las DOS operaciones de `07_ADUANA` (`OP-A-01` y
      `OP-A-02`) tienen `nodos`, `superviviente`, `eliminar` y `aristas_nuevas`
      VACIOS los cuatro, asi que salen aqui en SIN VARA ESCRITA y NO COMPUTABLE,
      y ESO ES CORRECTO: no dejan huella en el grafo y esta es una vara de
      grafo. Se miden APARTE, contra LO QUE INSTALAN, con
      `scripts/loop/vuelta145_3b_vara_de_codigo_fase07.py`, que pregunta por
      cada control DOS COSAS Y SOLO DOS: que exista en el codigo y que muerda
      por mutacion.

      ESE VEREDICTO NO ENTRA EN ESTA TABLA NI EN NINGUNA COLUMNA SUYA, y la
      razon se escribe para que nadie lo "arregle" luego: el contrato de esta
      columna es "destino medido contra el grafo", y meter ahi un veredicto de
      CODIGO serian DOS UNIDADES EN UNA COLUMNA, la especie exacta de la
      CORRECCION 18. La celda de las dos sigue diciendo SIN VARA ESCRITA, que
      es la verdad medida contra el grafo, y quien quiera el otro veredicto
      corre el otro instrumento.

POR QUE "NO COMPUTABLE" CUENTA COMO "SIN CUMPLIR", y es la decision que mas
manda en la cifra: "destino cumplido" es una AFIRMACION, y una operacion cuyo
destino no se puede medir NO HA SIDO DEMOSTRADA cumplida. Meterla en el saco
de las cumplidas seria exactamente la degradacion silenciosa que el banco 9
prohibe, y seria ademas la especie de la caida 4.1 (una frase de cierre sin
instrumento detras). El desglose se publica al lado para que nadie confunda
"no cumplida" con "no medible".

EL CAMPO `estado` NO ES VARA DE NADA. Se imprime como columna de CONTRASTE
porque EJECUTOR.md regla 2 manda declarar la discrepancia en vez de
resolverla copiando, pero ninguna cifra de este instrumento lo mira.

USO:
  python scripts/loop/tallar_estado_de_fase.py --fase 06_MESAS
  python scripts/loop/tallar_estado_de_fase.py --fase 05_SANEO --ref <commit>
  python scripts/loop/tallar_estado_de_fase.py --fases

--ref fija el grafo Y el OPERACIONES.jsonl Y los dos registros de remision en
un commit, para poder correr sobre SUJETO CONGELADO (banco 9.10: un sujeto que
se mueve solo no prueba nada). Por defecto WORK, el arbol de trabajo.

--- LA VARA DE ENLACE APRENDE A MIRAR LA VUELTA (TAREA 2.a, vuelta 141) ---

POR QUE NACE (acta de la vuelta 140, caida 4.1, "DE GUARDA QUE NO ALCANZA, Y ES
LA GRANDE DE HOY"). La vara ENLACE contaba cuantas `aristas_nuevas` estan
presentes y NUNCA miraba si la VUELTA estaba. Una fila cuya ida ya estaba puesta
salia como "YA PRESENTE" y la vara paraba ahi. Consecuencia medida por el
auditor: OP-E-04 no tenia TRES filas en violacion de su propia verificacion 0,
tenia CINCO (LD-35, LD-42, LD-48, LD-49 y LD-51), y DOS de esas vueltas las
escribio la vuelta 140 con OP-E-05, que la misma tabla publicaba como CUMPLIDA.
"YA PRESENTE" NO ES UN VEREDICTO: ES MEDIA MEDICION.

QUE HACE AHORA, Y DE DONDE SALE CADA COSA. La vara lee TAMBIEN la `verificacion`
de la ficha y clasifica su REGIMEN DE VUELTA en uno de tres, SIN mirar el campo
`tipo` (el encargo lo prohibe expresamente: la excepcion va escrita, no
adivinada del tipo):

  - PROHIBE. Alguna linea de `verificacion` dice que la vuelta no debe existir.
    Las tres formas que el plan usa hoy, LITERALES de las fichas y por eso
    escritas aqui como frases y no como una heuristica:
      * "la vuelta no debe existir"        (OP-E-04 v0, OP-M-01-SEXTO v2)
      * "la vuelta no existe ni literal ni resuelta"  (OP-M-01-ESLABONES v0,
                                                       OP-M-04 v7)
      * "la vuelta es una instruccion falsa"          (OP-M-03-ENLACES v0)
    En este regimen la operacion SOLO cumple si, para CADA una de sus
    direcciones, la IDA esta presente Y la VUELTA NO lo esta, medido con el
    resolutor puesto en las DOS VISTAS.

  - MUTUO. Alguna linea de `verificacion` declara la excepcion del BANCO 9.22
    ("La regla de la escalera vale para las ESCALERAS, no para los enlaces
    mutuos", hueco de orden 1 del 00_INDICE; y el 9.22: "ENLACE MUTUO: dos
    aristas, una por cada linea expandida"). Las formas literales:
      * "la vuelta si existe"             (OP-E-05 v0)
      * "es un enlace mutuo"              (OP-E-05 v0)
      * "la regla de la escalera no aplica" (OP-E-05 v0)
    En este regimen la vara EXIGE las dos direcciones (que ya vienen las dos en
    `aristas_nuevas`) y NO PENALIZA la vuelta.

  - SIN REGLA. Ninguna linea dice nada de la vuelta. La vara NO INVENTA una
    (EJECUTOR.md regla 5): mide la ida como siempre, MIDE la vuelta igual y la
    PUBLICA, pero no la usa para el veredicto, y lo dice en la celda.

Si una misma ficha trae las dos clases de frase, es ROJO nombrandola: una ficha
que prohibe y exige la vuelta a la vez no se resuelve adivinando.

Y LA COLUMNA DE DESTINO PUBLICA, POR OPERACION, cuantas direcciones tienen la
IDA presente y CUANTAS TIENEN LA VUELTA PRESENTE, nombrandolas las dos veces.

--- LA CELDA PUBLICA UNA SOLA UNIDAD (TAREA 2.c, vuelta 141) ---

POR QUE NACE (acta de la vuelta 140, adjudicacion 3.4). La celda de OP-E-04
decia "4 de 9 presentes" (numerador en FILAS DE FICHA) y a continuacion listaba
5 faltantes (DIRECCIONES distintas): 4 mas 5 da 9 filas cuando solo hay 8
direcciones. Dos unidades en una celda.

LA UNIDAD ADJUDICADA ES LA DIRECCION ("es lo que el grafo guarda y lo que la
vara mide, y la cadena esconde el enlace mutuo"). Desde la vuelta 141 el
NUMERADOR Y EL DENOMINADOR de la celda son DIRECCIONES distintas tras resolver;
las filas de ficha se siguen publicando, pero SIEMPRE NOMBRADAS COMO TALES
("N filas de ficha"), y cuando colapsan se dice en cuantas.

--- EL CATALOGO DE UNA MESA UNE SUS DOS FUENTES (TAREA 2.b, vuelta 141) ---

POR QUE NACE (acta de la vuelta 140, adjudicacion 3.1). `bloquea_a` NO es la
nomina completa de una mesa: OP-M-01.bloquea_a nombra OP-E-04, OP-E-05,
OP-M-01-ESLABONES, OP-M-01-FUSION y OP-S-12, y NO nombra OP-M-01-SEXTO, que la
tabla de remision de docs/plan/04_ENLACES.md manda expresamente a OP-M-01. Hoy
no mueve la cifra (OP-M-01 cae igual por OP-E-04), pero el dia que solo falte la
sexta la mesa cerraria con una hija fuera.

QUE HACE AHORA. La nomina de una mesa es la UNION de dos fuentes:
  (1) su campo `bloquea_a`, y
  (2) la COLUMNA DE DESTINO de la tabla de remision, PARSEADA de
      docs/plan/04_ENLACES.md por leer_remisiones() y no tecleada aqui.
La celda publica DE DONDE SALE CADA HIJA: "bloquea_a", "remision" o "las dos".

--- LA VARA FUSION APRENDE EL TERCER VEREDICTO (TAREA 2.c, vuelta 142) ---

POR QUE NACE (acta de la vuelta 141, adjudicacion 3.5, y es lo mas importante
que el auditor trajo esa vuelta). El reporte de la vuelta 141 propuso ENSANCHAR
esta vara pasando el `superviviente` por el resolutor y quedarse con lo que
saliera. EL AUDITOR LO MIDIO Y ESO PUBLICA UN VERDE FALSO:

  - OP-M-02-ADMIT: `superviviente` `fase_admit`, `eliminar`
    ["fase_admit_celebracion"]. Hoy `fase_admit` esta DEPRECADO y resuelve a
    `fase_admit_celebracion`, QUE ESTA VIVO.
  - OP-M-02-MEDIOS: `superviviente` `seis_medios_comunicacion_cliente`,
    `eliminar` ["estrategia_multicanal_bienvenida"]. Hoy el superviviente esta
    DEPRECADO y resuelve a `estrategia_multicanal_bienvenida`, QUE ESTA VIVO.

EN LAS DOS, EL QUE SOBREVIVE ES EL QUE LA FICHA MANDA ELIMINAR. Resolver a secas
y llamarlas CUMPLIDAS seria publicar CUMPLIDO sobre una operacion ejecutada al
reves, o sea la degradacion silenciosa del banco 9 por la puerta de un arreglo
que parece obvio. Y las TRES que COINCIDEN (ASSESS, ACTIVATE, ACCOMPLISH) ya
salian cumplidas sin resolutor, asi que el resolutor a secas silenciaria SOLO
los dos casos que merecen ruido.

LA EXCEPCION VA ESCRITA Y CITADA, NO ADIVINADA. Las dos cosas que la sostienen
existen desde la vuelta 64 y no son doctrina nueva:
  (1) el campo `nota` de las dos fichas lleva la CORRECCION DECLARADA de la
      vuelta 64: "ESTA FICHA ESTA CONSUMIDA. NO SE EJECUTA Y NO SE REHACE";
  (2) docs/loop/SALIDA_V64_CONSUMIDAS.txt computa CINCO fusiones de mesa
      consumidas, de las cuales DOS DIVERGEN (MEDIOS y ADMIT) y TRES COINCIDEN
      (ASSESS, ACTIVATE, ACCOMPLISH), con el criterio ya escrito alli: "el par
      resuelve a UN solo vivo" mas "DIVERGEN: la ficha decia X y el tramo dejo
      vivo a Y".
Y el resolutor se usa porque EJECUTOR.md regla 9 con P.1 lo mandan ("todo conteo
que toque ids pasa por el resolutor antes de contar"): la vara SI resuelve; lo
que no puede es quedarse solo con eso.

LOS TRES CASOS QUE LA VARA CLASIFICA AHORA:
  - superviviente escrito VIVO y absorbidos deprecados y en su ids_alias:
    CUMPLIDO, como siempre.
  - superviviente escrito DEPRECADO que resuelve a un VIVO que la propia ficha
    lista en `eliminar`: CONSUMIDA CON SUPERVIVIENTE DIVERGENTE, NUNCA cumplido,
    y la celda publica el id escrito, el id al que resuelve y el campo
    `eliminar` que lo condena.
  - superviviente DEPRECADO que resuelve a un VIVO que NO esta en `eliminar`:
    CONSUMIDA, se nombra, y tampoco se llama cumplida.

DONDE VA EL TERCER VEREDICTO EN LA CIFRA, Y POR QUE NO SALE DE `SIN CUMPLIR`.
La adjudicacion dice "NO ES CUMPLIDA NI SIN CUMPLIR", y eso se cumple EN SU
COLUMNA DE VEREDICTO, que publica su rotulo propio. En la CIFRA, en cambio, va
como SUB-SACO NOMBRADO dentro de `sin cumplir`, igual que `sin vara escrita`
desde la vuelta 140, y por la misma razon ya adjudicada (acta 140, 3.2: "NO
COMPUTABLE cuenta como SIN CUMPLIR"). EL MOTIVO ES MEDIBLE Y NO ES DE ESTILO:
verificar_cifras_del_reporte.py juzga las AFIRMACIONES DE CIERRE leyendo la
linea `sin cumplir: N` de esta salida y su lista `SIN CUMPLIR (N):`. Si una
DIVERGENTE saliera de ahi, una fase con una operacion EJECUTADA AL REVES dentro
publicaria `sin cumplir: 0` y la frase "la fase cierra" pasaria la guarda. Eso
es exactamente la degradacion silenciosa que este tercer veredicto nace para
impedir, entrando por la otra puerta. La CIFRA publica los dos sub-sacos con su
nombre y su nomina, para que nadie confunda "no cumplida" con "no medible" ni
con "consumida al reves".

CONSECUENCIA MEDIDA Y TRAIDA COMO PARADA (vuelta 142): el encargo esperaba que
los cuatro "de mas" de vuelta141_2e_caso_positivo_fase03.py bajaran a DOS. NO
BAJAN: siguen siendo cuatro, porque OP-M-02-ADMIT y OP-M-02-MEDIOS siguen
dentro de `sin cumplir` por lo de arriba, aunque ahora lleven el rotulo
DIVERGENTE. Se dice, se mide y no se ajusta.

MUTACIONES: scripts/loop/vuelta142_2c_mutaciones.py, EN MEMORIA y nunca en
disco, sobre una operacion ELEGIDA POR COMPUTO (la primera FUSION hoy CUMPLIDA
de la fase, por orden del catalogo) y nunca tecleada.

LAS MUTACIONES viven en scripts/loop/vuelta140_2a_mutaciones.py, que importa
este modulo y muta EN MEMORIA (nunca el disco). Las tres, todas sobre cifra
COMPUTADA y nunca sobre un literal (EJECUTOR.md regla 1, "EL CASO ROJO SE
PRUEBA POR MUTACION"):
  (i)   se le quita una arista presente al grafo en memoria: "con destino
        cumplido" tiene que BAJAR y la operacion tiene que salir NOMBRADA;
  (ii)  se mete en el catalogo una remitida de mentira que no existe en
        OPERACIONES.jsonl: ROJO nombrandola;
  (iii) caso positivo sobre sujeto congelado: la fase 05, cerrada desde la
        vuelta 136.

--- ADJUDICACION 6.10 DEL ACTA 155 (3 sep 2026): UN `--fase` QUE NO CALCE
EXACTAMENTE ES ROJO Y EXIT DISTINTO DE CERO ---

CORRECCION DECLARADA POR ADICION. NADA DEL TEXTO ANTERIOR SE BORRA.

EL HALLAZGO, MEDIDO POR EL AUDITOR EL 3 SEP 2026 Y SIN TUBERIA (la tuberia fue
su propia caida 2 y la declara): `--fase 06_MESAS` daba 16 del catalogo, 16
cumplidas, 0 sin cumplir y EXIT 0; `--fase 06` daba 11 DEL CATALOGO, 11
cumplidas, 0 sin cumplir, EXIT 0 Y NI UNA QUEJA (cero propias, once recogidas
por remision, porque `leer_remisiones` recorta el nombre de fase a su NUMERO y
ese numero si casa). EL CATALOGO COMPLETAMENTE VACIO SI ESTABA CAZADO
(`--fase NO_EXISTE`: ROJO y EXIT 1, por el fallo de `medir`); EL CATALOGO
PARCIAL POR UN NOMBRE QUE NO EXISTE, NO.

POR QUE IMPORTA Y NO ES TEORICO: es UN VERDE SOBRE UN UNIVERSO INCOMPLETO, la
misma especie exacta del hallazgo de OP-C-05 del acta 153. Y este instrumento
es el que midio el disparador que movio cinco fichas a HECHA, el que mide la
celda de la fila 03 de la tabla por fase y el muro de la fase 08, y es contra
el que `scripts/loop/verificar_cifras_del_reporte.py` coteja las afirmaciones
de cierre del reporte.

LO QUE SE ADJUDICA, POR EXTENSION DEL BANCO 9 (FALLAR RUIDOSO) Y SIN DOCTRINA
NUEVA: es la misma regla que ya caza el catalogo vacio, aplicada al catalogo
MUTILADO. `--fase X` donde X no sea EXACTAMENTE uno de los nombres de fase que
`docs/plan/OPERACIONES.jsonl` trae es ROJO Y EXIT DISTINTO DE CERO, con la
nomina de los nombres validos impresa al lado para que el rojo se pueda
arreglar sin adivinar.
"""
import argparse
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REL_GRAFO = "dataset/metadata/master_graph.json"
REL_OPS = "docs/plan/OPERACIONES.jsonl"
REL_INDICE = "docs/plan/00_INDICE.md"
REL_ENLACES = "docs/plan/04_ENLACES.md"

PATRON_ID_NODO = re.compile(r"^[a-z0-9_]+$")
PATRON_ARISTA = re.compile(r"([a-z0-9_]+)\s*->\s*([a-z0-9_]+)")
PATRON_OP = re.compile(r"OP-[A-Z0-9]+(?:-[A-Z0-9]+)*")

# EL TERCER VEREDICTO DE LA VARA FUSION (TAREA 2.c, vuelta 142). Las dos marcas
# viven aqui, en un solo sitio, porque las escribe destino_de_fusion() y las
# vuelven a leer medir() e imprimir(): dos copias del mismo rotulo se
# desincronizarian el dia que una cambie.
MARCA_DIVERGENTE = "CONSUMIDA CON SUPERVIVIENTE DIVERGENTE"
MARCA_CONSUMIDA = "CONSUMIDA:"


# ------------------------------------------------------------------ lectura

def leer_ruta(ref, rel):
    """Lee un fichero del arbol de trabajo (ref WORK) o de un commit."""
    if ref == "WORK":
        with io.open(os.path.join(RAIZ, rel), encoding="utf-8") as f:
            return f.read()
    r = subprocess.run(["git", "show", "%s:%s" % (ref, rel)], cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO (arnes): no se pudo leer %s en %s" % (rel, ref))
    return r.stdout.decode("utf-8")


def cargar_grafo(ref="WORK"):
    return json.loads(leer_ruta(ref, REL_GRAFO))["nodos"]


def cargar_ops(ref="WORK"):
    ops = []
    for linea in leer_ruta(ref, REL_OPS).splitlines():
        if linea.strip():
            ops.append(json.loads(linea))
    return ops


# --------------------------------------------------------------- remisiones

def leer_remisiones(fase, ref="WORK"):
    """Los dos registros de remision, LEIDOS DE SU FICHERO. Devuelve
    {id_op: {'de': <fase origen o None>, 'a': <mesa o None>, 'fuente': <cita>}}.

    NO se teclea ninguna nomina aqui: si un registro se reescribe, este
    instrumento lo sigue."""
    rem = {}
    numero = fase.split("_")[0].lstrip("0") or "0"

    # (1) 00_INDICE.md: la fila "enrutadas a la fase <N>".
    patron_fila = re.compile(r"enrutadas a la fase 0*%s\b" % re.escape(numero))
    for i, linea in enumerate(leer_ruta(ref, REL_INDICE).splitlines(), 1):
        if patron_fila.search(linea):
            for x in PATRON_OP.findall(linea):
                rem.setdefault(x, {"de": None, "a": None,
                                   "fuente": "%s:%d" % (REL_INDICE, i)})

    # (2) 04_ENLACES.md: la tabla de la seccion de las remitidas a las mesas.
    texto = leer_ruta(ref, REL_ENLACES).splitlines()
    cabecera = re.compile(r"LAS CINCO REMITIDAS A LAS MESAS DE LA FASE 0*%s\b" % re.escape(numero))
    dentro = False
    for i, linea in enumerate(texto, 1):
        if cabecera.search(linea):
            dentro = True
            continue
        if not dentro:
            continue
        if linea.startswith("|"):
            celdas = [c.strip().strip("`") for c in linea.strip().strip("|").split("|")]
            if len(celdas) >= 2 and PATRON_OP.fullmatch(celdas[0] or ""):
                mesa = celdas[1] if PATRON_OP.fullmatch(celdas[1] or "") else None
                rem[celdas[0]] = {"de": None, "a": mesa,
                                  "fuente": "%s:%d" % (REL_ENLACES, i)}
        elif linea.strip().startswith("#") or linea.strip().startswith("**SEGUNDA"):
            if rem:
                dentro = False
    return rem


# ----------------------------------------------------------------- catalogo

def construir_catalogo(fase, ops, remisiones, fallos):
    """Las de `fase` propia MAS las remitidas por escrito. ROJO nombrando si
    algo no se puede resolver sin decidir."""
    por_id = {}
    for o in ops:
        x = o.get("id_op")
        if x in por_id:
            fallos.append("%s aparece DOS VECES en %s: catalogo ambiguo" % (x, REL_OPS))
        por_id[x] = o

    propias = [o["id_op"] for o in ops if o.get("fase") == fase]
    catalogo = list(propias)

    for x, meta in sorted(remisiones.items()):
        if x not in por_id:
            fallos.append("%s esta REMITIDO a la fase %s por %s y NO EXISTE en %s: "
                          "no se puede medir su destino" % (x, fase, meta["fuente"], REL_OPS))
            continue
        if x in propias:
            fallos.append("%s tiene fase propia %s Y aparece remitido a la fase %s por %s: "
                          "no se puede resolver a que fase pertenece sin decidir"
                          % (x, fase, fase, meta["fuente"]))
            continue
        meta["de"] = por_id[x].get("fase")
        catalogo.append(x)

    return catalogo, por_id


# --------------------------------------------------------------- resolutor

def resolver_de(nodos):
    """El resolutor de alias de la casa (P.1), igual que en
    verificar_aristas_vivas.py y verificar_fusion_ops09.py."""
    alias = {}
    for nid, n in nodos.items():
        if n.get("deprecado"):
            continue
        for x in (n.get("ids_alias") or []):
            alias[x] = nid

    def resolver(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x
    return resolver


def vivo(n):
    return n is not None and not n.get("deprecado")


def arista_presente(nodos, resolver, origen, destino):
    """Presente si, tras resolver los dos extremos por alias, esta en
    nodos_siguientes del origen O en nodos_previos del destino."""
    o, d = resolver(origen), resolver(destino)
    no, nd = nodos.get(o), nodos.get(d)
    if not vivo(no) or not vivo(nd) or o == d:
        return False, o, d
    if any(resolver(x) == d for x in (no.get("nodos_siguientes") or [])):
        return True, o, d
    if any(resolver(x) == o for x in (nd.get("nodos_previos") or [])):
        return True, o, d
    return False, o, d


# ------------------------------------------------------------------ destino

def pares_de_aristas(op, fallos):
    pares = []
    for s in (op.get("aristas_nuevas") or []):
        hallados = PATRON_ARISTA.findall(s)
        if "->" in s and not hallados:
            fallos.append("%s: una cadena de aristas_nuevas trae '->' y el parser no "
                          "saca ningun par: %s" % (op.get("id_op"), s[:120]))
        pares.extend(hallados)
    return pares


def destino_de_fusion(op, nodos, fallos, resolver=None):
    """TAREA 2.c de la vuelta 142. Ver el bloque "LA VARA FUSION APRENDE EL
    TERCER VEREDICTO" del docstring del modulo.

    Devuelve (cumplido, razon), donde `cumplido` es True, False o None. El
    tercer veredicto NO es True nunca: `CONSUMIDA CON SUPERVIVIENTE DIVERGENTE`
    y `CONSUMIDA` salen con `cumplido` False y la razon los nombra entera."""
    sup = op.get("superviviente")
    absorbidos = [x for x in (op.get("nodos") or []) if x != sup]
    n_sup = nodos.get(sup)
    if not vivo(n_sup):
        # EL SUPERVIVIENTE ESCRITO NO ESTA VIVO. Antes de la vuelta 142 la vara
        # paraba aqui con "NO esta vivo hoy" y no decia mas. Ahora RESUELVE
        # (EJECUTOR.md regla 9, P.1) y publica cual de los dos casos es, sin
        # llamar CUMPLIDO a ninguno.
        if resolver is None:
            return False, "superviviente %s NO esta vivo hoy" % sup
        destino = resolver(sup)
        n_dest = nodos.get(destino)
        eliminar = list(op.get("eliminar") or [])
        if destino == sup or not vivo(n_dest):
            return False, ("superviviente %s NO esta vivo hoy y el resolutor (P.1) no lleva "
                           "a ningun nodo vivo (resuelve a %s)" % (sup, destino))
        if destino in eliminar:
            return False, (
                MARCA_DIVERGENTE + ": el `superviviente` escrito en la "
                "ficha es %s, hoy DEPRECADO; resuelve por alias (P.1) a %s, que esta VIVO; "
                "y %s es justamente uno de los que el campo `eliminar` de esta misma ficha "
                "manda eliminar (eliminar: %s). NO ES CUMPLIDA NI SIN CUMPLIR: la operacion "
                "se ejecuto al reves. Ver la correccion declarada de la vuelta 64 en el "
                "`nota` de la ficha (\"ESTA FICHA ESTA CONSUMIDA. NO SE EJECUTA Y NO SE "
                "REHACE\") y docs/loop/SALIDA_V64_CONSUMIDAS.txt, que computa cinco "
                "consumidas de las cuales dos DIVERGEN"
                % (sup, destino, destino, ", ".join(eliminar) or "vacio"))
        return False, (
            MARCA_CONSUMIDA + " el `superviviente` escrito en la ficha es %s, hoy DEPRECADO; resuelve "
            "por alias (P.1) a %s, que esta VIVO y NO esta en el campo `eliminar` de la ficha "
            "(eliminar: %s). El par resuelve a un solo vivo, pero NO es el superviviente "
            "escrito: se nombra y NO se llama cumplida"
            % (sup, destino, ", ".join(eliminar) or "vacio"))
    alias_sup = set(n_sup.get("ids_alias") or [])
    faltas = []
    for x in absorbidos:
        n = nodos.get(x)
        if n is None:
            faltas.append("%s no existe en el grafo" % x)
            continue
        if not n.get("deprecado"):
            faltas.append("%s NO esta deprecado" % x)
        if x not in alias_sup:
            faltas.append("%s no esta en ids_alias de %s" % (x, sup))
    if faltas:
        return False, "%d absorbido(s) OK de %d; %s" % (
            len(absorbidos) - len({f.split()[0] for f in faltas}), len(absorbidos),
            "; ".join(faltas))
    return True, "superviviente %s vivo, %d absorbido(s) deprecado(s) y en ids_alias" % (
        sup, len(absorbidos))


# ------------------------------------------- el regimen de vuelta de la ficha

# TAREA 2.a (vuelta 141). Las frases van LITERALES de las fichas del plan, no
# como heuristica: ver el bloque "LA VARA DE ENLACE APRENDE A MIRAR LA VUELTA"
# del docstring, donde cada una lleva la ficha y la linea de la que sale.
FRASES_PROHIBE_VUELTA = [
    "la vuelta no debe existir",
    "la vuelta no existe ni literal ni resuelta",
    "la vuelta es una instruccion falsa",
]
# La excepcion del BANCO 9.22, ESCRITA y no adivinada del campo `tipo`:
# "La regla de la escalera vale para las ESCALERAS, no para los enlaces mutuos"
# (00_INDICE, hueco de orden 1), y "ENLACE MUTUO: dos aristas, una por cada
# linea expandida" (banco 9.22).
FRASES_MUTUO = [
    "la vuelta si existe",
    "es un enlace mutuo",
    "la regla de la escalera no aplica",
]

# --------------- EL REGIMEN DE VUELTA PASA A SER POR PAR (TAREA 2.a, v143) ---
#
# POR QUE NACE (acta de la vuelta 142, adjudicacion 3.3 y caida 4.3 de la casa,
# "LA VARA DE ENLACE NO LEE LA EXCEPCION QUE LA 3.a ACABA DE ESCRIBIR, ASI QUE
# LA FASE 06 NO PUEDE CERRAR NUNCA").
#
# EL DEFECTO, MEDIDO POR EL AUDITOR CON EL ARBOL EN LAS DOS POSICIONES: corrio
# tallar_estado_de_fase.py --fase 06_MESAS CON la excepcion de la vuelta 142
# puesta y con esa misma excepcion guardada en git stash, y la celda de OP-E-04
# sale IDENTICA en las dos ("regimen de vuelta PROHIBE por la ficha
# (verificacion 0): la vuelta presente IMPIDE cumplir"). La causa esta en el
# codigo de arriba: regimen_de_vuelta() clasificaba POR OPERACION contra seis
# frases literales, y el texto de la excepcion no lleva ninguna de las de MUTUO.
# Y SI LA LLEVARA, SALDRIA AMBIGUO CON FALLO, porque la verificacion 0 de la
# misma ficha sigue entera y prohibiendo. O sea: NO HABIA REDACCION POSIBLE que
# arreglara esto mientras el regimen fuera uno por operacion. Consecuencia
# medida: OP-E-04 no podia llegar a CUMPLIDA ni ejecutando su ficha entera,
# "sin cumplir" nunca bajaba de 1 y la fase 06 no podia cerrar nunca.
#
# NO ES DOCTRINA NUEVA. El banco 9.22 define la figura POR PAR ("La figura exige
# dos lineas distintas, una en cada nodo", "El par es sano"), y el hueco de
# orden 1 del 00_INDICE:482 exige literal "LA GUARDA TIENE QUE LLEVAR LA
# EXCEPCION ESCRITA".
#
# QUE CAMBIA, EN TRES PIEZAS:
#
# (i) LA FICHA PUEDE DECLARAR PARES EXCEPTUADOS Y LA VARA LOS LEE. La excepcion
#     se lee de la `verificacion` de la ficha, NUNCA del campo `tipo` y NUNCA
#     adivinada. La frase que la dispara va LITERAL de la ficha, igual que las
#     seis de la vuelta 141: sale de la verificacion 5 de OP-E-04 (la sexta
#     linea), escrita en la vuelta 142 y commiteada en la 143, cuyo primer
#     renglon dice "EXCEPCION DEL 9.22 PARA LOS PARES MUTUOS NOMBRADOS".
#
#     LOS PARES SE PARSEAN DE LA VENTANA QUE LA PROPIA FICHA DELIMITA CON SUS
#     PALABRAS, y esto se declara aqui porque es una decision de lectura: la
#     ficha adjudica con la formula "adjudico DOBLE LINEA los pares de LD-35 con
#     LD-51, de LD-49, de LD-40 con LD-48 y de LD-45 con LD-53, y ESCALERA el de
#     LD-42". La ventana va del literal "DOBLE LINEA" al literal "y ESCALERA", y
#     SOLO de ahi se sacan pares. NO SE LEEN LOS LD DE LA LINEA ENTERA, y el
#     motivo es medible: la misma frase nombra LD-42 como ESCALERA, o sea como
#     el par que la excepcion EXPRESAMENTE NO cubre; leer la linea entera lo
#     colaria dentro y la excepcion se tragaria justo el caso que niega.
#
#     DENTRO DE LA VENTANA SE ACEPTAN LAS DOS FORMAS que el encargo nombra, "por
#     sus ids o por sus LD": un LD-<n> se traduce a par de nodos buscandolo en
#     el propio aristas_nuevas de la ficha (la fila que dice "por LD-<n>"), y
#     una flecha "A -> B" escrita dentro de la ventana se toma tal cual. Las dos
#     formas SE RESUELVEN POR ALIAS (P.1, EJECUTOR.md regla 9) antes de
#     comparar, y el par se guarda SIN ORDEN, porque un par exceptuado lo esta
#     en sus dos sentidos.
#
#     SI LA FICHA DISPARA LA EXCEPCION Y NO SE PUEDE SACAR NI UN PAR, ES FALLO
#     RUIDOSO (banco 9) y no se aplica ninguna excepcion: una excepcion que no
#     nombra pares es exactamente el caso que (ii) reserva para AMBIGUO.
#
# (ii) EL REGIMEN DEJA DE SER UNO POR OPERACION. Una operacion con excepcion
#     tiene regimen PROHIBE para las direcciones cuyo par NO esta exceptuado, y
#     MUTUO para las de los pares que SI lo estan. Una operacion SIN excepcion
#     se comporta EXACTAMENTE como antes de esta vuelta, y su celda sale con el
#     mismo texto (eso es lo que prueba la mutacion (iii) de
#     vuelta143_2a_mutaciones.py). LLEVAR PROHIBE Y UNA EXCEPCION NOMBRADA A LA
#     VEZ DEJA DE SER AMBIGUO: eso es justo lo que el hueco de orden 1 manda que
#     exista. AMBIGUO queda reservado a la ficha que prohibe y exige la vuelta
#     SIN nombrar pares.
#
# (iii) LA CELDA PUBLICA EL DESGLOSE Y NO UN TOTAL PELADO: cuantas direcciones
#     bajo PROHIBE tienen la vuelta presente (las que impiden cumplir), cuantas
#     bajo MUTUO tienen sus dos direcciones (las que se exigen), y la NOMINA de
#     los pares exceptuados que la ficha nombra, para que se vea crecer.
#
# MUTACIONES: scripts/loop/vuelta143_2a_mutaciones.py, todas EN MEMORIA y con el
# sujeto ELEGIDO POR COMPUTO, nunca tecleado.
FRASES_EXCEPCION_PAR = [
    "excepcion del 9.22 para los pares mutuos nombrados",
]
# Los dos literales con los que la propia ficha delimita su adjudicacion.
# LA VUELTA 144 LOS SUSTITUYE POR LA FORMULA CANONICA. Los viejos quedan
# escritos aqui, sin borrar, porque la CORRECCION 19 se apoya en ellos:
#     MARCA_ABRE_EXCEPCION   = "doble linea"     (hasta la vuelta 143)
#     MARCA_CIERRA_EXCEPCION = "y escalera"      (hasta la vuelta 143)
# Ver el bloque "LA FORMULA CANONICA DE LA EXCEPCION" justo debajo.
# --------------- LA FORMULA CANONICA DE LA EXCEPCION (TAREA 2.a, v144) -------
#
# POR QUE NACE (acta de la vuelta 143, adjudicacion 3.1 y caidas de la casa 4.2
# y 4.3; CORRECCION 19 de docs/plan/CORRECCIONES_A_APLICAR.md). La lectura que
# la vuelta 143 escribio arriba delimitaba la ventana con DOS LITERALES DEL
# PROPIO VOCABULARIO DEL 9.22 ("doble linea" para abrir, "y escalera" para
# cerrar). Esos dos literales pueden salir, y salen, en la PROSA QUE EXPLICA la
# excepcion, no solo en la formula que la adjudica. De ahi los dos agujeros,
# los dos medidos y los dos hacia el lado permisivo:
#
#   (A) EL CIERRE. `ventana = linea[ini:fin] if fin > ini else linea[ini:]`. Si
#       falta el literal de cierre, `find` da -1 y LA VENTANA SE ENSANCHA HASTA
#       EL FINAL DE LA LINEA SIN DECIR NADA. Medido (vuelta 144,
#       scripts/loop/vuelta144_1b_medir_ventana.py): quitado "y ESCALERA" en
#       memoria, los pares exceptuados suben de 4 a 5 CON CERO FALLOS, y el que
#       entra es revision_portafolio_periodica con sistema_gates_go_kill, o sea
#       EXACTAMENTE EL PAR QUE LA EXCEPCION NIEGA POR ESCRITO (el LD-42 que la
#       ficha adjudica como ESCALERA). Habia fallo ruidoso para la apertura
#       ausente y para el caso de cero pares; para el cierre ausente no lo
#       habia.
#
#   (B) LA APERTURA. `bajo.find(MARCA_ABRE_EXCEPCION)` toma la PRIMERA
#       ocurrencia. Medido sobre esa misma linea: "doble linea" aparece en las
#       posiciones 381 y 859; LA VENTANA REAL ARRANCABA EN 381, dentro de la
#       prosa del punto (1), no en 859, que es donde vive la formula. Son 478
#       caracteres de mas. Hoy inocuo por suerte (cero LD y cero flechas en ese
#       tramo, medido); el dia que una excepcion cite un LD-nn en su encabezado,
#       se cuela sola.
#
# LA DECISION, Y ES LA QUE LA CORRECCION 19 DEJA ESCRITA: LA VARA DEJA DE
# DEPENDER DE LA REDACCION DE UNA FICHA. La excepcion declara sus pares dentro
# de UNA FORMULA CANONICA con marca de apertura y de cierre INEQUIVOCAS, y la
# vara la exige entera.
#
# POR QUE ESTAS DOS MARCAS Y NO OTRAS, que es la parte que hay que justificar:
# "PARES EXCEPTUADOS:" y "FIN PARES EXCEPTUADOS" llevan la palabra EXCEPTUADOS
# pegada a un dos puntos o a un FIN, forma que la prosa explicativa en
# castellano no produce sola; y, a diferencia de "doble linea" o "y escalera",
# NO SON TERMINOS DEL VOCABULARIO DEL 9.22, que era justo lo que hacia que los
# viejos aparecieran tambien en la explicacion. La marca de cierre NO contiene
# a la de apertura (una lleva dos puntos y la otra no), asi que la comprobacion
# de ancla unica no se dispara sola.
#
# LOS TRES FALLOS RUIDOSOS, Y NINGUNO LEE DE MAS (banco 9):
#   (i)   falta la marca de APERTURA  -> ROJO nombrandola, conjunto VACIO.
#   (ii)  falta la marca de CIERRE    -> ROJO nombrandola, conjunto VACIO.
#         El `else linea[ini:]` MUERE: nunca se lee hasta el final de la linea.
#   (iii) la marca de apertura aparece MAS DE UNA VEZ -> ROJO POR AMBIGUA,
#         conjunto VACIO. No se toma la primera.
# Y sigue vivo el cuarto de la vuelta 143: la excepcion que dispara y no deja
# sacar ni un par es ROJO y no se aplica.
#
# LO VIEJO NO SE BORRA: el bloque de la vuelta 143 que hay encima queda entero,
# porque es donde vive el CRITERIO (que sigue adjudicado y vigente: los pares
# se sacan de la ventana que la ficha delimita, no de la linea entera). Lo que
# cambia es COMO se delimita esa ventana.
#
# MUTACIONES: scripts/loop/vuelta144_2a_mutaciones.py, todas EN MEMORIA y con
# el sujeto y el veredicto POR COMPUTO, nunca sobre un literal.
MARCA_ABRE_EXCEPCION = "pares exceptuados:"
MARCA_CIERRA_EXCEPCION = "fin pares exceptuados"
PATRON_LD = re.compile(r"\bLD-(\d+)\b")


def _pares_por_ld(op):
    """{'LD-<n>': [(origen, destino), ...]} sacado del PROPIO aristas_nuevas de
    la ficha. Es la traduccion de un LD a par de nodos, y no se teclea: la fila
    que dice "por LD-<n>" es la que aporta sus pares."""
    mapa = {}
    for cadena in (op.get("aristas_nuevas") or []):
        pares = PATRON_ARISTA.findall(cadena)
        if not pares:
            continue
        for n in PATRON_LD.findall(cadena):
            mapa.setdefault("LD-%s" % n, []).extend(pares)
    return mapa


def pares_exceptuados_de(op, resolver, fallos):
    """TAREA 2.a (vuelta 143). Los pares que la EXCEPCION ESCRITA de la ficha
    nombra. Ver el bloque "EL REGIMEN DE VUELTA PASA A SER POR PAR" de arriba.

    Devuelve (conjunto, cita, nomina):
      conjunto = set de frozenset({a, b}) con los dos extremos YA RESUELTOS;
      cita     = "verificacion <i>: <frase literal>" que dispara, o None;
      nomina   = ["a <-> b", ...] ordenada, para publicar en la celda."""
    disparo = None
    for i, linea in enumerate(op.get("verificacion") or []):
        bajo = (linea or "").lower()
        for f in FRASES_EXCEPCION_PAR:
            if f in bajo:
                disparo = (i, f, linea or "", bajo)
                break
        if disparo:
            break
    if disparo is None:
        return set(), None, []

    i, frase, linea, bajo = disparo
    cita = "verificacion %d: %s" % (i, frase)

    # LA FORMULA CANONICA, ENTERA O ROJO (TAREA 2.a, vuelta 144; CORRECCION 19).
    # Los tres extremos fallan RUIDOSO y ninguno lee de mas: nunca hay lectura
    # por defecto hasta el final de la linea.
    aperturas = [m.start() for m in re.finditer(re.escape(MARCA_ABRE_EXCEPCION), bajo)]
    if not aperturas:
        fallos.append("%s: dispara la excepcion del 9.22 (%s) pero su texto no trae la marca "
                      "de apertura '%s' de la formula canonica: la excepcion NO se aplica y "
                      "no se adivina que pares nombra"
                      % (op.get("id_op"), cita, MARCA_ABRE_EXCEPCION.upper()))
        return set(), cita, []
    if len(aperturas) > 1:
        fallos.append("%s: dispara la excepcion del 9.22 (%s) y la marca de apertura '%s' "
                      "aparece %d veces en la misma linea (posiciones %s): ANCLA AMBIGUA, la "
                      "excepcion NO se aplica y no se toma la primera"
                      % (op.get("id_op"), cita, MARCA_ABRE_EXCEPCION.upper(),
                         len(aperturas), ", ".join(str(x) for x in aperturas)))
        return set(), cita, []
    ini = aperturas[0]
    fin = bajo.find(MARCA_CIERRA_EXCEPCION, ini + len(MARCA_ABRE_EXCEPCION))
    if fin < 0:
        fallos.append("%s: dispara la excepcion del 9.22 (%s) y abre la formula canonica con "
                      "'%s' pero NO la cierra con '%s': la excepcion NO se aplica y la ventana "
                      "NO se ensancha hasta el final de la linea"
                      % (op.get("id_op"), cita, MARCA_ABRE_EXCEPCION.upper(),
                         MARCA_CIERRA_EXCEPCION.upper()))
        return set(), cita, []
    ventana = linea[ini + len(MARCA_ABRE_EXCEPCION):fin]

    mapa_ld = _pares_por_ld(op)
    crudos = []
    sueltos = []
    for n in PATRON_LD.findall(ventana):
        ld = "LD-%s" % n
        if ld in mapa_ld:
            crudos.extend(mapa_ld[ld])
        else:
            sueltos.append(ld)
    crudos.extend(PATRON_ARISTA.findall(ventana))
    if sueltos:
        fallos.append("%s: la excepcion nombra %s y su propio aristas_nuevas no trae ninguna "
                      "fila con ese LD: no se adivina a que par se refiere"
                      % (op.get("id_op"), ", ".join(sorted(set(sueltos)))))

    conjunto = set()
    for o, d in crudos:
        ro, rd = resolver(o), resolver(d)
        if ro == rd:
            continue
        conjunto.add(frozenset((ro, rd)))

    if not conjunto:
        fallos.append("%s: dispara la excepcion del 9.22 (%s) y NO se puede sacar ni un par "
                      "de su texto: una excepcion que no nombra pares no se aplica"
                      % (op.get("id_op"), cita))
        return set(), cita, []

    nomina = sorted(" <-> ".join(sorted(par)) for par in conjunto)
    return conjunto, cita, nomina


def regimen_de_vuelta(op, fallos, hay_excepcion=False):
    """PROHIBE / MUTUO / SIN REGLA, leido de la `verificacion` de la ficha.

    Devuelve (regimen, cita), donde cita es "verificacion <i>: <frase>" de la
    primera linea que lo decide, o None si ninguna lo dice. NUNCA mira el campo
    `tipo`: el encargo de la vuelta 141 lo prohibe expresamente.

    `hay_excepcion` (TAREA 2.a, vuelta 143) dice si la ficha NOMBRA pares
    exceptuados. Si los nombra, llevar PROHIBE y MUTUO a la vez YA NO ES
    AMBIGUO: la ficha ha dicho con sus palabras cuales pares salen de la
    prohibicion, que es lo que el hueco de orden 1 del 00_INDICE manda. AMBIGUO
    queda para la ficha que prohibe y exige la vuelta SIN nombrar pares."""
    prohibe = None
    mutuo = None
    for i, linea in enumerate(op.get("verificacion") or []):
        bajo = (linea or "").lower()
        for f in FRASES_PROHIBE_VUELTA:
            if f in bajo and prohibe is None:
                prohibe = "verificacion %d: %s" % (i, f)
        for f in FRASES_MUTUO:
            if f in bajo and mutuo is None:
                mutuo = "verificacion %d: %s" % (i, f)
    if prohibe and mutuo:
        if hay_excepcion:
            return "PROHIBE", "%s (y %s, resuelto por la excepcion nombrada)" % (prohibe, mutuo)
        fallos.append("%s: su verificacion PROHIBE y EXIGE la vuelta a la vez (%s / %s) y NO "
                      "nombra pares exceptuados: no se resuelve adivinando"
                      % (op.get("id_op"), prohibe, mutuo))
        return "AMBIGUO", "%s / %s" % (prohibe, mutuo)
    if prohibe:
        return "PROHIBE", prohibe
    if mutuo:
        return "MUTUO", mutuo
    return "SIN REGLA", None


def direcciones_de(pares, resolver):
    """Las DIRECCIONES distintas tras resolver, en el orden en que aparecen
    (TAREA 2.c, vuelta 141: la unidad publicada es la direccion, no la fila de
    ficha ni la cadena)."""
    vistas = []
    for o, d in pares:
        par = (resolver(o), resolver(d))
        if par not in vistas:
            vistas.append(par)
    return vistas


def destino_de_enlace(op, pares, nodos, resolver, fallos):
    """TAREA 2.a y 2.c de la vuelta 141, y TAREA 2.a de la vuelta 143. Mide IDA
    Y VUELTA de cada DIRECCION y juzga segun el regimen de vuelta que la propia
    ficha declara, QUE DESDE LA VUELTA 143 PUEDE SER DISTINTO PAR A PAR (ver el
    bloque "EL REGIMEN DE VUELTA PASA A SER POR PAR")."""
    exceptuados, cita_exc, nomina_exc = pares_exceptuados_de(op, resolver, fallos)
    regimen, cita = regimen_de_vuelta(op, fallos, hay_excepcion=bool(exceptuados))
    dirs = direcciones_de(pares, resolver)

    con_ida, sin_ida, con_vuelta = [], [], []
    # EL DESGLOSE POR PAR (TAREA 2.a.iii, vuelta 143): las direcciones cuyo par
    # NO esta exceptuado siguen bajo PROHIBE, y su vuelta presente impide
    # cumplir; las de los pares SI exceptuados van bajo MUTUO, y su vuelta no
    # solo no penaliza: se exige.
    vuelta_bajo_prohibe, dos_lineas_bajo_mutuo, mutuo_a_medias = [], [], []
    for ro, rd in dirs:
        ida, _, _ = arista_presente(nodos, resolver, ro, rd)
        vuelta, _, _ = arista_presente(nodos, resolver, rd, ro)
        nombre = "%s -> %s" % (ro, rd)
        (con_ida if ida else sin_ida).append(nombre)
        if vuelta:
            con_vuelta.append("%s -> %s" % (rd, ro))
        if exceptuados:
            par = frozenset((ro, rd))
            if par in exceptuados:
                if ida and vuelta:
                    dos_lineas_bajo_mutuo.append(nombre)
                else:
                    mutuo_a_medias.append(nombre)
            elif vuelta:
                vuelta_bajo_prohibe.append("%s -> %s" % (rd, ro))

    if not dirs:
        return False, "cero direcciones parseadas de aristas_nuevas"

    if exceptuados and regimen in ("PROHIBE", "MUTUO", "SIN REGLA"):
        # LA VUELTA SOLO PENALIZA DONDE LA FICHA NO LA HA EXCEPTUADO.
        cumplido = (not sin_ida) and (not vuelta_bajo_prohibe)
        nota = ("regimen de vuelta POR PAR por la EXCEPCION ESCRITA en la ficha (%s), "
                "banco 9.22 y hueco de orden 1 del 00_INDICE: %d direccion(es) de pares "
                "EXCEPTUADOS van bajo MUTUO (la vuelta NO penaliza y las dos se exigen) y "
                "%d bajo PROHIBE (la vuelta presente IMPIDE cumplir); el regimen de base de "
                "la ficha es %s (%s); PARES EXCEPTUADOS QUE LA FICHA NOMBRA (%d): %s"
                % (cita_exc,
                   len([1 for ro, rd in dirs if frozenset((ro, rd)) in exceptuados]),
                   len([1 for ro, rd in dirs if frozenset((ro, rd)) not in exceptuados]),
                   regimen, cita, len(nomina_exc), ", ".join(nomina_exc)))
    elif regimen == "MUTUO":
        cumplido = not sin_ida
        nota = ("regimen de vuelta MUTUO por la ficha (%s), banco 9.22: la vuelta NO "
                "penaliza y las dos direcciones se exigen" % cita)
    elif regimen == "PROHIBE":
        cumplido = (not sin_ida) and (not con_vuelta)
        nota = ("regimen de vuelta PROHIBE por la ficha (%s): la vuelta presente "
                "IMPIDE cumplir" % cita)
    elif regimen == "AMBIGUO":
        cumplido = False
        nota = "regimen de vuelta AMBIGUO (%s): no se juzga" % cita
    else:
        cumplido = not sin_ida
        nota = ("regimen de vuelta SIN REGLA: la ficha no dice nada de la vuelta, "
                "asi que se MIDE y se publica pero NO se juzga (EJECUTOR.md regla 5)")

    # LA CELDA PUBLICA UNA SOLA UNIDAD: el numerador y el denominador son
    # DIRECCIONES; las filas de ficha van nombradas como tales (TAREA 2.c).
    razon = "%d de %d direcciones con la IDA presente" % (len(con_ida), len(dirs))
    if len(pares) != len(dirs):
        razon += " (%d filas de ficha colapsan en %d direcciones)" % (len(pares), len(dirs))
    else:
        razon += " (%d filas de ficha, sin colapso)" % len(pares)
    razon += "; con la VUELTA presente %d de %d" % (len(con_vuelta), len(dirs))
    if con_vuelta:
        razon += ": " + ", ".join(con_vuelta)
    if sin_ida:
        razon += "; sin la IDA: " + ", ".join(sin_ida)
    if exceptuados:
        # EL DESGLOSE, NO UN TOTAL PELADO (TAREA 2.a.iii de la vuelta 143).
        razon += ("; bajo PROHIBE con la VUELTA presente (impiden cumplir) %d"
                  % len(vuelta_bajo_prohibe))
        if vuelta_bajo_prohibe:
            razon += ": " + ", ".join(vuelta_bajo_prohibe)
        razon += ("; bajo MUTUO con las DOS direcciones (se exigen) %d"
                  % len(dos_lineas_bajo_mutuo))
        if dos_lineas_bajo_mutuo:
            razon += ": " + ", ".join(dos_lineas_bajo_mutuo)
        if mutuo_a_medias:
            razon += ("; bajo MUTUO a medias (falta una de las dos) %d: %s"
                      % (len(mutuo_a_medias), ", ".join(mutuo_a_medias)))
    razon += "; " + nota
    return cumplido, razon


# --------------- LA MESA QUE DECLARA SU FIGURA (TAREA 3.a, vuelta 144) -------
#
# POR QUE NACE (acta de la vuelta 143, adjudicacion 3.9; CORRECCION 20 de
# docs/plan/CORRECCIONES_A_APLICAR.md). La rama `es_mesa` de `medir()` mide una
# mesa SOLO POR SUS HIJAS (`bloquea_a` union remision) y NUNCA mira los campos
# propios de la ficha. Medido leyendo el fuente con `ast`
# (scripts/loop/vuelta144_1c_medir_opm04.py): esa rama no lee `nodos`, ni
# `eliminar`, ni `superviviente`, ni `aristas_nuevas`, ni `preservar`.
#
# Eso vale para las cuatro mesas cuya cirugia la hacen sus hijas. NO vale para
# `OP-M-04`, que es LA UNICA MESA QUE LLEVA SU PROPIA CIRUGIA DENTRO: `nodos`
# con cuatro, `eliminar` con dos, un `superviviente` doble y un giro en
# `aristas_nuevas`. Sus dos hijas (`OP-S-12` y `OP-U-01`) no ejecutan su
# cirugia, y ademas ninguna esta en el catalogo de la fase 06, asi que la vara
# de mesa la dejaba en NO COMPUTABLE y caia en SIN VARA ESCRITA: el instrumento
# diciendo en voz alta que le falta una regla.
#
# LO QUE SE ANADE ES UN CASO MAS Y SOLO UNO, POR EXTENSION CITABLE: cuando el
# `tipo` de la mesa DECLARA SU FIGURA, la mesa se mide con las varas de esa
# figura SOBRE SUS PROPIOS CAMPOS. La frase que dispara va LITERAL DE LA FICHA
# y citada aqui, igual que las seis de la vuelta 141 y la excepcion de la 143:
#
#     "MESA ADJUDICADA: DOS FUSIONES MAS UN ENLACE"   (tipo de OP-M-04)
#
# NO ES DOCTRINA NUEVA Y LAS DOS VARAS YA ESTAN ESCRITAS EN ESTE MISMO FICHERO:
# `destino_de_fusion` (superviviente vivo, absorbidos deprecados y en
# `ids_alias`) y `destino_de_enlace` (direcciones con la IDA presente y el
# regimen de vuelta que la ficha declara). SE REUSAN, NO SE COPIAN: esta rama
# fabrica sub-fichas EN MEMORIA y se las pasa.
#
# UNA MESA QUE NO DECLARA SU FIGURA SE COMPORTA EXACTAMENTE COMO ANTES DE ESTA
# VUELTA, con el mismo texto de celda. Eso es lo que prueba la mutacion (iv) de
# scripts/loop/vuelta144_3a_mutaciones.py.
#
# --- LAS DOS DECISIONES DE LECTURA, DECLARADAS PORQUE SON DECISIONES ---
#
# (1) EL EMPAREJAMIENTO DE CADA FUSION NO SE TECLEA, SE DERIVA, Y CON UNA
#     EXIGENCIA DE COBERTURA QUE LO HACE NO CIRCULAR. La ficha nombra sus DOS
#     supervivientes en el campo `superviviente` y sus DOS eliminados en
#     `eliminar`, pero NO dice por escrito cual eliminado va con cual
#     superviviente en forma legible por maquina. Asignarlo a mano seria teclear
#     una celda. Se deriva del grafo: cada eliminado se asigna al superviviente
#     en cuyos `ids_alias` aparece. Y para que eso no sea circular (aceptar
#     cualquier reparto), se exige ADEMAS, y esto es lo que muerde:
#       - CADA eliminado tiene que estar en los `ids_alias` de EXACTAMENTE UNO
#         de los supervivientes: cero es ROJO nombrandolo, dos es ROJO
#         nombrandolo;
#       - CADA superviviente tiene que quedarse con AL MENOS UN absorbido,
#         porque la figura declara DOS fusiones y una fusion sin absorbido no es
#         una fusion.
#     Con las dos exigencias puestas, `destino_de_fusion` mide lo suyo (vivo,
#     deprecado, alias) sobre un reparto que ya no puede ser cualquiera.
#
# (2) LA DIRECCION DEL ENLACE SE LEE DE UNA FRASE LITERAL DE `aristas_nuevas`,
#     CITADA AQUI. El `aristas_nuevas` de esta mesa es prosa y NO trae ninguna
#     flecha "A -> B", asi que `pares_de_aristas` saca cero pares de el. Lo que
#     si trae, literal, es:
#
#         "LA OPERACION TERMINA CON UNA SOLA ARISTA entre madre e hijo, en la
#          direccion de la escalera: identificar hacia formalizar"
#
#     La marca es `en la direccion de la escalera:` y detras van dos palabras
#     separadas por `hacia`. CADA UNA TIENE QUE CASAR COMO PREFIJO CON
#     EXACTAMENTE UNO de los dos supervivientes: si casa con ninguno o con los
#     dos, es ROJO nombrandolo, nunca se elige el primero. Con eso se fabrica la
#     sub-ficha del ENLACE ("A -> B") y se le pasa a `destino_de_enlace` junto
#     con la `verificacion` ENTERA de la propia ficha, para que el regimen de
#     vuelta lo siga decidiendo la ficha y no esta rama.
#
# MUTACIONES: scripts/loop/vuelta144_3a_mutaciones.py, las cuatro EN MEMORIA y
# con el veredicto por computo.
FRASE_FIGURA_DOS_FUSIONES_UN_ENLACE = "mesa adjudicada: dos fusiones mas un enlace"
MARCA_DIRECCION_ESCALERA = "en la direccion de la escalera:"


def figura_declarada_de(op):
    """La figura que el propio `tipo` de la mesa declara, o None. La frase va
    literal de la ficha (ver el bloque de arriba)."""
    tipo = (op.get("tipo") or "").lower()
    if FRASE_FIGURA_DOS_FUSIONES_UN_ENLACE in tipo:
        return FRASE_FIGURA_DOS_FUSIONES_UN_ENLACE
    return None


def _supervivientes_de(op):
    """Los ids de nodo que el campo `superviviente` nombra Y que ademas estan en
    el propio `nodos` de la ficha. No se teclea ninguno: se cruzan los dos
    campos de la ficha."""
    texto = op.get("superviviente") or ""
    de_la_ficha = [x for x in (op.get("nodos") or [])]
    return [x for x in de_la_ficha if re.search(r"\b%s\b" % re.escape(x), texto)]


def _direccion_del_enlace(op, sups, fallos):
    """La direccion del enlace, leida de la frase literal de `aristas_nuevas`.
    Devuelve (origen, destino) o (None, None) con el fallo ya registrado."""
    cadena = None
    for s in (op.get("aristas_nuevas") or []):
        if MARCA_DIRECCION_ESCALERA in (s or "").lower():
            cadena = s
            break
    if cadena is None:
        fallos.append("%s: declara la figura %r y su aristas_nuevas no trae la marca %r: "
                      "no se adivina en que direccion va el enlace"
                      % (op.get("id_op"), FRASE_FIGURA_DOS_FUSIONES_UN_ENLACE,
                         MARCA_DIRECCION_ESCALERA))
        return None, None
    bajo = cadena.lower()
    cola = cadena[bajo.find(MARCA_DIRECCION_ESCALERA) + len(MARCA_DIRECCION_ESCALERA):]
    palabras = [p for p in re.split(r"[^a-z0-9_]+", cola.lower()) if p]
    if len(palabras) < 3 or palabras[1] != "hacia":
        fallos.append("%s: tras %r esperaba '<a> hacia <b>' y encontro %r: no se adivina"
                      % (op.get("id_op"), MARCA_DIRECCION_ESCALERA, palabras[:3]))
        return None, None
    extremos = []
    for tok in (palabras[0], palabras[2]):
        casan = [s for s in sups if s.startswith(tok)]
        if len(casan) != 1:
            fallos.append("%s: la palabra %r de la direccion del enlace casa con %d de los "
                          "supervivientes (%s) y tiene que casar con UNO: ambiguo, no se "
                          "toma el primero"
                          % (op.get("id_op"), tok, len(casan), ", ".join(casan) or "ninguno"))
            return None, None
        extremos.append(casan[0])
    if extremos[0] == extremos[1]:
        fallos.append("%s: la direccion del enlace sale con el mismo nodo en los dos "
                      "extremos (%s)" % (op.get("id_op"), extremos[0]))
        return None, None
    return extremos[0], extremos[1]


def destino_de_mesa_con_figura(op, nodos, resolver, fallos):
    """La mesa que declara su figura, medida con las varas de su figura sobre
    SUS PROPIOS campos. Ver el bloque "LA MESA QUE DECLARA SU FIGURA".

    Devuelve (cumplido, razon). `cumplido` es True o False; nunca None, porque
    aqui SI hay vara escrita."""
    partes = []
    sups = _supervivientes_de(op)
    elim = list(op.get("eliminar") or [])
    if len(sups) != 2 or len(elim) != 2:
        fallos.append("%s: la figura %r pide DOS supervivientes y DOS eliminados, y la ficha "
                      "trae %d y %d" % (op.get("id_op"),
                                        FRASE_FIGURA_DOS_FUSIONES_UN_ENLACE,
                                        len(sups), len(elim)))
        return False, ("la ficha declara la figura %r y no trae dos supervivientes y dos "
                       "eliminados (trae %d y %d)"
                       % (FRASE_FIGURA_DOS_FUSIONES_UN_ENLACE, len(sups), len(elim)))

    # ---- LAS DOS FUSIONES, con reparto derivado y cobertura exigida --------
    reparto = {s: [] for s in sups}
    sin_casa, con_dos_casas = [], []
    for x in elim:
        duenos = [s for s in sups if x in set((nodos.get(s) or {}).get("ids_alias") or [])]
        if len(duenos) == 1:
            reparto[duenos[0]].append(x)
        elif not duenos:
            sin_casa.append(x)
        else:
            con_dos_casas.append("%s (en %s)" % (x, " y ".join(duenos)))

    faltas_fusion = []
    if sin_casa:
        faltas_fusion.append("sin absorber por ninguno de los dos supervivientes: %s"
                             % ", ".join(sorted(sin_casa)))
    if con_dos_casas:
        faltas_fusion.append("en los ids_alias de LOS DOS supervivientes a la vez: %s"
                             % ", ".join(sorted(con_dos_casas)))
    vacios = [s for s in sups if not reparto[s]]
    if vacios and not sin_casa and not con_dos_casas:
        faltas_fusion.append("superviviente(s) sin ningun absorbido, y la figura declara DOS "
                             "fusiones: %s" % ", ".join(sorted(vacios)))

    # UNA FUSION SIN ABSORBIDO NO CUENTA COMO CUMPLIDA. `destino_de_fusion`
    # sobre un superviviente vivo y cero absorbidos devuelve True, y con razon,
    # porque en su contexto normal la nomina de absorbidos siempre esta llena.
    # Aqui la nomina la reparte esta rama, asi que el caso vacio existe y se
    # trata: se cuenta como NO cumplida y la celda lo dice con esas palabras.
    cumplidas = []
    for s in sups:
        sub = {"id_op": "%s (fusion de %s)" % (op.get("id_op"), s),
               "superviviente": s,
               "nodos": [s] + reparto[s],
               "eliminar": reparto[s]}
        ok, razon = destino_de_fusion(sub, nodos, fallos, resolver)
        if not reparto[s]:
            ok = False
            razon += " [SIN ABSORBIDO ASIGNADO: no es una fusion cumplida]"
        cumplidas.append(ok is True)
        partes.append("fusion de %s: %s" % (s, razon))
    n_fusiones_ok = sum(1 for c in cumplidas if c)
    fusiones_ok = all(cumplidas) and not faltas_fusion
    if faltas_fusion:
        partes.append("REPARTO DE ABSORBIDOS ROTO: " + "; ".join(faltas_fusion))

    # ---- EL ENLACE, con la direccion leida de la ficha ---------------------
    origen, destino = _direccion_del_enlace(op, sups, fallos)
    if origen is None:
        partes.append("enlace: NO se pudo leer la direccion de la ficha")
        enlace_ok = False
    else:
        sub_enlace = {"id_op": "%s (enlace)" % op.get("id_op"),
                      "aristas_nuevas": ["%s -> %s" % (origen, destino)],
                      "verificacion": list(op.get("verificacion") or [])}
        pares = pares_de_aristas(sub_enlace, fallos)
        ok_e, razon_e = destino_de_enlace(sub_enlace, pares, nodos, resolver, fallos)
        enlace_ok = ok_e is True
        partes.append("enlace %s -> %s (direccion leida de la ficha): %s"
                      % (origen, destino, razon_e))

    cumplido = bool(fusiones_ok and enlace_ok)
    cabeza = ("figura declarada en el propio `tipo` (%r), medida con las varas de FUSION y "
              "de ENLACE sobre los campos de la ficha: %d de %d fusiones con destino "
              "cumplido, reparto de absorbidos %s, y el enlace %s"
              % (op.get("tipo"), n_fusiones_ok, len(sups),
                 "ROTO" if faltas_fusion else "OK",
                 "CUMPLIDO" if enlace_ok else "SIN CUMPLIR"))
    return cumplido, cabeza + "; " + "; ".join(partes)


def es_mesa(op):
    return (op.get("tipo") or "").upper().startswith("MESA ADJUDICADA")


def medir(fase, ops, nodos, remisiones=None, ref="WORK"):
    """Devuelve (filas, cifra, fallos). Cada fila es un dict con todo lo que
    la tabla imprime. Ninguna celda se teclea fuera de aqui."""
    fallos = []
    if remisiones is None:
        remisiones = leer_remisiones(fase, ref)
    catalogo, por_id = construir_catalogo(fase, ops, remisiones, fallos)
    if not catalogo:
        fallos.append("la fase %s no tiene NINGUNA operacion en su catalogo: "
                      "o el nombre de fase no existe o el fichero cambio" % fase)
    resolver = resolver_de(nodos)
    en_catalogo = set(catalogo)

    # Primera pasada: las que no son mesa, para que las mesas puedan leerlas.
    veredicto = {}
    filas = {}
    for x in catalogo:
        op = por_id[x]
        if es_mesa(op):
            continue
        sup = op.get("superviviente")
        pares = pares_de_aristas(op, fallos)
        if sup and PATRON_ID_NODO.match(sup) and sup in nodos:
            vara = "FUSION"
            cumplido, razon = destino_de_fusion(op, nodos, fallos, resolver)
        elif pares:
            vara = "ENLACE"
            cumplido, razon = destino_de_enlace(op, pares, nodos, resolver, fallos)
        else:
            vara = "SIN VARA ESCRITA"
            cumplido = None
            razon = ("no hay regla escrita que mida contra el grafo el destino de "
                     "un tipo %s (ni superviviente resoluble ni aristas_nuevas)"
                     % (op.get("tipo") or "?"))
        veredicto[x] = cumplido
        filas[x] = dict(id_op=x, fase=op.get("fase"), estado=op.get("estado"),
                        tipo=op.get("tipo"), vara=vara, cumplido=cumplido, razon=razon,
                        remitida=remisiones.get(x))

    for x in catalogo:
        op = por_id[x]
        if not es_mesa(op):
            continue
        # TAREA 2.b (vuelta 141): LA NOMINA SON LAS DOS FUENTES UNIDAS.
        # `bloquea_a` NO es la nomina completa: OP-M-01.bloquea_a no nombra a
        # OP-M-01-SEXTO, que la tabla de remision de 04_ENLACES.md manda
        # expresamente a OP-M-01. La segunda fuente se PARSEA (leer_remisiones),
        # no se teclea.
        # LA MESA QUE DECLARA SU FIGURA SE MIDE POR SU FIGURA (TAREA 3.a,
        # vuelta 144; acta 143, adjudicacion 3.9). Es UN caso mas y solo uno:
        # una mesa que NO declara figura sigue midiendose por sus hijas,
        # exactamente como antes de esta vuelta.
        if figura_declarada_de(op) is not None:
            cumplido, razon = destino_de_mesa_con_figura(op, nodos, resolver, fallos)
            veredicto[x] = cumplido
            filas[x] = dict(id_op=x, fase=op.get("fase"), estado=op.get("estado"),
                            tipo=op.get("tipo"), vara="MESA POR FIGURA",
                            cumplido=cumplido, razon=razon,
                            remitida=remisiones.get(x))
            continue

        de_bloquea = [h for h in (op.get("bloquea_a") or []) if h != x]
        de_remision = [h for h, meta in sorted(remisiones.items())
                       if meta.get("a") == x and h != x]
        procedencia = {}
        for h in de_bloquea:
            procedencia[h] = "bloquea_a"
        for h in de_remision:
            procedencia[h] = "las dos" if h in procedencia else "remision"
        nomina = de_bloquea + [h for h in de_remision if h not in de_bloquea]

        hijas = [h for h in nomina if h in en_catalogo]
        fuera = [(h, (por_id.get(h) or {}).get("fase", "no existe"))
                 for h in nomina if h not in en_catalogo]
        celda_fuentes = "nomina de %d (bloquea_a %d, remision %d, union %d)" % (
            len(nomina), len(de_bloquea), len(de_remision), len(nomina))
        if not hijas:
            cumplido = None
            razon = ("NINGUNA de sus hijas esta en el catalogo de esta fase; %s; "
                     "nomina: %s" % (celda_fuentes,
                                     ", ".join("%s (%s)" % (h, f) for h, f in fuera) or "vacia"))
        else:
            sin = [h for h in hijas if veredicto.get(h) is not True]
            cumplido = not sin
            razon = "%d de %d hijas del catalogo con destino cumplido" % (len(hijas) - len(sin), len(hijas))
            razon += "; " + celda_fuentes
            razon += "; procedencia: " + ", ".join(
                "%s por %s" % (h, procedencia[h]) for h in hijas)
            if sin:
                razon += "; sin cumplir: " + ", ".join(sorted(sin))
            if fuera:
                razon += "; hijas FUERA del catalogo: " + ", ".join("%s (%s)" % (h, f) for h, f in fuera)
        veredicto[x] = cumplido
        filas[x] = dict(id_op=x, fase=op.get("fase"), estado=op.get("estado"),
                        tipo=op.get("tipo"), vara="MESA", cumplido=cumplido, razon=razon,
                        remitida=remisiones.get(x))

    orden = sorted(catalogo, key=lambda x: (filas[x]["vara"] != "MESA", x))
    lista = [filas[x] for x in orden]
    cumplidas = [f["id_op"] for f in lista if f["cumplido"] is True]
    sin_cumplir = [f["id_op"] for f in lista if f["cumplido"] is not True]
    sin_vara = [f["id_op"] for f in lista if f["cumplido"] is None]
    # EL TERCER VEREDICTO (TAREA 2.c, vuelta 142). Se publica COMO SUB-SACO
    # NOMBRADO DENTRO DE `sin cumplir`, exactamente igual que `sin vara escrita`
    # desde la vuelta 140, y POR LA MISMA RAZON ADJUDICADA (acta 140, 3.2): una
    # operacion cuyo destino no esta demostrado NO puede salir del saco de las
    # no cumplidas, porque el instrumento que lee la linea `sin cumplir: N` para
    # juzgar las afirmaciones de cierre (verificar_cifras_del_reporte.py) dejaria
    # pasar "la fase cierra" con una operacion EJECUTADA AL REVES dentro. Que no
    # sea "cumplida ni sin cumplir" se cumple donde se puede cumplir sin abrir
    # ese agujero: EN SU VEREDICTO, que es el suyo y no `SIN CUMPLIR`.
    divergentes = [f["id_op"] for f in lista
                   if f["vara"] == "FUSION" and (f["razon"] or "").startswith(MARCA_DIVERGENTE)]
    consumidas = [f["id_op"] for f in lista
                  if f["vara"] == "FUSION" and (f["razon"] or "").startswith(MARCA_CONSUMIDA)]
    cifra = dict(catalogo=len(lista), cumplido=len(cumplidas),
                 sin_cumplir=len(sin_cumplir), sin_vara=len(sin_vara),
                 nombres_sin_cumplir=sin_cumplir, nombres_sin_vara=sin_vara,
                 divergentes=len(divergentes), nombres_divergentes=divergentes,
                 consumidas=len(consumidas), nombres_consumidas=consumidas)
    return lista, cifra, fallos


# ---------------------------------------------------------------- impresion

def _celda(x):
    return (x or "").replace("|", "/")


def imprimir(fase, lista, cifra, fallos, ref="WORK"):
    print("ESTADO DE LA FASE %s | REF: %s" % (fase, ref))
    print("El campo `estado` va como CONTRASTE, no como veredicto: ninguna cifra lo mira.")
    print("")
    print("| id_op | fase escrita | estado (contraste) | vara | remitida: de / a | destino medido contra el grafo | veredicto |")
    print("|---|---|---|---|---|---|---|")
    for f in lista:
        rem = f["remitida"]
        if rem:
            celda_rem = "de %s / a %s (%s)" % (rem.get("de") or "?", rem.get("a") or "la fase, sin mesa nombrada", rem.get("fuente"))
        else:
            celda_rem = "no remitida"
        # EL TERCER VEREDICTO SE PUBLICA EN SU COLUMNA (TAREA 2.c, vuelta 142):
        # ni CUMPLIDO ni un SIN CUMPLIR a secas, sino su rotulo propio.
        razon_f = f["razon"] or ""
        if f["cumplido"] is True:
            v = "CUMPLIDO"
        elif razon_f.startswith(MARCA_DIVERGENTE):
            v = "CONSUMIDA CON SUPERVIVIENTE DIVERGENTE"
        elif razon_f.startswith(MARCA_CONSUMIDA):
            v = "CONSUMIDA"
        elif f["cumplido"] is False:
            v = "SIN CUMPLIR"
        else:
            v = "NO COMPUTABLE"
        print("| %s | %s | %s | %s | %s | %s | %s |" % (
            f["id_op"], _celda(f["fase"]), _celda(f["estado"]), f["vara"],
            _celda(celda_rem), _celda(f["razon"]), v))
    print("")
    print("CIFRA: operaciones del catalogo: %d | con destino cumplido: %d | sin cumplir: %d "
          "| de ellas, sin vara escrita: %d | de ellas, consumidas con superviviente "
          "divergente: %d | de ellas, consumidas: %d"
          % (cifra["catalogo"], cifra["cumplido"], cifra["sin_cumplir"], cifra["sin_vara"],
             cifra["divergentes"], cifra["consumidas"]))
    print("SIN CUMPLIR (%d): %s" % (len(cifra["nombres_sin_cumplir"]),
                                    ", ".join(cifra["nombres_sin_cumplir"]) or "ninguna"))
    print("SIN VARA ESCRITA (%d): %s" % (len(cifra["nombres_sin_vara"]),
                                         ", ".join(cifra["nombres_sin_vara"]) or "ninguna"))
    print("CONSUMIDAS CON SUPERVIVIENTE DIVERGENTE (%d): %s"
          % (len(cifra["nombres_divergentes"]),
             ", ".join(cifra["nombres_divergentes"]) or "ninguna"))
    print("CONSUMIDAS, superviviente deprecado que resuelve a un vivo NO condenado (%d): %s"
          % (len(cifra["nombres_consumidas"]),
             ", ".join(cifra["nombres_consumidas"]) or "ninguna"))
    if fallos:
        print("")
        print("ROJO, %d cosa(s) no cuadran:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fase")
    ap.add_argument("--ref", default="WORK")
    ap.add_argument("--fases", action="store_true", help="lista las fases que el fichero trae")
    a = ap.parse_args()

    ops = cargar_ops(a.ref)
    if a.fases or not a.fase:
        vistas = []
        for o in ops:
            if o.get("fase") not in vistas:
                vistas.append(o.get("fase"))
        print("FASES EN %s (%s):" % (REL_OPS, a.ref))
        for f in sorted(x for x in vistas if x):
            print("   %s (%d operacion(es) con fase propia)"
                  % (f, sum(1 for o in ops if o.get("fase") == f)))
        return 0 if a.fases else 2

    nodos = cargar_grafo(a.ref)
    lista, cifra, fallos = medir(a.fase, ops, nodos, ref=a.ref)
    return imprimir(a.fase, lista, cifra, fallos, ref=a.ref)


if __name__ == "__main__":
    raise SystemExit(main())
