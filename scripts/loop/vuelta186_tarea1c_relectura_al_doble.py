# -*- coding: utf-8 -*-
r"""vuelta186_tarea1c_relectura_al_doble.py . LA RELECTURA AL DOBLE DEL TRAMO DE
LA CIEGA DEL ACTA 186 (la que el auditor sello como V187).

QUIEN LA ENCARGA Y CON QUE PALABRAS. `AUDITOR.md` 1.2, leida hoy: *"si una
discrepancia aparece FUERA de los discutibles marcados, baja el credito de toda la
tanda: ese tramo se relee al doble y lo dices en el acta"*. Y el acta 186, seccion
4: *"EL CREDITO DE LA TANDA BAJA, Y NO POR FORMULA SINO POR LA LETRA: las cuatro
discrepancias caen FUERA de los discutibles marcados, porque el reporte no marco
ninguno"*. Las discrepancias son CUATRO, los puestos 338, 491, 1775 y 2599, y el
auditor LAS PIERDE LAS CUATRO a favor del archivo. Lo que llega al ejecutor es la
relectura, no la clase.

EL NOMBRE DEL SELLO NO SE DEDUCE DEL NUMERO DE VUELTA, Y ESTE ES EL PUNTO. La casa
nombra el sello del acta N como `V(N+1)`, asi que siendo acta **186** el sello se
llama **`V187`**. El `V186` NO EXISTE y no se fabrica: es el hueco que dejo la
`A.1` del acta 185, cuando aquel auditor nombro el suyo `V185b`. El encargo da las
rutas exactas y son las que estan aqui. Aqui no se copia el `sha256` del encargo:
se computa y se compara con el del sello.

QUE ES "AL DOBLE", DICHO ANTES DE HACERLO PARA QUE NO SE PUEDA ELEGIR DESPUES. Se
relee **el doble de puestos**: los 30 del tramo **mas 30 vecinos deterministas**.
La funcion `vecinos()` **SE IMPORTA** de
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`, no se copia, que es la
`6.6` del acta 172 al pie de la letra; y la maquina de la vara se importa de
`scripts/loop/vuelta182_tarea3_diferenciador_movido.py` por el mismo motivo.

CLON DECLARADO de `scripts/loop/vuelta185_tarea1e_relectura_al_doble.py`. Cambian
el sello (de `V185b` a `V187`, que es UNA DIFERENCIA MAS que declarar en el cotejo
de clones), la ciega, la ciega inmediatamente anterior (que ahora es la `V185b`),
la cabecera del acta que se cita de contraste, la lista de discrepancias (de siete
a cuatro), el nombre de la salida, y un bloque nuevo: LA CUENTA DE CLASES `B` DEL
UNIVERSO RELEIDO. El cotejo lo hace `scripts/loop/cotejar_clon_declarado.py` y su
salida se pega en el reporte con lo que salga.

LA CUENTA DE `B` NO SE INTERPRETA NI SE ADJUDICA: SOLO SE CUENTA. El encargo lo
pide con esas palabras, porque el puesto 338 es clase `B` y las `B` son 72 en todo
el archivo. Este fichero publica cuantas hay en el universo releido y no dice ni
una palabra mas sobre ellas.

LO QUE ESTA RELECTURA NO ES, Y SE DICE PARA NO VENDERLA DE MAS: **NO es una
relectura de juicio.** No vuelve a decidir la clase de ningun par. **Es la
relectura MECANICA del tramo con la vara**, que es la unica que se puede correr
sobre 60 pares sin inventarse nada. Lo que encuentre se nombra; **lo que la vara
no vea, esta salida NO lo afirma.**

USO:
  python scripts/loop/vuelta186_tarea1c_relectura_al_doble.py
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
SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_V187.json")
CIEGA = os.path.join(LOOP, "_auditor_v187_ciega_blind.txt")
NL = chr(10)
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 186"
PATRON_PUESTO = re.compile(r"^puesto_intra:\s*(\d+)\s*$")
# LAS CUATRO DISCREPANCIAS QUE EL ACTA 186 NOMBRA EN SU SECCION 4, Y QUE EL
# AUDITOR PIERDE LAS CUATRO A FAVOR DEL ARCHIVO. Van en una constante con
# nombre para que se vea que son un dato del acta y no del juicio de aqui.
LAS_CUATRO = [338, 491, 1775, 2599]


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
    w("VUELTA 186, TAREA 1.c: LA RELECTURA AL DOBLE DEL")
    w("TRAMO DE LA CIEGA DEL ACTA 186, encargada por AUDITOR.md 1.2 porque las")
    w("CUATRO discrepancias del auditor salieron FUERA del marcado")
    w("=" * 78)
    w("")

    w("A) EL CONTRASTE CON EL ACTA, QUE NO ES CORRECCION SINO COTEJO. EL")
    w("   ENCARGO YA NOMBRA LA FUENTE BUENA, Y AQUI SE MIDE QUE LISTA EL ACTA.")
    t_acta = io.open(ACTA, encoding="utf-8").read()
    ini9, fin9, cuerpo9 = seccion_del_acta(t_acta, CABECERA_ACTA, 4)
    if ini9 is None:
        w("   el acta 186 NO tiene seccion 4. Se dice y no se inventa.")
        puestos_sec9 = []
    else:
        w("   seccion 4 del acta 186: lineas %d a %d (%d lineas)"
          % (ini9, fin9, len(cuerpo9)))
        w("   su cabecera: %s" % cuerpo9[0].strip()[:100])
        puestos_sec9 = [int(x) for x in
                        re.findall(r"puesto_intra:\s*(\d+)", NL.join(cuerpo9))]
    w("   CIFRA puestos que la seccion 4 del acta 186 lista: %d" % len(puestos_sec9))
    w("   (la seccion 4 es la de la ciega, y publica el reparto y LAS CUATRO")
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
    w("   docs/loop/SELLO_APERTURA_AUDITOR_V187.json -> %d bytes en disco y %d "
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
    w("   (el criterio del sello dice que la muestra excluye 150 puestos: los 120 de")
    w("    las ciegas de las actas 183, 184, 185 y 185b, mas los 30 vecinos")
    w("    deterministas de la 1.e de la vuelta 185; aqui se comprueba contra la")
    w("    ciega INMEDIATAMENTE ANTERIOR en disco, que es la V185b)")
    ANTERIOR = os.path.join(LOOP, "_auditor_v185b_ciega_blind.txt")
    if os.path.exists(ANTERIOR):
        tramo_ant = puestos_de_la_ciega(io.open(ANTERIOR, encoding="utf-8").read())
        w("   ciega anterior: docs/loop/_auditor_v185b_ciega_blind.txt -> %d puestos"
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

    w("I) LAS CUATRO DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA VARA")
    w("   (el acta 186 las nombra en su seccion 4: los puestos 338, 491, 1775 y")
    w("    2599, que el auditor pierde LOS CUATRO a favor del archivo. Aqui NO se")
    w("    re-decide ninguna clase: solo se dice si estan en el universo releido y")
    w("    que ve la vara en ellas. LO QUE LA VARA NO VEA, NO SE AFIRMA)")
    for p in LAS_CUATRO:
        f = porpuesto.get(p)
        if f is None:
            w("   puesto %-6d NO ESTA EN EL ARCHIVO" % p)
            continue
        r = T3.analiza(f, porid)
        vivos_p = (f.get("nodo_a") in porid) and (f.get("nodo_b") in porid)
        w("   puesto %-6d clase %-3s declara %-3s lesion %-3s muertos %-3s | en el "
          "universo releido: %s"
          % (p, f.get("clase"), "SI" if r["declara"] else "no",
             "SI" if r["lesion"] else "no", "no" if vivos_p else "SI",
             "SI" if p in universo else "NO"))
        w("      nodos: %s contra %s" % (f.get("nodo_a"), f.get("nodo_b")))
    w("   CIFRA de las cuatro que caen DENTRO del universo releido: %d"
      % len([p for p in LAS_CUATRO if p in universo]))
    w("")

    w("I.1) CUANTAS CLASES `B` HAY EN EL UNIVERSO RELEIDO. SOLO SE CUENTA.")
    w("   (el encargo la pide con esas palabras porque el puesto 338 es clase `B`.")
    w("    ESTA CIFRA NO SE INTERPRETA NI SE ADJUDICA AQUI: se cuenta y se publica)")
    b_universo = [p for p in universo
                  if porpuesto.get(p) and porpuesto[p].get("clase") == "B"]
    w("   CIFRA clases `B` en el universo releido: %d de %d"
      % (len(b_universo), len(universo)))
    w("   LOS PUESTOS `B` DEL UNIVERSO: %s"
      % (", ".join(str(x) for x in b_universo) or "(ninguno)"))
    b_archivo = [f for f in filas if f.get("clase") == "B"]
    w("   CIFRA clases `B` en TODO el archivo, contadas del archivo y no del")
    w("   encargo: %d de %d filas" % (len(b_archivo), len(filas)))
    w("   de las cuatro discrepancias, cuales son clase `B`: %s"
      % (", ".join(str(p) for p in LAS_CUATRO
                   if porpuesto.get(p) and porpuesto[p].get("clase") == "B")
         or "(ninguna)"))
    w("")

    w("J) LO QUE ESTA RELECTURA SOSTIENE, Y NI UNA PALABRA MAS")
    w("   1. El tramo se leyo de la ciega SELLADA del auditor, cotejada por")
    w("      sha256 contra su propio sello, y NO del acta, que no lo lista. El")
    w("      sello se llama V187 porque la casa nombra el sello del acta N como")
    w("      V(N+1) y esta es el acta 186. El V186 NO EXISTE y no se fabrica: es")
    w("      el hueco que dejo la caida propia A.1 del acta 185. La ruta viene")
    w("      del encargo, no de deducirla del numero de vuelta.")
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
    w("   7. LA CUENTA DE CLASES `B` DEL UNIVERSO RELEIDO SE PUBLICA Y NO SE")
    w("      INTERPRETA. El encargo la pide porque el puesto 338 es `B`; aqui se")
    w("      cuenta y ahi se para.")
    w("")
    w("FIN")

    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V186_T1C_RELECTURA_AL_DOBLE.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
