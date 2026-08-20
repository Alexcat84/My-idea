# -*- coding: utf-8 -*-
"""vuelta58_deshacer_acto32.py . LA PRIMERA MITAD DE LA CORRECCION DECLARADA DEL
ACTO 32 DEL TRAMO 4: DESHACER LA FUSION EJECUTADA EN LA VUELTA 57.

SUCESOR DECLARADO de scripts/loop/vuelta55_deshacer_acto23.py, cuya maquina se
copia entera (alcance re-medido y no copiado, guardas antes de escribir, modos
simular y ejecutar, comprobacion de los dos vivos y sin alias cruzado).

POR QUE EXISTE. La vuelta 57 fundio el acto 32
(programa_de_referidos_de_franquiciados absorbido por
referidos_franquiciados_existentes) rompiendo un empate TRIPLE con la CANTIDAD
de lineas propias declaradas, una contra dos. El acta 57 del auditor (secciones
2 y 4, discutible D4) sostiene que por la letra vigente ese acto es EMPATE SIN
VARA y va DECLARADO: acta 53 pregunta 4 (linea 13015 de ACTA_AUDITOR.md, que
reserva el empate sin vara para cuando TODO empata) y acta 54 pregunta 4
(linea 13389: el conteo de caracteres no desempata; linea 13391: el propio
declarado de UN SOLO LADO es una vara no empatada). Aqui el propio declarado
esta A LOS DOS LADOS. La relectura conjunta de la vuelta 58 midio las varas
contra el grafo pre fusion (SALIDA_V58_RELECTURA_ACTO32_PREFUSION.txt: pasos
5 contra 5, condiciones 2 contra 2, cableado 3 contra 3, FORMA EMPATE SIN
VARA) y CONFIRMA el caso.

LO QUE ESTE INSTRUMENTO HACE, Y LO QUE NO. Deshace, y solo deshace. No funde en
ninguna direccion: el acto queda DECLARADO, que es el carril del empate sin
vara.

LO UNICO QUE NO ES COPIA DEL ANCESTRO, Y ES LO QUE ESTE ACTO OBLIGA A CAMBIAR:
EL DESHACER NO PUEDE SER UN RESTAURAR EL BLOB EN LOS CINCO FICHEROS. Medido:
de los cinco que el acto 32 toco, CUATRO no se han vuelto a tocar desde el lote
B y se restauran al blob de 0481113f (el commit del lote A), pero
principio_apalancamiento_numero_magico.json SI se toco despues, en el lote C
(706397c7), y por OTRO acto: el 35, que le cambio
marketing_en_ferias_comerciales_de_franquicias por
ferias_comerciales_franquicia. Restaurarle el blob borraria el acto 35. A ese
fichero se le aplica EL DIFF INVERSO del acto 32 (git apply -R), que toca
exactamente la linea del acto 32 y deja la del 35 intacta, y que FALLA VISIBLE
si el contexto no calza en vez de escribir a medias.

GUARDAS ANTES DE ESCRIBIR (si alguna falla, no se escribe nada):
  - el alcance se re-mide aqui de git y tiene que calzar con el declarado;
  - cada fichero se clasifica por MEDICION en restaurable o parcheable, y la
    clasificacion tiene que calzar con la declarada;
  - los cinco tienen que estar limpios en el arbol de trabajo;
  - el parche inverso se prueba con --check antes de aplicarse.

GUARDAS DESPUES DE ESCRIBIR:
  - los dos miembros VIVOS y ninguno con el otro en ids_alias;
  - los dos con TODOS sus campos identicos al blob pre fusion;
  - el cableado de los tres vecinos de vuelta al absorbido, contado.

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.

Uso: python scripts/loop/vuelta58_deshacer_acto32.py [--ejecutar]
"""
# ROTULO titulo especie=SELLO_FIJO sujeto=tramo:4 corte=2026-08-20 motivo="deshace la fusion del acto 32 del tramo 4, un acto nombrado: sujeto fijo"
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:57 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 57 DEL AUDITOR" corte=2026-08-20 motivo="nombra la vuelta 57 como la que ejecuto la fusion que este instrumento deshace"
import argparse
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANTES = "0481113f"   # el commit del lote A: el acto 32 todavia no se ha tocado
LOTE_B = "a1d7269d"  # el commit del lote B: el acto 32 ya esta fundido

SUP_VIEJO = "referidos_franquiciados_existentes"
ABS_VIEJO = "programa_de_referidos_de_franquiciados"

RESTAURABLES = ["dataset/nodos/estrategia_redes_sociales_franquicias.json",
                "dataset/nodos/programa_de_referidos_de_franquiciados.json",
                "dataset/nodos/referidos_franquiciados_existentes.json",
                "dataset/nodos/soporte_continuo_franquicia.json"]
PARCHEABLES = ["dataset/nodos/principio_apalancamiento_numero_magico.json"]
FICHEROS = sorted(RESTAURABLES + PARCHEABLES)
VECINOS = ["dataset/nodos/estrategia_redes_sociales_franquicias.json",
           "dataset/nodos/principio_apalancamiento_numero_magico.json",
           "dataset/nodos/soporte_continuo_franquicia.json"]


def git(*args, **kw):
    p = subprocess.run(["git"] + list(args), capture_output=True, cwd=RAIZ,
                       input=kw.get("entrada"))
    return (p.returncode, p.stdout.decode("utf-8", "replace"),
            p.stderr.decode("utf-8", "replace"))


def blob(commit, ruta):
    rc, out, _ = git("show", "%s:%s" % (commit, ruta))
    return json.loads(out) if rc == 0 else None


def leer(ruta):
    return json.load(io.open(os.path.join(RAIZ, ruta), encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("DESHACER EL ACTO 32 DEL TRAMO 4 . MODO %s"
          % ("EJECUTAR" if a.ejecutar else "SIMULAR"))
    print("=" * 78)
    print()
    fallos = []

    # --- 1. el alcance, re-medido aqui y no copiado ---
    rc, out, _ = git("diff", "--name-only", ANTES, LOTE_B, "--", "dataset/nodos/")
    tocados = [x.strip().replace("\\", "/") for x in out.splitlines() if x.strip()]
    print("  ficheros de nodos que el lote B (%s) toco: %d" % (LOTE_B, len(tocados)))
    propios = set(["dataset/nodos/%s.json" % SUP_VIEJO,
                   "dataset/nodos/%s.json" % ABS_VIEJO])
    del_acto = []
    for f in tocados:
        if f in propios:
            del_acto.append(f)
            continue
        rc, d, _ = git("diff", ANTES, LOTE_B, "--", f)
        marcado = [l for l in d.splitlines()
                   if l[:1] in "+-" and l[:3] not in ("+++", "---")
                   and (SUP_VIEJO in l or ABS_VIEJO in l)]
        if marcado:
            del_acto.append(f)
    print("  de esos, los que el ACTO 32 toco: %d" % len(del_acto))
    for f in del_acto:
        print("     %s" % f)
    calza = sorted(del_acto) == FICHEROS
    if not calza:
        fallos.append("el alcance medido no calza con el declarado: %s" % sorted(del_acto))
    print("  el alcance medido calza con el declarado: %s" % ("SI" if calza else "NO"))
    print()

    # --- 2. la clasificacion, POR MEDICION y no por lista ---
    rc, out, _ = git("diff", "--name-only", LOTE_B, "HEAD", "--", *FICHEROS)
    despues = sorted(x.strip().replace("\\", "/") for x in out.splitlines() if x.strip())
    print("  tocados DESPUES del lote B (van por PARCHE INVERSO): %d" % len(despues))
    for f in despues:
        rc, lg, _ = git("log", "--oneline", "%s..HEAD" % LOTE_B, "--", f)
        linea = lg.strip().splitlines()[0] if lg.strip() else "sin commit"
        print("     %s" % f)
        print("        lo movio: %s" % linea)
    calza2 = despues == sorted(PARCHEABLES)
    if not calza2:
        fallos.append("la clasificacion medida no calza: parcheables medidos %s" % despues)
    print("  la clasificacion medida calza con la declarada: %s" % ("SI" if calza2 else "NO"))
    print()

    # --- 3. los cinco limpios en el arbol de trabajo ---
    rc, out, _ = git("status", "--porcelain", "--", *FICHEROS)
    sucio = [x for x in out.splitlines() if x.strip()]
    print("  los cinco, sucios en el arbol de trabajo: %d %s" % (len(sucio), sucio))
    if sucio:
        fallos.append("hay ficheros sucios: %s" % sucio)
    print()

    # --- 4. el parche inverso se prueba antes de aplicarse ---
    parches = {}
    for f in PARCHEABLES:
        rc, d, _ = git("diff", ANTES, LOTE_B, "--", f)
        parches[f] = d.encode("utf-8")
        rc, _, err = git("apply", "-R", "--check", "-", entrada=parches[f])
        print("  parche inverso de %s: %s"
              % (f.split("/")[-1], "APLICA LIMPIO" if rc == 0 else "ROJO " + err.strip()))
        if rc != 0:
            fallos.append("el parche inverso de %s no aplica: %s" % (f, err.strip()))
    print()

    if fallos:
        print("  ROJO, %d fallos y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("     %s" % f)
        return 1

    print("  ESTADO DE HOY, antes de deshacer:")
    for nid in (SUP_VIEJO, ABS_VIEJO):
        d = leer("dataset/nodos/%s.json" % nid)
        print("     %-42s deprecado %-6s pasos %d cond %d ids_alias %s"
              % (nid, bool(d.get("deprecado")), len(d.get("pasos_accionables") or []),
                 len(d.get("condiciones_activacion") or []), d.get("ids_alias")))
    print()

    if not a.ejecutar:
        print("  MODO SIMULAR: no se escribe nada.")
        print("     %d ficheros se restaurarian al blob de %s" % (len(RESTAURABLES), ANTES))
        print("     %d recibiria el parche inverso del acto 32" % len(PARCHEABLES))
        print()
        print("FIN")
        return 0

    rc, out, err = git("checkout", ANTES, "--", *RESTAURABLES)
    if rc != 0:
        print("  ROJO: el checkout fallo: %s" % err)
        return 1
    print("  RESTAURADOS al blob de %s: %d ficheros" % (ANTES, len(RESTAURABLES)))
    for f in PARCHEABLES:
        rc, _, err = git("apply", "-R", "-", entrada=parches[f])
        if rc != 0:
            print("  ROJO: el parche inverso de %s fallo: %s" % (f, err))
            return 1
        print("  PARCHE INVERSO aplicado a %s" % f.split("/")[-1])
    print()

    # --- guardas de despues ---
    print("  ESTADO TRAS DESHACER:")
    ok = True
    for nid in (SUP_VIEJO, ABS_VIEJO):
        ruta = "dataset/nodos/%s.json" % nid
        d = leer(ruta)
        vivo = not d.get("deprecado")
        alias = d.get("ids_alias") or []
        print("     %-42s vivo %-6s pasos %d cond %d ids_alias %s"
              % (nid, vivo, len(d.get("pasos_accionables") or []),
                 len(d.get("condiciones_activacion") or []), alias))
        if not vivo or SUP_VIEJO in alias or ABS_VIEJO in alias:
            ok = False
        pre = blob(ANTES, ruta)
        igual = (pre == d)
        print("        campo a campo contra el blob pre fusion %s: %s"
              % (ANTES, "IDENTICO" if igual else "DISTINTO"))
        if not igual:
            ok = False
            for k in sorted(set(list(pre or {}) + list(d))):
                if (pre or {}).get(k) != d.get(k):
                    print("           campo que difiere: %s" % k)
    print("  LOS DOS VIVOS, SIN ALIAS CRUZADO Y CON SUS CAMPOS INTACTOS: %s"
          % ("SI" if ok else "NO"))
    print()

    print("  LOS TRES VECINOS, EL CABLEADO DE VUELTA:")
    for f in VECINOS:
        crudo = io.open(os.path.join(RAIZ, f), encoding="utf-8").read()
        n_sup = crudo.count('"%s"' % SUP_VIEJO)
        n_abs = crudo.count('"%s"' % ABS_VIEJO)
        print("     %-52s al absorbido %d | al superviviente %d"
              % (f.split("/")[-1], n_abs, n_sup))
        if n_abs != 1 or n_sup != 0:
            ok = False
    print("  EL CABLEADO VUELVE AL ABSORBIDO EN LOS TRES: %s" % ("SI" if ok else "NO"))
    print()
    print("FIN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
