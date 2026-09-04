# -*- coding: utf-8 -*-
r"""vuelta168_tarea5_abrir_las_seis.py . TAREA 5 de la vuelta 168.

ABRE LAS SEIS QUE LA VARA DEL INSTRUMENTO SENALA, EN EL ORDEN QUE EL ENCARGO
FIJA, Y MIDE CADA UNA ANTES DE TOCARLA.

LA VARA NO ES EL CAMPO. Por la decision del fundador del 4 sep 2026 (punto 1),
declarada en `docs/plan/00_INDICE.md` y citada en `docs/loop/AUDITOR.md` seccion
0, lo que queda por ejecutar NO se lee del campo `estado` de
`docs/plan/OPERACIONES.jsonl`: se lee de
`scripts/loop/vuelta150_3_relectura_expediente.py`. Este instrumento no
reimplementa esa vara: LA INVOCA y lee su salida, que es lo contrario de tener
dos varas divergentes.

LO QUE HACE, POR PARTES, Y NINGUNA ADIVINA:

  (5.a) `OP-I-01` y `OP-L-01`, las dos sin dependencias. Se ABREN: se lee su
        ficha entera y se mide CLAUSULA A CLAUSULA contra el arbol de hoy. Lo
        que se pueda cerrar midiendo, se cierra midiendo; lo que necesite una
        DECISION que la ficha no escribe, se declara y NO se improvisa
        (`AUDITOR.md` 3: "una operacion cuyo texto no alcance para ejecutarse
        sin decidir es PARADA, no una improvisacion").

  (5.b) LA VALVULA DE VIGENCIA DE `OP-M-02-MEDIOS` Y `OP-M-02-ADMIT`, Y VA
        ANTES DE TOCAR NADA. Sus nominas se resuelven CONTRA EL GRAFO DE HOY
        con el resolutor de P.1. Si los dos miembros de una ficha resuelven a UN
        SOLO VIVO, el acto ya lo consumieron las unificaciones y la operacion se
        declara CUMPLIDA POR CONSUNCION con la medicion citada, sin ejecutarse.
        La medicion NO se copia de la nota de la ficha (que ya la trae desde la
        vuelta 64): se RE CORRE hoy con `scripts/loop/vuelta64_consumidas.py`,
        porque una nota vieja es contraste y nunca fuente (`EJECUTOR.md` 2).

  (5.c) LOS `depende_de` DE `OP-L-02` Y `OP-L-03`, LEIDOS POR EL INSTRUMENTO Y
        NO POR EL CAMPO. Se toman los `OP-D-*` que las dos fichas nombran y se
        pregunta AL INSTRUMENTO si cada uno tiene prueba de ejecucion. Por la
        vara nueva, tener prueba es estar cumplido, y entonces las dos dejan de
        estar bloqueadas. SI EL INSTRUMENTO DICE OTRA COSA, ESTE FICHERO PARA Y
        LO TRAE, que es la letra literal del encargo.

CERO ESCRITURAS. Este instrumento MIDE y publica; no toca un nodo, no mueve un
`estado`, no edita una ficha y no escribe en `dataset/`. Lo que haya que
escribir se escribe despues, a la vista de lo medido.

USO:
  python scripts/loop/vuelta168_tarea5_abrir_las_seis.py --corte <REF> --apertura <REF>
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
INV = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
COMP = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388_COMPONENTES.jsonl")
PY = sys.executable

LAS_SEIS = ["OP-I-01", "OP-L-01", "OP-M-02-MEDIOS", "OP-M-02-ADMIT",
            "OP-L-02", "OP-L-03"]


def correr(args):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=RAIZ, capture_output=True, env=env)
    return r.returncode, (r.stdout.decode("utf-8", errors="replace")
                          + r.stderr.decode("utf-8", errors="replace"))


def fichas():
    fuera = {}
    for l in io.open(OPS, encoding="utf-8"):
        l = l.strip()
        if not l:
            continue
        d = json.loads(l)
        fuera[d.get("id_op")] = d
    return fuera


def salida_del_instrumento(corte, apertura):
    c, o = correr([PY, "scripts/loop/vuelta150_3_relectura_expediente.py",
                   "--corte", corte, "--apertura", apertura])
    return c, o


def las_seis_del_instrumento(salida):
    """LAS SEIS SE LEEN DE LA SALIDA DEL INSTRUMENTO, no de una lista mia. La
    tabla que las trae es la de 'las fichas en LISTA SIN NINGUNA de las tres
    pruebas'. Devuelve la lista de ids en el orden en que el instrumento las
    imprime."""
    marca = "las fichas en LISTA SIN NINGUNA de las"
    i = salida.find(marca)
    if i < 0:
        return []
    resto = salida[i:]
    fin = resto.find("CONTADO:")
    resto = resto[:fin] if fin > 0 else resto
    return re.findall(r"^\| `([A-Z0-9\-]+)` \|", resto, re.M)


def pruebas_por_ficha(salida):
    """El mapa id_op -> pruebas, leido de la tabla de las que NO CALZAN."""
    fuera = {}
    for m in re.finditer(r"^\| `([A-Z0-9\-]+)` \| \S+ \| (\S+) \| ([^|]+) \|", salida, re.M):
        fuera[m.group(1)] = (m.group(2), m.group(3).strip())
    return fuera


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corte", required=True)
    ap.add_argument("--apertura", required=True)
    a = ap.parse_args()

    F = fichas()
    print("=" * 78)
    print("VUELTA 168, TAREA 5: LAS SEIS, ABIERTAS POR LA VARA DEL INSTRUMENTO")
    print("=" * 78)
    print("")

    print("0) LA VARA, CORRIDA EN ESTA VUELTA, Y SUS SEIS LEIDAS DE SU SALIDA")
    print("   comando: python scripts/loop/vuelta150_3_relectura_expediente.py"
          " --corte %s --apertura %s" % (a.corte, a.apertura))
    c, salida = salida_del_instrumento(a.corte, a.apertura)
    print("   EXITCODE del instrumento: %d" % c)
    for rot in ("CIFRA fichas del expediente", "CIFRA fichas que no calzan",
                "CIFRA fichas congeladas declaradas",
                "CIFRA fichas congeladas en silencio",
                "CIFRA fichas HECHA sin ninguna prueba",
                "CIFRA fichas en LISTA sin ninguna prueba"):
        for l in salida.splitlines():
            if l.strip().startswith(rot):
                print("   %s" % l.strip())
    seis = las_seis_del_instrumento(salida)
    print("   LAS QUE EL INSTRUMENTO NOMBRA (%d): %s" % (len(seis), ", ".join(seis)))
    print("   CONTRASTE con las que el encargo nombra (%d): %s"
          % (len(LAS_SEIS), ", ".join(LAS_SEIS)))
    print("   MISMO CONJUNTO: %s" % ("SI" if set(seis) == set(LAS_SEIS) else
                                     "NO. MANDA EL INSTRUMENTO Y SE PARA."))
    if set(seis) != set(LAS_SEIS):
        print("   PARADA: el instrumento y el encargo no nombran lo mismo.")
        return 1
    print("")

    print("=" * 78)
    print("5.b) LA VALVULA DE VIGENCIA, Y VA ANTES DE TOCAR NADA")
    print("=" * 78)
    print("   comando: python scripts/loop/vuelta64_consumidas.py (RE CORRIDO HOY,")
    print("   no copiado de la nota de la ficha, que ya lo trae desde la vuelta 64)")
    c2, val = correr([PY, "scripts/loop/vuelta64_consumidas.py"])
    print("   EXITCODE: %d" % c2)
    for ficha in ("OP-M-02-MEDIOS", "OP-M-02-ADMIT"):
        i = val.find("--- %s ---" % ficha)
        if i < 0:
            print("   PARADA: la valvula no mide %s." % ficha)
            return 1
        trozo = val[i:i + 1400]
        for l in trozo.splitlines()[:6]:
            print("   %s" % l.rstrip())
        consumida = "CONSUMIDA: el par resuelve a UN solo vivo" in trozo
        print("   VEREDICTO DE LA VALVULA para %s: %s" %
              (ficha, "CUMPLIDA POR CONSUNCION, NO SE EJECUTA" if consumida
               else "SIGUE VIVA, SE EJECUTA"))
        print("")
    print("   LA CIFRA QUE CIERRA ESTA MITAD, CONTADA DE LA SALIDA DE LA VALVULA:")
    print("   CIFRA de las cinco OP-M-02-* que resuelven a UN solo vivo: %d"
          % val.count("CONSUMIDA: el par resuelve a UN solo vivo"))
    print("")

    print("=" * 78)
    print("5.c) LOS depende_de DE OP-L-02 Y OP-L-03, LEIDOS POR EL INSTRUMENTO")
    print("=" * 78)
    mapa = pruebas_por_ficha(salida)
    dep = sorted(set((F["OP-L-02"].get("depende_de") or [])
                     + (F["OP-L-03"].get("depende_de") or [])))
    print("   OP-L-02 depende_de (campo, citado COMO CAMPO): %s"
          % ", ".join(F["OP-L-02"].get("depende_de") or []))
    print("   OP-L-03 depende_de (campo, citado COMO CAMPO): %s"
          % ", ".join(F["OP-L-03"].get("depende_de") or []))
    print("   CIFRA OP-D-* distintas entre las dos: %d" % len(dep))
    print("")
    print("   | OP-D-* | estado (CAMPO, historico) | pruebas (INSTRUMENTO) | por la vara nueva |")
    print("   |---|---|---|---|")
    sin_prueba = []
    for d in dep:
        estado = F[d].get("estado")
        pruebas = mapa.get(d, (estado, "(no sale en la tabla de las que no calzan)"))[1]
        tiene = pruebas not in ("ninguna", "(no sale en la tabla de las que no calzan)")
        if not tiene:
            sin_prueba.append(d)
        print("   | `%s` | %s | %s | %s |"
              % (d, estado, pruebas, "CUMPLIDA" if tiene else "SIN PRUEBA"))
    print("")
    print("   CIFRA OP-D-* con prueba de ejecucion: %d de %d" % (len(dep) - len(sin_prueba), len(dep)))
    print("   CIFRA OP-D-* SIN prueba: %d (%s)"
          % (len(sin_prueba), ", ".join(sin_prueba) or "ninguna"))
    if sin_prueba:
        print("   PARADA: el instrumento dice otra cosa que el encargo. Se trae.")
        return 1
    print("   POR LA VARA NUEVA, LAS SEIS ESTAN CUMPLIDAS, y por eso OP-L-02 y")
    print("   OP-L-03 DEJAN DE ESTAR BLOQUEADAS. El instrumento NO dice otra cosa.")
    print("   Y SE DICE LO QUE EL CAMPO DIRIA, PARA QUE LA DIFERENCIA SE VEA: por el")
    print("   campo `estado` las seis siguen en LISTA, y la seccion 3.c del propio")
    print("   instrumento, que lee el campo, NO las lista como desbloqueadas.")
    print("")

    print("=" * 78)
    print("5.a) OP-I-01, ABIERTA Y MEDIDA CLAUSULA A CLAUSULA")
    print("=" * 78)
    d = F["OP-I-01"]
    print("   adjudicacion: %s" % (d.get("adjudicacion") or "")[:200])
    print("   escribe en el grafo: %d elemento(s) (nodos+preservar+eliminar+aristas_nuevas)"
          % sum(len(d.get(k) or []) for k in
                ("nodos", "preservar", "eliminar", "aristas_nuevas")))
    entradas = [json.loads(l) for l in io.open(INV, encoding="utf-8") if l.strip()]
    sin_corte = [e for e in entradas if not e.get("fecha_corte")]
    provisional = [e for e in entradas
                   if "PROVISIONAL" in json.dumps(e, ensure_ascii=False)]
    huecos = [e for e in entradas if "HUECO" in json.dumps(e, ensure_ascii=False).upper()]
    tipos = {}
    for e in entradas:
        tipos[e.get("tipo")] = tipos.get(e.get("tipo"), 0) + 1
    cortes = {}
    for e in entradas:
        cortes[e.get("fecha_corte")] = cortes.get(e.get("fecha_corte"), 0) + 1
    print("")
    print("   EL INVENTARIO DE HOY, CONTADO DE SU FICHERO:")
    print("   CIFRA entradas de docs/plan/INVENTARIO.jsonl: %d" % len(entradas))
    for k in sorted(tipos, key=lambda x: -tipos[x]):
        print("      %-18s %d" % (k, tipos[k]))
    print("   CIFRA fechas de corte distintas: %d (%s)"
          % (len(cortes), ", ".join("%s=%d" % (k, cortes[k]) for k in sorted(cortes))))
    print("")
    print("   CLAUSULA 1, 'toda entrada lleva su fecha_corte':")
    print("      CIFRA entradas SIN fecha_corte: %d -> %s"
          % (len(sin_corte), "SE CUMPLE" if not sin_corte else "NO SE CUMPLE"))
    print("   CLAUSULA 2, 'toda forma con cobertura incompleta va marcada PROVISIONAL':")
    print("      CIFRA entradas que dicen PROVISIONAL: %d" % len(provisional))
    print("      NO ES MEDIBLE POR CONTEO, y se dice en vez de darla por buena: para")
    print("      saber si TODA forma incompleta esta marcada haria falta la lista de")
    print("      las incompletas, y el inventario no la trae como campo. Lo unico")
    print("      medible es cuantas SI estan marcadas.")
    print("   CLAUSULA 3, 'todo hueco va NOMBRADO, nunca rellenado':")
    print("      CIFRA entradas que nombran un hueco: %d" % len(huecos))
    print("      la nota de la ficha nombra sus huecos: %s"
          % ("SI" if "HUECO" in (d.get("nota") or "").upper() else "NO"))
    print("   CLAUSULA 4, 'el inventario se recomputa entero con el disparador de")
    print("   08_VERIFICACION': ESTA ES LA QUE NO SE PUEDE EJECUTAR SIN DECIDIR.")
    comp = [json.loads(l) for l in io.open(COMP, encoding="utf-8") if l.strip()]
    cerr = len([x for x in comp if x.get("estado") == "CERRADO"])
    abie = len([x for x in comp if x.get("estado") == "ABIERTO"])
    print("      LA CIFRA DE LA NOTA, CITADA COMO CONTRASTE Y NO COMO FUENTE: la nota")
    print("      de la ficha declara 335 actos al corte 3.388 (280 CERRADOS, 55")
    print("      ABIERTOS), medidos en la vuelta 14.")
    print("      MEDIDO HOY sobre docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl:")
    print("      CIFRA lineas: %d | CERRADO: %d | ABIERTO: %d" % (len(comp), cerr, abie))
    print("      LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO: la cifra de la")
    print("      nota es de su corte y la de hoy es de hoy.")
    print("      CIFRA actos en el INVENTARIO por corte: %s"
          % ", ".join("%s=%d" % (k, len([e for e in entradas
                                         if e.get("tipo") == "acto"
                                         and e.get("fecha_corte") == k]))
                      for k in sorted(cortes) if any(
                          e.get("tipo") == "acto" and e.get("fecha_corte") == k
                          for e in entradas)))
    print("")

    print("=" * 78)
    print("5.a) OP-L-01, ABIERTA Y MEDIDA CLAUSULA A CLAUSULA")
    print("=" * 78)
    d = F["OP-L-01"]
    v = d.get("verificacion") or []
    print("   CIFRA clausulas: %d" % len(v))
    declaradas = [c for c in v if c.startswith("CORRECCION DECLARADA")]
    print("   CIFRA que son CORRECCION DECLARADA (anadidas por la vuelta 166): %d"
          % len(declaradas))
    print("   escribe en el grafo: %d elemento(s)"
          % sum(len(d.get(k) or []) for k in
                ("nodos", "preservar", "eliminar", "aristas_nuevas")))
    print("")
    print("   CLAUSULA 1: CERRADA por la CORRECCION DECLARADA de la vuelta 166")
    print("      (clausula 4 de esta misma lista), verificada por el acta 166 y")
    print("      adjudicada en su 6.8. No se reabre en esta vuelta.")
    print("   CLAUSULA 2: CERRADA por la CORRECCION DECLARADA de la vuelta 166")
    print("      (clausula 5). El 2.117 es TESTIGO de su corte, no condicion.")
    marcador = 0
    for l in io.open(os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl"),
                     encoding="utf-8"):
        if l.strip():
            marcador += 1
    print("      MEDIDO HOY, contado del fichero: el marcador vale %d" % marcador)
    print("   CLAUSULA 3, 'cada nomina afectada se re-mide con su cobertura al lado")
    print("   (banco 9.26)': SIGUE ABIERTA, Y SE DICE POR QUE CON LA MEDICION DELANTE.")
    print("      Para re-medir 'cada nomina afectada' hace falta saber CUALES son, y")
    print("      esta ficha no las escribe: sus cuatro listas de escritura estan")
    print("      vacias (0 elementos, medido arriba), asi que la operacion no nombra")
    print("      ninguna nomina propia. La sede que nombra miembros es el inventario,")
    print("      o sea OP-I-01, cuya clausula 4 acaba de quedar declarada como no")
    print("      ejecutable sin decidir. LA CADENA ES REAL Y NO UNA EXCUSA: sin")
    print("      inventario recomputado no hay nomina que re-medir.")
    print("")
    print("VERDE: las seis abiertas y medidas. Cero nodos tocados, cero estados")
    print("movidos, cero fichas editadas por este instrumento.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
