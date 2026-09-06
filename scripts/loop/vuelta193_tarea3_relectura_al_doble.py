# -*- coding: utf-8 -*-
r"""vuelta192_tarea2_relectura_al_doble.py . EL SUJETO DE LA RELECTURA AL DOBLE
DEL TRAMO DE LA VUELTA 191, ELEGIDO Y AISLADO ANTES DE QUE NADIE MIRE NADA.

QUIEN LA ENCARGA Y CON QUE PALABRAS. **La encarga el AUDITOR, no el ejecutor**, y
eso es la mitad del asunto: `AUDITOR.md` 1.2 pone el doble en su mano. El acta
192 lo encarga en su seccion 8 como TAREA 2 bloqueante, **y esta vez con MOTIVO
DOBLE**: el puesto **2832** cayo FUERA de los dudosos marcados de **dos lectores
independientes** en **dos tandas seguidas**, la del ejecutor en la vuelta 191 y la
del auditor en el acta 192.

QUE ES "EL TRAMO DE LA 191" Y QUE ES "AL DOBLE", DICHO ANTES DE ELEGIR NADA:

  . EL TRAMO es la tanda de 30 puestos de la vuelta 191,
    `docs/loop/SALIDA_V191_T2_CIEGA.txt`. El bloque `H.3` del sello de apertura de
    esta vuelta lo midio antes de tocar nada: 30 puestos, el 2832 DENTRO, y **el
    mismo conjunto exacto** que la ciega del auditor del acta 192,
    `docs/loop/_auditor_v192_ciega_blind.txt`. Aqui se vuelve a comprobar y no se
    cree.
  . AL DOBLE son sus **30 vecinos deterministas**, con `vecinos()` IMPORTADA de
    `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada. Sesenta
    puestos en total, que es el doble exacto.
  . EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO (acta 188, `5.2` y `7.3`): a
    `vecinos()` se le pasa el conjunto `evitar` con TODO lo ya consumido, de modo
    que **el cero sale por construccion y no por suerte**. Lo consumido son SEIS
    ficheros y no una cifra tecleada: las dos exclusiones, las dos ciegas de las
    actas 189b y 190, la tanda de la 190 **y la tanda de la 191, que es el propio
    tramo**.

Y AQUI LA RELECTURA NO ES MECANICA: **ES UNA CIEGA DE VERDAD**, con
`scripts/loop/aislador_de_ciega.py`, criterio escrito, ciega y destape en ficheros
SEPARADOS, y **las clases escritas y COMMITEADAS ANTES de abrir el destape**. Este
fichero escribe LA CIEGA Y EL DESTAPE y NO LOS LEE: quien los lee es el ejecutor,
con las manos, y escribe sus clases y sus dudosos en un tercer fichero.

Y LA PRECISION QUE EL ACTA 191 SUBRAYA EN SU `4.8` Y QUE SIGUE VALIENDO: **la
relectura del auditor sobre esos mismos 30 NO es el doble y no lo sustituye**. Al
doble es MAS EXTENSION, treinta vecinos nuevos; lo del auditor es OTRO LECTOR
sobre la misma extension. **Son dos controles distintos.**

LO QUE ESTE FICHERO NO HACE, Y ES LA MITAD QUE IMPORTA: **NO TOCA NINGUNA CLASE**.
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre en modo lectura y su `sha256` LF se
mide al entrar y al salir POR LAS DOS CONVENCIONES. Si de la relectura sale una
correccion, **se declara y se trae**, y no se escribe sobre el archivo.

CLON DECLARADO de scripts/loop/vuelta192_tarea2_relectura_al_doble.py. Cambia el
TRAMO, los `PUESTOS_DEL_ACTA` (que ahora son DOS y no uno), el
`UNIVERSO_CONSUMIDO` (que ahora lleva OCHO ficheros y no seis), la
`CIEGA_DEL_AUDITOR`, el CRITERIO y este docstring.

--- LA VARA DE LA CIEGA PASA A SER LA DEL BANCO (vuelta 193, TAREA 3.a) ---

**ES LA ADJUDICACION `4.9` DEL ACTA 193, QUE CONTESTA LA `P.3` A FAVOR, Y NO ES
DOCTRINA NUEVA:** sale POR EXTENSION CITABLE de `docs/BANCO_DE_TEXTOS.md` `9.6.1`,
**LA VARA DE LA RAMA CONTENIDO-MANDA: LA LINEA O EL PROCEDIMIENTO**, propuesta el
12 ago 2026 y adoptada por el auditor el mismo dia. Por `AUDITOR.md` 0 **el banco
es la primera fuente de verdad y el literal privado de un lector no es fuente de
nada**.

**LA FRASE VA COPIADA LITERAL Y NO PARAFRASEADA** (`9.5.0`: la regla se cita), y
va DENTRO del `CRITERIO` que se le pasa a `aislador_de_ciega.py`, con su numero
delante, para que quede escrito en la ciega y no en la cabeza del lector.

**LA VARA VIEJA SE NOMBRA EN VEZ DE BORRARSE**, porque una correccion que tapa lo
que corrige no se puede auditar. **Y la medicion que la tumba va en las DOS
direcciones**, que es lo que la separa de un criterio mal calibrado: en `1804` y
`2833` cada nodo trae procedimiento propio (CONTINUA, `D`) **y los dos lectores
leyeron `A`**; en `1068` lo que cada uno anade cabe en una linea (REPITE, `A`)
**y los dos leyeron `D`**.

LO QUE ESTE FICHERO NO HACE, Y ES LA MITAD QUE IMPORTA: **NO TOCA NINGUNA CLASE**.

USO:
  python scripts/loop/vuelta193_tarea3_relectura_al_doble.py
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
TRAMO = "docs/loop/SALIDA_V192_T2_CIEGA.txt"
# LOS DOS PUESTOS QUE CAYERON FUERA DEL MARCADO DE LOS DOS LECTORES. No es uno
# solo, como en la 192: son DOS, y los dos son los MISMOS para los dos lectores.
PUESTOS_DEL_ACTA = [1804, 2833]
# TODO LO YA CONSUMIDO, PARA QUE EL SOLAPE SALGA POR CONSTRUCCION. No es una lista
# tecleada de puestos: son ficheros, y los puestos se cuentan de ellos.
UNIVERSO_CONSUMIDO = [
    "docs/loop/_auditor_v190_exclusion.txt",
    "docs/loop/_auditor_v189b_exclusion.txt",
    "docs/loop/_auditor_v190_ciega_blind.txt",
    "docs/loop/_auditor_v189b_ciega_blind.txt",
    "docs/loop/SALIDA_V190_T4_CIEGA.txt",
    "docs/loop/SALIDA_V191_T2_CIEGA.txt",
    "docs/loop/_auditor_v192_ciega_blind.txt",
    "docs/loop/SALIDA_V192_T2_CIEGA.txt",
]
# EL MISMO CONJUNTO, MIRADO POR OTRO FICHERO: la ciega del auditor del acta 192.
# No se anade a `evitar` porque el encargo dice que es el MISMO conjunto que el
# tramo, y eso NO se cree: se comprueba y se publica.
CIEGA_DEL_AUDITOR = "docs/loop/_auditor_v193_ciega_blind.txt"
CIEGA = "docs/loop/SALIDA_V%d_T3_CIEGA.txt" % VUELTA
DESTAPE = "docs/loop/SALIDA_V%d_T3_DESTAPE.txt" % VUELTA
# LA VARA DE LAS CIEGAS, QUE DESDE ESTA VUELTA ES LA DEL BANCO Y NO UN LITERAL
# PRIVADO DEL LECTOR (vuelta 193, TAREA 3.a; adjudicacion 4.9 del acta 193, que
# contesta la P.3 A FAVOR). NO ES DOCTRINA NUEVA: sale POR EXTENSION CITABLE de
# una regla escrita, propuesta y adoptada el 12 ago 2026. Por `AUDITOR.md` 0 el
# banco es la primera fuente de verdad y el literal privado de un lector no es
# fuente de nada.
#
# LA FRASE VA COPIADA LITERAL Y NO PARAFRASEADA, que es lo que `9.5.0` exige: la
# regla SE CITA. Va con sus acentos, tal como esta en el banco.
VARA_DEL_BANCO = (
    "docs/BANCO_DE_TEXTOS.md 9.6.1, LA VARA DE LA RAMA CONTENIDO-MANDA: "
    "LA LINEA O EL PROCEDIMIENTO. Literal: \"Si lo que el hijo a\u00f1ade a lo "
    "que la madre ya dice CABE EN UNA L\u00cdNEA, REPITE. Si trae un "
    "PROCEDIMIENTO que la madre no tiene, CONTIN\u00daA.\"")

# Y LA VARA VIEJA SE NOMBRA EN VEZ DE BORRARSE, porque una correccion que tapa lo
# que corrige no se puede auditar: era el solape de pasos, un literal que el
# ejecutor y el auditor escribian cada uno por su cuenta. LA MEDICION QUE LA
# TUMBA es del acta 193 y va en las dos direcciones: en 1804 y 2833 cada nodo
# trae procedimiento entero propio, luego CONTINUA, luego D, y los DOS lectores
# leyeron A; en 1068 lo que cada uno anade cabe en una linea, luego REPITE, luego
# A, y los DOS leyeron D. Un criterio que se equivoca en los dos sentidos no esta
# calibrado de menos: mide otra cosa.
VARA_VIEJA = ("el solape de pasos entre madre e hijo, literal privado de cada "
              "lector, tumbado por la 4.9 del acta 193")

CRITERIO = ("relectura AL DOBLE del tramo de la vuelta 192 (AUDITOR.md 1.2, "
            "encargada por el AUDITOR en la seccion 8 del acta 193 y no auto "
            "encargada por el ejecutor): los 30 vecinos deterministas de la "
            "tanda de 30 puestos de la vuelta 192 (SALIDA_V192_T2_CIEGA.txt). "
            "EL MOTIVO ES TRIPLE: dos discrepancias cayeron fuera del marcado "
            "del auditor, las dos cayeron tambien fuera del marcado del "
            "ejecutor, y son el MISMO par (1804 y 2833) para los dos lectores. "
            "Elegidos con vecinos() importada de "
            "vuelta182_tarea1c_relectura_al_doble.py sobre el conjunto evitar "
            "de todo lo ya consumido, contado de sus ocho ficheros, para que el "
            "solape con el tramo y con el universo salga por construccion y no "
            "por suerte. "
            "LA VARA CON LA QUE SE LEE, CITADA POR NUMERO Y NO PARAFRASEADA: "
            + VARA_DEL_BANCO +
            " COMO SE APLICA, y es deliberadamente mecanico: se lee el paso de "
            "la madre que el hijo desarrolla y se pregunta si es una linea o si "
            "ya trae el procedimiento; se lee el nodo hijo entero y se pregunta "
            "que queda si se le quita lo que la madre ya dijo; y de lo que "
            "queda se pregunta si cabe en una linea o si es una secuencia de "
            "acciones con su propia logica. "
            "LA VARA QUE ESTA SUSTITUYE, NOMBRADA EN VEZ DE BORRADA: "
            + VARA_VIEJA + ".")

PAT_PUESTO = re.compile(r"puesto_intra[^0-9]{0,12}(\d+)")


def sha_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    datos = io.open(p, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest(),
            hashlib.sha256(datos).hexdigest())


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
    w("VUELTA %d, TAREA 3: EL SUJETO DE LA RELECTURA AL DOBLE DEL TRAMO DE LA 192"
      % VUELTA)
    w("=" * 78)
    w("")

    w("A) EL ARCHIVO, MEDIDO AL ENTRAR Y ABIERTO SOLO EN LECTURA")
    a = sha_de(ARCHIVO)
    w("   %s -> disco %d bytes | LF %d bytes" % (ARCHIVO, a[0], a[1]))
    w("   sha256 LF    : %s" % a[2])
    w("   sha256 disco : %s" % a[3])
    w("   los 16 primeros del LF: %s -> el encargo dice 0a77b5a35a962621: %s"
      % (a[2][:16], "CALZA" if a[2][:16] == "0a77b5a35a962621" else "NO CALZA"))
    w("   POR LAS DOS CONVENCIONES, que es lo que el encargo pide con esas")
    w("   palabras: los dos sha256 son iguales: %s" % ("SI" if a[2] == a[3] else "NO"))
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
    fuera_del_tramo = [p for p in PUESTOS_DEL_ACTA if p not in tramo]
    for p in PUESTOS_DEL_ACTA:
        w("   EL PUESTO %d, QUE TUMBO A LOS DOS LECTORES: %s del tramo"
          % (p, "DENTRO" if p in tramo else "FUERA"))
    if fuera_del_tramo:
        w("   PARADA: los puestos %s que el acta nombra no estan en el tramo que"
          % ", ".join(str(x) for x in fuera_del_tramo))
        w("   se dice releer. No se relee un tramo que no contiene al sujeto.")
        print(NL.join(L))
        return 1
    w("   Y LA CIEGA DEL AUDITOR DEL ACTA 193, QUE EL ENCARGO DICE QUE ES EL MISMO")
    w("   CONJUNTO. NO SE CREE: SE CUENTA DE SU FICHERO.")
    ciega_aud = puestos_de(CIEGA_DEL_AUDITOR)
    ca = sha_de(CIEGA_DEL_AUDITOR)
    w("   %s -> disco %d bytes | %d puestos"
      % (CIEGA_DEL_AUDITOR, ca[0] if ca else -1, len(ciega_aud)))
    w("   ES EL MISMO CONJUNTO QUE EL TRAMO: %s"
      % ("SI" if set(ciega_aud) == set(tramo) else
         "NO, la diferencia simetrica es %d" % len(set(ciega_aud) ^ set(tramo))))
    w("")

    w("C) EL UNIVERSO YA CONSUMIDO, CONTADO DE SUS OCHO FICHEROS")
    w("   (EL ENCARGO NO DA NINGUNA CIFRA AQUI Y MANDA CONTARLA DE SUS FICHEROS.")
    w("    Aqui no se copia ninguna: se cuentan, Y CON SUS NOMBRES)")
    evitar = set()
    antes = set()
    for rel in UNIVERSO_CONSUMIDO:
        s = sha_de(rel)
        if s is None:
            w("   %s -> NO EXISTE" % rel)
            continue
        nums = numeros_de(rel) if "exclusion" in rel else puestos_de(rel)
        dentro = [x for x in nums if 1 <= x <= puestos_archivo[-1]]
        evitar |= set(dentro)
        if rel != TRAMO:
            antes |= set(dentro)
        w("   %-48s %7d bytes | %4d numeros | %4d dentro del archivo"
          % (rel, s[0], len(nums), len(dentro)))
    w("   CIFRA universo consumido SIN la tanda de la 192: %d" % len(antes))
    w("   CIFRA universo consumido CON la tanda de la 192: %d" % len(evitar))
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
    w("   TODOS los vecinos existen en el archivo: %s"
      % ("SI" if todos_existen else "NO"))
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
    w("   1. leer docs/loop/SALIDA_V%d_T3_CIEGA.txt SIN abrir el destape," % VUELTA)
    w("   2. escribir las clases Y LOS DUDOSOS NOMBRADOS DELANTE en")
    w("      docs/loop/SALIDA_V%d_T3_MIS_CLASES.txt, y COMMITEARLO," % VUELTA)
    w("   3. y SOLO ENTONCES abrir docs/loop/SALIDA_V%d_T3_DESTAPE.txt y cotejar."
      % VUELTA)
    w("   EL ORDEN ES LA PRUEBA, Y EL COMMIT ES DONDE SE VE: unas clases escritas")
    w("   despues del destape no prueban nada.")
    w("")

    texto = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%d_T3_AISLAMIENTO.txt" % VUELTA)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(texto.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
