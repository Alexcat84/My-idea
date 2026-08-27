# -*- coding: utf-8 -*-
r"""vuelta98_tarea3_relectura_par42.py . VUELTA 98, TAREA 3: LA RELECTURA
CONJUNTA DEL PAR 42, Y EL RECOMPUTO DEL ADDENDUM QUE ARRASTRA.

POR QUE NACE (acta de la vuelta 97, seccion 3.2, linea 34789: la unica
discrepancia de las trece lecturas ciegas del auditor, y cae DENTRO de los
discutibles que el reporte 97 marco). El auditor lee **D** donde el ejecutor
escribio **A**, y por `AUDITOR.md` 1.3 NO lo cambia el: deja su caso escrito y
el ejecutor decide con la vara, contra el grafo.

LA DECISION DE ESTA VUELTA, y va con su razon y no con su conclusion sola: EL
PAR 42 SE MUEVE DE A A D. Ver la razon larga en el reporte y en la nueva razon
de la fila, que se escribe SIN BORRAR la vieja.

QUE MUEVE, y por eso hay recomputo y no solo un cambio de celda: la clase del 42
vive en `docs/plan/`, publicada en TRES sitios que este instrumento actualiza en
un solo gesto y con las cifras LEIDAS DEL JSONL, nunca tecleadas:
  1. `docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl`, fila 42: `clase` y `razon`
  2. `docs/plan/OPERACIONES.jsonl`, nota de OP-E-03: "RESULTADO: A 3, B 1, C 0,
     D 56. Los tres A son los pares 42, 88, 100."
  3. `docs/plan/04_ENLACES.md`, la tabla del apartado de la vuelta 97

LO QUE NO MUEVE, Y SE COMPRUEBA EN VEZ DE SUPONERSE:
  - LA DIRECCION del par NO cambia (`cultura_justa_2 -> preguntar_que_no_quien`
    sigue siendo madre e hijo; lo que cambia es la clase), asi que las cifras de
    direccion (33 afirmadas, 27 no resueltas) siguen igual. El instrumento las
    RECUENTA del JSONL y CAE si se movieron.
  - EL MARCADOR DEL CRIBADO Y LA TASA POR DOMINIO del banco 9.27 no se tocan:
    estos veredictos son LECTURA DIRIGIDA y viven fuera de la cola, cosa que las
    propias filas declaran en sus campos y el instrumento vuelve a comprobar.
  - NINGUNA CLASE DEL TRAMO 1 se mueve. El par 12 se queda en A, adjudicado por
    el acta 97 seccion 3.2 (b): su hijo esta repartido entre los pasos 1, 2 y 4
    de su madre, o sea que NO cabe dentro de UN paso y el test de reconocimiento
    del 9.6.2 no se cumple. El instrumento LO COMPRUEBA leyendo el fichero del
    tramo 1 y CAE si el 12 no sigue en A.

MECANICA DE ROJO, y no escribe nada si salta: (i) la fila 42 no esta o no esta
en la clase de partida; (ii) las cifras viejas que hay que sustituir no aparecen
EXACTAMENTE una vez en su fichero; (iii) la correccion YA ESTA escrita; (iv) la
direccion, el marcador o el par 12 se movieron; (v) tras escribir, el recuento
del JSONL no cuadra con lo que se publico.

USO:
  python scripts/loop/vuelta98_tarea3_relectura_par42.py --medir
  python scripts/loop/vuelta98_tarea3_relectura_par42.py --simular
  python scripts/loop/vuelta98_tarea3_relectura_par42.py --aplicar
"""
import argparse
import collections
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMO2 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl")
TRAMO1 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl")
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
ENLACES = os.path.join(RAIZ, "docs", "plan", "04_ENLACES.md")

PUESTO = 42
CLASE_VIEJA = "A"
CLASE_NUEVA = "D"
MARCA = "CORRECCION DECLARADA (vuelta 98, TAREA 3, relectura conjunta del par 42)"

RAZON_NUEVA = (
    " %s: LA CLASE PASA DE A A D. El texto de arriba se queda entero, sin borrar "
    "una letra, que es la regla de EJECUTOR.md 8. LO QUE ESTABA MAL EN MI LECTURA, "
    "verificado hoy contra dataset/metadata/master_graph.json y no contra mi "
    "recuerdo: (1) di por SOLAPE el paso 2 del hijo ('preguntate que elementos del "
    "sistema, las herramientas o las tareas influyeron'), pero el paso 2 de la "
    "madre solo dice QUE preguntar ('que es responsable en vez de quien es "
    "responsable') y NO dice DONDE mirar; nombrar los tres sitios donde mirar ya "
    "es el principio del como, o sea residuo y no solape. Con eso el residuo son "
    "TRES movimientos y no dos. (2) Y aunque el residuo fueran solo los pasos 3 y "
    "4, no son dos lineas sueltas: el 4 CONSUME la salida del 3 ('usa LO QUE "
    "ENCUENTRES'), y una dependencia entre dos pasos es lo que hace una secuencia "
    "en vez de una lista. (3) LA SENIAL DE VERIFICACION DEL 9.6.2, la de los "
    "entregables, que no mire la primera vez y decide mas rapido que los pasos: la "
    "madre entrega 'un protocolo de respuesta a incidentes' (diseno del programa "
    "organizacional) y el hijo entrega 'un registro del incidente centrado en que "
    "condiciones lo generaron'. El producto del hijo NO es uno de los productos de "
    "la madre: es lo que el paso 2 de la madre produce al ejecutarse, que es la "
    "firma exacta de madre e hijo. (4) SE COMPROBO EL OTRO SENTIDO para descartar "
    "la figura del 9.22: cultura_justa_2 no despliega en procedimiento ninguna "
    "linea de preguntar_que_no_quien (su materia propia son los pasos 1, 3 y 4, "
    "sobre no comprar programas prediseniados, involucrar pares con credibilidad "
    "tecnica y justicia restaurativa, y ninguno expande un paso del hijo), asi que "
    "hay PROCEDIMIENTO EN UN SOLO SENTIDO: tercera fila del 9.22, madre e hijo, el "
    "par CONTINUA, D. LA DIRECCION NO CAMBIA: sigue cultura_justa_2 -> "
    "preguntar_que_no_quien. Y NINGUNA CLASE DEL TRAMO 1 SE MUEVE: el par 12 se "
    "queda en A por la adjudicacion del acta 97 seccion 3.2 (b), porque su hijo "
    "esta repartido entre los pasos 1, 2 y 4 de su madre y el test de "
    "reconocimiento del 9.6.2 no se cumple ahi."
    % MARCA
)


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def escribir(ruta, filas):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        for x in filas:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")


def cuentas(filas):
    c = collections.Counter(f["clase"] for f in filas)
    a = sorted(f["puesto_tramo"] for f in filas if f["clase"] == "A")
    b = sorted(f["puesto_tramo"] for f in filas if f["clase"] == "B")
    con_dir = sum(1 for f in filas if f.get("direccion_leida"))
    sin_dir = sorted(f["puesto_tramo"] for f in filas if not f.get("direccion_leida"))
    return c, a, b, con_dir, sin_dir


def palabra(n):
    return {1: "El unico", 2: "Los dos", 3: "Los tres", 4: "Los cuatro",
            5: "Los cinco"}.get(n, "Los %d" % n)


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--medir", action="store_true")
    g.add_argument("--simular", action="store_true")
    g.add_argument("--aplicar", action="store_true")
    a = ap.parse_args()

    fallos = []
    t2 = cargar(TRAMO2)
    t1 = cargar(TRAMO1)
    fila = [f for f in t2 if f.get("puesto_tramo") == PUESTO]

    c_antes, a_antes, b_antes, dir_antes, sindir_antes = cuentas(t2)

    print("=" * 100)
    print("RELECTURA CONJUNTA DEL PAR %d, VUELTA 98 TAREA 3" % PUESTO)
    print("=" * 100)
    print("FICHERO DEL TRAMO 2: %d filas, contadas" % len(t2))
    print("FICHERO DEL TRAMO 1: %d filas, contadas" % len(t1))
    print()
    print("ESTADO ANTES, contado del JSONL y no tecleado:")
    print("   clases: A %d, B %d, C %d, D %d"
          % (c_antes["A"], c_antes["B"], c_antes["C"], c_antes["D"]))
    print("   los A: %s" % ", ".join(str(x) for x in a_antes))
    print("   los B: %s" % ", ".join(str(x) for x in b_antes))
    print("   direccion: %d afirmadas, %d no resueltas" % (dir_antes, len(sindir_antes)))

    if len(fila) != 1:
        fallos.append("el puesto %d aparece %d veces en el tramo 2, se esperaba 1"
                      % (PUESTO, len(fila)))
    elif fila[0].get("clase") != CLASE_VIEJA:
        fallos.append("el puesto %d esta en clase %r y se esperaba %r"
                      % (PUESTO, fila[0].get("clase"), CLASE_VIEJA))
    elif MARCA in (fila[0].get("razon") or ""):
        fallos.append("la correccion del puesto %d YA ESTA escrita" % PUESTO)

    # el par 12 del tramo 1 NO se mueve, y se comprueba en vez de suponerse
    f12 = [f for f in t1 if f.get("puesto_tramo") == 12]
    if len(f12) != 1:
        fallos.append("el par 12 aparece %d veces en el tramo 1, se esperaba 1" % len(f12))
    elif f12[0].get("clase") != "A":
        fallos.append("el par 12 del tramo 1 esta en clase %r y tiene que seguir en A"
                      % f12[0].get("clase"))
    else:
        print("   par 12 del tramo 1: clase %s, INTACTO (adjudicacion 3.2 (b) del acta 97)"
              % f12[0]["clase"])

    # la marca de LECTURA DIRIGIDA de la fila que se toca sigue completa
    if len(fila) == 1:
        f = fila[0]
        if (f.get("marca") != "LECTURA DIRIGIDA" or not f.get("fuera_de_la_cola")
                or f.get("mueve_el_marcador_del_cribado") is not False
                or not f.get("fuera_de_la_tasa_por_dominio")):
            fallos.append("la fila %d no trae la marca completa de LECTURA DIRIGIDA"
                          % PUESTO)

    # las cifras viejas tienen que estar EXACTAMENTE una vez donde se van a tocar
    nota_vieja = "RESULTADO: A %d, B %d, C %d, D %d. %s A son los pares %s." % (
        c_antes["A"], c_antes["B"], c_antes["C"], c_antes["D"],
        palabra(len(a_antes)), ", ".join(str(x) for x in a_antes))
    ops = cargar(OPERACIONES)
    op = [o for o in ops if o.get("id_op") == "OP-E-03"]
    if len(op) != 1:
        fallos.append("OP-E-03 aparece %d veces, se esperaba 1" % len(op))
    elif (op[0].get("nota") or "").count(nota_vieja) != 1:
        fallos.append("la frase de RESULTADO del tramo 2 aparece %d veces en la nota, "
                      "se esperaba 1. Se buscaba: %r"
                      % ((op[0].get("nota") or "").count(nota_vieja), nota_vieja))

    enlaces = io.open(ENLACES, encoding="utf-8").read()
    fila_a_vieja = "| clase A, REPITE | **%d** |" % c_antes["A"]
    fila_d_vieja = "| clase D, CONTINUA | **%d** |" % c_antes["D"]
    for etiqueta, cadena in (("A", fila_a_vieja), ("D", fila_d_vieja)):
        if enlaces.count(cadena) != 1:
            fallos.append("la fila de clase %s del tramo 2 (%r) aparece %d veces en "
                          "04_ENLACES.md, se esperaba 1"
                          % (etiqueta, cadena, enlaces.count(cadena)))
    if MARCA in enlaces:
        fallos.append("la correccion YA ESTA en 04_ENLACES.md")

    if a.medir:
        print()
        print("ANCLAS QUE HABRIA QUE TOCAR, localizadas y contadas:")
        print("   OPERACIONES.jsonl: %r -> apariciones %d"
              % (nota_vieja, (op[0].get("nota") or "").count(nota_vieja) if op else 0))
        print("   04_ENLACES.md: %r -> %d | %r -> %d"
              % (fila_a_vieja, enlaces.count(fila_a_vieja),
                 fila_d_vieja, enlaces.count(fila_d_vieja)))
        print()
        if fallos:
            print("ROJO, %d cosa(s) no cuadran:" % len(fallos))
            for x in fallos:
                print("   %s" % x)
            return 1
        print("VERDE: todo lo que hay que tocar esta donde se espera y una sola vez.")
        return 0

    if fallos:
        print()
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    # --- se calcula el estado DESPUES sobre una copia, sin escribir todavia ---
    t2n = json.loads(json.dumps(t2))
    fn = [f for f in t2n if f["puesto_tramo"] == PUESTO][0]
    fn["clase"] = CLASE_NUEVA
    fn["razon"] = fn["razon"] + RAZON_NUEVA
    c_desp, a_desp, b_desp, dir_desp, sindir_desp = cuentas(t2n)

    if dir_desp != dir_antes or sindir_desp != sindir_antes:
        print("ROJO: la direccion se movio y este cambio no debia moverla "
              "(antes %d/%d, despues %d/%d). NO SE ESCRIBE NADA."
              % (dir_antes, len(sindir_antes), dir_desp, len(sindir_desp)))
        return 1

    nota_nueva = "RESULTADO: A %d, B %d, C %d, D %d. %s A son los pares %s." % (
        c_desp["A"], c_desp["B"], c_desp["C"], c_desp["D"],
        palabra(len(a_desp)), ", ".join(str(x) for x in a_desp))
    apostilla = (
        " [%s: la frase de arriba se queda entera y sin borrar una letra. LA CIFRA "
        "BUENA, RECOMPUTADA DEL PROPIO JSONL en la vuelta 98 y no tecleada, es: %s "
        "El par 42 pasa de A a D tras la relectura conjunta que pidio el acta 97 "
        "seccion 3.2; la direccion del par NO cambia y las cifras de direccion (%d "
        "afirmadas, %d no resueltas) siguen identicas, comprobado. Ninguna clase del "
        "tramo 1 se mueve: el par 12 sigue en A.]"
        % (MARCA, nota_nueva, dir_desp, len(sindir_desp)))

    fila_a_nueva = "| clase A, REPITE | **%d** |" % c_desp["A"]
    fila_d_nueva = "| clase D, CONTINUA | **%d** |" % c_desp["D"]
    bloque_enlaces = (
        "\n**[%s.]** La tabla de arriba se queda entera y sin borrar una celda. "
        "**LAS CIFRAS BUENAS, RECOMPUTADAS DEL PROPIO JSONL** en la vuelta 98 y no "
        "tecleadas: **clase A, REPITE: %d** (antes %d) y **clase D, CONTINUA: %d** "
        "(antes %d). El **par 42** pasa de **A** a **D** tras la relectura conjunta "
        "que pidio el acta de la vuelta 97 (seccion 3.2, linea 34789): el residuo "
        "del hijo no son dos lineas sueltas sino una secuencia con dependencia "
        "(el paso 4 consume la salida del 3), y los **entregables lo confirman** "
        "(la madre entrega un protocolo de respuesta a incidentes, el hijo un "
        "registro de incidente, que es lo que el paso 2 de la madre produce al "
        "ejecutarse). **La direccion NO cambia** y las cifras de direccion siguen "
        "en **%d** afirmadas y **%d** no resueltas. **Ninguna clase del tramo 1 se "
        "mueve**: el par **12** sigue en **A**.\n"
        % (MARCA, c_desp["A"], c_antes["A"], c_desp["D"], c_antes["D"],
           dir_desp, len(sindir_desp)))

    print()
    print("ESTADO DESPUES, recomputado del JSONL:")
    print("   clases: A %d, B %d, C %d, D %d"
          % (c_desp["A"], c_desp["B"], c_desp["C"], c_desp["D"]))
    print("   los A: %s" % ", ".join(str(x) for x in a_desp))
    print("   direccion: %d afirmadas, %d no resueltas (IDENTICAS, comprobado)"
          % (dir_desp, len(sindir_desp)))
    print()
    print("--- lo que se anade a la razon de la fila %d (aditivo) ---" % PUESTO)
    print(RAZON_NUEVA.strip())
    print()
    print("--- lo que se anade a la nota de OP-E-03 (aditivo, detras de la frase vieja) ---")
    print(apostilla.strip())
    print()
    print("--- lo que se anade a 04_ENLACES.md (aditivo, detras de la tabla) ---")
    print(bloque_enlaces.strip())

    if a.simular:
        print()
        print("SIMULACION: no se escribio nada.")
        return 0

    escribir(TRAMO2, t2n)
    op[0]["nota"] = (op[0]["nota"] or "").replace(nota_vieja, nota_vieja + apostilla, 1)
    escribir(OPERACIONES, ops)
    ancla = fila_d_vieja
    io.open(ENLACES, "w", encoding="utf-8", newline="\n").write(
        enlaces.replace(ancla, ancla + "\n" + bloque_enlaces, 1))

    # re-lectura de comprobacion
    t2b = cargar(TRAMO2)
    c_b, a_b, _, dir_b, sindir_b = cuentas(t2b)
    opb = [o for o in cargar(OPERACIONES) if o.get("id_op") == "OP-E-03"][0]
    enlb = io.open(ENLACES, encoding="utf-8").read()
    bien = (len(t2b) == len(t2)
            and [f for f in t2b if f["puesto_tramo"] == PUESTO][0]["clase"] == CLASE_NUEVA
            and c_b == c_desp and a_b == a_desp
            and dir_b == dir_antes and sindir_b == sindir_antes
            and nota_vieja in opb["nota"] and MARCA in opb["nota"]
            and fila_a_nueva not in enlb.split(MARCA)[0]  # la tabla vieja NO se reescribio
            and fila_a_vieja in enlb and fila_d_vieja in enlb and MARCA in enlb)
    print()
    print("APLICADO. Re-lectura: tramo 2 con %d filas, el %d en clase %s, "
          "clases A %d B %d C %d D %d, direccion %d/%d, texto viejo intacto en los tres "
          "ficheros: %s"
          % (len(t2b), PUESTO, [f for f in t2b if f["puesto_tramo"] == PUESTO][0]["clase"],
             c_b["A"], c_b["B"], c_b["C"], c_b["D"], dir_b, len(sindir_b),
             "SI" if bien else "NO"))
    return 0 if bien else 1


if __name__ == "__main__":
    raise SystemExit(main())
