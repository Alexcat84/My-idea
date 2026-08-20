# -*- coding: utf-8 -*-
"""vuelta58_tallar_planes.py . SUCESOR DECLARADO de scripts/loop/vuelta57_tallar_planes.py,
al que NO reemplaza. LA ARITMETICA ES LA SUYA, COPIADA ENTERA Y NO RETECLEADA (el
fichero se copio byte a byte y solo despues se le anadio lo de abajo): las formas se
leen del MOTIVO SELLADO, las piezas se cuentan de las marcas del plan, y el
instrumento cae en ROJO con el acto nombrado si un motivo no encaja en ninguna forma
conocida.

POR QUE NACE. La TAREA 1.1 de la vuelta 58 DESHIZO el acto 32 del tramo 4: la
relectura conjunta confirmo el caso del auditor (acta 57, D4) y el acto quedo
DECLARADO por empate sin vara. Las cuatro tablas del registro del tramo 4 en
docs/plan/03_FUSIONES.md salieron del ancestro y ahora publican 44 fusiones donde
hay 43, y una forma (LOS TRES CONTEOS EMPATAN y decide la pieza declarada POR
CANTIDAD) que ya no existe en el tramo. La regla 1 dice que esas tablas se generan
del instrumento y se pegan enteras: para eso hace falta que el instrumento sepa que
un acto SELLADO fue retirado despues.

EL PLAN SELLADO NO SE TOCA, Y ESE ES EL PUNTO. Los PLAN_V57_*.json se quedan como
estan, con el acto 32 dentro y su motivo entero, porque un plan sellado es el
registro de lo que se decidio aquel dia y reescribirlo taparia lo que se corrige.
Lo que este sucesor anade es UN ARGUMENTO, --retirado, que saca al acto de las
tablas de fusion y lo pasa a la de DECLARADOS con su especie y su carril, dejando
constancia impresa de que el motivo sellado sigue ahi.

LO UNICO QUE CAMBIA:
  --retirado N|especie|carril   (repetible) retira el acto N de las tablas 1, 2 y 3
                                y lo anade a la tabla 4 con esa especie y ese carril.
  --vuelta N                    el titulo, que en el ancestro era constante.
Ninguna celda de la aritmetica se toca. Sin --retirado, este fichero imprime
EXACTAMENTE lo mismo que su ancestro, y eso se comprueba corriendo los dos.

DE SOLO LECTURA. No toca ni un nodo ni un plan: imprime.
"""

import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
LOTES = ["A", "B", "C"]

# Las frases de cabecera que el generador de planes escribe al principio de cada
# motivo. El orden importa: se prueba de la mas especifica a la mas general.
# LAS FRASES QUE ESTA VUELTA ANADE van marcadas: son formas que el tramo 4
# estreno y que el tallador de la vuelta 56 no podia reconocer. Ninguna de las
# viejas se toca ni se renombra, para que las dos corridas sigan comparables.
FORMAS = [
    ("LA GUARDA RESTRINGE Y ADEMAS LOS TRES CONTEOS",
     "LA PUERTA SOBREVIVE y los conteos concuerdan, contra la razon declarada"),
    ("LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE",
     "LA PUERTA SOBREVIVE, con el choque registrado"),
    ("LA PIEZA DECLARADA GANA A UN CONTEO",
     "LA PIEZA DECLARADA GANA A UN CONTEO de contenido"),
    ("LOS TRES CONTEOS EMPATAN Y DECIDE LA PIEZA DECLARADA POR CANTIDAD",
     "LOS TRES CONTEOS EMPATAN y decide la pieza declarada POR CANTIDAD"),
    ("LOS CONTEOS EMPATAN Y LA PIEZA DECLARADA DECIDE",
     "LOS CONTEOS EMPATAN y la PIEZA DECLARADA decide"),
    ("TODAS LAS VARAS DE CONTENIDO DE ACUERDO",
     "TODAS LAS VARAS de contenido de acuerdo"),
    ("CONTEOS DE CONTENIDO CONTRA PIEZA DECLARADA",
     "CONTEOS QUE CHOCAN CON LA PIEZA DECLARADA, y decide la declarada"),
    ("CONTENIDO, UNA SOLA VARA NO EMPATADA",
     "UNA SOLA VARA de contenido no empatada, y BASTA"),
    ("CONTENIDO, TODAS LAS VARAS DE ACUERDO",
     "TODAS LAS VARAS de contenido de acuerdo"),
    ("EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO",
     "EL CONTENIDO EMPATA y EL CABLEADO DECIDE SOLO"),
    # LAS FRASES QUE LA VUELTA 59 ANADE, y ninguna de las viejas se toca ni se
    # renombra, para que las corridas sigan comparables. Las cinco nombran
    # formas que YA EXISTEN en la letra vigente; lo que cambia es la frase con
    # la que el generador del tramo 5 las encabeza.
    ("LA GUARDA RESTRINGE Y LA PUERTA SOBREVIVE",
     "LA PUERTA SOBREVIVE, con el choque registrado"),
    ("LA PIEZA DECLARADA GANA A LOS DOS CONTEOS",
     "LA PIEZA DECLARADA GANA A LOS DOS CONTEOS de contenido"),
    ("LAS VARAS DE CONTENIDO CHOCAN Y DECIDE LA PIEZA DECLARADA",
     "CONTEOS QUE CHOCAN CON LA PIEZA DECLARADA, y decide la declarada"),
    ("UNA SOLA VARA DE CONTENIDO NO EMPATADA",
     "UNA SOLA VARA de contenido no empatada, y BASTA"),
    # LAS FRASES QUE LA VUELTA 60 ANADE, con los lotes B y C del tramo 5. Como
    # las de la 59, NINGUNA VIEJA SE TOCA NI SE RENOMBRA. Tres de las cuatro
    # nombran formas que YA EXISTEN en la letra vigente y solo cambian la frase
    # de cabecera; LA CUARTA ES FORMA NUEVA y va dicha: hasta este tramo ninguna
    # fusion se habia decidido por una FIGURA CON NOMBRE del informe en vez de
    # por una vara de las actas, y por eso se le da etiqueta propia en vez de
    # colarla dentro de una existente.
    ("LA PIEZA DECLARADA DECIDE, QUE ES LA VARA ESCRITA PARA CUANDO DOS VARAS DE CONTENIDO CHOCAN",
     "CONTEOS QUE CHOCAN CON LA PIEZA DECLARADA, y decide la declarada"),
    ("LA PIEZA DECLARADA DECIDE, Y ES VARA PORQUE ESTA DE UN SOLO LADO",
     "LOS TRES CONTEOS EMPATAN y decide LA PIEZA DECLARADA, que esta de UN SOLO LADO"),
    ("LA PIEZA DECLARADA DECIDE, Y ES VARA PORQUE LA RAZON LA RECONOCE ASIMETRICA",
     "LOS TRES CONTEOS EMPATAN y decide LA PIEZA DECLARADA, que esta de UN SOLO LADO"),
    ("LAS DOS VIAS ESCRITAS APUNTAN AL MISMO LADO",
     "EL CONTENIDO EMPATA y LA PIEZA DECLARADA Y EL CABLEADO COINCIDEN"),
    ("UNA FIGURA CON NOMBRE VENCE AL CONTEO DE PASOS",
     "UNA FIGURA CON NOMBRE del informe vence al conteo (EL CASO NO ES LA CASA)"),
]


def forma_de(motivo):
    for clave, nombre in FORMAS:
        if motivo.startswith(clave):
            return nombre
    return None


# LA CUENTA DE PERDIDAS, CORREGIDA EN LA VUELTA 60, Y EL TEXTO VIEJO SE QUEDA
# ESCRITO AQUI PORQUE UNA CORRECCION QUE TAPA LO QUE CORRIGE NO SE PUEDE AUDITAR.
# LO QUE HABIA ERA:
#
#     perdidas = act["nota_del_reparto"].count("PERDIDA NOMBRADA")
#
# Y CUENTA DE MAS, medido y no supuesto sobre los lotes B y C del tramo 5: de
# las SEIS apariciones del token, CINCO estan dentro de frases que dicen lo
# CONTRARIO de una perdida, porque anuncian que la perdida que la RAZON nombro
# esta REPUESTA por esta fusion:
#     lote B acto 20  "LA PERDIDA NOMBRADA QUE LA RAZON MARCO NO SE PIERDE ..."
#     lote B acto 28  "LA UNICA PERDIDA NOMBRADA SE REPONE DE APPEND ..."
#     lote B acto 31  "LA UNICA PERDIDA NOMBRADA SE REPONE DE APPEND ..."
#     lote B acto 32  "LA UNICA PERDIDA NOMBRADA SE REPONE DE APPEND ..."
#     lote C acto 36  "LA UNICA PERDIDA NOMBRADA SE REPONE DE INCISO ..."
# La unica de verdad es el acto 19 del lote B, que dice "se NOMBRA en vez de
# reponerse". Sin esta correccion la TABLA 1 del registro del tramo 5 habria
# publicado 5 perdidas en el lote B y 1 en el C, y las dos cifras son falsas.
#
# LA REGLA NUEVA ES TEXTUAL Y COMPROBABLE, no una adivinanza: una aparicion del
# token NO cuenta si en su misma frase (hasta el primer punto) el plan dice que
# la pieza SE REPONE o que NO SE PIERDE. El plan sellado no se toca.
#
# LO QUE ESTA CORRECCION NO ARREGLA, Y VA DICHO EN VEZ DE CALLARSE: sigue
# contando SOLO las perdidas que llevan el token, asi que SIGUE CONTANDO DE
# MENOS las que el plan nombra con otras palabras (un matiz de condicion que se
# declara, una denominacion que el instrumento no puede reponer). Esa segunda
# mitad NO se arregla aqui porque arreglarla a ojo seria inventar; queda
# declarada en el reporte con los actos nombrados.
# SEGUNDA CORRECCION DECLARADA (20 ago 2026, vuelta 62), Y ES JUSTO LA MITAD QUE
# LA PRIMERA DEJO SIN ARREGLAR, escrita cinco renglones mas arriba: "SIGUE
# CONTANDO DE MENOS las que el plan nombra con otras palabras". Ya no hace falta
# adivinar, porque los planes del tramo 6 nacen con el contrato CAMPO PROPIO v1
# y traen la perdida EN UN CAMPO. LA REGLA NUEVA NO ES UNA HEURISTICA:
#
#     si el plan declara "contrato_de_perdidas": "CAMPO PROPIO v1", la cuenta
#     sale del CAMPO perdidas de cada acto, que es una lista y se mide con len().
#     si NO lo declara, se cuenta por TOKEN como hasta ahora, con su aviso.
#
# POR QUE SE CORRIGE HOY, el mismo dia en que este instrumento cuenta las cifras
# de esta vuelta, que es lo que el D7 de la vuelta 60 marco como discutible: sin
# esto la TABLA 1 del registro del tramo 6 publicaria PERDIDAS NOMBRADAS 0
# cuando el campo sella DIECIOCHO, y publicar un cero falso es peor que corregir
# con contraste. EL CONTRASTE ESTA CORRIDO Y CITADO en el reporte: sobre los
# planes del tramo 5, que NO declaran el contrato, esta version da EXACTAMENTE
# las mismas cifras que el registro de aquel tramo publico (A 3, B 1, C 0, los
# tres 4). La aritmetica de piezas no se toca en esta correccion.
NO_ES_PERDIDA = ("SE REPONE", "SE REPONEN", "NO SE PIERDE")
CONTRATO_DE_PERDIDAS = "CAMPO PROPIO v1"


def cuenta_perdidas(nota):
    n = 0
    desde = 0
    while True:
        i = nota.find("PERDIDA NOMBRADA", desde)
        if i < 0:
            return n
        fin = nota.find(".", i)
        frase = nota[i:fin if fin > 0 else len(nota)]
        if not any(x in frase for x in NO_ES_PERDIDA):
            n += 1
        desde = i + 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, required=True)
    ap.add_argument("--prefijo", action="append", default=None,
                    help="prefijo de los planes; REPETIBLE (un tramo puede repartirse "
                         "entre varias vueltas); por defecto PLAN_V<vuelta>_OPU01_LOTE_")
    ap.add_argument("--retirado", action="append", default=[],
                    help="N|especie|carril . acto SELLADO que se retiro despues")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    # LO UNICO QUE ESTE SUCESOR ANADE, primera mitad: los retirados.
    retirados = {}
    for crudo in a.retirado:
        partes = crudo.split("|", 2)
        if len(partes) != 3 or not partes[0].strip().isdigit():
            print("  ROJO: --retirado mal formado (%s). Se espera N|especie|carril."
                  % crudo)
            return 1
        retirados[int(partes[0])] = (partes[1].strip(), partes[2].strip())

    # SEGUNDA COSA QUE ESTE FICHERO ANADE (vuelta 60), y el motivo esta medido:
    # EL TRAMO 5 SE REPARTIO ENTRE DOS VUELTAS. Su lote A lo sello la vuelta 59
    # (PLAN_V59_*) y sus lotes B y C la vuelta 60 (PLAN_V60_*). Con un prefijo
    # unico, el registro del CIERRE del tramo saldria con 31 fusiones en vez de
    # 47 y las cuatro tablas mentirian por omision. --prefijo pasa a ser
    # REPETIBLE y cada lote se busca en el primer prefijo que lo tenga. LA
    # ARITMETICA NO SE TOCA: con un solo prefijo este fichero imprime
    # EXACTAMENTE lo que imprimia, y eso se comprueba corriendo los dos.
    prefijos = a.prefijo or ["PLAN_V%d_OPU01_LOTE_" % a.vuelta]
    RUTA_DE = {}
    for L in LOTES:
        for pref in prefijos:
            cand = os.path.join(LOOP, "%s%s.json" % (pref, L))
            if os.path.exists(cand):
                RUTA_DE[L] = cand
                break
    LOTES_HALLADOS = [L for L in LOTES if L in RUTA_DE]
    if not LOTES_HALLADOS:
        print("ROJO: no hay ningun plan con prefijo %s. PARADA." % ", ".join(prefijos))
        return 1
    # EL NUMERO DE TRAMO SALE DEL PLAN Y NO DE UNA CONSTANTE (TAREA 1.1)
    _pr = json.load(io.open(RUTA_DE[LOTES_HALLADOS[0]], encoding="utf-8"))
    _m = re.match(r"\s*(\d+)", str(_pr.get("tramo", "")))
    num_tramo = _m.group(1) if _m else "SIN NUMERO EN EL CAMPO tramo DEL PLAN"

    print("=" * 78)
    print("LAS TABLAS DEL TRAMO %s, TALLADAS DE LOS PLANES SELLADOS (vuelta %d)"
          % (num_tramo, a.vuelta))
    print("  lotes hallados: %s" % ", ".join(
        "%s (%s)" % (L, os.path.basename(RUTA_DE[L])) for L in LOTES_HALLADOS))
    if retirados:
        print("ACTOS RETIRADOS DESPUES DEL SELLADO: %s"
              % ", ".join(str(n) for n in sorted(retirados)))
        print("El plan sellado NO se toca: el motivo del acto sigue entero en su fichero.")
    print("=" * 78)
    print()

    todos = []
    rojo = []
    sacados = []
    for L in LOTES_HALLADOS:
        p = RUTA_DE[L]
        plan = json.load(io.open(p, encoding="utf-8"))
        for act in plan["actos"]:
            if act["orden"] in retirados:
                esp, carril = retirados[act["orden"]]
                sacados.append({"orden": act["orden"], "lote": L,
                                "miembros": act["miembros_del_acto_entero"],
                                "especie": esp, "acumula_para": carril,
                                "forma_sellada": forma_de(act["motivo"])})
                continue
            c = {"APPEND": 0, "CUBIERTO": 0, "INCISO": 0}
            for d in (act["pasos"], act["condiciones"]):
                for marcas in d.values():
                    for m in marcas.values():
                        k = ("APPEND" if m == "APPEND"
                             else "INCISO" if m.startswith("INCISO") else "CUBIERTO")
                        c[k] += 1
            f = forma_de(act["motivo"])
            if f is None:
                rojo.append((L, act["orden"]))
            if plan.get("contrato_de_perdidas") == CONTRATO_DE_PERDIDAS:
                perdidas = len(act.get("perdidas") or [])
            else:
                perdidas = cuenta_perdidas(act["nota_del_reparto"])
            todos.append({"lote": L, "orden": act["orden"],
                          "sup": act["superviviente"], "abs": act["absorbidos"][0],
                          "forma": f, "piezas": sum(c.values()),
                          "append": c["APPEND"], "cubierto": c["CUBIERTO"],
                          "inciso": c["INCISO"], "perdidas": perdidas})

    if rojo:
        print("  ROJO: motivos cuya forma no se reconoce: %s" % rojo)
        return 1

    # CORRECCION DECLARADA (20 ago 2026, vuelta 62): estas dos lineas tallaban
    # "LOS TRES" a mano y el tramo 6 tiene DOS lotes, asi que la tabla habria
    # publicado un rotulo falso. EL TEXTO VIEJO SE QUEDA ESCRITO: decia
    #     print("--- TABLA 1: LOS TRES LOTES, CON SUS PIEZAS ---")
    #     print("| **los tres** | ...
    # Ahora la cuenta sale de los lotes HALLADOS. No toca ninguna cifra.
    print("--- TABLA 1: LOS %d LOTES, CON SUS PIEZAS ---" % len(LOTES_HALLADOS))
    print()
    print("| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas nombradas |")
    print("|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for L in LOTES_HALLADOS:
        f = [x for x in todos if x["lote"] == L]
        print("| **%s** | %s | **%d** | **%d** | **%d** | %d | %d | **%d** | **%d** |"
              % (L, ", ".join(str(x["orden"]) for x in f), len(f), len(f),
                 sum(x["piezas"] for x in f), sum(x["append"] for x in f),
                 sum(x["cubierto"] for x in f), sum(x["inciso"] for x in f),
                 sum(x["perdidas"] for x in f)))
    print("| **los %d** | | **%d** | **%d** | **%d** | **%d** | **%d** | **%d** | **%d** |"
          % (len(LOTES_HALLADOS), len(todos), len(todos),
             sum(x["piezas"] for x in todos),
             sum(x["append"] for x in todos), sum(x["cubierto"] for x in todos),
             sum(x["inciso"] for x in todos), sum(x["perdidas"] for x in todos)))
    print()

    print("--- TABLA 2: LA FORMA DEL VEREDICTO, CONTADA DE LOS MOTIVOS SELLADOS ---")
    print()
    cuenta = {}
    for x in todos:
        cuenta.setdefault(x["forma"], []).append(x["orden"])
    print("| la forma, leida del motivo sellado | cuantos | los actos |")
    print("|---|---:|---|")
    for f in sorted(cuenta, key=lambda k: (-len(cuenta[k]), k)):
        print("| **%s** | **%d** | %s |"
              % (f, len(cuenta[f]), ", ".join(str(n) for n in sorted(cuenta[f]))))
    print("| **suma** | **%d** | |" % sum(len(v) for v in cuenta.values()))
    print()

    print("--- TABLA 3: ACTO A ACTO, SUPERVIVIENTE Y ABSORBIDO ---")
    print()
    print("| acto | lote | sobrevive | absorbe | piezas | enteras | ya dichas | `INCISO` |")
    print("|---:|:---:|---|---|---:|---:|---:|---:|")
    for x in sorted(todos, key=lambda x: x["orden"]):
        print("| **%d** | %s | `%s` | `%s` | %d | %d | %d | %d |"
              % (x["orden"], x["lote"], x["sup"], x["abs"], x["piezas"],
                 x["append"], x["cubierto"], x["inciso"]))
    print()
    print("--- TABLA 4: LOS ACTOS DECLARADOS Y NO FUNDIDOS ---")
    print()
    print("| acto | lote | sus miembros | especie | se acumula para |")
    print("|---:|:---:|---|---|---|")
    # LO UNICO QUE ESTE SUCESOR ANADE, segunda mitad: los retirados entran aqui,
    # en su sitio por orden, junto a los que ya nacieron declarados.
    filas = []
    for L in LOTES_HALLADOS:
        p = RUTA_DE[L]
        plan = json.load(io.open(p, encoding="utf-8"))
        for d in plan.get("declarados_y_no_fundidos", []):
            filas.append((d["orden"], L, d["miembros"], d["especie"],
                          d["acumula_para"]))
    for s in sacados:
        filas.append((s["orden"], s["lote"], s["miembros"], s["especie"],
                      s["acumula_para"]))
    for orden, L, miembros, especie, carril in sorted(filas):
        print("| **%d** | %s | %s | **%s** | %s |"
              % (orden, L, ", ".join("`%s`" % m for m in miembros), especie, carril))
    print("| **suma** | | **%d declarados** | | |" % len(filas))
    print()
    if sacados:
        print("--- TABLA 5: LOS RETIRADOS DESPUES DEL SELLADO, CON SU FORMA VIEJA ---")
        print()
        print("| acto | lote | la forma que el motivo SELLADO le dio | donde queda ahora |")
        print("|---:|:---:|---|---|")
        for s in sorted(sacados, key=lambda x: x["orden"]):
            print("| **%d** | %s | %s | **%s** |"
                  % (s["orden"], s["lote"], s["forma_sellada"], s["especie"]))
        print()
    print("  actos tallados: %d | piezas: %d | perdidas nombradas: %d | retirados: %d"
          % (len(todos), sum(x["piezas"] for x in todos),
             sum(x["perdidas"] for x in todos), len(sacados)))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
