# -*- coding: utf-8 -*-
"""La baranda anti invencion de cifras, digitos y palabras.

EL ORIGEN (cirugia 1 del gradiente, ago 2026): `RE_CIFRA` era `\\d+` y solo veia
DIGITOS. Un peldano reencuadrado volvio con un ejemplo inventado escrito en
palabras, "no es lo mismo un veinte por ciento que un cuarenta y cinco", y la
baranda no lo vio. Se quito a mano.

EL ALCANCE ES ESTRECHO A PROPOSITO. Se midio primero sobre los 3.521 nodos
activos: un detector de numerales sueltos marcaria 2.488 nodos, el 70,7 por
ciento del catalogo, porque en espanol `un`, `una`, `dos` son articulos y
cuantificadores genericos. Fracciones, frecuencias y ordinales viven con DOS
sentidos en el mismo catalogo ("la mitad de los visitantes" contra "la primera
mitad de la llamada"). Todo eso queda fuera, y lo cubre la lectura del lote, que
es justo como se cazo el primer caso.

    "Una baranda que caza lo correcto no es estricta, esta rota."
"""
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

from cifras import cifras_de, cifras_nuevas  # noqa: E402


def test_DEBE_CAZAR_lo_que_se_adjudico():
    """Las tres clases del alcance adjudicado."""
    casos = [
        ("un veinte por ciento de tus clientes", "el compuesto exacto <numeral> por ciento"),
        ("cuarenta y cinco", "el compuesto de decena con unidad"),
        ("revisa cien pedidos", "la centena como cuantificador"),
        ("mas de mil millones", "el mil como palabra"),
        ("noventa por ciento de las veces", "otro porcentaje escrito"),
        ("cuesta 45 dolares", "los digitos de siempre, que no se pierden"),
    ]
    for t, por_que in casos:
        assert cifras_de(t), f"no cazo ({por_que}): {t!r}"
    print(f"  ok: caza las {len(casos)} formas del alcance adjudicado")


def test_NO_DEBE_CAZAR_lo_que_quedo_fuera():
    """La otra mitad, y la que mas ha costado en este proyecto. Cada caso viene
    del catalogo REAL, no de laboratorio: se buscaron en los 3.521 nodos."""
    casos = [
        ("cajas de doble pared", "un tipo de caja, no un multiplicador"),
        ("numero par de miembros", "paridad, no 'un par de'"),
        ("resolver de una vez los problemas", "modismo: definitivamente"),
        ("una vez por semana", "frecuencia, fuera del alcance"),
        ("la primera mitad de la llamada", "posicion, no fraccion"),
        ("la mitad de la llamada", "fraccion, fuera del alcance"),
        ("primero mide, segundo decide, tercero ajusta", "marcadores de discurso"),
        ("el metodo MIL-STD-105D no lleva palabras", "MIL dentro de un nombre propio"),
        ("existen tres tipos de canal", "cuantificador generico"),
        ("una solucion rapida", "articulo"),
        ("la ciencia del cliente", "'cien' dentro de otra palabra"),
        ("un milagro cualquiera", "'mil' dentro de otra palabra"),
        ("Mil Millones en mayuscula", "no es minuscula: la regla de tokenizacion"),
    ]
    malos = []
    for t, por_que in casos:
        # se ignoran los digitos, que son la regla vieja y no se juzga aqui
        c = {x for x in cifras_de(t) if not re.fullmatch(r"\d+(?:[.,]\d+)?", x)}
        if c:
            malos.append((t, por_que, sorted(c)))
    assert not malos, f"la extension caza lo correcto: {malos}"
    print(f"  ok: los {len(casos)} casos grises del catalogo real quedan fuera")


def test_la_regla_de_tokenizacion_resuelve_MIL_STD_sin_lista_de_exenciones():
    """La adjudicacion decidio NO tener lista de exenciones: MIL-STD cae solo,
    por la regla de que se matchean palabras completas en minuscula y jamas
    subcadenas de tokens con mayusculas, guiones o digitos pegados."""
    from cifras import RE_NUMERAL_GRANDE
    for t in ("el metodo MIL-STD-105D", "el metodo mil-std-105d", "norma MIL2000"):
        assert not RE_NUMERAL_GRANDE.search(t), f"la palabra casa dentro de un token: {t!r}"
    # y la misma palabra suelta y en minuscula SI casa
    assert RE_NUMERAL_GRANDE.search("mas de mil pedidos")
    print("  ok: MIL-STD cae por tokenizacion, sin lista de exenciones")


def test_LA_SEMANTICA_DE_DIFF_ESTA_INTACTA():
    """Lo que ya estaba en el original JAMAS dispara. Es toda la baranda: sin
    esto, cualquier nodo que hable de porcentajes seria irreescribible."""
    assert cifras_nuevas("subio un veinte por ciento",
                         "el crecimiento fue de un veinte por ciento") == []
    assert cifras_nuevas("cuesta 45 dolares", "cuesta 45 dolares") == []
    assert cifras_nuevas("subio un veinte por ciento", "el crecimiento fue bueno")
    # y con varias fuentes, como la usa el consolidador
    assert cifras_nuevas("mil clientes", ["hola", "tenemos mil clientes"]) == []
    print("  ok: solo la aparicion NUEVA dispara, con una fuente y con varias")


def test_los_dos_scripts_usan_LA_MISMA_baranda():
    """Estaba duplicada en revoz_pack y consolidar_pack. Una regla repartida en
    varios sitios no falla de golpe: falla en el que alguien olvido actualizar."""
    for script in ("revoz_pack.py", "consolidar_pack.py"):
        src = (BASE / "scripts" / script).read_text(encoding="utf-8")
        assert "from cifras import cifras_nuevas" in src, f"{script} no usa la fuente unica"
        assert "RE_CIFRA = re.compile" not in src, f"{script} conserva su copia de la regla"
    print("  ok: los dos scripts leen la misma baranda, y ninguno guarda copia")


def test_PASADA_EN_SECO_sobre_el_catalogo_real():
    """Cada nodo activo contra SI MISMO: por la semantica de diff tiene que dar
    CERO. Un solo disparo aqui seria un defecto de construccion."""
    nodos = [json.loads(p.read_text(encoding="utf-8"))
             for p in (BASE / "dataset" / "nodos").glob("*.json")]
    act = [x for x in nodos if not x.get("deprecado")]
    assert len(act) > 3000, f"solo {len(act)} activos: el catalogo no se cargo"
    disparos = []
    for x in act:
        t = " ".join([x["titulo_concepto"], x["resumen_teorico"],
                      " ".join(x["pasos_accionables"]), x.get("entregable_esperado") or "",
                      " ".join(x.get("condiciones_activacion") or [])])
        if cifras_nuevas(t, t):
            disparos.append(x["node_id"])
    assert not disparos, f"la baranda dispara contra el catalogo intacto: {disparos[:5]}"
    print(f"  ok: cero disparos sobre los {len(act)} nodos activos comparados consigo mismos")


def main():
    for f in (test_DEBE_CAZAR_lo_que_se_adjudico,
              test_NO_DEBE_CAZAR_lo_que_quedo_fuera,
              test_la_regla_de_tokenizacion_resuelve_MIL_STD_sin_lista_de_exenciones,
              test_LA_SEMANTICA_DE_DIFF_ESTA_INTACTA,
              test_los_dos_scripts_usan_LA_MISMA_baranda,
              test_PASADA_EN_SECO_sobre_el_catalogo_real):
        f()
    print("OK: la baranda ve las cifras en palabras y no toca lo que ya estaba.")


if __name__ == "__main__":
    main()
