# -*- coding: utf-8 -*-
"""comprobar_promesas_de_marcado.py . COMPRUEBA QUE TODO LO QUE UN PLAN SELLADO
PROMETE MARCAR EN EL REPORTE ESTA EFECTIVAMENTE EN LA SECCION 6 DEL REPORTE.

NOMBRE ESTABLE, y no lleva vuelta: los planes y el reporte entran por argumento.

POR QUE NACE. La caida de reporte de la vuelta 62 (acta 62, seccion 3, linea
16100): SEIS motivos sellados prometian VA MARCADO COMO DISCUTIBLE y la seccion 6
del reporte no traia ninguno. La regla que salio de ahi es la regla 2 del
protocolo del ejecutor leida entera: LO QUE UN MOTIVO SELLADO PROMETA DEL
REPORTE, EL REPORTE LO CUMPLE; y si al consolidar se decide que un discutible del
plan no llega a la seccion 6, EL REPORTE LO DICE CON SU MOTIVO EN VEZ DE
CALLARLO. UNA REGLA QUE SOLO VIVE EN LA ATENCION FALLA: esto la vuelve mecanica.

Es el sucesor de nombre estable de scripts/loop/_v63_sitios_promesa.py, que hacia
lo mismo sobre DOS planes y UN reporte concretos y ya nombrados dentro.

LA VARA, escrita para que se pueda discutir. Cuenta como PROMESA la frase VA
MARCADO COMO DISCUTIBLE (comparada sin distinguir mayusculas) dentro de los
campos motivo o nota_del_reparto de un acto. La palabra discutible suelta NO es
promesa: describir una razon como discutible es una lectura, prometer que va
marcado es un compromiso sobre otro fichero. Cuenta como CUMPLIDA si la seccion 6
del reporte nombra el acto por su orden o por el id de alguno de sus miembros.

CORRECCION DECLARADA (2026-08-20, vuelta 65, TAREA 1.b del encargo, por el carril
del banco 9.10 y por el de la correccion de instrumento estable; EL TEXTO VIEJO
SE QUEDA ENTERO ARRIBA Y NO SE TACHA, que es lo que hace auditable la
correccion). El parrafo de LA VARA de aqui arriba dice, verbatim: "Cuenta como
PROMESA la frase VA MARCADO COMO DISCUTIBLE (comparada sin distinguir
mayusculas)". LA AGUJA ERA SOLO SINGULAR Y AHORA TAMBIEN ES PLURAL: se anade la
forma VAN MARCADAS COMO DISCUTIBLES a la singular, SIN QUITAR NADA. Un campo que
traiga CUALQUIERA de las dos formas, o las dos, cuenta como UNA sola promesa, que
es lo que deja el conteo viejo intacto.

POR QUE SE ENSANCHA, y es una averia MEDIDA y no un capricho: la vuelta 64 sello
en PLAN_V64_OPM03II.json una nota que decia LAS DOS VAN MARCADAS COMO
DISCUTIBLES, en plural, y el propio ejecutor tuvo que escribir la forma singular
DENTRO de la nota para que este instrumento la viera. Lo adjudico el acta 64,
pregunta 6 (linea 16947): UNA PROMESA INVISIBLE ES PEOR QUE UNA INCUMPLIDA
PORQUE NO SALE EN ROJO.

LO QUE SE MIDIO ANTES DE ENSANCHAR, porque el acta mandaba PARAR si aparecia una
promesa INCUMPLIDA hoy invisible: barridos los 62 PLAN_*.json de docs/loop, la
forma plural aparece en UNO solo (PLAN_V64_OPM03II.json, acto 1,
nota_del_reparto) y ESE MISMO campo ya trae la singular. CERO promesas nuevas y
CERO incumplidas destapadas: el ensanche no es regresion ni hallazgo, es aguja.

DE SOLO LECTURA ENTERO.

Uso:
  python scripts/loop/comprobar_promesas_de_marcado.py --reporte docs/loop/REPORTE.md
      --plan docs/loop/PLAN_V63_OPM03I.json --plan docs/loop/PLAN_V63_OPM02PROG.json
exit 0 si todas las promesas estan cumplidas; exit 1 si alguna no lo esta.
"""
import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROMESA = "va marcado como discutible"
# ENSANCHE DE LA VUELTA 65 (acta 64, pregunta 6): la forma PLURAL se ANADE a la
# singular y no la sustituye. La constante vieja se queda con su nombre y su
# valor intactos, y las dos entran juntas en FORMAS.
PROMESA_PLURAL = "van marcadas como discutibles"
FORMAS = (PROMESA, PROMESA_PLURAL)
NL = chr(10)


def seccion6(texto):
    m = re.search(r"^## 6\..*?(?=^## 7\.)", texto, re.S | re.M)
    return m.group(0) if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reporte", required=True)
    ap.add_argument("--plan", action="append", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    rep = io.open(os.path.join(RAIZ, a.reporte.replace("/", os.sep)), encoding="utf-8").read()
    s6 = seccion6(rep)
    print("=" * 78)
    print("LAS PROMESAS DE MARCADO, COMPROBADAS CONTRA LA SECCION 6 DEL REPORTE")
    print("  reporte  : %s (cabecera: %s)" % (a.reporte, rep.split(NL)[0]))
    print("  seccion 6 leida: %d caracteres" % len(s6))
    print("  planes   : %d" % len(a.plan))
    print("  agujas   : %d, y se imprimen para que la vara no dependa del docstring:"
          % len(FORMAS))
    for f in FORMAS:
        print("     %s" % f.upper())
    print("=" * 78)
    if not s6:
        print()
        print("ROJO: el reporte no trae una seccion 6 legible. PARADA.")
        return 1

    filas = []
    for p in a.plan:
        d = json.load(io.open(os.path.join(RAIZ, p.replace("/", os.sep)), encoding="utf-8"))
        for acto in d["actos"]:
            for campo in ("motivo", "nota_del_reparto"):
                t = acto.get(campo) or ""
                bajo = t.lower()
                # UN campo con CUALQUIERA de las dos formas, o con las dos, es
                # UNA sola promesa: se toma la que aparece ANTES para recortar
                # la frase, y se declaran todas las formas halladas.
                presentes = [f for f in FORMAS if f in bajo]
                if not presentes:
                    continue
                i = min(bajo.index(f) for f in presentes)
                ini = bajo.rfind(".", 0, i) + 1
                fin = bajo.find(".", i)
                frase = t[ini:fin + 1 if fin > 0 else len(t)].strip()
                agujas = ["acto %d" % acto["orden"]] + list(acto["miembros"])
                halladas = [x for x in agujas if x.lower() in s6.lower()]
                filas.append((os.path.basename(p), acto["orden"], campo, frase,
                              halladas, agujas, presentes))

    print()
    if not filas:
        print("  NINGUN PLAN DE LOS PASADOS PROMETE MARCADO, y esa ausencia se publica.")
        print()
        print("FIN")
        return 0

    incumplidas = []
    for fichero, orden, campo, frase, halladas, agujas, presentes in filas:
        ok = bool(halladas)
        if not ok:
            incumplidas.append((fichero, orden, campo))
        print("  %-32s acto %-3d campo %-16s %s"
              % (fichero, orden, campo, "CUMPLIDA" if ok else "INCUMPLIDA"))
        print("     forma hallada: %s"
              % ", ".join("SINGULAR" if f == PROMESA else "PLURAL" for f in presentes))
        print("     promete: %s" % frase[:150])
        print("     hallado en la seccion 6 por: %s"
              % (", ".join(halladas) if halladas else
                 "NADA de: %s" % ", ".join(agujas)))
    print()
    print("  promesas medidas     : %d" % len(filas))
    print("  promesas CUMPLIDAS   : %d" % (len(filas) - len(incumplidas)))
    print("  promesas INCUMPLIDAS : %d" % len(incumplidas))
    print()
    if incumplidas:
        print("ROJO: la regla 2 leida entera dice que lo que un motivo sellado prometa del")
        print("reporte, el reporte lo cumple; y si no llega a la seccion 6, EL REPORTE LO DICE")
        print("CON SU MOTIVO. Estas no estan ni cumplidas ni explicadas:")
        for f, o, c in incumplidas:
            print("   %s acto %d campo %s" % (f, o, c))
        return 1
    print("VERDE: TODAS LAS PROMESAS DE MARCADO ESTAN CUMPLIDAS.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
