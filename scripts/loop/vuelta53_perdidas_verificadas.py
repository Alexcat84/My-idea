# -*- coding: utf-8 -*-
"""vuelta53_perdidas_verificadas.py . LAS TRES BUSQUEDAS QUE LA REGLA 9 DEL
EJECUTOR OBLIGA A CORRER ANTES DE DECLARAR UNA PERDIDA.

"Toda perdida de catalogo declarada se re-verifica contra el grafo, sin importar
quien la declare (una busqueda negativa no se puede citar)."

Las tres de esta vuelta, cada una con su motivo:

  MBO      . el acto 17 depreca critica_gestion_por_objetivos, cuyo titulo es el
             unico sitio donde los puestos 2477 y 2488 dicen que vive el
             ACRONIMO MBO. Antes de declarar la perdida hay que mirar el grafo
             entero: titulo, resumen, pasos, condiciones y entregable de TODOS
             los nodos VIVOS.
  PARETO   . el acto 19 depreca analisis_pareto, el titulo general del
             instrumento. Antes de declarar la perdida de nombre hay que ver
             que titulos vivos siguen llevando la palabra.
  COLEMAN  . el puesto 811 (par mixto del acto 6, clase B) escribe una
             CONDICION DE CONTEO: "la familia de los datos del cliente de
             Coleman ya lleva CUATRO nodos vistos... hay que contarla antes de
             decidir". Aqui se cuenta: los nodos vivos de la fuente Coleman que
             tocan la ficha del cliente, y TODOS los veredictos que los tocan
             entre si, con su clase.

ESTRICTAMENTE DE SOLO LECTURA. Imprime.

Uso: python scripts/loop/vuelta53_perdidas_verificadas.py <MBO|PARETO|COLEMAN>
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

CAMPOS = ("titulo_concepto", "resumen_teorico", "entregable_esperado", "etiqueta_arbol")
LISTAS = ("pasos_accionables", "condiciones_activacion")


def cargar():
    out = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
            out[d["node_id"]] = d
    return out


def texto(d):
    partes = [str(d.get(c) or "") for c in CAMPOS]
    for c in LISTAS:
        partes.extend(str(x) for x in (d.get(c) or []))
    return " \n ".join(partes)


def vivo(d):
    return not (d.get("deprecado") or d.get("deprecated"))


def main():
    modo = (sys.argv[1] if len(sys.argv) > 1 else "MBO").upper()
    sys.stdout.reconfigure(encoding="utf-8")
    todos = cargar()
    vivos = {k: v for k, v in todos.items() if vivo(v)}
    print("=" * 78)
    print("BUSQUEDA %s SOBRE EL GRAFO ENTERO" % modo)
    print("nodos: %d ficheros, %d vivos" % (len(todos), len(vivos)))
    print("=" * 78)
    print()

    if modo == "MBO":
        pat = re.compile(r"\bMBO\b")
        hits = [(k, d) for k, d in vivos.items() if pat.search(texto(d))]
        print("nodos VIVOS con el acronimo MBO como palabra entera: %d" % len(hits))
        for k, d in sorted(hits):
            print("  %-52s %s" % (k, d.get("titulo_concepto")))
        print()
        pat2 = re.compile(r"[Gg]esti[oó]n [Pp]or [Oo]bjetivos")
        hits2 = [(k, d) for k, d in vivos.items() if pat2.search(texto(d))]
        print("nodos VIVOS con la denominacion en castellano GESTION POR OBJETIVOS: %d" % len(hits2))
        for k, d in sorted(hits2):
            print("  %-52s %s" % (k, d.get("titulo_concepto")))

    elif modo == "PARETO":
        hits = [(k, d) for k, d in vivos.items()
                if "pareto" in str(d.get("titulo_concepto") or "").lower()]
        print("nodos VIVOS con PARETO en el TITULO: %d" % len(hits))
        for k, d in sorted(hits):
            print("  %-52s %s" % (k, d.get("titulo_concepto")))
        print()
        hits2 = [(k, d) for k, d in vivos.items() if "pareto" in texto(d).lower()]
        print("nodos VIVOS que nombran PARETO en cualquier campo: %d" % len(hits2))
        for k, d in sorted(hits2):
            print("  %-52s %s" % (k, d.get("titulo_concepto")))

    elif modo == "COLEMAN":
        fam = [k for k, d in vivos.items()
               if "coleman" in str(d.get("fuente") or "").lower()]
        print("nodos VIVOS de la fuente Coleman: %d" % len(fam))
        clave = re.compile(r"crm|cliente|customer", re.I)
        ficha = sorted(k for k in fam if clave.search(texto(vivos[k])))
        print("de ellos, los que nombran CRM, cliente o customer: %d" % len(ficha))
        print()
        nombrados = ["conexion_personal_emocional", "seguimiento_informacion_cliente",
                     "investigar_datos_cliente", "personalizacion_investigacion_prospecto"]
        print("LOS CUATRO QUE EL PUESTO 811 NOMBRA, y su estado hoy:")
        for k in nombrados:
            d = todos.get(k)
            print("  %-52s %s" % (k, "VIVO" if d and vivo(d) else ("DEPRECADO" if d else "NO EXISTE")))
        print()
        V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
        s = set(nombrados)
        pares = [r for r in V if r["nodo_a"] in s and r["nodo_b"] in s]
        print("TODOS LOS PARES ENTRE ESOS CUATRO, leidos del archivo (cobertura %d de 6):"
              % len(pares))
        for r in sorted(pares, key=lambda x: x["puesto_intra"]):
            print("  puesto %-6d %s  %-46s %s"
                  % (r["puesto_intra"], r["clase"], r["nodo_a"], r["nodo_b"]))
        faltan = []
        for i in range(len(nombrados)):
            for j in range(i + 1, len(nombrados)):
                a, b = nombrados[i], nombrados[j]
                if not any({r["nodo_a"], r["nodo_b"]} == {a, b} for r in pares):
                    faltan.append((a, b))
        print()
        print("PARES DE LA FAMILIA SIN LEER: %d" % len(faltan))
        for a, b in faltan:
            print("  %s contra %s" % (a, b))
    else:
        print("modo desconocido")
        return 1

    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
