# -*- coding: utf-8 -*-
"""vuelta159_tarea9_marcador_cierre.py . TAREA 9 DE LA VUELTA 159, EL MARCADOR
RECOMPUTADO AL CIERRE.

POR QUE EXISTE ESTE FICHERO Y NO SE REUSA EL DE LA 157: la salida
`docs/loop/SALIDA_V157_T9_MARCADOR_CIERRE.txt` existe, pero NINGUN `.py` del
repo la produce (buscado por su cabecera literal "MARCADOR DEL ARCHIVO, CONTADO
DE" sobre `scripts/loop/*.py`: cero resultados). Era un instrumento de un solo
uso. Eso es justo lo que la TAREA 7 de esta vuelta acaba de perseguir en otros
dos ficheros, asi que aqui se hace lo contrario: EL INSTRUMENTO SE ESCRIBE Y SE
COMMITEA, con nombre estable, para que la cifra del cierre tenga siempre un
productor vivo que la vuelva a sacar.

QUE CUENTA, Y CADA BLOQUE DICE DE QUE FICHERO SALE:
  - EL MARCADOR DEL ARCHIVO, de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`: n, las
    cuatro clases, puestos distintos, minimo, maximo, HUECOS y DUPLICADOS.
  - EL CENSO Y LAS ARISTAS, de `dataset/metadata/master_graph.json`: nodos,
    vivos, deprecados, las dos vistas, su suma y su UNION DIRIGIDA (las entradas
    de `nodos_previos` se dan la vuelta a (origen, destino) antes de unir, que
    es la definicion que el archivo publica), mas `solo_sig`, `solo_prev` y los
    auto enlaces.
  - EL REGISTRO DE CITAS, de `docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl`: filas,
    reparto por via y clase, y el reparto del campo `cita` por forma, que es lo
    que la TAREA 4 de esta vuelta unifico.

TODA LINEA VA CON EL ROTULO `CIFRA` para que `verificar_cifras_del_reporte.py`
pueda cotejarla contra el reporte.

USO:  python scripts/loop/vuelta159_tarea9_marcador_cierre.py

--- ADJUDICACION 6.8 DEL ACTA 159 (3 sep 2026): ESTE INSTRUMENTO SE PARAMETRIZA.
UN INSTRUMENTO QUE NACE PARA QUE LA CIFRA TENGA PRODUCTOR VIVO NO PUEDE OBLIGAR
A ESCRIBIR OTRO EL MES QUE VIENE ---

CORRECCION DECLARADA POR ADICION. Nada de lo escrito arriba se borra.

QUE SE CONFIRMA PRIMERO, PORQUE ES LO QUE JUSTIFICA QUE ESTE FICHERO EXISTA: el
auditor corrio `git log --all -S` sobre la cabecera de
`SALIDA_V157_T9_MARCADOR_CIERRE.txt` y NO DEVUELVE NADA en `scripts/`, ni vivo
ni muerto. Aquella salida era de un solo uso y el reporte de la vuelta 159 lo
dice bien.

EL AGUJERO DE CONSTRUCCION, HALLADO POR EL AUDITOR SOBRE ESTE MISMO REMEDIO
(acta 159, seccion 5.2): este fichero imprimia `"VUELTA 159, CIERRE: ..."`
LITERAL, sin `--vuelta` y sin `argparse`. En la vuelta 160 o mentia en su propia
cabecera o obligaba a que naciera otro instrumento de un solo uso, QUE ES
EXACTAMENTE EL DEFECTO QUE ESTE VINO A CERRAR. No es caida de reporte: el
reporte nunca afirmo que estuviera parametrizado.

EL REMEDIO, EJECUTADO EN LA TAREA 4 DE LA VUELTA 160: toma `--vuelta` y el
rotulo se interpola. El literal viejo queda en este registro y no en el codigo.
"""
import argparse
import io
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERED = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")


def jsonl(ruta):
    return [json.loads(x) for x in io.open(ruta, encoding="utf-8").read().splitlines()
            if x.strip()]


def main():
    # CORRECCION DECLARADA POR ADICION (vuelta 160, TAREA 4; adjudicacion 6.8 del
    # acta 159, hallada por el auditor en la seccion 5.2 sobre este mismo
    # remedio). LA LINEA VIEJA QUEDA AQUI, TACHADA Y LEGIBLE, porque la cabecera
    # de docs/loop/SALIDA_V159_T9_MARCADOR_CIERRE.txt se escribio con ella:
    #     ~~print("VUELTA 159, CIERRE: MARCADOR, CENSO, ARISTAS Y REGISTRO, AL CIERRE")~~
    # EL DEFECTO: este fichero nacio en la vuelta 159 PARA MATAR LOS ARTEFACTOS
    # DE UN SOLO USO (la salida de la 157 no tenia productor vivo en scripts/,
    # comprobado por el auditor con git log --all -S), y traia el numero de
    # vuelta CLAVADO en su propia cabecera, sin --vuelta y sin argparse. En la
    # vuelta 160 o mentia en su cabecera o obligaba a escribir otro instrumento
    # de un solo uso, QUE ES EXACTAMENTE EL DEFECTO QUE VINO A CERRAR.
    # EL REMEDIO: toma --vuelta y el rotulo se interpola. Sin valor por defecto
    # A PROPOSITO: un defecto silencioso volveria a clavar un numero, solo que
    # mas escondido. Quien lo corra tiene que decir de que vuelta habla.
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vuelta", type=int, required=True,
                    help="numero de vuelta del cierre que se esta midiendo")
    a = ap.parse_args()
    print("=" * 78)
    print("VUELTA %d, CIERRE: MARCADOR, CENSO, ARISTAS Y REGISTRO, AL CIERRE" % a.vuelta)
    print("=" * 78)
    print("")

    V = jsonl(VERED)
    clases = {}
    puestos = []
    for v in V:
        clases[v.get("clase")] = clases.get(v.get("clase"), 0) + 1
        p = v.get("puesto_intra", v.get("puesto"))
        if p is not None:
            puestos.append(int(p))
    print("MARCADOR DEL ARCHIVO, CONTADO DE docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
    print("CIFRA n, filas del archivo: %d" % len(V))
    for c in sorted(clases):
        print("CIFRA marcador clase %s: %d" % (c, clases[c]))
    print("CIFRA puestos distintos: %d" % len(set(puestos)))
    print("CIFRA puesto minimo: %d" % (min(puestos) if puestos else 0))
    print("CIFRA puesto maximo: %d" % (max(puestos) if puestos else 0))
    faltan = sorted(set(range(min(puestos), max(puestos) + 1)) - set(puestos)) if puestos else []
    dup = len(puestos) - len(set(puestos))
    print("CIFRA huecos: %d" % len(faltan))
    print("CIFRA duplicados: %d" % dup)
    print("")

    N = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    vivos = sum(1 for n in N.values() if not n.get("deprecado"))
    sig, prev, auto = set(), set(), 0
    n_sig = n_prev = 0
    for nid, n in N.items():
        for d in (n.get("nodos_siguientes") or []):
            n_sig += 1
            sig.add((nid, d))
            if nid == d:
                auto += 1
        for o in (n.get("nodos_previos") or []):
            n_prev += 1
            prev.add((o, nid))
            if nid == o:
                auto += 1
    print("CENSO Y ARISTAS, CONTADOS DE dataset/metadata/master_graph.json")
    print("CIFRA nodos: %d" % len(N))
    print("CIFRA vivos: %d" % vivos)
    print("CIFRA deprecados: %d" % (len(N) - vivos))
    print("CIFRA aristas nodos_siguientes: %d" % n_sig)
    print("CIFRA aristas nodos_previos: %d" % n_prev)
    print("CIFRA suma de las dos vistas: %d" % (n_sig + n_prev))
    print("CIFRA union DIRIGIDA de las dos vistas: %d" % len(sig | prev))
    print("CIFRA solo en nodos_siguientes: %d" % len(sig - prev))
    print("CIFRA solo en nodos_previos: %d" % len(prev - sig))
    print("CIFRA auto enlaces: %d" % auto)
    print("")

    E = jsonl(REGISTRO)
    por_via = {}
    for e in E:
        k = (e.get("via"), e.get("clase"))
        por_via[k] = por_via.get(k, 0) + 1
    print("EL REGISTRO DE CITAS, CONTADO DE docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl")
    print("CIFRA filas del registro de citas: %d" % len(E))
    for k in sorted(por_via, key=lambda x: (str(x[0]), str(x[1]))):
        print("CIFRA registro %s clase %s: %d" % (k[0], k[1], por_via[k]))
    con_rastro = sum(1 for e in E if "[ANTES " in e["cita"])
    vieja = sum(1 for e in E if "RECLASIFICADA A " in e["cita"])
    ld = sum(1 for e in E if e["cita"].startswith("LD-OPC05-"))
    print("CIFRA citas de lectura dirigida: %d" % ld)
    print("CIFRA citas con rastro de correccion: %d" % con_rastro)
    print("CIFRA citas en la forma vieja de la vuelta 156: %d" % vieja)
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
