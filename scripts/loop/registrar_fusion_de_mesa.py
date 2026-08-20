# -*- coding: utf-8 -*-
"""registrar_fusion_de_mesa.py . ESCRIBE EL REGISTRO DE UNA FUSION DE MESA AL
FINAL DE docs/plan/03_FUSIONES.md, CON CADA CELDA LEIDA DE UN INSTRUMENTO.

NOMBRE ESTABLE, y no lleva vuelta ni operacion: las dos las dice el PLAN que
entra por --plan. Hermano de scripts/loop/registrar_cierre_de_tramo.py, que hace
lo mismo para un tramo entero de OP-U-01.

NI UNA CELDA SE TECLEA. Las tres tablas salen de:
  - el PLAN SELLADO (--plan): superviviente, absorbidos, marcas pieza a pieza,
    perdidas con sus cuatro claves, y los campos copiados de la ficha;
  - la SALIDA DE LA EJECUCION (--ejecucion): censo antes y despues, delta de
    deprecados, redirecciones, P.16 y las cuatro guardas finales;
  - la SALIDA DE LA VERIFICACION (--verificacion), si se pasa.
Lo que no se pueda leer de un fichero NO SE ESCRIBE: el bloque DECLARA su falta.

NO REESCRIBE NI UNA LINEA DE ARRIBA: abre la pagina en modo adosar.

Uso:
  python scripts/loop/registrar_fusion_de_mesa.py --plan docs/loop/PLAN_V63_OPM03I.json
      --ejecucion docs/loop/SALIDA_V63_OPM03I_EJEC.txt
      [--verificacion docs/loop/SALIDA_V63_VERIFICAR_OPM03I.txt]
      [--nota "..."] [--simular]
"""
import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
NL = chr(10)


def leer(ruta, fallos, que):
    if not ruta:
        fallos.append("no se paso fichero de %s" % que)
        return ""
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    if not os.path.exists(p):
        fallos.append("no existe el fichero de %s: %s" % (que, ruta))
        return ""
    return io.open(p, encoding="utf-8").read()


def busca(texto, patron, etq, fallos, grupo=1):
    m = re.search(patron, texto)
    if not m:
        fallos.append("no se pudo leer %s de la salida" % etq)
        return "?"
    return m.group(grupo)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--ejecucion", required=True)
    ap.add_argument("--verificacion", default=None)
    ap.add_argument("--nota", action="append", default=[])
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    fallos = []
    plan = json.load(io.open(os.path.join(RAIZ, a.plan.replace("/", os.sep)), encoding="utf-8"))
    eje = leer(a.ejecucion, fallos, "ejecucion")
    ver = leer(a.verificacion, fallos, "verificacion") if a.verificacion else ""

    op = plan["operacion"]
    acto = plan["actos"][0]
    sup = acto["superviviente"]
    absorbidos = acto["absorbidos"]

    antes = busca(eje, r"censo ANTES: (\d+) ficheros, (\d+) vivos, (\d+) deprecados",
                  "censo antes", fallos, 0)
    despues = busca(eje, r"censo DESPUES: (\d+) ficheros, (\d+) vivos, (\d+) deprecados",
                    "censo despues", fallos, 0)
    delta = busca(eje, r"delta deprecados: ([+-]\d+ \(esperado [+-]\d+\): \w+)",
                  "delta de deprecados", fallos)
    # LA BARRA VERTICAL NO PUEDE VIAJAR DENTRO DE UNA CELDA: parte la tabla en
    # dos columnas de mas. Se leen los dos trozos por separado y se unen con coma.
    pasos_cond = "%s, condiciones %s" % (
        busca(eje, r"pasos (\d+ -> \d+ \(anadidos \d+\))", "pasos", fallos),
        busca(eje, r"condiciones (\d+ -> \d+ \(anadidas \d+\))", "condiciones", fallos))
    redir = re.findall(r"^   (\S+)\s+(nodos_\w+)\s+(\S+) -> (\S+)$", eje, re.M)
    n_redir = busca(eje, r"redirecciones sobre nodos VIVOS: (\d+)", "redirecciones", fallos)
    p16 = busca(eje, r"P\.16, DUPLICADAS QUE LA PROPIA FUSION FABRICA[^:]*: (\d+)",
                "P.16", fallos)
    autos = busca(eje, r"AUTO-ARISTAS que la fusion habria creado y se retiran: (\d+)",
                  "auto-aristas", fallos)
    gA = busca(eje, r"guarda A, cero AUTO-ARISTAS nuevas\s+: (\w+ \(\d+\))", "guarda A", fallos)
    gB = busca(eje, r"guarda B, cero DUPLICADAS nuevas tras resolver : (\w+ \(\d+\))",
               "guarda B", fallos)
    gC = busca(eje, r"guarda C, los CINCO campos que esta operacion NO redacta, intactos: (\d+ de \d+)",
               "guarda C", fallos)
    gD = busca(eje, r"guarda D, los \d+ absorbidos conservan su texto INTACTO: (\w+)",
               "guarda D", fallos)
    piezas = busca(eje, r"piezas repartidas   : (\d+ \([^)]*\))", "piezas", fallos)

    if fallos:
        print("ROJO, %d fallo(s) y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    L = []
    L.append("")
    L.append("---")
    L.append("")
    L.append("## `%s`: EL REGISTRO DE LA FUSION (%s, vuelta %d)"
             % (op, plan["fecha"], plan["vuelta"]))
    L.append("")
    L.append("**Cada celda de este registro sale de un instrumento corrido en la vuelta %d y pegada "
             "entera**, con el comando citado al lado. **El registro se adosa al final de la pagina y "
             "NO reescribe ni una linea de arriba.**" % plan["vuelta"])
    L.append("")
    L.append("| | |")
    L.append("|---|---|")
    L.append("| **la ficha** | `docs/plan/OPERACIONES.jsonl`, tipo **%s**, estado **LISTA**, fecha de "
             "corte **%s** |" % (plan.get("ficha_tipo"), plan.get("ficha_fecha_corte")))
    L.append("| **superviviente** | `%s` |" % sup)
    L.append("| **absorbe** | %s |" % ", ".join("`%s`" % x for x in absorbidos))
    L.append("| **plan sellado** | [`../loop/%s`](../loop/%s), contrato **`%s`** |"
             % (os.path.basename(a.plan), os.path.basename(a.plan),
                plan.get("contrato_de_perdidas")))
    L.append("| **censo del catalogo** | ANTES %s . DESPUES %s . **delta de deprecados %s** |"
             % (antes.split(": ", 1)[1], despues.split(": ", 1)[1], delta))
    L.append("| **el superviviente** | %s |" % pasos_cond)
    L.append("| **piezas repartidas** | **%s** |" % piezas)
    L.append("")
    L.append("**LA ADJUDICACION, COPIADA VERBATIM DE LA FICHA Y NO REDACTADA AQUI:**")
    L.append("")
    L.append("> %s" % (plan.get("ficha_adjudicacion") or "LA FICHA NO TRAE ADJUDICACION").replace(NL, " "))
    L.append("")
    L.append("### EL REPARTO, PIEZA A PIEZA, TALLADO DEL PLAN SELLADO")
    L.append("")
    L.append("| pieza del que muere | marca | a donde va |")
    L.append("|---|---|---|")
    for ab in absorbidos:
        for etq, campo in (("paso", "pasos"), ("condicion", "condiciones")):
            marcas = (acto[campo].get(ab) or {})
            for i in sorted(marcas, key=int):
                m = marcas[i]
                if m == "APPEND":
                    dest = "**viaja ENTERA** al superviviente"
                    marca = "`APPEND`"
                elif m.startswith("INCISO:"):
                    k = m[len("INCISO:"):].split("|")[0]
                    trozo = m[len("INCISO:"):].split("|")[1]
                    dest = "**`INCISO` ADOSADO** al paso %s: *%s*" % (k, trozo)
                    marca = "`INCISO`"
                elif m.startswith("CUBIERTO_COND:"):
                    dest = "ya lo dice la **condicion %s** del superviviente" % m.split(":")[1]
                    marca = "`CUBIERTO`"
                else:
                    # CUBIERTO:n APUNTA AL PASO n SI LA PIEZA ES UN PASO Y A LA
                    # CONDICION n SI ES UNA CONDICION, que es como lo lee el
                    # ejecutor. El primer borrador de este registro escribia paso
                    # en las dos ramas y publicaba un destino falso.
                    dest = ("ya lo dice %s **%s** del superviviente"
                            % ("el paso" if campo == "pasos" else "la condicion",
                               m.split(":")[1]))
                    marca = "`CUBIERTO`"
                L.append("| %s **%s** de `%s` | %s | %s |" % (etq, i, ab, marca, dest))
    L.append("")
    per = acto.get("perdidas") or []
    L.append("### LAS PERDIDAS, SELLADAS EN CAMPO PROPIO (`%s`)"
             % plan.get("contrato_de_perdidas"))
    L.append("")
    if not per:
        L.append("**EL ACTO DECLARA CERO PERDIDAS**, y la lista vacia del campo `perdidas` es una "
                 "**DECLARACION**, no un silencio.")
    else:
        L.append("| especie | que se pierde | donde vivia | enrutada a |")
        L.append("|---|---|---|---|")
        for p in per:
            L.append("| **%s** | %s | %s | %s |"
                     % (p["especie"], p["que"], p["donde"], p["enrutada_a"]))
    L.append("")
    L.append("### LAS REDIRECCIONES Y LAS GUARDAS, LEIDAS DE LA SALIDA DE LA EJECUCION")
    L.append("")
    L.append("**Redirecciones sobre nodos VIVOS: %s.** Salen enteras de "
             "[`../loop/%s`](../loop/%s):" % (n_redir, os.path.basename(a.ejecucion),
                                              os.path.basename(a.ejecucion)))
    L.append("")
    L.append("| nodo que nombraba al que muere | campo | pasa a nombrar |")
    L.append("|---|---|---|")
    for nid, campo, viejo, nuevo in redir:
        L.append("| `%s` | `%s` | `%s` |" % (nid, campo, nuevo))
    L.append("")
    L.append("| guarda | resultado |")
    L.append("|---|---|")
    L.append("| **`P.16`, duplicadas que la propia fusion fabrica** | **%s** |" % p16)
    L.append("| **auto-aristas que la fusion habria creado** | **%s** |" % autos)
    L.append("| **guarda A**, cero auto-aristas nuevas | **%s** |" % gA)
    L.append("| **guarda B**, cero duplicadas nuevas tras resolver | **%s** |" % gB)
    L.append("| **guarda C**, los cinco campos que la operacion NO redacta, intactos | **%s** |" % gC)
    L.append("| **guarda D**, el absorbido conserva su texto INTACTO | **%s** |" % gD)
    L.append("")
    if ver:
        L.append("### LO QUE LA FICHA MANDABA COMPROBAR DESPUES DE FUNDIR, COMPROBADO")
        L.append("")
        L.append("Sale de [`../loop/%s`](../loop/%s), corrida en esta vuelta:"
                 % (os.path.basename(a.verificacion), os.path.basename(a.verificacion)))
        L.append("")
        L.append("```")
        for l in ver.split(NL):
            if l.startswith(("1.", "2.", "3.", "4.", "5.", "6.")) or l.startswith("   "):
                L.append(l.rstrip())
        L.append("```")
        L.append("")
    for n in a.nota:
        L.append(n)
        L.append("")

    texto = NL.join(L)
    print("=" * 78)
    print("REGISTRO DE LA FUSION DE MESA %s" % op)
    print("  plan     : %s" % a.plan)
    print("  ejecucion: %s" % a.ejecucion)
    print("  lineas del registro: %d" % len(L))
    print("=" * 78)
    if a.simular:
        print(texto)
        print()
        print("MODO SIMULAR: no se adosa nada a la pagina.")
        return 0
    n0 = len(io.open(PAGINA, encoding="utf-8").read().split(NL))
    with io.open(PAGINA, "a", encoding="utf-8", newline=NL) as fh:
        fh.write(texto + NL)
    n1 = len(io.open(PAGINA, encoding="utf-8").read().split(NL))
    print("ADOSADO a %s: %d lineas antes, %d despues (+%d)."
          % (os.path.relpath(PAGINA, RAIZ), n0, n1, n1 - n0))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
