# -*- coding: utf-8 -*-
r"""vuelta187_tarea3_relectura_al_doble.py . LA RELECTURA AL DOBLE DEL TRAMO DE
LA CIEGA DEL ACTA 187 (la que el auditor sello como V188).

QUIEN LA ENCARGA Y CON QUE PALABRAS. `AUDITOR.md` 1.2, leida hoy: *"si una
discrepancia aparece FUERA de los discutibles marcados, baja el credito de toda la
tanda: ese tramo se relee al doble y lo dices en el acta"*. Y el acta 187, seccion
10: *"EL CREDITO DE LA TANDA BAJA POR LA LETRA: cuatro discrepancias fuera del
marcado, y tres fuera incluso de mis propios dudosos"*. Las discrepancias son
CUATRO, los puestos 226, 603, 1612 y 2448, y el auditor LAS PIERDE LAS CUATRO a
favor del archivo. Lo que llega al ejecutor es la relectura, no la clase.

EL NOMBRE DEL SELLO NO SE DEDUCE DEL NUMERO DE VUELTA, Y ESTE ES EL PUNTO. La casa
nombra el sello del acta N como `V(N+1)`, asi que siendo acta **187** el sello se
llama **`V188`**. El `V186` NO EXISTE y no se fabrica. El encargo da las rutas
exactas y son las que estan aqui. Aqui no se copia el `sha256` del encargo: se
computa y se compara con el del sello.

QUE ES "AL DOBLE", DICHO ANTES DE HACERLO PARA QUE NO SE PUEDA ELEGIR DESPUES. Se
relee **el doble de puestos**: los 30 del tramo **mas 30 vecinos deterministas**.
La funcion `vecinos()` **SE IMPORTA** de
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`, no se copia, que es la
`6.6` del acta 172 al pie de la letra; y la maquina de la vara se importa de
`scripts/loop/vuelta182_tarea3_diferenciador_movido.py` por el mismo motivo.

CLON DECLARADO de `scripts/loop/vuelta186_tarea1c_relectura_al_doble.py`. Cambian
el sello (de `V187` a `V188`), la ciega, la ciega inmediatamente anterior (que
ahora es la `V187`), la cabecera del acta que se cita de contraste, la lista de
discrepancias (otras cuatro), el nombre de la salida, UN TERCER SOLAPE QUE LA 186
NO MEDIA (contra los 293 puestos de `docs/loop/_auditor_v188_exclusion.txt`) y el
bloque de las `B`, que aqui no se limita a contarlas: publica, PARA CADA `B` DEL
UNIVERSO, si declara diferenciador, si tiene lesion exacta y si tiene nodo muerto.
El cotejo lo hace `scripts/loop/cotejar_clon_declarado.py` y su salida se pega en
el reporte con lo que salga.

EL CENSO DE LAS `B` NO SE INTERPRETA NI SE ADJUDICA: SOLO SE CUENTA Y SE PUBLICA.
El encargo lo pide con esas palabras y da su motivo, medido en el acta 187 `5.6`:
las tres `B` conocidas (338, 226, 603) dan NADA en las cuatro comprobaciones
mecanicas y aun asi son `B`. **Si la vara resulta ciega a la clase `B` entera, eso
es un hallazgo del fundador y no de este fichero.**

LO QUE ESTA RELECTURA NO ES, Y SE DICE PARA NO VENDERLA DE MAS: **NO es una
relectura de juicio.** No vuelve a decidir la clase de ningun par. **Es la
relectura MECANICA del tramo con la vara**, que es la unica que se puede correr
sobre 60 pares sin inventarse nada. Lo que encuentre se nombra; **lo que la vara
no vea, esta salida NO lo afirma.**

USO:
  python scripts/loop/vuelta187_tarea3_relectura_al_doble.py
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
SELLO = os.path.join(LOOP, "SELLO_APERTURA_AUDITOR_V188.json")
CIEGA = os.path.join(LOOP, "_auditor_v188_ciega_blind.txt")
ANTERIOR = os.path.join(LOOP, "_auditor_v187_ciega_blind.txt")
EXCLUSION = os.path.join(LOOP, "_auditor_v188_exclusion.txt")
NL = chr(10)
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 187"
PATRON_PUESTO = re.compile(r"^puesto_intra:\s*(\d+)\s*$")
# LAS CUATRO DISCREPANCIAS QUE EL ACTA 187 NOMBRA, Y QUE EL AUDITOR PIERDE LAS
# CUATRO A FAVOR DEL ARCHIVO. Van en una constante con nombre para que se vea que
# son un dato del acta y del encargo, y no del juicio de aqui.
LAS_CUATRO = [226, 603, 1612, 2448]


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
    w("VUELTA 187, TAREA 3: LA RELECTURA AL DOBLE DEL")
    w("TRAMO DE LA CIEGA DEL ACTA 187, encargada por AUDITOR.md 1.2 porque las")
    w("CUATRO discrepancias del auditor salieron FUERA del discutible de clase")
    w("marcado, y TRES fuera incluso de los dudosos que el auditor marco de antemano")
    w("=" * 78)
    w("")

    w("A) EL CONTRASTE CON EL ACTA, QUE NO ES CORRECCION SINO COTEJO. EL")
    w("   ENCARGO YA NOMBRA LA FUENTE BUENA, Y AQUI SE MIDE QUE LISTA EL ACTA.")
    t_acta = io.open(ACTA, encoding="utf-8").read()
    ini9, fin9, cuerpo9 = seccion_del_acta(t_acta, CABECERA_ACTA, 4)
    if ini9 is None:
        w("   el acta 187 NO tiene seccion 4. Se dice y no se inventa.")
        puestos_sec9 = []
    else:
        w("   seccion 4 del acta 187: lineas %d a %d (%d lineas)"
          % (ini9, fin9, len(cuerpo9)))
        w("   su cabecera: %s" % cuerpo9[0].strip()[:100])
        puestos_sec9 = [int(x) for x in
                        re.findall(r"puesto_intra:\s*(\d+)", NL.join(cuerpo9))]
    w("   CIFRA puestos que la seccion 4 del acta 187 lista: %d" % len(puestos_sec9))
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
    w("   docs/loop/SELLO_APERTURA_AUDITOR_V188.json -> %d bytes en disco y %d "
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

    w("F) LOS TRES SOLAPES, MEDIDOS Y NO SUPUESTOS")
    w("   (el encargo exige solape 0 por TRES lados: contra el tramo, contra la")
    w("    ciega inmediatamente anterior, y contra los 293 puestos de la exclusion.")
    w("    El tercero la vuelta 186 no lo media; aqui si, y se publica lo que salga)")
    w("   F.1 SOLAPE ENTRE EL TRAMO Y SUS VECINOS: %d" % len(set(dobles) & set(tramo)))
    if os.path.exists(ANTERIOR):
        tramo_ant = puestos_de_la_ciega(io.open(ANTERIOR, encoding="utf-8").read())
        w("   F.2 ciega anterior: docs/loop/_auditor_v187_ciega_blind.txt -> %d puestos"
          % len(tramo_ant))
        w("       SOLAPE del tramo de hoy con el anterior: %d"
          % len(set(tramo) & set(tramo_ant)))
        w("       SOLAPE del UNIVERSO ENTERO de hoy con el anterior: %d"
          % len(set(universo) & set(tramo_ant)))
    else:
        w("   F.2 LA CIEGA ANTERIOR NO ESTA EN DISCO. No se afirma ningun solape.")
    if os.path.exists(EXCLUSION):
        t_exc = io.open(EXCLUSION, encoding="utf-8", errors="replace").read()
        exc = sorted({int(x) for x in re.findall(r"\d+", t_exc)})
        w("   F.3 exclusion: docs/loop/_auditor_v188_exclusion.txt -> disco %d bytes"
          % os.path.getsize(EXCLUSION))
        w("       CIFRA puestos distintos que la exclusion lista: %d" % len(exc))
        w("       SOLAPE del TRAMO con la exclusion: %d" % len(set(tramo) & set(exc)))
        cruce = sorted(set(universo) & set(exc))
        w("       SOLAPE del UNIVERSO ENTERO con la exclusion: %d" % len(cruce))
        w("       (el criterio del sello habla de 293 puestos excluidos; la cifra de")
        w("        arriba esta CONTADA del fichero y no copiada del criterio)")
        if cruce:
            w("       LOS QUE CRUZAN, NOMBRADOS UNO A UNO EN VEZ DE DEJARLOS EN UNA")
            w("       CIFRA, Y CON EL PUESTO DEL TRAMO QUE LOS TRAJO:")
            for x in cruce:
                de_donde = [q for q in tramo if x in vecinos([q], maximo)]
                w("          puesto %-6d es %s | vecino determinista de %s"
                  % (x, "DEL TRAMO" if x in tramo else "VECINO",
                     ", ".join(str(q) for q in de_donde) or "(no localizado)"))
            w("       DECLARADO SIN ARREGLARLO: el encargo pide solape 0 con la")
            w("       exclusion. EL TRAMO LO CUMPLE (%d). Los que cruzan son"
              % len(set(tramo) & set(exc)))
            w("       VECINOS DETERMINISTAS, y vecinos() es una funcion IMPORTADA y")
            w("       CONGELADA: cambiarla aqui para que la cifra saliera cero seria")
            w("       mover la vara a mitad de la medicion, que es justo lo que la")
            w("       P.5.1 prohibe. Se publica la cifra y se nombran los puestos.")
    else:
        w("   F.3 LA EXCLUSION NO ESTA EN DISCO. No se afirma ningun solape.")
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
    w("   (el acta 187 las nombra: los puestos 226, 603, 1612 y 2448, que el")
    w("    auditor pierde LOS CUATRO a favor del archivo. Aqui NO se")
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

    w("I.1) EL CENSO DE LAS `B` DEL UNIVERSO RELEIDO, UNA POR UNA. SOLO SE CUENTA")
    w("     Y SE PUBLICA: NO SE INTERPRETA Y NO SE ADJUDICA.")
    w("   (el encargo lo pide con esas palabras y da su motivo, medido en el acta")
    w("    187 `5.6`: las TRES `B` conocidas (338, 226, 603) dan NADA en las cuatro")
    w("    comprobaciones mecanicas y aun asi son `B`. Si la vara resulta ciega a la")
    w("    clase `B` entera, eso es un hallazgo del fundador y no de este fichero)")
    b_universo = [p for p in universo
                  if porpuesto.get(p) and porpuesto[p].get("clase") == "B"]
    w("   CIFRA clases `B` en el universo releido: %d de %d"
      % (len(b_universo), len(universo)))
    w("   LOS PUESTOS `B` DEL UNIVERSO: %s"
      % (", ".join(str(x) for x in b_universo) or "(ninguno)"))
    w("")
    w("   PARA CADA `B` DEL UNIVERSO, SUS TRES COMPROBACIONES MECANICAS:")
    w("   %-7s %-9s %-9s %-11s  %s"
      % ("puesto", "declara", "lesion", "nodo muerto", "nodos"))
    n_b_declaran = n_b_lesion = n_b_muerto = n_b_nada = 0
    for p in b_universo:
        f = porpuesto[p]
        r = T3.analiza(f, porid)
        muerto = not ((f.get("nodo_a") in porid) and (f.get("nodo_b") in porid))
        if r["declara"]:
            n_b_declaran += 1
        if r["lesion"]:
            n_b_lesion += 1
        if muerto:
            n_b_muerto += 1
        if not r["declara"] and not r["lesion"] and not muerto:
            n_b_nada += 1
        w("   %-7d %-9s %-9s %-11s  %s contra %s%s"
          % (p, "SI" if r["declara"] else "NADA",
             "SI" if r["lesion"] else "NADA", "SI" if muerto else "NADA",
             f.get("nodo_a"), f.get("nodo_b"),
             "   <-- DEL TRAMO" if p in tramo else ""))
    w("")
    w("   LAS CIFRAS DEL CENSO DE `B`, CONTADAS DE LA TABLA DE ARRIBA:")
    w("      CIFRA `B` del universo: %d" % len(b_universo))
    w("      CIFRA `B` que DECLARAN diferenciador: %d" % n_b_declaran)
    w("      CIFRA `B` con LESION EXACTA: %d" % n_b_lesion)
    w("      CIFRA `B` con algun NODO MUERTO: %d" % n_b_muerto)
    w("      CIFRA `B` que dan NADA en las tres: %d de %d"
      % (n_b_nada, len(b_universo)))
    b_archivo = [f for f in filas if f.get("clase") == "B"]
    w("      CIFRA clases `B` en TODO el archivo, contadas del archivo y no del")
    w("      encargo: %d de %d filas" % (len(b_archivo), len(filas)))
    w("      de las cuatro discrepancias, cuales son clase `B`: %s"
      % (", ".join(str(p) for p in LAS_CUATRO
                   if porpuesto.get(p) and porpuesto[p].get("clase") == "B")
         or "(ninguna)"))
    w("   Y AQUI SE PARA. Esta salida NO dice que la vara sea ciega a la clase `B`,")
    w("   NO adjudica ninguna de estas `B` y NO propone nada: publica la cuenta y")
    w("   las tres columnas, que es exactamente lo que el encargo pide.")
    w("")

    w("J) LO QUE ESTA RELECTURA SOSTIENE, Y NI UNA PALABRA MAS")
    w("   1. El tramo se leyo de la ciega SELLADA del auditor, cotejada por")
    w("      sha256 contra su propio sello ANTES de leer un solo puesto, y NO del")
    w("      acta, que no lo lista. El sello se llama V188 porque la casa nombra")
    w("      el sello del acta N como V(N+1) y esta es el acta 187. El V186 NO")
    w("      EXISTE y no se fabrica. La ruta viene del encargo, no de deducirla")
    w("      del numero de vuelta.")
    w("   2. El tramo se releyo AL DOBLE: %d puestos contra los %d del tramo."
      % (len(universo), len(tramo)))
    w("   3. De los %d, %d declaran un diferenciador y %d lo tienen HOY movido al"
      % (len(universo), n_declaran, n_lesion))
    w("      otro nodo.")
    w("   4. Puestos con algun nodo muerto en el grafo de hoy: %d." % n_muertos)
    w("   5. LOS TRES SOLAPES VAN MEDIDOS Y NO SUPUESTOS, y el tercero (contra los")
    w("      puestos de la exclusion) la vuelta 186 no lo media.")
    w("   6. ESTA RELECTURA NO VUELVE A DECIDIR NINGUNA CLASE. Es la relectura")
    w("      MECANICA del tramo con la vara, no una lectura de juicio. Lo que la")
    w("      vara no ve, esta salida NO lo afirma.")
    w("   7. NINGUN VEREDICTO SE MUEVE EN ESTA TAREA. La TAREA 2 de esta misma")
    w("      vuelta SI movio uno, el 2.464, y lo dice en su sitio; aqui el archivo")
    w("      se abre para leer y se cierra.")
    w("   8. EL CENSO DE LAS `B` SE PUBLICA Y NO SE INTERPRETA. El encargo lo pide")
    w("      con sus tres columnas; aqui se cuentan y ahi se para. Si la vara")
    w("      resulta ciega a la clase `B` entera, eso es un hallazgo del fundador.")
    w("")
    w("FIN")

    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V187_T3_RELECTURA_AL_DOBLE.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
