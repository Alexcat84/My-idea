# -*- coding: utf-8 -*-
"""vuelta156_tarea2b_decidir_ld097.py . TAREAS 2.b, 2.c, 2.d y 2.e DE LA VUELTA 156.

LA DECISION DE `LD-OPC05-097` CON LA VARA, DESPUES DE HABER VERIFICADO CONTRA EL
GRAFO (TAREA 2.a, salidas SALIDA_V156_T2A_CONTRA_GRAFO.txt y
SALIDA_V156_T2A_PASOS_CON_HIJO.txt).

QUE HACE, Y EN ESTE ORDEN:
  2.d (ANTES)  guarda de frontera: sha256 de todo dataset/, censo y aristas, y
               numero de veredictos del cribado. Se mide ANTES de tocar nada.
  2.b          escribe la clase decidida en LAS DOS SEDES (el registro de citas
               y docs/plan/LECTURAS_DIRIGIDAS.md), con CORRECCION DECLARADA y
               con el texto viejo entero como PREFIJO.
  2.c          el par NO se registra como candidato a fusion, porque la decision
               NO es A. La fusion no se ejecuta y no habia nada que ejecutar.
  2.d (DESPUES) la misma guarda de frontera, con assert: el registro cambia, EL
               GRAFO NO, y n no se mueve.

LA CLASE QUE SE ESCRIBE Y POR QUE, en una linea: NI C NI A, SINO D. El detalle
entero va en el reporte de la vuelta 156 y en la propia razon del registro.

USO:  python scripts/loop/vuelta156_tarea2b_decidir_ld097.py
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

CITA = "LD-OPC05-097"
CLASE_VIEJA = "C"
CLASE_NUEVA = "D"
MARCA = "RELECTURA CONJUNTA DE LA VUELTA 156"

CORRECCION = (
    "  [CORRECCION DECLARADA (2026-09-03, vuelta 156, TAREA 2, "
    + MARCA + " por la adjudicacion 6.1 del acta 155). EL TEXTO VIEJO NO SE BORRA "
    "Y LA CLASE VIEJA SE NOMBRA: donde este par decia ~~clase C~~ pasa a CLASE D, "
    "sano y distinto, con la arista ya puesta. NI LA C QUE ESTABA ESCRITA NI LA A "
    "QUE EL ACTA 155 ADJUDICO. "
    "LA C CAE, y en eso el acta tiene razon: la C del 9.22 es sano CON FIGURA y la "
    "figura exige DOS LINEAS DISTINTAS, UNA EN CADA NODO (adjudicacion 6.2 del acta "
    "155). Se puede nombrar la linea de juran que el viaje expande (su paso 2, "
    "'analizar sintomas, formular teorias, probarlas e identificar la causa raiz', "
    "que el viaje ejecuta en sus pasos 1 a 4 con el Pareto, los diagramas causa "
    "efecto, el mecanismo de recoleccion y la validacion estadistica), PERO NO SE "
    "PUEDE NOMBRAR NINGUNA LINEA DEL VIAJE QUE JURAN EXPANDA: juran no expande, "
    "enuncia. Sin la segunda linea no hay figura y no hay C. "
    "LA A NO SE SOSTIENE, Y LO QUE LA TUMBA ES UNA MEDICION CONTRA EL GRAFO, no una "
    "opinion. El caso del acta descansa en que los dos restos fuera del solape son "
    "LINEA 'sin procedimiento en ningun lado'. Medido hoy contra "
    "docs/plan/PASO_NODO_CALIBRADO.jsonl, docs/plan/OP_E_01_DECIDIDAS.jsonl y el "
    "grafo (salida docs/loop/SALIDA_V156_T2A_PASOS_CON_HIJO.txt): el paso 1 de juran "
    "NO tiene hijo, o sea que ES linea; pero el paso 7 del viaje, gestionar la "
    "resistencia predecible al cambio, SI TIENE HIJO VIVO, resistencia_al_cambio, "
    "con la arista ESCRITA por OP-E-01 en el tramo 4 y puesta hoy en las dos vistas. "
    "Por la formulacion literal del banco 9.6.2, 'la prueba de que el paso de la "
    "madre es un procedimiento es que existe el hijo que lo ejecuta', ese paso es un "
    "PROCEDIMIENTO NOMBRADO EN UNA LINEA y no una linea. Sin linea en los dos "
    "sentidos, el segundo polo del 9.22 no aplica y no hay fusion. "
    "LO QUE SI HAY, y es el tercer caso que el propio 9.22 nombra: PROCEDIMIENTO EN "
    "UN SOLO SENTIDO. El viaje trae a juran un procedimiento entero que juran no "
    "tiene (el Pareto para descartar variables no relevantes, el brainstorming y los "
    "diagramas causa efecto, la recoleccion disenada para correlacionar cada teoria "
    "con el defecto, la validacion estadistica de que teoria explica la mayoria, la "
    "prueba de los remedios bajo condiciones operativas reales y la gestion de la "
    "resistencia); juran trae al viaje UNA LINEA, su paso 1, esporadico contra "
    "cronico y el enunciado del problema, sin hijo que lo ejecute. Ahi hay MADRE E "
    "HIJO, la vara del 9.6.1 se aplica UNA VEZ y el par CONTINUA: clase D, arreglo "
    "de ENLACE, y el enlace ya esta puesto en las dos vistas y en los dos sentidos. "
    "Y LA DIRECCION IMPORTA (9.6.2): preguntar que anade juran al viaje es "
    "preguntarlo AL REVES, y por ese camino toda madre compacta repite, que es "
    "exactamente lo que el 9.6.2 existe para impedir. "
    "UN DATO MAS, MEDIDO Y NO SUPUESTO, que empuja al mismo sitio: "
    "viaje_diagnostico_remedial es el SUPERVIVIENTE DECLARADO DEL ACTO 30 "
    "(docs/plan/03_FUSIONES.md y docs/plan/INVENTARIO.jsonl), la familia del viaje "
    "diagnostico, y las cuatro piezas que absorbio por INCISO son justo el Pareto, "
    "los diagramas causa efecto, la recoleccion para correlacionar y la validacion "
    "estadistica. juran_rcca_metodo NO era miembro de esa familia. La casa ya leyo "
    "esta familia y dejo a juran fuera. "
    "NO ES CANDIDATO A FUSION y no se ejecuta ninguna fusion (adjudicacion 6.1 del "
    "acta 155): la decision no es A. "
    "QUEDA MARCADO COMO DISCUTIBLE 1 DEL REPORTE DE LA VUELTA 156, porque discrepa "
    "de la adjudicacion 6.1 del acta 155 en el destino aunque coincida con ella en "
    "que la C no se sostiene.]")

RAZON_MD = (
    " CORRECCION DECLARADA (vuelta 156, " + MARCA + "): la clase pasa de ~~C~~ a D. "
    "La C cae porque no hay segunda linea que nombrar (juran no expande ninguna linea "
    "del viaje: enuncia). La A no se sostiene porque el paso 7 del viaje, gestionar la "
    "resistencia, SI tiene hijo vivo, resistencia_al_cambio, con arista ESCRITA por "
    "OP-E-01 en el tramo 4 y puesta hoy, asi que por el banco 9.6.2 es procedimiento "
    "nombrado en una linea y no linea, y sin linea en los dos sentidos el segundo polo "
    "del 9.22 no aplica. Queda PROCEDIMIENTO EN UN SOLO SENTIDO: madre juran, hijo el "
    "viaje, el par CONTINUA y el arreglo es enlace, que ya esta puesto. Medicion en "
    "docs/loop/SALIDA_V156_T2A_PASOS_CON_HIJO.txt."
)


def sha256_de_arbol(patrones):
    """Un solo sha256 de TODO dataset/, nombre de fichero incluido, para que un
    renombrado tampoco pase inadvertido."""
    h = hashlib.sha256()
    rutas = []
    for p in patrones:
        rutas += sorted(glob.glob(p))
    for ruta in sorted(rutas):
        h.update(os.path.basename(ruta).encode("utf-8"))
        with open(ruta, "rb") as fh:
            h.update(fh.read().replace(b"\r\n", b"\n"))
    return h.hexdigest(), len(rutas)


def censo_y_aristas():
    todos = {}
    for ruta in sorted(glob.glob(NODOS)):
        d = json.load(io.open(ruta, encoding="utf-8"))
        nid = d.get("node_id") or os.path.splitext(os.path.basename(ruta))[0]
        todos[nid] = d
    vivos = sum(1 for n in todos.values() if not n.get("deprecado"))
    sig = sum(len(n.get("nodos_siguientes") or []) for n in todos.values())
    prev = sum(len(n.get("nodos_previos") or []) for n in todos.values())
    return len(todos), vivos, len(todos) - vivos, sig, prev


def frontera(momento):
    sha, n_ficheros = sha256_de_arbol([NODOS, META])
    nodos, vivos, depre, sig, prev = censo_y_aristas()
    ver = sum(1 for x in io.open(VEREDICTOS, encoding="utf-8") if x.strip())
    print("  %-8s sha256 de dataset/ (%d fichero(s)): %s" % (momento, n_ficheros, sha))
    print("  %-8s censo: %d nodos / %d vivos / %d deprecados" % (momento, nodos, vivos, depre))
    print("  %-8s aristas: nodos_siguientes %d / nodos_previos %d / suma %d"
          % (momento, sig, prev, sig + prev))
    print("  %-8s veredictos del cribado (n): %d" % (momento, ver))
    return (sha, n_ficheros, nodos, vivos, depre, sig, prev, ver)


def entradas():
    return [json.loads(x) for x in io.open(REGISTRO, encoding="utf-8") if x.strip()]


def main():
    print("=" * 98)
    print("VUELTA 156, TAREAS 2.b a 2.e: LA DECISION DE LD-OPC05-097 CON LA VARA")
    print("=" * 98)
    print("")
    print("2.d GUARDA DE FRONTERA, ANTES DE TOCAR NADA")
    print("-" * 98)
    antes = frontera("ANTES")
    print("")

    print("2.b LA DECISION, ESCRITA EN LAS DOS SEDES, POR CORRECCION DECLARADA")
    print("-" * 98)
    print("  DECIDIDA: %s -> %s. NI la C escrita NI la A que adjudico el acta 155."
          % (CLASE_VIEJA, CLASE_NUEVA))
    print("")

    # --- SEDE 1: el registro de citas ---
    E = entradas()
    tocada = None
    for e in E:
        if e["cita"].startswith(CITA):
            tocada = e
            break
    assert tocada is not None, "no se encontro la entrada %s en el registro" % CITA
    cita_vieja = tocada["cita"]
    razon_vieja = tocada["razon"]
    clase_leida = tocada["clase"]
    print("  SEDE 1: docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl")
    print("     clase LEIDA hoy antes de tocar: %s" % clase_leida)
    assert clase_leida == CLASE_VIEJA, (
        "la clase de %s no es %s sino %s: el registro no esta donde se creia"
        % (CITA, CLASE_VIEJA, clase_leida))
    if MARCA in razon_vieja:
        print("     YA ESTABA: la marca ya vive en la razon. No se duplica.")
    else:
        tocada["clase"] = CLASE_NUEVA
        tocada["razon"] = razon_vieja + CORRECCION
        tocada["cita"] = cita_vieja + "  [RECLASIFICADA A %s EN LA VUELTA 156: ver la razon]" % CLASE_NUEVA
        with io.open(REGISTRO, "w", encoding="utf-8", newline="\n") as fh:
            for x in E:
                fh.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n")
        print("     clase escrita: %s. razon ampliada +%d caracteres. cita ampliada +%d."
              % (CLASE_NUEVA, len(CORRECCION),
                 len(tocada["cita"]) - len(cita_vieja)))

    D = entradas()
    puesta = [x for x in D if x["cita"].startswith(CITA)][0]
    assert puesta["clase"] == CLASE_NUEVA, "la clase no quedo escrita"
    assert puesta["razon"].startswith(razon_vieja), "el texto viejo de razon NO es prefijo"
    assert puesta["cita"].startswith(cita_vieja), "el texto viejo de cita NO es prefijo"
    assert len(D) == len(E) == 154, "el numero de lineas del registro se movio"
    print("     ASSERT: texto viejo de `razon` y de `cita` sigue siendo PREFIJO LITERAL. OK")
    print("     ASSERT: %d lineas antes, %d despues. OK" % (len(E), len(D)))

    # --- SEDE 2: docs/plan/LECTURAS_DIRIGIDAS.md ---
    print("")
    print("  SEDE 2: docs/plan/LECTURAS_DIRIGIDAS.md, la fila 97")
    texto = io.open(LD_MD, encoding="utf-8").read()
    if MARCA in texto:
        print("     YA ESTABA: la marca ya vive en la fila. No se duplica.")
    else:
        patron = re.compile(
            r"(\| 97 \| REGISTRO DE CITAS `OP-C-05` \| juran_rcca_metodo <-> "
            r"viaje_diagnostico_remedial \| )C( \| LD-OPC05-097 \| )([^\n|]+)(\|)")
        m = patron.search(texto)
        assert m is not None, "no se encontro la fila 97 con la forma esperada"
        vieja = m.group(0)
        nueva = (m.group(1) + CLASE_NUEVA + m.group(2)
                 + m.group(3).rstrip() + RAZON_MD + " " + m.group(4))
        texto = texto.replace(vieja, nueva)
        with io.open(LD_MD, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(texto)
        print("     fila reescrita: la celda de clase pasa de C a %s y la razon se AMPLIA"
              % CLASE_NUEVA)
        print("     (+%d caracteres), con la clase vieja nombrada dentro de la razon."
              % (len(nueva) - len(vieja)))
        print("     LA CELDA DE CLASE SE DEJA LIMPIA A PROPOSITO: el lector de este fichero")
        print("     (vuelta152_registro_de_citas_opc05.py) exige [A-Z]+ en esa celda, y un")
        print("     tachado ahi haria DESAPARECER el par del registro y pondria Gate 0 en")
        print("     rojo. La clase vieja no se pierde: vive en la razon de esta misma fila")
        print("     y en la `cita` y la `razon` del registro.")

    fila = [x for x in io.open(LD_MD, encoding="utf-8") if x.startswith("| 97 | REGISTRO DE CITAS")]
    assert len(fila) == 1, "la fila 97 no es unica"
    assert ("| juran_rcca_metodo <-> viaje_diagnostico_remedial | %s |" % CLASE_NUEVA) in fila[0], \
        "la celda de clase no quedo en %s" % CLASE_NUEVA
    assert MARCA in fila[0], "la correccion declarada no quedo en la fila"
    print("     ASSERT: la fila 97 es unica, su clase es %s y trae la correccion. OK" % CLASE_NUEVA)

    print("")
    print("2.c LA FUSION NO SE EJECUTA, Y NO HABIA NADA QUE EJECUTAR")
    print("-" * 98)
    print("  La adjudicacion 6.1 del acta 155 manda registrar CANDIDATO A FUSION solo SI la")
    print("  clase pasa a A. La decision de hoy es D, asi que NO se registra candidato, NO")
    print("  se elige superviviente y NO se toca una sola arista.")
    print("  CIFRA candidatos a fusion registrados: 0 par(es)")

    print("")
    print("2.d GUARDA DE FRONTERA, DESPUES")
    print("-" * 98)
    despues = frontera("DESPUES")
    print("")
    nombres = ("sha256 de dataset/", "ficheros de dataset/", "nodos", "vivos",
               "deprecados", "nodos_siguientes", "nodos_previos", "veredictos (n)")
    for nombre, a, b in zip(nombres, antes, despues):
        igual = a == b
        print("  %-24s antes=%s  despues=%s  IGUAL=%s"
              % (nombre, str(a)[:24], str(b)[:24], igual))
        assert igual, "LA FRONTERA SE CRUZO: %s cambio de %s a %s" % (nombre, a, b)
    print("")
    print("  ASSERT: el registro cambia, EL GRAFO NO. Las ocho magnitudes iguales.")
    print("  CIFRA veredictos del cribado: %d fila(s), y n NO se mueve." % despues[7])

    print("")
    print("CIFRA entradas del registro reclasificadas: 1 par(es)")
    print("CIFRA sedes corregidas: 2 fichero(s)")


main()
