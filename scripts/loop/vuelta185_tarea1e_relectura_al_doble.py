# -*- coding: utf-8 -*-
r"""vuelta185_tarea1e_relectura_al_doble.py . LA RELECTURA AL DOBLE DEL TRAMO DE
LA CIEGA DEL ACTA 185 (la que el auditor sello como V185b).

QUIEN LA ENCARGA Y CON QUE PALABRAS. `AUDITOR.md` 1.2, leida hoy: *"si una
discrepancia aparece FUERA de los discutibles marcados, baja el credito de toda la
tanda: ese tramo se relee al doble y lo dices en el acta"*. Y el acta 185, seccion
4: *"EL CREDITO DE LA TANDA BAJA, Y NO POR FORMULA SINO POR LA LETRA: las siete
discrepancias caen FUERA de los discutibles marcados, porque el reporte no marco
ninguno"*. Las discrepancias son SIETE, los puestos 1208, 1459, 2363, 2386, 2505,
2636 y 2854, y el auditor LAS PIERDE LAS SIETE: las adjudica a favor del archivo
sin regatear. Lo que llega al ejecutor es la relectura, no la clase.

EL NOMBRE DEL SELLO NO SE DEDUCE DEL NUMERO DE VUELTA, Y ESTE ES EL PUNTO. El
auditor de la 185 nombro su sello `V185b` cuando la casa lo nombra `V186`, y lo
declaro como su caida propia `A.1`. El fichero del que este clona lleva la ruta
`SELLO_APERTURA_AUDITOR_V185.json` CLAVADA EN UNA CONSTANTE, y un clon que copiara
esa linea leeria el sello equivocado. **El encargo da las tres rutas exactas y son
las que estan aqui.** Aqui no se copia el `sha256` del encargo: se computa y se
compara con el del sello.

QUE ES "AL DOBLE", DICHO ANTES DE HACERLO PARA QUE NO SE PUEDA ELEGIR DESPUES. Se
relee **el doble de puestos**: los 30 del tramo **mas 30 vecinos deterministas**.
La funcion `vecinos()` **SE IMPORTA** de
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`, no se copia, que es la
`6.6` del acta 172 al pie de la letra; y la maquina de la vara se importa de
`scripts/loop/vuelta182_tarea3_diferenciador_movido.py` por el mismo motivo.

CLON DECLARADO de `scripts/loop/vuelta184_tarea1d_relectura_al_doble.py`. Cambian
el sello, la ciega, la ciega anterior, la cabecera del acta que se cita de
contraste, la lista de discrepancias (de tres a siete) y el nombre de la salida.
El cotejo lo hace `scripts/loop/cotejar_clon_declarado.py` y su salida se pega en
el reporte con lo que salga.

LO QUE ESTA RELECTURA NO ES, Y SE DICE PARA NO VENDERLA DE MAS: **NO es una
relectura de juicio.** No vuelve a decidir la clase de ningun par. **Es la
relectura MECANICA del tramo con la vara**, que es la unica que se puede correr
sobre 60 pares sin inventarse nada. Lo que encuentre se nombra; **lo que la vara
no vea, esta salida NO lo afirma.**

USO:
  python scripts/loop/vuelta185_tarea1e_relectura_al_doble.py
"""
import hashlib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta182_tarea3_diferenciador_movido as T3   # noqa: E402
from vuelta182_tarea1c_relectura_al_doble import vecinos   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_V185b.json")
CIEGA = os.path.join(LOOP, "_auditor_v185b_ciega_blind.txt")
NL = chr(10)
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 185"
PATRON_PUESTO = re.compile(r"^puesto_intra:\s*(\d+)\s*$")


def puestos_de_la_ciega(texto):
    """LOS PUESTOS DEL TRAMO, LEIDOS DE LA SALIDA CIEGA Y NO TECLEADOS.

    PURA: recibe el texto del fichero. Devuelve la lista ordenada y sin
    repetidos, o lista vacia si el fichero no trae ninguno, que se declara en vez
    de inventarse."""
    vistos = []
    for linea in texto.replace(chr(13) + NL, NL).split(NL):
        m = PATRON_PUESTO.match(linea.strip())
        if m:
            vistos.append(int(m.group(1)))
    return sorted(set(vistos))


def seccion_del_acta(texto, cabecera, numero):
    """LA SECCION `## <numero>.` DE UN ACTA, ACOTADA. Devuelve (inicio, fin,
    lineas) en numeracion de 1, o (None, None, []) si no esta. PURA.

    Se usa SOLO para publicar el contraste con lo que el encargo dice: que la
    seccion 4 del acta 184 no lista ningun puesto. Una correccion que no ensena
    lo que corrige no se puede auditar (`EJECUTOR.md` 8)."""
    lineas = texto.replace(chr(13) + NL, NL).split(NL)
    base = [i for i, l in enumerate(lineas, 1) if l.startswith(cabecera)]
    if len(base) != 1:
        return None, None, []
    ini = None
    for i in range(base[0], len(lineas)):
        if lineas[i].startswith("## %d. " % numero):
            ini = i + 1
            break
    if ini is None:
        return None, None, []
    fin = len(lineas)
    for i in range(ini, len(lineas)):
        if lineas[i].startswith("## "):
            fin = i
            break
    return ini, fin, lineas[ini - 1:fin]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 185, TAREA 1.e: LA RELECTURA AL DOBLE DEL")
    w("TRAMO DE LA CIEGA DEL ACTA 185, encargada por AUDITOR.md 1.2 porque las")
    w("SIETE discrepancias del auditor salieron FUERA del marcado")
    w("=" * 78)
    w("")

    w("A) EL CONTRASTE CON EL ACTA, QUE NO ES CORRECCION SINO COTEJO. EL")
    w("   ENCARGO YA NOMBRA LA FUENTE BUENA, Y AQUI SE MIDE QUE LISTA EL ACTA.")
    t_acta = io.open(ACTA, encoding="utf-8").read()
    ini9, fin9, cuerpo9 = seccion_del_acta(t_acta, CABECERA_ACTA, 4)
    if ini9 is None:
        w("   el acta 185 NO tiene seccion 4. Se dice y no se inventa.")
        puestos_sec9 = []
    else:
        w("   seccion 4 del acta 185: lineas %d a %d (%d lineas)"
          % (ini9, fin9, len(cuerpo9)))
        w("   su cabecera: %s" % cuerpo9[0].strip()[:100])
        puestos_sec9 = [int(x) for x in
                        re.findall(r"puesto_intra:\s*(\d+)", NL.join(cuerpo9))]
    w("   CIFRA puestos que la seccion 4 del acta 185 lista: %d" % len(puestos_sec9))
    w("   (la seccion 4 es la de la ciega, y publica el reparto y LAS SIETE")
    w("    discrepancias, no los 30 puestos. Por eso el tramo se lee de la ciega")
    w("    sellada del auditor, que es donde estan, y no del acta)")
    w("")

    w("B) LA FUENTE DE VERDAD DEL TRAMO, COTEJADA CONTRA SU PROPIO SELLO")
    if not os.path.exists(SELLO) or not os.path.exists(CIEGA):
        w("   ROJO: falta el sello o la ciega del auditor. Sin ellos NO hay tramo")
        w("   que releer, y eso se dice en vez de fabricar uno.")
        print(NL.join(L))
        return 1
    sello = json.load(io.open(SELLO, encoding="utf-8"))
    datos = io.open(CIEGA, "rb").read()
    sha_hoy = hashlib.sha256(datos).hexdigest()
    w("   docs/loop/SELLO_APERTURA_AUDITOR_V185b.json -> %d bytes en disco y %d "
      "bytes normalizados a LF"
      % (os.path.getsize(SELLO), len(io.open(SELLO, "rb").read()
                                     .replace(chr(13).encode() + NL.encode(),
                                              NL.encode()))))
    w("   ciega: %s" % sello.get("ciega"))
    w("   bytes que el sello declara: %d | bytes en disco hoy: %d"
      % (sello.get("bytes_ciega", -1), os.path.getsize(CIEGA)))
    w("   sha256 del sello: %s" % sello.get("sha256_ciega", "(ninguno)"))
    w("   sha256 de hoy   : %s" % sha_hoy)
    calza = (sha_hoy == sello.get("sha256_ciega")
             and os.path.getsize(CIEGA) == sello.get("bytes_ciega"))
    w("   EL FICHERO ES EL QUE EL SELLO DICE: %s" % ("SI" if calza else "NO"))
    if not calza:
        w("   ROJO: la ciega de hoy NO es la que el auditor sello. Un tramo leido")
        w("   de un fichero movido no es el tramo. No se relee nada.")
        print(NL.join(L))
        return 1
    w("   criterio escrito, literal del sello:")
    w("      %s" % sello.get("criterio", "")[:200])
    w("")

    tramo = puestos_de_la_ciega(io.open(CIEGA, encoding="utf-8").read())
    w("C) EL TRAMO, LEIDO DE LA CIEGA SELLADA Y NO TECLEADO")
    w("   CIFRA puestos del tramo: %d" % len(tramo))
    w("   LOS PUESTOS: %s" % ", ".join(str(x) for x in tramo))
    if not tramo:
        w("   ROJO: la ciega no trae ningun puesto. No se inventa ninguno.")
        print(NL.join(L))
        return 1
    w("")

    filas = [json.loads(l) for l in io.open(T3.VEREDICTOS, encoding="utf-8")
             if l.strip()]
    porpuesto = {f.get("puesto_intra"): f for f in filas}
    maximo = max(porpuesto)
    grafo = json.load(io.open(T3.GRAFO, encoding="utf-8"))
    porid = T3.nodos_por_id(grafo)
    w("D) LOS DOS SUJETOS, CONTADOS")
    w("   veredictos: %d filas | maximo puesto %d" % (len(filas), maximo))
    w("   grafo: %d nodos" % len(porid))
    w("")

    dobles = vecinos(tramo, maximo)
    w("E) EL DOBLE, ELEGIDO DE FORMA DETERMINISTA Y NO POR AZAR")
    w("   (la funcion vecinos() se IMPORTA de")
    w("    scripts/loop/vuelta182_tarea1c_relectura_al_doble.py, no se copia)")
    w("   CIFRA vecinos anadidos: %d" % len(dobles))
    w("   LOS VECINOS: %s" % ", ".join(str(x) for x in dobles))
    w("   SOLAPE CON EL TRAMO: %d" % len(set(dobles) & set(tramo)))
    universo = sorted(set(tramo) | set(dobles))
    w("   CIFRA puestos que se releen EN TOTAL: %d" % len(universo))
    w("   ES EL DOBLE DEL TRAMO: %s"
      % ("SI" if len(universo) == 2 * len(tramo) else
         "NO, son %d y el doble seria %d" % (len(universo), 2 * len(tramo))))
    w("")

    w("F) EL SOLAPE CON EL TRAMO ANTERIOR, MEDIDO Y NO SUPUESTO")
    w("   (el criterio del sello dice que la muestra excluye los 90 puestos de")
    w("    las ciegas de las actas 183, 184 y del turno de auditor 185 que sello y")
    w("    murio sin escribir acta; aqui se comprueba contra esa ultima, que es la")
    w("    ciega inmediatamente anterior en disco)")
    ANTERIOR = os.path.join(LOOP, "_auditor_v185_ciega_blind.txt")
    if os.path.exists(ANTERIOR):
        tramo_ant = puestos_de_la_ciega(io.open(ANTERIOR, encoding="utf-8").read())
        w("   ciega anterior: docs/loop/_auditor_v185_ciega_blind.txt -> %d puestos"
          % len(tramo_ant))
        w("   SOLAPE del tramo de hoy con el anterior: %d"
          % len(set(tramo) & set(tramo_ant)))
    else:
        w("   LA CIEGA ANTERIOR NO ESTA EN DISCO. No se afirma ningun solape.")
    w("")

    w("G) LA RELECTURA MECANICA, PUESTO A PUESTO")
    w("   (la maquina se IMPORTA de vuelta182_tarea3_diferenciador_movido.py)")
    w("   %-6s %-6s %-8s %-8s %-7s %-6s  %s"
      % ("puesto", "clase", "declara", "lesion", "vivos", "cober", "nodos"))
    n_declaran = n_lesion = n_muertos = 0
    lesionados = []
    por_clase = {}
    for p in universo:
        f = porpuesto.get(p)
        if f is None:
            w("   %-6d NO ESTA EN EL ARCHIVO" % p)
            continue
        por_clase[f.get("clase")] = por_clase.get(f.get("clase"), 0) + 1
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

    w("H) LAS CIFRAS DE LA RELECTURA")
    w("   CIFRA puestos releidos: %d" % len(universo))
    w("   CIFRA que declaran diferenciador: %d" % n_declaran)
    w("   CIFRA con LESION EXACTA: %d" % n_lesion)
    w("   CIFRA con algun nodo MUERTO en el grafo de hoy: %d" % n_muertos)
    for k in sorted(por_clase, key=lambda x: (x is None, x)):
        w("   CIFRA clase %-6r: %d" % (k, por_clase[k]))
    w("   LOS LESIONADOS: %s"
      % (", ".join(str(p) for p, _r in lesionados) or "(ninguno)"))
    for p, r in lesionados:
        w("      PUESTO %d: %s" % (p, r["motivo"][:150]))
    w("")

    w("I) LAS SIETE DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA VARA")
    w("   (el acta 185 las nombra en su seccion 4: los puestos 1208, 1459, 2363,")
    w("    2386, 2505, 2636 y 2854, que el auditor pierde LOS SIETE a favor del")
    w("    archivo. Aqui NO se re-decide ninguna clase: solo se dice si estan en el")
    w("    universo releido y que ve la vara en ellas. LO QUE LA VARA NO VEA, NO SE")
    w("    AFIRMA)")
    for p in (1208, 1459, 2363, 2386, 2505, 2636, 2854):
        f = porpuesto.get(p)
        if f is None:
            w("   puesto %-6d NO ESTA EN EL ARCHIVO" % p)
            continue
        r = T3.analiza(f, porid)
        w("   puesto %-6d clase %-3s declara %-3s lesion %-3s | en el universo "
          "releido: %s"
          % (p, f.get("clase"), "SI" if r["declara"] else "no",
             "SI" if r["lesion"] else "no", "SI" if p in universo else "NO"))
    w("")

    w("J) LO QUE ESTA RELECTURA SOSTIENE, Y NI UNA PALABRA MAS")
    w("   1. El tramo se leyo de la ciega SELLADA del auditor, cotejada por")
    w("      sha256 contra su propio sello, y NO del acta, que no lo lista. El")
    w("      sello se llama V185b y no V186 porque el auditor lo nombro asi y lo")
    w("      declaro como su caida propia A.1: la ruta viene del encargo, no de")
    w("      deducirla del numero de vuelta.")
    w("   2. El tramo se releyo AL DOBLE: %d puestos contra los %d del tramo."
      % (len(universo), len(tramo)))
    w("   3. De los %d, %d declaran un diferenciador y %d lo tienen HOY movido al"
      % (len(universo), n_declaran, n_lesion))
    w("      otro nodo.")
    w("   4. Puestos con algun nodo muerto en el grafo de hoy: %d." % n_muertos)
    w("   5. ESTA RELECTURA NO VUELVE A DECIDIR NINGUNA CLASE. Es la relectura")
    w("      MECANICA del tramo con la vara, no una lectura de juicio. Lo que la")
    w("      vara no ve, esta salida NO lo afirma.")
    w("   6. NINGUN VEREDICTO SE MUEVE EN ESTA VUELTA: el archivo se abre para")
    w("      leer y se cierra, y su sha256 va medido en la apertura y en el")
    w("      cierre del reporte.")
    w("")
    w("FIN")

    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V185_T1E_RELECTURA_AL_DOBLE.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
