# -*- coding: utf-8 -*-
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
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:71 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 71 DEL AUDITOR" corte=2026-08-26 motivo="el titulo nombra el ACTA que este registro transcribe, que es de la vuelta 71; el fichero es de la vuelta 72 y por eso el numero no calza con su propia vuelta a proposito"
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
NL = chr(10)

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
from _v72_texto_acta71 import TEXTO  # noqa: E402

MARCA_IDEMPOTENCIA = "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 71"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 71 AL FINAL DE 03_FUSIONES.md")
    print("Con la guarda de citas copiada entera del ancestro (cuatro mecanismos, cero nuevos).")
    print("=" * 78)

    # LA IDEMPOTENCIA SE MIRA PRIMERO, y no despues de derivar: es la correccion
    # que la vuelta 68 declaro en su averia 7.2. Rojo tambien es seguro (no
    # escribe), pero la respuesta correcta a una pagina ya registrada es decirlo,
    # no fallar.
    crudo = io.open(PAGINA, encoding="utf-8").read()
    if MARCA_IDEMPOTENCIA in crudo:
        print()
        print("YA ADOSADA: la seccion del acta 71 ya esta en la pagina. No se escribe nada.")
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
