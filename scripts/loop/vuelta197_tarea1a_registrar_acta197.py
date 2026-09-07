# -*- coding: utf-8 -*-
r"""vuelta197_tarea1a_registrar_acta197.py . EL ACTA 197 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA, Y ESTE REGISTRADOR SIGUE SIENDO IDEMPOTENTE.

LA MAQUINA SE IMPORTA Y NO SE COPIA. Todo lo generico (acotar el acta, leer
secciones, familia y estado de una adjudicacion, filas de la tabla de credito,
numerales, expansion de rangos, la serie) sale de
`vuelta192_tarea1a_registrar_acta192.py`, y las piezas de la 194, la 195 y la 196
se importan tal cual. AQUI SOLO VIVE LO QUE EL ACTA 197 TIENE DISTINTO, y va
dicho uno por uno. CADA LECTOR NUEVO TRAE DELANTE LA CIFRA QUE LO JUSTIFICA,
medida sobre el acta acotada HOY y no supuesta:

  1. UN TITULAR DE CAIDA PUEDE LLEVAR DOS CLAVES. El acta 197 escribe
     ``### `C.E2` Y `C.E3` DEL EJECUTOR...`` y ``### `C.A3` Y `C.A4` MIAS...``.
     El lector de la 196 casa el titular POR SU PRINCIPIO y se queda con la
     PRIMERA clave. MEDIDO: sobre la seccion 3 de esta acta devuelve SEIS claves
     (`C.E1`, `C.E2`, `C.A1`, `C.A2`, `C.A3`, `C.A5`) y **pierde la `C.E3` y la
     `C.A4`**; con eso el cuerpo daria CUATRO caidas del auditor contra la fila
     del TOTAL, que dice **5**, y el registrador PARARIA sobre un acta correcta.
     `caidas_en_titular_con_varias_claves()` las lee todas.

  2. LA PARTE PUEDE VENIR EN PLURAL. El titular de la `C.A3` dice **MIAS**, y el
     lector heredado busca `\bMIA\b`, que NO casa con `MIAS`. MEDIDO: esas dos
     caidas saldrian `SIN DECIR` y el registrador PARARIA. `parte_de_la_caida_197()`
     corre PRIMERO el heredado entero y solo si calla prueba el plural, que es
     literal del acta.

  3. LA FILA DE PUESTOS TRAE SU CELDA ENTERA EN NEGRITA. El acta 197 escribe
     `**120 aislados, 120 cotejados, 8 quemados**`, con UN SOLO par de asteriscos
     envolviendo las tres cifras. El lector de la 195 exige `**N cotejados**` y
     `**N quemados**` con sus propios asteriscos. MEDIDO: devuelve
     `('120', None, None, None)` y el registrador PARARIA por "alguna de las tres
     cifras obligatorias no se lee". `cifras_de_la_fila_de_puestos_197()` lee la
     forma envolvente **despues** de correr entera la heredada.

  4. EL COTEJO LIMPIO NO SE ESCRIBE `sobre los N sin quemados`. El acta 197 lo
     escribe en la cabecera de su tabla de la seccion 2: *"**los 112 LIMPIOS, y es
     la cifra que manda**"*. MEDIDO: el patron de la 196 encuentra CERO, y como
     los quemados NO son cero la exigencia corre y el registrador PARARIA.
     `cotejo_limpio_197()` lo lee, y la exigencia SIGUE ENDURECIDA: tiene que
     CALZAR con `cotejados - quemados`.

  5. CINCO DE LAS SIETE ADJUDICACIONES NO DICEN SU ESTADO CON EL VOCABULARIO
     VIEJO. MEDIDO: con el heredado y el de la 196, `4.2`, `4.4`, `4.5`, `4.6` y
     `4.7` salen `SIN DECIR` y el registrador PARARIA sobre un acta que adjudica
     las siete con toda claridad. `estado_de_la_adjudicacion_197()` anade SEIS
     marcas LITERALES DEL ACTA. **SE ANADEN, NO SE ENSANCHA NINGUNA**: `EN CONTRA`
     y `A FAVOR` siguen primero y en ese orden, y una adjudicacion muda en el
     titulo Y en el parrafo sigue saliendo `SIN DECIR` y sigue haciendo PARAR.
     Y UNA DE LAS SEIS EXISTE POR UNA RAZON MEDIDA Y NO POR COMODIDAD: sin
     `NO MUEVE LA RACHA`, el estado de la `4.3` salia del PARRAFO y por la frase
     *"No adjudico a favor del bucle"*, o sea por un `A FAVOR` que en su sitio
     dice lo contrario. **Con la marca del titulo, la `4.3` ya no depende de esa
     frase**, y las dos cifras se publican.

  6. LA FILA DE CAIDAS DEL EJECUTOR NOMBRA CLAVES CON LETRA. Escribe
     `` (`C.E2`, `C.E3`) ``, y `PAT_CLAVE_C` es de solo digitos. MEDIDO: el
     heredado devuelve CERO claves y el cotejo de la 196 se va a la rama
     "la fila no nombra ninguna clave", que es la rama SIN dientes.
     `claves_con_letra_de_la_fila()` las lee, con lo que **la exigencia dura
     vuelve a correr** sobre esta acta: dos claves contra la fila que dice 2.
     **ESO ENDURECE, NO AFLOJA.**

  7. LA FILA DE FUERA DEL MARCADO NOMBRA SUS PUESTOS. La resta heredada
     (`numeral - hallazgos`) da **1** sobre esta acta, y la fila nombra **5**
     puestos con nombre y apellido. `puestos_que_nombra_la_fila()` los cuenta, y
     **LAS DOS CIFRAS SE PUBLICAN**: la resta no se retira, pero deja de ser la
     unica.

EL SUJETO DE CADA CIFRA SE CUENTA DEL CUERPO ACOTADO DEL ACTA, y el cuerpo se
acota AQUI con `R92.cuerpo_del_acta`, no por la linea que el encargo cita: el
fichero puede haber crecido y una linea heredada es una cifra sin medir.

USO:
  python scripts/loop/vuelta197_tarea1a_registrar_acta197.py
  python scripts/loop/vuelta197_tarea1a_registrar_acta197.py --simular
  python scripts/loop/vuelta197_tarea1a_registrar_acta197.py --mutacion
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
import vuelta196_tarea1a_registrar_acta196 as R96   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 197
VUELTA_QUE_ESCRIBE = 197
SUFIJO_QUE_ESCRIBE = "197"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "4."
PREFIJO_HALLAZGO = "5."
SECCION_DE_LOS_HALLAZGOS = 5
SECCION_DE_LAS_CAIDAS = 3
SECCION_DE_LA_METRICA = 7

AGUJA_FILA_AUD_ACUMULAN = R95.AGUJA_FILA_AUD_ACUMULAN
AGUJA_FILA_AUD_TOTAL = R95.AGUJA_FILA_AUD_TOTAL
AGUJA_FILA_CAIDAS_REPORTE = R95.AGUJA_FILA_CAIDAS_REPORTE
AGUJA_FILA_CAIDAS_CIFRA = R95.AGUJA_FILA_CAIDAS_CIFRA

MARCA_ESPECIE_METODO = R92.MARCA_ESPECIE_METODO
MARCA_ESPECIE_CIFRA = R92.MARCA_ESPECIE_CIFRA
MARCA_ESPECIE_REMEDIO = R94.MARCA_ESPECIE_REMEDIO
# LA ESPECIE QUE ESTA ACTA ESTRENA EN UN TITULAR, LITERAL DE LA `C.E1`:
# "ES DE REPORTE, NO DE CIFRA". Sin ella esa caida saldria SIN ESPECIE y el
# registrador PARARIA.
MARCA_ESPECIE_REPORTE = "DE REPORTE"
MARCAS_DE_ESPECIE_197 = (MARCA_ESPECIE_CIFRA, MARCA_ESPECIE_METODO,
                         MARCA_ESPECIE_REMEDIO, MARCA_ESPECIE_REPORTE)

# LA NOTA DE LA FILA DE PUESTOS, HEREDADA DE LA 196 Y QUE ESTA ACTA VUELVE A USAR.
NOTA_DE_PUESTOS_196 = R96.NOTA_DE_PUESTOS_196

# EL ARNES DE LA 191 QUE YA CUBRE EL CERO DE `EN CONTRA`.
ARNES_QUE_YA_CUBRE = R96.ARNES_QUE_YA_CUBRE

# LAS SEIS MARCAS DE ESTADO QUE EL ACTA 197 OBLIGA, TODAS LITERALES DE SUS
# PROPIOS TITULOS. Cada una lleva al lado la clave que la obliga.
MARCA_NO_ENTRAN_AL_CREDITO = "NO ENTRAN AL CREDITO"          # `4.2`
MARCA_NO_MUEVE_LA_RACHA = "NO MUEVE LA RACHA"                # `4.3`
MARCA_SALEN_DEL_CREDITO = "SALEN DEL CREDITO"                # `4.4`
MARCA_ADJUDICADA_POR_EXTENSION = "ADJUDICADA POR EXTENSION"  # `4.5`
MARCA_SE_MANTIENE = "SE MANTIENE Y NO SE AFLOJA"             # `4.6`
MARCA_NO_ES_CAIDA = "NO ES CAIDA"                            # `4.7`
MARCAS_NUEVAS_197 = (MARCA_NO_ENTRAN_AL_CREDITO, MARCA_NO_MUEVE_LA_RACHA,
                     MARCA_SALEN_DEL_CREDITO, MARCA_ADJUDICADA_POR_EXTENSION,
                     MARCA_SE_MANTIENE, MARCA_NO_ES_CAIDA)

# LA MARCA DE PARTE EN PLURAL, LITERAL DEL TITULAR DE LA `C.A3`.
MARCA_PARTE_AUDITOR_PLURAL = "MIAS"

# LOS PATRONES QUE ESTA ACTA OBLIGA A ESCRIBIR.
PAT_TITULAR_CAIDA = re.compile(r"^\s*#{2,4}\s")
PAT_CLAVE_CON_LETRA = re.compile(r"`C\.([A-Z])(\d+)`")
PAT_RANGO_CON_LETRA = re.compile(r"`C\.([A-Z])(\d+)`\s*a\s*`C\.([A-Z])(\d+)`")
PAT_COTEJO_LIMPIO_197 = re.compile(r"los\s+(\d+)\s+LIMPIOS")
PAT_PUESTO_EN_FILA = re.compile(r"`(\d{2,5})`")


def caidas_en_titular_con_varias_claves(lineas, ini, fin):
    """LAS CAIDAS DE UN TITULAR `###`, TODAS LAS CLAVES Y NO SOLO LA PRIMERA.
    PURA. Devuelve [(clave, linea, titulo_literal)] ordenada por linea y por el
    orden en que las claves aparecen en su titular.

    POR QUE EXISTE, MEDIDO Y NO SUPUESTO: el acta 197 mete DOS caidas en un solo
    titular dos veces (``### `C.E2` Y `C.E3` ...`` y ``### `C.A3` Y `C.A4` ...``).
    El lector de la 196 ancla el patron al PRINCIPIO de la linea y devuelve la
    primera clave de cada titular: SEIS donde el acta declara OCHO, y con eso el
    cuerpo daria CUATRO caidas del auditor contra la fila del TOTAL, que dice 5.

    NO SE ENSANCHA A CUALQUIER `C.n` DEL CUERPO: solo se leen las claves que
    estan EN LA LINEA DEL TITULAR. Una clave citada en el parrafo no es una
    caida nueva."""
    salida = []
    for i in range(ini, fin + 1):
        linea = lineas[i - 1]
        if not PAT_TITULAR_CAIDA.match(linea):
            continue
        vistas = []
        for m in re.finditer(r"`C\.([A-Z]?\d+)`", linea):
            clave = "C.%s" % m.group(1)
            if clave not in vistas:
                vistas.append(clave)
        for clave in vistas:
            salida.append((clave, i, linea.strip()))
    return salida


def parte_de_la_caida_197(titulo):
    """DE QUIEN ES UNA CAIDA, ADMITIENDO EL PLURAL. PURA.
    Devuelve `EJECUTOR`, `AUDITOR` o `SIN DECIR`.

    CORRE PRIMERO EL LECTOR DE LA 196 ENTERO Y SIN TOCAR, y solo si ese dice
    `SIN DECIR` prueba `MIAS`, que es literal del titular de la `C.A3` del acta
    197. MEDIDO: con el heredado solo, ese titular sale `SIN DECIR` porque su
    patron es `\\bMIA\\b` y `MIAS` no casa, y el registrador PARARIA.

    UN TITULO QUE NO DIGA NI UNA NI OTRA SIGUE SALIENDO `SIN DECIR`: la guarda
    no se afloja, se le anade una forma."""
    heredado = R96.parte_de_la_caida(titulo)
    if heredado != "SIN DECIR":
        return heredado
    if re.search(r"\b%s\b" % MARCA_PARTE_AUDITOR_PLURAL, titulo.upper()):
        return "AUDITOR"
    return "SIN DECIR"


def cifras_de_la_fila_de_puestos_197(texto_de_la_fila):
    """LAS CIFRAS DE LA FILA DE PUESTOS CUANDO LA CELDA ENTERA VA EN NEGRITA.
    PURA. Devuelve `(aislados, cotejados, quemados, limpio)`.

    CORRE PRIMERO LA HEREDADA ENTERA (`R95.cifras_de_la_fila_de_puestos`) y solo
    rellena las que esa deje en `None`. MEDIDO sobre esta acta: la heredada
    devuelve `('120', None, None, None)` porque el acta escribe
    `**120 aislados, 120 cotejados, 8 quemados**`, con UN SOLO par de asteriscos
    envolviendo las tres, y la heredada exige `**N cotejados**` con los suyos.

    `limpio` SE SIGUE DEVOLVIENDO COMO LA HEREDADA LO DEJE: aqui no se inventa,
    porque esta acta no lo escribe en su fila sino en su seccion 2, y eso lo lee
    `cotejo_limpio_197()`."""
    aisl, cot, quem, lim = R95.cifras_de_la_fila_de_puestos(texto_de_la_fila)
    if cot is None:
        m = re.search(r"(\d+)\s+cotejados", texto_de_la_fila)
        cot = m.group(1) if m else None
    if quem is None:
        m = re.search(r"(\w+)\s+quemados", texto_de_la_fila, re.IGNORECASE)
        quem = m.group(1) if m else None
    return aisl, cot, quem, lim


def cotejo_limpio_197(lineas, ini, fin):
    """EL COTEJO LIMPIO EN LA FORMA DEL ACTA 197. PURA. Devuelve [(linea, cifra)].

    El acta 197 lo escribe en la cabecera de la tabla de su seccion 2:
    *"**los 112 LIMPIOS, y es la cifra que manda**"*. MEDIDO: el patron de la 196
    (`sobre los N sin quemados`) encuentra CERO sobre esta acta, y como los
    quemados NO son cero la exigencia corre y el registrador PARARIA.

    LA EXIGENCIA DE LA 196 NO SE AFLOJA: quien llama sigue exigiendo que la cifra
    CALCE con `cotejados - quemados`. Lo unico que cambia es donde se lee."""
    salida = []
    for i in range(ini, fin + 1):
        for m in PAT_COTEJO_LIMPIO_197.finditer(lineas[i - 1]):
            salida.append((i, int(m.group(1))))
    return salida


def estado_de_la_adjudicacion_197(texto):
    """EL ESTADO DE UNA ADJUDICACION, CON LAS SEIS MARCAS DEL ACTA 197. PURA.

    CORRE PRIMERO EL LECTOR DE LA 196 ENTERO, que a su vez corre primero el
    heredado de la 192 con sus doce marcas. Solo si los dos callan se prueban las
    seis de esta acta, y en el orden en que estan escritas arriba.

    MEDIDO: con el vocabulario de la 196, CINCO de las siete adjudicaciones de
    esta acta (`4.2`, `4.4`, `4.5`, `4.6` y `4.7`) salen `SIN DECIR` y el
    registrador PARARIA sobre un acta que las adjudica todas con claridad.

    LAS SEIS SON LITERALES DE LOS TITULOS y no parafrasis. Una adjudicacion muda
    sigue saliendo `SIN DECIR`."""
    heredado = R96.estado_de_la_adjudicacion_196(texto)
    if heredado != "SIN DECIR":
        return heredado
    alto = texto.upper()
    if MARCA_NO_ENTRAN_AL_CREDITO in alto:
        return "PUBLICADAS Y FUERA DEL CREDITO"
    if MARCA_NO_MUEVE_LA_RACHA in alto:
        return "CONTESTADA: NO MUEVE LA RACHA, SIN DOCTRINA NUEVA"
    if MARCA_SALEN_DEL_CREDITO in alto:
        return "CONTESTADA: NO SE ENSANCHA LA LISTA BLANCA, SALEN DEL CREDITO"
    if MARCA_ADJUDICADA_POR_EXTENSION in alto:
        return "CONTESTADA POR EXTENSION Y CONTRA EL PROPIO AUDITOR"
    if MARCA_SE_MANTIENE in alto:
        return "SE MANTIENE, Y SE MIDE POR TRES VARAS"
    if MARCA_NO_ES_CAIDA in alto:
        return "NO ES CAIDA, Y SE ARREGLA IGUAL"
    return "SIN DECIR"


def estado_con_su_procedencia_197(titulo, parrafo):
    """EL ESTADO Y DE DONDE SALIO. PURA. Devuelve (estado, procedencia).

    Misma disciplina que la 196: el titulo entero primero, el parrafo solo si el
    titulo calla, y `SIN DECIR` en los dos sigue haciendo PARAR a quien llame."""
    e1 = estado_de_la_adjudicacion_197(titulo)
    if e1 != "SIN DECIR":
        return e1, "TITULO"
    e2 = estado_de_la_adjudicacion_197(parrafo)
    if e2 != "SIN DECIR":
        return e2, "PARRAFO"
    return "SIN DECIR", "NINGUNA"


def claves_con_letra_de_la_fila(texto):
    """LAS CLAVES `C.X n` DE UNA FILA, CON SUS RANGOS EXPANDIDOS. PURA.
    Devuelve (literales, expandidas), las dos listas de cadenas ordenadas.

    POR QUE EXISTE, Y ENDURECE EN VEZ DE AFLOJAR: la fila de caidas de metodo del
    acta 197 escribe `` **2** (`C.E2`, `C.E3`) ``, y `R92.expandir_rangos_de_clave`
    usa `PAT_CLAVE_C`, de SOLO DIGITOS. MEDIDO: devuelve CERO claves, con lo que
    el cotejo de la 196 se va a su rama condicional, la que NO compara nada. Con
    este lector la fila SI nombra claves y **la comparacion dura vuelve a correr**.

    UN RANGO AL REVES NO SE ADIVINA: se deja como las dos claves literales que es,
    y quien llama vera que no calza con el numeral y hara PARADA."""
    literales = []
    for letra, num in PAT_CLAVE_CON_LETRA.findall(texto):
        clave = "C.%s%s" % (letra, num)
        if clave not in literales:
            literales.append(clave)
    expandidas = list(literales)
    for la, a, lb, b in PAT_RANGO_CON_LETRA.findall(texto):
        if la != lb or int(a) > int(b):
            continue
        for k in range(int(a), int(b) + 1):
            clave = "C.%s%d" % (la, k)
            if clave not in expandidas:
                expandidas.append(clave)
    return sorted(literales), sorted(expandidas)


def puestos_que_nombra_la_fila(texto):
    """LOS PUESTOS QUE UNA FILA DE LA METRICA NOMBRA ENTRE COMILLAS INVERSAS.
    PURA. Devuelve la lista de cadenas, sin repetir y en el orden en que salen.

    POR QUE EXISTE, Y NO RETIRA A NADIE: la resta heredada
    (`numeral - hallazgos`) da **1** sobre esta acta, porque la fila cuenta juntas
    las discrepancias y los hallazgos en otras actas y en esta no. La fila de la
    197 nombra sus CINCO puestos con nombre y apellido. **LAS DOS CIFRAS SE
    PUBLICAN**: la resta sigue corriendo y su cifra sigue saliendo, y esta dice
    cuantos puestos nombra la fila de verdad."""
    vistos = []
    for m in PAT_PUESTO_EN_FILA.finditer(texto):
        if m.group(1) not in vistos:
            vistos.append(m.group(1))
    return vistos


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
    w("   EL ENCARGO CITA LA LINEA 69341 SOBRE 4595886 BYTES Y AQUI SE RECUENTA:")
    w("   las cifras de arriba salen de R92.cuerpo_del_acta corrido HOY.")
    secciones = R92.secciones_del_acta(lineas, inicio, fin)
    w("   SECCIONES `## n.` DEL ACTA, LEIDAS Y NO TECLEADAS: %s"
      % R92._lista(secciones))
    w("   Y LA SEDE DE LAS CAIDAS NO SE SUPONE: en el acta 197 es la seccion 3,")
    w("   titulada LAS CAIDAS, y guarda las de LOS DOS lados.")
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
    negrita_sola = R96.claves_en_negrita_sola(lineas, inicio, fin, PREFIJO_ADJ)
    w("   patron CON comillas inversas y LEAD de parrafo (el del acta 184) -> %d"
      % len(entrecomilladas))
    for clave, cuantas in entrecomilladas:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    w("   patron SIN comillas inversas (el del acta 189) -> %d" % len(sueltas))
    w("   patron de CLAVE SOLA EN NEGRITA (el que la 196 obligo) -> %d"
      % len(negrita_sola))
    w("   EL ACTA 197 VUELVE A LA FORMA UNICA DE LEAD DE PARRAFO, y por eso manda")
    w("   `claves_entrecomilladas`. LOS TRES LECTORES SE CORREN Y LAS TRES CIFRAS")
    w("   SE PUBLICAN: NINGUNO SE RETIRA.")
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
        w("   PARADA: ningun patron encuentra adjudicaciones y el acta 197 declara")
        w("   siete. No se escribe una entrada con cero.")
        print(NL.join(salida))
        return 1
    w("")

    w("D) EL TITULO DE CADA ADJUDICACION, SU FAMILIA Y SU ESTADO CON PROCEDENCIA")
    adjudicaciones = []
    n_sin_decir_196 = 0
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
            parrafo = R96.parrafo_que_empieza(lineas, inicio, fin, ln)
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
            entero = R96.parrafo_que_contiene(lineas, inicio, fin, ln)
            tit = R96.trozo_de_la_clave_inline(entero, clave, claves_inline)
            parrafo = tit
            forma = "NEGRITA SOLA"
            if not tit:
                w("   PARADA: %s no deja trozo legible en su parrafo." % clave)
                print(NL.join(salida))
                return 1
        est_196, proc_196 = R96.estado_con_su_procedencia(tit, parrafo)
        if est_196 == "SIN DECIR":
            n_sin_decir_196 += 1
        est, proc = estado_con_su_procedencia_197(tit, parrafo)
        if proc == "PARRAFO":
            n_del_parrafo += 1
        fam_her = R92.familia_de_la_adjudicacion(tit)
        fam = R96.familia_por_la_primera_clave(tit)
        if fam_her != fam:
            n_familia_distinta += 1
        adjudicaciones.append((clave, fam, est, ln, tit, forma, proc, fam_her,
                               est_196, proc_196))
        w("   %-5s linea %-6d [%-10s / %-52s] forma %s, estado del %s"
          % (clave, ln, fam, est[:52], forma, proc))
        w("         con el vocabulario de la 196 saldria: %s (del %s)"
          % (est_196[:52], proc_196))
        w("         %s" % tit[:150])
    w("   EL VOCABULARIO DE ESTADOS CRECE EN SEIS MARCAS, TODAS LITERALES DEL")
    w("   ACTA: %s" % ", ".join(repr(x) for x in MARCAS_NUEVAS_197))
    w("   Y LA CIFRA QUE LAS JUSTIFICA VA DELANTE: con el lector de la 196, %d"
      % n_sin_decir_196)
    w("   adjudicacion(es) saldrian SIN DECIR y este registrador PARARIA.")
    w("   %d estado(s) salieron del PARRAFO con el lector de esta acta."
      % n_del_parrafo)
    w("   SE ANADEN Y NO SE ENSANCHA NINGUNA: EN CONTRA y A FAVOR siguen yendo")
    w("   primero y en ese orden, y una adjudicacion muda en el titulo Y en el")
    w("   parrafo sigue saliendo SIN DECIR y sigue haciendo PARAR.")
    w("   Y LA MARCA %r EXISTE POR UNA MEDICION: sin ella el estado de la 4.3"
      % MARCA_NO_MUEVE_LA_RACHA)
    w("   salia del PARRAFO, y salia por la frase 'No adjudico a favor del")
    w("   bucle', o sea por un A FAVOR que en su sitio dice lo contrario.")
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
    w("   la familia heredada y la de la primera clave discrepan en %d de %d"
      % (n_familia_distinta, len(adjudicaciones)))
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
    w("   SEPTIMA ACTA SEGUIDA. La guarda VIEJA de la 190 corrida aqui: %s"
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
        w("   PARADA: ninguna adjudicacion nombra un `P.n` y el acta 197 declara")
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
    w("   EL ACTA 197 ESCRIBE SUS HALLAZGOS EN NEGRITA DE APERTURA DE PARRAFO,")
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
        w("   PARADA: ningun lector encuentra hallazgos y el acta 197 declara CUATRO.")
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
    n_disc_fuera = numeral - len(hallazgos)
    puestos_fila = puestos_que_nombra_la_fila(fila_fuera[0][1])
    w("   LA RESTA HEREDADA (numeral menos hallazgos) da %d, Y SE PUBLICA IGUAL."
      % n_disc_fuera)
    w("   LOS PUESTOS QUE LA PROPIA FILA NOMBRA, CONTADOS: %d -> %s"
      % (len(puestos_fila), ", ".join(puestos_fila) or "(ninguno)"))
    w("   LAS DOS CIFRAS SE PUBLICAN Y LA DISCREPANCIA SE DECLARA EN VEZ DE")
    w("   RESOLVERSE: en esta acta la fila NO cuenta juntos discrepancias y")
    w("   hallazgos, los cinco puestos que nombra son discrepancias, y la resta")
    w("   heredada da %d porque supone la mezcla de otras actas." % n_disc_fuera)
    if n_disc_fuera < 0:
        w("   PARADA: la resta da negativo.")
        print(NL.join(salida))
        return 1
    w("")

    w("F) LAS CAIDAS DE LA SECCION %d, TODAS LAS CLAVES DE CADA TITULAR"
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
    una_por_titular = R96.caidas_en_titular_con_letra(lineas, ini3, fin3)
    c_todas = caidas_en_titular_con_varias_claves(lineas, ini3, fin3)
    w("   EL LECTOR DE LA 194, CORRIDO TAL CUAL SOBRE ESTA SECCION -> %d"
      % len(heredadas))
    w("   EL LECTOR DE LA 196 (una clave por titular)               -> %d"
      % len(una_por_titular))
    w("   EL LECTOR DE ESTA ACTA (todas las claves del titular)     -> %d"
      % len(c_todas))
    perdidas = [k for k, _l, _t in c_todas
                if k not in [x for x, _l2, _t2 in una_por_titular]]
    w("   LAS QUE EL DE LA 196 PIERDE, NOMBRADAS: %s"
      % (", ".join(perdidas) or "(ninguna)"))
    w("   LAS TRES CIFRAS SE PUBLICAN Y NINGUN LECTOR SE RETIRA.")
    if not c_todas:
        w("   PARADA: la seccion %d no trae ninguna clave `C.n`."
          % SECCION_DE_LAS_CAIDAS)
        print(NL.join(salida))
        return 1
    caidas = []
    for clave, ln, literal in c_todas:
        parte_196 = R96.parte_de_la_caida(literal)
        parte = parte_de_la_caida_197(literal)
        esp = R92.especie_de_la_caida(literal, marcas=MARCAS_DE_ESPECIE_197)
        esp_196 = R92.especie_de_la_caida(literal, marcas=R96.MARCAS_DE_ESPECIE_196)
        caidas.append((clave, ln, parte, esp, literal, parte_196, esp_196))
        w("      %-6s linea %-6d parte %-9s (con el de la 196: %-9s) especie %s"
          % (clave, ln, parte, parte_196, ", ".join(esp) or "NINGUNA"))
        w("            %s" % literal[:130])
    sin_parte = [x for x in caidas if x[2] == "SIN DECIR"]
    if sin_parte:
        w("   PARADA: hay %d caida(s) SIN PARTE DECLARADA en su titulo:"
          % len(sin_parte))
        for k, ln, _p, _e, _l, _p6, _e6 in sin_parte:
            w("      %s en la linea %d" % (k, ln))
        print(NL.join(salida))
        return 1
    sin_parte_196 = [x[0] for x in caidas if x[5] == "SIN DECIR"]
    w("   CON EL LECTOR DE PARTE DE LA 196 SALDRIAN SIN DECIR: %d -> %s"
      % (len(sin_parte_196), ", ".join(sin_parte_196) or "(ninguna)"))
    w("   ESA ES LA CIFRA QUE OBLIGA EL PLURAL %r, literal del titular de la"
      % MARCA_PARTE_AUDITOR_PLURAL)
    w("   `C.A3`. La guarda no se afloja: se le anade una forma.")
    sin_especie = [x for x in caidas if not x[3]]
    if sin_especie:
        w("   PARADA: hay %d caida(s) SIN ESPECIE DECLARADA:" % len(sin_especie))
        for k, ln, _p, _e, _l, _p6, _e6 in sin_especie:
            w("      %s en la linea %d" % (k, ln))
        print(NL.join(salida))
        return 1
    sin_especie_196 = [x[0] for x in caidas if not x[6]]
    w("   CON LAS MARCAS DE ESPECIE DE LA 196 SALDRIAN SIN ESPECIE: %d -> %s"
      % (len(sin_especie_196), ", ".join(sin_especie_196) or "(ninguna)"))
    w("   ESA ES LA CIFRA QUE OBLIGA LA MARCA %r, literal de la `C.E1`."
      % MARCA_ESPECIE_REPORTE)
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
    w("   EL COTEJO CONTRA EL CUERPO SE HACE CONTRA LA DEL TOTAL:")
    w("   cuerpo del AUDITOR %d contra fila del TOTAL %d -> %s"
      % (len(c_aud), num_aud_total,
         "CALZA" if len(c_aud) == num_aud_total else "NO CALZA"))
    n_aud_196 = len([1 for _k, _l, lit in una_por_titular
                     if parte_de_la_caida_197(lit) == "AUDITOR"])
    w("   Y CON EL LECTOR DE LA 196 EL CUERPO HABRIA DADO %d, o sea %s:"
      % (n_aud_196, "CALZA" if n_aud_196 == num_aud_total else "NO CALZA"))
    w("   ESA ES LA CIFRA QUE OBLIGA EL LECTOR DE VARIAS CLAVES POR TITULAR, y")
    w("   NO SE TECLEA: sale de correr el lector viejo sobre esta misma acta.")
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
    w("   EL COTEJO DE LA FILA DE CIFRA CONTRA EL CUERPO: cuerpo %d contra fila"
      % n_cifra_eje)
    w("   %d -> %s" % (num_cif, "CALZA" if n_cifra_eje == num_cif else "NO CALZA"))
    if n_cifra_eje != num_cif:
        w("   PARADA: la fila de cifra publicada y el cuerpo no calzan.")
        print(NL.join(salida))
        return 1
    _lit_met_her, exp_met_her = R92.expandir_rangos_de_clave(fila_met[0][1])
    lit_met, exp_met = claves_con_letra_de_la_fila(fila_met[0][1])
    w("   EL LECTOR HEREDADO, DE SOLO DIGITOS, VE %d clave(s) en la fila de"
      % len(exp_met_her))
    w("   METODO, y con eso el cotejo de la 196 se iria a su rama SIN DIENTES.")
    w("   EL LECTOR DE CLAVES CON LETRA VE %s" % (", ".join(exp_met) or "(ninguna)"))
    if exp_met:
        w("   LA EXIGENCIA DURA VUELVE A CORRER, Y ESO ENDURECE:")
        if len(exp_met) != num_met:
            w("   PARADA: claves del rango %d contra fila %d."
              % (len(exp_met), num_met))
            print(NL.join(salida))
            return 1
        w("      %d claves contra fila %d -> CALZA" % (len(exp_met), num_met))
    else:
        w("   LA FILA NO NOMBRA NINGUNA CLAVE NI CON LETRA. La exigencia sigue")
        w("   siendo condicional, como la dejo la 196.")
    lit_rep, exp_rep = claves_con_letra_de_la_fila(fila_rep[0][1])
    w("   Y LA FILA DE REPORTE NOMBRA %s contra su cifra %d -> %s"
      % (", ".join(exp_rep) or "(ninguna)", num_rep,
         "CALZA" if len(exp_rep) == num_rep else "NO CALZA"))
    if exp_rep and len(exp_rep) != num_rep:
        w("   PARADA: la fila de reporte nombra claves que no calzan con su cifra.")
        print(NL.join(salida))
        return 1
    w("   LAS TRES DEL EJECUTOR SUMAN %d." % (num_rep + num_met + num_cif))
    m_racha_rep = re.search(r"racha de reporte:\s*(\d+)", fila_rep[0][1])
    m_racha_cif = re.search(r"racha de cifra publicada:\s*(\d+)", fila_cif[0][1])
    racha_rep = m_racha_rep.group(1) if m_racha_rep else None
    racha_cif = m_racha_cif.group(1) if m_racha_cif else None
    w("   LAS DOS RACHAS, LEIDAS DE LA CELDA DERECHA DE SU FILA Y NO SUPUESTAS:")
    w("      racha de reporte: %s | racha de cifra publicada: %s"
      % (racha_rep, racha_cif))
    if racha_rep is None or racha_cif is None:
        w("   PARADA: alguna de las dos celdas no publica su racha. No se teclea.")
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
    w("   LA FILA DE PUESTOS: %d" % len(fila_p))
    for ln, txt in fila_p:
        w("      LINEA %-6d %s" % (ln, txt))
    if len(fila_p) != 1:
        w("   PARADA: la fila de puestos aparece %d veces." % len(fila_p))
        print(NL.join(salida))
        return 1
    notas = R94.nota_de_la_fila_de_puestos(
        fila_p[0][1], (R92.NOTA_DE_PUESTOS, R94.NOTA_DE_PUESTOS_194,
                       R95.NOTA_DE_PUESTOS_195, NOTA_DE_PUESTOS_196))
    w("   LAS CUATRO NOTAS HEREDADAS:")
    for marca, tal_cual, en_mayus, literal in notas:
        w("      %-16r tal cual: %-3s | en mayusculas: %-3s | literal: %r"
          % (marca, "SI" if tal_cual else "NO", "SI" if en_mayus else "NO", literal))
    if not notas[3][2]:
        w("   PARADA: la fila de puestos no trae la nota de los quemados.")
        print(NL.join(salida))
        return 1
    her_cifras = R95.cifras_de_la_fila_de_puestos(fila_p[0][1])
    aisl, cot, quem, limpio_en_fila = cifras_de_la_fila_de_puestos_197(fila_p[0][1])
    w("   EL LECTOR DE LA 195, CORRIDO TAL CUAL: %r" % (her_cifras,))
    w("   EL LECTOR DE ESTA ACTA:                %r"
      % ((aisl, cot, quem, limpio_en_fila),))
    w("   ESA ES LA CIFRA QUE LO OBLIGA: el acta escribe las tres dentro de UN")
    w("   SOLO par de asteriscos y el heredado exige los suyos a cada una.")
    if not (aisl and cot and quem):
        w("   PARADA: alguna de las tres cifras obligatorias no se lee.")
        print(NL.join(salida))
        return 1
    cero_quemados = R95.quemados_son_cero(quem)
    w("   LOS QUEMADOS SON CERO: %s" % ("SI" if cero_quemados else "NO"))
    limpios_196 = R96.cotejo_limpio_del_cuerpo(lineas, inicio, fin)
    limpios = cotejo_limpio_197(lineas, inicio, fin)
    w("   EL COTEJO LIMPIO CON EL PATRON DE LA 196: %d acierto(s)" % len(limpios_196))
    w("   EL COTEJO LIMPIO CON EL PATRON DE ESTA ACTA:")
    for ln, cifra in limpios:
        w("      linea %d -> %d" % (ln, cifra))
    limpio = limpios[0][1] if limpios else None
    if not cero_quemados:
        esperado = int(cot) - int(quem)
        w("   HAY QUEMADOS, ASI QUE LA EXIGENCIA CORRE Y SIGUE ENDURECIDA:")
        w("   %s - %s = %d contra el %s que el acta publica -> %s"
          % (cot, quem, esperado, limpio,
             "CALZA" if limpio == esperado else "NO CALZA"))
        if limpio is None:
            w("   PARADA: hay quemados y el acta no publica el cotejo limpio.")
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
    w("   EL ENCARGO CITA R.59 Y DICE QUE MANDE MI CORRIDA: la de arriba es la")
    w("   mia, corrida HOY.")
    w("")

    w("K) LA DEUDA DE LA SERIE, REMEDIDA AQUI Y NO HEREDADA")
    salto = R92.actas_sin_entrada(halladas, 173, VUELTA_DEL_ACTA - 1)
    faltan, bajo, alto = salto
    w("   tramo mirado: actas 173 a %d" % (VUELTA_DEL_ACTA - 1))
    w("   CIFRA actas SIN entrada propia en la serie: %d" % len(faltan))
    w("   LAS QUE FALTAN: %s" % (", ".join(str(x) for x in faltan) or "(ninguna)"))
    w("   el registro heredado dice OCHO (173 a 180) -> %s"
      % ("CALZA" if len(faltan) == 8 else "NO CALZA, y la discrepancia se declara"))
    w("")

    medido = {
        "inicio": inicio, "fin": fin, "secciones": secciones,
        "bytes_acta": os.path.getsize(ACTA),
        "n_adj": len(claves), "n_entrecomillado": len(entrecomilladas),
        "n_suelto": len(sueltas), "n_negrita_sola": len(negrita_sola),
        "adjudicaciones": adjudicaciones,
        "n_discutibles": len(discutibles), "n_preg": len(preguntas),
        "n_otras": len(otras), "n_a_favor_discutibles": len(a_favor),
        "n_en_contra_discutibles": len(en_contra),
        "vieja_pararia": not en_contra,
        "n_sin_decir_196": n_sin_decir_196, "n_del_parrafo": n_del_parrafo,
        "n_familia_distinta": n_familia_distinta,
        "arnes_disco": len(datos_arnes), "arnes_lf": len(lf_arnes),
        "arnes_veredicto": ver_arnes[0] if ver_arnes else "",
        "preguntas": [(a[0], R92.PAT_P_DEL_TITULO.search(a[4]).group(0).strip("`"))
                      for a in preguntas],
        "hallazgos": hallazgos, "n_hall": len(hallazgos),
        "her_sueltos": len(her_sueltos), "her_comillas": len(her_comillas),
        "n_titulares": len(titulares),
        "fila_fuera": fila_fuera, "numeral_fila": numeral,
        "n_disc_fuera": n_disc_fuera, "puestos_fila": puestos_fila,
        "cabecera_seccion3": cabecera3,
        "seccion_caidas": SECCION_DE_LAS_CAIDAS,
        "n_heredadas": len(heredadas),
        "n_una_por_titular": len(una_por_titular), "perdidas": perdidas,
        "caidas": caidas, "c_aud": c_aud, "c_eje": c_eje,
        "n_aud": len(c_aud), "n_eje": len(c_eje),
        "n_cifra_eje": n_cifra_eje, "n_metodo_aud": n_metodo_aud,
        "sin_parte_196": sin_parte_196, "sin_especie_196": sin_especie_196,
        "n_corta": len(corta), "n_aud_196": n_aud_196,
        "num_aud_acum": num_aud_acum, "num_aud_total": num_aud_total,
        "num_rep": num_rep, "num_met": num_met, "num_cif": num_cif,
        "racha_rep": racha_rep, "racha_cif": racha_cif,
        "exp_met": exp_met, "exp_met_her": exp_met_her, "exp_rep": exp_rep,
        "fila_rep": fila_rep, "fila_met": fila_met, "fila_cif": fila_cif,
        "filas7": filas7, "n_filas7": len(filas7),
        "fila_puestos": fila_p, "notas": notas, "her_cifras": her_cifras,
        "aislados": aisl, "cotejados": cot, "quemados": quem,
        "limpio_en_fila": limpio_en_fila, "limpios": limpios, "limpio": limpio,
        "n_limpios_196": len(limpios_196),
        "cero_quemados": cero_quemados,
        "salto": salto, "numero": numero, "ya_registrada": len(ya),
        "sedes": sedes,
    }
    return salida, medido


def titulo_de_la_entrada(n_adj, n_hall, n_preg, n_cai_aud, n_cai_eje):
    """EL TITULO DE LA ENTRADA, CON SUS CINCO NUMERALES EN PALABRA. PURA.

    NO SE DELEGA EN LA MAQUINA DE OTRO REGISTRADOR, Y LA RAZON ESTA MEDIDA: todas
    cierran con `VUELTA_DEL_ACTA` de SU modulo, y por eso un titulo armado con
    ellas nombraria el acta equivocada."""
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
    p.append("Por adicion, como `R.21` a `R.58`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162. Salida:")
    p.append("`docs/loop/SALIDA_V%s_T1A_REGISTRO_R%d.txt`."
             % (SUFIJO_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LAS TAREAS 2, 3 Y 4 SIN EMPEZAR, ASI QUE SUS")
    p.append("GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA NO HA PASADO.** Es la forma que la")
    p.append("`6.4` del acta 172 adjudico como correcta. **Y EL ORDEN VA DECLARADO EN VEZ")
    p.append("DE DEJARSE, Y ESTA VEZ CONTRA MI:** la TAREA 1 va PRIMERA aunque el acta 197")
    p.append("publica en su `4.1` y en su `5.3` la clase de archivo de NUEVE puestos que")
    p.append("caen DENTRO de los 240 que la TAREA 3 lee a ciegas. **Esos nueve se declaran")
    p.append("QUEMADOS antes de leer y salen del credito**, que es la via que el propio")
    p.append("encargo manda y la misma que el acta 196 acepto para el `2662`.")
    p.append("**La 197 NO es vuelta de bateria** (`AUDITOR.md` 6.1: la 194 la corrio entera")
    p.append("por sus diez tramos y la proxima cae en la 199).")
    p.append("")
    p.append("**LOS CINCO NUMERALES DEL TITULO NO ESTAN TECLEADOS:** se cuentan del acta")
    p.append("acotada (lineas %d a %d, sobre un fichero de %d bytes). **%d adjudicaciones"
             % (m["inicio"], m["fin"], m["bytes_acta"], m["n_adj"]))
    p.append("numeradas (`4.1` a `4.%d`), %d hallazgos numerados en la seccion 5, %d"
             % (m["n_adj"], m["n_hall"], m["n_preg"]))
    p.append("preguntas contestadas DENTRO de las adjudicaciones, %d caidas propias del"
             % m["n_aud"])
    p.append("auditor y %d caidas del ejecutor.**"
             % (m["num_rep"] + m["num_met"] + m["num_cif"]))
    p.append("")
    p.append("### LOS SIETE LECTORES NUEVOS, CADA UNO CON LA CIFRA QUE LO OBLIGA")
    p.append("")
    p.append("**NINGUNO SE ESCRIBIO POR GUSTO: cada uno tiene delante la cifra que este")
    p.append("registrador habria publicado sin el, y en los seis primeros esa cifra es una")
    p.append("PARADA sobre un acta correcta.**")
    p.append("")
    p.append("| lector | que lee | sin el | con el |")
    p.append("|---|---|---|---|")
    p.append("| `caidas_en_titular_con_varias_claves()` | todas las claves de un titular |"
             " %d claves, pierde %s | %d claves |"
             % (m["n_una_por_titular"], ", ".join("`%s`" % x for x in m["perdidas"]),
                len(m["caidas"])))
    p.append("| `parte_de_la_caida_197()` | la parte en plural (`MIAS`) |"
             " %d `SIN DECIR` (%s) | 0 |"
             % (len(m["sin_parte_196"]),
                ", ".join("`%s`" % x for x in m["sin_parte_196"]) or "ninguna"))
    p.append("| `cifras_de_la_fila_de_puestos_197()` | la celda entera en negrita |"
             " `%r` | `%r` |"
             % (m["her_cifras"],
                (m["aislados"], m["cotejados"], m["quemados"], m["limpio_en_fila"])))
    p.append("| `cotejo_limpio_197()` | *\"los **112** LIMPIOS\"* |"
             " %d aciertos | %d aciertos |"
             % (m["n_limpios_196"], len(m["limpios"])))
    p.append("| `estado_de_la_adjudicacion_197()` | seis marcas literales del acta |"
             " %d `SIN DECIR` | 0 |" % m["n_sin_decir_196"])
    p.append("| `claves_con_letra_de_la_fila()` | `` `C.E2` `` en la fila de metodo |"
             " %d claves, rama sin dientes | %d claves, exigencia dura |"
             % (len(m["exp_met_her"]), len(m["exp_met"])))
    p.append("| `puestos_que_nombra_la_fila()` | los puestos de la fila de FUERA |"
             " la resta da %d | la fila nombra %d |"
             % (m["n_disc_fuera"], len(m["puestos_fila"])))
    p.append("")
    p.append("**EL SEPTIMO NO SALVA NINGUNA PARADA Y SE ESCRIBE IGUAL, Y SE DICE POR QUE:**")
    p.append("la resta heredada (`numeral - hallazgos`) da **%d** sobre esta acta, porque"
             % m["n_disc_fuera"])
    p.append("supone que la fila cuenta juntas las discrepancias y los hallazgos, **y en el")
    p.append("acta 197 no los cuenta juntos**: la fila nombra **%d** puestos"
             % len(m["puestos_fila"]))
    p.append("(%s), los %d son discrepancias, y los %d hallazgos viven en su propia"
             % (", ".join("`%s`" % x for x in m["puestos_fila"]),
                len(m["puestos_fila"]), m["n_hall"]))
    p.append("seccion. **LAS DOS CIFRAS SE PUBLICAN Y LA DISCREPANCIA SE DECLARA:** la")
    p.append("resta no se retira, deja de ser la unica.")
    p.append("")
    p.append("### LAS %d ADJUDICACIONES, UNA POR UNA, CON SU ESTADO Y SU PROCEDENCIA"
             % m["n_adj"])
    p.append("")
    p.append("| clave | familia | estado | de donde sale | con el lector de la 196 | linea |")
    p.append("|---|---|---|---|---|---:|")
    for (clave, fam, est, ln, _t, _forma, proc, _fam_her, est_196,
         _proc_196) in m["adjudicaciones"]:
        p.append("| `%s` | %s | %s | %s | %s | %d |"
                 % (clave, fam, est, proc, est_196, ln))
    p.append("")
    p.append("**EL VOCABULARIO DE ESTADOS CRECE EN SEIS MARCAS, TODAS LITERALES DE LOS")
    p.append("TITULOS DEL ACTA:** %s. **Con el lector"
             % ", ".join("`%s`" % x for x in MARCAS_NUEVAS_197))
    p.append("de la 196, %d de las %d saldrian `SIN DECIR` y este registrador PARARIA**"
             % (m["n_sin_decir_196"], m["n_adj"]))
    p.append("sobre un acta que las adjudica todas con claridad. **Se anaden y no se")
    p.append("ensancha ninguna:** `EN CONTRA` y `A FAVOR` siguen yendo primero y en ese")
    p.append("orden, y una adjudicacion muda en el titulo **y** en el parrafo sigue saliendo")
    p.append("`SIN DECIR` y sigue haciendo PARAR.")
    p.append("")
    p.append("**Y UNA DE LAS SEIS EXISTE POR UNA MEDICION Y NO POR COMODIDAD.** Sin")
    p.append("`NO MUEVE LA RACHA`, el estado de la `4.3` salia del **PARRAFO**, y salia por")
    p.append("la frase *\"No adjudico a favor del bucle: adjudico por la sede\"*: o sea, por")
    p.append("un `A FAVOR` que **en su sitio dice lo contrario de lo que el lector entiende**.")
    p.append("Con la marca del titulo, la `4.3` deja de depender de esa frase. **Las dos")
    p.append("lecturas se publican en la tabla de arriba.**")
    p.append("")
    p.append("### LAS %d CAIDAS DEL CUERPO, REPARTIDAS POR LO QUE SU TITULAR DICE"
             % len(m["caidas"]))
    p.append("")
    p.append("| clave | parte | especie | linea |")
    p.append("|---|---|---|---:|")
    for clave, ln, parte, esp, _lit, _p6, _e6 in m["caidas"]:
        p.append("| `%s` | %s | %s | %d |" % (clave, parte, ", ".join(esp), ln))
    p.append("")
    p.append("**DOS TITULARES LLEVAN DOS CLAVES CADA UNO** (``### `C.E2` Y `C.E3`...`` y")
    p.append("``### `C.A3` Y `C.A4`...``), y el lector de la 196 se queda con la primera de")
    p.append("cada uno. **MEDIDO: %d claves contra %d, y las que pierde son %s.**"
             % (m["n_una_por_titular"], len(m["caidas"]),
                ", ".join("`%s`" % x for x in m["perdidas"])))
    p.append("Con esa cuenta el cuerpo daria **%d** caidas del auditor contra la fila del"
             % m["n_aud_196"])
    p.append("TOTAL, que dice **%d**, y este registrador PARARIA sobre un acta correcta."
             % m["num_aud_total"])
    p.append("")
    p.append("**Y LA ESPECIE DE LA `C.E1` OBLIGA UNA MARCA NUEVA, LITERAL:**")
    p.append("`%s`. Su titular dice *\"ES DE REPORTE, NO DE CIFRA\"*, y con las"
             % MARCA_ESPECIE_REPORTE)
    p.append("marcas de la 196 saldria SIN ESPECIE (%s) y el registrador PARARIA."
             % (", ".join("`%s`" % x for x in m["sin_especie_196"]) or "ninguna"))
    p.append("")
    p.append("### LA TABLA DE CREDITO, CON LAS DOS PARTES PUBLICADAS")
    p.append("")
    p.append("| fila | cuerpo | fila del acta |")
    p.append("|---|---:|---:|")
    p.append("| caidas propias del auditor, TOTAL | %d | %d |"
             % (m["n_aud"], m["num_aud_total"]))
    p.append("| caidas propias del auditor, QUE ACUMULAN | %s | %s |"
             % (m["num_aud_acum"], m["num_aud_acum"]))
    p.append("| del ejecutor, de cifra publicada | %d | %d |"
             % (m["n_cifra_eje"], m["num_cif"]))
    p.append("| del ejecutor, de reporte | %d | %d |" % (m["num_rep"], m["num_rep"]))
    p.append("| del ejecutor, de metodo | %d | %d |" % (m["num_met"], m["num_met"]))
    p.append("")
    p.append("**LAS DOS RACHAS SE LEEN DE LA CELDA DERECHA DE SU PROPIA FILA Y NO SE")
    p.append("SUPONEN: racha de cifra publicada %s, racha de reporte %s.** La `C.E1` de la"
             % (m["racha_cif"], m["racha_rep"]))
    p.append("vuelta 196 **la re clasifico el propio auditor en su `4.3`**, de cifra")
    p.append("publicada a **reporte**, y por la letra del 27 ago 2026 **no acumula**, porque")
    p.append("vive en prosa de acompanamiento y no en una tabla, una cabecera o una")
    p.append("conclusion. **Lo registro como el acta lo escribe, y digo que me favorece.**")
    p.append("")
    p.append("### LA FILA DE PUESTOS Y EL COTEJO LIMPIO")
    p.append("")
    p.append("**%s aislados, %s cotejados, %s quemados**, y el cotejo limpio va sobre"
             % (m["aislados"], m["cotejados"], m["quemados"]))
    p.append("**%s**, leido de la seccion 2 del acta y **exigido a CALZAR** con"
             % m["limpio"])
    p.append("`cotejados - quemados` = **%d**. La exigencia que la 196 endurecio **sigue"
             % (int(m["cotejados"]) - int(m["quemados"])))
    p.append("entera**; lo unico que cambia es **donde se lee**, porque esta acta lo escribe")
    p.append("en la cabecera de su tabla y no en su fila de puestos.")
    p.append("")
    p.append("### LA METRICA DE CREDITO, TAL COMO EL ACTA LA PUBLICA")
    p.append("")
    for ln, txt in m["filas7"]:
        p.append(txt)
    p.append("")
    p.append("### LOS HALLAZGOS DE LA SECCION 5, QUE NO SALEN DE NINGUN DISCUTIBLE")
    p.append("")
    for clave, ln, tit in m["hallazgos"]:
        p.append("- **`%s`** (linea %d): %s" % (clave, ln, tit))
    p.append("")
    p.append("### LA DEUDA DE LA SERIE, REMEDIDA Y NO HEREDADA")
    p.append("")
    faltan, bajo, alto = m["salto"]
    p.append("Actas 173 a %d sin entrada propia en la serie: **%d** (%s). **La cifra"
             % (VUELTA_DEL_ACTA - 1, len(faltan),
                ", ".join(str(x) for x in faltan) or "ninguna"))
    p.append("se recomputa cada vuelta y no se hereda.** Los dos extremos del salto,")
    p.append("leidos de los titulos y no tecleados: bajo `%s`, alto `%s`."
             % (bajo, alto))
    p.append("")
    return NL.join(p) + NL


# ---------------------------------------------------------------- LA MUTACION
_CUENTA = {"casos": 0, "pasan": 0}


def _caso(w, nombre, obtenido, esperado):
    """UN CASO, Y LA CUENTA LA LLEVA EL ARNES Y NO EL QUE LO CITA."""
    ok = obtenido == esperado
    _CUENTA["casos"] += 1
    _CUENTA["pasan"] += 1 if ok else 0
    w("   %-64s %s" % (nombre, "VERDE" if ok else "ROJO"))
    if not ok:
        w("      esperado: %r" % (esperado,))
        w("      obtenido: %r" % (obtenido,))
    return ok


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION DE LOS SIETE LECTORES QUE ESTE REGISTRADOR
    ESTRENA.

    LOS SIETE SON PUROS y se corren sobre texto FABRICADO, con el valor esperado
    sacado de COMO SE FABRICO EL TEXTO y no de una constante igual a la obtenida.
    `EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION: de cada lector se
    comprueba ADEMAS que el heredado CAE sobre el mismo texto, que es la unica
    forma de que "hacia falta un lector nuevo" sea una medicion y no una excusa."""
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("VUELTA 197, TAREA 1: CASO POSITIVO POR MUTACION DEL REGISTRADOR")
    w("=" * 78)
    w("")

    w("A) `caidas_en_titular_con_varias_claves()` SOBRE TITULARES FABRICADOS")
    fab = [
        "## 3. LAS CAIDAS",
        "",
        "### `C.E1` DEL EJECUTOR, DE REPORTE",
        "Cuerpo, y aqui se cita la `C.A9` que NO es un titular.",
        "",
        "### `C.E2` Y `C.E3` DEL EJECUTOR, DE METODO",
        "Cuerpo.",
        "",
        "### `C.A3` Y `C.A4` MIAS, DE METODO",
        "Cuerpo.",
        "",
    ]
    viejo = [k for k, _l, _t in R96.caidas_en_titular_con_letra(fab, 1, len(fab))]
    nuevo = [k for k, _l, _t in caidas_en_titular_con_varias_claves(fab, 1, len(fab))]
    ok &= _caso(w, "el lector de la 196 se queda con la PRIMERA de cada titular",
                viejo, ["C.E1", "C.E2", "C.A3"])
    ok &= _caso(w, "el lector nuevo lee las CINCO claves de los tres titulares",
                nuevo, ["C.E1", "C.E2", "C.E3", "C.A3", "C.A4"])
    ok &= _caso(w, "y NO se cuela la `C.A9` que solo vive en el cuerpo",
                "C.A9" in nuevo, False)
    w("   LA MUTACION: si el lector nuevo mirara el parrafo y no el titular, la")
    w("   `C.A9` entraria y habria SEIS caidas donde hay cinco.")
    w("")

    w("B) `parte_de_la_caida_197()` Y EL PLURAL")
    ok &= _caso(w, "el lector de la 196 no sabe leer MIAS",
                R96.parte_de_la_caida("### `C.A3` Y `C.A4` MIAS, DE METODO"),
                "SIN DECIR")
    ok &= _caso(w, "el nuevo si, y devuelve AUDITOR",
                parte_de_la_caida_197("### `C.A3` Y `C.A4` MIAS, DE METODO"),
                "AUDITOR")
    ok &= _caso(w, "el singular sigue funcionando igual que antes",
                parte_de_la_caida_197("### `C.A1` MIA, DE METODO"), "AUDITOR")
    ok &= _caso(w, "el ejecutor sigue ganando cuando su marca esta",
                parte_de_la_caida_197("### `C.E1` DEL EJECUTOR, DE REPORTE"),
                "EJECUTOR")
    ok &= _caso(w, "un titular mudo SIGUE saliendo SIN DECIR y haciendo PARAR",
                parte_de_la_caida_197("### `C.X1` UNA CAIDA SIN DUENO"),
                "SIN DECIR")
    w("   LA MUTACION: si el plural se hubiera metido ENSANCHANDO el patron a")
    w("   `MIA` sin frontera, `MIAMI` tambien casaria. Se comprueba:")
    ok &= _caso(w, "una palabra que solo CONTIENE MIA no atribuye nada",
                parte_de_la_caida_197("### `C.X2` LA CAIDA DE MIAMI"), "SIN DECIR")
    w("")

    w("C) `cifras_de_la_fila_de_puestos_197()` CON LA CELDA ENTERA EN NEGRITA")
    fila_env = "| puestos | **120 aislados, 120 cotejados, 8 quemados** | **1.306** |"
    fila_vieja = ("| puestos | 60 aislados, **58 cotejados** y **DOS QUEMADOS** | "
                  "**1.186** |")
    ok &= _caso(w, "el lector de la 195 no lee la forma envolvente",
                R95.cifras_de_la_fila_de_puestos(fila_env),
                ("120", None, None, None))
    ok &= _caso(w, "el nuevo lee las tres cifras",
                cifras_de_la_fila_de_puestos_197(fila_env)[:3],
                ("120", "120", "8"))
    ok &= _caso(w, "y la forma VIEJA sigue leyendose igual que antes",
                cifras_de_la_fila_de_puestos_197(fila_vieja)[:3],
                R95.cifras_de_la_fila_de_puestos(fila_vieja)[:3])
    w("   LA MUTACION: si el nuevo hubiera SUSTITUIDO al heredado en vez de")
    w("   correr detras, la fila vieja habria cambiado de valor. No cambia.")
    w("")

    w("D) `cotejo_limpio_197()` DONDE EL ACTA LO ESCRIBE")
    fab2 = ["## 2. LA CIEGA",
            "",
            "| **los 112 LIMPIOS, y es la cifra que manda** | **103 de 112** | **9** |",
            ""]
    ok &= _caso(w, "el patron de la 196 no encuentra nada aqui",
                R96.cotejo_limpio_del_cuerpo(fab2, 1, len(fab2)), [])
    ok &= _caso(w, "el patron de esta acta lee el 112",
                [c for _l, c in cotejo_limpio_197(fab2, 1, len(fab2))], [112])
    fab3 = ["texto sin ninguna cifra de cotejo limpio"]
    ok &= _caso(w, "y sobre un texto mudo devuelve vacio, que es lo que hace PARAR",
                cotejo_limpio_197(fab3, 1, 1), [])
    w("   LA MUTACION QUE MAS IMPORTA: el acta trae DOS filas con la misma cifra,")
    w("   una en MAYUSCULAS (la del cotejo) y otra en minusculas (el reparto por")
    w("   clase). Si el patron fuera insensible a la caja, cogeria la que llegue")
    w("   antes y la cifra publicada dependeria del orden de las filas.")
    fab4 = ["| sobre los 999 limpios | A 16, D 96 | A 13, D 99 |"]
    ok &= _caso(w, "la fila en minusculas NO casa, y por eso no puede colarse",
                cotejo_limpio_197(fab4, 1, 1), [])
    w("")

    w("E) `estado_de_la_adjudicacion_197()` Y SUS SEIS MARCAS")
    casos_estado = [
        ("`4.2` LAS CUATRO QUEMADAS SE PUBLICAN Y NO ENTRAN AL CREDITO",
         "PUBLICADAS Y FUERA DEL CREDITO"),
        ("`4.3` LA `P.1`: NO MUEVE LA RACHA, Y NO HACE FALTA DOCTRINA NUEVA.",
         "CONTESTADA: NO MUEVE LA RACHA, SIN DOCTRINA NUEVA"),
        ("`4.4` NO SE ENSANCHA LA LISTA BLANCA; ESOS PUESTOS SALEN DEL CREDITO.",
         "CONTESTADA: NO SE ENSANCHA LA LISTA BLANCA, SALEN DEL CREDITO"),
        ("`4.5` ADJUDICADA POR EXTENSION Y CONTRA MI PROPIO TURNO.",
         "CONTESTADA POR EXTENSION Y CONTRA EL PROPIO AUDITOR"),
        ("`4.6` EL TOPE SE MANTIENE Y NO SE AFLOJA, PERO SE MIDE POR TRES VARAS.",
         "SE MANTIENE, Y SE MIDE POR TRES VARAS"),
        ("`4.7` EL 0 DE LA SECCION 9 NO ES CAIDA, Y SE ARREGLA IGUAL.",
         "NO ES CAIDA, Y SE ARREGLA IGUAL"),
    ]
    n_mudas = 0
    for texto, esperado in casos_estado:
        if R96.estado_de_la_adjudicacion_196(texto) == "SIN DECIR":
            n_mudas += 1
        ok &= _caso(w, "estado de %s" % texto[:44], estado_de_la_adjudicacion_197(texto),
                    esperado)
    ok &= _caso(w, "las SEIS salen SIN DECIR con el lector de la 196", n_mudas, 6)
    ok &= _caso(w, "EN CONTRA sigue ganando a todas las nuevas",
                estado_de_la_adjudicacion_197(
                    "`4.9` EN CONTRA, Y ADEMAS NO ES CAIDA"), "EN CONTRA")
    ok &= _caso(w, "A FAVOR sigue ganando a todas las nuevas",
                estado_de_la_adjudicacion_197(
                    "`4.9` A FAVOR, Y ADEMAS SE MANTIENE Y NO SE AFLOJA"), "A FAVOR")
    ok &= _caso(w, "una adjudicacion muda SIGUE saliendo SIN DECIR",
                estado_de_la_adjudicacion_197("`4.9` UN TITULO QUE NO DICE NADA"),
                "SIN DECIR")
    ok &= _caso(w, "y la procedencia sigue diciendo NINGUNA cuando los dos callan",
                estado_con_su_procedencia_197("`4.9` MUDO", "parrafo mudo"),
                ("SIN DECIR", "NINGUNA"))
    w("")

    w("F) `claves_con_letra_de_la_fila()` Y EL RANGO")
    fila_m = "| caidas del ejecutor de metodo | **2** (`C.E2`, `C.E3`) | no acumulan |"
    fila_r = ("| caidas propias del auditor, TOTAL | **5** (`C.A1` a `C.A5`, todas "
              "de metodo) | |")
    _l, e_her = R92.expandir_rangos_de_clave(fila_m)
    ok &= _caso(w, "el heredado, de solo digitos, no ve ninguna clave con letra",
                e_her, [])
    ok &= _caso(w, "el nuevo lee las dos claves sueltas",
                claves_con_letra_de_la_fila(fila_m)[1], ["C.E2", "C.E3"])
    ok &= _caso(w, "y expande el rango de cinco",
                claves_con_letra_de_la_fila(fila_r)[1],
                ["C.A1", "C.A2", "C.A3", "C.A4", "C.A5"])
    ok &= _caso(w, "un rango al reves NO se adivina: quedan sus dos literales",
                claves_con_letra_de_la_fila("(`C.A5` a `C.A1`)")[1],
                ["C.A1", "C.A5"])
    ok &= _caso(w, "y un rango de letras distintas tampoco se expande",
                claves_con_letra_de_la_fila("(`C.A1` a `C.E3`)")[1],
                ["C.A1", "C.E3"])
    w("")

    w("G) `puestos_que_nombra_la_fila()`")
    fila_f = ("| discrepancias y hallazgos FUERA del marcado | **5** (`655`, `719`, "
              "`976`, `1809`, `1810`) | **179** |")
    ok &= _caso(w, "lee los cinco puestos y no la cifra de la celda",
                puestos_que_nombra_la_fila(fila_f),
                ["655", "719", "976", "1809", "1810"])
    ok &= _caso(w, "no repite un puesto nombrado dos veces",
                puestos_que_nombra_la_fila("(`655`, `655`, `719`)"), ["655", "719"])
    ok &= _caso(w, "y una fila sin puestos devuelve vacio en vez de inventar",
                puestos_que_nombra_la_fila("| fila | **5** | **179** |"), [])
    w("")

    w("=" * 78)
    w("CASOS: %d | VERDES: %d | ROJOS: %d"
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
    ok_guarda, informe = R96.entrada_publica_las_dos_partes(
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
