# -*- coding: utf-8 -*-
r"""verificar_cabecera_mapeo.py . TAREA 2.f de la vuelta 134 (acta 133,
4.7), EXTENDIDA A SEIS PELDANOS en la TAREA 4.c de la vuelta 135 (acta
134, 3.3: la extension de la cola a `Caps?.` reordena el peldano de
localizador y el de prefijo, y esta guarda tiene que verlos los seis).

CONTRATO:
  - Recomputa desde dataset/ los SEIS peldanos de la cadena (cadena
    entera; mas titulo; mas localizador con la cola VIEJA; mas Apendice
    en la cola; mas prefijo sobre recortada con Apendice; mas abreviatura
    `Caps?.` en la cola Y en el prefijo), REUSANDO
    `vuelta135_tabla_mapeo_propuesto.py` (que ya recomputa e IMPRIME los
    seis en su stdout), sin reimplementar el union-find.
  - Lee la cabecera de docs/plan/OP_S_11_MAPEO_PROPUESTO.md (todo el texto
    antes de la fila `| grafia | canonica propuesta | ...`), extrae CADA
    cifra `**N grupos**` que declara (multiconjunto, sin importar el orden
    en que aparezcan en la prosa) y coteja contra el recomputo. Si la
    cabecera declara MENOS peldanos de los que el recomputo produce, ES
    ROJO EXIT 1 nombrando el peldano que falta (numero y etiqueta).
  - Coteja tambien las cifras de cierre de la cabecera (grupos totales,
    grupos de 2+, grafias en grupo, sin agrupar, colapsos que faltan,
    canonicas SINTETICAS) y el TOTAL filas del pie contra las filas reales
    de la tabla.

USO:
  python scripts/loop/verificar_cabecera_mapeo.py
  python scripts/loop/verificar_cabecera_mapeo.py --tabla RUTA

PRUEBA DE MUTACION (obligatoria): scripts/loop/vuelta134_2f_mutacion.py
(vieja, cinco peldanos, se queda commiteada) y
scripts/loop/vuelta135_4c_mutacion.py (nueva, seis peldanos), salida a
docs/loop/SALIDA_V135_4C_MUTACION.txt.
"""
import argparse
import io
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
RUTA_TABLA = os.path.join(RAIZ, "docs", "plan", "OP_S_11_MAPEO_PROPUESTO.md")

# EL ARBOL CONTRA EL QUE SE RECOMPUTA, FIJADO (reparacion 1.a de la vuelta 137,
# parada del 29 ago 2026 punto 1). La cabecera de OP_S_11_MAPEO_PROPUESTO.md
# describe el censo del corte en que se CALCULO, y ese corte es el commit que
# escribio la tabla: 2deac539 (vuelta 135, TAREA 4.b+4.c). Despues, la escritura
# de OP-S-11 (9e909a05, vuelta 136) canonizo el campo `fuente` de 726 nodos
# vivos, o sea que el censo VIVO de hoy trae 54 grafias ya canonicas, cada una
# su grupo de una, y el recomputo contra el arbol vivo devuelve [54]*6: ROJO
# PERMANENTE sobre una tabla que NO esta mal.
#   Ni la tabla ni la guarda estaban mal: cada una es correcta para SU corte, y
# lo cubre banco 9.10 ("lo que envejecio fue la nota, no el fichero sellado").
# Lo que faltaba era decir contra QUE corte recomputa esta guarda. Medido en la
# vuelta 137: dataset/nodos es IDENTICO entre 2deac539 y 9e909a05^ (git diff
# --stat vacio), asi que el sello de la tabla y el estado previo a la escritura
# son el mismo censo.
SELLO_APERTURA = "2deac539e17e7df0471df27c89c183857867e842"

ETIQUETAS = {
    111: "cadena entera",
    108: "mas titulo",
    106: "mas localizador con la cola VIEJA",
    105: "mas Apendice en la cola",
    104: "mas prefijo sobre recortada con Apendice",
    54: "mas abreviatura Caps?. en la cola y en el prefijo",
}


def leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


# vuelta135_tabla_mapeo_propuesto.py REGENERA ENTERO
# docs/plan/OP_S_11_MAPEO_PROPUESTO.md (su DESTINO declarado), que es
# precisamente el fichero que esta guarda tiene que LEER tal como esta en
# el arbol. Se toma una foto de bytes ANTES de cada corrida y se restaura
# DESPUES (no con git checkout, que perderia una edicion todavia sin
# commitear): asi esta guarda nunca ensucia nada con solo ejecutarse.
# REPARACION 1.a DE LA VUELTA 137 (parada del 29 ago 2026, punto 2): el script
# que se invoca escribe DOS ficheros, no uno. El segundo,
# docs/loop/SALIDA_V135_4B_PELDANOS.txt, no estaba en esta lista y por eso cada
# corrida de esta guarda lo ensuciaba (medido en la vuelta 136 y otra vez en la
# apertura de la 137: 8 lineas insertadas / 8 borradas, con los peldanos
# historicos 111/108/106/105/104 sobreescritos por 54).
FICHEROS_CON_EFECTO_SECUNDARIO = [
    RUTA_TABLA,
    os.path.join(RAIZ, "docs", "loop", "SALIDA_V135_4B_PELDANOS.txt"),
]


def _foto_sellados():
    foto = {}
    for ruta in FICHEROS_CON_EFECTO_SECUNDARIO:
        if os.path.exists(ruta):
            with io.open(ruta, "rb") as f:
                foto[ruta] = f.read()
    return foto


def _restaurar_sellados(foto):
    for ruta, contenido in foto.items():
        with io.open(ruta, "wb") as f:
            f.write(contenido)


def correr(script, *args, **kw):
    entorno = kw.pop("entorno", None)
    foto = _foto_sellados()
    env = dict(os.environ)
    if entorno:
        env.update(entorno)
    r = subprocess.run([sys.executable, os.path.join(LOOP_SCRIPTS, script)] + list(args),
                        capture_output=True, text=True, cwd=RAIZ, env=env)
    _restaurar_sellados(foto)
    return r.stdout + "\n" + r.stderr


def extraer_nodos_sellados(sello, destino):
    """Saca dataset/nodos del arbol SELLADO `sello` a `destino` sin tocar el
    arbol de trabajo (git archive a un tar en memoria, no un checkout). Devuelve
    la ruta del directorio de nodos extraido."""
    r = subprocess.run(["git", "archive", "--format=tar", sello, "dataset/nodos"],
                       capture_output=True, cwd=RAIZ)
    if r.returncode != 0:
        raise SystemExit("no se pudo extraer dataset/nodos del sello %s: %s" %
                         (sello, r.stderr.decode("utf-8", "replace")))
    with tarfile.open(fileobj=io.BytesIO(r.stdout)) as tf:
        try:
            tf.extractall(destino, filter="data")
        except TypeError:  # python anterior al filtro de extraccion
            tf.extractall(destino)
    return os.path.join(destino, "dataset", "nodos")


def recomputar(sello=SELLO_APERTURA):
    """Recomputa los seis peldanos contra el arbol FIJADO `sello`, no contra el
    arbol vivo. Con sello=None recomputa contra el arbol vivo (el comportamiento
    viejo, que se conserva para poder EXHIBIR la caida: es lo que hace
    --arbol-vivo)."""
    if sello is None:
        out = correr("vuelta135_tabla_mapeo_propuesto.py")
    else:
        tmp = tempfile.mkdtemp(prefix="sello_mapeo_")
        try:
            nodos = extraer_nodos_sellados(sello, tmp)
            out = correr("vuelta135_tabla_mapeo_propuesto.py",
                         entorno={"MAPEO_NODOS_DIR": nodos})
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    n_cadena = int(re.search(r"peldano 1 \(cadena entera\): (\d+)", out).group(1))
    n_titulo = int(re.search(r"peldano 2 \(\+ titulo\): (\d+)", out).group(1))
    n_localizador_vieja = int(re.search(r"peldano 3 \(\+ localizador cola VIEJA\): (\d+)", out).group(1))
    n_apendice = int(re.search(r"peldano 4 \(\+ Apendice\): (\d+)", out).group(1))
    n_prefijo_apendice = int(re.search(r"peldano 5 \(\+ prefijo sobre recortada con Apendice\): (\d+)", out).group(1))
    n_cap = int(re.search(r"peldano 6 \(\+ Caps\?\. en cola y en prefijo\): (\d+)", out).group(1))

    total_grupos = int(re.search(r"grupos totales \(6 peldanos\): (\d+)", out).group(1))
    dos_mas = int(re.search(r"grupos con 2\+ miembros: (\d+)", out).group(1))
    sin_agrupar = int(re.search(r"^sin agrupar: (\d+)", out, re.MULTILINE).group(1))
    en_grupo = int(re.search(r"^en grupo: (\d+)", out, re.MULTILINE).group(1))
    sinteticas = int(re.search(r"canonicas SINTETICAS: (\d+)", out).group(1))
    colapsos = int(re.search(r"colapsos que faltan para 55: (\d+)", out).group(1))
    grafias = int(re.search(r"^grafias: (\d+)", out, re.MULTILINE).group(1))
    rebase = max(0, 55 - total_grupos)

    return {
        "peldanos": [n_cadena, n_titulo, n_localizador_vieja, n_apendice, n_prefijo_apendice, n_cap],
        "total_grupos": total_grupos,
        "dos_mas": dos_mas,
        "en_grupo": en_grupo,
        "sin_agrupar": sin_agrupar,
        "sinteticas": sinteticas,
        "colapsos": colapsos,
        "rebase": rebase,
        "grafias": grafias,
    }


def cabecera_de(ruta_tabla):
    texto = leer(ruta_tabla)
    m = re.search(r"\n\|\s*grafia\s*\|", texto)
    return texto[:m.start()] if m else texto


def contar_filas_tabla(ruta_tabla):
    texto = leer(ruta_tabla)
    lineas = texto.split("\n")
    en_tabla = False
    filas = 0
    for l in lineas:
        if re.match(r"^\|\s*grafia\s*\|", l):
            en_tabla = True
            continue
        if not en_tabla:
            continue
        if re.match(r"^\|-+\|", l) or re.match(r"^\|\s*-+", l):
            continue
        if l.strip().startswith("|"):
            filas += 1
        elif l.strip() == "":
            continue
        else:
            break
    return filas


def leer_declarado(ruta_tabla):
    cab = cabecera_de(ruta_tabla)
    peldanos = [int(x) for x in re.findall(r"\*\*(\d+) grupos\*\*", cab)]

    m_total = re.search(
        r"CON LA CADENA COMPLETA \(peldano 6\): (\d+) grupos\*\*\s*\((\d+) con 2 o mas miembros / (\d+) en grupo, (\d+) sin agrupar\)",
        cab)
    m_colapsos = re.search(r"Quedan (\d+) colapsos para decision humana", cab)
    m_rebase = re.search(r"la meta de 55 queda REBASADA POR (\d+)", cab)
    m_sinteticas = re.search(r"en este corte: (\d+) canonicas SINTETICAS", cab)
    m_pie = re.search(
        r"TOTAL filas: (\d+) \((\d+) grafias en grupos mecanicos de 2 o mas, (\d+) sin agrupar\), contra (\d+) grafias del censo",
        leer(ruta_tabla))

    return {
        "peldanos": peldanos,
        "total_grupos": int(m_total.group(1)) if m_total else None,
        "dos_mas": int(m_total.group(2)) if m_total else None,
        "en_grupo": int(m_total.group(3)) if m_total else None,
        "sin_agrupar": int(m_total.group(4)) if m_total else None,
        "colapsos": int(m_colapsos.group(1)) if m_colapsos else None,
        "rebase": int(m_rebase.group(1)) if m_rebase else None,
        "sinteticas": int(m_sinteticas.group(1)) if m_sinteticas else None,
        "pie_total_filas": int(m_pie.group(1)) if m_pie else None,
        "pie_en_grupo": int(m_pie.group(2)) if m_pie else None,
        "pie_sin_agrupar": int(m_pie.group(3)) if m_pie else None,
        "pie_censo": int(m_pie.group(4)) if m_pie else None,
    }


def verificar(ruta_tabla, sello=SELLO_APERTURA):
    rec = recomputar(sello)
    dec = leer_declarado(ruta_tabla)
    filas_reales = contar_filas_tabla(ruta_tabla)

    fallos = []

    faltantes = [p for p in rec["peldanos"] if p not in dec["peldanos"]]
    for p in faltantes:
        fallos.append("peldano %d (%s) recomputado pero NO declarado en la cabecera" %
                       (p, ETIQUETAS.get(p, "?")))

    for campo, etiqueta in [
        ("total_grupos", "grupos totales"),
        ("dos_mas", "grupos con 2+ miembros"),
        ("en_grupo", "grafias en grupo"),
        ("sin_agrupar", "grafias sin agrupar"),
        ("colapsos", "colapsos que faltan para 55"),
        ("rebase", "meta de 55 rebasada por"),
        ("sinteticas", "canonicas SINTETICAS"),
    ]:
        if dec[campo] is None:
            fallos.append("cifra de cierre '%s' NO se pudo leer de la cabecera" % etiqueta)
        elif dec[campo] != rec[campo]:
            fallos.append("cifra de cierre '%s': cabecera dice %d, recomputo dice %d" %
                           (etiqueta, dec[campo], rec[campo]))

    if dec["pie_total_filas"] is None:
        fallos.append("pie 'TOTAL filas' NO se pudo leer")
    else:
        if dec["pie_total_filas"] != filas_reales:
            fallos.append("pie 'TOTAL filas' dice %d, la tabla real trae %d filas" %
                           (dec["pie_total_filas"], filas_reales))
        if dec["pie_censo"] != rec["grafias"]:
            fallos.append("pie 'grafias del censo' dice %d, recomputo dice %d" %
                           (dec["pie_censo"], rec["grafias"]))
        if dec["pie_en_grupo"] != rec["en_grupo"]:
            fallos.append("pie 'en grupos mecanicos de 2 o mas' dice %d, recomputo dice %d" %
                           (dec["pie_en_grupo"], rec["en_grupo"]))
        if dec["pie_sin_agrupar"] != rec["sin_agrupar"]:
            fallos.append("pie 'sin agrupar' dice %d, recomputo dice %d" %
                           (dec["pie_sin_agrupar"], rec["sin_agrupar"]))

    return fallos, rec, dec, filas_reales


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tabla", default=RUTA_TABLA)
    ap.add_argument("--sello", default=SELLO_APERTURA,
                    help="commit contra cuyo dataset/nodos se recomputa "
                         "(por defecto el sello de apertura de la tabla)")
    ap.add_argument("--arbol-vivo", action="store_true",
                    help="recomputa contra el arbol de trabajo VIVO en vez del "
                         "sello: sirve para EXHIBIR la caida que la reparacion "
                         "1.a de la vuelta 137 arregla, no para verificar")
    a = ap.parse_args()

    sello = None if a.arbol_vivo else a.sello
    print("recomputando contra: %s" % ("EL ARBOL VIVO" if sello is None else "sello " + sello))

    fallos, rec, dec, filas_reales = verificar(a.tabla, sello)

    if fallos:
        print("ROJO, %d cosa(s) no cuadran en la cabecera de %s:" % (len(fallos), a.tabla))
        for f in fallos:
            print("  %s" % f)
        print("recomputado: peldanos %s, total %d, 2+ %d, en_grupo %d, sin_agrupar %d, "
              "sinteticas %d, colapsos %d, rebase %d, grafias %d, filas reales %d" %
              (rec["peldanos"], rec["total_grupos"], rec["dos_mas"], rec["en_grupo"],
               rec["sin_agrupar"], rec["sinteticas"], rec["colapsos"], rec["rebase"],
               rec["grafias"], filas_reales))
        return 1

    print("VERDE EXIT 0: cabecera de %s cuadra con el recomputo:" % a.tabla)
    print("  peldanos declarados %s == recomputados %s" % (sorted(dec["peldanos"]), sorted(rec["peldanos"])))
    print("  total %d, 2+ %d, en_grupo %d, sin_agrupar %d, sinteticas %d, colapsos %d, rebase %d, "
          "filas reales %d == pie %d" %
          (rec["total_grupos"], rec["dos_mas"], rec["en_grupo"], rec["sin_agrupar"],
           rec["sinteticas"], rec["colapsos"], rec["rebase"], filas_reales, dec["pie_total_filas"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
