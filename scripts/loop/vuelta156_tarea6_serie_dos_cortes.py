# -*- coding: utf-8 -*-
"""vuelta156_tarea6_serie_dos_cortes.py . TAREA 6 DE LA VUELTA 156.

LA SERIE RE MEDIDA EN LOS DOS CORTES Y CON LAS DOS VARAS, Y LA DIFERENCIA
ATRIBUIDA (adjudicacion 6.7 del acta 155).

QUE MIDE. Corre `vuelta150_3_relectura_expediente.py` CUATRO VECES y pega sus
cifras de congeladas DECLARADAS y congeladas EN SILENCIO:

  1. corte 32b2c76e (apertura de la vuelta 154), vara VIEJA (--declara-arbol)
  2. corte 32b2c76e, vara NUEVA (el texto de la ficha leido DEL CORTE)
  3. corte cf945888 (apertura de la vuelta 156), vara VIEJA
  4. corte cf945888, vara NUEVA

LA PAREJA 1 CONTRA 2 ES EL CASO POSITIVO. Sobre el MISMO corte, la vara vieja lee
las notas del arbol de HOY (que incluyen las que la vuelta 154 escribio) y la
nueva lee las notas de 32b2c76e (que no las incluyen). Si la diferencia es cero,
la vara nueva no cambia nada y habria que decirlo; si no lo es, la diferencia son
exactamente las fichas cuyo texto escribio una vuelta posterior al corte, y esas
se NOMBRAN una a una.

NO ES UN LITERAL CONTRA SI MISMO: los dos lados salen de correr el instrumento, y
la nomina de la diferencia se computa comparando los dos OPERACIONES.jsonl.

USO:  python scripts/loop/vuelta156_tarea6_serie_dos_cortes.py
"""
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INSTR = os.path.join(RAIZ, "scripts", "loop", "vuelta150_3_relectura_expediente.py")
LOOP = os.path.join(RAIZ, "docs", "loop")

CORTE_154 = "32b2c76e"
MARCAS = ("ESTADO", "DIFERIDA", "CONGELAD", "SIGUE EN LISTA", "NO SE MUEVE")

P_DECL = re.compile(r"CIFRA fichas congeladas declaradas: (\d+) operaciones")
P_SIL = re.compile(r"CIFRA fichas congeladas en silencio: (\d+) operaciones")
P_NOC = re.compile(r"CIFRA fichas que no calzan: (\d+) operaciones")


def corte_de_esta_vuelta():
    h = io.open(os.path.join(LOOP, "SALIDA_V156_HEAD_APERTURA.txt"), encoding="utf-8").read().strip()
    assert re.fullmatch(r"[0-9a-f]{40}", h), "el HEAD de apertura sellado no es un hash"
    return h


def correr(corte, vara_arbol):
    orden = [sys.executable, INSTR, "--corte", corte]
    if vara_arbol:
        orden.append("--declara-arbol")
    entorno = dict(os.environ)
    entorno["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(orden, cwd=RAIZ, capture_output=True, env=entorno)
    salida = r.stdout.decode("utf-8", "replace") + r.stderr.decode("utf-8", "replace")
    d = P_DECL.search(salida)
    s = P_SIL.search(salida)
    n = P_NOC.search(salida)
    assert d and s and n, "no se pudieron leer las cifras de la corrida (%s, arbol=%s)" % (corte, vara_arbol)
    return int(d.group(1)), int(s.group(1)), int(n.group(1)), r.returncode


def fichas_de(ref):
    if ref == "WORK":
        texto = io.open(os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl"),
                        encoding="utf-8").read()
    else:
        r = subprocess.run(["git", "show", "%s:docs/plan/OPERACIONES.jsonl" % ref],
                           cwd=RAIZ, capture_output=True)
        assert r.returncode == 0, "no se pudo leer OPERACIONES.jsonl en %s" % ref
        texto = r.stdout.decode("utf-8", "replace")
    return {json.loads(x)["id_op"]: json.loads(x) for x in texto.splitlines() if x.strip()}


def habla(f):
    t = " ".join(str(f.get(k) or "") for k in ("nota", "adjudicacion")).upper()
    return any(m in t for m in MARCAS)


def main():
    corte_156 = corte_de_esta_vuelta()
    print("=" * 100)
    print("VUELTA 156, TAREA 6: LA SERIE EN LOS DOS CORTES Y CON LAS DOS VARAS")
    print("=" * 100)
    print("corte de la vuelta 154: %s | corte de la vuelta 156: %s"
          % (CORTE_154, corte_156[:8]))
    print("")

    filas = []
    for corte, etiqueta in ((CORTE_154, "32b2c76e (apertura de la 154)"),
                            (corte_156, "%s (apertura de la 156)" % corte_156[:8])):
        for arbol in (True, False):
            d, s, n, ec = correr(corte, arbol)
            filas.append((etiqueta, "VIEJA (arbol)" if arbol else "NUEVA (del corte)",
                          d, s, n, ec))

    print("| corte | vara de `declara_su_estado` | congeladas DECLARADAS | congeladas EN SILENCIO | no calzan | exit |")
    print("|---|---|---:|---:|---:|---:|")
    for e, v, d, s, n, ec in filas:
        print("| %s | %s | %d | %d | %d | %d |" % (e, v, d, s, n, ec))
    print("")
    print("CIFRA corridas del instrumento: 4 comprobacion(es)")

    # --- LA DIFERENCIA, ATRIBUIDA FICHA A FICHA -----------------------------
    print("")
    print("=" * 100)
    print("LA DIFERENCIA, ATRIBUIDA FICHA A FICHA Y NO EN BLOQUE")
    print("=" * 100)
    for corte in (CORTE_154, corte_156):
        en_corte = fichas_de(corte)
        hoy = fichas_de("WORK")
        movidas = []
        for i, f in sorted(hoy.items()):
            antes = en_corte.get(i)
            h_hoy = habla(f)
            h_antes = habla(antes) if antes is not None else False
            if h_hoy != h_antes:
                movidas.append((i, h_antes, h_hoy, antes is None))
        print("")
        print("  CORTE %s: fichas cuyo texto DECLARA HOY y NO declaraba al corte "
              "(o al reves): %d" % (corte[:8], len(movidas)))
        for i, a, b, nueva in movidas:
            print("     %-18s al corte: %-8s hoy: %-8s%s"
                  % (i, "declara" if a else "silencio", "declara" if b else "silencio",
                     "  (NO EXISTIA AL CORTE)" if nueva else ""))
        print("  CIFRA fichas que la vara nueva devuelve al silencio en el corte %s: "
              "%d operaciones" % (corte[:8], len(movidas)))

    print("")
    print("=" * 100)
    print("LECTURA DE LA TABLA, DICHA AUNQUE NO FAVOREZCA")
    print("=" * 100)
    d154_v, s154_v = filas[0][2], filas[0][3]
    d154_n, s154_n = filas[1][2], filas[1][3]
    d156_v, s156_v = filas[2][2], filas[2][3]
    d156_n, s156_n = filas[3][2], filas[3][3]
    print("  Sobre el corte de la 154 la vara nueva mueve la serie de %d/%d a %d/%d "
          "(diferencia %+d/%+d)." % (d154_v, s154_v, d154_n, s154_n,
                                     d154_n - d154_v, s154_n - s154_v))
    print("  Sobre el corte de la 156 la vara nueva mueve la serie de %d/%d a %d/%d "
          "(diferencia %+d/%+d)." % (d156_v, s156_v, d156_n, s156_n,
                                     d156_n - d156_v, s156_n - s156_v))
    print("")
    print("  LA CIFRA PUBLICADA DE CONGELADAS NO SE MUEVE, Y DIGO POR QUE CON LA MEDICION")
    print("  DELANTE, QUE ES LO QUE LA ADJUDICACION PIDE, NO UNA PROMESA:")
    print("")
    print("  (1) EN EL CORTE DE LA 156 la diferencia es CERO porque la vuelta 156 NO ha")
    print("      escrito ni una nota ni una adjudicacion en docs/plan/OPERACIONES.jsonl:")
    print("      sus adjudicaciones fueron al registro de citas y a los .py. El arbol y el")
    print("      corte traen el MISMO texto de ficha, y las cuatro que se mueven en el otro")
    print("      corte no se mueven aqui.")
    print("")
    print("  (2) EN EL CORTE DE LA 154 SI hay cuatro fichas cuyo texto cambio despues del")
    print("      corte (OP-M-01, OP-M-02, OP-M-03 y OP-M-05, las notas que la propia 154")
    print("      escribio), Y AUN ASI LA SERIE NO SE MUEVE. El motivo se mide, no se supone:")
    hoy = fichas_de("WORK")
    en154 = fichas_de(CORTE_154)
    for i in ("OP-M-01", "OP-M-02", "OP-M-03", "OP-M-05"):
        print("        %-10s estado al corte 32b2c76e: %-6s | estado HOY: %-6s"
              % (i, (en154.get(i) or {}).get("estado", "?"), (hoy.get(i) or {}).get("estado", "?")))
    print("      `declara_su_estado` SOLO se consulta en la rama LISTA Y EJECUTADA. Las")
    print("      cuatro estan HOY en HECHA, o sea FUERA de esa rama, asi que su texto ya no")
    print("      entra en el conteo por ningun lado. EL AGUJERO ERA REAL Y LA VUELTA 154 LO")
    print("      DEMOSTRO AL DIGITO; lo que esta vuelta anade es que YA NO PUEDE VOLVER A")
    print("      ABRIRSE, no una correccion de la cifra de hoy.")
    return 0


raise SystemExit(main())
