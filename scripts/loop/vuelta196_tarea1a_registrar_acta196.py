# -*- coding: utf-8 -*-
r"""vuelta196_tarea1a_registrar_acta196.py . EL ACTA 196 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA, Y ESTE REGISTRADOR SIGUE SIENDO IDEMPOTENTE.

LA MAQUINA SE IMPORTA Y NO SE COPIA. Todo lo generico (acotar el acta, leer
secciones, familia y estado de una adjudicacion, filas de la tabla de credito,
numerales, expansion de rangos, la serie) sale de
`vuelta192_tarea1a_registrar_acta192.py`, y las piezas de la 194 y la 195 se
importan tal cual. AQUI SOLO VIVE LO QUE EL ACTA 196 TIENE DISTINTO, y va dicho
uno por uno para que nadie tenga que adivinarlo. CADA UNO DE LOS SEIS TROZOS
NUEVOS TRAE DELANTE LA CIFRA QUE LO JUSTIFICA, medida sobre el acta y no supuesta:

  1. LAS ADJUDICACIONES VIENEN EN DOS FORMAS Y NO EN UNA. Las `4.1` a `4.7` son
     LEAD DE PARRAFO (``**`4.1` TITULO...**``), que es la forma que
     `claves_entrecomilladas` ya sabe leer. Las `4.8` a `4.14` son CLAVE SOLA EN
     NEGRITA Y EN MITAD DE UN PARRAFO (``**`4.8`** `D.1`, ...``), y sobre esa
     forma el lector heredado NO CASA: exige un espacio detras de la comilla de
     cierre y ahi hay un asterisco. MEDIDO: el heredado, corrido tal cual sobre
     esta acta, se para en la `4.8` y devuelve SIETE donde el acta declara
     CATORCE. `claves_en_negrita_sola()` lee la segunda forma. **LAS DOS CIFRAS
     SE PUBLICAN Y NINGUN LECTOR SE RETIRA.**

  2. EL ESTADO DE UNA ADJUDICACION PUEDE VIVIR EN EL PARRAFO Y NO EN EL TITULO.
     El titulo de la `4.1` es *"EL `976`, Y ES MI CAIDA POR LA MISMA PUERTA..."*
     y su veredicto, **A FAVOR DEL ARCHIVO**, esta al final del parrafo. MEDIDO:
     con el titulo y nada mas saldrian `SIN DECIR` las que la salida publica, y
     este registrador PARARIA. `estado_con_su_procedencia()` corre PRIMERO el
     vocabulario heredado sobre el TITULO, entero y sin tocar, y solo si sale
     `SIN DECIR` lee el PARRAFO. **Y PUBLICA DE DONDE SALIO CADA ESTADO**, que es
     la unica forma de que ensanchar la ventana no sea aflojar la guarda: una
     adjudicacion sin estado NI EN EL TITULO NI EN EL PARRAFO sigue saliendo
     `SIN DECIR` y sigue haciendo PARAR.

  3. UNA MARCA DE ESTADO NUEVA, LITERAL DEL ACTA: `VA CONTRA EL EJECUTOR`, que es
     como el acta 196 contesta la `P.3`. Con el vocabulario heredado esa saldria
     `SIN DECIR`: el acta escribe *"CONTESTADA POR EXTENSION"* y la marca vieja
     es `POR EXTENSION CITABLE`. **SE ANADE, NO SE ENSANCHA**, y `EN CONTRA` y
     `A FAVOR` siguen yendo primero y en ese orden.

  4. LAS CAIDAS SON TITULARES `###` Y SU CLAVE LLEVA LETRA: `C.E1` y `C.A1`. El
     patron heredado es ``^\s*\*\*`C\.(\d+)``` y no casa ni con el titular ni con
     la letra. MEDIDO: sobre esta acta devuelve CERO y el registrador PARARIA
     sobre un acta que declara DOS con toda claridad.
     `caidas_en_titular_con_letra()` las lee, y `parte_de_la_caida()` reparte por
     LO QUE EL PROPIO TITULO DICE (`DEL EJECUTOR` contra `MIA`), no por su
     posicion. **UNA CAIDA SIN PARTE DECLARADA HACE PARAR.**

  5. LA FILA DE CAIDAS DE METODO DEL EJECUTOR NO NOMBRA SUS CLAVES. El acta 195
     escribia `**0 nuevas**` y nombraba el rango; la 196 escribe *"**4**, las
     cuatro declaradas por el y cazadas dentro de la vuelta"* SIN nombrar `C.1` a
     `C.4`, porque esas cuatro son del REPORTE del ejecutor y no del cuerpo del
     acta. MEDIDO: el cotejo heredado compara claves del rango contra el numeral
     y daria 0 contra 4, o sea PARADA sobre un acta correcta. **LA EXIGENCIA SE
     HACE CONDICIONAL A QUE LA FILA NOMBRE ALGUNA CLAVE, Y EN ESA RAMA SIGUE
     ENTERA**: si nombra claves y no calzan, se para igual. **Lo que se estrecha
     es el caso, no la guarda**, que es la misma decision que la 195 tomo con el
     cotejo limpio.

  6. EL COTEJO LIMPIO NO VIVE EN LA FILA DE PUESTOS, VIVE EN LA SECCION 2. El
     acta 196 mide DOS QUEMADOS y su fila de puestos no escribe
     `cotejo limpio va sobre N`, asi que la exigencia de la 195 PARARIA. Pero el
     acta SI publica el cotejo limpio, en la cabecera de su tabla de la seccion 2
     (*"sobre los 58 sin quemados"*). `cotejo_limpio_del_cuerpo()` lo busca en el
     ACTA ENTERA, y la exigencia **se endurece en vez de aflojarse**: ya no basta
     con que el literal este, ahora tiene que CALZAR con `cotejados - quemados`.

EL SUJETO DE CADA CIFRA SE CUENTA DEL CUERPO ACOTADO DEL ACTA, y el cuerpo se
acota AQUI con `R92.cuerpo_del_acta`, no por la linea que el encargo cita: el
fichero puede haber crecido y una linea heredada es una cifra sin medir.

USO:
  python scripts/loop/vuelta196_tarea1a_registrar_acta196.py
  python scripts/loop/vuelta196_tarea1a_registrar_acta196.py --simular
  python scripts/loop/vuelta196_tarea1a_registrar_acta196.py --mutacion
"""
import argparse
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402
import vuelta192_tarea1a_registrar_acta192 as R92   # noqa: E402
import vuelta194_tarea1a_registrar_acta194 as R94   # noqa: E402
import vuelta195_tarea1a_registrar_acta195 as R95   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 196
VUELTA_QUE_ESCRIBE = 196
SUFIJO_QUE_ESCRIBE = "196"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "4."
PREFIJO_HALLAZGO = "5."
SECCION_DE_LOS_HALLAZGOS = 5
SECCION_DE_LAS_CAIDAS = 3
SECCION_DE_LA_METRICA = 7

# LA NOTA DE LA FILA DE PUESTOS QUE ESTA ACTA ESTRENA, LITERAL DE SU CELDA. Las
# tres heredadas se siguen buscando y sus cifras se publican.
NOTA_DE_PUESTOS_196 = "quemados"

AGUJA_FILA_AUD_ACUMULAN = R95.AGUJA_FILA_AUD_ACUMULAN
AGUJA_FILA_AUD_TOTAL = R95.AGUJA_FILA_AUD_TOTAL
AGUJA_FILA_CAIDAS_REPORTE = R95.AGUJA_FILA_CAIDAS_REPORTE
AGUJA_FILA_CAIDAS_CIFRA = R95.AGUJA_FILA_CAIDAS_CIFRA

MARCA_ESPECIE_METODO = R92.MARCA_ESPECIE_METODO
MARCA_ESPECIE_CIFRA = R92.MARCA_ESPECIE_CIFRA
MARCA_ESPECIE_REMEDIO = R94.MARCA_ESPECIE_REMEDIO
MARCAS_DE_ESPECIE_196 = (MARCA_ESPECIE_CIFRA, MARCA_ESPECIE_METODO,
                         MARCA_ESPECIE_REMEDIO)

# EL ARNES DE LA 191 QUE YA CUBRE EL CERO DE `EN CONTRA`, NOMBRADO PARA MEDIRLO
# EN VEZ DE RE FABRICAR SU CASO. Es la SEXTA acta seguida con cero.
ARNES_QUE_YA_CUBRE = "docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt"

# LA MARCA DE ESTADO QUE EL ACTA 196 ESTRENA, LITERAL DE SU `4.7`.
MARCA_CONTRA_EL_EJECUTOR = "VA CONTRA EL EJECUTOR"
MARCAS_NUEVAS_196 = (MARCA_CONTRA_EL_EJECUTOR,)

# LAS DOS MARCAS DE PARTE, LITERALES DE LOS DOS TITULARES DE LA SECCION 3.
MARCA_PARTE_EJECUTOR = "DEL EJECUTOR"
MARCA_PARTE_AUDITOR = "MIA"

# LOS DOS PATRONES QUE ESTA ACTA OBLIGA A ESCRIBIR.
PAT_CAIDA_TITULAR = re.compile(r"^\s*#{2,4}\s*`C\.([A-Z]?\d+)`")
PAT_COTEJO_LIMPIO = re.compile(r"sobre los\s+(\d+)\s+sin quemados")


def claves_en_negrita_sola(lineas, inicio, fin, prefijo, tope=40):
    """LAS ADJUDICACIONES ESCRITAS ``**`4.8`**``, o sea LA CLAVE SOLA EN NEGRITA
    Y EN MITAD DE UN PARRAFO, que es la forma con que el acta 196 numera sus
    siete discutibles. PURA. Devuelve [(clave, apariciones)].

    ES UN PATRON NUEVO Y NO UN ENSANCHE DEL VIEJO: `claves_entrecomilladas` sigue
    intacta y su cifra sobre esta acta se publica al lado.

    NO SE PARA EN EL PRIMER HUECO, y esa es la otra diferencia: el heredado corta
    la busqueda en cuanto una clave da cero, y aqui las siete que interesan
    empiezan en la `4.8`, o sea DESPUES del hueco que deja la otra forma. Se
    recorre el tope entero y se devuelve lo que haya."""
    claves = []
    for k in range(1, tope + 1):
        clave = "%s%d" % (prefijo, k)
        pat = re.compile(r"\*\*`%s`\*\*" % re.escape(clave))
        cuantas = sum(len(pat.findall(lineas[i - 1]))
                      for i in range(inicio, fin + 1))
        if cuantas:
            claves.append((clave, cuantas))
    return claves


def parrafo_que_empieza(lineas, ini, fin, ln):
    """EL PARRAFO QUE EMPIEZA EN LA LINEA `ln`: se acumula hasta la primera linea
    en blanco o hasta el fin del rango. PURA. Devuelve el texto en una sola linea.

    LA VENTANA ES EL PARRAFO Y NO LA LINEA porque el markdown parte las frases
    donde le cabe el ancho, y el veredicto de la `4.1` vive cuatro lineas mas
    abajo que su titulo."""
    trozos = []
    j = ln
    while j <= fin and lineas[j - 1].strip():
        trozos.append(lineas[j - 1].strip())
        j += 1
    return re.sub(r"\s+", " ", " ".join(trozos)).strip()


def parrafo_que_contiene(lineas, ini, fin, ln):
    """EL PARRAFO ENTERO AL QUE PERTENECE LA LINEA `ln`, hacia arriba y hacia
    abajo hasta las lineas en blanco. PURA.

    HACE FALTA PARA LA SEGUNDA FORMA: la `4.9` no empieza parrafo, empieza en
    mitad de uno, y el parrafo que la contiene es el que trae su veredicto."""
    a = ln
    while a > ini and lineas[a - 2].strip():
        a -= 1
    b = ln
    while b < fin and lineas[b].strip():
        b += 1
    return parrafo_que_empieza(lineas, ini, fin, a)


def trozo_de_la_clave_inline(parrafo, clave, todas):
    """EL TROZO DE PARRAFO QUE LE TOCA A UNA CLAVE ESCRITA ``**`4.n`**``. PURA.

    Va desde su propia marca hasta la marca de la clave SIGUIENTE que aparezca
    en el parrafo, o hasta el final. Devuelve "" si la marca no esta.

    POR QUE SE PARTE Y NO SE LEE EL PARRAFO ENTERO: las siete comparten UN SOLO
    parrafo, y darle a cada una el parrafo completo le daria a la `4.8` los
    veredictos de las otras seis. Un veredicto prestado no es un veredicto."""
    marcas = []
    for c in todas:
        m = re.search(r"\*\*`%s`\*\*" % re.escape(c), parrafo)
        if m:
            marcas.append((m.start(), c))
    marcas.sort()
    for idx, (pos, c) in enumerate(marcas):
        if c != clave:
            continue
        fin = marcas[idx + 1][0] if idx + 1 < len(marcas) else len(parrafo)
        return parrafo[pos:fin].strip()
    return ""


def estado_de_la_adjudicacion_196(texto):
    """EL ESTADO, LEIDO DE UN TEXTO. PURA.

    PRIMERO CORRE EL VOCABULARIO HEREDADO ENTERO (`R92.estado_de_la_adjudicacion`,
    doce marcas) y solo si ese devuelve `SIN DECIR` prueba la de esta acta. Ese
    orden importa: un texto que diga `EN CONTRA` tiene que salir `EN CONTRA`
    aunque tambien traiga la nueva."""
    heredado = R92.estado_de_la_adjudicacion(texto)
    if heredado != "SIN DECIR":
        return heredado
    if MARCA_CONTRA_EL_EJECUTOR in texto.upper():
        return "CONTESTADA POR EXTENSION Y EN CONTRA DEL EJECUTOR"
    return "SIN DECIR"


def estado_con_su_procedencia(titulo, parrafo):
    """EL ESTADO Y DE DONDE SALIO. PURA. Devuelve (estado, procedencia).

    `procedencia` vale `TITULO`, `PARRAFO` o `NINGUNA`. **LA VENTANA SE ENSANCHA
    Y LA GUARDA NO SE AFLOJA**: el titulo se lee primero y entero, el parrafo
    solo se mira si el titulo calla, y un texto que no diga nada en ninguno de
    los dos sigue saliendo `SIN DECIR` para que quien llame PARE."""
    e1 = estado_de_la_adjudicacion_196(titulo)
    if e1 != "SIN DECIR":
        return e1, "TITULO"
    e2 = estado_de_la_adjudicacion_196(parrafo)
    if e2 != "SIN DECIR":
        return e2, "PARRAFO"
    return "SIN DECIR", "NINGUNA"


def familia_por_la_primera_clave(texto):
    """SI UNA ADJUDICACION ES UN DISCUTIBLE O UNA PREGUNTA, LEIDO DE LA PRIMERA
    CLAVE QUE NOMBRA. PURA. Devuelve `DISCUTIBLE`, `PREGUNTA` u `OTRA`.

    POR QUE NO VALE LA MAQUINA HEREDADA, Y ESTA MEDIDO SOBRE ESTA ACTA: la
    heredada mira si el texto nombra ALGUN `P.n` y, si lo hace, gana la pregunta.
    La `4.10` del acta 196 dice *"`D.3`, declarar sujeto congelado en cuatro...,
    y su riesgo declarado es la `P.2` que adjudico en el `4.6`"*: adjudica un
    DISCUTIBLE y de paso CITA una pregunta ya adjudicada. Con el lector heredado
    sale PREGUNTA, y el registro publicaria CUATRO preguntas donde el acta
    declara TRES.

    LA REGLA ES LA DEL ACTA Y NO UNA INVENCION: **la clave que adjudica es la
    PRIMERA que la adjudicacion nombra**, porque asi las escribe todas
    (``**`4.10`** `D.3`, ...``). Una cita posterior es una cita, no el sujeto.

    UN TEXTO QUE NO NOMBRE NINGUNA SIGUE SALIENDO `OTRA`, que es lo que les toca
    a las cuatro discrepancias de la propia ciega del auditor."""
    m = re.search(r"`([DP])\.(\d+)`", texto)
    if not m:
        return "OTRA"
    return "PREGUNTA" if m.group(1) == "P" else "DISCUTIBLE"


def caidas_en_titular_con_letra(lineas, ini, fin):
    """LAS CAIDAS ESCRITAS ``### `C.E1` TITULO``. PURA.
    Devuelve [(clave, linea, titulo_literal)].

    DOS COSAS A LA VEZ, Y LAS DOS SON DEL ACTA 196: el titular `###` en vez de la
    negrita de lead, y la LETRA dentro de la clave (`C.E1` del ejecutor, `C.A1`
    del auditor), que el patron heredado, de solo digitos, no admite.

    EL RANGO ES PARAMETRO: este lector no supone que la sede sea la seccion 3."""
    salida = []
    for i in range(ini, fin + 1):
        m = PAT_CAIDA_TITULAR.match(lineas[i - 1])
        if m:
            salida.append(("C.%s" % m.group(1), i, lineas[i - 1].strip()))
    return salida


def parte_de_la_caida(titulo):
    """DE QUIEN ES UNA CAIDA, LEIDO DE SU PROPIO TITULO. PURA.

    Devuelve `EJECUTOR`, `AUDITOR` o `SIN DECIR`. La seccion 3 del acta 196
    guarda las de los DOS bajo un titulo que no atribuye
    (*"LAS CAIDAS DE ESTA VUELTA"*), asi que la atribucion NO se puede sacar de
    la seccion: sale de lo que cada titular dice de si mismo.

    `SIN DECIR` NO SE ADIVINA: quien llama para."""
    alto = titulo.upper()
    if MARCA_PARTE_EJECUTOR in alto:
        return "EJECUTOR"
    if re.search(r"\b%s\b" % MARCA_PARTE_AUDITOR, alto):
        return "AUDITOR"
    return "SIN DECIR"


def cotejo_limpio_del_cuerpo(lineas, ini, fin):
    """EL COTEJO LIMPIO, BUSCADO EN EL ACTA ENTERA Y NO SOLO EN SU FILA DE
    PUESTOS. PURA. Devuelve [(linea, cifra)].

    POR QUE SE ENSANCHA LA BUSQUEDA Y SE ENDURECE LA EXIGENCIA: el acta 196 mide
    DOS quemados y su fila de puestos no escribe `cotejo limpio va sobre N`, asi
    que la exigencia de la 195 PARARIA sobre un acta que SI publica el cotejo
    limpio, en la cabecera de la tabla de su seccion 2. Aqui se busca donde el
    acta lo escribe **y ademas se exige que CALCE con `cotejados - quemados`**,
    cosa que la 195 no comprobaba: le bastaba con que el literal estuviera."""
    salida = []
    for i in range(ini, fin + 1):
        for m in PAT_COTEJO_LIMPIO.finditer(lineas[i - 1]):
            salida.append((i, int(m.group(1))))
    return salida


def _medir():
    """LA PRIMERA MITAD DE main(): acotar el acta y contar. Devuelve o bien un
    entero (codigo de salida, cuando hay PARADA) o bien la tupla
    (salida, medido)."""
    salida = []
    w = salida.append
    w("=" * 78)
    w("VUELTA %d, TAREA 1: EL ACTA %d ENTERA, REGISTRADA"
      % (VUELTA_QUE_ESCRIBE, VUELTA_DEL_ACTA))
    w("=" * 78)
    w("")

    lineas, rango, err = R92.cuerpo_del_acta(None, CABECERA_ACTA)
    if err:
        w(err)
        print(NL.join(salida))
        return 1
    inicio, fin = rango
    w("A) EL CUERPO DEL ACTA, ACOTADO ANTES DE CONTAR NADA")
    w("   acta %d: docs/loop/ACTA_AUDITOR.md, lineas %d a %d"
      % (VUELTA_DEL_ACTA, inicio, fin))
    w("   por `fin - inicio + 1` da %d lineas" % (fin - inicio + 1))
    w("   docs/loop/ACTA_AUDITOR.md -> disco %d bytes" % os.path.getsize(ACTA))
    w("   EL ENCARGO CITA LA LINEA 69019 Y AQUI SE RECUENTA: la cifra de arriba")
    w("   sale de R92.cuerpo_del_acta corrido HOY, no de la linea heredada.")
    secciones = R92.secciones_del_acta(lineas, inicio, fin)
    w("   SECCIONES `## n.` DEL ACTA, LEIDAS Y NO TECLEADAS: %s"
      % R92._lista(secciones))
    w("   Y LA SEDE DE LAS CAIDAS NO SE SUPONE: en el acta 196 es la seccion 3,")
    w("   titulada LAS CAIDAS DE ESTA VUELTA, y guarda las de LOS DOS lados.")
    w("")

    w("B) LA IDEMPOTENCIA, COMPROBADA ANTES DE MEDIR NADA MAS")
    sedes = {}
    for ruta in SERIE.SEDES:
        rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
        sedes[rel] = io.open(ruta, encoding="utf-8", errors="replace").read()
    marca_t, marca_c = R92.marcas_del_acta(VUELTA_DEL_ACTA)
    w("   las DOS sedes que se miran: %s" % ", ".join(sorted(sedes)))
    w("   las DOS marcas literales, computadas de la vuelta y no tecleadas:")
    w("      %r" % marca_t)
    w("      %r" % marca_c)
    ya = R92.entradas_que_registran(VUELTA_DEL_ACTA, sedes)
    w("   CIFRA lineas que ya registran el acta %d: %d" % (VUELTA_DEL_ACTA, len(ya)))
    for r, i, mk, t in ya:
        w("      %s:%d %r" % (r, i, t[:100]))
    w("   CIFRA bytes de docs/PENDIENTES.md ANTES de tocar nada: %d"
      % os.path.getsize(SEDE))
    w("")

    w("C) LAS ADJUDICACIONES, CONTADAS CON LOS TRES PATRONES Y NO TECLEADAS")
    entrecomilladas = R92.claves_entrecomilladas(lineas, inicio, fin, PREFIJO_ADJ)
    sueltas = R92.claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_ADJ)
    negrita_sola = claves_en_negrita_sola(lineas, inicio, fin, PREFIJO_ADJ)
    w("   patron CON comillas inversas y LEAD de parrafo (el del acta 184) -> %d"
      % len(entrecomilladas))
    for clave, cuantas in entrecomilladas:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    w("   patron SIN comillas inversas (el del acta 189) -> %d" % len(sueltas))
    w("   patron de CLAVE SOLA EN NEGRITA (el que esta acta obliga) -> %d"
      % len(negrita_sola))
    for clave, cuantas in negrita_sola:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    w("   EL ACTA 196 USA LAS DOS FORMAS: las 4.1 a 4.7 son lead de parrafo y las")
    w("   4.8 a 4.14 son clave sola en negrita, DENTRO DE UN SOLO PARRAFO. El")
    w("   lector heredado se para en la 4.8 y devuelve %d donde el acta declara"
      % len(entrecomilladas))
    w("   CATORCE. NINGUN LECTOR SE RETIRA Y LAS TRES CIFRAS SE PUBLICAN.")
    claves = list(entrecomilladas)
    ya_estan = set(c for c, _n in claves)
    for clave, cuantas in negrita_sola:
        if clave not in ya_estan:
            claves.append((clave, cuantas))
    claves.sort(key=lambda x: int(x[0].split(".")[1]))
    w("   LA UNION, ORDENADA POR SU NUMERO: %d claves -> %s"
      % (len(claves), ", ".join(c for c, _n in claves)))
    dobles = [c for c, n in claves if n != 1]
    if dobles:
        w("   PARADA: hay claves repetidas dentro del acta: %s" % ", ".join(dobles))
        print(NL.join(salida))
        return 1
    if not claves:
        w("   PARADA: ningun patron encuentra adjudicaciones y el acta 196 declara")
        w("   catorce. No se escribe una entrada con cero.")
        print(NL.join(salida))
        return 1
    w("")

    w("D) EL TITULO DE CADA ADJUDICACION, SU FAMILIA Y SU ESTADO CON PROCEDENCIA")
    adjudicaciones = []
    n_sin_decir_titulo = 0
    n_del_parrafo = 0
    n_familia_distinta = 0
    claves_inline = [c for c, _n in negrita_sola]
    for clave, _n in claves:
        if clave in ya_estan:
            pat = re.compile(r"^\s*\*\*`%s` " % re.escape(clave))
            res, err2 = R92.titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
            if err2:
                w("   %s -> %s" % (clave, err2))
                print(NL.join(salida))
                return 1
            ln, tit = res
            parrafo = parrafo_que_empieza(lineas, inicio, fin, ln)
            forma = "LEAD"
        else:
            pat = re.compile(r"\*\*`%s`\*\*" % re.escape(clave))
            hits = [i for i in range(inicio, fin + 1) if pat.search(lineas[i - 1])]
            if len(hits) != 1:
                w("   PARADA: %s aparece %d veces en negrita sola."
                  % (clave, len(hits)))
                print(NL.join(salida))
                return 1
            ln = hits[0]
            entero = parrafo_que_contiene(lineas, inicio, fin, ln)
            tit = trozo_de_la_clave_inline(entero, clave, claves_inline)
            parrafo = tit
            forma = "NEGRITA SOLA"
            if not tit:
                w("   PARADA: %s no deja trozo legible en su parrafo." % clave)
                print(NL.join(salida))
                return 1
        est_titulo = estado_de_la_adjudicacion_196(tit)
        if est_titulo == "SIN DECIR":
            n_sin_decir_titulo += 1
        est, proc = estado_con_su_procedencia(tit, parrafo)
        if proc == "PARRAFO":
            n_del_parrafo += 1
        fam_her = R92.familia_de_la_adjudicacion(tit)
        fam = familia_por_la_primera_clave(tit)
        if fam_her != fam:
            n_familia_distinta += 1
        adjudicaciones.append((clave, fam, est, ln, tit, forma, proc, fam_her))
        w("   %-5s linea %-6d [%-10s / %-46s] forma %s, estado del %s"
          % (clave, ln, fam, est[:46], forma, proc))
        if fam_her != fam:
            w("         LA FAMILIA HEREDADA DABA %s Y LA DE LA PRIMERA CLAVE DA %s"
              % (fam_her, fam))
        w("         %s" % tit[:150])
    w("   LA VENTANA DEL ESTADO SE ENSANCHA AL PARRAFO Y LA CIFRA VA DELANTE: con")
    w("   el titulo y nada mas saldrian SIN DECIR %d adjudicacion(es), y este"
      % n_sin_decir_titulo)
    w("   registrador PARARIA. %d estado(s) salieron del PARRAFO." % n_del_parrafo)
    w("   LA MARCA NUEVA ES LITERAL DEL ACTA Y NO PARAFRASIS: %s"
      % ", ".join(repr(x) for x in MARCAS_NUEVAS_196))
    w("   SE ANADE Y NO SE ENSANCHA: ninguna vieja se retira ni se recorta, y una")
    w("   adjudicacion muda en el titulo Y en el parrafo sigue haciendo PARAR.")
    w("   Y LA FAMILIA SALE DE LA PRIMERA CLAVE QUE LA ADJUDICACION NOMBRA, NO DE")
    w("   QUE NOMBRE ALGUNA `P.n`: la heredada y la nueva discrepan en %d de las"
      % n_familia_distinta)
    w("   %d, y la heredada publicaria una PREGUNTA de mas. LAS DOS SE CORREN Y"
      % len(adjudicaciones))
    w("   LAS DOS CIFRAS SE PUBLICAN; la heredada NO se retira.")
    sin_decir = [a[0] for a in adjudicaciones if a[2] == "SIN DECIR"]
    if sin_decir:
        w("   PARADA: %s esta en un estado que este registrador NO SABE LEER."
          % ", ".join(sin_decir))
        print(NL.join(salida))
        return 1
    discutibles = [a for a in adjudicaciones if a[1] == "DISCUTIBLE"]
    preguntas = [a for a in adjudicaciones if a[1] == "PREGUNTA"]
    otras = [a for a in adjudicaciones if a[1] == "OTRA"]
    a_favor = [a for a in discutibles if a[2] == "A FAVOR"]
    en_contra = [a for a in discutibles if a[2] == "EN CONTRA"]
    w("   REPARTO POR FAMILIA: discutibles %d | preguntas %d | otras %d"
      % (len(discutibles), len(preguntas), len(otras)))
    w("   DE LOS DISCUTIBLES: A FAVOR %d | EN CONTRA %d | otro estado %d"
      % (len(a_favor), len(en_contra),
         len(discutibles) - len(a_favor) - len(en_contra)))
    sin_sentido = [a for a in discutibles if a[2] not in ("A FAVOR", "EN CONTRA")]
    if sin_sentido:
        w("   PARADA: hay %d discutible(s) cuyo estado no es ni A FAVOR ni EN CONTRA:"
          % len(sin_sentido))
        for a in sin_sentido:
            w("      %s -> %s" % (a[0], a[4][:120]))
        print(NL.join(salida))
        return 1
    w("   EL CERO DE `EN CONTRA` ES UN RESULTADO Y NO UNA PARADA, Y VA POR LA")
    w("   SEXTA ACTA SEGUIDA. La guarda VIEJA de la 190 corrida aqui: %s"
      % ("PARARIA" if not en_contra else "no pararia"))
    w("   Y NO SE VUELVE A FABRICAR SU CASO: EL ARNES DE LA 191 YA LO CUBRE, Y")
    w("   AQUI SE MIDE SU FICHERO EN VEZ DE CREERLO.")
    p_arnes = os.path.join(RAIZ, ARNES_QUE_YA_CUBRE.replace("/", os.sep))
    if not os.path.exists(p_arnes):
        w("   PARADA: %s NO EXISTE. Una ruta que promete prueba y no existe es"
          % ARNES_QUE_YA_CUBRE)
        w("   CAIDA DE CIFRA (EJECUTOR.md 1), y no se cita.")
        print(NL.join(salida))
        return 1
    datos_arnes = io.open(p_arnes, "rb").read()
    lf_arnes = datos_arnes.replace(b"\r\n", b"\n")
    t_arnes = lf_arnes.decode("utf-8", errors="replace")
    ver_arnes = [l.strip() for l in t_arnes.split(NL)
                 if l.strip().startswith("VEREDICTO")]
    w("   %s -> disco %d bytes | LF %d bytes"
      % (ARNES_QUE_YA_CUBRE, len(datos_arnes), len(lf_arnes)))
    w("   su veredicto, leido del propio fichero: %r"
      % (ver_arnes[0] if ver_arnes else "(sin linea de veredicto)"))
    if len(datos_arnes) == 0 or not ver_arnes or "VERDE" not in ver_arnes[0]:
        w("   PARADA: el arnes que se cita como cobertura mide cero bytes o no sale")
        w("   verde. Una ruta que promete prueba sobre un vacio es CAIDA DE CIFRA.")
        print(NL.join(salida))
        return 1
    if not preguntas:
        w("   PARADA: ninguna adjudicacion nombra un `P.n` y el acta 196 declara")
        w("   TRES preguntas contestadas. No se escribe una lista vacia.")
        print(NL.join(salida))
        return 1
    w("")

    w("E) LOS HALLAZGOS DE LA SECCION %d, Y AQUI MANDA EL LECTOR VIEJO"
      % SECCION_DE_LOS_HALLAZGOS)
    her_sueltos = R92.claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_HALLAZGO)
    her_comillas = R92.claves_entrecomilladas(lineas, inicio, fin, PREFIJO_HALLAZGO)
    titulares = R94.hallazgos_en_titular(lineas, inicio, fin, PREFIJO_HALLAZGO)
    w("   LOS TRES LECTORES, CORRIDOS TAL CUAL, Y LAS TRES CIFRAS SE PUBLICAN:")
    w("      claves_de_adjudicacion(prefijo %r) -> %d" % (PREFIJO_HALLAZGO,
                                                          len(her_sueltos)))
    w("      claves_entrecomilladas(prefijo %r) -> %d" % (PREFIJO_HALLAZGO,
                                                          len(her_comillas)))
    w("      hallazgos_en_titular() (el de la 194)  -> %d" % len(titulares))
    w("   EL ACTA 196 ESCRIBE SUS HALLAZGOS EN NEGRITA DE APERTURA DE PARRAFO,")
    w("   asi que manda `claves_entrecomilladas`. NO SE RETIRA NINGUNO.")
    hallazgos = []
    for clave, _n in her_comillas:
        pat = re.compile(r"^\s*\*\*`%s` " % re.escape(clave))
        res, err3 = R92.titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err3:
            w("   %s -> %s" % (clave, err3))
            print(NL.join(salida))
            return 1
        ln, tit = res
        hallazgos.append((clave, ln, tit))
        w("      %-5s linea %-6d %s" % (clave, ln, tit[:120]))
    if not hallazgos:
        w("   PARADA: ningun lector encuentra hallazgos y el acta 196 declara TRES.")
        print(NL.join(salida))
        return 1
    fila_fuera = R92.fila_de_la_metrica(lineas, inicio, fin, R92.AGUJA_FILA_FUERA)
    for ln, txt in fila_fuera:
        w("   LA FILA QUE DECIDE (linea %d): %s" % (ln, txt))
    if len(fila_fuera) != 1:
        w("   PARADA: la fila %r aparece %d veces en la tabla de credito."
          % (R92.AGUJA_FILA_FUERA, len(fila_fuera)))
        print(NL.join(salida))
        return 1
    numeral = R92.numeral_de_la_fila(fila_fuera[0][1])
    w("   EL NUMERAL DE LA PROPIA FILA, LEIDO Y NO TECLEADO: %s" % numeral)
    if numeral is None:
        w("   PARADA: la fila no trae cifra en su celda.")
        print(NL.join(salida))
        return 1
    w("   LA FILA CUENTA JUNTAS LAS DISCREPANCIAS Y LOS HALLAZGOS, y por eso su")
    w("   numeral (%d) NO tiene por que igualar a las claves `5.n` (%d)."
      % (numeral, len(hallazgos)))
    n_disc_fuera = numeral - len(hallazgos)
    w("   CIFRA discrepancias fuera del marcado, por resta: %d" % n_disc_fuera)
    if n_disc_fuera < 0:
        w("   PARADA: la resta da negativo. El numeral y las claves no cuadran de")
        w("   ninguna forma y no se elige a ojo.")
        print(NL.join(salida))
        return 1
    w("")

    w("F) LAS CAIDAS DE LA SECCION %d, DE LOS DOS LADOS Y REPARTIDAS POR SU TITULO"
      % SECCION_DE_LAS_CAIDAS)
    r3 = R92.rango_de_seccion(lineas, inicio, fin, SECCION_DE_LAS_CAIDAS)
    if r3 is None:
        w("   PARADA: el acta no tiene seccion %d." % SECCION_DE_LAS_CAIDAS)
        print(NL.join(salida))
        return 1
    ini3, fin3 = r3
    cabecera3 = lineas[ini3 - 1].strip()
    w("   la seccion %d va de la linea %d a la %d"
      % (SECCION_DE_LAS_CAIDAS, ini3, fin3))
    w("   SU CABECERA, LITERAL: %r" % cabecera3)
    heredadas = R94.caidas_propias_entrecomilladas(lineas, ini3, fin3)
    c_todas = caidas_en_titular_con_letra(lineas, ini3, fin3)
    w("   EL LECTOR HEREDADO, CORRIDO TAL CUAL SOBRE ESTA SECCION -> %d"
      % len(heredadas))
    w("   EL LECTOR DE TITULAR CON LETRA, que es el que esta acta obliga -> %d"
      % len(c_todas))
    w("   LAS DOS CIFRAS SE PUBLICAN Y EL HEREDADO NO SE RETIRA: la proxima acta")
    w("   que vuelva a la negrita de lead con clave de solo digitos lo necesita.")
    if not c_todas:
        w("   PARADA: la seccion %d no trae ninguna clave `C.n` y el acta declara"
          % SECCION_DE_LAS_CAIDAS)
        w("   dos. No se supone.")
        print(NL.join(salida))
        return 1
    caidas = []
    for clave, ln, literal in c_todas:
        parte = parte_de_la_caida(literal)
        esp = R92.especie_de_la_caida(literal, marcas=MARCAS_DE_ESPECIE_196)
        caidas.append((clave, ln, parte, esp, literal))
        w("      %-6s linea %-6d parte %-9s especie %s"
          % (clave, ln, parte, ", ".join(esp) or "NINGUNA"))
        w("            %s" % literal[:130])
    sin_parte = [x for x in caidas if x[2] == "SIN DECIR"]
    if sin_parte:
        w("   PARADA: hay %d caida(s) SIN PARTE DECLARADA en su titulo:"
          % len(sin_parte))
        for k, ln, _p, _e, _l in sin_parte:
            w("      %s en la linea %d" % (k, ln))
        w("   LA SECCION 3 GUARDA LAS DE LOS DOS LADOS Y SU TITULO NO ATRIBUYE:")
        w("   la parte sale de lo que cada titular dice de si mismo, o se para.")
        print(NL.join(salida))
        return 1
    sin_especie = [x for x in caidas if not x[3]]
    if sin_especie:
        w("   PARADA: hay %d caida(s) SIN ESPECIE DECLARADA:" % len(sin_especie))
        for k, ln, _p, _e, _l in sin_especie:
            w("      %s en la linea %d" % (k, ln))
        w("   LA GUARDA DE LA 193 SE CONSERVA ENTERA: cada caida DECLARA su")
        w("   especie o el registrador para. No se supone ninguna.")
        print(NL.join(salida))
        return 1
    c_aud = [x for x in caidas if x[2] == "AUDITOR"]
    c_eje = [x for x in caidas if x[2] == "EJECUTOR"]
    n_cifra_eje = len([x for x in c_eje if MARCA_ESPECIE_CIFRA in x[3]])
    n_metodo_aud = len([x for x in c_aud if MARCA_ESPECIE_METODO in x[3]])
    w("   REPARTO POR PARTE: del AUDITOR %d | del EJECUTOR %d"
      % (len(c_aud), len(c_eje)))
    w("   del EJECUTOR y DE CIFRA PUBLICADA: %d | del AUDITOR y DE METODO: %d"
      % (n_cifra_eje, n_metodo_aud))
    w("")

    w("G) LA FILA DE LAS PROPIAS DEL AUDITOR VIENE PARTIDA EN DOS, Y LAS DOS SE LEEN")
    corta = R92.fila_de_la_metrica(lineas, inicio, fin,
                                   R92.AGUJA_FILA_CAIDAS_AUDITOR)
    w("   la aguja corta de la 194 (%r) casa con %d fila(s)"
      % (R92.AGUJA_FILA_CAIDAS_AUDITOR, len(corta)))
    partidas = R95.filas_de_las_propias(lineas, inicio, fin)
    for aguja, f in sorted(partidas.items()):
        for ln, txt in f:
            w("      %-46s (linea %d) %s" % (aguja[:46], ln, txt[:110]))
        if len(f) != 1:
            w("   PARADA: la fila %r aparece %d veces." % (aguja, len(f)))
            print(NL.join(salida))
            return 1
    num_aud_acum = R92.numeral_de_la_fila(partidas[AGUJA_FILA_AUD_ACUMULAN][0][1])
    num_aud_total = R92.numeral_de_la_fila(partidas[AGUJA_FILA_AUD_TOTAL][0][1])
    w("   numerales leidos y no tecleados: QUE ACUMULAN %s | TOTAL del cuerpo %s"
      % (num_aud_acum, num_aud_total))
    if None in (num_aud_acum, num_aud_total):
        w("   PARADA: alguna de las dos mitades no trae cifra legible.")
        print(NL.join(salida))
        return 1
    w("   EL COTEJO CONTRA EL CUERPO SE HACE CONTRA LA DEL TOTAL, y AHORA EL")
    w("   CUERPO SI SEPARA LAS PARTES, que es lo que el lector nuevo permite:")
    w("   cuerpo del AUDITOR %d contra fila del TOTAL %d -> %s"
      % (len(c_aud), num_aud_total,
         "CALZA" if len(c_aud) == num_aud_total else "NO CALZA"))
    if len(c_aud) != num_aud_total:
        w("   PARADA: el cuerpo y la fila del TOTAL no calzan.")
        print(NL.join(salida))
        return 1
    w("")

    w("H) LAS TRES FILAS DE CAIDAS DEL EJECUTOR, Y EL COTEJO CONTRA EL CUERPO")
    fila_rep = R92.fila_de_la_metrica(lineas, inicio, fin,
                                      AGUJA_FILA_CAIDAS_REPORTE)
    fila_met = R92.fila_de_la_metrica(lineas, inicio, fin,
                                      R92.AGUJA_FILA_CAIDAS_METODO)
    fila_cif = R92.fila_de_la_metrica(lineas, inicio, fin,
                                      AGUJA_FILA_CAIDAS_CIFRA)
    for etiqueta, f in (("de reporte", fila_rep), ("de metodo", fila_met),
                        ("de cifra publicada", fila_cif)):
        for ln, txt in f:
            w("   %-20s (linea %d) %s" % (etiqueta, ln, txt))
    if not (fila_rep and fila_met and fila_cif):
        w("   PARADA: falta alguna de las tres filas de caidas del ejecutor.")
        print(NL.join(salida))
        return 1
    num_rep = R95.numeral_de_la_fila_195(fila_rep[0][1])
    num_met = R95.numeral_de_la_fila_195(fila_met[0][1])
    num_cif = R95.numeral_de_la_fila_195(fila_cif[0][1])
    w("   numerales: reporte %s | metodo %s | cifra publicada %s"
      % (num_rep, num_met, num_cif))
    if None in (num_rep, num_met, num_cif):
        w("   PARADA: alguna de las tres filas no trae cifra legible.")
        print(NL.join(salida))
        return 1
    w("   EL COTEJO DE LA FILA DE CIFRA CONTRA EL CUERPO, QUE LA 195 NO PODIA")
    w("   HACER PORQUE SU CUERPO NO SEPARABA PARTES: cuerpo %d contra fila %d -> %s"
      % (n_cifra_eje, num_cif,
         "CALZA" if n_cifra_eje == num_cif else "NO CALZA"))
    if n_cifra_eje != num_cif:
        w("   PARADA: la fila de cifra publicada y el cuerpo no calzan.")
        print(NL.join(salida))
        return 1
    _lit_met, exp_met = R92.expandir_rangos_de_clave(fila_met[0][1])
    w("   la fila de METODO nombra %s, con el rango expandido"
      % (", ".join("C.%d" % k for k in exp_met) or "(ninguna clave)"))
    if exp_met:
        w("   LA PARADA POR DESCUADRE SIGUE ENTERA EN ESA RAMA:")
        if len(exp_met) != num_met:
            w("   PARADA: claves del rango %d contra fila %d."
              % (len(exp_met), num_met))
            print(NL.join(salida))
            return 1
        w("      %d claves del rango contra fila %d -> CALZA"
          % (len(exp_met), num_met))
    else:
        w("   LA FILA NO NOMBRA NINGUNA CLAVE, Y ESO ES UNA MEDICION Y NO UN")
        w("   HUECO: las cuatro caidas de metodo del ejecutor viven en SU reporte")
        w("   y no en el cuerpo de esta acta, que solo publica su cifra. LA")
        w("   EXIGENCIA SE HACE CONDICIONAL A QUE LA FILA NOMBRE CLAVES, y en esa")
        w("   rama sigue entera. LO QUE SE ESTRECHA ES EL CASO, NO LA GUARDA.")
    w("   LAS TRES DEL EJECUTOR SUMAN %d." % (num_rep + num_met + num_cif))
    m_racha_rep = re.search(r"racha de reporte:\s*(\d+)", fila_rep[0][1])
    m_racha_cif = re.search(r"racha de cifra publicada:\s*(\d+)", fila_cif[0][1])
    racha_rep = m_racha_rep.group(1) if m_racha_rep else None
    racha_cif = m_racha_cif.group(1) if m_racha_cif else None
    w("   LAS DOS RACHAS, LEIDAS DE LA CELDA DERECHA DE SU FILA Y NO SUPUESTAS:")
    w("      racha de reporte: %s | racha de cifra publicada: %s"
      % (racha_rep, racha_cif))
    if racha_rep is None or racha_cif is None:
        w("   PARADA: el encargo manda registrar la racha de cifra publicada EN 1")
        w("   y la de reporte, y alguna de las dos celdas no la publica. No se")
        w("   teclea una.")
        print(NL.join(salida))
        return 1
    w("")

    w("I) LA METRICA DE CREDITO DE LA SECCION %d, ENTERA" % SECCION_DE_LA_METRICA)
    r7 = R92.rango_de_seccion(lineas, inicio, fin, SECCION_DE_LA_METRICA)
    if r7 is None:
        w("   PARADA: el acta no tiene seccion %d." % SECCION_DE_LA_METRICA)
        print(NL.join(salida))
        return 1
    filas7 = R92.filas_de_la_metrica(lineas, r7[0], r7[1])
    w("   la seccion %d va de la linea %d a la %d"
      % (SECCION_DE_LA_METRICA, r7[0], r7[1]))
    w("   CIFRA filas de datos: %d" % len(filas7))
    for ln, txt in filas7:
        w("      LINEA %-6d %s" % (ln, txt))
    if not filas7:
        w("   PARADA: la tabla de credito no trae ninguna fila de datos.")
        print(NL.join(salida))
        return 1
    fila_p = R92.fila_de_la_metrica(lineas, inicio, fin, R92.AGUJA_FILA_PUESTOS)
    w("   LA FILA DE PUESTOS, QUE EL ENCARGO MANDA REGISTRAR CON SU NOTA: %d"
      % len(fila_p))
    for ln, txt in fila_p:
        w("      LINEA %-6d %s" % (ln, txt))
    if len(fila_p) != 1:
        w("   PARADA: la fila de puestos aparece %d veces." % len(fila_p))
        print(NL.join(salida))
        return 1
    notas = R94.nota_de_la_fila_de_puestos(
        fila_p[0][1], (R92.NOTA_DE_PUESTOS, R94.NOTA_DE_PUESTOS_194,
                       R95.NOTA_DE_PUESTOS_195, NOTA_DE_PUESTOS_196))
    w("   LAS CUATRO NOTAS, LAS TRES HEREDADAS Y LA DE ESTA ACTA:")
    for marca, tal_cual, en_mayus, literal in notas:
        w("      %-16r tal cual: %-3s | en mayusculas: %-3s | literal: %r"
          % (marca, "SI" if tal_cual else "NO", "SI" if en_mayus else "NO", literal))
    if not notas[3][2]:
        w("   PARADA: la fila de puestos no trae la nota de los quemados.")
        print(NL.join(salida))
        return 1
    aisl, cot, quem, limpio_en_fila = R95.cifras_de_la_fila_de_puestos(fila_p[0][1])
    w("   aislados, cotejados, quemados y el cotejo limpio DE LA FILA:")
    w("      %r, %r, %r y %r" % (aisl, cot, quem, limpio_en_fila))
    if not (aisl and cot and quem):
        w("   PARADA: alguna de las tres cifras obligatorias no se lee.")
        print(NL.join(salida))
        return 1
    cero_quemados = R95.quemados_son_cero(quem)
    w("   LOS QUEMADOS SON CERO: %s" % ("SI" if cero_quemados else "NO"))
    limpios = cotejo_limpio_del_cuerpo(lineas, inicio, fin)
    w("   EL COTEJO LIMPIO, BUSCADO EN EL ACTA ENTERA Y NO SOLO EN SU FILA:")
    for ln, cifra in limpios:
        w("      linea %d -> %d" % (ln, cifra))
    limpio = limpios[0][1] if limpios else None
    if not cero_quemados:
        esperado = int(cot) - int(quem)
        w("   HAY QUEMADOS, ASI QUE LA EXIGENCIA CORRE, Y AHORA SE ENDURECE: no")
        w("   basta con que el literal este, tiene que CALZAR con cotejados menos")
        w("   quemados: %s - %s = %d contra el %s que el acta publica -> %s"
          % (cot, quem, esperado, limpio,
             "CALZA" if limpio == esperado else "NO CALZA"))
        if limpio is None:
            w("   PARADA: hay quemados y el acta no publica el cotejo limpio en")
            w("   ninguna parte. La exigencia SIGUE ENTERA y no se afloja.")
            print(NL.join(salida))
            return 1
        if limpio != esperado:
            w("   PARADA: el cotejo limpio publicado no calza con la resta.")
            print(NL.join(salida))
            return 1
    w("")

    w("J) EL NUMERO DE LA ENTRADA, QUE NO SE TECLEA")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    w("   serie recomputada de sus dos sedes: %d entradas" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SERIE.colisiones(halladas)), len(SERIE.huecos(halladas))))
    w("   SIGUIENTE LIBRE: R.%d" % numero)
    w("   EL ENCARGO NO ADELANTA NINGUN NUMERO: manda el instrumento.")
    w("")

    w("K) LA DEUDA DE LA SERIE, REMEDIDA AQUI Y NO HEREDADA")
    salto = R92.actas_sin_entrada(halladas, 173, VUELTA_DEL_ACTA - 1)
    faltan, bajo, alto = salto
    w("   tramo mirado: actas 173 a %d" % (VUELTA_DEL_ACTA - 1))
    w("   CIFRA actas SIN entrada propia en la serie: %d" % len(faltan))
    w("   LAS QUE FALTAN: %s" % (", ".join(str(x) for x in faltan) or "(ninguna)"))
    w("   el encargo dice OCHO (173 a 180) -> %s"
      % ("CALZA" if len(faltan) == 8 else "NO CALZA, y la discrepancia se declara"))
    w("")

    medido = {
        "inicio": inicio, "fin": fin, "secciones": secciones,
        "n_adj": len(claves), "n_entrecomillado": len(entrecomilladas),
        "n_suelto": len(sueltas), "n_negrita_sola": len(negrita_sola),
        "adjudicaciones": adjudicaciones,
        "n_discutibles": len(discutibles), "n_preg": len(preguntas),
        "n_otras": len(otras), "n_a_favor_discutibles": len(a_favor),
        "n_en_contra_discutibles": len(en_contra),
        "vieja_pararia": not en_contra,
        "n_sin_decir_titulo": n_sin_decir_titulo, "n_del_parrafo": n_del_parrafo,
        "n_familia_distinta": n_familia_distinta,
        "familias_heredadas": [(a[0], a[7], a[1]) for a in adjudicaciones],
        "arnes_disco": len(datos_arnes), "arnes_lf": len(lf_arnes),
        "arnes_veredicto": ver_arnes[0] if ver_arnes else "",
        "preguntas": [(c, R92.PAT_P_DEL_TITULO.search(t).group(0).strip("`"))
                      for c, _f, _e, _l, t, _fo, _p, _fh in preguntas],
        "hallazgos": hallazgos, "n_hall": len(hallazgos),
        "her_sueltos": len(her_sueltos), "her_comillas": len(her_comillas),
        "n_titulares": len(titulares),
        "fila_fuera": fila_fuera, "numeral_fila": numeral,
        "n_disc_fuera": n_disc_fuera,
        "cabecera_seccion3": cabecera3,
        "seccion_caidas": SECCION_DE_LAS_CAIDAS,
        "n_heredadas": len(heredadas), "caidas": caidas,
        "c_aud": c_aud, "c_eje": c_eje,
        "n_aud": len(c_aud), "n_eje": len(c_eje),
        "n_cifra_eje": n_cifra_eje, "n_metodo_aud": n_metodo_aud,
        "n_corta": len(corta),
        "num_aud_acum": num_aud_acum, "num_aud_total": num_aud_total,
        "num_rep": num_rep, "num_met": num_met, "num_cif": num_cif,
        "racha_rep": racha_rep, "racha_cif": racha_cif, "exp_met": exp_met,
        "fila_rep": fila_rep, "fila_met": fila_met, "fila_cif": fila_cif,
        "filas7": filas7, "n_filas7": len(filas7),
        "fila_puestos": fila_p, "notas": notas,
        "aislados": aisl, "cotejados": cot, "quemados": quem,
        "limpio_en_fila": limpio_en_fila, "limpios": limpios, "limpio": limpio,
        "cero_quemados": cero_quemados,
        "salto": salto, "numero": numero, "ya_registrada": len(ya),
        "sedes": sedes,
    }
    return salida, medido


def titulo_de_la_entrada(n_adj, n_hall, n_preg, n_cai_aud, n_cai_eje):
    """EL TITULO DE LA ENTRADA, CON SUS CINCO NUMERALES EN PALABRA. PURA.

    NO SE DELEGA EN LA MAQUINA DE OTRO REGISTRADOR, Y LA RAZON ESTA MEDIDA: todas
    cierran con `VUELTA_DEL_ACTA` de SU modulo, y por eso un titulo armado con
    ellas nombraria el acta equivocada. La marca de idempotencia de la casa es
    literalmente `del acta de la vuelta N`, asi que un numero mal puesto ahi rompe
    la comprobacion que impide escribir dos veces."""
    def trozo(n, sing, plur):
        if n == 1:
            return "la %s" % sing
        return "las %s %s" % (R92.PALABRA_CON_CERO[n], plur)

    def trozo_m(n, sing, plur):
        if n == 1:
            return "el %s" % sing
        return "los %s %s" % (R92.PALABRA_CON_CERO[n], plur)
    return ("Registro de %s, %s, %s, %s del auditor y %s del ejecutor "
            "del acta de la vuelta %d"
            % (trozo(n_adj, "adjudicacion numerada", "adjudicaciones numeradas"),
               trozo_m(n_hall, "hallazgo de la seccion 5",
                       "hallazgos de la seccion 5"),
               trozo(n_preg, "pregunta contestada", "preguntas contestadas"),
               trozo(n_cai_aud, "caida propia", "caidas propias"),
               trozo(n_cai_eje, "caida", "caidas"),
               VUELTA_DEL_ACTA))


def armar_entrada(numero, titulo, medido):
    """LA ENTRADA ENTERA. PURA: recibe todo lo ya medido en un diccionario y no
    lee ni escribe nada."""
    m = medido
    p = []
    p.append("## R.%d. %s" % (numero, titulo))
    p.append("")
    p.append("(Acta del auditor, vuelta %d, secciones %s; escrito en la vuelta %d,"
             % (VUELTA_DEL_ACTA, R92._lista(m["secciones"]), VUELTA_QUE_ESCRIBE))
    p.append("TAREA 1.)")
    p.append("")
    p.append("Por adicion, como `R.21` a `R.57`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.57`. Salida:")
    p.append("`docs/loop/SALIDA_V%s_T1A_REGISTRO_R%d.txt`."
             % (SUFIJO_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 2 SIN EMPEZAR, ASI QUE SUS GLOSAS NO")
    p.append("AFIRMAN EN PASADO LO QUE TODAVIA NO HA PASADO.** Es la forma que la `6.4` del")
    p.append("acta 172 adjudico como correcta. **Y EL ORDEN VA DECLARADO EN VEZ DE")
    p.append("DEJARSE:** esta vez la TAREA 1 va PRIMERA, al reves que en la 195, y el")
    p.append("motivo es una medicion y no una costumbre: **la seccion 2 del acta 196")
    p.append("publica el reparto del auditor sobre los 60 puestos del tramo, pero NO la")
    p.append("clase por puesto de ninguno de los 120 que la TAREA 2 lee a ciegas**, y las")
    p.append("cuatro que si nombra (`976`, `2428`, `2662`, `3173`) son puestos DESTAPADOS")
    p.append("del tramo, no del doble. **La 196 NO es vuelta de bateria** (`AUDITOR.md`")
    p.append("6.1: la 194 la corrio entera y la proxima cae en la 199).")
    p.append("")
    p.append("**LOS CINCO NUMERALES DEL TITULO NO ESTAN TECLEADOS:** se cuentan del acta")
    p.append("acotada (lineas %d a %d). **%d adjudicaciones numeradas (`4.1` a `4.%d`),"
             % (m["inicio"], m["fin"], m["n_adj"], m["n_adj"]))
    p.append("%d hallazgos numerados en la seccion 5, %d preguntas contestadas DENTRO de"
             % (m["n_hall"], m["n_preg"]))
    p.append("las adjudicaciones, %d caida propia del auditor y %d caidas del ejecutor.**"
             % (m["n_aud"], m["num_rep"] + m["num_met"] + m["num_cif"]))
    p.append("")
    p.append("### LAS ADJUDICACIONES VIENEN EN DOS FORMAS, Y LAS TRES CIFRAS SE PUBLICAN")
    p.append("")
    p.append("**EL ACTA 196 NUMERA DE DOS MANERAS Y ESO OBLIGO A ESCRIBIR UN LECTOR, CON")
    p.append("SU CIFRA DELANTE.** Las `4.1` a `4.7` son **lead de parrafo**")
    p.append("(``**`4.1` TITULO...**``), que es la forma del acta 184. Las `4.8` a `4.14`")
    p.append("son **clave sola en negrita y en mitad de un solo parrafo**")
    p.append("(``**`4.8`** `D.1`, ...``), y sobre esa forma el lector heredado no casa:")
    p.append("exige un espacio detras de la comilla de cierre y ahi hay un asterisco.")
    p.append("**MEDIDO: `claves_entrecomilladas` da %d, `claves_de_adjudicacion` da %d y"
             % (m["n_entrecomillado"], m["n_suelto"]))
    p.append("`claves_en_negrita_sola()`, el que esta acta obliga, da %d.** La union"
             % m["n_negrita_sola"])
    p.append("ordenada da **%d**, que es lo que el acta declara. **Ningun lector se"
             % m["n_adj"])
    p.append("retira**: la proxima acta que numere solo con lead lo necesita entero.")
    p.append("")
    p.append("### LAS %d ADJUDICACIONES, UNA POR UNA, CON SU ESTADO Y SU PROCEDENCIA"
             % m["n_adj"])
    p.append("")
    p.append("| clave | familia | estado | de donde sale el estado | forma | linea |")
    p.append("|---|---|---|---|---|---:|")
    for clave, fam, est, ln, _t, forma, proc, fam_her in m["adjudicaciones"]:
        p.append("| `%s` | %s | %s | %s | %s | %d |"
                 % (clave, fam, est, proc, forma, ln))
    p.append("")
    p.append("**LA VENTANA DEL ESTADO SE ENSANCHA DEL TITULO AL PARRAFO, Y LA CIFRA QUE LO")
    p.append("JUSTIFICA VA DELANTE.** El titulo de la `4.1` es *\"EL `976`, Y ES MI CAIDA")
    p.append("POR LA MISMA PUERTA...\"* y su veredicto, **A FAVOR DEL ARCHIVO**, esta al")
    p.append("final del parrafo. **Con el titulo y nada mas saldrian `SIN DECIR` %d"
             % m["n_sin_decir_titulo"])
    p.append("adjudicacion(es) y este registrador PARARIA**; **%d estado(s) salieron del"
             % m["n_del_parrafo"])
    p.append("PARRAFO**, y la tabla de arriba **publica de donde sale cada uno**. **Eso es")
    p.append("lo que impide que ensanchar la ventana sea aflojar la guarda:** una")
    p.append("adjudicacion muda en el titulo Y en el parrafo sigue saliendo `SIN DECIR` y")
    p.append("sigue haciendo PARAR.")
    p.append("")
    p.append("**Y LA FAMILIA SALE DE LA PRIMERA CLAVE QUE LA ADJUDICACION NOMBRA, NO DE")
    p.append("QUE NOMBRE ALGUNA `P.n`.** La `4.10` dice *\"`D.3`, declarar sujeto congelado")
    p.append("en cuatro..., y su riesgo declarado es la `P.2` que adjudico en el `4.6`\"*:")
    p.append("**adjudica un discutible y de paso CITA una pregunta ya adjudicada**. Con el")
    p.append("lector heredado sale PREGUNTA. **MEDIDO: la heredada y la nueva discrepan en")
    p.append("%d de las %d, y la heredada publicaria una PREGUNTA de mas y un DISCUTIBLE de"
             % (m["n_familia_distinta"], m["n_adj"]))
    p.append("menos.** **Las dos se corren y las dos cifras se publican; la heredada no se")
    p.append("retira.** Un texto que no nombre ninguna clave sigue saliendo `OTRA`, que es")
    p.append("lo que les toca a las cuatro discrepancias de la propia ciega del auditor.")
    p.append("")
    p.append("**Y EL VOCABULARIO DE ESTADOS CRECE EN UNA MARCA, LITERAL DEL ACTA:** %s,"
             % ", ".join("`%s`" % x for x in MARCAS_NUEVAS_196))
    p.append("que es como el acta contesta la `P.3`. Con el heredado, que dice")
    p.append("`POR EXTENSION CITABLE`, esa saldria `SIN DECIR`, porque el acta escribe")
    p.append("*\"CONTESTADA POR EXTENSION\"*. **Se anade y no se ensancha**: `EN CONTRA` y")
    p.append("`A FAVOR` siguen yendo primero y en ese orden.")
    p.append("")
    p.append("**LAS %d SON A FAVOR Y NINGUNA EN CONTRA, Y ES LA SEXTA ACTA SEGUIDA.**"
             % m["n_adj"])
    p.append("De las %d, **%d son discutibles del ejecutor y los %d van A FAVOR**; %d son"
             % (m["n_adj"], m["n_discutibles"], m["n_a_favor_discutibles"],
                m["n_preg"]))
    p.append("**preguntas contestadas por extension citable** (%s); y las %d restantes son"
             % (", ".join("`%s` en la `%s`" % (pn, c) for c, pn in m["preguntas"]),
                m["n_otras"]))
    p.append("**las cuatro discrepancias de la propia ciega del auditor, resueltas a favor")
    p.append("del archivo**. **CIFRA `EN CONTRA`: %d.**" % m["n_en_contra_discutibles"])
    p.append("")
    p.append("**Y ESE CERO NO SE VUELVE A PROBAR POR MUTACION: SE DICE CON SU FICHERO.**")
    p.append("`%s` mide **%d bytes** en disco y **%d** por LF, y su"
             % (ARNES_QUE_YA_CUBRE, m["arnes_disco"], m["arnes_lf"]))
    p.append("veredicto, leido del propio fichero, es %r. La guarda vieja de la 190"
             % m["arnes_veredicto"])
    p.append("(`if not en_contra: PARADA`) corrida sobre esta acta **%s**."
             % ("PARARIA" if m["vieja_pararia"] else "no pararia"))
    p.append("")
    p.append("### LOS %d HALLAZGOS DE LA SECCION 5, QUE NO SALEN DE NINGUN DISCUTIBLE"
             % m["n_hall"])
    p.append("")
    for clave, ln, tit in m["hallazgos"]:
        p.append("- **`%s`** (linea %d del acta): %s" % (clave, ln, tit[:220]))
    p.append("")
    p.append("**LOS TRES LECTORES SE CORREN Y LAS TRES CIFRAS SE PUBLICAN:**")
    p.append("`claves_entrecomilladas` da **%d**, `claves_de_adjudicacion` da **%d** y"
             % (m["her_comillas"], m["her_sueltos"]))
    p.append("`hallazgos_en_titular()` da **%d**. **Ninguno se retira.**"
             % m["n_titulares"])
    p.append("")
    p.append("**LA FILA DE LA TABLA DE CREDITO QUE LOS CUENTA, PEGADA Y NO PARAFRASEADA:**")
    p.append("")
    p.append("```")
    p.append(m["fila_fuera"][0][1])
    p.append("```")
    p.append("")
    p.append("**SU NUMERAL, LEIDO Y NO TECLEADO, ES %d, Y LAS CLAVES `5.n` SON %d.**"
             % (m["numeral_fila"], m["n_hall"]))
    p.append("**No se elige a ojo cual vale: la fila cuenta JUNTAS las discrepancias y los")
    p.append("hallazgos**, y su propia celda lo escribe nombrando el `2428`. Por resta")
    p.append("salen **%d discrepancia(s) fuera del marcado** mas los %d hallazgos."
             % (m["n_disc_fuera"], m["n_hall"]))
    p.append("")
    p.append("### LAS CAIDAS: LA SECCION %d GUARDA LAS DE LOS DOS LADOS"
             % m["seccion_caidas"])
    p.append("")
    p.append("**LA SEDE NO SE SUPONE Y SU TITULO NO ATRIBUYE.** En el acta 195 la sede era")
    p.append("la seccion 3 y se titulaba MIS CAIDAS PROPIAS; en la 194 era la 8 y en la")
    p.append("192 la 6. Aqui es la seccion %d y su cabecera, literal, es %r."
             % (m["seccion_caidas"], m["cabecera_seccion3"]))
    p.append("**Guarda las de LOS DOS lados**, asi que la atribucion no puede salir de la")
    p.append("seccion: **sale de lo que cada titular dice de si mismo**, y una caida sin")
    p.append("parte declarada hace PARAR.")
    p.append("")
    p.append("**Y ESO OBLIGO A ESCRIBIR EL SEGUNDO LECTOR, CON SU CIFRA DELANTE.** El acta")
    p.append("196 escribe sus caidas como **titulares `###` con LETRA en la clave**")
    p.append("(`C.E1` del ejecutor, `C.A1` del auditor), y el patron heredado es de")
    p.append("negrita de lead y de solo digitos. **MEDIDO: el lector heredado da %d sobre"
             % m["n_heredadas"])
    p.append("esta seccion y el de titular con letra da %d.** Con el heredado y nada mas,"
             % len(m["caidas"]))
    p.append("este registrador PARARIA sobre un acta que declara las dos con toda")
    p.append("claridad. **El heredado no se retira.**")
    p.append("")
    p.append("| clave | de quien | especie, leida de su titulo | linea del acta |")
    p.append("|---|---|---|---:|")
    for clave, ln, parte, esp, _lit in m["caidas"]:
        p.append("| `%s` | %s | %s | %d |" % (clave, parte, ", ".join(esp), ln))
    p.append("")
    p.append("**LA `%s` ES DEL EJECUTOR Y ES DE CIFRA PUBLICADA, NO DE REPORTE.** El acta"
             % m["c_eje"][0][0])
    p.append("la razona por `AUDITOR.md` 4, **LA RUTA QUE PROMETE PRUEBA ES CIFRA**: la")
    p.append("linea 19 del reporte de la 195 publica que el bloque `E` corrio")
    p.append("`scripts/loop/vuelta193_racha_de_cierres.py`, y ese fichero **no existe en")
    p.append("disco ni en ninguna rama**. Lo que corrio de verdad es")
    p.append("`vuelta192_racha_de_cierres.py`, que es el nombre que el propio reporte usa")
    p.append("bien mas abajo. **Lo que NO es, y el acta lo dice para no inflarlo:** no")
    p.append("mueve ningun dato, la corrida SI se hizo y su cifra es correcta y esta")
    p.append("sellada. **Lo falso es el nombre del instrumento.** **RACHA DE CIFRA")
    p.append("PUBLICADA: %s**, leida de la celda derecha de su fila y no supuesta; dos"
             % m["racha_cif"])
    p.append("tandas seguidas serian PARADA y hoy no lo son.")
    p.append("")
    p.append("**LA `%s` ES DEL AUDITOR, DE METODO, Y SU RACHA VA EN 2.** Reconto el"
             % m["c_aud"][0][0])
    p.append("marcador con `json` a mano en vez de por `AP.marcador()`, que es la misma")
    p.append("especie que la `C.1` del acta 195. **La remedio dentro de la vuelta** y")
    p.append("`AP.marcador()` da lo mismo que su cuenta. **A la tercera, el acta 197 tiene")
    p.append("que ABRIR con su remedio como tarea bloqueante del propio auditor**, y el")
    p.append("auditor lo deja escrito contra si mismo.")
    p.append("")
    p.append("| lo que se cuenta | del cuerpo del acta | de su fila de la tabla |")
    p.append("|---|---:|---:|")
    p.append("| caidas propias del auditor, TOTAL | %d | %d |"
             % (m["n_aud"], m["num_aud_total"]))
    p.append("| caidas propias del auditor, QUE ACUMULAN | (el cuerpo no las separa) | %d |"
             % m["num_aud_acum"])
    p.append("| del ejecutor, de cifra publicada | %d | %d |"
             % (m["n_cifra_eje"], m["num_cif"]))
    p.append("| del ejecutor, de reporte | (el cuerpo no las declara: son cero) | %d |"
             % m["num_rep"])
    p.append("| del ejecutor, de metodo | (viven en el reporte, no en el acta) | %d |"
             % m["num_met"])
    p.append("")
    p.append("**LA FILA DE LAS PROPIAS DEL AUDITOR SIGUE PARTIDA EN DOS**, que es el")
    p.append("remedio del hallazgo `5.1` del acta 195 aplicado otra vez. La aguja corta de")
    p.append("la 194 (`%s`) casa sobre esta acta con **%d**"
             % (R92.AGUJA_FILA_CAIDAS_AUDITOR, m["n_corta"]))
    p.append("filas, y quien se quedara con la primera registraria **%d** donde el cuerpo"
             % m["num_aud_acum"])
    p.append("declara **%d**." % m["n_aud"])
    p.append("")
    p.append("**Y ESTA ACTA PERMITE UN COTEJO QUE LA 195 NO PODIA HACER:** como el cuerpo")
    p.append("**separa las partes**, la fila de cifra publicada del ejecutor se puede")
    p.append("cotejar contra el cuerpo, y calza: **%d y %d**."
             % (m["n_cifra_eje"], m["num_cif"]))
    p.append("")
    p.append("**LA FILA DE CAIDAS DE METODO DEL EJECUTOR NO NOMBRA SUS CLAVES, Y ESO ES")
    p.append("UNA MEDICION Y NO UN HUECO.** El acta publica **%d** y no escribe `C.1` a"
             % m["num_met"])
    p.append("`C.4`, porque **esas cuatro viven en el reporte del ejecutor y no en el")
    p.append("cuerpo del acta**. El cotejo heredado compara claves del rango contra el")
    p.append("numeral y daria **%d contra %d**, o sea PARADA sobre un acta correcta."
             % (len(m["exp_met"]), m["num_met"]))
    p.append("**La exigencia se hace condicional a que la fila nombre alguna clave, y en")
    p.append("esa rama sigue entera**: si nombra claves y no calzan, se para igual. **Lo")
    p.append("que se estrecha es el caso, no la guarda.** **RACHA DE REPORTE: %s.**"
             % m["racha_rep"])
    p.append("")
    p.append("### LA METRICA DE CREDITO, Y SU FILA DE PUESTOS MIDE DOS QUEMADOS")
    p.append("")
    p.append("**LAS %d FILAS DE DATOS DE LA SECCION 7, PEGADAS DEL ACTA:**" % m["n_filas7"])
    p.append("")
    p.append("```")
    for _ln, txt in m["filas7"]:
        p.append(txt)
    p.append("```")
    p.append("")
    p.append("Son **%s aislados y %s cotejados, con %s quemados**, el `654` y el `719`."
             % (m["aislados"], m["cotejados"], m["quemados"]))
    p.append("**Salen del credito porque el encargo publico su clase de archivo**, que es")
    p.append("el hallazgo `5.1` del propio acta: un puesto cuya clase ya te dijeron no")
    p.append("prueba que leas bien. **Las cuatro notas se buscan y sus cifras se")
    p.append("publican:** `%s` de la 191 aparece **%s**, `%s` de la 194 aparece **%s**,"
             % (R92.NOTA_DE_PUESTOS, "SI" if m["notas"][0][2] else "NO",
                R94.NOTA_DE_PUESTOS_194, "SI" if m["notas"][1][2] else "NO"))
    p.append("`%s` de la 195 aparece **%s** y `%s`, la de esta acta, aparece **%s**."
             % (R95.NOTA_DE_PUESTOS_195, "SI" if m["notas"][2][2] else "NO",
                NOTA_DE_PUESTOS_196, "SI" if m["notas"][3][2] else "NO"))
    p.append("")
    p.append("**EL COTEJO LIMPIO NO VIVE EN LA FILA DE PUESTOS, Y LA EXIGENCIA SE ENDURECE")
    p.append("EN VEZ DE AFLOJARSE.** La fila publica %r como cotejo limpio, o sea nada, y"
             % m["limpio_en_fila"])
    p.append("**el registrador de la 195 PARARIA aqui**, porque exige el segundo cotejo en")
    p.append("cuanto hay quemados. Pero el acta **si publica el cotejo limpio**, en la")
    p.append("cabecera de la tabla de su seccion 2: `cotejo_limpio_del_cuerpo()` lo")
    p.append("encuentra en la(s) linea(s) %s con valor **%s**. **Y ahora no basta con que"
             % (", ".join(str(ln) for ln, _c in m["limpios"]) or "(ninguna)",
                m["limpio"]))
    p.append("el literal este: tiene que CALZAR con `cotejados - quemados`**, que da")
    p.append("**%d - %d = %d**. **Eso la 195 no lo comprobaba.**"
             % (int(m["cotejados"]), int(m["quemados"]),
                int(m["cotejados"]) - int(m["quemados"])))
    p.append("")
    p.append("### LA DEUDA DE LA SERIE, REMEDIDA AQUI EN VEZ DE HEREDARSE")
    p.append("")
    p.append("Tramo mirado: actas **173 a %d**. **CIFRA actas sin entrada propia en la"
             % (VUELTA_DEL_ACTA - 1))
    p.append("serie: %d** (%s). **Se registra y NO se arregla en esta vuelta**, que es lo"
             % (len(m["salto"][0]),
                ", ".join(str(x) for x in m["salto"][0]) or "ninguna"))
    p.append("que el encargo de la 196 deja escrito en su lista de lo que sigue fuera.")
    p.append("")
    p.append("**Y ESTA ENTRADA LA ESCRIBE UN REGISTRADOR IDEMPOTENTE, Y LA IDEMPOTENCIA NO")
    p.append("SE AFIRMA: SE PRUEBA RE CORRIENDOLO.** La comprobacion busca las DOS marcas")
    p.append("literales del acta %d (computadas de la vuelta, no tecleadas) **en LAS DOS"
             % VUELTA_DEL_ACTA)
    p.append("SEDES** de la serie. Antes de escribir esta entrada aparecian en **%d**"
             % m["ya_registrada"])
    p.append("linea(s); despues aparecen y **un re corrido no escribe nada**, con la sede")
    p.append("medida en bytes antes y despues.")
    return NL.join(p) + NL


def entrada_publica_las_dos_partes(entrada, n_aud, n_eje):
    """LA GUARDA: LA ENTRADA TIENE QUE PUBLICAR LAS CAIDAS DE LOS DOS LADOS, CADA
    UNA CON SU PARTE. PURA. Devuelve (ok, informe).

    ES LA HERMANA DE `entrada_publica_las_dos_mitades()` DE LA 195 Y NO SU COPIA.
    Alli lo que se podia perder era una MITAD de una fila; aqui lo que se puede
    perder es UN LADO ENTERO, porque la seccion 3 del acta 196 guarda las del
    ejecutor y las del auditor juntas y bajo un titulo que no atribuye. Una
    entrada que publicara solo las propias del auditor **borraria del registro la
    unica caida de cifra publicada de la vuelta**, que es justo la que acumula."""
    informe = []
    f_aud = "| caidas propias del auditor, TOTAL | %d | %d |" % (n_aud, n_aud)
    f_eje = "| del ejecutor, de cifra publicada | %d | %d |" % (n_eje, n_eje)
    t1 = f_aud in entrada
    t2 = f_eje in entrada
    informe.append("la fila del AUDITOR (%r) esta en la entrada: %s"
                   % (f_aud, "SI" if t1 else "NO"))
    informe.append("la fila del EJECUTOR (%r) esta en la entrada: %s"
                   % (f_eje, "SI" if t2 else "NO"))
    if n_aud == n_eje:
        informe.append("los dos lados miden lo mismo en esta acta, y la guarda "
                       "exige los dos igual: un lado que se calla no se arregla "
                       "porque las cifras coincidan")
    return (t1 and t2), informe


# ---------------------------------------------------------------- LA MUTACION
_CUENTA = {"casos": 0, "pasan": 0}


def _caso(w, nombre, obtenido, esperado):
    """UN CASO, Y LA CUENTA LA LLEVA EL ARNES Y NO EL QUE LO CITA."""
    ok = obtenido == esperado
    _CUENTA["casos"] += 1
    _CUENTA["pasan"] += 1 if ok else 0
    w("   %-62s %s" % (nombre, "VERDE" if ok else "ROJO"))
    if not ok:
        w("      esperado: %r" % (esperado,))
        w("      obtenido: %r" % (obtenido,))
    return ok


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION DE LO QUE ESTE REGISTRADOR ESTRENA.

    LO QUE PRUEBA, Y POR QUE PUEDE CAER: los seis trozos nuevos son PUROS y se
    corren sobre texto FABRICADO, con el valor esperado sacado de como se fabrico
    el texto y NO de una constante igual a la obtenida. `EJECUTOR.md` 1, EL CASO
    ROJO SE PRUEBA POR MUTACION."""
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("VUELTA 196, TAREA 1: CASO POSITIVO POR MUTACION DEL REGISTRADOR")
    w("=" * 78)
    w("")

    w("A) `claves_en_negrita_sola()` SOBRE UN PARRAFO FABRICADO CON LAS DOS FORMAS")
    fab = [
        "## 4. ADJUDICACIONES",
        "",
        "**`4.1` EL PRIMERO, A FAVOR DEL ARCHIVO.** Cuerpo del primero.",
        "",
        "**`4.2`** `D.1`, el segundo: **A FAVOR**, su motivo. **`4.3`** `D.2`, el",
        "tercero: **EN CONTRA**, su motivo.",
        "",
    ]
    lead = R92.claves_entrecomilladas(fab, 1, len(fab), "4.")
    sola = claves_en_negrita_sola(fab, 1, len(fab), "4.")
    ok &= _caso(w, "el lector heredado ve SOLO la forma de lead",
                [c for c, _n in lead], ["4.1"])
    ok &= _caso(w, "el lector nuevo ve SOLO la forma de negrita sola",
                [c for c, _n in sola], ["4.2", "4.3"])
    w("   LA MUTACION: si el lector nuevo casara tambien con el lead, la union")
    w("   contaria dos veces la `4.1`; y si el heredado bastara, la `4.2` y la")
    w("   `4.3` no existirian para este registrador.")
    w("")

    w("B) `trozo_de_la_clave_inline()` NO LE PRESTA A UNA CLAVE EL VEREDICTO DE OTRA")
    parrafo = parrafo_que_contiene(fab, 1, len(fab), 5)
    t2 = trozo_de_la_clave_inline(parrafo, "4.2", ["4.2", "4.3"])
    t3 = trozo_de_la_clave_inline(parrafo, "4.3", ["4.2", "4.3"])
    ok &= _caso(w, "el trozo de la `4.2` NO trae el `EN CONTRA` de la `4.3`",
                "EN CONTRA" in t2, False)
    ok &= _caso(w, "el trozo de la `4.3` SI trae su propio `EN CONTRA`",
                "EN CONTRA" in t3, True)
    ok &= _caso(w, "y por eso sus estados salen distintos",
                (estado_de_la_adjudicacion_196(t2),
                 estado_de_la_adjudicacion_196(t3)),
                ("A FAVOR", "EN CONTRA"))
    w("   LA MUTACION: con el parrafo ENTERO para las dos, la `4.2` saldria")
    w("   `EN CONTRA`, que es un veredicto prestado. Medido aqui:")
    ok &= _caso(w, "el parrafo entero le daria a la `4.2` el estado de la otra",
                estado_de_la_adjudicacion_196(parrafo), "EN CONTRA")
    w("")

    w("C) `estado_con_su_procedencia()` ENSANCHA LA VENTANA SIN AFLOJAR LA GUARDA")
    tit_mudo = "EL `976`, Y ES MI CAIDA POR LA MISMA PUERTA."
    par_con = tit_mudo + " Y aqui abajo: **A FAVOR DEL ARCHIVO.**"
    ok &= _caso(w, "con el titulo solo, el estado es SIN DECIR",
                estado_de_la_adjudicacion_196(tit_mudo), "SIN DECIR")
    ok &= _caso(w, "con el parrafo, sale A FAVOR y dice que vino del PARRAFO",
                estado_con_su_procedencia(tit_mudo, par_con), ("A FAVOR", "PARRAFO"))
    ok &= _caso(w, "y un texto mudo en LOS DOS sigue saliendo SIN DECIR",
                estado_con_su_procedencia(tit_mudo, tit_mudo),
                ("SIN DECIR", "NINGUNA"))
    ok &= _caso(w, "el titulo manda cuando habla: EN CONTRA gana al parrafo",
                estado_con_su_procedencia("ESTE VA EN CONTRA.", par_con),
                ("EN CONTRA", "TITULO"))
    ok &= _caso(w, "la marca nueva es literal y no parafrasis",
                estado_de_la_adjudicacion_196("CONTESTADA POR EXTENSION, Y VA "
                                              "CONTRA EL EJECUTOR."),
                "CONTESTADA POR EXTENSION Y EN CONTRA DEL EJECUTOR")
    ok &= _caso(w, "y el heredado NO la sabia leer, que es lo que la justifica",
                R92.estado_de_la_adjudicacion("CONTESTADA POR EXTENSION, Y VA "
                                              "CONTRA EL EJECUTOR."),
                "SIN DECIR")
    w("")

    w("D) `caidas_en_titular_con_letra()` Y `parte_de_la_caida()`")
    fab3 = [
        "## 3. LAS CAIDAS DE ESTA VUELTA",
        "",
        "### `C.E1` DEL EJECUTOR, DE CIFRA PUBLICADA: UNA RUTA QUE NO EXISTE",
        "",
        "Cuerpo.",
        "",
        "### `C.A1` MIA, DE METODO, Y ES LA MISMA ESPECIE QUE LA DEL ACTA 195",
        "",
        "Cuerpo.",
        "",
        "### `C.X1` SIN DECIR DE QUIEN ES",
        "",
    ]
    heredado = R94.caidas_propias_entrecomilladas(fab3, 1, len(fab3))
    nuevas = caidas_en_titular_con_letra(fab3, 1, len(fab3))
    ok &= _caso(w, "el lector heredado no ve NINGUNA de las tres",
                len(heredado), 0)
    ok &= _caso(w, "el lector nuevo ve las TRES, con su letra",
                [c for c, _l, _t in nuevas], ["C.E1", "C.A1", "C.X1"])
    ok &= _caso(w, "y la parte sale del titulo, con la tercera SIN DECIR",
                [parte_de_la_caida(t) for _c, _l, t in nuevas],
                ["EJECUTOR", "AUDITOR", "SIN DECIR"])
    w("   LA MUTACION: si `parte_de_la_caida` devolviera AUDITOR por defecto, la")
    w("   `C.E1` del ejecutor se registraria como propia del auditor y la caida")
    w("   que ACUMULA desapareceria del lado que le toca. La tercera prueba que")
    w("   el SIN DECIR existe y no se rellena solo.")
    ok &= _caso(w, "la especie tambien sale del titulo y no se supone",
                [R92.especie_de_la_caida(t, marcas=MARCAS_DE_ESPECIE_196)
                 for _c, _l, t in nuevas],
                [[MARCA_ESPECIE_CIFRA], [MARCA_ESPECIE_METODO], []])
    w("")

    w("E) `cotejo_limpio_del_cuerpo()` Y LA EXIGENCIA QUE SE ENDURECE")
    fab5 = [
        "| lo que se mide | sobre los 60 | sobre los 58 sin quemados |",
        "| coinciden | **56** | **54** |",
        "| puestos | 60 aislados, **60 cotejados**, **2 quemados** | **1.186** |",
    ]
    limpios = cotejo_limpio_del_cuerpo(fab5, 1, len(fab5))
    fila_p = fab5[2]
    a, c, q, l = R95.cifras_de_la_fila_de_puestos(fila_p)
    ok &= _caso(w, "la fila de puestos NO trae el cotejo limpio", l, None)
    ok &= _caso(w, "y el acta SI lo trae, en la cabecera de la otra tabla",
                [x[1] for x in limpios], [58])
    ok &= _caso(w, "y calza con cotejados menos quemados",
                int(c) - int(q), limpios[0][1])
    w("   LA MUTACION, Y ES LA QUE PRUEBA QUE LA EXIGENCIA SE ENDURECE: con un")
    w("   cotejo limpio FALSO, la guarda de la 195 lo dejaria pasar porque solo")
    w("   miraba que el literal estuviera; esta lo caza porque compara.")
    falso = ["| coinciden sobre los 47 sin quemados |"]
    lf = cotejo_limpio_del_cuerpo(falso, 1, 1)
    ok &= _caso(w, "un cotejo limpio de 47 con 60 y 2 NO calza",
                lf[0][1] == int(c) - int(q), False)
    ok &= _caso(w, "y sin quemados la exigencia ni siquiera corre",
                R95.quemados_son_cero("CERO"), True)
    w("")

    w("F) `familia_por_la_primera_clave()` NO DEJA QUE UNA CITA ROBE LA FAMILIA")
    con_cita = ("**`4.10`** `D.3`, declarar sujeto congelado en cuatro en vez de "
                "caso declarado: **A FAVOR**, la regla ofrece las dos salidas y "
                "su riesgo declarado es la `P.2` que adjudico en el `4.6`.")
    solo_p = "`4.5` `P.1`, LA RACHA DE CIERRES. A FAVOR DE MEDIR EL ACTO."
    sin_nada = "`4.1` EL `976`, Y ES MI CAIDA POR LA MISMA PUERTA."
    ok &= _caso(w, "la que adjudica un `D.n` y CITA un `P.n` es DISCUTIBLE",
                familia_por_la_primera_clave(con_cita), "DISCUTIBLE")
    w("   LA MUTACION: el lector heredado, corrido sobre EL MISMO texto, dice otra")
    w("   cosa, y por eso el lector nuevo no es un adorno.")
    ok &= _caso(w, "y la heredada la llamaria PREGUNTA",
                R92.familia_de_la_adjudicacion(con_cita), "PREGUNTA")
    ok &= _caso(w, "la que adjudica un `P.n` de verdad sigue siendo PREGUNTA",
                familia_por_la_primera_clave(solo_p), "PREGUNTA")
    ok &= _caso(w, "y la que no nombra ninguna clave sigue siendo OTRA",
                familia_por_la_primera_clave(sin_nada), "OTRA")
    w("")

    w("G) `entrada_publica_las_dos_partes()` SOBRE UNA ENTRADA FABRICADA")
    entera = ("| caidas propias del auditor, TOTAL | 1 | 1 |" + NL
              + "| del ejecutor, de cifra publicada | 1 | 1 |")
    coja = "| caidas propias del auditor, TOTAL | 1 | 1 |"
    ok1, _i1 = entrada_publica_las_dos_partes(entera, 1, 1)
    ok2, _i2 = entrada_publica_las_dos_partes(coja, 1, 1)
    ok &= _caso(w, "la entrada con LOS DOS lados pasa", ok1, True)
    ok &= _caso(w, "la entrada que se calla el lado del ejecutor CAE", ok2, False)
    w("")

    w("=" * 78)
    w("CIFRA casos: %d | pasan: %d | fallan: %d"
      % (_CUENTA["casos"], _CUENTA["pasan"], _CUENTA["casos"] - _CUENTA["pasan"]))
    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    w("=" * 78)
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_MUTACION_REGISTRADOR.txt"
                        % SUFIJO_QUE_ESCRIBE)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true",
                    help="mide y arma la entrada, pero NO escribe en la sede")
    ap.add_argument("--mutacion", action="store_true",
                    help="corre el caso positivo por mutacion y no toca nada")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    if a.mutacion:
        return prueba_de_mutacion()

    medido = _medir()
    if isinstance(medido, int):
        return medido
    salida, m = medido
    w = salida.append

    w("L) EL TITULO, CON SUS CINCO NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(m["n_adj"], m["n_hall"], m["n_preg"],
                                  m["n_aud"],
                                  m["num_rep"] + m["num_met"] + m["num_cif"])
    w("   %s" % titulo)
    w("")

    numero = m["numero"]
    entrada = armar_entrada(numero, titulo, m)
    w("M) LA ENTRADA ARMADA")
    w("   %d bytes | %d lineas por count(NL) | %d por len(split(NL))"
      % (len(entrada.encode("utf-8")), entrada.count(NL), len(entrada.split(NL))))
    w("   guiones largos o medios en la entrada: %d"
      % (entrada.count(chr(8212)) + entrada.count(chr(8211))))
    w("")

    w("N) LA GUARDA, CORRIDA SOBRE LA ENTRADA YA ARMADA")
    ok_guarda, informe = entrada_publica_las_dos_partes(
        entrada, m["n_aud"], m["n_cifra_eje"])
    for l in informe:
        w("   " + l)
    w("   VEREDICTO DE LA GUARDA: %s" % ("VERDE" if ok_guarda else "ROJO"))
    if not ok_guarda:
        w("   ROJO: la entrada no publica los dos lados. NO SE ESCRIBE NADA.")
        t = NL.join(salida) + NL
        ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_ROJO.txt" % SUFIJO_QUE_ESCRIBE)
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
        print(t)
        return 1
    w("")

    texto_sede = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    if a.simular:
        w("O) MODO --simular: NO SE ESCRIBE NADA EN LA SEDE.")
        w("")
        w("LA ENTRADA, ENTERA:")
        for l in entrada.split(NL):
            w("   | " + l)
    elif m["ya_registrada"]:
        w("O) NO SE ESCRIBE NADA, Y ESTA ES LA IDEMPOTENCIA HACIENDO SU TRABAJO.")
        w("   el acta %d YA TIENE ENTRADA en la serie: %d linea(s) la nombran."
          % (VUELTA_DEL_ACTA, m["ya_registrada"]))
        w("   NO se escribe una entrada nueva y NO se consume el numero R.%d." % numero)
        w("   docs/PENDIENTES.md sigue en %d bytes." % os.path.getsize(SEDE))
    else:
        nuevo = texto_sede.rstrip(NL) + NL + NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("O) ESCRITA EN docs/PENDIENTES.md")
        w("   la sede pasa de %d a %d bytes"
          % (len(texto_sede.encode("utf-8")), len(nuevo.encode("utf-8"))))
        rele = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
        w("   RELEIDA DEL DISCO: la entrada esta byte a byte: %s"
          % ("SI" if entrada.rstrip(NL) in rele else "NO"))
        de_nuevo = SERIE.entradas()
        w("   SERIE RECOMPUTADA DESPUES DE ESCRIBIR: %d entradas, siguiente libre R.%d"
          % (len(de_nuevo), SERIE.siguiente_libre(de_nuevo)))
        w("   CIFRA colisiones: %d | CIFRA huecos: %d"
          % (len(SERIE.colisiones(de_nuevo)), len(SERIE.huecos(de_nuevo))))
        sedes2 = {}
        for ruta in SERIE.SEDES:
            rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
            sedes2[rel] = io.open(ruta, encoding="utf-8", errors="replace").read()
        w("   Y LA IDEMPOTENCIA, REMEDIDA DESPUES DE ESCRIBIR: el acta %d aparece en"
          % VUELTA_DEL_ACTA)
        w("   %d linea(s), asi que un RE CORRIDO de este instrumento no escribiria"
          % len(R92.entradas_que_registran(VUELTA_DEL_ACTA, sedes2)))
        w("   nada.")
    w("")
    t = NL.join(salida) + NL
    if a.simular:
        nombre = "SALIDA_V%s_T1A_SIMULACION.txt" % SUFIJO_QUE_ESCRIBE
    elif m["ya_registrada"]:
        nombre = "SALIDA_V%s_T1A_RECORRIDO_SIN_ESCRIBIR.txt" % SUFIJO_QUE_ESCRIBE
    else:
        nombre = "SALIDA_V%s_T1A_REGISTRO_R%d.txt" % (SUFIJO_QUE_ESCRIBE, numero)
    ruta = os.path.join(LOOP, nombre)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
