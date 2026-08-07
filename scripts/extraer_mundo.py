#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extraer_mundo.py - Extraccion de nodos para los mundos nuevos, en DOS
etapas, siguiendo docs/SOP_EXTRACCION_PACKS.md.

Por que dos etapas y no una pasada a granel: el camino a granel
(scripts/pipeline_libros.py, un envio por trozo de libro pidiendo nodos
directamente) produjo packs de 896 y 332 nodos, inflados de conceptos
repetidos. El camino del SOP (indice primero, aprobacion del fundador,
luego nodos anclados al texto real) produjo risk_management con 55 nodos
y es el que entro limpio en la v1.4. La factura de la API no es el
problema; la limpieza posterior si.

  Etapa 1 (indice): a cada trozo se le pide SOLO una lista de conceptos
  (titulo, que aporta, ancla, fase). Salida pequena, sin riesgo de corte.
  Se consolida localmente en un indice por mundo, para que el fundador lo
  apruebe. Ningun nodo nace todavia.

  Etapa 2 (nodos): por cada concepto APROBADO se envia el concepto mas el
  fragmento real donde vive. El modelo no puede inventar un nodo que no se
  aprobo, y ninguno nace de memoria.

LAS TRAMPAS QUE ESTE SCRIPT CIERRA (todas cazadas en corridas anteriores):

  - Los bloques de pensamiento no rompen la lectura: se recorre
    response.content buscando type == "text", jamas content[0].
  - El corte por techo de tokens NO se reintenta contra el mismo techo. El
    techo ESCALA (16k -> 32k -> 64k) y, si aun asi se corta, la tanda se
    PARTE en dos. Repetir la condicion que causo el fallo no es reintentar.
    max_tokens es solo un techo: no se paga por lo que no se genera.
  - El esquema no se redeclara aqui: se importa del validador real
    (scripts/expansion/validar_esquema.py), que es la vara.
  - Reanudable: lo ya hecho no se vuelve a pagar.
  - Nada se degrada en silencio. Lo que no pasa las barandas se aparta a un
    archivo de rechazos con su motivo, y se dice en el resumen.

Uso:
  python scripts/extraer_mundo.py --mundo compras --etapa indice --dry-run
  python scripts/extraer_mundo.py --mundo compras --etapa indice
  python scripts/extraer_mundo.py --mundo compras --etapa nodos
"""
import argparse
import json
import os
import re
import sys
import time
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(BASE / "scripts" / "expansion"))

from chunker import chunk_text  # noqa: E402
# La vara de esquema es el validador del pipeline, no este archivo.
from validar_esquema import (  # noqa: E402
    CAMPOS_PERMITIDOS,
    FASES_VALIDAS,
    OBLIGATORIOS_NO_VACIOS,
    RE_ID,
)

MODEL = "claude-sonnet-5"
# La escalera de techos. Ver la cabecera: reintentar un corte con el mismo
# techo es reintentar el fallo.
TECHOS = (16000, 32000, 64000)
MAX_REINTENTOS_RED = 3
BACKOFF_BASE_SEG = 5
MAX_WORDS_POR_CHUNK = 5000
OVERLAP_WORDS = 500
CONCEPTOS_POR_TANDA = 8
# Tope de conceptos por fragmento. Sin tope, la sonda del 2026-08-07 devolvio 16
# por fragmento: a ese ritmo salen ~220 conceptos en entrega y ~700 en compras, y
# un indice de 700 lineas no lo revisa nadie. El tope obliga a ELEGIR en la
# fuente, que es donde se ve cual concepto vale.
MAX_CONCEPTOS_POR_TROZO = 6
# El indice consolidado que se le entrega al fundador (rango del SOP).
RANGO_INDICE = (40, 80)
PALABRAS_RESUMEN = (80, 150)
# Tirada de palabras literales que delata copia en vez de destilado.
TIRADA_LITERAL = 12
# Precio introductorio de claude-sonnet-5 (hasta 2026-08-31); lista: $3/$15.
PRECIO_IN_MTOK = 2.00
PRECIO_OUT_MTOK = 10.00

# ---------------------------------------------------------------------------
# Los dos mundos. El reparto de fuentes lo adjudico el fundador (2026-08-07,
# docs/PLAN_EXTRACCION_COMPRAS_Y_ENTREGA.md): el inventario de Muller va a
# compras, y Voss entra ACOTADO a proveedores.
#
# Las fuentes se leen donde viven (txt/), no se espejan a books/: duplicar
# 1.4 MB de texto crearia dos copias que se separan.
# ---------------------------------------------------------------------------
MUNDOS = {
    "compras": {
        "dominio": "compras",
        "label": "compras y abastecimiento (elegir proveedores, negociar, contratar, "
                 "controlar lo que se compra y el inventario que queda)",
        "fuentes": [
            ("txt/Procurenment/Diana L. Lindstrom - Procurement Project Management Success_ "
             "Achieving a Higher Level of Effectiveness-J. Ross Publishing (2014).txt",
             "Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014)"),
            ("txt/Procurenment/MULLER_INVENTARIO_EXTRACTO_MINERIA.md",
             "Max Muller, Essentials of Inventory Management"),
            ("txt/Procurenment/Rompe la barrera del no_ 9 prin - Chris Voss.txt",
             "Chris Voss, Rompe la barrera del no"),
        ],
    },
    "entrega": {
        "dominio": "entrega",
        "label": "entrega y logistica de salida (empacar, despachar, couriers, "
                 "fulfilment de comercio electronico y ultima milla)",
        "fuentes": [
            ("txt/Supply chain/RUSHTON_EXTRACTO_MINERIA.md",
             "Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management"),
            ("txt/Supply chain/E-logistics_Cap8_B2C_ecommerce_y_fulfilment.md",
             "Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment)"),
            ("txt/Supply chain/HowToPack_fxcom.txt", "Guia de empaque para envios (FedEx)"),
            ("txt/Supply chain/dhl_express_packing_guide_en.txt", "DHL Express, Guia de empaque"),
            ("txt/Supply chain/Packaging_Guidelines.txt", "Guia de empaque para transporte"),
            ("txt/Supply chain/ISTA_3P_26-26_Overview.txt",
             "ISTA 3P, Protocolo de ensayo de empaque para paqueteria"),
            ("txt/Supply chain/EXTRACCION_EMPAQUE_COURIERS.md",
             "Requisitos de empaque de los couriers"),
            ("txt/Supply chain/packaging_guide_infographic.txt", "Guia visual de empaque"),
        ],
    },
}

# Acotes por fuente: la palabra del fundador, aplicada en la ETAPA 1, antes de
# que nazca un solo nodo. Un acote que se aplicara despues no ahorraria nada.
ACOTES = {
    "Chris Voss, Rompe la barrera del no":
        "ACOTE OBLIGATORIO DE ESTA FUENTE: solo se admiten conceptos que se puedan "
        "anclar a una COMPRA real: negociar con un proveedor, un precio, un plazo, "
        "una garantia, un contrato de suministro. Si el concepto es de negociacion "
        "general (rehenes, salarios, vender a un cliente), NO lo incluyas aunque sea "
        "bueno. Es mejor devolver pocos conceptos que traer los que no son de comprar.",
}


# ---------------------------------------------------------------------------
# El envio endurecido
# ---------------------------------------------------------------------------
def _texto_de(respuesta):
    """El texto de la respuesta, sin asumir que viene en el primer bloque.

    Cuando el pensamiento esta activo, content[0] es un bloque de tipo
    "thinking" y leerlo directo devuelve vacio o revienta. Se busca por tipo.
    """
    for bloque in respuesta.content:
        if getattr(bloque, "type", "") == "text":
            return bloque.text
    return ""


def _extraer_arreglo(texto):
    """Tolera preambulos y vallas de markdown alrededor del JSON."""
    t = texto.strip()
    for valla in ("```json", "```"):
        if t.startswith(valla):
            t = t[len(valla):]
    if t.endswith("```"):
        t = t[:-3]
    t = t.strip()
    ini, fin = t.find("["), t.rfind("]")
    if ini != -1 and fin > ini:
        t = t[ini:fin + 1]
    return t


def _mensaje(cliente, techo, system, prompt):
    """SIEMPRE por streaming.

    Cazado en vivo el 2026-08-07: el SDK RECHAZA la llamada sin streaming
    cuando el techo es lo bastante alto como para que la peticion pudiera
    pasar de 10 minutos ("Streaming is required for operations that may take
    longer than 10 minutes"). O sea, la escalera de techos choca contra una
    segunda baranda del SDK justo cuando mas falta hace subir el techo.

    Se transmite siempre, no solo en los techos altos: un umbral seria una
    rama que casi nunca se ejercita y que envejece sin que nadie lo note.
    El precio de transmitir es que el SDK ya no reintenta solo lo transitorio,
    y por eso el bucle de reintentos de aqui abajo es obligatorio.
    """
    with cliente.messages.stream(
        model=MODEL,
        max_tokens=techo,
        system=system,
        messages=[{"role": "user", "content": prompt}],
    ) as s:
        return s.get_final_message()


def llamar(cliente, system, prompt, uso):
    """Una llamada, con la escalera de techos y el backoff de red.

    Devuelve (lista, None) o (None, motivo). El motivo "corte" es especial:
    le dice al llamador que parta la tanda y reenvie las mitades.
    """
    ultimo = None
    for intento, techo in enumerate(TECHOS, start=1):
        for red in range(1, MAX_REINTENTOS_RED + 1):
            try:
                r = _mensaje(cliente, techo, system, prompt)
                uso["in"] += r.usage.input_tokens
                uso["out"] += r.usage.output_tokens

                if r.stop_reason == "max_tokens":
                    ultimo = (f"cortada por el techo ({r.usage.output_tokens} de {techo})")
                    print(f"    [techo {intento}/{len(TECHOS)}] {ultimo}; subiendo")
                    break  # sube el techo, no repite el mismo

                try:
                    return json.loads(_extraer_arreglo(_texto_de(r))), None
                except json.JSONDecodeError as e:
                    ultimo = f"JSON invalido: {e}"
                    print(f"    [reintento {red}/{MAX_REINTENTOS_RED}] {ultimo}")
                    continue
            except Exception as e:  # rate limit, timeout, red
                ultimo = str(e)
                if red < MAX_REINTENTOS_RED:
                    espera = BACKOFF_BASE_SEG * (2 ** (red - 1))
                    print(f"    [reintento {red}/{MAX_REINTENTOS_RED}] {ultimo}; esperando {espera}s")
                    time.sleep(espera)
        else:
            continue  # agoto los reintentos de red en este techo, prueba el siguiente
    if ultimo and "cortada por el techo" in ultimo:
        return None, "corte"
    return None, f"fallo tras la escalera completa: {ultimo}"


# ---------------------------------------------------------------------------
# Las barandas locales (puras y testeables: no gastan un token)
# ---------------------------------------------------------------------------
GUIONES_VETADOS = ("—", "–")

# El modelo NUNCA escribe "dominio": lo inyecta el codigo despues de revisar,
# para no confiarle al modelo a que mundo pertenece el nodo. Asi que la revision
# no puede exigirselo, o rechazaria todos los nodos buenos. El validador real si
# lo exige, y para entonces ya esta puesto.
OBLIGATORIOS_DEL_MODELO = OBLIGATORIOS_NO_VACIOS - {"dominio"}


def _normalizar(texto):
    """Minusculas, sin acentos y sin puntuacion: para comparar palabras."""
    t = unicodedata.normalize("NFD", texto.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9\s]", " ", t).split()


def tirada_literal(resumen, fuente, n=TIRADA_LITERAL):
    """La primera tirada de n palabras que el resumen comparte LITERAL con la
    fuente, o None. Es la diferencia comprobable entre destilar y copiar: no
    hace falta criterio para verla, y las fuentes tienen copyright."""
    a, b = _normalizar(resumen), _normalizar(fuente)
    if len(a) < n or len(b) < n:
        return None
    tiradas_fuente = {" ".join(b[i:i + n]) for i in range(len(b) - n + 1)}
    for i in range(len(a) - n + 1):
        t = " ".join(a[i:i + n])
        if t in tiradas_fuente:
            return t
    return None


def revisar_nodo(nodo, fragmento, ids_tomados):
    """Todas las fallas del nodo, en una lista. Vacia = limpio.

    Se revisa TODO y se devuelve todo junto, en vez de parar en la primera:
    un nodo con tres problemas tiene que volver con los tres, no de uno en uno.
    """
    fallas = []

    renegados = set(nodo) - CAMPOS_PERMITIDOS
    if renegados:
        fallas.append(f"campos fuera de la lista blanca: {sorted(renegados)}")
    for campo in OBLIGATORIOS_DEL_MODELO:
        if not nodo.get(campo):
            fallas.append(f"falta el obligatorio '{campo}'")

    nid = nodo.get("node_id", "")
    if nid and not RE_ID.match(nid):
        fallas.append(f"node_id fuera de ^[a-z0-9_]+$: '{nid}'")
    if nid and nid in ids_tomados:
        fallas.append(f"node_id ya existe en el universo: '{nid}'")

    fase = nodo.get("fase_proyecto")
    if fase and fase not in FASES_VALIDAS:
        fallas.append(f"fase_proyecto invalida: '{fase}'")

    resumen = nodo.get("resumen_teorico", "")
    palabras = len(resumen.split())
    if resumen and not (PALABRAS_RESUMEN[0] <= palabras <= PALABRAS_RESUMEN[1]):
        fallas.append(f"resumen_teorico de {palabras} palabras "
                      f"(se pide {PALABRAS_RESUMEN[0]}-{PALABRAS_RESUMEN[1]})")

    copiado = tirada_literal(resumen, fragmento)
    if copiado:
        fallas.append(f"copia literal de la fuente: '...{copiado}...'")

    for campo, valor in nodo.items():
        texto = " ".join(valor) if isinstance(valor, list) else str(valor)
        if any(g in texto for g in GUIONES_VETADOS):
            fallas.append(f"guion largo en '{campo}'")

    etiqueta = nodo.get("etiqueta_arbol", "")
    if etiqueta and (len(etiqueta) > 40 or len(etiqueta.split()) > 6):
        fallas.append(f"etiqueta_arbol de {len(etiqueta.split())} palabras y "
                      f"{len(etiqueta)} caracteres (max 6 y 40)")

    return fallas


# ---------------------------------------------------------------------------
# Etapa 1: el indice
# ---------------------------------------------------------------------------
def prompt_indice(mundo_label, fuente_label, acote):
    extra = f"\n\n{acote}" if acote else ""
    return f"""Eres un experto en destilar libros a conceptos accionables para emprendedores.

Lees fragmentos de fuentes sobre {mundo_label} y devuelves un INDICE de conceptos:
todavia NO se escriben nodos. Solo la lista de lo que merece ser un concepto.

Un concepto merece entrar si un emprendedor SOLO, sin equipo y sin jefe, puede
hacer algo con el. Descarta lo que solo aplique a una corporacion con
departamentos, y descarta el relleno (historias, anecdotas, biografias).

Un concepto = una idea. No agrupes tres ni partas una en cinco.

DEVUELVE COMO MUCHO {MAX_CONCEPTOS_POR_TROZO} CONCEPTOS, los mas valiosos del
fragmento. Si hay mas candidatos, ELIGE: prefiere el concepto que cambia lo que
la persona hace, sobre el que solo describe. Devolver menos es correcto.{extra}

Devuelve EXCLUSIVAMENTE un arreglo JSON. Nada antes, nada despues, sin markdown.
Cada objeto:
{{
  "titulo": "Nombre corto del concepto",
  "aporta": "Una linea: que se lleva el emprendedor con esto",
  "ancla": "La seccion o el encabezado del fragmento donde vive",
  "fase": "ideacion | validacion | planificacion | ejecucion"
}}

Fuente: {fuente_label}

Si el fragmento no tiene conceptos aprovechables, devuelve []."""


def clave_titulo(titulo):
    return " ".join(_normalizar(titulo))


def etapa_indice(mundo, cliente, uso, max_llamadas=None, dry_run=False):
    cfg = MUNDOS[mundo]
    salida = BASE / "packs" / mundo / "indice"
    salida.mkdir(parents=True, exist_ok=True)
    progreso_path = salida / "_progreso_indice.json"
    progreso = json.loads(progreso_path.read_text(encoding="utf-8")) if progreso_path.exists() else {}
    crudos_path = salida / "_conceptos_crudos.json"
    crudos = json.loads(crudos_path.read_text(encoding="utf-8")) if crudos_path.exists() else []

    trozos = []
    for rel, label in cfg["fuentes"]:
        ruta = BASE / rel
        if not ruta.exists():
            print(f"  AVISO: no existe {rel}")
            continue
        for i, texto in enumerate(chunk_text(str(ruta), MAX_WORDS_POR_CHUNK, OVERLAP_WORDS)):
            trozos.append({"fuente": rel, "label": label, "i": i, "texto": texto})

    pendientes = [t for t in trozos if f"{t['fuente']}#{t['i']}" not in progreso]
    print(f"\n== {mundo}: {len(trozos)} trozos, {len(pendientes)} pendientes")
    if dry_run:
        palabras = sum(len(t["texto"].split()) for t in pendientes)
        est_in = palabras * 1.4 + len(pendientes) * 400
        est_out = len(pendientes) * 700
        print(f"   estimado: {est_in/1000:.0f}k in / {est_out/1000:.0f}k out "
              f"= ${est_in/1e6*PRECIO_IN_MTOK + est_out/1e6*PRECIO_OUT_MTOK:.2f}")
        return

    if max_llamadas:
        pendientes = pendientes[:max_llamadas]

    for n, t in enumerate(pendientes, start=1):
        print(f"  [{n}/{len(pendientes)}] {Path(t['fuente']).name} #{t['i']}")
        conceptos, err = llamar(
            cliente,
            prompt_indice(cfg["label"], t["label"], ACOTES.get(t["label"])),
            f"Fragmento:\n\n{t['texto']}",
            uso,
        )
        if err:
            print(f"    SALTADO: {err}")
            continue
        for c in conceptos:
            if not isinstance(c, dict) or not c.get("titulo"):
                continue
            c["fuente"] = t["fuente"]
            c["fuente_label"] = t["label"]
            c["chunk"] = t["i"]
            crudos.append(c)
        progreso[f"{t['fuente']}#{t['i']}"] = len(conceptos)
        crudos_path.write_text(json.dumps(crudos, ensure_ascii=False, indent=2), encoding="utf-8")
        progreso_path.write_text(json.dumps(progreso, ensure_ascii=False, indent=2), encoding="utf-8")

    consolidar_indice(mundo, crudos, salida)


def consolidar_indice(mundo, crudos, salida):
    """Funde repetidos por titulo normalizado y escribe el indice legible.

    La fusion es LOCAL: no se le paga al modelo por deduplicar lo que un
    diccionario resuelve. El solape entre trozos garantiza repetidos.
    """
    fundidos = {}
    for c in crudos:
        k = clave_titulo(c["titulo"])
        if k in fundidos:
            fundidos[k]["apariciones"] += 1
            if c["fuente"] not in fundidos[k]["fuentes"]:
                fundidos[k]["fuentes"].append(c["fuente"])
            fundidos[k]["chunks"].append({"fuente": c["fuente"], "chunk": c["chunk"]})
            continue
        fundidos[k] = {
            "titulo": c["titulo"],
            "aporta": c.get("aporta", ""),
            "ancla": c.get("ancla", ""),
            "fase": c.get("fase", "planificacion"),
            "fuentes": [c["fuente"]],
            "fuente_label": c.get("fuente_label", ""),
            "chunks": [{"fuente": c["fuente"], "chunk": c["chunk"]}],
            "apariciones": 1,
        }
    lista = sorted(fundidos.values(), key=lambda x: (-x["apariciones"], x["titulo"]))
    (salida / "_conceptos_fundidos.json").write_text(
        json.dumps(lista, ensure_ascii=False, indent=2), encoding="utf-8")

    orden = ["ideacion", "validacion", "planificacion", "ejecucion"]
    md = [f"# Indice tematico de {mundo}", "",
          f"{len(lista)} conceptos distintos, fundidos de {len(crudos)} apariciones.",
          "", "Marca con [ ] los que NO deben nacer. El resto se genera.", ""]
    for fase in orden:
        de_fase = [c for c in lista if c["fase"] == fase]
        if not de_fase:
            continue
        md.append(f"## {fase} ({len(de_fase)})")
        md.append("")
        for c in de_fase:
            md.append(f"- **{c['titulo']}** ({c['apariciones']}x) - {c['aporta']}")
        md.append("")
    (salida / f"INDICE_TEMATICO_{mundo}.md").write_text("\n".join(md), encoding="utf-8")
    print(f"\n  Indice: {len(lista)} conceptos distintos de {len(crudos)} apariciones")
    print(f"  -> {salida / f'INDICE_TEMATICO_{mundo}.md'}")


# ---------------------------------------------------------------------------
# Etapa 1-bis: consolidar el indice
#
# El dedupe local funde titulos IDENTICOS, que es lo que produce el solape entre
# trozos. No ve los casi-iguales: "Eleccion de canal de encuesta" y "Seleccion de
# metodo de encuesta segun canal" son el mismo concepto con dos nombres, y un
# diccionario no puede saberlo. Eso si necesita una lectura, y es UNA llamada
# sobre titulos cortos: barata comparada con generar los nodos repetidos y
# tirarlos despues.
# ---------------------------------------------------------------------------
def prompt_consolidar(mundo_label, cuantos):
    return f"""Eres un editor de indices de conocimiento sobre {mundo_label}.

Recibes una lista numerada de conceptos extraidos de varias fuentes. Muchos son
EL MISMO concepto con nombres distintos, o uno el caso particular de otro.

Tu trabajo: agruparlos en {cuantos[0]} a {cuantos[1]} conceptos finales.

REGLAS:
1. Cada numero de la entrada va en EXACTAMENTE UN grupo. Ninguno se queda fuera.
   Si un concepto no merece nacer, agrupalo igual y marcalo con "descartar": true.
2. El titulo final le habla al emprendedor, no al libro. Sin anglicismos de
   manual, sin nombres de autores, sin guiones largos.
3. Funde lo que es lo mismo. No fundas lo que solo se parece: si dos conceptos
   llevan a acciones distintas, son dos.
4. Marca "descartar": true lo que sea relleno, teoria sin accion, o que solo
   aplique a una corporacion con departamentos.

Devuelve EXCLUSIVAMENTE un arreglo JSON, sin markdown. Cada objeto:
{{
  "titulo": "El titulo final del concepto",
  "aporta": "Una linea: que se lleva el emprendedor",
  "fase": "ideacion | validacion | planificacion | ejecucion",
  "miembros": [3, 17, 42],
  "descartar": false
}}"""


ORDEN_FASES = ["ideacion", "validacion", "planificacion", "ejecucion"]


def escribir_indice_md(mundo, propuesto, salida, cabecera, huerfanos=()):
    """El indice legible. Vive en UNA funcion porque lo escriben dos: la
    consolidacion y la poda del fundador. Dos versiones del mismo formato se
    separarian a la primera edicion."""
    md = [f"# Indice propuesto de {mundo}", "", cabecera, "",
          "Borra las lineas de lo que NO debe nacer. Lo que quede se genera.", ""]
    for fase in ORDEN_FASES:
        de_fase = [c for c in propuesto if c["fase"] == fase]
        if not de_fase:
            continue
        md += [f"## {fase} ({len(de_fase)})", ""]
        for c in de_fase:
            md.append(f"- **{c['titulo']}** - {c['aporta']}")
            if len(c.get("fundidos_de", [])) > 1:
                md.append(f"  - funde: {', '.join(c['fundidos_de'])}")
        md.append("")
    if huerfanos:
        md += ["## Sin agrupar (se perderian si no los reclamas)", ""]
        md += [f"- {t}" for t in huerfanos] + [""]
    (salida / f"INDICE_PROPUESTO_{mundo}.md").write_text("\n".join(md), encoding="utf-8")


def etapa_consolidar(mundo, cliente, uso, max_llamadas=None, dry_run=False):
    cfg = MUNDOS[mundo]
    salida = BASE / "packs" / mundo / "indice"
    fundidos_path = salida / "_conceptos_fundidos.json"
    if not fundidos_path.exists():
        print(f"ERROR: falta {fundidos_path}. Corre antes la etapa 'indice'.")
        sys.exit(2)
    fundidos = json.loads(fundidos_path.read_text(encoding="utf-8"))
    print(f"\n== {mundo}: {len(fundidos)} conceptos a consolidar en "
          f"{RANGO_INDICE[0]}-{RANGO_INDICE[1]}")
    if dry_run:
        return

    lista = "\n".join(f"{i}. {c['titulo']} :: {c.get('aporta','')}"
                      for i, c in enumerate(fundidos))
    grupos, err = llamar(cliente, prompt_consolidar(cfg["label"], RANGO_INDICE),
                         f"Conceptos:\n\n{lista}", uso)
    if err:
        print(f"ERROR: la consolidacion fallo ({err}). No se escribe nada.")
        sys.exit(1)

    # Verificacion LOCAL, sin creerle al modelo: ningun concepto puede
    # desaparecer en silencio ni aparecer de la nada.
    asignados, inventados = set(), []
    propuesto = []
    for g in grupos:
        if not isinstance(g, dict) or not g.get("titulo"):
            continue
        miembros = []
        for i in g.get("miembros", []):
            if not isinstance(i, int) or not (0 <= i < len(fundidos)):
                inventados.append(i)
                continue
            miembros.append(i)
            asignados.add(i)
        if not miembros or g.get("descartar"):
            continue
        chunks, fuentes, label = [], [], ""
        for i in miembros:
            chunks.extend(fundidos[i]["chunks"])
            for f in fundidos[i]["fuentes"]:
                if f not in fuentes:
                    fuentes.append(f)
            label = label or fundidos[i].get("fuente_label", "")
        propuesto.append({
            "titulo": g["titulo"],
            "aporta": g.get("aporta", ""),
            "fase": g.get("fase", "planificacion"),
            "fuentes": fuentes,
            "fuente_label": label,
            "chunks": chunks,
            "fundidos_de": [fundidos[i]["titulo"] for i in miembros],
        })

    huerfanos = [fundidos[i]["titulo"] for i in range(len(fundidos)) if i not in asignados]
    (salida / "_indice_propuesto.json").write_text(
        json.dumps(propuesto, ensure_ascii=False, indent=2), encoding="utf-8")
    cabecera = f"{len(propuesto)} conceptos finales, fundidos de {len(fundidos)}."

    escribir_indice_md(mundo, propuesto, salida, cabecera, huerfanos)

    print(f"  {len(propuesto)} conceptos finales, {len(fundidos) - len(asignados)} sin agrupar")
    if inventados:
        print(f"  AVISO: el modelo cito {len(inventados)} indices que no existen; descartados")
    if huerfanos:
        print(f"  AVISO: {len(huerfanos)} conceptos quedaron fuera de todo grupo; van listados al final")
    print(f"  -> {salida / f'INDICE_PROPUESTO_{mundo}.md'}")


# ---------------------------------------------------------------------------
# Etapa 2: los nodos
# ---------------------------------------------------------------------------
def prompt_nodos(mundo_label, dominio):
    return f"""Eres un experto en destilar libros a nodos de un grafo de conocimiento
para emprendedores, sobre {mundo_label}.

Recibes CONCEPTOS YA APROBADOS y el fragmento real de la fuente donde vive cada
uno. Escribes un nodo por concepto. Ni uno mas: no inventes conceptos nuevos.

REGLAS QUE NO SE NEGOCIAN:
1. DESTILA, jamas copies. Las fuentes tienen copyright: el resumen va en tus
   palabras. Una tirada de {TIRADA_LITERAL} palabras identicas a la fuente hace
   que el nodo se rechace.
2. resumen_teorico: entre {PALABRAS_RESUMEN[0]} y {PALABRAS_RESUMEN[1]} palabras,
   con acentos correctos del espanol.
3. El tono le habla a UNA persona que puede estar sola, sin equipo y sin jefe.
   Cero "su organizacion", cero "el comite", cero "el departamento". Si la fuente
   habla en corporativo, traducelo a emprendedor individual.
4. pasos_accionables: de 3 a 6, imperativos, concretos, hacibles esta semana.
5. condiciones_activacion: de 2 a 4 SITUACIONES del emprendedor, en lenguaje
   llano. No describen el capitulo del libro, describen a la persona.
6. PROHIBIDOS los guiones largos y medios. Usa coma, dos puntos o punto.
7. nodos_previos y nodos_siguientes van como TITULOS textuales de otros
   conceptos (no como identificadores). El pipeline los resuelve despues.
8. etiqueta_arbol: maximo 6 palabras y 40 caracteres, en segunda persona o
   imperativo. Cero anglicismos de manual, cero nombres de autores. Es el
   titular que ve el emprendedor en el riel.

Devuelve EXCLUSIVAMENTE un arreglo JSON. Nada antes, nada despues, sin markdown.
Cada objeto, con estos campos y ninguno mas:
{{
  "node_id": "minusculas_y_guiones_bajos",
  "fase_proyecto": "ideacion | validacion | planificacion | ejecucion",
  "titulo_concepto": "El nombre del concepto",
  "fuente": "Autor, Titulo, seccion",
  "resumen_teorico": "...",
  "pasos_accionables": ["...", "..."],
  "entregable_esperado": "Una frase: el artefacto que queda en la mano",
  "nodos_previos": ["Titulo de otro concepto"],
  "nodos_siguientes": ["Titulo de otro concepto"],
  "condiciones_activacion": ["...", "..."],
  "etiqueta_arbol": "Tu Etiqueta Corta"
}}

El campo "dominio" NO lo escribes tu: lo pone el codigo ("{dominio}")."""


def texto_del_chunk(rel, indice, cache):
    if rel not in cache:
        cache[rel] = chunk_text(str(BASE / rel), MAX_WORDS_POR_CHUNK, OVERLAP_WORDS)
    trozos = cache[rel]
    return trozos[indice] if 0 <= indice < len(trozos) else ""


def ids_del_universo():
    ruta = BASE / "scripts" / "ids_existentes.txt"
    return {l.strip() for l in ruta.read_text(encoding="utf-8").splitlines() if l.strip()}


def enviar_tanda(cliente, system, tanda, cache, uso, dominio, ids_tomados, nodos_dir, rechazos):
    """Una tanda de conceptos. Si la respuesta se corta hasta el ultimo techo,
    la tanda se PARTE y cada mitad se reenvia: un concepto solo siempre cabe."""
    bloques = []
    for c in tanda:
        ref = c["chunks"][0]
        fragmento = texto_del_chunk(ref["fuente"], ref["chunk"], cache)
        bloques.append(
            f"### Concepto: {c['titulo']}\n"
            f"Fase: {c['fase']}\nQue aporta: {c.get('aporta','')}\n"
            f"Fuente: {c.get('fuente_label','')}\n"
            f"Fragmento real de la fuente:\n{fragmento}\n")
    nodos, err = llamar(cliente, system, "\n\n".join(bloques), uso)

    if err == "corte":
        if len(tanda) == 1:
            rechazos.append({"titulo": tanda[0]["titulo"], "motivo": "no cabe ni sola"})
            return 0
        medio = len(tanda) // 2
        print(f"    tanda cortada; partiendo en {medio} + {len(tanda) - medio}")
        return (enviar_tanda(cliente, system, tanda[:medio], cache, uso, dominio,
                             ids_tomados, nodos_dir, rechazos)
                + enviar_tanda(cliente, system, tanda[medio:], cache, uso, dominio,
                               ids_tomados, nodos_dir, rechazos))
    if err:
        for c in tanda:
            rechazos.append({"titulo": c["titulo"], "motivo": err})
        return 0

    guardados = 0
    for nodo in nodos:
        if not isinstance(nodo, dict):
            continue
        ref = tanda[0]["chunks"][0]
        fragmento = texto_del_chunk(ref["fuente"], ref["chunk"], cache)
        for c in tanda:
            if c["titulo"] == nodo.get("titulo_concepto"):
                r = c["chunks"][0]
                fragmento = texto_del_chunk(r["fuente"], r["chunk"], cache)
                break
        fallas = revisar_nodo(nodo, fragmento, ids_tomados)
        if fallas:
            rechazos.append({"titulo": nodo.get("titulo_concepto", "?"),
                             "node_id": nodo.get("node_id"), "motivo": fallas})
            continue
        # El dominio lo pone el codigo, justo tras fase_proyecto, nunca el modelo.
        ordenado = {}
        for k, v in nodo.items():
            ordenado[k] = v
            if k == "fase_proyecto":
                ordenado["dominio"] = dominio
        ordenado.setdefault("dominio", dominio)
        (nodos_dir / f"{ordenado['node_id']}.json").write_text(
            json.dumps(ordenado, ensure_ascii=False, indent=2), encoding="utf-8")
        ids_tomados.add(ordenado["node_id"])
        guardados += 1
    return guardados


def etapa_nodos(mundo, cliente, uso, max_llamadas=None, dry_run=False):
    cfg = MUNDOS[mundo]
    indice_dir = BASE / "packs" / mundo / "indice"
    aprobado = indice_dir / "indice_aprobado.json"
    if not aprobado.exists():
        print(f"ERROR: falta {aprobado}.\n"
              f"La etapa 2 no arranca sin el indice aprobado: ningun nodo nace sin visto.")
        sys.exit(2)

    conceptos = json.loads(aprobado.read_text(encoding="utf-8"))
    nodos_dir = BASE / "packs" / mundo / "nodos_crudos"
    nodos_dir.mkdir(parents=True, exist_ok=True)
    hechos = {p.stem for p in nodos_dir.glob("*.json")}
    ids_tomados = ids_del_universo() | hechos

    pendientes = [c for c in conceptos if clave_titulo(c["titulo"]) not in
                  {clave_titulo(t) for t in _titulos_hechos(nodos_dir)}]
    print(f"\n== {mundo}: {len(conceptos)} conceptos, {len(pendientes)} pendientes")
    if dry_run:
        print(f"   {(len(pendientes) + CONCEPTOS_POR_TANDA - 1)//CONCEPTOS_POR_TANDA} tandas "
              f"de hasta {CONCEPTOS_POR_TANDA}")
        return

    orden = ["ideacion", "validacion", "planificacion", "ejecucion"]
    pendientes.sort(key=lambda c: orden.index(c["fase"]) if c["fase"] in orden else 9)

    system = prompt_nodos(cfg["label"], cfg["dominio"])
    cache, rechazos, guardados = {}, [], 0
    tandas = [pendientes[i:i + CONCEPTOS_POR_TANDA]
              for i in range(0, len(pendientes), CONCEPTOS_POR_TANDA)]
    if max_llamadas:
        tandas = tandas[:max_llamadas]

    for n, tanda in enumerate(tandas, start=1):
        print(f"  [tanda {n}/{len(tandas)}] {len(tanda)} conceptos ({tanda[0]['fase']})")
        guardados += enviar_tanda(cliente, system, tanda, cache, uso, cfg["dominio"],
                                  ids_tomados, nodos_dir, rechazos)

    if rechazos:
        (nodos_dir / "_rechazos.json").write_text(
            json.dumps(rechazos, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n  Guardados {guardados} nodos. Rechazados {len(rechazos)}.")
    if rechazos:
        print(f"  Los rechazos, con su motivo, en {nodos_dir / '_rechazos.json'}")


def _titulos_hechos(nodos_dir):
    for p in nodos_dir.glob("*.json"):
        if p.name.startswith("_"):
            continue
        try:
            yield json.loads(p.read_text(encoding="utf-8")).get("titulo_concepto", "")
        except Exception:
            continue


# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mundo", required=True, choices=sorted(MUNDOS))
    ap.add_argument("--etapa", required=True, choices=("indice", "consolidar", "nodos"))
    ap.add_argument("--dry-run", action="store_true", help="cuenta y estima, no llama")
    ap.add_argument("--max-llamadas", type=int, help="tope de llamadas de esta corrida")
    args = ap.parse_args()

    cliente = None
    if not args.dry_run:
        from dotenv import load_dotenv
        import anthropic
        load_dotenv(BASE / ".env")
        clave = os.getenv("ANTHROPIC_API_KEY")
        if not clave:
            print("ERROR: falta ANTHROPIC_API_KEY en .env")
            sys.exit(2)
        cliente = anthropic.Anthropic(api_key=clave)

    uso = {"in": 0, "out": 0}
    inicio = time.time()
    {"indice": etapa_indice, "consolidar": etapa_consolidar, "nodos": etapa_nodos}[
        args.etapa](args.mundo, cliente, uso, args.max_llamadas, args.dry_run)

    if uso["in"] or uso["out"]:
        costo = uso["in"] / 1e6 * PRECIO_IN_MTOK + uso["out"] / 1e6 * PRECIO_OUT_MTOK
        print(f"\n  Tokens reales: {uso['in']:,} in / {uso['out']:,} out "
              f"= ${costo:.2f} en {time.time() - inicio:.0f}s")


if __name__ == "__main__":
    main()
