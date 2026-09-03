# -*- coding: utf-8 -*-
"""vuelta160_tarea1_registrar_adjudicaciones.py . TAREA 1 DE LA VUELTA 160.

DEJA ESCRITAS EN EL REPO LAS OCHO ADJUDICACIONES DE LA SECCION 6 DEL ACTA 159,
CADA UNA DONDE VIVE, TODAS POR ADICION Y CON CORRECCION DECLARADA. No borra una
sola linea del texto viejo: cada bloque se ANADE al final del docstring, detras
de los comentarios que ya estaban, o al final del campo del registro.

EL REPARTO ES EL QUE EL ENCARGO NOMBRA, LITERAL:
  6.1   los DOCE .py del alcance del patron de P.16, que son los mismos doce
        que la TAREA 1 de la vuelta 159 ya toco. La letra es que EL ALCANCE SON
        DOCE y que LA VARA ES LA LECTURA B.
  6.2   la razon de `LD-OPC05-004` del registro
        `docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl`
  6.3   la razon de `LD-OPC05-100` del mismo registro
  6.4   el instrumento de lectura del lote
        (scripts/loop/vuelta159_tarea3_lote2.py)
  6.5   scripts/loop/vuelta152_registro_de_citas_opc05.py, donde vive la
        doctrina de vias y clases, Y el instrumento del lote 2
  6.6   la funcion de la P3b de
        scripts/loop/vuelta150_3_relectura_expediente.py
  6.7   el instrumento del lote (scripts/loop/vuelta159_tarea3_lote2.py)
  6.8   scripts/loop/vuelta159_tarea9_marcador_cierre.py

UNA PRECISION SOBRE LA SEDE DE LA 6.4, LA 6.5 Y LA 6.7, DECLARADA EN VEZ DE
CALLADA, Y ES EL MISMO CASO QUE LA VUELTA 159 YA DECLARO: el encargo dice "el
instrumento del lote" y "el instrumento del lote 2", y el instrumento del TRAMO
AL DOBLE (las 37) todavia no existe cuando esta TAREA 1 corre, porque la TAREA 1
va primero por mandato del encargo. Se escribe en el instrumento del lote QUE
EXISTE, `vuelta159_tarea3_lote2.py`, que es el que leyo las 53 del lote 2 y el
que las tres adjudicaciones corrigen; el instrumento del tramo al doble nace en
la TAREA 2 con las tres adjudicaciones ya en su propio docstring.

LA 6.3 NO SE ESCRIBE EN ESTA TAREA Y SE DICE POR QUE, EN VEZ DE CALLARLO: la 6.3
manda `LD-OPC05-100` a RELECTURA CONJUNTA, y su bloque tiene que traer dentro el
VEREDICTO medido contra los nodos, que es la TAREA 2.a. Un bloque escrito aqui,
antes de leer, seria una adjudicacion sin medicion. Se escribe en la TAREA 2.a.

EL ALCANCE DE LA 6.1 NO SE TECLEA, SE RECOMPUTA, Y ADEMAS SE COTEJA CONTRA EL
FICHERO DE SALIDA QUE LO MIDIO. La nomina se computa del codigo (funcion
`ficheros_con_patron_p16`) Y se lee de la seccion C de
`docs/loop/SALIDA_V159_T5_ALCANCE.txt` (funcion `nomina_del_fichero_de_salida`),
y las dos tienen que salir IDENTICAS o el instrumento para. Ninguna de las dos
se teclea aqui.

LOS TRES BUSCADORES SE EXCLUYEN POR NOMBRE Y LA EXCLUSION SE DECLARA. Es la
trampa que `verificar_apertura_sellada.py` lleva escrita desde la vuelta 102 y
que la vuelta 159 volvio a pisar: un buscador del patron CONTIENE el patron
porque tiene que escribirlo para buscarlo. Hoy son tres, no dos:
`vuelta159_tarea1_registrar_adjudicaciones.py`,
`vuelta159_tarea5_alcance_p16.py` y ESTE MISMO FICHERO.

LA ADITIVIDAD SE MIDE, NO SE PROMETE (como en la 154, la 156, la 157 y la 159):
para los .py se corre `git diff --numstat` y se exige BORRADOS 0; para el JSONL
se comprueba POR ASSERT que el texto viejo de cada campo tocado sigue siendo
PREFIJO LITERAL del texto nuevo, y sobre las 154 entradas y no solo las tocadas.

ES IDEMPOTENTE: si el bloque ya esta escrito (se busca su marca literal), no lo
duplica y lo dice.

USO:  python scripts/loop/vuelta160_tarea1_registrar_adjudicaciones.py
"""
import io
import json
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
LOOP = os.path.join(RAIZ, "scripts", "loop")
SALIDA_ALCANCE = os.path.join(RAIZ, "docs", "loop", "SALIDA_V159_T5_ALCANCE.txt")

MARCA = "ADJUDICACION %s DEL ACTA 159"

PATRON_P16 = '"--porcelain", "--", "dataset/'

BUSCADORES = (
    "vuelta159_tarea1_registrar_adjudicaciones.py",
    "vuelta159_tarea5_alcance_p16.py",
    "vuelta160_tarea1_registrar_adjudicaciones.py",
)


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)


def ficheros_con_patron_p16():
    """LA NOMINA DE LA 6.1, RECOMPUTADA Y NO TECLEADA (lectura B del acta 159:
    pathspec que empieza por `dataset/`). Los tres buscadores se descartan POR
    NOMBRE, no por contenido, para que ningun fichero legitimo pueda quedar
    fuera por parecerse."""
    salida = []
    for nombre in sorted(os.listdir(LOOP)):
        if not nombre.endswith(".py") or nombre in BUSCADORES:
            continue
        try:
            texto = leer(os.path.join(LOOP, nombre))
        except (IOError, UnicodeDecodeError):
            continue
        if PATRON_P16 in texto:
            salida.append("scripts/loop/" + nombre)
    return salida


def nomina_del_fichero_de_salida():
    """LA MISMA NOMINA, CONTADA DE SU FICHERO (EJECUTOR.md 1, "LA TABLA SE
    CUENTA DE SU FICHERO"). Lee la seccion C de SALIDA_V159_T5_ALCANCE.txt, que
    es el fichero que midio el alcance y con el que el acta 159 lo adjudico."""
    dentro = False
    salida = []
    for linea in leer(SALIDA_ALCANCE).splitlines():
        if linea.startswith("C) LA NOMINA PRINCIPAL"):
            dentro = True
            continue
        if dentro:
            if linea.strip().startswith("CIFRA") or linea.startswith("D)"):
                break
            campos = linea.split()
            if campos and campos[0].endswith(".py"):
                salida.append("scripts/loop/" + campos[0])
    return sorted(salida)


def insertar_en_docstring(ruta_rel, bloque, marca):
    """Inserta BLOQUE justo antes del cierre del docstring DE MODULO. El texto
    viejo no se toca: el bloque queda al final, detras de todo lo anterior."""
    ruta = os.path.join(RAIZ, ruta_rel)
    texto = leer(ruta)
    if marca in texto:
        return "YA ESTABA", 0
    ini = texto.index('"""')
    fin = texto.index('"""', ini + 3)
    escribir(ruta, texto[:fin] + bloque + texto[fin:])
    return "ANADIDO", len(bloque.splitlines())


def insertar_tras_docstring_de_funcion(ruta_rel, nombre_def, bloque, marca):
    """Inserta BLOQUE como comentario DESPUES del docstring de UNA FUNCION y
    DESPUES de los bloques de comentario que otras vueltas ya dejaron ahi, para
    que el orden del fichero siga siendo cronologico. Comentario y no docstring
    por el motivo que la vuelta 157 midio: el docstring de `p3b_caso_positivo`
    cierra con tres comillas PEGADAS a su ultima linea de texto, asi que
    insertar dentro obligaria a re escribir esa linea, y una linea modificada es
    una linea borrada para `git diff --numstat`, que exige CERO."""
    ruta = os.path.join(RAIZ, ruta_rel)
    texto = leer(ruta)
    if marca in texto:
        return "YA ESTABA", 0
    i = texto.index("def %s(" % nombre_def)
    ini = texto.index('"""', i)
    fin = texto.index('"""', ini + 3) + 3
    salto = texto.index("\n", fin) + 1
    while True:
        fin_linea = texto.find("\n", salto)
        if fin_linea < 0:
            break
        linea = texto[salto:fin_linea]
        if linea.strip() == "" or linea.lstrip().startswith("#"):
            salto = fin_linea + 1
            continue
        break
    escribir(ruta, texto[:salto] + bloque + texto[salto:])
    return "ANADIDO", len(bloque.splitlines())


def entradas():
    return [json.loads(x) for x in leer(REGISTRO).splitlines() if x.strip()]


def guardar_entradas(E):
    with io.open(REGISTRO, "w", encoding="utf-8", newline="\n") as fh:
        for e in E:
            fh.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")


def numstat(ruta_rel):
    r = subprocess.run(["git", "diff", "--numstat", "--", ruta_rel],
                       cwd=RAIZ, capture_output=True)
    linea = r.stdout.decode("utf-8", "replace").strip()
    if not linea:
        return 0, 0
    campos = linea.split("\t")
    return int(campos[0]), int(campos[1])


def ld_de(e):
    return e["cita"].split(",")[0].strip()


# --------------------------------------------------------------------------
# 6.1, EN LOS DOCE FICHEROS DEL ALCANCE
# --------------------------------------------------------------------------

B61_DOC = """
--- ADJUDICACION 6.1 DEL ACTA 159 (3 sep 2026): EL ALCANCE DEL CHECK DE P.16 SON
DOCE, NO ONCE, Y LA VARA ES LA LECTURA B ---

CORRECCION DECLARADA POR ADICION. Nada de lo escrito arriba se borra, y en
particular NO SE BORRA la cifra ONCE que la adjudicacion 6.7 del acta 158 dejo
escrita: se corrige delante de ella para que la correccion se pueda auditar.

LA CIFRA VIEJA Y LA NUEVA, LAS DOS ESCRITAS. El acta 158 midio ONCE ficheros de
`scripts/loop/` con el patron literal del check de P.16 y su encargo mando parar
si la cuenta no daba once. La vuelta 159 recomputo y dio DOCE, paro por mandato
literal y NO TOCO UN SOLO CHECK. EL ACTA 159 ADJUDICA QUE SON DOCE Y QUE LA
CIFRA EQUIVOCADA ERA LA DEL ACTA, o sea la del auditor: lo midio el en dos
arboles distintos, el del commit del acta 158 y HEAD, y los dos dan 4 / 12 / 14
ficheros y 3 / 7 / 7 dentro de la bateria de las 23. EL ONCE NUNCA FUE CIERTO, y
la diferencia no la introdujo ninguna vuelta.

LA VARA DE LA LECTURA ES LA B, Y SE NOMBRA PARA QUE NO VUELVA A DERIVAR: B MEDIA
es "pathspec que empieza por dataset/", que es la que el ejecutor publico como
principal y la que la 6.7 del acta 158 sostiene al describir el defecto por su
instrumento. LA LECTURA ESTRECHA DE CUATRO (dataset/ Y docs/plan/ a la vez) NO
VALE, porque el defecto no depende de que el pathspec traiga tambien docs/plan/.

EL DUODECIMO ENTRA Y TIENE NOMBRE: `vuelta89_tarea4_guarda_op_c05.py`. Es del
mismo defecto que la serie 142 a 147, solo que mas viejo, y lleva las dos anclas
que la 6.7 describe (la del fin de linea y la de la suciedad anterior al
arranque), leidas por el auditor en su fuente. NO HAY MOTIVO DE VARA PARA
EXCLUIRLO.

LO QUE ESTO OBLIGA: la 5.a y la 5.c del encargo de la vuelta 159 se ejecutan
sobre LOS DOCE, no sobre once ni sobre cuatro. La nomina no se teclea: se
recomputa, y su medicion esta pegada en `docs/loop/SALIDA_V159_T5_ALCANCE.txt`.
"""

# --------------------------------------------------------------------------
# 6.2, EN LA RAZON DE LA FILA QUE NOMBRA
# --------------------------------------------------------------------------

B62_RAZON = (
    "  [ADJUDICACION 6.2 DEL ACTA 159 (2026-09-03), ANADIDA SIN BORRAR NADA DE "
    "LO ANTERIOR: ESTA FILA SE QUEDA EN D Y LA DISCREPANCIA ES DEL AUDITOR, NO "
    "DEL EJECUTOR. Su relectura ciega dio C tomando como segunda linea el paso "
    "3 del tune-up (ajusta tus hipotesis de ingresos segun los segmentos que "
    "mostraron entusiasmo) expandido por los pasos 1 a 3 de reempaquetado. "
    "DESTAPADO EL CASO, ESA ES EXACTAMENTE LA PAREJA QUE LA SEGUNDA PASADA DE "
    "LA VUELTA 159 YA HABIA NOMBRADO COMO EL PAR MAS FUERTE DESCARTADO Y YA "
    "HABIA DESCARTADO POR ESCRITO, porque reempaquetado es UN REMEDIO HERMANO, "
    "una de varias clases de pivote, y contesta QUE CAMBIAR y no COMO se "
    "ajustan las hipotesis de ingresos. El auditor adjudica D, que es la clase "
    "escrita, y registra la discrepancia como caida de lectura SUYA. NINGUNA "
    "CLASE SE MUEVE. Y esto es la 6.3 del acta 158 haciendo su trabajo: el par "
    "que convencio al lector de fuera ya estaba examinado y descartado por "
    "escrito antes de que lo mirara.]")

# --------------------------------------------------------------------------
# 6.4, EN EL INSTRUMENTO DE LECTURA DEL LOTE
# --------------------------------------------------------------------------

B64_DOC = """
--- ADJUDICACION 6.4 DEL ACTA 159 (3 sep 2026): EL CREDITO DE LA TANDA BAJA Y EL
LOTE 2 SE RELEE AL DOBLE. SON 37 SEGUNDAS LECTURAS Y VAN ENTERAS ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra, y en particular NO SE
BORRA el veredicto de CATORCE SOSTIENEN LA C Y TREINTA Y NUEVE BAJAN A D que
este instrumento publico: la segunda pasada se escribe delante de el.

EL MOTIVO ES LITERAL Y NO TIENE EXCEPCION: una discrepancia FUERA de los
discutibles marcados baja el credito de TODA la tanda y el tramo se relee al
doble. `LD-OPC05-100` esta fuera de los doce marcados de la vuelta 159.

LA CIFRA, COMPUTADA POR EL AUDITOR Y NO TECLEADA
(`docs/loop/_auditor_v159_tramo_al_doble.txt`): el lote 2 son 53; de esas releyo
el auditor 16, que son los cinco marcados que caen dentro del lote (078, 081,
084, 103, 116) mas los once de su muestra por computo (070, 075, 080, 085, 090,
095, 100, 105, 110, 115, 120); 53 menos 16 da 37, de las cuales 8 estan hoy en C
y 29 en D. EL INSTRUMENTO DEL TRAMO RECOMPUTA ESA NOMINA Y LA PUBLICA: si no da
37, para y lo dice ANTES de leer nada.

Y VAN LAS 37 ENTERAS, NO SOLO LAS QUE CAYERON A D, Y EL MOTIVO ESTA ESCRITO: la
discrepancia que abrio la bajada, la `100`, es una que SOSTUVO C, asi que
restringir el tramo a las caidas dejaria fuera justo la especie que lo disparo.

LA VARA ES LA MISMA Y NO SE AFLOJA: segunda pasada independiente bajo la 6.3 del
acta 158 (la pregunta binaria es un EXISTENCIAL y la razon nombra el par mas
fuerte descartado), con correccion declarada y el texto viejo entero como
prefijo, `n` sin moverse en 3.388, assert de frontera con sha256 de `dataset/` y
conteo de censo y aristas antes y despues (EL REGISTRO CAMBIA, EL GRAFO NO), y
Gate 0 con el ciclo entero al terminar. Y EL LIMITE DE LA 6.1 DEL ACTA 155 SIGUE
VIGENTE: LA QUE SALGA A NO SE VOLTEA; se marca como discutible, se publica su
caso y NO SE EJECUTA NINGUNA FUSION.
"""

# --------------------------------------------------------------------------
# 6.5, EN LA DOCTRINA Y EN EL INSTRUMENTO DEL LOTE 2
# --------------------------------------------------------------------------

B65_DOC = """
--- ADJUDICACION 6.5 DEL ACTA 159 (3 sep 2026): UNA INSTANCIA NO ES EL
PROCEDIMIENTO DE SU CATEGORIA. ADJUDICADA, Y NO ES DOCTRINA NUEVA ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

LA REGLA, TAL COMO EL EJECUTOR LA FORMULO EN EL LOTE 2 DE LA VUELTA 159 Y TAL
COMO EL ACTA 159 LA ADJUDICA: cuando la linea de un nodo dice "aplica tecnicas
graficas", "mapea tus fuentes de ingresos" o "consolida los planes
subsidiarios", y el otro nodo ES UNA de esas tecnicas, uno de esos patrones o
uno de esos planes, ESO NO ES EXPANSION: es un ejemplar de la categoria.

POR QUE NO ES DOCTRINA NUEVA Y POR ESO NO HUBO PARADA: una regla escrita la
cubre por extension citable. La 6.4 del acta 157 pregunta si el otro nodo es EL
COMO SE HACE de una linea; un ejemplar de una categoria es el QUE, no el COMO, y
por eso no la expande. Y la 6.4 del acta 158, en la `122`, ya escribio la forma
general: NOMBRAR SIN PROCEDIMENTAR ES EXACTAMENTE LO QUE LA 6.4 EXCLUYE.

LAS DOS CONDICIONES CON QUE SE ADJUDICA, Y LAS DOS SON OBLIGATORIAS:
  (a) CUANDO SEA EL UNICO MOTIVO DEL DESCARTE, la razon lo dice con esa letra y
      marca la fila como DISCUTIBLE, como ya se hizo en la `078` y la `103`.
  (b) SU CONSISTENCIA SE AUDITA EN LA SEGUNDA PASADA DE LA 6.4, sobre las 37: en
      cada una, si la regla APLICA se dice; y si NO aplica pudiendo parecer que
      si, TAMBIEN se dice, y se publica el conteo de las dos cosas. EL RIESGO DE
      UNA REGLA NUEVA NO ES APLICARLA MAL UNA VEZ, ES APLICARLA SOLO CUANDO
      CONVIENE.
"""

# --------------------------------------------------------------------------
# 6.6, EN LA FUNCION DE LA P3b
# --------------------------------------------------------------------------

B66_FUN = """    # --- ADJUDICACION 6.6 DEL ACTA 159 (3 sep 2026): LAS FICHAS DE LAS DOS
    # SALIDAS NO SE REESCRIBEN, Y LO QUE SI VA ES LA LECCION DEL ANGULO BARATO
    # ---
    #
    # REGISTRO POR ADICION. Nada de lo escrito arriba se borra.
    #
    # LO QUE NO VA, Y SE DICE PRIMERO PARA QUE NADIE LO VUELVA A ENCARGAR: las
    # fichas de `SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt` y de
    # `SALIDA_V136_3D_MUTACION.txt` NO SE REESCRIBEN. Medido por el auditor
    # (`docs/loop/_auditor_v159_productores.txt`) y recomputado por el ejecutor
    # en la TAREA 5 de la vuelta 160: las dos salidas se citan en CUATRO
    # lugares y en LOS CUATRO el nombre del productor ya esta en la misma cita
    # o en su misma frase partida por el ancho de columna
    # (`docs/plan/04_ENLACES.md:445` y `docs/plan/OPERACIONES.jsonl:45` nombran
    # `verificar_cobertura_bolsa_tres_vias.py`; `OPERACIONES.jsonl:36` nombra
    # `verificar_fuente_canonico.py`; `docs/PENDIENTES.md:6241` lo nombra dos
    # lineas arriba dentro del mismo parentesis). LA 6.9 DEL ACTA 158 PEDIA QUE
    # LA FICHA LO CITARA Y YA LO CITA. CIFRA fichas que hay que reescribir: 0.
    #
    # LO QUE SI VA, Y ES LA LECCION QUE HABRIA AHORRADO DOS VUELTAS: EL ANGULO
    # BARATO ERA LEER LA FICHA QUE CITA LA SALIDA, donde el productor llevaba
    # meses escrito al lado. Ni el barrido de 998 `.py` de la vuelta 157 ni los
    # cuatro angulos de la vuelta 159 (nombre del fichero, texto literal, los
    # `.py` de los commits, y la cabecera literal) lo miraron. LOS CUATRO
    # ANGULOS BUSCAN AL PRODUCTOR DESDE LA SALIDA; EL BARATO LO BUSCA DESDE
    # QUIEN LA CITA. Cuando una salida parezca huerfana, ESE ES EL PRIMER
    # ANGULO, no el ultimo: cuesta un grep sobre `docs/plan/` y no depende de
    # que el productor escriba su cabecera sin interpolar.
"""

# --------------------------------------------------------------------------
# 6.7, EN EL INSTRUMENTO DEL LOTE
# --------------------------------------------------------------------------

B67_DOC = """
--- ADJUDICACION 6.7 DEL ACTA 159 (3 sep 2026): LAS 18 EN C NO SE DAN POR
CERRADAS, Y LA 6.4 YA CONTESTA CUALES ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra, y en particular NO SE
BORRA la conclusion de la vuelta 159 de que el saco de lectura quedaba vacio: se
corrige delante de ella.

EL REPARTO DE LAS 18, ADJUDICADO POR EL ACTA 159 Y ESCRITO AQUI PARA QUE NO HAYA
QUE VOLVER A DECIDIRLO:
  CUATRO quedan CERRADAS porque tienen dos lecturas independientes cada una:
      `LD-OPC05-005`, `038`, `049` y `052`.
  OCHO caen dentro de las 37 del tramo al doble y SE RELEEN AHI.
  SEIS las releyo el auditor a ciegas en la vuelta 159: `095`, `100`, `110`,
      `081`, `084` y `116`, con la `100` en disputa y mandada a relectura
      conjunta por la 6.3.

LO QUE ESTO OBLIGA: NO HACE FALTA UNA PASADA APARTE PARA EL SACO. La 6.4 lo
cubre entero, y una pasada aparte solo repetiria lecturas ya hechas.
"""

# --------------------------------------------------------------------------
# 6.8, EN EL INSTRUMENTO DEL MARCADOR DE CIERRE
# --------------------------------------------------------------------------

B68_DOC = """
--- ADJUDICACION 6.8 DEL ACTA 159 (3 sep 2026): ESTE INSTRUMENTO SE PARAMETRIZA.
UN INSTRUMENTO QUE NACE PARA QUE LA CIFRA TENGA PRODUCTOR VIVO NO PUEDE OBLIGAR
A ESCRIBIR OTRO EL MES QUE VIENE ---

CORRECCION DECLARADA POR ADICION. Nada de lo escrito arriba se borra.

QUE SE CONFIRMA PRIMERO, PORQUE ES LO QUE JUSTIFICA QUE ESTE FICHERO EXISTA: el
auditor corrio `git log --all -S` sobre la cabecera de
`SALIDA_V157_T9_MARCADOR_CIERRE.txt` y NO DEVUELVE NADA en `scripts/`, ni vivo
ni muerto. Aquella salida era de un solo uso y el reporte de la vuelta 159 lo
dice bien.

EL AGUJERO DE CONSTRUCCION, HALLADO POR EL AUDITOR SOBRE ESTE MISMO REMEDIO
(acta 159, seccion 5.2): este fichero imprimia `"VUELTA 159, CIERRE: ..."`
LITERAL, sin `--vuelta` y sin `argparse`. En la vuelta 160 o mentia en su propia
cabecera o obligaba a que naciera otro instrumento de un solo uso, QUE ES
EXACTAMENTE EL DEFECTO QUE ESTE VINO A CERRAR. No es caida de reporte: el
reporte nunca afirmo que estuviera parametrizado.

EL REMEDIO, EJECUTADO EN LA TAREA 4 DE LA VUELTA 160: toma `--vuelta` y el
rotulo se interpola. El literal viejo queda en este registro y no en el codigo.
"""


def main():
    print("=" * 78)
    print("VUELTA 160, TAREA 1: LAS OCHO ADJUDICACIONES DEL ACTA 159")
    print("=" * 78)
    print("")

    print("A) EL ALCANCE DE LA 6.1, POR DOS VIAS INDEPENDIENTES")
    print("   patron literal buscado en el CODIGO (lectura B): %s" % PATRON_P16)
    print("   EXCLUSION DECLARADA: se descartan por nombre los TRES buscadores")
    print("   que contienen el patron porque tienen que escribirlo para buscarlo:")
    for b in BUSCADORES:
        print("      %s" % b)
    p16 = ficheros_con_patron_p16()
    print("   A.1 RECOMPUTADO DEL CODIGO, CIFRA ficheros: %d" % len(p16))
    fichero = nomina_del_fichero_de_salida()
    print("   A.2 CONTADO DE SU FICHERO (docs/loop/SALIDA_V159_T5_ALCANCE.txt,")
    print("       seccion C), CIFRA ficheros: %d" % len(fichero))
    for r in p16:
        print("      %s" % r)
    print("   CIFRA que el acta 158 (6.7) declaraba: 11")
    print("   CIFRA que el acta 159 (6.1) adjudica: 12")
    assert p16 == fichero, ("LAS DOS NOMINAS NO COINCIDEN.\n  codigo: %s\n  fichero: %s"
                            % (p16, fichero))
    print("   LAS DOS VIAS DAN LA MISMA NOMINA, ELEMENTO A ELEMENTO.")
    assert len(p16) == 12, "EL ALCANCE NO DA DOCE: da %d" % len(p16)
    print("   Y DA DOCE, que es lo que la 6.1 adjudica.")
    print("")

    E = entradas()
    clases_antes = {ld_de(e): e["clase"] for e in E}
    antes_razon = {ld_de(e): e["razon"] for e in E}

    ops = []

    print("B) LOS BLOQUES, UNO A UNO, TODOS POR ADICION")
    for ruta in p16:
        ops.append(("6.1", ruta) + insertar_en_docstring(ruta, B61_DOC, MARCA % "6.1"))

    lote = "scripts/loop/vuelta159_tarea3_lote2.py"
    ops.append(("6.4", lote) + insertar_en_docstring(lote, B64_DOC, MARCA % "6.4"))

    for ruta in ("scripts/loop/vuelta152_registro_de_citas_opc05.py", lote):
        ops.append(("6.5", ruta) + insertar_en_docstring(ruta, B65_DOC, MARCA % "6.5"))

    ops.append(("6.7", lote) + insertar_en_docstring(lote, B67_DOC, MARCA % "6.7"))

    p3b = "scripts/loop/vuelta150_3_relectura_expediente.py"
    ops.append(("6.6", p3b) + insertar_tras_docstring_de_funcion(
        p3b, "p3b_caso_positivo", B66_FUN, MARCA % "6.6"))

    marcador = "scripts/loop/vuelta159_tarea9_marcador_cierre.py"
    ops.append(("6.8", marcador) + insertar_en_docstring(marcador, B68_DOC, MARCA % "6.8"))

    for e in E:
        if ld_de(e) != "LD-OPC05-004":
            continue
        if (MARCA % "6.2") in e["razon"]:
            ops.append(("6.2", "registro:LD-OPC05-004", "YA ESTABA", 0))
        else:
            e["razon"] = e["razon"] + B62_RAZON
            ops.append(("6.2", "registro:LD-OPC05-004", "ANADIDO", 1))
    guardar_entradas(E)

    for etiqueta, ruta, estado, n in ops:
        print("   %-5s %-58s %-10s %s" % (etiqueta, ruta, estado, n or ""))
    print("   6.3   registro:LD-OPC05-100                                   "
          "DIFERIDA A LA TAREA 2.a")
    print("         (manda a RELECTURA CONJUNTA: su bloque lleva el veredicto")
    print("          medido contra los nodos, y aqui todavia no hay medicion)")
    print("")
    print("CIFRA operaciones de escritura de esta corrida: %d" % len(ops))
    print("CIFRA de ellas ANADIDAS: %d" % sum(1 for o in ops if o[2] == "ANADIDO"))
    print("CIFRA de ellas YA ESTABAN: %d" % sum(1 for o in ops if o[2] == "YA ESTABA"))
    print("CIFRA adjudicaciones diferidas a otra tarea de esta misma vuelta: 1")
    print("")

    py_tocados = sorted({o[1] for o in ops if o[1].endswith(".py")})

    print("C) LA ADITIVIDAD, MEDIDA Y NO PROMETIDA")
    print("   C.1 LOS .py, con git diff --numstat (se exige BORRADOS 0):")
    total_borrados = 0
    for ruta in py_tocados:
        mas, menos = numstat(ruta)
        total_borrados += menos
        print("       %-58s mas %-5d menos %d" % (ruta, mas, menos))
    print("   CIFRA ficheros .py tocados: %d" % len(py_tocados))
    print("   CIFRA borrados en los .py tocados: %d" % total_borrados)
    assert total_borrados == 0, "SE BORRO UNA LINEA DE UN .py: la aditividad esta rota"
    print("       CERO BORRADOS: ninguna linea vieja se toco.")
    print("")

    D = entradas()
    assert len(D) == len(E) == 154, "el numero de lineas del registro se movio"
    rotos = [ld_de(d) for d in D if not d["razon"].startswith(antes_razon[ld_de(d)])]
    print("   C.2 EL JSONL, por assert de prefijo sobre las %d entradas:" % len(D))
    print("       CIFRA razones cuyo texto viejo YA NO ES PREFIJO: %d" % len(rotos))
    assert not rotos, "PREFIJO ROTO en: %s" % ", ".join(rotos)
    print("       PREFIJO INTACTO en las %d." % len(D))

    movidas = [ld_de(d) for d in D if d["clase"] != clases_antes[ld_de(d)]]
    print("   C.3 CIFRA clases movidas por esta tarea: %d" % len(movidas))
    assert not movidas, "esta tarea NO mueve ninguna clase"
    print("       NINGUNA. La relectura conjunta va en la TAREA 2, no aqui.")

    pares_antes = {tuple(sorted(e["par"])) for e in E}
    pares_desp = {tuple(sorted(d["par"])) for d in D}
    assert pares_antes == pares_desp, "esta tarea NO mueve ningun par"
    print("   C.4 PARES: %d pares, los mismos antes y despues" % len(pares_desp))
    print("")

    r = subprocess.run(["git", "diff", "--numstat", "--", "docs/plan/"],
                       cwd=RAIZ, capture_output=True)
    print("   C.5 numstat de docs/plan/:")
    for l in r.stdout.decode("utf-8", "replace").strip().splitlines():
        print("       %s" % l)
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
