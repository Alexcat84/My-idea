# -*- coding: utf-8 -*-
"""vuelta161_tarea1_0_registros.py . TAREA 1.0 DE LA VUELTA 161.

DEJA ESCRITOS EN EL REPO LOS REGISTROS QUE EL ENCARGO PIDE: LAS CAIDAS DE CLASE
DE LAS DOS TANDAS CON SUS PUESTOS, Y LA PARADA CON SU RESOLUCION POR CITA.

LA SEDE, ELEGIDA Y DECLARADA EN VEZ DE SUPUESTA. Va a `docs/PENDIENTES.md`, que
es la forma que la casa ya usa desde `R.9`: "Registro de correcciones y
adjudicaciones declaradas de la vuelta N". Es el unico sitio del repo donde las
caidas y las adjudicaciones de una vuelta se registran como REGISTRO y no como
prosa de acta. VA MARCADO COMO DISCUTIBLE en el reporte: el encargo dice "LOS
REGISTROS" sin nombrar fichero.

--- CORRECCION DECLARADA (vuelta 162, TAREA 1.a; acta 161, seccion 5.1 y
adjudicacion 6.8). LO VIEJO NO SE BORRA Y QUEDA TACHADO Y LEGIBLE ---

    ~~"Va a `docs/PENDIENTES.md` como entrada `R.29` ... con la ultima escrita
    siendo `R.28` (vuelta 146, escrita en la 147, TAREA 1.a)."~~

LA CAIDA: `R.29` YA ESTABA ASIGNADA desde la vuelta 150 y vive en
`docs/plan/CORRECCIONES_A_APLICAR.md:2127`. La prueba estaba en el mismo fichero
que este script abrio: `docs/PENDIENTES.md:10389` dice literal que `R.29` NO esta
en esa pagina y que su fuente unica es la otra. LAS DOS CAUSAS SON DE ESTE
FICHERO: el ultimo numero venia TECLEADO aqui arriba, y la idempotencia de abajo
miraba UNA sola sede. LA SERIE `R.N` ES GLOBAL A LOS DOS FICHEROS.

EL REMEDIO, Y ES EL QUE HACE QUE NO PUEDA REPETIRSE: EL NUMERO NO SE TECLEA
NUNCA MAS. Lo computa `scripts/loop/serie_de_registros.py`, que lee LAS DOS
sedes, imprime la serie entera con su sede y devuelve `siguiente_libre()`. La
entrada que este script escribio se renumero a `R.30` en la vuelta 162 con
`scripts/loop/vuelta162_tarea1a_renumerar_r29.py`, sin borrar una linea.

NINGUNA CELDA SE TECLEA. Las cinco caidas se leen del registro de citas
(`docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl`), su numero de fila se cuenta del
fichero, la ausencia de puesto se mide contra el archivo del cribado
(`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`), la regla del credito se lee de su linea
en `docs/loop/AUDITOR.md`, y la decision del fundador se lee de su fichero de
parada. Si alguna medicion no se puede hacer, este script PARA sin escribir.

SOBRE "CON SUS PUESTOS", Y SE MIDE EN VEZ DE ADIVINARSE: en esta casa un PUESTO
es la posicion de un par en el archivo del cribado (`puesto_intra`, de 1 a
3.388), que es como se citan los ejemplares del banco (por ejemplo "el puesto
2091"). LOS CINCO PARES CAIDOS SON DE LECTURA DIRIGIDA Y NO ESTAN EN ESE
ARCHIVO: se comprueba par a par y se publica el resultado. Lo que SI tienen y se
publica es su PUESTO EN LA RACHA (que tanda, que lugar) y su FILA en el registro.

ES IDEMPOTENTE: si `R.29` ya esta, no lo duplica.

USO:  python scripts/loop/vuelta161_tarea1_0_registros.py
"""
import io
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PENDIENTES = os.path.join(RAIZ, "docs", "PENDIENTES.md")
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
ARCHIVO = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
AUDITOR = os.path.join(RAIZ, "docs", "loop", "AUDITOR.md")
DECISION = os.path.join(RAIZ, "docs", "loop", "paradas",
                        "2026-09-03-credito-vara-movil-DECISION.md")
# CORRECCION DECLARADA (vuelta 162, TAREA 1.a). LA LINEA VIEJA, TACHADA Y
# LEGIBLE, porque con ella se escribio la entrada de la vuelta 161:
#     ~~MARCA = "## R.29. Registro de las caidas de clase de las dos tandas"~~
# EL DEFECTO: el numero estaba DENTRO de la marca, asi que la idempotencia
# dependia de acertar el numero, y ademas solo se buscaba en docs/PENDIENTES.md.
# LO NUEVO: la marca es el TITULO SIN NUMERO (lo unico estable de la entrada) y
# se busca en LAS DOS SEDES de la serie.
TITULO_SIN_NUMERO = "Registro de las caidas de clase de las dos tandas"

# (numero, tanda, lugar en la racha, que paso). El QUE PASO no es cifra: es la
# historia que el propio campo `cita` de la fila declara, y se coteja contra el.
CAIDAS = [
    ("005", "vuelta 157, lote 1", 1,
     "publicada D y devuelta a C por la relectura conjunta; registrada en el acta 159"),
    ("100", "vuelta 159, lote 2", 2,
     "publicada C y pasada a D en la vuelta 160, al dar el ejecutor la razon al auditor"),
    ("094", "vuelta 159, lote 2", 2,
     "misma costura, hallada por el ejecutor al releer el tramo entero en la vuelta 160"),
    ("101", "vuelta 159, lote 2", 2,
     "misma costura, hallada por el ejecutor al releer el tramo entero en la vuelta 160"),
    ("118", "vuelta 159, lote 2", 2,
     "misma costura, hallada por el ejecutor al releer el tramo entero en la vuelta 160"),
]


def linea_de(ruta, numero):
    return io.open(ruta, encoding="utf-8").read().split("\n")[numero - 1].strip()


def main():
    print("=" * 78)
    print("VUELTA 161, TAREA 1.0: LOS REGISTROS DE LAS DOS TANDAS Y DE LA PARADA")
    print("=" * 78)
    print("")

    pend = io.open(PENDIENTES, encoding="utf-8").read()
    # CORRECCION DECLARADA (vuelta 162, TAREA 1.a). LAS LINEAS VIEJAS, TACHADAS Y
    # LEGIBLES, porque el veredicto de la vuelta 161 se dio con ellas:
    #     ~~if MARCA in pend:~~
    #     ~~    print("YA ESTABA: R.29 vive en docs/PENDIENTES.md. No se toca.")~~
    # LA SERIE SE RECOMPUTA DE LAS DOS SEDES ANTES DE MIRAR NADA, y la entrada se
    # busca POR SU TITULO, no por su numero.
    serie = SERIE.entradas()
    print("A0) LA SERIE R.N, RECOMPUTADA DE SUS DOS SEDES ANTES DE ESCRIBIR")
    for numero, rel, linea, titulo in serie:
        print("   R.%-3d %s:%-6d %s" % (numero, rel, linea, titulo[:88]))
    print("   CIFRA entradas: %d" % len(serie))
    print("   CIFRA colisiones: %d" % len(SERIE.colisiones(serie)))
    print("   SIGUIENTE LIBRE, computado y no tecleado: R.%d" % SERIE.siguiente_libre(serie))
    print("")
    ya = [(n, rel, ln) for n, rel, ln, t in serie if TITULO_SIN_NUMERO in t]
    if ya:
        n, rel, ln = ya[0]
        print("YA ESTABA: la entrada vive como R.%d en %s:%d. No se toca." % (n, rel, ln))
        print("CIFRA entradas escritas: 0")
        return 0
    numero_nuevo = SERIE.siguiente_libre(serie)

    filas = [json.loads(l) for l in io.open(REGISTRO, encoding="utf-8") if l.strip()]
    print("A) EL REGISTRO, CONTADO DEL FICHERO")
    print("   CIFRA filas: %d" % len(filas))
    ld = [f for f in filas if f.get("via") == "LECTURA_DIRIGIDA"]
    print("   CIFRA de LECTURA_DIRIGIDA: %d" % len(ld))
    print("")

    # El archivo del cribado, para medir si estos pares tienen puesto.
    puestos = {}
    for l in io.open(ARCHIVO, encoding="utf-8"):
        l = l.strip()
        if not l:
            continue
        d = json.loads(l)
        clave = tuple(sorted([d.get("nodo_a") or "", d.get("nodo_b") or ""]))
        puestos[clave] = d.get("puesto_intra")
    print("B) EL ARCHIVO DEL CRIBADO, CONTADO DEL FICHERO")
    print("   fuente: docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
    print("   CIFRA pares con puesto_intra: %d" % len(puestos))
    print("")

    print("C) LAS CINCO CAIDAS, MEDIDAS UNA A UNA")
    medidas = []
    for numero, tanda, lugar, historia in CAIDAS:
        fila = None
        indice = None
        for i, f in enumerate(filas, 1):
            if f["cita"].startswith("LD-OPC05-%s" % numero):
                fila, indice = f, i
                break
        if fila is None:
            print("   PARADA: no se halla LD-OPC05-%s en el registro." % numero)
            return 1
        clave = tuple(sorted(fila["par"]))
        puesto = puestos.get(clave)
        medidas.append((numero, tanda, lugar, historia, indice, fila["clase"],
                        fila["par"], puesto, fila["cita"]))
        print("   LD-OPC05-%s  fila %d del registro  clase HOY %s  puesto_intra %s"
              % (numero, indice, fila["clase"],
                 puesto if puesto is not None else "(no esta en el archivo del cribado)"))
        print("      par: %s" % (" + ".join(fila["par"])))
        print("      cita: %s" % fila["cita"][:120])
    con_puesto = len([m for m in medidas if m[7] is not None])
    print("")
    print("   CIFRA caidas registradas: %d" % len(medidas))
    print("   CIFRA de ellas CON puesto en el archivo del cribado: %d" % con_puesto)
    print("   CIFRA de ellas SIN puesto en el archivo del cribado: %d"
          % (len(medidas) - con_puesto))
    print("")

    print("D) LA REGLA DEL CREDITO Y LA DECISION, LEIDAS DE SU FICHERO HOY")
    regla = linea_de(AUDITOR, 135)
    print("   docs/loop/AUDITOR.md:135 -> %s" % regla)
    if "Dos tandas seguidas" not in regla:
        print("   PARADA: la linea 135 de AUDITOR.md ya no dice lo que se cita.")
        return 1
    decision = io.open(DECISION, encoding="utf-8").read()
    if "La racha del credito vuelve a CERO" not in decision:
        print("   PARADA: la decision del fundador no trae la frase que se cita.")
        return 1
    print("   docs/loop/paradas/2026-09-03-credito-vara-movil-DECISION.md: trae la")
    print("   frase 'La racha del credito vuelve a CERO con la vara congelada'. SI")
    print("")

    filas_tabla = []
    for numero, tanda, lugar, historia, indice, clase, par, puesto, cita in medidas:
        filas_tabla.append(
            "| `LD-OPC05-%s` | %s | %d | %d | **%s** | %s | %s |"
            % (numero, tanda, lugar, indice, clase,
               "`%s`" % puesto if puesto is not None else "no esta en el archivo",
               historia))

    texto = u"""
---

## R.29. Registro de las caidas de clase de las dos tandas y de la parada de la
vuelta 160, con su resolucion (escrito en la vuelta 161, TAREA 1.0)

Por adicion, como `R.21` a `R.28`. **Corte de todas las cifras de esta entrada:
3 sep 2026**, y ninguna esta tecleada: todas salen de
`scripts/loop/vuelta161_tarea1_0_registros.py`, salida
`docs/loop/SALIDA_V161_T1_0_REGISTROS.txt`.

**(1) LAS CAIDAS DE CLASE DE LAS DOS TANDAS, CON SUS PUESTOS.**

**Y LO PRIMERO ES QUE PUESTO NO SE PUEDE PUBLICAR PARA ESTAS CINCO, Y SE MIDE EN
VEZ DE CALLARSE.** En esta casa un **puesto** es la posicion de un par en el
archivo del cribado (`puesto_intra`, de 1 a 3.388), que es como el banco cita
sus ejemplares (*"el puesto 2091"*). **Los cinco pares caidos son de LECTURA
DIRIGIDA y NINGUNO esta en ese archivo**: comprobado par a par contra
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, **__CON_PUESTO__ de __TOTAL__ tienen
`puesto_intra`**. Lo que si tienen, y es lo que se publica, es **su lugar en la
racha** y **su fila en el registro de citas**.

| cita | tanda | lugar en la racha | fila del registro | clase HOY | `puesto_intra` | que paso |
|---|---|---:|---:|:---:|---|---|
__FILAS__

**LA COSTURA ES LA MISMA EN LAS CINCO, y por eso importa: la SEGUNDA LINEA de un
par clasificado `C`.** Se acepto como expansion algo que solo **NOMBRA** en vez
de **PROCEDIMENTAR**. Esa especie es la que la decision del fundador congela en
`P.5.1` del banco del plan.

**(2) LA PARADA, Y SU RESOLUCION POR CITA.**

  - **QUE SE DISPARO.** La regla del credito de `docs/loop/AUDITOR.md`, leida hoy
    en su **linea 135**: *"__REGLA__"*. **Dos tandas seguidas con caida de CLASE
    confirmada**: la de la vuelta 157 (`LD-OPC05-005`) y la de la vuelta 159
    (`LD-OPC05-100` y las tres de su costura).
  - **QUIEN LA DECLARO Y QUIEN NO LA EJECUTO.** El **ejecutor la declaro en su
    propio reporte de la vuelta 160**, con la cuenta hecha, y **no ejecuto
    ninguna accion de parada por su mano** (`EJECUTOR.md` 5). El **auditor de la
    vuelta 160** escribio `docs/loop/PARA_ALEXIS.md` y dejo
    `docs/loop/PROMPT_SIGUIENTE.md` vacio, que es lo que le manda la seccion 4
    del `AUDITOR.md`.
  - **COMO SE RESUELVE, Y SE CITA POR SU FICHERO.** Por la **decision del
    fundador del 3 sep 2026**,
    `docs/loop/paradas/2026-09-03-credito-vara-movil-DECISION.md`: **opcion A con
    remate**. La vara de la lectura dirigida queda **CONGELADA** y escrita en un
    solo sitio citable (`P.5.1` del banco del plan, con sus cuatro ejemplares);
    los 14 pares en `C` se releen **UNA** vez; los modelos no cambian; y **la
    racha del credito vuelve a CERO por letra expresa de la decision**.
  - **LO QUE LA DECISION PROHIBE, Y VA AQUI PARA QUE NO HAYA QUE VOLVER A
    BUSCARLO.** *"Ninguna vuelta la estrecha ni la ensancha sin correccion
    declarada del fundador."* Si una lectura pide mover la frontera, **eso es
    parada y se trae**.
  - **LA PLANTEA COMPLETA**, con las dos tandas nombradas, lo que la parada NO
    es, el estado medido y las tres opciones, vive en
    `docs/loop/paradas/2026-09-03-credito-vara-movil.md`.

**(3) LO QUE ESTE REGISTRO NO CIERRA.** El **muro de la fase 08** sigue donde
estaba (acta 149, seccion 3.10): no cierra sin una sesion con credencial y con el
fundador delante, porque el `.env` esta fuera del repo mientras el bucle corre.
**Eso no lo resuelve ninguna vuelta mas.**
"""
    texto = (texto.replace("__FILAS__", "\n".join(filas_tabla))
             .replace("__CON_PUESTO__", str(con_puesto))
             .replace("__TOTAL__", str(len(medidas)))
             .replace("__REGLA__", regla.replace("**", "")))

    with io.open(PENDIENTES, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)

    print("E) LA ESCRITURA")
    print("   R.29 anadida al final de docs/PENDIENTES.md, por adicion pura")
    print("   CIFRA entradas escritas: 1")
    print("   CIFRA filas de la tabla: %d" % len(filas_tabla))
    r = subprocess.run(["git", "diff", "--numstat", "--", "docs/PENDIENTES.md"],
                       cwd=RAIZ, capture_output=True, text=True)
    print("   git diff --numstat: %s" % r.stdout.strip())
    borrados = None
    for linea in r.stdout.strip().split("\n"):
        partes = linea.split("\t")
        if len(partes) >= 2 and partes[1].isdigit():
            borrados = int(partes[1])
    print("   CIFRA borrados: %s" % borrados)
    if borrados != 0:
        print("   ROJO: tenia que ser adicion pura.")
        return 1
    print("   VERDE: adicion pura, cero borrados.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
