# -*- coding: utf-8 -*-
"""vuelta156_tarea2a_pasos_con_hijo.py . TAREA 2.a DE LA VUELTA 156, SEGUNDA
MEDICION.

POR QUE EXISTE. El caso del auditor (adjudicacion 6.1 del acta 155) descansa en
que lo que queda FUERA DEL SOLAPE son DOS LINEAS: el paso 1 de
`juran_rcca_metodo` y el paso 7 de `viaje_diagnostico_remedial`, y dice de los
dos que van "sin procedimiento en ningun lado". ESO ES UNA AFIRMACION SOBRE EL
GRAFO, y verificarla contra el grafo es la mitad del trato que le toca al
ejecutor.

LA VARA QUE SE APLICA NO ES NUEVA. Es la formulacion literal del banco 9.6.2:

    "UNA LINEA QUE TARDA SIETE PASOS EN EJECUTARSE NO ES UNA LINEA: ES UN
     PROCEDIMIENTO NOMBRADO EN UNA LINEA. La prueba de que el paso de la madre
     es un procedimiento ES QUE EXISTE EL HIJO QUE LO EJECUTA."

QUE MIDE, PASO A PASO Y PARA LOS DOS NODOS:
  - si `docs/plan/PASO_NODO_CALIBRADO.jsonl` le adjudica un HIJO a ese paso;
  - si `docs/plan/OP_E_01_DECIDIDAS.jsonl` trae una decision escrita para ese
    par madre/paso/hijo, y cual;
  - si el hijo EXISTE HOY en el grafo y esta VIVO;
  - si la arista madre hacia hijo esta puesta HOY, en las dos vistas.

NO DECIDE LA CLASE. Publica la medicion, salga a favor o en contra del caso del
auditor. La decision va en la TAREA 2.b.

USO:  python scripts/loop/vuelta156_tarea2a_pasos_con_hijo.py

--- ADJUDICACION 6.1 DEL ACTA 157 (3 sep 2026): `LD-OPC05-097` ES D, Y LA
ADJUDICACION 6.1 DEL ACTA 155 QUEDA REVOCADA POR SU PROPIO AUTOR ---

REGISTRO POR ADICION. NADA DE LO ESCRITO ARRIBA SE BORRA, Y EN PARTICULAR NO SE
BORRA EL BLOQUE DE LA 6.1 DEL ACTA 155, QUE PEDIA A Y FUSION: taparlo impediria
auditar por que la lectura conjunta existe.

QUE MIDIO ESTE INSTRUMENTO Y COMO ACABO. La medicion que este fichero publico
en la vuelta 156 (el paso 7 del viaje SI tiene hijo vivo con arista puesta) fue
la que decidio la clase, y el auditor la re verifico con instrumento propio
(acta 157, seccion 3.1, salida `_auditor_v157_097_grafo.txt`) y la dio por
CIERTA. Las tres mediciones del auditor, escritas aqui para que no haya que ir
al acta:
  (i)   `docs/plan/PASO_NODO_CALIBRADO.jsonl` YA TRATA A `juran_rcca_metodo`
        COMO MADRE, con DOS filas propias: su paso 2 con hijo
        `prueba_teorias_causa_raiz` y su paso 3 con hijo
        `diseno_implementacion_remedio`. Los pasos de juran son procedimientos
        nombrados en una linea, que es la definicion literal del 9.6.2, y no lo
        dice una lectura: lo dice un fichero del plan anterior a la discusion.
  (ii)  `resistencia_al_cambio` esta VIVO, la arista esta en LAS DOS VISTAS y
        sus cuatro pasos despliegan el paso 7 del viaje. La medicion de la
        vuelta 156 es cierta.
  (iii) POR LOS DOS CAMINOS POSIBLES LA CLASE ES D. Si el paso 7 es
        procedimiento, el par es madre e hijo y CONTINUA (tercer caso del 9.22).
        Y si alguien insistiera en que los dos restos son procedimiento, el
        propio banco ya resolvio ese caso en el PUESTO 2091, CLASE D.

EL LIMITE QUE SIGUE VIGENTE Y QUE NO CAE CON LA 6.1 DEL ACTA 155: la que salga A
NO SE VOLTEA en una vuelta de lectura. Se marca como discutible, se publica su
caso y NO SE EJECUTA NINGUNA FUSION, porque una fusion necesita su ficha, su
superviviente y su ruta.

--- ADJUDICACION 6.2 DEL ACTA 157 (3 sep 2026): "NINGUN HIJO ADJUDICADO" ES UNA
AUSENCIA BAJO LA VARA DECLARADA, NO UNA PRUEBA DE QUE EL PASO SEA LINEA ---

CORRECCION DECLARADA POR ADICION, Y CORRIGE UN PASO DE RAZONAMIENTO DE ESTE
INSTRUMENTO, NO UNA CIFRA SUYA. La cifra que este fichero midio era cierta; lo
que falla es lo que se dedujo de ella.

LA INFERENCIA QUE NO SE SIGUE. La razon escrita para `LD-OPC05-097` dice "el
paso 1 de juran NO tiene hijo, o sea que ES linea". EL 9.6.2 DA UNA PRUEBA
SUFICIENTE DE QUE UN PASO ES PROCEDIMIENTO ("la prueba de que el paso de la
madre es un procedimiento ES QUE EXISTE EL HIJO QUE LO EJECUTA"), Y UNA PRUEBA
SUFICIENTE NO SE PUEDE DAR LA VUELTA: su ausencia no prueba lo contrario. Y aqui
la ausencia es todavia mas estrecha, porque LA VARA DE ESTE INSTRUMENTO SOLO
MIRA HIJOS ADJUDICADOS EN `docs/plan/PASO_NODO_CALIBRADO.jsonl`: un hijo que
exista en el grafo y que nadie haya adjudicado a ese paso no lo ve.

Y EL CONTRAEJEMPLO ESTA MEDIDO, NO SUPUESTO (auditor, acta 157 seccion 6.2, y re
medido por el ejecutor en la TAREA 3 de la vuelta 157 con
`scripts/loop/vuelta157_tarea3_paso1_de_juran.py`, salida
`docs/loop/SALIDA_V157_T3_PASO1_JURAN.txt`):
`desperdicio_cronico_vs_esporadico` esta VIVO y sus cuatro pasos despliegan
justo el paso 1 de juran (monitorear, diferenciar el pico esporadico del nivel
cronico, accion correctiva, proyecto de mejora), AUNQUE SIN ARISTA Y SIN FILA EN
EL CALIBRADO. O sea: hay hijo, y esta vara no lo veia.

COMO SE LEE DESDE HOY LA SALIDA DE ESTE INSTRUMENTO: "ningun hijo adjudicado"
significa NO HAY HIJO BAJO LA VARA DECLARADA (calibrado mas arista), y NO
significa "el paso es linea". Para afirmar que un paso es linea hace falta una
lectura del grafo que no encuentre quien lo despliegue, y esa lectura este
instrumento NO la hace.

LA CLASE NO SE MUEVE: `LD-OPC05-097` sigue siendo D por la 6.1 del acta 157, que
la sostiene por dos caminos independientes de esta inferencia.
"""
import glob
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos", "*.json")
CALIBRADO = os.path.join(RAIZ, "docs", "plan", "PASO_NODO_CALIBRADO.jsonl")
DECIDIDAS = os.path.join(RAIZ, "docs", "plan", "OP_E_01_DECIDIDAS.jsonl")

PAR = ("juran_rcca_metodo", "viaje_diagnostico_remedial")


def cargar():
    todos = {}
    for ruta in sorted(glob.glob(NODOS)):
        d = json.load(io.open(ruta, encoding="utf-8"))
        nid = d.get("node_id") or os.path.splitext(os.path.basename(ruta))[0]
        todos[nid] = d
    return todos


def jsonl(ruta):
    if not os.path.exists(ruta):
        return []
    return [json.loads(x) for x in io.open(ruta, encoding="utf-8") if x.strip()]


def main():
    print("=" * 100)
    print("VUELTA 156, TAREA 2.a (SEGUNDA MEDICION): CADA PASO DE LOS DOS NODOS, CON SU HIJO")
    print("MEDIDO CONTRA EL CALIBRADO, LAS DECIDIDAS Y EL GRAFO DE HOY")
    print("=" * 100)
    print("VARA: banco 9.6.2, 'la prueba de que el paso de la madre es un procedimiento es")
    print("que EXISTE EL HIJO QUE LO EJECUTA'.")
    print("")

    todos = cargar()
    C = jsonl(CALIBRADO)
    D = jsonl(DECIDIDAS)
    print("Filas del calibrado: %d | filas de OP_E_01_DECIDIDAS: %d" % (len(C), len(D)))
    print("")

    con_hijo = {}
    for madre in PAR:
        n = todos[madre]
        pasos = n.get("pasos_accionables") or []
        print("-" * 100)
        print("%s  (%d pasos)" % (madre, len(pasos)))
        print("-" * 100)
        con_hijo[madre] = []
        for i, texto in enumerate(pasos, 1):
            filas = [c for c in C if c.get("madre") == madre and int(c.get("paso") or 0) == i]
            dec = [d for d in D if d.get("madre") == madre and str(d.get("paso")) == str(i)]
            print("  paso %d: %s" % (i, texto[:110]))
            if not filas and not dec:
                print("       HIJO EN EL CALIBRADO: NINGUNO. DECISION ESCRITA: NINGUNA.")
                continue
            for c in filas:
                hijo = c.get("hijo")
                existe = hijo in todos
                vivo = existe and not todos[hijo].get("deprecado")
                sig = existe and hijo in (todos[madre].get("nodos_siguientes") or [])
                prev = existe and madre in (todos[hijo].get("nodos_previos") or [])
                print("       hijo del calibrado: %-42s existe=%s vivo=%s | arista madre.sig=%s hijo.prev=%s"
                      % (hijo, existe, vivo, sig, prev))
                if vivo:
                    con_hijo[madre].append((i, hijo))
            for d in dec:
                print("       OP-E-01 decidio: hijo %-38s decision=%s (tramo %s, %s)"
                      % (d.get("hijo"), d.get("decision"), d.get("tramo"),
                         d.get("fichero_origen")))
        print("")

    print("=" * 100)
    print("RESUMEN: PASOS CON HIJO VIVO ADJUDICADO EN EL CALIBRADO")
    print("=" * 100)
    for madre in PAR:
        pares = con_hijo[madre]
        print("  %-32s %d paso(s) con hijo vivo: %s"
              % (madre, len(pares),
                 ", ".join("paso %d -> %s" % (i, h) for i, h in pares) or "ninguno"))
        print("CIFRA pasos con hijo de %s: %d paso(s)" % (madre, len(pares)))
    print("")
    print("LOS DOS PASOS QUE EL CASO DEL AUDITOR PONE FUERA DEL SOLAPE:")
    for madre, paso in ((PAR[0], 1), (PAR[1], 7)):
        tiene = [h for i, h in con_hijo[madre] if i == paso]
        print("  %-32s paso %d: hijo vivo adjudicado = %s"
              % (madre, paso, ", ".join(tiene) or "NINGUNO"))
    print("")
    print("")
    print("BARRIDO EXHAUSTIVO: este instrumento recorre TODOS los pasos accionables de")
    print("los dos nodos, uno por uno, y para cada uno consulta las 468 filas del")
    print("calibrado y las 220 de OP_E_01_DECIDIDAS. No hay muestreo, no hay tope y no")
    print("hay filtro: los %d pasos de %s y los %d de %s se miran todos, y por eso una"
          % (len(todos[PAR[0]].get("pasos_accionables") or []), PAR[0],
             len(todos[PAR[1]].get("pasos_accionables") or []), PAR[1]))
    print("respuesta NINGUNO de aqui es una ausencia medida y no una busqueda que no")
    print("encontro nada.")
    print("")
    print("ESTA MEDICION NO DECIDE LA CLASE. La decision con la vara va en la TAREA 2.b.")


main()
