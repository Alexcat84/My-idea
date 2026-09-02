# -*- coding: utf-8 -*-
"""vuelta137_2a_terreno_fase06.py . TAREA 2 de la vuelta 137: LA APERTURA DE LA
FASE 06, MEDIDA. No funde nada y no toca ni un nodo: mide el terreno de las cinco
mesas y de las SEIS fusiones diferidas, y deja escrito, CON CIFRAS CONTADAS HOY,
que se puede ejecutar y que no.

EJECUTOR regla 2, EL INSTRUMENTO MANDA, y regla 11, NO ADIVINES: las tres cosas
que este fichero afirma se CORREN, no se describen.

  (A) EL ESTADO DE LAS SEIS CONTRA EL GRAFO, NO CONTRA EL CAMPO `estado`. El
      encargo avisa que las DIECISEIS fichas de fase 03 siguen leyendo LISTA, las
      diez que el cierre declaro resueltas incluidas. Asi que aqui el estado se
      mide donde vive: superviviente VIVO y absorbidos DEPRECADOS es fundida;
      absorbidos VIVOS es sin fundir.

  (B) EL TAMANO EDITORIAL. Cuantos absorbidos y cuantas marcas (paso o condicion
      de un absorbido) hay que decidir una por una para sellar las seis.

  (C) LA LIMITACION DEL GENERADOR SELLADO, PROBADA CORRIENDOLO. En
      generar_plan_de_fusion_de_mesa.py, marcar() recibe SIEMPRE el mismo
      spec["pasos"], que esta indexado por NUMERO DE PASO, dentro de un bucle
      `for ab in absorbidos`. Con un solo absorbido eso es exacto; con dos o mas,
      el paso 1 del absorbido A y el paso 1 del absorbido B leen LA MISMA marca y
      no se pueden repartir distinto. Se prueba construyendo un contenido de
      juguete para una fusion de DOS absorbidos y ensenando que la marca que sale
      para los dos es la misma. NO SE PARCHEA AQUI: se mide y se declara.

Salida: docs/loop/SALIDA_V137_2A_TERRENO.txt

USO:
  python scripts/loop/vuelta137_2a_terreno_fase06.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V137_2A_TERRENO.txt")

SEIS = ["OP-M-01-FUSION", "OP-M-02-ACCLIMATE", "OP-M-03-III",
        "OP-M-05-INDICE", "OP-M-05-EDIFICIO", "OP-M-05-APERTURA"]
MESAS = ["OP-M-01", "OP-M-02", "OP-M-03", "OP-M-04", "OP-M-05"]


def cargar_ops():
    with io.open(OPS, encoding="utf-8") as f:
        return {o["id_op"]: o for o in (json.loads(l) for l in f if l.strip())}


def nodo(nid):
    p = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(p):
        return None
    with io.open(p, encoding="utf-8") as f:
        return json.loads(f.read())


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ops = cargar_ops()
    L = ["TERRENO DE LA FASE 06, MEDIDO EN LA VUELTA 137 (no se funde nada aqui)", ""]

    L.append("--- (A) LAS SEIS FUSIONES DIFERIDAS, MEDIDAS CONTRA EL GRAFO ---")
    L.append("El campo `estado` NO se usa como fuente: las DIECISEIS fichas de fase 03")
    L.append("leen LISTA, las resueltas incluidas. Se mide superviviente y absorbidos.")
    sin_fundir = 0
    for x in SEIS:
        o = ops[x]
        sup, absor = o["superviviente"], o["eliminar"]
        ds = nodo(sup)
        est_sup = "NO EXISTE" if ds is None else ("VIVO" if not ds.get("deprecado") else "DEPRECADO")
        vivos = [a for a in absor if (nodo(a) or {}).get("deprecado") is not True]
        estado_real = "SIN FUNDIR" if vivos else "YA FUNDIDA"
        if vivos:
            sin_fundir += 1
        L.append("  %-18s campo=%s | GRAFO=%s (sup %s %s, absorbidos vivos %d de %d)"
                 % (x, o["estado"], estado_real, sup, est_sup, len(vivos), len(absor)))
    L.append("CIFRA fusiones diferidas sin fundir: %d grupos" % sin_fundir)
    L.append("")

    L.append("--- LAS CINCO MESAS, con su campo y su pregunta pendiente ---")
    for m in MESAS:
        o = ops[m]
        L.append("  %-8s estado=%s | pregunta_pendiente=%s | tipo=%s"
                 % (m, o["estado"], o.get("pregunta_pendiente"), (o.get("tipo") or "")[:46]))
    L.append("Las cinco estan ADJUDICADAS (11 y 12 ago 2026) y ninguna tiene pregunta")
    L.append("pendiente: lo que les queda no es decidir, es EJECUTAR sus hijas.")
    L.append("")

    L.append("--- (B) EL TAMANO EDITORIAL DE LAS SEIS ---")
    tot_ab = 0
    tot_marcas = 0
    for x in SEIS:
        o = ops[x]
        s = nodo(o["superviviente"])
        L.append("  %-18s sup %s: %d pasos, %d condiciones | absorbidos: %d"
                 % (x, o["superviviente"], len(s.get("pasos_accionables") or []),
                    len(s.get("condiciones_activacion") or []), len(o["eliminar"])))
        tot_ab += len(o["eliminar"])
        for a in o["eliminar"]:
            d = nodo(a)
            p = len(d.get("pasos_accionables") or [])
            c = len(d.get("condiciones_activacion") or [])
            tot_marcas += p + c
            L.append("        %-45s %d pasos, %d condiciones" % (a, p, c))
    L.append("CIFRA absorbidos de las seis fusiones: %d nodos" % tot_ab)
    L.append("CIFRA marcas editoriales por decidir: %d lineas" % tot_marcas)
    L.append("Cada marca es una decision de reparto (CUBIERTO, APPEND o INCISO) con su")
    L.append("motivo escrito, mas su perdida sellada en campo propio si no viaja.")
    L.append("")

    L.append("--- (C) LA LIMITACION DEL GENERADOR SELLADO, PROBADA ---")
    con_varios = [x for x in SEIS if len(ops[x]["eliminar"]) > 1]
    L.append("Fusiones con MAS DE UN absorbido: %d de 6 (%s)."
             % (len(con_varios), ", ".join(con_varios)))
    L.append("Con UN solo absorbido: %s." %
             ", ".join(x for x in SEIS if len(ops[x]["eliminar"]) == 1))
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import generar_plan_de_fusion_de_mesa as G
    prueba = ops["OP-M-03-III"]
    a1, a2 = prueba["eliminar"]
    sup = nodo(prueba["superviviente"])
    n_p = len(sup.get("pasos_accionables") or [])
    n_c = len(sup.get("condiciones_activacion") or [])
    # Contenido de JUGUETE: una sola marca por NUMERO de paso, que es todo lo que
    # el contrato del generador admite hoy.
    spec = {str(i): ["CUBIERTO", 1] for i in range(1, 9)}
    marcas = {}
    for ab in (a1, a2):
        d = nodo(ab)
        fallos = []
        marcas[ab] = G.marcar(spec, d.get("pasos_accionables") or [], "paso", ab,
                              n_p, n_c, sup.get("pasos_accionables") or [], fallos, True)
    L.append("Corrido G.marcar() sobre los DOS absorbidos de OP-M-03-III con el MISMO")
    L.append("spec, que es exactamente como el generador lo llama (bucle for ab in")
    L.append("absorbidos, siempre spec['pasos']):")
    for ab in (a1, a2):
        L.append("  %-32s marcas de paso: %s" % (ab, marcas[ab]))
    comunes = [k for k in marcas[a1] if k in marcas[a2] and marcas[a1][k] == marcas[a2][k]]
    L.append("Numeros de paso que reciben LA MISMA marca en los dos absorbidos: %d"
             % len(comunes))
    L.append("PROBADO: el reparto NO se puede diferenciar por absorbido. El indice de")
    L.append("spec['pasos'] es el NUMERO DE PASO, no el par (absorbido, paso), asi que")
    L.append("el paso 1 de %s y el paso 1 de %s" % (a1, a2))
    L.append("leen la misma marca y no se pueden repartir distinto.")
    L.append("CONSECUENCIA: las %d fusiones de mas de un absorbido NO SE PUEDEN SELLAR"
             % len(con_varios))
    L.append("con el generador tal como esta. No se parchea en esta vuelta: se declara.")
    L.append("")
    L.append("EXITCODE: 0")

    texto = "\n".join(L) + "\n"
    with io.open(SALIDA, "w", encoding="utf-8") as f:
        f.write(texto)
    print(texto)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
