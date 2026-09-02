# -*- coding: utf-8 -*-
r"""tallar_estado_de_fase.py . EL ESTADO DE UNA FASE DEJA DE SER UNA FRASE Y
PASA A SER UNA CIFRA COMPUTADA (TAREA 2.a de la vuelta 140, acta de la vuelta
139, seccion 4.1 y su escalada). Nombre estable, SIN numero de vuelta (como
tallar_cabecera_reporte.py y verificar_apertura_sellada.py): se invoca con
--fase y no se clona cada vuelta.

POR QUE NACE. La vuelta 139 publico "LA FASE 06 CIERRA SU CATALOGO" en su
cabecera y "hoy cierra" en su conclusion, y sobre esa frase pidio disparar el
pase de estado de seis operaciones. El auditor lo midio y no cerraba: el
catalogo de la fase 06 no son solo las seis fusiones, son tambien las CINCO
operaciones que la fase 04 le remitio en la vuelta 118, y esas tenian ONCE
aristas sin escribir. La racha de caidas de reporte llego a DOS y AUDITOR.md
1.2 obligo a encargar la escalada en la misma acta. La escalada literal de
EJECUTOR.md regla 1 (toda tabla tallada de su fichero) ya estaba hecha; la que
faltaba es esta: LA FRASE DE CIERRE DE UNA FASE SE COMPUTA, NO SE ESCRIBE.

QUE COMPRUEBA. Para una fase del 00_INDICE imprime UNA TABLA con, por
operacion de su catalogo: el id_op, su `estado` escrito en OPERACIONES.jsonl
(que se publica COMO CONTRASTE, nunca como veredicto), su `fase`, de donde
viene si es hija remitida y a que mesa fue remitida, y su DESTINO MEDIDO
CONTRA EL GRAFO. Cierra con una linea CIFRA y la lista NOMBRADA de las que no
cumplen.

EL CATALOGO DE UNA FASE, fijado por el auditor (acta 139, TAREA 2.a) para que
el instrumento no lo decida: son las operaciones cuyo campo `fase` es esa
fase, MAS las que otra fase le remitio POR ESCRITO. Los dos registros de
remision se LEEN DE SU FICHERO, no se teclean aqui:

  - docs/plan/00_INDICE.md, la fila que dice "enrutadas a la fase <N>": de ahi
    salen las SEIS fusiones que la fase 03 enruto a la fase 06.
  - docs/plan/04_ENLACES.md, seccion "SEGUNDA MITAD, LAS CINCO REMITIDAS A LAS
    MESAS DE LA FASE 06": de ahi salen las CINCO de la vuelta 118, con su
    mesa de destino.

Si un id remitido NO existe en OPERACIONES.jsonl, o una operacion aparece a la
vez con `fase` propia y como remitida desde otra, o hay ids duplicados en
OPERACIONES.jsonl, el instrumento CAE EN ROJO NOMBRANDOLA: fallar ruidoso,
nunca degradar en silencio (banco 9).

LAS VARAS DEL DESTINO, y de donde sale cada una:

  (1) FUSION. La escribe el encargo: "superviviente vivo con los absorbidos
      deprecados y en su ids_alias". Se aplica cuando `superviviente` es un id
      de nodo resoluble (patron de id y presente en el grafo). Absorbidos =
      `nodos` menos el superviviente.

  (2) ENLACE. La escribe el encargo: "cuantas de sus aristas_nuevas estan
      presentes hoy resolviendo por alias en las dos vistas". Se aplica cuando
      `aristas_nuevas` trae al menos un par `A -> B` parseable. Una arista
      cuenta como PRESENTE si, tras resolver los dos extremos por alias, esta
      en `nodos_siguientes` del origen O en `nodos_previos` del destino.
      Si una cadena de `aristas_nuevas` contiene "->" y NO produce ningun par,
      es ROJO nombrandola (una arista que el parser no ve es peor que ninguna).

  (3) MESA. ESTA VARA NO ESTA EN EL ENCARGO Y ES LECTURA MIA, DECLARADA AQUI Y
      MARCADA COMO DISCUTIBLE EN EL REPORTE DE LA VUELTA 140. Sale de dos
      cosas escritas: la fila 6 del 00_INDICE dice que la fase 06 "no tiene
      nada que hacer el dia de la pasada. SUS OPERACIONES HIJAS VIVEN EN LAS
      FASES 3 Y 4", y el campo `bloquea_a` de cada mesa NOMBRA a esas hijas.
      Una mesa tiene destino cumplido cuando TODAS sus hijas que estan en este
      catalogo lo tienen. Si una mesa no tiene NINGUNA hija en el catalogo, el
      destino NO SE DA POR CUMPLIDO: sale NO COMPUTABLE con sus hijas y la
      fase de cada una nombradas, para que se vea por que.

  (4) SIN VARA ESCRITA. Todo lo demas. NO HAY REGLA ESCRITA que mida contra el
      grafo el destino de una VIGENCIA, una HERRAMIENTA, un CAMPO_SUCIO, un
      RENOMBRE_CON_ALIAS, un REENCUADRE_DE_MARCO o un SANEO MECANICO, y
      EJECUTOR.md regla 5 prohibe inventarla. El instrumento NO se calla y NO
      la da por buena: sale NO COMPUTABLE, se cuenta en SIN CUMPLIR y se
      nombra en el desglose `de ellas, sin vara escrita`.

POR QUE "NO COMPUTABLE" CUENTA COMO "SIN CUMPLIR", y es la decision que mas
manda en la cifra: "destino cumplido" es una AFIRMACION, y una operacion cuyo
destino no se puede medir NO HA SIDO DEMOSTRADA cumplida. Meterla en el saco
de las cumplidas seria exactamente la degradacion silenciosa que el banco 9
prohibe, y seria ademas la especie de la caida 4.1 (una frase de cierre sin
instrumento detras). El desglose se publica al lado para que nadie confunda
"no cumplida" con "no medible".

EL CAMPO `estado` NO ES VARA DE NADA. Se imprime como columna de CONTRASTE
porque EJECUTOR.md regla 2 manda declarar la discrepancia en vez de
resolverla copiando, pero ninguna cifra de este instrumento lo mira.

USO:
  python scripts/loop/tallar_estado_de_fase.py --fase 06_MESAS
  python scripts/loop/tallar_estado_de_fase.py --fase 05_SANEO --ref <commit>
  python scripts/loop/tallar_estado_de_fase.py --fases

--ref fija el grafo Y el OPERACIONES.jsonl Y los dos registros de remision en
un commit, para poder correr sobre SUJETO CONGELADO (banco 9.10: un sujeto que
se mueve solo no prueba nada). Por defecto WORK, el arbol de trabajo.

LAS MUTACIONES viven en scripts/loop/vuelta140_2a_mutaciones.py, que importa
este modulo y muta EN MEMORIA (nunca el disco). Las tres, todas sobre cifra
COMPUTADA y nunca sobre un literal (EJECUTOR.md regla 1, "EL CASO ROJO SE
PRUEBA POR MUTACION"):
  (i)   se le quita una arista presente al grafo en memoria: "con destino
        cumplido" tiene que BAJAR y la operacion tiene que salir NOMBRADA;
  (ii)  se mete en el catalogo una remitida de mentira que no existe en
        OPERACIONES.jsonl: ROJO nombrandola;
  (iii) caso positivo sobre sujeto congelado: la fase 05, cerrada desde la
        vuelta 136.
"""
import argparse
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REL_GRAFO = "dataset/metadata/master_graph.json"
REL_OPS = "docs/plan/OPERACIONES.jsonl"
REL_INDICE = "docs/plan/00_INDICE.md"
REL_ENLACES = "docs/plan/04_ENLACES.md"

PATRON_ID_NODO = re.compile(r"^[a-z0-9_]+$")
PATRON_ARISTA = re.compile(r"([a-z0-9_]+)\s*->\s*([a-z0-9_]+)")
PATRON_OP = re.compile(r"OP-[A-Z0-9]+(?:-[A-Z0-9]+)*")


# ------------------------------------------------------------------ lectura

def leer_ruta(ref, rel):
    """Lee un fichero del arbol de trabajo (ref WORK) o de un commit."""
    if ref == "WORK":
        with io.open(os.path.join(RAIZ, rel), encoding="utf-8") as f:
            return f.read()
    r = subprocess.run(["git", "show", "%s:%s" % (ref, rel)], cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO (arnes): no se pudo leer %s en %s" % (rel, ref))
    return r.stdout.decode("utf-8")


def cargar_grafo(ref="WORK"):
    return json.loads(leer_ruta(ref, REL_GRAFO))["nodos"]


def cargar_ops(ref="WORK"):
    ops = []
    for linea in leer_ruta(ref, REL_OPS).splitlines():
        if linea.strip():
            ops.append(json.loads(linea))
    return ops


# --------------------------------------------------------------- remisiones

def leer_remisiones(fase, ref="WORK"):
    """Los dos registros de remision, LEIDOS DE SU FICHERO. Devuelve
    {id_op: {'de': <fase origen o None>, 'a': <mesa o None>, 'fuente': <cita>}}.

    NO se teclea ninguna nomina aqui: si un registro se reescribe, este
    instrumento lo sigue."""
    rem = {}
    numero = fase.split("_")[0].lstrip("0") or "0"

    # (1) 00_INDICE.md: la fila "enrutadas a la fase <N>".
    patron_fila = re.compile(r"enrutadas a la fase 0*%s\b" % re.escape(numero))
    for i, linea in enumerate(leer_ruta(ref, REL_INDICE).splitlines(), 1):
        if patron_fila.search(linea):
            for x in PATRON_OP.findall(linea):
                rem.setdefault(x, {"de": None, "a": None,
                                   "fuente": "%s:%d" % (REL_INDICE, i)})

    # (2) 04_ENLACES.md: la tabla de la seccion de las remitidas a las mesas.
    texto = leer_ruta(ref, REL_ENLACES).splitlines()
    cabecera = re.compile(r"LAS CINCO REMITIDAS A LAS MESAS DE LA FASE 0*%s\b" % re.escape(numero))
    dentro = False
    for i, linea in enumerate(texto, 1):
        if cabecera.search(linea):
            dentro = True
            continue
        if not dentro:
            continue
        if linea.startswith("|"):
            celdas = [c.strip().strip("`") for c in linea.strip().strip("|").split("|")]
            if len(celdas) >= 2 and PATRON_OP.fullmatch(celdas[0] or ""):
                mesa = celdas[1] if PATRON_OP.fullmatch(celdas[1] or "") else None
                rem[celdas[0]] = {"de": None, "a": mesa,
                                  "fuente": "%s:%d" % (REL_ENLACES, i)}
        elif linea.strip().startswith("#") or linea.strip().startswith("**SEGUNDA"):
            if rem:
                dentro = False
    return rem


# ----------------------------------------------------------------- catalogo

def construir_catalogo(fase, ops, remisiones, fallos):
    """Las de `fase` propia MAS las remitidas por escrito. ROJO nombrando si
    algo no se puede resolver sin decidir."""
    por_id = {}
    for o in ops:
        x = o.get("id_op")
        if x in por_id:
            fallos.append("%s aparece DOS VECES en %s: catalogo ambiguo" % (x, REL_OPS))
        por_id[x] = o

    propias = [o["id_op"] for o in ops if o.get("fase") == fase]
    catalogo = list(propias)

    for x, meta in sorted(remisiones.items()):
        if x not in por_id:
            fallos.append("%s esta REMITIDO a la fase %s por %s y NO EXISTE en %s: "
                          "no se puede medir su destino" % (x, fase, meta["fuente"], REL_OPS))
            continue
        if x in propias:
            fallos.append("%s tiene fase propia %s Y aparece remitido a la fase %s por %s: "
                          "no se puede resolver a que fase pertenece sin decidir"
                          % (x, fase, fase, meta["fuente"]))
            continue
        meta["de"] = por_id[x].get("fase")
        catalogo.append(x)

    return catalogo, por_id


# --------------------------------------------------------------- resolutor

def resolver_de(nodos):
    """El resolutor de alias de la casa (P.1), igual que en
    verificar_aristas_vivas.py y verificar_fusion_ops09.py."""
    alias = {}
    for nid, n in nodos.items():
        if n.get("deprecado"):
            continue
        for x in (n.get("ids_alias") or []):
            alias[x] = nid

    def resolver(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x
    return resolver


def vivo(n):
    return n is not None and not n.get("deprecado")


def arista_presente(nodos, resolver, origen, destino):
    """Presente si, tras resolver los dos extremos por alias, esta en
    nodos_siguientes del origen O en nodos_previos del destino."""
    o, d = resolver(origen), resolver(destino)
    no, nd = nodos.get(o), nodos.get(d)
    if not vivo(no) or not vivo(nd) or o == d:
        return False, o, d
    if any(resolver(x) == d for x in (no.get("nodos_siguientes") or [])):
        return True, o, d
    if any(resolver(x) == o for x in (nd.get("nodos_previos") or [])):
        return True, o, d
    return False, o, d


# ------------------------------------------------------------------ destino

def pares_de_aristas(op, fallos):
    pares = []
    for s in (op.get("aristas_nuevas") or []):
        hallados = PATRON_ARISTA.findall(s)
        if "->" in s and not hallados:
            fallos.append("%s: una cadena de aristas_nuevas trae '->' y el parser no "
                          "saca ningun par: %s" % (op.get("id_op"), s[:120]))
        pares.extend(hallados)
    return pares


def destino_de_fusion(op, nodos, fallos):
    sup = op.get("superviviente")
    absorbidos = [x for x in (op.get("nodos") or []) if x != sup]
    n_sup = nodos.get(sup)
    if not vivo(n_sup):
        return False, "superviviente %s NO esta vivo hoy" % sup
    alias_sup = set(n_sup.get("ids_alias") or [])
    faltas = []
    for x in absorbidos:
        n = nodos.get(x)
        if n is None:
            faltas.append("%s no existe en el grafo" % x)
            continue
        if not n.get("deprecado"):
            faltas.append("%s NO esta deprecado" % x)
        if x not in alias_sup:
            faltas.append("%s no esta en ids_alias de %s" % (x, sup))
    if faltas:
        return False, "%d absorbido(s) OK de %d; %s" % (
            len(absorbidos) - len({f.split()[0] for f in faltas}), len(absorbidos),
            "; ".join(faltas))
    return True, "superviviente %s vivo, %d absorbido(s) deprecado(s) y en ids_alias" % (
        sup, len(absorbidos))


def destino_de_enlace(pares, nodos, resolver):
    presentes = 0
    faltan = []
    for o, d in pares:
        ok, ro, rd = arista_presente(nodos, resolver, o, d)
        if ok:
            presentes += 1
        else:
            faltan.append("%s -> %s" % (ro, rd))
    cumplido = presentes == len(pares) and len(pares) > 0
    razon = "%d de %d presentes" % (presentes, len(pares))
    if faltan:
        razon += "; faltan: " + ", ".join(faltan)
    return cumplido, razon


def es_mesa(op):
    return (op.get("tipo") or "").upper().startswith("MESA ADJUDICADA")


def medir(fase, ops, nodos, remisiones=None, ref="WORK"):
    """Devuelve (filas, cifra, fallos). Cada fila es un dict con todo lo que
    la tabla imprime. Ninguna celda se teclea fuera de aqui."""
    fallos = []
    if remisiones is None:
        remisiones = leer_remisiones(fase, ref)
    catalogo, por_id = construir_catalogo(fase, ops, remisiones, fallos)
    if not catalogo:
        fallos.append("la fase %s no tiene NINGUNA operacion en su catalogo: "
                      "o el nombre de fase no existe o el fichero cambio" % fase)
    resolver = resolver_de(nodos)
    en_catalogo = set(catalogo)

    # Primera pasada: las que no son mesa, para que las mesas puedan leerlas.
    veredicto = {}
    filas = {}
    for x in catalogo:
        op = por_id[x]
        if es_mesa(op):
            continue
        sup = op.get("superviviente")
        pares = pares_de_aristas(op, fallos)
        if sup and PATRON_ID_NODO.match(sup) and sup in nodos:
            vara = "FUSION"
            cumplido, razon = destino_de_fusion(op, nodos, fallos)
        elif pares:
            vara = "ENLACE"
            cumplido, razon = destino_de_enlace(pares, nodos, resolver)
        else:
            vara = "SIN VARA ESCRITA"
            cumplido = None
            razon = ("no hay regla escrita que mida contra el grafo el destino de "
                     "un tipo %s (ni superviviente resoluble ni aristas_nuevas)"
                     % (op.get("tipo") or "?"))
        veredicto[x] = cumplido
        filas[x] = dict(id_op=x, fase=op.get("fase"), estado=op.get("estado"),
                        tipo=op.get("tipo"), vara=vara, cumplido=cumplido, razon=razon,
                        remitida=remisiones.get(x))

    for x in catalogo:
        op = por_id[x]
        if not es_mesa(op):
            continue
        hijas = [h for h in (op.get("bloquea_a") or []) if h in en_catalogo and h != x]
        fuera = [(h, (por_id.get(h) or {}).get("fase", "no existe"))
                 for h in (op.get("bloquea_a") or []) if h not in en_catalogo]
        if not hijas:
            cumplido = None
            razon = ("NINGUNA de sus hijas esta en el catalogo de esta fase; "
                     "bloquea_a: %s" % (", ".join("%s (%s)" % (h, f) for h, f in fuera) or "vacio"))
        else:
            sin = [h for h in hijas if veredicto.get(h) is not True]
            cumplido = not sin
            razon = "%d de %d hijas del catalogo con destino cumplido" % (len(hijas) - len(sin), len(hijas))
            if sin:
                razon += "; sin cumplir: " + ", ".join(sorted(sin))
            if fuera:
                razon += "; hijas FUERA del catalogo: " + ", ".join("%s (%s)" % (h, f) for h, f in fuera)
        veredicto[x] = cumplido
        filas[x] = dict(id_op=x, fase=op.get("fase"), estado=op.get("estado"),
                        tipo=op.get("tipo"), vara="MESA", cumplido=cumplido, razon=razon,
                        remitida=remisiones.get(x))

    orden = sorted(catalogo, key=lambda x: (filas[x]["vara"] != "MESA", x))
    lista = [filas[x] for x in orden]
    cumplidas = [f["id_op"] for f in lista if f["cumplido"] is True]
    sin_cumplir = [f["id_op"] for f in lista if f["cumplido"] is not True]
    sin_vara = [f["id_op"] for f in lista if f["cumplido"] is None]
    cifra = dict(catalogo=len(lista), cumplido=len(cumplidas),
                 sin_cumplir=len(sin_cumplir), sin_vara=len(sin_vara),
                 nombres_sin_cumplir=sin_cumplir, nombres_sin_vara=sin_vara)
    return lista, cifra, fallos


# ---------------------------------------------------------------- impresion

def _celda(x):
    return (x or "").replace("|", "/")


def imprimir(fase, lista, cifra, fallos, ref="WORK"):
    print("ESTADO DE LA FASE %s | REF: %s" % (fase, ref))
    print("El campo `estado` va como CONTRASTE, no como veredicto: ninguna cifra lo mira.")
    print("")
    print("| id_op | fase escrita | estado (contraste) | vara | remitida: de / a | destino medido contra el grafo | veredicto |")
    print("|---|---|---|---|---|---|---|")
    for f in lista:
        rem = f["remitida"]
        if rem:
            celda_rem = "de %s / a %s (%s)" % (rem.get("de") or "?", rem.get("a") or "la fase, sin mesa nombrada", rem.get("fuente"))
        else:
            celda_rem = "no remitida"
        v = "CUMPLIDO" if f["cumplido"] is True else ("SIN CUMPLIR" if f["cumplido"] is False else "NO COMPUTABLE")
        print("| %s | %s | %s | %s | %s | %s | %s |" % (
            f["id_op"], _celda(f["fase"]), _celda(f["estado"]), f["vara"],
            _celda(celda_rem), _celda(f["razon"]), v))
    print("")
    print("CIFRA: operaciones del catalogo: %d | con destino cumplido: %d | sin cumplir: %d "
          "| de ellas, sin vara escrita: %d" % (cifra["catalogo"], cifra["cumplido"],
                                                cifra["sin_cumplir"], cifra["sin_vara"]))
    print("SIN CUMPLIR (%d): %s" % (len(cifra["nombres_sin_cumplir"]),
                                    ", ".join(cifra["nombres_sin_cumplir"]) or "ninguna"))
    print("SIN VARA ESCRITA (%d): %s" % (len(cifra["nombres_sin_vara"]),
                                         ", ".join(cifra["nombres_sin_vara"]) or "ninguna"))
    if fallos:
        print("")
        print("ROJO, %d cosa(s) no cuadran:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fase")
    ap.add_argument("--ref", default="WORK")
    ap.add_argument("--fases", action="store_true", help="lista las fases que el fichero trae")
    a = ap.parse_args()

    ops = cargar_ops(a.ref)
    if a.fases or not a.fase:
        vistas = []
        for o in ops:
            if o.get("fase") not in vistas:
                vistas.append(o.get("fase"))
        print("FASES EN %s (%s):" % (REL_OPS, a.ref))
        for f in sorted(x for x in vistas if x):
            print("   %s (%d operacion(es) con fase propia)"
                  % (f, sum(1 for o in ops if o.get("fase") == f)))
        return 0 if a.fases else 2

    nodos = cargar_grafo(a.ref)
    lista, cifra, fallos = medir(a.fase, ops, nodos, ref=a.ref)
    return imprimir(a.fase, lista, cifra, fallos, ref=a.ref)


if __name__ == "__main__":
    raise SystemExit(main())
