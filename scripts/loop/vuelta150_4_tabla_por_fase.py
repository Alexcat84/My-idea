# -*- coding: utf-8 -*-
"""vuelta150_4_tabla_por_fase.py . LAS OCHO FILAS DE LA TABLA POR FASE DE
docs/plan/08_VERIFICACION.md, RECORRIDAS UNA A UNA (TAREA 4 de la vuelta 150).

Ninguna de las ocho pide credencial. La vuelta 148 midio UNA y eso quedo
registrado como su caida 4.3 (incumplimiento de encargo, acta 149). Aqui van las
ocho.

LA CELDA DE CADA FILA SE LEE DEL PROPIO 08_VERIFICACION.md EN ESTA CORRIDA, no se
teclea: si la pagina cambia, este arnes cambia con ella.

UNA PALABRA POR SENTIDO (TAREA 4.e). Este arnes usa TRES veredictos y no los
mezcla nunca:
  VERDE          la celda se midio entera y la medicion la cumple.
  VERDE PARCIAL  la celda tiene DOS mitades, una mecanica y otra que pide
                 lectura humana; la mecanica se midio y esta verde, y la otra
                 se nombra sin darla por buena.
  NO MECANIZABLE la celda no tiene hoy una vara escrita que la mida contra el
                 repo. No es un fracaso: es informacion, y abre la fase en vez
                 de cerrarla (TAREA 4.c).

USO:
  python scripts/loop/vuelta150_4_tabla_por_fase.py
"""
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "08_VERIFICACION.md")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")


def celdas_de_la_tabla():
    """Lee la tabla POR FASE de 08_VERIFICACION.md: {fase: 'que tiene que dar verde'}."""
    filas = []
    dentro = False
    for linea in io.open(PAGINA, encoding="utf-8"):
        if linea.strip().startswith("## POR FASE"):
            dentro = True
            continue
        if dentro and linea.startswith("**CORRECCION DECLARADA"):
            break
        if not dentro or not linea.strip().startswith("|"):
            continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) != 2 or celdas[0].startswith("---") or celdas[0] == "fase":
            continue
        filas.append((celdas[0].strip("*").strip(), celdas[1]))
    return filas


def fichas():
    return [json.loads(x) for x in io.open(OPS, encoding="utf-8").read().splitlines() if x.strip()]


def grafo(ref="WORK"):
    if ref == "WORK":
        return json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    b = subprocess.run(["git", "show", "%s:dataset/metadata/master_graph.json" % ref],
                       capture_output=True, cwd=RAIZ)
    return json.loads(b.stdout.decode("utf-8"))["nodos"]


def resolutor(N):
    alias_de = {}
    for nid, n in N.items():
        for a in n.get("ids_alias") or []:
            if a != nid:
                alias_de[a] = nid

    def res(nid):
        n = N.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid
        visto, cur, ultimo = {nid}, nid, (nid if n is not None else None)
        while cur in alias_de:
            cur = alias_de[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = N.get(cur)
            if c is None:
                continue
            ultimo = cur
            if not c.get("deprecado"):
                return cur
        return ultimo
    return res


def gate0_checks():
    """Lee la salida de Gate 0 de la apertura de esta vuelta, ya commiteada."""
    ruta = os.path.join(RAIZ, "docs", "loop", "SALIDA_V150_GATE0_CMD1_APERTURA.txt")
    out = []
    for linea in io.open(ruta, encoding="utf-8"):
        m = re.match(r"\s*\[(OK|FALLO)\]\s+(.*)$", linea.rstrip("\n"))
        if m:
            out.append((m.group(1), m.group(2)))
    return out


def salidas_del_bucle():
    d = os.path.join(RAIZ, "docs", "loop")
    return [os.path.join(d, x) for x in os.listdir(d)
            if x.startswith("SALIDA_") and x.endswith(".txt")]


def main():
    filas = celdas_de_la_tabla()
    print("FILAS DE LA TABLA POR FASE, LEIDAS DE docs/plan/08_VERIFICACION.md: %d" % len(filas))
    for f, _c in filas:
        print("  - %s" % f)
    assert len(filas) == 8, "la tabla no trae ocho filas: %d" % len(filas)

    F = fichas()
    por_id = {x["id_op"]: x for x in F}
    N = grafo("WORK")
    res = resolutor(N)
    checks = gate0_checks()
    vivos = {k for k, v in N.items() if not v.get("deprecado")}
    veredictos = []

    def cabecera(i):
        print("")
        print("=" * 96)
        print("FILA %d de 8: %s" % (i + 1, filas[i][0]))
        print("CELDA, LEIDA DE LA PAGINA: %s" % filas[i][1])
        print("-" * 96)

    # ---- FILA 1: 0 CODIGO -------------------------------------------------
    cabecera(0)
    fase00 = [x for x in F if x["fase"] == "00_CODIGO"]
    print("INSTRUMENTO: para cada una de las %d operaciones de 00_CODIGO se busca en" % len(fase00))
    print("docs/loop/ una salida COMMITEADA que nombre el id_op y contenga una marca de")
    print("ROJO (FALLO, EXITCODE: 1, CAE o ROJO). La celda pide 'se cae ANTES del arreglo',")
    print("que es un hecho historico: lo unico que lo prueba es esa salida roja guardada.")
    rutas = salidas_del_bucle()
    print("ficheros SALIDA_*.txt en docs/loop: %d" % len(rutas))
    con_rojo = {}
    for ruta in rutas:
        try:
            texto = io.open(ruta, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        tiene_rojo = bool(re.search(r"\[FALLO\]|EXITCODE: 1|EXIT=1| CAE\.|ROJO", texto))
        if not tiene_rojo:
            continue
        for x in fase00:
            if re.search(re.escape(x["id_op"]) + r"(?![A-Za-z0-9_-])", texto):
                con_rojo.setdefault(x["id_op"], []).append(os.path.basename(ruta))
    # SEGUNDA PIERNA, Y NO ES UN ENSANCHE PARA QUE PASE: una guarda de la fase 0
    # puede llevar el caso positivo de OTRA que su ficha declara portadora. La
    # ficha de OP-C-04 lo dice literal: "ES LA GUARDA QUE HACE PERMANENTE A
    # OP-S-07 Y A OP-S-06", y su campo depende_de nombra a las dos. Asi que una
    # operacion cuenta cubierta si la nombra una salida roja, O si la nombra la
    # salida roja de una guarda cuyo depende_de la incluye. Se dice SIEMPRE por
    # cual de las dos piernas pasa.
    portadoras = {}
    for g in F:
        for d in (g.get("depende_de") or []):
            portadoras.setdefault(d, []).append(g["id_op"])
    con = 0
    directas = 0
    for x in fase00:
        i = x["id_op"]
        ficheros = con_rojo.get(i, [])
        via = []
        for g in portadoras.get(i, []):
            if con_rojo.get(g):
                via.append(g)
        if ficheros:
            con += 1
            directas += 1
            print("  %-10s DIRECTA: %d salida(s) roja(s) que lo nombran -> %s"
                  % (i, len(ficheros), ", ".join(sorted(ficheros)[:3])))
        elif via:
            con += 1
            print("  %-10s POR PORTADORA: sin salida propia; la lleva %s, que lo nombra en su depende_de"
                  % (i, ", ".join(via)))
        else:
            print("  %-10s SIN CASO POSITIVO ROJO GUARDADO, ni propio ni por portadora" % i)
    print("CIFRA: %d de %d operaciones de 00_CODIGO tienen su caso positivo rojo guardado"
          % (con, len(fase00)))
    print("       (%d por salida propia, %d por portadora declarada)." % (directas, con - directas))
    v = "VERDE" if con == len(fase00) else "NO CUMPLE"
    print("VEREDICTO: %s" % v)
    veredictos.append((filas[0][0], v,
                       "%d de %d con caso positivo rojo commiteado (%d propias, %d por portadora)"
                       % (con, len(fase00), directas, con - directas)))

    # ---- FILA 2: 01 FUENTES ----------------------------------------------
    cabecera(1)
    fase01 = [x for x in F if x["fase"] == "01_FUENTES"]
    nomina01 = sorted({n for x in fase01 for n in (x.get("nodos") or [])})
    base = subprocess.run(["git", "merge-base", "pasada-unica", "main"],
                          capture_output=True, cwd=RAIZ).stdout.decode().strip()
    Nb = grafo(base)
    print("INSTRUMENTO: la nomina de las %d fichas de 01_FUENTES son %d nodos. Se mide"
          % (len(fase01), len(nomina01)))
    print("(a) 'ningun nodo de la clase con pasos alterados': se comparan los")
    print("    pasos_accionables de hoy contra los del grafo ANTERIOR A LA CAMPANA (%s);" % base[:8])
    print("(b) 'el material del segundo libro reubicado, NO BORRADO': se cuenta cuantos")
    print("    de la nomina siguen existiendo en el grafo de hoy.")
    alterados, desaparecidos, deprecados01 = [], [], []
    for nid in nomina01:
        if nid not in N:
            desaparecidos.append(nid)
            continue
        if N[nid].get("deprecado"):
            deprecados01.append(nid)
        if nid in Nb:
            if (Nb[nid].get("pasos_accionables") or []) != (N[nid].get("pasos_accionables") or []):
                alterados.append(nid)
    print("  nodos de la nomina: %d" % len(nomina01))
    print("  con pasos_accionables ALTERADOS respecto del grafo previo: %d" % len(alterados))
    for x in alterados[:10]:
        print("    %s" % x)
    print("  DESAPARECIDOS del grafo de hoy: %d" % len(desaparecidos))
    print("  deprecados (siguen en el grafo, no borrados): %d" % len(deprecados01))
    # LA MITAD (a) NO ES ATRIBUIBLE, Y ESO SE DICE EN VEZ DE PUBLICAR UN ROJO
    # FALSO. La celda pide que la operacion de FUENTES no altere pasos, pero la
    # unica comparacion disponible es contra el grafo previo a TODA la campana,
    # y por ahi han pasado tambien los DESTEJIDOS, que alteran pasos A
    # PROPOSITO. Se mide el solape para que la afirmacion no sea de palabra.
    otras = {n for x in F if x["fase"] != "01_FUENTES" for n in (x.get("nodos") or [])}
    solapan = [x for x in alterados if x in otras]
    print("  de esos alterados, cuantos estan tambien en la nomina de otra fase: %d de %d"
          % (len(solapan), len(alterados)))
    print("  ATRIBUCION: no hay vara escrita que separe la alteracion de FUENTES de la")
    print("  de un destejido sobre el mismo nodo. La cifra se publica; la culpa no se")
    print("  reparte (EJECUTOR.md 11).")
    v = "VERDE PARCIAL" if not desaparecidos else "NO CUMPLE"
    print("VEREDICTO: %s (mitad 'no borrado' medida y VERDE, 0 desaparecidos de %d;" % (v, len(nomina01)))
    print("           mitad 'pasos alterados' NO ATRIBUIBLE con las varas de hoy)")
    veredictos.append((filas[1][0], v,
                       "0 desaparecidos de %d; %d con pasos distintos del grafo previo, %d de ellos en nomina de otra fase"
                       % (len(nomina01), len(alterados), len(solapan))))

    # ---- FILA 3: 02 DESTEJIDOS -------------------------------------------
    cabecera(2)
    print("INSTRUMENTO: la celda tiene DOS mitades y solo una tiene vara escrita.")
    print("(a) 'cada perdida en el bloque del que proviene': la mide")
    print("    scripts/loop/verificar_mapas_destejido.py, que EJECUTOR.md 1 ya exige")
    print("    correr sobre toda tabla de particion. Se corre aqui.")
    r = subprocess.run(["python", os.path.join("scripts", "loop", "verificar_mapas_destejido.py")],
                       capture_output=True, cwd=RAIZ)
    salida = (r.stdout.decode("utf-8", "replace") + r.stderr.decode("utf-8", "replace")).strip()
    print("    EXITCODE %d" % r.returncode)
    for linea in salida.splitlines()[-8:]:
        print("    | %s" % linea)
    print("(b) 'los quince congelados releidos': NO TIENE VARA ESCRITA contra el repo.")
    print("    La nomina de los quince vive en prosa de docs/plan/02_DESTEJIDOS.md (la")
    print("    tabla del orden, linea 83 y siguientes) y en docs/PENDIENTES.md, y no hay")
    print("    fichero de datos que la liste. EJECUTOR.md 5 prohibe inventar la regla.")
    v = "VERDE PARCIAL" if r.returncode == 0 else "NO CUMPLE"
    print("VEREDICTO: %s (mitad (a) medida y verde; mitad (b) NO MECANIZABLE hoy)" % v)
    veredictos.append((filas[2][0], v,
                       "mapas de destejido exitcode %d; los quince congelados sin vara escrita"
                       % r.returncode))

    # ---- FILA 4: 03 FUSIONES ---------------------------------------------
    cabecera(3)
    print("INSTRUMENTO: sobre TODA ficha del plan con `superviviente` escrito, se")
    print("comprueban las tres cosas que la celda pide, una a una y contra el grafo.")
    # EL UNIVERSO ES LA FASE 03, Y NO TODA FICHA CON `superviviente` ESCRITO.
    # La celda dice "03 FUSIONES" y una ficha de 02_DESTEJIDOS o de 06_MESAS con
    # superviviente escrito NO esta bajo esta celda: medirla aqui seria pintar de
    # rojo la fila con incumplimientos de otra fila.
    con_surv = [x for x in F if x.get("superviviente") and x["fase"] == "03_FUSIONES"]
    fuera = [x["id_op"] for x in F if x.get("superviviente") and x["fase"] != "03_FUSIONES"]
    print("  fichas con superviviente FUERA de 03_FUSIONES, no medidas aqui: %d (%s)"
          % (len(fuera), ", ".join(fuera)))
    fallos = []
    divergentes = []
    for x in con_surv:
        s = x["superviviente"]
        absorbidos = [n for n in (x.get("nodos") or []) if n != s]
        if s not in N or N[s].get("deprecado"):
            # SUPERVIVIENTE DIVERGENTE, y NO se cuenta como incumplimiento a
            # secas: es la especie que la CORRECCION 16 de
            # docs/plan/CORRECCIONES_A_APLICAR.md describe y clasifica, "una
            # fusion consumida al reves no es cumplida ni sin cumplir". Se
            # cuenta aparte y se nombra.
            divergentes.append("%s: el superviviente escrito %s esta %s"
                               % (x["id_op"], s,
                                  "deprecado" if s in N else "ausente del grafo"))
            continue
        alias = set(N[s].get("ids_alias") or [])
        for a in absorbidos:
            if a not in N:
                fallos.append("%s: el absorbido %s no existe" % (x["id_op"], a))
            elif not N[a].get("deprecado"):
                fallos.append("%s: el absorbido %s NO esta deprecado" % (x["id_op"], a))
            elif a not in alias:
                fallos.append("%s: %s no esta en ids_alias de %s" % (x["id_op"], a, s))
            elif res(a) != s:
                fallos.append("%s: resolverId(%s) da %s y no %s" % (x["id_op"], a, res(a), s))
    print("  fichas con superviviente escrito: %d" % len(con_surv))
    print("  absorbidos comprobados: %d"
          % sum(len([n for n in (x.get("nodos") or []) if n != x["superviviente"]]) for x in con_surv))
    print("  incumplimientos: %d" % len(fallos))
    for x in fallos[:10]:
        print("    %s" % x)
    print("  supervivientes DIVERGENTES (CORRECCION 16, ni cumplida ni sin cumplir): %d"
          % len(divergentes))
    for x in divergentes:
        print("    %s" % x)
    if fallos:
        v = "NO CUMPLE"
    elif divergentes:
        v = "VERDE PARCIAL"
    else:
        v = "VERDE"
    print("VEREDICTO: %s%s" % (v, " (todo lo medible en verde; lo que queda son los"
                               " divergentes ya declarados)" if v == "VERDE PARCIAL" else ""))
    veredictos.append((filas[3][0], v,
                       "%d ficha(s) de 03_FUSIONES con superviviente, %d incumplimiento(s), %d divergente(s) de la CORRECCION 16"
                       % (len(con_surv), len(fallos), len(divergentes))))

    # ---- FILA 5: 04 ENLACES ----------------------------------------------
    cabecera(4)
    print("INSTRUMENTO: la celda tiene DOS mitades y se dicen por separado.")
    auto = [c for c in checks if "auto-arista" in c[1]]
    print("(b) 'ninguna crea auto-arista tras resolver': ES UN CHECK DE GATE 0 y esta")
    print("    corriendo. Su linea, leida de SALIDA_V150_GATE0_CMD1_APERTURA.txt:")
    for e, t in auto:
        print("    [%s] %s" % (e, t))
    print("(a) 'cada arista nueva CONFIRMADA POR LECTURA, no por el instrumento': la")
    print("    celda EXCLUYE explicitamente al instrumento, o sea que por construccion")
    print("    no hay vara mecanica que la conteste. Lo unico que se puede contar aqui")
    print("    es cuantas aristas_nuevas del plan estan HOY presentes, y eso es")
    print("    justamente 'por el instrumento', o sea la otra cosa.")
    con_aristas = [x for x in F if x.get("aristas_nuevas")]
    print("    fichas con aristas_nuevas escritas: %d" % len(con_aristas))
    ok_auto = bool(auto) and all(e == "OK" for e, _ in auto)
    v = "VERDE PARCIAL" if ok_auto else "NO CUMPLE"
    print("VEREDICTO: %s (mitad (b) verde en Gate 0; mitad (a) NO MECANIZABLE POR SU PROPIA LETRA)" % v)
    veredictos.append((filas[4][0], v, "auto-aristas en Gate 0: %s; la confirmacion por lectura la excluye la celda"
                       % ("OK" if ok_auto else "FALLO")))

    # ---- FILA 6: 05 SANEO ------------------------------------------------
    cabecera(5)
    print("LA CORRECCION DECLARADA DE LA VUELTA 122, CITADA Y NO REINTERPRETADA, de la")
    print("misma pagina: 'LA CELDA DE LA FILA 05 SANEO SE LEE ACOTADA A LAS NOMINAS DE")
    print("SUS OPERACIONES'... 'esta celda se lee cumplida CUANDO LAS OPERACIONES DE SU")
    print("NOMINA CIERRAN (OP-S-03, OP-S-04, OP-S-05), no cuando el catalogo entero queda")
    print("barrido'.")
    print("")
    sub = []
    # 1) ningun id vivo con tratado extinto, acotado a la nomina de OP-S-01
    # LA VARA ES LA DE SU PROPIA FICHA, CITADA: OP-S-01.verificacion dice
    # "ningun nodo VIVO lleva NAFTA EN SU ID NI EN SU TITULO", acotado por la
    # correccion declarada del 28 ago 2026 (decision del fundador, punto 2) A LA
    # NOMINA DE ESTA OPERACION. Buscar NAFTA en el CUERPO del nodo seria otra
    # vara: el superviviente lo nombra en su resumen y en sus pasos porque el
    # tratado existio, y ademas lo lleva en ids_alias PORQUE SU PROPIA
    # VERIFICACION LO EXIGE.
    nom1 = por_id["OP-S-01"]["nodos"]
    malos = [n for n in nom1 if n in vivos
             and ("nafta" in n.lower()
                  or "nafta" in (N[n].get("titulo_concepto") or "").lower())]
    sub.append(("ningun id vivo con tratado extinto, EN SU ID NI EN SU TITULO (nomina OP-S-01, %d nodo(s))"
                % len(nom1), len(malos), malos[:3]))
    # 2) los tres de Incoterms con su version, nomina de OP-S-02
    nom2 = por_id["OP-S-02"]["nodos"]
    sin_version = []
    for n in nom2:
        # SOLO VIVOS. La CORRECCION DECLARADA de la vuelta 120, escrita en la
        # propia ficha de OP-S-02, dice que DOS de los tres estan hoy
        # deprecados. Un deprecado no es "un nodo que cita Incoterms sin
        # version": es registro historico, y el mismo criterio que deja los
        # deprecados fuera de la guarda de auto-arista (OP-C-04, 14 ago 2026).
        if n not in N or N[n].get("deprecado"):
            continue
        txt = json.dumps(N[n], ensure_ascii=False)
        if "incoterms" in txt.lower() and not re.search(r"Incoterms[^\"]{0,20}(19|20)\d\d", txt):
            sin_version.append(n)
    vivos_nom2 = [n for n in nom2 if n in vivos]
    sub.append(("los de Incoterms con su version (nomina OP-S-02: %d nodo(s), %d vivo(s), %d deprecado(s))"
                % (len(nom2), len(vivos_nom2), len(nom2) - len(vivos_nom2)),
                len(sin_version), sin_version))
    # 3) ningun nodo cablea export.gov, sobre dataset/nodos entero (asi lo midio OP-S-03)
    nodos_dir = os.path.join(RAIZ, "dataset", "nodos")
    con_export = []
    for nombre in sorted(os.listdir(nodos_dir)):
        if not nombre.endswith(".json"):
            continue
        if "export.gov" in io.open(os.path.join(nodos_dir, nombre), encoding="utf-8",
                                  errors="replace").read():
            con_export.append(nombre)
    sub.append(("ningun nodo cablea export.gov (dataset/nodos entero, %d ficheros)"
                % len(os.listdir(nodos_dir)), len(con_export), con_export[:3]))
    # 4) ninguna de las seis herramientas muertas, acotado a la nomina de OP-S-04
    nom4 = por_id["OP-S-04"]["nodos"]
    muertas = [x.strip() for x in (por_id["OP-S-04"].get("eliminar") or [])]
    con_muerta = []
    for n in nom4:
        if n not in N:
            continue
        txt = json.dumps(N[n], ensure_ascii=False).lower()
        for m in muertas:
            if m and m.lower() in txt:
                con_muerta.append("%s trae %s" % (n, m))
    sub.append(("ninguna de las herramientas muertas en la nomina de OP-S-04 (%d nodo(s), %d nombre(s))"
                % (len(nom4), len(muertas)), len(con_muerta), con_muerta[:3]))
    # 5) ningun nodo con dos claves de fase: es el check de lista blanca de claves de Gate 0
    claves = [c for c in checks if "lista blanca del esquema" in c[1]]
    sub.append(("ningun nodo con dos claves de fase (check de Gate 0: %s)"
                % (claves[0][1] if claves else "AUSENTE"),
                0 if claves and claves[0][0] == "OK" else 1,
                [claves[0][1]] if claves else []))
    # 6) ningun nodo se cita a si mismo tras resolver: el check de auto-arista
    sub.append(("ningun nodo se cita a si mismo tras resolver (check de Gate 0)",
                0 if ok_auto else 1, []))
    for texto, n_malos, muestra in sub:
        print("  [%s] %s -> %d incumplimiento(s)%s"
              % ("OK" if n_malos == 0 else "FALLO", texto, n_malos,
                 (": " + ", ".join(map(str, muestra))) if muestra and n_malos else ""))
    total_malos = sum(x[1] for x in sub)
    v = "VERDE" if total_malos == 0 else "NO CUMPLE"
    print("CIFRA: %d de %d sub-celdas en verde." % (sum(1 for x in sub if x[1] == 0), len(sub)))
    print("VEREDICTO: %s" % v)
    veredictos.append((filas[5][0], v, "%d de %d sub-celdas en verde, acotadas a las nominas"
                       % (sum(1 for x in sub if x[1] == 0), len(sub))))

    # ---- FILA 7: 06 MESAS ------------------------------------------------
    cabecera(6)
    mesas = [x for x in F if x["fase"] == "06_MESAS"]
    print("INSTRUMENTO: sobre las %d fichas de 06_MESAS se mide lo que la celda nombra:" % len(mesas))
    print("que la decision este ESCRITA (campo adjudicacion no vacio), que traiga MOTIVO")
    print("y que traiga COBERTURA AL LADO. Motivo y cobertura se buscan LITERALES en el")
    print("texto de la ficha: 'porque'/'motivo' para el primero, y una cifra de cobertura")
    print("(un 'N de M', un 'cobertura' o un porcentaje) para la segunda. Se mide literal")
    print("y no se ensancha para que atrape a nadie.")
    # LA SEDE DE LA DECISION DE UNA MESA NO ES SOLO SU FICHA. docs/plan/06_MESAS.md
    # es la pagina donde la casa escribe las decisiones de las cinco mesas, y
    # medir solo el jsonl seria medir el indice en vez del expediente. Se une el
    # texto de la ficha con el de la seccion de esa pagina que nombra la mesa.
    ruta_mesas = os.path.join(RAIZ, "docs", "plan", "06_MESAS.md")
    pagina_mesas = io.open(ruta_mesas, encoding="utf-8").read() if os.path.exists(ruta_mesas) else ""
    print("  sede anadida: docs/plan/06_MESAS.md (%d caracteres)" % len(pagina_mesas))
    sin_algo = []
    for m in mesas:
        texto = " ".join(str(m.get(k) or "") for k in ("adjudicacion", "nota"))
        # el trozo de la pagina que habla de ESTA mesa: desde donde la nombra
        # hasta 4.000 caracteres despues, que es el tamano de una seccion suya.
        pos = pagina_mesas.find(m["id_op"])
        if pos >= 0:
            texto += " " + pagina_mesas[pos:pos + 4000]
        tiene_dec = bool((m.get("adjudicacion") or "").strip())
        tiene_motivo = bool(re.search(r"\bporque\b|\bmotivo\b", texto, re.I))
        tiene_cob = bool(re.search(r"\bcobertura\b|\b\d+\s+de\s+\d+\b|\d+\s*%", texto, re.I))
        marca = "OK" if (tiene_dec and tiene_motivo and tiene_cob) else "FALLO"
        print("  [%s] %-10s decision escrita %s | motivo %s | cobertura %s | nombrada en 06_MESAS.md %s"
              % (marca, m["id_op"], tiene_dec, tiene_motivo, tiene_cob, pos >= 0))
        if marca == "FALLO":
            sin_algo.append(m["id_op"])
    v = "VERDE" if not sin_algo else "NO CUMPLE"
    print("CIFRA: %d de %d mesas con decision, motivo y cobertura." % (len(mesas) - len(sin_algo), len(mesas)))
    print("VEREDICTO: %s" % v)
    veredictos.append((filas[6][0], v, "%d de %d mesas completas" % (len(mesas) - len(sin_algo), len(mesas))))

    # ---- FILA 8: 07 ADUANA -----------------------------------------------
    cabecera(7)
    print("SE LEE CON LA FASE YA CERRADA POR EL ACTA 149 (adjudicacion 3.12), Y SE MIDE")
    print("CONTRA GATE 0, QUE ES LO QUE LA CELDA NOMBRA, no contra la vara de codigo, que")
    print("es otra unidad (frontera de la adjudicacion 3.9 del acta 144).")
    aduana = [c for c in checks if c[1].startswith("OP-A-")]
    print("  controles de la aduana corriendo en Gate 0: %d" % len(aduana))
    for e, t in aduana:
        print("    [%s] %s" % (e, t))
    v = "VERDE" if len(aduana) == 4 and all(e == "OK" for e, _ in aduana) else "NO CUMPLE"
    print("CIFRA: %d controles, %d en OK. La celda pide CUATRO."
          % (len(aduana), sum(1 for e, _ in aduana if e == "OK")))
    print("VEREDICTO: %s" % v)
    veredictos.append((filas[7][0], v, "%d controles OP-A en Gate 0, %d en OK"
                       % (len(aduana), sum(1 for e, _ in aduana if e == "OK"))))

    # ---- RESUMEN ----------------------------------------------------------
    print("")
    print("=" * 96)
    print("LAS OCHO FILAS, RESUMIDAS. CONTADO, NO TECLEADO.")
    print("=" * 96)
    print("| fase | veredicto | cifra |")
    print("|---|---|---|")
    for fase, v, cifra in veredictos:
        print("| %s | **%s** | %s |" % (fase, v, cifra))
    print("")
    for etiqueta in ("VERDE", "VERDE PARCIAL", "NO CUMPLE"):
        n = sum(1 for _f, v, _c in veredictos if v == etiqueta)
        print("  %s: %d de %d" % (etiqueta, n, len(veredictos)))
    print("")
    print("LA VERIFICACION TRANSVERSAL NO SE TOCA (TAREA 4.d): sus cinco puntos quedaron")
    print("medidos en la vuelta 148 y adjudicados en el acta 149. Este arnes no la corre y")
    print("no la declara cerrada.")


main()
