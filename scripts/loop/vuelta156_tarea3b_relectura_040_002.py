# -*- coding: utf-8 -*-
"""vuelta156_tarea3b_relectura_040_002.py . TAREA 3.b DE LA VUELTA 156.

LOS DOS QUE EL ACTA 155 YA NOMBRO, RELEIDOS POR P.5 Y ADJUDICADOS: `LD-OPC05-040`
(`cost_management_plan` contra `stakeholder_register`) y `LD-OPC05-002`
(`actividades_clave` contra `key_resources_hypothesis`).

LA VARA (adjudicacion 6.2 del acta 155): la C es sano CON FIGURA y la figura
EXIGE DOS LINEAS DISTINTAS, UNA EN CADA NODO. O se nombran las dos, o la clase
es D.

LOS DOS SE RELEEN CONTRA SUS PASOS ENTEROS, LEIDOS HOY DEL GRAFO, y el veredicto
va escrito con las lineas que se buscaron y no se encontraron, no con un "no hay
figura" a secas.

TODO POR CORRECCION DECLARADA Y EN LAS DOS SEDES (el registro de citas y
docs/plan/LECTURAS_DIRIGIDAS.md), con el texto viejo entero como prefijo. LA
CELDA DE CLASE DEL .md SE DEJA LIMPIA A PROPOSITO: su lector exige [A-Z]+ y un
tachado ahi borraria el par del registro y pondria Gate 0 en rojo.

n NO SE MUEVE: los veredictos del cribado siguen donde estaban, y el grafo
tampoco. Guarda de frontera con assert antes y despues.

USO:  python scripts/loop/vuelta156_tarea3b_relectura_040_002.py
"""
import glob
import hashlib
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
LD_MD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos", "*.json")
META = os.path.join(RAIZ, "dataset", "metadata", "*.json")

MARCA = "RELECTURA POR P.5 DE LA VUELTA 156"

CASOS = {
    "LD-OPC05-040": {
        "fila": "40",
        "par": ("cost_management_plan", "stakeholder_register"),
        "clase_vieja": "C",
        "clase_nueva": "D",
        "veredicto": (
            "NO HAY FIGURA Y LA CLASE ES D, SANO Y DISTINTO. Releidos hoy los dos nodos "
            "enteros: cost_management_plan trae CUATRO pasos y los cuatro son de plan de "
            "costos (el nivel de precision de las estimaciones; las unidades, la moneda y "
            "los umbrales de varianza; las tecnicas de estimacion y el presupuesto por "
            "fases; las reglas de medicion de desempeno y quien tiene autoridad para "
            "asignar presupuesto). stakeholder_register trae SEIS y los seis son de "
            "registro de interesados (anotar a todos, posicion y rol y contacto y "
            "necesidad, que espera cada uno, cuanta influencia tiene, su postura a favor o "
            "neutral o en contra, y actualizar la lista). LAS DOS LINEAS QUE HABRIA QUE "
            "NOMBRAR SE BUSCARON Y NO ESTAN: ninguna linea de costos es expandida por el "
            "registro, y ninguna linea del registro es expandida por el plan de costos. La "
            "unica cercania es el paso 4 de costos, 'quien tiene autoridad para asignar "
            "presupuesto', contra el paso 2 del registro, 'la posicion, el rol'; y no es "
            "figura, porque el registro NO desarrolla la autoridad presupuestaria en ningun "
            "paso: lista a todos los interesados por igual. Son el dinero y las personas, y "
            "los dos formularios del mismo libro. EL ACTA 155 TENIA RAZON."),
    },
    "LD-OPC05-002": {
        "fila": "2",
        "par": ("actividades_clave", "key_resources_hypothesis"),
        "clase_vieja": "C",
        "clase_nueva": "D",
        "veredicto": (
            "NO HAY FIGURA Y LA CLASE ES D, SANO Y DISTINTO. Releidos hoy los dos nodos "
            "enteros: actividades_clave trae CUATRO pasos (decidir si el negocio es de "
            "produccion, resolucion de problemas o plataforma; listar las actividades que "
            "la propuesta de valor exige; vincular cada actividad con canales, relaciones e "
            "ingresos; priorizar lo core contra lo delegable a socios). "
            "key_resources_hypothesis trae CINCO (los recursos fisicos; de donde viene el "
            "dinero, con VC, grants, factoring o leasing; que talento hace falta ahora y "
            "despues; que ideas o marcas proteger como propiedad intelectual; de que "
            "terceros se depende fuera del propio control). LAS DOS LINEAS SE BUSCARON Y NO "
            "ESTAN: ninguna linea de actividades es desarrollada por recursos, y ninguna "
            "linea de recursos es desarrollada por actividades. Ni siquiera son del mismo "
            "libro (Business Model Generation contra The Startup Owner's Manual): son DOS "
            "BLOQUES DISTINTOS del mismo lienzo, lo que se hace contra lo que se necesita "
            "para hacerlo. EL ACTA 155 TENIA RAZON, y su propia muestra ciega daba la misma "
            "senal."),
    },
}


def sha256_de_arbol(patrones):
    h = hashlib.sha256()
    rutas = []
    for p in patrones:
        rutas += sorted(glob.glob(p))
    for ruta in sorted(rutas):
        h.update(os.path.basename(ruta).encode("utf-8"))
        with open(ruta, "rb") as fh:
            h.update(fh.read().replace(b"\r\n", b"\n"))
    return h.hexdigest(), len(rutas)


def censo():
    todos = {}
    for ruta in sorted(glob.glob(NODOS)):
        d = json.load(io.open(ruta, encoding="utf-8"))
        nid = d.get("node_id") or os.path.splitext(os.path.basename(ruta))[0]
        todos[nid] = d
    vivos = sum(1 for n in todos.values() if not n.get("deprecado"))
    sig = sum(len(n.get("nodos_siguientes") or []) for n in todos.values())
    prev = sum(len(n.get("nodos_previos") or []) for n in todos.values())
    return len(todos), vivos, sig, prev


def frontera(momento):
    sha, nf = sha256_de_arbol([NODOS, META])
    nodos, vivos, sig, prev = censo()
    ver = sum(1 for x in io.open(VEREDICTOS, encoding="utf-8") if x.strip())
    print("  %-8s sha256 dataset/ (%d ficheros) %s | censo %d/%d | aristas %d/%d | n %d"
          % (momento, nf, sha[:32], nodos, vivos, sig, prev, ver))
    return (sha, nf, nodos, vivos, sig, prev, ver)


def entradas():
    return [json.loads(x) for x in io.open(REGISTRO, encoding="utf-8") if x.strip()]


def pasos(nid):
    for ruta in sorted(glob.glob(NODOS)):
        d = json.load(io.open(ruta, encoding="utf-8"))
        if (d.get("node_id") or os.path.splitext(os.path.basename(ruta))[0]) == nid:
            return d.get("pasos_accionables") or [], d.get("fuente")
    return [], None


def main():
    print("=" * 100)
    print("VUELTA 156, TAREA 3.b: LOS DOS QUE EL ACTA 155 NOMBRO, RELEIDOS POR P.5")
    print("=" * 100)
    print("")
    print("GUARDA DE FRONTERA, ANTES")
    antes = frontera("ANTES")
    print("")

    print("LOS CUATRO NODOS, CON SUS PASOS ENTEROS LEIDOS HOY")
    print("-" * 100)
    for ld in sorted(CASOS):
        for nid in CASOS[ld]["par"]:
            P, fuente = pasos(nid)
            print("  %s  (%d pasos)  fuente: %s" % (nid, len(P), fuente))
            for i, s in enumerate(P, 1):
                print("     %d. %s" % (i, s))
        print("")

    print("=" * 100)
    print("LOS DOS VEREDICTOS, ESCRITOS EN LAS DOS SEDES")
    print("=" * 100)

    E = entradas()
    movidas = 0
    for ld in sorted(CASOS):
        c = CASOS[ld]
        e = next(x for x in E if x["cita"].startswith(ld))
        print("")
        print("  %s | %s <-> %s" % (ld, c["par"][0], c["par"][1]))
        assert tuple(sorted(e["par"])) == tuple(sorted(c["par"])), "%s: el par no es el esperado" % ld
        print("     clase LEIDA hoy antes de tocar: %s" % e["clase"])
        # LA IDEMPOTENCIA VA DELANTE DEL ASSERT (correccion de la propia vuelta 156):
        # en la segunda corrida la clase leida es LA NUEVA, y exigirle la vieja hacia
        # que el instrumento no se pudiera re correr para sellar su salida.
        if MARCA in e["razon"]:
            print("     YA ESTABA: no se duplica.")
            assert e["clase"] == c["clase_nueva"], (
                "%s trae la marca pero su clase es %s" % (ld, e["clase"]))
            continue
        assert e["clase"] == c["clase_vieja"], (
            "%s: la clase leida hoy es %s y no %s" % (ld, e["clase"], c["clase_vieja"]))
        bloque = ("  [CORRECCION DECLARADA (2026-09-03, vuelta 156, TAREA 3.b, " + MARCA
                  + " por la adjudicacion 6.2 del acta 155). EL TEXTO VIEJO NO SE BORRA Y LA "
                  "CLASE VIEJA SE NOMBRA: donde este par decia ~~clase " + c["clase_vieja"]
                  + "~~ pasa a CLASE " + c["clase_nueva"] + ". " + c["veredicto"]
                  + " n NO SE MUEVE y el grafo tampoco: esto cambia la LECTURA, no el archivo "
                  "del cribado.]")
        e["razon"] = e["razon"] + bloque
        e["cita"] = e["cita"] + "  [RECLASIFICADA A %s EN LA VUELTA 156: ver la razon]" % c["clase_nueva"]
        e["clase"] = c["clase_nueva"]
        movidas += 1
        print("     clase escrita: %s (razon +%d caracteres)" % (c["clase_nueva"], len(bloque)))

    if movidas:
        with io.open(REGISTRO, "w", encoding="utf-8", newline="\n") as fh:
            for x in E:
                fh.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n")

    D = entradas()
    assert len(D) == len(E) == 154, "el numero de lineas del registro se movio"
    for ld in sorted(CASOS):
        vieja = next(x for x in E if x["cita"].startswith(ld))
        nueva = next(x for x in D if x["cita"].startswith(ld))
        assert nueva["clase"] == CASOS[ld]["clase_nueva"], "%s no quedo en su clase" % ld
        assert nueva["razon"] == vieja["razon"], "%s no releyo lo que escribio" % ld
    print("")
    print("  ASSERT: 154 lineas antes y despues, y las dos clases escritas. OK")

    print("")
    print("  SEDE 2: docs/plan/LECTURAS_DIRIGIDAS.md")
    texto = io.open(LD_MD, encoding="utf-8").read()
    for ld in sorted(CASOS):
        c = CASOS[ld]
        a, b = c["par"]
        patron = re.compile(
            r"(\| %s \| REGISTRO DE CITAS `OP-C-05` \| %s <-> %s \| )%s( \| %s \| )([^\n|]+)(\|)"
            % (c["fila"], re.escape(a), re.escape(b), c["clase_vieja"], re.escape(ld)))
        m = patron.search(texto)
        if m is None:
            if ("| %s | REGISTRO DE CITAS `OP-C-05` | %s <-> %s | %s |"
                    % (c["fila"], a, b, c["clase_nueva"])) in texto:
                print("     %s YA ESTABA en %s" % (ld, c["clase_nueva"]))
                continue
            raise AssertionError("no se encontro la fila %s con la forma esperada" % c["fila"])
        nota = (" CORRECCION DECLARADA (vuelta 156, " + MARCA + "): la clase pasa de ~~"
                + c["clase_vieja"] + "~~ a " + c["clase_nueva"]
                + ". No hay dos lineas que nombrar, una en cada nodo, y sin figura no hay C "
                "(adjudicacion 6.2 del acta 155). Lectura entera en la razon del registro de "
                "citas y en docs/loop/SALIDA_V156_T3B_RELECTURA.txt.")
        vieja = m.group(0)
        nueva = (m.group(1) + c["clase_nueva"] + m.group(2)
                 + m.group(3).rstrip() + nota + " " + m.group(4))
        texto = texto.replace(vieja, nueva)
        print("     %s fila %s reescrita: clase %s -> %s, razon +%d caracteres"
              % (ld, c["fila"], c["clase_vieja"], c["clase_nueva"], len(nueva) - len(vieja)))
    with io.open(LD_MD, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)

    hoy = io.open(LD_MD, encoding="utf-8").read()
    for ld in sorted(CASOS):
        c = CASOS[ld]
        marca = ("| %s | REGISTRO DE CITAS `OP-C-05` | %s <-> %s | %s |"
                 % (c["fila"], c["par"][0], c["par"][1], c["clase_nueva"]))
        assert marca in hoy, "la fila %s no quedo en %s" % (c["fila"], c["clase_nueva"])
    print("     ASSERT: las dos filas quedan en D en el fichero de lecturas. OK")

    print("")
    print("GUARDA DE FRONTERA, DESPUES")
    despues = frontera("DESPUES")
    nombres = ("sha256 dataset/", "ficheros", "nodos", "vivos", "nodos_siguientes",
               "nodos_previos", "veredictos (n)")
    for nombre, x, y in zip(nombres, antes, despues):
        assert x == y, "LA FRONTERA SE CRUZO: %s cambio de %s a %s" % (nombre, x, y)
    print("  ASSERT: las siete magnitudes iguales. El registro cambia, EL GRAFO NO.")
    print("")
    F = entradas()
    LD = [x for x in F if x["via"] == "LECTURA_DIRIGIDA"]
    porclase = {k: sum(1 for x in LD if x["clase"] == k) for k in sorted({x["clase"] for x in LD})}
    # LA CIFRA SE CUENTA DEL REGISTRO, NO DE LO QUE ESTA CORRIDA MOVIO (correccion
    # de la propia vuelta 156): `movidas` vale 2 la primera vez y 0 la segunda, asi
    # que una salida sellada en la segunda corrida publicaba un 0 que no describe
    # nada. Se cuentan las entradas que llevan la marca de esta tarea.
    con_marca = sum(1 for x in F if MARCA in x["razon"])
    print("movidas EN ESTA CORRIDA: %d (0 si el bloque ya estaba escrito)" % movidas)
    print("CIFRA lecturas dirigidas reclasificadas por la TAREA 3.b: %d par(es)" % con_marca)
    print("CIFRA clases de las lecturas dirigidas tras la tarea: %s"
          % json.dumps(porclase, ensure_ascii=False))
    print("CIFRA veredictos del cribado: %d fila(s), y n NO se mueve." % despues[6])


main()
