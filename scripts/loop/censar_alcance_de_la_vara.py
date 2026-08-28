# -*- coding: utf-8 -*-
r"""censar_alcance_de_la_vara.py . EL TECHO DE CADA VARA, MEDIDO ANTES DE
CORRERLA (TAREA 4 de la vuelta 111, encargo del auditor, acta de la vuelta
110, seccion 1.1 "LA VARA DE TECHO DOS").

Nombre estable, SIN numero de vuelta (como tallar_cabecera_reporte.py y
contar_cierre_efectivo.py): no se clona cada vuelta.

POR QUE NACE. La TAREA 5 de la vuelta 110 encargo una vara que solo podia
morder en DOS pares de setenta y cuatro (de las 74 RESUELTA vivas, 72 eran
OBJETO y solo 87 y 109 eran SATELITE: el techo de hallazgos de esa vara era
DOS, y nadie lo dijo antes de correrla). La cosecha 0 de esa vara fue
CORRECTA, pero no probo salud: probo que la vara apuntaba donde casi no
habia nada que ver. Este instrumento publica, de un vistazo y contado de
las fuentes reales, la distribucion completa del expediente, para que
CUALQUIER vara futura pueda citar su techo ANTES de correrse.

QUE MIDE. Cruza dos fuentes:
  - `contar_cierre_efectivo.py` sobre los cuatro tramos de OP-E-03 (RESUELTA
    vs NO RESUELTA, con correccion_vNN aplicada).
  - los seis ficheros de `FICHEROS_VEREDICTO` (reusados de
    `verificar_cobertura_bolsa_tres_vias.py`), que dan el veredicto de la
    pregunta de tres vias (OBJETO / SATELITE / NO_OBJETO) puesto por puesto,
    el MAS NUEVO si un puesto aparece en mas de un fichero (mismo orden que
    `verificar_vuelco_de_veredicto.py`, que fija `apariciones[-1]` como el
    veredicto de HOY). CORREGIDO en la vuelta 112 (acta de la vuelta 111,
    4.1 "CAIDA DE EXPEDIENTE"): esta cabecera decia lo CONTRARIO de lo que
    el codigo siempre hizo. El codigo esta y estaba bien: tomar el MAS VIEJO
    da 70 OBJETO / 4 SATELITE, y ese fue el error de la PRIMERA VERSION de
    este censo (ver `veredicto_de_hoy_por_puesto` mas abajo); tomar el MAS
    NUEVO da 72 / 2, que es lo unico que calza con la cifra publicada.

Publica, por cada uno de los dos grupos (RESUELTA, NO RESUELTA): n del
grupo, y cuantos traen OBJETO, SATELITE, NO_OBJETO o SIN VEREDICTO. Los
grupos con 10 o menos miembros dentro de una celda traen la NOMINA
completa (para que "5 SATELITE" no se quede sin nombres, como paso con la
TAREA 3 de esta misma vuelta).

USO:
  python scripts/loop/censar_alcance_de_la_vara.py

CIFRA DE CONTROL DE LA VUELTA 111 (declarada por el auditor, 4.2 del
encargo, PARA CONTRASTAR, no para copiar): 183 en total; 74 RESUELTA con 72
OBJETO y 2 SATELITE (87 y 109); 109 NO RESUELTA con 104 SIN VEREDICTO y 5
SATELITE (20, 21, 38, 66, 93).

LA REGLA QUE NACE CON EL (4.3 del encargo): desde esta vuelta, toda vara que
se encargue sobre este expediente declara SU TECHO antes de correrse -- o
sea, sobre cuantos pares podria mover el veredicto si TODOS fallaran. Una
vara que sale con cosecha 0 sin decir su techo no ha demostrado salud: puede
que solo estuviera apuntando donde no habia nada.
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import contar_cierre_efectivo as cce  # noqa: E402
import verificar_cobertura_bolsa_tres_vias as vcb  # noqa: E402

TOPE_NOMINA = 10


def veredicto_de_hoy_por_puesto(ficheros):
    """veredicto[puesto] = (PALABRA, nombre_del_fichero), leido de la
    ULTIMA aparicion de ese puesto recorriendo FICHEROS_VEREDICTO EN SU
    ORDEN DECLARADO (105, 106, 107, 107, 108, 108): es el mismo orden
    cronologico que usa verificar_vuelco_de_veredicto.py para fijar
    `apariciones[-1]` como el veredicto de HOY quer un puesto que vuelca
    entre dos ficheros distintos (91, 109, 123, 145). Tomar la PRIMERA
    aparicion en vez de la ultima fue el error de la primera version de
    este censo (vuelta 111): daba 70 OBJETO / 4 SATELITE en vez de 72/2,
    porque leia el veredicto VIEJO de los cuatro puestos que ya volcaron."""
    veredicto = {}
    for nombre, formato in ficheros:
        ruta = os.path.join(LOOP, nombre)
        if not os.path.exists(ruta):
            continue
        texto = io.open(ruta, encoding="utf-8").read()
        if formato == "bloque":
            hallados = {}
            puesto_actual = None
            for linea in texto.splitlines():
                m = vcb.RE_BLOQUE_CABECERA.match(linea)
                if m:
                    puesto_actual = int(m.group(1))
                    continue
                if linea.strip() == "":
                    puesto_actual = None
                    continue
                if puesto_actual is not None:
                    vm = vcb.RE_BLOQUE_VEREDICTO.search(linea)
                    if vm:
                        hallados[puesto_actual] = vm.group(1)
                        puesto_actual = None
        elif formato == "tabla":
            hallados = {}
            for linea in texto.splitlines():
                m = vcb.RE_TABLA_FILA.match(linea)
                if m:
                    hallados[int(m.group(1))] = m.group(2)
        else:
            continue
        for puesto, palabra in hallados.items():
            veredicto[puesto] = (palabra, nombre)
    return veredicto


def censar():
    d, fallos = cce.cifras(cce.TRAMOS_OP_E_03_POR_DEFECTO)
    if fallos:
        return None, fallos
    no_resuelta = set(d["sin_dir"])
    todos = set(range(1, d["n"] + 1))
    resuelta = todos - no_resuelta

    ficheros = list(vcb.FICHEROS_VEREDICTO)
    veredicto = veredicto_de_hoy_por_puesto(ficheros)

    grupos = {"RESUELTA": sorted(resuelta), "NO RESUELTA": sorted(no_resuelta)}
    resultado = {}
    for etiqueta, puestos in grupos.items():
        celdas = {"OBJETO": [], "SATELITE": [], "NO_OBJETO": [], "SIN VEREDICTO": []}
        for p in puestos:
            v = veredicto.get(p)
            if v is None:
                celdas["SIN VEREDICTO"].append(p)
            else:
                celdas[v[0]].append(p)
        resultado[etiqueta] = {"n": len(puestos), "celdas": celdas}
    return resultado, []


def main():
    resultado, fallos = censar()
    if fallos:
        print("ROJO:", fallos)
        return 1

    print("FICHEROS DE ENTRADA (FICHEROS_VEREDICTO, %d):" % len(vcb.FICHEROS_VEREDICTO))
    for nombre, formato in vcb.FICHEROS_VEREDICTO:
        print("   %s (%s)" % (nombre, formato))
    print()

    n_total = sum(g["n"] for g in resultado.values())
    print("n TOTAL: %d" % n_total)
    for etiqueta in ("RESUELTA", "NO RESUELTA"):
        g = resultado[etiqueta]
        print("\n%s: n=%d" % (etiqueta, g["n"]))
        for celda in ("OBJETO", "SATELITE", "NO_OBJETO", "SIN VEREDICTO"):
            miembros = g["celdas"][celda]
            if len(miembros) <= TOPE_NOMINA:
                print("   %s: %d -- %s" % (celda, len(miembros), miembros))
            else:
                print("   %s: %d" % (celda, len(miembros)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
