# -*- coding: utf-8 -*-
r"""vuelta164_tarea1_registrar_acta163.py . TAREA 1 de la vuelta 164.

REGISTRA EN LA FORMA DE LA CASA (`R.N`) EL ACTA 163 ENTERA: SUS DIEZ
ADJUDICACIONES (6.1 a 6.10) Y LA CAIDA PROPIA DEL AUDITOR de su seccion 4. La
caida del auditor se registra IGUAL que las del ejecutor, por letra del encargo
de la vuelta 164 (*"Mis caidas se registran igual que las tuyas"*).

HEREDA EL INSTRUMENTO DE LA VUELTA 163 (`vuelta163_tarea1a_registrar_acta162.py`)
Y ARREGLA DOS COSAS QUE ESE NO PODIA SABER, LAS DOS MEDIDAS Y NO SUPUESTAS:

  (1) LA SANGRIA. En el acta 162 las adjudicaciones abren en columna 0
      (`**6.1 ...`); en el acta 163 abren con TRES ESPACIOS de sangria
      (`   **6.1 ...`, `docs/loop/ACTA_AUDITOR.md:54293`, leida hoy). El patron
      del instrumento viejo estaba anclado a `^\*\*`, asi que sobre el acta 163
      habria encontrado CERO y habria parado. El patron nuevo admite sangria
      (`^\s*\*\*`) y sigue exigiendo que cada clave aparezca EXACTAMENTE UNA VEZ
      dentro del cuerpo acotado del acta 163.

  (2) LA SEDE, QUE EL ACTA 163 NO REPITE. El instrumento viejo leia la frase
      *"la sede por defecto es `docs/PENDIENTES.md`"* DENTRO del acta que
      registraba, y paraba si no estaba. El acta 163 NO la repite: contada hoy,
      esa frase aparece UNA sola vez en todo `docs/loop/ACTA_AUDITOR.md` y vive
      en el cuerpo del acta 162, que es donde la adjudicacion 6.3 de ESA acta la
      escribio. La regla es vigente y de la casa, no de un acta concreta, asi que
      este instrumento la busca en el fichero ENTERO, comprueba que aparece
      exactamente una vez, IMPRIME su linea, y ademas DECLARA que el acta 163 no
      la repite. Sigue sin suponer nada: si la frase desapareciera del fichero,
      para sin escribir.

NINGUNA CELDA SE TECLEA: el numero lo computa `serie_de_registros.py` leyendo
LAS DOS sedes; el titulo y la linea de cada adjudicacion y de la caida se LEEN
HOY del acta; el reparto por via se CUENTA del diccionario de vias.

LA GLOSA DE CADA UNA SI ES PROSA DEL EJECUTOR, y va marcada como tal.

ES IDEMPOTENTE Y LO COMPRUEBA SOBRE LAS DOS SEDES, por su TITULO SIN NUMERO.

USO:  python scripts/loop/vuelta164_tarea1_registrar_acta163.py
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402

RAIZ = SERIE.RAIZ
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
CABECERA_ACTA_163 = "# ACTA DEL AUDITOR, VUELTA 163"
TITULO_SIN_NUMERO = ("Registro de las diez adjudicaciones y la caida propia "
                     "del acta de la vuelta 163")

# ARREGLO (4) DE ESTA VUELTA, Y LO CAZO EL ARNES DE MUTACION EN SU PRIMERA
# CORRIDA, CON LA ENTRADA YA ESCRITA Y ANTES DE COMMITEAR NADA. La idempotencia
# se comprueba buscando `TITULO_SIN_NUMERO` en el titulo que devuelve
# `serie_de_registros.py`, y ese instrumento lee el titulo de la LINEA DEL `##`
# Y SOLO DE ESA LINEA. El instrumento heredado de la vuelta 163 escribia su
# cabecera PARTIDA en tres lineas, asi que el titulo que la serie ve queda
# TRUNCADO a lo que cupo en la primera ("... del acta de la", sin el "vuelta
# 162"), NUNCA contiene el literal completo, y la comprobacion de idempotencia
# NO PUEDE dar positiva jamas: correr el registrador dos veces escribe la
# entrada DOS VECES, con dos numeros distintos. Medido hoy: la primera corrida
# escribio `R.33` y la segunda, sobre la misma acta, escribio `R.34`. Se
# restauro `docs/PENDIENTES.md` a HEAD (`git checkout --`) antes de commitear
# nada, y la cabecera pasa a ser UNA SOLA LINEA para que la serie vea el titulo
# entero. La comprobacion, ademas, deja de fiarse: si la entrada esta escrita
# pero la serie no puede verla, esto PARA en vez de escribir encima.
MARCA_EN_LA_SEDE = "## R.%d. " + TITULO_SIN_NUMERO

# LA LINEA QUE FIJA LA SEDE. Se busca LITERAL en el fichero ENTERO (ver (2) de
# la cabecera): la regla la escribio la adjudicacion 6.3 del acta 162 y el acta
# 163 no la repite.
FRASE_DE_LA_SEDE = "la sede por defecto es `docs/PENDIENTES.md`"

# VIA DE EJECUCION DE CADA ADJUDICACION. La via se CUENTA de aqui para el
# resumen; la prosa del resumen no lleva ninguna cifra tecleada.
VIA = {
    "6.1": "EN EL PROCEDIMIENTO",
    "6.2": "EN EL PROCEDIMIENTO",
    "6.3": "SIN TOCAR NADA",
    "6.4": "EN EL REPORTE",
    "6.5": "EN EL REPORTE",
    "6.6": "EN CODIGO",
    "6.7": "EN EL REPORTE",
    "6.8": "EN CODIGO",
    "6.9": "EN MEDICION",
    "6.10": "SIN TOCAR NADA",
}

QUE_HACE_ESTA_VUELTA = {
    "6.1": ("EJECUTADA EN EL PROCEDIMIENTO DE ESTA MISMA VUELTA. La vuelta se abre como "
            "164, no como una 163 prorrogada, y ABSORBE la cola de la 163: su reporte "
            "cubre las dos vueltas y las salidas ya selladas de la 163 se CITAN en vez "
            "de re correrse. El invariante ACTA N VUELTA N MAS 1 queda intacto, que es "
            "de donde cuelgan `tallar_cabecera_reporte.py` y "
            "`verificar_apertura_sellada.py`."),
    "6.2": ("EJECUTADA EN EL PROCEDIMIENTO, Y MEDIDA. La cola sin commitear de la 163 "
            "(la bateria nueva, las tres `SALIDA_V135_2E_MUTACION` re selladas y los "
            "ficheros sin versionar) entro en el MISMO commit que los diez "
            "`SALIDA_V164_*_APERTURA.txt`, primer commit del corredor e hijo directo "
            "del acta 163, sin fragmentar el bloque. La guarda "
            "`verificar_apertura_sellada.py --vuelta 164` sale VERDE sobre esa "
            "estructura."),
    "6.3": ("EJECUTADA SIN TOCAR NADA, Y ACATADA EN LA TAREA 3. El cruce de entregables "
            "queda como CORROBORADOR y no como decisor de `P.5.1`, asi que el veredicto "
            "de la `LD-OPC05-101` NO se decide con el, ni a favor ni en contra. La vara "
            "congelada no se estrecha."),
    "6.4": ("EJECUTADA EN EL REPORTE, TAREA 3 de esta vuelta. El veredicto de la "
            "`LD-OPC05-101` deja de vivir en el asunto del commit `1fa1bac9` y se "
            "publica en `docs/loop/REPORTE.md` con la letra de `P.5.1` delante, "
            "nombrando que parte de la frase y que ejemplar lo sostienen, y "
            "respondiendo punto por punto al caso de la seccion 3.2 del acta."),
    "6.5": ("EJECUTADA EN EL REPORTE, TAREA 4 de esta vuelta. La `LD-OPC05-005` se relee "
            "conjunta contra los dos nodos enteros del grafo con `P.5.1` y sus cuatro "
            "ejemplares delante. Si la clase se sostiene, la caida es del auditor y la "
            "firma el; si se mueve, va con correccion declarada y recomputo."),
    "6.6": ("EJECUTADA EN CODIGO, TAREA 2.c de esta vuelta. Los casos `F_hoy_*` y "
            "`G_mismo_exit` del arnes de la 4.b dejan de leer el arbol de trabajo vivo y "
            "pasan a computarse como DELTA sobre un sujeto fabricado, igual que se hizo "
            "con `160_6b` y con `162_1a`. La guarda `verificar_re_sellado.py` NO se "
            "toca."),
    "6.7": ("EJECUTADA EN EL REPORTE, TAREA 2.b de esta vuelta. Las tres "
            "`SALIDA_V135_2E_MUTACION` van nombradas con su `numstat` medido y su "
            "motivo, aunque el camino nuevo de la guarda ya no las vea desde la apertura "
            "de la 164. No se prohibe re sellar: se prohibe re sellar en silencio."),
    "6.8": ("EJECUTADA EN CODIGO, TAREA 2.a de esta vuelta. La bateria corre entera y "
            "publica el tiempo TOTAL y el de CADA arnes. La nomina NO se recorta para "
            "que corra antes, ningun arnes entra en verde alegado y ninguno se borra."),
    "6.9": ("EJECUTADA COMO MEDICION Y SOLO COMO MEDICION, TAREA 5 de esta vuelta. Los "
            "arneses de mutacion anteriores a la vuelta 148 que estan fuera de la nomina "
            "se corren y se publica cuantos dan exit 0 y cuantos rojo, con su nomina "
            "entera y su cronometro. NINGUNO entra en la bateria: con la cifra delante "
            "se decide, que es lo que la 6.7 del acta 156 hizo con las nueve salidas de "
            "la P3b."),
    "6.10": ("EJECUTADA SIN TOCAR NADA, Y A PROPOSITO. La `M` de "
             "`dataset/metadata/master_graph.json` es fin de linea y no contenido: "
             "recomputado hoy en la apertura, `git diff HEAD --numstat -- dataset/ web/ "
             "engine/` da CERO FILAS. No se arregla y no se commitea sola. Queda escrito "
             "para que no se herede como susto."),
}

QUE_HACE_CON_LA_CAIDA = {
    "CAIDA 1": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL EJECUTOR, "
                "porque no es suya. Su remedio ya esta aplicado y lo aplico la propia "
                "TAREA 1.c de la vuelta 163: la cifra contable del tramo se lee del "
                "registro y son DOS lecturas ciegas del auditor (`005` y `100`), no "
                "cuatro; `094`, `101` y `118` llevan `TRAMO_AL_DOBLE`, que es la segunda "
                "pasada del propio ejecutor. La 1.c midio, publico la diferencia y NO "
                "escribio marcas para no mover la cifra de `P.5.2`, que es lo correcto."),
}


def cuerpo_del_acta_163():
    """El texto del acta 163, acotado por su cabecera y por el final del fichero
    o la cabecera siguiente. Hace falta acotar: el fichero trae mas de un `6.1`
    y mas de una `CAIDA 1`."""
    texto = io.open(ACTA, encoding="utf-8").read()
    lineas = texto.split("\n")
    inicios = [i for i, l in enumerate(lineas, 1) if l.startswith(CABECERA_ACTA_163)]
    if len(inicios) != 1:
        raise SystemExit("ROJO: la cabecera del acta 163 aparece %d veces." % len(inicios))
    inicio = inicios[0]
    siguientes = [i for i, l in enumerate(lineas, 1)
                  if i > inicio and re.match(r"^# ACTA (DE LA VUELTA|DEL AUDITOR)", l)]
    fin = min(siguientes) - 1 if siguientes else len(lineas)
    return lineas, inicio, fin


def titulo_de_la_negrita(lineas, inicio, fin, patron, etiqueta):
    """EL TITULO ES LA NEGRITA DE APERTURA, NI UNA PALABRA MAS: se acumulan
    lineas hasta que la negrita CIERRA. Copiar la linea entera etiquetaria como
    'titulo literal' un trozo del CUERPO de la entrada.

    ARREGLO (3) DE ESTA VUELTA, Y LO CAZO EL PROPIO ARNES DE MUTACION DE ESTA
    TAREA ANTES DE PUBLICAR NADA. La version heredada de
    `vuelta163_tarea1a_registrar_acta162.py` acumulaba HASTA EL FINAL DEL ACTA
    buscando el `**` de cierre, sin ninguna frontera. Su camino de PARADA "la
    negrita no cierra" era, por eso, INALCANZABLE en cualquier documento donde
    despues venga otra negrita: al no cerrar la suya, la funcion seguia leyendo
    y se comia el `**` de APERTURA de la entrada siguiente, devolviendo como
    "titulo literal" un texto que mezcla dos entradas y saliendo en VERDE. Es la
    especie de la casa: una guarda cuyo rojo no puede dispararse.

    LA FRONTERA QUE SE PONE, Y POR QUE ESA: la LINEA EN BLANCO. Un titulo de
    acta no atraviesa un parrafo, y en el acta 163 leida hoy las diez
    adjudicaciones y la caida cierran su negrita dentro de su propio parrafo
    (medido: las once se leen con esta funcion y ninguna para). Si la negrita no
    cierra antes del parrafo, se PARA en vez de invadir la entrada siguiente.
    """
    aciertos = [i for i in range(inicio, fin + 1) if patron.match(lineas[i - 1])]
    if len(aciertos) != 1:
        return None, "PARADA: %s aparece %d veces dentro del acta 163." % (
            etiqueta, len(aciertos))
    ln = aciertos[0]
    acumulado = ""
    j = ln - 1
    cierre = -1
    while j < fin:
        trozo = lineas[j].strip()
        if not trozo and acumulado:
            break            # frontera de parrafo: la negrita tenia que cerrar antes
        acumulado = (acumulado + " " + trozo).strip() if acumulado else trozo
        cierre = acumulado.find("**", 2)
        if cierre >= 0:
            break
        j += 1
    if cierre < 0:
        return None, ("PARADA: la negrita de %s no cierra dentro de su parrafo."
                      % etiqueta)
    return (ln, re.sub(r"\s+", " ", acumulado[2:cierre]).strip()), None


def main():
    print("=" * 78)
    print("VUELTA 164, TAREA 1: EL ACTA 163 ENTERA, REGISTRADA EN LA FORMA DE LA CASA")
    print("=" * 78)
    print("")

    serie = SERIE.entradas()
    print("A) LA SERIE, RECOMPUTADA DE SUS DOS SEDES ANTES DE ESCRIBIR")
    for numero, rel, linea, titulo in serie:
        print("   R.%-3d %s:%-6d %s" % (numero, rel, linea, titulo[:88]))
    cols = SERIE.colisiones(serie)
    print("   CIFRA entradas: %d" % len(serie))
    print("   CIFRA colisiones: %d" % len(cols))
    print("   CIFRA huecos: %d" % len(SERIE.huecos(serie)))
    if cols:
        print("   PARADA: la serie trae colisiones. No se escribe encima de eso.")
        return 1
    ya = [(n, rel, ln) for n, rel, ln, t in serie if TITULO_SIN_NUMERO in t]
    if ya:
        n, rel, ln = ya[0]
        print("YA ESTABA: la entrada vive como R.%d en %s:%d. No se toca." % (n, rel, ln))
        print("CIFRA entradas escritas: 0")
        return 0
    # LA IDEMPOTENCIA NO SE FIA DE SI MISMA (arreglo (4)). Si el titulo esta
    # escrito EN EL FICHERO pero la serie no lo ve, la comprobacion de arriba es
    # ciega y escribir seria duplicar. Se PARA y se dice cual es la sede.
    for rel in ("docs/PENDIENTES.md", "docs/plan/CORRECCIONES_A_APLICAR.md"):
        ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.exists(ruta):
            continue
        if TITULO_SIN_NUMERO in io.open(ruta, encoding="utf-8").read():
            print("   PARADA: el titulo YA ESTA ESCRITO en %s pero la serie no lo ve."
                  % rel)
            print("   La cabecera tiene que caber en la linea del '##' o la")
            print("   idempotencia es ciega. No se escribe encima de eso.")
            return 1
    numero = SERIE.siguiente_libre(serie)
    print("   SIGUIENTE LIBRE, computado y no tecleado: R.%d" % numero)
    print("")

    lineas, inicio, fin = cuerpo_del_acta_163()
    print("B) LA SEDE, LEIDA DE LA REGLA ESCRITA Y NO SUPUESTA")
    print("   acta 163: docs/loop/ACTA_AUDITOR.md, lineas %d a %d" % (inicio, fin))
    todas = [i for i, l in enumerate(lineas, 1) if FRASE_DE_LA_SEDE in l]
    dentro = [i for i in todas if inicio <= i <= fin]
    print("   CIFRA veces que la frase de la sede aparece en el fichero entero: %d"
          % len(todas))
    print("   CIFRA veces que aparece DENTRO del acta 163: %d" % len(dentro))
    if len(todas) != 1:
        print("   PARADA: la frase de la sede no aparece exactamente una vez.")
        return 1
    print("   DECLARADO: el acta 163 NO repite la frase; la regla vive en la")
    print("   adjudicacion 6.3 del acta 162 y es de la casa, no de un acta.")
    print("   docs/loop/ACTA_AUDITOR.md:%d dice hoy: %s"
          % (todas[0], lineas[todas[0] - 1].strip()))
    sede_rel = "docs/PENDIENTES.md"
    por_sede = {}
    for n, rel, _l, _t in serie:
        por_sede.setdefault(rel, []).append(n)
    for rel in sorted(por_sede):
        print("   CIFRA entradas en %s: %d" % (rel, len(por_sede[rel])))
    if sede_rel not in por_sede:
        print("   PARADA: la sede que manda la 6.3 no tiene ninguna entrada de la serie.")
        return 1
    print("   SEDE: %s (la que la 6.3 del acta 162 fija por defecto)" % sede_rel)
    sede = os.path.join(RAIZ, sede_rel.replace("/", os.sep))
    print("")

    print("C) LAS DIEZ ADJUDICACIONES, LEIDAS HOY DE SU LINEA EN EL ACTA 163")
    adjudicaciones = []
    for k in range(1, 11):
        clave = "6.%d" % k
        patron = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        hallado, error = titulo_de_la_negrita(
            lineas, inicio, fin, patron, "la adjudicacion %s" % clave)
        if error:
            print("   " + error)
            return 1
        ln, titulo = hallado
        titulo = re.sub(r"^%s " % re.escape(clave), "", titulo).strip()
        adjudicaciones.append((clave, ln, titulo))
        print("   %-5s docs/loop/ACTA_AUDITOR.md:%d" % (clave, ln))
        print("      %s" % titulo[:150])
    print("   CIFRA adjudicaciones leidas: %d" % len(adjudicaciones))
    if len(adjudicaciones) != 10:
        print("   PARADA: se esperaban 10.")
        return 1
    print("")

    print("D) LA CAIDA PROPIA DEL AUDITOR, LEIDA HOY DE LA SECCION 4")
    caidas = []
    for k in range(1, 2):
        clave = "CAIDA %d" % k
        patron = re.compile(r"^\s*\*\*%s[,.]" % re.escape(clave))
        hallado, error = titulo_de_la_negrita(
            lineas, inicio, fin, patron, "la %s" % clave)
        if error:
            print("   " + error)
            return 1
        ln, titulo = hallado
        caidas.append((clave, ln, titulo))
        print("   %-8s docs/loop/ACTA_AUDITOR.md:%d" % (clave, ln))
        print("      %s" % titulo[:150])
    otras = [i for i in range(inicio, fin + 1)
             if re.match(r"^\s*\*\*CAIDA \d[,.]", lineas[i - 1])]
    print("   CIFRA caidas leidas: %d" % len(caidas))
    print("   CIFRA negritas 'CAIDA n' que hay en el acta 163: %d" % len(otras))
    if len(caidas) != 1 or len(otras) != 1:
        print("   PARADA: se esperaba exactamente UNA caida propia del auditor.")
        return 1
    print("")

    print("E) EL REPARTO POR VIA, CONTADO Y NO TECLEADO")
    reparto = {}
    for clave, _ln, _t in adjudicaciones:
        reparto.setdefault(VIA[clave], []).append(clave)
    for via in sorted(reparto):
        print("   CIFRA %s: %d (%s)" % (via, len(reparto[via]), ", ".join(reparto[via])))
    print("")

    bloques = []
    for clave, ln, titulo in adjudicaciones:
        bloques.append(
            "  - **%s (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). VIA: %s.** Titulo\n"
            "    literal del acta: *\"%s\"*\n"
            "    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s\n"
            % (clave, ln, VIA[clave], titulo, QUE_HACE_ESTA_VUELTA[clave]))

    bloques_caidas = []
    for clave, ln, titulo in caidas:
        bloques_caidas.append(
            "  - **%s (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy).** Titulo literal del\n"
            "    acta: *\"%s\"*\n"
            "    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s\n"
            % (clave, ln, titulo, QUE_HACE_CON_LA_CAIDA[clave]))

    linea_reparto = "; ".join(
        "%s: %d (%s)" % (via, len(reparto[via]), ", ".join(reparto[via]))
        for via in sorted(reparto))

    texto = (
        "\n"
        "---\n"
        "\n"
        "## R.%d. Registro de las diez adjudicaciones y la caida propia del acta de la vuelta 163\n"
        "\n"
        "(Acta del auditor, vuelta 163, secciones 4 y 6; escrito en la vuelta 164,\n"
        "TAREA 1.)\n"
        "\n"
        "Por adicion, como `R.21` a `R.32`. **Corte de todas las cifras de esta entrada:\n"
        "3 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa\n"
        "`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes. La\n"
        "SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, leida hoy en\n"
        "`docs/loop/ACTA_AUDITOR.md:%d`, y se DECLARA que el acta 163 no la repite (la\n"
        "regla es de la casa, no de un acta suelta). Salida:\n"
        "`docs/loop/SALIDA_V164_T1_REGISTRO_ACTA_163.txt`.\n"
        "\n"
        "**LAS DIEZ ADJUDICACIONES, CON SU LINEA EN EL ACTA LEIDA HOY.** El titulo de\n"
        "cada una es LITERAL del fichero (localizado dentro del cuerpo del acta 163, no\n"
        "de cualquier acta); la glosa que sigue es prosa del ejecutor y va marcada como\n"
        "tal.\n"
        "\n"
        "%s"
        "\n"
        "**EL REPARTO POR VIA, CONTADO Y NO TECLEADO:** %s.\n"
        "**Ninguna de las diez sube al fundador.**\n"
        "\n"
        "**LA CAIDA PROPIA DEL AUDITOR, REGISTRADA IGUAL QUE LAS DEL EJECUTOR** (letra\n"
        "del encargo de la vuelta 164, TAREA 1: *\"Mis caidas se registran igual que las\n"
        "tuyas\"*). No es del ejecutor y no acumula para sus rachas; se escribe aqui\n"
        "porque el registro de la casa no distingue de quien es la mano que cae.\n"
        "\n"
        "%s"
        "\n"
        "**LO QUE ESTE REGISTRO NO CIERRA.** La vara `P.5.1` sigue CONGELADA y ninguna de\n"
        "estas diez la estrecha ni la ensancha. Los veredictos de la `LD-OPC05-101` (6.4)\n"
        "y de la `LD-OPC05-005` (6.5) NO se resuelven aqui: van por su cuenta en las\n"
        "TAREAS 3 y 4 de la vuelta 164, y si mueven una clase publicada lo haran con\n"
        "correccion declarada y recomputo, en su propia entrada.\n"
        % (numero, todas[0], "".join(bloques), linea_reparto, "".join(bloques_caidas))
    )

    with io.open(sede, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)

    print("F) LA ESCRITURA")
    print("   R.%d anadida al final de %s, por adicion pura" % (numero, sede_rel))
    r = subprocess.run(["git", "diff", "--numstat", "--", sede_rel],
                       cwd=RAIZ, capture_output=True, text=True)
    print("   git diff --numstat: %s" % r.stdout.strip())
    print("")

    despues = SERIE.entradas()
    print("G) LA SERIE, RECOMPUTADA DESPUES")
    print("   CIFRA entradas: %d" % len(despues))
    print("   CIFRA colisiones: %d" % len(SERIE.colisiones(despues)))
    print("   CIFRA huecos: %d" % len(SERIE.huecos(despues)))
    print("   SIGUIENTE LIBRE: R.%d" % SERIE.siguiente_libre(despues))
    if SERIE.colisiones(despues):
        print("ROJO: la escritura creo una colision.")
        return 1
    print("")
    print("VERDE: el acta 163 queda registrada como R.%d en %s." % (numero, sede_rel))
    print("CIFRA entradas escritas: 1")
    print("CIFRA adjudicaciones registradas: %d" % len(adjudicaciones))
    print("CIFRA caidas del auditor registradas: %d" % len(caidas))
    return 0


# ---------------------------------------------------------------------------
# CASO POSITIVO POR MUTACION (EJECUTOR.md regla 1, "EL CASO ROJO SE PRUEBA POR
# MUTACION"). Se corre con `--mutar` y con el arnes de nombre propio
# `vuelta164_tarea1_mutacion_registro.py`, que es el que la bateria ve.
#
# CERO ESCRITURAS Y CERO FICHEROS: las actas de mentira se fabrican EN MEMORIA
# como listas de lineas, y las series de mentira como listas de tuplas. Nada
# toca `docs/PENDIENTES.md` ni `docs/loop/ACTA_AUDITOR.md`.
#
# LOS ESPERADOS QUE PUEDEN CADUCAR SON DELTAS, no estados clavados (la medicina
# de `162_1a`): el numero libre se mide como "cuanto lo mueve anadir una
# entrada", no como "vale R.33".
# ---------------------------------------------------------------------------

FRONTERA_FALSA = "# ACTA DEL AUDITOR, VUELTA 164 (frontera de mentira)"
CABECERA_FALSA = CABECERA_ACTA_163 + " (fabricada por la prueba de mutacion)"


def _acta_fabricada(sangria="   ", duplicar=None, quitar=None, sin_cierre=False,
                    dos_caidas=False):
    """Un acta 163 DE MENTIRA, en memoria. Devuelve (lineas, inicio, fin)."""
    L = ["ruido de otra acta",
         "**6.1 ESTA NO CUENTA, VIVE FUERA DEL CUERPO.** ruido",
         "",
         CABECERA_FALSA,
         "cuerpo cualquiera",
         "",
         "**CAIDA 1, TITULO DE LA CAIDA FABRICADA.** cuerpo de la caida",
         ""]
    if dos_caidas:
        L.append("**CAIDA 2, OTRA CAIDA FABRICADA.** cuerpo")
        L.append("")
    L.append("## 6. ADJUDICACIONES")
    L.append("")
    for k in range(1, 11):
        clave = "6.%d" % k
        if quitar == clave:
            continue
        for _ in range(2 if duplicar == clave else 1):
            if k == 4:
                # UNA NEGRITA QUE ABARCA DOS LINEAS, para probar que el titulo
                # se acumula hasta el cierre y NO se traga el cuerpo.
                L.append("%s**%s TITULO CUATRO QUE SIGUE" % (sangria, clave))
                L.append("EN LA LINEA DE ABAJO.** cuerpo que NO es titulo")
            elif k == 9 and sin_cierre:
                L.append("%s**%s TITULO NUEVE QUE NUNCA CIERRA" % (sangria, clave))
            else:
                L.append("%s**%s TITULO %d.** cuerpo de la adjudicacion"
                         % (sangria, clave, k))
            L.append("")
    L.append(FRONTERA_FALSA)
    L.append("")
    L.append("**6.1 ESTA TAMPOCO CUENTA.** ruido de despues")
    return L, L.index(CABECERA_FALSA) + 1, L.index(FRONTERA_FALSA)


def _titulo_de_la_negrita_VIEJA(lineas, inicio, fin, patron, etiqueta):
    """LA VERSION HEREDADA, COPIADA DE `vuelta163_tarea1a_registrar_acta162.py`
    ANTES DE TOCAR NADA, sin cambiarle una linea de logica. Existe SOLO para que
    la prueba pueda medir el defecto en vez de afirmarlo: se corre la vieja y la
    nueva sobre el MISMO sujeto y se publica lo que devuelve cada una. No la
    llama nadie mas."""
    aciertos = [i for i in range(inicio, fin + 1) if patron.match(lineas[i - 1])]
    if len(aciertos) != 1:
        return None, "PARADA: %s aparece %d veces dentro del acta 163." % (
            etiqueta, len(aciertos))
    ln = aciertos[0]
    acumulado = ""
    j = ln - 1
    cierre = -1
    while j < fin:
        trozo = lineas[j].strip()
        acumulado = (acumulado + " " + trozo).strip() if acumulado else trozo
        cierre = acumulado.find("**", 2)
        if cierre >= 0:
            break
        j += 1
    if cierre < 0:
        return None, "PARADA: la negrita de %s no cierra dentro del acta." % etiqueta
    return (ln, re.sub(r"\s+", " ", acumulado[2:cierre]).strip()), None


def _cuantas_ve(lineas, inicio, fin, plantilla):
    """Cuantas de las diez claves encuentra EXACTAMENTE UNA VEZ un patron dado."""
    vistas = 0
    for k in range(1, 11):
        pat = re.compile(plantilla % re.escape("6.%d" % k))
        if len([i for i in range(inicio, fin + 1) if pat.match(lineas[i - 1])]) == 1:
            vistas += 1
    return vistas


def prueba_de_mutacion():
    print("=" * 78)
    print("VUELTA 164, TAREA 1: CASO POSITIVO POR MUTACION DEL REGISTRADOR DEL ACTA 163")
    print("=" * 78)
    print("")
    casos = []

    # --- BLOQUE A: LA SANGRIA, QUE ES EL ARREGLO (1) DE ESTE INSTRUMENTO ---
    L, ini, fin = _acta_fabricada(sangria="   ")
    casos.append(("A_patron_nuevo_ve_las_diez_con_sangria",
                  _cuantas_ve(L, ini, fin, r"^\s*\*\*%s "), 10))
    casos.append(("A_patron_viejo_ve_cero_con_sangria",
                  _cuantas_ve(L, ini, fin, r"^\*\*%s "), 0))
    L0, ini0, fin0 = _acta_fabricada(sangria="")
    casos.append(("A_patron_nuevo_ve_las_diez_sin_sangria",
                  _cuantas_ve(L0, ini0, fin0, r"^\s*\*\*%s "), 10))
    casos.append(("A_el_patron_no_confunde_6_1_con_6_10",
                  len([i for i in range(ini, fin + 1)
                       if re.match(r"^\s*\*\*6\.1 ", L[i - 1])]), 1))

    # --- BLOQUE B: EL TITULO ES LA NEGRITA, NI UNA PALABRA MAS ---
    hallado, err = titulo_de_la_negrita(L, ini, fin, re.compile(r"^\s*\*\*6\.4 "), "6.4")
    casos.append(("B_titulo_multilinea_se_acumula_hasta_el_cierre",
                  hallado[1] if hallado else None,
                  "6.4 TITULO CUATRO QUE SIGUE EN LA LINEA DE ABAJO."))
    casos.append(("B_titulo_multilinea_no_se_traga_el_cuerpo",
                  "cuerpo que NO es titulo" in (hallado[1] if hallado else ""), False))
    casos.append(("B_titulo_multilinea_sin_error", err, None))

    # --- BLOQUE C: LOS TRES CAMINOS DE PARADA ---
    Ld, id_, fd = _acta_fabricada(duplicar="6.5")
    _h, e_dup = titulo_de_la_negrita(Ld, id_, fd, re.compile(r"^\s*\*\*6\.5 "), "6.5")
    casos.append(("C_duplicada_para", e_dup is not None, True))
    casos.append(("C_duplicada_dice_cuantas_veces", "2 veces" in (e_dup or ""), True))
    Lq, iq, fq = _acta_fabricada(quitar="6.7")
    _h, e_aus = titulo_de_la_negrita(Lq, iq, fq, re.compile(r"^\s*\*\*6\.7 "), "6.7")
    casos.append(("C_ausente_para", e_aus is not None, True))
    Ls, is_, fs = _acta_fabricada(sin_cierre=True)
    _h, e_sc = titulo_de_la_negrita(Ls, is_, fs, re.compile(r"^\s*\*\*6\.9 "), "6.9")
    casos.append(("C_negrita_sin_cierre_para", e_sc is not None, True))

    # --- BLOQUE C2: EL DEFECTO HEREDADO, MEDIDO Y NO AFIRMADO (arreglo (3)) ---
    # LA MISMA ACTA DE MENTIRA, SIN LINEAS EN BLANCO, que es como quedaria un
    # acta apretada: la funcion VIEJA no para y se traga la entrada siguiente;
    # la NUEVA tampoco tiene parrafo donde parar, asi que aqui las dos se
    # comportan igual. El caso que las separa es el de arriba, con parrafos.
    Lap, iap, fap = _acta_fabricada(sin_cierre=True)
    Lap = [l for l in Lap if l.strip() != ""]
    iap = Lap.index(CABECERA_FALSA) + 1
    fap = Lap.index(FRONTERA_FALSA)
    hv, ev = _titulo_de_la_negrita_VIEJA(
        Lap, iap, fap, re.compile(r"^\s*\*\*6\.9 "), "6.9")
    casos.append(("C2_la_VIEJA_no_para_sobre_un_acta_apretada", ev is None, True))
    # LA PRUEBA DE QUE EL CIERRE QUE LA VIEJA USA NO ES SUYO: devuelve como
    # titulo el texto SIN CERRAR de la 6.9, porque tomo por delimitador de
    # cierre el `**` de APERTURA de la 6.10, que vive en la linea siguiente.
    casos.append(("C2_la_VIEJA_devuelve_titulo_en_vez_de_parar", hv is not None, True))
    casos.append(("C2_y_el_titulo_es_el_texto_SIN_CERRAR_de_la_6_9",
                  hv[1] if hv else None, "6.9 TITULO NUEVE QUE NUNCA CIERRA"))
    casos.append(("C2_o_sea_que_el_cierre_lo_tomo_prestado_de_la_6_10",
                  Lap[hv[0]].strip().startswith("**6.10 ") if hv else None, True))
    hv2, ev2 = _titulo_de_la_negrita_VIEJA(
        Ls, is_, fs, re.compile(r"^\s*\*\*6\.9 "), "6.9")
    casos.append(("C2_la_VIEJA_tampoco_para_con_parrafos", ev2 is None, True))
    casos.append(("C2_y_la_NUEVA_si_para_sobre_lo_mismo", e_sc is not None, True))
    casos.append(("C2_las_dos_coinciden_donde_la_negrita_SI_cierra",
                  _titulo_de_la_negrita_VIEJA(
                      L, ini, fin, re.compile(r"^\s*\*\*6\.4 "), "6.4")[0][1]
                  == titulo_de_la_negrita(
                      L, ini, fin, re.compile(r"^\s*\*\*6\.4 "), "6.4")[0][1], True))

    # --- BLOQUE D: LA CAIDA DEL AUDITOR, Y EL ACOTADO QUE LA CUENTA ---
    pat_caida = re.compile(r"^\s*\*\*CAIDA \d[,.]")
    casos.append(("D_una_caida_se_ve_una_vez",
                  len([i for i in range(ini, fin + 1) if pat_caida.match(L[i - 1])]), 1))
    L2, i2, f2 = _acta_fabricada(dos_caidas=True)
    casos.append(("D_dos_caidas_se_ven_las_dos",
                  len([i for i in range(i2, f2 + 1) if pat_caida.match(L2[i - 1])]), 2))
    casos.append(("D_el_acotado_deja_fuera_el_ruido_de_otras_actas",
                  _cuantas_ve(L, 1, len(L), r"^\s*\*\*%s "), 9))

    # --- BLOQUE E: EL ACTA DE VERDAD, LEIDA HOY ---
    RL, ri, rf = cuerpo_del_acta_163()
    casos.append(("E_el_acta_163_trae_las_diez_adjudicaciones",
                  _cuantas_ve(RL, ri, rf, r"^\s*\*\*%s "), 10))
    casos.append(("E_el_acta_163_trae_una_sola_caida",
                  len([i for i in range(ri, rf + 1) if pat_caida.match(RL[i - 1])]), 1))
    todas = [i for i, l in enumerate(RL, 1) if FRASE_DE_LA_SEDE in l]
    casos.append(("E_la_frase_de_la_sede_esta_una_vez_en_el_fichero", len(todas), 1))
    casos.append(("E_y_cero_veces_dentro_del_acta_163",
                  len([i for i in todas if ri <= i <= rf]), 0))
    # LAS ONCE NEGRITAS DEL ACTA DE VERDAD, LEIDAS CON LA FUNCION ARREGLADA: si
    # el arreglo (3) hubiera cambiado alguna lectura real, aqui saldria.
    patrones = [(re.compile(r"^\s*\*\*6\.%d " % k), "6.%d" % k) for k in range(1, 11)]
    patrones.append((re.compile(r"^\s*\*\*CAIDA 1[,.]"), "CAIDA 1"))
    leidos, sin_error = [], 0
    for pat, et in patrones:
        h, e = titulo_de_la_negrita(RL, ri, rf, pat, et)
        if e is None:
            sin_error += 1
            # El mismo despojo del prefijo que hace main(): la clave `6.N` no es
            # parte del titulo, y en la caida no hay prefijo que quitar.
            leidos.append(re.sub(r"^%s " % re.escape(et), "", h[1]).strip())
    casos.append(("E_las_once_negritas_se_leen_sin_error", sin_error, 11))
    escrito = io.open(os.path.join(RAIZ, "docs", "PENDIENTES.md"),
                      encoding="utf-8").read()
    casos.append(("E_los_once_titulos_leidos_hoy_estan_en_PENDIENTES",
                  sum(1 for t in leidos if t in escrito), 11))

    # --- BLOQUE H: LA IDEMPOTENCIA CIEGA, QUE ES EL ARREGLO (4) ---
    # LA CABECERA TIENE QUE CABER EN LA LINEA DEL `##`, o la serie devuelve un
    # titulo TRUNCADO y la comprobacion de "ya estaba" no puede dar positiva.
    # Se mide sobre lo que `serie_de_registros.py` ve HOY, sin escribir nada.
    def _titulo_que_ve_la_serie(cabecera):
        m = re.match(r"^## R\.\d+\.\s*(.*)$", cabecera)
        return (m.group(1) if m else "").strip()
    apretada = "## R.99. " + TITULO_SIN_NUMERO
    partida = ("## R.99. Registro de las diez adjudicaciones y la caida propia "
               "del acta de la")
    casos.append(("H_cabecera_de_una_linea_deja_ver_el_titulo_entero",
                  TITULO_SIN_NUMERO in _titulo_que_ve_la_serie(apretada), True))
    casos.append(("H_cabecera_partida_lo_trunca_y_la_idempotencia_queda_ciega",
                  TITULO_SIN_NUMERO in _titulo_que_ve_la_serie(partida), False))
    casos.append(("H_la_cabecera_que_ESTE_instrumento_escribe_es_de_una_linea",
                  TITULO_SIN_NUMERO in _titulo_que_ve_la_serie(
                      MARCA_EN_LA_SEDE % 99), True))
    # Y LA PRUEBA SOBRE EL FICHERO DE VERDAD: el titulo que la serie ve para la
    # entrada de esta vuelta contiene el literal completo.
    mia = [t for _n, _r, _l, t in SERIE.entradas() if TITULO_SIN_NUMERO in t]
    casos.append(("H_la_serie_de_hoy_ve_la_entrada_de_esta_vuelta", len(mia), 1))

    # --- BLOQUE F: EL NUMERO NO SE TECLEA, Y SE MIDE COMO DELTA ---
    base = [(n, "docs/PENDIENTES.md", 10 * n, "titulo %d" % n) for n in range(1, 6)]
    mas_una = base + [(6, "docs/PENDIENTES.md", 60, "titulo 6")]
    casos.append(("F_anadir_una_mueve_el_libre_exactamente_uno",
                  SERIE.siguiente_libre(mas_una) - SERIE.siguiente_libre(base), 1))
    con_hueco = [(1, "s", 1, "t"), (2, "s", 2, "t"), (4, "s", 4, "t")]
    casos.append(("F_un_hueco_no_rellena_el_libre", SERIE.siguiente_libre(con_hueco), 5))
    casos.append(("F_el_hueco_si_se_cuenta", len(SERIE.huecos(con_hueco)), 1))
    chocada = base + [(3, "docs/plan/CORRECCIONES_A_APLICAR.md", 99, "otra")]
    casos.append(("F_una_colision_se_ve", len(SERIE.colisiones(chocada)), 1))
    casos.append(("F_serie_vacia_empieza_en_uno", SERIE.siguiente_libre([]), 1))

    # --- BLOQUE G: EL REPARTO SE CUENTA, NO SE TECLEA ---
    reparto = {}
    for clave in VIA:
        reparto.setdefault(VIA[clave], []).append(clave)
    casos.append(("G_las_vias_reparten_las_diez",
                  sum(len(v) for v in reparto.values()), 10))
    casos.append(("G_toda_adjudicacion_tiene_via_y_glosa",
                  sorted(VIA) == sorted(QUE_HACE_ESTA_VUELTA), True))

    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("")
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")
    print("   SEGUNDA PASADA: SE MUTA EL VALOR ESPERADO Y TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif esperado is None:
            mutado = "UN ERROR QUE NO HAY"
        else:
            mutado = str(esperado) + "_MUTADO"
        cae = (real != mutado)
        print("   %-52s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    print("")
    print("   CIFRA casos que CAEN al mutarles el esperado: %d de %d"
          % (caen, len(casos)))
    print("")
    if fallos == 0 and caen == len(casos):
        print("VERDE: %d casos, los %d pasan y los %d CAEN al mutarles el esperado."
              % (len(casos), len(casos), len(casos)))
        return 0
    print("ROJO: %d fallan y %d no caen al mutarlos." % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if "--mutar" in sys.argv:
        raise SystemExit(prueba_de_mutacion())
    raise SystemExit(main())
