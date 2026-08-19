# -*- coding: utf-8 -*-
"""vuelta40_guarda_puerta.py - EL CASO POSITIVO de la puerta reparada.

ESTRICTAMENTE DE SOLO LECTURA. No toca el instrumento, no toca un nodo, no
escribe ninguna cola.

POR QUE EXISTE. La puerta de `scripts/costuras_internas.py` se acaba de reparar,
y una puerta que solo se ha visto ABRIR no esta probada: hay que verla CERRAR.
Este script la empuja por los dos lados con el instrumento de verdad:

  1. CON LOS FIXTURES DE HOY, la puerta ABRE (y esa es la reparacion).
  2. CON UN FIXTURE QUE NO DISPARA, la puerta CIERRA con `CalibracionRota`, el
     diagnostico nombra al que falta Y AHORA TAMBIEN DICE QUE HACER. El fixture
     que se usa para empujarla es el RETIRADO, `plan_mejora_procesos`, que es
     precisamente el que tumbo el instrumento de verdad: o sea que la averia
     original QUEDA REPRODUCIDA A PROPOSITO, no recordada.
  3. LA PUERTA SE HEREDA POR IMPORTACION: llamar a la senal publica de un
     instrumento descalibrado revienta. Esa guarda es de la vuelta 34 y esta
     reparacion NO la afloja, asi que se vuelve a comprobar.
  4. `NO APLICA` SIGUE SIN DEJARSE COMPARAR con un umbral. Misma razon.

Uso: python scripts/loop/vuelta40_guarda_puerta.py
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))

import costuras_internas as ci  # noqa: E402

FALLOS = []


def comprueba(nombre, ok, detalle=""):
    print("  [%s] %s%s" % ("OK " if ok else "CAE", nombre,
                           (" | " + detalle) if detalle else ""))
    if not ok:
        FALLOS.append(nombre)


def main():
    from rapidfuzz.fuzz import token_sort_ratio as ratio

    print("CASO POSITIVO DE LA PUERTA DE CALIBRACION, vuelta 40, 19 ago 2026")
    print("Umbrales VIGENTES y no tocados: pareja %s, bloque %s"
          % (ci.UMBRAL_PAREJA, ci.UMBRAL_BLOQUE))
    print("")

    print("1. CON LOS FIXTURES DE HOY, LA PUERTA TIENE QUE ABRIR")
    faltan, detalle = ci.medir_calibracion(ratio)
    comprueba("los %d fixtures entran en la cola" % len(ci.CALIBRACION),
              not faltan, "faltan: %s" % (faltan or "ninguno"))
    for nid in ci.CALIBRACION:
        d = detalle[nid]
        comprueba("  fixture %s dispara" % nid, d["entra"],
                  "bloque %s, margen %s"
                  % (ci._texto_bloque(d["bloque"]),
                     ("%+.1f" % d["margen"]) if d["margen"] is not None else "NO APLICA"))
    anchos = [n for n in ci.CALIBRACION
              if (detalle[n]["margen"] or 0) >= 10.0]
    comprueba("criterio 3, al menos un fixture con margen amplio (10 puntos o mas)",
              bool(anchos), "los que cumplen: %s" % anchos)
    comprueba("criterio 3, mas de un fixture", len(ci.CALIBRACION) > 1,
              "son %d" % len(ci.CALIBRACION))
    por_bloque = [n for n in ci.CALIBRACION
                  if detalle[n]["margen"] is not None and detalle[n]["margen"] >= 0]
    comprueba("criterio 2, todos entran por la senal de BLOQUE",
              len(por_bloque) == len(ci.CALIBRACION), "%d de %d"
              % (len(por_bloque), len(ci.CALIBRACION)))
    print("")

    print("2. CON UN FIXTURE QUE NO DISPARA, LA PUERTA TIENE QUE CERRAR")
    print("   (se empuja con el RETIRADO plan_mejora_procesos: la averia de")
    print("    verdad, REPRODUCIDA a proposito y no recordada)")
    guardado_cal, guardado_estado = ci.CALIBRACION, ci._CALIBRACION
    try:
        ci.CALIBRACION = guardado_cal + ("plan_mejora_procesos",)
        ci._CALIBRACION = None
        cerro = False
        try:
            ci._asegurar_calibracion()
        except ci.CalibracionRota as err:
            cerro = True
            comprueba("la puerta CIERRA y nombra al que falta",
                      err.faltan == ["plan_mejora_procesos"], "faltan: %s" % err.faltan)
            comprueba("la excepcion lleva la medicion dentro",
                      "plan_mejora_procesos" in err.detalle,
                      "bloque %s" % ci._texto_bloque(
                          err.detalle["plan_mejora_procesos"]["bloque"]))
            print("   EL DIAGNOSTICO ENTERO, tal como lo veria quien lo corra:")
            print("   " + "-" * 68)
            salida = io.StringIO()
            atras, sys.stdout = sys.stdout, salida
            try:
                ci.imprimir_calibracion_rota(err)
            finally:
                sys.stdout = atras
            texto = salida.getvalue()
            for linea in texto.rstrip("\n").split("\n"):
                print("   | " + linea)
            print("   " + "-" * 68)
            comprueba("el diagnostico dice QUE HACER (anadido en la vuelta 40)",
                      "NO se afloja el umbral" in texto)
            comprueba("el diagnostico manda RETIRAR DECLARADO, no bajar el umbral",
                      "RETIRA DECLARADO" in texto)
        comprueba("la puerta NO se dejo pasar", cerro)

        print("")
        print("3. LA PUERTA SE HEREDA POR IMPORTACION (guarda de la vuelta 34)")
        ci._CALIBRACION = None
        reviento = False
        try:
            ci.peor_pareja(ratio, ["uno", "dos", "tres"])
        except ci.CalibracionRota:
            reviento = True
        comprueba("la senal publica peor_pareja revienta con la puerta cerrada",
                  reviento)
        ci._CALIBRACION = None
        reviento = False
        try:
            ci.mejor_bloque(ratio, ["uno", "dos", "tres", "cuatro"])
        except ci.CalibracionRota:
            reviento = True
        comprueba("la senal publica mejor_bloque revienta con la puerta cerrada",
                  reviento)
    finally:
        ci.CALIBRACION, ci._CALIBRACION = guardado_cal, guardado_estado

    print("")
    print("4. NO APLICA SIGUE SIN DEJARSE COMPARAR (guarda de la vuelta 34)")
    for nombre, fn in (("comparar con >=", lambda: ci.NO_APLICA >= 44),
                       ("convertir a float", lambda: float(ci.NO_APLICA)),
                       ("usar como booleano", lambda: bool(ci.NO_APLICA))):
        reviento = False
        try:
            fn()
        except TypeError:
            reviento = True
        comprueba("NO APLICA revienta al %s" % nombre, reviento)
    comprueba("y NO APLICA se sigue imprimiendo con su texto",
              str(ci.NO_APLICA) == "NO APLICA", str(ci.NO_APLICA))

    print("")
    print("5. LA PUERTA VUELVE A ESTAR COMO ESTABA tras el empuje")
    faltan2, _ = ci.medir_calibracion(ratio)
    comprueba("los fixtures de hoy siguen entrando", not faltan2,
              "faltan: %s" % (faltan2 or "ninguno"))
    comprueba("la lista de fixtures quedo intacta",
              ci.CALIBRACION == guardado_cal, str(ci.CALIBRACION))

    print("")
    if FALLOS:
        print("CAEN %d COMPROBACIONES: %s" % (len(FALLOS), FALLOS))
        return 1
    print("TODAS LAS COMPROBACIONES EN VERDE. La puerta abre cuando debe y "
          "cierra cuando debe.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
