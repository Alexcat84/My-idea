# -*- coding: utf-8 -*-
r"""vuelta193_tarea5d_rehacer_cotejo_auditor.py . EL COTEJO DEL AUDITOR DE LA 193,
RE ESCRITO CON EL INSTRUMENTO ARREGLADO Y COTEJADO CONTRA LO QUE EL PUBLICA A
MANO.

ES LA PIEZA `d` DE LA TAREA 5 DE LA VUELTA 193, sobre el hallazgo `5.2` del acta
193. `cuerpo_del_cotejo()` hacia `bool(du)`, y **`bool("no")` es `True`**: el
auditor llamo a la columna con las formas que el propio docstring del formato
especifica, `si` y `no`, y el instrumento le publico **`discrepancias FUERA de
los dudosos: 0 (ninguna)` teniendo DOS**.

QUE HACE, Y ES DELIBERADAMENTE EL CAMINO QUE REVENTABA:

  1. lee las 30 filas del fichero del auditor, `docs/loop/_auditor_v193_cotejo.txt`,
  2. le pasa `en dudosos` **COMO TEXTO `si` / `no`**, que es la forma que rompia,
     y NO como booleano,
  3. lo re escribe con el instrumento arreglado,
  4. y coteja el resultado contra **lo que el auditor publica a mano**: 30
     cotejados, 25 coinciden, 5 discrepan, 3 dentro (`965`, `1068`, `1814`) y 2
     fuera (`1804`, `2833`).

**Y CORRE ADEMAS EL CAMINO VIEJO**, aplicando `bool()` a esos mismos textos, para
que la diferencia sea una MEDICION y no una afirmacion.

**LO QUE NO HACE:** no toca el fichero del auditor. Escribe el suyo aparte, con
su nombre y su vuelta, que es lo que la casa hace con un corte nuevo.

USO:
  python scripts/loop/vuelta193_tarea5d_rehacer_cotejo_auditor.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cotejo_de_ciega as C   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

FUENTE = "docs/loop/_auditor_v193_cotejo.txt"
DESTINO = "docs/loop/SALIDA_V193_T5D_COTEJO_AUDITOR_REHECHO.txt"

# LO QUE EL AUDITOR PUBLICA A MANO, TECLEADO AQUI **A PROPOSITO Y COMO SUJETO DE
# LA COMPROBACION**, no como cifra publicada: es la vara contra la que se coteja
# lo que salga, y el encargo la escribe con estas palabras. Si no calzara, lo que
# se publica es la discrepancia, no una de las dos.
ESPERADO = {
    "total": 30, "coinciden": 25, "discrepan": 5,
    "disc_dentro": [965, 1068, 1814], "disc_fuera": [1804, 2833],
}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("VUELTA 193, TAREA 5.d: EL COTEJO DEL AUDITOR, RE ESCRITO CON EL")
    w("INSTRUMENTO ARREGLADO")
    w("=" * 78)
    w("")

    ruta = os.path.join(RAIZ, FUENTE.replace("/", os.sep))
    if not os.path.isfile(ruta):
        w("ROJO: no existe %s" % FUENTE)
        print(NL.join(L))
        return 1
    texto = io.open(ruta, encoding="utf-8", errors="replace").read()
    filas_leidas = C.filas_del_cotejo(texto)
    w("A) EL FICHERO DEL AUDITOR, LEIDO Y NO TOCADO")
    w("   %s -> disco %d bytes" % (FUENTE, os.path.getsize(ruta)))
    w("   CIFRA filas legibles: %d" % len(filas_leidas))
    ok_d, dec, cont, motivo = C.denominador(texto)
    w("   su propia guarda del denominador: declarado %s | contado %d | %s"
      % (dec, cont, motivo))
    if not filas_leidas:
        w("ROJO: no se pudo leer ninguna fila.")
        print(NL.join(L))
        return 1
    w("")

    w("B) LAS FILAS, RE ARMADAS CON `en dudosos` COMO TEXTO `si` / `no`")
    w("   (ES EL CAMINO QUE REVENTABA, A PROPOSITO: el auditor llamo a la columna")
    w("    con las formas que el docstring del formato especifica, y esas son")
    w("    justo las que `bool()` convertia todas en `si`)")
    filas_texto = [(p, cl, ca, "si" if du else "no")
                   for p, cl, ca, du, _v in filas_leidas]
    w("   CIFRA filas con `si` en texto: %d"
      % len([1 for f in filas_texto if f[3] == "si"]))
    w("   CIFRA filas con `no` en texto: %d"
      % len([1 for f in filas_texto if f[3] == "no"]))
    w("")

    w("C) EL CAMINO VIEJO, CORRIDO AQUI PARA QUE LA DIFERENCIA SEA UNA MEDICION")
    viejos = [bool(f[3]) for f in filas_texto]
    w("   `bool()` sobre los 30 textos da `si` en %d de %d"
      % (len([1 for v in viejos if v]), len(viejos)))
    disc_viejo_fuera = [f[0] for f, v in zip(filas_texto, viejos)
                        if not v and C.veredicto_de(f[1], f[2]) == "DISCREPA"]
    w("   con esa lectura, las discrepancias FUERA de los dudosos serian: %d (%s)"
      % (len(disc_viejo_fuera),
         ", ".join(str(x) for x in disc_viejo_fuera) or "ninguna"))
    w("   Y ESA ES LA CIFRA QUE EL INSTRUMENTO LE PUBLICO AL AUDITOR.")
    w("")

    w("D) EL CAMINO DE HOY, CON `normalizar_en_dudosos()`")
    cabecera = [
        "=" * 78,
        "COTEJO DE CIEGA DEL AUDITOR DE LA VUELTA 193, RE ESCRITO POR EL EJECUTOR",
        "DE LA 193 CON `cotejo_de_ciega.py` YA ARREGLADO (TAREA 5.d).",
        "FUENTE de las filas: %s, que NO se toca." % FUENTE,
        "LAS CLASES SON DEL AUDITOR Y NO MIAS: aqui no se re lee ninguna ciega,",
        "solo se re escribe el cotejo con el instrumento reparado.",
        "`en dudosos` va pasado COMO TEXTO `si` / `no`, que es la forma que",
        "`bool(du)` convertia toda en `si`.",
    ]
    destino = os.path.join(RAIZ, DESTINO.replace("/", os.sep))
    ok_esc, informe = C.escribir_cotejo(destino, cabecera, filas_texto)
    for l in informe:
        w("   " + l)
    ok &= ok_esc
    w("")

    w("E) LAS CIFRAS, COTEJADAS CONTRA LO QUE EL AUDITOR PUBLICA A MANO")
    releido = io.open(destino, encoding="utf-8").read()
    r = C.resumen(C.filas_del_cotejo(releido))
    for clave in ("total", "coinciden", "discrepan"):
        calza = r[clave] == ESPERADO[clave]
        ok &= calza
        w("   %-12s obtenido %-4d esperado %-4d -> %s"
          % (clave, r[clave], ESPERADO[clave], "CALZA" if calza else "NO CALZA"))
    for clave in ("disc_dentro", "disc_fuera"):
        calza = sorted(r[clave]) == sorted(ESPERADO[clave])
        ok &= calza
        w("   %-12s obtenido %-22s esperado %-22s -> %s"
          % (clave, r[clave], ESPERADO[clave], "CALZA" if calza else "NO CALZA"))
    w("   CIFRA en los dudosos del lector: %d" % r["dudosos"])
    w("")

    w("F) LA MUTACION QUE SEPARA LOS DOS CAMINOS")
    if len(disc_viejo_fuera) == len(ESPERADO["disc_fuera"]):
        w("   LA MUTACION NO CAYO: el camino viejo da la misma cifra de FUERA.")
        ok = False
    else:
        w("   LA MUTACION CAE: el camino viejo publica %d discrepancias FUERA y"
          % len(disc_viejo_fuera))
        w("   el de hoy publica %d (%s). La regla de parada de AUDITOR.md 1.2"
          % (len(r["disc_fuera"]),
             ", ".join(str(x) for x in sorted(r["disc_fuera"]))))
        w("   cuelga de esa cifra, asi que el camino viejo publicaba un VERDE")
        w("   donde habia una escalada.")
    w("")

    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    salida = os.path.join(LOOP, "SALIDA_V193_T5D_REHACER_COTEJO.txt")
    io.open(salida, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V193_T5D_REHACER_COTEJO.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
