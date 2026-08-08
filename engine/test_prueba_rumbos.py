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


def test_las_tres_clases_de_rumbo():
    """Adjudicadas ago 2026, al ampliar el banco para poder operar el nucleo.

    - VARA: cuenta en el marcador y en el trinquete.
    - DIAGNOSTICO: mide un trabajo que TODAVIA NO SE HA HECHO (la fusion y
      re-voz del nucleo). Contarlo seria pedirle al trinquete que vigile algo
      que ya sabemos que esta mal, y un guardian que siempre esta rojo no
      guarda nada. Lleva su `expectativa` escrita al lado.
    - HUECO: documenta un VACIO del catalogo, no una punteria.

    Y la clave del asunto: los de fuera NO entran en `por_rumbo`. Si entraran,
    el dia que un diagnostico se ponga verde -- que es justo lo que se espera
    de el -- el trinquete lo leeria como 'mejora' y nadie lo adjudicaria."""
    src = CORREDOR.read_text(encoding="utf-8")
    banco = json.loads(BANCO.read_text(encoding="utf-8"))["rumbos"]

    diag = [r for r in banco if r.get("diagnostico")]
    hueco = [r for r in banco if r.get("hueco")]
    assert len(diag) == 5, f"los cinco de punteria mala son 5, hay {len(diag)}"
    assert len(hueco) == 1, f"el rumbo-hueco es 1, hay {len(hueco)}"
    for r in diag:
        assert r.get("expectativa"), f"{r['id']}: diagnostico sin expectativa escrita"
        assert "VERDE" in r["expectativa"], f"{r['id']}: no dice que debe pasar"
    assert not hueco[0].get("ancla") and not hueco[0].get("ancla_conjunto"), (
        "al rumbo-hueco le inventaron un ancla: documenta que la respuesta NO existe")

    assert 'r.get("diagnostico") or r.get("hueco")' in src, "el corredor no conoce las clases"
    assert 'if not fuera:' in src, "los de fuera cuentan en el marcador"
    assert 'if not x["fuera_del_marcador"]' in src, "los de fuera entran en por_rumbo"
    assert "FUERA DEL MARCADOR" in src, "no se imprimen aparte"
    print(f"  ok: {len(diag)} de diagnostico y {len(hueco)} hueco, fuera del marcador y a la vista")


def test_el_ancla_por_conjunto():
    """Permitida en el nucleo: hay preguntas con varias respuestas legitimas, y
    fingir una sola vara unica es menos honesto que declarar el abanico.
    `ancla` exige TODAS; `ancla_conjunto` exige AL MENOS UNA."""
    src = CORREDOR.read_text(encoding="utf-8")
    assert "ancla_conjunto" in src, "el corredor no lee el ancla por conjunto"
    assert "not any(a in ids_top for a in conjunto)" in src, "no exige al menos una"
    banco = json.loads(BANCO.read_text(encoding="utf-8"))
    conj = [r for r in banco["rumbos"] if r.get("ancla_conjunto")]
    assert conj, "no hay ninguno"
    grafo = json.loads(
        (BASE / "dataset" / "metadata" / "master_graph.json").read_text(encoding="utf-8"))["nodos"]
    for r in conj:
        assert 2 <= len(r["ancla_conjunto"]) <= 4, f"{r['id']}: el conjunto es de 2 a 4"
        assert not r.get("ancla"), f"{r['id']}: tiene las dos formas de ancla"
        for a in r["ancla_conjunto"]:
            assert a in grafo, f"{r['id']}: {a} no existe"
            assert not grafo[a].get("deprecado"), f"{r['id']}: {a} esta deprecado"
    # y la regla queda escrita donde se lee sin abrir el codigo
    reglas = banco["_reglas"]
    assert "se corrige el ancla, no el catalogo" in reglas["el_ancla_se_corrige_contra_la_realidad"]
    assert "jamas el automatismo" in reglas["el_ancla_se_corrige_contra_la_realidad"], (
        "falta lo que impide que el banco se auto-corrija con la salida de hoy")
    print(f"  ok: {len(conj)} rumbos con ancla por conjunto, todas verificadas contra el grafo")


def test_ninguna_frontera_usa_la_clave_equivocada():
    """CAZADO EN LA FASE 0: tres fronteras nuevas se escribieron con `prohibido`
    y el corredor lee `prohibido_top3`. No fallaron: PASARON, verdes por dominio,
    con su chequeo de frontera sin aplicar nunca. Una baranda mal escrita no se
    queja, y por eso hace falta esto."""
    banco = json.loads(BANCO.read_text(encoding="utf-8"))["rumbos"]
    src = CORREDOR.read_text(encoding="utf-8")
    assert 'r.get("prohibido_top3")' in src
    malas = [r["id"] for r in banco if "prohibido" in r]
    assert not malas, f"estos usan una clave que nadie lee: {malas}"
    con = [r for r in banco if r.get("prohibido_top3")]
    assert len(con) >= 6, f"solo {len(con)} fronteras"
    print(f"  ok: las {len(con)} fronteras usan la clave que el corredor lee de verdad")


def test_el_trinquete_existe_y_tiene_sus_tres_salidas():
    """La punteria solo sube o canta. Tres salidas distintas, y la de MEJORA
    tambien para: un trinquete que deja pasar las mejoras sin registrarlas se
    afloja solo, porque la vara se queda vieja y deja de medir."""
    src = CORREDOR.read_text(encoding="utf-8")
    for nombre in ("SALIDA_OK = 0", "SALIDA_DERIVA = 1", "SALIDA_MEJORA = 2"):
        assert nombre in src, f"falta {nombre}"
    assert "K = 10" in src and "TOP_FRONTERA = 3" in src, "los umbrales aprobados cambiaron"
    # las tres guardas, en orden: rojos, ambares que crecen, y la mejora
    assert 'marcador["rojo"] or deprecados_ofrecidos' in src, "no corta con rojos"
    assert 'ambar_conocidos > base["marcador"]["ambar"]' in src, "no corta si crecen los ambares"
    assert "return SALIDA_MEJORA" in src, "una mejora no pide re-committear la vara"


def test_ampliar_el_banco_no_es_deriva():
    """Cazado al ampliar el banco de 30 a 48 para poder operar el nucleo (ago
    2026): el trinquete comparaba CONTEOS BRUTOS de ambares, asi que 18 rumbos
    nuevos lo hicieron gritar DERIVA cuando ninguno de los 30 originales se
    habia movido un milimetro.

    Un guardian que grita cuando le amplias la ronda deja de creerse, y ese es
    el peor final para un guardian. Pero un rumbo nuevo en ambar TAMPOCO se
    calla: es una debilidad que el banco viejo no veia, y hornearla en la linea
    base sin decirlo seria estrenar la ceguera."""
    src = CORREDOR.read_text(encoding="utf-8")
    # se cuenta sobre los rumbos que la vara conocia, no sobre el banco entero
    assert "conocidos = set(base[\"por_rumbo\"])" in src, "no acota al conjunto conocido"
    for var in ("ambar_conocidos", "verde_conocidos"):
        assert f"{var} = sum(" in src, f"{var} no se calcula sobre los conocidos"
        assert f'if rid in conocidos' in src, "el conteo no filtra por conocidos"
    # el rumbo nuevo no-verde se nombra, uno por uno
    assert "estrenos" in src, "los rumbos nuevos no se listan aparte"
    assert "RUMBOS NUEVOS QUE NO SALEN VERDES" in src, "no los canta"
    assert 'ahora["estado"] != "verde"' in src, "canta tambien los nuevos que salen verdes"
    # y salir con estrenos NO es OK: la vara se re-committea a proposito
    bloque = src[src.index("    if estrenos:", src.index("verde_conocidos = sum(")):]
    assert "return SALIDA_MEJORA" in bloque[:300], (
        "con estrenos sin adjudicar la corrida sale 0 y el ciclo sigue sin que nadie mire")
    print("  ok: ampliar el banco no es deriva, y un estreno en ambar no pasa callado")
    # y el banco declara los umbrales, para que se lean sin abrir el codigo
    u = json.loads(BANCO.read_text(encoding="utf-8"))["_umbrales"]
    assert u["K"] == 10 and u["top_frontera"] == 3
    print("  ok: trinquete con sus tres salidas y los umbrales aprobados")


def main():
    for f in (test_el_banco_cubre_el_catalogo, test_hay_rumbos_trampa_de_frontera,
              test_los_ids_de_ancla_existen_de_verdad, test_las_dos_puertas_dicen_lo_mismo,
              test_la_linea_base_esta_committeada,
              test_el_trinquete_existe_y_tiene_sus_tres_salidas,
              test_ampliar_el_banco_no_es_deriva, test_las_tres_clases_de_rumbo,
              test_el_ancla_por_conjunto, test_ninguna_frontera_usa_la_clave_equivocada):
        f()
    print("OK: el banco de rumbos y su puerta sostienen.")


if __name__ == "__main__":
    main()
