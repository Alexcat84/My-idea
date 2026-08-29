# -*- coding: utf-8 -*-
r"""vuelta135_tabla_mapeo_propuesto.py . TAREA 4.b de la vuelta 135: rehace
docs/plan/OP_S_11_MAPEO_PROPUESTO.md con la cola de localizador extendida a
`Caps?\.` (TAREA 4.a, `vuelta135_cola_localizador_cap.py`), ADJUDICADA por
el auditor (acta 134, 3.3), atada AL PREFIJO SOBRE RECORTADA igual que la
133 ato la extension de Apendice: el SEXTO peldano es la MISMA cadena de
las cinco reglas pero con la cola extendida a `Caps?\.` en TODOS los
sitios donde la cadena usa la cola (el agrupamiento por igualdad de la
forma recortada Y el prefijo sobre la recortada), no un incremento pegado
detras del 104.

MISMAS CUATRO COLUMNAS de las vueltas 130 a 133 (grafia, canonica
propuesta, motivo, bolsa). Reusa `vuelta133_tabla_mapeo_propuesto.py`
salvo en el recortador (usa `recortar_localizador_con_cap` de
`vuelta135_cola_localizador_cap.py` en vez de
`recortar_localizador_con_apendice`), sin reimplementar el union-find ni
la particion de bolsa 2 (`vuelta132_bolsa2_particion.py`).

LA CONSECUENCIA QUE SE MIRA CON LOS OJOS ABIERTOS: con la cola extendida a
`Caps?\.`, el catalogo pasa de 104 a 54 grupos (rebasa por UNO la meta de
55 de `05_SANEO.md`, 11 ago 2026, coste declarado, no escondido) y las
canonicas SINTETICAS del censo pasan de 0 a 3 (grupos multi miembro sin
libro: Edwards et al., DeMarco y Lister, Hubbard). La regla SINTETICA
(NOVENA entrada de la ficha `fuente`) NO SE BORRA, NO SE MARCA MUERTA:
sigue vigente y con caso en este corte.

No aplica la tabla a ningun nodo. `OP-S-11` sigue LISTA.

Salida: docs/plan/OP_S_11_MAPEO_PROPUESTO.md (unico fichero viejo que esta
vuelta puede cambiar de contenido, REGIMEN A CON LINEA VIEJA)

Uso:
  python scripts/loop/vuelta135_tabla_mapeo_propuesto.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta131_grupos_por_titulo import (  # noqa: E402
    cargar_censo,
    prefijo_cadena_entera_une,
    prefijo_titulo_une,
    resto_de,
    UnionFind,
)
from vuelta135_cola_localizador_cap import recortar_localizador_con_cap as recortar  # noqa: E402
from vuelta132_bolsa2_particion import RESIDUALES, PROPUESTA_FORASTERA, sondar, titulo_de  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DESTINO = os.path.join(RAIZ, "docs", "plan", "OP_S_11_MAPEO_PROPUESTO.md")
META_LIBROS_CANONICOS = 55
GUARDA_LONGITUD = 20


def prefijo_recortada_une(a, b):
    """La regla de la TAREA 4.b de la 133 (prefijo estricto sobre la forma
    recortada), ATADA aqui a la cola CON CAP de la TAREA 4.a de la 135:
    guarda de longitud >=20 y guarda de RESTO por simetria con la regla de
    titulo."""
    if a == b:
        return False
    ca, cb = recortar(a), recortar(b)
    if ca == cb:
        return False
    corto, largo = (ca, cb) if len(ca) <= len(cb) else (cb, ca)
    if not largo.startswith(corto):
        return False
    if len(corto) < GUARDA_LONGITUD:
        return False
    ra, rb = resto_de(a), resto_de(b)
    if ra and rb and not (ra.startswith(rb) or rb.startswith(ra)):
        return False
    return True


def calcular_bolsa2():
    bolsa = {}
    for grafia, _n in RESIDUALES:
        titulo = titulo_de(grafia)
        _prefijo, por_titulo = sondar(titulo)
        if por_titulo:
            titulo_completo = max(por_titulo, key=lambda t: len(por_titulo[t]))
            primero = sorted(set(por_titulo[titulo_completo]))[0]
            bolsa[grafia] = "2a %s" % primero
        else:
            assert grafia in PROPUESTA_FORASTERA
            bolsa[grafia] = "2b FORASTERO"
    return bolsa


def construir_uf(grafias):
    uf = UnionFind(grafias)
    for a in grafias:
        for b in grafias:
            if prefijo_cadena_entera_une(a, b):
                uf.une(a, b)
    for a in grafias:
        for b in grafias:
            if prefijo_titulo_une(a, b):
                uf.une(a, b)
    buck = {}
    for g in grafias:
        buck.setdefault(recortar(g), []).append(g)
    for _, miembros in buck.items():
        base = miembros[0]
        for m in miembros[1:]:
            uf.une(base, m)
    for a in grafias:
        for b in grafias:
            if prefijo_recortada_une(a, b):
                uf.une(a, b)
    return uf


def calcular():
    censo = cargar_censo()
    grafias = sorted(censo.keys())
    uf = construir_uf(grafias)

    grupos = {}
    for g in grafias:
        grupos.setdefault(uf.find(g), []).append(g)

    canonica_de = {}
    origen_de = {}
    for r, miembros in grupos.items():
        if len(miembros) == 1:
            canonica_de[r] = miembros[0]
            continue
        libros = [m for m in miembros if recortar(m) == m]
        vieja = max(miembros, key=len)
        if not libros:
            canonica_de[r] = recortar(vieja)
            origen_de[r] = "SINTETICA"
        else:
            nueva = max(libros, key=len)
            canonica_de[r] = nueva
            origen_de[r] = "la propia grafia" if nueva == vieja else "recorte de localizador"

    bolsa2 = calcular_bolsa2()

    filas = []
    for g in grafias:
        r = uf.find(g)
        miembros = grupos[r]
        canonica = canonica_de[r]
        if len(miembros) == 1:
            motivo = "SIN AGRUPAR (pide decision)"
        else:
            conecta_cadena = any(m != g and prefijo_cadena_entera_une(g, m) for m in miembros)
            conecta_titulo = any(m != g and prefijo_titulo_une(g, m) for m in miembros)
            conecta_localizador = any(m != g and recortar(g) == recortar(m) for m in miembros)
            conecta_prefijo = any(m != g and prefijo_recortada_une(g, m) for m in miembros)
            if conecta_cadena:
                regla = "cadena entera"
            elif conecta_titulo:
                regla = "titulo"
            elif conecta_localizador:
                regla = "localizador"
            elif conecta_prefijo:
                regla = "prefijo sobre recortada"
            else:
                regla = "SIN AGRUPAR DIRECTO (transitivo)"
            motivo = "MECANICO: agrupa por %s, canonica %s" % (regla, origen_de[r])
        bolsa = bolsa2.get(g, "")
        filas.append((g, canonica, motivo, bolsa))

    return censo, grafias, grupos, filas, origen_de


def contar(grafias, reglas_acumuladas):
    uf = UnionFind(grafias)
    for regla in reglas_acumuladas:
        for a in grafias:
            for b in grafias:
                if regla(a, b):
                    uf.une(a, b)
    return len({uf.find(g) for g in grafias})


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    censo, grafias, grupos, filas, origen_de = calcular()

    total_grafias = len(grafias)
    total_grupos = len(grupos)
    multi = {r: m for r, m in grupos.items() if len(m) > 1}
    sin_agrupar_n = sum(1 for r, m in grupos.items() if len(m) == 1)
    en_grupo_n = total_grafias - sin_agrupar_n
    colapsos_faltan = max(0, total_grupos - META_LIBROS_CANONICOS)
    rebase = max(0, META_LIBROS_CANONICOS - total_grupos)
    n_sinteticas = sum(1 for v in origen_de.values() if v == "SINTETICA")

    # Los SEIS peldanos historicos, cada uno con la cadena de reglas que le
    # corresponde en la vuelta en que se midio (docstring del modulo).
    n_cadena = contar(grafias, [prefijo_cadena_entera_une])
    n_titulo = contar(grafias, [prefijo_cadena_entera_une, prefijo_titulo_une])

    from vuelta132_grupos_por_localizador import recortar_localizador as recortar_vieja_132

    def regla_localizador_vieja_132(a, b):
        return a != b and recortar_vieja_132(a) == recortar_vieja_132(b)
    n_localizador_vieja = contar(grafias, [prefijo_cadena_entera_une, prefijo_titulo_une,
                                            regla_localizador_vieja_132])

    from vuelta133_cola_localizador_apendice import recortar_localizador_con_apendice

    def regla_localizador_apendice(a, b):
        return a != b and recortar_localizador_con_apendice(a) == recortar_localizador_con_apendice(b)
    n_apendice = contar(grafias, [prefijo_cadena_entera_une, prefijo_titulo_une,
                                   regla_localizador_apendice])

    def prefijo_recortada_apendice_une(a, b):
        if a == b:
            return False
        ca = recortar_localizador_con_apendice(a)
        cb = recortar_localizador_con_apendice(b)
        if ca == cb:
            return False
        corto, largo = (ca, cb) if len(ca) <= len(cb) else (cb, ca)
        if not largo.startswith(corto):
            return False
        if len(corto) < GUARDA_LONGITUD:
            return False
        ra, rb = resto_de(a), resto_de(b)
        if ra and rb and not (ra.startswith(rb) or rb.startswith(ra)):
            return False
        return True
    n_prefijo_apendice = contar(grafias, [prefijo_cadena_entera_une, prefijo_titulo_une,
                                           regla_localizador_apendice, prefijo_recortada_apendice_une])

    n_cap = total_grupos

    cabecera = """# OP-S-11: tabla de mapeo PROPUESTA del campo `fuente`

**PROPUESTA MEDIDA, escrita en la vuelta 130 (TAREA 3.b), REHECHA en la vuelta 131 (TAREA 3.c), REHECHA en la vuelta 132 (TAREA 3.e), REHECHA en la vuelta 133 (TAREA 4.d) con Apendice en la cola y el prefijo sobre la forma recortada APLICADO, y REHECHA OTRA VEZ en la vuelta 135 (TAREA 4.b) con la cola de localizador extendida a `Caps?.` (adjudicado por el auditor, acta 134, 3.3), ATADA al prefijo sobre la forma recortada. NO se ha aplicado a ningun nodo: `OP-S-11` sigue LISTA, sin tocar, y esta tabla no cambia su estado. LAS REGLAS MECANICAS LAS ADJUDICA EL AUDITOR EN SU ACTA; lo que queda para decision humana del fundador son los colapsos que ninguna regla mecanica alcanza.**

Separador elegido para identificar declaraciones dentro de `fuente`: **` | ` (pipe) unicamente**, medido y argumentado en `scripts/loop/vuelta130_censo_fuente.py` (`docs/loop/SALIDA_V130_3B_CENSO_FUENTE.txt`). El `;` NO se usa como separador de declaraciones. Corte del catalogo: 2026-08-29, 3.184 nodos vivos con `fuente`, %d grafias distintas en primera posicion con este separador.

**LOS SEIS PELDANOS, ACUMULADOS Y POR SEPARADO:** (1) `vuelta131_grupos_por_titulo.py`, prefijo estricto sobre CADENA ENTERA: **%d grupos**. (2) sumando prefijo sobre TITULO (>=20 caracteres, guarda de RESTO): **%d grupos**. (3) sumando `vuelta132_grupos_por_localizador.py`, localizador con la cola VIEJA (sin Apendice, sin Caps?.): **%d grupos**. (4) sumando la extension a `Apendice` (`vuelta133_cola_localizador_apendice.py`, TAREA 4.a de la 133): **%d grupos**. (5) sumando `vuelta133_prefijo_sobre_recortada.py` (TAREA 4.b de la 133, prefijo ESTRICTO sobre esa forma recortada CON Apendice): **%d grupos**. (6) con la cola extendida a `Caps?.` (`vuelta135_cola_localizador_cap.py`, TAREA 4.a de la 135) EN TODOS los sitios donde la cadena usa la cola, agrupamiento POR IGUALDAD y PREFIJO sobre la recortada: **%d grupos**. La canonica de cada grupo: forma mas larga que sigue siendo libro, o, si ninguna lo es, la forma recortada del miembro mas largo marcada SINTETICA (regla vigente desde la vuelta 131, TAREA 3.b; en este corte: %d canonicas SINTETICAS).

**CON LA CADENA COMPLETA (peldano 6): %d grupos** (%d con 2 o mas miembros / %d en grupo, %d sin agrupar), sobre %d grafias. Meta de `05_SANEO.md` (11 ago 2026): 55 libros canonicos. **Quedan %d colapsos para decision humana, y la meta de 55 queda REBASADA POR %d** (coste declarado, no escondido).

| grafia | canonica propuesta | motivo | bolsa |
|---|---|---|---|
""" % (
        total_grafias,
        n_cadena,
        n_titulo,
        n_localizador_vieja,
        n_apendice,
        n_prefijo_apendice,
        n_cap,
        n_sinteticas,
        total_grupos,
        len(multi),
        en_grupo_n,
        sin_agrupar_n,
        total_grafias,
        colapsos_faltan,
        rebase,
    )

    filas_ordenadas = sorted(filas, key=lambda t: t[0])
    cuerpo = "\n".join(
        "| %s | %s | %s | %s |" % (g, canon, motivo, bolsa) for g, canon, motivo, bolsa in filas_ordenadas
    )
    pie = "\n\nTOTAL filas: %d (%d grafias en grupos mecanicos de 2 o mas, %d sin agrupar), contra %d grafias del censo.\n" % (
        len(filas_ordenadas),
        en_grupo_n,
        sin_agrupar_n,
        total_grafias,
    )

    with open(DESTINO, "w", encoding="utf-8") as fh:
        fh.write(cabecera + cuerpo + pie)

    print("grafias: %d" % total_grafias)
    print("peldano 1 (cadena entera): %d" % n_cadena)
    print("peldano 2 (+ titulo): %d" % n_titulo)
    print("peldano 3 (+ localizador cola VIEJA): %d" % n_localizador_vieja)
    print("peldano 4 (+ Apendice): %d" % n_apendice)
    print("peldano 5 (+ prefijo sobre recortada con Apendice): %d" % n_prefijo_apendice)
    print("peldano 6 (+ Caps?. en cola y en prefijo): %d" % n_cap)
    print("grupos totales (6 peldanos): %d" % total_grupos)
    print("grupos con 2+ miembros: %d" % len(multi))
    print("sin agrupar: %d" % sin_agrupar_n)
    print("en grupo: %d" % en_grupo_n)
    print("canonicas SINTETICAS: %d" % n_sinteticas)
    print("colapsos que faltan para 55: %d" % colapsos_faltan)
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
