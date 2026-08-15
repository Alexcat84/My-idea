# -*- coding: utf-8 -*-
"""vuelta33_acto_opd02.py

SUCESOR DECLARADO de scripts/loop/vuelta32_acto_opd02.py. DE SOLO LECTURA: no
funde, no escribe y no decide. Mide las mismas tres cosas, digito a digito, para
que las dos corridas sigan siendo comparables, Y CORRIGE UNA DE ELLAS.

QUE CAMBIA, y va declarado porque cambiar un instrumento sin declararlo es lo que
la regla 2 del EJECUTOR.md prohibe:

  EL DETECTOR DE GANADOR EN LA RAZON DE UN PAR A.

  El de la vuelta 32 preguntaba `"gana" not in razon.lower()`. Es un SUBSTRING, y
  el substring `gana` vive dentro de `ganar`, `ganancia`, `ganado`. En el puesto
  526 la razon dice *saltarse la validacion por GANAR TIEMPO*, y el detector leyo
  ahi un ganador que no existe. De ahi salio la cifra publicada *DOS de los tres
  pares A no nombran ganador*, cuando la medicion buena da TRES de tres.

  EL DETECTOR NUEVO busca un VOCABULARIO DE ADJUDICACION con frontera de palabra,
  no un trozo de letra suelto. Y el vocabulario va escrito aqui arriba, entero,
  para que se pueda discutir en vez de adivinar.

LIMITE DECLARADO, para que nadie le atribuya al verde lo que no mide: esto sigue
siendo una busqueda LEXICA, no un lector de espanol. Una razon puede adjudicar sin
usar ninguna de estas palabras (por ejemplo *el segundo se queda con todo*), y este
detector la daria por no adjudicada. POR ESO EL SCRIPT IMPRIME LA RAZON ENTERA de
cada par A: la vara final es la lectura, y la lectura necesita el texto delante.
Esa es la misma disciplina del verificador de mapas, que tambien declara su limite.

Uso: python scripts/loop/vuelta33_acto_opd02.py
"""
import itertools
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

MARCAS = ["voc", "voice_of_customer", "voz_del_cliente"]

# EL VOCABULARIO DE ADJUDICACION, entero y con frontera de palabra. Sale de leer
# como el archivo escribe una adjudicacion cuando la escribe: las formas del verbo
# ganar en tercera persona, el sustantivo, las formas de sobrevivir, y las dos
# figuras con las que P.8 y el banco 9.3 nombran al que manda.
VOCABULARIO = [
    r"\bgana\b", r"\bgano\b", r"\bganan\b", r"\bganador\b", r"\bganadora\b",
    r"\bsobrevive\b", r"\bsobreviven\b", r"\bsobrevivio\b",
    r"\bsuperviviente\b", r"\bsupervivientes\b",
    r"\bla madre\b", r"\bdoctrina general\b", r"\bes hijo\b", r"\bhijo suyo\b",
    r"\babsorbe\b", r"\bse queda con\b",
]
RE_VOCABULARIO = re.compile("|".join(VOCABULARIO), re.IGNORECASE)

# El detector VIEJO, conservado para poder publicar las dos corridas y declarar la
# diferencia en vez de resolverla sustituyendo (EJECUTOR.md regla 2).
def detector_viejo(razon):
    return "gana" in razon.lower()


def detector_nuevo(razon):
    return RE_VOCABULARIO.findall(razon)


def vivo(d):
    return not d.get("deprecado") and not d.get("deprecated")


def main():
    ops = {}
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                o = json.loads(linea)
                ops[o["id_op"]] = o
    nomina = ops["OP-D-02"]["nodos"]

    vs = [json.loads(l) for l in open(VER, encoding="utf-8") if l.strip()]
    por_par = {}
    for v in vs:
        por_par[frozenset((v["nodo_a"], v["nodo_b"]))] = v

    print("=" * 78)
    print("EL ACTO DE OP-D-02, MEDIDO OTRA VEZ (vuelta 33, detector de ganador corregido)")
    print("=" * 78)
    print()
    print("NOMINA DE LA OPERACION, leida hoy del fichero: %d nodos" % len(nomina))
    for nid in nomina:
        ruta = os.path.join(NODOS, nid + ".json")
        if not os.path.exists(ruta):
            print("  %-32s AUSENTE" % nid)
            continue
        with open(ruta, encoding="utf-8") as fh:
            d = json.load(fh)
        print("  %-32s pasos %2d  vivo %s  fuente: %s"
              % (nid, len(d.get("pasos_accionables") or []), vivo(d), d.get("fuente")))

    print()
    print("--- 1. COBERTURA DEL ACTO: los pares internos, uno por uno ---")
    pares = list(itertools.combinations(sorted(nomina), 2))
    con, sin = [], []
    for a, b in pares:
        v = por_par.get(frozenset((a, b)))
        if v is None:
            sin.append((a, b))
            print("  [SIN VEREDICTO] %-30s contra %-30s" % (a, b))
        else:
            con.append(v)
            print("  [%s puesto %4d] %-30s contra %-30s"
                  % (v["clase"], v["puesto_intra"], v["nodo_a"], v["nodo_b"]))
    print()
    print("  PARES POSIBLES %d, CON VEREDICTO %d, SIN VEREDICTO %d"
          % (len(pares), len(con), len(sin)))
    print("  LA VERIFICACION DE LA OPERACION PIDE CERO SIN VEREDICTO EN LA COLA: %s"
          % ("CUMPLE" if not sin else "NO CUMPLE"))

    print()
    print("--- 2. EL CIERRE TRANSITIVO DE LAS A, y quien gana cada par A ---")
    aes = [v for v in con if v["clase"] == "A"]
    print("  pares A dentro de la nomina: %d" % len(aes))
    viejo_si = nuevo_si = 0
    for v in aes:
        print()
        print("    PUESTO %d: %s contra %s"
              % (v["puesto_intra"], v["nodo_a"], v["nodo_b"]))
        hits = detector_nuevo(v["razon"])
        vj = detector_viejo(v["razon"])
        viejo_si += 1 if vj else 0
        nuevo_si += 1 if hits else 0
        print("      DETECTOR VIEJO (substring 'gana')      : %s" % ("SI" if vj else "NO"))
        if vj and not hits:
            m = re.search(r"\w*gana\w*", v["razon"], re.IGNORECASE)
            print("        FALSO POSITIVO, y aqui esta la palabra: %r" % (m.group(0) if m else "?"))
        print("      DETECTOR NUEVO (vocabulario, palabra)  : %s%s"
              % ("SI" if hits else "NO", (" %s" % hits) if hits else ""))
        print("      LA RAZON ENTERA, para que la lectura mande sobre el lexico:")
        for i in range(0, len(v["razon"]), 96):
            print("        %s" % v["razon"][i:i + 96])
    print()
    print("  PARES A QUE NOMBRAN GANADOR, detector VIEJO: %d de %d" % (viejo_si, len(aes)))
    print("  PARES A QUE NOMBRAN GANADOR, detector NUEVO: %d de %d" % (nuevo_si, len(aes)))

    tocados = set()
    for v in aes:
        tocados |= {v["nodo_a"], v["nodo_b"]}
    print()
    print("  nodos dentro del cierre transitivo de las A: %d de %d de la nomina"
          % (len(tocados), len(nomina)))
    print("    %s" % sorted(tocados))
    fuera = sorted(set(nomina) - tocados)
    print("  nodos de la nomina FUERA del cierre: %s" % (fuera or "ninguno"))
    print("  campo superviviente de la operacion, leido hoy: %r"
          % ops["OP-D-02"]["superviviente"])
    print()
    print("  LA PRUEBA CORREGIDA DEL BANCO 9.3.1 (gano TODOS los pares A que lo tocan,")
    print("  contando SOLO las A), nodo por nodo:")
    for nid in sorted(nomina):
        suyos = [v for v in aes if nid in (v["nodo_a"], v["nodo_b"])]
        ganados = [v for v in suyos if detector_nuevo(v["razon"])]
        print("    %-32s pares A que lo tocan %d, con ganador citable %d  -> %s"
              % (nid, len(suyos), len(ganados),
                 "GANADOR POR DERECHO" if suyos and len(ganados) == len(suyos)
                 else "NO hay victoria citable"))

    print()
    print("--- 3. CENSO POR NOMBRE DE LA FAMILIA (banco 9.5.1) ---")
    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        with open(os.path.join(NODOS, nombre), encoding="utf-8") as fh:
            d = json.load(fh)
        todos[d["node_id"]] = d
    marcados = sorted(k for k, d in todos.items()
                      if vivo(d) and any(m in k for m in MARCAS))
    print("  marcas buscadas: %s" % MARCAS)
    print("  nodos vivos que llevan alguna marca: %d" % len(marcados))
    for k in marcados:
        print("    %-38s %s  %s" % (k, "EN LA NOMINA" if k in nomina else "fuera",
                                    todos[k].get("fuente")))
    print()
    print("=" * 78)
    print("FIN DE LA MEDICION. Nada se fundio y nada se escribio.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
