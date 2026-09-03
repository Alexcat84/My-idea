# -*- coding: utf-8 -*-
r"""vuelta142_2c_mutaciones.py . LA PRUEBA DE MUTACION DE LA TAREA 2.c de la
vuelta 142 (acta de la vuelta 141, adjudicacion 3.5: la vara FUSION aprende el
tercer veredicto, CONSUMIDA CON SUPERVIVIENTE DIVERGENTE).

TODO EN MEMORIA, NUNCA EN DISCO: se carga el grafo y las operaciones, se muta el
DICCIONARIO cargado y se vuelve a llamar a la vara. `dataset/` no se toca ni una
vez, y el arnes lo comprueba al final con `git status --porcelain -- dataset/`.

EL SUJETO SE ELIGE POR COMPUTO, NUNCA TECLEADO: la PRIMERA operacion de la fase
que hoy sale CUMPLIDA por la vara FUSION, en el orden del catalogo. Si no hay
ninguna, el caso se declara OMITIDO POR FALTA DE SUJETO y ESO ES ROJO, no verde
(EJECUTOR.md 1: una guarda sin sujeto es una guarda que no mide).

CUATRO CASOS, y las expectativas se COMPUTAN comparando el veredicto antes y
despues de mutar, nunca contra una frase literal:

  (0)  CONTRAPRUEBA SIN MUTAR: el sujeto elegido sale CUMPLIDO.
  (i)  DIVERGENTE: se DEPRECA el superviviente del sujeto y se le mete un alias
       hacia un id que la ficha SI lista en `eliminar`. Tiene que salir
       DIVERGENTE y NO cumplida.
  (ii) CONSUMIDA A SECAS: el mismo alias hacia un id que la ficha NO lista en
       `eliminar` (se fabrica un nodo vivo nuevo EN MEMORIA para eso). Tiene que
       salir CONSUMIDA, no DIVERGENTE, y tampoco cumplida.
  (iii) LOS DOS CASOS REALES: OP-M-02-ADMIT y OP-M-02-MEDIOS, sin mutar nada,
       tienen que salir las DOS como DIVERGENTES. Es el caso positivo sobre el
       grafo de hoy, y su sujeto tambien se computa (las FUSION cuyo
       superviviente escrito esta deprecado y resuelve a un vivo del `eliminar`).

USO:
  python scripts/loop/vuelta142_2c_mutaciones.py --fase 03_FUSIONES

--- ADJUDICACION 6.7 DEL ACTA 158 (3 sep 2026): EL CHECK DE P.16 SE CINE AL
CONTENIDO Y A LA VENTANA DEL PROPIO SCRIPT ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra, y el check que este
fichero lleva NO se modifica al escribir esto: esto es la adjudicacion, no el
remedio.

LAS DOS ANCLAS QUE SE MUEVEN EN LA MISMA LINEA, y el hallazgo es del ejecutor de
la vuelta 157, que lo trajo como pregunta en vez de esquivarlo callando. El
docstring dice que se comprueba que `dataset/` y `docs/plan/` NO SE TOCAN NI UNA
VEZ, o sea CONTENIDO. El instrumento es `git status --porcelain`, que ademas de
contenido ve:
  (i)  ESTADO DE FIN DE LINEA. Este repo tiene `core.autocrlf`, asi que un
       fichero reescrito por el ciclo queda marcado como modificado aunque su
       sha256 NORMALIZADO sea identico al de HEAD. Paso de verdad en la vuelta
       157 y tumbo tres mutaciones de la bateria en ROJO con el contenido
       intacto.
  (ii) SUCIEDAD ANTERIOR AL ARRANQUE DEL SCRIPT, que no es suya. El veredicto de
       este check depende de si alguien committeo tocando `dataset/` antes, y no
       de si las mutaciones de este fichero tocaron el dataset.

EL REMEDIO ADJUDICADO: huella de CONTENIDO tomada ANTES y DESPUES de las
mutaciones DENTRO del propio script, y comparada consigo misma. Con su caso
positivo por mutacion: si una mutacion escribe de verdad en `dataset/` o en
`docs/plan/`, el check SIGUE SALIENDO ROJO.

EL ALCANCE, Y AQUI HAY UNA DISCREPANCIA DE CIFRA QUE SE DECLARA EN VEZ DE
COPIARSE: el acta 158 mide ONCE ficheros con el patron literal, siete de ellos
dentro de la bateria de las 23. El recomputo de la vuelta 159
(`scripts/loop/vuelta159_tarea1_registrar_adjudicaciones.py`, funcion
`ficheros_con_patron_p16`, salida `docs/loop/SALIDA_V159_T1_ADJUDICACIONES.txt`)
da DOCE ficheros, y los SIETE de la bateria reproducen exactamente. El duodecimo
es `scripts/loop/vuelta89_tarea4_guarda_op_c05.py`: excluirlo devuelve los once
del acta al digito. La cifra de la vuelta 159 es la del computo, y por eso el
remedio de la 6.7 queda EN PARADA, declarada en el reporte de la vuelta 159.

--- ADJUDICACION 6.1 DEL ACTA 159 (3 sep 2026): EL ALCANCE DEL CHECK DE P.16 SON
DOCE, NO ONCE, Y LA VARA ES LA LECTURA B ---

CORRECCION DECLARADA POR ADICION. Nada de lo escrito arriba se borra, y en
particular NO SE BORRA la cifra ONCE que la adjudicacion 6.7 del acta 158 dejo
escrita: se corrige delante de ella para que la correccion se pueda auditar.

LA CIFRA VIEJA Y LA NUEVA, LAS DOS ESCRITAS. El acta 158 midio ONCE ficheros de
`scripts/loop/` con el patron literal del check de P.16 y su encargo mando parar
si la cuenta no daba once. La vuelta 159 recomputo y dio DOCE, paro por mandato
literal y NO TOCO UN SOLO CHECK. EL ACTA 159 ADJUDICA QUE SON DOCE Y QUE LA
CIFRA EQUIVOCADA ERA LA DEL ACTA, o sea la del auditor: lo midio el en dos
arboles distintos, el del commit del acta 158 y HEAD, y los dos dan 4 / 12 / 14
ficheros y 3 / 7 / 7 dentro de la bateria de las 23. EL ONCE NUNCA FUE CIERTO, y
la diferencia no la introdujo ninguna vuelta.

LA VARA DE LA LECTURA ES LA B, Y SE NOMBRA PARA QUE NO VUELVA A DERIVAR: B MEDIA
es "pathspec que empieza por dataset/", que es la que el ejecutor publico como
principal y la que la 6.7 del acta 158 sostiene al describir el defecto por su
instrumento. LA LECTURA ESTRECHA DE CUATRO (dataset/ Y docs/plan/ a la vez) NO
VALE, porque el defecto no depende de que el pathspec traiga tambien docs/plan/.

EL DUODECIMO ENTRA Y TIENE NOMBRE: `vuelta89_tarea4_guarda_op_c05.py`. Es del
mismo defecto que la serie 142 a 147, solo que mas viejo, y lleva las dos anclas
que la 6.7 describe (la del fin de linea y la de la suciedad anterior al
arranque), leidas por el auditor en su fuente. NO HAY MOTIVO DE VARA PARA
EXCLUIRLO.

LO QUE ESTO OBLIGA: la 5.a y la 5.c del encargo de la vuelta 159 se ejecutan
sobre LOS DOCE, no sobre once ni sobre cuatro. La nomina no se teclea: se
recomputa, y su medicion esta pegada en `docs/loop/SALIDA_V159_T5_ALCANCE.txt`.
"""
import argparse
import copy
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T

MARCA_DIVERGENTE = "CONSUMIDA CON SUPERVIVIENTE DIVERGENTE"
MARCA_CONSUMIDA = "CONSUMIDA:"


def veredicto_de(op, nodos):
    resolver = T.resolver_de(nodos)
    fallos = []
    return T.destino_de_fusion(op, nodos, fallos, resolver)


def fusiones_del_catalogo(fase, ops, nodos):
    """Las del catalogo que la vara enruta a FUSION, EN EL ORDEN DEL CATALOGO."""
    remisiones = T.leer_remisiones(fase)
    fallos = []
    catalogo, por_id = T.construir_catalogo(fase, ops, remisiones, fallos)
    salida = []
    for x in catalogo:
        op = por_id[x]
        if T.es_mesa(op):
            continue
        sup = op.get("superviviente")
        if sup and T.PATRON_ID_NODO.match(sup) and sup in nodos:
            salida.append(op)
    return salida


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fase", default="03_FUSIONES")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    ops = T.cargar_ops("WORK")
    nodos = T.cargar_grafo("WORK")
    fusiones = fusiones_del_catalogo(a.fase, ops, nodos)

    print("=" * 78)
    print("MUTACIONES DE LA TAREA 2.c | vuelta 142 | FASE %s" % a.fase)
    print("Todo EN MEMORIA. El sujeto se ELIGE POR COMPUTO, no se teclea.")
    print("FUSIONES en el catalogo de la fase: %d" % len(fusiones))
    print("=" * 78)

    resultados = []

    # ---- EL SUJETO: la primera FUSION hoy CUMPLIDA, por computo -------------
    sujeto = None
    for op in fusiones:
        cumplido, _r = veredicto_de(op, nodos)
        if cumplido is True:
            sujeto = op
            break
    if sujeto is None:
        print("")
        print("OMITIDO POR FALTA DE SUJETO: ninguna FUSION de la fase %s sale CUMPLIDA hoy, "
              "asi que no hay nada que mutar. ESO ES ROJO, no verde." % a.fase)
        return 1

    sup = sujeto.get("superviviente")
    eliminar = list(sujeto.get("eliminar") or [])
    print("")
    print("SUJETO ELEGIDO POR COMPUTO: %s | superviviente escrito %s | eliminar %s"
          % (sujeto.get("id_op"), sup, eliminar or "vacio"))

    # ---- (0) CONTRAPRUEBA SIN MUTAR ---------------------------------------
    cumplido0, razon0 = veredicto_de(sujeto, nodos)
    ok = cumplido0 is True
    resultados.append(("0 CONTRAPRUEBA sin mutar: %s sale CUMPLIDA" % sujeto.get("id_op"), ok))
    print("")
    print("(0) sin mutar -> cumplido=%s | %.150s" % (cumplido0, razon0))

    # ---- (i) DIVERGENTE ----------------------------------------------------
    # El destino del alias tiene que ser un id VIVO que la ficha liste en
    # `eliminar`. Se computa de la propia ficha; si la ficha no tiene ninguno
    # utilizable se fabrica uno EN MEMORIA y se anade a `eliminar` de la COPIA.
    nodos_i = copy.deepcopy(nodos)
    op_i = copy.deepcopy(sujeto)
    destino_i = next((x for x in eliminar if T.vivo(nodos_i.get(x))), None)
    if destino_i is None:
        destino_i = "_mutacion_v142_destino_condenado"
        nodos_i[destino_i] = {"node_id": destino_i, "deprecado": False,
                              "ids_alias": [], "nodos_siguientes": [], "nodos_previos": []}
        op_i["eliminar"] = eliminar + [destino_i]
    nodos_i[sup]["deprecado"] = True
    nodos_i[destino_i]["ids_alias"] = list(nodos_i[destino_i].get("ids_alias") or []) + [sup]
    cumplido_i, razon_i = veredicto_de(op_i, nodos_i)
    ok = (cumplido_i is not True) and razon_i.startswith(MARCA_DIVERGENTE)
    resultados.append(("i superviviente DEPRECADO con alias hacia un id que la ficha SI "
                       "condena: sale DIVERGENTE y NO cumplida", ok))
    print("")
    print("(i) alias %s -> %s (esta en eliminar) -> cumplido=%s" % (sup, destino_i, cumplido_i))
    print("    %.220s" % razon_i)

    # ---- (ii) CONSUMIDA A SECAS -------------------------------------------
    nodos_ii = copy.deepcopy(nodos)
    op_ii = copy.deepcopy(sujeto)
    destino_ii = "_mutacion_v142_destino_no_condenado"
    nodos_ii[destino_ii] = {"node_id": destino_ii, "deprecado": False,
                            "ids_alias": [sup], "nodos_siguientes": [], "nodos_previos": []}
    nodos_ii[sup]["deprecado"] = True
    # Y se comprueba POR COMPUTO que ese destino NO esta en `eliminar`.
    if destino_ii in (op_ii.get("eliminar") or []):
        print("ROJO (arnes): el destino fabricado ya estaba en eliminar; el caso (ii) no "
              "probaria lo que dice")
        return 1
    cumplido_ii, razon_ii = veredicto_de(op_ii, nodos_ii)
    ok = (cumplido_ii is not True) and razon_ii.startswith(MARCA_CONSUMIDA)
    resultados.append(("ii superviviente DEPRECADO con alias hacia un id que la ficha NO "
                       "condena: sale CONSUMIDA, no DIVERGENTE, y tampoco cumplida", ok))
    print("")
    print("(ii) alias %s -> %s (NO esta en eliminar) -> cumplido=%s"
          % (sup, destino_ii, cumplido_ii))
    print("     %.220s" % razon_ii)

    # ---- (iii) LOS DOS CASOS REALES, SIN MUTAR NADA ------------------------
    resolver = T.resolver_de(nodos)
    reales = []
    for op in fusiones:
        s = op.get("superviviente")
        if T.vivo(nodos.get(s)):
            continue
        d = resolver(s)
        if d != s and T.vivo(nodos.get(d)) and d in (op.get("eliminar") or []):
            reales.append(op)
    divergentes = []
    for op in reales:
        c, r = veredicto_de(op, nodos)
        if c is not True and r.startswith(MARCA_DIVERGENTE):
            divergentes.append(op.get("id_op"))
    ok = bool(reales) and len(divergentes) == len(reales)
    resultados.append(("iii CASO POSITIVO sobre el grafo de hoy: las %d FUSION con "
                       "superviviente deprecado que resuelve a un condenado salen TODAS "
                       "DIVERGENTES" % len(reales), ok))
    print("")
    print("(iii) halladas POR COMPUTO %d: %s" % (len(reales),
                                                 ", ".join(o.get("id_op") for o in reales)))
    print("      salen DIVERGENTES %d: %s" % (len(divergentes), ", ".join(divergentes)))

    # ---- P.16: el disco no se toco ----------------------------------------
    sucio = subprocess.run(["git", "status", "--porcelain", "--", "dataset/", "docs/plan/"],
                           cwd=T.RAIZ, capture_output=True, text=True).stdout.strip()
    ok = (sucio == "")
    resultados.append(("P.16 dataset/ y docs/plan/ SIN TOCAR tras las mutaciones", ok))
    print("")
    print("git status --porcelain -- dataset/ docs/plan/ : %r" % sucio)

    print("")
    print("=" * 78)
    verdes = 0
    for nombre, o in resultados:
        print("  %-5s %s" % ("VERDE" if o else "ROJO", nombre))
        verdes += 1 if o else 0
    print("CIFRA de la bateria 2.c: %d comprobaciones" % len(resultados))
    print("CIFRA verdes de la bateria 2.c: %d comprobaciones" % verdes)
    print("=" * 78)
    if verdes != len(resultados):
        print("ROJO: %d de %d casos no se comportan." % (len(resultados) - verdes, len(resultados)))
        return 1
    print("VERDE: los %d casos se comportan." % len(resultados))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
