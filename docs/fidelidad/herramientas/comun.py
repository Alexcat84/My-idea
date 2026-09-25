# -*- coding: utf-8 -*-
"""Piezas comunes del piloto de fidelidad: rutas, saneado de rayas,
troceado del libro, BM25 propio y la llamada a `claude -p` con su coste.

Regla de estilo de la casa: nada de lo que se escribe lleva raya (U+2014)
ni guion medio (U+2013). El texto del libro se sanea a `--` al trocearlo, de
modo que ni los prompts ni las citas devueltas las traen.
"""
import json, os, re, subprocess, time, unicodedata, math, collections, threading

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
FID = os.path.join(REPO, "docs", "fidelidad")
PIL = os.path.join(FID, "piloto_reason")
PRU = os.path.join(FID, "pruebas")
# Trabajo intermedio que NO se commitea (contiene el texto del libro).
WORK = r"C:\Users\AlexDesk\AppData\Local\Temp\fidel_run"
LIBRO = r"C:\Users\AlexDesk\Documents\I have an idea\books\Especificos\Health and Safety\Managing the Risks of Organizat - Reason, J. T_.txt"
FUENTE = "Managing the Risks of Organizat - Reason, J. T_"
CLAUDE = r"C:\Users\AlexDesk\AppData\Roaming\npm\node_modules\@anthropic-ai\claude-code\bin\claude.exe"
MODELO = "claude-opus-5-5"   # mandato del fundador: todo con Opus 5.5
MAX_PAR = 4                  # nunca mas de 4 procesos claude -p a la vez
# Intento activo de la prueba a ciegas (cada intento tiene su mezcla y su clave).
INTENTO = os.environ.get("FIDEL_INTENTO", "2")

os.makedirs(WORK, exist_ok=True)

def sanea(s):
    if isinstance(s, str):
        return s.replace("\u2014", "--").replace("\u2013", "--")
    if isinstance(s, list):
        return [sanea(x) for x in s]
    if isinstance(s, dict):
        return {k: sanea(v) for k, v in s.items()}
    return s

def escribe_jsonl(ruta, filas):
    with open(ruta, "w", encoding="utf-8") as f:
        for r in filas:
            f.write(json.dumps(sanea(r), ensure_ascii=False) + "\n")

def lee_jsonl(ruta):
    with open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]

def escribe_json(ruta, obj):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(sanea(obj), f, ensure_ascii=False, indent=1)

def grafo():
    g = json.load(open(os.path.join(REPO, "web", "lib", "assets", "master_graph.json"), encoding="utf-8"))["nodos"]
    return g

def nodos_reason():
    g = grafo()
    return {k: v for k, v in sorted(g.items()) if not v.get("deprecado") and v.get("fuente") == FUENTE}

# ── TROCEADO ────────────────────────────────────────────────────────────────

def lineas_libro():
    return sanea(open(LIBRO, encoding="utf-8").read()).split("\n")

def capitulos(L):
    """Inicio (linea, 1-indexada) de cada capitulo: un numero solo, tras tres
    lineas en blanco, seguido de un titulo corto que no es una nota."""
    exp, caps = 1, []
    for i, l in enumerate(L):
        if l.strip() == str(exp) and i >= 3 and all(not L[i - k].strip() for k in (1, 2, 3)):
            j = i + 1
            while j < len(L) and not L[j].strip():
                j += 1
            nxt = L[j].strip()
            if len(nxt) < 80 and not nxt[:1].isdigit() and not any(x in nxt for x in ("Ibid", "op. cit", "pp.", "p. ")):
                caps.append((exp, i + 1, nxt)); exp += 1
    return caps

def trocear(min_pal=120, max_pal=320):
    L = lineas_libro()
    caps = capitulos(L)
    def cap_de(n):
        c = 0
        for num, ini, _ in caps:
            if n >= ini: c = num
        return c
    frags, cur = [], []
    en_notas = False
    def cierra():
        if not cur: return
        texto = "\n".join(f"L{n}: {t}" for n, t in cur)
        frags.append({"id": f"F{len(frags):04d}", "cap": cap_de(cur[0][0]), "l_ini": cur[0][0],
                      "l_fin": cur[-1][0], "notas": en_notas, "texto": texto,
                      "palabras": sum(len(t.split()) for _, t in cur)})
        cur.clear()
    ini_caps = {ini for _, ini, _ in caps}
    for i, l in enumerate(L):
        n = i + 1
        t = l.strip()
        if n in ini_caps:
            cierra(); en_notas = False
        if not t:
            continue
        if t in ("Notes", "References", "Index", "Bibliography"):
            cierra(); en_notas = True
            continue
        pal = sum(len(x.split()) for _, x in cur)
        if cur and pal + len(t.split()) > max_pal and pal >= min_pal // 2:
            cierra()
        cur.append((n, t))
        if sum(len(x.split()) for _, x in cur) >= min_pal and len(t) > 80:
            cierra()
    cierra()
    return frags, caps

# ── BM25 PROPIO ─────────────────────────────────────────────────────────────

STOP = set("""a an the and or of to in on for with by from as at is are was were be been being this that these those it its
which who whom what when where why how not no nor but if then than so such can could may might must should would will shall
do does did done have has had having into about over under more most other some any each all both only own same very also
there their they them we our you your he she his her one two three el la los las un una unos unas y o de del al en con por
para que se su sus es son como lo le les ya mas pero sin sobre entre cada este esta estos estas ese esa esos esas tu tus""".split())

def _sin_acentos(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

def _raiz(w):
    for suf in ("ational", "ations", "ation", "ments", "ment", "ness", "ities", "ity", "ings", "ing", "ions", "ion",
                "edly", "ies", "ied", "ly", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            w = w[: -len(suf)]; break
    return w[:7]

def tokens(s):
    s = _sin_acentos(s.lower())
    return [_raiz(w) for w in re.findall(r"[a-z]+", s) if len(w) >= 3 and w not in STOP]

class BM25:
    def __init__(self, docs, k1=1.2, b=0.75):
        self.docs = [collections.Counter(tokens(d)) for d in docs]
        self.len = [sum(c.values()) for c in self.docs]
        self.avg = sum(self.len) / max(1, len(self.len))
        df = collections.Counter()
        for c in self.docs: df.update(c.keys())
        N = len(self.docs)
        self.idf = {t: math.log(1 + (N - n + 0.5) / (n + 0.5)) for t, n in df.items()}
        self.k1, self.b = k1, b
    def puntua(self, consulta):
        q = tokens(consulta)
        out = []
        for i, c in enumerate(self.docs):
            s = 0.0
            for t in q:
                f = c.get(t)
                if f:
                    s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * self.len[i] / self.avg))
            out.append(s)
        return out
    def ranking(self, consulta):
        s = self.puntua(consulta)
        return sorted(range(len(s)), key=lambda i: -s[i]), s

def rrf(rankings, pesos=None, k=60):
    pesos = pesos or [1.0] * len(rankings)
    acc = collections.defaultdict(float)
    for r, w in zip(rankings, pesos):
        for pos, d in enumerate(r[:200]):
            acc[d] += w / (k + pos + 1)
    return sorted(acc, key=lambda d: -acc[d])

# ── LLAMADA A CLAUDE -P ─────────────────────────────────────────────────────

_lock = threading.Lock()
# Desde la pasada 1: sin cache de prompt (cada prompt se usa una vez; escribir
# cache cuesta el doble) y sin el trafico auxiliar del CLI, que llamaba a un
# modelo pequeno por su cuenta. Asi TODO el coste de las pasadas es Opus 5.5.
# (Generacion de sinteticos, traduccion de consultas y oro corrieron antes de
# este ajuste: su registro de costes muestra esa llamada auxiliar, que no
# decidio nada.)
ENV = dict(os.environ, DISABLE_PROMPT_CACHING="1", CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1")
LOG_COSTES = os.path.join(PIL, "COSTES_LLAMADAS.jsonl")

def extrae_json(texto):
    t = texto.strip()
    m = re.search(r"```(?:json)?\s*(.*?)```", t, re.S)
    if m: t = m.group(1).strip()
    for a, b in (("[", "]"), ("{", "}")):
        i, j = t.find(a), t.rfind(b)
        if i != -1 and j > i:
            try:
                return json.loads(t[i:j + 1])
            except Exception:
                pass
    return json.loads(t)

def llama(etapa, clave, sistema, prompt, effort=None, max_turns=1, reintentos=2, timeout=1500):
    """Una llamada no interactiva a claude -p con Opus 5.5, sin herramientas.
    Devuelve (json_parseado, registro_de_coste). Guarda la respuesta cruda
    saneada en docs/fidelidad/piloto_reason/crudo/<etapa>/<clave>.json."""
    carpeta = os.path.join(PIL, "crudo", etapa)
    os.makedirs(carpeta, exist_ok=True)
    ruta = os.path.join(carpeta, f"{clave}.json")
    if os.path.exists(ruta):
        d = json.load(open(ruta, encoding="utf-8"))
        if d.get("parseado") is not None:
            return d["parseado"], d["coste"]
    cmd = [CLAUDE, "-p", "--model", MODELO, "--output-format", "json", "--tools", "",
           "--system-prompt", sistema, "--strict-mcp-config", "--no-session-persistence",
           "--max-turns", str(max_turns)]
    if effort:
        cmd += ["--effort", effort]
    ultimo = None
    for intento in range(reintentos + 1):
        t0 = time.time()
        p = subprocess.run(cmd, input=prompt.encode("utf-8"), capture_output=True, timeout=timeout, cwd=WORK, env=ENV)
        dt = time.time() - t0
        try:
            out = json.loads(p.stdout.decode("utf-8"))
        except Exception:
            ultimo = p.stderr.decode("utf-8", "replace")[:500] + p.stdout.decode("utf-8", "replace")[:500]
            continue
        coste = {"etapa": etapa, "clave": clave, "intento": intento, "usd": out.get("total_cost_usd", 0),
                 "turnos": out.get("num_turns"), "duracion_s": round(out.get("duration_ms", dt * 1000) / 1000, 1),
                 "pared_s": round(dt, 1), "modelos": sorted((out.get("modelUsage") or {}).keys()),
                 "tokens_in": (out.get("usage") or {}).get("input_tokens", 0) + (out.get("usage") or {}).get("cache_creation_input_tokens", 0) + (out.get("usage") or {}).get("cache_read_input_tokens", 0),
                 "tokens_out": (out.get("usage") or {}).get("output_tokens", 0),
                 "error": out.get("is_error")}
        with _lock:
            with open(LOG_COSTES, "a", encoding="utf-8") as f:
                f.write(json.dumps(coste, ensure_ascii=False) + "\n")
        try:
            parseado = extrae_json(out.get("result", ""))
        except Exception as e:
            ultimo = f"no parsea: {e}: {out.get('result','')[:300]}"
            continue
        escribe_json(ruta, {"coste": coste, "resultado": out.get("result", ""), "parseado": parseado})
        return sanea(parseado), coste
    raise RuntimeError(f"{etapa}/{clave}: {ultimo}")
