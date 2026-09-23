# -*- coding: utf-8 -*-
r"""importar_forja.py . EL PUENTE DE LA FORJA A LA APP (22 sep 2026).

Convierte los nodos de la forja (repo hermano `forja-nodos`, rama
`extraccion-mundo-11`, fichero `dataset/nodos.jsonl`, esquema
`esquema/nodo.schema.json`) al FORMATO DE PACK que consume
`scripts/integrar_packs.py`: una carpeta por dominio con un JSON por nodo en
`<dominio>/nodos/<node_id>.json`, en el esquema de `dataset/nodos` de My-idea
(la lista blanca es `scripts/expansion/validar_esquema.py`).

MODO SECO POR DEFECTO. Sin banderas, el pack se escribe en una carpeta
TEMPORAL fuera del repo (`tempfile.mkdtemp`) y se imprime el informe. Con
`--salida DIR` se escribe donde se diga, y el script SE NIEGA a escribir
dentro de `dataset/` (eso es de `integrar_packs.py --ejecutar`, herramienta de
sesion con credencial). Este script NO toca `dataset/`, NO llama a ninguna
API y NO lee el `.env`.

EL MAPEO, CAMPO POR CAMPO, esta explicado en `docs/PUENTE_FORJA.md`. En corto:

  forja                     -> My-idea
  id                        -> node_id (y nombre del fichero)
  titulo                    -> titulo_concepto
  resumen_teorico           -> resumen_teorico
  pasos_accionables         -> pasos_accionables
  condiciones_activacion    -> condiciones_activacion   (texto -> lista de uno)
  entregable_esperado       -> entregable_esperado
  fuentes[].clave           -> fuente   ("Titulo - Autor", orden conservado, " | ")
  ids_alias                 -> ids_alias
  nodos_previos/siguientes  -> nodos_previos/siguientes
  dominio                   -> dominio  (gestion_equipos, contratacion y
                               carrera_profesional a primer_equipo;
                               proteccion_consumidor fuera, al mundo 10)
  estado 'deprecado'        -> deprecado: true   ('vivo' no escribe nada)
  (no existe)               -> fase_proyecto    (del registro incremental
                               docs/puente_forja/fases_mundo11.jsonl)
  (no existe)               -> etiqueta_arbol   (opcional, la UI cae al titulo)
  denominaciones, escala_minima, atribuciones, marco_pais, vigencia,
  fuentes[].fecha           -> SIN DESTINO en el esquema de My-idea. No se
                               pierden: viajan en
                               `<dominio>/metadata/forja_campos_sin_destino.json`,
                               que integrar_packs.py no lee.

USO:
  python scripts/importar_forja.py                      # seco, carpeta temporal
  python scripts/importar_forja.py --forja RUTA         # otra copia de la forja
  python scripts/importar_forja.py --salida DIR         # el pack en DIR
  python scripts/importar_forja.py --fases OTRO.jsonl   # otro registro de fases
  python scripts/importar_forja.py --incluir-forja      # tambien el dominio 'forja'

Sale 0 si el pack se pudo construir (aunque el informe traiga huecos: el
informe es el producto del modo seco), 2 si la forja no se puede leer.
"""
import argparse
import collections
import io
import json
import os
import re
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATASET = BASE / "dataset"
DATASET_NODOS = DATASET / "nodos"
FORJA_DEFECTO = BASE.parent / "forja-nodos"
SEP_FUENTE = " | "
FASES_VALIDAS = {"ideacion", "validacion", "planificacion", "ejecucion"}
RE_ID = re.compile(r"^[a-z0-9_]+$")

# Los campos de la forja con destino en My-idea, y los que no tienen ninguno.
CON_DESTINO = {"id", "titulo", "resumen_teorico", "pasos_accionables",
               "condiciones_activacion", "entregable_esperado", "fuentes",
               "ids_alias", "nodos_previos", "nodos_siguientes", "dominio",
               "estado"}
SIN_DESTINO = ("denominaciones", "escala_minima", "atribuciones", "marco_pais",
               "vigencia")

# Dominios de la forja que no son contenido del producto: el manual interno de
# la casa. Quedan fuera del pack salvo --incluir-forja, y se informan.
DOMINIOS_FUERA = {"forja"}

# DECISIONES DEL FUNDADOR (23 sep 2026, docs/PUENTE_FORJA.md, DECISIONES):
# EL MUNDO 11 ES UN SOLO DOMINIO, el de la ficha `Primer Equipo` de
# docs/PENDIENTES.md, escrito `primer_equipo`. Los tres dominios de la forja
# que son del mundo 11 se mapean a el. `proteccion_consumidor` (las
# Directrices de la ONU) QUEDA FUERA: su casa es el mundo 10 (Vender), que aun
# no existe en la app. Un dominio de la forja que no este en ninguna de las
# tablas es DOMINIO DESCONOCIDO y el informe lo dice.
DOMINIO_DESTINO = {
    "gestion_equipos": "primer_equipo",
    "contratacion": "primer_equipo",
    "carrera_profesional": "primer_equipo",
}
DOMINIOS_A_OTRO_MUNDO = {"proteccion_consumidor": "mundo 10 (Vender), aun no existe en la app"}

# Las entradas horneadas del pack, versionadas en el repo (no en dataset/).
ENTRADAS = BASE / "docs" / "puente_forja"
FASES_DEFECTO = ENTRADAS / "fases_mundo11.jsonl"


# ---------------------------------------------------------------------------
# Lectura
# ---------------------------------------------------------------------------

def leer_forja(raiz):
    nodos = [json.loads(l) for l in io.open(raiz / "dataset" / "nodos.jsonl",
                                             encoding="utf-8") if l.strip()]
    fuentes = json.load(io.open(raiz / "fuentes" / "FUENTES_CANONICAS.json",
                                encoding="utf-8"))
    return nodos, fuentes


def catalogo_my_idea():
    """{id: 'vivo'|'deprecado'} de dataset/nodos y {alias: dueno}. Solo lee."""
    ids, alias = {}, {}
    for p in sorted(DATASET_NODOS.glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        nid = d.get("node_id") or p.stem
        ids[nid] = "deprecado" if d.get("deprecado") else "vivo"
        for a in d.get("ids_alias") or []:
            alias.setdefault(a, nid)
    return ids, alias


def dominios_de_my_idea():
    sys.path.insert(0, str(BASE / "scripts"))
    try:
        from run_phase1 import DOMINIOS_PERMITIDOS
        return set(DOMINIOS_PERMITIDOS)
    except Exception:  # noqa: BLE001
        return set()


def canonicas_de_my_idea():
    """El conjunto de grafias canonicas contra el que Gate 0 valida `fuente`."""
    sys.path.insert(0, str(BASE / "scripts" / "loop"))
    try:
        from verificar_fuente_canonico import cargar_tabla
        return set(cargar_tabla().values())
    except Exception:  # noqa: BLE001
        return None


# ---------------------------------------------------------------------------
# Conversion (pura)
# ---------------------------------------------------------------------------

def grafia_de(clave, fuentes):
    ficha = fuentes.get(clave) if isinstance(fuentes, dict) else None
    if isinstance(ficha, dict) and ficha.get("titulo_completo"):
        # La forma de la casa en la lista canonica de My-idea es "Titulo - Autor"
        # (docs/plan/OP_S_11_MAPEO_PROPUESTO.md): se escribe igual.
        autor = (ficha.get("autor") or "").strip()
        return "%s - %s" % (ficha["titulo_completo"], autor) if autor else ficha["titulo_completo"]
    return None


def leer_fases(ruta):
    """{node_id: fase}. Acepta el registro incremental .jsonl (una linea por id,
    con `node_id` y `fase_proyecto`) o un .json plano {node_id: fase}."""
    ruta = Path(ruta)
    if not ruta.exists():
        return {}
    if ruta.suffix == ".jsonl":
        out = {}
        for l in io.open(ruta, encoding="utf-8"):
            if l.strip():
                d = json.loads(l)
                out[d["node_id"]] = d["fase_proyecto"]
        return out
    return json.load(io.open(ruta, encoding="utf-8"))


def dominio_de_nodo_mi(nid):
    p = DATASET_NODOS / ("%s.json" % nid)
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8")).get("dominio")


def convertir(n, fuentes, fases):
    """(nodo_my_idea, sidecar, problemas). No toca disco."""
    problemas = []
    grafias = []
    for f in n.get("fuentes") or []:
        g = grafia_de(f.get("clave"), fuentes)
        if g is None:
            problemas.append("fuente sin ficha en FUENTES_CANONICAS: %s" % f.get("clave"))
        else:
            grafias.append(g)
    cond = n.get("condiciones_activacion")
    cond = [cond] if isinstance(cond, str) else list(cond or [])
    out = {
        "node_id": n.get("id"),
        "fase_proyecto": fases.get(n.get("id"), ""),
        "dominio": DOMINIO_DESTINO.get(n.get("dominio"), n.get("dominio")),
        "titulo_concepto": n.get("titulo"),
        "fuente": SEP_FUENTE.join(grafias),
        "resumen_teorico": n.get("resumen_teorico"),
        "pasos_accionables": list(n.get("pasos_accionables") or []),
        "entregable_esperado": n.get("entregable_esperado"),
        "nodos_previos": list(n.get("nodos_previos") or []),
        "nodos_siguientes": list(n.get("nodos_siguientes") or []),
        "condiciones_activacion": cond,
        "ids_alias": list(n.get("ids_alias") or []),
    }
    if n.get("estado") == "deprecado":
        out["deprecado"] = True
    extra = sorted(set(n) - CON_DESTINO - set(SIN_DESTINO))
    if extra:
        problemas.append("campo de la forja fuera de su propio esquema: %s" % extra)
    sidecar = {k: n[k] for k in SIN_DESTINO if k in n}
    sidecar["dominio_forja"] = n.get("dominio")
    fechas = [f.get("fecha") for f in n.get("fuentes") or []]
    if fechas:
        sidecar["fuentes_fecha"] = fechas
    return out, sidecar, problemas


def vacios(nodo):
    """Campos obligatorios de My-idea vacios en el nodo convertido."""
    obligatorios = ("node_id", "fase_proyecto", "dominio", "titulo_concepto", "fuente",
                    "resumen_teorico", "pasos_accionables", "entregable_esperado",
                    "condiciones_activacion")
    fuera = []
    for c in obligatorios:
        v = nodo.get(c)
        if v is None or (isinstance(v, str) and not v.strip()) or (isinstance(v, list) and not v):
            fuera.append(c)
    if nodo.get("fase_proyecto") and nodo["fase_proyecto"] not in FASES_VALIDAS:
        fuera.append("fase_proyecto (valor invalido)")
    return fuera


# ---------------------------------------------------------------------------
# Informe
# ---------------------------------------------------------------------------

def construir(forja, salida, fases, incluir_forja, ruta_fases="", entradas=ENTRADAS):
    nodos, fuentes = leer_forja(forja)
    ids_mi, alias_mi = catalogo_my_idea()
    dominios_mi = dominios_de_my_idea()
    canonicas = canonicas_de_my_idea()

    fuera = [n for n in nodos if n.get("dominio") in DOMINIOS_FUERA and not incluir_forja]
    a_otro_mundo = [n for n in nodos if n.get("dominio") in DOMINIOS_A_OTRO_MUNDO]
    dentro = [n for n in nodos if n not in fuera and n not in a_otro_mundo]
    ids_pack = {n["id"] for n in dentro}
    ids_forja = {n["id"] for n in nodos}

    convertidos, sidecars, problemas = {}, collections.defaultdict(dict), []
    for n in dentro:
        c, s, p = convertir(n, fuentes, fases)
        convertidos[c["node_id"]] = c
        if s:
            sidecars[c["dominio"]][c["node_id"]] = s
        problemas += ["%s: %s" % (c["node_id"], x) for x in p]

    # Colisiones con el catalogo de My-idea (id vivo, id deprecado o alias).
    colisiones = []
    for nid in sorted(ids_pack):
        if nid in ids_mi:
            colisiones.append((nid, "id %s en dataset/nodos" % ids_mi[nid].upper()))
        elif nid in alias_mi:
            colisiones.append((nid, "alias de %s en dataset/nodos" % alias_mi[nid]))
        for a in convertidos[nid]["ids_alias"]:
            if a in ids_mi or a in alias_mi:
                colisiones.append((nid, "su alias %s ya existe en My-idea" % a))

    # Aristas: destino inexistente, destino fuera del pack, reciprocidad.
    rotas, al_catalogo, fuera_pack, no_reciprocas = [], [], [], []
    for nid, c in sorted(convertidos.items()):
        for campo, inverso in (("nodos_previos", "nodos_siguientes"),
                               ("nodos_siguientes", "nodos_previos")):
            for dest in c[campo]:
                if dest in ids_pack:
                    if nid not in convertidos[dest][inverso]:
                        no_reciprocas.append((nid, campo, dest))
                elif dest in ids_forja:
                    fuera_pack.append((nid, campo, dest))
                elif dest in ids_mi or dest in alias_mi:
                    al_catalogo.append((nid, campo, dest))
                else:
                    rotas.append((nid, campo, dest))

    vacios_por_campo = collections.Counter()
    ejemplos_vacio = collections.defaultdict(list)
    ids_malos = []
    for nid, c in convertidos.items():
        for campo in vacios(c):
            vacios_por_campo[campo] += 1
            if len(ejemplos_vacio[campo]) < 3:
                ejemplos_vacio[campo].append(nid)
        if not RE_ID.match(nid or ""):
            ids_malos.append(nid)

    grafias_usadas = collections.Counter(g for c in convertidos.values()
                                         for g in c["fuente"].split(SEP_FUENTE) if g)
    no_canonicas = sorted(g for g in grafias_usadas if canonicas is not None and g not in canonicas)

    sin_destino = collections.Counter(k for n in dentro for k in SIN_DESTINO if k in n)
    sin_destino["fuentes[].fecha"] = sum(1 for n in dentro if n.get("fuentes"))

    por_dominio = collections.Counter(c["dominio"] for c in convertidos.values())
    dominios_nuevos = sorted(d for d in por_dominio if d not in dominios_mi)
    sin_mapa = sorted({n.get("dominio") for n in dentro if n.get("dominio") not in DOMINIO_DESTINO})

    # El registro de fases, INCREMENTAL: ids del pack sin fase (los nuevos de la
    # forja) e ids del registro que ya no estan en el pack (para revisar).
    ids_sin_fase = sorted(i for i in convertidos if not fases.get(i))
    ids_fase_huerfanos = sorted(i for i in fases if i not in convertidos)

    # Las entradas horneadas: puentes, semillas y brecha.
    horneado = {}
    for nombre in ("bridges_aprobados.json", "entry_seeds.json", "brecha_semillas.json"):
        rp = Path(entradas) / nombre
        horneado[nombre] = json.load(io.open(rp, encoding="utf-8")) if rp.exists() else None
    problemas_puentes = []
    puentes = (horneado["bridges_aprobados.json"] or {}).get("aprobados") or []
    por_ancla = collections.Counter(pz.get("core") for pz in puentes)
    for pz in puentes:
        c, m = pz.get("core"), pz.get("dominio")
        if ids_mi.get(c) != "vivo":
            problemas_puentes.append("ancla %s no es un nodo VIVO de My-idea" % c)
        elif dominio_de_nodo_mi(c) != "core":
            problemas_puentes.append("ancla %s no es del nucleo (ley del ancla)" % c)
        if m not in convertidos:
            problemas_puentes.append("el nodo del mundo %s no esta en el pack" % m)
    for c, k in por_ancla.items():
        if k > 3:
            problemas_puentes.append("ancla %s con %d puentes (el tope de integrar_packs es 3)" % (c, k))
    semillas = horneado["entry_seeds.json"] or []
    semillas_fuera = [s for s in semillas if s not in convertidos]
    brecha = ((horneado["brecha_semillas.json"] or {}).get("primer_equipo") or {})
    brecha_fuera = sorted({v for v in brecha.values() if v not in convertidos})

    # Escritura del pack (nunca dentro de dataset/).
    salida = Path(salida).resolve()
    if salida == DATASET.resolve() or DATASET.resolve() in salida.parents:
        raise SystemExit("ROJO: --salida apunta dentro de dataset/ (%s). Este script no "
                         "escribe ahi: eso es integrar_packs.py --ejecutar, con credencial." % salida)
    for dom in por_dominio:
        (salida / dom / "nodos").mkdir(parents=True, exist_ok=True)
        (salida / dom / "metadata").mkdir(parents=True, exist_ok=True)
    for nid, c in convertidos.items():
        p = salida / c["dominio"] / "nodos" / ("%s.json" % nid)
        p.write_text(json.dumps(c, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for dom, s in sidecars.items():
        (salida / dom / "metadata" / "forja_campos_sin_destino.json").write_text(
            json.dumps(s, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for dom in por_dominio:
        for nombre, contenido in horneado.items():
            if contenido is not None:
                (salida / dom / "metadata" / nombre).write_text(
                    json.dumps(contenido, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # La lista blanca de My-idea, corrida sobre el pack recien escrito.
    sys.path.insert(0, str(BASE / "scripts" / "expansion"))
    from validar_esquema import validar_carpeta
    validacion = {dom: validar_carpeta(salida / dom / "nodos") for dom in por_dominio}

    L = []
    w = L.append
    w("INFORME DEL PUENTE DE LA FORJA A LA APP, MODO SECO")
    w("forja leida: %s" % forja)
    w("pack escrito en: %s (fuera de dataset/)" % salida)
    w("")
    w("1. VOLUMEN")
    w("   nodos en la forja: %d" % len(nodos))
    w("   nodos en el pack: %d" % len(convertidos))
    w("   fuera del pack por dominio interno de la forja: %d %s"
      % (len(fuera), [n["id"] for n in fuera]))
    for dom, casa in sorted(DOMINIOS_A_OTRO_MUNDO.items()):
        ids_o = [n["id"] for n in a_otro_mundo if n.get("dominio") == dom]
        w("   fuera del pack por ser de otro mundo (%s, a %s): %d %s" % (dom, casa, len(ids_o), ids_o))
    for dom_f, k in sorted(collections.Counter(n.get("dominio") for n in dentro).items()):
        w("   dominio de la forja %-22s %3d nodos, destino %s" % (dom_f, k, DOMINIO_DESTINO.get(dom_f, "(SIN DESTINO)")))
    for dom, k in sorted(por_dominio.items()):
        w("   dominio %-22s %3d nodos" % (dom, k))
    w("   dominios del pack que Gate 0 de My-idea NO admite hoy: %s" % (dominios_nuevos or "(ninguno)"))
    w("   dominios de la forja SIN destino declarado (desconocidos): %s" % (sin_mapa or "(ninguno)"))
    w("")
    w("2. IDS QUE COLISIONAN CON EL CATALOGO DE MY-IDEA (id vivo, id deprecado o alias): %d" % len(colisiones))
    for nid, motivo in colisiones:
        w("   COLISION> %s: %s" % (nid, motivo))
    w("")
    w("3. ARISTAS")
    w("   aristas a ids INEXISTENTES (ni en la forja ni en My-idea): %d" % len(rotas))
    for x in rotas[:40]:
        w("   ROTA> %s.%s -> %s" % x)
    w("   aristas a ids de la forja que quedaron FUERA del pack: %d" % len(fuera_pack))
    for x in fuera_pack[:20]:
        w("   FUERA DEL PACK> %s.%s -> %s" % x)
    w("   aristas a ids del catalogo de My-idea: %d" % len(al_catalogo))
    for x in al_catalogo[:20]:
        w("   AL CATALOGO> %s.%s -> %s" % x)
    w("   aristas dentro del pack SIN su reciproca: %d" % len(no_reciprocas))
    for x in no_reciprocas[:20]:
        w("   SIN RECIPROCA> %s.%s -> %s" % x)
    w("")
    w("4. CAMPOS OBLIGATORIOS DE MY-IDEA VACIOS EN EL PACK")
    w("   registro de fases leido: %s (%d ids)" % (ruta_fases, len(fases)))
    w("   ids del pack SIN fase en el registro (los nuevos que faltan por clasificar): %d %s"
      % (len(ids_sin_fase), ids_sin_fase[:20]))
    w("   ids del registro que ya NO estan en el pack: %d %s" % (len(ids_fase_huerfanos), ids_fase_huerfanos[:10]))
    w("   reparto de fases en el pack: %s" % dict(sorted(collections.Counter(
        c["fase_proyecto"] or "(vacia)" for c in convertidos.values()).items())))
    if not vacios_por_campo:
        w("   (ninguno)")
    for campo, k in sorted(vacios_por_campo.items()):
        w("   %-30s %3d nodos, p. ej. %s" % (campo, k, ejemplos_vacio[campo]))
    w("   node_id que no son ascii minuscula: %d %s" % (len(ids_malos), ids_malos[:5]))
    w("")
    w("5. EL CAMPO fuente CONTRA LA LISTA CANONICA DE MY-IDEA (la que valida Gate 0)")
    for g, k in grafias_usadas.most_common():
        w("   %3d nodos | %s | canonica en My-idea: %s"
          % (k, g, "SI" if canonicas is not None and g in canonicas else "NO"))
    w("   grafias que Gate 0 rechazaria hoy: %d" % len(no_canonicas))
    w("")
    w("6. CAMPOS DE LA FORJA SIN DESTINO EN EL ESQUEMA DE MY-IDEA (viajan en metadata/forja_campos_sin_destino.json)")
    for k, v in sorted(sin_destino.items()):
        w("   %-18s %3d nodos" % (k, v))
    w("")
    w("7. LA LISTA BLANCA DE MY-IDEA (scripts/expansion/validar_esquema.py) SOBRE EL PACK")
    for dom, (n, fallas) in sorted(validacion.items()):
        w("   %-22s %3d nodos, %3d falla(s)" % (dom, n, len(fallas)))
        tipos = collections.Counter(re.sub(r"'.*", "", m) for _a, m in fallas)
        for t, k in tipos.most_common():
            w("      %3d x %s" % (k, t))
    w("")
    w("8. LAS ENTRADAS HORNEADAS DEL PACK (docs/puente_forja/, copiadas a <dominio>/metadata/)")
    w("   bridges_aprobados.json: %s | puentes %d | anclas distintas %d | maximo por ancla %d"
      % ("SI" if horneado["bridges_aprobados.json"] else "NO", len(puentes), len(por_ancla),
         max(por_ancla.values()) if por_ancla else 0))
    for x in problemas_puentes:
        w("   PUENTE MAL> %s" % x)
    w("   problemas de puentes: %d" % len(problemas_puentes))
    w("   entry_seeds.json: %s | semillas %d | fuera del pack %d %s"
      % ("SI" if horneado["entry_seeds.json"] else "NO", len(semillas), len(semillas_fuera), semillas_fuera))
    w("   brecha_semillas.json: %s | fases mapeadas %d | nodos fuera del pack %d %s"
      % ("SI" if horneado["brecha_semillas.json"] else "NO", len(brecha), len(brecha_fuera), brecha_fuera))
    w("   problemas de conversion: %d" % len(problemas))
    for x in problemas[:20]:
        w("   PROBLEMA> %s" % x)
    return "\n".join(L) + "\n"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--forja", default=str(FORJA_DEFECTO))
    ap.add_argument("--salida", default=None)
    ap.add_argument("--fases", default=str(FASES_DEFECTO),
                    help="registro de fases (.jsonl incremental o .json {node_id: fase})")
    ap.add_argument("--incluir-forja", action="store_true")
    a = ap.parse_args()
    forja = Path(a.forja).resolve()
    if not (forja / "dataset" / "nodos.jsonl").exists():
        print("ROJO: no encuentro %s" % (forja / "dataset" / "nodos.jsonl"))
        return 2
    fases = leer_fases(a.fases)
    salida = a.salida or tempfile.mkdtemp(prefix="puente_forja_")
    print(construir(forja, salida, fases, a.incluir_forja, ruta_fases=a.fases))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
