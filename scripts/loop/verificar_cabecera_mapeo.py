# -*- coding: utf-8 -*-
"""verificar_cabecera_mapeo.py . TAREA 2.f de la vuelta 134 (acta 133, 4.7:
la guarda que faltaba y que esta vuelta tiene caso, el peldano 106 que
desaparecio de la cabecera de docs/plan/OP_S_11_MAPEO_PROPUESTO.md).

CONTRATO:
  - Recomputa desde dataset/ los CINCO peldanos de la cadena (cadena entera;
    mas titulo; mas localizador con la cola VIEJA; mas Apendice en la cola;
    mas prefijo sobre recortada), REUSANDO los scripts existentes
    (vuelta131_grupos_por_titulo.py, vuelta133_cola_localizador_apendice.py,
    vuelta133_prefijo_sobre_recortada.py, vuelta133_tabla_mapeo_propuesto.py
    para las cifras de cierre), sin reimplementar su union-find.
  - Lee la cabecera de docs/plan/OP_S_11_MAPEO_PROPUESTO.md (todo el texto
    antes de la fila `| grafia | canonica propuesta | ...`), extrae CADA
    cifra `**N grupos**` que declara (multiconjunto, sin importar el orden
    en que aparezcan en la prosa: la reposicion del 106 puede llegar por
    ADICION al final del parrafo, no necesariamente en su posicion logica)
    y coteja contra el recomputo. Si la cabecera declara MENOS peldanos de
    los que el recomputo produce, ES ROJO EXIT 1 nombrando el peldano que
    falta (numero y etiqueta).
  - Coteja tambien las cifras de cierre de la cabecera (grupos totales,
    grupos de 2+, grafias en grupo, sin agrupar, colapsos que faltan,
    canonicas SINTETICAS) y el TOTAL filas del pie contra las filas reales
    de la tabla.

USO:
  python scripts/loop/verificar_cabecera_mapeo.py
  python scripts/loop/verificar_cabecera_mapeo.py --tabla RUTA

PRUEBA DE MUTACION (obligatoria): scripts/loop/vuelta134_2f_mutacion.py,
salida a docs/loop/SALIDA_V134_2F_MUTACION.txt.
"""
import argparse
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
RUTA_TABLA = os.path.join(RAIZ, "docs", "plan", "OP_S_11_MAPEO_PROPUESTO.md")

ETIQUETAS = {
    111: "cadena entera",
    108: "mas titulo",
    106: "mas localizador con la cola VIEJA",
    105: "mas Apendice en la cola",
    104: "mas prefijo sobre recortada",
}


def leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


# Estos scripts viejos, reusados aqui SOLO por su stdout, tienen efectos
# secundarios de escritura: vuelta133_cola_localizador_apendice.py y
# vuelta133_prefijo_sobre_recortada.py pisan su propio SALIDA_V133_*.txt
# sellado, y vuelta133_tabla_mapeo_propuesto.py REGENERA ENTERO
# docs/plan/OP_S_11_MAPEO_PROPUESTO.md (su DESTINO declarado), que es
# precisamente el fichero que esta guarda tiene que LEER tal como esta en
# el arbol, con la edicion de la 3.c puesta y no regenerada desde cero. Se
# toma una foto de bytes ANTES de cada corrida y se restaura DESPUES (no con
# git checkout, que perderia una edicion todavia sin commitear): asi esta
# guarda nunca ensucia nada con solo ejecutarse, este o no comiteado.
FICHEROS_CON_EFECTO_SECUNDARIO = [
    os.path.join(RAIZ, "docs", "loop", "SALIDA_V133_4A_COLA_CON_APENDICE.txt"),
    os.path.join(RAIZ, "docs", "loop", "SALIDA_V133_4B_PREFIJO_APLICADO.txt"),
    RUTA_TABLA,
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


def correr(script, *args):
    foto = _foto_sellados()
    r = subprocess.run([sys.executable, os.path.join(LOOP_SCRIPTS, script)] + list(args),
                        capture_output=True, text=True, cwd=RAIZ)
    _restaurar_sellados(foto)
    return r.stdout + "\n" + r.stderr


def recomputar():
    out1 = correr("vuelta131_grupos_por_titulo.py")
    cadena_entera = int(re.search(r"grupos base \(cadena entera, vuelta 130\): (\d+)", out1).group(1))
    titulo = int(re.search(r"grupos tras anadir regla de titulo: (\d+)", out1).group(1))

    out2 = correr("vuelta133_cola_localizador_apendice.py")
    localizador_vieja = int(re.search(r"grupos cola vieja \(solo Anexo\): (\d+)", out2).group(1))
    apendice = int(re.search(r"grupos cola extendida \(mas Apendice\): (\d+)", out2).group(1))

    out3 = correr("vuelta133_prefijo_sobre_recortada.py")
    prefijo = int(re.search(r"grupos tras prefijo sobre recortada: (\d+)", out3).group(1))

    out4 = correr("vuelta133_tabla_mapeo_propuesto.py")
    dos_mas = int(re.search(r"grupos con 2\+ miembros: (\d+)", out4).group(1))
    en_grupo = int(re.search(r"^en grupo: (\d+)", out4, re.MULTILINE).group(1))
    sin_agrupar = int(re.search(r"^sin agrupar: (\d+)", out4, re.MULTILINE).group(1))
    sinteticas = int(re.search(r"canonicas SINTETICAS: (\d+)", out4).group(1))
    colapsos = int(re.search(r"colapsos que faltan para 55: (\d+)", out4).group(1))
    total_grupos = int(re.search(r"grupos totales \(4 reglas\): (\d+)", out4).group(1))
    grafias = int(re.search(r"^grafias: (\d+)", out4, re.MULTILINE).group(1))

    return {
        "peldanos": [cadena_entera, titulo, localizador_vieja, apendice, prefijo],
        "total_grupos": total_grupos,
        "dos_mas": dos_mas,
        "en_grupo": en_grupo,
        "sin_agrupar": sin_agrupar,
        "sinteticas": sinteticas,
        "colapsos": colapsos,
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
        r"CON LAS CUATRO REGLAS MECANICAS: (\d+) grupos\*\*\s*\((\d+) con 2 o mas miembros / (\d+) en grupo, (\d+) sin agrupar\)",
        cab)
    m_colapsos = re.search(r"Quedan (\d+) colapsos para decision humana", cab)
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
        "sinteticas": int(m_sinteticas.group(1)) if m_sinteticas else None,
        "pie_total_filas": int(m_pie.group(1)) if m_pie else None,
        "pie_en_grupo": int(m_pie.group(2)) if m_pie else None,
        "pie_sin_agrupar": int(m_pie.group(3)) if m_pie else None,
        "pie_censo": int(m_pie.group(4)) if m_pie else None,
    }


def verificar(ruta_tabla):
    rec = recomputar()
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
    a = ap.parse_args()

    fallos, rec, dec, filas_reales = verificar(a.tabla)

    if fallos:
        print("ROJO, %d cosa(s) no cuadran en la cabecera de %s:" % (len(fallos), a.tabla))
        for f in fallos:
            print("  %s" % f)
        print("recomputado: peldanos %s, total %d, 2+ %d, en_grupo %d, sin_agrupar %d, "
              "sinteticas %d, colapsos %d, grafias %d, filas reales %d" %
              (rec["peldanos"], rec["total_grupos"], rec["dos_mas"], rec["en_grupo"],
               rec["sin_agrupar"], rec["sinteticas"], rec["colapsos"], rec["grafias"], filas_reales))
        return 1

    print("VERDE EXIT 0: cabecera de %s cuadra con el recomputo:" % a.tabla)
    print("  peldanos declarados %s == recomputados %s" % (sorted(dec["peldanos"]), sorted(rec["peldanos"])))
    print("  total %d, 2+ %d, en_grupo %d, sin_agrupar %d, sinteticas %d, colapsos %d, "
          "filas reales %d == pie %d" %
          (rec["total_grupos"], rec["dos_mas"], rec["en_grupo"], rec["sin_agrupar"],
           rec["sinteticas"], rec["colapsos"], filas_reales, dec["pie_total_filas"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
