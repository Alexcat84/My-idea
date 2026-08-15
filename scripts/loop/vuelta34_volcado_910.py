# -*- coding: utf-8 -*-
"""vuelta34_volcado_910.py - EL LOTE del paso 3 del orden interno de OP-D-03.

SUCESOR DECLARADO de scripts/loop/vuelta33_volcado_910_b.py, con la misma
disciplina y el cambio dicho (EJECUTOR.md regla 2): aquel volcaba tres congelados
de una FUSION y este vuelca los dos que un DESTEJIDO libera.

  738  B -> D   ab_testing_optimizacion contra split_testing_experimentos_ab
  1061 A -> D   ab_testing_optimizacion contra optimizacion_embudo_get_customers

POR QUE SE PUEDEN JUZGAR HOY, y no es una opinion: las dos razones viejas
escribieron su propia condicion de desbloqueo y las dos se cumplieron.

  - el 738 estaba congelado por el TOQUE UNICO del banco 9.4 con el refinamiento
    del 673, porque LOS DOS nodos estaban averiados por dentro. Medido hoy: los
    dos tienen CINCO pasos y ninguna juntura (split_testing_experimentos_ab lo
    destejio OP-F-04-RAC; ab_testing_optimizacion, esta misma vuelta).
  - el 1061 estaba congelado por dependencia y su razon vieja escribio la
    prediccion literal: "si el destejido deja a optimizacion_embudo con el A/B en
    una sola linea y a ab_testing como su procedimiento, el par pasa a D. No se
    puede saber antes". SE PUEDE SABER AHORA, y la condicion se cumple.

LA RAZON VIEJA SE COPIA DEL ARCHIVO POR MAQUINA, verbatim, y el script ABORTA si
no queda literalmente dentro de la nueva.

Uso: python scripts/loop/vuelta34_volcado_910.py
Salida: docs/loop/_lote_v34.jsonl. El archivo lo escribe scripts/corregir_veredicto.py.
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
LOTE = os.path.join(RAIZ, "docs", "loop", "_lote_v34.jsonl")

FECHA = "15 ago 2026"

CABECERA = (
    "REESCRITA EL %s POR EL DESTEJIDO DE OP-D-03, y la clase pasa de %%s a D. CORRECCION "
    "DECLARADA. El congelamiento se levanta porque su causa CAYO, medida hoy sobre el arbol "
    "y no recordada: ab_testing_optimizacion quedo estable el 15 ago 2026 con CINCO pasos, "
    "tras el destejido de la costura que su propia tabla de fronteras habia dejado escrita "
    "(01_FUENTES.md linea 947: los pasos 1 a 5 y 6 a 10 dicen la misma prueba A/B dos veces). "
    "El volcado va por el banco 9.10, con su barrido de tablas derivadas en el mismo acto. "
    % FECHA
)

CLASES = {738: ("B", "D"), 1061: ("A", "D")}

CUERPO = {
    738: (
        "POR QUE YA SE PUEDE JUZGAR: la razon vieja bloqueaba porque LOS DOS NODOS ESTABAN "
        "AVERIADOS POR DENTRO y el solape cruzaba LAS DOS JUNTURAS. MEDIDO HOY, LAS DOS CIRUGIAS "
        "ESTAN HECHAS: split_testing_experimentos_ab tiene CINCO pasos y no nueve, porque su "
        "bloque 6 a 9 (el grupo de control de desempeno inicial parecido y la diferencia neta) "
        "salio con OP-F-04-RAC hacia metodologia_evaluacion_entrenamiento_ventas, y su campo de "
        "fuente ya no declara dos libros sino uno, The Lean Startup; y ab_testing_optimizacion "
        "tiene CINCO pasos y no quince, porque OP-F-04-WEI se llevo el bloque 11 a 15 al anillo "
        "interior y esta vuelta colapso la repeticion del 1 a 5 contra el 6 a 10. NINGUNO DE LOS "
        "DOS TIENE JUNTURA. LA LECTURA, CONTRA LOS CINCO PASOS DE CADA UNO. Lo compartido es LA "
        "MECANICA: partir en dos, medir con las mismas metricas y comparar. Lo propio de "
        "ab_testing_optimizacion es el catalogo de elementos de la landing page que se prueban "
        "(botones, titulares, imagenes, ofertas, ubicacion de CTA, copy, prueba social y numero "
        "de campos de formulario), la eleccion de la metrica, la duracion en semanas con una sola "
        "metrica a la vez, y el cierre del ciclo implementando la ganadora y pasando a la "
        "siguiente metrica. Lo propio de split_testing_experimentos_ab es OTRO OBJETO ENTERO: la "
        "HIPOTESIS sobre el impacto de una FUNCIONALIDAD NUEVA, partir LA BASE DE CLIENTES y no "
        "el trafico, dejar al grupo A con la version estandar, y concluir si la funcionalidad "
        "tuvo impacto real en el comportamiento. Y LOS ENTREGABLES LO DICEN SIN AMBIGUEDAD, "
        "leidos hoy en los dos ficheros: plan de pruebas A/B con elementos priorizados y decision "
        "sobre la version ganadora, contra reporte de un experimento A/B con conclusiones sobre "
        "el impacto de una funcionalidad. UNO OPTIMIZA UNA PAGINA, EL OTRO DECIDE SI UNA "
        "FUNCIONALIDAD MERECE EXISTIR. CONTINUA: D, los dos sanos. ARISTA, BUSCADA HOY EN LOS DOS "
        "SENTIDOS CONTRA EL GRAFO: NO HAY NINGUNA, y NO SE DECLARA ARISTA QUE FALTA, con el "
        "criterio escrito el 15 ago 2026 en 02_DESTEJIDOS.md: la arista se declara donde lo "
        "compartido es un BLOQUE que uno expande de una LINEA del otro, y aqui no hay madre ni "
        "hijo, hay dos procedimientos completos que comparten una mecanica generica. DISCUTIBLE "
        "MARCADO: el archivo llamo A al 452 (ab_testing contra split_testing) y al 374 "
        "(split_testing contra split_testing_experimentos_ab), asi que quien encadene esas dos A "
        "dira que esta tambien lo es. Lo que separa este caso, y es lo que sostengo, es el "
        "objeto: la funcionalidad nueva no es un elemento de la pagina. Y QUEDA DECLARADO, SIN "
        "ARREGLARLO AQUI, que el 452 y el 1575 se emitieron contra los QUINCE pasos de "
        "ab_testing_optimizacion y hoy ese texto tiene cinco: entran en LA COLA DE RELECTURA por "
        "el mismo 9.4 que libera a este par."
    ),
    1061: (
        "POR QUE YA SE PUEDE JUZGAR, Y LA PREDICCION DE LA RAZON VIEJA ACERTO AL PIE DE LA LETRA. "
        "Aquella escribio: si el destejido deja a optimizacion_embudo con el A/B en una sola "
        "linea y a ab_testing como su procedimiento, el par pasa a D. MEDIDO HOY: "
        "optimizacion_embudo_get_customers tiene CINCO pasos (su bloque 6 a 10 de Weinberg salio "
        "con OP-F-04-WEI) y su A/B vive EN UNA SOLA LINEA, el paso 3: ejecutar pruebas A/B "
        "controladas cambiando no mas de dos variables a la vez. Y ab_testing_optimizacion es "
        "EXACTAMENTE el procedimiento entero de esa linea, en sus cinco pasos de hoy: elegir la "
        "metrica y los elementos, disenar las dos versiones cambiando un solo elemento, repartir "
        "el trafico y dejarla correr, medir cada version, e implementar la ganadora documentando. "
        "LA PRUEBA DE RECONOCIMIENTO DE MADRE E HIJO DEL 9.6.2 SE CUMPLE, y en un solo sentido. Y "
        "LA MADRE CONSERVA MATERIA PROPIA QUE EL HIJO NO TOCA EN NINGUN PASO, que es la otra "
        "mitad de la prueba: exigir el MVP de alta fidelidad y el dashboard funcionando antes de "
        "empezar, definir las metricas segun EL TIPO DE NEGOCIO WEB (e-commerce, mercado "
        "multi-lado, marketplace), y calcular el LTV y compararlo con el CAQ antes de escalar la "
        "inversion. CONTINUA: D, los dos sanos, madre optimizacion_embudo_get_customers e hijo "
        "ab_testing_optimizacion. UNA CIFRA DE LA RAZON VIEJA QUE HOY YA NO SE SOSTIENE, y se "
        "dice en vez de repetirla: aquella contaba entre lo propio de ab_testing la confianza "
        "estadistica, y eso vivia en el bloque 11 a 15 que OP-F-04-WEI se llevo al anillo "
        "interior. Ya no esta en el nodo. ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS CONTRA EL "
        "GRAFO: NO HAY NINGUNA. D, SANO, CON ARISTA QUE FALTA, con direccion de madre a hijo, por "
        "el criterio escrito el 15 ago 2026: lo compartido es un BLOQUE (el procedimiento entero) "
        "que expande UNA LINEA de la madre. Queda declarada para la fase 04."
    ),
}


def main():
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_puesto = {v["puesto_intra"]: v for v in V}

    # GUARDA DEL DIA: los tres nodos que sostienen las dos lecturas tienen que
    # tener HOY los pasos que la razon nueva dice que tienen.
    esperado = {"ab_testing_optimizacion": 5, "split_testing_experimentos_ab": 5,
                "optimizacion_embudo_get_customers": 5}
    for nid, n in sorted(esperado.items()):
        d = json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))
        real = len(d.get("pasos_accionables") or [])
        print("  guarda del dia: %-38s %d pasos (la razon dice %d) %s"
              % (nid, real, n, "OK" if real == n else "ABORTA"))
        if real != n:
            return 1

    filas = []
    for puesto in sorted(CUERPO):
        v = por_puesto.get(puesto)
        if v is None:
            print("ABORTA: el puesto %d no esta registrado" % puesto)
            return 1
        vieja, nueva_clase = CLASES[puesto]
        if v["clase"] != vieja:
            print("ABORTA: el puesto %d esta en %r y el lote esperaba %r"
                  % (puesto, v["clase"], vieja))
            return 1
        razon_vieja = v["razon"]
        razon = (CABECERA % vieja
                 + "LO QUE DECIA LA RAZON VIEJA, y se deja escrita ENTERA para que la "
                   "correccion se pueda auditar (copiada del archivo por maquina, no "
                   "transcrita): " + razon_vieja + " FIN DE LA RAZON VIEJA. "
                 + CUERPO[puesto])
        if razon_vieja not in razon:
            print("ABORTA: la razon vieja del %d no queda literal dentro de la nueva" % puesto)
            return 1
        filas.append({"puesto": puesto, "clase": nueva_clase, "razon": razon})
        print("  %d: %s -> %s, razon vieja conservada LITERAL (%d caracteres)"
              % (puesto, vieja, nueva_clase, len(razon_vieja)))

    with io.open(LOTE, "w", encoding="utf-8") as fh:
        for f in filas:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")
    print("\nESCRITO el lote: %s (%d filas). El archivo lo escribe "
          "scripts/corregir_veredicto.py" % (os.path.relpath(LOTE, RAIZ), len(filas)))

    # La cifra ESPERADA del marcador, escrita ANTES de correr el instrumento que
    # lo recomputa, con orden de parar si da otra cosa.
    conteo = {}
    for v in V:
        conteo[v["clase"]] = conteo.get(v["clase"], 0) + 1
    print("\nMARCADOR DE AHORA, contado aqui: n %d, A %d, B %d, C %d, D %d"
          % (len(V), conteo.get("A", 0), conteo.get("B", 0), conteo.get("C", 0),
             conteo.get("D", 0)))
    print("MARCADOR ESPERADO TRAS EL VOLCADO, escrito ANTES de correr el instrumento: "
          "n %d, A %d, B %d, C %d, D %d"
          % (len(V), conteo.get("A", 0) - 1, conteo.get("B", 0) - 1, conteo.get("C", 0),
             conteo.get("D", 0) + 2))
    print("Si el instrumento da otra cosa, SE PARA.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
