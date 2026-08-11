# -*- coding: utf-8 -*-
"""contar_nombre.py - contador de menciones por nombre para censos de familia.

NACE DE UN ERROR REPETIDO TRES VECES. El barrido por nombre hecho a mano fallo
en los puestos 637, 683 y 719 del cribado intra-dominio: dos veces prediciendo
gemelos que no lo eran y una vez contando de menos una familia entera porque sus
miembros no compartian la palabra del identificador. La regla que sale de ahi
esta en el banco: EL CENSO POR NOMBRE SE CUENTA POR SCRIPT.

QUE HACE. Busca uno o varios terminos como SUBCADENA en todo el texto util de
cada nodo del grafo (identificador, titulo, pasos, resumen teorico, condiciones
de activacion y entregable esperado), normalizando antes: minusculas, sin
acentos, y guion y guion bajo tratados como espacio, de modo que
`seis_herramientas`, `seis-herramientas` y `Seis Herramientas` cuentan igual.

QUE NO HACE. No decide nada. Un nodo que menciona un termino NO es por eso
miembro de una familia: la pertenencia se decide leyendo. Este script dice
DONDE MIRAR y cuantos son, que es exactamente lo que el conteo a mano hacia mal.

SOLO LECTURA. No escribe nada, nunca toca el grafo.

Uso:
  python scripts/contar_nombre.py "seis herramientas"
  python scripts/contar_nombre.py "customer discovery" "customer development"
  python scripts/contar_nombre.py --dominio core --campos titulo,pasos "cinco porques"
  python scripts/contar_nombre.py --todos "milk run"      (incluye deprecados)
"""
import json, sys, unicodedata, argparse
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

GRAFO = Path("dataset/metadata/master_graph.json")
CAMPOS = {
    "id": lambda k, v: k,
    "titulo": lambda k, v: v.get("titulo_concepto") or "",
    "pasos": lambda k, v: " ".join(v.get("pasos_accionables") or []),
    "resumen": lambda k, v: v.get("resumen_teorico") or "",
    "condiciones": lambda k, v: " ".join(v.get("condiciones_activacion") or []),
    "entregable": lambda k, v: v.get("entregable_esperado") or "",
}


def norm(s):
    """minusculas, sin acentos, guion y guion bajo como espacio, espacios colapsados."""
    if not isinstance(s, str):
        s = str(s)
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.lower().replace("_", " ").replace("-", " ")
    return " ".join(s.split())


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("terminos", nargs="*", help="uno o mas terminos a contar")
    ap.add_argument("--dominio", default=None, help="filtra por dominio, por ejemplo core")
    ap.add_argument("--campos", default=",".join(CAMPOS), help="campos a mirar, separados por coma")
    ap.add_argument("--todos", action="store_true", help="incluye tambien los nodos deprecados")
    ap.add_argument("--solo-id", action="store_true", help="atajo: busca solo en el identificador")
    a = ap.parse_args()

    terminos = [t for t in a.terminos if t and t.strip()]
    assert terminos, "FALLA RUIDOSA: no diste ningun termino que contar."
    campos = ["id"] if a.solo_id else [c.strip() for c in a.campos.split(",") if c.strip()]
    for c in campos:
        assert c in CAMPOS, "FALLA RUIDOSA: campo %r desconocido. Validos: %s" % (c, ", ".join(CAMPOS))
    assert GRAFO.exists(), "FALLA RUIDOSA: no encuentro %s" % GRAFO

    G = json.load(open(GRAFO, encoding="utf-8"))["nodos"]
    T = [(t, norm(t)) for t in terminos]

    filas = []
    for k, v in G.items():
        if a.dominio and v.get("dominio") != a.dominio:
            continue
        dep = bool(v.get("deprecado"))
        if dep and not a.todos:
            continue
        texto = {c: norm(CAMPOS[c](k, v)) for c in campos}
        por_termino, donde = {}, set()
        for t, tn in T:
            n = sum(texto[c].count(tn) for c in campos)
            if n:
                por_termino[t] = n
                donde |= {c for c in campos if tn in texto[c]}
        if por_termino:
            filas.append((k, dep, v.get("dominio"), sum(por_termino.values()), por_termino, sorted(donde)))

    filas.sort(key=lambda f: (-f[3], f[0]))
    vivos = [f for f in filas if not f[1]]
    deps = [f for f in filas if f[1]]

    print("TERMINOS: %s" % " | ".join(terminos))
    print("CAMPOS:   %s%s" % (", ".join(campos), "" if not a.dominio else "   DOMINIO: %s" % a.dominio))
    print("=" * 100)
    for etiqueta, grupo in (("VIVOS", vivos), ("DEPRECADOS", deps)):
        if not grupo:
            continue
        print("--- %s: %d nodos ---" % (etiqueta, len(grupo)))
        for k, dep, dom, tot, por, donde in grupo:
            detalle = ", ".join("%s x%d" % (t, n) for t, n in por.items())
            print("  %-52s %-12s x%-3d  [%s]  %s" % (k[:52], dom or "?", tot, ", ".join(donde), detalle))
    print("=" * 100)
    print("TOTAL vivos: %d | deprecados: %d | menciones vivas: %d"
          % (len(vivos), len(deps), sum(f[3] for f in vivos)))
    print("El script dice DONDE MIRAR y cuantos son. La pertenencia a una familia se decide LEYENDO.")


if __name__ == "__main__":
    main()
