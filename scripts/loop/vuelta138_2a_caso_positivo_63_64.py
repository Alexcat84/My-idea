# -*- coding: utf-8 -*-
"""vuelta138_2a_caso_positivo_63_64.py . EL CASO POSITIVO DE LA OPERACION 2.a.

GUARDA (i) DEL ENCARGO DE LA VUELTA 138: "EL FORMATO VIEJO SIGUE VALIENDO para
las de un solo absorbido, y eso no se promete, se PRUEBA: regenera los tres
planes de las vueltas 63 y 64 y compara byte a byte contra
docs/loop/PLAN_V63_OPM02PROG.json, PLAN_V63_OPM03I.json y PLAN_V64_OPM03II.json.
IDENTICOS."

POR QUE NO SE PUEDE REGENERAR CONTRA EL ARBOL DE HOY, medido y no supuesto: los
tres absorbidos (fases_de_retencion_de_clientes, decision_pivote_perseverar y
pivotar_o_proceder) estan HOY DEPRECADOS, porque las tres fusiones se ejecutaron
en las vueltas 63 y 64. El generador cae en ROJO con "el nodo X YA esta
deprecado", que es lo correcto. Regenerar contra el arbol de hoy no probaria
nada: probaria que el generador se niega a fundir un muerto.

CONTRA QUE SE REGENERA, ENTONCES: contra el arbol EN EL QUE cada plan se sello,
que es el PADRE del commit que anadio el plan (git log --diff-filter=A). En el
commit que lo anade el nodo YA esta deprecado, porque el plan y la ejecucion
viajaron en el mismo commit; en su padre sigue vivo. Los tres se comprueban aqui
con git show sobre las tres refs antes de comparar nada, y la comprobacion se
imprime.

COMO: git worktree add --detach sobre el padre, se copian DENTRO los cinco
ficheros de A_COPIAR (el codigo de hoy y los tres contenidos editoriales, que en
el padre todavia no existen), y se corre alli. P.16, QUIEN FABRICA LIMPIA: el
worktree se retira siempre, aun si el caso cae.

LA VARA ES EL BLOB DEL SELLADO, NO EL FICHERO DE HOY, y esto NO es una comodidad:
es un hallazgo medido de esta vuelta. git log sobre los tres planes dice que DOS
de ellos se EDITARON DESPUES de nacer: PLAN_V63_OPM02PROG.json en be69bc56 (vuelta
64, "EL D10 SE SELLA Y LAS CINCO CONSUMIDAS QUEDAN CORREGIDAS") y
PLAN_V64_OPM03II.json en ca74f202 (reporte de la vuelta 64); PLAN_V63_OPM03I.json
no se toco nunca. Comparar el regenerado contra el fichero DE HOY mediria esas
ediciones posteriores y no el generador, que es lo que se quiere probar. Asi que
la comparacion principal va contra el blob del commit del sellado, los bytes que
el generador escribio; y la deriva del fichero de hoy contra su sellado se MIDE Y
SE IMPRIME aparte, con los commits que la introdujeron, en vez de callarse.

LA UNICA DIFERENCIA TOLERADA, declarada y no escondida: el campo "fecha" del
plan, que el generador computa con datetime.date.today() y por tanto trae HOY en
la regeneracion y el dia del sellado en el fichero sellado. NO SE PARCHEA LA
FECHA NI SE FIJA POR BANDERA (el generador dice "LA FECHA SE MIDE, NO SE
TECLEA"): se comparan las lineas, y si la UNICA que difiere es la de "fecha", se
declara con las dos lineas impresas. Cualquier otra linea distinta es ROJO.

PRUEBA DE MUTACION (EJECUTOR regla 1, sobre una variable QUE EL CODIGO COMPUTA y
nunca sobre un literal): con --mutar-rotulo o --mutar-marca se corrompe UNA linea
concreta del texto regenerado EN MEMORIA antes de comparar, y el caso tiene que
CAER nombrando esa linea. La variable del veredicto es `distintas`, que sale de
comparar dos listas de lineas leidas de dos ficheros; no hay ningun literal
comparado consigo mismo.

EL RENOMBRE DE LA 2.c (VUELTA 139): la variable `deriva` pasa a ser la funcion
contar_distintas_por_posicion(), y a su lado se imprime el numstat de git del
MISMO par de blobs (numstat_entre). La prueba de mutacion va en
--mutar-cifras-de-deriva y muerde sobre LAS DOS CIFRAS COMPUTADAS.

--mutar-fecha ES DE OTRA ESPECIE Y SE DECLARA COMO TAL: mide EL BORDE DE LA
TOLERANCIA, no la mordida. Cambiar la linea de la fecha tiene que dar VERDE,
porque la fecha es la unica diferencia tolerada; si diera ROJO, la tolerancia
estaria mal escrita, y si --mutar-rotulo o --mutar-marca dieran VERDE, la
tolerancia se habria comido lineas que no le tocan. Las tres juntas acotan la
tolerancia por los dos lados: una linea dentro (VERDE) y dos fuera (ROJO).

USO:
  python scripts/loop/vuelta138_2a_caso_positivo_63_64.py
  python scripts/loop/vuelta138_2a_caso_positivo_63_64.py --mutar-rotulo
  python scripts/loop/vuelta138_2a_caso_positivo_63_64.py --mutar-marca
  python scripts/loop/vuelta138_2a_caso_positivo_63_64.py --mutar-fecha
  python scripts/loop/vuelta138_2a_caso_positivo_63_64.py --mutar-cifras-de-deriva
"""
import argparse
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GENERADOR = os.path.join("scripts", "loop", "generar_plan_de_fusion_de_mesa.py")

# LO QUE SE COPIA DE HOY AL ARBOL VIEJO, y por que EXACTAMENTE esto:
# el CODIGO va entero de hoy (el generador de mesa reparado en la 2.a y su
# hermano de lotes, del que importa las guardas), porque lo que se prueba es
# que EL GENERADOR DE HOY regenera los planes sellados sin moverlos; y los tres
# CONTENIDOS EDITORIALES tambien, porque ninguno nace hasta el commit del
# sellado y en el PADRE, que es el arbol contra el que se regenera, todavia no
# existen (medido: git log de los tres da UN solo commit, el del sellado, y
# desde entonces no se han vuelto a tocar, o sea que copiarlos de hoy es copiar
# los mismos bytes con los que se sellaron). LOS DATOS NO SE COPIAN: nodos y
# docs/plan/OPERACIONES.jsonl son los del arbol viejo, que es el punto.
A_COPIAR = [
    os.path.join("scripts", "loop", "generar_plan_de_fusion_de_mesa.py"),
    os.path.join("scripts", "loop", "generar_plan_del_lote.py"),
    os.path.join("scripts", "loop", "_v63_opm02prog.py"),
    os.path.join("scripts", "loop", "_v63_opm03i.py"),
    os.path.join("scripts", "loop", "_v64_opm03ii.py"),
]

CASOS = [
    # (plan sellado, id_op, modulo de contenido, vuelta, absorbido)
    ("PLAN_V63_OPM02PROG.json", "OP-M-02-PROG", "_v63_opm02prog", 63,
     "fases_de_retencion_de_clientes"),
    ("PLAN_V63_OPM03I.json", "OP-M-03-I", "_v63_opm03i", 63,
     "decision_pivote_perseverar"),
    ("PLAN_V64_OPM03II.json", "OP-M-03-II", "_v64_opm03ii", 64,
     "pivotar_o_proceder"),
]


def git(args, cwd=RAIZ):
    r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("ROJO: git %s fallo: %s" % (" ".join(args), r.stderr.strip()))
    return r.stdout


def commit_que_anade(rel):
    out = git(["log", "--diff-filter=A", "--pretty=format:%H", "--", rel])
    h = [x for x in out.splitlines() if x.strip()]
    if len(h) != 1:
        raise SystemExit("ROJO: %s tiene %d commits que lo anaden, se esperaba 1" % (rel, len(h)))
    return h[0]


def deprecado_en(ref, nodo):
    r = subprocess.run(["git", "show", "%s:dataset/nodos/%s.json" % (ref, nodo)],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return "NO EXISTE"
    d = json.loads(r.stdout.decode("utf-8"))
    return bool(d.get("deprecado") or d.get("deprecated"))


def _normalizar(datos):
    return datos.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def lineas(ruta):
    with io.open(ruta, "rb") as f:
        return _normalizar(f.read()).decode("utf-8").split("\n")


def lineas_de_blob(ref, rel):
    """Los bytes que el generador ESCRIBIO, leidos del commit del sellado."""
    r = subprocess.run(["git", "show", "%s:%s" % (ref, rel)], cwd=RAIZ,
                       capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO: no se pudo leer el blob %s:%s" % (ref[:8], rel))
    return _normalizar(r.stdout).decode("utf-8").split("\n")


def contar_distintas_por_posicion(a_lineas, b_lineas):
    """EL RENOMBRE DE LA 2.c (vuelta 139, encargo del auditor sobre el acta de la
    vuelta 138).

    ESTA FUNCION SE LLAMABA `deriva` Y ERA UNA VARIABLE SUELTA, y el nombre
    mentia sobre lo que mide. El auditor lo midio y lo declaro sin contarlo como
    caida: el instrumento publicaba 14 para `PLAN_V63_OPM02PROG.json` donde git
    dice 7 anadidas y 1 borrada (blob 0f692945 contra hoy). LAS DOS CIFRAS SON
    CIERTAS Y MIDEN COSAS DISTINTAS: esto compara LINEA i CONTRA LINEA i, asi
    que una insercion desplaza todo lo que sigue y CADA LINEA DESPLAZADA CUENTA
    COMO DISTINTA aunque su texto no haya cambiado. No es un diff, y `deriva` lo
    sugeria.

    NO SE CAMBIA LO QUE MIDE, SE CAMBIA COMO SE LLAMA, y al lado se imprime el
    numstat de git del MISMO par de blobs (ver numstat_entre), que si es un diff.
    Una cifra que se explica al lado de la otra no puede volver a leerse como si
    fuera la que no es.
    """
    total = 0
    for i in range(max(len(a_lineas), len(b_lineas))):
        x = a_lineas[i] if i < len(a_lineas) else None
        y = b_lineas[i] if i < len(b_lineas) else None
        if x != y:
            total += 1
    return total


def numstat_entre(ref_a, ref_b, rel):
    """El numstat de git del MISMO par de blobs que compara
    contar_distintas_por_posicion (vuelta 139, 2.c). Devuelve (anadidas,
    borradas). Si git no imprime fila para la ruta, no hubo cambio: (0, 0)."""
    out = git(["diff", "--numstat", ref_a, ref_b, "--", rel])
    for l in out.splitlines():
        campos = l.split("\t")
        if len(campos) == 3 and campos[0].isdigit() and campos[1].isdigit():
            return int(campos[0]), int(campos[1])
    return 0, 0


def commits_que_lo_editan(rel, sello):
    """Los commits posteriores al sellado que TOCAN el plan. Se miden y se
    imprimen; una edicion posterior no invalida el caso, pero callarla si."""
    out = git(["log", "--pretty=format:%H%s", "--", rel])
    filas = []
    for l in out.splitlines():
        if chr(1) not in l:
            continue
        h, s = l.split(chr(1), 1)
        if h != sello:
            filas.append((h, s))
    return filas


def mutar(texto_lineas, modo):
    """Corrompe UNA linea del texto regenerado. Devuelve (lineas, que_se_muto).
    No toca ningun fichero del repositorio: solo la lista en memoria que se
    compara. Es la prueba de mutacion del caso positivo."""
    if modo == "rotulo":
        for i, l in enumerate(texto_lineas):
            if l.lstrip().startswith('"rotulo":'):
                texto_lineas[i] = l + "   MUTADO"
                return texto_lineas, "la linea del rotulo (indice %d)" % i
        raise SystemExit("ROJO: no se hallo la linea del rotulo para mutar")
    if modo == "marca":
        for i, l in enumerate(texto_lineas):
            if '"APPEND"' in l:
                texto_lineas[i] = l.replace('"APPEND"', '"CUBIERTO:1"')
                return texto_lineas, "una marca APPEND cambiada a CUBIERTO:1 (indice %d)" % i
        raise SystemExit("ROJO: no se hallo ninguna marca APPEND para mutar")
    if modo == "fecha":
        for i, l in enumerate(texto_lineas):
            if l.lstrip().startswith('"fecha":'):
                texto_lineas[i] = ' "fecha": "1999-01-01",'
                return texto_lineas, "la linea de la fecha (indice %d)" % i
        raise SystemExit("ROJO: no se hallo la linea de la fecha para mutar")
    return texto_lineas, "NINGUNA"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutar-rotulo", dest="mut", action="store_const", const="rotulo")
    ap.add_argument("--mutar-marca", dest="mut", action="store_const", const="marca")
    ap.add_argument("--mutar-fecha", dest="mut", action="store_const", const="fecha")
    ap.add_argument("--mutar-cifras-de-deriva", dest="mut_cifras", action="store_true",
                    help="PRUEBA DE MUTACION DE LA 2.c (vuelta 139), sobre las DOS cifras "
                         "COMPUTADAS y no sobre ningun literal: inserta UNA linea en el "
                         "fichero de hoy EN MEMORIA antes de contar. La cuenta POSICIONAL "
                         "tiene que MOVERSE (prueba que sale de los datos), y el numstat de "
                         "git tiene que quedarse IGUAL (prueba que las dos cifras miden cosas "
                         "distintas, que es justo lo que el renombre declara). Ademas se corre "
                         "el numstat contra si mismo (sello..sello), que tiene que dar 0 y 0.")
    ap.set_defaults(mut=None)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("CASO POSITIVO DE LA OPERACION 2.a (vuelta 138): los TRES planes de las")
    print("vueltas 63 y 64, regenerados con el generador de HOY.")
    if a.mut == "fecha":
        print("MODO BORDE DE LA TOLERANCIA: fecha. EL CASO TIENE QUE SEGUIR VERDE.")
    elif a.mut:
        print("MODO MUTACION: %s. EL CASO TIENE QUE CAER." % a.mut)
    print("=" * 78)

    veredictos = []
    veredictos_cifras = []
    for nombre_plan, id_op, contenido, vuelta, absorbido in CASOS:
        rel = "docs/loop/%s" % nombre_plan
        sello = commit_que_anade(rel)
        padre = git(["rev-parse", "%s^" % sello]).strip()
        print("")
        print("-" * 78)
        print("%s (%s, vuelta %d)" % (nombre_plan, id_op, vuelta))
        print("  sellado en    : %s" % sello[:8])
        print("  se regenera en: %s (su padre)" % padre[:8])
        print("  absorbido %s, deprecado en el sello: %s"
              % (absorbido, deprecado_en(sello, absorbido)))
        print("  absorbido %s, deprecado en el padre: %s"
              % (absorbido, deprecado_en(padre, absorbido)))
        print("  absorbido %s, deprecado HOY        : %s"
              % (absorbido, deprecado_en("HEAD", absorbido)))

        tmp = tempfile.mkdtemp(prefix="wt_v138_2a_")
        wt = os.path.join(tmp, "arbol")
        a_lineas = None
        try:
            git(["worktree", "add", "--detach", "--quiet", wt, padre])
            for rel_cp in A_COPIAR:
                shutil.copyfile(os.path.join(RAIZ, rel_cp), os.path.join(wt, rel_cp))
            r = subprocess.run(
                [sys.executable, GENERADOR, "--vuelta", str(vuelta), "--id-op", id_op,
                 "--contenido", contenido, "--prefijo", "REGEN_V138_"],
                cwd=wt, capture_output=True, text=True)
            regen = os.path.join(wt, "docs", "loop",
                                 "REGEN_V138_%s.json" % id_op.replace("-", ""))
            if r.returncode != 0 or not os.path.exists(regen):
                print("  ROJO: el generador no sello el plan (exit %d)" % r.returncode)
                print("  ---- ultimas lineas de la salida del generador ----")
                for l in (r.stdout + r.stderr).splitlines()[-25:]:
                    print("  %s" % l)
                veredictos.append((nombre_plan, "ROJO, no se pudo regenerar"))
            else:
                for l in r.stdout.splitlines():
                    if "FORMATO DEL REPARTO" in l:
                        print(" %s" % l)
                a_lineas = lineas(regen)
        finally:
            subprocess.run(["git", "worktree", "remove", "--force", wt],
                           cwd=RAIZ, capture_output=True, text=True)
            shutil.rmtree(tmp, ignore_errors=True)

        if a_lineas is None:
            continue
        b_lineas = lineas_de_blob(sello, rel)

        # EL FICHERO DE HOY CONTRA SU SELLADO, medido e impreso, nunca callado.
        # LAS DOS CIFRAS VAN JUNTAS Y CADA UNA CON SU NOMBRE (vuelta 139, 2.c).
        hoy_lineas = lineas(os.path.join(RAIZ, rel))
        lineas_distintas_por_posicion = contar_distintas_por_posicion(hoy_lineas, b_lineas)
        anadidas, borradas = numstat_entre(sello, "HEAD", rel)
        editores = commits_que_lo_editan(rel, sello)
        print("  el fichero de HOY contra el blob del sellado, DOS cifras y no una:")
        print("     lineas distintas POR POSICION  : %d  (comparacion posicional: una "
              "insercion desplaza lo que sigue y todo lo desplazado cuenta)"
              % lineas_distintas_por_posicion)
        print("     numstat de git (%s..HEAD)  : %d anadida(s), %d borrada(s)"
              % (sello[:8], anadidas, borradas))
        print("     commits posteriores que lo tocan: %s"
              % (", ".join("%s (%s)" % (h[:8], s[:58]) for h, s in editores) or "NINGUNO"))

        if a.mut_cifras:
            # PRUEBA DE MUTACION DE LA 2.c, sobre las DOS cifras COMPUTADAS.
            mutadas = list(hoy_lineas)
            mutadas.insert(1, ' "LINEA INSERTADA POR LA MUTACION DE LA 2.c",')
            cuenta_mutada = contar_distintas_por_posicion(mutadas, b_lineas)
            numstat_consigo = numstat_entre(sello, sello, rel)
            print("     MUTACION 2.c, una linea insertada en el fichero de hoy EN MEMORIA:")
            print("        cuenta POSICIONAL antes %d, despues %d, se movio: %s"
                  % (lineas_distintas_por_posicion, cuenta_mutada,
                     cuenta_mutada != lineas_distintas_por_posicion))
            print("        numstat de git contra si mismo (%s..%s): %d anadida(s), "
                  "%d borrada(s)" % (sello[:8], sello[:8], numstat_consigo[0],
                                     numstat_consigo[1]))
            mut_ok = (cuenta_mutada != lineas_distintas_por_posicion
                      and numstat_consigo == (0, 0))
            veredictos_cifras.append((nombre_plan, mut_ok, lineas_distintas_por_posicion,
                                      cuenta_mutada, anadidas, borradas, numstat_consigo))

        if a.mut:
            a_lineas, que = mutar(a_lineas, a.mut)
            print("  MUTACION APLICADA AL REGENERADO: %s" % que)

        distintas = []
        for i in range(max(len(a_lineas), len(b_lineas))):
            x = a_lineas[i] if i < len(a_lineas) else "<no hay linea>"
            y = b_lineas[i] if i < len(b_lineas) else "<no hay linea>"
            if x != y:
                distintas.append((i + 1, x, y))

        solo_fecha = bool(distintas) and all(
            x.lstrip().startswith('"fecha":') and y.lstrip().startswith('"fecha":')
            for _, x, y in distintas)

        print("  lineas regeneradas %d, lineas selladas %d, lineas distintas %d"
              % (len(a_lineas), len(b_lineas), len(distintas)))
        if not distintas:
            print("  VERDE: IDENTICOS byte a byte, sin ninguna diferencia.")
            veredictos.append((nombre_plan, "IDENTICOS"))
        elif solo_fecha:
            for n, x, y in distintas:
                print("     linea %d regenerada: %s" % (n, x.strip()))
                print("     linea %d sellada   : %s" % (n, y.strip()))
            print("  VERDE CON LA UNICA DIFERENCIA DECLARADA: solo la linea de la fecha,")
            print("  que el generador computa con datetime.date.today() y no se parchea.")
            veredictos.append((nombre_plan, "IDENTICOS salvo la fecha, declarada"))
        else:
            for n, x, y in distintas[:12]:
                print("     linea %d regenerada: %s" % (n, x.strip()[:150]))
                print("     linea %d sellada   : %s" % (n, y.strip()[:150]))
            if len(distintas) > 12:
                print("     y %d linea(s) distinta(s) mas" % (len(distintas) - 12))
            print("  ROJO: hay diferencias fuera de la fecha.")
            veredictos.append((nombre_plan, "ROJO, %d linea(s) distintas" % len(distintas)))

    print("")
    print("=" * 78)
    for nombre_plan, v in veredictos:
        print("  %-28s %s" % (nombre_plan, v))
    malos = [v for _, v in veredictos if v.startswith("ROJO")]

    if a.mut_cifras:
        print("")
        print("  PRUEBA DE MUTACION DE LA 2.c, LAS DOS CIFRAS COMPUTADAS:")
        for nom, ok, antes, despues, an, bo, consigo in veredictos_cifras:
            print("     %-28s posicional %d -> %d | numstat %d/%d | consigo %d/%d | %s"
                  % (nom, antes, despues, an, bo, consigo[0], consigo[1],
                     "VERDE" if ok else "ROJO"))
        if not veredictos_cifras or not all(ok for _, ok, *_ in veredictos_cifras):
            print("ROJO DE LA MUTACION 2.c: alguna de las dos cifras no se movio como debe,")
            print("o sea que no se computa de los datos que dice medir.")
            print("FIN")
            return 1
        print("VERDE DE LA MUTACION 2.c: la cuenta POSICIONAL se mueve al insertar una")
        print("linea (sale de los datos) y el numstat de git NO se mueve por esa insercion")
        print("en memoria y da 0/0 contra si mismo (sale de git). Son dos cifras distintas")
        print("y ahora cada una lleva su nombre.")
        print("FIN")
        return 0 if not malos else 1

    if a.mut == "fecha":
        # BORDE DE LA TOLERANCIA: tiene que dar VERDE, no caer.
        if malos:
            print("ROJO DEL BORDE: mutar la fecha hizo caer el caso, o sea que la unica")
            print("diferencia declarada como tolerada NO lo esta de verdad.")
            print("FIN")
            return 1
        print("VERDE DEL BORDE: mutar la linea de la fecha NO hace caer el caso, que es")
        print("exactamente la tolerancia declarada, ni una linea mas.")
        print("FIN")
        return 0
    if a.mut:
        if malos:
            print("VERDE DE LA MUTACION: el caso CAE, %d de %d planes en ROJO."
                  % (len(malos), len(veredictos)))
            print("FIN")
            return 0
        print("ROJO DE LA MUTACION: el caso NO cae con la mutacion aplicada, o sea que no")
        print("puede fallar nunca y no prueba nada.")
        print("FIN")
        return 1
    if malos or len(veredictos) != len(CASOS):
        print("ROJO: %d de %d planes no se regeneran identicos." % (len(malos), len(CASOS)))
        print("FIN")
        return 1
    print("VERDE: los %d planes se regeneran identicos con el generador de hoy." % len(veredictos))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
