# -*- coding: utf-8 -*-
"""vuelta87_tarea5_desbloqueo_fase04.py . VUELTA 87, TAREA 5 (adjudicaciones
5.9 y 5.10 del acta 86). Publica, para las diez operaciones de
docs/plan/04_ENLACES.md, una tabla con: id, orden, sus dependencias, el
ESTADO REAL de cada dependencia, y si la operacion queda desbloqueada.

POR QUE NACE (acta 86, seccion 4 y punto (D) del encargo). El campo `estado`
de docs/plan/OPERACIONES.jsonl NO MIDE NADA desde el 15 ago 2026
(00_INDICE.md linea 111, decision del fundador): el valor HECHA no se
estrena, y el campo se queda en LISTA aunque la operacion ya se haya
ejecutado. El auditor casi publico que TODA la fase 04 seguia bloqueada
leyendo ese campo. Este instrumento NUNCA lee `estado`: lee la PROSA de la
pagina de fase de cada dependencia (docs/plan/<fase>.md, la fase se toma del
propio campo `fase` de la dependencia en OPERACIONES.jsonl) y, como respaldo
si la dependencia no tiene seccion propia en su pagina, el campo `nota`.

EL CRITERIO DE LECTURA, ESCRITO AQUI PORQUE BUSCAR UNA PALABRA SUELTA NO ES
UNA MEDICION ACEPTABLE EN ESTA CAMPANA (acta 86, adjudicacion 5.9):

  1. MARCAS NEGATIVAS ("DECISION PENDIENTE", "PENDIENTE DEL CIERRE", "SIGUE
     PENDIENTE", "QUEDA PENDIENTE", "ESPERA AL CIERRE", "ENRUTADA(S) A LA
     FASE") se buscan SOLO POR PROXIMIDAD LITERAL al id: una ventana de 220
     caracteres a cada lado de CADA mencion real del id en la pagina de fase
     (nunca la seccion entera, que puede tener miles de caracteres y hablar
     de otra cosa a mitad de camino), mas la cabecera de apertura de la
     pagina SI Y SOLO SI esa cabecera nombra al id (si no, es el resumen de
     otra operacion que la misma pagina abre). Si aparece cualquiera, la
     dependencia NO esta ejecutada, aunque tambien haya una marca positiva.
  2. MARCAS POSITIVAS (si ninguna negativa aparecio): dentro de las SECCIONES
     markdown cuyo encabezado nombra al id (el cuerpo completo de esas
     secciones, no solo la ventana de proximidad, porque el censo ANTES/
     DESPUES de una fusion puede vivir varios parrafos despues del titulo),
     una cabecera que junte el id con CERRADA, SELLADA o CIERRE; la frase
     literal "REGISTRO DE OPERACION HECHA" (acunada en la vuelta 30, ver
     scripts/loop/vuelta46_cierre_fase02.py); o una cabecera "EL REGISTRO DE
     LA FUSION" para ese id CON un censo medido antes/despues en el cuerpo
     ("censo del catalogo" + "ANTES" + "DESPUES", la firma de una fusion que
     de verdad corrio, no solo se planeo).
  3. Si no aparece ninguna marca de ninguna especie, ni en la pagina de fase
     ni (a falta de seccion) en el campo `nota`: NO SE PUEDE LEER, y la
     dependencia se publica como AMBIGUA, no se le adivina un lado.

LIMITE DECLARADO Y NO CALLADO: esto es un LOCALIZADOR DE FRASES POR
PROXIMIDAD, no un lector. LA PRIMERA CORRIDA DE ESTE INSTRUMENTO (sin la
ventana de proximidad, buscando en la seccion entera) dio DOS FALSOS
NEGATIVOS, y quedan citados para que nadie los repita: (a) `OP-M-03-I`,
`OP-M-03-II` y `OP-M-01-FUSION` salian NO EJECUTADA porque la cabecera de
apertura de `03_FUSIONES.md` se leia COMPLETA para cualquier id de esa
pagina, y esa cabecera declara a `OP-U-02` (otra operacion) "pendiente del
cierre del cribado"; (b) `OP-D-06` salia NO EJECUTADA porque su seccion de
cierre de la vuelta 43 tambien discute, mas abajo, un umbral sin relacion
("su umbral acompanante sigue pendiente del fundador") que no es sobre si
`OP-D-06` esta hecha. Los dos se citan en el reporte de esta vuelta como la
evidencia de por que la ventana de proximidad reemplazo la seccion entera
para las marcas negativas. Si una operacion futura cierra con palabras
nuevas que no esten en esta lista, el instrumento la va a publicar como
AMBIGUA (fallar ruidoso, no silencioso) y hay que ensanchar la lista a mano,
con el caso citado.

USO:
  python scripts/loop/vuelta87_tarea5_desbloqueo_fase04.py
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


def cargar_operaciones():
    ops = {}
    for linea in io.open(OPS, encoding="utf-8"):
        linea = linea.strip()
        if linea:
            d = json.loads(linea)
            ops[d["id_op"]] = d
    return ops


def ruta_fase(nombre_fase):
    ruta = os.path.join(PLAN, nombre_fase + ".md")
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
    nombra. Una seccion puede tener miles de caracteres y hablar de varias
    cosas a la vez (un parametro pendiente, un umbral, otra operacion citada
    de pasada); tomar la seccion completa como evidencia hace que una frase
    negativa SOBRE OTRA COSA se lea como si fuera sobre el id. La proximidad
    ata la marca a la mencion real del id, no al parrafo que la rodea."""
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


# CORRECCIONES DECLARADAS A MANO, CITADAS (no automaticas, no calladas). El
# localizador por proximidad puede atar una frase negativa a una mencion del
# id que en realidad pertenece a OTRA clausula de la misma oracion. Cada
# entrada aqui es un caso REAL que este instrumento produjo mal en esta
# vuelta, con la cita de por que y con que se corrige.
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
        # La cabecera de la pagina (resumen de apertura) SOLO cuenta como
        # evidencia si de verdad nombra a ESTE id: si no, es ruido de otra
        # operacion que la pagina tambien resume ahi mismo.
        cabecera_relevante = cabecera_pagina if patron_id.search(cabecera_pagina) else ""
        secciones = secciones_de(texto_completo, oid)
        # Las CABECERAS de seccion completas (para las marcas tipo "## OP-X
        # CERRADA" o "EL REGISTRO DE LA FUSION", y para el censo ANTES/DESPUES
        # que puede vivir a mas de VENTANA caracteres del titulo).
        cuerpo_secciones = "\n".join(s[2] for s in secciones)
        # Y la proximidad literal, para las marcas NEGATIVAS: una frase
        # pendiente atada a la mencion real del id, no a todo el parrafo.
        proximidad = ventanas_de_proximidad(texto_completo, oid)

        neg = marca_negativa(cabecera_relevante) or marca_negativa(proximidad)
        if neg:
            return "NO EJECUTADA", neg, os.path.basename(ruta)

        pos = marca_positiva(oid, cabecera_relevante + "\n" + cuerpo_secciones)
        if pos:
            return "EJECUTADA", pos, os.path.basename(ruta)

    nota = d.get("nota") or ""
    neg = marca_negativa(nota)
    if neg:
        return "NO EJECUTADA", neg, "OPERACIONES.jsonl:nota"
    pos = marca_positiva(oid, nota)
    if pos:
        return "EJECUTADA", pos, "OPERACIONES.jsonl:nota"

    return "AMBIGUA", "ninguna marca positiva ni negativa reconocida", "(ninguna)"


def estado_real_corregido(oid, ops):
    """estado_real() con las CORRECCIONES_MANUALES aplicadas encima, citadas
    y con la fuente automatica original conservada para que la comparacion
    se pueda auditar (nunca se tapa lo que se corrige)."""
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
    print("TAREA 5: LO QUE VIENE DESPUES DE OP-E-01, TALLADO (vuelta 87)")
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
    print("RESUMEN: OPERACIONES DE FASE 04 DESBLOQUEADAS HOY (ademas de OP-E-01, que")
    print("esta misma vuelta cierra)")
    print("=" * 90)
    desbloqueadas = [d["id_op"] for d, _, desb in filas if desb == "SI" and d["id_op"] != "OP-E-01"]
    print("  %s" % (", ".join(desbloqueadas) if desbloqueadas else "NINGUNA"))
    print()
    print("NO SE ABRE NINGUNA OPERACION ESTA VUELTA: esta tabla se publica y se lee su")
    print("texto para contestar si alcanza para ejecutarla sin decidir nada; abrirla es")
    print("trabajo de la vuelta siguiente.")


if __name__ == "__main__":
    main()
