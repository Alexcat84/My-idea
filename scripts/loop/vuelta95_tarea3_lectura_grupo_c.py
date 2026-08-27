# -*- coding: utf-8 -*-
"""vuelta95_tarea3_lectura_grupo_c.py . VUELTA 95, TAREA 3(b) a (f): LA LECTURA
DE LAS 18 FILAS DEL GRUPO C del cribado de cita de linea
(scripts/loop/vuelta95_tarea3a_cribado_cita_de_linea.py), con la MISMA mecanica
exacta con la que se resolvieron el 1009, el 1281 y el 1992 (leer los
`pasos_accionables` de los dos nodos SIN la razon, adjudicar a ciegas, y SOLO
DESPUES destapar la razon completa de docs/INTRA_DOMINIO_VEREDICTOS.jsonl).

LA UNICA PREGUNTA QUE OP-E-07.verificacion MANDA: LA RAZON NOMBRA CUAL DE LOS
DOS NODOS ES LA MADRE, SI O NO, con la frase literal citada.

YA RESUELTOS SIN RELECTURA (encargo de la vuelta 95, TAREA 3.c y 3.d):
  1083: CONFIRMADO de la casa, la razon dice "que LA MADRE no tiene". QUEDA.
  1191: la razon usa literalmente "la madre" (busca precision, este busca
        dispersion). QUEDA. NO SE RELEE COMO DUDOSO (encargo explicito).
  1886: leido a ciegas por el acta de la vuelta 93 (ACTA_AUDITOR.md linea
        32695: "encaje limpio dentro del paso 1", razon "una de tres
        columnas ... dentro de esa columna", COINCIDE). QUEDA.

LAS 15 RESTANTES, leidas en esta vuelta, pasos primero y razon despues. EL
CRITERIO APLICADO (banco 9.6.2, "COMO SE RECONOCE UN PAR MADRE E HIJO: el hijo
cabe entero dentro de UN PASO de la madre"; la formula citable es "UNA LINEA
QUE TARDA VARIOS PASOS EN EJECUTARSE... ES UN PROCEDIMIENTO NOMBRADO EN UNA
LINEA"): la razon NOMBRA la madre si identifica un paso, fase o linea UNICA Y
CONCRETA de un nodo que el otro desarrolla ENTERO (aunque no use la palabra
"madre"), o si usa la palabra "madre" literalmente. La razon NO la nombra
(candidata a relectura conjunta, nunca resuelta sola) si compara CLASES
ENTERAS sin anclar a un paso especifico (el patron exacto que hizo salir al
1098, 1009, 1281 y 1992).

USO:
  python scripts/loop/vuelta95_tarea3_lectura_grupo_c.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
ENTRADA = os.path.join(PLAN, "OP_E_07_DIRECCION_V94.jsonl")

# (puesto, ancla citada de la razon o None, veredicto)
# veredicto: "QUEDA" (razon nombra la madre, con o sin la palabra literal) o
# "RELECTURA CONJUNTA" (duda genuina, NO se resuelve sola).
VEREDICTOS_15 = [
    (886, None, "RELECTURA CONJUNTA",
     "fit_problema_solucion 'trae un procedimiento que ESAS FASES no tienen' "
     "(las CUATRO fases enteras, no una): compara la clase entera contra lo "
     "que le falta, y el propio solape citado cae dentro de los pasos del "
     "HIJO (sus 'tres primeros'), no de un paso de la madre. Sin ancla."),
    (890, None, "RELECTURA CONJUNTA",
     "checkpoints_validacion 'trae el procedimiento para fijar ESOS UMBRALES, "
     "que LA ETAPA DA POR SUPUESTOS': plural, sin paso numerado ni 'es UNA "
     "LINEA'. Su hermano de la misma relacion (896) SI ancla a un paso "
     "('que es UNA LINEA de umbral'); este no lo hace."),
    (896, "que es UNA LINEA de umbral", "QUEDA",
     "customer_validation 'manda medir si por cada peso invertido... regresan "
     "dos, QUE ES UNA LINEA de umbral'. realizar_pruebas_pasa_no_pasa 'trae "
     "el procedimiento ENTERO de ese umbral'. Formula canonica del 9.6.2."),
    (909, "Sus dos referencias al mapa son lineas", "QUEDA",
     "estrategia_de_ventas: 'Sus dos referencias al mapa SON LINEAS, e "
     "influence_map_organizacional trae el procedimiento de construirlo'."),
    (910, "Su primer paso es UNA LINEA", "QUEDA",
     "evaluacion_industria_cliente: 'Su PRIMER PASO es UNA LINEA, y "
     "voice_of_customer_estrategico trae el procedimiento'."),
    (940, "Ese tercer paso es UNA LINEA", "QUEDA",
     "invitar_ia_a_todo: 'Ese TERCER PASO es UNA LINEA, y "
     "principio_mejora_continua_ia trae el procedimiento ENTERO de esa "
     "linea'."),
    (947, None, "RELECTURA CONJUNTA",
     "product_market_fit 'trae el CHECKLIST de seis evaluaciones que decide "
     "SI ESO alcanzo': evalua el RESULTADO del proceso entero de "
     "customer_discovery, no un paso especifico nombrado. Sin ancla clara."),
    (983, "en la cuarta [fase]... UNA LINEA", "QUEDA",
     "customer_discovery_overview: 'EN LA CUARTA dice evaluar si hay "
     "validacion suficiente: UNA LINEA'. realizar_pruebas_pasa_no_pasa "
     "'trae el procedimiento del umbral'."),
    (993, "Ese tercer paso es una linea", "QUEDA",
     "alineacion_etica_ia_negocio: 'Ese TERCER PASO es una linea, y "
     "comprender_alineacion_etica_ia trae la auditoria'."),
    (1020, "desarrolla UNA de las OCHO con procedimiento propio", "QUEDA",
     "fase_acclimate_experiencia_cliente 'desarrolla UNA de las OCHO [fases "
     "del programa] con procedimiento propio'. Misma jerarquia sana del "
     "puesto 829 con otra fase (razon lo cita explicito)."),
    (1057, "Ese segundo paso es una linea", "QUEDA",
     "celebracion_hitos_cliente: 'Ese SEGUNDO PASO es una linea, y "
     "regalos_estrategicos_sorpresa trae el procedimiento ENTERO'."),
    (1086, "Es una madre con tres hijos verificados", "QUEDA",
     "filosofia_customer_validation 'cierra con TRES PREGUNTAS en una sola "
     "linea'; decision_pivotar_o_proceder 'trae el procedimiento de "
     "contestarlas'. Ademas la razon dice literalmente 'Es una MADRE con "
     "tres hijos verificados', nombrando al mismo nodo de este par."),
    (1196, "Ese tercer paso es UNA LINEA", "QUEDA",
     "colaboracion_creador_consumidor: 'Ese TERCER PASO es UNA LINEA y "
     "co_creation_session trae su procedimiento'. El solape cae ENTERO en "
     "el primer bloque del hijo (veredicto INVARIANTE, dice la razon)."),
    (1220, "ingenieria_de_prompts_efectiva es la MADRE", "QUEDA",
     "'define el rol igual que LA MADRE'... 'ingenieria_de_prompts_efectiva "
     "ES LA MADRE y tiene CUATRO HIJAS SANAS'. La mas explicita de las 15."),
    (1844, None, "RELECTURA CONJUNTA",
     "productos_crudos 'NOMBRA EL PROBLEMA' (tres items enteros); "
     "diagnostico_de_productos_crudos 'TRAE EL PROCEDIMIENTO' (cuatro items "
     "enteros): sin paso numerado unico, la misma forma de clase-entera-"
     "contra-clase-entera que hizo salir al 1098/1009/1281. Marcado por "
     "prudencia pese a no ser identico a 886/947."),
]

YA_RESUELTOS = [
    (1083, "QUEDA", "CONFIRMADO de la casa: 'que LA MADRE no tiene' (acta 94)."),
    (1191, "QUEDA", "razon usa literalmente 'la madre' (acta 94, encargo 95 lo cierra sin releer)."),
    (1886, "QUEDA", "acta 93, ACTA_AUDITOR.md linea 32695: 'encaje limpio dentro del paso 1', "
                    "razon 'una de tres columnas ... dentro de esa columna', COINCIDE."),
]


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    filas = {f["puesto"]: f for f in cargar_jsonl(ENTRADA)}
    veredictos = {int(v["puesto_intra"]): v for v in cargar_jsonl(VEREDICTOS)}

    grupo_c_esperado = {886, 890, 896, 909, 910, 940, 947, 983, 993, 1020, 1057,
                        1083, 1086, 1191, 1196, 1220, 1844, 1886}
    vistos = set(p for p, _, _ in YA_RESUELTOS) | set(p for p, _, _, _ in VEREDICTOS_15)
    if vistos != grupo_c_esperado:
        print("ROJO: la lista cubierta (%d) no coincide con el grupo C esperado (%d). "
              "Diferencia: %s" % (len(vistos), len(grupo_c_esperado),
                                  sorted(vistos ^ grupo_c_esperado)))
        return 1

    print("=" * 90)
    print("LECTURA DEL GRUPO C, 18 PUESTOS (vuelta 95, TAREA 3.b a 3.f)")
    print("=" * 90)
    print()
    print("--- YA RESUELTOS SIN RELECTURA (3) ---")
    for p, v, nota in YA_RESUELTOS:
        f = filas[p]
        print("  %d | %s -> %s | %s | %s" % (p, f["madre"], f["hijo"], v, nota))
    print()
    print("--- LEIDOS EN ESTA VUELTA (15) ---")
    quedan, relectura = [], []
    for p, ancla, v, nota in VEREDICTOS_15:
        f = filas[p]
        print("  %d | %s -> %s | %s" % (p, f["madre"], f["hijo"], v))
        print("      ancla: %s" % (ancla or "(ninguna, esa es la razon)"))
        print("      %s" % nota)
        (quedan if v == "QUEDA" else relectura).append(p)
    print()
    print("QUEDAN (razon nombra la madre): %d de 15 -> %s" % (len(quedan), quedan))
    print("RELECTURA CONJUNTA (duda genuina, NO resueltos solo): %d de 15 -> %s"
          % (len(relectura), relectura))
    print()
    print("NINGUNO SALE ESTA VUELTA: cero aristas retiradas. Los %d de RELECTURA "
          "CONJUNTA quedan pendientes para la mesa, no adjudicados solos."
          % len(relectura))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
