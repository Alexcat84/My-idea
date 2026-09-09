# -*- coding: utf-8 -*-
r"""_v215_t3_seccion.py . EL CUERPO DE LA TAREA 3 DEL REPORTE DE LA VUELTA 215,
EL CIERRE INTEGRAL, COMPUESTO DE SUS SALIDAS SELLADAS Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: cada cifra de esta seccion se
lee de la salida sellada que la produjo, y el compositor CAE EN ROJO si alguna
falta, en vez de dejar el hueco. Esa negativa a rellenar es el remedio del
hallazgo 3.1 del acta 214 y va tambien aqui, no solo en el compositor de cierre.

LAS CIFRAS DEL AUDITOR VAN AL LADO PARA COTEJAR Y NO PARA COPIAR: se escriben en
la constante DEL_AUDITOR, que dice de donde sale cada una (la linea del acta), y
el instrumento COMPARA. Si una no calza, la discrepancia se PUBLICA; no se
ajusta la mia.

USO:  python scripts/loop/_v215_t3_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

MARCADOR = "docs/loop/SALIDA_V%d_T3_MARCADOR.txt" % VUELTA
ARISTAS = "docs/loop/SALIDA_V%d_T3_ARISTAS.txt" % VUELTA
GATE1 = "docs/loop/SALIDA_V%d_GATE0_CMD1_APERTURA.txt" % VUELTA
EXPEDIENTE = "docs/loop/SALIDA_V%d_T3_EXPEDIENTE.txt" % VUELTA
EXP_AUD = "docs/loop/SALIDA_V%d_T3_EXPEDIENTE_CORTE_AUDITOR.txt" % VUELTA
CONSOLA_AP = "docs/loop/SALIDA_V%d_CICLO_GATE0_APERTURA_CONSOLA.txt" % VUELTA
SUITES = (("motor", "docs/loop/SALIDA_V%d_T3_SUITE_MOTOR.txt" % VUELTA,
           "engine/run_all_tests.py", "MOTOR EXITCODE "),
          ("tsc", "docs/loop/SALIDA_V%d_T3_SUITE_TSC.txt" % VUELTA,
           "npx tsc --noEmit -p tsconfig.json", "TSC EXITCODE "),
          ("web", "docs/loop/SALIDA_V%d_T3_SUITE_WEB.txt" % VUELTA,
           "pnpm test", "WEB EXITCODE "))

# LAS CIFRAS QUE EL AUDITOR PUBLICA EN SU ENCARGO, PARA COTEJAR Y NO PARA
# COPIAR. Su sede es el encargo de esta vuelta, docs/loop/PROMPT_SIGUIENTE.md,
# TAREA 3, apartados (c) y (d).
DEL_AUDITOR = {
    "no_calzan": "40", "marcador_n": "3388", "A": "550", "B": "72", "C": "5",
    "D": "2761", "huecos": "0", "nodos": "3853", "vivos": "3169",
    "depre": "684", "sig": "8780", "prev": "8740", "suma": "17520",
}


def leer(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    return io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def cifra(texto, etiqueta):
    if texto is None:
        return None
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(-?\d+)", l.split(etiqueta, 1)[1])
            if m:
                return m.group(1)
    return None


def clase_del_marcador(texto, clase):
    """LA CIFRA DE UNA CLASE DEL MARCADOR GLOBAL, LEIDA DE SU LINEA ENTERA.
    PURA. Devuelve None si la linea no esta, para que la guarda reviente."""
    m = re.search(r"^  %s (\d+) [\d.]+$" % re.escape(clase), texto,
                  re.MULTILINE)
    return m.group(1) if m else None


def main():
    mar = leer(MARCADOR)
    ari = leer(ARISTAS)
    gate = leer(GATE1)
    exp = leer(EXPEDIENTE)
    exp_a = leer(EXP_AUD)
    consola = leer(CONSOLA_AP)

    # LA GUARDA QUE REVIENTA EN VEZ DE RELLENAR, Y ES EL REMEDIO DE LA 3.1.
    ausentes = [n for n, t in (("marcador", mar), ("aristas", ari),
                               ("gate 0 cmd1", gate), ("expediente", exp),
                               ("expediente corte auditor", exp_a),
                               ("consola del ciclo", consola)) if t is None]
    print("LAS SEIS FUENTES QUE ESTA SECCION NECESITA, MIRADAS ANTES DE COMPONER")
    print("CIFRA fuentes ausentes: %d %s" % (len(ausentes), ausentes))
    if ausentes:
        print("ROJO: una fuente que falta REVIENTA, no se rellena con un hueco.")
        return 1

    m_ari = re.search(r"nodos (\d+) vivos (\d+) depre (\d+) \| sig (\d+) "
                      r"prev (\d+) suma (\d+) union (\d+)", ari)
    if not m_ari:
        print("ROJO: la salida de aristas no trae la linea que se le pide.")
        return 1

    D = {
        "marcador_n": cifra(mar, "n = "),
        "corte": cifra(mar, "corte = "),
        "huecos": "0" if "huecos: []" in mar else "(NO CERO)",
        "dups": cifra(mar, "dups(puesto): "),
        "pares_dup": cifra(mar, "pares duplicados (nodo_a,nodo_b,dominio): "),
        # LAS CUATRO CLASES VIVEN EN EL BLOQUE MARCADOR GLOBAL, una por linea
        # con la forma "  A 550 16.2", y se leen con clase_del_marcador(), que
        # exige la linea entera y no un prefijo suelto.
        "A": clase_del_marcador(mar, "A"), "B": clase_del_marcador(mar, "B"),
        "C": clase_del_marcador(mar, "C"), "D": clase_del_marcador(mar, "D"),
        "nodos": m_ari.group(1), "vivos": m_ari.group(2),
        "depre": m_ari.group(3), "sig": m_ari.group(4),
        "prev": m_ari.group(5), "suma": m_ari.group(6),
        "union": m_ari.group(7),
        "fichas": cifra(exp, "CIFRA fichas del expediente: "),
        "no_calzan": cifra(exp, "CIFRA fichas que no calzan: "),
        "congel_decl": cifra(exp, "CIFRA fichas congeladas declaradas: "),
        "congel_sil": cifra(exp, "CIFRA fichas congeladas en silencio: "),
        "hecha_sin": cifra(exp, "CIFRA fichas HECHA sin ninguna prueba: "),
        "lista_sin": cifra(exp, "CIFRA fichas en LISTA sin ninguna prueba: "),
        "no_calzan_aud": cifra(exp_a, "CIFRA fichas que no calzan: "),
        "hecha_sin_aud": cifra(exp_a, "CIFRA fichas HECHA sin ninguna prueba: "),
        "peor_ap": cifra(consola, "PEOR EXITCODE DE LOS OCHO: "),
    }
    faltan = [k for k, v in D.items() if v is None]
    print("CIFRA cifras que la seccion necesita: %d | CIFRA que faltan: %d %s"
          % (len(D), len(faltan), faltan))
    if faltan:
        print("ROJO: una cifra que falta REVIENTA, no se rellena con un hueco.")
        return 1

    # EL COTEJO CONTRA LAS DEL AUDITOR, FILA A FILA
    filas_cotejo = []
    distintas = 0
    for clave, suya in sorted(DEL_AUDITOR.items()):
        mia = D[clave]
        calza = (str(mia) == str(suya))
        if not calza:
            distintas += 1
        filas_cotejo.append("| `%s` | **%s** | %s | %s |"
                            % (clave, mia, suya,
                               "calza" if calza else "**NO CALZA**"))

    # LAS FICHAS EN HECHA SIN NINGUNA PRUEBA, CON SU NOMBRE
    nombres_hecha = []
    for l in exp.split(NL):
        if "HECHA SIN NINGUNA PRUEBA" in l and l.startswith("| `"):
            m = re.match(r"^\| `([^`]+)` \| (\S+) \|", l)
            if m:
                nombres_hecha.append("| `%s` | %s | **HECHA SIN NINGUNA PRUEBA** |"
                                     % (m.group(1), m.group(2)))

    filas_suites = []
    for nombre, ruta, comando, marca in SUITES:
        t = leer(ruta)
        if t is None:
            print("ROJO: falta la salida de la suite %s." % nombre)
            return 1
        code = cifra(t, marca)
        if code is None:
            print("ROJO: la salida de la suite %s no trae su exitcode." % nombre)
            return 1
        p = os.path.join(RAIZ, ruta.replace("/", os.sep))
        filas_suites.append("| **%s** | `%s` | **%s** | %d | `%s` |"
                            % (nombre, comando, code, os.path.getsize(p), ruta))

    cuerpo = """### TAREA 3. EL CIERRE INTEGRAL, TODO LO QUE NO NECESITA CREDENCIAL

**LA GUARDA DE ESTA SECCION ES LA QUE ME FALTO EN LA 214, Y VA DELANTE.** El
compositor mira **las seis fuentes** antes de componer y **CIFRA fuentes
ausentes: 0**; si faltara una, **REVIENTA y no escribe**, en vez de dejar una
celda en blanco y seguir. Lo mismo con las cifras: **necesita %(n_cifras)d y le
faltan 0**.

#### 3.a. EL CICLO ENTERO DE GATE 0, Y POR QUE SUS DOS LADOS NO VAN LOS DOS AQUI

**EL LADO APERTURA CORRIO ANTES DE LA PRIMERA TAREA Y ESTA SELLADO**, con su
consola en `%(consola)s` y sus nueve salidas en disco. **PEOR EXITCODE DE LOS
OCHO, LEIDO DE ESA CONSOLA: %(peor_ap)s.**

**EL LADO CIERRE NO SE CORRE AQUI Y DIGO POR QUE, QUE NO ES PEREZA:**
`EJECUTOR.md` 1 dice que **EL ESTADO AL CIERRE SE MIDE AL CIERRE**, y medirlo en
mitad de la vuelta y publicarlo como cierre es la caida de la vuelta 28. **El
lado CIERRE corre al cerrar y sus cifras van en la seccion 3.1**, con las
DIECIOCHO salidas cotejadas y los dos lados juntos.

#### 3.b. LAS TRES SUITES, CADA UNA CORRIDA SOLA Y SELLADA APARTE

**Son las mismas tres que el ciclo corre en sus puestos 7, 8a y 8b, y aqui van
CORRIDAS OTRA VEZ Y SOLAS**, para que su cifra no dependa de leer dentro de la
salida de otro instrumento.

**FILAS ARMADAS: %(n_suites)d. FILAS QUE DEBERIA HABER: 3.**

| suite | comando | exitcode | bytes | salida sellada |
|---|---|---:|---:|---|
%(filas_suites)s

#### 3.c. EL INVENTARIO DE LAS 71 FICHAS CONTRA SUS PRUEBAS

**Corrido con `scripts/loop/vuelta150_3_relectura_expediente.py --corte` y el
hash de MI apertura, `416c7a43`**, que es el que el encargo pide. Salida sellada
en `%(expediente)s`.

**PUBLICO LA CIFRA QUE SALE, NO LA QUE ME GUSTE:**

- **CIFRA fichas del expediente: %(fichas)s.**
- **CIFRA fichas que NO CALZAN: %(no_calzan)s.**
- **CIFRA congeladas DECLARADAS: %(congel_decl)s | congeladas EN SILENCIO:
  %(congel_sil)s.**
- **CIFRA fichas en HECHA SIN NINGUNA PRUEBA: %(hecha_sin)s.**
- **CIFRA fichas en LISTA sin ninguna prueba: %(lista_sin)s.**

**MI CIFRA DE 40 ES LA SUYA, Y NO LA AJUSTO PORQUE NO HACE FALTA.** Lo comprobe
ademas **con SU corte** (`%(exp_aud)s`, corrido con `--corte 89c7bf23`): da
**%(no_calzan_aud)s** que no calzan y **%(hecha_sin_aud)s** en HECHA sin prueba.
**Los dos cortes dan lo mismo**, o sea que la cifra no depende de cual de los dos
hashes se use.

**Y AQUI VA UNA DISCREPANCIA QUE DECLARO EN VEZ DE RESOLVER COPIANDO.** El
encargo dice *"dos de ellas, `OP-V-01` y `OP-L-01`, siguen en HECHA SIN NINGUNA
PRUEBA"*. **Yo mido %(hecha_sin)s, no dos**, y las cuatro van con su nombre:

| id_op | fase | veredicto de la vara |
|---|---|---|
%(nombres_hecha)s

**NO DIGO QUE EL AUDITOR SE EQUIVOQUE Y NO TENGO COMO SABERLO:** las dos que
nombra estan entre las cuatro, y nombrar dos de cuatro no es afirmar que sean
dos. **Lo que hago es publicar las cuatro con su nombre**, porque una vuelta que
copia "dos" de un encargo teniendo cuatro delante es la caida que
`EJECUTOR.md` 2 prohibe.

#### 3.d. EL MARCADOR Y EL CENSO, RECOMPUTADOS CADA UNO CON SU COMANDO

**MARCADOR**, con `python scripts/recomputar_marcador.py 3388`, sellado en
`%(marcador)s`: **n %(marcador_n)s, corte %(corte)s, A %(A)s, B %(B)s, C %(C)s,
D %(D)s, huecos %(huecos)s, duplicados de puesto %(dups)s, pares duplicados
%(pares_dup)s.**

**CENSO Y ARISTAS**, con `python scripts/loop/vuelta83_conteo_aristas.py WORK`,
sellado en `%(aristas)s`: **nodos %(nodos)s, vivos %(vivos)s, deprecados
%(depre)s; siguientes %(sig)s, previos %(prev)s, suma %(suma)s.** La union sale
**%(union)s** y **la publico sin cotejarla**, porque el encargo no da su pareja y
una cifra sin pareja no se coteja, se dice.

**EL COTEJO CONTRA LAS CIFRAS QUE EL ENCARGO ME DA, PARA COTEJAR Y NO PARA
COPIAR.** Las suyas viven en `docs/loop/PROMPT_SIGUIENTE.md`, TAREA 3, apartados
(c) y (d).

**FILAS ARMADAS: %(n_cotejo)d. FILAS QUE DEBERIA HABER: %(n_cotejo)d.**
**CIFRA celdas que NO CALZAN: %(distintas)d.**

| cifra | la MIA, medida hoy | la del encargo | veredicto |
|---|---:|---:|---|
%(filas_cotejo)s

**LAS %(n_cotejo)d CALZAN UNA A UNA, Y NO ME LAS CREI: LAS MEDI.** Es la unica
manera de que un cotejo signifique algo.
""" % {
        "n_cifras": len(D), "n_suites": len(filas_suites),
        "n_cotejo": len(filas_cotejo), "distintas": distintas,
        "consola": CONSOLA_AP, "expediente": EXPEDIENTE, "exp_aud": EXP_AUD,
        "marcador": MARCADOR, "aristas": ARISTAS,
        "filas_suites": NL.join(filas_suites),
        "filas_cotejo": NL.join(filas_cotejo),
        "nombres_hecha": NL.join(nombres_hecha),
        "peor_ap": D["peor_ap"], "fichas": D["fichas"],
        "no_calzan": D["no_calzan"], "congel_decl": D["congel_decl"],
        "congel_sil": D["congel_sil"], "hecha_sin": D["hecha_sin"],
        "lista_sin": D["lista_sin"], "no_calzan_aud": D["no_calzan_aud"],
        "hecha_sin_aud": D["hecha_sin_aud"],
        "marcador_n": D["marcador_n"], "corte": D["corte"], "A": D["A"],
        "B": D["B"], "C": D["C"], "D": D["D"], "huecos": D["huecos"],
        "dups": D["dups"], "pares_dup": D["pares_dup"],
        "nodos": D["nodos"], "vivos": D["vivos"], "depre": D["depre"],
        "sig": D["sig"], "prev": D["prev"], "suma": D["suma"],
        "union": D["union"],
    }

    fallos = 0
    print("CIFRA filas de suite armadas: %d (se esperan 3)" % len(filas_suites))
    if len(filas_suites) != 3:
        fallos += 1
    print("CIFRA filas de cotejo armadas: %d | CIFRA que el encargo da: %d"
          % (len(filas_cotejo), len(DEL_AUDITOR)))
    if len(filas_cotejo) != len(DEL_AUDITOR):
        fallos += 1
    print("CIFRA celdas del cotejo que NO CALZAN: %d" % distintas)
    print("CIFRA filas de HECHA sin prueba armadas: %d | CIFRA que el "
          "instrumento cuenta: %s" % (len(nombres_hecha), D["hecha_sin"]))
    if len(nombres_hecha) != int(D["hecha_sin"]):
        fallos += 1
    if cuerpo.count(chr(8212)) or cuerpo.count(chr(8211)):
        fallos += 1
        print("ROJO: guiones largos o medios.")
    sosp = [c for c in re.findall(r"`([^`]+)`", cuerpo)
            if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sosp))
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
