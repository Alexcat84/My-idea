# -*- coding: utf-8 -*-
r"""vuelta136_simular_ops11.py . TAREA 3.b de la vuelta 136: simulacion
PREVIA de la ejecucion de `OP-S-11` (el campo `fuente` canonico), sobre
copia en memoria, ANTES de escribir un solo byte.

Lee el GRAFO (dataset/nodos/*.json, nodos vivos con `fuente`) y la TABLA
YA ADJUDICADA y verificada en la vuelta 135
(docs/plan/OP_S_11_MAPEO_PROPUESTO.md, 129 filas grafia -> canonica). NO
rehace la tabla ni reimplementa el union-find: la parsea tal cual esta
escrita.

LA REGLA DE APLICACION (encargo de la vuelta 136, PROMPT_SIGUIENTE.md,
TAREA 3.b): el campo `fuente` se parte por ` | `, CADA declaracion se
sustituye por su canonica de la tabla, y el resultado se vuelve a unir por
` | ` QUITANDO las repetidas que la normalizacion produzca, CONSERVANDO EL
ORDEN de la primera aparicion. Se aplica a TODAS las posiciones, no solo a
la primera.

Publica, cada una con su linea `CIFRA <etiqueta>: <n> <unidad>`:
  - nodos vivos con `fuente`
  - grafias distintas en primera posicion
  - grafias distintas en posicion NO primera
  - cuantas de esas NO estan en la tabla
  - nodos cuyo campo CAMBIA
  - nodos cuyo campo NO cambia
  - grafias distintas en cualquier posicion DESPUES
  - LAS PERDIDAS REPARTIDAS: nodo por nodo, cuando la normalizacion hace
    que dos declaraciones del MISMO campo colapsen en una (perdida de
    DECLARACION REPETIDA, no de nodo ni de arista: ningun nodo muere y
    ninguna arista se mueve, asi que la tabla de seis motivos de perdida
    de 05_SANEO.md NO APLICA aqui).

Salida: docs/loop/SALIDA_V136_3B_SIMULACION.txt

Uso:
  python scripts/loop/vuelta136_simular_ops11.py
"""
import glob
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
TABLA = os.path.join(RAIZ, "docs", "plan", "OP_S_11_MAPEO_PROPUESTO.md")
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V136_3B_SIMULACION.txt")


def cargar_tabla():
    """Parsea docs/plan/OP_S_11_MAPEO_PROPUESTO.md: devuelve dict grafia ->
    canonica, leido de la tabla ya escrita, sin recalcular nada."""
    texto = io.open(TABLA, encoding="utf-8").read()
    lineas = texto.splitlines()
    mapa = {}
    en_tabla = False
    for ln in lineas:
        if ln.startswith("| grafia | canonica propuesta"):
            en_tabla = True
            continue
        if en_tabla and ln.startswith("|---"):
            continue
        if en_tabla and ln.startswith("|"):
            partes = ln.split("|")
            # ['', ' grafia ', ' canonica ', ' motivo ', ' bolsa ', '']
            if len(partes) < 5:
                continue
            grafia = partes[1].strip()
            canonica = partes[2].strip()
            mapa[grafia] = canonica
            continue
        if en_tabla and not ln.startswith("|"):
            break
    return mapa


def cargar_nodos_vivos_con_fuente():
    """Devuelve lista de (ruta, id, fuente_original) de nodos vivos (no
    deprecados) con campo `fuente` no vacio."""
    out = []
    for p in sorted(glob.glob(os.path.join(NODOS, "*.json"))):
        d = json.loads(io.open(p, encoding="utf-8").read())
        if d.get("deprecado"):
            continue
        fu = d.get("fuente")
        if not fu:
            continue
        out.append((p, d.get("id") or os.path.splitext(os.path.basename(p))[0], fu))
    return out


def declaraciones_de(fuente):
    return [d.strip() for d in fuente.split("|")]


def normalizar(declaraciones, mapa):
    """Sustituye cada declaracion por su canonica (o la deja igual si no
    esta en la tabla) y quita las repetidas conservando el orden de la
    primera aparicion. Devuelve (lista_mapeada_sin_dedup, lista_deduped)."""
    mapeadas = [mapa.get(d, d) for d in declaraciones]
    vistas = []
    for d in mapeadas:
        if d not in vistas:
            vistas.append(d)
    return mapeadas, vistas


def simular():
    mapa = cargar_tabla()
    nodos = cargar_nodos_vivos_con_fuente()

    grafias_primera = set()
    grafias_no_primera = set()
    no_primera_sin_cubrir = set()
    cambian = []
    no_cambian = []
    grafias_despues = set()
    perdidas = []

    for ruta, id_nodo, fuente in nodos:
        declaraciones = declaraciones_de(fuente)
        grafias_primera.add(declaraciones[0])
        for d in declaraciones[1:]:
            grafias_no_primera.add(d)
            if d not in mapa:
                no_primera_sin_cubrir.add(d)

        mapeadas, deduped = normalizar(declaraciones, mapa)
        grafias_despues.update(deduped)

        if deduped != declaraciones:
            cambian.append((id_nodo, declaraciones, deduped))
        else:
            no_cambian.append(id_nodo)

        if len(mapeadas) > len(deduped):
            perdidas.append((id_nodo, len(mapeadas) - len(deduped), declaraciones, deduped))

    return {
        "mapa": mapa,
        "total_nodos": len(nodos),
        "grafias_primera": grafias_primera,
        "grafias_no_primera": grafias_no_primera,
        "no_primera_sin_cubrir": no_primera_sin_cubrir,
        "cambian": cambian,
        "no_cambian": no_cambian,
        "grafias_despues": grafias_despues,
        "perdidas": perdidas,
    }


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    r = simular()

    lineas = []
    lineas.append("SIMULACION OP-S-11, vuelta 136, TAREA 3.b (copia en memoria, cero escritura)")
    lineas.append("")
    lineas.append("CIFRA nodos vivos con fuente: %d nodos" % r["total_nodos"])
    lineas.append("CIFRA grafias distintas en primera posicion: %d grafias" % len(r["grafias_primera"]))
    lineas.append("CIFRA grafias distintas en posicion NO primera: %d grafias" % len(r["grafias_no_primera"]))
    lineas.append("CIFRA grafias en posicion NO primera sin cubrir en la tabla: %d grafias" %
                   len(r["no_primera_sin_cubrir"]))
    if r["no_primera_sin_cubrir"]:
        for g in sorted(r["no_primera_sin_cubrir"]):
            lineas.append("  SIN CUBRIR: %s" % g)
    lineas.append("CIFRA nodos cuyo campo fuente CAMBIA: %d nodos" % len(r["cambian"]))
    lineas.append("CIFRA nodos cuyo campo fuente NO cambia: %d nodos" % len(r["no_cambian"]))
    lineas.append("CIFRA grafias distintas en cualquier posicion DESPUES: %d grafias" % len(r["grafias_despues"]))
    lineas.append("")
    lineas.append("LAS PERDIDAS REPARTIDAS (perdida de DECLARACION REPETIDA dentro del propio")
    lineas.append("campo; ningun nodo muere y ninguna arista se mueve, la tabla de seis motivos")
    lineas.append("de perdida de 05_SANEO.md no aplica aqui): %d nodo(s)" % len(r["perdidas"]))
    for id_nodo, n, antes, despues in sorted(r["perdidas"]):
        lineas.append("  %s pierde %d declaracion(es) repetida(s): %s -> %s" %
                       (id_nodo, n, " | ".join(antes), " | ".join(despues)))
    lineas.append("")
    lineas.append("EXITCODE: 0")

    texto = "\n".join(lineas) + "\n"
    with io.open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write(texto)
    sys.stdout.write(texto)


if __name__ == "__main__":
    raise SystemExit(main())
