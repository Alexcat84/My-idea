# -*- coding: utf-8 -*-
"""vuelta36_volcado_643.py - EL VOLCADO DEL 643, la sexta y ultima lectura del acto.

SUCESOR DECLARADO de scripts/loop/vuelta36_volcado_910.py, de esta misma vuelta, y
lo que cambia va dicho (EJECUTOR.md regla 2): aquel leia cinco razones YA ESCRITAS
de una propuesta sellada por otra vuelta y este SI escribe la razon, porque la
lectura dirigida del 643 es de HOY y no existia sellada en ningun sitio.

  643  A -> D   split_testing contra test_ab_precio

Y VA DICHA DE ENTRADA LA DIFERENCIA DE ESPECIE CON LAS CINCO ANTERIORES, porque
callarla seria vender esta como si fuera la sexta de una tanda uniforme:

  LAS CINCO SE VOLTEARON PORQUE EL TEXTO HABIA CAMBIADO BAJO EL VEREDICTO. Sus
  razones viejas afirmaban cosas que hoy son falsas sobre el fichero.

  EL 643 NO. Sus dos nodos no cambiaron una coma, y por eso NO estaba rancio
  (SALIDA_V35_RANCIOS.txt lo puso en la lista de AL DIA). Su razon vieja describe
  el texto de hoy con exactitud, incluidos LOS DOS PROPIOS que esta lectura vuelve
  a encontrar. LO QUE CAMBIA AQUI ES EL CRITERIO, NO EL TEXTO, y por eso el par se
  lee por el mandato de P.5 de leer el ACTO ENTERO antes de fundirlo, con el
  alcance que el fundador fijo el 15 ago 2026: dentro del acto en operacion y
  nunca fuera.

LA RAZON VIEJA SE COPIA DEL ARCHIVO POR MAQUINA, verbatim, y el script ABORTA si
no queda literalmente dentro de la nueva.

Uso: python scripts/loop/vuelta36_volcado_643.py
Salida: docs/loop/_lote_v36_643.jsonl. El archivo lo escribe scripts/corregir_veredicto.py.
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
LOTE = os.path.join(RAIZ, "docs", "loop", "_lote_v36_643.jsonl")

PUESTO = 643
A = "split_testing"
B = "test_ab_precio"
PASOS_HOY = {A: 4, B: 5}
CLASE_VIEJA = "A"
CLASE_NUEVA = "D"

# La cifra que este volcado deja, escrita ANTES de correr el instrumento.
ESPERADO = {"n": 3388, "A": 575, "B": 83, "C": 8, "D": 2722}

CABECERA = (
    "REESCRITA EL 18 ago 2026 POR LA LECTURA DIRIGIDA LD-82, y la clase pasa de A a D. "
    "CORRECCION DECLARADA, con el texto viejo entero debajo. "
    "Y LO PRIMERO QUE SE DICE ES LA DIFERENCIA CON LAS CINCO RELECTURAS DEL MISMO DIA, porque "
    "presentarla como la sexta de una tanda uniforme seria mentir por omision: AQUELLAS CINCO SE "
    "VOLTEARON PORQUE EL TEXTO HABIA CAMBIADO BAJO EL VEREDICTO, y sus razones viejas afirmaban "
    "cosas que hoy son falsas sobre el fichero. ESTA NO. Los dos nodos de este par NO CAMBIARON "
    "UNA COMA, medido con las dos varas de la vuelta 35 (fecha de lectura contra fecha de cambio "
    "de los ficheros, y comparacion del texto de los pasos en el commit de la lectura contra el "
    "de hoy), y por eso este par salio en la lista de AL DIA y no en la de rancios. LA RAZON "
    "VIEJA DESCRIBE EL TEXTO DE HOY CON EXACTITUD, incluidos los dos propios que esta lectura "
    "vuelve a encontrar. LO QUE CAMBIA AQUI ES EL CRITERIO, NO EL TEXTO, y queda escrito asi "
    "para que se pueda discutir por lo que es. "
    "POR QUE SE LEE IGUAL: P.5 manda leer el ACTO ENTERO despues de su destejido y ANTES de su "
    "fusion, y el fundador lo adjudico el 15 ago 2026 con su alcance escrito, dentro del acto en "
    "operacion y nunca fuera. Este es el ultimo par sin releer del acto de OP-D-03. La lectura va "
    "con los dos nodos impresos ENTEROS delante y la arista buscada en LOS DOS SENTIDOS contra el "
    "grafo, con el resolutor de alias aplicado antes de comparar por P.1. "
)

CUERPO = (
    "LA MEDICION QUE SOSTIENE ESTA LECTURA NO ES EL CRITERIO DEL 738, Y ESO ES A PROPOSITO. "
    "Las cinco relecturas de esta misma vuelta se decidieron con aquel criterio (la mecanica "
    "compartida no basta, el objeto decide), y aquel criterio lo escribio la vuelta 34, QUE NADIE "
    "HA AUDITADO. Colgar un sexto veredicto de la misma vara heredada, y sola, seria encadenar "
    "seis lecturas a un criterio sin auditar. ASI QUE EL 643 SE MIDE PRIMERO CON UNA VARA QUE NO "
    "DEPENDE DE EL: LA CONTENCION. Un par REPITE cuando el contenido de uno vive DENTRO del otro. "
    "MEDIDO PASO POR PASO CON EL TEXTO DELANTE (scripts/loop/vuelta36_ld_643.py, salida en "
    "docs/loop/SALIDA_V36_LD_643.txt), y la correspondencia se declara solo donde el GESTO es el "
    "mismo, no donde los dos hablan del mismo tema. "
    "DE LOS CUATRO PASOS DE split_testing, DOS TIENEN PAREJA: definir las variaciones a testear "
    "contra definir las variantes a testear, que es casi verbatim; y medir la tasa de conversion "
    "del CTA de cada variante contra medir el porcentaje de usuarios que prefiere cada una, mismo "
    "gesto con otra metrica. LOS OTROS DOS NO LA TIENEN: dividir el trafico EQUITATIVAMENTE entre "
    "control y retador, que en el otro nodo no existe (su paso 2 manda implementar en un canal "
    "real, que es otra cosa); y ASEGURAR SIGNIFICANCIA ESTADISTICA POR ENCIMA DEL 95 POR CIENTO "
    "ANTES DE CONCLUIR, que NO ESTA EN NINGUN PASO del otro. "
    "Y DE LOS CINCO PASOS DE test_ab_precio, TRES NO TIENEN PAREJA: implementar el test en un "
    "canal real, que el otro no nombra nunca; EJECUTAR MULTIPLES RONDAS PARA AFINAR EL PRECIO "
    "OPTIMO, que el otro no hace porque no itera, concluye una vez con la significancia en la "
    "mano; y seleccionar el precio o modelo validado con mayor conversion, o sea QUEDARSE CON LA "
    "GANADORA, que el otro nodo NO TIENE COMO PASO, porque su cierre es el umbral estadistico. "
    "LA ARITMETICA: split_testing conserva 2 propios de 4, el 50 por ciento; test_ab_precio "
    "conserva 3 propios de 5, el 60 por ciento. NINGUNO CONTIENE AL OTRO Y CADA LADO CONSERVA LA "
    "MAYORIA DE SUS PROPIOS PASOS. Eso no es repetir. "
    "Y LO SEGUNDO, QUE ES LO QUE DE VERDAD DECIDE, ESTA ESCRITO DENTRO DE LA PROPIA RAZON VIEJA Y "
    "JUEGA CONTRA SU CLASE. Aquella cierra diciendo, con estas palabras, que lo propio de "
    "test_ab_precio son LAS RONDAS MULTIPLES para afinar hasta el precio optimo, QUE EL GENERAL NO "
    "PIDE; y que lo propio de split_testing es el UMBRAL DEL NOVENTA Y CINCO POR CIENTO, que es lo "
    "que impide declarar ganador a un ruido, Y ES LO MAS CARO DE PERDER DE LOS DOS. UNA A LLEVA A "
    "FUNDIR, Y FUNDIR ES QUE UNO DE LOS DOS MUERA. Si lo mas caro de perder vive en un lado y la "
    "busqueda iterativa del optimo vive en el otro, entonces la fusion tendria que conservarlos "
    "los dos, Y ESO NO ES LA FORMA DE UN PAR QUE REPITE: ES LA FORMA DE UN PAR QUE CONTINUA. LA "
    "RAZON VIEJA NOMBRO EL MOTIVO PARA NO FUNDIR Y AUN ASI CLASIFICO A. "
    "LOS ENTREGABLES LO DICEN SIN AMBIGUEDAD, y el 9.6.2 dice que deciden mas rapido que los "
    "pasos, leidos hoy en los dos ficheros: RESULTADOS COMPARATIVOS DE CONVERSION ENTRE VARIANTES "
    "CON SIGNIFICANCIA ESTADISTICA, contra UN PRECIO O MODELO DE MONETIZACION VALIDADO CON DATOS "
    "DE CONVERSION REALES DE AL MENOS CIENTOS DE USUARIOS TESTEADOS. El primero entrega una "
    "comparacion valida; el segundo entrega una decision sobre cuanto y como se cobra. Dos "
    "productos distintos. Y LAS CONDICIONES DE ACTIVACION TAMBIEN: cuando hay multiples "
    "alternativas de propuesta de valor, precio o mensaje que comparar, contra cuando hay "
    "incertidumbre sobre el precio o el modelo de ingresos y multiples opciones de monetizacion "
    "viables. "
    "LA PRUEBA DE MADRE E HIJO DEL 9.6.2 SE CORRIO Y NO SE CUMPLE, y se dice porque es la lectura "
    "que un auditor va a probar primero: la regla pide que EL HIJO QUEPA ENTERO DENTRO DE UN PASO "
    "DE LA MADRE. test_ab_precio no cabe en ninguno de los cuatro pasos de split_testing: TRES de "
    "sus cinco pasos no tienen casa en ningun paso del otro. El precio aparece en split_testing "
    "como UNA PALABRA dentro del parentesis del paso 1, no como una linea que sea un procedimiento "
    "nombrado. NO HAY MADRE E HIJO. "
    "CONTINUA: D, los dos sanos. "
    "ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS CONTRA EL GRAFO Y CON EL RESOLUTOR APLICADO: NO HAY "
    "NINGUNA. Y NO SE DECLARA ARISTA QUE FALTA, por la vara escrita el 15 ago 2026 en "
    "02_DESTEJIDOS.md: se declara donde lo compartido es un BLOQUE que uno expande de una LINEA "
    "del otro, y NO se declara donde es LINEA CONTRA LINEA con cableado propio denso a los dos "
    "lados. Aqui lo compartido son DOS GESTOS SUELTOS Y NO CONTIGUOS (el paso 1 contra el 1, y el "
    "3 contra el 4), no un bloque; y el cableado propio esta medido hoy: split_testing tiene 5 "
    "aristas y test_ab_precio 4. "
    "DISCUTIBLE MARCADO, Y ES EL MAS FUERTE DE TODA LA VUELTA, MAS QUE CUALQUIERA DE LAS CINCO: "
    "este es el UNICO par del acto donde el objeto de un nodo esta NOMBRADO DENTRO del objeto del "
    "otro. split_testing lista precio entre sus cuatro variables y su condicion de activacion "
    "dice precio con todas sus letras. Quien sostenga que eso funda la repeticion tiene una frase "
    "literal del catalogo de su lado, y la razon vieja la escribio mejor que nadie: no es una "
    "tecnica distinta, es la misma con una de sus cuatro variables. LO QUE SOSTENGO ES QUE LA "
    "VARIABLE COMPARTIDA NO ES EL PROCEDIMIENTO, y que los dos procedimientos divergen justo en "
    "lo que cada uno tiene de mas caro. PERO ESTE PAR SE PUEDE LEER AL REVES SIN FORZAR NADA, y "
    "va dicho antes de saber si acierto. "
    "SEGUNDO DISCUTIBLE MARCADO: no declarar arista. El ejemplar del 755 (15 ago 2026) declaro "
    "ARISTA QUE FALTA sin madre e hijo, porque lo compartido cubria TRES pasos del superviviente. "
    "Aqui lo compartido cubre DOS de cuatro, que es la mitad, y esta al filo de esa vara. Lo "
    "resuelvo por el lado del 827 (linea contra linea con cableado propio) y lo marco."
)


def main():
    print("=" * 78)
    print("VOLCADO DEL PUESTO %d: %s contra %s" % (PUESTO, A, B))
    print("=" * 78)

    print("\nGUARDA 1: los pasos de hoy")
    for nid, esperado in sorted(PASOS_HOY.items()):
        d = json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))
        real = len(d.get("pasos_accionables") or [])
        print("  %-16s %d pasos (la razon dice %d)  %s"
              % (nid, real, esperado, "OK" if real == esperado else "ABORTA"))
        if real != esperado:
            return 1

    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_puesto = {v["puesto_intra"]: v for v in V}
    v = por_puesto.get(PUESTO)
    if v is None:
        print("ABORTA: el puesto %d no esta registrado" % PUESTO)
        return 1
    if v["clase"] != CLASE_VIEJA:
        print("ABORTA: el puesto %d esta en %r y este volcado esperaba %r"
              % (PUESTO, v["clase"], CLASE_VIEJA))
        return 1
    if {v["nodo_a"], v["nodo_b"]} != {A, B}:
        print("ABORTA: el puesto %d no es el par que este volcado cree" % PUESTO)
        return 1

    razon_vieja = v["razon"]
    razon = (CABECERA
             + "LO QUE DECIA LA RAZON VIEJA, y se deja escrita ENTERA para que la correccion se "
               "pueda auditar (copiada del archivo por maquina, no transcrita): "
             + razon_vieja + " FIN DE LA RAZON VIEJA. "
             + CUERPO)
    if razon_vieja not in razon:
        print("ABORTA: la razon vieja no queda literal dentro de la nueva")
        return 1
    print("\nGUARDA 2: la razon vieja, copiada por maquina y literal dentro")
    print("  %d: %s -> %s, razon vieja %d caracteres dentro de %d  OK"
          % (PUESTO, CLASE_VIEJA, CLASE_NUEVA, len(razon_vieja), len(razon)))

    print("\nGUARDA 3: el marcador esperado, escrito ANTES de volcar")
    conteo = {}
    for x in V:
        conteo[x["clase"]] = conteo.get(x["clase"], 0) + 1
    ahora = {"n": len(V), "A": conteo.get("A", 0), "B": conteo.get("B", 0),
             "C": conteo.get("C", 0), "D": conteo.get("D", 0)}
    tras = {"n": ahora["n"], "A": ahora["A"] - 1, "B": ahora["B"], "C": ahora["C"],
            "D": ahora["D"] + 1}
    print("  MARCADOR DE AHORA:      n %d, A %d, B %d, C %d, D %d"
          % (ahora["n"], ahora["A"], ahora["B"], ahora["C"], ahora["D"]))
    print("  MARCADOR TRAS ESTE:     n %d, A %d, B %d, C %d, D %d"
          % (tras["n"], tras["A"], tras["B"], tras["C"], tras["D"]))
    print("  EL ESCRITO EN EL SCRIPT: n %d, A %d, B %d, C %d, D %d"
          % (ESPERADO["n"], ESPERADO["A"], ESPERADO["B"], ESPERADO["C"], ESPERADO["D"]))
    if tras != ESPERADO:
        print("  ABORTA: no coinciden. SE PARA.")
        return 1
    print("  COINCIDEN. OK")

    with io.open(LOTE, "w", encoding="utf-8") as fh:
        fh.write(json.dumps({"puesto": PUESTO, "clase": CLASE_NUEVA, "razon": razon},
                            ensure_ascii=False) + "\n")
    print("\nESCRITO el lote: %s (1 fila). El archivo lo escribe scripts/corregir_veredicto.py."
          % os.path.relpath(LOTE, RAIZ).replace("\\", "/"))
    print("\nLO QUE ESTE VOLCADO DEJA, y va escrito antes de que nadie lo compute: el acto de")
    print("OP-D-03 se queda con CERO pares A. Los seis nodos salen del cierre transitivo y la")
    print("operacion cierra con su destejido hecho y SIN FUSION.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
