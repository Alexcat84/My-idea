#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""inventario_escala.py - Escribe docs/INVENTARIO_ESCALA.md desde lo ya clasificado.

SOLO LECTURA. Lee packs/_core/poda/_censo_escala.jsonl y los nodos, y escribe UN
documento. Cero API, cero campos tocados.

POR QUE ES UN INVENTARIO Y NO UN CENSO CERRADO: el plan de la compuerta de
escala se retiro entero por decision de producto del fundador (ago 2026). No hay
campo `escala`, ni condicion nueva en esOfrecible, ni chequeo de alcanzabilidad,
ni migracion. La direccion es otra: entrevista mas honestidad de mundos.

Por eso el censo se cerro barato. Clasificar los que faltan habria costado unos
seis dolares para alimentar una decision que ya no existe.

Y por eso NO se calcula el simulacro de encierro: medía el efecto de una
compuerta que no se va a construir.
"""
import collections
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
REGISTRO = BASE / "packs" / "_core" / "poda" / "_censo_escala.jsonl"
REPORTE = BASE / "docs" / "INVENTARIO_ESCALA.md"

# Los ocho que el rumbo-trampa `frontera_artesana_sola_no_corporativo` prohibe
# en el top-3 de una artesana sola. Sirven de calibracion: los clasificados
# deberian haber salido corporativos.
OCHO_DEL_RUMBO = [
    "plan_gestion_recursos_humanos", "equipo_multifuncional_real",
    "framework_evaluacion_director_ventas", "evaluacion_balanceada_de_ejecutivos",
    "customer_development_team", "equipo_mejora_calidad_2",
    "involucramiento_sindical_calidad", "chief_sustainability_officer",
]


def activos():
    out = {}
    for p in sorted((BASE / "dataset" / "nodos").glob("*.json")):
        n = json.loads(p.read_text(encoding="utf-8"))
        if not n.get("deprecado"):
            out[n["node_id"]] = n
    return out


def juzgados():
    d = {}
    if REGISTRO.exists():
        for linea in REGISTRO.read_text(encoding="utf-8").splitlines():
            if linea.strip():
                x = json.loads(linea)
                d[x["id"]] = x
    return d


def semillas():
    s = set()
    rutas = [BASE / "dataset" / "metadata" / "entry_seeds.json"]
    rutas += list((BASE / "packs").glob("*/metadata/entry_seeds.json"))
    for p in rutas:
        if p.exists():
            d = json.loads(p.read_text(encoding="utf-8"))
            s |= set(d["seeds"] if isinstance(d, dict) else d)
    return s


def limpiar(t):
    return (t or "").replace("|", "/").replace("\n", " ").strip()


def main():
    act, hechos, seeds = activos(), juzgados(), semillas()
    U = [x for x in hechos.values() if x["v"] == "U"]
    C = [x for x in hechos.values() if x["v"] == "C"]
    D = [x for x in hechos.values() if x["v"] == "D"]
    sin = sorted(set(act) - set(hechos))
    dom_sin = collections.Counter(act[i].get("dominio", "core") for i in sin)
    semillas_corp = [x for x in C if x["id"] in seeds]

    L = []
    A = L.append
    A("# INVENTARIO INFORMATIVO PARCIAL de escala corporativa")
    A("")
    A("**No alimenta ninguna compuerta.** El plan de la compuerta de escala se retiro "
      "entero por decision de producto del fundador: no hay campo `escala`, ni condicion "
      "nueva en `esOfrecible`, ni chequeo de alcanzabilidad por escala, ni migracion, ni "
      "fases posteriores.")
    A("")
    A("**La direccion es otra**: entrevista mas honestidad de mundos. El nucleo entrega el "
      "plan completo con su base, y **sus nodos superficiales de temas de mundo existen a "
      "proposito y se quedan**. La invitacion a profundizar va en UN mensaje al final del "
      "plan, derivada de los temas que el plan toco y nombrando el mundo aplicable. "
      "**Nada se esconde por estructura.**")
    A("")
    A("**Para que sirve esto, entonces**, sus dos usos:")
    A("")
    A("1. material para que el interprete converse **sabiendo** que nodos son de operacion "
      "corporativa;")
    A("2. insumo del **mapa tema-a-mundo** de la invitacion al final del plan.")
    A("")
    A(f"**Es PARCIAL a proposito.** El censo se cerro barato en cuanto se retiro el plan "
      f"que lo pedia: clasificar los {len(sin)} restantes habria costado unos seis dolares "
      f"para alimentar una decision que ya no existe.")
    A("")
    A("## La definicion aplicada")
    A("")
    A("> Un nodo es de ESCALA CORPORATIVA si sus `pasos_accionables` son IMPOSIBLES sin al "
      "menos una de estas tres cosas: **(a)** personas a quienes delegar, **(b)** funciones "
      "o areas separadas, **(c)** una autoridad formal por encima del lector. Si los pasos "
      "se pueden hacer estando SOLO, el nodo es UNIVERSAL, aunque hable de empresas, "
      "mencione departamentos o cite una norma industrial.")
    A("")
    A("**Deciden los pasos.** No decide el titulo, ni el vocabulario, ni la fuente, ni las "
      "`condiciones_activacion`. Cada veredicto de abajo **cita el paso concreto** que no "
      "se puede hacer estando solo.")
    A("")
    A("## Los conteos")
    A("")
    A("| | nodos | % de lo clasificado |")
    A("|---|---:|---:|")
    n = max(1, len(hechos))
    A(f"| UNIVERSALES | **{len(U)}** | {100 * len(U) / n:.1f}% |")
    A(f"| CORPORATIVOS | **{len(C)}** | {100 * len(C) / n:.1f}% |")
    A(f"| DUDOSOS | **{len(D)}** | {100 * len(D) / n:.1f}% |")
    A(f"| **clasificados** | **{len(hechos)}** | de {len(act)} activos |")
    A(f"| **SIN CLASIFICAR** | **{len(sin)}** | el censo se cerro antes |")
    A("")
    A("### Lo que quedo sin clasificar, por dominio")
    A("")
    A("| dominio | sin clasificar |")
    A("|---|---:|")
    for dom, c in sorted(dom_sin.items(), key=lambda kv: -kv[1]):
        A(f"| {dom} | {c} |")
    A("")

    por_dom = collections.defaultdict(collections.Counter)
    for x in hechos.values():
        por_dom[x.get("dominio", "core")][x["v"]] += 1
    A("### Lo clasificado, por dominio")
    A("")
    A("| dominio | universales | corporativos | dudosos |")
    A("|---|---:|---:|---:|")
    for dom in sorted(por_dom):
        c = por_dom[dom]
        A(f"| {dom} | {c['U']} | {c['C']} | {c['D']} |")
    A("")

    A("## Las semillas de entrada corporativas")
    A("")
    if semillas_corp:
        A("**AVISO.** Una semilla corporativa seria la puerta de entrada de un mundo "
          "cerrada para un usuario solo.")
        A("")
        A("| node_id | dominio | cond | razon |")
        A("|---|---|---|---|")
        for x in semillas_corp:
            A(f"| `{x['id']}` | {x.get('dominio')} | ({x.get('cond')}) | "
              f"{limpiar(x.get('razon'))} |")
    else:
        A("**NINGUNA de las clasificadas.** Ningun nodo marcado corporativo es semilla de "
          "entrada de su mundo.")
    A("")

    A("## Calibracion contra el rumbo-trampa")
    A("")
    A("Los ocho nodos que el rumbo `frontera_artesana_sola_no_corporativo` prohibe en el "
      "top-3 de una artesana sola. Los que este censo alcanzo a clasificar **deberian haber "
      "salido CORPORATIVOS**; lo que salga distinto se reporta **sin corregirlo**, porque "
      "ajustar un veredicto para que cuadre con la expectativa es justo lo que un censo no "
      "puede hacer.")
    A("")
    A("| node_id | veredicto | cond | razon |")
    A("|---|---|---|---|")
    NOMBRE = {"U": "UNIVERSAL", "C": "CORPORATIVO", "D": "DUDOSO"}
    desacuerdos = []
    for nid in OCHO_DEL_RUMBO:
        x = hechos.get(nid)
        if not x:
            A(f"| `{nid}` | (sin clasificar) | | el censo se cerro antes de llegar |")
            continue
        v = NOMBRE[x["v"]]
        if x["v"] != "C":
            desacuerdos.append((nid, v))
        A(f"| `{nid}` | **{v}** | ({x.get('cond', '')}) | {limpiar(x.get('razon'))} |")
    A("")
    if desacuerdos:
        A("**DESACUERDO CON LA EXPECTATIVA, reportado sin corregir**: "
          + ", ".join(f"`{i}` salio {v}" for i, v in desacuerdos) + ".")
    else:
        A("**Sin desacuerdos** entre los clasificados.")
    A("")

    A("## Los candidatos, uno por uno")
    A("")
    A("Los universales no se listan: basta el conteo.")
    A("")
    A("| node_id | dominio | veredicto | cond | razon (citando el paso) |")
    A("|---|---|---|---|---|")
    for x in sorted(C + D, key=lambda y: (y["v"], y.get("dominio", ""), y["id"])):
        A(f"| `{x['id']}` | {x.get('dominio')} | **{NOMBRE[x['v']]}** | "
          f"({x.get('cond', '?')}) | {limpiar(x.get('razon'))} "
          f"*Paso citado: {limpiar(x.get('paso'))}* |")
    A("")
    A("---")
    A("")
    A("### Nota historica: el simulacro de encierro")
    A("")
    A("El encargo original pedia calcular cuantos nodos universales quedarian inalcanzables "
      "si los corporativos dejaran de ofrecerse. **No se calculo y no se calculara**: medía "
      "el efecto de una compuerta que ya no se va a construir. Queda dicho aqui para que "
      "nadie lo busque creyendo que se perdio.")

    REPORTE.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"  escrito: {REPORTE}")
    print(f"  U={len(U)} C={len(C)} D={len(D)} | sin clasificar={len(sin)} | "
          f"semillas corporativas={len(semillas_corp)} | desacuerdos={len(desacuerdos)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
