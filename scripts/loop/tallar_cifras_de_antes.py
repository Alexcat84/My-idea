# -*- coding: utf-8 -*-
r"""tallar_cifras_de_antes.py . EL INSTRUMENTO QUE EXIGE MEDIR TODO "ANTES"
(TAREA 2, BLOQUEANTE, de la vuelta 111, encargo del auditor, acta de la
vuelta 110, seccion 1.2 "TU CAIDA DE EXPEDIENTE").

Nombre estable, SIN numero de vuelta (como tallar_veredictos_reporte.py y
tallar_cabecera_reporte.py): no se clona cada vuelta.

POR QUE NACE. EJECUTOR.md dice, desde el 14 ago 2026, "LA CITA LLEVA SU
LINEA": toda afirmacion sobre un estado ANTERIOR se escribe con la medicion
del dia al lado. Esa regla se escribio dos veces y se salto dos veces: la
vuelta 109 publico "antes de la TAREA 3 era 73/74" sin correr el instrumento
sobre ese estado (caida 4.2 de su acta), y la vuelta 110 repitio la misma
especie en el caso O de su TAREA 2 ("antes y despues, sin apagarse", citando
UN SOLO fichero para los DOS estados). Dos vueltas seguidas de la misma
especie disparan EJECUTOR.md 1 ("la extension del tallador... queda
AUTOMATICAMENTE ENCARGADA"): este fichero es esa extension, puesta en
codigo para que no dependa mas de la memoria de quien escribe el reporte.

QUE MIDE, EXACTO Y NADA MAS.

  (1) Recorre `docs/loop/REPORTE.md` (o el fichero que se pase por
      `--fichero`, para poder correrlo sobre un reporte historico via
      `git show <ref>:docs/loop/REPORTE.md > tmp && --fichero tmp`) LINEA A
      LINEA, y cada linea la separa en ORACIONES (terminadas en `.`, `!` o
      `?`), PROTEGIENDO los tramos entre backticks (\`...\`): un punto
      dentro de un nombre de fichero como \`SALIDA_V110_TAREA2_4_CASO_N_
      ANTES.txt\` NO es un final de oracion. Tambien se normaliza `ª`/`º` a
      `a`/`o` antes de buscar, para que "1.ª operacion" y "1.a operacion"
      cuenten como la misma frase.

  (2) MARCA toda oracion que contenga, con limite de palabra y sin
      distinguir mayusculas, alguna de esta lista CERRADA de palabras
      sueltas: "antes", "previamente", "hoy da", "ya era", "era", "sin el
      arreglo", "pasaba de", "quedaba en". Es la lista literal del encargo,
      no se amplia sin decision del fundador.

  (3) LAS EXCLUSIONES SE DECLARAN, NO SE ESCONDEN (2.2 del encargo). Antes
      de aplicar la vara, toda oracion marcada se cruza contra una lista
      CERRADA de USOS DE ORDEN (instrucciones de secuencia, no afirmaciones
      de estado): "antes de decidir", "antes de nada", "antes de la 1.a
      operacion", "antes de escribir", "antes de tocar", "antes de correr"
      (cubre "antes de correrla" y "antes de correrse", TAREA 4.3 de este
      mismo encargo), "antes de leer", "antes de publicar", "antes de
      mirar". Si la oracion CONTIENE alguna de estas frases Y NINGUNA otra
      marca de la lista (2) le sobra fuera de esa frase, se declara
      EXCLUIDA: se IMPRIME con su numero de linea y su motivo (la frase de
      orden que la excluyo), y no se le aplica la vara. Una exclusion
      callada es un boquete (letra del encargo).

  (4) LA VARA (2.3 del encargo), solo sobre las oraciones marcadas y NO
      excluidas: se buscan las citas a fichero dentro de la MISMA oracion,
      como tokens entre backticks que terminen en `.txt` o `.md`
      (`\`NOMBRE.txt\`` o `\`carpeta/NOMBRE.md\``), y cada cita cuenta solo
      si el fichero EXISTE de verdad en `docs/loop/`. Si la oracion contiene
      ademas un indicio de que tambien habla del otro lado ("despues",
      "después", "hoy" o "ahora", fuera de las frases de orden ya
      excluidas), tiene que traer DOS citas DISTINTAS que existan (una por
      lado); si no, con UNA cita que exista basta. Una oracion marcada sin
      ninguna cita que exista, o con el numero de citas distintas por
      debajo del exigido, ES UN HALLAZGO.

MECANICA DE ROJO: si hay al menos un hallazgo, termina con "ROJO, N
hallazgo(s)" nombrando cada oracion por su numero de linea y su texto, y
exit 1. Si no hay ninguno, "VERDE" y exit 0. Nunca corrige nada: solo mide y
nombra.

USO:
  python scripts/loop/tallar_cifras_de_antes.py
  python scripts/loop/tallar_cifras_de_antes.py --fichero docs/loop/REPORTE.md

CASO POSITIVO OBLIGATORIO (2.4 del encargo, salida commiteada en
docs/loop/SALIDA_V111_TAREA2_4_CASO_POSITIVO.txt): corrido sobre el reporte
de la vuelta 110 tal como quedo commiteado (`git show 27ecfe43:docs/loop/
REPORTE.md`), da ROJO EXIT 1 nombrando LA LINEA DEL CASO O (cita un solo
fichero para "antes y despues") y NO nombra la del caso N (cita dos
ficheros distintos, uno por lado).

CASO ROJO POR MUTACION (2.5 del encargo, salidas commiteadas en
docs/loop/SALIDA_V111_TAREA2_5_MUTACION_ANTES.txt y
docs/loop/SALIDA_V111_TAREA2_5_MUTACION_DESPUES.txt): sobre una copia del
reporte 110 a la que se le quita, a la oracion del caso N, una de sus dos
citas, la oracion tiene que pasar de NO nombrada a NOMBRADA, ROJO EXIT 1.

--- TAREA 2 de la vuelta 112 (acta de la vuelta 111, 4.2 "LA CAIDA GRANDE ES
DE GUARDA QUE NO ALCANZA") ---

POR QUE NACE, CON EL EJEMPLAR DELANTE. Este instrumento resolvia CADA cita
con `os.path.join(LOOP, nombre)`, sin aceptar la forma `carpeta/NOMBRE.md`
que el propio docstring de arriba ya prometia. Esa es la forma que usan
TODAS Y CADA UNA de las citas del reporte de la vuelta 111
(`docs/loop/SALIDA_V111_...txt`): la ruta se resolvia a
`docs/loop/docs/loop/SALIDA_...`, nunca existe, y la cita se descartaba EN
SILENCIO. El hermano mayor `tallar_veredictos_reporte.py` resuelve bien
contra RAIZ y por eso si encontraba esos mismos ficheros: el VERDE de este
instrumento sobre el reporte de la vuelta 111 era VACUO (cero oraciones
marcadas, cero citas evaluadas).

(2.1) `resolver_cita()` ahora acepta LAS DOS FORMAS, copiando la mecanica
del hermano `tallar_veredictos_reporte.py:resolver_cita`: un nombre pelado
(`SALIDA_...txt`) se resuelve contra `docs/loop/`; una ruta que ya trae el
prefijo (`docs/loop/SALIDA_...txt`) se deja tal cual. LOS DOS TALLADORES
RESUELVEN IGUAL desde esta vuelta.

MUTACION S (2.3 del encargo, salidas commiteadas en
docs/loop/SALIDA_V112_TAREA2_3_MUTACION_S_ANTES.txt y
docs/loop/SALIDA_V112_TAREA2_3_MUTACION_S_DESPUES.txt), sobre
`docs/loop/_auditor_v111_mut/sonda_backticks.md` (la sonda del auditor): la
misma oracion, con el mismo fichero citado con el nombre pelado y con la
ruta `docs/loop/` delante. ANTES del arreglo: ROJO, la linea 4 (la de la
ruta con prefijo) sale en "0/1 citas ()" siendo la cita real y existente.
DESPUES: VERDE, las lineas 3 y 4 contadas IGUAL (1/1 cada una).

(2.2) LA LISTA DE MARCAS SE AMPLIA, con el presente y el perfecto de los
mismos verbos que ya traia: "pasa de", "queda en", "quedo en", "daba",
"dio". LA AMPLIA EL AUDITOR POR ENCARGO (acta de la vuelta 111, 4.4): la
letra vieja de este docstring, "es la lista literal del encargo, no se
amplia sin decision del fundador", era de un antecesor y quedo corregida en
esa acta, seccion 4.4 -- la lista la habia cerrado un ENCARGO DEL AUDITOR
(vuelta 110), no una decision del fundador, asi que ampliarla es tambien
del auditor.

MUTACION T (2.4 del encargo, salidas commiteadas en
docs/loop/SALIDA_V112_TAREA2_4_MUTACION_T_ANTES.txt y
docs/loop/SALIDA_V112_TAREA2_4_MUTACION_T_DESPUES.txt), sobre el reporte de
la vuelta 111 tal como quedo commiteado (`git show 9aea9f43:docs/loop/
REPORTE.md`): ANTES del arreglo, VERDE VACUO (cero oraciones marcadas: "pasa
de" no estaba en la lista). DESPUES, MARCA la oracion de la TAREA 2.5 ("la
pasa de OK a hallazgo, ROJO EXIT 1
(`docs/loop/SALIDA_V111_TAREA2_5_MUTACION_DESPUES.txt`)") y la evalua con la
cita ya bien resuelta. EL REPORTE DE LA 111 NO SE REESCRIBE: es historia; lo
que cambia es la MEDICION sobre el, y se publica tal cual sale.
"""
import argparse
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")

MARCAS = [
    "antes", "previamente", "hoy da", "ya era", "era",
    "sin el arreglo", "pasaba de", "quedaba en",
    "pasa de", "queda en", "quedo en", "daba", "dio",
]

EXCLUSIONES_ORDEN = [
    "antes de decidir",
    "antes de nada",
    "antes de la 1.a operacion",
    "antes de escribir",
    "antes de tocar",
    "antes de correr",
    "antes de leer",
    "antes de publicar",
    "antes de mirar",
]

INDICIOS_DEL_OTRO_LADO = ["despues", "después", "hoy", "ahora"]

_RE_MARCAS = re.compile(r"\b(" + "|".join(re.escape(m) for m in
                        sorted(MARCAS, key=len, reverse=True)) + r")\b", re.IGNORECASE)
_RE_EXCLUSIONES = re.compile(r"(" + "|".join(re.escape(e) for e in
                             sorted(EXCLUSIONES_ORDEN, key=len, reverse=True)) + r")", re.IGNORECASE)
_RE_INDICIO = re.compile(r"\b(" + "|".join(re.escape(i) for i in INDICIOS_DEL_OTRO_LADO) + r")\b",
                         re.IGNORECASE)
_RE_CITA = re.compile(r"`([^`]+\.(?:txt|md))`")


def resolver_cita(nombre):
    """(2.1, vuelta 112) Devuelve la ruta relativa a RAIZ para NOMBRE,
    aceptando las DOS formas que el docstring de este modulo ya prometia: el
    nombre pelado (SALIDA_...txt, resuelto contra docs/loop/) y la ruta ya
    relativa a la raiz (docs/loop/SALIDA_...txt, dejada tal cual). Antes de
    esta vuelta el codigo hacia SIEMPRE os.path.join(LOOP, nombre), asi que
    una cita con el prefijo se resolvia a docs/loop/docs/loop/SALIDA_...,
    que nunca existe: TODAS las citas del reporte de la vuelta 111 usaban esa
    forma y se descartaban en silencio (acta de la vuelta 111, 4.2). Mismo
    mecanismo que el hermano tallar_veredictos_reporte.py:resolver_cita: los
    dos talladores resuelven igual."""
    if nombre.startswith("docs/loop/"):
        return nombre
    return "docs/loop/%s" % nombre


def _normalizar(texto):
    return texto.replace("ª", "a").replace("º", "o")


def _proteger_backticks(linea):
    """Sustituye los puntos DENTRO de tramos entre backticks por un
    marcador, para que la particion en oraciones no los tome por un final
    de frase. Se restauran despues de partir."""
    partes = linea.split("`")
    for i in range(1, len(partes), 2):
        partes[i] = partes[i].replace(".", "\x00")
    return "`".join(partes)


def _restaurar(texto):
    return texto.replace("\x00", ".")


def oraciones_de_la_linea(num_linea, linea_original):
    linea = _normalizar(linea_original)
    protegida = _proteger_backticks(linea)
    trozos = re.split(r"(?<=[.!?])\s+", protegida)
    resultado = []
    for t in trozos:
        t = _restaurar(t).strip()
        if t:
            resultado.append((num_linea, t))
    return resultado


def clasificar(oracion):
    """Devuelve uno de: None (no marcada), 'excluida' (con su motivo),
    o un dict con el hallazgo/veredicto de la vara."""
    if not _RE_MARCAS.search(oracion):
        return None

    exc = _RE_EXCLUSIONES.search(oracion)
    if exc:
        # Solo se declara EXCLUIDA si, quitando la frase de orden, no
        # queda ninguna otra marca suelta en el resto de la oracion.
        resto = oracion[:exc.start()] + oracion[exc.end():]
        if not _RE_MARCAS.search(resto):
            return {"tipo": "excluida", "motivo": exc.group(1)}

    citas = []
    for m in _RE_CITA.finditer(oracion):
        nombre = m.group(1)
        ruta = os.path.join(RAIZ, resolver_cita(nombre))
        if os.path.exists(ruta) and nombre not in citas:
            citas.append(nombre)

    exige_dos = bool(_RE_INDICIO.search(oracion))
    requeridas = 2 if exige_dos else 1
    if len(citas) >= requeridas:
        return {"tipo": "ok", "citas": citas, "requeridas": requeridas}
    return {"tipo": "hallazgo", "citas": citas, "requeridas": requeridas}


def verificar(ruta_fichero):
    with open(ruta_fichero, encoding="utf-8") as f:
        lineas = f.readlines()

    excluidas = []
    hallazgos = []
    ok = []
    for i, linea in enumerate(lineas, start=1):
        for num_linea, oracion in oraciones_de_la_linea(i, linea):
            veredicto = clasificar(oracion)
            if veredicto is None:
                continue
            if veredicto["tipo"] == "excluida":
                excluidas.append((num_linea, oracion, veredicto["motivo"]))
            elif veredicto["tipo"] == "hallazgo":
                hallazgos.append((num_linea, oracion, veredicto["citas"], veredicto["requeridas"]))
            else:
                ok.append((num_linea, oracion, veredicto["citas"], veredicto["requeridas"]))
    return excluidas, hallazgos, ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fichero", default=os.path.join(LOOP, "REPORTE.md"))
    a = ap.parse_args()

    if not os.path.exists(a.fichero):
        print("ROJO: no existe %s" % a.fichero)
        return 1

    excluidas, hallazgos, ok = verificar(a.fichero)

    print("EXCLUSIONES (%d), letra del encargo 'no se esconden':" % len(excluidas))
    for num_linea, oracion, motivo in excluidas:
        print("   linea %d, motivo '%s': %s" % (num_linea, motivo, oracion))

    print()
    print("ORACIONES QUE CUMPLEN LA VARA (%d):" % len(ok))
    for num_linea, oracion, citas, req in ok:
        print("   linea %d, %d/%d citas (%s): %s" % (num_linea, len(citas), req, ", ".join(citas), oracion))

    print()
    if hallazgos:
        print("ROJO, %d hallazgo(s):" % len(hallazgos))
        for num_linea, oracion, citas, req in hallazgos:
            print("   linea %d, %d/%d citas (%s): %s" % (num_linea, len(citas), req, ", ".join(citas), oracion))
        return 1

    print("VERDE: ninguna oracion marcada incumple la vara.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
