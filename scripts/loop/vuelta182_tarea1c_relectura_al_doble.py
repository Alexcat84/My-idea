# -*- coding: utf-8 -*-
r"""vuelta182_tarea1c_relectura_al_doble.py . LA RELECTURA AL DOBLE DEL TRAMO DE
LA CIEGA DE LA VUELTA 181.

QUIEN LA ENCARGA Y CON QUE PALABRAS. El acta 181, adjudicacion `7.2`
(`docs/loop/ACTA_AUDITOR.md:63171`, leida hoy): *"El tramo se relee al doble
igualmente, por `AUDITOR.md` 1.2, porque salieron fuera del marcado"*. Y
`AUDITOR.md:57`, tambien leida hoy: *"si una discrepancia aparece FUERA de los
discutibles marcados, baja el credito de toda la tanda: ese tramo se relee al
doble y lo dices en el acta"*.

QUE ES EL TRAMO, Y NO SE TECLEA: los **30 puestos** que la seccion 8 del acta 181
lista. Se leen del acta con su linea, no de memoria.

QUE ES "AL DOBLE", DICHO ANTES DE HACERLO PARA QUE NO SE PUEDA ELEGIR DESPUES.
Se relee **el doble de puestos**: los 30 del tramo **mas 30 vecinos**, elegidos de
forma determinista (el puesto inmediatamente siguiente de cada uno que no este ya
en el tramo, subiendo hasta encontrar uno libre). **Sesenta en total.** Es la
lectura que el MODO AUSTERO de `EJECUTOR.md` ya usa para las lecturas dirigidas
("LOTES AL DOBLE"), aplicada aqui.

Y LA VECINDAD NO ES UN CAPRICHO: el puesto de al lado comparte dominio y banda
con el del tramo, asi que si el tramo tiene un sesgo, sus vecinos son el sitio
donde mas barato se ve.

QUE SE MIDE DE CADA UNO, Y ES MECANICO. La maquina **se importa** de
`scripts/loop/vuelta182_tarea3_diferenciador_movido.py`, no se copia:

  1. Si su razon **declara un diferenciador**.
  2. Si ese diferenciador **esta hoy** en los pasos del nodo que segun la razon no
     lo tiene, o sea si tiene **LESION EXACTA**.
  3. Si sus **dos nodos siguen vivos** en el grafo de hoy.

LO QUE ESTA RELECTURA NO ES, Y SE DICE PARA NO VENDERLA DE MAS: **NO es una
relectura de juicio.** No vuelve a decidir la clase de ningun par: eso es trabajo
de lectura humana y esta vuelta no la hace. **Es la relectura MECANICA del tramo
con la vara nueva de esta vuelta**, que es la unica que se puede correr sobre 60
pares sin inventarse nada. Lo que encuentre se nombra; lo que no pueda ver, se
declara que no lo ve.

USO:
  python scripts/loop/vuelta182_tarea1c_relectura_al_doble.py
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta182_tarea3_diferenciador_movido as T3   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
NL = chr(10)
CABECERA_181 = "# ACTA DEL AUDITOR, VUELTA 181"
AGUJA_PUESTOS = "LOS 30 PUESTOS SON"


def puestos_del_tramo():
    """LOS PUESTOS DEL TRAMO, LEIDOS DEL ACTA Y NO TECLEADOS.
    Devuelve (linea, lista) o (None, [])."""
    texto = io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
    lineas = texto.split(NL)
    base = [i for i, l in enumerate(lineas, 1) if l.startswith(CABECERA_181)]
    if len(base) != 1:
        return None, []
    for i in range(base[0], len(lineas)):
        if AGUJA_PUESTOS in lineas[i]:
            bloque = NL.join(lineas[i:i + 4])
            crudo = bloque.split(":", 1)[1] if ":" in bloque else ""
            return i + 1, [int(x) for x in re.findall(r"\d+", crudo.replace(".", ""))]
    return None, []


def vecinos(tramo, maximo, evitar=None):
    """EL DOBLE DEL TRAMO, DE FORMA DETERMINISTA Y REPRODUCIBLE. PURA.

    Para cada puesto del tramo se toma el siguiente libre hacia arriba; si se
    sale del archivo, se baja. Ni azar ni semilla: la misma entrada da siempre la
    misma salida, y eso es lo que hace que otro pueda repetir esta lectura.

    EL CONJUNTO `evitar` NACE EN LA VUELTA 188 (TAREA 5.a), Y ES ADITIVO
    (adjudicacion `5.2` y respuesta `7.3` del acta 188, contestando la `P.3` del
    reporte de la 187: **el solape se le exige AL UNIVERSO**, porque la exclusion
    existe para que nadie relea lo ya leido y los 60 se leen todos).

    **SU REGLA NO CAMBIA: CAMBIA LO QUE SE LE PASA.** Sin `evitar` se comporta
    EXACTAMENTE igual que antes, y eso no se afirma, se prueba: el arnes
    `scripts/loop/vuelta188_tarea5a_mutacion_vecinos_evitar.py` lleva dentro una
    copia CONGELADA de la version anterior y exige que las dos den la misma
    salida sobre una bateria de tramos.

    CON `evitar`, ademas de saltar los puestos del propio tramo, salta los de ese
    conjunto **al subir y al bajar**, de forma que **el cero del solape sale por
    construccion y no por suerte**. Eso es exactamente lo que el reporte de la 187
    NO hizo, y con razon: torcer una funcion congelada a mitad de la medicion es
    lo que `P.5.1` prohibe. **La vara no se tuerce; se le pasa otra cosa.**"""
    fuera = set(evitar or ())
    elegidos = []
    ocupados = set(tramo) | fuera
    for p in sorted(tramo):
        q = p + 1
        while q in ocupados and q <= maximo:
            q += 1
        if q > maximo:
            q = p - 1
            while q in ocupados and q >= 1:
                q -= 1
        if 1 <= q <= maximo and q not in fuera:
            elegidos.append(q)
            ocupados.add(q)
    return sorted(elegidos)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 182, TAREA 1.c: LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DE LA 181")
    w("encargada por la adjudicacion 7.2 del acta 181, por AUDITOR.md 1.2")
    w("=" * 78)
    w("")

    linea, tramo = puestos_del_tramo()
    if not tramo:
        w("ROJO: no se pudo leer el tramo del acta. No se inventa ninguno.")
        print(NL.join(L))
        return 1
    w("A) EL TRAMO, LEIDO DEL ACTA CON SU LINEA")
    w("   docs/loop/ACTA_AUDITOR.md:%d" % linea)
    w("   CIFRA puestos del tramo: %d" % len(tramo))
    w("   LOS PUESTOS: %s" % ", ".join(str(x) for x in sorted(tramo)))
    w("")

    filas = [json.loads(l) for l in io.open(T3.VEREDICTOS, encoding="utf-8")
             if l.strip()]
    porpuesto = {f.get("puesto_intra"): f for f in filas}
    maximo = max(porpuesto)
    grafo = json.load(io.open(T3.GRAFO, encoding="utf-8"))
    porid = T3.nodos_por_id(grafo)
    w("B) LOS DOS SUJETOS, CONTADOS")
    w("   veredictos: %d filas | maximo puesto %d" % (len(filas), maximo))
    w("   grafo: %d nodos" % len(porid))
    w("")

    dobles = vecinos(tramo, maximo)
    w("C) EL DOBLE, ELEGIDO DE FORMA DETERMINISTA Y NO POR AZAR")
    w("   CIFRA vecinos anadidos: %d" % len(dobles))
    w("   LOS VECINOS: %s" % ", ".join(str(x) for x in dobles))
    w("   SOLAPE CON EL TRAMO: %d" % len(set(dobles) & set(tramo)))
    universo = sorted(set(tramo) | set(dobles))
    w("   CIFRA puestos que se releen EN TOTAL: %d" % len(universo))
    w("   ES EL DOBLE DEL TRAMO: %s"
      % ("SI" if len(universo) == 2 * len(tramo) else
         "NO, son %d y el doble seria %d" % (len(universo), 2 * len(tramo))))
    w("")

    w("D) LA RELECTURA MECANICA, PUESTO A PUESTO")
    w("   (la maquina se IMPORTA de vuelta182_tarea3_diferenciador_movido.py)")
    w("   %-6s %-6s %-8s %-8s %-7s %-6s  %s"
      % ("puesto", "clase", "declara", "lesion", "vivos", "cober", "nodos"))
    n_declaran = n_lesion = n_muertos = 0
    lesionados = []
    for p in universo:
        f = porpuesto.get(p)
        if f is None:
            w("   %-6d NO ESTA EN EL ARCHIVO" % p)
            continue
        r = T3.analiza(f, porid)
        vivos = (f.get("nodo_a") in porid) and (f.get("nodo_b") in porid)
        if not vivos:
            n_muertos += 1
        if r["declara"]:
            n_declaran += 1
        if r["lesion"]:
            n_lesion += 1
            lesionados.append((p, r))
        w("   %-6d %-6s %-8s %-8s %-7s %-6.2f  %s contra %s%s"
          % (p, f.get("clase"), "SI" if r["declara"] else "no",
             "SI" if r["lesion"] else "no", "SI" if vivos else "NO",
             r["cobertura"], f.get("nodo_a"), f.get("nodo_b"),
             "   <-- DEL TRAMO" if p in tramo else ""))
    w("")

    w("E) LAS CIFRAS DE LA RELECTURA")
    w("   CIFRA puestos releidos: %d" % len(universo))
    w("   CIFRA que declaran diferenciador: %d" % n_declaran)
    w("   CIFRA con LESION EXACTA: %d" % n_lesion)
    w("   CIFRA con algun nodo MUERTO en el grafo de hoy: %d" % n_muertos)
    w("   LOS LESIONADOS: %s"
      % (", ".join(str(p) for p, _r in lesionados) or "(ninguno)"))
    for p, r in lesionados:
        w("      PUESTO %d: %s" % (p, r["motivo"][:150]))
    w("")

    w("F) LO QUE ESTA RELECTURA SOSTIENE, Y NI UNA PALABRA MAS")
    w("   1. El tramo se releyo AL DOBLE: %d puestos contra los %d del tramo."
      % (len(universo), len(tramo)))
    w("   2. De los %d, %d declaran un diferenciador y %d lo tienen HOY movido al"
      % (len(universo), n_declaran, n_lesion))
    w("      otro nodo. El 2.464 esta en el tramo y sale: %s"
      % ("SI" if any(p == T3.PUESTO_OBLIGATORIO for p, _r in lesionados) else "NO"))
    w("   3. Ningun par de este tramo tiene un nodo muerto: %s"
      % ("SI, cero muertos" if n_muertos == 0 else "NO, hay %d" % n_muertos))
    w("   4. ESTA RELECTURA NO VUELVE A DECIDIR NINGUNA CLASE. Es la relectura")
    w("      MECANICA del tramo con la vara nueva de esta vuelta, no una lectura")
    w("      de juicio. Lo que la vara no ve, esta salida NO lo afirma.")
    w("")
    w("FIN")

    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_T1C_RELECTURA_AL_DOBLE.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
