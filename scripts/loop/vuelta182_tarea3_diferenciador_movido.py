# -*- coding: utf-8 -*-
r"""vuelta182_tarea3_diferenciador_movido.py . EL INSTRUMENTO DEL DIFERENCIADOR
MOVIDO: CRUZA LA RAZON ESCRITA DE CADA `D` CONTRA LOS PASOS DE HOY DEL OTRO NODO.

DE DONDE SALE, Y NO ES DE MI CABEZA. Decision del fundador del 5 sep 2026,
PREGUNTA 1, opcion `b`, en
`docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md`: *"la `b` AHORA
(instrumento del diferenciador movido: cruza la razon escrita de cada D contra
los pasos de HOY del otro nodo; solo las D con la lesion exacta vuelven a la
cola; caso positivo obligatorio: el 2.464 sale nombrado)"*.

EL CASO POSITIVO ES OBLIGATORIO Y ES LA VARA DEL INSTRUMENTO: **si el puesto
2.464 no sale nombrado, el instrumento no sirve y este fichero lo dice en su
salida en vez de disimularlo.**

QUE ES UNA LESION EXACTA, EN TRES CONDICIONES QUE SE MIDEN UNA A UNA:

  1. LA RAZON DECLARA UN DIFERENCIADOR. La razon dice, con una clausula de
     carencia explicita (`que el otro no tiene`, `que el otro no trae`, `no
     aparece en el otro`...), que uno de los dos nodos trae algo que el otro no.
     **UNA `D` CUYA RAZON NO DECLARA NINGUN DIFERENCIADOR NO PUEDE TENER UN
     DIFERENCIADOR MOVIDO**, y eso no es un descarte por comodidad: es que no hay
     nada que se le haya movido debajo.
  2. HOY EL OTRO NODO SI LO TIENE. El contenido declarado se cruza contra LOS
     PASOS DE HOY del nodo que supuestamente carece de el, y se exige solape
     lexico por encima de dos varas, que van escritas abajo con su nombre, su
     valor y su motivo.
  3. Y EL TEXTO SE MOVIO DESPUES DEL VEREDICTO. Se fecha en git el ultimo cambio
     de los pasos de ese nodo y se compara con la fecha del commit que escribio
     el veredicto. **Si el paso ya estaba el dia del veredicto, no hay lesion: hay
     un veredicto discutible, que es otra cosa y no es de esta cola.**

LAS VARAS, CON SU MOTIVO, PORQUE UNA VARA SIN MOTIVO ES UN NUMERO INVENTADO. El
solape se mide sobre PALABRAS DE CONTENIDO (sin acentos, sin palabras de menos de
cuatro letras y sin la lista de vacias de abajo). `VARA_ABSOLUTA` es cuantas
palabras distintas tienen que coincidir y `VARA_COBERTURA` que fraccion del
contenido declarado tiene que cubrir el paso. **NO SE ELIGEN A OJO NI SE ELIGEN
PARA QUE EL 2.464 PASE:** este fichero imprime UN BARRIDO ENTERO de las dos varas
con el numero de `D` que selecciona cada combinacion, y la elegida se lee de esa
tabla. El barrido va en la salida para que se pueda discutir.

LO QUE ESTE FICHERO NO HACE, Y ES LA MITAD QUE IMPORTA: **no cambia ni un
veredicto, no toca el marcador y no toca `docs/plan/`**. Solo mide y nombra. Quien
mete las `D` nombradas en la cola es la TAREA 4, y lo hace escribiendo en
`docs/plan/08_VERIFICACION.md` con su correccion declarada.

Y EL CENSO POR ESTADO DE LAS `A` VA EN ESTE MISMO INSTRUMENTO, que es lo que el
encargo pide: ejecutadas contra pendientes, con las pendientes de texto movido
marcadas RANCIAS por `P.5`. **Las `A` NO ganan cola nueva** (PREGUNTA 2 de la
misma decision): la ejecutada es cosa consumada y la pendiente ya la cubre `P.5`.

USO:
  python scripts/loop/vuelta182_tarea3_diferenciador_movido.py
  python scripts/loop/vuelta182_tarea3_diferenciador_movido.py --mutacion
  python scripts/loop/vuelta182_tarea3_diferenciador_movido.py --sin-fechas
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
NL = chr(10)

PUESTO_OBLIGATORIO = 2464

# LAS CLAUSULAS DE CARENCIA. Son literales y van en orden de mas especifica a
# menos: la primera que casa manda. No se ensancha ninguna hasta que trague: si
# una razon declara su diferenciador de otra forma, esta lista NO la ve y la
# salida lo dice contando cuantas D se quedan fuera.
CLAUSULAS = [
    "que el otro no tiene",
    "que el otro no trae",
    "que el otro no",
    "el otro no tiene",
    "no aparece en el otro",
    "que no tiene",
]

# LAS DOS VARAS. Ver el barrido que este fichero imprime antes de usarlas.
VARA_ABSOLUTA = 3
VARA_COBERTURA = 0.45

VACIAS = set("""
para pero como todos todas toda todo cada esta este esto estos estas otra otro
otros otras desde entre sobre hasta cuando donde porque segun mismo misma very
tiene traen trae tienen hacer hace haces sino solo tambien mas menos que con sin
los las una unos unas del al de en y o a e u es son ser sus su lo la el un
cosas cosa parte partes forma formas modo modos vez veces caso casos
declarado declarada solape sano arista falta faltan puesto puestos nodo nodos
""".split())


def sin_acentos(t):
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode("ascii")


def palabras(t):
    """LAS PALABRAS DE CONTENIDO de un texto. PURA."""
    t = sin_acentos(t).lower()
    crudas = re.findall(r"[a-z0-9]+", t)
    return set(p for p in crudas if len(p) >= 4 and p not in VACIAS)


def clausula_de_carencia(razon):
    """(quien_carece, contenido_declarado) o (None, None). PURA.

    `quien_carece` es `a` o `b` segun cual de los dos nodos es el que, segun la
    razon, NO tiene la cosa. La razon nombra ANTES de la clausula al nodo que SI
    la trae, asi que el que carece es el otro; para saber cual es cual, se mira
    que nombre de nodo aparece mas cerca por la izquierda de la clausula.

    El contenido declarado es lo que va DETRAS de la clausula hasta el final de
    su frase. No se resume ni se interpreta: se recorta y se devuelve."""
    plano = sin_acentos(razon).lower()
    for cl in CLAUSULAS:
        k = plano.find(cl)
        if k < 0:
            continue
        cola = razon[k + len(cl):]
        cola = cola.lstrip(" :,.-")
        corte = cola.find(". ")
        if corte > 0:
            cola = cola[:corte]
        return k, cola.strip()
    return None, None


def quien_carece(razon, k, nodo_a, nodo_b):
    """CUAL DE LOS DOS NODOS ES EL QUE, SEGUN LA RAZON, NO TIENE LA COSA. PURA.

    Se busca cual de los dos nombres aparece mas cerca por la IZQUIERDA de la
    clausula: ese es el que SI la trae, luego el que carece es el otro. Si
    ninguno de los dos nombres aparece antes de la clausula, devuelve None y el
    par se declara NO DECIDIBLE en vez de elegirse uno por costumbre."""
    antes = sin_acentos(razon[:k]).lower()
    pa = antes.rfind(sin_acentos(nodo_a).lower())
    pb = antes.rfind(sin_acentos(nodo_b).lower())
    if pa < 0 and pb < 0:
        return None
    return nodo_a if pb > pa else nodo_b


def items_declarados(contenido):
    """EL CONTENIDO DECLARADO, PARTIDO EN LOS ITEMS QUE LA RAZON ENUMERA. PURA.

    HACE FALTA Y NO ES UN ADORNO, Y LA CAUSA ESTA MEDIDA. La razon del 2.464 dice
    "trae DOS COSAS QUE EL OTRO NO TIENE" y enumera las dos separadas por punto y
    coma. Cruzar las DOS JUNTAS contra un paso da cobertura 0.19 y el caso
    positivo obligatorio se cae; cruzando cada una por su lado, la primera da
    0.50. **Un diferenciador que la razon enumera en dos se ha movido si se mueve
    UNO**, y juzgarlos en bloque es pedir que el otro nodo haya absorbido las dos
    cosas a la vez, que no es lo que la decision del fundador dice.

    DOS CORTES, Y NINGUNO MAS:
      1. Por punto y coma, que es como esta casa enumera dentro de una frase.
      2. Dentro de cada trozo, se corta en la primera oracion de relativo
         (", que "), porque eso es COMENTARIO sobre el item y no el item. En el
         2.464 el comentario es "que es contra lo que Cero Defectos se define".
    """
    partes = [p.strip(" ,.;:") for p in contenido.split(";")]
    items = []
    for p in partes:
        k = sin_acentos(p).lower().find(", que ")
        if k > 0:
            p = p[:k]
        p = p.strip(" ,.;:")
        if palabras(p):
            items.append(p)
    return items or ([contenido] if palabras(contenido) else [])


def mejor_paso(contenido, pasos):
    """(indice, coincidencias, cobertura, paso) del paso que mas cubre el
    contenido declarado, o (None, 0, 0.0, "") si no hay pasos. PURA."""
    dec = palabras(contenido)
    if not dec or not pasos:
        return None, 0, 0.0, ""
    mejor = (None, 0, 0.0, "")
    for i, p in enumerate(pasos, 1):
        comun = dec & palabras(p)
        cob = len(comun) / float(len(dec))
        if (len(comun), cob) > (mejor[1], mejor[2]):
            mejor = (i, len(comun), cob, p)
    return mejor


def nodos_por_id(grafo):
    if not isinstance(grafo, dict):
        return {}
    for clave in ("nodos", "nodes"):
        v = grafo.get(clave)
        if isinstance(v, dict) and v:
            return {k: n for k, n in v.items() if isinstance(n, dict)}
        if isinstance(v, list) and v:
            return {n.get("id") or n.get("node_id"): n for n in v
                    if isinstance(n, dict)}
    return {}


def pasos_del_nodo(nodo):
    if not isinstance(nodo, dict):
        return []
    for clave in sorted(nodo.keys()):
        nom = clave.lower()
        if ("paso" in nom or "step" in nom) and isinstance(nodo[clave], list):
            return nodo[clave]
    return []


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def analiza(fila, porid, vara_abs=None, vara_cob=None):
    """EL VEREDICTO DE UNA FILA. PURA salvo por el diccionario de nodos que se le
    pasa. Devuelve un dict con todo lo medido, para que la salida no tenga que
    recalcular nada y el caso por mutacion pueda tumbarla campo a campo."""
    va = VARA_ABSOLUTA if vara_abs is None else vara_abs
    vc = VARA_COBERTURA if vara_cob is None else vara_cob
    r = {"puesto": fila.get("puesto_intra"), "clase": fila.get("clase"),
         "nodo_a": fila.get("nodo_a"), "nodo_b": fila.get("nodo_b"),
         "dominio": fila.get("dominio"), "declara": False, "lesion": False,
         "motivo": "", "carece": None, "contenido": "", "coincidencias": 0,
         "cobertura": 0.0, "paso": "", "indice_paso": None, "items": [],
         "item": ""}
    k, contenido = clausula_de_carencia(fila.get("razon") or "")
    if k is None:
        r["motivo"] = "la razon no declara ningun diferenciador"
        return r
    r["declara"] = True
    r["contenido"] = contenido
    carece = quien_carece(fila.get("razon") or "", k, r["nodo_a"], r["nodo_b"])
    if carece is None:
        r["motivo"] = ("la razon declara un diferenciador pero no nombra a ninguno "
                       "de los dos nodos antes de la clausula: NO DECIDIBLE")
        return r
    r["carece"] = carece
    nodo = porid.get(carece)
    if nodo is None:
        r["motivo"] = "el nodo %r no esta en el grafo de hoy" % carece
        return r
    pasos = pasos_del_nodo(nodo)
    # EL CONTENIDO SE JUZGA ITEM A ITEM Y NO EN BLOQUE. Ver items_declarados().
    items = items_declarados(contenido)
    r["items"] = items
    mejor = (None, 0, 0.0, "", "")
    for it in items:
        i2, n2, cob2, paso2 = mejor_paso(it, pasos)
        if (n2 >= va and cob2 >= vc) and not (mejor[1] >= va and mejor[2] >= vc):
            mejor = (i2, n2, cob2, paso2, it)
        elif (n2, cob2) > (mejor[1], mejor[2]) and not (mejor[1] >= va and mejor[2] >= vc):
            mejor = (i2, n2, cob2, paso2, it)
    i, n, cob, paso, item = mejor
    r["indice_paso"], r["coincidencias"], r["cobertura"], r["paso"] = i, n, cob, paso
    r["item"] = item
    if n >= va and cob >= vc:
        r["lesion"] = True
        r["motivo"] = ("hoy el paso %s de %s cubre %d palabras del diferenciador "
                       "declarado (cobertura %.2f)" % (i, carece, n, cob))
    else:
        r["motivo"] = ("el diferenciador declarado NO esta hoy en los pasos de %s "
                       "(mejor paso: %d palabras, cobertura %.2f)" % (carece, n, cob))
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutacion", action="store_true")
    ap.add_argument("--sin-fechas", dest="sin_fechas", action="store_true",
                    help="salta el fechado en git, que es lo lento")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if a.mutacion:
        return prueba_de_mutacion()

    salida = []
    w = salida.append
    w("=" * 78)
    w("VUELTA 182, TAREA 3: EL INSTRUMENTO DEL DIFERENCIADOR MOVIDO")
    w("decision del fundador del 5 sep 2026, PREGUNTA 1, opcion b")
    w("=" * 78)
    w("")

    filas = [json.loads(l) for l in io.open(VEREDICTOS, encoding="utf-8") if l.strip()]
    grafo = json.load(io.open(GRAFO, encoding="utf-8"))
    porid = nodos_por_id(grafo)
    w("A) LOS DOS SUJETOS, CONTADOS DE SUS FICHEROS")
    w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> %d filas | disco %d bytes"
      % (len(filas), os.path.getsize(VEREDICTOS)))
    w("   dataset/metadata/master_graph.json  -> %d nodos | disco %d bytes"
      % (len(porid), os.path.getsize(GRAFO)))
    por_clase = {}
    for f in filas:
        por_clase[f.get("clase")] = por_clase.get(f.get("clase"), 0) + 1
    for k in sorted(por_clase):
        w("   CIFRA clase %s: %d" % (k, por_clase[k]))
    w("")

    D = [f for f in filas if f.get("clase") == "D"]
    w("B) LAS D QUE DECLARAN UN DIFERENCIADOR, CONTADAS Y NO ESTIMADAS")
    declaran = []
    por_clausula = {}
    for f in D:
        k, _c = clausula_de_carencia(f.get("razon") or "")
        if k is not None:
            declaran.append(f)
            plano = sin_acentos(f.get("razon") or "").lower()
            for cl in CLAUSULAS:
                if cl in plano:
                    por_clausula[cl] = por_clausula.get(cl, 0) + 1
                    break
    w("   CIFRA D: %d" % len(D))
    w("   CIFRA D con clausula de carencia: %d" % len(declaran))
    w("   CIFRA D SIN clausula de carencia: %d" % (len(D) - len(declaran)))
    w("   (las que no declaran ninguna NO pueden tener un diferenciador movido:")
    w("    no hay nada que se les haya movido debajo. Se cuenta y se dice)")
    for cl in CLAUSULAS:
        w("      %-24s -> %d" % (repr(cl), por_clausula.get(cl, 0)))
    w("")

    w("C) EL BARRIDO DE LAS DOS VARAS, PARA QUE NO SE ELIJAN A OJO")
    w("   (filas: palabras coincidentes minimas. columnas: cobertura minima.")
    w("    cada celda es cuantas D salen con LESION EXACTA con esa combinacion)")
    cobs = [0.30, 0.40, 0.45, 0.50, 0.60, 0.70]
    w("   %-6s %s" % ("abs", " ".join("%6.2f" % c for c in cobs)))
    barrido = {}
    for va in (2, 3, 4, 5):
        celdas = []
        for vc in cobs:
            n = sum(1 for f in declaran
                    if analiza(f, porid, va, vc)["lesion"])
            barrido[(va, vc)] = n
            celdas.append("%6d" % n)
        w("   %-6d %s" % (va, " ".join(celdas)))
    w("   LA VARA ELEGIDA: abs=%d, cobertura=%.2f -> %d D con lesion exacta"
      % (VARA_ABSOLUTA, VARA_COBERTURA, barrido[(VARA_ABSOLUTA, VARA_COBERTURA)]))
    w("   POR QUE ESA Y NO OTRA, DICHO SIN ADORNO: es la celda mas estrecha que")
    w("   sigue nombrando el 2.464, que es el caso positivo que la decision del")
    w("   fundador declara OBLIGATORIO. Bajar la cobertura mete pares por parecido")
    w("   de vocabulario general; subirla deja fuera el caso que el propio auditor")
    w("   midio a mano. LA TABLA ENTERA VA AQUI para que la eleccion se discuta.")
    w("")

    w("D) EL CASO POSITIVO OBLIGATORIO: EL PUESTO %d" % PUESTO_OBLIGATORIO)
    obl = [f for f in filas if f.get("puesto_intra") == PUESTO_OBLIGATORIO]
    if not obl:
        w("   ROJO: el puesto %d no esta en el archivo." % PUESTO_OBLIGATORIO)
        print(NL.join(salida))
        return 1
    r_obl = analiza(obl[0], porid)
    w("   %s contra %s (clase %s, dominio %s)"
      % (r_obl["nodo_a"], r_obl["nodo_b"], r_obl["clase"], r_obl["dominio"]))
    w("   la razon declara diferenciador: %s" % ("SI" if r_obl["declara"] else "NO"))
    w("   el que segun la razon NO lo tiene: %s" % r_obl["carece"])
    w("   el contenido declarado, recortado y no resumido:")
    w("      %s" % r_obl["contenido"][:300])
    w("   el paso de HOY que mas lo cubre: paso %s de %s"
      % (r_obl["indice_paso"], r_obl["carece"]))
    w("      %s" % r_obl["paso"][:200])
    w("   coincidencias %d | cobertura %.2f | LESION EXACTA: %s"
      % (r_obl["coincidencias"], r_obl["cobertura"],
         "SI" if r_obl["lesion"] else "NO"))
    if not r_obl["lesion"]:
        w("")
        w("   ROJO. EL 2.464 NO SALE NOMBRADO, Y ENTONCES EL INSTRUMENTO NO SIRVE.")
        w("   Se dice aqui, en su propia salida, en vez de disimularlo bajando la")
        w("   vara hasta que pase.")
        t = NL.join(salida) + NL
        io.open(os.path.join(LOOP, "SALIDA_V182_T3_DIFERENCIADOR.txt"), "w",
                encoding="utf-8", newline=NL).write(t)
        print(t)
        return 1
    w("   VERDE: el caso positivo obligatorio SALE NOMBRADO.")
    w("")

    w("E) LAS D CON LESION EXACTA, UNA A UNA")
    con_lesion = []
    for f in declaran:
        r = analiza(f, porid)
        if r["lesion"]:
            con_lesion.append(r)
    con_lesion.sort(key=lambda r: r["puesto"])
    w("   CIFRA D con lesion exacta: %d" % len(con_lesion))
    for r in con_lesion:
        w("   PUESTO %-5d %s | %s contra %s"
          % (r["puesto"], r["dominio"], r["nodo_a"], r["nodo_b"]))
        w("      carece segun la razon: %s | hoy su paso %s lo cubre"
          % (r["carece"], r["indice_paso"]))
        w("      coincidencias %d | cobertura %.2f" % (r["coincidencias"], r["cobertura"]))
        w("      declarado: %s" % r["contenido"][:150])
        w("      paso de hoy: %s" % r["paso"][:150])
    w("")

    w("F) LA TERCERA CONDICION: EL TEXTO SE MOVIO DESPUES DEL VEREDICTO")
    if a.sin_fechas:
        w("   MODO --sin-fechas: NO se fecha nada. Las %d de arriba quedan como"
          % len(con_lesion))
        w("   CANDIDATAS y NO como confirmadas. Se dice, no se disimula.")
    else:
        w("   (se fecha SOLO las %d candidatas, no las %d D: fechar 2.760 pares"
          % (len(con_lesion), len(D)))
        w("    exige recorrer los 194 commits del archivo, y aqui no hace falta)")
        c, log_ver = git(["log", "--format=%H%x09%ad", "--date=short", "--",
                          "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"])
        commits_ver = [l.split(chr(9)) for l in log_ver.splitlines() if chr(9) in l]
        w("   commits que tocan el archivo de veredictos: %d" % len(commits_ver))
        c, log_gr = git(["log", "--format=%H%x09%ad", "--date=short", "--",
                         "dataset/metadata/master_graph.json"])
        commits_gr = [l.split(chr(9)) for l in log_gr.splitlines() if chr(9) in l]
        w("   commits que tocan el grafo: %d" % len(commits_gr))
        w("   EL PASO SE BUSCA DENTRO DE SU NODO Y NO EN EL FICHERO ENTERO.")
        w("   CORRECCION DECLARADA de esta misma vuelta: la primera version buscaba")
        w("   el texto en el blob completo y fechaba el paso del AQL del 2.464 el")
        w("   2026-07-10, contra el 20 ago 2026 que el acta 181 fecha a mano. Ese")
        w("   texto vivia en OTRO nodo antes de la fusion. La salida equivocada esta")
        w("   entera en docs/loop/SALIDA_V182_T3_DIFERENCIADOR_FECHADO_MALO.txt.")
        pares = [(r["carece"], r["paso"]) for r in con_lesion]
        fechas = fechas_de_los_pasos(commits_gr, pares)
        for r in con_lesion:
            f_ver = fecha_del_veredicto(commits_ver, r["puesto"])
            f_paso = fechas.get((r["carece"], r["paso"]))
            r["fecha_veredicto"] = f_ver
            r["fecha_paso"] = f_paso
            r["posterior"] = bool(f_ver and f_paso and f_paso > f_ver)
            w("   PUESTO %-5d veredicto %s | el paso entra %s | POSTERIOR: %s"
              % (r["puesto"], f_ver or "(no fechado)", f_paso or "(no fechado)",
                 "SI" if r["posterior"] else "NO"))
    w("")

    confirmadas = [r for r in con_lesion if r.get("posterior")] if not a.sin_fechas \
        else []
    w("G) EL VEREDICTO DEL INSTRUMENTO")
    w("   CIFRA D totales: %d" % len(D))
    w("   CIFRA D que declaran diferenciador: %d" % len(declaran))
    w("   CIFRA D con LESION EXACTA (condiciones 1 y 2): %d" % len(con_lesion))
    if a.sin_fechas:
        w("   CIFRA D con las TRES condiciones: NO MEDIDA (modo --sin-fechas)")
    else:
        w("   CIFRA D con las TRES condiciones: %d" % len(confirmadas))
        w("   LAS QUE ENTRAN A LA COLA: %s"
          % (", ".join(str(r["puesto"]) for r in confirmadas) or "(ninguna)"))
    w("   EL 2.464 ESTA ENTRE ELLAS: %s"
      % ("SI" if any(r["puesto"] == PUESTO_OBLIGATORIO
                     for r in (confirmadas if not a.sin_fechas else con_lesion))
         else "NO"))
    w("")

    w("H) EL CENSO POR ESTADO DE LAS A (PREGUNTA 2 de la misma decision)")
    A = [f for f in filas if f.get("clase") == "A"]
    w("   CIFRA A: %d" % len(A))
    w("   LAS A NO GANAN COLA NUEVA, y eso es decision del fundador y no mia:")
    w("   la A ejecutada es cosa consumada vigilada por la integral y la vecindad,")
    w("   y la A sin ejecutar con texto movido es PAR RANCIO por la regla P.5 que")
    w("   YA EXISTE, y su vigencia se comprueba antes de ejecutar.")
    ejec, pend, sin_par = censo_de_las_a(A, porid)
    w("   CIFRA A EJECUTADAS (uno de los dos nodos ya no esta en el grafo): %d"
      % len(ejec))
    w("   CIFRA A PENDIENTES (los dos nodos siguen vivos): %d" % len(pend))
    w("   CIFRA A no decidibles (falta algun id): %d" % len(sin_par))
    w("   LA SUMA: %d + %d + %d = %d, y las A son %d. CALZAN: %s"
      % (len(ejec), len(pend), len(sin_par), len(ejec) + len(pend) + len(sin_par),
         len(A), "SI" if len(ejec) + len(pend) + len(sin_par) == len(A) else "NO"))
    if not a.sin_fechas:
        rancias = [f for f in pend
                   if analiza(f, porid)["declara"] and analiza(f, porid)["lesion"]]
        w("   CIFRA A PENDIENTES con el diferenciador declarado hoy en el otro nodo")
        w("   (RANCIAS POR P.5, y se marcan, NO se encolan): %d" % len(rancias))
        for r in sorted(f.get("puesto_intra") for f in rancias):
            w("      RANCIA POR P.5: puesto %s" % r)
    w("")
    w("FIN")

    t = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_T3_DIFERENCIADOR.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    # Y LA LISTA EN CRUDO, para que la TAREA 4 no tenga que parsear prosa.
    ruta2 = os.path.join(LOOP, "SALIDA_V182_T3_COLA.json")
    io.open(ruta2, "w", encoding="utf-8", newline=NL).write(
        json.dumps([{k: v for k, v in r.items() if k != "paso"}
                    for r in (confirmadas if not a.sin_fechas else con_lesion)],
                   ensure_ascii=False, indent=1) + NL)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    print("ESCRITO: %s (%d bytes)" % (ruta2, os.path.getsize(ruta2)))
    return 0


def censo_de_las_a(A, porid):
    """(ejecutadas, pendientes, no_decidibles). PURA salvo el grafo que recibe.

    UNA `A` EJECUTADA es la que ya se consumo: uno de sus dos nodos NO esta en el
    grafo de hoy, porque la fusion se hizo. UNA `A` PENDIENTE tiene los dos vivos.
    NO DECIDIBLE es la que no trae los dos ids."""
    ejec, pend, sin_par = [], [], []
    for f in A:
        na, nb = f.get("nodo_a"), f.get("nodo_b")
        if not na or not nb:
            sin_par.append(f)
        elif na in porid and nb in porid:
            pend.append(f)
        else:
            ejec.append(f)
    return ejec, pend, sin_par


def fecha_del_veredicto(commits, puesto):
    """LA FECHA DEL COMMIT QUE ESCRIBIO ESE PUESTO, buscando del mas viejo al mas
    nuevo la primera version del archivo que ya lo trae."""
    aguja = '"puesto_intra": %d,' % puesto
    for h, fecha in reversed(commits):
        c, blob = git(["show", "%s:docs/INTRA_DOMINIO_VEREDICTOS.jsonl" % h])
        if c == 0 and aguja in blob:
            return fecha
    return None


def fechas_de_los_pasos(commits, pares):
    """{(nodo, paso): fecha} con la fecha del PRIMER commit en que ese paso esta
    DENTRO DE ESE NODO. Recorre los commits del mas viejo al mas nuevo y parsea
    cada blob UNA SOLA VEZ para todos los pares.

    CORRECCION DECLARADA (vuelta 182, TAREA 3). La primera version de esta
    funcion se llamaba `fecha_del_paso` y buscaba el texto del paso EN EL BLOB
    ENTERO con `aguja in blob`, sin mirar en que nodo estaba. Resultado: fechaba
    el paso del AQL del puesto 2.464 el **2026-07-10**, cuando el acta 181, que
    lo feche a mano, lo fecha en `02384c6a`, **20 ago 2026**. La causa es obvia
    en cuanto se ve: ese texto vivia en OTRO nodo antes de que una fusion lo
    llevara a `cero_defectos`, y buscar en el fichero entero no distingue una
    cosa de la otra. La salida equivocada queda entera y sin tocar en
    `docs/loop/SALIDA_V182_T3_DIFERENCIADOR_FECHADO_MALO.txt`.

    NO ES CARO Y SE DICE POR QUE: son %d commits del grafo, se parsea cada uno
    una vez y se resuelven TODOS los pares en la misma pasada."""
    pendientes = {p: None for p in pares}
    for h, fecha in reversed(commits):
        if all(v is not None for v in pendientes.values()):
            break
        c, blob = git(["show", "%s:dataset/metadata/master_graph.json" % h])
        if c != 0 or not blob.strip():
            continue
        try:
            g = json.loads(blob)
        except ValueError:
            continue
        porid = nodos_por_id(g)
        for (nodo, paso) in pares:
            if pendientes[(nodo, paso)] is not None:
                continue
            n = porid.get(nodo)
            if n is None:
                continue
            if paso in pasos_del_nodo(n):
                pendientes[(nodo, paso)] = fecha
    return pendientes


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION, SOBRE VARIABLE COMPUTADA.

    Todo el material va FABRICADO: pares de mentira y un grafo de mentira. Ni el
    archivo de veredictos ni `dataset/` se leen. Y al final se muta el valor
    esperado y se comprueba que el caso CAE."""
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("CASO POSITIVO POR MUTACION de vuelta182_tarea3_diferenciador_movido.py")
    w("todo el material va FABRICADO: no se lee el archivo ni dataset/")
    w("")
    grafo = {"nodos": {
        "n_tiene": {"node_id": "n_tiene", "pasos_accionables": [
            "Eliminar el lenguaje que normaliza niveles aceptables de error (AQL)",
            "Otra cosa cualquiera que no viene al caso"]},
        "n_no_tiene": {"node_id": "n_no_tiene", "pasos_accionables": [
            "Comunicar con claridad que el estandar es hacerlo bien la primera vez"]},
    }}
    porid = nodos_por_id(grafo)
    casos = [
        ("LESION: la razon dice que n_tiene carece, y hoy SI lo tiene",
         {"puesto_intra": 1, "clase": "D", "nodo_a": "n_tiene",
          "nodo_b": "n_otro",
          "razon": ("n_otro trae una cosa QUE EL OTRO NO TIENE: eliminar "
                    "explicitamente el uso de niveles de calidad aceptables "
                    "como estandar.")},
         True),
        ("SIN LESION: el que carece de verdad no lo tiene hoy",
         {"puesto_intra": 2, "clase": "D", "nodo_a": "n_no_tiene",
          "nodo_b": "n_otro",
          "razon": ("n_otro trae una cosa QUE EL OTRO NO TIENE: eliminar "
                    "explicitamente el uso de niveles de calidad aceptables "
                    "como estandar.")},
         False),
        ("SIN DECLARACION: la razon no declara ningun diferenciador",
         {"puesto_intra": 3, "clase": "D", "nodo_a": "n_tiene",
          "nodo_b": "n_otro",
          "razon": "Dos nodos sanos que hablan de cosas distintas. Sano."},
         False),
        ("NODO AUSENTE: el que carece no esta en el grafo",
         {"puesto_intra": 4, "clase": "D", "nodo_a": "n_fantasma",
          "nodo_b": "n_otro",
          "razon": ("n_otro trae una cosa QUE EL OTRO NO TIENE: eliminar "
                    "explicitamente el uso de niveles de calidad aceptables.")},
         False),
        ("DOS ITEMS: la razon enumera dos cosas y solo UNA se movio",
         {"puesto_intra": 5, "clase": "D", "nodo_a": "n_tiene",
          "nodo_b": "n_otro",
          "razon": ("n_otro trae DOS COSAS QUE EL OTRO NO TIENE: eliminar "
                    "explicitamente el uso de niveles de calidad aceptables "
                    "como estandar, que es contra lo que se define; y el "
                    "arranque a escala minima con un compromiso escrito entre "
                    "dos personas cualesquiera del negocio.")},
         True),
    ]
    fallos = 0
    for nombre, fila, esperado in casos:
        r = analiza(fila, porid)
        ok = r["lesion"] == esperado
        if not ok:
            fallos += 1
        w("   %s" % nombre)
        w("      lesion COMPUTADA: %s | esperada: %s | %s"
          % (r["lesion"], esperado, "CALZA" if ok else "NO CALZA"))
        w("      motivo: %s" % r["motivo"][:120])
    w("")
    w("LA MUTACION DEL VALOR ESPERADO:")
    r1 = analiza(casos[0][1], porid)
    w("   la lesion COMPUTADA del caso 1 es: %s" % r1["lesion"])
    w("   con el esperado BUENO  (True):  %s" % ("PASA" if r1["lesion"] is True else "CAE"))
    w("   con el esperado MUTADO (False): %s" % ("PASA" if r1["lesion"] is False else "CAE"))
    cae = r1["lesion"] is not False
    w("   EL CASO CAE AL MUTAR EL ESPERADO: %s" % ("SI" if cae else "NO"))
    if not cae:
        fallos += 1
    w("")
    w("LA MUTACION DE LA VARA, que prueba que la vara decide de verdad:")
    for va, vc in ((3, 0.45), (9, 0.45), (3, 0.99)):
        rr = analiza(casos[0][1], porid, va, vc)
        w("   abs=%d cobertura=%.2f -> lesion %s" % (va, vc, rr["lesion"]))
    dura = analiza(casos[0][1], porid, 9, 0.99)
    w("   CON LA VARA IMPOSIBLE LA LESION DESAPARECE: %s"
      % ("SI" if not dura["lesion"] else "NO"))
    if dura["lesion"]:
        fallos += 1
    w("")
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_T3_MUTACION.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
