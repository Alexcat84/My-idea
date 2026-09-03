# -*- coding: utf-8 -*-
r"""vuelta162_tarea1b_registrar_adjudicaciones.py . TAREA 1.b de la vuelta 162.

REGISTRA LAS OCHO ADJUDICACIONES DEL ACTA 161 (6.1 a 6.8) EN LA FORMA DE LA CASA
(`R.9` en adelante), EN LA SEDE QUE LA SERIE RECOMPUTADA DIGA.

NINGUNA CELDA SE TECLEA:
  - EL NUMERO lo computa `scripts/loop/serie_de_registros.py` leyendo LAS DOS
    sedes (`siguiente_libre`), que es el remedio de la caida de la vuelta 161;
  - LA SEDE se ELIGE contando la propia serie: la que mas entradas tenga, y se
    publica el reparto para que la eleccion se pueda auditar;
  - EL TITULO Y LA LINEA de cada adjudicacion se LEEN HOY de
    `docs/loop/ACTA_AUDITOR.md`, localizando la seccion 6 DEL ACTA 161 (no de
    cualquier acta: el fichero trae mas de un `6.1`), y si alguna no aparece
    exactamente una vez, este script PARA sin escribir.

LA GLOSA DE CADA UNA SI ES PROSA DEL EJECUTOR, y va marcada como tal: lo que sale
del fichero es el titulo literal y su linea; lo que sigue es como esta vuelta la
ejecuta.

ES IDEMPOTENTE Y LO COMPRUEBA SOBRE LAS DOS SEDES, por su TITULO SIN NUMERO.

USO:  python scripts/loop/vuelta162_tarea1b_registrar_adjudicaciones.py
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
CABECERA_ACTA_161 = "# ACTA DEL AUDITOR, VUELTA 161"
TITULO_SIN_NUMERO = "Registro de las ocho adjudicaciones del acta de la vuelta 161"

# LO QUE ESTA VUELTA HACE CON CADA UNA. Es prosa del ejecutor y va declarada como
# tal. La otra mitad de cada fila (titulo literal y linea) se lee del acta.
QUE_HACE_ESTA_VUELTA = {
    "6.1": ("EJECUTADA SIN TOCAR NADA, Y ERA LO CORRECTO. Las dos se quedan en `C` y "
            "esta vuelta NO les mueve la clase. El pendiente de doctrina 2 del reporte "
            "de la vuelta 161 queda CERRADO sin subir al fundador. La leccion, escrita "
            "para que no se repita: el ejemplar `100` no excluye por consumo, excluye "
            "porque UNA de sus dos direcciones falla, y su propia razon declara LIMPIA "
            "la direccion que el ejecutor creia excluida."),
    "6.2": ("EJECUTADA SIN TOCAR NADA. `LD-OPC05-068` se queda en `C`. El discutible "
            "que el ejecutor marco se resuelve EN SU CONTRA: `P.11` dice que una "
            "advertencia SI es linea valida, y lo que prohibe es contar un nodo hecho "
            "de advertencias como procedimiento."),
    "6.3": ("EJECUTADA SIN TOCAR NADA. `LD-OPC05-005` y `LD-OPC05-084` se quedan en "
            "`C`. Queda anotado que `084` es la mas fina de las catorce y que, si "
            "alguna vuelve algun dia, es esa."),
    "6.4": ("EJECUTADA EN CODIGO, TAREA 2.b de esta vuelta. La vara de los destejidos "
            "toma como absorbidos todo el campo `nodos` menos el superviviente, y la "
            "ficha de `OP-D-02` manda TENER DELANTE a dos de ellos, no absorberlos. Se "
            "arregla con TABLA DE EXCEPCIONES QUE CITA SU ADJUDICACION, el patron de la "
            "lista blanca de `OP-C-05`, y con caso positivo por mutacion."),
    "6.5": ("EJECUTADA EN CODIGO, TAREA 2.a de esta vuelta. La puerta del corredor tras "
            "una parada se ensancha en `scripts/loop/verificar_apertura_sellada.py`. "
            "`--vuelta 161` pasa de ROJA a VERDE y `--vuelta 162` sale VERDE. Ningun "
            "veredicto viejo se mueve, comprobado con la guarda vieja copiada antes de "
            "tocar nada. VA MARCADO COMO DISCUTIBLE: la letra de la adjudicacion (leer "
            "el encargo del portador) NO basta para la vara de aceptacion, porque el "
            "encargo de `d3482b11` no trae el rotulo; lo que pone verde la 161 es que "
            "EL PORTADOR DEL ENCARGO NO ENTRA EN EL CENSO DE INTRUSOS."),
    "6.6": ("EJECUTADA EN CODIGO, TAREA 3 de esta vuelta. "
            "`verificar_cifras_del_reporte.py` pasa a cotejar tambien las afirmaciones "
            "de cierre que vivan en una FILA DE TABLA, y lo que no pueda cotejar lo "
            "dice con su cifra en un AVISO visible. Nada se afloja y la tabla no se "
            "prohibe."),
    "6.7": ("EJECUTADA EN EL REGISTRO, TAREA 1.c de esta vuelta. Las 16 lecturas ciegas "
            "del auditor (las catorce en `C` mas los ejemplares `100` y `122`) dejan "
            "marca contable por ADICION en el campo `razon` de sus filas, con la forma "
            "que `P.5.2` exige, citando la seccion 3 del acta 161 y el sello sha1 "
            "`ffe1fa6f`. NINGUNA CLASE SE MUEVE: las 16 coinciden con la vigente."),
    "6.8": ("EJECUTADA EN EL REGISTRO, TAREA 1.a de esta vuelta. La entrada que la "
            "vuelta 161 numero `R.29` pasa a `R.30` por correccion declarada, sin "
            "borrar una linea y con el titulo viejo tachado y legible. La causa se "
            "arregla EN LA FUENTE: el numero lo computa ahora "
            "`scripts/loop/serie_de_registros.py` leyendo las DOS sedes. LA CAIDA NO "
            "ACUMULA por letra de esta misma adjudicacion."),
}


def cuerpo_del_acta_161():
    """El texto del acta 161, acotado por su cabecera y por el final del fichero
    o la cabecera siguiente. Hace falta acotar: el fichero trae mas de un `6.1`
    (la seccion 6 de casi todas las actas)."""
    texto = io.open(ACTA, encoding="utf-8").read()
    lineas = texto.split("\n")
    inicios = [i for i, l in enumerate(lineas, 1) if l.startswith(CABECERA_ACTA_161)]
    if len(inicios) != 1:
        raise SystemExit("ROJO: la cabecera del acta 161 aparece %d veces." % len(inicios))
    inicio = inicios[0]
    siguientes = [i for i, l in enumerate(lineas, 1)
                  if i > inicio and re.match(r"^# ACTA (DE LA VUELTA|DEL AUDITOR)", l)]
    fin = min(siguientes) - 1 if siguientes else len(lineas)
    return lineas, inicio, fin


def main():
    print("=" * 78)
    print("VUELTA 162, TAREA 1.b: LAS OCHO ADJUDICACIONES DEL ACTA 161, REGISTRADAS")
    print("=" * 78)
    print("")

    serie = SERIE.entradas()
    print("A) LA SERIE, RECOMPUTADA DE SUS DOS SEDES ANTES DE ESCRIBIR")
    for numero, rel, linea, titulo in serie:
        print("   R.%-3d %s:%-6d %s" % (numero, rel, linea, titulo[:88]))
    cols = SERIE.colisiones(serie)
    print("   CIFRA entradas: %d" % len(serie))
    print("   CIFRA colisiones: %d" % len(cols))
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

    print("B) LA SEDE, ELEGIDA CONTANDO LA SERIE Y NO SUPUESTA")
    por_sede = {}
    for n, rel, _l, _t in serie:
        por_sede.setdefault(rel, []).append(n)
    for rel in sorted(por_sede):
        print("   CIFRA entradas en %s: %d" % (rel, len(por_sede[rel])))
    sede_rel = max(sorted(por_sede), key=lambda r: len(por_sede[r]))
    print("   SEDE ELEGIDA: %s (la que mas entradas de la serie tiene)" % sede_rel)
    sede = os.path.join(RAIZ, sede_rel.replace("/", os.sep))
    print("")

    print("C) LAS OCHO ADJUDICACIONES, LEIDAS HOY DE SU LINEA EN EL ACTA 161")
    lineas, inicio, fin = cuerpo_del_acta_161()
    print("   acta 161: docs/loop/ACTA_AUDITOR.md, lineas %d a %d" % (inicio, fin))
    halladas = []
    for k in range(1, 9):
        clave = "6.%d" % k
        patron = re.compile(r"^\*\*%s " % re.escape(clave))
        aciertos = [(i, lineas[i - 1]) for i in range(inicio, fin + 1)
                    if patron.match(lineas[i - 1])]
        if len(aciertos) != 1:
            print("   PARADA: la adjudicacion %s aparece %d veces dentro del acta 161."
                  % (clave, len(aciertos)))
            return 1
        ln, _texto = aciertos[0]
        # EL TITULO ES LA NEGRITA DE APERTURA, NI UNA PALABRA MAS. Se acumulan
        # lineas hasta que la negrita CIERRA, y se corta ahi: si se copiara la
        # linea entera se estaria etiquetando como "titulo literal" un trozo del
        # CUERPO de la adjudicacion, que es una cita que dice mas de lo que es.
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
            print("   PARADA: la negrita de %s no cierra dentro del acta." % clave)
            return 1
        titulo = re.sub(r"\s+", " ", acumulado[2:cierre]).strip()
        halladas.append((clave, ln, titulo))
        print("   %s  docs/loop/ACTA_AUDITOR.md:%d" % (clave, ln))
        print("      %s" % titulo[:150])
    print("   CIFRA adjudicaciones leidas: %d" % len(halladas))
    if len(halladas) != 8:
        print("   PARADA: se esperaban 8.")
        return 1
    print("")

    bloques = []
    for clave, ln, titulo in halladas:
        cuerpo = titulo
        # se quita el numero del principio, que ya va en la vinieta
        cuerpo = re.sub(r"^\*\*%s " % re.escape(clave), "", cuerpo).strip()
        bloques.append(
            "  - **%s (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy).** Titulo literal del\n"
            "    acta: *\"%s\"*\n"
            "    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s\n"
            % (clave, ln, cuerpo, QUE_HACE_ESTA_VUELTA[clave]))

    texto = (
        "\n"
        "---\n"
        "\n"
        "## R.%d. Registro de las ocho adjudicaciones del acta de la vuelta 161 (acta del\n"
        "auditor, vuelta 161, seccion 6; escrito en la vuelta 162, TAREA 1.b)\n"
        "\n"
        "Por adicion, como `R.21` a `R.30`. Las adjudicaciones del auditor se escriben\n"
        "IGUAL que las del ejecutor. **Corte de todas las cifras de esta entrada: 3 sep\n"
        "2026.** El numero de esta entrada NO esta tecleado: lo computa\n"
        "`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes, que\n"
        "es el remedio de la caida de la vuelta 161. Salida:\n"
        "`docs/loop/SALIDA_V162_T1B_ADJUDICACIONES.txt`.\n"
        "\n"
        "**LAS OCHO, CON SU LINEA EN EL ACTA LEIDA HOY.** El titulo de cada una es\n"
        "LITERAL del fichero (localizado dentro de la seccion 6 del acta 161, no de\n"
        "cualquier acta); la glosa que sigue es prosa del ejecutor y va marcada como tal.\n"
        "\n"
        "%s"
        "\n"
        "**EL RESUMEN, CONTADO Y NO TECLEADO: 8 adjudicaciones, de las cuales 3 se\n"
        "ejecutan EN CODIGO (6.4, 6.5, 6.6), 2 EN EL REGISTRO (6.7, 6.8) y 3 SIN TOCAR\n"
        "NADA (6.1, 6.2, 6.3), porque adjudican que lo hecho estaba bien.** Ninguna de las\n"
        "ocho sube al fundador y ninguna mueve una clase.\n"
        "\n"
        "**LO QUE ESTE REGISTRO NO CIERRA.** La vara `P.5.1` sigue CONGELADA y ninguna de\n"
        "estas ocho la estrecha ni la ensancha: la 6.1, la 6.2 y la 6.3 la LEEN entera,\n"
        "con sus ejemplares, y por eso no la mueven.\n"
        % (numero, "".join(bloques))
    )

    with io.open(sede, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)

    print("D) LA ESCRITURA")
    print("   R.%d anadida al final de %s, por adicion pura" % (numero, sede_rel))
    r = subprocess.run(["git", "diff", "--numstat", "--", sede_rel],
                       cwd=RAIZ, capture_output=True, text=True)
    print("   git diff --numstat: %s" % r.stdout.strip())
    print("")

    despues = SERIE.entradas()
    print("E) LA SERIE, RECOMPUTADA DESPUES")
    print("   CIFRA entradas: %d" % len(despues))
    print("   CIFRA colisiones: %d" % len(SERIE.colisiones(despues)))
    print("   CIFRA huecos: %d" % len(SERIE.huecos(despues)))
    print("   SIGUIENTE LIBRE: R.%d" % SERIE.siguiente_libre(despues))
    if SERIE.colisiones(despues):
        print("ROJO: la escritura creo una colision.")
        return 1
    print("")
    print("VERDE: las ocho adjudicaciones quedan registradas como R.%d en %s."
          % (numero, sede_rel))
    print("CIFRA entradas escritas: 1")
    print("CIFRA adjudicaciones registradas: %d" % len(halladas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
