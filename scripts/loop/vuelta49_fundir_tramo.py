# -*- coding: utf-8 -*-
"""vuelta49_fundir_tramo.py . EJECUTA TRAMOS DE `OP-U-01`.

SUCESOR DECLARADO de scripts/loop/vuelta48_fundir_tramo.py, al que NO reemplaza.
Es el MISMO instrumento con UNA sola cosa nueva, y la novedad nace de una
correccion del auditor, no de un capricho.

EL TERCER DESTINO QUE FALTABA: `INCISO`. El instrumento de la vuelta 48 sabia
DOS destinos para una pieza del nodo que muere, APPEND (viaja entera como paso
nuevo) y CUBIERTO:n (ya lo dice el paso n del superviviente). El acta de la
vuelta 48, seccion 4, encontro el caso de en medio en el acto 49: el paso 3 de
`storytelling_para_el_cambio` estaba marcado `CUBIERTO:3` y NO era verdad
completa, porque el paso del superviviente decia las demostraciones y no decia
QUIEN modela. Marcarlo `APPEND` habria duplicado las demostraciones; marcarlo
`CUBIERTO` perdia el matiz. La figura correcta ya existia en la casa y es el
INCISO ADOSADO, remedio escrito de SALVAGUARDA en la TABLA DE LOS SEIS MOTIVOS
DE PERDIDA DE LINEA (`docs/plan/02_DESTEJIDOS.md`, precedente `OP-D-02` paso 1,
linea 220): "el inciso se adosa al paso que protege". La vuelta 49 lo aplico a
mano con `scripts/loop/vuelta49_inciso_adosado.py` y aqui queda incorporado al
instrumento de fundir, para que ninguna pieza vuelva a tener que elegir entre
duplicarse y perderse.

LA MARCA SE ESCRIBE ASI, con tres campos separados por barra vertical:
    "INCISO:<n>|<inciso VERBATIM del paso del que muere>|<nexo>"
y lleva sus DOS guardas propias, las mismas del instrumento suelto: el inciso
tiene que ser trozo LITERAL del paso del absorbido, y si ya esta dentro del paso
del superviviente no se apila. El NEXO es lo unico que el instrumento aporta de
su cosecha y se imprime aparte para poder discutirlo por separado del contenido.

Lo que sigue es el docstring del instrumento del que este desciende, entero:

vuelta48_fundir_tramo.py . EJECUTA EL TRAMO 1 DE `OP-U-01`.

SUCESOR DECLARADO de scripts/loop/vuelta39_fundir.py, al que NO reemplaza.
Aquel ejecuta UN plan de UN acto con grupos de pasos redactados a mano, porque
venia de un destejido y habia que repartir por bloques. Aqui son DIECISIETE
actos de FUSION PURA sin bloques, y la regla de la pagina para ese caso es la
otra mitad de la misma linea: cada perdida al bloque del que proviene, y LA QUE
NO TENGA BLOQUE, AL SUPERVIVIENTE. Por eso este instrumento no redacta texto
nuevo: mueve piezas VERBATIM.

EL CONTRATO, y es lo que hace que no haya erratas posibles:
  - El plan NO trae texto. Trae INDICES. Cada paso y cada condicion de cada
    nodo absorbido lleva una marca: APPEND (viaja entero al superviviente),
    CUBIERTO:n (ya lo dice el paso n del superviviente) o CUBIERTO_COND:n (ya
    lo dice su condicion n).
  - La COBERTURA se comprueba: cada indice del absorbido aparece EXACTAMENTE
    UNA VEZ y no sobra ninguno. Si el plan se olvida de una pieza, esto cae en
    rojo y no escribe. Una perdida sin destino no es una perdida: es un olvido.
  - El texto que se anade se lee del fichero del nodo por su indice. No se
    teclea aqui ni en el plan.

LO QUE NO TOCA: titulo_concepto, etiqueta_arbol, fuente, resumen_teorico y
entregable_esperado del superviviente. Esta operacion funde y reparte; no
redacta. Y el nodo que muere queda DEPRECADO CON ALIAS, con su texto INTACTO,
que es lo que hace que un recorrido viejo siga contando algo.

P.16, QUIEN FABRICA LIMPIA, y aqui hay una divergencia con el encargo que se
declara en vez de resolverse en silencio: el encargo dice que las duplicadas
que la fusion fabrique QUEDAN PARA OP-S-12, y a la vez pone como guarda
obligatoria CERO DUPLICADAS O AUTO-ARISTAS TRAS RESOLVER. Las dos no caben. Se
sigue P.16 del banco del plan mas la guarda: se MIDEN antes de limpiarlas, se
imprimen una por una, y se limpian EN LA MISMA OPERACION.

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.

Uso:
  python scripts/loop/vuelta49_fundir_tramo.py --plan docs/loop/PLAN_V49_OPU01.json [--ejecutar]
"""
import argparse
import collections
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
    total = vivos = dep = 0
    for nombre in os.listdir(NODOS):
        if not nombre.endswith(".json"):
            continue
        total += 1
        d, _ = leer_crudo(nombre[:-5])
        if d.get("deprecado") or d.get("deprecated"):
            dep += 1
        else:
            vivos += 1
    return total, vivos, dep


def cargar_semillas():
    """Las MISMAS fuentes que lee scripts/run_phase1.py: las 20 puertas core mas
    las semillas de cada mundo integrado."""
    out = set()
    p = os.path.join(RAIZ, "dataset", "metadata", "entry_seeds.json")
    if os.path.exists(p):
        out.update(json.load(io.open(p, encoding="utf-8")).get("seeds", []))
    packs = os.path.join(RAIZ, "packs")
    if os.path.isdir(packs):
        for d in sorted(os.listdir(packs)):
            q = os.path.join(packs, d, "metadata", "entry_seeds.json")
            if os.path.exists(q):
                out.update(json.load(io.open(q, encoding="utf-8")))
    return out


def cargar_puentes():
    """Extremos core y de dominio de todo puente APROBADO."""
    out = {}
    packs = os.path.join(RAIZ, "packs")
    if not os.path.isdir(packs):
        return out
    for d in sorted(os.listdir(packs)):
        q = os.path.join(packs, d, "metadata", "bridges_aprobados.json")
        if not os.path.exists(q):
            continue
        for x in json.load(io.open(q, encoding="utf-8")).get("aprobados", []):
            for extremo in ("core", "dominio"):
                if x.get(extremo):
                    out[x[extremo]] = d
    return out


SEMILLAS = cargar_semillas()
PUENTES = cargar_puentes()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    plan = json.load(io.open(a.plan, encoding="utf-8"))
    modo = "EJECUTAR" if a.ejecutar else "SIMULAR"
    print("=" * 78)
    print("OP-U-01, TRAMO %s . MODO %s" % (plan["tramo"], modo))
    print("plan: %s (%s)" % (a.plan, plan["estado"]))
    print("=" * 78)

    fallos = []
    total_antes, vivos_antes, dep_antes = censo()
    print("censo ANTES: %d ficheros, %d vivos, %d deprecados"
          % (total_antes, vivos_antes, dep_antes))
    print("semillas de entrada cargadas: %d | extremos de puente aprobado: %d"
          % (len(SEMILLAS), len(PUENTES)))

    # ---- todo el catalogo en memoria; NADA se escribe hasta el final ----
    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d, c = leer_crudo(nombre[:-5])
            todos[d["node_id"]] = [json.loads(json.dumps(d)), c]

    todos_absorbidos = set()
    for act in plan["actos"]:
        todos_absorbidos.update(act["absorbidos"])

    tabla_perdidas = []
    resumen = []

    for act in plan["actos"]:
        n = act["orden"]
        sup = act["superviviente"]
        abs_ = list(act["absorbidos"])
        print()
        print("-" * 78)
        print("ACTO %d . sobrevive %s . absorbe %s" % (n, sup, ", ".join(abs_)))

        # GUARDA 1: los miembros existen, estan vivos, y el plan los nombra todos.
        # SE JUZGA A SI MISMA, no a la lista global de fallos: el primer borrador
        # imprimia ROJO en todos los actos siguientes al primero que fallara por
        # otra causa, que es un semaforo que no mide lo que dice medir.
        rotos_1 = []
        for x in act["miembros"]:
            if x not in todos:
                rotos_1.append("%s no existe en el catalogo" % x)
            elif todos[x][0].get("deprecado") or todos[x][0].get("deprecated"):
                rotos_1.append("%s YA esta deprecado" % x)
        if sorted(act["miembros"]) != sorted([sup] + abs_):
            rotos_1.append("miembros y superviviente mas absorbidos no calzan")
        for r in rotos_1:
            fallos.append("acto %d: %s" % (n, r))
        print("  guarda 1, miembros vivos y nomina completa: %s"
              % ("OK" if not rotos_1 else "ROJO %s" % rotos_1))

        s = todos[sup][0]
        pasos_sup = list(s.get("pasos_accionables") or [])
        cond_sup = list(s.get("condiciones_activacion") or [])
        n_pasos0, n_cond0 = len(pasos_sup), len(cond_sup)

        # GUARDA 1B, LA PUERTA. Nace de un GATE 0 EN ROJO de esta misma vuelta y
        # se escribe aqui para que no vuelva a pasar en silencio (canon 9 del
        # banco): el acto 36 absorbia
        # investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor, que es
        # SEMILLA DE ENTRADA del mundo compras y ademas DESTINO DE UN PUENTE
        # APROBADO. Al deprecarlo, run_phase1.py dio GATE 0: FALLIDO por dos
        # chequeos a la vez. Una semilla es la puerta por la que se entra a un
        # mundo: deprecarla es cerrar la puerta, y ninguna regla de esta
        # operacion autoriza a mover una puerta. Un nodo que es semilla o
        # extremo de puente NO SE ABSORBE: su acto se declara.
        for muere in abs_:
            if muere in SEMILLAS:
                fallos.append("acto %d: %s es SEMILLA DE ENTRADA y no se puede absorber" % (n, muere))
            if muere in PUENTES:
                fallos.append("acto %d: %s es extremo de PUENTE APROBADO (%s) y no se puede absorber"
                              % (n, muere, PUENTES[muere]))
        print("  guarda 1B, ningun absorbido es semilla ni extremo de puente: %s"
              % ("ROJO" if any(x in SEMILLAS or x in PUENTES for x in abs_) else "OK"))

        # GUARDA 2: COBERTURA EXACTA. cada indice una vez, ninguno de mas
        rotas = 0
        for muere in abs_:
            d = todos[muere][0]
            for etq, campo, marcas in (("pasos", "pasos_accionables", act["pasos"]),
                                       ("condiciones", "condiciones_activacion",
                                        act["condiciones"])):
                real = set(str(i) for i in range(1, len(d.get(campo) or []) + 1))
                dicho = set((marcas.get(muere) or {}).keys())
                faltan, sobran = sorted(real - dicho), sorted(dicho - real)
                if faltan or sobran:
                    rotas += 1
                    fallos.append("acto %d, %s de %s: faltan %s, sobran %s"
                                  % (n, etq, muere, faltan, sobran))
        print("  guarda 2, cobertura exacta de indices (cero olvidos): %s"
              % ("OK" if not rotas else "ROJO"))

        # --- construir el superviviente sobre COPIA EN MEMORIA ---
        anadidos_p, anadidos_c, incisos_puestos = [], [], []
        for muere in abs_:
            d = todos[muere][0]
            for i, texto in enumerate(d.get("pasos_accionables") or [], 1):
                m = (act["pasos"].get(muere) or {}).get(str(i), "")
                if m == "APPEND":
                    pasos_sup.append(texto)
                    anadidos_p.append((muere, i, len(pasos_sup)))
                    destino = "PASO %d del superviviente" % len(pasos_sup)
                elif m.startswith("INCISO:"):
                    # EL TERCER DESTINO. Ver el docstring: ni APPEND ni CUBIERTO.
                    try:
                        cual, inciso, nexo = m[len("INCISO:"):].split("|")
                        k = int(cual)
                    except ValueError:
                        fallos.append("acto %d: marca INCISO mal formada %r" % (n, m))
                        tabla_perdidas.append((n, muere, "paso", i, texto, "MARCA ROTA"))
                        continue
                    if inciso not in texto:
                        fallos.append("acto %d: el inciso %r NO es trozo verbatim del paso %d de %s"
                                      % (n, inciso, i, muere))
                    if not (1 <= k <= len(pasos_sup)):
                        fallos.append("acto %d: INCISO al paso %d, que el superviviente no tiene" % (n, k))
                        destino = "MARCA ROTA"
                    elif inciso in pasos_sup[k - 1]:
                        destino = ("el INCISO ya estaba dentro del PASO %d del superviviente "
                                   "(idempotencia: no se apila)" % k)
                    else:
                        pasos_sup[k - 1] = pasos_sup[k - 1] + nexo + inciso
                        incisos_puestos.append((muere, i, k, inciso, nexo))
                        destino = ("INCISO ADOSADO al PASO %d del superviviente "
                                   "(SALVAGUARDA, tabla de los seis motivos)" % k)
                elif m.startswith("CUBIERTO_COND:"):
                    destino = "ya lo dice la CONDICION %s del superviviente" % m.split(":")[1]
                elif m.startswith("CUBIERTO:"):
                    destino = "ya lo dice el PASO %s del superviviente" % m.split(":")[1]
                else:
                    destino = "MARCA DESCONOCIDA %r" % m
                    fallos.append("acto %d: marca desconocida %r" % (n, m))
                tabla_perdidas.append((n, muere, "paso", i, texto, destino))
            for i, texto in enumerate(d.get("condiciones_activacion") or [], 1):
                m = (act["condiciones"].get(muere) or {}).get(str(i), "")
                if m == "APPEND":
                    cond_sup.append(texto)
                    anadidos_c.append((muere, i, len(cond_sup)))
                    destino = "CONDICION %d del superviviente" % len(cond_sup)
                elif m.startswith("CUBIERTO:"):
                    destino = "ya lo dice la CONDICION %s del superviviente" % m.split(":")[1]
                else:
                    destino = "MARCA DESCONOCIDA %r" % m
                    fallos.append("acto %d: marca desconocida %r" % (n, m))
                tabla_perdidas.append((n, muere, "condicion", i, texto, destino))

        # GUARDA 3: nada se pierde por el camino ni se duplica literal
        if len(set(pasos_sup)) != len(pasos_sup):
            fallos.append("acto %d: el superviviente queda con un paso repetido literal" % n)
        if len(set(cond_sup)) != len(cond_sup):
            fallos.append("acto %d: el superviviente queda con una condicion repetida literal" % n)
        print("  guarda 3, cero repetidos literales en el resultado: %s"
              % ("OK" if len(set(pasos_sup)) == len(pasos_sup)
                 and len(set(cond_sup)) == len(cond_sup) else "ROJO"))

        s["pasos_accionables"] = pasos_sup
        s["condiciones_activacion"] = cond_sup
        alias = list(s.get("ids_alias") or [])
        merged = list(s.get("merged_originals") or [])
        for muere in abs_:
            if muere not in alias:
                alias.append(muere)
            if not any(m.get("node_id") == muere for m in merged):
                dm = todos[muere][0]
                merged.append({"node_id": muere,
                               "titulo": dm.get("titulo_concepto"),
                               "fuente": dm.get("fuente")})
        s["ids_alias"] = alias
        s["merged_originals"] = merged
        for muere in abs_:
            todos[muere][0]["deprecado"] = True

        print("  pasos %d -> %d (anadidos %d) | condiciones %d -> %d (anadidas %d)"
              % (n_pasos0, len(pasos_sup), len(anadidos_p),
                 n_cond0, len(cond_sup), len(anadidos_c)))
        if incisos_puestos:
            print("  INCISOS ADOSADOS: %d" % len(incisos_puestos))
            for muere, i, k, inciso, nexo in incisos_puestos:
                print("     del paso %d de %s al PASO %d del superviviente" % (i, muere, k))
                print("        inciso VERBATIM: %r" % inciso)
                print("        nexo (lo unico de cosecha propia): %r" % nexo)
                print("        paso resultante: %s" % pasos_sup[k - 1])
        print("  alias del superviviente: %s" % alias)
        resumen.append({"acto": n, "superviviente": sup, "absorbidos": abs_,
                        "pasos_antes": n_pasos0, "pasos_despues": len(pasos_sup),
                        "condiciones_antes": n_cond0,
                        "condiciones_despues": len(cond_sup)})

    # ---- REDIRECCIONES, medidas contra el catalogo de HOY ----
    print()
    print("=" * 78)
    print("REDIRECCIONES Y P.16, sobre el catalogo entero")
    print("=" * 78)
    destino = {}
    for act in plan["actos"]:
        for muere in act["absorbidos"]:
            destino[muere] = act["superviviente"]

    redirigidos, en_deprecados, fabricadas, autos = [], [], [], []
    for nid, par in todos.items():
        d = par[0]
        for campo in CAMPOS:
            lista = list(d.get(campo) or [])
            if not any(x in destino for x in lista):
                continue
            if nid in todos_absorbidos:
                # el nodo que muere conserva su texto INTACTO: registro historico
                continue
            if d.get("deprecado") or d.get("deprecated"):
                for x in lista:
                    if x in destino:
                        en_deprecados.append((nid, campo, x))
                continue
            sustituida = [destino.get(x, x) for x in lista]
            for x in lista:
                if x in destino:
                    redirigidos.append((nid, campo, x, destino[x]))
            # P.16: medir ANTES de limpiar
            antes = len(lista) - len(set(lista))
            desp = len(sustituida) - len(set(sustituida))
            if desp > antes:
                fabricadas.append((nid, campo))
            limpia, vistos = [], set()
            for x in sustituida:
                if x == nid:
                    autos.append((nid, campo))
                    continue
                if x not in vistos:
                    vistos.add(x)
                    limpia.append(x)
            d[campo] = limpia

    print("redirecciones sobre nodos VIVOS: %d" % len(redirigidos))
    for nid, campo, x, y in sorted(redirigidos):
        print("   %-52s %-17s %s -> %s" % (nid, campo, x, y))
    print()
    print("nodos DEPRECADOS que nombran a un absorbido y NO se tocan: %d" % len(en_deprecados))
    for nid, campo, x in sorted(en_deprecados):
        print("   %-52s %-17s %s (registro historico)" % (nid, campo, x))
    print()
    print("P.16, DUPLICADAS QUE LA PROPIA FUSION FABRICA, medidas antes de limpiarlas: %d"
          % len(fabricadas))
    for nid, campo in sorted(fabricadas):
        print("   %-52s %s" % (nid, campo))
    print()
    print("AUTO-ARISTAS que la fusion habria creado y se retiran: %d" % len(autos))
    for nid, campo in sorted(autos):
        print("   %-52s %s" % (nid, campo))

    # ---- GUARDAS FINALES sobre la copia ya construida ----
    print()
    print("=" * 78)
    print("GUARDAS FINALES sobre la copia en memoria")
    print("=" * 78)
    alias_map = {}
    for nid, par in todos.items():
        if par[0].get("deprecado"):
            continue
        for x in (par[0].get("ids_alias") or []):
            alias_map[x] = nid

    def res(x):
        v = set()
        while x in alias_map and x not in v:
            v.add(x)
            x = alias_map[x]
        return x

    # CORRECCION DECLARADA SOBRE MI PROPIA GUARDA, 19 ago 2026 (vuelta 48). El
    # primer borrador contaba las duplicadas TRAS RESOLVER sobre el catalogo
    # ENTERO y salio ROJO con 894. Fui a mirar antes de tocar el plan: las 894
    # YA ESTABAN, son el backlog historico que docs/plan/ARISTAS_DUPLICADAS.jsonl
    # censa y que OP-S-12 tiene encargado. Una guarda que suma el pasivo ajeno al
    # propio no mide nada: se cae siempre y deja de ser guarda. La vara correcta
    # es la que ya usaba scripts/loop/vuelta39_fundir.py, SOLO LAS NUEVAS: se
    # cuentan antes y despues y se resta. Lo que esta operacion tiene que
    # garantizar es que no FABRICA ninguna, no que limpia las de otros.
    def censo_defectos(estado_alias, leer):
        def r(x):
            v = set()
            while x in estado_alias and x not in v:
                v.add(x)
                x = estado_alias[x]
            return x
        dups, auto = set(), set()
        for nid in todos:
            d = leer(nid)
            if d.get("deprecado"):
                continue
            for campo in CAMPOS:
                lista = d.get(campo) or []
                if nid in lista:
                    auto.add((nid, campo))
                rr = [r(x) for x in lista if r(x) != nid]
                vistos = set()
                for x in rr:
                    if x in vistos:
                        dups.add((nid, campo, x))
                    vistos.add(x)
        return dups, auto

    alias0 = {}
    orig_cache = {}
    for nid in todos:
        o, _ = leer_crudo(nid)
        orig_cache[nid] = o
        if not o.get("deprecado"):
            for x in (o.get("ids_alias") or []):
                alias0[x] = nid
    dup0, auto0 = censo_defectos(alias0, lambda n: orig_cache[n])
    dup1, auto1 = censo_defectos(alias_map, lambda n: todos[n][0])
    nuevas_dup = sorted(dup1 - dup0)
    nuevas_auto = sorted(auto1 - auto0)
    for nid, campo, x in nuevas_dup:
        fallos.append("DUPLICADA NUEVA: %s en %s resuelve dos veces a %s" % (nid, campo, x))
    for nid, campo in nuevas_auto:
        fallos.append("AUTO-ARISTA NUEVA: %s en %s" % (nid, campo))
    print("  duplicadas tras resolver ANTES del tramo (pasivo historico, OP-S-12): %d"
          % len(dup0))
    print("  duplicadas tras resolver DESPUES del tramo                          : %d"
          % len(dup1))
    print("guarda A, cero AUTO-ARISTAS nuevas             : %s (%d)"
          % ("OK" if not nuevas_auto else "ROJO", len(nuevas_auto)))
    print("guarda B, cero DUPLICADAS nuevas tras resolver : %s (%d)"
          % ("OK" if not nuevas_dup else "ROJO", len(nuevas_dup)))
    print("  y el tramo BAJA el pasivo historico en %d, porque P.16 limpia lo que"
          % (len(dup0) - len(dup1)))
    print("  la propia sustitucion toca. Ni una duplicada ajena se toca de mas.")

    intactos = 0
    for act in plan["actos"]:
        sup = act["superviviente"]
        orig, _ = leer_crudo(sup)
        d = todos[sup][0]
        for campo in ("titulo_concepto", "etiqueta_arbol", "fuente",
                      "resumen_teorico", "entregable_esperado"):
            if d.get(campo) != orig.get(campo):
                fallos.append("acto %d: %s cambio en %s y esta operacion no redacta"
                              % (act["orden"], sup, campo))
            else:
                intactos += 1
    print("guarda C, los CINCO campos que esta operacion NO redacta, intactos: %d de %d"
          % (intactos, len(plan["actos"]) * 5))

    # LA GUARDA D SE JUZGA A SI MISMA Y NO A LA LISTA GLOBAL: el primer borrador
    # imprimia "revisar" en cuanto CUALQUIER otra guarda hubiera fallado, que es
    # un semaforo que no mide lo que dice medir.
    rotos_d = []
    for muere in sorted(todos_absorbidos):
        orig, _ = leer_crudo(muere)
        d = todos[muere][0]
        if (d.get("pasos_accionables") != orig.get("pasos_accionables")
                or d.get("condiciones_activacion") != orig.get("condiciones_activacion")
                or d.get(CAMPOS[0]) != orig.get(CAMPOS[0])
                or d.get(CAMPOS[1]) != orig.get(CAMPOS[1])):
            rotos_d.append(muere)
            fallos.append("el absorbido %s perdio texto y debe quedar INTACTO" % muere)
    print("guarda D, los %d absorbidos conservan su texto INTACTO: %s"
          % (len(todos_absorbidos), "OK" if not rotos_d else "ROJO %s" % rotos_d))

    print()
    print("TABLA DE PERDIDAS, pieza por pieza (%d filas)" % len(tabla_perdidas))
    print("%5s %-44s %-10s %3s  %s" % ("acto", "de que nodo", "que", "n", "a donde va"))
    for n, muere, que, i, texto, dest in tabla_perdidas:
        print("%5d %-44s %-10s %3d  %s" % (n, muere, que, i, dest))
        print("        %s" % texto[:150])

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    print()
    print("RESUMEN DEL TRAMO")
    print("  actos fundidos      : %d" % len(plan["actos"]))
    print("  nodos implicados    : %d" % sum(len(x["miembros"]) for x in plan["actos"]))
    print("  nodos que MUEREN    : %d" % len(todos_absorbidos))
    print("  piezas repartidas   : %d (%d viajan enteras, %d ya estaban dichas)"
          % (len(tabla_perdidas),
             sum(1 for r in tabla_perdidas if r[5].startswith(("PASO", "CONDICION"))),
             sum(1 for r in tabla_perdidas if r[5].startswith("ya lo dice"))))
    print("  actos DECLARADOS y no fundidos: %d" % len(plan["declarados_y_no_fundidos"]))

    if not a.ejecutar:
        print()
        print("SIMULACION: cero escrituras.")
        return 0

    tocados = set()
    for act in plan["actos"]:
        tocados.add(act["superviviente"])
        tocados.update(act["absorbidos"])
    for nid, campo, x, y in redirigidos:
        tocados.add(nid)
    for nid in sorted(tocados):
        escribir(nid, todos[nid][0], todos[nid][1])
    total_d, vivos_d, dep_d = censo()
    print()
    print("ESCRITO. ficheros tocados: %d" % len(tocados))
    print("censo DESPUES: %d ficheros, %d vivos, %d deprecados" % (total_d, vivos_d, dep_d))
    print("censo ANTES  : %d ficheros, %d vivos, %d deprecados"
          % (total_antes, vivos_antes, dep_antes))
    print("delta deprecados: %+d (esperado %+d): %s"
          % (dep_d - dep_antes, len(todos_absorbidos),
             "OK" if dep_d - dep_antes == len(todos_absorbidos) else "ROJO"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
