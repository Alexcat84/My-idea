# -*- coding: utf-8 -*-
r"""vuelta140_3_poda_del_solape_sexto.py . LA PODA DEL SOLAPE DE OP-M-01-SEXTO
(TAREA 3, remitida 3 de 5, de la vuelta 140).

QUE ES ESTA OPERACION. `OP-M-01-SEXTO` es de tipo `ENLACE MAS PODA DEL SOLAPE`,
y su nota dice que es *"LA PRIMERA OPERACION DEL PLAN QUE COBRA UNA A SIN
FUNDIR"*: sus dos veredictos A (puestos 488 y LD-52) son ciertos y dicen que un
bloque de `gestion_de_portafolio_gates_go_kill` REPITE lo que el superviviente
ya trae, asi que ese bloque **se poda** en vez de fundirse, y **la arista
sustituye al bloque podado**.

ESTE INSTRUMENTO SOLO PODA. La arista la escribe
`vuelta140_3_escribir_aristas.py --op OP-M-01-SEXTO`, que es el mismo que las
demas remitidas, para que la escritura de aristas tenga UN solo camino.

LA PODA SE LEE CONTRA EL NODO DE HOY, NO CONTRA LA FICHA (encargo de la vuelta
140, TAREA 3, punto 3): el superviviente `sistema_gates_go_kill` quedo en 17
pasos tras `OP-M-01-FUSION` de la vuelta 139, y la ficha se sello el 12 ago
2026 contra un nodo de 6 pasos. Si la poda que la ficha describe ya no calzara
con el nodo fundido, este instrumento CAE EN ROJO y no poda nada.

LAS GUARDAS, y cada una sale de una VERIFICACION LITERAL de la ficha:
  (G1) el nodo a podar existe y esta VIVO.
  (G2) EL PASO QUE SE PODA NO SE ELIGE POR SU NUMERO: se BUSCA por su
       contenido (habla de establecer gates o puntos de decision formales con
       criterios visibles de Go/Kill) y se comprueba que el hallado es el que
       la ficha llama "el paso 2". Si la busqueda halla cero o mas de uno, o si
       no cae en la posicion que la ficha dice, es ROJO. Un indice tecleado
       envejece; una busqueda con su comprobacion, no.
  (G3) LA PODA CALZA CONTRA EL NODO DE HOY (verificacion 0 de la ficha): el
       superviviente tiene que traer, EN SU TEXTO DE HOY, las dos mitades de lo
       que se poda (definir los gates, y criterios claros y visibles). Si no las
       trae, la poda estaria tirando algo que nadie mas dice: ROJO.
  (G4) LAS CUATRO PIEZAS PROPIAS SIGUEN EN EL NODO TRAS LA PODA (verificacion 1
       de la ficha: *"si al podar el paso 2 se lleva por delante el embudo o los
       seis criterios, la poda se paso de larga"*). Las cuatro se buscan por su
       marca en el texto que QUEDA, no en el que habia.
  (G5) se poda EXACTAMENTE UN paso: 5 -> 4.
  (G6) ningun otro campo del nodo cambia.

TODAS LAS BUSQUEDAS DE TEXTO VAN SIN TILDES EN LOS DOS LADOS. Es la correccion
1 de la vuelta 139 hecha regla: una busqueda que compara "vision general" contra
un texto que la lleva con tilde da 0 y parece una medicion.

MODOS: `--simular` (por defecto, cero escrituras) y `--ejecutar`.
`--mutacion-negativa` borra en memoria del superviviente la mitad de texto que
la G3 exige, y comprueba que la G3 CAE y no se poda nada. El valor esperado NO
es un literal: se compara el veredicto de la G3 con mutacion contra el veredicto
de la G3 sin ella, y tienen que ser DISTINTOS.

USO:
  python scripts/loop/vuelta140_3_poda_del_solape_sexto.py
  python scripts/loop/vuelta140_3_poda_del_solape_sexto.py --ejecutar
  python scripts/loop/vuelta140_3_poda_del_solape_sexto.py --mutacion-negativa
"""
import argparse
import io
import json
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

OP = "OP-M-01-SEXTO"
A_PODAR = "gestion_de_portafolio_gates_go_kill"
SUPERVIVIENTE_FICHA = "sistema_gates_go_kill"

# La marca del paso que se poda, sacada de la verificacion 0 de la ficha:
# "el paso 2, establecer gates formales con criterios visibles de Go/Kill".
MARCA_DEL_PASO = ("establecer gates", "go/kill")
POSICION_QUE_DICE_LA_FICHA = 2

# Las dos mitades que el superviviente tiene que traer para que la poda calce
# (G3). Salen del texto del propio paso podado, partido en sus dos mitades.
MITADES_EN_EL_SUPERVIVIENTE = [
    ("define los gates", "definir los gates", "establece los gates"),
    ("criterios claros y visibles", "criterios visibles", "criterios claros"),
]

# Las CUATRO piezas propias, con la marca de cada una, sacadas del campo
# `preservar` de la ficha.
PIEZAS_PROPIAS = [
    ("EL EMBUDO", "embudo"),
    ("LOS SEIS CRITERIOS", "seis criterios"),
    ("MATAR EN FIRME", "matar"),
    ("EL BALANCE Y LA MEZCLA", "balance y mezcla"),
]


def plano(texto):
    """Sin tildes y en minusculas, en los DOS lados de toda comparacion."""
    d = unicodedata.normalize("NFD", texto or "")
    return "".join(c for c in d if unicodedata.category(c) != "Mn").lower()


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


def guarda_3(pasos_superviviente):
    """Devuelve (ok, detalle). Se saca a funcion propia para que la mutacion
    negativa la llame dos veces y compare los DOS veredictos computados."""
    detalle = []
    ok = True
    llanos = [plano(p) for p in pasos_superviviente]
    for alternativas in MITADES_EN_EL_SUPERVIVIENTE:
        hallada = None
        for alt in alternativas:
            for i, p in enumerate(llanos, 1):
                if plano(alt) in p:
                    hallada = (alt, i)
                    break
            if hallada:
                break
        detalle.append((alternativas[0], hallada))
        if hallada is None:
            ok = False
    return ok, detalle


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    ap.add_argument("--mutacion-negativa", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    modo = ("MUTACION NEGATIVA (nunca escribe)" if a.mutacion_negativa
            else ("EJECUTAR" if a.ejecutar else "SIMULAR"))
    print("=" * 78)
    print("PODA DEL SOLAPE DE %s . MODO %s" % (OP, modo))
    print("=" * 78)

    nodos = T.cargar_grafo("WORK")
    resolver = T.resolver_de(nodos)
    fallos = []

    # (G1)
    d, cola = leer_crudo(A_PODAR)
    n_grafo = nodos.get(A_PODAR)
    vivo = T.vivo(n_grafo)
    print("(G1) %s existe y esta VIVO: %s" % (A_PODAR, vivo))
    if not vivo:
        fallos.append("(G1) %s no esta vivo" % A_PODAR)

    sup = resolver(SUPERVIVIENTE_FICHA)
    n_sup = nodos.get(sup)
    print("     el superviviente de la ficha, %s, resuelve hoy a %s (vivo=%s) y tiene %d pasos"
          % (SUPERVIVIENTE_FICHA, sup, T.vivo(n_sup),
             len((n_sup or {}).get("pasos_accionables") or [])))

    pasos = list(d.get("pasos_accionables") or [])
    print("")
    print("(G2) EL PASO QUE SE PODA, BUSCADO POR SU CONTENIDO y no por su numero:")
    candidatos = []
    for i, p in enumerate(pasos, 1):
        pl = plano(p)
        if all(plano(m) in pl for m in MARCA_DEL_PASO):
            candidatos.append((i, p))
    for i, p in candidatos:
        print("     candidato en la posicion %d: %s" % (i, p))
    if len(candidatos) != 1:
        print("     ROJO: se hallaron %d candidatos y la ficha nombra UNO" % len(candidatos))
        fallos.append("(G2) %d candidatos a podar, se esperaba 1" % len(candidatos))
        pos = None
    else:
        pos = candidatos[0][0]
        calza = (pos == POSICION_QUE_DICE_LA_FICHA)
        print("     el hallado esta en la posicion %d y la ficha dice 'el paso %d': %s"
              % (pos, POSICION_QUE_DICE_LA_FICHA, "OK" if calza else "ROJO"))
        if not calza:
            fallos.append("(G2) el paso hallado esta en %d y la ficha dice %d"
                          % (pos, POSICION_QUE_DICE_LA_FICHA))

    # (G3) la poda calza contra el nodo de HOY
    pasos_sup = list((n_sup or {}).get("pasos_accionables") or [])
    if a.mutacion_negativa:
        limpio_ok, _ = guarda_3(pasos_sup)
        pasos_sup = [p for p in pasos_sup
                     if not any(plano(alt) in plano(p)
                                for alt in MITADES_EN_EL_SUPERVIVIENTE[1])]
        print("")
        print("MUTACION NEGATIVA: se borran EN MEMORIA del superviviente los pasos que")
        print("traen la 2.a mitad. Pasos del superviviente: %d -> %d"
              % (len((n_sup or {}).get("pasos_accionables") or []), len(pasos_sup)))
        print("   veredicto de la G3 SIN mutar (computado): %s" % limpio_ok)

    ok3, detalle3 = guarda_3(pasos_sup)
    print("")
    print("(G3) LA PODA CALZA CONTRA EL NODO DE HOY (las dos mitades de lo podado")
    print("     viven en el texto del superviviente):")
    for marca, hallada in detalle3:
        if hallada:
            print("     '%s' -> hallada como '%s' en el paso %d de %s"
                  % (marca, hallada[0], hallada[1], sup))
        else:
            print("     '%s' -> NO HALLADA en ningun paso de %s" % (marca, sup))
    print("     veredicto G3 (computado): %s" % ok3)
    if a.mutacion_negativa:
        print("   los DOS veredictos de la G3, sin mutar y mutado: %s y %s. DISTINTOS: %s"
              % (limpio_ok, ok3, limpio_ok != ok3))
        if limpio_ok == ok3:
            print("CAIDA DEL ARNES: la mutacion no movio el veredicto, el caso no prueba nada.")
            return 1
    if not ok3:
        fallos.append("(G3) el superviviente NO trae en su texto de hoy lo que la poda "
                      "quita: podar seria perder catalogo")

    if fallos:
        print("")
        print("SE ABORTA SIN PODAR NADA, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("   [ROJO] %s" % f)
        return 1

    if a.mutacion_negativa:
        print("")
        print("MUTACION NEGATIVA: NO DEBIA LLEGAR AQUI con la G3 caida. CAIDA DEL ARNES.")
        return 1

    podado = pasos[pos - 1]
    quedan = pasos[:pos - 1] + pasos[pos:]
    print("")
    print("EL PASO QUE SE PODA, entero:")
    print("   %s" % podado)
    print("PASOS: %d -> %d" % (len(pasos), len(quedan)))

    # (G4) las cuatro piezas propias siguen en lo que QUEDA
    print("")
    print("(G4) LAS CUATRO PIEZAS PROPIAS DE `preservar`, buscadas en el texto QUE QUEDA:")
    llanos = [plano(p) for p in quedan]
    for nombre, marca in PIEZAS_PROPIAS:
        donde = [i for i, p in enumerate(llanos, 1) if plano(marca) in p]
        print("     %-24s (marca '%s') -> paso(s) %s" % (nombre, marca, donde or "NINGUNO"))
        if not donde:
            fallos.append("(G4) la pieza propia %s NO sobrevive a la poda" % nombre)

    # (G5)
    print("")
    print("(G5) se poda EXACTAMENTE UN paso: %s (%d -> %d)"
          % ("OK" if len(quedan) == len(pasos) - 1 else "ROJO", len(pasos), len(quedan)))
    if len(quedan) != len(pasos) - 1:
        fallos.append("(G5) se podaron %d pasos" % (len(pasos) - len(quedan)))

    # (G6)
    nuevo = json.loads(json.dumps(d))
    nuevo["pasos_accionables"] = quedan
    otros = [k for k in nuevo if k != "pasos_accionables" and nuevo[k] != d.get(k)]
    otros += ["%s (borrado)" % k for k in d if k not in nuevo]
    print("(G6) ningun otro campo del nodo cambia: %s" % ("OK" if not otros else "ROJO %s" % otros))
    if otros:
        fallos.append("(G6) cambian otros campos: %s" % otros)

    if fallos:
        print("")
        print("SE ABORTA SIN PODAR NADA, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("   [ROJO] %s" % f)
        return 1

    if not a.ejecutar:
        print("")
        print("SIMULACION: cero escrituras. La poda esta lista para --ejecutar.")
        return 0

    with io.open(ruta(A_PODAR), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(nuevo, ensure_ascii=False, indent=2) + cola)
    print("")
    print("PODADO. fichero tocado: dataset/nodos/%s.json (1 paso menos, ningun otro campo)"
          % A_PODAR)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
