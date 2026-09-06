# -*- coding: utf-8 -*-
r"""vuelta195_tarea1a_registrar_acta195.py . EL ACTA 195 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA, Y ESTE REGISTRADOR SIGUE SIENDO IDEMPOTENTE.

LA MAQUINA SE IMPORTA Y NO SE COPIA. Todo lo generico (acotar el acta, leer
secciones, familia y estado de una adjudicacion, filas de la tabla de credito,
numerales, expansion de rangos, la serie) sale de
`vuelta192_tarea1a_registrar_acta192.py`; y `caidas_propias_entrecomilladas()` y
`nota_de_la_fila_de_puestos()` salen de `vuelta194_tarea1a_registrar_acta194.py`.
AQUI SOLO VIVE LO QUE EL ACTA 195 TIENE DISTINTO, y va dicho uno por uno para que
nadie tenga que adivinarlo:

  1. LOS HALLAZGOS VUELVEN A SER NEGRITAS Y NO TITULARES `###`. El acta 194
     escribia `### \`5.1\` TITULO` y por eso la 194 tuvo que ANADIR el lector
     `hallazgos_en_titular()`. El acta 195 escribe `**\`5.1\` TITULO...**`, o sea
     la forma vieja. **LOS TRES LECTORES SE CORREN Y LAS TRES CIFRAS SE PUBLICAN**,
     y el que manda aqui es `claves_entrecomilladas`. **El lector de la 194 NO se
     retira**: retirarlo estrecharia el vocabulario a la forma del acta de hoy, y
     la proxima que titule con `###` haria PARAR el instrumento.

  2. LAS CAIDAS PROPIAS DEL AUDITOR VIVEN EN LA SECCION 3. En el acta 194 estaban
     en la 8 y en la 192 en la 6. **LA SEDE NO SE SUPONE: se pasa por parametro y
     se publica su cabecera literal.**

  3. LA FILA DE CREDITO DE LAS CAIDAS PROPIAS DEL AUDITOR VIENE PARTIDA EN DOS, y
     esto NO es una rareza: **es el remedio del hallazgo `5.1` del propio acta 195
     aplicado por el auditor a su propia tabla en la vuelta en que lo levanta**.
     Una fila dice `caidas propias del auditor QUE ACUMULAN` y otra
     `caidas propias del auditor, TOTAL del cuerpo`. El registrador de la 194
     buscaba la aguja `caidas propias del auditor`, que aqui casa con LAS DOS, y
     **se quedaba con la primera en silencio**: registraria el 0 de las que
     acumulan como si fuera el total, que es exactamente la confusion que el
     hallazgo `5.1` denuncia. **Aqui se leen LAS DOS, se publican LAS DOS, y el
     cotejo contra el cuerpo se hace contra la del TOTAL**, que es la que mide lo
     mismo que el cuerpo.

  4. LA FILA DE PUESTOS NO TRAE `cotejo limpio va sobre N`, Y ESO NO ES UN FALLO:
     esta acta mide **CERO QUEMADOS**, asi que no hay dos cotejos que publicar y
     el acta no escribe el segundo. El registrador de la 194 PARARIA aqui, porque
     exigia las tres cifras. **La exigencia se hace condicional a que haya
     quemados, y las dos ramas se publican**: si hay quemados y falta el segundo
     cotejo, SIGUE PARANDO.

  5. LA NOTA DE LA FILA DE PUESTOS ES `CERO QUEMADOS`. Las dos heredadas
     (`SOLAPE TOTAL` de la 191 y `ONCE QUEMADOS` de la 194) **se siguen buscando y
     sus cifras se publican**, salgan como salgan.

  6. SE ANADE LA FILA DE `caidas del ejecutor que ACUMULAN por cifra publicada`,
     que el encargo manda registrar expresamente (CERO CAIDAS DEL EJECUTOR, de
     cifra publicada Y de reporte). No se deduce de las otras: se lee.

TODA CIFRA SE CUENTA DEL CUERPO ACOTADO DEL ACTA Y NINGUNA DEL ENCARGO. Donde el
encargo publica una, se computa la propia y SE PUBLICAN LAS DOS.

EL NUMERO DE LA ENTRADA NO SE TECLEA: lo computa `serie_de_registros.py`
recomputando la serie de sus DOS sedes.

USO:
  python scripts/loop/vuelta195_tarea1a_registrar_acta195.py --simular
  python scripts/loop/vuelta195_tarea1a_registrar_acta195.py
  python scripts/loop/vuelta195_tarea1a_registrar_acta195.py --mutacion
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

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 195
VUELTA_QUE_ESCRIBE = 195
SUFIJO_QUE_ESCRIBE = "195"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "4."
PREFIJO_HALLAZGO = "5."
SECCION_DE_LOS_HALLAZGOS = 5
SECCION_DE_LAS_CAIDAS_PROPIAS = 3
SECCION_DE_LA_METRICA = 7

# LA NOTA DE LA FILA DE PUESTOS QUE ESTA ACTA ESTRENA, LITERAL DE SU CELDA. Las
# dos heredadas se siguen buscando y sus cifras se publican.
NOTA_DE_PUESTOS_195 = "CERO quemados"

# LAS AGUJAS DE LAS FILAS DE LA TABLA DE CREDITO. Las dos primeras son las dos
# mitades en que el acta 195 parte la fila de las propias del auditor, y son
# LITERALES DE SU TABLA: no se deducen ni se parafrasean.
AGUJA_FILA_AUD_ACUMULAN = "caidas propias del auditor QUE ACUMULAN"
AGUJA_FILA_AUD_TOTAL = "caidas propias del auditor, TOTAL del cuerpo"
AGUJA_FILA_CAIDAS_REPORTE = "caidas del ejecutor de reporte"
AGUJA_FILA_CAIDAS_CIFRA = "caidas del ejecutor que ACUMULAN por cifra publicada"

MARCA_ESPECIE_METODO = R92.MARCA_ESPECIE_METODO
MARCA_ESPECIE_CIFRA = R92.MARCA_ESPECIE_CIFRA
MARCA_ESPECIE_REMEDIO = R94.MARCA_ESPECIE_REMEDIO
MARCAS_DE_ESPECIE_195 = (MARCA_ESPECIE_CIFRA, MARCA_ESPECIE_METODO,
                         MARCA_ESPECIE_REMEDIO)

# EL ARNES DE LA 191 QUE YA CUBRE EL CERO DE `EN CONTRA`, NOMBRADO PARA MEDIRLO
# EN VEZ DE RE FABRICAR SU CASO. Es la QUINTA acta seguida con cero.
ARNES_QUE_YA_CUBRE = "docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt"


# LAS DOS MARCAS DE ESTADO QUE EL ACTA 195 ESTRENA, LITERALES DE SUS DOS
# PREGUNTAS Y NO PARAFRASEADAS. El acta 195 contesta la `P.1` con *"CONTESTADA, y
# la respuesta corrige a mi predecesor, no al ejecutor"* y la `P.3` con
# *"CONTESTADA, con las dos mitades"*, y NINGUNA de las doce marcas heredadas casa
# con ellas: las dos saldrian `SIN DECIR` y este registrador PARARIA.
#
# SE ANADEN, NO SE ENSANCHAN, que es la diferencia que el acta 184 adjudico a
# favor en su `5.3`: ninguna marca vieja se retira ni se recorta, y la cifra de
# cuantas saldrian SIN DECIR con el vocabulario heredado SE PUBLICA al lado.
MARCA_CORRIGE_AL_PREDECESOR = "LA RESPUESTA CORRIGE A MI PREDECESOR"
MARCA_DOS_MITADES = "CON LAS DOS MITADES"
MARCAS_NUEVAS_195 = (MARCA_CORRIGE_AL_PREDECESOR, MARCA_DOS_MITADES)


def estado_de_la_adjudicacion_195(titulo):
    """EL ESTADO DE UNA ADJUDICACION DEL ACTA 195, LEIDO DE SU TITULO. PURA.

    PRIMERO CORRE EL VOCABULARIO HEREDADO ENTERO (`R92.estado_de_la_adjudicacion`,
    que ya lleva doce marcas) y solo si ese devuelve `SIN DECIR` prueba las DOS de
    esta acta. Ese orden importa y va escrito: un titulo que diga `EN CONTRA`
    tiene que salir `EN CONTRA` aunque tambien traiga una de las nuevas.

    Si ninguna casa, sigue devolviendo `SIN DECIR` y quien llama PARA. **La parada
    por estado no legible se conserva entera: lo que crece es el vocabulario, no
    la manga.**"""
    heredado = R92.estado_de_la_adjudicacion(titulo)
    if heredado != "SIN DECIR":
        return heredado
    alto = titulo.upper()
    if MARCA_CORRIGE_AL_PREDECESOR in alto:
        return "CONTESTADA, Y LA RESPUESTA CORRIGE AL PREDECESOR DEL AUDITOR"
    if MARCA_DOS_MITADES in alto:
        return "CONTESTADA CON LAS DOS MITADES: CORRIDA SI, VERDE NO"
    return "SIN DECIR"


def filas_de_las_propias(lineas, ini, fin, agujas=None):
    """LAS DOS MITADES DE LA FILA DE CAIDAS PROPIAS DEL AUDITOR. PURA salvo por
    recibir las lineas ya acotadas.

    Devuelve `{aguja: [(linea, texto)]}` para cada aguja que se le pase, SIN
    elegir ninguna. Quien llama decide cual coteja contra el cuerpo, y este
    fichero lo dice arriba: la del TOTAL, porque es la que mide lo mismo.

    POR QUE NO VALE LA MAQUINA TAL CUAL: `fila_de_la_metrica` con la aguja corta
    `caidas propias del auditor` casa con LAS DOS mitades, y quien la llamaba se
    quedaba con `[0]`, o sea con la de las que ACUMULAN. Sobre esta acta eso
    registraria **0** donde el cuerpo declara **1**, que es la confusion que el
    hallazgo `5.1` del acta denuncia. Aqui las dos se leen con SU aguja larga."""
    salida = {}
    for aguja in (agujas or (AGUJA_FILA_AUD_ACUMULAN, AGUJA_FILA_AUD_TOTAL)):
        salida[aguja] = R92.fila_de_la_metrica(lineas, ini, fin, aguja)
    return salida


def numeral_de_la_fila_195(texto_de_la_fila):
    """LA CIFRA DE LA SEGUNDA CELDA, TAMBIEN CUANDO LLEVA UNA PALABRA PEGADA.
    PURA. Devuelve el entero o `None`.

    POR QUE HACE FALTA, MEDIDO Y NO SUPUESTO: la fila de caidas de metodo del
    acta 195 escribe **`**0 nuevas**`**, y el lector heredado
    (`R91.numeral_de_la_fila`) busca `**<digitos>**` pegados o un numero al
    principio de la celda. Sobre `**0 nuevas**` devuelve `None`, y quien llama
    PARA por una fila que SI trae su cifra y solo la acompana de un adjetivo.

    SE ANADE Y NO SE ENSANCHA: el heredado corre PRIMERO y entero, y solo si
    devuelve `None` se prueba la forma con palabra. Asi ninguna fila que el
    heredado ya leia cambia de valor, y una celda de verdad muda sigue dando
    `None` y sigue haciendo PARAR."""
    heredado = R92.numeral_de_la_fila(texto_de_la_fila)
    if heredado is not None:
        return heredado
    celdas = [c.strip() for c in texto_de_la_fila.strip().strip("|").split("|")]
    if len(celdas) < 2:
        return None
    m = re.search(r"\*\*(\d+)\s+[^*]+\*\*", celdas[1])
    return int(m.group(1)) if m else None


def cifras_de_la_fila_de_puestos(texto_de_la_fila):
    """LAS CIFRAS QUE LA FILA DE PUESTOS TRAE, Y `None` EN LA QUE NO ESTE. PURA.

    Devuelve `(aislados, cotejados, quemados, limpio)`, cada uno el literal leido
    o `None`.

    `limpio` PUEDE FALTAR LEGITIMAMENTE, y por eso se devuelve `None` en vez de
    hacer caer a quien llama: si el acta mide CERO quemados no hay un segundo
    cotejo que publicar, asi que el acta no lo escribe. La exigencia vive en quien
    llama y es CONDICIONAL: solo se exige si los quemados no son cero."""
    aisl = re.search(r"(\d+)\s+aislados", texto_de_la_fila)
    cot = re.search(r"\*\*(\d+)\s+cotejados\*\*", texto_de_la_fila)
    quem = re.search(r"\*\*(\w+)\s+quemados\*\*", texto_de_la_fila, re.IGNORECASE)
    lim = re.search(r"cotejo limpio va sobre\s+(\d+)", texto_de_la_fila)
    return (aisl.group(1) if aisl else None,
            cot.group(1) if cot else None,
            quem.group(1) if quem else None,
            lim.group(1) if lim else None)


def quemados_son_cero(literal):
    """SI EL LITERAL DE LOS QUEMADOS SIGNIFICA CERO. PURA.

    Acepta el digito y la palabra, en cualquier caja, porque esta casa escribe las
    dos formas: la 194 escribio `ONCE QUEMADOS` y la 195 escribe `CERO quemados`.
    Devuelve `False` ante `None`, que es lo prudente: si no se pudo leer, NO se
    supone que sean cero, y entonces la exigencia del segundo cotejo se mantiene."""
    if literal is None:
        return False
    return literal.strip().lower() in ("0", "cero")


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
    w("   Y LA SEDE DE LAS CAIDAS PROPIAS NO SE SUPONE: en el acta 195 la seccion")
    w("   3 es MIS CAIDAS PROPIAS (en la 194 era la 8 y en la 192 la 6). Se lee")
    w("   la %d." % SECCION_DE_LAS_CAIDAS_PROPIAS)
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
    w("   EL ACTA 195 NUMERA CON COMILLAS INVERSAS, ASI QUE MANDA EL PRIMERO, Y")
    w("   LA CIFRA DEL OTRO SE PUBLICA IGUAL EN VEZ DE CALLARSE.")
    claves = entrecomilladas
    dobles = [c for c, n in claves if n != 1]
    if dobles:
        w("   PARADA: hay claves repetidas dentro del acta: %s" % ", ".join(dobles))
        print(NL.join(salida))
        return 1
    if not claves:
        w("   PARADA: ningun patron encuentra adjudicaciones y el acta 195 declara")
        w("   diez. No se escribe una entrada con cero.")
        print(NL.join(salida))
        return 1
    w("")

    w("D) EL TITULO LITERAL DE CADA ADJUDICACION, SU FAMILIA Y SU ESTADO")
    w("   (EL VOCABULARIO ES EL HEREDADO ENTERO Y NO SE LE ANADE NINGUNA MARCA)")
    adjudicaciones = []
    n_sin_decir_heredado = 0
    for clave, _n in claves:
        pat = re.compile(r"^\s*\*\*`%s` " % re.escape(clave))
        res, err2 = R92.titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err2:
            w("   %s -> %s" % (clave, err2))
            print(NL.join(salida))
            return 1
        ln, tit = res
        est_her = R92.estado_de_la_adjudicacion(tit)
        if est_her == "SIN DECIR":
            n_sin_decir_heredado += 1
        adjudicaciones.append((clave, R92.familia_de_la_adjudicacion(tit),
                               estado_de_la_adjudicacion_195(tit), ln, tit))
        w("   %-5s linea %-6d [%s / %s]" % (clave, ln, adjudicaciones[-1][1],
                                            adjudicaciones[-1][2]))
        w("         %s" % tit[:150])
    w("   EL VOCABULARIO DE ESTADOS CRECE EN DOS MARCAS, Y LA CIFRA QUE LO")
    w("   JUSTIFICA VA DELANTE: con el vocabulario HEREDADO y nada mas saldrian")
    w("   SIN DECIR %d adjudicacion(es), y este registrador PARARIA."
      % n_sin_decir_heredado)
    w("   LAS DOS MARCAS NUEVAS SON LITERALES DEL ACTA Y NO PARAFRASIS: %s"
      % ", ".join(repr(x) for x in MARCAS_NUEVAS_195))
    w("   SE ANADEN Y NO SE ENSANCHAN: ninguna vieja se retira ni se recorta.")
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
    w("   QUINTA ACTA SEGUIDA. La guarda VIEJA de la 190 corrida aqui: %s"
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
        w("   PARADA: ninguna adjudicacion nombra un `P.n` y el acta 195 declara")
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
    w("   EL ACTA 195 VUELVE A LA NEGRITA DE APERTURA DE PARRAFO, asi que aqui")
    w("   manda `claves_entrecomilladas` y el lector de la 194 da CERO. NO SE")
    w("   RETIRA NINGUNO: retirar el de la 194 estrecharia el vocabulario a la")
    w("   forma del acta de hoy, y la proxima que titule con `###` haria PARAR.")
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
        w("   PARADA: ningun lector encuentra hallazgos y el acta 195 declara TRES.")
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

    w("F) LAS CAIDAS PROPIAS DEL AUDITOR, LEIDAS DE LA SECCION %d"
      % SECCION_DE_LAS_CAIDAS_PROPIAS)
    r3 = R92.rango_de_seccion(lineas, inicio, fin, SECCION_DE_LAS_CAIDAS_PROPIAS)
    if r3 is None:
        w("   PARADA: el acta no tiene seccion %d." % SECCION_DE_LAS_CAIDAS_PROPIAS)
        print(NL.join(salida))
        return 1
    ini3, fin3 = r3
    cabecera3 = lineas[ini3 - 1].strip()
    w("   la seccion %d va de la linea %d a la %d"
      % (SECCION_DE_LAS_CAIDAS_PROPIAS, ini3, fin3))
    w("   SU CABECERA, LITERAL: %r" % cabecera3)
    c_aud = R94.caidas_propias_entrecomilladas(lineas, ini3, fin3)
    w("   CIFRA caidas propias leidas del CUERPO: %d" % len(c_aud))
    especies_aud = []
    n_sin_especie_vieja = 0
    for clave, ln, literal in c_aud:
        vieja = R92.especie_de_la_caida(literal)
        esp = R92.especie_de_la_caida(literal, marcas=MARCAS_DE_ESPECIE_195)
        if not vieja:
            n_sin_especie_vieja += 1
        especies_aud.append((clave, ln, esp))
        w("      %-5s linea %-6d especie %s   (con el vocabulario de la 193: %s)"
          % (clave, ln, ", ".join(esp) or "NINGUNA", ", ".join(vieja) or "NINGUNA"))
        w("            %s" % literal[:120])
    if not c_aud:
        w("   PARADA: la seccion %d no trae ninguna clave `C.n` y el acta declara"
          % SECCION_DE_LAS_CAIDAS_PROPIAS)
        w("   una. No se supone.")
        print(NL.join(salida))
        return 1
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

    w("G) LA FILA DE LAS PROPIAS VIENE PARTIDA EN DOS, Y LAS DOS SE LEEN")
    w("   NO ES UNA RAREZA: es el remedio del hallazgo `5.1` del propio acta 195")
    w("   aplicado por el auditor a SU MISMA tabla en la vuelta en que lo levanta.")
    w("   Y LA AGUJA CORTA DE LA 194 (%r) CASA CON LAS DOS: quien la usara se"
      % R92.AGUJA_FILA_CAIDAS_AUDITOR)
    corta = R92.fila_de_la_metrica(lineas, inicio, fin,
                                   R92.AGUJA_FILA_CAIDAS_AUDITOR)
    w("   quedaria con la primera EN SILENCIO. Medido aqui: la aguja corta da %d"
      % len(corta))
    w("   fila(s), y la primera es la de las que ACUMULAN.")
    partidas = filas_de_las_propias(lineas, inicio, fin)
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
    w("   EL COTEJO CONTRA EL CUERPO SE HACE CONTRA LA DEL TOTAL, que es la que")
    w("   mide lo mismo que el cuerpo: cuerpo %d contra fila %d -> %s"
      % (len(c_aud), num_aud_total,
         "CALZA" if len(c_aud) == num_aud_total else "NO CALZA"))
    if len(c_aud) != num_aud_total:
        w("   PARADA: el cuerpo y la fila del TOTAL no calzan, y aqui SI es error")
        w("   de lectura o de acta, no una fila que mide otra cosa. No se elige.")
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
        w("   LA DE CIFRA PUBLICADA LA MANDA REGISTRAR EL ENCARGO EXPRESAMENTE.")
        print(NL.join(salida))
        return 1
    her_rep = R92.numeral_de_la_fila(fila_rep[0][1])
    her_met = R92.numeral_de_la_fila(fila_met[0][1])
    her_cif = R92.numeral_de_la_fila(fila_cif[0][1])
    num_rep = numeral_de_la_fila_195(fila_rep[0][1])
    num_met = numeral_de_la_fila_195(fila_met[0][1])
    num_cif = numeral_de_la_fila_195(fila_cif[0][1])
    w("   numerales con el lector HEREDADO: reporte %s | metodo %s | cifra %s"
      % (her_rep, her_met, her_cif))
    w("   numerales con el lector de esta acta: reporte %s | metodo %s | cifra %s"
      % (num_rep, num_met, num_cif))
    w("   LA DIFERENCIA ESTA EN LA FILA DE METODO, QUE ESCRIBE `**0 nuevas**`: el")
    w("   heredado busca `**<digitos>**` pegados y devuelve None sobre ella, y")
    w("   quien llama PARARIA por una fila que SI trae su cifra y solo la")
    w("   acompana de un adjetivo. SE ANADE Y NO SE ENSANCHA: el heredado corre")
    w("   primero y entero, y una celda de verdad muda sigue dando None.")
    if None in (num_rep, num_met, num_cif):
        w("   PARADA: alguna de las tres filas no trae cifra legible.")
        print(NL.join(salida))
        return 1
    _lit_met, exp_met = R92.expandir_rangos_de_clave(fila_met[0][1])
    w("   la fila de METODO nombra %s, con el rango expandido"
      % (", ".join("C.%d" % k for k in exp_met) or "(ninguna)"))
    w("   LA PARADA POR DESCUADRE SIGUE ENTERA PARA LA FILA DE METODO:")
    if len(exp_met) != num_met:
        w("   PARADA: claves del rango %d contra fila %d." % (len(exp_met), num_met))
        print(NL.join(salida))
        return 1
    w("      %d claves del rango contra fila %d -> CALZA" % (len(exp_met), num_met))
    w("   LAS TRES DEL EJECUTOR SUMAN %d, Y ESA ES LA CIFRA QUE VA AL TITULO."
      % (num_rep + num_met + num_cif))
    w("   LA RACHA DE REPORTE, LEIDA DE LA CELDA DERECHA DE SU FILA Y NO SUPUESTA:")
    m_racha = re.search(r"racha de reporte:\s*(\d+)", fila_rep[0][1])
    racha_rep = m_racha.group(1) if m_racha else None
    w("      %s" % (("racha de reporte: %s" % racha_rep) if racha_rep
                    else "(la celda no publica la racha)"))
    if racha_rep is None:
        w("   PARADA: el encargo manda registrar que la racha de reporte VUELVE A")
        w("   CERO, y la fila no la publica. No se teclea una.")
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
                       NOTA_DE_PUESTOS_195))
    w("   LAS TRES NOTAS, LAS DOS HEREDADAS Y LA DE ESTA ACTA, BUSCADAS LAS TRES:")
    for marca, tal_cual, en_mayus, literal in notas:
        w("      %-16r tal cual: %-3s | en mayusculas: %-3s | literal: %r"
          % (marca, "SI" if tal_cual else "NO", "SI" if en_mayus else "NO", literal))
    nueva_ok = notas[2][2]
    if not nueva_ok:
        w("   PARADA: el encargo pide registrar la fila de puestos CON SU NOTA de")
        w("   los quemados, y la fila no la trae. Una nota que no esta no se")
        w("   parafrasea.")
        print(NL.join(salida))
        return 1
    aisl, cot, quem, limpio = cifras_de_la_fila_de_puestos(fila_p[0][1])
    w("   aislados, cotejados, quemados y el tramo limpio, leidos de la celda:")
    w("      %r, %r, %r y %r" % (aisl, cot, quem, limpio))
    if not (aisl and cot and quem):
        w("   PARADA: alguna de las tres cifras obligatorias no se lee.")
        print(NL.join(salida))
        return 1
    cero_quemados = quemados_son_cero(quem)
    w("   LOS QUEMADOS SON CERO: %s" % ("SI" if cero_quemados else "NO"))
    w("   Y POR ESO LA EXIGENCIA DEL SEGUNDO COTEJO ES CONDICIONAL, Y SE DICE:")
    w("   el registrador de la 194 exigia SIEMPRE `cotejo limpio va sobre N`, y")
    w("   sobre esta acta PARARIA. Con CERO quemados no hay dos cotejos que")
    w("   publicar, asi que el acta no escribe el segundo, Y ESO ES CORRECTO.")
    if not cero_quemados and limpio is None:
        w("   PARADA: hay quemados y la fila no publica el cotejo limpio. La")
        w("   exigencia SIGUE ENTERA en esa rama y no se afloja.")
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
    w("   el encargo adelanta R.57 -> %s"
      % ("CALZA" if numero == 57 else "NO CALZA, y la discrepancia se declara"))
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
        "n_suelto": len(sueltas),
        "adjudicaciones": adjudicaciones,
        "n_discutibles": len(discutibles), "n_preg": len(preguntas),
        "n_otras": len(otras), "n_a_favor_discutibles": len(a_favor),
        "n_en_contra_discutibles": len(en_contra),
        "vieja_pararia": not en_contra,
        "n_sin_decir_heredado": n_sin_decir_heredado,
        "arnes_disco": len(datos_arnes), "arnes_lf": len(lf_arnes),
        "arnes_veredicto": ver_arnes[0] if ver_arnes else "",
        "preguntas": [(c, R92.PAT_P_DEL_TITULO.search(t).group(0).strip("`"))
                      for c, _f, _e, _l, t in preguntas],
        "hallazgos": hallazgos, "n_hall": len(hallazgos),
        "her_sueltos": len(her_sueltos), "her_comillas": len(her_comillas),
        "n_titulares": len(titulares),
        "fila_fuera": fila_fuera, "numeral_fila": numeral,
        "n_disc_fuera": n_disc_fuera,
        "cabecera_seccion3": cabecera3,
        "seccion_propias": SECCION_DE_LAS_CAIDAS_PROPIAS,
        "c_aud": c_aud, "n_aud": len(c_aud), "especies_aud": especies_aud,
        "n_sin_especie_vieja": n_sin_especie_vieja, "n_remedio": n_remedio,
        "n_metodo": n_metodo, "n_cifra": n_cifra,
        "n_corta": len(corta), "partidas": partidas,
        "num_aud_acum": num_aud_acum, "num_aud_total": num_aud_total,
        "num_rep": num_rep, "num_met": num_met, "num_cif": num_cif,
        "racha_rep": racha_rep, "exp_met": exp_met,
        "her_met": her_met,
        "fila_rep": fila_rep, "fila_met": fila_met, "fila_cif": fila_cif,
        "filas7": filas7, "n_filas7": len(filas7),
        "fila_puestos": fila_p, "notas": notas,
        "aislados": aisl, "cotejados": cot, "quemados": quem, "limpio": limpio,
        "cero_quemados": cero_quemados,
        "salto": salto, "numero": numero, "ya_registrada": len(ya),
        "sedes": sedes,
    }
    return salida, medido


def titulo_de_la_entrada(n_adj, n_hall, n_preg, n_cai_aud, n_cai_eje):
    """EL TITULO DE LA ENTRADA, CON SUS CINCO NUMERALES EN PALABRA. PURA.

    NO SE DELEGA EN LA MAQUINA DE LA 192 NI EN LA DE LA 194, Y LA RAZON ESTA
    MEDIDA: las dos cierran con `VUELTA_DEL_ACTA` de SU modulo, que es 192 y 194,
    y por eso un titulo armado con ellas nombraria el acta equivocada. La marca de
    idempotencia de la casa es literalmente `del acta de la vuelta N`, asi que un
    numero mal puesto ahi rompe la comprobacion que impide escribir dos veces.

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
    p.append("Por adicion, como `R.21` a `R.56`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.56`. Salida:")
    p.append("`docs/loop/SALIDA_V%s_T1A_REGISTRO_R%d.txt`."
             % (SUFIJO_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 2 YA CERRADA Y LAS TAREAS 3 Y 4 SIN")
    p.append("EMPEZAR, ASI QUE SUS GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA NO HA")
    p.append("PASADO.** Es la forma que la `6.4` del acta 172 adjudico como correcta. **Y")
    p.append("el orden va declarado en vez de dejarse:** la TAREA 2 fue antes que esta")
    p.append("porque la seccion 2 del acta 195 publica las clases del auditor sobre los")
    p.append("mismos 30 puestos que el ejecutor tenia que leer a ciegas, y registrar el")
    p.append("acta antes habria quemado la ciega. **La 195 NO es vuelta de bateria**")
    p.append("(`AUDITOR.md` 6.1: la 194 la corrio entera y la proxima cae en la 199).")
    p.append("")
    p.append("**LOS CINCO NUMERALES DEL TITULO NO ESTAN TECLEADOS:** se cuentan del acta")
    p.append("acotada (lineas %d a %d). **%d adjudicaciones numeradas (`4.1` a `4.%d`),"
             % (m["inicio"], m["fin"], m["n_adj"], m["n_adj"]))
    p.append("%d hallazgos numerados en la seccion 5, %d preguntas contestadas DENTRO de"
             % (m["n_hall"], m["n_preg"]))
    p.append("las adjudicaciones, %d caida propia del auditor y %d caidas del ejecutor.**"
             % (m["n_aud"], m["num_rep"] + m["num_met"] + m["num_cif"]))
    p.append("")
    p.append("**LA FORMA DE LOS NUMERALES SE MIDE CON LOS DOS PATRONES Y LAS DOS CIFRAS SE")
    p.append("PUBLICAN.** El patron entrecomillado (el del acta 184) da %d y el suelto (el"
             % m["n_entrecomillado"])
    p.append("del acta 189) da %d. **El acta 195 numera con comillas inversas, asi que"
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
    p.append("**EL CERO DE `EN CONTRA` VA POR LA QUINTA ACTA SEGUIDA.** De las %d,"
             % m["n_adj"])
    p.append("**%d son discutibles del ejecutor y los %d van A FAVOR**; las otras %d son"
             % (m["n_discutibles"], m["n_a_favor_discutibles"], m["n_preg"]))
    p.append("**preguntas contestadas** (%s), **dos de ellas por extension citable y con"
             % ", ".join("`%s` en la `%s`" % (pn, c) for c, pn in m["preguntas"]))
    p.append("la cita comprobada contra su fichero**. **CIFRA `EN CONTRA`: %d.**"
             % m["n_en_contra_discutibles"])
    p.append("")
    p.append("**Y ESE CERO NO SE VUELVE A PROBAR POR MUTACION: SE DICE CON SU FICHERO.**")
    p.append("`%s` mide **%d bytes** en disco y **%d** por LF, y su"
             % (ARNES_QUE_YA_CUBRE, m["arnes_disco"], m["arnes_lf"]))
    p.append("veredicto, leido del propio fichero, es %r. La guarda vieja de la 190"
             % m["arnes_veredicto"])
    p.append("(`if not en_contra: PARADA`) corrida sobre esta acta **%s**."
             % ("PARARIA" if m["vieja_pararia"] else "no pararia"))
    p.append("")
    p.append("### LOS %d HALLAZGOS DE LA SECCION 5, Y AQUI EL LECTOR QUE MANDA ES EL VIEJO"
             % m["n_hall"])
    p.append("")
    for clave, ln, tit in m["hallazgos"]:
        p.append("- **`%s`** (linea %d del acta): %s" % (clave, ln, tit[:200]))
    p.append("")
    p.append("**LOS TRES LECTORES SE CORREN Y LAS TRES CIFRAS SE PUBLICAN.** El acta 195")
    p.append("**vuelve a la negrita de apertura de parrafo**, que es la forma vieja:")
    p.append("`claves_entrecomilladas` da **%d**, `claves_de_adjudicacion` da **%d** y"
             % (m["her_comillas"], m["her_sueltos"]))
    p.append("`hallazgos_en_titular()`, el lector que la 194 tuvo que ANADIR para su acta,")
    p.append("da **%d**. **Ninguno se retira**: retirar el de la 194 estrecharia el"
             % m["n_titulares"])
    p.append("vocabulario a la forma del acta de hoy, y la proxima que titule con `###`")
    p.append("haria PARAR el instrumento.")
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
    p.append("hallazgos**, y su propia celda lo escribe nombrando el `654` y el `719`. Por")
    p.append("resta salen **%d discrepancias fuera del marcado** mas los %d hallazgos."
             % (m["n_disc_fuera"], m["n_hall"]))
    p.append("")
    p.append("### LAS CAIDAS, Y LA FILA DE LAS PROPIAS VIENE PARTIDA EN DOS A PROPOSITO")
    p.append("")
    p.append("**LA SEDE DE LAS CAIDAS PROPIAS NO SE SUPONE: es la seccion %d.** En el acta"
             % m["seccion_propias"])
    p.append("194 estaban en la 8 y en la 192 en la 6. Su cabecera, literal: %r"
             % m["cabecera_seccion3"])
    p.append("")
    p.append("| lo que se cuenta | del cuerpo del acta | de su fila de la tabla |")
    p.append("|---|---:|---:|")
    p.append("| caidas propias del auditor, TOTAL | %d | %d |"
             % (m["n_aud"], m["num_aud_total"]))
    p.append("| caidas propias del auditor, QUE ACUMULAN | (el cuerpo no las separa) | %d |"
             % m["num_aud_acum"])
    p.append("| del ejecutor, de reporte | (el cuerpo no las declara: son cero) | %d |"
             % m["num_rep"])
    p.append("| del ejecutor, de cifra publicada | (el cuerpo no las declara: son cero) | %d |"
             % m["num_cif"])
    p.append("| del ejecutor, de metodo, con el rango expandido | %d | %d |"
             % (len(m["exp_met"]), m["num_met"]))
    p.append("")
    p.append("**LA FILA DE LAS PROPIAS VIENE PARTIDA EN DOS, Y ESO NO ES UNA RAREZA DEL")
    p.append("ACTA: ES EL REMEDIO DE SU PROPIO HALLAZGO `5.1` APLICADO A SU MISMA TABLA EN")
    p.append("LA VUELTA EN QUE LO LEVANTA.** El `5.1` denuncia que la fila del acta 194")
    p.append("decia *\"caidas propias del auditor: 1\"* cuando su cuerpo declaraba dos,")
    p.append("porque en realidad contaba **solo las que acumulan**. Aqui el acta escribe")
    p.append("las dos filas con su rotulo entero.")
    p.append("")
    p.append("**Y ESO OBLIGO A CAMBIAR EL LECTOR, CON SU MEDICION DELANTE.** La aguja corta")
    p.append("de la 194 (`%s`) casa sobre esta acta con **%d**"
             % (R92.AGUJA_FILA_CAIDAS_AUDITOR, m["n_corta"]))
    p.append("filas, y quien la usara se quedaria con `[0]`, o sea con la de las que")
    p.append("ACUMULAN: **registraria %d donde el cuerpo declara %d**, que es exactamente"
             % (m["num_aud_acum"], m["n_aud"]))
    p.append("la confusion que el `5.1` denuncia. **`filas_de_las_propias()` lee las dos")
    p.append("con su aguja larga, publica las dos, y coteja contra la del TOTAL**, que es")
    p.append("la que mide lo mismo que el cuerpo. **El cotejo calza: %d y %d.**"
             % (m["n_aud"], m["num_aud_total"]))
    p.append("")
    p.append("**LA ESPECIE DE LA CAIDA PROPIA, LEIDA DE SU PARRAFO Y NO SUPUESTA:**")
    p.append("")
    for k, ln, esp in m["especies_aud"]:
        p.append("- **DEL AUDITOR**, `%s` (linea %d del acta): %s"
                 % (k, ln, ", ".join(esp)))
    p.append("")
    p.append("**EL VOCABULARIO DE ESTADOS SI CRECE, EN DOS MARCAS, Y LA CIFRA QUE LO")
    p.append("JUSTIFICA VA DELANTE:** con el heredado entero y nada mas saldrian `SIN")
    p.append("DECIR` **%d** adjudicaciones (la `4.8` y la `4.10`) y este registrador"
             % m["n_sin_decir_heredado"])
    p.append("**PARARIA**. Las dos marcas nuevas son **literales del acta y no")
    p.append("parafrasis**: %s. **Se anaden y no se ensanchan**"
             % ", ".join("`%s`" % x for x in MARCAS_NUEVAS_195))
    p.append("(la diferencia que el acta 184 adjudico a favor en su `5.3`): ninguna vieja")
    p.append("se retira ni se recorta, y el heredado corre PRIMERO, de modo que un titulo")
    p.append("que dijera `EN CONTRA` seguiria saliendo `EN CONTRA`.")
    p.append("")
    p.append("**EL VOCABULARIO DE ESPECIES NO CRECE EN ESTA ACTA**, y se dice porque en la")
    p.append("194 si crecio: con el de la 193 y nada mas saldrian SIN ESPECIE **%d**"
             % m["n_sin_especie_vieja"])
    p.append("caida(s). Reparto: **DE CIFRA PUBLICADA %d, DE METODO %d, ROMPER UN"
             % (m["n_cifra"], m["n_metodo"]))
    p.append("REMEDIO ESCRITO %d**." % m["n_remedio"])
    p.append("")
    p.append("**LA `C.1` DEL AUDITOR ES DE METODO Y NO ACUMULA**, y el propio acta lo")
    p.append("razona: no toca ninguno de los tres prohibidos antes del sello, **el sujeto")
    p.append("NO se quemo**, y lo probo DESPUES por la propia cuarta puerta (**30 de 30")
    p.append("sellados vuelven TAPADOS y 0 destapes apuntados**). **No continua ninguna")
    p.append("racha: abre la suya en 1.**")
    p.append("")
    p.append("**Y LAS TRES DEL EJECUTOR SON CERO: %d de reporte, %d de cifra publicada y"
             % (m["num_rep"], m["num_cif"]))
    p.append("%d de metodo.** **LA RACHA DE REPORTE VUELVE A CERO**, leida de la celda"
             % m["num_met"])
    p.append("derecha de su fila y no supuesta: **racha de reporte: %s**. La 194 la dejo"
             % m["racha_rep"])
    p.append("en 1 y esta vuelta la corta. **NO HAY ESCALADA QUE ENCARGAR**, y el acta lo")
    p.append("dice expresamente para que no se lea como olvido.")
    p.append("")
    p.append("### LA METRICA DE CREDITO, Y SU FILA DE PUESTOS MIDE CERO QUEMADOS")
    p.append("")
    p.append("**LAS %d FILAS DE DATOS DE LA SECCION 7, PEGADAS DEL ACTA:**" % m["n_filas7"])
    p.append("")
    p.append("```")
    for _ln, txt in m["filas7"]:
        p.append(txt)
    p.append("```")
    p.append("")
    p.append("**LA NOTA DE LA FILA DE PUESTOS ES `%s`.** Las dos heredadas se"
             % NOTA_DE_PUESTOS_195)
    p.append("siguen buscando y sus cifras se publican: `%s` (de la 191) aparece"
             % R92.NOTA_DE_PUESTOS)
    p.append("**%s** y `%s` (de la 194) aparece **%s**."
             % ("SI" if m["notas"][0][2] else "NO", R94.NOTA_DE_PUESTOS_194,
                "SI" if m["notas"][1][2] else "NO"))
    p.append("")
    p.append("Son **%s aislados y %s cotejados, con %s quemados**. **ESA ES LA DIFERENCIA"
             % (m["aislados"], m["cotejados"], m["quemados"]))
    p.append("CON LA 194, QUE MIDIO ONCE, Y EL ACTA LE PONE CAUSA: los mensajes de commit")
    p.append("del ejecutor ya no publican clases por puesto ni el reparto de una ciega.")
    p.append("**ESO FUNCIONO, Y SE REGISTRA COMO LO QUE ES: UN REMEDIO A MANO QUE MIDIO.**")
    p.append("Su guarda de codigo sigue pendiente y va nombrada en lo que queda fuera.")
    p.append("")
    p.append("**Y LA FILA NO PUBLICA UN SEGUNDO COTEJO, QUE TAMBIEN ES UNA MEDICION Y NO")
    p.append("UN HUECO:** con **%s** quemados no hay dos cotejos que publicar, asi que el"
             % m["quemados"])
    p.append("acta escribe uno solo. **El registrador de la 194 exigia SIEMPRE el segundo y")
    p.append("sobre esta acta PARARIA.** Aqui la exigencia se hace **condicional a que haya")
    p.append("quemados**, y **en esa rama sigue entera**: si los hubiera y faltara el")
    p.append("segundo cotejo, el registrador para igual. **Lo que se estrecha es el caso,")
    p.append("no la guarda.**")
    p.append("")
    p.append("### LA DEUDA DE LA SERIE, REMEDIDA AQUI EN VEZ DE HEREDARSE")
    p.append("")
    p.append("Tramo mirado: actas **173 a %d**. **CIFRA actas sin entrada propia en la"
             % (VUELTA_DEL_ACTA - 1))
    p.append("serie: %d** (%s). **Se registra y NO se arregla en esta vuelta**, que es lo"
             % (len(m["salto"][0]),
                ", ".join(str(x) for x in m["salto"][0]) or "ninguna"))
    p.append("que el encargo de la 195 deja escrito en su lista de lo que sigue fuera.")
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


def entrada_publica_las_dos_mitades(entrada, total, acumulan):
    """LA GUARDA: LA ENTRADA TIENE QUE PUBLICAR LAS DOS MITADES DE LA FILA. PURA.
    Devuelve (ok, informe).

    ES LA HERMANA DE `entrada_publica_las_dos()` DE LA 194 Y NO SU COPIA, y la
    diferencia es la que importa: alli el acta se contradecia consigo misma y la
    guarda exigia declarar el descuadre; aqui **el acta esta bien y son sus dos
    filas las que miden cosas distintas**, asi que lo que se exige es que la
    entrada no se quede con una sola. Publicar solo el `%d` de las que acumulan
    seria repetir el error que el hallazgo `5.1` denuncia, esta vez desde el
    registro."""
    informe = []
    f_total = "| caidas propias del auditor, TOTAL | %d | %d |" % (total, total)
    f_acum = ("| caidas propias del auditor, QUE ACUMULAN | "
              "(el cuerpo no las separa) | %d |" % acumulan)
    t1 = f_total in entrada
    t2 = f_acum in entrada
    informe.append("la fila del TOTAL (%r) esta en la entrada: %s"
                   % (f_total, "SI" if t1 else "NO"))
    informe.append("la fila de las QUE ACUMULAN (%r) esta en la entrada: %s"
                   % (f_acum, "SI" if t2 else "NO"))
    if total == acumulan:
        informe.append("las dos mitades miden lo mismo en esta acta, y la guarda "
                       "exige las dos igual: un rotulo que se calla no se arregla "
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

    LO QUE PRUEBA, Y POR QUE PUEDE CAER: los cuatro trozos nuevos son PUROS y se
    corren sobre texto FABRICADO, con el valor esperado sacado de como se fabrico
    el texto y NO de una constante igual a la obtenida. `EJECUTOR.md` 1, EL CASO
    ROJO SE PRUEBA POR MUTACION."""
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("VUELTA 195, TAREA 1: CASO POSITIVO POR MUTACION DEL REGISTRADOR")
    w("=" * 78)
    w("")

    w("A) `filas_de_las_propias()` SOBRE UNA TABLA FABRICADA CON LA FILA PARTIDA")
    fab = [
        "## 7. LA METRICA",
        "",
        "| | esta vuelta | acumulado |",
        "|---|---:|---:|",
        "| caidas propias del auditor QUE ACUMULAN | **0** | racha 0 |",
        "| caidas propias del auditor, TOTAL del cuerpo | **7** | racha 1 |",
        "",
    ]
    partidas = filas_de_las_propias(fab, 1, len(fab))
    ok &= _caso(w, "la aguja de QUE ACUMULAN casa con UNA sola fila",
                len(partidas[AGUJA_FILA_AUD_ACUMULAN]), 1)
    ok &= _caso(w, "la aguja de TOTAL casa con UNA sola fila",
                len(partidas[AGUJA_FILA_AUD_TOTAL]), 1)
    ok &= _caso(w, "y cada una trae SU numeral, que son distintos",
                (R92.numeral_de_la_fila(partidas[AGUJA_FILA_AUD_ACUMULAN][0][1]),
                 R92.numeral_de_la_fila(partidas[AGUJA_FILA_AUD_TOTAL][0][1])),
                (0, 7))
    w("   LA MUTACION, Y ES LA QUE PRUEBA QUE EL LECTOR NUEVO HACIA FALTA: la")
    w("   aguja CORTA de la 194 casa con LAS DOS filas, y quien se quedara con la")
    w("   primera registraria 0 donde el cuerpo declara 7. Si diera una sola fila,")
    w("   el lector nuevo seria un adorno.")
    corta = R92.fila_de_la_metrica(fab, 1, len(fab), R92.AGUJA_FILA_CAIDAS_AUDITOR)
    ok &= _caso(w, "la aguja corta de la 194 casa con LAS DOS", len(corta), 2)
    ok &= _caso(w, "y su primera fila es la de las QUE ACUMULAN, o sea el 0",
                R92.numeral_de_la_fila(corta[0][1]), 0)
    w("")

    w("B) `cifras_de_la_fila_de_puestos()` Y LA EXIGENCIA CONDICIONAL")
    con_quemados = ("| puestos | 30 aislados, **30 cotejados**, **ONCE QUEMADOS** "
                    "por el contexto, y el cotejo limpio va sobre 19 | **1.096** |")
    sin_quemados = ("| puestos | 30 aislados, **30 cotejados**, **CERO quemados** "
                    "| **1.126** |")
    a1 = cifras_de_la_fila_de_puestos(con_quemados)
    a2 = cifras_de_la_fila_de_puestos(sin_quemados)
    ok &= _caso(w, "con quemados lee las CUATRO cifras", a1, ("30", "30", "ONCE", "19"))
    ok &= _caso(w, "sin quemados lee tres y devuelve None en el cotejo limpio",
                a2, ("30", "30", "CERO", None))
    w("   LA MUTACION: si `quemados_son_cero` dijera que SI ante cualquier cosa, la")
    w("   exigencia del segundo cotejo se apagaria para siempre y una fila con once")
    w("   quemados y sin cotejo limpio pasaria por buena.")
    ok &= _caso(w, "`CERO` es cero", quemados_son_cero("CERO"), True)
    ok &= _caso(w, "`0` es cero", quemados_son_cero("0"), True)
    ok &= _caso(w, "`ONCE` NO es cero", quemados_son_cero("ONCE"), False)
    ok &= _caso(w, "y `None` NO es cero, que es lo prudente",
                quemados_son_cero(None), False)
    w("")

    w("C) `entrada_publica_las_dos_mitades()`, QUE CAE SI LA ENTRADA SE QUEDA CON")
    w("   UNA SOLA MITAD")
    buena = ("bla bla" + NL
             + "| caidas propias del auditor, TOTAL | 1 | 1 |" + NL
             + "| caidas propias del auditor, QUE ACUMULAN | "
               "(el cuerpo no las separa) | 0 |" + NL)
    mala = ("bla bla" + NL
            + "| caidas propias del auditor, TOTAL | 1 | 1 |" + NL)
    ok &= _caso(w, "la entrada con LAS DOS mitades pasa",
                entrada_publica_las_dos_mitades(buena, 1, 0)[0], True)
    w("   LA MUTACION: se quita la mitad de las que ACUMULAN y la guarda TIENE que")
    w("   caer. Si no cayera, el registro repetiria desde su lado el error que el")
    w("   hallazgo 5.1 denuncia en la tabla del acta.")
    ok &= _caso(w, "y la entrada que se queda con UNA sola CAE",
                entrada_publica_las_dos_mitades(mala, 1, 0)[0], False)
    w("")

    w("B.2) `numeral_de_la_fila_195()`, QUE LEE `**0 nuevas**` SIN ENSANCHAR")
    con_palabra = "| caidas del ejecutor de metodo | **0 nuevas** | |"
    limpia = "| caidas del ejecutor de reporte | **7** | racha 0 |"
    muda = "| una fila sin cifra | ninguna cosa | |"
    w("   LA MUTACION: si el heredado ya leyera `**0 nuevas**`, el lector nuevo")
    w("   seria un adorno; y si el nuevo leyera cualquier cosa, una celda muda")
    w("   dejaria de hacer PARAR.")
    ok &= _caso(w, "el heredado NO lee `**0 nuevas**`",
                R92.numeral_de_la_fila(con_palabra), None)
    ok &= _caso(w, "el nuevo SI la lee, y da 0",
                numeral_de_la_fila_195(con_palabra), 0)
    ok &= _caso(w, "y no cambia lo que el heredado ya leia",
                (R92.numeral_de_la_fila(limpia), numeral_de_la_fila_195(limpia)),
                (7, 7))
    ok &= _caso(w, "una celda muda sigue dando None con los dos",
                (R92.numeral_de_la_fila(muda), numeral_de_la_fila_195(muda)),
                (None, None))
    w("")

    w("C.2) `estado_de_la_adjudicacion_195()`, QUE ANADE DOS MARCAS SIN ENSANCHAR")
    t48 = ("`4.8` (`P.1`, cual es la sede): CONTESTADA, y la respuesta corrige a "
           "mi predecesor, no al ejecutor.")
    t410 = "`4.10` (`P.3`, la bateria): CONTESTADA, con las dos mitades."
    w("   LA MUTACION: con el vocabulario HEREDADO estos dos titulos salen SIN")
    w("   DECIR, y el registrador PARA. Si el heredado ya los leyera, las marcas")
    w("   nuevas serian un adorno y su cifra no diria nada.")
    ok &= _caso(w, "con el heredado, la de la 4.8 sale SIN DECIR",
                R92.estado_de_la_adjudicacion(t48), "SIN DECIR")
    ok &= _caso(w, "con el heredado, la de la 4.10 sale SIN DECIR",
                R92.estado_de_la_adjudicacion(t410), "SIN DECIR")
    ok &= _caso(w, "con el nuevo, la de la 4.8 se lee",
                estado_de_la_adjudicacion_195(t48),
                "CONTESTADA, Y LA RESPUESTA CORRIGE AL PREDECESOR DEL AUDITOR")
    ok &= _caso(w, "con el nuevo, la de la 4.10 se lee",
                estado_de_la_adjudicacion_195(t410),
                "CONTESTADA CON LAS DOS MITADES: CORRIDA SI, VERDE NO")
    w("   Y LA PARADA SE CONSERVA: un titulo mudo sigue saliendo SIN DECIR, y el")
    w("   heredado sigue mandando por delante del nuevo.")
    ok &= _caso(w, "un titulo mudo sigue saliendo SIN DECIR",
                estado_de_la_adjudicacion_195("`4.9` (`P.9`, algo): pues eso."),
                "SIN DECIR")
    ok &= _caso(w, "y `EN CONTRA` gana aunque el titulo traiga una marca nueva",
                estado_de_la_adjudicacion_195(
                    "`4.9` (`P.9`): EN CONTRA, con las dos mitades."),
                "EN CONTRA")
    w("")

    w("D) `titulo_de_la_entrada()` NOMBRA EL ACTA 195 Y NO OTRA")
    t = titulo_de_la_entrada(10, 3, 3, 1, 0)
    ok &= _caso(w, "el titulo cierra con `del acta de la vuelta 195`",
                t.endswith("del acta de la vuelta %d" % VUELTA_DEL_ACTA), True)
    w("   LA MUTACION: la maquina de la 194 cierra con SU numero, y un titulo")
    w("   armado con ella nombraria el acta equivocada, que es lo que rompe la")
    w("   marca de idempotencia de la casa.")
    ok &= _caso(w, "la de la 194 cierra con `del acta de la vuelta 194`",
                R94.titulo_de_la_entrada(10, 3, 3, 1, 0).endswith(
                    "del acta de la vuelta %d" % R94.VUELTA_DEL_ACTA), True)
    ok &= _caso(w, "y las dos frases NO son la misma",
                t == R94.titulo_de_la_entrada(10, 3, 3, 1, 0), False)
    ok &= _caso(w, "la concordancia del singular sale bien con UNA caida propia",
                "la caida propia" in t, True)
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
    ok_guarda, informe = entrada_publica_las_dos_mitades(
        entrada, m["n_aud"], m["num_aud_acum"])
    for l in informe:
        w("   " + l)
    w("   VEREDICTO DE LA GUARDA: %s" % ("VERDE" if ok_guarda else "ROJO"))
    if not ok_guarda:
        w("   ROJO: la entrada no publica las dos mitades. NO SE ESCRIBE NADA.")
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
