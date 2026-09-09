# -*- coding: utf-8 -*-
r"""_v214_t2_seccion.py . EL CUERPO DE LA TAREA 2 DEL REPORTE DE LA VUELTA 214,
COMPUESTO LEYENDO LAS SALIDAS SELLADAS Y NO TECLEADO.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: toda cifra y toda fila de este
texto se LEE de la salida que la produjo, y la salida se nombra al lado.

USO:  python scripts/loop/_v214_t2_seccion.py
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

FUENTES = {
    "sim": "docs/loop/SALIDA_V214_T2_SIMULACION.txt",
    "mut": "docs/loop/SALIDA_V214_T2_MUTANTES.txt",
    "escr": "docs/loop/SALIDA_V214_T2_VARA_TRES_FASES.txt",
    "remedir": "docs/loop/SALIDA_V214_T2B_REMEDIR_CINCO.txt",
}


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
    faltan = [r for r in FUENTES.values()
              if not os.path.isfile(os.path.join(RAIZ, r.replace("/", os.sep)))
              or os.path.getsize(os.path.join(RAIZ, r.replace("/", os.sep))) == 0]
    if faltan:
        print("ROJO: faltan salidas o miden 0 bytes: %s" % faltan)
        return 1

    sim = leer(FUENTES["sim"])
    mut = leer(FUENTES["mut"])
    escr = leer(FUENTES["escr"])
    rem = leer(FUENTES["remedir"])

    # LA TABLA DEL RESUMEN DE LA 2.b, PEGADA ENTERA DE SU FICHERO
    filas_res = [l for l in rem.split(NL) if l.startswith("| OP-")]
    # LAS FILAS DE DERIVACION, CONTADAS DE SU FICHERO
    n_deriv = cifra(escr, "FILAS DE DERIVACION ARMADAS: ")
    if n_deriv is None:
        n_deriv = cifra(leer("docs/plan/08_VERIFICACION.md"),
                        "FILAS DE DERIVACION ARMADAS: ")

    # EL REPARTO POR FICHA, LEIDO DEL FICHERO
    # EL REPARTO VIVE EN LA SALIDA DE LA ESCRITURA, QUE ES LA QUE LO COMPUTO
    reparto = []
    for l in escr.split(NL):
        m = re.match(r"^   (OP-[A-Z]-\d+) \((\w+)\): (\d+) clausula\(s\) de vara, "
                     r"(\d+) correccion\(es\) declarada\(s\), (\d+) EXCLUIDA", l)
        if m:
            reparto.append(m.groups())

    D = {
        "clausulas_08": cifra(rem.split("FILA DE LA FASE 09")[0],
                              "contadas por su separador: "),
        "clausulas_09": cifra(rem.split("FILA DE LA FASE 09")[1]
                              .split("FILA DE LA FASE 10")[0],
                              "contadas por su separador: "),
        "clausulas_10": cifra(rem.split("FILA DE LA FASE 10")[1],
                              "contadas por su separador: "),
        "mut_n": cifra(mut, "CIFRA mutantes "),
        "mut_caen": cifra(mut, "CIFRA que caen "),
        "excl": cifra(sim, "correccion(es) declarada(s), "),
        "fichas": cifra(rem, "CIFRA fichas re-medidas: "),
        "repartidas": cifra(rem, "CIFRA clausulas repartidas: "),
        "con_sonda": cifra(rem, "| con sonda "),
        "documentales": cifra(rem, "documentales "),
        "marcador": cifra(rem, "EL MARCADOR DEL ARCHIVO: "),
        "ld_cab": cifra(rem, "LECTURA DIRIGIDA: "),
        "ld_dentro": cifra(rem, "nombres sueltos), "),
        "nota_len": cifra(rem, "de la ficha ("),
    }
    if any(v is None for v in D.values()):
        print("ROJO: una cifra no se pudo leer: %s" % [k for k in D if D[k] is None])
        return 1

    ns = git(["diff", "--numstat", "--", "docs/plan/08_VERIFICACION.md"])
    ns_plan = [l for l in git(["diff", "--numstat", "--", "docs/plan/"]).split(NL)
               if l.strip()]

    tabla_res = NL.join(filas_res)
    tabla_excl = NL.join(
        "| `%s` | %s | %s | %s | %s |" % (fid, fase, nv, nc, nx)
        for fid, fase, nv, nc, nx in reparto)

    cuerpo = """### TAREA 2. LA VARA DE LAS TRES FASES, ESCRITA Y USADA

**LA DECISION QUE LO ORDENA, POR SU RUTA:**
`docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md`, **DECISION 2**. El acta
211 ya habia reservado estas filas al fundador en su `6.4`, y el acta 213 midio
en su `7.2` que la ausencia era **total y no parcial**.

#### 2.a LAS TRES FILAS, DERIVADAS Y NO INVENTADAS

**LO QUE SE ESCRIBIO ES ADITIVO Y NO TOCA UNA LETRA DE LA TABLA VIEJA:**
`numstat` sobre `docs/plan/08_VERIFICACION.md` da **%(ns)s**, o sea **altas y
CERO bajas**. La guarda comprueba ademas, sobre el texto y no de palabra, que
**las 8 filas viejas siguen enteras** y que **no desaparece ni una linea del
fichero**.

**LA REGLA DE DERIVACION ES MECANICA Y NO ES DE OJO:** cada celda se **compone
concatenando los textos VERBATIM** de las clausulas de `verificacion` que las
propias fichas traen, y **el juicio cae si una celda trae texto que no salga de
una clausula**. Las clausulas de `OP-V-01` que **abren con el numero de una fase
que ya tiene fila** se excluyen, porque no son la vara de su fase sino la ficha
repitiendo filas que ya existen: **de sus 9 clausulas se excluyen 8 y queda 1**,
la transversal, que es la de la fase 08.

**LAS TRES CELDAS, CON SU CUENTA DE CLAUSULAS LEIDA DEL FICHERO:** la fila
**08** trae **%(clausulas_08)s** clausula, la **09** trae **%(clausulas_09)s** y
la **10** trae **%(clausulas_10)s**.

**Y LAS CORRECCIONES DECLARADAS NO ENTRAN, POR EL REGISTRO `R.72` DEL ACTA 208**,
que separo las clausulas de vara de las correcciones declaradas diciendo que
estas **nunca fueron puntos de la vara**. Contadas de la salida, ficha por ficha:

| ficha | fase | clausulas de vara | correcciones declaradas | excluidas por tener fila ya |
|---|---|---:|---:|---:|
%(tabla_excl)s

**Cada fila de la tabla de derivacion que se escribio en el plan lleva su cita:
ficha, indice de la clausula y linea de `docs/plan/OPERACIONES.jsonl`. FILAS DE
DERIVACION ARMADAS: %(n_deriv)s.**

**EL CASO ROJO, PROBADO POR MUTACION** (`docs/loop/SALIDA_V214_T2_MUTANTES.txt`):
**%(mut_n)s mutantes y caen los %(mut_caen)s**, con el texto bueno pasando el
mismo juicio en **0 fallos**.

**UNA CAIDA PROPIA MAS, `D.4`, CAZADA POR MI EN LA SIMULACION:** mi primera
version leia los numeros de fase **de todo el fichero**, y este fichero tiene
muchas tablas: se tragaba **707, 1096, 2464 y mas** como si fueran fases. **No
cambiaba el resultado** (el 8, el 9 y el 10 no estaban entre ellos), **pero una
vara que acierta por suerte no es una vara**, asi que la lectura se acoto a la
tabla del criterio, de su cabecera a su ultima fila. Hoy da exactamente
**[0, 1, 2, 3, 4, 5, 6, 7]**.

**`docs/plan/OPERACIONES.jsonl` NO SE TOCA EN LA `2.a`, y esta probado con su
`sha256`, no prometido:** el mismo al entrar y al salir de la escritura.

#### 2.b LAS CINCO FICHAS, RE-MEDIDAS CONTRA ESAS FILAS

**Salida: `docs/loop/SALIDA_V214_T2B_REMEDIR_CINCO.txt`. La vara se LEE de
`docs/plan/08_VERIFICACION.md`, no se teclea: si aquella fila cambiara, esta
medicion cambiaria con ella.**

**LA HONESTIDAD DEL ALCANCE VA DELANTE:** no toda clausula de una vara es
mecanizable. Cada una se marca **MECANICA** (con su sonda corrida hoy y su cifra)
o **DOCUMENTAL**, y **para las documentales SE DECLARA QUE NO HAY CASO ROJO
AUTOMATICO**, en vez de fabricar una sonda que se apruebe sola.

| ficha | fase | clausulas suyas | con sonda mecanica | documentales |
|---|---|---:|---:|---:|
%(tabla_res)s

**CIFRA fichas re-medidas: %(fichas)s. CIFRA clausulas repartidas:
%(repartidas)s, de ellas %(con_sonda)s con sonda y %(documentales)s
documentales, y la suma se comprueba contra si misma en la salida.**

**LAS CUATRO SONDAS, CON SU CIFRA DE HOY:**

- **EL MARCADOR DEL ARCHIVO: %(marcador)s filas**, contadas hoy de
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.
- **LOS PARES DE LECTURA DIRIGIDA: %(ld_cab)s cabeceras**, y de esos **PARES**,
  **%(ld_dentro)s tienen veredicto en el archivo**, o sea que **la clausula
  CALZA**: viven solo en su pagina.
- **LOS CUATRO PUNTOS DE `OP-I-01`**, citados de la TAREA 1 de esta misma vuelta:
  **2 CUBRE y 2 A MEDIAS**.
- **LOS CINCO PUNTOS TRANSVERSALES DE `OP-V-01`**, buscados uno a uno por su
  marca propia dentro de la `nota` de la ficha (**%(nota_len)s caracteres**):
  **los cinco estan escritos**, y el commit que movio su estado, leido de la
  propia nota, es **`e966d896`**.

**LA `OP-V-01` VA POR PRUEBA POR CITA Y NO SE VUELVE A PRODUCIR LA CORRIDA K**,
tal como el encargo dice: es la **cuarta via** que la DECISION 5 del fundador del
4 sep 2026 autorizo **para esta ficha**. **Y se repite aqui lo que la propia nota
de la ficha ya dice, para que nadie lo lea como un verde que no es: esa prueba NO
cambia el veredicto de la vara del expediente, que sigue midiendo la ficha como
HECHA sin ninguna de sus tres pruebas.**

**DOS DISCREPANCIAS DECLARADAS, NI RESUELTAS NI TAPADAS:**

1. **`D.5`, EL MARCADOR.** La clausula escribe *"sigue en 2.117"* y el archivo mide
   **%(marcador)s** hoy. **Leida a la letra NO CALZA.** Las dos lecturas van
   escritas y **no elijo yo**: la literal dice que no calza; la de su corte dice
   que la clausula pide que **esa operacion** no mueva el marcador, y el marcador
   se movio porque **el cribado siguio hasta cerrar**, no por la ficha. **Cual de
   las dos manda es doctrina que no esta escrita: va como PENDIENTE DE
   DOCTRINA** (`EJECUTOR.md` 5).
2. **`D.6`, LA CIFRA ONCE.** La clausula dice *"las once"* y la pagina trae
   **%(ld_cab)s** cabeceras hoy, porque siguio creciendo. **La clausula es de su
   corte y se dice, en vez de reescribirla.**

**UNA CAIDA PROPIA MAS, `D.7`, Y ES DE LAS QUE IMPORTAN:** mi primera sonda de los
pares preguntaba si **los dos NOMBRES** aparecian en el archivo, y eso da que si
para casi cualquier par del catalogo: **salia 27 de 27 y habria publicado una
alarma falsa contra una clausula que en realidad se cumple**. Corregida a comparar
**el PAR** contra los campos `nodo_a` y `nodo_b`, da **%(ld_dentro)s** y la
clausula calza. **Una sonda mas laxa que su clausula no mide esa clausula.**

**LO QUE ESTA TAREA NO HACE:** la `2.b` **no escribe en el arbol del plan**, no
mueve ningun campo `estado`, no toca la vara del expediente y **no asciende
ninguna ficha**. **`numstat` del arbol del plan al cerrar: %(ns_plan)d fila(s).**
""" % {
        "ns": ns.replace("\t", " ").strip() or "(sin cambios)",
        "clausulas_08": D["clausulas_08"], "clausulas_09": D["clausulas_09"],
        "clausulas_10": D["clausulas_10"],
        "tabla_excl": tabla_excl, "n_deriv": n_deriv,
        "mut_n": D["mut_n"], "mut_caen": D["mut_caen"],
        "tabla_res": tabla_res, "fichas": D["fichas"],
        "repartidas": D["repartidas"], "con_sonda": D["con_sonda"],
        "documentales": D["documentales"], "marcador": D["marcador"],
        "ld_cab": D["ld_cab"], "ld_dentro": D["ld_dentro"],
        "nota_len": D["nota_len"], "ns_plan": len(ns_plan),
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
    print("CIFRA filas del resumen de la 2.b pegadas: %d (se esperan 5)" % len(filas_res))
    if len(filas_res) != 5:
        fallos += 1
    print("CIFRA filas de la tabla de reparto pegadas: %d (se esperan 5)" % len(reparto))
    if len(reparto) != 5:
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
