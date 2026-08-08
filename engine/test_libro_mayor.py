# -*- coding: utf-8 -*-
"""El libro mayor de costos (docs/COSTOS.jsonl).

LA AVERIA DE ORIGEN (2026-08-08, cierre del ciclo del censo): el fundador pidio
el costo total del ciclo y no se pudo certificar. Cada corrida imprimia lo suyo
y lo escribia en un informe que la corrida siguiente PISABA, asi que al final
solo quedaba la ultima tanda de cada script. La suma tenia que salir de la
memoria del chat.

LA POLITICA: "un numero honesto con su limite declarado vale mas que uno redondo
de memoria." El libro es de APENDICE y las filas rescatadas van marcadas
`parcial`, para que un total con filas dudosas se declare dudoso en vez de
sonar exacto.
"""
import io
import json
import os
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

import libro_mayor  # noqa: E402


def con_libro_temporal(fn):
    """Ejecuta fn contra un libro de usar y tirar; jamas toca el de verdad."""
    real = libro_mayor.LIBRO
    tmp = Path(tempfile.mkdtemp()) / "COSTOS.jsonl"
    libro_mayor.LIBRO = tmp
    try:
        return fn()
    finally:
        libro_mayor.LIBRO = real


def test_anota_las_cuatro_cosas_pedidas():
    def cuerpo():
        libro_mayor.anotar("quality", "re-voz", 0.6789, nodos=33)
        (fila,) = libro_mayor.leer()
        for campo in ("fecha", "pack", "operacion", "costo_usd"):
            assert campo in fila, f"falta {campo}: el encargo pedia los cuatro"
        assert fila["pack"] == "quality" and fila["operacion"] == "re-voz"
        assert fila["costo_usd"] == 0.6789, "el costo se redondeo y perdio centavos"
        assert fila["nodos"] == 33, "el extra no llego al libro"
        assert fila["fecha"].startswith("20"), fila["fecha"]
    con_libro_temporal(cuerpo)
    print("  ok: anota fecha, pack, operacion y costo (mas lo que le pasen)")


def test_es_de_apendice_jamas_reescribe():
    # Si una corrida pudiera pisar a otra volveria la averia de origen con otro
    # disfraz: el libro entero existe para que eso sea imposible.
    def cuerpo():
        for i in range(3):
            libro_mayor.anotar("exportacion", "consolidacion", 0.10, ronda=i)
        filas = libro_mayor.leer()
        assert len(filas) == 3, f"se pisaron corridas: quedaron {len(filas)}"
        assert [f["ronda"] for f in filas] == [0, 1, 2], "el orden no es el de llegada"
        assert libro_mayor.total(filas) == 0.30
    con_libro_temporal(cuerpo)
    print("  ok: tres corridas, tres lineas; el libro solo crece")


def test_anotar_jamas_tumba_la_corrida():
    # El trabajo ya se hizo y ya se pago. Un disco lleno no puede convertir una
    # corrida exitosa de $0.70 en una excepcion.
    def cuerpo():
        libro_mayor.LIBRO = Path(tempfile.mkdtemp()) / "no" / "existe"
        os.makedirs(libro_mayor.LIBRO.parent.parent, exist_ok=True)
        # un archivo donde deberia ir el directorio: mkdir fallara
        libro_mayor.LIBRO.parent.write_text("soy un archivo", encoding="utf-8")
        assert libro_mayor.anotar("quality", "re-voz", 1.0) is None
    con_libro_temporal(cuerpo)
    print("  ok: si no puede anotar, avisa y devuelve None; no lanza")


def test_el_total_declara_su_limite():
    def cuerpo():
        libro_mayor.anotar("quality", "consolidacion", 0.06, parcial=True)
        libro_mayor.anotar("quality", "re-voz", 0.20)
        filas = libro_mayor.leer()
        assert libro_mayor.total(filas) == 0.26
        assert any(f.get("parcial") for f in filas), (
            "sin la marca `parcial` un total con filas rescatadas sonaria exacto")
    con_libro_temporal(cuerpo)
    print("  ok: las filas rescatadas van marcadas y el total se declara dudoso")


def test_deduce_el_pack_de_la_ruta_del_lote():
    # re-voz recibe --lote packs/<pack>/poda/<archivo>, no --pack.
    assert libro_mayor.pack_del_lote("packs/exportacion/poda/_revoz_cierre_ciclo.json") == "exportacion"
    assert libro_mayor.pack_del_lote(BASE / "packs" / "quality" / "poda" / "x.json") == "quality"
    assert libro_mayor.pack_del_lote("docs/algo.json") is None, "invento un pack donde no habia"
    print("  ok: deduce el pack del lote, y devuelve None cuando no hay")


def test_los_dos_scripts_anotan_de_verdad():
    """El remache: el encargo era 'las dos lineas en revoz_pack y consolidar_pack'.
    Un libro que existe pero que nadie llama es peor que no tenerlo, porque su
    total en cero se lee como 'el ciclo no costo nada'."""
    for script, op in (("revoz_pack.py", '"re-voz"'), ("consolidar_pack.py", '"consolidacion"')):
        src = (BASE / "scripts" / script).read_text(encoding="utf-8")
        assert "import libro_mayor" in src, f"{script} no importa el libro"
        assert f"libro_mayor.anotar(" in src, f"{script} no anota"
        assert op in src, f"{script} no dice que operacion fue"
        # y anota lo que REALMENTE costo, no una constante
        cuerpo = src[src.index("libro_mayor.anotar("):]
        assert "costo" in cuerpo[:200], f"{script} anota algo que no es el costo calculado"
    print("  ok: los dos scripts importan el libro y anotan su costo real")


def test_el_libro_de_verdad_esta_bien_formado():
    ruta = BASE / "docs" / "COSTOS.jsonl"
    assert ruta.exists(), "el libro no existe en docs/"
    filas = [json.loads(l) for l in io.open(ruta, encoding="utf-8").read().splitlines() if l.strip()]
    assert filas, "el libro esta vacio"
    assert filas[0]["operacion"] == "apertura-del-libro", (
        "la primera linea debe decir POR QUE el libro nace tarde")
    assert "memoria" in filas[0]["nota"], "la apertura no deja dicha la politica"
    for f in filas[1:]:
        assert f.get("parcial") is True, (
            f"{f['pack']}/{f['operacion']}: es del ciclo viejo y no esta marcada parcial")
        assert "origen" in f, "una fila rescatada sin decir de donde salio"
    print(f"  ok: el libro real trae {len(filas)} filas, todas las viejas marcadas")


def main():
    for f in (test_anota_las_cuatro_cosas_pedidas, test_es_de_apendice_jamas_reescribe,
              test_anotar_jamas_tumba_la_corrida, test_el_total_declara_su_limite,
              test_deduce_el_pack_de_la_ruta_del_lote, test_los_dos_scripts_anotan_de_verdad,
              test_el_libro_de_verdad_esta_bien_formado):
        f()
    print("OK: el libro mayor apendiza, declara su limite y nadie lo puede pisar.")


if __name__ == "__main__":
    main()
