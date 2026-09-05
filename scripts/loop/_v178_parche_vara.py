# -*- coding: utf-8 -*-
r"""_v178_parche_vara.py . EL PARCHE QUE ANADE LA COLUMNA `CONSUMIDA` A
`scripts/loop/vuelta150_3_relectura_expediente.py` (vuelta 178, TAREA 4).

ES UN PARCHE, NO CODIGO VIVO: empieza por guion bajo, no lo ve el censo de
arneses y no entra en ninguna nomina. Cada sustitucion lleva su `assert`.

LO QUE ESTE PARCHE NO HACE, Y ES LO QUE MANDA: no toca NI UN VEREDICTO de la
vara. La vara es del fundador. Lo que se anade es UNA COLUMNA y UNA SEGUNDA
CIFRA al lado de la primera, nunca en vez de ella.
"""
import io
import os

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R = os.path.join(RAIZ, "scripts", "loop", "vuelta150_3_relectura_expediente.py")

t = io.open(R, encoding="utf-8").read().replace(chr(13) + NL, NL)
PARES = []

BLOQUE = '''NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

# LA COLUMNA `CONSUMIDA` (vuelta 178, TAREA 4). NO ES UNA EXCLUSION.
#
# POR QUE NACE, Y LA CIFRA ES DE ESTA MISMA VARA. Esta vara imprime SEIS fichas
# en LISTA sin ninguna prueba de ejecucion, y DOS de las seis estan CONSUMIDAS
# por otras: su fusion ya la ejecuto otra operacion, asi que el trabajo real son
# CUATRO. La vara no lo sabia y por eso su ultima cifra decia mas de lo que hay.
#
# QUE SE ANADE Y QUE NO. SE ANADE UNA COLUMNA. NO se excluye ninguna ficha, NO
# se toca ningun veredicto y NO se cambia ninguna cifra vieja: la cuenta final
# publica LAS DOS, "seis en LISTA sin prueba, de las cuales cuatro son trabajo
# real y dos estan consumidas por X e Y". PODAR LA CIFRA DE LA VARA SIN EL
# FUNDADOR ES LO QUE LA CASA RESERVA, y esto no lo hace.
#
# COMO SE MIDE, Y SON DOS COSAS DISTINTAS QUE VAN JUNTAS:
#
#   (1) SI ESTA CONSUMIDA: contra el GRAFO y por el resolutor de `P.1`, no
#       leyendo un acta. Una ficha esta CONSUMIDA cuando tiene DOS O MAS nodos
#       en su nomina y TODOS resuelven a UN SOLO NODO VIVO: eso significa que la
#       fusion que la ficha describe YA OCURRIO, la haya ejecutado quien la haya
#       ejecutado. Es exactamente la medicion que hizo
#       `scripts/loop/vuelta64_consumidas.py` en la vuelta 64.
#
#   (2) POR CUAL: eso NO se puede medir contra el grafo, porque el grafo guarda
#       el resultado y no quien lo hizo. Se LEE DE LA PROPIA FICHA, buscando los
#       `id_op` que su texto nombre en la frase que lo declara, y se dice que
#       viene de ahi. Si la ficha no nombra a nadie, la columna dice CONSUMIDA
#       SIN DECIR POR QUIEN, en vez de inventar un culpable.
PATRON_ID_OP = re.compile(r"OP-[A-Z]+-[A-Z0-9]+(?:-[A-Z0-9]+)?")
MARCAS_DE_CONSUMIDA = ("ESTA FICHA ESTA CONSUMIDA", "SU FUSION YA LA EJECUTO",
                       "YA LA EJECUTO")


def mapa_de_alias(directorio=None):
    """EL RESOLUTOR DE `P.1`: {alias: destino}. Lee `dataset/nodos/`.

    `directorio` va por parametro para que el caso positivo por mutacion de esta
    columna pueda apuntarlo a uno fabricado."""
    base = directorio or NODOS
    mapa = {}
    if not os.path.isdir(base):
        return mapa
    for f in sorted(os.listdir(base)):
        if not f.endswith(".json"):
            continue
        d = json.load(io.open(os.path.join(base, f), encoding="utf-8"))
        for a in (d.get("ids_alias") or []):
            mapa[a] = d["node_id"]
    return mapa


def resolver(mapa, x):
    visto = set()
    while x in mapa and x not in visto:
        visto.add(x)
        x = mapa[x]
    return x


def vivos_del_grafo(ruta=None):
    """{id: True si el grafo lo tiene y NO esta deprecado}."""
    p = ruta or GRAFO
    if not os.path.exists(p):
        return {}
    g = json.load(io.open(p, encoding="utf-8"))["nodos"]
    return dict((k, not bool(v.get("deprecado"))) for k, v in g.items())


def texto_de_la_ficha(f):
    """TODO el texto de la ficha en una cadena. PURA."""
    trozos = []
    for k, v in f.items():
        if isinstance(v, str):
            trozos.append(v)
        elif isinstance(v, list):
            trozos.extend(x for x in v if isinstance(x, str))
    return chr(10).join(trozos)


def consumida_por(f, mapa, vivos):
    """(esta_consumida, [id_op que la ficha nombra], destino). PURA a proposito:
    recibe el mapa de alias y el diccionario de vivos, para que su caso positivo
    por mutacion pueda fabricar los dos sin tocar el repo.

    LA MEDICION Y LA ATRIBUCION VAN SEPARADAS y se devuelven las dos: la primera
    sale del grafo, la segunda de la propia ficha."""
    nodos = f.get("nodos") or []
    if len(nodos) < 2:
        return False, [], None
    destinos = {resolver(mapa, n) for n in nodos}
    if len(destinos) != 1:
        return False, [], None
    destino = list(destinos)[0]
    if not vivos.get(destino, False):
        return False, [], destino
    texto = texto_de_la_ficha(f)
    if not any(m in texto.upper() for m in MARCAS_DE_CONSUMIDA):
        nombrados = []
    else:
        trozo = texto
        for m in MARCAS_DE_CONSUMIDA:
            i = texto.upper().find(m)
            if i >= 0:
                trozo = texto[i:i + 400]
                break
        nombrados = sorted({x for x in PATRON_ID_OP.findall(trozo)
                            if x != f.get("id_op")})
    return True, nombrados, destino


'''

PARES.append(('def fichas():', BLOQUE + 'def fichas():'))

# ------------------------------------------------- LA TABLA FINAL Y SU CUENTA
VIEJO = '''    print("| id_op | fase | tipo | depende_de medido |")
    print("|---|---|---|---|")
    pendientes = 0
    for f in F:
        i = f["id_op"]
        if f["estado"] != "LISTA":
            continue
        if v1.get(i, (False,))[0] or v2[i] or v3[i][1] or v3b.get(i):
            continue
        pendientes += 1
        dep = f.get("depende_de") or []
        medido = ", ".join("%s=%s" % (d, por_id[d]["estado"] if d in por_id else "NO EXISTE")
                           for d in dep) or "(vacio)"
        print("| `%s` | %s | %s | %s |" % (i, f["fase"], f["tipo"], medido))
    print("")
    print("CONTADO: %d ficha(s) en LISTA sin ninguna prueba de ejecucion." % pendientes)'''
NUEVO = '''    # LA COLUMNA `CONSUMIDA` (vuelta 178, TAREA 4). SE ANADE, NO SE EXCLUYE:
    # LAS SEIS SIGUEN IMPRIMIENDOSE Y LA CIFRA VIEJA SIGUE PUBLICANDOSE.
    mapa_alias = mapa_de_alias()
    vivos = vivos_del_grafo()
    print("| id_op | fase | tipo | depende_de medido | consumida por |")
    print("|---|---|---|---|---|")
    pendientes = 0
    consumidas = []
    for f in F:
        i = f["id_op"]
        if f["estado"] != "LISTA":
            continue
        if v1.get(i, (False,))[0] or v2[i] or v3[i][1] or v3b.get(i):
            continue
        pendientes += 1
        dep = f.get("depende_de") or []
        medido = ", ".join("%s=%s" % (d, por_id[d]["estado"] if d in por_id else "NO EXISTE")
                           for d in dep) or "(vacio)"
        esta, nombrados, destino = consumida_por(f, mapa_alias, vivos)
        if esta:
            consumidas.append((i, nombrados, destino))
            celda = ("SI, por %s" % ", ".join("`%s`" % x for x in nombrados)) \\
                if nombrados else "SI, PERO LA FICHA NO DICE POR QUIEN"
        else:
            celda = "no"
        print("| `%s` | %s | %s | %s | %s |" % (i, f["fase"], f["tipo"], medido, celda))
    print("")
    print("CONTADO: %d ficha(s) en LISTA sin ninguna prueba de ejecucion." % pendientes)
    print("")
    print("Y LA CUENTA PUBLICA LAS DOS, NUNCA SOLO LA SEGUNDA (vuelta 178, TAREA 4):")
    print("  %d en LISTA sin prueba, de las cuales %d son TRABAJO REAL y %d estan"
          % (pendientes, pendientes - len(consumidas), len(consumidas)))
    print("  CONSUMIDAS por otras fichas.")
    for i, nombrados, destino in consumidas:
        print("     CONSUMIDA: %-20s por %-28s (sus nodos resuelven al VIVO %s)"
              % (i, ", ".join(nombrados) or "(la ficha no lo dice)", destino))
    if not consumidas:
        print("     (ninguna consumida)")
    print("  COMO SE MIDE: si esta consumida sale del GRAFO por el resolutor de P.1")
    print("  (dos o mas nodos que resuelven a UN SOLO nodo VIVO, o sea que la fusion")
    print("  que la ficha describe ya ocurrio); por CUAL sale de la propia ficha, y")
    print("  se dice, porque el grafo guarda el resultado y no quien lo hizo.")
    print("  PODAR LA CIFRA DE LA VARA SIN EL FUNDADOR ES LO QUE LA CASA RESERVA:")
    print("  las %d se siguen imprimiendo enteras y la cifra vieja no se toca."
          % pendientes)'''
PARES.append((VIEJO, NUEVO))

PARES.append(('''    print("CIFRA fichas en LISTA sin ninguna prueba: %d operaciones" % pendientes)''',
'''    print("CIFRA fichas en LISTA sin ninguna prueba: %d operaciones" % pendientes)
    print("CIFRA de esas que estan CONSUMIDAS por otra ficha: %d operaciones"
          % len(consumidas))
    print("CIFRA de esas que son TRABAJO REAL: %d operaciones"
          % (pendientes - len(consumidas)))'''))

for viejo, nuevo in PARES:
    assert viejo in t, "NO ESTA: " + viejo[:70]
    t = t.replace(viejo, nuevo, 1)

io.open(R, "w", encoding="utf-8", newline=NL).write(t)
print("PARCHES APLICADOS: %d" % len(PARES))
