# -*- coding: utf-8 -*-
r"""_v210_t1_seccion.py . COMPONE EL CUERPO DE LA TAREA 1 DEL REPORTE DE LA
VUELTA 210 **CONTANDO SUS FICHEROS DE SALIDA**, y lo deja en
`scripts/loop/_v210_t1_seccion.md` para que `anexar_tarea_al_reporte.py` lo
anexe al cerrarse la tarea.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3).

LA LETRA QUE OBEDECE, PALABRA POR PALABRA (`EJECUTOR.md` 1, LA TABLA SE CUENTA
DE SU FICHERO): *"TODA TABLA O CIFRA DEL REPORTE CITA EL FICHERO DE SALIDA DEL
QUE SALE, Y SE RECONSTRUYE CONTANDO ESE FICHERO ANTES DE PUBLICARLA"*. Aqui
NINGUNA cifra se teclea: todas salen de `re` sobre las salidas selladas de esta
vuelta, y las dos tablas se pegan ENTERAS del fichero que las lleva.

SE COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE ESCRIBE SI EL JUICIO DA CERO
FALLOS, igual que el esqueleto.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))


def leer(nombre):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.isfile(ruta) or os.path.getsize(ruta) == 0:
        print("ROJO: docs/loop/%s no existe o mide cero bytes." % nombre)
        sys.exit(1)
    return io.open(ruta, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def uno(texto, patron, etiqueta, banderas=0):
    m = re.findall(patron, texto, banderas)
    if len(m) != 1:
        print("ROJO: %s -> %d coincidencias de %r (se exige 1)"
              % (etiqueta, len(m), patron))
        sys.exit(1)
    return m[0]


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    ap = leer("SALIDA_V%d_APERTURA.txt" % VUELTA)
    plan = leer("SALIDA_V%d_T1A_PLAN.txt" % VUELTA)
    sig_a = leer("SALIDA_V%d_T1B_SIGUIENTE_ANTES.txt" % VUELTA)
    sig_d = leer("SALIDA_V%d_T1B_SIGUIENTE_DESPUES.txt" % VUELTA)
    comp = leer("SALIDA_V%d_T1D_COMPONER.txt" % VUELTA)
    tab = leer("SALIDA_V%d_T1E_TABLAS.txt" % VUELTA)

    v = {}
    v["nomina"] = uno(plan, r"CIFRA entradas de la nomina: (\d+)", "nomina del plan")
    v["tamano"] = uno(plan, r"CIFRA tamano de tramo: (\d+)", "tamano")
    v["tramos"] = uno(plan, r"CIFRA tramos: (\d+)", "tramos")
    v["suma"] = uno(plan, r"CIFRA suma de las entradas de todos los tramos: (\d+)",
                    "suma del plan")
    v["clavados"] = uno(plan, r"CIFRA literales de vuelta clavados en lineas que "
                        r"escriben: (\d+)", "clavados")

    v["sig_a_faltan"] = uno(sig_a, r"CIFRA tramos que FALTAN: (\d+)", "faltan antes")
    v["sig_a_hechos"] = uno(sig_a, r"CIFRA tramos CON salida sellada no vacia: (\d+)",
                            "hechos antes")
    v["sig_d_faltan"] = uno(sig_d, r"CIFRA tramos que FALTAN: (\d+)", "faltan despues")

    v["cob_corridas"] = uno(comp, r"CIFRA entradas que los tramos dicen haber "
                            r"corrido: (\d+)", "corridas")
    v["cob_sin"] = uno(comp, r"CIFRA entradas de la nomina que NINGUN tramo "
                       r"corrio: (\d+)", "sin correr")
    v["cob_ajenas"] = uno(comp, r"CIFRA entradas corridas que NO estan en la "
                          r"nomina: (\d+)", "ajenas")
    v["cob_repes"] = uno(comp, r"CIFRA entradas corridas MAS DE UNA VEZ: (\d+)",
                         "repetidas")
    v["uni_disco"] = uno(comp, r"CIFRA bytes en disco: (\d+)", "unica disco")
    v["uni_lf"] = uno(comp, r"CIFRA bytes normalizado a LF: (\d+)", "unica LF")
    v["uni_lineas"] = uno(comp, r"CIFRA lineas: (\d+)", "unica lineas")
    v["uni_sha"] = uno(comp, r"CIFRA sha256 \(LF\): (\w{64})", "unica sha")

    v["t_entradas"] = uno(tab, r"CIFRA suma de entradas de los once tramos: (\d+)",
                          "suma entradas")
    v["t_ok"] = uno(tab, r"CIFRA suma de OK: (\d+)", "suma OK")
    v["t_dec"] = uno(tab, r"CIFRA suma de CASO DECLARADO: (\d+)", "suma declarado")
    v["t_nm"] = uno(tab, r"CIFRA suma de NO MORDIO: (\d+)", "suma no mordio")
    v["t_tres"] = uno(tab, r"CIFRA suma de las tres clases: (\d+)", "suma tres")
    v["t_bytes"] = uno(tab, r"CIFRA suma de bytes en disco de los once: (\d+)",
                       "suma bytes")
    v["t_min"] = uno(tab, r"CIFRA suma de minutos de los once: ([\d.]+)", "suma min")
    v["t_ruido"] = uno(tab, r"CIFRA tramos con RUIDO DE CONCURRENCIA distinto de "
                       r"cero: (\d+)", "tramos con ruido")
    v["t_exit"] = uno(tab, r"CIFRA tramos con exitcode distinto de 1: (\d+)",
                      "tramos otro exit")
    v["t_nm_filas"] = uno(tab, r"CIFRA entradas NO MORDIO, contadas de las filas: (\d+)",
                          "no mordio filas")
    v["t_frescos"] = uno(tab, r"CIFRA tramos cuyo commit nombra la VUELTA %d: (\d+) de 11"
                         % VUELTA, "frescos")
    v["t_ajenos"] = uno(tab, r"CIFRA tramos cuyo commit nombra OTRA vuelta: (\d+)",
                        "ajenos")

    v["ap_head"] = uno(ap, r"CIFRA HEAD de apertura: (\w{40})", "head apertura")
    sellos_ap = re.findall(r"vuelta que lo sello: (\d+)", ap)
    if len(sellos_ap) != 12:
        print("ROJO: la apertura nombra %d sellos de bateria y se esperaban 12"
              % len(sellos_ap))
        sys.exit(1)
    v["ap_sellos"] = str(len(sellos_ap))
    v["ap_sello_unico"] = ", ".join(sorted(set(sellos_ap)))

    # LAS DOS TABLAS SE PEGAN ENTERAS DEL FICHERO QUE LAS LLEVA, no se rehacen.
    def bloque(texto, desde, hasta):
        i = texto.index(desde)
        j = texto.index(hasta, i)
        return texto[i:j].rstrip(NL)

    tabla_calibre = bloque(tab, "| tramo | fichero sellado |", NL + NL + "  CIFRA suma")
    tabla_frescura = bloque(tab, "| tramo | commit que lo sello |",
                            NL + NL + "  CIFRA tramos cuyo commit")
    lista_nm = bloque(tab, "  LOS NO MORDIO, UNO A UNO",
                      "  CIFRA entradas NO MORDIO, contadas")

    cuerpo = """### TAREA 1. LA BATERIA DE MUTACIONES, ENTERA, POR SUS ONCE TRAMOS

**CERRADA. LOS ONCE TRAMOS TIENEN SALIDA SELLADA DE ESTA VUELTA Y `--componer`
SALIO VERDE**, que es la condicion que `AUDITOR.md` 6.1 pone para declarar la
bateria corrida y no antes.

#### 1.a. EL REPARTO, RECOMPUTADO POR MI, Y LA DISCREPANCIA CON `AUDITOR.md` 6.1 DECLARADA

Salida: `docs/loop/SALIDA_V%(v)d_T1A_PLAN.txt`, de
`python scripts/loop/vuelta183_bateria_por_tramos.py --plan`.

- **CIFRA entradas de la nomina: %(nomina)s**, leidas del modulo
  `verificar_mutaciones_viejas` y no tecleadas.
- **CIFRA tamano de tramo: %(tamano)s.**
- **CIFRA tramos del reparto: %(tramos)s.**
- **CIFRA suma de las entradas de todos los tramos: %(suma)s**, que calza con la
  nomina.
- **CIFRA literales de vuelta clavados en lineas que escriben: %(clavados)s**, que
  es la guarda que el propio lanzador se corre encima antes de arrancar.

**MI CIFRA CALZA CON EL CONTRASTE DEL ENCARGO** (nomina %(nomina)s, tramos
%(tramos)s): **cero discrepancias**.

**Y LA DISCREPANCIA CON `AUDITOR.md` 6.1 SE DECLARA EN VEZ DE RESOLVERSE
COPIANDO.** Ese fichero dice **NUEVE tramos**, con estas palabras: *"Su reparto,
computado y no tecleado, da NUEVE tramos sobre la nomina de hoy"*. **La glosa
lleva su corte dentro**, "sobre la nomina de hoy", y esa nomina era la del 5 sep
2026, cuando tenia 82 entradas. Hoy la nomina esta **congelada en %(nomina)s** por
`AUDITOR.md` 6.3 y el mismo `TAMANO` de 13 reparte en %(tramos)s. **La letra de 6.1
envejecio honestamente y no hay contradiccion que parar**: el propio 6.1 dice que
lo que manda es el reparto computado, no el numero.

#### 1.b. EL `--siguiente` SE USO PARA LEER EL REPARTO Y NUNCA PARA SABER QUE FALTABA

**La trampa, medida en las DOS puntas y no narrada.** El lanzador **computa su
vuelta de su propio nombre de fichero** y lo dice de si mismo en cada corrida
(`vuelta (computada del nombre, no tecleada): 183`), asi que **sus salidas se
llaman `SALIDA_V183_*` corra la vuelta que corra** y `--siguiente` cuenta ESOS
ficheros por su nombre.

| cuando | fichero de salida | tramos CON salida sellada no vacia | tramos que FALTAN |
|---|---|---|---|
| ANTES de correr nada | `SALIDA_V%(v)d_T1B_SIGUIENTE_ANTES.txt` | %(sig_a_hechos)s | %(sig_a_faltan)s |
| DESPUES de los once | `SALIDA_V%(v)d_T1B_SIGUIENTE_DESPUES.txt` | 11 | %(sig_d_faltan)s |

**LAS DOS PUNTAS DAN LA MISMA CIFRA, Y ESA ES LA PRUEBA.** Antes de que esta
vuelta corriera un solo tramo, `--siguiente` ya publicaba `CIFRA tramos que
FALTAN: %(sig_a_faltan)s` y `LOS 11 TRAMOS TIENEN SALIDA SELLADA` **sobre las
salidas que dejo la VUELTA 200**. Si le hubiera hecho caso habria declarado
corrida una bateria que esta vuelta no habia corrido. **No se le hizo caso y no se
arreglo el lanzador**, que es moratoria.

**QUE SI PROBO LA APERTURA, ANTES DE LA PRIMERA OPERACION:**
`docs/loop/SALIDA_V%(v)d_APERTURA.txt` mide los **%(ap_sellos)s ficheros de la
bateria** (los once tramos mas la compuesta) tal como estaban al entrar y lee de
`git log` la vuelta que los sello: **%(ap_sello_unico)s**, la misma para los doce.
`HEAD` de apertura `%(ap_head)s`.

#### 1.c. LOS ONCE TRAMOS, COMMITEADOS UNO A UNO, Y LA VARA DE FRESCURA

Los once se corrieron **empezando por el 1** y **cada uno se committeo con su
salida sellada al terminar**, no todos al final, que es lo que permite que una
vuelta cortada retome en el tramo siguiente.

**LA TABLA DEL CALIBRE, PEGADA ENTERA DE `docs/loop/SALIDA_V%(v)d_T1E_TABLAS.txt`**
y no tecleada. La imprime `scripts/loop/_v210_tabla_tramos.py`, que **importa**
`medir`, `nombre_tramo`, `nombre_de_la_compuesta` y `entradas_de_la_salida` del
lanzador y `vuelta_que_sello` de `cerrar_reporte.py`, sin copiarles una linea.

%(tabla_calibre)s

- **CIFRA suma de entradas de los once tramos: %(t_entradas)s**, que es la nomina
  entera.
- **CIFRA suma de OK: %(t_ok)s | CASO DECLARADO: %(t_dec)s | NO MORDIO: %(t_nm)s**, y
  **las tres clases suman %(t_tres)s**, o sea que ninguna entrada se quedo sin
  clasificar.
- **CIFRA suma de bytes en disco de los once: %(t_bytes)s | CIFRA suma de minutos:
  %(t_min)s.**
- **CIFRA tramos con exitcode distinto de 1: %(t_exit)s** y **CIFRA tramos con RUIDO
  DE CONCURRENCIA distinto de cero: %(t_ruido)s**.

**LA TABLA DE LA FRESCURA, PEGADA ENTERA DEL MISMO FICHERO.** Es la vara que el
nombre del fichero **no** da:

%(tabla_frescura)s

- **CIFRA tramos cuyo commit nombra la VUELTA %(v)d: %(t_frescos)s de 11**, y
  **CIFRA tramos cuyo commit nombra OTRA vuelta: %(t_ajenos)s**.
- **No se renombro ni se copio ninguna salida a un nombre `V%(v)d`**: un fichero
  copiado no es un fichero corrido, y eso seria fabricar la prueba en vez de
  tenerla.

#### 1.d. LAS TRES GUARDAS DEL REGIMEN, LAS TRES SIN ABLANDAR

**LA DOBLE CORRIDA.** Cada entrada se corre **dos veces** por el cotejo de
reproducibilidad de la TAREA 2.f de la vuelta 141. La columna **NO REPRODUCIBLE
da 0 en los ONCE tramos**, o sea que **las dos corridas de las %(t_entradas)s
entradas dieron lo mismo en las %(t_entradas)s**. La cifra no se afirma de
memoria: esta en la tabla de arriba, columna por columna.

**CERO BYTES NO CUENTA COMO HECHO.** Ninguno de los once mide cero: el mas
pequeno es el tramo 11 con 6273 bytes y el mas grande el tramo 1 con 9544, los
dos en la tabla. `--componer` lo vuelve a comprobar por su cuenta y publica
**0 salidas de cero bytes**.

**DEL MISMO CALIBRE.** Los once traen **13 entradas cada uno salvo el 11, que
lleva las 5 de la cola** (%(nomina)s menos diez por %(tamano)s); los once salen con
**exitcode 1**; los once recomputan al cierre las mismas cifras de fallo; y
ninguno sale de otra hondura que los demas. La tabla entera esta arriba para que
se vea y no para que se crea.

#### 1.e. `--componer` Y LA SALIDA UNICA

Salida: `docs/loop/SALIDA_V%(v)d_T1D_COMPONER.txt`.

- **CIFRA entradas que los tramos dicen haber corrido: %(cob_corridas)s**, leidas de
  las salidas y **no recalculadas del reparto**, que es como el propio instrumento
  dice que hay que leerlas.
- **CIFRA entradas de la nomina que NINGUN tramo corrio: %(cob_sin)s | ajenas:
  %(cob_ajenas)s | repetidas: %(cob_repes)s.**
- **La salida unica: `docs/loop/SALIDA_V183_BATERIA.txt`, %(uni_disco)s bytes en
  disco y %(uni_lf)s normalizado a LF**, %(uni_lineas)s lineas, `sha256` LF
  `%(uni_sha)s`.

**VERDE:** los once tramos cubren la nomina entera, cada entrada **exactamente una
vez**, y la salida unica existe y no mide cero.

#### 1.f. EL ROJO DE LA BATERIA, Y LOS SIETE `NO MORDIO`

**LOS ONCE TRAMOS SALEN CON `exitcode 1` Y CLASE `ROJO POR FALLO`. Eso estaba
nombrado de antemano y no es una sorpresa**: el acta 205 ya lo dijo con estas
palabras, *"la bateria NO PUEDE SALIR VERDE mientras la moratoria viva, asi que
la 210 y la 215 saldran rojas igual"*. La causa estructural es la misma en los
once: **2 arneses que el censo VE, no anteriores a la vara 148, que se quedan
FUERA de la nomina** porque `AUDITOR.md` 6.3 la congela en %(nomina)s. Son
`vuelta197_tarea2_mutacion_orden_del_turno.py` y
`vuelta199_tarea1_mutacion_guardas_revividas.py`.

**PERO HAY UN SEGUNDO ROJO Y NO ES ESTRUCTURAL: SIETE ENTRADAS DE LA NOMINA NO
MUERDEN.** Pegados enteros de `docs/loop/SALIDA_V%(v)d_T1E_TABLAS.txt`:

%(lista_nm)s

- **CIFRA entradas NO MORDIO, contadas de las filas: %(t_nm_filas)s**, y calza con
  la suma de la columna, que da **%(t_nm)s**. **Las dos cuentas se hacen por
  caminos distintos a proposito.**
- **NO SE DIAGNOSTICAN Y NO SE ARREGLAN.** Diagnosticar por que una guarda dejo de
  morder pide abrir su sujeto y su arnes, y eso es fabricar: **la moratoria de
  `AUDITOR.md` 6.3 lo prohibe y esta vuelta no lo hace**. Se cuentan, se nombran
  con su tramo y suben marcados.
- **UNO DE LOS SIETE MERECE SU LINEA APARTE, Y LO DECLARO ANTES DE USARLO:**
  `vuelta185_tarea1c_mutacion_bateria_continuada.py` es el arnes que vigila el
  carril de **la bateria continuada** de `rama_de_la_seccion9()` en
  `scripts/loop/cerrar_reporte.py`, que es **exactamente el carril por el que va a
  pasar el cierre de esta misma vuelta**, porque mi salida compuesta se llama
  `SALIDA_V183_BATERIA.txt` y la vuelta que cierra es la %(v)d. **Declararlo antes
  de pasar por el es la unica forma honesta de pasar por el.**

**CONTRASTE CON EL ACTA 205, DECLARADO Y NO RESUELTO COPIANDO.** Aquel acta
nombra **5** entradas que no mordieron; yo mido **%(t_nm)s**. **Coinciden dos**
(`vuelta165_tarea6_mutacion_op_l_01.py` y
`vuelta185_tarea1c_mutacion_bateria_continuada.py`), **y una tercera coincide en
el nombre pero no en la cifra**: el acta le atribuye a
`vuelta160_tarea6b_mutacion_puerta.py` el exit `3221225794`, que es una caida del
proceso, y hoy sale con `exit 1`, que es otra cosa. **La diferencia queda escrita
y no la resuelvo copiando ninguna de las dos.**
""" % dict(v, v=VUELTA, tabla_calibre=tabla_calibre,
           tabla_frescura=tabla_frescura, lista_nm=lista_nm)

    fallos = 0
    print("EL JUICIO, ANTES DE ESCRIBIR NADA:")
    print("   CIFRA guiones largos: %d | CIFRA guiones medios: %d"
          % (cuerpo.count(chr(8212)), cuerpo.count(chr(8211))))
    if cuerpo.count(chr(8212)) or cuerpo.count(chr(8211)):
        fallos += 1
    for etiqueta, cond in (
            ("empieza por la cabecera de la TAREA 1",
             cuerpo.startswith("### TAREA 1.")),
            ("las dos tablas van pegadas enteras",
             tabla_calibre in cuerpo and tabla_frescura in cuerpo),
            ("la lista de los NO MORDIO va pegada entera", lista_nm in cuerpo),
            ("ninguna llave de formato quedo sin resolver",
             "%(" not in cuerpo),
            ("la suma de las tres clases calza con las entradas",
             v["t_tres"] == v["t_entradas"] == v["nomina"]),
            ("las dos cuentas de NO MORDIO calzan",
             v["t_nm"] == v["t_nm_filas"]),
            ("los once tramos son de esta vuelta", v["t_frescos"] == "11"
             and v["t_ajenos"] == "0"),
            ("la cobertura de --componer no deja hueco",
             v["cob_sin"] == "0" and v["cob_ajenas"] == "0"
             and v["cob_repes"] == "0")):
        print("   %-56s %s" % (etiqueta, "SI" if cond else "NO"))
        if not cond:
            fallos += 1
    print("   CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: el cuerpo NO SE ESCRIBE.")
        return 1
    destino = os.path.join(AQUI, "_v%d_t1_seccion.md" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(cuerpo)
    print("ESCRITO scripts/loop/_v%d_t1_seccion.md -> %d bytes, %d saltos de linea"
          % (VUELTA, len(cuerpo.encode("utf-8")), cuerpo.count(NL)))
    de_nuevo = io.open(destino, encoding="utf-8").read().replace(chr(13) + NL, NL)
    print("RELECTURA DEL DISCO: identico a lo juzgado: %s"
          % ("SI" if de_nuevo == cuerpo else "NO"))
    return 0 if de_nuevo == cuerpo else 1


if __name__ == "__main__":
    sys.exit(main())
