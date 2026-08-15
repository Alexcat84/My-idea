# -*- coding: utf-8 -*-
"""vuelta33_plan_opd02.py

CONSTRUYE el plan sellado de la FUSION de OP-D-02: `voz_del_cliente_voc` absorbe a
`enfoque_mercado_voc`. NO ejecuta nada: escribe docs/loop/PLAN_V33_OPD02_FUSION.json.

POR QUE UN CONSTRUCTOR Y NO UN JSON TECLEADO. EJECUTOR.md regla 1, cuarto renglon:
lo que existe en un instrumento no se transcribe a mano. Los textos originales, los
prefijos, las fuentes y los conteos NO se teclean aqui: SE LEEN DEL GRAFO. Lo unico
mio son los textos finales unidos y los motivos de perdida, y los dos pasan por
guardas escritas para caer:

  1. cada paso final tiene que EMPEZAR por el prefijo de su PRIMER origen
  2. cobertura exacta: los 5 pasos del superviviente mas los 5 del absorbido,
     cada uno en exactamente un destino, sin huecos ni repetidos (igual en
     condiciones, 3 mas 2)
  3. las TRES piezas del campo `preservar` de la operacion tienen que aparecer
     LITERALMENTE dentro de los pasos finales, y el script aborta si alguna falta
  4. la fuente de los dos nodos tiene que ser la que el plan espera

LA NOMENCLATURA DE ORIGENES, porque aqui hay DOS nodos y no uno: `S1` a `S5` son
los pasos del superviviente y `A1` a `A5` los del absorbido. Igual en condiciones,
`SC1` a `SC3` y `AC1` a `AC2`.

Uso: python scripts/loop/vuelta33_plan_opd02.py [--escribir]
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
SALIDA = os.path.join(RAIZ, "docs", "loop", "PLAN_V33_OPD02_FUSION.json")

SUP = "voz_del_cliente_voc"
ABS_ = "enfoque_mercado_voc"
FUENTE = "Winning at New Products - Robert G. Cooper"

# ---------------------------------------------------------------------------
# LO UNICO MIO: los textos finales unidos, sus origenes y su motivo de perdida.
# Los motivos salen de LA TABLA DE LOS SEIS MOTIVOS DE PERDIDA DE LINEA
# (docs/INTRA_DOMINIO_INFORME.md, seccion LOS SEIS MOTIVOS), citada por su nombre.
# ---------------------------------------------------------------------------
PASOS_FINALES = [
    {
        "origenes": ["S1", "A1"],
        "texto": (
            "Prepárate (o prepara a quien te ayude) para observar a tus clientes en su propio "
            "entorno, no solo entrevistarlos, y empieza por los más exigentes."
        ),
        "motivo": (
            "SALVAGUARDA: el superviviente manda observar a tus clientes y no dice a CUALES, "
            "asi que el paso se resuelve solo por el sesgo por defecto, observar a los que "
            "estan mas a mano. El absorbido dice contra que sesgo se elige (los mas exigentes) "
            "y el inciso se adosa al paso que protege, que es un paso de DECISION y no de "
            "ejecucion, que es la firma escrita de la clase."
        ),
    },
    {
        "origenes": ["S2"],
        "texto": (
            "Observa directamente a tu cliente en el lugar donde usa tu producto o servicio, por "
            "ejemplo acompañándolo durante su trabajo real, como ir con la policía en sus "
            "controles nocturnos."
        ),
        "motivo": "VERBATIM: el superviviente conserva su paso entero y el absorbido no le anade nada.",
    },
    {
        "origenes": ["S3"],
        "texto": (
            "Complementa tus entrevistas con observación real: tu cliente no siempre te va a "
            "contar sus problemas o su comportamiento real cuando lo entrevistas."
        ),
        "motivo": "VERBATIM: el superviviente conserva su paso entero. Aqui vive el 'hazles entrevistas a fondo' del absorbido, que ya decia lo mismo.",
    },
    {
        "origenes": ["A2", "A3"],
        "texto": (
            "Haz una evaluación preliminar de mercado y un análisis competitivo detallado de "
            "productos, precios y tecnologías antes de comprometer recursos importantes."
        ),
        "motivo": (
            "NO ES PERDIDA: es PRESERVAR. El campo preservar de OP-D-02 manda salvar de "
            "enfoque_mercado_voc la evaluacion preliminar de mercado y el analisis competitivo "
            "detallado, y el superviviente no dice ninguna de las dos en ninguno de sus cinco "
            "pasos. Entra como PASO NUEVO porque no hay paso del superviviente al que adosarlo "
            "sin cambiarle el objeto."
        ),
    },
    {
        "origenes": ["S4", "A4"],
        "texto": (
            "Usa lo que observas desde el inicio para diseñar tu producto, no lo dejes para "
            "verificar al final, y prueba tus primeras ideas de concepto con clientes reales "
            "antes de empezar el desarrollo formal."
        ),
        "motivo": (
            "NO ES PERDIDA: es PRESERVAR, la tercera pieza. El campo preservar manda salvar "
            "probar los conceptos con clientes reales antes del desarrollo formal, y se adosa "
            "al paso del superviviente que ya habla de usar lo observado para disenar, que es "
            "el mismo momento del proceso."
        ),
    },
    {
        "origenes": ["S5", "A5"],
        "texto": (
            "Mantén contacto con tu cliente durante todo el desarrollo, en ciclos cortos, no "
            "solo al principio y al final."
        ),
        "motivo": (
            "ALCANCE: el superviviente manda mantener el contacto durante todo el desarrollo y "
            "no dice a que cadencia. El absorbido la trae (ciclos cortos) y entra a la "
            "enumeracion que el superviviente ya tiene. Es la misma lectura de cadencia que "
            "OP-D-01 aplico en su paso 6, y se cita para que el criterio sea el mismo."
        ),
    },
]

CONDICIONES_FINALES = [
    {
        "origenes": ["SC1"],
        "texto": "Cuando no tienes ideas claras de qué hace diferente a tu producto",
        "motivo": "VERBATIM.",
    },
    {
        "origenes": ["SC2", "AC1"],
        "texto": (
            "Si estás diseñando tu producto a partir de supuestos propios y no de lo que "
            "observas en el terreno"
        ),
        "motivo": (
            "VERBATIM, y ABSORBE sin cambiar una letra: la condicion 1 del absorbido (cuando no "
            "tienes evidencia directa de lo que necesita tu cliente) es esta misma dicha al "
            "reves. No hay perdida que repartir."
        ),
    },
    {
        "origenes": ["SC3", "AC2"],
        "texto": (
            "Antes de avanzar a la etapa de desarrollo formal de tu producto, o mientras avanzas "
            "en él sin buscar retroalimentación externa"
        ),
        "motivo": (
            "ALCANCE: el superviviente nombra UN solo momento (antes de la etapa formal) y el "
            "absorbido trae el otro (mientras avanzas sin retroalimentacion externa). El segundo "
            "momento entra a la enumeracion que el superviviente ya tiene."
        ),
    },
]

ENTREGABLE_FINAL = (
    "Un resumen de lo que aprendiste observando y entrevistando a tu cliente, con la evaluación "
    "preliminar de mercado, el análisis competitivo y los resultados de las pruebas de concepto, "
    "que alimente directamente cómo diseñas tu producto"
)

RESUMEN_EXTRA = (
    " Y la escucha no se agota en observar: antes de comprometer recursos importantes conviene "
    "hacer la evaluación preliminar de mercado y el análisis competitivo detallado, y probar tus "
    "primeras ideas de concepto con clientes reales antes de empezar el desarrollo formal."
)

# Las TRES piezas del campo `preservar`, tal como hay que encontrarlas en el resultado.
PRESERVAR_LITERAL = [
    "evaluación preliminar de mercado",
    "análisis competitivo detallado",
    "clientes reales antes de empezar el desarrollo formal",
]

RASTROS = [
    "observar",
    "su propio entorno",
    "más exigentes",
    "evaluación preliminar de mercado",
    "análisis competitivo detallado",
    "productos, precios y tecnologías",
    "clientes reales",
    "desarrollo formal",
    "ciclos cortos",
    "todo el desarrollo",
]


def nodo(nid):
    with io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


def main():
    escribir = "--escribir" in sys.argv
    s, a = nodo(SUP), nodo(ABS_)

    fallos = []
    for nid, d in ((SUP, s), (ABS_, a)):
        if d.get("fuente") != FUENTE:
            fallos.append("%s: fuente %r, esperada %r" % (nid, d.get("fuente"), FUENTE))
        if d.get("deprecado") or d.get("deprecated"):
            fallos.append("%s: ya esta deprecado" % nid)

    sp = list(s.get("pasos_accionables") or [])
    ap = list(a.get("pasos_accionables") or [])
    sc = list(s.get("condiciones_activacion") or [])
    ac = list(a.get("condiciones_activacion") or [])
    print("LEIDO DEL GRAFO HOY, sin teclear nada:")
    print("  %-28s pasos %d  condiciones %d" % (SUP, len(sp), len(sc)))
    print("  %-28s pasos %d  condiciones %d" % (ABS_, len(ap), len(ac)))
    if len(sp) != 5 or len(ap) != 5 or len(sc) != 3 or len(ac) != 2:
        fallos.append("los conteos no son los que el plan espera (5/5 pasos, 3/2 condiciones)")

    origen = {}
    for i, t in enumerate(sp, 1):
        origen["S%d" % i] = t
    for i, t in enumerate(ap, 1):
        origen["A%d" % i] = t
    for i, t in enumerate(sc, 1):
        origen["SC%d" % i] = t
    for i, t in enumerate(ac, 1):
        origen["AC%d" % i] = t

    # GUARDA 2: cobertura exacta
    for etiqueta, finales, esperados in (
        ("pasos", PASOS_FINALES, ["S%d" % i for i in range(1, 6)] + ["A%d" % i for i in range(1, 6)]),
        ("condiciones", CONDICIONES_FINALES, ["SC%d" % i for i in range(1, 4)] + ["AC%d" % i for i in range(1, 3)]),
    ):
        usados = [o for f in finales for o in f["origenes"]]
        rep = sorted({o for o in usados if usados.count(o) > 1})
        faltan = sorted(set(esperados) - set(usados))
        sobran = sorted(set(usados) - set(esperados))
        print("  cobertura de %s: %d origenes de %d, repetidos %s, faltan %s, sobran %s"
              % (etiqueta, len(usados), len(esperados), rep, faltan, sobran))
        if rep or faltan or sobran:
            fallos.append("cobertura rota en %s" % etiqueta)

    # GUARDA 1: cada final empieza por el prefijo de su PRIMER origen
    for etiqueta, finales in (("pasos", PASOS_FINALES), ("condiciones", CONDICIONES_FINALES)):
        for k, f in enumerate(finales, 1):
            primero = origen.get(f["origenes"][0])
            if primero is None:
                fallos.append("%s %d: origen %s desconocido" % (etiqueta, k, f["origenes"][0]))
                continue
            pref = primero[:34]
            if not f["texto"].startswith(pref):
                fallos.append("%s %d: no empieza por el prefijo de %s (%r)"
                              % (etiqueta, k, f["origenes"][0], pref))
        print("  guarda de prefijo sobre %s: %d de %d revisados" % (etiqueta, len(finales), len(finales)))

    # GUARDA 3: el preservar, literal
    cuerpo = " ".join(f["texto"] for f in PASOS_FINALES)
    for pieza in PRESERVAR_LITERAL:
        ok = pieza in cuerpo
        print("  preservar %-55r %s" % (pieza, "PRESENTE" if ok else "AUSENTE"))
        if not ok:
            fallos.append("el preservar %r no aparece literal en los pasos finales" % pieza)

    print()
    if fallos:
        print("SE ABORTA, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1
    print("LAS CUATRO GUARDAS EN VERDE.")
    print()
    print("EL RESULTADO: %d pasos y %d condiciones (estandar de 3 a 6)"
          % (len(PASOS_FINALES), len(CONDICIONES_FINALES)))
    for i, f in enumerate(PASOS_FINALES, 1):
        print("  %d <- %-12s %s" % (i, ",".join(f["origenes"]), f["texto"][:88]))

    plan = {
        "operacion": "OP-D-02: la FUSION de la voz del cliente. voz_del_cliente_voc absorbe a enfoque_mercado_voc",
        "regla": "OP-D-02 (docs/plan/02_DESTEJIDOS.md), con la perdida repartida por LA TABLA DE LOS SEIS MOTIVOS DE PERDIDA DE LINEA y el alcance fijado por P.10 y P.12",
        "motivo": (
            "El acto se leyo ENTERO por P.5 (LD-72, LD-73 y LD-74, 15 ago 2026) y resulto ser una "
            "CADENA de tres A con DOS nodos puente y cero triangulos cerrados. La salida que P.10 "
            "nombra para ese caso es FUNDIR SOLO EL SUBCONJUNTO CERRADO Y ENLAZAR EL RESTO, y el "
            "subconjunto cerrado es el par del puesto 386. homework_frontend_loading y "
            "voice_of_customer_homework NO entran en la fusion."
        ),
        "fecha_corte": "2026-08-15",
        "superviviente": SUP,
        "absorbido": ABS_,
        "fuente_esperada": FUENTE,
        "pasos_totales_superviviente": len(sp),
        "pasos_totales_absorbido": len(ap),
        "condiciones_totales_superviviente": len(sc),
        "condiciones_totales_absorbido": len(ac),
        "origenes": origen,
        "prefijos_superviviente": [t[:34] for t in sp],
        "prefijos_absorbido": [t[:34] for t in ap],
        "prefijos_condiciones_superviviente": [t[:34] for t in sc],
        "prefijos_condiciones_absorbido": [t[:34] for t in ac],
        "grupos_pasos": PASOS_FINALES,
        "grupos_condiciones": CONDICIONES_FINALES,
        "pasos_finales": [f["texto"] for f in PASOS_FINALES],
        "condiciones_finales": [f["texto"] for f in CONDICIONES_FINALES],
        "entregable_final": ENTREGABLE_FINAL,
        "entregable_viejo": s.get("entregable_esperado"),
        "resumen_final": (s.get("resumen_teorico") or "") + RESUMEN_EXTRA,
        "resumen_viejo": s.get("resumen_teorico"),
        "titulo_sin_cambio": s.get("titulo_concepto"),
        "preservar_literal": PRESERVAR_LITERAL,
        "rastros": RASTROS,
        "redirecciones_esperadas": [
            {"nodo": "homework_frontend_loading", "campo": "nodos_previos"},
            {"nodo": "procesamiento_paralelo_con_espirales", "campo": "nodos_siguientes"},
            {"nodo": "ventaja_competitiva_producto", "campo": "nodos_previos"},
        ],
    }

    if not escribir:
        print()
        print("SIN --escribir: cero escrituras.")
        return 0
    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
    print()
    print("PLAN SELLADO ESCRITO: %s" % SALIDA)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
