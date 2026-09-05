# -*- coding: utf-8 -*-
r"""vuelta169_tarea3_op_i_01.py . `OP-I-01` CLAUSULA 4, CON EL ALCANCE QUE LA
ADJUDICACION 6.4 DEL ACTA 168 LE PUSO (TAREA 3 de la vuelta 169).

LA CLAUSULA, VERBATIM DE LA FICHA: *"el inventario se recomputa entero con el
disparador de 08_VERIFICACION"*. Y EL DISPARADOR ESTA ESCRITO Y ES CITABLE:
`docs/plan/08_VERIFICACION.md:379` y siguientes, cuatro pasos en orden, y su
PASO 4 dice literal *"LAS NOMINAS Y LOS ACTOS: cada racimo y cada acto se re-mide
con su cobertura al lado (banco 9.26), usando las componentes del paso 3"*.

DE AHI SALE EL ALCANCE, Y NO SE INVENTA NADA:
  DENTRO del disparador, y por tanto EJECUTABLE: las entradas de tipo `acto` y
  `racimo` de `docs/plan/INVENTARIO.jsonl`, re medidas sobre las componentes del
  paso 3 y con su cobertura al lado, CON EL RESOLUTOR DELANTE por `P.1`.
  FUERA del disparador, que NO las nombra: `familia_de_ids`, `figura`, `defecto`
  y `dominio`. NO se recomputan y NO se inventan: SE DECLARAN con su cifra de hoy
  y con la frase de que el disparador no las alcanza.

LAS CIFRAS DE COMPONENTES SALEN DE CONTAR EL FICHERO SELLADO, NO DE REGENERARLO
(encargo de la vuelta 169, TAREA 3, ultimo parrafo). Este instrumento hace las
DOS cosas y las mantiene separadas: cuenta `RECOMPUTO_3388_COMPONENTES.jsonl` (la
nomina sellada, que es la que manda) y ADEMAS corre `scripts/plan/recomputo_3388.py`
a una salida propia de esta vuelta para poder decir si el instrumento reproduce
hoy lo que el fichero sellado guarda. Si discrepan, LA DISCREPANCIA SE DECLARA.

POR QUE NO SE PISA LA NOMINA SELLADA: `recomputo_3388.py` exige `--salida` sin
default desde la vuelta 48 (canon 9 del banco) justamente para que una corrida
desnuda no la pise en silencio. Aqui la salida va a `docs/loop/RECOMPUTO_V169.jsonl`.

USO:
  python scripts/loop/vuelta169_tarea3_op_i_01.py
"""
import collections
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INVENTARIO = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
COMPONENTES = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388_COMPONENTES.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
# LA SALIDA DEL RECOMPUTO ES CONFIGURABLE, Y SE DICE POR QUE. Su sitio de la casa
# es `docs/loop/RECOMPUTO_V169.jsonl` (asi lo hizo la vuelta 166 con el suyo), pero
# la bateria de mutaciones vigila `docs/loop/` y reporta como RUIDO DE
# CONCURRENCIA todo fichero que aparezca ahi mientras corre. Cuando este
# instrumento se corre EN PARALELO con la bateria, su salida va fuera y se mueve
# a su sitio despues. El destino final NO cambia: cambia donde se escribe mientras
# hay otra guarda mirando el directorio.
SALIDA_V169 = os.environ.get(
    "V169_RECOMPUTO_SALIDA",
    os.path.join(RAIZ, "docs", "loop", "RECOMPUTO_V169.jsonl"))
DISPARADOR = os.path.join(RAIZ, "docs", "plan", "08_VERIFICACION.md")

# LOS TIPOS QUE EL PASO 4 DEL DISPARADOR NOMBRA, LEIDOS DE SU FRASE Y NO TECLEADOS
# A OJO: la frase es "cada racimo y cada acto". Se guarda aqui la frase entera para
# que la guarda de abajo compruebe que sigue diciendo eso y no otra cosa.
FRASE_PASO_4 = ("LAS NOMINAS Y LOS ACTOS")
DENTRO = ("acto", "racimo")


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 169, TAREA 3: OP-I-01 CLAUSULA 4, CON SU ALCANCE ADJUDICADO")
    print("=" * 78)
    print("")

    print("A) EL DISPARADOR SE LEE DE SU SEDE ANTES DE APLICARLO, Y SI NO ESTA, PARA")
    texto_disp = io.open(DISPARADOR, encoding="utf-8").read()
    lineas_disp = texto_disp.split("\n")
    n_paso4 = [i for i, l in enumerate(lineas_disp, 1) if FRASE_PASO_4 in l]
    print("   sede: docs/plan/08_VERIFICACION.md")
    print("   la frase %r aparece en la(s) linea(s): %s" % (FRASE_PASO_4, n_paso4))
    if len(n_paso4) != 1:
        print("   ROJO: el paso 4 del disparador no se localiza sin ambiguedad.")
        return 1
    print("   texto del paso 4, leido hoy:")
    print("      %s" % lineas_disp[n_paso4[0] - 1].strip())
    for palabra in ("racimo", "acto", "cobertura", "9.26", "paso 3"):
        print("      contiene %-10s: %s" % (palabra, palabra in lineas_disp[n_paso4[0] - 1]))
    print("")

    print("B) EL INVENTARIO, CONTADO POR TIPO, Y EL ALCANCE PARTIDO EN DOS")
    inv = cargar(INVENTARIO)
    por_tipo = collections.Counter(x.get("tipo") for x in inv)
    dentro = [x for x in inv if x.get("tipo") in DENTRO]
    fuera = [x for x in inv if x.get("tipo") not in DENTRO]
    print("   CIFRA entradas del inventario: %d" % len(inv))
    print("   | tipo | entradas | dentro del disparador |")
    print("   |---|---:|---|")
    for t, n in por_tipo.most_common():
        print("   | `%s` | %d | %s |" % (t, n, "SI" if t in DENTRO else "NO"))
    print("   CIFRA DENTRO del disparador (acto mas racimo): %d de %d"
          % (len(dentro), len(inv)))
    print("   CIFRA FUERA del disparador: %d de %d" % (len(fuera), len(inv)))
    print("")

    print("C) LAS VIGENTES CONTRA LAS SUPERADAS, POR fecha_corte")
    cortes = collections.Counter((x["tipo"], x.get("fecha_corte")) for x in dentro)
    for (t, c), n in sorted(cortes.items()):
        print("   %-8s corte %s -> %d" % (t, c, n))
    corte_nuevo = max(c for (_t, c) in cortes)
    # QUE ES VIGENTE, Y SE CORRIGE AQUI PORQUE LA PRIMERA CORRIDA DE ESTE
    # INSTRUMENTO LO TENIA MAL. La primera version partia por `fecha_corte`, y eso
    # dejaba fuera ONCE racimos del corte 2026-08-11 QUE NO ESTAN SUPERADOS: la
    # marca SUPERADA la llevan los 221 actos viejos, uno a uno, y NINGUN racimo.
    # Partir por la fecha en vez de por la marca daba 337 vigentes donde hay 348,
    # y once nominas se habrian quedado sin re-medir sin que nadie lo notara.
    # Cazado midiendo antes de publicar. LA VARA ES LA MARCA, NO LA FECHA.
    def superada(e):
        return "SUPERADA" in ((e.get("estado") or "") + (e.get("nota") or ""))
    vigentes = [x for x in dentro if not superada(x)]
    superadas = [x for x in dentro if superada(x)]
    print("   corte mas reciente, computado y no tecleado: %s" % corte_nuevo)
    print("   LA VARA DE VIGENCIA ES LA MARCA `SUPERADA`, NO LA `fecha_corte`.")
    print("   CIFRA entradas VIGENTES (sin marca SUPERADA): %d" % len(vigentes))
    print("   CIFRA entradas marcadas SUPERADA (no se borran, no se re-miden): %d"
          % len(superadas))
    rep_vig = collections.Counter(x["tipo"] for x in vigentes)
    rep_sup = collections.Counter(x["tipo"] for x in superadas)
    print("   reparto de las vigentes: %s" % dict(sorted(rep_vig.items())))
    print("   reparto de las superadas: %s" % dict(sorted(rep_sup.items())))
    fechas_vig = collections.Counter(x.get("fecha_corte") for x in vigentes)
    print("   y las vigentes NO son todas del corte nuevo: %s"
          % dict(sorted(fechas_vig.items())))
    print("")

    print("D) EL FICHERO SELLADO DE COMPONENTES, CONTADO Y NO REGENERADO")
    comps = cargar(COMPONENTES)
    est = collections.Counter(c.get("estado") for c in comps)
    print("   fichero: docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl")
    print("   CIFRA lineas del fichero: %d" % len(comps))
    for k, v in sorted(est.items()):
        print("   CIFRA %-9s: %d" % (k, v))
    print("")

    print("E) EL INSTRUMENTO SE CORRE HOY, A SALIDA PROPIA, Y SE COTEJA")
    r = subprocess.run(
        [sys.executable, os.path.join("scripts", "plan", "recomputo_3388.py"),
         "--salida", os.path.relpath(SALIDA_V169, RAIZ).replace(os.sep, "/")],
        cwd=RAIZ, capture_output=True)
    salida = (r.stdout.decode("utf-8", "replace")
              + r.stderr.decode("utf-8", "replace")).replace("\r\n", "\n")
    print("   exit de scripts/plan/recomputo_3388.py: %d" % r.returncode)
    if r.returncode != 0:
        print("   ROJO: el recomputo no corrio. Primeras lineas de su salida:")
        for l in salida.split("\n")[:20]:
            print("      " + l)
        return 1
    hoy = cargar(SALIDA_V169)
    est_hoy = collections.Counter(c.get("estado") for c in hoy)
    print("   CIFRA lineas de la corrida de HOY: %d" % len(hoy))
    for k, v in sorted(est_hoy.items()):
        print("   CIFRA %-9s de HOY: %d" % (k, v))
    iguales = (len(hoy) == len(comps) and est_hoy == est)
    print("   la corrida de hoy REPRODUCE el fichero sellado en linea y estado: %s"
          % iguales)
    if not iguales:
        print("   DISCREPANCIA DECLARADA, no resuelta copiando:")
        print("      sellado: %d lineas, %s" % (len(comps), dict(sorted(est.items()))))
        print("      hoy    : %d lineas, %s" % (len(hoy), dict(sorted(est_hoy.items()))))
    for linea in salida.split("\n"):
        if re.match(r"^(A crudas|de esas,|PARES DISTINTOS|de esos,)", linea):
            print("   paso 1: %s" % linea.strip())
    print("")

    print("F) (3.a) CADA ACTO Y CADA RACIMO VIGENTE, RE MEDIDO SOBRE LAS COMPONENTES")
    print("   DEL PASO 3, CON SU COBERTURA AL LADO Y EL RESOLUTOR DELANTE (P.1)")
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x, visto=None):
        visto = visto or set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    idx = {}
    for c in comps:
        idx[frozenset(res(m) for m in c["miembros"])] = c

    calzan, no_calzan, sin_componente = [], [], []
    for e in vigentes:
        clave = frozenset(res(m) for m in e["miembros"])
        c = idx.get(clave)
        if c is None:
            sin_componente.append(e)
            continue
        cob_hoy = "%d de %d pares leidos; %d en cola; %d fuera de cola" % (
            c["leidos"], c["posibles"], c["en_cola_sin_leer"], c["fuera_de_cola"])
        # LA COMPARACION ES DE CIFRAS, NO DE CADENA, Y SE DICE POR QUE. Las
        # entradas de tipo `racimo` escriben su cobertura como "N de M" y las de
        # tipo `acto` como "N de M pares leidos; X en cola; Y fuera de cola".
        # Comparar al caracter entre los dos formatos daba DOCE diferencias de las
        # que NUEVE eran solo de formato: la cifra era la misma. Lo que el banco
        # 9.26 pide es "cuantos pares leidos de cuantos posibles", asi que eso es
        # lo que se compara, y el calce al caracter se publica APARTE.
        m = re.search(r"(\d+) de (\d+)", e.get("cobertura", "") or "")
        cifras_ficha = (int(m.group(1)), int(m.group(2))) if m else None
        cifras_hoy = (c["leidos"], c["posibles"])
        if cifras_ficha == cifras_hoy:
            calzan.append(e)
        else:
            no_calzan.append((e, cob_hoy))
    print("   CIFRA entradas vigentes re medidas: %d" % len(vigentes))
    print("   CIFRA cuyas CIFRAS de cobertura calzan con su componente de hoy: %d" % len(calzan))
    print("   CIFRA cuyas CIFRAS de cobertura DIFIEREN de las de hoy: %d" % len(no_calzan))
    print("   CIFRA sin componente en el fichero sellado: %d" % len(sin_componente))
    for e, cob_hoy in no_calzan[:40]:
        print("      DIFIERE %s" % e["nombre"])
        print("         ficha: %s" % e.get("cobertura"))
        print("         hoy  : %s" % cob_hoy)
    if len(no_calzan) > 40:
        print("      ... y %d mas" % (len(no_calzan) - 40))
    for e in sin_componente[:40]:
        print("      SIN COMPONENTE: %s (tamano %d)" % (e["nombre"], len(e["miembros"])))
    if len(sin_componente) > 40:
        print("      ... y %d mas" % (len(sin_componente) - 40))
    print("")

    print("G) (3.b) LO QUE EL DISPARADOR NO ALCANZA: SE DECLARA CON SU CIFRA DE HOY")
    print("   El paso 4 del disparador nombra 'cada racimo y cada acto' y NADA MAS.")
    print("   Estas entradas NO se recomputan y NO se inventan:")
    print("   | tipo | entradas hoy |")
    print("   |---|---:|")
    for t, n in sorted(((t, n) for t, n in por_tipo.items() if t not in DENTRO),
                       key=lambda x: -x[1]):
        print("   | `%s` | %d |" % (t, n))
    print("   CIFRA total FUERA del disparador: %d de %d" % (len(fuera), len(inv)))
    print("")

    print("H) (3.c) LA DISCREPANCIA DE LA NOTA DE LA FICHA, MEDIDA Y NO RESUELTA AQUI")
    actos_vig = [x for x in vigentes if x["tipo"] == "acto"]
    print("   la nota de OP-I-01 declara: 335 actos (280 CERRADOS, 55 ABIERTOS)")
    print("   CIFRA entradas de tipo acto vigentes (sin marca SUPERADA) hoy: %d" % len(actos_vig))
    print("   CIFRA lineas del fichero de componentes hoy: %d" % len(comps))
    for k in sorted(est):
        print("   CIFRA componentes %-9s hoy: %d" % (k, est[k]))
    print("   LA CIFRA VIEJA NO SE BORRA Y LA NUEVA NO SE COPIA ENCIMA:")
    print("      la correccion entra por el carril del banco 9.10 en el instrumento")
    print("      scripts/loop/vuelta169_tarea3_corregir_ficha.py, con la cifra vieja")
    print("      tachada y entera y el contador cuadrado en el mismo acto.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
