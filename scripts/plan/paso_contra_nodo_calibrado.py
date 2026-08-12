#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""paso_contra_nodo_calibrado.py . el barrido paso contra nodo CON LA SENAL DEL VERBO.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo. Escribe solo en docs/plan/.

QUE ANADE ESTA CORRIDA, y por que.
El modo de fallo del instrumento viejo esta medido: en CUATRO de los cinco falsos
positivos de la muestra pineada de 24, EL PASO Y EL HIJO COMPARTEN EL SUSTANTIVO Y
CAMBIAN EL VERBO. Leer contra disenar, monitorear contra lograr, listar contra
definir, comprar contra certificar. El instrumento medía vocabulario y no accion.

LA CALIBRACION, declarada, y NO toca los umbrales viejos:
  - se extrae la FAMILIA DE ACCION del paso (su primer verbo) y la del hijo (el
    nucleo de su titulo, resolviendo la nominalizacion: seleccion -> seleccionar).
  - SI LAS DOS FAMILIAS SE CONOCEN Y SON DISTINTAS, EL CANDIDATO SE DESCARTA.
    Mismo sustantivo y accion distinta NO ES CANDIDATO.
  - si alguna de las dos no se reconoce, el candidato SE MANTIENE: la senal solo
    resta, nunca suma, y en la duda no descarta.

UMBRALES, los mismos del instrumento original y por el mismo motivo:
  --umbral-titulo 72 | --umbral-contencion 0.45 | --min-tokens 4
No se tocan a proposito: si se movieran a la vez que se anade la senal, no habria
forma de saber cual de los dos cambios produjo la diferencia.
"""
import argparse, collections, json, re, unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"
SALIDA = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO.jsonl"

# EL BASE SE IMPORTA DEL INSTRUMENTO ORIGINAL, no se reimplementa.
# Motivo: si la normalizacion se reescribe, la corrida nueva no es comparable con la
# vieja, y entonces la calibracion no se puede medir. Se cambia UNA cosa: el verbo.
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("pcn", RAIZ / "scripts" / "paso_contra_nodo.py")
_pcn = _ilu.module_from_spec(_spec); _spec.loader.exec_module(_pcn)
VACIAS = _pcn.VACIAS

# EL DEFECTO QUE ENCONTRO LA PRIMERA MUESTRA, y su correccion declarada.
# La lista de vacias del instrumento original CONTIENE VEINTE FORMAS VERBALES
# (crea, crear, define, definir, determina, determinar, establece, establecer,
# evalua, evaluar, hacer, haz, identifica, identificar, realiza, realizar,
# revisa, revisar, usa, usar). Estan ahi con razon PARA LO SUYO: el original
# mide SOLAPE DE VOCABULARIO y esos verbos son ruido en casi todo paso.
# Pero para LA SENAL DEL VERBO son justamente la senal, y filtrarlos la deja
# ciega en los casos mas frecuentes. Medido en la muestra pineada de 24 del
# 11 ago 2026: en 21 de 24 filas al menos una de las dos familias salio None.
# CORRECCION: contenido() sigue usando VACIAS SIN TOCAR, para que la bolsa
# bruta siga siendo la misma y las dos corridas sean comparables. Solo
# familia() usa una lista PURAMENTE GRAMATICAL, que es VACIAS menos los verbos.
VERBOS_EN_VACIAS = {"crea", "crear", "define", "definir", "determina", "determinar",
                    "establece", "establecer", "evalua", "evaluar", "hacer", "haz",
                    "identifica", "identificar", "realiza", "realizar", "revisa",
                    "revisar", "usa", "usar"}
VACIAS_GRAM = set(VACIAS) - VERBOS_EN_VACIAS

# LAS FAMILIAS DE ACCION. Declaradas aqui para que se puedan discutir de una.
FAMILIAS = {
    "OBSERVAR": """leer revisar mirar analizar evaluar medir monitorear identificar detectar
        investigar comparar verificar comprobar diagnosticar listar enumerar observar auditar
        examinar estudiar consultar rastrear analisis evaluacion medicion monitoreo revision
        identificacion investigacion comparacion verificacion diagnostico lectura auditoria""",
    "CONSTRUIR": """disenar crear desarrollar construir armar elaborar redactar formular montar
        preparar generar produccion diseno creacion desarrollo construccion elaboracion
        redaccion preparacion generacion mapear mapa modelar modelo""",
    "DEFINIR": """definir establecer fijar delimitar especificar determinar precisar definicion
        establecimiento determinacion especificacion criterio criterios""",
    "DECIDIR": """decidir elegir seleccionar priorizar escoger optar decision eleccion seleccion
        priorizacion""",
    "EJECUTAR": """ejecutar aplicar implementar realizar hacer lanzar correr usar utilizar operar
        ejecucion aplicacion implementacion realizacion lanzamiento uso utilizacion operacion""",
    "CONSEGUIR": """obtener conseguir comprar contratar adquirir negociar pedir solicitar reclutar
        obtencion compra contratacion adquisicion negociacion solicitud reclutamiento""",
    "COMUNICAR": """comunicar presentar explicar informar avisar documentar reportar compartir
        publicar comunicacion presentacion explicacion informe documentacion reporte""",
    "LOGRAR": """lograr alcanzar cumplir certificar garantizar asegurar mantener sostener logro
        cumplimiento certificacion garantia mantenimiento""",
    "GESTIONAR": """gestionar administrar coordinar dirigir controlar supervisar gestion
        administracion coordinacion direccion control supervision""",
}
# EL SEGUNDO DEFECTO QUE ENCONTRO LA MUESTRA: la tabla guarda INFINITIVOS y el
# corpus escribe en imperativo de tu ("documenta", "define", "revisa"). El
# reductor de sufijos va al reves (quita y busca la raiz) y la raiz nunca esta.
# CORRECCION: por cada infinitivo se registra tambien su forma de tu, con la
# regla mecanica ar->a, er/ir->e. Nada se anade a mano.
DE_PALABRA = {}
for fam, palabras in FAMILIAS.items():
    for p in palabras.split():
        DE_PALABRA[p] = fam
        if p.endswith("ar"):
            DE_PALABRA.setdefault(p[:-2] + "a", fam)
        elif p.endswith(("er", "ir")):
            DE_PALABRA.setdefault(p[:-2] + "e", fam)


norm = _pcn.norm
contenido = _pcn.contenido


def familia(texto, primeras=4):
    """La familia de accion de un texto: la primera palabra reconocida entre las
    primeras `primeras` de contenido. None si no se reconoce ninguna."""
    for w in [x for x in norm(texto).split() if x not in VACIAS_GRAM][:primeras]:
        if w in DE_PALABRA:
            return DE_PALABRA[w]
        for suf in ("ar", "er", "ir", "a", "e"):
            if w.endswith(suf) and w[: -len(suf)] in DE_PALABRA:
                return DE_PALABRA[w[: -len(suf)]]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--umbral-titulo", type=float, default=72.0)
    ap.add_argument("--umbral-contencion", type=float, default=0.45)
    ap.add_argument("--min-tokens", type=int, default=4)
    args = ap.parse_args()
    from rapidfuzz.fuzz import token_set_ratio

    G = json.load(open(GRAFO, encoding="utf-8"))["nodos"]
    DEP = {k for k, v in G.items() if v.get("deprecado")}
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def vivo(x):
        if x in G and x not in DEP:
            return x
        y = ALIAS.get(x)
        return y if y in G and y not in DEP else None

    def vecinos(n):
        out = set()
        for campo in ("nodos_siguientes", "nodos_previos"):
            for y in (G[n].get(campo) or []):
                r = vivo(y)
                if r and r != n:
                    out.add(r)
        return out

    vivos = [k for k in G if k not in DEP]
    por_dominio = collections.defaultdict(list)
    for k in vivos:
        por_dominio[G[k].get("dominio") or "?"].append(k)
    ident, indice, titulo_norm, fam_hijo = {}, collections.defaultdict(set), {}, {}
    for k in vivos:
        g = G[k]
        ident[k] = contenido(" ".join([g.get("titulo_concepto") or "",
                                       g.get("resumen_teorico") or "",
                                       g.get("entregable_esperado") or ""]))
        for w in ident[k]:
            indice[w].add(k)
        titulo_norm[k] = norm(g.get("titulo_concepto") or "")
        fam_hijo[k] = familia(g.get("titulo_concepto") or "")

    filas, descartados = [], []
    for dom, nodos in por_dominio.items():
        set_dom = set(nodos)
        for madre in nodos:
            pasos = G[madre].get("pasos_accionables") or []
            vec_m = vecinos(madre)
            for i, paso in enumerate(pasos, 1):
                toks = contenido(paso)
                if len(toks) < args.min_tokens:
                    continue
                paso_norm = norm(paso)
                fp = familia(paso)
                golpes = collections.Counter()
                for w in toks:
                    for k in indice.get(w, ()):
                        golpes[k] += 1
                minimo = args.umbral_contencion * len(toks)
                for hijo, n_comunes in golpes.items():
                    if hijo == madre or hijo not in set_dom or n_comunes < minimo:
                        continue
                    t = token_set_ratio(paso_norm, titulo_norm[hijo])
                    if t < args.umbral_titulo:
                        continue
                    fh = fam_hijo[hijo]
                    fila = {"dominio": dom, "madre": madre, "paso": i, "texto_paso": paso,
                            "hijo": hijo, "titulo_hijo": G[hijo].get("titulo_concepto"),
                            "titulo_ratio": round(t, 1), "contencion": round(n_comunes / len(toks), 3),
                            "familia_paso": fp, "familia_hijo": fh,
                            "arista": hijo in vec_m or madre in vecinos(hijo)}
                    # LA SENAL DEL VERBO: solo resta, y en la duda no descarta.
                    if fp and fh and fp != fh:
                        fila["descartado_por"] = "verbo: %s contra %s" % (fp, fh)
                        descartados.append(fila)
                    else:
                        filas.append(fila)

    filas.sort(key=lambda f: -(f["titulo_ratio"] / 100 * f["contencion"]))
    with open(SALIDA, "w", encoding="utf-8", newline="\n") as f:
        for fila in filas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

    tot = len(filas) + len(descartados)
    sin_a = [f for f in filas if not f["arista"]]
    sin_a_desc = [f for f in descartados if not f["arista"]]
    print("UMBRALES: titulo %.0f | contencion %.2f | min tokens %d  (LOS MISMOS del original)"
          % (args.umbral_titulo, args.umbral_contencion, args.min_tokens))
    print()
    print("CANDIDATOS BRUTOS (antes de la senal del verbo): %d" % tot)
    print("DESCARTADOS POR LA SENAL DEL VERBO:              %d  (%.1f%%)" % (len(descartados), 100.0 * len(descartados) / max(tot, 1)))
    print("BOLSA REDUCIDA:                                  %d" % len(filas))
    print()
    print("SIN ARISTA, brutos:  %d" % (len(sin_a) + len(sin_a_desc)))
    print("SIN ARISTA, descartados por el verbo: %d" % len(sin_a_desc))
    print("SIN ARISTA, BOLSA REDUCIDA: %d" % len(sin_a))
    print()
    print("REPARTO POR DOMINIO de la bolsa reducida sin arista")
    c = collections.Counter(f["dominio"] for f in sin_a)
    cb = collections.Counter(f["dominio"] for f in sin_a + sin_a_desc)
    print("| dominio | brutos | reducidos | descartados |")
    print("|---|---:|---:|---:|")
    for d in sorted(cb, key=lambda x: -cb[x]):
        print("| %s | %d | %d | %d |" % (d, cb[d], c.get(d, 0), cb[d] - c.get(d, 0)))
    print()
    print("LOS PARES DE FAMILIAS QUE MAS DESCARTAN")
    for k, n in collections.Counter(f["descartado_por"] for f in descartados).most_common(8):
        print("   %-34s %d" % (k, n))


if __name__ == "__main__":
    main()
