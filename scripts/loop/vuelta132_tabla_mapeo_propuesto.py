# -*- coding: utf-8 -*-
"""vuelta132_tabla_mapeo_propuesto.py . TAREA 3.e de la vuelta 132: rehace
docs/plan/OP_S_11_MAPEO_PROPUESTO.md con 3.a (localizador AGRUPA) y 3.b
(canonica sintetica) puestas, y con 3.c (BOLSA 2) en su columna.

MISMAS TRES COLUMNAS de la vuelta 131 mas una CUARTA (BOLSA), y reparo la
caida 4.5 del acta 131: la columna de motivo dice DOS cosas separadas:
  (1) QUE REGLA AGRUPO LA FILA: cadena entera / titulo / localizador / SIN
      AGRUPAR. Prioridad cadena entera > titulo > localizador (la primera
      regla, en ese orden, que conecta esta fila con OTRO miembro de su
      grupo final).
  (2) DE DONDE SALE LA CANONICA DEL GRUPO: "la propia grafia" (el miembro
      mas largo ya era un libro, la regla del localizador no fue decisiva),
      "recorte de localizador" (el miembro mas largo NO era un libro pero
      SI habia otro miembro que si lo era, y ese gano por la regla de 3.b),
      o "SINTETICA" (ningun miembro es libro, la canonica se fabrica
      recortando el mas largo, 3.b).
Una fila agrupada por cadena entera cuya canonica se fijo por localizador
dice las DOS cosas, no solo la segunda (que es lo que la tabla de la 131
hacia y lo que cobro la caida 4.5).

La CUARTA columna, BOLSA: vacia para las agrupadas: `2a <fichero:linea>` o
`2b FORASTERO` para las cuatro de 3.c.

No aplica la tabla a ningun nodo. `OP-S-11` sigue LISTA.

Salida: docs/plan/OP_S_11_MAPEO_PROPUESTO.md (unico fichero viejo que esta
vuelta puede cambiar de contenido)

Uso:
  python scripts/loop/vuelta132_tabla_mapeo_propuesto.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta131_grupos_por_titulo import (  # noqa: E402
    cargar_censo,
    prefijo_cadena_entera_une,
    prefijo_titulo_une,
    UnionFind,
)
from vuelta132_grupos_por_localizador import recortar_localizador  # noqa: E402
from vuelta132_bolsa2_particion import RESIDUALES, PROPUESTA_FORASTERA, sondar, titulo_de  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DESTINO = os.path.join(RAIZ, "docs", "plan", "OP_S_11_MAPEO_PROPUESTO.md")
META_LIBROS_CANONICOS = 55


def calcular_bolsa2():
    """Reproduce 3.c: para cada una de las cuatro grafias residuales, su
    columna de bolsa (2a con fichero:linea, o 2b FORASTERO)."""
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


def calcular():
    censo = cargar_censo()
    grafias = sorted(censo.keys())
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
        buck.setdefault(recortar_localizador(g), []).append(g)
    for _, miembros in buck.items():
        base = miembros[0]
        for m in miembros[1:]:
            uf.une(base, m)

    grupos = {}
    for g in grafias:
        grupos.setdefault(uf.find(g), []).append(g)

    canonica_de = {}
    origen_de = {}
    for r, miembros in grupos.items():
        if len(miembros) == 1:
            canonica_de[r] = miembros[0]
            continue
        libros = [m for m in miembros if recortar_localizador(m) == m]
        vieja = max(miembros, key=len)
        if not libros:
            canonica_de[r] = recortar_localizador(vieja)
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
            if conecta_cadena:
                regla = "cadena entera"
            elif conecta_titulo:
                regla = "titulo"
            else:
                regla = "localizador"
            motivo = "MECANICO: agrupa por %s, canonica %s" % (regla, origen_de[r])
        bolsa = bolsa2.get(g, "")
        filas.append((g, canonica, motivo, bolsa))

    return censo, grafias, grupos, filas


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    censo, grafias, grupos, filas = calcular()

    total_grafias = len(grafias)
    total_grupos = len(grupos)
    multi = {r: m for r, m in grupos.items() if len(m) > 1}
    sin_agrupar_n = sum(1 for r, m in grupos.items() if len(m) == 1)
    en_grupo_n = total_grafias - sin_agrupar_n
    colapsos_faltan = total_grupos - META_LIBROS_CANONICOS

    # cifras de cada regla por separado y acumulada (para la cabecera)
    uf1 = UnionFind(grafias)
    for a in grafias:
        for b in grafias:
            if prefijo_cadena_entera_une(a, b):
                uf1.une(a, b)
    n_cadena = len({uf1.find(g) for g in grafias})
    uf2 = UnionFind(grafias)
    for a in grafias:
        for b in grafias:
            if prefijo_cadena_entera_une(a, b):
                uf2.une(a, b)
    for a in grafias:
        for b in grafias:
            if prefijo_titulo_une(a, b):
                uf2.une(a, b)
    n_titulo = len({uf2.find(g) for g in grafias})

    cabecera = """# OP-S-11: tabla de mapeo PROPUESTA del campo `fuente`

**PROPUESTA MEDIDA, escrita en la vuelta 130 (TAREA 3.b), REHECHA en la vuelta 131 (TAREA 3.c) y REHECHA OTRA VEZ en la vuelta 132 (TAREA 3.e) con la regla del localizador agrupando y la canonica sintetica. NO se ha aplicado a ningun nodo: `OP-S-11` sigue LISTA, sin tocar, y esta tabla no cambia su estado. La adjudica el fundador.**

Separador elegido para identificar declaraciones dentro de `fuente`: **` | ` (pipe) unicamente**, medido y argumentado en `scripts/loop/vuelta130_censo_fuente.py` (`docs/loop/SALIDA_V130_3B_CENSO_FUENTE.txt`). El `;` NO se usa como separador de declaraciones. Corte del catalogo: 2026-08-29, 3.184 nodos vivos con `fuente`, %d grafias distintas en primera posicion con este separador.

**LAS REGLAS MECANICAS, ACUMULADAS:** (1) `vuelta131_grupos_por_titulo.py`, prefijo estricto sobre CADENA ENTERA: %d grupos. (2) sumando prefijo sobre TITULO (>=20 caracteres, guarda de RESTO): %d grupos. (3) sumando `vuelta132_grupos_por_localizador.py`, igualdad EXACTA de la forma recortada de localizador (AGRUPA, ramal xiv): %d grupos. La canonica de cada grupo la fija `vuelta132_canonica_sintetica.py` (SOLO CORONA, ramal xiv): forma mas larga que sigue siendo libro, o, si ninguna lo es, la forma recortada del miembro mas largo marcada SINTETICA.

**CON LAS TRES REGLAS MECANICAS: %d grupos** (%d con 2 o mas miembros / %d en grupo, %d sin agrupar), sobre %d grafias. Meta de `05_SANEO.md` (11 ago 2026): 55 libros canonicos. **Quedan %d colapsos para decision humana.**

| grafia | canonica propuesta | motivo | bolsa |
|---|---|---|---|
""" % (
        total_grafias,
        n_cadena,
        n_titulo,
        total_grupos,
        total_grupos,
        len(multi),
        en_grupo_n,
        sin_agrupar_n,
        total_grafias,
        colapsos_faltan,
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
    print("grupos con cadena entera sola: %d" % n_cadena)
    print("grupos con cadena entera + titulo: %d" % n_titulo)
    print("grupos totales (3 reglas): %d" % total_grupos)
    print("grupos con 2+ miembros: %d" % len(multi))
    print("sin agrupar: %d" % sin_agrupar_n)
    print("en grupo: %d" % en_grupo_n)
    print("colapsos que faltan para 55: %d" % colapsos_faltan)
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
