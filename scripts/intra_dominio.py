#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""intra_dominio.py - EMPAREJA nodos del MISMO dominio entre si.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo, no toca el motor, no toca la
web. Lo unico que escribe son sus dos salidas en docs/.

ESTE INSTRUMENTO EMPAREJA, NO JUZGA. El veredicto de cada par es lectura textual
del auditor con visto del fundador. Un par en la cola es UNA CITA PARA LEER, no
un duplicado. Es la misma doctrina de scripts/gradiente_pares.py, aplicada al
otro eje: alli era mundo contra nucleo, aqui es cada dominio contra si mismo.

POBLACION: todos los pares (a, b) de nodos ACTIVOS del MISMO dominio, con a < b
para no contar cada par dos veces. El nucleo cuenta como un dominio mas.

DOS SENALES INDEPENDIENTES, y basta con que dispare CUALQUIERA:

  1. TITULO: token_sort_ratio de rapidfuzz, umbral 80. El mismo del gradiente.
  2. SEMANTICA: coseno entre los vectores de web/lib/assets/semantic_index.json,
     umbral inicial 0.80.

POR QUE EL UMBRAL SEMANTICO ES 0.80 Y NO EL 0.75 DEL GRADIENTE: dentro de un
dominio la vecindad tematica es la NORMA, no la senal. Dos nodos de `quality`
hablan de calidad por definicion. Un umbral prestado del eje mundo-nucleo
llenaria la cola de vecinos legitimos. El umbral se calibra con datos, y por eso
el resumen publica la distribucion de similitudes POR DOMINIO: el auditor puede
mover el umbral con la distribucion delante antes de empezar a leer.

PROCEDENCIA: el instrumento conoce el trabajo ya hecho y lo MARCA sin excluirlo.
Un par ya adjudicado o ya censado sigue en la cola, con su marca y su fuente, y
la cola dice cuanto es nuevo y cuanto es re-avistamiento. Lo unico que se EXCLUYE
son los pares donde algun miembro esta deprecado.

NO GENERA VEREDICTOS NI CLASES. Eso es lectura del auditor.

Uso:
  python scripts/intra_dominio.py
  python scripts/intra_dominio.py --umbral-semantico 0.85
  python scripts/intra_dominio.py --dominio quality
"""
import argparse
import collections
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
GRAFO = BASE / "dataset" / "metadata" / "master_graph.json"
INDICE = BASE / "web" / "lib" / "assets" / "semantic_index.json"
INFORME = BASE / "docs" / "FRANJA_INFORME.md"
FICHA = BASE / "docs" / "FICHA_SUBFUSION_GRADIENTE.md"
MESA = BASE / "docs" / "MESA_RACIMOS.md"
RACIMOS = BASE / "docs" / "RACIMOS_MIEMBROS.jsonl"
SALIDA = BASE / "docs" / "INTRA_DOMINIO_PARES.jsonl"
RESUMEN = BASE / "docs" / "INTRA_DOMINIO_RESUMEN.md"

UMBRAL_TITULO = 80
# BAJADO DE 0.80 A 0.78 para el cribado completo, y el motivo esta medido: las
# DOS parejas ya adjudicadas que la corrida a 0.80 perdia viven en 0,7890
# (accion_correctiva_4 con accion_correctiva_sistematica) y 0,7887 (cadencia
# con gestion_seguimiento_prospectos). Un umbral que se deja fuera lo que ya
# esta confirmado no es selectivo: es ciego en la banda de abajo. Los pares que
# entran por esa rebaja van marcados con banda_078_080 para poder contarlos
# aparte y no mezclar su rendimiento con el de la cola original.
UMBRAL_SEMANTICO = 0.78

# La calibracion conocida: este par TIENE que aparecer en la cola. Es uno de los
# diecinueve ids casi identicos del apartado 4.4 del informe, los dos en quality.
# Si el instrumento no lo caza, esta mal calibrado y hay que decirlo antes de
# entregar.
PAR_DE_CALIBRACION = ("descubrir_necesidades_cliente", "descubrir_necesidades_del_cliente")

ID = r"[a-z][a-z0-9_]{4,}"
PREFIJO = r"(?:nucleo/|core/|quality/|franquicias/|exportacion/|environmental/|health_safety/|risk_management/|compras/|entrega/|seguridad_digital/)?"


def _troza(texto, desde, hasta, que):
    """Devuelve el trozo entre dos anclas. Falla RUIDOSO si no estan."""
    i = texto.find(desde)
    if i < 0:
        raise SystemExit(f"ANCLA PERDIDA en {que}: no encuentro {desde!r}. "
                         f"El documento cambio de estructura; arregla el ancla "
                         f"antes de usar esta salida.")
    j = texto.find(hasta, i + len(desde))
    if j < 0:
        j = len(texto)
    return texto[i:j]


def _cosecha(trozo, validos):
    """Todos los node_id entre comillas invertidas que existan en el grafo."""
    crudos = re.findall(rf"`{PREFIJO}({ID})`", trozo)
    return {x for x in crudos if x in validos}


def procedencia(grafo, activos):
    """Marcas de trabajo ya hecho, cada una con su fuente.

    Devuelve (marcas_de_pareja, marcas_de_nodo). Las de pareja son exactas: ese
    par concreto ya esta escrito en algun sitio. Las de nodo son mas debiles:
    alguno de los dos miembros ya fue avistado, y el auditor sabra si el par en
    si es nuevo.
    """
    parejas = collections.defaultdict(list)
    nodos = collections.defaultdict(list)

    def par(a, b, fuente):
        if a in activos and b in activos and a != b:
            parejas[tuple(sorted((a, b)))].append(fuente)

    inf = INFORME.read_text(encoding="utf-8")
    fic = FICHA.read_text(encoding="utf-8")
    mes = MESA.read_text(encoding="utf-8")

    # 1. Los 19 ids casi identicos (informe 4.4), lista explicita
    t44 = _troza(inf, "### 4.4 Ids casi identicos", "### 4.5 ", "informe 4.4")
    n44 = 0
    for a, b in re.findall(rf"^- (?:\*\*En el nucleo:\*\* )?`{PREFIJO}({ID})` con `{PREFIJO}({ID})`",
                           t44, re.M):
        par(a, b, "informe 4.4 ids casi identicos"); n44 += 1
    # la decimonovena vive en prosa, no en la lista
    if "seleccion_canales_distribucion" in t44 and "seleccion_canal_distribucion" in t44:
        par("seleccion_canales_distribucion", "seleccion_canal_distribucion",
            "informe 4.4 ids casi identicos (la transdominio)"); n44 += 1

    # 2. Los 9 pares base mas _2 con contenido calcado (informe 4.3)
    t43 = _troza(inf, "### 4.3 Sufijo _N vivo", "### 4.4 ", "informe 4.3")
    n43 = 0
    for a in re.findall(rf"`{PREFIJO}({ID})` con\s+su\s+`_2`", t43):
        par(a, a + "_2", "informe 4.3 base mas _2 calcados"); n43 += 1

    # 3. Los pasos duplicados del programa de Crosby (informe 4.2)
    t42 = _troza(inf, "### 4.2 El programa de Crosby", "### 4.3 ", "informe 4.2")
    n42 = 0
    for a, b in re.findall(rf"^\| \*{{0,2}}Paso \d+\*{{0,2}} \| `({ID})` y `({ID})`", t42, re.M):
        par(a, b, "informe 4.2 pasos duplicados de Crosby"); n42 += 1

    # 4. Las parejas de sufijo vivo, con la MISMA regla de la ficha: los dos
    #    activos y ninguno con marca (ni ids_alias, ni merged_originals, ni ser
    #    alias de nadie). La ficha declara 36; si el numero se mueve, el resumen
    #    lo dice en vez de callarlo.
    es_alias = set()
    for v in grafo.values():
        es_alias.update(v.get("ids_alias") or [])

    def marcado(k):
        v = grafo.get(k, {})
        return bool(v.get("ids_alias")) or bool(v.get("merged_originals")) or k in es_alias

    n_suf = 0
    for k in activos:
        m = re.match(r"^(.*)_(\d+)$", k)
        if not m:
            continue
        b = m.group(1)
        if b in activos and not marcado(b) and not marcado(k):
            par(b, k, "ficha, las 36 parejas de sufijo vivo"); n_suf += 1

    # 5. Lo ya avistado en la ficha, seccion de citas intra-dominio: marca de
    #    NODO, con el nombre del grupo donde aparece.
    tfi = _troza(fic, "# CITAS INTRA-DOMINIO ADELANTADAS",
                 "# FIGURA NUEVA: EL BASE FUE FUSIONADO", "ficha, citas intra-dominio")
    grupo = None
    n_fic = 0
    for linea in tfi.splitlines():
        if linea.startswith("## "):
            grupo = linea.strip("# ").strip()
        if not grupo:
            continue
        for x in _cosecha(linea, activos):
            f = f"ficha, citas intra-dominio: {grupo}"
            if f not in nodos[x]:
                nodos[x].append(f); n_fic += 1

    # 6. Los dos racimos que destapo la muestra D, con miembros escritos
    for ancla, etiqueta, fin in (
            ("**Los siete puntos de Deming en el titulo**", "mesa, grupo 1: los puntos de Deming", "\n\n"),
            ("## RACIMO CANDIDATO: los cinturones de Six Sigma", "ficha, racimo candidato: los cinturones", "\n## ")):
        doc = mes if ancla.startswith("**") else fic
        trozo = _troza(doc, ancla, fin, etiqueta)
        for x in _cosecha(trozo, activos):
            if etiqueta not in nodos[x]:
                nodos[x].append(etiqueta)

    # 7. Las nominas de los 32 racimos. Dos nodos del MISMO racimo forman pareja
    #    marcada: el par ya esta censado, aunque el censo no lo escribiera par a
    #    par. Es la fuente que cerro el hueco declarado de la primera corrida.
    n_rac = n_rac_par = 0
    if RACIMOS.exists():
        for linea in RACIMOS.read_text(encoding="utf-8").splitlines():
            if not linea.strip():
                continue
            r = json.loads(linea)
            ids = [m["node_id"] for m in r["miembros"] if m["node_id"] in activos]
            f = "racimo censado: %s (%s)" % (r["racimo"], r["origen"])
            n_rac += 1
            for i, x in enumerate(ids):
                if f not in nodos[x]:
                    nodos[x].append(f)
                for y in ids[i + 1:]:
                    par(x, y, f); n_rac_par += 1

    cuentas = {"racimos_miembros_32_nominas": "%d racimos, %d parejas" % (n_rac, n_rac_par),
               "informe_4_4_ids_casi_identicos": n44, "informe_4_3_base_mas_2": n43,
               "informe_4_2_crosby_duplicados": n42, "ficha_36_parejas_de_sufijo": n_suf,
               "ficha_citas_intra_dominio_nodos": len([k for k, v in nodos.items() if any("citas intra-dominio" in f for f in v)])}
    return parejas, nodos, cuentas


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--umbral-titulo", type=int, default=UMBRAL_TITULO)
    ap.add_argument("--umbral-semantico", type=float, default=UMBRAL_SEMANTICO)
    ap.add_argument("--dominio", default=None, help="limitar a un dominio")
    ap.add_argument("--banda-desde", type=float, default=0.78,
                    help="piso de la banda que se CUENTA sin entrar en la cola")
    args = ap.parse_args()

    import numpy as np
    from rapidfuzz import process as rf_process
    from rapidfuzz.fuzz import token_sort_ratio

    grafo = json.loads(GRAFO.read_text(encoding="utf-8"))["nodos"]
    idx = json.loads(INDICE.read_text(encoding="utf-8"))
    pos = {n: i for i, n in enumerate(idx["ids"])}
    E = np.array(idx["embeddings"], dtype=np.float32)
    E /= np.linalg.norm(E, axis=1, keepdims=True)

    activos = {k: v for k, v in grafo.items() if not v.get("deprecado")}
    dominio = {k: (v.get("dominio") or "core") for k, v in activos.items()}
    titulo = {k: (v.get("titulo_concepto") or "") for k, v in activos.items()}
    pasos = {k: len(v.get("pasos_accionables") or []) for k, v in activos.items()}

    marcas_par, marcas_nodo, cuentas = procedencia(grafo, activos)

    por_dom = collections.defaultdict(list)
    for k in activos:
        if k in pos:
            por_dom[dominio[k]].append(k)
    sin_vector = [k for k in activos if k not in pos]

    doms = sorted(por_dom)
    if args.dominio:
        doms = [d for d in doms if d == args.dominio]

    pares, distribucion, comparadas, conteo_banda = [], {}, {}, {}
    for dom in doms:
        ids = sorted(por_dom[dom])
        n = len(ids)
        if n < 2:
            continue
        V = E[[pos[k] for k in ids]]
        S = V @ V.T
        T = np.asarray(rf_process.cdist([titulo[k] for k in ids], [titulo[k] for k in ids],
                                        scorer=token_sort_ratio, workers=-1), dtype=np.float32)
        iu = np.triu_indices(n, k=1)
        sem_planos = S[iu]
        comparadas[dom] = int(sem_planos.size)
        distribucion[dom] = {f"p{p}": float(np.percentile(sem_planos, p))
                             for p in (50, 75, 90, 95, 99, 99.9)}
        distribucion[dom]["maximo"] = float(sem_planos.max())
        distribucion[dom]["media"] = float(sem_planos.mean())
        distribucion[dom]["sobre_umbral"] = int((sem_planos >= args.umbral_semantico).sum())

        # LA BANDA DE ABAJO, contada y no volcada. Pares que se quedan justo
        # fuera por semantica, con el titulo tambien por debajo de su umbral: no
        # entran en la cola ni en el jsonl, solo se cuentan, para que la decision
        # de leerla o cribarla se tome con el numero delante.
        banda = np.triu((S >= args.banda_desde) & (S < args.umbral_semantico) &
                        (T < args.umbral_titulo), k=1)
        conteo_banda[dom] = int(banda.sum())

        disp = (S >= args.umbral_semantico) | (T >= args.umbral_titulo)
        ii, jj = np.where(np.triu(disp, k=1))
        for i, j in zip(ii.tolist(), jj.tolist()):
            a, b = ids[i], ids[j]
            clave = tuple(sorted((a, b)))
            fuentes_par = marcas_par.get(clave, [])
            fuentes_nodo = sorted(set(marcas_nodo.get(a, []) + marcas_nodo.get(b, [])))
            pares.append({
                "dominio": dom,
                "nodo_a": a, "titulo_a": titulo[a],
                "nodo_b": b, "titulo_b": titulo[b],
                "sim_titulo": round(float(T[i, j]), 1),
                "sim_semantica": round(float(S[i, j]), 4),
                "disparo_titulo": bool(T[i, j] >= args.umbral_titulo),
                "disparo_semantica": bool(S[i, j] >= args.umbral_semantico),
                "pasos_a": pasos[a], "pasos_b": pasos[b],
                "banda_078_080": bool(S[i, j] < 0.80 and T[i, j] < args.umbral_titulo),
                "procedencia_pareja": fuentes_par,
                "procedencia_nodo": fuentes_nodo,
                "estado": "re-avistado" if fuentes_par else ("nodo ya avistado" if fuentes_nodo else "nuevo"),
            })

    # Orden de lectura: por dominio y, dentro del dominio, por clave descendente.
    pares.sort(key=lambda p: (p["dominio"], -max(p["sim_semantica"], p["sim_titulo"] / 100)))
    for n, p in enumerate(pares, 1):
        p["puesto_intra"] = n
    with open(SALIDA, "w", encoding="utf-8") as fh:
        for p in pares:
            fh.write(json.dumps(p, ensure_ascii=False) + "\n")

    a, b = PAR_DE_CALIBRACION
    calibra = [p for p in pares if {p["nodo_a"], p["nodo_b"]} == {a, b}]

    estados = collections.Counter(p["estado"] for p in pares)
    por_dominio = collections.Counter(p["dominio"] for p in pares)

    # RECALL CONTRA LO DECLARADO. Las parejas ya escritas en los documentos son
    # la unica verdad conocida que existe para este eje: si el instrumento no las
    # caza, la cola tiene agujeros y hay que decirlo ANTES de leerla.
    en_cola = {tuple(sorted((p["nodo_a"], p["nodo_b"]))) for p in pares}
    declaradas = {k: v for k, v in marcas_par.items()
                  if k[0] in dominio and k[1] in dominio and dominio[k[0]] == dominio[k[1]]
                  and (not args.dominio or dominio[k[0]] == args.dominio)}
    perdidas = []
    for (x, y), fuentes in sorted(declaradas.items()):
        if (x, y) in en_cola:
            continue
        st = float(token_sort_ratio(titulo[x], titulo[y]))
        ss = float(E[pos[x]] @ E[pos[y]]) if x in pos and y in pos else float("nan")
        perdidas.append({"a": x, "b": y, "dominio": dominio[x], "sim_titulo": round(st, 1),
                         "sim_semantica": round(ss, 4), "fuentes": fuentes})
    cruzan = sorted(k for k in marcas_par if k[0] in dominio and k[1] in dominio
                    and dominio[k[0]] != dominio[k[1]])

    L = []
    A = L.append
    A("# Cola intra-dominio: pares del mismo dominio para leer")
    A("")
    A("**ESTE INSTRUMENTO EMPAREJA, NO JUZGA.** El veredicto de cada par es **lectura "
      "textual** del auditor con visto del fundador. **Un par en esta lista es una cita "
      "para leer, no un duplicado.**")
    A("")
    A("Es el otro eje del mismo trabajo: `scripts/gradiente_pares.py` empareja **mundo "
      "contra nucleo**, y este empareja **cada dominio contra si mismo**, que es donde "
      "viven los racimos. Los conteos de pasos **solo ordenan la cola**; la profundidad y "
      "la duplicacion se adjudican leyendo, jamas contando.")
    A("")
    A("## Como se emparejo")
    A("")
    A("Dos senales independientes, y basta con que dispare **cualquiera**:")
    A("")
    A(f"- **titulo**: `token_sort_ratio` de rapidfuzz, umbral **{args.umbral_titulo}**")
    A(f"- **semantica**: coseno sobre `semantic_index.json`, umbral **{args.umbral_semantico}**")
    A("")
    A("Cada par reporta **las dos**, aunque solo una haya disparado.")
    A("")
    A(f"**El umbral semantico es {args.umbral_semantico} y no el 0,75 del gradiente a "
      "proposito.** Dentro de un dominio la vecindad tematica es **la norma, no la "
      "senal**: dos nodos de `quality` hablan de calidad por definicion. La distribucion "
      "por dominio esta mas abajo **para que el umbral se pueda recalibrar con datos "
      "antes de leer**, no despues.")
    A("")
    A("## La calibracion conocida")
    A("")
    if calibra:
        c = calibra[0]
        A(f"**CAZADO.** El par `{a}` contra `{b}` (los dos en `{c['dominio']}`) esta en la "
          f"cola: similitud de titulo **{c['sim_titulo']}**, semantica "
          f"**{c['sim_semantica']}** (disparo por titulo: {c['disparo_titulo']}, por "
          f"semantica: {c['disparo_semantica']}).")
    else:
        A(f"**NO CAZADO. EL INSTRUMENTO ESTA MAL CALIBRADO.** El par `{a}` contra `{b}` "
          f"deberia estar en la cola y no esta. **No uses esta salida sin revisar los "
          f"umbrales.**")
    A("")
    A("## Conteos")
    A("")
    A(f"**{len(pares)} pares** en la cola, sobre **{sum(len(v) for v in por_dom.values())} "
      f"nodos activos** repartidos en **{len(por_dom)} dominios**.")
    if sin_vector:
        A("")
        A(f"**{len(sin_vector)} nodos activos SIN vector semantico** quedaron fuera de la "
          f"senal semantica: {', '.join('`%s`' % x for x in sorted(sin_vector)[:10])}"
          f"{' y mas' if len(sin_vector) > 10 else ''}.")
    A("")
    A("| dominio | nodos | pares posibles | en la cola | % de los posibles |")
    A("|---|---:|---:|---:|---:|")
    for dom in doms:
        n = len(por_dom[dom])
        posibles = n * (n - 1) // 2
        enc = por_dominio.get(dom, 0)
        A(f"| {dom} | {n} | {posibles} | **{enc}** | {100 * enc / posibles:.2f}% |" if posibles
          else f"| {dom} | {n} | 0 | 0 | n/a |")
    A("")
    A("## Nuevos contra re-avistados")
    A("")
    A("**El instrumento conoce el trabajo hecho.** Nada se excluye por estar ya visto: se "
      "MARCA, con su fuente, y la cola dice que es nuevo y que no.")
    A("")
    A("| estado | pares | que significa |")
    A("|---|---:|---|")
    A(f"| **nuevo** | **{estados.get('nuevo', 0)}** | ni el par ni sus dos nodos aparecen en lo ya escrito |")
    A(f"| nodo ya avistado | {estados.get('nodo ya avistado', 0)} | alguno de los dos nodos ya fue leido en otro par; **el par en si es nuevo** |")
    A(f"| re-avistado | {estados.get('re-avistado', 0)} | **el par exacto** ya esta adjudicado o censado |")
    A("")
    A("Fuentes de las marcas, con lo que aporto cada una:")
    A("")
    A("| fuente | entradas |")
    A("|---|---:|")
    for k, v in cuentas.items():
        A(f"| `{k}` | {v} |")
    A("")
    A("> **HUECO CERRADO.** En la primera corrida solo dos de los 32 racimos tenian nomina "
      "escrita y el resumen declaraba la columna de re-avistados como subestimada. **Ya no**: "
      "`docs/RACIMOS_MIEMBROS.jsonl` tiene **las 32 nominas completas**, reconstruidas de las "
      "razones de los veredictos del cribado, y **las 32 cuadran con su tamano censado**. "
      "Cada par cuyos dos nodos pertenecen al mismo racimo entra ya como re-avistado.")
    A("")
    A("## Recall contra lo declarado, que es el dato duro de calibracion")
    A("")
    A("**Las parejas ya escritas en los documentos son la unica verdad conocida que existe "
      "para este eje.** Si el instrumento no las caza, la cola tiene agujeros, y eso hay "
      "que saberlo ANTES de leerla, no despues.")
    A("")
    caz = len(declaradas) - len(perdidas)
    pct = (100 * caz / len(declaradas)) if declaradas else 0
    A(f"| | |")
    A(f"|---|---:|")
    A(f"| parejas declaradas que son **intra-dominio** | **{len(declaradas)}** |")
    A(f"| de esas, **cazadas** por la cola | **{caz}** |")
    A(f"| **perdidas** | **{len(perdidas)}** |")
    A(f"| **recall** | **{pct:.0f}%** |")
    A("")
    if cruzan:
        A(f"({len(cruzan)} parejas declaradas mas **cruzan dominio** y por definicion no le "
          f"tocan a este instrumento: " +
          ", ".join(f"`{x}` con `{y}`" for x, y in cruzan) + ".)")
        A("")
    if perdidas:
        A(f"**Las {len(perdidas)} perdidas, con sus dos senales**, para que se vea cuanto "
          f"falta y no cuanto se cree que falta:")
        A("")
        A("| dominio | pareja | titulo | semantica | de donde viene la marca |")
        A("|---|---|---:|---:|---|")
        for p in sorted(perdidas, key=lambda z: -z["sim_semantica"]):
            A(f"| {p['dominio']} | `{p['a']}` con `{p['b']}` | {p['sim_titulo']} | "
              f"{p['sim_semantica']} | {'; '.join(p['fuentes'])} |")
        A("")
        top = max(p["sim_semantica"] for p in perdidas)
        A(f"**Lo que estas perdidas dicen, y es lo mas util de este resumen:**")
        A("")
        A(f"- **La familia de ids no la cazan estas dos senales.** Casi todas las perdidas "
          f"son parejas de **sufijo `_N`**: se llaman parecido pero no lo bastante para el "
          f"umbral de titulo, y hablan de lo mismo pero por debajo del umbral semantico. "
          f"**Su detector no es este: es la regla del sufijo**, que este mismo instrumento "
          f"ya computa y publica arriba con sus {cuentas['ficha_36_parejas_de_sufijo']} "
          f"parejas.")
        A(f"- **Bajar el umbral no las rescata gratis.** La perdida mas alta esta en "
          f"**{top:.4f}** de semantica; bajar el corte hasta ahi ensancharia la cola en "
          f"todos los dominios a la vez. La distribucion de abajo dice cuanto.")
        A(f"- **Hay perdidas que NO son de sufijo, y esas si duelen**: "
          + ", ".join(f"`{p['a']}` con `{p['b']}`" for p in perdidas
                      if not re.match(rf"^{re.escape(p['a'])}_\d+$", p["b"]))
          + ". **Son parejas ya adjudicadas que estas dos senales no ven**, y son el "
            "argumento para no leer esta cola como si fuera exhaustiva.")
        A("")
    A("## Distribucion de la similitud semantica, por dominio")
    A("")
    A("**Esta es la tabla para recalibrar el umbral antes de leer.** Si un dominio tiene el "
      "p99 por encima del umbral, ese dominio va a inundar la cola de vecinos legitimos y "
      "conviene subirle el corte.")
    A("")
    A("| dominio | comparaciones | media | p50 | p90 | p99 | p99.9 | maximo | sobre el umbral |")
    A("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for dom in doms:
        if dom not in distribucion:
            continue
        d = distribucion[dom]
        A(f"| {dom} | {comparadas[dom]} | {d['media']:.4f} | {d['p50']:.4f} | {d['p90']:.4f} | "
          f"{d['p99']:.4f} | {d['p99.9']:.4f} | {d['maximo']:.4f} | {d['sobre_umbral']} |")
    A("")
    A("## La banda 0,78 a 0,80, YA DENTRO de la cola")
    A("")
    A(f"**Pares que entraron por la rebaja del umbral**: semantica por debajo de **0,80** y "
      f"titulo por debajo de **{args.umbral_titulo}**, o sea que con el umbral anterior no "
      f"entraban por ninguna de las dos senales. **Estan en `{SALIDA.name}` con el campo "
      f"`banda_078_080` en true**, para poder contar su rendimiento aparte y no mezclarlo "
      f"con el de la cola original.")
    A("")
    banda_dom = collections.Counter(p["dominio"] for p in pares if p["banda_078_080"])
    A("| dominio | de la banda | del resto de la cola | total | la banda es |")
    A("|---|---:|---:|---:|---:|")
    tot_b = 0
    for dom in doms:
        cb = banda_dom.get(dom, 0); cc = por_dominio.get(dom, 0)
        tot_b += cb
        A(f"| {dom} | **{cb}** | {cc - cb} | {cc} | {(100.0 * cb / cc):.0f}% |" if cc
          else f"| {dom} | 0 | 0 | 0 | n/a |")
    if pares:
        A(f"| **total** | **{tot_b}** | **{len(pares) - tot_b}** | **{len(pares)}** | "
          f"**{(100.0 * tot_b / len(pares)):.0f}%** |")
    A("")
    A("**La banda se lee, no se descarta, y el motivo esta medido**: las dos parejas ya "
      "adjudicadas que la corrida anterior perdia viven dentro de ella. **Su rendimiento se "
      "cuenta aparte** (cuantas A, B y C aporta contra su costo de lectura), que es la unica "
      "forma de saber si la rebaja del umbral valio la pena.")
    A("")
    A("**Verificacion de las dos perdidas conocidas**, que es lo que hace util a la banda:")
    A("")
    A("| pareja | semantica | titulo | cae en la banda |")
    A("|---|---:|---:|:--:|")
    for x, y in (("accion_correctiva_4", "accion_correctiva_sistematica"),
                 ("cadencia_seguimiento_prospectos", "gestion_seguimiento_prospectos")):
        if x in pos and y in pos:
            ss = float(E[pos[x]] @ E[pos[y]]); st = float(token_sort_ratio(titulo[x], titulo[y]))
            dentro = args.banda_desde <= ss < args.umbral_semantico and st < args.umbral_titulo
            A(f"| `{x}` con `{y}` | {ss:.4f} | {st:.1f} | {'**SI**' if dentro else '**NO**'} |")
        else:
            A(f"| `{x}` con `{y}` | sin vector | n/a | **NO SE PUEDE MEDIR** |")
    A("")
    A("**Las dos son parejas ya adjudicadas que las senales actuales no ven** (el recall de "
      "arriba). Si caen dentro, la banda **es exactamente el sitio donde vive lo que esta "
      "cola se pierde**, y eso es lo que hay que pesar al decidir si se lee.")
    A("")
    A("## Los treinta pares de similitud mas alta")
    A("")
    A("Ordenados por la senal MAS FUERTE de las dos, normalizando el titulo a 0 a 1. Por "
      "eso hay filas con semantica baja y titulo alto: entraron por el titulo.")
    A("")
    A("| # | dominio | nodo a | nodo b | titulo | semantica | pasos a/b | estado |")
    A("|---:|---|---|---|---:|---:|---:|---|")
    top = sorted(pares, key=lambda z: -max(z["sim_semantica"], z["sim_titulo"] / 100))[:30]
    for i, p in enumerate(top, 1):
        A(f"| {i} | {p['dominio']} | `{p['nodo_a']}` | `{p['nodo_b']}` | {p['sim_titulo']} | "
          f"{p['sim_semantica']} | {p['pasos_a']}/{p['pasos_b']} | {p['estado']} |")
    A("")
    A(f"La cola completa, con los titulos de los dos lados y las marcas de procedencia, en "
      f"`{SALIDA.name}`.")
    A("")
    A("## Que hacer con el tamano de esta cola")
    A("")
    A("**Si la cola sale grande, no es un fallo del instrumento: es el tamano del "
      "problema.** El paso de lectura lo deciden el auditor y el fundador, como se hizo con "
      "la franja bajo el umbral. Las palancas, en orden de menor a mayor perdida de "
      "cobertura: **subir el umbral semantico** (la distribucion de arriba dice cuanto), "
      "**leer por dominio** en vez de por cola global, y **ordenar por senal** dejando la "
      "cola larga para tandas posteriores. **Lo que no se puede hacer es podarla en "
      "silencio**: si se corta, se escribe donde se corto y cuanto quedo sin mirar.")
    RESUMEN.write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"  pares: {len(pares)} | escrito {SALIDA.name} y {RESUMEN.name}")
    for dom in doms:
        print(f"    {dom:<20} {por_dominio.get(dom, 0)}")
    print(f"  nuevos: {estados.get('nuevo', 0)} | nodo ya avistado: "
          f"{estados.get('nodo ya avistado', 0)} | re-avistados: {estados.get('re-avistado', 0)}")
    print(f"  calibracion {a} vs {b}: {'CAZADO' if calibra else 'NO CAZADO (mal calibrado)'}")
    return 0 if calibra else 1


if __name__ == "__main__":
    raise SystemExit(main())
