# -*- coding: utf-8 -*-
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
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:69 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 69 DEL AUDITOR" corte=2026-08-26 motivo="el titulo nombra el ACTA que este registro transcribe, que es de la vuelta 69; el fichero es de la vuelta 70 y por eso el numero no calza con su propia vuelta a proposito"
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
NL = chr(10)

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

RE_MARCA = re.compile(r"\[\[([A-Z0-9_]+)\]\]")
RE_VERBATIM = re.compile(r"\[\[VERBATIM:([A-Z0-9_]+):(\d+)\]\]")
# LA FORMA CANONICA DE UNA CITA DE LINEA EN EL TEXTO. Todo numero que aparezca
# asi tiene que salir de una aguja.
RE_CITA = re.compile(r"l[ií]neas?\s+\*\*(\d+)\*\*(?:\s+a\s+\*\*(\d+)\*\*)?")
# Y LA RED MAS ANCHA: TODO numero de 3 a 5 digitos que el texto ponga en
# negrita. En las tablas la cita de linea va sola en su celda, sin la palabra
# linea delante, y sin esta segunda red esas celdas quedarian fuera del cotejo.
RE_NEGRITA = re.compile(r"\*\*(\d{3,5})\*\*")

_CACHE = {}


def lineas_de(ruta):
    if ruta not in _CACHE:
        _CACHE[ruta] = io.open(ruta, encoding="utf-8").read().split(NL)
    return _CACHE[ruta]


def derivar(fallos, callado=False):
    """CONDICION 1: cada cita sale de buscar su aguja, y la aguja tiene que ser
    UNICA en su fichero. Devuelve {CLAVE: (numero, ruta, aguja)}."""
    if not callado:
        print()
        print("  --- GUARDA DE CITAS, CONDICION 1: LAS CITAS SE DERIVAN POR AGUJA ---")
    derivadas = {}
    # las claves sin ancla primero: una clave anclada necesita su ancla derivada.
    orden = ([c for c in sorted(AGUJAS) if c not in ANCLAS]
             + [c for c in sorted(AGUJAS) if c in ANCLAS])
    for clave in orden:
        ruta, aguja = AGUJAS[clave]
        lineas = lineas_de(ruta)
        desde, hasta, etq_ventana = 0, len(lineas), "todo el fichero"
        if clave in ANCLAS:
            ancla, ventana = ANCLAS[clave]
            if ancla not in derivadas:
                fallos.append("la clave %s se ancla en %s y %s no se pudo derivar"
                              % (clave, ancla, ancla))
                continue
            desde = derivadas[ancla][0] - 1
            hasta = min(len(lineas), desde + ventana)
            etq_ventana = "ventana %d..%d" % (desde + 1, hasta)
        hallazgos = [i + 1 for i in range(desde, hasta) if aguja in lineas[i]]
        if len(hallazgos) != 1:
            fallos.append("la aguja de %s aparece %d veces en %s (%s; tiene que aparecer 1)"
                          % (clave, len(hallazgos), os.path.basename(ruta), etq_ventana))
            if not callado:
                print("     %-24s ROJO  %d hallazgos en %s" % (clave, len(hallazgos), etq_ventana))
            continue
        n = hallazgos[0]
        derivadas[clave] = (n, ruta, aguja)
        if not callado:
            print("     %-24s %-6d %s" % (clave, n, lineas[n - 1].strip()[:78]))
    return derivadas


def negativas(derivadas, fallos):
    """LAS AGUJAS NEGATIVAS: lo que una linea NO debe decir, medido."""
    print()
    print("  --- GUARDA DE CITAS, AGUJAS NEGATIVAS ---")
    for clave, aguja in NEGATIVAS:
        if clave not in derivadas:
            continue
        n, ruta, _ = derivadas[clave]
        real = lineas_de(ruta)[n - 1]
        if aguja in real:
            fallos.append("la linea %d (%s) SI contiene %r y no deberia" % (n, clave, aguja))
            print("     %-22s ROJO  la linea %d contiene %r" % (clave, n, aguja))
        else:
            print("     %-22s OK    la linea %d NO contiene %r" % (clave, n, aguja[:44]))


def sustituir(texto, derivadas, fallos, usos):
    """Sustituye [[VERBATIM:CLAVE:N]] y [[CLAVE]] por lo medido, contando cuantas
    veces se usa cada clave (una clave con cero usos es una cita muerta)."""
    def rep_verbatim(m):
        clave, cuantas = m.group(1), int(m.group(2))
        if clave not in derivadas:
            fallos.append("VERBATIM sobre clave no derivada: %s" % clave)
            return m.group(0)
        n, ruta, _ = derivadas[clave]
        usos[clave] = usos.get(clave, 0) + 1
        crudas = lineas_de(ruta)[n - 1:n - 1 + cuantas]
        return NL.join("> " + c for c in crudas)

    texto = RE_VERBATIM.sub(rep_verbatim, texto)

    def rep(m):
        clave = m.group(1)
        if clave not in derivadas:
            fallos.append("marca sin aguja derivada: %s" % clave)
            return m.group(0)
        usos[clave] = usos.get(clave, 0) + 1
        return str(derivadas[clave][0])

    return RE_MARCA.sub(rep, texto)


def cotejar_texto(texto, derivadas, fallos, usos):
    """CONDICION 2: toda cita de la forma linea NNNN del texto FINAL sale de una
    aguja derivada, y toda aguja derivada se usa al menos una vez."""
    print()
    print("  --- GUARDA DE CITAS, CONDICION 2: EL TEXTO NUEVO, COTEJADO ---")
    numeros = {}
    for clave, (n, ruta, aguja) in derivadas.items():
        numeros.setdefault(n, []).append((clave, ruta, aguja))
    halladas = []
    for m in RE_CITA.finditer(texto):
        for g in m.groups():
            if g:
                halladas.append(int(g))
    usadas = set()
    malas = 0
    for n in sorted(set(halladas)):
        if n not in numeros:
            fallos.append("el texto cita la linea %d y ese numero NO sale de ninguna aguja" % n)
            print("     linea %-6d ROJO  no sale de ninguna aguja" % n)
            malas += 1
            continue
        usadas.add(n)
        clave, ruta, aguja = numeros[n][0]
        real = lineas_de(ruta)[n - 1]
        ok = aguja in real
        if not ok:
            fallos.append("el texto cita la linea %d y su contenido no calza con la aguja" % n)
            malas += 1
        print("     linea %-6d %-4s %-24s %s"
              % (n, "OK" if ok else "MAL", clave, real.strip()[:58]))
    print()
    print("     citas de linea en forma canonica: %d distintas | MALAS: %d"
          % (len(set(halladas)), malas))

    # LA RED ANCHA: todo numero en negrita de 3 a 5 digitos.
    negritas = sorted(set(int(m.group(1)) for m in RE_NEGRITA.finditer(texto)))
    fuera = []
    for n in negritas:
        if n in numeros:
            usadas.add(n)
            continue
        if str(n) in NUMEROS_DECLARADOS:
            continue
        fuera.append(n)
    if fuera:
        for n in fuera:
            fallos.append("el texto escribe **%d** en negrita y ni sale de una aguja "
                          "ni esta en NUMEROS_DECLARADOS" % n)
        print("     ROJO: numeros en negrita sin aguja ni declaracion: %s"
              % ", ".join(str(n) for n in fuera))
    else:
        print("     numeros en negrita de 3 a 5 digitos: %d, TODOS con aguja o declarados "
              "(%s)" % (len(negritas), ", ".join(sorted(NUMEROS_DECLARADOS))))

    # NINGUNA CITA MUERTA: toda clave derivada se usa al menos una vez.
    sin_usar = sorted(c for c in derivadas if usos.get(c, 0) == 0)
    if sin_usar:
        fallos.append("hay %d aguja(s) derivada(s) que el texto no usa: %s"
                      % (len(sin_usar), ", ".join(sin_usar)))
        print("     ROJO: agujas derivadas sin usar: %s" % ", ".join(sin_usar))
    else:
        print("     todas las %d agujas derivadas se usan al menos una vez: OK"
              % len(derivadas))


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v70_texto_acta69 import TEXTO  # noqa: E402

MARCA_IDEMPOTENCIA = "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 69"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 69 AL FINAL DE 03_FUSIONES.md")
    print("Con la guarda de citas copiada entera del ancestro (cuatro mecanismos, cero nuevos).")
    print("=" * 78)

    # LA IDEMPOTENCIA SE MIRA PRIMERO, y no despues de derivar: es la correccion
    # que la vuelta 68 declaro en su averia 7.2. Rojo tambien es seguro (no
    # escribe), pero la respuesta correcta a una pagina ya registrada es decirlo,
    # no fallar.
    crudo = io.open(PAGINA, encoding="utf-8").read()
    if MARCA_IDEMPOTENCIA in crudo:
        print()
        print("YA ADOSADA: la seccion del acta 69 ya esta en la pagina. No se escribe nada.")
        return 0

    fallos = []
    derivadas = derivar(fallos)
    negativas(derivadas, fallos)
    usos = {}
    texto = sustituir(TEXTO, derivadas, fallos, usos)
    cotejar_texto(texto, derivadas, fallos, usos)

    for mal, nombre in ((chr(8212), "guion largo"), (chr(8211), "guion medio")):
        if mal in texto:
            fallos.append("el texto trae un %s" % nombre)
    if RE_MARCA.search(texto) or RE_VERBATIM.search(texto):
        fallos.append("quedan marcas sin sustituir en el texto final")

    print()
    print("  agujas derivadas: %d | FALLOS: %d" % (len(derivadas), len(fallos)))
    if fallos:
        print()
        print("ROJO: %d fallo(s) y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    antes = len(crudo.split(NL))
    print()
    print("  la pagina tiene %d lineas y el texto anade %d" % (antes, texto.count(NL)))
    if a.simular:
        print()
        print("  SIMULACION: no se escribe nada. El texto empieza asi:")
        for l in texto.split(NL)[:8]:
            print("     %s" % l[:100])
        print()
        print("FIN")
        return 0

    with io.open(PAGINA, "a", encoding="utf-8", newline=NL) as fh:
        fh.write(texto)
    despues = len(io.open(PAGINA, encoding="utf-8").read().split(NL))
    print()
    print("GUARDAS TRAS ESCRIBIR")
    print("  lineas antes %d, despues %d (delta %d)" % (antes, despues, despues - antes))
    txt = io.open(PAGINA, encoding="utf-8").read()
    print("  guiones largos %d, guiones medios %d"
          % (txt.count(chr(8212)), txt.count(chr(8211))))
    # RE-COTEJO TRAS ADOSAR: las sedes de arriba no se movieron. Se mide sobre
    # LAS LINEAS DE ARRIBA SOLAS (las que habia antes de adosar), y no sobre la
    # pagina entera, que es la correccion de la averia 7.3 de la vuelta 68.
    _CACHE.clear()
    lineas_de(PAGINA)
    _CACHE[PAGINA] = _CACHE[PAGINA][:antes]
    re_fallos = []
    re_derivadas = derivar(re_fallos, callado=True)
    movidas = [c for c in derivadas
               if c in re_derivadas and re_derivadas[c][0] != derivadas[c][0]]
    print("  re-cotejo tras adosar: %d agujas re-derivadas" % len(re_derivadas))
    print("  las sedes de arriba siguen en su linea: %s"
          % ("OK (%d de %d)" % (len(derivadas), len(derivadas)) if not movidas
             else "ROJO, se movieron: %s" % ", ".join(movidas)))
    if movidas or re_fallos:
        return 1
    print()
    print("VERDE: registro adosado y nada de arriba reescrito.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
