# -*- coding: utf-8 -*-
r"""vuelta143_3c_girar_arista.py . EL GIRO DE UNA ARISTA DE ESCALERA: LA VUELTA
SE RETIRA Y LA IDA SE ESCRIBE, EN LA MISMA OPERACION (TAREA 3.c de la vuelta
143).

POR QUE NACE UN INSTRUMENTO NUEVO, MEDIDO Y NO SUPUESTO. El encargo pide que
"la vuelta A -> B se retira Y la ida B -> A se escribe, en el mismo commit, y EL
GRADO TOTAL NO SUBE NI BAJA porque es un giro y no una poda". Ninguno de los dos
instrumentos que la casa ya tiene puede hacer eso solo, y cada uno lo dice con
su propia guarda, que esta bien puesta:

  - `vuelta141_3_retirar_vuelta.py` exige en su guarda 5 que LA IDA SIGA
    PRESENTE al terminar ("una escalera sin peldano no es una escalera"). Aqui
    la ida NO esta puesta todavia, asi que retirar primero aborta.
  - `vuelta140_3_escribir_aristas.py` exige en su guarda 5 UNA SOLA DIRECCION
    salvo MUTUO o par exceptuado. Aqui la inversa SI existe (es justo la que se
    va a retirar) y el par NO esta exceptuado, asi que escribir primero aborta.
    Medido en esta vuelta: la simulacion de `--op OP-E-04` sale ROJO con
    exactamente ese fallo y con cero escrituras.

Las dos guardas tienen razon POR SEPARADO. Lo que falta es la operacion ATOMICA
que las satisface a la vez, y esa es esta: el par nunca se queda sin arista y
nunca tiene las dos.

DE DONDE SALE LA AUTORIDAD, y no es de aqui: de la CONTRAORDEN DEL AUDITOR del
12 ago 2026 en docs/plan/EXPEDIENTE_MESA_JUNTA_ASESORA.md, "en una escalera, la
arista de vuelta no es redundante, es FALSA", y de la ficha, que tiene que
PROHIBIR la vuelta y NOMBRAR el par. Las dos cosas se comprueban con la MISMA
funcion que el retirador usa (`prohibicion_de`), importada y no reimplementada.

LAS GUARDAS, todas con su salida impresa, y si UNA cae no se escribe nada:
  (1) LOS DOS EXTREMOS resuelven por alias (P.1) y estan VIVOS. Se declara si
      el id dado resuelve a otro.
  (2) CERO AUTO-ARISTAS: los dos extremos no resuelven al mismo nodo.
  (3) EL ESTADO DE PARTIDA ES EL DE UN GIRO: la VUELTA existe hoy en las dos
      vistas y la IDA no existe. Si las dos estan puestas esto no es un giro,
      es una poda, y hay que usar el retirador; si ninguna esta puesta, es una
      escritura y hay que usar el escritor. Se aborta diciendo cual.
  (4) LA FICHA PROHIBE LA VUELTA Y NOMBRA EL PAR (guarda 3.d del encargo:
      "si una escritura o una retirada toca una arista que ninguna operacion
      del plan propone ni prohibe, paras esa y la traes"). La frase se CITA.
  (5) EL PAR NO ESTA EXCEPTUADO POR LA FICHA. Un par exceptuado del 9.22 lleva
      sus DOS direcciones a proposito, asi que girarlo seria borrar una arista
      legitima. Se lee con `T.pares_exceptuados_de`, la misma funcion que la
      vara y el escritor.
  (6) P.9, SE ESCRIBE EL ID VIVO RESUELTO, nunca el id de la ficha si esta
      deprecado.
  (7) CERO DUPLICADAS NUEVAS tras resolver en las listas tocadas, medido como
      DELTA y no como total.
  (8) NINGUN OTRO CAMPO cambia en ningun nodo tocado.
  (9) EL GRADO TOTAL NO SE MUEVE: las cuatro cifras del censo
      (`nodos_siguientes`, `nodos_previos`, suma y union) tienen que salir
      EXACTAMENTE IGUALES antes y despues. Si suben o bajan, se aborta: eso
      querria decir que la operacion no fue un giro.
  (10) EL RESULTADO ES EL GIRO: al terminar, la IDA esta presente y la VUELTA
      no lo esta.

MODOS: `--simular` (por defecto, CERO escrituras: todo el camino sobre una copia
en memoria) y `--ejecutar`. `--mutacion-negativa` apunta el giro a una direccion
que NINGUNA operacion del plan nombra, ELEGIDA POR COMPUTO del grafo y no
tecleada, para probar que la guarda (4) aborta sin escribir nada aunque se pase
`--ejecutar`.

EL SUJETO DE LA MUTACION NEGATIVA TIENE QUE TENER FORMA DE GIRO, y esto se
corrigio corriendolo. La primera version reusaba
`vuelta141_3_retirar_vuelta.direccion_sin_prohibicion`, que elige a proposito
una direccion con LAS DOS aristas puestas (para que la guarda 5 del RETIRADOR no
se adelante). Aqui eso hace que muerda la guarda 3 ("las dos estan puestas: eso
es una PODA") y no la 4, que es la que esta prueba mide: aborta sin escribir,
si, pero por el motivo equivocado, y un caso rojo que cae por otra guarda no
prueba la que dice probar (EJECUTOR.md regla 1). El selector propio de aqui,
`direccion_de_giro_sin_prohibicion`, exige las tres cosas a la vez: la VUELTA
puesta, la IDA ausente, y el par NO nombrado por ninguna `aristas_nuevas` del
plan en ninguna de las dos direcciones.

USO:
  python scripts/loop/vuelta143_3c_girar_arista.py --retirar-de revision_portafolio_periodica \
      --retirar-a sistema_gates_go_kill --por-la-op OP-E-04
  ... --ejecutar
  ... --mutacion-negativa --ejecutar

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
"""
import argparse
import copy
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T
import vuelta141_3_retirar_vuelta as R


def sin_resolver_a(lista, resolver, objetivo):
    return [x for x in (lista or []) if resolver(x) != objetivo]


def dups(lista, resolver):
    r = [resolver(x) for x in (lista or [])]
    return len(r) - len(set(r))


def direccion_de_giro_sin_prohibicion(nodos, resolver, ops):
    """PARA LA MUTACION NEGATIVA. Elige POR COMPUTO una direccion con FORMA DE
    GIRO (la vuelta puesta y la ida ausente) que NINGUNA operacion del plan
    nombre en sus `aristas_nuevas`, en ninguna de las dos direcciones. Asi la
    guarda 3 pasa y la que muerde es la 4, que es la que esta prueba mide. No se
    teclea nada: se recorre el grafo."""
    nombradas = set()
    for o in ops:
        for a, b in T.pares_de_aristas(o, []):
            nombradas.add((resolver(a), resolver(b)))
            nombradas.add((resolver(b), resolver(a)))
    for nid in sorted(nodos):
        n = nodos[nid]
        if n.get("deprecado"):
            continue
        for x in (n.get("nodos_siguientes") or []):
            d = resolver(x)
            if d == nid or not T.vivo(nodos.get(d)):
                continue
            if (nid, d) in nombradas:
                continue
            # forma de giro: la vuelta nid -> d puesta y la ida d -> nid ausente
            if not T.arista_presente(nodos, resolver, nid, d)[0]:
                continue
            if T.arista_presente(nodos, resolver, d, nid)[0]:
                continue
            return nid, d
    return None, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--retirar-de", required=True, dest="de")
    ap.add_argument("--retirar-a", required=True, dest="a")
    ap.add_argument("--por-la-op", required=True, dest="por_la_op")
    ap.add_argument("--ejecutar", action="store_true")
    ap.add_argument("--mutacion-negativa", action="store_true", dest="mutacion")
    arg = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    ops = T.cargar_ops("WORK")
    por_id = {o["id_op"]: o for o in ops}
    if arg.por_la_op not in por_id:
        print("ROJO: %s no existe en %s" % (arg.por_la_op, T.REL_OPS))
        return 1
    op = por_id[arg.por_la_op]
    nodos = T.cargar_grafo("WORK")
    resolver = T.resolver_de(nodos)

    de, a = arg.de, arg.a
    if arg.mutacion:
        m_de, m_a = direccion_de_giro_sin_prohibicion(nodos, resolver, ops)
        if m_de is None:
            print("ROJO (arnes): no se hallo por computo ninguna direccion CON FORMA DE GIRO "
                  "y sin prohibicion. Sin sujeto no hay mutacion negativa, y ESO ES ROJO.")
            return 1
        de, a = m_de, m_a
        print("MUTACION NEGATIVA: el giro se apunta a %s -> %s, elegida POR COMPUTO porque "
              "tiene FORMA DE GIRO (la vuelta puesta y la ida ausente) y NO esta nombrada en "
              "ninguna aristas_nuevas del plan. Asi la guarda 3 pasa y la que tiene que "
              "morder es la 4." % (de, a))

    modo = ("MUTACION NEGATIVA (nunca escribe)" if arg.mutacion
            else ("EJECUTAR" if arg.ejecutar else "SIMULAR"))
    print("=" * 78)
    print("GIRO DE ARISTA . MODO %s" % modo)
    print("se RETIRA la vuelta %s -> %s y se ESCRIBE la ida %s -> %s" % (de, a, a, de))
    print("por la operacion %s" % arg.por_la_op)
    print("=" * 78)

    # ---- (1) extremos resueltos y vivos ------------------------------------
    rd, rh = resolver(de), resolver(a)
    if rd != de or rh != a:
        print("guarda 1, RESUELTOS POR ALIAS y se declara: %s -> %s (de %s -> %s)"
              % (rd, rh, de, a))
    else:
        print("guarda 1, los dos ids son DIRECTOS: no hay alias que resolver")
    vivos = T.vivo(nodos.get(rd)) and T.vivo(nodos.get(rh))
    print("guarda 1, los dos extremos existen y estan VIVOS: %s" % ("OK" if vivos else "ROJO"))
    if not vivos:
        print("SE ABORTA SIN ESCRIBIR NADA.")
        return 1

    # ---- (2) cero auto-aristas --------------------------------------------
    if rd == rh:
        print("guarda 2, cero auto-aristas: ROJO (los dos extremos resuelven a %s)" % rd)
        print("SE ABORTA SIN ESCRIBIR NADA.")
        return 1
    print("guarda 2, cero auto-aristas: OK")

    # ---- (3) el estado de partida es el de un GIRO -------------------------
    vuelta_hay, _, _ = T.arista_presente(nodos, resolver, rd, rh)
    ida_hay, _, _ = T.arista_presente(nodos, resolver, rh, rd)
    print("guarda 3, estado de partida: la VUELTA %s -> %s esta puesta: %s | la IDA %s -> %s "
          "esta puesta: %s" % (rd, rh, vuelta_hay, rh, rd, ida_hay))
    if not vuelta_hay or ida_hay:
        print("guarda 3: ROJO. Esto NO es un giro.")
        if vuelta_hay and ida_hay:
            print("   las DOS estan puestas: eso es una PODA, y se hace con "
                  "vuelta141_3_retirar_vuelta.py.")
        elif not vuelta_hay and not ida_hay:
            print("   NINGUNA esta puesta: eso es una ESCRITURA, y se hace con "
                  "vuelta140_3_escribir_aristas.py.")
        else:
            print("   solo esta la IDA: no hay vuelta que retirar.")
        print("SE ABORTA SIN ESCRIBIR NADA.")
        return 1
    print("guarda 3: OK, es un giro")

    # ---- (4) la ficha prohibe la vuelta Y nombra el par --------------------
    frase, nota = R.prohibicion_de(op, resolver, rd, rh)
    print("guarda 4, la ficha PROHIBE la vuelta y NOMBRA el par: %s"
          % ("OK" if frase else "ROJO"))
    print("   %s" % (("%s %s" % (frase, nota)) if frase else nota))
    if not frase:
        print("SE ABORTA SIN ESCRIBIR NADA (guarda 3.d del encargo).")
        return 1

    # ---- (5) el par NO esta exceptuado ------------------------------------
    # LOS FALLOS DEL PARSER SE RECOGEN Y ABORTAN (TAREA 2.b, vuelta 144; acta
    # 143, adjudicacion 3.3 y caida de la casa 4.4). Hasta la vuelta 143 esta
    # llamada pasaba una lista literal vacia y TIRABA los fallos: si el parseo
    # de la excepcion fallaba, el conjunto salia vacio, `exceptuado` salia
    # False, la guarda 5 decia OK y EL GIRO PROCEDIA A BORRAR UNA ARISTA. De
    # los tres instrumentos que leen la excepcion, este era el unico que se
    # comia sus fallos, y es el unico que DESTRUYE. Ahora hace lo mismo que
    # vuelta140_3_escribir_aristas.py:149-164: los recoge, los imprime y aborta
    # con ellos, ANTES de tocar nada.
    fallos_exc = []
    exceptuados, cita_exc, nomina_exc = T.pares_exceptuados_de(op, resolver, fallos_exc)
    if fallos_exc:
        print("guarda 5, la lectura de la excepcion de la ficha: ROJO, %d fallo(s)"
              % len(fallos_exc))
        for f in fallos_exc:
            print("   %s" % f)
        print("   NO se puede saber si el par esta exceptuado, y un giro BORRA una arista.")
        print("SE ABORTA SIN ESCRIBIR NADA.")
        return 1
    exceptuado = frozenset((rd, rh)) in exceptuados
    print("guarda 5, el par NO esta exceptuado por la ficha: %s"
          % ("ROJO" if exceptuado else "OK"))
    if nomina_exc:
        print("   pares exceptuados que la ficha nombra (%d): %s"
              % (len(nomina_exc), ", ".join(nomina_exc)))
    if exceptuado:
        print("   el par %s SI esta en la excepcion (%s): lleva sus dos direcciones a "
              "proposito y girarlo borraria una arista legitima."
              % (" <-> ".join(sorted((rd, rh))), cita_exc))
        print("SE ABORTA SIN ESCRIBIR NADA.")
        return 1

    # ---- el giro, sobre una COPIA en memoria -------------------------------
    antes = R.cifras_del_censo(nodos, resolver)
    copia = copy.deepcopy(nodos)
    res_c = T.resolver_de(copia)
    # retirada de la vuelta rd -> rh, en las dos vistas
    copia[rd]["nodos_siguientes"] = sin_resolver_a(copia[rd].get("nodos_siguientes"), res_c, rh)
    copia[rh]["nodos_previos"] = sin_resolver_a(copia[rh].get("nodos_previos"), res_c, rd)
    # escritura de la ida rh -> rd, en las dos vistas, con los IDS RESUELTOS (P.9)
    copia[rh].setdefault("nodos_siguientes", []).append(rd)
    copia[rd].setdefault("nodos_previos", []).append(rh)
    print("guarda 6, P.9: lo que se escribe son los ids VIVOS resueltos %r y %r" % (rh, rd))

    # ---- (7) cero duplicadas NUEVAS tras resolver -------------------------
    crece = False
    for nid, campo in ((rd, "nodos_siguientes"), (rh, "nodos_previos"),
                       (rh, "nodos_siguientes"), (rd, "nodos_previos")):
        d0 = dups(nodos[nid].get(campo), resolver)
        d1 = dups(copia[nid].get(campo), res_c)
        print("guarda 7, duplicadas tras resolver en %s.%s: %d -> %d" % (nid, campo, d0, d1))
        if d1 > d0:
            crece = True
    if crece:
        print("guarda 7: ROJO, el giro fabricaria una duplicada NUEVA. SE ABORTA.")
        return 1
    print("guarda 7: OK, cero duplicadas nuevas")

    # ---- (8) ningun otro campo cambia -------------------------------------
    otros = []
    for nid in (rd, rh):
        for k in copia[nid]:
            if k in ("nodos_siguientes", "nodos_previos"):
                continue
            if copia[nid][k] != nodos[nid].get(k):
                otros.append("%s.%s" % (nid, k))
    print("guarda 8, ningun otro campo cambia: %s" % ("OK" if not otros else "ROJO %s" % otros))
    if otros:
        print("SE ABORTA SIN ESCRIBIR NADA.")
        return 1

    # ---- (9) el grado total NO se mueve -----------------------------------
    despues = R.cifras_del_censo(copia, res_c)
    print("guarda 9, EL GRADO TOTAL NO SE MUEVE (es un giro, no una poda ni una escritura):")
    print("   antes  : sig %d prev %d suma %d union %d"
          % (antes["sig"], antes["prev"], antes["suma"], antes["union"]))
    print("   despues: sig %d prev %d suma %d union %d"
          % (despues["sig"], despues["prev"], despues["suma"], despues["union"]))
    iguales = all(antes[k] == despues[k] for k in ("sig", "prev", "suma", "union"))
    print("   las CUATRO cifras identicas: %s" % iguales)
    if not iguales:
        print("SE ABORTA SIN ESCRIBIR NADA: si el grado se mueve, no fue un giro.")
        return 1

    # ---- (10) el resultado es el giro -------------------------------------
    vuelta_desp, _, _ = T.arista_presente(copia, res_c, rd, rh)
    ida_desp, _, _ = T.arista_presente(copia, res_c, rh, rd)
    print("guarda 10, resultado: la IDA %s -> %s esta puesta: %s | la VUELTA %s -> %s esta "
          "puesta: %s" % (rh, rd, ida_desp, rd, rh, vuelta_desp))
    if not ida_desp or vuelta_desp:
        print("guarda 10: ROJO. SE ABORTA SIN ESCRIBIR NADA.")
        return 1
    print("guarda 10: OK")

    if arg.mutacion:
        print("")
        print("MUTACION NEGATIVA: NO DEBIA LLEGAR AQUI. La guarda 4 tenia que haber abortado. "
              "CAIDA DEL ARNES.")
        return 1

    if not arg.ejecutar:
        print("")
        print("SIMULACION: cero escrituras. El giro esta listo para --ejecutar.")
        return 0

    # ---- escritura en disco, solo los dos ficheros de nodo ----------------
    for nid in (rd, rh):
        datos, cola = R.leer_crudo(nid)
        datos["nodos_siguientes"] = copia[nid].get("nodos_siguientes") or []
        datos["nodos_previos"] = copia[nid].get("nodos_previos") or []
        R.escribir_crudo(nid, datos, cola)
    print("")
    print("ESCRITO. ficheros de nodo tocados: 2 (%s, %s)" % (rd, rh))
    sucio = subprocess.run(["git", "status", "--porcelain", "--", "dataset/nodos/"],
                           cwd=T.RAIZ, capture_output=True, text=True).stdout.strip()
    print("git status --porcelain -- dataset/nodos/ tras el giro:")
    for ln in sucio.splitlines():
        print("   %s" % ln)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
