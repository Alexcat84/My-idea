# -*- coding: utf-8 -*-
r"""vuelta179_tarea1b_corrida_sobre_178.py . LA GUARDA NUEVA, CORRIDA SOBRE EL
REPORTE ARCHIVADO DE LA 178, Y SE PUBLICA LO QUE SALGA.

POR QUE EXISTE ESTE FICHERO Y NO BASTA CON EL ARNES DE MUTACION. El encargo de la
vuelta 179, TAREA 1.b, lo pide con estas palabras: *"corre la guarda nueva sobre
docs/loop/reportes/REPORTE_V178.md y publica lo que salga: si caza la caida de la
178 en su primera corrida, dilo con esas palabras; si no la caza, la guarda no
sirve y hay que arreglarla antes de seguir"*. Un arnes de mutacion prueba la
guarda contra casos FABRICADOS; esto la prueba contra EL CASO REAL que la motivo,
que es otra cosa y no se sustituyen.

EL SUJETO NO SE RETOCA. `docs/loop/reportes/REPORTE_V178.md` dice lo que se
publico y no se le cambia una coma: el encargo lo prohibe expresamente. Este
fichero SOLO LEE.

LO QUE ESTE FICHERO NO AFIRMA: no dice de antemano que la guarda cace la caida.
Corre y imprime. Si no la caza, sale en ROJO.

USO:
  python scripts/loop/vuelta179_tarea1b_corrida_sobre_178.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)
SUJETO = os.path.join(RAIZ, "docs", "loop", "reportes", "REPORTE_V178.md")


def main():
    print("=" * 78)
    print("LA GUARDA DE LA CITA DE ARNES, CORRIDA SOBRE EL REPORTE DE LA 178")
    print("=" * 78)
    print("")

    print("A) EL SUJETO, MEDIDO ANTES DE LEERLO, Y NO SE RETOCA")
    if not os.path.exists(SUJETO):
        print("   ROJO: no existe %s" % SUJETO)
        return 1
    texto = io.open(SUJETO, encoding="utf-8").read().replace(chr(13) + NL, NL)
    print("   docs/loop/reportes/REPORTE_V178.md")
    print("   CIFRA bytes en disco: %d | bytes normalizado a LF: %d"
          % (os.path.getsize(SUJETO), len(texto.encode("utf-8"))))
    print("   CIFRA lineas: %d" % texto.count(NL))
    print("")

    print("B) LO QUE LA GUARDA ENCUENTRA, IMPRESO SALGA LO QUE SALGA")
    citas = CR.citas_de_arnes_que_no_calzan(texto, CR.lector_de_docs_loop)
    rojas = [c for c in citas if not c[4].startswith("SIN COTEJO")]
    sin_cotejo = [c for c in citas if c[4].startswith("SIN COTEJO")]
    for n, ruta, publicada, propia, motivo in citas:
        print("   linea %-5d %-38s publicada %s | del fichero %s"
              % (n, ruta, publicada, propia if propia is not None else "(no medible)"))
        print("      %s" % motivo)
    print("   CIFRA citas que NO calzan: %d" % len(rojas))
    print("   CIFRA citas SIN COTEJO posible: %d" % len(sin_cotejo))
    print("")

    print("C) LAS CITAS QUE LA GUARDA MIRO Y DEJO PASAR, PARA QUE SE VEA QUE NO")
    print("   ACUSA A TODAS. Se listan TODAS las parejas que emparejo, calcen o no.")
    total_parejas = 0
    for linea0, parrafo, renglones in CR.parrafos_fuera_de_cerca(texto):
        for publicada, ruta, dist in CR.emparejar_citas(parrafo):
            total_parejas += 1
            n = linea0
            for num, renglon in renglones:
                if ruta in renglon:
                    n = num
                    break
            contenido = CR.lector_de_docs_loop(ruta)
            propia, _forma = CR.cifra_propia_del_arnes(contenido or "")
            print("   linea %-5d %-38s publicada %-4s fichero %-4s distancia %d -> %s"
                  % (n, ruta, publicada,
                     propia if propia is not None else "?", dist,
                     "CALZA" if propia == publicada else "NO CALZA"))
    print("   CIFRA parejas cifra-fichero que la guarda emparejo: %d" % total_parejas)
    print("   CIFRA de esas que calzan: %d" % (total_parejas - len(citas)))
    print("")

    print("D) LAS CIFRAS DE CASOS QUE LA GUARDA NO EMPAREJO CON NINGUN FICHERO")
    print("   (por no haber ninguno cerca en su parrafo). NO SE ACUSAN: una")
    print("   guarda que inventa un rojo no sirve para cazar los de verdad.")
    sueltas = 0
    for linea0, parrafo, renglones in CR.parrafos_fuera_de_cerca(texto):
        cifras = [m for m in CR.PATRON_CASOS.finditer(parrafo)]
        emparejadas = set(v for v, _r, _d in CR.emparejar_citas(parrafo))
        for m in cifras:
            if int(m.group(1) or m.group(2)) not in emparejadas:
                sueltas += 1
    print("   CIFRA cifras de casos sin fichero emparejado: %d" % sueltas)
    print("")

    print("E) EL VEREDICTO")
    caza_la_178 = [c for c in rojas
                   if "SALIDA_V178_T1E_MUTACION.txt" in c[1] and c[2] == 16 and c[3] == 18]
    if caza_la_178:
        n, ruta, pub, pro, _m = caza_la_178[0]
        print("   LA GUARDA CAZA LA CAIDA DE LA 178 EN SU PRIMERA CORRIDA.")
        print("   linea %d, fichero %s, cifra publicada %d, cifra del fichero %d."
              % (n, ruta, pub, pro))
        print("   VERDE.")
        return 0
    print("   LA GUARDA NO CAZA LA CAIDA DE LA 178. No sirve tal como esta y hay")
    print("   que arreglarla antes de seguir, que es lo que el encargo manda.")
    print("   ROJO.")
    return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
