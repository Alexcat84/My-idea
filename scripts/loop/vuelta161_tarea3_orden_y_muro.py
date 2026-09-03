# -*- coding: utf-8 -*-
"""vuelta161_tarea3_orden_y_muro.py . TAREA 3 DE LA VUELTA 161.

SIGUE EL ORDEN ESCRITO EN MODO CONTINUO Y MIDE DONDE SE PARA. El encargo dice
que el orden se sigue HASTA EL MURO CONOCIDO Y YA ADJUDICADO (acta 149, seccion
3.10): la fase 08 no cierra sin una SESION CON CREDENCIAL Y CON EL FUNDADOR
DELANTE, porque el `.env` esta fuera del repo mientras el bucle corre, y eso
esta bien.

ESTE INSTRUMENTO NO CIERRA NINGUNA FASE Y NO TOCA NINGUN NODO. Hace tres cosas,
y las tres son medicion:

  (A) LEE EL ORDEN DE SU FICHERO. Las fases y su orden salen de
      `docs/plan/00_INDICE.md` y de los nombres de fase de
      `docs/plan/OPERACIONES.jsonl`, nunca de una lista tecleada aqui.

  (B) RECORRE EL ORDEN Y SE PARA EN LA PRIMERA FASE QUE NO CIERRA, nombrando
      sus operaciones sin cumplir una a una. Las cifras salen de
      `tallar_estado_de_fase.py`, que es el instrumento de la casa para esto.

  (C) MIDE EL MURO EN VEZ DE CITARLO DE MEMORIA: comprueba que el `.env` NO
      existe en el arbol, que ESTA en `.gitignore`, y CORRE la prueba de rumbos
      para ver si falla visible. La cita del acta 149 se lee de su linea.

USO:  python scripts/loop/vuelta161_tarea3_orden_y_muro.py
"""
import io
import os
import re
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
INDICE = os.path.join(RAIZ, "docs", "plan", "00_INDICE.md")
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
LINEA_ACTA_149 = 50182


def fases_del_fichero():
    """Los nombres de fase, leidos de OPERACIONES.jsonl y ordenados por su
    prefijo numerico, que es el orden escrito del plan."""
    nombres = set()
    for l in io.open(OPERACIONES, encoding="utf-8"):
        l = l.strip()
        if not l:
            continue
        import json
        f = json.loads(l).get("fase")
        if f:
            nombres.add(f)
    return sorted(nombres)


def estado(fase):
    r = subprocess.run([sys.executable,
                        os.path.join(RAIZ, "scripts", "loop",
                                     "tallar_estado_de_fase.py"),
                        "--fase", fase],
                       cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    salida = r.stdout or ""
    m = re.search(r"CIFRA: operaciones del catalogo: (\d+) \| con destino "
                  r"cumplido: (\d+) \| sin cumplir: (\d+) \| de ellas, sin vara "
                  r"escrita: (\d+)", salida)
    sin = re.search(r"^SIN CUMPLIR \((\d+)\): (.+)$", salida, re.M)
    sinvara = re.search(r"^SIN VARA ESCRITA \((\d+)\): (.+)$", salida, re.M)
    if not m:
        return None, r.returncode
    return ({"catalogo": int(m.group(1)),
             "cumplidas": int(m.group(2)),
             "sin_cumplir": int(m.group(3)),
             "sin_vara": int(m.group(4)),
             "nombres": sin.group(2) if sin else "ninguna",
             "nombres_sin_vara": sinvara.group(2) if sinvara else "ninguna"},
            r.returncode)


def main():
    print("=" * 78)
    print("VUELTA 161, TAREA 3: EL ORDEN ESCRITO, RECORRIDO HASTA DONDE LLEGA")
    print("=" * 78)
    print("")

    print("A) EL ORDEN, LEIDO DEL FICHERO Y NO TECLEADO")
    fases = fases_del_fichero()
    print("   fuente: docs/plan/OPERACIONES.jsonl (campo `fase`)")
    for f in fases:
        print("   %s" % f)
    print("   CIFRA fases con operaciones: %d" % len(fases))
    print("")

    print("B) EL RECORRIDO, FASE A FASE, CON SUS CIFRAS TALLADAS")
    print("   instrumento: scripts/loop/tallar_estado_de_fase.py --fase <N>")
    print("")
    # CAIDA MIA DE LA VUELTA 161, CAZADA LEYENDO MI PROPIA SALIDA ANTES DE
    # COMMITEARLA, Y SE DECLARA EN VEZ DE TAPARSE. Mi primera version leia la
    # columna "sin cumplir" del tallador como si fuera "operaciones pendientes",
    # y publico "LA PRIMERA DEL ORDEN QUE NO CIERRA: 00_CODIGO", que contradice
    # el estado publicado de la campana (las fases 01 a 07 estan cerradas por
    # acta). El tallador cuenta como SIN CUMPLIR tambien las NO COMPUTABLES, o
    # sea aquellas para cuyo tipo NO HAY REGLA ESCRITA que mida el destino
    # contra el grafo, y las publica aparte en su propia cifra "de ellas, sin
    # vara escrita". Una cosa es que una operacion falle su destino medido y
    # otra que nadie haya escrito con que medirla. Se separan las dos columnas.
    print("   | fase | catalogo | cumplidas | sin cumplir | de ellas SIN VARA "
          "ESCRITA | sin cumplir CON VARA QUE MIDE | las que faltan |")
    print("   |---|---:|---:|---:|---:|---:|---|")
    primera_con_vara = None
    filas = []
    for f in fases:
        d, rc = estado(f)
        if d is None:
            print("   | %s | (no se pudo medir, exit %d) | | | | | |" % (f, rc))
            continue
        con_vara = d["sin_cumplir"] - d["sin_vara"]
        d["con_vara"] = con_vara
        d["fase"] = f
        filas.append(d)
        print("   | %s | %d | %d | %d | %d | %d | %s |"
              % (f, d["catalogo"], d["cumplidas"], d["sin_cumplir"],
                 d["sin_vara"], con_vara, d["nombres"]))
        if con_vara and primera_con_vara is None:
            primera_con_vara = d
    print("")
    print("   CIFRA fases medidas: %d" % len(filas))
    print("   CIFRA fases sin NINGUNA sin cumplir: %d"
          % len([x for x in filas if x["sin_cumplir"] == 0]))
    print("   CIFRA fases sin ninguna sin cumplir CON VARA QUE MIDE: %d"
          % len([x for x in filas if x["con_vara"] == 0]))
    print("   CIFRA operaciones del plan entero: %d"
          % sum(x["catalogo"] for x in filas))
    print("   CIFRA sin cumplir en total: %d" % sum(x["sin_cumplir"] for x in filas))
    print("   CIFRA de ellas SIN VARA ESCRITA (no computables): %d"
          % sum(x["sin_vara"] for x in filas))
    print("   CIFRA de ellas SIN CUMPLIR CON VARA QUE MIDE: %d"
          % sum(x["con_vara"] for x in filas))
    print("")
    print("   LO QUE ESTA TABLA DICE Y LO QUE NO, Y SE SEPARA A PROPOSITO:")
    print("   'sin cumplir' del tallador incluye las NO COMPUTABLES, o sea las")
    print("   de un tipo para el que NO HAY REGLA ESCRITA que mida su destino")
    print("   contra el grafo. Esa columna NO dice que la operacion este")
    print("   pendiente: dice que nadie ha escrito con que medirla. La columna")
    print("   que si muerde es la ultima.")
    if primera_con_vara:
        print("   LA PRIMERA DEL ORDEN CON ALGO SIN CUMPLIR Y CON VARA QUE MIDE:")
        print("      %s, con %d (%s)"
              % (primera_con_vara["fase"], primera_con_vara["con_vara"],
                 primera_con_vara["nombres"]))
    else:
        print("   NINGUNA FASE tiene una operacion sin cumplir con vara que mida.")
    print("")

    print("C) EL MURO, MEDIDO HOY Y NO CITADO DE MEMORIA")
    cita = io.open(ACTA, encoding="utf-8").read().split("\n")[LINEA_ACTA_149 - 1]
    print("   ACTA_AUDITOR.md:%d, leida hoy:" % LINEA_ACTA_149)
    print("      %s" % cita.strip())
    if "FASE 08" not in cita:
        print("   PARADA: esa linea ya no dice lo que se cita.")
        return 1

    env = os.path.join(RAIZ, ".env")
    gitignore = io.open(os.path.join(RAIZ, ".gitignore"), encoding="utf-8").read()
    print("   .env existe en el arbol de trabajo: %s" % os.path.exists(env))
    print("   .env esta en .gitignore: %s"
          % any(l.strip() == ".env" for l in gitignore.split("\n")))
    print("")
    print("   LA PRUEBA DE RUMBOS, CORRIDA HOY (tiene que fallar VISIBLE):")
    ruta = os.path.join(RAIZ, "scripts", "rumbos", "prueba_rumbos.py")
    if not os.path.exists(ruta):
        print("      ROJO: no existe %s" % ruta)
        return 1
    r = subprocess.run([sys.executable, ruta], cwd=RAIZ, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    for linea in (r.stdout or "").strip().split("\n")[-6:]:
        print("      %s" % linea)
    for linea in (r.stderr or "").strip().split("\n")[-6:]:
        if linea.strip():
            print("      [err] %s" % linea)
    print("      EXITCODE de la prueba de rumbos: %d" % r.returncode)
    falla_visible = r.returncode != 0
    print("      FALLA VISIBLE: %s" % falla_visible)
    print("")

    print("D) LO QUE APARECIO AL RECORRER EL ORDEN, Y NO LO ARREGLO: OP-D-02")
    print("   Es la UNICA operacion de una fase distinta de la 03 que sale SIN")
    print("   CUMPLIR CON UNA VARA QUE MIDE. Se mide y se declara, no se toca.")
    import json
    grafo = json.loads(io.open(os.path.join(RAIZ, "dataset", "metadata",
                                            "master_graph.json"),
                               encoding="utf-8").read())["nodos"]
    ficha = None
    for l in io.open(OPERACIONES, encoding="utf-8"):
        l = l.strip()
        if l and json.loads(l).get("id_op") == "OP-D-02":
            ficha = json.loads(l)
            break
    if ficha is None:
        print("   PARADA: no se halla la ficha de OP-D-02.")
        return 1
    sup = ficha.get("superviviente")
    print("   superviviente escrito en la ficha: %s" % sup)
    print("   campo `nodos` de la ficha (%d): %s"
          % (len(ficha.get("nodos", [])), ", ".join(ficha.get("nodos", []))))
    print("   campo `eliminar` de la ficha: %s" % ficha.get("eliminar"))
    alias = (grafo.get(sup) or {}).get("ids_alias") or []
    print("   ids_alias del superviviente HOY: %s" % alias)
    for n in ficha.get("nodos", []):
        nodo = grafo.get(n) or {}
        print("      %-32s existe=%s deprecado=%s en ids_alias del superviviente=%s"
              % (n, n in grafo, bool(nodo.get("deprecado")), n in alias))
    print("   LA VARA DEL TALLADOR toma como ABSORBIDOS a todo `nodos` menos el")
    print("   superviviente, o sea TRES, y exige de los tres que esten deprecados")
    print("   y en ids_alias. LA FICHA NO DICE ESO: su orden interno manda FUNDIR")
    print("   con enfoque_mercado_voc (punto 2) y solo TENER DELANTE a")
    print("   homework_frontend_loading y voice_of_customer_homework (punto 4), y")
    print("   su campo `eliminar` esta VACIO. Medido contra el grafo, el unico")
    print("   absorbido que la ficha manda SI esta hecho: enfoque_mercado_voc")
    print("   deprecado y en ids_alias del superviviente.")
    print("   NO TOCO LA VARA NI LA FICHA. Queda PENDIENTE DE DOCTRINA y va como")
    print("   pregunta: si `tener delante` cuenta como absorcion para la vara de")
    print("   los DESTEJIDOS, esta operacion esta sin cumplir; si no cuenta, la")
    print("   vara es mas ancha que la ficha y el rojo es falso.")
    print("")

    print("E) DONDE TERMINA LO QUE UN BUCLE PUEDE HACER SOLO")
    print("   La fase 08 tiene UNA operacion, OP-V-01, y su punto 9 es la")
    print("   verificacion TRANSVERSAL: Gate 0 verde, suite verde, VUELO COMPLETO,")
    print("   PRUEBA DE RUMBOS y REINDEXADO SEMANTICO. Las tres ultimas necesitan")
    print("   credencial: VOYAGE_API_KEY para el indice y los rumbos,")
    print("   NEXT_PUBLIC_SUPABASE_URL y SUPABASE_SERVICE_ROLE_KEY mas un next dev")
    print("   levantado para el vuelo. El .env esta fuera del repo mientras el")
    print("   bucle corre Y ESO ESTA BIEN (AUDITOR.md seccion 4).")
    print("   SE PARA Y SE DICE: no es un fallo del bucle, es su frontera.")
    print("   EL MERGE NO SE PIDE NI SE HACE.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
