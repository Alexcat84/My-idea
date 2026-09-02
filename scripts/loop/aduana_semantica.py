# -*- coding: utf-8 -*-
r"""aduana_semantica.py . LA PUERTA SEMANTICA DE `OP-A-02`, EL CONTROL A2.6
(TAREA 3.e de la vuelta 147). NOMBRE ESTABLE, SIN NUMERO DE VUELTA.

LA FRASE QUE LO GOBIERNA TODO, citada de la ficha de `OP-A-02`: *"LA ADUANA NO
JUZGA, OBLIGA A JUZGAR"*. Y el mecanismo, citado de su `adjudicacion`: *"Al
insertar un nodo corre el indice semantico contra SU DOMINIO y el NUCLEO. Si
algun vecino supera el umbral de la cola, LA INSERCION SE BLOQUEA hasta que
quien inserta escriba el veredicto continua-o-repite CITANDO EL ID DEL VECINO.
NUNCA bloquea por parecido: solo por VEREDICTO AUSENTE."*

POR QUE SE PUEDE CABLEAR HOY Y NO SE PODIA AYER. El reporte de la vuelta 146
declaro que *"el umbral de la cola no tiene numero en ninguna parte"* y de ahi
saco que la puerta no se podia cablear. **Era falso**, y es la caida 4.2 del acta
146: el umbral existe, esta en `scripts/intra_dominio.py`, que ES el cribado
intra que la `evidencia` de `OP-A-02` manda usar (*"el umbral de la cola es el
mismo del cribado intra"*). Ver la CORRECCION 26.

LOS DOS UMBRALES NO SE TECLEAN AQUI: SE IMPORTAN. `UMBRAL_SEMANTICO` (0.78, con
su calibracion escrita en el propio fichero) y `UMBRAL_TITULO` (80,
`token_sort_ratio` de rapidfuzz) se leen de `scripts/intra_dominio.py`. Copiar
los numeros aqui serian DOS VERSIONES DE LA MISMA VARA, que es la averia de los
dos `master_graph` que el chequeo de gemelos vino a curar. Y **este modulo NO
ACEPTA UN UMBRAL POR PARAMETRO**, a proposito y no por olvido: la ficha dice con
todas sus letras *"bajar el umbral no es una salida"*, asi que no se le da la
palanca a nadie.

Y EL INDICE TAMPOCO SE REESCRIBE: se lee `web/lib/assets/semantic_index.json`,
el mismo que usa el cribado intra, con la misma normalizacion de vectores.

QUE HACE, PASO A PASO.

  (1) El candidato tiene que TENER VECTOR en el indice. Si no lo tiene, no se
      puede "correr el indice contra su dominio y el nucleo", y entonces
      **BLOQUEA DICIENDOLO**, jamas pasa en silencio (banco 9, fallar ruidoso).
      No es una decision improvisada: es la PRECONDICION del mecanismo que la
      ficha describe, y su remedio esta escrito en el propio mensaje (construir
      el indice para el candidato antes de insertarlo).
  (2) VECINDARIO = los nodos VIVOS de SU DOMINIO mas los nodos VIVOS del NUCLEO
      (`dominio == "core"`), y ninguno mas. Es exactamente el reparto que la
      `nota` de la ficha justifica: *"la duplicacion vive dentro del dominio y
      contra el nucleo; entre dominios distintos casi no hay"*.
  (3) VECINO SOBRE EL UMBRAL = coseno >= `UMBRAL_SEMANTICO` O
      `token_sort_ratio` de titulo >= `UMBRAL_TITULO`. Las dos piernas, porque
      las dos son "el umbral de la cola" del cribado intra.
  (4) Por CADA vecino sobre el umbral tiene que existir un VEREDICTO escrito que
      CITE SU ID. Si falta uno solo, LA INSERCION SE BLOQUEA nombrando al vecino
      que no tiene veredicto.
  (5) **NUNCA BLOQUEA POR PARECIDO.** Un candidato con veinte vecinos por encima
      del umbral y veinte veredictos escritos ENTRA. Uno con un solo vecino y
      sin veredicto NO ENTRA. Lo que se exige es que alguien haya mirado y lo
      haya escrito.

DONDE SE ESCRIBE EL VEREDICTO, Y ESTO LO DECIDO YO Y LO DECLARO. La ficha dice
QUE hay que escribir y QUE tiene que citar, pero no DONDE. Elijo
`dataset/metadata/veredictos_aduana.json`, por el mismo argumento que el auditor
adjudico A FAVOR para la nomina de la aduana (acta 146, 3.4): **es dato y no
nodo**, no lo sincroniza `sync_assets_web.py`, no toca el grafo, y vive al lado
del dato hermano contra el que mide la otra mitad de la aduana. **NO es una
regla nueva**: es el mismo sitio y el mismo criterio que ya se adjudicaron para
`aduana_fuente_multiple.json`. Formato:

    {"veredictos": [
        {"nodo": "<id del candidato>",
         "vecino": "<id del vecino sobre el umbral>",
         "veredicto": "continua" | "repite",
         "por_que": "<una linea de quien lo escribio>"}
    ]}

`continua` significa "sigue adelante, no es el mismo concepto"; `repite`
significa "es el mismo y no debe entrar". **LOS DOS SON VEREDICTOS ESCRITOS**, y
por eso los dos desbloquean la puerta: `repite` desbloquea la PUERTA y a la vez
dice que no entre, que es cosa de quien inserta, no de la aduana. La aduana no
juzga.

LA FRONTERA, PORQUE ES LO QUE MAS FACIL SE LEE DE MAS. Esta puerta **no decide
si dos nodos son el mismo concepto** y no rechaza por parecerse. Lo unico que
consigue es que **nadie inserte sin haber mirado a los vecinos y haberlo
escrito**. El sintoma que impide esta en la propia nota de la ficha: *"400 pares
en A que nadie vio entrar"*.

USO (como libreria, que es como se cablea):
    from aduana_semantica import evaluar
    permitido, bloqueos, vecinos = evaluar(candidato, grafo, indice, veredictos)
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_INDICE = os.path.join(RAIZ, "web", "lib", "assets", "semantic_index.json")
RUTA_GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
RUTA_VEREDICTOS_REL = "dataset/metadata/veredictos_aduana.json"
RUTA_VEREDICTOS = os.path.join(RAIZ, RUTA_VEREDICTOS_REL.replace("/", os.sep))

VEREDICTOS_VALIDOS = ("continua", "repite")


def umbrales():
    """LOS DOS UMBRALES, IMPORTADOS Y NO TECLEADOS. Se leen de
    `scripts/intra_dominio.py`, que ES el cribado intra que la evidencia de
    `OP-A-02` manda usar. Si alguien los cambiara alli, esta puerta cambia con
    ellos, que es justo lo que "el mismo del cribado intra" significa."""
    import sys
    sys.path.insert(0, os.path.join(RAIZ, "scripts"))
    import intra_dominio
    return intra_dominio.UMBRAL_SEMANTICO, intra_dominio.UMBRAL_TITULO


def cargar_indice(ruta=None):
    with io.open(ruta or RUTA_INDICE, encoding="utf-8") as f:
        return json.load(f)


def cargar_grafo(ruta=None):
    with io.open(ruta or RUTA_GRAFO, encoding="utf-8") as f:
        return json.load(f)["nodos"]


def cargar_veredictos(ruta=None):
    """Lista de veredictos escritos. Un fichero que no existe es una lista
    vacia y NO un error: significa que nadie ha escrito ningun veredicto
    todavia, y entonces la puerta bloquea a todo el que tenga vecinos, que es
    el comportamiento correcto."""
    r = ruta or RUTA_VEREDICTOS
    if not os.path.exists(r):
        return []
    with io.open(r, encoding="utf-8") as f:
        return json.load(f).get("veredictos", [])


def vecindario(candidato_id, dominio_candidato, grafo):
    """Los nodos VIVOS de SU DOMINIO mas los del NUCLEO, y ninguno mas. El
    propio candidato queda fuera: un nodo no es vecino de si mismo."""
    fuera = []
    for nid, n in grafo.items():
        if nid == candidato_id or n.get("deprecado"):
            continue
        dom = n.get("dominio") or "core"
        if dom == dominio_candidato or dom == "core":
            fuera.append(nid)
    return sorted(fuera)


def evaluar(candidato, grafo, indice, veredictos):
    """(permitido, bloqueos, vecinos_sobre_umbral).

    `candidato` es el dict del nodo que quiere entrar (con `node_id` o `id`,
    `dominio` y `titulo_concepto`). `grafo`, `indice` y `veredictos` son datos
    YA CARGADOS: se pasan en vez de leerse aqui para que la simulacion y la
    prueba de mutacion puedan correr SOBRE COPIA EN MEMORIA sin escribir un
    byte en `dataset/`."""
    import numpy as np
    from rapidfuzz.fuzz import token_sort_ratio

    umbral_sem, umbral_tit = umbrales()
    cid = candidato.get("node_id") or candidato.get("id")
    dom = candidato.get("dominio") or "core"
    tit = candidato.get("titulo_concepto") or ""

    pos = dict((n, i) for i, n in enumerate(indice["ids"]))
    if cid not in pos:
        return False, ["%s NO TIENE VECTOR en el indice semantico: no se puede correr el "
                       "indice contra su dominio y el nucleo, asi que la aduana BLOQUEA en "
                       "vez de dejarlo pasar sin mirar. Remedio: construir el indice para "
                       "el candidato ANTES de insertarlo" % cid], []

    E = np.array(indice["embeddings"], dtype=np.float32)
    E = E / np.linalg.norm(E, axis=1, keepdims=True)
    v = E[pos[cid]]

    vecinos = []
    for nid in vecindario(cid, dom, grafo):
        sem = float(v @ E[pos[nid]]) if nid in pos else None
        t_otro = grafo[nid].get("titulo_concepto") or ""
        titulo_sim = float(token_sort_ratio(tit, t_otro)) if (tit and t_otro) else 0.0
        por = []
        if sem is not None and sem >= umbral_sem:
            por.append("semantica %.4f >= %.2f" % (sem, umbral_sem))
        if titulo_sim >= umbral_tit:
            por.append("titulo %.1f >= %d" % (titulo_sim, umbral_tit))
        if por:
            vecinos.append((nid, "; ".join(por)))

    escritos = set()
    for x in veredictos:
        if (x.get("nodo") == cid and x.get("veredicto") in VEREDICTOS_VALIDOS
                and x.get("vecino")):
            escritos.add(x["vecino"])

    bloqueos = []
    for nid, por_que in vecinos:
        if nid not in escritos:
            bloqueos.append("%s supera el umbral de la cola contra %s (%s) y NO hay veredicto "
                            "continua-o-repite que cite ese id: LA INSERCION SE BLOQUEA. La "
                            "aduana no juzga, obliga a juzgar, y bajar el umbral no es una "
                            "salida" % (cid, nid, por_que))
    return (not bloqueos), bloqueos, vecinos
