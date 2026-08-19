# -*- coding: utf-8 -*-
"""vuelta43_cierre_opd06.py - EL CIERRE DE VUELTA SOBRE OP-D-06, MEDIDO.

ESTRICTAMENTE DE SOLO LECTURA. No escribe un solo nodo.

EXISTE POR LA REGLA 1 DE EJECUTOR.md, cuarto renglon: LA TABLA SE IMPRIME, NO SE
TECLEA. Todo lo que sale de aqui se lee de dataset/nodos, de
docs/INTRA_DOMINIO_VEREDICTOS.jsonl y de docs/plan/OPERACIONES.jsonl, y se pega
ENTERO en el reporte y en el registro.

QUE CONTESTA, que son los cuatro puntos del cierre de la operacion:

  (1) EL RECOMPUTO DEL CIERRE TRANSITIVO sobre los nodos de OP-D-06: la
      componente de cada acto por la relacion gemelo (banco 9.24, cierre
      transitivo sobre las A del archivo), medida HOY y no al corte del 2117.
      Si alguna componente crecio, el acto ya no es de dos y hay que PARAR.
  (2) LOS PARES DE LA OPERACION RELEIDOS CONTRA SU SUPERVIVIENTE: por cada acto,
      su clase hoy, si sus dos nodos siguen vivos o uno esta deprecado con
      alias, y si el resolutor devuelve al superviviente.
  (3) LA VERIFICACION PUNTO POR PUNTO de la lista `verificacion` de OP-D-06 en
      OPERACIONES.jsonl, cada punto con lo que se puede medir al lado.
  (4) EL ESTADO AL CIERRE de los nodos de la operacion: censo, enlaces y cola.

Uso: python scripts/loop/vuelta43_cierre_opd06.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
COLA = os.path.join(RAIZ, "docs", "COSTURAS_INTERNAS.jsonl")
CAMPOS = ("nodos_previos", "nodos_siguientes")

# LOS NUEVE ACTOS, leidos de la nota de OPERACIONES.jsonl y NO tecleados aqui:
# el puesto es la llave y los dos nodos se leen del archivo de veredictos.
PUESTOS = [285, 331, 341, 344, 361, 392, 494, 711, 969]


def cargar_nodos():
    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.loads(io.open(os.path.join(NODOS, nombre), encoding="utf-8").read())
            todos[d["node_id"]] = d
    return todos


def cargar_veredictos():
    filas = []
    for l in io.open(VER, encoding="utf-8"):
        l = l.strip()
        if l:
            filas.append(json.loads(l))
    return filas


def main():
    todos = cargar_nodos()
    vers = cargar_veredictos()
    por_puesto = dict((v["puesto_intra"], v) for v in vers)

    # resolutor: id -> id vivo, siguiendo ids_alias
    alias = {}
    for nid, d in todos.items():
        for a in (d.get("ids_alias") or []):
            alias[a] = nid

    def resolver(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x

    def vivo(nid):
        d = todos.get(nid)
        return bool(d) and not (d.get("deprecado") or d.get("deprecated"))

    print("=" * 78)
    print("EL CIERRE DE OP-D-06, MEDIDO HOY CONTRA EL ARCHIVO Y EL GRAFO")
    print("=" * 78)

    # ---------------------------------------------------------------
    print()
    print("### (1) EL RECOMPUTO DEL CIERRE TRANSITIVO, sobre las A del archivo HOY")
    print("  Banco 9.24: una familia es el CIERRE TRANSITIVO de la relacion gemelo.")
    print("  Se construye con las A VIGENTES de docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
    print("  medidas HOY, no al corte del puesto 2117.")
    print()
    ady = {}
    n_a = 0
    for v in vers:
        if v.get("clase") != "A":
            continue
        n_a += 1
        a, b = resolver(v["nodo_a"]), resolver(v["nodo_b"])
        ady.setdefault(a, set()).add(b)
        ady.setdefault(b, set()).add(a)
    print("  pares de clase A vigentes en el archivo hoy: %d" % n_a)
    print()

    def componente(sem):
        pila, visto = [sem], set()
        while pila:
            x = pila.pop()
            if x in visto:
                continue
            visto.add(x)
            for y in ady.get(x, ()):
                if y not in visto:
                    pila.append(y)
        return visto

    print("  %-7s %-62s %s" % ("puesto", "el par del acto", "componente hoy"))
    crecidos = []
    for p in PUESTOS:
        v = por_puesto.get(p)
        if not v:
            print("  %-7d NO ESTA EN EL ARCHIVO" % p)
            continue
        a, b = v["nodo_a"], v["nodo_b"]
        ra, rb = resolver(a), resolver(b)
        comp = componente(ra) | componente(rb)
        comp = set(c for c in comp if c)
        marca = "de DOS" if len(comp) <= 2 else "CRECIO a %d" % len(comp)
        if v.get("clase") != "A":
            marca = "%s (clase %s hoy, ya no aporta arista)" % (
                "de DOS" if len(comp) <= 2 else "CRECIO a %d" % len(comp), v.get("clase"))
        if len(comp) > 2:
            crecidos.append((p, sorted(comp)))
        print("  %-7d %-62s %s" % (p, "%s con %s" % (a, b), marca))
        if len(comp) > 2:
            print("          miembros: %s" % ", ".join(sorted(comp)))
    print()
    print("  GUARDA: actos cuya componente CRECIO por encima de dos: %d" % len(crecidos))
    if not crecidos:
        print("  LOS NUEVE SIGUEN SIENDO DE DOS, medido hoy. Ninguno crecio.")

    # ---------------------------------------------------------------
    print()
    print("### (2) LOS PARES DE LA OPERACION, RELEIDOS CONTRA SU SUPERVIVIENTE")
    print()
    print("  %-7s %-4s %-44s %-10s %-44s %s"
          % ("puesto", "cl", "nodo A", "estado A", "nodo B", "estado B"))
    hechos = 0
    for p in PUESTOS:
        v = por_puesto.get(p)
        if not v:
            continue
        a, b = v["nodo_a"], v["nodo_b"]

        def estado(nid):
            if nid not in todos:
                return "NO EXISTE"
            if vivo(nid):
                return "VIVO"
            r = resolver(nid)
            return "DEPR->%s" % ("OK" if vivo(r) and r != nid else "ROTO")
        ea, eb = estado(a), estado(b)
        if "DEPR" in ea or "DEPR" in eb:
            hechos += 1
        print("  %-7d %-4s %-44s %-10s %-44s %s"
              % (p, v.get("clase"), a, ea, b, eb))
    print()
    print("  actos con una fusion ya ejecutada (uno de los dos deprecado con alias sano): %d de %d"
          % (hechos, len(PUESTOS)))

    # ---------------------------------------------------------------
    print()
    print("### (3) LA VERIFICACION DE OP-D-06, PUNTO POR PUNTO")
    print()
    op = None
    for l in io.open(OPS, encoding="utf-8"):
        d = json.loads(l)
        if d.get("id_op") == "OP-D-06":
            op = d
            break
    for i, punto in enumerate(op["verificacion"], 1):
        print("  %d. %s" % (i, punto))
    print()
    print("  estado declarado en OPERACIONES.jsonl: %s | fecha_corte: %s"
          % (op.get("estado"), op.get("fecha_corte")))
    print("  nodos declarados en la nomina: %d" % len(op.get("nodos") or []))
    faltan = [n for n in (op.get("nodos") or []) if n not in todos]
    print("  nodos de la nomina AUSENTES del grafo: %d %s"
          % (len(faltan), faltan if faltan else ""))

    # ---------------------------------------------------------------
    print()
    print("### (4) EL ESTADO AL CIERRE, recomputado (regla 1)")
    print()
    f = v_ = d_ = e = 0
    for nid, d in todos.items():
        f += 1
        if d.get("deprecado") or d.get("deprecated"):
            d_ += 1
        else:
            v_ += 1
        for campo in CAMPOS:
            e += len(d.get(campo) or [])
    print("  ficheros    : %d" % f)
    print("  vivos       : %d" % v_)
    print("  deprecados  : %d" % d_)
    print("  enlaces     : %d (previos mas siguientes)" % e)
    cola = sum(1 for l in io.open(COLA, encoding="utf-8") if l.strip())
    print("  cola de costuras: %d nodos sobre %d activos (%.1f por ciento)"
          % (cola, v_, 100.0 * cola / v_))
    marcador = {}
    for v in vers:
        marcador[v.get("clase")] = marcador.get(v.get("clase"), 0) + 1
    print("  marcador    : n %d | %s | tasa de A %.1f por ciento"
          % (len(vers),
             " ".join("%s %d" % (k, marcador[k]) for k in sorted(marcador)),
             100.0 * marcador.get("A", 0) / len(vers)))

    print()
    print("=" * 78)
    print("FIN DEL CIERRE MEDIDO")
    return 0


if __name__ == "__main__":
    sys.exit(main())
