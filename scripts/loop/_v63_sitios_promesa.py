# -*- coding: utf-8 -*-
"""_v63_sitios_promesa.py . MIDE LOS SITIOS DE LA PROMESA DE MARCADO DE LA
VUELTA 62 Y LOS COTEJA CONTRA LA SECCION 6 DEL REPORTE QUE LOS PROMETIA.

POR QUE EXISTE. El acta 62 (seccion 2, linea 16085, y seccion 3, linea 16100)
declara una CAIDA DE REPORTE: seis motivos sellados prometen VA MARCADO COMO
DISCUTIBLE y la seccion 6 del reporte no trae ninguno de los seis. El encargo de
la vuelta 63 manda registrar esa caida CON SUS SEIS SITIOS, y la regla 1 del
ejecutor dice que una tabla cuyo contenido vive en un plan sellado SE GENERA
desde el plan y no se teclea. Esto es ese generador.

EL PREFIJO _ ES EL DE LA CASA para los ficheros de una vuelta concreta. Lleva el
numero de vuelta en el nombre a proposito: mide DOS planes concretos contra UN
reporte concreto, y no pretende ser el instrumento estable de nada.

ES DE SOLO LECTURA. No escribe un nodo, ni un plan, ni el reporte.

LA VARA DE LA PROMESA, escrita para que se pueda discutir: cuenta como PROMESA la
frase VA MARCADO COMO DISCUTIBLE (comparada sin distinguir mayusculas) dentro del
campo motivo o nota_del_reparto de un acto del plan. La palabra discutible suelta
NO es promesa: describir una razon como discutible es una lectura, prometer que va
marcado es un compromiso sobre otro fichero. Los dos casos se imprimen por separado
para que la vara se vea.

LA VARA DEL CUMPLIMIENTO: el acto esta cumplido si la seccion 6 del reporte lo
nombra, sea por su numero de acto o por el id de alguno de sus dos miembros.

Uso:
  python scripts/loop/_v63_sitios_promesa.py
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLANES = ("docs/loop/PLAN_V62_OPU01_LOTE_A.json", "docs/loop/PLAN_V62_OPU01_LOTE_B.json")
REPORTE = "docs/loop/REPORTE.md"
PROMESA = "va marcado como discutible"


def seccion6(texto):
    m = re.search(r"^## 6\..*?(?=^## 7\.)", texto, re.S | re.M)
    return m.group(0) if m else ""


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    rep = io.open(os.path.join(RAIZ, REPORTE.replace("/", os.sep)), encoding="utf-8").read()
    s6 = seccion6(rep)
    print("=" * 78)
    print("LOS SITIOS DE LA PROMESA DE MARCADO DE LA VUELTA 62, MEDIDOS")
    print("  planes  : %s" % ", ".join(PLANES))
    print("  reporte : %s (cabecera: %s)" % (REPORTE, rep.split(chr(10))[0]))
    print("  seccion 6 leida: %d caracteres" % len(s6))
    print("=" * 78)
    print()
    promesas, sueltos = [], []
    for p in PLANES:
        d = json.load(io.open(os.path.join(RAIZ, p.replace("/", os.sep)), encoding="utf-8"))
        for a in d["actos"]:
            for campo in ("motivo", "nota_del_reparto"):
                t = a.get(campo) or ""
                bajo = t.lower()
                if PROMESA in bajo:
                    i = bajo.index(PROMESA)
                    ini = bajo.rfind(".", 0, i) + 1
                    fin = bajo.find(".", i)
                    frase = t[ini:fin + 1 if fin > 0 else len(t)].strip()
                    promesas.append((os.path.basename(p), a["orden"], campo,
                                     a["miembros"], frase))
                elif "discutible" in bajo:
                    sueltos.append((os.path.basename(p), a["orden"], campo))
    print("A) LOS SITIOS QUE PROMETEN (frase %r):" % PROMESA.upper())
    print()
    print("%-6s %-6s %-18s %-9s %-9s %s" % ("acto", "lote", "campo", "dice EN", "cumplida", "por donde se busco en la seccion 6"))
    print("%-6s %-6s %-18s %-9s %-9s %s" % ("", "", "", "EL REPORTE", "", ""))
    print("-" * 110)
    incumplidas = []
    for fichero, orden, campo, miembros, frase in promesas:
        lote = fichero.split("_LOTE_")[1][0]
        dice = "SI" if re.search(r"en el reporte", frase, re.I) else "NO"
        agujas = ["acto %d" % orden, "acto **%d**" % orden] + list(miembros)
        halladas = [x for x in agujas if x.lower() in s6.lower()]
        cumplida = "SI" if halladas else "NO"
        if not halladas:
            incumplidas.append(orden)
        print("%-6d %-6s %-18s %-9s %-9s %s"
              % (orden, lote, campo, dice, cumplida,
                 ", ".join(halladas) if halladas else "ninguna de: %s" % ", ".join(agujas)))
    print()
    print("  promesas medidas      : %d" % len(promesas))
    print("  promesas CUMPLIDAS    : %d" % (len(promesas) - len(incumplidas)))
    print("  promesas INCUMPLIDAS  : %d, en los actos %s"
          % (len(incumplidas), ", ".join(str(x) for x in sorted(incumplidas))))
    print()
    print("B) EL OTRO LADO DE LA VARA, para que se vea que la vara separa: sitios que")
    print("   solo usan la palabra discutible SIN prometer marcado, y que NO cuentan:")
    for fichero, orden, campo in sueltos:
        print("     %-38s acto %-3d campo %s" % (fichero, orden, campo))
    print("   son %d, y ninguno entra en la cuenta de arriba." % len(sueltos))
    print()
    print("C) LA FRASE ENTERA DE CADA PROMESA, para que el registro no dependa de esta tabla:")
    for fichero, orden, campo, miembros, frase in promesas:
        print()
        print("   acto %-3d (%s, campo %s)" % (orden, fichero, campo))
        print("      %s" % frase)
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
