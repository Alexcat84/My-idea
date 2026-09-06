# -*- coding: utf-8 -*-
r"""vuelta193_tarea3f_que_cambia_la_vara.py . QUE CAMBIA LA VARA `9.6.1` SOBRE LO
QUE YA ESTABA MEDIDO, CONTADO DE SUS FICHEROS Y NO TECLEADO.

ES LA PIEZA `f` DE LA TAREA 3 DE LA VUELTA 193: *"PUBLICA LO QUE LA VARA NUEVA
CAMBIA: cuantos de tus dudosos y de tus discrepancias habrian salido distinto con
`9.6.1`. Si no cambia nada, DILO, que tambien es un dato y me dejaria a mi con
una adjudicacion floja."*

DE DONDE SALE CADA CIFRA, Y NINGUNA DE ESTE FICHERO:

  . mi tanda de la 192, de `docs/loop/SALIDA_V192_T2_COTEJO.txt`, leida con
    `filas_del_cotejo()` del formato unico;
  . mi tanda de la 193, de `docs/loop/SALIDA_V193_T3_COTEJO.txt`, la primera
    leida ENTERA con la vara del banco;
  . y los TRES veredictos que el acta 193 adjudica en su `4.9`, que van
    tecleados aqui **como sujeto de la comprobacion y no como cifra publicada**,
    con el numero de la adjudicacion al lado.

LO QUE ESTE FICHERO NO HACE: no re lee ninguna ciega, no toca ninguna clase y no
re clasifica la tanda de la 192. **Una re lectura de la 192 con la vara nueva
seria otra ciega, y una ciega que se lee sabiendo el destape no prueba nada.** Lo
que se puede decir sin volver a leer es lo que se dice: cuales de mis
discrepancias caen DENTRO del alcance de la vara, y cual es su alcance medido.

USO:
  python scripts/loop/vuelta193_tarea3f_que_cambia_la_vara.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cotejo_de_ciega as C   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

COTEJO_192 = "docs/loop/SALIDA_V192_T2_COTEJO.txt"
COTEJO_193 = "docs/loop/SALIDA_V193_T3_COTEJO.txt"

# LOS TRES VEREDICTOS QUE EL ACTA 193 ADJUDICA EN SU `4.9`. Van tecleados aqui
# **como sujeto de la comprobacion**, con su numero delante, y NO como cifra
# publicada: lo que se publica es el cruce contra mi fichero de la 192.
VARA_DEL_ACTA = {1804: "D", 2833: "D", 1068: "A"}

# LAS CLASES QUE LA VARA `9.6.1` SABE EMITIR, LEIDAS DE SU PROPIO LITERAL. La
# frase tiene DOS salidas y nada mas: REPITE y CONTINUA.
CLASES_DE_LA_VARA = ("A", "D")


def leer(rel):
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(ruta):
        return None
    return io.open(ruta, encoding="utf-8", errors="replace").read()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 193, TAREA 3.f: QUE CAMBIA LA VARA 9.6.1 SOBRE LO YA MEDIDO")
    w("=" * 78)
    w("")

    t192 = leer(COTEJO_192)
    t193 = leer(COTEJO_193)
    if t192 is None or t193 is None:
        w("ROJO: falta alguno de los dos cotejos.")
        print(NL.join(L))
        return 1
    f192 = C.filas_del_cotejo(t192)
    f193 = C.filas_del_cotejo(t193)

    w("A) MI TANDA DE LA 192, LEIDA DE SU FICHERO")
    w("   %s -> %d filas" % (COTEJO_192, len(f192)))
    r192 = C.resumen(f192)
    w("   coinciden %d | discrepan %d | dudosos %d"
      % (r192["coinciden"], r192["discrepan"], r192["dudosos"]))
    w("   discrepancias DENTRO: %s" % r192["disc_dentro"])
    w("   discrepancias FUERA:  %s" % r192["disc_fuera"])
    w("   REPARTO DEL LECTOR:  %s"
      % ", ".join("%s %d" % (k, r192["reparto_lector"][k])
                  for k in sorted(r192["reparto_lector"])))
    w("   REPARTO DEL ARCHIVO: %s"
      % ", ".join("%s %d" % (k, r192["reparto_archivo"][k])
                  for k in sorted(r192["reparto_archivo"])))
    w("")

    w("B) LAS DIEZ DISCREPANCIAS DE LA 192, UNA A UNA, CONTRA EL ALCANCE DE LA")
    w("   VARA. La vara 9.6.1 tiene DOS salidas y nada mas: REPITE -> A y")
    w("   CONTINUA -> D. Un par que yo llame %r cae FUERA de su alcance."
      % [c for c in ("B", "C")])
    disc192 = [f for f in f192 if f[4] == "DISCREPA"]
    dentro_alcance, fuera_alcance, adjudicados = [], [], []
    for p, cl, ca, du, _v in disc192:
        en_alcance = cl in CLASES_DE_LA_VARA and ca in CLASES_DE_LA_VARA
        adj = VARA_DEL_ACTA.get(p)
        marca = []
        if adj:
            marca.append("la 4.9 del acta 193 la resuelve en %s" % adj)
            adjudicados.append((p, cl, ca, adj))
        if en_alcance:
            dentro_alcance.append(p)
        else:
            fuera_alcance.append(p)
            marca.append("FUERA del alcance de la vara: yo dije %s" % cl)
        w("   puesto %-5d yo %s / archivo %s / %s de mis dudosos%s"
          % (p, cl, ca, "DENTRO" if du else "FUERA",
             (" -> " + "; ".join(marca)) if marca else ""))
    w("")
    w("   CIFRA discrepancias de la 192: %d" % len(disc192))
    w("   CIFRA DENTRO del alcance de la vara (A contra D): %d (%s)"
      % (len(dentro_alcance), ", ".join(str(x) for x in dentro_alcance)))
    w("   CIFRA FUERA del alcance de la vara (yo dije B): %d (%s)"
      % (len(fuera_alcance), ", ".join(str(x) for x in fuera_alcance)))
    w("")

    w("C) LO QUE LA VARA CAMBIA DE VERDAD, Y SON LAS TRES QUE EL ACTA ADJUDICA")
    cambian, no_cambian = [], []
    for p, cl, ca, adj in adjudicados:
        if adj == ca and adj != cl:
            cambian.append(p)
        else:
            no_cambian.append((p, cl, ca, adj))
    w("   CIFRA discrepancias que la vara resuelve BIEN: %d (%s)"
      % (len(cambian), ", ".join(str(x) for x in cambian) or "ninguna"))
    for p in cambian:
        fila = [f for f in disc192 if f[0] == p][0]
        w("      puesto %d: yo dije %s, el archivo dice %s, la vara dice %s"
          % (p, fila[1], fila[2], VARA_DEL_ACTA[p]))
    if no_cambian:
        w("   CIFRA adjudicadas que NO calzan con el archivo: %d" % len(no_cambian))
        for p, cl, ca, adj in no_cambian:
            w("      puesto %d: yo %s, archivo %s, vara %s" % (p, cl, ca, adj))
    resto = [f[0] for f in disc192 if f[0] not in VARA_DEL_ACTA]
    w("   CIFRA discrepancias que la vara NO toca: %d (%s)"
      % (len(resto), ", ".join(str(x) for x in resto)))
    w("")

    w("D) MIS DUDOSOS DE LA 192 CONTRA MIS DUDOSOS DE LA 193")
    r193 = C.resumen(f193)
    w("   dudosos de la 192: %d de %d" % (r192["dudosos"], r192["total"]))
    w("   dudosos de la 193: %d de %d" % (r193["dudosos"], r193["total"]))
    w("   discrepancias FUERA del marcado, 192: %d | 193: %d"
      % (len(r192["disc_fuera"]), len(r193["disc_fuera"])))
    w("   tasa de coincidencia, 192: %d de %d | 193: %d de %d"
      % (r192["coinciden"], r192["total"], r193["coinciden"], r193["total"]))
    w("")

    w("E) EL ALCANCE DE LA VARA, MEDIDO SOBRE LA TANDA DE LA 193, QUE ES LA")
    w("   PRIMERA LEIDA ENTERA CON ELLA. AQUI ESTA EL DATO QUE NO ME ESPERABA.")
    w("   %s -> %d filas" % (COTEJO_193, len(f193)))
    w("   REPARTO DEL LECTOR (yo, leyendo SOLO con 9.6.1): %s"
      % ", ".join("%s %d" % (k, r193["reparto_lector"][k])
                  for k in sorted(r193["reparto_lector"])))
    w("   REPARTO DEL ARCHIVO sobre los mismos 30: %s"
      % ", ".join("%s %d" % (k, r193["reparto_archivo"][k])
                  for k in sorted(r193["reparto_archivo"])))
    b_lector = r193["reparto_lector"].get("B", 0)
    b_archivo = r193["reparto_archivo"].get("B", 0)
    w("   CIFRA `B` que emiti leyendo con la vara: %d" % b_lector)
    w("   CIFRA `B` que el archivo tiene en el mismo tramo: %d" % b_archivo)
    b_puestos = sorted(f[0] for f in f193 if f[2] == "B")
    w("   los puestos donde el archivo dice `B`: %s"
      % ", ".join(str(x) for x in b_puestos))
    disc_por_b = sorted(f[0] for f in f193 if f[4] == "DISCREPA" and f[2] == "B")
    w("   CIFRA discrepancias mias que el archivo resuelve en `B`: %d (%s)"
      % (len(disc_por_b), ", ".join(str(x) for x in disc_por_b)))
    w("")
    w("   LO QUE ESTO MIDE, DICHO SIN ADORNO: la vara 9.6.1 tiene DOS salidas,")
    w("   REPITE y CONTINUA, y leyendola literal NO PUEDE EMITIR `B` NUNCA. El")
    w("   archivo si usa `B` en este tramo, y %d de mis %d discrepancias son"
      % (len(disc_por_b), r193["discrepan"]))
    w("   exactamente eso: un par que el archivo llama `B` y que la vara solo")
    w("   sabe empujar a `A` o a `D`.")
    w("")

    w("F) LAS DOS COSAS QUE SE PUBLICAN JUNTAS Y NINGUNA SE RESUELVE COPIANDO")
    w("   A FAVOR DE LA VARA: de mis %d discrepancias de la 192, la vara resuelve"
      % len(disc192))
    w("   BIEN las %d que el acta 193 adjudica (%s), y las tres estaban DENTRO de"
      % (len(cambian), ", ".join(str(x) for x in cambian)))
    w("   su alcance. Ninguna de las tres la resuelve el criterio viejo.")
    w("   EN CONTRA DE LA VARA: %d de esas %d discrepancias (%s) son pares que yo"
      % (len(fuera_alcance), len(disc192),
         ", ".join(str(x) for x in fuera_alcance)))
    w("   llame `B`, y la vara no tiene salida `B`. Y en la tanda de la 193,")
    w("   leida ENTERA con ella, emiti CERO `B` sobre un tramo donde el archivo")
    w("   tiene %d." % b_archivo)
    w("   O SEA: la vara arregla el eje A contra D, que es donde nos tumbo a los")
    w("   dos lectores, y NO dice nada sobre el eje que mas discrepancias me")
    w("   produce a mi. Las dos mitades van publicadas.")
    w("")

    texto = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V193_T3F_QUE_CAMBIA_LA_VARA.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: docs/loop/SALIDA_V193_T3F_QUE_CAMBIA_LA_VARA.txt (%d bytes)"
          % len(texto.encode("utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
