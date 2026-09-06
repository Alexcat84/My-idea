# -*- coding: utf-8 -*-
r"""vuelta195_tarea2_relectura_al_doble.py . EL SUJETO DE LA RELECTURA AL DOBLE
DEL TRAMO DE LA TANDA DEL AUDITOR DE LA 195, ELEGIDO Y AISLADO ANTES DE QUE NADIE
MIRE NADA.

QUIEN LA ENCARGA Y CON QUE PALABRAS. **La encarga el AUDITOR y es DEUDA SUYA**:
`AUDITOR.md` 1.2 pone el doble en su mano, y dos discrepancias suyas, el `654` y
el `719`, cayeron FUERA de su marcado, asi que EL CREDITO DE SU TANDA BAJA Y EL
TRAMO SE RELEE AL DOBLE. Quien la paga es el ejecutor, con el instrumento.

QUE ES EL TRAMO Y QUE ES EL DOBLE, Y NINGUNO SE ELIGE AQUI:

  . EL TRAMO son los 30 puestos de `docs/loop/_auditor_v195_ciega_blind.txt`.
  . EL DOBLE son sus 30 vecinos deterministas, con `vecinos()` IMPORTADA de
    `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y NO copiada.
  . LOS DOS ESTAN CERRADOS DESDE ANTES en
    `docs/loop/_auditor_v195_doble_para_la_196.txt`, sellado por el auditor para
    que no se puedan elegir despues de mirar. **AQUI SE RECOMPUTAN Y SE COTEJAN
    CONTRA ESA SELLADA**: si la recomputacion no da lo mismo, se publica la
    propia y se dice de que ficheros sale, en vez de copiar la ajena.
  . EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO (acta 188, `5.2` y `7.3`): a
    `vecinos()` se le pasa el conjunto `evitar` con TODO lo ya consumido, contado
    de sus DOCE ficheros, de modo que **el cero sale por construccion y no por
    suerte**. La cifra de 591 que el encargo trae NO se copia: se cuenta aqui.

CLON DECLARADO de scripts/loop/vuelta193_tarea3_relectura_al_doble.py. Cambia el
TRAMO (que ahora es la ciega del AUDITOR y no una salida del ejecutor), los
`PUESTOS_DEL_ACTA`, el `UNIVERSO_CONSUMIDO` (que pasa de OCHO ficheros a DOCE), la
`SELLADA_DEL_DOBLE` que aqui se coteja y que alli no existia, el CRITERIO y este
docstring. **Y LA MAQUINA NO SE TOCA.**

LA VARA SIGUE SIENDO LA DEL BANCO, `docs/BANCO_DE_TEXTOS.md` `9.6.1`, citada por
numero y copiada literal y no parafraseada (`9.5.0`: la regla SE CITA).

Y LLEVA PUESTO EL ERROR QUE EL AUDITOR MIDIO EN SU PROPIA TANDA, QUE ES LO MAS
UTIL QUE SACO DE ELLA: **LA VARA DE CONTENIDO-MANDA ES EL SUELO, NO EL TECHO.**
Antes de aplicarla se pregunta si el par pertenece a una familia con REGLA PROPIA
ya fijada, porque entonces manda la especifica. El `719` se perdio por no
preguntarlo: hay regla fijada en el puesto `595` (en una serie por fases, dos
nodos de fases distintas son sanos y dos nodos de la MISMA fase son gemelos) con
el `580` de precedente vivo. Eso va DENTRO del criterio, escrito en la ciega y no
en la cabeza del lector.

Y LA CLASE `B` NO SE SALTA: el auditor emitio CERO `B` en 30 pares y el archivo
tenia una. Un lector que solo reparte `A` y `D` no esta leyendo mas fino, esta
perdiendo una clase entera. Eso tambien va dentro del criterio.

LO QUE ESTE FICHERO NO HACE, Y ES LA MITAD QUE IMPORTA: **NO TOCA NINGUNA CLASE**.
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre en modo lectura y su `sha256` LF se
mide al entrar y al salir POR LAS DOS CONVENCIONES. Y **NO LEE EL DESTAPE**: lo
escribe y lo deja cerrado. Quien lee la ciega es el ejecutor, con las manos, y
escribe sus clases en un tercer fichero ANTES de abrir el destape.

USO:
  python scripts/loop/vuelta195_tarea2_relectura_al_doble.py
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
TRAMO = "docs/loop/_auditor_v195_ciega_blind.txt"
# LA SELLADA DEL AUDITOR, QUE AQUI SE COTEJA Y NO SE COPIA.
SELLADA_DEL_DOBLE = "docs/loop/_auditor_v195_doble_para_la_196.txt"
# LOS DOS PUESTOS QUE CAYERON FUERA DEL MARCADO DEL AUDITOR Y QUE DISPARAN
# AUDITOR.md 1.2. Se comprueba que estan DENTRO del tramo que se dice releer.
PUESTOS_DEL_ACTA = [654, 719]
# TODO LO YA CONSUMIDO, PARA QUE EL SOLAPE SALGA POR CONSTRUCCION. No es una lista
# tecleada de puestos: son ficheros, y los puestos se cuentan de ellos.
UNIVERSO_CONSUMIDO = [
    "docs/loop/_auditor_v189b_exclusion.txt",
    "docs/loop/_auditor_v190_exclusion.txt",
    "docs/loop/_auditor_v189b_ciega_blind.txt",
    "docs/loop/_auditor_v190_ciega_blind.txt",
    "docs/loop/SALIDA_V190_T4_CIEGA.txt",
    "docs/loop/SALIDA_V191_T2_CIEGA.txt",
    "docs/loop/_auditor_v192_ciega_blind.txt",
    "docs/loop/SALIDA_V192_T2_CIEGA.txt",
    "docs/loop/_auditor_v193_ciega_blind.txt",
    "docs/loop/SALIDA_V193_T3_CIEGA.txt",
    "docs/loop/_auditor_v194_ciega_blind.txt",
    "docs/loop/_auditor_v195_ciega_blind.txt",
]
CIEGA = "docs/loop/SALIDA_V%d_T2_CIEGA.txt" % VUELTA
DESTAPE = "docs/loop/SALIDA_V%d_T2_DESTAPE.txt" % VUELTA

VARA_DEL_BANCO = (
    "docs/BANCO_DE_TEXTOS.md 9.6.1, LA VARA DE LA RAMA CONTENIDO-MANDA: "
    "LA LINEA O EL PROCEDIMIENTO. Literal: \"Si lo que el hijo añade a lo "
    "que la madre ya dice CABE EN UNA LÍNEA, REPITE. Si trae un "
    "PROCEDIMIENTO que la madre no tiene, CONTINÚA.\"")

# EL SUELO Y NO EL TECHO. Es el error que el auditor midio en su propia tanda y
# que el encargo manda llevar puesto. No es doctrina nueva: es el orden en que se
# aplican dos reglas que ya existen, y va escrito para que no se olvide a mitad.
LA_VARA_ES_EL_SUELO = (
    "LA VARA DE CONTENIDO-MANDA ES EL SUELO, NO EL TECHO. ANTES de aplicarla se "
    "pregunta si el par pertenece a una familia con REGLA PROPIA YA FIJADA, "
    "porque entonces manda la especifica. Precedente medido y citado: el puesto "
    "595 fija que en una serie por fases, dos nodos de FASES DISTINTAS son sanos "
    "y dos nodos de la MISMA fase son gemelos, con el 580 de precedente vivo. El "
    "auditor perdio el 719 por no preguntarselo y llamo A a lo que es D.")

# LA CLASE `B` EXISTE Y NO SE SALTA.
LA_B_NO_SE_SALTA = (
    "LA CLASE B NO SE SALTA. El auditor emitio CERO B en 30 pares y el archivo "
    "tenia una, el 654: dos listas del mismo paso del embudo, cruzadas en el "
    "medio, sin arista y sin que ninguna nombre a la otra. Un lector que solo "
    "reparte A y D no esta leyendo mas fino: esta perdiendo una clase entera.")

CRITERIO = ("relectura AL DOBLE del tramo de la tanda del AUDITOR de la vuelta "
            "195 (AUDITOR.md 1.2, y es DEUDA DEL AUDITOR que paga el ejecutor "
            "con el instrumento): los 30 puestos de _auditor_v195_ciega_blind.txt "
            "MAS sus 30 vecinos deterministas. EL MOTIVO: dos discrepancias del "
            "auditor, el 654 y el 719, cayeron FUERA de su marcado, asi que el "
            "credito de su tanda baja y el tramo se relee al doble. "
            "Los vecinos, elegidos con vecinos() importada de "
            "vuelta182_tarea1c_relectura_al_doble.py sobre el conjunto evitar de "
            "todo lo ya consumido, contado de sus doce ficheros, para que el "
            "solape con el tramo y con el universo salga por construccion y no "
            "por suerte. "
            "LA VARA CON LA QUE SE LEE, CITADA POR NUMERO Y NO PARAFRASEADA: "
            + VARA_DEL_BANCO + " " + LA_VARA_ES_EL_SUELO + " " +
            LA_B_NO_SE_SALTA +
            " COMO SE APLICA, y es deliberadamente mecanico: primero se pregunta "
            "si hay regla propia de familia; si no la hay, se lee el paso de la "
            "madre que el hijo desarrolla y se pregunta si es una linea o si ya "
            "trae el procedimiento; se lee el nodo hijo entero y se pregunta que "
            "queda si se le quita lo que la madre ya dijo; y de lo que queda se "
            "pregunta si cabe en una linea o si es una secuencia de acciones con "
            "su propia logica.")

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


def doble_de_la_sellada(rel=None):
    """LOS 30 VECINOS QUE LA SELLADA DEL AUDITOR PUBLICA. PURA salvo por leer el
    fichero, y con `rel` por parametro para que se pueda apuntar a uno fabricado.

    Se lee SOLO la linea que empieza por `EL DOBLE`, y no todos los numeros del
    fichero: el fichero trae tambien el tramo y la cifra del universo, y meterlos
    en el mismo saco daria un cotejo que siempre calza y no prueba nada."""
    p = os.path.join(RAIZ, (rel or SELLADA_DEL_DOBLE).replace("/", os.sep))
    if not os.path.isfile(p):
        return []
    for l in io.open(p, encoding="utf-8", errors="replace"):
        if l.strip().startswith("EL DOBLE"):
            crudo = l.split(":", 1)[1] if ":" in l else ""
            return sorted(int(x) for x in re.findall(r"\d+", crudo))
    return []


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2: EL SUJETO DE LA RELECTURA AL DOBLE DEL TRAMO DEL"
      % VUELTA)
    w("AUDITOR DE LA 195. Deuda suya por AUDITOR.md 1.2, pagada con instrumento.")
    w("=" * 78)
    w("")

    w("A) EL ARCHIVO, MEDIDO AL ENTRAR Y ABIERTO SOLO EN LECTURA")
    a = sha_de(ARCHIVO)
    w("   %s -> disco %d bytes | LF %d bytes" % (ARCHIVO, a[0], a[1]))
    w("   sha256 LF    : %s" % a[2])
    w("   sha256 disco : %s" % a[3])
    w("   los 16 primeros del LF: %s -> el encargo dice 0a77b5a35a962621: %s"
      % (a[2][:16], "CALZA" if a[2][:16] == "0a77b5a35a962621" else "NO CALZA"))
    w("   POR LAS DOS CONVENCIONES: los dos sha256 son iguales: %s"
      % ("SI" if a[2] == a[3] else "NO"))
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
    w("   %s" % TRAMO)
    w("      disco %d bytes | LF %d bytes | sha256 LF %s" % (t[0], t[1], t[2][:16]))
    w("   CIFRA puestos del tramo: %d" % len(tramo))
    w("   %s" % ", ".join(str(x) for x in tramo))
    fuera_del_tramo = [p for p in PUESTOS_DEL_ACTA if p not in tramo]
    for p in PUESTOS_DEL_ACTA:
        w("   EL PUESTO %d, QUE CAYO FUERA DEL MARCADO DEL AUDITOR: %s del tramo"
          % (p, "DENTRO" if p in tramo else "FUERA"))
    if fuera_del_tramo:
        w("   PARADA: los puestos %s que el acta nombra no estan en el tramo que"
          % ", ".join(str(x) for x in fuera_del_tramo))
        w("   se dice releer. No se relee un tramo que no contiene al sujeto.")
        print(NL.join(L))
        return 1
    w("")

    w("C) EL UNIVERSO YA CONSUMIDO, CONTADO DE SUS DOCE FICHEROS")
    w("   EL ENCARGO PUBLICA 591 Y ADEMAS MANDA RECOMPUTARLO. Aqui no se copia")
    w("   ninguna cifra: se cuentan, Y CON SUS NOMBRES.")
    evitar = set()
    antes = set()
    vistos = 0
    for rel in UNIVERSO_CONSUMIDO:
        s = sha_de(rel)
        if s is None:
            w("   %-46s NO EXISTE" % rel)
            continue
        vistos += 1
        nums = numeros_de(rel) if "exclusion" in rel else puestos_de(rel)
        dentro = [x for x in nums if 1 <= x <= puestos_archivo[-1]]
        evitar |= set(dentro)
        if rel != TRAMO:
            antes |= set(dentro)
        w("   %-46s %7d bytes | %4d numeros | %4d dentro del archivo"
          % (rel, s[0], len(nums), len(dentro)))
    w("   CIFRA ficheros del universo que EXISTEN: %d de %d"
      % (vistos, len(UNIVERSO_CONSUMIDO)))
    w("   CIFRA universo consumido SIN el tramo de la 195: %d" % len(antes))
    w("   CIFRA universo consumido CON el tramo de la 195: %d" % len(evitar))
    w("   LA CIFRA DEL ENCARGO ES 591 SOBRE DOCE FICHEROS. LA MIA ES %d SOBRE %d."
      % (len(evitar), vistos))
    w("   CALZAN: %s" % ("SI" if len(evitar) == 591 else
                         "NO, y manda la mia, que sale de los ficheros de arriba"))
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

    w("D.1) EL COTEJO CONTRA LA SELLADA DEL AUDITOR, QUE NO SE COPIA")
    sellado = doble_de_la_sellada()
    s = sha_de(SELLADA_DEL_DOBLE)
    w("   %s" % SELLADA_DEL_DOBLE)
    w("      disco %d bytes | LF %d bytes | sha256 LF %s"
      % (s[0], s[1], s[2][:16]) if s else "      NO EXISTE")
    w("   CIFRA vecinos que la sellada publica: %d" % len(sellado))
    w("   MI RECOMPUTACION Y LA SELLADA SON EL MISMO CONJUNTO: %s"
      % ("SI" if set(sellado) == set(elegidos) else "NO"))
    if set(sellado) != set(elegidos):
        w("   SOLO EN LA SELLADA: %s"
          % ", ".join(str(x) for x in sorted(set(sellado) - set(elegidos))))
        w("   SOLO EN LA MIA:     %s"
          % ", ".join(str(x) for x in sorted(set(elegidos) - set(sellado))))
        w("   SE PUBLICA LA MIA CON SUS FICHEROS, Y LA DISCREPANCIA SE DECLARA")
        w("   EN VEZ DE RESOLVERSE COPIANDO (EJECUTOR.md 2).")
    w("")

    w("E) EL AISLAMIENTO DE LOS SESENTA, CON aislador_de_ciega.py")
    w("   SE LEEN LOS SESENTA, TRAMO Y DOBLE, que es lo que el encargo pide con")
    w("   esas palabras: LEE LOS 60 A CIEGAS, tramo y doble.")
    universo = sorted(set(tramo) | set(elegidos))
    w("   CIFRA puestos que van a la ciega: %d" % len(universo))
    lista = ",".join(str(x) for x in universo)
    cmd = [PY, "scripts/loop/aislador_de_ciega.py",
           "--criterio", CRITERIO,
           "--ciega", CIEGA, "--destape", DESTAPE,
           "--puestos", lista]
    w("   comando: aislador_de_ciega.py --criterio <el de arriba> --ciega %s"
      % CIEGA)
    w("            --destape %s --puestos <los %d puestos>" % (DESTAPE, len(universo)))
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
        m = sha_de(rel)
        if m is None:
            w("   ROJO: %s NO EXISTE tras el aislador" % rel)
        else:
            w("   %s -> disco %d bytes | LF %d bytes | sha256 LF %s"
              % (rel, m[0], m[1], m[2][:16]))
            w("      LA RUTA QUE PROMETE PRUEBA ES CIFRA: no esta vacia: %s"
              % ("SI" if m[0] > 0 else "NO, CERO BYTES"))
    w("")

    w("F) EL ARCHIVO AL SALIR, REMEDIDO Y NO SUPUESTO")
    b = sha_de(ARCHIVO)
    w("   sha256 LF al entrar: %s" % a[2][:16])
    w("   sha256 LF al salir : %s" % b[2][:16])
    w("   NO SE MOVIO NINGUN VEREDICTO: %s" % ("SI" if a[2] == b[2] else "NO"))
    w("")
    w("G) LO QUE FALTA, Y LO HACE EL EJECUTOR CON LAS MANOS")
    w("   Este fichero NO LEE EL DESTAPE. Escribe la ciega y el destape y los")
    w("   deja cerrados. Las clases se escriben en un tercer fichero ANTES de")
    w("   abrir el destape, y ese orden es lo unico que hace que el cotejo valga.")
    w("")
    w("FIN")

    texto = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%d_T2_SUJETO.txt" % VUELTA)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(texto.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
