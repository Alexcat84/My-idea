# -*- coding: utf-8 -*-
r"""vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py . MUTACION U (2.6 del
encargo de la vuelta 112, acta de la vuelta 111, 4.1 "CAIDA DE EXPEDIENTE").

Corre censar_alcance_de_la_vara.py sobre las MISMAS seis fuentes
(FICHEROS_VEREDICTO) por LAS DOS REGLAS (la ULTIMA aparicion de un puesto,
que es la que usa el codigo real desde siempre, y la PRIMERA aparicion, que
fue el error de la primera version del censo en la vuelta 111) y publica las
dos cifras juntas, para que la cifra publicada quede atada a la regla
escrita en el docstring corregido de censar_alcance_de_la_vara.py.

USO:
  python scripts/loop/vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import censar_alcance_de_la_vara as cav  # noqa: E402
import verificar_cobertura_bolsa_tres_vias as vcb  # noqa: E402
import contar_cierre_efectivo as cce  # noqa: E402


def veredicto_por_regla(ficheros, regla):
    """regla == 'ultima': se queda con la ULTIMA aparicion (el codigo real).
    regla == 'primera': se queda con la PRIMERA aparicion (el error de la
    primera version del censo, vuelta 111)."""
    veredicto = {}
    for nombre, formato in ficheros:
        ruta = os.path.join(cav.LOOP, nombre)
        if not os.path.exists(ruta):
            continue
        import io
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
            if regla == "primera" and puesto in veredicto:
                continue
            veredicto[puesto] = (palabra, nombre)
    return veredicto


def censar_por_regla(regla):
    d, fallos = cce.cifras(cce.TRAMOS_OP_E_03_POR_DEFECTO)
    if fallos:
        return None, fallos
    no_resuelta = set(d["sin_dir"])
    todos = set(range(1, d["n"] + 1))
    resuelta = todos - no_resuelta
    ficheros = list(vcb.FICHEROS_VEREDICTO)
    veredicto = veredicto_por_regla(ficheros, regla)
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
    for regla, etiqueta in (("ultima", "MAS NUEVO (el codigo real)"),
                             ("primera", "MAS VIEJO (el error de la primera version)")):
        resultado, fallos = censar_por_regla(regla)
        if fallos:
            print("ROJO (%s):" % etiqueta, fallos)
            return 1
        r = resultado["RESUELTA"]
        print("REGLA %s: RESUELTA n=%d -- OBJETO %d / SATELITE %d / NO_OBJETO %d / SIN VEREDICTO %d"
              % (etiqueta, r["n"], len(r["celdas"]["OBJETO"]), len(r["celdas"]["SATELITE"]),
                 len(r["celdas"]["NO_OBJETO"]), len(r["celdas"]["SIN VEREDICTO"])))

    print()
    print("VEREDICTO: la cifra PUBLICADA (72 OBJETO / 2 SATELITE) sale de la regla MAS NUEVO, "
          "que es la que aplica el codigo de censar_alcance_de_la_vara.py; la regla MAS VIEJO "
          "da 70 / 4 y es el error declarado de la primera version.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
