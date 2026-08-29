# -*- coding: utf-8 -*-
"""vuelta133_tabla_mapeo_propuesto.py . TAREA 4.d de la vuelta 133: rehace
docs/plan/OP_S_11_MAPEO_PROPUESTO.md con 4.a (cola de localizador con
`Apendice`) y 4.b (prefijo sobre recortada, APLICADO, adjudicado por el
auditor) puestas.

MISMAS CUATRO COLUMNAS de la vuelta 132 (grafia, canonica propuesta,
motivo, bolsa). El vocabulario de la columna de motivo GANA DOS VALORES
NUEVOS: la regla que agrupa puede ser ahora `cadena entera`, `titulo`,
`localizador` o `prefijo sobre recortada` (prioridad en ese orden: la
primera regla, en ese orden, que conecta esta fila con OTRO miembro de su
grupo final); de donde sale la canonica sigue siendo `la propia grafia`,
`recorte de localizador` o `SINTETICA`.

LA CONSECUENCIA QUE SE MIRA CON LOS OJOS ABIERTOS (TAREA 4.c): con 4.a y
4.b puestas, las canonicas SINTETICAS del censo pasan de UNA a CERO. LA
REGLA SINTETICA (NOVENA entrada de la ficha `fuente`, vuelta 131) NO SE
BORRA, NO SE MARCA MUERTA Y NO SE SACA DEL CODIGO: queda VIGENTE Y SIN
CASO EN ESTE CORTE (se sigue evaluando en el codigo de abajo; solo no
encuentra ningun grupo sin libro que coronar).

No aplica la tabla a ningun nodo. `OP-S-11` sigue LISTA.

CORRIGE LA FRASE DE ATRIBUCION DE LA CABECERA VIEJA: las reglas mecanicas
las adjudica el auditor en su acta (asi lo hizo con 3.1 y con esta misma
extension, acta 132); lo que queda para decision humana del fundador son
los colapsos que ninguna regla mecanica alcanza.

Salida: docs/plan/OP_S_11_MAPEO_PROPUESTO.md (unico fichero viejo que esta
vuelta puede cambiar de contenido, REGIMEN A CON LINEA VIEJA)

Uso:
  python scripts/loop/vuelta133_tabla_mapeo_propuesto.py
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
from vuelta133_cola_localizador_apendice import recortar_localizador_con_apendice as recortar  # noqa: E402
from vuelta132_bolsa2_particion import RESIDUALES, PROPUESTA_FORASTERA, sondar, titulo_de  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DESTINO = os.path.join(RAIZ, "docs", "plan", "OP_S_11_MAPEO_PROPUESTO.md")
META_LIBROS_CANONICOS = 55
GUARDA_LONGITUD = 20


def prefijo_recortada_une(a, b):
    """La regla NUEVA de la TAREA 4.b: prefijo estricto sobre la forma
    recortada (con la cola de 4.a), guarda de longitud >=20 y guarda de
    RESTO por simetria con la regla de titulo."""
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
    colapsos_faltan = total_grupos - META_LIBROS_CANONICOS
    n_sinteticas = sum(1 for v in origen_de.values() if v == "SINTETICA")

    n_cadena = contar(grafias, [prefijo_cadena_entera_une])
    n_titulo = contar(grafias, [prefijo_cadena_entera_une, prefijo_titulo_une])

    def regla_localizador_vieja_bucket(a, b):
        return a != b and recortar(a) == recortar(b)
    n_localizador = contar(grafias, [prefijo_cadena_entera_une, prefijo_titulo_une, regla_localizador_vieja_bucket])
    # n_localizador de esta vuelta YA incluye Apendice (4.a): 105, no 106.
    n_apendice = n_localizador
    n_prefijo = total_grupos

    cabecera = """# OP-S-11: tabla de mapeo PROPUESTA del campo `fuente`

**PROPUESTA MEDIDA, escrita en la vuelta 130 (TAREA 3.b), REHECHA en la vuelta 131 (TAREA 3.c), REHECHA en la vuelta 132 (TAREA 3.e) y REHECHA OTRA VEZ en la vuelta 133 (TAREA 4.d) con la cola de localizador extendida a `Apendice` y el prefijo sobre la forma recortada APLICADO. NO se ha aplicado a ningun nodo: `OP-S-11` sigue LISTA, sin tocar, y esta tabla no cambia su estado. LAS REGLAS MECANICAS LAS ADJUDICA EL AUDITOR EN SU ACTA (asi lo hizo con 3.1 y con esta extension, acta 132); lo que queda para decision humana del fundador son los colapsos que ninguna regla mecanica alcanza.**

Separador elegido para identificar declaraciones dentro de `fuente`: **` | ` (pipe) unicamente**, medido y argumentado en `scripts/loop/vuelta130_censo_fuente.py` (`docs/loop/SALIDA_V130_3B_CENSO_FUENTE.txt`). El `;` NO se usa como separador de declaraciones. Corte del catalogo: 2026-08-29, 3.184 nodos vivos con `fuente`, %d grafias distintas en primera posicion con este separador.

**LAS REGLAS MECANICAS, ACUMULADAS Y POR SEPARADO:** (1) `vuelta131_grupos_por_titulo.py`, prefijo estricto sobre CADENA ENTERA: **%d grupos**. (2) sumando prefijo sobre TITULO (>=20 caracteres, guarda de RESTO): **%d grupos**. (3) sumando `vuelta132_grupos_por_localizador.py` MAS la extension a `Apendice` de esta vuelta (`vuelta133_cola_localizador_apendice.py`, TAREA 4.a), igualdad EXACTA de la forma recortada: **%d grupos**. (4) sumando `vuelta133_prefijo_sobre_recortada.py` (TAREA 4.b, prefijo ESTRICTO sobre esa misma forma recortada, guarda de longitud y guarda de RESTO): **%d grupos**. La canonica de cada grupo: forma mas larga que sigue siendo libro, o, si ninguna lo es, la forma recortada del miembro mas largo marcada SINTETICA (regla vigente desde la vuelta 131, TAREA 3.b; VIGENTE Y SIN CASO en este corte: %d canonicas SINTETICAS).

**CON LAS CUATRO REGLAS MECANICAS: %d grupos** (%d con 2 o mas miembros / %d en grupo, %d sin agrupar), sobre %d grafias. Meta de `05_SANEO.md` (11 ago 2026): 55 libros canonicos. **Quedan %d colapsos para decision humana.**

| grafia | canonica propuesta | motivo | bolsa |
|---|---|---|---|
""" % (
        total_grafias,
        n_cadena,
        n_titulo,
        n_apendice,
        n_prefijo,
        n_sinteticas,
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
    print("grupos cadena entera sola: %d" % n_cadena)
    print("grupos cadena entera + titulo: %d" % n_titulo)
    print("grupos + localizador (con Apendice): %d" % n_apendice)
    print("grupos + prefijo sobre recortada: %d" % n_prefijo)
    print("grupos totales (4 reglas): %d" % total_grupos)
    print("grupos con 2+ miembros: %d" % len(multi))
    print("sin agrupar: %d" % sin_agrupar_n)
    print("en grupo: %d" % en_grupo_n)
    print("canonicas SINTETICAS: %d" % n_sinteticas)
    print("colapsos que faltan para 55: %d" % colapsos_faltan)
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
