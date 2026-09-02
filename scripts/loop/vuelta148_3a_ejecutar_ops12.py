# -*- coding: utf-8 -*-
"""vuelta148_3a_ejecutar_ops12.py . LA EJECUCION DE `OP-S-12`, SANEO MECANICO:
LAS ARISTAS QUE SE REPITEN AL RESOLVER (TAREA 3 de la vuelta 148).

QUE HACE. Por cada nodo VIVO y por cada uno de sus dos campos de arista, quita
las entradas que SOBRAN: las que, tras resolver la cadena de alias, apuntan a un
destino que YA aparece en la misma lista. De cada grupo SOBREVIVE UNA, en la
POSICION de la primera aparicion del grupo, y CUAL sobrevive se elige por
preferencia: primero el id CANONICO (el que ya es el destino resuelto), luego el
primero que sea un nodo VIVO, y solo si no hay ninguno, el primero.

ESA PREFERENCIA NO ES UN ADORNO Y NO LA DEDUJE YO: LA CAZO GATE 0. La primera
version se quedaba siempre con la primera, y como el motivo dominante de estas
duplicadas es "el id nuevo mas su alias" (922 de 925 por la propia ficha),
cuando el alias iba delante se conservaba el ALIAS y se borraba la referencia
viva. Gate 0 cayo con dos fantasmas, nodos activos cuya unica entrada quedaba
deprecada. Ver el docstring de `depurar` y
docs/loop/SALIDA_V148_3A_GATE0_TRAS_OPS12.txt.

QUE NO TOCA, y es literal de la ficha:
  - el mismo destino en `nodos_previos` Y en `nodos_siguientes` NO es duplicado,
    es ida y vuelta, y decidir eso es otra operacion;
  - la AUTO-ARISTA (destino igual al propio nodo) es `OP-S-07`: aqui se deja
    intacta y no se cuenta, para no inflar dos cifras con lo mismo.
  - los nodos DEPRECADOS no se tocan.

DONDE ESCRIBE. En `dataset/nodos/*.json`, que es la fuente de la que
`run_phase1.py` recompila `master_graph.json`. Medido en esta vuelta: las listas
del fichero fuente y las del grafo son IDENTICAS, asi que la basura vive en el
fuente y ahi hay que quitarla.

EL FORMATO SE PRESERVA BYTE A BYTE. Medido en esta vuelta sobre LOS 3.853
ficheros: `json.dumps(..., ensure_ascii=False, indent=2)` mas el salto de linea
final SOLO SI el original lo tenia reproduce los 3.853 EXACTOS (2.080 con salto
final y 1.773 sin el). Se escribe solo lo que cambia y no se reformatea nada.

LA GUARDA QUE VA ANTES DE ESCRIBIR, Y ES LA VERIFICACION 2 DE LA FICHA: el
VECINDARIO RESUELTO de cada nodo (conjunto de destinos distintos, por campo)
tiene que ser IDENTICO antes y despues. Si un solo nodo cambiara de vecindario,
NO SE ESCRIBE NADA y se para: eso significaria que se borro una arista de
verdad y no una repeticion.

USO:
  python scripts/loop/vuelta148_3a_ejecutar_ops12.py            # mide, no toca
  python scripts/loop/vuelta148_3a_ejecutar_ops12.py --ejecutar # escribe
"""
import argparse
import collections
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")


def cargar_grafo():
    return json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]


def resolutor(G):
    """P.1 del banco del plan: todo conteo que toque ids pasa por el resolutor.
    Misma semantica que scripts/plan/aristas_duplicadas_tras_resolver.py."""
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        visto = set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x
    return res


def depurar(lista, nodo_id, res, vivo):
    """(lista_nueva, quitadas). De cada grupo que resuelve al mismo destino
    SOBREVIVE UNO, y CUAL sobrevive importa.

    LA REGLA INGENUA "SE QUEDA LA PRIMERA" ES INCORRECTA, Y NO LO DEDUJE: LO
    CAZO GATE 0 (vuelta 148). El motivo dominante de estas duplicadas, por la
    propia ficha, es "el id nuevo mas su alias": 922 de 925. Si en la lista el
    ALIAS va delante del id nuevo, quedarse con la primera CONSERVA EL ALIAS Y
    BORRA LA REFERENCIA VIVA. Corrido asi, Gate 0 cayo con
    "Ningun nodo ACTIVO cuya unica entrada este deprecada (valor: 2 fantasmas:
    ['comunicacion_aprendizaje_continuo', 'financiamiento_sba_exportacion'])":
    dos nodos activos se quedaron colgando de una entrada deprecada. La salida
    esta commiteada en docs/loop/SALIDA_V148_3A_GATE0_TRAS_OPS12.txt.

    LA REGLA BUENA, POR PREFERENCIA Y EN ESTE ORDEN:
      (1) el que YA ES el destino resuelto (el id canonico);
      (2) si ninguno lo es, el primero que sea un nodo VIVO del grafo;
      (3) si ninguno lo es, el primero, que es lo que habia antes.
    El superviviente se queda EN LA POSICION DE LA PRIMERA aparicion del grupo,
    para no reordenar la lista mas de lo necesario.

    La auto-arista se deja pasar SIEMPRE, sin contarla ni tocarla: es OP-S-07."""
    grupos = {}          # destino -> lista de literales, en orden
    orden = []           # destinos en orden de primera aparicion
    nueva = []
    for x in lista:
        d = res(x)
        if d == nodo_id:          # auto-arista: es OP-S-07, aqui no se toca
            nueva.append(("auto", x))
            continue
        if d not in grupos:
            grupos[d] = []
            orden.append(d)
            nueva.append(("grupo", d))
        grupos[d].append(x)

    def preferido(d, cuales):
        for x in cuales:
            if x == d:
                return x
        for x in cuales:
            if vivo(x):
                return x
        return cuales[0]

    salida = []
    for clase, valor in nueva:
        if clase == "auto":
            salida.append(valor)
            continue
        salida.append(preferido(valor, grupos[valor]))
    # Las quitadas se cuentan POR CONTEO y no por identidad: si el mismo literal
    # aparece dos veces en la lista, comparar con `is not` dejaria fuera las dos.
    quitadas = []
    for d in orden:
        fuera = list(grupos[d])
        fuera.remove(preferido(d, grupos[d]))
        quitadas.extend((x, d) for x in fuera)
    return salida, quitadas


def vecindario_resuelto(nodo, res, nodo_id):
    """El conjunto de destinos distintos por campo. Es lo que NO puede cambiar."""
    return dict((c, frozenset(res(x) for x in (nodo.get(c) or []))) for c in CAMPOS)


def leer_fuente(nid):
    ruta = os.path.join(NODOS, "%s.json" % nid)
    if not os.path.exists(ruta):
        return None, None, None
    crudo = io.open(ruta, encoding="utf-8", newline="").read()
    return ruta, crudo, json.loads(crudo.replace("\r\n", "\n"))


def escribir_fuente(ruta, crudo_original, obj):
    """Preserva el salto de linea final tal como estaba. Devuelve el texto."""
    texto = json.dumps(obj, ensure_ascii=False, indent=2)
    if crudo_original.replace("\r\n", "\n").endswith("\n"):
        texto += "\n"
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(texto)
    return texto


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true",
                    help="escribe en dataset/nodos/ (por defecto solo mide)")
    a = ap.parse_args()

    G = cargar_grafo()
    res = resolutor(G)

    vivos = [k for k, v in G.items() if not v.get("deprecado")]
    set_vivos = set(vivos)

    def vivo(x):
        return x in set_vivos
    print("OP-S-12, SANEO MECANICO DE ARISTAS DUPLICADAS TRAS RESOLVER")
    print("nodos en el grafo: %d | vivos: %d | deprecados: %d"
          % (len(G), len(vivos), len(G) - len(vivos)))
    print("")

    cambios = []          # (nid, ruta, crudo, obj_nuevo, quitadas_por_campo)
    total_quitadas = 0
    por_campo = collections.Counter()
    por_dominio = collections.Counter()
    sin_fichero = []
    rotos = []
    autos_vistas = 0

    for nid in sorted(vivos):
        ruta, crudo, obj = leer_fuente(nid)
        if obj is None:
            sin_fichero.append(nid)
            continue
        antes = vecindario_resuelto(obj, res, nid)
        nuevo = dict(obj)
        quitadas_nodo = {}
        for campo in CAMPOS:
            lista = obj.get(campo)
            if not lista:
                continue
            autos_vistas += sum(1 for x in lista if res(x) == nid)
            depurada, quitadas = depurar(lista, nid, res, vivo)
            if quitadas:
                nuevo[campo] = depurada
                quitadas_nodo[campo] = quitadas
                por_campo[campo] += len(quitadas)
        if not quitadas_nodo:
            continue
        # LA GUARDA, ANTES DE ESCRIBIR NADA
        despues = vecindario_resuelto(nuevo, res, nid)
        if antes != despues:
            rotos.append((nid, antes, despues))
            continue
        total_quitadas += sum(len(v) for v in quitadas_nodo.values())
        por_dominio[obj.get("dominio") or "core"] += sum(len(v) for v in quitadas_nodo.values())
        cambios.append((nid, ruta, crudo, nuevo, quitadas_nodo))

    print("VERIFICACION 2 DE LA FICHA, ANTES DE ESCRIBIR: el vecindario RESUELTO de cada")
    print("nodo tiene que ser IDENTICO antes y despues.")
    if rotos:
        print("   ROJO: %d nodo(s) CAMBIAN de vecindario. NO SE ESCRIBE NADA." % len(rotos))
        for nid, antes, despues in rotos[:5]:
            print("      %s: antes %s | despues %s" % (nid, antes, despues))
        return 1
    print("   VERDE: los %d nodo(s) con duplicadas conservan su vecindario resuelto entero."
          % len(cambios))
    print("")

    print("VERIFICACION 3 DE LA FICHA: cero solape con OP-S-07 (ningun grupo tiene destino")
    print("igual al propio nodo).")
    solapes = [(nid, c, x, d) for nid, _r, _cr, _n, q in cambios
               for c, lst in q.items() for x, d in lst if d == nid]
    print("   auto-aristas VISTAS y dejadas intactas: %d" % autos_vistas)
    print("   auto-aristas QUITADAS por esta operacion: %d %s"
          % (len(solapes), "" if not solapes else solapes[:3]))
    if solapes:
        print("   ROJO: se iba a borrar una auto-arista, que es OP-S-07. NO SE ESCRIBE NADA.")
        return 1
    print("")

    if sin_fichero:
        print("AVISO: %d nodo(s) vivos del grafo sin fichero en dataset/nodos/: %s"
              % (len(sin_fichero), ", ".join(sin_fichero[:5])))
        print("")

    print("LO QUE SOBRA, MEDIDO POR ESTE INSTRUMENTO")
    print("   nodos con al menos una duplicada : %d" % len(cambios))
    print("   entradas que SOBRAN              : %d" % total_quitadas)
    for c in CAMPOS:
        print("      %-18s %d" % (c, por_campo[c]))
    print("   por dominio:")
    for d, n in por_dominio.most_common():
        print("      %-20s %d" % (d, n))
    print("")
    print("CIFRA entradas duplicadas que sobran: %d entradas" % total_quitadas)
    print("CIFRA nodos con al menos una duplicada: %d nodos" % len(cambios))
    print("")

    if not a.ejecutar:
        print("MODO MEDICION: no se escribio un solo byte. Para ejecutar, --ejecutar")
        return 0

    escritos = 0
    for nid, ruta, crudo, nuevo, _q in cambios:
        escribir_fuente(ruta, crudo, nuevo)
        escritos += 1
    print("ESCRITOS: %d fichero(s) de dataset/nodos/." % escritos)
    print("Ahora hay que recompilar el grafo con el ciclo entero de Gate 0 en su orden.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
