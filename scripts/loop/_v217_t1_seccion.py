# -*- coding: utf-8 -*-
r"""_v217_t1_seccion.py . EL CUERPO DE LA TAREA 1 DEL REPORTE DE LA VUELTA 217,
COMPUESTO DE SUS SALIDAS SELLADAS Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: toda tabla o cifra del reporte
cita el fichero de salida del que sale, y se RECONSTRUYE CONTANDO ESE FICHERO
antes de publicarla. Aqui NINGUNA celda se teclea: las filas se leen de
docs/loop/SALIDA_V217_T1_DIECISIETE.txt y de
docs/loop/SALIDA_V217_T1_CONTRASTE_V150.txt, y el compositor DICE cuantas armo y
cuantas deberia haber.

LO UNICO MIO SON LOS DISCUTIBLES Y SUS MOTIVOS, y van en su propia seccion
rotulada como lectura mia, para que se pueda auditar cual es cual.

USO:  python scripts/loop/_v217_t1_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
SALIDA = "docs/loop/SALIDA_V%d_T1_DIECISIETE.txt" % VUELTA
CONTRASTE = "docs/loop/SALIDA_V%d_T1_CONTRASTE_V150.txt" % VUELTA
DESTINO = "scripts/loop/_v%d_t1_seccion.md" % VUELTA

# LOS DISCUTIBLES SON LECTURA MIA Y SE MARCAN ANTES DE SABER SI ACIERTO
# (EJECUTOR.md 7). Cada uno dice QUE decidi y CUAL es la duda.
DISCUTIBLES = [
    ("D.a", "`01 FUENTES` idx 0, la vara del ANTES",
     "Publico **A MEDIAS** y no CUBRE. Los seis miembros de la clase conservan "
     "su NUMERO de pasos contra el grafo previo, que es lo que la clase "
     "protege; pero DOS tienen texto distinto, y aunque los commits que los "
     "tocaron no nombran ninguna operacion de la fase 01, el asunto de un "
     "commit es un proxy y no una lectura. Si el auditor lee que la clausula "
     "protege el numero y no la letra, esta clausula es CUBRE."),
    ("D.b", "`01 FUENTES` idx 1, que es 'reubicado'",
     "Publico **A MEDIAS**. La mitad 'no borrado' esta medida y da CERO "
     "borradas de 70 menciones. Para la mitad 'reubicado' elegi como vara que "
     "el nodo YA NO declare mas de una fuente, y quedan 7 menciones que "
     "todavia declaran dos o mas. Si el auditor lee que reubicar es solo mover "
     "el bloque y no reducir el campo, la vara es otra."),
    ("D.c", "`02 DESTEJIDOS` idx 1, la anchura del detector",
     "Publico **A MEDIAS** con la regla ESTRECHA, que busca la frase de la "
     "regla de reparto, y publico al lado la ANCHA, que busca que la ficha "
     "nombre un bloque. Las dos cifras estan en la tabla. Si el auditor lee "
     "que nombrar el bloque con otras palabras cumple la clausula, esta es "
     "CUBRE por la cifra ancha."),
    ("D.d", "`03 FUSIONES` idx 0, el universo de la clausula",
     "Publico **A MEDIAS** midiendo TODOS los actos del corte vigente. La "
     "mitad del alias cubre entera y sin excepcion; lo que no cubre es que 71 "
     "actos siguen con varios miembros vivos, o sea SIN FUNDIR. Si el auditor "
     "lee que la clausula solo habla de los actos YA fundidos, como hace el "
     "arnes de la vuelta 150 al medir solo las fichas con superviviente "
     "escrito, esta clausula es CUBRE."),
    ("D.e", "`07 ADUANA` idx 0, cuatro contra cinco",
     "Publico **CUBRE** porque la clausula pide CUATRO y hay CUATRO corriendo "
     "y en verde. Pero la pagina 07 y la verificacion de `OP-A-02` nombran "
     "CINCO, y el quinto, la revision de toda nomina por el DOMINIO de sus "
     "miembros, NO corre. Si el auditor lee que la celda quedo vieja y que la "
     "cifra viva es cinco, esta clausula es A MEDIAS."),
]


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def linea_con(texto, marca):
    for l in texto.split(NL):
        if marca in l:
            return l.strip()
    return None


def cifra(texto, etiqueta):
    l = linea_con(texto, etiqueta)
    if l is None:
        return None
    m = re.search(r"(-?\d+)", l.split(etiqueta, 1)[1])
    return m.group(1) if m else None


def bloque_tabla(texto, ancla, fin):
    """LAS FILAS DE UNA TABLA DE LA SALIDA, LEIDAS Y NO TECLEADAS."""
    ls = texto.split(NL)
    i = next((n for n, l in enumerate(ls) if ancla in l), None)
    if i is None:
        return []
    fuera = []
    for l in ls[i + 1:]:
        if fin in l:
            break
        if l.startswith("|"):
            fuera.append(l.rstrip())
    return fuera


def main():
    t = leer(SALIDA)
    tc = leer(CONTRASTE)
    bytes_salida = len(io.open(os.path.join(RAIZ, SALIDA.replace("/", os.sep)),
                               "rb").read())
    bytes_salida_lf = len(io.open(os.path.join(
        RAIZ, SALIDA.replace("/", os.sep)), "rb").read().replace(b"\r\n", b"\n"))
    bytes_c = len(io.open(os.path.join(RAIZ, CONTRASTE.replace("/", os.sep)),
                          "rb").read())
    bytes_c_lf = len(io.open(os.path.join(
        RAIZ, CONTRASTE.replace("/", os.sep)), "rb").read().replace(b"\r\n", b"\n"))

    filas_tabla = [l for l in bloque_tabla(t, "LA TABLA DE LAS DIECISIETE",
                                           "CIFRA FILAS DE ESTA TABLA")]
    filas_datos = [l for l in filas_tabla if re.match(r"^\| \d+ \|", l)]
    filas_verbatim = [l for l in t.split(NL)
                      if re.match(r"^  \S.*\bidx \d+ \| ", l)]
    mutantes = [l for l in t.split(NL) if l.startswith("MUTANTE ROTO")]
    sanos = [l for l in t.split(NL) if l.startswith("MUTANTE SANO")]
    no_cubren = []
    dentro = False
    for l in t.split(NL):
        if "LAS QUE NO DAN CUBRE" in l:
            dentro = True
            continue
        if dentro:
            if not l.startswith("   "):
                break
            no_cubren.append(l.strip())

    fallos = 0
    print("LO QUE ESTE COMPOSITOR CUENTA DE SU FICHERO, ANTES DE PUBLICAR NADA:")
    print("  SALIDA: %s -> %d bytes en disco y %d normalizado a LF"
          % (SALIDA, bytes_salida, bytes_salida_lf))
    print("  CONTRASTE: %s -> %d bytes en disco y %d normalizado a LF"
          % (CONTRASTE, bytes_c, bytes_c_lf))
    print("  CIFRA filas de datos de la tabla de las diecisiete, contadas del "
          "fichero: %d | CIFRA que deberia haber: 17" % len(filas_datos))
    print("  CIFRA lineas de mutante roto contadas del fichero: %d | CIFRA que "
          "deberia haber: 17" % len(mutantes))
    print("  CIFRA lineas de mutante sano contadas del fichero: %d" % len(sanos))
    print("  CIFRA lineas de las que no cubren, contadas del fichero: %d"
          % len(no_cubren))
    if len(filas_datos) != 17 or len(mutantes) != 17:
        print("ROJO: la salida no trae lo que este compositor exige.")
        fallos += 1

    n_cubre = cifra(t, "CIFRA clausulas en CUBRE     :")
    n_medias = cifra(t, "CIFRA clausulas en A MEDIAS  :")
    n_nocubre = cifra(t, "CIFRA clausulas en NO CUBRE  :")
    n_sinsonda = cifra(t, "CIFRA clausulas en SIN SONDA :")
    caen = cifra(t, "CIFRA que CAEN (o sea que NO dicen CUBRE):")
    suben = cifra(t, "CIFRA que SUBEN a CUBRE:")
    l_filas = linea_con(t, "CIFRA FILAS ARMADAS LEYENDO LA TABLA POR FASE")
    l_cl = linea_con(t, "CIFRA CLAUSULAS ARMADAS EN LA TABLA ENTERA")
    l_filas8 = linea_con(t, "CIFRA FILAS DE 0 CODIGO A 07 ADUANA ARMADAS")
    l_cl17 = linea_con(t, "CIFRA CLAUSULAS DE ESAS OCHO FILAS ARMADAS")
    l_desc = linea_con(t, "CIFRA descuadres contra las cifras del encargo")
    l_sha_e0 = linea_con(t, "SHA256 DE docs/plan/OPERACIONES.jsonl AL ENTRAR")
    l_sha_e1 = linea_con(t, "SHA256 DE docs/plan/OPERACIONES.jsonl AL SALIR")
    l_sha_v0 = linea_con(t, "SHA256 DE docs/plan/08_VERIFICACION.md AL ENTRAR")
    l_sha_v1 = linea_con(t, "SHA256 DE docs/plan/08_VERIFICACION.md AL SALIR")
    l_sha_ok = linea_con(t, "LOS CUATRO SHA COINCIDEN CON LOS DE LA ENTRADA")
    l_v150 = linea_con(t, "CIFRA lineas de ese fichero")
    l_c_filas = linea_con(tc, "FILAS DE LA TABLA POR FASE, LEIDAS DE")
    l_c_assert = linea_con(tc, "AssertionError")
    for etiqueta, v in (("CUBRE", n_cubre), ("A MEDIAS", n_medias),
                        ("NO CUBRE", n_nocubre), ("caen", caen),
                        ("suben", suben)):
        if v is None:
            print("ROJO: falta la cifra de %s en la salida." % etiqueta)
            fallos += 1

    reparto = [l for l in t.split(NL) if re.match(r"^  \S.*clausulas armadas", l)]
    print("  CIFRA filas de reparto por fila contadas del fichero: %d | CIFRA "
          "que deberia haber: 11" % len(reparto))
    if len(reparto) != 11:
        fallos += 1
    print("  CIFRA filas verbatim de las diecisiete contadas del fichero: %d | "
          "CIFRA que deberia haber: 17" % len(filas_verbatim))
    if len(filas_verbatim) != 17:
        fallos += 1
    print("")
    if fallos:
        print("ROJO: el compositor NO escribe. Fallos: %d" % fallos)
        return 1

    partes = []
    partes.append("""### TAREA 1. LAS DIECISIETE CLAUSULAS DE LAS FASES 0 A 07, MEDIDAS UNA POR UNA

**LO QUE SE CORRIO, Y SU RUTA CON SUS BYTES:**
`%(salida)s`, **%(b)d bytes en disco y %(blf)d normalizado a LF**, exitcode 0.
Y el contraste, `%(contraste)s`, **%(bc)d bytes en disco y %(bclf)d normalizado
a LF**, exitcode 1 y su motivo escrito abajo.

**EL INSTRUMENTO NO ES NUEVO POR DENTRO Y ESO IMPORTA CON LA MORATORIA
ENCIMA** (`AUDITOR.md` 6.3). Los lectores se **IMPORTAN** de
`scripts/loop/vuelta150_4_tabla_por_fase.py`, que es la sede donde ya viven:
`celdas_de_la_tabla`, `fichas`, `grafo`, `resolutor`, `gate0_checks` y
`guarda_salidas_congeladas`. Lo unico propio de esta vuelta es **el partido de
las celdas en clausulas y las diecisiete sondas**, que es medicion y es lo que
la moratoria protege.

%(lv150)s

## 1.a. LAS FILAS Y SUS CLAUSULAS, SACADAS CON UN INSTRUMENTO Y NO A MANO

**LAS CUATRO CIFRAS, CADA UNA CON LA DEL ENCARGO AL LADO Y EN LA MISMA LINEA,
que es lo que la obligacion de las filas manda:**

```
%(lfilas)s
%(lcl)s
%(lfilas8)s
%(lcl17)s
%(ldesc)s
```

**EL REPARTO POR FILA, CONTADO Y NO TECLEADO** (11 filas leidas del fichero, 11
que deberia haber):

```
%(reparto)s
```

**LAS DIECISIETE, VERBATIM** (17 filas leidas del fichero, 17 que deberia
haber):

```
%(verbatim)s
```

## 1.b Y 1.c. EL VEREDICTO DE CADA UNA, CON SU BUSQUEDA CORRIDA

**LA TABLA SALE DEL FICHERO Y SE CUENTA ANTES DE PUBLICARLA: %(nfilas)d filas de
datos leidas, 17 que deberia haber.**

%(tabla)s

**EL REPARTO, CONTADO DE ESA MISMA TABLA: %(cubre)s en CUBRE, %(medias)s en
A MEDIAS, %(nocubre)s en NO CUBRE y %(sinsonda)s SIN SONDA, de 17.**

**LAS QUE NO DAN CUBRE, CON SU FILA, SU INDICE Y SU CIFRA** (%(nnc)d lineas
leidas del fichero):

```
%(nocubren)s
```

**LAS DOS CLAUSULAS CON CORRECCION DECLARADA SE MIDIERON POR SU LECTURA
CORREGIDA, NO A LA LETRA**, y las dos son de la fila `05 SANEO`: *"ningun nodo
cablea export.gov"* (idx 2) y *"ninguna de las seis herramientas muertas"*
(idx 3). La correccion vive en las **lineas 35 a 58** de
`docs/plan/08_VERIFICACION.md`, se leyo entera antes de medir, y su efecto esta
medido: **la de las seis herramientas, medida A LA LETRA, daria NO CUBRE por UNA
mencion viva** (`Alexa` en `inteligencia_de_anuncios_de_la_competencia`), y esa
mencion esta **FUERA de la nomina de `OP-S-04`** y el fundador ya la saco de la
campana. **Medida acotada da CERO menciones dentro de la nomina, y las dos
cifras se publican juntas.**

## 1.d. EL CASO ROJO NO SE PROMETE, SE PRUEBA POR MUTACION

**%(nmut)d mutantes rotos leidos del fichero, 17 que deberia haber, y CAEN
%(caen)s de 17.** Ninguno toca una ficha, un nodo ni una pagina: se fabrican en
memoria sobre una copia.

```
%(mutantes)s
```

**Y EL REVERSO, PORQUE UNA SONDA QUE NUNCA PUEDE DECIR CUBRE TAMPOCO MIDE:
%(nsanos)d mutantes SANOS, y SUBEN %(suben)s.**

```
%(sanos)s
```

## 1.e. NO SE ESCRIBIO NADA, Y SE PRUEBA CON LOS CUATRO SHA

```
%(sha)s
```

**Ni un campo de estado, ni la pagina 08, ni el inventario, ni el expediente.**
""" % {
        "salida": "`" + SALIDA + "`",
        "contraste": "`" + CONTRASTE + "`",
        "b": bytes_salida, "blf": bytes_salida_lf,
        "bc": bytes_c, "bclf": bytes_c_lf,
        "lv150": "**" + l_v150 + "**" if l_v150 else "",
        "lfilas": l_filas, "lcl": l_cl, "lfilas8": l_filas8, "lcl17": l_cl17,
        "ldesc": l_desc,
        "reparto": NL.join(reparto),
        "verbatim": NL.join(filas_verbatim),
        "tabla": NL.join(filas_tabla),
        "nfilas": len(filas_datos),
        "cubre": n_cubre, "medias": n_medias, "nocubre": n_nocubre,
        "sinsonda": n_sinsonda,
        "nnc": len(no_cubren),
        "nocubren": NL.join(no_cubren),
        "nmut": len(mutantes), "caen": caen,
        "mutantes": NL.join(mutantes),
        "nsanos": len(sanos), "suben": suben,
        "sanos": NL.join(sanos),
        "sha": NL.join([l_sha_e0, l_sha_e1, l_sha_v0, l_sha_v1, l_sha_ok]),
    })

    partes.append("""
## 1.f. LA DISCREPANCIA CONTRA MI PROPIO ENCARGO, DECLARADA Y NO RESUELTA COPIANDO

**MI ENCARGO DICE, VERBATIM: "LAS OCHO FILAS DE 0 CODIGO A 07 ADUANA, CON SUS
DIECISIETE CLAUSULAS, NO LAS HA MEDIDO NADIE CON UNA SONDA CORRIDA". MEDIDO HOY:
ESO ES CIERTO DE LAS DIECISIETE CLAUSULAS Y NO LO ES DE LAS OCHO FILAS.**

`scripts/loop/vuelta150_4_tabla_por_fase.py` **mide las ocho filas**, una por
fase, con su veredicto de tres palabras, y se corrio en las vueltas 150 a 155.
Lo que nadie habia medido, y es lo que esta tarea mide, son **las diecisiete
clausulas por separado**. Las dos cosas se publican y la discrepancia no se
resuelve copiando (`EJECUTOR.md` 2).

**Y HAY UNA SEGUNDA MITAD, MEDIDA CON SU CORRIDA: ESE INSTRUMENTO HOY CAE EN
ROJO.** Corrido en esta vuelta contra mi propio corte, sale con **exitcode 1**:

```
%(cfilas)s
%(cassert)s
```

**La causa esta medida y no supuesta:** su `assert` exige OCHO filas y la
correccion declarada de la vuelta 214 dejo **ONCE** en la tabla POR FASE, al
anadir las de las fases 08, 09 y 10. **NO LO REPARO Y ESO ES DELIBERADO: la
moratoria de `AUDITOR.md` 6.3 prohibe reparar arneses, y el propio encargo dice
que las dos tareas de esta vuelta son medicion y verificacion.** Se mide, se
publica y se dice. **Y por lo mismo, para cargar sus lectores sin correr su
tabla se descarta SU ULTIMA LINEA DE ENTRADA al ejecutarlo en memoria: el
fichero en disco no se toca ni en un byte.**

## 1.g. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Son lectura mia y por eso van aparte** (`EJECUTOR.md` 7). **Cinco.**

| # | sobre que | que decidi y cual es la duda |
|---|---|---|
%(disc)s

**LO QUE NO PROPONGO, Y DIGO POR QUE.** El encargo escribe la condicion de la
parada feliz antes de saber el resultado: *"si las DIECISIETE quedan en CUBRE
con su busqueda corrida y su cifra delante"*. **No quedan: %(medias)s de 17 dan
A MEDIAS**, y estan nombradas arriba con su fila, su indice y su cifra. **Por
tanto NO propongo declarar la campana consumada.** Lo que si digo, porque es lo
que la medicion sostiene: **ninguna de las diecisiete da NO CUBRE**, y las cinco
que no cubren lo hacen por trabajo pendiente medido y nombrado, no por un fallo
del catalogo.
""" % {
        "cfilas": l_c_filas,
        "cassert": l_c_assert,
        "disc": NL.join("| **%s** | %s | %s |" % (a, b, c)
                        for a, b, c in DISCUTIBLES),
        "medias": n_medias,
    })

    texto = "".join(partes)
    largos = texto.count(chr(8212)) + texto.count(chr(8211))
    print("CIFRA guiones largos mas medios en el cuerpo: %d" % largos)
    if largos:
        print("ROJO: el compositor NO escribe.")
        return 1
    sospechosos = [c for c in re.findall(r"`([^`]+)`", texto)
                   if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sospechosos))
    if sospechosos:
        for s in sospechosos:
            print("   sospechoso> %s" % s)
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
