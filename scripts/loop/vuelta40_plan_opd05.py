# -*- coding: utf-8 -*-
"""vuelta40_plan_opd05.py - CONSTRUYE Y SELLA el plan de la fusion de OP-D-05.

ESTRICTAMENTE DE SOLO LECTURA SOBRE EL GRAFO. Lo unico que escribe es el propio
plan en docs/loop/PLAN_V40_OPD05.json. No toca ni un nodo.

SUCESOR DECLARADO de los planes de la vuelta 38 (PLAN_V38_OPD04_TALLER.json y
PLAN_V38_OPD04_ALTERNANCIA.json), que se escribieron a mano. Este los GENERA, y
la diferencia importa por la regla 1 del EJECUTOR (la tabla se imprime, no se
teclea): el diccionario `origenes` sale VERBATIM de dataset/nodos, las
redirecciones y las duplicadas se MIDEN contra el grafo con la misma aritmetica
que usa el ejecutor de fusiones, y los pasos finales se DERIVAN de los grupos.
Lo unico tecleado son las agrupaciones y sus MOTIVOS, que es exactamente lo que
no puede salir de un instrumento: la lectura.

EL ESQUEMA es el de la vuelta 38 y no se cambia, porque el ejecutor
scripts/loop/vuelta39_fundir.py lo consume tal cual y sus trece guardas estan
escritas contra el.

Uso: python scripts/loop/vuelta40_plan_opd05.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop", "PLAN_V40_OPD05.json")
CAMPOS = ("nodos_previos", "nodos_siguientes")
OPUESTO = {"nodos_previos": "nodos_siguientes", "nodos_siguientes": "nodos_previos"}

SUP = "seleccion_ceo_fundador"
ABS = ["asignacion_de_titulos_ejecutivos", "errores_comunes_asignacion_roles"]
PREF = {"S": SUP, "T": ABS[0], "E": ABS[1]}

# ---------------------------------------------------------------------------
# LO UNICO TECLEADO: LOS GRUPOS Y SUS MOTIVOS. La lectura no sale de un script.
# ---------------------------------------------------------------------------
GRUPOS_PASOS = [
    (["S1", "E1", "E5"],
     "Evalúa la compatibilidad de motivaciones con tus socios antes de fundar "
     "juntos, y reúnete con tu equipo fundador para discutir abiertamente quién "
     "debe ser el CEO, sin asumir que la persona con la idea lo será "
     "automáticamente: confronta el conflicto de frente en lugar de evitarlo con "
     "títulos ambiguos",
     "LAS TRES PIEZAS SON EL MISMO MOMENTO: la conversacion que se tiene ANTES, "
     "antes de fundar y antes de titular. Y las dos del donante son ADVERTENCIAS, "
     "no procedimientos: por P.11 califican el paso que el superviviente ya tenia "
     "en vez de anadir pasos, y por esa misma regla VIAJAN ENTERAS, porque una "
     "advertencia es lo mas facil de perder en una fusion y lo mas caro de "
     "recuperar."),
    (["T1", "E2"],
     "Identifica quién es la 'persona de la idea' original en el equipo y evalúa "
     "objetivamente si es realmente la mejor opción para CEO",
     "LA MISMA PIEZA VISTA POR LOS DOS LADOS: el donante T la IDENTIFICA y el "
     "donante E obliga a PONERLA A PRUEBA. Sueltas son media pieza cada una, y el "
     "superviviente solo la nombraba de refilon dentro de su paso 1."),
    (["S2", "T2", "T3"],
     "Evalúa a los candidatos según su capacidad de ejecución, no solo su pasión y "
     "visión, midiendo el nivel de compromiso (full-time vs part-time) de cada "
     "cofundador y mapeando el capital humano, social y financiero que aporta cada "
     "fundador",
     "LA VARA DE LA EVALUACION. El superviviente decia CONTRA QUE evaluar (la "
     "capacidad de ejecucion) y no decia QUE MIRAR para medirla. Del donante "
     "viajan las dos varas concretas que le faltaban, que son ademas las que su "
     "propio resumen usa para explicar el 47 por ciento."),
    (["S3", "E3"],
     "Considera roles alternativos para la persona con la idea si no es el mejor "
     "CEO, como presidente de la junta (Chairman), director de tecnología (CTO) o "
     "director científico (Chief Scientific Officer), y sé cauteloso al asignar "
     "títulos C-level tempranamente, considerando el crecimiento futuro",
     "EL MISMO OBJETO: los titulos que NO son el de CEO. El superviviente trae el "
     "catalogo concreto de roles alternativos, que no tiene ninguno de los otros "
     "dos, y el donante trae la advertencia de no inflarlos. Juntas son la pieza "
     "entera; separadas, el catalogo se lee como un premio de consolacion."),
    (["T4", "E4"],
     "Negocia explícitamente el título de CEO antes de que surjan conflictos, y "
     "evita colocar automáticamente a cofundadores en la junta directiva solo por "
     "lealtad",
     "EL REPARTO DE PODER FORMAL, y el superviviente NO LO NOMBRABA en ninguno de "
     "sus cuatro pasos: ni la negociacion explicita del titulo ni la junta. Las "
     "dos piezas son de los donantes y las dos viajan, la segunda como advertencia "
     "por P.11."),
    (["S4", "T5"],
     "Documenta el acuerdo formalmente para evitar ambigüedad futura, dejando por "
     "escrito por qué se asignó cada título para futura referencia",
     "LA MISMA ACCION DICHA DOS VECES, y del donante viaja el POR QUE: no basta "
     "con documentar el acuerdo, hay que documentar el MOTIVO de cada titulo. Es "
     "la pieza que hace auditable la decision, que es de lo que trata el nodo."),
]

GRUPOS_CONDICIONES = [
    (["SC1", "TC1", "EC1"],
     "Si tú y tu equipo fundador aún no han definido formalmente quién es el CEO, "
     "o están por definir roles formales en las primeras etapas de formación del "
     "equipo, antes de asignar títulos formales",
     "LA MISMA CONDICION DICHA TRES VECES, y de los donantes viaja EL MOMENTO: "
     "las primeras etapas, antes de asignar titulos formales."),
    (["SC2", "TC2", "EC2"],
     "Si existe ambigüedad o conflicto latente sobre quién lidera tu equipo, hay "
     "tensión sobre quién debe ser CEO, o el equipo está evitando una conversación "
     "difícil sobre quién lidera",
     "LA MISMA CONDICION DICHA TRES VECES, y del donante viaja la senal mas util "
     "de las tres: que el equipo ESTA EVITANDO la conversacion, que es el sintoma "
     "que se ve desde fuera."),
    (["TC3"],
     "Cuando se está preparando documentación para inversionistas",
     "PIEZA PROPIA DEL DONANTE, sin equivalente en el superviviente ni en el otro: "
     "el disparador EXTERNO, el unico de los tres que no viene del propio equipo. "
     "Viaja entera y sola, y por eso tiene grupo propio."),
]

ENTREGABLE = ("Un acuerdo fundacional por escrito que designe formalmente al CEO "
              "y los demás títulos ejecutivos, con la decisión de cada uno "
              "justificada por la capacidad de liderazgo y el aporte de cada "
              "persona, revisado antes de firmarlo contra un checklist de los "
              "errores comunes al asignar roles")

RESUMEN = (
    "La decisión de quién será CEO suele tomarse de forma casual o por defecto: "
    "la persona con la idea, o la que tiene la voz más fuerte, sin que evalúes "
    "realmente quién es el mejor candidato. Esta decisión pesa simbólica y "
    "realmente, y por la inercia propia de cualquier organización, es muy difícil "
    "revertirla sin causar disrupción. Tienes que evaluar activamente quién tiene "
    "la capacidad de liderar en las distintas etapas cambiantes de tu startup, no "
    "solo quién tiene pasión y visión inicial. La asignación de títulos "
    "ejecutivos (CEO, CTO, COO, etc.) entre cofundadores es una de las "
    "negociaciones más críticas y difíciles al inicio de un startup: los títulos "
    "tienen significado simbólico y traducen en autoridad real, afectando tanto la "
    "motivación interna como la percepción externa (inversores, empleados), y los "
    "factores que determinan quién recibe qué título incluyen el nivel de "
    "compromiso de cada fundador, si es la 'persona de la idea' original, y su "
    "capital humano, social y financiero (experiencia previa fundando, años de "
    "experiencia laboral, capital semilla invertido). Las 'personas de la idea' "
    "tienen 47% de probabilidad de convertirse en CEO vs 12% de los no-idea, pero "
    "este ajuste inicial puede debilitarse conforme la startup madura. Y existen "
    "'caminos fáciles' que los equipos fundadores toman por evitar conflicto "
    "inmediato pero que generan problemas mayores a largo plazo: evitar el "
    "conflicto nombrando múltiples líderes, subestimar la 'inercia de títulos' (es "
    "difícil revertir un título mal asignado), inflar títulos C-level sin "
    "justificación real, querer aliados en la junta directiva, e ignorar "
    "motivaciones incompatibles entre socios.")

PRESERVAR = [
    "presidente de la junta (Chairman)",
    "Chief Scientific Officer",
    "capital humano, social y financiero",
    "full-time vs part-time",
    "47%",
    "inercia de títulos",
    "junta directiva solo por lealtad",
    "compatibilidad de motivaciones",
]
RASTROS = [
    "títulos ambiguos",
    "C-level",
    "inversionistas",
    "checklist",
    "capacidad de ejecución",
]


def leer(nid):
    return json.loads(io.open(os.path.join(NODOS, nid + ".json"),
                              encoding="utf-8").read())


def main():
    nodos = dict((nid, leer(nid)) for nid in [SUP] + ABS)

    # --- origenes VERBATIM, generados del fichero (regla 1) ---
    origenes = {}
    for p, nid in PREF.items():
        d = nodos[nid]
        for i, t in enumerate(d.get("pasos_accionables") or [], 1):
            origenes["%s%d" % (p, i)] = t
        for i, t in enumerate(d.get("condiciones_activacion") or [], 1):
            origenes["%sC%d" % (p, i)] = t

    # --- las redirecciones, con la MISMA aritmetica del ejecutor de fusiones ---
    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = leer(nombre[:-5])
            todos[d["node_id"]] = d
    redirecciones, muertos = [], []
    for nid, d in todos.items():
        if nid in ABS:
            continue
        for campo in CAMPOS:
            for muere in ABS:
                if muere in (d.get(campo) or []):
                    fila = {"nodo": nid, "campo": campo, "nombraba": muere}
                    (muertos if d.get("deprecado") or d.get("deprecated")
                     else redirecciones).append(fila)
    redirecciones.sort(key=lambda r: (r["nodo"], r["campo"], r["nombraba"]))
    muertos.sort(key=lambda r: (r["nodo"], r["campo"], r["nombraba"]))

    # --- las duplicadas que la fusion fabrica, misma aritmetica ---
    dup = []
    for r in redirecciones:
        antes = list(todos[r["nodo"]].get(r["campo"]) or [])
        despues = [SUP if x in ABS else x for x in antes]
        if (len(despues) - len(set(despues))) > (len(antes) - len(set(antes))):
            f = {"nodo": r["nodo"], "campo": r["campo"], "resuelve_a": SUP}
            if f not in dup:
                dup.append(f)

    # --- la simetrizacion esperada, medida y no supuesta ---
    propias = dict((c, list(nodos[SUP].get(c) or [])) for c in CAMPOS)
    sim_aristas = []
    for r in redirecciones:
        if r["nodo"] in propias[OPUESTO[r["campo"]]]:
            continue
        a = {"campo": OPUESTO[r["campo"]], "vecino": r["nodo"]}
        if a not in sim_aristas:
            sim_aristas.append(a)
    sim_aristas.sort(key=lambda a: (a["campo"], a["vecino"]))

    plan = {
        "operacion": ("OP-D-05, FUSION UNICA: LA SELECCION DEL CEO. "
                      "seleccion_ceo_fundador absorbe a "
                      "asignacion_de_titulos_ejecutivos y a "
                      "errores_comunes_asignacion_roles"),
        "estado": ("SELLADO en la vuelta 40, 19 ago 2026, ANTES de ejecutar. "
                   "El destejido de la operacion quedo declarado SIN COSTURA que "
                   "destejer (la unica que el archivo nombraba, en "
                   "seleccion_ceo_fundador, ya se la llevo OP-F-04-HOR en "
                   "2bd8dd76), asi que P.5 se contesta sobre texto YA ESTABLE."),
        "regla": ("OP-D-05 de docs/plan/02_DESTEJIDOS.md, acto 4 del cierre "
                  "transitivo, tres nodos y tres pares A del archivo (492, 673 y "
                  "833). Regla de reparto adjudicada el 11 ago 2026: cada perdida "
                  "al bloque del que proviene, y la que no tenga bloque al "
                  "superviviente."),
        "motivo": ("El acto se leyo ENTERO por P.5 con el texto ya estable y "
                   "resulto UNA sola familia: UN subconjunto cerrado que es el "
                   "acto entero, los 3 de 3 pares en A, CERO nodos puente de P.10 "
                   "y CERO aristas cojas en los tres. Los tres son de la MISMA "
                   "fuente, The Founder's Dilemmas: NO es acto de fuente mixta, "
                   "al contrario que los dos de OP-D-04."),
        "fecha_corte": "2026-08-19",
        "superviviente": SUP,
        "absorbidos": list(ABS),
        "fuente_esperada": nodos[SUP].get("fuente"),
        "prefijos": {"S": "%s (superviviente)" % SUP, "T": ABS[0], "E": ABS[1]},
        "origenes": origenes,
        "grupos_pasos": [{"origenes": o, "texto": t, "motivo": m}
                         for o, t, m in GRUPOS_PASOS],
        "grupos_condiciones": [{"origenes": o, "texto": t, "motivo": m}
                               for o, t, m in GRUPOS_CONDICIONES],
        "pasos_finales": [t for _o, t, _m in GRUPOS_PASOS],
        "condiciones_finales": [t for _o, t, _m in GRUPOS_CONDICIONES],
        "entregable_final": ENTREGABLE,
        "resumen_final": RESUMEN,
        "titulo_sin_cambio": nodos[SUP].get("titulo_concepto"),
        "etiqueta_arbol_sin_cambio": nodos[SUP].get("etiqueta_arbol"),
        "preservar_literal": PRESERVAR,
        "rastros": RASTROS,
        "entregable_viejo": nodos[SUP].get("entregable_esperado"),
        "resumen_viejo": nodos[SUP].get("resumen_teorico"),
        "pasos_totales": dict((nid, len(nodos[nid].get("pasos_accionables") or []))
                              for nid in [SUP] + ABS),
        "condiciones_totales": dict(
            (nid, len(nodos[nid].get("condiciones_activacion") or []))
            for nid in [SUP] + ABS),
        "eleccion_p8": {
            "regla": ("P.8, EL CABLEADO DESEMPATA, NO DECIDE. Donde el contenido "
                      "dice algo manda el contenido, aunque el margen de aristas "
                      "apunte al otro lado."),
            "decide": "EL CONTENIDO",
            "elegido": SUP,
            "especie_de_9_3_1": ("POR ELEGIR. De los TRES pares A, UNO SOLO nombra "
                                 "ganador en su razon (el 673). No hay GANADOR POR "
                                 "DERECHO, asi que la eleccion es de P.8."),
            "lectura_de_contenido": [
                "1. PADRE DECLARADO POR EL ARCHIVO, que P.8 cuenta como CONTENIDO "
                "con el mismo peso que el texto. La razon del par 673 dice, "
                "literal: 'El corto cabe entero dentro del primer bloque del "
                "largo'. El corto es errores_comunes_asignacion_roles y el primer "
                "bloque del largo es lo que HOY es seleccion_ceo_fundador entero, "
                "sus cuatro pasos, porque el segundo bloque ya se lo llevo "
                "OP-F-04-HOR. O sea que el archivo declara CONTENIDO de uno "
                "contenido en el otro, y nombra al continente. Es ademas el UNICO "
                "de los tres pares que nombra ganador.",
                "2. EL EJE COMUN ES EL TITULO DEL SUPERVIVIENTE. La razon del par "
                "492 dice que los dos 'mandan decidir con intencion quien es el "
                "CEO en vez de darlo por hecho', y el titulo de "
                "seleccion_ceo_fundador es, literal, 'Decidir con intencion quien "
                "sera el CEO fundador'. La cabeza de la serie es el nodo cuyo "
                "titulo ES el eje, y los otros dos son sus caras: la razon del "
                "833 los describe como 'el mismo reparto de titulos contado en "
                "positivo y en negativo'.",
                "3. P.11 SOBRE LOS DOS DONANTES, y desempata sin hacer falta el "
                "cableado. errores_comunes_asignacion_roles es, por la vara, "
                "LINEA y no procedimiento: quitadas las frases que empiezan por "
                "NO, por EVITA o por DE VERDAD (confrontar EN LUGAR DE evitarlo, "
                "evaluar OBJETIVAMENTE si es REALMENTE la mejor opcion, SER "
                "CAUTELOSOS, EVITAR colocar por lealtad) lo que queda es una "
                "lista de punteros. Un checklist de advertencias no es la cabeza "
                "de un procedimiento. Y P.11 lo cierra por el otro lado: eso NO "
                "autoriza a borrarlas, asi que las cinco viajan y este plan dice "
                "en que grupo cae cada una.",
                "4. PIEZA PROPIA QUE NADIE MAS TIENE: el catalogo concreto de "
                "roles alternativos (presidente de la junta, CTO, Chief "
                "Scientific Officer) es del superviviente y no aparece en ninguno "
                "de los otros dos. Es la unica pieza del acto que dice QUE HACER "
                "con la persona de la idea cuando no es el mejor CEO.",
            ],
            "cableado_solo_como_desempate": {
                "usado_para_decidir": False,
                "por_que_se_cita": ("porque va A FAVOR del elegido y hay que decir "
                                    "que NO hizo falta: si el contenido no hubiera "
                                    "hablado, esta cifra habria decidido sola, y si "
                                    "hubiera ido en contra, habria perdido igual. "
                                    "Es prelacion, no coincidencia afortunada."),
                "instrumento": ("scripts/loop/vuelta39_acto.py --op OP-D-05, salida "
                                "docs/loop/SALIDA_V40_OPD05_ACTO.txt, bloque 5"),
                "grados_medidos_hoy": {SUP: 9, ABS[0]: 4, ABS[1]: 4},
                "lectura": ("NUEVE contra CUATRO y CUATRO, y gana el nueve, que es "
                            "el mismo que gana por contenido. Cuando las dos varas "
                            "coinciden la regla no se luce, y por eso se dice que "
                            "la que mandaba era la primera."),
                "coste_medido_de_la_eleccion": ("CERO aristas. Los tres nodos tienen "
                                                "CERO aristas propias sin reciproco "
                                                "(bloque 6 de la salida del acto), "
                                                "asi que elegir a cualquiera de los "
                                                "tres no perdia ni una arista. La "
                                                "eleccion se juega entera en el "
                                                "contenido."),
            },
        },
        "simulacion": {
            "instrumento": ("scripts/plan/simular_fusion.py (P.7), "
                            "scripts/loop/vuelta40_reciprocidad_post.py y "
                            "scripts/loop/vuelta40_registros_no_grafo.py"),
            "redirecciones_esperadas": redirecciones,
            "redirecciones_no_tocadas_por_deprecadas": muertos,
            "duplicadas_nuevas_esperadas": dup,
            "registros_que_no_son_el_grafo": {
                "por_que_va_en_el_plan": ("la leccion de la vuelta 39: su plan "
                                          "enumero 17 referencias de NODO, no miro "
                                          "el registro de puentes, y Gate 0 cayo en "
                                          "rojo DESPUES de escribir. Aqui se "
                                          "enumera ANTES."),
                "instrumento": ("scripts/loop/vuelta40_registros_no_grafo.py, salida "
                                "en docs/loop/SALIDA_V40_OPD05_REGISTROS.txt"),
                "bridges_aprobados_que_los_nombran": 0,
                "registros_vivos_que_hay_que_redirigir": [],
                "aun_asi_se_corre": ("scripts/reanclar_por_resolutor.py ENTRE la "
                                     "fusion y run_phase1, practica adjudicada por "
                                     "el acta de la vuelta 39 para toda fusion "
                                     "futura. Una guarda que solo se corre cuando "
                                     "se sospecha no es una guarda."),
            },
            "simetrizacion_esperada": {
                "quien_la_escribe": ("scripts/run_phase1.py, paso 5, Simetrizacion "
                                     "de enlaces. NO la escribe el ejecutor de "
                                     "fusiones: el redirige a los vecinos y no toca "
                                     "la lista propia del superviviente."),
                "vara": ("la tasa de reciprocidad del grafo medida hoy es 99,59 por "
                         "ciento (15.445 de 15.508 aristas de nodos vivos, "
                         "resueltas por P.1), asi que romper la reciprocidad es un "
                         "defecto y no lo corriente."),
                "guarda_para_el_dia_de_la_ejecucion": ("symmetrize_added tiene que "
                                                       "traer EXACTAMENTE estas "
                                                       "entradas para el "
                                                       "superviviente, ni una mas "
                                                       "ni una menos"),
                "aristas": sim_aristas,
            },
        },
        "tabla_perdidas_p13": [],
    }

    # --- la tabla de perdidas, DERIVADA de los grupos (regla 1) ---
    destino = {}
    for k, (ors, _t, _m) in enumerate(GRUPOS_PASOS, 1):
        for o in ors:
            destino[o] = "paso %d del resultado" % k
    for k, (ors, _t, _m) in enumerate(GRUPOS_CONDICIONES, 1):
        for o in ors:
            destino[o] = "condicion %d del resultado" % k
    for clave in sorted(origenes, key=lambda x: (x[0], "C" in x, x)):
        nid = PREF[clave[0]]
        plan["tabla_perdidas_p13"].append({
            "pieza": clave,
            "texto": origenes[clave],
            "de": nid,
            "clase": "VIAJA" if clave in destino else "SE PIERDE",
            "destino": destino.get(clave, ""),
        })

    io.open(SALIDA, "w", encoding="utf-8", newline="\n").write(
        json.dumps(plan, ensure_ascii=False, indent=1) + "\n")

    print("PLAN SELLADO: %s" % os.path.relpath(SALIDA, RAIZ).replace("\\", "/"))
    print("  superviviente : %s" % SUP)
    print("  absorbidos    : %s" % ", ".join(ABS))
    print("  fuente de los tres: %s" % plan["fuente_esperada"])
    print("  origenes generados VERBATIM del fichero: %d" % len(origenes))
    print("  pasos finales : %d (estandar 3 a 6: %s)"
          % (len(plan["pasos_finales"]),
             "DENTRO" if 3 <= len(plan["pasos_finales"]) <= 6 else "FUERA"))
    print("  condiciones finales: %d" % len(plan["condiciones_finales"]))
    print("  redirecciones esperadas: %d" % len(redirecciones))
    for r in redirecciones:
        print("      %-46s %-18s %s" % (r["nodo"], r["campo"], r["nombraba"]))
    print("  deprecados que nombran y no se tocan: %d" % len(muertos))
    print("  duplicadas que la fusion fabrica: %d" % len(dup))
    for f in dup:
        print("      %-46s %s" % (f["nodo"], f["campo"]))
    print("  simetrizacion esperada: %d aristas" % len(sim_aristas))
    for a in sim_aristas:
        print("      %s.%-18s += %s" % (SUP, a["campo"], a["vecino"]))
    print("")
    print("  LA TABLA DE PERDIDAS, DERIVADA de los grupos y no tecleada:")
    viajan = [f for f in plan["tabla_perdidas_p13"] if f["clase"] == "VIAJA"]
    pierden = [f for f in plan["tabla_perdidas_p13"] if f["clase"] != "VIAJA"]
    for f in plan["tabla_perdidas_p13"]:
        print("      %-5s %-34s %-8s %s" % (f["pieza"], f["de"][:34], f["clase"],
                                            f["destino"]))
    print("      VIAJAN %d de %d. SE PIERDEN %d."
          % (len(viajan), len(plan["tabla_perdidas_p13"]), len(pierden)))
    print("      LECTURA: la regla de reparto de OP-D-05 manda cada perdida al")
    print("      bloque del que proviene, y la que no tenga bloque al")
    print("      superviviente. Con CERO perdidas no hay nada que repartir, y eso")
    print("      es lo que hay que comprobar al cierre, no suponerlo.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
