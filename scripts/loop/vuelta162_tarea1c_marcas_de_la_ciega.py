# -*- coding: utf-8 -*-
r"""vuelta162_tarea1c_marcas_de_la_ciega.py . TAREA 1.c de la vuelta 162.

LAS DIECISEIS LECTURAS CIEGAS DEL AUDITOR DE LA VUELTA 161 DEJAN MARCA CONTABLE
EN EL REGISTRO, POR ADICION, SIN MOVER UNA SOLA CLASE.

POR QUE, Y NO ES INICIATIVA DEL EJECUTOR: ADJUDICACION 6.7 DEL ACTA 161. La
`P.5.2` obliga tambien al auditor, el auditor la adopta, y resuelve el choque con
`AUDITOR.md` 2 (*"las mediciones las corre quien tiene el instrumento"*) dandole
la mano al ejecutor: *"el ejecutor escribe mis marcas en la vuelta siguiente, por
adicion, citando la seccion de mi acta"*. **La firma la da LA VUELTA, no la
persona**, que es lo que la propia `P.5.2` dice.

LA MARCA CUMPLE LAS DOS CONDICIONES DE `P.5.2`: dice que es una **RELECTURA** y
dice **EN QUE VUELTA** (`RELECTURA CIEGA DEL AUDITOR, VUELTA 161`). La forma se
anade a `FORMAS_QUE_CUENTAN` del contador, igual que la vuelta 161 hizo con la
suya, o la definicion no contaria la lectura que la motiva.

NINGUNA CLASE SE MUEVE, Y NO SE PROMETE, SE COMPRUEBA: las 16 coinciden con la
vigente, y el instrumento lo asegura por assert antes de escribir.

DE DONDE SALE EL VEREDICTO DE CADA UNA, Y LAS DOS PROCEDENCIAS SE DECLARAN
APARTE porque NO son la misma prueba:
  - SEIS de las dieciseis (`049`, `098`, `052`, `095`, `100`, `122`) tienen su
    veredicto ESCRITO Y SELLADO en `docs/loop/_auditor_v161_mis_adjudicaciones.txt`
    (sha1 `ffe1fa6f`, comprobado hoy con `git hash-object`). El instrumento LO
    PARSEA de ahi: no se teclea.
  - LAS OTRAS DIEZ no tienen fichero con su letra: su veredicto se deriva de la
    TABLA DE LA SECCION 3 DEL ACTA 161, que publica **16 leidos, 16 coinciden, 0
    discrepan**. La derivacion se dice con todas sus letras en la propia marca,
    en vez de presentarla como si fuera una letra sellada. La tabla se LEE hoy
    del acta y se comprueba que sigue diciendo eso; si no, el instrumento PARA.

USO:  python scripts/loop/vuelta162_tarea1c_marcas_de_la_ciega.py
"""
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta159_motor_veredictos as motor  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = motor.RAIZ
SELLO = os.path.join(RAIZ, "docs", "loop", "_auditor_v161_mis_adjudicaciones.txt")
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
SHA1_ESPERADO = "ffe1fa6f"
MARCA = "RELECTURA CIEGA DEL AUDITOR, VUELTA 161"
EJEMPLARES = ["LD-OPC05-100", "LD-OPC05-122"]
FILA_TOTAL = "| **total** | **16** | **16** | **0** |"


def sha1_del_sello():
    r = subprocess.run(["git", "hash-object", "docs/loop/_auditor_v161_mis_adjudicaciones.txt"],
                       cwd=RAIZ, capture_output=True, text=True)
    return r.stdout.strip()


def veredictos_sellados():
    """{LD: clase} parseado del fichero sellado. NO se teclea ninguna letra."""
    d = {}
    for linea in io.open(SELLO, encoding="utf-8").read().split("\n"):
        m = re.match(r"^(\d{3})\s+([A-D])\s+\S", linea)
        if m:
            d["LD-OPC05-%s" % m.group(1)] = m.group(2)
    return d


def fila_de_la_tabla():
    """La fila TOTAL de la tabla de la seccion 3 del acta 161, leida hoy con su
    numero de linea. None si no esta."""
    lineas = io.open(ACTA, encoding="utf-8").read().split("\n")
    inicios = [i for i, l in enumerate(lineas, 1)
               if l.startswith("# ACTA DEL AUDITOR, VUELTA 161")]
    if len(inicios) != 1:
        return None, None
    for i in range(inicios[0], len(lineas) + 1):
        if lineas[i - 1].strip() == FILA_TOTAL:
            return i, lineas[i - 1].strip()
    return None, None


def main():
    print("=" * 78)
    print("VUELTA 162, TAREA 1.c: LAS 16 MARCAS DE LA CIEGA DEL AUDITOR")
    print("=" * 78)
    print("")

    print("A) EL SELLO, COMPROBADO HOY CON git hash-object")
    sha = sha1_del_sello()
    print("   sha1 de docs/loop/_auditor_v161_mis_adjudicaciones.txt: %s" % sha)
    print("   el acta 161 seccion 3 lo cita como: %s" % SHA1_ESPERADO)
    if not sha.startswith(SHA1_ESPERADO):
        print("   PARADA: el sello NO calza. No se escribe nada.")
        return 1
    print("   CALZA.")
    print("")

    print("B) LA TABLA DE LA SECCION 3 DEL ACTA 161, LEIDA HOY")
    ln, fila = fila_de_la_tabla()
    if ln is None:
        print("   PARADA: no se halla la fila total de la tabla de la ciega.")
        return 1
    print("   docs/loop/ACTA_AUDITOR.md:%d" % ln)
    print("      %s" % fila)
    print("")

    print("C) LA NOMINA, RECOMPUTADA DEL REGISTRO Y NO TECLEADA")
    E = motor.entradas()
    clases = {motor.ld_de(e): e["clase"] for e in E}
    en_c = sorted(ld for ld, c in clases.items()
                  if c == "C" and ld.startswith("LD-OPC05-"))
    print("   CIFRA en C hoy: %d" % len(en_c))
    print("   nomina en C: %s" % ", ".join(x.split("-")[-1] for x in en_c))
    nomina = en_c + [x for x in EJEMPLARES if x not in en_c]
    print("   mas los DOS ejemplares de exclusion: %s" % ", ".join(EJEMPLARES))
    print("   CIFRA nomina total: %d" % len(nomina))
    if len(nomina) != 16:
        print("   PARADA: la nomina no da 16.")
        return 1
    print("")

    print("D) LOS VEREDICTOS DE LA CIEGA, CON SU PROCEDENCIA DECLARADA APARTE")
    sellados = veredictos_sellados()
    print("   CIFRA con veredicto SELLADO y parseado del fichero: %d" % len(sellados))
    for ld in sorted(sellados):
        print("      %-16s sello dice %s | clase vigente %s" % (ld, sellados[ld], clases.get(ld)))
    discrepan = [ld for ld, c in sellados.items() if clases.get(ld) != c]
    print("   CIFRA discrepancias entre el sello y la clase vigente: %d" % len(discrepan))
    if discrepan:
        print("   PARADA: el sello del auditor discrepa de la clase vigente en %s."
              % ", ".join(discrepan))
        print("   Eso no lo resuelve esta tarea: seria mover una clase, y el encargo")
        print("   dice que las 16 coinciden.")
        return 1
    derivados = [ld for ld in nomina if ld not in sellados]
    print("   CIFRA con veredicto DERIVADO de la tabla del acta (16 de 16): %d"
          % len(derivados))
    print("      %s" % ", ".join(x.split("-")[-1] for x in sorted(derivados)))
    print("")

    veredictos = {}
    for ld in nomina:
        vigente = clases[ld]
        if ld in sellados:
            procedencia = (
                "SU LETRA ESTA SELLADA: el fichero de adjudicaciones ciegas del auditor "
                "(docs/loop/_auditor_v161_mis_adjudicaciones.txt, sha1 %s comprobado hoy "
                "con git hash-object) le da %s, y la clase vigente de esta fila es %s. "
                "CALZAN." % (SHA1_ESPERADO, sellados[ld], vigente))
        else:
            procedencia = (
                "SU LETRA NO ESTA EN NINGUN FICHERO SELLADO, Y SE DICE EN VEZ DE "
                "PRESENTARLA COMO SI LO ESTUVIERA: se deriva de la tabla de la seccion 3 "
                "del acta 161, leida hoy en docs/loop/ACTA_AUDITOR.md:%d, que publica "
                "'%s', o sea CERO discrepancias sobre las dieciseis. Por esa tabla, la "
                "lectura ciega dio %s, que es la clase vigente." % (ln, fila, vigente))
        motivo = (
            "MARCA DE SEGUNDA LECTURA POR P.5.2, ESCRITA POR EL EJECUTOR DE LA VUELTA "
            "162 POR LA ADJUDICACION 6.7 DEL ACTA 161, QUE SE LA ENCARGA CON ESAS "
            "PALABRAS ('el ejecutor escribe mis marcas en la vuelta siguiente, por "
            "adicion, citando la seccion de mi acta'). LA LECTURA ES DEL AUDITOR Y LA "
            "MANO ES DEL EJECUTOR: la firma la da LA VUELTA, no la persona. QUE FUE: "
            "relectura CIEGA, metodo declarado en la seccion 3 del acta 161 "
            "(docs/loop/_auditor_v161_ciega.py imprime solo titulo, fuente, entregable y "
            "pasos de los dos nodos, sin clase, sin via, sin cita y sin razon; las "
            "adjudicaciones se sellaron ANTES de destapar ninguna razon). VARA APLICADA: "
            "P.5.1 tal como el fundador la congelo, frase mas cuatro ejemplares. "
            "RESULTADO GLOBAL DE LA CIEGA: 16 leidos, 16 coinciden, 0 discrepan. ESTA "
            "FILA: %s LA CLASE NO SE MUEVE Y ESTA MARCA NO LA TOCA: es contable, no "
            "correctiva." % procedencia)
        veredictos[ld] = (vigente, motivo)

    def cabeza(vieja, nueva):
        return ("  [%s (2026-09-03), ANADIDA SIN BORRAR NADA DE LO ANTERIOR: LA "
                "CLASE SE SOSTIENE EN %s. " % (MARCA, vieja))

    def nota_md(vieja, nueva, motivo):
        return ("RELECTURA CIEGA DEL AUDITOR (vuelta 161, acta 161 seccion 3, sello sha1 "
                "%s), marca escrita por el ejecutor de la vuelta 162 por la adjudicacion "
                "6.7: la clase SE SOSTIENE en %s." % (SHA1_ESPERADO, vieja))

    rc = motor.aplicar(
        "E) LA ESCRITURA, POR ADICION, CON LAS GUARDAS DEL MOTOR",
        veredictos, MARCA, cabeza, nota_md, ids_esperados=sorted(nomina))
    if rc != 0:
        return rc

    D = motor.entradas()
    con_marca = [motor.ld_de(d) for d in D if MARCA in d["razon"]]
    print("")
    print("F) LA MARCA, RECONTADA DEL FICHERO YA ESCRITO")
    print("   CIFRA filas con la marca de la ciega: %d" % len(con_marca))
    print("   %s" % ", ".join(sorted(x.split("-")[-1] for x in con_marca)))
    movidas = [motor.ld_de(d) for d in D if d["clase"] != clases[motor.ld_de(d)]]
    print("   CIFRA clases movidas por esta tarea: %d" % len(movidas))
    if len(con_marca) != 16 or movidas:
        print("ROJO: o no son 16 marcas o alguna clase se movio.")
        return 1
    print("VERDE: las 16 marcas escritas, cero clases movidas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
