# -*- coding: utf-8 -*-
r"""vuelta163_tarea1b_relectura_101.py . TAREA 1.b de la vuelta 163.

LA RELECTURA CONJUNTA DE LA `LD-OPC05-101` (acta 162, seccion 5.3, por
`AUDITOR.md` 1.3). La ciega del auditor, sellada en
`docs/loop/_auditor_v162_mis_adjudicaciones.txt` con sha1 `eda489c3` antes de
destapar nada, le da `C`. El registro dice `D`.

QUE HACE ESTE INSTRUMENTO Y QUE NO HACE, DICHO ANTES DE NADA:

  - SI HACE: (1) leer la vara `P.5.1` DE HOY del banco, frase y tabla de los
    cuatro ejemplares, PARSEADAS y no tecleadas; (2) imprimir los DOS nodos del
    par ENTEROS desde el grafo; (3) comprobar contra el grafo que el par existe
    en las DOS vistas; (4) imprimir los CUATRO ejemplares con sus dos nodos
    enteros, que es lo que los hace vara y no adorno; (5) MEDIR el cruce de
    entregables (el tercer criterio del ejemplar `100`) Y PUBLICAR SU
    CALIBRACION sobre los cuatro ejemplares.

  - NO HACE: decidir la clase. LA CLASIFICACION DE LOS PASOS ES UNA LECTURA DEL
    EJECUTOR, UNA TABLA A MANO, Y POR `EJECUTOR.md` 1 ("EL CASO ROJO SE PRUEBA
    POR MUTACION") ESO SE DECLARA EN VEZ DE FABRICARLE UN CASO ROJO QUE SE
    APRUEBE SOLO: **NO HAY CASO ROJO AUTOMATICO PARA EL VEREDICTO.** Lo que si
    tiene caso por mutacion es lo mecanico: el parseo de la vara y la medicion
    del cruce de entregables.

LA MEDICION DEL CRUCE DE ENTREGABLES SE PUBLICA CON SU CALIBRACION, Y ESO
CAMBIA COMO SE PUEDE USAR. El ejemplar `100` llama a ese criterio "LA DECISIVA
PORQUE SE LEE DE UN CAMPO Y SE PUEDE VOLVER A MEDIR". Mecanizado como cruce de
PALABRAS DISTINTIVAS del titulo, se corre aqui sobre los cuatro ejemplares y se
publica cuantos reproduce. Si no reproduce los cuatro, NO SE USA COMO DECISOR y
se dice: un corroborador que solo acierta parte de su propia vara no puede
sostener un veredicto.

USO:
  python scripts/loop/vuelta163_tarea1b_relectura_101.py
  python scripts/loop/vuelta163_tarea1b_relectura_101.py --mutacion
"""
import argparse
import io
import json
import os
import re
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
BANCO = os.path.join(RAIZ, "docs", "plan", "BANCO_DEL_PLAN.md")
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")

EN_DISPUTA = "LD-OPC05-101"

# Palabras que no distinguen a nada. Se listan aqui para que el cruce de
# entregables no se dispare con un articulo.
VACIAS = set("""el la los las un una unos unas de del al a y o u en con por para
sobre entre su sus tu tus mi mis lo se es son ser como que cual cuales""".split())


def sin_tildes(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s)
                   if not unicodedata.combining(c)).lower()


def cargar_grafo():
    return json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]


def vara_de_hoy():
    """`P.5.1` LEIDA HOY DEL BANCO: la frase entre comillas angulares y la tabla
    de los cuatro ejemplares. Nada de esto se teclea; si el banco no trae
    exactamente cuatro ejemplares, esto PARA."""
    texto = io.open(BANCO, encoding="utf-8").read()
    lineas = texto.split("\n")
    inicios = [i for i, l in enumerate(lineas, 1) if l.startswith("## P.5.1 ")]
    if len(inicios) != 1:
        raise SystemExit("ROJO: `## P.5.1` aparece %d veces en el banco." % len(inicios))
    inicio = inicios[0]
    siguientes = [i for i, l in enumerate(lineas, 1)
                  if i > inicio and re.match(r"^## P\.", l)]
    fin = min(siguientes) - 1 if siguientes else len(lineas)
    cuerpo = lineas[inicio - 1:fin]

    frase = " ".join(l.lstrip("> ").strip() for l in cuerpo if l.startswith(">")).strip()
    frase = re.sub(r"\s+", " ", frase.replace("**", ""))

    ejemplares = []
    for l in cuerpo:
        m = re.match(r"^\|\s*\*\*`(LD-OPC05-\d+)`\*\*\s*\|\s*\*\*(\w+)\*\*\s*\|\s*(.*?)\s*\|\s*$", l)
        if m:
            ejemplares.append((m.group(1), m.group(2), m.group(3).replace("**", "")))
    return inicio, fin, frase, ejemplares


def filas_del_registro():
    filas = {}
    for l in io.open(REGISTRO, encoding="utf-8"):
        l = l.strip()
        if not l:
            continue
        d = json.loads(l)
        cita = d.get("cita", "")
        m = re.match(r"^(LD-OPC05-\d+)", cita)
        if m:
            filas[m.group(1)] = d
    return filas


def imprimir_nodo(g, nid, sangria="   "):
    n = g[nid]
    print("%s%s" % (sangria, nid))
    print("%s  titulo:     %s" % (sangria, n.get("titulo_concepto")))
    print("%s  fuente:     %s" % (sangria, n.get("fuente")))
    print("%s  fase:       %s" % (sangria, n.get("fase_proyecto")))
    print("%s  entregable: %s" % (sangria, n.get("entregable_esperado")))
    pasos = n.get("pasos_accionables") or []
    print("%s  PASOS (%d):" % (sangria, len(pasos)))
    for i, p in enumerate(pasos, 1):
        print("%s   %2d. %s" % (sangria, i, p))


def arista_en_las_dos_vistas(g, a, b):
    sig_a = set(g[a].get("nodos_siguientes") or [])
    prev_a = set(g[a].get("nodos_previos") or [])
    sig_b = set(g[b].get("nodos_siguientes") or [])
    prev_b = set(g[b].get("nodos_previos") or [])
    return {
        "a_siguientes_trae_b": b in sig_a,
        "a_previos_trae_b": b in prev_a,
        "b_siguientes_trae_a": a in sig_b,
        "b_previos_trae_a": a in prev_b,
    }


def palabras_distintivas(g, x, y):
    """Las palabras del titulo de X que NO estan en el titulo de Y. Es lo que
    hace falta para que el cruce no se dispare con un sustantivo de dominio
    compartido."""
    def toks(nid):
        t = sin_tildes(g[nid].get("titulo_concepto") or "")
        return set(w for w in re.findall(r"[a-z0-9]+", t) if w not in VACIAS and len(w) > 2)
    return toks(x) - toks(y)


def cruce_de_entregables(g, a, b, entregables=None):
    """EL TERCER CRITERIO DEL EJEMPLAR `100`, MECANIZADO: el entregable de X esta
    escrito EN TERMINOS DE Y si contiene alguna palabra DISTINTIVA del titulo de
    Y. `entregables` permite pasar copias mutadas sin tocar el grafo."""
    ent = entregables or {}
    ea = sin_tildes(ent.get(a, g[a].get("entregable_esperado") or ""))
    eb = sin_tildes(ent.get(b, g[b].get("entregable_esperado") or ""))
    da = palabras_distintivas(g, a, b)
    db = palabras_distintivas(g, b, a)
    # PALABRA ENTERA, NO PREFIJO. Lo cazo la propia prueba de mutacion de este
    # instrumento: con `\bmodel` (sin cierre) la palabra distintiva `model` de
    # "Business Model Canvas" casaba dentro de `modelo`, que es palabra
    # COMPARTIDA por los dos titulos, y el cruce se quedaba pegado en
    # ASIMETRICO aunque se le quitara al entregable la unica palabra que de
    # verdad nombra al otro. Un prefijo no es una palabra.
    en_a = sorted(w for w in db if re.search(r"\b%s\b" % re.escape(w), ea))
    en_b = sorted(w for w in da if re.search(r"\b%s\b" % re.escape(w), eb))
    if en_a and not en_b:
        veredicto = "ASIMETRICO: %s consume a %s" % (a, b)
    elif en_b and not en_a:
        veredicto = "ASIMETRICO: %s consume a %s" % (b, a)
    elif en_a and en_b:
        veredicto = "SIMETRICO: los dos entregables se nombran"
    else:
        veredicto = "NINGUNO: ningun entregable nombra al otro"
    return veredicto, en_a, en_b


def main(mutacion=False):
    print("=" * 78)
    print("VUELTA 163, TAREA 1.b: LA RELECTURA CONJUNTA DE LA LD-OPC05-101")
    print("=" * 78)
    print("")
    print("LO QUE ESTE INSTRUMENTO NO HACE: no decide la clase. La clasificacion de")
    print("los pasos es una LECTURA DEL EJECUTOR, tabla a mano, y por EJECUTOR.md 1")
    print("SE DECLARA QUE NO HAY CASO ROJO AUTOMATICO PARA EL VEREDICTO en vez de")
    print("fabricarle uno que se apruebe solo. El veredicto va en el reporte, con la")
    print("letra de P.5.1 delante.")
    print("")

    g = cargar_grafo()
    filas = filas_del_registro()

    print("A) LA VARA, LEIDA HOY DEL BANCO Y NO TECLEADA")
    inicio, fin, frase, ejemplares = vara_de_hoy()
    print("   docs/plan/BANCO_DEL_PLAN.md, lineas %d a %d" % (inicio, fin))
    print("   FRASE: %s" % frase)
    print("   CIFRA ejemplares parseados de la tabla: %d" % len(ejemplares))
    for eid, ver, motivo in ejemplares:
        print("      %s  %-7s  %s" % (eid, ver, motivo))
    if len(ejemplares) != 4:
        print("   PARADA: la vara congelada tiene CUATRO ejemplares y el banco trae %d."
              % len(ejemplares))
        return 1
    print("")

    print("B) EL PAR EN DISPUTA, CONTRA EL GRAFO Y ENTERO")
    fila = filas.get(EN_DISPUTA)
    if not fila:
        print("   PARADA: %s no esta en el registro." % EN_DISPUTA)
        return 1
    a, b = fila["par"]
    print("   %s | clase VIGENTE en el registro: %s | via: %s"
          % (EN_DISPUTA, fila["clase"], fila["via"]))
    print("   cita: %s" % fila["cita"])
    print("")
    imprimir_nodo(g, a)
    print("")
    imprimir_nodo(g, b)
    print("")

    print("C) LA ARISTA, EN LAS DOS VISTAS")
    vistas = arista_en_las_dos_vistas(g, a, b)
    for k in sorted(vistas):
        print("   %-24s %s" % (k, vistas[k]))
    print("   CIFRA vistas que traen el par: %d de 4" % sum(1 for v in vistas.values() if v))
    print("")

    print("D) LOS CUATRO EJEMPLARES, CON SUS DOS NODOS ENTEROS")
    print("   (una regla sin sus casos se vuelve a estrechar sola: los ejemplares")
    print("   son la vara tanto como la frase, y por eso se leen del grafo)")
    for eid, ver, motivo in ejemplares:
        f = filas.get(eid)
        if not f:
            print("   PARADA: el ejemplar %s no esta en el registro." % eid)
            return 1
        print("")
        print("   --- %s : %s (%s) | clase vigente en el registro: %s"
              % (eid, ver, motivo, f["clase"]))
        for nid in f["par"]:
            imprimir_nodo(g, nid, sangria="      ")
    print("")

    print("E) EL CRUCE DE ENTREGABLES, MEDIDO Y CON SU CALIBRACION")
    print("   Es el TERCER criterio del ejemplar 100, el que su razon llama 'la")
    print("   decisiva porque se lee de un campo y se puede volver a medir'.")
    print("   Mecanizado: el entregable de X esta escrito EN TERMINOS DE Y si trae")
    print("   alguna palabra DISTINTIVA del titulo de Y (las compartidas no cuentan).")
    print("")
    aciertos = 0
    for eid, ver, _m in ejemplares:
        f = filas[eid]
        x, y = f["par"]
        veredicto, en_x, en_y = cruce_de_entregables(g, x, y)
        predice = "D" if veredicto.startswith("ASIMETRICO") else "C"
        calza = "CALZA" if predice == f["clase"] else "NO CALZA"
        if predice == f["clase"]:
            aciertos += 1
        print("   %s (%s, clase %s): %s" % (eid, ver, f["clase"], veredicto))
        print("      palabras de %s dentro del entregable de %s: %s"
              % (y, x, ", ".join(en_x) or "ninguna"))
        print("      palabras de %s dentro del entregable de %s: %s"
              % (x, y, ", ".join(en_y) or "ninguna"))
        print("      predice %s -> %s" % (predice, calza))
    print("")
    print("   CIFRA ejemplares que el cruce reproduce: %d de %d" % (aciertos, len(ejemplares)))
    if aciertos < len(ejemplares):
        print("   POR TANTO NO SE USA COMO DECISOR, Y SE DICE: un corroborador que solo")
        print("   acierta parte de su propia vara no puede sostener un veredicto. La")
        print("   razon de la vuelta 160 lo cito como corroboracion del D de la 101; se")
        print("   mide aqui y se publica que, mecanizado, no reproduce la vara entera.")
    print("")
    veredicto, en_x, en_y = cruce_de_entregables(g, a, b)
    print("   EL PAR EN DISPUTA: %s" % veredicto)
    print("      palabras de %s dentro del entregable de %s: %s"
          % (b, a, ", ".join(en_x) or "ninguna"))
    print("      palabras de %s dentro del entregable de %s: %s"
          % (a, b, ", ".join(en_y) or "ninguna"))
    print("")

    print("F) LO QUE LA VUELTA 160 USO PARA TUMBAR LA VUELTA, Y NO ESTA EN LA VARA")
    razon = fila["razon"]
    for cita in ("LD-OPC05-027", "LD-OPC05-004"):
        veces = razon.count(cita)
        en_vara = any(cita == eid for eid, _v, _m in ejemplares)
        print("   %s citado en la razon de la 101: %d vez(ces) | es ejemplar de P.5.1: %s"
              % (cita, veces, "SI" if en_vara else "NO"))
    print("   CIFRA sub varas citadas en la razon que NO son ejemplares de P.5.1: %d"
          % sum(1 for c in ("LD-OPC05-027", "LD-OPC05-004")
                if razon.count(c) and not any(c == e for e, _v, _m in ejemplares)))
    print("")

    print("G) LA CIEGA DEL AUDITOR, COMPROBADA Y NO CITADA DE MEMORIA")
    sello = os.path.join(RAIZ, "docs", "loop", "_auditor_v162_mis_adjudicaciones.txt")
    print("   fichero: docs/loop/_auditor_v162_mis_adjudicaciones.txt")
    print("   existe: %s" % os.path.exists(sello))
    if os.path.exists(sello):
        txt = io.open(sello, encoding="utf-8", errors="replace").read()
        m = re.search(r"^\s*101\s+.*?\s([CD])\s*$", txt, re.M)
        print("   veredicto sellado para la 101, parseado del fichero: %s"
              % (m.group(1) if m else "NO PARSEADO"))
    print("")
    print("VERDE: dossier completo. EL VEREDICTO NO LO DA ESTE FICHERO: lo da la")
    print("lectura del ejecutor, publicada en el reporte con la letra de P.5.1")
    print("delante y SIN apoyarse en la 027 ni en la 004.")
    return 0


def prueba_de_mutacion():
    """CASO POSITIVO POR MUTACION SOBRE LO MECANICO. El veredicto de clase NO
    tiene caso rojo automatico y eso se declara arriba; lo que se muta aqui es
    lo que si es mecanico: el parseo de la vara y el cruce de entregables."""
    print("=" * 78)
    print("VUELTA 163, TAREA 1.b: CASO POSITIVO POR MUTACION (solo lo mecanico)")
    print("=" * 78)
    print("")
    g = cargar_grafo()
    filas = filas_del_registro()
    a, b = filas[EN_DISPUTA]["par"]
    casos = []

    _i, _f, frase, ejemplares = vara_de_hoy()
    casos.append(("la_vara_trae_cuatro_ejemplares", len(ejemplares), 4))
    casos.append(("la_frase_es_la_congelada",
                  "SOLO CUENTA COMO EXPANSION SI TRAE PROCEDIMIENTO PROPIO" in frase, True))
    ids = [e for e, _v, _m in ejemplares]
    casos.append(("los_cuatro_ejemplares_son_esos",
                  ids, ["LD-OPC05-052", "LD-OPC05-095", "LD-OPC05-122", "LD-OPC05-100"]))
    casos.append(("ni_la_027_ni_la_004_son_ejemplares",
                  ("LD-OPC05-027" in ids) or ("LD-OPC05-004" in ids), False))

    v0, _x, _y = cruce_de_entregables(g, a, b)
    casos.append(("el_par_en_disputa_sale_asimetrico", v0.startswith("ASIMETRICO"), True))

    # MUTACION 1: se le quita al entregable de search la palabra del lienzo.
    ent = {b: (g[b].get("entregable_esperado") or "").replace("lienzo", "conjunto")}
    v1, _x, _y = cruce_de_entregables(g, a, b, entregables=ent)
    casos.append(("sin_la_palabra_del_lienzo_el_cruce_CAMBIA", v1 != v0, True))
    casos.append(("sin_la_palabra_del_lienzo_deja_de_ser_asimetrico",
                  v1.startswith("ASIMETRICO"), False))

    # MUTACION 2: se le mete al entregable del lienzo una palabra de search.
    ent2 = {a: (g[a].get("entregable_esperado") or "") + " tras la busqueda del modelo"}
    v2, _x, _y = cruce_de_entregables(g, a, b, entregables=ent2)
    casos.append(("con_la_palabra_de_search_el_cruce_SE_VUELVE_SIMETRICO",
                  v2.startswith("SIMETRICO"), True))

    # MUTACION 3: la arista sigue en las dos vistas.
    vistas = arista_en_las_dos_vistas(g, a, b)
    casos.append(("el_par_existe_en_las_dos_vistas",
                  sum(1 for v in vistas.values() if v), 4))

    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("")
    print("   CIFRA casos: %d | CIFRA que pasan: %d | CIFRA que fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")
    print("   SEGUNDA PASADA: SE MUTA EL VALOR ESPERADO DE CADA CASO Y TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, list):
            mutado = esperado + ["LD-OPC05-999"]
        else:
            mutado = str(esperado) + "_MUTADO"
        cae = (real != mutado)
        print("   %-52s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    print("")
    print("   CIFRA casos que CAEN al mutar su esperado: %d de %d" % (caen, len(casos)))
    if fallos or caen != len(casos):
        print("ROJO: la bateria no se comporta.")
        return 1
    print("VERDE: %d casos, los %d pasan y los %d CAEN al mutarles el valor esperado."
          % (len(casos), len(casos), len(casos)))
    print("Y SE REPITE LO QUE IMPORTA: NINGUNO DE ESTOS CASOS DECIDE LA CLASE. El")
    print("veredicto de la 101 es una lectura a mano y NO TIENE CASO ROJO AUTOMATICO.")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutacion", action="store_true")
    args = ap.parse_args()
    raise SystemExit(prueba_de_mutacion() if args.mutacion else main())
