# -*- coding: utf-8 -*-
r"""vuelta188_tarea5a_relectura_al_doble.py . LA RELECTURA AL DOBLE DEL TRAMO DE
LA CIEGA DEL ACTA 188.

QUIEN LA ENCARGA Y POR QUE. `AUDITOR.md` 1.2. La discrepancia del auditor (**el
puesto 1202**) cayo **FUERA del discutible de clase marcado**: el reporte de la
187 marco el **2464**. **Fue UNA sola y estaba en sus propios dudosos, y el
credito baja igual porque la letra no distingue.**

EL COTEJO DEL `sha256` VA ANTES DE LEER UN SOLO PUESTO, contra
`docs/loop/SELLO_APERTURA_AUDITOR_V189.json`, y **la cifra del encargo NO se
copia: se computa y se compara**. Si no calza, PARADA y no se lee nada.

QUE ES "AL DOBLE": los **30 puestos** de `docs/loop/_auditor_v189_ciega_blind.txt`
mas **30 vecinos deterministas**, con `vecinos()` **IMPORTADA** de
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y **no copiada**.
**Sesenta puestos releidos, que es el doble exacto.**

Y AQUI VA EL REMEDIO DEL `D.2` DEL REPORTE DE LA 187, ADJUDICADO A FAVOR Y AUN ASI
ARREGLADO (acta 188, `5.2` y `7.3`): **el solape se le exige AL UNIVERSO**, no al
tramo, porque la exclusion existe para que nadie relea lo ya leido y **los 60 se
leen todos**. Se arregla **por parametro y de forma aditiva**: a `vecinos()` se le
pasa el conjunto `evitar` con los **351** puestos de
`docs/loop/_auditor_v189_exclusion.txt`, y **el cero sale por construccion y no por
suerte**. Su regla no cambia: cambia lo que se le pasa.

NINGUNA CLASE SE VUELVE A DECIDIR. **Es la relectura MECANICA del universo con la
vara de esta casa**, no una lectura de juicio. Lo que la vara no vea, esta salida
NO lo afirma.

USO:
  python scripts/loop/vuelta188_tarea5a_relectura_al_doble.py
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
NL = chr(10)
VUELTA = 188
SELLO_N = "V%d" % (VUELTA + 1)
CIEGA = "docs/loop/_auditor_v%d_ciega_blind.txt" % (VUELTA + 1)
CIEGA_ANTERIOR = "docs/loop/_auditor_v%d_ciega_blind.txt" % VUELTA
EXCLUSION = "docs/loop/_auditor_v%d_exclusion.txt" % (VUELTA + 1)
SELLO = "docs/loop/SELLO_APERTURA_AUDITOR_%s.json" % SELLO_N
PUESTO_DEL_AUDITOR = 1202

PAT_PUESTO = re.compile(r"puesto_intra[^0-9]{0,12}(\d+)")

# LA NOTA DE NOMINA: EVIDENCIA DE FAMILIA Y NO DEL PAR. El acta 188, seccion 4,
# dice que la razon del archivo en el puesto 1202 cierra con una NOTA DE NOMINA
# que cita el banco `9.20` y `9.10` y habla de un RACIMO y de CUATRO A contra
# hermanos. Aqui SOLO SE CUENTA Y SE PUBLICA: no se interpreta y no se adjudica.
# Si resulta que la salida ciega no lleva la carta que decide una parte de los
# pares, ESO ES UN HALLAZGO DEL FUNDADOR Y NO MIO.
MARCAS_DE_FAMILIA = ("NOTA DE NOMINA", "NOTA DE LA NOMINA", "racimo", "RACIMO",
                     "cumulo", "CUMULO", "hermanos", "HERMANOS",
                     "contra hermanos", "9.20")


def sha_de(ruta):
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    datos = io.open(p, "rb").read()
    lf = datos.replace(chr(13).encode() + chr(10).encode(), chr(10).encode())
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest())


def puestos_de(ruta, patron=PAT_PUESTO):
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    if not os.path.isfile(p):
        return []
    t = io.open(p, encoding="utf-8", errors="replace").read()
    return sorted(set(int(x) for x in patron.findall(t)))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 5.a: LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA %d"
      % (VUELTA, VUELTA))
    w("encargada por AUDITOR.md 1.2, porque la discrepancia del auditor (el puesto")
    w("%d) cayo FUERA del discutible de clase marcado (el reporte marco el 2464)"
      % PUESTO_DEL_AUDITOR)
    w("=" * 78)
    w("")

    w("A) EL COTEJO DEL sha256, ANTES DE LEER UN SOLO PUESTO")
    w("   (el encargo publica 41098 bytes y sha256 LF 4dbbedc0ac89951e. AQUI NO SE")
    w("    COPIA NINGUNA DE LAS DOS: se computan y se comparan)")
    p_sello = os.path.join(RAIZ, SELLO.replace("/", os.sep))
    if not os.path.isfile(p_sello):
        w("   PARADA: %s NO EXISTE." % SELLO)
        print(NL.join(L))
        return 1
    sello = json.load(io.open(p_sello, encoding="utf-8"))
    ds, ls, ss = sha_de(SELLO)
    w("   %s -> disco %d bytes | LF %d bytes" % (SELLO, ds, ls))
    calza = True
    for clave_r, clave_b, clave_s in (("ciega", "bytes_ciega", "sha256_ciega"),
                                      ("destape", "bytes_destape", "sha256_destape")):
        ruta = sello[clave_r]
        m = sha_de(ruta)
        if m is None:
            w("   PARADA: %s NO EXISTE." % ruta)
            print(NL.join(L))
            return 1
        d, l, s = m
        ok_b = (sello[clave_b] == d)
        ok_s = (sello[clave_s] == s)
        w("   %-8s %s" % (clave_r, ruta))
        w("      bytes: el sello dice %d | medido en disco %d -> %s"
          % (sello[clave_b], d, "CALZA" if ok_b else "NO CALZA"))
        w("      sha256: el sello dice %s" % sello[clave_s])
        w("              medido LF     %s" % s)
        w("              -> %s" % ("CALZA" if ok_s else "NO CALZA"))
        calza = calza and ok_b and ok_s
    if not calza:
        w("   PARADA: el sello no calza con el disco. NO SE LEE NI UN PUESTO.")
        print(NL.join(L))
        return 1
    w("   LOS DOS CALZAN. Se puede leer.")
    w("")

    w("B) EL TRAMO Y SU DOBLE, CON `vecinos()` IMPORTADA Y NO COPIADA")
    tramo = puestos_de(CIEGA)
    w("   %s -> %d puestos distintos" % (CIEGA, len(tramo)))
    w("   LOS PUESTOS DEL TRAMO: %s" % ", ".join(str(x) for x in tramo))
    filas = [json.loads(l) for l in io.open(T3.VEREDICTOS, encoding="utf-8")
             if l.strip()]
    porpuesto = {f.get("puesto_intra"): f for f in filas}
    maximo = max(porpuesto)
    grafo = json.load(io.open(T3.GRAFO, encoding="utf-8"))
    porid = T3.nodos_por_id(grafo)
    w("   veredictos: %d filas | maximo puesto %d | grafo: %d nodos"
      % (len(filas), maximo, len(porid)))
    excl = puestos_de(EXCLUSION, re.compile(r"(\d+)"))
    de, le, se = sha_de(EXCLUSION)
    w("   %s -> disco %d bytes | LF %d bytes | %d puestos distintos"
      % (EXCLUSION, de, le, len(excl)))
    w("   el encargo dice 351 -> %s" % ("CALZA" if len(excl) == 351 else "NO CALZA"))
    w("")
    w("   EL REMEDIO DEL `D.2`, QUE ES ADITIVO Y NO TUERCE LA VARA: a `vecinos()`")
    w("   se le pasa el conjunto `evitar` con los %d de la exclusion, y el cero"
      % len(excl))
    w("   sale POR CONSTRUCCION. Su regla no cambia: cambia lo que se le pasa.")
    sin_evitar = vecinos(tramo, maximo)
    dobles = vecinos(tramo, maximo, evitar=set(excl))
    w("      SIN `evitar` (la conducta de la 187): %d vecinos, y su solape con la"
      % len(sin_evitar))
    w("      exclusion es %d: %s"
      % (len(set(sin_evitar) & set(excl)),
         ", ".join(str(x) for x in sorted(set(sin_evitar) & set(excl))) or "ninguno"))
    w("      CON `evitar`: %d vecinos" % len(dobles))
    w("   LOS VECINOS: %s" % ", ".join(str(x) for x in dobles))
    universo = sorted(set(tramo) | set(dobles))
    w("   CIFRA puestos que se releen EN TOTAL: %d" % len(universo))
    w("   ES EL DOBLE EXACTO DEL TRAMO: %s"
      % ("SI" if len(universo) == 2 * len(tramo) else
         "NO, son %d y el doble seria %d" % (len(universo), 2 * len(tramo))))
    w("")

    w("C) LOS TRES SOLAPES DEL UNIVERSO, QUE ES LO QUE EL ACTA 188 EXIGE")
    ciega_ant = puestos_de(CIEGA_ANTERIOR)
    solapes = [
        ("el UNIVERSO contra el TRAMO (los vecinos no repiten el tramo)",
         sorted(set(dobles) & set(tramo))),
        ("el UNIVERSO contra %s" % CIEGA_ANTERIOR,
         sorted(set(universo) & set(ciega_ant))),
        ("el UNIVERSO contra la EXCLUSION de %d puestos" % len(excl),
         sorted(set(universo) & set(excl))),
    ]
    for etiqueta, s in solapes:
        w("   SOLAPE %s: %d" % (etiqueta, len(s)))
        if s:
            w("      LOS QUE CRUZAN, NOMBRADOS: %s"
              % ", ".join(str(x) for x in s))
            w("      NO SE ARREGLA A LA FUERZA: se declara.")
    w("   CIFRA solapes que NO dan 0: %d" % len([1 for _e, s in solapes if s]))
    w("")

    w("D) LA RELECTURA MECANICA, PUESTO A PUESTO")
    w("   (la maquina se IMPORTA de vuelta182_tarea3_diferenciador_movido.py, y")
    w("    NINGUNA CLASE SE VUELVE A DECIDIR)")
    w("   %-6s %-6s %-8s %-8s %-7s %-6s %-8s %s"
      % ("puesto", "clase", "declara", "lesion", "vivos", "cober", "familia",
         "nodos"))
    n_declaran = n_lesion = n_muertos = n_familia = 0
    lesionados = []
    con_familia = []
    por_clase = {}
    for p in universo:
        f = porpuesto.get(p)
        if f is None:
            w("   %-6d NO ESTA EN EL ARCHIVO" % p)
            continue
        r = T3.analiza(f, porid)
        vivos = (f.get("nodo_a") in porid) and (f.get("nodo_b") in porid)
        razon = str(f.get("razon") or "")
        familia = any(x in razon for x in MARCAS_DE_FAMILIA)
        if not vivos:
            n_muertos += 1
        if r["declara"]:
            n_declaran += 1
        if r["lesion"]:
            n_lesion += 1
            lesionados.append((p, r))
        if familia:
            n_familia += 1
            con_familia.append(p)
        por_clase[f.get("clase")] = por_clase.get(f.get("clase"), 0) + 1
        w("   %-6d %-6s %-8s %-8s %-7s %-6.2f %-8s %s contra %s%s"
          % (p, f.get("clase"), "SI" if r["declara"] else "no",
             "SI" if r["lesion"] else "no", "SI" if vivos else "NO",
             r["cobertura"], "SI" if familia else "no",
             f.get("nodo_a"), f.get("nodo_b"),
             "   <-- DEL TRAMO" if p in tramo else ""))
    w("")

    w("E) LAS CIFRAS DE LA RELECTURA")
    w("   CIFRA puestos releidos: %d" % len(universo))
    w("   CIFRA que declaran diferenciador: %d" % n_declaran)
    w("   CIFRA con LESION EXACTA: %d" % n_lesion)
    w("   CIFRA con algun nodo MUERTO en el grafo de hoy: %d" % n_muertos)
    w("   REPARTO POR CLASE, CONTADO DEL ARCHIVO:")
    for k in sorted(por_clase, key=lambda x: (x is None, str(x))):
        w("      clase %-6s %d" % (repr(k), por_clase[k]))
    w("   LOS LESIONADOS: %s"
      % (", ".join(str(p) for p, _r in lesionados) or "(ninguno)"))
    for p, r in lesionados:
        w("      PUESTO %d: %s" % (p, r["motivo"][:150]))
    w("")

    w("F) LA CIFRA QUE EL ACTA 188 PIDE APARTE, Y QUE SOLO SE CUENTA")
    w("   (evidencia DE FAMILIA y no del par: una razon que se apoya en un racimo,")
    w("    en unos hermanos o en una NOTA DE NOMINA, en vez de en los dos nodos")
    w("    del par. SOLO SE CUENTA Y SE PUBLICA: no se interpreta y no se")
    w("    adjudica, y el motivo esta escrito en el acta 188, seccion 4)")
    w("   LAS MARCAS QUE SE BUSCAN, LITERALES: %s"
      % ", ".join(repr(x) for x in MARCAS_DE_FAMILIA))
    w("   CIFRA de los %d releidos cuya razon lleva evidencia DE FAMILIA: %d"
      % (len(universo), n_familia))
    w("   LOS PUESTOS: %s"
      % (", ".join(str(x) for x in con_familia) or "(ninguno)"))
    w("   Y EL REPARTO ENTRE TRAMO Y VECINOS, PORQUE NO ES LO MISMO:")
    w("      del TRAMO (los 30 que el auditor leyo a ciegas): %d de %d"
      % (len([p for p in con_familia if p in tramo]), len(tramo)))
    w("      de los VECINOS: %d de %d"
      % (len([p for p in con_familia if p not in tramo]), len(dobles)))
    w("   **SI RESULTA QUE LA SALIDA CIEGA NO LLEVA LA CARTA QUE DECIDE UNA PARTE")
    w("   DE LOS PARES, ESO ES UN HALLAZGO DEL FUNDADOR Y NO MIO.**")
    w("")

    w("G) EL PUESTO %d, MIRADO CON LA MISMA VARA Y PUBLICADO APARTE" % PUESTO_DEL_AUDITOR)
    w("   (el auditor lo pierde a favor del archivo. Aqui se dice si esta dentro")
    w("    del universo releido y QUE VE LA VARA EN EL. Lo que la vara no vea, no")
    w("    se afirma)")
    dentro = PUESTO_DEL_AUDITOR in universo
    w("   esta dentro del universo releido: %s" % ("SI" if dentro else "NO"))
    w("   esta en el TRAMO de la ciega: %s"
      % ("SI" if PUESTO_DEL_AUDITOR in tramo else "NO"))
    f = porpuesto.get(PUESTO_DEL_AUDITOR)
    if f is None:
        w("   NO ESTA EN EL ARCHIVO DE VEREDICTOS.")
    else:
        r = T3.analiza(f, porid)
        vivos = (f.get("nodo_a") in porid) and (f.get("nodo_b") in porid)
        razon = str(f.get("razon") or "")
        w("   nodo_a: %s" % f.get("nodo_a"))
        w("   nodo_b: %s" % f.get("nodo_b"))
        w("   clase que el archivo dice HOY: %s" % f.get("clase"))
        w("   dominio: %s | banda: %s" % (f.get("dominio"), f.get("banda_078_080")))
        w("   la vara ve: declara diferenciador %s | LESION EXACTA %s | vivos %s |"
          % ("SI" if r["declara"] else "no", "SI" if r["lesion"] else "no",
             "SI" if vivos else "NO"))
        w("   cobertura %.2f" % r["cobertura"])
        w("   motivo de la vara: %s" % (r["motivo"] or "(ninguno)")[:300])
        w("   su razon lleva evidencia DE FAMILIA: %s"
          % ("SI" if any(x in razon for x in MARCAS_DE_FAMILIA) else "no"))
        w("   LA RAZON DEL ARCHIVO, PEGADA ENTERA Y NO RESUMIDA:")
        for trozo in razon.split(NL):
            w("      | %s" % trozo)
        w("   **NINGUNA CLASE SE MUEVE AQUI.** Esta seccion mide y publica.")
    w("")

    w("H) LO QUE ESTA RELECTURA SOSTIENE, Y NI UNA PALABRA MAS")
    w("   1. El tramo se releyo AL DOBLE: %d puestos contra los %d del tramo."
      % (len(universo), len(tramo)))
    w("   2. Los tres solapes del UNIVERSO se publican, y %d de los tres no dan 0."
      % len([1 for _e, s in solapes if s]))
    w("   3. NINGUNA CLASE SE VUELVE A DECIDIR. Es la relectura MECANICA del")
    w("      universo con la vara de esta casa, no una lectura de juicio.")
    w("   4. La cuenta de evidencia DE FAMILIA se publica y NO se interpreta.")
    w("")
    w("FIN")

    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%d_T5A_RELECTURA_AL_DOBLE.txt" % VUELTA)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
