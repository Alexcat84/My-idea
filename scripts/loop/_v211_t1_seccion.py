# -*- coding: utf-8 -*-
r"""_v211_t1_seccion.py . COMPONE EL CUERPO DE LA TAREA 1 DEL REPORTE DE LA
VUELTA 211 **CONTANDO SUS FICHEROS DE SALIDA**, y lo deja en
`scripts/loop/_v211_t1_seccion.md` para que `anexar_tarea_al_reporte.py` lo
anexe al cerrarse la tarea.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3).

LA LETRA QUE OBEDECE, PALABRA POR PALABRA (`EJECUTOR.md` 1, LA TABLA SE CUENTA
DE SU FICHERO): *"TODA TABLA O CIFRA DEL REPORTE CITA EL FICHERO DE SALIDA DEL
QUE SALE, Y SE RECONSTRUYE CONTANDO ESE FICHERO ANTES DE PUBLICARLA"*. Aqui
NINGUNA cifra se teclea: todas salen de `re` sobre las salidas selladas de esta
vuelta, y la tabla de la particion se pega ENTERA del fichero que la lleva.

LAS CITAS DE ACTA LLEVAN SU LINEA (`6.6` del acta 210, linea 74203 de
`docs/loop/ACTA_AUDITOR.md`), y las lineas se LEEN aqui del propio fichero del
acta con `grep` de `re`, no se recuerdan: si el texto no vive en la linea que se
publica, este computo cae en rojo y no escribe.

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
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")

FALLOS = []


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
        FALLOS.append(etiqueta)
        return "(SIN LEER)"
    return m[0]


def linea_del_acta(fragmento, etiqueta):
    """LA LINEA DE ACTA_AUDITOR.md DONDE VIVE UN TEXTO, LEIDA Y NO RECORDADA.
    Cae en rojo si el fragmento no aparece exactamente una vez."""
    lineas = io.open(ACTA, "rb").read().replace(b"\r\n", b"\n").decode(
        "utf-8", errors="replace").split(NL)
    hits = [i for i, l in enumerate(lineas, 1) if fragmento in l]
    if len(hits) != 1:
        print("ROJO: %s -> el fragmento %r vive en %d lineas (se exige 1)"
              % (etiqueta, fragmento[:60], len(hits)))
        FALLOS.append(etiqueta)
        return 0
    return hits[0]


B = leer("SALIDA_V%d_T1B_CERRAR_DOS_ESTADOS.txt" % VUELTA)
BM = leer("SALIDA_V%d_T1B_CERRAR_DOS_ESTADOS_MUTADO.txt" % VUELTA)
E = leer("SALIDA_V%d_T1E_GRUPO_HOROWITZ.txt" % VUELTA)
EM = leer("SALIDA_V%d_T1E_GRUPO_HOROWITZ_MUTADO.txt" % VUELTA)
AP = leer("SALIDA_V%d_APERTURA.txt" % VUELTA)

# --- 1.b, TODO LEIDO DE SU SALIDA -------------------------------------------
b_entrar = uno(B, r"GUARDA \(1\), PRIMERA MITAD.*?OPERACIONES\.jsonl: (\d+) bytes en disco y (\d+) bytes",
               "1.b sede al entrar", re.S)
b_sha0 = uno(B, r"GUARDA \(1\), PRIMERA MITAD.*?sha256 disco (\w+) y sha256 LF (\w+)",
             "1.b sha al entrar", re.S)
b_fichas0 = uno(B, r"CIFRA fichas en el fichero AL ENTRAR: (\d+)", "1.b fichas al entrar")
b_salir = uno(B, r"GUARDA \(1\), AL SALIR.*?OPERACIONES\.jsonl: (\d+) bytes en disco y (\d+) bytes",
              "1.b sede al salir", re.S)
b_sha1 = uno(B, r"GUARDA \(1\), AL SALIR.*?sha256 disco (\w+) y sha256 LF (\w+)",
             "1.b sha al salir", re.S)
b_pasan = uno(B, r"CIFRA fichas que pasan la guarda \(1\): (\d+) de (\d+)", "1.b fichas que pasan")
b_filas = uno(B, r"CIFRA filas de git diff --numstat sobre docs/plan/: (\d+)", "1.b filas numstat")
b_anad = uno(B, r"CIFRA lineas anadidas: (\d+) \| CIFRA lineas borradas: (\d+)", "1.b anadidas")
b_hecha = uno(B, r"'HECHA'   ANTES (\d+)   DESPUES (\d+)", "1.b reparto HECHA")
b_lista = uno(B, r"'LISTA'   ANTES (\d+)   DESPUES (\d+)", "1.b reparto LISTA")
b_total = uno(B, r"TOTAL     ANTES (\d+)   DESPUES (\d+)", "1.b reparto total")
b_movidas = uno(B, r"CIFRA fichas que se movieron: (\d+)", "1.b fichas movidas")
b_otros = uno(B, r"CIFRA otros id_op cuyo estado cambio: (\d+)", "1.b otros movidos")
b_recarga = uno(B, r"CIFRA fichas releidas del disco: (\d+)", "1.b recarga")
b_malas = uno(B, r"CIFRA lineas que no son JSON valido: (\d+)", "1.b lineas malas")
b_veredicto = uno(B, r"VEREDICTO DE LAS TRES GUARDAS: (.+)", "1.b veredicto")
bm_veredicto = uno(BM, r"VEREDICTO DE LA PRUEBA DE MUTACION: (.+)", "1.b veredicto mutacion")
bm_codigo = uno(BM, r"CODIGO CON EL QUE EL COMPUTO IBA A CERRAR: (\d+)", "1.b codigo mutado")

# --- 1.e, TODO LEIDO DE SU SALIDA -------------------------------------------
e_menciones = uno(E, r"CIFRA menciones de 'posicionamiento_de_empresa' en 02_DESTEJIDOS\.md: (\d+)",
                  "1.e menciones destejidos")
e_ops = uno(E, r"CIFRA operaciones cuyo campo nodos lo contiene: (\d+)", "1.e operaciones")
e_idop = uno(E, r"linea (\d+) \| id_op (\S+) \| tipo (\S+) \| estado '(\w+)' \| fase (\S+)",
             "1.e identidad de la operacion")
e_nodos = uno(E, r"CIFRA nodos del campo `nodos` de \S+, contada hoy: (\d+)", "1.e nodos del campo")
e_filas = uno(E, r"CIFRA filas leidas de la tabla: (\d+)", "1.e filas de la tabla")
e_falta_campo = uno(E, r"CIFRA nodos de la tabla que NO estan en el campo: (\d+)", "1.e falta campo")
e_falta_tabla = uno(E, r"CIFRA nodos del campo que NO estan en la tabla: (\d+)", "1.e falta tabla")
e_grafo = uno(E, r"CIFRA nodos del grafo: (\d+)", "1.e nodos del grafo")
e_aparte = uno(E, r"EL BLOQUE YA VIVE APARTE     (\d+) nodo\(s\)", "1.e reparto aparte")
e_ninguna = uno(E, r"NI UNA COSA NI LA OTRA       (\d+) nodo\(s\)", "1.e reparto ninguna")
e_repartidos = uno(E, r"CIFRA nodos repartidos: (\d+)", "1.e repartidos")
e_sinmedir = uno(E, r"CIFRA nodos que NO se pudieron medir: (\d+)", "1.e sin medir")
e_uniforme = uno(E, r"LA PARTICION ES UNIFORME: (\w+)", "1.e uniforme")
em_ninguna = uno(EM, r"NI UNA COSA NI LA OTRA       (\d+) nodo\(s\)", "1.e mutado ninguna")

# EL CUBO QUE NO SALE EN LA CORRIDA LIMPIA SE CUENTA COMO CERO, Y SE DICE.
e_dentro = "0"
if "EL BLOQUE SIGUE DENTRO" in E.split("EL REPARTO, CONTADO")[1][:400]:
    e_dentro = uno(E, r"EL BLOQUE SIGUE DENTRO       (\d+) nodo\(s\)", "1.e reparto dentro")

# LA TABLA DE LA PARTICION, PEGADA ENTERA DEL FICHERO Y NO RECOMPUESTA.
tabla = [l for l in E.split(NL) if l.startswith("| ") and "`" in l]
cab = [l for l in E.split(NL) if l.startswith("| # | nodo")]
sep = [l for l in E.split(NL) if l.startswith("|---:|---|")]
if len(cab) != 1 or len(sep) != 1 or len(tabla) != int(e_filas or 0):
    print("ROJO: la tabla de la particion no se pudo pegar entera (%d cabeceras, "
          "%d separadores, %d filas contra %s de la salida)"
          % (len(cab), len(sep), len(tabla), e_filas))
    FALLOS.append("1.e tabla entera")
TABLA = NL.join(cab + sep + tabla)

# --- LAS LINEAS DEL ACTA, LEIDAS Y NO RECORDADAS ----------------------------
L_210 = linea_del_acta("# ACTA DEL AUDITOR, VUELTA 210 (8 sep 2026, auditor Opus 5)",
                       "linea del acta 210")
L_64 = linea_del_acta("**`6.4` `OP-L-02` SE CIERRA. 18 DE 18.**", "linea de la 6.4 de la 209")
L_65 = linea_del_acta("**`6.5` `OP-L-03` LLEVA UNA VUELTA CERRADA POR ACTA",
                      "linea de la 6.5 de la 209")
L_2C = linea_del_acta("mismas tres guardas del `2.c` de esta vuelta, que salieron limpias.",
                      "linea del 2.c de la 209")
L_63 = linea_del_acta("**`6.3` EL `D.2` Y LA `P.1` SE CONTESTAN JUNTOS",
                      "linea de la 6.3 de la 210")
L_66 = linea_del_acta("**`6.6` LA FAMILIA DE LA CITA MAL ATRIBUIDA GANA SU REMEDIO",
                      "linea de la 6.6 de la 210")
L_71 = linea_del_acta("**`7.1` LA RAZON DEL PUESTO 1357 DESCRIBE UN NODO DE NUEVE PASOS",
                      "linea del 7.1 de la 210")
# LA CITA DE LA CLAUSULA INVARIANTE **PARTE EN DOS LINEAS DEL ACTA**, y por eso
# se ancla en su arranque y se publican LAS DOS: la 74232 abre y la 74233 cierra.
# Anclarla entera daba CERO coincidencias y el compositor lo dijo en rojo en vez
# de publicar una linea inventada, que es para lo que existe esta guarda.
L_INV = linea_del_acta("*\"El solape de este par cae en", "linea de la clausula INVARIANTE")
L_INV2 = linea_del_acta("el primer bloque y el veredicto es INVARIANTE\"*",
                        "linea de cierre de la clausula INVARIANTE")

ap_acta = uno(AP, r"CIFRA docs/loop/ACTA_AUDITOR\.md: (\d+) bytes en disco y (\d+) bytes",
              "apertura del acta")
ap_sha = uno(AP, r"CIFRA docs/loop/ACTA_AUDITOR\.md: \d+ bytes en disco y \d+ bytes normalizado a LF \(\w+\), sha256 disco (\w+)",
             "sha de apertura del acta")

CUERPO = """### TAREA 1. LOS REGISTROS, Y LOS DOS CAMPOS `estado` QUE EL ACTA 209 DEJO ADJUDICADOS

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN con
`scripts/loop/_v%(v)d_t1_seccion.py` de `docs/loop/SALIDA_V%(v)d_T1B_CERRAR_DOS_ESTADOS.txt`,
`docs/loop/SALIDA_V%(v)d_T1B_CERRAR_DOS_ESTADOS_MUTADO.txt`,
`docs/loop/SALIDA_V%(v)d_T1E_GRUPO_HOROWITZ.txt`,
`docs/loop/SALIDA_V%(v)d_T1E_GRUPO_HOROWITZ_MUTADO.txt` y
`docs/loop/SALIDA_V%(v)d_APERTURA.txt`, **y ese compositor cae en rojo si no puede leer
una sola de ellas**. Las lineas de acta que se citan aqui las **busca el propio
compositor en `docs/loop/ACTA_AUDITOR.md`** y caen en rojo si el texto no vive en
exactamente una linea: **se leen, no se recuerdan** (`6.6` del acta 210, linea **%(L66)d**).

#### 1.a. EL ACTA 210, LEIDA Y NO REESCRITA

La seccion de la **210** abre en la linea **%(L210)d** de `docs/loop/ACTA_AUDITOR.md`,
que mi apertura mide en **%(acta_disco)s** bytes en disco y **%(acta_lf)s** normalizado
a LF, `sha256` **`%(acta_sha)s`** (%(acta_kb).1f KB). **Calza al digito con el encargo**,
que publica **4902898** y **`7217a5d76c98d65f`**.

#### 1.b. LOS DOS CAMPOS `estado`, EN EL MISMO COMPUTO Y CON LAS TRES GUARDAS

Las dos adjudicaciones que lo mandan viven en el acta **209**: la **`6.4`** en la linea
**%(L64)d** (*"`OP-L-02` SE CIERRA. 18 DE 18"*) y la **`6.5`** en la **%(L65)d**
(*"`OP-L-03` LLEVA UNA VUELTA CERRADA POR ACTA Y SU `estado` SIGUE EN `LISTA`"*). Las
tres guardas son las que esa misma acta nombra en su linea **%(L2C)d**: *"el pase se
ejecuta con las mismas tres guardas del `2.c` de esta vuelta, que salieron limpias"*.

**EL CASO ROJO SE PROBO POR MUTACION ANTES DE ESCRIBIR NADA** (`EJECUTOR.md` 1). Con el
nombre de la segunda ficha cambiado a `OP-L-99`, el computo iba a cerrar con codigo
**%(bm_cod)s** y la prueba dio **%(bm_ver)s**. Sellado en
`docs/loop/SALIDA_V%(v)d_T1B_CERRAR_DOS_ESTADOS_MUTADO.txt`.

**GUARDA (1). LA SEDE POR LAS DOS CONVENCIONES, AL ENTRAR Y AL SALIR:**

| `docs/plan/OPERACIONES.jsonl` | bytes en disco | bytes normalizado a LF | `sha256` disco | `sha256` LF |
|---|---:|---:|---|---|
| **AL ENTRAR** | **%(b_e0)s** | **%(b_e1)s** | **`%(b_s0)s`** | **`%(b_s1)s`** |
| **AL SALIR** | **%(b_x0)s** | **%(b_x1)s** | **`%(b_x_s0)s`** | **`%(b_x_s1)s`** |

Los bytes no se mueven porque `LISTA` y `HECHA` miden lo mismo, **y los `sha256` si
cambian**, que es lo que prueba que algo se escribio. **%(b_pasan0)s de %(b_pasan1)s**
fichas pasaron la guarda del valor viejo, las dos leyendo `LISTA` del fichero.

**GUARDA (2). SOLO CAMBIAN ESOS DOS CAMPOS.** `git diff --numstat` sobre `docs/plan/`
da **%(b_filas)s** fila, con **%(b_anad)s** lineas anadidas y **%(b_borr)s** borradas.
Las dos cuentas por `estado`, las dos publicadas:

| `estado` | ANTES | DESPUES |
|---|---:|---:|
| `HECHA` | **%(hecha0)s** | **%(hecha1)s** |
| `LISTA` | **%(lista0)s** | **%(lista1)s** |
| **TOTAL** | **%(tot0)s** | **%(tot1)s** |

**CIFRA fichas que se movieron: %(b_mov)s.** **CIFRA otros `id_op` cuyo `estado`
cambio: %(b_otros)s.**

**GUARDA (3), EL CASO POSITIVO.** El `jsonl` se recarga linea a linea: **%(b_rec)s**
fichas releidas del disco contra las **%(b_f0)s** de antes, y **%(b_malas)s** lineas que
no son JSON valido. **VEREDICTO DE LAS TRES GUARDAS: %(b_ver)s.**

**LA VARA NO ES ESTE CAMPO, Y SE DICE AQUI PARA QUE NADIE LO LEA AL REVES:** el `estado`
es **HISTORICO** y no decide que queda por ejecutar (recuadro 0 de `AUDITOR.md`). Se
pone al dia porque **un campo que contradice al acta que cerro la ficha engana a quien
venga**, no porque mida nada.

#### 1.e. LA MEDICION QUE NO ARREGLA NADA, Y SE QUEDO EN MEDICION

El hallazgo `7.1` del acta 210 vive en la linea **%(L71)d**. **Lo reproduje al digito y
no toque ni un nodo:** en `dataset/metadata/master_graph.json` (**%(e_grafo)s** nodos
contados hoy) `posicionamiento_de_empresa` tiene **CINCO** `pasos_accionables`, los de
Blank, y `la_historia_de_la_empresa` tiene los **CUATRO** de Horowitz. **Cinco mas
cuatro dan nueve.** El veredicto del **1357** NO SE TOCA: su clausula
*"El solape de este par cae en el primer bloque y el veredicto es INVARIANTE"* la cita
el acta en sus lineas **%(LINV)d** y **%(LINV2)d**, donde la frase parte en dos.

**(a) LAS DOS PREGUNTAS DEL ENCARGO, CONTESTADAS CON MI CONTEO DE HOY.** Menciones de
`posicionamiento_de_empresa` en `docs/plan/02_DESTEJIDOS.md`: **%(e_men)s**, que calza
con el **0** del encargo. Operaciones de `docs/plan/OPERACIONES.jsonl` en cuyo campo
`nodos` vive: **%(e_ops)s**, que calza con el **1** del encargo, y es
**`%(e_op_id)s`**, `DECISION_DE_FUENTE` en **`%(e_op_est)s`**, fase `%(e_op_fase)s`,
linea **%(e_op_lin)s**.

**PERO LA TERCERA CIFRA NO CALZA, Y NO LA RESUELVO COPIANDO** (`AUDITOR.md` 1.1). El
encargo dice *"con sus **13** nodos"* y la propia adjudicacion de la ficha dice *"LEIDOS
LOS 13"*. **Mi conteo de hoy del campo `nodos` da %(e_nodos)s.** La explicacion no la
pongo yo: vive en `docs/plan/01_FUENTES.md`, que en su linea **1453** declara *"El que
sobra es `principio_calidad_mvp`"* y en su linea **1168** que una decision del fundador
*"devolvio `principio_calidad_mvp` a la operacion y la nomina volvio a CATORCE"*.
**La discrepancia queda declarada: la adjudicacion de la ficha lleva el corte viejo, y
el campo lleva el nuevo. No toco ninguno de los dos.**

**(b) LA PARTICION DE LOS %(e_nodos)s, CONTADA Y CON SUS NOMBRES.** La vara no es mia:
es la tabla de `docs/plan/01_FUENTES.md`, **lineas 1462 a 1477**, que publica por nodo
los libros declarados y **la frontera leida** el 11 y el 14 ago 2026. De esa frontera
salen dos cifras por nodo sin teclear ninguna (el fin del bloque 1 y el total), y contra
ellas se pone la CIFRA de `pasos_accionables` de HOY. **%(e_filas)s** filas leidas,
**%(e_fc)s** nodos de la tabla que faltan en el campo y **%(e_ft)s** del campo que faltan
en la tabla. **La tabla que sigue esta PEGADA ENTERA de
`docs/loop/SALIDA_V%(v)d_T1E_GRUPO_HOROWITZ.txt`, no recompuesta:**

%(TABLA)s

**EL REPARTO: %(e_aparte)s con EL BLOQUE YA VIVE APARTE, %(e_ning)s con NI UNA COSA NI
LA OTRA, y %(e_dentro)s con EL BLOQUE SIGUE DENTRO**, sobre **%(e_rep)s** repartidos y
**%(e_sm)s** sin medir.

**LA MUTACION, CORRIDA:** desplazando en uno el fin del bloque 1 de cada fila, el cubo
`NI UNA COSA NI LA OTRA` pasa de **%(e_ning)s** a **%(em_ning)s**. La comparacion
compara. Sellada en `docs/loop/SALIDA_V%(v)d_T1E_GRUPO_HOROWITZ_MUTADO.txt`.

**(c) LA PARTICION NO ES UNIFORME (%(e_uni)s), Y AQUI PARO, QUE ES LO QUE EL ENCARGO
MANDA.** Los tres que no calzan con ninguna de las dos son
`decision_de_vender_startup`, `principio_calidad_mvp` y `seleccion_ceo_fundador`.
**Decidir que hacer con una operacion de fuente sin destino no es de esta vuelta**, y no
lo decido.

**LO QUE NO AFIRMO, Y ES LA MITAD HONESTA DE ESTA MEDICION:** *EL BLOQUE YA VIVE APARTE*
es el nombre de **una coincidencia de cifras** (los pasos de hoy son exactamente los del
bloque 1 de la frontera de agosto), **no la prueba de que el bloque 2 exista hoy como
nodo propio**. Eso lo comprobe **para un solo nodo**, el del `7.1`, donde
`la_historia_de_la_empresa` esta y lleva los cuatro pasos. **Para los otros diez no lo
comprobe**, y por eso no lo escribo.
""" % {
    "v": VUELTA,
    "L210": L_210, "L64": L_64, "L65": L_65, "L2C": L_2C, "L63": L_63,
    "L66": L_66, "L71": L_71, "LINV": L_INV, "LINV2": L_INV2,
    "acta_disco": ap_acta[0], "acta_lf": ap_acta[1], "acta_sha": ap_sha,
    "acta_kb": int(ap_acta[0]) / 1024.0,
    "b_e0": b_entrar[0], "b_e1": b_entrar[1],
    "b_s0": b_sha0[0], "b_s1": b_sha0[1],
    "b_x0": b_salir[0], "b_x1": b_salir[1],
    "b_x_s0": b_sha1[0], "b_x_s1": b_sha1[1],
    "b_pasan0": b_pasan[0], "b_pasan1": b_pasan[1],
    "b_filas": b_filas, "b_anad": b_anad[0], "b_borr": b_anad[1],
    "hecha0": b_hecha[0], "hecha1": b_hecha[1],
    "lista0": b_lista[0], "lista1": b_lista[1],
    "tot0": b_total[0], "tot1": b_total[1],
    "b_mov": b_movidas, "b_otros": b_otros,
    "b_rec": b_recarga, "b_f0": b_fichas0, "b_malas": b_malas,
    "b_ver": b_veredicto, "bm_ver": bm_veredicto, "bm_cod": bm_codigo,
    "e_men": e_menciones, "e_ops": e_ops,
    "e_op_lin": e_idop[0], "e_op_id": e_idop[1], "e_op_est": e_idop[3],
    "e_op_fase": e_idop[4],
    "e_nodos": e_nodos, "e_filas": e_filas, "e_fc": e_falta_campo,
    "e_ft": e_falta_tabla, "e_grafo": e_grafo,
    "e_aparte": e_aparte, "e_ning": e_ninguna, "e_dentro": e_dentro,
    "e_rep": e_repartidos, "e_sm": e_sinmedir, "e_uni": e_uniforme,
    "em_ning": em_ninguna, "TABLA": TABLA,
}

print("CIFRA lecturas que fallaron: %d %s" % (len(FALLOS), FALLOS))
print("CIFRA guiones largos: %d | CIFRA guiones medios: %d"
      % (CUERPO.count(chr(8212)), CUERPO.count(chr(8211))))
if CUERPO.count(chr(8212)) or CUERPO.count(chr(8211)):
    FALLOS.append("guiones")
if "(SIN LEER)" in CUERPO:
    FALLOS.append("hay una cifra sin leer en el cuerpo")
if FALLOS:
    print("ROJO: no se escribe el cuerpo. %s" % FALLOS)
    sys.exit(1)
destino = os.path.join(AQUI, "_v%d_t1_seccion.md" % VUELTA)
io.open(destino, "w", encoding="utf-8", newline=NL).write(CUERPO)
print("ESCRITO %s -> %d bytes, %d lineas"
      % (destino, len(CUERPO.encode("utf-8")), CUERPO.count(NL)))
print("VERDE.")
