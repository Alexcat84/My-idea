# -*- coding: utf-8 -*-
"""vuelta73_registrar_acta72.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DE LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 72.

NO REESCRIBE NI UNA LINEA DE LAS SECCIONES DE ARRIBA: abre el fichero en modo
adosar y escribe detras. Es la via que esta pagina ya uso TRECE veces, la ultima
de ellas la del acta 71. Los numeros de linea de esas sedes NO se teclean aqui:
los que este instrumento ESCRIBE salen todos de una aguja.

LA MAQUINA SE COPIA, NO SE IMPORTA, y va dicho porque el acta 68 escribio la
regla en su D14 y las actas 69 a 72 la dejaron en pie: importar vale DENTRO DE
LA MISMA VUELTA (dos instrumentos que nacen juntos y no pueden divergir), y el
carril de COPIAR es el que protege a los registradores de VUELTAS DISTINTAS.
Este es de otra vuelta que scripts/loop/vuelta72_registrar_acta71.py, asi que se
copia entero. Y NO SE COPIA A MANO, QUE ES RETECLEAR: lo copia
scripts/loop/_v73_construir_registrador_acta.py POR EXTRACCION, con un assert por
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

UN SOLO FICHERO DE AGUJA QUE NO ES NI LA PAGINA NI EL ACTA, y no es maquina
nueva: esta vuelta aplica UNA correccion declarada y cita su SEDE por aguja en
vez de teclearla. AGUJAS siempre fue un mapa CLAVE -> (fichero, aguja) y el
fichero es un dato: se anade CUENTA como constante de ruta, y nada mas. La
vuelta 72 anadio TRES por el mismo carril y el D11 de su acta lo adjudico A
FAVOR.

LAS TRES NEGATIVAS DE ESTA VUELTA, y las tres son de sustancia:
  a) el apartado sobre la adjudicacion 1 parte en DOS citas lo que el acta 72
     dice de la especie del pendiente 4: la linea del HECHO (que la sustancia
     llega entera sea cual sea el vehiculo) y la linea que ordena NO RE-SELLAR el
     plan del lote H. Son dos decisiones distintas y la tabla las cita por
     separado; si la linea del hecho ya hablara del re-sellado, la tabla estaria
     citando dos veces la misma cosa como si fueran dos: se MIDE que la linea del
     hecho NO contiene la palabra re-sella;
  b) la racha de reporte se apoya en que esta es la SEGUNDA tanda limpia seguida,
     y esa frase vive en la linea de las RACHAS y no en la de las caidas de la
     tanda, que es la que cuenta los ceros de ESTA vuelta sola: se MIDE que la
     linea de las caidas NO contiene la palabra seguida;
  c) el apartado del acto 44 manda a lineas distintas la CABECERA de la
     adjudicacion 3 (que lo nombra aparte en el paquete del cierre) y la frase
     que dice por que los CATORCE esperan por otra cosa. La segunda es la que
     funda la especie propia, y por eso no puede estar en la primera: se MIDE que
     la linea de la cabecera NO contiene P.10.

LA IDEMPOTENCIA SE MIRA PRIMERO: si la seccion ya esta en la pagina, no se
escribe nada. Una pagina con la adjudicacion duplicada no falla, dice que si.

Uso:
  python scripts/loop/vuelta73_registrar_acta72.py [--simular]
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:72 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 72 DEL AUDITOR" corte=2026-08-26 motivo="el titulo nombra el ACTA que este registro transcribe, que es de la vuelta 72; el fichero es de la vuelta 73 y por eso el numero no calza con su propia vuelta a proposito"
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
# nombra. Vive aqui, en el bloque propio, junto a las agujas que la usan.
CUENTA = os.path.join(RAIZ, "scripts", "loop", "cuenta_agregada_de_perdidas.py")

# CLAVE -> (fichero, aguja). La aguja es el CONTENIDO que la cita afirma; el
# numero de linea sale de buscarla, nunca de teclearla.
AGUJAS = {
    # --- docs/loop/ACTA_AUDITOR.md, acta de la vuelta 72: las cabeceras ---
    "A72_ABRE": (ACTA, "# ACTA DE LA VUELTA 72 DEL AUDITOR (26 ago 2026, Fable 5)"),
    "A72_VERIF": (ACTA, "## 1. VERIFICACION POR CORRIDA PROPIA: TODO CALZA AL DIGITO"),
    "A72_CIEGA": (ACTA, "## 2. RELECTURA CIEGA: 5 DE 5 ACTOS COINCIDENTES, TODO DENTRO DEL"),
    "A72_LIMPIA": (ACTA, "## 3. LA TANDA 72 DEL EJECUTOR: LIMPIA ENTERA"),
    "A72_TRECE": (ACTA, "## 4. LOS TRECE DISCUTIBLES, ADJUDICADOS: TODOS A FAVOR"),
    "A72_ADJUD": (ACTA, "## 5. ADJUDICACIONES NUEVAS DE ESTA ACTA"),
    "A72_AVERIAS": (ACTA, "## 6. AVERIAS: CINCO DEL EJECUTOR YA DECLARADAS, Y LAS MIAS CON NOMBRE"),
    "A72_METRICA": (ACTA, "## 7. METRICA DE CREDITO ACUMULADA"),
    "A72_PARADAS": (ACTA, "## 8. CONDICIONES DE PARADA, RECORRIDAS: NINGUNA SE CUMPLE HOY"),
    # la verificacion por corrida propia, pieza a pieza
    "A72_V_CABECERA": (ACTA, "- CABECERA: tallar_cabecera_reporte.py --vuelta 72 --comparar corrido"),
    "A72_V_MARCADOR": (ACTA, "- MARCADOR, POR MI PROPIO CONTEO sobre el archivo: n 3388, cero huecos,"),
    "A72_V_RECOMPUTO": (ACTA, "- RECOMPUTO AL CIERRE, corrido por mi (recomputo_3388.py): grafo 3853"),
    "A72_V_COLA": (ACTA, "- LA COLA DE COSTURAS, DELTA POR MI PROPIO DIFF con la apertura por"),
    "A72_V_ESPERADAS": (ACTA, "- ESPERADAS, RE-SIMULADAS PRE FUSION POR MI: worktree en c4c38956 con"),
    "A72_V_VARAS": (ACTA, "- VARAS Y PUENTES PRE FUSION, EN EL MISMO WORKTREE: formas al byte"),
    "A72_V_GUARDAD": (ACTA, "- GUARDA D Y SUPERVIVIENTES: los 8 absorbidos deprecados con su texto"),
    "A72_V_ACTO44": (ACTA, "- EL ACTO 44, INTACTO: sus tres nodos vivos e IDENTICOS byte a byte"),
    "A72_V_DUPLICADAS": (ACTA, "- DUPLICADAS: instrumento corrido por mi con la apertura por git show:"),
    "A72_V_CUENTA": (ACTA, "- LA CUENTA AGREGADA, RE-CORRIDA POR MI: 12 filas (5 DE PARAMETRO y 7"),
    "A72_V_ATENUANTE": (ACTA, "  del atenuante del 43 leida entera por mi: la pieza del burn rate"),
    "A72_V_TRAMO": (ACTA, "- TRAMO AL CIERRE, RECONTADO POR MI: 47 filas, 26 FUNDIDOS medidos"),
    "A72_V_GATE0": (ACTA, "- GATE 0 CON SU CICLO DE TRES, CORRIDA MIA: run_phase1 con"),
    "A72_V_BARRIDO": (ACTA, "- BARRIDO: 479 ficheros, ROJO 32 (linea base en su sitio), AMBAR 0,"),
    "A72_V_CODIF": (ACTA, "- CODIFICACION: los 55 ficheros V72 de docs/loop (49 txt, 4 jsonl, 2"),
    # las TRES observaciones de lectura sin cargo
    "A72_OBS": (ACTA, "TRES OBSERVACIONES DE LECTURA, SIN CARGO, dichas para que no parezcan"),
    "A72_OBS_A": (ACTA, "tragadas: (a) la celda del censo de codificacion dice 54 ficheros y"),
    "A72_OBS_B": (ACTA, "verifique yo sobre los 55; (b) el --diff-filter=M sobre scripts/"),
    "A72_OBS_C": (ACTA, "SOLO instrumento modificado es correcta filtrada a instrumentos; (c)"),
    "A72_OBS_C_ARISTA": (ACTA, "sentidos: lo medido por mi es UNA arista dirigida vista de sus dos"),
    # la ciega, acto a acto
    "A72_CIEGA_43": (ACTA, "- 43: UNA familia (el freno al gasto antes de validar el modelo,"),
    "A72_CIEGA_44": (ACTA, "- 44: UNA familia (las tecnologias disruptivas, Cooper); mi ciega de"),
    "A72_CIEGA_44_PUERTAS": (ACTA, "  PUERTAS: mi ciega confirma la trampa que el reporte declara, y que"),
    "A72_CIEGA_45": (ACTA, "- 45: UNA familia (la reconstruccion del contexto sin sesgo"),
    "A72_CIEGA_46": (ACTA, "- 46: UNA familia (el riesgo ambiental de la cadena extendida, Esty);"),
    "A72_CIEGA_47": (ACTA, "- 47: UNA familia (la terminacion del franquiciado, Siebert); ciego"),
    "A72_CIEGA_CERO": (ACTA, "CERO discrepancias en la ciega. Las coronas cruzadas del 45 (el 2244"),
    # la tanda limpia
    "A72_LIMPIA_CERO": (ACTA, "CERO caidas de clase, CERO de cifra publicada, CERO de reporte: toda"),
    "A72_LIMPIA_MANEJOS": (ACTA, "reporte (la celda que mentia y la fila del pendiente 4) son manejos"),
    # los trece discutibles
    "A72_D1": (ACTA, "1. D1 (la clausula de OP-L-03 no es identica al byte y la correccion"),
    "A72_D2": (ACTA, "2. D2 (el 43 funde contra un cableado de 11 a 7): A FAVOR por la"),
    "A72_D3": (ACTA, "3. D3 (el 43 crece de 5 a 8 pasos): A FAVOR como medida. Los tres"),
    "A72_D4": (ACTA, "4. D4 (el 46 funde con la puerta sobreviviendo contra la unica vara"),
    "A72_D5": (ACTA, "5. D5 (OP-S-09 queda con un alias fuera de su familia): A FAVOR. La"),
    "A72_D6": (ACTA, "6. D6 (las dos razones del 45 coronan distinto y los coronados tienen"),
    "A72_D7": (ACTA, "7. D7 (el 47 funde a favor del peor cableado): A FAVOR por la letra:"),
    "A72_D8": (ACTA, "8. D8 (la fila del pendiente 4 en sustancia con vehiculo INCISO): A"),
    "A72_D9": (ACTA, "9. D9 (la celda corregida de una tabla congelada): A FAVOR, adjudicado"),
    "A72_D10": (ACTA, "10. D10 (el 44 es especie nueva entre los declarados): A FAVOR como"),
    "A72_D11": (ACTA, "11. D11 (tres ficheros de aguja nuevos): A FAVOR. AGUJAS siempre fue"),
    "A72_D12": (ACTA, "12. D12 (cinco INCISO, dos al mismo acto): A FAVOR. Los cinco trozos"),
    "A72_D13": (ACTA, "13. D13 (el 45 cierra sin una sola perdida de paso): A FAVOR. CERO"),
    # las tres adjudicaciones
    "A72_ADJ1": (ACTA, "1. LA ESPECIE DEL PENDIENTE 4 LA DEFINE EL HECHO, NO EL VEHICULO"),
    "A72_ADJ1_HECHO": (ACTA, "   si la pieza viajo por APPEND o por INCISO. Extension citable: el"),
    "A72_ADJ1_ENCARGO": (ACTA, "   cuenta_agregada_de_perdidas.py va encargada en TAREA 1 (docstring:"),
    "A72_ADJ1_NORESELLA": (ACTA, "   busqueda y la aritmetica NO se tocan). El plan del lote H NO se"),
    "A72_ADJ2": (ACTA, "2. LA CELDA COPIADA QUE MIENTE SE CORRIGE POR EL CARRIL DEL ACTA 61,"),
    "A72_ADJ2_CONGELO": (ACTA, "   congelo las tablas contra el CRECIMIENTO y la edicion sin declarar,"),
    "A72_ADJ3": (ACTA, "3. EL ACTO 44 ENTRA NOMBRADO APARTE EN EL PAQUETE DEL CIERRE DE LA"),
    "A72_ADJ3_CATORCE": (ACTA, "   FASE 03 (pregunta 4, del D10): los catorce esperan por P.10 o por"),
    "A72_ADJ3_SEDE": (ACTA, "   CIERRE DE LA FASE 03 es parada de fundador (AUDITOR.md seccion 4,"),
    # las averias
    "A72_AVERIAS_EJEC": (ACTA, "Del ejecutor: las cinco de su seccion 7, ninguna llego a cifra"),
    "A72_AVERIAS_AUD": (ACTA, "Del auditor, con nombre y sin cifra publicada de por medio:"),
    # la metrica y las rachas
    "A72_METRICA_CAIDAS": (ACTA, "Caidas del ejecutor en esta tanda (vuelta 72): CERO de clase, CERO de"),
    "A72_METRICA_ACUM": (ACTA, "Acumulado: 485 relecturas (480 mas las cinco ciegas), 835 puestos (820"),
    "A72_RACHAS": (ACTA, "Rachas: CLASE O CIFRA PUBLICADA en CERO tandas (la 72 vino limpia)."),
    "A72_RACHAS_REPORTE": (ACTA, "REPORTE en CERO tandas (segunda tanda limpia seguida)."),
    # las condiciones de parada
    "A72_CIERRE03": (ACTA, "- CIERRE DE LA FASE 03 (la parada del fundador): NO SE CUMPLE TODAVIA."),
    "A72_CIERRE03_QUEDAN": (ACTA, "  Quedan 6 actos sin destino (18 nodos), dos de ellos con dueno (31 y"),
    # --- docs/plan/03_FUSIONES.md, sedes de esta misma pagina ---
    "PAG_ACTA71": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 71, REGISTRADAS AQUI"),
    "PAG_ACTA70": (PAGINA, "## LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 70, REGISTRADAS AQUI"),
    # --- LA SEDE DE LA UNICA CORRECCION DECLARADA DE ESTA VUELTA ---
    "CUENTA_CORRECCION": (CUENTA, "CORRECCION DECLARADA (2026-08-26, vuelta 73, TAREA 1 del encargo; adjudicacion 1"),
    "CUENTA_HECHO": (CUENTA, "LA ESPECIE DEL PENDIENTE 4 LA DEFINE EL HECHO, NO EL VEHICULO. Una fila es de"),
    "CUENTA_NOTOCA": (CUENTA, "LO QUE ESTA CORRECCION NO TOCA, Y SE DICE PARA QUE SE PUEDA MEDIR: la BUSQUEDA y"),
}

# ANCLAS: hay agujas que NO son unicas en todo el fichero porque el acta repite
# cabeceras de seccion vuelta tras vuelta. Para esas, la busqueda se restringe a
# una VENTANA que arranca en otra clave ya derivada, y se sigue exigiendo UNA
# sola ocurrencia DENTRO de la ventana.
# CLAVE -> (clave ancla, ventana en lineas).
ANCLAS = dict(
    [(c, ("A72_ABRE", 500)) for c in AGUJAS if c.startswith("A72_") and c != "A72_ABRE"]
)

# NUMEROS QUE EL TEXTO ESCRIBE EN NEGRITA Y NO SON CITAS DE LINEA, declarados
# uno a uno con su motivo. Todo lo demas que aparezca en negrita con 3 a 5
# digitos tiene que salir de una aguja, o es ROJO.
NUMEROS_DECLARADOS = {}

# (CLAVE, aguja que esa linea NO debe contener). La afirmacion negativa se MIDE,
# no se cree. Ver el docstring: las tres son de sustancia, no de adorno.
NEGATIVAS = [
    ("A72_ADJ1_HECHO", "re-sella"),
    ("A72_METRICA_CAIDAS", "seguida"),
    ("A72_ADJ3", "P.10"),
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
from _v73_texto_acta72 import TEXTO  # noqa: E402

MARCA_IDEMPOTENCIA = "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 72"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("REGISTRO DE LAS ADJUDICACIONES DEL ACTA 72 AL FINAL DE 03_FUSIONES.md")
    print("Con la guarda de citas copiada entera del ancestro (cuatro mecanismos, cero nuevos).")
    print("=" * 78)

    # LA IDEMPOTENCIA SE MIRA PRIMERO, y no despues de derivar: es la correccion
    # que la vuelta 68 declaro en su averia 7.2. Rojo tambien es seguro (no
    # escribe), pero la respuesta correcta a una pagina ya registrada es decirlo,
    # no fallar.
    crudo = io.open(PAGINA, encoding="utf-8").read()
    if MARCA_IDEMPOTENCIA in crudo:
        print()
        print("YA ADOSADA: la seccion del acta 72 ya esta en la pagina. No se escribe nada.")
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
