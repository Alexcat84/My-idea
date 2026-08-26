# -*- coding: utf-8 -*-
"""_v74_construir_registrador_acta.py . ARMA scripts/loop/vuelta74_registrar_acta73.py
COPIANDO LA MAQUINA DE scripts/loop/vuelta73_registrar_acta72.py, NO RETECLEANDOLA.

POR QUE EXISTE. El acta 68 escribio la regla en su D14 y las actas 69, 70, 71,
72 y 73 la dejaron en pie: importar una guarda vale DENTRO DE LA MISMA VUELTA; el
carril de COPIAR es el que protege a los registradores de VUELTAS DISTINTAS. El
registrador del acta 73 es de OTRA vuelta que la maquina del acta 72, asi que la
maquina se COPIA. Y copiar a mano es reteclear: este fichero la EXTRAE del
ancestro y le pega encima, con un assert por cada cambio, exactamente las piezas
propias.

LO QUE SE COPIA LITERAL (medido con assert de presencia en el ancestro):
  lineas_de, derivar, negativas, sustituir, cotejar_texto, las cinco expresiones
  regulares, _CACHE y el cuerpo de main.

LO QUE ES PROPIO Y NO SE COPIA: el docstring, el ROTULO, la ruta nueva, AGUJAS,
ANCLAS, NUMEROS_DECLARADOS, NEGATIVAS, el modulo de texto que se importa y la
marca de idempotencia.

LA ADJUDICACION 3 DEL ACTA 69 SE RESPETA CON TODAS SUS LETRAS: la maquina NO
CRECE Y TAMPOCO ENCOGE. Cero mecanismos nuevos, cero filas nuevas, cero columnas
nuevas, y ninguno de los cuatro mecanismos de la guarda de citas se cae por el
camino: los cuatro salen del ancestro tal cual.

LA RUTA NUEVA NO ES MAQUINA NUEVA, Y SE DICE POR QUE. Esta vuelta deja escrita
una REGLA NUEVA DE REDACCION (la del D13 del acta 73) que nombra TRES FORMAS, y
esas tres formas no se teclean: se citan por aguja sobre el fichero que las
define, scripts/loop/comprobar_promesas_de_marcado.py. La maquina de agujas del
ancestro YA buscaba en el fichero que cada CLAVE nombra: AGUJAS es un mapa CLAVE
-> (fichero, aguja) y el fichero es un dato, no un mecanismo. Lo unico que se
anade es UNA constante de ruta en el bloque PROPIO, junto a las agujas que la
usan. Es el mismo carril que la vuelta 72 uso con tres rutas y la 73 con una,
adjudicado A FAVOR en el D11 del acta 72. Ni una funcion nueva, ni una condicion
nueva, ni una tabla nueva.

Y LA RAZON DE FONDO DE CITAR ESAS TRES FORMAS EN VEZ DE TECLEARLAS ES LA PROPIA
REGLA QUE SE REGISTRA: una regla que nombra tres cadenas TECLEADAS puede divergir
del instrumento sin que nadie lo note, que es exactamente la especie de averia
que el D13 declara. Citada por aguja, si el instrumento cambiara una forma, el
registro caeria en ROJO.

EL CORTE DEL BLOQUE DE IMPORTS ES EL MISMO QUE USO EL CONSTRUCTOR DE LA VUELTA
73, y se dice para que no parezca casualidad: aquel corte se movio al comienzo
del bloque PROPIO porque su ancestro estrenaba rutas propias delante. El mio
tambien las tiene (la del acta 72), asi que el corte sigue siendo ese y se MIDE
con un assert de que la ruta del ancestro no se cuela.

Uso: python scripts/loop/_v74_construir_registrador_acta.py
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANCESTRO = os.path.join(RAIZ, "scripts", "loop", "vuelta73_registrar_acta72.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop", "vuelta74_registrar_acta73.py")
NL = chr(10)

CABECERA = '''# -*- coding: utf-8 -*-
"""vuelta74_registrar_acta73.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DE LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 73.

NO REESCRIBE NI UNA LINEA DE LAS SECCIONES DE ARRIBA: abre el fichero en modo
adosar y escribe detras. Es la via que esta pagina ya uso CATORCE veces, la
ultima de ellas la del acta 72. Los numeros de linea de esas sedes NO se teclean
aqui: los que este instrumento ESCRIBE salen todos de una aguja.

LA MAQUINA SE COPIA, NO SE IMPORTA, y va dicho porque el acta 68 escribio la
regla en su D14 y las actas 69 a 73 la dejaron en pie: importar vale DENTRO DE
LA MISMA VUELTA (dos instrumentos que nacen juntos y no pueden divergir), y el
carril de COPIAR es el que protege a los registradores de VUELTAS DISTINTAS.
Este es de otra vuelta que scripts/loop/vuelta73_registrar_acta72.py, asi que se
copia entero. Y NO SE COPIA A MANO, QUE ES RETECLEAR: lo copia
scripts/loop/_v74_construir_registrador_acta.py POR EXTRACCION, con un assert por
cada pieza. Lo unico propio son las RUTAS, las AGUJAS, las ANCLAS, los
NUMEROS_DECLARADOS, las NEGATIVAS y el texto importado.

LA MAQUINA NO CRECE NI ENCOGE EN ESTA VUELTA, Y SE DICE: la adjudicacion 3 del
acta 69 congelo las tablas de los registradores y prohibio que crezcan sin
encargo previo, y el D12 del acta 73 recordo que encoger esta igual de prohibido.
Aqui no entra ni un mecanismo nuevo ni se cae ninguno. Los cuatro de la guarda de
citas son los del ancestro:

  1. LAS CITAS DE LINEA DEL TEXTO SE DERIVAN POR AGUJA, NO SE TECLEAN.
  2. TODA CITA DE LA FORMA linea NNNN SE COTEJA CONTRA EL CONTENIDO DE ESA LINEA
     ANTES DE ESCRIBIR, y toda CLAVE derivada se usa al menos una vez.
  3. LA RED ANCHA: todo numero de 3 a 5 digitos en NEGRITA sale de una aguja o
     esta declarado uno a uno con su motivo en NUMEROS_DECLARADOS.
  4. LAS AGUJAS NEGATIVAS: pares (CLAVE, aguja que esa linea NO debe contener).

UN SOLO FICHERO DE AGUJA QUE NO ES NI LA PAGINA NI EL ACTA, y no es maquina
nueva: esta vuelta deja escrita la REGLA NUEVA DE REDACCION del D13 del acta 73,
que nombra TRES FORMAS de promesa de marcado, y esas tres se CITAN por aguja
sobre el fichero que las define en vez de teclearse. AGUJAS siempre fue un mapa
CLAVE -> (fichero, aguja) y el fichero es un dato: se anade PROMESAS como
constante de ruta, y nada mas. La vuelta 72 anadio TRES por el mismo carril y su
D11 lo adjudico A FAVOR; la 73 anadio UNA.

LAS TRES NEGATIVAS DE ESTA VUELTA, y las tres son de sustancia:
  a) el apartado de las otras dos preguntas parte en DOS citas lo que el acta 73
     dice del CHOCAN invisible: la linea que ANUNCIA que ahi se adjudica la
     pregunta 1, y la linea que ESCRIBE la extension. Son dos cosas distintas y
     la tabla las cita por separado; si la linea de la extension ya anunciara la
     pregunta, la tabla estaria citando dos veces la misma cosa como si fueran
     dos: se MIDE que la linea de la extension NO contiene la palabra pregunta;
  b) las DOS rachas se registran en filas distintas porque la regla de la parada
     las cuenta por separado (dos seguidas una, tres la otra), y el acta las
     escribe en dos lineas: se MIDE que la linea de la racha de CLASE O CIFRA
     PUBLICADA NO contiene la palabra REPORTE, que es la otra;
  c) el apartado de la regla nueva manda a lineas distintas la NEGATIVA (que el
     instrumento NO se ensancha) y la NOMINA de las tres formas. La negativa es
     la que hace que la regla no sea maquina nueva, y por eso no puede estar en
     la linea que nombra las formas: se MIDE que la linea de la negativa NO
     contiene la palabra DISCUTIBLE.

LA IDEMPOTENCIA SE MIRA PRIMERO: si la seccion ya esta en la pagina, no se
escribe nada. Una pagina con la adjudicacion duplicada no falla, dice que si.

Uso:
  python scripts/loop/vuelta74_registrar_acta73.py [--simular]
"""
'''

PROPIO = '''
# LA RUTA NUEVA. Es DATO, no mecanismo: AGUJAS siempre fue un mapa
# CLAVE -> (fichero, aguja) y la maquina siempre busco en el fichero que la clave
# nombra. Vive aqui, en el bloque propio, junto a las agujas que la usan. Es el
# fichero que DEFINE las tres formas de promesa de marcado, y la regla nueva las
# cita en vez de teclearlas.
PROMESAS = os.path.join(RAIZ, "scripts", "loop", "comprobar_promesas_de_marcado.py")

# CLAVE -> (fichero, aguja). La aguja es el CONTENIDO que la cita afirma; el
# numero de linea sale de buscarla, nunca de teclearla.
AGUJAS = {
    # --- docs/loop/ACTA_AUDITOR.md, acta de la vuelta 73: las cabeceras ---
    "A73_ABRE": (ACTA, "# ACTA DE LA VUELTA 73 DEL AUDITOR (26 ago 2026, Fable 5)"),
    "A73_VERIF": (ACTA, "## 1. VERIFICACION, TODA POR CORRIDA PROPIA DE HOY"),
    "A73_CIEGA": (ACTA, "## 2. RELECTURA CIEGA, EMPEZANDO POR LOS DISCUTIBLES MARCADOS"),
    "A73_TRECE": (ACTA, "## 3. LOS TRECE DISCUTIBLES, ADJUDICADOS"),
    "A73_AVERIAS": (ACTA, "## 4. LAS CUATRO AVERIAS DEL EJECUTOR"),
    "A73_PROPIOS": (ACTA, "## 5. ERRORES PROPIOS DEL AUDITOR, CON NOMBRE"),
    "A73_METRICA": (ACTA, "## 6. METRICA DE CREDITO ACUMULADA"),
    "A73_PARADAS": (ACTA, "## 7. CONDICIONES DE PARADA, RECORRIDAS: NINGUNA SE CUMPLE HOY"),
    "A73_ENCARGO": (ACTA, "## 8. ENCARGO"),
    # la verificacion por corrida propia, pieza a pieza
    "A73_V_CADENA": (ACTA, "- CADENA DE COMMITS: los seis del reporte estan en la rama y en orden"),
    "A73_V_MARCADOR": (ACTA, "- MARCADOR DESDE EL ARCHIVO, con mi propio python sobre"),
    "A73_V_CABECERA": (ACTA, "- CABECERA TALLADA: re-corri tallar_cabecera_reporte.py --vuelta 73 y la"),
    "A73_V_RECOMPUTO": (ACTA, "- RECOMPUTO AL CIERRE: corri scripts/plan/recomputo_3388.py sobre el"),
    "A73_V_GRAFO": (ACTA, "- GRAFO, contado por mi sobre master_graph.json: 3853 ficheros, 3188"),
    "A73_V_ABSORBIDOS": (ACTA, "- LOS OCHO ABSORBIDOS estan deprecados y LOS CUATRO SUPERVIVIENTES vivos"),
    "A73_V_COLA": (ACTA, "- COLA DE COSTURAS: 1440 en c584f060 (git show contado por mi) y 1438"),
    "A73_V_COLISIONES": (ACTA, "- COLISIONES: re-corri vuelta51_censo_colisiones.py y mi salida es"),
    "A73_V_ESPERADAS": (ACTA, "- ESPERADAS PRE FUSION: en worktree sobre c584f060 re-corri"),
    "A73_V_VARAS": (ACTA, "- VARAS Y PUENTES PRE FUSION, en el mismo worktree: la tabla entera de"),
    "A73_V_DUPLICADAS": (ACTA, "- DUPLICADAS: 898 grupos y 711 nodos contados por mi sobre"),
    "A73_V_OPERACIONES": (ACTA, "- OPERACIONES E INVENTARIO: 71 fichas, todas LISTA, CERO dependencias"),
    "A73_V_NUMSTAT": (ACTA, "- NUMSTAT: 1562faa9 trae 260 0 en 03_FUSIONES.md y 33 0 en"),
    "A73_V_CUENTA": (ACTA, "- CUENTA AGREGADA: re-corrida sobre el plan sellado: 18 perdidas, 12 de"),
    "A73_V_PROMESAS": (ACTA, "- PROMESAS DE MARCADO: re-corri comprobar_promesas_de_marcado.py: 2"),
    "A73_V_BORDE": (ACTA, "- BORDE DEL DUENO: re-corri _v73_borde_del_dueno.py (6 entradas de tipo"),
    "A73_V_TRAMO": (ACTA, "- TRAMO AL CIERRE: recompute por mi cuenta sobre el fichero fijado y el"),
    "A73_V_GATE0": (ACTA, "- GATE 0 Y SUITES, corridos por mi: run_phase1 --reaplico-curaduria dio"),
    "A73_V_BARRIDO": (ACTA, "- BARRIDO DE TITULOS re-corrido por mi: 487 ficheros, ROJO 32, AMBAR 0,"),
    "A73_V_CENSO": (ACTA, "- FICHEROS V73: 52 contados por mi con grep -c, como el censo del"),
    # la ciega
    "A73_CIEGA_LEIDOS": (ACTA, "Los cuatro actos del lote I, 12 nodos, leidos ENTEROS del grafo PRE"),
    "A73_CIEGA_4DE4": (ACTA, "CIEGA 4 DE 4: mis cuatro coronas son las cuatro del ejecutor, cero"),
    "A73_CIEGA_2290": (ACTA, "matan LOS DOS a new_view_vs_old_view_de_error_humano con la contencion"),
    "A73_CIEGA_50": (ACTA, "mismo sitio: el entregable del uno es el informe entero y el del otro"),
    "A73_CIEGA_INCISO": (ACTA, "Los siete INCISO estan VERBATIM en los supervivientes de hoy, con sus"),
    # los discutibles que traen adjudicacion
    "A73_D13": (ACTA, "D13 (las dos promesas de marcado invisibles para la guarda): A FAVOR"),
    "A73_D13_NOENSANCHA": (ACTA, "la practica de frases selladas: NO se ensancha el instrumento; se"),
    "A73_D13_PLANES": (ACTA, "planes ejecutados no se re-sellan (acta 68, D15); la regla rige de la"),
    "A73_D1_PREG1": (ACTA, "que hablan apuntan al mismo. Adjudicacion de la pregunta 1 de la"),
    "A73_D1_EXT": (ACTA, "cuando la unica vara que habla apunta al nodo que las razones escritas"),
    "A73_D7_PREG2": (ACTA, "Adjudicacion de la pregunta 2 de la seccion 8: es una regla practica de"),
    # las averias y los errores propios
    "A73_AVERIAS_CUATRO": (ACTA, "Las cuatro (7.1 a 7.4) son manejos propios cazados por instrumento o"),
    "A73_PROPIOS_ENLACES": (ACTA, "- Mi primera cuenta de enlaces (14898) uso una definicion mia (solo"),
    # la metrica y las rachas
    "A73_METRICA_CAIDAS": (ACTA, "Caidas del ejecutor en esta tanda (vuelta 73): CERO de clase, CERO de"),
    "A73_METRICA_ACUM": (ACTA, "Acumulado: 489 relecturas (485 mas las cuatro ciegas), 847 puestos (835"),
    "A73_RACHAS": (ACTA, "Rachas: CLASE O CIFRA PUBLICADA en CERO tandas (tercera limpia"),
    "A73_RACHAS_REPORTE": (ACTA, "seguida). REPORTE en CERO tandas (tercera limpia seguida)."),
    # la condicion de parada del cierre de la fase 03, pieza a pieza
    "A73_CIERRE03": (ACTA, "- CIERRE DE LA FASE 03 (la parada del fundador): NO SE CUMPLE TODAVIA,"),
    "A73_CIERRE03_UNICO": (ACTA, "  pero es lo unico que queda delante: ya no hay ningun acto del tramo"),
    "A73_CIERRE03_FICHAS": (ACTA, "  el destino de cada una de las 16 fichas de 03_FUSIONES, los QUINCE"),
    "A73_CIERRE03_QUINCE": (ACTA, "  declarados con su subconjunto descrito (el 44 NOMBRADO APARTE, acta"),
    "A73_CIERRE03_DUENOS": (ACTA, "  viven en 01_FUENTES, 05_SANEO y 00_CODIGO, fuera de la fase 03, y eso"),
    "A73_CIERRE03_MESA": (ACTA, "  de la fase 06_MESAS: si no es de la 03, no la bloquea, y eso tambien"),
    "A73_CIERRE03_QUIEN": (ACTA, "  se mide, no se supone). La vuelta 74 arma ese peso; el auditor de la"),
    # --- docs/plan/03_FUSIONES.md, sedes de esta misma pagina ---
    "PAG_ACTA72": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 72, REGISTRADAS AQUI"),
    "PAG_ACTA71": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 71, REGISTRADAS AQUI"),
    # --- LAS TRES FORMAS DE LA REGLA NUEVA, EN EL FICHERO QUE LAS DEFINE ---
    "PROM_SINGULAR": (PROMESAS, 'PROMESA = "va marcado como discutible"'),
    "PROM_PLURAL": (PROMESAS, 'PROMESA_PLURAL = "van marcadas como discutibles"'),
    "PROM_SINCOMO": (PROMESAS, 'PROMESA_SIN_COMO = "va marcado discutible"'),
    "PROM_FORMAS": (PROMESAS, "FORMAS = (PROMESA, PROMESA_PLURAL, PROMESA_SIN_COMO)"),
    "PROM_IMPRIME": (PROMESAS, "agujas   : %d, y se imprimen para que la vara no dependa del docstring"),
}

# ANCLAS: hay agujas que NO son unicas en todo el fichero porque el acta repite
# cabeceras de seccion vuelta tras vuelta. Para esas, la busqueda se restringe a
# una VENTANA que arranca en otra clave ya derivada, y se sigue exigiendo UNA
# sola ocurrencia DENTRO de la ventana.
# CLAVE -> (clave ancla, ventana en lineas).
ANCLAS = dict(
    [(c, ("A73_ABRE", 500)) for c in AGUJAS if c.startswith("A73_") and c != "A73_ABRE"]
)

# NUMEROS QUE EL TEXTO ESCRIBE EN NEGRITA Y NO SON CITAS DE LINEA, declarados
# uno a uno con su motivo. Todo lo demas que aparezca en negrita con 3 a 5
# digitos tiene que salir de una aguja, o es ROJO.
NUMEROS_DECLARADOS = {}

# (CLAVE, aguja que esa linea NO debe contener). La afirmacion negativa se MIDE,
# no se cree. Ver el docstring: las tres son de sustancia, no de adorno.
NEGATIVAS = [
    ("A73_D1_EXT", "pregunta"),
    ("A73_RACHAS", "REPORTE"),
    ("A73_D13_NOENSANCHA", "DISCUTIBLE"),
]
'''

CIERRE = '''
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v74_texto_acta73 import TEXTO  # noqa: E402

MARCA_IDEMPOTENCIA = "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 73"
'''


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    src = io.open(ANCESTRO, encoding="utf-8").read()
    print("=" * 78)
    print("CONSTRUCCION DE vuelta74_registrar_acta73.py POR EXTRACCION DEL ANCESTRO")
    print("  ancestro: %s (%d lineas)" % (os.path.basename(ANCESTRO), len(src.split(NL))))
    print("=" * 78)

    # PIEZA 1: el bloque de imports y rutas, del ancestro y literal. EL CORTE ES
    # EL MISMO QUE USO EL CONSTRUCTOR DE LA VUELTA 73 (el comienzo del bloque
    # PROPIO) porque mi ancestro tambien estrena una ruta propia delante de
    # AGUJAS: cortar en el comentario de AGUJAS se llevaria prosa ajena al bloque
    # de imports. Se MIDE que la ruta del ancestro no se cuela.
    i1 = src.index("import argparse")
    f1 = src.index("# LA RUTA NUEVA")
    imports = src[i1:f1]
    assert "PAGINA = os.path.join" in imports and "ACTA = os.path.join" in imports
    assert "NL = chr(10)" in imports
    assert "AGUJAS" not in imports and "CUENTA = os.path.join" not in imports
    print("  PIEZA 1 imports y rutas   : %d lineas, EXTRAIDA" % imports.count(NL))

    # PIEZA 2: de las expresiones regulares hasta el final de cotejar_texto, del
    # ancestro y literal. Es la maquina entera de la guarda de citas.
    i2 = src.index("RE_MARCA = re.compile")
    f2 = src.index("sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))")
    maquina = src[i2:f2]
    for pieza in ("def lineas_de(", "def derivar(", "def negativas(", "def sustituir(",
                  "def cotejar_texto(", "RE_CITA = re.compile", "RE_NEGRITA = re.compile",
                  "RE_VERBATIM = re.compile", "_CACHE = {}"):
        assert pieza in maquina, pieza
    print("  PIEZA 2 la maquina entera : %d lineas, EXTRAIDA (9 piezas comprobadas)"
          % maquina.count(NL))

    # PIEZA 3: main entero, del ancestro y literal, con DOS cambios declarados:
    # los dos rotulos que nombran el acta que se registra.
    i3 = src.index("def main():")
    cuerpo = src[i3:]
    assert "def main()" in cuerpo and 'if __name__ == "__main__":' in cuerpo
    cambios = [
        ('print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 72 AL FINAL DE 03_FUSIONES.md")',
         'print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 73 AL FINAL DE 03_FUSIONES.md")'),
        ('print("YA ADOSADA: la seccion del acta 72 ya esta en la pagina. No se escribe nada.")',
         'print("YA ADOSADA: la seccion del acta 73 ya esta en la pagina. No se escribe nada.")'),
    ]
    for viejo, nuevo in cambios:
        assert cuerpo.count(viejo) == 1, viejo
        cuerpo = cuerpo.replace(viejo, nuevo)
    print("  PIEZA 3 main entero       : %d lineas, EXTRAIDA con %d rotulos cambiados"
          % (cuerpo.count(NL), len(cambios)))

    # PIEZA 4: EL ROTULO DEL FICHERO HIJO, EXTRAIDO DEL ANCESTRO Y NO TECLEADO
    # AQUI. Va por extraccion por dos motivos y los dos se dicen: es la misma
    # doctrina de copiar y no reteclear que rige la maquina, y un rotulo escrito
    # DENTRO del constructor es un ROTULO HUERFANO para el barrido de titulos,
    # porque el titulo que cubre no es el del constructor sino el del hijo. Es la
    # leccion de la averia 7.4 de la vuelta 70.
    i4 = src.index("# ROTULO titulo")
    f4 = src.index(NL, i4)
    rotulo = src[i4:f4]
    cambios_rotulo = [("cita=vuelta:72", "cita=vuelta:73"),
                      ("ACTA DE LA VUELTA 72 DEL AUDITOR", "ACTA DE LA VUELTA 73 DEL AUDITOR"),
                      ("que es de la vuelta 72", "que es de la vuelta 73"),
                      ("el fichero es de la vuelta 73", "el fichero es de la vuelta 74")]
    for viejo, nuevo in cambios_rotulo:
        assert rotulo.count(viejo) == 1, viejo
        rotulo = rotulo.replace(viejo, nuevo)
    print("  PIEZA 4 el rotulo del hijo: EXTRAIDO con %d campos cambiados" % len(cambios_rotulo))

    salida = (CABECERA + rotulo + NL + imports + PROPIO.lstrip(NL) + NL + maquina
              + CIERRE.lstrip(NL) + NL + cuerpo)
    for mal, nombre in ((chr(8212), "guion largo"), (chr(8211), "guion medio")):
        assert mal not in salida, nombre
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(salida)
    print()
    print("ESCRITO %s (%d lineas)" % (os.path.basename(DESTINO), len(salida.split(NL))))

    # LA PRUEBA DE QUE LA MAQUINA NO SE RETECLEO: las dos piezas copiadas tienen
    # que aparecer LITERALES dentro del fichero nuevo.
    nuevo = io.open(DESTINO, encoding="utf-8").read()
    print("  la maquina aparece LITERAL en el destino : %s" % (maquina in nuevo))
    print("  los imports aparecen LITERALES           : %s" % (imports in nuevo))
    assert maquina in nuevo and imports in nuevo
    print()
    print("VERDE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
