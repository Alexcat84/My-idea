# -*- coding: utf-8 -*-
r"""vuelta169_tarea1_registrar_acta168.py . TAREA 1.a de la vuelta 169.

REGISTRA EN LA FORMA DE LA CASA (`R.N`) EL ACTA 168 ENTERA: SUS ADJUDICACIONES
`6.n` Y LAS CAIDAS PROPIAS DEL AUDITOR de su seccion 3. Hereda la maquina de
`vuelta168_tarea1_registrar_acta167.py` SIN tocarle el mecanismo, y la maquina es
la que importa: NINGUNA CIFRA SE TECLEA. El numero de la entrada lo computa
`serie_de_registros.py` recomputando la serie de sus DOS sedes; el conteo de
adjudicaciones se barre del acta parando en el primer hueco; el conteo de caidas
se cuenta de las negritas `CAIDA n` del cuerpo acotado; y el numeral en palabra
del titulo, con su concordancia, sale de esos dos conteos.

QUE CAMBIA RESPECTO DEL INSTRUMENTO DE LA VUELTA 168:

  (1) EL CUERPO ACOTADO pasa del acta 167 al acta 168 (`CABECERA_ACTA`), que es
      hoy la ULTIMA del fichero: `fin` cae en el final del fichero y no en la
      cabecera siguiente.
  (2) LAS DOS CIFRAS VUELVEN A MOVERSE, Y ESTA VEZ LAS DOS EN SENTIDOS DISTINTOS
      QUE LA VEZ ANTERIOR: el `R.37` registro SEIS adjudicaciones y DOS caidas;
      el acta 168 trae DIEZ adjudicaciones y DOS caidas. La rama del plural de
      "caidas propias" se vuelve a escoger sola, y el numeral de las
      adjudicaciones sube de "seis" a "diez" sin que nadie lo teclee. Si el
      numeral estuviera tecleado, la herencia lo habria arrastrado.
  (3) EL BARRIDO DE `6.n` TIENE QUE LLEGAR A `6.10` SIN CONFUNDIRLA CON `6.1`,
      que es exactamente lo que el patron `^\s*\*\*6\.1 ` (con el espacio al
      final) impide, y lo que el arnes hermano prueba por mutacion.

USO:  python scripts/loop/vuelta169_tarea1_registrar_acta168.py
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402

RAIZ = SERIE.RAIZ
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 168"

FRASE_DE_LA_SEDE = "la sede por defecto es `docs/PENDIENTES.md`"

PALABRA = {1: "una", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis",
           7: "siete", 8: "ocho", 9: "nueve", 10: "diez", 11: "once",
           12: "doce", 13: "trece", 14: "catorce", 15: "quince",
           16: "dieciseis", 17: "diecisiete", 18: "dieciocho",
           19: "diecinueve", 20: "veinte"}


def titulo_de_la_entrada(n_adj, n_cai):
    """El titulo, con sus dos numerales COMPUTADOS y no tecleados."""
    cola = ("la caida propia" if n_cai == 1
            else "las %s caidas propias" % PALABRA[n_cai])
    return ("Registro de las %s adjudicaciones y %s del acta de la vuelta 168"
            % (PALABRA[n_adj], cola))


VIA = {
    "6.1": "EJECUTADA",
    "6.2": "EJECUTADA",
    "6.3": "EJECUTADA",
    "6.4": "EJECUTADA",
    "6.5": "EJECUTADA",
    "6.6": "SIN TOCAR NADA",
    "6.7": "EJECUTADA",
    "6.8": "SIN TOCAR NADA",
    "6.9": "EJECUTADA",
    "6.10": "SIN TOCAR NADA",
}

QUE_HACE_ESTA_VUELTA = {
    "6.1": ("EJECUTADA, TAREA 1.b de esta vuelta. La bateria se re corrio ENTERA y su "
            "salida se escribio en `docs/loop/SALIDA_V168_T3_BATERIA_CIERRE.txt`, que "
            "abria esta vuelta con CERO BYTES y SIN COMMITEAR (medido y sellado antes "
            "de la primera operacion en `docs/loop/SALIDA_V169_APERTURA.txt`, seccion "
            "D). El fichero NO se borro ni se reescribio a mano: se sobrescribio con la "
            "corrida de verdad. Y al pie de la seccion 3.c del reporte de la 168 va la "
            "nota fechada adosada, por el carril del banco 9.10, que dice que la tabla "
            "se publico antes que su fuente, que la celda `72` era una prediccion "
            "correcta y no una medicion, y que hoy la fuente existe. NINGUNA PALABRA "
            "VIEJA SE BORRA."),
    "6.2": ("EJECUTADA, TAREA 2 de esta vuelta, y ahora si autorizada por nombre. "
            "`scripts/loop/vuelta166_tarea3_mutacion_retrato.py` se re ancla con la "
            "misma vara del 3.b de la vuelta 168, EL NUMERO CAMBIA Y EL FILO NO: (a) la "
            "constante `TRECE VECES` de sus dos casos sale del computo, igual que "
            "`cuantas`; (b) la mutacion deja de estar clavada al texto vivo y muta la "
            "palabra que el propio instrumento acaba de leer, CON UNA GUARDA NUEVA QUE "
            "CAE SI EL REPLACE NO CAMBIA NADA, que es el modo de fallo que dejo la "
            "guarda muda. Ningun caso se quita y ninguna comprobacion se afloja."),
    "6.3": ("EJECUTADA, TAREA 1.c de esta vuelta, POR ADICION Y SIN BORRAR. Al parrafo "
            "LA CAUSA, MEDIDA del reporte de la 168 se le adosa la medicion del acta: "
            "el arnes del retrato NACIO ROJO EN SU PROPIO COMMIT `33fe1380`, de la "
            "vuelta 166, y la vuelta 167 NO movio esa fila. La frase que culpaba a la "
            "167 se queda entera y visible. Y la leccion viaja con ella porque es mas "
            "grande que este arnes: UN ARNES QUE SE ESCRIBE CONTRA EL DOCUMENTO DE "
            "ANTES DE LA CORRECCION, Y SE COMMITEA JUNTO CON LA CORRECCION, NACE "
            "MUERTO; la unica forma de cazarlo es correrlo DESPUES de escribir, en el "
            "mismo acto."),
    "6.4": ("EJECUTADA, TAREA 3 de esta vuelta. El alcance de la clausula 4 de "
            "`OP-I-01` no se improvisa: sale del disparador que la propia clausula "
            "nombra, `docs/plan/08_VERIFICACION.md`, cuyo paso 4 se lee HOY de su linea "
            "y se comprueba que sigue diciendo 'cada racimo y cada acto ... con su "
            "cobertura al lado'. DENTRO y por tanto ejecutable: las entradas de tipo "
            "`acto` y `racimo`, re medidas sobre las componentes del paso 3 con el "
            "resolutor delante por `P.1`. FUERA, porque el disparador no las nombra: "
            "`familia_de_ids`, `figura`, `defecto` y `dominio`, que NO se recomputan y "
            "NO se inventan, sino que se DECLARAN con su cifra de hoy."),
    "6.5": ("EJECUTADA, TAREA 4 de esta vuelta, y desencadenada por la 6.4 como el acta "
            "manda. `cada nomina afectada` deja de ser indefinido: son las nominas que "
            "el paso 4 del disparador re-mide, con su cobertura al lado por el banco "
            "9.26. No hay doctrina nueva: hay una sede citada."),
    "6.6": ("SE ACATA SIN TOCAR NADA. `OP-M-02-MEDIOS` y `OP-M-02-ADMIT` quedan "
            "CUMPLIDAS POR CONSUNCION y esta vuelta NO las ejecuta ni las reabre. Su "
            "divergencia con el superviviente que la ficha adjudico el 12 ago queda "
            "DECLARADA y no deshecha, por el mismo criterio con que la vuelta 64 la "
            "declaro: el tramo ya ejecutado manda sobre la adjudicacion previa, y "
            "borrar la adjudicacion vieja taparia el desacuerdo."),
    "6.7": ("EJECUTADA, TAREA 5 de esta vuelta. Las dos quedan desbloqueadas y el campo "
            "`estado` NO se toca: sigue diciendo `LISTA` en las seis `OP-D-*` y la vara "
            "es el instrumento, por la decision del fundador del 4 sep 2026. LO QUE "
            "ESTA VUELTA MIDE Y TRAE, y no estaba previsto en el encargo: el lote de "
            "sales roadmap ESTA LEIDO DESDE EL 14 ago 2026 como `LD-66` a `LD-70` en "
            "`docs/plan/LD_SALES_ROADMAP.md`, y las SEIS nominas de `OP-L-02` dan hoy "
            "cobertura COMPLETA, cero pares sin veredicto, con el resolutor delante."),
    "6.8": ("SE ACATA SIN TOCAR NADA. El discutible de la TAREA 4 de la vuelta 168 "
            "queda adjudicado a favor del ejecutor y esta vuelta no lo reabre: "
            "`scripts/loop/vuelta150_3_relectura_expediente.py` NO se toca, `OP-V-01` "
            "sigue midiendose HECHA SIN NINGUNA PRUEBA por el instrumento, y que siga "
            "saliendo en rojo DESPUES de escribir su prueba por cita es la senal de que "
            "el arreglo se hizo bien."),
    "6.9": ("EJECUTADA, TAREA 1.c de esta vuelta, por adicion y en una linea. A la traza "
            "del fichero de componentes del reporte de la 168 se le anade la subida que "
            "faltaba, `801c59f9` con 335, y la frase 'trazada commit a commit' se "
            "corrige por lo que de verdad es: LOS CUATRO PUNTOS EN QUE LA CIFRA CAMBIA "
            "HACIA ABAJO. No mueve ninguna cifra: es precision, y la palabra vieja se "
            "queda."),
    "6.10": ("SE ACATA SIN TOCAR NADA, Y ESTA VUELTA LA MANTIENE. Ninguna clase se movio "
             "por el acta 168 y ninguna se mueve por esta vuelta: "
             "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` NO se toca, ni siquiera al cerrar la "
             "cobertura de las seis nominas de `OP-L-02`, porque una lectura dirigida no "
             "entra en la cola y no mueve su marcador, que es su definicion escrita."),
}

QUE_HACE_CON_LA_CAIDA = {
    "CAIDA 1": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. El auditor imprimio la columna `clase` de "
                "los diez pares resueltos del lote de sales roadmap y solo despues se "
                "planteo usar ese lote como sujeto de ciega. LO QUE ESTA VUELTA ANADE, "
                "medido y no supuesto: ese lote no solo estaba quemado como sujeto de "
                "ciega, es que ADEMAS YA ESTABA LEIDO desde el 14 ago 2026 como `LD-66` "
                "a `LD-70`. O sea que la caida es mas barata de lo que su propio autor "
                "creyo, porque el lote no era nomina limpia para nadie. Lo que ensena "
                "sigue en pie con las palabras del acta: mirar es irreversible, y por "
                "eso se mira en el orden que deja opciones."),
    "CAIDA 2": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. Y SE REGISTRA AUNQUE NO LLEGARA A "
                "PUBLICARSE, que es exactamente lo que la hace valiosa: el auditor conto "
                "la serie con un `grep` sobre UNA sede, le salio 27 y 28 contra el 28 y "
                "29 del reporte, y la cazo corriendo el instrumento de la casa ANTES de "
                "escribir. NO HAY CIFRA PUBLICADA QUE CORREGIR POR ELLA y esta entrada "
                "no declara ninguna correccion en su nombre. Lo que ensena, en sus "
                "palabras: un `grep` sobre una sede no es un censo de una serie que la "
                "casa reparte en dos. Y esta misma TAREA lo vuelve a obedecer: el numero "
                "`R.N` de esta entrada lo computa `serie_de_registros.py` sobre las DOS "
                "sedes, no un `grep`."),
}


def cuerpo_del_acta():
    """El texto del acta 168, acotado por su cabecera y por el final del fichero
    o la cabecera siguiente."""
    texto = io.open(ACTA, encoding="utf-8").read()
    lineas = texto.split("\n")
    inicios = [i for i, l in enumerate(lineas, 1) if l.startswith(CABECERA_ACTA)]
    if len(inicios) != 1:
        raise SystemExit("ROJO: la cabecera del acta 168 aparece %d veces." % len(inicios))
    inicio = inicios[0]
    siguientes = [i for i, l in enumerate(lineas, 1)
                  if i > inicio and re.match(r"^# ACTA (DE LA VUELTA|DEL AUDITOR)", l)]
    fin = min(siguientes) - 1 if siguientes else len(lineas)
    return lineas, inicio, fin


def titulo_de_la_negrita(lineas, inicio, fin, patron, etiqueta):
    """EL TITULO ES LA NEGRITA DE APERTURA, NI UNA PALABRA MAS, con la LINEA EN
    BLANCO como frontera."""
    aciertos = [i for i in range(inicio, fin + 1) if patron.match(lineas[i - 1])]
    if len(aciertos) != 1:
        return None, "PARADA: %s aparece %d veces dentro del acta 168." % (
            etiqueta, len(aciertos))
    ln = aciertos[0]
    acumulado = ""
    j = ln - 1
    cierre = -1
    while j < fin:
        trozo = lineas[j].strip()
        if not trozo and acumulado:
            break
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
    """LA CIFRA NO SE TECLEA. Barre `6.1`, `6.2`, ... hacia arriba y para en la
    primera que no aparece. El espacio final del patron es el que impide que
    `6.1` se coma a `6.10`."""
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
    print("VUELTA 169, TAREA 1.a: EL ACTA 168 ENTERA, REGISTRADA EN LA FORMA DE LA CASA")
    print("=" * 78)
    print("")

    lineas, inicio, fin = cuerpo_del_acta()
    print("A) EL CUERPO DEL ACTA, ACOTADO ANTES DE CONTAR NADA")
    print("   acta 168: docs/loop/ACTA_AUDITOR.md, lineas %d a %d" % (inicio, fin))
    print("")

    print("B) LAS ADJUDICACIONES, CONTADAS DEL ACTA Y NO TECLEADAS")
    claves = claves_de_adjudicacion(lineas, inicio, fin)
    for clave, cuantas in claves:
        if cuantas != 1:
            print("   PARADA: %s aparece %d veces." % (clave, cuantas))
            return 1
    print("   CIFRA adjudicaciones halladas: %d (%s)"
          % (len(claves), ", ".join(c for c, _ in claves)))
    if not claves:
        print("   PARADA: el acta 168 no trae ninguna adjudicacion 6.n.")
        return 1
    sin_glosa = [c for c, _ in claves if c not in QUE_HACE_ESTA_VUELTA or c not in VIA]
    if sin_glosa:
        print("   PARADA: sin glosa escrita en este instrumento: %s"
              % ", ".join(sin_glosa))
        return 1
    print("   todas tienen VIA y glosa escritas: SI")
    print("")

    print("C) LAS CAIDAS PROPIAS DEL AUDITOR, CONTADAS DEL ACTA Y NO TECLEADAS")
    encontradas = [i for i in range(inicio, fin + 1)
                   if re.match(r"^\s*\*\*CAIDA \d[,.]", lineas[i - 1])]
    print("   CIFRA negritas 'CAIDA n' halladas en el acta 168: %d" % len(encontradas))
    if not encontradas:
        print("   PARADA: no hay ninguna caida propia que registrar.")
        return 1
    print("")

    n_adj, n_cai = len(claves), len(encontradas)
    titulo_entrada = titulo_de_la_entrada(n_adj, n_cai)
    print("D) EL TITULO DE LA ENTRADA, COMPUESTO CON LOS DOS CONTEOS")
    print("   %s" % titulo_entrada)
    print("   CONTRASTE, Y ES CONTRASTE Y NO FUENTE: el encargo de la 169 nombra")
    print("   'sus adjudicaciones 6.1 a 6.10', o sea DIEZ. Manda el conteo.")
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
    print("   CIFRA veces que aparece DENTRO del acta 168: %d" % len(dentro))
    if len(todas) != 1:
        print("   PARADA: la frase de la sede no aparece exactamente una vez.")
        return 1
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

    print("G) LAS ADJUDICACIONES, LEIDAS HOY DE SU LINEA EN EL ACTA 168")
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

    suben = [c for via in reparto for c in reparto[via] if via.startswith("AL FUNDADOR")]
    if not suben:
        linea_fundador = "**Ninguna de las %s sube al fundador.**" % PALABRA[n_adj]
    elif len(suben) == 1:
        linea_fundador = (
            "**UNA DE LAS %s SUBE AL FUNDADOR, Y NO SE TECLEA QUE SEA UNA: SALE DEL\n"
            "REPARTO.** Es la `%s`." % (PALABRA[n_adj].upper(), suben[0]))
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
        "(Acta del auditor, vuelta 168, secciones 3 y 6; escrito en la vuelta 169,\n"
        "TAREA 1.a.)\n\n"
        "Por adicion, como `R.21` a `R.37`. **Corte de todas las cifras de esta entrada:\n"
        "4 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa\n"
        "`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes,\n"
        "que es exactamente la vara que la `CAIDA 2` de esta misma acta enseno a usar.\n"
        "La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, leida hoy\n"
        "en `docs/loop/ACTA_AUDITOR.md:%d`. Salida:\n"
        "`docs/loop/SALIDA_V169_T1_REGISTRO_ACTA_168.txt`.\n\n"
        % (numero, titulo_entrada, todas[0]))
    trozos.append(
        "**Y LAS DOS CIFRAS DEL TITULO TAMPOCO ESTAN TECLEADAS:** se cuentan del acta\n"
        "(%d adjudicaciones `6.n` y %d negritas `CAIDA n` dentro del cuerpo acotado,\n"
        "lineas %d a %d) y de ahi sale el numeral en palabra, **incluida la\n"
        "concordancia**. **EL `R.37` REGISTRO SEIS Y DOS; ESTE REGISTRA %d Y %d**, y el\n"
        "numeral de las adjudicaciones subio solo. **Y ESTA VUELTA PRUEBA ADEMAS EL\n"
        "BORDE QUE NINGUNA ANTERIOR TOCO:** el acta 168 es la primera que llega a\n"
        "`6.10`, y el barrido tiene que contarla SIN confundirla con `6.1`. Lo que lo\n"
        "impide es el espacio final del patron `^\\s*\\*\\*6\\.1 `, y el arnes hermano lo\n"
        "prueba por mutacion en vez de afirmarlo.\n\n"
        % (n_adj, n_cai, inicio, fin, n_adj, n_cai))
    trozos.append(
        "**LAS %s ADJUDICACIONES, CON SU LINEA EN EL ACTA LEIDA HOY.** El titulo de\n"
        "cada una es LITERAL del fichero (localizado dentro del cuerpo del acta 168, no\n"
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
        "la mano que cae. En el acta 168 viven en la **seccion 3**.\n\n%s\n"
        % (palabra_caidas, "".join(bloques_caidas)))
    trozos.append(
        "**LO QUE ESTE REGISTRO NO CIERRA, Y SE DICE ANTES DE QUE NADIE LO SUPONGA.**\n"
        "La vara `P.5.1` sigue CONGELADA y ninguna de estas %s la estrecha ni la\n"
        "ensancha. **Ninguna clase del cribado se mueve por esta entrada** y\n"
        "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no se toca, que es lo que la `6.10`\n"
        "reserva. **Ningun `estado` de `docs/plan/OPERACIONES.jsonl` se mueve por esta\n"
        "entrada**: el campo sigue jubilado como historico y la vara del trabajo\n"
        "pendiente sigue siendo `scripts/loop/vuelta150_3_relectura_expediente.py`.\n"
        "**Y las dos `OP-M-02` siguen sin ejecutarse**, por la `6.6`.\n"
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
    print("VERDE: el acta 168 queda registrada como R.%d." % numero)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
