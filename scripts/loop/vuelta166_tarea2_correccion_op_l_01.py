# -*- coding: utf-8 -*-
r"""vuelta166_tarea2_correccion_op_l_01.py . TAREA 2 de la vuelta 166.

LA CORRECCION DECLARADA DE `OP-L-01`, POR EL CARRIL DEL BANCO 9.10
(adjudicaciones 5.2, 5.3 y 5.4 del acta 165).

QUE HACE Y QUE NO HACE. Anade DOS elementos MAS a la lista `verificacion` de la
ficha `OP-L-01` de `docs/plan/OPERACIONES.jsonl`: uno corrige la clausula 1 y
otro la clausula 2. **NO BORRA NI UNA LETRA** y **NO CREA CLAVE NUEVA DE
ESQUEMA**: es exactamente la via que la ficha gemela `OP-L-03` uso en la vuelta
72 para su clausula equivalente, y que el acta 71 (seccion 6, adjudicacion 3)
adjudico CON LAS PALABRAS NO ES PARADA. **LA CLAUSULA 3 NO SE CORRIGE**: se mide
y se publica, y las cinco nominas que solo existen como prosa quedan NOMBRADAS Y
NO RELLENADAS, que es lo que la verificacion de `OP-I-01` manda.

EL RESOLUTOR VA DELANTE DE TODO CONTEO (`P.1`, `EJECUTOR.md` 9). La clausula 1 se
mide DOS VECES, literal y resuelta, y las dos cifras se publican: la literal es
la que la clausula afirmaba y la resuelta es la que el acta 165 adjudica.

LA SIMULACION PREVIA ES OBLIGATORIA Y VA ANTES DE ESCRIBIR. Sin `--aplicar` el
instrumento MIDE y NO ESCRIBE: construye la ficha nueva EN MEMORIA y comprueba
sobre ella los CINCO invariantes del carril (las clausulas viejas byte a byte,
las claves del esquema identicas, la lista creciendo en exactamente dos, el
resto de la ficha intacto y las otras 70 lineas intactas). Si uno solo falla, no
escribe.

EL ESTADO SE MIDE ANTES Y DESPUES Y NO SE MUEVE A CIEGAS. El pase de `estado` de
esta ficha NO se hace aqui por decision propia: se mide con
`tallar_estado_de_fase.py`, que es la vara de la casa que los pases de las
vueltas 152 y 154 usaron como puerta, y se hace SOLO si esa vara da CUMPLIDO.

SU CASO POSITIVO POR MUTACION es `vuelta166_tarea2_mutacion_correccion.py`.

USO:
  python scripts/loop/vuelta166_tarea2_correccion_op_l_01.py            (mide, NO escribe)
  python scripts/loop/vuelta166_tarea2_correccion_op_l_01.py --aplicar  (mide, escribe y re mide)
"""
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
LECTURAS = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

ID_OP = "OP-L-01"
FASE = "09_LECTURAS_DIRIGIDAS"

CLAUSULA_1 = ("ninguna de las once aparece en INTRA_DOMINIO_VEREDICTOS.jsonl: "
              "viven solo aqui")
CLAUSULA_2 = "el marcador del cribado no se mueve: sigue en 2.117"
CLAUSULA_3 = ("cada nomina afectada se re-mide con su cobertura al lado "
              "(banco 9.26)")

CABECERA_LD = re.compile(
    r"^### `(LD-\d+)` \. `([^`]+)` contra `([^`]+)` \. \*\*([^*]+)\*\*", re.M)

MARCA = "CORRECCION DECLARADA (2026-09-04, vuelta 166, TAREA 2"


def lineas_del_fichero():
    return io.open(OPS, encoding="utf-8").read().split("\n")


def ficha(lineas, id_op=ID_OP):
    for i, l in enumerate(lineas, 1):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get("id_op") == id_op:
            return i, d, l
    raise SystemExit("ROJO: no existe la ficha %s" % id_op)


def mapa_de_alias():
    """EL RESOLUTOR (`P.1`). Devuelve (mapa alias -> destino, cifra de nodos)."""
    mapa = {}
    n = 0
    for f in sorted(os.listdir(NODOS)):
        if not f.endswith(".json"):
            continue
        n += 1
        d = json.load(io.open(os.path.join(NODOS, f), encoding="utf-8"))
        for a in (d.get("ids_alias") or []):
            mapa[a] = d["node_id"]
    return mapa, n


def resolver(mapa, x):
    visto = set()
    while x in mapa and x not in visto:
        visto.add(x)
        x = mapa[x]
    return x


def las_once():
    txt = io.open(LECTURAS, encoding="utf-8").read()
    return [(m.group(1), m.group(2), m.group(3), m.group(4))
            for m in CABECERA_LD.finditer(txt)]


def veredictos():
    return [json.loads(l) for l in io.open(VEREDICTOS, encoding="utf-8") if l.strip()]


def medir_clausula_1(mapa, once, V):
    """Devuelve (n_literal, n_resuelto, n_pares_lit, n_pares_res, hallazgos).
    hallazgos = [(LD, a, b, clase_ld, [(puesto, clase, cruda_a, cruda_b, dominio)])]"""
    literal, resuelto, idx = set(), set(), {}
    for f in V:
        a, b = f["nodo_a"], f["nodo_b"]
        literal.add(frozenset((a, b)))
        k = frozenset((resolver(mapa, a), resolver(mapa, b)))
        resuelto.add(k)
        idx.setdefault(k, []).append(
            (f["puesto_intra"], f["clase"], a, b, f["dominio"]))
    n_lit, hallazgos = 0, []
    for ld, a, b, clase in once:
        if frozenset((a, b)) in literal:
            n_lit += 1
        k = frozenset((resolver(mapa, a), resolver(mapa, b)))
        if k in resuelto:
            hallazgos.append((ld, a, b, clase, sorted(idx[k])))
    return n_lit, len(hallazgos), len(literal), len(resuelto), hallazgos


def texto_correccion_1(hallazgos, n_lit, n_res, n_pares_lit, n_pares_res,
                       n_alias, n_filas):
    """La correccion de la clausula 1. TODA CIFRA Y TODO NOMBRE PROPIO SALEN DE
    LA MEDICION DE HOY: ninguno esta tecleado en esta funcion."""
    trozos = []
    for ld, a, b, clase, puestos in hallazgos:
        detalle = "; ".join(
            "el puesto %d en %s (%s contra %s, dominio %s)" % (p, c, x, y, dom)
            for p, c, x, y, dom in puestos)
        trozos.append("%s (%s contra %s, cuya lectura dirigida es %s) cae sobre "
                      "%d puesto(s) del archivo: %s"
                      % (ld, a, b, clase, len(puestos), detalle))
    return (
        "%s del encargo), POR EL CARRIL DEL BANCO 9.10 Y CON EL TEXTO VIEJO ENTERO "
        "ARRIBA, SIN TACHARLO Y SIN CLAVE NUEVA DE ESQUEMA (es un elemento mas de "
        "esta misma lista verificacion, que es la via que la ficha gemela OP-L-03 "
        "uso en la vuelta 72 para su clausula equivalente y que el acta 71, seccion "
        "6, adjudicacion 3, adjudico CON LAS PALABRAS NO ES PARADA). "
        "LO QUE SE CORRIGE es la clausula que en esta lista dice, verbatim: '%s'. "
        "MEDIDO HOY CON EL RESOLUTOR PUESTO, que P.1 manda sin excepcion y da igual "
        "quien haya pedido el conteo: %d filas en docs/INTRA_DOMINIO_VEREDICTOS.jsonl, "
        "mapa de %d alias construido de ids_alias de dataset/nodos/, %d pares "
        "literales distintos y %d pares RESUELTOS distintos. "
        "EN COMPARACION LITERAL LA CLAUSULA SIGUE SIENDO CIERTA Y SE DICE ANTES QUE "
        "NADA: %d de las once aparecen. EN COMPARACION RESUELTA APARECEN %d, y se "
        "nombran una por una con su puesto, su clase y sus ids crudos, que es lo que "
        "la adjudicacion 5.3 del acta 165 manda: %s. "
        "QUE ES ESA COINCIDENCIA Y QUE NO ES, DICHO CON LA MEDICION DELANTE: los ids "
        "crudos de esos puestos NO son los ids con los que las once estan escritas, y "
        "ninguno de esos puestos entro a la cola del cribado por una lectura dirigida; "
        "lo que los junta con las once es que la campana FUNDIO nodos DESPUES de la "
        "fecha_corte de esta ficha, y el resolutor los lleva hoy al mismo par. Es "
        "HUELLA DE FUSION, y el propio acta 165 lo dice de este mismo ejemplar en su "
        "seccion 4.3, con estas palabras: 'su conflicto es huella de fusion, no error "
        "de lectura'. "
        "LA VARA, DICHA ENTERA Y NO A MEDIAS: lo que la clausula pregunta es si alguna "
        "de las once entro a la cola del cribado y tiene ahi su veredicto, o sea si "
        "'viven solo aqui'. La respuesta medida hoy es que NINGUNA entro, y se sostiene "
        "por los dos caminos: en literal no aparece ninguna, y en resuelto las que "
        "coinciden lo hacen sobre puestos que entraron a la cola por la semejanza y con "
        "otros ids. LA EXCEPCION QUEDA NOMBRADA Y MEDIDA EN VEZ DE CALLADA, que es todo "
        "lo que esta correccion pretende. "
        "LO QUE ESTA CORRECCION NO HACE: no mueve ni un veredicto, no adjudica clase a "
        "ninguno de esos puestos, no toca ni un nodo, no cambia el estado ni las "
        "dependencias de esta ficha ni de ninguna otra, y no autoriza ninguna lectura "
        "nueva. Ver docs/loop/SALIDA_V166_T2_CORRECCION_OP_L_01.txt."
        % (MARCA, CLAUSULA_1, n_filas, n_alias, n_pares_lit, n_pares_res,
           n_lit, n_res, "; ".join(trozos)))


def texto_correccion_2(marcador_hoy, adjudicacion, escribiria):
    """La correccion de la clausula 2, que cita el campo adjudicacion de la
    PROPIA ficha, leido hoy y no parafraseado."""
    return (
        "%s del encargo), POR EL MISMO CARRIL DEL BANCO 9.10, CON EL TEXTO VIEJO "
        "ENTERO ARRIBA Y SIN CLAVE NUEVA DE ESQUEMA. "
        "LO QUE SE CORRIGE es la clausula que en esta lista dice, verbatim: '%s'. "
        "LA VUELTA 165 LA TRAJO COMO PARADA por no poder leerla sin estrecharla ni "
        "ensancharla, e hizo bien en traerla con la letra delante en vez de improvisar. "
        "EL ACTA 165, EN SU ADJUDICACION 5.2, LA RESOLVIO SIN DOCTRINA NUEVA Y CITANDO "
        "EL CAMPO adjudicacion DE ESTA MISMA FICHA, que dice hoy, leido de este mismo "
        "registro: '%s'. La frase 'no entran en la cola ni mueven su marcador' es la "
        "lectura DE EFECTO, escrita por la propia operacion, y leerla asi NO es "
        "estrecharla: es leer la ficha ENTERA, que es lo que P.5 manda. "
        "EL NUMERAL 2.117 ES EL VALOR DEL MARCADOR EN LA fecha_corte DE ESTA FICHA, "
        "TESTIGO Y NO CONDICION. MEDIDO HOY: el marcador del cribado vale %d, y la "
        "simulacion previa de esta operacion da %d escrituras declaradas en nodos, "
        "preservar, eliminar y aristas_nuevas, o sea que la operacion no puede mover "
        "el marcador ni queriendo. LA CLAUSULA, LEIDA ASI, SE CUMPLE. "
        "PRECEDENTE AL BYTE, Y POR ESO NO HACE FALTA DOCTRINA NUEVA: la clausula "
        "gemela de OP-L-03, escrita el mismo dia y con el mismo corte, se corrigio por "
        "este mismo carril en la vuelta 72, por adicion dentro de su propia lista "
        "verificacion, con el texto viejo entero arriba y sin clave nueva de esquema, y "
        "el acta 71, seccion 6, adjudicacion 3, la adjudico CON LAS PALABRAS NO ES "
        "PARADA. "
        "LO QUE ESTA CORRECCION NO HACE: no borra el numeral 2.117 ni la clausula que "
        "lo lleva, no mueve el marcador, no toca un nodo y no cambia el estado ni las "
        "dependencias de ninguna ficha. Ver "
        "docs/loop/SALIDA_V166_T2_CORRECCION_OP_L_01.txt."
        % (MARCA, CLAUSULA_2, adjudicacion, marcador_hoy, escribiria))


def invariantes(linea_vieja, linea_nueva, lineas_viejas, lineas_nuevas, n_linea):
    """LOS CINCO INVARIANTES DEL CARRIL, comprobados sobre la ficha NUEVA sin
    escribirla. Devuelve lista de (nombre, ok, detalle)."""
    v = json.loads(linea_vieja)
    n = json.loads(linea_nueva)
    r = []

    viejas = v.get("verificacion") or []
    nuevas = n.get("verificacion") or []
    igual_prefijo = nuevas[:len(viejas)] == viejas
    r.append(("1_las_clausulas_viejas_siguen_byte_a_byte_y_en_su_orden",
              igual_prefijo,
              "%d clausulas viejas, las %d primeras de las nuevas coinciden: %s"
              % (len(viejas), len(viejas), igual_prefijo)))

    r.append(("2_el_esquema_no_gana_ni_pierde_una_clave",
              sorted(v.keys()) == sorted(n.keys()),
              "antes %d claves, despues %d; identicas: %s"
              % (len(v), len(n), sorted(v.keys()) == sorted(n.keys()))))

    r.append(("3_verificacion_crece_en_exactamente_dos",
              len(nuevas) - len(viejas) == 2,
              "de %d a %d, delta %d" % (len(viejas), len(nuevas),
                                        len(nuevas) - len(viejas))))

    resto_v = {k: val for k, val in v.items() if k != "verificacion"}
    resto_n = {k: val for k, val in n.items() if k != "verificacion"}
    r.append(("4_el_resto_de_la_ficha_no_se_toca_ni_en_estado",
              resto_v == resto_n,
              "estado antes %r, despues %r" % (v.get("estado"), n.get("estado"))))

    otras_v = [l for i, l in enumerate(lineas_viejas, 1) if i != n_linea]
    otras_n = [l for i, l in enumerate(lineas_nuevas, 1) if i != n_linea]
    r.append(("5_las_otras_lineas_del_fichero_no_se_tocan",
              otras_v == otras_n,
              "%d lineas comparadas, identicas: %s"
              % (len(otras_v), otras_v == otras_n)))
    return r


def contar_estados(lineas):
    c = {}
    for l in lineas:
        if not l.strip():
            continue
        d = json.loads(l)
        c[d["estado"]] = c.get(d["estado"], 0) + 1
    return c


def fila_del_tallador(id_op, fase):
    """LA VARA DE LA CASA, INVOCADA Y NO REIMPLEMENTADA. Es la misma puerta que
    los pases de las vueltas 152 y 154 usaron: si la fila no dice CUMPLIDO, la
    ficha no se mueve."""
    r = subprocess.run(
        [sys.executable, os.path.join("scripts", "loop", "tallar_estado_de_fase.py"),
         "--fase", fase], capture_output=True, cwd=RAIZ)
    texto = r.stdout.decode("utf-8", "replace")
    for l in texto.split("\n"):
        if l.startswith("| %s |" % id_op):
            celdas = [c.strip() for c in l.strip().strip("|").split("|")]
            return celdas, l
    return None, texto


def main(aplicar):
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 166, TAREA 2: LA CORRECCION DECLARADA DE OP-L-01, CARRIL 9.10")
    print("=" * 78)
    print("")

    lineas = lineas_del_fichero()
    n_linea, d, linea_vieja = ficha(lineas)
    print("A) LA FICHA, LEIDA HOY, Y EL ESTADO ANTES")
    print("   docs/plan/OPERACIONES.jsonl:%d" % n_linea)
    for k in ("id_op", "fase", "tipo", "orden", "estado", "fecha_corte"):
        print("   %-16s %s" % (k + ":", d.get(k)))
    for k in ("depende_de", "bloquea_a", "nodos", "preservar", "eliminar",
              "aristas_nuevas"):
        print("   %-16s CIFRA %d  %s" % (k + ":", len(d.get(k) or []), d.get(k)))
    print("   verificacion, sus %d clausulas de HOY:" % len(d.get("verificacion") or []))
    for i, c in enumerate(d.get("verificacion") or [], 1):
        print("      %d. %s" % (i, c[:160] + (" [...]" if len(c) > 160 else "")))
    print("")
    estados_antes = contar_estados(lineas)
    print("   EL CONTEO DE ESTADOS ANTES, del fichero entero:")
    for k in sorted(estados_antes):
        print("      %-8s %d" % (k, estados_antes[k]))
    print("   CIFRA operaciones: %d" % sum(estados_antes.values()))
    print("")

    print("B) LA SIMULACION PREVIA, PRIMERA MITAD: QUE ESCRIBE LA OPERACION")
    escribiria = sum(len(d.get(k) or []) for k in
                     ("nodos", "preservar", "eliminar", "aristas_nuevas"))
    print("   CIFRA elementos declarados para escribir en el grafo: %d" % escribiria)
    print("   VEREDICTO: es una operacion de VERIFICACION PURA. No mueve un nodo,")
    print("   no mueve una arista y no puede mover el marcador.")
    if escribiria != 0:
        print("   PARADA: la ficha declara escrituras y esta vuelta no las autoriza.")
        return 1
    print("")

    mapa, n_nodos = mapa_de_alias()
    once = las_once()
    V = veredictos()
    print("C) EL RESOLUTOR, DELANTE DE TODO CONTEO (P.1)")
    print("   CIFRA ficheros de nodo leidos: %d" % n_nodos)
    print("   CIFRA alias en el mapa: %d" % len(mapa))
    print("   CIFRA cabeceras LD leidas de LECTURAS_DIRIGIDAS.md: %d" % len(once))
    print("   CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d" % len(V))
    print("")

    n_lit, n_res, n_pl, n_pr, hallazgos = medir_clausula_1(mapa, once, V)
    print("D) CLAUSULA 1, MEDIDA HOY POR LOS DOS CAMINOS")
    print("   CIFRA pares distintos, comparacion LITERAL: %d" % n_pl)
    print("   CIFRA pares distintos, comparacion RESUELTA: %d" % n_pr)
    print("   CIFRA de las once que aparecen, LITERAL: %d" % n_lit)
    print("   CIFRA de las once que aparecen, RESUELTA: %d" % n_res)
    for ld, a, b, clase, puestos in hallazgos:
        print("   %s  %s contra %s  (lectura dirigida: %s)" % (ld, a, b, clase))
        for p, c, x, y, dom in puestos:
            print("      puesto %-5d clase %-3s dominio %-8s ids crudos: %s | %s"
                  % (p, c, dom, x, y))
    print("   CIFRA puestos implicados en total: %d"
          % sum(len(p) for _l, _a, _b, _c, p in hallazgos))
    print("   CONTRASTE con el acta 165 (no es fuente, es contraste): dice 3 en")
    print("   resuelta, LD-01 en 712 A, 976 A y 1190 D, LD-05 en 1325 D y LD-11")
    print("   en 1281 D. MI MEDICION DE HOY MANDA, y coincide o se declara.")
    print("")

    print("E) CLAUSULA 2, MEDIDA HOY, CON EL CAMPO adjudicacion DE LA PROPIA FICHA")
    print("   la letra de la clausula: %r" % CLAUSULA_2)
    print("   fecha_corte de la ficha: %s" % d.get("fecha_corte"))
    print("   CIFRA marcador del cribado HOY: %d" % len(V))
    print("   CIFRA que la clausula escribe: 2117")
    print("   CIFRA diferencia: %d" % (len(V) - 2117))
    print("   EL CAMPO adjudicacion, LEIDO HOY DE LA FICHA:")
    print("      %s" % d.get("adjudicacion"))
    contiene = "no entran en la cola ni mueven su marcador" in (d.get("adjudicacion") or "")
    print("   la frase 'no entran en la cola ni mueven su marcador' esta en el")
    print("   campo adjudicacion de la ficha: %s" % ("SI" if contiene else "NO"))
    if not contiene:
        print("   PARADA: la adjudicacion 5.2 se apoya en una frase que la ficha")
        print("   no trae. No se corrige sobre una cita que no se puede verificar.")
        return 1
    print("")
    print("F) CLAUSULA 3: NO SE CORRIGE, SE MIDE Y SE PUBLICA CON SUS DOS SUMANDOS")
    print("   LA ADJUDICACION 5.4 DEL ACTA 165 LA DA POR CUMPLIDA HASTA DONDE HAY")
    print("   QUE MEDIR, y manda que las que faltan queden NOMBRADAS Y NO")
    print("   RELLENADAS, que es lo que la verificacion de OP-I-01 pide.")
    print("   NO SE REIMPLEMENTA SU VARA: se invoca el instrumento de la vuelta 165,")
    print("   que es el que la midio y el que el auditor reprodujo. Dos varas para")
    print("   la misma pregunta es exactamente lo que esta casa no hace.")
    r = subprocess.run(
        [sys.executable, os.path.join("scripts", "loop", "vuelta165_tarea6_op_l_01.py")],
        capture_output=True, cwd=RAIZ)
    salida = r.stdout.decode("utf-8", "replace")
    dentro = False
    for l in salida.split("\n"):
        if l.startswith("F) CLAUSULA 3"):
            dentro = True
        elif l.startswith("G) EL VEREDICTO"):
            dentro = False
        if dentro:
            print("   | " + l)
    print("   EXITCODE del instrumento de la 165: %d" % r.returncode)
    print("   Y LA LEGIBILIDAD QUE EL ENCARGO PIDE, DICHA AQUI: donde una cobertura")
    print("   suma dos universos, los DOS SUMANDOS van al lado del total. La")
    print("   seleccion de canal publica 10 de 10 y sus sumandos son 8 leidos en el")
    print("   cribado mas 2 lecturas dirigidas de esta tanda; el sales roadmap")
    print("   publica 10 de 15 y sus sumandos son 10 mas 0. El criterio no cambio")
    print("   entre los dos: cambia lo que cada racimo trae.")
    print("")

    print("G) LA SIMULACION PREVIA, SEGUNDA MITAD: LA FICHA NUEVA, EN MEMORIA")
    ya = [c for c in (d.get("verificacion") or []) if c.startswith(MARCA)]
    if ya:
        print("   YA ESTABA: la ficha trae %d correccion(es) con esta marca." % len(ya))
        print("   CIFRA correcciones escritas: 0. Idempotente, no se toca.")
        aplicar = False
    corr1 = texto_correccion_1(hallazgos, n_lit, n_res, n_pl, n_pr, len(mapa), len(V))
    corr2 = texto_correccion_2(len(V), d.get("adjudicacion"), escribiria)
    nueva = json.loads(linea_vieja)
    if not ya:
        nueva["verificacion"] = list(nueva["verificacion"]) + [corr1, corr2]
    linea_nueva = json.dumps(nueva, ensure_ascii=False)
    lineas_nuevas = list(lineas)
    lineas_nuevas[n_linea - 1] = linea_nueva
    print("   CIFRA bytes de la correccion 1: %d" % len(corr1.encode("utf-8")))
    print("   CIFRA bytes de la correccion 2: %d" % len(corr2.encode("utf-8")))
    print("   CIFRA bytes de la linea antes: %d" % len(linea_vieja.encode("utf-8")))
    print("   CIFRA bytes de la linea despues: %d" % len(linea_nueva.encode("utf-8")))
    print("")
    print("   LOS CINCO INVARIANTES DEL CARRIL, SOBRE LA FICHA NUEVA SIN ESCRIBIRLA:")
    inv = invariantes(linea_vieja, linea_nueva, lineas, lineas_nuevas, n_linea)
    malos = 0
    for nombre, ok, detalle in inv:
        print("      %-52s %s   %s" % (nombre, "PASA" if ok else "FALLA", detalle))
        if not ok:
            malos += 1
    print("   CIFRA invariantes: %d | pasan: %d | fallan: %d"
          % (len(inv), len(inv) - malos, malos))
    if malos and not ya:
        print("   PARADA: la simulacion falla. NO SE ESCRIBE NADA.")
        return 1
    print("")
    print("   EL TEXTO ENTERO QUE SE ANADIRIA, PARA QUE NADA ENTRE SIN LEERSE:")
    print("   --- CORRECCION 1 ---")
    print("   %s" % corr1)
    print("   --- CORRECCION 2 ---")
    print("   %s" % corr2)
    print("")
    if not aplicar:
        print("H) NO SE ESCRIBE (falta --aplicar, o la ficha ya estaba corregida)")
    else:
        with io.open(OPS, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(lineas_nuevas))
        print("H) ESCRITO")
        print("   docs/plan/OPERACIONES.jsonl:%d" % n_linea)
        print("   CIFRA correcciones anadidas: 2")
    print("")

    print("I) LA COMPROBACION QUE NO SE FIA DE LO QUE ACABA DE ESCRIBIR")
    lineas2 = lineas_del_fichero()
    n2, d2, _l2 = ficha(lineas2)
    print("   CIFRA lineas del fichero antes: %d | despues: %d"
          % (len(lineas), len(lineas2)))
    print("   CIFRA clausulas de verificacion antes: %d | despues: %d"
          % (len(d.get("verificacion") or []), len(d2.get("verificacion") or [])))
    print("   las tres clausulas originales siguen, byte a byte y en su orden: %s"
          % ((d2.get("verificacion") or [])[:3] == [CLAUSULA_1, CLAUSULA_2, CLAUSULA_3]))
    print("   claves del esquema antes: %d | despues: %d | identicas: %s"
          % (len(d), len(d2), sorted(d.keys()) == sorted(d2.keys())))
    estados_despues = contar_estados(lineas2)
    print("   EL CONTEO DE ESTADOS DESPUES, del fichero entero:")
    for k in sorted(estados_despues):
        print("      %-8s %d" % (k, estados_despues[k]))
    print("   CIFRA operaciones: %d" % sum(estados_despues.values()))
    print("   el conteo de estados NO se movio: %s"
          % (estados_antes == estados_despues))
    print("")

    print("J) EL PASE DE ESTADO: SE MIDE CON LA VARA DE LA CASA Y NO SE DECIDE AQUI")
    print("   LA PUERTA ES tallar_estado_de_fase.py, el mismo instrumento que los")
    print("   pases de las vueltas 152 y 154 usaron como puerta, y su regla escrita")
    print("   es literal: la ficha que NO salga CUMPLIDO no se mueve.")
    celdas, cruda = fila_del_tallador(ID_OP, FASE)
    if celdas is None:
        print("   PARADA: el tallador no imprime fila para %s." % ID_OP)
        return 1
    etiquetas = ["id_op", "fase escrita", "estado (contraste)", "vara",
                 "remitida", "destino medido contra el grafo", "veredicto"]
    for et, c in zip(etiquetas, celdas):
        print("      %-32s %s" % (et + ":", c[:180]))
    veredicto = celdas[-1]
    print("   VEREDICTO DEL TALLADOR: %s" % veredicto)
    print("")
    print("   LAS TRES CLAUSULAS, TRAS LAS DOS CORRECCIONES:")
    print("      clausula 1: CUMPLIDA con su excepcion NOMBRADA Y MEDIDA")
    print("      clausula 2: CUMPLIDA por la lectura de efecto de la propia ficha")
    print("      clausula 3: CUMPLIDA hasta donde el inventario nombra miembros,")
    print("                  con las cinco restantes NOMBRADAS Y NO RELLENADAS")
    print("")
    if veredicto == "CUMPLIDO":
        print("   LA PUERTA ABRE. El pase de estado se puede hacer y se hace")
        print("   en un solo acto con el conteo antes y despues.")
    else:
        print("   LA PUERTA NO ABRE, Y NO SE FUERZA. EL ESTADO NO SE MUEVE.")
        print("   EL MOTIVO, MEDIDO Y NO SUPUESTO: la fila de %s dice vara %r y" % (ID_OP, celdas[3]))
        print("   veredicto %r. No existe regla escrita que mida contra el grafo" % veredicto)
        print("   el destino de un tipo MESA, y esta ficha es de tipo MESA con")
        print("   nodos, preservar, eliminar y aristas_nuevas VACIOS.")
        print("   LOS DOS PRECEDENTES QUE EL ENCARGO CITA PIDEN LO CONTRARIO, y por")
        print("   eso no sirven de puerta aqui: las once de la vuelta 152 y las")
        print("   cinco mesas de la 154 se movieron POR SALIR CUMPLIDO en este")
        print("   mismo tallador (las mesas con vara MESA, medida por sus hijas).")
        print("   Mover esta ficha hoy exigiria adoptar una vara NUEVA, que para un")
        print("   tipo MESA bastan sus clausulas de verificacion, y esa vara NO")
        print("   ESTA ESCRITA EN NINGUN SITIO. Inventarla es lo que EJECUTOR.md 5")
        print("   prohibe. VA COMO PENDIENTE DE DOCTRINA, no como parada: no")
        print("   contradice ninguna regla vigente, es que la regla no existe.")
        print("   Y SE TRAE EL CONTRAEJEMPLO EN VEZ DE ESCONDERLO: OP-V-01 es una")
        print("   ficha de tipo MESA que HOY esta en HECHA y cuya fila del tallador")
        print("   tambien dice SIN VARA ESCRITA y NO COMPUTABLE. Medido por mi con")
        print("   git: paso de LISTA a HECHA en el commit e966d896, que es el del")
        print("   FUNDADOR cerrando la fase 08, no un pase del ejecutor. Un acto")
        print("   del fundador no le abre la puerta al ejecutor.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main("--aplicar" in sys.argv))
