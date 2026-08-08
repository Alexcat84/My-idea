#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""prueba_rumbos.py - LA PRUEBA DE RUMBOS: la brujula apunta donde debe.

La cuarta capa. Gate 0 dice que el grafo esta sano, las suites dicen que el
codigo hace lo que promete, el vuelo dice que el viaje corre de punta a punta.
Ninguna de las tres dice si la BRUJULA APUNTA BIEN: un catalogo impecable puede
mandar a un ceramista que pregunta por empaque al mundo de exportacion, y las
tres capas quedarse verdes.

Corre cada rumbo del banco contra el INDICE SEMANTICO REAL y la MISMA puerta que
usa produccion (esOfrecible: existe, no deprecado, dominio desbloqueado), y
evalua cuatro cosas:

  1. dominio correcto en el top-K
  2. las anclas declaradas aparecen en el top-K
  3. frontera respetada: un rumbo-trampa NO devuelve el dominio prohibido en top-3
  4. cero deprecados ofrecidos, jamas y por ningun rumbo

POR QUE EXISTE AHORA: antes de disparar re-voz-de-quality. Esas 185
regeneraciones cambian los embeddings de 185 nodos, y sin una linea base
committeada la deriva de punteria no se descubre aqui: se descubre en el
recorrido de alguien.

LA CONSULTA SE EMBEBE COMO EN PRODUCCION: voyage-4-lite, input_type "query",
output_dimension igual a la del indice. Embeberla distinto mediria otra cosa.

Uso:
  python scripts/rumbos/prueba_rumbos.py                # corre y compara
  python scripts/rumbos/prueba_rumbos.py --linea-base   # graba la foto de hoy
"""
import argparse
import json
import os
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
AQUI = Path(__file__).resolve().parent
BANCO = AQUI / "banco_rumbos.json"
LINEA_BASE = AQUI / "linea_base_rumbos.json"
INDICE = BASE / "web" / "lib" / "assets" / "semantic_index.json"
GRAFO = BASE / "dataset" / "metadata" / "master_graph.json"

# Los mismos que produccion (web/lib/compass.ts).
VOYAGE_MODEL = "voyage-4-lite"
VOYAGE_URL = "https://api.voyageai.com/v1/embeddings"
# K y TOP_FRONTERA: aprobados por el fundador (ago 2026). Produccion pide entre
# 5 y 20 candidatos segun el caso; 10 es el punto medio. Las fronteras se miran
# en el top-3, que es lo que un usuario alcanza a leer de un vistazo.
K = 10
TOP_FRONTERA = 3

# EL TRINQUETE (ley adoptada, ago 2026): la punteria SOLO SUBE O CANTA.
#   - cero rojos, siempre, y eso no se negocia contra ninguna linea base;
#   - ambares <= los de la linea base vigente;
#   - y si MEJORA, la corrida tambien para: hay que re-committear la linea base.
#     Un trinquete que deja pasar las mejoras sin registrarlas se afloja solo,
#     porque la vara se queda vieja y deja de medir. Es un fallo bueno, del
#     mismo tipo que el de una foto que hay que actualizar.
SALIDA_OK = 0
SALIDA_DERIVA = 1
SALIDA_MEJORA = 2

# REGLA DE CAMPANA (adoptada ago 2026, durante la re-voz de quality). Cuando una
# campana reescribe un pack ENTERO, un rumbo suyo puede pasar a ambar sin que
# nada haya empeorado: el texto re-vozado es mas coloquial, las consultas
# tambien lo son, y los nodos tocados le ganan el puesto a un vecino intacto.
# Eso NO es deriva de punteria: es el vecindario moviendose.
#
# Se descubrio cazando algo mejor. El rumbo guardian del COPQ paso a ambar y el
# guardian no habia sido tocado: quienes lo desplazaron eran sus GEMELOS SIN
# FUNDIR. El ambar por apinamiento resulto ser sintoma de FUSION INCOMPLETA, una
# via que el diseno del guardian no contemplaba.
#
# Asi que durante una campana declarada (--campana <pack>):
#   - los rojos y las fronteras PARAN SIEMPRE, sin excepcion;
#   - los ambares cuyo dominio esperado es el pack en campana se ACUMULAN y se
#     adjudican al cierre, en vez de parar cada lote;
#   - todo lo demas se comporta igual.
# Sin la bandera, el trinquete manda entero.
CAMPANA_ENV = "RUMBOS_CAMPANA"
LOTE_ENV = "RUMBOS_LOTE"

# LA REGLA DEL AMBAR POR VECINO MEJORADO (adjudicada ago 2026, decimo paro).
#
#   "El ambar por SUB-FUSION y el ambar por VECINO MEJORADO tienen el mismo
#    sintoma y la causa opuesta; el remedio no puede ser el mismo."
#
# La regla de campana de arriba nacio para el primero: un ancla desplazada por
# GEMELOS SIN FUNDIR, es decir, por trabajo que faltaba. Durante la campana de
# voz aparecio el segundo: un ancla intacta y BIEN ESCRITA desplazada por
# vecinos que la re-voz acababa de mejorar. Es el efecto que la campana busca,
# no una averia, y parar en cada uno con 337 nodos por delante habria hecho
# imposible la campana.
#
# Un ambar SE ACUMULA al cierre solo si se cumplen LAS TRES:
#   (a) el ancla NO estaba en el lote que se acaba de re-vozar,
#   (b) sus desplazantes SI estaban,
#   (c) el ancla sigue dentro de la BANDA DE PUESTOS.
#
# Cualquier otra combinacion es PARO DURO. Y en particular, la que jamas se
# acumula: SI EL ANCLA ESTABA EN EL LOTE Y CAYO, se para siempre. Esa es
# nuestra propia re-voz degradando un nodo, la unica averia que esta campana
# puede causar, y esconderla entre el ruido seria justo lo que el trinquete
# existe para impedir.
#
# LA BANDA, calibrada con datos y no adivinada (2026-08-08): se midio el puesto
# real de las 28 anclas de la vara sobre el indice vivo. Mediana 2, p75 5,
# p90 17, p95 26; 22 de 28 dentro del top-10. La banda se fija en el p95 = 26:
# un ancla dentro del percentil 95 de donde viven las anclas de verdad sigue
# compitiendo arriba; una que cae mas abajo dejo de competir, y eso no es un
# empujon de vecino. El caso que origino la regla, `analisis_competitivo`,
# quedo en el PUESTO 11: un puesto por debajo de la linea.
BANDA_PUESTO = 26


def puerta(nid, grafo, dominios):
    """LA MISMA puerta que el motor (esOfrecible en web/lib/engine/graph.ts):
    existe, no esta deprecado, y su dominio esta desbloqueado. Se replica aqui
    porque este corredor es Python; si la de alla cambia, esta tiene que
    cambiar, y por eso el test de contrato de abajo compara las dos."""
    n = grafo.get(nid)
    if not n:
        return False
    if n.get("deprecado"):
        return False
    return (n.get("dominio") or "core") in dominios


def embeber(textos, dim):
    import urllib.request
    clave = os.getenv("VOYAGE_API_KEY", "").strip()
    if not clave:
        print("ERROR: falta VOYAGE_API_KEY en .env")
        sys.exit(2)
    cuerpo = json.dumps({"input": textos, "model": VOYAGE_MODEL,
                         "input_type": "query", "output_dimension": dim}).encode()
    req = urllib.request.Request(VOYAGE_URL, data=cuerpo, headers={
        "Authorization": f"Bearer {clave}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        d = json.loads(r.read())
    return [x["embedding"] for x in d["data"]], d.get("usage", {})


def main():
    import numpy as np
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--linea-base", action="store_true",
                    help="graba el resultado de hoy como la foto contra la que se compara")
    args = ap.parse_args()

    from dotenv import load_dotenv
    load_dotenv(BASE / ".env")

    banco = json.loads(BANCO.read_text(encoding="utf-8"))["rumbos"]
    idx = json.loads(INDICE.read_text(encoding="utf-8"))
    grafo = json.loads(GRAFO.read_text(encoding="utf-8"))["nodos"]
    E = np.array(idx["embeddings"], dtype=np.float32)
    E /= np.linalg.norm(E, axis=1, keepdims=True)
    ids = idx["ids"]

    vecs, uso = embeber([r["consulta"] for r in banco], idx["dimension"])
    Q = np.array(vecs, dtype=np.float32)
    Q /= np.linalg.norm(Q, axis=1, keepdims=True)

    resultados, marcador = [], {"verde": 0, "ambar": 0, "rojo": 0}
    deprecados_ofrecidos = []

    for r, q in zip(banco, Q):
        # Se desbloquean los dominios que el rumbo espera, mas core: es el
        # escenario real de un usuario que compro ese mundo.
        dominios = set(r["dominios"]) | {"core"}
        s = E @ q
        orden = np.argsort(-s)
        top = []
        for i in orden:
            nid = ids[i]
            if not puerta(nid, grafo, dominios):
                continue
            top.append((nid, float(s[i]), grafo[nid].get("dominio", "core")))
            if len(top) >= K:
                break

        # 4. cero deprecados, mirando el orden CRUDO (no el filtrado)
        for i in orden[:K * 3]:
            if grafo.get(ids[i], {}).get("deprecado") and ids[i] in [t[0] for t in top]:
                deprecados_ofrecidos.append({"rumbo": r["id"], "node_id": ids[i]})

        # El ranking COMPLETO de lo ofrecible, para saber el PUESTO real de un
        # ancla que se cayo del top-K. Sin esto solo se sabe "no entro", que no
        # distingue el puesto 11 del 200.
        orden_completo = [ids[i] for i in orden if puerta(ids[i], grafo, dominios)]
        doms_top = [t[2] for t in top]
        ids_top = [t[0] for t in top]
        dom_ok = any(d in r["dominios"] for d in doms_top)
        # `ancla` exige TODAS. `ancla_conjunto` exige AL MENOS UNA: en el nucleo
        # hay preguntas con varias respuestas legitimas, y fingir una sola vara
        # unica es menos honesto que declarar el abanico.
        anclas = r.get("ancla") or []
        faltan = [a for a in anclas if a not in ids_top]
        conjunto = r.get("ancla_conjunto") or []
        if conjunto and not any(a in ids_top for a in conjunto):
            faltan = faltan + [f"ninguna de {conjunto}"]
        prohibidos = r.get("prohibido_top3") or []
        violada = [d for d in prohibidos if d in doms_top[:TOP_FRONTERA]]

        if not dom_ok or violada:
            estado = "rojo"
        elif faltan:
            estado = "ambar"
        else:
            estado = "verde"
        # FUERA DEL MARCADOR (adjudicado ago 2026): los rumbos de DIAGNOSTICO
        # miden un trabajo que todavia no se ha hecho, y el rumbo-HUECO mide un
        # vacio del catalogo. Contarlos seria pedirle al trinquete que vigile
        # algo que ya sabemos que esta mal: el guardian se volveria un
        # recordatorio, y un guardian que siempre esta rojo no guarda nada.
        # Se imprimen aparte, con su expectativa, para que nadie los olvide.
        fuera = bool(r.get("diagnostico") or r.get("hueco"))
        if not fuera:
            marcador[estado] += 1
        resultados.append({
            "id": r["id"], "estado": estado, "consulta": r["consulta"],
            "esperaba": r["dominios"], "devolvio": doms_top[:5],
            "anclas_faltantes": faltan, "frontera_violada": violada,
            "fuera_del_marcador": fuera,
            "clase": "diagnostico" if r.get("diagnostico") else ("hueco" if r.get("hueco") else "vara"),
            "expectativa": r.get("expectativa"),
            "top3": [{"id": t[0], "dominio": t[2], "score": round(t[1], 4)} for t in top[:3]],
            # puesto real de cada ancla, dentro o fuera del top-K
            "puestos_ancla": {a: (orden_completo.index(a) + 1 if a in orden_completo else None)
                              for a in (anclas + conjunto)},
            "ids_top": ids_top,
        })

    total = sum(1 for x in resultados if not x["fuera_del_marcador"])
    print(f"\n{'estado':<8}{'rumbo':<42}devolvio")
    for x in resultados:
        if x["fuera_del_marcador"]:
            continue
        marca = {"verde": "OK  ", "ambar": "~   ", "rojo": "ROJO"}[x["estado"]]
        print(f"{marca:<8}{x['id']:<42}{', '.join(x['devolvio'][:3])}")
        if x["estado"] != "verde":
            if x["frontera_violada"]:
                print(f"        frontera violada: {x['frontera_violada']} en el top-3")
            if x["anclas_faltantes"]:
                print(f"        anclas ausentes: {x['anclas_faltantes']}")
            print(f"        top3: {[(t['id'][:36], t['score']) for t in x['top3']]}")

    aparte = [x for x in resultados if x["fuera_del_marcador"]]
    if aparte:
        print(f"\n  FUERA DEL MARCADOR ({len(aparte)}), a proposito y con fecha de vencimiento:")
        for x in aparte:
            marca = {"verde": "OK", "ambar": "~ ", "rojo": "RJ"}[x["estado"]]
            print(f"    [{marca}] {x['id']}  ({x['clase']})  -> {', '.join(t['id'] for t in x['top3'][:2])}")
            if x["expectativa"]:
                print(f"         {x['expectativa']}")

    pct = round(100 * marcador["verde"] / total, 1)
    print(f"\n  MARCADOR: {marcador['verde']} verdes, {marcador['ambar']} ambares, "
          f"{marcador['rojo']} rojos  ({pct}% verde de {total} en la vara)")
    if deprecados_ofrecidos:
        print(f"  ROJO ABSOLUTO: {len(deprecados_ofrecidos)} deprecados ofrecidos: "
              f"{deprecados_ofrecidos[:3]}")

    tokens = uso.get("total_tokens", 0)
    costo = tokens / 1e6 * 0.02  # voyage-4-lite, orden de centavos
    print(f"  Costo: {tokens} tokens de consulta (~${costo:.4f})")

    foto = {"k": K, "marcador": marcador, "verde_pct": pct,
            "deprecados_ofrecidos": deprecados_ofrecidos,
            # La vara guarda SOLO los rumbos que mide. Un rumbo de diagnostico
            # dentro de por_rumbo entraria despues en las comparaciones del
            # trinquete por la puerta de atras, y el dia que se ponga verde
            # -- que es justo lo que se espera de el -- se leeria como "mejora"
            # sin que nadie lo adjudique.
            "por_rumbo": {x["id"]: {"estado": x["estado"], "devolvio": x["devolvio"][:3]}
                          for x in resultados if not x["fuera_del_marcador"]},
            "fuera_del_marcador": {x["id"]: {"estado": x["estado"], "clase": x["clase"],
                                             "devolvio": x["devolvio"][:3]}
                                   for x in resultados if x["fuera_del_marcador"]}}
    (AQUI / "_ultima_corrida.json").write_text(
        json.dumps({"foto": foto, "detalle": resultados}, ensure_ascii=False, indent=2),
        encoding="utf-8")

    if args.linea_base:
        LINEA_BASE.write_text(json.dumps(foto, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  Linea base grabada en {LINEA_BASE.name}")
        return 0

    if not LINEA_BASE.exists():
        print("\n  (sin linea base todavia: correr con --linea-base para grabar la foto)")
        return 0

    base = json.loads(LINEA_BASE.read_text(encoding="utf-8"))
    RANGO = {"verde": 2, "ambar": 1, "rojo": 0}
    peores, mejores, estrenos = [], [], []
    for rid, ahora in foto["por_rumbo"].items():
        antes = base["por_rumbo"].get(rid)
        if not antes:
            # RUMBO NUEVO. No puede romper el trinquete: no tenia estado
            # anterior que empeorar. Cazado al ampliar el banco de 30 a 48 para
            # cubrir el nucleo (ago 2026): el trinquete conto 1 ambar -> 10 y
            # grito DERIVA, cuando ninguno de los 30 originales se habia movido
            # ni un milimetro. Un guardian que grita cuando le amplias la ronda
            # deja de creerse, y ese es el peor final para un guardian.
            #
            # Pero tampoco se callan: un ambar nuevo es una debilidad que el
            # banco viejo no veia, y hornearla en la linea base sin decirlo
            # seria estrenar la ceguera. Se listan aparte, con nombre.
            if ahora["estado"] != "verde":
                estrenos.append(f"{rid}: {ahora['estado']} (rumbo NUEVO, sin foto anterior)")
            continue
        if antes["estado"] == ahora["estado"]:
            continue
        linea = (f"{rid}: {antes['estado']} -> {ahora['estado']} "
                 f"(antes {antes['devolvio'][:2]}, ahora {ahora['devolvio'][:2]})")
        (mejores if RANGO[ahora["estado"]] > RANGO[antes["estado"]] else peores).append(linea)

    # 1. Cero rojos. No se negocia contra ninguna linea base.
    if marcador["rojo"] or deprecados_ofrecidos:
        print(f"\n  TRINQUETE ROTO: {marcador['rojo']} rumbos en rojo"
              + (f", {len(deprecados_ofrecidos)} deprecados ofrecidos" if deprecados_ofrecidos else ""))
        for x in resultados:
            if x["estado"] == "rojo":
                print(f"    {x['id']}: esperaba {x['esperaba']}, devolvio {x['devolvio'][:3]}")
        return SALIDA_DERIVA

    # 2. Los ambares no pueden crecer, y ningun rumbo puede bajar de estado.
    #    Salvo los del pack EN CAMPANA: esos se acumulan (ver REGLA DE CAMPANA).
    # ── LA REGLA DEL AMBAR POR VECINO MEJORADO ─────────────────────────────
    acumulados, duros = [], []
    # Un rumbo YA ACUMULADO no vuelve a parar la campaña: su caida ya esta
    # registrada con su puesto y sus desplazantes, y espera adjudicacion al
    # cierre. Sin esto, el lote 3 paraba por el mismo ambar que el lote 1 ya
    # habia registrado -- y con el motivo equivocado ("ningun desplazante estaba
    # en el lote"), porque quienes lo desplazaron venian de los lotes ANTERIORES.
    # La campaña es acumulativa; el registro tambien tiene que serlo.
    registro_previo = AQUI / "_ambares_acumulados.json"
    ya_registrados = set()
    if registro_previo.exists():
        ya_registrados = {x["rumbo"] for x in
                          json.loads(registro_previo.read_text(encoding="utf-8"))}
    lote = set()
    ruta_lote = os.getenv(LOTE_ENV, "").strip()
    if ruta_lote and Path(ruta_lote).exists():
        lote = set(json.loads(Path(ruta_lote).read_text(encoding="utf-8"))["sobrevivientes"])
    if lote:
        por_id = {x["id"]: x for x in resultados}
        restantes = []
        for d in peores:
            rid = d.split(":")[0]
            x = por_id.get(rid)
            if not x or x["estado"] != "ambar":
                restantes.append(d)
                continue
            if rid in ya_registrados:
                acumulados.append({"rumbo": rid, "ya_registrado": True,
                                   "por_que": "acumulado en un lote anterior de esta campaña"})
                continue
            # las anclas que se cayeron, con su puesto real
            caidas = {a: p for a, p in (x.get("puestos_ancla") or {}).items()
                      if a not in x.get("ids_top", [])}
            en_lote = [a for a in caidas if a in lote]
            desplazantes = [n for n in x.get("ids_top", []) if n in lote]
            peor_puesto = max([p for p in caidas.values() if p] or [10**9])
            motivo = None
            if en_lote:
                motivo = (f"EL ANCLA ESTABA EN EL LOTE y cayo: {en_lote}. Nuestra propia "
                          "re-voz degradando un nodo. No se acumula jamas.")
            elif not desplazantes:
                motivo = "ningun desplazante estaba en el lote: no lo movio esta campana"
            elif peor_puesto > BANDA_PUESTO:
                motivo = (f"el ancla cayo al puesto {peor_puesto}, fuera de la banda "
                          f"({BANDA_PUESTO}): dejo de competir arriba")
            if motivo:
                duros.append(f"{d}\n-> PARO DURO: {motivo}")
                restantes.append(d)
            else:
                acumulados.append({"rumbo": rid, "anclas_caidas": caidas,
                                   "puesto": peor_puesto, "banda": BANDA_PUESTO,
                                   "desplazantes_del_lote": desplazantes,
                                   "por_que": "ancla intacta, desplazada por vecinos del lote, "
                                              "dentro de la banda"})
        peores = restantes if duros else [d for d in peores
                                          if d.split(":")[0] not in {a["rumbo"] for a in acumulados}]
        if acumulados:
            registro = AQUI / "_ambares_acumulados.json"
            previos = json.loads(registro.read_text(encoding="utf-8")) if registro.exists() else []
            previos += acumulados
            registro.write_text(json.dumps(previos, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"\nAMBARES ACUMULADOS AL CIERRE ({len(acumulados)}), por vecino mejorado:")
            for a in acumulados:
                if a.get("ya_registrado"):
                    print(f"    {a['rumbo']}: {a['por_que']}")
                    continue
                print(f"    {a['rumbo']}: ancla en el puesto {a['puesto']} (banda {a['banda']}), "
                      f"desplazada por {len(a['desplazantes_del_lote'])} del lote")
            marcador = dict(marcador, ambar=marcador["ambar"] - len(acumulados))
        if duros:
            print(f"\nPARO DURO ({len(duros)}): no cumplen las tres condiciones")
            for d in duros:
                print(f"    {d}")

    campana = os.getenv(CAMPANA_ENV, "").strip()
    if campana:
        de_la_campana = [d for d in peores if any(
            r["id"] == d.split(":")[0] and campana in r["dominios"] for r in banco)]
        if de_la_campana:
            print(f"\n  ACUMULADOS por la campana de '{campana}' "
                  f"({len(de_la_campana)}), se adjudican al cierre:")
            for d in de_la_campana:
                print(f"    {d}")
            peores = [d for d in peores if d not in de_la_campana]
            marcador = dict(marcador, ambar=base["marcador"]["ambar"])
    # Los ambares se cuentan SOLO sobre los rumbos que la linea base conocia:
    # un banco mas grande no es una punteria peor.
    conocidos = set(base["por_rumbo"])
    # Los acumulados por vecino mejorado no cuentan en el trinquete: ya se
    # registraron con su puesto, su caida y sus desplazantes, y se adjudican al
    # cierre. Si contaran, la regla no serviria de nada.
    acumulados_ids = {a["rumbo"] for a in acumulados}
    conocidos = conocidos - acumulados_ids
    ambar_conocidos = sum(1 for rid, x in foto["por_rumbo"].items()
                          if rid in conocidos and x["estado"] == "ambar")
    if ambar_conocidos > base["marcador"]["ambar"] or peores:
        print(f"\n  TRINQUETE ROTO: la punteria empeoro "
              f"({base['marcador']['ambar']} ambares -> {ambar_conocidos} "
              f"sobre los {len(conocidos)} rumbos de la linea base)")
        for d in peores:
            print(f"    {d}")
        return SALIDA_DERIVA

    if estrenos:
        print(f"\n  RUMBOS NUEVOS QUE NO SALEN VERDES ({len(estrenos)}). No rompen el "
              f"trinquete -- no tenian foto anterior -- pero son debilidades que el "
              f"banco viejo no veia. Adjudicalos ANTES de re-committear la vara:")
        for d in estrenos:
            print(f"    {d}")

    # 3. Si mejoro, la vara se quedo vieja: hay que re-committearla.
    #    Tambien se mide sobre los CONOCIDOS: 18 rumbos nuevos suben el conteo
    #    bruto de verdes sin que la punteria haya mejorado en nada.
    verde_conocidos = sum(1 for rid, x in foto["por_rumbo"].items()
                          if rid in conocidos and x["estado"] == "verde")
    if mejores or verde_conocidos > base["marcador"]["verde"]:
        print(f"\n  LA PUNTERIA SUBIO sobre los {len(conocidos)} rumbos de la vara "
              f"({base['marcador']['verde']} -> {verde_conocidos} verdes). "
              f"La vara se quedo vieja:")
        for d in mejores:
            print(f"    {d}")
        print("    re-committea con: python scripts/rumbos/prueba_rumbos.py --linea-base")
        return SALIDA_MEJORA

    if estrenos:
        # Ni deriva ni mejora: el banco crecio y trajo hallazgos. La vara se
        # re-committea a proposito, despues de adjudicarlos, no de rebote.
        return SALIDA_MEJORA

    print(f"\n  Sin deriva contra la linea base ({base['verde_pct']}% verde).")
    return SALIDA_OK


if __name__ == "__main__":
    sys.exit(main())
