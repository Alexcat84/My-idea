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


# Los dos nodos que dieron origen a la clase. Si el instrumento no los caza, no
# sirve para lo que se construyo y no entrega nada.
CALIBRACION = ("plan_mejora_procesos", "economia_circular_como_modelo_de_negocio")

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
        pasos = (nodos.get(nid) or {}).get("pasos_accionables") or []
        sp = _peor_pareja(ratio, pasos)
        sb = _mejor_bloque(ratio, pasos)
        entra = sp[0] >= UMBRAL_PAREJA
        if not isinstance(sb[0], NoAplica):
            entra = entra or (bool(sb[1]) and sb[0] >= UMBRAL_BLOQUE)
        detalle[nid] = {"pasos": len(pasos), "pareja": sp, "bloque": sb, "entra": entra}
        if not entra:
            faltan.append(nid)
    return faltan, detalle


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
              % (nid, d["pasos"], sp[0], sp[1], sp[2],
                 ("NO APLICA" if isinstance(sb[0], NoAplica)
                  else "%.1f (corte tras %d)" % (sb[0], sb[1]))))
    print("  Umbrales usados: pareja %s, bloque %s" % (umbral_pareja, umbral_bloque))


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
    A("## La calibracion conocida")
    A("")
    for c in CALIBRACION:
        f = next(x for x in filas if x["node_id"] == c)
        A(f"**CAZADO** `{c}`: pareja **{f['sim_pareja']}**, bloque "
          f"**{f['sim_bloque_texto']}** con el corte **tras el paso {f['corte']}**.")
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
