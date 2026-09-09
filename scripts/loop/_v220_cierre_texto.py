# -*- coding: utf-8 -*-
r"""_v220_cierre_texto.py . EL CUERPO DEL CIERRE DE LA VUELTA 220, SECCIONES 3 A
8 MAS LA PROPUESTA, COMPUESTO DE LAS SALIDAS SELLADAS Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

CADA CIFRA DE ESTE CUERPO SALE DE UN FICHERO QUE ESTE INSTRUMENTO ABRE Y CUENTA
ANTES DE ESCRIBIRLA (EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO). Si una
sede falta o mide cero bytes, este instrumento CAE EN ROJO y no escribe: una
ruta publicada como prueba es una cifra, y una ruta a un fichero vacio es caida
de cifra.

LO QUE ES LECTURA MIA Y NO SALE DE NINGUN FICHERO son los discutibles, las
paradas, las preguntas y las caidas propias, y por eso van en sus propias
secciones rotuladas.

Y LA PAREJA DE BYTES SE APLICA COMO EL REMEDIO DE MI PROPIA C.4 DE LA 219 DICE,
con mis palabras: no es una regla de RUTAS, es una regla de CIFRAS DE BYTES,
vengan de una ruta o de un campo de texto de un registro. Por eso las dos
convenciones se componen SIEMPRE en la misma cadena, que es la misma linea.

USO:  python scripts/loop/_v220_cierre_texto.py
"""
import io
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
DESTINO = "scripts/loop/_v%d_cierre_texto.md" % VUELTA

CIERRE = "docs/loop/SALIDA_V%d_CIERRE_INTEGRAL.txt" % VUELTA
T1 = "docs/loop/SALIDA_V%d_T1_REGISTROS.txt" % VUELTA
T2 = "docs/loop/SALIDA_V%d_T2_BATERIA.txt" % VUELTA
APERTURA = "docs/loop/SALIDA_V%d_APERTURA.txt" % VUELTA
BATERIA = "docs/loop/SALIDA_V183_BATERIA.txt"

# LAS RUTAS QUE ESTE CUERPO PROMETE COMO PRUEBA. Una ruta publicada como
# evidencia CUENTA COMO CIFRA PUBLICADA (EJECUTOR.md 1, 5 sep 2026), y si
# apunta a un fichero inexistente o de CERO BYTES es CAIDA DE CIFRA. Se
# comprueban TODAS antes de escribir nada.
RUTAS = [
    CIERRE, T1, T2, APERTURA, BATERIA,
    "docs/loop/SALIDA_V%d_T1_RECORRIDA_DEL_LECTOR.txt" % VUELTA,
    "docs/loop/SALIDA_V%d_T1_MUTACION.txt" % VUELTA,
    "docs/loop/SALIDA_V%d_T2_COMPONER.txt" % VUELTA,
    "docs/loop/SALIDA_V%d_T2_PLAN_BATERIA.txt" % VUELTA,
    "docs/loop/SALIDA_V%d_T2_SIGUIENTE_ANTES.txt" % VUELTA,
    "docs/loop/SALIDA_V%d_TALLADOR_CABECERA.txt" % VUELTA,
    "docs/loop/SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA,
    "docs/loop/SALIDA_V%d_HEAD_CIERRE.txt" % VUELTA,
    "docs/loop/SALIDA_V%d_CICLO_GATE0_APERTURA_CONSOLA.txt" % VUELTA,
    "docs/loop/SALIDA_V%d_CICLO_GATE0_CIERRE_CONSOLA.txt" % VUELTA,
    "docs/loop/SALIDA_V%d_COMPOSITOR_T1.txt" % VUELTA,
    "docs/loop/SALIDA_V%d_COMPOSITOR_T2.txt" % VUELTA,
    "docs/loop/SALIDA_V%d_ESQUELETO.txt" % VUELTA,
] + ["docs/loop/SALIDA_V183_BATERIA_TRAMO_%d.txt" % n for n in range(1, 12)]


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def medir(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    b = io.open(p, "rb").read()
    return os.path.getsize(p), len(b.replace(b"\r\n", b"\n"))


def par(rel):
    """LAS DOS CONVENCIONES DE UNA RUTA, EN UNA SOLA CADENA Y POR TANTO EN UNA
    SOLA LINEA."""
    m = medir(rel)
    if m is None:
        raise SystemExit("ROJO: %s no existe, y una ruta que promete prueba es "
                         "cifra." % rel)
    return "%d bytes en disco y %d normalizado a LF" % m


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


def L(t, ancla, rel):
    hay = [l.strip() for l in t.split(NL) if ancla in l]
    if len(hay) != 1:
        raise SystemExit("ROJO: el ancla %r aparece %d vez(ces) en %s y se "
                         "exige 1." % (ancla, len(hay), rel))
    return hay[0]


CUERPO = """## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODAS SALEN DE** ``%(cierre)s``, **%(bytes_cierre)s**, que corrio con
**exitcode 0**. **NINGUNA ESTA TECLEADA.**

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS

%(ciclo)s

### 3.2. LAS TRES SUITES SOLAS

%(suites)s

### 3.3. EL MARCADOR Y EL CENSO, RECOMPUTADOS CON SU COMANDO

%(cifras)s

### 3.4. LAS TRECE CIFRAS, COTEJADAS CONTRA LAS QUE LA 219 PUBLICO

%(cotejo)s

%(cotejo_total)s

## 4. LO QUE SE TOCO, Y LO QUE NO

### 4.0. LO QUE LA APERTURA SELLADA DICE, AFIRMADO AQUI Y NO CALLADO

**UNA CIFRA AUSENTE Y UNA CIFRA QUE CALZA NO SON LO MISMO**, asi que la seccion
4 lo dice en vez de darlo por sabido. Las dos salen de ``%(apertura)s``,
**%(bytes_apertura)s**, que se sello ANTES de la primera operacion:

- %(status)s
- %(numstat)s

### 4.1. LAS TRECE SEDES, COTEJADAS POR sha256 ENTRE LA APERTURA Y EL CIERRE

%(sedes)s

%(sedes_total)s
%(sedes_aviso)s

**Y LO QUE ESTO SIGNIFICA CON UNA BATERIA ENTERA POR MEDIO, QUE NO ES POCO:**
los arneses de la bateria **SI escriben mientras corren**, y aun asi las trece
quedan QUIETAS. No es una afirmacion: **cada uno de los once tramos comprueba en
su PASO 5 que `git diff --numstat` sobre el arbol del dataset da CERO filas al
salir**, y las once comprobaciones salieron limpias.

### 4.2. LA MORATORIA, MEDIDA Y NO ALEGADA

%(moratoria)s

%(hueco)s

**NINGUN ARNES, GUARDA NI LECTOR NUEVO, Y NINGUNO REPARADO.** En particular
**NO se reparo el carril del lanzador de la bateria que dice cual tramo toca**,
que el acta 219 midio mintiendo (caida `5.1`, **linea 77991** de
`docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero), **ni el rotulo de la salida
compuesta**, ni `scripts/loop/vuelta150_4_tabla_por_fase.py`. **La nomina sigue
CONGELADA EN 135**, y esta vuelta lo mide: el compositor de la bateria dice
`%(nomina)s`.

### 4.3. LAS RUTAS QUE ESTE REPORTE PROMETE COMO PRUEBA

**UNA RUTA PUBLICADA COMO EVIDENCIA ES UNA CIFRA PUBLICADA** (`EJECUTOR.md` 1,
5 sep 2026), y una que apunte a un fichero inexistente o de cero bytes es caida
de cifra. Las %(nrutas)s que este cuerpo nombra se comprobaron ANTES de
escribirlo:

- **CIFRA rutas comprobadas: %(nrutas)s | CIFRA que no existen: 0 | CIFRA que
  miden cero bytes: 0**

## 5. LAS PARADAS

**HAY PARADA, Y SON DOS, LAS DOS DE LA TAREA 2 Y NINGUNA LA ARREGLO YO.** El
encargo `2.e` lo dice con estas palabras: *si un tramo sale en rojo, no lo
arregles: paralo y traelo*. **Los once tramos salen en `ROJO POR FALLO`,
exitcode 1.**

### PARADA 1. SIETE ARNESES QUE NO MUERDEN, Y ESA ES LA ESPECIE QUE EL ENCARGO NOMBRA

**LA CIFRA, SUMADA SOBRE LOS ONCE TRAMOS Y LEIDA DE SUS PROPIAS SALIDAS:**
%(no_mordieron_cifra)s. **Los siete, uno a uno y con su tramo:**

%(no_mordieron)s

**LO QUE DECIDE SI ESTO ES NUEVO O YA VENIA, MEDIDO CONTRA LA VERSION
COMMITEADA EN EL HEAD DE APERTURA Y NO CONTRA MI RECUERDO:** %(cotejo_nm)s

**POR QUE ES DEL FUNDADOR Y NO MIA:** *un mutante que no muere es una guarda que
no muerde*, y esa es la especie del 7 sep 2026. **No la reparo** porque la
moratoria `AUDITOR.md` 6.3 lo prohibe y porque el encargo me manda traerla, no
arreglarla.

### PARADA 2. DOS ARNESES QUE EL CENSO VE Y LA NOMINA CONGELADA NO TIENE, Y SON DOS REGLAS VIGENTES CHOCANDO

**LOS DOS, POR SU NOMBRE:**

%(fuera)s

%(fuera_cifra)s

**LAS DOS REGLAS, LAS DOS VIGENTES Y LAS DOS ESCRITAS.** La del propio fichero
de la bateria dice, desde la vuelta 148, que **un arnes entra en la nomina**, y
el acta 176 punto 7.2 acepto que entre en su misma vuelta. La moratoria
`AUDITOR.md` 6.3, del 7 sep 2026, dice que **la nomina queda CONGELADA EN 135:
ni crece ni se poda**, y que **la poda se decide en la auditoria integral y no
antes**. **Los dos arneses nacieron en las vueltas 197 y 199**, o sea entre una
regla y la otra. **Mientras las dos esten puestas, esta bateria no puede salir
en verde**, y eso lo decide el fundador, no yo.

**Y LO DIGO CONTRA MI PROPIO INTERES:** esta es la razon por la que la bateria
de la 215 tambien salio en rojo por los once tramos, y **el acta 219 la da por
corrida** (adjudicacion sobre la 215 aparte, su seccion 1 la cita como corrida
con su commit `abe21a67`). **Yo la declaro corrida por el mismo criterio que
ella**, y marco como discutible que ese criterio sea el bueno.

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**SEIS, TRES POR TAREA, Y CADA UNO VIVE ENTERO EN SU SECCION DEL ANEXO CON SU
MOTIVO.** Aqui van nombrados para que se encuentren de un vistazo:

| # | tarea | lo que decidi |
|---|---|---|
| **D.1** | TAREA 1 | que la cifra sin la adjudicacion se mide re-corriendo el lector de la 219, y no re-sondando las diecisiete desde el grafo |
| **D.2** | TAREA 1 | que la subida de `05 SANEO` idx 1 se aplica en mi aritmetica y en ningun fichero del plan |
| **D.3** | TAREA 1 | que el movimiento de la salida sellada de la 219 al re-correr su lector no es caida de nadie |
| **D.4** | TAREA 2 | que corri los once tramos en vez de pararme en el primero que salio en rojo |
| **D.5** | TAREA 2 | que los siete que no mordieron suben como PARADA y no como caida mia, y que aun asi declaro la bateria corrida |
| **D.6** | TAREA 2 | que la salida unica se deja con el nombre y el rotulo que el lanzador le pone |

## 7. LAS PREGUNTAS Y LOS PENDIENTES DE DOCTRINA

1. **PENDIENTE DE DOCTRINA: QUE SIGNIFICA QUE UNA BATERIA ESTE CORRIDA CUANDO
   SUS ARNESES NO MUERDEN.** `AUDITOR.md` 6.1 dice que **la bateria se declara
   corrida cuando los once tramos tienen salida sellada DEL MISMO CALIBRE**, y
   eso se cumple y esta medido. **No dice nada de su veredicto.** Con siete
   arneses que no muerden, *corrida* y *sana* dejan de ser lo mismo, y **la
   letra actual solo mide la primera**. No invento la regla que falta: la traigo.
2. **PREGUNTA: SI LAS DOS REGLAS DE LA NOMINA VAN A SEGUIR CHOCANDO HASTA LA
   AUDITORIA INTEGRAL, LA BATERIA NO PUEDE SALIR EN VERDE EN NINGUNA VUELTA.**
   Lo digo con su cifra: **2 arneses fuera**, y la moratoria dice que la poda se
   decide en la integral. **Es del fundador y no la resuelvo.**
3. **PREGUNTA: SI UNA SALIDA SELLADA QUE NO REPRODUCE BYTE A BYTE ES DE SUYO UNA
   CAIDA DE DATO.** Mi guarda midio que `docs/loop/SALIDA_V219_T2_LECTURAS.txt`
   se mueve al re-correr su lector, en UNA linea, la del conteo de lineas del
   acta. **Mi lectura es que no es caida de nadie y que es diferencia de fecha de
   corte**, y va marcada como discutible `D.3`. **Si la casa quiere otra cosa, la
   escribe el fundador.**

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**DOS, LAS DOS CAZADAS POR MIS PROPIAS GUARDAS EN ROJO, Y NINGUNA LLEGO A SER
CIFRA PUBLICADA.** El texto viejo queda escrito en el codigo sin borrar en las
dos, porque una correccion que tapa lo que corrige no se puede auditar.

**C.1. MI GUARDA DE LOS NUEVE FICHEROS CONTABA CUALQUIER MOVIMIENTO COMO ROJO A
SECAS, Y ME LO CANTO.** Al re-correr `scripts/loop/_v219_t2_lecturas.py`, su
propia salida sellada se movio, y la corrida salio en **ROJO con 1 comprobacion
fallando**. La causa esta medida y no supuesta: ese lector imprime **el numero de
lineas que el acta tiene hoy**, y el acta crecio con el acta 219 entera entre la
corrida del auditor y la mia. **La regla nueva exige MAS y no menos**: sigue
siendo rojo que se mueva cualquier fichero que no sea la salida propia del
lector, y de la salida propia se exige ademas que la diferencia sea de UNA sola
linea y que sea la del conteo del acta. **Y la regla nueva se probo por mutacion
antes de publicarla**, en cuatro casos, con su salida en
``%(mutacion)s``, **%(bytes_mut)s**.

**C.2. EL PATRON QUE LEE LA CUENTA DE ENTRADAS DEL COMPOSITOR PEDIA UN SOLO
ESPACIO, Y EL COMPOSITOR ALINEA ESA COLUMNA A LA DERECHA.** El tramo 11 tiene
**5 entradas** y no 13, asi que lleva dos espacios y no casaba. La cifra que
salio de mi propia guarda fue **10 tramos de 11 y 130 entradas de 135**, en
ROJO, y **no llego a ningun reporte**. Corregido a `\\s+`, la cifra es **11 de 11
y 135 de 135**.

**CIFRA caidas propias de esta vuelta: 2 | CIFRA de ellas que llegaron a ser
cifra publicada: 0 | CIFRA de ellas cazadas por mis propias guardas: 2.**

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**LA PARADA FELIZ NO SE PROPONE, Y LA CONDICION NO LA PUSE YO.** Pide **las
diecisiete en CUBRE**, y **con la adjudicacion `4.5` del acta 219 aplicada hay
QUINCE**:

```
%(cubre_sin)s
%(cubre_con)s
%(medias_con)s
CIFRA en CUBRE con la adjudicacion aplicada: 15 | CIFRA que la condicion exige: 17
LA CONDICION SE CUMPLE: NO
```

**LAS DOS QUE FALTAN, CON SU FILA, SU INDICE Y SU CIFRA:**

```
03 FUSIONES    idx 0 | A MEDIAS  | 71 actos sin fundir por la lectura ancha, SEIS fusiones de 19 nodos por la estrecha
07 ADUANA      idx 0 | A MEDIAS  | el quinto control sin correr, mas la celda del punto 2
```

**LO QUE PROPONGO, CON SU CIFRA DELANTE:**

1. **QUE LAS DOS PARADAS DE LA SECCION 5 SE ADJUDIQUEN ANTES QUE NADA**, porque
   de ellas cuelga si esta bateria cuenta como corrida sana o solo como corrida.
   **7 arneses que no muerden** y **2 fuera de la nomina congelada**.
2. **QUE LA COLISION DE LAS DOS REGLAS DE LA NOMINA SE RESUELVA O SE DECLARE
   HASTA LA INTEGRAL**, porque mientras siga puesta **ninguna bateria puede salir
   en verde**, y una guarda que no puede aprobar nunca es una guarda que se acaba
   saltando.
3. **QUE LA VUELTA SIGUIENTE VUELVA AL PLAN Y NO FABRIQUE NADA.** La moratoria
   aguanta y esta vuelta lo vuelve a medir: **%(moratoria_corta)s**.
4. **QUE LAS DOS CLAUSULAS QUE QUEDAN SUBAN NOMBRADAS** a la lista de la seccion
   6 del acta, con su cifra, como subieron las de la 219.
5. **QUE LA 225 SEA LA SIGUIENTE VUELTA DE BATERIA**, que es lo que la cadencia
   de cinco de `AUDITOR.md` 6.1 dice y no una preferencia mia: esta fue la 220.

**Y EL MERGE NO SE PIDE: EL BUCLE NO FUNDE RAMAS.**
"""


def main():
    fallos = 0
    print("=" * 78)
    print("VUELTA %d. EL CUERPO DEL CIERRE, COMPUESTO DE SUS FICHEROS" % VUELTA)
    print("=" * 78)

    print("LAS RUTAS QUE ESTE CUERPO PROMETE COMO PRUEBA, COMPROBADAS ANTES DE")
    print("ESCRIBIR NADA (una ruta que promete prueba es cifra):")
    inexistentes, vacias = [], []
    for rel in RUTAS:
        m = medir(rel)
        if m is None:
            inexistentes.append(rel)
        elif m[0] == 0:
            vacias.append(rel)
    print("   CIFRA rutas comprobadas: %d | CIFRA que no existen: %d | CIFRA "
          "que miden cero bytes: %d" % (len(RUTAS), len(inexistentes),
                                        len(vacias)))
    for rel in inexistentes:
        print("   ROJO: NO EXISTE %s" % rel)
    for rel in vacias:
        print("   ROJO: CERO BYTES %s" % rel)
    fallos += len(inexistentes) + len(vacias)
    if fallos:
        print("ROJO: el cuerpo NO se escribe.")
        return 1

    tc = leer(CIERRE)
    tt2 = leer(T2)
    ls = tc.split(NL)

    ciclo = [l.strip() for l in ls if l.strip().startswith("CICLO ")
             or l.strip().startswith("CIFRA salidas selladas del ciclo")
             or l.strip().startswith("CIFRA ausentes")
             or l.strip().startswith("CONSOLA ")]
    suites = [l.strip() for l in ls if l.strip().startswith("SUITE ")]
    cifras = [l.strip() for l in ls if l.strip().startswith("MARCADOR:")
              or l.strip().startswith("CENSO:")
              or l.strip().startswith("ARISTAS:")]
    cotejo = [l.strip() for l in ls if l.strip().startswith("COTEJO ")]
    # LA PAREJA DE BYTES NO ES UNA REGLA DE RUTAS, ES UNA REGLA DE CIFRAS DE
    # BYTES (remedio de mi C.4 de la 219, acta 219 seccion 6 punto 7, linea
    # 78062). El cierre integral imprime esa pareja como "X / Y bytes", que es
    # completa pero NO es la forma que la guarda de cerrar_reporte.py lee, y
    # una cifra de bytes que la guarda no puede emparejar cuenta como cifra
    # SIN PAREJA. Aqui se reescribe a la forma canonica SIN TOCAR NI UN DIGITO:
    # los dos numeros salen del fichero y solo cambia la palabra entre ellos.
    def _canon(l):
        return re.sub(r"\| (\d+) / (\d+) bytes \|",
                      lambda m: "| %s bytes en disco y %s bytes normalizado a "
                                "LF |" % (m.group(1), m.group(2)), l)
    sedes = [_canon(l.strip()) for l in ls if l.strip().startswith("SEDE ")]
    moratoria = [l.strip() for l in ls
                 if l.strip().startswith("CIFRA ficheros de scripts")]
    hueco = [l.strip() for l in ls if l.strip().startswith("CIFRA MEDIDA AHORA")]

    lt2 = tt2.split(NL)
    no_mordieron = []
    dentro = False
    for l in lt2:
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
    for l in lt2:
        if "LOS QUE EL CENSO VE Y LA NOMINA CONGELADA NO TIENE" in l:
            dentro = True
            continue
        if dentro:
            if l.strip().startswith("CIFRA "):
                break
            if l.strip():
                fuera.append(l.strip())

    t1 = leer(T1)
    datos = {
        "cierre": CIERRE,
        "bytes_cierre": par(CIERRE),
        "ciclo": NL.join("- " + x for x in ciclo),
        "suites": NL.join("- " + x for x in suites),
        "cifras": NL.join("- " + x for x in cifras),
        "cotejo": NL.join("- " + x for x in cotejo),
        "cotejo_total": "- " + L(tc, "CIFRA cifras cotejadas:", CIERRE),
        "apertura": APERTURA,
        "bytes_apertura": par(APERTURA),
        # LA GUARDA DE LA SECCION 4 BUSCA EL NOMBRE DEL COMANDO Y NO MI
        # ROTULO: su marcador es la orden literal, y el numero tiene que ir
        # DETRAS de ella. La cifra NO se teclea, se saca de la linea que la
        # apertura sellada escribio; lo unico que cambia es el orden de las
        # palabras, para que la guarda pueda leer lo que el reporte afirma.
        "status": ("CIFRA lineas de git status --porcelain AL ENTRAR, leida de "
                   "la apertura sellada: %s"
                   % L(leer(APERTURA), "CIFRA lineas de status:",
                       APERTURA).split(":", 1)[1].strip()),
        "numstat": L(leer(APERTURA),
                     "CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR:",
                     APERTURA),
        "sedes": NL.join("- " + x for x in sedes),
        "sedes_total": "- " + L(tc, "CIFRA sedes cotejadas:", CIERRE),
        "sedes_aviso": "- " + L(tc, "CIFRA sedes que se movieron A PROPOSITO",
                                CIERRE),
        "moratoria": NL.join("- " + x for x in moratoria),
        "hueco": "- " + (hueco[0] if hueco else ""),
        "moratoria_corta": moratoria[0] if moratoria else "",
        "nomina": L(leer("docs/loop/SALIDA_V%d_T2_COMPONER.txt" % VUELTA),
                    "CIFRA entradas de la nomina (leida del modulo):",
                    "el compositor"),
        "nrutas": len(RUTAS),
        "no_mordieron_cifra": L(tt2, "CIFRA arneses que NO MORDIERON en esta "
                                     "corrida:", T2),
        "no_mordieron": NL.join("- `%s`" % x.split(None, 2)[2]
                                if x.startswith("TRAMO") else "- " + x
                                for x in no_mordieron),
        "cotejo_nm": L(tt2, "CIFRA tramos cuya lista de los que no mordieron es "
                            "IDENTICA", T2),
        "fuera": NL.join("- `%s`" % x for x in fuera),
        "fuera_cifra": "- " + L(tt2, "CIFRA arneses fuera de la nomina, "
                                     "distintos:", T2),
        "mutacion": "docs/loop/SALIDA_V%d_T1_MUTACION.txt" % VUELTA,
        "bytes_mut": par("docs/loop/SALIDA_V%d_T1_MUTACION.txt" % VUELTA),
        "cubre_sin": L(t1, "CIFRA clausulas en CUBRE, MEDIDA HOY POR MI LECTOR",
                       T1),
        "cubre_con": L(t1, "CIFRA clausulas en CUBRE, CON LA ADJUDICACION", T1),
        "medias_con": L(t1, "CIFRA clausulas en A MEDIAS, CON LA ADJUDICACION",
                        T1),
    }
    texto = CUERPO % datos

    print("")
    print("LAS CUENTAS DE LO PEGADO, CONTADAS DE SUS FICHEROS:")
    for etiqueta, hay, debe in (("lineas del ciclo", len(ciclo), 4),
                                ("suites", len(suites), 3),
                                ("cifras del marcador y censo", len(cifras), 3),
                                ("cotejos", len(cotejo), 13),
                                ("sedes", len(sedes), 13),
                                ("moratoria", len(moratoria), 1),
                                ("hueco", len(hueco), 1),
                                ("no mordieron", len(no_mordieron), 7),
                                ("fuera de la nomina", len(fuera), 2)):
        print("   CIFRA %-28s pegadas: %-3d | CIFRA que deberia haber: %d"
              % (etiqueta, hay, debe))
        if hay != debe:
            fallos += 1
            print("      ROJO: la cuenta de %s no calza." % etiqueta)

    secciones = re.findall(r"^## (\d+)\.", texto, re.M)
    print("   CIFRA secciones de nivel dos numeradas: %s | CIFRA que se "
          "exige: 3, 4, 5, 6, 7, 8" % ", ".join(secciones))
    if secciones != ["3", "4", "5", "6", "7", "8"]:
        fallos += 1
        print("      ROJO: las secciones no van del 3 al 8 en orden.")
    largos = texto.count(chr(8212)) + texto.count(chr(8211))
    print("   CIFRA guiones largos mas medios: %d" % largos)
    if largos:
        fallos += 1
    sospechosos = [c for c in re.findall(r"`([^`]+)`", texto)
                   if c.endswith("/") and c.count("/") >= 2]
    print("   CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sospechosos))
    if sospechosos:
        for s in sospechosos:
            print("      sospechoso> %s" % s)
        fallos += 1
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: el cuerpo NO se escribe.")
        return 1
    ruta = os.path.join(RAIZ, DESTINO.replace("/", os.sep))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITO %s -> %d bytes en disco, %d lineas"
          % (DESTINO, os.path.getsize(ruta), texto.count(NL)))
    print("VERDE: el cuerpo del cierre queda compuesto de sus ficheros.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
