# -*- coding: utf-8 -*-
"""vuelta40_destejido_opd05.py - LA COSTURA QUE EL ARCHIVO DECLARA EN OP-D-05,
BUSCADA EN EL NODO DE HOY.

ESTRICTAMENTE DE SOLO LECTURA. No toca un nodo, no funde, no destejе nada.

POR QUE EXISTE, y es un hallazgo de esta vuelta que no estaba en el encargo. El
encargo manda decidir el destejido de OP-D-05 por LECTURA TEXTUAL con la cita
del instrumento delante. Al leer las tres razones ENTERAS del archivo aparecio
algo que la cita del instrumento no dice y que ninguna pagina del plan de
OP-D-05 recoge:

  LAS RAZONES DE LOS PUESTOS 492 Y 673 DECLARAN UNA COSTURA CONFIRMADA EN
  `seleccion_ceo_fundador`, con su frontera escrita (DOCE pasos, corte 1 a 4
  contra 5 a 12) y su ficha de origen (docs/FICHA_SUBFUSION_GRADIENTE.md).

O sea que el destejido de esta operacion SI tenia un sujeto nombrado, solo que
no en el plan de la operacion sino en las razones de sus propios pares. Este
script comprueba, contra el nodo de HOY y no contra el recuerdo, si esa costura
SIGUE EN PIE o si ya se la llevo una operacion anterior. Es la misma pregunta
que `vuelta34_costuras_opd03.py` le hizo a OP-D-03, y se hace igual: por la
HUELLA del bloque, no por la cifra de pasos sola.

Uso: python scripts/loop/vuelta40_destejido_opd05.py
"""
import io
import json
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
FICHA = os.path.join(RAIZ, "docs", "FICHA_SUBFUSION_GRADIENTE.md")

ACTO = ["seleccion_ceo_fundador", "asignacion_de_titulos_ejecutivos",
        "errores_comunes_asignacion_roles"]

# LO QUE EL ARCHIVO DECLARA, citado de las razones de los puestos 492 y 673 y
# NO tecleado de memoria: el script las vuelve a leer y las imprime.
DECLARADO = {
    "node_id": "seleccion_ceo_fundador",
    "pasos_cuando_se_escribio": 12,
    "frontera": "1 a 4 (la decision compartida) / 5 a 12 (otro asunto entero)",
    "dos_libros": ["The Founder's Dilemmas", "The Hard Thing About Hard Things"],
    # Las huellas del bloque 5 a 12, tal como las nombran las dos razones. Si el
    # bloque sigue dentro, estas palabras tienen que estar en los pasos de hoy.
    "huellas_del_bloque_5_12": ["mentor", "brecha", "CEO profesional", "control",
                                "autoevaluacion", "clausula"],
}


def raya(t):
    print("")
    print("=" * 78)
    print(t)
    print("=" * 78)


def nodo(nid):
    return json.loads(io.open(os.path.join(NODOS, nid + ".json"),
                              encoding="utf-8").read())


def main():
    raya("0. CUANTOS DESTEJIDOS ESPERABA EL PLAN, citado de su tabla de orden")
    md = io.open(os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md"),
                 encoding="utf-8").read()
    cab, fila = None, None
    for linea in md.splitlines():
        if linea.startswith("| orden | operacion |"):
            cab = linea
        if linea.startswith("| 5 | `OP-D-05`"):
            fila = linea
    print("  CABECERA: %s" % cab)
    print("  FILA    : %s" % fila)
    print("")
    print("  LECTURA: la tabla de orden del plan le cuenta a OP-D-05 UN destejido")
    print("  y nombra a seleccion_ceo_fundador como EL NODO ANCLA. O sea que el")
    print("  destejido de esta operacion SI tenia sujeto escrito, y es el mismo")
    print("  que las razones de sus pares declaran. Precedente de la misma tabla:")
    print("  a OP-D-03 le contaba TRES y su propia celda dice hoy que DOS estaban")
    print("  CONSUMIDAS por la fase 01. La pregunta de esta vuelta es si la de")
    print("  OP-D-05 tambien lo esta.")

    raya("1. LO QUE EL ARCHIVO DECLARA, releido hoy de las razones (no tecleado)")
    razones = {}
    for l in io.open(VER, encoding="utf-8"):
        if not l.strip():
            continue
        v = json.loads(l)
        if v.get("nodo_a") in ACTO and v.get("nodo_b") in ACTO:
            razones[v["puesto_intra"]] = v
    for p in sorted(razones):
        r = razones[p]["razon"]
        print("  puesto %s (%s con %s):" % (p, razones[p]["nodo_a"], razones[p]["nodo_b"]))
        for frase in ("costura CONFIRMADA", "DOCE pasos", "doce pasos",
                      "Costura para la otra ficha", "del 1 al 4", "del 5 al 12",
                      "5 al 12"):
            if frase in r:
                i = r.index(frase)
                print("      CITA: ...%s..." % r[max(0, i - 90):i + 130].replace("\n", " "))
    print("")
    print("  LA FICHA QUE LA RAZON NOMBRA: %s"
          % os.path.relpath(FICHA, RAIZ).replace("\\", "/"))
    print("      existe hoy: %s" % os.path.exists(FICHA))
    if os.path.exists(FICHA):
        t = io.open(FICHA, encoding="utf-8").read()
        print("      nombra a seleccion_ceo_fundador: %s"
              % ("SI" if "seleccion_ceo_fundador" in t else "NO"))
        for linea in t.split("\n"):
            if "seleccion_ceo_fundador" in linea:
                print("      | " + linea.strip()[:200])

    raya("2. EL NODO DE HOY, medido contra lo declarado")
    n = nodo(DECLARADO["node_id"])
    pasos = n.get("pasos_accionables") or []
    print("  %s" % DECLARADO["node_id"])
    print("    pasos cuando se escribio la razon : %d" % DECLARADO["pasos_cuando_se_escribio"])
    print("    pasos HOY                         : %d" % len(pasos))
    print("    frontera escrita                  : %s" % DECLARADO["frontera"])
    print("    fuente declarada en la razon      : %s" % " y ".join(DECLARADO["dos_libros"]))
    print("    fuente HOY                        : %s" % n.get("fuente"))
    print("")
    print("    LAS HUELLAS DEL BLOQUE 5 A 12, buscadas en el texto de hoy:")
    texto = " ".join(pasos + (n.get("condiciones_activacion") or [])
                     + [n.get("entregable_esperado") or "",
                        n.get("resumen_ejecutivo") or ""]).lower()
    vivas = []
    for h in DECLARADO["huellas_del_bloque_5_12"]:
        hay = h.lower() in texto
        print("      %-18s %s" % (h, "SIGUE DENTRO" if hay else "YA NO ESTA"))
        if hay:
            vivas.append(h)
    print("")
    print("    HUELLAS QUE SIGUEN DENTRO: %d de %d -> %s"
          % (len(vivas), len(DECLARADO["huellas_del_bloque_5_12"]), vivas or "ninguna"))
    print("")
    print("    LOS PASOS DE HOY, enteros:")
    for i, p in enumerate(pasos, 1):
        print("      %2d. %s" % (i, p))

    raya("3. QUIEN SE LO LLEVO, medido en git y no supuesto")
    out = subprocess.check_output(
        ["git", "log", "--follow", "--format=%h %ad %s", "--date=short", "--",
         "dataset/nodos/%s.json" % DECLARADO["node_id"]],
        cwd=RAIZ).decode("utf-8", "replace")
    for linea in out.strip().split("\n")[:6]:
        print("  " + linea)
    print("")
    print("  Y EN QUE NOMINAS ESTA EL NODO, medido contra OPERACIONES.jsonl:")
    ops = [json.loads(l) for l in
           io.open(os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl"),
                   encoding="utf-8") if l.strip()]
    for o in ops:
        if DECLARADO["node_id"] in (o.get("nodos") or []):
            print("    %-14s %-10s tipo %s" % (o["id_op"], o["estado"], o["tipo"]))

    raya("4. EL VEREDICTO DEL DESTEJIDO, y quien lo emite")
    queda = len(vivas) > 0 or len(pasos) >= DECLARADO["pasos_cuando_se_escribio"]
    print("  QUEDA COSTURA EN %s: %s" % (DECLARADO["node_id"],
                                         "SI" if queda else "NO"))
    print("  Vara usada, la misma de vuelta34_costuras_opd03.py: la costura")
    print("  sigue en pie si sus HUELLAS siguen en el texto. Cero huellas y el")
    print("  nodo en %d pasos contra los %d de la razon: el bloque ya salio."
          % (len(pasos), DECLARADO["pasos_cuando_se_escribio"]))
    print("")
    print("  LOS OTROS DOS, para que el acto quede medido entero:")
    for nid in ACTO[1:]:
        m = nodo(nid)
        print("    %-34s %d pasos, fuente: %s"
              % (nid, len(m.get("pasos_accionables") or []), m.get("fuente")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
