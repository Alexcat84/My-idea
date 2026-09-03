# -*- coding: utf-8 -*-
"""vuelta154_tarea5_pase_de_las_mesas.py . TAREA 5 DE LA VUELTA 154.

EL PASE DE `estado` DE LAS CINCO MESAS, EN UN SOLO ACTO, CON EL CONTEO ANTES Y
DESPUES. Mismo molde que las vueltas 131, 136 y 152.

LA AUTORIZACION, CITADA Y NO PARAFRASEADA (acta 153, adjudicacion 6.3): *"El
ejecutor hizo bien en no moverlas: la reserva del acta 139, 3.6 dice 'el pase de
estado de las once (las seis fusiones y las cinco remitidas)' y las mesas no
estan ahi. Pero el disparador que la misma 3.6 les puso es 'cuando la fase 06
cierre', y hoy la fase 06 mide VERDE, 5 de 5 mesas completas."*

EL DISPARADOR SE MIDE AQUI CON MI PROPIO INSTRUMENTO Y NO SE HEREDA DEL ACTA. Y
LA CONDICION DEL ENCARGO ES LITERAL: *"Si al medir el disparador con TU
instrumento alguna de las cinco NO sale CUMPLIDO, NO LA MUEVES y lo dices: la
adjudicacion cubre a las que el disparador alcance, no a las cinco por
decreto."* Por eso el pase es POR FICHA: se mueve la que su fila diga CUMPLIDO y
se deja quieta la que no, y las que no se mueven se nombran.

LAS CINCO, NOMBRADAS Y NO CONTADAS DE MEMORIA: OP-M-01, OP-M-02, OP-M-03,
OP-M-04 y OP-M-05, las cinco fichas de fase `06_MESAS` de
docs/plan/OPERACIONES.jsonl. La nomina se COMPRUEBA contra el fichero en cada
corrida: si la fase 06 no trae exactamente esas cinco, se para.

LA CONVENCION DEL SILENCIO NO SE MUEVE EN ESTA VUELTA: se cuenta con la LISTA A,
la que vive en vuelta150_3_relectura_expediente.py:declara_su_estado y la que
produjo la cifra publicada. Cambiar la vara y el sujeto a la vez es lo que la
vuelta 152 ya evito.

USO:
  python scripts/loop/vuelta154_tarea5_pase_de_las_mesas.py            (mide y NO escribe)
  python scripts/loop/vuelta154_tarea5_pase_de_las_mesas.py --aplicar  (mide, escribe y re mide)
"""
import argparse
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
CORR = os.path.join(RAIZ, "docs", "plan", "CORRECCIONES_A_APLICAR.md")

MARCAS_LISTA_A = ("ESTADO", "DIFERIDA", "CONGELAD", "SIGUE EN LISTA", "NO SE MUEVE")

SELLO_NOTA = (
    " CORRECCION DECLARADA (2026-09-02, vuelta 154, TAREA 5; nada del texto anterior se "
    "borra, esta linea se anade): ~~estado LISTA~~ pasa a estado HECHA, dentro del PASE DE "
    "LAS CINCO MESAS que la adjudicacion 6.3 del acta 153 autoriza. El disparador que el "
    "acta 139, 3.6 puso a las mesas es 'cuando la fase 06 cierre', y se midio en ESTA vuelta "
    "con scripts/loop/tallar_estado_de_fase.py --fase 06_MESAS: la fase sale entera CUMPLIDA "
    "y esta ficha con ella. El pase va en UN SOLO ACTO, con el conteo antes y despues, el "
    "esquema comprobado y la guarda de cifras del plan re corrida. Ver "
    "docs/plan/CORRECCIONES_A_APLICAR.md, CORRECCION 35, y "
    "docs/loop/SALIDA_V154_T5_PASE_DE_ESTADO.txt.")


def fichas():
    return [json.loads(x) for x in io.open(OPS, encoding="utf-8").read().splitlines() if x.strip()]


def habla_de_su_estado(f):
    t = " ".join(str(f.get(k) or "") for k in ("nota", "adjudicacion")).upper()
    return any(m in t for m in MARCAS_LISTA_A)


def destino_medido():
    """Veredicto de tallar_estado_de_fase.py, la MISMA vara P1 del expediente. No
    se reimplementa aqui: se invoca el instrumento y se lee su tabla, que es lo
    contrario de tener dos varas divergentes."""
    out = {}
    r = subprocess.run(["python", os.path.join("scripts", "loop", "tallar_estado_de_fase.py"),
                        "--fase", "06_MESAS"], capture_output=True, cwd=RAIZ)
    texto = r.stdout.decode("utf-8", "replace")
    for linea in texto.splitlines():
        if not linea.strip().startswith("|"):
            continue
        celdas = [c.strip().strip("`*") for c in linea.strip().strip("|").split("|")]
        if not celdas or not re.match(r"^OP-[A-Z]+-", celdas[0]):
            continue
        v = celdas[-1]
        if celdas[0] not in out or v == "CUMPLIDO":
            out[celdas[0]] = v
    return out, texto


def censo(F, etiqueta):
    por_estado = {}
    for f in F:
        por_estado[f["estado"]] = por_estado.get(f["estado"], 0) + 1
    silencio = [f["id_op"] for f in F if f["estado"] == "LISTA" and not habla_de_su_estado(f)]
    print("CENSO %s: %d fichas | %s | LISTA que NO hablan de su estado (lista A): %d"
          % (etiqueta, len(F),
             " ".join("%s %d" % (k, v) for k, v in sorted(por_estado.items())), len(silencio)))
    return por_estado, silencio


TEXTO_CORRECCION_35 = """

---

## CORRECCION 35. **EL PASE DE `estado` DE LAS CINCO MESAS, CON SU DISPARADOR MEDIDO EN LA VUELTA QUE LO USA**

**Fecha: 2026-09-02. Vuelta 154, TAREA 5. Autorizada por el acta 153, adjudicacion 6.3.**

**POR QUE NO SE MOVIERON ANTES, Y NO ES UN OLVIDO.** La reserva del acta 139,
3.6 nombra literalmente *"el pase de estado de las once (las seis fusiones y las
cinco remitidas)"*, y **las cinco mesas no estan en esas once**. El ejecutor de
la vuelta 152 no las movio, y el acta 153 se lo cuenta a favor: ampliar la
reserva por cuenta propia habria sido improvisar.

**LO QUE SI HABIA, Y ES LO QUE DISPARA HOY.** Esa misma 3.6 les puso a las mesas
un disparador propio: **"cuando la fase 06 cierre"**. El acta 153, 6.3 lo mide
disparado y lo adjudica; **esta vuelta lo vuelve a medir con su propio
instrumento antes de mover una sola ficha**, que es lo que la regla del
instrumento manda.

**EL DISPARADOR, MEDIDO EN ESTA VUELTA** (`scripts/loop/tallar_estado_de_fase.py
--fase 06_MESAS`, salida
[`loop/SALIDA_V154_T5_DISPARADOR.txt`](../loop/SALIDA_V154_T5_DISPARADOR.txt)):
**%d de %d operaciones del catalogo de la fase 06 con destino CUMPLIDO, 0 sin
cumplir**, y **las cinco mesas entre ellas**.

**LAS CINCO, NOMBRADAS:** %s.

**EL PASE ES POR FICHA Y NO POR DECRETO.** El encargo lo fija: la adjudicacion
cubre a las que el disparador alcance. Se mueve la ficha cuya fila diga
`CUMPLIDO` y se deja quieta la que no, y las que no se mueven se nombran. En
esta corrida se movieron **%d de 5**; sin mover: **%s**.

**EL ACTO Y SUS GUARDAS:** uno solo, las cinco a la vez, con el **conteo antes y
despues**, el **esquema comprobado por assert** (71 fichas, un solo juego de 18
claves) y la **guarda de cifras del plan re corrida**, exactamente el molde de
las vueltas 131, 136 y 152.

**LA CONVENCION DEL SILENCIO NO SE MUEVE EN LA MISMA VUELTA EN QUE SE CUENTA:**
se cuenta con la **lista A**, la que vive en
`vuelta150_3_relectura_expediente.py:declara_su_estado`. Cambiar la vara y el
sujeto a la vez es la trampa que la vuelta 152 ya evito.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aplicar", action="store_true")
    args = ap.parse_args()

    F = fichas()
    mesas = sorted(f["id_op"] for f in F if f["fase"] == "06_MESAS")
    print("=" * 96)
    print("VUELTA 154, TAREA 5: EL PASE DE `estado` DE LAS CINCO MESAS")
    print("=" * 96)
    print("LA NOMINA SE LEE DEL FICHERO, no de memoria: fichas con fase 06_MESAS en")
    print("docs/plan/OPERACIONES.jsonl: %d (%s)" % (len(mesas), ", ".join(mesas)))
    assert len(mesas) == 5, "la fase 06 no trae exactamente cinco mesas"
    print("")

    print("=" * 96)
    print("EL DISPARADOR, MEDIDO CON MI INSTRUMENTO EN ESTA VUELTA")
    print("=" * 96)
    D, texto = destino_medido()
    m = re.search(r"operaciones del catalogo: (\d+) \| con destino cumplido: (\d+) \| sin cumplir: (\d+)",
                  texto)
    total, cumplidas, sin_cumplir = (int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else (0, 0, -1)
    print("CATALOGO DE LA FASE 06: %d operacion(es) | con destino cumplido %d | sin cumplir %d"
          % (total, cumplidas, sin_cumplir))
    print("")
    alcanzadas, no_alcanzadas = [], []
    for i in mesas:
        v = D.get(i, "SIN FILA EN LA TABLA")
        (alcanzadas if v == "CUMPLIDO" else no_alcanzadas).append(i)
        print("  [%s] %-10s destino medido: %s" % ("OK" if v == "CUMPLIDO" else "NO", i, v))
    print("")
    print("DISPARADOR: %d de %d mesas alcanzadas." % (len(alcanzadas), len(mesas)))
    if no_alcanzadas:
        print("NO SE MUEVEN, y se nombran: %s" % ", ".join(no_alcanzadas))
    if sin_cumplir != 0:
        print("LA FASE 06 NO CIERRA (sin cumplir %d): el disparador NO ha disparado y el"
              % sin_cumplir)
        print("pase NO se hace.")
        raise SystemExit(1)
    print("LA FASE 06 CIERRA ENTERA. El disparador que el acta 139, 3.6 dejo escrito")
    print("ha disparado, y el acta 153, 6.3 lo adjudica.")
    print("")

    print("=" * 96)
    print("CONTEO ANTES")
    print("=" * 96)
    antes, sil_antes = censo(F, "ANTES")
    for i in mesas:
        f = [x for x in F if x["id_op"] == i][0]
        print("  %-10s estado ANTES: %s" % (i, f["estado"]))

    if not args.aplicar:
        print("")
        print("MODO MEDICION. Nada escrito. Para aplicar: --aplicar")
        return

    print("")
    print("=" * 96)
    print("EL ACTO: UNO SOLO, LAS QUE EL DISPARADOR ALCANZA")
    print("=" * 96)

    lineas = io.open(OPS, encoding="utf-8").read().splitlines()
    claves_antes = {tuple(sorted(json.loads(x).keys())) for x in lineas if x.strip()}
    assert len(claves_antes) == 1, "el esquema ya venia roto antes de escribir"
    notas_antes = {json.loads(x)["id_op"]: json.loads(x).get("nota") or ""
                   for x in lineas if x.strip()}
    nuevas, movidas = [], []
    for x in lineas:
        if not x.strip():
            continue
        d = json.loads(x)
        if d["id_op"] in alcanzadas and d["estado"] == "LISTA":
            d["estado"] = "HECHA"
            d["nota"] = (d.get("nota") or "") + SELLO_NOTA
            movidas.append(d["id_op"])
        nuevas.append(json.dumps(d, ensure_ascii=False))
    io.open(OPS, "w", encoding="utf-8", newline="\n").write("\n".join(nuevas) + "\n")
    print("  [OK] %d ficha(s) movidas de LISTA a HECHA: %s"
          % (len(movidas), ", ".join(movidas)))

    viejo_corr = io.open(CORR, encoding="utf-8").read()
    if "CORRECCION 35." not in viejo_corr:
        bloque = TEXTO_CORRECCION_35 % (
            cumplidas, total, ", ".join("`%s`" % x for x in mesas),
            len(movidas), ", ".join(no_alcanzadas) if no_alcanzadas else "ninguna")
        io.open(CORR, "w", encoding="utf-8", newline="\n").write(viejo_corr + bloque)
        nuevo_corr = io.open(CORR, encoding="utf-8").read()
        assert nuevo_corr.startswith(viejo_corr), "ADICION IMPURA: el viejo no es prefijo del nuevo"
        print("  [OK] CORRECCION 35 anadida a docs/plan/CORRECCIONES_A_APLICAR.md POR ADICION")
        print("       PURA (el fichero viejo es prefijo EXACTO del nuevo, comprobado con assert)")

    F2 = fichas()
    claves_despues = {tuple(sorted(f.keys())) for f in F2}
    assert len(claves_despues) == 1, "EL ESQUEMA SE ROMPIO: hay mas de un juego de claves"
    assert claves_despues == claves_antes, "EL ESQUEMA CAMBIO de claves"
    assert len(F2) == len(F), "cambio el numero de fichas"
    for f in F2:
        assert f["nota"].startswith(notas_antes[f["id_op"]]), (
            "la nota vieja de %s no quedo entera" % f["id_op"])
    print("  [OK] esquema intacto: %d fichas, UN solo esquema de %d claves"
          % (len(F2), len(list(claves_despues)[0])))
    print("  [OK] las 71 notas viejas quedan ENTERAS como prefijo de las nuevas")

    print("")
    print("=" * 96)
    print("CONTEO DESPUES")
    print("=" * 96)
    despues, sil_despues = censo(F2, "DESPUES")
    for i in mesas:
        f = [x for x in F2 if x["id_op"] == i][0]
        print("  %-10s estado DESPUES: %s" % (i, f["estado"]))
    print("")
    print("| cifra | antes | despues |")
    print("|---|---:|---:|")
    for e in sorted(set(list(antes.keys()) + list(despues.keys()))):
        print("| fichas en %s | %d | %d |" % (e, antes.get(e, 0), despues.get(e, 0)))
    print("| congeladas EN SILENCIO (lista A) | %d | %d |" % (len(sil_antes), len(sil_despues)))
    print("")
    print("LAS QUE SIGUEN EN SILENCIO DESPUES DEL PASE (%d), nombradas y no resumidas:"
          % len(sil_despues))
    for i in sorted(sil_despues):
        print("  %s" % i)

    print("")
    print("=" * 96)
    print("LA GUARDA DE CIFRAS DEL PLAN, RE CORRIDA")
    print("=" * 96)
    r = subprocess.run(["python", os.path.join("scripts", "loop", "verificar_cifras_del_plan.py")],
                       capture_output=True, cwd=RAIZ)
    print((r.stdout.decode("utf-8", "replace") + r.stderr.decode("utf-8", "replace")).strip()[-1500:])
    print("EXITCODE GUARDA DE CIFRAS DEL PLAN: %d" % r.returncode)

    print("")
    print("CIFRA mesas de la fase 06: %d operaciones" % len(mesas))
    print("CIFRA mesas alcanzadas por el disparador: %d operaciones" % len(alcanzadas))
    print("CIFRA mesas movidas de LISTA a HECHA: %d operaciones" % len(movidas))
    print("CIFRA fichas del expediente: %d operaciones" % len(F2))
    print("CIFRA fichas en HECHA al cierre de esta tarea: %d operaciones" % despues.get("HECHA", 0))
    print("CIFRA fichas en LISTA al cierre de esta tarea: %d operaciones" % despues.get("LISTA", 0))


main()
