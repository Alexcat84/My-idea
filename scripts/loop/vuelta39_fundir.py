# -*- coding: utf-8 -*-
"""vuelta39_fundir.py

EJECUTA una de las DOS fusiones selladas de OP-D-04 en la vuelta 38:
  docs/loop/PLAN_V38_OPD04_TALLER.json       (reglas_brainstorming absorbe DOS)
  docs/loop/PLAN_V38_OPD04_ALTERNANCIA.json  (pensamiento_convergente_divergente absorbe DOS)

SUCESOR DECLARADO de scripts/loop/vuelta33_fundir.py, al que NO reemplaza. Aquel
ejecuta el esquema de UN absorbido de PLAN_V33 (campo `absorbido`, prefijos por
lista, cobertura sobre S1..Sn y A1..An). Estos dos planes traen otro esquema y
otra aritmetica, y por eso hace falta otro instrumento en vez de un parche:

  1. DOS ABSORBIDOS POR OPERACION, no uno. El desempate de P.8 ya esta decidido
     y sellado: aqui no se recalcula ni una decision, se ejecuta lo escrito.
  2. LA GUARDA DE TEXTO ES VERBATIM, no por prefijo. El plan trae el diccionario
     `origenes` con el texto ENTERO de cada paso y cada condicion de los tres
     nodos, asi que se compara caracter a caracter contra dataset/nodos. Si
     alguien edito un nodo entre el sellado (19 ago 2026) y hoy, esto cae.
  3. LOS PASOS FINALES SE DERIVAN DE LOS GRUPOS y se cotejan contra el campo
     `pasos_finales` del plan: si el plan se contradice a si mismo, cae.
  4. P.16, QUIEN FABRICA LIMPIA: la duplicada que la propia fusion fabrica se
     mide ANTES de limpiarla, se coteja contra `duplicadas_nuevas_esperadas` del
     plan, y se resuelve EN LA MISMA OPERACION.
  5. A6 DEL ACTA DE LA VUELTA 38: titulo_concepto y etiqueta_arbol del
     superviviente NO SE TOCAN, y la guarda lo comprueba sobre la copia final.

LO QUE NO HACE, y va dicho porque es la mitad del contrato: NO le escribe al
superviviente las aristas que los absorbidos declaraban en su propio fichero.
Esas las escribe scripts/run_phase1.py en su paso 5 (Simetrizacion de enlaces),
con precedente medido en el commit 72c718ea. El plan trae la lista entera en
`simulacion.simetrizacion_esperada` y su guarda de exactitud se corre APARTE,
sobre el log del ciclo, con scripts/loop/vuelta39_guarda_simetrizacion.py.

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.

Uso:
  python scripts/loop/vuelta39_fundir.py --plan docs/loop/PLAN_V38_OPD04_TALLER.json [--ejecutar]
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")


def ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def leer_crudo(nid):
    with io.open(ruta(nid), encoding="utf-8", newline="") as fh:
        bruto = fh.read()
    cola = ""
    while bruto and bruto[-1] in "\r\n":
        cola = bruto[-1] + cola
        bruto = bruto[:-1]
    return json.loads(bruto), cola


def escribir(nid, datos, cola):
    with io.open(ruta(nid), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def censo():
    vivos = deprecados = total = 0
    for nombre in os.listdir(NODOS):
        if not nombre.endswith(".json"):
            continue
        total += 1
        d, _ = leer_crudo(nombre[:-5])
        if d.get("deprecado") or d.get("deprecated"):
            deprecados += 1
        else:
            vivos += 1
    return total, vivos, deprecados


def main():
    modo = "--simular"
    plan_ruta = None
    argv = sys.argv[1:]
    for i, x in enumerate(argv):
        if x in ("--simular", "--ejecutar"):
            modo = x
        elif x == "--plan":
            plan_ruta = argv[i + 1]
    if not plan_ruta:
        sys.exit("hace falta --plan <ruta>")

    plan = json.load(io.open(plan_ruta, encoding="utf-8"))
    sup = plan["superviviente"]
    absorbidos = list(plan["absorbidos"])
    sim = plan["simulacion"]

    print("PLAN     : %s" % plan_ruta)
    print("OPERACION: %s" % plan["operacion"])
    print("SELLADO  : %s" % plan["estado"])
    print("MODO     : %s" % modo)
    print("=" * 78)

    fallos = []
    total_antes, vivos_antes, dep_antes = censo()
    print("censo ANTES: %d ficheros, %d vivos, %d deprecados"
          % (total_antes, vivos_antes, dep_antes))

    # prefijo -> node_id (el del superviviente trae el sufijo entre parentesis)
    pref = {}
    for k, v in plan["prefijos"].items():
        pref[k] = v.split(" (")[0].strip()
    if sorted(pref.values()) != sorted([sup] + absorbidos):
        fallos.append("los prefijos del plan no nombran a los tres nodos")

    nodos = {}
    for nid in [sup] + absorbidos:
        nodos[nid] = leer_crudo(nid)

    # GUARDA 1: fuente del SUPERVIVIENTE y vida de los TRES.
    # El campo `fuente_esperada` del plan es la fuente DEL SUPERVIVIENTE, no la de
    # los tres: los dos actos de OP-D-04 son DE FUENTE MIXTA, medido hoy, y el
    # primer borrador de este instrumento lo leyo como si fuera de los tres y CAYO
    # en rojo contra brainstorming_divergente y brainstorming_efectivo. La guarda
    # no se afloja, se corrige y se abre: la fuente de cada absorbido SE IMPRIME y
    # viaja verbatim a merged_originals, que es donde el archivo la conserva.
    d_sup = nodos[sup][0]
    if d_sup.get("fuente") != plan["fuente_esperada"]:
        fallos.append("%s: fuente %r, el plan esperaba %r"
                      % (sup, d_sup.get("fuente"), plan["fuente_esperada"]))
    for nid in [sup] + absorbidos:
        d = nodos[nid][0]
        if d.get("deprecado") or d.get("deprecated"):
            fallos.append("%s: ya esta deprecado" % nid)
    print("guarda 1, fuente del superviviente contra el plan y vida de los TRES: %s"
          % ("OK" if not fallos else "ROJO"))
    print("  ACTO DE FUENTE MIXTA, las tres fuentes impresas y ninguna escondida:")
    for nid in [sup] + absorbidos:
        papel = "superviviente" if nid == sup else "absorbido"
        print("    %-38s %-14s %s" % (nid, papel, nodos[nid][0].get("fuente")))

    # GUARDA 2: conteos
    reales, esperados = {}, {}
    for nid in [sup] + absorbidos:
        d = nodos[nid][0]
        reales[nid] = (len(d.get("pasos_accionables") or []),
                       len(d.get("condiciones_activacion") or []))
        esperados[nid] = (plan["pasos_totales"][nid], plan["condiciones_totales"][nid])
    for nid in [sup] + absorbidos:
        marca = "OK" if reales[nid] == esperados[nid] else "ROJO"
        print("guarda 2, %-38s pasos y condiciones %s contra %s: %s"
              % (nid, reales[nid], esperados[nid], marca))
        if reales[nid] != esperados[nid]:
            fallos.append("%s: conteos %s, el plan esperaba %s" % (nid, reales[nid], esperados[nid]))

    # GUARDA 3: VERBATIM contra dataset/nodos, pieza a pieza
    origenes = plan["origenes"]
    calzan = cotejadas = 0
    for p, nid in sorted(pref.items()):
        d = nodos[nid][0]
        for etiqueta, campo in (("", "pasos_accionables"), ("C", "condiciones_activacion")):
            for i, texto in enumerate(d.get(campo) or [], 1):
                clave = "%s%s%d" % (p, etiqueta, i)
                cotejadas += 1
                if clave not in origenes:
                    fallos.append("origen ausente del plan: %s (%s, %s %d)" % (clave, nid, campo, i))
                elif origenes[clave] != texto:
                    fallos.append("NO VERBATIM en %s: %r contra el plan %r"
                                  % (clave, texto[:60], origenes[clave][:60]))
                else:
                    calzan += 1
    universo_total = set(
        "%s%s%d" % (p, e, i)
        for p, nid in pref.items()
        for e, campo in (("", "pasos_accionables"), ("C", "condiciones_activacion"))
        for i in range(1, len(nodos[nid][0].get(campo) or []) + 1))
    sobrantes = sorted(set(origenes) - universo_total)
    if sobrantes:
        fallos.append("origenes del plan que ya no existen en los nodos: %s" % sobrantes)
    print("guarda 3, VERBATIM contra dataset/nodos: %d de %d calzan, %d sobrantes en el plan"
          % (calzan, cotejadas, len(sobrantes)))

    # GUARDA 4: cobertura exacta de los origenes por los grupos
    for etq, grupos, sufijo, campo in (("pasos", plan["grupos_pasos"], "", "pasos_accionables"),
                                       ("condiciones", plan["grupos_condiciones"], "C",
                                        "condiciones_activacion")):
        usados = [o for g in grupos for o in g["origenes"]]
        universo = set("%s%s%d" % (p, sufijo, i)
                       for p, nid in pref.items()
                       for i in range(1, len(nodos[nid][0].get(campo) or []) + 1))
        rep = sorted({o for o in usados if usados.count(o) > 1})
        fal = sorted(universo - set(usados))
        sob = sorted(set(usados) - universo)
        print("guarda 4, cobertura de %-12s %d de %d, repetidos %s, faltan %s, sobran %s"
              % (etq, len(usados), len(universo), rep, fal, sob))
        if rep or fal or sob:
            fallos.append("cobertura rota en %s" % etq)

    # GUARDA 5: los finales se DERIVAN de los grupos y calzan con el campo sellado
    pasos_derivados = [g["texto"] for g in plan["grupos_pasos"]]
    cond_derivadas = [g["texto"] for g in plan["grupos_condiciones"]]
    ok5 = (pasos_derivados == list(plan["pasos_finales"])
           and cond_derivadas == list(plan["condiciones_finales"]))
    print("guarda 5, los finales derivados de los grupos calzan con el campo sellado: %s"
          % ("OK" if ok5 else "ROJO"))
    if not ok5:
        fallos.append("los pasos o condiciones finales no se derivan de los grupos")

    pasos_finales = list(plan["pasos_finales"])
    cond_finales = list(plan["condiciones_finales"])

    # GUARDAS 6 y 7, sobre el NODO RESULTANTE ENTERO y no solo sobre sus pasos.
    # El primer borrador de este instrumento heredo de vuelta33_fundir.py un cuerpo
    # hecho SOLO de pasos y CAYO en rojo contra la alternancia por tres piezas
    # ('3-5 alternativas', 'convergencia', 'iteraciones') que viven en el
    # entregable y en el resumen. Ir a mirar dijo que las tres SI sobreviven, asi
    # que lo roto era la vara y no el plan. La vara corregida NO afloja nada: se
    # cotejan los CUATRO campos de texto que la fusion escribe y ADEMAS se imprime
    # en cual sobrevive cada pieza, para que la sede no se pueda esconder.
    partes = {"pasos": " ".join(pasos_finales),
              "condiciones": " ".join(cond_finales),
              "entregable": plan["entregable_final"],
              "resumen": plan["resumen_final"]}

    def sedes(pieza):
        return [k for k in ("pasos", "condiciones", "entregable", "resumen") if pieza in partes[k]]

    for etq, lista, guarda in (("preservar_literal", plan["preservar_literal"], 6),
                               ("rastros", plan["rastros"], 7)):
        vivas = 0
        print("guarda %d, %s en el nodo resultante entero:" % (guarda, etq))
        for pieza in lista:
            d_sedes = sedes(pieza)
            if d_sedes:
                vivas += 1
            else:
                fallos.append("%s ausente del nodo resultante: %r" % (etq, pieza))
            print("    %-42s %s" % (repr(pieza), d_sedes or "AUSENTE [ROJO]"))
        print("    %d de %d" % (vivas, len(lista)))

    # --- las redirecciones, medidas contra el grafo de HOY y no contra el plan ---
    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d, c = leer_crudo(nombre[:-5])
            todos[d["node_id"]] = (d, c)

    redirecciones, muertos = [], []
    for nid, (d, _c) in todos.items():
        if nid in absorbidos:
            continue
        for campo in CAMPOS:
            lista = d.get(campo) or []
            for muere in absorbidos:
                if muere in lista:
                    if d.get("deprecado") or d.get("deprecated"):
                        muertos.append((nid, campo, muere))
                    else:
                        redirecciones.append((nid, campo, muere))
    redirecciones.sort()
    muertos.sort()
    print("redirecciones medidas hoy sobre nodos VIVOS: %d" % len(redirecciones))
    for nid, campo, muere in redirecciones:
        print("    %-48s %-18s %s -> %s" % (nid, campo, muere, sup))
    print("nodos DEPRECADOS que nombran y NO se tocan: %d" % len(muertos))
    for nid, campo, muere in muertos:
        print("    %-48s %-18s %s (deprecado: registro historico)" % (nid, campo, muere))

    esperadas = sorted((r["nodo"], r["campo"], r["nombraba"]) for r in sim["redirecciones_esperadas"])
    if sorted(redirecciones) != esperadas:
        fallos.append("las redirecciones de hoy no son las del plan: hoy %d, plan %d"
                      % (len(redirecciones), len(esperadas)))
    print("guarda 8, redirecciones contra el plan sellado (%d esperadas): %s"
          % (len(esperadas), "OK" if sorted(redirecciones) == esperadas else "ROJO"))
    esp_muertos = sorted((r["nodo"], r["campo"], r["nombraba"])
                         for r in sim["redirecciones_no_tocadas_por_deprecadas"])
    if sorted(muertos) != esp_muertos:
        fallos.append("los deprecados que nombran no son los del plan: hoy %s, plan %s"
                      % (sorted(muertos), esp_muertos))
    print("guarda 8b, deprecados que nombran contra el plan (%d esperados): %s"
          % (len(esp_muertos), "OK" if sorted(muertos) == esp_muertos else "ROJO"))

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    # --- el resultado, sobre COPIA EN MEMORIA ---
    s, cola_s = nodos[sup]
    s_nuevo = json.loads(json.dumps(s))
    s_nuevo["pasos_accionables"] = pasos_finales
    s_nuevo["condiciones_activacion"] = cond_finales
    s_nuevo["entregable_esperado"] = plan["entregable_final"]
    s_nuevo["resumen_teorico"] = plan["resumen_final"]
    alias = list(s_nuevo.get("ids_alias") or [])
    merged = list(s_nuevo.get("merged_originals") or [])
    for muere in absorbidos:
        if muere not in alias:
            alias.append(muere)
        if not any(m.get("node_id") == muere for m in merged):
            a = nodos[muere][0]
            merged.append({"node_id": muere,
                           "titulo": a.get("titulo_concepto"),
                           "fuente": a.get("fuente")})
    s_nuevo["ids_alias"] = alias
    s_nuevo["merged_originals"] = merged

    cambios = {sup: (s_nuevo, cola_s)}
    for muere in absorbidos:
        a, cola_a = nodos[muere]
        a_nuevo = json.loads(json.dumps(a))
        a_nuevo["deprecado"] = True
        cambios[muere] = (a_nuevo, cola_a)

    # P.16: se sustituye, se MIDE la duplicada fabricada, y se limpia en el acto
    fabricadas = []
    for nid, campo, _muere in redirecciones:
        base = cambios.get(nid, (json.loads(json.dumps(todos[nid][0])), todos[nid][1]))
        d2 = base[0]
        antes = list(d2.get(campo) or [])
        sustituida = [sup if x in absorbidos else x for x in antes]
        dup_antes = len(antes) - len(set(antes))
        dup_despues = len(sustituida) - len(set(sustituida))
        if dup_despues > dup_antes:
            fabricadas.append({"nodo": nid, "campo": campo, "resuelve_a": sup})
        limpia, vistos = [], set()
        for x in sustituida:
            if x not in vistos:
                vistos.add(x)
                limpia.append(x)
        d2[campo] = limpia
        cambios[nid] = (d2, base[1])

    print()
    print("### P.16, LAS DUPLICADAS QUE LA PROPIA FUSION FABRICA, medidas antes de limpiarlas")
    for f in fabricadas:
        print("    %-48s %-18s -> %s" % (f["nodo"], f["campo"], f["resuelve_a"]))
    print("    TOTAL FABRICADAS: %d" % len(fabricadas))
    esp_dup = sim["duplicadas_nuevas_esperadas"]
    igual = (sorted((f["nodo"], f["campo"], f["resuelve_a"]) for f in fabricadas)
             == sorted((f["nodo"], f["campo"], f["resuelve_a"]) for f in esp_dup))
    print("guarda 9, duplicadas fabricadas contra el plan (%d esperadas): %s"
          % (len(esp_dup), "OK" if igual else "ROJO"))
    if not igual:
        fallos.append("las duplicadas fabricadas no son las del plan: hoy %s, plan %s"
                      % (fabricadas, esp_dup))

    # GUARDA 10 y 11, sobre la copia ya construida y limpia
    auto = dupes = 0
    for nid, (d, _c) in cambios.items():
        for campo in CAMPOS:
            lista = d.get(campo) or []
            if nid in lista:
                auto += 1
                fallos.append("AUTO-ARISTA: %s se nombra a si mismo en %s" % (nid, campo))
            if len(lista) != len(set(lista)):
                dupes += 1
                fallos.append("DUPLICADA SIN RESOLVER: %s tiene repetidos en %s" % (nid, campo))
    print("guarda 10, cero auto-arista tras resolver: %s (%d)" % ("OK" if not auto else "ROJO", auto))
    print("guarda 11, cero duplicada tras resolver: %s (%d)" % ("OK" if not dupes else "ROJO", dupes))

    # GUARDA 12, a6 del acta: titulo y etiqueta del superviviente INTACTOS
    ok12 = (s_nuevo.get("titulo_concepto") == s.get("titulo_concepto")
            == plan["titulo_sin_cambio"]
            and s_nuevo.get("etiqueta_arbol") == s.get("etiqueta_arbol")
            == plan["etiqueta_arbol_sin_cambio"])
    print("guarda 12, a6 del acta, titulo y etiqueta SIN TOCAR (%r / %r): %s"
          % (plan["titulo_sin_cambio"], plan["etiqueta_arbol_sin_cambio"],
             "OK" if ok12 else "ROJO"))
    if not ok12:
        fallos.append("titulo o etiqueta del superviviente cambiaron, y a6 lo prohibe")

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    print()
    print("EL RESULTADO, sobre copia en memoria:")
    print("  %s: %d pasos, %d condiciones, alias %s"
          % (sup, len(s_nuevo["pasos_accionables"]), len(s_nuevo["condiciones_activacion"]),
             s_nuevo["ids_alias"]))
    for i, p in enumerate(s_nuevo["pasos_accionables"], 1):
        print("    %d. %s" % (i, p))
    for i, c in enumerate(s_nuevo["condiciones_activacion"], 1):
        print("    c%d. %s" % (i, c))
    print("  entregable: %s" % s_nuevo["entregable_esperado"])
    for muere in absorbidos:
        a_nuevo = cambios[muere][0]
        print("  %s: deprecado True, texto INTACTO (%d pasos, %d condiciones)"
              % (muere, len(a_nuevo.get("pasos_accionables") or []),
                 len(a_nuevo.get("condiciones_activacion") or [])))
    print("  ficheros que se tocarian: %d" % len(cambios))

    if modo == "--simular":
        print()
        print("SIMULACION: cero escrituras.")
        return 0

    for nid, (d, c) in cambios.items():
        escribir(nid, d, c)
    total_desp, vivos_desp, dep_desp = censo()
    print()
    print("ESCRITO. censo DESPUES: %d ficheros, %d vivos, %d deprecados"
          % (total_desp, vivos_desp, dep_desp))
    print("         censo ANTES  : %d ficheros, %d vivos, %d deprecados"
          % (total_antes, vivos_antes, dep_antes))
    rojo = 0
    if total_desp != total_antes:
        print("  [ROJO] EL CENSO SE MOVIO, y una fusion no borra ficheros")
        rojo = 1
    if vivos_desp != vivos_antes - len(absorbidos):
        print("  [ROJO] los vivos no bajaron en %d" % len(absorbidos))
        rojo = 1
    if dep_desp != dep_antes + len(absorbidos):
        print("  [ROJO] los deprecados no subieron en %d" % len(absorbidos))
        rojo = 1
    if not rojo:
        print("guarda 13, el censo no se movio y los vivos bajaron en %d: OK" % len(absorbidos))
    return rojo


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
