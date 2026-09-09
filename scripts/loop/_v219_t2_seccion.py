# -*- coding: utf-8 -*-
r"""_v219_t2_seccion.py . EL CUERPO DE LA TAREA 2 DEL REPORTE DE LA VUELTA 219,
COMPUESTO DE SU SALIDA SELLADA Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: ninguna celda se teclea. Las
filas se leen de docs/loop/SALIDA_V219_T2_LECTURAS.txt y el compositor DICE
cuantas armo y cuantas deberia haber.

LO UNICO MIO SON LOS DISCUTIBLES Y SUS MOTIVOS, y van en su propia seccion
rotulada como lectura mia, para que se pueda auditar cual es cual.

USO:  python scripts/loop/_v219_t2_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
SALIDA = "docs/loop/SALIDA_V%d_T2_LECTURAS.txt" % VUELTA
DESTINO = "scripts/loop/_v%d_t2_seccion.md" % VUELTA


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def L(t, ancla):
    hay = [l.strip() for l in t.split(NL) if ancla in l]
    if len(hay) != 1:
        raise SystemExit("ROJO: el ancla %r aparece %d vez(ces) en %s y se "
                         "exige 1." % (ancla, len(hay), SALIDA))
    return hay[0]


def bloque_tabla(t, cabecera):
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


DISCUTIBLES = [
    ("D.1", "QUE LA VARA DE REUBICADO ES LA DEL GRAFO Y NO LA DEL CAMPO `fuente`",
     "Subo `01 FUENTES` idx 1 a **CUBRE** aplicando la vara que la `4.5` del acta "
     "218 (**linea 77628** de `docs/loop/ACTA_AUDITOR.md`) fija: **reubicado es "
     "un hecho comprobable en el grafo, no una frase escrita en una ficha**, y "
     "el encargo la repite palabra por palabra. **Y digo antes de saber si "
     "acierto que la sonda del instrumento de la 217 sigue diciendo A MEDIAS "
     "por su propio detector**, que mira si el nodo dejo de declarar dos "
     "fuentes. **Las dos lecturas estan medidas y publicadas juntas arriba.** Si "
     "el auditor lee que *reubicado* exige que el material SALGA del nodo, "
     "entonces **cinco de las siete no lo estan** (las que `P.19` y `P.20` "
     "fundieron dentro dejando la fuente intacta a proposito) y **la clausula "
     "vuelve a A MEDIAS**. Mi motivo para leerlo al reves es que `P.19` punto 2 "
     "**obliga** a dejar la fuente intacta cuando el material se funde dentro, "
     "asi que **el campo `fuente` sin tocar es la senal de la operacion hecha, "
     "no la de la operacion pendiente**: castigarla seria medir contra una vara "
     "que la propia doctrina prohibe cumplir."),
    ("D.2", "QUE LA FRONTERA DE LA 2.b NO LA DECIDO, PERO SI DIGO COMO LA LEO",
     "El encargo me manda medir los tres, escribir mi lectura con su motivo y "
     "**marcarla**, y eso hago: **NO la aplico al recuento** y `05 SANEO` idx 1 "
     "se queda en **A MEDIAS sin mover**. **Como la leo yo:** el tercero queda "
     "**FUERA DEL ALCANCE** de la clausula, no como incumplimiento. **El motivo, "
     "y es una cita, no una opinion:** el acto literal de `OP-S-02` es *anadir "
     "version a una cita que ya existe*, y el superviviente del tercero **no "
     "tiene la cita**, porque la palabra se perdio en una fusion anterior por "
     "debajo de la granularidad del paso. Eso lo adjudico el acta 120 en su "
     "**linea 41699** y quedo anotado como trabajo post campana en la "
     "**linea 1574** de `docs/PENDIENTES.md`, las dos leidas hoy del fichero. "
     "**Y es la misma forma de razonar que el auditor uso en su `4.4`** (acta "
     "218, **linea 77614**): una clausula de verificacion verifica **lo que su "
     "operacion hizo**. **Si el auditor lee lo contrario**, que un diferido "
     "escrito sigue contando como incumplimiento mientras el nodo no lleve la "
     "version, **la clausula se queda en A MEDIAS para siempre** hasta que "
     "alguien ejecute el trabajo post campana, y eso conviene saberlo antes de "
     "medir la parada feliz contra ella."),
    ("D.3", "QUE EL REPARTO DE TANDA A LIBRO ES MIO",
     "La pregunta *cual es el segundo libro de esta mencion* la contesto yo con "
     "una tabla escrita a mano de seis entradas (`OP-F-02` a Mollick, `OP-F-03` "
     "a Hugos, y las cuatro de `OP-F-04` a Coleman, Horowitz, Weinberg y "
     "Rackham). **No se puede deducir del campo `fuente`**, y el propio "
     "`01_FUENTES.md` explica por que: un nodo que no se toco y uno fundido por "
     "`P.19` **se ven igual ahi**. **La guarda que le puse**: la propia ficha "
     "del expediente tiene que nombrar ese apellido en su texto, y las seis lo "
     "hacen. **Lo que esa guarda NO prueba** es que el apellido nombrado sea el "
     "de la tanda y no otro citado de pasada, **y eso lo digo yo en vez de "
     "dejar que parezca comprobado**."),
]

CUERPO = """### TAREA 2. LAS DOS CLAUSULAS QUE TODAVIA SE PUEDEN MOVER LEYENDO

**LO QUE SE CORRIO, Y SU RUTA CON SUS DOS CONVENCIONES EN LA MISMA LINEA:**
``%(salida)s``, **%(bytes_salida)s**, exitcode 0.

**ES LECTURA, NO INSTRUMENTO NUEVO.** `scripts/loop/_v%(v)d_t2_lecturas.py`
lleva prefijo de guion bajo, esta fuera del censo y fuera de la nomina, y muere
con la vuelta. **La sonda de la clausula NO SE CLONO: se IMPORTA** de
`scripts/loop/_v217_t1_diecisiete.py`, que es la que publico el 7, y el
resolutor viene por la misma via. **Las dos clausulas bloqueadas no se
intentaron**, que es lo que el encargo manda: `07 ADUANA` idx 0 depende de un
control que no corre y de una celda que es sede del fundador, y `03 FUSIONES`
idx 0 depende de ejecutar las SEIS fusiones enrutadas, que es trabajo de plan y
no de lectura.

**EL ESTADO DEL ARBOL, MEDIDO AL EMPEZAR LA TAREA:**
%(grafo)s
%(expediente)s

#### 2.a. `01 FUENTES` idx 1: EL MATERIAL DEL SEGUNDO LIBRO, REUBICADO O BORRADO

**PRIMERO LA CIFRA, REPRODUCIDA Y NO HEREDADA, QUE ES LO QUE EL ENCARGO PIDE
ANTES DE NADA:**

%(cifra7)s

**LAS DOS CIFRAS CALZAN, ASI QUE NO HAY PARADA POR AHI.** Y digo, porque
callarlo seria sesgo, que **la sonda por su propio detector estrecho sigue
diciendo `A MEDIAS`**: %(ver_sonda)s **Ese no es el detector que el encargo
manda usar**, y la vara que si es la de la `4.5` del acta 218 (**linea 77628**
de `docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero): **reubicado es un hecho
comprobable en el grafo, no una frase escrita en una ficha.**

**LA TABLA, PEGADA ENTERA DE `%(salida)s` Y NO TECLEADA** (%(n2a)s filas armadas
leyendo ese fichero, y **la cifra que deberia haber es 7**):

%(tabla_2a)s

**SEIS DE LAS SIETE VIVEN DENTRO DE SU PROPIO NODO, Y NO POR DESCUIDO: POR
DOCTRINA.** `P.19` punto 2 **obliga** a dejar el campo `fuente` intacto cuando
el material se funde dentro del nodo en vez de salir, y `01_FUENTES.md` lo dice
con todas las letras: *ahi la fuente se reduce porque el material se fue; aqui
el material se queda y solo deja de estar dicho dos veces*. **Los cinco nodos
que las alojan estan VIVOS, resueltos con el resolutor delante, y sus pasos de
hoy calzan uno a uno con la cifra que su propio registro publico** (23, 15, 8,
7 y 6).

**Y LA SEPTIMA ES LA UNICA QUE SE MUDO, Y ES LA QUE HABIA QUE COMPROBAR DE
VERDAD.** El bloque de Hugos de `principio_calidad_mvp`, tramo **11 a 14**, ya
no vive en el nodo que lo declaraba: su enrutamiento esta escrito en la
**linea 500** de `docs/plan/01_FUENTES.md` y su destino es
`ejecucion_incremental_transicion_tecnologica`. **No me creo el registro: lo
comprobe acto por acto contra los pasos del receptor**, y los cuatro estan:

%(actos)s

%(cifra_actos)s

**EL SALDO, Y LA VARA APLICADA SIN PROMEDIAR:**

%(saldo_2a)s

%(vara_2a)s

%(veredicto_2a)s

#### 2.b. `05 SANEO` idx 1: LOS TRES DE INCOTERMS CON SU VERSION

**LA ANOTACION DEL ACTA 120, LOCALIZADA Y CON SU LINEA LEIDA DEL FICHERO, QUE
ES LO QUE EL ENCARGO PIDE Y NO DE MEMORIA:**

%(acta120)s

%(adj120)s

**Y SU SEDE, PORQUE UNA ADJUDICACION QUE MANDA ANOTAR NO ES LA ANOTACION.** El
acta 120 dice que *la mitad que falta es LA ANOTACION, que la 120 no escribio, y
va como tarea de la 121*, y esa anotacion **existe y la localice**:

%(pend)s

%(pend_post)s

**LOS TRES DE LA NOMINA, LEIDOS DEL EXPEDIENTE Y NO TECLEADOS:**

%(sujeto)s
%(estado_ficha)s

**LA TABLA, PEGADA ENTERA DE `%(salida)s`** (%(n2b)s filas armadas leyendo ese
fichero, y **la cifra que deberia haber es 3**):

%(tabla_2b)s

%(cifra_2b)s

**LA PREGUNTA QUE DECIDE LA CLAUSULA ES DE FRONTERA Y NO DE CONTEO, Y NO LA
DECIDO YO.** Va entera al bloque de discutibles de abajo, con mi lectura y su
motivo, y **no se aplica al recuento**:

%(frontera)s

%(veredicto_2b)s

#### 2.c. EL RECUENTO DE LAS DIECISIETE, REHECHO AL CIERRE DE ESTA TAREA

**NO SE HEREDA** (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE). Las
17 filas salen de mi propia corrida de hoy, y la unica que esta tarea mueve es
la de `01 FUENTES` idx 1:

%(fuente17)s
%(nfilas17)s
%(reparto_t1)s
%(sube)s
%(mueve)s

**LAS TRES CIFRAS DEL CIERRE, CADA UNA CON LA QUE LA TAREA 1 DEJO AL LADO:**

%(cierre17)s

**LA TABLA ENTERA AL CIERRE DE ESTA TAREA, PEGADA DE `%(salida)s`**
(%(n17)s filas armadas leyendo ese fichero, y **la cifra que deberia haber es
17**):

%(tabla_17)s

**LAS QUE SIGUEN SIN CUBRIR, CON SU FILA, SU INDICE Y SU CIFRA:**

%(resto17)s

%(cifra_resto)s

#### 2.d. LA PARADA FELIZ: NO SE PROPONE, Y LA CONDICION NO LA PONGO YO

%(parada)s

#### ESTA TAREA SOLO LEE, Y SE PRUEBA CON LOS SHA

%(sha)s

%(sha_total)s

#### LOS DISCUTIBLES DE LA TAREA 2, MARCADOS ANTES DE SABER SI ACIERTO

| # | que decidi | la duda que dejo escrita |
|---|---|---|
%(disc)s

#### EL CASO ROJO, DICHO CUAL ES CUAL

%(caso_rojo)s
"""


def main():
    t = leer(SALIDA)
    p = os.path.join(RAIZ, SALIDA.replace("/", os.sep))
    b = io.open(p, "rb").read()
    bytes_salida = ("%d bytes en disco y %d normalizado a LF"
                    % (os.path.getsize(p), len(b.replace(b"\r\n", b"\n"))))

    tabla_2a = bloque_tabla(t, "| # | ficha | nodo que la declara |")
    tabla_2b = bloque_tabla(t, "| # | nodo de la nomina |")
    tabla_17 = bloque_tabla(t, "| # | fila | idx | veredicto |")

    ls = t.split(NL)
    cifra7 = [l.strip() for l in ls
              if l.strip().startswith("sonda> CIFRA menciones que TODAVIA")
              or l.strip().startswith("CIFRA menciones que TODAVIA declaran mas "
                                      "de una fuente, MEDIDA HOY")]
    actos = [l.strip() for l in ls if l.strip().startswith("acto '")]
    acta120 = [l.strip() for l in ls
               if "EL ACTA 120 EMPIEZA EN LA LINEA" in l
               or "LA ADJUDICACION 3.1 DEL ACTA 120 VIVE EN LA LINEA" in l]
    # CORRECCION DECLARADA DENTRO DE LA PROPIA VUELTA, y el patron viejo queda
    # escrito sin borrar: la primera version filtraba con r"^\s+417\d\d> " y
    # r"^\s+159\d> ", que son las decenas de linea del dia, no un patron. El de
    # arriba dejaba fuera la 41699, que es JUSTO la primera linea de la
    # adjudicacion, y la guarda de conteo lo canto en rojo (14 de 15).
    adj120 = [l.strip() for l in ls if re.match(r"^\s+4\d{4}> ", l)]
    pend = [l.strip() for l in ls if "LA SEXTA ENTRADA VIVE EN LA LINEA" in l]
    pend_post = [l.strip() for l in ls if re.match(r"^\s+1\d{3}> ", l)]
    resto17 = [l.strip() for l in ls
               if re.match(r"^\s{3}\S.*\sidx \d+ \| (CUBRE|A MEDIAS|NO CUBRE)",
                           l)]
    sha = [l.strip() for l in ls if " AL ENTRAR: sha256" in l
           or " AL SALIR:   sha256" in l]
    cierre17 = [l.strip() for l in ls
                if "AL CIERRE DE LA TAREA 2:" in l and l.strip().startswith("CIFRA")]
    frontera = [l.strip() for l in ls
                if l.strip().startswith("LA PREGUNTA QUE DECIDE LA CLAUSULA")
                or l.strip().startswith("LO MEDIDO:")
                or l.strip().startswith("MI LECTURA, CON SU MOTIVO")]
    parada = [l.strip() for l in ls
              if l.strip().startswith("LA CONDICION PIDE QUE LAS DIECISIETE")
              or l.strip().startswith("CIFRA en CUBRE:")
              or l.strip().startswith("LA CONDICION SE CUMPLE:")
              or l.strip().startswith("POR TANTO, LA PARADA FELIZ:")]

    datos = {
        "v": VUELTA,
        "salida": SALIDA,
        "bytes_salida": bytes_salida,
        "grafo": "- " + L(t, "EL GRAFO DE HOY, MEDIDO Y NO HEREDADO:"),
        "expediente": "- " + L(t, "EL EXPEDIENTE DE HOY:"),
        "cifra7": NL.join("- " + x for x in cifra7),
        "ver_sonda": L(t, "EL VEREDICTO QUE LA SONDA DA HOY POR SU PROPIO "
                          "DETECTOR"),
        "n2a": len(tabla_2a) - 2,
        "tabla_2a": NL.join(tabla_2a),
        "actos": NL.join("- " + x for x in actos),
        "cifra_actos": L(t, "CIFRA actos del material hallados en el receptor:"),
        "saldo_2a": L(t, "CIFRA menciones cuyo material VIVE en un nodo vivo"),
        "vara_2a": L(t, "CIFRA borradas sin destino:"),
        "veredicto_2a": "**" + L(t, "VEREDICTO DE 01 FUENTES idx 1:") + "**",
        "acta120": NL.join("- " + x for x in acta120),
        "adj120": NL.join("> " + x for x in adj120),
        "pend": NL.join("- " + x for x in pend),
        "pend_post": NL.join("> " + x for x in pend_post),
        "sujeto": "- " + L(t, "EL SUJETO SON LOS TRES DE LA NOMINA DE OP-S-02"),
        "estado_ficha": "- " + L(t, "EL ESTADO DE LA FICHA, LEIDO DEL "
                                    "EXPEDIENTE:"),
        "n2b": len(tabla_2b) - 2,
        "tabla_2b": NL.join(tabla_2b),
        "cifra_2b": L(t, "CIFRA de los tres que llegan a una version de "
                         "Incoterms"),
        "frontera": NL.join("- " + x for x in frontera),
        "veredicto_2b": "**" + L(t, "VEREDICTO DE 05 SANEO idx 1 QUE ESTA TAREA "
                                    "APLICA:") + "**",
        "fuente17": "- " + L(t, "LA FUENTE DE LAS 17 FILAS ES MI PROPIA CORRIDA"),
        "nfilas17": "- " + L(t, "CIFRA filas armadas leyendo ese fichero:"),
        "reparto_t1": "- " + L(t, "EL REPARTO QUE LA TAREA 1 DEJO MEDIDO:"),
        # EL ANCLA LLEVA EL NOMBRE DE LA FILA A PROPOSITO: "SUBE POR LECTURA:"
        # a secas aparece DOS veces en la salida, porque la tabla del cierre
        # repite la marca dentro de la celda del veredicto. La guarda lo canto
        # en rojo y aqui queda declarado en vez de tapado.
        "sube": "- " + L(t, "SUBE POR LECTURA: 01 FUENTES"),
        "mueve": "- " + L(t, "CIFRA clausulas que esta tarea mueve:"),
        "cierre17": NL.join("- " + x for x in cierre17),
        "n17": len(tabla_17) - 2,
        "tabla_17": NL.join(tabla_17),
        "resto17": NL.join("- " + x for x in resto17),
        "cifra_resto": L(t, "CIFRA clausulas que siguen sin cubrir:"),
        "parada": NL.join("- " + x for x in parada),
        "sha": NL.join("- " + x for x in sha),
        "sha_total": L(t, "COINCIDEN AL ENTRAR Y AL SALIR POR LAS DOS "
                          "CONVENCIONES:"),
        "disc": NL.join("| **%s** | %s | %s |" % (a, b_, c)
                        for a, b_, c in DISCUTIBLES),
        "caso_rojo": L(t, "EL CASO ROJO, DICHO CUAL ES CUAL:"),
    }
    texto = CUERPO % datos

    fallos = 0
    for etiqueta, medido, debido in (
            ("tabla 2.a", datos["n2a"], 7),
            ("tabla 2.b", datos["n2b"], 3),
            ("tabla de las 17", datos["n17"], 17),
            ("cifras del 7 reproducido", len(cifra7), 2),
            ("actos del material mudado", len(actos), 4),
            ("lineas de la adjudicacion 3.1 del acta 120", len(adj120), 15),
            ("lineas de la anotacion de PENDIENTES", len(pend_post), 2),
            ("cifras del cierre de las 17", len(cierre17), 3),
            ("filas de las que no cubren", len(resto17), 3),
            ("lineas de sha", len(sha), 12),
            ("lineas de la parada feliz", len(parada), 4)):
        print("CIFRA %s, contadas del fichero: %d | CIFRA que deberia haber: %d"
              % (etiqueta, medido, debido))
        if medido != debido:
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
