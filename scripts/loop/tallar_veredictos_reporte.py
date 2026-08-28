# -*- coding: utf-8 -*-
"""tallar_veredictos_reporte.py . EL TALLADOR DE VEREDICTOS (TAREA 1.1 de la
vuelta 102, encargo del auditor, acta de la vuelta 101, "LA RACHA DE REPORTE
PASA DE UNO A DOS", escalada obligada por EJECUTOR.md 1.2).

POR QUE NACE, CON EL EJEMPLAR DELANTE. El reporte de la vuelta 101 publico,
en su parrafo de cabecera, "VERDE contra `scripts/loop/verificar_apertura_
sellada.py --vuelta 101`, `docs/loop/SALIDA_V101_TAREA1_2_MUTACION_
APERTURA.txt`", y remato en la TAREA 1 con "(1.3) usada sobre esta apertura:
VERDE". El fichero citado como evidencia, commiteado por el propio ejecutor,
imprime en su PRIMER bloque "ROJO, apertura de la vuelta 101 NO sellada
antes de la 1.a operacion ... EXIT=1". Nadie abrio el fichero citado antes
de teclear el veredicto. Este instrumento automatiza esa apertura.

QUE MIDE, EXACTO Y NADA MAS.

  (1) LOCALIZA cada palabra VERDE, ROJO, PASA o FALLA en `docs/loop/REPORTE.md`
      (linea a linea, respetando mayusculas: son las cuatro palabras que el
      reporte usa para veredictos, no cualquier "verde" de otro sentido).

  (2) PARA CADA UNA, busca el fichero `docs/loop/SALIDA_...` que la
      afirmacion CITA, DENTRO DEL MISMO PARRAFO (un parrafo es el texto
      entre dos lineas en blanco). La convencion de escritura de esta
      campana, repetida en cada acta y cada reporte, es "AFIRMACION
      (fichero)" o "AFIRMACION, `fichero`": el fichero de evidencia va
      DESPUES de la palabra de veredicto, no antes (un fichero citado ANTES,
      como el sello de un hash, suele ser contexto, no la evidencia de ESTE
      veredicto). Por eso se prefiere la PRIMERA cita que aparezca DESPUES
      de la palabra; solo si no hay ninguna despues en el mismo parrafo, se
      usa la mas cercana ANTES. Si no hay ninguna cita en el parrafo, la
      afirmacion NO CITA FICHERO y se ignora (no es lo que este tallador
      comprueba: EJECUTOR.md solo exige tallar lo que un fichero ya mide).

  (3) ABRE ese fichero y calcula SU VEREDICTO REAL: la ULTIMA linea de todo
      el fichero que empiece (tras quitar espacios) por VERDE, ROJO, PASA o
      FALLA (asi una salida con varios bloques, cada uno con su propio
      veredicto de caso, se lee por su LINEA DE CIERRE/RESUMEN, que es
      convencion de esta familia de instrumentos: "VERDE GENERAL", "TODOS
      LOS TESTS PASARON", etc. van al final). Si ninguna linea empieza asi,
      cae al ULTIMO `EXIT=N` o `EXITCODE N` del fichero (N==0 es VERDE, N!=0
      es ROJO). Si tampoco hay eso, EL VEREDICTO NO ES LEGIBLE.

  (4) COMPARA: VERDE y PASA son la misma clase (OK); ROJO y FALLA son la
      misma clase (MAL). Si la clase de la afirmacion del reporte NO
      coincide con la clase real del fichero, o si el fichero no existe, o
      si su veredicto no es legible, ES UN HALLAZGO: se imprime nombrando el
      fichero Y LA LINEA del reporte donde vive la afirmacion.

MECANICA DE ROJO: si HAY AL MENOS UN HALLAZGO, el tallador termina con
"ROJO, N hallazgo(s)" y exit 1. Si no hay ninguno (incluido el caso de que
el reporte no cite ningun fichero junto a un veredicto), termina con "VERDE"
y exit 0. Nunca corrige nada: solo mide y nombra.

USO:
  python scripts/loop/tallar_veredictos_reporte.py
  python scripts/loop/tallar_veredictos_reporte.py --reporte docs/loop/REPORTE.md

PRUEBA DE MUTACION, caso positivo OBLIGATORIO (con su salida commiteada,
docs/loop/SALIDA_V102_TAREA1_1_MUTACION_VEREDICTOS.txt):
  (a) ROJO sobre `docs/loop/REPORTE.md` de la vuelta 101 tal como esta
      commiteado en `8dfc4b48` (`git show 8dfc4b48:docs/loop/REPORTE.md`),
      que es el caso real medido por el auditor: tiene que nombrar
      `docs/loop/SALIDA_V101_TAREA1_2_MUTACION_APERTURA.txt` como el
      fichero cuyo veredicto real (ROJO) contradice la afirmacion VERDE del
      reporte.
  (b) VERDE sobre `docs/loop/REPORTE.md` de la vuelta 102, una vez escrito
      bien (cada veredicto que cite un fichero calza con lo que ese fichero
      dice de verdad).
"""
import argparse
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CLASE = {"VERDE": "OK", "PASA": "OK", "ROJO": "MAL", "FALLA": "MAL"}
RE_VEREDICTO_PALABRA = re.compile(r"\b(VERDE|ROJO|PASA|FALLA)\b")
RE_CITA = re.compile(r"`([^`]*docs/loop/SALIDA_[^`]+\.(?:txt|md))`")
RE_LINEA_VEREDICTO = re.compile(r"^(VERDE|ROJO|PASA|FALLA)\b")
RE_EXIT = re.compile(r"EXIT(?:CODE)?[=: ]+(\d+)", re.IGNORECASE)


def leer_texto(ruta_o_ref, fallos):
    """RUTA_O_REF es o bien una ruta real (por defecto docs/loop/REPORTE.md)
    o, con --commit, se lee de `git show <commit>:<ruta>` para poder probar
    contra un REPORTE.md historico sin tocar el arbol de trabajo."""
    ruta_abs = ruta_o_ref if os.path.isabs(ruta_o_ref) else os.path.join(RAIZ, ruta_o_ref)
    if not os.path.exists(ruta_abs):
        fallos.append("no existe %s" % ruta_o_ref)
        return None
    return io.open(ruta_abs, encoding="utf-8").read()


def leer_texto_de_commit(commit, ruta, fallos):
    try:
        r = subprocess.run(["git", "show", "%s:%s" % (commit, ruta)], cwd=RAIZ,
                           capture_output=True, text=True, check=True)
        return r.stdout
    except Exception as e:
        fallos.append("no se pudo leer %s en %s: %s" % (ruta, commit, e))
        return None


def parrafos_con_offset(texto):
    """Divide TEXTO en parrafos (separados por linea(s) en blanco) y
    devuelve, por cada parrafo, su texto y el OFFSET absoluto donde empieza
    (para poder recuperar el numero de linea real despues)."""
    partes = []
    offset = 0
    for bloque in re.split(r"(\n\s*\n)", texto):
        if bloque.strip():
            partes.append((offset, bloque))
        offset += len(bloque)
    return partes


def numero_de_linea(texto, offset):
    return texto.count("\n", 0, offset) + 1


def veredicto_real_del_fichero(ruta_rel, fallos_locales):
    ruta_abs = os.path.join(RAIZ, ruta_rel)
    if not os.path.exists(ruta_abs):
        return None, "el fichero citado no existe"
    contenido = io.open(ruta_abs, encoding="utf-8").read()
    ultima = None
    for linea in contenido.splitlines():
        m = RE_LINEA_VEREDICTO.match(linea.strip())
        if m:
            ultima = m.group(1)
    if ultima is not None:
        return CLASE[ultima], None
    codigos = RE_EXIT.findall(contenido)
    if codigos:
        return ("OK" if codigos[-1] == "0" else "MAL"), None
    return None, "el fichero no trae ninguna linea VERDE/ROJO/PASA/FALLA ni EXIT=N: veredicto no legible"


def hallar_afirmaciones(texto):
    """Para cada ocurrencia de VERDE/ROJO/PASA/FALLA, busca la cita de
    fichero MAS CERCANA (por distancia de caracteres) dentro del MISMO
    parrafo. Devuelve una lista de (linea, palabra, fichero_citado) SOLO
    para las ocurrencias que si citan un fichero."""
    afirmaciones = []
    for offset_parrafo, parrafo in parrafos_con_offset(texto):
        citas = [(m.start(), m.group(1)) for m in RE_CITA.finditer(parrafo)]
        if not citas:
            continue
        for m in RE_VEREDICTO_PALABRA.finditer(parrafo):
            pos = m.start()
            despues = [c for c in citas if c[0] > pos]
            antes = [c for c in citas if c[0] <= pos]
            if despues:
                mejor = min(despues, key=lambda c: c[0] - pos)
            else:
                mejor = max(antes, key=lambda c: c[0])
            linea = numero_de_linea(texto, offset_parrafo + pos)
            afirmaciones.append((linea, m.group(1), mejor[1]))
    return afirmaciones


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reporte", default="docs/loop/REPORTE.md")
    ap.add_argument("--commit", default=None,
                    help="si se da, lee --reporte de `git show <commit>:<reporte>` en vez del arbol de trabajo")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    fallos = []
    if a.commit:
        texto = leer_texto_de_commit(a.commit, a.reporte, fallos)
        etiqueta_fuente = "%s:%s" % (a.commit, a.reporte)
    else:
        texto = leer_texto(a.reporte, fallos)
        etiqueta_fuente = a.reporte
    if texto is None:
        print("ROJO, no se pudo leer %s:" % etiqueta_fuente)
        for f in fallos:
            print("   %s" % f)
        return 1

    afirmaciones = hallar_afirmaciones(texto)
    print("=" * 90)
    print("TALLA DE VEREDICTOS de %s: %d afirmacion(es) VERDE/ROJO/PASA/FALLA citan fichero."
          % (etiqueta_fuente, len(afirmaciones)))
    print("=" * 90)

    hallazgos = []
    for linea, palabra, fichero in afirmaciones:
        clase_afirmada = CLASE[palabra]
        clase_real, motivo = veredicto_real_del_fichero(fichero, fallos)
        if motivo is not None:
            hallazgos.append("REPORTE.md linea %d: afirma %s citando `%s`, pero %s"
                             % (linea, palabra, fichero, motivo))
            continue
        if clase_real != clase_afirmada:
            hallazgos.append("REPORTE.md linea %d: afirma %s (clase %s) citando `%s`, "
                             "y el veredicto REAL de ese fichero es %s"
                             % (linea, palabra, clase_afirmada, fichero, clase_real))
        else:
            print("   linea %d: %s citando `%s` -- calza (fichero real: %s)"
                  % (linea, palabra, fichero, clase_real))

    print()
    if hallazgos:
        print("ROJO, %d hallazgo(s):" % len(hallazgos))
        for h in hallazgos:
            print("   %s" % h)
        return 1

    print("VERDE: las %d afirmacion(es) que citan fichero calzan con el veredicto real de su fichero."
          % len(afirmaciones))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
