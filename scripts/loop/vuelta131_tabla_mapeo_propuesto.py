# -*- coding: utf-8 -*-
"""vuelta131_tabla_mapeo_propuesto.py . TAREA 3.c de la vuelta 131:
rehace docs/plan/OP_S_11_MAPEO_PROPUESTO.md con las DOS reglas mecanicas
nuevas de esta vuelta (titulo, `vuelta131_grupos_por_titulo.py`, y
localizador, `vuelta131_canonica_sin_localizador.py`) puestas encima de
la regla vieja de prefijo sobre cadena entera (`vuelta130_...py`).

MISMAS TRES COLUMNAS que la tabla de la vuelta 130 (grafia, canonica
propuesta, motivo). El motivo dice CUAL de las tres reglas mecanicas
agrupo cada fila:
  - "MECANICO: localizador (revoca canonica=mas larga)": el GRUPO entero
    es uno de los CINCO cuya canonica cambia con la regla de la TAREA
    3.b (sin ella, la tabla propondria un capitulo/seccion/anexo o una
    forma con puntuacion colgando como nombre de libro). Se marca asi
    TODA fila del grupo, porque esa es la razon por la que la canonica
    propuesta en la tabla es la correcta y no la mas larga a ciegas.
  - "MECANICO: prefijo sobre cadena entera": la fila conecta con al
    menos otro miembro de su grupo por la regla vieja (una grafia es
    prefijo estricto de la otra en la CADENA ENTERA).
  - "MECANICO: prefijo sobre titulo": la fila SOLO conecta con su grupo
    por la regla nueva de la TAREA 3.a (prefijo sobre el TITULO, con
    guarda de RESTO), no por cadena entera.
  - "SIN AGRUPAR (pide decision)": grupo de 1 sola grafia.

No aplica la tabla a ningun nodo. `OP-S-11` sigue LISTA. Esta vuelta NO
decide las 53 decisiones humanas que quedan (SIN AGRUPAR y grupos
mecanicos): esas las adjudica el auditor.

Salida: docs/plan/OP_S_11_MAPEO_PROPUESTO.md (unico fichero viejo que
esta vuelta puede cambiar de contenido)

Uso:
  python scripts/loop/vuelta131_tabla_mapeo_propuesto.py
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
from vuelta131_canonica_sin_localizador import elegir_canonica  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DESTINO = os.path.join(RAIZ, "docs", "plan", "OP_S_11_MAPEO_PROPUESTO.md")
META_LIBROS_CANONICOS = 55


def calcular():
    censo = cargar_censo()
    grafias = sorted(censo.keys())
    uf = UnionFind(grafias)
    for a in grafias:
        for b in grafias:
            if prefijo_cadena_entera_une(a, b):
                uf.une(a, b)
            if prefijo_titulo_une(a, b):
                uf.une(a, b)
    grupos = {}
    for g in grafias:
        grupos.setdefault(uf.find(g), []).append(g)

    grupos_localizador_cambia = set()
    canonica_de = {}
    for r, miembros in grupos.items():
        if len(miembros) == 1:
            canonica_de[r] = miembros[0]
            continue
        vieja = max(miembros, key=len)
        nueva = elegir_canonica(miembros)
        canonica_de[r] = nueva
        if nueva != vieja:
            grupos_localizador_cambia.add(r)

    filas = []
    for g in grafias:
        r = uf.find(g)
        miembros = grupos[r]
        canonica = canonica_de[r]
        if len(miembros) == 1:
            motivo = "SIN AGRUPAR (pide decision)"
        elif r in grupos_localizador_cambia:
            motivo = "MECANICO: localizador (revoca canonica=mas larga)"
        else:
            conecta_cadena = any(
                m != g and prefijo_cadena_entera_une(g, m) for m in miembros
            )
            if conecta_cadena:
                motivo = "MECANICO: prefijo sobre cadena entera"
            else:
                motivo = "MECANICO: prefijo sobre titulo"
        filas.append((g, canonica, motivo))

    return censo, grafias, grupos, filas, grupos_localizador_cambia


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    censo, grafias, grupos, filas, cambia = calcular()

    total_grafias = len(grafias)
    total_grupos = len(grupos)
    multi = {r: m for r, m in grupos.items() if len(m) > 1}
    sin_agrupar_n = sum(1 for r, m in grupos.items() if len(m) == 1)
    en_grupo_n = total_grafias - sin_agrupar_n
    colapsos_faltan = total_grupos - META_LIBROS_CANONICOS

    cabecera = """# OP-S-11: tabla de mapeo PROPUESTA del campo `fuente`

**PROPUESTA MEDIDA, escrita en la vuelta 130 (TAREA 3.b) y REHECHA en la vuelta 131 (TAREA 3.c) con dos reglas mecanicas nuevas. NO se ha aplicado a ningun nodo: `OP-S-11` sigue LISTA, sin tocar, y esta tabla no cambia su estado. La adjudica el auditor.**

Separador elegido para identificar declaraciones dentro de `fuente`: **` | ` (pipe) unicamente**, medido y argumentado en `scripts/loop/vuelta130_censo_fuente.py` (`docs/loop/SALIDA_V130_3B_CENSO_FUENTE.txt`). El `;` NO se usa como separador de declaraciones: en los 264 nodos vivos que lo traen, junta coautores del mismo libro, listas de capitulos del mismo libro, o (en un punado de casos del dominio `risk_management`) dos citas academicas pegadas sin ambiguedad de autoria; partir por `;` fabricaria grafias que son apellidos sueltos o fragmentos de titulo, no declaraciones nuevas. Corte del catalogo: 2026-08-29, 3.184 nodos vivos con `fuente`, %d grafias distintas en primera posicion con este separador.

**LAS DOS REGLAS NUEVAS DE ESTA VUELTA (revocan la vieja "prefijo sobre cadena entera" que perdia a Hugos y elegia localizadores como canonica):** (1) `scripts/loop/vuelta131_grupos_por_titulo.py`, prefijo estricto sobre el TITULO (segmento antes del primer " - "), titulo corto >= 20 caracteres, con guarda de RESTO (no funde autores distintos); (2) `scripts/loop/vuelta131_canonica_sin_localizador.py`, la canonica de un grupo es la forma mas larga que sigue siendo un libro tras recortar cola de localizador (capitulo/capitulos/seccion/Anexo) y puntuacion final, no la mas larga a ciegas.

**CON LAS TRES REGLAS MECANICAS (cadena entera + titulo + localizador): %d grupos** (%d con 2 o mas miembros / %d en grupo, %d sin agrupar), sobre %d grafias. Meta de `05_SANEO.md` (11 ago 2026): 55 libros canonicos. **Quedan %d colapsos para decision humana.**

| grafia | canonica propuesta | motivo |
|---|---|---|
""" % (
        total_grafias,
        total_grupos,
        len(multi),
        en_grupo_n,
        sin_agrupar_n,
        total_grafias,
        colapsos_faltan,
    )

    filas_ordenadas = sorted(filas, key=lambda t: t[0])
    cuerpo = "\n".join(
        "| %s | %s | %s |" % (g, canon, motivo) for g, canon, motivo in filas_ordenadas
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
    print("grupos totales (3 reglas): %d" % total_grupos)
    print("grupos con 2+ miembros: %d" % len(multi))
    print("sin agrupar: %d" % sin_agrupar_n)
    print("en grupo: %d" % en_grupo_n)
    print("colapsos que faltan para 55: %d" % colapsos_faltan)
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
