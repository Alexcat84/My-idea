# -*- coding: utf-8 -*-
r"""_v215_t1_seccion.py . EL CUERPO DE LA TAREA 1 DEL REPORTE DE LA VUELTA 215,
COMPUESTO DE SU SALIDA SELLADA Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: toda tabla o cifra del reporte
cita el fichero de salida del que sale, y se reconstruye contando ese fichero
antes de publicarla. Las filas de la tabla de adjudicaciones se LEEN de la
salida sellada de _v215_t1_registros.py, no se teclean, y el compositor DICE
cuantas armo y cuantas deberia haber.

LAS GLOSAS DE LAS CINCO QUE SE APLICAN COMO ORDEN SI LAS ESCRIBO YO, y eso se
dice: la LINEA y el TITULO salen del acta por instrumento, y la columna de QUE
ME OBLIGA A HACER es mi lectura del encargo. Se separan en dos columnas para que
se pueda auditar cual es cual.

USO:  python scripts/loop/_v215_t1_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
SALIDA = "docs/loop/SALIDA_V%d_T1_REGISTROS.txt" % VUELTA
MUTANTES = "docs/loop/SALIDA_V%d_T1_MUTANTES.txt" % VUELTA

# LO QUE CADA UNA DE LAS CINCO ME OBLIGA A HACER EN ESTA VUELTA. ES MI LECTURA
# DEL ENCARGO, NO TEXTO DEL ACTA, y por eso vive aqui y no se mezcla con lo que
# el instrumento lee del acta.
QUE_ME_OBLIGA = {
    "5.1": "CORRO ONCE TRAMOS Y NO PARO EN NUEVE. La bateria se declara corrida "
           "cuando los ONCE que el reparto compute tengan salida sellada del "
           "mismo calibre. NO reescribo el fichero del auditor: el nueve es la "
           "cifra a su corte y se corrige por declaracion.",
    "5.2": "NO USO EL CARRIL DE LA SENAL DE ARRANQUE PARA DECIDIR NADA. Corro "
           "tramo por tramo del 1 al 11 y commiteo cada salida al terminar, y "
           "publico ANTES el commit y la fecha de los sellos viejos.",
    "5.3": "NO VUELVO A TRAER EL MARCADOR COMO PENDIENTE DE DOCTRINA. La "
           "clausula pide que ESA operacion no mueva el marcador, no afirma "
           "cuanto vale. PENDIENTE CERRADO, y esta vuelta no mueve el marcador.",
    "5.4": "MIDO EL PUNTO 3 DE `OP-I-01` CORRIENDO LA BUSQUEDA Y PUBLICANDO SU "
           "CERO CON EL COMANDO DELANTE. Lo que se prohibe es afirmar una "
           "busqueda NO CORRIDA, no publicar la que da cero. Va en la TAREA 4.",
    "5.5": "BUSCO LA SEDE QUE SI REGENERA LA VISTA HUMANA ANTES DE DECIR SI EL "
           "PUNTO 4 CUBRE. No la invento: publico la busqueda con su comando, y "
           "si la sede no existe eso tambien es un resultado. Va en la TAREA 4.",
}


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


def main():
    salida = leer(SALIDA)
    mut = leer(MUTANTES)

    filas_adj = []
    for l in salida.split(NL):
        m = re.match(r"^ADJUDICACION (\d+\.\d+) \| linea (\d+) \| (.*)$", l)
        if not m:
            continue
        etiqueta, linea, texto = m.group(1), m.group(2), m.group(3)
        # EL TITULO ES LO QUE VA HASTA EL PRIMER CIERRE DE NEGRITA, que es como
        # el acta separa el titulo de la adjudicacion de su fundamento.
        cuerpo = texto.split("`%s`" % etiqueta, 1)[-1]
        titulo = cuerpo.split("**", 1)[0].strip()
        obliga = QUE_ME_OBLIGA.get(etiqueta, "REGISTRADA, no me da orden nueva.")
        filas_adj.append("| **`%s`** | **%s** | %s | %s |"
                         % (etiqueta, linea, titulo, obliga))

    filas_hall = []
    for l in salida.split(NL):
        m = re.match(r"^HALLAZGO (\d+\.\d+) \| linea (\d+) \| (.*)$", l)
        if not m:
            continue
        etiqueta, linea, texto = m.group(1), m.group(2), m.group(3)
        cuerpo = texto.split("`%s`" % etiqueta, 1)[-1]
        titulo = cuerpo.split("**", 1)[0].strip()
        filas_hall.append("| **`%s`** | **%s** | %s |" % (etiqueta, linea, titulo))

    D = {
        "lineas_acta": cifra(salida, "CIFRA lineas de docs/loop/ACTA_AUDITOR.md: "),
        "abre": cifra(salida, "CIFRA linea donde ABRE el acta de la vuelta 214: "),
        "entradas": cifra(salida, "CIFRA entradas halladas en el acta entera: "),
        "n_adj": cifra(salida, "CIFRA adjudicaciones (seccion 5): "),
        "n_mut": cifra(mut, "CIFRA mutantes: "),
        "caen": cifra(mut, "CIFRA mutantes que CAEN: "),
        "bueno": cifra(mut, "CIFRA fallos del texto bueno: "),
    }

    cuerpo = """### TAREA 1. LOS REGISTROS, Y LA LINEA DE CADA UNO LEIDA HOY

**LA FUENTE ES EL ACTA Y EL LECTOR ES UN INSTRUMENTO.**
`scripts/loop/_v%(v)d_t1_registros.py` abre `docs/loop/ACTA_AUDITOR.md`
(**%(lineas_acta)s** lineas hoy), localiza el acta de la vuelta 214 por su
cabecera en la **linea %(abre)s**, y saca sus entradas numeradas con
`enumerate()`. **NINGUN NUMERO DE LINEA DE ESTA SECCION SE TECLEA**, que es lo
que manda el `6.6` del acta 210 y la letra de `EJECUTOR.md` 1.

#### 1.a. LAS NUEVE ADJUDICACIONES, CON SU LINEA Y CON LO QUE ME OBLIGAN A HACER

**FILAS ARMADAS LEYENDO `%(salida)s`: %(n_filas_adj)d. FILAS QUE DEBERIA HABER,
CONTADAS POR EL PROPIO INSTRUMENTO SOBRE EL ACTA: %(n_adj)s.** **LAS DOS SE
ESCRIBEN JUNTAS**, por la obligacion de las filas.

| adjudicacion | linea del acta | titulo, VERBATIM del acta | que me obliga a hacer en esta vuelta (LECTURA MIA) |
|---|---:|---|---|
%(filas_adj)s

**LAS CUATRO ULTIMAS (`5.6` a `5.9`) NO ME DAN ORDEN NUEVA Y LO DIGO EN VEZ DE
INFLARLAS:** dos responden preguntas de la 214, una adjudica sus tres discutibles
a su favor, y la `5.9` confirma su `D.3`. **Se registran porque el encargo manda
registrar LAS NUEVE, no solo las cinco que mandan.**

#### 1.b. EL HALLAZGO CONTRA MI PROPIO REPORTE DE LA 214, QUE ES LA CAIDA QUE ACUMULA

**FILAS ARMADAS: %(n_filas_hall)d.** El acta trae dos entradas en su seccion 3 y
las dos van aqui, porque esconder la que me favorece seria elegir.

| hallazgo | linea del acta | titulo, VERBATIM del acta |
|---|---:|---|
%(filas_hall)s

**LO REGISTRO SIN ATENUARLO, PORQUE ES MIO Y ES EL UNICO QUE ACUMULA.** Mi
seccion 3.1 de la 214, la del ciclo entero de Gate 0, **salio publicada VACIA**:
sus dos filas decian que no habia fichero de consola y las tres columnas de
medicion salieron en blanco. **La causa esta medida y no supuesta: el fichero de
consola que mi compositor buscaba NUNCA EXISTIO**, ni en el arbol ni en la
historia, porque el ciclo imprime su consola por `stdout` y yo no la redirigi. **Y
lo que importa mas que la celda vacia: mi compositor escribio una fila en blanco
y siguio**, que es degradacion silenciosa, que es justo lo que el banco 9
prohibe.

**MI RACHA DE CAIDA DE REPORTE QUEDA EN UNO**, y el remedio de las dos mitades va
en la **TAREA 5** de esta vuelta, que es bloqueante: la consola se sella **desde
dentro del propio instrumento** y el compositor **CAE EN ROJO** si no la
encuentra, en vez de rellenar con un hueco.

#### 1.c. LA GUARDA DE ESTA TAREA, Y SU PRUEBA DE MUTACION

**Las cuatro comprobaciones viven en una funcion pura, `juzgar()`, para que se
puedan mutar sin tocar el acta**: que las adjudicaciones sean nueve, que sus
etiquetas vayan de `5.1` a `5.9` sin huecos ni repeticiones, que las cinco que el
encargo manda aplicar esten, y que el hallazgo `3.1` aparezca.

**`%(mutantes)s`: %(n_mut)s mutantes, CAEN %(caen)s, y el texto bueno pasa el
mismo juicio en %(bueno)s fallos.** El mutante `F` es el que de verdad me
importaba: **las dos listas vacias**, que es lo que devuelve un lector que no
encuentra nada, **cae con 4 fallos**. Un lector roto que no cae es exactamente la
enfermedad de mi `3.1`.
""" % {
        "v": VUELTA,
        "salida": SALIDA,
        "mutantes": MUTANTES,
        "filas_adj": NL.join(filas_adj),
        "filas_hall": NL.join(filas_hall),
        "n_filas_adj": len(filas_adj),
        "n_filas_hall": len(filas_hall),
        "lineas_acta": D["lineas_acta"], "abre": D["abre"],
        "n_adj": D["n_adj"], "n_mut": D["n_mut"],
        "caen": D["caen"], "bueno": D["bueno"],
    }

    fallos = 0
    print("CIFRA filas de adjudicacion armadas: %d | CIFRA que el acta dice: %s"
          % (len(filas_adj), D["n_adj"]))
    if len(filas_adj) != int(D["n_adj"]):
        fallos += 1
    print("CIFRA filas de hallazgo armadas: %d (se esperan 2)" % len(filas_hall))
    if len(filas_hall) != 2:
        fallos += 1
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
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: no se escribe el cuerpo.")
        return 1
    destino = os.path.join(RAIZ, "scripts", "loop",
                           "_v%d_t1_seccion.md" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(cuerpo)
    print("ESCRITO %s -> %d bytes, %d lineas"
          % (destino, len(cuerpo.encode("utf-8")), cuerpo.count(NL)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
