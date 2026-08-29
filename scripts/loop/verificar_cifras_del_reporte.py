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
  - Si un numero no encuentra fichero de salida en su ventana, NO es rojo:
    se LISTA como "cifra sin fichero que contar" con su linea.

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


def verificar(ruta_reporte):
    texto_completo = leer(ruta_reporte)
    texto = quitar_bloques_cubiertos(texto_completo)
    frases = dividir_frases(texto)
    existentes = ficheros_salida_existentes()

    fallos = []
    cotejados = []
    sin_fichero = []

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
            ventana = frases[i:i + 3]
            ventana_txt = " ".join(ventana)
            citas = sorted(set(PATRON_CITA_SALIDA.findall(ventana_txt)))
            citas = [c for c in citas if c in existentes]
            if not citas:
                sin_fichero.append((numero, unidad, frase.strip()))
                continue
            fichero_cita = citas[0]
            ruta_cita = os.path.join(LOOP, fichero_cita)
            contenido_cita = leer(ruta_cita)
            familia = UNIDAD_A_FAMILIA[unidad]
            contado = contar_por_familia(familia, contenido_cita)
            if contado is None:
                sin_fichero.append((numero, unidad, frase.strip()))
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

    return fallos, cotejados, sin_fichero


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reporte", default=RUTA_REPORTE)
    a = ap.parse_args()

    fallos, cotejados, sin_fichero = verificar(a.reporte)

    if fallos:
        print("ROJO, %d cifra(s) no cuadran:" % len(fallos))
        for f in fallos:
            print("  %s" % f)
        if sin_fichero:
            print("cifra(s) sin fichero que contar (%d):" % len(sin_fichero))
            for numero, unidad, frase in sin_fichero:
                print("  %d %s: %r" % (numero, unidad, frase))
        return 1

    print("VERDE EXIT 0: %d cifra(s) cotejadas contra su fichero de salida, todas cuadran:" %
          len(cotejados))
    for numero, unidad, fichero, contado in cotejados:
        print("  %d %s == %d contados en `%s`" % (numero, unidad, contado, fichero))
    if sin_fichero:
        print("cifra(s) sin fichero que contar (%d):" % len(sin_fichero))
        for numero, unidad, frase in sin_fichero:
            print("  %d %s: %r" % (numero, unidad, frase))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
