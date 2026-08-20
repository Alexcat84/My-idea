# -*- coding: utf-8 -*-
# ROTULO titulo especie=SELLO_FIJO sujeto=acta:63 corte=2026-08-20 motivo="el numero del titulo es la vuelta propia del fichero y no entra por argumento"
"""_v63_verificar_opm03i.py . COMPRUEBA, UNA POR UNA, LAS CINCO COSAS QUE LA
FICHA DE OP-M-03-I MANDA COMPROBAR DESPUES DE FUNDIR.

DE SOLO LECTURA. Lee el arbol de hoy y el arbol de ANTES de la fusion (por git
show del commit de apertura de la vuelta), y compara.

LAS CINCO, copiadas de docs/plan/OPERACIONES.jsonl:
  1. LAS TRES PIEZAS PROPIAS DEL PAR ESTAN EN EL TEXTO FINAL: racionalizacion del
     fracaso, linea base nueva y comprobacion posterior.
  2. EL BLOQUE DEL PUNTO BRILLANTE, los 5 pasos, sigue BYTE A BYTE en
     puntos_brillantes_antes_del_pivote, con su fuente Traction sola.
  3. LA ARISTA del sujeto muerto hacia ese nodo queda REDIRIGIDA al superviviente
     CON SU ESPEJO, y no se pierde.
  4. EL NODO PROPIO sigue VIVO y NO deprecado.
  5. EL ALIAS del superviviente carga el id que muere.
Y una sexta que la ficha pide de otra forma y aqui se mide igual: el absorbido
queda DEPRECADO con su texto INTACTO.

Uso: python scripts/loop/_v63_verificar_opm03i.py [--antes <hash>]
exit 0 si las seis pasan; exit 1 si alguna falla.
"""
import argparse
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SUP = "pivotar_o_perseverar"
MUERE = "decision_pivote_perseverar"
PROPIO = "puntos_brillantes_antes_del_pivote"
NL = chr(10)


def hoy(nid):
    return json.load(io.open(os.path.join(RAIZ, "dataset", "nodos", nid + ".json"),
                             encoding="utf-8"))


def antes(nid, commit):
    bruto = subprocess.check_output(
        ["git", "show", "%s:dataset/nodos/%s.json" % (commit, nid)], cwd=RAIZ)
    return json.loads(bruto.decode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--antes", default="0f7d2ef0",
                    help="commit del arbol PREVIO a la fusion")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    fallos = []
    print("=" * 78)
    print("VERIFICACION DE OP-M-03-I, LAS SEIS COSAS QUE LA FICHA MANDA COMPROBAR")
    print("  arbol de ANTES: commit %s (por git show)" % a.antes)
    print("=" * 78)

    s = hoy(SUP)
    m = hoy(MUERE)
    p = hoy(PROPIO)
    p0 = antes(PROPIO, a.antes)
    m0 = antes(MUERE, a.antes)

    # 1
    print()
    print("1. LAS TRES PIEZAS PROPIAS DEL PAR, EN EL TEXTO FINAL DEL SUPERVIVIENTE")
    texto = NL.join(s["pasos_accionables"])
    piezas = [("racionalizacion del fracaso", "racionalizar el fracaso"),
              ("linea base nueva", "nueva línea base"),
              ("comprobacion posterior", "después del cambio")]
    for etq, aguja in piezas:
        donde = [i for i, x in enumerate(s["pasos_accionables"], 1) if aguja in x]
        ok = bool(donde)
        print("   %-28s %-4s %s" % (etq, "OK" if ok else "ROJO",
                                    "paso %s" % donde if donde else "NO ESTA"))
        if not ok:
            fallos.append("la pieza %s no esta en el texto final" % etq)
    print("   el superviviente queda con %d pasos y %d condiciones"
          % (len(s["pasos_accionables"]), len(s["condiciones_activacion"])))

    # 2
    print()
    print("2. EL BLOQUE DEL PUNTO BRILLANTE, BYTE A BYTE EN SU NODO PROPIO")
    igual = p["pasos_accionables"] == p0["pasos_accionables"]
    print("   pasos hoy: %d | pasos antes: %d | IDENTICOS BYTE A BYTE: %s"
          % (len(p["pasos_accionables"]), len(p0["pasos_accionables"]),
             "SI" if igual else "NO"))
    if not igual:
        fallos.append("los pasos del nodo propio cambiaron")
    print("   fuente: %r (antes %r)" % (p.get("fuente"), p0.get("fuente")))
    if p.get("fuente") != p0.get("fuente"):
        fallos.append("la fuente del nodo propio cambio")
    cero_en_el_muerto = sum(1 for x in m["pasos_accionables"]
                            if x in p0["pasos_accionables"])
    print("   pasos del bloque que estaban en el que MUERE: %d de %d (la correccion "
          "declarada de la ficha decia 0 de 5)"
          % (cero_en_el_muerto, len(p0["pasos_accionables"])))
    if cero_en_el_muerto != 0:
        fallos.append("el que muere si traia pasos del bloque")

    # 3
    print()
    print("3. LA ARISTA REDIRIGIDA AL SUPERVIVIENTE, CON SU ESPEJO")
    ida = PROPIO in (s.get("nodos_siguientes") or [])
    vuelta = SUP in (p.get("nodos_previos") or [])
    antes_ida = PROPIO in (m0.get("nodos_siguientes") or [])
    antes_vuelta = MUERE in (p0.get("nodos_previos") or [])
    print("   ANTES: el que muere lo nombraba en nodos_siguientes: %s | el nodo propio "
          "nombraba al que muere en nodos_previos: %s" % (antes_ida, antes_vuelta))
    print("   HOY  : el superviviente lo nombra en nodos_siguientes: %s | el nodo propio "
          "nombra al superviviente en nodos_previos: %s" % (ida, vuelta))
    print("   el id del muerto ya NO aparece en el nodo propio: %s"
          % (MUERE not in (p.get("nodos_previos") or [])))
    if not (ida and vuelta):
        fallos.append("la arista no quedo redirigida con su espejo")
    if MUERE in (p.get("nodos_previos") or []):
        fallos.append("el nodo propio sigue nombrando al muerto")

    # 4
    print()
    print("4. EL NODO PROPIO SIGUE VIVO")
    vivo = not (p.get("deprecado") or p.get("deprecated"))
    print("   deprecado: %r | VIVO: %s" % (p.get("deprecado"), "SI" if vivo else "NO"))
    if not vivo:
        fallos.append("el nodo propio quedo deprecado")

    # 5
    print()
    print("5. EL ALIAS DEL SUPERVIVIENTE CARGA EL ID QUE MUERE")
    alias = s.get("ids_alias") or []
    print("   ids_alias: %s" % alias)
    if MUERE not in alias:
        fallos.append("el alias no carga el id que muere")
    fundidos = [x.get("node_id") for x in (s.get("merged_originals") or [])]
    print("   merged_originals: %s" % fundidos)
    if MUERE not in fundidos:
        fallos.append("merged_originals no registra al que muere")

    # 6
    print()
    print("6. EL ABSORBIDO, DEPRECADO Y CON SU TEXTO INTACTO")
    dep = bool(m.get("deprecado") or m.get("deprecated"))
    intacto = (m["pasos_accionables"] == m0["pasos_accionables"]
               and m["condiciones_activacion"] == m0["condiciones_activacion"]
               and m.get("nodos_previos") == m0.get("nodos_previos")
               and m.get("nodos_siguientes") == m0.get("nodos_siguientes"))
    print("   deprecado: %s | texto y aristas INTACTOS: %s"
          % ("SI" if dep else "NO", "SI" if intacto else "NO"))
    if not dep:
        fallos.append("el absorbido no quedo deprecado")
    if not intacto:
        fallos.append("el absorbido perdio texto o aristas")

    print()
    print("=" * 78)
    if fallos:
        print("ROJO, %d comprobacion(es) fallan:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("LAS SEIS EN VERDE.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
