# -*- coding: utf-8 -*-
r"""vuelta141_3_retirar_vuelta.py . RETIRA LA VUELTA DE UNA ESCALERA, POR LA
CONTRAORDEN DEL 12 ago 2026 (TAREA 3.c de la vuelta 141).

QUE HACE, Y NO MAS. Retira UNA direccion `A -> B` de las DOS vistas
(`A.nodos_siguientes` y `B.nodos_previos`) de `dataset/nodos/*.json`,
resolviendo por alias (P.1) antes de tocar nada. Ningun otro campo cambia.

DE DONDE SALE LA AUTORIDAD PARA BORRAR, y no es de aqui: de la CONTRAORDEN DEL
AUDITOR del 12 ago 2026 en docs/plan/EXPEDIENTE_MESA_JUNTA_ASESORA.md, "en una
escalera, la arista de vuelta no es redundante, es FALSA", con su remedio
operativo escrito: la vuelta SE RETIRA del campo, en el mismo commit de la
operacion que lo descubre, y EL GRADO TOTAL NO SUBE. Este script EXIGE que una
operacion del plan PROHIBA esa vuelta en su `verificacion`, y la cita; si
ninguna la prohibe, ABORTA (guarda 3.d del encargo: la contraorden cubre la
vuelta de una escalera que una ficha prohibe, no cubre podar el grafo por
gusto).

LAS GUARDAS, todas con su salida impresa, y si UNA cae no se escribe nada:
  (1) LOS DOS EXTREMOS resuelven por alias y estan VIVOS. Se declara si el id
      dado resuelve a otro.
  (2) CERO AUTO-ARISTAS: los dos extremos no resuelven al mismo nodo.
  (3) LA VUELTA EXISTE HOY, medida en las DOS VISTAS. Retirar lo que no esta es
      un ROJO, no un salto.
  (4) UNA OPERACION DEL PLAN LA PROHIBE: alguna linea de `verificacion` de
      `--por-la-op` dice que la vuelta no debe existir. La frase se CITA.
  (5) LA IDA SIGUE PRESENTE al terminar. Si el retiro dejara al par sin ninguna
      arista, es ROJO: una escalera sin peldano no es una escalera.
  (6) EL GRADO TOTAL SE MIDE ANTES Y DESPUES, en las cuatro cifras del censo
      (`nodos_siguientes`, `nodos_previos`, suma y union). PODA: la union baja
      EXACTAMENTE en 1 y no sube. Si sube, se aborta.
  (7) CERO DUPLICADAS Y CERO AUTO-ARISTAS tras resolver en las dos listas
      tocadas, medido despues.

MODOS: `--simular` (por defecto, CERO escrituras: hace todo el camino sobre una
copia en memoria) y `--ejecutar`. `--mutacion-negativa` apunta el retiro a una
direccion que NINGUNA operacion prohibe, ELEGIDA POR COMPUTO del grafo y no
tecleada, para probar que la guarda (4) aborta sin escribir nada aunque se pase
`--ejecutar`.

USO:
  python scripts/loop/vuelta141_3_retirar_vuelta.py --de asignacion_recursos_en_gates \
      --a sistema_gates_go_kill --por-la-op OP-M-01-ESLABONES
  ... --ejecutar
  ... --mutacion-negativa --ejecutar
"""
import argparse
import copy
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T

RAIZ = T.RAIZ
NODOS = os.path.join(RAIZ, "dataset", "nodos")

# Las mismas frases literales que la vara de enlace de tallar_estado_de_fase.py
# usa para clasificar el regimen de vuelta de una ficha. No se duplican: se
# importan, para que el que mide y el que borra lean la ficha igual.
FRASES_PROHIBE = T.FRASES_PROHIBE_VUELTA


def ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def leer_crudo(nid):
    with io.open(ruta(nid), encoding="utf-8", newline="") as fh:
        bruto = fh.read()
    cola = ""
    while bruto and bruto[-1] in "\r\n":
        cola = bruto[-1] + cola
        bruto = bruto[:-1]
    return json.loads(bruto), cola


def escribir_crudo(nid, datos, cola):
    with io.open(ruta(nid), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def cifras_del_censo(nodos, resolver):
    """Las cuatro cifras del censo, con la misma definicion que
    scripts/loop/vuelta83_conteo_aristas.py: sig, prev, suma y union de pares
    (a, b) SIN resolver, que es como el censo de la cabecera las cuenta."""
    sig = set()
    prev = set()
    nsig = nprev = 0
    for nid, n in nodos.items():
        s = n.get("nodos_siguientes") or []
        p = n.get("nodos_previos") or []
        nsig += len(s)
        nprev += len(p)
        for x in s:
            sig.add((nid, x))
        for x in p:
            prev.add((x, nid))
    return dict(sig=nsig, prev=nprev, suma=nsig + nprev, union=len(sig | prev))


def prohibicion_de(op, resolver, rd, rh):
    """La linea de `verificacion` que prohibe la vuelta DE ESTE PAR, CITADA, o
    None con el motivo.

    NO BASTA CON QUE LA FICHA TRAIGA UNA CLAUSULA DE ESCALERA. Se exige ADEMAS
    que la ficha NOMBRE ESTE PAR en sus `aristas_nuevas` (en cualquiera de las
    dos direcciones, tras resolver): la contraorden cubre "la vuelta de una
    escalera QUE UNA FICHA PROHIBE", o sea la vuelta de UNA FILA SUYA, no
    cualquier arista del grafo que le apetezca a quien invoca el script. Sin
    esta segunda mitad, una ficha con clausula de escalera autorizaria a podar
    cualquier cosa, que es justo lo que la guarda 3.d del encargo prohibe."""
    frase = None
    for i, linea in enumerate(op.get("verificacion") or []):
        bajo = (linea or "").lower()
        for f in FRASES_PROHIBE:
            if f in bajo:
                frase = "verificacion %d de %s: %r" % (i, op.get("id_op"), linea)
                break
        if frase:
            break
    if frase is None:
        return None, ("%s no trae ninguna linea de verificacion que prohiba la vuelta"
                      % op.get("id_op"))
    suyo = set()
    for x, y in T.pares_de_aristas(op, []):
        suyo.add((resolver(x), resolver(y)))
    if (rh, rd) in suyo:
        return frase, "y la IDA %s -> %s es una fila de %s" % (rh, rd, op.get("id_op"))
    if (rd, rh) in suyo:
        return frase, ("y el par esta en %s, pero como fila %s -> %s: la direccion que se "
                       "retira es la que la ficha PROPONE" % (op.get("id_op"), rd, rh))
    return None, ("%s trae la clausula de escalera pero NO NOMBRA este par en sus "
                  "aristas_nuevas: la contraorden cubre la vuelta de UNA FILA SUYA, no "
                  "cualquier arista del grafo" % op.get("id_op"))


def direccion_sin_prohibicion(nodos, resolver, ops):
    """PARA LA MUTACION NEGATIVA. Elige POR COMPUTO una direccion que NINGUNA
    operacion del plan nombre en sus aristas_nuevas Y CUYA IDA TAMBIEN ESTE
    PRESENTE, para que la guarda 5 (la ida sigue puesta) no se adelante y sea
    la guarda 4 la que muerda, que es la que esta prueba mide. No se teclea
    nada: se recorre el grafo."""
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
            if d == nid or (nodos.get(d) or {}).get("deprecado"):
                continue
            if (nid, d) in nombradas:
                continue
            if not T.arista_presente(nodos, resolver, nid, d)[0]:
                continue
            if not T.arista_presente(nodos, resolver, d, nid)[0]:
                continue
            return nid, d
    return None, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--de", required=True)
    ap.add_argument("--a", required=True)
    ap.add_argument("--por-la-op", required=True, dest="por_la_op")
    ap.add_argument("--ejecutar", action="store_true")
    ap.add_argument("--mutacion-negativa", action="store_true", dest="mutacion")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    ops = T.cargar_ops("WORK")
    por_id = {o.get("id_op"): o for o in ops}
    nodos = T.cargar_grafo("WORK")
    resolver = T.resolver_de(nodos)

    modo = "EJECUTAR" if a.ejecutar else "SIMULAR"
    print("=" * 78)
    print("RETIRO DE LA VUELTA | MODO: %s%s" % (modo, "  (MUTACION NEGATIVA)" if a.mutacion else ""))
    print("=" * 78)

    de, hacia = a.de, a.a
    if a.mutacion:
        de, hacia = direccion_sin_prohibicion(nodos, resolver, ops)
        if de is None:
            print("ROJO (arnes): no hay ninguna direccion presente que ninguna ficha nombre.")
            return 1
        print("MUTACION NEGATIVA: la direccion se ELIGE POR COMPUTO entre las que ninguna")
        print("ficha del plan nombra en sus aristas_nuevas. Elegida: %s -> %s" % (de, hacia))

    op = por_id.get(a.por_la_op)
    if op is None:
        print("ROJO: la operacion %s no existe en %s" % (a.por_la_op, T.REL_OPS))
        return 1

    fallos = []

    # (1) y (2)
    rd, rh = resolver(de), resolver(hacia)
    print("")
    print("GUARDA 1, LOS DOS EXTREMOS RESUELTOS (P.1) Y VIVOS:")
    for dado, res in ((de, rd), (hacia, rh)):
        n = nodos.get(res)
        print("   %s -> resuelve a %s | existe %s | vivo %s%s"
              % (dado, res, n is not None, bool(n) and not n.get("deprecado"),
                 "  (EL ID DADO ESTA DEPRECADO Y SE DECLARA)" if dado != res else ""))
        if n is None or n.get("deprecado"):
            fallos.append("%s no resuelve a un nodo vivo" % dado)
    print("GUARDA 2, CERO AUTO-ARISTAS: %s" % ("ROJO, los dos resuelven a %s" % rd
                                               if rd == rh else "OK, %s != %s" % (rd, rh)))
    if rd == rh:
        fallos.append("auto-arista: los dos extremos resuelven a %s" % rd)

    # (3)
    presente, _, _ = T.arista_presente(nodos, resolver, rd, rh)
    ida, _, _ = T.arista_presente(nodos, resolver, rh, rd)
    print("GUARDA 3, LA VUELTA EXISTE HOY (dos vistas): %s -> %s : %s"
          % (rd, rh, "PRESENTE" if presente else "NO PRESENTE"))
    print("           y la IDA:                          %s -> %s : %s"
          % (rh, rd, "PRESENTE" if ida else "NO PRESENTE"))
    if not presente:
        fallos.append("la vuelta %s -> %s no esta presente: no hay nada que retirar" % (rd, rh))

    # (4)
    cita, nota = prohibicion_de(op, resolver, rd, rh)
    print("GUARDA 4, UNA OPERACION DEL PLAN PROHIBE LA VUELTA DE ESTE PAR:")
    if cita:
        print("   SI. %s" % cita)
        print("       %s" % nota)
    else:
        print("   NO. %s" % nota)
        fallos.append("%s: la contraorden no cubre podar el grafo por gusto "
                      "(guarda 3.d del encargo)" % nota)

    # (5)
    print("GUARDA 5, LA IDA SIGUE PRESENTE AL TERMINAR: %s"
          % ("OK, la ida esta puesta" if ida else "ROJO, el par quedaria sin ninguna arista"))
    if not ida:
        fallos.append("la ida %s -> %s no esta presente: retirar la vuelta dejaria el par suelto"
                      % (rh, rd))

    # (6) LA SIMULACION, SIEMPRE, SOBRE COPIA EN MEMORIA.
    antes = cifras_del_censo(nodos, resolver)
    simulado = copy.deepcopy(nodos)
    n_de, n_hacia = simulado[rd], simulado[rh]
    quitadas_sig = [x for x in (n_de.get("nodos_siguientes") or []) if resolver(x) == rh]
    quitadas_prev = [x for x in (n_hacia.get("nodos_previos") or []) if resolver(x) == rd]
    n_de["nodos_siguientes"] = [x for x in (n_de.get("nodos_siguientes") or [])
                                if resolver(x) != rh]
    n_hacia["nodos_previos"] = [x for x in (n_hacia.get("nodos_previos") or [])
                                if resolver(x) != rd]
    despues = cifras_del_censo(simulado, resolver)
    print("")
    print("GUARDA 6, EL GRADO TOTAL ANTES Y DESPUES (simulacion sobre copia en memoria):")
    print("   entradas literales que se quitarian: de %s.nodos_siguientes %s | de "
          "%s.nodos_previos %s" % (rd, quitadas_sig, rh, quitadas_prev))
    for k in ("sig", "prev", "suma", "union"):
        print("   %-6s antes %6d  despues %6d  delta %+d"
              % (k, antes[k], despues[k], despues[k] - antes[k]))
    delta_union = despues["union"] - antes["union"]
    if delta_union != -1:
        fallos.append("la union del grafo se mueve en %+d y una PODA tiene que bajarla en "
                      "exactamente 1 (contraorden del 12 ago 2026)" % delta_union)
    else:
        print("   PODA CORRECTA: la union baja en exactamente 1 y no sube.")

    # (7)
    resolver_sim = T.resolver_de(simulado)
    print("")
    print("GUARDA 7, CERO DUPLICADAS Y CERO AUTO-ARISTAS NUEVAS TRAS RESOLVER.")
    print("   LO QUE SE MIDE ES EL DELTA, NO EL TOTAL, y es la misma decision que la")
    print("   guarda 6 de vuelta140_3_escribir_aristas.py ya tomo: las duplicadas que YA")
    print("   ESTABAN se imprimen para que se vean, pero no bloquean, porque tienen dueno")
    print("   escrito (OP-S-12, atadura 2 del 00_INDICE) y castigar a quien no las hizo")
    print("   bloquea sin arreglar nada. Un RETIRO ademas no puede fabricar duplicadas:")
    print("   solo quita entradas. Si el delta no es cero, algo muy raro paso.")

    def dups_y_autos(grafo, res, nid, campo):
        lista = grafo[nid].get(campo) or []
        resueltos = [res(x) for x in lista]
        dups = sorted({x for x in resueltos if resueltos.count(x) > 1})
        autos = sorted({x for x in resueltos if x == nid})
        return len(lista), dups, autos

    for nid, campo in ((rd, "nodos_siguientes"), (rh, "nodos_previos")):
        n_a, dups_a, autos_a = dups_y_autos(nodos, resolver, nid, campo)
        n_d, dups_d, autos_d = dups_y_autos(simulado, resolver_sim, nid, campo)
        nuevas = [x for x in dups_d if x not in dups_a]
        autos_nuevos = [x for x in autos_d if x not in autos_a]
        print("   %s.%s: %d -> %d entradas" % (nid, campo, n_a, n_d))
        print("      duplicadas YA PRESENTES (no bloquean, dueno OP-S-12): %s"
              % (dups_a or "ninguna"))
        print("      duplicadas NUEVAS: %s | auto-aristas NUEVAS: %s"
              % (nuevas or "ninguna", autos_nuevos or "ninguna"))
        if nuevas:
            fallos.append("%s.%s gana duplicadas nuevas tras resolver: %s" % (nid, campo, nuevas))
        if autos_nuevos:
            fallos.append("%s.%s gana auto-aristas nuevas: %s" % (nid, campo, autos_nuevos))

    print("")
    if fallos:
        print("ROJO, %d guarda(s) caen. NO SE ESCRIBE NADA (ni siquiera en modo --ejecutar):"
              % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("VERDE: las 7 guardas pasan.")
    if not a.ejecutar:
        print("MODO SIMULAR: cero escrituras. Para escribir, --ejecutar.")
        return 0

    for nid, campo, quitadas in ((rd, "nodos_siguientes", quitadas_sig),
                                 (rh, "nodos_previos", quitadas_prev)):
        datos, cola = leer_crudo(nid)
        antes_lista = list(datos.get(campo) or [])
        datos[campo] = [x for x in antes_lista if x not in quitadas]
        escribir_crudo(nid, datos, cola)
        print("   ESCRITO %s.%s: %d -> %d entradas (quitadas: %s)"
              % (nid, campo, len(antes_lista), len(datos[campo]), quitadas))
    print("")
    print("EJECUTADO: la vuelta %s -> %s queda retirada en las dos vistas." % (rd, rh))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
