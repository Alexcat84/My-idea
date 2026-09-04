# -*- coding: utf-8 -*-
r"""vuelta168_tarea1_registrar_acta167.py . TAREA 1 de la vuelta 168.

REGISTRA EN LA FORMA DE LA CASA (`R.N`) EL ACTA 167 ENTERA: SUS ADJUDICACIONES
`6.n` Y LAS CAIDAS PROPIAS DEL AUDITOR de su seccion 3. Las caidas del auditor
se registran IGUAL que las del ejecutor, por el precedente que la vuelta 167
fijo en el `R.36` y que esta vuelta hereda sin reabrirlo.

QUE CAMBIA RESPECTO DEL INSTRUMENTO DE LA VUELTA 167
(`vuelta167_tarea1_registrar_acta166.py`), cuya maquina se hereda SIN tocarle
el mecanismo:

  (1) EL CUERPO ACOTADO pasa del acta 166 al acta 167 (`CABECERA_ACTA`), que es
      hoy la ULTIMA del fichero: `fin` cae en el final del fichero y no en la
      cabecera siguiente.
  (2) LAS CIFRAS NO SE TECLEAN Y ESTA VUELTA LO NOTA: el acta 167 trae MENOS
      adjudicaciones que la 166 y MAS caidas propias, asi que el numeral en
      palabra y las DOS ramas de concordancia del titulo (singular y plural de
      "caida propia") salen del conteo y no de una constante. La 167 escogio la
      rama del singular; esta escoge la del plural, y es la misma funcion.
  (3) UNA VIA NUEVA, Y NACE DE UN HECHO Y NO DE UN GUSTO: el acta 167 SUBE una
      adjudicacion al fundador con esas palabras ("no lo adjudico ni en un
      sentido ni en el otro: lo subo"), cosa que el acta 166 no hacia. La linea
      del reparto por via del `R.36` decia "Ninguna de las nueve sube al
      fundador"; aqui esa frase SE COMPUTA en vez de teclearse, y dice la
      verdad de este acta: cuantas suben y cuales.

NINGUNA CELDA SE TECLEA: el numero de la entrada lo computa
`serie_de_registros.py` recomputando la serie de sus dos sedes, y el
instrumento ademas se niega a escribir si el titulo esta en el fichero pero la
serie no lo ve (la trampa de la cabecera partida que cazo la vuelta 164).

USO:  python scripts/loop/vuelta168_tarea1_registrar_acta167.py
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402

RAIZ = SERIE.RAIZ
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 167"

FRASE_DE_LA_SEDE = "la sede por defecto es `docs/PENDIENTES.md`"

PALABRA = {1: "una", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis",
           7: "siete", 8: "ocho", 9: "nueve", 10: "diez", 11: "once",
           12: "doce", 13: "trece", 14: "catorce", 15: "quince",
           16: "dieciseis", 17: "diecisiete", 18: "dieciocho",
           19: "diecinueve", 20: "veinte"}


def titulo_de_la_entrada(n_adj, n_cai):
    """El titulo, con sus dos numerales COMPUTADOS y no tecleados. La
    concordancia de la segunda mitad se elige con el conteo: una caida lleva
    singular y dos o mas llevan plural."""
    cola = ("la caida propia" if n_cai == 1
            else "las %s caidas propias" % PALABRA[n_cai])
    return ("Registro de las %s adjudicaciones y %s del acta de la vuelta 167"
            % (PALABRA[n_adj], cola))


VIA = {
    "6.1": "SIN TOCAR NADA",
    "6.2": "SIN TOCAR NADA",
    "6.3": "SIN TOCAR NADA",
    "6.4": "EN MEDICION",
    "6.5": "EN MEDICION",
    "6.6": "AL FUNDADOR, YA CONTESTADA",
}

QUE_HACE_ESTA_VUELTA = {
    "6.1": ("SE ACATA SIN TOCAR NADA. La parada que la vuelta 167 trajo sobre `OP-C-01` "
            "queda adjudicada A FAVOR DEL EJECUTOR y esta vuelta no la reabre: la ficha "
            "no se edita, su estado no se mueve y la operacion no se ejecuta. Lo que "
            "esta vuelta anade es el marco donde ese caso deja de ser suelto: la "
            "decision del fundador del 4 sep 2026 jubila el campo `estado` y pone la "
            "vara en el instrumento, y por esa vara `OP-C-01` no esta entre las seis que "
            "quedan. La TAREA 5 de esta vuelta lo vuelve a medir con el instrumento y "
            "publica su salida."),
    "6.2": ("SE ACATA SIN TOCAR NADA, Y ES LA QUE EL FUNDADOR CONTESTO. El ejecutor no "
            "mueve ni un `estado` en esta vuelta, que es exactamente lo que la "
            "adjudicacion reserva. La decision del fundador (punto 1) resuelve el fondo "
            "por otra via, y no moviendo los treinta y seis estados: el campo queda "
            "JUBILADO COMO HISTORICO, la vara del trabajo pendiente pasa a ser "
            "`scripts/loop/vuelta150_3_relectura_expediente.py`, y la reconciliacion "
            "ficha por ficha se hace UNA vez en la auditoria integral como acto de "
            "archivo. Ya esta declarado en `docs/plan/00_INDICE.md` y citado en "
            "`docs/loop/AUDITOR.md` seccion 0, asi que esta vuelta no lo vuelve a "
            "escribir."),
    "6.3": ("SE ACATA SIN TOCAR NADA. La `A` del puesto 611 se queda donde esta y "
            "NINGUNA CLASE SE MUEVE en esta vuelta. La adjudicacion se cierra CONTRA EL "
            "PROPIO AUDITOR y no abre relectura conjunta, asi que no hay nada que el "
            "ejecutor tenga que verificar contra el grafo ni que recomputar. El archivo "
            "de veredictos no se toca."),
    "6.4": ("EJECUTADA COMO MEDICION, y gobierna la vuelta entera y no una tarea suelta. "
            "Es la relectura al doble DE SEDE: toda afirmacion sobre el estado de una "
            "operacion del plan se mide con "
            "`scripts/loop/vuelta150_3_relectura_expediente.py` ANTES de escribirse, y "
            "el comando se pega al lado. Esta vuelta la cumple donde mas cuesta: la "
            "TAREA 5 no lee el campo `estado` para saber que abrir, sino el instrumento, "
            "y los `depende_de` de `OP-L-02` y `OP-L-03` se leen tambien por el "
            "instrumento. El campo solo se cita diciendo que es el campo."),
    "6.5": ("EJECUTADA COMO MEDICION, TAREA 1 de esta vuelta, y por el carril del banco "
            "9.10. Al `R.36` se le ADOSA una nota fechada al final diciendo que sus "
            "glosas de la 6.1, 6.3, 6.4 y 6.9 describian LO ENCARGADO y no LO OCURRIDO, "
            "con el hash de la parada al lado. NINGUNA PALABRA VIEJA SE BORRA: la glosa "
            "equivocada se queda entera y visible, porque una correccion que tapa lo que "
            "corrige no se puede auditar."),
    "6.6": ("SUBIDA AL FUNDADOR POR EL AUDITOR, Y YA CONTESTADA, asi que esta vuelta no "
            "la adjudica ni la reabre: la ACATA. El auditor se nego a aplicar por "
            "tercera vez el precedente de la vuelta cortada y lo subio con esas "
            "palabras. El fundador contesto en el punto 3 de su decision del 4 sep 2026, "
            "y no aplicando el precedente otra vez sino cambiando la maquina: EL REPORTE "
            "ABRE CON LA VUELTA y crece por anexion, con tope de cinco tareas. Esta "
            "vuelta es la primera que corre bajo esa regla y la estrena sobre si misma: "
            "el esqueleto de `docs/loop/REPORTE.md` se tallo ANTES de esta TAREA 1."),
}

QUE_HACE_CON_LA_CAIDA = {
    "CAIDA 1": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. Es la caida que abrio la parada y la que "
                "el fundador contesto: el auditor leyo el campo `estado` de "
                "`docs/plan/OPERACIONES.jsonl` como si fuera un rastreador del trabajo, "
                "conto 6 en `LISTA` y 1 en `HECHA` (conteo exacto) y de ahi saco una "
                "conclusion falsa, sin correr el instrumento que la casa escribio en la "
                "vuelta 150 para esto exactamente. LO QUE SI ARRASTRA, y por eso se "
                "escribe aqui y no se calla: su 6.9 del acta 166 llego a "
                "`docs/PENDIENTES.md` como `R.36` y fue el encargo de la TAREA 5 de la "
                "vuelta 167, o sea que ESTA CAIDA SI SALIO DE SU ACTA. El remedio no es "
                "borrar aquella glosa: es la nota adosada de la 6.5, que esta misma "
                "TAREA 1 escribe. Lo que ensena muerde a cualquiera: contar bien un "
                "campo y sacar la conclusion equivocada sigue siendo una caida, porque "
                "LA FUENTE HAY QUE ELEGIRLA ANTES DE CONTARLA."),
    "CAIDA 2": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. Y SE DICE LO QUE NO ARRASTRA, con la "
                "medicion delante: la letra ciega equivocada era la del auditor, la "
                "adjudicacion 6.3 la retiro en el mismo acta, y NINGUNA CLASE SE MOVIO, "
                "asi que NO HAY CIFRA PUBLICADA QUE CORREGIR POR ELLA y esta entrada no "
                "declara ninguna correccion en su nombre. La `A` del puesto 611 sigue "
                "siendo `A` y su razon sigue siendo la que estaba escrita. Lo que "
                "ensena, en las palabras del propio acta: antes de sellar una letra, la "
                "vara que se va a citar SE LEE ENTERA, no se recuerda."),
}
def cuerpo_del_acta():
    """El texto del acta 166, acotado por su cabecera y por el final del fichero
    o la cabecera siguiente. Hace falta acotar: el fichero trae mas de un `6.1`
    y mas de una `CAIDA 1`."""
    texto = io.open(ACTA, encoding="utf-8").read()
    lineas = texto.split("\n")
    inicios = [i for i, l in enumerate(lineas, 1) if l.startswith(CABECERA_ACTA)]
    if len(inicios) != 1:
        raise SystemExit("ROJO: la cabecera del acta 166 aparece %d veces." % len(inicios))
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
        return None, "PARADA: %s aparece %d veces dentro del acta 166." % (
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


def claves_de_adjudicacion(lineas, inicio, fin, tope=40):
    """LA CIFRA NO SE TECLEA. Barre `6.1`, `6.2`, ... hacia arriba y devuelve las
    que aparecen EXACTAMENTE UNA VEZ en el cuerpo, parando en la primera que no
    aparece. El tope es un cortafuegos de bucle, no una cifra esperada."""
    claves = []
    for k in range(1, tope + 1):
        clave = "6.%d" % k
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        cuantas = len([i for i in range(inicio, fin + 1) if pat.match(lineas[i - 1])])
        if cuantas == 0:
            break
        claves.append((clave, cuantas))
    return claves


def main():
    print("=" * 78)
    print("VUELTA 168, TAREA 1: EL ACTA 167 ENTERA, REGISTRADA EN LA FORMA DE LA CASA")
    print("=" * 78)
    print("")

    lineas, inicio, fin = cuerpo_del_acta()
    print("A) EL CUERPO DEL ACTA, ACOTADO ANTES DE CONTAR NADA")
    print("   acta 167: docs/loop/ACTA_AUDITOR.md, lineas %d a %d" % (inicio, fin))
    print("")

    print("B) LAS ADJUDICACIONES, CONTADAS DEL ACTA Y NO TECLEADAS")
    print("   se barre 6.1 hacia arriba hasta la primera que no aparece.")
    claves = claves_de_adjudicacion(lineas, inicio, fin)
    for clave, cuantas in claves:
        if cuantas != 1:
            print("   PARADA: %s aparece %d veces." % (clave, cuantas))
            return 1
    print("   CIFRA adjudicaciones halladas: %d (%s)"
          % (len(claves), ", ".join(c for c, _ in claves)))
    if not claves:
        print("   PARADA: el acta 167 no trae ninguna adjudicacion 6.n.")
        return 1
    sin_glosa = [c for c, _ in claves if c not in QUE_HACE_ESTA_VUELTA or c not in VIA]
    if sin_glosa:
        print("   PARADA: sin glosa escrita en este instrumento: %s"
              % ", ".join(sin_glosa))
        return 1
    print("   todas tienen VIA y glosa escritas: SI")
    print("")

    print("C) LAS CAIDAS PROPIAS DEL AUDITOR, CONTADAS DEL ACTA Y NO TECLEADAS")
    print("   viven en la SECCION 3 del acta 167, igual que en la 166.")
    encontradas = [i for i in range(inicio, fin + 1)
                   if re.match(r"^\s*\*\*CAIDA \d[,.]", lineas[i - 1])]
    print("   CIFRA negritas 'CAIDA n' halladas en el acta 167: %d" % len(encontradas))
    if not encontradas:
        print("   PARADA: no hay ninguna caida propia que registrar.")
        return 1
    print("")

    n_adj, n_cai = len(claves), len(encontradas)
    titulo_entrada = titulo_de_la_entrada(n_adj, n_cai)
    print("D) EL TITULO DE LA ENTRADA, COMPUESTO CON LOS DOS CONTEOS")
    print("   %s" % titulo_entrada)
    print("   CONTRASTE, Y ES CONTRASTE Y NO FUENTE: el encargo de la 168 NO cifra")
    print("   las adjudicaciones del acta 167; solo nombra la 6.5 por su numero.")
    print("   CIFRA adjudicaciones contadas: %d | CIFRA caidas contadas: %d"
          % (n_adj, n_cai))
    print("")

    serie = SERIE.entradas()
    print("E) LA SERIE, RECOMPUTADA DE SUS DOS SEDES ANTES DE ESCRIBIR")
    for numero, rel, linea, titulo in serie:
        print("   R.%-3d %s:%-6d %s" % (numero, rel, linea, titulo[:88]))
    cols = SERIE.colisiones(serie)
    print("   CIFRA entradas: %d" % len(serie))
    print("   CIFRA colisiones: %d" % len(cols))
    print("   CIFRA huecos: %d" % len(SERIE.huecos(serie)))
    if cols:
        print("   PARADA: la serie trae colisiones. No se escribe encima de eso.")
        return 1
    ya = [(n, rel, ln) for n, rel, ln, t in serie if titulo_entrada in t]
    if ya:
        n, rel, ln = ya[0]
        print("YA ESTABA: la entrada vive como R.%d en %s:%d. No se toca." % (n, rel, ln))
        print("CIFRA entradas escritas: 0")
        return 0
    for rel in ("docs/PENDIENTES.md", "docs/plan/CORRECCIONES_A_APLICAR.md"):
        ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.exists(ruta):
            continue
        if titulo_entrada in io.open(ruta, encoding="utf-8").read():
            print("   PARADA: el titulo YA ESTA ESCRITO en %s pero la serie no lo ve."
                  % rel)
            return 1
    numero = SERIE.siguiente_libre(serie)
    print("   SIGUIENTE LIBRE, computado y no tecleado: R.%d" % numero)
    print("")

    print("F) LA SEDE, LEIDA DE LA REGLA ESCRITA Y NO SUPUESTA")
    todas = [i for i, l in enumerate(lineas, 1) if FRASE_DE_LA_SEDE in l]
    dentro = [i for i in todas if inicio <= i <= fin]
    print("   CIFRA veces que la frase de la sede aparece en el fichero entero: %d"
          % len(todas))
    print("   CIFRA veces que aparece DENTRO del acta 167: %d" % len(dentro))
    if len(todas) != 1:
        print("   PARADA: la frase de la sede no aparece exactamente una vez.")
        return 1
    print("   DECLARADO: el acta 167 NO repite la frase; la regla vive en la")
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
    print("G) LAS ADJUDICACIONES, LEIDAS HOY DE SU LINEA EN EL ACTA 167")
    adjudicaciones = []
    for clave, _c in claves:
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
    if len(adjudicaciones) != n_adj:
        print("   PARADA: se leyeron menos de las que se contaron.")
        return 1
    print("")

    print("H) LAS CAIDAS, LEIDAS HOY DE LA SECCION 3")
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

    print("I) EL REPARTO POR VIA, CONTADO Y NO TECLEADO")
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

    # LA FRASE DEL FUNDADOR SE COMPUTA, NO SE TECLEA. El `R.36` decia
    # "Ninguna de las nueve sube al fundador" porque el acta 166 no subia
    # ninguna; el acta 167 SI sube una (su 6.6, con la palabra "lo subo"), asi
    # que la frase tiene que salir del reparto y no de la memoria del que
    # escribe. Las vias que empiezan por "AL FUNDADOR" son las que cuentan.
    suben = [c for via in reparto for c in reparto[via] if via.startswith("AL FUNDADOR")]
    if not suben:
        linea_fundador = ("**Ninguna de las %s sube al fundador.**" % PALABRA[n_adj])
    elif len(suben) == 1:
        linea_fundador = (
            "**UNA DE LAS %s SUBE AL FUNDADOR, Y NO SE TECLEA QUE SEA UNA: SALE DEL\n"
            "REPARTO.** Es la `%s`, y el acta la sube con esas palabras. **Y YA ESTA\n"
            "CONTESTADA**, asi que esta entrada la registra como acatada y no como\n"
            "pendiente." % (PALABRA[n_adj].upper(), suben[0]))
    else:
        linea_fundador = (
            "**%s DE LAS %s SUBEN AL FUNDADOR** (%s), y la cifra sale del reparto."
            % (PALABRA[len(suben)].upper(), PALABRA[n_adj].upper(), ", ".join(suben)))
    print("   CIFRA que suben al fundador: %d (%s)"
          % (len(suben), ", ".join(suben) or "ninguna"))


    palabra_caidas = ("LA CAIDA PROPIA DEL AUDITOR, REGISTRADA"
                      if n_cai == 1 else
                      "LAS %s CAIDAS PROPIAS DEL AUDITOR, REGISTRADAS"
                      % PALABRA[n_cai].upper())

    trozos = []
    trozos.append(
        "\n---\n\n## R.%d. %s\n\n"
        "(Acta del auditor, vuelta 167, secciones 3 y 6; escrito en la vuelta 168,\n"
        "TAREA 1.)\n\n"
        "Por adicion, como `R.21` a `R.36`. **Corte de todas las cifras de esta entrada:\n"
        "4 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa\n"
        "`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes. La\n"
        "SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, leida hoy en\n"
        "`docs/loop/ACTA_AUDITOR.md:%d`, y se DECLARA que el acta 167 no la repite (la\n"
        "regla es de la casa, no de un acta suelta). Salida:\n"
        "`docs/loop/SALIDA_V168_T1_REGISTRO_ACTA_167.txt`.\n\n"
        % (numero, titulo_entrada, todas[0]))
    trozos.append(
        "**Y LAS DOS CIFRAS DEL TITULO TAMPOCO ESTAN TECLEADAS**, que es lo que la\n"
        "adjudicacion 5.7 del acta 165 firmo como metodo correcto y esta vuelta repite:\n"
        "se cuentan del acta (%d adjudicaciones `6.n` y %d negritas `CAIDA n` dentro del\n"
        "cuerpo acotado, lineas %d a %d) y de ahi sale el numeral en palabra, **incluida\n"
        "la concordancia**. **Y ESTA VUELTA LO PRUEBA MEJOR QUE LA ANTERIOR, porque las\n"
        "dos cifras BAJARON Y SUBIERON A LA VEZ:** el `R.36` registro nueve\n"
        "adjudicaciones y UNA caida, y esta registra %d y %d. Si el numeral estuviera\n"
        "tecleado, la herencia del instrumento lo habria arrastrado. **El encargo de la\n"
        "168 no cifra ninguna de las dos**, asi que no hay contraste que declarar contra\n"
        "el: manda el conteo, que es lo unico que hay.\n\n"
        % (n_adj, n_cai, inicio, fin, n_adj, n_cai))
    trozos.append(
        "**LAS %s ADJUDICACIONES, CON SU LINEA EN EL ACTA LEIDA HOY.** El titulo de\n"
        "cada una es LITERAL del fichero (localizado dentro del cuerpo del acta 167, no\n"
        "de cualquier acta); la glosa que sigue es prosa del ejecutor y va marcada como\n"
        "tal.\n\n%s\n"
        % (PALABRA[n_adj].upper(), "".join(bloques)))
    trozos.append(
        "**EL REPARTO POR VIA, CONTADO Y NO TECLEADO:** %s.\n%s\n\n"
        % (linea_reparto, linea_fundador))
    trozos.append(
        "**%s IGUAL QUE LAS DEL EJECUTOR**\n"
        "(precedente del `R.36`, escrito en la vuelta 167 por letra de su encargo, y\n"
        "heredado aqui sin reabrirlo). No son del ejecutor y no acumulan para sus\n"
        "rachas; se escriben aqui porque el registro de la casa no distingue de quien es\n"
        "la mano que cae. En el acta 167 viven en la **seccion 3**, igual que en la 166 y\n"
        "en la 165.\n\n%s\n" % (palabra_caidas, "".join(bloques_caidas)))
    trozos.append(
        "**LA DIFERENCIA ENTRE LAS DOS CAIDAS, Y ES LA QUE IMPORTA PARA EL ARCHIVO**\n"
        "(`EJECUTOR.md` 8 pide correccion declarada sin borrar el texto viejo). **LA\n"
        "`CAIDA 2` NO ARRASTRA NADA**: se resolvio dentro de su propia acta, ninguna\n"
        "clase se movio y no hay cifra publicada que corregir por ella. **LA `CAIDA 1`\n"
        "SI ARRASTRA, y por eso esta entrada no se limita a nombrarla:** su origen, la\n"
        "adjudicacion 6.9 del acta 166, salio del acta y llego a `docs/PENDIENTES.md`\n"
        "como `R.36` y al encargo de la vuelta 167 como su TAREA 5. **El remedio esta\n"
        "escrito en la adjudicacion 6.5 del acta 167 y esta misma TAREA 1 lo ejecuta:\n"
        "una nota fechada ADOSADA al final del `R.36`, por el carril del banco 9.10, sin\n"
        "reescribir ni una palabra de la glosa vieja.** Una correccion que tapa lo que\n"
        "corrige no se puede auditar.\n\n")
    trozos.append(
        "**LO QUE ESTE REGISTRO NO CIERRA.** La vara `P.5.1` sigue CONGELADA y ninguna de\n"
        "estas %s la estrecha ni la ensancha. **Ninguna clase del cribado se mueve por\n"
        "esta entrada:** la 6.3 retira la letra ciega DEL AUDITOR y deja la `A` del\n"
        "puesto 611 donde estaba, y retirar una letra propia no es adjudicar un par.\n"
        "**Ningun `estado` de `docs/plan/OPERACIONES.jsonl` se mueve por esta entrada**,\n"
        "que es justo lo que la 6.2 reserva. Y los pasos 2, 3 y 4 del\n"
        "`RECOMPUTO_3388.md` siguen sin recomputarse: no estan encargados y ampliarlo\n"
        "seria decidir su alcance.\n"
        % PALABRA[n_adj])
    texto = "".join(trozos)

    with io.open(sede, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)
    print("J) ESCRITO")
    print("   R.%d en %s" % (numero, sede_rel))
    print("   CIFRA adjudicaciones escritas: %d" % len(adjudicaciones))
    print("   CIFRA caidas escritas: %d" % len(caidas))
    print("   CIFRA entradas escritas: 1")
    print("")

    serie2 = SERIE.entradas()
    ve = [(n, rel, ln) for n, rel, ln, t in serie2 if titulo_entrada in t]
    print("K) LA SERIE, RECOMPUTADA DESPUES DE ESCRIBIR")
    print("   CIFRA entradas: %d" % len(serie2))
    print("   CIFRA colisiones: %d" % len(SERIE.colisiones(serie2)))
    print("   CIFRA huecos: %d" % len(SERIE.huecos(serie2)))
    print("   la serie VE la entrada nueva: %s"
          % ("SI, R.%d en %s:%d" % ve[0] if ve else "NO"))
    if not ve:
        print("   PARADA: escrita pero invisible para la serie. Revisar la cabecera.")
        return 1
    print("")
    print("VERDE: el acta 167 queda registrada como R.%d." % numero)
    return 0


# ---------------------------------------------------------------------------
# CASO POSITIVO POR MUTACION (EJECUTOR.md regla 1, "EL CASO ROJO SE PRUEBA POR
# MUTACION"). Se corre con `--mutar` y con el arnes de nombre propio
# `vuelta168_tarea1_mutacion_registro.py`, que es el que la bateria ve.
#
# CERO ESCRITURAS Y CERO FICHEROS: las actas de mentira se fabrican EN MEMORIA
# como listas de lineas. Nada toca `docs/PENDIENTES.md` ni
# `docs/loop/ACTA_AUDITOR.md`.
#
# QUE MIDE, Y POR QUE ES ESTO Y NO OTRA COSA. Lo que este instrumento CAMBIA
# respecto del de la vuelta 167 son DOS cosas: (a) el acta acotada es la 167, que
# trae MENOS adjudicaciones y MAS caidas que la 166, o sea que las dos cifras se
# mueven en sentidos opuestos a la vez; y (b) la LINEA DEL FUNDADOR del reparto
# deja de ser una frase fija ("Ninguna de las nueve sube al fundador") y pasa a
# computarse de las vias. Asi que lo que hay que poder tumbar es exactamente eso,
# ademas de todo lo que la 167 ya tumbaba: que el barrido siga a lo que el acta
# trae, que pare en el primer hueco, que NO confunda `6.1` con `6.10` a `6.14`, y
# que el titulo cambie solo cuando cambian los conteos, EN LAS DOS RAMAS.
#
# NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: los casos salen de correr las
# funciones reales sobre sujetos distintos, y la segunda pasada muta cada valor
# esperado y exige que el caso CAIGA.
# ---------------------------------------------------------------------------

FRONTERA_FALSA = "# ACTA DEL AUDITOR, VUELTA 168 (frontera de mentira)"
CABECERA_FALSA = CABECERA_ACTA + " (fabricada por la prueba de mutacion)"
PAT_CAIDA = re.compile(r"^\s*\*\*CAIDA \d[,.]")


def _acta_fabricada(adjudicaciones=9, caidas=1, sangria="  ", duplicar=None,
                    quitar=None, sin_cierre=False):
    """Un acta 167 DE MENTIRA, en memoria. Devuelve (lineas, inicio, fin)."""
    L = ["ruido de otra acta",
         "**6.1 ESTA NO CUENTA, VIVE FUERA DEL CUERPO.** ruido",
         "**CAIDA 1. ESTA TAMPOCO, VIVE FUERA DEL CUERPO.** ruido",
         "",
         CABECERA_FALSA,
         "cuerpo cualquiera",
         "",
         "## 3. MI CAIDA PROPIA, CON SU NOMBRE",
         ""]
    for k in range(1, caidas + 1):
        L.append("%s**CAIDA %d. TITULO DE LA CAIDA %d FABRICADA.** cuerpo"
                 % (sangria, k, k))
        L.append("")
    L.append("## 6. ADJUDICACIONES")
    L.append("")
    for k in range(1, adjudicaciones + 1):
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


def prueba_de_mutacion():
    print("=" * 78)
    print("VUELTA 168, TAREA 1: CASO POSITIVO POR MUTACION DEL REGISTRADOR DEL ACTA 167")
    print("=" * 78)
    print("")
    casos = []

    print("A) LA CIFRA DE ADJUDICACIONES SIGUE AL ACTA Y NO A UNA CONSTANTE")
    for n in (1, 5, 9, 14, 17):
        L, ini, fin = _acta_fabricada(adjudicaciones=n)
        visto = len(claves_de_adjudicacion(L, ini, fin))
        print("   acta fabricada con %d adjudicaciones -> el barrido ve %d" % (n, visto))
        casos.append(("A_con_%d_adjudicaciones_ve_%d" % (n, n), visto, n))
    print("")

    print("B) EL BARRIDO NO CONFUNDE 6.1 CON 6.10 A 6.14")
    L, ini, fin = _acta_fabricada(adjudicaciones=14)
    p1 = re.compile(r"^\s*\*\*%s " % re.escape("6.1"))
    casos.append(("B_el_patron_de_6_1_acierta_una_sola_vez",
                  len([i for i in range(ini, fin + 1) if p1.match(L[i - 1])]), 1))
    _h, e1 = titulo_de_la_negrita(L, ini, fin, p1, "6.1")
    casos.append(("B_y_su_titulo_se_lee_sin_error", e1 is None, True))
    print("   6.1 acierta %d vez dentro del cuerpo con 6.10 a 6.14 presentes"
          % len([i for i in range(ini, fin + 1) if p1.match(L[i - 1])]))
    print("")

    print("C) EL BARRIDO PARA EN EL PRIMER HUECO Y NO SALTA POR ENCIMA")
    Lq, iq, fq = _acta_fabricada(adjudicaciones=14, quitar="6.7")
    vistas = len(claves_de_adjudicacion(Lq, iq, fq))
    print("   acta de 14 con la 6.7 ausente -> el barrido ve %d (para en el hueco)"
          % vistas)
    casos.append(("C_para_en_el_hueco_y_ve_6", vistas, 6))
    Ld, id_, fd = _acta_fabricada(adjudicaciones=14, duplicar="6.5")
    dup = [c for c, n in claves_de_adjudicacion(Ld, id_, fd) if n != 1]
    print("   acta con la 6.5 duplicada -> claves con conteo distinto de 1: %s"
          % (", ".join(c for c in dup) or "ninguna"))
    casos.append(("C_la_duplicada_se_detecta", len(dup), 1))
    _h, e_dup = titulo_de_la_negrita(Ld, id_, fd, re.compile(r"^\s*\*\*6\.5 "), "6.5")
    casos.append(("C_duplicada_para", e_dup is not None, True))
    Ls, is_, fs = _acta_fabricada(adjudicaciones=14, sin_cierre=True)
    _h, e_sc = titulo_de_la_negrita(Ls, is_, fs, re.compile(r"^\s*\*\*6\.9 "), "6.9")
    print("   negrita sin cierre: %s" % (e_sc or "NO PARA"))
    casos.append(("C_negrita_sin_cierre_para", e_sc is not None, True))
    print("")

    print("D) EL ACOTADO DEJA FUERA EL RUIDO DE OTRAS ACTAS")
    L, ini, fin = _acta_fabricada()
    casos.append(("D_sin_acotar_hay_ruido_de_caidas", _cuenta_caidas(L, 1, len(L)), 3))
    casos.append(("D_acotado_no_lo_ve", _cuenta_caidas(L, ini, fin), 1))
    casos.append(("D_sin_acotar_la_6_1_esta_tres_veces",
                  len([i for i in range(1, len(L) + 1)
                       if re.match(r"^\s*\*\*6\.1 ", L[i - 1])]), 3))
    print("   sin acotar: %d negritas CAIDA | acotado: %d"
          % (_cuenta_caidas(L, 1, len(L)), _cuenta_caidas(L, ini, fin)))
    print("")
    print("E) EL TITULO SIGUE A LOS DOS CONTEOS Y NO A UNA CONSTANTE,")
    print("   Y CONCUERDA EN NUMERO EN SUS DOS RAMAS")
    for na, nc, esperado in ((6, 2, "seis"), (9, 1, "nueve"), (14, 3, "catorce")):
        t = titulo_de_la_entrada(na, nc)
        print("   (%d, %d) -> %s" % (na, nc, t))
        casos.append(("E_titulo_%d_%d_dice_%s" % (na, nc, esperado),
                      t.split()[3], esperado))
    casos.append(("E_la_rama_de_UNA_caida_va_en_singular",
                  "y la caida propia del acta" in titulo_de_la_entrada(9, 1), True))
    casos.append(("E_la_rama_de_DOS_caidas_va_en_plural",
                  "y las dos caidas propias del acta" in titulo_de_la_entrada(9, 2),
                  True))
    casos.append(("E_titulo_6_2_no_es_igual_al_de_6_1",
                  titulo_de_la_entrada(6, 2) == titulo_de_la_entrada(6, 1), False))
    casos.append(("E_titulo_6_2_no_es_igual_al_de_9_2",
                  titulo_de_la_entrada(6, 2) == titulo_de_la_entrada(9, 2), False))
    print("")

    print("F) UNA ADJUDICACION O UNA CAIDA SIN GLOSA TIENE QUE PARAR")
    L17, i17, f17 = _acta_fabricada(adjudicaciones=17, caidas=4)
    claves17 = [c for c, _n in claves_de_adjudicacion(L17, i17, f17)]
    sin_glosa = [c for c in claves17 if c not in QUE_HACE_ESTA_VUELTA]
    print("   claves del acta de 17: sin glosa escrita -> %s"
          % (", ".join(sin_glosa) or "ninguna"))
    casos.append(("F_las_adjudicaciones_sin_glosa_se_detectan", len(sin_glosa), 11))
    claves_c17 = [re.match(r"^\s*\*\*(CAIDA \d)[,.]", L17[i - 1]).group(1)
                  for i in range(i17, f17 + 1) if PAT_CAIDA.match(L17[i - 1])]
    sin_glosa_c = [c for c in claves_c17 if c not in QUE_HACE_CON_LA_CAIDA]
    casos.append(("F_las_caidas_sin_glosa_se_detectan", len(sin_glosa_c), 2))
    L6, i6, f6 = _acta_fabricada(adjudicaciones=6, caidas=2)
    casos.append(("F_las_seis_de_hoy_SI_tienen_glosa",
                  len([c for c, _n in claves_de_adjudicacion(L6, i6, f6)
                       if c not in QUE_HACE_ESTA_VUELTA]), 0))
    print("")
    print("G) EL ACTA DE VERDAD, LEIDA HOY")
    RL, ri, rf = cuerpo_del_acta()
    print("   cuerpo del acta 167: lineas %d a %d" % (ri, rf))
    reales = claves_de_adjudicacion(RL, ri, rf)
    n_adj = len(reales)
    n_cai = _cuenta_caidas(RL, ri, rf)
    print("   CIFRA adjudicaciones 6.n que trae la seccion 6: %d" % n_adj)
    print("   CIFRA caidas que trae la seccion 3: %d" % n_cai)
    casos.append(("G_el_acta_167_trae_SEIS_adjudicaciones", n_adj, 6))
    casos.append(("G_cada_una_aparece_una_sola_vez",
                  len([c for c, n in reales if n != 1]), 0))
    casos.append(("G_el_acta_167_trae_DOS_caidas", n_cai, 2))
    todas = [i for i, l in enumerate(RL, 1) if FRASE_DE_LA_SEDE in l]
    casos.append(("G_la_frase_de_la_sede_esta_una_vez_en_el_fichero", len(todas), 1))
    casos.append(("G_y_cero_veces_dentro_del_acta_167",
                  len([i for i in todas if ri <= i <= rf]), 0))
    patrones = [(re.compile(r"^\s*\*\*%s " % re.escape(c)), c) for c, _n in reales]
    patrones += [(re.compile(r"^\s*\*\*CAIDA %d[,.]" % k), "CAIDA %d" % k)
                 for k in range(1, n_cai + 1)]
    sin_error = 0
    for pat, et in patrones:
        _h, e = titulo_de_la_negrita(RL, ri, rf, pat, et)
        if e is None:
            sin_error += 1
    print("   CIFRA negritas que se leen sin error: %d de %d"
          % (sin_error, len(patrones)))
    casos.append(("G_las_ocho_negritas_se_leen_sin_error", sin_error, 8))
    casos.append(("G_el_titulo_que_saldra_dice_seis_y_dos_en_plural",
                  titulo_de_la_entrada(n_adj, n_cai),
                  "Registro de las seis adjudicaciones y las dos caidas propias "
                  "del acta de la vuelta 167"))
    # LA RAMA NUEVA DE ESTA VUELTA: la linea del fundador se computa. Se prueba
    # sobre las vias REALES de este instrumento y sobre un reparto sin ninguna
    # via de fundador, para que las DOS ramas queden ejercidas.
    suben_reales = sorted(c for c, v in VIA.items() if v.startswith("AL FUNDADOR"))
    casos.append(("G_las_vias_reales_suben_UNA_al_fundador", len(suben_reales), 1))
    casos.append(("G_y_la_que_sube_es_la_6_6", ",".join(suben_reales), "6.6"))
    casos.append(("G_sin_via_de_fundador_no_sube_ninguna",
                  len([c for c, v in {"6.1": "EN MEDICION"}.items()
                       if v.startswith("AL FUNDADOR")]), 0))
    print("")
    print("H) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("I) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        else:
            mutado = str(esperado) + "_mutado"
        cae = (real != mutado)
        print("   %-52s %s   (esperado mutado=%r)"
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
