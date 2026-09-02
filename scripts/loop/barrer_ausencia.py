# -*- coding: utf-8 -*-
r"""barrer_ausencia.py . EL INSTRUMENTO DEL BARRIDO EXHAUSTIVO (TAREA 2 de la
vuelta 146, la ESCALADA de `AUDITOR.md` 1.2 disparada por la racha de reporte
llegando a DOS, acta de la vuelta 145).

NOMBRE ESTABLE, SIN NUMERO DE VUELTA, como `verificar_apertura_sellada.py`,
`tallar_cabecera_reporte.py` y `verificar_mutaciones_viejas.py`: se corre igual
en toda vuelta y no se clona.

POR QUE NACE. `verificar_ausencias_del_reporte.py` (su hermana, la guarda)
exige que toda AFIRMACION DE AUSENCIA del reporte venga respaldada por un
BARRIDO EXHAUSTIVO COMPUTADO sellado en una salida. Una guarda que exige algo
que nadie sabe producir no es una guarda, es un muro: este instrumento es lo
que hace que la exigencia se pueda cumplir, y por eso nace en la misma tarea.

QUE ES UN BARRIDO EXHAUSTIVO, ESCRITO AQUI Y NO ADIVINADO. Un recorrido del
UNIVERSO ENTERO de donde la cosa podria estar, con su universo y su cardinal
publicados. Para ficheros del repositorio son DOS PIERNAS y las dos son
obligatorias:

  (1) POR NOMBRE, sobre `git ls-files` (el universo entero de lo versionado, no
      el arbol de trabajo: un fichero sin versionar no es del repositorio).
  (2) POR CONTENIDO, sobre ESE MISMO universo. Esta es la pierna que faltaba el
      dia de la caida: la vuelta 145 miro TRES RUTAS TECLEADAS A MANO y
      concluyo que la lista canonica de libros no existia. Existia, y se llama
      `docs/plan/OP_S_11_MAPEO_PROPUESTO.md`. Una busqueda por nombre NO PUEDE
      hallar un fichero que se llama por su operacion duena; una por contenido
      SI. Por eso la guarda hermana no acepta un barrido de una sola pierna.

EL SELLO QUE IMPRIME, y es el contrato que la guarda hermana lee (si se cambia
una de estas cinco lineas hay que cambiarlo en las dos, y por eso viven aqui
escritas y no adivinadas):

  BARRIDO EXHAUSTIVO
    PREGUNTA: <la ausencia que este barrido respalda, en una linea>
    UNIVERSO: <de donde sale el universo>
    CARDINAL: <n>
    POR CONTENIDO: <patron> | <n> ficheros con coincidencia
    VEREDICTO: HALLADO / NO HALLADO

`PREGUNTA:` es obligatoria a proposito: obliga al barrido a decir QUE ausencia
respalda, para que un reporte no pueda apoyar una ausencia en el barrido del
vecino sin que se vea.

LA FRONTERA, Y ES LA MISMA QUE LA DE LA GUARDA: este instrumento NO decide si
lo que se busca "deberia" existir ni si su ausencia es buena o mala. Recorre el
universo, dice lo que encuentra y sella. El VEREDICTO que imprime es un HECHO
MEDIDO (hay o no hay coincidencias), nunca un juicio.

USO:
  python scripts/loop/barrer_ausencia.py \
      --pregunta "existe una lista canonica de libros con sus alias" \
      --nombre "libros_canonicos|fuentes_canonicas|LIBROS_CANONICOS" \
      --contenido "grafia|canonica propuesta" \
      --candidato dataset/metadata/libros_canonicos.json

`--candidato` se puede repetir: son las rutas que alguien miraria a mano. NO
son el barrido; se imprimen APARTE, bajo su propio rotulo, justamente para que
se vea la diferencia entre mirar tres nombres y recorrer el universo.
"""
import argparse
import io
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MARCA = "BARRIDO EXHAUSTIVO"
EXTENSIONES_DE_TEXTO = (".md", ".py", ".txt", ".json", ".jsonl", ".ts", ".tsx",
                        ".js", ".jsx", ".yml", ".yaml", ".css", ".html", ".sql")


def universo(prefijos=None):
    """El universo entero de lo versionado en la rama actual. Se lee de git y
    no del arbol de trabajo (`EJECUTOR.md`, LA IDENTIDAD SE LEE DE GIT).

    `prefijos` ACOTA el universo por ruta, y SOLO se usa cuando la pregunta lo
    pide de verdad: "esta este control instalado EN EL CODIGO" tiene por
    universo el codigo, no el repositorio entero, y meter en el universo los
    ficheros de salida que citan el literal como SONDA daria coincidencias que
    no son instalaciones. EL RECORTE NO SE ESCONDE: se imprime en la linea
    `UNIVERSO:` del sello y el `CARDINAL:` es el del universo YA acotado, para
    que quien lea sepa exactamente sobre que se barrio."""
    r = subprocess.run(["git", "ls-files"], cwd=RAIZ, capture_output=True, text=True,
                       check=True)
    rutas = [l for l in r.stdout.splitlines() if l.strip()]
    if prefijos:
        rutas = [x for x in rutas if any(x.startswith(p) for p in prefijos)]
    return rutas


def por_nombre(rutas, patron):
    rx = re.compile(patron, re.IGNORECASE)
    return [r for r in rutas if rx.search(os.path.basename(r))]


def por_contenido(rutas, patron):
    """Recorre el MISMO universo leyendo cada fichero de texto. Los ficheros
    que no se pueden decodificar se cuentan y se publican: un fichero que no se
    pudo mirar NO es un fichero sin coincidencia (banco 9, fallar ruidoso)."""
    rx = re.compile(patron, re.IGNORECASE)
    aciertos, ilegibles = [], []
    for r in rutas:
        if not r.lower().endswith(EXTENSIONES_DE_TEXTO):
            continue
        ruta = os.path.join(RAIZ, r)
        if not os.path.exists(ruta):
            continue
        try:
            with io.open(ruta, encoding="utf-8") as f:
                texto = f.read()
        except (UnicodeDecodeError, OSError):
            ilegibles.append(r)
            continue
        if rx.search(texto):
            aciertos.append(r)
    return aciertos, ilegibles


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pregunta", required=True)
    ap.add_argument("--nombre", required=True, help="regex sobre el NOMBRE de fichero")
    ap.add_argument("--contenido", required=True, help="regex sobre el CONTENIDO")
    ap.add_argument("--candidato", action="append", default=[],
                    help="ruta que alguien miraria a mano; se imprime APARTE")
    ap.add_argument("--universo-prefijo", action="append", default=[], dest="prefijos",
                    help="acota el universo por prefijo de ruta; se declara en el sello")
    # LA SONDA NO ES UNA INSTALACION (misma especie que "la guarda que se
    # envenena sola" de verificar_apertura_sellada.py). Un barrido que busca el
    # literal de un control SE ENCUENTRA A SI MISMO en el instrumento que lo
    # sonda, y contarlo seria publicar como instalado un control que solo
    # existe dentro de la vara que pregunta por el. Las exclusiones NO se
    # esconden: se imprimen en el sello, una a una, con su motivo al lado en el
    # reporte que las use.
    ap.add_argument("--excluir", action="append", default=[],
                    help="ruta excluida del universo por ser SONDA y no instalacion; "
                         "se declara entera en el sello")
    a = ap.parse_args()

    rutas = [r for r in universo(a.prefijos) if r not in set(a.excluir)]
    nom = por_nombre(rutas, a.nombre)
    con, ilegibles = por_contenido(rutas, a.contenido)
    todos = sorted(set(nom) | set(con))

    print(MARCA)
    print("  PREGUNTA: %s" % a.pregunta)
    print("  UNIVERSO: git ls-files de la rama actual%s"
          % (" ACOTADO a %s" % ", ".join(a.prefijos) if a.prefijos
             else " (todo lo versionado, sin acotar)"))
    print("  CARDINAL: %d" % len(rutas))
    print("  EXCLUIDOS POR SER SONDA Y NO INSTALACION (declarados, no escondidos): %d"
          % len(a.excluir))
    for x in a.excluir:
        print("      %s" % x)
    print("  POR NOMBRE: %s | %d ficheros con coincidencia" % (a.nombre, len(nom)))
    print("  POR CONTENIDO: %s | %d ficheros con coincidencia" % (a.contenido, len(con)))
    print("  NO DECODIFICABLES (mirados y no leidos, NO cuentan como sin coincidencia): %d"
          % len(ilegibles))
    for r in ilegibles[:20]:
        print("      %s" % r)
    print("  VEREDICTO: %s" % ("HALLADO" if todos else "NO HALLADO"))
    print("  LOS QUE COINCIDEN (union de las dos piernas): %d" % len(todos))
    for r in todos[:60]:
        marcas = []
        if r in nom:
            marcas.append("nombre")
        if r in con:
            marcas.append("contenido")
        print("      %s  [%s]" % (r, " y ".join(marcas)))
    if len(todos) > 60:
        print("      ... y %d mas" % (len(todos) - 60))

    if a.candidato:
        print("  RUTAS CANDIDATAS MIRADAS A MANO (NO SON EL BARRIDO, van aparte):")
        for c in a.candidato:
            print("      %s -> %s" % (c, "EXISTE" if c in set(rutas) else "NO EXISTE"))
    print("CIFRA ficheros del universo: %d ficheros" % len(rutas))
    print("CIFRA ficheros que coinciden: %d ficheros" % len(todos))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
