# -*- coding: utf-8 -*-
r"""_v213_arreglar_esqueleto.py . LA CORRECCION DE MI PROPIA PROSA DE ESQUELETO,
QUE ROMPIA LA OBLIGACION 1 DEL ENCARGO DE LA VUELTA 213.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo y fuera de la
nomina. Moratoria de AUDITOR.md 6.3. Muere con la vuelta.

QUE PASO, MEDIDO Y NO CONTADO DE MEMORIA. La obligacion 1 del encargo dice que
NINGUN REPORTE CITA UN DIRECTORIO A SECAS COMO RUTA entre comillas inversas
(adjudicacion 6.2 del acta 212). El esqueleto que YO talle en la apertura de
esta misma vuelta escribia, en su propio bloque de prosa,
`scripts/loop/` entre comillas inversas. **Lo cazo
vuelta186_rutas_del_reporte.py corriendo sobre el reporte cerrado**, que es
exactamente el instrumento que la obligacion existe para que pueda llegar a
imprimir: revento con FileNotFoundError sobre ese directorio.

POR QUE NO SE REGENERA EL ESQUELETO ENTERO. `_v213_esqueleto.py` YA esta
corregido y su texto nuevo es el que se pega aqui, pero el esqueleto no se puede
volver a correr en la misma vuelta: su PASO 0 llama al archivador, el archivador
lee de git el ultimo REPORTE.md, y ese ya es el de la 213, asi que la guarda cae
en (a) con razon. **La guarda es correcta y no se toca.** Lo que se hace es la
sustitucion UNA, declarada, sobre el esqueleto tal como git lo lleva.

LO QUE ESTE COMPUTO GARANTIZA, Y CAE EN ROJO SI NO:
  . el texto viejo aparece EXACTAMENTE UNA VEZ antes de tocar nada;
  . el texto nuevo es el que `_v213_esqueleto.py` lleva HOY en su fuente, leido
    de ese fichero y no tecleado aqui dos veces;
  . despues de escribir NO QUEDA NI UN directorio de dos tramos entre comillas
    inversas en todo el reporte;
  . y se publican los bytes antes y despues.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
NL = chr(10)
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
ESQ = os.path.join(AQUI, "_v213_esqueleto.py")
BT = chr(96)

VIEJO = ("> lector nuevo, y ninguno reparado. Todo lo que esta vuelta escribe en" + NL
         + "> " + BT + "scripts/loop/" + BT + " son ficheros " + BT + "_v213_*" + BT
         + " **con prefijo de guion bajo, fuera del" + NL
         + "> censo y fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda.")

sys.stdout.reconfigure(encoding="utf-8")


def main():
    fuente = io.open(ESQ, encoding="utf-8").read()
    m = re.search(r"> lector nuevo, y ninguno reparado\. Todo lo que esta vuelta "
                  r"escribe en el arbol" + NL + r".*?no se poda\.", fuente, re.S)
    if not m:
        print("ROJO: no encuentro el texto nuevo dentro de _v213_esqueleto.py.")
        return 1
    NUEVO = m.group(0).replace("_v%(v)d_*", "_v213_*")
    print("EL TEXTO NUEVO NO SE TECLEA AQUI: SE LEE DE scripts/loop/_v213_esqueleto.py")
    for l in NUEVO.split(NL):
        print("   nuevo> " + l)
    print("")
    texto = io.open(REPORTE, encoding="utf-8", newline="").read()
    antes = len(texto.encode("utf-8"))
    n = texto.count(VIEJO)
    print("CIFRA bytes del reporte ANTES: %d" % antes)
    print("CIFRA veces que aparece el texto viejo: %d (se exige 1)" % n)
    if n != 1:
        print("ROJO: no se escribe nada.")
        return 1
    nuevo_texto = texto.replace(VIEJO, NUEVO)
    dirs = re.findall(BT + r"[^" + BT + NL + r"]*/[^" + BT + NL + r"]*/" + BT,
                      nuevo_texto)
    print("CIFRA directorios de dos tramos entre comillas inversas DESPUES: %d "
          "(se exigen 0)" % len(dirs))
    for d in sorted(set(dirs)):
        print("   QUEDA> " + d)
    if dirs:
        print("ROJO: no se escribe nada.")
        return 1
    io.open(REPORTE, "w", encoding="utf-8", newline="").write(nuevo_texto)
    de_nuevo = io.open(REPORTE, encoding="utf-8", newline="").read()
    despues = len(de_nuevo.encode("utf-8"))
    print("CIFRA bytes del reporte DESPUES: %d" % despues)
    print("CIFRA relectura del disco identica a lo juzgado: %s"
          % ("SI" if de_nuevo == nuevo_texto else "NO"))
    print("VERDE: la prosa del esqueleto queda corregida."
          if de_nuevo == nuevo_texto else "ROJO: lo escrito no es lo juzgado.")
    return 0 if de_nuevo == nuevo_texto else 1


if __name__ == "__main__":
    sys.exit(main())
