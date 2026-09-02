# -*- coding: utf-8 -*-
r"""vuelta142_2a_nomina_unidades.py . LA NOMINA DE UNIDADES DE UN REPORTE,
MEDIDA Y NO TECLEADA (TAREA 2.a.i de la vuelta 142, acta de la vuelta 141,
caida 4.5 del auditor).

POR QUE NACE. `verificar_cifras_del_reporte.py` sale VERDE EXIT 0 cotejando
CERO cifras porque su `UNIDADES` es un vocabulario cerrado (fichero, par,
grupo, grafia, colapso, nodo, linea, arista) y el reporte publica sus cifras en
DIRECCIONES, filas y comprobaciones. El encargo prohibe expresamente teclear la
ampliacion de memoria: "NO las teclees de memoria: sacalas midiendo el
REPORTE.md de la vuelta 141 y el de esta, y publica la nomina de unidades vistas
que NO estan en el vocabulario".

QUE MIDE. Sobre el fichero que se le pase (y con el MISMO partido de frases y el
MISMO recorte de bloques cubiertos que usa la guarda, importados de ella para
que no midan cosas distintas), busca toda pareja `<numero> <palabra>` y agrupa
por palabra, diciendo de cada una si esta DENTRO o FUERA del vocabulario de la
guarda EN EL MOMENTO DE CORRER.

Por que el patron es mas ancho que el de la guarda: la guarda solo ve las
palabras de su propio `UNIDADES`; este instrumento tiene que ver TODAS para
poder decir cuales le faltan. Se filtran los numeros con separador de miles o
decimal solo cuando no son enteros, igual que la guarda.

QUE NO ES: no adjudica que una palabra DEBA entrar al vocabulario. Mide que se
usa como unidad y con que frecuencia; quien decide es el encargo.

USO:
  python scripts/loop/vuelta142_2a_nomina_unidades.py docs/loop/REPORTE.md
  python scripts/loop/vuelta142_2a_nomina_unidades.py A.md B.md
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_cifras_del_reporte as V

# EL PATRON ANCHO Y LA NOMINA DE RUIDO SE IMPORTAN DE LA GUARDA, no se copian:
# la guarda los usa para publicar su nomina en cada corrida y este instrumento
# para medirla aparte, y dos copias de la misma pregunta se desincronizarian el
# dia que una crezca. La guarda es la fuente; aqui solo se lee.
PATRON_NUMERO_PALABRA = V.PATRON_NUMERO_PALABRA
RUIDO = V.RUIDO


def medir(ruta):
    texto = V.quitar_bloques_cubiertos(V.leer(ruta))
    frases = V.dividir_frases(texto)
    vistas = {}
    for i, frase in enumerate(frases):
        for m in PATRON_NUMERO_PALABRA.finditer(frase):
            numero_txt = m.group(1).replace(".", "").replace(",", "")
            if not numero_txt.isdigit():
                continue
            palabra = m.group(2).lower()
            vistas.setdefault(palabra, []).append((i, int(numero_txt), frase.strip()))
    return vistas


def main():
    rutas = sys.argv[1:]
    if not rutas:
        print("USO: vuelta142_2a_nomina_unidades.py <reporte.md> [<reporte.md> ...]")
        return 2
    sys.stdout.reconfigure(encoding="utf-8")

    vocabulario = set(u.lower() for u in V.UNIDADES)
    print("=" * 78)
    print("NOMINA DE UNIDADES MEDIDA SOBRE %d FICHERO(S)" % len(rutas))
    print("Vocabulario de verificar_cifras_del_reporte.py EN EL MOMENTO DE CORRER")
    print("(%d palabra(s)): %s" % (len(vocabulario), ", ".join(sorted(vocabulario))))
    print("=" * 78)

    global_dentro, global_fuera, global_ruido = {}, {}, {}
    for ruta in rutas:
        if not os.path.exists(ruta):
            print("")
            print("ROJO (arnes): no existe %s" % ruta)
            return 1
        vistas = medir(ruta)
        print("")
        print("--- %s ---" % ruta)
        dentro = {p: v for p, v in vistas.items() if p in vocabulario}
        ruido = {p: v for p, v in vistas.items() if p not in vocabulario and p in RUIDO}
        fuera = {p: v for p, v in vistas.items() if p not in vocabulario and p not in RUIDO}
        print("   cifras con unidad DENTRO del vocabulario: %d en %d palabra(s)"
              % (sum(len(v) for v in dentro.values()), len(dentro)))
        for p in sorted(dentro, key=lambda x: (-len(dentro[x]), x)):
            print("      %-16s %d vez(ces)" % (p, len(dentro[p])))
        print("   cifras con unidad FUERA del vocabulario: %d en %d palabra(s)"
              % (sum(len(v) for v in fuera.values()), len(fuera)))
        for p in sorted(fuera, key=lambda x: (-len(fuera[x]), x)):
            print("      %-16s %d vez(ces)   p.ej. linea %d: %.90s"
                  % (p, len(fuera[p]), fuera[p][0][0], fuera[p][0][2]))
        print("   descartadas por la nomina de RUIDO declarada: %d en %d palabra(s): %s"
              % (sum(len(v) for v in ruido.values()), len(ruido),
                 ", ".join(sorted(ruido)) or "ninguna"))
        for d, acc in ((dentro, global_dentro), (fuera, global_fuera), (ruido, global_ruido)):
            for p, v in d.items():
                acc.setdefault(p, []).extend(v)

    print("")
    print("=" * 78)
    print("NOMINA UNIDA DE LOS %d FICHERO(S)" % len(rutas))
    print("CIFRA dentro del vocabulario: %d cifras" % sum(len(v) for v in global_dentro.values()))
    print("CIFRA fuera del vocabulario: %d cifras" % sum(len(v) for v in global_fuera.values()))
    print("PALABRAS FUERA DEL VOCABULARIO (%d), por frecuencia:" % len(global_fuera))
    for p in sorted(global_fuera, key=lambda x: (-len(global_fuera[x]), x)):
        print("   %-18s %d" % (p, len(global_fuera[p])))
    print("PALABRAS DENTRO DEL VOCABULARIO (%d), por frecuencia:" % len(global_dentro))
    for p in sorted(global_dentro, key=lambda x: (-len(global_dentro[x]), x)):
        print("   %-18s %d" % (p, len(global_dentro[p])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
