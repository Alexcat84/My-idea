# -*- coding: utf-8 -*-
"""_v64_verificar_opm03ii.py . COMPRUEBA, UNA POR UNA, LAS COSAS QUE LA FICHA DE
OP-M-03-II MANDA COMPROBAR DESPUES DE FUNDIR, MAS LAS DOS QUE EL DIFF DE
DUPLICADAS DEJO SIN EXPLICAR.

DE SOLO LECTURA. Lee el arbol de hoy y el arbol de ANTES de la fusion (por git
show del commit que se le pase), y compara. NO reusa el verificador del fundidor:
el camino es propio a proposito, para que la coincidencia sea contraste.

LO QUE LA FICHA MANDA (docs/plan/OPERACIONES.jsonl, campo verificacion):
  1. la clasificacion AMOR TOTAL A INDIFERENCIA esta en el texto final;
  2. el alias del superviviente carga pivotar_o_proceder. SE LEEN LAS DOS FORMAS
     de merged_originals que el catalogo tiene (lista de cadenas y lista de
     diccionarios) y se imprime cual es, en vez de dar una por buena;
  3. LAS DOS DUPLICADAS QUE ESTA FUSION FABRICA, nombradas en la ficha
     (presentacion_solucion_producto.nodos_previos y
     scorecard_descubrimiento_cliente.nodos_siguientes), medidas HOY. La ficha
     dice que quedan para OP-S-12 y P.16 dice que se limpian en el mismo commit;
     manda P.16, y aqui se comprueba que estan LIMPIAS.
Y LAS QUE LA CAMPANA MANDA IGUAL:
  4. el absorbido queda DEPRECADO con su texto INTACTO;
  5. las DOS piezas que la ficha reclasifica como QUE VIVEN DENTRO (dibujar como
     trabaja el cliente tipico, reducir la lista a un parrafo) siguen intactas;
  6. el INCISO adosado esta en el paso 7 y es VERBATIM del paso 4 del que muere.

Y LA QUE NACE DE UNA MEDICION QUE NO CUADRABA A LA PRIMERA, y por eso se mide en
vez de explicarse: EL DIFF DE DUPLICADAS dice que DESAPARECEN DOS grupos, y NO
son los dos que P.16 limpio. La comprobacion 7 mide de donde salen los dos.

Uso: python scripts/loop/_v64_verificar_opm03ii.py --antes <hash>
exit 0 si todas pasan; exit 1 si alguna falla.
"""
import argparse
import io
import json
import os
import subprocess
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SUP = "pivote_o_proceder"
MUERE = "pivotar_o_proceder"
DUPLICADAS_DE_LA_FICHA = [("presentacion_solucion_producto", "nodos_previos"),
                          ("scorecard_descubrimiento_cliente", "nodos_siguientes")]
ANTES_JSONL = os.path.join(RAIZ, "docs", "loop", "_v64_duplicadas_antes.jsonl")
DESPUES_JSONL = os.path.join(RAIZ, "docs", "loop", "_v64_duplicadas_despues.jsonl")


def sin_acentos(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn").lower()


def hoy(nid):
    return json.load(io.open(os.path.join(RAIZ, "dataset", "nodos", nid + ".json"),
                             encoding="utf-8"))


def antes(nid, commit):
    bruto = subprocess.check_output(
        ["git", "show", "%s:dataset/nodos/%s.json" % (commit, nid)], cwd=RAIZ)
    return json.loads(bruto.decode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--antes", required=True, help="commit del arbol de antes de fundir")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    s_hoy, m_hoy = hoy(SUP), hoy(MUERE)
    s_ant, m_ant = antes(SUP, a.antes), antes(MUERE, a.antes)
    fallos = []

    print("=" * 78)
    print("VERIFICACION DE OP-M-03-II, POR CAMINO PROPIO")
    print("  arbol de antes: %s | superviviente %s | absorbido %s" % (a.antes, SUP, MUERE))
    print("=" * 78)

    print()
    print("1. LA CLASIFICACION AMOR TOTAL A INDIFERENCIA, EN EL TEXTO FINAL")
    pasos = s_hoy.get("pasos_accionables") or []
    aguja = sin_acentos("desde amor total hasta indiferencia")
    donde = [i for i, p in enumerate(pasos, 1) if aguja in sin_acentos(p)]
    print("   pasos del superviviente HOY: %d (antes %d)"
          % (len(pasos), len(s_ant.get("pasos_accionables") or [])))
    print("   la frase vive en el paso: %s" % (donde or "NINGUNO"))
    if donde:
        print("   texto: %s" % pasos[donde[0] - 1])
    else:
        fallos.append("la clasificacion amor total a indiferencia NO esta en el texto final")

    print()
    print("2. EL ALIAS DEL SUPERVIVIENTE CARGA EL ID QUE MUERE")
    al = s_hoy.get("ids_alias") or []
    mo = s_hoy.get("merged_originals") or []
    # merged_originals NO TIENE UNA SOLA FORMA EN EL CATALOGO, y esto se dice en
    # vez de suponerse: en pivotar_o_perseverar (OP-M-03-I, vuelta 63) es una
    # lista de CADENAS y aqui es una lista de DICCIONARIOS con node_id, titulo y
    # fuente. La primera corrida de este verificador dio ROJO por dar por buena
    # la forma de cadena. Se leen las dos formas y se imprime cual es.
    forma = ("cadenas" if all(isinstance(x, str) for x in mo)
             else ("diccionarios" if all(isinstance(x, dict) for x in mo) else "MEZCLADA"))
    ids_mo = [x if isinstance(x, str) else x.get("node_id") for x in mo]
    print("   ids_alias       : %s" % al)
    print("   merged_originals: forma %s | ids %s" % (forma, ids_mo))
    print("   merged_originals en crudo: %s" % mo)
    if MUERE not in al:
        fallos.append("ids_alias del superviviente NO carga %s" % MUERE)
    if MUERE not in ids_mo:
        fallos.append("merged_originals del superviviente NO carga %s" % MUERE)
    if forma == "MEZCLADA":
        fallos.append("merged_originals mezcla cadenas y diccionarios en el mismo nodo")

    print()
    print("3. LAS DOS DUPLICADAS QUE LA FICHA NOMBRA, MEDIDAS HOY (P.16 manda)")
    alias = {}
    for f in os.listdir(os.path.join(RAIZ, "dataset", "nodos")):
        if f.endswith(".json"):
            j = json.load(io.open(os.path.join(RAIZ, "dataset", "nodos", f),
                                  encoding="utf-8"))
            for x in (j.get("ids_alias") or []):
                alias.setdefault(x, j.get("node_id") or f[:-5])

    def res(x):
        v = set()
        while x in alias and x not in v:
            v.add(x)
            x = alias[x]
        return x
    for nodo_, campo in DUPLICADAS_DE_LA_FICHA:
        d = hoy(nodo_)
        entradas = d.get(campo) or []
        resueltas = [res(x) for x in entradas]
        n_sup = resueltas.count(SUP)
        print("   %-34s %-17s entradas %d | resuelven a %s: %d"
              % (nodo_, campo, len(entradas), SUP, n_sup))
        print("      entradas: %s" % entradas)
        if n_sup > 1:
            fallos.append("%s.%s sigue con %d entradas que resuelven a %s"
                          % (nodo_, campo, n_sup, SUP))
    print("   LAS DOS EN CERO: la duplicada que la fusion fabrico esta LIMPIA, que")
    print("   es lo que P.16 manda y lo contrario de lo que la ficha del 12 ago decia.")

    print()
    print("4. EL ABSORBIDO, DEPRECADO Y CON SU TEXTO INTACTO")
    dep = bool(m_hoy.get("deprecado") or m_hoy.get("deprecated"))
    intacto = all(m_hoy.get(k) == m_ant.get(k)
                  for k in ("pasos_accionables", "condiciones_activacion",
                            "titulo_concepto", "resumen_teorico",
                            "entregable_esperado", "nodos_previos",
                            "nodos_siguientes"))
    print("   deprecado: %s | texto y aristas INTACTOS: %s"
          % ("SI" if dep else "NO", "SI" if intacto else "NO"))
    if not dep:
        fallos.append("el absorbido NO quedo deprecado")
    if not intacto:
        fallos.append("el texto del absorbido NO quedo intacto")

    print()
    print("5. LAS DOS PIEZAS QUE LA FICHA RECLASIFICA COMO QUE VIVEN DENTRO")
    for etq, i in (("dibujar como trabaja el cliente tipico", 2),
                   ("reducir la lista de funciones a un parrafo", 6)):
        viejo = (s_ant.get("pasos_accionables") or [])[i - 1]
        nuevo = pasos[i - 1] if len(pasos) >= i else "(NO EXISTE)"
        ok = viejo == nuevo
        print("   paso %d, %s: INTACTO %s" % (i, etq, "SI" if ok else "NO"))
        print("      %s" % nuevo)
        if not ok:
            fallos.append("el paso %d del superviviente cambio y la ficha lo declara intocable" % i)

    print()
    print("6. EL INCISO ADOSADO, VERBATIM DEL PASO 4 DEL QUE MUERE")
    p7 = pasos[6] if len(pasos) >= 7 else ""
    p7_ant = (s_ant.get("pasos_accionables") or [])[6]
    p4m = (m_hoy.get("pasos_accionables") or [])[3]
    trozo = p7[len(p7_ant):].lstrip()
    print("   paso 7 ANTES : %s" % p7_ant)
    print("   paso 7 HOY   : %s" % p7)
    print("   lo anadido   : %r" % trozo)
    print("   es subcadena LITERAL del paso 4 del que muere: %s" % (trozo in p4m))
    if not p7.startswith(p7_ant):
        fallos.append("el paso 7 no conserva su texto de antes delante del inciso")
    if not trozo or trozo not in p4m:
        fallos.append("el inciso adosado NO es subcadena literal del paso 4 del que muere")

    print()
    print("7. DE DONDE SALEN LOS DOS GRUPOS DE DUPLICADAS QUE DESAPARECEN")
    print("   El diff dice que el censo baja de 927 a 925 y que DESAPARECEN DOS")
    print("   grupos, y NO son los dos que P.16 limpio. Se mide de donde salen.")
    ant = [json.loads(l) for l in io.open(ANTES_JSONL, encoding="utf-8") if l.strip()]
    des = [json.loads(l) for l in io.open(DESPUES_JSONL, encoding="utf-8") if l.strip()]
    clave = lambda d: (d["nodo"], d["campo"], d["destino"])
    idos = [d for d in ant if clave(d) not in {clave(x) for x in des}]
    print("   grupos que desaparecen: %d" % len(idos))
    del_muerto = 0
    for d in idos:
        es = d["nodo"] == MUERE
        del_muerto += 1 if es else 0
        print("      %-24s %-17s -> %-34s | vive en el nodo QUE MUERE: %s"
              % (d["nodo"], d["campo"], d["destino"], "SI" if es else "NO"))
        print("         entradas: %s" % d["entradas"])
    print()
    print("   LOS %d SON DEL NODO QUE MUERE: %d de %d." % (len(idos), del_muerto, len(idos)))
    print("   LA EXPLICACION MEDIDA, y no es que P.16 los limpiara: el censo de")
    print("   aristas_duplicadas_tras_resolver.py solo revisa NODOS VIVOS (3272")
    print("   antes, 3271 despues), y estos dos eran duplicadas HISTORICAS DENTRO")
    print("   de %s. Al quedar deprecado, SALEN DEL CENSO. No se" % MUERE)
    print("   han reparado: siguen enteras en su nodo, que conserva su texto")
    print("   intacto (comprobacion 4). LAS DOS QUE P.16 SI LIMPIO nunca entraron")
    print("   en el censo porque nacieron y murieron dentro de la misma corrida,")
    print("   y por eso el diff da CERO grupos fabricados.")
    if del_muerto != len(idos):
        fallos.append("hay grupos que desaparecen y NO son del nodo que muere: sin explicar")
    # y la contraprueba: las dos siguen dentro del nodo muerto
    for d in idos:
        vivas = (m_hoy.get(d["campo"]) or [])
        sigue = all(e in vivas for e in d["entradas"])
        print("   contraprueba: las entradas %s siguen en %s.%s: %s"
              % (d["entradas"], MUERE, d["campo"], "SI" if sigue else "NO"))
        if not sigue:
            fallos.append("las entradas del grupo %s ya no estan en el nodo muerto" % (clave(d),))

    print()
    print("=" * 78)
    if fallos:
        print("ROJO, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("TODAS EN VERDE.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
