# -*- coding: utf-8 -*-
"""VUELTA 152, TAREA 6.a: EL REGISTRO DE CITAS DE `OP-C-05`.

LA DECISION DEL FUNDADOR QUE LO MANDA (2 sep 2026, PREGUNTA 1, opcion c con
atajo de registro, en
docs/loop/paradas/2026-09-02-opc05-bidireccionales-DECISION.md): la mitad de
bidireccionales de OP-C-05 exige que CADA par bidireccional entre vivos tenga un
VEREDICTO DE LECTURA REGISTRADO CON CITA. La lista blanca deja de ser una lista
a mano y pasa a ser un REGISTRO DE CITAS. UN PAR SIN CITA ES ROJO.

LAS DOS VIAS QUE VALEN, Y NO HAY UNA TERCERA AUTOMATICA:

  (1) EL CRIBADO, cuando el par existe en docs/INTRA_DOMINIO_VEREDICTOS.jsonl
      con clase D, B o C. La C es el enlace mutuo legitimo del banco 9.22; la D
      y la B son pares leidos que NO se funden, o sea que la arista de ida y
      vuelta entre ellos no es una escalera que haya que retirar. La cita es EL
      PUESTO.
  (2) LA DECLARACION SELLADA DE P.10, cuando el par cae bajo un nodo puente ya
      declarado y la salida escrita fue DECLARADO Y NO FUNDIDO.

  (3) Y lo que no cubran las dos, VA A LECTURA DIRIGIDA POR P.5, se registra en
      docs/plan/LECTURAS_DIRIGIDAS.md y entra aqui con via LECTURA_DIRIGIDA.
      Este instrumento NO la inventa: la lee de su fichero.

P.1 NO ES OPCIONAL AQUI, Y LA DIFERENCIA ESTA MEDIDA. Todo conteo que toque ids
pasa por el resolutor antes de contar. Sin resolver, el mismo grafo da 147
pares; resolviendo da 153. Las SEIS que faltan solo aparecen tras la resolucion,
y sin ella el registro se daria por completo dejando seis pares sin cita. El
instrumento resuelve LOS DOS LADOS, tanto los del grafo como los del archivo del
cribado (un par leido hace ochenta vueltas puede tener hoy los dos ids
deprecados y resolver a otros dos), y lo dice en su salida.

CONTRASTE QUE PRUEBA QUE MIDE BIEN: sobre el mergebase con main (36b57d78)
tienen que salir 83 pares, no 153.

USO:
  python scripts/loop/vuelta152_registro_de_citas_opc05.py
  python scripts/loop/vuelta152_registro_de_citas_opc05.py --escribir
  python scripts/loop/vuelta152_registro_de_citas_opc05.py --ref <REF>

--- ADJUDICACION 6.1 DEL ACTA 155 (3 sep 2026): `LD-OPC05-097` VA A RELECTURA
CONJUNTA, Y LA C ESCRITA NO SE SOSTIENE POR SI SOLA ---

REGISTRO POR ADICION. NADA DE LO ESCRITO ARRIBA SE BORRA.

EL CASO DEL AUDITOR, QUE LEYO EL PAR A CIEGAS (sin ver la clase, la via, la
cita ni la razon) Y LLEGO A LA MISMA CLASE A QUE EL EJECUTOR MARCO COMO
DISCUTIBLE, con tres reglas escritas empujando al mismo sitio:
  (i)   el perfil de MADRE E HIJO del 9.6.2 NO se cumple, porque el hijo
        tendria que caber ENTERO DENTRO DE UN PASO de la madre y
        `viaje_diagnostico_remedial` se reparte entre los pasos 2, 3 y 4 de
        `juran_rcca_metodo`;
  (ii)  el 9.6.3 manda pesar LO QUE QUEDA FUERA DEL SOLAPE, y fuera quedan el
        paso 1 de juran (esporadico contra cronico, y el enunciado) y el paso 7
        del viaje (gestionar la resistencia), los dos LINEA por la regla
        practica del informe 67.6, sin procedimiento en ningun lado;
  (iii) con LINEA en los dos sentidos, el SEGUNDO POLO del 9.22 dice que
        REPITEN y prescribe FUSION.

Y LA RAZON ESCRITA SE DELATA SOLA: nombra la diferencia de granularidad y las
dos apostillas, que es la definicion literal del segundo polo, y NO nombra una
sola LINEA DISTINTA EN CADA NODO, que es lo que la C exige.

EL LIMITE, ESCRITO ANTES DE QUE SE CRUCE: si la clase pasa a A, se cambia LA
CLASE con su correccion declarada y el par se registra como CANDIDATO A FUSION.
LA FUSION NO SE EJECUTA en una vuelta de lectura ni sin su ficha, su
superviviente y su ruta.

--- ADJUDICACION 6.2 DEL ACTA 155 (3 sep 2026): PARA REGISTRAR C, LA RAZON
TIENE QUE NOMBRAR LAS DOS LINEAS. DONDE NO PUEDA NOMBRARLAS, LA CLASE ES D ---

CORRECCION DECLARADA POR ADICION, y no es doctrina nueva: es extension citable
del 9.22, que lo dice el mismo en su comprobacion separadora, "LA FIGURA EXIGE
DOS LINEAS DISTINTAS, UNA EN CADA NODO", siendo la C sano CON FIGURA.

LO QUE CAMBIA AL REGISTRAR: una entrada en clase C cuya razon NO pueda nombrar
una linea distinta en cada uno de los dos nodos NO es C. Es D, sano y distinto.
El ejemplar que la obliga es `LD-OPC05-040` (`cost_management_plan` contra
`stakeholder_register`): el dinero y las personas, sin una sola linea de uno
que el otro expanda.

LA FRONTERA, MEDIDA PARA QUE NADIE SE ASUSTE: la guarda de `OP-C-05` de
`scripts/run_phase1.py` mete en `_citados` el campo `par` de TODA linea del
registro, SIN MIRAR LA CLASE, asi que RECLASIFICAR DE C A D NO PONE GATE 0 EN
ROJO. Lo que la clase mueve es la lectura, no la cobertura del registro.

--- ADJUDICACION 6.3 DEL ACTA 157 (3 sep 2026): EL SACO DE LAS C SIN FIGURA SE
VACIA LEYENDO, EN LOTES, Y NO EN BLOQUE ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

EL HECHO QUE LO OBLIGA, MEDIDO Y NO SOSPECHADO (auditor, acta 157 seccion 5.1,
salida `_auditor_v157_figura.txt`, con vara propia mas estrecha que la del
ejecutor y coincidiendo en el numero que importa):

    en los 3.388 veredictos del cribado la C aparece 5 veces  : 0,15 por ciento
    en este mismo registro, la via CRIBADO tiene 32 entradas  : CERO en C
    en este mismo registro, la via LECTURA_DIRIGIDA tiene 122 : 119 en C, o sea
                                                                97,5 por ciento
    y el 9.22 dice de su figura: "Primera aparicion en 1.100 pares leidos. Es
    rara".

UNA FIGURA QUE EL BANCO LLAMA RARA NO PUEDE SER EL 97,5 POR CIENTO DE UNA VIA.
LA C DE LA VIA DE LECTURAS DIRIGIDAS Y LA C DEL ARCHIVO NO SON LA MISMA LETRA, y
eso no es una sospecha de redaccion: es una divergencia medida entre dos vias
del mismo fichero.

LAS TRES SALIDAS Y POR QUE SE ELIGE LA SEGUNDA. Reclasificar 116 clases EN
BLOQUE seria mover 116 cifras publicadas sin una lectura detras, que es la
especie exacta de caida que esta campana persigue. Ajustar la vara para que no
las alcance seria dejar escrita como figura rara una letra que el 97,5 por
ciento de una via lleva puesta. SE ADJUDICA LEER: LA CLASE ES UN HECHO SOBRE LOS
NODOS Y SOLO UNA LECTURA LA FIJA. Se lee EN LOTES, una a una.

LAS GUARDAS DEL LOTE, QUE NO SE AFLOJAN: correccion declarada y aditiva en cada
una; `n` NO SE MUEVE; assert de frontera con sha256 de `dataset/` y conteo de
censo y aristas antes y despues (el registro cambia, EL GRAFO NO); Gate 0 al
terminar el lote; y LA QUE SALGA A NO SE VOLTEA, se marca como discutible y no
se ejecuta ninguna fusion.

--- ADJUDICACION 6.4 DEL ACTA 157 (3 sep 2026): NOMBRAR DOS PASOS NO BASTA. LA
FIGURA PIDE DOS LINEAS DISTINTAS Y QUE CADA NODO EXPANDA LA DEL OTRO ---

CORRECCION DECLARADA POR ADICION, y NO ES DOCTRINA NUEVA: es cita literal del
9.22, que escribe su propia comprobacion separadora.

LA VARA, EN UNA SOLA PREGUNTA ESTRECHA Y BINARIA, que es la que se aplica a cada
lectura dirigida en clase C:

    SE PUEDEN NOMBRAR DOS LINEAS DISTINTAS, UNA EN CADA NODO, Y DECIR QUE
    PROCEDIMIENTO DEL OTRO NODO EXPANDE CADA UNA?

  - Si SI: la C se sostiene, y la razon LAS NOMBRA.
  - Si NO: la clase es D.
  - Y si la razon describe que CADA NODO EXPANDE LO SUYO, eso es el PUESTO 2091
    del banco y la clase es D. Dos nodos sanos que no se tocan son D, no C.

LO QUE EL 9.22 DICE Y QUE ESTA VARA SOLO REPITE: "Si las dos direcciones apuntan
a la misma linea, no es esta figura". O sea que ni siquiera nombrar dos punteros
de paso basta si los dos punteros van a la misma linea. `LD-OPC05-031` se
delataba solo diciendo de si mismo que las dos son "casi la misma linea" y
sosteniendose "porque el sujeto es distinto": SUJETO DISTINTO ES LA DEFINICION
DE D, NO DE C.

ESTA VARA ALCANZA AL SACO PEQUENO IGUAL QUE AL GRANDE: traer puntero de paso NO
protege. Y no protege tampoco ser SANO: la 6.3 del acta 155 sostuvo
`LD-OPC05-046` en C por el 9.6.3, o sea POR SER SANO, y bajo esta vara SANO SIN
FIGURA ES D. Esa parte de la 6.3 del acta 155 queda revocada por el acta 157.

--- ADJUDICACION 6.6 DEL ACTA 157 (3 sep 2026): LA D SE QUEDA, EL MOTIVO LO
LLEVA LA RAZON, Y ANTES DE PROPONER UNA LETRA NUEVA SE MIDE LA CUENTA ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

LA OBJECION, QUE EL ACTA CONCEDE: la etiqueta D se lee en el archivo como SANO Y
DISTINTO, y hay pares registrados en D cuyo motivo real es MADRE E HIJO, EL PAR
CONTINUA (tercer caso del 9.22). La etiqueta no miente sobre la clase, pero no
cubre uno de sus dos motivos.

POR QUE NO ES PARADA Y NO SE INVENTA LETRA: EL ARCHIVO YA RESOLVIO ESA ESPECIE
EN D DESDE HACE TIEMPO, y el auditor lo midio en el registro del cribado el 3
sep 2026: los PUESTOS 316 ("la eleccion del metodo de estimacion contra la hoja
que lo calcula"), 478 ("EL HIJO CON CASA PROPIA"), 1424, 1494 y 2066 son todos
madre e hijo REGISTRADOS EN D. No hay contradiccion que resolver ni regla nueva
que escribir. UNA LETRA NUEVA SI SERIA DOCTRINA NUEVA Y ESO SI SERIA PARADA: no
se abre sin la cuenta delante.

LO QUE SE ENCARGA ANTES DE QUE NADIE PROPONGA NADA, Y ES SOLO MEDIR: repartir
las D de este registro en MADRE E HIJO (el par continua) contra SANO Y DISTINTO,
por lectura de su razon, publicar los dos conteos y la nomina de cada saco, y
declarar la vara con sus limites. Se hace en la TAREA 8 de la vuelta 157 con
`scripts/loop/vuelta157_tarea8_dos_especies_de_d.py`, salida
`docs/loop/SALIDA_V157_T8_DOS_ESPECIES_D.txt`. ESA TAREA MIDE: no reclasifica
nada y no toca una clase.

--- ADJUDICACION 6.8 DEL ACTA 157 (3 sep 2026): EL LECTOR SE ENSANCHA PARA
ACEPTAR LA CELDA TACHADA Y TOMAR LA ULTIMA CLASE ESCRITA ---

CORRECCION DECLARADA POR ADICION, y toca `citas_de_lectura_dirigida`, que es la
funcion de este fichero que lee `docs/plan/LECTURAS_DIRIGIDAS.md`.

EL CHOQUE QUE LA ORIGINA, Y LAS DOS REGLAS QUE CHOCABAN. La costumbre de la casa
es NO TAPAR LO QUE SE CORRIGE, y en el `.md` eso se escribe tachando la clase
vieja (`~~C~~ D`). Pero el patron de esta funcion pedia `([A-Z]+)` en la celda
de clase, asi que una celda tachada NO CASABA Y LA FILA DESAPARECIA DEL
REGISTRO. Medido por mutacion por el auditor (acta 157, seccion 5.4, salida
`_auditor_v157_tachado.txt`) sobre la fila 97: como estaba, 1 coincidencia; con
`~~C~~ D`, 0 COINCIDENCIAS. La vuelta 156 eligio bien al dejar la celda limpia,
porque lo otro tumbaba Gate 0.

LO QUE SE ADJUDICA: LA GUARDA SE ADAPTA AL REGISTRO HONESTO, NO AL REVES (banco
9, por extension). El patron acepta una celda con una o mas clases tachadas
seguidas de la clase vigente, Y TOMA LA ULTIMA CLASE ESCRITA. Con su caso
positivo por mutacion (`scripts/loop/vuelta157_tarea4b_mutacion_tachado.py`,
salida `docs/loop/SALIDA_V157_T4B_MUTACION_TACHADO.txt`), que exige las tres
cosas: que el lector VIEJO pierda la fila tachada, que el NUEVO la recupere con
la clase buena, Y que el conteo de pares del registro salga IDENTICO antes y
despues sobre el fichero SIN tachar.

--- ADJUDICACION 6.3 DEL ACTA 158 (3 sep 2026): LA PREGUNTA BINARIA DE LA 6.4 ES
UN EXISTENCIAL. SE HACE SOBRE TODOS LOS PARES DE LINEAS CANDIDATOS, NO SOBRE EL
PRIMERO QUE SE ENCUENTRE ---

CORRECCION DECLARADA POR ADICION, y NO ES DOCTRINA NUEVA: es la letra de la 6.4
del acta 157 leida entera. La 6.4 pregunta si SE PUEDEN nombrar dos lineas
distintas, y eso es un existencial: basta con que EXISTA UN PAR que cumpla.

LA CONSECUENCIA, QUE ES LO QUE AL LOTE 1 LE FALTO: hallar un par de lineas que
colapsa en la misma linea prueba que ESE PAR no es la figura, NO que no la haya.
El colapso del 9.22 descarta un par, no un nodo.

LA REGLA DE ESCRITURA QUE SE ADJUDICA, Y ES OBLIGATORIA DESDE LA PRIMERA LECTURA
DEL LOTE 2: cuando el colapso del 9.22 sea el motivo del descarte, la razon
tiene que decir TAMBIEN que NINGUN otro par de lineas sostiene la figura, y
NOMBRAR el par mas fuerte que se descarto.

EL CASO QUE LA ORIGINA, PARA QUE NO SE LEA COMO UNA REGLA SIN CUERPO
(`LD-OPC05-005`, acta 158 seccion 3.1): la razon del lote 1 descarto la figura
porque el paso 1 de `aim_of_leadership` y el paso 13 de
`causas_comunes_vs_especiales` son la misma linea, y para ESE par tenia razon.
Pero habia otro par disponible: el paso 2 de aim (investigar las causas de raiz
DEL SISTEMA) contra el paso 13 de causas, cada uno expandido por procedimientos
del otro nodo. Un existencial no se refuta con un caso.

--- ADJUDICACION 6.6 DEL ACTA 158 (3 sep 2026): EL CAMPO `cita` SE UNIFICA EN
UNA SOLA FORMA, Y GANA LA QUE NO TAPA ---

CORRECCION DECLARADA POR ADICION, y toca el campo `cita` del registro
`docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl`. Nada de lo escrito arriba se borra.

EL HECHO, MEDIDO POR EL AUDITOR COMPARANDO EL REGISTRO DE `abb2fe4e` CONTRA HEAD
(acta 158, seccion 5.1): en la vuelta 157 cambiaron 62 campos `cita`, y
cambiaron POR SOBREESCRITURA (`'LD-OPC05-001, clase C'` paso a
`'LD-OPC05-001, clase D'`, sin dejar el texto viejo). Pero las TRES que la
vuelta 156 reclasifico dicen otra cosa EN EL MISMO FICHERO
(`'LD-OPC05-002, clase C  [RECLASIFICADA A D EN LA VUELTA 156: ver la razon]'`).
DOS FORMAS PARA EL MISMO HECHO, EN EL MISMO FICHERO, EN DOS VUELTAS SEGUIDAS. Y
ademas esas tres hoy leen literalmente "clase C" en una fila cuya clase es D.

LO QUE SE ADJUDICA, POR EXTENSION DE LA 6.8 DEL ACTA 157 (la costumbre de la
casa, no tapar lo que se corrige) Y DE LA LEY DE UNA SOLA FUENTE: UNA SOLA FORMA
para las 65 filas corregidas, la que lleva la clase VIGENTE Y el rastro:

    clase D [ANTES C, RECLASIFICADA EN LA VUELTA N: ver la razon]

Con eso las 62 recuperan el rastro que la sobreescritura les quito y las 3 de la
vuelta 156 dejan de leer "clase C" en una fila que es D. Se hace POR ADICION,
con correccion declarada, y con el assert de que NINGUNA clase se mueve al
hacerlo y de que el conteo de pares del registro sale identico antes y despues.
Se ejecuta en la TAREA 4 de la vuelta 159.

NINGUNA CIFRA PUBLICADA ERA FALSA POR ESTO y el acta lo dice: la razon declara
la correccion en las 62 y ningun reporte afirmo nada sobre las citas. Lo que se
corrige es que la del 156 tapa menos y la del 157 tapa mas.

--- ADJUDICACION 6.5 DEL ACTA 159 (3 sep 2026): UNA INSTANCIA NO ES EL
PROCEDIMIENTO DE SU CATEGORIA. ADJUDICADA, Y NO ES DOCTRINA NUEVA ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra.

LA REGLA, TAL COMO EL EJECUTOR LA FORMULO EN EL LOTE 2 DE LA VUELTA 159 Y TAL
COMO EL ACTA 159 LA ADJUDICA: cuando la linea de un nodo dice "aplica tecnicas
graficas", "mapea tus fuentes de ingresos" o "consolida los planes
subsidiarios", y el otro nodo ES UNA de esas tecnicas, uno de esos patrones o
uno de esos planes, ESO NO ES EXPANSION: es un ejemplar de la categoria.

POR QUE NO ES DOCTRINA NUEVA Y POR ESO NO HUBO PARADA: una regla escrita la
cubre por extension citable. La 6.4 del acta 157 pregunta si el otro nodo es EL
COMO SE HACE de una linea; un ejemplar de una categoria es el QUE, no el COMO, y
por eso no la expande. Y la 6.4 del acta 158, en la `122`, ya escribio la forma
general: NOMBRAR SIN PROCEDIMENTAR ES EXACTAMENTE LO QUE LA 6.4 EXCLUYE.

LAS DOS CONDICIONES CON QUE SE ADJUDICA, Y LAS DOS SON OBLIGATORIAS:
  (a) CUANDO SEA EL UNICO MOTIVO DEL DESCARTE, la razon lo dice con esa letra y
      marca la fila como DISCUTIBLE, como ya se hizo en la `078` y la `103`.
  (b) SU CONSISTENCIA SE AUDITA EN LA SEGUNDA PASADA DE LA 6.4, sobre las 37: en
      cada una, si la regla APLICA se dice; y si NO aplica pudiendo parecer que
      si, TAMBIEN se dice, y se publica el conteo de las dos cosas. EL RIESGO DE
      UNA REGLA NUEVA NO ES APLICARLA MAL UNA VEZ, ES APLICARLA SOLO CUANDO
      CONVIENE.
"""
import argparse
import collections
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VERED = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")

CLASES_QUE_VALEN = ("D", "B", "C")

# LOS PUENTES DE P.10, leidos de docs/plan/BANCO_DEL_PLAN.md, seccion P.10, tabla
# LOS TRES EJEMPLARES. Solo cuentan los que la tabla cierra como DECLARADO Y NO
# FUNDIDO, o sea aquellos cuya columna "como acabo" dice que el par NO se funde y
# se enlaza. Se escriben aqui con su fila para que la cita se pueda ir a ver.
PUENTES_P10 = {
    "customer_validation": "P.10 ejemplar 3, tabla LOS TRES EJEMPLARES: puente doble con "
                           "filosofia_customer_validation sobre LD-59; 'no queda lectura que "
                           "desempate: se funde solo el triangulo cerrado y el cuarto SE ENLAZA'",
    "filosofia_customer_validation": "P.10 ejemplar 3, tabla LOS TRES EJEMPLARES: puente doble con "
                                     "customer_validation sobre LD-59; el cuarto SE ENLAZA",
}


def cargar(ref):
    if ref == "WORK":
        return json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    b = subprocess.run(["git", "show", "%s:dataset/metadata/master_graph.json" % ref],
                       capture_output=True, cwd=RAIZ)
    if b.returncode:
        raise SystemExit("ROJO: no se pudo leer %s" % ref)
    return json.loads(b.stdout.decode("utf-8"))["nodos"]


def hacer_resolver(N):
    """P.1, RE ESCRITO AQUI y no importado del codigo que esta guarda vigila."""
    alias = {}
    for nid, n in N.items():
        for a in (n.get("ids_alias") or []):
            if a != nid:
                alias[a] = nid

    def r(nid):
        n = N.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid
        visto, cur, ult = {nid}, nid, (nid if n is not None else None)
        while cur in alias:
            cur = alias[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = N.get(cur)
            if c is None:
                continue
            ult = cur
            if not c.get("deprecado"):
                return cur
        return ult
    return r


def bidireccionales(N, resolver=True):
    r = hacer_resolver(N)
    S = set()
    for nid, n in N.items():
        if n.get("deprecado"):
            continue
        for d in (n.get("nodos_siguientes") or []):
            if d not in N:
                continue
            a, b = (r(nid), r(d)) if resolver else (nid, d)
            if a and b and a != b and not N[a].get("deprecado") and not N[b].get("deprecado"):
                S.add((a, b))
    return {tuple(sorted(p)) for p in S if (p[1], p[0]) in S}


def citas_del_cribado(N):
    """El archivo del cribado, con LOS DOS LADOS RESUELTOS con el resolutor de
    hoy. Un par leido hace ochenta vueltas puede traer dos ids que hoy estan
    deprecados: sin resolver, ese veredicto se perderia."""
    r = hacer_resolver(N)
    idx = collections.defaultdict(list)
    for x in io.open(VERED, encoding="utf-8"):
        if not x.strip():
            continue
        d = json.loads(x)
        a, b = r(d["nodo_a"]), r(d["nodo_b"])
        if a and b and a != b:
            idx[tuple(sorted((a, b)))].append(d)
    return idx


# EL PATRON DE LA FILA DE LECTURA DIRIGIDA, EN DOS VERSIONES Y LAS DOS VIVAS
# (vuelta 157, TAREA 4, adjudicacion 6.8 del acta 157).
#
# EL VIEJO NO SE BORRA Y NO ES DECORACION: es EL SUJETO del caso positivo por
# mutacion `scripts/loop/vuelta157_tarea4b_mutacion_tachado.py`, que lo importa
# de aqui y exige que SIGA PERDIENDO la fila tachada. Borrarlo dejaria la
# correccion sin nada contra lo que probarse.
PATRON_FILA_LD_VIEJO = re.compile(
    r"REGISTRO DE CITAS `OP-C-05`\s*\|\s*([a-z0-9_]+)\s*<->\s*([a-z0-9_]+)\s*\|\s*"
    r"([A-Z]+)\s*\|\s*(LD-[A-Za-z0-9.\-]+)\s*\|\s*([^\n|]+)")

# EL NUEVO acepta la celda de clase con UNA O MAS CLASES TACHADAS delante de la
# vigente (`~~C~~ D`, y tambien `~~B~~ ~~C~~ D` el dia que haga falta), y de esa
# celda se toma LA ULTIMA CLASE ESCRITA. Lo demas del patron no se toca.
PATRON_FILA_LD = re.compile(
    r"REGISTRO DE CITAS `OP-C-05`\s*\|\s*([a-z0-9_]+)\s*<->\s*([a-z0-9_]+)\s*\|\s*"
    r"((?:~~[A-Z]+~~\s*)*[A-Z]+)\s*\|\s*(LD-[A-Za-z0-9.\-]+)\s*\|\s*([^\n|]+)")


def clase_de_celda(celda):
    """LA ULTIMA CLASE ESCRITA EN LA CELDA, que es la vigente.

    En `~~C~~ D` la clase es D y la C queda a la vista, que es exactamente lo
    que la costumbre de la casa pide: no tapar lo que se corrige. En una celda
    limpia (`D`) devuelve D, asi que el fichero SIN tachar se lee igual que
    antes de esta correccion, y eso lo comprueba el conteo del caso positivo."""
    return re.findall(r"[A-Z]+", celda)[-1]


def citas_de_lectura_dirigida(N, patron=None):
    """Las lecturas de esta campana escritas en docs/plan/LECTURAS_DIRIGIDAS.md
    con la marca de registro de citas de OP-C-05. Se leen de su fichero: este
    instrumento NO adjudica, solo recoge.

    CORRECCION DECLARADA (vuelta 157, TAREA 4, adjudicacion 6.8 del acta 157):
    la celda de clase admite el TACHADO y se toma la ULTIMA clase escrita. El
    patron viejo, que pedia `[A-Z]+` a secas y perdia la fila entera cuando la
    celda venia tachada, sigue vivo arriba como `PATRON_FILA_LD_VIEJO` para que
    su caso positivo por mutacion tenga contra que compararse.

    `patron` existe SOLO para esa mutacion: en produccion nadie lo pasa y vale
    el nuevo."""
    r = hacer_resolver(N)
    out = {}
    if not os.path.exists(LD):
        return out
    texto = io.open(LD, encoding="utf-8").read()
    return citas_de_lectura_dirigida_de_texto(texto, r, patron)


def citas_de_lectura_dirigida_de_texto(texto, r, patron=None):
    """El mismo recorrido pero sobre un TEXTO en memoria, para que la mutacion
    pueda tachar una celda SIN TOCAR EL FICHERO DEL REPO."""
    out = {}
    for m in (patron or PATRON_FILA_LD).finditer(texto):
        a, b = r(m.group(1)), r(m.group(2))
        if not a or not b or a == b:
            continue
        out[tuple(sorted((a, b)))] = {
            "clase": clase_de_celda(m.group(3)), "ld": m.group(4),
            "motivo": m.group(5).strip()}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="WORK")
    ap.add_argument("--escribir", action="store_true")
    args = ap.parse_args()

    N = cargar(args.ref)
    CON = bidireccionales(N, True)
    SIN = bidireccionales(N, False)
    print("REF: %s" % args.ref)
    print("=" * 96)
    print("P.1 PRIMERO, Y CON LA DIFERENCIA MEDIDA")
    print("=" * 96)
    print("  pares bidireccionales entre vivos RESOLVIENDO ALIAS (P.1) : %d" % len(CON))
    print("  pares bidireccionales entre vivos SIN resolver            : %d" % len(SIN))
    print("  pares que SOLO aparecen tras resolver                     : %d" % len(CON - SIN))
    for p in sorted(CON - SIN):
        print("      %s <-> %s" % p)
    print("  SIN P.1 el registro se daria por completo dejando esos pares sin cita.")
    print("")

    cribado = citas_del_cribado(N)
    lecturas = citas_de_lectura_dirigida(N)

    registro, sin_veredicto = [], []
    for p in sorted(CON):
        a, b = p
        filas = [x for x in cribado.get(p, []) if x["clase"] in CLASES_QUE_VALEN]
        malas = [x for x in cribado.get(p, []) if x["clase"] not in CLASES_QUE_VALEN]
        if filas:
            f = sorted(filas, key=lambda x: (x["clase"] != "C", x.get("puesto_intra") or 0))[0]
            registro.append({
                "par": [a, b], "via": "CRIBADO", "clase": f["clase"],
                "cita": "puesto %s, dominio %s, clase %s"
                        % (f.get("puesto_intra"), f.get("dominio"), f["clase"]),
                "nodo_a_leido": f["nodo_a"], "nodo_b_leido": f["nodo_b"],
                "razon": (f.get("razon") or "")[:400]})
            continue
        if p in lecturas:
            L = lecturas[p]
            registro.append({
                "par": [a, b], "via": "LECTURA_DIRIGIDA", "clase": L["clase"],
                "cita": "%s, clase %s" % (L["ld"], L["clase"]),
                "nodo_a_leido": a, "nodo_b_leido": b, "razon": L["motivo"]})
            continue
        puente = [x for x in (a, b) if x in PUENTES_P10]
        if puente:
            registro.append({
                "par": [a, b], "via": "P.10", "clase": "DECLARADO Y NO FUNDIDO",
                "cita": PUENTES_P10[puente[0]],
                "nodo_a_leido": a, "nodo_b_leido": b,
                "razon": "nodo puente declarado en P.10; su salida escrita es enlazar, no fundir"})
            continue
        sin_veredicto.append((p, malas))

    print("=" * 96)
    print("EL CRUCE, CONTADO")
    print("=" * 96)
    porvia = collections.Counter(x["via"] for x in registro)
    for via in ("CRIBADO", "P.10", "LECTURA_DIRIGIDA"):
        print("  con cita por %-18s : %d" % (via, porvia.get(via, 0)))
    print("  CON CITA, TOTAL              : %d de %d" % (len(registro), len(CON)))
    print("  SIN VEREDICTO                : %d" % len(sin_veredicto))
    print("")
    if registro:
        print("  clases de las citas del cribado: %s"
              % dict(collections.Counter(x["clase"] for x in registro if x["via"] == "CRIBADO")))
    print("")

    print("=" * 96)
    print("LOS PARES SIN VEREDICTO (%d). ESTOS SON LOS QUE VAN A LECTURA DIRIGIDA POR P.5."
          % len(sin_veredicto))
    print("=" * 96)
    for (a, b), malas in sin_veredicto:
        extra = ""
        if malas:
            extra = "  [OJO: el cribado SI trae este par con clase %s, que NO vale aqui]" % (
                ", ".join(sorted({x["clase"] for x in malas})))
        print("  %-46s <-> %s%s" % (a, b, extra))
    print("")

    if args.escribir:
        lineas = [json.dumps(x, ensure_ascii=False, sort_keys=True) for x in registro]
        io.open(REGISTRO, "w", encoding="utf-8", newline="\n").write("\n".join(lineas) + "\n")
        print("ESCRITO: docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl con %d entrada(s)." % len(registro))
        vuelto = [json.loads(x) for x in io.open(REGISTRO, encoding="utf-8") if x.strip()]
        assert len(vuelto) == len(registro), "el registro no releyo lo que escribio"
        assert {tuple(sorted(x["par"])) for x in vuelto} == {tuple(sorted(x["par"])) for x in registro}
        print("  [OK] releido y cotejado: %d entradas, mismos pares." % len(vuelto))
        print("  [OK] pares del grafo cubiertos: %d de %d. SIN CITA: %d"
              % (len(registro), len(CON), len(sin_veredicto)))


main()
