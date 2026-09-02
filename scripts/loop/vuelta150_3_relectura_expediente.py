# -*- coding: utf-8 -*-
"""vuelta150_3_relectura_expediente.py . LA RELECTURA AL DOBLE DEL TRAMO DEL
EXPEDIENTE (TAREA 3 de la vuelta 150), encargada por el acta 149 seccion 5 al
amparo de AUDITOR.md 1.2.

RECORRE LAS 71 FICHAS DE docs/plan/OPERACIONES.jsonl y coteja el campo `estado`
contra LO QUE EL REPO DICE QUE SE EJECUTO. Publica la tabla de las que NO CALZAN
y CERO de las que si: la tabla corta es la que se lee.

EL CRITERIO (TAREA 3.b), DECLARADO AQUI Y MEDIBLE CONTRA EL REPO, NUNCA CONTRA
UN ACTA. Una operacion cuenta como EJECUTADA si al menos una de estas tres
pruebas da positivo, y SIEMPRE se dice cual:

  (P1) VARA DE GRAFO. `scripts/loop/tallar_estado_de_fase.py` dice DESTINO
       CUMPLIDO para esa operacion. Es la unica de las tres que mira el DATO.
       Fuente escrita: acta 139, TAREA 2.a, y sus afinados de las vueltas 141 y
       142. No se reimplementa aqui: se invoca el instrumento y se lee su
       tabla, que es lo contrario de tener dos varas divergentes.

  (P2) VARA DE CODIGO, MITAD DE PRESENCIA. El `id_op` aparece hoy en el codigo
       vivo (`scripts/`, `engine/`, `web/lib/`), excluyendo `scripts/loop/`, que
       es el cuaderno del bucle y no el producto. Fuente escrita: adjudicacion
       3.9 del acta 144, "una operacion que no deja huella en el grafo... se
       mide contra LO QUE INSTALA, y para un control eso significa dos cosas y
       solo dos: que el control EXISTA en el codigo y que MUERDA por mutacion".
       AQUI SE MIDE SOLO LA PRIMERA MITAD Y SE DICE: la segunda (que muerda) se
       prueba por mutacion una a una y no se puede barrer para 71 fichas en una
       vuelta. Una P2 sola NO es prueba de que el control funcione; es prueba de
       que esta instalado.

  (P3) HUELLA EN GIT. Existe al menos un commit de la rama activa cuyo MENSAJE
       nombra el `id_op` Y que ademas toca `dataset/`, `scripts/`, `engine/` o
       `web/`. La segunda condicion es la que separa una EJECUCION de un
       REGISTRO: un commit que solo mueve `docs/` esta anotando el plan, no
       corriendolo. Es el registro que el repo lleva de si mismo, leido con
       `git log`, no una memoria.

NO CALZA cuando:
  - `estado` dice `LISTA` y alguna prueba dice ejecutada, SIN que la ficha
    declare por que sigue congelada; o
  - `estado` dice `HECHA` y NINGUNA prueba dice ejecutada.

UN ESTADO CONGELADO A PROPOSITO ES LEGITIMO SI LO DICE (acta 149, 4.2). Aqui se
mide si lo dice: se busca en el campo `nota` o `adjudicacion` de la propia ficha
una mencion explicita a su `estado`. Si la trae, la fila sale como CONGELADO
DECLARADO y no como incumplimiento; si no la trae, sale como CONGELADO EN
SILENCIO, que es exactamente la caida 4.2 del acta 149.

TAREA 3.c: al final lista las operaciones DESBLOQUEADAS, o sea con `estado`
LISTA y TODAS sus `depende_de` en `HECHA`, con su `depende_de` medido al lado.

USO:
  python scripts/loop/vuelta150_3_relectura_expediente.py
"""
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
FASES = ["00_CODIGO", "01_FUENTES", "02_DESTEJIDOS", "03_FUSIONES", "04_ENLACES",
         "05_SANEO", "06_MESAS", "07_ADUANA", "08_VERIFICACION",
         "09_LECTURAS_DIRIGIDAS", "10_INVENTARIO"]


def fichas():
    return [json.loads(x) for x in io.open(OPS, encoding="utf-8").read().splitlines() if x.strip()]


def p1_vara_de_grafo():
    """Invoca tallar_estado_de_fase.py para cada fase y lee su tabla. Devuelve
    {id_op: (veredicto, fase_en_que_salio)}."""
    out = {}
    for fase in FASES:
        r = subprocess.run(["python", os.path.join("scripts", "loop", "tallar_estado_de_fase.py"),
                            "--fase", fase], capture_output=True, cwd=RAIZ)
        texto = r.stdout.decode("utf-8", "replace")
        for linea in texto.splitlines():
            if not linea.strip().startswith("|"):
                continue
            celdas = [c.strip().strip("`*") for c in linea.strip().strip("|").split("|")]
            if not celdas or not re.match(r"^OP-[A-Z]+-\d", celdas[0]):
                continue
            idop = celdas[0]
            cumplido = "CUMPLIDO" in linea.upper() and "NO CUMPLIDO" not in linea.upper()
            if idop not in out or cumplido:
                out[idop] = (cumplido, fase, linea.strip())
    return out


def p2_vara_de_codigo(ids):
    """El id_op aparece en el codigo vivo. scripts/loop/ queda FUERA: es el
    cuaderno del bucle, no el producto."""
    hits = {i: [] for i in ids}
    for base in ("scripts", "engine", os.path.join("web", "lib")):
        raiz = os.path.join(RAIZ, base)
        for dirpath, dirnames, filenames in os.walk(raiz):
            dirnames[:] = [d for d in dirnames
                           if d not in ("__pycache__", "node_modules", "loop")]
            for nombre in filenames:
                if not nombre.endswith((".py", ".ts", ".tsx", ".js", ".json")):
                    continue
                ruta = os.path.join(dirpath, nombre)
                try:
                    texto = io.open(ruta, encoding="utf-8", errors="replace").read()
                except OSError:
                    continue
                for i in ids:
                    # FRONTERA DE PALABRA, y no es cosmetica: `OP-M-01` es
                    # PREFIJO LITERAL de `OP-M-01-FUSION` y de
                    # `OP-M-01-ESLABONES`, asi que un `in` crudo le regalaria a
                    # la madre la huella de sus hijas. Se exige que detras del
                    # id no venga otro segmento del mismo id.
                    if re.search(re.escape(i) + r"(?![A-Za-z0-9_-])", texto):
                        hits[i].append(os.path.relpath(ruta, RAIZ).replace("\\", "/"))
    return hits


def p3_huella_en_git(ids):
    """Commits de la rama activa cuyo mensaje nombra el id_op Y que tocan
    dataset/, scripts/, engine/ o web/."""
    hits = {}
    for i in ids:
        # MISMA FRONTERA DE PALABRA que en P2, por el mismo motivo: sin ella
        # `OP-M-01` heredaria los commits de `OP-M-01-FUSION`.
        r = subprocess.run(["git", "log", "--format=%H", "-E", "--grep",
                            re.escape(i) + "([^A-Za-z0-9_-]|$)"], capture_output=True, cwd=RAIZ)
        commits = [c for c in r.stdout.decode().split() if c]
        con_codigo = []
        for c in commits:
            n = subprocess.run(["git", "show", "--name-only", "--format=", c],
                               capture_output=True, cwd=RAIZ).stdout.decode("utf-8", "replace")
            rutas = [x for x in n.splitlines() if x.strip()]
            if any(x.startswith(("dataset/", "scripts/", "engine/", "web/")) for x in rutas):
                con_codigo.append(c[:8])
        hits[i] = (len(commits), con_codigo)
    return hits


def declara_su_estado(f):
    """La ficha dice algo explicito sobre su propio campo estado."""
    texto = " ".join(str(f.get(k) or "") for k in ("nota", "adjudicacion"))
    t = texto.upper()
    for marca in ("ESTADO", "DIFERIDA", "CONGELAD", "SIGUE EN LISTA", "NO SE MUEVE"):
        if marca in t:
            return True, marca
    return False, None


def main():
    F = fichas()
    ids = [f["id_op"] for f in F]
    print("FICHAS EN docs/plan/OPERACIONES.jsonl: %d" % len(F))
    assert len(set(ids)) == len(ids), "hay ids duplicados"

    print("")
    print("CRITERIO (TAREA 3.b): las tres pruebas estan escritas en el docstring de")
    print("este fichero, cada una con la fuente que la autoriza. Se dice SIEMPRE cual")
    print("de las tres sostiene cada fila.")
    print("")

    v1 = p1_vara_de_grafo()
    v2 = p2_vara_de_codigo(ids)
    v3 = p3_huella_en_git(ids)

    print("COBERTURA DE CADA PRUEBA, CONTADA:")
    print("  P1 vara de grafo: %d ficha(s) con veredicto computable, %d con DESTINO CUMPLIDO"
          % (len(v1), sum(1 for k in v1 if v1[k][0])))
    print("  P2 vara de codigo (presencia): %d ficha(s) con el id_op en codigo vivo"
          % sum(1 for i in ids if v2[i]))
    print("  P3 huella en git (mensaje + rutas de codigo o dato): %d ficha(s)"
          % sum(1 for i in ids if v3[i][1]))
    print("")

    filas_malas = []
    congelados_declarados = 0
    calzan = 0
    for f in F:
        i = f["id_op"]
        estado = f["estado"]
        pruebas = []
        if v1.get(i, (False,))[0]:
            pruebas.append("P1")
        if v2[i]:
            pruebas.append("P2")
        if v3[i][1]:
            pruebas.append("P3")
        ejecutada = bool(pruebas)
        if estado == "HECHA" and ejecutada:
            calzan += 1
            continue
        if estado == "LISTA" and not ejecutada:
            calzan += 1
            continue
        if estado == "LISTA" and ejecutada:
            dice, marca = declara_su_estado(f)
            if dice:
                congelados_declarados += 1
                filas_malas.append((i, f["fase"], estado, "+".join(pruebas),
                                    "CONGELADO DECLARADO (la ficha habla de su estado: %s)" % marca,
                                    v2[i][:2], v3[i][1][:3]))
            else:
                filas_malas.append((i, f["fase"], estado, "+".join(pruebas),
                                    "CONGELADO EN SILENCIO: la ficha no dice nada de su estado",
                                    v2[i][:2], v3[i][1][:3]))
        elif estado == "HECHA" and not ejecutada:
            filas_malas.append((i, f["fase"], estado, "ninguna",
                                "HECHA SIN NINGUNA PRUEBA: el estado afirma mas que el repo",
                                v2[i][:2], v3[i][1][:3]))

    print("=" * 100)
    print("TABLA DE LAS QUE NO CALZAN (%d de %d). Las %d que calzan NO se imprimen."
          % (len(filas_malas), len(F), calzan))
    print("=" * 100)
    print("| id_op | fase | estado | pruebas | motivo |")
    print("|---|---|---|---|---|")
    for i, fase, estado, pr, motivo, _c, _g in filas_malas:
        print("| `%s` | %s | %s | %s | %s |" % (i, fase, estado, pr, motivo))
    print("")
    print("DESGLOSE, con la evidencia de cada fila:")
    for i, fase, estado, pr, motivo, cod, gits in filas_malas:
        print("  %s (%s, estado %s)" % (i, fase, estado))
        print("    pruebas que dan positivo: %s" % (pr or "ninguna"))
        if cod:
            print("    P2, en codigo vivo: %s" % ", ".join(cod))
        if gits:
            print("    P3, commits con codigo o dato: %s" % ", ".join(gits))
    print("")
    print("CONTADO: no calzan %d | de ellas, congeladas DECLARADAS %d | congeladas EN SILENCIO %d | HECHA sin prueba %d"
          % (len(filas_malas), congelados_declarados,
             sum(1 for x in filas_malas if "SILENCIO" in x[4]),
             sum(1 for x in filas_malas if "HECHA SIN" in x[4])))

    print("")
    print("=" * 100)
    print("TAREA 3.c: OPERACIONES DESBLOQUEADAS, con su depende_de MEDIDO")
    print("=" * 100)
    por_id = {f["id_op"]: f for f in F}
    desbloqueadas = []
    for f in F:
        if f["estado"] != "LISTA":
            continue
        dep = f.get("depende_de") or []
        estados_dep = [(d, por_id[d]["estado"] if d in por_id else "NO EXISTE") for d in dep]
        if all(e == "HECHA" for _d, e in estados_dep) and dep:
            desbloqueadas.append((f, estados_dep))
    print("Criterio: estado LISTA y TODAS sus depende_de en HECHA. Las de depende_de VACIO")
    print("no entran: nunca estuvieron bloqueadas y contarlas aqui seria ruido.")
    print("")
    print("| id_op | fase | tipo | depende_de medido |")
    print("|---|---|---|---|")
    for f, ed in desbloqueadas:
        print("| `%s` | %s | %s | %s |"
              % (f["id_op"], f["fase"], f["tipo"],
                 ", ".join("%s=%s" % (d, e) for d, e in ed)))
    print("")
    print("CONTADO: %d operacion(es) LISTA con todas sus dependencias en HECHA." % len(desbloqueadas))
    sin_dep = [f for f in F if f["estado"] == "LISTA" and not (f.get("depende_de") or [])]
    print("CONTRASTE: %d operacion(es) LISTA con depende_de VACIO (nunca bloqueadas)." % len(sin_dep))

    print("")
    print("Y LO QUE DE VERDAD QUEDA POR CORRER: las fichas en LISTA SIN NINGUNA de las")
    print("tres pruebas. Son las unicas cuyo estado LISTA calza con el repo, o sea las")
    print("unicas que el expediente y el arbol dicen a la vez que no se han ejecutado.")
    print("")
    print("| id_op | fase | tipo | depende_de medido |")
    print("|---|---|---|---|")
    pendientes = 0
    for f in F:
        i = f["id_op"]
        if f["estado"] != "LISTA":
            continue
        if v1.get(i, (False,))[0] or v2[i] or v3[i][1]:
            continue
        pendientes += 1
        dep = f.get("depende_de") or []
        medido = ", ".join("%s=%s" % (d, por_id[d]["estado"] if d in por_id else "NO EXISTE")
                           for d in dep) or "(vacio)"
        print("| `%s` | %s | %s | %s |" % (i, f["fase"], f["tipo"], medido))
    print("")
    print("CONTADO: %d ficha(s) en LISTA sin ninguna prueba de ejecucion." % pendientes)


main()
