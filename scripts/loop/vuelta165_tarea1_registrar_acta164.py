# -*- coding: utf-8 -*-
r"""vuelta165_tarea1_registrar_acta164.py . TAREA 1 de la vuelta 165.

REGISTRA EN LA FORMA DE LA CASA (`R.N`) EL ACTA 164 ENTERA: SUS DIEZ
ADJUDICACIONES (6.1 a 6.10) Y LAS CAIDAS PROPIAS DEL AUDITOR de su seccion 4.
Las caidas del auditor se registran IGUAL que las del ejecutor, por letra del
encargo de la vuelta 165 (*"registra tambien, con su nombre, MIS DOS CAIDAS de
la seccion 4 del acta, igual que hiciste con la de la 163"*).

CUANTAS CAIDAS SE REGISTRAN, Y POR QUE NO SE TECLEA LA CIFRA. El encargo de la
165 dice DOS en su TAREA 1 y TRES en su propia prosa de apertura (*"Y VAN MIS
TRES CAIDAS DE HOY"*), y las enumera. La seccion 4 del acta 164, CONTADA HOY
por este instrumento con el patron `^\s*\*\*CAIDA \d[,.]` dentro del cuerpo
acotado del acta, trae TRES. NO SE ADIVINA CUAL DE LAS DOS CIFRAS DEL ENCARGO
manda: se registra LO QUE LA SECCION CONTIENE, contado, y la discrepancia entre
las dos cifras del encargo se DECLARA en la propia entrada y en el reporte.
Registrar las tres cubre las dos; registrar dos dejaria una caida del auditor
sin registro y esa si seria una perdida.

HEREDA EL INSTRUMENTO DE LA VUELTA 164 (`vuelta164_tarea1_registrar_acta163.py`)
SIN CAMBIARLE EL MECANISMO, y solo mueve lo que el acta nueva mueve:

  (1) EL CUERPO ACOTADO pasa del acta 163 al acta 164 (`CABECERA_ACTA`), que es
      hoy la ULTIMA del fichero: `fin` cae en el final del fichero y no en la
      cabecera siguiente. Medido: cuerpo en las lineas 54404 a 54828.
  (2) LAS CAIDAS dejan de ser una y pasan a ser LAS QUE HAYA. El instrumento
      viejo llevaba `range(1, 2)` y un `!= 1` tecleados; aqui el numero de
      caidas se COMPUTA del acta (`negritas 'CAIDA n' halladas`) y la glosa de
      cada una se busca por su clave: si apareciera una caida sin glosa
      escrita, PARA en vez de publicar una entrada coja.

NINGUNA CELDA SE TECLEA: el numero de la entrada lo computa
`serie_de_registros.py` recomputando LAS DOS sedes; el titulo y la linea de cada
adjudicacion y de cada caida se LEEN HOY del acta; el reparto por via se CUENTA
del diccionario de vias.

LA GLOSA DE CADA UNA SI ES PROSA DEL EJECUTOR, y va marcada como tal.

ES IDEMPOTENTE Y LO COMPRUEBA SOBRE LAS DOS SEDES, por su TITULO SIN NUMERO, y
ademas se niega a escribir si el titulo esta en el fichero pero la serie no lo
ve (la trampa de la cabecera partida que cazo la vuelta 164).

USO:  python scripts/loop/vuelta165_tarea1_registrar_acta164.py
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402

RAIZ = SERIE.RAIZ
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 164"
TITULO_SIN_NUMERO = ("Registro de las diez adjudicaciones y las tres caidas "
                     "propias del acta de la vuelta 164")

FRASE_DE_LA_SEDE = "la sede por defecto es `docs/PENDIENTES.md`"

VIA = {
    "6.1": "SIN TOCAR NADA",
    "6.2": "SIN TOCAR NADA",
    "6.3": "EN CODIGO",
    "6.4": "EN EL REPORTE",
    "6.5": "EN MEDICION",
    "6.6": "EN MEDICION",
    "6.7": "SIN TOCAR NADA",
    "6.8": "SIN TOCAR NADA",
    "6.9": "EN MEDICION",
    "6.10": "EN EJECUCION",
}

QUE_HACE_ESTA_VUELTA = {
    "6.1": ("SE ACATA SIN TOCAR NADA. La caida de clase de la `LD-OPC05-005` queda "
            "CONFIRMADA por segunda pluma y cuenta UNA para la racha de cifra "
            "publicada, que queda en UNO. La vuelta 165 no la vuelve a abrir ni la "
            "vuelve a mover: lo que cambia es el cuidado, no el registro."),
    "6.2": ("SE ACATA SIN TOCAR NADA. La `LD-OPC05-101` se queda en `D` con la firma "
            "del auditor, y su veredicto sigue viviendo en la razon del registro y no "
            "en el asunto de un commit. La vuelta 165 NO la relee y no la mueve."),
    "6.3": ("EJECUTADA EN CODIGO, TAREA 2 de esta vuelta. El punto ciego del censo de "
            "`verificar_mutaciones_viejas.py` se arregla EN LA FUENTE y con su caso "
            "positivo por mutacion, que hoy para este agujero no existia: el caso tiene "
            "que CAER si alguien devuelve el patron a su forma vieja."),
    "6.4": ("EJECUTADA EN EL REPORTE, TAREA 3 de esta vuelta. La cadena entera y cerrada "
            "va escrita en el reporte de la 165 (92 vistos por el censo, 53 en la "
            "nomina, 51 visibles al censo, 41 fuera), SIN BORRAR la frase vieja, y la "
            "relectura al doble del tramo se hace."),
    "6.5": ("EJECUTADA COMO MEDICION, TAREA 4 de esta vuelta. La PENDIENTE DE DOCTRINA "
            "queda retirada por el ejecutor: la regla no habla del calendario sino del "
            "ESTADO DEL SUJETO, asi que no puede ser retroactiva ni dejar de serlo. Los "
            "41 se miden UNO POR UNO y se publica cual tiene sujeto congelado y cual "
            "sujeto vivo, con su evidencia. Ninguno entra en bloque y ninguno se "
            "descarta en bloque."),
    "6.6": ("EJECUTADA COMO MEDICION, TAREA 4 de esta vuelta. Todo arnes que entre entra "
            "con su tiempo publicado al lado, y si el total de la bateria pasa de VEINTE "
            "MINUTOS se dice en el reporte con la cifra delante. La nomina NO se recorta "
            "por cuenta propia para que corra antes."),
    "6.7": ("SE ACATA SIN TOCAR NADA. El campo `cita` NO crece: es el puntero que la "
            "guarda `C.7` coteja contra la `clase`, y la historia entera sigue viviendo "
            "en la `razon`. La PREGUNTA 1 del reporte de la 164 queda CERRADA y la 165 "
            "no la arrastra."),
    "6.8": ("SE ACATA SIN TOCAR NADA. `node_modules/` es alcance del fundador, no "
            "bloquea nada y no dispara parada. La PREGUNTA 2 queda CERRADA y el reporte "
            "de la 165 DEJA DE ARRASTRARLA; sigue apareciendo como `??` en `git status` "
            "y eso ya no es una pregunta del bucle."),
    "6.9": ("EJECUTADA COMO MEDICION, TAREA 5 de esta vuelta. Las suites de la web, el "
            "`tsc` y el `sha256` del indice semantico se CORREN con el comando del "
            "ejecutor y se publican con el; NINGUNA cifra se copia del commit del "
            "fundador, que se cita solo como CONTRASTE. Y "
            "`SELLO_SESION_CREDENCIAL_2026-09-03.md` se cierra POR ADICION, sin borrar "
            "su ultima linea, que era cierta el dia que se escribio."),
    "6.10": ("EJECUTADA EN EJECUCION, TAREA 6 de esta vuelta. Se abre el ultimo tramo de "
             "la fase III por `OP-L-01`, la unica de las cuatro en `LISTA` sin "
             "dependencias declaradas: se lee su ficha entera y se comprueban sus TRES "
             "clausulas de verificacion contra el archivo de HOY. Si el texto de la "
             "operacion no alcanza para ejecutarse sin decidir, eso es PARADA y se trae "
             "con la letra delante, no se improvisa."),
}

QUE_HACE_CON_LA_CAIDA = {
    "CAIDA 1": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL EJECUTOR, "
                "porque no es suya. Su remedio esta ACATADO en el procedimiento de esta "
                "vuelta y es comprobable en el bloque de apertura: "
                "`scripts/loop/vuelta165_apertura.py` corre el ciclo ENTERO y en su "
                "orden (`--reaplico-curaduria`, `etiquetas_de_cara --aplicar`, "
                "`sync_assets_web` y DESPUES el `numstat`), nunca `run_phase1` suelto, y "
                "su `numstat` de `dataset/ web/ engine/` da CERO FILAS."),
    "CAIDA 2": ("SE REGISTRA CON SU NOMBRE Y LO QUE ENSENA SE ESCRIBE ENTERO: una ciega "
                "que no puede ver la razon tampoco puede refutar la razon, y lo que la "
                "ciega decide es la CLASE y no el camino ajeno. No acumula para ninguna "
                "racha del ejecutor. La `LD-OPC05-101` no se reabre por esto: su letra "
                "coincide por los dos caminos y la 6.2 la firma."),
    "CAIDA 3": ("SE REGISTRA CON SU NOMBRE Y SU REMEDIO SE ACATA EN EL PROCEDIMIENTO DE "
                "ESTA VUELTA: la bateria se corre SOLA, sin trabajo del ejecutor al "
                "lado, y su comprobacion de RUIDO DE CONCURRENCIA se publica con la "
                "cifra que salga. Y va con lo que la propia caida ensena sobre la cifra "
                "que arrastra: el reloj de 19,9 minutos del auditor esta medido CON "
                "ruido, asi que es un TECHO y no un suelo, y asi se cita en la TAREA 4."),
}


def cuerpo_del_acta():
    """El texto del acta 164, acotado por su cabecera y por el final del fichero
    o la cabecera siguiente. Hace falta acotar: el fichero trae mas de un `6.1`
    y mas de una `CAIDA 1`."""
    texto = io.open(ACTA, encoding="utf-8").read()
    lineas = texto.split("\n")
    inicios = [i for i, l in enumerate(lineas, 1) if l.startswith(CABECERA_ACTA)]
    if len(inicios) != 1:
        raise SystemExit("ROJO: la cabecera del acta 164 aparece %d veces." % len(inicios))
    inicio = inicios[0]
    siguientes = [i for i, l in enumerate(lineas, 1)
                  if i > inicio and re.match(r"^# ACTA (DE LA VUELTA|DEL AUDITOR)", l)]
    fin = min(siguientes) - 1 if siguientes else len(lineas)
    return lineas, inicio, fin


def titulo_de_la_negrita(lineas, inicio, fin, patron, etiqueta):
    """EL TITULO ES LA NEGRITA DE APERTURA, NI UNA PALABRA MAS, con la LINEA EN
    BLANCO como frontera (arreglo (3) de la vuelta 164: sin frontera, la funcion
    se comia el `**` de apertura de la entrada siguiente y salia en verde)."""
    aciertos = [i for i in range(inicio, fin + 1) if patron.match(lineas[i - 1])]
    if len(aciertos) != 1:
        return None, "PARADA: %s aparece %d veces dentro del acta 164." % (
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
    print("VUELTA 165, TAREA 1: EL ACTA 164 ENTERA, REGISTRADA EN LA FORMA DE LA CASA")
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

    lineas, inicio, fin = cuerpo_del_acta()
    print("B) LA SEDE, LEIDA DE LA REGLA ESCRITA Y NO SUPUESTA")
    print("   acta 164: docs/loop/ACTA_AUDITOR.md, lineas %d a %d" % (inicio, fin))
    todas = [i for i, l in enumerate(lineas, 1) if FRASE_DE_LA_SEDE in l]
    dentro = [i for i in todas if inicio <= i <= fin]
    print("   CIFRA veces que la frase de la sede aparece en el fichero entero: %d"
          % len(todas))
    print("   CIFRA veces que aparece DENTRO del acta 164: %d" % len(dentro))
    if len(todas) != 1:
        print("   PARADA: la frase de la sede no aparece exactamente una vez.")
        return 1
    print("   DECLARADO: el acta 164 NO repite la frase; la regla vive en la")
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

    print("C) LAS DIEZ ADJUDICACIONES, LEIDAS HOY DE SU LINEA EN EL ACTA 164")
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

    print("D) LAS CAIDAS PROPIAS DEL AUDITOR, CONTADAS Y LEIDAS HOY DE LA SECCION 4")
    print("   LA CIFRA NO SE TECLEA: se cuentan las negritas 'CAIDA n' del cuerpo")
    print("   acotado del acta 164. El encargo de la 165 dice DOS en su TAREA 1 y")
    print("   TRES en su prosa de apertura; no se adivina cual manda, se cuenta.")
    encontradas = [i for i in range(inicio, fin + 1)
                   if re.match(r"^\s*\*\*CAIDA \d[,.]", lineas[i - 1])]
    print("   CIFRA negritas 'CAIDA n' halladas en el acta 164: %d" % len(encontradas))
    if not encontradas:
        print("   PARADA: no hay ninguna caida propia que registrar.")
        return 1
    caidas = []
    for ln0 in encontradas:
        m = re.match(r"^\s*\*\*(CAIDA \d)[,.]", lineas[ln0 - 1])
        clave = m.group(1)
        patron = re.compile(r"^\s*\*\*%s[,.]" % re.escape(clave))
        hallado, error = titulo_de_la_negrita(
            lineas, inicio, fin, patron, "la %s" % clave)
        if error:
            print("   " + error)
            return 1
        ln, titulo = hallado
        if clave not in QUE_HACE_CON_LA_CAIDA:
            print("   PARADA: %s no tiene glosa escrita en este instrumento." % clave)
            return 1
        caidas.append((clave, ln, titulo))
        print("   %-8s docs/loop/ACTA_AUDITOR.md:%d" % (clave, ln))
        print("      %s" % titulo[:150])
    print("   CIFRA caidas leidas: %d" % len(caidas))
    if len(caidas) != len(encontradas):
        print("   PARADA: se leyeron menos caidas de las que hay.")
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
        "## R.%d. %s\n"
        "\n"
        "(Acta del auditor, vuelta 164, secciones 4 y 6; escrito en la vuelta 165,\n"
        "TAREA 1.)\n"
        "\n"
        "Por adicion, como `R.21` a `R.33`. **Corte de todas las cifras de esta entrada:\n"
        "4 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa\n"
        "`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes. La\n"
        "SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, leida hoy en\n"
        "`docs/loop/ACTA_AUDITOR.md:%d`, y se DECLARA que el acta 164 no la repite (la\n"
        "regla es de la casa, no de un acta suelta). Salida:\n"
        "`docs/loop/SALIDA_V165_T1_REGISTRO_ACTA_164.txt`.\n"
        "\n"
        "**LAS DIEZ ADJUDICACIONES, CON SU LINEA EN EL ACTA LEIDA HOY.** El titulo de\n"
        "cada una es LITERAL del fichero (localizado dentro del cuerpo del acta 164, no\n"
        "de cualquier acta); la glosa que sigue es prosa del ejecutor y va marcada como\n"
        "tal.\n"
        "\n"
        "%s"
        "\n"
        "**EL REPARTO POR VIA, CONTADO Y NO TECLEADO:** %s.\n"
        "**Ninguna de las diez sube al fundador.**\n"
        "\n"
        "**LAS CAIDAS PROPIAS DEL AUDITOR, REGISTRADAS IGUAL QUE LAS DEL EJECUTOR**\n"
        "(letra del encargo de la vuelta 165, TAREA 1). No son del ejecutor y no acumulan\n"
        "para sus rachas; se escriben aqui porque el registro de la casa no distingue de\n"
        "quien es la mano que cae.\n"
        "\n"
        "**Y SE DECLARA LA DISCREPANCIA DE CIFRA DEL PROPIO ENCARGO, EN VEZ DE\n"
        "RESOLVERLA COPIANDO** (`EJECUTOR.md` 2). Su TAREA 1 pide registrar *\"MIS DOS\n"
        "CAIDAS de la seccion 4 del acta\"*; su prosa de apertura, en el mismo encargo,\n"
        "dice *\"Y VAN MIS TRES CAIDAS DE HOY, que se registran igual que las tuyas\"* y\n"
        "las enumera. La seccion 4 del acta 164, CONTADA HOY por este instrumento dentro\n"
        "del cuerpo acotado del acta, trae TRES negritas `CAIDA n`. Se registran LAS QUE\n"
        "LA SECCION CONTIENE: registrar tres cubre dos, y registrar dos dejaria una caida\n"
        "del auditor sin registro.\n"
        "\n"
        "%s"
        "\n"
        "**LO QUE ESTE REGISTRO NO CIERRA.** La vara `P.5.1` sigue CONGELADA y ninguna de\n"
        "estas diez la estrecha ni la ensancha. La `LD-OPC05-005` y la `LD-OPC05-101` NO\n"
        "se reabren aqui ni en ningun sitio de la vuelta 165: la 6.1 confirma la primera\n"
        "y la 6.2 firma la segunda. La `OP-L-01` que abre la 6.10 se ejecuta en la TAREA\n"
        "6 de la vuelta 165 y, si su texto no alcanza para ejecutarse sin decidir, sale\n"
        "por PARADA y no por improvisacion.\n"
        % (numero, TITULO_SIN_NUMERO, todas[0], "".join(bloques), linea_reparto,
           "".join(bloques_caidas))
    )

    with io.open(sede, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)
    print("F) ESCRITO")
    print("   R.%d en %s" % (numero, sede_rel))
    print("   CIFRA adjudicaciones escritas: %d" % len(adjudicaciones))
    print("   CIFRA caidas escritas: %d" % len(caidas))
    print("   CIFRA entradas escritas: 1")
    print("")

    serie2 = SERIE.entradas()
    ve = [(n, rel, ln) for n, rel, ln, t in serie2 if TITULO_SIN_NUMERO in t]
    print("G) LA SERIE, RECOMPUTADA DESPUES DE ESCRIBIR")
    print("   CIFRA entradas: %d" % len(serie2))
    print("   CIFRA colisiones: %d" % len(SERIE.colisiones(serie2)))
    print("   CIFRA huecos: %d" % len(SERIE.huecos(serie2)))
    print("   la serie VE la entrada nueva: %s" % ("SI, R.%d en %s:%d" % ve[0] if ve else "NO"))
    if not ve:
        print("   PARADA: escrita pero invisible para la serie. Revisar la cabecera.")
        return 1
    print("")
    print("VERDE: el acta 164 queda registrada como R.%d." % numero)
    return 0


# ---------------------------------------------------------------------------
# CASO POSITIVO POR MUTACION (EJECUTOR.md regla 1, "EL CASO ROJO SE PRUEBA POR
# MUTACION"). Se corre con `--mutar` y con el arnes de nombre propio
# `vuelta165_tarea1_mutacion_registro.py`, que es el que la bateria ve.
#
# CERO ESCRITURAS Y CERO FICHEROS: las actas de mentira se fabrican EN MEMORIA
# como listas de lineas. Nada toca `docs/PENDIENTES.md` ni
# `docs/loop/ACTA_AUDITOR.md`.
#
# QUE MIDE, Y POR QUE ES ESTO Y NO OTRA COSA. Lo que este instrumento CAMBIA
# respecto del de la vuelta 164 es UNA SOLA cosa: la cifra de caidas dejo de
# estar tecleada (`range(1, 2)` y `!= 1`) y pasa a COMPUTARSE del acta. Asi que
# lo que hay que poder tumbar es exactamente eso: que el conteo siga a lo que el
# acta trae, sea cual sea, y que una caida SIN GLOSA pare en vez de publicar una
# entrada coja.
#
# NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: los casos salen de correr las
# funciones reales sobre sujetos distintos, y la segunda pasada muta cada valor
# esperado y exige que el caso CAIGA.
# ---------------------------------------------------------------------------

FRONTERA_FALSA = "# ACTA DEL AUDITOR, VUELTA 165 (frontera de mentira)"
CABECERA_FALSA = CABECERA_ACTA + " (fabricada por la prueba de mutacion)"
PAT_CAIDA = re.compile(r"^\s*\*\*CAIDA \d[,.]")


def _acta_fabricada(caidas=3, sangria="  ", duplicar=None, quitar=None,
                    sin_cierre=False):
    """Un acta 164 DE MENTIRA, en memoria. Devuelve (lineas, inicio, fin)."""
    L = ["ruido de otra acta",
         "**6.1 ESTA NO CUENTA, VIVE FUERA DEL CUERPO.** ruido",
         "**CAIDA 1. ESTA TAMPOCO, VIVE FUERA DEL CUERPO.** ruido",
         "",
         CABECERA_FALSA,
         "cuerpo cualquiera",
         "",
         "## 4. MIS CAIDAS PROPIAS DE ESTA VUELTA, CON SU NOMBRE",
         ""]
    for k in range(1, caidas + 1):
        L.append("%s**CAIDA %d. TITULO DE LA CAIDA %d FABRICADA.** cuerpo"
                 % (sangria, k, k))
        L.append("")
    L.append("## 6. ADJUDICACIONES")
    L.append("")
    for k in range(1, 11):
        clave = "6.%d" % k
        if quitar == clave:
            continue
        for _ in range(2 if duplicar == clave else 1):
            if k == 4:
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
    L.append("**CAIDA 9. NI ESTA.** ruido de despues")
    return L, L.index(CABECERA_FALSA) + 1, L.index(FRONTERA_FALSA)


def _cuenta_caidas(lineas, inicio, fin):
    return len([i for i in range(inicio, fin + 1) if PAT_CAIDA.match(lineas[i - 1])])


def _cuantas_ve(lineas, inicio, fin, plantilla):
    vistas = 0
    for k in range(1, 11):
        pat = re.compile(plantilla % re.escape("6.%d" % k))
        if len([i for i in range(inicio, fin + 1) if pat.match(lineas[i - 1])]) == 1:
            vistas += 1
    return vistas


def prueba_de_mutacion():
    print("=" * 78)
    print("VUELTA 165, TAREA 1: CASO POSITIVO POR MUTACION DEL REGISTRADOR DEL ACTA 164")
    print("=" * 78)
    print("")
    casos = []

    print("A) LA CIFRA DE CAIDAS SIGUE AL ACTA Y NO A UNA CONSTANTE")
    for n in (1, 2, 3, 5):
        L, ini, fin = _acta_fabricada(caidas=n)
        visto = _cuenta_caidas(L, ini, fin)
        print("   acta fabricada con %d caidas -> el conteo ve %d" % (n, visto))
        casos.append(("A_con_%d_caidas_ve_%d" % (n, n), visto, n))
    print("")

    print("B) EL ACOTADO DEJA FUERA EL RUIDO DE OTRAS ACTAS")
    L, ini, fin = _acta_fabricada(caidas=3)
    fuera = _cuenta_caidas(L, 1, len(L))
    print("   sin acotar, el fichero entero trae %d negritas CAIDA" % fuera)
    print("   acotado al cuerpo, trae %d" % _cuenta_caidas(L, ini, fin))
    casos.append(("B_sin_acotar_hay_ruido", fuera, 5))
    casos.append(("B_acotado_no_lo_ve", _cuenta_caidas(L, ini, fin), 3))
    casos.append(("B_el_acotado_ve_las_diez_adjudicaciones",
                  _cuantas_ve(L, ini, fin, r"^\s*\*\*%s "), 10))
    casos.append(("B_sin_acotar_la_6_1_esta_tres_veces",
                  len([i for i in range(1, len(L) + 1)
                       if re.match(r"^\s*\*\*6\.1 ", L[i - 1])]), 3))
    print("")

    print("C) LOS CAMINOS DE PARADA SIGUEN VIVOS")
    Ld, id_, fd = _acta_fabricada(duplicar="6.5")
    _h, e_dup = titulo_de_la_negrita(Ld, id_, fd, re.compile(r"^\s*\*\*6\.5 "), "6.5")
    print("   duplicada: %s" % (e_dup or "NO PARA"))
    casos.append(("C_duplicada_para", e_dup is not None, True))
    Lq, iq, fq = _acta_fabricada(quitar="6.7")
    _h, e_aus = titulo_de_la_negrita(Lq, iq, fq, re.compile(r"^\s*\*\*6\.7 "), "6.7")
    print("   ausente: %s" % (e_aus or "NO PARA"))
    casos.append(("C_ausente_para", e_aus is not None, True))
    Ls, is_, fs = _acta_fabricada(sin_cierre=True)
    _h, e_sc = titulo_de_la_negrita(Ls, is_, fs, re.compile(r"^\s*\*\*6\.9 "), "6.9")
    print("   negrita sin cierre: %s" % (e_sc or "NO PARA"))
    casos.append(("C_negrita_sin_cierre_para", e_sc is not None, True))
    print("")

    print("D) UNA CAIDA SIN GLOSA TIENE QUE PARAR, NO PUBLICARSE COJA")
    L5, i5, f5 = _acta_fabricada(caidas=5)
    claves5 = [re.match(r"^\s*\*\*(CAIDA \d)[,.]", L5[i - 1]).group(1)
               for i in range(i5, f5 + 1) if PAT_CAIDA.match(L5[i - 1])]
    sin_glosa = [c for c in claves5 if c not in QUE_HACE_CON_LA_CAIDA]
    print("   claves del acta de 5 caidas: %s" % ", ".join(claves5))
    print("   sin glosa escrita en este instrumento: %s"
          % (", ".join(sin_glosa) or "ninguna"))
    casos.append(("D_las_que_no_tienen_glosa_se_detectan", len(sin_glosa), 2))
    L3, i3, f3 = _acta_fabricada(caidas=3)
    claves3 = [re.match(r"^\s*\*\*(CAIDA \d)[,.]", L3[i - 1]).group(1)
               for i in range(i3, f3 + 1) if PAT_CAIDA.match(L3[i - 1])]
    casos.append(("D_las_tres_de_hoy_SI_tienen_glosa",
                  len([c for c in claves3 if c not in QUE_HACE_CON_LA_CAIDA]), 0))
    print("")

    print("E) EL ACTA DE VERDAD, LEIDA HOY")
    RL, ri, rf = cuerpo_del_acta()
    print("   cuerpo del acta 164: lineas %d a %d" % (ri, rf))
    n_adj = _cuantas_ve(RL, ri, rf, r"^\s*\*\*%s ")
    n_cai = _cuenta_caidas(RL, ri, rf)
    print("   CIFRA adjudicaciones que se leen exactamente una vez: %d" % n_adj)
    print("   CIFRA caidas que trae la seccion 4: %d" % n_cai)
    casos.append(("E_el_acta_164_trae_las_diez_adjudicaciones", n_adj, 10))
    casos.append(("E_el_acta_164_trae_TRES_caidas", n_cai, 3))
    todas = [i for i, l in enumerate(RL, 1) if FRASE_DE_LA_SEDE in l]
    casos.append(("E_la_frase_de_la_sede_esta_una_vez_en_el_fichero", len(todas), 1))
    casos.append(("E_y_cero_veces_dentro_del_acta_164",
                  len([i for i in todas if ri <= i <= rf]), 0))
    patrones = [(re.compile(r"^\s*\*\*6\.%d " % k), "6.%d" % k) for k in range(1, 11)]
    patrones += [(re.compile(r"^\s*\*\*CAIDA %d[,.]" % k), "CAIDA %d" % k)
                 for k in (1, 2, 3)]
    sin_error = 0
    for pat, et in patrones:
        _h, e = titulo_de_la_negrita(RL, ri, rf, pat, et)
        if e is None:
            sin_error += 1
    print("   CIFRA negritas que se leen sin error: %d de %d" % (sin_error, len(patrones)))
    casos.append(("E_las_trece_negritas_se_leen_sin_error", sin_error, 13))
    print("")

    print("F) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-46s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("G) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        else:
            mutado = str(esperado) + "_mutado"
        cae = (real != mutado)
        print("   %-46s %s   (esperado mutado=%r)"
              % (nombre, "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    if "--mutar" in sys.argv:
        sys.exit(prueba_de_mutacion())
    sys.exit(main())
