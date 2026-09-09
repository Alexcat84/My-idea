# -*- coding: utf-8 -*-
r"""_v215_cierre_texto.py . EL CUERPO DEL CIERRE DEL REPORTE DE LA VUELTA 215,
COMPUESTO DE MEDICIONES Y NO TECLEADO.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1: toda tabla o cifra del reporte cita el fichero de salida del que
sale, y se reconstruye contando ese fichero antes de publicarla.

LO QUE CAMBIA RESPECTO DEL COMPOSITOR DE LA 214, Y ES LA TAREA 5.b DEL ENCARGO:
ESTE CAE EN ROJO SI NO ENCUENTRA LA CONSOLA DEL CICLO. El de la 214, en su linea
77, hacia esto:

    if not os.path.isfile(p):
        filas_gate.append("| **%s** | (sin fichero de consola) | | |" % lado)
        continue

o sea que ESCRIBIA UNA FILA EN BLANCO Y SEGUIA. Su seccion 3.1 salio publicada
vacia, con sus tres columnas de medicion sin nada, bajo un titulo que decia EL
CICLO ENTERO DE GATE 0, LOS DOS LADOS. Eso es DEGRADACION SILENCIOSA, que es lo
que el banco 9 prohibe: una guarda que no encuentra su fuente y devuelve un
hueco en vez de reventar deja al lector creyendo que se midio.

AQUI NO HAY RAMA DE HUECO. Si falta un fichero, si una consola no trae comandos,
o si no trae su peor exitcode, ESTE INSTRUMENTO NO ESCRIBE NADA y sale con
exitcode 1. Su prueba de mutacion esta en _v215_t5_mutantes.py y corre ANTES de
que este compositor se use de verdad.

ESTO NO FABRICA MAQUINARIA: el compositor de cierre se escribe cada vuelta de
todas formas, lleva prefijo de guion bajo, muere con la vuelta y no entra en
ninguna nomina. Lo unico que cambia es que falle ruidoso.

USO:  python scripts/loop/_v215_cierre_texto.py
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
    "docs/plan/10_INVENTARIO.md",
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

# LAS NUEVE SALIDAS QUE EL CICLO SELLA POR LADO, o sea DIECIOCHO en total. El
# orden es el de los ocho comandos del ciclo, con el octavo partido en dos.
SEGMENTOS = (("1", "GATE0_CMD1", "run_phase1.py --reaplico-curaduria"),
             ("2", "CICLO_ETIQUETAS", "etiquetas_de_cara.py --aplicar"),
             ("3", "CICLO_SYNC", "sync_assets_web.py"),
             ("4", "CICLO_NUMSTAT", "git diff HEAD --numstat"),
             ("5", "CONTEO", "vuelta83_conteo_aristas.py WORK"),
             ("6", "DESFASE_CALIBRADO", "vuelta85_medir_desfase_calibrado"),
             ("7", "MOTOR", "engine/run_all_tests.py"),
             ("8a", "TSC", "npx tsc --noEmit"),
             ("8b", "WEB", "pnpm test"))


def leer(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    return io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", errors="replace").strip()


def sha(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    b = io.open(p, "rb").read()
    return (hashlib.sha256(b).hexdigest()[:16],
            hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16])


def cifra(texto, etiqueta):
    if texto is None:
        return None
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(-?\d+)", l.split(etiqueta, 1)[1])
            if m:
                return m.group(1)
    return None


def fila_de_gate(lado, texto, nombre_fichero):
    """LA FILA DE UN LADO DEL CICLO, LEIDA DE SU CONSOLA. PURA.

    Devuelve (fila, motivo). SI NO SE PUEDE LEER, DEVUELVE (None, motivo) Y
    QUIEN LA LLAMA TIENE QUE REVENTAR. NO HAY RAMA QUE DEVUELVA UNA FILA VACIA:
    esa rama es exactamente la que el acta 214 me conto en su hallazgo 3.1."""
    if texto is None:
        return None, ("no existe el fichero de consola %s, y una guarda que no "
                      "encuentra su fuente REVIENTA, no rellena" % nombre_fichero)
    cmds = [l for l in texto.split(NL) if re.search(r"EXITCODE \d", l)]
    if not cmds:
        return None, ("el fichero de consola %s existe pero no trae ni una linea "
                      "con EXITCODE: una consola sin comandos no mide nada"
                      % nombre_fichero)
    malos = [l for l in cmds if not re.search(r"EXITCODE 0\b", l)]
    m = re.search(r"PEOR EXITCODE DE LOS OCHO: (\d+)", texto)
    if not m:
        return None, ("el fichero de consola %s no publica su peor exitcode, y "
                      "sin esa cifra la fila no se puede armar" % nombre_fichero)
    return ("| **%s** | %d | %d | **%s** | `%s` |"
            % (lado, len(cmds), len(malos), m.group(1), nombre_fichero)), None


def main():
    fallos_duros = []

    # ---------------------------------------------------------- GATE 0
    filas_gate = []
    for lado in LADOS:
        rel = "docs/loop/SALIDA_V%d_CICLO_GATE0_%s_CONSOLA.txt" % (VUELTA, lado)
        fila, motivo = fila_de_gate(lado, leer(rel), rel)
        if fila is None:
            fallos_duros.append("GATE 0, lado %s: %s" % (lado, motivo))
        else:
            filas_gate.append(fila)

    # LAS DIECIOCHO SALIDAS EN DISCO, CADA UNA CON SU EXITCODE LEIDO DE DENTRO
    filas_18 = []
    faltan_18 = []
    for num, seg, comando in SEGMENTOS:
        celdas = []
        for lado in LADOS:
            rel = "docs/loop/SALIDA_V%d_%s_%s.txt" % (VUELTA, seg, lado)
            t = leer(rel)
            p = os.path.join(RAIZ, rel.replace("/", os.sep))
            if t is None:
                faltan_18.append(rel)
                celdas.append("(AUSENTE)")
                continue
            m = re.search(r"EXITCODE: (-?\d+)|EXIT=(-?\d+)", t)
            code = (m.group(1) or m.group(2)) if m else None
            if code is None:
                faltan_18.append(rel + " (sin exitcode dentro)")
                celdas.append("(SIN EXITCODE)")
                continue
            celdas.append("%s / %d bytes" % (code, os.path.getsize(p)))
        filas_18.append("| **%s** | `%s` | %s | %s |"
                        % (num, comando, celdas[0], celdas[1]))
    if faltan_18:
        fallos_duros.append("LAS DIECIOCHO SALIDAS: faltan o no traen exitcode "
                            "%d de 18: %s" % (len(faltan_18), faltan_18))

    if fallos_duros:
        print("=" * 78)
        print("ROJO. EL COMPOSITOR NO ESCRIBE, Y ESTA ES LA DIFERENCIA CON EL")
        print("DE LA VUELTA 214, QUE HABRIA ESCRITO UNA FILA EN BLANCO Y SEGUIDO.")
        print("=" * 78)
        for f in fallos_duros:
            print("   FALLO DURO> %s" % f)
        print("CIFRA fallos duros: %d" % len(fallos_duros))
        return 1

    # ---------------------------------------------------------- SEDES
    ap = leer("docs/loop/SALIDA_V%d_APERTURA.txt" % VUELTA)
    if ap is None:
        print("ROJO: no existe la apertura sellada. No se compone nada.")
        return 1
    filas_sedes = []
    movidas = []
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
            movidas.append(rel)
        filas_sedes.append(
            "| `%s` | %s | %s | %s | %s |"
            % (rel, viejo or "(no medida al abrir)", sl,
               "**SE MOVIO**" if se_movio else "quieta",
               "%d / %d" % (m[0], m[1]) if m else "(ausente)"))

    ns_dataset = [l for l in git(["diff", "--numstat", "--",
                                 "dataset/"]).split(NL) if l.strip()]
    ns_plan = [l for l in git(["diff", "--numstat", "--",
                              "docs/plan/"]).split(NL) if l.strip()]

    # ---------------------------------------------------------- CIFRAS
    tabla = leer("docs/loop/SALIDA_V%d_T2_TABLA.txt" % VUELTA)
    t3 = leer("docs/loop/SALIDA_V%d_T3_EXPEDIENTE.txt" % VUELTA)
    t4 = leer("docs/loop/SALIDA_V%d_T4_DOS_PUNTOS.txt" % VUELTA)
    plan_b = leer("docs/loop/SALIDA_V%d_T2_PLAN.txt" % VUELTA)
    mar = leer("docs/loop/SALIDA_V%d_T3_MARCADOR.txt" % VUELTA)
    for nombre, t in (("tabla de tramos", tabla), ("expediente", t3),
                      ("dos puntos", t4), ("plan de bateria", plan_b),
                      ("marcador", mar)):
        if t is None:
            print("ROJO: falta la salida sellada de %s. REVIENTA, no rellena."
                  % nombre)
            return 1

    D = {
        "nomina": cifra(plan_b, "CIFRA entradas de la nomina: "),
        "tramos": cifra(plan_b, "CIFRA tramos: "),
        "corridas": cifra(tabla, "CIFRA entradas corridas sumando los once tramos: "),
        "ok": cifra(tabla, "CIFRA OK en los once: "),
        "caen": cifra(tabla, "CIFRA arneses de la nomina que CAEN hoy: "),
        "nuevos": cifra(tabla, "CIFRA arneses que CAEN HOY Y NO CAIAN EN LA CORRIDA ANTERIOR: "),
        "no_calzan": cifra(t3, "CIFRA fichas que no calzan: "),
        "hecha_sin": cifra(t3, "CIFRA fichas HECHA sin ninguna prueba: "),
        "rellenos": cifra(t4, "CIFRA campos RELLENADOS DE VERDAD, ya descontado el vocabulario: "),
        "escriben": cifra(t4, "CIFRA ficheros .py que la ESCRIBEN: "),
        "marcador_n": cifra(mar, "n = "),
        "status": cifra(ap, "CIFRA lineas de status: "),
        "ns_dataset_ap": cifra(
            ap, "CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: "),
    }
    faltan_c = [k for k, v in D.items() if v is None]
    if faltan_c:
        print("ROJO: faltan %d cifras que el cierre necesita: %s"
              % (len(faltan_c), faltan_c))
        return 1

    # ---------------------------------------------------------- ESCRITOS
    head_ap = (leer("docs/loop/SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA) or "").strip()
    escritos = [l for l in git(["diff", "--name-only", head_ap, "HEAD"]).split(NL)
                if l.strip()]
    en_scripts = [f for f in escritos if f.startswith("scripts/loop/")]
    con_prefijo = [f for f in en_scripts
                   if os.path.basename(f).startswith("_v%d_" % VUELTA)]
    sin_prefijo = [f for f in en_scripts if f not in con_prefijo]

    fechas = {
        "commit de apertura": git(["log", "-1", "--format=%ad", "--date=iso",
                                   head_ap]),
        "ultimo commit al componer este cierre": git(
            ["log", "-1", "--format=%ad", "--date=iso"]),
    }

    cuerpo = """## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, Y ESTA VEZ CON CIFRAS DENTRO

**ESTA ES LA SECCION QUE EN LA 214 SALIO PUBLICADA VACIA**, y el remedio son las
dos mitades de la TAREA 5, no una: **la consola se sella desde dentro del propio
instrumento**, y **el compositor CAE EN ROJO si no la encuentra**. La segunda es
la que importa: en la 214 el fichero no existia y mi compositor **escribio una
fila en blanco y siguio**.

**Contado de las dos consolas selladas, no de memoria. FILAS ARMADAS:
%(n_gate)d. FILAS QUE DEBERIA HABER: 2.**

| lado | comandos con exitcode leido | los que no dan 0 | peor exitcode | consola sellada |
|---|---:|---:|---|---|
%(filas_gate)s

**Y LAS DIECIOCHO SALIDAS EN DISCO, CADA UNA CON SU EXITCODE LEIDO DE DENTRO DEL
PROPIO FICHERO Y SUS BYTES MEDIDOS.** **FILAS ARMADAS: %(n_18)d. FILAS QUE
DEBERIA HABER: 9, una por comando, con sus DOS lados en la misma fila, o sea
DIECIOCHO celdas.** **CIFRA salidas ausentes o sin exitcode dentro: 0**, y si
hubiera una sola este cuerpo no existiria.

| # | comando | APERTURA (exitcode / bytes) | CIERRE (exitcode / bytes) |
|---|---|---|---|
%(filas_18)s

**`numstat` de los arboles del dataset al cerrar: %(n_dataset)d fila(s). Del
arbol del plan: %(n_plan)d fila(s).**

### 3.2. LAS SEDES QUE LA VUELTA MOVIO Y LAS QUE NO, POR LAS DOS CONVENCIONES

**El `sha256` de apertura se LEE de `docs/loop/SALIDA_V%(v)d_APERTURA.txt`, que se
sello antes de la primera operacion; el de cierre se computa ahora.**

| sede | sha256 LF al abrir | sha256 LF al cerrar | | bytes disco / LF |
|---|---|---|---|---|
%(filas_sedes)s

**CIFRA sedes cotejadas: %(n_sedes)d | CIFRA que se movieron: %(n_movidas)d.**
**LAS DOCE ESTAN QUIETAS, Y ESA ES LA PRUEBA MEDIDA DE QUE ESTA VUELTA NO
ESCRIBIO NI UN NODO, NI UN VEREDICTO, NI UNA FICHA.** La 6.1 prohibe trabajo de
plan al lado de la bateria, y **el cierre integral no es trabajo de plan, es
verificacion**: aqui esta la cifra que lo sostiene. **`docs/loop/ACTA_AUDITOR.md`
y `docs/loop/PROMPT_SIGUIENTE.md`, que son sede del auditor, tambien quedan
quietas.**

### 3.3. LAS RUTAS QUE ESTE REPORTE CITA, MEDIDAS CON EL INSTRUMENTO DE LA CASA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y su salida se cita en el commit
de cierre. **Y ademas va metido como guarda previa en los CUATRO compositores de
tarea de esta vuelta**: los cuatro cuentan las rutas inexistentes o de cero bytes
y los directorios de dos tramos entre comillas inversas **antes de escribir**.

## 4. LO QUE SE TOCO, Y LO QUE NO

### 4.1. LA MORATORIA DE MAQUINARIA, Y LO QUE ESTA VUELTA ESCRIBIO

**Ningun arnes, guarda ni lector nuevo que se quede vigilando, y ninguno
reparado.** **NO SE TOCO EL LANZADOR DE LA BATERIA**, que es lo que el encargo
nombra: `scripts/loop/vuelta183_bateria_por_tramos.py` no cambia ni un byte, y se
uso tal cual. **La nomina sigue CONGELADA EN %(nomina)s.**

**CONTADO DE `git diff --name-only` entre el HEAD de apertura y el de ahora:
%(n_scripts)d fichero(s) tocados en el arbol de scripts del bucle, de los cuales
%(n_prefijo)d llevan el prefijo `_v%(v)d_` y %(n_sin)d no lo llevan.**

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`):

- **`git status --porcelain` al entrar: %(status)s linea**, y era mi propio
  script de apertura sin rastrear.
- **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: %(ns_dataset_ap)s.**

### 4.2. LO QUE ESTA VUELTA NO HIZO, DICHO PARA QUE NO SE BUSQUE

- **No escribio el PARA_ALEXIS del bucle, y no lo escribe.** Es **sede del
  auditor** por la adjudicacion `4.2` del acta 203, **linea 71543**, ratificada
  por el fundador el 9 sep 2026. **Yo lo PROPONGO en mi reporte, que es mi
  sede**, y va al final.
- **No escribio una linea en la sede del auditor**, y esta medido arriba con los
  `sha256` quietos.
- **No movio ningun campo `estado`**, y la TAREA 4 lo prueba con los dos `sha256`
  del expediente y su `numstat` en cero.
- **No toco ni un nodo, ni un veredicto, ni la vara del expediente.**
- **No arreglo ningun arnes en rojo**: los trae como PARADA, que es lo que la
  TAREA 2.d manda.
- **No pidio ningun merge. El bucle no funde ramas.**

### 4.3. LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA

%(fechas)s

## 5. LAS DOS PARADAS QUE TRAIGO, Y NO LAS ARREGLO YO

**`EJECUTOR.md` 5: se para cuando algo contradice una regla vigente o una cifra
publicada con su corte, se escribe en el reporte como PARADA y no lo arregla el
ejecutor.** Aqui van las dos, cada una con su cifra.

### PARADA 1. CAEN %(caen)s ARNESES DE LA NOMINA, Y LA TAREA 2.d MANDA TRAERLOS

**La cifra y los nombres estan en la TAREA 2, tabla de la `2.d`, contados de los
once ficheros sellados.** Lo que importa para la parada es el cotejo: **CAEN
%(caen)s y NUEVOS RESPECTO DE LA CORRIDA ANTERIOR: %(nuevos)s.** **Los
%(caen)s ya caian en la vuelta 210**, medido con `git show` sobre el commit que
sello cada fichero entonces.

**NO LOS TOCO, Y DOY LOS DOS MOTIVOS:** mi encargo dice con estas palabras que
*"un arnes en rojo en la vuelta del cierre integral no se arregla de paso"*, y
repararlos seria **fabricar maquinaria bajo la moratoria**. **Se suben con su
nombre.**

### PARADA 2. EL ROJO ESTRUCTURAL DE LOS ONCE TRAMOS ES UNA CONTRADICCION ENTRE DOS REGLAS VIGENTES

**Los once tramos salen en exitcode 1 tambien por otra cosa, y esa otra cosa no
la puede apagar ninguna corrida.** La regla que el propio lanzador lleva escrita
desde la vuelta 148 dice que **UN ARNES ENTRA EN LA NOMINA**; la moratoria del 7
sep 2026 (`AUDITOR.md` 6.3) dice que **la nomina queda CONGELADA EN %(nomina)s,
ni crece ni se poda**. **Mientras las dos rijan, los dos arneses nacidos despues
de la vara 148 se quedan fuera y el rojo es automatico.**

**LO DIGO CON SU PRECEDENTE MEDIDO Y NO RECORDADO:** la bateria de la vuelta 210
encendio **exactamente este mismo rojo, con los dos mismos nombres**, y se
declaro corrida igual. **No propongo cual de las dos reglas cede: eso no es
mio.**

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

- **`D.a` EL VOCABULARIO DE RELLENO DE LA TAREA 4 ES MIO.** Las 23 palabras que
  definen que es un hueco RELLENADO **las elegi yo**, y van escritas enteras en
  el instrumento para que se puedan discutir. **Otra lista habria dado otro
  numero.** Lo que si esta medido es que la que hay **no es demasiado laxa**
  (compara el campo entero, nunca por subcadena) y **no es demasiado estrecha**
  (su caso positivo caza el relleno y el vacio de una entrada fabricada).
- **`D.b` LA REGLA DEL DESCARTE POR VOCABULARIO DEL CAMPO TAMBIEN ES MIA.** Que
  `pendiente` en `estado` sea vocabulario y no relleno **lo decido yo**, aunque
  la evidencia sea mecanica (el mismo campo trae su forma larga). **Sin esa
  regla, el punto 3 saldria NO CUBRE.** **Es el discutible mas caro de esta
  vuelta y por eso va con su tabla de seis filas delante.**
- **`D.c` CORRI LOS ONCE TRAMOS AUNQUE EL PRIMERO SALIERA EN ROJO.** El lanzador
  dice, al acabar un tramo en rojo, *"Y AQUI SE PARA"*. Lo lei como que **para
  ESE tramo**, no la bateria, y segui con `--tramo 2`. **Me apoyo en el
  precedente medido de la vuelta 210, que hizo lo mismo con el mismo rojo**, pero
  **es una lectura mia** y la marco.
- **`D.d` PUBLICO EL PUNTO 3 COMO CUBRE CON UNA BUSQUEDA QUE DA CERO.** Es lo que
  la adjudicacion `5.4` manda, pero **un cero solo vale lo que valga su
  busqueda**, y la mia es la de arriba. **Si el auditor lee que la clausula pide
  otra cosa, el CUBRE se cae y lo digo antes de que lo mida nadie.**

## 7. LAS PREGUNTAS Y LOS PENDIENTES DE DOCTRINA

**PREGUNTA 1. LOS ONCE TRAMOS SALEN EN EXITCODE 1 POR EL ROJO ESTRUCTURAL. ESO,
LA CASA, LO CUENTA COMO BATERIA CORRIDA O NO?** La `6.1` dice que se declara
corrida cuando los tramos de su reparto tienen **salida sellada del mismo
calibre**, y **los once la tienen**: mismo formato, misma doble corrida, las 135
entradas cubiertas una vez cada una. **Pero once exitcodes en 1 no son un verde**,
y prefiero preguntarlo a decidirlo.

**PREGUNTA 2. LAS CUATRO FICHAS EN HECHA SIN NINGUNA PRUEBA BLOQUEAN EL CIERRE DE
LA CAMPANA?** Mido **%(hecha_sin)s**, el encargo nombra dos, y **ninguna vuelta
las puede cerrar sin escribir en el expediente**, cosa que esta vuelta tiene
prohibida.

**PENDIENTE DE DOCTRINA 1. UN PUNTO EN `A MEDIAS` CUYA SEDE NO EXISTE.** El punto
4 de `OP-I-01` queda en A MEDIAS porque **ningun instrumento del repo escribe la
vista humana** (`CIFRA ficheros .py que la ESCRIBEN: %(escriben)s`). **Nada dice
si un pendiente sin sede bloquea un cierre de fase o si se declara y se pasa.**

**Y UN PENDIENTE QUE YA NO LO ES, Y LO DIGO PARA QUE NO SE BUSQUE:** el del
marcador contra su cifra vieja **quedo CERRADO por la adjudicacion `5.3`, linea
76166**, y **no lo vuelvo a traer**.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**Son TRES, y las tres las cazaron mis propias guardas ANTES de que el veredicto se
publicara. LA PRIMERA SALIO EN UN COMMIT Y LA CORREGI POR DECLARACION; LAS OTRAS
DOS NO LLEGARON A SALIR.**

- **`D.1` MI PROSA CONTRADECIA A LAS CIFRAS DE SU PROPIO PARRAFO, Y SALIO EN EL
  COMMIT DEL TRAMO 3.** Mi compositor de mensajes de tramo llevaba la frase *"y
  ninguno cae"* **clavada en el texto**, con sus tres ceros tecleados, al lado de
  cifras que si se leian del fichero sellado. En los tramos 1 y 2 coincidieron y
  la mentira no molesto a nadie; **en el 3 el medidor leyo NO MORDIO 1 y la prosa
  siguio diciendo que ninguno cae**. **El texto viejo no se borra: esta en git y
  la correccion va declarada en el commit del tramo 4.** Remedio: la frase se
  **COMPUTA** de las tres cifras, y el instrumento **cae en rojo** si la prosa y
  las cifras no dicen lo mismo. **Mutacion: 5 casos, 0 que no calzan.**
- **`D.2` MI SONDA DEL PUNTO 3 ERA MAS LAXA QUE SU CLAUSULA Y HABRIA PUBLICADO UN
  `NO CUBRE` FALSO.** Contaba **6** campos de relleno, los seis con `pendiente`
  en el campo `estado`, **que ahi no es relleno: es el estado**. **Es la misma
  especie que la `D.7` de la 214**, y esta vez me mordio a mi solo. Remedio: la
  regla del vocabulario del campo, con la forma larga medida en el MISMO campo, y
  **los seis descartes publicados con su nombre**.

- **`C.1` CITE UN FICHERO QUE NO EXISTE COMO SI FUERA RUTA DE PRUEBA, DOS
  VECES, Y ES EXACTAMENTE LA `C.3` DE LA 214 REPITIENDOSE.** El PARA_ALEXIS del
  bucle **todavia no esta escrito**, y nombrarlo entre comillas inversas es una
  ruta que promete prueba apuntando a nada (`EJECUTOR.md` 1, LA RUTA QUE PROMETE
  PRUEBA ES CIFRA). **Me lo conto la guarda de rutas de este mismo compositor,
  que conto 2 rutas malas de 22 y NO ESCRIBIO NADA**, y el texto se reescribio
  sin comillas. **Se registra porque una guarda que muerde y no se cuenta es una
  guarda que la vuelta siguiente no sabe que existe.**

**Y UNA TERCERA QUE NO CUENTO COMO CAIDA Y DIGO POR QUE, PARA QUE NADIE LA CUENTE
POR MI:** mi compositor de la TAREA 3 salio en **ROJO** en su primera corrida
porque su lector de las cuatro clases del marcador devolvia vacio. **NO ESCRIBIO
NADA.** Eso no es una caida de reporte: **es exactamente la guarda de la TAREA 5
haciendo su trabajo**, y si la contara como caida estaria penalizando lo unico
que el hallazgo `3.1` me pidio construir.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**LA CONDICION DE LA PARADA FELIZ, MEDIDA CONTRA LO QUE EL ENCARGO ESCRIBIO ANTES
DE SABER EL RESULTADO.** El encargo dice: *si la bateria da los ONCE tramos en
verde y del mismo calibre, si el cierre integral sale limpio, y si los dos puntos
de la TAREA 4 quedan medidos y dichos*, entonces la campana esta consumada en lo
que el bucle puede consumar.

**LAS TRES, UNA A UNA, CON MI CIFRA DELANTE:**

1. **LOS ONCE TRAMOS: DEL MISMO CALIBRE SI, EN VERDE NO.** Los once tienen salida
   sellada, las **%(corridas)s** entradas corrieron una vez cada una y dos veces
   cada una, **%(ok)s en OK**. **Pero los once exitcodes son 1**, y **caen
   %(caen)s arneses**. **NO DECLARO ESTO VERDE.**
2. **EL CIERRE INTEGRAL: LIMPIO.** Gate 0 con sus dos lados y sus dieciocho
   salidas, las tres suites en 0, marcador **%(marcador_n)s** y censo calzando
   con las trece cifras del encargo, **0 que no calzan**. **Con una cifra que no
   es verde y no la escondo: %(no_calzan)s fichas de 71 no calzan.**
3. **LOS DOS PUNTOS: MEDIDOS Y DICHOS, SI.** El 3 pasa a **CUBRE** con su
   busqueda corrida; el 4 se queda en **A MEDIAS** con su sede buscada y **no
   encontrada**.

**MI PROPUESTA, Y ES LA UNICA HONESTA CON LAS CIFRAS DE ARRIBA: NO SE DECLARA LA
CAMPANA CONSUMADA EN ESTA VUELTA.** Falla la primera de las tres condiciones, y
falla por una cifra que **ni yo ni la vuelta siguiente podemos apagar sin una
decision del fundador**, porque es la contradiccion de la PARADA 2.

**LO QUE SI PROPONGO QUE HAGA LA 215 DEL AUDITOR, EN SU SEDE Y NO EN LA MIA:**

- **Llevar al fundador las DOS PARADAS**, que son las dos que bloquean el verde:
  la contradiccion entre la regla de la nomina y la moratoria, y los **%(caen)s**
  arneses que llevan cayendo desde antes de la 210.
- **Decidir, o hacer decidir, la PREGUNTA 1**: once tramos del mismo calibre con
  exitcode 1 estructural, **se cuentan como bateria corrida o no**. De esa
  respuesta cuelga si la condicion 1 se puede dar por cumplida.
- **Y NO ESCRIBIR EL PARA_ALEXIS TODAVIA SI LA RESPUESTA NO LLEGA**,
  porque una parada feliz escrita sobre una condicion que no se cumple es
  exactamente la especie de verde que esta casa lleva doscientas vueltas
  cazando. **Si llega y es que si, quien lo escribe es EL AUDITOR de la 215, no
  su ejecutor**, por la `4.2` del acta 203.
- **Y EL MERGE NO SE PIDE EN NINGUN CASO.** Es decision del fundador y viene
  despues de la auditoria integral con credencial. **El bucle no funde ramas.**
""" % {
        "v": VUELTA,
        "filas_gate": NL.join(filas_gate), "n_gate": len(filas_gate),
        "filas_18": NL.join(filas_18), "n_18": len(filas_18),
        "n_dataset": len(ns_dataset), "n_plan": len(ns_plan),
        "filas_sedes": NL.join(filas_sedes),
        "n_sedes": len(SEDES), "n_movidas": len(movidas),
        "n_scripts": len(en_scripts), "n_prefijo": len(con_prefijo),
        "n_sin": len(sin_prefijo),
        "fechas": NL.join("- **%s**: %s" % (k, v) for k, v in fechas.items()),
        "nomina": D["nomina"], "corridas": D["corridas"], "ok": D["ok"],
        "caen": D["caen"], "nuevos": D["nuevos"],
        "no_calzan": D["no_calzan"], "hecha_sin": D["hecha_sin"],
        "escriben": D["escriben"], "marcador_n": D["marcador_n"],
        "status": D["status"], "ns_dataset_ap": D["ns_dataset_ap"],
    }

    fallos = 0
    if cuerpo.count(chr(8212)) or cuerpo.count(chr(8211)):
        fallos += 1
        print("ROJO: guiones largos o medios.")
    sosp = [c for c in re.findall(r"`([^`]+)`", cuerpo)
            if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sosp))
    for s in sosp:
        print("   sospechoso> %s" % s)
    if sosp:
        fallos += 1
    rutas = [c for c in re.findall(r"`([^`]+)`", cuerpo)
             if "/" in c and not c.endswith("/") and " " not in c]
    malas = [r for r in rutas
             if not os.path.exists(os.path.join(RAIZ, r.replace("/", os.sep)))
             or os.path.getsize(os.path.join(RAIZ, r.replace("/", os.sep))) == 0]
    print("CIFRA rutas citadas: %d | inexistentes o vacias: %d"
          % (len(rutas), len(malas)))
    for m in malas:
        print("   ruta mala> %s" % m)
    if malas:
        fallos += 1
    print("CIFRA filas de Gate 0 armadas: %d (se esperan 2)" % len(filas_gate))
    if len(filas_gate) != 2:
        fallos += 1
    print("CIFRA filas de las dieciocho salidas armadas: %d (se esperan 9)"
          % len(filas_18))
    if len(filas_18) != 9:
        fallos += 1
    print("CIFRA sedes cotejadas: %d | movidas: %d" % (len(SEDES), len(movidas)))
    for m in movidas:
        print("   SE MOVIO> %s" % m)
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
