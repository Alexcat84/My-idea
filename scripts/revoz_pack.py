#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""revoz_pack.py - Regenera la VOZ de un lote de nodos. No su contenido.

EL ANCLAJE, y por que no es el que decia el encargo. La baranda pedia regenerar
"desde SU MISMO fragmento de fuente". Los libros de quality (Juran, Deming,
Crosby) NO estan en el repo: se usaron en la era P1-HSEQ y no se conservaron. No
hay fragmento al que anclar.

Asi que el ancla es EL NODO MISMO, y eso hace la baranda anti-invencion MAS
estricta, no menos: cuando se ancla a un libro, el modelo puede traer cualquier
cosa que este en el libro; anclado al nodo, el conjunto permitido es exactamente
un texto, y todo lo que no este ahi es invencion. La re-voz no es una
re-extraccion: es una traduccion de voz de un texto que ya fue aprobado.

LO QUE CAMBIA: la voz. LO QUE NO: los hechos, las cifras, el titulo, el id y las
aristas. Un nodo que vuelve diciendo algo nuevo se rechaza.

LAS BARANDAS, comprobables sin criterio:
  - toda CIFRA del texto nuevo tiene que estar en el viejo;
  - el vocabulario vetado desaparece (la gerencia, la alta direccion, el
    departamento, el comite, los stakeholders, su organizacion, el voseo);
  - resumen entre 80 y 150 palabras, cero guiones largos, tildes correctas;
  - titulo, node_id y aristas INTACTOS, salvo que el titulo lleve jerga; si un
    titulo cambia, se listan sus aristas entrantes para re-verificarlas.

Uso:
  python scripts/revoz_pack.py --lote packs/quality/poda/_revoz_lote.json --dry-run
  python scripts/revoz_pack.py --lote packs/quality/poda/_revoz_lote.json --tanda 40
"""
import argparse
import json
import os
import re
import sys
import time
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import libro_mayor  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
NODOS = BASE / "dataset" / "nodos"
MODEL = "claude-sonnet-5"
TECHOS = (16000, 32000, 64000)
PRECIO_IN, PRECIO_OUT = 2.00, 10.00
PALABRAS = (80, 150)
POR_TANDA = 40

VETADO = {
    "voz corporativa": [
        r"\bla gerencia\b", r"\bla alta direcci[óo]n\b", r"\bel departamento de\b",
        r"\btu departamento\b", r"\bel comit[ée]\b", r"\bun comit[ée]\b",
        r"\blos stakeholders\b", r"\blas partes interesadas\b",
        r"\b[st]u organizaci[óo]n\b", r"\brecursos humanos\b",
    ],
    # OJO con las ambiguas: "sabes", "puedes" y "tienes" son el TU correcto;
    # el voseo lleva TILDE ("sabes" con tilde). El patron [ee] cazaba las dos
    # y rechazo tres nodos bien escritos. Para esas formas se EXIGE la tilde.
    "voseo": [r"\bvos\b", r"\bpodés\b", r"\btenés\b", r"\bquerés\b", r"\bsabés\b", r"\bhacés\b"],
    # ORTOGRAFIA ROTA que la correccion automatica no alcanzo. Va como VETO y no
    # solo como correccion porque la lista de TILDES es finita: si el modelo
    # inventa una forma nueva sin tilde, la correccion no la ve y el nodo se
    # publicaria roto. Cazado en el piloto de voz: "pequeno" no es una palabra.
    "ortografia rota": [r"\b(?:pequen[oa]s?|disen(?:[oa]s?|ar|as|an|ado|ada)|manana|compania|espanol|senal(?:es)?|anos)\b",
                        r"\b(?:vision|hipotesis|solucion|validacion|automatizacion|version|decision|revision|mision|presion|precision|conversion)\b"],
    "matriz o puntaje": [
        r"\bmatriz de (?:riesgo|probabilidad|impacto|prioridad)", r"\bpunt[úu][ae]\b",
        r"\bescala de\s*1\s*a\s*(?:5|10)\b", r"\bprobabilidad\s*(?:x|por|\*)\s*impacto\b",
    ],
}
# SOLO las que llevan tilde SIEMPRE. La primera version incluia "cuando",
# "quien", "cuanto" y "mas", que solo la llevan cuando son interrogativas o de
# cantidad: "cuando llegue el pedido" es correcto sin tilde, y eso rechazo 39
# nodos buenos de 40 en la primera tanda. Una baranda que caza lo correcto no
# es estricta, es rota.
# ORTOGRAFIA: las que llevan tilde SIEMPRE, con su forma correcta. Se CORRIGEN
# a maquina antes de juzgar, en vez de rechazar el nodo entero: poner una tilde
# es determinista y no es inventar, y el experimento del 2026-08-07 ya dejo dicho
# que la ortografia no mueve la recuperacion (se cuida por la VOZ). Rechazar 15
# nodos buenos por una tilde seria pagar la API dos veces por un acento.
#
# NO entran las ambiguas: "practica"/"publico"/"practico" son tambien formas
# verbales ("el practica", "yo publico") y corregirlas a ciegas rompe frases
# correctas. Esas se dejan pasar y las mira el ojo humano.
TILDES = {
    "rapido": "rápido", "rapida": "rápida", "aqui": "aquí", "asi": "así",
    "despues": "después", "segun": "según", "tambien": "también",
    "metodo": "método", "metodos": "métodos", "tecnica": "técnica",
    "tecnicas": "técnicas", "articulo": "artículo", "articulos": "artículos",
    "fragil": "frágil", "fragiles": "frágiles", "numero": "número",
    "numeros": "números", "codigo": "código", "analisis": "análisis",
    "dia": "día", "dias": "días", "linea": "línea", "lineas": "líneas",
    "ademas": "además", "estandar": "estándar", "estandares": "estándares",
    "logistica": "logística", "economico": "económico", "economica": "económica",
    "basico": "básico", "basica": "básica", "unico": "único", "unica": "única",
    "credito": "crédito", "informacion": "información", "produccion": "producción",
    # Ampliacion tras el PILOTO DE VOZ (ago 2026): la --instruccion se paso
    # escrita SIN TILDES y el modelo imito el estilo. Ocho de quince nodos
    # salieron con la ortografia rota. Se corrige a maquina, que es determinista
    # y no es inventar, y ademas se veta abajo para que no vuelva a pasar.
    "vision": "visión", "hipotesis": "hipótesis", "solucion": "solución",
    "validacion": "validación", "creacion": "creación",
    "evaluacion": "evaluación", "definicion": "definición", "automatizacion": "automatización",
    "descripcion": "descripción", "iteracion": "iteración", "medicion": "medición",
    "operacion": "operación", "presentacion": "presentación", "reaccion": "reacción",
    "atencion": "atención", "intencion": "intención", "conversion": "conversión",
    "decision": "decisión", "precision": "precisión", "revision": "revisión",
    "mision": "misión", "presion": "presión", "version": "versión",
    # LA EÑE. No es una tilde: es otra letra, y "pequeno" no es una palabra.
    "pequeno": "pequeño", "pequena": "pequeña", "pequenos": "pequeños",
    "pequenas": "pequeñas", "diseno": "diseño", "disenos": "diseños",
    "disenar": "diseñar", "disenas": "diseñas", "diseno_v": "diseño",
    "disenan": "diseñan", "disenado": "diseñado", "disenada": "diseñada",
    "manana": "mañana", "compania": "compañía",
    "espanol": "español", "senal": "señal", "senales": "señales",
    "ano": "año", "anos": "años", "duena": "dueña", "dueno": "dueño",
}


def corregir_tildes(valor):
    """Pone las tildes que faltan, conservando mayuscula inicial."""
    if isinstance(valor, list):
        return [corregir_tildes(v) for v in valor]
    if not isinstance(valor, str):
        return valor

    def _una(m):
        w = m.group(0)
        fija = TILDES.get(w.lower())
        if not fija:
            return w
        return fija.capitalize() if w[0].isupper() else fija

    return re.sub(r"\b\w+\b", _una, valor, flags=re.UNICODE)


SIN_TILDE = tuple(TILDES)

SYSTEM = """Eres el redactor de un grafo de conocimiento para emprendedores.

Recibes UN nodo ya aprobado y lo reescribes EN LA VOZ DE LA CASA. No es una
re-extraccion: es una traduccion de voz. El contenido ya fue validado.

LO QUE NO PUEDES CAMBIAR:
- los HECHOS. Ni uno nuevo, ni uno menos.
- las CIFRAS. Si el nodo dice 15%, dice 15%. Si no dice ninguna, no inventes.
- el TITULO, salvo que el titulo mismo lleve jerga corporativa.

LO QUE SI CAMBIAS:
1. LA LENTE. Quien lee es UNA persona sola, con un telefono. Sin equipo, sin
   jefe, sin departamento, sin comite. Mueren "la gerencia", "la alta
   direccion", "el departamento", "los stakeholders", "tu organizacion".
   Nacen "tu", "tu negocio", "tu decides", "la persona que te ayuda".
   Si el texto dice "presentar a la alta direccion para justificar la
   inversion", eso se vuelve "tener el numero claro antes de decidir si vale
   la pena". El CONCEPTO se conserva; el supuesto de que hay jerarquia, no.
2. EL TU DE LA CASA. Jamas voseo: nada de "vos", "podes", "tenes".
3. SIN MATRICES NI PUNTAJES. Si el nodo puntua algo por probabilidad e
   impacto, o propone una matriz de dos ejes, cuenta el concepto SIN la
   escala: la gravedad se dice con palabras que una persona entiende.
4. SIN DATOS CABLEADOS de otro mercado. Un umbral legal, una tarifa o un
   organismo de un pais concreto se vuelve metodo mas "preguntalo en tu
   mercado". Si el dato es universal (una formula, una proporcion del propio
   libro), se queda.
5. ORTOGRAFIA IMPECABLE. Todas las tildes. Cero guiones largos o medios.
6. El resumen conserva APROXIMADAMENTE el largo del original. No lo alargues
   para que suene mejor: si el original decia lo suyo en 60 palabras, la
   version en voz de la casa tambien cabe en 60. Alargar es inventar.

Devuelve EXCLUSIVAMENTE un objeto JSON, sin markdown:
{"titulo_concepto": "...", "resumen_teorico": "...", "pasos_accionables": ["..."],
 "entregable_esperado": "...", "condiciones_activacion": ["..."]}

Si el titulo no llevaba jerga, devuelvelo IDENTICO."""


def _texto(r):
    for b in r.content:
        if getattr(b, "type", "") == "text":
            return b.text
    return ""


def _objeto(t):
    t = t.strip()
    for v in ("```json", "```"):
        if t.startswith(v):
            t = t[len(v):]
    if t.endswith("```"):
        t = t[:-3]
    i, j = t.find("{"), t.rfind("}")
    return t[i:j + 1] if i != -1 and j > i else t


def llamar(cli, prompt, uso):
    ultimo = None
    for techo in TECHOS:
        for intento in range(3):
            try:
                with cli.messages.stream(model=MODEL, max_tokens=techo, system=SYSTEM,
                                         messages=[{"role": "user", "content": prompt}]) as s:
                    r = s.get_final_message()
                uso["in"] += r.usage.input_tokens
                uso["out"] += r.usage.output_tokens
                if r.stop_reason == "max_tokens":
                    ultimo = "cortada"
                    break
                return json.loads(_objeto(_texto(r))), None
            except json.JSONDecodeError as e:
                ultimo = f"JSON invalido: {e}"
            except Exception as e:
                ultimo = str(e)
                time.sleep(5 * (intento + 1))
    return None, ultimo or "fallo"


RE_CIFRA = re.compile(r"\d+(?:[.,]\d+)?")


def texto_de(n):
    return " ".join([n.get("titulo_concepto", ""), n.get("resumen_teorico", ""),
                     " ".join(n.get("pasos_accionables") or []),
                     " ".join(n.get("condiciones_activacion") or []),
                     n.get("entregable_esperado", "") or ""])


def revisar(nuevo, viejo):
    """Todas las fallas juntas. Vacia = limpio."""
    fallas = []
    t_nuevo, t_viejo = texto_de(nuevo), texto_de(viejo)

    inventadas = sorted(set(RE_CIFRA.findall(t_nuevo)) - set(RE_CIFRA.findall(t_viejo)))
    if inventadas:
        fallas.append(f"cifras que el nodo original no tenia: {inventadas}")

    for etiqueta, patrones in VETADO.items():
        for p in patrones:
            m = re.search(p, t_nuevo, re.I)
            if m:
                fallas.append(f"{etiqueta} sobrevivio: '{m.group(0)}'")
                break

    # El largo se mide CONTRA EL ORIGINAL, no contra la vara de la extraccion.
    # Estos nodos ya existen y muchos tienen 55-75 palabras; exigirles 80 en una
    # reescritura de VOZ los empuja a rellenar, que es presion de invencion
    # justo donde se prohibe inventar. Se admite +/-35% y nunca mas de 150.
    pal = len((nuevo.get("resumen_teorico") or "").split())
    pal_viejo = len((viejo.get("resumen_teorico") or "").split())
    piso, techo = max(45, int(pal_viejo * 0.65)), min(PALABRAS[1], int(pal_viejo * 1.35) + 10)
    if not (piso <= pal <= techo):
        fallas.append(f"resumen de {pal} palabras (el original tenia {pal_viejo}; "
                      f"se admite {piso}-{techo})")
    if any(g in t_nuevo for g in ("—", "–")):
        fallas.append("guion largo")

    minus = t_nuevo.lower().split()
    sin = sorted({w for w in SIN_TILDE if w in minus})
    if sin:
        fallas.append(f"palabras sin tilde: {sin}")

    for campo in ("pasos_accionables", "condiciones_activacion"):
        if not nuevo.get(campo):
            fallas.append(f"{campo} vacio")
    if not (nuevo.get("entregable_esperado") or "").strip():
        fallas.append("entregable vacio")
    return fallas


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lote", required=True)
    ap.add_argument("--extra", nargs="*", default=[], help="node_id sueltos a incluir")
    ap.add_argument("--tanda", type=int, default=POR_TANDA)
    ap.add_argument("--saltar", help="json con una lista de node_id a NO tocar")
    # La re-voz normal se ancla al nodo y no sabe QUE hay que arreglar: en un
    # lote de 36 eso basta, porque la baranda dice donde duele y el modelo lo
    # ve. En una micro re-voz adjudicada NO basta: `criterio_bazooka_peashooter`
    # salio de la primera pasada con "el equipo de consultores y abogados"
    # intacto, porque nadie le dijo que lo que moria era la ESCALA. La
    # instruccion viaja como ORDEN del editor, no como material: sigue prohibido
    # inventar, y lo que se pide es quitar, no agregar.
    ap.add_argument("--instruccion", help="orden extra del editor para esta corrida "
                                          "(adjudicaciones puntuales). ESCRIBELA CON "
                                          "TILDES: el modelo imita el estilo de lo que "
                                          "recibe, y una orden en ASCII sale en ASCII")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    lote = json.loads(Path(args.lote).read_text(encoding="utf-8"))
    ids = list(lote["sobrevivientes"]) + list(args.extra)
    hechos_path = Path(args.lote).parent / "_revoz_hechos.json"
    hechos = json.loads(hechos_path.read_text(encoding="utf-8")) if hechos_path.exists() else {}
    # SKIP-LIST: nodos que pueden evaporarse en una fusion pendiente. Gastar API
    # en re-vozarlos seria pagar por texto que va a desaparecer. Fusion primero,
    # voz despues: la misma aritmetica de la campana, aplicada a escala micro.
    saltar = set()
    if args.saltar:
        crudo = json.loads(Path(args.saltar).read_text(encoding="utf-8"))
        saltar = set(crudo if isinstance(crudo, list) else
                     [x["node_id"] for x in crudo.get("familia", [])])
        print(f"  skip-list: {len(saltar)} nodos fuera de esta campana")
    pendientes = [n for n in ids if n not in hechos and n not in saltar]
    print(f"  {len(ids)} en el lote, {len(pendientes)} pendientes, tanda de {args.tanda}")
    if args.dry_run:
        return

    from dotenv import load_dotenv
    import anthropic
    load_dotenv(BASE / ".env")
    cli = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    uso = {"in": 0, "out": 0}
    ok, rechazos, muestra, titulos_cambiados = 0, [], [], []

    for nid in pendientes[:args.tanda]:
        ruta = NODOS / f"{nid}.json"
        if not ruta.exists():
            rechazos.append({"node_id": nid, "motivo": "no existe en dataset/nodos"})
            continue
        viejo = json.loads(ruta.read_text(encoding="utf-8"))
        prompt = json.dumps({k: viejo.get(k) for k in (
            "titulo_concepto", "resumen_teorico", "pasos_accionables",
            "entregable_esperado", "condiciones_activacion")}, ensure_ascii=False, indent=2)
        if args.instruccion:
            prompt = (f"ORDEN DEL EDITOR PARA ESTE NODO (manda sobre lo demas, "
                      f"pero NO autoriza a inventar):\n{args.instruccion}\n\n" + prompt)
        nuevo, err = llamar(cli, prompt, uso)
        if err or not isinstance(nuevo, dict):
            rechazos.append({"node_id": nid, "motivo": err or "respuesta no es objeto"})
            continue
        # La ortografia se corrige a maquina ANTES de juzgar (ver TILDES).
        for k in ("titulo_concepto", "resumen_teorico", "pasos_accionables",
                  "entregable_esperado", "condiciones_activacion"):
            if k in nuevo:
                nuevo[k] = corregir_tildes(nuevo[k])
        fallas = revisar(nuevo, viejo)
        if fallas:
            # REPESCA de una vuelta: se le dice al modelo QUE fallo y se le pide
            # solo eso. Perder un nodo bueno por un "la gerencia" que se le
            # escapo es pagar la API dos veces por un descuido de forma.
            detalle = "; ".join(fallas)
            nuevo2, err2 = llamar(cli, prompt + (
                f"\n\nTU VERSION ANTERIOR SE RECHAZO POR: {detalle}. "
                "Corrige EXACTAMENTE eso y nada mas. No agregues contenido."), uso)
            if isinstance(nuevo2, dict):
                for k in ("titulo_concepto", "resumen_teorico", "pasos_accionables",
                          "entregable_esperado", "condiciones_activacion"):
                    if k in nuevo2:
                        nuevo2[k] = corregir_tildes(nuevo2[k])
                fallas2 = revisar(nuevo2, viejo)
                if not fallas2:
                    nuevo, fallas = nuevo2, []
                else:
                    fallas = fallas2
        if fallas:
            rechazos.append({"node_id": nid, "motivo": fallas})
            continue

        if nuevo["titulo_concepto"] != viejo["titulo_concepto"]:
            titulos_cambiados.append({"node_id": nid, "de": viejo["titulo_concepto"],
                                      "a": nuevo["titulo_concepto"]})
        antes = {k: viejo.get(k) for k in ("titulo_concepto", "resumen_teorico")}
        for k in ("titulo_concepto", "resumen_teorico", "pasos_accionables",
                  "entregable_esperado", "condiciones_activacion"):
            viejo[k] = nuevo[k]
        ruta.write_text(json.dumps(viejo, ensure_ascii=False, indent=2), encoding="utf-8")
        hechos[nid] = True
        # SE PERSISTE EN CADA NODO, no al final. Un lote de 52 no cabe en una
        # ventana de 10 minutos, y cuando el primero se corto por tiempo el
        # registro no se habia escrito: los nodos SI estaban en disco, pero la
        # cuenta de lo ya pagado se habia perdido y re-correr habria pagado la
        # API dos veces por el mismo trabajo. Es la misma averia que dejo el lote
        # de ejecucion a medias en la fusion. Escribir 52 veces un JSON de 52
        # claves no cuesta nada; volver a pagar 52 llamadas si.
        hechos_path.write_text(json.dumps(hechos, ensure_ascii=False, indent=2), encoding="utf-8")
        ok += 1
        if len(muestra) < 5:
            muestra.append({"node_id": nid, "antes": antes,
                            "despues": {"titulo_concepto": nuevo["titulo_concepto"],
                                        "resumen_teorico": nuevo["resumen_teorico"]}})
        print(f"  [{ok}] {nid}")

    hechos_path.write_text(json.dumps(hechos, ensure_ascii=False, indent=2), encoding="utf-8")
    informe = Path(args.lote).parent / "_revoz_ultima_tanda.json"
    informe.write_text(json.dumps({
        "regenerados": ok, "rechazos": rechazos, "muestra": muestra,
        "titulos_cambiados": titulos_cambiados,
        "costo_usd": round(uso["in"] / 1e6 * PRECIO_IN + uso["out"] / 1e6 * PRECIO_OUT, 2),
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n  Regenerados {ok}. Rechazados {len(rechazos)}. "
          f"Titulos cambiados {len(titulos_cambiados)}.")
    costo = uso["in"] / 1e6 * PRECIO_IN + uso["out"] / 1e6 * PRECIO_OUT
    libro_mayor.anotar(libro_mayor.pack_del_lote(args.lote), "re-voz", costo,
                       nodos=ok, lote=Path(args.lote).name, tokens=uso)
    print(f"  Costo de la tanda: ${costo:.2f}")
    print(f"  Hechos en total: {len(hechos)}/{len(ids)}")
    if titulos_cambiados:
        print("  OJO: hay titulos cambiados; sus aristas entrantes se re-verifican al cierre.")


if __name__ == "__main__":
    main()
