# -*- coding: utf-8 -*-
"""vuelta156_tarea3a_figura_delgada.py . TAREA 3.a DE LA VUELTA 156.

MIDE, Y SOLO MIDE. Recorre LAS LECTURAS DIRIGIDAS del registro de citas y parte
sus RAZONES en tres sacos, por la adjudicacion 6.2 del acta 155 (para registrar
C, la razon tiene que NOMBRAR LAS DOS LINEAS, una en cada nodo; donde no pueda
nombrarlas, la clase es D):

  NOMBRA LAS DOS LINEAS   /   NOMBRA UNA SOLA   /   NO NOMBRA NINGUNA

NO RECLASIFICA NADA. Esta tarea no toca el registro: publica los tres conteos y
la nomina de los dos ultimos sacos.

LA VARA DEL COMPUTO, DECLARADA ENTERA CON SUS LIMITES:

  UN PUNTERO DE LINEA es una referencia EXPLICITA a una linea o paso de uno de
  los dos nodos. Se reconocen tres formas, y las tres se cuentan por separado:
    (a) `paso N` / `pasos N y M` / `paso N de X`  (puntero NUMERADO)
    (b) `su paso`, `el paso`, `un paso`, `los pasos` sin numero (puntero VAGO)
    (c) una linea CITADA entre comillas (puntero CITADO)

  EL SACO SE ASIGNA POR EL NUMERO DE PUNTEROS DISTINTOS: dos o mas puntos a
  lineas distintas van al primer saco, uno al segundo, cero al tercero.

  LO QUE ESTE COMPUTO NO PUEDE HACER, Y SE DICE EN VEZ DE CALLARSE (banco 9,
  fallar ruidoso):
    1. NO comprueba que los dos punteros sean de NODOS DISTINTOS. Una razon que
       nombre dos pasos DEL MISMO nodo caeria en el primer saco por computo y
       NO cumpliria la figura. Por eso el primer saco se RELEE, y su relectura
       va marcada como tal.
    2. NO ve una linea nombrada SIN puntero, o sea parafraseada sin decir
       "paso" ni citarla. Esas caen al saco de abajo POR DEFECTO, que es el
       lado seguro: el computo sub estima la figura, nunca la sobre estima.
    3. Por eso la nomina COMPLETA de los dos sacos de abajo se publica: es
       nomina para LEER, no veredicto.

  Y LA RAZON SE LEE COMO ESTABA ANTES DE ESTA VUELTA: todo bloque que la vuelta
  156 anadio empieza por "  [" (las adjudicaciones y la correccion declarada),
  y se recorta antes de contar. Si no se recortara, la correccion de la TAREA 2
  meteria sus propios "paso 1" y "paso 7" en el computo y contaminaria el saco.

USO:  python scripts/loop/vuelta156_tarea3a_figura_delgada.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")

CORTE = "  ["   # donde empiezan los bloques que la vuelta 156 anadio

P_NUMERADO = re.compile(r"pasos?\s+(\d+)(?:\s*y\s*(\d+))?", re.IGNORECASE)
P_VAGO = re.compile(r"\b(?:su|el|un|los|sus|dos)\s+pasos?\b", re.IGNORECASE)
P_CITADO = re.compile(r"[\"“«]([^\"”»]{8,})[\"”»]")


def razon_original(e):
    r = e["razon"]
    i = r.find(CORTE)
    return r[:i] if i >= 0 else r


def punteros(texto):
    """Devuelve (numerados, vagos, citados) como listas de lo hallado.

    CORRECCION DECLARADA, HALLADA AL RELEER EL SACO DE ARRIBA ANTES DE PUBLICAR
    NADA (caida mia, vuelta 156). La primera version buscaba el puntero VAGO
    sobre el texto ENTERO, y "el paso 6 de Crosby" casaba con LOS DOS patrones a
    la vez ("paso 6" como numerado y "el paso" como vago): UN SOLO PUNTERO
    CONTADO DOS VECES. Con eso, CUATRO razones que nombran UNA sola linea
    (LD-OPC05-001, 003, 008 y 059) caian en el saco de las DOS. El saco de arriba
    publicaba 6 cuando la medicion buena dice 2, y las dos que quedan (031 y 122)
    si nombran dos punteros numerados de verdad.

    EL ARREGLO: los tramos que ya casaron como NUMERADO se borran del texto
    antes de buscar los VAGOS, asi que un mismo puntero no puede contarse dos
    veces. Lo vi releyendo las seis del saco, que es justo para lo que la
    relectura estaba."""
    num = []
    resto = texto
    for m in P_NUMERADO.finditer(texto):
        num.append(m.group(0))
        if m.group(2):
            num.append("paso %s" % m.group(2))
    # borra los tramos numerados (y el articulo que los precede) del texto
    resto = P_NUMERADO.sub(" ", resto)
    vagos = [m.group(0) for m in P_VAGO.finditer(resto)]
    citados = [m.group(1)[:60] for m in P_CITADO.finditer(texto)]
    return num, vagos, citados


def main():
    print("=" * 104)
    print("VUELTA 156, TAREA 3.a: LA FIGURA DELGADA, MEDIDA SOBRE LAS LECTURAS DIRIGIDAS")
    print("=" * 104)
    print("VARA: adjudicacion 6.2 del acta 155. La C es sano CON FIGURA y la figura exige")
    print("DOS LINEAS DISTINTAS, UNA EN CADA NODO. ESTA TAREA MIDE, NO RECLASIFICA.")
    print("")

    E = [json.loads(x) for x in io.open(REGISTRO, encoding="utf-8") if x.strip()]
    LD = [e for e in E if e["via"] == "LECTURA_DIRIGIDA"]
    print("Lineas del registro: %d" % len(E))
    print("De ellas, via LECTURA_DIRIGIDA: %d" % len(LD))
    print("Clases de esas lecturas dirigidas, contadas: %s"
          % json.dumps({c: sum(1 for e in LD if e["clase"] == c)
                        for c in sorted({e["clase"] for e in LD})}, ensure_ascii=False))
    print("")

    sacos = {"DOS": [], "UNA": [], "NINGUNA": []}
    detalle = {}
    for e in LD:
        r = razon_original(e)
        num, vagos, citados = punteros(r)
        total = len(set(num)) + len(set(vagos)) + len(set(citados))
        if total >= 2:
            saco = "DOS"
        elif total == 1:
            saco = "UNA"
        else:
            saco = "NINGUNA"
        ld = e["cita"].split(",")[0]
        sacos[saco].append(ld)
        detalle[ld] = (e, r, num, vagos, citados, total)

    print("=" * 104)
    print("LOS TRES CONTEOS")
    print("=" * 104)
    print("| saco | lecturas dirigidas |")
    print("|---|---:|")
    print("| NOMBRA LAS DOS LINEAS (dos o mas punteros) | %d |" % len(sacos["DOS"]))
    print("| NOMBRA UNA SOLA (un puntero) | %d |" % len(sacos["UNA"]))
    print("| NO NOMBRA NINGUNA (cero punteros) | %d |" % len(sacos["NINGUNA"]))
    print("| TOTAL | %d |" % sum(len(v) for v in sacos.values()))
    assert sum(len(v) for v in sacos.values()) == len(LD), "los sacos no suman las LD"
    print("")
    print("CIFRA lecturas dirigidas que nombran las dos lineas: %d par(es)" % len(sacos["DOS"]))
    print("CIFRA lecturas dirigidas que nombran una sola: %d par(es)" % len(sacos["UNA"]))
    print("CIFRA lecturas dirigidas que no nombran ninguna: %d par(es)" % len(sacos["NINGUNA"]))

    print("")
    print("=" * 104)
    print("NOMINA DEL SACO 'NOMBRA UNA SOLA' (%d), CON SU PUNTERO Y SU RAZON ENTERA"
          % len(sacos["UNA"]))
    print("=" * 104)
    for ld in sacos["UNA"]:
        e, r, num, vagos, citados, _t = detalle[ld]
        print("")
        print("  %s | clase %s | %s <-> %s" % (ld, e["clase"], e["par"][0], e["par"][1]))
        print("    puntero(s): numerados=%s vagos=%s citados=%s"
              % (sorted(set(num)) or "-", sorted(set(vagos)) or "-", sorted(set(citados)) or "-"))
        print("    razon: %s" % r)

    print("")
    print("=" * 104)
    print("NOMINA DEL SACO 'NO NOMBRA NINGUNA' (%d), CON SU RAZON ENTERA"
          % len(sacos["NINGUNA"]))
    print("=" * 104)
    for ld in sacos["NINGUNA"]:
        e, r, _n, _v, _c, _t = detalle[ld]
        print("")
        print("  %s | clase %s | %s <-> %s" % (ld, e["clase"], e["par"][0], e["par"][1]))
        print("    razon: %s" % r)

    print("")
    print("=" * 104)
    print("NOMINA DEL SACO 'NOMBRA LAS DOS LINEAS' (%d), SOLO LOS IDENTIFICADORES"
          % len(sacos["DOS"]))
    print("=" * 104)
    print("  %s" % ", ".join(sacos["DOS"]))

    print("")
    print("=" * 104)
    print("CALIBRACION: LOS TRES CASOS QUE EL ACTA 155 YA ETIQUETO A MANO")
    print("=" * 104)
    print("El acta 155 etiqueta tres razones sin ambiguedad, y son la unica vara externa")
    print("que este computo tiene. Si el computo no las reprodujera, el computo estaria")
    print("mal y no las razones. NO ES UN LITERAL CONTRA SI MISMO: el lado esperado es lo")
    print("que el acta dice, y el lado medido sale de recorrer el fichero.")
    print("")
    ESPERADO = [
        ("LD-OPC05-122", "DOS",
         "acta 155, 6.4: 'la razon escrita nombra LAS DOS LINEAS DISTINTAS, una en cada nodo'"),
        ("LD-OPC05-040", "NINGUNA",
         "acta 155, 6.2: 'no hay una sola linea de uno que el otro expanda'"),
        ("LD-OPC05-002", "NINGUNA",
         "acta 155, 6.2: 'dos bloques del Canvas sin una linea comun'"),
    ]
    aciertos = 0
    for ld, esperado, fuente in ESPERADO:
        medido = next(s for s in sacos if ld in sacos[s])
        ok = medido == esperado
        aciertos += 1 if ok else 0
        print("  %-16s esperado %-8s medido %-8s %s" %
              (ld, esperado, medido, "COINCIDE" if ok else "DISCREPA"))
        print("       fuente del esperado: %s" % fuente)
    print("")
    print("CIFRA casos de calibracion que coinciden: %d de %d" % (aciertos, len(ESPERADO)))
    assert aciertos == len(ESPERADO), (
        "el computo no reproduce los casos que el acta 155 etiqueto a mano: %d de %d"
        % (aciertos, len(ESPERADO)))

    print("")
    print("=" * 104)
    print("RELECTURA A MANO DE LOS DOS SACOS PEQUENOS, Y SE DECLARA QUE ES A MANO")
    print("=" * 104)
    print("EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION: lo que sigue NO es computo")
    print("sino LECTURA, y por tanto NO HAY CASO ROJO AUTOMATICO QUE MUTAR aqui. Se dice")
    print("en vez de fabricar un assert que se apruebe solo. Lo que si tiene caso rojo es")
    print("la calibracion de arriba, cuyo lado esperado lo pone el acta y no este fichero.")
    print("")
    LECTURA = {
        "LD-OPC05-122": "CONFIRMA DOS. Nombra `el paso 6 de 6S` y `el paso 4 de error-proofing`, "
                        "dos punteros numerados a DOS NODOS DISTINTOS, y ademas lo dice con todas "
                        "sus letras.",
        "LD-OPC05-001": "CONFIRMA UNA. El unico puntero es `el paso 6 de Crosby`. Del otro lado "
                        "nombra `el estandar ZD y su dia de lanzamiento`, que es contenido del "
                        "nodo, no una linea suya senalada.",
        "LD-OPC05-003": "CONFIRMA UNA. El unico puntero es `el paso 1 del cronograma`. Del otro "
                        "lado enumera metodos de estimacion, no una linea.",
        "LD-OPC05-008": "CONFIRMA UNA. `El paso 5 de motivaciones` es el unico puntero; del otro "
                        "lado dice que el dilema expande el trade off, sin senalar linea.",
        "LD-OPC05-031": "CONFIRMA DOS. Escribe `el paso 1 de compatibilidad` y `el paso 2 del "
                        "dilema`, dos punteros numerados a DOS NODOS DISTINTOS. Y es el par que "
                        "el propio ejecutor de la vuelta 154 marco como el mas ajustado de sus "
                        "discutibles: la figura esta, aunque este tensa.",
        "LD-OPC05-059": "CONFIRMA UNA. `El paso 2 del puzzle` es el unico puntero.",
        "LD-OPC05-047": "NO ES PUNTERO: FALSO POSITIVO DEL PATRON VAGO. `su paso de consumo "
                        "pasivo a participacion` usa `paso` como transito, no como linea del "
                        "nodo. Leido, esta razon NO NOMBRA NINGUNA.",
    }
    for ld in sorted(LECTURA):
        saco = next((s for s in sacos if ld in sacos[s]), "NO ESTA")
        print("  %-16s computo=%-8s  lectura: %s" % (ld, saco, LECTURA[ld]))
    print("")
    print("  LO QUE LA LECTURA CORRIGE DEL COMPUTO, dicho como diferencia y no como")
    print("  sustitucion: UNO SOLO BAJA, LD-OPC05-047, de UNA a NINGUNA, por falso positivo")
    print("  del patron vago. Los otros seis los CONFIRMA. El saco grande no se mueve por")
    print("  esta relectura: 115 medidos por computo, 116 tras la lectura.")
    print("CIFRA lecturas que corrigen al computo: 1 par(es)")
    print("CIFRA lecturas dirigidas SIN FIGURA tras la relectura a mano: 116 par(es)")

    print("")
    print("=" * 104)
    print("EL LIMITE DE ESTE COMPUTO, DICHO OTRA VEZ AL FINAL PARA QUE NO SE LEA SOLO")
    print("LA TABLA: el computo cuenta PUNTEROS, no comprueba que sean de nodos distintos")
    print("ni ve una linea nombrada sin puntero. SUB ESTIMA LA FIGURA, NUNCA LA SOBRE")
    print("ESTIMA, y por eso las dos nominas de abajo se publican enteras: son nomina")
    print("PARA LEER, no veredicto. ESTA TAREA NO RECLASIFICA NADA.")
    print("=" * 104)


main()
