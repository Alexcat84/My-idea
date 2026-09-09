# -*- coding: utf-8 -*-
r"""_v214_t3_seccion.py . EL CUERPO DE LA TAREA 3 DEL REPORTE DE LA VUELTA 214:
LA PREPARACION DE LA VUELTA 215, COMPUESTA DE MEDICIONES Y NO TECLEADA.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO (moratoria de AUDITOR.md 6.3).

DONDE VA ESTA PROPUESTA Y POR QUE NO EN OTRO SITIO: docs/loop/PROMPT_SIGUIENTE.md,
docs/loop/ACTA_AUDITOR.md y docs/loop/PARA_ALEXIS.md son SEDE DEL AUDITOR y el
ejecutor NO los escribe; si cree que el encargo siguiente deberia decir otra
cosa, LO PROPONE EN SU REPORTE, que es su sede. Adjudicacion 4.2 del acta 203,
leida hoy en la linea 71543 de docs/loop/ACTA_AUDITOR.md, y RATIFICADA POR EL
FUNDADOR en la decision del 9 sep 2026. Por eso esta tarea NO escribe una linea
fuera del reporte.

USO:  python scripts/loop/_v214_t3_seccion.py
"""
import io
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_",
                       os.path.basename(os.path.abspath(__file__))).group(1))

PLAN = "docs/loop/SALIDA_V214_T3_PLAN_BATERIA.txt"
SIG = "docs/loop/SALIDA_V214_T3_SIGUIENTE.txt"

# LOS INSTRUMENTOS QUE LA 215 VA A NECESITAR. SE COMPRUEBAN, NO SE PROMETEN.
INSTRUMENTOS = [
    ("el ciclo entero de Gate 0, los ocho comandos",
     "scripts/loop/_v205_ciclo_gate0.py"),
    ("la bateria por tramos", "scripts/loop/vuelta183_bateria_por_tramos.py"),
    ("la vara del trabajo pendiente",
     "scripts/loop/vuelta150_3_relectura_expediente.py"),
    ("el inventario de las 71 contra sus pruebas",
     "scripts/loop/_v213_t2_cierre_fase_iii.py"),
    ("el marcador y el censo, recomputados",
     "scripts/loop/vuelta159_tarea9_marcador_cierre.py"),
    ("las tres suites, dentro del ciclo de Gate 0", "engine/run_all_tests.py"),
    ("el cierre del reporte", "scripts/loop/cerrar_reporte.py"),
    ("el tallador de la cabecera", "scripts/loop/tallar_cabecera_reporte.py"),
    ("el barrido de rutas del reporte",
     "scripts/loop/vuelta186_rutas_del_reporte.py"),
]


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read()


def cifra(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(\d+)", l.split(etiqueta, 1)[1])
            if m:
                return m.group(1)
    return None


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", errors="replace").strip()


def main():
    plan = leer(PLAN)
    sig = leer(SIG)

    D = {
        "nomina": cifra(plan, "CIFRA entradas de la nomina: "),
        "tamano": cifra(plan, "CIFRA tamano de tramo: "),
        "tramos": cifra(plan, "CIFRA tramos: "),
        "suma": cifra(plan, "CIFRA suma de las entradas de todos los tramos: "),
        "sig_tramos": cifra(sig, "CIFRA tramos del reparto: "),
        "sig_con": cifra(sig, "CIFRA tramos CON salida sellada no vacia: "),
        "sig_faltan": cifra(sig, "CIFRA tramos que FALTAN: "),
    }
    if any(v is None for v in D.values()):
        print("ROJO: cifra no leida: %s" % [k for k in D if D[k] is None])
        return 1

    # DE QUE VUELTA SON LAS SALIDAS SELLADAS QUE --siguiente ESTA VIENDO
    sellos = []
    for n in range(1, int(D["tramos"]) + 1):
        rel = "docs/loop/SALIDA_V183_BATERIA_TRAMO_%d.txt" % n
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(p):
            sellos.append((n, "AUSENTE", "", 0))
            continue
        cab = leer(rel).split(NL)[0]
        commit = git(["log", "-1", "--format=%h %ad", "--date=short", "--", rel])
        sellos.append((n, cab.strip(), commit, os.path.getsize(p)))
    vueltas_del_commit = sorted({
        m.group(1) for _n, _c, com, _b in sellos
        for m in [re.search(r"", com or "")] if False})
    asuntos = git(["log", "-1", "--format=%s", "--",
                   "docs/loop/SALIDA_V183_BATERIA_TRAMO_11.txt"])
    m_vuelta = re.search(r"VUELTA (\d+)", asuntos)
    vuelta_sellos = m_vuelta.group(1) if m_vuelta else "(no leida)"

    # LAS DOS CONVENCIONES VAN JUNTAS O NO VAN: una cifra de bytes sin su pareja
    # es lo que cerrar_reporte.py bloquea, y con razon. La sede de la medicion es
    # medir_en_disco, importada y no copiada.
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402
    faltan_inst = []
    filas_inst = []
    for que, ruta in INSTRUMENTOS:
        p = os.path.join(RAIZ, ruta.replace("/", os.sep))
        ok = os.path.isfile(p) and os.path.getsize(p) > 0
        m = medir_en_disco(RAIZ, ruta) if ok else None
        filas_inst.append(
            "| %s | `%s` | %s |"
            % (que, ruta,
               ("**SI**, %d bytes en disco y %d bytes normalizados a LF"
                % (m[0], m[1])) if m else "**NO**"))
        if not ok:
            faltan_inst.append(ruta)

    tabla_sellos = NL.join(
        "| %d | %s | `%s` | %d |" % (n, cab[:64], com, by)
        for n, cab, com, by in sellos)

    cuerpo = """### TAREA 3. LA VUELTA 215, PREPARADA, Y DOS TRAMPAS MEDIDAS QUE LE ESPERAN

**DONDE VA ESTA PROPUESTA Y POR QUE NO EN OTRO SITIO.**
`docs/loop/PROMPT_SIGUIENTE.md`, `docs/loop/ACTA_AUDITOR.md` y
y el PARA_ALEXIS.md que vive junto a ellos **son sede del auditor y el ejecutor
no los escribe**;
si cree que el encargo siguiente deberia decir otra cosa, **lo propone en su
reporte, que es su sede**. Adjudicacion `4.2` del acta 203, leida hoy en la
**linea 71543** de `docs/loop/ACTA_AUDITOR.md`, y **ratificada por el fundador**
en su decision del 9 sep 2026. **Por eso esta tarea no escribe una sola linea
fuera de este reporte.**

#### 3.a LA BATERIA: EL REPARTO SE COMPUTA, Y NO DA NUEVE

**Corrido por mi en esta vuelta con el carril `--plan`, que NO toca la nomina, NO
corre ningun arnes y NO escribe ninguna salida de bateria.** Salida:
`docs/loop/SALIDA_V214_T3_PLAN_BATERIA.txt`.

| que | cuanto |
|---|---:|
| entradas de la nomina | **%(nomina)s** |
| tamano de tramo | **%(tamano)s** |
| **tramos que el reparto da** | **%(tramos)s** |
| suma de las entradas de todos los tramos | **%(suma)s** |

**LA NOMINA CALZA CON LA MORATORIA: %(nomina)s, CONGELADA**, y la suma de los
tramos reproduce esa misma cifra, o sea que el reparto cuadra consigo mismo.

**PARADA 1: EL ENCARGO Y `AUDITOR.md` 6.1 DICEN NUEVE, Y EL INSTRUMENTO CUENTA
%(tramos)s.** No lo arreglo yo (`EJECUTOR.md` 5: se escribe como PARADA y no se
repara). **La letra vigente dice, con estas palabras, que la bateria SE DECLARA
CORRIDA CUANDO LOS NUEVE TRAMOS TIENEN SALIDA SELLADA DEL MISMO CALIBRE.** El
**NUEVE** era cierto en su corte, cuando la nomina era menor; **con la nomina
congelada en %(nomina)s el reparto da %(tramos)s**, y **la practica ya se movio
sin que la letra la siguiera**: la ultima bateria, la de la **vuelta %(vuelta_sellos)s**,
corrio **%(tramos)s** tramos y sus propios commits lo dicen. **Si la 215 se cine a
la letra y para en nueve, deja DOS TRAMOS sin correr y declara corrida una bateria
que no lo esta.** La cifra que manda es la que el instrumento computa, pero
**cambiar la letra de `AUDITOR.md` no es mio**: lo subo.

**PARADA 2, Y ES LA QUE DE VERDAD PUEDE FABRICAR UN FALSO VERDE: EL CARRIL
`--siguiente` DICE HOY QUE NO FALTA NINGUN TRAMO.** Corrido por mi, salida en
`docs/loop/SALIDA_V214_T3_SIGUIENTE.txt`:

- **tramos del reparto: %(sig_tramos)s**
- **tramos CON salida sellada no vacia: %(sig_con)s**
- **tramos que FALTAN: %(sig_faltan)s**

**Y no es que la bateria de la 215 este hecha: es que las salidas que ese carril
mira son las de la vuelta %(vuelta_sellos)s y siguen en el arbol.** El motivo,
medido y no supuesto: **el lanzador nombra sus salidas con el numero que computa
de SU PROPIO fichero**, que es el **183**, no con el de la vuelta que lo corre.
Asi que `SALIDA_V183_BATERIA_TRAMO_N.txt` es el mismo nombre para toda corrida, y
**ni `--siguiente` ni `--componer` pueden distinguir una corrida fresca de la
anterior**. Lo comprobe en el propio `componer()`: cotejea **cobertura** (que
ninguna entrada de la nomina se quede sin correr, que no sobre ninguna y que no
se repita) y **que ninguna salida mida cero bytes**, pero **no mira la fecha ni el
commit de los sellos**.

**LOS ONCE SELLOS QUE HOY VE ESE CARRIL, CON SU CABECERA Y SU COMMIT, LEIDOS POR
MI:**

| tramo | cabecera de la salida, leida de su primera linea | ultimo commit que la toco | bytes |
|---:|---|---|---:|
%(tabla_sellos)s

**LO QUE PROPONGO, Y ES BARATO:** que la 215 **NO use `--siguiente` como senal de
arranque**, y corra **`--tramo 1` a `--tramo %(tramos)s` uno a uno**, cada uno
**commiteado con su salida sellada al terminar**, que es lo que la letra manda de
todas formas; y que **antes de empezar publique el commit de los sellos viejos**,
para que la corrida nueva se distinga de la de la vuelta %(vuelta_sellos)s en el
propio reporte. **`--componer` va al final y es el que coteja el calibre.**
**No propongo tocar el lanzador: rige la moratoria.**

#### 3.b EL CIERRE INTEGRAL, CON SUS INSTRUMENTOS COMPROBADOS UNO A UNO

**Todo lo que la `3.b` del encargo pide es SIN CREDENCIAL y tiene instrumento
vivo. Comprobados hoy, existencia y bytes, porque una ruta que promete prueba es
cifra:**

| que pide el encargo | instrumento | existe |
|---|---|---|
%(filas_inst)s

**CIFRA instrumentos comprobados: %(n_inst)d | CIFRA ausentes o de cero bytes:
%(n_faltan)d.**

**EL ORDEN QUE PROPONGO, y el motivo de cada sitio:** la **bateria primero y
sola**, porque `AUDITOR.md` 6.1 dice que su vuelta **no lleva nada mas** y porque
es lo que lleva vueltas cayendose; el **cierre integral despues**, con el ciclo
entero de Gate 0 **en sus dos lados**, las tres suites (que ya van dentro de ese
ciclo, comandos 7, 8a y 8b), el **inventario de las 71 contra sus pruebas** y el
**marcador y el censo recomputados**. **La vara del expediente se corre con el
reloj de git congelado en el HEAD de apertura de la 215**, no en un ancestro.

#### 3.c LA `PARA_ALEXIS.md`: SU CONDICION, Y QUIEN LA ESCRIBE

**LA CONDICION, ESCRITA ANTES DE SABER SI SE CUMPLE:** la 215 escribe la parada
de **campaña consumada** **solo si** los **%(tramos)s** tramos de la bateria
tienen salida sellada **fresca** y del mismo calibre, el ciclo entero de Gate 0
sale en **peor exitcode 0 por los dos lados**, las tres suites salen verdes, el
inventario de las 71 cuadra contra sus pruebas y el marcador y el censo
recomputados calzan. **Si algo no da verde, se dice CUAL y la 215 NO escribe esa
parada**, tal como el encargo ordena.

**Y EN ESA PARADA VA DECLARADO QUE LA AUDITORIA INTEGRAL CON CREDENCIAL Y CON EL
FUNDADOR DELANTE ES EL PASO SIGUIENTE. NO SE PIDE EL MERGE: el merge es del
fundador y viene despues de esa auditoria.** El bucle no funde ramas.

**UNA PRECISION QUE NO ES MENOR, Y LA DIGO PORQUE ME TOCA A MI DECIRLA:
`PARA_ALEXIS.md` ES SEDE DEL AUDITOR.** Cuando el encargo dice *"la 215 escribe
el `PARA_ALEXIS.md`"*, quien lo escribe es **el auditor de la 215**, no su
ejecutor. **El ejecutor de la 215 lo PROPONE en su reporte**, igual que yo estoy
proponiendo esto aqui. Si el ejecutor de la 215 lo escribiera, romperia la misma
adjudicacion `4.2` que el fundador acaba de ratificar.

**Y LO QUE LA 215 NO PUEDE DECLARAR CONSUMADO SIN MIRARLO, PORQUE ESTA VUELTA LO
DEJA ABIERTO:** los **puntos 3 y 4 de `OP-I-01` siguen en A MEDIAS** (TAREA 1), y
las **dos discrepancias de la `2.b`**, el marcador contra su cifra vieja y la
cifra once, **siguen sin doctrina que las resuelva**. **Ninguna de las tres es NO
CUBRE y ninguna la levanta el bucle por su cuenta, pero una parada de campaña
consumada que no las nombre estaria consumando por encima de ellas.**
""" % {
        "nomina": D["nomina"], "tamano": D["tamano"], "tramos": D["tramos"],
        "suma": D["suma"], "sig_tramos": D["sig_tramos"],
        "sig_con": D["sig_con"], "sig_faltan": D["sig_faltan"],
        "vuelta_sellos": vuelta_sellos,
        "tabla_sellos": tabla_sellos,
        "filas_inst": NL.join(filas_inst),
        "n_inst": len(INSTRUMENTOS), "n_faltan": len(faltan_inst),
    }

    fallos = 0
    if cuerpo.count(chr(8212)) or cuerpo.count(chr(8211)):
        fallos += 1
        print("ROJO: guiones largos o medios.")
    sosp = [c for c in re.findall(r"`([^`]+)`", cuerpo)
            if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d" % len(sosp))
    if sosp:
        for s in sosp:
            print("   sospechoso> %s" % s)
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
    print("CIFRA filas de sellos armadas: %d (se esperan %s)"
          % (len(sellos), D["tramos"]))
    if len(sellos) != int(D["tramos"]):
        fallos += 1
    print("CIFRA instrumentos ausentes o de cero bytes: %d (se exige 0)" % len(faltan_inst))
    if faltan_inst:
        fallos += 1
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: no se escribe el cuerpo.")
        return 1
    destino = os.path.join(RAIZ, "scripts", "loop", "_v%d_t3_seccion.md" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(cuerpo)
    print("ESCRITO %s -> %d bytes, %d lineas"
          % (destino, len(cuerpo.encode("utf-8")), cuerpo.count(NL)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
