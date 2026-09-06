# -*- coding: utf-8 -*-
r"""vuelta190_tarea4_relectura_al_doble.py . EL SUJETO DE LA RELECTURA AL DOBLE
DEL TRAMO DEL PUESTO 2422, ELEGIDO Y AISLADO ANTES DE QUE NADIE MIRE NADA.

QUIEN LA ENCARGA Y POR QUE. `AUDITOR.md` 1.2. El acta 189 encontro la discrepancia
del puesto **2422 FUERA de sus dudosos marcados**, y esa letra dice que eso baja el
credito de la tanda y obliga a **releer ese tramo AL DOBLE**. La vuelta 189 la
aplazo con razon (era vuelta de bateria y la bateria va sola), **y esa razon ya no
vale hoy**: es una deuda del acta 189 y no se salta dos vueltas seguidas.

QUE ES "EL TRAMO DEL 2422" Y QUE ES "AL DOBLE", DICHO ANTES DE ELEGIR NADA:

  . EL TRAMO es la ciega del acta 189, `docs/loop/_auditor_v189b_ciega_blind.txt`,
    **30 puestos**, y el 2422 esta DENTRO (el bloque G.1 del sello de apertura de
    esta vuelta lo midio antes de tocar nada).
  . AL DOBLE son sus **30 vecinos deterministas**, con `vecinos()` IMPORTADA de
    `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada. Sesenta
    puestos en total, que es el doble exacto.
  . EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO (acta 188, `5.2` y `7.3`): a
    `vecinos()` se le pasa el conjunto `evitar` con TODO lo ya consumido, de modo
    que **el cero sale por construccion y no por suerte**.

Y AQUI LA RELECTURA NO ES MECANICA: **ES UNA CIEGA DE VERDAD**, con
`scripts/loop/aislador_de_ciega.py`, criterio escrito, ciega y destape en ficheros
SEPARADOS, y **las clases escritas ANTES de abrir el destape**. Este fichero
escribe LA CIEGA Y EL DESTAPE y NO LOS LEE: quien los lee es el ejecutor, con las
manos, y escribe sus clases en un tercer fichero antes de destapar.

LO QUE ESTE FICHERO NO HACE, Y ES LA MITAD QUE IMPORTA: **NO TOCA NINGUNA CLASE**.
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre en modo lectura y su `sha256` LF se
mide al entrar y al salir. Si de la relectura sale una correccion, **se declara y
se trae**, y no se escribe sobre el archivo en esta vuelta.

USO:
  python scripts/loop/vuelta190_tarea4_relectura_al_doble.py
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta182_tarea1c_relectura_al_doble import vecinos   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
PY = sys.executable
VUELTA = int(re.search(r"vuelta(\d+)_",
                       os.path.basename(os.path.abspath(__file__))).group(1))

ARCHIVO = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
TRAMO = "docs/loop/_auditor_v189b_ciega_blind.txt"
PUESTO_DEL_ACTA = 2422
# TODO LO YA CONSUMIDO, PARA QUE EL SOLAPE SALGA POR CONSTRUCCION. No es una lista
# tecleada de puestos: son ficheros, y los puestos se cuentan de ellos.
UNIVERSO_CONSUMIDO = [
    "docs/loop/_auditor_v190_exclusion.txt",
    "docs/loop/_auditor_v189b_exclusion.txt",
    "docs/loop/_auditor_v190_ciega_blind.txt",
    "docs/loop/_auditor_v189b_ciega_blind.txt",
]
CIEGA = "docs/loop/SALIDA_V%d_T4_CIEGA.txt" % VUELTA
DESTAPE = "docs/loop/SALIDA_V%d_T4_DESTAPE.txt" % VUELTA
CRITERIO = ("relectura AL DOBLE del tramo del puesto 2422 (AUDITOR.md 1.2): los "
            "30 vecinos deterministas del tramo de la ciega del acta 189, "
            "elegidos con vecinos() sobre el conjunto evitar de todo lo ya "
            "consumido, para que el solape salga por construccion. La 189 aplazo "
            "esta relectura por ser vuelta de bateria y esa razon ya no vale.")

PAT_PUESTO = re.compile(r"puesto_intra[^0-9]{0,12}(\d+)")


def sha_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    datos = io.open(p, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest())


def puestos_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return []
    t = io.open(p, encoding="utf-8", errors="replace").read()
    return sorted(set(int(x) for x in PAT_PUESTO.findall(t)))


def numeros_de(rel):
    """TODOS los enteros de un fichero de exclusion, que es como la casa los
    escribe."""
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return []
    t = io.open(p, encoding="utf-8", errors="replace").read()
    return sorted(set(int(x) for x in re.findall(r"\d+", t)))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 4: EL SUJETO DE LA RELECTURA AL DOBLE DEL TRAMO DEL 2422"
      % VUELTA)
    w("=" * 78)
    w("")

    w("A) EL ARCHIVO, MEDIDO AL ENTRAR Y ABIERTO SOLO EN LECTURA")
    a = sha_de(ARCHIVO)
    w("   %s -> disco %d bytes | LF %d bytes" % (ARCHIVO, a[0], a[1]))
    w("   sha256 LF: %s" % a[2])
    w("   los 16 primeros: %s -> el encargo dice 0a77b5a35a962621: %s"
      % (a[2][:16], "CALZA" if a[2][:16] == "0a77b5a35a962621" else "NO CALZA"))
    filas = [json.loads(l) for l in
             io.open(os.path.join(RAIZ, ARCHIVO.replace("/", os.sep)),
                     encoding="utf-8") if l.strip()]
    puestos_archivo = sorted(f.get("puesto_intra") for f in filas)
    w("   CIFRA filas: %d | MIN %d | MAX %d"
      % (len(filas), puestos_archivo[0], puestos_archivo[-1]))
    w("")

    w("B) EL TRAMO, CONTADO DE SU FICHERO Y NO TECLEADO")
    tramo = puestos_de(TRAMO)
    t = sha_de(TRAMO)
    w("   %s -> disco %d bytes | LF %d bytes | sha256 LF %s"
      % (TRAMO, t[0], t[1], t[2][:16]))
    w("   CIFRA puestos del tramo: %d" % len(tramo))
    w("   %s" % ", ".join(str(x) for x in tramo))
    w("   EL PUESTO %d, QUE ES EL QUE DISPARA ESTA RELECTURA: %s del tramo"
      % (PUESTO_DEL_ACTA, "DENTRO" if PUESTO_DEL_ACTA in tramo else "FUERA"))
    if PUESTO_DEL_ACTA not in tramo:
        w("   PARADA: el puesto que el acta nombra no esta en el tramo que se dice")
        w("   releer. No se relee un tramo que no contiene al sujeto.")
        print(NL.join(L))
        return 1
    w("")

    w("C) EL UNIVERSO YA CONSUMIDO, CONTADO DE SUS FICHEROS")
    evitar = set()
    for rel in UNIVERSO_CONSUMIDO:
        s = sha_de(rel)
        if s is None:
            w("   %s -> NO EXISTE" % rel)
            continue
        nums = numeros_de(rel) if "exclusion" in rel else puestos_de(rel)
        dentro = [x for x in nums if 1 <= x <= puestos_archivo[-1]]
        evitar |= set(dentro)
        w("   %-48s %6d bytes | %4d numeros | %4d dentro del archivo"
          % (rel, s[0], len(nums), len(dentro)))
    w("   CIFRA universo consumido (union, sin repetir): %d" % len(evitar))
    w("")

    w("D) LOS VECINOS DETERMINISTAS, CON vecinos() IMPORTADA Y NO COPIADA")
    w("   (su regla no se toca: cambia lo que se le pasa. Es la `5.2` del acta 188)")
    elegidos = vecinos(tramo, puestos_archivo[-1], evitar=evitar)
    w("   CIFRA vecinos elegidos: %d" % len(elegidos))
    w("   %s" % ", ".join(str(x) for x in elegidos))
    w("   AL DOBLE: %d del tramo mas %d vecinos = %d puestos"
      % (len(tramo), len(elegidos), len(tramo) + len(elegidos)))
    w("   ES EL DOBLE EXACTO: %s" % ("SI" if len(elegidos) == len(tramo) else "NO"))
    w("   SOLAPE de los vecinos con el propio tramo: %d"
      % len(set(elegidos) & set(tramo)))
    w("   SOLAPE de los vecinos con el universo consumido: %d"
      % len(set(elegidos) & evitar))
    w("   (los dos ceros salen POR CONSTRUCCION y no por suerte: `evitar` va")
    w("    dentro de la llamada, no comprobado despues)")
    todos_existen = all(p in set(puestos_archivo) for p in elegidos)
    w("   TODOS los vecinos existen en el archivo: %s" % ("SI" if todos_existen else "NO"))
    if not elegidos or not todos_existen:
        w("   PARADA: la seleccion sale vacia o nombra un puesto que no existe.")
        print(NL.join(L))
        return 1
    w("")

    w("E) EL AISLAMIENTO, CON aislador_de_ciega.py Y EL CRITERIO ESCRITO")
    lista = ",".join(str(x) for x in elegidos)
    cmd = [PY, "scripts/loop/aislador_de_ciega.py",
           "--criterio", CRITERIO,
           "--ciega", CIEGA, "--destape", DESTAPE,
           "--puestos", lista]
    w("   comando: aislador_de_ciega.py --criterio <el de arriba> --ciega %s"
      % CIEGA)
    w("            --destape %s --puestos <los %d vecinos>" % (DESTAPE, len(elegidos)))
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, env=env)
    salida = (r.stdout.decode("utf-8", errors="replace")
              + r.stderr.decode("utf-8", errors="replace"))
    for l in salida.replace(chr(13) + NL, NL).split(NL):
        if l.strip():
            w("      | " + l.rstrip())
    w("   exitcode del aislador: %d" % r.returncode)
    if r.returncode != 0:
        w("   PARADA: el aislador cayo en rojo. No se lee nada.")
        print(NL.join(L))
        return 1
    for rel in (CIEGA, DESTAPE):
        s = sha_de(rel)
        if s is None:
            w("   %s -> NO EXISTE. PARADA." % rel)
            print(NL.join(L))
            return 1
        w("   %s -> disco %d bytes | LF %d bytes | sha256 LF %s"
          % (rel, s[0], s[1], s[2][:16]))
    en_ciega = puestos_de(CIEGA)
    en_destape = puestos_de(DESTAPE)
    w("   CIFRA puestos en la ciega: %d | en el destape: %d"
      % (len(en_ciega), len(en_destape)))
    w("   LOS DOS TRAEN LOS MISMOS PUESTOS: %s"
      % ("SI" if en_ciega == en_destape == sorted(elegidos) else "NO"))
    w("")

    w("F) LA GUARDA DE FUGA, DICHA CON SUS PALABRAS")
    w("   el aislador NO escribe ninguno de los dos ficheros si algun valor de")
    w("   `clase` o de `razon` de los pares elegidos aparece en el texto ciego.")
    w("   Que los dos existan con bytes es la prueba de que esa guarda paso.")
    texto_ciego = io.open(os.path.join(RAIZ, CIEGA.replace("/", os.sep)),
                          encoding="utf-8", errors="replace").read()
    for palabra in ("clase", "razon", "DISCUTIBLE"):
        w("   la palabra %r aparece %d vez(ces) en la ciega"
          % (palabra, texto_ciego.count(palabra)))
    w("")

    w("G) EL ARCHIVO, REMEDIDO AL SALIR DE ESTE FICHERO")
    b = sha_de(ARCHIVO)
    w("   %s -> disco %d bytes | LF %d bytes" % (ARCHIVO, b[0], b[1]))
    w("   sha256 LF: %s" % b[2])
    w("   IDENTICO AL DE LA ENTRADA: %s" % ("SI" if a == b else "NO"))
    w("   (este fichero abre el archivo SOLO EN LECTURA y no decide ninguna clase)")
    w("")

    w("H) LO QUE FALTA, Y LO HACE UNA PERSONA CON LAS MANOS")
    w("   1. leer docs/loop/SALIDA_V%d_T4_CIEGA.txt SIN abrir el destape," % VUELTA)
    w("   2. escribir las clases en docs/loop/SALIDA_V%d_T4_MIS_CLASES.txt," % VUELTA)
    w("   3. y SOLO ENTONCES abrir docs/loop/SALIDA_V%d_T4_DESTAPE.txt y cotejar."
      % VUELTA)
    w("   EL ORDEN ES LA PRUEBA: unas clases escritas despues del destape no")
    w("   prueban nada, y por eso van en un fichero aparte y commiteado antes.")
    w("")

    texto = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%d_T4_AISLAMIENTO.txt" % VUELTA)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(texto.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
