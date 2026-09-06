# -*- coding: utf-8 -*-
r"""vuelta191_tarea6_mutacion_bloque_tallado.py . EL CASO POSITIVO POR MUTACION DE
LA EXENCION DEL BLOQUE DE LA CABECERA TALLADA.

QUE SE CAMBIO Y POR QUE, DICHO SIN ADORNO. `cifras_sin_pareja()` deja fuera los
bloques cercados **porque son citas de la salida de un instrumento**, y desde esta
vuelta deja fuera tambien el bloque `<!-- CABECERA TALLADA -->` por el MISMO
motivo. La causa esta medida: **el asunto del commit del acta 190 trae dentro
`961248 bytes` y un `sha256`**, y ese asunto lo cita literal la fila de identidad
que produce `tallar_cabecera_reporte.py`. El reporte no afirma esas cifras: las
cita, y este fichero escribe encima del bloque que la tabla va *"PEGADA ENTERA DEL
FICHERO QUE LA LLEVA Y NO TECLEADA"*.

ESTO ES UNA EXENCION Y SE PRUEBA COMO TAL, no se afirma. **Un arnes que solo
comprobara que el reporte de hoy pasa no probaria nada**: lo que hay que probar es
que la exencion NO alcanza a la prosa del ejecutor y que el bloque solo se exime
cuando se puede DELIMITAR. Los cuatro casos:

  1. una cifra sin pareja EN LA PROSA sigue siendo ROJO,
  2. la misma cifra DENTRO del bloque tallado ya no lo es,
  3. si falta una de las dos marcas, **no se exime nada** y la cifra vuelve a ser
     ROJO: un bloque que no se puede delimitar no se puede eximir,
  4. la exencion tiene un tamano medible y no es "todo el documento".

Y LO QUE NO SE PIERDE, DICHO CON SU NOMBRE: el contenido de ese bloque lo vigila
`--comparar`, que exige que sea IDENTICO BYTE A BYTE al fichero del tallador. Este
arnes lo corre tambien, sobre el reporte de verdad.

USO:
  python scripts/loop/vuelta191_tarea6_mutacion_bloque_tallado.py
"""
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
SALIDA = os.path.join(LOOP, "SALIDA_V191_T6_MUTACION_BLOQUE_TALLADO.txt")

# LA CIFRA FABRICADA. Va SIN pareja a proposito: una sola aparicion de `bytes` y
# una sola marca de convencion.
CIFRA = "el fichero mide 961248 bytes segun LF"


def documento(prosa_con_cifra, dentro_del_bloque, abre=True, cierra=True):
    """UN REPORTE FABRICADO. PURA. No se toca el repo para probar."""
    L = ["# REPORTE DE LA VUELTA 999 (fabricado para el arnes).", ""]
    if prosa_con_cifra:
        L.append("Prosa del ejecutor: " + CIFRA)
        L.append("")
    if abre:
        L.append(CR.MARCA_ABRE)
    if dentro_del_bloque:
        L.append("| una fila de la tabla tallada | " + CIFRA + " |")
    if cierra:
        L.append(CR.MARCA_CIERRA)
    L.append("")
    return NL.join(L) + NL


def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    w("   %-56s obtenido %-10s esperado %-10s -> %s"
      % (nombre, repr(obtenido)[:10], repr(esperado)[:10], "PASA" if ok else "CAE"))
    return 0 if ok else 1


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    fallos = 0
    no_cayeron = 0
    w("=" * 78)
    w("VUELTA 191, TAREA 6: MUTACION DE LA EXENCION DEL BLOQUE DE LA CABECERA")
    w("TALLADA EN `cifras_sin_pareja()`")
    w("=" * 78)
    w("")

    w("A) LOS CUATRO CASOS, SOBRE DOCUMENTOS FABRICADOS")
    d_prosa = documento(True, False)
    d_bloque = documento(False, True)
    d_los_dos = documento(True, True)
    d_sin_cierre = documento(False, True, cierra=False)
    fallos += _caso(w, "1. la cifra EN LA PROSA sigue siendo ROJO",
                    len(CR.cifras_sin_pareja(d_prosa)), 1)
    fallos += _caso(w, "2. la misma cifra DENTRO del bloque ya no lo es",
                    len(CR.cifras_sin_pareja(d_bloque)), 0)
    fallos += _caso(w, "   y con las dos a la vez, solo cuenta la de la prosa",
                    len(CR.cifras_sin_pareja(d_los_dos)), 1)
    fallos += _caso(w, "3. sin la marca de cierre NO se exime nada",
                    len(CR.cifras_sin_pareja(d_sin_cierre)), 1)
    w("")

    w("B) LAS MUTACIONES, CORRIDAS Y NO AFIRMADAS")
    w("   MUTACION 1: si la exencion alcanzara a la prosa, este arnes no probaria")
    w("   nada y la guarda seria un adorno")
    en_prosa = CR.cifras_sin_pareja(d_prosa)
    if not en_prosa:
        w("      LA MUTACION NO CAYO: la prosa tambien queda exenta.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: la prosa sigue dando %d fallo(s), o sea que la"
          % len(en_prosa))
        w("      exencion NO alcanza a lo que el ejecutor escribe.")
    w("   MUTACION 2: si el bloque NO estuviera exento, la misma cifra daria rojo")
    w("   dentro. Se comprueba corriendo la delimitacion sobre el mismo texto")
    dentro = CR.lineas_del_bloque_tallado(d_bloque)
    w("      lineas que la delimitacion exime: %d (%s)"
      % (len(dentro), ", ".join(str(x) for x in sorted(dentro))))
    if not dentro:
        w("      LA MUTACION NO CAYO: no exime ninguna linea, asi que el caso 2")
        w("      pasaba por otra razon.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: exime %d linea(s) y son las del bloque, no el"
          % len(dentro))
        w("      documento entero.")
    w("   MUTACION 3: un bloque con la marca de apertura DUPLICADA no se puede")
    w("   delimitar, y entonces no se exime nada")
    d_doble = d_bloque.replace(CR.MARCA_ABRE, CR.MARCA_ABRE + NL + CR.MARCA_ABRE, 1)
    dob = CR.lineas_del_bloque_tallado(d_doble)
    fallos += _caso(w, "   con la marca duplicada: lineas eximidas", len(dob), 0)
    if dob:
        w("      LA MUTACION NO CAYO: exime %d lineas sobre un bloque ambiguo."
          % len(dob))
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: 0 lineas eximidas, y la cifra de dentro vuelve a")
        w("      contar: %d fallo(s)." % len(CR.cifras_sin_pareja(d_doble)))
    w("")

    w("C) EL TAMANO DE LA EXENCION SOBRE EL REPORTE DE VERDAD, MEDIDO")
    ruta = os.path.join(LOOP, "REPORTE.md")
    if not os.path.isfile(ruta):
        w("   NO EXISTE docs/loop/REPORTE.md. Este bloque queda SIN CORRER.")
    else:
        t = io.open(ruta, encoding="utf-8", errors="replace").read()
        total = t.replace(chr(13) + NL, NL).count(NL)
        eximidas = CR.lineas_del_bloque_tallado(t)
        w("   docs/loop/REPORTE.md -> %d saltos de linea" % total)
        w("   CIFRA lineas eximidas por el bloque tallado: %d" % len(eximidas))
        w("   o sea el %.2f por ciento del documento"
          % (100.0 * len(eximidas) / total if total else 0.0))
        w("   CIFRA cifras sin pareja que quedan: %d" % len(CR.cifras_sin_pareja(t)))
        for n, esp, muestra, linea in CR.cifras_sin_pareja(t):
            w("      linea %-5d %-6s %-14s | %s" % (n, esp, muestra, linea[:90]))
    w("")

    w("D) LA GUARDA QUE SI VIGILA ESE BLOQUE, CORRIDA SOBRE EL REPORTE DE VERDAD")
    w("   (la exencion no pierde cobertura: `--comparar` exige que el bloque sea")
    w("    IDENTICO BYTE A BYTE al fichero del tallador)")
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, "scripts/loop/tallar_cabecera_reporte.py",
                        "--comparar", "docs/loop/REPORTE.md",
                        "--fase04", "--vuelta", "191"],
                       cwd=RAIZ, capture_output=True, env=env)
    sal = (r.stdout.decode("utf-8", errors="replace")
           + r.stderr.decode("utf-8", errors="replace"))
    for l in sal.replace(chr(13) + NL, NL).split(NL):
        if l.strip():
            w("      | " + l.rstrip()[:150])
    w("   exitcode de --comparar: %d" % r.returncode)
    w("   (si el reporte todavia no esta cerrado, este bloque dice lo que dice y")
    w("    no se maquilla: la corrida buena es la del cierre)")
    w("")

    w("=" * 78)
    w("CIFRA casos que CAEN: %d" % fallos)
    w("CIFRA mutaciones que NO cayeron (y deberian): %d" % no_cayeron)
    w("VEREDICTO: %s" % ("ROJO" if (fallos or no_cayeron) else "VERDE"))
    texto = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: docs/loop/SALIDA_V191_T6_MUTACION_BLOQUE_TALLADO.txt (%d bytes)"
          % len(texto.encode("utf-8")))
    return 1 if (fallos or no_cayeron) else 0


if __name__ == "__main__":
    sys.exit(main())
