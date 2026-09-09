# -*- coding: utf-8 -*-
r"""_v218_t1_seccion.py . EL CUERPO DE LA TAREA 1 DEL REPORTE DE LA VUELTA 218,
COMPUESTO DE SU SALIDA SELLADA Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: toda tabla o cifra del reporte
cita el fichero de salida del que sale, y se RECONSTRUYE CONTANDO ESE FICHERO
antes de publicarla. Aqui NINGUNA celda se teclea: las filas se leen de
docs/loop/SALIDA_V218_T1_REGISTROS.txt, y el compositor DICE cuantas armo y
cuantas deberia haber.

LO UNICO MIO SON LOS DISCUTIBLES Y SUS MOTIVOS, y van en su propia seccion
rotulada como lectura mia, para que se pueda auditar cual es cual.

USO:  python scripts/loop/_v218_t1_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
SALIDA = "docs/loop/SALIDA_V%d_T1_REGISTROS.txt" % VUELTA
MAR_A = "docs/loop/SALIDA_V%d_T1_MARCADOR_ANTES.txt" % VUELTA
MAR_D = "docs/loop/SALIDA_V%d_T1_MARCADOR_DESPUES.txt" % VUELTA
DESTINO = "scripts/loop/_v%d_t1_seccion.md" % VUELTA

# LOS DISCUTIBLES SON LECTURA MIA Y SE MARCAN ANTES DE SABER SI ACIERTO
# (EJECUTOR.md 7). Cada uno dice QUE decidi y CUAL es la duda.
DISCUTIBLES = [
    ("D.1", "PUESTO 299, la clase que muevo de B a D",
     "Confirmo el caso del auditor contra el grafo y **escribo la correccion**: "
     "las dos condiciones del banco `9.6.2` se cumplen y la regla no admite el "
     "empate. **La duda que dejo escrita antes de saber si acierto**: el paso 2 "
     "del hijo, el guion breve con el fallo de empresa y la decision no "
     "negociable, toca ademas el paso 3 de la madre, definir el mensaje central. "
     "Si el auditor lee que eso rompe la condicion de caber dentro de UN SOLO "
     "paso, el par no es madre e hijo por esa via y la `B` volveria a estar "
     "viva. Yo leo que no la rompe, porque el paso 4 de la madre ya dice "
     "explicando la situacion y dejando claro que la decision es innegociable, "
     "y ahi cabe el guion entero."),
    ("D.2", "PUESTO 1249, la D que se sostiene con menos margen",
     "Sostengo **D** y corrijo la razon, y **digo que el margen se estrecho**: "
     "con la cifra vieja lo compartido era una linea en un paso de cada lado, y "
     "medido hoy son TRES de los CUATRO pasos del nodo pequeno. Lo que le queda "
     "fuera del solape es **UN paso y su entregable**, no dos bloques de "
     "procedimiento como en el ejemplar del `9.6.3`. **Si el auditor lee que un "
     "solo paso propio no basta para el lado del pequeno, esta clase se vuelve "
     "`B` y no `A`**, porque el lado grande conserva ocho pasos y la fusion "
     "borraria la lectura del puesto 520."),
    ("D.3", "el sitio donde escribo, que es el registro y no el plan",
     "El encargo prohibe escribir en el plan y no escribo en el plan: los seis "
     "`sha256` del expediente, de la pagina 08 y de la pagina 07 coinciden al "
     "entrar y al salir. **Lo que si escribo es el registro del cribado**, "
     "porque es donde el carril de la `5.7` del acta 217 manda la correccion "
     "declarada con recomputo del marcador y donde el modo austero pone las "
     "decisiones de lectura. **Si el auditor lee que la prohibicion alcanzaba "
     "tambien al registro, esta escritura sobra y se revierte**, y lo digo yo "
     "antes de que me lo digan."),
]


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def medir(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    b = io.open(p, "rb").read()
    return len(b), len(b.replace(b"\r\n", b"\n"))


def L(texto, marca):
    for l in texto.split(NL):
        if marca in l:
            return l.strip()
    raise SystemExit("ROJO: falta la linea %r" % marca)


def bloque(texto, desde, hasta):
    ls = texto.split(NL)
    i = next(n for n, l in enumerate(ls) if desde in l)
    j = next(n for n, l in enumerate(ls) if n > i and hasta in l)
    return [l for l in ls[i + 1:j]]


def main():
    print("LAS SEDES QUE ESTE CUERPO CITA COMO PRUEBA, MEDIDAS ANTES DE "
          "CITARLAS (una ruta que promete prueba es cifra):")
    fallos = 0
    for rel in (SALIDA, MAR_A, MAR_D):
        m = medir(rel)
        if m is None:
            print("   ROJO: %s NO EXISTE" % rel)
            fallos += 1
        elif m[0] == 0:
            print("   ROJO: %s mide CERO BYTES" % rel)
            fallos += 1
        else:
            print("   %-52s %7d bytes en disco y %7d normalizado a LF"
                  % (rel, m[0], m[1]))
    if fallos:
        return 1

    t = leer(SALIDA)
    ms = medir(SALIDA)

    tabla = [l for l in t.split(NL) if l.startswith("| ") and " | 0 |" in l
             or re.match(r"^\| \d+ \| ", l)]
    tabla = [l for l in t.split(NL) if re.match(r"^\| \d+ \| ", l)]
    print("CIFRA filas de la tabla de las diecisiete armadas leyendo la salida: "
          "%d | CIFRA que deberia haber: 17" % len(tabla))
    if len(tabla) != 17:
        return 1

    adj = [l for l in t.split(NL) if l.startswith("| **D.")]
    print("CIFRA filas de adjudicacion armadas leyendo la salida: %d | CIFRA que "
          "deberia haber: 4" % len(adj))
    if len(adj) != 4:
        return 1

    seis = bloque(t, "LAS SEIS QUE NO DAN CUBRE, CON SU FILA Y SU INDICE:",
                  "CIFRA filas que no dan CUBRE")
    print("CIFRA filas de las que no cubren armadas leyendo la salida: %d | "
          "CIFRA que deberia haber: 6" % len(seis))
    if len(seis) != 6:
        return 1

    mar = [l for l in t.split(NL) if l.strip().startswith("clase ")]
    print("CIFRA filas del marcador armadas leyendo la salida: %d | CIFRA que "
          "deberia haber: 4" % len(mar))
    if len(mar) != 4:
        return 1

    sha = [L(t, "SHA256 DE docs/plan/OPERACIONES.jsonl AL ENTRAR"),
           L(t, "SHA256 DE docs/plan/OPERACIONES.jsonl AL SALIR"),
           L(t, "SHA256 DE docs/plan/08_VERIFICACION.md AL ENTRAR"),
           L(t, "SHA256 DE docs/plan/08_VERIFICACION.md AL SALIR"),
           L(t, "SHA256 DE docs/plan/07_ADUANA.md AL ENTRAR"),
           L(t, "SHA256 DE docs/plan/07_ADUANA.md AL SALIR"),
           L(t, "LOS SEIS SHA DEL PLAN COINCIDEN CON LOS DE LA ENTRADA")]

    texto = """### TAREA 1. LOS REGISTROS

**LO QUE SE CORRIO, Y SU RUTA CON SUS BYTES:**
``%(salida)s``, **%(bd)d bytes en disco y %(bl)d normalizado a LF**, exitcode 0.

**EL INSTRUMENTO NO ES ARNES NUEVO Y ESO IMPORTA CON LA MORATORIA ENCIMA**
(`AUDITOR.md` 6.3). Los lectores `grafo` y `resolutor` se **IMPORTAN**, y el
cargador que los saca de `scripts/loop/vuelta150_4_tabla_por_fase.py` sin tocar
ese fichero en disco tambien se **IMPORTA**, de
`scripts/loop/_v217_t1_diecisiete.py`. **IMPORTAR NO ES CLONAR**, adjudicado en
el acta 206, adjudicacion `6.5`, **linea 72517** de `docs/loop/ACTA_AUDITOR.md`,
leida hoy del fichero.

#### 1.a. EL RECUENTO CORREGIDO, CON CORRECCION DECLARADA Y RECOMPUTO

**LA CORRECCION NO ES MIA Y LO DIGO PRIMERO:** la adjudica el auditor en la
`5.5` del acta 217, **linea 77275** de `docs/loop/ACTA_AUDITOR.md`, leida hoy
del fichero. **Yo la reproduzco en la fuente y la registro.**

**LA CLAUSULA CORREGIDA, CON SU FILA, SU INDICE Y SUS DOS CIFRAS ENFRENTADAS:**

```
%(fuentes)s
```

**QUIEN MANDA NO LO DECIDO YO:** la correccion declarada de la vuelta 214,
escrita en la **linea 64** de `docs/plan/08_VERIFICACION.md` y leida hoy, dice
que las filas **no se inventan, se derivan**, y que cada celda se compone de las
clausulas de verificacion que las propias fichas traen. **Manda la ficha, y la
ficha dice CINCO.** El quinto control nacio el **13 ago 2026**, despues de que se
escribiera la celda, y **no corre**.

**EL RECOMPUTO, CON LAS DOS CIFRAS JUNTAS Y NINGUNA TECLEADA:**

```
%(recuento)s
```

**LA CELDA DE LA PAGINA 08 NO SE TOCA**, y no por olvido: corregirla es **sede
del fundador** y sube nombrada a la auditoria integral. Lo que esta vuelta hace
es **registrar el recuento corregido**, no reescribir la vara.

**LA TABLA ENTERA, CONTADA DE SU FICHERO** (%(nfilas)d filas de datos leidas de
``%(salida)s``, 17 que deberia haber), **con el veredicto viejo escrito al lado
del nuevo en la unica fila que se mueve:**

%(tabla)s

**LAS SEIS QUE NO DAN CUBRE, CON SU FILA, SU INDICE Y SU CIFRA** (%(nseis)d
lineas leidas del fichero, 6 que deberia haber):

```
%(seis)s
```

#### 1.b. LAS CUATRO ADJUDICACIONES A FAVOR DE MI LECTURA, REGISTRADAS SIN CAMBIAR VEREDICTO

**NINGUNA DE LAS CUATRO MUEVE UN VEREDICTO**, y por eso se registran y no se
recomputan. **Cada una lleva su numero de adjudicacion Y SU LINEA de
`docs/loop/ACTA_AUDITOR.md`, leida del fichero y no recordada**, que es la
obligacion `6.6` del acta 210, **linea 74203**.

| rotulo | adjudicacion del acta 217 | su linea, LEIDA | clausula | veredicto que se sostiene | por que |
|---|---|---:|---|---|---|
%(adj)s

**Y LA QUINTA ES LA QUE SI MUEVE UNA CIFRA**, `D.e`, adjudicada en la `5.5` del
acta 217, **linea 77275**: es la correccion de la `1.a` de arriba y no se repite
aqui.

#### 1.c. LAS DOS DISCREPANCIAS DE LA CIEGA, MEDIDAS CONTRA EL GRAFO

**EL VEREDICTO DE LAS DOS ES MIO Y LAS DOS SE DECIDEN CON LA VARA.** Los dos
pares se leyeron del grafo vivo **con el resolutor delante** (`P.1`), y de cada
nodo se publican sus pasos, su entregable y sus aristas en la salida sellada.

**PUESTO 299, `entrenamiento_de_gerentes_para_despidos` contra
`proceso_despidos_responsables`. MI CLASE ERA `B`. CONFIRMO EL CASO DEL AUDITOR
Y LA CLASE PASA A `D`.** El caso lo escribe el auditor en su `5.7` del acta 217,
**linea 77304**, leida hoy. **Medido contra el grafo:** la madre trae **5** pasos
y el hijo **4**; los cuatro del hijo caen dentro del **paso 4** de la madre, y la
madre conserva **3** pasos que el hijo no toca, el 1, el 2 y el 5. Los
entregables apuntan igual: la madre entrega tres productos y el hijo el primero
de los tres, que es el perfil del `2.215` del banco `9.6.2`. **Las dos
condiciones se cumplen y la regla no admite el empate**, asi que el *no lo
decido* de la razon vieja no se sostiene. **Arista, dato del grafo y no
argumento: NO hay en ninguno de los dos sentidos.**

**PUESTO 1249, `cierre_segun_complejidad_venta` contra
`relacion_continua_con_cliente`. LA CLASE NO CAMBIA, SIGUE SIENDO `D`. LA RAZON
SI SE CORRIGE.** El caso lo escribe el auditor en su `5.8` del acta 217, **linea
77312**, leida hoy. **Su cifra la reproduzco y la confirmo:** la razon vieja
decia que lo compartido era **una linea en un paso de cada uno**, y medido hoy
son **TRES de los CUATRO** pasos del nodo pequeno, el 1 con el 7, el 4 con el 8 y
el 3 con el 3 y el 12. **Y hay una segunda mitad que anado yo:**
`cierre_segun_complejidad_venta` trae **DOCE** pasos y la razon vieja enumeraba
**CINCO**, o sea que leyo menos de la mitad del nodo. **La clase se sostiene, y
no por la cifra sino por las dos reglas:** el `9.6.2` **no aplica en modo madre e
hijo**, porque su prueba pide que el pequeno quepa dentro de **UN** paso del
grande y aqui toca **cuatro**; y manda el `9.6.3`, que dice que la vara **no
tiene bascula** y pregunta que queda fuera del solape y en que lado. **Fuera del
solape el grande conserva 8 de sus 12 pasos**, que son la tesis del racimo, y el
pequeno conserva su paso 2 y su entregable. **Y las cuatro lecturas del racimo
siguen dando lo mismo**, 520, 1206 y 1217 en `D` como esta.

#### 1.d. LO QUE SE ESCRIBIO, DONDE, Y EL MARCADOR RECOMPUTADO

**SE ESCRIBIO EN EL REGISTRO DEL CRIBADO, `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`,
Y EN NINGUN SITIO MAS.** Las dos correcciones van **declaradas**, y la razon
vieja de cada una queda **escrita entera dentro de la nueva**, copiada del
archivo por maquina: una correccion que tapa lo que corrige no se puede auditar.

```
%(escrituras)s
```

**EL MARCADOR, RECOMPUTADO CON SU COMANDO ANTES Y DESPUES**, `python
scripts/recomputar_marcador.py 3388`, sellado en ``%(mar_a)s`` (**%(mad)d bytes
en disco y %(mal)d normalizado a LF**) y en ``%(mar_d)s`` (**%(mdd)d bytes en
disco y %(mdl)d normalizado a LF**):

```
%(marcador)s
%(movimiento)s
```

#### 1.e. EL PLAN NO SE TOCA, Y SE PRUEBA CON LOS SEIS SHA

```
%(sha)s
```

**Y LA SEDE QUE SI SE MUEVE SE DICE EN VOZ ALTA, NO SE ESCONDE:**

```
%(shaver)s
```

#### 1.f. LOS DISCUTIBLES DE ESTA TAREA, MARCADOS ANTES DE SABER SI ACIERTO

**Son lectura mia y por eso van aparte** (`EJECUTOR.md` 7). **Tres.**

| # | sobre que | que decidi y cual es la duda |
|---|---|---|
%(disc)s
""" % {
        "salida": SALIDA,
        "bd": ms[0], "bl": ms[1],
        "mar_a": MAR_A, "mar_d": MAR_D,
        "mad": medir(MAR_A)[0], "mal": medir(MAR_A)[1],
        "mdd": medir(MAR_D)[0], "mdl": medir(MAR_D)[1],
        "fuentes": NL.join([
            L(t, "FUENTE 1, LA CELDA:"),
            "   " + L(t, "| **07 ADUANA** | los cuatro"),
            L(t, "FUENTE 2, LA FICHA:"),
            "   " + L(t, "VERBATIM idx 3:"),
            L(t, "FUENTE 3, LA PAGINA DE LA FASE:"),
            "   " + L(t, "EL QUINTO, CON SU ORIGEN:"),
            L(t, "CIFRA que la celda de la pagina 08 pide:")]),
        "recuento": NL.join([
            L(t, "CIFRA clausulas en CUBRE, RECOMPUTADAS:"),
            L(t, "CIFRA clausulas en A MEDIAS, RECOMPUTADAS:"),
            L(t, "CIFRA clausulas en NO CUBRE, RECOMPUTADAS:"),
            L(t, "CIFRA filas tocadas por la correccion:")]),
        "nfilas": len(tabla),
        "tabla": NL.join(["| # | fila | idx | veredicto | la clausula, VERBATIM |",
                          "|---:|---|---:|---|---|"] + tabla),
        "nseis": len(seis),
        "seis": NL.join(x.strip() for x in seis),
        "adj": NL.join(adj),
        "escrituras": NL.join([l.strip() for l in t.split(NL)
                               if l.strip().startswith("TOCADO puesto")]
                              + [L(t, "CIFRA lineas tocadas:"),
                                 L(t, "CIFRA lineas del registro que difieren"),
                                 L(t, "RELECTURA DEL DISCO:")]),
        "marcador": NL.join(x.strip() for x in mar),
        "movimiento": L(t, "EL MOVIMIENTO ES EL QUE LA CORRECCION PREDICE"),
        "sha": NL.join(sha),
        "shaver": NL.join([
            L(t, "SHA256 DE docs/INTRA_DOMINIO_VEREDICTOS.jsonl AL ENTRAR"),
            L(t, "SHA256 DE docs/INTRA_DOMINIO_VEREDICTOS.jsonl AL SALIR"),
            L(t, "ESA SEDE SE MOVIO A PROPOSITO:"),
            L(t, "CIFRA bytes de docs/INTRA_DOMINIO_VEREDICTOS.jsonl al salir:")]),
        "disc": NL.join("| **%s** | %s | %s |" % (a, b, c)
                        for a, b, c in DISCUTIBLES),
    }

    mayores = [l for l in texto.split(NL)
               if l.startswith("## ") and not l.startswith("### ")]
    print("CIFRA encabezados de nivel dos en el cuerpo del anexo: %d | CIFRA "
          "que deberia haber: 0" % len(mayores))
    if mayores:
        for m in mayores:
            print("   sospechoso> %s" % m)
        return 1
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
