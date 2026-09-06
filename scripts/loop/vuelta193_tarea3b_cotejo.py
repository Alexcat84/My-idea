# -*- coding: utf-8 -*-
r"""vuelta193_tarea3b_cotejo.py . EL DESTAPE DE LA CIEGA DE LA VUELTA 193,
COTEJADO CONTRA MIS CLASES YA COMMITEADAS.

SE CORRE DESPUES DEL COMMIT DE `docs/loop/SALIDA_V193_T3_MIS_CLASES.txt` Y NO
ANTES. El orden es la prueba y el commit es donde se ve: unas clases escritas
despues del destape no prueban nada.

USA EL FORMATO UNICO, `scripts/loop/cotejo_de_ciega.py`, **ya con el arreglo de
la TAREA 5 puesto**: `en dudosos` se le pasa **COMO TEXTO `si` / `no`**, que es
la forma que `bool(du)` convertia toda en `si` y que le mordio al auditor de la
193. Aqui se pasa a proposito por ese camino, para que el arreglo se ejercite en
su primer uso de verdad y no solo en su mutacion.

LO QUE ESTE FICHERO NO HACE: **no toca ninguna clase**.
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre solo en lectura y su `sha256` LF se
mide al entrar y al salir por las dos convenciones.

USO:
  python scripts/loop/vuelta193_tarea3b_cotejo.py
"""
import hashlib
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cotejo_de_ciega as C   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

ARCHIVO = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
MIS_CLASES = "docs/loop/SALIDA_V193_T3_MIS_CLASES.txt"
DESTAPE = "docs/loop/SALIDA_V193_T3_DESTAPE.txt"
COTEJO = "docs/loop/SALIDA_V193_T3_COTEJO.txt"

PAT_MIA = re.compile(r"^puesto\s+(\d+)\s*->\s*([ABCD])\s*(\[DUDOSO\])?\s*$")
# CON re.M A PROPOSITO: la linea vive EN MEDIO del fichero, y sin la
# bandera `^` solo casa al principio del texto. Sin ella `declarados` sale None y
# la guarda cae en rojo, que es lo que hizo en su primera corrida.
PAT_DUDOSOS = re.compile(r"^CIFRA dudosos:\s*(\d+)", re.M)


def sha_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    datos = io.open(p, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest(),
            hashlib.sha256(datos).hexdigest())


def mis_clases():
    """MIS CLASES Y MIS DUDOSOS, LEIDOS DE MI PROPIO FICHERO. Devuelve
    (dict puesto -> clase, set de dudosos). La marca `[DUDOSO]` va en la MISMA
    linea de la clase a proposito: asi no hace falta cruzar dos listas, y la
    lista de arriba del fichero queda como control de la de abajo."""
    ruta = os.path.join(RAIZ, MIS_CLASES.replace("/", os.sep))
    clases, dudosos = {}, set()
    for linea in io.open(ruta, encoding="utf-8", errors="replace"):
        m = PAT_MIA.match(linea.strip())
        if not m:
            continue
        clases[int(m.group(1))] = m.group(2)
        if m.group(3):
            dudosos.add(int(m.group(1)))
    return clases, dudosos


def clases_del_destape():
    """LAS CLASES DEL ARCHIVO, LEIDAS DEL DESTAPE. Devuelve dict puesto -> clase."""
    ruta = os.path.join(RAIZ, DESTAPE.replace("/", os.sep))
    texto = io.open(ruta, encoding="utf-8", errors="replace").read()
    salida = {}
    puesto = None
    for linea in texto.replace(chr(13) + NL, NL).split(NL):
        m = re.match(r"^puesto_intra:\s*(\d+)", linea.strip())
        if m:
            puesto = int(m.group(1))
            continue
        m2 = re.match(r"^clase:\s*([A-Za-z]+)", linea.strip())
        if m2 and puesto is not None:
            salida[puesto] = m2.group(1).upper()
            puesto = None
    return salida


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("VUELTA 193, TAREA 3.b: EL DESTAPE, COTEJADO CONTRA MIS CLASES COMMITEADAS")
    w("=" * 78)
    w("")

    w("A) EL ARCHIVO, MEDIDO AL ENTRAR Y ABIERTO SOLO EN LECTURA")
    a = sha_de(ARCHIVO)
    w("   %s -> disco %d bytes | LF %d bytes" % (ARCHIVO, a[0], a[1]))
    w("   sha256 LF: %s" % a[2])
    w("   los 16 primeros: %s" % a[2][:16])
    w("")

    w("B) MIS CLASES, LEIDAS DE MI PROPIO FICHERO Y NO TECLEADAS AQUI")
    clases, dudosos = mis_clases()
    s = sha_de(MIS_CLASES)
    w("   %s -> disco %d bytes | sha256 LF %s" % (MIS_CLASES, s[0], s[2][:16]))
    w("   CIFRA clases leidas: %d" % len(clases))
    w("   CIFRA dudosos marcados en la misma linea: %d (%s)"
      % (len(dudosos), ", ".join(str(x) for x in sorted(dudosos))))
    texto_mias = io.open(os.path.join(RAIZ, MIS_CLASES.replace("/", os.sep)),
                         encoding="utf-8", errors="replace").read()
    m = PAT_DUDOSOS.search(texto_mias.replace(chr(13) + NL, NL))
    declarados = int(m.group(1)) if m else None
    w("   CIFRA dudosos DECLARADA en la cabecera del mismo fichero: %s"
      % declarados)
    w("   LAS DOS CALZAN: %s"
      % ("SI" if declarados == len(dudosos) else "NO, y la discrepancia se declara"))
    ok &= (declarados == len(dudosos))
    reparto_mio = {}
    for v in clases.values():
        reparto_mio[v] = reparto_mio.get(v, 0) + 1
    w("   REPARTO MIO: %s"
      % ", ".join("%s %d" % (k, reparto_mio[k]) for k in sorted(reparto_mio)))
    w("")

    w("C) EL DESTAPE, ABIERTO AHORA Y NO ANTES")
    archivo_clases = clases_del_destape()
    d = sha_de(DESTAPE)
    w("   %s -> disco %d bytes | sha256 LF %s" % (DESTAPE, d[0], d[2][:16]))
    w("   CIFRA clases leidas del destape: %d" % len(archivo_clases))
    faltan = sorted(p for p in clases if p not in archivo_clases)
    w("   puestos mios que el destape no trae: %d (%s)"
      % (len(faltan), ", ".join(str(x) for x in faltan) or "ninguno"))
    if faltan:
        w("   PARADA: no se coteja contra un destape incompleto.")
        print(NL.join(L))
        return 1
    w("")

    w("D) EL COTEJO, CON EL FORMATO UNICO Y `en dudosos` PASADO COMO TEXTO")
    w("   (a proposito por el camino que reventaba antes de la TAREA 5)")
    filas = [(p, clases[p], archivo_clases[p],
              "si" if p in dudosos else "no") for p in sorted(clases)]
    cabecera = [
        "=" * 78,
        "COTEJO DE CIEGA. EJECUTOR DE LA VUELTA 193, TAREA 3.",
        "Tramo: los 30 vecinos deterministas del tramo de la 192, aislados en",
        "docs/loop/SALIDA_V193_T3_AISLAMIENTO.txt.",
        "Mis clases: %s, COMMITEADAS ANTES de abrir el destape." % MIS_CLASES,
        "LA VARA: docs/BANCO_DE_TEXTOS.md 9.6.1, LA VARA DE LA RAMA",
        "CONTENIDO-MANDA: LA LINEA O EL PROCEDIMIENTO, citada por numero y",
        "copiada literal dentro del criterio de la ciega (adjudicacion 4.9 del",
        "acta 193). REPITE -> A, CONTINUA -> D.",
        "`en dudosos` va pasado COMO TEXTO `si` / `no`, que es la forma que",
        "`bool(du)` convertia toda en `si` antes de la TAREA 5 de esta vuelta.",
    ]
    destino = os.path.join(RAIZ, COTEJO.replace("/", os.sep))
    ok_esc, informe = C.escribir_cotejo(destino, cabecera, filas)
    for l in informe:
        w("   " + l)
    ok &= ok_esc
    w("")

    w("E) LAS CIFRAS, COMPUTADAS DE LAS FILAS Y NO TECLEADAS")
    releido = io.open(destino, encoding="utf-8").read()
    r = C.resumen(C.filas_del_cotejo(releido))
    for clave in ("total", "coinciden", "discrepan", "dudosos"):
        w("   %-12s %d" % (clave, r[clave]))
    w("   discrepancias DENTRO de mis dudosos: %d (%s)"
      % (len(r["disc_dentro"]),
         ", ".join(str(x) for x in r["disc_dentro"]) or "ninguna"))
    w("   discrepancias FUERA de mis dudosos: %d (%s)"
      % (len(r["disc_fuera"]),
         ", ".join(str(x) for x in r["disc_fuera"]) or "ninguna"))
    w("   REPARTO DEL LECTOR:  %s"
      % ", ".join("%s %d" % (k, r["reparto_lector"][k])
                  for k in sorted(r["reparto_lector"])))
    w("   REPARTO DEL ARCHIVO: %s"
      % ", ".join("%s %d" % (k, r["reparto_archivo"][k])
                  for k in sorted(r["reparto_archivo"])))
    w("")
    w("   LA REGLA QUE CUELGA DE LA CIFRA DE FUERA, DICHA CON SU NUMERO:")
    w("   AUDITOR.md 1.2 baja el credito de la tanda y encarga la relectura al")
    w("   doble POR LO QUE CAE FUERA DEL MARCADO. Con %d fuera, %s"
      % (len(r["disc_fuera"]),
         "esa escalada se dispara y va declarada aqui."
         if r["disc_fuera"] else "no se dispara, y eso tambien se dice."))
    w("")

    w("F) LAS DISCREPANCIAS, UNA POR UNA")
    for p, cl, ca, du, ver in C.filas_del_cotejo(releido):
        if ver == "DISCREPA":
            w("   puesto %-5d yo dije %s, el archivo dice %s, %s de mis dudosos"
              % (p, cl, ca, "DENTRO" if du else "FUERA"))
    w("")

    w("G) EL ARCHIVO, REMEDIDO AL SALIR")
    b = sha_de(ARCHIVO)
    w("   %s -> disco %d bytes | LF %d bytes" % (ARCHIVO, b[0], b[1]))
    w("   sha256 LF: %s" % b[2])
    w("   IDENTICO AL DE LA ENTRADA: %s" % ("SI" if a == b else "NO"))
    ok &= (a == b)
    w("   (no se toco ninguna clase: si de esta relectura sale una correccion,")
    w("    se declara y se trae, y no se escribe ni una fila)")
    w("")

    w("VEREDICTO DEL COTEJO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    salida = os.path.join(LOOP, "SALIDA_V193_T3_COTEJO_SALIDA.txt")
    io.open(salida, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V193_T3_COTEJO_SALIDA.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
