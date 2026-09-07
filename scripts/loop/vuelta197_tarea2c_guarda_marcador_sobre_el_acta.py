# -*- coding: utf-8 -*-
r"""vuelta197_tarea2c_guarda_marcador_sobre_el_acta.py . LA GUARDA DE LA `C.A1`,
CORRIDA SOBRE EL ACTA 197 DE VERDAD Y NO SOBRE UN TEXTO FABRICADO.

POR QUE EXISTE ADEMAS DEL ARNES. `scripts/loop/vuelta197_tarea2_mutacion_orden_del_turno.py`
prueba `guarda_del_marcador()` con su caso positivo por mutacion, sobre texto
fabricado y con las cuatro mutaciones que tienen que morder. **Eso prueba la
funcion; esto prueba la casa.** La `C.A1` va por su TERCERA acta seguida (195, 196
y 197) y el remedio de memoria ya fallo una vez, asi que la guarda tiene que poder
correrse sobre el acta REAL sin que nadie tenga que montar nada.

LO QUE HACE, EN ORDEN:

  1. SELLA la salida de `AP.marcador()` de la vuelta 197 en
     `docs/loop/SALIDA_MARCADOR_AUDITOR_V197.json`. **Esa es la salida contra la
     que la guarda coteja**, y sin ella la guarda cae en rojo por construccion.
  2. ACOTA el cuerpo del acta 197 en `docs/loop/ACTA_AUDITOR.md`, contando su
     cabecera EN ESTA CORRIDA y no por una linea heredada.
  3. Corre `AP.guarda_del_marcador()` sobre ese cuerpo.
  4. Y CORRE LA MUTACION SOBRE EL ACTA REAL: le cambia una cifra al cuerpo y
     comprueba que la guarda CAE. Sin eso, un verde sobre el acta real no
     probaria que la guarda mira.

EL FICHERO DEL TURNO NO SE TOCA, Y VA DICHO PORQUE `marcador()` APUNTA SU TOQUE:
`AP.RUTA_DEL_TURNO` se redirige a un temporal durante toda la corrida y se
restaura al final, con la sede de verdad medida antes y despues. **Se olvida el
turno del temporal ANTES de restaurar la ruta**, que es la caida que este mismo
frente cometio una vez y que ya lleva su motivo escrito en el arnes.

USO:
  python scripts/loop/vuelta197_tarea2c_guarda_marcador_sobre_el_acta.py
"""
import hashlib
import io
import os
import re
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apertura_del_auditor as AP   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SALIDA = os.path.join(LOOP, "SALIDA_V197_T2C_GUARDA_MARCADOR_ACTA_197.txt")
VUELTA = "197"


def medir(ruta):
    if not os.path.isfile(ruta):
        return (False, 0, "")
    d = io.open(ruta, "rb").read()
    return (True, len(d), hashlib.sha256(d.replace(b"\r\n", b"\n")).hexdigest())


def cuerpo_del_acta(lineas, vuelta):
    """(inicio, fin) 1-indexados del cuerpo de un acta, o None. PURA.

    Se acota por la cabecera `# ACTA DEL AUDITOR, VUELTA N` y termina en la
    siguiente cabecera `# ACTA` o al final. **La linea NO se hereda de ningun
    encargo: se cuenta aqui.**"""
    ini = [i for i, l in enumerate(lineas)
           if re.match(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA %s\b" % vuelta, l)]
    if len(ini) != 1:
        return None
    i0 = ini[0]
    sig = [i for i, l in enumerate(lineas) if i > i0 and re.match(r"^#\s+ACTA\b", l)]
    return (i0 + 1, (sig[0] if sig else len(lineas)))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 197, TAREA 2.c: LA GUARDA DE LA C.A1 SOBRE EL ACTA 197 REAL")
    w("=" * 78)
    w("")

    turno_antes = medir(AP.RUTA_DEL_TURNO)
    w("0) LA SEDE DE VERDAD DEL TURNO, MEDIDA ANTES DE TOCAR NADA")
    w("   %s" % ("EXISTE, %d bytes, sha256 LF %s"
                 % (turno_antes[1], turno_antes[2][:16])
                 if turno_antes[0] else "NO EXISTE"))
    w("   SE MIDE PORQUE `marcador()` APUNTA SU TOQUE y escribiria en ella. La")
    w("   ruta se redirige a un temporal durante toda esta corrida.")
    w("")

    tmp = tempfile.mkdtemp(prefix="v197_guarda_marcador_")
    ruta_original = AP.RUTA_DEL_TURNO
    ok = True
    try:
        AP.RUTA_DEL_TURNO = os.path.join(tmp, "_TURNO_DEL_AUDITOR.json")

        w("A) LA SALIDA DE `AP.marcador()` DE ESTA VUELTA, SELLADA")
        destino, m = AP.sellar_marcador(VUELTA)
        rel = os.path.relpath(destino, RAIZ).replace(os.sep, "/")
        w("   %s (%d bytes)" % (rel, os.path.getsize(destino)))
        w("   filas: %d" % m["filas"])
        w("   por_clase: %s"
          % ", ".join("%s %d" % (k, m["por_clase"][k])
                      for k in sorted(m["por_clase"], key=lambda x: str(x))))
        w("   ESTAS CIFRAS SALEN DE CONTAR docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
        w("   POR EL CARRIL, no de ninguna tabla. Es lo que la C.A1 no hizo tres")
        w("   actas seguidas.")
        w("")

        w("B) EL CUERPO DEL ACTA %s, ACOTADO EN ESTA CORRIDA" % VUELTA)
        lineas = io.open(ACTA, encoding="utf-8", errors="replace").read().split(NL)
        rango = cuerpo_del_acta(lineas, VUELTA)
        if rango is None:
            w("   ROJO: la cabecera del acta %s no aparece exactamente una vez."
              % VUELTA)
            ok = False
            cuerpo = ""
        else:
            i0, i1 = rango
            cuerpo = NL.join(lineas[i0 - 1:i1])
            w("   lineas %d a %d (%d lineas), sobre un fichero de %d bytes"
              % (i0, i1, i1 - i0 + 1, os.path.getsize(ACTA)))
        w("")

        w("C) LA GUARDA, CORRIDA SOBRE ESE CUERPO")
        verde, informe = AP.guarda_del_marcador(cuerpo, VUELTA)
        for l in informe:
            w("   " + l)
        w("   VEREDICTO SOBRE EL ACTA REAL: %s" % ("VERDE" if verde else "ROJO"))
        ok = ok and verde
        w("")

        w("D) LA MUTACION SOBRE EL ACTA REAL, PORQUE UN VERDE SIN ELLA NO PRUEBA")
        w("   QUE LA GUARDA MIRE")
        cifras = AP.cifras_del_marcador_del_acta(cuerpo)
        w("   cifras leidas del acta: %r" % (cifras,))
        mutaciones = 0
        cayeron = 0
        if cifras:
            sucio_filas = cuerpo.replace("**%d filas" % cifras["filas"],
                                         "**%d filas" % (cifras["filas"] + 1), 1)
            mutaciones += 1
            v1, _i = AP.guarda_del_marcador(sucio_filas, VUELTA)
            cayeron += 0 if v1 else 1
            w("   filas %d -> %d: la guarda %s"
              % (cifras["filas"], cifras["filas"] + 1,
                 "DEJA PASAR (mal)" if v1 else "CAE"))
            for clase in sorted(cifras["por_clase"]):
                valor = cifras["por_clase"][clase]
                sucio = cuerpo.replace("%s %d" % (clase, valor),
                                       "%s %d" % (clase, valor + 1), 1)
                if sucio == cuerpo:
                    w("   clase %s: no se pudo mutar el literal, y SE DICE en vez"
                      % clase)
                    w("      de contarlo como caso corrido.")
                    continue
                mutaciones += 1
                v2, _i2 = AP.guarda_del_marcador(sucio, VUELTA)
                cayeron += 0 if v2 else 1
                w("   clase %s %d -> %d: la guarda %s"
                  % (clase, valor, valor + 1,
                     "DEJA PASAR (mal)" if v2 else "CAE"))
        w("   CIFRA mutaciones corridas: %d | CIFRA que CAYERON: %d"
          % (mutaciones, cayeron))
        if mutaciones == 0 or cayeron != mutaciones:
            w("   ROJO: alguna mutacion no mordio, o no hubo ninguna que correr.")
            ok = False
        w("")

        w("E) Y EL OTRO CASO ROJO: SIN LA SALIDA SELLADA, LA GUARDA CAE")
        w("   se corre sobre una base VACIA, sin borrar la sellada de verdad")
        vacio = os.path.join(tmp, "sin_salidas")
        os.makedirs(vacio)
        v3, inf3 = AP.guarda_del_marcador(cuerpo, VUELTA, base=vacio)
        for l in inf3[-3:]:
            w("   " + l)
        w("   la guarda %s" % ("DEJA PASAR (mal)" if v3 else "CAE"))
        if v3:
            ok = False
        w("")
    finally:
        AP.olvidar_todo()
        AP.RUTA_DEL_TURNO = ruta_original
        shutil.rmtree(tmp, ignore_errors=True)
        w("F) EL TEMPORAL SE RETIRA Y LA SEDE SE REMIDE (P.16)")
        turno_despues = medir(AP.RUTA_DEL_TURNO)
        w("   al entrar: %s"
          % ("EXISTE, %d bytes, sha256 LF %s"
             % (turno_antes[1], turno_antes[2][:16])
             if turno_antes[0] else "NO EXISTE"))
        w("   al salir:  %s"
          % ("EXISTE, %d bytes, sha256 LF %s"
             % (turno_despues[1], turno_despues[2][:16])
             if turno_despues[0] else "NO EXISTE"))
        igual = turno_despues == turno_antes
        w("   LA SEDE DE VERDAD NO CAMBIO: %s" % ("SI" if igual else "NO"))
        ok = ok and igual and not os.path.exists(tmp)
    w("")
    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (SALIDA, len(t.encode("utf-8"))))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
