# -*- coding: utf-8 -*-
"""_v72_construir_registrador_acta.py . ARMA scripts/loop/vuelta72_registrar_acta71.py
COPIANDO LA MAQUINA DE scripts/loop/vuelta71_registrar_acta70.py, NO RETECLEANDOLA.

POR QUE EXISTE. El acta 68 escribio la regla en su D14 y las actas 69, 70 y 71 la
dejaron en pie: importar una guarda vale DENTRO DE LA MISMA VUELTA; el carril de
COPIAR es el que protege a los registradores de VUELTAS DISTINTAS. El registrador
del acta 71 es de OTRA vuelta que la maquina del acta 70, asi que la maquina se
COPIA. Y copiar a mano es reteclear: este fichero la EXTRAE del ancestro y le
pega encima, con un assert por cada cambio, exactamente las piezas propias.

LO QUE SE COPIA LITERAL (medido con assert de presencia en el ancestro):
  lineas_de, derivar, negativas, sustituir, cotejar_texto, las cinco expresiones
  regulares, _CACHE y el cuerpo de main.

LO QUE ES PROPIO Y NO SE COPIA: el docstring, el ROTULO, las TRES rutas nuevas,
AGUJAS, ANCLAS, NUMEROS_DECLARADOS, NEGATIVAS, el modulo de texto que se importa
y la marca de idempotencia.

LA ADJUDICACION 3 DEL ACTA 69 SE RESPETA CON TODAS SUS LETRAS: la maquina NO
CRECE. Cero mecanismos nuevos, cero filas nuevas, cero columnas nuevas. Los
cuatro mecanismos de la guarda de citas salen del ancestro tal cual.

LAS TRES RUTAS NUEVAS NO SON MAQUINA NUEVA, Y SE DICE POR QUE. Esta vuelta cita
la sede de sus tres correcciones declaradas, y dos de ellas no viven ni en la
pagina ni en el acta (docs/plan/OPERACIONES.jsonl, scripts/rumbos/banco_rumbos.json
y scripts/loop/generar_plan_del_lote.py). La maquina de agujas del ancestro YA
buscaba en el fichero que cada CLAVE nombra: AGUJAS es un mapa CLAVE -> (fichero,
aguja) y el fichero es un dato, no un mecanismo. Lo unico que se anade son tres
constantes de ruta en el bloque PROPIO, junto a las AGUJAS que las usan. Ni una
funcion nueva, ni una condicion nueva, ni una tabla nueva.

Uso: python scripts/loop/_v72_construir_registrador_acta.py
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANCESTRO = os.path.join(RAIZ, "scripts", "loop", "vuelta71_registrar_acta70.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop", "vuelta72_registrar_acta71.py")
NL = chr(10)

CABECERA = '''# -*- coding: utf-8 -*-
"""vuelta72_registrar_acta71.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DE LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 71.

NO REESCRIBE NI UNA LINEA DE LAS SECCIONES DE ARRIBA: abre el fichero en modo
adosar y escribe detras. Es la via que esta pagina ya uso DOCE veces, la ultima
de ellas la del acta 70. Los numeros de linea de esas sedes NO se teclean aqui:
los que este instrumento ESCRIBE salen todos de una aguja.

LA MAQUINA SE COPIA, NO SE IMPORTA, y va dicho porque el acta 68 escribio la
regla en su D14 y las actas 69, 70 y 71 la dejaron en pie: importar vale DENTRO
DE LA MISMA VUELTA (dos instrumentos que nacen juntos y no pueden divergir), y el
carril de COPIAR es el que protege a los registradores de VUELTAS DISTINTAS.
Este es de otra vuelta que scripts/loop/vuelta71_registrar_acta70.py, asi que se
copia entero. Y NO SE COPIA A MANO, QUE ES RETECLEAR: lo copia
scripts/loop/_v72_construir_registrador_acta.py POR EXTRACCION, con un assert por
cada pieza. Lo unico propio son las RUTAS, las AGUJAS, las ANCLAS, los
NUMEROS_DECLARADOS, las NEGATIVAS y el texto importado.

LA MAQUINA NO CRECE EN ESTA VUELTA, Y SE DICE: la adjudicacion 3 del acta 69
congelo las tablas de los registradores y prohibio que crezcan sin encargo
previo. Aqui no entra ni un mecanismo nuevo. Los cuatro de la guarda de citas
son los del ancestro:

  1. LAS CITAS DE LINEA DEL TEXTO SE DERIVAN POR AGUJA, NO SE TECLEAN.
  2. TODA CITA DE LA FORMA linea NNNN SE COTEJA CONTRA EL CONTENIDO DE ESA LINEA
     ANTES DE ESCRIBIR, y toda CLAVE derivada se usa al menos una vez.
  3. LA RED ANCHA: todo numero de 3 a 5 digitos en NEGRITA sale de una aguja o
     esta declarado uno a uno con su motivo en NUMEROS_DECLARADOS.
  4. LAS AGUJAS NEGATIVAS: pares (CLAVE, aguja que esa linea NO debe contener).

TRES FICHEROS DE AGUJA QUE LAS VUELTAS ANTERIORES NO USABAN, y no son maquina
nueva: esta vuelta aplica TRES correcciones declaradas y cita la SEDE de cada una
por aguja en vez de teclearla. Dos de esas sedes no viven ni en la pagina ni en
el acta. AGUJAS siempre fue un mapa CLAVE -> (fichero, aguja) y el fichero es un
dato: se anaden OPS, GENERADOR y BANCO como constantes de ruta, y nada mas.

LAS TRES NEGATIVAS DE ESTA VUELTA, y las tres son de sustancia:
  a) el apartado a) parte en DOS citas lo que el acta 71 dice de la sede de las
     celdas malas (la linea del HECHO y la linea que nombra las TRES sedes
     reales), y si la linea del hecho ya nombrara el plan sellado la tabla
     estaria citando dos veces la misma cosa como si fueran dos medidas: se MIDE
     que la linea del hecho NO contiene PLAN_V70;
  b) la reclasificacion se apoya en que el contador VUELVE A CERO, y esa frase
     tiene que estar en la linea del CONTADOR y no en la de la definicion de la
     regla, que es la que la funda: se MIDE que la linea de la definicion NO
     contiene la palabra VUELVE;
  c) el apartado e) manda a lineas distintas la ADJUDICACION de la ficha de
     OP-L-03 (que dice NO ES PARADA) y la frase del acta que la llama LA MISMA
     frase que la de OP-U-02, porque la segunda es la que esta seccion DISCUTE
     con su medicion propia: se MIDE que la linea de la adjudicacion NO contiene
     la palabra MISMA.

LA IDEMPOTENCIA SE MIRA PRIMERO: si la seccion ya esta en la pagina, no se
escribe nada. Una pagina con la adjudicacion duplicada no falla, dice que si.

Uso:
  python scripts/loop/vuelta72_registrar_acta71.py [--simular]
"""
'''

PROPIO = '''
# LAS TRES RUTAS NUEVAS. Son DATO, no mecanismo: AGUJAS siempre fue un mapa
# CLAVE -> (fichero, aguja) y la maquina siempre busco en el fichero que la clave
# nombra. Viven aqui, en el bloque propio, junto a las agujas que las usan.
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
GENERADOR = os.path.join(RAIZ, "scripts", "loop", "generar_plan_del_lote.py")
BANCO = os.path.join(RAIZ, "scripts", "rumbos", "banco_rumbos.json")

# CLAVE -> (fichero, aguja). La aguja es el CONTENIDO que la cita afirma; el
# numero de linea sale de buscarla, nunca de teclearla.
AGUJAS = {
    # --- docs/loop/ACTA_AUDITOR.md, acta de la vuelta 71: las cabeceras ---
    "A71_ABRE": (ACTA, "# ACTA DE LA VUELTA 71 DEL AUDITOR (26 ago 2026, Fable 5)"),
    "A71_VERIF": (ACTA, "## 1. VERIFICACION POR CORRIDA PROPIA: TODO CALZA AL DIGITO"),
    "A71_CIEGA": (ACTA, "## 2. RELECTURA CIEGA: 5 DE 5 ACTOS CON SUPERVIVIENTE COINCIDENTE,"),
    "A71_RECLAS": (ACTA, "## 3. LA NOTICIA DE LA TANDA: LA CAIDA DE LA VUELTA 70 ESTABA MAL"),
    "A71_LIMPIA": (ACTA, "## 4. LA TANDA 71 DEL EJECUTOR: LIMPIA ENTERA"),
    "A71_QUINCE": (ACTA, "## 5. LOS QUINCE DISCUTIBLES, ADJUDICADOS: TODOS A FAVOR"),
    "A71_ADJUD": (ACTA, "## 6. ADJUDICACIONES NUEVAS DE ESTA ACTA"),
    "A71_AVERIAS": (ACTA, "## 7. AVERIAS: SEIS DEL EJECUTOR YA DECLARADAS, Y LAS MIAS CON NOMBRE"),
    "A71_METRICA": (ACTA, "## 8. METRICA DE CREDITO ACUMULADA"),
    "A71_PARADAS": (ACTA, "## 9. CONDICIONES DE PARADA, RECORRIDAS: NINGUNA SE CUMPLE HOY"),
    # la reclasificacion, pieza a pieza
    "A71_RECLAS_HECHO": (ACTA, "EL HECHO, MEDIDO HOY POR MI (sonda SEDE_CELDAS_MALAS_V70.txt): las dos"),
    "A71_RECLAS_CERO": (ACTA, "y 3) tienen CERO ocurrencias en docs/plan/03_FUSIONES.md, medido sobre"),
    "A71_RECLAS_SEDES": (ACTA, "TRES: docs/loop/PLAN_V70_OPU02_LOTE_F.json (el motivo sellado),"),
    "A71_RECLAS_ACTA": (ACTA, "MI ACTA 70 ESCRIBIO OTRA COSA: que el registro del lote F en"),
    "A71_RECLAS_CAIDA_ACTA": (ACTA, "y ES UNA CAIDA DE ACTA DEL AUDITOR: se declara aqui con nombre y entra"),
    "A71_RECLAS_LETRA": (ACTA, "LA RECLASIFICACION, POR LA LETRA Y NO POR CLEMENCIA: la regla de la"),
    "A71_RECLAS_DEFINE": (ACTA, "define la caida de CIFRA PUBLICADA como un veredicto, el marcador, o"),
    "A71_RECLAS_CONTADOR": (ACTA, "O CIFRA PUBLICADA VUELVE A CERO TANDAS. La correccion declarada que se"),
    "A71_RECLAS_MANEJO": (ACTA, "El manejo del ejecutor en su seccion 2.1 fue el debido: declaro la"),
    # la tanda limpia
    "A71_LIMPIA_CERO": (ACTA, "CERO caidas de clase, CERO de cifra publicada, CERO de reporte: toda"),
    # la ciega, acto a acto
    "A71_CIEGA_38": (ACTA, "- 38: UNA familia (la escala del problema y los roles de compra,"),
    "A71_CIEGA_39": (ACTA, "- 39: UNA familia (defensa en profundidad, Reason); ciego"),
    "A71_CIEGA_40": (ACTA, "- 40: UNA familia (la meta de traccion, Weinberg); ciego traction_goal"),
    "A71_CIEGA_41": (ACTA, "- 41: UNA familia (las cinco letras de DMADV dos veces dentro de un"),
    "A71_CIEGA_42": (ACTA, "- 42: UNA familia (el equipo multifuncional de Cooper); ciego"),
    "A71_CIEGA_CERO": (ACTA, "CERO discrepancias en la ciega. Los hechos del D5 confirmados"),
    # los quince discutibles
    "A71_D1": (ACTA, "1. D1 (el acto 39 pese a la familia_de_ids con nomina entera): A"),
    "A71_D2": (ACTA, "2. D2 (el 39 contra un cableado de 11 a 2): A FAVOR por la letra (el"),
    "A71_D3": (ACTA, "3. D3 (el 38 contra un cableado de 12 a 4): A FAVOR, misma letra, las"),
    "A71_D4": (ACTA, "4. D4 (el 42 elige al mas pequeno por la sola vara de condiciones): A"),
    "A71_D5": (ACTA, "5. D5 (las dos razones del 39 coronan distinto): A FAVOR por el"),
    "A71_D6": (ACTA, "6. D6 (tres supervivientes entran a la cola de costuras): A FAVOR. La"),
    "A71_D7": (ACTA, "7. D7 (tres nodos a siete pasos, segunda vuelta seguida): A FAVOR por"),
    "A71_D8": (ACTA, "8. D8 (nueve APPEND, tres en un acto): A FAVOR; los nueve son gestos"),
    "A71_D9": (ACTA, "9. D9 (dos CUBIERTO contra una condicion): A FAVOR; la marca existe"),
    "A71_D10": (ACTA, "10. D10 (los nexos de los INCISO son cosecha propia): A FAVOR. Los"),
    "A71_D11": (ACTA, "11. D11 (fundir con OP-L-03 en la entrada y su letra vieja): A FAVOR,"),
    "A71_D12": (ACTA, "12. D12 (el 41 sella siete perdidas y no repone nada): A FAVOR. Las"),
    "A71_D13": (ACTA, "13. D13 (una perdida sellada sobre un supuesto desmentido): A FAVOR."),
    "A71_D14": (ACTA, "14. D14 (dos salidas transcodificadas de cp1252 a UTF-8): A FAVOR con"),
    "A71_D15": (ACTA, "15. D15 (la correccion adosada al registro y no al modulo): A FAVOR,"),
    # las siete adjudicaciones
    "A71_ADJ1": (ACTA, "1. LA RECLASIFICACION DE LA CAIDA DE LA VUELTA 70 (seccion 3): caida"),
    "A71_ADJ2": (ACTA, "2. LA FRONTERA DEL DUENO CUANDO LA familia_de_ids CUBRE LA NOMINA"),
    "A71_ADJ2_TIPO": (ACTA, "   principio del acta 70 (adjudicacion 2) es de TIPO y no de"),
    "A71_ADJ2_RESOLUCION": (ACTA, "   TERCERA, y es la que decide el caso entero: la propia entrada trae"),
    "A71_ADJ2_BORDE": (ACTA, "   EJECUTARLA, no usurparla. EL BORDE QUEDA DICHO: esta adjudicacion"),
    "A71_ADJ3": (ACTA, "3. LA FICHA DE OP-L-03 (pregunta 4): NO ES PARADA y su CORRECCION"),
    "A71_ADJ3_MISMA": (ACTA, "   DECLARADA VA ENCARGADA en TAREA 1 de la vuelta 72. Es LA MISMA"),
    "A71_ADJ4": (ACTA, "4. EL MODULO DE CONTENIDO DE UNA VUELTA PASADA NO SE EDITA (pregunta"),
    "A71_ADJ5": (ACTA, "5. LAS SALIDAS SE ESCRIBEN EN UTF-8 DESDE EL ORIGEN (del D14): regla"),
    "A71_ADJ6": (ACTA, "6. EL PREFIJO DEL GENERADOR DE PLANES (pregunta 5): CORRECCION"),
    "A71_ADJ7": (ACTA, "7. EL ANCLA DUPLICADA DEL RUMBO (medicion mia, seccion 1): el"),
    # las condiciones de parada
    "A71_CIERRE03": (ACTA, "- CIERRE DE LA FASE 03 (la parada del fundador): NO SE CUMPLE TODAVIA."),
    "A71_CIERRE03_QUEDAN": (ACTA, "  Quedan 11 actos sin destino (33 nodos), dos de ellos con dueno (31 y"),
    # --- docs/plan/03_FUSIONES.md, sedes de esta misma pagina ---
    "PAG_ACTA70": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 70, REGISTRADAS AQUI"),
    "PAG_ACTA69": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 69, REGISTRADAS AQUI"),
    # --- LAS TRES SEDES DE LAS TRES CORRECCIONES DECLARADAS DE ESTA VUELTA ---
    "OPS_CORRECCION_OPL03": (OPS, "CORRECCION DECLARADA (2026-08-26, vuelta 72, TAREA 1 del encargo)"),
    "GEN_CORRECCION": (GENERADOR, "  8. EL PREFIJO DEL NOMBRE DEL FICHERO SE DERIVA DE --operacion EN VEZ DE TENER"),
    "BANCO_RUMBO": (BANCO, '"id": "nucleo_le_sirve_a_todo_el_mundo"'),
}

# ANCLAS: hay agujas que NO son unicas en todo el fichero porque el acta repite
# cabeceras de seccion vuelta tras vuelta. Para esas, la busqueda se restringe a
# una VENTANA que arranca en otra clave ya derivada, y se sigue exigiendo UNA
# sola ocurrencia DENTRO de la ventana.
# CLAVE -> (clave ancla, ventana en lineas).
ANCLAS = dict(
    [(c, ("A71_ABRE", 500)) for c in AGUJAS if c.startswith("A71_") and c != "A71_ABRE"]
)

# NUMEROS QUE EL TEXTO ESCRIBE EN NEGRITA Y NO SON CITAS DE LINEA, declarados
# uno a uno con su motivo. Todo lo demas que aparezca en negrita con 3 a 5
# digitos tiene que salir de una aguja, o es ROJO.
NUMEROS_DECLARADOS = {}

# (CLAVE, aguja que esa linea NO debe contener). La afirmacion negativa se MIDE,
# no se cree. Ver el docstring: las tres son de sustancia, no de adorno.
NEGATIVAS = [
    ("A71_RECLAS_HECHO", "PLAN_V70"),
    ("A71_RECLAS_DEFINE", "VUELVE"),
    ("A71_ADJ3", "MISMA"),
]
'''

CIERRE = '''
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v72_texto_acta71 import TEXTO  # noqa: E402

MARCA_IDEMPOTENCIA = "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 71"
'''


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    src = io.open(ANCESTRO, encoding="utf-8").read()
    print("=" * 78)
    print("CONSTRUCCION DE vuelta72_registrar_acta71.py POR EXTRACCION DEL ANCESTRO")
    print("  ancestro: %s (%d lineas)" % (os.path.basename(ANCESTRO), len(src.split(NL))))
    print("=" * 78)

    # PIEZA 1: el bloque de imports y rutas, del ancestro y literal.
    i1 = src.index("import argparse")
    f1 = src.index("# CLAVE -> (fichero, aguja)")
    imports = src[i1:f1]
    assert "PAGINA = os.path.join" in imports and "ACTA = os.path.join" in imports
    assert "NL = chr(10)" in imports
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
        ('print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 70 AL FINAL DE 03_FUSIONES.md")',
         'print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 71 AL FINAL DE 03_FUSIONES.md")'),
        ('print("YA ADOSADA: la seccion del acta 70 ya esta en la pagina. No se escribe nada.")',
         'print("YA ADOSADA: la seccion del acta 71 ya esta en la pagina. No se escribe nada.")'),
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
    cambios_rotulo = [("cita=vuelta:70", "cita=vuelta:71"),
                      ("ACTA DE LA VUELTA 70 DEL AUDITOR", "ACTA DE LA VUELTA 71 DEL AUDITOR"),
                      ("que es de la vuelta 70", "que es de la vuelta 71"),
                      ("el fichero es de la vuelta 71", "el fichero es de la vuelta 72")]
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
