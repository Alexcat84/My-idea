# -*- coding: utf-8 -*-
r"""verificar_ausencias_del_reporte.py . LA TERCERA ESCALADA (TAREA 2 de la
vuelta 146, encargada por `AUDITOR.md` 1.2 al llegar la racha de reporte a DOS
tandas seguidas, acta de la vuelta 145, seccion 5).

NOMBRE ESTABLE, SIN NUMERO DE VUELTA, como sus dos hermanas mayores
`tallar_cabecera_reporte.py` y `verificar_cifras_del_reporte.py`.

POR QUE NACE, Y POR QUE NO BASTABA CON LO QUE YA HABIA. La escalada del 26 ago
2026 (toda tabla y toda cifra del reporte contada de su fichero) esta
construida y corriendo: es `verificar_cifras_del_reporte.py`, y en la vuelta
145 salio verde con 8 de 8. NO CUBRE LA ESPECIE QUE FALLO EN LA 145, y el
motivo es mecanico: aquella guarda coteja CIFRAS contra el fichero que las
cuenta, y UNA AUSENCIA NO TIENE FICHERO QUE CONTAR. El reporte de la vuelta 145
publico, en su 3.c, "no existe en el repositorio ninguna lista canonica de
libros con sus alias de escritura" y de ahi saco `PRERREQUISITO CUMPLIDO: NO` y
el bloqueo de la fase 07. Existia: `docs/plan/OP_S_11_MAPEO_PROPUESTO.md`, y su
operacion duena `OP-S-11` esta HECHA desde el 29 ago. El metodo, escrito en la
propia salida de aquella vuelta: "candidatos mirados: <tres rutas>",
"hallados: NINGUNO". TRES RUTAS TECLEADAS A MANO, CERO BUSQUEDA POR CONTENIDO.

NO ES DOCTRINA NUEVA. `EJECUTOR.md` 9 dice desde hace vueltas "una busqueda
negativa no se puede citar", y el propio reporte de la 145 LA CITA en su
discutible 10 y LA INCUMPLE en la misma pagina. Es la caida 4.2 de la casa del
acta 145: una regla que se puede citar y romper a la vez es prosa, no guarda.
Esto es la guarda que la hace morder. Registrada como CORRECCION 23.

--- LA FRONTERA, PRIMERO, PORQUE ES LO QUE MAS FACIL SE LEE DE MAS ---

ESTA GUARDA NO DECIDE SI LA COSA EXISTE. Decide si LA AFIRMACION ESTA
RESPALDADA POR UN BARRIDO QUE PUDO HABERLA HALLADO. Esa segunda mitad de la
frase es lo que la vuelta 147 le anade y es toda la escalada: hasta la 146
bastaba con que EXISTIERA un barrido con su sello; desde la 147, ese barrido
tiene ademas que HABER TENIDO PODER PARA ENCONTRAR LA COSA, o sea que al menos
una de las cadenas que busco por contenido exista en alguna parte del universo.
Sigue sin decidir el HECHO: un reporte que diga "no existe X" con un barrido
exhaustivo, sellado y CON PODER detras pasa aunque X exista, y un reporte que
diga "no existe X" sin barrido cae aunque X de verdad no exista. LO QUE SE
VIGILA ES EL METODO, NO EL HECHO.

Y NO ENTRA EN NINGUNA COLUMNA DE `tallar_estado_de_fase.py`, por la misma razon
de unidades de la adjudicacion 3.9 del acta 144 y de la CORRECCION 18: aquella
tabla mide DESTINO CONTRA EL GRAFO, y esto mide RESPALDO DE UNA AFIRMACION. Dos
unidades no comparten columna.

--- EL VOCABULARIO DE DISPARO, CERRADO Y DECLARADO ---

Lo elige el ejecutor y se escribe aqui entero para que la proxima ampliacion
sea un acto declarado y no una adivinanza del instrumento (misma doctrina que
`VERBOS_DE_CIERRE` en la guarda de cifras). Dispara una frase que traiga
cualquiera de estas formas, sin distinguir mayusculas:

    no existe / no existen / no hay ningun / no hay ninguna
    hallados: NINGUNO / hallado: NINGUNO / no se hallo / no se halla
    no esta en el repositorio / NO INSTALADO / NO INSTALADOS
    PRERREQUISITO CUMPLIDO: NO

Y LAS OCHO QUE SE SUMAN EN LA VUELTA 147 (TAREA 2.a de la ESCALADA DE LA
ESCALADA), con su motivo MEDIDO y no supuesto: el acta 146 midio el escape de
las doce de arriba sobre el propio reporte de la 146 y publico SEIS
afirmaciones de ausencia coladas enteras; REMEDIDO EN LA 147 SOBRE EL MISMO
SUJETO CONGELADO (`723b4639:docs/loop/REPORTE.md`) SALEN CINCO, y la propia
cifra de cobertura del acta (de 3 vistas a 8) es la que cuadra con CINCO y no
con seis. La discrepancia se declara y no se resuelve copiando
(`EJECUTOR.md` 2). UNA DE ELLAS LLEVABA DENTRO LA
AFIRMACION FALSA DEL UMBRAL (la cabecera de la PREGUNTA 2, *"EL UMBRAL DE LA
COLA NO TIENE NUMERO EN NINGUNA PARTE"*), que es literalmente la caida 4.2 de
esa acta. La familia que se escapaba es la del VERBO DE TENENCIA y la del
LUGAR:

    no tiene / no tienen / no da un numero
    no halla ningun / no halla ninguna
    no trae ningun / no trae ninguna
    en ninguna parte

LA AMPLIACION ES UN ACTO DECLARADO Y NO UNA ADIVINANZA DEL INSTRUMENTO: se
escribe aqui entera, como se escribieron las doce, y su efecto se MIDE y se
publica en el reporte de la vuelta que la instala, sobre sujetos CONGELADOS por
ref, no sobre el arbol vivo.

LA GUARDA DISPARA DE MAS A PROPOSITO, igual que su hermana: el coste de un
disparo de mas es UNA CITA de barrido, y el coste de un disparo de menos fue la
caida 4.1 del acta 145. **EL REMEDIO DE UN ROJO DE ESTA CLASE ES CORRER EL
BARRIDO, JAMAS REESCRIBIR LA PROSA HASTA QUE LA GUARDA NO ENCUENTRE NADA**, que
es el ramal (xxi) del acta 136: una cobertura de cero no es un verde, es un
plato vacio.

--- QUE CUENTA COMO BARRIDO EXHAUSTIVO, ESCRITO Y NO ADIVINADO ---

La afirmacion tiene que CITAR EN SU VENTANA un `docs/loop/SALIDA_V<N>_*.txt`
EXISTENTE que traiga el SELLO COMPLETO que imprime `barrer_ausencia.py`, y
desde la vuelta 147 son SEIS piezas, todas obligatorias:

  (1) la marca literal `BARRIDO EXHAUSTIVO`
  (2) `PREGUNTA:` con texto (que ausencia respalda ese barrido)
  (3) `UNIVERSO:` con texto (de donde sale el universo)
  (4) `CARDINAL:` con un numero MAYOR QUE CERO (un universo vacio no es un
      universo: es un barrido que no barrio nada)
  (5) `POR CONTENIDO:` (la segunda pierna). ESTA ES LA PIEZA QUE MAS IMPORTA:
      es exactamente la que faltaba el dia de la caida. Un barrido de una sola
      pierna, por nombre, NO PUEDE hallar un fichero que se llama por su
      operacion duena.
  (6) LA VITALIDAD DE LA PIERNA POR CONTENIDO (vuelta 147, TAREA 2.b): al
      menos UNA de las alternativas de primer nivel del patron de contenido
      tiene que APARECER EN EL UNIVERSO. Su motivo entero, su criterio y su
      limite estan escritos en el docstring de `barrer_ausencia.py`, seccion LA
      SEXTA PIEZA DEL SELLO, y no se repiten aqui para que no haya dos
      versiones de la misma doctrina.
      LOS SELLOS ANTERIORES A LA 147 NO CAEN POR VIEJOS: si no publican la
      linea de vitalidad, esta guarda LA RECOMPUTA, con el mismo instrumento y
      SOBRE EL ARBOL DEL COMMIT DEL SELLO cuando se la juzga congelada
      (`--sello-ref`). Medir un sello viejo contra el arbol de HOY da falsos
      verdes, y esta medido: los tres identificadores muertos del barrido del
      umbral de la 146 salen VIVOS hoy porque el docstring que documenta la
      caida los escribe.

Y HAY UN ROJO CON NOMBRE PROPIO: si el fichero citado trae `candidatos
mirados:` y NO trae la marca `BARRIDO EXHAUSTIVO`, la guarda cae nombrando ESE
patron, porque es literalmente el metodo de la caida de la 145. Una lista de
rutas candidatas escritas a mano NO ES UN BARRIDO.

--- LA VENTANA, Y POR QUE ESTA ES BIDIRECCIONAL ---

La ventana es LA MISMA FRASE mas HASTA DOS FRASES ANTES y HASTA DOS DESPUES.
SE DECLARA LA DIFERENCIA CON LA GUARDA DE CIFRAS, que para COTEJAR usa
forward-only por doctrina adjudicada (acta 135, 3.1): alli ensanchar dejaria
que una cifra cuadrara contra el fichero DEL VECINO, y aqui NO HAY NADA QUE
CUADRAR. La pregunta de esta guarda es BINARIA (hay o no hay barrido sellado
respaldando esta frase) y en la prosa de estos reportes la cita del barrido
PRECEDE casi siempre a la conclusion que introduce ("Barrido en `SALIDA_X`:
no existe ninguna..."), asi que una ventana solo-adelante seria
estructuralmente incapaz de aprobar la escritura natural.

LO QUE SE PAGA POR ENSANCHAR, DICHO EN VOZ ALTA Y NO ESCONDIDO: una frase de
ausencia PODRIA apoyarse en el barrido del vecino. Lo que lo mitiga, y por eso
`PREGUNTA:` es obligatoria en el sello: el barrido tiene que declarar QUE
ausencia respalda, asi que el prestamo queda ESCRITO y visible en la salida que
la guarda imprime. Queda MARCADO COMO DISCUTIBLE en el reporte de la vuelta
146, no zanjado por mi.

--- LO QUE SE RECORTA ANTES DE PARSEAR, Y POR QUE ESO NO ES UNA PUERTA DE
SERVICIO ---

UN REPORTE QUE DOCUMENTA LA CAIDA TIENE QUE PODER CITARLA. El reporte de la
vuelta 146 cita verbatim la frase de la 3.c de la 145 (es su tarea 1.b), y esa
frase dispara este vocabulario. Si no hubiera manera de citar, la guarda
obligaria a esconder justo el texto que hay que auditar, que es lo contrario de
`EJECUTOR.md` 8.

LA SALIDA NO ES UN INTERRUPTOR QUE ESCRIBE EL AUDITADO, y esta es la leccion de
la vuelta 135 ("una exencion que escribe el auditado no es una exencion, es un
interruptor"). Un bloque de cita se delimita asi:

    <!-- CITA CONGELADA <ref>:<ruta> -->
    ...texto citado...
    <!-- FIN CITA CONGELADA -->

y LA GUARDA LO COMPRUEBA ELLA MISMA: lee el blob de ese ref con `git show` y
exige que CADA LINEA del bloque que dispara el vocabulario aparezca, VERBATIM y
tras quitar el adorno de markdown, dentro de ese blob. Una linea que no este en
el ref es ROJO NOMBRANDOLA. No se puede meter texto propio en un bloque de
cita: solo cabe lo que ya esta commiteado en el commit citado. Es el mismo
patron que la vara de citas de la vuelta 145, la que se para con la cita
muerta.

Las marcas siguen la regla de las tres de la guarda de cifras: con las dos se
quita lo delimitado, sin ninguna no se quita nada, y con UNA SOLA es ROJO.

--- LA EXENCION DECLARADA, PARA LA FRASE QUE NO HABLA DEL REPOSITORIO
(TAREA 2.4 de la vuelta 148) ---

POR QUE NACE. La caida 4.2 del acta 147: la vuelta 147 REESCRIBIO DOS FRASES
para callar un rojo de esta guarda. El motivo era legitimo (la guarda dispara
sobre prosa que no afirma NADA sobre el repositorio: un falso positivo) y el
ejecutor lo declaro en vez de esconderlo, pero LAS DOS FRASES ORIGINALES NO
VIVEN EN NINGUN BLOB, asi que su "dicen exactamente lo mismo" es incomprobable.
El auditor pidio una de dos salidas: un bloque de exencion declarada, o la
frase vieja pegada al lado de la nueva. NUNCA UNA REESCRITURA SIN RASTRO.

LA FORMA:

    <!-- EXENCION DECLARADA: <motivo, en una linea> -->
    ...la frase que no afirma nada sobre el repositorio...
    <!-- FIN EXENCION DECLARADA -->

Y AQUI ESTA LO QUE IMPIDE QUE SEA UN INTERRUPTOR (leccion de la vuelta 135,
"una exencion que escribe el auditado no es una exencion, es un interruptor").
LA GUARDA COMPRUEBA ELLA MISMA QUE LO EXIMIDO DE VERDAD NO HABLA DEL
REPOSITORIO: si dentro del bloque aparece CUALQUIER cosa que apunte al repo (una
ruta `docs/`, `scripts/`, `dataset/`, `web/`, `engine/`, `packs/`, un nombre de
fichero con extension conocida, o un `SALIDA_V<N>_...`), LA EXENCION SE RECHAZA
Y ES ROJO NOMBRANDO LO QUE APARECIO. Una frase que nombra un fichero SI afirma
algo sobre el repositorio, y esa necesita barrido como cualquier otra.

Ademas: el motivo NO PUEDE IR VACIO, valen las tres reglas de marcas de la casa
(con las dos se quita, sin ninguna no se quita nada, con una sola es ROJO), y
CADA EXENCION USADA SE IMPRIME en la salida con su motivo, para que se vea
cuantas hay y de que. Una exencion invisible seria peor que el rojo que evita.

LA FRONTERA: esto NO exime de barrido a ninguna afirmacion sobre el repo. Lo
unico que hace es dar salida al falso positivo, con rastro, en vez de empujar a
reescribir la frase y perder el original.

TAMBIEN SE RECORTAN los bloques `<!-- COMMITS TALLADOS -->` y
`<!-- CABECERA TALLADA -->`, por el mismo motivo por el que la guarda de cifras
los recorta: sus lineas son ASUNTOS DE COMMIT y CELDAS TALLADAS DE
INSTRUMENTOS, no prosa del reporte, y dentro de una lista de commits o de una
tabla tallada no hay donde poner una cita. LA CABECERA SE SUMO EN LA PRIMERA
CORRIDA DE ESTA GUARDA SOBRE UN REPORTE REAL (vuelta 146, 4.c) y se dice por
que no la debilita: la celda de identidad de la cabecera trae el ASUNTO DEL
COMMIT DEL ACTA leido de `git log`, y ese asunto puede contener cualquier
formula del vocabulario sin que sea una afirmacion de quien escribe el reporte;
ademas `tallar_cabecera_reporte.py --comparar` ya exige que ese bloque sea
IDENTICO AL TALLADOR, o sea que no cabe meter ahi una frase propia.

--- CERO AFIRMACIONES VISTAS NO ES VERDE ---

Si la guarda recorre el reporte y no encuentra NINGUNA afirmacion de ausencia,
lo dice y sale VERDE con su COBERTURA en cero, PERO NOMBRANDOLO: "0 vistas" es
un dato, no un aprobado, y se imprime igual de grande que un verde lleno. NO se
sale en rojo por ello, a diferencia de la guarda de cifras, y la razon es que
un reporte sin ninguna afirmacion de ausencia es perfectamente posible y
legitimo (la mayoria de las vueltas del cribado no publicaban ninguna),
mientras que un reporte sin NINGUNA cifra no lo es.

PRUEBA DE MUTACION (obligatoria, `EJECUTOR.md` 1, "EL CASO ROJO SE PRUEBA POR
MUTACION", y sobre SUJETO CONGELADO por la CORRECCION 22):
`scripts/loop/vuelta146_2b_mutacion_ausencias.py`, salida a
`docs/loop/SALIDA_V146_2B_MUTACION_AUSENCIAS.txt`.

USO:
  python scripts/loop/verificar_ausencias_del_reporte.py
  python scripts/loop/verificar_ausencias_del_reporte.py --reporte RUTA
  python scripts/loop/verificar_ausencias_del_reporte.py --ref a9b638ba
"""
import argparse
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
RUTA_REPORTE = os.path.join(LOOP, "REPORTE.md")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verificar_cifras_del_plan import dividir_frases  # noqa: E402
# UNA SOLA IMPLEMENTACION DE LA VITALIDAD, NO DOS (la averia de los dos
# `master_graph` que el chequeo de gemelos vino a curar): el instrumento la
# computa para imprimirla en su sello y esta guarda la importa de ahi para
# recomputarla sobre los sellos anteriores a la vuelta 147.
from barrer_ausencia import (  # noqa: E402
    ROTULO_VITALIDAD,
    universo,
    vitalidad_de_contenido,
)

# --- VOCABULARIO CERRADO DE LAS AFIRMACIONES DE AUSENCIA ---
# Ver el docstring, seccion "EL VOCABULARIO DE DISPARO". Ampliarlo es un acto
# declarado que se escribe AQUI y se dice en el reporte, nunca una adivinanza.
FORMULAS_DE_AUSENCIA = (
    "no existe", "no existen",
    "no hay ningun", "no hay ninguna",
    "hallados: ninguno", "hallado: ninguno",
    "no se hallo", "no se halla",
    "no esta en el repositorio",
    "no instalado", "no instalados",
    "prerrequisito cumplido: no",
    # LAS OCHO DE LA VUELTA 147 (TAREA 2.a). Ver el docstring: la familia del
    # VERBO DE TENENCIA y la del LUGAR, que es por donde se colo la caida 4.2
    # del acta 146. No se sustituye ninguna de las doce de arriba: se suman.
    "no tiene", "no tienen",
    "no da un numero",
    "no halla ningun", "no halla ninguna",
    "no trae ningun", "no trae ninguna",
    "en ninguna parte",
)

# LAS DOCE DE ANTES DE LA VUELTA 147, CONSERVADAS PARA PODER MEDIR EL ESCAPE.
# No se borra lo viejo, se escribe al lado (`EJECUTOR.md` 8): sin esta tupla no
# hay forma de publicar "cuantas veia el vocabulario viejo y cuantas el nuevo"
# sobre el mismo sujeto congelado, que es lo que la TAREA 2.a exige reproducir.
# `--vocabulario viejo` la usa; ninguna corrida normal la toca.
FORMULAS_DE_AUSENCIA_VIEJAS = FORMULAS_DE_AUSENCIA[:12]

# --- EL SELLO DEL BARRIDO. Contrato compartido con barrer_ausencia.py. ---
MARCA_BARRIDO = "BARRIDO EXHAUSTIVO"
PATRON_PREGUNTA = re.compile(r"^\s*PREGUNTA:\s*(\S.*)$", re.MULTILINE)
PATRON_UNIVERSO = re.compile(r"^\s*UNIVERSO:\s*(\S.*)$", re.MULTILINE)
PATRON_CARDINAL = re.compile(r"^\s*CARDINAL:\s*(\d+)\s*$", re.MULTILINE)
PATRON_POR_CONTENIDO = re.compile(r"^\s*POR CONTENIDO:", re.MULTILINE)
# El metodo exacto de la caida de la vuelta 145, cazado por su nombre.
PATRON_CANDIDATOS_A_MANO = re.compile(r"candidatos mirados\s*:", re.IGNORECASE)

PATRON_CITA_SALIDA = re.compile(r"SALIDA_V\d+_[A-Za-z0-9_]+\.txt")

MARCA_CITA_ABRE = re.compile(r"<!--\s*CITA CONGELADA\s+(\S+?):(\S+?)\s*-->")
MARCA_CITA_CIERRA = "<!-- FIN CITA CONGELADA -->"
MARCA_EXENCION_ABRE = re.compile(r"<!--\s*EXENCION DECLARADA:\s*(.*?)\s*-->")
MARCA_EXENCION_CIERRA = "<!-- FIN EXENCION DECLARADA -->"
# LO QUE DELATA QUE UNA FRASE SI HABLA DEL REPOSITORIO. Si algo de esto aparece
# dentro de un bloque de exencion, la exencion no vale: esa frase necesita
# barrido como cualquier otra.
PATRON_APUNTA_AL_REPO = re.compile(
    r"(?:docs/|scripts/|dataset/|web/|engine/|packs/"
    r"|SALIDA_V\d+"
    r"|(?<![\w.-])[\w.-]+\.(?:py|md|json|jsonl|ts|tsx|txt|yml|yaml)(?![\w.-]))")
MARCA_COMMITS_ABRE = "<!-- COMMITS TALLADOS -->"
MARCA_COMMITS_CIERRA = "<!-- FIN COMMITS TALLADOS -->"
MARCA_CABECERA_ABRE = "<!-- CABECERA TALLADA -->"
MARCA_CABECERA_CIERRA = "<!-- FIN CABECERA TALLADA -->"


def leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


def leer_ref(ref, ruta):
    r = subprocess.run(["git", "show", "%s:%s" % (ref, ruta)], cwd=RAIZ,
                       capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8", "replace")


def desadornar(linea):
    """Quita el adorno de markdown para poder cotejar una cita VERBATIM contra
    el blob de su ref: asteriscos de enfasis, acentos graves de codigo y los
    espacios de sangria y de final. No toca ninguna palabra."""
    s = linea.replace("**", "").replace("*", "").replace("`", "")
    return re.sub(r"\s+", " ", s).strip()


# El vocabulario EN USO. Vale el nuevo salvo que `--vocabulario viejo` lo
# cambie, y eso solo lo hace la medicion del escape de la TAREA 2.a.
VOCABULARIO_ACTIVO = list(FORMULAS_DE_AUSENCIA)


def dispara(frase):
    # EL ESPACIO EN BLANCO SE NORMALIZA ANTES DE BUSCAR (vuelta 147, hallado
    # midiendo esta misma guarda sobre el reporte de la 147). Una formula
    # PARTIDA POR UN SALTO DE LINEA se le escapaba entera: `en ninguna parte`
    # con el salto justo detras de `en` no casaba, y el reporte va envuelto a
    # 88 columnas, asi que el escape no es raro, es lo normal. Escapar por
    # donde cae el salto de linea del envoltorio es la misma especie que
    # escapar por una palabra que no esta en el vocabulario, y una guarda que
    # depende de donde parta el editor no mide lo que dice medir.
    b = re.sub(r"\s+", " ", frase.lower())
    return [f for f in VOCABULARIO_ACTIVO if f in b]


def quitar_bloque_simple(texto, abre, cierra, fallos, rotulo):
    """Las tres reglas de la casa: con las dos marcas se quita lo delimitado,
    sin ninguna no se quita nada, con UNA SOLA es ROJO."""
    a, c = texto.find(abre), texto.find(cierra)
    if a == -1 and c == -1:
        return texto
    if a == -1 or c == -1:
        fallos.append("%s: falta la marca %s" % (rotulo, cierra if c == -1 else abre))
        return texto
    if c < a:
        fallos.append("%s: la marca de cierre va antes que la de apertura" % rotulo)
        return texto
    return texto[:a] + texto[c + len(cierra):]


# REFS QUE SE MUEVEN. Un ref congelado es un HASH (o algo que se resuelva a uno
# y no cambie): `HEAD`, `HEAD~n`, `HEAD^`, el nombre de una rama y las etiquetas
# movibles NO lo son. Se comprueba por la FORMA del ref y no por lo que hoy
# resuelva, porque lo que hoy resuelve es justamente lo que va a cambiar.
PATRON_HASH = re.compile(r"^[0-9a-f]{7,40}$", re.IGNORECASE)


def es_ref_movil(ref):
    """True si el ref NO es un hash de commit. Ver el comentario de arriba y el
    bloque de `quitar_citas_congeladas` que lo usa: la enfermedad del sujeto
    vivo (CORRECCION 22) metida dentro de una cita."""
    return not bool(PATRON_HASH.match(ref.strip()))


def quitar_exenciones_declaradas(texto, fallos, usadas):
    """Quita los bloques `<!-- EXENCION DECLARADA: motivo -->` ... `<!-- FIN
    EXENCION DECLARADA -->` DESPUES DE COMPROBAR QUE LO EXIMIDO DE VERDAD NO
    HABLA DEL REPOSITORIO. Ver el docstring: una exencion que escribe el
    auditado no es una exencion, es un interruptor, y lo que la salva de serlo
    es que la guarda la verifica ella misma y la imprime."""
    fuera = []
    pos = 0
    while True:
        m = MARCA_EXENCION_ABRE.search(texto, pos)
        if m is None:
            fuera.append(texto[pos:])
            break
        cierre = texto.find(MARCA_EXENCION_CIERRA, m.end())
        if cierre == -1:
            fallos.append("bloque de EXENCION DECLARADA abierto en el offset %d y nunca "
                          "cerrado con %s" % (m.start(), MARCA_EXENCION_CIERRA))
            fuera.append(texto[pos:])
            break
        motivo = (m.group(1) or "").strip()
        cuerpo = texto[m.end():cierre]
        if not motivo:
            fallos.append("EXENCION DECLARADA sin motivo escrito: una exencion sin motivo es "
                          "un interruptor. Escribir el motivo en la propia marca")
        # finditer y no findall: el patron lleva grupos internos y findall
        # devolveria los grupos en vez de lo que caso.
        apunta = sorted(set(x.group(0) for x in PATRON_APUNTA_AL_REPO.finditer(cuerpo)))
        if apunta:
            fallos.append("EXENCION DECLARADA (%r) RECHAZADA: lo eximido SI apunta al "
                          "repositorio (%s). Una frase que nombra una ruta o un fichero "
                          "afirma algo sobre el repo y necesita barrido como cualquier otra"
                          % (motivo[:80], ", ".join(apunta[:5])))
        else:
            usadas.append((motivo, " ".join(cuerpo.split())[:160]))
            cuerpo = ""   # solo se quita si la exencion es legitima
        fuera.append(texto[pos:m.start()])
        fuera.append(cuerpo)
        pos = cierre + len(MARCA_EXENCION_CIERRA)
    # LA REGLA DE LAS TRES MARCAS: un cierre suelto, sin apertura, es ROJO.
    if MARCA_EXENCION_CIERRA in texto and MARCA_EXENCION_ABRE.search(texto) is None:
        fallos.append("EXENCION DECLARADA: hay una marca de cierre %s sin su apertura"
                      % MARCA_EXENCION_CIERRA)
    return "".join(fuera)


def quitar_citas_congeladas(texto, fallos):
    """Quita los bloques `<!-- CITA CONGELADA ref:ruta -->` ... `<!-- FIN CITA
    CONGELADA -->` DESPUES DE COMPROBARLOS UNO A UNO contra el blob de su ref.
    Ver el docstring: la salida no es un interruptor que escribe el auditado."""
    fuera = []
    pos = 0
    while True:
        m = MARCA_CITA_ABRE.search(texto, pos)
        if m is None:
            break
        fin = texto.find(MARCA_CITA_CIERRA, m.end())
        if fin == -1:
            fallos.append("bloque de CITA CONGELADA abierto en el offset %d y nunca "
                          "cerrado con %s" % (m.start(), MARCA_CITA_CIERRA))
            break
        ref, ruta = m.group(1), m.group(2)
        cuerpo = texto[m.end():fin]
        if es_ref_movil(ref):
            # UNA CITA ANCLADA A UN REF MOVIL NO ESTA CONGELADA (vuelta 147,
            # TAREA 2, hallazgo de la propia medicion). El reporte de la 146
            # escribio `<!-- CITA CONGELADA HEAD:docs/loop/PROMPT_SIGUIENTE.md
            # -->` y salio VERDE el dia que se escribio; medido hoy sobre el
            # blob congelado de ese mismo reporte sale ROJO, porque `HEAD` ya
            # no es el commit de entonces y `PROMPT_SIGUIENTE.md` se sobreescribe
            # cada vuelta. Es EXACTAMENTE la enfermedad del SUJETO VIVO que la
            # CORRECCION 22 curo en la bateria de mutaciones viejas, reaparecida
            # dentro del mecanismo de cita. Un verde que no sobrevive a su
            # vuelta no es un verde.
            fallos.append("CITA CONGELADA %s:%s: %r NO es un ref congelado, es un ref MOVIL, "
                          "asi que esta cita no esta congelada y su verde no sobrevive a la "
                          "vuelta. Usese el hash del commit" % (ref, ruta, ref))
        blob = leer_ref(ref, ruta)
        if blob is None:
            fallos.append("CITA CONGELADA %s:%s: no se pudo leer ese blob con git show" % (ref, ruta))
        else:
            plano = desadornar(blob)
            for linea in cuerpo.split("\n"):
                if not dispara(linea):
                    continue
                aguja = desadornar(linea)
                if aguja and aguja not in plano:
                    fallos.append("CITA CONGELADA %s:%s: esta linea dispara el vocabulario "
                                  "y NO esta en ese blob, asi que no es una cita: %r"
                                  % (ref, ruta, aguja[:150]))
        fuera.append((m.start(), fin + len(MARCA_CITA_CIERRA)))
        pos = fin + len(MARCA_CITA_CIERRA)

    if texto.count(MARCA_CITA_CIERRA) != len(fuera) and not fallos:
        fallos.append("hay %d marcas %s y %d bloques de cita bien formados: descuadre"
                      % (texto.count(MARCA_CITA_CIERRA), MARCA_CITA_CIERRA, len(fuera)))

    salida, ultimo = [], 0
    for a, b in fuera:
        salida.append(texto[ultimo:a])
        ultimo = b
    salida.append(texto[ultimo:])
    return "".join(salida)


def sello_del_barrido(nombre):
    """(es_barrido, motivo) del fichero de salida citado. Ver el docstring,
    seccion QUE CUENTA COMO BARRIDO EXHAUSTIVO."""
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        return False, "el fichero citado no existe en docs/loop/"
    try:
        texto = leer(ruta)
    except UnicodeDecodeError:
        with io.open(ruta, "rb") as f:
            texto = f.read().decode("utf-8", "replace")
    return sello_de_texto(texto)


def sello_de_texto(texto, ref=None):
    """El MISMO juicio de `sello_del_barrido`, pero sobre el TEXTO y no sobre
    un nombre de fichero del arbol de trabajo. Se parte en dos (vuelta 147,
    TAREA 2.c) para poder juzgar un sello CONGELADO POR REF DE GIT, que es la
    unica forma de que la prueba de mutacion de esta guarda no envejezca
    (CORRECCION 22). El juicio es uno solo: no hay dos versiones."""
    if MARCA_BARRIDO not in texto:
        if PATRON_CANDIDATOS_A_MANO.search(texto):
            return False, ("trae 'candidatos mirados:' y NO trae la marca %r: es una "
                           "LISTA DE RUTAS A MANO, que es el metodo exacto de la caida "
                           "de la vuelta 145, no un barrido" % MARCA_BARRIDO)
        return False, "no trae la marca %r" % MARCA_BARRIDO
    faltan = []
    if not PATRON_PREGUNTA.search(texto):
        faltan.append("PREGUNTA:")
    if not PATRON_UNIVERSO.search(texto):
        faltan.append("UNIVERSO:")
    m_card = PATRON_CARDINAL.search(texto)
    if not m_card:
        faltan.append("CARDINAL:")
    elif int(m_card.group(1)) <= 0:
        faltan.append("CARDINAL: mayor que cero (un universo vacio no es un universo)")
    m_cont = PATRON_POR_CONTENIDO.search(texto)
    if not m_cont:
        faltan.append("POR CONTENIDO: (la segunda pierna, la que faltaba en la caida)")
    if faltan:
        return False, "trae la marca pero le falta: %s" % ", ".join(faltan)

    # LA SEXTA PIEZA (vuelta 147, TAREA 2.b): LA PIERNA POR CONTENIDO TIENE QUE
    # PODER HABER HALLADO LA COSA. Ver el docstring de `barrer_ausencia.py`,
    # seccion LA SEXTA PIEZA DEL SELLO: si TODAS las alternativas del patron de
    # contenido tienen CERO apariciones en el universo entero, el barrido no
    # puede distinguir "la cosa no existe" de "adivine mal el nombre".
    ok_vit, motivo_vit = vitalidad_del_sello(texto, ref)
    if not ok_vit:
        return False, motivo_vit
    return True, "sello completo, con la pierna por contenido viva"


PATRON_UNIVERSO_ACOTADO = re.compile(r"^\s*UNIVERSO:.*ACOTADO a (.+?)\s*$", re.MULTILINE)
PATRON_EXCLUIDOS = re.compile(
    r"^\s*EXCLUIDOS POR SER SONDA Y NO INSTALACION[^:]*:\s*(\d+)\s*$", re.MULTILINE)


def _prefijos_y_excluidos(texto):
    """Reconstruye el universo DECLARADO EN EL SELLO: los prefijos de la linea
    `UNIVERSO:` y las rutas excluidas por ser sonda. Las exclusiones se honran
    a proposito: ignorarlas haria parecer VIVA una alternativa cuyo unico
    fichero es la propia sonda que la busca, que es justo el caso que
    `--excluir` existe para no contar."""
    m = PATRON_UNIVERSO_ACOTADO.search(texto)
    prefijos = [p.strip() for p in m.group(1).split(",") if p.strip()] if m else []
    excluidos = []
    m2 = PATRON_EXCLUIDOS.search(texto)
    if m2:
        n = int(m2.group(1))
        resto = texto[m2.end():].splitlines()
        for linea in resto[1:1 + n]:
            if linea.strip():
                excluidos.append(linea.strip())
    return prefijos, excluidos


def vitalidad_del_sello(texto, ref=None):
    """(ok, motivo) de la SEXTA PIEZA. Dos caminos, y el segundo es el que hace
    que esta guarda muerda sobre los barridos de ANTES de la vuelta 147:

      (1) EL SELLO LA PUBLICA (barridos de la 147 en adelante): se lee su linea
          `VITALIDAD DE LOS PATRONES DE CONTENIDO: <vivas> de <total>`.
      (2) EL SELLO NO LA PUBLICA (barridos viejos): NO se cae por vieja, que
          seria un rojo sin contenido. SE RECOMPUTA AQUI Y AHORA, con el mismo
          `vitalidad_de_contenido` que usa el instrumento (UNA sola
          implementacion, importada, nunca dos), sobre el universo que el propio
          sello declara. Asi el rojo del barrido del umbral de la 146 no dice
          "te falta una linea": dice QUE SUS TRES PATRONES ESTAN MUERTOS, medido
          hoy.

    En los dos caminos el veredicto es el mismo: TODAS las alternativas muertas
    es ROJO; al menos una viva pasa."""
    m = re.search(r"^\s*%s:\s*(\d+) de (\d+)\b" % re.escape(ROTULO_VITALIDAD),
                  texto, re.MULTILINE)
    if m:
        vivas, total = int(m.group(1)), int(m.group(2))
        if vivas == 0:
            return False, ("su sello declara %d de %d alternativas de contenido VIVAS: la "
                           "pierna POR CONTENIDO esta ENTERAMENTE MUERTA y no puede "
                           "distinguir que la cosa no exista de que se adivinara mal el "
                           "nombre" % (vivas, total))
        return True, "vitalidad declarada en el sello: %d de %d vivas" % (vivas, total)

    m_cont = PATRON_POR_CONTENIDO.search(texto)
    linea = texto[m_cont.start():texto.find("\n", m_cont.start())]
    cuerpo = linea.split(":", 1)[1]
    patron = cuerpo.rsplit("|", 1)[0].strip() if "| " in cuerpo else cuerpo.strip()
    prefijos, excluidos = _prefijos_y_excluidos(texto)
    try:
        rutas = [r for r in universo(prefijos, ref) if r not in set(excluidos)]
        vit = vitalidad_de_contenido(rutas, patron, ref)
    except Exception as e:
        return False, ("su sello no publica %r y no se pudo recomputar la vitalidad de sus "
                       "patrones de contenido: %s" % (ROTULO_VITALIDAD, e))
    vivas = [x for x in vit if x[1] not in (None, 0)]
    donde = "el arbol de %s" % ref[:8] if ref else "el arbol de trabajo de hoy"
    if not vivas:
        muertas = ", ".join(repr(a) for a, _ in vit)
        return False, ("su sello es anterior a la vuelta 147 y no publica %r, asi que la "
                       "recomputo aqui sobre el universo que el mismo declara, leido de %s "
                       "(%d ficheros): SUS %d ALTERNATIVAS DE CONTENIDO ESTAN TODAS MUERTAS, "
                       "cero apariciones en todo el universo (%s). Una pierna por contenido de "
                       "nombres que nadie escribio nunca no puede respaldar una ausencia"
                       % (ROTULO_VITALIDAD, donde, len(rutas), len(vit), muertas))
    return True, ("vitalidad RECOMPUTADA sobre %s (sello anterior a la 147): %d de %d "
                  "alternativas vivas" % (donde, len(vivas), len(vit)))


def ventana(frases, i):
    """La misma frase mas hasta DOS antes y hasta DOS despues. Bidireccional a
    proposito: ver el docstring, seccion LA VENTANA."""
    return " ".join(frases[max(0, i - 2):i + 3])


def verificar(texto):
    fallos = []
    exenciones = []
    texto = quitar_exenciones_declaradas(texto, fallos, exenciones)
    texto = quitar_citas_congeladas(texto, fallos)
    texto = quitar_bloque_simple(texto, MARCA_COMMITS_ABRE, MARCA_COMMITS_CIERRA,
                                 fallos, "COMMITS TALLADOS")
    texto = quitar_bloque_simple(texto, MARCA_CABECERA_ABRE, MARCA_CABECERA_CIERRA,
                                 fallos, "CABECERA TALLADA")

    frases = dividir_frases(texto)
    vistas, respaldadas = [], []
    for i, fr in enumerate(frases):
        formulas = dispara(fr)
        if not formulas:
            continue
        vistas.append((i, fr, formulas))
        citas = PATRON_CITA_SALIDA.findall(ventana(frases, i))
        if not citas:
            fallos.append("AUSENCIA SIN BARRIDO: %r (dispara por %s) no cita ningun "
                          "SALIDA_V<N>_*.txt en su ventana"
                          % (fr.strip()[:150], ", ".join(formulas)))
            continue
        buenos, motivos = [], []
        for c in sorted(set(citas)):
            ok, motivo = sello_del_barrido(c)
            (buenos if ok else motivos).append(c if ok else "%s (%s)" % (c, motivo))
        if not buenos:
            fallos.append("AUSENCIA MAL RESPALDADA: %r (dispara por %s) cita %s, y ninguno "
                          "es un barrido exhaustivo sellado: %s"
                          % (fr.strip()[:150], ", ".join(formulas), ", ".join(sorted(set(citas))),
                             "; ".join(motivos)))
            continue
        respaldadas.append((fr, formulas, buenos))
    return fallos, vistas, respaldadas, exenciones


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reporte", default=RUTA_REPORTE)
    ap.add_argument("--ref", default=None,
                    help="lee el reporte del blob de ese ref en vez del arbol de trabajo")
    ap.add_argument("--vocabulario", choices=("nuevo", "viejo"), default="nuevo",
                    help="'viejo' usa las DOCE formulas de antes de la vuelta 147; existe "
                         "SOLO para medir el escape de la TAREA 2.a sobre sujeto congelado")
    ap.add_argument("--sello", default=None, metavar="RUTA",
                    help="juzga el SELLO de UN barrido (no un reporte) y sale VERDE o ROJO; "
                         "con --sello-ref lo lee del blob de ese ref, congelado")
    ap.add_argument("--sello-ref", default=None, metavar="REF",
                    help="ref de git del que leer el fichero de --sello")
    a = ap.parse_args()

    global VOCABULARIO_ACTIVO
    VOCABULARIO_ACTIVO = list(FORMULAS_DE_AUSENCIA_VIEJAS if a.vocabulario == "viejo"
                              else FORMULAS_DE_AUSENCIA)

    if a.sello:
        rel = os.path.relpath(os.path.abspath(a.sello), RAIZ).replace("\\", "/")
        if a.sello_ref:
            texto = leer_ref(a.sello_ref, rel)
            if texto is None:
                print("ROJO PREVIO: no se pudo leer %s:%s" % (a.sello_ref, rel))
                return 1
            sujeto = "%s:%s" % (a.sello_ref, rel)
        else:
            if not os.path.exists(a.sello):
                print("ROJO PREVIO: no existe %s" % a.sello)
                return 1
            texto = leer(a.sello)
            sujeto = a.sello
        ok, motivo = sello_de_texto(texto, a.sello_ref)
        print("SUJETO DEL SELLO: %s" % sujeto)
        print("%s: %s" % ("VERDE EXIT 0" if ok else "ROJO EXIT 1", motivo))
        return 0 if ok else 1

    if a.ref:
        rel = os.path.relpath(os.path.abspath(a.reporte), RAIZ).replace("\\", "/")
        texto = leer_ref(a.ref, rel)
        if texto is None:
            print("ROJO PREVIO: no se pudo leer %s:%s" % (a.ref, rel))
            return 1
        sujeto = "%s:%s" % (a.ref, rel)
    else:
        if not os.path.exists(a.reporte):
            print("ROJO PREVIO: no existe %s" % a.reporte)
            return 1
        texto = leer(a.reporte)
        sujeto = a.reporte

    fallos, vistas, respaldadas, exenciones = verificar(texto)

    print("SUJETO: %s" % sujeto)
    if fallos:
        print("ROJO EXIT 1, %d afirmacion(es) de ausencia sin barrido exhaustivo detras:"
              % len(fallos))
        for f in fallos:
            print("   %s" % f)
    else:
        print("VERDE EXIT 0: las %d afirmacion(es) de ausencia vistas vienen respaldadas "
              "por un barrido exhaustivo sellado." % len(vistas))
    for fr, formulas, buenos in respaldadas:
        print("   RESPALDADA por %s: %r" % (", ".join(buenos), fr.strip()[:120]))
    # CADA EXENCION USADA SE IMPRIME (vuelta 148, TAREA 2.4). Una exencion
    # invisible seria peor que el rojo que evita.
    for motivo, cuerpo in exenciones:
        print("   EXENCION DECLARADA aceptada (no apunta al repositorio) | motivo: %s"
              % motivo)
        print("      texto eximido: %r" % cuerpo)
    print("<!-- COBERTURA DE AUSENCIAS -->")
    print("COBERTURA DE AUSENCIAS: %d vistas / %d respaldadas / %d en rojo / %d exentas "
          "declaradas | vocabulario de %d formulas"
          % (len(vistas), len(respaldadas), len(fallos), len(exenciones),
             len(VOCABULARIO_ACTIVO)))
    print("<!-- FIN COBERTURA DE AUSENCIAS -->")
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
