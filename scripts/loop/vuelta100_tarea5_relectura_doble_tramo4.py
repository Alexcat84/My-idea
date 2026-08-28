# -*- coding: utf-8 -*-
r"""vuelta100_tarea5_relectura_doble_tramo4.py . VUELTA 100, TAREA 5: LA
RELECTURA AL DOBLE DEL TRAMO 4 (acta 99, credito de tanda bajado por la
discrepancia del 174, fuera de los discutibles marcados; AUDITOR.md 1.2).

MUESTRA, EN LOS DOS FLANCOS (letra nueva del acta 99, seccion 5): 5 filas
AFIRMADAS de MENOR `titulo_ratio` (el flanco que destapo el 174 y el 175, y
que hasta ahora nadie atacaba) y 5 filas NO RESUELTAS de MAYOR `titulo_ratio`
(el flanco de siempre). `titulo_ratio` se lee de
`docs/plan/DIFERENCIA_CONTRA_COLA.jsonl`, indexado por `puesto_tramo - 1`
(verificado: la fila 151 del tramo casa `conditions_precedent_financing` /
`entender_term_sheet`, identico en los dos ficheros).

EL ESTADO "AFIRMADA/NO RESUELTA" SE LEE EFECTIVO (aplicando correccion_v100
de la TAREA 3 de esta misma vuelta, 174 y 175 ya NO RESUELTA), no crudo, para
no repetir la caida de la 4.4.

RESULTADO DE LA LECTURA, contra el grafo (dataset/nodos/*.json), leido hoy:

  179 (juran_rcca_metodo -> diseno_implementacion_remedio, paso 3): SOSTENIDA.
  El hijo (6 pasos) es la elaboracion entera de "disenar e implementar el
  remedio"; la madre conserva definir/analizar/controlar sin tocar.

  177 (liderazgo_ejecutivo_innovacion -> estrategia_de_innovacion_de_producto,
  paso 1): SOSTENIDA. El hijo (6 pasos) es la elaboracion entera de "definir
  y comunicar tu estrategia de innovacion"; la madre conserva participar en
  decisiones go/kill, revisar portafolio, no microgestionar y metas propias.

  172 (desarrollo_en_espiral -> protocepto, paso 1): SE MUEVE. El hijo NO
  cabe entero en el paso 1 ("construir una version minima"): su paso 2
  ("muestra el protocept al cliente y recoge lo que piensa sobre tu
  hipotesis de mercado") es el paso 2 de la madre ("probar la version con
  clientes reales para medir interes, preferencia e intencion de compra"), y
  su paso 4 ("repite el ciclo en periodos cortos... acercandote a un
  prototipo que funcione de verdad") es el paso 5 de la madre ("repetir el
  ciclo varias veces... hasta pruebas de campo formales"). LA SENAL DEL
  ENTREGABLE (9.6.2) lo confirma: el entregable de la madre es "una serie
  documentada de prototipos iterativos, con registros de feedback de cliente
  en cada ciclo, que culmina en una definicion validada"; el del hijo es
  "una serie de versiones intermedias... con el feedback del cliente y los
  ajustes tecnicos en cada ciclo": el hijo reproduce la MITAD del entregable
  de la madre (serie mas feedback), no solo el resultado de un paso. El
  9.6.2 falla POR EXCESO DE GENERO. NO RESUELTA.

  169 (modelo_customer_development -> diseno_experimentos_pass_fail, paso 3):
  SOSTENIDA. El hijo (6 pasos) disena y ejecuta el experimento pass/fail
  entero; la madre conserva identificar el paso actual, formular la
  hipotesis, evaluar el stop sign y decidir retroceder, que el hijo no toca.

  161 (seis_herramientas_comunicacion_celebracion ->
  celebracion_automatizada_de_hitos, paso 2): SE MUEVE. LA PROPIA RAZON
  ORIGINAL YA LO CONCEDE: "el hijo es la version AUTOMATIZADA y CON UPSELL
  de la misma practica". Automatizacion de deteccion del hito y oferta de
  upsell NO estan en NINGUN paso de la madre (que solo cubre canal,
  mensaje, personalizacion por journey, momento y medicion de reaccion): el
  hijo no cabe entero en el paso 2, anade territorio que la madre entera no
  cubre. El 9.6.2 falla POR EXCESO DE GENERO. NO RESUELTA.

  181 (valor_intangible_sostenibilidad -> alineacion_engagement_estrategia_general,
  paso 1): SOSTENIDA (ya confirmada hoy en la relectura ciega del auditor,
  acta 99 seccion 3).

  151 (conditions_precedent_financing -> entender_term_sheet, paso 3):
  SOSTENIDA. FALSO AMIGO POR OBJETO COMPARTIDO confirmado: la madre negocia
  el contrato del fundador antes de firmar; el hijo clasifica clausulas por
  economia y control, un marco de lectura, no ese tramite.

  152: SOSTENIDA (ya adjudicada hoy, acta 99 4.1, CONFIRMADO).

  155 (transformacion_calidad_compromiso_alta_direccion_japon ->
  planificacion_calidad_crosby, paso 5): SOSTENIDA. Dos autores, dos marcos,
  ningun paso en comun: la madre es compromiso de la alta direccion
  (Deming), el hijo es inventario operativo de tareas (Crosby).

  157: SOSTENIDA (ya adjudicada hoy, acta 99 4.1, CONFIRMADO por el flanco
  dificil, contra el paso 3 de la madre).

DOS FILAS NUEVAS SE MUEVEN (172, 161), NINGUNA DE LAS DIEZ ESTABA EN LOS
DISCUTIBLES MARCADOS DEL ACTA 99: SE REGISTRAN COMO DISCUTIBLES NUEVOS, PARA
LA RELECTURA CIEGA DEL AUDITOR EN LA VUELTA SIGUIENTE (AUDITOR.md 1.3: la
decision final es del ejecutor cuando no hay auditor con quien contrastar en
vivo, pero se marca para que se verifique).

MECANICA DE ROJO, y no escribe nada si salta: (i) TRAMO4 no trae 33 filas;
(ii) el conteo de partida (efectivo, tras la TAREA 3) no da 11/22; (iii) las
filas 172 o 161 no existen, no tienen `direccion_leida`, o ya traen
`correccion_v100`; (iv) `DIFERENCIA_CONTRA_COLA.jsonl` no da 183 filas o el
cotejo puesto-a-puesto de 151 falla.

USO:
  python scripts/loop/vuelta100_tarea5_relectura_doble_tramo4.py --simular
  python scripts/loop/vuelta100_tarea5_relectura_doble_tramo4.py --aplicar
"""
import argparse
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMO4 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO4_V99.jsonl")
DIFCOLA = os.path.join(RAIZ, "docs", "plan", "DIFERENCIA_CONTRA_COLA.jsonl")

BASE_TOTAL = 33
BASE_AFIRMADA_EFECTIVA = 11
BASE_NO_RESUELTA_EFECTIVA = 22

CORRECCIONES = {
    172: {
        "campo_corregido": "direccion_leida",
        "valor_anterior": "desarrollo_en_espiral -> protocepto",
        "valor_nuevo": None,
        "cita_corregida": "banco 9.6.2 (senal del entregable: el del hijo reproduce serie "
                           "iterativa + feedback de cliente, la mitad del entregable de la "
                           "madre, no solo el resultado del paso 1)",
        "razon": (
            "CORRECCION DECLARADA (vuelta 100, TAREA 5, relectura al doble del tramo 4, "
            "discutible NUEVO, sin marcar previamente). El texto viejo de razon y "
            "direccion_leida NO SE BORRA. Leidos hoy dataset/nodos/desarrollo_en_espiral.json "
            "y dataset/nodos/protocepto.json: el hijo tiene CUATRO pasos y NO cabe entero en "
            "el paso 1 de la madre ('construir una version minima, rapida y economica'). Su "
            "paso 2 ('muestra ese protocept al cliente y recoge lo que piensa sobre tu "
            "hipotesis de mercado') es el paso 2 de la madre ('probar la version con clientes "
            "reales para medir interes, preferencia e intencion de compra'); su paso 4 "
            "('repite el ciclo en periodos cortos... acercandote cada vez mas a un prototipo "
            "que funcione de verdad') es el paso 5 de la madre ('repetir el ciclo varias "
            "veces... hasta llegar a pruebas de campo formales'). La senal del entregable "
            "(banco 9.6.2) lo confirma: la madre entrega 'una serie documentada de prototipos "
            "iterativos, con registros de feedback de cliente en cada ciclo, que culmina en "
            "una definicion validada'; el hijo entrega 'una serie de versiones intermedias... "
            "con el feedback del cliente y los ajustes tecnicos en cada ciclo', que reproduce "
            "la MITAD del entregable de la madre (serie mas feedback), no solo el resultado "
            "de construir. El test del 9.6.2 falla POR EXCESO DE GENERO: la razon original "
            "declaraba que 'los otros pasos de la madre... quedan enteros y sin tocar por el "
            "hijo', y esa afirmacion no se sostiene contra el texto de los pasos 2 y 4 del "
            "hijo. SE MUEVE: el par 172 pasa de DIRECCION AFIRMADA a NO RESUELTA. Clase D no "
            "cambia. DISCUTIBLE NUEVO, fuera de los marcados del acta 99: se registra para la "
            "relectura ciega del auditor en la vuelta siguiente."
        ),
    },
    161: {
        "campo_corregido": "direccion_leida",
        "valor_anterior": "seis_herramientas_comunicacion_celebracion -> celebracion_automatizada_de_hitos",
        "valor_nuevo": None,
        "cita_corregida": "banco 9.6.2 (exceso de genero: automatizacion de deteccion y "
                           "upsell no estan en ningun paso de la madre), no la coincidencia "
                           "casi verbatim del paso 2",
        "razon": (
            "CORRECCION DECLARADA (vuelta 100, TAREA 5, relectura al doble del tramo 4, "
            "discutible NUEVO, sin marcar previamente). El texto viejo de razon y "
            "direccion_leida NO SE BORRA. Leidos hoy "
            "dataset/nodos/seis_herramientas_comunicacion_celebracion.json y "
            "dataset/nodos/celebracion_automatizada_de_hitos.json: la propia razon original ya "
            "concede el punto sin verlo ('el hijo es la version AUTOMATIZADA y CON UPSELL de "
            "la misma practica de celebracion'). Ni la deteccion automatica del hito "
            "(implementar tecnologia/software) ni la oferta de upsell relevante estan en "
            "NINGUN paso de la madre (evaluar canal, disenar mensaje, personalizar por "
            "journey, elegir momento, medir reaccion): el hijo no cabe entero dentro del paso "
            "2, anade territorio que la madre ENTERA no cubre en ningun paso. El test del "
            "9.6.2 falla POR EXCESO DE GENERO. SE MUEVE: el par 161 pasa de DIRECCION AFIRMADA "
            "a NO RESUELTA. Clase D no cambia. DISCUTIBLE NUEVO, fuera de los marcados del "
            "acta 99: se registra para la relectura ciega del auditor en la vuelta siguiente."
        ),
    },
}

SOSTENIDAS = [179, 177, 169, 181, 151, 152, 155, 157]


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def estado_efectivo(fila):
    v100 = fila.get("correccion_v100")
    if v100 and v100.get("campo_corregido") == "direccion_leida":
        return bool(v100.get("valor_nuevo"))
    return bool(fila.get("direccion_leida"))


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--simular", action="store_true")
    g.add_argument("--aplicar", action="store_true")
    a = ap.parse_args()

    fallos = []
    filas = cargar(TRAMO4)
    if len(filas) != BASE_TOTAL:
        fallos.append("%s trae %d filas, se esperaban %d" % (os.path.basename(TRAMO4), len(filas), BASE_TOTAL))

    dc = cargar(DIFCOLA)
    if len(dc) != 183:
        fallos.append("DIFERENCIA_CONTRA_COLA.jsonl trae %d filas, se esperaban 183" % len(dc))
    else:
        f151 = next(f for f in filas if f.get("puesto_tramo") == 151)
        if dc[150].get("madre") != f151.get("madre_de_la_bolsa") or dc[150].get("hijo") != f151.get("hijo_de_la_bolsa"):
            fallos.append("el cotejo puesto 151 contra DIFERENCIA_CONTRA_COLA[150] no casa")

    afirmada_antes = sum(1 for f in filas if estado_efectivo(f))
    no_resuelta_antes = len(filas) - afirmada_antes
    if afirmada_antes != BASE_AFIRMADA_EFECTIVA or no_resuelta_antes != BASE_NO_RESUELTA_EFECTIVA:
        fallos.append("conteo efectivo de partida da afirmada=%d no_resuelta=%d, se esperaba %d/%d"
                      % (afirmada_antes, no_resuelta_antes, BASE_AFIRMADA_EFECTIVA, BASE_NO_RESUELTA_EFECTIVA))

    objetivo = {}
    for p in (172, 161):
        fila = next((f for f in filas if f.get("puesto_tramo") == p), None)
        if fila is None:
            fallos.append("no existe la fila puesto_tramo=%d" % p)
            continue
        if not fila.get("direccion_leida"):
            fallos.append("la fila %d ya esta sin direccion_leida" % p)
        if "correccion_v100" in fila:
            fallos.append("la fila %d ya trae correccion_v100" % p)
        objetivo[p] = fila

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("=" * 100)
    print("RELECTURA AL DOBLE DEL TRAMO 4 (vuelta 100, TAREA 5, %s)"
          % ("SIMULACION" if a.simular else "APLICADO"))
    print("=" * 100)
    print("ANTES (efectivo tras TAREA 3): afirmada %d, NO RESUELTA %d, total %d"
          % (afirmada_antes, no_resuelta_antes, len(filas)))
    print("SOSTENIDAS (8): %s" % ", ".join(str(x) for x in SOSTENIDAS))
    print("SE MUEVEN (2, discutibles nuevos): 172, 161")
    afirmada_desp = afirmada_antes - 2
    no_resuelta_desp = no_resuelta_antes + 2
    print("DESPUES: afirmada %d, NO RESUELTA %d, total %d (%.1f%%)"
          % (afirmada_desp, no_resuelta_desp, len(filas), 100.0 * no_resuelta_desp / len(filas)))

    if a.simular:
        print()
        print("SIMULACION: no se escribio nada.")
        return 0

    for p in (172, 161):
        objetivo[p]["correccion_v100"] = CORRECCIONES[p]

    with io.open(TRAMO4, "w", encoding="utf-8", newline="\n") as f:
        for fila in filas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

    filas2 = cargar(TRAMO4)
    bien = (len(filas2) == BASE_TOTAL
            and all("correccion_v100" in f for f in filas2 if f.get("puesto_tramo") in (172, 161))
            and all(f.get("direccion_leida") == CORRECCIONES[f["puesto_tramo"]]["valor_anterior"]
                    for f in filas2 if f.get("puesto_tramo") in (172, 161)))
    print()
    print("APLICADO. Re-lectura: %d filas, correccion_v100 presente en 172 y 161, "
          "direccion_leida vieja intacta: %s" % (len(filas2), "SI" if bien else "NO"))
    return 0 if bien else 1


if __name__ == "__main__":
    raise SystemExit(main())
