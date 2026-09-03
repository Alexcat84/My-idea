# -*- coding: utf-8 -*-
"""vuelta160_tarea7c_mutacion_guarda_cita.py . TAREA 7.c DE LA VUELTA 160.

LA PRUEBA DE MUTACION DE LA GUARDA QUE NACIO EN LA TAREA 7.b, y va porque
EJECUTOR.md 1 lo manda con esta letra: *NINGUN assert, GUARDA O CASO ROJO SE
PUBLICA COMO PRUEBA SIN HABER CORRIDO ANTES SU PRUEBA DE MUTACION*.

LA GUARDA QUE SE PRUEBA es la C.7 de `vuelta159_motor_veredictos.py`: al
terminar de escribir, ninguna fila puede tener en su campo `cita` una clase
distinta de la vigente. Nacio porque mis TAREAS 2.a y 2.b movieron cuatro clases
de C a D y dejaron sus cuatro citas diciendo `clase C`, que es la regresion de
la adjudicacion 6.6 del acta 158.

Y SE PRUEBA DE VERDAD, NO SOBRE UNA COPIA DE SU LOGICA. El arnes corre
`motor.aplicar` ENTERO, con sus seis guardas, apuntando a COPIAS TEMPORALES del
registro, del `.md` y del fichero de veredictos. NO SE TOCA NI UN FICHERO DEL
ARBOL: las tres rutas del modulo se repuntan y se restauran en un `finally`, y
al final se comprueba por sha256 que los tres originales estan intactos.

  CASO 1, EL ROJO QUE TIENE QUE CAER. Se mueve la clase de una fila cuya `cita`
  declara la clase VIEJA, que es exactamente lo que pasa cuando una tarea mueve
  una clase y no reescribe la cita. `motor.aplicar` TIENE QUE REVENTAR con
  AssertionError y el mensaje tiene que NOMBRAR la fila.

  CASO 2, LA CONTRAPRUEBA. La misma corrida sobre la misma copia, pero con un
  veredicto que SOSTIENE la clase: la guarda no puede caer. Sin esta, el caso 1
  no distinguiria una guarda que muerde de una que muerde siempre.

  CASO 3, LA MUTACION DEL VALOR ESPERADO. Se cambia el valor con el que la
  guarda compara (se le hace comparar la clase contra si misma) y se comprueba
  que ENTONCES YA NO CAE sobre el escenario del caso 1. Esto es lo que separa
  una guarda que mide de un `assert` que se aprueba solo.

USO:  python scripts/loop/vuelta160_tarea7c_mutacion_guarda_cita.py
"""
import hashlib
import io
import json
import os
import shutil
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import vuelta159_motor_veredictos as motor  # noqa: E402

MARCA = "PRUEBA DE MUTACION DE LA GUARDA DE LA CITA, VUELTA 160"


class Capturada(object):
    def __init__(self):
        self.trozos = []

    def write(self, s):
        self.trozos.append(s)
        return len(s)

    def flush(self):
        pass

    def valor(self):
        return "".join(self.trozos)


def sha(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as fh:
        h.update(fh.read())
    return h.hexdigest()


def cabeza(vieja, nueva):
    return "  [%s (2026-09-03): %s a %s. " % (MARCA, vieja, nueva)


def nota_md(vieja, nueva, motivo):
    return "PRUEBA DE MUTACION (vuelta 160): %s a %s." % (vieja, nueva)


def sujeto(rutas_registro):
    """LA FILA SUJETO NO SE TECLEA, SE COMPUTA: la primera fila cuya `cita`
    declara EXACTAMENTE la clase vigente, para que moverla deje la cita
    mintiendo. Devuelve (ld, clase_vigente, clase_contraria)."""
    E = [json.loads(x) for x in io.open(rutas_registro, encoding="utf-8") if x.strip()]
    for e in E:
        ld = e["cita"].split(",")[0].strip()
        if motor.clase_escrita_en_la_cita(e["cita"]) == e["clase"] and e["clase"] in "CD":
            return ld, e["clase"], ("C" if e["clase"] == "D" else "D")
    raise AssertionError("no hay ninguna fila que sirva de sujeto")


def correr(v, tmp):
    """Corre motor.aplicar con las rutas repuntadas a TMP. Devuelve
    (excepcion o None, salida)."""
    reales = (motor.REGISTRO, motor.LD_MD, motor.VERED)
    real_out = sys.stdout
    buf = Capturada()
    err = None
    try:
        motor.REGISTRO = os.path.join(tmp, "REGISTRO_DE_CITAS_OPC05.jsonl")
        motor.LD_MD = os.path.join(tmp, "LECTURAS_DIRIGIDAS.md")
        motor.VERED = os.path.join(tmp, "INTRA_DOMINIO_VEREDICTOS.jsonl")
        sys.stdout = buf
        try:
            motor.aplicar("PRUEBA DE MUTACION", v, MARCA, cabeza, nota_md,
                          ids_esperados=list(v))
        except Exception as e:  # noqa: BLE001
            err = e
    finally:
        motor.REGISTRO, motor.LD_MD, motor.VERED = reales
        sys.stdout = real_out
    return err, buf.valor()


def preparar(tmp):
    shutil.copy(os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl"),
                os.path.join(tmp, "REGISTRO_DE_CITAS_OPC05.jsonl"))
    shutil.copy(os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md"),
                os.path.join(tmp, "LECTURAS_DIRIGIDAS.md"))
    shutil.copy(os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl"),
                os.path.join(tmp, "INTRA_DOMINIO_VEREDICTOS.jsonl"))


def main():
    print("=" * 78)
    print("VUELTA 160, TAREA 7.c: PRUEBA DE MUTACION DE LA GUARDA DE LA CITA")
    print("=" * 78)
    print("")

    originales = {
        "docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl":
            os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl"),
        "docs/plan/LECTURAS_DIRIGIDAS.md":
            os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md"),
        "docs/INTRA_DOMINIO_VEREDICTOS.jsonl":
            os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl"),
    }
    sha_antes = dict((k, sha(v)) for k, v in originales.items())
    print("SHA256 DE LOS TRES ORIGINALES, ANTES DE NADA:")
    for k in sorted(sha_antes):
        print("   %-45s %s" % (k, sha_antes[k][:16]))
    print("")

    resultados = []
    tmp = tempfile.mkdtemp()
    try:
        preparar(tmp)
        ld, vigente, contraria = sujeto(os.path.join(tmp, "REGISTRO_DE_CITAS_OPC05.jsonl"))
        print("SUJETO COMPUTADO (no tecleado): %s, clase vigente %s, su cita la declara"
              % (ld, vigente))
        print("")

        # ------------------------------------------------------------------
        print("CASO 1: SE MUEVE LA CLASE Y NO SE TOCA LA CITA. TIENE QUE REVENTAR")
        print("-" * 78)
        preparar(tmp)
        err1, s1 = correr({ld: (contraria, "mutacion del arnes")}, tmp)
        es_assert = isinstance(err1, AssertionError)
        nombra = bool(err1) and ld in str(err1)
        ok1 = es_assert and nombra
        print("   excepcion: %s" % type(err1).__name__ if err1 else "   NINGUNA")
        print("   es AssertionError: %s" % es_assert)
        print("   el mensaje NOMBRA la fila %s: %s" % (ld, nombra))
        if err1:
            print("   mensaje: %s" % str(err1)[:200])
        for linea in s1.splitlines():
            if "C.7" in linea or "la cita dice" in linea:
                print("      | %s" % linea)
        print("   VEREDICTO: %s" % ("OK" if ok1 else "ROJO"))
        resultados.append(("CASO 1, la guarda CAE con la cita mintiendo", ok1))
        print("")

        # ------------------------------------------------------------------
        print("CASO 2, CONTRAPRUEBA: se SOSTIENE la clase. NO puede caer")
        print("-" * 78)
        preparar(tmp)
        err2, s2 = correr({ld: (vigente, "contraprueba del arnes")}, tmp)
        ok2 = err2 is None and "C.7" in s2
        print("   excepcion: %s" % (type(err2).__name__ if err2 else "NINGUNA"))
        if err2:
            print("   mensaje: %s" % str(err2)[:200])
        for linea in s2.splitlines():
            if "C.7" in linea or "cada cita declara" in linea:
                print("      | %s" % linea)
        print("   VEREDICTO: %s" % ("OK" if ok2 else "ROJO"))
        resultados.append(("CASO 2, contraprueba: sosteniendo la clase no cae", ok2))
        print("")

        # ------------------------------------------------------------------
        print("CASO 3, MUTACION DEL VALOR ESPERADO: si la guarda compara la clase")
        print("contra SI MISMA, deja de caer sobre el escenario del caso 1")
        print("-" * 78)
        real_fn = motor.clase_escrita_en_la_cita
        preparar(tmp)
        try:
            # LA MUTACION: la guarda pasa a leer la clase VIGENTE en vez de la
            # escrita en la cita, con lo que se compara consigo misma y no puede
            # caer nunca. Si el caso 1 siguiera cayendo con esto puesto, su rojo
            # no vendria de lo que dice medir.
            E = [json.loads(x) for x in
                 io.open(os.path.join(tmp, "REGISTRO_DE_CITAS_OPC05.jsonl"),
                         encoding="utf-8") if x.strip()]
            vigentes = dict((e["cita"].split(",")[0].strip(), e["clase"]) for e in E)
            vigentes[ld] = contraria
            motor.clase_escrita_en_la_cita = (
                lambda cita: vigentes.get(cita.split(",")[0].strip()))
            err3, s3 = correr({ld: (contraria, "mutacion del valor esperado")}, tmp)
        finally:
            motor.clase_escrita_en_la_cita = real_fn
        ok3 = err3 is None
        print("   excepcion con el valor esperado mutado: %s"
              % (type(err3).__name__ if err3 else "NINGUNA"))
        if err3:
            print("   mensaje: %s" % str(err3)[:200])
        print("   LA GUARDA DEJA DE CAER, o sea que su rojo del caso 1 venia de la")
        print("   comparacion que dice hacer y no de otra cosa.")
        print("   VEREDICTO: %s" % ("OK" if ok3 else "ROJO"))
        resultados.append(("CASO 3, mutado el valor esperado, la guarda no cae", ok3))
        print("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # ----------------------------------------------------------------------
    print("=" * 78)
    print("LOS TRES ORIGINALES, INTACTOS (medido, no prometido):")
    intactos = True
    for k in sorted(originales):
        ahora = sha(originales[k])
        igual = (ahora == sha_antes[k])
        intactos = intactos and igual
        print("   %-45s %s  identico: %s" % (k, ahora[:16], igual))
    resultados.append(("LA FRONTERA: los tres ficheros reales no se tocaron", intactos))
    print("")
    buenas = sum(1 for _, ok in resultados if ok)
    for nombre, ok in resultados:
        print("  %-5s %s" % ("OK" if ok else "ROJO", nombre))
    print("")
    print("CIFRA casos del arnes: %d" % len(resultados))
    print("CIFRA casos que se comportan: %d" % buenas)
    print("=" * 78)
    if buenas != len(resultados):
        print("ROJO: %d de %d no se comportan." % (len(resultados) - buenas, len(resultados)))
        return 1
    print("VERDE: los %d se comportan. LA GUARDA DE LA CITA MUERDE, Y MUERDE POR"
          % buenas)
    print("LO QUE DICE MEDIR.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
