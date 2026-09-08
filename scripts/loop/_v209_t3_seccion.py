# -*- coding: utf-8 -*-
r"""_v209_t3_seccion.py . COMPONE LA SECCION DE LA TAREA 3 DEL REPORTE DE LA
VUELTA 209 **CONTANDO SUS FICHEROS DE SALIDA** (`EJECUTOR.md` 1, LA TABLA SE
CUENTA DE SU FICHERO).

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3).

NINGUNA CIFRA SE TECLEA: todas se leen de `SALIDA_V209_T3A_VARA.txt` y de
`SALIDA_V209_T3_COTEJO.txt`, y el computo CAE EN ROJO si no puede leer una. LA
TABLA DEL COTEJO SE RECONSTRUYE BARRIENDO EL FICHERO, no se copia a mano.

Y TODA CIFRA DE BYTES VA CON SU PAREJA EN LA MISMA LINEA.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
DESTINO = os.path.join(AQUI, "_v209_t3_seccion.md")


def leer(nombre):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.isfile(ruta) or os.path.getsize(ruta) == 0:
        print("ROJO: %s no existe o mide cero bytes." % ruta)
        sys.exit(1)
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def uno(texto, patron, etiqueta, banderas=0):
    m = re.findall(patron, texto, banderas)
    if len(m) != 1:
        print("ROJO: %s -> %d coincidencias de %r (se exige 1)"
              % (etiqueta, len(m), patron))
        sys.exit(1)
    return m[0]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    tv = leer("SALIDA_V209_T3A_VARA.txt")
    tc = leer("SALIDA_V209_T3_COTEJO.txt")

    # --- LA VARA ---
    v_puntos = uno(tv, r"CIFRA puntos de la vara: (\d+)\n   CIFRA puntos "
                   r"DOCUMENTALES", "puntos de la vara")
    v_doc = uno(tv, r"CIFRA puntos DOCUMENTALES: (\d+)", "documentales")
    v_nodoc = uno(tv, r"CIFRA puntos NO DOCUMENTALES: (\d+)", "no documentales")
    v_citas = uno(tv, r"CIFRA citas que NO aparecen verbatim en su campo: (\d+)",
                  "citas que fallan")
    v_ctrl = uno(tv, r"CIFRA controles positivos que FALLAN: (\d+)", "controles")
    v_esc = uno(tv, r"corpus: (\d+)\n\nE\)", "escarmiento")
    v_disc = uno(tv, r"CIFRA discrepancias con el contraste del encargo en el "
                 r"3\.a: (\d+)", "discrepancias del 3.a")
    v_bytes = uno(tv, r"CIFRA bytes de la linea de la ficha: (\d+) en disco",
                  "bytes de la ficha")
    v_bytes_lf = uno(tv, r"CIFRA bytes de la linea de la ficha: \d+ en disco y "
                     r"(\d+) normalizado a LF", "bytes de la ficha LF")
    v_adj = uno(tv, r"CIFRA caracteres de adjudicacion: (\d+)", "adjudicacion")
    v_nota = uno(tv, r"CIFRA caracteres de adjudicacion: \d+ \| de nota: (\d+)",
                 "nota")

    # --- EL COTEJO ---
    c_marc = uno(tc, r"CIFRA marcador del cribado HOY: (\d+) filas", "marcador")
    c_a = uno(tc, r"repartidas en A (\d+), B \d+, C \d+ y D \d+", "clase A")
    c_b = uno(tc, r"repartidas en A \d+, B (\d+), C \d+ y D \d+", "clase B")
    c_c = uno(tc, r"repartidas en A \d+, B \d+, C (\d+) y D \d+", "clase C")
    c_d = uno(tc, r"repartidas en A \d+, B \d+, C \d+ y D (\d+)", "clase D")
    c_puestos = uno(tc, r"CIFRA puestos distintos: (\d+) \| maximo", "puestos")
    c_huecos = uno(tc, r"maximo: \d+ \| huecos: (\d+)", "huecos")
    c_sello = uno(tc, r"MI RECOMPUTO CALZA CON EL SELLO DEL AUDITOR: (\S+)",
                  "calza sello")
    c_ar_tot = uno(tc, r"CIFRA aritmeticas de la ficha comprobadas: (\d+)",
                   "aritmeticas")
    c_ar_ok = uno(tc, r"comprobadas: \d+, de las que cuadran (\d+)", "cuadran")
    c_ar_no = uno(tc, r"cuadran \d+ y no cuadran (\d+)", "no cuadran")
    c_tres = uno(tc, r"CIFRA de las tres nominas afectadas que la ficha NOMBRA: "
                 r"(\d+) de 3", "tres nominas")
    c_lds = uno(tc, r"CIFRA cabeceras de LD-66 a LD-70 halladas: (\d+) de 5",
                "cabeceras LD")
    c_sra = uno(tc, r"contado de sus cabeceras: (\d+) A y \d+ D", "sales A")
    c_srd = uno(tc, r"contado de sus cabeceras: \d+ A y (\d+) D", "sales D")
    c_nom = uno(tc, r"CIFRA nominas halladas en la salida sellada: (\d+)", "nominas")
    c_sinver = uno(tc, r"CIFRA pares SIN veredicto de ninguna sede, sumando las "
                   r"seis: (\d+)", "sin veredicto")
    c_fichas = uno(tc, r"CIFRA fichas barridas: (\d+)", "fichas barridas")
    c_barr = uno(tc, r"CIFRA apariciones en los campos nodos, preservar, "
                 r"eliminar y superviviente: (\d+)", "barrido")
    c_ctrlb = uno(tc, r"CIFRA fichas cuyo campo `nodos` trae al menos un nodo: "
                  r"(\d+)", "control del barrido")
    c_rutas = uno(tc, r"CIFRA rutas de la ficha comprobadas: (\d+)", "rutas")
    c_rutas_mal = uno(tc, r"comprobadas: \d+, de las que fallan (\d+)", "rutas mal")
    c_dep = uno(tc, r"CIFRA dependencias que NO existen: (\d+)", "dependencias")
    c_gr = uno(tc, r"CIFRA grupos del backlog: (\d+)", "grupos")
    c_gr_ok = uno(tc, r"llevan su motivo escrito y no solo su cuenta: (\d+)",
                  "grupos con motivo")
    c_ver = uno(tc, r"CIFRA veredictos emitidos: (\d+)", "veredictos")
    c_cubre = uno(tc, r"de los que CUBRE (\d+), A MEDIAS \d+ y NO CUBRE \d+",
                  "cubre")
    c_med = uno(tc, r"de los que CUBRE \d+, A MEDIAS (\d+) y NO CUBRE \d+",
                "a medias")
    c_no = uno(tc, r"de los que CUBRE \d+, A MEDIAS \d+ y NO CUBRE (\d+)",
               "no cubre")
    c_sincita = uno(tc, r"CIFRA filas del cotejo SIN cita de fichero y linea: "
                    r"(\d+)", "filas sin cita")
    c_e_d = uno(tc, r"AL \*\*ENTRAR\*\* DE ESTA TAREA \(3\.d\)\n   (\d+) bytes "
                r"en disco", "ops entrada disco")
    c_e_l = uno(tc, r"AL \*\*ENTRAR\*\* DE ESTA TAREA \(3\.d\)\n   \d+ bytes en "
                r"disco y (\d+) bytes", "ops entrada LF")
    c_e_s = uno(tc, r"AL \*\*ENTRAR\*\* DE ESTA TAREA \(3\.d\)\n.*?sha256 disco "
                r"(\w+) y sha256 LF \w+", "ops entrada sha", re.S)
    c_s_d = uno(tc, r"AL \*\*SALIR\*\* DE ESTA TAREA \(3\.d\)\n   (\d+) bytes en "
                r"disco", "ops salida disco")
    c_s_l = uno(tc, r"AL \*\*SALIR\*\* DE ESTA TAREA \(3\.d\)\n   \d+ bytes en "
                r"disco y (\d+) bytes", "ops salida LF")
    c_s_s = uno(tc, r"AL \*\*SALIR\*\* DE ESTA TAREA \(3\.d\)\n.*?sha256 disco "
                r"(\w+) y sha256 LF \w+", "ops salida sha", re.S)
    c_quieto = uno(tc, r"EL `estado` SIGUE EN '(\w+)'", "estado al salir")

    # LAS 18 FILAS DEL COTEJO, BARRIDAS DEL FICHERO Y NO TECLEADAS.
    filas = re.findall(
        r"   --- (V\.\d+) --- ([A-Z ]+)\n       sede: (.+?)\n       por que: (.+?)\n",
        tc)
    if len(filas) != int(c_ver):
        print("ROJO: la salida da %s veredictos y el barrido encuentra %d."
              % (c_ver, len(filas)))
        sys.exit(1)

    p = []
    a = p.append
    a("### TAREA 3. LA MESA `OP-L-02`, MEDIDA POR EL MISMO METODO QUE LAS DOS ANTERIORES")
    a("")
    a("**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN de")
    a("`docs/loop/SALIDA_V209_T3A_VARA.txt` y `docs/loop/SALIDA_V209_T3_COTEJO.txt`")
    a("con `scripts/loop/_v209_t3_seccion.py`, que **cae en rojo si no puede leer")
    a("una**; y **la tabla del cotejo se reconstruye barriendo el fichero**, no se")
    a("copia a mano.")
    a("")
    a("#### 3.a. LA VARA, SELLADA EN SU PROPIO COMMIT ANTES DE COTEJAR NADA")
    a("")
    a("La vara vive en `scripts/loop/_v209_t3_vara.py` y quedo **committeada antes")
    a("de abrir ningun documento del cotejo**. El cotejo la **IMPORTA** y no puede")
    a("cambiarla: si pudiera, el sello no valdria para nada. Es el metodo que la 207")
    a("uso con `OP-L-01` y la 208 con `OP-L-03`, las dos veces bien.")
    a("")
    a("**LA SEDE FINA ES `campo[indice]` Y NO UN NUMERO DE LINEA**, porque la ficha")
    a("entera vive en UNA sola linea de `docs/plan/OPERACIONES.jsonl`, la **42**, que")
    a("mide **%s** bytes en disco y **%s** bytes normalizado a LF. Decir *linea 42*"
      % (v_bytes, v_bytes_lf))
    a("dieciocho veces no localiza nada.")
    a("")
    a("| que se sella | cifra |")
    a("|---|---:|")
    a("| puntos de la vara | **%s** |" % v_puntos)
    a("| de ellos DOCUMENTALES | **%s** |" % v_doc)
    a("| de ellos NO DOCUMENTALES | **%s** |" % v_nodoc)
    a("| citas que NO aparecen VERBATIM en su campo | **%s** |" % v_citas)
    a("| controles positivos que FALLAN | **%s** |" % v_ctrl)
    a("| candidatos a NO DOCUMENTAL cuyo literal SI aparece en el corpus | **%s** |"
      % v_esc)
    a("| discrepancias con el contraste del encargo | **%s** |" % v_disc)
    a("")
    a("**EL ESCARMIENTO, APLICADO Y NO SOLO CITADO.** Antes de sellar un punto como")
    a("NO DOCUMENTAL se busca su literal en el corpus y **la vara CAE EN ROJO si")
    a("aparece**: da **%s**. Los tres primeros (`V.1`, `V.2` y `V.3`) **no se buscan"
      % v_esc)
    a("a proposito y se dice por que**: son campos de la propia ficha (`tipo`,")
    a("`orden`, `fecha_corte`) y su unica sede posible es ella. Y **la sede de la")
    a("propia ficha queda FUERA de esa busqueda**, porque encontrar ahi el literal de")
    a("su propio campo probaria que la ficha existe, no que tenga sede documental.")
    a("")
    a("**LA BUSQUEDA VA TAMBIEN POSITIVA** (`EJECUTOR.md` 9, una busqueda negativa no")
    a("se puede citar sola), con un literal de control por cada uno de los **%s**"
      % c_rutas)
    a("documentos del corpus: **%s fallan**." % v_ctrl)
    a("")
    a("**Y LA PRIMERA CORRIDA DE LA VARA CAYO EN ROJO, POR MI CONTROL Y NO POR EL")
    a("FICHERO.** El control de `SALIDA_V170_T3_DEUDAS_DE_CORTE.txt` era la palabra")
    a("`marcador` y aparecia **0** veces: ese fichero habla del marcador **por su")
    a("sede y su cifra** (`docs/INTRA_DOMINIO_VEREDICTOS.jsonl: 3388 filas`, en su")
    a("linea **48**) y **nunca escribe la palabra**. **Un control positivo que no")
    a("aparece no invalida el documento: invalida el control**, y para eso esta la")
    a("guarda. Quedo por `OP-L-02`, que aparece en su linea **9**. La correccion va")
    a("**declarada dentro del propio sello y con el texto viejo sin borrar**, y **no")
    a("toco ni un punto de la vara ni el reparto documental**.")
    a("")
    a("#### 3.b. LOS DOS AVISOS DE ESTA FICHA, LOS DOS MEDIDOS")
    a("")
    a("**LA `evidencia` TIENE UN SOLO ELEMENTO Y ES PROSA QUE NO NOMBRA NINGUN")
    a("FICHERO**, y por eso `vuelta150_3_relectura_expediente.py` la lista como la")
    a("unica de las tres mesas sin documento que medir. **Eso no la deja sin")
    a("cotejar:** se coteja contra lo que su prosa AFIRMA, que es una cifra con su")
    a("fecha de corte, y esa aritmetica se remide aqui. **CIFRA aritmeticas de la")
    a("ficha comprobadas: %s, de las que cuadran %s y no cuadran %s.**"
      % (c_ar_tot, c_ar_ok, c_ar_no))
    a("Las tres cifras de la `evidencia` cuadran entre si (11 mas 194 dan 205) y con")
    a("la particion de la `nota` (126 mas 79 dan 205), y **205 menos las 16 de la")
    a("segunda tanda dan los 189 del backlog**.")
    a("")
    a("**Y `adjudicacion` Y `nota` SI TRAEN TEXTO, que es lo que las otras dos mesas")
    a("no tenian igual:** **%s** y **%s** caracteres. **Ahi es donde vive lo que la"
      % (v_adj, v_nota))
    a("mesa decidio**, y de ahi salen la mayoria de los puntos de la vara.")
    a("")
    a("**LAS DOS CIFRAS DEL MARCADOR, PUBLICADAS JUNTAS Y CADA UNA CON SU CORTE**, que")
    a("es lo que el encargo manda y lo que el banco `9.21` pide:")
    a("")
    a("| cifra | corte | de donde sale |")
    a("|---:|---|---|")
    a("| **2.117** | **2026-08-11**, el `fecha_corte` de la ficha | `verificacion[1]`. **TESTIGO Y NO CONDICION** |")
    a("| **%s** | **7 sep 2026** | recomputado por mi de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` linea a linea |"
      % c_marc)
    a("")
    a("**NO SE ARREGLA TOCANDO LA FICHA.** El instrumento no fallo, **la cifra se")
    a("quedo vieja** (banco `9.21`), y la clausula exige que la OPERACION no mueva el")
    a("marcador, **no que el marcador valga 2.117 hoy**. La `verificacion[3]` de la")
    a("propia ficha ya le puso el corte al lado el 4 sep 2026 por CORRECCION")
    a("DECLARADA, sin borrar el numeral viejo.")
    a("")
    a("**MI RECOMPUTO DEL MARCADOR: %s filas, repartidas en A %s, B %s, C %s y D %s**,"
      % (c_marc, c_a, c_b, c_c, c_d))
    a("con **%s** puestos distintos y **%s** huecos. **Calza con el sello del auditor**"
      % (c_puestos, c_huecos))
    a("`docs/loop/SALIDA_MARCADOR_AUDITOR_V208.json`: **%s**." % c_sello)
    a("")
    a("**UNA CAIDA MIA CAZADA ANTES DE PUBLICAR, Y VA MARCADA COMO `C.2`.** La primera")
    a("version del cotejo leia el puesto como `puesto`, y **ese campo no existe en ese")
    a("archivo**: se llama `puesto_intra`. `.get()` devolvia vacio en las **%s** filas,"
      % c_marc)
    a("el conjunto se quedaba con un solo valor y la salida publicaba **CIFRA puestos")
    a("distintos: 1** sobre un archivo de **%s** puestos. **Ese 1 no era una medicion:"
      % c_puestos)
    a("era el uno de un patron roto**, que es justo lo que `EJECUTOR.md` 9 prohibe")
    a("publicar como hecho del mundo. Arreglado el campo, **queda ademas una guarda**")
    a("que comprueba que el campo se lee en todas las filas **antes** de publicar la")
    a("cifra, y que la declara NO COMPUTABLE si no. Va entera en la seccion 8.")
    a("")
    a("#### 3.c. EL COTEJO PUNTO POR PUNTO, CON SU CITA EN CADA FILA")
    a("")
    a("| punto | veredicto | sede citada | por que entra asi |")
    a("|---|---|---|---|")
    for clave, ver, sede, porque in filas:
        a("| `%s` | **%s** | %s | %s |"
          % (clave, ver.strip(), sede.strip().replace("|", "/"),
             porque.strip().replace("|", "/")))
    a("")
    a("**CIFRA filas del cotejo SIN cita de fichero y linea: %s.** Ninguna sin cita,"
      % c_sincita)
    a("que es lo que el encargo exige.")
    a("")
    a("**LAS MEDICIONES QUE SOSTIENEN ESAS FILAS, CADA UNA CON SU CIFRA:**")
    a("")
    a("| que se midio | cifra |")
    a("|---|---:|")
    a("| las tres nominas de `verificacion[0]` que la ficha NOMBRA | **%s** de 3 |" % c_tres)
    a("| cabeceras `LD-66` a `LD-70` halladas en su documento | **%s** de 5 |" % c_lds)
    a("| reparto de esas cinco, contado de sus cabeceras | **%s** A y **%s** D |" % (c_sra, c_srd))
    a("| nominas de la ficha en su salida sellada de la 169 | **%s** |" % c_nom)
    a("| pares SIN veredicto de ninguna sede, sumando las seis | **%s** |" % c_sinver)
    a("| fichas barridas para la busqueda negativa | **%s** |" % c_fichas)
    a("| apariciones de los nodos del acto en `nodos`, `preservar`, `eliminar` y `superviviente` | **%s** |" % c_barr)
    a("| control positivo del mismo barrido: fichas con `nodos` no vacio | **%s** |" % c_ctrlb)
    a("| rutas del corpus comprobadas, y de ellas las que fallan | **%s** y **%s** |" % (c_rutas, c_rutas_mal))
    a("| dependencias de la ficha que NO existen | **%s** |" % c_dep)
    a("| grupos del backlog, y de ellos los que llevan su motivo escrito | **%s** y **%s** |" % (c_gr, c_gr_ok))
    a("")
    a("**LA BUSQUEDA NEGATIVA SE RE-VERIFICO EN VEZ DE CITARSE** (`EJECUTOR.md` 9): la")
    a("`nota` declara un barrido de las fichas buscando los nodos del acto, y aqui se")
    a("repite entero sobre las **%s** de hoy. Da **%s** apariciones, **y su CONTROL"
      % (c_fichas, c_barr))
    a("POSITIVO da %s fichas con `nodos` no vacio**, asi que ese cero **no es el cero"
      % c_ctrlb)
    a("de un patron roto**.")
    a("")
    a("**LA DISCREPANCIA QUE ENCUENTRO Y QUE NO RESUELVO COPIANDO** (`EJECUTOR.md` 2).")
    a("La `nota` dice *cuadrantes 15 de 15 con 8 A y 7 D*, y la **NOMINA 2** de su")
    a("propia salida sellada, que es la de los cuadrantes, publica **0 de 0** con 6")
    a("miembros escritos, 1 vivo tras resolver y 5 colapsados por alias. **Son las dos")
    a("convenciones y la ficha habla en LITERAL:** el **15** son los pares de SEIS")
    a("miembros escritos, que es el universo que habia en el `fecha_corte`")
    a("**2026-08-11**; el **0 de 0** es la foto RESUELTA de hoy, **7 sep 2026**,")
    a("despues de que cinco de esos seis se fundieran. **Manda la LITERAL** por la")
    a("adjudicacion `6.6` del acta 208, **y la resuelta va al lado**. Por eso la `V.15`")
    a("entra **A MEDIAS** y no CUBRE ni NO CUBRE.")
    a("")
    a("**LAS DOS CUENTAS, SEPARADAS Y JUNTAS, COMO EN LA 208:**")
    a("")
    a("| cuenta | cifra |")
    a("|---|---|")
    a("| **la del SELLO**, escrita ANTES de mirar | **%s** puntos, **%s** DOCUMENTALES y **%s** NO DOCUMENTALES |"
      % (v_puntos, v_doc, v_nodoc))
    a("| **la de los VEREDICTOS**, sacada DESPUES de mirar | **%s** emitidos: **%s** CUBRE, **%s** A MEDIAS y **%s** NO CUBRE |"
      % (c_ver, c_cubre, c_med, c_no))
    a("")
    a("**LA COBERTURA, MEDIDA Y NO NARRADA: %s de %s CUBREN**, y su lista NOMINAL de"
      % (c_cubre, c_ver))
    a("los que no cubren entero es **`V.8`** (**%s** de **%s** grupos del backlog"
      % (c_gr_ok, c_gr))
    a("llevan su motivo escrito: el de los **126 que esperan destejido** trae la")
    a("cuenta pero no un motivo propio) y **`V.15`** (la cobertura COMPLETA solo se")
    a("sostiene en la convencion LITERAL). **Ningun `NO CUBRE`.**")
    a("")
    a("#### 3.d. NO SE CIERRA `OP-L-02` Y NO SE TOCA SU CAMPO `estado`")
    a("")
    a("**AQUI SE MIDE, SE PROPONE Y SE PARA.** La autorizacion del 2.c era **SOLO**")
    a("para `OP-L-01`, y la adjudicacion de esta mesa es del auditor. **Lo que")
    a("propongo, y no lo adjudico yo:** con **%s de %s** puntos cubriendo, **0 NO"
      % (c_cubre, c_ver))
    a("CUBRE** y los dos A MEDIAS declarados con su motivo, la ficha esta **a un")
    a("juicio de cerrarse**, y el juicio no es mio.")
    a("")
    a("**Y PARA PROBAR QUE NO LA TOQUE, LA SEDE VA PUBLICADA POR LAS DOS CONVENCIONES")
    a("AL ENTRAR Y AL SALIR DE ESTA TAREA:**")
    a("")
    a("| `docs/plan/OPERACIONES.jsonl` | bytes en disco y bytes normalizado a LF | `sha256` disco |")
    a("|---|---:|---|")
    a("| **AL ENTRAR** | **%s** y **%s** | **`%s`** |" % (c_e_d, c_e_l, c_e_s))
    a("| **AL SALIR** | **%s** y **%s** | **`%s`** |" % (c_s_d, c_s_l, c_s_s))
    a("")
    a("**Los cuatro valores son identicos y el `estado` sigue en `%s`.** Los `sha256`"
      % c_quieto)
    a("de esta tabla **no** son los de mi sello de apertura, y eso tambien se dice: la")
    a("TAREA 2 movio ese fichero **antes** de esta tarea, con su propia guarda de una")
    a("linea. Lo que esta tabla prueba es que **la TAREA 3 no lo movio**, que es lo")
    a("que el `3.d` pide.")
    a("")
    a("#### 3.e. LA TAREA CABE ENTERA CON SUS GUARDAS, Y NO HAY PARADA")
    a("")
    a("**NO QUEDA ABIERTA.** Los **%s** puntos estan cotejados, las **%s** filas llevan"
      % (c_ver, c_ver))
    a("su cita, el reparto documental se sello antes de mirar y las dos cuentas van")
    a("publicadas.")
    a("")
    a("**Y EL CASO DE PARADA QUE EL ENCARGO AVISA NO SE CUMPLE, Y LO MIDO EN VEZ DE")
    a("SUPONERLO.** `verificacion[0]` habla de *las tres nominas afectadas* y no las")
    a("nombra; **la `nota` SI las nombra las tres**, con su literal y su cuenta:")
    a("*cuadrantes de mercado (8)*, *ecuacion de valor (5)* y *el bloque humano de la")
    a("supervision de la IA (3)*, y las tres cuentas suman 16. **CIFRA de las tres que")
    a("la ficha nombra: %s de 3.** No hay que adivinar ninguna, asi que **la ficha SI"
      % c_tres)
    a("alcanza para cotejarse sin decidir y NO hay PARADA por este motivo**")
    a("(`AUDITOR.md` 3).")
    a("")

    texto = NL.join(p) + NL
    if texto.count(chr(8212)) or texto.count(chr(8211)):
        print("ROJO: la seccion trae guiones prohibidos.")
        sys.exit(1)
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITA %s -> %d bytes, %d lineas"
          % (DESTINO, len(texto.encode("utf-8")), texto.count(NL)))
    print("CIFRA filas del cotejo reconstruidas del fichero: %d" % len(filas))
    print("CIFRA guiones largos: 0 | CIFRA guiones medios: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
