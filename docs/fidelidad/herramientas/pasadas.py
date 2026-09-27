# -*- coding: utf-8 -*-
"""Las dos pasadas del piloto sobre Reason, a ciegas.

PASADA 1 (Opus 5.5, filtro de ALTO RECALL): lotes de LOTE1 items barajados
con ids opacos; cada item lleva su nodo, su paso y los K fragmentos del
metodo de busqueda elegido. Marca todo lo que PODRIA ser contrario.
PASADA 2 (Opus 5.5, a fondo, --effort high): un item por llamada, solo los
marcados, con el nodo completo, los capitulos enteros donde caen sus mejores
fragmentos y el resto de fragmentos recuperados. Decide FIEL, INFERIDO o
CONTRARIO con cita de linea (intento 1).

Desde el intento 2 (anadido del fundador, 25 sep 2026): la pasada 1 pone dos
marcas (podria contradecir; trae dato concreto) y la pasada 2 decide entre
cuatro veredictos: CONTRARIO, INFERIDO-ANADIDO, INFERIDO-OPERATIVO, FIEL.
El intento lo fija la variable FIDEL_INTENTO y el argumento, que deben casar.

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

# ── INTENTO 2 EN ADELANTE: anadido del fundador (25 sep 2026) ────────────────
# Cuatro veredictos; la pasada 1 lleva dos marcas; todo paso con cualquiera va a la 2.
DEFINICIONES_2 = """Veredictos (definiciones del fundador):
- CONTRARIO: el paso aconseja lo que el libro desaconseja o contradice. Incluye: invertir una recomendacion del
  libro; mandar como via principal por un camino que el libro presenta como dificil, poco prometedor, ineficaz o
  contraproducente; invertir una prioridad, un orden o una causalidad que el libro afirma; convertir en regla
  general algo que el libro limita o condiciona; quitar una condicion esencial, de modo que seguir el paso lleve a
  hacer lo que el libro desaconseja.
- INFERIDO-ANADIDO: afirma algo concreto que el libro no respalda (una cifra, un plazo, una herramienta, un
  responsable, una norma, una frecuencia).
- INFERIDO-OPERATIVO: concreta lo que el libro dice, en su misma direccion, sin datos nuevos.
- FIEL: el libro dice lo que el paso aconseja.
Si un paso cumple varias, manda la primera de esta lista (CONTRARIO antes que INFERIDO-ANADIDO, y este antes que
INFERIDO-OPERATIVO)."""

INSTR1_2 = """Para cada item, lee el paso como lo leeria un cliente que lo va a ejecutar, y contrastalo con los
fragmentos del libro (cada linea empieza con su numero Lnnn). Pon DOS marcas independientes:
- podria_contradecir = true si hay cualquier indicio de choque con algun fragmento, aunque sea parcial o de matiz,
  o si los fragmentos no tratan el asunto del paso y no puedes descartar que el libro diga otra cosa. Ante la duda, true.
- dato_concreto = true si el paso trae CUALQUIER dato concreto: un numero, porcentaje o cifra; un plazo o una
  frecuencia; el nombre de una herramienta, programa, metodo con nombre propio, norma, estandar o ley; o un rol,
  cargo o responsable concreto de hacerlo. Da igual si el libro lo trae o no: la pasada siguiente lo comprueba.
Ademas, una clase provisional: FIEL, INFERIDO-OPERATIVO, INFERIDO-ANADIDO, POSIBLE_CONTRARIO o SIN_COBERTURA.

Responde SOLO con un array JSON, un objeto por item y en el mismo orden:
[{"id": "...", "podria_contradecir": true|false, "dato_concreto": true|false, "datos": ["los datos concretos, literales"],
  "clase": "...", "lineas": [numeros de las lineas del libro en que te apoyas], "razon": "maximo 30 palabras"}]"""

INSTR2_2 = """Decide el veredicto del PASO A JUZGAR (no de los otros pasos del nodo, que solo son contexto):
CONTRARIO, INFERIDO-ANADIDO, INFERIDO-OPERATIVO o FIEL. Busca en todo el contexto del libro lo que dice sobre ese
asunto, incluido lo que matiza, limita o desaconseja. Comprueba cada dato concreto del paso (cifra, plazo,
frecuencia, herramienta, norma, responsable o rol): si el libro no lo respalda, el paso es INFERIDO-ANADIDO (salvo
que ademas sea CONTRARIO). Cita la linea o lineas que deciden el veredicto y copia literalmente el trozo decisivo
(maximo 50 palabras, en el idioma del libro). Si es CONTRARIO o INFERIDO-ANADIDO, escribe en espanol como deberia
decir el paso para ser fiel al libro (mismo estilo: una frase accionable).

Responde SOLO con un objeto JSON:
{"id": "...", "veredicto": "CONTRARIO|INFERIDO-ANADIDO|INFERIDO-OPERATIVO|FIEL", "lineas": [n, ...],
 "cita": "texto literal del libro", "datos_sin_respaldo": ["solo si INFERIDO-ANADIDO"], "razon": "maximo 60 palabras",
 "paso_fiel": "solo si CONTRARIO o INFERIDO-ANADIDO; si no, cadena vacia"}"""

# Ajuste del intento 3 (tras el intento 2: el anadido sintetico A08 salio CONTRARIO,
# con el dato inventado visto en la razon pero no en datos_sin_respaldo, porque la
# instruccion lo pedia "solo si INFERIDO-ANADIDO"). Ahora los datos sin respaldo se
# listan SIEMPRE, y un CONTRARIO que ademas inventa un dato lleva tambien_anadido.
INSTR2_3 = INSTR2_2.replace(
    '"datos_sin_respaldo": ["solo si INFERIDO-ANADIDO"]',
    '"datos_sin_respaldo": ["todo dato concreto del paso que el libro no respalda, sea cual sea el veredicto"], "tambien_anadido": true|false').replace(
    "si el libro no lo respalda, el paso es INFERIDO-ANADIDO (salvo\nque ademas sea CONTRARIO).",
    "si el libro no lo respalda, el paso es INFERIDO-ANADIDO (salvo\nque ademas sea CONTRARIO). Lista SIEMPRE esos datos sin respaldo, aunque el veredicto sea CONTRARIO, y en ese\n"
    "caso pon tambien_anadido = true: el paso se corregira por las dos cosas.")
assert INSTR2_3 != INSTR2_2 and "tambien_anadido = true" in INSTR2_3

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
    cons = json.load(open(os.path.join(C.PIL, f"consultas_traducidas_i{C.INTENTO}.json"), encoding="utf-8"))
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
        defs, instr = (DEFINICIONES, INSTR1) if intento == "1" else (DEFINICIONES_2, INSTR1_2)
        prompt = defs + "\n\n" + instr + "\n\n" + "\n\n".join(bloques)
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
                if intento == "1":
                    if d.get("clase") in ("POSIBLE_CONTRARIO", "SIN_COBERTURA"):
                        d["marca"] = True
                else:
                    d["marca"] = bool(d.get("podria_contradecir") or d.get("dato_concreto")
                                      or d.get("clase") in ("POSIBLE_CONTRARIO", "SIN_COBERTURA", "INFERIDO-ANADIDO"))
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
        a = r1[it["id"]]
        if intento == "1":
            defs, instr, sosp = DEFINICIONES, INSTR2, f"{a.get('clase')}: {a.get('razon','')}"
        else:
            defs, instr = DEFINICIONES_2, (INSTR2_2 if intento == "2" else INSTR2_3)
            sosp = (f"clase {a.get('clase')}; podria_contradecir={a.get('podria_contradecir')}; "
                    f"dato_concreto={a.get('dato_concreto')} {a.get('datos') or ''}; {a.get('razon','')}")
        prompt = (defs + "\n\n" + instr + f"\n\n=== NODO ===\nTitulo: {it['titulo']}\nResumen: {it['resumen']}\n"
                  f"Entregable: {it['entregable']}\nOtros pasos del nodo (contexto):\n{otros}\n\n"
                  f"=== PASO A JUZGAR (id {it['id']}) ===\n{it['paso']}\n\n"
                  f"Sospecha del filtro previo (puede estar equivocada): {sosp}\n\n"
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
    assert sys.argv[2] == C.INTENTO, "FIDEL_INTENTO y el argumento no casan"
    {"p1": p1, "p2": p2}[sys.argv[1]](sys.argv[2])
