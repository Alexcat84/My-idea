# -*- coding: utf-8 -*-
r"""verificar_cabecera_pegada_o_condensada.py . LA GUARDA DE LA TAREA 2 DE LA
VUELTA 107 (encargo del auditor sobre el acta de la vuelta 106, caida 1.1:
"tu cabecera dice 'pegada entera' y esta re-tecleada").

POR QUE NACE. `tallar_cabecera_reporte.py --comparar` ya coteja la cabecera
tallada contra la que un REPORTE.md YA TIENE, pero busca cada fila POR SU
ETIQUETA (`tabla_del_fichero` indexa por el texto de la primera celda): si
el reporte re-teclea la etiqueta ("censo" por "censo: nodos / vivos /
deprecados"), la fila deja de encontrarse y sale AUSENTE, aunque el VALOR de
la fila sea perfectamente fiel. Esta guarda compara POR POSICION (fila 1
contra fila 1, fila 2 contra fila 2...), que es lo que hace falta para
distinguir "la misma fila con la etiqueta condensada" de "una fila que de
verdad falta o se movio de sitio".

QUE MIDE, LAS DOS COSAS POR SEPARADO. (a) NUMERO DE FILAS Y ORDEN: si el
reporte trae mas o menos filas que el tallador, ROJO directo. El ORDEN se
verifica indirectamente: si una fila cambio de posicion, sus cifras ya no
calzan contra la fila tallada de esa misma posicion, y eso lo atrapa la
comprobacion (b). (b) POR CADA CELDA (etiqueta, apertura, cierre) de cada
fila: normaliza (colapsa espacios repetidos, quita `**` y comillas
invertidas, Y NADA MAS: no se normalizan abreviaturas ni sinonimos, porque
eso es justo lo que tiene que saltar) y compara el texto entero. Si el texto
normalizado es IDENTICO, la celda esta PEGADA. Si difiere, se extraen TODOS
los numeros de la celda (secuencias de digitos con separador de miles) de
las dos versiones: si el CONJUNTO de numeros calza, la celda cambio de
REDACCION pero no de CIFRA (retecleada, no rota); si el conjunto de numeros
NO calza, es una CIFRA DISTINTA, y eso es ROJO siempre, sea cual sea el
veredicto general.

VEREDICTO GENERAL, LAS DOS PALABRAS EXACTAS QUE PIDE EL ENCARGO:
  - "PEGADA ENTERA": las N filas, las tres celdas de cada una, identicas
    tras normalizar.
  - "CONDENSADA": mismo numero de filas, mismo orden (ninguna cifra
    descuadrada), pero M de N filas con alguna celda retecleada.
  - ROJO (no es un tercer nombre, es la ausencia de veredicto): el numero
    de filas no calza, o alguna celda trae una cifra distinta, o el propio
    reporte AFIRMA "pegada entera" cuando esta guarda mide CONDENSADA.

USO:
  python scripts/loop/verificar_cabecera_pegada_o_condensada.py --vuelta 107
  python scripts/loop/verificar_cabecera_pegada_o_condensada.py --vuelta 106 --reporte <(git show e1fefbba:docs/loop/REPORTE.md)
  python scripts/loop/verificar_cabecera_pegada_o_condensada.py --vuelta 106 --reporte docs/loop/_v107_tarea2_reporte106_mutado.md

CASO POSITIVO Y CASO ROJO: ver docs/loop/SALIDA_V107_TAREA2_3_CASO_POSITIVO_V106.txt
(CONDENSADA, 8 de 10) y docs/loop/SALIDA_V107_TAREA2_4_CASO_ROJO_MUTACION.txt
(cifra alterada, la guarda la senala).
"""
import argparse
import importlib.util
import io
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TALLADOR = os.path.join(RAIZ, "scripts", "loop", "tallar_cabecera_reporte.py")


def _cargar_tallador():
    spec = importlib.util.spec_from_file_location("tallar_cabecera_reporte", TALLADOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def filas_talladas(mod, vuelta, con_miles=True):
    """Reproduce EXACTAMENTE el camino de main() en modo --fase04 hasta
    construir `f` (la lista de filas), sin imprimir nada."""
    fallos = []
    apertura = mod.lado_fase04(vuelta, "APERTURA", fallos, con_miles)
    cierre = mod.lado_fase04(vuelta, "CIERRE", fallos, con_miles)
    rama = mod.rama_actual(fallos)
    commit_ap, asunto_acta = mod.commit_apertura_desde_git(vuelta, rama, fallos)
    head_real = mod.leer_head_apertura(vuelta, fallos)
    procedencia_sello = mod.procedencia_sello_apertura(vuelta, rama, head_real, fallos)
    head_cierre = mod.leer_head_cierre(vuelta, fallos)
    arbol_verde = None
    if commit_ap and head_real:
        arbol_acta = mod.arbol_dataset(commit_ap, "commit del acta %s" % commit_ap, fallos)
        arbol_head = mod.arbol_dataset(head_real, "HEAD real de apertura %s" % head_real[:8], fallos)
        if arbol_acta is not None and arbol_head is not None:
            arbol_verde = arbol_acta == arbol_head
    if fallos:
        return None, fallos

    f = mod.filas_fase04(apertura, cierre, con_miles)
    celda_identidad_ap = (
        "rama `%s`, commit del acta `%s` (asunto real leido de git log: %r), "
        "HEAD real de apertura `%s` (%s, leido de git log --diff-filter=A), arboles "
        "de `dataset/` %s"
        % (rama, commit_ap, asunto_acta, head_real[:8], procedencia_sello,
           "IGUALES: VERDE" if arbol_verde else "?")
    )
    celda_identidad_ci = (
        "rama `%s`, HEAD de cierre `%s` (leido de `SALIDA_V%d_HEAD_CIERRE.txt`, "
        "sellado tras la ultima operacion)"
        % (rama, head_cierre[:8] if head_cierre else "?", vuelta)
    )
    f.append(("identidad: rama y commit de apertura (leidos de git, no tecleados)",
              celda_identidad_ap, celda_identidad_ci))
    return f, fallos


RE_FILA = re.compile(r"^\|\s*(.*?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")
RE_SEP = re.compile(r"^\|[\s:-]+\|[\s:-]+\|[\s:-]+\|$")


def filas_del_reporte(ruta):
    """Extrae la PRIMERA tabla de 3 columnas que sigue a una linea que
    contenga la palabra CABECERA, EN ORDEN (no indexada por etiqueta)."""
    texto = io.open(ruta, encoding="utf-8").read()
    lineas = texto.splitlines()
    inicio = None
    for i, l in enumerate(lineas):
        if "CABECERA" in l.upper():
            inicio = i
            break
    if inicio is None:
        return None, "no se encontro una linea con 'CABECERA' en %s" % ruta
    filas = []
    vista_header = False
    vista_sep = False
    for l in lineas[inicio:]:
        l = l.strip()
        if not l.startswith("|"):
            if vista_sep:
                break
            continue
        if RE_SEP.match(l):
            vista_sep = True
            continue
        m = RE_FILA.match(l)
        if not m:
            continue
        if not vista_header:
            vista_header = True
            continue
        if not vista_sep:
            continue
        filas.append((m.group(1), m.group(2), m.group(3)))
    if not filas:
        return None, "no se hallo una tabla de datos tras la linea CABECERA en %s" % ruta
    return filas, None


def normalizar(celda):
    celda = celda.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", celda).strip()


RE_NUMERO = re.compile(r"\d[\d.,]*\d|\d")


def numeros(celda):
    """Los numeros de la celda, con el punto de millares quitado (el
    tallador los escribe '3.388'; una redaccion condensada puede escribirlos
    '3388' y sigue siendo la MISMA cifra). La coma NO se toca: en este
    corpus la coma es separador DECIMAL de porcentaje ('60,1%'), nunca de
    millares, asi que quitarla cambiaria el valor."""
    return sorted(n.replace(".", "") for n in RE_NUMERO.findall(celda))


def cotejar(f_tallada, f_reporte):
    n_t = len(f_tallada)
    n_r = len(f_reporte)
    if n_t != n_r:
        return {
            "veredicto": "ROJO",
            "razon": "numero de filas distinto: tallador %d, reporte %d" % (n_t, n_r),
        }

    filas_retecleadas = 0
    detalle = []
    cifras_rotas = []
    for i in range(n_t):
        et_t, ap_t, ci_t = f_tallada[i]
        et_r, ap_r, ci_r = f_reporte[i]
        fila_identica = True
        for nombre, tallado, real in (("etiqueta", et_t, et_r), ("apertura", ap_t, ap_r),
                                      ("cierre", ci_t, ci_r)):
            nt, nr = normalizar(tallado), normalizar(real)
            if nt == nr:
                continue
            fila_identica = False
            # SUBCONJUNTO, no igualdad: condensar puede DEJAR FUERA una cifra
            # redundante (el total entre parentesis, p.ej.), y eso no es una
            # cifra distinta. Lo que SI es rojo es que aparezca en el reporte
            # una cifra que el tallador no tiene en esa misma celda.
            if not set(numeros(nr)) <= set(numeros(nt)):
                cifras_rotas.append((i + 1, nombre, nt, nr))
        if not fila_identica:
            filas_retecleadas += 1
            detalle.append(i + 1)

    if cifras_rotas:
        return {
            "veredicto": "ROJO",
            "razon": "cifra distinta (no solo redaccion) en %d celda(s)" % len(cifras_rotas),
            "cifras_rotas": cifras_rotas,
        }

    if filas_retecleadas == 0:
        return {"veredicto": "PEGADA ENTERA", "n": n_t}

    return {"veredicto": "CONDENSADA", "n": n_t, "m": filas_retecleadas, "filas": detalle}


RE_ANUNCIO_CABECERA = re.compile(r"^\*{0,2}CABECERA\b", re.IGNORECASE)


def reporte_afirma_pegada_entera(ruta):
    """Busca 'pegada entera' SOLO en la linea que ANUNCIA la cabecera (la
    que EMPIEZA, tras quitar el resaltado, con la palabra CABECERA: el
    patron `**CABECERA, tallada con...`), no en cualquier linea que
    mencione la palabra de pasada (por ejemplo, el nombre del propio
    script `tallar_cabecera_reporte.py` la contiene) ni en el reporte
    entero, donde puede EXPLICAR la guarda citando la frase entre
    comillas sin que eso sea una promesa sobre su propia tabla."""
    for l in io.open(ruta, encoding="utf-8").read().splitlines():
        if RE_ANUNCIO_CABECERA.match(l.strip()):
            return "pegada entera" in l.lower()
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, required=True)
    ap.add_argument("--reporte", default=os.path.join("docs", "loop", "REPORTE.md"))
    a = ap.parse_args()

    ruta_reporte = a.reporte if os.path.isabs(a.reporte) else os.path.join(RAIZ, a.reporte)

    mod = _cargar_tallador()
    f_tallada, fallos = filas_talladas(mod, a.vuelta)
    if f_tallada is None:
        print("ROJO: la cabecera no se pudo tallar (%d fallo(s)):" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    f_reporte, err = filas_del_reporte(ruta_reporte)
    if f_reporte is None:
        print("ROJO: %s" % err)
        return 1

    resultado = cotejar(f_tallada, f_reporte)
    veredicto = resultado["veredicto"]

    # LA MEDICION SE IMPRIME SIEMPRE, aunque el veredicto final sea rojo por
    # otra razon: "CONDENSADA" es lo que la tabla ES, no un juicio de si el
    # reporte tenia permiso para estarlo.
    if veredicto == "ROJO":
        print("ROJO: %s" % resultado["razon"])
        for fila, nombre, nt, nr in resultado.get("cifras_rotas", []):
            print("   fila %d, %s: tallador dice %r, reporte dice %r" % (fila, nombre, nt, nr))
        return 1

    if veredicto == "PEGADA ENTERA":
        print("MEDICION: PEGADA ENTERA. Las %d filas, identicas tras normalizar." % resultado["n"])
    else:
        print("MEDICION: CONDENSADA. %d de %d filas con alguna celda retecleada (filas %s), "
              "ninguna cifra descuadrada." % (resultado["m"], resultado["n"], resultado["filas"]))

    afirma_pegada = reporte_afirma_pegada_entera(ruta_reporte)
    if veredicto == "CONDENSADA" and afirma_pegada:
        print("ROJO: el reporte dice 'pegada entera' pero la medicion de arriba es CONDENSADA: "
              "prometer una cosa y medir otra.")
        return 1

    print("VERDE: la medicion de arriba calza con lo que el reporte afirma.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
