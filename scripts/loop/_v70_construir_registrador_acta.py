# -*- coding: utf-8 -*-
"""_v70_construir_registrador_acta.py . ARMA scripts/loop/vuelta70_registrar_acta69.py
COPIANDO LA MAQUINA DE scripts/loop/vuelta69_registrar_acta68.py, NO RETECLEANDOLA.

POR QUE EXISTE. El acta 68 escribio la regla en su D14 y el acta 69 la dejo en
pie: importar una guarda vale DENTRO DE LA MISMA VUELTA; el carril de COPIAR es
el que protege a los registradores de VUELTAS DISTINTAS. El registrador del acta
69 es de OTRA vuelta que la maquina del acta 68, asi que la maquina se COPIA. Y
copiar a mano es retecleaar: este fichero la EXTRAE del ancestro y le pega
encima, con un assert por cada cambio, exactamente las piezas propias.

LO QUE SE COPIA LITERAL (medido con assert de presencia en el ancestro):
  lineas_de, derivar, negativas, sustituir, cotejar_texto, las cinco expresiones
  regulares, _CACHE y el cuerpo de main.

LO QUE ES PROPIO Y NO SE COPIA: el docstring, el ROTULO, AGUJAS, ANCLAS,
NUMEROS_DECLARADOS, NEGATIVAS, el modulo de texto que se importa y la marca de
idempotencia.

LA ADJUDICACION 3 DEL ACTA 69 SE RESPETA CON TODAS SUS LETRAS: la maquina NO
CRECE. Cero mecanismos nuevos, cero filas nuevas, cero columnas nuevas. Los
cuatro mecanismos de la guarda de citas salen del ancestro tal cual.

Uso: python scripts/loop/_v70_construir_registrador_acta.py
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANCESTRO = os.path.join(RAIZ, "scripts", "loop", "vuelta69_registrar_acta68.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop", "vuelta70_registrar_acta69.py")
NL = chr(10)

CABECERA = '''# -*- coding: utf-8 -*-
"""vuelta70_registrar_acta69.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DE LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 69.

NO REESCRIBE NI UNA LINEA DE LAS SECCIONES DE ARRIBA: abre el fichero en modo
adosar y escribe detras. Es la via que esta pagina ya uso DIEZ veces, la ultima
de ellas la del acta 68. Los numeros de linea de esas sedes NO se teclean aqui:
los que este instrumento ESCRIBE salen todos de una aguja.

LA MAQUINA SE COPIA, NO SE IMPORTA, y va dicho porque el acta 68 escribio la
regla en su D14 y el acta 69 la dejo en pie: importar vale DENTRO DE LA MISMA
VUELTA (dos instrumentos que nacen juntos y no pueden divergir), y el carril de
COPIAR es el que protege a los registradores de VUELTAS DISTINTAS. Este es de
otra vuelta que scripts/loop/vuelta69_registrar_acta68.py, asi que se copia
entero. Y NO SE COPIA A MANO, QUE ES RETECLEAR: lo copia
scripts/loop/_v70_construir_registrador_acta.py POR EXTRACCION, con un assert por
cada pieza. Lo unico propio son las AGUJAS, las ANCLAS, los NUMEROS_DECLARADOS,
las NEGATIVAS y el texto importado.

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

LAS TRES NEGATIVAS DE ESTA VUELTA, y las tres son de sustancia:
  a) esta seccion parte en DOS citas lo que el acta 69 dice de la linea base (el
     PASA DE 4 A 6 y el LA ARITMETICA NO SE TOCA), asi que se MIDE que la linea
     de lo adjudicado NO contiene la palabra ARITMETICA;
  b) la adjudicacion del acto 37 se cita como frase propia y no como coletilla
     del 31, asi que se MIDE que esa linea NO nombra al 31;
  c) el apartado g) afirma DOS cosas distintas del tramo (cero puentes y cero D
     internos por un lado, dos actos con dueno por otro) y las manda a lineas
     distintas, asi que se MIDE que la linea de los ceros NO dice dueno.

LA IDEMPOTENCIA SE MIRA PRIMERO: si la seccion ya esta en la pagina, no se
escribe nada. Una pagina con la adjudicacion duplicada no falla, dice que si.

Uso:
  python scripts/loop/vuelta70_registrar_acta69.py [--simular]
"""
'''

PROPIO = '''
# CLAVE -> (fichero, aguja). La aguja es el CONTENIDO que la cita afirma; el
# numero de linea sale de buscarla, nunca de teclearla.
AGUJAS = {
    # --- docs/loop/ACTA_AUDITOR.md, acta de la vuelta 69 ---
    "A69_ABRE": (ACTA, "# ACTA DE LA VUELTA 69 DEL AUDITOR (26 ago 2026, Fable 5)"),
    "A69_VERIF": (ACTA, "## 1. VERIFICACION POR CORRIDA PROPIA: TODO AL DIGITO, CERO CAIDAS"),
    "A69_PERDIDAS_FILA5": (ACTA, "  describe el mecanismo del pendiente 4 en su prosa y NO lleva la"),
    "A69_OPS_MENCION": (ACTA, "  sobre OPERACIONES.jsonl devuelve UNA sola mencion"),
    "A69_TRAMO": (ACTA, "- EL TRAMO AL CIERRE, RECONTADO POR MI: 47 filas, cerrados 26, quedan"),
    "A69_TRAMO_PUENTES": (ACTA, "  21 actos y 63 nodos; cero con par D interno (recontado sobre"),
    "A69_CIEGA": (ACTA, "## 2. RELECTURA CIEGA: 5 DE 5 COINCIDEN, TODAS DENTRO DEL MARCADO"),
    "A69_CIEGA_2838": (ACTA, "- 2838 (D5): mi lectura ciega dio A por contencion con superviviente"),
    "A69_CIEGA_839": (ACTA, "- 839 (D13, el par que cruza los dos libros del acto 26): ciega A,"),
    "A69_CIEGA_775": (ACTA, "- 775 (D1, la primera colision nueva): ciega B, el marco entero contra"),
    "A69_CIEGA_220": (ACTA, "- 220 y 482 (D6, los dos pares del acto 29): ciegas A y A, repeticion"),
    "A69_CIEGA_SUP": (ACTA, "Ademas adjudique CIEGO el superviviente en los dos actos discutidos:"),
    "A69_CIEGA_CERO": (ACTA, "Los dos coinciden con lo ejecutado. CERO discrepancias, CERO fuera del"),
    "A69_CAIDAS": (ACTA, "## 3. CAIDAS: CERO DEL EJECUTOR; TRES MANEJOS PROPIOS DECLARADOS"),
    "A69_CAIDAS_CERO": (ACTA, "Del ejecutor, en esta tanda: CERO de clase, CERO de cifra publicada,"),
    "A69_MANEJOS": (ACTA, "Del auditor, con nombre y sin cifra publicada de por medio:"),
    "A69_CATORCE": (ACTA, "## 4. LOS CATORCE DISCUTIBLES, ADJUDICADOS: TODOS A FAVOR"),
    "A69_D1": (ACTA, "1. D1 (dos colisiones fabricadas): A FAVOR. Predichas antes de tocar"),
    "A69_D2": (ACTA, "2. D2 (la puerta del 26 a nueve pasos): A FAVOR por el carril del D8"),
    "A69_D3": (ACTA, "3. D3 (cuatro INCISO en el acto 30): A FAVOR. Ninguno apilado, pasos"),
    "A69_D4": (ACTA, "4. D4 (el racimo del 29): A FAVOR. La particion 3 mas 2 esta MEDIDA"),
    "A69_D5": (ACTA, "5. D5 (el 2838 con discutible fuerte de su autor): A FAVOR. Mi ciega"),
    "A69_D6": (ACTA, "6. D6 (una sola vara con margen 2 contra 1): A FAVOR. La letra dice"),
    "A69_D7": (ACTA, "7. D7 (el tope del lote): A FAVOR. El contrato es entregar lo"),
    "A69_D8": (ACTA, "8. D8 (la fila de figura en tabla_declarado): A FAVOR, condiciones del"),
    "A69_D9": (ACTA, "9. D9 (cuatro atenuantes medidos): A FAVOR por el carril del D10 del"),
    "A69_D10": (ACTA, "10. D10 (la fila 5 sin frase sellada, 14 y no 15): A FAVOR. La cuenta"),
    "A69_D11": (ACTA, "11. D11 (el plan sellado dos veces): A FAVOR, el mismo carril del D15"),
    "A69_D12": (ACTA, "12. D12 (los nexos de los INCISO): A FAVOR. El trozo es verbatim"),
    "A69_D13": (ACTA, "13. D13 (ocho perdidas en el acto 26): A FAVOR. El 839 sostiene la"),
    "A69_D14": (ACTA, "14. D14 (dos puertas crecen el mismo dia): A FAVOR. La guarda 1B con"),
    "A69_ADJUD": (ACTA, "## 5. ADJUDICACIONES NUEVAS DE ESTA ACTA"),
    "A69_ADJ1": (ACTA, "1. LA LINEA BASE DEL CENSO DE COLISIONES PASA DE 4 A 6 (la pregunta 5"),
    "A69_ADJ1_CARRIL": (ACTA, "   del reporte). El carril es el mismo con el que la base paso de 2 a"),
    "A69_ADJ1_ENCARGO": (ACTA, "   puestos. El ejecutor aplica en TAREA 1 la CORRECCION DECLARADA"),
    "A69_ADJ1_ARIT": (ACTA, "   6, citando esta acta); LA ARITMETICA NO SE TOCA: la guarda sigue"),
    "A69_ADJ2": (ACTA, "2. EL ACTO 31 NO ES UNA FUSION DE OP-U-02, Y EL PREFIJO DEL LOTE F"),
    "A69_ADJ2_LETRA": (ACTA, "   ABRE EN EL 32. La letra esta en la ficha de OP-U-02 (criterio del"),
    "A69_ADJ2_DUENO": (ACTA, "   que el recomputo abra. El 31 tiene dueno medido (OP-F-04-WEI y"),
    "A69_ADJ2_SALTO": (ACTA, "   prefijo va DECLARADO con esta cita y no rompe el prefijo sin"),
    "A69_ADJ2_37": (ACTA, "   mismo vale para el 37 (OP-S-07) cuando el prefijo lo alcance."),
    "A69_ADJ3": (ACTA, "3. tabla_declarado QUEDA CONGELADA. La fila de duenos (vuelta 68) y la"),
    "A69_ADJ3_REGLA": (ACTA, "   ejecutor dijo: desde esta acta, ninguna fila ni columna nueva entra"),
    "A69_ADJ4": (ACTA, "4. EL PENDIENTE 6 NO PIDE DOCTRINA Y QUEDA ANOTADO: en lo que resta"),
    "A69_ADJ4_SALEN": (ACTA, "   que vengan saldran de la guarda 1B (dos o mas puertas), de la"),
    "A69_ADJ4_VOLUMEN": (ACTA, "   colisiones puede subir: cada una sigue exigiendo prediccion, sello"),
    "A69_METRICA": (ACTA, "## 6. METRICA DE CREDITO ACUMULADA"),
    "A69_ACUMULADO": (ACTA, "Acumulado: 469 relecturas (464 mas las cinco ciegas), 799 puestos (794"),
    "A69_RACHAS": (ACTA, "Rachas: CLASE O CIFRA sigue EN CERO (dos tandas limpias seguidas, 68 y"),
    "A69_PARADAS": (ACTA, "## 7. CONDICIONES DE PARADA, RECORRIDAS: NINGUNA SE CUMPLE"),
    "A69_CIERRE03": (ACTA, "- CIERRE DE LA FASE 03 (la parada del fundador): NO SE CUMPLE TODAVIA."),
    "A69_CIERRE03_CATORCE": (ACTA, "  Quedan 21 actos y 63 nodos del tramo, dos actos con dueno, la mesa"),
    # --- docs/plan/03_FUSIONES.md, sedes de esta misma pagina ---
    "PAG_ACTA68": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 68, REGISTRADAS AQUI"),
    "PAG_ACTA67": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 67, REGISTRADAS AQUI"),
    "PAG_ACTA52": (PAGINA, "### LAS TRES ADJUDICACIONES DEL ACTA DE LA VUELTA 52, REGISTRADAS AQUI"),
    "PAG_ACTA57": (PAGINA, "### LA ADJUDICACION DEL ACTA 57 SOBRE EL **ACTO 25**"),
    "PAG_LOTE_E": (PAGINA, "## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE E`"),
    "PAG_TRAMO_CIERRE_E": (PAGINA, "### h) **LO QUE QUEDA DEL TRAMO AL CIERRE DE ESTE LOTE, MEDIDO Y NO ARRASTRADO**"),
    "PAG_COLISIONES_E": (PAGINA, "### g) **LAS DOS COLISIONES DE CLASE QUE ESTA VUELTA FABRICA, PREDICHAS"),
    "PAG_ACTO27": (PAGINA, "### e) **EL `ACTO 27`: `DECLARADO Y NO FUNDIDO` POR `P.10`, CON LA `ESTRELLA` ENCIMA**"),
    "PAG_PENDIENTES68": (PAGINA, "### g) **LOS PENDIENTES HEREDADOS, NOMBRADOS CON SU DESTINO**"),
    "PAG_LINEA_BASE": (PAGINA, "### c) **UNA COLISION QUE FABRICA UNA FUSION TIENE DE DUENA A QUIEN LA FABRICA"),
    "PAG_ACTO1_P10": (PAGINA, "### a) **EL ACTO 1: `DECLARADO Y NO FUNDIDO` POR `P.10`"),
    "PAG_CUARTO_MOTIVO": (PAGINA, "### d) **EL CUARTO MOTIVO SELLADO DEL `DECLARADO Y NO FUNDIDO`"),
    "PAG_GUARDA_1B": (PAGINA, "### c) **UN ACTO CON DOS O MAS PUERTAS CIERRA `DECLARADO Y NO FUNDIDO`"),
    "PAG_P5_MOTIVO": (PAGINA, "### b) **UN ACTO CUYO `P.5` CONTESTA QUE NO ES UNA FAMILIA CIERRA"),
    "PAG_TRANSITO": (PAGINA, "### e) **EL TRANSITO DEL ACTO CON FORMA `EMPATE SIN VARA`"),
}

# ANCLAS: hay agujas que NO son unicas en todo el fichero porque el acta repite
# cabeceras de seccion vuelta tras vuelta. Para esas, la busqueda se restringe a
# una VENTANA que arranca en otra clave ya derivada, y se sigue exigiendo UNA
# sola ocurrencia DENTRO de la ventana.
# CLAVE -> (clave ancla, ventana en lineas).
ANCLAS = dict(
    [(c, ("A69_ABRE", 500)) for c in AGUJAS if c.startswith("A69_") and c != "A69_ABRE"]
)

# NUMEROS QUE EL TEXTO ESCRIBE EN NEGRITA Y NO SON CITAS DE LINEA, declarados
# uno a uno con su motivo. Todo lo demas que aparezca en negrita con 3 a 5
# digitos tiene que salir de una aguja, o es ROJO.
NUMEROS_DECLARADOS = {
    "2838": "el puesto de la primera relectura ciega del acta 69, el A por contencion del acto 30",
    "839": "el puesto de la ciega del acto 26, el par que cruza los dos libros",
    "775": "el puesto de la ciega de la primera colision nueva del acto 25",
    "220": "el primero de los dos puestos de la ciega del acto 29",
    "482": "el segundo de los dos puestos de la ciega del acto 29",
}

# (CLAVE, aguja que esa linea NO debe contener). La afirmacion negativa se MIDE,
# no se cree. Ver el docstring: las tres son de sustancia, no de adorno.
NEGATIVAS = [
    ("A69_ADJ1", "ARITMETICA"),
    ("A69_ADJ2_37", "31"),
    ("A69_TRAMO_PUENTES", "dueno"),
]
'''

CIERRE = '''
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v70_texto_acta69 import TEXTO  # noqa: E402

MARCA_IDEMPOTENCIA = "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 69"
'''


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    src = io.open(ANCESTRO, encoding="utf-8").read()
    print("=" * 78)
    print("CONSTRUCCION DE vuelta70_registrar_acta69.py POR EXTRACCION DEL ANCESTRO")
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
        ('print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 68 AL FINAL DE 03_FUSIONES.md")',
         'print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 69 AL FINAL DE 03_FUSIONES.md")'),
        ('print("Con la guarda de citas heredada entera de la vuelta 68 (cuatro mecanismos).")',
         'print("Con la guarda de citas copiada entera del ancestro (cuatro mecanismos, cero nuevos).")'),
        ('print("YA ADOSADA: la seccion del acta 68 ya esta en la pagina. No se escribe nada.")',
         'print("YA ADOSADA: la seccion del acta 69 ya esta en la pagina. No se escribe nada.")'),
    ]
    for viejo, nuevo in cambios:
        assert cuerpo.count(viejo) == 1, viejo
        cuerpo = cuerpo.replace(viejo, nuevo)
    print("  PIEZA 3 main entero       : %d lineas, EXTRAIDA con 3 rotulos cambiados"
          % cuerpo.count(NL))

    # PIEZA 4: EL ROTULO DEL FICHERO HIJO, EXTRAIDO DEL ANCESTRO Y NO TECLEADO
    # AQUI. Va por extraccion por dos motivos y los dos se dicen: es la misma
    # doctrina de copiar y no retecleaar que rige la maquina, y un rotulo escrito
    # DENTRO del constructor es un ROTULO HUERFANO para el barrido de titulos,
    # porque el titulo que cubre no es el del constructor sino el del hijo. El
    # barrido lo cazo en su primera corrida de esta vuelta y por eso se cambio.
    i4 = src.index("# ROTULO titulo")
    f4 = src.index(NL, i4)
    rotulo = src[i4:f4]
    cambios_rotulo = [("cita=vuelta:68", "cita=vuelta:69"),
                      ("ACTA DE LA VUELTA 68 DEL AUDITOR", "ACTA DE LA VUELTA 69 DEL AUDITOR"),
                      ("que es de la vuelta 68", "que es de la vuelta 69"),
                      ("el fichero es de la vuelta 69", "el fichero es de la vuelta 70")]
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
