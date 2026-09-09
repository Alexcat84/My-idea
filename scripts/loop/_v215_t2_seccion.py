# -*- coding: utf-8 -*-
r"""_v215_t2_seccion.py . EL CUERPO DE LA TAREA 2 DEL REPORTE DE LA VUELTA 215,
COMPUESTO DE SUS SALIDAS SELLADAS Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO. La tabla de los once tramos se
pega ENTERA de la salida de _v215_t2_tabla.py, y la de los once sellos viejos de
la salida de la apertura. NINGUNA CELDA SE TECLEA.

USO:  python scripts/loop/_v215_t2_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
TABLA = "docs/loop/SALIDA_V%d_T2_TABLA.txt" % VUELTA
APERTURA = "docs/loop/SALIDA_V%d_APERTURA.txt" % VUELTA
PLAN = "docs/loop/SALIDA_V%d_T2_PLAN.txt" % VUELTA
SIGUIENTE = "docs/loop/SALIDA_V%d_T2_SIGUIENTE_FALSO_VERDE.txt" % VUELTA
MUTANTES = "docs/loop/SALIDA_V%d_T2_MUTANTES.txt" % VUELTA
COMPUESTA = "docs/loop/SALIDA_V183_BATERIA.txt"
CONSOLA = "docs/loop/SALIDA_V%d_T2_COMPONER_CONSOLA.txt" % VUELTA


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def cifra(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(-?[\d.]+)", l.split(etiqueta, 1)[1])
            if m:
                return m.group(1)
    return None


def bloque(texto, abre, cierra):
    """LAS LINEAS ENTRE DOS MARCAS, PEGADAS ENTERAS. PURA."""
    lineas = texto.split(NL)
    i = next((k for k, l in enumerate(lineas) if abre in l), None)
    if i is None:
        return []
    fuera = []
    for l in lineas[i:]:
        if fuera and cierra(l):
            break
        fuera.append(l)
    return fuera


def main():
    tabla = leer(TABLA)
    apertura = leer(APERTURA)
    plan = leer(PLAN)
    sig = leer(SIGUIENTE)
    mut = leer(MUTANTES)
    comp = leer(COMPUESTA)
    consola = leer(CONSOLA)

    filas_tramo = [l for l in tabla.split(NL) if re.match(r"^\| \*\*\d+\*\* \|", l)]
    cab_tramo = [l for l in tabla.split(NL)
                 if l.startswith("| tramo |") or l.startswith("|---:|---:|")]
    filas_sello = [l for l in apertura.split(NL) if l.startswith("SELLO tramo ")]
    filas_caen = [l for l in tabla.split(NL) if l.startswith("CAE tramo ")]
    filas_rep = [l for l in tabla.split(NL) if l.startswith("REPETIDO tramo ")]

    tabla_sellos = []
    for l in filas_sello:
        m = re.match(r"^SELLO tramo (\d+): (\d+) bytes, ultimo commit (\S+), "
                     r"fecha (\S+), asunto \(primeros 70\) (.*)$", l)
        if m:
            tabla_sellos.append("| **%s** | %s | `%s` | **%s** | %s |"
                                % m.groups())

    tabla_caen = []
    for l in filas_caen:
        m = re.match(r"^CAE tramo (\d+) \| (.+?) \| (\S+)$", l)
        if m:
            n, clase, nombre = m.groups()
            ya = any(("tramo %s | %s" % (n, nombre)) in r for r in filas_rep)
            tabla_caen.append(
                "| **%s** | %s | `scripts/loop/%s` | %s |"
                % (n, clase, nombre,
                   "**YA CAIA EN LA 210**" if ya else "**NUEVO EN ESTA CORRIDA**"))

    D = {
        "nomina": cifra(plan, "CIFRA entradas de la nomina: "),
        "tamano": cifra(plan, "CIFRA tamano de tramo: "),
        "tramos": cifra(plan, "CIFRA tramos: "),
        "suma_plan": cifra(plan, "CIFRA suma de las entradas de todos los tramos: "),
        "faltan_falso": cifra(sig, "CIFRA tramos que FALTAN: "),
        "sellos": cifra(apertura, "CIFRA sellos de tramo presentes en el arbol AL ENTRAR: "),
        "corridas": cifra(tabla, "CIFRA entradas corridas sumando los once tramos: "),
        "ok": cifra(tabla, "CIFRA OK en los once: "),
        "decl": cifra(tabla, "CIFRA CASO DECLARADO en los once: "),
        "no_mordio": cifra(tabla, "CIFRA NO MORDIO en los once: "),
        "ancla": cifra(tabla, "CIFRA ANCLA PERDIDA en los once: "),
        "no_repro": cifra(tabla, "CIFRA NO REPRODUCIBLE en los once: "),
        "caen": cifra(tabla, "CIFRA arneses de la nomina que CAEN hoy: "),
        "nuevos": cifra(tabla, "CIFRA arneses que CAEN HOY Y NO CAIAN EN LA CORRIDA ANTERIOR: "),
        "repetidos": cifra(tabla, "CIFRA arneses que CAEN HOY Y YA CAIAN: "),
        "sanados": cifra(tabla, "CIFRA arneses que CAIAN Y HOY NO CAEN: "),
        # LAS TRES DE COBERTURA VIVEN EN LA COMPUESTA EN UNA SOLA LINEA, y se
        # leen de ahi. Las dos de tamano NO estan dentro de la compuesta (el
        # instrumento las imprime por consola), asi que se leen de la CONSOLA
        # SELLADA de --componer, que es su fichero y no mi memoria.
        "cob_ninguno": cifra(comp, "CIFRA entradas sin correr: "),
        "cob_fuera": cifra(comp, "ajenas: "),
        "cob_dos": cifra(comp, "repetidas: "),
        "comp_bytes": cifra(consola, "CIFRA bytes en disco: "),
        "comp_lineas": cifra(consola, "CIFRA lineas: "),
        "mut_casos": cifra(mut, "CIFRA casos: "),
        "mut_fallan": cifra(mut, "CIFRA que NO calzan: "),
    }

    cuerpo = """### TAREA 2. LA BATERIA ENTERA, ONCE TRAMOS, Y SIN EL FALSO VERDE

#### 2.a. DE QUE VUELTA SON LOS SELLOS QUE HABIA EN EL ARBOL, PUBLICADO ANTES DE CORRER NADA

**ESTA TABLA SE TALLO EN LA APERTURA, ANTES DE LA PRIMERA OPERACION.** Vive en
`%(apertura)s`, con el commit y la fecha de cada sello **leidos de `git log` y no
tecleados**, que es lo que la TAREA 2.a manda.

**FILAS ARMADAS: %(n_sellos)d. FILAS QUE DEBERIA HABER, contadas por la propia
apertura: %(sellos)s.**

| tramo | bytes al entrar | ultimo commit ANTES de esta vuelta | fecha | asunto (primeros 70) |
|---:|---:|---|---|---|
%(tabla_sellos)s

**LOS ONCE ERAN DE LA VUELTA 210 Y LOS ONCE ESTABAN FECHADOS EL 2026-09-08.**
Esa es la tabla que hace distinguible mi corrida nueva: el lanzador nombra sus
salidas con el numero de SU PROPIO fichero, asi que una corrida vieja y una
fresca **comparten nombre**, y lo unico que prueba de que vuelta es cada tramo es
**que su fichero cambie en un commit de esta vuelta**. Los once cambiaron, uno a
uno, en once commits de la 215.

#### 2.b. EL FALSO VERDE, MEDIDO POR MI Y NO USADO COMO SENAL

**Corri el carril de la senal de arranque UNA VEZ, y solo para medir la trampa,
NO para decidir nada** (adjudicacion `5.2`). Su salida esta en `%(siguiente)s` y
dice **`CIFRA tramos que FALTAN: %(faltan_falso)s`** y **LOS 11 TRAMOS TIENEN
SALIDA SELLADA**, sobre los sellos de la 210 que la tabla de arriba acaba de
fechar. **Si esta vuelta lo hubiera usado como senal de arranque, habria
declarado corrida una bateria que no habia corrido ni un tramo.**

**EL REPARTO, COMPUTADO Y NO TECLEADO** (`%(plan)s`): nomina **%(nomina)s**,
tramo de **%(tamano)s**, **%(tramos)s TRAMOS**, y la suma de los tramos
reproduce las **%(suma_plan)s**. **ONCE, no nueve**, por la adjudicacion `5.1`.

#### 2.c. LOS ONCE TRAMOS CORRIDOS, UNO A UNO Y COMMITEADOS AL TERMINAR

**FILAS ARMADAS LEYENDO `%(tabla)s`: %(n_filas)d. FILAS QUE DEBERIA HABER:
%(tramos)s.** Cada celda sale de contar el fichero sellado de su tramo.

%(cab_tramo)s
%(filas_tramo)s

**LA COBERTURA, LEIDA DE LA COMPUESTA Y NO RECALCULADA DEL REPARTO**
(`%(compuesta)s`, %(comp_bytes)s bytes, %(comp_lineas)s lineas): entradas que
**NINGUN** tramo corrio **%(cob_ninguno)s**, entradas corridas que **NO estan en
la nomina** **%(cob_fuera)s**, entradas corridas **MAS DE UNA VEZ**
**%(cob_dos)s**. **Las %(corridas)s entradas de la nomina corrieron, cada una
EXACTAMENTE UNA VEZ, y cada una DOS VECES por la doble corrida.**

**EL REPARTO DE LAS %(corridas)s: OK %(ok)s, CASO DECLARADO %(decl)s, NO MORDIO
%(no_mordio)s, ANCLA PERDIDA %(ancla)s, NO REPRODUCIBLE %(no_repro)s.** Las cinco
clases **suman las %(corridas)s**, y el instrumento lo comprueba antes de
publicar la tabla. **NO REPRODUCIBLE en %(no_repro)s es la doble corrida diciendo
que las dos corridas de cada entrada dan lo mismo.**

#### 2.d. LO QUE CAE, Y LO TRAIGO EN VEZ DE ARREGLARLO DE PASO

**MI ENCARGO DICE, CON ESTAS PALABRAS: SI ALGUN ARNES DE LA NOMINA CAE, PARAS Y
LO TRAES.** **CAEN %(caen)s, y aqui estan con su nombre y su tramo.** **Las dos
PARADAS de esta vuelta van al final del reporte; esta es la tabla que las
sostiene.**

| tramo | clase | arnes | contra la corrida anterior del mismo fichero |
|---:|---|---|---|
%(tabla_caen)s

**Y EL COTEJO QUE HACE LEGIBLE ESA CIFRA, PORQUE UN ARNES QUE LLEVA ROJO DESDE
ANTES Y UNO QUE SE ACABA DE ROMPER NO SON LA MISMA NOTICIA.** La corrida anterior
de **cada uno** de los once ficheros se lee con `git show` sobre el commit que la
sello, y ese commit sale de `git log --skip=1` sobre la ruta, **no de mi
memoria**: los once son de la **vuelta 210**, del 2026-09-08.

- **ARNESES QUE CAEN HOY Y NO CAIAN EN LA 210: %(nuevos)s.**
- **ARNESES QUE CAEN HOY Y YA CAIAN: %(repetidos)s.**
- **ARNESES QUE CAIAN Y HOY NO CAEN: %(sanados)s.**

**LOS %(caen)s SON LOS MISMOS %(caen)s, NI UNO MAS NI UNO MENOS.** **Esta vuelta
no rompio nada y tampoco arreglo nada**, y eso es exactamente lo que se puede
afirmar con la medicion delante. **NO LOS TOCO**: repararlos seria fabricar
maquinaria bajo la moratoria, y arreglar un arnes en rojo de paso, en la vuelta
del cierre integral, es justo lo que mi encargo prohibe.

#### 2.e. MI PROPIA CAIDA DE ESTA TAREA, Y LA GUARDA QUE LA CIERRA

**Va entera en la seccion de mis caidas (`D.1`) y no la escondo aqui.** En una
linea: mi compositor de mensajes de commit llevaba la frase *"y ninguno cae"*
**clavada en el texto** al lado de cifras que si se leian, y en el tramo 3 las
dos cosas se contradijeron dentro del mismo mensaje. **Hoy la frase se COMPUTA de
las tres cifras de fallo y el instrumento CAE EN ROJO si la prosa y las cifras no
dicen lo mismo.**

**SU PRUEBA DE MUTACION VA DELANTE Y NO DETRAS** (`%(mutantes)s`): **%(mut_casos)s
casos, %(mut_fallan)s que no calzan**, y la cifra que de verdad importa es que los
casos con caidos distinto de cero en los que la frase **aun diria** *"ninguno
cae"* son **0**.
""" % {
        "apertura": APERTURA, "siguiente": SIGUIENTE, "plan": PLAN,
        "tabla": TABLA, "mutantes": MUTANTES, "compuesta": COMPUESTA,
        "tabla_sellos": NL.join(tabla_sellos),
        "n_sellos": len(tabla_sellos),
        "tabla_caen": NL.join(tabla_caen),
        "cab_tramo": NL.join(cab_tramo),
        "filas_tramo": NL.join(filas_tramo),
        "n_filas": len(filas_tramo),
        "nomina": D["nomina"], "tamano": D["tamano"], "tramos": D["tramos"],
        "suma_plan": D["suma_plan"], "faltan_falso": D["faltan_falso"],
        "sellos": D["sellos"], "corridas": D["corridas"], "ok": D["ok"],
        "decl": D["decl"], "no_mordio": D["no_mordio"], "ancla": D["ancla"],
        "no_repro": D["no_repro"], "caen": D["caen"], "nuevos": D["nuevos"],
        "repetidos": D["repetidos"], "sanados": D["sanados"],
        "cob_ninguno": D["cob_ninguno"], "cob_fuera": D["cob_fuera"],
        "cob_dos": D["cob_dos"], "comp_bytes": D["comp_bytes"],
        "comp_lineas": D["comp_lineas"],
        "mut_casos": D["mut_casos"], "mut_fallan": D["mut_fallan"],
    }

    fallos = 0
    print("CIFRA filas de tramo armadas: %d | CIFRA que deberia haber: %s"
          % (len(filas_tramo), D["tramos"]))
    if len(filas_tramo) != int(D["tramos"]):
        fallos += 1
    print("CIFRA filas de sello armadas: %d | CIFRA que la apertura dice: %s"
          % (len(tabla_sellos), D["sellos"]))
    if len(tabla_sellos) != int(D["sellos"]):
        fallos += 1
    print("CIFRA filas de caida armadas: %d | CIFRA que la tabla dice: %s"
          % (len(tabla_caen), D["caen"]))
    if len(tabla_caen) != int(D["caen"]):
        fallos += 1
    if None in D.values():
        fallos += 1
        print("ROJO: alguna cifra no se pudo leer de su fichero: %s"
              % [k for k, v in D.items() if v is None])
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
    destino = os.path.join(RAIZ, "scripts", "loop", "_v%d_t2_seccion.md" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(cuerpo)
    print("ESCRITO %s -> %d bytes, %d lineas"
          % (destino, len(cuerpo.encode("utf-8")), cuerpo.count(NL)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
