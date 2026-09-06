# -*- coding: utf-8 -*-
r"""vuelta191_tarea2b_cotejo.py . EL COTEJO DE LA RELECTURA AL DOBLE DEL TRAMO
DEL 3182, DESPUES DE ABRIR EL DESTAPE Y NO ANTES.

POR QUE ES UN FICHERO Y NO UNAS ORDENES SUELTAS. El cotejo de la vuelta 190
(`docs/loop/SALIDA_V190_T4_COTEJO.txt`) existe en disco pero **no hay ningun
instrumento commiteado que lo produzca**: `grep -rl "EL COTEJO, DESPUES DE ABRIR
EL DESTAPE" scripts/loop/` da CERO ficheros, medido en esta vuelta. Una tabla que
solo existe en su salida no se puede volver a correr, y `EJECUTOR.md` 1 dice que
**la tabla se imprime, no se teclea**. Aqui queda el instrumento.

QUE HACE, Y NADA MAS: lee mis clases (que ya estan commiteadas), lee el destape,
y **cuenta**. No decide ninguna clase, no toca
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y no escribe ninguna fila.

EL ORDEN NO SE PROMETE, SE LEE DE GIT: este fichero busca en `git log` los
commits del aislamiento y de las clases y publica sus hashes con su asunto. Si
alguno no aparece o aparece mas de una vez, **CAE EN ROJO**: un orden que no se
puede leer no se afirma.

USO:
  python scripts/loop/vuelta191_tarea2b_cotejo.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
VUELTA = int(re.search(r"vuelta(\d+)_",
                       os.path.basename(os.path.abspath(__file__))).group(1))

CIEGA = "docs/loop/SALIDA_V%d_T2_CIEGA.txt" % VUELTA
CLASES = "docs/loop/SALIDA_V%d_T2_MIS_CLASES.txt" % VUELTA
DESTAPE = "docs/loop/SALIDA_V%d_T2_DESTAPE.txt" % VUELTA
SALIDA = "docs/loop/SALIDA_V%d_T2_COTEJO.txt" % VUELTA

AGUJA_AISLAMIENTO = "VUELTA %d, TAREA 2, PASO 1" % VUELTA
AGUJA_CLASES = "VUELTA %d, TAREA 2, PASO 2" % VUELTA

# LA FILA DE MI TABLA DE CLASES: `  puesto | clase | motivo`.
PAT_MI_FILA = re.compile(r"^\s*(\d+)\s*\|\s*([ABCD])\s*\|\s*(.*)$")
PAT_DUDOSOS = re.compile(r"^\s{3}((?:\d+,\s*)+\d+)\s*$")


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def medir(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    datos = io.open(p, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    texto = lf.decode("utf-8", errors="replace")
    return dict(disco=len(datos), lf=len(lf),
                lineas_count=texto.count(NL), lineas_split=len(texto.split(NL)),
                sha=hashlib.sha256(lf).hexdigest(), texto=texto)


def mis_clases(texto):
    """MI TABLA, LEIDA DE MI FICHERO Y NO TECLEADA. Devuelve (dict, dudosos)."""
    clases = {}
    dudosos = set()
    en_dudosos = False
    for linea in texto.split(NL):
        if "MIS DUDOSOS" in linea:
            en_dudosos = True
            continue
        if en_dudosos:
            m = PAT_DUDOSOS.match(linea)
            if m:
                dudosos |= set(int(x) for x in re.findall(r"\d+", m.group(1)))
                continue
            if linea.strip():
                en_dudosos = False
        m = PAT_MI_FILA.match(linea)
        if m:
            clases[int(m.group(1))] = (m.group(2), m.group(3).strip())
    return clases, dudosos


def del_destape(texto):
    """LAS CLASES DEL ARCHIVO, LEIDAS DEL DESTAPE. Devuelve dict."""
    salida = {}
    puesto = None
    clase = None
    for linea in texto.split(NL):
        m = re.match(r"^puesto_intra:\s*(\d+)", linea)
        if m:
            puesto = int(m.group(1))
            clase = None
            continue
        m = re.match(r"^clase:\s*([ABCD])", linea)
        if m and puesto is not None:
            clase = m.group(1)
            salida[puesto] = clase
            continue
        m = re.match(r"^razon:\s*(.*)$", linea)
        if m and puesto is not None and clase is not None:
            salida[puesto] = (clase, m.group(1).strip())
    return dict((k, v if isinstance(v, tuple) else (v, ""))
                for k, v in salida.items())


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    rojos = []
    w("=" * 78)
    w("VUELTA %d, TAREA 2: EL COTEJO, DESPUES DE ABRIR EL DESTAPE" % VUELTA)
    w("=" * 78)
    w("")

    w("A) LOS TRES FICHEROS, MEDIDOS POR LAS DOS CONVENCIONES DE BYTES Y POR LAS")
    w("   DOS DE LINEAS, QUE ES LA TAREA 3 DE ESTA MISMA VUELTA")
    med = {}
    for rel in (CIEGA, CLASES, DESTAPE):
        m = medir(rel)
        med[rel] = m
        if m is None:
            w("   %-46s NO EXISTE" % rel)
            rojos.append("no existe %s" % rel)
            continue
        w("   %-46s disco %6d | LF %6d | lineas count(NL) %4d | split %4d | "
          "sha256 LF %s"
          % (rel, m["disco"], m["lf"], m["lineas_count"], m["lineas_split"],
             m["sha"][:16]))
    if rojos:
        w("ROJO: %s" % "; ".join(rojos))
        print(NL.join(L))
        return 1
    w("")

    w("B) EL ORDEN, LEIDO DE GIT Y NO PROMETIDO")
    c, log = git(["log", "--format=%h%x09%s", "-40"])
    for etiqueta, aguja in (("aislamiento (paso 1)", AGUJA_AISLAMIENTO),
                            ("mis clases (paso 2)", AGUJA_CLASES)):
        hits = [l for l in log.splitlines() if aguja in l]
        w("   %-22s -> %d commit(s)" % (etiqueta, len(hits)))
        for h in hits:
            w("      %s" % h[:140])
        if len(hits) != 1:
            rojos.append("%s aparece %d veces en los 40 ultimos commits"
                         % (etiqueta, len(hits)))
    w("   Y EL FICHERO DE CLASES ESTA EN GIT SIN CAMBIOS DESDE SU COMMIT:")
    c, st = git(["status", "--porcelain", "--", CLASES])
    w("      git status de %s: %r" % (CLASES, st.strip() or "(limpio)"))
    if st.strip():
        rojos.append("el fichero de clases tiene cambios sin commitear")
    if rojos:
        w("")
        w("ROJO, %d motivo(s), y el cotejo NO se publica:" % len(rojos))
        for r in rojos:
            w("   " + r)
        print(NL.join(L))
        return 1
    w("")

    mias, dudosos = mis_clases(med[CLASES]["texto"])
    archivo = del_destape(med[DESTAPE]["texto"])
    w("C) LOS DOS REPARTOS, CONTADOS DE SUS FICHEROS")
    w("   CIFRA puestos en mis clases: %d" % len(mias))
    w("   CIFRA puestos en el destape: %d" % len(archivo))
    w("   CIFRA dudosos mios, leidos de mi propia cabecera: %d" % len(dudosos))
    w("      %s" % ", ".join(str(x) for x in sorted(dudosos)))
    if set(mias) != set(archivo):
        w("   ROJO: los dos ficheros no traen los mismos puestos.")
        print(NL.join(L))
        return 1
    for etiqueta, d in (("MIO", dict((k, v[0]) for k, v in mias.items())),
                        ("DEL ARCHIVO", dict((k, v[0]) for k, v in archivo.items()))):
        cuenta = {}
        for v in d.values():
            cuenta[v] = cuenta.get(v, 0) + 1
        w("   REPARTO %-12s %s"
          % (etiqueta, " ".join("%s %d" % (k, cuenta[k]) for k in sorted(cuenta))))
    w("")

    w("D) EL COTEJO, PUESTO A PUESTO")
    w("   puesto | mia | archivo | veredicto | dudoso mio")
    coinciden = []
    discrepan = []
    for p in sorted(mias):
        mia = mias[p][0]
        arc = archivo[p][0]
        ok = mia == arc
        (coinciden if ok else discrepan).append(p)
        w("   %6d |  %s  |    %s    | %-9s | %s"
          % (p, mia, arc, "COINCIDE" if ok else "DISCREPA",
             "SI" if p in dudosos else "no"))
    w("")

    w("E) LAS CIFRAS, CONTADAS Y NO TECLEADAS")
    dentro = [p for p in discrepan if p in dudosos]
    fuera = [p for p in discrepan if p not in dudosos]
    w("   CIFRA releidos: %d" % len(mias))
    w("   CIFRA COINCIDEN: %d" % len(coinciden))
    w("   CIFRA DISCREPAN: %d" % len(discrepan))
    w("   CIFRA discrepancias DENTRO de mis dudosos: %d (%s)"
      % (len(dentro), ", ".join(str(x) for x in dentro) or "ninguna"))
    w("   CIFRA discrepancias FUERA de mis dudosos: %d (%s)"
      % (len(fuera), ", ".join(str(x) for x in fuera) or "ninguna"))
    w("   CIFRA dudosos que SI coincidieron: %d"
      % len([p for p in coinciden if p in dudosos]))
    w("")

    w("F) LAS DISCREPANCIAS, UNA A UNA, CON LA RAZON DEL ARCHIVO AL LADO")
    for p in discrepan:
        w("   PUESTO %d  (dudoso mio: %s)" % (p, "SI" if p in dudosos else "NO"))
        w("      mi clase %s, mi motivo: %s" % (mias[p][0], mias[p][1][:150]))
        w("      del archivo %s, su razon: %s" % (archivo[p][0], archivo[p][1][:200]))
    if not discrepan:
        w("   (ninguna)")
    w("")

    w("G) LA MARCA `DISCUTIBLE MARCADO` EN LAS RAZONES DE ESTOS 30, CONTADA AQUI")
    w("   (es la vara de la TAREA 5 aplicada al tramo de la TAREA 2, y se cuenta")
    w("    del destape, que es el fichero que trae las razones)")
    con_marca = [p for p in sorted(archivo) if "DISCUTIBLE MARCADO" in archivo[p][1]]
    w("   CIFRA de los 30 con la marca: %d (%s)"
      % (len(con_marca), ", ".join(str(x) for x in con_marca) or "ninguno"))
    w("   CIFRA de los que me tumbaron que llevan la marca: %d de %d"
      % (len([p for p in discrepan if p in con_marca]), len(discrepan)))
    w("")

    w("H) EL ARCHIVO NO SE TOCA, Y SE MIDE PARA DECIRLO")
    a = medir("docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
    w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> disco %d | LF %d | sha256 LF %s"
      % (a["disco"], a["lf"], a["sha"]))
    c, ns = git(["diff", "--numstat", "--", "dataset/"])
    w("   CIFRA filas de `git diff --numstat -- dataset/`: %d"
      % len([l for l in ns.splitlines() if l.strip()]))
    w("")
    w("FIN DEL COTEJO")

    texto = NL.join(L) + NL
    io.open(os.path.join(RAIZ, SALIDA.replace("/", os.sep)), "w",
            encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)" % (SALIDA, len(texto.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
