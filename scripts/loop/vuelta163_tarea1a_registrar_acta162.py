# -*- coding: utf-8 -*-
r"""vuelta163_tarea1a_registrar_acta162.py . TAREA 1.a de la vuelta 163.

REGISTRA EN LA FORMA DE LA CASA (`R.N`) EL ACTA 162 ENTERA: SUS DOCE
ADJUDICACIONES (6.1 a 6.12) Y LAS TRES CAIDAS PROPIAS DEL AUDITOR de su
seccion 2. Las caidas del auditor se registran IGUAL que las del ejecutor, por
letra del encargo de la vuelta 163.

LA SEDE NO SE SUPONE: la adjudicacion 6.3 del acta 162 la escribe con todas sus
letras (*"la sede por defecto es `docs/PENDIENTES.md`, y salir de ahi exige
remision escrita como la de la 150"*). Este instrumento LEE esa linea del acta
de hoy y PARA si no la encuentra, en vez de fiarse de la costumbre; y ademas
publica el reparto contado, que es lo que hace auditable la eleccion.

NINGUNA CELDA SE TECLEA:
  - EL NUMERO lo computa `scripts/loop/serie_de_registros.py` leyendo LAS DOS
    sedes (`siguiente_libre`);
  - EL TITULO Y LA LINEA de cada adjudicacion y de cada caida se LEEN HOY de
    `docs/loop/ACTA_AUDITOR.md`, acotando el cuerpo DEL ACTA 162 (el fichero
    trae mas de un `6.1` y mas de una `CAIDA 1`), y si alguna no aparece
    exactamente una vez, este script PARA sin escribir;
  - EL REPARTO por via de ejecucion se CUENTA del diccionario de vias, no se
    teclea en la prosa.

LA GLOSA DE CADA UNA SI ES PROSA DEL EJECUTOR, y va marcada como tal.

ES IDEMPOTENTE Y LO COMPRUEBA SOBRE LAS DOS SEDES, por su TITULO SIN NUMERO.

USO:  python scripts/loop/vuelta163_tarea1a_registrar_acta162.py
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
CABECERA_ACTA_162 = "# ACTA DEL AUDITOR, VUELTA 162"
TITULO_SIN_NUMERO = ("Registro de las doce adjudicaciones y las tres caidas propias "
                     "del acta de la vuelta 162")

# LA LINEA DE LA 6.3 QUE FIJA LA SEDE. Se busca LITERAL dentro del acta 162: si
# el auditor no la escribio, este instrumento no elige sede por costumbre.
FRASE_DE_LA_SEDE = "la sede por defecto es `docs/PENDIENTES.md`"

# VIA DE EJECUCION DE CADA ADJUDICACION. La via se CUENTA de aqui para el
# resumen; la prosa del resumen no lleva ninguna cifra tecleada.
VIA = {
    "6.1": "SIN TOCAR NADA",
    "6.2": "SIN TOCAR NADA",
    "6.3": "EN EL REGISTRO",
    "6.4": "SIN TOCAR NADA",
    "6.5": "SIN TOCAR NADA",
    "6.6": "EN CODIGO",
    "6.7": "EN CODIGO",
    "6.8": "EN CODIGO",
    "6.9": "SIN TOCAR NADA",
    "6.10": "SIN TOCAR NADA",
    "6.11": "EN CODIGO",
    "6.12": "SIN TOCAR NADA",
}

QUE_HACE_ESTA_VUELTA = {
    "6.1": ("EJECUTADA SIN TOCAR NADA EN LO YA HECHO. La seccion 11 del reporte de la "
            "vuelta 162 no era un incumplimiento: era la medicion correcta de un error "
            "del auditor. La vara de aceptacion queda CORREGIDA POR DECLARACION a "
            "CUATRO filas de fase, y es esa la que usa la TAREA 4.a de esta vuelta. La "
            "PREGUNTA 1 del reporte 162 queda CERRADA."),
    "6.2": ("EJECUTADA SIN TOCAR NADA. El discutible 1 y la PREGUNTA 2 del reporte 162 "
            "quedan adjudicados A FAVOR, con su frontera escrita en el acta: la "
            "exencion cubre UN solo commit, solo bajo la firma de parada y solo si el "
            "portador es unico. `scripts/loop/verificar_apertura_sellada.py` se queda "
            "como esta y esta vuelta no le toca una linea."),
    "6.3": ("EJECUTADA EN EL REGISTRO, Y ESTA MISMA ENTRADA ES SU CUMPLIMIENTO. La sede "
            "por defecto de la serie `R.N` es `docs/PENDIENTES.md`, y salir de ahi "
            "exige remision escrita como la de la vuelta 150. Este registro se escribe "
            "ahi por esa regla, no por costumbre, y el instrumento LEE la frase de la "
            "6.3 en el acta antes de elegir."),
    "6.4": ("EJECUTADA SIN TOCAR NADA. Las diez marcas derivadas de la TAREA 1.c de la "
            "vuelta 162 se quedan como estan, con su procedencia escrita dentro de la "
            "marca. El discutible 3 y la PREGUNTA 3 del reporte 162 quedan CERRADOS. La "
            "deuda se cierra hacia adelante y es del auditor: desde el acta 162 su "
            "ciega sella la letra CASO POR CASO."),
    "6.5": ("EJECUTADA SIN TOCAR NADA. La firma de parada sigue exigiendo que "
            "`docs/loop/PROMPT_SIGUIENTE.md` EXISTA Y ESTE VACIO, porque es lo que "
            "`AUDITOR.md` seccion 4 manda hacer. El discutible 4 del reporte 162 queda "
            "adjudicado EN CONTRA de ensanchar la guarda, y el error cae del lado "
            "seguro."),
    "6.6": ("EJECUTADA EN CODIGO, TAREA 4.a de esta vuelta. "
            "`scripts/loop/verificar_cifras_del_reporte.py` pasa a ROMPER cuando el "
            "reporte trae afirmaciones de cierre y coteja CERO, en prosa y en tabla. El "
            "AVISO que no tumba se queda tal cual. El PENDIENTE DE DOCTRINA 1 del "
            "reporte 162 queda CERRADO sin doctrina nueva."),
    "6.7": ("EJECUTADA EN CODIGO, TAREA 4.b de esta vuelta. "
            "`scripts/loop/verificar_re_sellado.py` mide ademas, contra el commit de "
            "apertura de la vuelta, TODA `docs/loop/SALIDA_*` MODIFICADA, y la que no "
            "este declarada en el reporte sale en ROJO con su nombre. El camino viejo "
            "no se toca."),
    "6.8": ("EJECUTADA EN CODIGO, TAREA 2 de esta vuelta y BLOQUEANTE. Los veintidos "
            "arneses de mutacion nacidos despues de la vuelta 147 entran en la nomina "
            "de `scripts/loop/verificar_mutaciones_viejas.py`, cada uno con su sujeto "
            "congelado o como CASO DECLARADO con su exit y su motivo MEDIDO. Y la "
            "guarda se mira a si misma: ROJO si algun arnes posterior a la ultima "
            "vuelta de su nomina se queda fuera."),
    "6.9": ("EJECUTADA SIN TOCAR NADA. `RELECTURA CIEGA DEL AUDITOR, VUELTA N` se queda "
            "en `FORMAS_QUE_CUENTAN`: `P.5.2` (1) define que cuenta por su CONTENIDO, "
            "no por una lista cerrada de literales. El discutible 6 del reporte 162 "
            "queda adjudicado a favor de lo hecho."),
    "6.10": ("EJECUTADA SIN TOCAR NADA. La tabla de excepciones de absorbidos sigue "
             "siendo POR OPERACION, y su caducidad ya esta resuelta por construccion: "
             "la entrada se cae sola si una de sus frases desaparece de la ficha. El "
             "discutible 7 y el PENDIENTE DE DOCTRINA 2 del reporte 162 quedan CERRADOS "
             "sin doctrina nueva."),
    "6.11": ("EJECUTADA EN CODIGO, TAREA 5.a de esta vuelta. "
             "`vuelta161_tarea1c_segunda_lectura.py` gana nombre estable POR REMISION, "
             "sin borrar el viejo y sin romper las citas de las actas, y la cifra de "
             "`P.5.2` sale IDENTICA antes y despues. El discutible 8 del reporte 162 "
             "queda adjudicado: reusar el instrumento fue correcto, el nombre era la "
             "deuda."),
    "6.12": ("EJECUTADA SIN TOCAR NADA, Y A PROPOSITO. `node_modules/` sigue sin "
             "versionar y sin ignorar, y esta vuelta NO lo commitea y NO toca "
             "`.gitignore`, que es alcance del fundador. Queda anotado y no dispara "
             "parada. La PREGUNTA 4 del reporte 162 queda CERRADA."),
}

QUE_HACE_CON_LA_CAIDA = {
    "CAIDA 1": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL EJECUTOR, "
                "porque no es suya. Su remedio ya esta aplicado: la vara de aceptacion "
                "de la TAREA 4.a de esta vuelta dice CUATRO, que es la cifra medida "
                "sobre el sujeto congelado, y no el OCHO recordado."),
    "CAIDA 2": ("SE REGISTRA CON SU NOMBRE Y SU REMEDIO ES LA TAREA 2 DE ESTA VUELTA, "
                "que es bloqueante. Un verde que cuenta 23 de 45 no es un verde: es un "
                "verde que no mira, y la guarda pasa a mirarse a si misma para que el "
                "linaje no pueda repetirse en silencio."),
    "CAIDA 3": ("SE REGISTRA CON SU NOMBRE AUNQUE NO LLEGO A PUBLICARSE, que es "
                "exactamente como se registran las del ejecutor cazadas antes del "
                "commit. La leccion es la de siempre: la definicion se LEE de la casa, "
                "no se inventa."),
}


def cuerpo_del_acta_162():
    """El texto del acta 162, acotado por su cabecera y por el final del fichero
    o la cabecera siguiente. Hace falta acotar: el fichero trae mas de un `6.1`
    y mas de una `CAIDA 1`."""
    texto = io.open(ACTA, encoding="utf-8").read()
    lineas = texto.split("\n")
    inicios = [i for i, l in enumerate(lineas, 1) if l.startswith(CABECERA_ACTA_162)]
    if len(inicios) != 1:
        raise SystemExit("ROJO: la cabecera del acta 162 aparece %d veces." % len(inicios))
    inicio = inicios[0]
    siguientes = [i for i, l in enumerate(lineas, 1)
                  if i > inicio and re.match(r"^# ACTA (DE LA VUELTA|DEL AUDITOR)", l)]
    fin = min(siguientes) - 1 if siguientes else len(lineas)
    return lineas, inicio, fin


def titulo_de_la_negrita(lineas, inicio, fin, patron, etiqueta):
    """EL TITULO ES LA NEGRITA DE APERTURA, NI UNA PALABRA MAS: se acumulan
    lineas hasta que la negrita CIERRA. Copiar la linea entera etiquetaria como
    'titulo literal' un trozo del CUERPO de la entrada."""
    aciertos = [i for i in range(inicio, fin + 1) if patron.match(lineas[i - 1])]
    if len(aciertos) != 1:
        return None, "PARADA: %s aparece %d veces dentro del acta 162." % (
            etiqueta, len(aciertos))
    ln = aciertos[0]
    acumulado = ""
    j = ln - 1
    cierre = -1
    while j < fin:
        acumulado = (acumulado + " " + lineas[j].strip()).strip() if acumulado \
            else lineas[j].strip()
        cierre = acumulado.find("**", 2)
        if cierre >= 0:
            break
        j += 1
    if cierre < 0:
        return None, "PARADA: la negrita de %s no cierra dentro del acta." % etiqueta
    return (ln, re.sub(r"\s+", " ", acumulado[2:cierre]).strip()), None


def main():
    print("=" * 78)
    print("VUELTA 163, TAREA 1.a: EL ACTA 162 ENTERA, REGISTRADA EN LA FORMA DE LA CASA")
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
    numero = SERIE.siguiente_libre(serie)
    print("   SIGUIENTE LIBRE, computado y no tecleado: R.%d" % numero)
    print("")

    lineas, inicio, fin = cuerpo_del_acta_162()
    print("B) LA SEDE, LEIDA DE LA ADJUDICACION 6.3 Y NO SUPUESTA")
    print("   acta 162: docs/loop/ACTA_AUDITOR.md, lineas %d a %d" % (inicio, fin))
    sedes_dichas = [i for i in range(inicio, fin + 1) if FRASE_DE_LA_SEDE in lineas[i - 1]]
    if len(sedes_dichas) != 1:
        print("   PARADA: la frase de la sede aparece %d veces en el acta 162."
              % len(sedes_dichas))
        return 1
    print("   docs/loop/ACTA_AUDITOR.md:%d dice hoy: %s"
          % (sedes_dichas[0], lineas[sedes_dichas[0] - 1].strip()))
    sede_rel = "docs/PENDIENTES.md"
    por_sede = {}
    for n, rel, _l, _t in serie:
        por_sede.setdefault(rel, []).append(n)
    for rel in sorted(por_sede):
        print("   CIFRA entradas en %s: %d" % (rel, len(por_sede[rel])))
    if sede_rel not in por_sede:
        print("   PARADA: la sede que manda la 6.3 no tiene ninguna entrada de la serie.")
        return 1
    print("   SEDE: %s (la que la 6.3 fija por defecto; salir de ahi exige remision)"
          % sede_rel)
    sede = os.path.join(RAIZ, sede_rel.replace("/", os.sep))
    print("")

    print("C) LAS DOCE ADJUDICACIONES, LEIDAS HOY DE SU LINEA EN EL ACTA 162")
    adjudicaciones = []
    for k in range(1, 13):
        clave = "6.%d" % k
        patron = re.compile(r"^\*\*%s " % re.escape(clave))
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
    if len(adjudicaciones) != 12:
        print("   PARADA: se esperaban 12.")
        return 1
    print("")

    print("D) LAS TRES CAIDAS PROPIAS DEL AUDITOR, LEIDAS HOY DE LA SECCION 2")
    caidas = []
    for k in range(1, 4):
        clave = "CAIDA %d" % k
        patron = re.compile(r"^\*\*%s[,.]" % re.escape(clave))
        hallado, error = titulo_de_la_negrita(
            lineas, inicio, fin, patron, "la %s" % clave)
        if error:
            print("   " + error)
            return 1
        ln, titulo = hallado
        caidas.append((clave, ln, titulo))
        print("   %-8s docs/loop/ACTA_AUDITOR.md:%d" % (clave, ln))
        print("      %s" % titulo[:150])
    print("   CIFRA caidas leidas: %d" % len(caidas))
    if len(caidas) != 3:
        print("   PARADA: se esperaban 3.")
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
        "## R.%d. Registro de las doce adjudicaciones y las tres caidas propias del acta\n"
        "de la vuelta 162 (acta del auditor, vuelta 162, secciones 2 y 6; escrito en la\n"
        "vuelta 163, TAREA 1.a)\n"
        "\n"
        "Por adicion, como `R.21` a `R.31`. **Corte de todas las cifras de esta entrada:\n"
        "3 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa\n"
        "`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes. La\n"
        "SEDE tampoco se supone: sale de la adjudicacion 6.3 del propio acta 162, leida\n"
        "hoy en `docs/loop/ACTA_AUDITOR.md:%d`. Salida:\n"
        "`docs/loop/SALIDA_V163_T1A_REGISTRO_ACTA_162.txt`.\n"
        "\n"
        "**LAS DOCE ADJUDICACIONES, CON SU LINEA EN EL ACTA LEIDA HOY.** El titulo de\n"
        "cada una es LITERAL del fichero (localizado dentro del cuerpo del acta 162, no\n"
        "de cualquier acta); la glosa que sigue es prosa del ejecutor y va marcada como\n"
        "tal.\n"
        "\n"
        "%s"
        "\n"
        "**EL REPARTO POR VIA, CONTADO Y NO TECLEADO:** %s.\n"
        "**Ninguna de las doce sube al fundador.**\n"
        "\n"
        "**LAS TRES CAIDAS PROPIAS DEL AUDITOR, REGISTRADAS IGUAL QUE LAS DEL EJECUTOR**\n"
        "(letra del encargo de la vuelta 163, TAREA 1.a: *\"Mis caidas se registran igual\n"
        "que las tuyas\"*). Ninguna de las tres es del ejecutor y ninguna acumula para sus\n"
        "rachas; se escriben aqui porque el registro de la casa no distingue de quien es\n"
        "la mano que cae.\n"
        "\n"
        "%s"
        "\n"
        "**LO QUE ESTE REGISTRO NO CIERRA.** La vara `P.5.1` sigue CONGELADA y ninguna de\n"
        "estas doce la estrecha ni la ensancha. La relectura conjunta de la\n"
        "`LD-OPC05-101` (acta 162, seccion 5.3) NO se resuelve aqui: va por su cuenta en\n"
        "la TAREA 1.b de la vuelta 163, y si mueve una clase publicada lo hara con\n"
        "correccion declarada y recomputo, en su propia entrada.\n"
        % (numero, sedes_dichas[0], "".join(bloques), linea_reparto,
           "".join(bloques_caidas))
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
    print("VERDE: el acta 162 queda registrada como R.%d en %s." % (numero, sede_rel))
    print("CIFRA entradas escritas: 1")
    print("CIFRA adjudicaciones registradas: %d" % len(adjudicaciones))
    print("CIFRA caidas del auditor registradas: %d" % len(caidas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
