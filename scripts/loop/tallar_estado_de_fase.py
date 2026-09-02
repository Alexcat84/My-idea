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


def regimen_de_vuelta(op, fallos):
    """PROHIBE / MUTUO / SIN REGLA, leido de la `verificacion` de la ficha.

    Devuelve (regimen, cita), donde cita es "verificacion <i>: <frase>" de la
    primera linea que lo decide, o None si ninguna lo dice. NUNCA mira el campo
    `tipo`: el encargo de la vuelta 141 lo prohibe expresamente."""
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
        fallos.append("%s: su verificacion PROHIBE y EXIGE la vuelta a la vez (%s / %s): "
                      "no se resuelve adivinando" % (op.get("id_op"), prohibe, mutuo))
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
    """TAREA 2.a y 2.c de la vuelta 141. Mide IDA Y VUELTA de cada DIRECCION y
    juzga segun el regimen de vuelta que la propia ficha declara."""
    regimen, cita = regimen_de_vuelta(op, fallos)
    dirs = direcciones_de(pares, resolver)

    con_ida, sin_ida, con_vuelta = [], [], []
    for ro, rd in dirs:
        ida, _, _ = arista_presente(nodos, resolver, ro, rd)
        vuelta, _, _ = arista_presente(nodos, resolver, rd, ro)
        nombre = "%s -> %s" % (ro, rd)
        (con_ida if ida else sin_ida).append(nombre)
        if vuelta:
            con_vuelta.append("%s -> %s" % (rd, ro))

    if not dirs:
        return False, "cero direcciones parseadas de aristas_nuevas"

    if regimen == "MUTUO":
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
    razon += "; " + nota
    return cumplido, razon


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
