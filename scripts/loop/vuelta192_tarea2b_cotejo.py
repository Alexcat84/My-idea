# -*- coding: utf-8 -*-
r"""vuelta192_tarea2b_cotejo.py . EL COTEJO DE LA RELECTURA AL DOBLE DE LA VUELTA
192, CORRIDO DESPUES DE QUE LAS CLASES DEL LECTOR ESTEN COMMITEADAS.

EL ORDEN ES LA PRUEBA Y ESTA EN GIT: el aislamiento y sus dos ficheros quedaron
commiteados primero; `docs/loop/SALIDA_V192_T2_MIS_CLASES.txt` fue en SU PROPIO
COMMIT, con sus quince dudosos NOMBRADOS DELANTE; y este fichero es el primero de
la cadena que ABRE el destape.

Y ES EL PRIMER USUARIO DEL FORMATO UNICO. La salida NO la compone este fichero:
la compone `scripts/loop/cotejo_de_ciega.py`, que es la pieza `a` de la TAREA 5 y
tiene nombre estable sin numero de vuelta. **Se escribio antes porque esta tarea
necesitaba un cotejo de todas formas, y usarlo aqui es la prueba de que el
formato sirve para lo que dice servir**, en vez de una plantilla que nadie ha
corrido. La guarda del denominador se le aplica a esta misma salida y su
veredicto se publica.

LO QUE ESTE FICHERO NO HACE: no toca ninguna clase. `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
se abre en LECTURA y su `sha256` se mide al entrar y al salir por las dos
convenciones. Si de la relectura sale una correccion, **se declara y se trae**.

CLON DECLARADO de scripts/loop/vuelta191_tarea2b_cotejo.py, con UNA DIFERENCIA
DECLARADA: aquel componia la tabla el mismo y este la delega en el formato unico.

USO:
  python scripts/loop/vuelta192_tarea2b_cotejo.py
"""
import hashlib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cotejo_de_ciega as FORMATO   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
VUELTA = 192

ARCHIVO = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
CIEGA = "docs/loop/SALIDA_V192_T2_CIEGA.txt"
DESTAPE = "docs/loop/SALIDA_V192_T2_DESTAPE.txt"
MIS_CLASES = "docs/loop/SALIDA_V192_T2_MIS_CLASES.txt"
SALIDA = os.path.join(LOOP, "SALIDA_V192_T2_COTEJO.txt")
MARCA = "DISCUTIBLE MARCADO"

PAT_MIS = re.compile(r"^\s*(\d+)\s*\|\s*([A-D])\s*\|\s*(.*)$")
PAT_DUDOSOS = re.compile(r"MIS DUDOSOS, NOMBRADOS DELANTE[^:]*:\s*(.*?)\n\n",
                         re.S)


def sha_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    d = io.open(p, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return len(d), len(lf), hashlib.sha256(lf).hexdigest()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2: EL COTEJO DE LA RELECTURA AL DOBLE" % VUELTA)
    w("=" * 78)
    w("")

    w("A) EL ARCHIVO, MEDIDO AL ENTRAR Y ABIERTO SOLO EN LECTURA")
    a = sha_de(ARCHIVO)
    w("   %s -> disco %d bytes | LF %d bytes" % (ARCHIVO, a[0], a[1]))
    w("   sha256 LF: %s" % a[2])
    w("")

    w("B) MIS CLASES, LEIDAS DE SU FICHERO COMMITEADO Y NO DE LA MEMORIA")
    t_mis = io.open(os.path.join(RAIZ, MIS_CLASES.replace("/", os.sep)),
                    encoding="utf-8").read().replace(chr(13) + NL, NL)
    m = sha_de(MIS_CLASES)
    w("   %s -> disco %d bytes | LF %d bytes | sha256 LF %s"
      % (MIS_CLASES, m[0], m[1], m[2][:16]))
    mis = {}
    motivos = {}
    for linea in t_mis.split(NL):
        mm = PAT_MIS.match(linea)
        if mm:
            mis[int(mm.group(1))] = mm.group(2)
            motivos[int(mm.group(1))] = mm.group(3).strip()
    w("   CIFRA clases leidas de mi fichero: %d" % len(mis))
    md = PAT_DUDOSOS.search(t_mis)
    dudosos = sorted(set(int(x) for x in re.findall(r"\d+", md.group(1)))) if md else []
    w("   CIFRA dudosos que declare DELANTE: %d" % len(dudosos))
    w("   %s" % ", ".join(str(x) for x in dudosos))
    w("")

    w("C) EL DESTAPE, ABIERTO AHORA Y NO ANTES")
    d = sha_de(DESTAPE)
    w("   %s -> disco %d bytes | LF %d bytes | sha256 LF %s"
      % (DESTAPE, d[0], d[1], d[2][:16]))
    t_dest = io.open(os.path.join(RAIZ, DESTAPE.replace("/", os.sep)),
                     encoding="utf-8").read().replace(chr(13) + NL, NL)
    archivo = {}
    razones = {}
    puesto = None
    for linea in t_dest.split(NL):
        if linea.startswith("puesto_intra: "):
            puesto = int(linea.split(": ", 1)[1])
        elif linea.startswith("clase: ") and puesto is not None:
            archivo[puesto] = linea.split(": ", 1)[1].strip()
        elif linea.startswith("razon: ") and puesto is not None:
            razones[puesto] = linea.split(": ", 1)[1]
    w("   CIFRA clases leidas del destape: %d" % len(archivo))
    w("")

    w("D) LAS DOS LISTAS TIENEN QUE SER EL MISMO CONJUNTO, O NO SE COTEJA")
    w("   puestos en mis clases: %d | en el destape: %d" % (len(mis), len(archivo)))
    if set(mis) != set(archivo):
        w("   PARADA: los conjuntos difieren en %d puesto(s): %s"
          % (len(set(mis) ^ set(archivo)),
             ", ".join(str(x) for x in sorted(set(mis) ^ set(archivo)))))
        print(NL.join(L))
        return 1
    w("   SON EL MISMO CONJUNTO: SI")
    w("")

    w("E) EL COTEJO, COMPUESTO POR EL FORMATO UNICO Y NO POR ESTE FICHERO")
    cabecera = [
        "vuelta: %d, TAREA 2. Relectura AL DOBLE del tramo de la vuelta 191." % VUELTA,
        "lector: el ejecutor de la vuelta %d." % VUELTA,
        "tramo releido: docs/loop/SALIDA_V191_T2_CIEGA.txt (los 30 de la 191).",
        "sujeto: %s (disco %d bytes | LF %d bytes, sha256 LF %s)"
        % (CIEGA, sha_de(CIEGA)[0], sha_de(CIEGA)[1], sha_de(CIEGA)[2][:16]),
        "destape: %s (disco %d bytes | LF %d bytes, sha256 LF %s)"
        % (DESTAPE, d[0], d[1], d[2][:16]),
        "clases del lector: %s (disco %d bytes | LF %d bytes, sha256 LF %s),"
        % (MIS_CLASES, m[0], m[1], m[2][:16]),
        "   escritas y COMMITEADAS en su propio commit ANTES de abrir el destape.",
        "archivo: %s (disco %d bytes | LF %d bytes, sha256 LF %s), abierto SOLO EN"
        % (ARCHIVO, a[0], a[1], a[2][:16]),
        "   LECTURA: esta tarea no escribe ni una fila.",
    ]
    filas = [(p, mis[p], archivo[p], p in dudosos) for p in sorted(mis)]
    ok, informe = FORMATO.escribir_cotejo(SALIDA, cabecera, filas)
    for l in informe:
        w("   " + l)
    if not ok:
        w("   PARADA: el cotejo no pasa la guarda de su propio formato.")
        print(NL.join(L))
        return 1
    w("")

    w("F) LAS CIFRAS, COMPUTADAS DE LAS FILAS DEL COTEJO Y NO TECLEADAS")
    releido = io.open(SALIDA, encoding="utf-8").read()
    fil = FORMATO.filas_del_cotejo(releido)
    r = FORMATO.resumen(fil)
    w("   CIFRA cotejados: %d" % r["total"])
    w("   CIFRA que COINCIDEN: %d" % r["coinciden"])
    w("   CIFRA que DISCREPAN: %d" % r["discrepan"])
    w("   CIFRA discrepancias DENTRO de mis dudosos: %d (%s)"
      % (len(r["disc_dentro"]),
         ", ".join(str(x) for x in r["disc_dentro"]) or "ninguna"))
    w("   CIFRA discrepancias FUERA de mis dudosos: %d (%s)"
      % (len(r["disc_fuera"]),
         ", ".join(str(x) for x in r["disc_fuera"]) or "ninguna"))
    w("   MI REPARTO:        %s"
      % ", ".join("%s %d" % (k, r["reparto_lector"][k])
                  for k in sorted(r["reparto_lector"])))
    w("   REPARTO DEL ARCHIVO: %s"
      % ", ".join("%s %d" % (k, r["reparto_archivo"][k])
                  for k in sorted(r["reparto_archivo"])))
    w("")

    w("G) CADA DISCREPANCIA, CON MI MOTIVO Y LA RAZON DEL ARCHIVO ENFRENTADAS")
    for p, cl, ca, du, ver in fil:
        if ver != "DISCREPA":
            continue
        w("   ---- puesto %d: yo %s, el archivo %s. %s"
          % (p, cl, ca, "DENTRO de mis dudosos" if du else "FUERA de mis dudosos"))
        w("        mi motivo: %s" % motivos.get(p, "(sin motivo)")[:200])
        w("        razon del archivo (primeros 400): %s"
          % razones.get(p, "(sin razon)")[:400])
    w("")

    w("H) LA MARCA %r EN LOS TREINTA, CONTADA DEL DESTAPE" % MARCA)
    con_marca = sorted(p for p in razones if MARCA in razones[p])
    w("   CIFRA de los 30 que la llevan: %d (%s)"
      % (len(con_marca), ", ".join(str(x) for x in con_marca) or "ninguno"))
    disc = set(r["disc_dentro"]) | set(r["disc_fuera"])
    w("   CIFRA de mis %d discrepancias que la llevan: %d (%s)"
      % (len(disc), len(disc & set(con_marca)),
         ", ".join(str(x) for x in sorted(disc & set(con_marca))) or "ninguna"))
    w("   (esto se cuenta y NO se glosa aqui: el encargo prohibe expresamente re")
    w("    medir la marca contra la dificultad en esta vuelta)")
    w("")

    w("I) EL SEGUNDO LECTOR, DICHO CON SUS NUMEROS Y NO SUPUESTO")
    w("   el encargo pide que, SI un tramo vuelve a tumbar a los dos lectores en")
    w("   los mismos puestos, se diga con sus numeros. AQUI SE MIDE:")
    ciega_aud = os.path.join(LOOP, "_auditor_v192_ciega_blind.txt")
    aud = []
    if os.path.exists(ciega_aud):
        t_aud = io.open(ciega_aud, encoding="utf-8", errors="replace").read()
        aud = sorted(set(int(x) for x in
                         re.findall(r"puesto_intra[^0-9]{0,12}(\d+)", t_aud)))
    w("   los 30 de la ciega del auditor del acta 192: %d puestos" % len(aud))
    w("   SOLAPE con los 30 de ESTA tanda: %d" % len(set(aud) & set(mis)))
    w("   O SEA: sobre ESTE tramo hay UN SOLO LECTOR, el ejecutor. El auditor leyo")
    w("   los 30 de la 191, que son OTRO conjunto. NO HAY CRUCE DE DOS LECTORES")
    w("   QUE PUBLICAR AQUI, y decirlo es la respuesta al encargo: la via barata")
    w("   de separar el par dificil del lector distraido NO se puede correr sobre")
    w("   este tramo, porque nadie mas lo ha leido.")
    w("")

    w("J) EL ARCHIVO, REMEDIDO AL SALIR. NO SE ESCRIBIO NI UNA FILA.")
    b = sha_de(ARCHIVO)
    w("   %s -> disco %d bytes | LF %d bytes" % (ARCHIVO, b[0], b[1]))
    w("   sha256 LF: %s" % b[2])
    w("   IDENTICO AL DE LA ENTRADA: %s" % ("SI" if a == b else "NO"))
    w("")
    w("FIN")

    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V192_T2_RECUENTO.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V192_T2_RECUENTO.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
