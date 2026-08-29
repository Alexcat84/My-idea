# -*- coding: utf-8 -*-
r"""verificar_cifras_del_plan.py . LA GUARDA CONTRA LA RACHA DE CIFRA
PUBLICADA (TAREA 1.f de la vuelta 123, acta de la vuelta 122, seccion 4.1 y
"RACHAS": "CLASE O CIFRA PUBLICADA DEL EJECUTOR: SUBE DE CERO A UNO... SI LA
VUELTA 123 TRAE OTRA DE ESTA CLASE, ES PARADA").

POR QUE NACE. La 122 escribio, en el punto 0 de `verificacion` de `OP-S-08`,
"prueba propia en web/lib/engine/accesosResueltos.test.ts (32 casos, verde en
SALIDA_V122_WEB_APERTURA.txt)". La suite tiene 27 casos (`npx vitest run`).
NO es la escalada de EJECUTOR.md 1.2 (esa es de racha de REPORTE, no de cifra
publicada); es una guarda de codigo nueva y propia, bloqueante, para que una
cifra de esta clase (numero de casos de una suite, citando su ruta) no pueda
volver a colarse SIN que algo la muerda antes del commit.

CONTRATO (exacto, del encargo del auditor, TAREA 1.f de la vuelta 123):
  - Toma --base <ref> (por defecto, el commit ACTA DE LA VUELTA <N> DEL
    AUDITOR mas reciente de la rama actual: "el acta anterior") y compara
    docs/plan/OPERACIONES.jsonl entre --base y el arbol de trabajo (o
    --work <ruta>, para poder correr la guarda sobre una COPIA sin tocar el
    fichero real, que es lo que exige su propio caso positivo).
  - Para cada fila cuyo id_op aparezca en las dos versiones y haya cambiado,
    calcula el TEXTO ANADIDO de cada campo de texto (str o lista de str): la
    parte nueva que no estaba en la version base, por diff de secuencias
    (difflib), no una resta de substrings.
  - Sobre ESE texto anadido busca, con vocabulario CERRADO, pares (numero,
    artefacto): un numero seguido de "caso", "casos", "test", "tests",
    "prueba" o "pruebas", en la MISMA frase (partida por punto, sin partir
    puntos de miles) que una ruta citada que termine en ".test.ts".
  - Para cada par: corre `npx vitest run <ruta sin el prefijo web/>` desde
    web/ y lee la linea "Tests  N passed". Si N no es el numero escrito,
    ROJO EXIT 1 diciendo el id_op, el campo, el numero escrito, el numero
    real y la ruta.
  - Si la ruta citada no existe, ROJO.
  - Si no hay ningun par, VERDE EXIT 0 diciendo "0 pares" y las filas que
    examino (los id_op que cambiaron), para que se vea que corrio.
  - Si cuadran todos, VERDE EXIT 0 con el recuento.

La guarda NO corrige nada: solo lee, compara contra vitest, y grita.

USO:
  python scripts/loop/verificar_cifras_del_plan.py
  python scripts/loop/verificar_cifras_del_plan.py --base ed916471
  python scripts/loop/verificar_cifras_del_plan.py --base ed916471 --work RUTA

CASO POSITIVO (vuelta 123, criterio de HECHO de la fase 08: "una fase esta
hecha cuando su verificacion se caeria si el fallo volviera"):
`scripts/loop/vuelta123_tarea1f_caso_positivo.py` corre esta guarda con
`--base ed916471` (el acta de la vuelta 121, ANTERIOR a que la 122 escribiera
la cifra) contra una COPIA de docs/plan/OPERACIONES.jsonl TAL COMO ESTABA
ANTES de la correccion 2.a de esta misma vuelta (el punto 0 de `OP-S-08`
todavia dice "32 casos"): tiene que dar ROJO nombrando `OP-S-08`, 32 contra
27, y `web/lib/engine/accesosResueltos.test.ts`. Y una segunda corrida, sobre
el fichero YA CORREGIDO por la 2.a, con el mismo `--base`, tiene que dar
VERDE.
"""
import argparse
import difflib
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_PLAN = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

PATRON_NUMERO_ARTEFACTO = re.compile(
    r"\b(\d+)\s+(?:casos?|tests?|pruebas?)\b", re.IGNORECASE)
PATRON_RUTA_TEST = re.compile(r"([A-Za-z0-9_./\\-]+\.test\.ts)")


def _git(args, contexto):
    # encoding="utf-8" EXPLICITO: en Windows, subprocess.run(text=True) sin
    # encoding decodifica con la codificacion de consola (cp1252/cp437), no
    # UTF-8, y mutila cualquier tilde o eñe del blob (hallado al probar esta
    # guarda: "campaña" salia "campa�a" via git show y comparaba
    # distinto contra el mismo texto leido con io.open(encoding="utf-8")).
    try:
        r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True, text=True,
                           encoding="utf-8", check=True)
        return r.stdout
    except Exception as e:
        raise SystemExit("ROJO (arnes): no se pudo correr git %s (%s): %s" % (" ".join(args), contexto, e))


def commit_acta_mas_reciente():
    rama = _git(["rev-parse", "--abbrev-ref", "HEAD"], "rama actual").strip()
    out = _git(["log", rama, "--pretty=format:%H\x01%s"], "git log de la rama")
    patrones = [
        re.compile(r"^ACTA DE LA VUELTA (\d+) DEL AUDITOR\b"),
        re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA (\d+)\b"),
    ]
    for linea in out.splitlines():
        if "\x01" not in linea:
            continue
        h, s = linea.split("\x01", 1)
        if any(p.match(s) for p in patrones):
            return h
    raise SystemExit("ROJO (arnes): ningun commit 'ACTA DE LA VUELTA N DEL AUDITOR' en la rama %s" % rama)


def leer_jsonl_texto(texto):
    filas = {}
    orden = []
    for linea in texto.splitlines():
        linea = linea.strip()
        if not linea:
            continue
        d = json.loads(linea)
        filas[d["id_op"]] = d
        orden.append(d["id_op"])
    return filas, orden


def leer_base(ref):
    out = _git(["show", "%s:docs/plan/OPERACIONES.jsonl" % ref], "leer base %s" % ref)
    return leer_jsonl_texto(out)


def leer_work(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return leer_jsonl_texto(f.read())


def campos_de_texto(fila):
    """node id_op -> {campo: texto_plano}, uniendo listas de str con '\n'."""
    out = {}
    for k, v in fila.items():
        if isinstance(v, str):
            out[k] = v
        elif isinstance(v, list) and all(isinstance(x, str) for x in v):
            out[k] = "\n".join(v)
    return out


def texto_anadido(base_txt, work_txt):
    """La parte de work_txt que NO estaba en base_txt, por diff de secuencias
    (difflib), concatenando los tramos 'insert' y 'replace' del lado nuevo.

    Los trozos se unen con '\n' ENTRE ELLOS, nunca pegados: si no se separan,
    dos tramos anadidos que en el texto real quedaban lejos (por ejemplo, en
    dos elementos distintos de una lista, cuando el '\n' que los separaba
    coincidia por casualidad entre base y work y quedaba fuera del tramo
    'insert'/'replace') se sueldan en una sola frase y fabrican un par falso
    (hallado al probar esta guarda contra OP-S-08: "accesosResueltos.test.ts"
    del elemento 2 se colaba en la misma frase que "32 casos" del elemento 1
    anterior)."""
    sm = difflib.SequenceMatcher(None, base_txt, work_txt, autojunk=False)
    trozos = [work_txt[j1:j2] for tag, i1, i2, j1, j2 in sm.get_opcodes()
              if tag in ("insert", "replace")]
    return "\n".join(trozos)


def dividir_frases(texto):
    """Parte primero por LINEA (una lista de str se une con '\n', y un
    elemento de la lista NUNCA se mezcla con el siguiente aunque no acabe en
    punto: hallado al probar esta guarda, un "tres frentes" del elemento
    verificacion[1] se colaba en la misma frase que "32 casos" del
    verificacion[0] anterior, fabricando un par falso con una ruta sin
    directorio). Dentro de cada linea, parte por punto seguido de
    espacio/fin, sin partir un punto de miles (siempre trae otro digito
    pegado detras)."""
    frases = []
    for linea in texto.split("\n"):
        if not linea.strip():
            continue
        p = 0
        for m in re.finditer(r"\.(?!\d)(?:\s+|$)", linea):
            frases.append(linea[p:m.end()])
            p = m.end()
        if p < len(linea) and linea[p:].strip():
            frases.append(linea[p:])
    return frases


def pares_en_texto(texto):
    """[(numero:int, ruta:str), ...] hallados en la MISMA frase."""
    pares = []
    for frase in dividir_frases(texto):
        rutas = PATRON_RUTA_TEST.findall(frase)
        if not rutas:
            continue
        for m in PATRON_NUMERO_ARTEFACTO.finditer(frase):
            for ruta in rutas:
                pares.append((int(m.group(1)), ruta))
    return pares


def numero_real_de_vitest(ruta):
    """Corre `npx vitest run <ruta sin prefijo web/>` desde web/ y lee
    'Tests  N passed'. Devuelve (numero_o_None, salida_completa)."""
    ruta_rel = ruta[len("web/"):] if ruta.startswith("web/") else ruta
    web_dir = os.path.join(RAIZ, "web")
    r = subprocess.run(["npx", "vitest", "run", ruta_rel], cwd=web_dir,
                       capture_output=True, text=True, shell=(os.name == "nt"))
    salida = r.stdout + r.stderr
    m = re.search(r"Tests\s+(\d+)\s+passed", salida)
    return (int(m.group(1)) if m else None), salida


def verificar(base_ref, ruta_work):
    base_filas, _ = leer_base(base_ref)
    work_filas, work_orden = leer_work(ruta_work)

    filas_cambiadas = []
    for id_op in work_orden:
        if id_op not in base_filas:
            continue
        if work_filas[id_op] == base_filas[id_op]:
            continue
        filas_cambiadas.append(id_op)

    fallos = []
    pares_vistos = []
    for id_op in filas_cambiadas:
        base_campos = campos_de_texto(base_filas[id_op])
        work_campos = campos_de_texto(work_filas[id_op])
        for campo, work_txt in work_campos.items():
            base_txt = base_campos.get(campo, "")
            if work_txt == base_txt:
                continue
            anadido = texto_anadido(base_txt, work_txt)
            for numero, ruta in pares_en_texto(anadido):
                ruta_abs = os.path.join(RAIZ, ruta.replace("/", os.sep))
                if not os.path.exists(ruta_abs):
                    fallos.append('%s.%s: cita `%s`, que NO EXISTE' % (id_op, campo, ruta))
                    continue
                real, salida_vitest = numero_real_de_vitest(ruta)
                if real is None:
                    fallos.append('%s.%s: no se pudo leer "Tests N passed" de vitest sobre `%s`'
                                  % (id_op, campo, ruta))
                    continue
                pares_vistos.append((id_op, campo, numero, real, ruta))
                if real != numero:
                    fallos.append('%s.%s: escribe %d, vitest da %d, en `%s`'
                                  % (id_op, campo, numero, real, ruta))
    return fallos, pares_vistos, filas_cambiadas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=None)
    ap.add_argument("--work", default=RUTA_PLAN)
    a = ap.parse_args()

    base_ref = a.base or commit_acta_mas_reciente()
    fallos, pares_vistos, filas_cambiadas = verificar(base_ref, a.work)

    if fallos:
        print("ROJO, %d cosa(s) no cuadran (base %s, work %s):" % (len(fallos), base_ref[:8], a.work))
        for f in fallos:
            print("  " + f)
        return 1

    if not pares_vistos:
        print("VERDE EXIT 0: 0 pares (base %s). Filas cambiadas examinadas (%d): %s"
              % (base_ref[:8], len(filas_cambiadas), ", ".join(filas_cambiadas) or "ninguna"))
        return 0

    print("VERDE EXIT 0: %d par(es) cotejados contra vitest (base %s), todos cuadran:"
          % (len(pares_vistos), base_ref[:8]))
    for id_op, campo, numero, real, ruta in pares_vistos:
        print("  %s.%s: %d == %d en `%s`" % (id_op, campo, numero, real, ruta))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
