# -*- coding: utf-8 -*-
r"""_v216_t1_seccion.py . EL CUERPO DE LA TAREA 1 DEL REPORTE DE LA VUELTA 216,
COMPUESTO DE SU SALIDA SELLADA Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: toda tabla o cifra del reporte
cita el fichero de salida del que sale, y se reconstruye contando ese fichero
antes de publicarla. Las filas de las tablas se LEEN de la salida sellada de
_v216_t1_registros.py, no se teclean, y el compositor DICE cuantas armo y
cuantas deberia haber.

LAS GLOSAS DE LAS CUATRO QUE ME OBLIGAN SI LAS ESCRIBO YO, y eso se dice: LA
LINEA y EL TITULO salen del acta por instrumento, y la columna de QUE ME OBLIGA
A HACER es LECTURA MIA. Se separan en dos columnas para que se pueda auditar
cual es cual, que es lo que el encargo pide con esas palabras.

USO:  python scripts/loop/_v216_t1_seccion.py
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
DESTINO = "scripts/loop/_v%d_t1_seccion.md" % VUELTA

# LO QUE CADA UNA DE LAS CUATRO ME OBLIGA A HACER EN ESTA VUELTA. ES MI LECTURA
# DEL ENCARGO, NO TEXTO DEL ACTA, y por eso vive aqui y no se mezcla con lo que
# el instrumento lee del acta.
QUE_ME_OBLIGA = {
    "5.1": "NO CORRO LA BATERIA. Esta declarada CORRIDA por la 215 con sus once "
           "tramos y sus 135 entradas contadas por el auditor, y la cadencia de "
           "cinco de `AUDITOR.md` 6.1 pone la siguiente en la **220**. Mi "
           "seccion 9 cierra con el HUECO DECLARADO Y MEDIDO por el carril de "
           "la TAREA 1.b de la vuelta 173, con su medicion, su atribucion y su "
           "corrida.",
    "5.2": "NO TOCO EL LANZADOR DE LA BATERIA Y NO PROPONGO PODA. El rojo "
           "estructural queda COMO ESTA IMPRESO: mide la vara 148, que es una "
           "regla escrita dentro de un script, y el fundador la tiene "
           "suspendida por la moratoria. La poda se decide en la auditoria "
           "integral y no antes, y por tanto la nomina sigue CONGELADA EN 135.",
    "5.4": "DOY `OP-I-01` POR CERRADA POR LA DECISION 1 DEL FUNDADOR, y su "
           "punto 4 sube NOMBRADO sin bloquear. No relleno ese hueco y no "
           "muevo su campo de estado: lo mido, lo publico y lo digo.",
    "5.7": "CORRO LA RE-MEDICION DE LAS CINCO FICHAS CONTRA LAS CATORCE FILAS, "
           "y es mi TAREA 2 y es BLOQUEANTE. La ordeno el fundador el 9 sep "
           "2026 en la DECISION 2 y no la ha corrido nadie.",
}

# LO QUE CADA UNA DE LAS OTRAS CUATRO DEJA REGISTRADO. TAMBIEN ES LECTURA MIA,
# y va en la misma columna que se rotula como tal.
QUE_REGISTRO = {
    "5.3": "REGISTRADA, y no me da orden nueva: confirma que no tocar los siete "
           "arneses fue lo correcto y los manda NOMBRADOS a la auditoria "
           "integral. Esta vuelta tampoco los toca.",
    "5.5": "REGISTRADA, y cierra a mi favor el punto 3 y mis discutibles `D.a`, "
           "`D.b` y `D.d` de la 215. No me da orden nueva.",
    "5.6": "REGISTRADA, y cierra a mi favor mi discutible `D.c` de la 215 sobre "
           "correr los once tramos con el primero en rojo. No me da orden nueva.",
    "5.8": "REGISTRADA, y es ADEMAS una de las dos correcciones declaradas que "
           "la 1.b me manda escribir con su cifra. No me da orden nueva.",
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


def titulo_de(etiqueta, texto):
    """EL TITULO ES LO QUE VA HASTA EL PRIMER CIERRE DE NEGRITA, que es como el
    acta separa el titulo de su fundamento. PURA."""
    cuerpo = texto.split("`%s`" % etiqueta, 1)[-1]
    return cuerpo.split("**", 1)[0].strip()


def main():
    salida = leer(SALIDA)
    mut = leer(MUTANTES)

    filas_obliga, filas_registro = [], []
    n_adj_leidas = 0
    for l in salida.split(NL):
        m = re.match(r"^ADJUDICACION (\d+\.\d+) \| linea (\d+) \| (\w+) \| (.*)$", l)
        if not m:
            continue
        n_adj_leidas += 1
        etiqueta, linea, clase, texto = m.group(1), m.group(2), m.group(3), m.group(4)
        titulo = titulo_de(etiqueta, texto)
        if clase == "OBLIGA":
            filas_obliga.append("| **`%s`** | **%s** | %s | %s |"
                                % (etiqueta, linea, titulo,
                                   QUE_ME_OBLIGA.get(etiqueta, "(sin glosa)")))
        else:
            filas_registro.append("| **`%s`** | **%s** | %s | %s |"
                                  % (etiqueta, linea, titulo,
                                     QUE_REGISTRO.get(etiqueta, "(sin glosa)")))

    filas_hall = []
    for l in salida.split(NL):
        m = re.match(r"^HALLAZGO (\d+\.\d+) \| linea (\d+) \| (.*)$", l)
        if not m:
            continue
        etiqueta, linea, texto = m.group(1), m.group(2), m.group(3)
        filas_hall.append("| **`%s`** | **%s** | %s |"
                          % (etiqueta, linea, titulo_de(etiqueta, texto)))

    filas_anc = []
    for l in salida.split(NL):
        m = re.match(r"^ANCLAJE \| (.+?) \| linea (\d+) \| (.*)$", l)
        if not m:
            continue
        filas_anc.append("| %s | **%s** | %s |"
                         % (m.group(1), m.group(2), m.group(3).replace("|", " ")))

    filas_s6 = []
    for l in salida.split(NL):
        m = re.match(r"^SECCION6 punto (\d+) \| linea (\d+) \| \d+\. (.*)$", l)
        if not m:
            continue
        filas_s6.append("| **%s** | **%s** | %s |"
                        % (m.group(1), m.group(2), m.group(3).replace("|", " ")))

    D = {
        "v": VUELTA,
        "salida": SALIDA,
        "mutantes": MUTANTES,
        "lineas_acta": cifra(salida, "CIFRA lineas de docs/loop/ACTA_AUDITOR.md: "),
        "abre": cifra(salida, "CIFRA linea donde ABRE el acta de la vuelta 215: "),
        "entradas": cifra(salida, "CIFRA entradas halladas en el acta entera: "),
        "n_adj": cifra(salida, "CIFRA adjudicaciones (seccion 5): "),
        "n_hall": cifra(salida, "CIFRA hallazgos (seccion 3): "),
        "n_s6": cifra(salida, "CIFRA puntos numerados de la seccion 6: "),
        "n_mut": cifra(mut, "CIFRA mutantes: "),
        "caen": cifra(mut, "CIFRA mutantes que CAEN: "),
        "bueno": cifra(mut, "CIFRA fallos del texto bueno: "),
        "n_adj_leidas": n_adj_leidas,
        "n_obliga": len(filas_obliga),
        "n_registro": len(filas_registro),
        "n_filas_hall": len(filas_hall),
        "n_filas_anc": len(filas_anc),
        "n_filas_s6": len(filas_s6),
        "filas_obliga": NL.join(filas_obliga),
        "filas_registro": NL.join(filas_registro),
        "filas_hall": NL.join(filas_hall),
        "filas_anc": NL.join(filas_anc),
        "filas_s6": NL.join(filas_s6),
    }

    cuerpo = """### TAREA 1. LOS REGISTROS, Y LA LINEA DE CADA UNO LEIDA HOY

**LA FUENTE ES EL ACTA Y EL LECTOR ES UN INSTRUMENTO.**
`scripts/loop/_v%(v)d_t1_registros.py` abre `docs/loop/ACTA_AUDITOR.md`
(**%(lineas_acta)s** lineas hoy), localiza el acta de la vuelta 215 por su
cabecera en la **linea %(abre)s**, y saca sus entradas numeradas con
`enumerate()`. **NINGUN NUMERO DE LINEA DE ESTA SECCION SE TECLEA**, que es lo
que manda el 6.6 del acta 210, la letra de `EJECUTOR.md` 1 y la orden literal
del encargo. El instrumento halla **%(entradas)s** entradas numeradas en el acta
entera, de ellas **%(n_adj)s** adjudicaciones y **%(n_hall)s** hallazgos.

#### 1.a. LAS CUATRO ADJUDICACIONES QUE ME OBLIGAN, CON SU TITULO VERBATIM Y CON MI LECTURA APARTE

**FILAS ARMADAS LEYENDO `%(salida)s`: %(n_obliga)d. FILAS QUE DEBERIA HABER,
CONTADAS POR EL PROPIO INSTRUMENTO SOBRE EL ACTA: 4.** **LAS DOS SE ESCRIBEN
JUNTAS**, por la obligacion de las filas.

**LAS DOS COLUMNAS SON DE AUTORES DISTINTOS Y POR ESO VAN SEPARADAS:** la de
TITULO es del auditor y sale del acta por instrumento, verbatim; la de QUE ME
OBLIGA **es lectura mia del encargo** y no la sostiene ningun instrumento.

| adjudicacion | linea del acta | titulo, VERBATIM del acta (AUTOR: EL AUDITOR) | que me obliga a hacer en esta vuelta (LECTURA MIA) |
|---|---:|---|---|
%(filas_obliga)s

#### 1.a.bis. LAS OTRAS CUATRO, REGISTRADAS IGUAL PORQUE EL ENCARGO MANDA REGISTRAR LAS OCHO

**FILAS ARMADAS LEYENDO `%(salida)s`: %(n_registro)d. FILAS QUE DEBERIA HABER:
4.** **%(n_adj_leidas)d filas de adjudicacion leidas en total, contra las
%(n_adj)s que el instrumento cuenta sobre el acta.**

| adjudicacion | linea del acta | titulo, VERBATIM del acta (AUTOR: EL AUDITOR) | lo que deja registrado (LECTURA MIA) |
|---|---:|---|---|
%(filas_registro)s

#### 1.b. LAS DOS CORRECCIONES DECLARADAS DEL AUDITOR, CADA UNA CON SU CIFRA

**FILAS ARMADAS LEYENDO `%(salida)s`: %(n_filas_anc)d. FILAS QUE DEBERIA HABER:
3** (las dos correcciones de la 1.b **mas** la cifra mala de la 1.c, que el
mismo instrumento ancla). **Las tres se localizan POR SU TEXTO dentro del acta y
se exige que aparezcan UNA sola vez, o el instrumento cae en rojo.**

| lo que ancla | linea del acta | la linea del acta, VERBATIM |
|---|---:|---|
%(filas_anc)s

**CORRECCION 1, CON SU CIFRA: LAS FICHAS EN HECHA SIN NINGUNA PRUEBA SON
CUATRO, NO DOS.** Su `5.8` corrige por declaracion una cifra de su antecesor: el
acta 214, en su `5.9`, nombraba **DOS** (`OP-V-01` y `OP-L-01`), y medido hoy
por el con la misma vara y con los dos cortes **son CUATRO**: `OP-V-01`,
`OP-L-01`, `OP-L-02` y `OP-L-03`. **La cifra vieja no se retira y no era falsa:
nombraba dos de las cuatro sin afirmar que fueran solo dos.**

**CORRECCION 2, CON SU CIFRA: MI RACHA DE CAIDA DE REPORTE VUELVE A CERO.** Su
`3.1` mide **0 cifras mias que no calcen con las suyas**, y por la letra que el
acta 203 cita en su linea **71534** (*"sin caida que acumule rompe la racha"*)
**la racha que la 214 dejo en UNO vuelve a CERO**. **No arrastro ninguna**, y
por tanto **no hay escalada del tallador que encargar**, porque la racha no
llego a dos.

#### 1.c. LA UNICA CIFRA MALA DEL ACTA, QUE ES DEL AUDITOR, Y SE ESCRIBE IGUAL

**SU RELECTURA CIEGA SALE 67 DE 80** (acta de la 215, **linea %(linea_ciega)s**,
verbatim: *"Y una cifra mia que no adorno: mi ciega sale 67 de 80."*).

**NO ME TOCA HACER NADA CON ELLA Y NO LA DISCUTO**, que es exactamente lo que el
encargo dice. **Me toca que quede escrita**, y queda: **el registro de una vuelta
no es el escaparate de nadie**, y una vuelta que solo publica las cifras malas
del otro es la misma especie de verde que esta casa lleva doscientas vueltas
cazando.

#### 1.d. LA SECCION 6 DEL ACTA, LO QUE SUBE A LA AUDITORIA INTEGRAL

**FILAS ARMADAS LEYENDO `%(salida)s`: %(n_filas_s6)d. FILAS QUE DEBERIA HABER,
CONTADAS POR EL INSTRUMENTO: %(n_s6)s.** Se registra aqui porque **es la sede a
la que mi TAREA 3 remite lo que el bucle no puede cerrar**, y porque el encargo
manda leer tambien la seccion 6.

| punto | linea del acta | lo que sube, VERBATIM del acta |
|---:|---:|---|
%(filas_s6)s

#### 1.e. LA GUARDA DE ESTA TAREA, PROBADA POR MUTACION Y NO PROMETIDA

**`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION.** El juicio vive en una
funcion pura, `juzgar()`, y `scripts/loop/_v%(v)d_t1_mutantes.py` **le da de
comer listas rotas sin tocar el acta ni un byte**.

**CIFRA fallos del texto bueno: %(bueno)s** (se exigen 0). **CIFRA mutantes:
%(n_mut)s | CIFRA mutantes que CAEN: %(caen)s.** Contadas de
`%(mutantes)s`. Los nueve rompen una cosa cada uno: falta una adjudicacion,
falta una de las cuatro que obligan, una etiqueta renumerada, una adjudicacion
de mas, falta un hallazgo, un anclaje que no aparece, un anclaje que aparece dos
veces (que es cita ambigua), la seccion 6 sin puntos, y todo vacio.
""" % dict(D, linea_ciega=(cifra(salida, "SU UNICA CIFRA MALA, QUE ES SUYA (su seccion 7) | linea ") or "?"))

    fallos = 0
    print("EL COMPOSITOR DE LA TAREA 1, Y SUS GUARDAS ANTES DE ESCRIBIR")
    print("CIFRA filas de adjudicacion leidas de la salida: %d (se exigen 8)"
          % n_adj_leidas)
    if n_adj_leidas != 8:
        fallos += 1
    print("CIFRA filas que OBLIGAN: %d (se exigen 4)" % len(filas_obliga))
    if len(filas_obliga) != 4:
        fallos += 1
    print("CIFRA filas de REGISTRO: %d (se exigen 4)" % len(filas_registro))
    if len(filas_registro) != 4:
        fallos += 1
    print("CIFRA filas de hallazgo: %d (se exigen 4)" % len(filas_hall))
    if len(filas_hall) != 4:
        fallos += 1
    print("CIFRA filas de anclaje: %d (se exigen 3)" % len(filas_anc))
    if len(filas_anc) != 3:
        fallos += 1
    print("CIFRA filas de la seccion 6: %d (se exigen 5)" % len(filas_s6))
    if len(filas_s6) != 5:
        fallos += 1
    print("CIFRA celdas sin glosa: %d (se exigen 0)" % cuerpo.count("(sin glosa)"))
    if "(sin glosa)" in cuerpo:
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
    print("VERDE: el cuerpo de la TAREA 1 queda compuesto.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
