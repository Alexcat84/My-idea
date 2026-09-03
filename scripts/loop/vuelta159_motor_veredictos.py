# -*- coding: utf-8 -*-
"""vuelta159_motor_veredictos.py . EL MOTOR COMUN DE LAS LECTURAS DE LA VUELTA
159 (TAREAS 2.a, 2.b y 3).

POR QUE UN MOTOR Y NO TRES CLONES. Esta vuelta aplica veredictos en TRES
nominas distintas (las tres en disputa de la 2.a, el tramo de 41 de la 2.b y el
lote 2 de 53 de la TAREA 3) CON LAS MISMAS GUARDAS. Clonar el instrumento tres
veces es la manera conocida de que las tres copias se desincronicen, y la ley de
una sola fuente lo prohibe: la copia muere y redirige a la fuente.

QUE HACE, Y NADA MAS: escribe la clase y la razon en el registro
`docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl` y la fila del `.md`
`docs/plan/LECTURAS_DIRIGIDAS.md`, POR ADICION, y corre las guardas de la 2.d.

LO QUE CAMBIA RESPECTO DEL INSTRUMENTO DEL LOTE 1, Y ES UN CAMBIO DE VERDAD:

  (i)  LA CLASE PUEDE MOVERSE EN LOS DOS SENTIDOS. El instrumento de la vuelta
       157 llevaba `assert` de que toda clase movida iba DE C A D, porque aquel
       lote solo podia bajar. La relectura conjunta de la 6.4 del acta 158 puede
       DEVOLVER una D a C si los nodos lo dicen, y una guarda que lo prohiba
       seria una guarda que impide corregir. Se sustituye por una guarda mas
       estrecha y que si vale: NINGUNA CLASE SE MUEVE A `A` (limite de la 6.1
       del acta 155, "la que salga A no se voltea"), y toda clase movida queda
       en la lista publicada con su origen y su destino.
  (ii) LA CELDA DEL `.md` ACUMULA TACHADOS. `C` pasa a `~~C~~ D`, y `~~C~~ D`
       pasa a `~~C~~ ~~D~~ C`. El rastro entero queda a la vista, que es la
       costumbre de la casa: una correccion que tapa lo que corrige no se puede
       auditar.

LAS GUARDAS DE LA 2.d, QUE NO SE AFLOJAN:
  - CADA CAMBIO DE CLASE CON CORRECCION DECLARADA y el texto viejo entero como
    PREFIJO, comprobado por assert sobre las 154 entradas y no solo las tocadas.
  - `n` NO SE MUEVE: los veredictos del cribado se cuentan antes y despues y
    tienen que seguir en 3.388.
  - ASSERT DE FRONTERA: sha256 de todo `dataset/` y conteo de censo y aristas
    antes y despues. EL REGISTRO CAMBIA, EL GRAFO NO.
  - NINGUN PAR SE MUEVE.
  - Gate 0 se corre al terminar, fuera de este modulo, con el ciclo entero.

ES IDEMPOTENTE por marca literal: cada tarea pasa su propia MARCA.

NO SE INVOCA SOLO: lo importan `vuelta159_tarea2a_relectura_conjunta.py`,
`vuelta159_tarea2b_relectura_tramo.py` y `vuelta159_tarea3_lote2.py`.
"""
import hashlib
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
LD_MD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
VERED = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
DATASET = os.path.join(RAIZ, "dataset")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

N_CRIBADO = 3388


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def entradas():
    return [json.loads(x) for x in leer(REGISTRO).splitlines() if x.strip()]


def guardar(E):
    with io.open(REGISTRO, "w", encoding="utf-8", newline="\n") as fh:
        for e in E:
            fh.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")


def ld_de(e):
    return e["cita"].split(",")[0].strip()


def sha_dataset():
    """sha256 de TODO dataset/, fichero a fichero y en orden, NORMALIZANDO fin
    de linea, para que la frontera no dependa de core.autocrlf."""
    h = hashlib.sha256()
    for raiz, dirs, ficheros in os.walk(DATASET):
        dirs.sort()
        for f in sorted(ficheros):
            ruta = os.path.join(raiz, f)
            h.update(os.path.relpath(ruta, RAIZ).replace("\\", "/").encode("utf-8"))
            with open(ruta, "rb") as fh:
                h.update(fh.read().replace(b"\r\n", b"\n").replace(b"\r", b"\n"))
    return h.hexdigest()


def censo_y_aristas():
    N = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    vivos = sum(1 for n in N.values() if not n.get("deprecado"))
    sig = sum(len(n.get("nodos_siguientes") or []) for n in N.values())
    prev = sum(len(n.get("nodos_previos") or []) for n in N.values())
    return len(N), vivos, len(N) - vivos, sig, prev


def n_veredictos():
    return sum(1 for x in io.open(VERED, encoding="utf-8") if x.strip())


def celda_nueva(celda, clase_nueva):
    """Acumula el tachado. `C` mas D da `~~C~~ D`. `~~C~~ D` mas C da
    `~~C~~ ~~D~~ C`. La clase VIGENTE es siempre el ultimo token."""
    t = celda.split()
    if not t:
        return clase_nueva
    if t[-1] == clase_nueva:
        return celda.strip()
    return " ".join(t[:-1] + ["~~%s~~" % t[-1], clase_nueva])


def tocar_md(texto, ld, clase_nueva, nota):
    """Reescribe la celda de clase y anade la nota al final de la columna de
    motivo. El texto viejo de la columna NO se borra: la nota va detras."""
    num = int(ld.split("-")[-1])
    pat = re.compile(
        r"(\| %d \| REGISTRO DE CITAS `OP-C-05` \| [a-z0-9_]+ <-> [a-z0-9_]+ \| )"
        r"([^|]*)( \| %s \| )([^\n|]*)(\|)" % (num, re.escape(ld)))
    m = pat.search(texto)
    if not m:
        return texto, False, None
    celda_vieja = m.group(2).strip()
    celda = celda_nueva(celda_vieja, clase_nueva)
    nuevo = "%s%s%s%s %s |" % (m.group(1), celda, m.group(3),
                              m.group(4).rstrip(), nota)
    return texto[:m.start()] + nuevo + texto[m.end():], True, (celda_vieja, celda)


def aplicar(titulo, veredictos, marca, cabeza, nota_md, ids_esperados=None):
    """VEREDICTOS es {ld: (clase_nueva, motivo)}. CABEZA es una funcion
    (vieja, nueva) que devuelve la cabeza del bloque que se anade a la razon."""
    print("=" * 78)
    print(titulo)
    print("=" * 78)
    print("")

    if ids_esperados is not None:
        assert sorted(veredictos) == sorted(ids_esperados), (
            "la nomina sellada y los veredictos escritos no calzan")
        print("CIFRA lecturas de la nomina sellada: %d" % len(ids_esperados))
    print("CIFRA veredictos escritos en este instrumento: %d" % len(veredictos))
    print("")

    print("A) LA FRONTERA, ANTES DE TOCAR NADA")
    sha_antes = sha_dataset()
    censo_antes = censo_y_aristas()
    n_antes = n_veredictos()
    print("   sha256 de dataset/ ANTES : %s" % sha_antes)
    print("   censo ANTES              : %d nodos, %d vivos, %d deprecados" % censo_antes[:3])
    print("   aristas ANTES            : %d siguientes, %d previos" % censo_antes[3:])
    print("   CIFRA n, veredictos del cribado ANTES: %d" % n_antes)
    print("")

    E = entradas()
    antes_razon = {ld_de(e): e["razon"] for e in E}
    antes_clase = {ld_de(e): e["clase"] for e in E}
    texto_md = leer(LD_MD)

    print("B) LOS VEREDICTOS, UNO A UNO")
    cambian, se_quedan, ya, sin_fila = 0, 0, 0, []
    celdas = {}
    for e in E:
        ld = ld_de(e)
        if ld not in veredictos:
            continue
        nueva, motivo = veredictos[ld]
        vieja = e["clase"]
        if marca in e["razon"]:
            ya += 1
            print("   %-16s %s -> %s   YA ESTABA" % (ld, vieja, nueva))
            continue
        assert nueva != "A", (
            "%s: la que salga A no se voltea y tampoco se escribe aqui" % ld)
        e["razon"] = e["razon"] + cabeza(vieja, nueva) + motivo + "]"
        e["clase"] = nueva
        texto_md, ok, par = tocar_md(texto_md, ld, nueva, nota_md(vieja, nueva, motivo))
        if not ok:
            sin_fila.append(ld)
        else:
            celdas[ld] = par
        if nueva != vieja:
            cambian += 1
        else:
            se_quedan += 1
        print("   %-16s %s -> %s   %s" % (ld, vieja, nueva, motivo[:76]))
    print("")

    if sin_fila:
        print("ROJO: no se encontro la fila del .md de: %s" % ", ".join(sin_fila))
        print("FIN")
        return 1

    guardar(E)
    with io.open(LD_MD, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto_md)

    if celdas:
        print("   LAS CELDAS DEL .md, ANTES Y DESPUES (el rastro no se tapa):")
        for ld in sorted(celdas):
            print("      %-16s [%s] -> [%s]" % (ld, celdas[ld][0], celdas[ld][1]))
        print("")

    print("C) LAS GUARDAS, MEDIDAS Y NO PROMETIDAS")
    D = entradas()
    assert len(D) == len(E) == 154, "el numero de lineas del registro se movio"
    rotos = [ld_de(d) for d in D if not d["razon"].startswith(antes_razon[ld_de(d)])]
    assert not rotos, "PREFIJO ROTO en: %s" % ", ".join(rotos)
    print("   C.1 PREFIJO: las %d razones conservan su texto viejo ENTERO" % len(D))

    pares_antes = {tuple(sorted(e["par"])) for e in E}
    pares_desp = {tuple(sorted(d["par"])) for d in D}
    assert pares_antes == pares_desp, "esta tarea NO mueve ningun par"
    print("   C.2 PARES: %d pares, los mismos antes y despues" % len(pares_desp))

    movidas = [(ld_de(d), antes_clase[ld_de(d)], d["clase"])
               for d in D if d["clase"] != antes_clase[ld_de(d)]]
    print("   C.3 CLASES MOVIDAS: %d" % len(movidas))
    for ld, v, n in sorted(movidas):
        print("       %-16s %s -> %s" % (ld, v, n))
    assert all(n != "A" for _, _, n in movidas), "ninguna clase se mueve a A"
    print("       NINGUNA SE MUEVE A A: el limite de la 6.1 del acta 155 se cumple.")

    sha_desp = sha_dataset()
    censo_desp = censo_y_aristas()
    n_desp = n_veredictos()
    print("   C.4 FRONTERA, sha256 de dataset/ DESPUES: %s" % sha_desp)
    print("       censo DESPUES  : %d nodos, %d vivos, %d deprecados" % censo_desp[:3])
    print("       aristas DESPUES: %d siguientes, %d previos" % censo_desp[3:])
    assert sha_antes == sha_desp, "EL GRAFO SE MOVIO: la frontera esta rota"
    assert censo_antes == censo_desp, "el censo o las aristas se movieron"
    print("       EL REGISTRO CAMBIA, EL GRAFO NO: sha256 IDENTICO y censo IDENTICO")
    print("   C.5 CIFRA n, veredictos del cribado DESPUES: %d" % n_desp)
    assert n_antes == n_desp == N_CRIBADO, "n se movio: tenia que quedarse en 3.388"
    print("       n NO SE MUEVE y sigue en 3.388")
    print("")

    r = subprocess.run(["git", "diff", "--numstat", "--", "docs/plan/"],
                       cwd=RAIZ, capture_output=True)
    print("   C.6 numstat de docs/plan/:")
    for l in r.stdout.decode("utf-8", "replace").strip().splitlines():
        print("       %s" % l)
    print("")

    clases = {}
    for d in D:
        if d.get("via") == "LECTURA_DIRIGIDA":
            clases[d["clase"]] = clases.get(d["clase"], 0) + 1
    print("D) EL SACO, RECONTADO SOBRE EL REGISTRO YA ESCRITO")
    print("   CIFRA lecturas dirigidas por clase: %s" % json.dumps(clases, sort_keys=True))
    print("   CIFRA con la clase movida en esta tarea: %d" % cambian)
    print("   CIFRA que sostienen su clase en esta tarea: %d" % se_quedan)
    print("   CIFRA que ya estaban escritas: %d" % ya)
    print("")
    print("NINGUNA SALIO A. No hay candidato a fusion, no se toca una arista y n no")
    print("se mueve. El limite de la 6.1 del acta 155 sigue vigente y no se cruzo.")
    print("FIN")
    return 0
