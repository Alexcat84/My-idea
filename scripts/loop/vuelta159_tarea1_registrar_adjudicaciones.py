# -*- coding: utf-8 -*-
"""vuelta159_tarea1_registrar_adjudicaciones.py . TAREA 1 DE LA VUELTA 159.

DEJA ESCRITAS EN EL REPO LAS DOCE ADJUDICACIONES DE LA SECCION 6 DEL ACTA 158,
CADA UNA DONDE VIVE, TODAS POR ADICION Y CON CORRECCION DECLARADA. No borra una
sola linea del texto viejo: cada bloque se ANADE al final del docstring, detras
de los comentarios que ya estaban, o al final del campo del registro.

EL REPARTO ES EL QUE EL ENCARGO NOMBRA, LITERAL:
  6.1 y 6.2   scripts/loop/verificar_apertura_sellada.py Y
              scripts/loop/tallar_cabecera_reporte.py, que es donde vive el
              invariante ACTA N, VUELTA N MAS 1
  6.3         scripts/loop/vuelta152_registro_de_citas_opc05.py, donde vive la
              doctrina de vias y clases, Y el instrumento de lectura del lote
              (scripts/loop/vuelta157_tarea2_lote1_veredictos.py)
  6.4 y 6.5   la razon de LD-OPC05-005, LD-OPC05-027 y LD-OPC05-122 del
              registro docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl
  6.6         el instrumento que escribe el campo `cita`: nace en
              scripts/loop/vuelta152_registro_de_citas_opc05.py y las dos
              formas divergentes las escribieron
              scripts/loop/vuelta156_tarea2b_decidir_ld097.py y
              scripts/loop/vuelta157_tarea2_lote1_veredictos.py. Va en los tres,
              porque el hecho que la 6.6 corrige vive repartido en los tres.
  6.7         los .py que llevan el patron literal del check de P.16
  6.8         scripts/loop/verificar_re_sellado.py
  6.9 y 6.10  la funcion de la P3b de
              scripts/loop/vuelta150_3_relectura_expediente.py
  6.11        scripts/loop/vuelta157_tarea8_dos_especies_de_d.py, el instrumento
              de la TAREA 8 de la vuelta 157
  6.12        el instrumento del lote
              (scripts/loop/vuelta157_tarea2_lote1_veredictos.py)

UNA PRECISION SOBRE LA SEDE DE LA 6.3 Y DE LA 6.12, DECLARADA EN VEZ DE
CALLADA: el encargo dice "el instrumento del lote", y el instrumento del lote 2
todavia no existe cuando esta TAREA 1 corre (la TAREA 1 va primero por mandato
del encargo). Se escribe en el instrumento del lote QUE EXISTE,
`vuelta157_tarea2_lote1_veredictos.py`, que es el que aplico el lote 1 y el que
la 6.3 corrige; y el instrumento del lote 2 nace en la TAREA 3 con las dos
adjudicaciones ya en su propio docstring.

EL ALCANCE DE LA 6.7 NO SE TECLEA, SE RECOMPUTA. El acta dice ONCE ficheros. El
computo de esta vuelta da DOCE (funcion `ficheros_con_patron_p16`). El bloque se
escribe en LOS DOCE MEDIDOS, no en once tecleados, y la discrepancia se publica
en la salida y en el reporte. Escribir la adjudicacion en un fichero de mas es
aditivo y no rompe nada; dejarlo fuera seria dejar sin marca un fichero que
lleva el patron.

LA ADITIVIDAD SE MIDE, NO SE PROMETE (como en la 154, la 156 y la 157): para los
.py se corre `git diff --numstat` y se exige BORRADOS 0; para el JSONL se
comprueba POR ASSERT que el texto viejo de cada campo tocado sigue siendo
PREFIJO LITERAL del texto nuevo, y sobre las 154 entradas y no solo las tocadas.

ES IDEMPOTENTE: si el bloque ya esta escrito (se busca su marca literal), no lo
duplica y lo dice.

USO:  python scripts/loop/vuelta159_tarea1_registrar_adjudicaciones.py
"""
import io
import json
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
LOOP = os.path.join(RAIZ, "scripts", "loop")

MARCA = "ADJUDICACION %s DEL ACTA 158"

PATRON_P16 = '"--porcelain", "--", "dataset/'


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)


def ficheros_con_patron_p16():
    """LA NOMINA DE LA 6.7, RECOMPUTADA Y NO TECLEADA. Devuelve la lista
    ordenada de ficheros de scripts/loop/ cuyo CODIGO invoca
    `git status --porcelain` con un pathspec que empieza por `dataset/`, que es
    el patron literal que el acta 158 describe en su 6.7.

    ESTE INSTRUMENTO SE EXCLUYE A SI MISMO, Y LA EXCLUSION SE DECLARA EN VEZ DE
    CALLARSE. Es la misma trampa que `verificar_apertura_sellada.py` ya lleva
    escrita desde la vuelta 102 ("la guarda que se envenena sola"): el buscador
    de un patron CONTIENE el patron que busca, porque tiene que escribirlo para
    buscarlo. La primera corrida de esta vuelta lo demostro: dio TRECE, y el
    decimotercero era el propio fichero. Se descarta POR NOMBRE, no por
    contenido, para que ningun fichero legitimo pueda quedar fuera por
    parecerse."""
    yo = os.path.basename(os.path.abspath(__file__))
    salida = []
    for nombre in sorted(os.listdir(LOOP)):
        if not nombre.endswith(".py") or nombre == yo:
            continue
        ruta = os.path.join(LOOP, nombre)
        try:
            texto = leer(ruta)
        except (IOError, UnicodeDecodeError):
            continue
        if PATRON_P16 in texto:
            salida.append("scripts/loop/" + nombre)
    print("   EXCLUSION DECLARADA: se descarta el propio instrumento, %s, que"
          % yo)
    print("   contiene el patron porque tiene que escribirlo para buscarlo.")
    return salida


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
    que el orden del fichero siga siendo cronologico.

    POR QUE COMENTARIO Y NO DENTRO DEL DOCSTRING, Y ESTO YA LO APRENDIO LA
    VUELTA 157 CON SU PROPIA GUARDA DE ADITIVIDAD: el docstring de
    `p3b_caso_positivo` cierra con tres comillas PEGADAS a su ultima linea de
    texto, asi que insertar dentro obligaba a re escribir esa linea, y una linea
    modificada es una linea borrada para `git diff --numstat`, que exige CERO."""
    ruta = os.path.join(RAIZ, ruta_rel)
    texto = leer(ruta)
    if marca in texto:
        return "YA ESTABA", 0
    i = texto.index("def %s(" % nombre_def)
    ini = texto.index('"""', i)
    fin = texto.index('"""', ini + 3) + 3
    salto = texto.index("\n", fin) + 1
    # se salta todo lo que ya sea comentario o linea en blanco, para quedar
    # DETRAS de los bloques que otras vueltas dejaron aqui
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
# 6.1 y 6.2, EN LAS DOS GUARDAS QUE LLEVAN EL INVARIANTE ESCRITO
# --------------------------------------------------------------------------

B61_DOC = """
--- ADJUDICACION 6.1 DEL ACTA 158 (3 sep 2026): LA VUELTA QUE ABRE UN ACTA N SE
NUMERA N MAS 1, Y ESA ARITMETICA ES LA DE ESTA GUARDA ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

EL INVARIANTE, QUE ESTA GUARDA YA LLEVABA ESCRITO Y QUE AHORA QUEDA DICHO CON SU
NOMBRE: la apertura de la vuelta N es el commit del acta de la vuelta N MENOS 1.
Dicho al reves, que es como se lee desde fuera: EL ACTA N ABRE LA VUELTA N MAS 1.

QUE PASO Y POR QUE NO FUE CAIDA DE NADIE (acta 158, seccion 4, medido con
`git log` sobre la rama): el invariante se cumplio sin excepcion en todo el
tramo (acta 149 abre la 150, acta 151 la 152, acta 153 la 154, acta 155 la 156).
El acta 157 abria la vuelta 158, pero el encargo de aquella vuelta NUNCA dijo
que numero de vuelta tocaba, solo de que acta venia; el ejecutor numero la suya
157 igualando su vuelta al numero del acta, y esta guarda y
`tallar_cabecera_reporte.py` se quedaron las dos ciegas buscando un
"ACTA DE LA VUELTA 156" que no existe.

EL REMEDIO NO ES DE CODIGO Y ESTA GUARDA NO SE TOCA: desde el acta 158 EL
ENCARGO LLEVA EL NUMERO DE VUELTA EN SU CABECERA FIJA, junto al rotulo de hashes
admitidos. La aritmetica de esta guarda era la correcta y sigue igual.
"""

B62_DOC = """
--- ADJUDICACION 6.2 DEL ACTA 158 (3 sep 2026): EL SELLO DE APERTURA TARDIO ES
CAIDA DE PROCEDIMIENTO, NO DE CIFRA, Y SU REMEDIO YA ESTABA CONSTRUIDO: ES ESTA
GUARDA, DESBLOQUEADA ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

EL HECHO. En la vuelta 157 el valor de la apertura no fue falso (es re derivable
de git, y el auditor lo re derivo: `git rev-parse 23004b4d^` da `abb2fe4e`),
pero `SALIDA_V157_HEAD_APERTURA.txt` no se sello hasta el cierre. La regla que
se incumplio ya existe, y su guarda es esta.

LO QUE ESTE CASO DEJA ESCRITO, Y VALE PARA CUALQUIER GUARDA DE LA CASA: EN LA
MISMA VUELTA EN QUE ESTA GUARDA QUEDO CIEGA PASO EXACTAMENTE EL FALLO QUE
VIGILA. Una guarda bloqueada no es un evento neutro. No hay que construir nada:
desbloqueada, muerde.
"""

# --------------------------------------------------------------------------
# 6.3, EN LA DOCTRINA Y EN EL INSTRUMENTO DE LECTURA DEL LOTE
# --------------------------------------------------------------------------

B63_DOC = """
--- ADJUDICACION 6.3 DEL ACTA 158 (3 sep 2026): LA PREGUNTA BINARIA DE LA 6.4 ES
UN EXISTENCIAL. SE HACE SOBRE TODOS LOS PARES DE LINEAS CANDIDATOS, NO SOBRE EL
PRIMERO QUE SE ENCUENTRE ---

CORRECCION DECLARADA POR ADICION, y NO ES DOCTRINA NUEVA: es la letra de la 6.4
del acta 157 leida entera. La 6.4 pregunta si SE PUEDEN nombrar dos lineas
distintas, y eso es un existencial: basta con que EXISTA UN PAR que cumpla.

LA CONSECUENCIA, QUE ES LO QUE AL LOTE 1 LE FALTO: hallar un par de lineas que
colapsa en la misma linea prueba que ESE PAR no es la figura, NO que no la haya.
El colapso del 9.22 descarta un par, no un nodo.

LA REGLA DE ESCRITURA QUE SE ADJUDICA, Y ES OBLIGATORIA DESDE LA PRIMERA LECTURA
DEL LOTE 2: cuando el colapso del 9.22 sea el motivo del descarte, la razon
tiene que decir TAMBIEN que NINGUN otro par de lineas sostiene la figura, y
NOMBRAR el par mas fuerte que se descarto.

EL CASO QUE LA ORIGINA, PARA QUE NO SE LEA COMO UNA REGLA SIN CUERPO
(`LD-OPC05-005`, acta 158 seccion 3.1): la razon del lote 1 descarto la figura
porque el paso 1 de `aim_of_leadership` y el paso 13 de
`causas_comunes_vs_especiales` son la misma linea, y para ESE par tenia razon.
Pero habia otro par disponible: el paso 2 de aim (investigar las causas de raiz
DEL SISTEMA) contra el paso 13 de causas, cada uno expandido por procedimientos
del otro nodo. Un existencial no se refuta con un caso.
"""

# --------------------------------------------------------------------------
# 6.4 y 6.5, EN LAS RAZONES DE LAS TRES EN DISPUTA
# --------------------------------------------------------------------------

B64_RAZON = (
    "  [ADJUDICACION 6.4 DEL ACTA 158 (2026-09-03), ANADIDA SIN BORRAR NADA DE "
    "LO ANTERIOR: ESTA LECTURA QUEDA EN DISPUTA Y VA A RELECTURA CONJUNTA. La "
    "ciega del auditor discrepa de la clase escrita y su caso esta en las "
    "secciones 3 y 3.1 del acta 158. LA ADJUDICACION NO LA DECIDE LA PLUMA DEL "
    "AUDITOR: el ejecutor verifica contra los nodos y decide con la vara, "
    "incluso contra el, y publica lo que mida. MI LECTURA NO ES LA VARA, EL "
    "NODO LO ES. El veredicto de la relectura conjunta se anade detras de este "
    "corchete, en la TAREA 2.a de la vuelta 159, sin borrar esto.]")

B65_RAZON = (
    "  [ADJUDICACION 6.5 DEL ACTA 158 (2026-09-03), ANADIDA SIN BORRAR NADA DE "
    "LO ANTERIOR: EL CREDITO DE LA TANDA DE LA VUELTA 157 BAJA Y EL TRAMO SE "
    "RELEE AL DOBLE. El motivo es literal y no tiene excepcion para un fallo de "
    "metodo interesante: LD-OPC05-005 es una discrepancia FUERA de los "
    "discutibles marcados, o sea una lectura que el ejecutor hizo y no marco. "
    "El tramo es el lote 1, y releerlo al doble significa que las 41 lecturas "
    "que cayeron a D y que nadie ha vuelto a mirar reciben una segunda pasada "
    "independiente bajo la 6.3. Esta fila es una de las tres en disputa que "
    "abren esa relectura.]")

# --------------------------------------------------------------------------
# 6.6, EN LOS TRES INSTRUMENTOS QUE ESCRIBEN EL CAMPO cita
# --------------------------------------------------------------------------

B66_DOC = """
--- ADJUDICACION 6.6 DEL ACTA 158 (3 sep 2026): EL CAMPO `cita` SE UNIFICA EN
UNA SOLA FORMA, Y GANA LA QUE NO TAPA ---

CORRECCION DECLARADA POR ADICION, y toca el campo `cita` del registro
`docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl`. Nada de lo escrito arriba se borra.

EL HECHO, MEDIDO POR EL AUDITOR COMPARANDO EL REGISTRO DE `abb2fe4e` CONTRA HEAD
(acta 158, seccion 5.1): en la vuelta 157 cambiaron 62 campos `cita`, y
cambiaron POR SOBREESCRITURA (`'LD-OPC05-001, clase C'` paso a
`'LD-OPC05-001, clase D'`, sin dejar el texto viejo). Pero las TRES que la
vuelta 156 reclasifico dicen otra cosa EN EL MISMO FICHERO
(`'LD-OPC05-002, clase C  [RECLASIFICADA A D EN LA VUELTA 156: ver la razon]'`).
DOS FORMAS PARA EL MISMO HECHO, EN EL MISMO FICHERO, EN DOS VUELTAS SEGUIDAS. Y
ademas esas tres hoy leen literalmente "clase C" en una fila cuya clase es D.

LO QUE SE ADJUDICA, POR EXTENSION DE LA 6.8 DEL ACTA 157 (la costumbre de la
casa, no tapar lo que se corrige) Y DE LA LEY DE UNA SOLA FUENTE: UNA SOLA FORMA
para las 65 filas corregidas, la que lleva la clase VIGENTE Y el rastro:

    clase D [ANTES C, RECLASIFICADA EN LA VUELTA N: ver la razon]

Con eso las 62 recuperan el rastro que la sobreescritura les quito y las 3 de la
vuelta 156 dejan de leer "clase C" en una fila que es D. Se hace POR ADICION,
con correccion declarada, y con el assert de que NINGUNA clase se mueve al
hacerlo y de que el conteo de pares del registro sale identico antes y despues.
Se ejecuta en la TAREA 4 de la vuelta 159.

NINGUNA CIFRA PUBLICADA ERA FALSA POR ESTO y el acta lo dice: la razon declara
la correccion en las 62 y ningun reporte afirmo nada sobre las citas. Lo que se
corrige es que la del 156 tapa menos y la del 157 tapa mas.
"""

# --------------------------------------------------------------------------
# 6.7, EN LOS .py QUE LLEVAN EL PATRON DEL CHECK DE P.16
# --------------------------------------------------------------------------

B67_DOC = """
--- ADJUDICACION 6.7 DEL ACTA 158 (3 sep 2026): EL CHECK DE P.16 SE CINE AL
CONTENIDO Y A LA VENTANA DEL PROPIO SCRIPT ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra, y el check que este
fichero lleva NO se modifica al escribir esto: esto es la adjudicacion, no el
remedio.

LAS DOS ANCLAS QUE SE MUEVEN EN LA MISMA LINEA, y el hallazgo es del ejecutor de
la vuelta 157, que lo trajo como pregunta en vez de esquivarlo callando. El
docstring dice que se comprueba que `dataset/` y `docs/plan/` NO SE TOCAN NI UNA
VEZ, o sea CONTENIDO. El instrumento es `git status --porcelain`, que ademas de
contenido ve:
  (i)  ESTADO DE FIN DE LINEA. Este repo tiene `core.autocrlf`, asi que un
       fichero reescrito por el ciclo queda marcado como modificado aunque su
       sha256 NORMALIZADO sea identico al de HEAD. Paso de verdad en la vuelta
       157 y tumbo tres mutaciones de la bateria en ROJO con el contenido
       intacto.
  (ii) SUCIEDAD ANTERIOR AL ARRANQUE DEL SCRIPT, que no es suya. El veredicto de
       este check depende de si alguien committeo tocando `dataset/` antes, y no
       de si las mutaciones de este fichero tocaron el dataset.

EL REMEDIO ADJUDICADO: huella de CONTENIDO tomada ANTES y DESPUES de las
mutaciones DENTRO del propio script, y comparada consigo misma. Con su caso
positivo por mutacion: si una mutacion escribe de verdad en `dataset/` o en
`docs/plan/`, el check SIGUE SALIENDO ROJO.

EL ALCANCE, Y AQUI HAY UNA DISCREPANCIA DE CIFRA QUE SE DECLARA EN VEZ DE
COPIARSE: el acta 158 mide ONCE ficheros con el patron literal, siete de ellos
dentro de la bateria de las 23. El recomputo de la vuelta 159
(`scripts/loop/vuelta159_tarea1_registrar_adjudicaciones.py`, funcion
`ficheros_con_patron_p16`, salida `docs/loop/SALIDA_V159_T1_ADJUDICACIONES.txt`)
da DOCE ficheros, y los SIETE de la bateria reproducen exactamente. El duodecimo
es `scripts/loop/vuelta89_tarea4_guarda_op_c05.py`: excluirlo devuelve los once
del acta al digito. La cifra de la vuelta 159 es la del computo, y por eso el
remedio de la 6.7 queda EN PARADA, declarada en el reporte de la vuelta 159.
"""

# --------------------------------------------------------------------------
# 6.8, EN LA GUARDA DE RE SELLADO
# --------------------------------------------------------------------------

B68_DOC = """
--- ADJUDICACION 6.8 DEL ACTA 158 (3 sep 2026): ESTA GUARDA NO PUEDE ACUSAR A SU
PROPIA SALIDA ---

CORRECCION DECLARADA POR ADICION. Nada de lo escrito arriba se borra.

EL HECHO, MEDIDO POR EL AUDITOR CORRIENDO ESTA GUARDA (acta 158, seccion 5.2):
sobre el reporte en HEAD sale ROJO exit 1 acusando
`SALIDA_V157_T9_CIFRAS_REPORTE.txt` y `SALIDA_V157_T9_RE_SELLADO.txt`, y lo
verifico con `git diff --numstat b166ab47 HEAD` (2 y 2 sobre el primero, 24 y 22
sobre el segundo).

Y EL MOTIVO ES DE CONSTRUCCION, NO DE DICTADO: esta guarda compara cada salida
citada contra su commit de tarea, y EL COMMIT QUE PUBLICA EL REPORTE RE ESCRIBE
NECESARIAMENTE la salida de esta misma guarda y la del verificador de cifras,
porque las dos se re corren sobre el reporte final. NINGUN REPORTE PUEDE DEJARLA
VERDE EN HEAD. Exigir al ejecutor una afirmacion que expira al commitearla seria
exigir lo imposible, y el acta lo dice con esas palabras: NO ES CAIDA SUYA.

EL REMEDIO ADJUDICADO: esta guarda EXIME de la comparacion los ficheros que ella
misma y el verificador de cifras escriben sobre el reporte final (o compara
contra el commit del reporte en vez de contra HEAD), Y PUBLICA ESA EXENCION COMO
LINEA COMPUTADA CON LOS NOMBRES EXENTOS. Una exencion que no se imprime es un
agujero; una que se imprime es una vara con su limite dicho. Con su caso
positivo por mutacion: un fichero de tarea NORMAL re sellado y no declarado
TIENE QUE SEGUIR SALIENDO ROJO.
"""

# --------------------------------------------------------------------------
# 6.9 y 6.10, EN LA FUNCION DE LA P3b
# --------------------------------------------------------------------------

B69_FUN = """    # --- ADJUDICACION 6.9 DEL ACTA 158 (3 sep 2026): LAS DOS SALIDAS SIN
    # PRODUCTOR SE BUSCAN EN LA HISTORIA DE GIT Y DESPUES SE DECLARAN, NO SE
    # RETIRAN A CIEGAS ---
    #
    # REGISTRO POR ADICION. Nada de lo de arriba se borra ni se suaviza.
    #
    # EL HECHO. La vuelta 157 barrio 998 `.py` POR SU TEXTO y no hallo productor
    # de `SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt` ni de
    # `SALIDA_V136_3D_MUTACION.txt`, las dos citadas por fichas cuya P3b se
    # sostiene en ellas. El acta concede que el barrido fue correcto y senala
    # que le faltaba un angulo barato y decisivo: LA HISTORIA DE GIT, porque un
    # productor pudo MORIR o CAMBIAR DE NOMBRE y un barrido del arbol de hoy no
    # lo ve.
    #
    # LO ADJUDICADO. Se busca con `git log --all -S` sobre el texto de cada
    # salida. Si aparece, se nombra el productor y la ficha lo cita. Si no
    # aparece, la cita queda declarada ARTEFACTO HUERFANO junto a la funcion,
    # con esa letra, igual que ya se hizo con el proxy sin respaldo efectivo.
    # LA CITA NO SE BORRA: SE MARCA. Se ejecuta en la TAREA 7 de la vuelta 159.
"""

B610_FUN = """    # --- ADJUDICACION 6.10 DEL ACTA 158 (3 sep 2026): LAS DOS PRUEBAS DE
    # MUTACION QUE NO MUERDEN. SE LEE EL ROJO ANTES DE TOCAR NADA ---
    #
    # REGISTRO POR ADICION. Nada de lo de arriba se borra ni se suaviza.
    #
    # EL HECHO, CONFIRMADO POR EL AUDITOR CORRIENDOLAS EL:
    # `vuelta96_tarea3_prueba_mutacion.py` sale exit 1 y
    # `vuelta97_tarea2_prueba_mutacion.py` sale exit 1. Las dos sostienen la P3b
    # de `OP-E-03`, o sea que su rojo toca justo a esta funcion.
    #
    # LO ADJUDICADO, POR EL PRECEDENTE DE LOS CASOS DECLARADOS DE LA BATERIA: se
    # lee POR QUE cae cada una ANTES de tocar nada. Si el rojo delata una
    # REGRESION REAL de la guarda que nombra, ES HALLAZGO y se trae. Si es una
    # EXPECTATIVA ENVEJECIDA sobre un sujeto congelado, se declara CASO
    # DECLARADO con su motivo escrito y su marca obligatoria.
    #
    # LO QUE NO SE HACE, Y ES LA CAIDA QUE ESTA CAMPANA PERSIGUE DESDE EL
    # PRINCIPIO: AJUSTAR LA EXPECTATIVA HASTA QUE SALGA VERDE. Se ejecuta en la
    # TAREA 8 de la vuelta 159.
"""

# --------------------------------------------------------------------------
# 6.11, EN EL INSTRUMENTO DE LA TAREA 8 DE LA 157
# --------------------------------------------------------------------------

B611_DOC = """
--- ADJUDICACION 6.11 DEL ACTA 158 (3 sep 2026): LA CUENTA DE LAS DOS ESPECIES
DE D SE CIERRA AQUI, Y SIN LETRA NUEVA. ESTE INSTRUMENTO NO SE VUELVE A CORRER
COMO ENCARGO ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

QUE MIDIO ESTE INSTRUMENTO Y COMO LO JUZGA EL ACTA: su vara lexica cazo UNO de
los CINCO puestos que el acta nombro, y dejo el 71,9 por ciento del registro y
el 96,6 por ciento del archivo en SIN MARCA. EL EJECUTOR PUBLICO ESO EN VEZ DE
RETOCAR LAS MARCAS HASTA QUE SALIERA, y el acta lo dice con todas sus letras:
ES EXACTAMENTE LO QUE SE LE PIDIO.

LO ADJUDICADO: LA CUENTA CUMPLIO SU ENCARGO Y NO SE REPITE. Lo que dejo medido
es util y se escribe con su limite: LA ESPECIE EXISTE EN LOS DOS REGISTROS, ES
UNA COTA INFERIOR, Y UNA VARA LEXICA NO LA PUEDE MEDIR; SOLO UNA LECTURA.

LO QUE QUEDA PROHIBIDO Y POR QUE: NO SE ABRE LETRA NUEVA (seria doctrina nueva y
seria parada) y NO SE ENCARGA UNA SEGUNDA PASADA LEXICA, que solo repetiria el
mismo residuo. HILO CERRADO.
"""

# --------------------------------------------------------------------------
# 6.12, EN EL INSTRUMENTO DEL LOTE
# --------------------------------------------------------------------------

B612_DOC = """
--- ADJUDICACION 6.12 DEL ACTA 158 (3 sep 2026): EL LOTE 2 VA, CON LA 6.3 PUESTA
DESDE LA PRIMERA LECTURA ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

EL LOTE 2 SON 53, de `LD-OPC05-068` a `LD-OPC05-121`, y NINGUNA trae puntero de
paso: el saco pequeno se agoto entero en el lote 1. LA NOMINA NO SE TECLEA: la
recomputa su instrumento, como se hizo con la del lote 1, y si no da 53 se para
y se dice ANTES de leer nada.

EL CRITERIO ES EL MISMO DE LA 6.4 DEL ACTA 157, con la unica correccion de la
6.3 del acta 158, que es lo que el lote 1 enseno: la pregunta es un existencial,
asi que cuando el colapso del 9.22 sea el motivo del descarte, la razon tiene
que decir TAMBIEN que ningun otro par de lineas sostiene la figura, y NOMBRAR el
par mas fuerte que se descarto.

LAS GUARDAS SON LAS MISMAS Y NO SE AFLOJAN: correccion declarada con el texto
viejo entero como prefijo, `n` no se mueve y sigue en 3.388, assert de frontera
con sha256 de `dataset/` y conteo de censo y aristas antes y despues (EL
REGISTRO CAMBIA, EL GRAFO NO), Gate 0 al terminar, y LA QUE SALGA A NO SE
VOLTEA.
"""


def main():
    print("=" * 78)
    print("VUELTA 159, TAREA 1: LAS DOCE ADJUDICACIONES DEL ACTA 158")
    print("=" * 78)
    print("")

    print("A) EL ALCANCE DE LA 6.7, RECOMPUTADO ANTES DE ESCRIBIR NADA")
    print("   patron literal buscado en el CODIGO: %s" % PATRON_P16)
    p16 = ficheros_con_patron_p16()
    print("   CIFRA ficheros de scripts/loop/ con el patron: %d" % len(p16))
    for r in p16:
        print("      %s" % r)
    print("   CIFRA que el acta 158 (6.7) declara: 11")
    if len(p16) != 11:
        print("   DISCREPANCIA DECLARADA: el computo da %d y el acta dice 11."
              % len(p16))
        print("   Se escribe en LOS %d MEDIDOS. La cifra se publica en el reporte."
              % len(p16))
    print("")

    E = entradas()
    clases_antes = {ld_de(e): e["clase"] for e in E}
    antes_razon = {ld_de(e): e["razon"] for e in E}

    ops = []

    print("B) LOS BLOQUES, UNO A UNO, TODOS POR ADICION")
    for ruta in ("scripts/loop/verificar_apertura_sellada.py",
                 "scripts/loop/tallar_cabecera_reporte.py"):
        ops.append(("6.1", ruta) + insertar_en_docstring(ruta, B61_DOC, MARCA % "6.1"))
        ops.append(("6.2", ruta) + insertar_en_docstring(ruta, B62_DOC, MARCA % "6.2"))

    for ruta in ("scripts/loop/vuelta152_registro_de_citas_opc05.py",
                 "scripts/loop/vuelta157_tarea2_lote1_veredictos.py"):
        ops.append(("6.3", ruta) + insertar_en_docstring(ruta, B63_DOC, MARCA % "6.3"))

    for ruta in ("scripts/loop/vuelta152_registro_de_citas_opc05.py",
                 "scripts/loop/vuelta156_tarea2b_decidir_ld097.py",
                 "scripts/loop/vuelta157_tarea2_lote1_veredictos.py"):
        ops.append(("6.6", ruta) + insertar_en_docstring(ruta, B66_DOC, MARCA % "6.6"))

    for ruta in p16:
        ops.append(("6.7", ruta) + insertar_en_docstring(ruta, B67_DOC, MARCA % "6.7"))

    ops.append(("6.8", "scripts/loop/verificar_re_sellado.py")
               + insertar_en_docstring("scripts/loop/verificar_re_sellado.py",
                                       B68_DOC, MARCA % "6.8"))

    p3b = "scripts/loop/vuelta150_3_relectura_expediente.py"
    ops.append(("6.9", p3b) + insertar_tras_docstring_de_funcion(
        p3b, "p3b_caso_positivo", B69_FUN, MARCA % "6.9"))
    ops.append(("6.10", p3b) + insertar_tras_docstring_de_funcion(
        p3b, "p3b_caso_positivo", B610_FUN, MARCA % "6.10"))

    t8 = "scripts/loop/vuelta157_tarea8_dos_especies_de_d.py"
    ops.append(("6.11", t8) + insertar_en_docstring(t8, B611_DOC, MARCA % "6.11"))

    lote = "scripts/loop/vuelta157_tarea2_lote1_veredictos.py"
    ops.append(("6.12", lote) + insertar_en_docstring(lote, B612_DOC, MARCA % "6.12"))

    tres = ("LD-OPC05-005", "LD-OPC05-027", "LD-OPC05-122")
    for e in E:
        ld = ld_de(e)
        if ld not in tres:
            continue
        for etiqueta, bloque in (("6.4", B64_RAZON), ("6.5", B65_RAZON)):
            if (MARCA % etiqueta) in e["razon"]:
                ops.append((etiqueta, "registro:" + ld, "YA ESTABA", 0))
                continue
            e["razon"] = e["razon"] + bloque
            ops.append((etiqueta, "registro:" + ld, "ANADIDO", 1))
    guardar_entradas(E)

    for etiqueta, ruta, estado, n in ops:
        print("   %-5s %-58s %-10s %s" % (etiqueta, ruta, estado, n or ""))
    print("")
    print("CIFRA operaciones de escritura de esta corrida: %d" % len(ops))
    print("CIFRA de ellas ANADIDAS: %d" % sum(1 for o in ops if o[2] == "ANADIDO"))
    print("CIFRA de ellas YA ESTABAN: %d" % sum(1 for o in ops if o[2] == "YA ESTABA"))
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
