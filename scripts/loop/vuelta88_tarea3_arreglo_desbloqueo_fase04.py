# -*- coding: utf-8 -*-
"""vuelta88_tarea3_arreglo_desbloqueo_fase04.py . VUELTA 88, TAREA 3
(adjudicaciones 6.2 y 6.3 del acta de la vuelta 87).

SUCESOR DECLARADO de scripts/loop/vuelta87_tarea5_desbloqueo_fase04.py, que NO
se borra ni se toca: este fichero es la correccion, y el viejo queda como
evidencia de lo que traia. NINGUNO de los tres defectos de aqui abajo cambia
la tabla que la vuelta 87 publico (lo verifico en el reporte: ninguna de las
diez operaciones de la fase 04 depende de una operacion de fase 00_CODIGO), y
los tres hay que arreglarlos antes de que la tabla se use para abrir nada
(acta de la vuelta 87, seccion 3.3).

LOS TRES DEFECTOS ARREGLADOS AQUI:

(3.a) EL RESPALDO POR `nota` NO DISPARABA NUNCA, ni cuando la dependencia no
tenia apartado de cierre en su pagina de fase. La causa medida: `marca_
positiva()` del instrumento viejo busca SIEMPRE una CABECERA markdown (una
linea que empiece por `#`), y el campo `nota` es PROSA CORRIDA sin cabeceras:
la funcion no podia encontrar nada ahi aunque la nota dijera literalmente que
la operacion "queda HECHA". CASO MEDIDO: `OP-E-02` aparece en `04_ENLACES.md`
(lineas 6 y 558, mencion sin seccion propia), no tiene apartado de cierre, cae
al respaldo de `nota`, y el `nota` SI dice "la operacion queda HECHA" y
"CIERRE POR DECLARACION (26 ago 2026, vuelta 76...)" pero la funcion vieja
devolvia `AMBIGUA` igual, porque buscaba una cabecera que la prosa nunca
tiene.

EL ARREGLO: una funcion nueva, `marca_positiva_prosa()`, SIN anclaje a
cabecera, para leer el campo `nota` (que nunca es markdown de pagina): busca
las mismas tres senales que `marca_positiva()` mas dos formas que YA son
idioma establecido en `OPERACIONES.jsonl` (grep propio: aparecen en mas de
quince notas de la fase 02 y 04) y que la version vieja nunca podia leer por
no llevar cabecera: la frase literal `"queda HECHA"` y la frase literal
`"CIERRE POR DECLARACION"`. El respaldo dispara ahora **cuando la pagina de
fase no dio ninguna marca reconocida** (haya o no seccion propia: antes solo
funcionaba de casualidad cuando la nota traia, por azar, una cabecera con
`#`, que nunca es el caso), no solo cuando falta la seccion.

(3.b) `ruta_fase("00_CODIGO")` devolvia `None` porque la pagina se llama
`FASE_0_CODIGO.md`, no `00_CODIGO.md` (medido: `os.path.exists` daba `False`
para la ruta vieja). Toda dependencia de fase `00_CODIGO` (hoy `OP-C-04` y
`OP-C-05`) caia SIEMPRE al respaldo de `nota`, y por el defecto 3.a ese
respaldo tampoco disparaba: las dos salian `AMBIGUA` por partida doble.
EL ARREGLO: un mapa explicito de excepciones fase -> nombre de fichero, con
`00_CODIGO` apuntando a `FASE_0_CODIGO.md`; el resto de fases sigue el patron
`<fase>.md` como antes.

(3.c) EL DOCSTRING VIEJO NOMBRA EL SEGUNDO FALSO NEGATIVO COMO `OP-D-06`
(ronda vieja, lectura de seccion entera: la seccion `OP-D-06 CERRADA` empieza
en la linea 3407 de `02_DESTEJIDOS.md` y la frase del umbral cae dentro de
ella) y el bloque `CORRECCIONES_MANUALES` mas el reporte de la vuelta 87 lo
nombran `OP-D-01` (ronda nueva, ventana de proximidad de 220 caracteres: la
UNICA mencion de `OP-D-01` que alcanza esa misma frase, linea 3580). LOS DOS
SON CIERTOS, cada uno de su ronda (medido en `docs/loop/_auditor_v87_falsos_
negativos.txt`, citado por el acta de la vuelta 87 seccion 3.3 punto 3): no es
una mentira, es un docstring que cuenta la ronda vieja y se salta la ronda
nueva. EL ARREGLO: este docstring nombra los DOS casos, uno al lado del otro,
sin borrar ninguno.

  - RONDA VIEJA (instrumento sin ventana de proximidad, lectura de la seccion
    entera): `OP-D-06` salia NO EJECUTADA porque su seccion de cierre (`02_
    DESTEJIDOS.md`, "OP-D-06 CERRADA", que empieza en la linea 3407) discute,
    mas abajo, un umbral sin relacion ("su umbral acompanante sigue pendiente
    del fundador") que no es sobre si `OP-D-06` esta hecha.
  - RONDA NUEVA (instrumento con ventana de proximidad de 220 caracteres, el
    que corre HOY): `OP-D-01` sale NO EJECUTADA por la misma frase del umbral
    (linea 3580), porque esa linea cae DENTRO de la ventana de la UNICA
    mencion de `OP-D-01` que la alcanza, aunque `OP-D-01` SI esta hecha (fuente
    autoritativa: `02_DESTEJIDOS.md` linea 4470, "EL CIERRE DE LA FASE 02,
    DECLARADO MIDIENDO", tabla de las 9 operaciones: `OP-D-01` SI, con
    "REGISTRO DE OPERACION HECHA", linea 3581). Por eso `CORRECCIONES_
    MANUALES` sigue teniendo la entrada `OP-D-01`, sin tocar: es el defecto
    de HOY, no el de la vuelta 43.

CASO ROJO INVENTADO (3.d), sobre COPIA y sin tocar el arbol real: ver
scripts/loop/vuelta88_tarea3_caso_rojo.py.

USO:
  python scripts/loop/vuelta88_tarea3_arreglo_desbloqueo_fase04.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
PLAN = os.path.join(RAIZ, "docs", "plan")

PRIMERAS_LINEAS_CABECERA = 15

MARCAS_NEGATIVAS = [
    re.compile(r"DECISION PENDIENTE", re.I),
    re.compile(r"PENDIENTE DEL CIERRE", re.I),
    re.compile(r"SIGUE PENDIENTE", re.I),
    re.compile(r"QUEDA PENDIENTE", re.I),
    re.compile(r"ESPERA AL CIERRE", re.I),
    re.compile(r"ENRUTADAS? A LA FASE", re.I),
]

# TAREA 3.b: mapa de excepciones fase -> nombre de fichero. La fase 0 vive en
# FASE_0_CODIGO.md, no en 00_CODIGO.md (unica excepcion medida hoy).
PAGINA_DE_FASE = {
    "00_CODIGO": "FASE_0_CODIGO.md",
}


def cargar_operaciones():
    ops = {}
    for linea in io.open(OPS, encoding="utf-8"):
        linea = linea.strip()
        if linea:
            d = json.loads(linea)
            ops[d["id_op"]] = d
    return ops


def ruta_fase(nombre_fase):
    nombre_fichero = PAGINA_DE_FASE.get(nombre_fase, nombre_fase + ".md")
    ruta = os.path.join(PLAN, nombre_fichero)
    return ruta if os.path.exists(ruta) else None


VENTANA = 220  # caracteres a cada lado de una mencion del id (proximidad, no seccion entera)


def secciones_de(texto, oid):
    """Todas las secciones markdown cuyo encabezado nombra oid (limite de
    palabra), cada una como (linea_encabezado_1_based, texto_encabezado,
    cuerpo_hasta_la_siguiente_cabecera_del_mismo_nivel_o_superior)."""
    lineas = texto.split("\n")
    patron_id = re.compile(r"(?<![\w-])" + re.escape(oid) + r"(?![\w-])")
    cabeceras = [(i, l) for i, l in enumerate(lineas) if l.lstrip().startswith("#")]
    resultado = []
    for idx, (i, l) in enumerate(cabeceras):
        if not patron_id.search(l):
            continue
        nivel = len(l) - len(l.lstrip("#"))
        fin = len(lineas)
        for j, l2 in cabeceras[idx + 1:]:
            nivel2 = len(l2) - len(l2.lstrip("#"))
            if nivel2 <= nivel:
                fin = j
                break
        cuerpo = "\n".join(lineas[i:fin])
        resultado.append((i + 1, l.strip(), cuerpo))
    return resultado


def ventanas_de_proximidad(texto, oid):
    """DEVUELVE SOLO EL TEXTO CERCANO a cada mencion literal del id (limite de
    palabra), +/- VENTANA caracteres, en vez de la SECCION ENTERA que lo
    nombra."""
    patron_id = re.compile(r"(?<![\w-])" + re.escape(oid) + r"(?![\w-])")
    trozos = []
    for m in patron_id.finditer(texto):
        ini = max(0, m.start() - VENTANA)
        fin = min(len(texto), m.end() + VENTANA)
        trozos.append(texto[ini:fin])
    return "\n...\n".join(trozos)


def marca_negativa(texto):
    for pat in MARCAS_NEGATIVAS:
        m = pat.search(texto)
        if m:
            inicio = max(0, m.start() - 50)
            return texto[inicio:m.end() + 50].replace("\n", " ").strip()
    return None


def marca_positiva(oid, texto):
    """Positiva ANCLADA A CABECERA, para texto de PAGINA (markdown)."""
    pat_cabecera_cierre = re.compile(
        r"^#+.*" + re.escape(oid) + r".*\b(CERRADA|SELLADA|CIERRE)\b", re.I | re.M)
    m = pat_cabecera_cierre.search(texto)
    if m:
        return m.group(0).strip()[:140]
    if "REGISTRO DE OPERACION HECHA" in texto:
        idx = texto.index("REGISTRO DE OPERACION HECHA")
        return texto[max(0, idx - 60):idx + 40].replace("\n", " ").strip()
    pat_fusion = re.compile(
        r"^#+.*" + re.escape(oid) + r".*EL REGISTRO DE LA FUSION", re.I | re.M)
    if pat_fusion.search(texto) and "censo del catalogo" in texto.lower() \
            and re.search(r"\bANTES\b", texto) and re.search(r"\bDESPUES\b", texto):
        m2 = pat_fusion.search(texto)
        return m2.group(0).strip()[:140] + " [+ censo ANTES/DESPUES medido en el cuerpo]"
    return None


def marca_positiva_prosa(texto):
    """TAREA 3.a: positiva SIN anclaje a cabecera, para el campo `nota`
    (prosa corrida, nunca markdown de pagina). Ademas de "REGISTRO DE
    OPERACION HECHA" (ya reconocida), suma dos frases que ya son idioma
    establecido en OPERACIONES.jsonl (grep propio sobre el fichero: aparecen
    en mas de quince notas de las fases 02 y 04) y que la version anclada a
    cabecera no podia leer nunca en un campo sin '#': "queda HECHA" y
    "CIERRE POR DECLARACION"."""
    if "REGISTRO DE OPERACION HECHA" in texto:
        idx = texto.index("REGISTRO DE OPERACION HECHA")
        return texto[max(0, idx - 60):idx + 40].replace("\n", " ").strip()
    if "queda HECHA" in texto:
        idx = texto.index("queda HECHA")
        return texto[max(0, idx - 80):idx + 20].replace("\n", " ").strip()
    if "CIERRE POR DECLARACION" in texto:
        idx = texto.index("CIERRE POR DECLARACION")
        return texto[idx:idx + 140].replace("\n", " ").strip()
    return None


# CORRECCIONES DECLARADAS A MANO, CITADAS (no automaticas, no calladas), sin
# tocar respecto de la vuelta 87: el defecto de OP-D-01 es de HOY (ver 3.c en
# el docstring de arriba), no lo arregla el defecto 3.a ni el 3.b.
CORRECCIONES_MANUALES = {
    "OP-D-01": (
        "EJECUTADA",
        "el crudo del instrumento ata OP-D-01 a la frase 'su umbral acompanante "
        "sigue pendiente del fundador [...] y el par 494 sigue yendo a OP-D-01 "
        "como cura acoplada mayor' (02_DESTEJIDOS.md linea 3580), pero esa "
        "'pendiente' es sobre el umbral MIN_BLOQUE y el enrutamiento del par "
        "494, no sobre si OP-D-01 esta hecha. FUENTE AUTORITATIVA: "
        "02_DESTEJIDOS.md linea 4470 ('EL CIERRE DE LA FASE 02, DECLARADO "
        "MIDIENDO'), tabla de las 9 operaciones: OP-D-01 SI, con REGISTRO DE "
        "OPERACION HECHA, linea 3581 (la seccion que empieza justo despues de "
        "la frase que confundio al localizador).",
    ),
}


def estado_real(oid, ops):
    """Devuelve (veredicto, evidencia, fuente) para la dependencia oid.
    veredicto en {"EJECUTADA", "NO EJECUTADA", "AMBIGUA", "ID DESCONOCIDO"}."""
    d = ops.get(oid)
    if d is None:
        return "ID DESCONOCIDO", "no aparece en OPERACIONES.jsonl", "-"

    fase = d.get("fase")
    ruta = ruta_fase(fase) if fase else None
    if ruta:
        texto_completo = io.open(ruta, encoding="utf-8").read()
        cabecera_pagina = "\n".join(texto_completo.split("\n")[:PRIMERAS_LINEAS_CABECERA])
        patron_id = re.compile(r"(?<![\w-])" + re.escape(oid) + r"(?![\w-])")
        cabecera_relevante = cabecera_pagina if patron_id.search(cabecera_pagina) else ""
        secciones = secciones_de(texto_completo, oid)
        cuerpo_secciones = "\n".join(s[2] for s in secciones)
        proximidad = ventanas_de_proximidad(texto_completo, oid)

        neg = marca_negativa(cabecera_relevante) or marca_negativa(proximidad)
        if neg:
            return "NO EJECUTADA", neg, os.path.basename(ruta)

        pos = marca_positiva(oid, cabecera_relevante + "\n" + cuerpo_secciones)
        if pos:
            return "EJECUTADA", pos, os.path.basename(ruta)

    # TAREA 3.a: el respaldo por `nota` dispara CUANDO NO HAY MARCA
    # RECONOCIDA en la pagina de fase (arriba), sea porque no hay pagina, no
    # hay seccion propia, o la seccion no trae ninguna marca. Y ahora SI
    # puede leer una nota de prosa corrida (marca_positiva_prosa, sin
    # anclaje a cabecera).
    nota = d.get("nota") or ""
    neg = marca_negativa(nota)
    if neg:
        return "NO EJECUTADA", neg, "OPERACIONES.jsonl:nota"
    pos = marca_positiva_prosa(nota)
    if pos:
        return "EJECUTADA", pos, "OPERACIONES.jsonl:nota"

    return "AMBIGUA", "ninguna marca positiva ni negativa reconocida", "(ninguna)"


def estado_real_corregido(oid, ops):
    """estado_real() con las CORRECCIONES_MANUALES aplicadas encima, citadas
    y con la fuente automatica original conservada."""
    v, ev, fuente = estado_real(oid, ops)
    if oid in CORRECCIONES_MANUALES:
        v2, cita = CORRECCIONES_MANUALES[oid]
        return v2, "CORREGIDO A MANO: %s (crudo del instrumento: %s | %s)" % (cita, v, ev), "correccion manual, ver docstring"
    return v, ev, fuente


def main():
    ops = cargar_operaciones()
    fase04 = sorted([d for d in ops.values() if d["fase"] == "04_ENLACES"],
                     key=lambda d: d.get("orden", 999))

    print("=" * 90)
    print("TAREA 3 (vuelta 88): EL INSTRUMENTO DE LA TAREA 5 (vuelta 87), ARREGLADO")
    print("Las diez operaciones de docs/plan/04_ENLACES.md, orden de la ficha.")
    print("=" * 90)
    print()
    print("%-20s %-6s %-45s %-20s" % ("id_op", "orden", "depende_de", "DESBLOQUEADA"))
    print("-" * 100)

    filas = []
    for d in fase04:
        oid = d["id_op"]
        depende = d.get("depende_de") or []
        estados_dep = [(dep, estado_real_corregido(dep, ops)) for dep in depende]
        if not depende:
            desbloqueada = "SI (sin dependencias)"
        elif all(v == "EJECUTADA" for _, (v, _, _) in estados_dep):
            desbloqueada = "SI"
        elif any(v in ("NO EJECUTADA",) for _, (v, _, _) in estados_dep):
            desbloqueada = "NO"
        else:
            desbloqueada = "NO SE PUEDE DECIR (dependencia AMBIGUA)"
        filas.append((d, estados_dep, desbloqueada))
        print("%-20s %-6s %-45s %-20s" % (oid, d.get("orden"),
                                          ", ".join(depende) or "(ninguna)", desbloqueada))

    print()
    print("=" * 90)
    print("EL DETALLE, DEPENDENCIA POR DEPENDENCIA, CON SU EVIDENCIA CITADA")
    print("=" * 90)
    for d, estados_dep, desbloqueada in filas:
        oid = d["id_op"]
        print()
        print("%s (orden %s) -> DESBLOQUEADA: %s" % (oid, d.get("orden"), desbloqueada))
        if not estados_dep:
            print("  (esta operacion no declara depende_de)")
        for dep, (v, ev, fuente) in estados_dep:
            print("  depende de %-20s | %-14s | fuente %-28s | %s" % (dep, v, fuente, ev))

    print()
    print("=" * 90)
    print("RESUMEN: OPERACIONES DE FASE 04 DESBLOQUEADAS HOY (ademas de OP-E-01, ya")
    print("cerrada)")
    print("=" * 90)
    desbloqueadas = [d["id_op"] for d, _, desb in filas if desb == "SI" and d["id_op"] != "OP-E-01"]
    print("  %s" % (", ".join(desbloqueadas) if desbloqueadas else "NINGUNA"))
    print()
    print("NO SE ABRE NINGUNA OPERACION ESTA VUELTA: esta tabla se publica y se lee su")
    print("texto para contestar si alcanza para ejecutarla sin decidir nada.")
    print()
    print("=" * 90)
    print("CASO OBLIGATORIO 3.a: OP-E-02 leida directamente, citando su nota")
    print("=" * 90)
    v, ev, fuente = estado_real_corregido("OP-E-02", ops)
    print("OP-E-02 -> %s | fuente %s | %s" % (v, fuente, ev))
    print()
    print("=" * 90)
    print("CASO OBLIGATORIO 3.b: OP-C-04 y OP-C-05 leidas directamente")
    print("=" * 90)
    for oid in ("OP-C-04", "OP-C-05"):
        v, ev, fuente = estado_real_corregido(oid, ops)
        print("%s -> %s | fuente %s | %s" % (oid, v, fuente, ev))


if __name__ == "__main__":
    main()
