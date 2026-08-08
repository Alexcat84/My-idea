# -*- coding: utf-8 -*-
"""La prueba de rumbos: su banco y su puerta.

Esto NO corre la prueba (necesita clave de Voyage y red). Custodia lo que se
puede romper sin que nadie lo note:

  1. que el banco siga cubriendo el catalogo entero,
  2. que la puerta del corredor sea LA MISMA que la del motor.

El punto 2 es el importante. El corredor es Python y la puerta de produccion es
TypeScript, asi que hay dos escrituras de la misma regla. Es la clase de copia
que esta casa persigue, y aqui no habia forma de evitarla: lo que si hay es un
test que compara las dos y canta si se separan. Si mañana esOfrecible gana una
condicion y el corredor no, la prueba de rumbos medira un motor que ya no existe
y seguira en verde.
"""
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
BANCO = BASE / "scripts" / "rumbos" / "banco_rumbos.json"
CORREDOR = BASE / "scripts" / "rumbos" / "prueba_rumbos.py"
PUERTA_TS = BASE / "web" / "lib" / "engine" / "graph.ts"

DOMINIOS = ["core", "quality", "health_safety", "environmental", "seguridad_digital",
            "exportacion", "franquicias", "risk_management", "compras", "entrega"]


def test_el_banco_cubre_el_catalogo():
    rumbos = json.loads(BANCO.read_text(encoding="utf-8"))["rumbos"]
    cubiertos = {d for r in rumbos for d in r["dominios"]}
    faltan = [d for d in DOMINIOS if d not in cubiertos]
    assert not faltan, f"el banco no cubre: {faltan}"
    assert len(rumbos) >= 25, f"solo {len(rumbos)} rumbos; el encargo pedia ~30"
    print(f"  ok: {len(rumbos)} rumbos cubren los {len(DOMINIOS)} dominios")


def test_hay_rumbos_trampa_de_frontera():
    rumbos = json.loads(BANCO.read_text(encoding="utf-8"))["rumbos"]
    trampas = [r for r in rumbos if r.get("prohibido_top3")]
    assert len(trampas) >= 3, f"solo {len(trampas)} trampas de frontera; el encargo pedia 3-4"
    # Y la frontera nombrada expresamente en el encargo tiene que estar.
    ids = {r["id"] for r in trampas}
    assert any("empaque_domestico" in i for i in ids), "falta la frontera empaque domestico/exportacion"
    assert any("proveedor" in i for i in ids), "falta la frontera falla de proveedor/compras"
    print(f"  ok: {len(trampas)} rumbos-trampa, con las dos fronteras nombradas en el encargo")


def test_los_ids_de_ancla_existen_de_verdad():
    """Un ancla mal escrita convierte un rumbo en ambar para siempre y nadie
    sabe por que: parece que la brujula falla cuando falla el banco."""
    grafo = json.loads(
        (BASE / "dataset" / "metadata" / "master_graph.json").read_text(encoding="utf-8"))["nodos"]
    rumbos = json.loads(BANCO.read_text(encoding="utf-8"))["rumbos"]
    malas = [(r["id"], a) for r in rumbos for a in (r.get("ancla") or []) if a not in grafo]
    assert not malas, f"anclas que no existen en el grafo: {malas}"
    # y ninguna puede estar deprecada: seria pedirle a la brujula que ofrezca
    # justo lo que la puerta le prohibe ofrecer.
    depre = [(r["id"], a) for r in rumbos for a in (r.get("ancla") or [])
             if grafo[a].get("deprecado")]
    assert not depre, f"anclas DEPRECADAS: {depre}"
    print("  ok: todas las anclas del banco existen y ninguna esta deprecada")


def test_las_dos_puertas_dicen_lo_mismo():
    """El corredor replica esOfrecible en Python. Si una gana una condicion y la
    otra no, la prueba mide un motor que ya no existe."""
    ts = PUERTA_TS.read_text(encoding="utf-8")
    cuerpo_ts = ts[ts.index("export function esOfrecible"):]
    cuerpo_ts = cuerpo_ts[:cuerpo_ts.index("\n}")]
    py = CORREDOR.read_text(encoding="utf-8")
    cuerpo_py = py[py.index("def puerta("):]
    cuerpo_py = cuerpo_py[:cuerpo_py.index("\ndef ")]

    # Las tres condiciones, escritas distinto en cada lengua pero presentes.
    assert "if (!n) return false" in cuerpo_ts and "if not n:" in cuerpo_py, \
        "una de las dos puertas dejo de comprobar que el nodo exista"
    assert "n.deprecado" in cuerpo_ts and 'n.get("deprecado")' in cuerpo_py, \
        "una de las dos puertas dejo de comprobar la deprecacion"
    assert "dominio" in cuerpo_ts and "dominio" in cuerpo_py, \
        "una de las dos puertas dejo de comprobar el dominio"

    # Y la cuenta de condiciones: si alguien anade una cuarta a la de TS, aqui
    # se entera. Se cuentan los `return false` / `if` de decision.
    condiciones_ts = len(re.findall(r"if \(", cuerpo_ts))
    assert condiciones_ts == 2, (
        f"esOfrecible tiene {condiciones_ts} guardas y el corredor esta escrito para 2. "
        "Si le anadiste una condicion, replicala en scripts/rumbos/prueba_rumbos.py")
    print("  ok: la puerta del corredor y la del motor comprueban lo mismo")


def test_la_linea_base_esta_committeada():
    lb = BASE / "scripts" / "rumbos" / "linea_base_rumbos.json"
    assert lb.exists(), "sin linea base no hay deriva que cantar"
    base = json.loads(lb.read_text(encoding="utf-8"))
    assert base["marcador"]["rojo"] == 0, f"la linea base tiene rojos: {base['marcador']}"
    assert not base.get("deprecados_ofrecidos"), "la linea base ofrece deprecados"
    print(f"  ok: linea base con {base['verde_pct']}% verde, 0 rojos, 0 deprecados")


def main():
    for f in (test_el_banco_cubre_el_catalogo, test_hay_rumbos_trampa_de_frontera,
              test_los_ids_de_ancla_existen_de_verdad, test_las_dos_puertas_dicen_lo_mismo,
              test_la_linea_base_esta_committeada):
        f()
    print("OK: el banco de rumbos y su puerta sostienen.")


if __name__ == "__main__":
    main()
