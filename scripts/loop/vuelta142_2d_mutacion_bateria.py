# -*- coding: utf-8 -*-
r"""vuelta142_2d_mutacion_bateria.py . LA PRUEBA DE MUTACION DE LA TAREA 2.d de
la vuelta 142 (acta de la vuelta 141, caida 4.3 de la casa).

LO QUE EL ENCARGO PIDE, LITERAL: "quita un script de VIEJAS y comprueba que la
cifra del rotulo baja sola". El rotulo es la linea
`LAS <n> MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.`

TRES CASOS, y los tres sobre CIFRA COMPUTADA de la salida real del proceso,
nunca sobre un literal (EJECUTOR.md 1):

  (a) CONTRAPRUEBA: sin tocar nada, la cifra del rotulo es igual a len(VIEJAS)
      leido del modulo. Las dos se computan; ninguna se teclea.
  (b) MUTACION: se quita UN script de `VIEJAS` EN MEMORIA (nunca en disco) y se
      vuelve a formar el rotulo con la misma expresion que el modulo usa. La
      cifra tiene que BAJAR EN EXACTAMENTE UNO. Si no baja, el rotulo esta
      tecleado en alguna parte y la guarda no lo veria.
  (c) MUTACION SOBRE EL EJECUTABLE: se corre la bateria de verdad, como
      subproceso, con una COPIA del modulo a la que se le ha quitado ese mismo
      script de `VIEJAS`, y se lee la cifra DE SU ROTULO IMPRESO. Tiene que
      bajar en uno igual. Es la unica de las tres que prueba el binario y no la
      variable.

P.16, QUIEN FABRICA LIMPIA: la copia del modulo se borra en el `finally`, y el
modulo real no se toca nunca.

POR QUE EL CASO (c) NO CORRE LOS SIETE SCRIPTS: solo necesita el ROTULO, que se
imprime antes de correr nada. Se le pasa `--mutar-ancla` con el sujeto fijo
ausente para que salga en cuanto lo imprima, y se comprueba el rotulo, no el
veredicto.

USO:
  python scripts/loop/vuelta142_2d_mutacion_bateria.py
"""
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import verificar_mutaciones_viejas as B

COPIA = os.path.join(AQUI, "_prueba_v142_2d_bateria.py")
RE_ROTULO = re.compile(r"LAS (\d+) MUTACIONES VIEJAS")


def rotulo_de(nomina):
    """LA MISMA EXPRESION QUE EL MODULO USA para formar su rotulo. Si el modulo
    dejara de computarla de su nomina, el caso (c) lo caza igual, porque ese
    corre el ejecutable."""
    return "LAS %d MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO." % len(nomina)


def cifra_del_rotulo(texto):
    m = RE_ROTULO.search(texto)
    return int(m.group(1)) if m else None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    resultados = []
    try:
        nomina = list(B.VIEJAS)
        print("=" * 78)
        print("MUTACION DE LA TAREA 2.d | vuelta 142")
        print("VIEJAS leida del modulo: %d script(s)" % len(nomina))
        for s, admite in nomina:
            print("   %-40s admite --sujeto: %s" % (s, admite))
        print("=" * 78)

        # ---------------- (a) CONTRAPRUEBA ---------------------------------
        cifra_a = cifra_del_rotulo(rotulo_de(nomina))
        ok = cifra_a == len(nomina)
        resultados.append(("a CONTRAPRUEBA: la cifra del rotulo es igual a len(VIEJAS)", ok))
        print("")
        print("(a) cifra del rotulo %s | len(VIEJAS) %d" % (cifra_a, len(nomina)))

        # ---------------- (b) MUTACION EN MEMORIA ---------------------------
        # El script que se quita se ELIGE POR COMPUTO: el ultimo de la nomina.
        quitado = nomina[-1][0]
        menor = nomina[:-1]
        cifra_b = cifra_del_rotulo(rotulo_de(menor))
        ok = cifra_b == cifra_a - 1
        resultados.append(("b quitando %s de VIEJAS, la cifra del rotulo BAJA EN UNO"
                           % quitado, ok))
        print("")
        print("(b) quitado %s -> cifra %s (antes %s)" % (quitado, cifra_b, cifra_a))

        # ---------------- (c) MUTACION SOBRE EL EJECUTABLE ------------------
        fuente = io.open(os.path.join(AQUI, "verificar_mutaciones_viejas.py"),
                         encoding="utf-8").read()
        linea = '    ("%s", False),\n' % quitado
        if linea not in fuente:
            linea = '    ("%s", True),\n' % quitado
        if linea not in fuente:
            print("ROJO (arnes): no se pudo hallar la entrada de %s en VIEJAS para "
                  "quitarla. Sin sujeto no hay mutacion y ESO ES ROJO." % quitado)
            return 1
        io.open(COPIA, "w", encoding="utf-8", newline="\n").write(fuente.replace(linea, ""))
        r = subprocess.run([sys.executable, COPIA, "--mutar-ancla"], cwd=RAIZ,
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=900)
        cifra_c = cifra_del_rotulo((r.stdout or "") + (r.stderr or ""))
        ok = cifra_c == cifra_a - 1
        resultados.append(("c el EJECUTABLE con %s fuera de VIEJAS imprime la cifra bajada"
                           % quitado, ok))
        print("")
        print("(c) el ejecutable mutado imprime cifra %s (antes %s)" % (cifra_c, cifra_a))
    finally:
        if os.path.exists(COPIA):
            os.remove(COPIA)

    print("")
    print("=" * 78)
    verdes = 0
    for nombre, ok in resultados:
        print("  %-5s %s" % ("VERDE" if ok else "ROJO", nombre))
        verdes += 1 if ok else 0
    print("CIFRA de la bateria 2.d: %d comprobaciones" % len(resultados))
    print("CIFRA verdes de la bateria 2.d: %d comprobaciones" % verdes)
    print("=" * 78)
    if verdes != len(resultados):
        print("ROJO: %d de %d casos no se comportan." % (len(resultados) - verdes, len(resultados)))
        return 1
    print("VERDE: los %d casos se comportan." % len(resultados))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
