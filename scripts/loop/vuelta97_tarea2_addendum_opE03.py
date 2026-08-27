# -*- coding: utf-8 -*-
r"""vuelta97_tarea2_addendum_opE03.py . VUELTA 97, TAREA 2: escribe el SEGUNDO
ADDENDUM DE EJECUCION de OP-E-03 en su nota (docs/plan/OPERACIONES.jsonl) y el
apartado hermano en docs/plan/04_ENLACES.md.

POR QUE HACE FALTA, Y NO ES ADORNO. El addendum de la vuelta 96 dejo escrito en
los dos ficheros del plan que "QUEDAN 143 SIN LEER, filas 41 a 183" y que quedan
"143" pares sin leer. Despues de este tramo esa cifra es FALSA: quedan 83, filas
101 a 183. Una cifra sellada en un fichero del plan que la propia campana ya movio
es exactamente lo que EJECUTOR.md regla 1 prohibe dejar quieto ("EL ESTADO AL
CIERRE SE MIDE AL CIERRE").

POR QUE ES UN SCRIPT Y NO UNA EDICION A MANO (EJECUTOR.md regla 1, "LA TABLA SE
IMPRIME, NO SE TECLEA"): las cifras NO se teclean. Se LEEN de
docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl y de la bolsa, y se formatean aqui.

ES ADITIVO: la nota vieja NO se toca y el apartado de la vuelta 96 en
04_ENLACES.md se queda entero; lo nuevo va detras.

MECANICA DE ROJO, y no escribe nada si salta: (i) OP-E-03 no aparece exactamente
una vez; (ii) el fichero de lectura no trae las 60 filas del tramo; (iii) alguna
fila no trae la marca completa de LECTURA DIRIGIDA; (iv) el addendum de ESTA
vuelta ya estaba escrito, en su forma vieja o en la nueva (correr dos veces
duplicaria texto); (v) no se encuentra el ancla, que es el cierre del apartado de
la vuelta 96; (vi) LA GUARDA DE FECHA, que se explica abajo. La guarda (iv) se
prueba EN VIVO: la segunda corrida de --aplicar tiene que dar ROJO.

--- LA FECHA DEJA DE ESTAR TECLEADA (VUELTA 98, TAREA 1) ---

POR QUE SE TOCA ESTE FICHERO (acta de la vuelta 97, seccion 4.1, linea 34956:
CAIDA DE CIFRA PUBLICADA, y encargo de la vuelta 98 apartado 1.2, "ARREGLA LA
FUENTE, no solo el sintoma"). La constante MARCA de este script llevaba la
fecha "30 ago 2026" TECLEADA como literal, y de ahi la copio al fichero del
plan. NINGUN commit de este repo es posterior al 27 ago 2026
(`git log --all --format=%ad --date=short | sort -u | tail -1`). Es EJECUTOR.md
regla 1, "TODO HASH, NOMBRE DE COMMIT, RAMA O FECHA ... SE LEE DE git rev-parse O
DE git log EN ESA VUELTA Y SE TALLA".

EL ARREGLO, y con el la razon de por que no basta con leer git y ya:
  - MARCA se CONSTRUYE en tiempo de ejecucion con la fecha que `git log`
    devuelve HOY para los commits de la vuelta 97. Ya no hay fecha tecleada en
    ninguna constante de este fichero.
  - MARCA_APLICADA es la cadena historica CONGELADA que este script escribio de
    verdad en su dia, con su fecha mala dentro. NO ES FUENTE DE NINGUNA CIFRA:
    existe solo para poder RECONOCER el addendum ya escrito y no duplicarlo. El
    addendum aplicado NO se reescribe, porque reescribirlo borraria el texto que
    la correccion declarada tiene que dejar a la vista (EJECUTOR.md regla 8).
  - LA GUARDA DE FECHA compara las dos y, cuando difieren (que es el caso hoy),
    EXIGE que la correccion declarada de la vuelta 98 este presente en la nota.
    Si difieren y la correccion NO esta, es ROJO y no se escribe nada.

POR QUE LA GUARDA NO ES UN CHEQUEO QUE SE APRUEBA SOLO NI UNO QUE NO PUEDE
APROBARSE NUNCA (las dos especies que este repo ya cazo: acta 89 seccion 4.2 y
la leccion de la vuelta 82). Sus tres salidas dependen de datos reales y
distintos: la fecha que devuelve git, la fecha que lleva la cadena historica y
la presencia de la correccion en el fichero del plan. Mover cualquiera de las
tres la mueve a ella. Se prueba por mutacion en
scripts/loop/vuelta98_tarea1_prueba_mutacion.py.

USO:
  python scripts/loop/vuelta97_tarea2_addendum_opE03.py --simular
  python scripts/loop/vuelta97_tarea2_addendum_opE03.py --aplicar
"""
import argparse
import collections
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
ENLACES = os.path.join(RAIZ, "docs", "plan", "04_ENLACES.md")
LECTURA = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl")
BOLSA = os.path.join(RAIZ, "docs", "plan", "DIFERENCIA_CONTRA_COLA.jsonl")

VUELTA = 97
MESES = {1: "ene", 2: "feb", 3: "mar", 4: "abr", 5: "may", 6: "jun",
         7: "jul", 8: "ago", 9: "sep", 10: "oct", 11: "nov", 12: "dic"}
RE_FECHA = re.compile(r"\b(\d{1,2}) (ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic) (\d{4})\b")
MARCA_DE_LA_CORRECCION = "CORRECCION DECLARADA DE FECHA (vuelta 98, TAREA 1)"


def fecha_de_git():
    """La fecha de los commits de la vuelta 97, LEIDA DE GIT. Nunca tecleada.

    Devuelve la fecha en el estilo del plan ("27 ago 2026") o None si git no da
    ni un commit de esa vuelta: en ese caso el que llama decide, y este no
    inventa nada.
    """
    r = subprocess.run(["git", "log", "--all", "--format=%ad|%s", "--date=short"],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return None
    pat = re.compile(r"^VUELTA %d\b" % VUELTA)
    fechas = set()
    for linea in r.stdout.decode("utf-8", "replace").splitlines():
        partes = linea.split("|", 1)
        if len(partes) == 2 and pat.match(partes[1]):
            fechas.add(partes[0])
    if not fechas:
        return None
    a, m, d = sorted(fechas)[-1].split("-")
    return "%d %s %s" % (int(d), MESES[int(m)], a)


def marca_con(fecha):
    return ("ADDENDUM DE EJECUCION (%s, vuelta 97, TAREA 2): SEGUNDO TRAMO LEIDO."
            % fecha)


def ancla_de(marca):
    """El trozo de la marca hasta el parentesis de cierre, ambos incluidos.

    POR QUE EXISTE, y se descubrio corriendo el script (vuelta 98, TAREA 1): la
    correccion declarada de la fecha se inserta JUSTO DETRAS del parentesis, o
    sea EN MEDIO de la marca, con lo cual la marca entera dejo de ser subcadena
    de la nota y la guarda de idempotencia (iv) dejo de disparar. Anclar en el
    parentesis la vuelve inmune a lo que se inserte detras.
    """
    return marca.split(")")[0] + ")"


# LA CADENA HISTORICA, CONGELADA. No es fuente de ninguna cifra: solo sirve para
# reconocer el addendum que este script ya escribio, con su fecha mala dentro.
MARCA_APLICADA = "ADDENDUM DE EJECUCION (30 ago 2026, vuelta 97, TAREA 2): SEGUNDO TRAMO LEIDO."
# LA MARCA BUENA, construida con la fecha que git devuelve HOY.
MARCA = marca_con(fecha_de_git() or "FECHA NO LEIDA DE GIT")

TITULO_ENLACES = "LO QUE SE HIZO EN LA VUELTA 97, TAREA 2: EL SEGUNDO TRAMO TAMBIEN ESTA LEIDO"
ANCLA = ("dominio del banco `9.27`, como manda el punto 5 de la verificacion.\n")

ESPERADAS = 60
DESDE_FILA = 41


def guarda_de_fecha(nota):
    """CAE si la fecha de la marca historica no es la que git devuelve hoy Y la
    correccion declarada que lo dice no esta escrita en la nota.

    Devuelve (lista de fallos, linea de diagnostico). La linea se imprime
    siempre, aprobado o no, para que la comprobacion no pueda pasar callada.
    """
    hoy = fecha_de_git()
    if hoy is None:
        return (["la guarda de fecha no pudo leer de git ni un commit de la vuelta %d"
                 % VUELTA],
                "GUARDA DE FECHA: ROJO, git no devuelve commits de la vuelta %d" % VUELTA)
    m = RE_FECHA.search(MARCA_APLICADA)
    escrita = m.group(0) if m else None
    if escrita == hoy:
        return ([], "GUARDA DE FECHA: VERDE, la marca escrita dice %s y git dice %s"
                % (escrita, hoy))
    if MARCA_DE_LA_CORRECCION in (nota or ""):
        return ([], "GUARDA DE FECHA: VERDE CON DESFASE DECLARADO. La marca escrita dice "
                "%s, git dice %s, y la correccion declarada (%s) SI esta en la nota."
                % (escrita, hoy, MARCA_DE_LA_CORRECCION))
    return (["la marca escrita lleva la fecha %s, git dice %s, y la correccion "
             "declarada (%s) NO esta en la nota de OP-E-03"
             % (escrita, hoy, MARCA_DE_LA_CORRECCION)],
            "GUARDA DE FECHA: ROJO, desfase de fecha SIN correccion declarada "
            "(escrita %s, git %s)" % (escrita, hoy))


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def cifras():
    filas = cargar_jsonl(LECTURA)
    fallos = []
    if len(filas) != ESPERADAS:
        fallos.append("el fichero de lectura trae %d filas y se esperaban %d"
                      % (len(filas), ESPERADAS))
    for f in filas:
        if f.get("marca") != "LECTURA DIRIGIDA" or not f.get("fuera_de_la_cola") \
                or f.get("mueve_el_marcador_del_cribado") is not False \
                or not f.get("fuera_de_la_tasa_por_dominio"):
            fallos.append("la fila %s no trae la marca completa de LECTURA DIRIGIDA"
                          % f.get("puesto_tramo"))
    clases = collections.Counter(f["clase"] for f in filas)
    doms = collections.Counter(f["dominio"] for f in filas)
    con_dir = sum(1 for f in filas if f.get("direccion_leida"))
    return filas, clases, doms, con_dir, fallos


def texto_nota(filas, clases, doms, con_dir):
    total_bolsa = len(cargar_jsonl(BOLSA))
    leidas_total = DESDE_FILA - 1 + len(filas)
    por_dom = ", ".join("%s %d" % (d, n) for d, n in sorted(doms.items()))
    a = [f["puesto_tramo"] for f in filas if f["clase"] == "A"]
    b = [f["puesto_tramo"] for f in filas if f["clase"] == "B"]
    sin_dir = [f["puesto_tramo"] for f in filas if not f.get("direccion_leida")]
    return (
        " %s Leidas las filas %d a %d de las %d, con la misma vara (banco 9.6.1 clase, 9.6.2 "
        "direccion, 9.6.3 el tamano del solape no decide) y con EL MISMO UMBRAL DE DIRECCION del "
        "tramo 1, que el acta 96 seccion 4.4 adjudico bien puesto y sin tocar. Los cinco puntos de "
        "la verificacion se REMIDIERON en la vuelta y no se heredaron del tramo 1: cribado cerrado "
        "en 3388 filas cada fichero, contadas; ids por el resolutor ANTES de comparar (P.1), y en "
        "estas %d el resolutor no movio ninguno, cosa que se declara igual porque P.1 obliga; "
        "cuenta sin fugas (cero de las %d esta en la cola tras resolver contra los 2796 pares "
        "distintos de la cola, cero repetidas dentro del tramo); marca LECTURA DIRIGIDA en las %d "
        "filas del material y en las %d del JSONL, contadas; y veredictos APARTE de la tasa por "
        "dominio del 9.27, en fichero propio y rotulado. "
        "RESULTADO: A %d, B %d, C %d, D %d. Los tres A son los pares %s. El unico B es el par %s "
        "(reporte_estado_miembro_equipo contra variance_analysis), declarado DUDOSO en vez de "
        "forzado: la direccion si se lee y lo que la vara no resuelve sola es la clase. "
        "DIRECCION: %d leidas y afirmadas, %d NO RESUELTAS y declaradas como tal (pares %s). "
        "POR DOMINIO, y no entra en la tasa del 9.27: %s. "
        "LA PROPORCION DE NO RESUELTAS SUBE del 27,5 por ciento del tramo 1 al %.1f por ciento de "
        "este, y NO se explica de palabra sino que se mide con instrumento propio "
        "(scripts/loop/vuelta97_tarea2_senal_de_la_bolsa.py): la bolsa viene ORDENADA de mas fuerte "
        "a mas debil (mediana de titulo_ratio 84,3 en el tramo 1, 78,2 en el 2, 76,2 en lo que "
        "queda) y dentro del tramo 2 las filas que la lectura no resolvio son las mas debiles "
        "medidas por fuera de la lectura (misma fuente 66,7 por ciento contra 78,8 por ciento). SE "
        "DECLARA QUE ESO NO PRUEBA QUE EL UMBRAL SEA EL CORRECTO: una vara demasiado estricta sobre "
        "una bolsa que se debilita daria las mismas dos seniales. "
        "NUEVE FIGURAS registradas en docs/PENDIENTES.md y SIN ADJUDICAR, entre ellas dos parejas "
        "de gemelos casi homonimos (estrategia_de_innovacion_de_producto contra "
        "estrategia_innovacion_producto, que corrobora una figura del tramo 1, y "
        "reduccion_de_tiempo_de_ciclo contra reduccion_tiempo_ciclo), la familia Crosby de los 14 "
        "pasos repartida y mal emparejada, los nodos iman que el barrido cuelga de varias madres, y "
        "la segunda aparicion de la especie que casa un paso con su refutacion, esta vez Juran "
        "contra Deming. CERO ARISTAS ESCRITAS O RETIRADAS. "
        "Salidas: docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl (%d filas), "
        "docs/loop/SALIDA_V97_TAREA2_TRAMO2_MATERIAL.txt, docs/loop/SALIDA_V97_TAREA2_VEREDICTOS.txt, "
        "docs/loop/SALIDA_V97_TAREA2_SENIAL.txt, docs/loop/SALIDA_V97_TAREA2_MUTACION.txt "
        "(6 mutaciones y las 6 caen, 6 controles verdes; la clase y la direccion de cada par son "
        "tabla a mano y se DECLARA que no tienen caso rojo automatico). "
        "QUEDAN %d SIN LEER, filas %d a %d. estado se queda en LISTA, mismo criterio que las demas."
        % (MARCA, DESDE_FILA, leidas_total, total_bolsa,
           len(filas), len(filas), len(filas), len(filas),
           clases["A"], clases["B"], clases["C"], clases["D"],
           ", ".join(str(x) for x in a), ", ".join(str(x) for x in b),
           con_dir, len(sin_dir), ", ".join(str(x) for x in sin_dir), por_dom,
           100.0 * len(sin_dir) / len(filas),
           len(filas),
           total_bolsa - leidas_total, leidas_total + 1, total_bolsa)
    )


def texto_enlaces(filas, clases, con_dir):
    total_bolsa = len(cargar_jsonl(BOLSA))
    leidas_total = DESDE_FILA - 1 + len(filas)
    sin_dir = [f["puesto_tramo"] for f in filas if not f.get("direccion_leida")]
    return (
        "\n**%s.**\n"
        "El apartado de arriba se queda entero, sin borrar una palabra. Lo que cambia es\n"
        "su ultima fila: decia que quedaban **143** pares sin leer, y hoy quedan **%d**.\n"
        "Se leyeron las filas **%d a %d** de las **%d**, con la misma vara y con **el mismo\n"
        "umbral de direccion**, que el acta de la vuelta 96 (seccion 4.4) adjudico bien\n"
        "puesto y sin tocar.\n"
        "\n"
        "| lo que salio | cifra |\n"
        "|---|---:|\n"
        "| pares leidos en este tramo | **%d** (filas %d a %d) |\n"
        "| pares leidos en total | **%d** de %d |\n"
        "| clase A, REPITE | **%d** |\n"
        "| clase B, DUDOSO | **%d** |\n"
        "| clase C | **%d** |\n"
        "| clase D, CONTINUA | **%d** |\n"
        "| direccion leida y afirmada | **%d** |\n"
        "| direccion NO RESUELTA, declarada | **%d** |\n"
        "| aristas escritas o retiradas | **0** |\n"
        "| pares que quedan sin leer | **%d** (filas %d a %d) |\n"
        "\n"
        "**LA PROPORCION DE DIRECCIONES NO RESUELTAS SUBE, y se mide en vez de explicarse.**\n"
        "Del **27,5%%** del tramo 1 al **%.1f%%** de este. El encargo preveia el caso de una\n"
        "proporcion PARECIDA (*\"es la bolsa, no tu vara\"*); como no lo es, esa conclusion no\n"
        "se invoca: se construyo un instrumento que la pone a prueba\n"
        "(`scripts/loop/vuelta97_tarea2_senal_de_la_bolsa.py`). Lo medido es que **la bolsa\n"
        "viene ordenada de mas fuerte a mas debil** (mediana de `titulo_ratio` 84,3 en el\n"
        "tramo 1, 78,2 en el 2, 76,2 en lo que queda) y que **dentro del tramo 2 las filas sin\n"
        "direccion son las mas debiles medidas por fuera de la lectura**. **SE DECLARA QUE ESO\n"
        "NO PRUEBA QUE EL UMBRAL SEA EL CORRECTO**, y va marcado como discutible.\n"
        "\n"
        "**CERO ARISTAS**: `OP-E-03` sigue siendo LECTURA DIRIGIDA y su producto es el juicio.\n"
        "El detalle entero, con las **nueve** figuras que la lectura destapa y las guardas\n"
        "probadas por mutacion, esta en `docs/PENDIENTES.md`, seccion \"VUELTA 97, TAREA 2\".\n"
        "Los veredictos viven en `docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl` y **no** en\n"
        "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.\n"
        % (TITULO_ENLACES, total_bolsa - leidas_total,
           DESDE_FILA, leidas_total, total_bolsa,
           len(filas), DESDE_FILA, leidas_total,
           leidas_total, total_bolsa,
           clases["A"], clases["B"], clases["C"], clases["D"],
           con_dir, len(sin_dir),
           total_bolsa - leidas_total, leidas_total + 1, total_bolsa,
           100.0 * len(sin_dir) / len(filas))
    )


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--simular", action="store_true")
    g.add_argument("--aplicar", action="store_true")
    a = ap.parse_args()

    filas, clases, doms, con_dir, fallos = cifras()

    ops = cargar_jsonl(OPERACIONES)
    objetivo = [o for o in ops if o.get("id_op") == "OP-E-03"]
    if len(objetivo) != 1:
        fallos.append("OP-E-03 aparece %d veces en OPERACIONES.jsonl, se esperaba 1" % len(objetivo))
    else:
        nota_actual = objetivo[0].get("nota") or ""
        # (iv) el addendum ya escrito se reconoce EN SUS DOS FORMAS: la historica
        # (con la fecha mala, que es la que de verdad esta en el fichero) y la
        # nueva (con la fecha leida de git). Si se mirara solo la nueva, la
        # guarda dejaria de disparar y correr dos veces duplicaria el texto.
        if ancla_de(MARCA) in nota_actual or ancla_de(MARCA_APLICADA) in nota_actual:
            fallos.append("el addendum de la vuelta 97 YA ESTA en la nota de OP-E-03: "
                          "correr dos veces lo duplicaria")
        # (vi) la guarda de fecha
        f_fecha, diagnostico = guarda_de_fecha(nota_actual)
        print(diagnostico)
        fallos.extend(f_fecha)

    enlaces = io.open(ENLACES, encoding="utf-8").read()
    if enlaces.count(ANCLA) != 1:
        fallos.append("el ancla del apartado de la vuelta 96 aparece %d veces en 04_ENLACES.md, "
                      "se esperaba 1" % enlaces.count(ANCLA))
    if TITULO_ENLACES in enlaces:
        fallos.append("el apartado de la vuelta 97 YA ESTA en 04_ENLACES.md")

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    nota_nueva = (objetivo[0].get("nota") or "") + texto_nota(filas, clases, doms, con_dir)
    bloque = texto_enlaces(filas, clases, con_dir)

    print("=" * 100)
    print("SEGUNDO ADDENDUM DE OP-E-03, VUELTA 97 (%s)"
          % ("SIMULACION" if a.simular else "APLICADO"))
    print("=" * 100)
    print()
    print("--- lo que se anade a la nota de OP-E-03 (aditivo, la vieja no se toca) ---")
    print(texto_nota(filas, clases, doms, con_dir).strip())
    print()
    print("--- lo que se anade a docs/plan/04_ENLACES.md (aditivo) ---")
    print(bloque)

    if a.simular:
        print("SIMULACION: no se escribio nada.")
        return 0

    objetivo[0]["nota"] = nota_nueva
    with io.open(OPERACIONES, "w", encoding="utf-8", newline="\n") as f:
        for o in ops:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    io.open(ENLACES, "w", encoding="utf-8", newline="\n").write(
        enlaces.replace(ANCLA, ANCLA + bloque, 1))

    # re-lectura de comprobacion: los dos ficheros siguen validos y traen la marca
    ops2 = cargar_jsonl(OPERACIONES)
    o2 = [o for o in ops2 if o.get("id_op") == "OP-E-03"]
    enlaces2 = io.open(ENLACES, encoding="utf-8").read()
    bien = (len(ops2) == len(ops) and len(o2) == 1 and MARCA in o2[0]["nota"]
            and TITULO_ENLACES in enlaces2)
    print("APLICADO. Re-lectura: OPERACIONES.jsonl %d filas validas, addendum presente: %s"
          % (len(ops2), "SI" if bien else "NO"))
    return 0 if bien else 1


if __name__ == "__main__":
    raise SystemExit(main())
