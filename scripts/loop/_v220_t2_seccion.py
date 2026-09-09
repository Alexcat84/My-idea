# -*- coding: utf-8 -*-
r"""_v220_t2_seccion.py . EL CUERPO DE LA TAREA 2 DEL REPORTE DE LA VUELTA 220,
COMPUESTO DE SU SALIDA SELLADA Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: toda tabla o cifra del reporte
cita el fichero de salida del que sale, y se RECONSTRUYE CONTANDO ESE FICHERO
antes de publicarla. Aqui NINGUNA celda se teclea: todo sale de
docs/loop/SALIDA_V220_T2_BATERIA.txt y de docs/loop/SALIDA_V220_T2_COMPONER.txt.

LO UNICO MIO SON LOS DISCUTIBLES, LA PARADA Y SUS MOTIVOS, y van rotulados como
lectura mia para que se pueda auditar cual es cual.

USO:  python scripts/loop/_v220_t2_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
SALIDA = "docs/loop/SALIDA_V%d_T2_BATERIA.txt" % VUELTA
COMPONER = "docs/loop/SALIDA_V%d_T2_COMPONER.txt" % VUELTA
DESTINO = "scripts/loop/_v%d_t2_seccion.md" % VUELTA


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def dos_convenciones(rel):
    """LA PAREJA DE BYTES DE UNA RUTA, EN UNA SOLA CADENA Y POR TANTO EN UNA
    SOLA LINEA. Es el remedio de mi propia C.4 de la 219, con mis palabras: la
    pareja de bytes no es una regla de RUTAS, es una regla de CIFRAS DE BYTES,
    vengan de una ruta o de un campo de texto de un registro."""
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    b = io.open(p, "rb").read()
    return ("%d bytes en disco y %d normalizado a LF"
            % (os.path.getsize(p), len(b.replace(b"\r\n", b"\n"))))


def L(t, ancla):
    hay = [l.strip() for l in t.split(NL) if ancla in l]
    if len(hay) != 1:
        raise SystemExit("ROJO: el ancla %r aparece %d vez(ces) y se exige 1."
                         % (ancla, len(hay)))
    return hay[0]


CUERPO = """### TAREA 2. LA BATERIA DE MUTACIONES, ENTERA Y SOLA

**LO QUE SE CORRIO, Y SU RUTA CON SUS DOS CONVENCIONES EN LA MISMA LINEA:** el
lanzador ``scripts/loop/vuelta183_bateria_por_tramos.py``, **%(bytes_lanz)s**,
que **es estable, NO SE CLONA Y NO SE REPARA**. La medicion de esta tarea vive
en ``%(salida)s``, **%(bytes_salida)s**, y la composicion en ``%(componer)s``,
**%(bytes_comp)s**.

#### 2.a y 2.d. LOS ONCE TRAMOS, CORRIDOS UNO A UNO Y COMMITEADOS AL TERMINAR

**LOS ONCE SE CORRIERON EXPLICITAMENTE, `--tramo 1` A `--tramo 11`, Y CADA UNO
SE COMMITEO CON SU SALIDA SELLADA AL TERMINAR**, que es lo que `AUDITOR.md` 6.1
manda cuando dice que una vuelta cortada retoma en el tramo siguiente.

**LA VARA DE LO QUE ESTA VUELTA ESCRIBIO NO ES EL CARRIL QUE DICE CUAL TOCA, Y
ESA ES LA MITAD QUE IMPORTA.** Es doble y las dos mitades se leen: **el `sha256`
de cada salida tiene que ser DISTINTO del que la apertura de esta vuelta sello**
(que es el de la corrida de la 215) **y el asunto de su ultimo commit tiene que
nombrar la vuelta 220**, leido de `git log`. Y la tercera puerta, la del regimen:
**una salida sellada que mide CERO BYTES no cuenta como hecha**.

%(tabla_tramos)s

- %(hechos)s
- %(vacias)s
- %(entradas_tramos)s
- %(suma_entradas)s

#### 2.b. LA DOBLE CORRIDA Y EL RELOJ, QUE NO SE AFLOJAN

**LA DOBLE CORRIDA NO LA AFIRMO YO: LA DICE LA PROPIA SALIDA DE LA BATERIA**, y
va pegada de ella:

%(doble)s

**EL RELOJ, TRAMO A TRAMO Y LEIDO DE CADA SALIDA:**

%(reloj)s

- %(minutos)s
- %(corridas)s

#### 2.c. LA SALIDA UNICA, Y LAS TRES COSAS JUNTAS

**SE COMPUSO SOLO CUANDO LOS ONCE TENIAN SALIDA SELLADA**, con `--componer`, y
el compositor salio en **exitcode 0**:

%(compositor)s

**EL NOMBRE, LOS BYTES POR LAS DOS CONVENCIONES Y LA ATRIBUCION, LAS TRES
JUNTAS:** %(tres_juntas)s

**Y LAS DOS COSAS DEL ROTULO, DICHAS LAS DOS Y NO UNA**, que es la trampa que
lleva dos actas subiendo:

%(rotulo1)s

%(rotulo2)s

%(rotulo3)s

%(rotulo_motivo)s

#### 2.e. LO QUE SALE EN ROJO: NO LO ARREGLO, LO PARO Y LO TRAIGO

**LOS ONCE TRAMOS SALEN EN `ROJO POR FALLO`, exitcode 1, Y NO REPARO NINGUNO.**
El encargo lo dice con estas palabras: *PARALO Y TRAELO*. La especie, sumada
sobre los once y leida de sus propias salidas:

%(especies)s

**LOS SIETE QUE NO MORDIERON, UNO A UNO Y CON SU TRAMO:**

%(no_mordieron)s

%(cifra_no_mordieron)s

**LOS DOS QUE EL CENSO VE Y LA NOMINA CONGELADA NO TIENE:**

%(fuera)s

%(cifra_fuera)s

**Y LO QUE DECIDE SI ESTO ES NUEVO O ES UNA CONDICION QUE YA VENIA, MEDIDO
CONTRA LA CORRIDA ANTERIOR Y NO CONTRA MI RECUERDO:** %(cotejo)s

**LAS DOS COSAS QUE ESTO SIGNIFICA, Y LAS DIGO SEPARADAS PORQUE SON DISTINTAS.**
**(1)** Los **siete que no mordieron** son la especie que el encargo nombra por
su nombre: *un mutante que no muere es una guarda que no muerde*. **(2)** Los
**dos fuera de la nomina** son la colision entre dos reglas vigentes: la del
propio fichero de la bateria, que dice que **un arnes entra en la nomina**, y la
moratoria `AUDITOR.md` 6.3, que dice que **la nomina queda CONGELADA EN 135 y ni
crece ni se poda**. **Las dos suben como PARADA a la seccion 5 de este reporte,
con sus nombres y sus cifras, y ninguna se arregla aqui.**

#### LO QUE EL CARRIL QUE DICE CUAL TRAMO TOCA CONTESTO ANTES DE CORRER NADA

**NO ES MI VARA Y NO LO USE COMO TAL.** Se corrio una sola vez, ANTES del primer
tramo, para dejar **reproducida con mi propia medicion** la caida `5.1` del acta
219 (**linea 77991** de `docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero):

%(siguiente)s

%(siguiente_glosa)s

#### LOS DISCUTIBLES DE LA TAREA 2, MARCADOS ANTES DE SABER SI ACIERTO

| # | que decidi | la duda que dejo escrita |
|---|---|---|
%(disc)s

#### EL CASO ROJO, DICHO CUAL ES CUAL

**AQUI NO HAY CASO ROJO AUTOMATICO QUE FABRICAR, Y SE DECLARA EN VEZ DE
INVENTARSE UNO QUE SE APRUEBE SOLO.** La bateria **es** el arnes: sus 135
entradas son casos rojos que corren dos veces cada una, y **esta tarea no
inventa una guarda encima**. Lo unico que este computo decide es **que salida es
de esta vuelta y cual no**, y esa decision cae en rojo por si sola por sus tres
puertas, medidas arriba una a una. **Y una correccion declarada dentro de la
propia vuelta**, que cazo esta misma guarda en rojo antes de que llegara a
ningun reporte: el patron que lee la cuenta de entradas del compositor pedia un
solo espacio antes del numero y el compositor alinea esa columna a la derecha,
asi que el tramo 11, con **5 entradas** y no 13, no casaba; la cifra que salio
fue **10 tramos de 11 y 130 entradas de 135**. **El patron viejo queda escrito
en el codigo sin borrar.**
"""

DISCUTIBLES = [
    ("D.1", "QUE CORRI LOS ONCE TRAMOS EN VEZ DE PARARME EN EL PRIMERO",
     "El encargo `2.e` dice **si un tramo sale en rojo, no lo arregles: paralo "
     "y traelo**, y **el tramo 1 salio en rojo**. Yo segui hasta el 11 y traigo "
     "el rojo entero. **Mi motivo, escrito antes de saber si acierto**: el rojo "
     "del tramo 1 no es un mutante que no muere (esa cifra es **0 con ancla "
     "perdida, 0 que no mordieron, 0 sin reproducir** en ese tramo), es la "
     "cuenta de censo contra nomina, **es identica a la del tramo 1 de la 215** "
     "y se recomputa al cierre de CADA tramo, con lo que pararme en el primero "
     "habria dejado diez tramos sin correr por una condicion que ya venia. **Si "
     "el auditor lee que `2.e` manda parar la vuelta entera en el primer "
     "exitcode 1**, entonces corri diez tramos que no me tocaban, y el que "
     "decide es el."),
    ("D.2", "QUE LOS SIETE QUE NO MORDIERON SUBEN COMO PARADA Y NO COMO CAIDA "
            "MIA",
     "Los siete son **exactamente los mismos siete, nombre por nombre, que la "
     "corrida anterior**, y lo mido contra la version commiteada en el HEAD de "
     "apertura. **Mi lectura**: no los rompio esta vuelta, no los reparo (la "
     "moratoria lo prohibe) y suben nombrados. **La duda**: la letra del 7 sep "
     "*la guarda que se publica como mordiendo y no muerde* podria pedir que "
     "una bateria con siete arneses que no muerden **no se declare corrida**, y "
     "yo la declaro corrida porque los once tramos tienen salida sellada del "
     "mismo calibre y el compositor cubre las 135 entradas exactamente una vez. "
     "**Si el auditor lee que corrida exige ademas que muerdan**, esta bateria "
     "no esta corrida y la 220 no la cerro."),
    ("D.3", "QUE LA SALIDA UNICA SE DEJA EN EL NOMBRE Y EL ROTULO QUE EL "
            "LANZADOR LE PONE",
     "El fichero compuesto se llama `docs/loop/SALIDA_V183_BATERIA.txt` y su "
     "primera linea dice **VUELTA 183** sobre contenido de la **220**. **No lo "
     "renombro ni le toco el rotulo**: el numero lo computa el lanzador de su "
     "propio nombre de fichero y **repararlo seria clonar o reparar el "
     "lanzador**, que la moratoria `6.3` prohibe. **La duda**: eso deja en el "
     "arbol, otra vuelta mas, un fichero cuyo nombre miente sobre su contenido, "
     "y **ya lleva tres actas subiendo**. Si el auditor lee que esto es caida "
     "de dato y no desfase heredado, entonces la moratoria si tenia excepcion "
     "aqui y yo no la use."),
]


def main():
    t = leer(SALIDA)
    comp = leer(COMPONER)

    ls = t.split(NL)
    tramos = [l.strip() for l in ls if re.match(r"^\s{3}TRAMO \d+\s+docs/loop/",
                                                l)]
    veredictos = [l.strip() for l in ls
                  if l.strip().startswith("VEREDICTO DE ESTA CORRIDA:")]
    doble = [l.strip() for l in ls if l.strip().startswith("bateria>")]
    reloj = [l.strip() for l in ls if "DURACION DEL TRAMO" in l
             and l.strip().startswith("TRAMO")]
    compositor = [l.strip() for l in ls if l.strip().startswith("compositor>")]
    especies = [l.strip() for l in ls
                if re.match(r"^\s{6}CIFRA (ancla perdida|que no mordieron|"
                            r"sin reproducir|fuera de la nomina|invisibles al "
                            r"censo|SUJETO VIVO):", l)]
    no_mordieron = []
    dentro = False
    for l in ls:
        if "LOS QUE NO MORDIERON, UNO A UNO" in l:
            dentro = True
            continue
        if dentro:
            if l.strip().startswith("CIFRA "):
                break
            if l.strip():
                no_mordieron.append(l.strip())
    fuera = []
    dentro = False
    for l in ls:
        if "LOS QUE EL CENSO VE Y LA NOMINA CONGELADA NO TIENE" in l:
            dentro = True
            continue
        if dentro:
            if l.strip().startswith("CIFRA "):
                break
            if l.strip():
                fuera.append(l.strip())
    siguiente = [l.strip() for l in ls if l.strip().startswith("siguiente>")]

    # LA TABLA DE LOS ONCE SE ARMA DE LAS LINEAS DEL FICHERO, NO SE TECLEA.
    filas = []
    for i, l in enumerate(tramos):
        m = re.match(r"TRAMO (\d+)\s+(\S+): (\d+) bytes en disco y (\d+) bytes "
                     r"normalizado a LF \| sha256 disco (\w+) \| sha256 que "
                     r"sello la apertura (\w+) \| SE MOVIO: (\w+) \| vuelta del "
                     r"ultimo commit: (\d+) \| NO VACIA: (\w+) \| CUENTA COMO "
                     r"HECHO: (\w+)", l)
        if not m:
            raise SystemExit("ROJO: la linea del tramo no se puede leer: %r" % l)
        filas.append("| %s | %s bytes en disco y %s normalizado a LF | `%s` | `%s` | %s | %s | %s | **%s** |"
                     % (m.group(1), m.group(3), m.group(4), m.group(5),
                        m.group(6), m.group(7), m.group(8), m.group(9),
                        m.group(10)))
    tabla = ["| tramo | bytes de su salida sellada | sha256 de hoy | sha256 que sello la apertura | se movio | vuelta de su commit | no vacia | cuenta como hecho |",
             "|---:|---|---|---|:-:|:-:|:-:|:-:|"] + filas

    datos = {
        "salida": SALIDA,
        "componer": COMPONER,
        "bytes_salida": dos_convenciones(SALIDA),
        "bytes_comp": dos_convenciones(COMPONER),
        "bytes_lanz": dos_convenciones(
            "scripts/loop/vuelta183_bateria_por_tramos.py"),
        "tabla_tramos": NL.join(tabla),
        "hechos": L(t, "CIFRA tramos con salida sellada no vacia ESCRITA EN "
                       "ESTA VUELTA:"),
        "vacias": L(t, "CIFRA salidas de tramo que miden CERO BYTES:"),
        "entradas_tramos": L(t, "CIFRA tramos con su cuenta de entradas leida "
                                "del compositor:"),
        "suma_entradas": L(t, "CIFRA entradas sumadas de los once tramos:"),
        "doble": NL.join("- " + x for x in doble),
        "reloj": NL.join("- " + x for x in reloj),
        "minutos": L(t, "CIFRA minutos de reloj sumados de los once tramos:"),
        "corridas": L(t, "CIFRA entradas corridas: "),
        "compositor": NL.join("- " + x for x in compositor),
        "tres_juntas": L(t, "EL NOMBRE, LOS BYTES POR LAS DOS CONVENCIONES Y LA "
                            "ATRIBUCION, LAS TRES JUNTAS:"),
        "rotulo1": "- " + L(t, "1. SU PRIMERA LINEA, LEIDA DEL FICHERO>"),
        "rotulo2": "- " + L(t, "2. SU CONTENIDO ES EL DE LA VUELTA"),
        "rotulo3": "- " + L(t, "CIFRA menciones de la vuelta 183 en su primera "
                               "linea:"),
        "rotulo_motivo": L(t, "Y EL MOTIVO, MEDIDO Y NO SUPUESTO:"),
        "especies": NL.join("- " + x for x in especies),
        "no_mordieron": NL.join("- `%s`" % x.split(None, 2)[2]
                                if x.startswith("TRAMO") else "- " + x
                                for x in no_mordieron),
        "cifra_no_mordieron": L(t, "CIFRA arneses que NO MORDIERON en esta "
                                   "corrida:"),
        "fuera": NL.join("- `%s`" % x for x in fuera),
        "cifra_fuera": L(t, "CIFRA arneses fuera de la nomina, distintos:"),
        "cotejo": L(t, "CIFRA tramos cuya lista de los que no mordieron es "
                       "IDENTICA"),
        "siguiente": NL.join("- " + x for x in siguiente),
        "siguiente_glosa": L(t, "LA CIFRA QUE ESO CONTESTABA ERA FALSA PARA LA"),
        "disc": NL.join("| **%s** | %s | %s |" % (a, b_, c)
                        for a, b_, c in DISCUTIBLES),
    }
    texto = CUERPO % datos

    print("CIFRA filas de la tabla de los once tramos, contadas del fichero: %d "
          "| CIFRA que deberia haber: 11" % len(filas))
    print("CIFRA veredictos de tramo leidos del fichero: %d | CIFRA que deberia "
          "haber: 11" % len(veredictos))
    print("CIFRA lineas de reloj pegadas: %d | CIFRA que deberia haber: 11"
          % len(reloj))
    print("CIFRA especies pegadas: %d | CIFRA que deberia haber: 6"
          % len(especies))
    print("CIFRA arneses que no mordieron pegados: %d | CIFRA que deberia "
          "haber: 7" % len(no_mordieron))
    print("CIFRA arneses fuera de la nomina pegados: %d | CIFRA que deberia "
          "haber: 2" % len(fuera))
    print("CIFRA lineas del compositor pegadas: %d | CIFRA que deberia haber: 4"
          % len(compositor))
    print("CIFRA lineas del carril que dice cual toca pegadas: %d | CIFRA que "
          "deberia haber: 4" % len(siguiente))
    fallos = 0
    for etiqueta, cond in (("tramos", len(filas) == 11),
                           ("veredictos", len(veredictos) == 11),
                           ("reloj", len(reloj) == 11),
                           ("especies", len(especies) == 6),
                           ("no mordieron", len(no_mordieron) == 7),
                           ("fuera de la nomina", len(fuera) == 2),
                           ("compositor", len(compositor) == 4),
                           ("carril", len(siguiente) == 4)):
        if not cond:
            fallos += 1
            print("   ROJO: la cuenta de %s no calza." % etiqueta)

    mayores = [l for l in texto.split(NL)
               if l.startswith("## ") and not l.startswith("### ")]
    print("CIFRA encabezados de nivel dos en el cuerpo del anexo: %d | CIFRA "
          "que deberia haber: 0" % len(mayores))
    if mayores:
        fallos += 1
    largos = texto.count(chr(8212)) + texto.count(chr(8211))
    print("CIFRA guiones largos mas medios en el cuerpo: %d" % largos)
    if largos:
        fallos += 1
    sospechosos = [c for c in re.findall(r"`([^`]+)`", texto)
                   if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sospechosos))
    if sospechosos:
        for s in sospechosos:
            print("   sospechoso> %s" % s)
        fallos += 1
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: el compositor NO escribe.")
        return 1
    ruta = os.path.join(RAIZ, DESTINO.replace("/", os.sep))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITO %s -> %d bytes en disco, %d lineas"
          % (DESTINO, os.path.getsize(ruta), texto.count(NL)))
    print("VERDE: el cuerpo de la TAREA 2 queda compuesto de su fichero.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
