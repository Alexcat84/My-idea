# -*- coding: utf-8 -*-
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
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:73 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 73 DEL AUDITOR" corte=2026-08-26 motivo="el titulo nombra el ACTA que este registro transcribe, que es de la vuelta 73; el fichero es de la vuelta 74 y por eso el numero no calza con su propia vuelta a proposito"
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
NL = chr(10)

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
from _v74_texto_acta73 import TEXTO  # noqa: E402

MARCA_IDEMPOTENCIA = "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 73"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 73 AL FINAL DE 03_FUSIONES.md")
    print("Con la guarda de citas copiada entera del ancestro (cuatro mecanismos, cero nuevos).")
    print("=" * 78)

    # LA IDEMPOTENCIA SE MIRA PRIMERO, y no despues de derivar: es la correccion
    # que la vuelta 68 declaro en su averia 7.2. Rojo tambien es seguro (no
    # escribe), pero la respuesta correcta a una pagina ya registrada es decirlo,
    # no fallar.
    crudo = io.open(PAGINA, encoding="utf-8").read()
    if MARCA_IDEMPOTENCIA in crudo:
        print()
        print("YA ADOSADA: la seccion del acta 73 ya esta en la pagina. No se escribe nada.")
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
