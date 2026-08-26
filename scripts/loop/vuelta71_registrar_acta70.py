# -*- coding: utf-8 -*-
"""vuelta71_registrar_acta70.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DE LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 70.

NO REESCRIBE NI UNA LINEA DE LAS SECCIONES DE ARRIBA: abre el fichero en modo
adosar y escribe detras. Es la via que esta pagina ya uso ONCE veces, la ultima
de ellas la del acta 69. Los numeros de linea de esas sedes NO se teclean aqui:
los que este instrumento ESCRIBE salen todos de una aguja.

LA MAQUINA SE COPIA, NO SE IMPORTA, y va dicho porque el acta 68 escribio la
regla en su D14 y las actas 69 y 70 la dejaron en pie: importar vale DENTRO DE
LA MISMA VUELTA (dos instrumentos que nacen juntos y no pueden divergir), y el
carril de COPIAR es el que protege a los registradores de VUELTAS DISTINTAS.
Este es de otra vuelta que scripts/loop/vuelta70_registrar_acta69.py, asi que se
copia entero. Y NO SE COPIA A MANO, QUE ES RETECLEAR: lo copia
scripts/loop/_v71_construir_registrador_acta.py POR EXTRACCION, con un assert por
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
  a) esta seccion parte en DOS citas lo que el acta 70 dice del cableado (la
     linea de las cifras CRUDAS y la de las cifras del INSTRUMENTO), y si las dos
     mitades cayeran en la misma linea la correccion citaria su propio error como
     si fuera su remedio: se MIDE que la linea de las crudas NO contiene la cifra
     buena;
  b) la adjudicacion de la linea base se cita aparte de su aritmetica, asi que se
     MIDE que la linea de lo adjudicado NO contiene la palabra aritmetica;
  c) el apartado h) manda a lineas distintas las DOS consecuencias de las puertas
     (el acto 44 que cierra DECLARADO por la guarda 1B, y los actos 46 y 51 que
     funden con su puerta viva), asi que se MIDE que la linea de los que FUNDEN
     NO nombra al 44.

LA IDEMPOTENCIA SE MIRA PRIMERO: si la seccion ya esta en la pagina, no se
escribe nada. Una pagina con la adjudicacion duplicada no falla, dice que si.

Uso:
  python scripts/loop/vuelta71_registrar_acta70.py [--simular]
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:70 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 70 DEL AUDITOR" corte=2026-08-26 motivo="el titulo nombra el ACTA que este registro transcribe, que es de la vuelta 70; el fichero es de la vuelta 71 y por eso el numero no calza con su propia vuelta a proposito"
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
    # --- docs/loop/ACTA_AUDITOR.md, acta de la vuelta 70 ---
    "A70_ABRE": (ACTA, "# ACTA DE LA VUELTA 70 DEL AUDITOR (26 ago 2026, Fable 5)"),
    "A70_VERIF": (ACTA, "## 1. VERIFICACION POR CORRIDA PROPIA: CASI TODO AL DIGITO, Y DOS"),
    "A70_CIEGA": (ACTA, "## 2. RELECTURA CIEGA: 6 DE 6 COINCIDEN, MAS TRES SUPERVIVIENTES"),
    "A70_CAIDA": (ACTA, "## 3. UNA CAIDA DE CIFRA PUBLICADA: EL CABLEADO CITADO EN CRUDO, SIN"),
    "A70_REPORTE": (ACTA, "## 4. DOS CAIDAS DE REPORTE, CON NOMBRE"),
    "A70_CATORCE": (ACTA, "## 5. LOS CATORCE DISCUTIBLES, ADJUDICADOS: TODOS A FAVOR"),
    "A70_ADJUD": (ACTA, "## 6. ADJUDICACIONES NUEVAS DE ESTA ACTA"),
    "A70_METRICA": (ACTA, "## 8. METRICA DE CREDITO ACUMULADA"),
    "A70_PARADAS": (ACTA, "## 9. CONDICIONES DE PARADA, RECORRIDAS: NINGUNA SE CUMPLE HOY"),
    # la caida de cifra publicada, pieza a pieza
    "A70_CAIDA_HECHO": (ACTA, "EL HECHO, MEDIDO: el registro del lote F en docs/plan/03_FUSIONES.md"),
    "A70_CAIDA_CRUDAS": (ACTA, "publica el cableado del acto 34 como 6 contra 5 y 2, y el del acto 36"),
    "A70_CAIDA_BUENAS": (ACTA, "worktree, identicas) mide 6 contra 4 y 2, y 4 contra 3 y 2. La causa"),
    "A70_CAIDA_CAUSA": (ACTA, "numeros publicados son el conteo CRUDO de las listas de enlaces, sin"),
    "A70_CAIDA_P1": (ACTA, "P.1 con estas palabras: TODO ID PASA POR EL RESOLUTOR ANTES DE"),
    "A70_CAIDA_NO_MUEVE": (ACTA, "LO QUE NO SE MUEVE: ningun ganador cambia (6 mayor que 4 y 5 mayor"),
    "A70_CAIDA_CONTADOR": (ACTA, "CERO A UNA TANDA. Dos tandas seguidas serian PARADA: la vuelta 72 lo"),
    # las dos caidas de reporte
    "A70_REP_PUERTAS": (ACTA, "1. LAS PUERTAS DE LOS QUE QUEDAN NO SON CERO. La seccion 10 del"),
    "A70_PUERTAS_CUATRO": (ACTA, "   varas_n_arias sobre los 16: CUATRO tienen puertas. El 31 una"),
    "A70_PUERTAS_ESPECIE": (ACTA, "   es una busqueda no corrida afirmada como corrida, que es"),
    "A70_REP_D3": (ACTA, "2. EL DESGLOSE DEL D3: el reporte dice que el superviviente del acto"),
    "A70_RACHA_REPORTE": (ACTA, "acumulan para la parada. La racha de reporte queda en UNA tanda (la"),
    # la ciega, puesto a puesto
    "A70_CIEGA_880": (ACTA, "- 880 (D8, acto 35): ciega A por contencion (el marcador visual es el"),
    "A70_CIEGA_2233": (ACTA, "- 2233 (D6, acto 34): ciega A (mismo gesto: sustituir el ritual de"),
    "A70_CIEGA_2272": (ACTA, "- 2272 (D6, acto 34): ciega A (el mismo ciclo de culpa contado dos"),
    "A70_CIEGA_2562": (ACTA, "- 2562 (acto 36): ciega A (el mismo artefacto; el paso 8 de"),
    "A70_CIEGA_2639": (ACTA, "- 2639 (D4, acto 36): ciega A con residuo capacitar y auditar."),
    "A70_CIEGA_279": (ACTA, "- 279 (la colision): ciega B (la etapa entera contra la senal que"),
    "A70_CIEGA_SUP": (ACTA, "Supervivientes adjudicados CIEGOS antes de destapar: en el 34 elegi"),
    "A70_CIEGA_SALDO": (ACTA, "CERO discrepancias en la ciega. PERO la verificacion de la seccion 1"),
    # los catorce discutibles
    "A70_D1": (ACTA, "1. D1 (el acto 34 pese a la entrada familia_de_ids con OP-S-09): A"),
    "A70_D2": (ACTA, "2. D2 (la colision fabricada y la base): A FAVOR. Predicha antes de"),
    "A70_D3": (ACTA, "3. D3 (el acto 33 contra el cableado 9 a 3): A FAVOR por la letra: el"),
    "A70_D4": (ACTA, "4. D4 (diez pasos): A FAVOR por el carril del catalogo mas rico"),
    "A70_D5": (ACTA, "5. D5 (dos nodos mas a ocho): A FAVOR, mismo carril; tres nodos de"),
    "A70_D6": (ACTA, "6. D6 (las dos razones del 34 coronan distinto): A FAVOR. Mi ciega"),
    "A70_D7": (ACTA, "7. D7 (el 32 por cableado con margen de uno): A FAVOR. Contenido"),
    "A70_D8": (ACTA, "8. D8 (el 35 contra la vara de pasos): A FAVOR. CHOCAN lo decide la"),
    "A70_D9": (ACTA, "9. D9 (seis APPEND de paso): A FAVOR; los seis son gestos que las"),
    "A70_D10": (ACTA, "10. D10 (el 33 triplica condiciones): A FAVOR por la puerta del acta"),
    "A70_D11": (ACTA, "11. D11 (los nexos de los INCISO): A FAVOR. Los cinco trozos son"),
    "A70_D12": (ACTA, "12. D12 (el fichero del marcador de apertura generado al cierre): A"),
    "A70_D13": (ACTA, "13. D13 (dos instrumentos nuevos sin encargo): A FAVOR con la"),
    "A70_D14": (ACTA, "14. D14 (arreglar las regresiones propias en vez de declarar base"),
    # las cuatro adjudicaciones
    "A70_ADJ1": (ACTA, "1. LA LINEA BASE DEL CENSO DE COLISIONES PASA DE 6 A 7 (pregunta 5)."),
    "A70_ADJ1_TRES": (ACTA, "   una fusion, PREDICHA, PUBLICADA con duena sellada y registrada con"),
    "A70_ADJ1_CARRIL": (ACTA, "   mismo carril (2 por el acta 64, 4 por el acta 66, 6 por el acta"),
    "A70_ADJ1_ENCARGO": (ACTA, "   69, 7 por esta) y la correccion declarada del defecto de --base va"),
    "A70_ADJ2": (ACTA, "2. LA FRONTERA DEL DUENO, LEIDA SOBRE SU SUJETO (pregunta 6, la de"),
    "A70_ADJ2_TRES": (ACTA, "   MEDIDO con tres fuentes: los dos campos duenos_* del fichero"),
    "A70_ADJ2_FAMILIA": (ACTA, "   nombra una operacion sobre PARTE de la nomina NO es dueno del"),
    "A70_ADJ2_DEBE": (ACTA, "   fusion le debe es dejarselo servible, cosa que quedo medida y"),
    "A70_ADJ2_ARIT": (ACTA, "   aritmetica (las 47 entradas tipo acto del tramo nombran OP-U-02:"),
    "A70_ADJ2_EXT": (ACTA, "   Extension citable, no doctrina nueva."),
    "A70_ADJ3_REGLA": (ACTA, "   Desde esta acta, TODA cifra de cableado que se publique sale de la"),
    "A70_ADJ4_PUERTAS": (ACTA, "   lo que resta del tramo SI quedan puertas (44 con DOS, 46 y 51 con"),
    "A70_ADJ4_DOS": (ACTA, "   posibles son DOS: la guarda 1B con dos o mas puertas (el acto 44,"),
    "A70_ADJ4_54": (ACTA, "   Los actos 46 y 51 funden con su puerta sobreviviendo (acta 54,"),
    # los pendientes, el credito y las paradas
    "A70_PERDIDAS": (ACTA, "- LA CUENTA AGREGADA DE PERDIDAS, RECONTADA POR MI sobre el plan"),
    "A70_ESTADO_OPS": (ACTA, "  entradas de inventario, contadas por mi. OPERACIONES.jsonl y"),
    "A70_ACUMULADO": (ACTA, "Acumulado: 475 relecturas (469 mas las seis ciegas), 805 puestos (799"),
    "A70_RACHAS": (ACTA, "Rachas: CLASE O CIFRA PUBLICADA pasa de cero a UNA tanda (la caida de"),
    "A70_RACHAS_71": (ACTA, "de la vuelta 71 trae otra caida de clase o de cifra publicada, ES"),
    "A70_CIERRE03": (ACTA, "- CIERRE DE LA FASE 03 (la parada del fundador): NO SE CUMPLE"),
    "A70_CIERRE03_16": (ACTA, "  TODAVIA. Quedan 16 actos sin destino (48 nodos), dos de ellos con"),
    # --- docs/plan/03_FUSIONES.md, sedes de esta misma pagina ---
    "PAG_ACTA69": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 69, REGISTRADAS AQUI"),
    "PAG_ACTA68": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 68, REGISTRADAS AQUI"),
    "PAG_LOTE_F": (PAGINA, "## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE F`"),
    "PAG_TRAMO_CIERRE_F": (PAGINA, "### h) **LO QUE QUEDA DEL TRAMO AL CIERRE DE ESTE LOTE, MEDIDO Y NO ARRASTRADO**"),
    "PAG_ACTO34": (PAGINA, "### c) **EL `ACTO 34`: EL CICLO DE CULPA, DOS RAZONES QUE CORONAN SUPERVIVIENTES DISTINTOS"),
    "PAG_ACTO34_CABLE": (PAGINA, "ACUERDO`: pasos (5 contra 4 y 4) y condiciones (3 contra 2 y 2) apuntan al mismo nodo."),
    "PAG_ACTO36": (PAGINA, "### e) **EL `ACTO 36`: EL PLAN DE CONTROL DE JURAN, EL ACTO MEJOR DECLARADO DEL LOTE"),
    "PAG_ACTO36_FORMA": (PAGINA, "**La forma es `CHOCAN`** (pasos al superviviente, condiciones a"),
    "PAG_COLISION_F": (PAGINA, "### g) **LA COLISION DE CLASE QUE ESTA VUELTA FABRICA, PREDICHA ANTES DE TOCAR UN NODO"),
    "PAG_PENDIENTES": (PAGINA, "### h) **LOS PENDIENTES HEREDADOS, NOMBRADOS CON SU DESTINO**"),
    "PAG_LINEA_BASE": (PAGINA, "### c) **UNA COLISION QUE FABRICA UNA FUSION TIENE DE DUENA A QUIEN LA FABRICA"),
    "PAG_ACTO1_P10": (PAGINA, "### a) **EL ACTO 1: `DECLARADO Y NO FUNDIDO` POR `P.10`"),
    "PAG_CUARTO_MOTIVO": (PAGINA, "### d) **EL CUARTO MOTIVO SELLADO DEL `DECLARADO Y NO FUNDIDO`"),
    "PAG_GUARDA_1B": (PAGINA, "### c) **UN ACTO CON DOS O MAS PUERTAS CIERRA `DECLARADO Y NO FUNDIDO`"),
    "PAG_P5_MOTIVO": (PAGINA, "### b) **UN ACTO CUYO `P.5` CONTESTA QUE NO ES UNA FAMILIA CIERRA"),
    "PAG_TRANSITO": (PAGINA, "### e) **EL TRANSITO DEL ACTO CON FORMA `EMPATE SIN VARA`"),
}

# ANCLAS: hay agujas que NO son unicas en todo el fichero porque el acta repite
# cabeceras de seccion vuelta tras vuelta, y porque esta pagina repite la
# cabecera del cierre de tramo una vez por lote. Para esas, la busqueda se
# restringe a una VENTANA que arranca en otra clave ya derivada, y se sigue
# exigiendo UNA sola ocurrencia DENTRO de la ventana.
# CLAVE -> (clave ancla, ventana en lineas).
ANCLAS = dict(
    [(c, ("A70_ABRE", 500)) for c in AGUJAS if c.startswith("A70_") and c != "A70_ABRE"]
    + [("PAG_TRAMO_CIERRE_F", ("PAG_LOTE_F", 500))]
)

# NUMEROS QUE EL TEXTO ESCRIBE EN NEGRITA Y NO SON CITAS DE LINEA, declarados
# uno a uno con su motivo. Todo lo demas que aparezca en negrita con 3 a 5
# digitos tiene que salir de una aguja, o es ROJO.
NUMEROS_DECLARADOS = {
    "880": "el puesto de la ciega del acto 35, el A por contencion con residuo del ethos",
    "2233": "el primero de los dos puestos de la ciega del acto 34",
    "2272": "el segundo de los dos puestos de la ciega del acto 34",
    "2562": "el primero de los dos puestos de la ciega del acto 36",
    "2639": "el segundo de los dos puestos de la ciega del acto 36, el del residuo capacitar y auditar",
    "279": "el puesto de la ciega de la colision que el lote F fabrico",
    "475": "el acumulado de relecturas del auditor al cierre de la vuelta 70",
    "805": "el acumulado de puestos leidos del auditor al cierre de la vuelta 70",
}

# (CLAVE, aguja que esa linea NO debe contener). La afirmacion negativa se MIDE,
# no se cree. Ver el docstring: las tres son de sustancia, no de adorno.
NEGATIVAS = [
    ("A70_CAIDA_CRUDAS", "6 contra 4"),
    ("A70_ADJ1", "aritmetica"),
    ("A70_ADJ4_54", "44"),
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
from _v71_texto_acta70 import TEXTO  # noqa: E402

MARCA_IDEMPOTENCIA = "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 70"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 70 AL FINAL DE 03_FUSIONES.md")
    print("Con la guarda de citas copiada entera del ancestro (cuatro mecanismos, cero nuevos).")
    print("=" * 78)

    # LA IDEMPOTENCIA SE MIRA PRIMERO, y no despues de derivar: es la correccion
    # que la vuelta 68 declaro en su averia 7.2. Rojo tambien es seguro (no
    # escribe), pero la respuesta correcta a una pagina ya registrada es decirlo,
    # no fallar.
    crudo = io.open(PAGINA, encoding="utf-8").read()
    if MARCA_IDEMPOTENCIA in crudo:
        print()
        print("YA ADOSADA: la seccion del acta 70 ya esta en la pagina. No se escribe nada.")
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
