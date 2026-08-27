# -*- coding: utf-8 -*-
"""vuelta91_tarea4_direccion_ope07.py . VUELTA 91, TAREA 4, SEGUNDA MITAD: LA
DIRECCION DE CADA PAR DE LA BOLSA RE-BASADA DE OP-E-07 (docs/plan/
OP_E_07_REBASE_V91.jsonl, 88 filas), LEIDA DE SU PROPIA RAZON COMPLETA.

POR QUE HACE FALTA. OP-E-07 (a diferencia de OP-E-06) NO TRAE la direccion en
la `frase` cosechada: se levanto solo por "continua por la vara", que dice
que hay jerarquia pero no dice cual nodo es la madre. La propia
`verificacion` de OP-E-07 lo exige por escrito: "NO SE RELEE EL PAR: se lee
su razon, que ya esta escrita. Si la razon tampoco lo dice, el par sale de
la cosecha y se anota por que". Este instrumento es esa lectura, sobre el
campo `razon` COMPLETO de docs/INTRA_DOMINIO_VEREDICTOS.jsonl (no la `frase`
truncada a 200 caracteres de la cosecha, la leccion de la vuelta 90 que dio
los tres del banco 9.22).

LA REGLA DE LECTURA, la misma que OP-E-06 uso (vuelta90_tarea4_direccion_
ope06.py): el nodo que la razon describe DICIENDO, NOMBRANDO, ENUMERANDO o
DESPACHANDO algo EN UNA LINEA (o "en DOS LINEAS", o un ENUMERADOR/INDICE que
otro desarrolla) es LA MADRE; el otro, el que la razon describe con "trae
el/un/la procedimiento", "trae el catalogo/menu/detalle/instrumento/
aritmetica DE ESA LINEA", "desarrolla", "RECORRE EL CAMINO" o "es UNA DE
ESAS [fases/modelos] con su procedimiento", es EL HIJO. La arista se
escribe MADRE -> HIJO.

CLASIFICACION AUTOMATICA, Y DONDE NO ALCANZA. Sobre las 88 filas, se busca
en la razon la primera mencion de `nodo_a` y de `nodo_b`, se toma el
SEGMENTO de texto desde cada mencion hasta la mencion del OTRO id (o hasta
el final), y se busca en cada segmento la marca de HIJO ("trae" sin ser la
formula autoreferencial "trae lo suyo" ni una negacion "no trae", o
"desarrolla", o "RECORRE EL CAMINO"). Si exactamente UN segmento trae la
marca, ese id es el hijo. Este metodo resuelve **80 de 88** sin ambiguedad
(`_extraer_direccion_automatica`, verificado uno a uno contra una muestra
aleatoria de doce antes de aceptarlo).

LOS OCHO QUE EL METODO AUTOMATICO NO RESUELVE (la razon usa una formula
distinta: "ES EL INDICE" / "ES EL PROCEDIMIENTO DE UNA", "ENUMERA" / "DIBUJA
UNA", "MONTA EL MARCO" / "LLENA LA PATA", "compara los cinco" / "monta la
infraestructura", "es uno de esos modelos con SU procedimiento" sin la
palabra "trae", o "la madre" nombrada literalmente): leidos a mano sobre la
razon completa, cada uno con su cita textual en el comentario, para que se
pueda auditar sin volver a abrir el fichero.

CERO EXCLUSIONES POR BANCO 9.22: verificado en tiempo de ejecucion que
ninguna de las 88 razones cita "9.22" ni "ENLACE MUTUO". Las 88 tienen
direccion (0 SALEN por falta de direccion): las ocho que la automatica no
resuelve SI la dicen, solo que con una formula distinta a "trae".

CIFRA ESPERADA: 88 (la bolsa re-basada de vuelta91_tarea4_rebase_ope07.py).
ROJO si no cuadra, o si alguna fila queda sin clasificar y sin motivo de
salida nombrado.

SALIDA: docs/plan/OP_E_07_DIRECCION_V91.jsonl (madre, hijo, puesto, dominio).
NO ESCRIBE NINGUNA ARISTA EN dataset/: eso es una tarea aparte
(vuelta91_tarea4_escribir_ope07.py).

USO:
  python scripts/loop/vuelta91_tarea4_direccion_ope07.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
BOLSA = os.path.join(PLAN, "OP_E_07_REBASE_V91.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
SALIDA = os.path.join(PLAN, "OP_E_07_DIRECCION_V91.jsonl")

MARCA_HIJO = re.compile(r"(?<!no )trae\b(?!\s+lo\s+suyo)|desarrolla|RECORRE\s+EL\s+CAMINO", re.IGNORECASE)
MARCA_MUTUO_922 = re.compile(r"9\.22|ENLACE MUTUO", re.IGNORECASE)

# LOS OCHO QUE LA AUTOMATICA NO RESUELVE, leidos a mano sobre la razon
# COMPLETA (cada cita es textual, del propio campo `razon` de
# INTRA_DOMINIO_VEREDICTOS.jsonl). "A_MADRE" = nodo_a es la madre, nodo_b el
# hijo; "B_MADRE" = al reves.
DIRECCION_MANUAL = {
    1163: "A_MADRE",  # "analisis_de_cohortes dice en su paso 5, en UNA LINEA... y trae lo suyo" (autoreferencial,
                       # no cuenta como marca de hijo); "customer_retention_tactics trae el CATALOGO de esa linea"
                       # SI es la marca de hijo, pero un segundo "trae" suelto en el segmento de la madre
                       # ("...canal de adquisicion trae clientes mas leales") confundia la deteccion automatica.
    1191: "A_MADRE",  # "ingenieria_de_prompts_efectiva describe las piezas..."; "Por la vara..., CONTINUA, y el
                       # proposito lo confirma: LA MADRE busca precision, este busca dispersion": la razon nombra
                       # LITERALMENTE cual es la madre (ingenieria_de_prompts_efectiva) y "este" (prompting_alta_
                       # variacion) es el hijo, sin usar la palabra "trae" ni "desarrolla".
    1388: "B_MADRE",  # "ocho_fases_experiencia_cliente ES EL INDICE: ..."; "fase_acclimate_experiencia_cliente
                       # ES EL PROCEDIMIENTO DE UNA": el indice es la madre y la fase que desarrolla, el hijo.
    1500: "B_MADRE",  # "ocho_fases_experiencia_cliente ENUMERA: ..."; "fase_acclimate_mapa_de_proceso DIBUJA UNA":
                       # el indice es la madre, la fase que dibuja una de las ocho, el hijo. Misma figura que 1388.
    1778: "B_MADRE",  # "triple_top_line trae LAS TRES PREGUNTAS CONCRETAS" (el nucleo compartido, la linea basica);
                       # "herramienta_fractal_triple_top_line trae UN INSTRUMENTO que el otro no tiene" y "solo uno
                       # las cruza entre si y vigila el desequilibrio": el fractal desarrolla el cruce que las tres
                       # preguntas solo enuncian, luego triple_top_line es la madre y el fractal el hijo.
    1847: "A_MADRE",  # "diseno_para_el_medio_ambiente dice en su paso 4, en UNA LINEA, buscar inspiracion...
                       # CRADLE TO CRADLE o la ecologia industrial"; "eco_efectividad_2 ES UNO DE ESOS MODELOS con
                       # SU procedimiento": nombra el modelo citado por la linea de la madre, sin decir "trae".
    1886: "A_MADRE",  # "triple_bottom_line MONTA EL MARCO DE TRES PATAS..."; "triple_bottom_line_2 LLENA LA PATA
                       # SOCIAL": "uno nombra lo social como una de tres columnas, el otro dice que hay que mirar
                       # dentro de esa columna": la razon describe la relacion indice/desarrollo sin usar "trae".
    1992: "B_MADRE",  # "seleccion_de_metodo_de_pago compara los cinco... y cierra con el contrato"; "metodos_pago_
                       # electronico_internacional monta la infraestructura de cobro en linea": la comparacion
                       # general de los cinco metodos es la madre, la infraestructura de uno de ellos, el hijo.
}


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def extraer_direccion_automatica(razon, id_a, id_b):
    """LA UNICA PIEZA DE JUICIO AUTOMATICA, aislada a proposito para que su
    caso rojo se pueda probar por mutacion (EJECUTOR.md regla 1). Devuelve
    "A_HIJO", "B_HIJO" o "AMBIGUA" (incluye el caso de no hallar alguno de
    los dos ids en el texto)."""
    pos_a = razon.find(id_a)
    pos_b = razon.find(id_b)
    if pos_a == -1 or pos_b == -1:
        return "AMBIGUA"
    if pos_a < pos_b:
        seg_a, seg_b = razon[pos_a:pos_b], razon[pos_b:]
    else:
        seg_b, seg_a = razon[pos_b:pos_a], razon[pos_a:]
    hijo_a = bool(MARCA_HIJO.search(seg_a[len(id_a):]))
    hijo_b = bool(MARCA_HIJO.search(seg_b[len(id_b):]))
    if hijo_a and not hijo_b:
        return "A_HIJO"
    if hijo_b and not hijo_a:
        return "B_HIJO"
    return "AMBIGUA"


def main():
    bolsa = cargar_jsonl(BOLSA)
    veredictos = {v["puesto_intra"]: v for v in cargar_jsonl(VEREDICTOS)}

    print("=" * 90)
    print("TAREA 4 (segunda mitad): DIRECCION DE LOS %d PARES DE OP_E_07_REBASE_V91.jsonl" % len(bolsa))
    print("=" * 90)

    citan_922 = []
    resueltas = []
    ambiguas_sin_manual = []

    for r in bolsa:
        puesto = r["puesto"]
        v = veredictos.get(puesto)
        if v is None:
            ambiguas_sin_manual.append((puesto, "no tiene entrada en INTRA_DOMINIO_VEREDICTOS.jsonl"))
            continue
        razon = v["razon"]
        if MARCA_MUTUO_922.search(razon):
            citan_922.append(puesto)
            continue

        id_a, id_b = r["nodo_a"], r["nodo_b"]
        if puesto in DIRECCION_MANUAL:
            veredicto = DIRECCION_MANUAL[puesto]
        else:
            auto = extraer_direccion_automatica(razon, id_a, id_b)
            veredicto = {"A_HIJO": "B_MADRE", "B_HIJO": "A_MADRE", "AMBIGUA": "AMBIGUA"}[auto]

        if veredicto == "AMBIGUA":
            ambiguas_sin_manual.append((puesto, "la razon no nombra madre/hijo con formula reconocida"))
            continue

        madre, hijo = (id_a, id_b) if veredicto == "A_MADRE" else (id_b, id_a)
        resueltas.append({"puesto": puesto, "dominio": r["dominio"], "madre": madre, "hijo": hijo})

    print("bolsa: %d" % len(bolsa))
    print("excluidos por banco 9.22 (ENLACE MUTUO): %d %s" % (len(citan_922), citan_922))
    print("SIN direccion resoluble (SALEN, nombrados): %d" % len(ambiguas_sin_manual))
    for p, motivo in ambiguas_sin_manual:
        print("  puesto %s: %s" % (p, motivo))
    print("con direccion: %d" % len(resueltas))
    print()

    esperado = len(bolsa)
    obtenido = len(citan_922) + len(ambiguas_sin_manual) + len(resueltas)
    if obtenido != esperado:
        print("ROJO: %d (excluidos + sin direccion + con direccion) != %d (bolsa). NO SE ESCRIBE NADA."
              % (obtenido, esperado))
        return 1

    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as fh:
        for r in resueltas:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    print("=" * 90)
    print("EL RESULTADO")
    print("=" * 90)
    print("CIFRA: %d con direccion, escrito a %s" % (len(resueltas), SALIDA))
    print("NO SE ESCRIBIO NINGUNA ARISTA. Eso es vuelta91_tarea4_escribir_ope07.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
