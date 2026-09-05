# -*- coding: utf-8 -*-
r"""vuelta170_tarea1_registrar_acta169.py . TAREA 1.a de la vuelta 170.

REGISTRA EN LA FORMA DE LA CASA (`R.N`) EL ACTA 169 ENTERA: SUS ADJUDICACIONES
`6.n` Y LAS CAIDAS PROPIAS DEL AUDITOR de su seccion 3. Hereda la maquina de
`vuelta169_tarea1_registrar_acta168.py` SIN tocarle el mecanismo, y la maquina
es la que importa: NINGUNA CIFRA SE TECLEA. El numero de la entrada lo computa
`serie_de_registros.py` recomputando la serie de sus DOS sedes; el conteo de
adjudicaciones se barre del acta parando en el primer hueco; el conteo de
caidas se cuenta de las negritas `CAIDA n` del cuerpo acotado; y el numeral en
palabra del titulo, con su concordancia, sale de esos dos conteos.

QUE CAMBIA RESPECTO DEL INSTRUMENTO DE LA VUELTA 169:

  (1) EL CUERPO ACOTADO pasa del acta 168 al acta 169 (`CABECERA_ACTA`), que es
      hoy la ULTIMA del fichero: `fin` cae en el final del fichero y no en la
      cabecera siguiente.
  (2) LAS DOS CIFRAS SE MUEVEN OTRA VEZ Y LAS DOS HACIA ARRIBA: el `R.38`
      registro DIEZ adjudicaciones y DOS caidas; el acta 169 trae DOCE y TRES.
      Los dos numerales suben solos y ninguno esta tecleado. Si lo estuvieran,
      la herencia los habria arrastrado, que es justo la especie de caida que
      esta maquina existe para impedir.
  (3) EL BARRIDO DE `6.n` TIENE QUE LLEGAR A `6.12` SIN CONFUNDIR `6.1` CON
      `6.10`, `6.11` NI `6.12`. Lo que lo impide sigue siendo el espacio final
      del patron `^\s*\*\*6\.1 `, ya probado por mutacion en la vuelta 169; esta
      vuelta lo estira dos numeros mas y el arnes hermano lo vuelve a probar.

USO:  python scripts/loop/vuelta170_tarea1_registrar_acta169.py
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402

RAIZ = SERIE.RAIZ
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 169"
VUELTA_DEL_ACTA = 169
VUELTA_QUE_ESCRIBE = 170

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
    return ("Registro de las %s adjudicaciones y %s del acta de la vuelta %d"
            % (PALABRA[n_adj], cola, VUELTA_DEL_ACTA))


VIA = {
    "6.1": "EJECUTADA",
    "6.2": "EJECUTADA",
    "6.3": "EJECUTADA",
    "6.4": "EJECUTADA",
    "6.5": "SIN TOCAR NADA",
    "6.6": "SIN TOCAR NADA",
    "6.7": "SIN TOCAR NADA",
    "6.8": "SIN TOCAR NADA",
    "6.9": "EJECUTADA",
    "6.10": "EJECUTADA",
    "6.11": "EJECUTADA",
    "6.12": "SIN TOCAR NADA",
}

QUE_HACE_ESTA_VUELTA = {
    "6.1": ("EJECUTADA, TAREA 2.a de esta vuelta. Nace "
            "`scripts/loop/aislador_de_ciega.py`, con nombre estable y sin numero de "
            "vuelta. Recibe un CRITERIO ESCRITO, elige los pares con el, imprime en la "
            "salida ciega SOLO `puesto_intra`, `nodo_a`, `nodo_b` y los pasos de los "
            "dos nodos, y escribe el destape (clase y razon) EN UN FICHERO APARTE que "
            "no hace falta abrir hasta tener las clases escritas. La regla que el acta "
            "pide (EL SUJETO DE LA CIEGA SE ELIGE Y SE AISLA ANTES DEL PRIMER COMANDO "
            "DE VERIFICACION) deja de depender de que alguien se acuerde: el "
            "instrumento no puede imprimir la clase en la salida ciega porque la "
            "construye campo a campo desde una lista blanca, y su caso positivo por "
            "mutacion CAE si el destape se cuela."),
    "6.2": ("EJECUTADA, TAREA 1.b de esta vuelta, POR EL CARRIL DEL BANCO 9.10 Y SIN "
            "BORRAR UNA PALABRA. El comentario de "
            "`scripts/loop/vuelta166_tarea3_mutacion_retrato.py` que dice que la vuelta "
            "167 anadio una tachada QUEDA ENTERO Y TACHADO, con la correccion fechada "
            "adosada debajo y la tabla de commits MEDIDA POR MI EN ESTA VUELTA pegada "
            "al lado. La correccion dice las dos cosas que el acta pide: quien anadio "
            "la decimotercera tachada, y por que el computo dice CATORCE. La tabla no "
            "se copio del acta: se midio con el localizador del propio instrumento "
            "sobre los commits que tocan el retrato."),
    "6.3": ("EJECUTADA, TAREA 1.c de esta vuelta. El arnes gana un caso que ANCLA POR "
            "MEDICION el commit de nacimiento de la decimotercera tachada, leyendolo de "
            "`git log` en vez de contarlo en prosa: recorre los commits que tocan el "
            "retrato, cuenta las tachadas en el blob de cada uno y comprueba que el "
            "primero que llega a trece es el que el arnes nombra. Con su caso positivo "
            "por mutacion. Una historia escrita en un comentario se pudre; una anclada "
            "en un caso cae."),
    "6.4": ("EJECUTADA, TAREA 2.b de esta vuelta. Nace "
            "`scripts/loop/archivar_reporte.py`, con nombre estable y sin numero de "
            "vuelta, que copia el reporte de la vuelta que cierra a "
            "`docs/loop/reportes/REPORTE_V<N>.md`. NO borra nada, no cambia ninguna "
            "regla y no crea sede nueva: le da nombre de fichero a la que ya existia. "
            "Lee el texto DE GIT y no del arbol de trabajo, y por eso puede archivar "
            "HACIA ATRAS: el de la 168, que hoy solo vivia en `1eec382f`, queda en "
            "`docs/loop/reportes/REPORTE_V168.md` con sus 31.263 bytes y 530 lineas, "
            "cifras que coinciden con las que el propio mensaje de `1eec382f` publica."),
    "6.5": ("SE ACATA SIN TOCAR NADA. La adjudicacion ratifica lo que el ejecutor ya "
            "hizo: el 332 del fichero sellado y el 47 de hoy sobre el grafo vivo se "
            "publican LOS DOS, cada uno con su corte, por `9.21`. Esta vuelta no "
            "recomputa ninguno de los dos ni borra el otro, y `RECOMPUTO_3388_COMPONENTES.jsonl` "
            "sigue siendo la foto del cierre transitivo al corte 3.388."),
    "6.6": ("SE ACATA SIN TOCAR NADA. La 'parada' que la TAREA 4 de la 169 trajo queda "
            "adjudicada: NO es parada, y el universo re-medible de la clausula 3 son "
            "las 348 vivas, no las 569. Esta vuelta no la reabre ni re-mide las 221 "
            "entradas que llevan escrita su marca `SUPERADA`, porque contradecir una "
            "marca escrita no es ejecutar una clausula."),
    "6.7": ("SE ACATA SIN TOCAR NADA. La regla de la SEDE DEL ROJO queda escrita y esta "
            "vuelta la obedece tal cual: un rojo que causo OTRA vuelta se trae sin "
            "tocarlo; un rojo que causaron las escrituras de ESTA misma sesion se "
            "arregla en ESTA misma sesion. La bateria abre esta vuelta EN VERDE por "
            "medicion del auditor, asi que no hay ningun rojo heredado que clasificar."),
    "6.8": ("SE ACATA SIN TOCAR NADA. El retoque del rotulo `las_doce_tachadas` queda "
            "adjudicado a favor del ejecutor y al reves de como lo temia: no solo "
            "estaba permitido, era obligatorio, porque un rotulo que teclea una cifra "
            "que su propio computo desmiente es una cifra falsa en el texto de una "
            "guarda. Esta vuelta no lo reabre."),
    "6.9": ("EJECUTADA, TAREA 4.a de esta vuelta, POR ADICION PURA. Las filas de tabla "
            "de la segunda tanda de `docs/plan/LECTURAS_DIRIGIDAS.md` ganan numero `LD` "
            "sin perder una palabra de su texto, con el siguiente libre COMPUTADO POR "
            "INSTRUMENTO igual que `serie_de_registros.py` computa los `R.n`. Numerar "
            "no es reescribir. El instrumento PARA si el conteo no cuadra con lo que el "
            "encargo supone, en vez de ajustar la cifra al encargo."),
    "6.10": ("EJECUTADA, TAREA 4.b de esta vuelta, Y LA FORMA DE EJECUTARLA ES NO "
             "EJECUTAR LA FUSION. Los cinco nodos puente del sales roadmap quedan "
             "REGISTRADOS CON SU MEDICION y con la salida de `P.10` nombrada, y NO se "
             "funden: ninguna operacion escrita recoge esta fusion, y ejecutar una "
             "fusion que ninguna ficha ordena es la improvisacion que `AUDITOR.md` "
             "seccion 3 prohibe con esas palabras. Su ejecucion espera a la operacion "
             "que abra este acto por `P.5` y `P.8`."),
    "6.11": ("EJECUTADA, TAREA 3 de esta vuelta, POR ADICION Y CON LA CIFRA VIEJA "
             "ENTERA. Las apariciones de '53 familias' en la nota de `OP-I-01`, la "
             "aritmetica de 671 que una de ellas sostiene, y el 'el marcador sigue en "
             "2.117' de la clausula 2 de `OP-L-01` y de `OP-L-02` ganan su fecha de "
             "corte al lado por `9.21`, sin que ninguna letra vieja se sustituya. "
             "Ninguna de las tres era una mentira: las tres son ciertas en su corte y "
             "les faltaba el corte escrito. Las apariciones se CUENTAN con instrumento "
             "en esta vuelta y no se copian del acta."),
    "6.12": ("SE ACATA SIN TOCAR NADA, Y ESTA VUELTA LA MANTIENE. Ninguna clase se "
             "movio por el acta 169 y ninguna se mueve por esta vuelta: "
             "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` NO se toca, ni al cerrar la forma "
             "de las nominas de `OP-L-02` ni al registrar los cinco puentes, porque una "
             "lectura dirigida no entra en la cola y no mueve su marcador."),
}

QUE_HACE_CON_LA_CAIDA = {
    "CAIDA 1": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. Y ES LA UNICA DE LAS TRES QUE VIENE CON "
                "REMEDIO DE CODIGO ENCARGADO: dos turnos de auditor seguidos quemando "
                "el sujeto de ciega dejaron de ser un descuido, y por eso la `6.1` "
                "manda construir el aislador en vez de limitarse a escribir la regla. "
                "Esta vuelta lo construye (TAREA 2.a). Lo que ensena, con las palabras "
                "del acta: mirar es irreversible, y por eso se mira en el orden que "
                "deja opciones; lo que el remedio anade es que el orden deje de "
                "depender de que alguien se acuerde."),
    "CAIDA 2": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. Y SE REGISTRA AUNQUE NO LLEGARA A "
                "PUBLICARSE: el auditor casi acusa al ejecutor dos veces con un "
                "resolutor casero (0 colapsos y 334 componentes contra 398 y 47; 6 y 9 "
                "contra 8 y 7), y en los dos casos el equivocado era el. NO HAY CIFRA "
                "PUBLICADA QUE CORREGIR POR ELLA. Lo que ensena, en sus palabras: un "
                "auditor que mide con un instrumento peor que el del ejecutor no esta "
                "verificando, esta adivinando con ceremonia. La regla que lo cierra ya "
                "existe y es `P.1`: todo conteo que toque ids pasa por el resolutor "
                "antes de contar."),
    "CAIDA 3": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. Una clase equivocada del auditor en su "
                "relectura ciega, el puesto 788, resuelta a favor del archivo tras "
                "releer la regla. NO MUEVE NINGUN DATO y por eso la `6.12` puede decir "
                "que ninguna clase se mueve por el acta 169; cuenta como discrepancia "
                "en la metrica de credito del propio auditor y esta vuelta no la "
                "reabre."),
}


def cuerpo_del_acta():
    """El texto del acta, acotado por su cabecera y por el final del fichero o
    la cabecera siguiente."""
    texto = io.open(ACTA, encoding="utf-8").read()
    lineas = texto.split("\n")
    inicios = [i for i, l in enumerate(lineas, 1) if l.startswith(CABECERA_ACTA)]
    if len(inicios) != 1:
        raise SystemExit("ROJO: la cabecera del acta %d aparece %d veces."
                         % (VUELTA_DEL_ACTA, len(inicios)))
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
        return None, "PARADA: %s aparece %d veces dentro del acta %d." % (
            etiqueta, len(aciertos), VUELTA_DEL_ACTA)
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
    `6.1` se coma a `6.10`, `6.11` y `6.12`."""
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
    print("VUELTA %d, TAREA 1.a: EL ACTA %d ENTERA, REGISTRADA EN LA FORMA DE LA CASA"
          % (VUELTA_QUE_ESCRIBE, VUELTA_DEL_ACTA))
    print("=" * 78)
    print("")

    lineas, inicio, fin = cuerpo_del_acta()
    print("A) EL CUERPO DEL ACTA, ACOTADO ANTES DE CONTAR NADA")
    print("   acta %d: docs/loop/ACTA_AUDITOR.md, lineas %d a %d"
          % (VUELTA_DEL_ACTA, inicio, fin))
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
        print("   PARADA: el acta %d no trae ninguna adjudicacion 6.n." % VUELTA_DEL_ACTA)
        return 1
    sin_glosa = [c for c, _ in claves if c not in QUE_HACE_ESTA_VUELTA or c not in VIA]
    if sin_glosa:
        print("   PARADA: sin glosa escrita en este instrumento: %s"
              % ", ".join(sin_glosa))
        return 1
    sobran = [c for c in QUE_HACE_ESTA_VUELTA if c not in [k for k, _ in claves]]
    if sobran:
        print("   PARADA: este instrumento trae glosa para adjudicaciones que el acta "
              "no tiene: %s" % ", ".join(sorted(sobran)))
        return 1
    print("   todas tienen VIA y glosa escritas: SI")
    print("   y ninguna glosa sobra: SI")
    print("")

    print("C) LAS CAIDAS PROPIAS DEL AUDITOR, CONTADAS DEL ACTA Y NO TECLEADAS")
    encontradas = [i for i in range(inicio, fin + 1)
                   if re.match(r"^\s*\*\*CAIDA \d[,.]", lineas[i - 1])]
    print("   CIFRA negritas 'CAIDA n' halladas en el acta %d: %d"
          % (VUELTA_DEL_ACTA, len(encontradas)))
    if not encontradas:
        print("   PARADA: no hay ninguna caida propia que registrar.")
        return 1
    print("")

    n_adj, n_cai = len(claves), len(encontradas)
    titulo_entrada = titulo_de_la_entrada(n_adj, n_cai)
    print("D) EL TITULO DE LA ENTRADA, COMPUESTO CON LOS DOS CONTEOS")
    print("   %s" % titulo_entrada)
    print("   CONTRASTE, Y ES CONTRASTE Y NO FUENTE: el encargo de la %d nombra"
          % VUELTA_QUE_ESCRIBE)
    print("   'sus adjudicaciones 6.1 a 6.12', o sea DOCE. Manda el conteo.")
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
    print("   CIFRA veces que aparece DENTRO del acta %d: %d"
          % (VUELTA_DEL_ACTA, len(dentro)))
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

    print("G) LAS ADJUDICACIONES, LEIDAS HOY DE SU LINEA EN EL ACTA %d" % VUELTA_DEL_ACTA)
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
        "(Acta del auditor, vuelta %d, secciones 3 y 6; escrito en la vuelta %d,\n"
        "TAREA 1.a.)\n\n"
        "Por adicion, como `R.21` a `R.38`. **Corte de todas las cifras de esta entrada:\n"
        "4 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa\n"
        "`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.\n"
        "La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, leida hoy\n"
        "en `docs/loop/ACTA_AUDITOR.md:%d`. Salida:\n"
        "`docs/loop/SALIDA_V%d_T1_REGISTRO_ACTA_%d.txt`.\n\n"
        % (numero, titulo_entrada, VUELTA_DEL_ACTA, VUELTA_QUE_ESCRIBE,
           todas[0], VUELTA_QUE_ESCRIBE, VUELTA_DEL_ACTA))
    trozos.append(
        "**Y LAS DOS CIFRAS DEL TITULO TAMPOCO ESTAN TECLEADAS:** se cuentan del acta\n"
        "(%d adjudicaciones `6.n` y %d negritas `CAIDA n` dentro del cuerpo acotado,\n"
        "lineas %d a %d) y de ahi sale el numeral en palabra, **incluida la\n"
        "concordancia**. **EL `R.38` REGISTRO DIEZ Y DOS; ESTE REGISTRA %d Y %d**, y los\n"
        "dos numerales subieron solos. **Y ESTA ENTRADA ESTIRA DOS NUMEROS MAS EL BORDE\n"
        "QUE LA ANTERIOR ESTRENO:** el acta 168 fue la primera en llegar a `6.10` y el\n"
        "acta 169 llega a `6.12`, asi que el barrido tiene que contar tres claves de dos\n"
        "digitos sin confundir ninguna con `6.1`. Lo que lo impide sigue siendo el\n"
        "espacio final del patron `^\\s*\\*\\*6\\.1 `, y el arnes hermano lo prueba por\n"
        "mutacion en vez de afirmarlo.\n\n"
        % (n_adj, n_cai, inicio, fin, n_adj, n_cai))
    trozos.append(
        "**LAS %s ADJUDICACIONES, CON SU LINEA EN EL ACTA LEIDA HOY.** El titulo de\n"
        "cada una es LITERAL del fichero (localizado dentro del cuerpo del acta %d, no\n"
        "de cualquier acta); la glosa que sigue es prosa del ejecutor y va marcada como\n"
        "tal.\n\n%s\n"
        % (PALABRA[n_adj].upper(), VUELTA_DEL_ACTA, "".join(bloques)))
    trozos.append(
        "**EL REPARTO POR VIA, CONTADO Y NO TECLEADO:** %s.\n%s\n\n"
        % (linea_reparto, linea_fundador))
    trozos.append(
        "**%s IGUAL QUE LAS DEL EJECUTOR**\n"
        "(precedente del `R.36`, escrito en la vuelta 167 por letra de su encargo, y\n"
        "heredado aqui sin reabrirlo). No son del ejecutor y no acumulan para sus\n"
        "rachas; se escriben aqui porque el registro de la casa no distingue de quien es\n"
        "la mano que cae. En el acta %d viven en la **seccion 3**.\n\n%s\n"
        % (palabra_caidas, VUELTA_DEL_ACTA, "".join(bloques_caidas)))
    trozos.append(
        "**LO QUE ESTE REGISTRO NO CIERRA, Y SE DICE ANTES DE QUE NADIE LO SUPONGA.**\n"
        "La vara `P.5.1` sigue CONGELADA y ninguna de estas %s la estrecha ni la\n"
        "ensancha. **Ninguna clase del cribado se mueve por esta entrada** y\n"
        "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no se toca, que es lo que la `6.12`\n"
        "reserva. **Ningun `estado` de `docs/plan/OPERACIONES.jsonl` se mueve por esta\n"
        "entrada**: el campo sigue jubilado como historico y la vara del trabajo\n"
        "pendiente sigue siendo `scripts/loop/vuelta150_3_relectura_expediente.py`.\n"
        "**Y las dos `OP-M-02` siguen sin ejecutarse**, por la `6.6` del acta 168.\n"
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
    print("VERDE: el acta %d queda registrada como R.%d." % (VUELTA_DEL_ACTA, numero))
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

FRONTERA_FALSA = "# ACTA DEL AUDITOR, VUELTA 170 (frontera de mentira)"
CABECERA_FALSA = CABECERA_ACTA + " (fabricada por la prueba de mutacion)"
PAT_CAIDA = re.compile(r"^\s*\*\*CAIDA \d[,.]")


def _acta_fabricada(adjudicaciones=12, caidas=3, sangria="  ", duplicar=None,
                    quitar=None, sin_cierre=False):
    """Un acta 169 DE MENTIRA, en memoria. Devuelve (lineas, inicio, fin)."""
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
    print("VUELTA 170, TAREA 1.a: CASO POSITIVO POR MUTACION DEL REGISTRADOR DEL ACTA 169")
    print("=" * 78)
    print("")
    casos = []

    print("A) LA CIFRA DE ADJUDICACIONES SIGUE AL ACTA Y NO A UNA CONSTANTE")
    for n in (1, 5, 9, 12, 14, 17):
        L, ini, fin = _acta_fabricada(adjudicaciones=n)
        visto = len(claves_de_adjudicacion(L, ini, fin))
        print("   acta fabricada con %d adjudicaciones -> el barrido ve %d" % (n, visto))
        casos.append(("A_con_%d_adjudicaciones_ve_%d" % (n, n), visto, n))
    print("")

    print("B) EL BARRIDO NO CONFUNDE 6.1 CON 6.10, 6.11, 6.12 NI 6.13 A 6.14")
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
    casos.append(("D_sin_acotar_hay_ruido_de_caidas", _cuenta_caidas(L, 1, len(L)), 5))
    casos.append(("D_acotado_no_lo_ve", _cuenta_caidas(L, ini, fin), 3))
    casos.append(("D_sin_acotar_la_6_1_esta_tres_veces",
                  len([i for i in range(1, len(L) + 1)
                       if re.match(r"^\s*\*\*6\.1 ", L[i - 1])]), 3))
    print("   sin acotar: %d negritas CAIDA | acotado: %d"
          % (_cuenta_caidas(L, 1, len(L)), _cuenta_caidas(L, ini, fin)))
    print("")
    print("E) EL TITULO SIGUE A LOS DOS CONTEOS Y NO A UNA CONSTANTE,")
    print("   Y CONCUERDA EN NUMERO EN SUS DOS RAMAS")
    for na, nc, esperado in ((6, 2, "seis"), (9, 1, "nueve"), (12, 3, "doce"),
                             (14, 3, "catorce")):
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
    casos.append(("F_las_adjudicaciones_sin_glosa_se_detectan", len(sin_glosa), 5))
    claves_c17 = [re.match(r"^\s*\*\*(CAIDA \d)[,.]", L17[i - 1]).group(1)
                  for i in range(i17, f17 + 1) if PAT_CAIDA.match(L17[i - 1])]
    sin_glosa_c = [c for c in claves_c17 if c not in QUE_HACE_CON_LA_CAIDA]
    casos.append(("F_las_caidas_sin_glosa_se_detectan", len(sin_glosa_c), 1))
    L6, i6, f6 = _acta_fabricada(adjudicaciones=12, caidas=3)
    casos.append(("F_las_doce_de_hoy_SI_tienen_glosa",
                  len([c for c, _n in claves_de_adjudicacion(L6, i6, f6)
                       if c not in QUE_HACE_ESTA_VUELTA]), 0))
    print("")
    print("G) EL ACTA DE VERDAD, LEIDA HOY")
    RL, ri, rf = cuerpo_del_acta()
    print("   cuerpo del acta 169: lineas %d a %d" % (ri, rf))
    reales = claves_de_adjudicacion(RL, ri, rf)
    n_adj = len(reales)
    n_cai = _cuenta_caidas(RL, ri, rf)
    print("   CIFRA adjudicaciones 6.n que trae la seccion 6: %d" % n_adj)
    print("   CIFRA caidas que trae la seccion 3: %d" % n_cai)
    casos.append(("G_el_acta_169_trae_DOCE_adjudicaciones", n_adj, 12))
    casos.append(("G_cada_una_aparece_una_sola_vez",
                  len([c for c, n in reales if n != 1]), 0))
    casos.append(("G_el_acta_169_trae_TRES_caidas", n_cai, 3))
    todas = [i for i, l in enumerate(RL, 1) if FRASE_DE_LA_SEDE in l]
    casos.append(("G_la_frase_de_la_sede_esta_una_vez_en_el_fichero", len(todas), 1))
    casos.append(("G_y_cero_veces_dentro_del_acta_169",
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
    casos.append(("G_las_quince_negritas_se_leen_sin_error", sin_error, 15))
    casos.append(("G_el_titulo_que_saldra_dice_doce_y_tres_en_plural",
                  titulo_de_la_entrada(n_adj, n_cai),
                  "Registro de las doce adjudicaciones y las tres caidas propias "
                  "del acta de la vuelta 169"))
    # LA RAMA NUEVA DE ESTA VUELTA: la linea del fundador se computa. Se prueba
    # sobre las vias REALES de este instrumento y sobre un reparto sin ninguna
    # via de fundador, para que las DOS ramas queden ejercidas.
    suben_reales = sorted(c for c, v in VIA.items() if v.startswith("AL FUNDADOR"))
    casos.append(("G_las_vias_reales_no_suben_NINGUNA_al_fundador",
                  len(suben_reales), 0))
    ejecutadas = sorted(c for c, v in VIA.items() if v == "EJECUTADA")
    casos.append(("G_el_reparto_real_da_SIETE_ejecutadas", len(ejecutadas), 7))
    sin_tocar = sorted(c for c, v in VIA.items() if v == "SIN TOCAR NADA")
    casos.append(("G_y_CINCO_sin_tocar_nada", len(sin_tocar), 5))
    casos.append(("G_y_las_dos_vias_suman_las_doce",
                  len(ejecutadas) + len(sin_tocar), 12))
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


if __name__ == "__main__":
    if "--mutar" in sys.argv:
        raise SystemExit(prueba_de_mutacion())
    raise SystemExit(main())
