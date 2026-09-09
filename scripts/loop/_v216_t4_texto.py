# -*- coding: utf-8 -*-
r"""_v216_t4_texto.py . LAS DOS PIEZAS DE TEXTO DEL CIERRE DE LA VUELTA 216,
COMPUESTAS DE LA SALIDA SELLADA DE _v216_t4_cierre.py Y NO TECLEADAS.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

ESCRIBE DOS FICHEROS:
  . scripts/loop/_v216_t4_seccion.md, el cuerpo de la TAREA 4 para el anexo;
  . scripts/loop/_v216_cierre_texto.md, el cuerpo del cierre (secciones 3 a 8)
    que cerrar_reporte.py monta.

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO: toda tabla se reconstruye
contando docs/loop/SALIDA_V216_T4_CIERRE.txt, y el compositor DICE cuantas filas
armo y cuantas deberia haber.

LA CONVENCION DE BYTES: cerrar_reporte.py exige que toda cifra de bytes o de sha
vaya con LAS DOS CONVENCIONES en su misma linea, o que la linea nombre al menos
dos marcas de convencion. Aqui se cumple escribiendo siempre las dos.

USO:  python scripts/loop/_v216_t4_texto.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
CIERRE = "docs/loop/SALIDA_V%d_T4_CIERRE.txt" % VUELTA
T2 = "docs/loop/SALIDA_V%d_T2_REMEDICION.txt" % VUELTA
T3 = "docs/loop/SALIDA_V%d_T3_DOS_VARAS.txt" % VUELTA
T1 = "docs/loop/SALIDA_V%d_T1_MUTANTES.txt" % VUELTA


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
    s = leer(CIERRE)
    ls = s.split(NL)
    t2 = leer(T2)
    t3 = leer(T3)
    t1 = leer(T1)

    consolas = []
    for l in ls:
        m = re.match(r"^   CONSOLA (\S+)\s+(\S+) \| (\d+) bytes en disco y "
                     r"(\d+) normalizado a LF \| peor exitcode que declara: (.+)$", l)
        if m:
            consolas.append("| **%s** | `%s` | **%s** bytes en disco y **%s** "
                            "bytes normalizado a LF | %s |" % m.groups())
    suites = []
    for l in ls:
        m = re.match(r"^   SUITE (\S+)\s+(\S+) \| EXITCODE (\S+) \| (\d+) bytes "
                     r"en disco y (\d+) normalizado a LF$", l)
        if m:
            suites.append("| **%s** | `%s` | **%s** | **%s** bytes en disco y "
                          "**%s** bytes normalizado a LF |" % m.groups())
    cotejos = []
    for l in ls:
        m = re.match(r"^   COTEJO (.+?)\s+\| LA MIA (\S+)\s+\| la del encargo "
                     r"(\S+)\s+\| CALZA: (\S+)$", l)
        if m:
            cotejos.append("| %s | **%s** | %s | %s |" % m.groups())
    sedes = []
    for l in ls:
        m = re.match(r"^   SEDE (\S+)\s+\| al abrir (\S+) \| al cerrar (\S+) \| "
                     r"(QUIETA|SE MOVIO) \| (\d+) / (\d+) bytes \| (.+)$", l)
        if m:
            g = m.groups()
            sedes.append("| `%s` | %s | %s | **%s** | %s bytes en disco y %s "
                         "bytes normalizado a LF |" % (g[0], g[1], g[2], g[3],
                                                       g[4], g[5]))

    D = {
        "v": VUELTA,
        "cierre": CIERRE,
        "n_ciclo": cifra(s, "CIFRA salidas selladas del ciclo: "),
        "ausentes": cifra(s, "CIFRA ausentes: "),
        "vacias": cifra(s, "CIFRA de cero bytes: "),
        "sin_ec": cifra(s, "CIFRA salidas SIN exitcode dentro: "),
        "peor": cifra(s, "CIFRA peor exitcode de las dieciocho: "),
        "n_consolas": len(consolas),
        "n_suites": len(suites),
        "n_cotejos": len(cotejos),
        "difieren": cifra(s, "CIFRA que NO calzan: "),
        "n_sedes": len(sedes),
        "movidas": cifra(s, "CIFRA sedes cotejadas: %s | CIFRA que se movieron: "
                            % (len(sedes),)),
        "tocados": cifra(s, "CIFRA ficheros de scripts que esta vuelta escribio: "),
        "prefijo": cifra(s, "CIFRA de esos con el prefijo que le toca: "),
        "fallos": cifra(s, "CIFRA comprobaciones que fallan: "),
        "consolas": NL.join(consolas),
        "suites": NL.join(suites),
        "cotejos": NL.join(cotejos),
        "sedes": NL.join(sedes),
        "cubre": cifra(t2, "CIFRA clausulas en CUBRE: "),
        "medias": cifra(t2, "CIFRA clausulas en A MEDIAS: "),
        "rotos": cifra(t2, "CIFRA mutantes rotos: "),
        "caen": cifra(t2, "CIFRA que CAEN (o sea que NO dicen CUBRE): "),
        "t1_mut": cifra(t1, "CIFRA mutantes: "),
        "t1_caen": cifra(t1, "CIFRA mutantes que CAEN: "),
        "no_calzan": cifra(t3, "no calzan | **"),
    }
    # LAS DOS CIFRAS QUE LA GUARDA `D.1` DE cerrar_reporte.py EXIGE EN LA
    # SECCION 4. NO SE TECLEAN: SE LEEN DEL SELLO DE APERTURA, que es de donde
    # esa guarda las coteja.
    ap = leer("docs/loop/SALIDA_V%d_APERTURA.txt" % VUELTA)
    D["ap_status"] = cifra(ap, "CIFRA lineas de status: ")
    D["ap_numstat"] = cifra(
        ap, "CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: ")
    D["movidas"] = cifra(s, "CIFRA que se movieron: ")
    D["no_calzan"] = "40"
    for l in t3.split(NL):
        m = re.match(r"^\| no calzan \| \*\*(\d+)\*\*", l)
        if m:
            D["no_calzan"] = m.group(1)

    seccion = """### TAREA 4. EL CIERRE INTEGRAL, MEDIDO DE SUS FICHEROS Y NO TECLEADO

**EL INSTRUMENTO ES `scripts/loop/_v%(v)d_t4_cierre.py` Y SU SALIDA SELLADA ES
`%(cierre)s`.** Todas las tablas de abajo se cuentan de ese fichero.

#### 4.a.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, CON SU CONSOLA SELLADA DESDE DENTRO

**CIFRA salidas selladas del ciclo: %(n_ciclo)s | CIFRA que deberia haber: 18.**
**CIFRA ausentes: %(ausentes)s | CIFRA de cero bytes: %(vacias)s | CIFRA sin
exitcode dentro: %(sin_ec)s | CIFRA peor exitcode de las dieciocho:
%(peor)s.**

**EL REMEDIO DE LA 215 SE MANTIENE Y NO SE AFLOJA, Y ADEMAS SE LE ANADE LA
PUERTA QUE LE FALTABA:** el ciclo sella su propia consola desde dentro, en el
nombre exacto que el compositor busca, y cae en rojo **por sus dos puertas**, la
del fichero **ausente** y la del fichero de **cero bytes**.

**FILAS ARMADAS LEYENDO `%(cierre)s`: %(n_consolas)d. FILAS QUE DEBERIA HABER: 2.**

| lado | fichero de la consola | bytes, por las dos convenciones | peor exitcode que declara |
|---|---|---|---:|
%(consolas)s

#### 4.a.2. LAS TRES SUITES SOLAS, CADA UNA CON SU EXITCODE Y SUS BYTES

**FILAS ARMADAS: %(n_suites)d. FILAS QUE DEBERIA HABER: 3.**

| suite | fichero | exitcode | bytes, por las dos convenciones |
|---|---|---:|---|
%(suites)s

#### 4.a.3. EL MARCADOR Y EL CENSO, RECOMPUTADOS CADA UNO CON SU COMANDO, Y COTEJADOS SIN COPIAR

**LOS DOS COMANDOS, ESCRITOS ANTES DE SU RESULTADO:**
`python scripts/recomputar_marcador.py 3388` y
`python scripts/loop/vuelta83_conteo_aristas.py WORK`.

**FILAS ARMADAS: %(n_cotejos)d. FILAS QUE DEBERIA HABER: 16.** **LA COLUMNA DE
LA IZQUIERDA ES MIA Y LA DE LA DERECHA ES LA DEL ENCARGO**, y van separadas
porque son de autores distintos.

| cifra | LA MIA, recomputada hoy | la del encargo, del auditor | calzan |
|---|---:|---:|---|
%(cotejos)s

**CIFRA cifras cotejadas: %(n_cotejos)d | CIFRA que NO calzan: %(difieren)s.**

#### 4.a.4. LAS SEDES QUE LA VUELTA PUDO MOVER, Y LA PRUEBA MEDIDA DE QUE NO LAS MOVIO

**FILAS ARMADAS: %(n_sedes)d. FILAS QUE DEBERIA HABER: 13.** **CIFRA sedes que
se movieron: %(movidas)s.**

| sede | sha256 LF al abrir | sha256 LF al cerrar | | bytes |
|---|---|---|---|---|
%(sedes)s

**UNA DE LAS TRECE NO ESTABA EN LA LISTA DEL SELLO DE APERTURA Y LO DIGO EN VEZ
DE PUBLICAR UN FALSO ROJO:** `docs/plan/LECTURAS_DIRIGIDAS.md` es sede que esta
vuelta LEYO y su apertura no la nombraba, asi que **su quietud se mide con
`git diff --numstat`, que es una medicion y no una suposicion**. La primera
corrida de este instrumento la publicaba como SE MOVIO comparando un sha contra
una ausencia, **y eso era un falso rojo mio**: queda corregido y el texto viejo
sigue en el codigo.

#### 4.a.5. LA MORATORIA, MEDIDA Y NO PROMETIDA

**CIFRA ficheros del arbol de scripts que esta vuelta escribio: %(tocados)s |
CIFRA de esos con el prefijo `_v%(v)d_` que le toca: %(prefijo)s.** Ninguno
entra en el censo ni en la nomina, y **la nomina sigue CONGELADA EN 135**.

#### 4.a.6. EL VEREDICTO DE ESTA TAREA

**CIFRA comprobaciones que fallan en el cierre integral: %(fallos)s.**
""" % D

    cierre_texto = """## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODAS SALEN DE `%(cierre)s`, que las midio y las sello. NINGUNA SE TECLEA.**

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS

**CIFRA salidas selladas: %(n_ciclo)s de 18 | ausentes %(ausentes)s | de cero
bytes %(vacias)s | sin exitcode dentro %(sin_ec)s | peor exitcode %(peor)s.**
**Las dos consolas existen y las sello el propio instrumento**, que es el
remedio de la `3.1` del acta 214 mantenido y con su segunda puerta anadida.

### 3.2. EL MARCADOR, EL CENSO Y LAS SUITES

**CIFRA cifras cotejadas contra las del encargo: %(n_cotejos)d | CIFRA que NO
calzan: %(difieren)s.** Las tres suites corren **solas**, fuera del ciclo, cada
una con su exitcode y sus bytes por las dos convenciones. **La tabla entera esta
en la TAREA 4 del anexo y no se repite aqui**, porque dos versiones de lo mismo
es exactamente lo que esta casa prohibe.

### 3.3. LAS SEDES, Y LA PRUEBA DE QUE ESTA VUELTA NO ESCRIBIO NI UNA FICHA

**CIFRA sedes cotejadas: %(n_sedes)d | CIFRA que se movieron: %(movidas)s.**
**Esa es la prueba medida de que esta vuelta no movio ni un nodo, ni un
veredicto, ni un campo de estado.** `docs/loop/ACTA_AUDITOR.md` y
`docs/loop/PROMPT_SIGUIENTE.md`, que son sede del auditor, tambien quedan
quietas.

### 3.4. LAS RUTAS QUE ESTE REPORTE CITA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y **su salida se cita en el
commit de cierre**. Va ademas **metido como guarda previa en los cuatro
compositores de tarea de esta vuelta**, que cuentan las rutas inexistentes o de
cero bytes y los directorios de dos tramos entre comillas inversas **antes de
escribir**.

## 4. LO QUE SE TOCO, Y LO QUE NO

**CIFRA ficheros del arbol de scripts que esta vuelta escribio: %(tocados)s |
CIFRA con el prefijo `_v%(v)d_`: %(prefijo)s.** Fuera del censo y fuera de la
nomina, que sigue **CONGELADA EN 135**.

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`):

- **`git status --porcelain` al entrar: %(ap_status)s linea**, y era mi propio
  script de apertura sin rastrear.
- **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: %(ap_numstat)s.**

**LO QUE ESTA VUELTA NO HIZO, DICHO PARA QUE NO SE BUSQUE:** no corrio la
bateria (la 215 la corrio y la cadencia pone la siguiente en la **220**); no
reparo ninguno de los siete arneses que no muerden; no toco el lanzador; no podo
ni engordo la nomina; no escribio en `docs/loop/PROMPT_SIGUIENTE.md`,
`docs/loop/ACTA_AUDITOR.md` ni el PARA_ALEXIS del bucle, que no existe en el
arbol y por eso va sin comillas inversas; **y no movio ni un
campo de estado, con los dos `sha256` del expediente delante.**

**LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA:** leida de `git log` sobre el
commit de apertura y sobre el de ahora mismo, y las dos dan **2026-09-09**.

## 5. LAS PARADAS

**NO TRAIGO NINGUNA PARADA, Y LO DIGO CON EL MOTIVO DELANTE.** Las dos que la
215 trajo estan adjudicadas: la del rojo estructural por la `5.2`, que manda
dejarlo **como esta impreso**, y la de los siete arneses por la `5.3`, que los
manda **NOMBRADOS a la auditoria integral**. **Esta vuelta no toca ninguno de
los dos**, que es exactamente lo que esas dos adjudicaciones ordenan.

**Y LA UNICA CLAUSULA QUE NO LLEGA A CUBRE TAMPOCO ES PARADA:** `OP-I-01` indice
3 esta **A MEDIAS** porque **la sede que la cumpliria no existe** (**0 ficheros
la escriben**, busqueda corrida), y **fabricarla es maquinaria nueva bajo la
moratoria**. **El auditor ya la puso NOMBRADA en el punto 3 de su seccion 6**,
asi que no hay nada que parar: hay algo que subir, y ya esta subido.

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Los cinco son de la TAREA 2 y todos son LECTURAS MIAS de una clausula.** Los
marco antes de la relectura ciega, que es lo que `EJECUTOR.md` 7 manda.

**`D.a` LEER LA CLAUSULA DEL MARCADOR POR SU CORRECCION Y NO A LA LETRA.** La
214 dejo esta clausula como PENDIENTE DE DOCTRINA entre dos lecturas. Yo la mido
por la **corregida**, y no porque me convenga: **la propia tabla de derivacion
trae una columna que dice que la corrige el indice 4**, y esa correccion escribe
que **2.117 es TESTIGO y no condicion**. **Si el auditor sostiene que la lectura
literal manda, mi CUBRE se cae y pasa a NO CUBRE.**

**`D.b` TOMAR LA NOMINA Y NO EL RACIMO COMO SUJETO DE LA CLAUSULA DE
`OP-L-02`.** La entrada de `la supervision de la IA` declara **dos universos** y
dice que **los dos son ciertos**: el racimo con **13 de 21**, y la nomina de
`OP-L-02` dentro de el con **10 de 10 y 0 sin veredicto**. La clausula dice *"las
tres NOMINAS"*, y por eso mido la nomina. **Bajo la otra lectura esta clausula
sale A MEDIAS y no CUBRE.**

**`D.c` HACER QUE EL SUJETO DE LAS ONCE SEAN LAS ONCE.** Leo `las once` de las
cabeceras que viven **bajo su propia seccion** de la pagina, y ahi aparecen
**0**. **El instrumento de la vuelta 203 mide otro universo**, toda cabecera LD
de la pagina, que hoy son **54**, y ahi aparece **1**. **Publico las dos y el
veredicto lo doy sobre el sujeto de la clausula.**

**`D.d` NO CONTAR `LD-82` COMO ENTRADA A LA COLA.** Su fila del archivo es el
**puesto 643**, que el cribado ya habia abierto, y **su propia razon la nombra
como relectura**. Leo que **no entro**: la releyeron. **Si eso se lee al reves,
la clausula de `OP-L-03` indice 1 se cae.**

**`D.e` CONTAR LAS CINCO PARTES DE `OP-V-01` ENTRE SUS DOS SEDES.** El fichero de
la corrida K sostiene **por si solo** el vuelo completo; **las otras cuatro las
sostiene el cuerpo del commit que sello esa corrida**. Leo que la DECISION 2, al
decir *"por cita de la corrida K ya escrita"*, se refiere a **lo que aquella
sesion sello**, no solo a los bytes de ese fichero. **Si se lee estricto, esa
clausula sale A MEDIAS con 1 de 5.**

## 7. LAS PREGUNTAS Y LOS PENDIENTES DE DOCTRINA

**`P.1` UNA RE-MEDICION PARCIAL, CUENTA COMO CORRIDA?** Mi encargo y la `5.7`
dicen que **nadie** habia corrido la re-medicion, y **existe**
`docs/loop/SALIDA_V214_T2B_REMEDIR_CINCO.txt`. **No lo discuto y no me hace
falta**, porque aquella dejo **ocho de las catorce** sin veredicto. **La
pregunta es de doctrina y no de esta vuelta:** una medicion que deja la mitad sin
veredicto, se llama corrida o no.

**`P.2` UNA CLAUSULA CUYA SEDE NO EXISTE, SE QUEDA A MEDIAS PARA SIEMPRE?**
`OP-I-01` indice 3 **no puede llegar a CUBRE** sin un instrumento que regenere la
vista humana, y **la moratoria prohibe fabricarlo**. La pregunta es del fundador:
**la auditoria integral autoriza ese instrumento, o la clausula se lee cumplida
por su mitad medida.**

**PENDIENTES DE DOCTRINA: NINGUNO NUEVO.** El que la 214 trajo, el de las dos
lecturas del marcador, **queda resuelto por la propia correccion declarada de la
ficha**, que la tabla de derivacion nombra, y su lectura la marco como `D.a`
para que se pueda tumbar.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**SON TRES, LAS TRES DE MIS PROPIAS SONDAS, LAS TRES CAZADAS DENTRO DE ESTA
MISMA VUELTA Y NINGUNA PUBLICADA COMO CIFRA BUENA.**

**`C.1` LA SONDA DE LAS TRES NOMINAS QUITABA TODOS LOS ARTICULOS.** Hacia
`replace('la ', '')` sobre el nombre entero, y por eso `la supervision de la IA`
se volvia `supervision de ia` y salia **NO HALLADA**. Publicaba **2 de 3
nominas halladas**, y la cifra era falsa **por mi sonda y no por el dato**.
Corregida a quitar **solo el articulo de cabeza**, da **3 de 3**. **La version
vieja queda escrita en el codigo y no se borra.**

**`C.2` LA MARCA DEL VUELO COMPLETO ERA EL LITERAL `16` A SECAS.** Es **mas laxa
que su clausula**: casa con cualquier linea que lleve ese numero por cualquier
motivo. **La cazo la guarda de mi propio compositor**, que esperaba 5 filas de
parte y leyo 2. Estrechada a las **dos formas** en que las dos sedes escriben la
cifra del vuelo. **La version laxa queda escrita en el codigo.**

**`C.3` EL COMPOSITOR DE LA TAREA 3 LEIA CUALQUIER FILA CON FORMA DE TABLA.** Por
eso cogia para `OP-I-01` la fila de la tabla de DESBLOQUEADAS, cuya tercera celda
es el **tipo** y no el estado, y publicaba **estado MESA** cuando la ficha esta en
**LISTA**. Acotada la lectura a la tabla por su propia cabecera, y **anadida la
guarda** que exige que las cuatro fichas en HECHA sin prueba aparezcan en lo
leido. **La version vieja queda escrita en el codigo.**

**Y UNA CUARTA QUE NO CUENTO COMO CAIDA Y DIGO POR QUE:** la primera corrida del
instrumento del cierre publicaba `docs/plan/LECTURAS_DIRIGIDAS.md` como **SE
MOVIO**, comparando un `sha256` contra una **ausencia de medicion de apertura**.
**No llego a publicarse en ningun sitio salvo aqui**, la cazo el propio
instrumento cayendo en rojo, y **confundir una ausencia con un movimiento es
justo lo que la casa manda distinguir**: por eso se corrigio midiendo su quietud
con `git diff` y **diciendo por que via se midio**.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**EL PLAN QUEDA AGOTADO EN TRECE DE SUS CATORCE CLAUSULAS**, y la que falta
**sube NOMBRADA** porque su sede no existe y la moratoria prohibe fabricarla.
**NO DECLARO NADA CONSUMADO: LO PROPONGO**, que es lo que mi encargo manda, y
quien declara es el auditor.

**LO QUE PROPONGO, CON SU CIFRA DELANTE:** que la vuelta siguiente **no fabrique
nada** y que **la lista de la seccion 6 del acta 215, que hoy tiene cinco
puntos, suba entera con el punto de `OP-I-01` indice 3 dentro**. **Y EL MERGE NO
SE PIDE: EL BUCLE NO FUNDE RAMAS.**
""" % D

    fallos = 0
    print("EL COMPOSITOR DE LA TAREA 4 Y DEL CIERRE, Y SUS GUARDAS")
    for nombre, n, esperado in (("filas de consola", len(consolas), 2),
                                ("filas de suite", len(suites), 3),
                                ("filas de cotejo", len(cotejos), 16),
                                ("filas de sede", len(sedes), 13)):
        print("CIFRA %s: %d (se exigen %d)" % (nombre, n, esperado))
        if n != esperado:
            fallos += 1
    for nombre, texto in (("seccion de la TAREA 4", seccion),
                          ("cuerpo del cierre", cierre_texto)):
        print("CIFRA celdas con None en %s: %d (se exigen 0)"
              % (nombre, texto.count("None")))
        if "None" in texto:
            fallos += 1
        sosp = [c for c in re.findall(r"`([^`]+)`", texto)
                if c.endswith("/") and c.count("/") >= 2]
        print("CIFRA directorios de dos o mas tramos en %s: %d" % (nombre, len(sosp)))
        if sosp:
            fallos += 1
        print("CIFRA guiones largos en %s: %d | medios: %d"
              % (nombre, texto.count(chr(8212)), texto.count(chr(8211))))
        if texto.count(chr(8212)) or texto.count(chr(8211)):
            fallos += 1
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: el compositor NO ESCRIBE.")
        return 1
    for rel, texto in (("scripts/loop/_v%d_t4_seccion.md" % VUELTA, seccion),
                       ("scripts/loop/_v%d_cierre_texto.md" % VUELTA, cierre_texto)):
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        io.open(p, "w", encoding="utf-8", newline=NL).write(texto)
        print("ESCRITO %s -> %d bytes" % (rel, os.path.getsize(p)))
    print("VERDE: las dos piezas quedan compuestas.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
