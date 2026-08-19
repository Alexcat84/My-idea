# -*- coding: utf-8 -*-
"""vuelta40_costuras_opd05.py - QUE DICE EL INSTRUMENTO YA VIVO de los tres
nodos de OP-D-05, y el texto entero delante para la lectura.

ESTRICTAMENTE DE SOLO LECTURA. No toca un nodo, no toca el instrumento, no
regenera ninguna cola: LEE LA COLA QUE EL INSTRUMENTO YA ENTREGO.

LA DIFERENCIA CON `vuelta34_costuras_opd03.py`, y es la razon de que este exista.
Aquel tuvo que REIMPLEMENTAR las senales copiadas del instrumento, porque el
instrumento sellado se negaba a entregar y a ser importado con la puerta roja, y
lo decia en cada linea de su salida. ESO SE ACABO: la puerta se reparo en la
PARTE A de esta vuelta y el instrumento entrega con exit 0, asi que aqui NO se
recalcula ni una cifra. Lo que se lee es `docs/COSTURAS_INTERNAS.jsonl`, que es
LA COLA DEL INSTRUMENTO, y punto.

LAS TRES COSAS QUE SEPARA, porque confundirlas es lo que ha parado vueltas:

  (a) LA NOMINA. El plan sellado de `OP-D-05` (docs/plan/02_DESTEJIDOS.md) NO
      nombra ninguna costura, al contrario que `OP-D-03`, que nombraba tres por
      su id. Este script COMPRUEBA esa ausencia contra el fichero en vez de
      fiarse de que alguien lo leyo, porque de ella depende que el destejido de
      esta operacion se decida por lectura y no por nomina heredada.
  (b) QUE CITA EL INSTRUMENTO. Cada uno de los tres, dentro o fuera de la cola
      entregada, con su ficha entera si esta dentro. EL INSTRUMENTO CITA Y NO
      JUZGA: estar en la cola no es una costura probada.
  (c) EL TEXTO ENTERO de los tres nodos, que es lo unico que decide. Con la
      cita del instrumento delante, como manda el encargo, y con `P.11` a mano
      para separar advertencia de procedimiento.

Uso: python scripts/loop/vuelta40_costuras_opd05.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
COLA = os.path.join(RAIZ, "docs", "COSTURAS_INTERNAS.jsonl")
DESTEJIDOS = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")

ACTO = ["seleccion_ceo_fundador",
        "asignacion_de_titulos_ejecutivos",
        "errores_comunes_asignacion_roles"]


def raya(t):
    print("")
    print("=" * 78)
    print(t)
    print("=" * 78)


def main():
    raya("(a) LA NOMINA: QUE NOMBRA EL PLAN SELLADO DE OP-D-05, comprobado")
    md = io.open(DESTEJIDOS, encoding="utf-8").read()
    ini = md.index("## `OP-D-05`")
    fin = md.index("## `OP-D-06`", ini)
    seccion = md[ini:fin]
    print("  LA SECCION ENTERA, citada literal:")
    for linea in seccion.rstrip().split("\n"):
        print("  | " + linea)
    print("")
    print("  contiene la palabra 'Costuras:' : %s"
          % ("SI" if "Costuras:" in seccion else "NO"))
    print("  nombra alguno de los tres por su id como costura:")
    for nid in ACTO:
        print("    %-40s aparece en la seccion: %s"
              % (nid, "SI" if nid in seccion else "NO"))
    print("")
    print("  LECTURA: el plan LISTA los tres nodos del acto y sus tres pares, y")
    print("  NO declara ninguna costura por su id. Contra OP-D-03, cuyo plan si")
    print("  escribia 'Costuras: ab_testing_optimizacion, ...'. O sea que aqui")
    print("  el destejido NO viene dado por el plan: lo decide la lectura, con")
    print("  la cita del instrumento delante.")

    raya("(b) QUE CITA EL INSTRUMENTO YA VIVO, leido de su cola entregada")
    cola = {}
    for l in io.open(COLA, encoding="utf-8"):
        if l.strip():
            f = json.loads(l)
            cola[f["node_id"]] = f
    print("  fichero leido : %s" % os.path.relpath(COLA, RAIZ).replace("\\", "/"))
    print("  citas en la cola: %d" % len(cola))
    print("")
    for nid in ACTO:
        f = cola.get(nid)
        print("  %s" % nid)
        if not f:
            print("      NO ESTA EN LA COLA. El instrumento no lo cita.")
            print("")
            continue
        por = []
        if f["disparo_pareja"]:
            por.append("pareja")
        if f["disparo_bloque"]:
            por.append("bloque")
        print("      CITADO POR: %s" % " y ".join(por))
        print("      pasos %d | pareja %.1f (pasos %d y %d) | bloque %s | corte tras %s"
              % (f["pasos"], f["sim_pareja"], f["pareja"][0], f["pareja"][1],
                 f["sim_bloque_texto"], f["corte"]))
        print("      franja 44 a 45: %s" % ("SI" if f["franja_44_45"] else "NO"))
        print("      LA PAREJA QUE CITA, literal:")
        print("        paso %d: %s" % (f["pareja"][0], f["paso_a"]))
        print("        paso %d: %s" % (f["pareja"][1], f["paso_b"]))
        print("")
    fuera = [n for n in ACTO if n not in cola]
    dentro = [n for n in ACTO if n in cola]
    print("  RESUMEN: CITADOS %d de 3 (%s). NO CITADOS: %s"
          % (len(dentro), ", ".join(dentro) or "ninguno", ", ".join(fuera) or "ninguno"))
    print("  Y LO QUE ESO NO DICE: el instrumento CITA Y NO JUZGA. Una cita es")
    print("  una lectura obligada, no una costura probada; y un silencio suyo no")
    print("  es un certificado de sanidad (su propio encabezado declara el limite")
    print("  del comparador de tokens, que no ve equivalencias semanticas).")

    raya("(c) EL TEXTO ENTERO DE LOS TRES, que es lo que decide")
    for nid in ACTO:
        n = json.loads(io.open(os.path.join(NODOS, nid + ".json"),
                               encoding="utf-8").read())
        print("")
        print("-" * 78)
        print("%s   [%s]" % (nid, n.get("dominio")))
        print("-" * 78)
        print("  titulo    : %s" % n.get("titulo_concepto"))
        print("  fuente    : %s" % n.get("fuente"))
        print("  vivo      : %s" % (not n.get("deprecado")))
        print("  resumen   : %s" % (n.get("resumen_ejecutivo") or "")[:600])
        print("  entregable: %s" % n.get("entregable_esperado"))
        print("  PASOS (%d):" % len(n.get("pasos_accionables") or []))
        for i, p in enumerate(n.get("pasos_accionables") or [], 1):
            print("    %2d. %s" % (i, p))
        print("  CONDICIONES DE ACTIVACION (%d):"
              % len(n.get("condiciones_activacion") or []))
        for c in (n.get("condiciones_activacion") or []):
            print("    - %s" % c)
        print("  nodos_previos   : %s" % (n.get("nodos_previos") or []))
        print("  nodos_siguientes: %s" % (n.get("nodos_siguientes") or []))
    print("")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
