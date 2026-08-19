# -*- coding: utf-8 -*-
"""vuelta39_cerrar_opd04.py - EL CIERRE DE OP-D-04, escrito por instrumento y no a mano.

SUCESOR DECLARADO de scripts/loop/vuelta36_cerrar_opd03.py (EJECUTOR.md regla 2), y
lo que cambia va dicho: aquel cerraba un destejido SIN FUSION, con el campo
`superviviente` en null porque no habia ninguno. Este cierra una operacion con DOS
FUSIONES EJECUTADAS y DOS supervivientes, y el campo se queda en null POR OTRO
MOTIVO: la adjudicacion a4 del acta de la vuelta 38, que dice que el esquema tiene
UN campo y la operacion produce DOS, asi que escribir uno mentiria por omision y
escribir una lista estrenaria formato sin pagina. La verdad va en la nota, con los
dos supervivientes y los dos planes sellados nombrados.

POR QUE EL ESTADO SE QUEDA EN `LISTA` Y NO SE INVENTA UNO NUEVO. La casa registra el
hecho consumado en la NOTA, no en el estado, y las 71 operaciones estan en LISTA
incluidas las que ya se ejecutaron. Inventar un estado HECHA seria inventar una
regla, y la regla 5 de EJECUTOR.md lo prohibe. Sigue como PENDIENTE DE DOCTRINA
heredado.

GUARDAS, escritas para caer:
  1. la operacion existe y su estado es el que este cierre espera.
  2. el texto viejo de la nota queda LITERAL dentro de la nueva, o aborta: una
     correccion que tapa lo que corrige no se puede auditar.
  3. el campo `superviviente` SIGUE EN null al terminar, que es lo que a4 manda.
  4. los CUATRO absorbidos estan deprecados y los TRES vivos siguen vivos, medido
     hoy en dataset/nodos y no supuesto del plan.
  5. los TRES pares entre los vivos estan declarados EN LOS DOS EXTREMOS (P.10).
  6. el numero de operaciones no cambia y ninguna otra se toca (byte a byte).

Uso: python scripts/loop/vuelta39_cerrar_opd04.py [--simular|--ejecutar]
"""
import io
import itertools
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")

ID_OP = "OP-D-04"
ESTADO_ESPERADO = "LISTA"

VIVOS = ["reglas_brainstorming", "pensamiento_convergente_divergente",
         "construir_sobre_ideas_ajenas"]
ABSORBIDOS = ["brainstorming_divergente", "brainstorming_efectivo",
              "generar_multiples_opciones", "design_attitude_vs_decision_attitude"]

CIERRE = (
    " REGISTRO DE CIERRE, 19 ago 2026 (vuelta 39). CORRECCION DECLARADA, y el texto viejo se "
    "queda entero delante porque una correccion que tapa lo que corrige no se puede auditar: "
    "todo lo de arriba se escribio con la fusion EN ESPERA, y la fusion YA ESTA HECHA. "
    "OP-D-04 CIERRA CON LAS DOS FUSIONES EJECUTADAS, no con una. "
    "LO QUE SE HIZO, medido en esta vuelta y no recordado: la DECISION 2 del fundador (19 ago "
    "2026) mandaba que la eleccion se publicara SELLADA y que la fusion esperara el acta del "
    "auditor; el acta de la vuelta 38 llego, confirmo las tres lecturas dirigidas en D (a1 y a2), "
    "confirmo las dos elecciones de P.8, y adjudico en a3 que la regla FAMILIA DECLARADA no "
    "gobierna esas tres lecturas, por el orden de fuentes de AUDITOR.md seccion 0. Con eso LAS "
    "DOS FUSIONES QUEDARON AUTORIZADAS y esta vuelta las ejecuto tal como estaban selladas, sin "
    "recalcular ninguna decision, con las dos simulaciones re-corridas antes de escribir y BYTE "
    "IGUAL contra las salidas de la vuelta 38. "
    "LOS DOS SUPERVIVIENTES, con su plan sellado al lado. UNO, EL TALLER: reglas_brainstorming "
    "absorbe a brainstorming_divergente y a brainstorming_efectivo, plan "
    "docs/loop/PLAN_V38_OPD04_TALLER.json, ejecucion en docs/loop/SALIDA_V39_TALLER_EJEC.txt; "
    "pasa de 5 pasos a 7 y de 2 condiciones a 4. DOS, LA ALTERNANCIA: "
    "pensamiento_convergente_divergente absorbe a generar_multiples_opciones y a "
    "design_attitude_vs_decision_attitude, plan docs/loop/PLAN_V38_OPD04_ALTERNANCIA.json, "
    "ejecucion en docs/loop/SALIDA_V39_ALTERNANCIA_EJEC.txt; pasa de 4 pasos a 7 y de 2 "
    "condiciones a 3. "
    "EL CAMPO superviviente SE QUEDA EN null, y aqui NO es por falta de superviviente sino por "
    "sobra: esta operacion produce DOS y el esquema tiene UN campo. Lo adjudica el acta de la "
    "vuelta 38, punto a4: escribir uno solo mentiria por omision y estrenar una lista seria "
    "decision de esquema, o sea de la casa. Va como recomendacion al fundador y no bloquea. Es "
    "el mismo null que OP-D-03 pero por el motivo contrario, y por eso se dice. "
    "LA TERCERA SALIDA DE P.10, COMPLETA: fundidos los DOS subconjuntos cerrados, el resto SE "
    "ENLAZA. Los tres vivos que quedan (reglas_brainstorming, pensamiento_convergente_divergente "
    "y construir_sobre_ideas_ajenas) quedan enlazados en los TRES pares y en LOS DOS EXTREMOS de "
    "cada uno. Dos de los tres pares llegaron solos con las fusiones y su simetrizacion; el "
    "tercero (reglas_brainstorming hacia construir_sobre_ideas_ajenas) se escribio a proposito, "
    "resuelto al dia de su escritura por P.9 y con los dos extremos escritos de una vez, de modo "
    "que el ciclo posterior no tuvo NADA que anadir. La direccion no se invento: el superviviente "
    "del taller ENUNCIA la regla de construir sobre las ideas de otros y no trae su procedimiento "
    "porque vive entero en el otro nodo, cuya condicion de activacion dice 'Durante sesiones de "
    "brainstorming o co-creacion en equipo'. Salida en docs/loop/SALIDA_V39_ENLACE_P10.txt. "
    "EL CUARTO MIEMBRO DEL RACIMO MIXTO, brainstorming, quedo enlazado al superviviente del "
    "taller SIN ESCRIBIR LA ARISTA: la trajo la propia fusion al redirigir la entrada que "
    "nombraba a brainstorming_efectivo, y tras el ciclo los dos se declaran cada uno en el "
    "extremo del otro, medido sobre los dos ficheros. "
    "EL CENSO: 3.853 ficheros antes y despues, nadie borrado. Vivos 3.538 a 3.536 a 3.534 y "
    "deprecados 315 a 317 a 319, exactamente dos por fusion; los cuatro absorbidos quedan "
    "deprecados con su TEXTO INTACTO y su fichero en pie. "
    "UNA COSA QUE EL PLAN SELLADO NO TRAIA Y APARECIO EJECUTANDO, declarada y no silenciada: "
    "Gate 0 cayo en rojo a la primera con un puente aprobado de quality apuntando al recien "
    "deprecado brainstorming_efectivo. El plan enumeraba las 17 referencias de NODO y no las del "
    "registro de puentes. Se resolvio con el instrumento de la casa, "
    "scripts/reanclar_por_resolutor.py, que mueve REFERENCIAS y jamas nodos y va por el resolutor "
    "(P.1): el ancla pasa a reglas_brainstorming con ancla_original guardando de donde venia. No "
    "es una decision recalculada, es la misma redireccion, y el precedente esta medido tres veces "
    "en git (a2902995, 06dd2922 y 33265c05, que fue el que creo el instrumento). Va como "
    "DISCUTIBLE al auditor. "
    "EL ESTADO SE QUEDA EN LISTA porque el esquema de OPERACIONES.jsonl no tiene otro, igual que "
    "en OP-D-01, OP-D-02 y OP-D-03, que tambien estan ejecutadas. Sigue como PENDIENTE DE "
    "DOCTRINA heredado: el esquema no distingue una operacion HECHA de una pendiente, y hoy eso "
    "solo se lee en la nota."
)


def main():
    modo = "--simular"
    for x in sys.argv[1:]:
        if x in ("--simular", "--ejecutar"):
            modo = x

    print("CIERRE DE %s" % ID_OP)
    print("MODO: %s" % modo)
    print("=" * 78)

    with io.open(OPS, encoding="utf-8-sig", newline="") as fh:
        bruto = fh.read()
    lineas = bruto.split("\n")
    fallos = []

    idx = None
    for i, l in enumerate(lineas):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get("id_op") == ID_OP:
            idx = i
            op = d
    print("guarda 1, la operacion existe: %s" % ("OK" if idx is not None else "ROJO"))
    if idx is None:
        return 1
    print("guarda 1b, estado %r contra el esperado %r: %s"
          % (op.get("estado"), ESTADO_ESPERADO,
             "OK" if op.get("estado") == ESTADO_ESPERADO else "ROJO"))
    if op.get("estado") != ESTADO_ESPERADO:
        fallos.append("estado inesperado")

    # guarda 4: los cuatro absorbidos deprecados y los tres vivos vivos
    print("guarda 4, los CUATRO absorbidos y los TRES vivos, medidos hoy en dataset/nodos:")
    G = {}
    for nid in VIVOS + ABSORBIDOS:
        G[nid] = json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))
    for nid in ABSORBIDOS:
        dep = bool(G[nid].get("deprecado"))
        print("    %-40s absorbido  deprecado=%s %s" % (nid, dep, "OK" if dep else "ROJO"))
        if not dep:
            fallos.append("%s deberia estar deprecado" % nid)
    for nid in VIVOS:
        dep = bool(G[nid].get("deprecado"))
        print("    %-40s vivo       deprecado=%s %s" % (nid, dep, "OK" if not dep else "ROJO"))
        if dep:
            fallos.append("%s deberia estar vivo" % nid)

    # guarda 5: los tres pares en los dos extremos
    print("guarda 5, los TRES pares entre los vivos, declarados en LOS DOS EXTREMOS (P.10):")
    for a, b in itertools.combinations(VIVOS, 2):
        de_a = [c for c in CAMPOS if b in (G[a].get(c) or [])]
        de_b = [c for c in CAMPOS if a in (G[b].get(c) or [])]
        ok = bool(de_a) and bool(de_b)
        print("    %-36s %-36s %s %s / %s" % (a, b, "OK" if ok else "ROJO", de_a or "-", de_b or "-"))
        if not ok:
            fallos.append("el par %s / %s no esta en los dos extremos" % (a, b))

    vieja = op.get("nota") or ""
    nueva = vieja + CIERRE

    # guarda 2: el texto viejo LITERAL dentro de la nueva
    ok2 = vieja in nueva and len(nueva) > len(vieja)
    print("guarda 2, el texto viejo (%d caracteres) queda LITERAL dentro de la nueva (%d): %s"
          % (len(vieja), len(nueva), "OK" if ok2 else "ROJO"))
    if not ok2:
        fallos.append("la nota vieja no sobrevive literal")

    op["nota"] = nueva

    # guarda 3: el campo superviviente sigue en null
    ok3 = op.get("superviviente") is None
    print("guarda 3, el campo superviviente SIGUE EN null (a4 del acta): %s"
          % ("OK" if ok3 else "ROJO"))
    if not ok3:
        fallos.append("el campo superviviente no esta en null")

    nuevas = list(lineas)
    nuevas[idx] = json.dumps(op, ensure_ascii=False)
    salida = "\n".join(nuevas)

    # guarda 6: mismo numero de operaciones y ninguna otra tocada, byte a byte
    antes = [l for l in lineas if l.strip()]
    despues = [l for l in nuevas if l.strip()]
    distintas = [i for i in range(min(len(antes), len(despues))) if antes[i] != despues[i]]
    ok6 = len(antes) == len(despues) == 71 and distintas == [antes.index(lineas[idx])]
    print("guarda 6, %d operaciones antes y %d despues, lineas distintas: %s: %s"
          % (len(antes), len(despues), distintas, "OK" if ok6 else "ROJO"))
    if not ok6:
        fallos.append("se movio mas de una linea o cambio el numero de operaciones")

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    print()
    print("LA COLA DE LA NOTA NUEVA, %d caracteres anadidos:" % (len(nueva) - len(vieja)))
    print("  ...%s" % nueva[-600:])

    if modo == "--simular":
        print()
        print("SIMULACION: cero escrituras.")
        return 0

    with io.open(OPS, "w", encoding="utf-8", newline="") as fh:
        fh.write(salida)
    print()
    print("ESCRITO en %s" % OPS)

    rel = [json.loads(l) for l in io.open(OPS, encoding="utf-8-sig") if l.strip()]
    op2 = [x for x in rel if x.get("id_op") == ID_OP][0]
    print("RELEIDO DEL FICHERO: %d operaciones, %s con superviviente=%r y nota de %d caracteres"
          % (len(rel), ID_OP, op2.get("superviviente"), len(op2.get("nota") or "")))
    return 0 if len(rel) == 71 and op2.get("superviviente") is None else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
