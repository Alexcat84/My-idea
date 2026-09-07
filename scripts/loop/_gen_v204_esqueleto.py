# -*- coding: utf-8 -*-
r"""_gen_v204_esqueleto.py . GENERA scripts/loop/vuelta204_esqueleto_reporte.py
COMO CLON DECLARADO DE LA 203, COPIANDO TODO LO DEMAS BYTE A BYTE.

Fichero de computo con PREFIJO DE GUION BAJO: fuera del censo y fuera de la
nomina, que es lo que el `4.5` del acta 199 y el `4.6` del acta 203 llaman
COMPUTO DE UNA VUELTA. Cambia EXACTAMENTE cuatro cosas y las imprime una a una:
el docstring, la constante `VUELTA`, la lista `TAREAS` y el bloque de prosa del
encabezado del reporte. TODO LO DEMAS, incluidas las cinco funciones puras y las
guardas del PASO 0, se copia sin tocar, y al final se COTEJA cuantas lineas
vinieron sin tocar y cuantas son nuevas, contadas con `difflib` y no a ojo.
"""
import difflib
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FUENTE = os.path.join(RAIZ, "scripts", "loop", "vuelta203_esqueleto_reporte.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop", "vuelta204_esqueleto_reporte.py")

DOCSTRING = 'r' + chr(34) * 3 + '''vuelta204_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 204,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta203_esqueleto_reporte.py, generado de el
programaticamente con `scripts/loop/_gen_v204_esqueleto.py`. Cambia el numero de
vuelta, la lista TAREAS, este docstring y el bloque de prosa del encabezado. EL
CODIGO DE LAS FUNCIONES VA IGUAL, byte a byte, porque se copio y no se re
escribio.

POR QUE CUATRO TAREAS, Y LA CIFRA NO SE TECLEA: la racha de cierres, contada del
instrumento en el bloque `E` del sello de apertura de ESTA vuelta, vale 5, con
las vueltas 199, 200, 201, 202 y 203. `AUDITOR.md` 6.2 apaga el regimen temporal
de dos sub-tareas cuando DOS VUELTAS SEGUIDAS cierran su propio reporte con
`cerrar_reporte.py`, y con racha 5 SE APAGA y vuelve el tope de CINCO. El encargo
trae CUATRO mas la TAREA 0, que es un remedio de gobierno y no trabajo de plan.
LA CIFRA SE LEE DEL SELLO, con `racha_del_sello()`, y si el sello no la trae este
esqueleto CAE EN ROJO y no escribe nada.

Y ESTA NO ES VUELTA DE BATERIA: la 200 lo fue y cerro entera, y por la cadencia
de `AUDITOR.md` 6.1 le toca a la 205. La seccion 9 cierra con el HUECO DECLARADO
Y MEDIDO por el carril de `cerrar_reporte.py`. El trabajo de esta vuelta es EL
PLAN, que es lo que la moratoria 6.3 manda.

EL DESFASE DE `PATRONES_ACTA` NO APARECE EN ESTA VUELTA, Y ESO SE MIDE EN VEZ DE
SUPONERSE: `PATRONES_ACTA` pide el acta de `VUELTA - 1`, o sea la 203, y el acta
que ORDENA esta vuelta ES la 203. El literal `DESFASE DECLARADO` se sigue
CONTANDO de los reportes archivados, con su fecha de corte, porque esa cifra es
de inventario y envejece sola.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

USO:
  python scripts/loop/vuelta204_esqueleto_reporte.py
''' + chr(34) * 3

T1 = ('LOS REGISTROS. `R.67` PARA EL ACTA 177 Y `R.68` PARA EL ACTA 178, las dos '
      'siguientes de la deuda por el `4.9` del acta 201, y va PRIMERA porque '
      '`AUDITOR.md` 1.4 pone los registros en la TAREA 1. **LA DEUDA SE REMIDE '
      'AQUI Y NO SE COPIA DEL ENCARGO**: se cuenta cuantas actas de la 177 a la '
      '180 siguen sin registro. **DE QUE CONVENCION SON SE COMPRUEBA, NO SE '
      'SUPONE**: la 184 es la frontera, y si un acta ya escribe sus claves con '
      'comillas inversas **el lector heredado basta y se dice**. **EL COMPUTO DE '
      'LA 203 SE REUTILIZA**, `scripts/loop/_v203_reparto_de_actas_viejas.py`, '
      'clonado a un `_v204_*` **con su cifra de `difflib` al lado**, y no se '
      'escribe un tercero. **CADA ACTA SE ACOTA EN ESTA VUELTA** por linea de '
      'inicio y de fin, con **el reparto entero y cada numeral con la seccion de '
      'la que sale nombrada por su TITULO**. **UN NUMERAL NO COMPUTABLE SE '
      'DECLARA EN VEZ DE PUBLICAR UN CERO**, con **las tres lecturas** cuando '
      'discrepen, porque un cero de convencion no es un cero de ausencia. **SE '
      'COTEJA CONTRA LA FILA DE METRICA DE CADA ACTA**, que la escribio el '
      'auditor de aquella vuelta y no el ejecutor. **CIERRA CON LA SERIE MEDIDA** '
      'por `scripts/loop/serie_de_registros.py` y **no con una expresion regular '
      'propia**. **GUARDA OBLIGATORIA Y CORRIDA DOS VECES**, con **crecimiento '
      '0** la segunda')

T2 = ('EL TAMANO DEL AGUJERO DE `cobertura`, MEDIDO Y NO TAPADO. Adjudicado en '
      'el `4.3` del acta 203: **`OP-I-01` no se cierra** porque sus clausulas '
      '**2** y **3** no se caerian si el fallo volviera, ya que `cobertura` es '
      'texto libre. **ESTA TAREA NO CIERRA LA FICHA Y NO ESCRIBE LA VARA**: la '
      'vara es codigo permanente y va a la auditoria integral por el `4.7`. Lo '
      'que se pide es **medir de que tamano es el agujero**, para que quien '
      'escriba la vara despues sepa contra que. **CUANTAS FORMAS DISTINTAS toma '
      'hoy el campo `cobertura`** en las entradas de `docs/plan/INVENTARIO.jsonl` '
      '(**la cifra de entradas se RECUENTA**), **agrupadas por su forma**, y '
      '**cuantas quedarian fuera de cualquier vara razonable**. **LA BUSQUEDA ES '
      'POSITIVA Y NUNCA NEGATIVA** (`EJECUTOR.md` 9) y **SE DECLARA SOBRE QUE '
      'CAMPO CORRE CADA UNA**, que es la `C.2` del acta 203: la misma variante '
      'da cifras distintas sobre el campo y sobre el fichero entero, y **una '
      'vara sin declarar convierte una medicion buena en una acusacion**. **SE '
      'MIDE LO MISMO PARA LA CLAUSULA 3**, la de los huecos nombrados, que '
      'comparte el agujero. **PROPONE, NO CIERRA**, y **no toca el `estado`**')

T3 = ('LA DISCREPANCIA DE COMPONENTES QUE EL PROPIO INSTRUMENTO DECLARA. La 203 '
      'la reprodujo y no la persiguio, y lo dijo. **SE MIDE DE DONDE SALE LA '
      'DIFERENCIA**, con el resolutor delante, y **se declara**: cuantas '
      'componentes del sellado no estan hoy, cuantas hay hoy que no estaban, y '
      '**si la causa es el universo, la fecha o el instrumento**. **LA NOMINA '
      'SELLADA NO SE REGENERA**: `docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` '
      '**se CUENTA, no se reescribe**. **EL INSTRUMENTO ESCRIBE SOBRE UNA SEDE '
      'SELLADA EN LA 169**, asi que va con **protocolo del sello**: se mide '
      'antes, se corre, se restaura con `git checkout --` y se REMIDE. **SUS DOS '
      'TAMANOS DISCREPAN POR EL CRLF** y eso es el `PD.2`: **se publica, no se '
      'resuelve**. **SI DE AQUI SALE QUE UNA CIFRA PUBLICADA ENVEJECIO**, va por '
      'el carril del banco `9.10`, **POR ADICION Y EN SU SEDE**, con el texto '
      'viejo entero y sin tachar. **SI SALE QUE HACE FALTA CODIGO, SE PARA Y SE '
      'TRAE**')

T4 = ('EL CENSO DE LO QUE QUEDA DEL PLAN, MEDIDO Y NO NARRADO. Las cuatro fichas '
      'reales estan medidas y **ninguna se cerro**, y la moratoria `6.3` dice que '
      'el trabajo es el plan hasta agotarlo: **ese tramo esta agotado y la '
      'pregunta que nadie ha contestado con una cifra es QUE QUEDA**. **SE '
      'CUENTAN LAS FICHAS DE `docs/plan/OPERACIONES.jsonl` POR `estado`** (la '
      'cifra se RECUENTA) **y se cruza esa cuenta con la vara del trabajo '
      'pendiente**, `scripts/loop/vuelta150_3_relectura_expediente.py --corte '
      '<HEAD de apertura>`, **que nunca es el campo `estado`** (`AUDITOR.md` 0) y '
      '**a la que se le pasa un COMMIT y no una fecha**. **LAS DOS LECTURAS SE '
      'PUBLICAN JUNTAS Y LA DISCREPANCIA SE DECLARA**: ese cruce es el punto, no '
      'la suma. **SE NOMBRAN UNA A UNA LAS CONGELADAS EN SILENCIO Y LA `HECHA` '
      'SIN NINGUNA PRUEBA**, que son las que nadie ha mirado nunca y el candidato '
      'natural al trabajo de la 205. **NINGUNA FICHA SE CIERRA Y NINGUN `estado` '
      'SE MUEVE**: lo que esta tarea produce es **el mapa de lo que queda**, para '
      'que el fundador decida el orden')

TAREAS_TXT = ("TAREAS = [" + NL
              + "".join("    (%r, %r)," % (n, t) + NL
                        for n, t in (('1', T1), ('2', T2), ('3', T3), ('4', T4)))
              + "]")

PROSA = '''> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta%(v)d_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **LA TAREA 0 DEL ENCARGO ES BLOQUEANTE Y NO TIENE FILA EN LA TABLA, PORQUE NO ES
> TRABAJO SINO UNA PROHIBICION**: `docs/loop/PROMPT_SIGUIENTE.md`,
> `docs/loop/ACTA_AUDITOR.md` y `docs/loop/PARA_ALEXIS.md` **son sede del auditor**,
> y el ejecutor **no las escribe, no las reescribe, no las borra y no las
> reordena**. La 203 se escribio a si misma su encargo siguiente y con eso **borro
> la prueba de que se le mando**. **Aqui se obedece midiendo**: el bloque `C.1` del
> sello de apertura midio las tres **contra el HEAD de apertura**, y la seccion 4
> las vuelve a medir **al cierre**. **Lo que esta sesion propone para la vuelta
> siguiente vive en su propia seccion del reporte, que es su sede.** **Proponer es
> del ejecutor. Encargar es del auditor.**
>
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA.** La
> 200 lo fue y cerro entera; `AUDITOR.md` 6.1 dice que la bateria corre **cada
> cinco vueltas**, en vuelta propia, y por esa cadencia **le toca a la 205**. Aqui
> la **seccion 9 cierra igual**, con el **HUECO DECLARADO Y MEDIDO** por el carril
> de `cerrar_reporte.py`, que lleva **su nombre, sus bytes medidos y su atribucion,
> las tres juntas, o no vale**, y **distinguiendo si el cero sale de que no hay
> fichero o de medir uno vacio**. El bloque `I` del sello de apertura ya lo midio:
> **0 ficheros `SALIDA_V%(v)d_BATERIA_TRAMO_N.txt`** y
> **`docs/loop/SALIDA_V%(v)d_BATERIA.txt` NO EXISTE**, o sea que **el cero es de
> ausencia de fichero y no de fichero vacio**.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3, decision del fundador
> del 7 sep 2026), **con su linea exacta ya adjudicada dos veces, asi que aqui no
> se vuelve a discutir**: el `4.5` del acta 199 y el `4.6` del acta 203 dicen que
> la moratoria prohibe **arneses, guardas y lectores QUE SE QUEDEN VIGILANDO**, y
> que **un computo de una vuelta que muere con ella no es eso, aunque traiga una
> lectura que no existia**. Por eso todo lo que esta vuelta escribe son ficheros
> `_v204_*` **con prefijo de guion bajo, fuera del censo y fuera de la nomina**, y
> los lectores que hacen falta **se IMPORTAN o se clonan con su cifra de `difflib`
> al lado**. **La nomina queda CONGELADA EN 135**, y el bloque `F` del sello de
> apertura la midio contra ese congelado sin tocarla. **EL TRABAJO ES EL PLAN**,
> que es para lo que el bucle existe.
>
> **EL TOPE DE SUB-TAREAS ES CINCO, Y LA CIFRA QUE LO MANDA NO SE TECLEA.**
> El bloque `E` del sello de apertura de esta vuelta corrio el instrumento de la
> racha sobre el inventario ENTERO y **la racha de cierres vale %(racha)s**, con las
> vueltas **%(cuales)s**. `AUDITOR.md` 6.2 apaga el regimen temporal de dos
> sub-tareas cuando **DOS vueltas seguidas** cierran su propio reporte con
> `cerrar_reporte.py`, y con **%(racha)s** **SE APAGA**. **Este encargo trae CUATRO
> mas la TAREA 0, y cabe.** **Y ese mismo bloque corrio el instrumento de la racha
> COMPROBANDO ANTES SI ESCRIBE**, que es lo que el encargo pide expresamente: **SI
> ESCRIBE**, pisa su propia salida sellada, asi que se midio antes, se corrio, y la
> sellada se **RESTAURO con `git checkout --` y se REMIDIO IDENTICA**.
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. **El desfase de calibrado se midio
> DENTRO del bloque de apertura y ANTES de la primera operacion.** Y su bloque `F`
> publica la cifra de arneses del censo fuera de la nomina **con su vara al lado y
> las dos medidas**: con vara **%(vara)s** salen **%(conv)s** y sin vara salen
> **%(sinv)s**. **Esas son las cifras de HOY.**
>
> **LO QUE EL ACTA 203 ADJUDICO NO SE VUELVE A LEVANTAR AQUI.** Su `4.3` deja
> **`OP-I-01` SIN CERRAR**, porque sus clausulas **2** y **3** no se caerian si el
> fallo volviera (`cobertura` es texto libre) y la **4** se cae solo en la parte
> que recomputa: **aqui no se levanta y no se le toca el `estado`**. Su `4.4` deja
> contestado que el parametro opcional de `vuelta184_tarea1a_registrar_acta184.py`
> **no roza la moratoria**. Su `4.6` fija que **un computo `_v204_*` puede traer una
> lectura nueva**. Su `4.8` dice que **un reporte archivado que existe pero no
> titula seccion de preguntas se trata como el que no existe, DECLARANDOLO**. Y la
> **vara de las actas anteriores a la 184** sigue siendo la del `4.1` del acta 202:
> **el numeral se toma de la seccion cuyo PROPIO TITULO lo nombra, nunca del numero
> de seccion**, y las claves se cuentan por su numeracion `N.M`, **lleve o no
> comillas inversas**, y **la entrada declara que uso esa vara**. **`OP-L-01` y
> `OP-L-02` tampoco se cierran** (actas 202 `4.3` y `4.4`) y **sus correcciones ya
> estan escritas: no se repiten.**
>
> **LA CIFRA QUE EL ACTA 202 MIDIO EN SU `5.2` Y AQUI SE OBEDECE:** el inventario de
> salidas **se mide a si mismo y envejece dentro de la propia vuelta**. Esa media
> linea va escrita en el bloque `J` del sello de apertura: **junto al corte se
> declaran los ficheros que nacen despues de medirlo**, con sus nombres, y **el
> cierre remide la cifra en vez de heredarla** (banco `9.21`).
>
> **LAS DOS CIFRAS QUE LA 203 APRENDIO EN ROJO Y AQUI SE OBEDECEN DE ENTRADA:**
> **(a)** una pareja de bytes completa **puede ser FALSA** si se le pega a una ruta
> el tamano que tenia **en mitad de la vuelta**, asi que **detras de cada ruta va SU
> tamano al cierre** y el intermedio se dice **sin nombrar la ruta**; **(b)** el
> markdown **parte la frase donde le cabe el ancho**, asi que **cada cifra va junto
> a su pareja en el MISMO renglon**.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni **podar la nomina**, ni **mover
> un solo campo `estado`** (la vara del trabajo pendiente es
> `scripts/loop/vuelta150_3_relectura_expediente.py`, nunca el campo, por el
> recuadro de `AUDITOR.md` 0), ni **mover una clase ni un veredicto**, ni **cerrar
> ninguna ficha por cuenta del ejecutor**: lo que estas tareas producen es **lectura
> medida**, y si de ella sale que una ficha esta cumplida, **se propone con su
> evidencia y lo adjudica el auditor**. **Y siguen fuera, nombradas para que la 205
> no las redescubra:** la **operacion de codigo de la escalada** (acta 202, `4.6`,
> ratificada en el `4.9` del acta 203), **encargada y con su ejecucion SUSPENDIDA**
> hasta la primera vuelta despues de que la moratoria se levante; la **vara escrita
> para `cobertura`** (acta 203, `4.7`); la **reparacion del HEAD envejecido** de
> `vuelta170_tarea5b_veredicto_op_l_02.py`; el **cierre del turno del auditor que se
> reabre despues de declarar las clases**; que **`aislador_de_ciega.py` pueda servir
> un par cuyo nodo ya murio** (acta 203, `5.3`); los **dos arneses que el censo ve y
> la nomina congelada no tiene**; **anadir `docs/PENDIENTES.md` como quinta sede de
> cifra publicada**; y **QUE HACER CON LAS FILAS `B` DEL ARCHIVO**. **Las de codigo
> van a la auditoria integral: la moratoria las prohibe hoy.**
>
> **NO SE MUEVE NINGUNA CLASE Y NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor,
> y **las dos convenciones se publican**. **Y no se toca `dataset/` a mano**: el
> `numstat` de `dataset/`, `web/`, `engine/` y `docs/plan/` se mide al entrar y al
> salir y **las dos cifras se publican**.'''

src = io.open(FUENTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
L = src.split(NL)
n_antes = len(L)

# 1. EL DOCSTRING: la linea 1 es el coding, el docstring va de la 2 hasta su
#    cierre, localizado CONTANDO y no tecleado.
assert L[0].startswith("# -*- coding"), L[0][:60]
assert L[1].startswith('r' + chr(34) * 3 + 'vuelta203_esqueleto_reporte.py'), L[1][:60]
cierres = [i for i in range(2, len(L)) if L[i] == chr(34) * 3]
assert cierres, "no se encuentra el cierre del docstring"
fin_doc = cierres[0]
doc_viejo = NL.join(L[1:fin_doc + 1])
texto = L[0] + NL + DOCSTRING + NL + NL.join(L[fin_doc + 1:])
print("1) DOCSTRING: %d lineas viejas -> %d lineas nuevas"
      % (doc_viejo.count(NL) + 1, DOCSTRING.count(NL) + 1))

# 2. LA CONSTANTE.
assert texto.count("VUELTA = 203") == 1, texto.count("VUELTA = 203")
texto = texto.replace("VUELTA = 203", "VUELTA = 204")
print("2) CONSTANTE: VUELTA = 203 -> VUELTA = 204, 1 sola aparicion")

# 3. LA LISTA TAREAS: del marcador de apertura al primer ']' en columna 0.
i = texto.index("TAREAS = [")
j = texto.index(NL + "]" + NL, i) + len(NL + "]")
tareas_viejo = texto[i:j]
texto = texto[:i] + TAREAS_TXT + texto[j:]
print("3) TAREAS: %d bytes viejos -> %d bytes nuevos, %d entradas"
      % (len(tareas_viejo), len(TAREAS_TXT), 4))

# 4. EL BLOQUE DE PROSA: del primer '> **ESTE REPORTE SE ABRIO' hasta la linea
#    que cierra la prosa, justo antes del veredicto sin escribir.
ini = texto.index("> **ESTE REPORTE SE ABRIO")
fin = texto.index(NL + NL + "**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**")
prosa_vieja = texto[ini:fin]
texto = texto[:ini] + PROSA + texto[fin:]
print("4) PROSA: %d bytes viejos -> %d bytes nuevos"
      % (len(prosa_vieja), len(PROSA)))

# LA CIFRA QUE CONVIERTE "CLON DECLARADO" EN UNA MEDICION Y NO EN UNA PALABRA:
# cuantas lineas vienen SIN TOCAR de la fuente y cuantas son nuevas, contadas
# con difflib.
nuevas = texto.split(NL)
sm = difflib.SequenceMatcher(None, L, nuevas, autojunk=False)
iguales = sum(b.size for b in sm.get_matching_blocks())
print("")
print("EL CLON, MEDIDO Y NO AFIRMADO (difflib.SequenceMatcher):")
print("   CIFRA lineas de la fuente %s: %d"
      % (os.path.basename(FUENTE), n_antes))
print("   CIFRA lineas del destino %s: %d"
      % (os.path.basename(DESTINO), len(nuevas)))
print("   CIFRA lineas que vienen SIN TOCAR de la fuente: %d" % iguales)
print("   CIFRA lineas nuevas o cambiadas en el destino: %d" % (len(nuevas) - iguales))

io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
print("")
print("ESCRITO: scripts/loop/vuelta204_esqueleto_reporte.py (%d bytes)"
      % len(texto.encode("utf-8")))
