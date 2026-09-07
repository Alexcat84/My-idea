# -*- coding: utf-8 -*-
r"""vuelta196_tarea2_relectura_al_doble.py . EL SUJETO DE LA RELECTURA AL DOBLE
DEL TRAMO DE LA TANDA DEL AUDITOR DE LA 196, ELEGIDO Y AISLADO ANTES DE QUE NADIE
MIRE NADA.

QUIEN LA ENCARGA Y CON QUE PALABRAS. **La encarga el AUDITOR y es DEUDA SUYA**:
`AUDITOR.md` 1.2 pone el doble en su mano, y UNA discrepancia suya, el `2428`,
cayo FUERA de su marcado, asi que EL CREDITO DE SU TANDA BAJA Y EL TRAMO SE RELEE
AL DOBLE. Quien la paga es el ejecutor, con el instrumento.

SON CIENTO VEINTE PARES, Y LA CIFRA NO ES UN DESCUIDO: la serie medida va 30, 60
y ahora 120, porque cada tanda doblada que vuelva a dar una discrepancia fuera del
marcado dobla otra vez. La regla es del fundador y esta escrita; aqui se ejecuta.

QUE ES EL TRAMO Y QUE ES EL DOBLE, Y NINGUNO SE ELIGE AQUI:

  . EL TRAMO son los 60 puestos de `docs/loop/_auditor_v196_ciega_blind.txt`.
  . EL DOBLE son sus 60 vecinos deterministas, con `vecinos()` IMPORTADA de
    `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y NO copiada.
  . LOS DOS ESTAN CERRADOS DESDE ANTES en
    `docs/loop/_auditor_v196_doble_para_la_197.txt`, sellado por el auditor para
    que no se puedan elegir despues de mirar. **AQUI SE RECOMPUTAN Y SE COTEJAN
    CONTRA ESA SELLADA**: si la recomputacion no da lo mismo, se publica la
    propia y se dice de que ficheros sale, en vez de copiar la ajena.
  . EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO (acta 188, `5.2` y `7.3`): a
    `vecinos()` se le pasa el conjunto `evitar` con TODO lo ya consumido, contado
    de sus CATORCE ficheros, de modo que **el cero sale por construccion y no por
    suerte**. La cifra de 621 que el encargo trae NO se copia: se cuenta aqui.

CLON DECLARADO de scripts/loop/vuelta195_tarea2_relectura_al_doble.py. Cambia el
TRAMO, la SELLADA, los `PUESTOS_DEL_ACTA` (que pasan de dos a UNO), el
`UNIVERSO_CONSUMIDO` (de DOCE ficheros a CATORCE), el CRITERIO, la lista de
QUEMADOS que este fichero estrena y este docstring. **Y LA MAQUINA NO SE TOCA.**

LO QUE ESTE FICHERO ESTRENA, Y ES LA PIEZA (f) DEL ENCARGO ADELANTADA AL SUJETO:
**LOS PUESTOS QUEMADOS SE DECLARAN ANTES DE LEER, NO DESPUES DE COTEJAR.** El
hallazgo `5.1` del acta 196 mide que el encargo quema puestos de la ciega
siguiente, y esta vuelta lo sufre en una forma nueva y peor: **la TAREA 1 obliga a
leer el acta 196 ENTERA, y la seccion 4 de esa acta publica la clase de archivo de
CUATRO puestos que estan dentro de estos 120** (`976` en su `4.1`, `2428` en su
`4.2`, `2662` en su `4.3` y `3173` en su `4.4`). El propio `PROMPT_SIGUIENTE.md`
de esta vuelta publica ademas la razon del `976` (*"la misma A del puesto 712"*) y
la del `2428` (*"ARISTA QUE FALTA, y con direccion"*). Y su seccion `5.1` dice que
el encargo de la 195 publico la clase del `654` y del `719`, que tambien estan
dentro. **SEIS de los 120 llegan con su clase sabida o derivable, y salen del
credito**, exactamente como el auditor saco sus dos. La lista va AQUI, en el
sujeto, sellada antes de leer nada, para que no se pueda elegir despues.

LA VARA SIGUE SIENDO LA DEL BANCO, `docs/BANCO_DE_TEXTOS.md` `9.6.1`, citada por
numero y copiada literal y no parafraseada (`9.5.0`: la regla SE CITA), con sus
precisiones `9.6.2` y `9.6.3`.

Y LLEVA PUESTOS LOS DOS ERRORES QUE EL EJECUTOR Y EL AUDITOR COMPARTEN, que es lo
mas util que salio de la auditoria: **LA VARA ES EL SUELO Y NO EL TECHO** (antes
de aplicarla se pregunta si el par pertenece a una familia con REGLA PROPIA ya
fijada) y **LA SEMEJANZA DE LOS IDS NO DECIDE** (el banco `9.6.3` dice que el
tamano del solape no decide y que se pesa el resto y en que lado). Los dos van
DENTRO del criterio, escritos en la ciega y no en la cabeza del lector.

Y LA CLASE `B` NI SE SALTA NI SE SOBRE EMITE: el sesgo esta medido en las dos
direcciones y las dos son perdida. El ejecutor emitio 4 `B` donde el archivo tenia
1; el auditor de la 195 emitio 0 donde tenia 1; el auditor de la 196 emitio 1 y
acerto.

LO QUE ESTE FICHERO NO HACE, Y ES LA MITAD QUE IMPORTA: **NO TOCA NINGUNA CLASE**.
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre en modo lectura y su `sha256` LF se
mide al entrar y al salir POR LAS DOS CONVENCIONES. Y **NO LEE EL DESTAPE**: lo
escribe y lo deja cerrado.

USO:
  python scripts/loop/vuelta196_tarea2_relectura_al_doble.py
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
TRAMO = "docs/loop/_auditor_v196_ciega_blind.txt"
# LA SELLADA DEL AUDITOR, QUE AQUI SE COTEJA Y NO SE COPIA.
SELLADA_DEL_DOBLE = "docs/loop/_auditor_v196_doble_para_la_197.txt"
# EL PUESTO QUE CAYO FUERA DEL MARCADO DEL AUDITOR Y QUE DISPARA AUDITOR.md 1.2.
PUESTOS_DEL_ACTA = [2428]

# LOS QUEMADOS, DECLARADOS ANTES DE LEER Y CON SU SEDE. Cada uno dice DONDE se
# publico su clase, para que la declaracion se pueda comprobar y no haya que
# creersela. NO SE ELIGEN DESPUES DE COTEJAR: se sellan aqui.
QUEMADOS = {
    976: "acta 196, adjudicacion 4.1: publica que el archivo dice A, y el "
         "PROMPT_SIGUIENTE de esta vuelta publica ademas su razon",
    2428: "acta 196, adjudicacion 4.2: publica que el archivo dice D, y el "
          "PROMPT_SIGUIENTE de esta vuelta publica ademas su razon",
    2662: "acta 196, adjudicacion 4.3: publica que el archivo dice D por una "
          "correccion declarada de la vuelta 51",
    3173: "acta 196, adjudicacion 4.4: publica que el archivo dice D y que el "
          "propio archivo se marca DISCUTIBLE MARCADO fuerte",
    654: "acta 196, hallazgo 5.1: declara que el encargo de la 195 publico su "
         "clase de archivo al ensenar la leccion de la B que faltaba",
    719: "acta 196, hallazgo 5.1: declara que el encargo de la 195 publico su "
         "clase de archivo al ensenar la leccion de la regla de familia",
}

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
    "docs/loop/SALIDA_V195_T2_CIEGA.txt",
    "docs/loop/_auditor_v196_ciega_blind.txt",
]
CIEGA = "docs/loop/SALIDA_V%d_T2_CIEGA.txt" % VUELTA
DESTAPE = "docs/loop/SALIDA_V%d_T2_DESTAPE.txt" % VUELTA

VARA_DEL_BANCO = (
    "docs/BANCO_DE_TEXTOS.md 9.6.1, LA VARA DE LA RAMA CONTENIDO-MANDA: "
    "LA LINEA O EL PROCEDIMIENTO. Literal: \"Si lo que el hijo añade a lo "
    "que la madre ya dice CABE EN UNA LÍNEA, REPITE. Si trae un "
    "PROCEDIMIENTO que la madre no tiene, CONTINÚA.\"")

# EL SUELO Y NO EL TECHO. Es el PRIMERO de los dos errores que el ejecutor y el
# auditor compartieron, medido en el 976 por los dos.
LA_VARA_ES_EL_SUELO = (
    "PRIMERO: LA VARA DE CONTENIDO-MANDA ES EL SUELO, NO EL TECHO. ANTES de "
    "aplicarla se pregunta si el par pertenece a una familia con REGLA PROPIA YA "
    "FIJADA, porque entonces manda la especifica. Y consultar la familia NO quema "
    "nada, porque las clases de OTROS puestos no son el sujeto sellado.")

# LA SEMEJANZA DE LOS IDS NO DECIDE. Es el SEGUNDO error compartido, medido en el
# 2428 por los dos, y su regla vive en el banco 9.6.3.
LOS_IDS_NO_DECIDEN = (
    "SEGUNDO: LA SEMEJANZA DE LOS IDS NO DECIDE. El banco 9.6.3 dice que el "
    "TAMANO DEL SOLAPE NO DECIDE y que se pesa EL RESTO Y EN QUE LADO. Dos ids "
    "que se diferencian en una letra pueden ser dos procedimientos distintos: si "
    "uno GENERA y el otro ELIGE, uno abre el abanico y el otro lo cierra, y "
    "entonces lo que hay es una ARISTA QUE FALTA, con direccion, y no una "
    "repeticion.")

# LA CLASE `B` NI SE SALTA NI SE SOBRE EMITE, y el sesgo esta medido en las dos
# direcciones.
LA_B_EN_SU_SITIO = (
    "LA CLASE B NI SE SALTA NI SE SOBRE EMITE, y el sesgo esta medido en LAS DOS "
    "direcciones: el ejecutor de la 195 emitio 4 B donde el archivo tenia 1, y el "
    "auditor de la 195 emitio 0 donde tenia 1. Las dos son perdida. B es el par "
    "que se pisa sin arista y sin que ninguno nombre al otro, no un comodin para "
    "la duda.")

CRITERIO = ("relectura AL DOBLE del tramo de la tanda del AUDITOR de la vuelta "
            "196 (AUDITOR.md 1.2, y es DEUDA DEL AUDITOR que paga el ejecutor "
            "con el instrumento): los 60 puestos de _auditor_v196_ciega_blind.txt "
            "MAS sus 60 vecinos deterministas, o sea CIENTO VEINTE pares. EL "
            "MOTIVO: UNA discrepancia del auditor, el 2428, cayo FUERA de su "
            "marcado, asi que el credito de su tanda baja y el tramo se relee al "
            "doble. La serie medida va 30, 60 y ahora 120. "
            "Los vecinos, elegidos con vecinos() importada de "
            "vuelta182_tarea1c_relectura_al_doble.py sobre el conjunto evitar de "
            "todo lo ya consumido, contado de sus catorce ficheros, para que el "
            "solape con el tramo y con el universo salga por construccion y no "
            "por suerte. "
            "LA VARA CON LA QUE SE LEE, CITADA POR NUMERO Y NO PARAFRASEADA: "
            + VARA_DEL_BANCO + " Y CON SUS DOS PRECISIONES, 9.6.2 y 9.6.3. "
            + LA_VARA_ES_EL_SUELO + " " + LOS_IDS_NO_DECIDEN + " " +
            LA_B_EN_SU_SITIO +
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
    """LOS 60 VECINOS QUE LA SELLADA DEL AUDITOR PUBLICA. PURA salvo por leer el
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
    w("AUDITOR DE LA 196. Deuda suya por AUDITOR.md 1.2, pagada con instrumento.")
    w("SON CIENTO VEINTE PARES: la serie medida va 30, 60 y ahora 120.")
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

    w("C) EL UNIVERSO YA CONSUMIDO, CONTADO DE SUS CATORCE FICHEROS")
    w("   EL ENCARGO PUBLICA 621 Y ADEMAS MANDA RECOMPUTARLO. Aqui no se copia")
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
    w("   CIFRA universo consumido, UNION DE LOS %d FICHEROS: %d" % (vistos, len(evitar)))
    w("   LA CIFRA DEL ENCARGO ES 621 SOBRE CATORCE FICHEROS -> %s"
      % ("CALZA" if len(evitar) == 621 else "NO CALZA, y manda la mia"))
    w("")
    w("   Y EL `561 SIN EL TRAMO` DEL ENCARGO SE MIDE POR LAS DOS LECTURAS,")
    w("   PORQUE NO SIGNIFICAN LO MISMO Y LA DIFERENCIA ES UNA MEDICION:")
    sin_fichero = len(antes)
    sin_puestos = len(evitar - set(tramo))
    w("      (a) UNION DE LOS OTROS %d FICHEROS, sin el del tramo: %d"
      % (vistos - 1, sin_fichero))
    w("      (b) DIFERENCIA DE CONJUNTOS, el universo menos los %d puestos del"
      % len(tramo))
    w("          tramo: %d" % sin_puestos)
    w("   LA (b) CALZA CON EL 561 DEL ENCARGO: %s"
      % ("SI" if sin_puestos == 561 else "NO"))
    w("   LA (a) NO TIENE POR QUE, Y LA CAUSA ESTA MEDIDA Y NO SUPUESTA: los 60")
    w("   puestos del tramo del auditor SON LOS MISMOS 60 de la tanda del")
    w("   ejecutor de la 195, asi que quitar SU FICHERO no los quita del")
    w("   universo, porque SALIDA_V195_T2_CIEGA.txt los trae enteros. Medido:")
    dentro_195 = len(set(tramo) & set(puestos_de("docs/loop/SALIDA_V195_T2_CIEGA.txt")))
    w("      puestos del tramo que tambien estan en SALIDA_V195_T2_CIEGA.txt: %d de %d"
      % (dentro_195, len(tramo)))
    w("   LO QUE MANDA PARA `vecinos()` ES LA UNION ENTERA (%d), que es la que"
      % len(evitar))
    w("   va DENTRO de la llamada. Las tres cifras se publican.")
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

    w("D.2) LOS QUEMADOS, DECLARADOS AQUI Y NO DESPUES DE COTEJAR")
    w("   ES LA PIEZA (f) DEL ENCARGO, ADELANTADA AL SUJETO, Y ES LA MISMA")
    w("   OPERACION QUE EL AUDITOR HIZO CON SUS DOS: un puesto cuya clase ya me")
    w("   dijeron NO prueba que yo lea bien, asi que SALE DEL CREDITO.")
    w("   LA CAUSA ES ESTRUCTURAL Y ESTA MEDIDA: la TAREA 1 de esta misma vuelta")
    w("   OBLIGA a leer el acta 196 entera, y su seccion 4 publica la clase de")
    w("   archivo de cuatro puestos que estan DENTRO de estos 120. No es un")
    w("   descuido mio ni suyo: es el hallazgo 5.1 del acta en su forma peor.")
    universo = sorted(set(tramo) | set(elegidos))
    quemados_dentro = sorted(k for k in QUEMADOS if k in set(universo))
    quemados_fuera = sorted(k for k in QUEMADOS if k not in set(universo))
    for k in sorted(QUEMADOS):
        w("   %-5d %s -> %s" % (k, "DENTRO" if k in set(universo) else "FUERA",
                                QUEMADOS[k]))
    w("   CIFRA quemados declarados: %d" % len(QUEMADOS))
    w("   CIFRA quemados DENTRO de los %d: %d" % (len(universo), len(quemados_dentro)))
    w("   CIFRA quemados FUERA: %d" % len(quemados_fuera))
    w("   CIFRA puestos que quedan para el credito limpio: %d"
      % (len(universo) - len(quemados_dentro)))
    w("   LOS QUEMADOS SE LEEN IGUAL Y SU CLASE SE PUBLICA IGUAL: lo que sale es")
    w("   el CREDITO, no la lectura. El cotejo se publica sobre los %d Y sobre"
      % len(universo))
    w("   los %d, que es lo que el acta 196 adjudico a favor en su 4.13."
      % (len(universo) - len(quemados_dentro)))
    w("")

    w("E) EL AISLAMIENTO DE LOS CIENTO VEINTE, CON aislador_de_ciega.py")
    w("   SE LEEN LOS CIENTO VEINTE, TRAMO Y DOBLE, que es lo que el encargo pide")
    w("   con esas palabras: LEE LOS 120 A CIEGAS, tramo y doble.")
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
