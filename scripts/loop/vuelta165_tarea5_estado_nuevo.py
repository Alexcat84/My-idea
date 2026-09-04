# -*- coding: utf-8 -*-
r"""vuelta165_tarea5_estado_nuevo.py . TAREA 5 de la vuelta 165: EL ESTADO NUEVO
SE MIDE, NO SE HEREDA (adjudicacion 6.9 del acta 164).

POR QUE. El fundador cerro la fase 08 en una sesion con credencial, y su commit
publica cifras que la cabecera del bucle lleva. NINGUNA de esas cifras se copia:
se corre y se publica CON EL COMANDO, y el commit del fundador se cita solo como
CONTRASTE.

QUE CORRE, Y CADA UNO CON SU COMANDO IMPRESO AL LADO:
  1. las suites de la web
  2. el `tsc`
  3. el `sha256` del indice semantico, calculado byte a byte sobre el fichero
     que `sync_assets_web.py` declara como su sede (leida del propio script y no
     de la memoria, que es la medicina que el auditor uso para saldar la deuda
     de los assets en la 164)

USO:  python scripts/loop/vuelta165_tarea5_estado_nuevo.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def correr(cmd, cwd):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, shell=True)
    return r.returncode, (r.stdout.decode("utf-8", errors="replace")
                          + r.stderr.decode("utf-8", errors="replace"))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 165, TAREA 5: EL ESTADO NUEVO, CORRIDO CON MI COMANDO")
    print("=" * 78)
    print("")

    web = os.path.join(RAIZ, "web")

    print("1) LAS SUITES DE LA WEB")
    print("   COMANDO: pnpm test   (cwd: web/)")
    c, o = correr("pnpm test", web)
    for l in o.split("\n"):
        if re.search(r"Test Files|Tests |Duration|RUN ", l):
            print("   %s" % l.strip())
    print("   EXITCODE: %d" % c)
    m1 = re.search(r"Test Files\s+(\d+) passed \((\d+)\)", o)
    m2 = re.search(r"Tests\s+(\d+) passed(?: \| (\d+) skipped)? \((\d+)\)", o)
    print("   CIFRA ficheros de test: %s" % (m1.group(1) if m1 else "?"))
    print("   CIFRA pruebas pasadas: %s" % (m2.group(1) if m2 else "?"))
    print("   CONTRASTE, y solo contraste: la cabecera de la vuelta 164 publica")
    print("   80 ficheros y 1.030 pasadas; el commit e966d896 del fundador dice")
    print("   82 y 1.040. La cifra que vale es la de arriba, corrida aqui.")
    print("")

    print("2) EL TSC")
    print("   COMANDO: npx tsc --noEmit -p tsconfig.json   (cwd: web/)")
    c2, o2 = correr("npx tsc --noEmit -p tsconfig.json", web)
    lineas = [l for l in o2.split("\n") if l.strip()]
    print("   EXITCODE: %d" % c2)
    print("   CIFRA lineas de salida: %d" % len(lineas))
    for l in lineas[:5]:
        print("   %s" % l)
    print("")

    print("3) EL SHA256 DEL INDICE SEMANTICO")
    print("   LA SEDE SE LEE DEL PROPIO sync_assets_web.py, NO DE LA MEMORIA")
    fuente = io.open(os.path.join(RAIZ, "scripts", "sync_assets_web.py"),
                     encoding="utf-8").read()
    m = re.search(r"DEST\s*=\s*(.+)", fuente)
    print("   linea de DEST en el script: %s" % (m.group(0).strip() if m else "?"))
    m2 = re.search(r'semantic_index_path\s*=\s*DEST\s*/\s*"([^"]+)"', fuente)
    nombre = m2.group(1) if m2 else "semantic_index.json"
    print("   nombre del fichero, leido del script: %s" % nombre)
    candidatos = [os.path.join(RAIZ, "web", "lib", "assets", nombre),
                  os.path.join(RAIZ, "dataset", "metadata", nombre),
                  os.path.join(RAIZ, "engine", nombre)]
    hallados = 0
    for ruta in candidatos:
        rel = os.path.relpath(ruta, RAIZ).replace(os.sep, "/")
        if not os.path.exists(ruta):
            print("   %-44s NO EXISTE" % rel)
            continue
        hallados += 1
        datos = io.open(ruta, "rb").read()
        print("   %-44s %d bytes  sha256=%s"
              % (rel, len(datos), hashlib.sha256(datos).hexdigest()))
    print("   CIFRA sedes del indice que existen en disco: %d" % hallados)
    print("")
    # EL BARRIDO VA SELLADO EN LA FORMA DE LA CASA, con sus DOS PIERNAS, porque
    # una busqueda negativa no se puede citar (EJECUTOR.md 9) y porque la frase
    # "no existe en ninguna otra sede" es una afirmacion de AUSENCIA.
    universo, por_nombre, por_contenido, no_leidos = [], [], [], 0
    for base, dirs, ficheros in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in ("node_modules", ".git", ".next",
                                                "__pycache__")]
        for f in ficheros:
            ruta = os.path.join(base, f)
            rel = os.path.relpath(ruta, RAIZ).replace(os.sep, "/")
            universo.append(rel)
            if f == nombre:
                por_nombre.append(rel)
    # LA SEGUNDA PIERNA, POR CONTENIDO: quien DECLARA la ruta del indice en su
    # texto. Se mira solo lo que es texto y cabe en memoria; lo que no se puede
    # decodificar se CUENTA y no se cuela como "sin coincidencia".
    marca = "semantic_index"
    for rel in universo:
        if not rel.endswith((".py", ".ts", ".tsx", ".js", ".json", ".md", ".txt")):
            continue
        if rel.endswith(nombre):
            continue
        try:
            texto = io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                            encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            no_leidos += 1
            continue
        if marca in texto:
            por_contenido.append(rel)
    print("BARRIDO EXHAUSTIVO")
    print("  PREGUNTA: existe el indice semantico en alguna sede que no sea la que")
    print("  sync_assets_web.py declara, o es esa la unica")
    print("  UNIVERSO: os.walk del repo entero ACOTADO a todo menos node_modules,")
    print("  .git, .next y __pycache__")
    print("  CARDINAL: %d" % len(universo))
    print("  POR NOMBRE: %s | %d ficheros con coincidencia" % (nombre, len(por_nombre)))
    for rel in sorted(por_nombre):
        print("      %s  [nombre]" % rel)
    print("  POR CONTENIDO: %s | %d ficheros con coincidencia"
          % (marca, len(por_contenido)))
    for rel in sorted(por_contenido)[:12]:
        print("      %s  [contenido]" % rel)
    if len(por_contenido) > 12:
        print("      ... y %d mas" % (len(por_contenido) - 12))
    print("  VITALIDAD DE LOS PATRONES DE CONTENIDO: %d de %d alternativas "
          "aparecen en el universo" % (1 if por_contenido else 0, 1))
    print("      %-46s -> %-6d %s"
          % (marca, len(por_contenido), "viva" if por_contenido else "MUERTA"))
    print("  NO DECODIFICABLES (mirados y no leidos, NO cuentan como sin "
          "coincidencia): %d" % no_leidos)
    print("  VEREDICTO: %s" % ("UNA SOLA SEDE" if len(por_nombre) == 1
                               else "MAS DE UNA SEDE"))
    print("CIFRA ficheros del universo: %d ficheros" % len(universo))
    print("CIFRA sedes del indice halladas por nombre: %d ficheros" % len(por_nombre))
    print("CIFRA ficheros que solo lo nombran, sin serlo: %d ficheros"
          % len(por_contenido))
    print("   CONTRASTE, y solo contraste: el sello de la sesion con credencial")
    print("   publica 42223fcc y el auditor dice haberlo recomputado en la 164.")
    print("   La cifra que vale es la de arriba.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
