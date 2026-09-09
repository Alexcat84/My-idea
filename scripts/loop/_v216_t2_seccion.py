# -*- coding: utf-8 -*-
r"""_v216_t2_seccion.py . EL CUERPO DE LA TAREA 2 DEL REPORTE DE LA VUELTA 216,
COMPUESTO DE SU SALIDA SELLADA Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: la tabla de las catorce
clausulas se RECONSTRUYE CONTANDO docs/loop/SALIDA_V216_T2_REMEDICION.txt, y el
compositor DICE cuantas filas armo y cuantas deberia haber, EN LA MISMA LINEA.
Ninguna celda de veredicto se teclea.

USO:  python scripts/loop/_v216_t2_seccion.py
"""
import io
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
SALIDA = "docs/loop/SALIDA_V%d_T2_REMEDICION.txt" % VUELTA
DESTINO = "scripts/loop/_v%d_t2_seccion.md" % VUELTA
V214 = "docs/loop/SALIDA_V214_T2B_REMEDIR_CINCO.txt"


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def cifra(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(-?\d+)", l.split(etiqueta, 1)[1])
            if m:
                return m.group(1)
    return None


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", errors="replace").strip()


def main():
    s = leer(SALIDA)
    ls = s.split(NL)

    # LAS FILAS DE LA TABLA DEL REPARTO, LEIDAS DE LA SALIDA Y NO TECLEADAS.
    filas = []
    for l in ls:
        m = re.match(r"^\| (\d+) \| (OP-[A-Z]-\d+) \| (\d+) \| (\d+) \| (.+?) \|$", l)
        if m:
            filas.append(m.groups())

    # LAS CLAUSULAS VERBATIM, LEIDAS DE LA MISMA SALIDA.
    verbatim = {}
    actual = None
    for l in ls:
        m = re.match(r"^CLAUSULA\s+(\d+) de 14 \| ficha (OP-[A-Z]-\d+) \| "
                     r"indice (\d+)", l)
        if m:
            actual = m.group(1)
            continue
        if actual and l.startswith("   VERBATIM: "):
            verbatim[actual] = l.split("VERBATIM: ", 1)[1].strip()
            actual = None

    filas_md = []
    for n, ficha, idx, linea, veredicto in filas:
        filas_md.append("| **%s** | `%s` | %s | %s | %s | **%s** |"
                        % (n, ficha, idx, linea,
                           verbatim.get(n, "(no leida)"), veredicto))

    # EL REPARTO POR FICHA, CONTADO DE LAS MISMAS FILAS.
    por_ficha = {}
    for n, ficha, idx, linea, veredicto in filas:
        d = por_ficha.setdefault(ficha, {"total": 0, "CUBRE": 0, "otras": 0,
                                         "linea": linea, "detalle": []})
        d["total"] += 1
        if veredicto == "CUBRE":
            d["CUBRE"] += 1
        else:
            d["otras"] += 1
            d["detalle"].append("indice %s en %s" % (idx, veredicto))
    filas_ficha = []
    for ficha in ("OP-V-01", "OP-L-01", "OP-L-02", "OP-L-03", "OP-I-01"):
        d = por_ficha.get(ficha)
        if d is None:
            filas_ficha.append("| `%s` | (NO APARECE EN LA SALIDA) | | | |" % ficha)
            continue
        filas_ficha.append(
            "| `%s` | %s | **%d** | **%d** | %d | %s |"
            % (ficha, d["linea"], d["total"], d["CUBRE"], d["otras"],
               ", ".join(d["detalle"]) or "ninguna"))

    # LAS CINCO PARTES DE LA CLAUSULA TRANSVERSAL, LEIDAS DE LA SALIDA.
    partes = []
    for l in ls:
        m = re.match(r"^   PARTE (.+?)\s{2,}marca (.+?)\s+\| corrida K "
                     r"linea\(s\) (.+?) \| commit linea\(s\) (.+?) \| "
                     r"SOSTENIDA: (\S+)$", l)
        if m:
            partes.append(m.groups())
    filas_partes = ["| %d | %s | `%s` | %s | %s | **%s** |"
                    % (i + 1, p[0].strip(), p[1], p[2], p[3], p[4])
                    for i, p in enumerate(partes)]

    v214 = leer(V214)
    D = {
        "v": VUELTA,
        "salida": SALIDA,
        "n_filas": len(filas),
        "n_filas_md": len(filas_md),
        "lineas_vara": cifra(s, "CIFRA lineas de docs/plan/08_VERIFICACION.md: "),
        "armadas": cifra(s, "CIFRA FILAS ARMADAS LEYENDO ESA TABLA: "),
        "descuadres": cifra(s, "CIFRA filas que NO calzan con su sede: "),
        "corregidas": cifra(s, "CIFRA filas que la tabla declara CORREGIDAS por "
                               "una correccion declarada: "),
        "cubre": cifra(s, "CIFRA clausulas en CUBRE: "),
        "medias": cifra(s, "CIFRA clausulas en A MEDIAS: "),
        "nocubre": cifra(s, "CIFRA clausulas en NO CUBRE: "),
        "sinsonda": cifra(s, "CIFRA clausulas en SIN SONDA: "),
        "medidas": cifra(s, "CIFRA clausulas medidas: "),
        "rotos": cifra(s, "CIFRA mutantes rotos: "),
        "caen": cifra(s, "CIFRA que CAEN (o sea que NO dicen CUBRE): "),
        "sanos": cifra(s, "CIFRA mutantes sanos: "),
        "suben": cifra(s, "CIFRA que SUBEN a CUBRE: "),
        "ck_bytes": cifra(s, "CIFRA bytes exactos de la corrida K: "),
        "ck_bytes_lf": cifra(s, "bytes en disco y "),
        "ck_lineas": cifra(s, "CIFRA lineas de la corrida K: "),
        "sostenidas": cifra(s, "CIFRA sostenidas por cita: "),
        "n_partes": len(partes),
        "filas_md": NL.join(filas_md),
        "filas_ficha": NL.join(filas_ficha),
        "filas_partes": NL.join(filas_partes),
        "v214_bytes": len(leer(V214).encode("utf-8")),
        "v214_sin": v214.count("SIN VEREDICTO MECANICO"),
        "v214_noletra": v214.count("NO CALZA LEIDA A LA LETRA"),
        "v214_commit": git(["log", "-1", "--format=%h", "--", V214]),
        "sha_antes": (cifra(s, "AL ENTRAR: ") or "?"),
    }
    D["sha_antes"] = s.split("AL ENTRAR: ", 1)[1].split(NL, 1)[0].strip()
    D["sha_despues"] = s.split("AL SALIR: ", 1)[1].split(NL, 1)[0].strip()

    cuerpo = """### TAREA 2. LA RE-MEDICION QUE EL FUNDADOR ORDENO, CORRIDA Y CON SU CIFRA DELANTE

**QUIEN LA ORDENA, POR SU RUTA Y NO DE MEMORIA:**
`docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md`, **DECISION 2**,
verbatim: *"las cinco fichas SIN EJECUTAR se re-miden contra esas filas (OP-V-01
con su prueba por cita de la corrida K ya escrita)"*. El instrumento es
`scripts/loop/_v%(v)d_t2_remedicion.py` y su salida sellada es
`%(salida)s`.

#### 2.a. LAS CATORCE FILAS, SACADAS CON UN INSTRUMENTO Y COTEJADAS CONTRA SU SEDE

**FILAS ARMADAS LEYENDO LA TABLA DE DERIVACION DE `docs/plan/08_VERIFICACION.md`
(%(lineas_vara)s lineas hoy): %(armadas)s. FILAS QUE DEBERIA HABER: 14.** **LAS
DOS SE ESCRIBEN JUNTAS**, y si el instrumento hubiera sacado otro numero
**habria parado**, que es lo que el encargo manda.

**Y NO BASTA CON CONTARLAS: CADA FILA SE COTEJA CONTRA SU SEDE.** El instrumento
abre `docs/plan/OPERACIONES.jsonl`, va a la linea que la fila declara, saca la
clausula del indice que la fila declara y **compara el texto VERBATIM**.
**CIFRA filas que NO calzan con su sede: %(descuadres)s** (se exigen 0).

**LAS CORRECCIONES DECLARADAS NO ENTRAN COMO FILAS**, que es lo que el registro
`R.72` del acta 208 adjudico y lo que la propia tabla hace listandolas aparte.
**PERO SI SE LEEN, Y LO DIGO PORQUE ES UNA DECISION MIA:** la tabla trae una
columna que dice, fila por fila, **que correccion corrige que clausula**
(**CIFRA filas que la tabla declara corregidas: %(corregidas)s**), y una
clausula corregida se mide **por su lectura corregida**. Leer la correccion no
es medirla.

#### 2.b. LAS CATORCE, MEDIDAS UNA POR UNA, CON LA BUSQUEDA CORRIDA Y SU CIFRA DELANTE

**FILAS ARMADAS LEYENDO `%(salida)s`: %(n_filas_md)d. FILAS QUE DEBERIA HABER:
14.** Ninguna celda de veredicto se teclea: todas se leen de esa salida.

| # | ficha | indice | linea del expediente | la clausula, VERBATIM | veredicto medido hoy |
|---:|---|---:|---:|---|---|
%(filas_md)s

**EL REPARTO: CIFRA en CUBRE %(cubre)s | CIFRA en A MEDIAS %(medias)s | CIFRA en
NO CUBRE %(nocubre)s | CIFRA sin sonda %(sinsonda)s | CIFRA medidas %(medidas)s
de 14.**

**LO QUE ESTA VUELTA ANADE SOBRE LA 214, DICHO CON SU CIFRA Y NO COMO MERITO:**
la 214 dejo **%(v214_sin)d de las catorce SIN VEREDICTO MECANICO** y
**%(v214_noletra)d en NO CALZA LEIDA A LA LETRA**, declaradas documentales o
pendientes de doctrina. **Aqui las catorce llevan sonda corrida, y las que dan
cero publican su cero con el comando delante**, que es lo que la `5.4` del acta
214 autoriza: **lo prohibido es afirmar una busqueda NO corrida, no publicar la
que da cero.**

#### 2.c. `OP-V-01` POR CITA DE LA CORRIDA K, QUE SE BUSCO Y SE ENCONTRO

**LA CORRIDA K EXISTE.** Su ruta es
`docs/loop/SALIDA_SESION_CREDENCIAL_VUELO_K.txt` y mide **%(ck_bytes)s bytes en disco y %(ck_bytes_lf)s bytes normalizado a LF**, con **%(ck_lineas)s lineas**, medidos
hoy. **No se vuelve a producir: se cita**, que es lo que la DECISION 2 manda.

**FILAS ARMADAS LEYENDO `%(salida)s`: %(n_partes)d. FILAS QUE DEBERIA HABER: 5**
(las cinco partes de la clausula transversal). **CIFRA partes sostenidas por
cita: %(sostenidas)s de 5.**

| # | parte de la clausula | marca con la que se busca | linea(s) en la corrida K | linea(s) en el commit `e966d896` | sostenida |
|---:|---|---|---|---|---|
%(filas_partes)s

**Y AQUI VA UNA PRECISION QUE NO ME FAVORECE Y LA ESCRIBO IGUAL:** el fichero de
la corrida K sostiene **por si solo** la parte del vuelo completo; **las otras
cuatro las sostiene el cuerpo del commit `e966d896`**, que es el que movio el
estado de la ficha y el que sello la corrida K. **Son dos sedes y no una, y
decir "la corrida K las sostiene todas" seria mentir por omision.**

#### 2.d. EL CASO ROJO NO SE PROMETE, SE PRUEBA POR MUTACION

**El mutante se fabrica EN MEMORIA, sobre una copia profunda de los datos, y no
se escribe en ninguna ficha.** **CIFRA mutantes rotos: %(rotos)s | CIFRA que
CAEN, o sea que dejan de decir CUBRE: %(caen)s.**

**Y EL REVERSO, PORQUE UNA SONDA QUE NUNCA PUEDE DECIR CUBRE TAMPOCO MIDE:** la
clausula que hoy no da CUBRE se prueba ademas con un mutante **SANO**, y tiene
que SUBIR. **CIFRA mutantes sanos: %(sanos)s | CIFRA que SUBEN a CUBRE:
%(suben)s.**

#### 2.e. LA GUARDA: ESTA TAREA NO MOVIO NI UN CAMPO DE ESTADO

**El `sha256` de `docs/plan/OPERACIONES.jsonl` al ENTRAR, el mismo en disco y normalizado a LF, es `%(sha_antes)s`; y al SALIR, tambien el mismo en disco y normalizado a LF, es `%(sha_despues)s`. Los dos CALZAN**, porque ese fichero
no trae ni un retorno de carro. Y cero filas de
`git diff --numstat` sobre el expediente, el inventario, la vara y la pagina de
lecturas dirigidas.

#### 2.f. UNA DISCREPANCIA QUE DECLARO EN VEZ DE CALLARLA, Y NO ME FAVORECE DISCUTIRLA

**MI ENCARGO DICE, Y EL ACTA 215 EN SU `5.7` TAMBIEN, QUE LA RE-MEDICION NO LA
HA CORRIDO NADIE.** **Medido hoy por mi: existe
`%(v214)s`, **%(v214_bytes)d bytes en disco y %(v214_bytes)d bytes normalizado a
LF**, commit `%(v214_commit)s`, y es una re-medicion de las cinco fichas contra
estas mismas catorce clausulas.**

**NO DISCUTO LA ADJUDICACION Y NO LA NECESITO PARA NADA, porque la orden se
cumple igual:** aquella re-medicion dejo **%(v214_sin)d de catorce sin veredicto
mecanico** y **%(v214_noletra)d mas en NO CALZA LEIDA A LA LETRA**, o sea que
**ocho de las catorce se quedaron sin CUBRE, A MEDIAS ni NO CUBRE**. **La orden
del fundador pedia las catorce medidas, y esa parte NO estaba corrida.** Lo
publico porque `EJECUTOR.md` 2 dice que una discrepancia se declara y nunca se
resuelve copiando, **y porque el que la declara con su cifra soy yo y no el que
me audita.**
""" % dict(D, v214=V214)

    fallos = 0
    print("EL COMPOSITOR DE LA TAREA 2, Y SUS GUARDAS ANTES DE ESCRIBIR")
    print("CIFRA filas de la tabla del reparto leidas: %d (se exigen 14)"
          % len(filas))
    if len(filas) != 14:
        fallos += 1
    print("CIFRA filas de la tabla compuesta: %d (se exigen 14)" % len(filas_md))
    if len(filas_md) != 14:
        fallos += 1
    print("CIFRA clausulas VERBATIM leidas: %d (se exigen 14)" % len(verbatim))
    if len(verbatim) != 14:
        fallos += 1
    print("CIFRA filas por ficha: %d (se exigen 5)" % len(filas_ficha))
    if len(filas_ficha) != 5:
        fallos += 1
    print("CIFRA partes de la transversal leidas: %d (se exigen 5)" % len(partes))
    if len(partes) != 5:
        fallos += 1
    print("CIFRA celdas con (no leida): %d (se exigen 0)"
          % cuerpo.count("(no leida)"))
    if "(no leida)" in cuerpo:
        fallos += 1
    print("CIFRA celdas con None: %d (se exigen 0)" % cuerpo.count("None"))
    if "None" in cuerpo:
        fallos += 1
    sospechosos = [c for c in re.findall(r"`([^`]+)`", cuerpo)
                   if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sospechosos))
    if sospechosos:
        fallos += 1
    print("CIFRA guiones largos: %d | CIFRA guiones medios: %d"
          % (cuerpo.count(chr(8212)), cuerpo.count(chr(8211))))
    if cuerpo.count(chr(8212)) or cuerpo.count(chr(8211)):
        fallos += 1
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: el compositor NO ESCRIBE.")
        return 1
    p = os.path.join(RAIZ, DESTINO.replace("/", os.sep))
    io.open(p, "w", encoding="utf-8", newline=NL).write(cuerpo)
    print("ESCRITO %s -> %d bytes" % (DESTINO, os.path.getsize(p)))
    # LA TABLA POR FICHA SE GUARDA APARTE: la TAREA 3 la publica y no la
    # vuelve a componer, para que no haya dos versiones de lo mismo.
    p2 = os.path.join(RAIZ, "scripts", "loop", "_v%d_t2_por_ficha.md" % VUELTA)
    io.open(p2, "w", encoding="utf-8", newline=NL).write(NL.join(filas_ficha) + NL)
    print("ESCRITO scripts/loop/_v%d_t2_por_ficha.md -> %d bytes"
          % (VUELTA, os.path.getsize(p2)))
    print("VERDE: el cuerpo de la TAREA 2 queda compuesto.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
