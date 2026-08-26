# -*- coding: utf-8 -*-
"""vuelta69_registrar_acta68.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DE LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 68.

NO REESCRIBE NI UNA LINEA DE LAS SECCIONES DE ARRIBA: abre el fichero en modo
adosar y escribe detras. Es la via que esta pagina ya uso NUEVE veces (acta 52
en la linea 1250, acta 57 sobre el acto 25 en la 2475, acta 61 en la 2689, acta
62 en la 2933, acta 63 en la 3307, acta 64 en la 3613, acta 65 en la 3962, acta
66 en la 4478 y acta 67 en la 5031). Esos nueve numeros son del ancestro y se
citan como historia; los que este instrumento ESCRIBE salen todos de una aguja.

LA MAQUINA SE COPIA, NO SE IMPORTA, y va dicho porque el acta 68 escribio la
regla en su D14: importar la guarda vale DENTRO DE LA MISMA VUELTA (dos
instrumentos que nacen juntos y no pueden divergir), y el carril de COPIAR es el
que protege a los registradores de VUELTAS DISTINTAS. Este es de otra vuelta que
scripts/loop/vuelta68_registrar_acta67.py, asi que se copia entero: derivar,
negativas, sustituir y cotejar_texto salen de ahi LITERALES, y lo unico propio
son las AGUJAS, las ANCLAS, las NEGATIVAS y el texto importado.

LA GUARDA DE CITAS, HEREDADA ENTERA DE LA VUELTA 68 (que la ensancho por la
caida de cifra publicada de la 67), con sus cuatro mecanismos:

  1. LAS CITAS DE LINEA DEL TEXTO SE DERIVAN POR AGUJA, NO SE TECLEAN. El texto
     no lleva ningun numero de linea escrito a mano: lleva marcas [[CLAVE]], y
     cada CLAVE es un par (fichero, aguja). El instrumento BUSCA la aguja en el
     fichero, exige que aparezca EXACTAMENTE UNA VEZ (en el fichero o en una
     ventana anclada) y sustituye la marca por el numero que la busqueda
     devuelve.
  2. TODA CITA DE LA FORMA linea NNNN PRESENTE EN EL TEXTO NUEVO SE COTEJA
     CONTRA EL CONTENIDO DE ESA LINEA ANTES DE ESCRIBIR, y toda CLAVE derivada
     se usa al menos una vez para que la lista no crie citas muertas.
  3. LA RED ANCHA: todo numero de 3 a 5 digitos en NEGRITA tiene que salir de
     una aguja o estar declarado uno a uno con su motivo en NUMEROS_DECLARADOS.
     Es la red que caza la celda de tabla que no lleva la palabra linea delante,
     que es exactamente donde cayo la vuelta 67.
  4. LAS AGUJAS NEGATIVAS: pares (CLAVE, aguja que esa linea NO debe contener).
     Sirven para MEDIR una afirmacion negativa en vez de creerla.

LAS DOS NEGATIVAS DE ESTA VUELTA, y no son de adorno: esta seccion parte en DOS
citas lo que el acta 68 dice en un solo parrafo (el CUATRO que el reporte dijo y
el SEIS que el auditor midio), asi que se MIDE que la linea del CUATRO no
contiene la palabra SEIS; y se MIDE que la linea que adjudica el superviviente
del acto 18 no nombra a ningun otro miembro del acto, que es lo que convierte
una adjudicacion en una adjudicacion y no en una lista.

ESTA VUELTA NO LLEVA BLOQUE VERBATIM ni correccion declarada de cita: la maquina
de [[VERBATIM:CLAVE:N]] se copia igual (el carril de copiar no recorta), y si no
se usa, no se usa. La idempotencia se sigue mirando PRIMERO, que es la
correccion que la vuelta 68 declaro en su averia 7.2.

LA GUARDA DE IDEMPOTENCIA: si la seccion ya esta en la pagina, no se escribe
nada. Una pagina con la adjudicacion duplicada no falla, dice que si.

Uso:
  python scripts/loop/vuelta69_registrar_acta68.py [--simular]
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:68 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 68 DEL AUDITOR" corte=2026-08-26 motivo="el titulo nombra el ACTA que este registro transcribe, que es de la vuelta 68; el fichero es de la vuelta 69 y por eso el numero no calza con su propia vuelta a proposito"
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
    # --- docs/loop/ACTA_AUDITOR.md, acta de la vuelta 68 ---
    "A68_ABRE": (ACTA, "# ACTA DE LA VUELTA 68 DEL AUDITOR (26 ago 2026, Fable 5)"),
    "A68_VERIF": (ACTA, "## 1. VERIFICACION POR CORRIDA PROPIA: TODO AL DIGITO SALVO UNA CUENTA"),
    "A68_CIEGA": (ACTA, "## 2. RELECTURA CIEGA"),
    "A68_CAIDAS": (ACTA, "## 3. CAIDAS DE ESTA TANDA: UNA DE REPORTE DEL EJECUTOR (UNA CUENTA DEL"),
    "A68_CAIDA_MEDICION": (ACTA, "- LA CAIDA, CON SU MEDICION: el D9 del reporte dice CUATRO PERDIDAS CON"),
    "A68_CAIDA_SEIS": (ACTA, "  registro, fila a fila: SEIS filas llevan ATENUANTE DECLARADO en su"),
    "A68_CAIDA_FILAS": (ACTA, "  campo que (las filas 3, 4, 7, 8, 9 y 10). La otra mitad de la frase"),
    "A68_CAIDA_DOS": (ACTA, "  del D9 es exacta (DOS de la especie del pendiente 4, las filas 8 y"),
    "A68_CAIDA_LECTURA": (ACTA, "  10). Hay una lectura con la que el cuatro se entiende (excluir la"),
    "A68_ESPECIE": (ACTA, "- LA ESPECIE: la cuenta vive SOLO en REPORTE.md. El registro de"),
    "A68_RELECTURA_DOBLE": (ACTA, "- LA RELECTURA AL DOBLE, EJECUTADA: el tramo es la tabla de perdidas y"),
    "A68_EFECTO_CREDITO": (ACTA, "- EFECTO EN EL CREDITO: la racha de reporte en cero se rompe en la"),
    "A68_PERDIDAS_FILA": (ACTA, "- LAS PERDIDAS DEL PLAN, CONTADAS FILA A FILA (las 11 leidas enteras,"),
    "A68_DIECISEIS": (ACTA, "## 4. ADJUDICACION DE LOS DIECISEIS DISCUTIBLES: TODOS A FAVOR, CON LA"),
    "A68_D1": (ACTA, "1. D1, el ensanche de la guarda de citas con cuatro mecanismos donde el"),
    "A68_D2": (ACTA, "2. D2, fundir el acto 22 con el racimo del inventario en estado en"),
    "A68_D3": (ACTA, "3. D3, el superviviente del acto 22 contra el cableado 7 a 3: A FAVOR."),
    "A68_D4": (ACTA, "4. D4, el nodo de nueve pasos: A FAVOR por el carril del D8 del acta 67"),
    "A68_D5": (ACTA, "5. D5, tres APPEND de condicion en el acto 19 (2 a 5): A FAVOR. La vara"),
    "A68_D6": (ACTA, "6. D6, el acto 18 en transito sin superviviente elegido: A FAVOR. Es"),
    "A68_D7": (ACTA, "7. D7, declarar el lote en seis: A FAVOR. El encargo manda declarar al"),
    "A68_D8": (ACTA, "8. D8, dos perdidas con dos sedes en una fila: A FAVOR, es la"),
    "A68_D9": (ACTA, "9. D9, sobre-sellar perdidas con atenuante declarado: LA PRACTICA A"),
    "A68_D10": (ACTA, "10. D10, sellar la perdida que el INCISO del mismo acto repara: A"),
    "A68_D11": (ACTA, "11. D11, un CUBIERTO que apunta al superviviente cuando el contenido"),
    "A68_D12": (ACTA, "12. D12, los dos INCISO con nexo de coma sobre pasos que no terminan en"),
    "A68_D13": (ACTA, "13. D13, la fila de duenos en tabla_declarado sin encargo: A FAVOR con"),
    "A68_D14": (ACTA, "14. D14, importar la guarda en vez de copiarla: A FAVOR con la regla"),
    "A68_D15": (ACTA, "15. D15, el plan sellado dos veces: A FAVOR. El diff de sellos esta"),
    "A68_D16": (ACTA, "16. D16, leer entero y declarar el acto con dueno en vez de saltarlo: A"),
    "A68_ADJUD": (ACTA, "## 5. LAS ADJUDICACIONES NUEVAS Y LOS PENDIENTES"),
    "A68_SUP18": (ACTA, "1. EL SUPERVIVIENTE DEL ACTO 18, ADJUDICADO (el carril del transito,"),
    "A68_SUP18_ES": (ACTA, "   razones leidas por mi): EL SUPERVIVIENTE ES alianzas_cross_industry."),
    "A68_SUP18_PRIMERA": (ACTA, "   PRIMERA, EL ALCANCE: es el unico de los cuatro que apunta al MERCADO"),
    "A68_SUP18_SEGUNDA": (ACTA, "   SEGUNDA, EL REPARTO CON MENOS PERDIDA: sus piezas ya alojan lo"),
    "A68_SUP18_TERCERA": (ACTA, "   TERCERA, LO BUSCABLE: trae los nombres propios (EICC, AIM-PROGRESS)"),
    "A68_SUP18_CUARTA": (ACTA, "   CUARTA, EL CABLEADO NO LO DESMIENTE: empata en cabeza (3 con"),
    "A68_SUP18_CONSERVAR": (ACTA, "   LO QUE EL PLAN DEL LOTE E TIENE QUE CONSERVAR O SELLAR, nombrado"),
    "A68_P5": (ACTA, "2. LA PREGUNTA 5 DEL REPORTE (un racimo del inventario en estado en"),
    "A68_P5_CRITERIO": (ACTA, "   abrio su universo es el dueno MEDIDO: los dos campos duenos_* del"),
    "A68_P5_FRONTERA": (ACTA, "   entrada del inventario nombra una operacion en su campo"),
    "A68_P6": (ACTA, "3. LA PREGUNTA 6 (la fusion adjudicada del transito, cuenta para el"),
    "A68_P6_PLAN": (ACTA, "   acto 18 se ejecuta como PRIMERA operacion del lote E, dentro del"),
    "A68_PEND4": (ACTA, "4. EL SUBCONJUNTO CERRADO DE UN ACTO CON PUENTE (heredado): sigue"),
    "A68_PEND5": (ACTA, "5. LA MARCA PARA YA LO DICE EL APPEND DE UN HERMANO (heredado): sigue"),
    "A68_PEND6": (ACTA, "6. EL INCISO DE CONDICIONES (heredado): sigue en su carril, CUATRO"),
    "A68_PEND7": (ACTA, "7. EL ESQUEMA DE OPERACIONES.jsonl (heredado): sigue pendiente; esta"),
    "A68_METRICA": (ACTA, "## 6. METRICA DE CREDITO ACUMULADA"),
    "A68_ACUMULADO": (ACTA, "Acumulado: 464 relecturas (463 mas la ciega), 794 puestos (786 mas los"),
    "A68_RACHAS": (ACTA, "Rachas: CLASE O CIFRA EN CERO otra vez (la 68 quedo limpia y la racha"),
    "A68_PARADAS": (ACTA, "## 7. CONDICIONES DE PARADA, RECORRIDAS: NINGUNA SE CUMPLE"),
    "A68_CIERRE03": (ACTA, "- CIERRE DE LA FASE 03 (la parada de AUDITOR.md): NO SE CUMPLE TODAVIA."),
    # --- docs/plan/03_FUSIONES.md, sedes de esta misma pagina ---
    "PAG_ACTA67": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 67, REGISTRADAS AQUI"),
    "PAG_ACTA66": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 66, REGISTRADAS AQUI"),
    "PAG_TRANSITO": (PAGINA, "### e) **EL TRANSITO DEL ACTO CON FORMA `EMPATE SIN VARA`"),
    "PAG_ACTO18_TRANSITO": (PAGINA, "### d) **EL `ACTO 18`, `ABIERTO EN TRANSITO`: EL ESTRENO DEL CARRIL"),
    "PAG_ACTO22": (PAGINA, "### b) **EL `ACTO 22`: EL BLOQUE DE CUATRO DEL RACIMO DE LA SUPERVISION"),
    "PAG_LOTE_D": (PAGINA, "## `OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE D`"),
    "PAG_ACTO1_P10": (PAGINA, "### a) **EL ACTO 1: `DECLARADO Y NO FUNDIDO` POR `P.10`"),
    "PAG_GUARDA_1B": (PAGINA, "### c) **UN ACTO CON DOS O MAS PUERTAS CIERRA `DECLARADO Y NO FUNDIDO`"),
    "PAG_P5_MOTIVO": (PAGINA, "### b) **UN ACTO CUYO `P.5` CONTESTA QUE NO ES UNA FAMILIA CIERRA"),
    "PAG_CUARTO_MOTIVO": (PAGINA, "### d) **EL CUARTO MOTIVO SELLADO DEL `DECLARADO Y NO FUNDIDO`"),
    "PAG_LINEA_BASE": (PAGINA, "### c) **UNA COLISION QUE FABRICA UNA FUSION TIENE DE DUENA A QUIEN LA FABRICA"),
    "PAG_CARRIL_COLISIONES": (PAGINA, "### b) **EL CARRIL DE LAS DOS COLISIONES DE CLASE VIGENTES"),
}

# ANCLAS: hay agujas que NO son unicas en todo el fichero porque el acta repite
# cabeceras de seccion vuelta tras vuelta (RELECTURA CIEGA, METRICA DE CREDITO
# ACUMULADA, CONDICIONES DE PARADA). Para esas, la busqueda se restringe a una
# VENTANA que arranca en otra clave ya derivada, y se sigue exigiendo UNA sola
# ocurrencia DENTRO de la ventana.
# CLAVE -> (clave ancla, ventana en lineas).
ANCLAS = dict(
    [(c, ("A68_ABRE", 500)) for c in AGUJAS if c.startswith("A68_") and c != "A68_ABRE"]
)

# NUMEROS QUE EL TEXTO ESCRIBE EN NEGRITA Y NO SON CITAS DE LINEA, declarados
# uno a uno con su motivo. Todo lo demas que aparezca en negrita con 3 a 5
# digitos tiene que salir de una aguja, o es ROJO.
NUMEROS_DECLARADOS = {
    "1797": "el puesto de la primera razon del acto 18, la misma alianza entre competidores dos veces",
    "1871": "el puesto que ve la familia del acto 18 pasar de DOS a TRES por cierre transitivo",
    "1903": "el puesto que la ve pasar de TRES a CUATRO y trae los nombres propios de las coaliciones",
}

# (CLAVE, aguja que esa linea NO debe contener). La afirmacion negativa se MIDE,
# no se cree. Ver el docstring: las dos son de sustancia, no de adorno.
NEGATIVAS = [
    ("A68_CAIDA_MEDICION", "SEIS"),
    ("A68_SUP18_ES", "co_opetition_industria"),
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
from _v69_texto_acta68 import TEXTO  # noqa: E402

MARCA_IDEMPOTENCIA = "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 68"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 68 AL FINAL DE 03_FUSIONES.md")
    print("Con la guarda de citas heredada entera de la vuelta 68 (cuatro mecanismos).")
    print("=" * 78)

    # LA IDEMPOTENCIA SE MIRA PRIMERO, y no despues de derivar: es la correccion
    # que la vuelta 68 declaro en su averia 7.2. Rojo tambien es seguro (no
    # escribe), pero la respuesta correcta a una pagina ya registrada es decirlo,
    # no fallar.
    crudo = io.open(PAGINA, encoding="utf-8").read()
    if MARCA_IDEMPOTENCIA in crudo:
        print()
        print("YA ADOSADA: la seccion del acta 68 ya esta en la pagina. No se escribe nada.")
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
