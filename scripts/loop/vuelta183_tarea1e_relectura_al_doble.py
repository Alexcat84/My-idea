# -*- coding: utf-8 -*-
r"""vuelta183_tarea1e_relectura_al_doble.py . LA RELECTURA AL DOBLE DEL TRAMO DE
LA CIEGA DE LA VUELTA 182.

QUIEN LA ENCARGA Y CON QUE PALABRAS. `AUDITOR.md:57`, leida hoy: *"si una
discrepancia aparece FUERA de los discutibles marcados, baja el credito de toda la
tanda: ese tramo se relee al doble y lo dices en el acta"*. Y el acta 182, seccion
4: *"EL TRAMO SE RELEE AL DOBLE, por `AUDITOR.md:57`, porque las seis salieron
fuera del marcado"*. Las seis discrepancias son del auditor y las adjudica a favor
del archivo; lo que llega al ejecutor es la relectura.

CORRECCION DECLARADA, Y NO SE TAPA LO QUE CORRIGE. El encargo de esta vuelta dice
que el tramo son *"los 30 puestos de la seccion 9 de mi acta 182, leidos del acta
y no tecleados"*. **Medido antes de escribir una linea de este fichero**, en el
bloque H.8 de `docs/loop/SALIDA_V183_APERTURA.txt`: la seccion 9 del acta 182
(lineas 63644 a 63658) es **LA METRICA DE CREDITO**, una tabla de siete filas que
dice *"puestos | 30 aislados, 30 limpios | 736"* **y no lista ningun puesto**. El
parseo de esa seccion devolvio **CERO puestos**. La ciega del acta 182 es su
**seccion 4**, y ahi solo estan **los 6 puestos que discrepan**, no los 30.

DE DONDE SALEN LOS 30, ENTONCES, Y POR QUE ESTA ES LA FUENTE Y NO OTRA. Del
fichero que el propio auditor sello antes de su primer comando de verificacion:
`docs/loop/_auditor_v183_ciega_blind.txt`, nombrado en
`docs/loop/SELLO_APERTURA_AUDITOR_V183.json` con sus **41.200 bytes** y su
`sha256`. **Es una fuente MEJOR que el acta, no peor:** el acta seria una copia a
mano de lo que ese fichero ya dice, y esta relectura coteja ademas el `sha256` del
sello contra el fichero de hoy, asi que si alguien lo hubiera movido, esta salida
lo diria antes de leer un solo puesto.

QUE ES "AL DOBLE", DICHO ANTES DE HACERLO PARA QUE NO SE PUEDA ELEGIR DESPUES. Se
relee **el doble de puestos**: los 30 del tramo **mas 30 vecinos deterministas**.
La funcion `vecinos()` **SE IMPORTA** de
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`, no se copia, que es la
`6.6` del acta 172 al pie de la letra; y la maquina de la vara se importa de
`scripts/loop/vuelta182_tarea3_diferenciador_movido.py` por el mismo motivo.

LO QUE ESTA RELECTURA NO ES, Y SE DICE PARA NO VENDERLA DE MAS: **NO es una
relectura de juicio.** No vuelve a decidir la clase de ningun par. **Es la
relectura MECANICA del tramo con la vara**, que es la unica que se puede correr
sobre 60 pares sin inventarse nada. Lo que encuentre se nombra; **lo que la vara
no vea, esta salida NO lo afirma.**

USO:
  python scripts/loop/vuelta183_tarea1e_relectura_al_doble.py
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
SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_V183.json")
CIEGA = os.path.join(LOOP, "_auditor_v183_ciega_blind.txt")
NL = chr(10)
CABECERA_182 = "# ACTA DEL AUDITOR, VUELTA 182"
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
    seccion 9 del acta 182 no lista ningun puesto. Una correccion que no ensena
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
    w("VUELTA 183, TAREA 1.e: LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DE LA 182")
    w("encargada por AUDITOR.md:57, porque las seis discrepancias salieron")
    w("FUERA del marcado")
    w("=" * 78)
    w("")

    w("A) LA CORRECCION DECLARADA: DONDE EL ENCARGO DICE QUE ESTA EL TRAMO Y")
    w("   DONDE ESTA DE VERDAD. NO SE TAPA LO QUE SE CORRIGE.")
    t_acta = io.open(ACTA, encoding="utf-8").read()
    ini9, fin9, cuerpo9 = seccion_del_acta(t_acta, CABECERA_182, 9)
    if ini9 is None:
        w("   el acta 182 NO tiene seccion 9. Se dice y no se inventa.")
        puestos_sec9 = []
    else:
        w("   seccion 9 del acta 182: lineas %d a %d (%d lineas)"
          % (ini9, fin9, len(cuerpo9)))
        w("   su cabecera: %s" % cuerpo9[0].strip()[:100])
        puestos_sec9 = [int(x) for x in
                        re.findall(r"puesto_intra:\s*(\d+)", NL.join(cuerpo9))]
    w("   CIFRA puestos que la seccion 9 lista: %d" % len(puestos_sec9))
    w("   (el encargo dice que el tramo son los 30 puestos de esa seccion; la")
    w("    seccion es LA METRICA DE CREDITO y no lista ninguno. Se declara y se")
    w("    va a la fuente que si los tiene, que es la del propio auditor)")
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
    w("   docs/loop/SELLO_APERTURA_AUDITOR_V183.json -> %d bytes en disco y %d "
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

    w("F) EL SOLAPE CON EL TRAMO DE LA 181, MEDIDO Y NO SUPUESTO")
    w("   (el criterio del sello dice que la muestra excluye los 30 de la 181 y")
    w("    los 43 de la 180; aqui se comprueba contra el tramo que la 182 releyo)")
    try:
        from vuelta182_tarea1c_relectura_al_doble import puestos_del_tramo as p181
        linea181, tramo181 = p181()
        w("   tramo de la 181, leido del acta: %d puestos (linea %s)"
          % (len(tramo181), linea181))
        w("   SOLAPE del tramo de hoy con el de la 181: %d"
          % len(set(tramo) & set(tramo181)))
    except Exception as e:
        w("   NO SE PUDO LEER EL TRAMO DE LA 181: %r" % (e,))
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

    w("I) LAS SEIS DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA VARA")
    w("   (el acta 182 las nombra en su seccion 4: 375, 393, 1280, 1815, 2416 y")
    w("    2470. Aqui NO se re-decide ninguna clase: solo se dice si estan en el")
    w("    universo releido y que ve la vara en ellas)")
    for p in (375, 393, 1280, 1815, 2416, 2470):
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
    w("      sha256 contra su propio sello, y NO del acta, que no lo lista.")
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
    ruta = os.path.join(LOOP, "SALIDA_V183_T1E_RELECTURA_AL_DOBLE.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
