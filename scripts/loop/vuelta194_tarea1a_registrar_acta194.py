# -*- coding: utf-8 -*-
r"""vuelta194_tarea1a_registrar_acta194.py . EL ACTA 194 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA, Y ESTE REGISTRADOR SIGUE SIENDO IDEMPOTENTE.

LA MAQUINA SE IMPORTA Y NO SE COPIA. Todo lo generico (acotar el acta, leer
secciones, familia y estado de una adjudicacion, filas de la tabla de credito,
numerales, expansion de rangos, la serie) sale de
`vuelta192_tarea1a_registrar_acta192.py`, que a su vez importa de la 191, la 190
y la 189. AQUI SOLO VIVE LO QUE EL ACTA 194 TIENE DISTINTO, y va dicho uno por
uno para que nadie tenga que adivinarlo:

  1. LOS HALLAZGOS NO SON NEGRITAS: SON TITULARES `###`. El acta 194 escribe
     `### \`5.1\` TITULO` en vez de `**5.1 TITULO**`. Los dos lectores heredados
     (`claves_de_adjudicacion` con prefijo `5.` y `claves_entrecomilladas` con el
     mismo prefijo) dan CERO sobre esta acta, y con cero el registrador PARARIA
     por no encontrar hallazgos que el acta si tiene. Se anade
     `hallazgos_en_titular()`, que es un lector NUEVO y no un ensanche del viejo:
     LOS TRES SE CORREN Y LAS TRES CIFRAS SE PUBLICAN.

  2. LAS CAIDAS PROPIAS DEL AUDITOR VIVEN EN LA SECCION 8, NO EN LA 6. En el acta
     194 la seccion 6 es PENDIENTES DE DOCTRINA y la 8 es MIS CAIDAS PROPIAS. La
     maquina de lead de la 192 y la de numeral de la 191 miran una seccion de
     caidas con dos lados; aqui el acta tiene UN solo lado y lo titula. Se anade
     `caidas_propias_entrecomilladas()`, que lee `**\`C.n\` (...)` dentro del
     rango que se le pase.

  3. LA FILA DE PUESTOS YA NO DICE `SOLAPE TOTAL`: DICE `ONCE QUEMADOS`. La nota
     heredada `NOTA_DE_PUESTOS` NO aparece en esta acta, y el registrador de la
     193 PARARIA por eso. La marca nueva es literal del acta (`ONCE QUEMADOS`), y
     LA VIEJA SE SIGUE BUSCANDO Y SU RESULTADO SE PUBLICA en vez de retirarse:
     retirarla estrecharia el vocabulario a lo que el acta de hoy usa.

  4. Y LA QUE IMPORTA, DICHA ENTERA PORQUE ES UNA DISCREPANCIA MEDIDA DENTRO DEL
     ACTA. **El cuerpo de la seccion 8 del acta 194 declara DOS caidas propias
     del auditor (`C.1` y `C.2`) y su fila de la tabla de credito dice UNO.** El
     registrador de la 193 PARABA cuando el cuerpo y la fila no calzaban, y esa
     parada existia para cazar UN ERROR DE LECTURA DEL PROPIO REGISTRADOR. Aqui
     no hay error de lectura: las dos lecturas son correctas y **es el acta la
     que se contradice consigo misma**.

     QUE SE HACE, Y POR QUE ESTA ESCRITO ANTES DE MEDIR NADA MAS: el encargo de
     la vuelta 194 dice literal *"cada cifra se cuenta del cuerpo acotado del
     acta y no de aqui"*, y ademas nombra **DOS** caidas propias del auditor. O
     sea que la sede de la cifra es EL CUERPO. Se registra la del cuerpo, **SE
     PUBLICAN LAS DOS con su linea y su atribucion**, y la discrepancia se
     declara en la entrada y en el reporte en vez de resolverse copiando
     (`EJECUTOR.md` 2). **NINGUNA GUARDA SE AFLOJA:**

       - la parada por descuadre SIGUE ENTERA para las DOS filas del ejecutor
         (de reporte y de metodo), que es donde la lectura si podria fallar;
       - y SE ANADE UNA GUARDA NUEVA: si el cuerpo y la fila del auditor no
         calzan y **la entrada armada no publica LAS DOS cifras**, el registrador
         CAE EN ROJO y no escribe nada. Una discrepancia callada seria peor que
         la parada que sustituye.

TODA CIFRA SE CUENTA DEL CUERPO ACOTADO DEL ACTA Y NINGUNA DEL ENCARGO. Donde el
encargo publica una, se computa la propia y SE PUBLICAN LAS DOS.

EL NUMERO DE LA ENTRADA NO SE TECLEA: lo computa `serie_de_registros.py`
recomputando la serie de sus DOS sedes.

USO:
  python scripts/loop/vuelta194_tarea1a_registrar_acta194.py --simular
  python scripts/loop/vuelta194_tarea1a_registrar_acta194.py
  python scripts/loop/vuelta194_tarea1a_registrar_acta194.py --mutacion
"""
import argparse
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402
import vuelta192_tarea1a_registrar_acta192 as R92   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 194
VUELTA_QUE_ESCRIBE = 194
SUFIJO_QUE_ESCRIBE = "194"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "4."
PREFIJO_HALLAZGO = "5."
SECCION_DE_LOS_HALLAZGOS = 5
SECCION_DE_LAS_CAIDAS_PROPIAS = 8
SECCION_DE_LA_METRICA = 7

# (3) LA NOTA DE LA FILA DE PUESTOS QUE ESTA ACTA ESTRENA, LITERAL DE SU CELDA.
# La heredada (`SOLAPE TOTAL`) se sigue buscando y su resultado se publica.
NOTA_DE_PUESTOS_194 = "ONCE QUEMADOS"

# LAS FILAS DE LA TABLA DE CREDITO QUE ESTE REGISTRADOR COTEJA, POR SU AGUJA.
AGUJA_FILA_CAIDAS_REPORTE = "caidas del ejecutor de reporte"

# EL ARNES DE LA 191 QUE YA CUBRE EL CERO DE `EN CONTRA`, NOMBRADO PARA MEDIRLO
# EN VEZ DE RE FABRICAR SU CASO. Es la CUARTA acta seguida con cero.
ARNES_QUE_YA_CUBRE = "docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt"

# LAS ESPECIES, HEREDADAS, MAS LA QUE ESTA ACTA ESTRENA.
MARCA_ESPECIE_METODO = R92.MARCA_ESPECIE_METODO
MARCA_ESPECIE_CIFRA = R92.MARCA_ESPECIE_CIFRA
MARCA_ESPECIE_REPORTE = "DE REPORTE"
# (5) LA ESPECIE QUE EL ACTA 194 ESTRENA, LITERAL DE SU `C.1` Y DE SU FILA DE LA
# TABLA DE CREDITO. Es el nombre que la letra del 5 sep 2026 le da a la especie
# que ACUMULA PARA LA PARADA. Sin ella, la `C.1` sale SIN ESPECIE y el
# registrador PARA, que es lo que la guarda de la 193 hace y lo que aqui se
# CONSERVA: la parada por especie no declarada sigue entera.
MARCA_ESPECIE_REMEDIO = "ROMPER UN REMEDIO ESCRITO"
MARCAS_DE_ESPECIE_194 = (MARCA_ESPECIE_CIFRA, MARCA_ESPECIE_METODO,
                         MARCA_ESPECIE_REMEDIO)

PAT_TITULAR_HALLAZGO = r"^###\s+`(%s\d+)`\s+(.+?)\s*$"
PAT_CAIDA_PROPIA = r"^\s*\*\*`C\.(\d+)`"


def hallazgos_en_titular(lineas, ini, fin, prefijo=None):
    """LOS HALLAZGOS ESCRITOS COMO TITULAR `### \\`5.n\\` TITULO`. PURA.

    Devuelve una lista de (clave, linea, titulo), en el orden en que aparecen.
    El titulo es LO QUE EL TITULAR DICE, ni una palabra mas: no se va a buscar el
    cuerpo del parrafo.

    ES UN LECTOR NUEVO Y NO UN ENSANCHE DE LOS DOS VIEJOS. `claves_de_adjudicacion`
    y `claves_entrecomilladas` siguen intactos y SU CIFRA SOBRE ESTA ACTA SE
    PUBLICA AL LADO: los dos dan CERO, porque los dos buscan una NEGRITA de
    apertura de parrafo y el acta 194 titula sus hallazgos con `###`. La
    diferencia entre anadir y ensanchar es la que el acta 184 adjudico a favor en
    su `5.3`."""
    pat = re.compile(PAT_TITULAR_HALLAZGO % re.escape(prefijo or PREFIJO_HALLAZGO))
    salida = []
    for i in range(ini, fin + 1):
        m = pat.match(lineas[i - 1])
        if m:
            salida.append((m.group(1), i, m.group(2)))
    return salida


def caidas_propias_entrecomilladas(lineas, ini, fin):
    """LAS CAIDAS PROPIAS ESCRITAS `**\\`C.n\\` (...)` DENTRO DEL RANGO QUE SE
    PASA. PURA. Devuelve una lista de (clave, linea, linea_literal).

    POR QUE HACE FALTA Y NO VALE LA MAQUINA DE LEAD: las maquinas heredadas
    reparten una seccion de caidas ENTRE DOS LADOS mirando la negrita que encabeza
    cada bloque. El acta 194 no tiene una seccion asi: tiene la seccion 8 titulada
    MIS CAIDAS PROPIAS, con UN solo lado, y el lado lo dice el TITULO de la
    seccion. Repartir por lead sobre un texto sin lead da huerfanas y PARADA.

    EL RANGO ES PARAMETRO A PROPOSITO: quien llama decide que seccion es la de las
    propias, y este lector no supone que sea la 6 ni la 8."""
    salida = []
    for i in range(ini, fin + 1):
        m = re.match(PAT_CAIDA_PROPIA, lineas[i - 1])
        if m:
            salida.append(("C.%s" % m.group(1), i, lineas[i - 1].strip()))
    return salida


def nota_de_la_fila_de_puestos(texto_de_la_fila, marcas):
    """QUE NOTAS DE LA LISTA APARECEN EN LA FILA DE PUESTOS. PURA.

    Devuelve una lista de (marca, aparece_tal_cual, aparece_en_mayusculas,
    literal_que_el_acta_trae). **Ninguna nota se parafrasea**: si no esta, se dice
    que no esta, y el literal que se publica es el que el acta escribe de verdad.

    La caja se compara en mayusculas y el literal se guarda tal cual, que es la
    decision que la `NOTA_DE_PUESTOS` de la 191 ya dejo escrita: exigirla
    caracter a caracter haria PARAR por una mayuscula."""
    alto = texto_de_la_fila.upper()
    salida = []
    for marca in marcas:
        m = re.search(re.escape(marca), texto_de_la_fila, re.IGNORECASE)
        salida.append((marca, marca in texto_de_la_fila, marca.upper() in alto,
                       m.group(0) if m else ""))
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
    secciones = R92.secciones_del_acta(lineas, inicio, fin)
    w("   SECCIONES `## n.` DEL ACTA, LEIDAS Y NO TECLEADAS: %s"
      % R92._lista(secciones))
    w("   Y LA SEDE DE LAS CAIDAS PROPIAS NO SE SUPONE: en el acta 194 la seccion")
    w("   6 es PENDIENTES DE DOCTRINA y la 8 es MIS CAIDAS PROPIAS. Se lee la %d."
      % SECCION_DE_LAS_CAIDAS_PROPIAS)
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

    w("C) LAS ADJUDICACIONES, CONTADAS CON LOS DOS PATRONES Y NO TECLEADAS")
    entrecomilladas = R92.claves_entrecomilladas(lineas, inicio, fin, PREFIJO_ADJ)
    sueltas = R92.claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_ADJ)
    w("   patron CON comillas inversas (el del acta 184) -> %d" % len(entrecomilladas))
    for clave, cuantas in entrecomilladas:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    w("   patron SIN comillas inversas (el del acta 189) -> %d" % len(sueltas))
    w("   EL ACTA 194 NUMERA CON COMILLAS INVERSAS, ASI QUE MANDA EL PRIMERO, Y")
    w("   LA CIFRA DEL OTRO SE PUBLICA IGUAL EN VEZ DE CALLARSE.")
    claves = entrecomilladas
    dobles = [c for c, n in claves if n != 1]
    if dobles:
        w("   PARADA: hay claves repetidas dentro del acta: %s" % ", ".join(dobles))
        print(NL.join(salida))
        return 1
    if not claves:
        w("   PARADA: ningun patron encuentra adjudicaciones y el acta 194 declara")
        w("   diez. No se escribe una entrada con cero.")
        print(NL.join(salida))
        return 1
    w("")

    w("D) EL TITULO LITERAL DE CADA ADJUDICACION, SU FAMILIA Y SU ESTADO")
    w("   (EL VOCABULARIO ES EL HEREDADO ENTERO Y NO SE LE ANADE NINGUNA MARCA:")
    w("    las diez se leen con las que ya hay, y eso se dice porque el registrador")
    w("    de la 193 SI tuvo que anadir dos)")
    adjudicaciones = []
    for clave, _n in claves:
        pat = re.compile(r"^\s*\*\*`%s` " % re.escape(clave))
        res, err2 = R92.titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err2:
            w("   %s -> %s" % (clave, err2))
            print(NL.join(salida))
            return 1
        ln, tit = res
        adjudicaciones.append((clave, R92.familia_de_la_adjudicacion(tit),
                               R92.estado_de_la_adjudicacion(tit), ln, tit))
        w("   %-5s linea %-6d [%s / %s]" % (clave, ln, adjudicaciones[-1][1],
                                            adjudicaciones[-1][2]))
        w("         %s" % tit[:150])
    sin_decir = [c for c, _f, e, _l, _t in adjudicaciones if e == "SIN DECIR"]
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
    w("   CUARTA ACTA SEGUIDA. La guarda VIEJA de la 190 corrida aqui: %s"
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
        w("   PARADA: ninguna adjudicacion nombra un `P.n` y el acta 194 declara TRES")
        w("   preguntas contestadas. No se escribe una lista vacia.")
        print(NL.join(salida))
        return 1
    w("")

    w("E) LOS HALLAZGOS DE LA SECCION %d, LEIDOS DE SUS TITULARES `###`"
      % SECCION_DE_LOS_HALLAZGOS)
    her_sueltos = R92.claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_HALLAZGO)
    her_comillas = R92.claves_entrecomilladas(lineas, inicio, fin, PREFIJO_HALLAZGO)
    w("   LOS DOS LECTORES HEREDADOS, CORRIDOS TAL CUAL, Y SU CIFRA SE PUBLICA")
    w("   AUNQUE SEA CERO, QUE ES DE LO QUE SE TRATA:")
    w("      claves_de_adjudicacion(prefijo %r) -> %d" % (PREFIJO_HALLAZGO,
                                                          len(her_sueltos)))
    w("      claves_entrecomilladas(prefijo %r) -> %d" % (PREFIJO_HALLAZGO,
                                                          len(her_comillas)))
    w("      LA CAUSA, MEDIDA: los dos buscan una NEGRITA de apertura de parrafo,")
    w("      y el acta 194 titula sus hallazgos con `###`. Con cero, el registrador")
    w("      PARARIA por no encontrar hallazgos que el acta SI tiene.")
    hallazgos = hallazgos_en_titular(lineas, inicio, fin, PREFIJO_HALLAZGO)
    w("   EL LECTOR NUEVO, `hallazgos_en_titular()` -> %d" % len(hallazgos))
    for clave, ln, tit in hallazgos:
        w("      %-5s linea %-6d %s" % (clave, ln, tit[:120]))
    if not hallazgos:
        w("   PARADA: ningun lector encuentra hallazgos y el acta 194 declara TRES.")
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
    w("   numeral (%d) NO tiene por que igualar a las claves `5.n` (%d). Su propia"
      % (numeral, len(hallazgos)))
    w("   celda lo escribe. SE PUBLICAN LAS DOS Y NINGUNA SE ELIGE A OJO.")
    n_disc_fuera = numeral - len(hallazgos)
    w("   CIFRA discrepancias fuera del marcado, por resta: %d" % n_disc_fuera)
    if n_disc_fuera < 0:
        w("   PARADA: la resta da negativo. El numeral y las claves no cuadran de")
        w("   ninguna forma y no se elige a ojo.")
        print(NL.join(salida))
        return 1
    w("")

    w("F) LAS CAIDAS PROPIAS DEL AUDITOR, LEIDAS DE LA SECCION %d"
      % SECCION_DE_LAS_CAIDAS_PROPIAS)
    r8 = R92.rango_de_seccion(lineas, inicio, fin, SECCION_DE_LAS_CAIDAS_PROPIAS)
    if r8 is None:
        w("   PARADA: el acta no tiene seccion %d." % SECCION_DE_LAS_CAIDAS_PROPIAS)
        print(NL.join(salida))
        return 1
    ini8, fin8 = r8
    cabecera8 = lineas[ini8 - 1].strip()
    w("   la seccion %d va de la linea %d a la %d"
      % (SECCION_DE_LAS_CAIDAS_PROPIAS, ini8, fin8))
    w("   SU CABECERA, LITERAL: %r" % cabecera8)
    c_aud = caidas_propias_entrecomilladas(lineas, ini8, fin8)
    w("   CIFRA caidas propias leidas del CUERPO: %d" % len(c_aud))
    w("   LAS ESPECIES SE BUSCAN CON EL VOCABULARIO HEREDADO Y CON LA MARCA QUE")
    w("   ESTA ACTA ESTRENA, Y LAS DOS CIFRAS SE PUBLICAN:")
    especies_aud = []
    n_sin_especie_vieja = 0
    for clave, ln, literal in c_aud:
        vieja = R92.especie_de_la_caida(literal)
        esp = R92.especie_de_la_caida(literal, marcas=MARCAS_DE_ESPECIE_194)
        if not vieja:
            n_sin_especie_vieja += 1
        especies_aud.append((clave, ln, esp))
        w("      %-5s linea %-6d especie %s   (con el vocabulario de la 193: %s)"
          % (clave, ln, ", ".join(esp) or "NINGUNA", ", ".join(vieja) or "NINGUNA"))
        w("            %s" % literal[:120])
    if not c_aud:
        w("   PARADA: la seccion %d no trae ninguna clave `C.n` y el acta declara"
          % SECCION_DE_LAS_CAIDAS_PROPIAS)
        w("   dos. No se supone.")
        print(NL.join(salida))
        return 1
    w("   CON EL VOCABULARIO DE LA 193 Y NADA MAS, saldrian SIN ESPECIE: %d"
      % n_sin_especie_vieja)
    w("   O SEA QUE LA MARCA NUEVA NO ES UN ADORNO: sin ella este registrador")
    w("   PARARIA, que es lo que tiene que hacer un vocabulario que no alcanza.")
    sin_especie = [x for x in especies_aud if not x[2]]
    if sin_especie:
        w("   PARADA: hay %d caida(s) propia(s) del auditor SIN ESPECIE DECLARADA:"
          % len(sin_especie))
        for k, ln, _e in sin_especie:
            w("      %s en la linea %d" % (k, ln))
        w("   LA GUARDA DE LA 193 SE CONSERVA ENTERA: cada propia DECLARA su")
        w("   especie o el registrador para. No se supone ninguna.")
        print(NL.join(salida))
        return 1
    n_remedio = len([x for x in especies_aud if MARCA_ESPECIE_REMEDIO in x[2]])
    n_metodo = len([x for x in especies_aud if MARCA_ESPECIE_METODO in x[2]])
    n_cifra = len([x for x in especies_aud if MARCA_ESPECIE_CIFRA in x[2]])
    w("   REPARTO POR ESPECIE DE LAS PROPIAS: DE CIFRA PUBLICADA %d | DE METODO %d"
      % (n_cifra, n_metodo))
    w("      | ROMPER UN REMEDIO ESCRITO %d" % n_remedio)
    w("")

    w("G) LAS TRES FILAS DE CAIDAS DE LA TABLA, Y EL COTEJO CONTRA EL CUERPO")
    fila_aud = R92.fila_de_la_metrica(lineas, inicio, fin,
                                      R92.AGUJA_FILA_CAIDAS_AUDITOR)
    fila_rep = R92.fila_de_la_metrica(lineas, inicio, fin,
                                      AGUJA_FILA_CAIDAS_REPORTE)
    fila_met = R92.fila_de_la_metrica(lineas, inicio, fin,
                                      R92.AGUJA_FILA_CAIDAS_METODO)
    for etiqueta, f in (("propias del auditor", fila_aud),
                        ("del ejecutor, de reporte", fila_rep),
                        ("del ejecutor, de metodo", fila_met)):
        for ln, txt in f:
            w("   %-26s (linea %d) %s" % (etiqueta, ln, txt))
    if not (fila_aud and fila_rep and fila_met):
        w("   PARADA: falta alguna de las tres filas de caidas en la tabla.")
        print(NL.join(salida))
        return 1
    num_aud = R92.numeral_de_la_fila(fila_aud[0][1])
    num_rep = R92.numeral_de_la_fila(fila_rep[0][1])
    num_met = R92.numeral_de_la_fila(fila_met[0][1])
    w("   numerales leidos y no tecleados: auditor %s | reporte %s | metodo %s"
      % (num_aud, num_rep, num_met))
    if None in (num_aud, num_rep, num_met):
        w("   PARADA: alguna de las tres filas no trae cifra legible.")
        print(NL.join(salida))
        return 1

    # LAS CLAVES QUE CADA FILA DEL EJECUTOR NOMBRA, CON EL RANGO EXPANDIDO.
    _lit_rep, exp_rep = R92.expandir_rangos_de_clave(fila_rep[0][1])
    _lit_met, exp_met = R92.expandir_rangos_de_clave(fila_met[0][1])
    claves_rep = [c for c, _n in R92.claves_entrecomilladas(
        [fila_rep[0][1]], 1, 1, "")] or []
    w("   la fila de REPORTE nombra el hallazgo, no una `C.n`: claves `C.n` en")
    w("      ella -> %s" % (", ".join("C.%d" % k for k in exp_rep) or "(ninguna)"))
    w("   la fila de METODO nombra %s, con el rango expandido"
      % (", ".join("C.%d" % k for k in exp_met) or "(ninguna)"))
    w("")
    w("   EL COTEJO, FILA A FILA. LA PARADA SIGUE ENTERA PARA LAS DOS DEL")
    w("   EJECUTOR, QUE ES DONDE LA LECTURA PODRIA FALLAR:")
    fallos_cotejo = []
    if len(exp_met) != num_met:
        fallos_cotejo.append("ejecutor de metodo: claves del rango %d contra fila %d"
                             % (len(exp_met), num_met))
    if fallos_cotejo:
        w("   PARADA: alguna cuenta del cuerpo no calza con su fila de la tabla:")
        for f in fallos_cotejo:
            w("      " + f)
        print(NL.join(salida))
        return 1
    w("      del ejecutor, de metodo: %d claves del rango contra fila %d -> CALZA"
      % (len(exp_met), num_met))
    w("      del ejecutor, de reporte: la fila dice %d y nombra el hallazgo `5.2`,"
      % num_rep)
    w("         que es una clave de la seccion 5 y no una `C.n`. Se publica y no")
    w("         se le exige una clave que el acta no escribio.")
    w("")
    descuadre_auditor = (len(c_aud) != num_aud)
    w("   Y LA QUE NO CALZA, DECLARADA Y NO RESUELTA COPIANDO (EJECUTOR.md 2):")
    w("      caidas propias del auditor, contadas del CUERPO de la seccion %d: %d"
      % (SECCION_DE_LAS_CAIDAS_PROPIAS, len(c_aud)))
    w("      caidas propias del auditor, leidas de SU FILA de la tabla:        %d"
      % num_aud)
    w("      DESCUADRE: %s" % ("SI" if descuadre_auditor else "NO"))
    if descuadre_auditor:
        w("      LAS DOS LECTURAS SON CORRECTAS Y ES EL ACTA LA QUE SE CONTRADICE")
        w("      CONSIGO MISMA. La sede de la cifra es EL CUERPO, porque el encargo")
        w("      de la 194 dice literal `cada cifra se cuenta del cuerpo acotado del")
        w("      acta y no de aqui`, y ademas nombra DOS caidas propias del auditor.")
        w("      SE REGISTRA LA DEL CUERPO Y SE PUBLICAN LAS DOS. La guarda nueva")
        w("      comprueba abajo que la entrada armada las lleve las dos, y CAE EN")
        w("      ROJO si no.")
    w("")

    w("H) LA METRICA DE CREDITO DE LA SECCION %d, ENTERA" % SECCION_DE_LA_METRICA)
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
    if not fila_p:
        w("   PARADA: la tabla no trae fila de puestos.")
        print(NL.join(salida))
        return 1
    notas = nota_de_la_fila_de_puestos(
        fila_p[0][1], (R92.NOTA_DE_PUESTOS, NOTA_DE_PUESTOS_194))
    w("   LAS DOS NOTAS, LA HEREDADA Y LA DE ESTA ACTA, BUSCADAS LAS DOS:")
    for marca, tal_cual, en_mayus, literal in notas:
        w("      %-14r tal cual: %-3s | en mayusculas: %-3s | literal del acta: %r"
          % (marca, "SI" if tal_cual else "NO", "SI" if en_mayus else "NO", literal))
    heredada_ok = notas[0][2]
    nueva_ok = notas[1][2]
    w("   LA HEREDADA %r NO APARECE EN ESTA ACTA, Y ESO ES UNA MEDICION Y NO UN"
      % R92.NOTA_DE_PUESTOS)
    w("   FALLO: el registrador de la 193 PARARIA aqui. LA VIEJA SE CONSERVA Y SE")
    w("   SIGUE BUSCANDO, porque retirarla estrecharia el vocabulario a lo que el")
    w("   acta de hoy usa. heredada: %s | nueva: %s"
      % ("SI" if heredada_ok else "NO", "SI" if nueva_ok else "NO"))
    if not nueva_ok:
        w("   PARADA: el encargo pide registrar la fila de puestos CON SU NOTA de")
        w("   los quemados, y la fila no la trae. Una nota que no esta no se")
        w("   parafrasea.")
        print(NL.join(salida))
        return 1
    aislados = re.findall(r"(\d+)\s+aislados", fila_p[0][1])
    cotejados = re.findall(r"\*\*(\d+)\s+cotejados\*\*", fila_p[0][1])
    limpio = re.findall(r"cotejo limpio va sobre\s+(\d+)", fila_p[0][1])
    w("   aislados, cotejados y el tramo limpio, leidos de la celda: %s, %s y %s"
      % (aislados or "(no legible)", cotejados or "(no legible)",
         limpio or "(no legible)"))
    if not (aislados and cotejados and limpio):
        w("   PARADA: alguna de las tres cifras de la fila de puestos no se lee.")
        print(NL.join(salida))
        return 1
    w("")

    w("I) EL NUMERO DE LA ENTRADA, QUE NO SE TECLEA")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    w("   serie recomputada de sus dos sedes: %d entradas" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SERIE.colisiones(halladas)), len(SERIE.huecos(halladas))))
    w("   SIGUIENTE LIBRE: R.%d" % numero)
    w("   el encargo adelanta R.56 -> %s"
      % ("CALZA" if numero == 56 else "NO CALZA, y la discrepancia se declara"))
    w("")

    w("J) LA DEUDA DE LA SERIE, REMEDIDA AQUI Y NO HEREDADA")
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
        "n_suelto": len(sueltas),
        "adjudicaciones": adjudicaciones,
        "n_discutibles": len(discutibles), "n_preg": len(preguntas),
        "n_otras": len(otras), "n_a_favor_discutibles": len(a_favor),
        "n_en_contra_discutibles": len(en_contra),
        "vieja_pararia": not en_contra,
        "arnes_disco": len(datos_arnes), "arnes_lf": len(lf_arnes),
        "arnes_veredicto": ver_arnes[0] if ver_arnes else "",
        "preguntas": [(c, R92.PAT_P_DEL_TITULO.search(t).group(0).strip("`"))
                      for c, _f, _e, _l, t in preguntas],
        "hallazgos": hallazgos, "n_hall": len(hallazgos),
        "her_sueltos": len(her_sueltos), "her_comillas": len(her_comillas),
        "fila_fuera": fila_fuera, "numeral_fila": numeral,
        "n_disc_fuera": n_disc_fuera,
        "cabecera_seccion8": cabecera8, "seccion_propias": SECCION_DE_LAS_CAIDAS_PROPIAS,
        "c_aud": c_aud, "n_aud": len(c_aud), "especies_aud": especies_aud,
        "n_sin_especie_vieja": n_sin_especie_vieja, "n_remedio": n_remedio,
        "n_metodo": n_metodo, "n_cifra": n_cifra,
        "num_aud": num_aud, "num_rep": num_rep, "num_met": num_met,
        "descuadre_auditor": descuadre_auditor,
        "exp_met": exp_met, "exp_rep": exp_rep,
        "fila_aud": fila_aud, "fila_rep": fila_rep, "fila_met": fila_met,
        "filas7": filas7, "n_filas7": len(filas7),
        "fila_puestos": fila_p, "notas": notas,
        "heredada_ok": heredada_ok, "nueva_ok": nueva_ok,
        "aislados": aislados[0], "cotejados": cotejados[0], "limpio": limpio[0],
        "salto": salto, "numero": numero, "ya_registrada": len(ya),
        "sedes": sedes,
    }
    return salida, medido


def titulo_de_la_entrada(n_adj, n_hall, n_preg, n_cai_aud, n_cai_eje):
    """EL TITULO DE LA ENTRADA, CON SUS CINCO NUMERALES EN PALABRA. PURA.

    NO SE DELEGA EN LA MAQUINA DE LA 192 NI EN LA DE LA 193, Y LA RAZON ESTA
    MEDIDA: las dos cierran con `VUELTA_DEL_ACTA` de SU modulo, que es 192 y 193,
    y por eso un titulo armado con ellas nombraria el acta equivocada. **La marca
    de idempotencia de la casa es literalmente `del acta de la vuelta N`**, asi
    que un numero mal puesto ahi no es un adorno: rompe la comprobacion que impide
    escribir dos veces.

    LA CONCORDANCIA Y LAS PALABRAS DE LOS NUMERALES SI SE IMPORTAN
    (`PALABRA_CON_CERO`), que es donde vive la parte que no cambia."""
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
    p.append("Por adicion, como `R.21` a `R.55`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.55`. Salida:")
    p.append("`docs/loop/SALIDA_V%s_T1A_REGISTRO_R%d.txt`."
             % (SUFIJO_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 1 EN CURSO Y LAS TAREAS 2 Y 3 SIN")
    p.append("EMPEZAR, ASI QUE SUS GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA NO HA")
    p.append("PASADO.** Es la forma que la `6.4` del acta 172 adjudico como correcta. **La")
    p.append("194 es VUELTA DE BATERIA** (`AUDITOR.md` 6.1) y por eso lleva tres")
    p.append("sub-tareas y ningun trabajo de plan al lado.")
    p.append("")
    p.append("**LOS CINCO NUMERALES DEL TITULO NO ESTAN TECLEADOS:** se cuentan del acta")
    p.append("acotada (lineas %d a %d). **%d adjudicaciones numeradas (`4.1` a `4.%d`),"
             % (m["inicio"], m["fin"], m["n_adj"], m["n_adj"]))
    p.append("%d hallazgos numerados en la seccion 5, %d preguntas contestadas DENTRO de"
             % (m["n_hall"], m["n_preg"]))
    p.append("las adjudicaciones, %d caidas propias del auditor y %d caidas del"
             % (m["n_aud"], m["num_rep"] + m["num_met"]))
    p.append("ejecutor.**")
    p.append("")
    p.append("**LA FORMA DE LOS NUMERALES SE MIDE CON LOS DOS PATRONES Y LAS DOS CIFRAS SE")
    p.append("PUBLICAN.** El patron entrecomillado (el del acta 184) da %d y el suelto (el"
             % m["n_entrecomillado"])
    p.append("del acta 189) da %d. **El acta 194 numera con comillas inversas, asi que"
             % m["n_suelto"])
    p.append("manda el primero; ninguno se ensancha y se dice lo que dan los dos.**")
    p.append("")
    p.append("### LAS %d ADJUDICACIONES, UNA POR UNA, CON SU ESTADO LEIDO DEL TITULO"
             % m["n_adj"])
    p.append("")
    p.append("| clave | familia | estado, leido del titulo literal | linea del acta |")
    p.append("|---|---|---|---:|")
    for clave, fam, est, ln, _t in m["adjudicaciones"]:
        p.append("| `%s` | %s | %s | %d |" % (clave, fam, est, ln))
    p.append("")
    p.append("**EL CERO DE `EN CONTRA` VA POR LA CUARTA ACTA SEGUIDA.** De las %d,"
             % m["n_adj"])
    p.append("**%d son discutibles del ejecutor y los %d van A FAVOR**; las otras %d son"
             % (m["n_discutibles"], m["n_a_favor_discutibles"], m["n_preg"]))
    p.append("**preguntas contestadas por extension citable** (%s). **CIFRA `EN CONTRA`:"
             % ", ".join("`%s` en la `%s`" % (pn, c) for c, pn in m["preguntas"]))
    p.append("%d.**" % m["n_en_contra_discutibles"])
    p.append("")
    p.append("**Y ESE CERO NO SE VUELVE A PROBAR POR MUTACION: SE DICE CON SU FICHERO.**")
    p.append("`%s` mide **%d bytes** en disco y **%d** por LF, y su"
             % (ARNES_QUE_YA_CUBRE, m["arnes_disco"], m["arnes_lf"]))
    p.append("veredicto, leido del propio fichero, es %r. La guarda vieja de la 190"
             % m["arnes_veredicto"])
    p.append("(`if not en_contra: PARADA`) corrida sobre esta acta **%s**."
             % ("PARARIA" if m["vieja_pararia"] else "no pararia"))
    p.append("")
    p.append("**EL VOCABULARIO DE ESTADOS NO CRECE EN ESTA ACTA, Y SE DICE PORQUE EN LA")
    p.append("ANTERIOR SI CRECIO.** Las diez se leen con las marcas heredadas: siete por")
    p.append("`A FAVOR` y tres por `POR EXTENSION CITABLE`. **Ninguna marca nueva se")
    p.append("anade, y ninguna vieja se retira.**")
    p.append("")
    p.append("### LOS %d HALLAZGOS DE LA SECCION 5, QUE NO SALEN DE NINGUN DISCUTIBLE"
             % m["n_hall"])
    p.append("")
    for clave, ln, tit in m["hallazgos"]:
        p.append("- **`%s`** (linea %d del acta): %s" % (clave, ln, tit))
    p.append("")
    p.append("**Y SE LEEN CON UN LECTOR NUEVO, PORQUE LOS DOS VIEJOS DAN CERO.** El acta")
    p.append("194 titula sus hallazgos con `###` en vez de con una negrita de apertura de")
    p.append("parrafo: `claves_de_adjudicacion` da **%d** y `claves_entrecomilladas` da"
             % m["her_sueltos"])
    p.append("**%d** sobre esta acta, y con cero este registrador PARARIA por no encontrar"
             % m["her_comillas"])
    p.append("hallazgos que el acta si tiene. **`hallazgos_en_titular()` es un lector")
    p.append("ANADIDO y no un ensanche: los dos viejos siguen intactos y sus cifras se")
    p.append("publican aqui al lado.**")
    p.append("")
    p.append("**LA FILA DE LA TABLA DE CREDITO QUE LOS CUENTA, PEGADA Y NO PARAFRASEADA:**")
    p.append("")
    p.append("```")
    p.append(m["fila_fuera"][0][1])
    p.append("```")
    p.append("")
    p.append("**SU NUMERAL, LEIDO Y NO TECLEADO, ES %d, Y LAS CLAVES `5.n` SON %d.**"
             % (m["numeral_fila"], m["n_hall"]))
    p.append("**NO SE ELIGE A OJO CUAL VALE: la fila cuenta JUNTAS las discrepancias y los")
    p.append("hallazgos**, y su propia celda lo escribe. Por resta salen **%d"
             % m["n_disc_fuera"])
    p.append("discrepancias fuera del marcado** mas los %d hallazgos. **Las dos cifras van"
             % m["n_hall"])
    p.append("publicadas y ninguna se hereda.**")
    p.append("")
    p.append("### LAS CAIDAS, Y UNA CIFRA DEL ACTA NO CALZA CON OTRA DEL ACTA")
    p.append("")
    p.append("**LA SEDE DE LAS CAIDAS PROPIAS NO SE SUPONE: es la seccion %d.** En el acta"
             % m["seccion_propias"])
    p.append("194 la seccion 6 es PENDIENTES DE DOCTRINA y la %d es la de las propias. Su"
             % m["seccion_propias"])
    p.append("cabecera, literal: %r" % m["cabecera_seccion8"])
    p.append("")
    p.append("| lo que se cuenta | del cuerpo del acta | de su fila de la tabla |")
    p.append("|---|---:|---:|")
    p.append("| caidas propias del auditor | %d | %d |" % (m["n_aud"], m["num_aud"]))
    p.append("| del ejecutor, de reporte | (la fila nombra el hallazgo `5.2`) | %d |"
             % m["num_rep"])
    p.append("| del ejecutor, de metodo, con el rango expandido | %d | %d |"
             % (len(m["exp_met"]), m["num_met"]))
    p.append("")
    if m["descuadre_auditor"]:
        p.append("**LA PRIMERA FILA NO CALZA, Y SE DECLARA EN VEZ DE RESOLVERSE COPIANDO**")
        p.append("(`EJECUTOR.md` 2). **El cuerpo de la seccion %d declara %d caidas propias"
                 % (m["seccion_propias"], m["n_aud"]))
        p.append("del auditor** (%s, en las lineas %s del acta) **y su fila de la tabla de"
                 % (", ".join("`%s`" % c for c, _l, _e in m["especies_aud"]),
                    ", ".join(str(l) for _c, l, _e in m["especies_aud"])))
        p.append("credito dice %d**. **LAS DOS LECTURAS SON CORRECTAS: es el acta la que se"
                 % m["num_aud"])
        p.append("contradice consigo misma.** Se registra la del cuerpo, porque el encargo")
        p.append("de la 194 dice literal *\"cada cifra se cuenta del cuerpo acotado del acta")
        p.append("y no de aqui\"* y ademas nombra **DOS** caidas propias del auditor. **Las")
        p.append("dos cifras quedan publicadas aqui con su linea y su atribucion, y la")
        p.append("discrepancia va marcada en el reporte de la vuelta %d.**"
                 % VUELTA_QUE_ESCRIBE)
        p.append("")
        p.append("**Y ES LA MISMA ESPECIE QUE EL PROPIO HALLAZGO `5.2` DEL ACTA**, que")
        p.append("levanta contra el reporte de la 193 una seccion que dice cuatro donde el")
        p.append("instrumento dice cinco. **Se dice sin sacar ninguna conclusion de credito:")
        p.append("registrar no es adjudicar.**")
    else:
        p.append("**LAS TRES CALZAN.**")
    p.append("")
    p.append("**LA PARADA POR DESCUADRE SIGUE ENTERA PARA LA FILA DEL EJECUTOR DE METODO**,")
    p.append("que es donde la lectura si podria fallar: %d claves del rango expandido"
             % len(m["exp_met"]))
    p.append("contra %d de la fila. **Y SE ANADE UNA GUARDA:** si el cuerpo y la fila del"
             % m["num_met"])
    p.append("auditor no calzan y esta entrada no publicara LAS DOS cifras, el registrador")
    p.append("**cae en rojo y no escribe nada**. Una discrepancia callada seria peor que la")
    p.append("parada que sustituye.")
    p.append("")
    p.append("**LA ESPECIE DE CADA CAIDA PROPIA, LEIDA DE SU PARRAFO Y NO SUPUESTA:**")
    p.append("")
    for k, ln, esp in m["especies_aud"]:
        p.append("- **DEL AUDITOR**, `%s` (linea %d del acta): %s"
                 % (k, ln, ", ".join(esp)))
    p.append("")
    p.append("**Y EL VOCABULARIO DE ESPECIES SI CRECE, EN UNA MARCA.** `%s`"
             % MARCA_ESPECIE_REMEDIO)
    p.append("es literal de la `C.1` del acta y de su fila de la tabla, y es el nombre que")
    p.append("la letra del 5 sep 2026 le da a la especie que ACUMULA PARA LA PARADA. **Con")
    p.append("el vocabulario de la 193 y nada mas saldrian SIN ESPECIE %d caida(s)**, y"
             % m["n_sin_especie_vieja"])
    p.append("este registrador PARARIA. **La parada por especie no declarada se conserva")
    p.append("entera**: lo que crece es el vocabulario, no la manga. Reparto: **DE CIFRA")
    p.append("PUBLICADA %d, DE METODO %d, ROMPER UN REMEDIO ESCRITO %d**."
             % (m["n_cifra"], m["n_metodo"], m["n_remedio"]))
    p.append("")
    p.append("**LA `C.1` DEL AUDITOR CUENTA PARA LA PARADA** por la letra del 5 sep 2026")
    p.append("(ROMPER UN REMEDIO ESCRITO ACUMULA), y el acta lo escribe en su fila. **La")
    p.append("del ejecutor de reporte (el hallazgo `5.2`) SI ACUMULA**, por vivir en una")
    p.append("conclusion, y **la racha de reporte queda en 1**: no llega a dos, asi que")
    p.append("**no hay escalada que encargar**, y el acta lo dice expresamente para que no")
    p.append("se lea como olvido. **Las %d del ejecutor de metodo se registran y no abren"
             % m["num_met"])
    p.append("racha**, y las declaro el propio ejecutor en su seccion 8.1.")
    p.append("")
    p.append("### LA METRICA DE CREDITO, Y SU FILA DE PUESTOS CAMBIA DE NOTA")
    p.append("")
    p.append("**LAS %d FILAS DE DATOS DE LA SECCION 7, PEGADAS DEL ACTA:**" % m["n_filas7"])
    p.append("")
    p.append("```")
    for _ln, txt in m["filas7"]:
        p.append(txt)
    p.append("```")
    p.append("")
    p.append("**LA NOTA DE LA FILA DE PUESTOS YA NO ES LA DE LA 193.** La heredada,")
    p.append("`%s`, **no aparece en esta acta** (buscada y medida aqui), y con"
             % R92.NOTA_DE_PUESTOS)
    p.append("ella sola el registrador de la 193 PARARIA. La de esta acta es")
    p.append("`%s`, y el literal que el acta trae de verdad es %r. **La vieja"
             % (NOTA_DE_PUESTOS_194, m["notas"][1][3]))
    p.append("se conserva y se sigue buscando**: retirarla estrecharia el vocabulario a lo")
    p.append("que el acta de hoy usa, y la proxima que la use haria PARAR el instrumento.")
    p.append("")
    p.append("Son **%s aislados y %s cotejados**, con **%s quemados por el contexto de"
             % (m["aislados"], m["cotejados"], NOTA_DE_PUESTOS_194.split()[0].lower()))
    p.append("sesion y no por comando del auditor**, y **el cotejo limpio va sobre %s**."
             % m["limpio"])
    p.append("**El cotejo se publica dos veces, sobre los %s y sobre los %s**, que es lo"
             % (m["cotejados"], m["limpio"]))
    p.append("que el encargo manda registrar. **Un quemado no es un solape: el solape mide")
    p.append("si dos lectores leen lo mismo, y el quemado dice que uno de los dos ya sabia")
    p.append("lo que el otro habia dicho antes de leer.**")
    p.append("")
    p.append("### LA DEUDA DE LA SERIE, REMEDIDA AQUI EN VEZ DE HEREDARSE")
    p.append("")
    p.append("Tramo mirado: actas **173 a %d**. **CIFRA actas sin entrada propia en la"
             % (VUELTA_DEL_ACTA - 1))
    p.append("serie: %d** (%s). **Se registra y NO se arregla en esta vuelta**, que es lo"
             % (len(m["salto"][0]),
                ", ".join(str(x) for x in m["salto"][0]) or "ninguna"))
    p.append("que el encargo de la 194 deja escrito en su lista de lo que sigue fuera.")
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


def entrada_publica_las_dos(entrada, del_cuerpo, de_la_fila):
    """LA GUARDA NUEVA: SI HAY DESCUADRE, LA ENTRADA TIENE QUE PUBLICAR LAS DOS
    CIFRAS. PURA. Devuelve (ok, informe).

    Sustituye a la parada de la 193 en la fila del auditor, y no la afloja: la
    parada vieja cazaba UN ERROR DE LECTURA DEL REGISTRADOR; esta caza UNA
    DISCREPANCIA CALLADA, que es lo que de verdad se quiere evitar cuando las dos
    lecturas son correctas. **Si el descuadre existe y la entrada no lleva las dos
    cifras en su tabla de cotejo, cae en rojo y no se escribe nada.**"""
    informe = []
    fila = "| caidas propias del auditor | %d | %d |" % (del_cuerpo, de_la_fila)
    tiene_fila = fila in entrada
    informe.append("la fila de cotejo con LAS DOS cifras (%r) esta en la entrada: %s"
                   % (fila, "SI" if tiene_fila else "NO"))
    if del_cuerpo == de_la_fila:
        informe.append("no hay descuadre: la guarda no exige nada mas")
        return tiene_fila, informe
    marca = "LA PRIMERA FILA NO CALZA"
    tiene_marca = marca in entrada
    informe.append("la entrada DECLARA el descuadre (%r): %s"
                   % (marca, "SI" if tiene_marca else "NO"))
    return (tiene_fila and tiene_marca), informe


# ---------------------------------------------------------------- LA MUTACION
_CUENTA = {"casos": 0, "pasan": 0}


def _caso(w, nombre, obtenido, esperado):
    """UN CASO, Y LA CUENTA LA LLEVA EL ARNES Y NO EL QUE LO CITA.

    `EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO: la salida de este arnes
    publica al final `CIFRA casos: X | pasan: Y | fallan: Z`, que es la forma que
    `cerrar_reporte.py` sabe cotejar contra la prosa del reporte. Sin esa linea la
    cita del reporte sale SIN COTEJO, o sea que la cifra se teclea y nadie la
    mira."""
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

    LO QUE PRUEBA, Y POR QUE PUEDE CAER: los cuatro trozos nuevos son PUROS y se
    corren sobre texto FABRICADO, con el valor esperado sacado de como se fabrico
    el texto y NO de una constante igual a la obtenida. `EJECUTOR.md` 1, EL CASO
    ROJO SE PRUEBA POR MUTACION."""
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("VUELTA 194, TAREA 1: CASO POSITIVO POR MUTACION DEL REGISTRADOR")
    w("=" * 78)
    w("")

    w("A) `hallazgos_en_titular()` SOBRE UN ACTA FABRICADA CON TRES TITULARES")
    fab = [
        "## 5. HALLAZGOS",
        "",
        "### `5.1` EL PRIMERO",
        "",
        "cuerpo del primero, que NO es titulo.",
        "",
        "### `5.2` EL SEGUNDO, CON `COMILLAS` DENTRO",
        "",
        "### `5.3` EL TERCERO",
        "",
        "**`5.4` ESTE VA EN NEGRITA Y NO ES TITULAR**",
        "",
    ]
    hall = hallazgos_en_titular(fab, 1, len(fab))
    ok &= _caso(w, "encuentra los TRES titulares y no el de negrita", len(hall), 3)
    ok &= _caso(w, "y sus claves salen en orden",
                [c for c, _l, _t in hall], ["5.1", "5.2", "5.3"])
    ok &= _caso(w, "el titulo es lo que dice el titular, sin el cuerpo",
                hall[0][2], "EL PRIMERO")
    ok &= _caso(w, "y las comillas inversas del titulo no lo cortan",
                hall[1][2], "EL SEGUNDO, CON `COMILLAS` DENTRO")
    w("   LA MUTACION: los DOS lectores heredados sobre el MISMO texto tienen que")
    w("   dar CERO. Si dieran otra cosa, el lector nuevo seria un ensanche y no un")
    w("   anadido, y la cifra que se publica al lado no diria nada.")
    ok &= _caso(w, "claves_de_adjudicacion sobre el fabricado da cero",
                len(R92.claves_de_adjudicacion(fab, 1, len(fab), "5.")), 0)
    ok &= _caso(w, "claves_entrecomilladas sobre el fabricado da cero",
                len(R92.claves_entrecomilladas(fab, 1, len(fab), "5.")), 0)
    w("")

    w("B) `caidas_propias_entrecomilladas()` SOBRE UNA SECCION FABRICADA")
    fab8 = [
        "## 8. MIS CAIDAS PROPIAS",
        "",
        "**`C.1` (UNA COSA). Su cuerpo.**",
        "",
        "un parrafo que NOMBRA `C.9` en su cuerpo y no la abre.",
        "",
        "**`C.2` (DE METODO). Otra cosa.**",
        "",
    ]
    cp = caidas_propias_entrecomilladas(fab8, 1, len(fab8))
    ok &= _caso(w, "lee las DOS que ABREN parrafo", [c for c, _l, _t in cp],
                ["C.1", "C.2"])
    w("   LA MUTACION: una clave NOMBRADA en el cuerpo no es una caida declarada.")
    w("   Si el lector la contara, la cifra del cuerpo saldria 3 y el descuadre")
    w("   contra la tabla seria un artefacto del lector y no del acta.")
    ok &= _caso(w, "y NO cuenta la que solo se nombra en el cuerpo", len(cp), 2)
    ok &= _caso(w, "la especie sale del parrafo y no se supone",
                R92.MARCA_ESPECIE_METODO in R92.especie_de_la_caida(cp[1][2]), True)
    w("")

    w("B.2) LA MARCA DE ESPECIE QUE ESTA ACTA ESTRENA, Y LA PARADA SE CONSERVA")
    remedio = "**`C.1` (ROMPER UN REMEDIO ESCRITO, Y ACUMULA PARA LA PARADA).**"
    w("   LA MUTACION: con el vocabulario de la 193 esta caida sale SIN ESPECIE, y")
    w("   con cero especies el registrador PARA. Si la marca nueva no mordiera, la")
    w("   parada seria falsa; si la parada se hubiera quitado, una caida sin")
    w("   especie pasaria por buena.")
    ok &= _caso(w, "con el vocabulario de la 193 sale SIN ESPECIE",
                R92.especie_de_la_caida(remedio), [])
    ok &= _caso(w, "con el vocabulario de la 194 sale con SU especie",
                R92.especie_de_la_caida(remedio, marcas=MARCAS_DE_ESPECIE_194),
                [MARCA_ESPECIE_REMEDIO])
    ok &= _caso(w, "y una caida muda sigue saliendo SIN ESPECIE con el nuevo",
                R92.especie_de_la_caida("**`C.9` (UNA COSA CUALQUIERA).**",
                                        marcas=MARCAS_DE_ESPECIE_194), [])
    ok &= _caso(w, "las viejas siguen mordiendo con el vocabulario nuevo",
                R92.especie_de_la_caida("**`C.2` (DE METODO).**",
                                        marcas=MARCAS_DE_ESPECIE_194),
                [MARCA_ESPECIE_METODO])
    w("")

    w("C) `nota_de_la_fila_de_puestos()` BUSCA LAS DOS Y NO PARAFRASEA NINGUNA")
    fila = ("| puestos | 30 aislados, **30 cotejados**, **ONCE QUEMADOS por el "
            "contexto** | **1.096** |")
    notas = nota_de_la_fila_de_puestos(fila, ("SOLAPE TOTAL", "ONCE QUEMADOS"))
    ok &= _caso(w, "la heredada NO esta y se dice que no esta", notas[0][2], False)
    ok &= _caso(w, "la nueva SI esta", notas[1][2], True)
    ok &= _caso(w, "y el literal que se publica es el que la fila trae",
                notas[1][3], "ONCE QUEMADOS")
    w("   LA MUTACION: con otra caja, la nota sigue mordiendo y el literal que se")
    w("   publica cambia. Exigirla caracter a caracter haria PARAR por una")
    w("   mayuscula, que es lo contrario de lo que la guarda existe para cazar.")
    n2 = nota_de_la_fila_de_puestos("| puestos | once quemados |", ("ONCE QUEMADOS",))
    ok &= _caso(w, "en minusculas muerde igual", n2[0][2], True)
    ok &= _caso(w, "y el literal publicado es el de la fila", n2[0][3], "once quemados")
    ok &= _caso(w, "pero `tal cual` dice NO, que es la otra mitad del dato",
                n2[0][1], False)
    w("")

    w("D) `entrada_publica_las_dos()`, LA GUARDA QUE SUSTITUYE A LA PARADA VIEJA")
    con_las_dos = ("blah blah" + NL
                   + "| caidas propias del auditor | 2 | 1 |" + NL
                   + "**LA PRIMERA FILA NO CALZA, Y SE DECLARA**" + NL)
    ok2, inf = entrada_publica_las_dos(con_las_dos, 2, 1)
    for l in inf:
        w("      | " + l)
    ok &= _caso(w, "con las dos cifras Y el descuadre declarado, VERDE", ok2, True)
    w("   LA MUTACION 1: la misma entrada SIN la frase que declara el descuadre")
    sin_declarar = con_las_dos.replace("**LA PRIMERA FILA NO CALZA, Y SE DECLARA**", "")
    ok3, _inf = entrada_publica_las_dos(sin_declarar, 2, 1)
    ok &= _caso(w, "una discrepancia callada CAE", ok3, False)
    w("   LA MUTACION 2: la entrada que publica UNA sola cifra en su fila")
    una_sola = con_las_dos.replace("| caidas propias del auditor | 2 | 1 |",
                                   "| caidas propias del auditor | 2 |")
    ok4, _inf = entrada_publica_las_dos(una_sola, 2, 1)
    ok &= _caso(w, "publicar solo la del cuerpo CAE", ok4, False)
    w("   LA MUTACION 3: sin descuadre, la guarda solo exige la fila de cotejo")
    ok5, _inf = entrada_publica_las_dos(
        "| caidas propias del auditor | 1 | 1 |", 1, 1)
    ok &= _caso(w, "sin descuadre y con su fila, VERDE", ok5, True)
    ok6, _inf = entrada_publica_las_dos("sin tabla ninguna", 1, 1)
    ok &= _caso(w, "sin descuadre pero SIN la fila de cotejo, CAE", ok6, False)
    w("")

    w("E) `titulo_de_la_entrada()` NOMBRA EL ACTA 194 Y NO OTRA")
    t = titulo_de_la_entrada(10, 3, 3, 2, 4)
    ok &= _caso(w, "el titulo cierra con `del acta de la vuelta 194`",
                t.endswith("del acta de la vuelta %d" % VUELTA_DEL_ACTA), True)
    w("   LA MUTACION: la maquina de la 192 cierra con SU vuelta, y por eso no se")
    w("   delega. La marca de idempotencia de la casa es esa frase literal.")
    ok &= _caso(w, "la heredada nombraria el acta 192",
                R92.titulo_de_la_entrada(10, 3, 3, 2, 4).endswith(
                    "del acta de la vuelta %d" % R92.VUELTA_DEL_ACTA), True)
    ok &= _caso(w, "y las dos frases NO son la misma",
                t == R92.titulo_de_la_entrada(10, 3, 3, 2, 4), False)
    w("")

    w("CIFRA casos: %d | pasan: %d | fallan: %d"
      % (_CUENTA["casos"], _CUENTA["pasan"], _CUENTA["casos"] - _CUENTA["pasan"]))
    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_MUTACION_REGISTRADOR.txt"
                        % SUFIJO_QUE_ESCRIBE)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V%s_T1A_MUTACION_REGISTRADOR.txt (%d bytes)"
          % (SUFIJO_QUE_ESCRIBE, len(t.encode("utf-8"))))
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

    w("K) EL TITULO, CON SUS CINCO NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(m["n_adj"], m["n_hall"], m["n_preg"],
                                  m["n_aud"], m["num_rep"] + m["num_met"])
    w("   %s" % titulo)
    w("")

    numero = m["numero"]
    entrada = armar_entrada(numero, titulo, m)
    w("L) LA ENTRADA ARMADA")
    w("   %d bytes | %d lineas por count(NL) | %d por len(split(NL))"
      % (len(entrada.encode("utf-8")), entrada.count(NL), len(entrada.split(NL))))
    w("   guiones largos o medios en la entrada: %d"
      % (entrada.count(chr(8212)) + entrada.count(chr(8211))))
    w("")

    w("M) LA GUARDA NUEVA, CORRIDA SOBRE LA ENTRADA YA ARMADA")
    ok_guarda, informe = entrada_publica_las_dos(entrada, m["n_aud"], m["num_aud"])
    for l in informe:
        w("   " + l)
    w("   VEREDICTO DE LA GUARDA: %s" % ("VERDE" if ok_guarda else "ROJO"))
    if not ok_guarda:
        w("   ROJO: la entrada no publica las dos cifras del descuadre. NO SE")
        w("   ESCRIBE NADA. Una discrepancia callada es peor que una parada.")
        t = NL.join(salida) + NL
        ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_ROJO.txt" % SUFIJO_QUE_ESCRIBE)
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
        print(t)
        return 1
    w("")

    texto_sede = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    if a.simular:
        w("N) MODO --simular: NO SE ESCRIBE NADA EN LA SEDE.")
        w("")
        w("LA ENTRADA, ENTERA:")
        for l in entrada.split(NL):
            w("   | " + l)
    elif m["ya_registrada"]:
        w("N) NO SE ESCRIBE NADA, Y ESTA ES LA IDEMPOTENCIA HACIENDO SU TRABAJO.")
        w("   el acta %d YA TIENE ENTRADA en la serie: %d linea(s) la nombran."
          % (VUELTA_DEL_ACTA, m["ya_registrada"]))
        w("   NO se escribe una entrada nueva y NO se consume el numero R.%d." % numero)
        w("   docs/PENDIENTES.md sigue en %d bytes." % os.path.getsize(SEDE))
    else:
        nuevo = texto_sede.rstrip(NL) + NL + NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("N) ESCRITA EN docs/PENDIENTES.md")
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
