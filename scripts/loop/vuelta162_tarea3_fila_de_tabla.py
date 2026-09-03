# -*- coding: utf-8 -*-
r"""vuelta162_tarea3_fila_de_tabla.py . TAREA 3 de la vuelta 162.

Aplica sobre `scripts/loop/verificar_cifras_del_reporte.py` la ADJUDICACION 6.6
DEL ACTA 161: la guarda de cifras no puede perder cobertura en silencio.

Parche de una sola pasada, con anclas literales.

USO:  python scripts/loop/vuelta162_tarea3_fila_de_tabla.py
"""
import io

RUTA = "scripts/loop/verificar_cifras_del_reporte.py"

ANCLA_BLOQUE = """def comprobar_afirmaciones_de_cierre(frases, existentes):
"""

BLOQUE = r'''# --- ADJUDICACION 6.6 DEL ACTA 161 (3 sep 2026): LA GUARDA NO PUEDE PERDER
# COBERTURA EN SILENCIO, Y LA FILA DE TABLA TAMBIEN SE COTEJA ----------------
#
# REGISTRO POR ADICION. Nada de lo escrito arriba se borra.
#
# EL HECHO, MEDIDO Y REPRODUCIBLE (acta 161, seccion 5.2). Esta guarda salio
# VERDE con cobertura 1 de 1 sobre el reporte de la vuelta 161 declarando
# "afirmaciones de CIERRE cotejadas: 0", y sobre el de la vuelta 160
# (`git show aa6bb622:docs/loop/REPORTE.md`) declara 5. DE CINCO A CERO EN UNA
# VUELTA, y no porque nadie aflojara la guarda: porque las cifras de fase se
# mudaron DE LA PROSA A UNA TABLA, y el disparo de `es_afirmacion_de_cierre` pide
# un SUJETO mas un VERBO en prosa (`cierra`, `cierre`, `queda completa`). Una
# fila como `| fase 03: catalogo / cumplidas / sin cumplir | 16 / 12 / 4 | ... |`
# trae el sujeto y NO trae verbo. La guarda dejo de ver. Es el banco 9: verde y
# mal.
#
# LO QUE SE ADJUDICA, Y NO AFLOJA NADA NI PROHIBE LA TABLA:
#   (a) UNA FILA DE TABLA ES AFIRMACION DE CIERRE COTEJABLE cuando trae un SUJETO
#       de `SUJETOS_DE_CIERRE` COMO PALABRA ENTERA (`\bfase\b`, `\bcatalogo\b`, y
#       no dentro de otra, que `desfase` lleva `fase` dentro) Y CITA en la misma
#       fila una salida existente de `tallar_estado_de_fase.py`, reconocida POR
#       SU CONTENIDO. Esa cita es evidencia MAS FUERTE que el verbo de prosa: la
#       fila no dice "cierra", dice "esto es lo que ese instrumento mide".
#   (b) EL COTEJO ES NUMERICO Y CONTRA EL INSTRUMENTO: la fila tiene que traer,
#       EN ORDEN Y SEGUIDOS, los tres numeros que la linea `CIFRA:` de ese
#       fichero publica (catalogo, cumplido, sin cumplir). Si no los trae, ROJO
#       nombrando la fila, los numeros que si trae y los que el fichero dice.
#   (c) LO QUE NO SE PUEDA COTEJAR SE DICE, CON SU CIFRA, EN UN AVISO VISIBLE
#       (banco 9, fallar ruidoso): una fila que nombra un sujeto de cierre y trae
#       numeros pero NO cita salida de estado de fase NO se puede cotejar, y la
#       guarda publica CUANTAS son y CUALES. El AVISO no tumba la guarda: avisar
#       de lo que no se midio es lo contrario de fallar por ello.
#   (d) EL CAMINO DE PROSA NO SE TOCA. `es_afirmacion_de_cierre` y
#       `comprobar_afirmaciones_de_cierre` quedan exactamente igual, y por eso el
#       reporte de la vuelta 160 SIGUE DANDO 5.

PATRON_CIFRA_DE_FASE = re.compile(
    r"CIFRA:\s*operaciones del catalogo:\s*(\d+)\s*\|\s*con destino cumplido:\s*(\d+)"
    r"\s*\|\s*sin cumplir:\s*(\d+)")
PATRON_NUMERO_SUELTO = re.compile(r"\d+")


def leer_cifra_de_fase(contenido):
    """(catalogo, cumplido, sin_cumplir) de una salida de
    `tallar_estado_de_fase.py`, o None si no lo es. Se reconoce POR CONTENIDO,
    igual que `leer_estado_de_fase`."""
    if MARCA_ESTADO_DE_FASE not in contenido:
        return None
    m = PATRON_CIFRA_DE_FASE.search(contenido)
    if m is None:
        return None
    return tuple(int(x) for x in m.groups())


def _sujeto_como_palabra(linea):
    """El SUJETO de cierre presente COMO PALABRA ENTERA, o None. `desfase` NO
    cuenta, y esa es justo la fila de la cabecera que si no reventaria el aviso
    con un falso positivo."""
    plana = _sin_tildes(linea).lower()
    for s in SUJETOS_DE_CIERRE:
        if re.search(r"\b%s\b" % re.escape(s), plana):
            return s
    return None


def _subsecuencia_seguida(numeros, tripla):
    """True si `tripla` aparece EN ORDEN Y SEGUIDA dentro de `numeros`."""
    n, k = len(numeros), len(tripla)
    return any(tuple(numeros[i:i + k]) == tuple(tripla) for i in range(n - k + 1))


def comprobar_filas_de_tabla_de_cierre(texto, existentes):
    """ADJUDICACION 6.6 DEL ACTA 161. Devuelve (fallos, cotejadas, avisos).

      - `cotejadas`: [(linea, sujeto, fichero, tripla, numeros_de_la_fila)]
      - `avisos`: [(linea, sujeto, numeros, texto_de_la_fila)] para las filas que
        NOMBRAN un sujeto de cierre y TRAEN numeros pero no citan salida de
        estado de fase. NO son fallo: son lo que la guarda declara que no midio.
    """
    fallos, cotejadas, avisos = [], [], []
    for i, linea in enumerate(texto.split("\n"), 1):
        if not linea.strip().startswith("|"):
            continue
        sujeto = _sujeto_como_palabra(linea)
        if sujeto is None:
            continue
        numeros = [int(x) for x in PATRON_NUMERO_SUELTO.findall(linea.replace(".", ""))]
        if not numeros:
            continue
        triplas = []
        for c in dict.fromkeys(PATRON_CITA_SALIDA.findall(linea)):
            if c not in existentes:
                continue
            t = leer_cifra_de_fase(leer(os.path.join(LOOP, c)))
            if t is not None:
                triplas.append((c, t))
        if not triplas:
            avisos.append((i, sujeto, numeros, linea.strip()))
            continue
        for fichero, tripla in triplas:
            if _subsecuencia_seguida(numeros, tripla):
                cotejadas.append((i, sujeto, fichero, tripla, numeros))
            else:
                fallos.append(
                    "linea %d: FILA DE TABLA con sujeto de cierre '%s' que cita `%s`, y sus "
                    "numeros NO traen seguida la tripla que ese fichero publica. El fichero "
                    "dice catalogo %d, cumplido %d, sin cumplir %d; la fila trae %s. Fila: %r"
                    % (i, sujeto, fichero, tripla[0], tripla[1], tripla[2],
                       numeros, linea.strip()))
    return fallos, cotejadas, avisos


def comprobar_afirmaciones_de_cierre(frases, existentes):
'''

ANCLA_FIRMA = """def verificar(ruta_reporte, cierres_out=None, nomina_out=None):
"""

NUEVA_FIRMA = """def verificar(ruta_reporte, cierres_out=None, nomina_out=None,
              filas_out=None, avisos_out=None):
"""

ANCLA_LLAMADA = """    fallos_cierre, cierres_cotejados = comprobar_afirmaciones_de_cierre(frases, existentes)
    fallos.extend(fallos_cierre)
    if cierres_out is not None:
        cierres_out.extend(cierres_cotejados)
"""

NUEVA_LLAMADA = """    fallos_cierre, cierres_cotejados = comprobar_afirmaciones_de_cierre(frases, existentes)
    fallos.extend(fallos_cierre)
    if cierres_out is not None:
        cierres_out.extend(cierres_cotejados)

    # ADJUDICACION 6.6 DEL ACTA 161: LAS FILAS DE TABLA, ADEMAS DE LA PROSA. Se
    # corre sobre el MISMO `texto` (ya sin los bloques cubiertos), para que la
    # cabecera tallada quede fuera aqui igual que queda fuera de todo lo demas.
    # LA ARIDAD NO SE TOCA: los dos resultados salen por parametros de salida,
    # por la misma razon que `cierres_out` en la vuelta 140.
    fallos_filas, filas_cotejadas, avisos_filas = comprobar_filas_de_tabla_de_cierre(
        texto, existentes)
    fallos.extend(fallos_filas)
    if filas_out is not None:
        filas_out.extend(filas_cotejadas)
    if avisos_out is not None:
        avisos_out.extend(avisos_filas)
"""

ANCLA_MAIN = """    cierres = []
    nomina = {}
    fallos, cotejados, exentas, total_cifras = verificar(
        a.reporte, cierres_out=cierres, nomina_out=nomina)
"""

NUEVA_MAIN = """    cierres = []
    nomina = {}
    filas_cierre = []
    avisos_filas = []
    fallos, cotejados, exentas, total_cifras = verificar(
        a.reporte, cierres_out=cierres, nomina_out=nomina,
        filas_out=filas_cierre, avisos_out=avisos_filas)
"""

ANCLA_COBERTURA = '''    cobertura += (" | afirmaciones de CIERRE cotejadas contra tallar_estado_de_fase.py: %d"
                  % len(cierres))
'''

NUEVA_COBERTURA = '''    cobertura += (" | afirmaciones de CIERRE cotejadas contra tallar_estado_de_fase.py: %d"
                  % len(cierres))
    # ADJUDICACION 6.6 DEL ACTA 161: la cobertura dice tambien cuantas FILAS DE
    # TABLA de cierre se cotejaron y cuantas quedaron SIN COTEJAR, siempre, verde
    # o rojo. Una cobertura que no dice lo que no midio es la que se quedo ciega.
    cobertura += (" | filas de TABLA de cierre cotejadas: %d | filas de TABLA de cierre "
                  "SIN COTEJAR (aviso): %d" % (len(filas_cierre), len(avisos_filas)))
'''

ANCLA_AVISO_ROJO = '''    if fallos:
        print("ROJO, %d cifra(s) no cuadran:" % len(fallos))
'''

NUEVO_AVISO_ROJO = '''    def _imprimir_filas_y_avisos():
        """ADJUDICACION 6.6 DEL ACTA 161. SE IMPRIME SIEMPRE, verde o rojo: las
        filas de tabla cotejadas con lo que su fichero dice, y el AVISO VISIBLE
        con las que no se pudieron cotejar Y SU CIFRA."""
        if filas_cierre:
            print("FILA(S) DE TABLA de cierre cotejadas contra tallar_estado_de_fase.py "
                  "(%d), cada una con LO QUE SU FICHERO DICE (computado, no tecleado):"
                  % len(filas_cierre))
            for i, sujeto, fichero, tripla, numeros in filas_cierre:
                print("  linea %d (sujeto '%s') <-> `%s`: catalogo %d, cumplido %d, sin "
                      "cumplir %d; la fila los trae seguidos entre %s"
                      % (i, sujeto, fichero, tripla[0], tripla[1], tripla[2], numeros))
        if avisos_filas:
            print("AVISO, Y VA EN VOZ ALTA (banco 9, adjudicacion 6.6 del acta 161): %d "
                  "fila(s) de tabla NOMBRAN un sujeto de cierre y TRAEN cifras, y esta "
                  "guarda NO LAS PUDO COTEJAR porque no citan ninguna salida de "
                  "tallar_estado_de_fase.py. Van con su cifra:" % len(avisos_filas))
            for i, sujeto, numeros, fila in avisos_filas:
                print("  linea %d (sujeto '%s') cifras %s: %r" % (i, sujeto, numeros, fila))
        else:
            print("AVISO: 0 fila(s) de tabla de cierre quedaron sin cotejar.")

    if fallos:
        print("ROJO, %d cifra(s) no cuadran:" % len(fallos))
'''

ANCLA_ROJO_COBERTURA = """        if exentas:
            print("cifra(s) exentas por (sin instrumento) (%d):" % len(exentas))
            for numero, unidad, frase in exentas:
                print("  %d %s: %r" % (numero, unidad, frase))
        print(cobertura)
        return 1
"""

NUEVO_ROJO_COBERTURA = """        if exentas:
            print("cifra(s) exentas por (sin instrumento) (%d):" % len(exentas))
            for numero, unidad, frase in exentas:
                print("  %d %s: %r" % (numero, unidad, frase))
        _imprimir_filas_y_avisos()
        print(cobertura)
        return 1
"""

ANCLA_VERDE_COBERTURA = """        for i, sujeto, verbo, fichero, estado in cierres:
            print("  linea %d (sujeto '%s', verbo '%s') <-> `%s`: %s"
                  % (i, sujeto, verbo, fichero, estado))
    print(cobertura)
    return 0
"""

NUEVO_VERDE_COBERTURA = """        for i, sujeto, verbo, fichero, estado in cierres:
            print("  linea %d (sujeto '%s', verbo '%s') <-> `%s`: %s"
                  % (i, sujeto, verbo, fichero, estado))
    _imprimir_filas_y_avisos()
    print(cobertura)
    return 0
"""

PARCHES = [
    ("bloque de filas de tabla", ANCLA_BLOQUE, BLOQUE),
    ("firma de verificar", ANCLA_FIRMA, NUEVA_FIRMA),
    ("llamada dentro de verificar", ANCLA_LLAMADA, NUEVA_LLAMADA),
    ("cabecera de main", ANCLA_MAIN, NUEVA_MAIN),
    ("linea de cobertura", ANCLA_COBERTURA, NUEVA_COBERTURA),
    ("impresora de filas y avisos", ANCLA_AVISO_ROJO, NUEVO_AVISO_ROJO),
    ("cola del rojo", ANCLA_ROJO_COBERTURA, NUEVO_ROJO_COBERTURA),
    ("cola del verde", ANCLA_VERDE_COBERTURA, NUEVO_VERDE_COBERTURA),
]


def main():
    s = io.open(RUTA, encoding="utf-8").read()
    for nombre, ancla, nuevo in PARCHES:
        n = s.count(ancla)
        if n != 1:
            raise SystemExit("ROJO: el ancla %r aparece %d veces (se esperaba 1)" % (nombre, n))
        s = s.replace(ancla, nuevo, 1)
        print("  aplicado: %s" % nombre)
    io.open(RUTA, "w", encoding="utf-8", newline="\n").write(s)
    print("VERDE: %d parches aplicados sobre %s" % (len(PARCHES), RUTA))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
