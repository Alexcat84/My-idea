# -*- coding: utf-8 -*-
r"""vuelta143_2b_mutacion_bateria.py . LA PRUEBA DE MUTACION DE LA TAREA 2.b de
la vuelta 143 (acta de la vuelta 142, adjudicacion 3.2 y caida 4.4 de la casa).

LO QUE EL ENCARGO PIDE, LITERAL: "rompe a proposito el caso fabricado y
comprueba que la bateria lo marca."

QUE SE ROMPE, Y POR QUE ESE Y NO OTRO. El caso fabricado del 2.a.ii mete EN
MEMORIA la vuelta de una direccion elegida por computo (el `poner_arista` del
PASO A) y luego la quita (el PASO B). Si esa inyeccion NO SE HACE, el caso se
queda sin defecto que probar: el PASO A saldria con la operacion ya cumplida y
el arnes tiene que cantarlo. La mutacion, por tanto, borra de una COPIA del
fichero la linea que inyecta la vuelta fabricada, y comprueba que la bateria de
mutaciones CAE (exit distinto de 0) nombrando su comprobacion.

TRES CASOS, todos SOBRE EL EJECUTABLE y con la cifra leida de la salida real,
nunca contra un literal (EJECUTOR.md regla 1):

  (a) CONTRAPRUEBA: el fichero SIN mutar sale VERDE exit 0, y su salida declara
      que el sujeto es FABRICADO (o sea, que la mutacion tiene algo que romper).
  (b) MUTACION: sobre una COPIA con la inyeccion de la vuelta fabricada
      borrada, la bateria tiene que CAER, y la comprobacion que cae tiene que
      ser una del bloque 2.a.ii.
  (c) LA CIFRA DE COMPROBACIONES BAJA O EL VEREDICTO CAMBIA, computado de las
      dos salidas: verdes en la corrida limpia contra verdes en la mutada.

P.16, QUIEN FABRICA LIMPIA: la copia se borra en el `finally` y el fichero real
no se toca nunca.

USO:
  python scripts/loop/vuelta143_2b_mutacion_bateria.py
"""
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))

REAL = os.path.join(AQUI, "vuelta141_2_mutaciones.py")
COPIA = os.path.join(AQUI, "_prueba_v143_2b_bateria.py")

LINEA_INYECCION = "        poner_arista(nodos_iia, res_iia, rd_f, ro_f)\n"
RE_VERDES = re.compile(r"comprobaciones corridas: (\d+) \| verdes: (\d+)")


def corre(ruta):
    r = subprocess.run([sys.executable, ruta], cwd=RAIZ, capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=900)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def verdes_de(texto):
    m = RE_VERDES.search(texto)
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    resultados = []
    try:
        print("=" * 78)
        print("MUTACION DE LA TAREA 2.b | vuelta 143")
        print("Se rompe A PROPOSITO el caso fabricado del 2.a.ii y se comprueba que la")
        print("bateria lo marca. Todo sobre una COPIA; el fichero real no se toca.")
        print("=" * 78)

        # ---------------- (a) CONTRAPRUEBA SIN MUTAR ------------------------
        codigo_a, salida_a = corre(REAL)
        corridas_a, verdes_a = verdes_de(salida_a)
        fabricado = "SUJETO FABRICADO EN MEMORIA" in salida_a
        ok = (codigo_a == 0) and fabricado and (corridas_a is not None) \
            and (corridas_a == verdes_a)
        resultados.append(("a CONTRAPRUEBA sin mutar: la bateria sale VERDE exit 0 y su "
                           "sujeto del 2.a.ii es FABRICADO EN MEMORIA (o sea, hay algo que "
                           "romper)", ok))
        print("")
        print("(a) exit %s | comprobaciones %s | verdes %s | sujeto fabricado: %s"
              % (codigo_a, corridas_a, verdes_a, fabricado))

        # ---------------- (b) SE ROMPE EL CASO FABRICADO --------------------
        fuente = io.open(REAL, encoding="utf-8").read()
        if LINEA_INYECCION not in fuente:
            print("ROJO (arnes): no se halla la linea que inyecta la vuelta fabricada. Sin "
                  "sujeto que romper no hay mutacion, y ESO ES ROJO.")
            return 1
        io.open(COPIA, "w", encoding="utf-8", newline="\n").write(
            fuente.replace(LINEA_INYECCION, ""))
        codigo_b, salida_b = corre(COPIA)
        corridas_b, verdes_b = verdes_de(salida_b)
        cae_en_2aii = bool(re.search(r"ROJO\s+2\.a\.ii", salida_b))
        ok = (codigo_b != 0) and cae_en_2aii
        resultados.append(("b rota la inyeccion de la vuelta fabricada, la bateria CAE y la "
                           "comprobacion que cae es del bloque 2.a.ii", ok))
        print("")
        print("(b) exit %s | comprobaciones %s | verdes %s | cae una del 2.a.ii: %s"
              % (codigo_b, corridas_b, verdes_b, cae_en_2aii))
        for linea in salida_b.splitlines():
            if linea.strip().startswith("ROJO "):
                print("    %s" % linea.strip())

        # ---------------- (c) LA CIFRA DE VERDES BAJA -----------------------
        ok = (verdes_a is not None) and (verdes_b is not None) and (verdes_b < verdes_a)
        resultados.append(("c la cifra de comprobaciones VERDES baja al romper el caso "
                           "(%s contra %s)" % (verdes_b, verdes_a), ok))
        print("")
        print("(c) verdes limpias %s | verdes con el caso roto %s" % (verdes_a, verdes_b))
    finally:
        if os.path.exists(COPIA):
            os.remove(COPIA)

    print("")
    print("=" * 78)
    verdes = 0
    for nombre, ok in resultados:
        print("  %-5s %s" % ("VERDE" if ok else "ROJO", nombre))
        verdes += 1 if ok else 0
    print("CIFRA de la bateria 2.b: %d comprobaciones" % len(resultados))
    print("CIFRA verdes de la bateria 2.b: %d comprobaciones" % verdes)
    print("=" * 78)
    if verdes != len(resultados):
        print("ROJO: %d de %d casos no se comportan." % (len(resultados) - verdes, len(resultados)))
        return 1
    print("VERDE: los %d casos se comportan." % len(resultados))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
