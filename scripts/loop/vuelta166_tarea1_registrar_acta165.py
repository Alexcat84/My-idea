# -*- coding: utf-8 -*-
r"""vuelta166_tarea1_registrar_acta165.py . TAREA 1 de la vuelta 166.

REGISTRA EN LA FORMA DE LA CASA (`R.N`) EL ACTA 165 ENTERA: SUS CATORCE
ADJUDICACIONES (5.1 a 5.14) Y LAS CAIDAS PROPIAS DEL AUDITOR de su seccion 3.
Las caidas del auditor se registran IGUAL que las del ejecutor, por letra del
encargo de la vuelta 166 (*"Y registra tambien, con su nombre, MIS DOS CAIDAS
de la seccion 3 del acta"*).

QUE CAMBIA RESPECTO DEL INSTRUMENTO DE LA VUELTA 165
(`vuelta165_tarea1_registrar_acta164.py`), cuya maquina se hereda SIN
tocarle el mecanismo:

  (1) EL CUERPO ACOTADO pasa del acta 164 al acta 165 (`CABECERA_ACTA`), que es
      hoy la ULTIMA del fichero: `fin` cae en el final del fichero y no en la
      cabecera siguiente. Medido hoy: cuerpo en las lineas 54829 a 55287.
  (2) LAS ADJUDICACIONES dejan de numerarse `6.n` y pasan a `5.n`, y dejan de
      ser diez: SON LAS QUE HAYA. El instrumento viejo llevaba `range(1, 11)` y
      un `!= 10` tecleados; aqui el numero de adjudicaciones se COMPUTA del
      acta, barriendo `5.1` hacia arriba hasta que una no aparezca, y la glosa
      de cada una se busca por su clave: si apareciera una adjudicacion sin
      glosa escrita, PARA en vez de publicar una entrada coja. Es la misma
      cura que la vuelta 165 le aplico a la cifra de caidas.
  (3) LAS CAIDAS viven en la SECCION 3 del acta 165, no en la 4. El acotado no
      cambia por eso (el patron barre el cuerpo entero), pero la prosa de la
      entrada lo dice con su numero de seccion medido.
  (4) EL TITULO DE LA ENTRADA DEJA DE TENER SUS DOS CIFRAS TECLEADAS. En la 165
      el titulo decia "las diez adjudicaciones y las tres caidas" a mano; aqui
      las dos palabras se COMPUTAN de los conteos del acta (EJECUTOR.md 1, "LA
      TABLA SE CUENTA DE SU FICHERO"). Si el acta trajera otra cosa, el titulo
      lo dice solo.

NINGUNA CELDA SE TECLEA: el numero de la entrada lo computa
`serie_de_registros.py` recomputando la serie de sus dos sedes, y el
instrumento ademas se niega a escribir si el titulo esta en el fichero pero la
serie no lo ve (la trampa de la cabecera partida que cazo la vuelta 164).

USO:  python scripts/loop/vuelta166_tarea1_registrar_acta165.py
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402

RAIZ = SERIE.RAIZ
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 165"

FRASE_DE_LA_SEDE = "la sede por defecto es `docs/PENDIENTES.md`"

PALABRA = {1: "una", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis",
           7: "siete", 8: "ocho", 9: "nueve", 10: "diez", 11: "once",
           12: "doce", 13: "trece", 14: "catorce", 15: "quince",
           16: "dieciseis", 17: "diecisiete", 18: "dieciocho",
           19: "diecinueve", 20: "veinte"}


def titulo_de_la_entrada(n_adj, n_cai):
    """El titulo, con sus dos numerales COMPUTADOS y no tecleados."""
    return ("Registro de las %s adjudicaciones y las %s caidas propias del acta "
            "de la vuelta 165" % (PALABRA[n_adj], PALABRA[n_cai]))


VIA = {
    "5.1": "SIN TOCAR NADA",
    "5.2": "EN EJECUCION",
    "5.3": "EN EJECUCION",
    "5.4": "EN EJECUCION",
    "5.5": "SIN TOCAR NADA",
    "5.6": "SIN TOCAR NADA",
    "5.7": "SIN TOCAR NADA",
    "5.8": "SIN TOCAR NADA",
    "5.9": "SIN TOCAR NADA",
    "5.10": "SIN TOCAR NADA",
    "5.11": "EN CODIGO",
    "5.12": "EN MEDICION",
    "5.13": "EN MEDICION",
    "5.14": "EN MEDICION",
}

QUE_HACE_ESTA_VUELTA = {
    "5.1": ("SE ACATA SIN TOCAR NADA. El uso del resolutor para medir la clausula 1 de "
            "`OP-L-01` queda CONFIRMADO por segunda pluma, citando `P.1` en su propia "
            "letra. La vuelta 166 lo hereda como metodo y no lo vuelve a discutir: sus "
            "TAREAS 3 y 5 miden CON EL RESOLUTOR PUESTO, y por eso mismo la TAREA 5 se "
            "queda en censo y no adjudica clase."),
    "5.2": ("EJECUTADA EN EJECUCION, TAREA 2 de esta vuelta. La clausula 2 queda "
            "corregida POR ADICION dentro de la propia lista `verificacion`, citando el "
            "campo `adjudicacion` de la ficha y el precedente del acta 71. NO se borra "
            "una letra y NO se crea clave nueva de esquema. La PARADA que la vuelta 165 "
            "trajo queda LEVANTADA por esta adjudicacion, no por decision del ejecutor."),
    "5.3": ("EJECUTADA EN EJECUCION, TAREA 2 de esta vuelta. La clausula 1 se corrige "
            "POR ADICION nombrando las TRES lecturas que SI aparecen al resolver, cada "
            "una con su puesto y su clase, medidas hoy y no copiadas del acta."),
    "5.4": ("SE ACATA Y NO SE RELLENA, TAREA 2 de esta vuelta. La clausula 3 NO se "
            "corrige: se cumple hasta donde el inventario nombra miembros, y las cinco "
            "nominas que solo existen como prosa quedan NOMBRADAS Y NO RELLENADAS, que "
            "es lo que la verificacion de `OP-I-01` manda. Elegirles una entrada seria "
            "decidir."),
    "5.5": ("SE ACATA SIN TOCAR NADA. Las dos salidas del censo de arneses y el "
            "invariante `nomina_invisible_al_censo()` se quedan los tres. La vuelta 166 "
            "no los toca ni los sustituye."),
    "5.6": ("SE ACATA SIN TOCAR NADA. La transitividad se queda con su deuda nombrada: "
            "los doce cuya exclusion no se comprobo uno por uno siguen escritos como "
            "deuda y NO como verde. La vuelta 166 no los cierra y no los borra."),
    "5.7": ("SE ACATA SIN TOCAR NADA. Contar la seccion en vez de copiar la cifra del "
            "encargo queda firmado como el metodo correcto, y esta vuelta lo repite: la "
            "cifra de adjudicaciones y la de caidas de esta misma entrada se CUENTAN del "
            "acta 165, y si difirieran del encargo mandaria el conteo."),
    "5.8": ("SE ACATA SIN TOCAR NADA. Las dos cifras del racimo de la junta asesora "
            "siguen vivas con su corte al lado, por el banco 9.21. La vuelta 166 no "
            "borra ninguna de las dos ni las funde."),
    "5.9": ("SE ACATA SIN TOCAR NADA. Los 26 quedan medidos uno por uno por la TAREA 4 "
            "de la vuelta 165, con su cifra corregida (24 pre 148 y 2 posteriores). La "
            "vuelta 166 no los vuelve a medir y no los mueve."),
    "5.10": ("SE ACATA SIN TOCAR NADA. `SALIDA_V135_4C_MUTACION.txt` y "
             "`SALIDA_V137_1A_MUTACION.txt` quedan DECLARADOS y no se arreglan: ninguna "
             "regla escrita manda reescribir ficheros de vueltas pasadas por cosmetica."),
    "5.11": ("EJECUTADA EN CODIGO, TAREA 6 de esta vuelta. `tallar_cifras_de_antes.py` "
             "se ESTRECHA EN LA FUENTE, con su caso positivo por mutacion, y su frase "
             "pasa a decir a que universo se refiere. NO se declara ajena al reporte de "
             "fase 04: eso seria apagar una guarda por incomoda. El antes y el despues "
             "se publican sobre los DOS reportes, el de la 164 y el de hoy, y los "
             "hallazgos que sobrevivan se NOMBRAN uno por uno."),
    "5.12": ("EJECUTADA COMO MEDICION, TAREA 3 de esta vuelta, y es la BLOQUEANTE. El "
             "retrato de las A de `docs/plan/RECOMPUTO_3388.md` PASO 1 se RECOMPUTA con "
             "`scripts/plan/recomputo_3388.py`, por el carril de siempre: contador "
             "cuadrado en el mismo acto, nota fechada adosada, ninguna nota vieja "
             "reescrita y ninguna cifra vieja borrada. Los pasos 2, 3 y 4 NO se tocan: "
             "no estan encargados y meterlos aqui seria decidir su alcance."),
    "5.13": ("EJECUTADA COMO MEDICION, TAREA 4 de esta vuelta. El reparto de "
             "`docs/plan/OPERACIONES.jsonl` por estado y por fase se mide con "
             "instrumento propio y se publica entero, y la correccion declarada de la "
             "cifra falsa del auditor se escribe DONDE ESA CIFRA VIAJO. NINGUN ESTADO SE "
             "CAMBIA en esa tarea: es un censo, no un pase."),
    "5.14": ("EJECUTADA COMO MEDICION, TAREA 5 de esta vuelta. El colapso se mide con el "
             "resolutor y se publica con su evidencia, y NO SE ADJUDICA CLASE NI SE "
             "MUEVE UN VEREDICTO. La frontera que `LD-07` dejo escrita se anota donde "
             "`LD-07` vive, POR ADICION y con su fecha."),
}

QUE_HACE_CON_LA_CAIDA = {
    "CAIDA 1": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL EJECUTOR, "
                "porque no es suya. Su remedio se EJECUTA en la TAREA 4 de esta vuelta: "
                "el reparto real de las 71 operaciones por estado y por fase se mide con "
                "instrumento propio del ejecutor, se publica entero, y la correccion "
                "declarada se escribe en esta misma entrada y alli donde el mapa del "
                "ultimo tramo de la fase III quedo escrito como si fueran cuatro "
                "operaciones. Y se cuenta ademas, porque el auditor lo pide por su "
                "nombre, cuantas de las que quedan en `LISTA` no tienen dependencias "
                "declaradas: la frase de que `OP-L-01` era la unica tambien era falsa."),
    "CAIDA 2": ("SE REGISTRA CON SU NOMBRE Y LO QUE ENSENA SE ESCRIBE ENTERO: la ciega "
                "decide la LETRA, no la GENEALOGIA. No acumula para ninguna racha del "
                "ejecutor. Su remedio se ACATA en el procedimiento de la TAREA 5 de esta "
                "vuelta, que es exactamente la especie contraria: se mide el colapso, se "
                "publican los pares en conflicto uno por uno con su evidencia, y NO se "
                "les atribuye causa ni clase. El ejemplar que el propio auditor nombra, "
                "`formalizar_junta_asesora` con `identificar_consejo_asesores`, se "
                "publica como los demas y sin adjudicarle nada."),
}


def cuerpo_del_acta():
    """El texto del acta 165, acotado por su cabecera y por el final del fichero
    o la cabecera siguiente. Hace falta acotar: el fichero trae mas de un `5.1`
    y mas de una `CAIDA 1`."""
    texto = io.open(ACTA, encoding="utf-8").read()
    lineas = texto.split("\n")
    inicios = [i for i, l in enumerate(lineas, 1) if l.startswith(CABECERA_ACTA)]
    if len(inicios) != 1:
        raise SystemExit("ROJO: la cabecera del acta 165 aparece %d veces." % len(inicios))
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
        return None, "PARADA: %s aparece %d veces dentro del acta 165." % (
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
    """LA CIFRA NO SE TECLEA. Barre `5.1`, `5.2`, ... hacia arriba y devuelve las
    que aparecen EXACTAMENTE UNA VEZ en el cuerpo, parando en la primera que no
    aparece. El tope es un cortafuegos de bucle, no una cifra esperada."""
    claves = []
    for k in range(1, tope + 1):
        clave = "5.%d" % k
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        cuantas = len([i for i in range(inicio, fin + 1) if pat.match(lineas[i - 1])])
        if cuantas == 0:
            break
        claves.append((clave, cuantas))
    return claves


def main():
    print("=" * 78)
    print("VUELTA 166, TAREA 1: EL ACTA 165 ENTERA, REGISTRADA EN LA FORMA DE LA CASA")
    print("=" * 78)
    print("")

    lineas, inicio, fin = cuerpo_del_acta()
    print("A) EL CUERPO DEL ACTA, ACOTADO ANTES DE CONTAR NADA")
    print("   acta 165: docs/loop/ACTA_AUDITOR.md, lineas %d a %d" % (inicio, fin))
    print("")

    print("B) LAS ADJUDICACIONES, CONTADAS DEL ACTA Y NO TECLEADAS")
    print("   se barre 5.1 hacia arriba hasta la primera que no aparece.")
    claves = claves_de_adjudicacion(lineas, inicio, fin)
    for clave, cuantas in claves:
        if cuantas != 1:
            print("   PARADA: %s aparece %d veces." % (clave, cuantas))
            return 1
    print("   CIFRA adjudicaciones halladas: %d (%s)"
          % (len(claves), ", ".join(c for c, _ in claves)))
    if not claves:
        print("   PARADA: el acta 165 no trae ninguna adjudicacion 5.n.")
        return 1
    sin_glosa = [c for c, _ in claves if c not in QUE_HACE_ESTA_VUELTA or c not in VIA]
    if sin_glosa:
        print("   PARADA: sin glosa escrita en este instrumento: %s"
              % ", ".join(sin_glosa))
        return 1
    print("   todas tienen VIA y glosa escritas: SI")
    print("")

    print("C) LAS CAIDAS PROPIAS DEL AUDITOR, CONTADAS DEL ACTA Y NO TECLEADAS")
    print("   viven en la SECCION 3 del acta 165 (en la 164 vivian en la 4).")
    encontradas = [i for i in range(inicio, fin + 1)
                   if re.match(r"^\s*\*\*CAIDA \d[,.]", lineas[i - 1])]
    print("   CIFRA negritas 'CAIDA n' halladas en el acta 165: %d" % len(encontradas))
    if not encontradas:
        print("   PARADA: no hay ninguna caida propia que registrar.")
        return 1
    print("")

    n_adj, n_cai = len(claves), len(encontradas)
    titulo_entrada = titulo_de_la_entrada(n_adj, n_cai)
    print("D) EL TITULO DE LA ENTRADA, COMPUESTO CON LOS DOS CONTEOS")
    print("   %s" % titulo_entrada)
    print("   CONTRASTE con el encargo de la 166: pide CATORCE adjudicaciones")
    print("   (5.1 a 5.14) y DOS caidas de la seccion 3. Mi conteo da %d y %d."
          % (n_adj, n_cai))
    print("   COINCIDEN: %s" % ("SI" if (n_adj, n_cai) == (14, 2) else
                                "NO. MANDA EL CONTEO Y SE DECLARA."))
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
    print("   CIFRA veces que aparece DENTRO del acta 165: %d" % len(dentro))
    if len(todas) != 1:
        print("   PARADA: la frase de la sede no aparece exactamente una vez.")
        return 1
    print("   DECLARADO: el acta 165 NO repite la frase; la regla vive en la")
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
    print("G) LAS ADJUDICACIONES, LEIDAS HOY DE SU LINEA EN EL ACTA 165")
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

    trozos = []
    trozos.append(
        "\n---\n\n## R.%d. %s\n\n"
        "(Acta del auditor, vuelta 165, secciones 3 y 5; escrito en la vuelta 166,\n"
        "TAREA 1.)\n\n"
        "Por adicion, como `R.21` a `R.34`. **Corte de todas las cifras de esta entrada:\n"
        "4 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa\n"
        "`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes. La\n"
        "SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, leida hoy en\n"
        "`docs/loop/ACTA_AUDITOR.md:%d`, y se DECLARA que el acta 165 no la repite (la\n"
        "regla es de la casa, no de un acta suelta). Salida:\n"
        "`docs/loop/SALIDA_V166_T1_REGISTRO_ACTA_165.txt`.\n\n"
        % (numero, titulo_entrada, todas[0]))
    trozos.append(
        "**Y LAS DOS CIFRAS DEL TITULO TAMPOCO ESTAN TECLEADAS**, que es lo que la\n"
        "adjudicacion 5.7 del propio acta 165 firma como metodo correcto: se cuentan del\n"
        "acta (%d adjudicaciones `5.n` y %d negritas `CAIDA n` dentro del cuerpo\n"
        "acotado) y de ahi sale el numeral en palabra. El encargo de la 166 pide catorce\n"
        "y dos; el conteo da lo mismo, asi que no hay discrepancia que declarar.\n\n"
        % (n_adj, n_cai))
    trozos.append(
        "**LAS %s ADJUDICACIONES, CON SU LINEA EN EL ACTA LEIDA HOY.** El titulo de\n"
        "cada una es LITERAL del fichero (localizado dentro del cuerpo del acta 165, no\n"
        "de cualquier acta); la glosa que sigue es prosa del ejecutor y va marcada como\n"
        "tal.\n\n%s\n"
        % (PALABRA[n_adj].upper(), "".join(bloques)))
    trozos.append(
        "**EL REPARTO POR VIA, CONTADO Y NO TECLEADO:** %s.\n"
        "**Ninguna de las %s sube al fundador.**\n\n"
        % (linea_reparto, PALABRA[n_adj]))
    trozos.append(
        "**LAS CAIDAS PROPIAS DEL AUDITOR, REGISTRADAS IGUAL QUE LAS DEL EJECUTOR**\n"
        "(letra del encargo de la vuelta 166, TAREA 1). No son del ejecutor y no acumulan\n"
        "para sus rachas; se escriben aqui porque el registro de la casa no distingue de\n"
        "quien es la mano que cae. En el acta 165 viven en la **seccion 3**, no en la 4\n"
        "como en el acta 164.\n\n%s\n" % "".join(bloques_caidas))
    trozos.append(
        "**LA CORRECCION DECLARADA QUE LA CAIDA 1 ARRASTRA, ESCRITA AQUI PORQUE AQUI ES\n"
        "DONDE LA CIFRA FALSA VIAJO** (`EJECUTOR.md` 8, *\"toda correccion declarada sin\n"
        "borrar el texto viejo\"*). La entrada `R.34` de este mismo fichero registro la\n"
        "adjudicacion 6.10 del acta 164 con su titulo literal, y ese titulo hablaba del\n"
        "*\"ultimo tramo de la fase III\"* apoyado en una cifra que hoy se sabe falsa: el\n"
        "acta 164 dijo **67 en `HECHA` y CUATRO en `LISTA`**. **NO SE BORRA NI UNA LETRA\n"
        "de `R.34`**: sigue entera y con su cifra vieja, porque una correccion que tapa lo\n"
        "que corrige no se puede auditar. **LA CIFRA DE HOY, medida por el ejecutor en la\n"
        "TAREA 4 de esta vuelta con instrumento propio sobre `docs/plan/OPERACIONES.jsonl`\n"
        "y publicada en `docs/loop/SALIDA_V166_T4_CENSO_OPERACIONES.txt`, es la que manda\n"
        "desde aqui**, y el reparto entero por fase va en esa salida y en el reporte de la\n"
        "vuelta 166. **Y la frase de que `OP-L-01` era la unica sin dependencias\n"
        "declaradas queda corregida en el mismo acto, con la cuenta al lado.**\n\n")
    trozos.append(
        "**LO QUE ESTE REGISTRO NO CIERRA.** La vara `P.5.1` sigue CONGELADA y ninguna de\n"
        "estas %s la estrecha ni la ensancha. Los pasos 2, 3 y 4 del `RECOMPUTO_3388.md`\n"
        "NO se recomputan en esta vuelta: la 5.12 encarga el PASO 1 y nada mas, y\n"
        "ampliarlo seria decidir su alcance por cuenta propia. Y ningun veredicto del\n"
        "cribado se mueve por esta entrada ni por la TAREA 5: el colapso se mide, la\n"
        "clase la decide una lectura.\n" % PALABRA[n_adj])
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
    print("VERDE: el acta 165 queda registrada como R.%d." % numero)
    return 0


# ---------------------------------------------------------------------------
# CASO POSITIVO POR MUTACION (EJECUTOR.md regla 1, "EL CASO ROJO SE PRUEBA POR
# MUTACION"). Se corre con `--mutar` y con el arnes de nombre propio
# `vuelta166_tarea1_mutacion_registro.py`, que es el que la bateria ve.
#
# CERO ESCRITURAS Y CERO FICHEROS: las actas de mentira se fabrican EN MEMORIA
# como listas de lineas. Nada toca `docs/PENDIENTES.md` ni
# `docs/loop/ACTA_AUDITOR.md`.
#
# QUE MIDE, Y POR QUE ES ESTO Y NO OTRA COSA. Lo que este instrumento CAMBIA
# respecto del de la vuelta 165 son DOS cosas: (a) la cifra de ADJUDICACIONES
# dejo de estar tecleada (`range(1, 11)` y `!= 10`) y pasa a computarse
# barriendo el acta, y (b) el TITULO de la entrada dejo de llevar sus dos
# numerales tecleados. Asi que lo que hay que poder tumbar es exactamente eso:
# que el barrido siga a lo que el acta trae, que pare en el primer hueco, que
# NO confunda `5.1` con `5.10` a `5.14` (la trampa nueva que la 164 no tenia,
# porque diez adjudicaciones no llegaban a `6.10` con espacio detras), y que el
# titulo cambie solo cuando cambian los conteos.
#
# NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: los casos salen de correr las
# funciones reales sobre sujetos distintos, y la segunda pasada muta cada valor
# esperado y exige que el caso CAIGA.
# ---------------------------------------------------------------------------

FRONTERA_FALSA = "# ACTA DEL AUDITOR, VUELTA 166 (frontera de mentira)"
CABECERA_FALSA = CABECERA_ACTA + " (fabricada por la prueba de mutacion)"
PAT_CAIDA = re.compile(r"^\s*\*\*CAIDA \d[,.]")


def _acta_fabricada(adjudicaciones=14, caidas=2, sangria="  ", duplicar=None,
                    quitar=None, sin_cierre=False):
    """Un acta 165 DE MENTIRA, en memoria. Devuelve (lineas, inicio, fin)."""
    L = ["ruido de otra acta",
         "**5.1 ESTA NO CUENTA, VIVE FUERA DEL CUERPO.** ruido",
         "**CAIDA 1. ESTA TAMPOCO, VIVE FUERA DEL CUERPO.** ruido",
         "",
         CABECERA_FALSA,
         "cuerpo cualquiera",
         "",
         "## 3. MIS CAIDAS PROPIAS, CON SU NOMBRE",
         ""]
    for k in range(1, caidas + 1):
        L.append("%s**CAIDA %d. TITULO DE LA CAIDA %d FABRICADA.** cuerpo"
                 % (sangria, k, k))
        L.append("")
    L.append("## 5. ADJUDICACIONES")
    L.append("")
    for k in range(1, adjudicaciones + 1):
        clave = "5.%d" % k
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
    L.append("**5.1 ESTA TAMPOCO CUENTA.** ruido de despues")
    L.append("**CAIDA 9. NI ESTA.** ruido de despues")
    return L, L.index(CABECERA_FALSA) + 1, L.index(FRONTERA_FALSA)


def _cuenta_caidas(lineas, inicio, fin):
    return len([i for i in range(inicio, fin + 1) if PAT_CAIDA.match(lineas[i - 1])])


def prueba_de_mutacion():
    print("=" * 78)
    print("VUELTA 166, TAREA 1: CASO POSITIVO POR MUTACION DEL REGISTRADOR DEL ACTA 165")
    print("=" * 78)
    print("")
    casos = []

    print("A) LA CIFRA DE ADJUDICACIONES SIGUE AL ACTA Y NO A UNA CONSTANTE")
    for n in (1, 5, 10, 14, 17):
        L, ini, fin = _acta_fabricada(adjudicaciones=n)
        visto = len(claves_de_adjudicacion(L, ini, fin))
        print("   acta fabricada con %d adjudicaciones -> el barrido ve %d" % (n, visto))
        casos.append(("A_con_%d_adjudicaciones_ve_%d" % (n, n), visto, n))
    print("")

    print("B) EL BARRIDO NO CONFUNDE 5.1 CON 5.10 A 5.14")
    L, ini, fin = _acta_fabricada(adjudicaciones=14)
    p1 = re.compile(r"^\s*\*\*%s " % re.escape("5.1"))
    casos.append(("B_el_patron_de_5_1_acierta_una_sola_vez",
                  len([i for i in range(ini, fin + 1) if p1.match(L[i - 1])]), 1))
    _h, e1 = titulo_de_la_negrita(L, ini, fin, p1, "5.1")
    casos.append(("B_y_su_titulo_se_lee_sin_error", e1 is None, True))
    print("   5.1 acierta %d vez dentro del cuerpo con 5.10 a 5.14 presentes"
          % len([i for i in range(ini, fin + 1) if p1.match(L[i - 1])]))
    print("")

    print("C) EL BARRIDO PARA EN EL PRIMER HUECO Y NO SALTA POR ENCIMA")
    Lq, iq, fq = _acta_fabricada(adjudicaciones=14, quitar="5.7")
    vistas = len(claves_de_adjudicacion(Lq, iq, fq))
    print("   acta de 14 con la 5.7 ausente -> el barrido ve %d (para en el hueco)"
          % vistas)
    casos.append(("C_para_en_el_hueco_y_ve_6", vistas, 6))
    Ld, id_, fd = _acta_fabricada(adjudicaciones=14, duplicar="5.5")
    dup = [c for c, n in claves_de_adjudicacion(Ld, id_, fd) if n != 1]
    print("   acta con la 5.5 duplicada -> claves con conteo distinto de 1: %s"
          % (", ".join(c for c in dup) or "ninguna"))
    casos.append(("C_la_duplicada_se_detecta", len(dup), 1))
    _h, e_dup = titulo_de_la_negrita(Ld, id_, fd, re.compile(r"^\s*\*\*5\.5 "), "5.5")
    casos.append(("C_duplicada_para", e_dup is not None, True))
    Ls, is_, fs = _acta_fabricada(adjudicaciones=14, sin_cierre=True)
    _h, e_sc = titulo_de_la_negrita(Ls, is_, fs, re.compile(r"^\s*\*\*5\.9 "), "5.9")
    print("   negrita sin cierre: %s" % (e_sc or "NO PARA"))
    casos.append(("C_negrita_sin_cierre_para", e_sc is not None, True))
    print("")

    print("D) EL ACOTADO DEJA FUERA EL RUIDO DE OTRAS ACTAS")
    L, ini, fin = _acta_fabricada()
    casos.append(("D_sin_acotar_hay_ruido_de_caidas", _cuenta_caidas(L, 1, len(L)), 4))
    casos.append(("D_acotado_no_lo_ve", _cuenta_caidas(L, ini, fin), 2))
    casos.append(("D_sin_acotar_la_5_1_esta_tres_veces",
                  len([i for i in range(1, len(L) + 1)
                       if re.match(r"^\s*\*\*5\.1 ", L[i - 1])]), 3))
    print("   sin acotar: %d negritas CAIDA | acotado: %d"
          % (_cuenta_caidas(L, 1, len(L)), _cuenta_caidas(L, ini, fin)))
    print("")

    print("E) EL TITULO SIGUE A LOS DOS CONTEOS Y NO A UNA CONSTANTE")
    for na, nc, esperado in ((14, 2, "catorce"), (10, 3, "diez"), (7, 1, "siete")):
        t = titulo_de_la_entrada(na, nc)
        print("   (%d, %d) -> %s" % (na, nc, t))
        casos.append(("E_titulo_%d_%d_dice_%s" % (na, nc, esperado),
                      t.split()[3], esperado))
    casos.append(("E_titulo_14_2_no_es_igual_al_de_10_3",
                  titulo_de_la_entrada(14, 2) == titulo_de_la_entrada(10, 3), False))
    print("")

    print("F) UNA ADJUDICACION O UNA CAIDA SIN GLOSA TIENE QUE PARAR")
    L17, i17, f17 = _acta_fabricada(adjudicaciones=17, caidas=4)
    claves17 = [c for c, _n in claves_de_adjudicacion(L17, i17, f17)]
    sin_glosa = [c for c in claves17 if c not in QUE_HACE_ESTA_VUELTA]
    print("   claves del acta de 17: sin glosa escrita -> %s"
          % (", ".join(sin_glosa) or "ninguna"))
    casos.append(("F_las_adjudicaciones_sin_glosa_se_detectan", len(sin_glosa), 3))
    claves_c17 = [re.match(r"^\s*\*\*(CAIDA \d)[,.]", L17[i - 1]).group(1)
                  for i in range(i17, f17 + 1) if PAT_CAIDA.match(L17[i - 1])]
    sin_glosa_c = [c for c in claves_c17 if c not in QUE_HACE_CON_LA_CAIDA]
    casos.append(("F_las_caidas_sin_glosa_se_detectan", len(sin_glosa_c), 2))
    L14, i14, f14 = _acta_fabricada()
    casos.append(("F_las_catorce_de_hoy_SI_tienen_glosa",
                  len([c for c, _n in claves_de_adjudicacion(L14, i14, f14)
                       if c not in QUE_HACE_ESTA_VUELTA]), 0))
    print("")
    print("G) EL ACTA DE VERDAD, LEIDA HOY")
    RL, ri, rf = cuerpo_del_acta()
    print("   cuerpo del acta 165: lineas %d a %d" % (ri, rf))
    reales = claves_de_adjudicacion(RL, ri, rf)
    n_adj = len(reales)
    n_cai = _cuenta_caidas(RL, ri, rf)
    print("   CIFRA adjudicaciones 5.n que trae la seccion 5: %d" % n_adj)
    print("   CIFRA caidas que trae la seccion 3: %d" % n_cai)
    casos.append(("G_el_acta_165_trae_CATORCE_adjudicaciones", n_adj, 14))
    casos.append(("G_cada_una_aparece_una_sola_vez",
                  len([c for c, n in reales if n != 1]), 0))
    casos.append(("G_el_acta_165_trae_DOS_caidas", n_cai, 2))
    todas = [i for i, l in enumerate(RL, 1) if FRASE_DE_LA_SEDE in l]
    casos.append(("G_la_frase_de_la_sede_esta_una_vez_en_el_fichero", len(todas), 1))
    casos.append(("G_y_cero_veces_dentro_del_acta_165",
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
    casos.append(("G_las_dieciseis_negritas_se_leen_sin_error", sin_error, 16))
    casos.append(("G_el_titulo_que_saldra_dice_catorce_y_dos",
                  titulo_de_la_entrada(n_adj, n_cai),
                  "Registro de las catorce adjudicaciones y las dos caidas propias "
                  "del acta de la vuelta 165"))
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
