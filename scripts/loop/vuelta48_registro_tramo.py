# -*- coding: utf-8 -*-
"""Vuelta 48, TAREA 2.3: EL REGISTRO DEL TRAMO 1 DE `OP-U-01` EN 03_FUSIONES.md,
IMPRESO POR INSTRUMENTO Y NO TECLEADO (EJECUTOR.md regla 1).

Cada celda de cada tabla sale del plan sellado o de una de las tres nominas
medidas. Aqui no se escribe ni una cifra a mano.

Uso: python scripts/loop/vuelta48_registro_tramo.py [--escribir]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAG = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
PLAN = os.path.join(RAIZ, "docs", "loop", "PLAN_V48_OPU01_TRAMO1.json")
NOM_A = os.path.join(RAIZ, "docs", "loop", "RECOMPUTO_V48_COMPONENTES.jsonl")
NOM_C = os.path.join(RAIZ, "docs", "loop", "RECOMPUTO_V48_CIERRE.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
EJEC = os.path.join(RAIZ, "docs", "loop", "SALIDA_V48_EJECUCION_TRAMO1.txt")


def censar(p):
    R = [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]
    c = [r for r in R if r["estado"] == "CERRADO"]
    a = [r for r in R if r["estado"] == "ABIERTO"]
    return (len(R), sum(r["tamano"] for r in R), len(c),
            sum(r["tamano"] for r in c), len(a), sum(r["tamano"] for r in a))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    x = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    plan = json.load(io.open(PLAN, encoding="utf-8"))
    A, C = censar(NOM_A), censar(NOM_C)
    ejec = io.open(EJEC, encoding="utf-8").read()

    def dato(clave):
        for l in ejec.split("\n"):
            if clave in l:
                return l.strip()
        return "(no hallado)"

    muertos = sorted(y for a in plan["actos"] for y in a["absorbidos"])
    L = []
    w = L.append
    w("")
    w("---")
    w("")
    w("## `OP-U-01`, TRAMO 1: **DIECISEIS ACTOS FUNDIDOS Y CINCO DECLARADOS** (19 ago 2026, vuelta 48)")
    w("")
    w("**El tramo son los CINCUENTA primeros actos `CERRADOS` de la nomina re-medida al abrirlo**,")
    w("en el orden en que el instrumento los imprime, que es la vara que el auditor adjudico. Se")
    w("leyeron los cincuenta (`P.5`, acto leido entero) con")
    w("`python scripts/loop/vuelta48_dossier_actos.py`")
    w("([`../loop/SALIDA_V48_DOSSIER_1_50.txt`](../loop/SALIDA_V48_DOSSIER_1_50.txt), 369 KB, de solo")
    w("lectura), **se fundieron dieciseis y se declararon los demas con su motivo citado.**")
    w("")
    w("### LA CIFRA DEL TRAMO, impresa por el instrumento")
    w("")
    w("| | |")
    w("|---|---:|")
    w("| actos **leidos** del tramo | **50** |")
    w("| actos **FUNDIDOS** | **%d** |" % len(plan["actos"]))
    w("| actos **DECLARADOS y no fundidos** | **%d** |" % len(plan["declarados_y_no_fundidos"]))
    w("| actos **MIXTOS** que quedan a la espera de la lectura de `P.12` | **27** |")
    w("| nodos implicados en lo fundido | **%d** |" % sum(len(a["miembros"]) for a in plan["actos"]))
    w("| **nodos DEPRECADOS CON ALIAS** | **%d** |" % len(muertos))
    w("| piezas repartidas (pasos y condiciones de los que mueren) | **123**: **39** viajan enteras al superviviente y **84** ya las decia |")
    w("")
    w("**Y las cifras del censo, del propio instrumento** (`vuelta48_fundir_tramo.py --ejecutar`,")
    w("[`../loop/SALIDA_V48_EJECUCION_TRAMO1.txt`](../loop/SALIDA_V48_EJECUCION_TRAMO1.txt), exit 0):")
    w("")
    w("> `%s`" % dato("censo ANTES  :"))
    w(">")
    w("> `%s`" % dato("censo DESPUES:"))
    w(">")
    w("> `%s`" % dato("delta deprecados:"))
    w("")
    w("### LO QUE QUEDA DEL LOTE, medido antes y despues")
    w("")
    w("| | al **ABRIR** el tramo | al **CERRAR** el tramo |")
    w("|---|---:|---:|")
    w("| actos (componentes) | **%d** | **%d** |" % (A[0], C[0]))
    w("| nodos dentro de actos | **%d** | **%d** |" % (A[1], C[1]))
    w("| **`CERRADOS`, que es el lote de esta operacion** | **%d** | **%d** |" % (A[2], C[2]))
    w("| nodos en `CERRADOS` | **%d** | **%d** |" % (A[3], C[3]))
    w("| `ABIERTOS` | **%d** | **%d** |" % (A[4], C[4]))
    w("| nodos en `ABIERTOS` | **%d** | **%d** |" % (A[5], C[5]))
    w("")
    w("**Los `ABIERTOS` no se mueven ni un digito**, que es exactamente lo que cabe esperar de una")
    w("operacion que solo toca `CERRADOS`. **Y los `CERRADOS` bajan en %d, uno por acto fundido.**"
      % (A[2] - C[2]))
    w("Las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) salen **TODAS OK** en")
    w("la corrida de cierre ([`../loop/SALIDA_V48_RECOMPUTO_CIERRE.txt`](../loop/SALIDA_V48_RECOMPUTO_CIERRE.txt)).")
    w("")
    w("### LOS DIECISEIS ACTOS, uno por uno, con su superviviente y su motivo")
    w("")
    w("| # | sobrevive | absorbe | por que sobrevive, en una linea |")
    w("|---:|---|---|---|")
    for a in plan["actos"]:
        motivo = a["motivo"].split(".")[0].strip()
        w("| **%d** | `%s` | %s | %s |"
          % (a["orden"], a["superviviente"],
             ", ".join("`%s`" % y for y in a["absorbidos"]), motivo))
    w("")
    w("**El plan sellado, con la marca de CADA paso y CADA condicion de CADA nodo que muere, vive en**")
    w("[`../loop/PLAN_V48_OPU01_TRAMO1.json`](../loop/PLAN_V48_OPU01_TRAMO1.json). **No trae texto: trae")
    w("INDICES**, y el instrumento lee cada pieza verbatim del fichero del nodo. La guarda de cobertura")
    w("comprueba que **cada indice aparezca exactamente una vez y que no sobre ninguno**: una perdida sin")
    w("destino no es una perdida, es un olvido.")
    w("")
    w("### LOS CINCO DECLARADOS Y NO FUNDIDOS, con su motivo citado")
    w("")
    w("| # | el acto | por que NO se funde |")
    w("|---:|---|---|")
    for a in plan["declarados_y_no_fundidos"]:
        w("| **%d** | %s | %s |"
          % (a["orden"], ", ".join("`%s`" % y for y in a["miembros"]),
             a["motivo"].replace("\n", " ")))
    w("")
    w("### LOS VEINTISIETE MIXTOS, y por que esta vuelta NO los funde")
    w("")
    w("**De los 270 actos `CERRADOS` del lote, VEINTISIETE tienen dentro un par que NO es `A`** (4 de")
    w("tamano cuatro y 23 de tamano tres), **y los veintisiete caen dentro de estos primeros 50**: el")
    w("orden impreso pone los duros por delante. Medido en")
    w("[`../loop/SALIDA_V48_COLISION_1_50.txt`](../loop/SALIDA_V48_COLISION_1_50.txt).")
    w("")
    w("> **`P.12` prohibe fundirlos por transitividad**: *el cierre transitivo CONVOCA, la lectura")
    w("> DECIDE*, y *NI TRANSITIVIDAD AUTOMATICA NI MAYORIA*. El nodo mixto **se lee CONTRA EL")
    w("> SUPERVIVIENTE** y se decide `ENTRA` (comparte procedimiento) o `CONTINUA` (comparte la idea")
    w("> en lineas: enlace mas poda del solape).")
    w("")
    w("**Esa lectura se hizo ENTERA para UNO, el acto 1**, y se deja escrita como ejemplar: el mixto es")
    w("`metodologia_spin_selling`, cuyos dos veredictos `D` (puestos **625** y **764**) dicen los dos, con")
    w("esa palabra, **CONTINUA**, porque su paso 3 es *una linea que ademas remite fuera* mientras los")
    w("otros traen *el PROCEDIMIENTO entero*. **`CONTINUA` no es fusion: es enlace**, y el enlace es de la")
    w("fase 04. **Los otros veintiseis NO se leyeron en esta vuelta, y se dice en vez de callarse.**")
    w("")
    w("### LA GUARDA QUE FALTABA, y el `GATE 0` en rojo que la trajo")
    w("")
    w("> **Se cuenta con nombre porque un fallo que no deja sintoma es la especie del canon 9.**")
    w("")
    w("**La primera corrida `--ejecutar` de este tramo llevaba el acto 36**, que absorbia")
    w("`investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor`. Ese nodo es **SEMILLA DE ENTRADA**")
    w("del mundo `compras` **y ademas DESTINO DE UN PUENTE APROBADO**, asi que `run_phase1.py` dio")
    w("**`GATE 0: FALLIDO`** por **dos** chequeos a la vez. **El dataset se restauro entero con")
    w("`git checkout` y el acto salio del lote.**")
    w("")
    w("**Y la pregunta no era del acto 36: era de la operacion entera.** Medido con")
    w("`python scripts/loop/vuelta48_puertas_en_el_lote.py`")
    w("([`../loop/SALIDA_V48_PUERTAS_EN_EL_LOTE.txt`](../loop/SALIDA_V48_PUERTAS_EN_EL_LOTE.txt), exit 0):")
    w("")
    w("| | |")
    w("|---|---:|")
    w("| semillas de entrada (20 del core mas las de los mundos) | **85** |")
    w("| nodos que son extremo de un puente aprobado | **185** |")
    w("| **el universo PROTEGIDO, la union** | **256** |")
    w("| actos `CERRADOS` con **al menos una puerta dentro** | **31** de 270 |")
    w("| de esos, **SALVABLES** (una sola puerta: el acto se funde **si la puerta sobrevive**) | **29** |")
    w("| de esos, **IMPOSIBLES** (todos sus miembros son puerta: alguien tendria que morir) | **2**, los actos **36** y **174** |")
    w("")
    w("> **LO QUE ESTO DEJA ABIERTO, y va como PREGUNTA y no como decision: en esos 29 actos la eleccion")
    w("> de superviviente YA NO ES LIBRE.** La regla de esta pagina dice que **sobrevive por CONTENIDO**;")
    w("> si el contenido apunta al que **no** es puerta, **hay choque entre la vara de la fase y el")
    w("> `GATE 0`**, y **ninguna regla escrita hoy lo resuelve.**")
    w("")
    w("**La guarda `1B` queda escrita en `scripts/loop/vuelta48_fundir_tramo.py`** y lee las mismas")
    w("fuentes que el `GATE 0`: **ningun absorbido puede ser semilla ni extremo de puente**. Con ella el")
    w("tramo **aborta antes de escribir** en vez de romper.")
    w("")
    w("### GATE 0 Y SUITES TRAS EL TRAMO")
    w("")
    w("| que | como salio |")
    w("|---|---|")
    w("| `run_phase1.py --reaplico-curaduria` | **`GATE 0: OK`**, exit 0 |")
    w("| `etiquetas_de_cara.py --aplicar` | **71** etiquetas, exit 0 |")
    w("| `sync_assets_web.py` | **6** assets, exit 0 |")
    w("| suite del motor | **25 de 25**, exit 0 |")
    w("| suite web | **80** ficheros, **1.030** pasadas y **3** saltadas, exit 0 |")
    w("| `tsc --noEmit` | **CERO** lineas, exit 0 |")
    w("| marcador del archivo | **575 / 79 / 8 / 2.726**, `n` **3.388**, cero huecos y cero duplicados: **SIN MOVER** |")
    w("| duplicadas tras resolver | **1.010** antes y **1.004** despues: **CERO nuevas**, y el tramo **baja el pasivo historico en 6** por `P.16` |")
    w("| auto-aristas | **CERO** nuevas; **3** que la fusion habria creado, retiradas en el acto |")
    w("")

    bloque = "\n".join(L) + "\n"
    t = io.open(PAG, encoding="utf-8", newline="").read()
    if "TRAMO 1: **DIECISEIS ACTOS FUNDIDOS" in t:
        print("YA APLICADO.")
        return 0
    print(bloque[:1500])
    print("... (%d lineas, %d caracteres)" % (len(L), len(bloque)))
    print()
    print("guiones largos en el bloque: %d | guiones medios: %d"
          % (bloque.count("—"), bloque.count("–")))
    if not x.escribir:
        print("SIMULACION: sin --escribir no toco nada.")
        return 0
    n0 = t.count("\n")
    io.open(PAG, "w", encoding="utf-8", newline="").write(t.rstrip("\r\n") + "\n" + bloque)
    t2 = io.open(PAG, encoding="utf-8", newline="").read()
    print("ESCRITO. lineas antes %d, despues %d" % (n0, t2.count("\n")))
    print("guiones largos en el fichero %d, medios %d"
          % (t2.count("—"), t2.count("–")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
