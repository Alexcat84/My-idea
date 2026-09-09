# -*- coding: utf-8 -*-
r"""_v214_sustituir_t3.py . LA SUSTITUCION DECLARADA Y MEDIDA DEL CUERPO DE LA
TAREA 3 DENTRO DEL REPORTE DE LA VUELTA 214.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO (moratoria de AUDITOR.md 6.3).

POR QUE EXISTE, Y ES UNA CAIDA MIA: mi tabla de instrumentos de la TAREA 3
publicaba NUEVE cifras de bytes SIN SU PAREJA, y la guarda de cerrar_reporte.py
(toda cifra de bytes y todo sha con su pareja) la bloqueo. Tenia razon: una cifra
de bytes sin decir por que convencion no se puede cotejar.

POR QUE NO SE REHACE EL ESQUELETO: se intento, y el archivador lo nego con razon,
porque git ya tiene el reporte de la 214 en esa ruta y archivarlo bajo el numero
213 seria archivar un texto bajo un numero que no es el suyo. La guarda mordio y
no se le da la vuelta.

EL PRECEDENTE DE LA FORMA: scripts/loop/_v213_arreglar_esqueleto.py, que corrigio
la C.1 de la 213 por sustitucion declarada y medida.

EL TEXTO VIEJO NO SE TECLEA: se LEE de git, del commit donde se anexo. El nuevo
se LEE del fichero que el compositor acaba de escribir. Aqui no se escribe prosa.

USO:
  python scripts/loop/_v214_sustituir_t3.py --simular
  python scripts/loop/_v214_sustituir_t3.py --escribir
"""
import io
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE = "docs/loop/REPORTE.md"
CUERPO = "scripts/loop/_v214_t3_seccion.md"
COMMIT_VIEJO = "354cca1b"


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read()


def main():
    modo = sys.argv[1] if len(sys.argv) > 1 else "--simular"
    print("=" * 78)
    print("VUELTA 214. SUSTITUCION DECLARADA DEL CUERPO DE LA TAREA 3. MODO %s"
          % modo)
    print("=" * 78)

    c, viejo = git(["show", "%s:%s" % (COMMIT_VIEJO, CUERPO)])
    if c != 0 or not viejo.strip():
        print("ROJO: no se pudo leer el texto viejo de git.")
        return 1
    viejo = viejo.replace(chr(13) + NL, NL).strip(NL)
    nuevo = leer(CUERPO).replace(chr(13) + NL, NL).strip(NL)
    texto = leer(REPORTE).replace(chr(13) + NL, NL)

    print("EL TEXTO VIEJO SE LEE DE git show %s:%s, NO SE TECLEA."
          % (COMMIT_VIEJO, CUERPO))
    print("   CIFRA bytes del texto viejo:  %d" % len(viejo.encode("utf-8")))
    print("   CIFRA bytes del texto nuevo:  %d" % len(nuevo.encode("utf-8")))
    print("   CIFRA veces que el viejo aparece en el reporte: %d (se exige 1)"
          % texto.count(viejo))
    print("   CIFRA veces que el nuevo aparece ya en el reporte: %d (se exige 0)"
          % texto.count(nuevo))
    print("")

    fallos = 0
    if texto.count(viejo) != 1:
        fallos += 1
        print("ROJO: el texto viejo no aparece exactamente una vez.")
    if viejo == nuevo:
        fallos += 1
        print("ROJO: el texto nuevo es identico al viejo, no hay nada que sustituir.")

    salida = texto.replace(viejo, nuevo, 1)

    # LO QUE DE VERDAD CAMBIA, MEDIDO LINEA A LINEA
    la, lb = texto.split(NL), salida.split(NL)
    print("LO QUE CAMBIA, MEDIDO Y NO PROMETIDO:")
    print("   CIFRA lineas antes: %d | despues: %d" % (len(la), len(lb)))
    solo_en_viejo = [l for l in la if l not in set(lb)]
    solo_en_nuevo = [l for l in lb if l not in set(la)]
    print("   CIFRA lineas que solo estaban antes: %d" % len(solo_en_viejo))
    print("   CIFRA lineas que solo estan despues: %d" % len(solo_en_nuevo))
    fuera = [l for l in solo_en_viejo if l not in viejo.split(NL)]
    print("   CIFRA lineas perdidas FUERA del bloque de la TAREA 3: %d (se exige 0)"
          % len(fuera))
    for l in fuera[:10]:
        print("      perdida> %s" % l[:96])
    if fuera:
        fallos += 1

    # LAS CIFRAS DE BYTES SIN PAREJA, QUE ES LO QUE ESTO VIENE A ARREGLAR
    pat_bytes = re.compile(r"(\d[\d.]*)\s*bytes")
    pat_pareja = re.compile(
        r"(\d[\d.]*)\s*bytes\s+en\s+disco\s+y\s+(\d[\d.]*)\s*bytes\s+normalizados\s+a\s+LF")
    def huerfanas(t):
        n = 0
        for l in t.split(NL):
            if "bytes" not in l:
                continue
            if pat_pareja.search(l):
                continue
            if pat_bytes.search(l):
                n += 1
        return n
    print("")
    print("LA CAIDA QUE ESTO ARREGLA, CONTADA A LOS DOS LADOS DEL BLOQUE:")
    print("   CIFRA lineas con bytes SIN pareja en el bloque VIEJO: %d"
          % huerfanas(viejo))
    print("   CIFRA lineas con bytes SIN pareja en el bloque NUEVO: %d (se exige 0)"
          % huerfanas(nuevo))
    if huerfanas(nuevo):
        fallos += 1

    for marca in ("### TAREA 3.", "<!-- ANEXO DE TAREAS -->",
                  "<!-- FIN ANEXO DE TAREAS -->", "<!-- TABLA DE TAREAS -->"):
        n = salida.count(marca)
        print("   marca %-34s aparece %d vez(ces) (se exige 1)" % (marca, n))
        if n != 1:
            fallos += 1
    largos = salida.count(chr(8212)) + salida.count(chr(8211))
    print("   CIFRA guiones largos mas medios: %d" % largos)
    if largos:
        fallos += 1
    print("")
    print("CIFRA comprobaciones que fallan: %d" % fallos)

    if modo == "--escribir":
        if fallos:
            print("ROJO: NO SE ESCRIBE. El reporte queda intacto.")
            return 1
        io.open(os.path.join(RAIZ, REPORTE.replace("/", os.sep)), "w",
                encoding="utf-8", newline=NL).write(salida)
        de_nuevo = leer(REPORTE).replace(chr(13) + NL, NL)
        print("ESCRITO %s -> %d bytes" % (REPORTE, len(de_nuevo.encode("utf-8"))))
        print("   RELECTURA identica a lo juzgado: %s"
              % ("SI" if de_nuevo == salida else "NO"))
        print("   el cuerpo nuevo esta byte a byte: %s"
              % ("SI" if nuevo in de_nuevo else "NO"))
        print("   el cuerpo viejo ya NO esta: %s"
              % ("SI" if viejo not in de_nuevo else "NO"))
        ok = (de_nuevo == salida and nuevo in de_nuevo and viejo not in de_nuevo)
        print("VERDE: la sustitucion queda hecha." if ok else "ROJO.")
        return 0 if ok else 1

    print("SIMULACION: NO SE ESCRIBE NADA.")
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
