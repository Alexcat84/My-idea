# -*- coding: utf-8 -*-
"""El aviso de curaduria revertida de scripts/run_phase1.py.

LA AVERIA DE ORIGEN (2026-08-07, integrando compras y entrega): run_phase1
recompila master_graph.json desde dataset/nodos/, y la curaduria de etiquetas
de cara no vive en los nodos, vive en dataset/metadata/etiquetas_de_cara_v1*
y se aplica sobre las dos COPIAS del grafo. Cada recompilacion la borra. Se
llevo por delante 71 etiquetas del core, que volvieron a su titulo de libro
("Canvas", "Pivotar", "SPIN", "DMAIC"), y NADA se quejo: el grafo seguia
siendo valido y el Gate 0 daba OK.

Es la clase mas peligrosa de averia: degrada la VOZ sin romper la estructura,
y el Gate solo mira la estructura. Volvio a morder en la verificacion previa
al tag de produccion, esta vez por la via de fuera (correr run_phase1 suelto
para comprobar el Gate), que el paso e-bis de integrar_packs no cubre.

Los dos escenarios que definen el arreglo:
  - run_phase1 SUELTO sobre una copia curada -> grita y falla (codigo != 0)
  - el flujo via integrar_packs, que reaplica justo despues -> limpio y callado

Y lo que JAMAS hace: auto-aplicar. Eso creaeria una segunda fuente de
curaduria, prohibida por el remache del e-bis.
"""
import io
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

from run_phase1 import (  # noqa: E402
    avisar_curaduria, curaduria_revertida, etiquetas_curadas, indice_rojo_declarado,
)


def capturar(fn):
    """Ejecuta fn con la salida capturada; devuelve (resultado, texto)."""
    antes, buf = sys.stdout, io.StringIO()
    sys.stdout = buf
    try:
        return fn(), buf.getvalue()
    finally:
        sys.stdout = antes


def grafo_curado():
    """Un grafo minimo con las etiquetas EN SU FORMA CURADA."""
    return {nid: {"etiqueta_arbol": etiqueta}
            for nid, etiqueta in list(etiquetas_curadas().items())[:5]}


def test_la_curaduria_real_existe():
    curadas = etiquetas_curadas()
    assert len(curadas) > 50, f"solo {len(curadas)} etiquetas curadas; listas mal leidas"
    print(f"  ok: la curaduria real trae {len(curadas)} etiquetas")


def test_suelto_sobre_copia_revertida_grita_y_falla():
    nodos = grafo_curado()
    victima = next(iter(nodos))
    nodos[victima]["etiqueta_arbol"] = "Actualiza tu Canvas tras Descubrir"

    assert curaduria_revertida(nodos) == [victima], curaduria_revertida(nodos)
    codigo, salida = capturar(lambda: avisar_curaduria(nodos, reaplico=False))
    assert codigo != 0, "no fallo: un script que lo llame se lo tragaria en silencio"
    assert "REVERTISTE LA CURADURIA DE ETIQUETAS" in salida, salida
    assert "etiquetas_de_cara.py --aplicar" in salida, salida
    assert "\033[1;31m" in salida, "el aviso no sale en rojo"
    assert victima in salida, "no dice CUAL etiqueta se perdio"
    print(f"  ok: suelto sobre copia revertida grita en rojo y sale con {codigo}")


def test_via_integrar_packs_limpio_y_callado():
    # El flujo de la linea de ensamblaje: recompila y reaplica acto seguido,
    # asi que el aviso sobra; sin la bandera pararia justo antes de arreglarlo.
    nodos = grafo_curado()
    nodos[next(iter(nodos))]["etiqueta_arbol"] = "Actualiza tu Canvas tras Descubrir"
    codigo, salida = capturar(lambda: avisar_curaduria(nodos, reaplico=True))
    assert codigo == 0, codigo
    assert salida == "", f"deberia callar y dijo: {salida!r}"
    print("  ok: via integrar_packs (con e-bis detras) pasa limpio y callado")


def test_copia_intacta_no_molesta():
    nodos = grafo_curado()
    assert curaduria_revertida(nodos) == []
    codigo, salida = capturar(lambda: avisar_curaduria(nodos, reaplico=False))
    assert codigo == 0 and salida == "", (codigo, salida)
    print("  ok: sobre una copia intacta no dice nada")


def test_jamas_auto_aplica():
    # La baranda del remache: avisar_curaduria NO puede escribir. Si algun dia
    # alguien "resuelve" el aviso aplicando la curaduria aqui, habria dos
    # fuentes y el bug volveria con otro disfraz.
    fuente = (BASE / "scripts" / "run_phase1.py").read_text(encoding="utf-8")
    cuerpo = fuente[fuente.index("def avisar_curaduria"):fuente.index("def main():")]
    for prohibido in ("write_text", "json.dump", 'open(', "etiqueta_arbol ="):
        assert prohibido not in cuerpo, f"el aviso escribe: '{prohibido}'"
    print("  ok: el aviso avisa; no toca un solo archivo")


def test_el_nodo_fantasma_con_nombre():
    """Un nodo ACTIVO cuya UNICA entrada esta deprecada existe, tiene titulo y
    contenido, y NADIE puede llegar a el. No es un huerfano historico: es una
    baja causada por una deprecacion, y el efecto es DOMINO.

    Cazado al deprecar los programas de OSHA (ago 2026): cerrar esa puerta dejo
    colgando a "Derecho del Trabajador a Rechazar Trabajo Peligroso", que el
    auditor habia protegido expresamente como universal. El porcentaje de
    alcanzabilidad NO lo cazo: con 99.86% pasaba de largo. Por eso este chequeo
    es de CERO TOLERANCIA y va aparte del umbral, que existe para el flotante
    historico."""
    src = (BASE / "scripts" / "run_phase1.py").read_text(encoding="utf-8")
    assert "Ningun nodo ACTIVO cuya unica entrada este deprecada" in src, "falta el chequeo"
    cuerpo = src[src.index("fantasmas = []"):src.index("seeds = load_entry_seeds()")]
    assert "all(r in deprecados for r in entradas)" in cuerpo, "no exige que TODAS lo esten"
    assert "if entradas and" in cuerpo, "un nodo sin entradas no es un fantasma, es una raiz"
    assert "not fantasmas" in src, "el chequeo tolera fantasmas"
    print("  ok: el nodo-fantasma-con-nombre tiene su chequeo de cero tolerancia")


def test_todo_activo_tiene_vector_en_el_indice():
    """LA CLASE DE LA TRAMPA SILENCIOSA (ago 2026).

    Al revivir diez nodos deprecados de seleccion, los diez EXISTIAN en el
    grafo, pasaban todos los chequeos, y la brujula era INCAPAZ de encontrarlos:
    el indice semantico se habia construido cuando estaban deprecados, y
    build_semantic_index los excluye a proposito.

    No es un caso, es una CLASE: cualquier cambio de estado de deprecado la
    reproduce, y tambien un nodo nuevo sin reindexar. Un nodo ofrecible que el
    indice no conoce es invisible para el salto semantico y para la prueba de
    rumbos, y NINGUNA DE LAS DOS SE QUEJA: simplemente no lo devuelven nunca.

    Es la misma familia que el nodo-fantasma-con-nombre: existe, tiene titulo, y
    nadie puede llegar a el. Por eso el chequeo es de cero tolerancia."""
    src = (BASE / "scripts" / "run_phase1.py").read_text(encoding="utf-8")
    assert "Todo nodo ACTIVO tiene vector en el indice semantico" in src, "falta el chequeo"
    # El span arranca en REMEDIO, que es donde vive el mensaje, y no en
    # `ruta_indice`: el remedio se extrajo a una constante al arreglar la
    # autodesactivacion, y buscarlo mas abajo lo dejaba fuera.
    cuerpo = src[src.index("REMEDIO = ("):src.index("seeds = load_entry_seeds()")]
    assert "set(activos) - con_vector" in cuerpo, "no compara contra los ACTIVOS"
    assert "not sin_vector" in cuerpo, "el chequeo tolera activos sin vector"
    # ROJO DECLARADO (opcion B extendida, 14 ago 2026): un id nuevo de la
    # pasada, declarado en INDICE_ROJO_DECLARADO.jsonl, se resta ANTES de
    # fallar; cualquier OTRO id sin vector sigue sin tolerancia.
    assert "rojo_declarado = indice_rojo_declarado()" in cuerpo, (
        "el chequeo no consulta la lista de rojo declarado")
    assert "nid in rojo_declarado" in cuerpo, (
        "el chequeo no resta los ids declarados de los que fallan")
    # y el mensaje tiene que decir QUE HACER, no solo que algo esta mal
    assert "corre el reindex ANTES de usar esta copia" in cuerpo, (
        "el aviso no dice que hacer: un fallo sin remedio a la vista se ignora")
    assert "build_semantic_index_voyage.py" in cuerpo, "no nombra el comando"
    # la otra direccion se REPORTA pero no tumba: un vector de mas no hace
    # invisible a nadie, y la puerta unica ya lo filtra al consultar.
    assert "con_vector - set(activos)" in cuerpo, "no reporta los vectores que sobran"

    # LOS DOS FIXTURES DEL CHEQUEO. Todo patron nace con uno que debe cazar y
    # uno que no; este tambien, porque su primera version se AUTODESACTIVABA:
    # estaba envuelto en `if ruta_indice.exists()` y sin el archivo no entraba
    # en la lista. El Gate salia verde sin el chequeo, y un chequeo ausente y
    # uno verde se ven igual en el resumen.

    # (1) CAZA: sin indice en la ruta, el chequeo aparece y FALLA.
    assert "if not ruta_indice.exists():" in cuerpo, (
        "no hay rama para el indice ausente: el chequeo se autodesactiva")
    rama_ausente = cuerpo[cuerpo.index("if not ruta_indice.exists():"):cuerpo.index("else:")]
    assert "False" in rama_ausente, "el indice ausente no hace fallar el chequeo"
    assert "NO HAY INDICE" in rama_ausente, "no dice que el problema es que falta el indice"
    assert "REMEDIO" in rama_ausente, "el caso sin indice no trae el remedio"

    # (2) NO CAZA: con el indice presente y completo, pasa. Se comprueba contra
    # el estado real del repo, que es la unica prueba que no se puede fingir.
    # SALVO los ids que la FASE III declaro al crearlos (opcion B extendida,
    # 14 ago 2026): esos se restan e IMPRIMEN, no tumban el fixture; cualquier
    # otro activo sin vector si lo tumba, sin excepcion.
    import json as _json
    idx = BASE / "web" / "lib" / "assets" / "semantic_index.json"
    assert idx.exists(), "no hay indice en el repo: este fixture no puede correr"
    ids = set(_json.loads(idx.read_text(encoding="utf-8"))["ids"])
    grafo = _json.loads(
        (BASE / "dataset" / "metadata" / "master_graph.json").read_text(encoding="utf-8"))["nodos"]
    activos = {k for k, n in grafo.items() if not n.get("deprecado")}
    faltan = activos - ids
    rojo_declarado = indice_rojo_declarado()
    declarados = sorted(nid for nid in faltan if nid in rojo_declarado)
    sin_declarar = sorted(nid for nid in faltan if nid not in rojo_declarado)
    if declarados:
        print(f"  rojo declarado, {len(declarados)} id(s) (INDICE_ROJO_DECLARADO.jsonl):")
        for nid in declarados:
            operacion, fecha = rojo_declarado[nid]
            print(f"    {nid} ({operacion}, {fecha})")
    assert not sin_declarar, (
        f"hay {len(sin_declarar)} activos sin vector y sin declarar en el repo: "
        f"{sin_declarar[:5]}")

    # Y el chequeo se agrega SIEMPRE, en las dos ramas.
    assert cuerpo.count('"Todo nodo ACTIVO tiene vector en el indice semantico"') == 2, (
        "el chequeo no se agrega en las dos ramas: en una de ellas desaparece del resumen")
    print("  ok: todo activo tiene vector, con sus dos fixtures y sin autodesactivarse")


def main():
    for f in (test_el_nodo_fantasma_con_nombre, test_la_curaduria_real_existe,
              test_suelto_sobre_copia_revertida_grita_y_falla,
              test_via_integrar_packs_limpio_y_callado,
              test_copia_intacta_no_molesta,
              test_jamas_auto_aplica,
              test_todo_activo_tiene_vector_en_el_indice):
        f()
    print("OK: la curaduria revertida grita, falla y jamas se auto-aplica.")


if __name__ == "__main__":
    main()
