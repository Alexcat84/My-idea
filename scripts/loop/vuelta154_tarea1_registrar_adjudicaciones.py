# -*- coding: utf-8 -*-
"""vuelta154_tarea1_registrar_adjudicaciones.py . TAREA 1 DE LA VUELTA 154.

DEJA ESCRITAS EN EL REPO LAS NUEVE ADJUDICACIONES DE LA SECCION 6 DEL ACTA 153,
CADA UNA DONDE VIVE, TODAS POR ADICION Y CON CORRECCION DECLARADA. No borra una
sola linea del texto viejo: cada bloque se ANADE al final del docstring o del
campo, con su fecha, su fuente citada y su motivo.

EL REPARTO, que es el que el encargo nombra:
  6.1 y 6.2  scripts/loop/vuelta150_3_relectura_expediente.py (el instrumento
             de la relectura del expediente: la vara P3 y la asimetria P2/P3)
  6.5        el mismo instrumento (el corte estricto, que es la regla de su
             propio --corte y por eso vive con el)
  6.3        docs/plan/OPERACIONES.jsonl, las cinco fichas OP-M-01..OP-M-05
  6.4 y 6.9  docs/plan/OPERACIONES.jsonl, ficha OP-C-05
  6.6        scripts/loop/vuelta150_4_tabla_por_fase.py (el arnes de la tabla)
  6.7        scripts/loop/verificar_apertura_sellada.py (la guarda del corredor)
  6.8        scripts/loop/verificar_cifras_del_reporte.py (la linea CIFRA)

ES IDEMPOTENTE: si el bloque ya esta escrito (se busca su marca literal), no lo
duplica y lo dice. Asi se puede re correr sin ensuciar el fichero.

USO:  python scripts/loop/vuelta154_tarea1_registrar_adjudicaciones.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

MARCA = "ADJUDICACION %s DEL ACTA 153"


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)


def insertar_en_docstring(ruta_rel, bloque, marca):
    """Inserta BLOQUE justo antes del cierre del docstring de modulo. El texto
    viejo no se toca: el bloque queda al final, detras de todo lo anterior."""
    ruta = os.path.join(RAIZ, ruta_rel)
    texto = leer(ruta)
    if marca in texto:
        return "YA ESTABA", 0
    ini = texto.index('"""')
    fin = texto.index('"""', ini + 3)
    nuevo = texto[:fin] + bloque + texto[fin:]
    escribir(ruta, nuevo)
    return "ANADIDO", len(bloque.splitlines())


def fichas():
    return [json.loads(x) for x in leer(OPS).splitlines() if x.strip()]


def guardar_fichas(F):
    with io.open(OPS, "w", encoding="utf-8", newline="\n") as fh:
        for f in F:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")


B61 = """
--- ADJUDICACION 6.1 DEL ACTA 153 (2 sep 2026): LA P3 DEJA DE CONTAR MENCIONES ---

CORRECCION DECLARADA. NADA DE LO ESCRITO ARRIBA SE BORRA: este bloque se anade
debajo y describe lo que cambia a partir de hoy.

LA VARA YA EXISTIA Y NO ES DOCTRINA NUEVA. Es el CRITERIO DE HECHO de
docs/plan/08_VERIFICACION.md: "UNA FASE ESTA HECHA CUANDO SU VERIFICACION SE
CAERIA SI EL FALLO VOLVIERA. No cuando pasa verde: cuando se CAERIA." Un commit
que NOMBRA una operacion no hace que ninguna verificacion se caiga.

LO QUE CAMBIA: la P3 pasa a contar SOLO commits que tocan `dataset/`, `web/` o
`engine/`. `scripts/` SALE de la lista de rutas. El ejemplar que lo obliga, y es
el que el acta manda usar como caso de mutacion: `c9c6ea40` (el commit que
publica que OP-V-01 y OP-L-01 NO tienen prueba) toca `docs/loop/` y
`scripts/loop/`, y con la vara vieja contaba como PRUEBA DE EJECUCION de esas
dos fichas por la sola ruta `scripts/`. Con la vara nueva deja de contar.

Y LA SEGUNDA VIA, escrita porque la adjudicacion la nombra: tambien cuenta "el
caso positivo de la ficha corriendo en rojo antes y en verde despues". Esa via
se mide aqui como P3b y su alcance esta declarado junto a la funcion que la
implementa: NO se re corre un caso positivo por ficha en cada corrida (serian 71
mutaciones por vuelta), se exige que la ficha CITE una salida de caso positivo o
de mutacion que EXISTA en el arbol del corte.

LO QUE ESTA LECTURA SUPONE Y SE DECLARA EN VEZ DE CALLARSE: la adjudicacion dice
"commits que tocan dataset/, web/ o engine/ EN LA NOMINA DE LA FICHA". Se lee
"la nomina de la ficha" como "el mensaje del commit nombra el id_op de la
ficha", que es la condicion que la P3 ya tenia y que la adjudicacion no toca.
Queda marcado como discutible en el reporte de la vuelta 154.
"""

B62 = """
--- ADJUDICACION 6.2 DEL ACTA 153 (2 sep 2026): LA ASIMETRIA P2 CONTRA P3 SE
QUEDA, Y SE ESCRIBE AQUI DENTRO PORQUE LA ADJUDICACION LO EXIGE ---

CORRECCION DECLARADA POR ADICION. La condicion literal del acta es que la
asimetria quede escrita DENTRO DEL INSTRUMENTO y no solo en el reporte, "para
que la lea quien venga detras". Esta es esa escritura.

LA ASIMETRIA: la P3 corre con el reloj de git CONGELADO en `--corte`, y la P2
NO se congela: lee el ARBOL DE TRABAJO de hoy.

POR QUE NO ES UNA INCOHERENCIA:
  - La P2 mide EXISTENCIA de un control en el codigo vivo. Existencia es un
    ESTADO, no una ejecucion, y el estado de hoy se mide en el arbol de hoy. Un
    control instalado hoy esta instalado, lo instalara quien lo instalara y el
    dia que fuera.
  - La P3 mide EJECUCION, o sea un ACTO fechado. Un acto que la propia vuelta
    acaba de cometer no puede ser la prueba de que la vuelta hizo el trabajo:
    ahi es donde la vara se cuenta a si misma, y por eso solo esta va congelada.

LO QUE LA ASIMETRIA CUESTA, DICHO EN VOZ ALTA: si la propia vuelta INSTALA el
id_op en `scripts/`, `engine/` o `web/lib/`, la P2 lo vera en la misma corrida.
Eso NO es la caida que el acta 151 hallo (aquella era la P3 comiendose su propio
papeleo), pero es su vecina, y por eso se nombra aqui en vez de esconderse.
"""

B65 = """
--- ADJUDICACION 6.5 DEL ACTA 153 (2 sep 2026): EL CORTE ES EL HEAD DE APERTURA,
EN ESTRICTO ---

CORRECCION DECLARADA POR ADICION, y la caida es del auditor, no de este
instrumento. El acta 151 congelo el reloj en `c9c6ea40~1` (`fb3c0c75`), que cae
DENTRO de la vuelta 150; la regla escrita en el bloque de arriba pide EL HEAD DE
APERTURA DE LA VUELTA, o sea el commit anterior al primero que la vuelta
escribe, que para la 150 era `fe98cf97`. El acta 153, seccion 2, tercer parrafo,
se lo concede entero al ejecutor y lo registra como caida de vara DEL AUDITOR.

NO CAMBIO UN DIGITO en aquella medicion (los dos cortes dan 58/13/30/67), pero
la vara laxa no se hereda: `--corte` es el HEAD DE APERTURA y no un ancestro
cualquiera cercano.
"""

B66 = """
--- ADJUDICACION 6.6 DEL ACTA 153 (2 sep 2026): LA FILA 03 FUSIONES, Y LOS DOS
DIVERGENTES DEJAN DE CONTAR COMO FALTA ---

CORRECCION DECLARADA POR ADICION. NADA DE LO ESCRITO ARRIBA SE BORRA.

LO QUE FALTABA NO ERA UNA MEDICION SINO UNA DECISION, y el acta 153 la toma:
"los dos divergentes que la CORRECCION 16 ya clasifica NO son un pendiente de la
fase 03. La celda pide un superviviente por acto con el resto deprecado y con
alias, y eso esta medido en 0 incumplimientos sobre 14 fichas. La fila 03 pasa a
VERDE en cuanto el arnes deje de contar los dos divergentes como falta, y eso es
un cambio de la celda, NO DEL GRAFO."

ES UN CAMBIO DE LA CELDA, NO DEL GRAFO, y esa frontera se vigila: si al correr
el arnes con esta adjudicacion aplicada se mueve una sola cifra del grafo, se
para. Ninguna linea de `dataset/` se toca por esto.
"""

B67 = """
--- ADJUDICACION 6.7 DEL ACTA 153 (2 sep 2026): EL CORREDOR ADMITE EL COMMIT DE
LA DECISION DEL FUNDADOR, Y LO NOMBRA APARTE ---

CORRECCION DECLARADA POR ADICION. NADA DEL TEXTO ANTERIOR SE BORRA.

EL CASO REAL QUE LA OBLIGA (vuelta 152): el corredor traia DOS commits, el del
ejecutor (`6f419952`) y `d9fa886b`, LA DECISION DEL FUNDADOR, que toca
`docs/loop/AUDITOR.md` y `docs/plan/OPERACIONES.jsonl` porque el encargo manda
aplicar las respuestas donde viven. La guarda fallaba por los dos por igual.

LO QUE EL ACTA ADJUDICA: `AUDITOR.md` seccion 4 trata la decision del fundador
como una CATEGORIA PROPIA, ajena al trabajo del bucle; un commit de decision NO
es el ejecutor tocando nada. El corredor ADMITE el commit de la decision del
fundador QUE `docs/loop/PROMPT_SIGUIENTE.md` CITA POR SU HASH, y la guarda lo
NOMBRA APARTE en vez de fallar por el.

Y LA MITAD QUE NO SE TOCA, dicha con todas sus letras: EL ROJO POR UN COMMIT DEL
PROPIO EJECUTOR DENTRO DEL CORREDOR SE QUEDA INTACTO. Esa mitad del rojo de la
vuelta 152 era legitima. La admision es por HASH CITADO EN EL ENCARGO, no por
autor adivinado ni por ruta: un hash que el encargo no cite no entra.
"""

B68 = """
--- ADJUDICACION 6.8 DEL ACTA 153 (2 sep 2026): LA LINEA CIFRA NO ERA DOCTRINA
PENDIENTE, ESTABA ESCRITA AQUI ---

REGISTRO POR ADICION, sin corregir nada: el contrato de abajo no cambia ni una
coma. Se escribe aqui porque la vuelta 152 lo trajo como PREGUNTA 3 ("cual es el
formato exacto de la linea CIFRA y donde va") y la respuesta estaba en este
mismo fichero, a una lectura de distancia.

EL CONTRATO, RE LEIDO Y CITADO POR SU LINEA:
  - FORMATO: `CIFRA <etiqueta>: <n> <unidad>`, con la unidad tomada del
    vocabulario CERRADO de `UNIDADES` (fichero(s), par(es), grupo(s), grafia(s),
    colapso(s), nodo(s), linea(s), arista(s), direccion(es), fila(s),
    comprobacion(es), operacion(es)). Ver el bloque "LA LINEA `CIFRA` (2.c)" del
    docstring y el patron `PATRON_CIFRA_ETIQUETA`.
  - DONDE VA: EN EL FICHERO DE SALIDA QUE LA CIFRA CITA, nunca en el reporte. La
    guarda la busca en el fichero citado y coteja contra ella.
  - LA LINEA EMPIEZA EN COLUMNA CERO: el patron es MULTILINE y anclado en `^`.
  - SE APLICA IGUAL A UN REPORTE DE FASE III: esta guarda no distingue fase.
"""

B63 = ("ADJUDICACION 6.3 DEL ACTA 153 (2026-09-02), REGISTRADA POR ADICION Y SIN "
       "BORRAR UNA LINEA DE LO ANTERIOR: el pase de estado de esta mesa QUEDA "
       "AUTORIZADO. La reserva del acta 139, 3.6 nombraba literalmente 'las once (las "
       "seis fusiones y las cinco remitidas)' y las cinco mesas NO estaban ahi, asi que "
       "el ejecutor de la vuelta 152 hizo bien en NO moverlas. Pero el disparador que "
       "esa misma 3.6 les puso es 'cuando la fase 06 cierre', y el acta 153, 6.3 lo "
       "mide disparado: la fase 06 sale VERDE, 5 de 5 mesas completas, con el arnes al "
       "corte 6f695db6. Las cinco pasan de estado EN UN SOLO ACTO, con el conteo antes "
       "y despues, el esquema intacto y la guarda de cifras del plan re corrida. NO ES "
       "DOCTRINA NUEVA: es el mismo acto de las vueltas 131, 136 y 152 con su "
       "disparador ya disparado.")

B64 = ("ADJUDICACION 6.4 DEL ACTA 153 (2026-09-02), REGISTRADA POR ADICION: LAS 121 "
       "LECTURAS DIRIGIDAS EN CLASE C QUEDAN SOSTENIDAS. El auditor releyo OCHO a "
       "ciegas (los cuatro marcados 008, 031, 042 y 059, mas cuatro elegidos por "
       "zancada fija fuera del marcado: 005, 020, 035 y 050), imprimiendo solo titulo y "
       "pasos accionables de los dos nodos, sin clase, sin via y sin razon, y "
       "adjudicando ANTES de destapar. OCHO PUESTOS, OCHO COINCIDEN, CERO DISCREPAN. El "
       "031 queda declarado como el mas tenso y la C se sostiene por el arreglo que la "
       "figura prescribe: fundirlos borraria el procedimiento de la compatibilidad con "
       "el socio antes de fundar, que el otro nodo no contiene.")

B69 = ("ADJUDICACION 6.9 DEL ACTA 153 (2026-09-02), REGISTRADA POR ADICION: NO SE ABRE "
       "UNA TERCERA VIA DE CITA. La verificacion 7 de esta ficha pide que CADA ENTRADA "
       "CITE SU LECTURA, y una lectura dirigida que cita la declaracion sellada de "
       "OP-E-04 cumple ese contrato entero. Abrir una via nueva contra la letra de la "
       "decision del fundador del 2 sep 2026 (que nombra DOS: el veredicto del cribado "
       "y la declaracion sellada de P.10, mas la lectura dirigida por P.5 para lo que "
       "esas dos no cubran) seria doctrina nueva sin necesidad. LAS VIAS SIGUEN SIENDO "
       "LAS QUE LA DECISION NOMBRA.")


def main():
    print("=" * 78)
    print("VUELTA 154, TAREA 1: LAS NUEVE ADJUDICACIONES DE LA SECCION 6 DEL ACTA 153,")
    print("ESCRITAS DONDE CADA UNA VIVE, TODAS POR ADICION.")
    print("=" * 78)
    print("")

    hechas = 0
    docs = [
        ("6.1", "scripts/loop/vuelta150_3_relectura_expediente.py", B61),
        ("6.2", "scripts/loop/vuelta150_3_relectura_expediente.py", B62),
        ("6.5", "scripts/loop/vuelta150_3_relectura_expediente.py", B65),
        ("6.6", "scripts/loop/vuelta150_4_tabla_por_fase.py", B66),
        ("6.7", "scripts/loop/verificar_apertura_sellada.py", B67),
        ("6.8", "scripts/loop/verificar_cifras_del_reporte.py", B68),
    ]
    for num, ruta, bloque in docs:
        estado, n = insertar_en_docstring(ruta, bloque, MARCA % num)
        print("  %s  %-58s %s (%d lineas)" % (num, ruta, estado, n))
        if estado == "ANADIDO":
            hechas += 1

    F = fichas()
    print("")
    print("FICHAS EN docs/plan/OPERACIONES.jsonl ANTES: %d" % len(F))
    claves_antes = sorted({k for f in F for k in f})
    mesas = ["OP-M-01", "OP-M-02", "OP-M-03", "OP-M-04", "OP-M-05"]
    for f in F:
        i = f["id_op"]
        if i in mesas and (MARCA % "6.3") not in (f.get("nota") or ""):
            f["nota"] = ((f.get("nota") or "") + " " + B63).strip()
            print("  6.3  %-12s nota ampliada (+%d caracteres)" % (i, len(B63)))
            hechas += 1
        if i == "OP-C-05":
            for num, bloque in (("6.4", B64), ("6.9", B69)):
                if (MARCA % num) not in (f.get("nota") or ""):
                    f["nota"] = ((f.get("nota") or "") + " " + bloque).strip()
                    print("  %s  %-12s nota ampliada (+%d caracteres)"
                          % (num, i, len(bloque)))
                    hechas += 1
    guardar_fichas(F)
    G = fichas()
    claves_despues = sorted({k for f in G for k in f})
    print("FICHAS EN docs/plan/OPERACIONES.jsonl DESPUES: %d" % len(G))
    print("ESQUEMA: claves antes %d, claves despues %d, IGUALES: %s"
          % (len(claves_antes), len(claves_despues), claves_antes == claves_despues))
    assert len(F) == len(G) == 71, "el numero de fichas se movio"
    assert claves_antes == claves_despues, "el esquema se movio"
    estados_antes = [f["estado"] for f in F]
    estados_despues = [g["estado"] for g in G]
    print("ESTADOS: ninguno se mueve en esta tarea. IGUALES: %s"
          % (estados_antes == estados_despues))
    assert estados_antes == estados_despues, "esta tarea NO mueve estados"

    print("")
    print("CIFRA adjudicaciones escritas: %d operaciones" % hechas)
    print("CIFRA fichas del expediente: %d operaciones" % len(G))
    print("")
    print("NADA SE BORRA: los seis bloques de docstring se insertan al FINAL del")
    print("docstring, y las tres notas de ficha se CONCATENAN detras del texto viejo.")


main()
