# -*- coding: utf-8 -*-
r"""verificar_cifras_del_reporte.py . LA SEGUNDA MITAD DE LA ESCALADA (TAREA
2.e de la vuelta 133, encargada por AUDITOR.md 1.2 al llegar la racha de
reporte a DOS tandas seguidas, acta de la vuelta 132). EJECUTOR.md 1 la nombra
literal: "la extension del tallador a las fases mecanicas", "TODA TABLA DEL
REPORTE TALLADA DE FICHEROS DE SALIDA".

POR QUE NACE. La racha de las vueltas 74, 75 y 76 (EJECUTOR.md, "LA TABLA SE
CUENTA DE SU FICHERO") mostro que en el tramo mecanico las cifras del reporte
se volvieron a teclear, porque `tallar_cabecera_reporte.py` solo cubre LA
CABECERA (censo, Gate 0, aristas, motor, web, tsc, marcador) y
`tallar_identidad_reporte.py` (2.a) solo cubre EL PARRAFO DE IDENTIDAD: el
CUERPO del reporte, con sus tablas de adjudicaciones y sus cifras de prosa,
sigue sin ningun instrumento que lo muerda.

CONTRATO (cerrado, para no tener que decidir nada al correrla):
  - Recorre docs/loop/REPORTE.md SALTANDO la tabla tallada de la cabecera
    (delimitada por las lineas que `tallar_cabecera_reporte.py --comparar`
    reconoce: se salta desde la primera fila de tabla markdown hasta la
    ultima fila de tabla consecutiva del bloque de cabecera) y el parrafo de
    identidad (las tres lineas de rotulo que empiezan por "HEAD sellado" o
    "commit de nacimiento").
  - Busca pares (numero, unidad) con VOCABULARIO CERRADO de unidades:
    fichero/ficheros, par/pares, grupo/grupos, grafia/grafias,
    colapso/colapsos, nodo/nodos, linea/lineas, arista/aristas (singular o
    plural, sin distinguir mayusculas).
  - Para cada par, busca en la MISMA frase o en las DOS SIGUIENTES una cita
    de docs/loop/SALIDA_V<N>_*.txt: MISMA doctrina de ventana que
    `verificar_cifras_del_plan.py` (se REUSA `dividir_frases` de ese modulo,
    no se reinventa).
  - Si hay cita, CUENTA la cifra EN ESE FICHERO (nunca confia en un total ya
    impreso por el instrumento: se recuentan las instancias, "la tabla se
    cuenta de su fichero"). LA UNIDAD MANDA COMO SE CUENTA (ramal xvii):
      * fichero/ficheros: tokens DISTINTOS que parecen ruta de fichero (con
        extension conocida), deduplicados por cadena literal.
      * par/pares: tokens DISTINTOS `<ruta>:<numero>` (fichero:linea).
      * arista/aristas: lineas que traen `IZQUIERDA -> DERECHA` (el formato
        que ya usan `vuelta83_conteo_aristas.py`, `verificar_aristas_vivas.py`
        y `verificar_huerfanas_por_fusion.py`).
      * linea/lineas: lineas no vacias del fichero.
      * grupo/grupos, grafia/grafias, colapso/colapsos, nodo/nodos: no hay
        una convencion mecanica establecida todavia en ningun instrumento de
        esta campana para estas cuatro unidades (ninguna de ellas imprime,
        hoy, un listado de una linea por entidad con un separador fijo). Se
        cuenta con la MISMA convencion generica declarada aqui (lineas no
        vacias con sangria de lista, es decir que empiezan por dos o mas
        espacios y NO son una linea de arista ni de par), documentada para
        que sea auditable, PERO cuando esa cuenta no permita distinguir con
        confianza la unidad pedida, la guarda prefiere no inventar: si el
        fichero citado no tiene NINGUNA linea de ese tipo, se trata como
        "cifra sin fichero que contar" en vez de fabricar un cero espurio.
    Si las dos cuentas posibles del mismo bloque (ficheros vs pares) dan
    numeros distintos y la cifra escrita coincide con la que NO corresponde a
    su unidad, ROJO nombrando las dos cuentas (ramal xvii hecho codigo).
  - Si no cuadra, ROJO EXIT 1 con la linea, el numero escrito, el numero
    contado y el fichero.
  - LA SALIDA DE EMERGENCIA, ESTRECHADA EN LA VUELTA 134 (acta 133, 4.4: la
    version vieja de esta regla se tragaba 7 de 8 cifras del reporte y la
    escalada nacio ciega). Una cifra (numero, unidad) SIN fichero de salida
    en su ventana (ni citado, ni citado-pero-incontable) es ROJO EXIT 1
    nombrando la linea y la cifra, SALVO que caiga en una de estas TRES
    exenciones, cerradas y todas:
      (i) las cifras del parrafo de identidad y de la tabla tallada de la
          cabecera: ya quedan fuera porque quitar_bloques_cubiertos() las
          retira antes de parsear, asi que nunca llegan a esta funcion.
      (ii) la cifra del tope de 1.k, que habla del propio REPORTE.md (frase
          que trae "wc -l" y "REPORTE.md" con unidad linea/lineas): se
          coteja con el conteo EN VIVO de lineas del propio fichero del
          reporte, no con un SALIDA_V*.txt. Si cuadra, CUENTA COMO COTEJADA.
      (iii) una cifra que el reporte marque explicitamente con el literal
          `(sin instrumento)` PEGADO justo detras del numero y su unidad:
          se LISTA APARTE, en su propia lista de "exentas por (sin
          instrumento)", y CUENTA en la linea de COBERTURA, pero no se
          verifica contra nada.
    NINGUNA OTRA EXENCION.

LO QUE ESTA GUARDA NO CUBRE, DICHO EN VEZ DE CALLADO: los headline de
`docs/plan/OP_S_11_MAPEO_PROPUESTO.md` (105 grupos, 104, 39 grafias, etc.) NO
citan un `SALIDA_V<N>_*.txt` a su lado (citan la tabla del plan, que
`verificar_cifras_del_plan.py` ya declara, por contrato propio, que NUNCA
puede mirar): esas cifras caen, por diseno, en "cifra sin fichero que contar",
no en rojo ni en verde. Esta guarda solo puede cotejar lo que un
`SALIDA_V<N>_*.txt` mecanico realmente contiene.

USO:
  python scripts/loop/verificar_cifras_del_reporte.py
  python scripts/loop/verificar_cifras_del_reporte.py --reporte RUTA

PRUEBA DE MUTACION (obligatoria, EJECUTOR.md 1 "EL CASO ROJO SE PRUEBA POR
MUTACION"): scripts/loop/vuelta133_tarea2e_mutacion_cifras.py, salida a
docs/loop/SALIDA_V133_2E_MUTACION.txt.

--- LA PUERTA DE SERVICIO SE TAPIA (TAREA 2 de la vuelta 135, acta 134,
4.1) ---

POR QUE NACE. La exencion (iii) de arriba eximia una cifra con SOLO el
literal `(sin instrumento)` pegado, escrito por EL AUDITADO, sin que la
guarda comprobara nada por si misma. El auditor lo probo con tres
mutaciones sobre el reporte real de la 134: `118 grafias` a `999 grafias`
dio VERDE EXIT 0, `54 grupos` a `77 grupos` dio VERDE EXIT 0, y solo una
cifra nueva SIN marca y sin fichero dio ROJO. Las dos primeras cifras SI
tenian fichero de instrumento commiteado cerca (`SALIDA_V134_4A_CENSO_
COLA.txt` y `SALIDA_V134_4B_EFECTO_CAP.txt`) y la exencion las dejaba
pasar de todos modos: "una exencion que escribe el auditado no es una
exencion, es un interruptor" (ramal xix).

LA CONDICION NUEVA (2.b). El literal `(sin instrumento)` exime una cifra
SOLO SI la guarda comprueba, ELLA MISMA, que en la VENTANA AMPLIA de esa
cifra (`ventana_amplia()`: la propia frase mas HASTA DOS frases ANTES y
HASTA DOS frases DESPUES, bidireccional) no hay ningun `SALIDA_V<N>_*.txt`
existente citado. Se ensancha la ventana SOLO para esta pregunta binaria
(hay o no hay UN fichero cerca): en la prosa de este reporte la cita casi
siempre PRECEDE al numero que introduce (patron "4.a (`FICHERO`, ...): ...
<numero> ...") y el wrap de linea de `dividir_frases` corta la frase justo
ahi, así que una ventana solo-adelante (la que sigue usando, SIN TOCAR, el
cotejo normal de mas abajo, MISMA doctrina que `verificar_cifras_del_
plan.py`) no la veria nunca. Si la ventana amplia SI trae un fichero
citado, el literal es ILEGAL: ROJO EXIT 1 nombrando la linea, la cifra y
el fichero, motivo "hay instrumento en la ventana: la cifra se coteja, no
se exime". Las exenciones (i) y (ii) NO cambian. NINGUNA CUARTA EXENCION.

LA LINEA `CIFRA` (2.c). Para que tapiar la puerta no deje al auditado sin
salida honesta, un instrumento puede imprimir una linea
`CIFRA <etiqueta>: <n> <unidad>` (unidad del vocabulario cerrado de
arriba). Cuando una cifra del reporte cita un fichero, la guarda busca
PRIMERO una linea `CIFRA` de esa MISMA familia de unidad en ese fichero y
coteja contra ella; solo si no la encuentra cae a la convencion generica
de recuento (`contar_por_familia`) que ya tenia. Si no puede contar de
ninguna de las dos maneras, sigue siendo ROJO nombrando el fichero.

PRUEBA DE MUTACION (obligatoria): scripts/loop/vuelta135_2e_mutacion_1.py,
_2.py y _3.py, salidas a docs/loop/SALIDA_V135_2E_MUTACION_1.txt, _2.txt y
_3.txt: (1) `118 grafias` a `999 grafias` sobre copia del reporte real de
la 134, ROJO; (2) `54 grupos` a `77 grupos`, ROJO; (3) caso negativo, una
cifra con fichero citado, linea `CIFRA` puesta y numero CORRECTO, VERDE.
"""
import argparse
import glob
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
RUTA_REPORTE = os.path.join(LOOP, "REPORTE.md")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verificar_cifras_del_plan import dividir_frases  # noqa: E402

UNIDADES = ["fichero", "ficheros", "par", "pares", "grupo", "grupos",
            "grafia", "grafias", "colapso", "colapsos", "nodo", "nodos",
            "linea", "lineas", "arista", "aristas"]
PATRON_NUMERO_UNIDAD = re.compile(
    r"\b(\d+(?:[.,]\d+)?)\s+(%s)\b" % "|".join(UNIDADES), re.IGNORECASE)
PATRON_CITA_SALIDA = re.compile(r"SALIDA_V\d+_[A-Za-z0-9_]+\.txt")
PATRON_RUTA_FICHERO = re.compile(
    r"[A-Za-z0-9_./\\-]+\.(?:py|md|ts|tsx|js|jsx|json|jsonl|txt)\b")
PATRON_PAR_FICHERO_LINEA = re.compile(
    r"[A-Za-z0-9_./\\-]+\.(?:py|md|ts|tsx|js|jsx|json|jsonl|txt):\d+\b")
PATRON_ARISTA = re.compile(r"^\s*\S+\s*->\s*\S+", re.MULTILINE)
PATRON_CIFRA_ETIQUETA = re.compile(
    r"^CIFRA\s+[^:\n]+:\s*(\d+(?:[.,]\d+)?)\s+(%s)\b" % "|".join(UNIDADES),
    re.IGNORECASE | re.MULTILINE)


def leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


def quitar_bloques_cubiertos(texto):
    """Quita la tabla de cabecera (tallada por tallar_cabecera_reporte.py) y
    el parrafo de identidad (tallado por tallar_identidad_reporte.py, 2.a):
    esos dos bloques ya tienen su propio tallador y no se recorren aqui."""
    lineas = texto.split("\n")
    fuera = []
    en_tabla_cabecera = False
    for l in lineas:
        es_fila_tabla = l.strip().startswith("|")
        es_rotulo_identidad = (l.startswith("HEAD sellado") or
                                l.startswith("commit de nacimiento") or
                                "HEAD sellado de apertura" in l or
                                "HEAD sellado de cierre" in l or
                                "commit de nacimiento de las salidas de apertura" in l)
        if es_rotulo_identidad:
            continue
        if es_fila_tabla:
            en_tabla_cabecera = True
            continue
        if en_tabla_cabecera and not es_fila_tabla:
            en_tabla_cabecera = False
        fuera.append(l)
    return "\n".join(fuera)


def contar_ficheros(contenido):
    return len(set(PATRON_RUTA_FICHERO.findall(contenido)))


def contar_pares(contenido):
    return len(set(PATRON_PAR_FICHERO_LINEA.findall(contenido)))


def contar_aristas(contenido):
    return len(PATRON_ARISTA.findall(contenido))


def contar_lineas(contenido):
    return len([l for l in contenido.split("\n") if l.strip()])


def contar_por_cifra_etiquetada(contenido, unidad):
    """2.c: busca PRIMERO una linea `CIFRA <etiqueta>: <n> <unidad>` de la
    MISMA unidad CANONICA (singular/plural de la MISMA palabra: "grafia" no
    cotejua contra una linea CIFRA de "grupo" solo por compartir familia
    generica). Devuelve None si no hay ninguna (el llamador cae a
    `contar_por_familia`)."""
    canonica = UNIDAD_CANONICA[unidad]
    for m in PATRON_CIFRA_ETIQUETA.finditer(contenido):
        numero_txt = m.group(1).replace(".", "").replace(",", "")
        u = m.group(2).lower()
        if UNIDAD_CANONICA.get(u) == canonica and numero_txt.isdigit():
            return int(numero_txt)
    return None


def ventana_amplia(frases, i):
    """2.b: ventana BIDIRECCIONAL (+/-2), SOLO para decidir la LEGALIDAD de
    la exencion (iii). La cita casi siempre PRECEDE al numero en la prosa
    de este reporte; la ventana forward-only del cotejo normal (sin tocar,
    mas abajo) no la veria. Ver docstring del modulo."""
    return frases[max(0, i - 2):i + 3]


def contar_generico_bullets(contenido):
    """Convencion generica para grupo/grafia/colapso/nodo (docstring del
    modulo): lineas con sangria de lista (2+ espacios) que no son ya una
    arista ni un par fichero:linea. Devuelve None si no hay ninguna (para que
    el llamador prefiera 'sin fichero que contar' antes que fabricar un
    cero)."""
    n = 0
    for l in contenido.split("\n"):
        if not re.match(r"^\s{2,}\S", l):
            continue
        if PATRON_ARISTA.match(l) or PATRON_PAR_FICHERO_LINEA.search(l):
            continue
        n += 1
    return n if n > 0 else None


UNIDAD_A_FAMILIA = {
    "fichero": "fichero", "ficheros": "fichero",
    "par": "par", "pares": "par",
    "arista": "arista", "aristas": "arista",
    "linea": "linea", "lineas": "linea",
    "grupo": "generico", "grupos": "generico",
    "grafia": "generico", "grafias": "generico",
    "colapso": "generico", "colapsos": "generico",
    "nodo": "generico", "nodos": "generico",
}

# Canonica SINGULAR de cada unidad (2.c): la familia de arriba agrupa
# grupo/grafia/colapso/nodo en un solo "generico" para el CONTEO GENERICO
# (ninguno tiene convencion mecanica propia), pero la linea `CIFRA` SI
# distingue entre ellas: "118 grafias" y "54 grupos" son unidades
# DISTINTAS y no pueden cotejar contra la misma linea `CIFRA` solo porque
# comparten familia generica.
UNIDAD_CANONICA = {
    "fichero": "fichero", "ficheros": "fichero",
    "par": "par", "pares": "par",
    "grupo": "grupo", "grupos": "grupo",
    "grafia": "grafia", "grafias": "grafia",
    "colapso": "colapso", "colapsos": "colapso",
    "nodo": "nodo", "nodos": "nodo",
    "linea": "linea", "lineas": "linea",
    "arista": "arista", "aristas": "arista",
}


def contar_por_familia(familia, contenido):
    if familia == "fichero":
        return contar_ficheros(contenido)
    if familia == "par":
        return contar_pares(contenido)
    if familia == "arista":
        return contar_aristas(contenido)
    if familia == "linea":
        return contar_lineas(contenido)
    return contar_generico_bullets(contenido)


def ficheros_salida_existentes():
    return set(os.path.basename(p) for p in glob.glob(os.path.join(LOOP, "SALIDA_V*.txt")))


def contar_lineas_del_propio_reporte(ruta_reporte):
    """Replica `wc -l`: cuenta caracteres de nueva linea, no lineas con
    contenido (wc -l no distingue lineas en blanco)."""
    with io.open(ruta_reporte, "rb") as f:
        return f.read().count(b"\n")


def clasificar_exencion(frase, m, unidad):
    """Devuelve 'ii', 'iii' o None. (i) no llega aqui: ya la quito
    quitar_bloques_cubiertos() antes de parsear."""
    resto = frase[m.end():].lstrip()
    if resto.startswith("(sin instrumento)"):
        return "iii"
    if unidad in ("linea", "lineas") and "wc -l" in frase and "REPORTE.md" in frase:
        return "ii"
    return None


def verificar(ruta_reporte):
    texto_completo = leer(ruta_reporte)
    texto = quitar_bloques_cubiertos(texto_completo)
    frases = dividir_frases(texto)
    existentes = ficheros_salida_existentes()

    fallos = []
    cotejados = []
    exentas_sin_instrumento = []
    total_cifras = 0

    for i, frase in enumerate(frases):
        for m in PATRON_NUMERO_UNIDAD.finditer(frase):
            numero_txt = m.group(1)
            unidad = m.group(2).lower()
            if "," in numero_txt or "." in numero_txt:
                numero_txt_norm = numero_txt.replace(".", "").replace(",", "")
            else:
                numero_txt_norm = numero_txt
            if not numero_txt_norm.isdigit():
                continue
            numero = int(numero_txt_norm)
            total_cifras += 1

            exencion = clasificar_exencion(frase, m, unidad)
            if exencion == "iii":
                ventana_ilegal = ventana_amplia(frases, i)
                ventana_ilegal_txt = " ".join(ventana_ilegal)
                citas_cercanas = sorted(set(PATRON_CITA_SALIDA.findall(ventana_ilegal_txt)))
                citas_cercanas = [c for c in citas_cercanas if c in existentes]
                if citas_cercanas:
                    fallos.append(
                        "linea %d: \"%d %s\" marca (sin instrumento) pero su ventana amplia "
                        "SI cita `%s`: la cifra se coteja, no se exime (hay instrumento en la "
                        "ventana)" % (i, numero, unidad, citas_cercanas[0]))
                    continue
                exentas_sin_instrumento.append((numero, unidad, frase.strip()))
                continue
            if exencion == "ii":
                contado_vivo = contar_lineas_del_propio_reporte(ruta_reporte)
                if contado_vivo != numero:
                    fallos.append(
                        "linea %d: tope 1.k \"%d %s\" <-> `wc -l %s`: contado %d" %
                        (i, numero, unidad, os.path.basename(ruta_reporte), contado_vivo))
                else:
                    cotejados.append((numero, unidad, "wc -l %s" % os.path.basename(ruta_reporte), contado_vivo))
                continue

            ventana = frases[i:i + 3]
            ventana_txt = " ".join(ventana)
            citas = sorted(set(PATRON_CITA_SALIDA.findall(ventana_txt)))
            citas = [c for c in citas if c in existentes]
            if not citas:
                fallos.append(
                    "linea %d: \"%d %s\" SIN fichero de salida en su ventana (ni exenta): %r" %
                    (i, numero, unidad, frase.strip()))
                continue
            fichero_cita = citas[0]
            ruta_cita = os.path.join(LOOP, fichero_cita)
            contenido_cita = leer(ruta_cita)
            familia = UNIDAD_A_FAMILIA[unidad]
            contado = contar_por_cifra_etiquetada(contenido_cita, unidad)
            if contado is None:
                contado = contar_por_familia(familia, contenido_cita)
            if contado is None:
                fallos.append(
                    "linea %d: \"%d %s\" cita `%s` pero no se pudo CONTAR en el (ni exenta)" %
                    (i, numero, unidad, fichero_cita))
                continue
            if contado != numero:
                # ramal (xvii): si la otra familia cotejable (fichero vs par)
                # SI cuadra, se nombra para que se vea que la unidad escrita
                # es la que esta mal, no la cifra.
                otra = None
                if familia == "fichero":
                    otra = ("par", contar_pares(contenido_cita))
                elif familia == "par":
                    otra = ("fichero", contar_ficheros(contenido_cita))
                msg = ("linea %d: \"%d %s\" <-> `%s`: contado %d" %
                       (i, numero, unidad, fichero_cita, contado))
                if otra and otra[1] == numero:
                    msg += (" (NO CUADRA como %s, pero SI cuadra como %s: %d; "
                            "la unidad escrita no corresponde a la cifra)" %
                            (unidad, otra[0], otra[1]))
                fallos.append(msg)
            else:
                cotejados.append((numero, unidad, fichero_cita, contado))

    return fallos, cotejados, exentas_sin_instrumento, total_cifras


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reporte", default=RUTA_REPORTE)
    a = ap.parse_args()

    fallos, cotejados, exentas, total_cifras = verificar(a.reporte)
    cobertura = "COBERTURA: %d cotejadas / %d exentas / %d cifras" % (
        len(cotejados), len(exentas), total_cifras)

    if fallos:
        print("ROJO, %d cifra(s) no cuadran:" % len(fallos))
        for f in fallos:
            print("  %s" % f)
        if exentas:
            print("cifra(s) exentas por (sin instrumento) (%d):" % len(exentas))
            for numero, unidad, frase in exentas:
                print("  %d %s: %r" % (numero, unidad, frase))
        print(cobertura)
        return 1

    print("VERDE EXIT 0: %d cifra(s) cotejadas contra su fichero de salida o wc -l, todas cuadran:" %
          len(cotejados))
    for numero, unidad, fichero, contado in cotejados:
        print("  %d %s == %d contados en `%s`" % (numero, unidad, contado, fichero))
    if exentas:
        print("cifra(s) exentas por (sin instrumento) (%d):" % len(exentas))
        for numero, unidad, frase in exentas:
            print("  %d %s: %r" % (numero, unidad, frase))
    print(cobertura)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
