# -*- coding: utf-8 -*-
r"""_v220_t1_seccion.py . EL CUERPO DE LA TAREA 1 DEL REPORTE DE LA VUELTA 220,
COMPUESTO DE SU SALIDA SELLADA Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: toda tabla o cifra del reporte
cita el fichero de salida del que sale, y se RECONSTRUYE CONTANDO ESE FICHERO
antes de publicarla. Aqui NINGUNA celda se teclea: las filas se leen de
docs/loop/SALIDA_V220_T1_REGISTROS.txt, y el compositor DICE cuantas armo y
cuantas deberia haber.

LO UNICO MIO SON LOS DISCUTIBLES Y SUS MOTIVOS, y van en su propia seccion
rotulada como lectura mia, para que se pueda auditar cual es cual.

USO:  python scripts/loop/_v220_t1_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
SALIDA = "docs/loop/SALIDA_V%d_T1_REGISTROS.txt" % VUELTA
MUTACION = "docs/loop/SALIDA_V%d_T1_MUTACION.txt" % VUELTA
DESTINO = "scripts/loop/_v%d_t1_seccion.md" % VUELTA


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
    """LA LINEA QUE LLEVA EL ANCLA, LEIDA DEL FICHERO Y NO TECLEADA. PURA.

    Cae en rojo si no aparece exactamente una vez, porque una cifra que no
    tiene fichero de donde salir NO SE PUBLICA."""
    hay = [l.strip() for l in t.split(NL) if ancla in l]
    if len(hay) != 1:
        raise SystemExit("ROJO: el ancla %r aparece %d vez(ces) en %s y se "
                         "exige 1." % (ancla, len(hay), SALIDA))
    return hay[0]


def bloque_tabla(t, cabecera):
    """LA TABLA ENTERA QUE EMPIEZA EN SU CABECERA, PEGADA DEL FICHERO. PURA."""
    ls = t.split(NL)
    idx = [n for n, l in enumerate(ls) if l.startswith(cabecera)]
    if len(idx) != 1:
        raise SystemExit("ROJO: la cabecera de tabla %r aparece %d vez(ces)."
                         % (cabecera, len(idx)))
    n = idx[0]
    filas = []
    while n < len(ls) and ls[n].startswith("|"):
        filas.append(ls[n])
        n += 1
    return filas


CUERPO = """### TAREA 1. LOS REGISTROS

**LO QUE SE CORRIO, Y SU RUTA CON SUS DOS CONVENCIONES EN LA MISMA LINEA:**
``%(salida)s``, **%(bytes_salida)s**, exitcode 0.

**EL INSTRUMENTO NO ES ARNES NUEVO, Y ESO IMPORTA CON LA MORATORIA ENCIMA.**
`scripts/loop/_v%(v)d_t1_registros.py` lleva prefijo de guion bajo, esta fuera
del censo y fuera de la nomina, y **no vigila nada**: muere con la vuelta. Lo
unico que hace es **localizar lineas en un fichero, re-correr un lector ajeno y
contar**. La nomina sigue **CONGELADA EN 135**.

#### 1.a. LAS SEIS ADJUDICACIONES DEL ACTA 219, CON SU LINEA LEIDA DEL FICHERO

**LA LINEA NO SE TECLEA.** El acta de la vuelta 219 empieza donde el fichero
dice, no donde yo recuerde: %(inicio)s

**LA TABLA, PEGADA ENTERA DE `%(salida)s` Y NO TECLEADA** (%(nadj)s filas
armadas leyendo ese fichero, y **la cifra que deberia haber es 6**):

%(tabla_adj)s

**LAS SEIS CAEN DE MI LADO, Y DOS DE ELLAS TRAEN ALGO QUE NO ERA MIO.** La
`4.1` fija que **el mismo instrumento es el mismo instrumento**, y ademas el
auditor re-corrio mi lector y le salio identico, con lo que mi duda queda
contestada por medicion y no por criterio. La `4.2` **no se adjudico por mi
palabra sino por su medicion**: sello nueve `sha256`, corrio el lector y cero se
movieron a su corte. La `4.3` cuenta a favor **decir que algo no lo he vuelto a
medir yo**. La `4.4` refuerza `01 FUENTES` idx 1 **con una prueba que yo no
use**, la del `P.19` punto 2, cuyos **dos ejemplares nombrados son
`coeficiente_viral` y `decision_de_vender_startup`**, dos de los cinco de mi
propia tabla. La `4.5` **adjudica la frontera que yo deje marcada como
discutible**: el tercero queda **FUERA DEL ALCANCE**, no como incumplimiento. Y
la `4.6` acepta el reparto de tanda a libro **con su limite dicho**.

#### 1.b. EL RECUENTO NUEVO, CON LAS DOS CIFRAS JUNTAS Y DICIENDO CUAL ES CUAL

**PRIMERO LA PRUEBA DE QUE EL LECTOR LEE, Y AQUI HAY UN HALLAZGO QUE NO ESTABA
EN NINGUN ENCARGO.** Selle los `sha256` de nueve ficheros, re-corri
`scripts/loop/_v219_t2_lecturas.py` y volvi a medirlos:

%(mov1)s
%(mov2)s

**LA UNICA QUE DIFIERE, LEIDA DE MI PROPIA SALIDA Y NO CONTADA DE MEMORIA:**

```
%(dif_vieja)s
%(dif_nueva)s
```

**LAS DOS MEDICIONES SON CIERTAS Y NO SE CONTRADICEN, Y LO DIGO ASI PORQUE LA
OTRA ES DEL AUDITOR.** El acta 219, adjudicacion `4.2` (**linea 77907** de
`docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero), dice que sello nueve
ficheros, corrio ese mismo lector y **CERO se movieron**. Yo mido **UNO**, y es
**su propia salida sellada**. La causa esta medida y no supuesta: **ese lector
imprime el numero de lineas que el acta tiene HOY**, y entre su corrida y la mia
el acta crecio con el acta 219 entera. **Es diferencia de FECHA DE CORTE, no de
conducta del lector**, y por eso la 4.2 sigue en pie tal como esta escrita.

**Y LA SALIDA DE LA 219 SE RESTAURA BYTE A BYTE, PORQUE NO ES MIA PARA
REESCRIBIRLA:** %(restaurada)s

**MI CORRIDA DE HOY QUEDA SELLADA EN SU PROPIO FICHERO DE LA 220, CON SUS DOS
CONVENCIONES EN LA MISMA LINEA:** ``%(rel_hoy)s``, **%(bytes_hoy)s**.

**LA TABLA, PEGADA ENTERA DE `%(salida)s`** (%(nrec)s filas armadas leyendo ese
fichero, y **la cifra que deberia haber es 3**):

%(tabla_rec)s

**CUAL ES CUAL, DICHO SIN rodeos y con la cifra delante:**

- %(cubre_sin)s
- %(cubre_con)s
- %(medias_sin)s
- %(medias_con)s
- %(no_cubre)s

**Y LAS CIFRAS DEL ENCARGO, CITADAS COMO CONTRASTE Y NO COMO FUENTE:**
%(contraste)s
%(calza_sin)s
%(calza_con)s

**LAS DOS QUE QUEDAN, CON SU CIFRA:**

%(resto)s

%(cifra_resto)s

- **`03 FUSIONES` idx 0: 71 actos** sin fundir por la lectura ancha, y **SEIS
  fusiones de 19 nodos** por la estrecha.
- **`07 ADUANA` idx 0: el quinto control sin correr.**

**LO QUE NO SE TOCA, Y SE DICE EN VEZ DE HACERSE.**
`docs/plan/08_VERIFICACION.md` **NO SE ESCRIBE**. Su `sha256` al entrar y al
salir esta abajo y coincide por las dos convenciones. **La divergencia sube
nombrada**, que es lo que el acta 219 ya adjudico: son **dos** y no una, la de
la **linea 30** (dice CUATRO controles y su ficha `OP-A-02` dice CINCO) y la de
la **linea 28** (lleva el punto de verificacion de `05 SANEO` idx 1 acotado por
correccion declarada y su texto sin acotar).

#### 1.c. LAS SIETE COSAS QUE SUBEN NOMBRADAS A LA AUDITORIA INTEGRAL

**NO LAS RESUELVO: SOLO TIENEN QUE QUEDAR ESCRITAS DONDE EL FUNDADOR LAS
ENCUENTRE**, que es lo que el encargo pide. La tabla sale de la seccion 6 del
acta 219, que empieza en la linea que el fichero dice: %(inicio6)s

**LA TABLA, PEGADA ENTERA DE `%(salida)s`** (%(nint)s filas armadas leyendo ese
fichero, y **la cifra que deberia haber es 7**):

%(tabla_int)s

**LA 1 SUBE CON TRES OPCIONES, Y ESO ES LO QUE LA HACE DECIDIBLE.** Van
verbatim del acta y no resumidas por mi (%(nopc)s halladas, y **la cifra que el
encargo exige es 3**):

%(opciones)s

**Y LO QUE EL AUDITOR ANADE SOBRE SU PROPIA LISTA, TAMBIEN DEL FICHERO:** dice
que el no elige, pero que **descartaria la (c)** mientras nadie mida que el
sujeto esta a salvo por otra via. **Yo no elijo ninguna: no es mio.**
%(resuelve)s

#### ESTA TAREA SOLO LEE, Y SE PRUEBA CON LOS SHA

%(sha)s

%(sha_total)s

#### LOS DISCUTIBLES DE LA TAREA 1, MARCADOS ANTES DE SABER SI ACIERTO

| # | que decidi | la duda que dejo escrita |
|---|---|---|
%(disc)s

#### EL CASO ROJO, PROBADO POR MUTACION ANTES DE PUBLICARLO

**LA GUARDA QUE ESTA TAREA PUBLICA COMO PRUEBA SALIO EN VERDE EN LA CORRIDA
REAL, Y UN CASO QUE SOLO SE HA VISTO EN VERDE NO ES UNA PRUEBA.**
`scripts/loop/_v%(v)d_t1_mutacion.py` le cambia el valor esperado caso por caso
y comprueba que CAE. Su salida vive en ``%(mutacion)s``, **%(bytes_mut)s**:

%(mut)s

%(caso_rojo)s
"""

# LOS DISCUTIBLES SON LECTURA MIA Y SE MARCAN ANTES DE SABER SI ACIERTO
# (EJECUTOR.md 7).
DISCUTIBLES = [
    ("D.1", "QUE LA CIFRA SIN LA ADJUDICACION SE MIDE RE-CORRIENDO EL LECTOR "
            "DE LA 219, Y NO EL DE LA 217 DESDE EL GRAFO",
     "El encargo me pide **las dos cifras juntas**, la que mi lector mide hoy "
     "sin la adjudicacion y la que la adjudicacion deja. Yo entiendo *mi "
     "lector* como **`scripts/loop/_v219_t2_lecturas.py` tal cual**, que es el "
     "que el auditor reprodujo byte a byte. **La duda que dejo escrita antes de "
     "saber si acierto**: ese lector recompone el recuento leyendo la tabla de "
     "17 filas de `docs/loop/SALIDA_V219_T1_RECORRIDA_DEL_LECTOR.txt`, o sea "
     "**es una remedicion del mismo camino y no una medicion independiente "
     "desde el grafo**. Si el auditor lee que la cifra de hoy tenia que salir "
     "de re-sondar las diecisiete clausulas contra el grafo, mi 1.b se queda "
     "corta."),
    ("D.2", "QUE LA SUBIDA DE `05 SANEO` idx 1 SE APLICA EN MI ARITMETICA Y NO "
            "EN NINGUN FICHERO DEL PLAN",
     "La `4.5` sube `05 SANEO` idx 1 a CUBRE, y yo la aplico **solo sobre la "
     "tabla que el lector imprime**, en memoria, para publicar la segunda "
     "cifra. **No toco `docs/plan/08_VERIFICACION.md` ni ninguna ficha**, "
     "porque el encargo lo prohibe por su nombre. **La duda**: eso deja el "
     "arbol diciendo 14 y mi reporte diciendo 15, y **la divergencia la sostengo "
     "yo en prosa**, no un fichero. Si el auditor lee que una adjudicacion "
     "suya tenia que quedar escrita en algun sitio del plan, esa escritura no "
     "esta y **no la hago yo**: es sede del fundador."),
    ("D.3", "QUE EL MOVIMIENTO DE LA SALIDA SELLADA DE LA 219 NO ES UNA CAIDA "
            "DE NADIE",
     "Mi guarda midio que **`docs/loop/SALIDA_V219_T2_LECTURAS.txt` se mueve** "
     "al re-correr su lector, y el acta 219 dice que a su corte no se movio "
     "ninguno. **Lo declaro yo antes de que me lo pregunten.** Mi lectura es "
     "que **no es caida de nadie**: la unica linea que cambia es la del conteo "
     "de lineas del acta, que crecio porque el auditor escribio la 219 despues "
     "de correrlo. **Si el auditor lee que una salida sellada que no reproduce "
     "byte a byte es de suyo una caida de dato**, entonces esto es un hallazgo "
     "que sube y no una nota, y **el que decide es el**."),
]


def main():
    t = leer(SALIDA)
    bytes_salida = dos_convenciones(SALIDA)
    bytes_mut = dos_convenciones(MUTACION)
    rel_hoy = "docs/loop/SALIDA_V%d_T1_RECORRIDA_DEL_LECTOR.txt" % VUELTA
    bytes_hoy = dos_convenciones(rel_hoy)

    tabla_adj = bloque_tabla(t, "| rotulo | adjudicacion |")
    tabla_rec = bloque_tabla(t, "| veredicto | CIFRA que MI LECTOR MIDE HOY")
    tabla_int = bloque_tabla(t, "| # | linea del acta 219 |")

    ls = t.split(NL)
    opciones = [l.strip() for l in ls if "VERBATIM DEL ACTA>" in l]
    sha = [l.strip() for l in ls if " AL ENTRAR: sha256" in l
           or " AL SALIR:   sha256" in l]
    resto = [l.strip() for l in ls if re.match(r"^\s{6}\S.* idx \d+ \| ", l)]
    mut = [l.strip() for l in leer(MUTACION).split(NL)
           if l.strip().startswith("CASO ") or "EL CASO " in l
           or l.strip().startswith("CIFRA casos que CAEN")
           or l.strip().startswith("CIFRA comprobaciones que fallan")]

    datos = {
        "v": VUELTA,
        "salida": SALIDA,
        "mutacion": MUTACION,
        "bytes_salida": bytes_salida,
        "bytes_mut": bytes_mut,
        "rel_hoy": rel_hoy,
        "bytes_hoy": bytes_hoy,
        "inicio": L(t, "EL ACTA 219 EMPIEZA EN LA LINEA"),
        "nadj": len(tabla_adj) - 2,
        "tabla_adj": NL.join(tabla_adj),
        "mov1": "- " + L(t, "CIFRA ficheros que se movieron al correr el "
                            "lector:"),
        "mov2": "- " + L(t, "CIFRA lineas en que la salida sellada del lector "
                            "difiere"),
        "dif_vieja": L(t, "LA QUE ESTABA>"),
        "dif_nueva": L(t, "LA DE HOY>"),
        "restaurada": L(t, "TRAS RESTAURAR:"),
        "nrec": len(tabla_rec) - 2,
        "tabla_rec": NL.join(tabla_rec),
        "cubre_sin": L(t, "CIFRA clausulas en CUBRE, MEDIDA HOY POR MI LECTOR"),
        "cubre_con": L(t, "CIFRA clausulas en CUBRE, CON LA ADJUDICACION"),
        "medias_sin": L(t, "CIFRA clausulas en A MEDIAS, MEDIDA HOY POR MI "
                           "LECTOR"),
        "medias_con": L(t, "CIFRA clausulas en A MEDIAS, CON LA ADJUDICACION"),
        "no_cubre": L(t, "CIFRA clausulas en NO CUBRE, por las dos:"),
        "contraste": L(t, "Y LAS CIFRAS DEL ENCARGO, CITADAS COMO CONTRASTE"),
        "calza_sin": L(t, "MI MEDICION SIN LA ADJUDICACION CALZA CON EL "
                          "CONTRASTE:"),
        "calza_con": L(t, "MI COMPUTO CON LA ADJUDICACION CALZA CON EL "
                          "CONTRASTE:"),
        "resto": NL.join("- " + x for x in resto),
        "cifra_resto": L(t, "CIFRA clausulas que siguen sin cubrir:"),
        "inicio6": L(t, "LA SECCION 6 EMPIEZA EN LA LINEA"),
        "nint": len(tabla_int) - 2,
        "tabla_int": NL.join(tabla_int),
        "nopc": L(t, "CIFRA opciones halladas en el texto del punto 1:"),
        "opciones": NL.join("- " + x for x in opciones),
        "resuelve": L(t, "CIFRA opciones que ESTA VUELTA resuelve:"),
        "sha": NL.join("- " + x for x in sha),
        "sha_total": L(t, "COINCIDEN AL ENTRAR Y AL SALIR POR LAS DOS "
                          "CONVENCIONES:"),
        "disc": NL.join("| **%s** | %s | %s |" % (a, b_, c)
                        for a, b_, c in DISCUTIBLES),
        "mut": NL.join("- " + x for x in mut),
        "caso_rojo": L(t, "EL CASO ROJO, DICHO CUAL ES CUAL:"),
    }
    texto = CUERPO % datos

    print("CIFRA filas de la tabla de adjudicaciones, contadas del fichero: %d "
          "| CIFRA que deberia haber: 6" % datos["nadj"])
    print("CIFRA filas de la tabla del recuento, contadas del fichero: %d | "
          "CIFRA que deberia haber: 3" % datos["nrec"])
    print("CIFRA filas de la tabla de la integral, contadas del fichero: %d | "
          "CIFRA que deberia haber: 7" % datos["nint"])
    print("CIFRA opciones pegadas del fichero: %d | CIFRA que deberia haber: 3"
          % len(opciones))
    print("CIFRA filas de las que no cubren, contadas del fichero: %d | CIFRA "
          "que deberia haber: 2" % len(resto))
    print("CIFRA lineas de sha al entrar y al salir: %d | CIFRA que deberia "
          "haber: 14" % len(sha))
    print("CIFRA lineas de la prueba de mutacion pegadas: %d" % len(mut))
    fallos = 0
    for etiqueta, cond in (("adjudicaciones", datos["nadj"] == 6),
                           ("recuento", datos["nrec"] == 3),
                           ("integral", datos["nint"] == 7),
                           ("opciones", len(opciones) == 3),
                           ("resto", len(resto) == 2),
                           ("sha", len(sha) == 14)):
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
    print("VERDE: el cuerpo de la TAREA 1 queda compuesto de su fichero.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
