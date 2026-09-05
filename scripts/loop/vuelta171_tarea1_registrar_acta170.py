# -*- coding: utf-8 -*-
r"""vuelta171_tarea1_registrar_acta170.py . TAREA 1.a de la vuelta 171.

REGISTRA EN LA FORMA DE LA CASA (`R.N`) EL ACTA 170 ENTERA: SUS ADJUDICACIONES
`6.n` Y LAS CAIDAS PROPIAS DEL AUDITOR de su seccion 3. Clon declarado de
`vuelta170_tarea1_registrar_acta169.py` SIN tocarle el mecanismo, y la maquina
es la que importa: NINGUNA CIFRA SE TECLEA. El numero de la entrada lo computa
`serie_de_registros.py` recomputando la serie de sus DOS sedes; el conteo de
adjudicaciones se barre del acta parando en el primer hueco; el conteo de
caidas se cuenta de las negritas `CAIDA n` del cuerpo acotado; y el numeral en
palabra del titulo, con su concordancia, sale de esos dos conteos.

QUE CAMBIA RESPECTO DEL INSTRUMENTO DE LA VUELTA 170, Y LAS DOS COSAS ESTAN
MEDIDAS ANTES DE ESCRIBIRLAS:

  (1) EL CUERPO ACOTADO pasa del acta 169 al acta 170 (`CABECERA_ACTA`), que es
      hoy la ULTIMA del fichero: `fin` cae en el final del fichero y no en la
      cabecera siguiente.

  (2) LA FORMA DE LAS NEGRITAS DE CAIDA CAMBIO, Y SI NO SE ADAPTA EL PATRON EL
      CONTEO SALE CERO. El acta 169 escribia `**CAIDA 1. ...**` al principio de
      linea. El acta 170 las escribe como VINETA Y CON COMILLAS INVERSAS:
      ``- **`CAIDA 1`. ...**``. El patron viejo `^\s*\*\*CAIDA \d[,.]` no casa
      con ninguna de las cuatro, medido: da 0. El patron nuevo acepta la vineta
      opcional y las comillas inversas opcionales, y por eso casa con las dos
      formas; el arnes hermano lo prueba por mutacion CON LAS DOS, para que
      adaptar el patron no signifique aflojarlo. Y `titulo_de_la_negrita` gana
      lo mismo: la vineta se recorta antes de buscar el cierre de la negrita, o
      el titulo saldria con el guion de lista pegado delante.

  (3) LAS DOS CIFRAS SE MUEVEN OTRA VEZ: el `R.39` registro DOCE adjudicaciones
      y TRES caidas; el acta 170 trae DOCE y CUATRO. Los dos numerales salen
      solos de los conteos y ninguno esta tecleado.

USO:  python scripts/loop/vuelta171_tarea1_registrar_acta170.py
      python scripts/loop/vuelta171_tarea1_registrar_acta170.py --mutar
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402

RAIZ = SERIE.RAIZ
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 170"
VUELTA_DEL_ACTA = 170
VUELTA_QUE_ESCRIBE = 171

FRASE_DE_LA_SEDE = "la sede por defecto es `docs/PENDIENTES.md`"

# EL PATRON DE LA NEGRITA DE CAIDA, ADAPTADO A LAS DOS FORMAS. Ver el punto (2)
# del docstring. La vineta y las comillas inversas son OPCIONALES: asi casa con
# `**CAIDA 1.` (acta 169) y con ``- **`CAIDA 1`.`` (acta 170) sin dejar de
# exigir la negrita, el numero y el signo de puntuacion detras.
PAT_CAIDA = re.compile(r"^\s*(?:-\s+)?\*\*`?CAIDA (\d+)`?[,.]")

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
    "6.6": "EJECUTADA",
    "6.7": "SIN TOCAR NADA",
    "6.8": "SIN TOCAR NADA",
    "6.9": "EJECUTADA",
    "6.10": "SIN TOCAR NADA",
    "6.11": "EJECUTADA",
    "6.12": "EJECUTADA",
}

QUE_HACE_ESTA_VUELTA = {
    "6.1": ("EJECUTADA, TAREA 3 de esta vuelta. La 'parada' de la numeracion `LD` queda "
            "cerrada por donde el acta dice: la regla estaba escrita en el codigo del "
            "instrumento que el encargo nombraba, `serie_de_registros.py:97-102`, "
            "`return (max(nums) + 1) if nums else 1`, sin condicional de huecos. EL "
            "SIGUIENTE LIBRE ES EL MAYOR MAS UNO, y las 16 filas de la segunda tanda "
            "ganan `LD-139` a `LD-154` por ADICION PURA, con los numeros COMPUTADOS POR "
            "INSTRUMENTO y sin tocar una palabra de su texto. El `D.6` (la adyacencia "
            "del tramo `LD-12` a `LD-27`) se publica como CONTRASTE MEDIDO y no como "
            "fundamento: una adyacencia no es una asignacion."),
    "6.2": ("EJECUTADA, Y LA FORMA DE EJECUTARLA ES EL ORDEN. La numeracion no se "
            "escribe hasta que los cinco borradores salen de `docs/`: primero la TAREA "
            "2 limpia y vuelve a medir, y solo cuando las dos varas (el mayor de las "
            "HECHAS y el mayor del UNIVERSO) convergen en `LD-138` entra la TAREA 3. Si "
            "no convergieran, esta vuelta para y lo trae, que es lo que el acta manda."),
    "6.3": ("EJECUTADA, TAREA 2 de esta vuelta, CON `git mv` Y SIN BORRAR NI EDITAR "
            "NADA. Los cinco `docs/loop/_v170_t*_seccion.md` se mueven a "
            "`scripts/loop/`, que es donde la propia vuelta 170 aparco el borrador de "
            "su cierre. El motivo no es doctrina nueva: `vuelta48_contar_ld.py` ya "
            "excluye `REPORTE.md` por NARRATIVO DEL BUCLE, y un fichero que es "
            "literalmente una seccion de ese mismo reporte es de la misma especie. "
            "Despues se vuelve a correr el contador y se publican las TRES lecturas al "
            "lado: la de `222ca6a7`, la de HEAD antes de mover y la de despues."),
    "6.4": ("EJECUTADA, TAREA 4.a de esta vuelta, POR EL CARRIL DEL BANCO `9.10`. La "
            "entrada `R.38` afirma que 'el arnes hermano lo prueba por mutacion' y ese "
            "arnes no existe. La frase vieja QUEDA ENTERA Y TACHADA y debajo va la "
            "correccion fechada con su medicion pegada. 'No es mio y el encargo no me "
            "manda tocarlo' no vale para una afirmacion falsa en la serie de registros: "
            "la serie es una sola y la lee todo el que venga detras."),
    "6.5": ("SE ACATA SIN TOCAR NADA. `node_modules/` se queda como esta y NO entra en "
            "`.gitignore`: medido en esta vuelta, `.gitignore` no tiene hoy ninguna "
            "linea de `node_modules`, y anadirla es un cambio de alcance del repo que "
            "la casa reserva al fundador. Esta vuelta lo mide en su sello de apertura, "
            "lo declara y no lo decide."),
    "6.6": ("EJECUTADA, TAREA 5.a de esta vuelta, Y SE ENCHUFA DE VERDAD. Nace "
            "`scripts/loop/paso0_archivar_anterior.py`, con nombre estable y sin numero "
            "de vuelta para que el enchufe no se pierda en el siguiente clon. El "
            "esqueleto lo llama como PASO 0 y SE NIEGA A ESCRIBIR si el reporte "
            "anterior no esta archivado. Y su clausula fuerte no es que el archivo "
            "exista, sino que EL TEXTO QUE SE VA A PISAR este guardado byte a byte: se "
            "cotejan los dos sha256, porque las clausulas debiles se cumplen con un "
            "archivo viejo y solo esa mira lo que se va a destruir. Con su caso "
            "positivo por mutacion, que la tumba en sus cuatro modos."),
    "6.7": ("SE ACATA SIN TOCAR NADA. La adjudicacion confirma en disco que a `OP-L-01` "
            "no habia que escribirle una segunda correccion, porque su indice 4 ya "
            "traia la del 2.117 fechada desde la vuelta 166. Esta vuelta no la reabre y "
            "no escribe una segunda: dejar dos versiones de la misma cosa es lo que la "
            "adjudicacion evita."),
    "6.8": ("SE ACATA SIN TOCAR NADA. Los dos universos del campo `forma` de `la "
            "supervision de la IA` (el racimo entero 13 de 21 y la nomina de `OP-L-02` "
            "10 de 10) se quedan los dos escritos, cada uno con lo que cubre, por "
            "`9.26` y `9.16`. El `P.3` y el `PD.3` quedan contestados ahi y esta vuelta "
            "no los reabre."),
    "6.9": ("EJECUTADA, TAREA 5.b de esta vuelta, Y LA FORMA DE EJECUTARLA ES MEDIR "
            "ANTES DE LEGISLAR. Se corre el CENSO del campo `forma` sobre las 672 "
            "entradas de `docs/plan/INVENTARIO.jsonl`, con la nomina de palabras y "
            "cuantas entradas usa cada una, porque decir 'no encontre vocabulario "
            "cerrado' es una busqueda negativa y `EJECUTOR.md` 9 no deja citarla. Con "
            "el censo delante se dice si `FUNDIDA` cabe o si no hay vocabulario y sube "
            "al fundador. MIENTRAS TANTO LA PALABRA SE QUEDA: describe un hecho "
            "verificado y ninguna regla escrita la prohibe."),
    "6.10": ("SE ACATA SIN TOCAR NADA. La entrada de los dos arneses nuevos en la "
             "bateria el dia que nacen queda adjudicada a favor del ejecutor: la "
             "condicion desde la vuelta 148 es SUJETO CONGELADO y no plazo. Esta vuelta "
             "no la reabre, y los arneses que escribe hoy entran con la misma vara."),
    "6.11": ("EJECUTADA, TAREA 4.b de esta vuelta, POR ADICION Y SIN TOCAR LA LETRA "
             "VIEJA. El `81` de `docs/plan/00_INDICE.md:644`, cierto en su corte del 19 "
             "ago 2026, gana al lado la cifra que el mismo instrumento mide hoy, por "
             "`9.21`. Se hace DESPUES de la TAREA 2 porque el contador es el mismo "
             "instrumento que la TAREA 2 limpia, y una cifra medida sobre un "
             "instrumento envenenado no se publica."),
    "6.12": ("EJECUTADA, TAREA 5.c de esta vuelta, COMO BARRIDO MEDIDO Y CON SU COMANDO "
             "ESCRITO. Los 8 pares sin leer de `la supervision de la IA` se buscan uno "
             "a uno en `nodos`, `preservar`, `eliminar` y `superviviente` de las 71 "
             "fichas de `docs/plan/OPERACIONES.jsonl`. No se afirma que sean backlog "
             "nuevo, porque eso es lo que la busqueda tiene que decir: una busqueda "
             "negativa no se puede citar."),
}

QUE_HACE_CON_LA_CAIDA = {
    "CAIDA 1": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. Y SE REGISTRA AUNQUE NO LLEGARA A "
                "PUBLICARSE: el auditor escribio un contador casero de tachadas para no "
                "importar el del ejecutor y le dio 20 donde el instrumento dice 12. Lo "
                "vio antes de publicarlo y rehizo el conteo sobre la fila correcta. Lo "
                "que ensena es la misma `P.1` de siempre, dicha para las varas de "
                "texto: un contador casero al lado de uno ya probado no es "
                "verificacion, es una segunda opinion sin credenciales."),
    "CAIDA 2": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. Dos trazas por teclear de memoria la "
                "forma de un fichero que tenia delante (clave `nodes` en el grafo, "
                "clave `id` en las fichas). NINGUNA CIFRA SALIO DE AHI. Es el mismo "
                "vicio que la campana persigue: mirar el fichero antes de contarlo."),
    "CAIDA 3": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. La bateria se corrio con las suites de la "
                "web y el aislador al lado, y ella misma lo cazo: su contador de RUIDO "
                "DE CONCURRENCIA marca 6 ficheros y los seis son del auditor. El verde "
                "se sostiene por `NO REPRODUCIBLE` en cero sobre 75 entradas, y el "
                "propio auditor dice que eso es un argumento y no una excusa. Esta "
                "vuelta no rehace esa corrida: la cita con su atribucion en la seccion "
                "9 del reporte de la 170 y no la copia como propia."),
    "CAIDA 4": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya, PERO ES LA UNICA DE LAS CUATRO QUE LE "
                "COSTO CODIGO A ESTA VUELTA, Y ESO SE DICE AQUI PORQUE EL ACTA NO PODIA "
                "SABERLO. El asunto del commit del acta (`d7b18370`) salio con una "
                "arroba suelta delante del titulo y otra detras, por sintaxis de "
                "here-string de PowerShell colada en bash; el acta declara que el texto "
                "es correcto y que no reescribe la rama, y esta vuelta lo respeta. LA "
                "CONSECUENCIA MECANICA QUE AQUELLA DECLARACION NO MIDIO: los "
                "instrumentos de la casa localizan el commit del acta exigiendo que el "
                "asunto EMPIECE por su titulo, y con la arroba delante eso da CERO "
                "(medido: de 400 asuntos, 0 empiezan por el titulo y 1 lo contiene). "
                "Sin remedio, la fila de identidad de la cabecera de esta vuelta se "
                "cae entera. El remedio es el mismo y por el mismo motivo que la "
                "segunda forma del titulo de la vuelta 106: la casa no reescribe la "
                "historia, ADAPTA LA BUSQUEDA. `tallar_cabecera_reporte.py:buscar_acta` "
                "hace dos pasadas, la estricta primero y la suelta SOLO si la estricta "
                "da cero, y las dos exigen UN SOLO acierto, asi que cero sigue siendo "
                "ROJO y dos siguen siendo ROJO. Con su caso positivo por mutacion."),
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


def _sin_vineta(trozo):
    """Recorta la vineta de lista para que la negrita empiece en la columna 0.
    Sin esto, el titulo de una caida del acta 170 saldria con el guion pegado."""
    return re.sub(r"^-\s+", "", trozo.strip())


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
        trozo = _linea_de_negrita(lineas[j], j == ln - 1)
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


def _linea_de_negrita(linea, es_la_primera):
    """La primera linea pierde su vineta; las de continuacion se dejan tal cual
    (una vineta en una linea de continuacion seria otra entrada, no esta)."""
    return _sin_vineta(linea) if es_la_primera else linea.strip()


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


def _cuenta_caidas(lineas, inicio, fin):
    return len([i for i in range(inicio, fin + 1) if PAT_CAIDA.match(lineas[i - 1])])


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
    viejo = re.compile(r"^\s*\*\*CAIDA \d[,.]")
    n_viejo = len([i for i in range(inicio, fin + 1) if viejo.match(lineas[i - 1])])
    encontradas = [i for i in range(inicio, fin + 1) if PAT_CAIDA.match(lineas[i - 1])]
    print("   CIFRA con el patron VIEJO (el del acta 169): %d" % n_viejo)
    print("   CIFRA con el patron NUEVO (las dos formas):  %d" % len(encontradas))
    print("   (la diferencia es la que el docstring predice: el acta 170 escribe")
    print("    sus caidas como vineta y con comillas inversas)")
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
        m = PAT_CAIDA.match(lineas[ln0 - 1])
        clave = "CAIDA %s" % m.group(1)
        patron = re.compile(r"^\s*(?:-\s+)?\*\*`?%s`?[,.]" % re.escape(clave))
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
        "Por adicion, como `R.21` a `R.39`. **Corte de todas las cifras de esta entrada:\n"
        "4 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa\n"
        "`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.\n"
        "La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, leida hoy\n"
        "en `docs/loop/ACTA_AUDITOR.md:%d`. Salida:\n"
        "`docs/loop/SALIDA_V%d_T1A_REGISTRO_ACTA_%d.txt`.\n\n"
        % (numero, titulo_entrada, VUELTA_DEL_ACTA, VUELTA_QUE_ESCRIBE,
           todas[0], VUELTA_QUE_ESCRIBE, VUELTA_DEL_ACTA))
    trozos.append(
        "**Y LAS DOS CIFRAS DEL TITULO TAMPOCO ESTAN TECLEADAS:** se cuentan del acta\n"
        "(%d adjudicaciones `6.n` y %d negritas `CAIDA n` dentro del cuerpo acotado,\n"
        "lineas %d a %d) y de ahi sale el numeral en palabra, **incluida la\n"
        "concordancia**. **EL `R.39` REGISTRO DOCE Y TRES; ESTE REGISTRA %d Y %d.**\n\n"
        "**Y AQUI HAY UNA ADAPTACION DE PATRON QUE SE DECLARA EN VEZ DE PASAR CALLANDO,\n"
        "PORQUE UN PATRON QUE SE AFLOJA SIN DECIRLO ES UNA GUARDA MENOS.** El acta 169\n"
        "escribia sus caidas como `**CAIDA 1. ...**` al principio de linea; el acta 170\n"
        "las escribe como vineta y con comillas inversas, ``- **`CAIDA 1`. ...**``. El\n"
        "patron de la vuelta 170, corrido sobre el acta 170, cuenta **%d**; el de esta\n"
        "vuelta, que acepta la vineta y las comillas como OPCIONALES, cuenta **%d**. Las\n"
        "dos cifras se publican al lado y el arnes hermano prueba por mutacion que el\n"
        "patron nuevo casa con **las dos formas** y sigue exigiendo la negrita, el\n"
        "numero y el signo detras: adaptar no es aflojar.\n\n"
        % (n_adj, n_cai, inicio, fin, n_adj, n_cai, n_viejo, n_cai))
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
        "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no se toca. **Ningun `estado` de\n"
        "`docs/plan/OPERACIONES.jsonl` se mueve por esta entrada**: el campo sigue\n"
        "jubilado como historico y la vara del trabajo pendiente sigue siendo\n"
        "`scripts/loop/vuelta150_3_relectura_expediente.py`. **Y las dos `OP-M-02`\n"
        "siguen sin ejecutarse**, por la `6.6` del acta 168. **Y `OP-L-03` queda abierta\n"
        "y leida y NO se ejecuta en esta vuelta**, por el tope de cinco tareas.\n"
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
# `vuelta171_tarea1a_mutacion_registro.py`, que es el que la bateria ve.
#
# CERO ESCRITURAS Y CERO FICHEROS: las actas de mentira se fabrican EN MEMORIA
# como listas de lineas.
#
# QUE MIDE DE NUEVO ESTA VUELTA, ademas de todo lo que la 170 ya tumbaba: que el
# patron de caida casa con LAS DOS FORMAS (la del acta 169 y la del acta 170),
# que NO casa con una negrita que no sea de caida, y que el titulo de una caida
# escrita como vineta sale SIN el guion de lista pegado delante.
#
# NINGUN VEREDICTO ES UNA CONSTANTE LITERAL.
# ---------------------------------------------------------------------------

FRONTERA_FALSA = "# ACTA DEL AUDITOR, VUELTA 171 (frontera de mentira)"
CABECERA_FALSA = CABECERA_ACTA + " (fabricada por la prueba de mutacion)"


def _acta_fabricada(adjudicaciones=12, caidas=4, sangria="  ", duplicar=None,
                    quitar=None, sin_cierre=False, forma="vineta"):
    """Un acta 170 DE MENTIRA, en memoria. Devuelve (lineas, inicio, fin).

    `forma` elige como se escriben las negritas de caida: "vineta" es la del
    acta 170 y "plana" es la del acta 169."""
    def caida(k):
        if forma == "vineta":
            return "%s- **`CAIDA %d`. TITULO DE LA CAIDA %d FABRICADA.** cuerpo" % (
                sangria, k, k)
        return "%s**CAIDA %d. TITULO DE LA CAIDA %d FABRICADA.** cuerpo" % (sangria, k, k)

    L = ["ruido de otra acta",
         "**6.1 ESTA NO CUENTA, VIVE FUERA DEL CUERPO.** ruido",
         "- **`CAIDA 1`. ESTA TAMPOCO, VIVE FUERA DEL CUERPO.** ruido",
         "",
         CABECERA_FALSA,
         "cuerpo cualquiera",
         "",
         "## 3. MIS CAIDAS PROPIAS, CON SU NOMBRE",
         ""]
    for k in range(1, caidas + 1):
        L.append(caida(k))
        L.append("")
    L.append("## 6. LAS ADJUDICACIONES")
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
    L.append("- **`CAIDA 9`. NI ESTA.** ruido de despues")
    return L, L.index(CABECERA_FALSA) + 1, L.index(FRONTERA_FALSA)


def prueba_de_mutacion():
    print("=" * 78)
    print("VUELTA 171, TAREA 1.a: CASO POSITIVO POR MUTACION DEL REGISTRADOR DEL ACTA 170")
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
    print("   acta de 14 con la 6.7 ausente -> el barrido ve %d" % vistas)
    casos.append(("C_para_en_el_hueco_y_ve_6", vistas, 6))
    Ld, id_, fd = _acta_fabricada(adjudicaciones=14, duplicar="6.5")
    dup = [c for c, n in claves_de_adjudicacion(Ld, id_, fd) if n != 1]
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
    casos.append(("D_sin_acotar_hay_ruido_de_caidas", _cuenta_caidas(L, 1, len(L)), 6))
    casos.append(("D_acotado_no_lo_ve", _cuenta_caidas(L, ini, fin), 4))
    casos.append(("D_sin_acotar_la_6_1_esta_tres_veces",
                  len([i for i in range(1, len(L) + 1)
                       if re.match(r"^\s*\*\*6\.1 ", L[i - 1])]), 3))
    print("   sin acotar: %d negritas CAIDA | acotado: %d"
          % (_cuenta_caidas(L, 1, len(L)), _cuenta_caidas(L, ini, fin)))
    print("")

    print("E) EL PATRON DE CAIDA CASA CON LAS DOS FORMAS, Y ES LO NUEVO DE HOY")
    Lv, iv, fv = _acta_fabricada(caidas=4, forma="vineta")
    Lp, ip, fp = _acta_fabricada(caidas=4, forma="plana")
    viejo = re.compile(r"^\s*\*\*CAIDA \d[,.]")
    n_v_nuevo = _cuenta_caidas(Lv, iv, fv)
    n_p_nuevo = _cuenta_caidas(Lp, ip, fp)
    n_v_viejo = len([i for i in range(iv, fv + 1) if viejo.match(Lv[i - 1])])
    n_p_viejo = len([i for i in range(ip, fp + 1) if viejo.match(Lp[i - 1])])
    print("   forma VINETA (acta 170): patron nuevo %d, patron viejo %d"
          % (n_v_nuevo, n_v_viejo))
    print("   forma PLANA  (acta 169): patron nuevo %d, patron viejo %d"
          % (n_p_nuevo, n_p_viejo))
    casos.append(("E_el_patron_nuevo_ve_las_vineta", n_v_nuevo, 4))
    casos.append(("E_el_patron_nuevo_ve_las_planas", n_p_nuevo, 4))
    casos.append(("E_el_patron_VIEJO_NO_ve_las_vineta", n_v_viejo, 0))
    casos.append(("E_el_patron_viejo_si_ve_las_planas", n_p_viejo, 4))
    ruido = ["- **`CAIDAS 3`. plural, no es una caida.** x",
             "- **`CAIDA X`. sin numero.** x",
             "- **`CAIDA 3` sin puntuacion detras** x",
             "- `CAIDA 3`. sin negrita x"]
    casos.append(("E_no_casa_con_negritas_que_no_son_caida",
                  len([l for l in ruido if PAT_CAIDA.match(l)]), 0))
    _h, _e = titulo_de_la_negrita(Lv, iv, fv,
                                  re.compile(r"^\s*(?:-\s+)?\*\*`?CAIDA 2`?[,.]"), "CAIDA 2")
    titulo_v = _h[1] if _h else ""
    print("   titulo leido de una caida con vineta: %r" % titulo_v)
    casos.append(("E_el_titulo_sale_sin_el_guion_de_lista",
                  titulo_v, "`CAIDA 2`. TITULO DE LA CAIDA 2 FABRICADA."))
    print("")

    print("F) EL TITULO SIGUE A LOS DOS CONTEOS Y CONCUERDA EN NUMERO")
    for na, nc, esperado in ((6, 2, "seis"), (9, 1, "nueve"), (12, 4, "doce"),
                             (14, 3, "catorce")):
        t = titulo_de_la_entrada(na, nc)
        print("   (%d, %d) -> %s" % (na, nc, t))
        casos.append(("F_titulo_%d_%d_dice_%s" % (na, nc, esperado),
                      t.split()[3], esperado))
    casos.append(("F_la_rama_de_UNA_caida_va_en_singular",
                  "y la caida propia del acta" in titulo_de_la_entrada(9, 1), True))
    casos.append(("F_la_rama_de_CUATRO_va_en_plural",
                  "y las cuatro caidas propias del acta" in titulo_de_la_entrada(9, 4),
                  True))
    casos.append(("F_titulo_12_3_no_es_igual_al_de_12_4",
                  titulo_de_la_entrada(12, 3) == titulo_de_la_entrada(12, 4), False))
    print("")

    print("G) UNA ADJUDICACION O UNA CAIDA SIN GLOSA TIENE QUE PARAR")
    L17, i17, f17 = _acta_fabricada(adjudicaciones=17, caidas=6)
    claves17 = [c for c, _n in claves_de_adjudicacion(L17, i17, f17)]
    sin_glosa = [c for c in claves17 if c not in QUE_HACE_ESTA_VUELTA]
    print("   claves del acta de 17 sin glosa: %s" % (", ".join(sin_glosa) or "ninguna"))
    casos.append(("G_las_adjudicaciones_sin_glosa_se_detectan", len(sin_glosa), 5))
    claves_c17 = ["CAIDA %s" % PAT_CAIDA.match(L17[i - 1]).group(1)
                  for i in range(i17, f17 + 1) if PAT_CAIDA.match(L17[i - 1])]
    sin_glosa_c = [c for c in claves_c17 if c not in QUE_HACE_CON_LA_CAIDA]
    casos.append(("G_las_caidas_sin_glosa_se_detectan", len(sin_glosa_c), 2))
    L6, i6, f6 = _acta_fabricada(adjudicaciones=12, caidas=4)
    casos.append(("G_las_doce_de_hoy_SI_tienen_glosa",
                  len([c for c, _n in claves_de_adjudicacion(L6, i6, f6)
                       if c not in QUE_HACE_ESTA_VUELTA]), 0))
    print("")

    print("H) EL ACTA DE VERDAD, LEIDA HOY")
    RL, ri, rf = cuerpo_del_acta()
    print("   cuerpo del acta 170: lineas %d a %d" % (ri, rf))
    reales = claves_de_adjudicacion(RL, ri, rf)
    n_adj = len(reales)
    n_cai = _cuenta_caidas(RL, ri, rf)
    n_cai_viejo = len([i for i in range(ri, rf + 1) if viejo.match(RL[i - 1])])
    print("   CIFRA adjudicaciones 6.n que trae la seccion 6: %d" % n_adj)
    print("   CIFRA caidas con el patron nuevo: %d | con el viejo: %d"
          % (n_cai, n_cai_viejo))
    casos.append(("H_el_acta_170_trae_DOCE_adjudicaciones", n_adj, 12))
    casos.append(("H_cada_una_aparece_una_sola_vez",
                  len([c for c, n in reales if n != 1]), 0))
    casos.append(("H_el_acta_170_trae_CUATRO_caidas", n_cai, 4))
    casos.append(("H_y_el_patron_viejo_no_habria_visto_ninguna", n_cai_viejo, 0))
    todas = [i for i, l in enumerate(RL, 1) if FRASE_DE_LA_SEDE in l]
    casos.append(("H_la_frase_de_la_sede_esta_una_vez_en_el_fichero", len(todas), 1))
    casos.append(("H_y_cero_veces_dentro_del_acta_170",
                  len([i for i in todas if ri <= i <= rf]), 0))
    patrones = [(re.compile(r"^\s*\*\*%s " % re.escape(c)), c) for c, _n in reales]
    patrones += [(re.compile(r"^\s*(?:-\s+)?\*\*`?CAIDA %d`?[,.]" % k), "CAIDA %d" % k)
                 for k in range(1, n_cai + 1)]
    sin_error = 0
    for pat, et in patrones:
        _h, e = titulo_de_la_negrita(RL, ri, rf, pat, et)
        if e is None:
            sin_error += 1
    print("   CIFRA negritas que se leen sin error: %d de %d"
          % (sin_error, len(patrones)))
    casos.append(("H_las_dieciseis_negritas_se_leen_sin_error", sin_error, 16))
    casos.append(("H_el_titulo_que_saldra_dice_doce_y_cuatro",
                  titulo_de_la_entrada(n_adj, n_cai),
                  "Registro de las doce adjudicaciones y las cuatro caidas propias "
                  "del acta de la vuelta 170"))
    suben_reales = sorted(c for c, v in VIA.items() if v.startswith("AL FUNDADOR"))
    casos.append(("H_las_vias_reales_no_suben_NINGUNA_al_fundador", len(suben_reales), 0))
    ejecutadas = sorted(c for c, v in VIA.items() if v == "EJECUTADA")
    casos.append(("H_el_reparto_real_da_OCHO_ejecutadas", len(ejecutadas), 8))
    sin_tocar = sorted(c for c, v in VIA.items() if v == "SIN TOCAR NADA")
    casos.append(("H_y_CUATRO_sin_tocar_nada", len(sin_tocar), 4))
    casos.append(("H_y_las_dos_vias_suman_las_doce",
                  len(ejecutadas) + len(sin_tocar), 12))
    print("")

    print("I) PASADA 1, LOS CASOS TAL CUAL")
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

    print("J) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
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
    sys.stdout.reconfigure(encoding="utf-8")
    if "--mutar" in sys.argv:
        sys.exit(prueba_de_mutacion())
    sys.exit(main())
