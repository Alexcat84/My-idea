# -*- coding: utf-8 -*-
r"""vuelta193_tarea1a_registrar_acta193.py . EL ACTA 193 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA, Y ESTE REGISTRADOR SIGUE SIENDO IDEMPOTENTE.

LA MAQUINA SE IMPORTA Y NO SE COPIA. Todo lo generico (acotar el acta, contar
claves, leer titulos, repartir caidas por lead heredado, expandir rangos, leer
filas de la tabla de credito, la serie) sale de
`vuelta192_tarea1a_registrar_acta192.py`, que a su vez importa de la 191, la 190
y la 189. AQUI SOLO VIVE LO QUE EL ACTA 193 TIENE DISTINTO, y va dicho uno por
uno para que nadie tenga que adivinarlo:

  1. `MIA` EN SINGULAR. El acta 193 declara UNA caida propia y encabeza su
     parrafo con **MIA: UNA, DE METODO.**, no con `MIAS`. Con las marcas
     heredadas (`MARCAS_LEAD_AUDITOR = ("MIAS",)`) el reparto sale MEDIDO Y MAL:
     las cuatro claves caen del lado del ejecutor y el auditor sale con CERO. La
     marca se ensancha a `MIA`, que cubre las dos formas, y la cifra de antes se
     publica al lado en vez de taparse.
  2. DOS MARCAS DE ESTADO NUEVAS, literales de dos titulos del acta 193:
     `NO LO CAMBIAN` (la `4.8`) y `ADJUDICADO: SE CONGELAN` (la `4.10`). Sin
     ellas las dos salen `SIN DECIR` y el registrador PARA, que es lo correcto:
     un estado que la maquina no sabe leer no se supone.
  3. LA CAIDA PROPIA DE ESTA ACTA ES **DE METODO** Y NO HAY NINGUNA DE CIFRA
     PUBLICADA. El registrador de la 192 PARABA si ninguna propia era `DE CIFRA
     PUBLICADA`, porque su encargo decia que una lo era. Aqui esa parada seria
     falsa: lo que se exige es que CADA propia DECLARE su especie, y el reparto
     por especie se publica salga lo que salga.
  4. LAS CAIDAS DEL EJECUTOR VAN POR DOS FILAS Y NO POR UNA. El acta 193 asigna
     UNA caida de REPORTE (`C.1`, que NO acumula) y ademas CITA las cuatro de
     METODO que el propio reporte de la 192 se declaro (`C.1` a `C.4`). Son dos
     cifras distintas, viven en dos filas distintas de la tabla de credito, y
     LAS DOS SE COTEJAN CONTRA SU FILA. Mezclarlas seria publicar un 5 que no
     dice nada.

TODA CIFRA SE CUENTA DEL CUERPO ACOTADO DEL ACTA Y NINGUNA DEL ENCARGO. Donde el
encargo publica una, se computa la propia y SE PUBLICAN LAS DOS.

EL NUMERO DE LA ENTRADA NO SE TECLEA: lo computa `serie_de_registros.py`
recomputando la serie de sus DOS sedes.

USO:
  python scripts/loop/vuelta193_tarea1a_registrar_acta193.py --simular
  python scripts/loop/vuelta193_tarea1a_registrar_acta193.py
  python scripts/loop/vuelta193_tarea1a_registrar_acta193.py --mutacion
"""
import argparse
import hashlib
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

VUELTA_DEL_ACTA = 193
VUELTA_QUE_ESCRIBE = 193
SUFIJO_QUE_ESCRIBE = "193"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "4."
PREFIJO_HALLAZGO = "5."
SECCION_DE_LOS_HALLAZGOS = 5
SECCION_DE_LAS_CAIDAS = 6
SECCION_DE_LA_METRICA = 7

# (1) LA MARCA DEL LEAD DEL AUDITOR, ENSANCHADA A LA FORMA SINGULAR.
MARCAS_LEAD_AUDITOR_193 = ("MIA",)

# (2) LAS DOS MARCAS DE ESTADO QUE EL ACTA 193 ESTRENA, LITERALES DE SUS TITULOS.
MARCA_NO_LO_CAMBIAN = "NO LO CAMBIAN"
MARCA_SE_CONGELAN = "ADJUDICADO: SE CONGELAN"

# (4) LA FILA DE LA TABLA QUE LLEVA LA CAIDA DE REPORTE DEL EJECUTOR.
AGUJA_FILA_CAIDAS_REPORTE = "caidas del ejecutor de reporte"

# EL ARNES DE LA 191 QUE YA CUBRE EL CERO DE `EN CONTRA`, NOMBRADO PARA MEDIRLO
# EN VEZ DE RE FABRICAR SU CASO. Es la tercera acta seguida con cero.
ARNES_QUE_YA_CUBRE = "docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt"

# LA ESPECIE, HEREDADA.
MARCA_ESPECIE_METODO = R92.MARCA_ESPECIE_METODO
MARCA_ESPECIE_CIFRA = R92.MARCA_ESPECIE_CIFRA
MARCA_ESPECIE_REPORTE = "DE REPORTE"


def estado_de_la_adjudicacion(titulo):
    """EL ESTADO DE UNA ADJUDICACION, LEIDO DE SU TITULO LITERAL. PURA.

    Delega primero en la maquina de la 192, que ya lleva doce marcas, y solo si
    aquella sale `SIN DECIR` prueba LAS DOS MARCAS NUEVAS DEL ACTA 193. Asi el
    vocabulario CRECE y no se re escribe: si una marca vieja muerde, manda ella.

    **Si un titulo no dijera ninguna, el estado sale `SIN DECIR` y quien llama
    hace PARADA en vez de suponer.**"""
    heredado = R92.estado_de_la_adjudicacion(titulo)
    if heredado != "SIN DECIR":
        return heredado
    alto = titulo.upper()
    if MARCA_NO_LO_CAMBIAN in alto:
        return "CONTESTADA: EL REGIMEN NO CAMBIA, Y EL DOBLE VA ENCARGADO IGUAL"
    if MARCA_SE_CONGELAN in alto:
        return "CONTESTADA Y ENCARGADA COMO BLOQUEANTE"
    return "SIN DECIR"


def caidas_del_ejecutor_repartidas(lineas, ini6, fin6):
    """LAS CAIDAS DEL EJECUTOR, SEPARADAS EN LAS QUE EL ACTA ASIGNA Y LAS QUE EL
    ACTA CITA. Devuelve (asignadas, citadas), dos listas de (linea, claves,
    especies, negrita).

    POR QUE HACE FALTA, Y NO ES UN ADORNO: el acta 193 escribe DOS cosas
    distintas del ejecutor en la misma seccion. Una es **la caida que adjudica**
    (`C.1`, de REPORTE, que no acumula). La otra es **una cita** de las cuatro
    caidas de METODO que el propio reporte de la 192 ya se habia declarado
    (`C.1` a `C.4` del reporte). Contarlas juntas da cinco claves y publica un
    numero que no corresponde a ninguna fila de la tabla de credito.

    LA VARA, ESCRITA ANTES DE MEDIR: **es ASIGNADA el parrafo cuya NEGRITA
    empieza por la clave** (asi es como el acta titula sus caidas); es CITADA
    cualquier otro parrafo del lado del ejecutor que nombre claves en su cuerpo.
    Semi-pura: solo lee las lineas que le pasan."""
    asignadas, citadas = [], []
    for a, _b, neg, txt in R92.parrafos_con_negrita(lineas, ini6, fin6):
        claves_neg = sorted(set(int(x) for x in R92.PAT_CLAVE_C.findall(neg)))
        _lit, exp = R92.expandir_rangos_de_clave(txt)
        fila = (a, exp, R92.especie_de_la_caida(txt), neg)
        if claves_neg:
            asignadas.append((a, claves_neg, R92.especie_de_la_caida(txt), neg))
        elif exp:
            citadas.append(fila)
    return asignadas, citadas


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
    claves = R92.claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_ADJ)
    entrecomilladas = R92.claves_entrecomilladas(lineas, inicio, fin, PREFIJO_ADJ)
    w("   patron SIN comillas inversas -> %d" % len(claves))
    for clave, cuantas in claves:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    w("   patron CON comillas inversas (el del acta 188) -> %d" % len(entrecomilladas))
    dobles = [c for c, n in claves if n != 1]
    if dobles:
        w("   PARADA: hay claves repetidas dentro del acta: %s" % ", ".join(dobles))
        print(NL.join(salida))
        return 1
    if not claves:
        w("   PARADA: ningun patron encuentra adjudicaciones y el acta 193 declara")
        w("   diez. No se escribe una entrada con cero.")
        print(NL.join(salida))
        return 1
    w("")

    w("D) EL TITULO LITERAL DE CADA ADJUDICACION, SU FAMILIA Y SU ESTADO")
    w("   (EL VOCABULARIO LLEVA LAS DOS MARCAS NUEVAS DEL ACTA 193 Y CONSERVA LAS")
    w("    DOCE HEREDADAS. `EN CONTRA` sigue buscandose PRIMERO aunque hoy no")
    w("    muerda, y las nuevas solo se prueban si ninguna vieja mordio)")
    adjudicaciones = []
    n_sin_decir_vieja = 0
    for clave, _n in claves:
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, err2 = R92.titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err2:
            w("   %s -> %s" % (clave, err2))
            print(NL.join(salida))
            return 1
        ln, tit = res
        if R92.estado_de_la_adjudicacion(tit) == "SIN DECIR":
            n_sin_decir_vieja += 1
        adjudicaciones.append((clave, R92.familia_de_la_adjudicacion(tit),
                               estado_de_la_adjudicacion(tit), ln, tit))
        w("   %-5s linea %-6d [%s / %s]" % (clave, ln, adjudicaciones[-1][1],
                                            adjudicaciones[-1][2]))
        w("         %s" % tit[:150])
    sin_decir = [c for c, _f, e, _l, _t in adjudicaciones if e == "SIN DECIR"]
    if sin_decir:
        w("   PARADA: %s esta en un estado que este registrador NO SABE LEER."
          % ", ".join(sin_decir))
        print(NL.join(salida))
        return 1
    w("   CON EL VOCABULARIO DE LA 192 Y NADA MAS, saldrian SIN DECIR: %d"
      % n_sin_decir_vieja)
    w("   O SEA QUE LAS DOS MARCAS NUEVAS NO SON UN ADORNO: sin ellas este")
    w("   registrador PARARIA, que es lo que tiene que hacer un vocabulario que")
    w("   no alcanza.")
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
    w("   TERCERA ACTA SEGUIDA. La guarda VIEJA de la 190 corrida aqui: %s"
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
    w("   sha256 LF: %s" % hashlib.sha256(lf_arnes).hexdigest())
    w("   su veredicto, leido del propio fichero: %r"
      % (ver_arnes[0] if ver_arnes else "(sin linea de veredicto)"))
    if len(datos_arnes) == 0 or not ver_arnes or "VERDE" not in ver_arnes[0]:
        w("   PARADA: el arnes que se cita como cobertura mide cero bytes o no sale")
        w("   verde. Una ruta que promete prueba sobre un vacio es CAIDA DE CIFRA.")
        print(NL.join(salida))
        return 1
    if not preguntas:
        w("   PARADA: ninguna adjudicacion nombra un `P.n` y el acta 193 declara TRES")
        w("   preguntas contestadas. No se escribe una lista vacia.")
        print(NL.join(salida))
        return 1
    w("")

    w("E) LOS HALLAZGOS DE LA SECCION %d, Y CUANTOS CUENTAN FUERA DEL MARCADO"
      % SECCION_DE_LOS_HALLAZGOS)
    claves_h = R92.claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_HALLAZGO)
    hallazgos = []
    for clave, _n in claves_h:
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, err3 = R92.titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err3:
            w("   %s -> %s" % (clave, err3))
            print(NL.join(salida))
            return 1
        hallazgos.append((clave, res[0], res[1]))
        w("   %-5s linea %-6d %s" % (clave, res[0], res[1][:120]))
    if not hallazgos:
        w("   PARADA: la seccion %d no trae ninguna clave `5.n`."
          % SECCION_DE_LOS_HALLAZGOS)
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
    nombrados, sueltos, piezas = R92.hallazgos_que_la_tabla_nombra(
        hallazgos, fila_fuera[0][1])
    w("   PARTIENDO POR `;` Y POR `,`: %d pieza(s), casan %d"
      % (len(piezas), len(nombrados)))
    w("   LOS QUE LA SUBCADENA NO NOMBRA: %d (%s)"
      % (len(sueltos), ", ".join(c for c, _l, _t in sueltos) or "ninguno"))
    numeral = R92.numeral_de_la_fila(fila_fuera[0][1])
    w("   EL NUMERAL DE LA PROPIA FILA, LEIDO Y NO TECLEADO: %s" % numeral)
    if numeral is None:
        w("   PARADA: la fila no trae cifra en su celda.")
        print(NL.join(salida))
        return 1
    w("   LA FILA DE LA 193 CUENTA JUNTAS LAS DISCREPANCIAS Y LOS HALLAZGOS, y")
    w("   por eso su numeral (%s) NO tiene por que igualar a las claves `5.n`"
      % numeral)
    w("   (%d). SE PUBLICAN LAS DOS Y NINGUNA SE ELIGE A OJO: el acta escribe en"
      % len(hallazgos))
    w("   su celda `(1804, 2833; y los cuatro hallazgos de la seccion 5)`, o sea")
    w("   DOS discrepancias mas los %d hallazgos." % len(hallazgos))
    n_disc_fuera = numeral - len(hallazgos) if numeral is not None else None
    w("   CIFRA discrepancias fuera del marcado, por resta: %s" % n_disc_fuera)
    if n_disc_fuera is None or n_disc_fuera < 0:
        w("   PARADA: la resta da negativo. El numeral y las claves no cuadran de")
        w("   ninguna forma y no se elige a ojo.")
        print(NL.join(salida))
        return 1
    w("")

    w("F) LAS CAIDAS, CON EL LEAD DEL AUDITOR EN SINGULAR")
    r6 = R92.rango_de_seccion(lineas, inicio, fin, SECCION_DE_LAS_CAIDAS)
    if r6 is None:
        w("   PARADA: el acta no tiene seccion %d." % SECCION_DE_LAS_CAIDAS)
        print(NL.join(salida))
        return 1
    ini6, fin6 = r6
    cabecera6 = lineas[ini6 - 1].strip()
    w("   la seccion %d va de la linea %d a la %d"
      % (SECCION_DE_LAS_CAIDAS, ini6, fin6))
    w("   SU CABECERA, LITERAL: %r" % cabecera6)
    w("")
    w("   LA MAQUINA HEREDADA, CORRIDA TAL CUAL, Y SU CIFRA SE PUBLICA AUNQUE ESTE")
    w("   MAL, QUE ES DE LO QUE SE TRATA:")
    her_eje, her_aud, her_hu = R92.caidas_por_lead_heredado(lineas, ini6, fin6)
    w("      con MARCAS_LEAD_AUDITOR = %r: ejecutor %d | auditor %d | huerfanas %d"
      % (R92.MARCAS_LEAD_AUDITOR, len(her_eje), len(her_aud), len(her_hu)))
    w("      EL ACTA 193 DECLARA UNA PROPIA DEL AUDITOR, Y ESA MAQUINA DA %d."
      % len(her_aud))
    w("      LA CAUSA, MEDIDA: el acta encabeza con `MIA: UNA, DE METODO.`, en")
    w("      SINGULAR, y la marca heredada es `MIAS`.")
    w("")
    c_eje, c_aud, huerfanas = R92.caidas_por_lead_heredado(
        lineas, ini6, fin6, marcas_aud=MARCAS_LEAD_AUDITOR_193)
    w("   CON LA MARCA ENSANCHADA A %r:" % (MARCAS_LEAD_AUDITOR_193,))
    w("      DEL EJECUTOR: %d clave(s)" % len(c_eje))
    for ln, k, neg, her in c_eje:
        w("         %s en la linea %d, heredada: %s, bajo %r" % (k, ln, her, neg[:60]))
    w("      DEL AUDITOR: %d" % len(c_aud))
    for ln, k, neg, her in c_aud:
        w("         %s en la linea %d, heredada: %s, bajo %r" % (k, ln, her, neg[:60]))
    w("      HUERFANAS: %d" % len(huerfanas))
    if huerfanas:
        w("   PARADA: hay caida(s) en un parrafo cuya negrita no dice de quien son.")
        print(NL.join(salida))
        return 1
    if not c_aud:
        w("   PARADA: no se encuentra ninguna caida propia del auditor y el acta 193")
        w("   declara UNA, escrita y no omitida.")
        print(NL.join(salida))
        return 1
    w("")

    w("   LAS DEL EJECUTOR, SEPARADAS EN ASIGNADAS Y CITADAS (la vara va escrita")
    w("   en el docstring de `caidas_del_ejecutor_repartidas`, ANTES de medir)")
    asignadas, citadas = caidas_del_ejecutor_repartidas(lineas, ini6, fin6)
    lineas_aud = set(ln for ln, _k, _n, _h in c_aud)
    asig_eje = [x for x in asignadas if x[0] not in lineas_aud]
    asig_aud = [x for x in asignadas if x[0] in lineas_aud]
    for a, ks, esp, neg in asig_eje:
        w("      ASIGNADA AL EJECUTOR (linea %d): C.%s | especie %s | %r"
          % (a, ",".join(str(k) for k in ks), esp or "NINGUNA", neg[:60]))
    for a, ks, esp, neg in asig_aud:
        w("      ASIGNADA AL AUDITOR  (linea %d): C.%s | especie %s | %r"
          % (a, ",".join(str(k) for k in ks), esp or "NINGUNA", neg[:60]))
    for a, exp, esp, neg in citadas:
        w("      CITADA (linea %d): %s | especie %s | %r"
          % (a, ", ".join("C.%d" % k for k in exp), esp or "NINGUNA", neg[:60]))
    n_eje_asignadas = sum(len(ks) for _a, ks, _e, _n in asig_eje)
    n_eje_citadas = sum(len(exp) for _a, exp, _e, _n in citadas)
    w("      CIFRA claves ASIGNADAS al ejecutor: %d" % n_eje_asignadas)
    w("      CIFRA claves CITADAS del ejecutor, con el rango expandido: %d"
      % n_eje_citadas)
    w("")

    w("   LAS TRES FILAS DE LA TABLA QUE COTEJAN ESTAS TRES CIFRAS")
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
            w("      %-26s (linea %d) %s" % (etiqueta, ln, txt))
    if not (fila_aud and fila_rep and fila_met):
        w("   PARADA: falta alguna de las tres filas de caidas en la tabla.")
        print(NL.join(salida))
        return 1
    num_aud = R92.numeral_de_la_fila(fila_aud[0][1])
    num_rep = R92.numeral_de_la_fila(fila_rep[0][1])
    num_met = R92.numeral_de_la_fila(fila_met[0][1])
    w("      numerales leidos y no tecleados: auditor %s | reporte %s | metodo %s"
      % (num_aud, num_rep, num_met))
    if None in (num_aud, num_rep, num_met):
        w("   PARADA: alguna de las tres filas no trae cifra legible.")
        print(NL.join(salida))
        return 1
    fallos_cotejo = []
    if len(c_aud) != num_aud:
        fallos_cotejo.append("auditor: parrafos %d contra fila %d"
                             % (len(c_aud), num_aud))
    if n_eje_asignadas != num_rep:
        fallos_cotejo.append("ejecutor de reporte: asignadas %d contra fila %d"
                             % (n_eje_asignadas, num_rep))
    if n_eje_citadas != num_met:
        fallos_cotejo.append("ejecutor de metodo: citadas %d contra fila %d"
                             % (n_eje_citadas, num_met))
    if fallos_cotejo:
        w("   PARADA: alguna cuenta del cuerpo no calza con su fila de la tabla:")
        for f in fallos_cotejo:
            w("      " + f)
        print(NL.join(salida))
        return 1
    w("      LAS TRES CALZAN: %d = %d, %d = %d, %d = %d."
      % (len(c_aud), num_aud, n_eje_asignadas, num_rep, n_eje_citadas, num_met))
    w("      Y LA DE ANTES SE PUBLICA IGUAL: contarlas juntas daria %d claves, que"
      % (n_eje_asignadas + n_eje_citadas))
    w("      no es el numeral de ninguna fila de la tabla.")
    w("")

    w("   LA ESPECIE DE CADA CAIDA, LEIDA DEL PARRAFO Y NO SUPUESTA")
    especies_aud = [(", ".join("C.%d" % k for k in ks), a, esp)
                    for a, ks, esp, _n in asig_aud]
    especies_eje = [(", ".join("C.%d" % k for k in ks), a, esp)
                    for a, ks, esp, _n in asig_eje]
    for k, a, esp in especies_aud + especies_eje:
        w("      %s (linea %d) -> %s" % (k, a, ", ".join(esp) or "NINGUNA"))
    sin_especie = [x for x in especies_aud if not x[2]]
    if not especies_aud or sin_especie:
        w("   PARADA: hay %d caida(s) propia(s) del auditor sin especie declarada."
          % len(sin_especie))
        print(NL.join(salida))
        return 1
    con_cifra = [x for x in especies_aud if MARCA_ESPECIE_CIFRA in x[2]]
    con_metodo = [x for x in especies_aud if MARCA_ESPECIE_METODO in x[2]]
    w("      REPARTO POR ESPECIE DE LAS PROPIAS DEL AUDITOR:")
    w("         DE CIFRA PUBLICADA: %d | DE METODO: %d"
      % (len(con_cifra), len(con_metodo)))
    w("      Y AQUI ESTA LA DIFERENCIA CON EL REGISTRADOR DE LA 192, DICHA EN VEZ")
    w("      DE CALLADA: aquel PARABA si ninguna propia era `DE CIFRA PUBLICADA`,")
    w("      porque su encargo decia que una lo era. En el acta 193 NINGUNA lo es,")
    w("      y esa parada seria falsa. LO QUE SE EXIGE AQUI es que cada propia")
    w("      DECLARE su especie, y el reparto se publica salga lo que salga.")
    if not con_metodo:
        w("   PARADA: el acta 193 declara su unica propia como DE METODO y ningun")
        w("   parrafo lo dice. No se supone.")
        print(NL.join(salida))
        return 1
    especie_rep = [x for x in especies_eje if MARCA_ESPECIE_REPORTE in " ".join(x[2])]
    w("      LA DEL EJECUTOR, POR SU ESPECIE: la marca %r aparece en su parrafo: %s"
      % (MARCA_ESPECIE_REPORTE,
         "SI" if MARCA_ESPECIE_REPORTE in asig_eje[0][3].upper() else "NO"))
    w("")

    w("G) LA METRICA DE CREDITO DE LA SECCION %d, ENTERA" % SECCION_DE_LA_METRICA)
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
    nota_exacta = bool(fila_p) and R92.NOTA_DE_PUESTOS in fila_p[0][1]
    nota = bool(fila_p) and R92.NOTA_DE_PUESTOS in fila_p[0][1].upper()
    literal = ""
    quemados = ""
    if fila_p:
        mm = re.search(r"(?i)(solape\s+total)", fila_p[0][1])
        literal = mm.group(1) if mm else ""
        mq = re.search(r"(?i)(cero\s+quemados)", fila_p[0][1])
        quemados = mq.group(1) if mq else ""
    w("   el literal %r aparece TAL CUAL en la fila: %s"
      % (R92.NOTA_DE_PUESTOS, "SI" if nota_exacta else "NO"))
    w("   comparado en mayusculas: %s" % ("SI" if nota else "NO"))
    w("   LO QUE EL ACTA ESCRIBE DE VERDAD, LEIDO Y NO PARAFRASEADO: %r" % literal)
    w("   Y LA OTRA MITAD QUE EL ENCARGO MANDA REGISTRAR, LEIDA IGUAL: %r"
      % quemados)
    if not nota:
        w("   PARADA: el encargo pide registrar la fila de puestos CON SU NOTA de")
        w("   solape total, y la fila no la trae.")
        print(NL.join(salida))
        return 1
    if not quemados:
        w("   PARADA: el encargo pide registrar el CERO QUEMADOS de la misma fila,")
        w("   y la fila no lo trae. Una nota que no esta no se parafrasea.")
        print(NL.join(salida))
        return 1
    numeros_p = re.findall(r"(\d+)\s+aislados", fila_p[0][1])
    cot_p = re.findall(r"\*\*(\d+)\s+cotejados\*\*", fila_p[0][1])
    w("   aislados y cotejados, leidos de la celda: %s y %s"
      % (numeros_p or "(no legible)", cot_p or "(no legible)"))
    w("")

    w("H) EL NUMERO DE LA ENTRADA, QUE NO SE TECLEA")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    w("   serie recomputada de sus dos sedes: %d entradas" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SERIE.colisiones(halladas)), len(SERIE.huecos(halladas))))
    w("   SIGUIENTE LIBRE: R.%d" % numero)
    w("   el encargo adelanta R.55 -> %s"
      % ("CALZA" if numero == 55 else "NO CALZA, y la discrepancia se declara"))
    w("")

    w("I) LA DEUDA DE LA SERIE, REMEDIDA AQUI Y NO HEREDADA")
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
        "adjudicaciones": adjudicaciones,
        "n_discutibles": len(discutibles), "n_preg": len(preguntas),
        "n_otras": len(otras), "n_a_favor_discutibles": len(a_favor),
        "n_en_contra_discutibles": len(en_contra),
        "vieja_pararia": not en_contra,
        "n_sin_decir_vieja": n_sin_decir_vieja,
        "arnes_disco": len(datos_arnes), "arnes_lf": len(lf_arnes),
        "arnes_veredicto": ver_arnes[0] if ver_arnes else "",
        "preguntas": [(c, R92.PAT_P_DEL_TITULO.search(t).group(0).strip("`"))
                      for c, _f, _e, _l, t in preguntas],
        "hallazgos": hallazgos, "n_hall": len(hallazgos),
        "hall_nombrados": nombrados, "piezas_fuera": piezas,
        "fila_fuera": fila_fuera, "numeral_fila": numeral,
        "n_disc_fuera": n_disc_fuera,
        "cabecera_seccion6": cabecera6,
        "her_eje": len(her_eje), "her_aud": len(her_aud),
        "c_eje": c_eje, "c_aud": c_aud,
        "n_aud": len(c_aud), "n_eje": n_eje_asignadas,
        "n_eje_citadas": n_eje_citadas,
        "num_aud": num_aud, "num_rep": num_rep, "num_met": num_met,
        "especies_aud": especies_aud, "especies_eje": especies_eje,
        "n_cifra": len(con_cifra), "n_metodo": len(con_metodo),
        "fila_aud": fila_aud, "fila_rep": fila_rep, "fila_met": fila_met,
        "filas7": filas7, "n_filas7": len(filas7),
        "fila_puestos": fila_p, "nota_de_puestos": nota,
        "nota_exacta": nota_exacta, "nota_literal": literal,
        "quemados_literal": quemados,
        "aislados": numeros_p[0] if numeros_p else "",
        "cotejados": cot_p[0] if cot_p else "",
        "salto": salto, "numero": numero, "ya_registrada": len(ya),
        "sedes": sedes,
    }
    return salida, medido


def titulo_de_la_entrada(n_adj, n_hall, n_preg, n_cai_aud, n_cai_eje):
    """EL TITULO DE LA ENTRADA, CON SUS CINCO NUMERALES EN PALABRA. PURA.

    NO SE DELEGA EN LA MAQUINA DE LA 192, Y LA RAZON ESTA MEDIDA: aquella cierra
    con `VUELTA_DEL_ACTA` de SU modulo, que es 192, y por eso un titulo armado
    con ella nombraria el acta equivocada. **La marca de idempotencia de la casa
    es literalmente `del acta de la vuelta N`**, asi que un numero mal puesto ahi
    no es un adorno: rompe la comprobacion que impide escribir dos veces.

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
    p.append("Por adicion, como `R.21` a `R.54`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.54`. Salida:")
    p.append("`docs/loop/SALIDA_V%s_T1A_REGISTRO_R%d.txt`."
             % (SUFIJO_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 1 EN CURSO Y LAS TAREAS 2 A 5 SIN")
    p.append("EMPEZAR, ASI QUE SUS GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA NO HA")
    p.append("PASADO.** Es la forma que la `6.4` del acta 172 adjudico como correcta.")
    p.append("")
    p.append("**LOS CINCO NUMERALES DEL TITULO NO ESTAN TECLEADOS:** se cuentan del acta")
    p.append("acotada (lineas %d a %d). **%d adjudicaciones numeradas (`4.1` a `4.%d`),"
             % (m["inicio"], m["fin"], m["n_adj"], m["n_adj"]))
    p.append("%d hallazgos numerados en la seccion 5, %d preguntas contestadas DENTRO de"
             % (m["n_hall"], m["n_preg"]))
    p.append("las adjudicaciones, %d caida propia del auditor y %d caida del ejecutor.**"
             % (m["n_aud"], m["n_eje"]))
    p.append("")
    p.append("**LA FORMA DE LOS NUMERALES SE MIDE CON LOS DOS PATRONES Y LAS DOS CIFRAS SE")
    p.append("PUBLICAN.** El patron entrecomillado (el del acta 188) da %d y el suelto (el"
             % m["n_entrecomillado"])
    p.append("del acta 189) da %d. **Ninguno se ensancha: se corren los dos y se dice lo"
             % m["n_adj"])
    p.append("que dan.**")
    p.append("")
    p.append("### LAS %d ADJUDICACIONES, UNA POR UNA, CON SU ESTADO LEIDO DEL TITULO"
             % m["n_adj"])
    p.append("")
    p.append("| clave | familia | estado, leido del titulo literal | linea del acta |")
    p.append("|---|---|---|---:|")
    for clave, fam, est, ln, _t in m["adjudicaciones"]:
        p.append("| `%s` | %s | %s | %d |" % (clave, fam, est, ln))
    p.append("")
    p.append("**EL CERO DE `EN CONTRA` VA POR LA TERCERA ACTA SEGUIDA.** De las %d,"
             % m["n_adj"])
    p.append("**%d son discutibles del ejecutor y los %d van A FAVOR**; las otras %d son"
             % (m["n_discutibles"], m["n_a_favor_discutibles"], m["n_preg"]))
    p.append("**preguntas contestadas** (%s). **CIFRA `EN CONTRA`: %d.**"
             % (", ".join("`%s` en la `%s`" % (pn, c) for c, pn in m["preguntas"]),
                m["n_en_contra_discutibles"]))
    p.append("")
    p.append("**Y ESE CERO NO SE VUELVE A PROBAR POR MUTACION: SE DICE CON SU FICHERO.**")
    p.append("`%s` mide **%d bytes** en disco y **%d** por LF, y su"
             % (ARNES_QUE_YA_CUBRE, m["arnes_disco"], m["arnes_lf"]))
    p.append("veredicto, leido del propio fichero, es %r. La guarda vieja de la 190"
             % m["arnes_veredicto"])
    p.append("(`if not en_contra: PARADA`) corrida sobre esta acta **%s**."
             % ("PARARIA" if m["vieja_pararia"] else "no pararia"))
    p.append("")
    p.append("**EL VOCABULARIO DE ESTADOS CRECE EN DOS MARCAS Y NO SE RE ESCRIBE.** Las")
    p.append("nuevas son literales de dos titulos del acta 193: `NO LO CAMBIAN` (la `4.8`)")
    p.append("y `ADJUDICADO: SE CONGELAN` (la `4.10`). **Con el vocabulario de la 192 y")
    p.append("nada mas, saldrian `SIN DECIR` %d adjudicaciones**, y este registrador"
             % m["n_sin_decir_vieja"])
    p.append("PARARIA. **Las marcas viejas se prueban PRIMERO y las nuevas solo si ninguna")
    p.append("vieja mordio.**")
    p.append("")
    p.append("### LOS %d HALLAZGOS DE LA SECCION 5, QUE NO SALEN DE NINGUN DISCUTIBLE"
             % m["n_hall"])
    p.append("")
    for clave, ln, tit in m["hallazgos"]:
        p.append("- **`%s`** (linea %d del acta): %s" % (clave, ln, tit))
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
    p.append("### LAS CAIDAS, Y LA MAQUINA HEREDADA SE PUBLICA AUNQUE DE MAL")
    p.append("")
    p.append("**LA CABECERA DE LA SECCION 6, LITERAL:** %r" % m["cabecera_seccion6"])
    p.append("")
    p.append("**LA CAUSA ESTA MEDIDA Y NO SUPUESTA.** `caidas_por_lead_heredado()` con las")
    p.append("marcas de la 192 (`MARCAS_LEAD_AUDITOR = (\"MIAS\",)`) reparte **%d al"
             % m["her_eje"])
    p.append("ejecutor y %d al auditor** sobre esta acta, y **el acta declara UNA propia**."
             % m["her_aud"])
    p.append("El acta 193 encabeza su parrafo con **`MIA: UNA, DE METODO.`, en SINGULAR**.")
    p.append("Con la marca ensanchada a `MIA`, que cubre las dos formas, el reparto sale")
    p.append("**%d y %d, y CERO huerfanas**. **La cifra de antes se publica al lado en vez"
             % (len(m["c_eje"]), m["n_aud"]))
    p.append("de taparse.**")
    p.append("")
    p.append("**Y LAS DEL EJECUTOR VAN POR DOS FILAS Y NO POR UNA.** El acta 193 escribe")
    p.append("dos cosas distintas en la misma seccion: **la caida que ADJUDICA** (`C.1`, de")
    p.append("REPORTE, que NO acumula) y **una CITA** de las cuatro de METODO que el propio")
    p.append("reporte de la 192 ya se habia declarado (`C.1` a `C.4` del reporte).")
    p.append("**Contarlas juntas daria %d claves, que no es el numeral de ninguna fila.**"
             % (m["n_eje"] + m["n_eje_citadas"]))
    p.append("")
    p.append("| lo que se cuenta | del cuerpo del acta | de su fila de la tabla |")
    p.append("|---|---:|---:|")
    p.append("| caidas propias del auditor | %d | %d |" % (m["n_aud"], m["num_aud"]))
    p.append("| del ejecutor, de reporte, ASIGNADAS | %d | %d |"
             % (m["n_eje"], m["num_rep"]))
    p.append("| del ejecutor, de metodo, CITADAS con el rango expandido | %d | %d |"
             % (m["n_eje_citadas"], m["num_met"]))
    p.append("")
    p.append("**LAS TRES CALZAN**, y si alguna no calzara este registrador PARARIA en vez")
    p.append("de elegir la que conviene.")
    p.append("")
    p.append("**LA ESPECIE DE CADA CAIDA, LEIDA DE SU PARRAFO Y NO SUPUESTA:**")
    p.append("")
    for k, ln, esp in m["especies_aud"]:
        p.append("- **DEL AUDITOR**, %s (linea %d del acta): %s"
                 % (k, ln, ", ".join(esp)))
    for k, ln, esp in m["especies_eje"]:
        p.append("- **DEL EJECUTOR**, %s (linea %d del acta): %s"
                 % (k, ln, ", ".join(esp) or "la declara su propia negrita"))
    p.append("")
    p.append("**REPARTO POR ESPECIE DE LAS PROPIAS DEL AUDITOR: DE CIFRA PUBLICADA %d, DE"
             % m["n_cifra"])
    p.append("METODO %d.** El registrador de la 192 PARABA si ninguna propia era `DE CIFRA"
             % m["n_metodo"])
    p.append("PUBLICADA`, porque su encargo decia que una lo era; **en el acta 193 ninguna")
    p.append("lo es, y esa parada seria falsa**. Lo que este registrador exige es que")
    p.append("**cada propia DECLARE su especie**, y el reparto se publica salga lo que")
    p.append("salga. **La caida del ejecutor NO ACUMULA por la letra del 27 ago 2026, y la")
    p.append("racha de reporte queda en 0**, tal como el acta lo escribe.")
    p.append("")
    p.append("### LA METRICA DE CREDITO, CON SU FILA DE PUESTOS Y SUS DOS NOTAS")
    p.append("")
    p.append("**LAS %d FILAS DE DATOS DE LA SECCION 7, PEGADAS DEL ACTA:**" % m["n_filas7"])
    p.append("")
    p.append("```")
    for _ln, txt in m["filas7"]:
        p.append(txt)
    p.append("```")
    p.append("")
    p.append("**LA FILA DE PUESTOS TRAE SUS DOS NOTAS Y LAS DOS SE REGISTRAN, LEIDAS Y NO")
    p.append("PARAFRASEADAS:** %r y %r. Son **%s aislados y %s cotejados**, y **el solape"
             % (m["nota_literal"], m["quemados_literal"], m["aislados"], m["cotejados"]))
    p.append("es TOTAL A PROPOSITO: eso es CONTROL, no cobertura nueva.** Un solape total")
    p.append("no anade puestos al archivo: **mide si dos lectores independientes leen lo")
    p.append("mismo**, que es justo lo que esta tanda tenia que medir.")
    p.append("")
    p.append("### LA DEUDA DE LA SERIE, REMEDIDA AQUI EN VEZ DE HEREDARSE")
    p.append("")
    p.append("Tramo mirado: actas **173 a %d**. **CIFRA actas sin entrada propia en la"
             % (VUELTA_DEL_ACTA - 1))
    p.append("serie: %d** (%s). **Se registra y NO se arregla en esta vuelta**, que es lo"
             % (len(m["salto"][0]),
                ", ".join(str(x) for x in m["salto"][0]) or "ninguna"))
    p.append("que el encargo de la 193 deja escrito en su lista de lo que sigue fuera.")
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


# ---------------------------------------------------------------- LA MUTACION
def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    w("   %-62s %s" % (nombre, "VERDE" if ok else "ROJO"))
    if not ok:
        w("      esperado: %r" % (esperado,))
        w("      obtenido: %r" % (obtenido,))
    return ok


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION DE LO QUE ESTE REGISTRADOR ESTRENA.

    LO QUE PRUEBA, Y POR QUE PUEDE CAER: los tres trozos nuevos son PUROS o
    SEMI-PUROS y se corren sobre texto FABRICADO, con el valor esperado sacado de
    como se fabrico el texto y NO de una constante igual a la obtenida.
    `EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION."""
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("VUELTA 193, TAREA 1: CASO POSITIVO POR MUTACION DEL REGISTRADOR")
    w("=" * 78)
    w("")

    w("A) LAS DOS MARCAS DE ESTADO NUEVAS MUERDEN, Y LAS VIEJAS MANDAN PRIMERO")
    ok &= _caso(w, "un titulo con NO LO CAMBIAN sale contestado",
                estado_de_la_adjudicacion("4.8 `P.1`, si tres cambian el regimen. "
                                          "NO LO CAMBIAN, Y ES EL MISMO DOBLE."),
                "CONTESTADA: EL REGIMEN NO CAMBIA, Y EL DOBLE VA ENCARGADO IGUAL")
    ok &= _caso(w, "un titulo con ADJUDICADO: SE CONGELAN sale bloqueante",
                estado_de_la_adjudicacion("4.10 `P.2`. ADJUDICADO: SE CONGELAN O SE "
                                          "DECLARAN, Y ES BLOQUEANTE DE LA 193."),
                "CONTESTADA Y ENCARGADA COMO BLOQUEANTE")
    w("   LA MUTACION 1: si una marca VIEJA muerde, tiene que mandar ella aunque")
    w("   el titulo traiga ademas una nueva")
    ok &= _caso(w, "EN CONTRA gana a NO LO CAMBIAN en el mismo titulo",
                estado_de_la_adjudicacion("4.9 EN CONTRA, aunque NO LO CAMBIAN"),
                "EN CONTRA")
    w("   LA MUTACION 2: un titulo que no diga ninguna sale SIN DECIR, que es lo")
    w("   que hace PARAR al registrador. Si saliera cualquier otra cosa, un estado")
    w("   ilegible pasaria por bueno")
    ok &= _caso(w, "un titulo mudo sale SIN DECIR",
                estado_de_la_adjudicacion("4.1 `D.1`, una cosa cualquiera."),
                "SIN DECIR")
    w("")

    w("B) EL LEAD DEL AUDITOR EN SINGULAR, SOBRE UNA SECCION 6 FABRICADA")
    w("   (el texto se fabrica aqui con UNA caida de cada lado, asi que el valor")
    w("    esperado sale de la construccion y no de la medicion)")
    fab = [
        "## 6. LAS CAIDAS",
        "",
        "**DEL EJECUTOR: UNA DE REPORTE, Y NO ACUMULA.**",
        "",
        "**`C.1` (DE REPORTE, NO ACUMULA). UNA COSA CUALQUIERA.** Y su cuerpo.",
        "",
        "**MIA: UNA, DE METODO.**",
        "",
        "**`C.1` (DE METODO). OTRA COSA CUALQUIERA.** Y su cuerpo.",
        "",
    ]
    ce_v, ca_v, hu_v = R92.caidas_por_lead_heredado(fab, 1, len(fab))
    ok &= _caso(w, "CON LA MARCA VIEJA el auditor sale con cero", len(ca_v), 0)
    ok &= _caso(w, "y sus dos claves caen del lado del ejecutor", len(ce_v), 2)
    ce_n, ca_n, hu_n = R92.caidas_por_lead_heredado(
        fab, 1, len(fab), marcas_aud=MARCAS_LEAD_AUDITOR_193)
    ok &= _caso(w, "CON LA MARCA NUEVA el reparto sale 1 y 1",
                (len(ce_n), len(ca_n), len(hu_n)), (1, 1, 0))
    w("   LA MUTACION: si la marca nueva no cambiara el reparto, no estaria")
    w("   arreglando nada")
    if (len(ce_v), len(ca_v)) == (len(ce_n), len(ca_n)):
        w("      LA MUTACION NO CAYO: los dos repartos son iguales.")
        ok = False
    else:
        w("      LA MUTACION CAE: %d/%d con la vieja contra %d/%d con la nueva."
          % (len(ce_v), len(ca_v), len(ce_n), len(ca_n)))
    w("   Y LA MUTACION AL REVES: la marca nueva NO puede romper la forma en")
    w("   PLURAL, que es la que usan las actas anteriores")
    fab_plural = list(fab)
    fab_plural[6] = "**MIAS: UNA, DE METODO.**"
    _ce, ca_p, _hu = R92.caidas_por_lead_heredado(
        fab_plural, 1, len(fab_plural), marcas_aud=MARCAS_LEAD_AUDITOR_193)
    ok &= _caso(w, "con MIAS en plural la marca nueva sigue repartiendo bien",
                len(ca_p), 1)
    w("")

    w("C) LAS ASIGNADAS Y LAS CITADAS, SOBRE UNA SECCION 6 FABRICADA CON LAS DOS")
    fab2 = [
        "## 6. LAS CAIDAS",
        "",
        "**DEL EJECUTOR: UNA DE REPORTE.**",
        "",
        "**`C.1` (DE REPORTE). LA ASIGNADA.** Su cuerpo, que no nombra mas claves.",
        "",
        "**UNA NEGRITA QUE NO EMPIEZA POR CLAVE**, y en su cuerpo cita `C.1` a `C.4`.",
        "",
    ]
    asig, cit = caidas_del_ejecutor_repartidas(fab2, 1, len(fab2))
    ok &= _caso(w, "la asignada es UNA y su clave es la 1",
                [(ks) for _a, ks, _e, _n in asig], [[1]])
    ok &= _caso(w, "la citada expande su rango a CUATRO",
                [len(exp) for _a, exp, _e, _n in cit], [4])
    w("   LA MUTACION: si las dos se contaran juntas saldrian %d claves, que es la"
      % (sum(len(k) for _a, k, _e, _n in asig)
         + sum(len(e) for _a, e, _e2, _n in cit)))
    w("   cifra que no corresponde a ninguna fila de la tabla del acta 193")
    junto = (sum(len(k) for _a, k, _e, _n in asig)
             + sum(len(e) for _a, e, _e2, _n in cit))
    if junto == 1 or junto == 4:
        w("      LA MUTACION NO CAYO: juntarlas da lo mismo que separarlas.")
        ok = False
    else:
        w("      LA MUTACION CAE: juntas dan %d, separadas dan 1 y 4." % junto)
    w("   LA MUTACION 2: una seccion SIN parrafo de cita tiene que dar CERO")
    w("   citadas, o el reparto estaria inventando una")
    asig3, cit3 = caidas_del_ejecutor_repartidas(fab2[:6], 1, 6)
    ok &= _caso(w, "sin parrafo de cita, citadas es cero", len(cit3), 0)
    w("")

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

    w("J) EL TITULO, CON SUS CINCO NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(m["n_adj"], m["n_hall"], m["n_preg"],
                                  m["n_aud"], m["n_eje"])
    w("   %s" % titulo)
    w("")

    numero = m["numero"]
    entrada = armar_entrada(numero, titulo, m)
    w("K) LA ENTRADA ARMADA")
    w("   %d bytes | %d lineas por count(NL) | %d por len(split(NL))"
      % (len(entrada.encode("utf-8")), entrada.count(NL), len(entrada.split(NL))))
    w("   guiones largos o medios en la entrada: %d"
      % (entrada.count(chr(8212)) + entrada.count(chr(8211))))
    w("")

    texto_sede = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    if a.simular:
        w("L) MODO --simular: NO SE ESCRIBE NADA EN LA SEDE.")
        w("")
        w("LA ENTRADA, ENTERA:")
        for l in entrada.split(NL):
            w("   | " + l)
    elif m["ya_registrada"]:
        w("L) NO SE ESCRIBE NADA, Y ESTA ES LA IDEMPOTENCIA HACIENDO SU TRABAJO.")
        w("   el acta %d YA TIENE ENTRADA en la serie: %d linea(s) la nombran."
          % (VUELTA_DEL_ACTA, m["ya_registrada"]))
        w("   NO se escribe una entrada nueva y NO se consume el numero R.%d." % numero)
        w("   docs/PENDIENTES.md sigue en %d bytes." % os.path.getsize(SEDE))
    else:
        nuevo = texto_sede.rstrip(NL) + NL + NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("L) ESCRITA EN docs/PENDIENTES.md")
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
