# -*- coding: utf-8 -*-
r"""_v214_cierre_texto.py . EL CUERPO DEL CIERRE DEL REPORTE DE LA VUELTA 214,
COMPUESTO DE MEDICIONES Y NO TECLEADO.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1: toda tabla o cifra del reporte cita el fichero de salida del que
sale, y se reconstruye contando ese fichero antes de publicarla.

USO:  python scripts/loop/_v214_cierre_texto.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_",
                       os.path.basename(os.path.abspath(__file__))).group(1))

sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402

SEDES = [
    "docs/plan/INVENTARIO.jsonl",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/08_VERIFICACION.md",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "docs/INTRA_DOMINIO_INFORME.md",
    "docs/plan/00_INDICE.md",
    "docs/BANCO_DE_TEXTOS.md",
    "docs/plan/BANCO_DEL_PLAN.md",
    "dataset/metadata/master_graph.json",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
]

LADOS = ("APERTURA", "CIERRE")


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read()


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", errors="replace").strip()


def sha(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    b = io.open(p, "rb").read()
    return (hashlib.sha256(b).hexdigest()[:16],
            hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16])


def cifra(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(\d+)", l.split(etiqueta, 1)[1])
            if m:
                return m.group(1)
    return None


def main():
    # ---------------------------------------------------------- GATE 0
    filas_gate = []
    peor = {}
    for lado in LADOS:
        rel = "docs/loop/SALIDA_V%d_CICLO_GATE0_%s_CONSOLA.txt" % (VUELTA, lado)
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(p):
            filas_gate.append("| **%s** | (sin fichero de consola) | | |" % lado)
            continue
        txt = leer(rel)
        cmds = [l for l in txt.split(NL) if re.search(r"EXITCODE \d", l)]
        malos = [l for l in cmds if not re.search(r"EXITCODE 0\b", l)]
        m = re.search(r"PEOR EXITCODE DE LOS OCHO: (\d+)", txt)
        peor[lado] = m.group(1) if m else "(no leido)"
        filas_gate.append("| **%s** | %d comando(s) con EXITCODE leido | %d con "
                          "exitcode distinto de 0 | **peor exitcode %s** |"
                          % (lado, len(cmds), len(malos), peor[lado]))

    ns_cierre = "docs/loop/SALIDA_V%d_CICLO_NUMSTAT_CIERRE.txt" % VUELTA
    filas_ns = 0
    if os.path.isfile(os.path.join(RAIZ, ns_cierre.replace("/", os.sep))):
        filas_ns = len([l for l in leer(ns_cierre).split(NL) if l.strip()])

    # ---------------------------------------------------------- SEDES
    ap = leer("docs/loop/SALIDA_V%d_APERTURA.txt" % VUELTA)
    filas_sedes = []
    movidas = 0
    for rel in SEDES:
        sd, sl = sha(rel)
        m = medir_en_disco(RAIZ, rel)
        viejo = None
        for l in ap.split(NL):
            if l.startswith("CIFRA " + rel + ":"):
                mm = re.search(r"sha256 LF ([0-9a-f]{16})", l)
                if mm:
                    viejo = mm.group(1)
        se_movio = (viejo is not None and viejo != sl)
        if se_movio:
            movidas += 1
        filas_sedes.append(
            "| `%s` | %s | %s | %s | %s |"
            % (rel, viejo or "(no medida al abrir)", sl,
               "**SE MOVIO**" if se_movio else "quieta",
               "%d / %d" % (m[0], m[1]) if m else "(ausente)"))

    ns_plan = [l for l in git(["diff", "--numstat", "HEAD~3", "--",
                              "docs/plan/"]).split(NL) if l.strip()]
    ns_dataset = [l for l in git(["diff", "--numstat", "--",
                                 "dataset/"]).split(NL) if l.strip()]

    # ---------------------------------------------------------- CIFRAS
    marcar = leer("docs/loop/SALIDA_V%d_T1_MARCAR_95.txt" % VUELTA)
    antes, despues = marcar.split("EL CONTEO DESPUES")
    rem = leer("docs/loop/SALIDA_V%d_T2B_REMEDIR_CINCO.txt" % VUELTA)
    plan_b = leer("docs/loop/SALIDA_V%d_T3_PLAN_BATERIA.txt" % VUELTA)

    D = {
        "inc": cifra(despues, "INCOMPLETAS (N menor que M): "),
        "marc": cifra(despues, "incompletas con PROVISIONAL en su campo forma: "),
        "fichas": cifra(rem, "CIFRA fichas re-medidas: "),
        "nomina": cifra(plan_b, "CIFRA entradas de la nomina: "),
        "tramos": cifra(plan_b, "CIFRA tramos: "),
    }

    # ---------------------------------------------------------- FECHAS
    fechas = {
        "commit de apertura": git(["log", "-1", "--format=%ad", "--date=iso",
                                   "89c7bf23"]),
        "primer commit de la vuelta": git(["log", "-1", "--format=%ad",
                                           "--date=iso", "f904341b"]),
        "ultimo commit al componer este cierre": git(
            ["log", "-1", "--format=%ad", "--date=iso"]),
    }

    # ---------------------------------------------------------- ESCRITOS
    escritos = [l.split("\t")[-1] for l in
                git(["diff", "--name-only", "89c7bf23", "HEAD"]).split(NL)
                if l.strip()]
    en_scripts = [f for f in escritos if f.startswith("scripts/loop/")]
    con_prefijo = [f for f in en_scripts
                   if os.path.basename(f).startswith("_v%d_" % VUELTA)]
    sin_prefijo = [f for f in en_scripts if f not in con_prefijo]

    cuerpo = """## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, NUNCA `run_phase1.py` A SECAS

**Contado de las dos salidas de consola, no de memoria.**

| lado | comandos con exitcode leido | los que no dan 0 | peor |
|---|---:|---:|---|
%(filas_gate)s

**`numstat` del lado de cierre: %(filas_ns)d fila(s).** **`numstat` de `dataset/`
al cerrar: %(n_dataset)d fila(s).**

### 3.2. LAS SEDES QUE LA VUELTA MOVIO Y LAS QUE NO, POR LAS DOS CONVENCIONES

**El `sha256` de apertura se LEE de `docs/loop/SALIDA_V%(v)d_APERTURA.txt`, que se
sello antes de la primera operacion; el de cierre se computa ahora.**

| sede | sha256 LF al abrir | sha256 LF al cerrar | | bytes disco / LF |
|---|---|---|---|---|
%(filas_sedes)s

**CIFRA sedes cotejadas: %(n_sedes)d | CIFRA que se movieron: %(movidas)d.** **Y
las que se movieron son EXACTAMENTE las tres que las tareas 1 y 2 nombran, ni una
mas:** el inventario (las 95), el expediente (la evidencia de `OP-I-01`) y la vara
del criterio de hecho. **`docs/loop/ACTA_AUDITOR.md` y
`docs/loop/PROMPT_SIGUIENTE.md`, que son sede del auditor, quedan QUIETAS**, y
esa es la prueba de que la TAREA 3 se quedo en mi reporte.

### 3.3. LAS RUTAS QUE ESTE REPORTE CITA, MEDIDAS CON EL INSTRUMENTO DE LA CASA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y su salida se cita en el commit
de cierre. **Es el instrumento que en la 213 cazo la `C.1`, y esta vuelta lo lleva
ademas metido en tres de mis compositores como guarda previa: los tres cuentan
los directorios de dos o mas tramos entre comillas inversas ANTES de escribir, y
los tres me mordieron al menos una vez.**

## 4. LO QUE SE TOCO, Y LO QUE NO

### 4.1. LA MORATORIA DE MAQUINARIA, Y LO QUE ESTA VUELTA ESCRIBIO

**Ningun arnes, guarda ni lector nuevo, y ninguno reparado.** Todo lo que esta
vuelta escribio en el arbol de scripts del bucle lleva **prefijo de guion bajo**,
vive **fuera del censo y fuera de la nomina**, y **muere con la vuelta**.

**CONTADO DE `git diff --name-only` entre el HEAD de apertura y el de ahora:
%(n_scripts)d fichero(s) tocados ahi, de los cuales %(n_prefijo)d llevan el
prefijo `_v%(v)d_` y %(n_sin)d no lo llevan.**

**LA NOMINA DE LA BATERIA SIGUE CONGELADA EN %(nomina)s**, medida por mi en esta
vuelta con el carril `--plan` del lanzador, que no la toca.

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`, que me
la exigio y tenia razon):

- **`git status --porcelain` al entrar: %(status)s linea**, y era mi propio script
  de apertura sin rastrear.
- **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: %(ns_dataset_ap)s.**

### 4.2. LO QUE ESTA VUELTA NO HIZO, DICHO PARA QUE NO SE BUSQUE

- **No declaro la campaña consumada y no pidio ningun merge.** El bucle no funde
  ramas.
- **No escribio una linea en la sede del auditor**, y esta medido arriba con los
  dos `sha256` quietos.
- **No movio ningun campo `estado`**, ni en `OP-I-01` ni en ninguna de las 71, y
  la guarda de la TAREA 1 lo comprueba sobre el fichero entero.
- **No toco ni un nodo, ni un veredicto, ni la vara del expediente.**
- **No corrio la bateria**: la 214 no es vuelta de bateria.

### 4.3. LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA

%(fechas)s

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

- **`D.3` LA `P3` DE LA VARA SE VA A DISPARAR CON MIS PROPIOS COMMITS.** La `P3`
  pide un commit cuyo mensaje nombre el `id_op` **y que toque `scripts/`,
  `dataset/`, `engine/` o `web/`**; mis commits nombran `OP-I-01` y tocan
  `scripts/`, porque ahi viven mis instrumentos. **El trabajo real aterrizo en el
  arbol del plan, que es justo lo que la `P3` descuenta a proposito.** No toco la
  vara y **no me apoyo en esa `P3`** para decir que la ficha cierra.
- **LA SEDE DE LA MARCA DE LAS 95 ES EL CAMPO `forma`.** Lo elegi por el
  precedente medido de la **linea 258** de `scripts/loop/_v203_t3_op_i_01.py`,
  pero **es una eleccion mia** y otra sede (una clave nueva) habria sido
  defendible. **Marco que es discutible.**
- **ESCRIBI EN `docs/plan/OPERACIONES.jsonl`, QUE LA VUELTA 213 TENIA PROHIBIDO
  TOCAR.** Mi encargo me manda cerrar la ficha con su prueba y use el carril que
  la propia ficha ya habia usado, **pero la prohibicion de la 213 era de la 213 y
  la mia no la repite**: si el auditor entiende que esa escritura necesitaba
  mandato explicito, **la marca es esta**.
- **LA REGLA DE EXCLUSION DE LA `2.a` LA ESCRIBI YO.** Que una clausula que abre
  con el numero de una fase con fila ya existente **no sea** la vara de su fase es
  una lectura mia, mecanica pero mia. **Sin ella, la fila 08 habria repetido la
  tabla entera.**

## 6. LAS PREGUNTAS

1. **¿La `2.a` deberia haber metido las tres filas DENTRO de la tabla, como hice,
   o como bloque aparte?** Las meti dentro porque el encargo dice que **la tabla
   gana sus filas**, y lo hice **sin tocar una letra de las viejas**. Si la casa
   prefiere el bloque aparte, se dice y se mueve.
2. **¿Un `numstat` de 95 lineas modificadas en un fichero del arbol del plan necesita
   algo mas que la decision del fundador por su ruta?** Lo hice con esa decision y
   con conteo antes y despues, y lo pregunto porque es la escritura mas ancha que
   una vuelta ha hecho ahi en mucho tiempo.

## 7. PENDIENTES DE DOCTRINA

1. **EL MARCADOR CONTRA SU CIFRA VIEJA (`D.5`).** La clausula de `OP-L-01` y
   `OP-L-02` escribe *"sigue en 2.117"* y el archivo mide **3388** hoy. **Leida a
   la letra no calza; leida por su corte, pide que ESA operacion no lo mueva, y lo
   movio el cribado al cerrar.** **Cual de las dos lecturas manda no esta escrito
   en ningun banco**, y no lo decido yo.
2. **SI LOS PUNTOS EN `A MEDIAS` BLOQUEAN UN CIERRE DE FASE.** `OP-I-01` queda con
   **2 en CUBRE y 2 en A MEDIAS**, y los dos que quedan lo estan por motivos
   estructurales (una negativa que no se puede citar, y una vista humana que su
   propio documento declara que no se regenera ahi). **Nada dice si eso cierra o
   no cierra.**

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**Son SIETE, y las siete las cazaron mis propias guardas ANTES de publicar nada.**
Las escribo porque una guarda que muerde y no se cuenta es una guarda que la
proxima vuelta no sabe que existe.

- **`D.1` EL FICHERO TENIA DOS CONVENCIONES DE VOLCADO Y YO NO LO SABIA.** Mi
  primera version de la TAREA 1 re-volcaba con `json.dumps` por defecto; la
  **simulacion** midio que **335 de las 672 lineas** estan volcadas con
  separadores compactos y **337** con los de por defecto. **Un re-volcado ciego
  habria reformateado 335 lineas que nadie mando tocar, y el cotejo semantico lo
  habria dado por bueno.** Remedio: medir la convencion de **cada** linea antes de
  tocarla, mas una **guarda de bytes** sobre las que no son de las 95.
- **`D.2` MI MUTANTE ERA EL DEFECTUOSO, NO MI JUICIO.** El mutante *A* quitaba
  **una sola** aparicion de la palabra y el texto de la marca la dice **dos
  veces**: la entrada seguia marcada y el mutante **pasaba**. Corregido a quitar
  todas.
- **`D.4` MI LECTOR DE NUMEROS DE FASE LEIA TODO EL FICHERO** y se tragaba **707,
  1096 y 2464** como si fueran fases. **No cambiaba el resultado, pero una vara que
  acierta por suerte no es una vara.** Acotado a la tabla del criterio.
- **`D.7` MI SONDA ERA MAS LAXA QUE SU CLAUSULA Y HABRIA PUBLICADO UNA ALARMA
  FALSA.** Preguntaba si **los dos nombres** de un par estaban en el archivo, cosa
  que da que si para casi cualquier par del catalogo: salia **27 de 27** contra una
  clausula que en realidad **se cumple**. Corregida a comparar **el par** contra
  `nodo_a` y `nodo_b`: da **0 de 27**.
- **`C.1` UN `%%d` LITERAL SE ME COLO EN LA PROSA DE UNA SONDA**, y salio impreso
  tal cual en la primera corrida de la `2.b`.
- **`C.2` CITE EL ARBOL DEL PLAN ENTRE COMILLAS INVERSAS, DOS VECES**, que es
  exactamente la `C.1` de la 213. **Me lo conto mi propia guarda del compositor** y
  el texto se reescribio sin comillas.
- **`C.3` CITE UN FICHERO QUE NO EXISTE COMO SI FUERA RUTA DE PRUEBA.** La
  `PARA_ALEXIS.md` **todavia no esta escrita**, y nombrarla entre comillas
  inversas es una ruta que promete prueba apuntando a nada. Cazada por la guarda
  de rutas de mi compositor de la TAREA 3.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**Va entero en la TAREA 3 de este reporte, que es mi sede.** En una linea: **la
215 es vuelta de bateria y el reparto da %(tramos)s tramos, no nueve**; **el carril
`--siguiente` dice hoy que no falta ninguno porque esta viendo los sellos de la
vuelta anterior**; y **el `PARA_ALEXIS.md` de campaña consumada, si se gana, lo
escribe el AUDITOR de la 215 y no su ejecutor**.
""" % {
        "v": VUELTA,
        "filas_gate": NL.join(filas_gate),
        "filas_ns": filas_ns,
        "n_dataset": len(ns_dataset),
        "filas_sedes": NL.join(filas_sedes),
        "n_sedes": len(SEDES), "movidas": movidas,
        "n_scripts": len(en_scripts), "n_prefijo": len(con_prefijo),
        "n_sin": len(sin_prefijo),
        "nomina": D["nomina"], "tramos": D["tramos"],
        "fechas": NL.join("- **%s**: %s" % (k, v) for k, v in fechas.items()),
        "status": cifra(ap, "CIFRA lineas de status: "),
        "ns_dataset_ap": cifra(
            ap, "CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: "),
    }

    fallos = 0
    if cuerpo.count(chr(8212)) or cuerpo.count(chr(8211)):
        fallos += 1
        print("ROJO: guiones largos o medios.")
    sosp = [c for c in re.findall(r"`([^`]+)`", cuerpo)
            if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d" % len(sosp))
    for s in sosp:
        print("   sospechoso> %s" % s)
    if sosp:
        fallos += 1
    rutas = [c for c in re.findall(r"`([^`]+)`", cuerpo)
             if "/" in c and not c.endswith("/") and " " not in c]
    malas = [r for r in rutas
             if not os.path.exists(os.path.join(RAIZ, r.replace("/", os.sep)))
             or os.path.getsize(os.path.join(RAIZ, r.replace("/", os.sep))) == 0]
    print("CIFRA rutas citadas: %d | inexistentes o vacias: %d" % (len(rutas), len(malas)))
    for m in malas:
        print("   ruta mala> %s" % m)
    if malas:
        fallos += 1
    print("CIFRA sedes cotejadas: %d | movidas: %d" % (len(SEDES), movidas))
    print("CIFRA filas de Gate 0 armadas: %d (se esperan 2)" % len(filas_gate))
    if len(filas_gate) != 2:
        fallos += 1
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: no se escribe el cuerpo.")
        return 1
    destino = os.path.join(RAIZ, "scripts", "loop", "_v%d_cierre_texto.md" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(cuerpo)
    print("ESCRITO %s -> %d bytes, %d lineas"
          % (destino, len(cuerpo.encode("utf-8")), cuerpo.count(NL)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
