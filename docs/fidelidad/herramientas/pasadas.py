# -*- coding: utf-8 -*-
"""Las dos pasadas del piloto sobre Reason, a ciegas.

PASADA 1 (Opus 5.5, filtro de ALTO RECALL): lotes de LOTE1 items barajados
con ids opacos; cada item lleva su nodo, su paso y los K fragmentos del
metodo de busqueda elegido. Marca todo lo que PODRIA ser contrario.
PASADA 2 (Opus 5.5, a fondo, --effort high): un item por llamada, solo los
marcados, con el nodo completo, los capitulos enteros donde caen sus mejores
fragmentos y el resto de fragmentos recuperados. Decide FIEL, INFERIDO o
CONTRARIO con cita de linea.

Ningun prompt sabe que hay sinteticos. uso:
  python pasadas.py p1 <intento>   |   python pasadas.py p2 <intento>
"""
import json, os, sys, collections
from concurrent.futures import ThreadPoolExecutor
import comun as C
import busqueda as B

METODO, K = "D", 20
LOTE1 = 4

LIBRO_REF = "James Reason, \"Managing the Risks of Organizational Accidents\" (1997)"

DEFINICIONES = """Definiciones:
- CONTRARIO: el paso aconseja lo que el libro desaconseja o contradice. Incluye: invertir una recomendacion del
  libro; mandar como via principal por un camino que el libro presenta como dificil, poco prometedor, ineficaz o
  contraproducente; invertir una prioridad, un orden o una causalidad que el libro afirma; convertir en regla
  general algo que el libro limita o condiciona; quitar una condicion esencial, de modo que seguir el paso lleve a
  hacer lo que el libro desaconseja.
- FIEL: el libro dice lo que el paso aconseja.
- INFERIDO: el libro no lo dice literalmente, pero es una extension razonable en su misma direccion y no choca
  con nada de lo que el libro dice."""

SIS1 = (f"Eres el FILTRO de alto recall de una auditoria de fidelidad. Un catalogo en espanol da a sus clientes pasos "
        f"accionables extraidos de {LIBRO_REF}. Regla de la casa: nunca le decimos a un cliente lo contrario de lo que "
        "dice su fuente. Otra pasada, mas lenta, revisara a fondo SOLO lo que marques; lo que no marques no se vuelve a "
        "mirar. Por eso, ante la duda, marca. Respondes SOLO con JSON valido.")

SIS2 = (f"Eres el auditor final de fidelidad de un catalogo en espanol cuyos pasos accionables se extrajeron de "
        f"{LIBRO_REF}. Regla de la casa: nunca le decimos a un cliente lo contrario de lo que dice su fuente. Juzgas "
        "con el texto del libro delante, con precision: ni dejas pasar un contrario ni llamas contrario a un paso que "
        "el libro respalda o del que solo se aparta en el detalle. Respondes SOLO con JSON valido.")

INSTR1 = """Para cada item, lee el paso como lo leeria un cliente que lo va a ejecutar, y contrastalo con los
fragmentos del libro (cada linea empieza con su numero Lnnn). Clasifica:
- POSIBLE_CONTRARIO: hay cualquier indicio de choque con algun fragmento, aunque sea parcial o de matiz.
- SIN_COBERTURA: los fragmentos no tratan el asunto del paso y no puedes descartar que el libro diga otra cosa.
- FIEL o INFERIDO: solo si estas seguro de que no hay choque.
marca = true para POSIBLE_CONTRARIO, para SIN_COBERTURA, y para cualquier FIEL o INFERIDO del que no estes seguro.

Responde SOLO con un array JSON, un objeto por item y en el mismo orden:
[{"id": "...", "clase": "FIEL|INFERIDO|POSIBLE_CONTRARIO|SIN_COBERTURA", "marca": true|false,
  "lineas": [numeros de las lineas del libro en que te apoyas], "razon": "maximo 30 palabras"}]"""

INSTR2 = """Decide el veredicto del PASO A JUZGAR (no de los otros pasos del nodo, que solo son contexto):
FIEL, INFERIDO o CONTRARIO. Busca en todo el contexto del libro lo que dice sobre ese asunto, incluido lo que
matiza, limita o desaconseja. Cita la linea o lineas que deciden el veredicto y copia literalmente el trozo
decisivo (maximo 50 palabras, en el idioma del libro). Si es CONTRARIO, escribe en espanol como deberia decir el
paso para ser fiel al libro (mismo estilo: una frase accionable).

Responde SOLO con un objeto JSON:
{"id": "...", "veredicto": "FIEL|INFERIDO|CONTRARIO", "lineas": [n, ...], "cita": "texto literal del libro",
 "razon": "maximo 60 palabras", "paso_fiel": "solo si CONTRARIO; si no, cadena vacia"}"""

def _datos():
    items = B._items()
    cons = json.load(open(os.path.join(C.PIL, "consultas_traducidas.json"), encoding="utf-8"))
    frags, _ = B.indice()
    fx = {f["id"]: f for f in frags}
    return items, cons, frags, fx

def _frags_item(it, cons, fx):
    ids = B.recuperar_item(it, METODO, K, cons)
    return ids, sorted((fx[i] for i in ids), key=lambda f: f["l_ini"])

def p1(intento):
    items, cons, frags, fx = _datos()
    lotes = [items[i:i + LOTE1] for i in range(0, len(items), LOTE1)]
    def uno(ix_lote):
        ix, lote = ix_lote
        bloques = []
        for it in lote:
            _, fs = _frags_item(it, cons, fx)
            txt = "\n\n".join(f"[cap. {f['cap']}, L{f['l_ini']}-L{f['l_fin']}]\n{f['texto']}" for f in fs)
            bloques.append(f"### ITEM {it['id']}\nNodo: {it['titulo']}\nResumen del nodo: {it['resumen']}\n"
                           f"PASO: {it['paso']}\nFragmentos del libro:\n{txt}")
        prompt = DEFINICIONES + "\n\n" + INSTR1 + "\n\n" + "\n\n".join(bloques)
        esperados = [it["id"] for it in lote]
        for rep in range(3):
            datos, _ = C.llama(f"pasada1_i{intento}", f"lote_{ix:03d}" + (f"_r{rep}" if rep else ""), SIS1, prompt)
            if isinstance(datos, dict): datos = [datos]
            if sorted(d.get("id") for d in datos) == sorted(esperados):
                return datos
        raise RuntimeError(f"lote {ix}: ids no casan")
    out = {}
    with ThreadPoolExecutor(C.MAX_PAR) as ex:
        for datos in ex.map(uno, enumerate(lotes)):
            for d in datos:
                if d.get("clase") in ("POSIBLE_CONTRARIO", "SIN_COBERTURA"):
                    d["marca"] = True
                out[d["id"]] = d
    C.escribe_json(os.path.join(C.PIL, f"pasada1_i{intento}.json"), out)
    n = sum(1 for d in out.values() if d["marca"])
    print("pasada 1:", len(out), "items;", n, "marcados", collections.Counter(d["clase"] for d in out.values()))

def _contexto2(it, cons, frags, fx):
    ids, fs = _frags_item(it, cons, fx)
    # capitulos enteros de los mejores fragmentos (maximo 2): el de mas votos entre los 5 primeros
    votos = collections.Counter(fx[i]["cap"] for i in ids[:5])
    caps = [c for c, _ in votos.most_common(2)]
    partes = []
    for c in sorted(caps):
        cuerpo = "\n".join(f["texto"] for f in frags if f["cap"] == c)
        partes.append(f"=== CAPITULO {c} ENTERO ===\n{cuerpo}")
    resto = [f for f in fs if f["cap"] not in caps]
    if resto:
        partes.append("=== OTROS FRAGMENTOS RECUPERADOS ===\n" + "\n\n".join(
            f"[cap. {f['cap']}, L{f['l_ini']}-L{f['l_fin']}]\n{f['texto']}" for f in resto))
    return "\n\n".join(partes), caps

def p2(intento):
    items, cons, frags, fx = _datos()
    r1 = json.load(open(os.path.join(C.PIL, f"pasada1_i{intento}.json"), encoding="utf-8"))
    marcados = [it for it in items if r1[it["id"]]["marca"]]
    def uno(it):
        ctx, caps = _contexto2(it, cons, frags, fx)
        otros = "\n".join(f"- {p}" for p in it["otros_pasos"])
        prompt = (DEFINICIONES + "\n\n" + INSTR2 + f"\n\n=== NODO ===\nTitulo: {it['titulo']}\nResumen: {it['resumen']}\n"
                  f"Entregable: {it['entregable']}\nOtros pasos del nodo (contexto):\n{otros}\n\n"
                  f"=== PASO A JUZGAR (id {it['id']}) ===\n{it['paso']}\n\n"
                  f"Sospecha del filtro previo (puede estar equivocada): {r1[it['id']].get('clase')}: {r1[it['id']].get('razon','')}\n\n"
                  f"=== CONTEXTO DEL LIBRO (cada linea empieza con Lnnn) ===\n{ctx}")
        datos, _ = C.llama(f"pasada2_i{intento}", it["id"], SIS2, prompt, effort="high")
        if isinstance(datos, list): datos = datos[0]
        datos["id"] = it["id"]; datos["capitulos_enteros"] = caps
        return datos
    out = {}
    with ThreadPoolExecutor(C.MAX_PAR) as ex:
        for d in ex.map(uno, marcados):
            out[d["id"]] = d
    C.escribe_json(os.path.join(C.PIL, f"pasada2_i{intento}.json"), out)
    print("pasada 2:", len(out), "juzgados", collections.Counter(d["veredicto"] for d in out.values()))

if __name__ == "__main__":
    {"p1": p1, "p2": p2}[sys.argv[1]](sys.argv[2])
