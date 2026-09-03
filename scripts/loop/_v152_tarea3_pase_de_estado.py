# -*- coding: utf-8 -*-
"""VUELTA 152, TAREA 3: EL PASE DE `estado` DE LAS ONCE, COMO UN SOLO ACTO,
CON EL CONTEO ANTES Y DESPUES.

RESERVADO DESDE EL ACTA 139, 3.6, y se cita literal: "Cuando las cinco
remitidas queden con destino, el pase de estado de las once (las seis fusiones
y las cinco remitidas) va en UNA sola adjudicacion, con el conteo antes y
despues y la guarda de cifras del plan re-corrida, como en las vueltas 131 y
136."

LAS ONCE, NOMBRADAS Y NO CONTADAS DE MEMORIA:
  seis fusiones   OP-M-01-FUSION, OP-M-02-ACCLIMATE, OP-M-03-III,
                  OP-M-05-APERTURA, OP-M-05-EDIFICIO, OP-M-05-INDICE
  cinco remitidas OP-E-04, OP-E-05, OP-M-01-ESLABONES, OP-M-01-SEXTO,
                  OP-M-03-ENLACES
Las seis salen de la P.5 del acta 139 ("las cinco" mas OP-M-02-ACCLIMATE,
seccion 1) y las cinco de la remision de la vuelta 118 que el acta 139 fija en
su 3.7. LAS ONCE SE VUELVEN A COMPROBAR AQUI contra la tabla de
tallar_estado_de_fase.py: si alguna NO sale CUMPLIDA, el pase no se hace.

EL AVISO DEL ENCARGO, ATENDIDO ANTES DE CONTAR. El "30 congeladas en silencio"
NO es un cardinal duro: es una CONVENCION que se mueve segun la lista de marcas
con la que se pregunta si una ficha habla de su propio estado. Aqui se miden
CUATRO listas y se publica el abanico, y SOLO DESPUES se declara cual se usa.
LA QUE SE USA ES LA DE LA LISTA A, que es la que ya vive en
vuelta150_3_relectura_expediente.py:declara_su_estado y por tanto la que produjo
la cifra publicada: cambiarla en la misma vuelta en que se cuenta seria mover la
vara y el sujeto a la vez.

USO:
  python scripts/loop/_v152_tarea3_pase_de_estado.py            (mide y NO escribe)
  python scripts/loop/_v152_tarea3_pase_de_estado.py --aplicar  (mide, escribe y vuelve a medir)
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

SEIS_FUSIONES = ["OP-M-01-FUSION", "OP-M-02-ACCLIMATE", "OP-M-03-III",
                 "OP-M-05-APERTURA", "OP-M-05-EDIFICIO", "OP-M-05-INDICE"]
CINCO_REMITIDAS = ["OP-E-04", "OP-E-05", "OP-M-01-ESLABONES", "OP-M-01-SEXTO",
                   "OP-M-03-ENLACES"]
LAS_ONCE = SEIS_FUSIONES + CINCO_REMITIDAS

LISTAS_DE_MARCAS = {
    "A (la del instrumento vigente, vuelta150_3:declara_su_estado)":
        ("ESTADO", "DIFERIDA", "CONGELAD", "SIGUE EN LISTA", "NO SE MUEVE"),
    "B (solo la palabra ESTADO)":
        ("ESTADO",),
    "C (solo las dos que nombran el congelamiento)":
        ("CONGELAD", "DIFERID"),
    "D (ancha: se suma todo lo que la casa ha usado para decir que una ficha no corre)":
        ("ESTADO", "DIFERID", "CONGELAD", "SIGUE EN LISTA", "NO SE MUEVE",
         "NO SE EJECUTA", "NO SE REHACE", "CONSUMIDA", "REMITID", "NO SE TOCA"),
}


def fichas():
    return [json.loads(x) for x in io.open(OPS, encoding="utf-8").read().splitlines() if x.strip()]


def habla_de_su_estado(f, marcas):
    t = " ".join(str(f.get(k) or "") for k in ("nota", "adjudicacion")).upper()
    return any(m in t for m in marcas)


def destino_medido():
    """Veredicto de tallar_estado_de_fase.py, la MISMA vara P1 del expediente.
    No se reimplementa aqui: se invoca y se lee su tabla."""
    out = {}
    for fase in ("03_FUSIONES", "04_ENLACES", "06_MESAS"):
        r = subprocess.run(["python", os.path.join("scripts", "loop", "tallar_estado_de_fase.py"),
                            "--fase", fase], capture_output=True, cwd=RAIZ)
        for linea in r.stdout.decode("utf-8", "replace").splitlines():
            if not linea.strip().startswith("|"):
                continue
            celdas = [c.strip().strip("`*") for c in linea.strip().strip("|").split("|")]
            if not celdas or not re.match(r"^OP-[A-Z]+-", celdas[0]):
                continue
            v = celdas[-1]
            if celdas[0] not in out or v == "CUMPLIDO":
                out[celdas[0]] = v
    return out


def censo(F, etiqueta):
    marcas = LISTAS_DE_MARCAS["A (la del instrumento vigente, vuelta150_3:declara_su_estado)"]
    por_estado = {}
    for f in F:
        por_estado[f["estado"]] = por_estado.get(f["estado"], 0) + 1
    silencio = [f["id_op"] for f in F if f["estado"] == "LISTA" and not habla_de_su_estado(f, marcas)]
    print("CENSO %s: %d fichas | %s | LISTA que NO hablan de su estado (lista A): %d"
          % (etiqueta, len(F), " ".join("%s %d" % (k, v) for k, v in sorted(por_estado.items())),
             len(silencio)))
    return por_estado, silencio


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aplicar", action="store_true")
    args = ap.parse_args()

    F = fichas()
    print("=" * 96)
    print("EL ABANICO DE LA CONVENCION, MEDIDO ANTES DE ELEGIR (aviso del encargo)")
    print("=" * 96)
    print("Pregunta: cuantas fichas en LISTA NO hablan de su propio estado, o sea")
    print("cuantas estan CONGELADAS EN SILENCIO. La respuesta depende de la lista de marcas:")
    print("")
    abanico = []
    for nombre, marcas in LISTAS_DE_MARCAS.items():
        n = sum(1 for f in F if f["estado"] == "LISTA" and not habla_de_su_estado(f, marcas))
        abanico.append(n)
        print("  lista %-72s -> %d" % (nombre, n))
    print("")
    print("ABANICO MEDIDO HOY: de %d a %d sobre las mismas 71 fichas y el mismo arbol."
          % (min(abanico), max(abanico)))
    print("POR ESO SE DECLARA LA VARA ANTES DE CONTAR: SE USA LA LISTA A, la que ya vive")
    print("en vuelta150_3_relectura_expediente.py y la que produjo la cifra publicada.")
    print("")

    print("=" * 96)
    print("LA PUERTA DEL ACTA 139, 3.6: LAS CINCO REMITIDAS TIENEN QUE TENER DESTINO")
    print("=" * 96)
    D = destino_medido()
    faltan = []
    for i in LAS_ONCE:
        v = D.get(i, "SIN FILA EN LA TABLA")
        marca = "OK" if v == "CUMPLIDO" else "NO"
        if v != "CUMPLIDO":
            faltan.append(i)
        grupo = "fusion  " if i in SEIS_FUSIONES else "remitida"
        print("  [%s] %-8s %-20s destino medido: %s" % (marca, grupo, i, v))
    print("")
    print("PUERTA: %d de %d con destino CUMPLIDO." % (len(LAS_ONCE) - len(faltan), len(LAS_ONCE)))
    if faltan:
        print("LA PUERTA NO SE ABRE. El pase NO se hace. Sin destino: %s" % ", ".join(faltan))
        raise SystemExit(1)
    print("LA PUERTA SE ABRE: el disparador que el acta 139 dejo escrito ha disparado.")
    print("")

    print("=" * 96)
    print("CONTEO ANTES")
    print("=" * 96)
    antes, sil_antes = censo(F, "ANTES")
    for i in LAS_ONCE:
        f = [x for x in F if x["id_op"] == i][0]
        print("  %-20s estado ANTES: %s" % (i, f["estado"]))
    ya = [i for i in LAS_ONCE if [x for x in F if x["id_op"] == i][0]["estado"] == "HECHA"]
    print("  de las once, ya estaban en HECHA: %d" % len(ya))

    if not args.aplicar:
        print("")
        print("MODO MEDICION. Nada escrito. Para aplicar: --aplicar")
        return

    # ------------------------------------------------------------- ESCRITURA
    print("")
    print("=" * 96)
    print("EL ACTO: UNO SOLO, LAS ONCE A LA VEZ")
    print("=" * 96)

    viejo_corr = io.open(CORR, encoding="utf-8").read()
    bloque = TEXTO_CORRECCION_31 % (
        ", ".join("`%s`" % x for x in SEIS_FUSIONES),
        ", ".join("`%s`" % x for x in CINCO_REMITIDAS),
        min(abanico), max(abanico), len(sil_antes))
    io.open(CORR, "w", encoding="utf-8", newline="\n").write(viejo_corr + bloque)
    nuevo_corr = io.open(CORR, encoding="utf-8").read()
    assert nuevo_corr.startswith(viejo_corr), "ADICION IMPURA: el fichero viejo no es prefijo del nuevo"
    print("  [OK] CORRECCION 31 anadida a docs/plan/CORRECCIONES_A_APLICAR.md POR ADICION PURA")
    print("       (el fichero viejo es prefijo EXACTO del nuevo, comprobado con un assert)")

    lineas = io.open(OPS, encoding="utf-8").read().splitlines()
    claves_antes = {tuple(sorted(json.loads(x).keys())) for x in lineas if x.strip()}
    assert len(claves_antes) == 1, "el esquema ya venia roto antes de escribir"
    nuevas, movidas = [], []
    for x in lineas:
        if not x.strip():
            continue
        d = json.loads(x)
        if d["id_op"] in LAS_ONCE and d["estado"] == "LISTA":
            d["estado"] = "HECHA"
            d["nota"] = (d.get("nota") or "") + SELLO_NOTA
            movidas.append(d["id_op"])
        nuevas.append(json.dumps(d, ensure_ascii=False))
    io.open(OPS, "w", encoding="utf-8", newline="\n").write("\n".join(nuevas) + "\n")
    print("  [OK] %d ficha(s) movidas de LISTA a HECHA: %s" % (len(movidas), ", ".join(movidas)))

    F2 = fichas()
    claves_despues = {tuple(sorted(f.keys())) for f in F2}
    assert len(claves_despues) == 1, "EL ESQUEMA SE ROMPIO: hay mas de un juego de claves"
    assert claves_despues == claves_antes, "EL ESQUEMA CAMBIO de claves"
    assert len(F2) == len(F), "cambio el numero de fichas"
    print("  [OK] esquema intacto: %d fichas, UN solo esquema de %d claves"
          % (len(F2), len(list(claves_despues)[0])))

    print("")
    print("=" * 96)
    print("CONTEO DESPUES")
    print("=" * 96)
    despues, sil_despues = censo(F2, "DESPUES")
    for i in LAS_ONCE:
        f = [x for x in F2 if x["id_op"] == i][0]
        print("  %-20s estado DESPUES: %s" % (i, f["estado"]))
    print("")
    print("| cifra | antes | despues |")
    print("|---|---|---|")
    for e in sorted(set(list(antes.keys()) + list(despues.keys()))):
        print("| fichas en %s | %d | %d |" % (e, antes.get(e, 0), despues.get(e, 0)))
    print("| congeladas EN SILENCIO (lista A declarada) | %d | %d |" % (len(sil_antes), len(sil_despues)))
    print("")
    print("LAS QUE SIGUEN EN SILENCIO DESPUES DEL PASE (%d), nombradas y no resumidas:"
          % len(sil_despues))
    for i in sorted(sil_despues):
        print("  %s" % i)

    print("")
    print("=" * 96)
    print("LA GUARDA DE CIFRAS DEL PLAN, RE-CORRIDA (lo pide el acta 139, 3.6)")
    print("=" * 96)
    r = subprocess.run(["python", os.path.join("scripts", "loop", "verificar_cifras_del_plan.py")],
                       capture_output=True, cwd=RAIZ)
    print((r.stdout.decode("utf-8", "replace") + r.stderr.decode("utf-8", "replace")).strip()[-1500:])
    print("EXITCODE: %d" % r.returncode)


SELLO_NOTA = (
    " CORRECCION DECLARADA (2026-09-02, vuelta 152, TAREA 3; nada del texto anterior se borra, "
    "esta linea se anade): ~~estado LISTA~~ pasa a estado HECHA, dentro del PASE DE LAS ONCE que "
    "el acta 139, 3.6, dejo reservado literalmente para 'cuando las cinco remitidas queden con "
    "destino'. El disparador se midio en esta vuelta y disparo: las once salen CUMPLIDO en la "
    "tabla de scripts/loop/tallar_estado_de_fase.py. El pase va en UN SOLO ACTO, con el conteo "
    "antes y despues y la guarda de cifras del plan re-corrida, tal como esa reserva lo exige. "
    "Ver docs/plan/CORRECCIONES_A_APLICAR.md, CORRECCION 31, y "
    "docs/loop/SALIDA_V152_T3_PASE_DE_ESTADO.txt.")

TEXTO_CORRECCION_31 = """

---

## CORRECCION 31. **EL PASE DE `estado` DE LAS ONCE, EN UN SOLO ACTO, CON EL DISPARADOR MEDIDO Y LA CONVENCION DECLARADA ANTES DE CONTAR**

**Fecha: 2026-09-02. Vuelta 152, TAREA 3. Reservada desde el acta 139, 3.6.**

**LA RESERVA, CITADA LITERAL Y NO PARAFRASEADA** (acta 139, adjudicacion 3.6):
*"Cuando las cinco remitidas queden con destino, el pase de estado de las once
(las seis fusiones y las cinco remitidas) va en UNA sola adjudicacion, con el
conteo antes y despues y la guarda de cifras del plan re-corrida, como en las
vueltas 131 y 136."*

**LAS ONCE, NOMBRADAS.**

  - **seis fusiones:** %s
  - **cinco remitidas:** %s

**EL DISPARADOR HA DISPARADO, Y SE MIDE EN VEZ DE AFIRMARSE.** Las once salen
**CUMPLIDO** en la tabla de `scripts/loop/tallar_estado_de_fase.py`, que es la
misma vara P1 con la que el expediente se relee. La salida entera, con las once
filas una a una, esta en `docs/loop/SALIDA_V152_T3_PASE_DE_ESTADO.txt`.

**LA CONVENCION SE DECLARA ANTES DE CONTAR, Y NO DESPUES.** El *"30 congeladas
en silencio"* **no es un cardinal duro**: es una convencion que depende de con
que lista de marcas se pregunta si una ficha habla de su propio `estado`. Medido
hoy con **cuatro listas distintas sobre las mismas 71 fichas y el mismo arbol**,
la respuesta va **de %d a %d**. Por eso esta correccion declara la vara ANTES:
se usa **la lista A**, la que ya vive en
`scripts/loop/vuelta150_3_relectura_expediente.py:declara_su_estado`
(`ESTADO`, `DIFERIDA`, `CONGELAD`, `SIGUE EN LISTA`, `NO SE MUEVE`), porque es la
que produjo la cifra publicada y cambiarla en la misma vuelta en que se cuenta
seria mover la vara y el sujeto a la vez. Con esa vara, ANTES del pase habia
**%d** fichas en `LISTA` que no hablan de su estado.

**LO QUE ESTA CORRECCION NO HACE.** No borra ni reescribe una sola linea de las
once fichas: el `estado` se mueve y el motivo se **anade** al campo `nota`. No
toca el esquema, y se comprueba con un `assert` despues de escribir: las **71
fichas siguen teniendo UN solo esquema de 18 claves**. Y **no mueve el `estado`
de las cinco mesas** (`OP-M-01` a `OP-M-05`), que hoy tambien miden CUMPLIDO:
la reserva del acta 139 nombra **once** y solo once, y ampliarla por mi cuenta
seria doctrina nueva disfrazada de cita. Queda dicho aqui, medido, para que el
auditor decida.
"""

main()
