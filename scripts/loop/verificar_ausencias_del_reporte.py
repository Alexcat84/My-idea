# -*- coding: utf-8 -*-
r"""verificar_ausencias_del_reporte.py . LA TERCERA ESCALADA (TAREA 2 de la
vuelta 146, encargada por `AUDITOR.md` 1.2 al llegar la racha de reporte a DOS
tandas seguidas, acta de la vuelta 145, seccion 5).

NOMBRE ESTABLE, SIN NUMERO DE VUELTA, como sus dos hermanas mayores
`tallar_cabecera_reporte.py` y `verificar_cifras_del_reporte.py`.

POR QUE NACE, Y POR QUE NO BASTABA CON LO QUE YA HABIA. La escalada del 26 ago
2026 (toda tabla y toda cifra del reporte contada de su fichero) esta
construida y corriendo: es `verificar_cifras_del_reporte.py`, y en la vuelta
145 salio verde con 8 de 8. NO CUBRE LA ESPECIE QUE FALLO EN LA 145, y el
motivo es mecanico: aquella guarda coteja CIFRAS contra el fichero que las
cuenta, y UNA AUSENCIA NO TIENE FICHERO QUE CONTAR. El reporte de la vuelta 145
publico, en su 3.c, "no existe en el repositorio ninguna lista canonica de
libros con sus alias de escritura" y de ahi saco `PRERREQUISITO CUMPLIDO: NO` y
el bloqueo de la fase 07. Existia: `docs/plan/OP_S_11_MAPEO_PROPUESTO.md`, y su
operacion duena `OP-S-11` esta HECHA desde el 29 ago. El metodo, escrito en la
propia salida de aquella vuelta: "candidatos mirados: <tres rutas>",
"hallados: NINGUNO". TRES RUTAS TECLEADAS A MANO, CERO BUSQUEDA POR CONTENIDO.

NO ES DOCTRINA NUEVA. `EJECUTOR.md` 9 dice desde hace vueltas "una busqueda
negativa no se puede citar", y el propio reporte de la 145 LA CITA en su
discutible 10 y LA INCUMPLE en la misma pagina. Es la caida 4.2 de la casa del
acta 145: una regla que se puede citar y romper a la vez es prosa, no guarda.
Esto es la guarda que la hace morder. Registrada como CORRECCION 23.

--- LA FRONTERA, PRIMERO, PORQUE ES LO QUE MAS FACIL SE LEE DE MAS ---

ESTA GUARDA NO DECIDE SI LA COSA EXISTE. Decide si LA AFIRMACION esta
RESPALDADA. Un reporte que diga "no existe X" con un barrido exhaustivo detras
pasa aunque X exista (entonces el barrido lo habria encontrado y el reporte
seria contradictorio a la vista de cualquiera, que es justo lo que la guarda
hermana de cifras dice de su propio caso analogo); y un reporte que diga "no
existe X" sin barrido cae aunque X de verdad no exista. LO QUE SE VIGILA ES EL
METODO, NO EL HECHO.

Y NO ENTRA EN NINGUNA COLUMNA DE `tallar_estado_de_fase.py`, por la misma razon
de unidades de la adjudicacion 3.9 del acta 144 y de la CORRECCION 18: aquella
tabla mide DESTINO CONTRA EL GRAFO, y esto mide RESPALDO DE UNA AFIRMACION. Dos
unidades no comparten columna.

--- EL VOCABULARIO DE DISPARO, CERRADO Y DECLARADO ---

Lo elige el ejecutor y se escribe aqui entero para que la proxima ampliacion
sea un acto declarado y no una adivinanza del instrumento (misma doctrina que
`VERBOS_DE_CIERRE` en la guarda de cifras). Dispara una frase que traiga
cualquiera de estas formas, sin distinguir mayusculas:

    no existe / no existen / no hay ningun / no hay ninguna
    hallados: NINGUNO / hallado: NINGUNO / no se hallo / no se halla
    no esta en el repositorio / NO INSTALADO / NO INSTALADOS
    PRERREQUISITO CUMPLIDO: NO

LA GUARDA DISPARA DE MAS A PROPOSITO, igual que su hermana: el coste de un
disparo de mas es UNA CITA de barrido, y el coste de un disparo de menos fue la
caida 4.1 del acta 145. **EL REMEDIO DE UN ROJO DE ESTA CLASE ES CORRER EL
BARRIDO, JAMAS REESCRIBIR LA PROSA HASTA QUE LA GUARDA NO ENCUENTRE NADA**, que
es el ramal (xxi) del acta 136: una cobertura de cero no es un verde, es un
plato vacio.

--- QUE CUENTA COMO BARRIDO EXHAUSTIVO, ESCRITO Y NO ADIVINADO ---

La afirmacion tiene que CITAR EN SU VENTANA un `docs/loop/SALIDA_V<N>_*.txt`
EXISTENTE que traiga el SELLO COMPLETO que imprime `barrer_ausencia.py`, y son
CINCO piezas, todas obligatorias:

  (1) la marca literal `BARRIDO EXHAUSTIVO`
  (2) `PREGUNTA:` con texto (que ausencia respalda ese barrido)
  (3) `UNIVERSO:` con texto (de donde sale el universo)
  (4) `CARDINAL:` con un numero MAYOR QUE CERO (un universo vacio no es un
      universo: es un barrido que no barrio nada)
  (5) `POR CONTENIDO:` (la segunda pierna). ESTA ES LA PIEZA QUE MAS IMPORTA:
      es exactamente la que faltaba el dia de la caida. Un barrido de una sola
      pierna, por nombre, NO PUEDE hallar un fichero que se llama por su
      operacion duena.

Y HAY UN ROJO CON NOMBRE PROPIO: si el fichero citado trae `candidatos
mirados:` y NO trae la marca `BARRIDO EXHAUSTIVO`, la guarda cae nombrando ESE
patron, porque es literalmente el metodo de la caida de la 145. Una lista de
rutas candidatas escritas a mano NO ES UN BARRIDO.

--- LA VENTANA, Y POR QUE ESTA ES BIDIRECCIONAL ---

La ventana es LA MISMA FRASE mas HASTA DOS FRASES ANTES y HASTA DOS DESPUES.
SE DECLARA LA DIFERENCIA CON LA GUARDA DE CIFRAS, que para COTEJAR usa
forward-only por doctrina adjudicada (acta 135, 3.1): alli ensanchar dejaria
que una cifra cuadrara contra el fichero DEL VECINO, y aqui NO HAY NADA QUE
CUADRAR. La pregunta de esta guarda es BINARIA (hay o no hay barrido sellado
respaldando esta frase) y en la prosa de estos reportes la cita del barrido
PRECEDE casi siempre a la conclusion que introduce ("Barrido en `SALIDA_X`:
no existe ninguna..."), asi que una ventana solo-adelante seria
estructuralmente incapaz de aprobar la escritura natural.

LO QUE SE PAGA POR ENSANCHAR, DICHO EN VOZ ALTA Y NO ESCONDIDO: una frase de
ausencia PODRIA apoyarse en el barrido del vecino. Lo que lo mitiga, y por eso
`PREGUNTA:` es obligatoria en el sello: el barrido tiene que declarar QUE
ausencia respalda, asi que el prestamo queda ESCRITO y visible en la salida que
la guarda imprime. Queda MARCADO COMO DISCUTIBLE en el reporte de la vuelta
146, no zanjado por mi.

--- LO QUE SE RECORTA ANTES DE PARSEAR, Y POR QUE ESO NO ES UNA PUERTA DE
SERVICIO ---

UN REPORTE QUE DOCUMENTA LA CAIDA TIENE QUE PODER CITARLA. El reporte de la
vuelta 146 cita verbatim la frase de la 3.c de la 145 (es su tarea 1.b), y esa
frase dispara este vocabulario. Si no hubiera manera de citar, la guarda
obligaria a esconder justo el texto que hay que auditar, que es lo contrario de
`EJECUTOR.md` 8.

LA SALIDA NO ES UN INTERRUPTOR QUE ESCRIBE EL AUDITADO, y esta es la leccion de
la vuelta 135 ("una exencion que escribe el auditado no es una exencion, es un
interruptor"). Un bloque de cita se delimita asi:

    <!-- CITA CONGELADA <ref>:<ruta> -->
    ...texto citado...
    <!-- FIN CITA CONGELADA -->

y LA GUARDA LO COMPRUEBA ELLA MISMA: lee el blob de ese ref con `git show` y
exige que CADA LINEA del bloque que dispara el vocabulario aparezca, VERBATIM y
tras quitar el adorno de markdown, dentro de ese blob. Una linea que no este en
el ref es ROJO NOMBRANDOLA. No se puede meter texto propio en un bloque de
cita: solo cabe lo que ya esta commiteado en el commit citado. Es el mismo
patron que la vara de citas de la vuelta 145, la que se para con la cita
muerta.

Las marcas siguen la regla de las tres de la guarda de cifras: con las dos se
quita lo delimitado, sin ninguna no se quita nada, y con UNA SOLA es ROJO.

TAMBIEN SE RECORTAN los bloques `<!-- COMMITS TALLADOS -->` y
`<!-- CABECERA TALLADA -->`, por el mismo motivo por el que la guarda de cifras
los recorta: sus lineas son ASUNTOS DE COMMIT y CELDAS TALLADAS DE
INSTRUMENTOS, no prosa del reporte, y dentro de una lista de commits o de una
tabla tallada no hay donde poner una cita. LA CABECERA SE SUMO EN LA PRIMERA
CORRIDA DE ESTA GUARDA SOBRE UN REPORTE REAL (vuelta 146, 4.c) y se dice por
que no la debilita: la celda de identidad de la cabecera trae el ASUNTO DEL
COMMIT DEL ACTA leido de `git log`, y ese asunto puede contener cualquier
formula del vocabulario sin que sea una afirmacion de quien escribe el reporte;
ademas `tallar_cabecera_reporte.py --comparar` ya exige que ese bloque sea
IDENTICO AL TALLADOR, o sea que no cabe meter ahi una frase propia.

--- CERO AFIRMACIONES VISTAS NO ES VERDE ---

Si la guarda recorre el reporte y no encuentra NINGUNA afirmacion de ausencia,
lo dice y sale VERDE con su COBERTURA en cero, PERO NOMBRANDOLO: "0 vistas" es
un dato, no un aprobado, y se imprime igual de grande que un verde lleno. NO se
sale en rojo por ello, a diferencia de la guarda de cifras, y la razon es que
un reporte sin ninguna afirmacion de ausencia es perfectamente posible y
legitimo (la mayoria de las vueltas del cribado no publicaban ninguna),
mientras que un reporte sin NINGUNA cifra no lo es.

PRUEBA DE MUTACION (obligatoria, `EJECUTOR.md` 1, "EL CASO ROJO SE PRUEBA POR
MUTACION", y sobre SUJETO CONGELADO por la CORRECCION 22):
`scripts/loop/vuelta146_2b_mutacion_ausencias.py`, salida a
`docs/loop/SALIDA_V146_2B_MUTACION_AUSENCIAS.txt`.

USO:
  python scripts/loop/verificar_ausencias_del_reporte.py
  python scripts/loop/verificar_ausencias_del_reporte.py --reporte RUTA
  python scripts/loop/verificar_ausencias_del_reporte.py --ref a9b638ba
"""
import argparse
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
RUTA_REPORTE = os.path.join(LOOP, "REPORTE.md")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verificar_cifras_del_plan import dividir_frases  # noqa: E402

# --- VOCABULARIO CERRADO DE LAS AFIRMACIONES DE AUSENCIA ---
# Ver el docstring, seccion "EL VOCABULARIO DE DISPARO". Ampliarlo es un acto
# declarado que se escribe AQUI y se dice en el reporte, nunca una adivinanza.
FORMULAS_DE_AUSENCIA = (
    "no existe", "no existen",
    "no hay ningun", "no hay ninguna",
    "hallados: ninguno", "hallado: ninguno",
    "no se hallo", "no se halla",
    "no esta en el repositorio",
    "no instalado", "no instalados",
    "prerrequisito cumplido: no",
)

# --- EL SELLO DEL BARRIDO. Contrato compartido con barrer_ausencia.py. ---
MARCA_BARRIDO = "BARRIDO EXHAUSTIVO"
PATRON_PREGUNTA = re.compile(r"^\s*PREGUNTA:\s*(\S.*)$", re.MULTILINE)
PATRON_UNIVERSO = re.compile(r"^\s*UNIVERSO:\s*(\S.*)$", re.MULTILINE)
PATRON_CARDINAL = re.compile(r"^\s*CARDINAL:\s*(\d+)\s*$", re.MULTILINE)
PATRON_POR_CONTENIDO = re.compile(r"^\s*POR CONTENIDO:", re.MULTILINE)
# El metodo exacto de la caida de la vuelta 145, cazado por su nombre.
PATRON_CANDIDATOS_A_MANO = re.compile(r"candidatos mirados\s*:", re.IGNORECASE)

PATRON_CITA_SALIDA = re.compile(r"SALIDA_V\d+_[A-Za-z0-9_]+\.txt")

MARCA_CITA_ABRE = re.compile(r"<!--\s*CITA CONGELADA\s+(\S+?):(\S+?)\s*-->")
MARCA_CITA_CIERRA = "<!-- FIN CITA CONGELADA -->"
MARCA_COMMITS_ABRE = "<!-- COMMITS TALLADOS -->"
MARCA_COMMITS_CIERRA = "<!-- FIN COMMITS TALLADOS -->"
MARCA_CABECERA_ABRE = "<!-- CABECERA TALLADA -->"
MARCA_CABECERA_CIERRA = "<!-- FIN CABECERA TALLADA -->"


def leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


def leer_ref(ref, ruta):
    r = subprocess.run(["git", "show", "%s:%s" % (ref, ruta)], cwd=RAIZ,
                       capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8", "replace")


def desadornar(linea):
    """Quita el adorno de markdown para poder cotejar una cita VERBATIM contra
    el blob de su ref: asteriscos de enfasis, acentos graves de codigo y los
    espacios de sangria y de final. No toca ninguna palabra."""
    s = linea.replace("**", "").replace("*", "").replace("`", "")
    return re.sub(r"\s+", " ", s).strip()


def dispara(frase):
    b = frase.lower()
    return [f for f in FORMULAS_DE_AUSENCIA if f in b]


def quitar_bloque_simple(texto, abre, cierra, fallos, rotulo):
    """Las tres reglas de la casa: con las dos marcas se quita lo delimitado,
    sin ninguna no se quita nada, con UNA SOLA es ROJO."""
    a, c = texto.find(abre), texto.find(cierra)
    if a == -1 and c == -1:
        return texto
    if a == -1 or c == -1:
        fallos.append("%s: falta la marca %s" % (rotulo, cierra if c == -1 else abre))
        return texto
    if c < a:
        fallos.append("%s: la marca de cierre va antes que la de apertura" % rotulo)
        return texto
    return texto[:a] + texto[c + len(cierra):]


def quitar_citas_congeladas(texto, fallos):
    """Quita los bloques `<!-- CITA CONGELADA ref:ruta -->` ... `<!-- FIN CITA
    CONGELADA -->` DESPUES DE COMPROBARLOS UNO A UNO contra el blob de su ref.
    Ver el docstring: la salida no es un interruptor que escribe el auditado."""
    fuera = []
    pos = 0
    while True:
        m = MARCA_CITA_ABRE.search(texto, pos)
        if m is None:
            break
        fin = texto.find(MARCA_CITA_CIERRA, m.end())
        if fin == -1:
            fallos.append("bloque de CITA CONGELADA abierto en el offset %d y nunca "
                          "cerrado con %s" % (m.start(), MARCA_CITA_CIERRA))
            break
        ref, ruta = m.group(1), m.group(2)
        cuerpo = texto[m.end():fin]
        blob = leer_ref(ref, ruta)
        if blob is None:
            fallos.append("CITA CONGELADA %s:%s: no se pudo leer ese blob con git show" % (ref, ruta))
        else:
            plano = desadornar(blob)
            for linea in cuerpo.split("\n"):
                if not dispara(linea):
                    continue
                aguja = desadornar(linea)
                if aguja and aguja not in plano:
                    fallos.append("CITA CONGELADA %s:%s: esta linea dispara el vocabulario "
                                  "y NO esta en ese blob, asi que no es una cita: %r"
                                  % (ref, ruta, aguja[:150]))
        fuera.append((m.start(), fin + len(MARCA_CITA_CIERRA)))
        pos = fin + len(MARCA_CITA_CIERRA)

    if texto.count(MARCA_CITA_CIERRA) != len(fuera) and not fallos:
        fallos.append("hay %d marcas %s y %d bloques de cita bien formados: descuadre"
                      % (texto.count(MARCA_CITA_CIERRA), MARCA_CITA_CIERRA, len(fuera)))

    salida, ultimo = [], 0
    for a, b in fuera:
        salida.append(texto[ultimo:a])
        ultimo = b
    salida.append(texto[ultimo:])
    return "".join(salida)


def sello_del_barrido(nombre):
    """(es_barrido, motivo) del fichero de salida citado. Ver el docstring,
    seccion QUE CUENTA COMO BARRIDO EXHAUSTIVO: las cinco piezas van todas."""
    ruta = os.path.join(LOOP, nombre)
    if not os.path.exists(ruta):
        return False, "el fichero citado no existe en docs/loop/"
    try:
        texto = leer(ruta)
    except UnicodeDecodeError:
        with io.open(ruta, "rb") as f:
            texto = f.read().decode("utf-8", "replace")
    if MARCA_BARRIDO not in texto:
        if PATRON_CANDIDATOS_A_MANO.search(texto):
            return False, ("trae 'candidatos mirados:' y NO trae la marca %r: es una "
                           "LISTA DE RUTAS A MANO, que es el metodo exacto de la caida "
                           "de la vuelta 145, no un barrido" % MARCA_BARRIDO)
        return False, "no trae la marca %r" % MARCA_BARRIDO
    faltan = []
    if not PATRON_PREGUNTA.search(texto):
        faltan.append("PREGUNTA:")
    if not PATRON_UNIVERSO.search(texto):
        faltan.append("UNIVERSO:")
    m_card = PATRON_CARDINAL.search(texto)
    if not m_card:
        faltan.append("CARDINAL:")
    elif int(m_card.group(1)) <= 0:
        faltan.append("CARDINAL: mayor que cero (un universo vacio no es un universo)")
    if not PATRON_POR_CONTENIDO.search(texto):
        faltan.append("POR CONTENIDO: (la segunda pierna, la que faltaba en la caida)")
    if faltan:
        return False, "trae la marca pero le falta: %s" % ", ".join(faltan)
    return True, "sello completo"


def ventana(frases, i):
    """La misma frase mas hasta DOS antes y hasta DOS despues. Bidireccional a
    proposito: ver el docstring, seccion LA VENTANA."""
    return " ".join(frases[max(0, i - 2):i + 3])


def verificar(texto):
    fallos = []
    texto = quitar_citas_congeladas(texto, fallos)
    texto = quitar_bloque_simple(texto, MARCA_COMMITS_ABRE, MARCA_COMMITS_CIERRA,
                                 fallos, "COMMITS TALLADOS")
    texto = quitar_bloque_simple(texto, MARCA_CABECERA_ABRE, MARCA_CABECERA_CIERRA,
                                 fallos, "CABECERA TALLADA")

    frases = dividir_frases(texto)
    vistas, respaldadas = [], []
    for i, fr in enumerate(frases):
        formulas = dispara(fr)
        if not formulas:
            continue
        vistas.append((i, fr, formulas))
        citas = PATRON_CITA_SALIDA.findall(ventana(frases, i))
        if not citas:
            fallos.append("AUSENCIA SIN BARRIDO: %r (dispara por %s) no cita ningun "
                          "SALIDA_V<N>_*.txt en su ventana"
                          % (fr.strip()[:150], ", ".join(formulas)))
            continue
        buenos, motivos = [], []
        for c in sorted(set(citas)):
            ok, motivo = sello_del_barrido(c)
            (buenos if ok else motivos).append(c if ok else "%s (%s)" % (c, motivo))
        if not buenos:
            fallos.append("AUSENCIA MAL RESPALDADA: %r (dispara por %s) cita %s, y ninguno "
                          "es un barrido exhaustivo sellado: %s"
                          % (fr.strip()[:150], ", ".join(formulas), ", ".join(sorted(set(citas))),
                             "; ".join(motivos)))
            continue
        respaldadas.append((fr, formulas, buenos))
    return fallos, vistas, respaldadas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reporte", default=RUTA_REPORTE)
    ap.add_argument("--ref", default=None,
                    help="lee el reporte del blob de ese ref en vez del arbol de trabajo")
    a = ap.parse_args()

    if a.ref:
        rel = os.path.relpath(os.path.abspath(a.reporte), RAIZ).replace("\\", "/")
        texto = leer_ref(a.ref, rel)
        if texto is None:
            print("ROJO PREVIO: no se pudo leer %s:%s" % (a.ref, rel))
            return 1
        sujeto = "%s:%s" % (a.ref, rel)
    else:
        if not os.path.exists(a.reporte):
            print("ROJO PREVIO: no existe %s" % a.reporte)
            return 1
        texto = leer(a.reporte)
        sujeto = a.reporte

    fallos, vistas, respaldadas = verificar(texto)

    print("SUJETO: %s" % sujeto)
    if fallos:
        print("ROJO EXIT 1, %d afirmacion(es) de ausencia sin barrido exhaustivo detras:"
              % len(fallos))
        for f in fallos:
            print("   %s" % f)
    else:
        print("VERDE EXIT 0: las %d afirmacion(es) de ausencia vistas vienen respaldadas "
              "por un barrido exhaustivo sellado." % len(vistas))
    for fr, formulas, buenos in respaldadas:
        print("   RESPALDADA por %s: %r" % (", ".join(buenos), fr.strip()[:120]))
    print("<!-- COBERTURA DE AUSENCIAS -->")
    print("COBERTURA DE AUSENCIAS: %d vistas / %d respaldadas / %d en rojo | vocabulario "
          "de %d formulas" % (len(vistas), len(respaldadas), len(fallos),
                              len(FORMULAS_DE_AUSENCIA)))
    print("<!-- FIN COBERTURA DE AUSENCIAS -->")
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
