# -*- coding: utf-8 -*-
"""vuelta148_2a_mutacion_nomina_commiteada.py . PRUEBA DE MUTACION del LADO DEL
COMMIT de la guarda de la nomina (TAREA 2.1 de la vuelta 148, sobre la caida
4.4.a del acta 147).

EL AGUJERO QUE SE REPRODUCE, TAL COMO EL AUDITOR LO PROBO. La guarda comparaba
el arbol de trabajo contra `HEAD`. Si el re-sellado de la nomina llegaba YA
COMMITEADO, los dos lados decian lo mismo y la guarda no veia nada: el ataque
que su propio docstring describe (regenerar la nomina para hacer callar a Gate
0) seguia abierto entero con solo dar un `git commit` de por medio.

EL CASO CENTRAL ES EL 2: `texto_hoy` y `texto_head` SON EL MISMO TEXTO, los dos
mutados. Contra HEAD no hay ninguna diferencia que ver. Lo unico que delata el
movimiento es el ANCLA DE LA VUELTA, y por eso la guarda tiene que caer.

LA MUTACION VA SOBRE VARIABLE COMPUTADA (EJECUTOR 1): el sujeto se ELIGE del
contenido real de la nomina (la primera entrada por orden), no se teclea, y el
texto mutado se fabrica a partir del texto real. Nada de esto toca el disco:
los tres textos se le pasan a `verificar` en memoria, y el arnes comprueba que
`dataset/` queda identico.

USO:
  python scripts/loop/vuelta148_2a_mutacion_nomina_commiteada.py
"""
import hashlib
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import verificar_nomina_sellada as G

REPORTE_MUDO = "Un reporte que no dice nada de la nomina.\n"


def huella_de_dataset():
    h = hashlib.sha256()
    base = os.path.join(RAIZ, "dataset")
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames.sort()
        for nombre in sorted(filenames):
            ruta = os.path.join(dirpath, nombre)
            h.update(os.path.relpath(ruta, RAIZ).replace(os.sep, "/").encode("utf-8"))
            with open(ruta, "rb") as f:
                h.update(f.read())
    return h.hexdigest()


def main():
    fallos = []
    huella_antes = huella_de_dataset()

    texto_real = io.open(G.RUTA_NOMINA, encoding="utf-8").read()
    datos = json.loads(texto_real)
    adjudicados = datos["adjudicados"]
    print("NOMINA REAL: %d entrada(s), leidas de %s" % (len(adjudicados), G.RUTA_NOMINA_REL))

    # EL SUJETO SE ELIGE POR COMPUTO, no se teclea.
    elegido = sorted(x["node_id"] for x in adjudicados)[0]
    print("SUJETO ELEGIDO POR COMPUTO (el primero por orden): %s" % elegido)

    def texto_sin(nid):
        d = json.loads(texto_real)
        d["adjudicados"] = [x for x in d["adjudicados"] if x["node_id"] != nid]
        return json.dumps(d, ensure_ascii=False, indent=2)

    def texto_con_entrada_de_mas(nid_nuevo):
        d = json.loads(texto_real)
        plantilla = json.loads(json.dumps(d["adjudicados"][0]))
        plantilla["node_id"] = nid_nuevo
        d["adjudicados"].append(plantilla)
        return json.dumps(d, ensure_ascii=False, indent=2)

    ancla_hash, asunto = G.ancla_de_la_vuelta()
    texto_ancla = G.nomina_en(ancla_hash)
    print("ANCLA DE LA VUELTA, LEIDA DE GIT: %s '%s'" % (ancla_hash[:8], asunto[:60]))
    if texto_ancla is None:
        print("ARNES ROTO: no se pudo leer la nomina del ancla")
        return 1

    # ---------------------------------------------------------------
    # CASO 1. VERDE DE CONTROL: nada se movio en ningun lado.
    # ---------------------------------------------------------------
    ok1, fallos1, det1 = G.verificar(texto_real, texto_real, REPORTE_MUDO, texto_real)
    print("")
    print("CASO 1 (nada se movio): ok=%s, fallos=%d" % (ok1, len(fallos1)))
    if not ok1:
        fallos.append("CASO 1: sin movimiento deberia salir VERDE y salio ROJO: %s" % fallos1)

    # ---------------------------------------------------------------
    # CASO 2. EL AGUJERO. Arbol y HEAD IDENTICOS y los dos movidos: el
    # re-sellado llego YA COMMITEADO. La guarda vieja no veia nada.
    # ---------------------------------------------------------------
    movido = texto_sin(elegido)
    ok2, fallos2, det2 = G.verificar(movido, movido, REPORTE_MUDO, texto_ancla)
    print("")
    print("CASO 2 (EL AGUJERO: arbol y HEAD identicos, los dos movidos): ok=%s, fallos=%d"
          % (ok2, len(fallos2)))
    for f in fallos2:
        print("   | %s" % f[:200])
    if ok2:
        fallos.append("CASO 2: LA GUARDA SIGUE CIEGA al movimiento que llega ya commiteado")
    if not any(elegido in f for f in fallos2):
        fallos.append("CASO 2: la guarda cayo pero NO nombra %s" % elegido)
    if not any("YA COMMITEADOS" in f for f in fallos2):
        fallos.append("CASO 2: la guarda no dice que el movimiento llego ya commiteado")

    # LA COMPROBACION QUE HACE HONESTO AL CASO 2: contra HEAD, de verdad, NO
    # habia nada que ver. Si aqui saliera diferencia, el caso 2 estaria
    # cayendo por el camino viejo y no probaria nada.
    e_h, s_h, c_h = G.diferencias(G._adjudicados(movido), G._adjudicados(movido))
    print("   contra HEAD, diferencias: %d entran, %d salen, %d cambian (tienen que ser 0)"
          % (len(e_h), len(s_h), len(c_h)))
    if e_h or s_h or c_h:
        fallos.append("CASO 2: contra HEAD SI habia diferencia, asi que el caso no prueba "
                      "el lado del commit")

    # ---------------------------------------------------------------
    # CASO 3. EL MISMO MOVIMIENTO, DECLARADO EN EL REPORTE: pasa.
    # La guarda no impide re-sellar, impide re-sellar CALLANDO.
    # ---------------------------------------------------------------
    reporte_declarado = ("%s\nSe retira %s de la nomina por lo que sea.\n"
                         % (G.MARCA_DECLARACION, elegido))
    ok3, fallos3, det3 = G.verificar(movido, movido, reporte_declarado, texto_ancla)
    print("")
    print("CASO 3 (el mismo movimiento, DECLARADO): ok=%s, fallos=%d" % (ok3, len(fallos3)))
    if not ok3:
        fallos.append("CASO 3: declarado con marca y node_id deberia pasar y no paso: %s"
                      % fallos3)

    # ---------------------------------------------------------------
    # CASO 4. DECLARADO A MEDIAS: la marca sin el node_id NO basta.
    # ---------------------------------------------------------------
    ok4, fallos4, _ = G.verificar(movido, movido, G.MARCA_DECLARACION + "\n", texto_ancla)
    print("CASO 4 (marca sin nombrar el node_id): ok=%s, fallos=%d" % (ok4, len(fallos4)))
    if ok4:
        fallos.append("CASO 4: la marca sola basto; el node_id tiene que nombrarse")

    # ---------------------------------------------------------------
    # CASO 5. UNA ENTRADA QUE ENTRA YA COMMITEADA (el ataque real: la
    # nomina CRECE para que Gate 0 se calle).
    # ---------------------------------------------------------------
    colado = "nodo_colado_en_la_nomina_v148"
    crecida = texto_con_entrada_de_mas(colado)
    ok5, fallos5, _ = G.verificar(crecida, crecida, REPORTE_MUDO, texto_ancla)
    print("CASO 5 (una entrada COLADA, ya commiteada): ok=%s, fallos=%d" % (ok5, len(fallos5)))
    if ok5:
        fallos.append("CASO 5: una entrada colada y commiteada paso sin declararse")
    if not any(colado in f for f in fallos5):
        fallos.append("CASO 5: la guarda no nombra la entrada colada %s" % colado)

    # ---------------------------------------------------------------
    # CASO 6. SIN ANCLA NO HAY VERDE. Se simula que git no halla acta.
    # ---------------------------------------------------------------
    real = G.ancla_de_la_vuelta
    G.ancla_de_la_vuelta = lambda: (None, "simulacion del arnes: rama sin acta")
    try:
        ok6, fallos6, _ = G.verificar(texto_real, texto_real, REPORTE_MUDO, None)
    finally:
        G.ancla_de_la_vuelta = real
    print("CASO 6 (sin ancla): ok=%s, fallos=%d" % (ok6, len(fallos6)))
    if ok6:
        fallos.append("CASO 6: sin ancla dio VERDE, o sea un verde por no haber podido mirar")

    huella_despues = huella_de_dataset()
    print("")
    print("HUELLA dataset/ antes:   %s" % huella_antes)
    print("HUELLA dataset/ despues: %s" % huella_despues)
    if huella_antes != huella_despues:
        fallos.append("dataset/ CAMBIO durante el arnes")
    else:
        print("dataset/ IDENTICO: el arnes no escribio un byte.")

    print("")
    if fallos:
        print("ROJO, el lado del commit NO esta cerrado (%d):" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("VERDE: los seis casos se comportan. EL AGUJERO ESTA CERRADO: con arbol y HEAD")
    print("identicos y los dos movidos, la guarda CAE, nombra el node_id y dice que el")
    print("movimiento llego YA COMMITEADO. Declararlo sigue bastando; la marca sola no; una")
    print("entrada colada tampoco pasa; y sin ancla no hay verde.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
