#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""costuras_internas.py - CITA los nodos con texto repetido DENTRO de si mismos.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo, ni el motor, ni la web. Lo
unico que escribe son sus dos salidas en docs/.

ESTE INSTRUMENTO CITA, NO JUZGA. Igual que gradiente_pares.py, del que es el
hermano chico. Un nodo en la cola es UNA CITA PARA LEER, no una costura
probada. El veredicto es lectura textual del auditor con visto del fundador.

QUE BUSCA. La clase nacio de dos hallazgos del gradiente: `plan_mejora_procesos`
(puesto 83) y `economia_circular_como_modelo_de_negocio` (puesto 97), dos nodos
del nucleo con DOS SECUENCIAS CASI IDENTICAS PEGADAS DENTRO. No son duplicados
entre nodos: son un solo nodo al que le sobran pasos. Dos figuras identicas en
temas sin relacion significan que la tanda que pego sin tejer dejo mas huellas, y
esas no se cazan esperando el tercer golpe de suerte.

DOS SEÑALES INDEPENDIENTES, y basta con que dispare CUALQUIERA. Se reportan LAS
DOS siempre, aunque solo una haya disparado, porque el auditor necesita ver por
que entro cada nodo:

  1. PAREJA DE PASOS: token_sort_ratio de rapidfuzz entre cada dos pasos del
     mismo nodo, umbral 80. Caza el paso REPETIDO casi literal.

  2. ALINEACION DE BLOQUES: para cada corte posible de la lista, se empareja el
     segundo bloque contra el primero EN ORDEN (emparejamiento monotono) y se
     promedian las tres mejores parejas. Umbral 44. Caza el BLOQUE reiniciado,
     que es la figura de los dos hallazgos, y ademas dice DONDE esta el corte.
     (Bajado de 45 a 44 en ago 2026 por un falso negativo medido: ver la nota
     de UMBRAL_BLOQUE.)

POR QUE HACEN FALTA LAS DOS, medido antes de escribirlo. Con la señal 1 sola, y
en cualquier umbral, la calibracion NO entra: la mejor pareja interna de
`plan_mejora_procesos` es 60.0 y la de `economia_circular` 54.7, y bajar el
umbral hasta ahi caza 856 nodos, el 24 por ciento del catalogo. Esta casa ya
adjudico que una baranda que caza lo correcto no es estricta, esta rota. El
motivo es que esas dos costuras son PARAFRASIS con cola distinta, no copias:
"Establecer metricas de exito en cada etapa" contra "Establece metricas para
cada etapa (¿estas obteniendo suficientes candidatos?)". La señal 2 las pone en
los puestos 7 y 32 de 567, y acierta el corte exacto en las dos.

LA CALIBRACION CONOCIDA: los dos nodos de arriba TIENEN que aparecer en la cola.
Si falta alguno, el instrumento esta mal calibrado, lo dice y SALE CON CODIGO 1
SIN ENTREGAR.

===========================================================================
RECALIBRACION DECLARADA (15 ago 2026, vuelta 34, decision del fundador)
===========================================================================

NADA DE LO DE ARRIBA SE BORRA: describe el instrumento tal como se calibro en
su dia, y una correccion que tapa lo que corrige no se puede auditar. Lo que
sigue es lo que se midio HOY, con sus ids y sus cifras.

LO QUE SE ROMPIO, medido en la vuelta 33: la senal de bloque recorria
`range(MIN_BLOQUE, n - MIN_BLOQUE + 1)` con `MIN_BLOQUE = 3`, y con CINCO pasos
ese rango es VACIO: devolvia 0,0 diga lo que diga el texto. Y LOS DOS NODOS DE
CALIBRACION TIENEN CINCO PASOS HOY, porque esta misma campana los destejio.
El 0,0 no era un nodo sin bloque: era la senal muerta.

EL CAMBIO, tal como lo decidio el fundador: `MIN_BLOQUE` pasa a 2, o sea senal
para todo nodo de CUATRO pasos o mas; por debajo de eso la senal devuelve
`NO APLICA` EXPLICITO en vez de un cero silencioso, y ese valor REVIENTA si
alguien lo compara con un umbral, en vez de dejarse leer como "no hay bloque".

LAS CIFRAS DE HOY, medidas sobre el grafo del 15 ago 2026 (los nodos, no el
recuerdo), con la regla vieja al lado para que la discrepancia se vea:

  plan_mejora_procesos                     5 pasos  pareja 47,1  (docstring: 60,0)
      bloque VIEJO NO APLICA (n<6)   ->    bloque NUEVO 43,1 con corte tras 2
  economia_circular_como_modelo_de_negocio 5 pasos  pareja 54,3  (docstring: 54,7)
      bloque VIEJO NO APLICA (n<6)   ->    bloque NUEVO 44,2 con corte tras 3

LO QUE LA RECALIBRACION **NO** ARREGLA, y va escrito aqui porque callarlo seria
la degradacion silenciosa contra la que existe la propia puerta:

  1. LA PUERTA SIGUE ROJA. `plan_mejora_procesos` da 43,1 contra un umbral de
     44: se queda fuera de la cola POR 0,9 PUNTOS, que es exactamente la
     distancia del falso negativo que en su dia bajo el umbral de 45 a 44. El
     instrumento sigue negandose a entregar, y ahora tambien se niega a que le
     importen las senales, que es lo que la decision manda.
  2. EL COSTO, medido sobre el catalogo entero antes de aplicar nada
     (scripts/loop/vuelta34_calibrar_costuras.py, salida en
     docs/loop/SALIDA_V34_CALIBRACION.txt): la cola pasaria de 122 a 1.497
     nodos, el 42,3 por ciento del catalogo activo. La causa es que
     `MIN_BLOQUE` no es un solo dial: tambien es la K del promedio de las K
     mejores parejas, y promediar las DOS mejores en vez de las TRES sube el
     puntaje de todo el catalogo con el umbral quieto en 44. Medido: el p50 de
     la senal nueva es 45,8, o sea que el umbral quedo POR DEBAJO DE LA
     MEDIANA. Disparar deja de ser noticia.
  3. Y por eso la frase que este mismo encabezado escribio sigue mandando:
     una baranda que caza lo correcto no es estricta, esta rota. Con 24 por
     ciento esta casa ya adjudico que no. Con 42,3 tampoco.

QUEDA COMO PENDIENTE DE DOCTRINA, no como arreglo silencioso: que umbral
acompana a `MIN_BLOQUE = 2`, o contra que nodos se recalibra la puerta, es
doctrina de medicion y la decide el fundador. Lo que esta vuelta hace es
aplicar la letra, medir el efecto y publicarlo.

===========================================================================
LA PUERTA REPARADA (19 ago 2026, vuelta 40, encargo del acta del auditor 39)
===========================================================================

NADA DE LO DE ARRIBA SE BORRA, por lo mismo de siempre: una correccion que tapa
lo que corrige no se puede auditar. La RECALIBRACION DECLARADA de la vuelta 34
dejo la puerta EN ROJO y lo dijo en su punto 1. Siguio en rojo desde entonces, y
la vuelta 39 la volvio a declarar sin tocarla. Esta seccion la repara.

LA AVERIA, MEDIDA Y NO RECORDADA. `plan_mejora_procesos`, uno de los dos
fixtures, daba 43,1 contra un umbral de 44 y el instrumento se negaba entero
(exit 1, cero entregas). EL MOTIVO NO ERA EL INSTRUMENTO: era el fixture. El
ultimo commit que toco `dataset/nodos/plan_mejora_procesos.json` es `2bd8dd76`
(*OP-F-04-HOR ejecutada en casi todo: doce nodos en trece cortes*), medido con
`git log --follow` en la vuelta 40, y ese nodo esta EN LA NOMINA de
`OP-F-04-HOR`, medido contra `docs/plan/OPERACIONES.jsonl` en la misma vuelta.
O sea: LA PROPIA CAMPANA RECORTO SU FIXTURE POR UNA OPERACION LEGITIMA, y la
puerta confundio "mi fixture quedo rancio" con "el instrumento esta roto".

QUE SE REPARA Y QUE NO SE TOCA:

  * LOS UMBRALES NO SE TOCAN. Pareja 80 y bloque 44 se quedan donde estaban.
    Aflojar el umbral para que el fixture entre seria arreglar la vara en vez
    de la pieza, y esta casa ya lo adjudico dos veces.
  * NINGUN NODO SE TOCA. La reparacion vive entera en `scripts/`. `dataset/`
    no se abre para escribir.
  * LA SEMANTICA DE LA PUERTA NO SE AFLOJA: los fixtures siguen teniendo que
    entrar TODOS, y si falta uno el instrumento sigue negandose a entregar con
    codigo 1. Lo que cambia es CONTRA QUE NODOS se comprueba, y que ahora hay
    un criterio escrito para elegirlos y un camino escrito para retirarlos.
  * LO QUE SE ANADE: un AVISO DE BORDE. En su corrida normal el instrumento
    imprime el margen de cada fixture y AVISA si alguno esta a menos de un
    punto del umbral. La averia de hoy se vio por un exit 1 a destiempo; con
    el aviso, la siguiente se ve venir. Un instrumento que puede advertir y
    calla es la degradacion silenciosa contra la que existe la propia puerta.

LO QUE ESTA REPARACION **NO** ARREGLA, y va escrito por la misma razon que lo
de arriba: LA COLA SIGUE EN EL 42,3 POR CIENTO DEL CATALOGO. Medido en la
vuelta 40 sobre el grafo de ese dia
(`scripts/loop/vuelta40_calibrar_costuras.py`, salida en
`docs/loop/SALIDA_V40_CALIBRACION.txt`): 1.496 nodos en la cola sobre 3.534
activos, y 1.494 de esos entran por la senal de bloque. ES EXACTAMENTE EL COSTO
QUE LA VUELTA 34 MIDIO Y PUBLICO (1.497 sobre el grafo de aquel dia), o sea que
el pendiente de doctrina del punto 2 de arriba SIGUE ENTERO Y SIGUE ABIERTO:
que umbral acompana a `MIN_BLOQUE = 2` lo decide el fundador, y la vuelta 40 NO
lo decide. Reparar la puerta no era arreglar la escala, y no se disfraza de eso.

Uso:
  python scripts/costuras_internas.py
  python scripts/costuras_internas.py --umbral-pareja 75 --umbral-bloque 50
"""
import argparse
import json
import statistics
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
GRAFO = BASE / "dataset" / "metadata" / "master_graph.json"
SALIDA = BASE / "docs" / "COSTURAS_INTERNAS.jsonl"
RESUMEN = BASE / "docs" / "COSTURAS_INTERNAS_RESUMEN.md"
# Marca de corte: lo que este por debajo de esta marca en el resumen NO lo
# genera el script y sobrevive a las regeneraciones.
MARCA_MANUAL = "<!-- MANUAL -->"

UMBRAL_PAREJA = 80
# BAJADO DE 45 A 44 (lote 15, ago 2026), y el motivo es un FALSO NEGATIVO medido.
# `nucleo/propuesta_gasto_capital` tiene dos narraciones del mismo analisis de
# gasto de capital y quedo fuera de la cola por 0,9 puntos: bloque 44,1.
#
# Lo instructivo es que la señal SI lo vio: su corte propuesto fue tras el paso 5,
# exactamente donde la lectura encontro la costura. No fallo la señal, fallo el
# umbral.
#
# Y la razon de fondo esta medida: el paso 3 dice "calcular NPV usando el hurdle
# rate" y el 11 dice "calcular el valor presente neto (VPN)". Son LA MISMA COSA con
# la sigla en dos idiomas, y para token_sort_ratio se parecen un 46,2.
#
# Costo del cambio, medido antes de aplicarlo: 18 citas mas (106 -> 124 por esta
# señal). Adjudicado como barato frente al mandato de leerlas todas.
UMBRAL_BLOQUE = 44

# Minimo de pasos POR LADO para que un bloque signifique algo.
#
# ~~MIN_BLOQUE = 3~~ BAJADO A 2 el 15 ago 2026 por decision del fundador (ver la
# RECALIBRACION DECLARADA del encabezado). El comentario viejo decia: "con menos
# de tres pasos por lado, 'el segundo bloque repite al primero' no es una
# afirmacion, es ruido". Se queda escrito porque es el argumento que el cambio
# contradice, y quien lo revise tiene que poder leerlo.
#
# Y LO QUE ESTE NUMERO MUEVE NO ES SOLO EL RANGO DE CORTES: es tambien la K del
# promedio de las K mejores parejas de mas abajo, o sea LA ESCALA DEL PUNTAJE.
# Medido antes de aplicarlo: la cola pasa de 122 a 1.497 nodos con el umbral
# quieto en 44, y el p50 de la senal nueva es 45,8.
MIN_BLOQUE = 2
# El minimo de pasos para que la senal APLIQUE. Con MIN_BLOQUE = 2 son cuatro.
MIN_PASOS_BLOQUE = MIN_BLOQUE * 2


class NoAplica(object):
    """LO QUE LA SENAL DEVUELVE CUANDO EL NODO NO LLEGA AL MINIMO, y no es cero.

    CERO ES UNA MEDICION; ESTO ES LA AUSENCIA DE MEDICION. La averia de la
    vuelta 33 vivio meses porque la senal muerta devolvia 0,0 y ese 0,0 se
    publico como si dijera "este nodo no tiene bloque repetido". No lo decia.

    Por eso este valor NO se deja comparar con un umbral: cualquier `>=`, `<`,
    `float()` o `if` sobre el REVIENTA con el motivo escrito. Un instrumento
    que no puede medir tiene que decirlo, no devolver un numero comodo.
    """

    def __repr__(self):
        return "NO APLICA"

    def __str__(self):
        return "NO APLICA"

    def _revienta(self, *_a, **_k):
        raise TypeError(
            "NO APLICA no es un numero: la senal de bloque no aplica a este nodo "
            "(menos de %d pasos). Trata el caso, no lo compares con un umbral."
            % MIN_PASOS_BLOQUE)

    __ge__ = __gt__ = __le__ = __lt__ = __float__ = __bool__ = _revienta


NO_APLICA = NoAplica()


class CalibracionRota(RuntimeError):
    """La puerta de calibracion, que ahora vive en las senales.

    LLEVA LA MEDICION DENTRO (`detalle`) para que quien la cace pueda imprimir
    por que fallo sin volver a medir."""

    def __init__(self, faltan, detalle):
        self.faltan = faltan
        self.detalle = detalle
        RuntimeError.__init__(
            self, "INSTRUMENTO MAL CALIBRADO: %s" % ", ".join(faltan))


# ===========================================================================
# LA CALIBRACION. EL CRITERIO VA ESCRITO ARRIBA DE LA LISTA, para que quien la
# toque despues no tenga que adivinarlo ni deducirlo de los ids.
# ===========================================================================
#
# QUE ES ESTA LISTA. Los nodos contra los que el instrumento comprueba QUE
# SIGUE CAZANDO LA CLASE PARA LA QUE SE CONSTRUYO. Si alguno no aparece en la
# cola, no entrega nada y sale con codigo 1. Tienen que entrar TODOS: la puerta
# no se aflojo, se le cambio el fixture.
#
# EL CRITERIO, y cada punto se MIDIO en la vuelta 40 antes de escribirse
# (salida entera en `docs/loop/SALIDA_V40_CALIBRACION.txt`):
#
#   1. DISPARA HOY con los umbrales VIGENTES, y su medicion va impresa al lado.
#      El umbral no se mueve nunca para que un fixture entre.
#   2. ENTRA POR LA SENAL DE BLOQUE, que es la senal de la que nacio la clase.
#      Los dos fundadores entraron por bloque y no por pareja, y el propio
#      encabezado mide por que la pareja sola no calibra nada.
#   3. MAS DE UNO, Y AL MENOS UNO CON MARGEN AMPLIO. La averia que esta lista
#      repara es justo lo contrario: el fixture era uno de dos, una operacion
#      legitima recorto su nodo, y el instrumento entero se nego a entregar por
#      0,9 puntos.
#   4. SE PREFIERE EL QUE NO ESTE EN LA NOMINA DE NINGUNA OPERACION del plan,
#      medido contra `docs/plan/OPERACIONES.jsonl`. Ese es el nodo que la
#      propia campana no tiene previsto recortar, y es el que ancla la puerta.
#   5. CUANDO UN FIXTURE QUEDA RANCIO SE RETIRA DECLARADO, con su motivo y su
#      commit de origen, y se queda escrito abajo en `CALIBRACION_RETIRADA`.
#      NUNCA se afloja el umbral y nunca se borra el fixture viejo.
#
# LOS TRES DE HOY, con su medicion del 19 ago 2026 al lado (umbral de bloque
# 44, o sea que el margen es lo que sobra):
#
#   fases_traccion_producto                   bloque 72,6 corte tras 4  margen +28,6
#       EL ANCLA. El bloque mas alto del catalogo activo medido ese dia, y el
#       UNICO de los tres que NO esta en la nomina de ninguna operacion del
#       plan: la campana no tiene previsto recortarlo. Criterios 1 a 4.
#   reglas_brainstorming                      bloque 50,6 corte tras 2  margen  +6,6
#       El candidato que el acta del auditor de la vuelta 39 propuso, VERIFICADO
#       AQUI con el instrumento y no citado de aquella pagina. Su operacion
#       (OP-D-04) ya esta CERRADA, asi que no le queda corte pendiente. AVISO
#       DECLARADO: la misma acta lo mando a la cola de lectura como cualquier
#       citado, y si una lectura futura lo desteje, este fixture se retira por
#       el punto 5 igual que el anterior.
#   economia_circular_como_modelo_de_negocio  bloque 44,2 corte tras 3  margen  +0,2
#       EL FUNDADOR SUPERVIVIENTE. De los dos nodos que dieron origen a la
#       clase, es el que HOY sigue disparando, y se queda por eso. VA
#       DECLARADO FRAGIL: dos decimas de margen. No se retira mientras cumpla
#       el criterio 1 (retirar un fixture que SI dispara seria acomodar la
#       puerta), pero el aviso de borde lo va a nombrar en cada corrida.
CALIBRACION = ("fases_traccion_producto",
               "reglas_brainstorming",
               "economia_circular_como_modelo_de_negocio")

# LOS RETIRADOS, QUE NO SE BORRAN. No gobiernan la puerta, pero el instrumento
# LOS SIGUE MIDIENDO Y LOS IMPRIME en cada corrida: un fixture retirado en
# silencio es una calibracion que nadie puede auditar. Si alguno vuelve a
# disparar, el instrumento lo dice, y reincorporarlo es decision de quien lea,
# no del script.
CALIBRACION_RETIRADA = (
    {
        "node_id": "plan_mejora_procesos",
        "retirado": "19 ago 2026, vuelta 40",
        "motivo": ("fixture RANCIO: la propia campana recorto el nodo por una "
                   "operacion legitima y dejo de disparar (bloque 43,1 contra "
                   "umbral 44, por 0,9 puntos), con lo que el instrumento se "
                   "nego a entregar entero desde la vuelta 34"),
        "commit_de_origen": "2bd8dd76",
        "operacion": "OP-F-04-HOR, que lo lleva en su nomina",
        "medicion_al_retirarlo": "5 pasos, pareja 47,1, bloque 43,1 corte tras 2",
    },
)

# A cuantos puntos del umbral un fixture se considera AL BORDE y el instrumento
# lo avisa en su corrida normal, sin fallar. No es un umbral de decision: es un
# aviso, y por eso no entra en ninguna comparacion de disparo.
MARGEN_DE_AVISO = 1.0

# LA PUERTA SE MUDA A LAS SENALES (15 ago 2026, decision del fundador). Vivia en
# el `main()`, y por eso `scripts/loop/vuelta32_costura_opd01.py` pudo importar
# las senales POR DEBAJO de ella y publicar una cifra de una senal muerta. Una
# guarda que se saltea importando es un test verde y mal. Desde hoy la heredan
# `peor_pareja` y `mejor_bloque`, o sea TODA importacion.
_CALIBRACION = None   # None = sin comprobar todavia; se comprueba UNA vez


def _peor_pareja(ratio, pasos):
    """La senal 1, cruda y SIN puerta. Uso interno: la puerta la usa para
    medirse a si misma, y llamarla desde fuera se saltaria la baranda."""
    mejor = (0.0, 0, 0)
    for a in range(len(pasos)):
        for b in range(a + 1, len(pasos)):
            s = ratio(pasos[a], pasos[b])
            if s > mejor[0]:
                mejor = (s, a + 1, b + 1)
    return mejor


def _mejor_bloque(ratio, pasos):
    """La senal 2, cruda y SIN puerta. Devuelve (NO_APLICA, 0) si la lista no
    llega al minimo, y (0.0, 0) si llega pero ningun corte puntua: son dos cosas
    distintas y desde hoy se distinguen."""
    if len(pasos) < MIN_PASOS_BLOQUE:
        return (NO_APLICA, 0)
    mejor = (0.0, 0)
    n = len(pasos)
    for corte in range(MIN_BLOQUE, n - MIN_BLOQUE + 1):
        a, b = pasos[:corte], pasos[corte:]
        # Emparejamiento MONOTONO: cada paso del segundo bloque se empareja con
        # uno del primero, sin retroceder. Es lo que distingue "la secuencia
        # vuelve a empezar" de "estos dos pasos se parecen".
        j, puntajes = 0, []
        for paso in b:
            candidatos = [(ratio(a[k], paso), k) for k in range(j, len(a))]
            if not candidatos:
                break
            s, k = max(candidatos)
            puntajes.append(s)
            j = k + 1
        if len(puntajes) >= MIN_BLOQUE:
            score = sum(sorted(puntajes, reverse=True)[:MIN_BLOQUE]) / MIN_BLOQUE
            if score > mejor[0]:
                mejor = (score, corte)
    return mejor


def _ficha(ratio, nodos, nid):
    """La medicion de UN nodo con las senales CRUDAS, con su margen al lado.

    El margen es lo que le sobra a la senal de bloque por encima de su umbral, y
    existe para que un fixture al borde se pueda AVISAR antes de que caiga, en
    vez de descubrirse por un exit 1 a destiempo (la averia de la vuelta 34)."""
    pasos = (nodos.get(nid) or {}).get("pasos_accionables") or []
    sp = _peor_pareja(ratio, pasos)
    sb = _mejor_bloque(ratio, pasos)
    aplica = not isinstance(sb[0], NoAplica)
    entra = sp[0] >= UMBRAL_PAREJA
    if aplica:
        entra = entra or (bool(sb[1]) and sb[0] >= UMBRAL_BLOQUE)
    return {"pasos": len(pasos), "pareja": sp, "bloque": sb, "entra": entra,
            "existe": bool(nodos.get(nid)),
            "margen": (sb[0] - UMBRAL_BLOQUE) if aplica else None}


def medir_calibracion(ratio=None):
    """Mide los nodos de calibracion con las senales CRUDAS y dice quien entra.

    Devuelve (faltan, detalle): `faltan` son los ids que NO entran en la cola con
    los umbrales por defecto, y `detalle` trae la medicion de cada uno para que
    quien la imprima no tenga que volver a medir.
    """
    if ratio is None:
        from rapidfuzz.fuzz import token_sort_ratio as ratio
    nodos = json.loads(GRAFO.read_text(encoding="utf-8"))["nodos"]
    faltan, detalle = [], {}
    for nid in CALIBRACION:
        detalle[nid] = _ficha(ratio, nodos, nid)
        if not detalle[nid]["entra"]:
            faltan.append(nid)
    return faltan, detalle


def medir_retiradas(ratio=None):
    """Mide los fixtures RETIRADOS, que no gobiernan la puerta pero se siguen
    publicando. Un fixture retirado en silencio es una calibracion que nadie
    puede auditar, y si alguno vuelve a disparar hay que enterarse."""
    if ratio is None:
        from rapidfuzz.fuzz import token_sort_ratio as ratio
    nodos = json.loads(GRAFO.read_text(encoding="utf-8"))["nodos"]
    salida = []
    for r in CALIBRACION_RETIRADA:
        f = _ficha(ratio, nodos, r["node_id"])
        d = dict(r)
        d["medicion_de_hoy"] = f
        salida.append(d)
    return salida


def _texto_bloque(sb):
    """El bloque en texto, y NO APLICA nunca se maquilla como un cero."""
    if isinstance(sb[0], NoAplica):
        return "NO APLICA"
    return "%.1f (corte tras %d)" % (sb[0], sb[1])


def fixtures_al_borde(detalle, margen=MARGEN_DE_AVISO):
    """Los fixtures que SI entran pero por menos de `margen` puntos. El aviso que
    la puerta vieja no tenia: aviso, no fallo."""
    return [nid for nid, d in sorted(detalle.items())
            if d["entra"] and d["margen"] is not None and d["margen"] < margen]


def _asegurar_calibracion():
    """LA PUERTA. Se comprueba UNA vez por proceso y la hereda toda importacion.

    No es cosmetica: `scripts/loop/vuelta32_costura_opd01.py` importo las senales
    por debajo de la puerta vieja (que vivia en el `main()`) y publico como
    medicion un 0,0 de una senal muerta. Desde hoy, importar las senales de un
    instrumento descalibrado LEVANTA `CalibracionRota`.
    """
    global _CALIBRACION
    if _CALIBRACION is None:
        _CALIBRACION = medir_calibracion()
    faltan, detalle = _CALIBRACION
    if faltan:
        raise CalibracionRota(faltan, detalle)


def peor_pareja(ratio, pasos):
    """La pareja de pasos mas parecida del nodo: (similitud, i, j) en base 1.
    CON LA PUERTA DE CALIBRACION DELANTE."""
    _asegurar_calibracion()
    return _peor_pareja(ratio, pasos)


def mejor_bloque(ratio, pasos):
    """El corte que mejor explica la lista como DOS bloques, uno repitiendo al
    otro: (score, corte), con el corte en base 1 ('los pasos 1 a corte contra el
    resto'). Devuelve (NO_APLICA, 0) si la lista no llega a MIN_PASOS_BLOQUE.
    CON LA PUERTA DE CALIBRACION DELANTE."""
    _asegurar_calibracion()
    return _mejor_bloque(ratio, pasos)


def imprimir_calibracion_rota(err, umbral_pareja=UMBRAL_PAREJA,
                              umbral_bloque=UMBRAL_BLOQUE):
    """El texto que el instrumento lleva dando desde que la puerta existe, con la
    medicion de hoy al lado. No se maquilla ninguna cifra."""
    print("INSTRUMENTO MAL CALIBRADO. No entrega nada.")
    print("  La calibracion conocida no aparece en la cola: %s" % err.faltan)
    for nid, d in sorted(err.detalle.items()):
        sp, sb = d["pareja"], d["bloque"]
        print("    %s: %d pasos, mejor pareja %.1f (pasos %d y %d), mejor bloque %s"
              % (nid, d["pasos"], sp[0], sp[1], sp[2], _texto_bloque(sb)))
    print("  Umbrales usados: pareja %s, bloque %s" % (umbral_pareja, umbral_bloque))
    # EL CAMINO ESCRITO, ANADIDO EN LA VUELTA 40. La averia de la vuelta 34
    # vivio cinco vueltas en parte porque el diagnostico decia QUE fallaba y no
    # QUE HACER, y lo unico a mano era aflojar el umbral. Se dice aqui.
    print("")
    print("  QUE HACER, y que NO:")
    print("    NO se afloja el umbral para que el fixture entre: eso arregla la")
    print("    vara en vez de la pieza. Si la campana recorto el nodo por una")
    print("    operacion legitima, EL FIXTURE QUEDO RANCIO y se RETIRA DECLARADO")
    print("    en CALIBRACION_RETIRADA, con su motivo y su commit de origen, y")
    print("    se elige otro por el criterio escrito arriba de CALIBRACION.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--umbral-pareja", type=float, default=UMBRAL_PAREJA)
    ap.add_argument("--umbral-bloque", type=float, default=UMBRAL_BLOQUE)
    args = ap.parse_args()

    from rapidfuzz.fuzz import token_sort_ratio as ratio

    # LA PUERTA, PRIMERO Y NO AL FINAL. Antes se comprobaba despues de barrer el
    # catalogo entero; ahora vive en las senales, asi que la primera llamada la
    # dispara igual. Se pregunta aqui para poder imprimir el diagnostico entero
    # en vez de una traza.
    try:
        _asegurar_calibracion()
    except CalibracionRota as err:
        imprimir_calibracion_rota(err, args.umbral_pareja, args.umbral_bloque)
        return 1
    _faltan, detalle_calib = _CALIBRACION
    retiradas = medir_retiradas(ratio)

    nodos = json.loads(GRAFO.read_text(encoding="utf-8"))["nodos"]
    activos = {k: v for k, v in nodos.items() if not v.get("deprecado")}

    filas, sc_pareja, sc_bloque = [], [], []
    for nid, n in sorted(activos.items()):
        pasos = n.get("pasos_accionables") or []
        if len(pasos) < 2:
            continue
        s_par, i, j = peor_pareja(ratio, pasos)
        sc_pareja.append(s_par)
        s_blo, corte = mejor_bloque(ratio, pasos)
        aplica_bloque = not isinstance(s_blo, NoAplica)
        if aplica_bloque and corte:
            sc_bloque.append(s_blo)
        disparo_p = s_par >= args.umbral_pareja
        disparo_b = aplica_bloque and bool(corte) and s_blo >= args.umbral_bloque
        if not (disparo_p or disparo_b):
            continue
        filas.append({
            "node_id": nid,
            "dominio": n.get("dominio"),
            "titulo": n.get("titulo_concepto", ""),
            "pasos": len(pasos),
            "sim_pareja": round(s_par, 1),
            "pareja": [i, j],
            "paso_a": pasos[i - 1],
            "paso_b": pasos[j - 1],
            # NO APLICA no se escribe como 0.0: se escribe como null con su
            # texto al lado, para que ningun lector lo sume ni lo compare.
            "sim_bloque": round(s_blo, 1) if aplica_bloque else None,
            "sim_bloque_texto": ("%.1f" % s_blo) if aplica_bloque else "NO APLICA",
            "corte": corte,
            "disparo_pareja": disparo_p,
            "disparo_bloque": disparo_b,
            # La franja que el umbral 45 dejaba fuera. Se marca para que la
            # lectura del auditor las encuentre JUNTAS y no repartidas por la cola.
            "franja_44_45": bool(disparo_b and 44.0 <= s_blo < 45.0),
        })

    # Ordena por la señal MAS FUERTE de las dos, normalizando ambas a 0-1.
    filas.sort(key=lambda f: max(f["sim_pareja"] / 100,
                                 (f["sim_bloque"] or 0.0) / 100),
               reverse=True)

    L = []
    A = L.append
    A("# Costuras internas: nodos con texto repetido DENTRO de si mismos")
    A("")
    A("**ESTE INSTRUMENTO CITA, NO JUZGA.** Hermano chico de "
      "`scripts/gradiente_pares.py`. **Un nodo en esta lista es una cita para "
      "leer, no una costura probada.** El veredicto es **lectura textual** del "
      "auditor con visto del fundador.")
    A("")
    A("La clase nacio de dos hallazgos del gradiente: `plan_mejora_procesos` "
      "(puesto 83) y `economia_circular_como_modelo_de_negocio` (puesto 97). **No "
      "son duplicados entre nodos: son un solo nodo al que le sobran pasos.**")
    A("")
    A("## Las dos señales")
    A("")
    A("| señal | que caza | umbral |")
    A("|---|---|---:|")
    A(f"| **pareja de pasos** | el paso repetido casi literal (`token_sort_ratio`) | **{args.umbral_pareja}** |")
    A(f"| **alineacion de bloques** | la secuencia que vuelve a empezar, y **donde** | **{args.umbral_bloque}** |")
    A("")
    A("**Basta con que dispare cualquiera, y se reportan las dos siempre**, como "
      "en el hermano mayor: el auditor necesita ver por que entro cada nodo.")
    A("")
    A("### Por que hacen falta las dos, medido")
    A("")
    A("**Con la señal de pareja sola, y en cualquier umbral, la calibracion no "
      "entra.** La mejor pareja interna de `plan_mejora_procesos` es **60.0** y la "
      "de `economia_circular` **54.7**; bajar el umbral hasta ahi caza **856 "
      "nodos, el 24 por ciento del catalogo**.")
    A("")
    A("> **Una baranda que caza lo correcto no es estricta, esta rota.**")
    A("")
    A("El motivo es que esas dos costuras son **parafrasis con cola distinta**, no "
      "copias. La señal de bloques las pone en los **puestos 7 y 32 de 567** y "
      "**acierta el corte exacto en las dos**.")
    A("")
    A("> **CORRECCION DECLARADA (15 ago 2026, vuelta 34).** Las cifras del parrafo "
      "de arriba **son las del dia en que se calibro y se quedan escritas**, pero "
      "**hoy no se reproducen**: esta misma campaña destejio los dos nodos, y "
      "medidos contra el grafo de hoy dan **pareja 47,1 y 54,3** con **cinco pasos "
      "cada uno**. La señal de bloque se recalibro (`MIN_BLOQUE` de 3 a 2, señal "
      "para todo nodo de cuatro pasos o mas, `NO APLICA` explicito por debajo), y "
      "**la puerta de calibracion se mudo a las señales para que toda importacion "
      "la herede**. Detalle entero, con el costo medido, en el encabezado de "
      "`scripts/costuras_internas.py`.")
    A("")
    A("> **SEGUNDA CORRECCION DECLARADA (19 ago 2026, vuelta 40).** La puerta de "
      "arriba **quedo EN ROJO desde aquella recalibracion**: `plan_mejora_procesos` "
      "daba **43,1 contra 44** y el instrumento **no entregaba nada** (exit 1). **El "
      "roto no era el instrumento: era el fixture.** La propia campaña recorto ese "
      "nodo por una operacion legitima (`OP-F-04-HOR`, commit `2bd8dd76`), que es lo "
      "que lo dejo rancio. **La puerta se reparo cambiandole el fixture, con criterio "
      "escrito, y SIN TOCAR NI UN UMBRAL NI UN NODO**: el retirado se queda declarado "
      "abajo con su motivo. **Lo que la reparacion NO arregla y no se disfraza: la "
      "cola sigue en el 42,3 por ciento del catalogo**, que es el pendiente de "
      "doctrina del `MIN_BLOQUE = 2` y **lo decide el fundador**.")
    A("")
    A("## La calibracion conocida")
    A("")
    A("**Los nodos contra los que se comprueba que el instrumento sigue cazando "
      "la clase para la que se construyo. Tienen que entrar TODOS**, y si falta "
      "uno el instrumento no entrega nada. **El criterio de eleccion esta escrito "
      "arriba de la lista en `scripts/costuras_internas.py`.**")
    A("")
    A("| fixture | pasos | pareja | bloque | corte | margen sobre el umbral |")
    A("|---|---:|---:|---:|---:|---:|")
    for c in CALIBRACION:
        f = next(x for x in filas if x["node_id"] == c)
        d = detalle_calib.get(c) or {}
        m = d.get("margen")
        A(f"| **CAZADO** `{c}` | {f['pasos']} | {f['sim_pareja']} | "
          f"{f['sim_bloque_texto']} | {f['corte']} | "
          f"{('%+.1f' % m) if m is not None else 'NO APLICA'} |")
    A("")
    borde = fixtures_al_borde(detalle_calib)
    if borde:
        A(f"> **AVISO DE BORDE: {len(borde)} fixture o mas esta a menos de "
          f"{MARGEN_DE_AVISO:.1f} puntos del umbral** ({', '.join('`%s`' % b for b in borde)}). "
          "**No es un fallo y no cambia nada hoy**, pero es el mismo sitio del que "
          "vino la averia de la vuelta 34: un fixture al borde cae con cualquier "
          "recorte legitimo del nodo. **Se dice para que la proxima se vea venir.**")
        A("")
    if CALIBRACION_RETIRADA:
        A("### Los fixtures RETIRADOS, que no se borran")
        A("")
        A("**No gobiernan la puerta, pero se siguen midiendo y publicando en cada "
          "corrida**: un fixture retirado en silencio es una calibracion que nadie "
          "puede auditar.")
        A("")
        A("| fixture retirado | cuando | por que | commit de origen | como quedo hoy |")
        A("|---|---|---|---|---|")
        for r in retiradas:
            f = r["medicion_de_hoy"]
            hoy = ("**VUELVE A DISPARAR**" if f["entra"] else "sigue sin disparar")
            A(f"| `{r['node_id']}` | {r['retirado']} | {r['motivo']} | "
              f"`{r['commit_de_origen']}` ({r['operacion']}) | {hoy}: "
              f"{f['pasos']} pasos, pareja {f['pareja'][0]:.1f}, bloque "
              f"{_texto_bloque(f['bloque'])} |")
        A("")
    A("## Conteos")
    A("")
    A(f"**{len(filas)} nodos** en la cola, sobre {len(activos)} activos.")
    A("")
    por_dom = {}
    for f in filas:
        por_dom[f["dominio"]] = por_dom.get(f["dominio"], 0) + 1
    A("| dominio | nodos |")
    A("|---|---:|")
    for dom, c in sorted(por_dom.items(), key=lambda x: -x[1]):
        A(f"| {dom} | {c} |")
    A("")
    A("## Distribucion, para calibrar")
    A("")
    A("| percentil | mejor pareja interna | alineacion de bloques |")
    A("|---|---:|---:|")
    qp = statistics.quantiles(sc_pareja, n=100)
    qb = statistics.quantiles(sc_bloque, n=100)
    for etiqueta, k in (("p50", 50), ("p90", 90), ("p99", 99)):
        A(f"| {etiqueta} | {qp[k - 1]:.1f} | {qb[k - 1]:.1f} |")
    A(f"| maximo | {max(sc_pareja):.1f} | {max(sc_bloque):.1f} |")
    A("")
    A(f"Nodos evaluados por bloques ({MIN_PASOS_BLOQUE} pasos o mas): "
      f"**{len(sc_bloque)}**. Los de menos dan **NO APLICA**, que no es cero.")
    A("")
    franja = [f for f in filas if f["franja_44_45"]]
    A("## La franja 44 a 45: lo que el umbral viejo dejaba fuera")
    A("")
    A(f"**{len(franja)} citas** entraron al bajar el umbral de bloque de 45 a 44. "
      "**Van juntas aqui a proposito**, para que la lectura del auditor las "
      "encuentre sin rastrearlas por la cola.")
    A("")
    A("| # | dominio | nodo | pasos | bloque | corte |")
    A("|---:|---|---|---:|---:|---:|")
    for i, f in enumerate(sorted(franja, key=lambda x: -x["sim_bloque"]), 1):
        A(f"| {i} | {f['dominio']} | `{f['node_id']}` | {f['pasos']} | "
          f"{f['sim_bloque']} | {f['corte']} |")
    A("")
    A("**El motivo del cambio fue un FALSO NEGATIVO medido**: "
      "`nucleo/propuesta_gasto_capital`, con costura confirmada por lectura, quedaba "
      "fuera por **0,9 puntos** (bloque 44,1). **La señal si lo habia visto**: su "
      "corte propuesto es tras el paso 5, exactamente donde la lectura encontro la "
      "costura.")
    A("")
    A("## EL LIMITE DECLARADO, que bajar el umbral NO cierra")
    A("")
    A("**Bajar el umbral recupera a ESE falso negativo. No cierra el mecanismo que "
      "lo produjo.**")
    A("")
    A("> **Un comparador de tokens no ve equivalencias semanticas, a ningun "
      "umbral.** En el nodo recuperado, el paso 3 dice *\"calcular NPV usando el "
      "hurdle rate\"* y el 11 dice *\"calcular el valor presente neto (VPN)\"*. "
      "**Son la misma cosa con la sigla en dos idiomas, y para este instrumento se "
      "parecen un 46,2.**")
    A("")
    A("**Las redes que quedan debajo, y por eso el limite se declara en vez de "
      "taparse:**")
    A("")
    A("| red | que caza que este instrumento no |")
    A("|---|---|")
    A("| **(a) los rebotes del gradiente** | ya cazaron **cuatro** costuras sin buscarlas, leyendo pares por otra razon |")
    A("| **(b) el barrido semantico intra-dominio** del final | los embeddings **si** ven que `NPV` y `VPN` viven juntos |")
    A("| **(c) la pasada unica** | relee **entero** cada nodo que toca antes de destejerlo |")
    A("")
    A("> **Ninguna cola sustituye a leer el nodo.** Este instrumento ordena la "
      "lectura; no la reemplaza.")
    A("")
    A("## Los veinte primeros")
    A("")
    A("| # | dominio | nodo | pasos | pareja | bloque | corte | entro por |")
    A("|---:|---|---|---:|---:|---:|---:|---|")
    for i, f in enumerate(filas[:20], 1):
        por = []
        if f["disparo_pareja"]:
            por.append("pareja")
        if f["disparo_bloque"]:
            por.append("bloque")
        A(f"| {i} | {f['dominio']} | `{f['node_id']}` | {f['pasos']} | "
          f"{f['sim_pareja']} | {f['sim_bloque_texto']} | {f['corte'] or ''} | "
          f"{' y '.join(por)} |")
    A("")
    A(f"La cola completa, con los dos pasos de cada pareja, en `{SALIDA.name}`.")
    # Todo lo que venga despues de la marca MANUAL en el resumen anterior se
    # CONSERVA. El resumen es un archivo generado, y sin esto el informe de
    # cierre escrito a mano se perderia en la siguiente regeneracion SIN DEJAR
    # RASTRO. Misma solucion que en scripts/intra_dominio.py.
    manual = ""
    if RESUMEN.exists():
        previo = RESUMEN.read_text(encoding="utf-8")
        if MARCA_MANUAL in previo:
            manual = previo[previo.index(MARCA_MANUAL):].rstrip() + "\n"
    RESUMEN.write_text("\n".join(L) + "\n" + manual, encoding="utf-8")

    with open(SALIDA, "w", encoding="utf-8") as fh:
        for f in filas:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")

    print(f"  nodos en la cola: {len(filas)} | escrito {SALIDA.name} y {RESUMEN.name}")
    print(f"  calibracion: los {len(CALIBRACION)} nodos conocidos, CAZADOS")
    for c in CALIBRACION:
        d = detalle_calib[c]
        m = d["margen"]
        print("    %-44s %d pasos | pareja %5.1f | bloque %-22s | margen %s"
              % (c, d["pasos"], d["pareja"][0], _texto_bloque(d["bloque"]),
                 ("%+.1f" % m) if m is not None else "NO APLICA"))
    for b in fixtures_al_borde(detalle_calib):
        print("  AVISO DE BORDE: el fixture %s entra por menos de %.1f puntos "
              "(margen %+.1f). No es un fallo; es el sitio del que vino la averia "
              "de la vuelta 34." % (b, MARGEN_DE_AVISO, detalle_calib[b]["margen"]))
    for r in retiradas:
        f = r["medicion_de_hoy"]
        print("  RETIRADO y NO borrado: %s (%s, commit %s) | hoy: bloque %s, %s"
              % (r["node_id"], r["retirado"], r["commit_de_origen"],
                 _texto_bloque(f["bloque"]),
                 "VUELVE A DISPARAR" if f["entra"] else "sigue sin disparar"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
