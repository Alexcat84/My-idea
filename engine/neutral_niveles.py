# -*- coding: utf-8 -*-
"""SEGURIDAD MAXIMA DE SENTIDO para las neutrales (decision del fundador, corrida final, 8 oct 2026).

Principio: cuanto menos se toca la pregunta, menos puede cambiar su sentido. El generador deja de reescribir
libremente. Tres niveles, en este orden:

  NIVEL 1, BASE TAL CUAL: si la base no supone ningun papel (ni jefe, ni equipo, ni socios, ni plurales que den por
  hecho un grupo) y pasa todas las guardas (sin voseo, sin genero marcado al lector, sin voz de libro, sin guion
  largo), la neutral ES la base, palabra por palabra. Sin llamar a ningun modelo.

  NIVEL 2, EDICION MINIMA: el editor (Haiku 5.5) solo propone reemplazos de fragmentos cortos que contienen el problema
  (el papel supuesto, la conjugacion del voseo, la marca de genero). Se aplican aqui, en el codigo, y pasan TODAS las
  comprobaciones: diferencia palabra por palabra (fuera del fragmento no cambia nada), terminos clave del nodo,
  polaridad (negaciones, limites, cifras, plazos), problema resuelto, las guardas de siempre y un JUEZ INDEPENDIENTE
  de otro modelo (Sonnet 5.5): ¿pregunta exactamente lo mismo, en el mismo sentido? Ante cualquier duda, no.

  NIVEL 3, PLANTILLA SEGURA: si la edicion no supera TODO (dos intentos), la neutral queda vacia con nivel 3 y la app
  usa la plantilla neutral generica que ya existe (web/lib/engine/adaptadorPregunta.ts, plantillaNeutral). Nunca una
  neutral dudosa.

Prueba: engine/test_neutral_niveles.py (clientes falsos, sin API).
"""
import difflib
import json
import re
import unicodedata
from collections import Counter

import build_question_cache as bqc

MODELO_EDITOR = bqc.MODEL  # claude-haiku-5-5
MODELO_JUEZ = "claude-sonnet-5-5"
PARAMETROS_JUEZ = {"thinking": {"type": "between_tools"}}  # Sonnet 5.5 razona por defecto y rechaza "disabled"
PRECIO_JUEZ = {"in": 2.0, "out": 10.0, "read": 0.10, "write": 2.50}  # por millon
INTENTOS = 2
MAX_FRAG_PALABRAS = 6
MAX_NUEVO_PALABRAS = 14

ROLES = r"(jef[ea]s?|equipo\w*|socio\w*|emplead\w*|colaborador\w*|subordinad\w*|gerente\w*|directiv\w*|departamento\w*|junta|cofundador\w*|personal)"
# "tu equipo", "tus socios": dan por hecho que existen, aunque vayan en una frase con "si"; salvo que el propio texto
# los vuelva condicionales justo despues ("tu equipo, si lo tienes").
PAPEL_POSESIVO = re.compile(r"\b(tu|tus)\s+(propi[oa]s?\s+)?" + ROLES + r"\b", re.I)
CONDICIONAL_PEGADO = re.compile(r"^[^.?!]{0,40}?\bsi\s+(l[oa]s?\s+)?(tienes|hay|existe|existen)\b", re.I)
PAPEL_SUELTO = re.compile(r"\b(jef[ea]s?|recursos humanos|emplead\w*|subordinad\w*|gerente\w*|cofundador\w*|personal a tu cargo|"
                          # "el equipo" (singular, con articulo) da por hecho un equipo; "equipos" suele ser maquinaria
                          r"(todo |el resto )?(el|al|del) equipo(?! de (protecci|c[oó]mputo|carga|trabajo pesado))|"
                          r"responsables de equipos?|los departamentos|las [aá]reas de tu empresa|los trabajadores)\b", re.I)
CONDICIONAL = re.compile(r"\b(si|en caso|cuando tengas|alg[uú]n d[ií]a|en alg[uú]n momento)\b", re.I)
GRUPO = re.compile(r"\b(ustedes|vosotr[oa]s|ambos|ambas|entre todos|tu empresa|tu organizaci[oó]n|tu compa[ñn][ií]a|"
                   r"tu plantilla|tu gente|"
                   # papeles implicitos y plurales de grupo (cuarta vuelta, 8 oct 2026): nunca tal cual
                   r"la gente que trabaja|la gente de tu|como organizaci[oó]n|para que todos|"
                   r"todos (sepan|entiendan|est[eé]n|tengan|conozcan)|quien(es)? toma(n)? (las )?decisiones|quien aprueba|"
                   r"(tienen|tengan|tenemos) claro|alguien que trabaja contigo|"
                   r"nosotros|nuestr[oa]s?|tenemos|queremos|sabemos|podemos|"
                   r"(c[oó]mo|qu[eé]) (desarrollan|inventan|deciden|organizan)|van inventando)\b|\b\w+(?:áis|éis)\b", re.I)
VOZ_LIBRO = re.compile(r"\b(el libro|del libro|el autor|la autora|seg[uú]n (el|la) (autor|autora|libro|texto)|"
                       r"como se (explica|ilustra|describe)|el texto)\b", re.I)
EDITABLES = {"papel", "grupo", "personas", "voseo", "genero"}
CIERRE_CONDICIONAL = re.compile(r",\s*si\s+(l[oa]s?\s+)?(tienes|hay|existe|existen)$", re.I)

# Terminos clave: si estan en la base, siguen en la neutral (sin sinonimos: la edicion minima no los toca).
TERMINOS = [
    ("franquic", r"franquic"), ("proveedor", r"proveedor"), ("export", r"export"),
    ("import", r"\bimport(ar|as|a|o|amos|an|aci[oó]n|aciones|ador\w*)\b"), ("aduan", r"aduan"),
    ("socio", r"\bsoci[oa]s?\b"), ("inversionist", r"inversionist|inversor"), ("financiaci", r"financiaci"),
    ("segurid", r"segurid"), ("accident", r"accident"), ("riesg", r"riesg"), ("calidad", r"calidad"),
    ("ambient", r"ambient"), ("residu", r"residu"), ("emisi", r"emisi[oó]n|emisiones"), ("energ", r"energ"),
    ("cumplimiento", r"cumplimiento"), ("legal", r"\blegal(es|mente)?\b"), ("contrato", r"\bcontrato(s)?\b"),
    ("certific", r"certific"), ("patent", r"patent"), ("licenci", r"licenci"), ("cliente", r"\bclientes?\b"),
    ("precio", r"\bprecios?\b"), ("venta", r"\bventas?\b|\bvender\b"), ("marca", r"\bmarcas?\b"),
]
NEGACION = {"no", "sin", "nunca", "solo", "sólo", "solamente", "únicamente", "salvo", "excepto", "ni", "jamás",
            "tampoco", "nadie", "nada", "ningún", "ninguna", "ninguno", "más", "menos"}
CIFRA = {"dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "quince", "veinte",
         "treinta", "cien", "cientos", "mil", "miles", "millón", "millones", "primer", "primero", "primera", "segundo",
         "segunda", "tercer", "tercero", "tercera", "mitad", "doble", "triple"}
PLAZO = re.compile(r"^(d[ií]as?|semanas?|mes(es)?|años?|horas?|minutos?|fechas?|trimestres?|semestres?|lunes|martes|"
                   r"mi[eé]rcoles|jueves|viernes|enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|"
                   r"noviembre|diciembre)$", re.I)


def _palabras(t):
    return re.findall(r"\S+", t or "")


def _frase_de(texto, inicio):
    a = max(texto.rfind(c, 0, inicio) for c in ".?!¿¡") + 1
    fins = [i for i in (texto.find(c, inicio) for c in ".?!") if i >= 0]
    return texto[a:(min(fins) if fins else len(texto))]


def problemas(texto):
    """Los problemas de una pregunta para su neutral: [{clase, fragmento, inicio, fin}]. Lista vacia = ninguno."""
    out = []

    def anota(clase, m):
        out.append({"clase": clase, "fragmento": m.group(0), "inicio": m.start(), "fin": m.end()})

    for m in PAPEL_POSESIVO.finditer(texto):
        if not CONDICIONAL_PEGADO.search(texto[m.end():]):
            anota("papel", m)
    for m in PAPEL_SUELTO.finditer(texto):
        if not any(p["inicio"] <= m.start() < p["fin"] for p in out) and not CONDICIONAL.search(_frase_de(texto, m.start())):
            anota("papel", m)
    for m in GRUPO.finditer(texto):
        anota("grupo", m)
    for m in bqc.PERSONAS.finditer(texto):
        if not bqc.CONDICIONAL_PERSONAS.search(_frase_de(texto, m.start())) and not any(
                p["inicio"] <= m.start() < p["fin"] for p in out):
            anota("personas", m)
    for a, b, w in bqc.voseo_en(texto):
        if w.lower() == "vos":
            # el pronombre va con la palabra de antes: tras preposicion pasa a "ti" ("de vos" -> "de ti"), si no a "tu"
            previa = re.search(r"(\S+)\s+$", texto[:a])
            if previa:
                a = previa.start(1)
        out.append({"clase": "voseo", "fragmento": texto[a:b], "inicio": a, "fin": b})
    for m in bqc.GENERO.finditer(texto):
        anota("genero", m)
    for m in VOZ_LIBRO.finditer(texto):
        anota("voz_de_libro", m)
    for m in re.finditer(r"[—–]", texto):
        anota("guion", m)
    return out


def nivel_1(base):
    """¿La base sirve tal cual como neutral? Sin papeles, sin grupos, sin voseo, sin genero, sin voz de libro."""
    return bool(base and base.strip()) and not problemas(base)


def aplicar_cambios(base, cambios, probs=None, editables=None, max_frag=MAX_FRAG_PALABRAS):
    """Aplica los reemplazos del editor. Devuelve (texto, None) o (None, motivo). Cada fragmento: existe una sola vez,
    es corto y contiene un problema detectado en la base (o uno de `probs`, los que trae el lector de bases)."""
    if not isinstance(cambios, list) or not cambios:
        return None, "sin_cambios"
    probs = problemas(base) if probs is None else probs
    editables = EDITABLES if editables is None else editables
    texto = base
    for c in cambios:
        orig = (c or {}).get("original") if isinstance(c, dict) else None
        nuevo = (c or {}).get("nuevo") if isinstance(c, dict) else None
        if not isinstance(orig, str) or not isinstance(nuevo, str) or not orig:
            return None, "cambio_invalido"
        n = base.count(orig)
        if n == 0:
            return None, "fragmento_inexistente"
        # la misma palabra de voseo repetida ("tenés ... tenés") se cambia en todas sus apariciones
        repetida_voseo = n > 1 and len(_palabras(orig)) == 1 and orig.lower() != "vos" and all(
            any(p["clase"] == "voseo" and p["inicio"] == m.start() for p in probs)
            for m in re.finditer(r"(?<!\w)" + re.escape(orig) + r"(?!\w)", base)) and len(
            re.findall(r"(?<!\w)" + re.escape(orig) + r"(?!\w)", base)) == n
        if n > 1 and not repetida_voseo:
            return None, "fragmento_repetido"
        if len(_palabras(orig)) > max_frag:
            return None, "fragmento_largo"
        ini = base.index(orig)
        if not any(p["clase"] in editables and ini <= p["inicio"] and p["fin"] <= ini + len(orig) for p in probs):
            return None, "fragmento_sin_problema"
        if len(_palabras(nuevo)) > MAX_NUEVO_PALABRAS:
            return None, "reemplazo_largo"
        if repetida_voseo:
            texto = re.sub(r"(?<!\w)" + re.escape(orig) + r"(?!\w)", nuevo, texto)
            continue
        if texto.count(orig) != 1:
            return None, "fragmentos_solapados"
        # el condicional insertado se cierra con su coma si lo que sigue no es puntuacion ("tu equipo, si lo tienes, no")
        pos = texto.index(orig) + len(orig)
        if CIERRE_CONDICIONAL.search(nuevo) and pos < len(texto) and texto[pos] not in ",.;:?!)":
            nuevo = nuevo + ","
        texto = texto.replace(orig, nuevo, 1)
    return texto, None


def _spans_permitidos(base, cambios):
    """Indices de las palabras de la base que caen dentro de algun fragmento permitido."""
    pos, permitidas = [], set()
    for m in re.finditer(r"\S+", base):
        pos.append((m.start(), m.end()))
    for c in cambios:
        for m in re.finditer(re.escape(c["original"]), base):
            ini, fin = m.start(), m.end()
            for i, (a, b) in enumerate(pos):
                if a < fin and b > ini:
                    permitidas.add(i)
    return permitidas


def cambio_fuera(base, neutral, cambios):
    """True si la neutral cambia algo fuera de los fragmentos permitidos (diferencia palabra por palabra)."""
    pb, pn = _palabras(base), _palabras(neutral)
    permitidas = _spans_permitidos(base, cambios)
    for op, i1, i2, _j1, _j2 in difflib.SequenceMatcher(a=pb, b=pn, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        tocadas = set(range(i1, i2)) if i2 > i1 else {i1 - 1, i1}
        if i2 > i1 and not tocadas <= permitidas:
            return True
        if i2 == i1 and not (tocadas & permitidas):
            return True
    return False


def _sin_tildes(t):
    return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn").lower()


def terminos_clave(base, nodo):
    """Los terminos propios del tema que estan en la base: los de la lista y las palabras largas de la etiqueta del nodo."""
    b = base.lower()
    out = [nombre for nombre, rx in TERMINOS if re.search(rx, b)]
    etiqueta = " ".join(str(nodo.get(k) or "") for k in ("etiqueta_arbol", "titulo_concepto")) if nodo else ""
    for w in re.findall(r"[A-Za-zÁÉÍÓÚÑáéíóúñü]+", etiqueta):
        raiz = _sin_tildes(w)[:6]
        if len(w) >= 6 and raiz in _sin_tildes(base) and raiz not in out and not any(raiz.startswith(t[:5]) for t in out):
            out.append(raiz)
    return out


def termino_perdido(base, neutral, nodo):
    """El primer termino clave de la base que no sigue en la neutral, o None."""
    n, ns = neutral.lower(), _sin_tildes(neutral)
    rx = dict(TERMINOS)
    for t in terminos_clave(base, nodo):
        if t in rx:
            if not re.search(rx[t], n):
                return t
        elif t not in ns:
            return t
    return None


def _polar(t):
    c = Counter()
    for w in re.findall(r"[\wáéíóúñü]+", (t or "").lower()):
        if w in NEGACION or w in CIFRA or w.isdigit() or re.search(r"\d", w) or PLAZO.match(w):
            c[w] += 1
    return c


def polaridad_cambiada(base, neutral):
    """True si cambia alguna negacion o limite, cifra, plazo o fecha."""
    return _polar(base) != _polar(neutral)


def comprobar_edicion(base, neutral, cambios, nodo):
    """None si la edicion minima supera las comprobaciones automaticas; si no, el motivo."""
    esperado, err = aplicar_cambios(base, cambios)
    if err:
        return err
    if cambio_fuera(base, neutral, cambios) or neutral != esperado:
        return "cambio_fuera_del_fragmento"
    if termino_perdido(base, neutral, nodo):
        return "termino_clave_perdido"
    if polaridad_cambiada(base, neutral):
        return "polaridad_cambiada"
    if any(p["clase"] in EDITABLES for p in problemas(neutral)):
        return "problema_sin_resolver"
    return bqc.comprobar_neutral(base, neutral)


SYSTEM_EDICION = (
    "PROHIBIDO usar guiones largos o medios. Recibes una PREGUNTA BASE de una entrevista de emprendimiento y la lista "
    "de PROBLEMAS detectados en ella: un papel o una estructura que da por hecho (jefe, equipo, socios, empleados), un "
    "plural que supone un grupo, voseo, o el genero femenino marcado al lector. Tu trabajo es la EDICION MINIMA: cambia "
    "SOLO las palabras exactas de cada problema y deja TODO lo demas identico, letra por letra. Reglas: (1) cada cambio "
    "reemplaza un fragmento corto (seis palabras como maximo) que contiene el problema, copiado EXACTAMENTE como esta "
    "en la base; (2) para un papel supuesto, conserva el termino y vuelvelo condicional ('tu equipo' pasa a 'tu "
    "equipo, si lo tienes'), o nombra a quien lo cumpliria sin suponerlo ('tu jefe' pasa a 'quien decide por encima "
    "de ti, si lo hay'); un plural de grupo pasa a la persona ('ustedes deciden' pasa a 'decides'); (3) el voseo pasa "
    "a tuteo ('tenes' pasa a 'tienes'); el genero, al masculino generico ('tu misma' pasa a 'tu mismo'); (4) no "
    "cambies ningun termino del tema (franquicia, proveedor, exportacion, socio, inversionista, cliente...), ninguna "
    "negacion o limite (no, sin, nunca, solo, salvo, mas, menos), ninguna cifra, plazo ni fecha; no añadas preguntas "
    "ni frases. Responde SOLO un JSON: {\"cambios\": [{\"original\": str, \"nuevo\": str}]}."
)

SYSTEM_JUEZ = (
    "Eres un juez independiente. Recibes una PREGUNTA BASE y su version NEUTRAL, que solo debia quitar o volver "
    "condicional un papel supuesto (jefe, equipo, socios, empleados), un plural de grupo, el voseo o el genero marcado. "
    "Decide si la NEUTRAL pregunta EXACTAMENTE lo mismo que la BASE, en el mismo sentido: el mismo foco, las mismas "
    "opciones, la misma polaridad, los mismos terminos del tema, nada añadido. Ante CUALQUIER duda, responde false. "
    "Responde SOLO un JSON: {\"mismo_sentido\": true o false, \"motivo\": str}."
)


def _texto_de(msg):
    return "".join(b.text for b in msg.content if getattr(b, "type", "") == "text")


def neutral_por_niveles(cli_editor, cli_juez, nid, base, graph, intentos=INTENTOS):
    """La neutral de UNA pregunta por niveles. Devuelve {nivel, texto (None en el 3), motivo, cambios, tokens...}."""
    r = {"nivel": None, "texto": None, "motivo": None, "cambios": None,
         "tokens_in": 0, "tokens_out": 0, "cache_read": 0, "cache_write": 0, "juez_in": 0, "juez_out": 0,
         "juez_read": 0, "juez_write": 0}
    if nivel_1(base):
        return {**r, "nivel": 1, "texto": base}
    probs = problemas(base)
    no_editables = sorted({p["clase"] for p in probs if p["clase"] not in EDITABLES})
    if no_editables:
        return {**r, "nivel": 3, "motivo": "no_editable:" + ",".join(no_editables)}
    nodo = graph.get(nid, {})
    aviso = None
    for _ in range(intentos):
        pedido = {"pregunta_base": base, "problemas": [{"clase": p["clase"], "fragmento": p["fragmento"]} for p in probs],
                  "terminos_que_no_cambian": terminos_clave(base, nodo)}
        if aviso:
            pedido["el_intento_anterior_fallo_por"] = aviso
        msg = cli_editor.messages.create(
            model=MODELO_EDITOR, **bqc.PARAMETROS_MODELO, max_tokens=400,
            system=[{"type": "text", "text": SYSTEM_EDICION, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": json.dumps(pedido, ensure_ascii=False)}])
        r["tokens_in"] += msg.usage.input_tokens
        r["tokens_out"] += msg.usage.output_tokens
        lei, esc = bqc._cache_de(msg.usage)
        r["cache_read"] += lei
        r["cache_write"] += esc
        try:
            cambios = bqc._json_de(_texto_de(msg)).get("cambios")
        except (ValueError, AttributeError):
            aviso = r["motivo"] = "salida_no_json"
            continue
        neutral, err = aplicar_cambios(base, cambios)
        if err:
            aviso = r["motivo"] = err
            continue
        motivo = comprobar_edicion(base, neutral, cambios, nodo)
        if motivo:
            aviso = r["motivo"] = motivo
            continue
        j = cli_juez.messages.create(
            model=MODELO_JUEZ, **PARAMETROS_JUEZ, max_tokens=300,
            system=[{"type": "text", "text": SYSTEM_JUEZ, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": json.dumps({"pregunta_base": base, "neutral": neutral}, ensure_ascii=False)}])
        r["juez_in"] += j.usage.input_tokens
        r["juez_out"] += j.usage.output_tokens
        lei, esc = bqc._cache_de(j.usage)
        r["juez_read"] += lei
        r["juez_write"] += esc
        try:
            veredicto = bqc._json_de(_texto_de(j))
        except ValueError:
            veredicto = {}
        if veredicto.get("mismo_sentido") is True:
            return {**r, "nivel": 2, "texto": neutral, "motivo": None, "cambios": cambios}
        aviso = r["motivo"] = "juez_independiente"
    return {**r, "nivel": 3, "texto": None}


def costo_usd(t):
    """El coste real de una corrida: el editor a precio de Haiku 5.5 y el juez a precio de Sonnet 5.5."""
    editor = bqc.costo_usd({"tokens_in": t["tokens_in"], "tokens_out": t["tokens_out"],
                            "cache_read": t["cache_read"], "cache_write": t["cache_write"]})
    juez = (t["juez_in"] * PRECIO_JUEZ["in"] + t["juez_out"] * PRECIO_JUEZ["out"] + t["juez_read"] * PRECIO_JUEZ["read"]
            + t["juez_write"] * PRECIO_JUEZ["write"]) / 1_000_000
    return editor + juez


def correr_niveles(cli_editor, cli_juez, cache, graph, origen="pregunta", destino="pregunta_neutral", guardar=None,
                   rehacer=False, limite=None):
    """Pone la neutral por niveles a cada `origen` vivo. Guarda `destino` (sin el, en el nivel 3) y `destino`_nivel.
    Reanudable: sin `rehacer`, solo trabaja las que aun no tienen nivel."""
    campo_nivel = destino + "_nivel"
    trabajo = [nid for nid, e in cache.items()
               if e.get(origen) and nid in graph and not graph[nid].get("deprecado") and (rehacer or campo_nivel not in e)]
    if limite is not None:
        trabajo = trabajo[:limite]
    tot = Counter()
    niveles, motivos3 = Counter(), Counter()
    for i, nid in enumerate(trabajo, 1):
        base = cache[nid][origen]
        res = neutral_por_niveles(cli_editor, cli_juez, nid, base, graph)
        for k in ("tokens_in", "tokens_out", "cache_read", "cache_write", "juez_in", "juez_out", "juez_read", "juez_write"):
            tot[k] += res[k]
        e = {k: v for k, v in cache[nid].items() if k != destino}
        if res["texto"] is not None:
            e[destino] = res["texto"]
        e[campo_nivel] = res["nivel"]
        cache[nid] = e
        assert cache[nid][origen] == base  # el origen queda intacto
        niveles[res["nivel"]] += 1
        if res["nivel"] == 3:
            motivos3[res["motivo"]] += 1
        if guardar and i % 50 == 0:
            guardar(cache)
    if guardar:
        guardar(cache)
    return {"niveles": dict(niveles), "motivos_nivel_3": dict(motivos3), "tokens": dict(tot), "costo": costo_usd(tot),
            "trabajadas": len(trabajo)}


# --- CORRECCION DECLARADA DE BASES (decision del fundador, cuarta vuelta, 8 oct 2026) ---------------------------------
# El voseo, el ingles y las formas rotas son defectos que se corrigen tambien en las preguntas base (REGLAS C34), por
# correccion declarada y con la misma maquina de edicion minima: solo las palabras exactas del problema, comprobaciones
# automaticas y juez independiente. Si algo duda, la base NO se toca y queda reportada.
CLASES_DE_BASE = {"voseo", "forma_rota", "ingles"}

SYSTEM_CORRECCION = (
    "PROHIBIDO usar guiones largos o medios. Recibes una PREGUNTA BASE de una entrevista de emprendimiento y los "
    "PROBLEMAS de lengua detectados en ella, cada uno con su fragmento exacto: voseo (pasa a tuteo neutro: 'tenes' "
    "pasa a 'tienes', 'sentis' a 'sientes', 'contas' a 'cuentas'), una palabra o frase en ingles (pasa a su "
    "equivalente en espanol neutro) o una forma rota (concordancia, persona o regimen equivocados; se arregla con el "
    "minimo de palabras). Tu trabajo es la EDICION MINIMA: cada cambio reemplaza EXACTAMENTE el fragmento del problema, "
    "copiado tal como esta en la base, y nada mas; todo lo demas queda identico, letra por letra. No cambies terminos "
    "del tema, negaciones, limites, cifras, plazos ni fechas. Responde SOLO un JSON: "
    "{\"cambios\": [{\"original\": str, \"nuevo\": str}]}."
)

SYSTEM_JUEZ_CORRECCION = (
    "Eres un juez independiente. Recibes una PREGUNTA BASE y su version CORREGIDA, que solo debia pasar el voseo a "
    "tuteo, traducir una palabra en ingles o arreglar una forma rota. Decide si la CORREGIDA pregunta EXACTAMENTE lo "
    "mismo que la BASE, en el mismo sentido, y si los cambios hechos son correctos en espanol neutro. Juzga SOLO los cambios "
    "hechos: no rechaces porque quede otra palabra sin tocar, que no se pidio corregir. Ante CUALQUIER duda, "
    "responde false. Responde SOLO un JSON: {\"mismo_sentido\": true o false, \"motivo\": str}."
)


def corregir_base(cli_editor, cli_juez, nid, base, graph, extras, intentos=INTENTOS, max_frag=MAX_FRAG_PALABRAS):
    """La correccion declarada de UNA base. `extras`: los problemas que trae el lector ({clase, fragmento}). Devuelve
    {corregida (None si no se toca), clases, cambios, motivo, tokens...}."""
    r = {"corregida": None, "clases": [], "cambios": None, "motivo": None, "tokens_in": 0, "tokens_out": 0,
         "cache_read": 0, "cache_write": 0, "juez_in": 0, "juez_out": 0, "juez_read": 0, "juez_write": 0}
    probs = [p for p in problemas(base) if p["clase"] in CLASES_DE_BASE]
    for e in extras or []:
        frag = (e or {}).get("fragmento") or ""
        if frag and base.count(frag) == 1 and e.get("clase") in CLASES_DE_BASE:
            ini = base.index(frag)
            probs.append({"clase": e["clase"], "fragmento": frag, "inicio": ini, "fin": ini + len(frag)})
    if not probs:
        return {**r, "motivo": "sin_problemas_de_base"}
    nodo = graph.get(nid, {})
    fragmentos = {p["fragmento"] for p in probs}
    aviso = None
    for _ in range(intentos):
        pedido = {"pregunta_base": base, "problemas": [{"clase": p["clase"], "fragmento": p["fragmento"]} for p in probs]}
        if aviso:
            pedido["el_intento_anterior_fallo_por"] = aviso
        msg = cli_editor.messages.create(
            model=MODELO_EDITOR, **bqc.PARAMETROS_MODELO, max_tokens=400,
            system=[{"type": "text", "text": SYSTEM_CORRECCION, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": json.dumps(pedido, ensure_ascii=False)}])
        r["tokens_in"] += msg.usage.input_tokens
        r["tokens_out"] += msg.usage.output_tokens
        lei, esc = bqc._cache_de(msg.usage)
        r["cache_read"] += lei
        r["cache_write"] += esc
        try:
            cambios = bqc._json_de(_texto_de(msg)).get("cambios")
        except (ValueError, AttributeError):
            aviso = r["motivo"] = "salida_no_json"
            continue
        if not isinstance(cambios, list) or not cambios or any(
                not isinstance(c, dict) or c.get("original") not in fragmentos for c in cambios):
            aviso = r["motivo"] = "fragmento_mas_que_el_problema"
            continue
        corregida, err = aplicar_cambios(base, cambios, probs=probs, editables=CLASES_DE_BASE, max_frag=max_frag)
        if err:
            aviso = r["motivo"] = err
            continue
        if cambio_fuera(base, corregida, cambios):
            aviso = r["motivo"] = "cambio_fuera_del_fragmento"
            continue
        if termino_perdido(base, corregida, nodo):
            aviso = r["motivo"] = "termino_clave_perdido"
            continue
        if polaridad_cambiada(base, corregida):
            aviso = r["motivo"] = "polaridad_cambiada"
            continue
        if bqc.voseo_en(corregida) or re.search(r"[—–]", corregida):
            aviso = r["motivo"] = "problema_sin_resolver"
            continue
        j = cli_juez.messages.create(
            model=MODELO_JUEZ, **PARAMETROS_JUEZ, max_tokens=300,
            system=[{"type": "text", "text": SYSTEM_JUEZ_CORRECCION, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": json.dumps({"pregunta_base": base, "corregida": corregida}, ensure_ascii=False)}])
        r["juez_in"] += j.usage.input_tokens
        r["juez_out"] += j.usage.output_tokens
        lei, esc = bqc._cache_de(j.usage)
        r["juez_read"] += lei
        r["juez_write"] += esc
        try:
            veredicto = bqc._json_de(_texto_de(j))
        except ValueError:
            veredicto = {}
        if veredicto.get("mismo_sentido") is True:
            return {**r, "corregida": corregida, "clases": sorted({p["clase"] for p in probs}), "cambios": cambios,
                    "motivo": None}
        aviso = r["motivo"] = "juez_independiente"
    return r
