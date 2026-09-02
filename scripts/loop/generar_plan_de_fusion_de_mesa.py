# -*- coding: utf-8 -*-
"""generar_plan_de_fusion_de_mesa.py . SELLA EL PLAN DE UNA FUSION DE MESA
LEYENDO LA OPERACION DE docs/plan/OPERACIONES.jsonl.

NOMBRE ESTABLE, y no lleva vuelta ni operacion: las dos entran por argumento
(--vuelta, --id-op) y el contenido editorial por --contenido. Es la vara del
acta 58, pregunta 4.

HERMANO de scripts/loop/generar_plan_del_lote.py, NO sucesor: aquel sella lotes
de un TRAMO de OP-U-01 y lee su insumo de un fichero de tramo; este sella UNA
FUSION DE MESA y lee su insumo de la FICHA DE LA OPERACION. LA MAQUINA DE LAS
GUARDAS NO SE RETECLEA NI SE COPIA: se IMPORTA de aquel (puertas,
extraer_verbatim, el contrato y sus tres especies), para que el que sella un lote
y el que sella una mesa no puedan discrepar en silencio.

LA CABECERA SE ARMA DE LA FICHA, NUNCA DE UN LITERAL. Nombre de la operacion,
nodos, superviviente, absorbidos, adjudicacion, verificacion, evidencia, notas y
dependencias salen del jsonl y se copian VERBATIM al plan. Este fichero no sabe
nada de ninguna operacion concreta, y por eso no puede envejecer: es la leccion
del censo de plantillas de la vuelta 63.

LAS GUARDAS AL SELLAR, todas las del hermano:
  - el superviviente y los absorbidos que el plan usa TIENEN que ser los que la
    ficha escribe, y si no lo son es ROJO y no se escribe nada;
  - GUARDA 1B: ningun absorbido es semilla de entrada ni extremo de puente;
  - los dos miembros VIVOS y no deprecados;
  - COBERTURA EXACTA: cada paso y cada condicion de cada absorbido con marca
    UNICA, ni una de menos ni una de mas;
  - el INCISO se EXTRAE del nodo y se comprueba VERBATIM, con su juntura;
  - las PERDIDAS se validan al sellar: especie fuera de las tres escritas o
    clave que falta es ROJO;
  - el campo perdidas va SIEMPRE, aunque vacio (contrato CAMPO PROPIO v1).

DE ESCRITURA SOLO SOBRE docs/loop/PLAN_V<N>_*.json. No toca ni un nodo.

--- EL REPARTO SE INDEXA POR EL PAR (VUELTA 138, OPERACION 2.a) ---

CORRECCION DECLARADA, y el texto viejo de arriba se queda entero porque una
correccion que tapa lo que corrige no se puede auditar. Hasta esta vuelta, la
linea "COBERTURA EXACTA: cada paso y cada condicion de cada absorbido con marca
UNICA" era verdad SOLO con un absorbido: `marcar(spec["pasos"], ...)` corria
dentro de `for ab in absorbidos` con el MISMO `spec` cada vez, y `spec["pasos"]`
se indexaba por NUMERO DE PASO, nunca por el par, asi que el paso 1 de dos
absorbidos distintos leia LA MISMA marca.

NO ES UNA REGRESION, ES UN CAMINO QUE ESTRENA. Los TRES usos historicos del
generador (OP-M-02-PROG y OP-M-03-I en la vuelta 63, OP-M-03-II en la vuelta 64)
tienen EXACTAMENTE UN absorbido cada uno: el camino de dos o mas nunca habia
corrido. La fase 06 lo estrena con cinco de sus seis mesas.

LO QUE CAMBIA, en reparto_por_par():
  - el reparto acepta el FORMATO POR PAR, {"<absorbido>": {"1": marca, ...}};
  - el FORMATO VIEJO plano, {"1": marca, ...}, SIGUE VALIENDO con un unico
    absorbido, y por eso los tres planes sellados se regeneran IDENTICOS;
  - el FORMATO VIEJO con dos o mas absorbidos es ROJO y el ROJO los nombra:
    no se acepta en silencio compartiendo marcas;
  - la marca que falta cae ROJO NOMBRANDO EL PAR, no solo el numero;
  - --reparto-viejo EXHIBE el defecto (reparte el dict plano a todos los
    absorbidos e imprime las colisiones) y nunca escribe.

--- LA QUINTA MARCA: VIAJA_EN_EL_ACTO (VUELTA 139, OPERACION 2.a) ---

CORRECCION DECLARADA POR ADICION, y el texto de arriba se queda entero.

POR QUE NACE, y NO ES DOCTRINA NUEVA. La vuelta 138 se detuvo ante una pieza
que DOS O MAS absorbidos del mismo acto tienen y el superviviente NO, porque
ninguna de las cuatro marcas del contrato la sostenia: `CUBIERTO` afirma del
superviviente algo que su texto no dice, el doble `APPEND` fabrica la
repeticion que `P.13` prohibe por su nombre ("obliga a injertar en el
superviviente algo que ya esta, y eso es como se fabrica una repeticion nueva
el dia de la pasada"), y declararla PERDIDA es lo que `P.13` llama PERDIDA
FALSA, ademas de no caber en ESPECIES_DE_PERDIDA. El acta de la vuelta 138,
adjudicacion 3.1, lo cerro citando `P.13`: lo que faltaba NO era doctrina,
era VOCABULARIO DEL INSTRUMENTO, el mismo carril que la 3.4 del acta 137.

QUE DICE LA MARCA, exactamente y nada mas:
    VIAJA_EN_EL_ACTO:<absorbido>|<n>
    "esta pieza ya viaja en este mismo acto, por el paso n del absorbido
     <absorbido>"
NO afirma nada del texto del superviviente, que es lo que hacia insostenible a
CUBIERTO, y NO es una perdida, que es lo que `P.13` llama perdida falsa. Es
`VIVE DENTRO` de `P.13` ("se tacha de la lista y SE ANOTA DONDE VIVE")
aplicado al superviviente DESPUES de la fusion en vez de antes.

QUE REDACCION VIAJA, fijado por el auditor y no decidido aqui: LA DEL ABSORBIDO
CUYO PASO LLEVA EL APPEND. Si el segundo dueno trae un MATIZ que el primero no
trae, ESE MATIZ NO ES VIAJA_EN_EL_ACTO: es una pieza propia y viaja con su
propia marca, por `P.13`. La casa ya escribe asi (ficha de OP-M-05-APERTURA,
"VIAJA SOLO EL MATIZ").

LAS SEIS GUARDAS AL SELLAR, todas ROJO y sin escribir nada si fallan:
  (i)   el destino (absorbido, n) EXISTE en la misma operacion: el absorbido
        esta en `absorbidos` y n esta entre sus pasos. ROJO NOMBRANDO LOS DOS.
  (ii)  el destino LLEVA UNA MARCA QUE HACE VIAJAR LA PIEZA, o sea APPEND o
        INCISO. Si lleva CUBIERTO, CUBIERTO_COND u otro VIAJA_EN_EL_ACTO, es
        ROJO con la letra "cadena que no llega a viajar", nombrando el par.
        NO HAY CADENAS: el destino viaja directo o es rojo.
  (iii) la auto referencia (el mismo absorbido y el mismo n) es ROJO.
  (iv)  COBERTURA EXACTA sigue mandando, indexada por el par (2.a de la 138).
  (v)   cada VIAJA_EN_EL_ACTO lleva EN EL PLAN una linea editorial, copiada
        VERBATIM del contenido, en `lineas_de_viaje`, indexada por el par
        ORIGEN "<absorbido>|<n>". Sin esa linea, ROJO. La linea tiene ademas
        que NOMBRAR AL ABSORBIDO DESTINO, que es la parte de "CUAL de las dos
        redacciones viaja" que una maquina puede comprobar.
  (vi)  el REPARTO impreso cuenta la marca nueva junto a APPEND, CUBIERTO e
        INCISO, y la cifra es COMPUTADA de las marcas, no un literal.

SOLO PARA PASOS, como el INCISO. Una condicion marcada VIAJA_EN_EL_ACTO es
ROJO: la marca nombra "el paso n" del absorbido destino, y el destino de una
condicion no esta definido por ninguna regla escrita. Cuando haga falta, se
adjudica; hoy no se inventa.

Uso:
  python scripts/loop/generar_plan_de_fusion_de_mesa.py --vuelta 63
      --id-op OP-M-03-I --contenido _v63_opm03i [--simular]
"""
import argparse
import datetime
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop")
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
NL = chr(10)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generar_plan_del_lote import (  # noqa: E402
    CONTRATO_DE_PERDIDAS, CLAVES_DE_PERDIDA, ESPECIES_DE_PERDIDA,
    extraer_verbatim, puertas,
)


def ficha(id_op):
    for l in io.open(OPERACIONES, encoding="utf-8"):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get("id_op") == id_op:
            return d
    return None


def marcar(spec_marcas, textos, etq, ab, n_sup_pasos, n_sup_cond, pasos_sup, fallos,
           permite_cond):
    """Traduce las marcas editoriales a las del contrato del ejecutor. Devuelve el
    dict de marcas. Es la MISMA aritmetica que el hermano de los lotes, y las
    mismas cuatro marcas: APPEND, CUBIERTO:n, CUBIERTO_COND:n e INCISO:n|trozo|nexo."""
    marcas = {}
    for i, texto in enumerate(textos, 1):
        m = spec_marcas.get(str(i))
        if not m:
            fallos.append("el %s %d de %s no tiene marca: FALTA EL PAR (%s, %d)"
                          % (etq, i, ab, ab, i))
            continue
        if m[0] == "APPEND":
            marcas[str(i)] = "APPEND"
        elif m[0] == "CUBIERTO":
            tope = n_sup_cond if etq == "condicion" else n_sup_pasos
            if not (1 <= m[1] <= tope):
                fallos.append("%s %d: CUBIERTO:%d y el superviviente tiene %d"
                              % (etq, i, m[1], tope))
            marcas[str(i)] = "CUBIERTO:%d" % m[1]
        elif m[0] == "CUBIERTO_COND":
            if not permite_cond:
                fallos.append("%s %d: CUBIERTO_COND no vale para una condicion" % (etq, i))
            if not (1 <= m[1] <= n_sup_cond):
                fallos.append("%s %d: CUBIERTO_COND:%d y el superviviente tiene %d condiciones"
                              % (etq, i, m[1], n_sup_cond))
            marcas[str(i)] = "CUBIERTO_COND:%d" % m[1]
        elif m[0] == "INCISO":
            if etq == "condicion":
                fallos.append("condicion %d: el INCISO de condiciones NO existe todavia "
                              "(acta 55, pregunta 5)" % i)
                continue
            _, k, ascii_trozo, nexo = m
            trozo, motivo = extraer_verbatim(texto, ascii_trozo)
            if trozo is None:
                fallos.append("%s %d de %s: INCISO %r, %s" % (etq, i, ab, ascii_trozo, motivo))
                continue
            if "|" in trozo or "|" in nexo:
                fallos.append("%s %d: el INCISO o su nexo llevan la barra vertical, que es el "
                              "separador de la marca" % (etq, i))
            if not (1 <= k <= n_sup_pasos):
                fallos.append("%s %d: INCISO al paso %d y el superviviente tiene %d"
                              % (etq, i, k, n_sup_pasos))
            else:
                resultante = pasos_sup[k - 1] + nexo + trozo
                if (pasos_sup[k - 1].rstrip().endswith((".", "!", "?"))
                        and nexo.lstrip().startswith((",", ";"))):
                    fallos.append("%s %d de %s: JUNTURA ROTA, el paso del superviviente acaba "
                                  "en punto y el nexo abre con coma: %r"
                                  % (etq, i, ab, resultante[-90:]))
                print("  INCISO al paso %d del superviviente" % k)
                print("      trozo pedido en ASCII  : %r" % ascii_trozo)
                print("      trozo EXTRAIDO del nodo: %r" % trozo)
                print("      paso resultante        : %s" % resultante)
            marcas[str(i)] = "INCISO:%d|%s|%s" % (k, trozo, nexo)
        elif m[0] == "VIAJA_EN_EL_ACTO":
            # LA QUINTA MARCA (vuelta 139, 2.a). Aqui solo se comprueba lo que
            # se puede ver con UN absorbido delante: la forma, la especie y la
            # AUTO REFERENCIA (guarda iii). Las guardas (i), (ii) y (v) miran
            # los otros absorbidos del acto y viven en
            # validar_viaja_en_el_acto(), que corre cuando ya estan todos
            # marcados. Se parte a proposito: una guarda que necesita el acto
            # entero no puede fingir que le basta un absorbido.
            if etq == "condicion":
                fallos.append("condicion %d de %s: VIAJA_EN_EL_ACTO NO vale para una "
                              "condicion: la marca nombra EL PASO n del absorbido destino, y "
                              "el destino de una condicion no lo escribe ninguna regla. "
                              "Cuando haga falta se adjudica; aqui no se inventa" % (i, ab))
                continue
            if len(m) != 3:
                fallos.append("paso %d de %s: VIAJA_EN_EL_ACTO mal formada %r: se escribe "
                              "['VIAJA_EN_EL_ACTO', '<absorbido destino>', <n>]" % (i, ab, m))
                continue
            _, ab_destino, n_destino = m
            if not isinstance(n_destino, int):
                fallos.append("paso %d de %s: VIAJA_EN_EL_ACTO con numero de paso %r, que no "
                              "es un entero" % (i, ab, n_destino))
                continue
            if "|" in str(ab_destino):
                fallos.append("paso %d de %s: el absorbido destino %r lleva la barra vertical, "
                              "que es el separador de la marca" % (i, ab, ab_destino))
                continue
            # GUARDA (iii), AUTO REFERENCIA: el mismo absorbido y el mismo paso.
            if ab_destino == ab and n_destino == i:
                fallos.append("paso %d de %s: VIAJA_EN_EL_ACTO AUTO REFERENTE, se apunta a si "
                              "mismo (%s, %d). Una pieza no puede viajar por su propio paso"
                              % (i, ab, ab, i))
                continue
            marcas[str(i)] = "VIAJA_EN_EL_ACTO:%s|%d" % (ab_destino, n_destino)
        else:
            fallos.append("%s %d: marca desconocida %r" % (etq, i, m))
    sobra = set(spec_marcas) - {str(i) for i in range(1, len(textos) + 1)}
    if sobra:
        fallos.append("marcas de %s que sobran para el absorbido %s: %s"
                      % (etq, ab, sorted(sobra)))
    return marcas


def viaja_a(marca):
    """Devuelve (absorbido_destino, n_destino) si la marca es VIAJA_EN_EL_ACTO,
    y None si no lo es. UNA sola forma de leer la marca, para que el generador y
    el fundidor no puedan discrepar en silencio sobre como se parte."""
    if not isinstance(marca, str) or not marca.startswith("VIAJA_EN_EL_ACTO:"):
        return None
    resto = marca[len("VIAJA_EN_EL_ACTO:"):]
    if "|" not in resto:
        return None
    ab, num = resto.rsplit("|", 1)
    if not num.isdigit():
        return None
    return ab, int(num)


def validar_viaja_en_el_acto(marcas_p, absorbidos, pasos_por_ab, lineas, fallos):
    """LAS GUARDAS (i), (ii) Y (v) DE LA QUINTA MARCA (vuelta 139, 2.a).

    Corre cuando TODOS los absorbidos ya estan marcados, porque las tres miran
    fuera del absorbido que lleva la marca:

      (i)  el destino (absorbido, n) EXISTE en la misma operacion. ROJO
           NOMBRANDO LOS DOS, el absorbido y el numero.
      (ii) el destino LLEVA UNA MARCA QUE HACE VIAJAR LA PIEZA (APPEND o
           INCISO). Si lleva CUBIERTO, CUBIERTO_COND u otro VIAJA_EN_EL_ACTO,
           es ROJO con la letra "cadena que no llega a viajar", nombrando el
           par. NO HAY CADENAS: el destino viaja directo o es rojo.
      (v)  cada VIAJA_EN_EL_ACTO lleva su linea editorial en `lineas_de_viaje`,
           indexada por el par ORIGEN "<absorbido>|<n>", no vacia, y que NOMBRE
           AL ABSORBIDO DESTINO (la parte comprobable de "cual de las dos
           redacciones viaja": viaja la del destino, que es la que lleva el
           APPEND, fijado por el auditor en el encargo de la 139).

    Devuelve la lista de (ab_origen, n_origen, ab_destino, n_destino), que es
    una cifra COMPUTADA de las marcas y no un literal.
    """
    hallados = []
    for ab in absorbidos:
        for num, marca in sorted((marcas_p.get(ab) or {}).items(), key=lambda x: int(x[0])):
            destino = viaja_a(marca)
            if destino is None:
                continue
            ab_d, n_d = destino
            i = int(num)
            hallados.append((ab, i, ab_d, n_d))

            # (i) EL DESTINO EXISTE, y el ROJO nombra los dos.
            if ab_d not in absorbidos:
                fallos.append(
                    "paso %d de %s: VIAJA_EN_EL_ACTO al absorbido %r y el paso %d, y el "
                    "absorbido %r NO esta en esta operacion (los absorbidos son: %s)"
                    % (i, ab, ab_d, n_d, ab_d, ", ".join(absorbidos)))
                continue
            n_pasos_destino = len(pasos_por_ab.get(ab_d) or [])
            if not (1 <= n_d <= n_pasos_destino):
                fallos.append(
                    "paso %d de %s: VIAJA_EN_EL_ACTO al absorbido %s y el paso %d, y %s "
                    "tiene %d paso(s): ese paso NO existe"
                    % (i, ab, ab_d, n_d, ab_d, n_pasos_destino))
                continue

            # (ii) EL DESTINO VIAJA DE VERDAD. Cero cadenas.
            marca_destino = (marcas_p.get(ab_d) or {}).get(str(n_d))
            if marca_destino is None:
                fallos.append(
                    "paso %d de %s: VIAJA_EN_EL_ACTO al par (%s, %d), que no tiene marca"
                    % (i, ab, ab_d, n_d))
                continue
            if not (marca_destino == "APPEND" or marca_destino.startswith("INCISO:")):
                fallos.append(
                    "paso %d de %s: CADENA QUE NO LLEGA A VIAJAR. Apunta al par (%s, %d), "
                    "cuya marca es %r, y solo APPEND o INCISO hacen viajar la pieza"
                    % (i, ab, ab_d, n_d, marca_destino))

            # (v) LA LINEA EDITORIAL, indexada por el par ORIGEN.
            clave = "%s|%d" % (ab, i)
            linea = (lineas or {}).get(clave)
            if not isinstance(linea, str) or not linea.strip():
                fallos.append(
                    "paso %d de %s: VIAJA_EN_EL_ACTO SIN LINEA EDITORIAL. Falta la clave %r "
                    "en lineas_de_viaje, que dice POR QUE los dos son el mismo gesto y CUAL "
                    "de las dos redacciones viaja" % (i, ab, clave))
            elif ab_d not in linea:
                fallos.append(
                    "paso %d de %s: la linea editorial de %r no NOMBRA al absorbido destino "
                    "%s, asi que no dice cual de las dos redacciones viaja: %r"
                    % (i, ab, clave, ab_d, linea))

    sobran = sorted(set((lineas or {}).keys()) - {"%s|%d" % (a_, i_) for a_, i_, _, _ in hallados})
    if sobran:
        fallos.append("lineas_de_viaje trae claves que no corresponden a ningun "
                      "VIAJA_EN_EL_ACTO: %s" % ", ".join(repr(x) for x in sobran))
    return hallados


def reparto_por_par(spec, clave, absorbidos, fallos, forzar_viejo=False):
    """EL REPARTO SE INDEXA POR EL PAR (absorbido, numero de paso).

    OPERACION 2.a DE LA VUELTA 138, adjudicada en el acta de la vuelta 137,
    seccion 3.4, como OPERACION DE CODIGO BLOQUEANTE. EL DEFECTO, probado por
    los dos lados: `marcar(spec["pasos"], ...)` se llamaba dentro de
    `for ab in absorbidos` con el MISMO `spec` cada vez, y `spec["pasos"]` se
    indexaba por NUMERO DE PASO, nunca por el par; el paso 1 de dos absorbidos
    distintos leia LA MISMA marca. Los TRES usos historicos del generador
    (OP-M-02-PROG y OP-M-03-I en la vuelta 63, OP-M-03-II en la vuelta 64)
    tienen EXACTAMENTE UN absorbido cada uno, asi que el camino de dos o mas
    NO HA CORRIDO NUNCA: esto no repara una regresion, estrena un camino.

    LOS DOS FORMATOS QUE SE ACEPTAN, y por que los dos:

      FORMATO VIEJO (plano, indexado por numero de paso):
          {"1": [...], "2": [...]}
      VALE SOLO SI LA OPERACION TIENE UN UNICO ABSORBIDO, que es el caso de
      los tres planes ya sellados. Con dos o mas es ROJO, y el ROJO nombra los
      absorbidos: no se acepta en silencio compartiendo marcas, porque eso es
      exactamente el defecto que esta funcion repara (banco 9, fallar ruidoso).

      FORMATO POR PAR (indexado por absorbido y dentro por numero de paso):
          {"absorbido_a": {"1": [...]}, "absorbido_b": {"1": [...]}}
      Es el unico que vale con dos o mas absorbidos, y tambien vale con uno.

    EL DICT VACIO no es ambiguo y no se trata como formato: `{}` significa que
    NINGUN absorbido trae piezas de esa especie (lo normal en `condiciones`
    cuando ningun absorbido tiene condiciones), y se expande a `{}` por
    absorbido.

    `forzar_viejo` es la bandera de exhibicion (--reparto-viejo, guarda (iv)
    del encargo): reparte el dict PLANO a TODOS los absorbidos, que es
    literalmente lo que hacia el codigo viejo, para que el defecto se pueda
    ENSENAR y no solo contar. Una reparacion que no puede exhibir el defecto
    que repara no se puede auditar.

    Devuelve (por_absorbido, nombre_del_formato).
    """
    bruto = spec.get(clave)
    if bruto is None:
        fallos.append("el contenido no trae la clave %r del reparto" % clave)
        return {ab: {} for ab in absorbidos}, "AUSENTE"
    if not isinstance(bruto, dict):
        fallos.append("el reparto de %s no es un dict sino %s" % (clave, type(bruto).__name__))
        return {ab: {} for ab in absorbidos}, "NO ES DICT"

    claves = list(bruto.keys())
    if not claves:
        return {ab: {} for ab in absorbidos}, "VACIO"

    son_numeros = [k for k in claves if str(k).isdigit()]
    son_absorbidos = [k for k in claves if k in absorbidos]

    if len(son_numeros) == len(claves):
        # FORMATO VIEJO, plano.
        if forzar_viejo:
            return {ab: bruto for ab in absorbidos}, "VIEJO FORZADO (EXHIBICION)"
        if len(absorbidos) != 1:
            fallos.append(
                "el reparto de %s viene en FORMATO VIEJO (indexado por numero de paso) y la "
                "operacion tiene %d absorbidos (%s): con dos o mas, el mismo numero de paso de "
                "absorbidos distintos leeria LA MISMA marca. Indexa por el par "
                "(absorbido, numero de paso)." % (clave, len(absorbidos), ", ".join(absorbidos)))
            return {ab: {} for ab in absorbidos}, "VIEJO EN ROJO"
        return {absorbidos[0]: bruto}, "VIEJO (un solo absorbido)"

    if len(son_absorbidos) == len(claves):
        # FORMATO POR PAR.
        faltan = [ab for ab in absorbidos if ab not in bruto]
        if faltan:
            fallos.append("el reparto de %s no trae entrada para los absorbidos %s"
                          % (clave, ", ".join(faltan)))
        por_ab = {}
        for ab in absorbidos:
            sub = bruto.get(ab)
            if sub is None:
                por_ab[ab] = {}
                continue
            if not isinstance(sub, dict):
                fallos.append("el reparto de %s del absorbido %s no es un dict sino %s"
                              % (clave, ab, type(sub).__name__))
                por_ab[ab] = {}
                continue
            no_numeros = [k for k in sub if not str(k).isdigit()]
            if no_numeros:
                fallos.append("el reparto de %s del absorbido %s tiene claves que no son numero "
                              "de paso: %s" % (clave, ab, ", ".join(sorted(no_numeros))))
            por_ab[ab] = sub
        return por_ab, "POR PAR (absorbido, numero de paso)"

    # NI UNA COSA NI LA OTRA: se nombran las claves que no encajan, sin resumir.
    sueltas = [k for k in claves if not str(k).isdigit() and k not in absorbidos]
    fallos.append(
        "el reparto de %s mezcla formatos o trae claves desconocidas: %d clave(s) de numero de "
        "paso, %d clave(s) de absorbido, y estas no son ninguna de las dos: %s"
        % (clave, len(son_numeros), len(son_absorbidos), ", ".join(repr(k) for k in sorted(sueltas))))
    return {ab: {} for ab in absorbidos}, "MEZCLADO EN ROJO"


def exhibir_reparto(marcas_p, marcas_c, absorbidos):
    """GUARDA (iv) DEL ENCARGO DE LA VUELTA 138: el fallo viejo queda EXHIBIBLE.

    Imprime la tabla (absorbido, numero de paso) -> marca y CUENTA las
    colisiones, es decir los numeros de paso en los que dos absorbidos
    distintos reciben la MISMA marca. Devuelve el numero de colisiones, que es
    una cifra COMPUTADA de las marcas y no un literal: es la variable sobre la
    que muerde la prueba de mutacion.
    """
    colisiones = 0
    for etq, d in (("paso", marcas_p), ("condicion", marcas_c)):
        numeros = sorted({n for ab in absorbidos for n in (d.get(ab) or {})},
                         key=lambda x: int(x))
        for n in numeros:
            valores = [(ab, (d.get(ab) or {}).get(n)) for ab in absorbidos]
            presentes = [(ab, v) for ab, v in valores if v is not None]
            iguales = len({v for _, v in presentes}) == 1 and len(presentes) > 1
            if iguales:
                colisiones += 1
            for ab, v in presentes:
                print("     %-9s %-3s %-46s %s%s" % (etq, n, ab[:46], v,
                                                     "   <== COLISION" if iguales else ""))
    return colisiones


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, required=True)
    ap.add_argument("--id-op", dest="id_op", required=True)
    ap.add_argument("--contenido", required=True,
                    help="modulo del contenido editorial, con la constante FUSION")
    ap.add_argument("--prefijo", default=None,
                    help="prefijo del plan; por defecto PLAN_V<vuelta>_")
    ap.add_argument("--simular", action="store_true")
    ap.add_argument("--reparto-viejo", dest="reparto_viejo", action="store_true",
                    help="EXHIBE el defecto reparado en la vuelta 138: reparte el dict "
                         "PLANO de marcas a TODOS los absorbidos, como hacia el codigo "
                         "viejo, e imprime la tabla (absorbido, paso) con sus COLISIONES. "
                         "NUNCA escribe el plan.")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    op = ficha(a.id_op)
    if op is None:
        print("ROJO: %s no esta en docs/plan/OPERACIONES.jsonl. PARADA." % a.id_op)
        return 1
    mod = __import__(a.contenido)
    spec = getattr(mod, "FUSION", None)
    if spec is None:
        print("ROJO: el modulo %s no trae la constante FUSION. PARADA." % a.contenido)
        return 1

    print("=" * 78)
    print("GENERADOR DEL PLAN DE LA FUSION DE MESA %s (vuelta %d)" % (a.id_op, a.vuelta))
    print("  ficha leida de: docs/plan/OPERACIONES.jsonl")
    print("  tipo: %s | estado: %s | fecha de corte: %s"
          % (op.get("tipo"), op.get("estado"), op.get("fecha_corte")))
    print("=" * 78)
    print()

    fallos = []
    if op.get("estado") != "LISTA":
        fallos.append("la ficha dice estado %r y no LISTA" % op.get("estado"))
    sup = op.get("superviviente")
    absorbidos = list(op.get("eliminar") or [])
    miembros = list(op.get("nodos") or [])
    print("  LA FICHA MANDA, y esto es lo que dice:")
    print("     nodos         : %s" % ", ".join(miembros))
    print("     superviviente : %s" % sup)
    print("     eliminar      : %s" % ", ".join(absorbidos))
    if spec.get("superviviente") != sup:
        fallos.append("el contenido dice superviviente %r y la ficha dice %r"
                      % (spec.get("superviviente"), sup))
    if sorted(spec.get("absorbidos") or []) != sorted(absorbidos):
        fallos.append("el contenido dice absorbidos %r y la ficha dice %r"
                      % (spec.get("absorbidos"), absorbidos))
    if sorted(miembros) != sorted([sup] + absorbidos):
        fallos.append("nodos no calza con superviviente mas eliminar")

    prot = puertas()
    for x in absorbidos:
        if x in prot:
            fallos.append("GUARDA 1B EN ROJO: el absorbido %s es semilla o extremo de puente" % x)
    print("     guarda 1B, ningun absorbido es puerta: %s"
          % ("ROJO" if any(x in prot for x in absorbidos) else "OK"))

    nodos = {}
    for x in [sup] + absorbidos:
        p = os.path.join(NODOS, x + ".json")
        if not os.path.exists(p):
            fallos.append("el nodo %s no existe en el catalogo" % x)
            continue
        nodos[x] = json.load(io.open(p, encoding="utf-8"))
        if nodos[x].get("deprecado") or nodos[x].get("deprecated"):
            fallos.append("el nodo %s YA esta deprecado" % x)
    print("     los %d miembros vivos y presentes: %s"
          % (len(miembros), "OK" if len(nodos) == len(miembros) and not fallos else "ver fallos"))
    if fallos:
        print()
        print("ROJO, %d fallo(s) y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    pasos_sup = list(nodos[sup].get("pasos_accionables") or [])
    cond_sup = list(nodos[sup].get("condiciones_activacion") or [])
    print()
    print("  EL SUPERVIVIENTE DE HOY: %d pasos y %d condiciones" % (len(pasos_sup), len(cond_sup)))

    # EL REPARTO SE INDEXA POR EL PAR (absorbido, numero de paso), vuelta 138, 2.a.
    spec_p, formato_p = reparto_por_par(spec, "pasos", absorbidos, fallos,
                                        forzar_viejo=a.reparto_viejo)
    spec_c, formato_c = reparto_por_par(spec, "condiciones", absorbidos, fallos,
                                        forzar_viejo=a.reparto_viejo)
    print("  FORMATO DEL REPARTO: pasos %s | condiciones %s" % (formato_p, formato_c))
    marcas_p, marcas_c = {}, {}
    pasos_por_ab = {}
    for ab in absorbidos:
        pa = list(nodos[ab].get("pasos_accionables") or [])
        ca = list(nodos[ab].get("condiciones_activacion") or [])
        pasos_por_ab[ab] = pa
        print("  EL ABSORBIDO %s: %d pasos y %d condiciones" % (ab, len(pa), len(ca)))
        marcas_p[ab] = marcar(spec_p.get(ab) or {}, pa, "paso", ab, len(pasos_sup),
                              len(cond_sup), pasos_sup, fallos, permite_cond=True)
        marcas_c[ab] = marcar(spec_c.get(ab) or {}, ca, "condicion", ab, len(pasos_sup),
                              len(cond_sup), pasos_sup, fallos, permite_cond=False)

    # LAS GUARDAS (i), (ii) Y (v) DE LA QUINTA MARCA (vuelta 139, 2.a): miran el
    # acto entero, asi que corren cuando ya estan todos los absorbidos marcados.
    lineas_de_viaje = spec.get("lineas_de_viaje") or {}
    viajes = validar_viaja_en_el_acto(marcas_p, absorbidos, pasos_por_ab,
                                      lineas_de_viaje, fallos)
    if viajes:
        print()
        print("  VIAJA_EN_EL_ACTO, %d pieza(s) que ya viajan por otro absorbido:" % len(viajes))
        for ab_o, n_o, ab_d, n_d in viajes:
            print("     el paso %d de %s viaja por el paso %d de %s" % (n_o, ab_o, n_d, ab_d))
            print("        linea editorial: %s" % lineas_de_viaje.get("%s|%d" % (ab_o, n_o)))

    if a.reparto_viejo:
        print()
        print("  ==== EXHIBICION DEL REPARTO VIEJO (guarda (iv), vuelta 138) ====")
        print("  El dict PLANO de marcas se reparte a los %d absorbidos, que es lo que"
              % len(absorbidos))
        print("  hacia el codigo viejo. NO se escribe ningun plan.")
        colisiones = exhibir_reparto(marcas_p, marcas_c, absorbidos)
        print("  COLISIONES DEL REPARTO VIEJO: %d" % colisiones)
        if fallos:
            print("  (y ademas %d fallo(s) de marca, informativos en esta exhibicion)"
                  % len(fallos))
        print()
        print("FIN")
        return 0

    for p_ in (spec.get("perdidas") or []):
        faltan = [k for k in CLAVES_DE_PERDIDA if k not in p_]
        if faltan:
            fallos.append("a una perdida le faltan las claves %s" % ", ".join(faltan))
        elif p_["especie"] not in ESPECIES_DE_PERDIDA:
            fallos.append("especie de perdida desconocida %r. Las escritas son: %s"
                          % (p_["especie"], ", ".join(ESPECIES_DE_PERDIDA)))

    print()
    if fallos:
        print("  ROJO, %d fallos y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("     %s" % f)
        return 1

    # GUARDA (vi) DE LA QUINTA MARCA (vuelta 139, 2.a): el reparto impreso cuenta
    # VIAJA_EN_EL_ACTO junto a las otras tres, y las CUATRO cifras salen de las
    # marcas, ninguna es un literal.
    cuenta = {"APPEND": 0, "CUBIERTO": 0, "INCISO": 0, "VIAJA_EN_EL_ACTO": 0}
    for d in (marcas_p, marcas_c):
        for por_ab in d.values():
            for m in por_ab.values():
                if m == "APPEND":
                    k = "APPEND"
                elif m.startswith("INCISO"):
                    k = "INCISO"
                elif m.startswith("VIAJA_EN_EL_ACTO"):
                    k = "VIAJA_EN_EL_ACTO"
                else:
                    k = "CUBIERTO"
                cuenta[k] += 1
    print("  LA FICHA EN VERDE: cobertura exacta, guarda 1B, incisos extraidos y verbatim.")
    print("  REPARTO: piezas %d (enteras %d, ya dichas %d, de INCISO %d, que ya viajan en el acto %d)"
          % (sum(cuenta.values()), cuenta["APPEND"], cuenta["CUBIERTO"], cuenta["INCISO"],
             cuenta["VIAJA_EN_EL_ACTO"]))
    print()
    print("  LAS PERDIDAS SELLADAS EN CAMPO PROPIO (contrato %s):" % CONTRATO_DE_PERDIDAS)
    print("     perdidas selladas: %d" % len(spec.get("perdidas") or []))
    for p_ in (spec.get("perdidas") or []):
        print("        %-22s %s" % (p_["especie"], p_["que"]))
    if not (spec.get("perdidas") or []):
        print("        NINGUNA, y la lista vacia es una DECLARACION de cero perdidas.")

    acto = {
        "orden": 1,
        "miembros": [sup] + absorbidos,
        "miembros_del_acto_entero": miembros,
        "figura": "FUSION DE MESA, la ficha la escribe con su adjudicacion sellada",
        "superviviente": sup,
        "motivo": spec["motivo"],
        "absorbidos": absorbidos,
        "pasos": marcas_p,
        "condiciones": marcas_c,
        "nota_del_reparto": spec["nota"],
        "perdidas": list(spec.get("perdidas") or []),
    }
    # GUARDA (v) DE LA QUINTA MARCA (vuelta 139, 2.a): la linea editorial de cada
    # VIAJA_EN_EL_ACTO va EN EL PLAN, copiada VERBATIM del contenido como el
    # resto.
    #
    # POR QUE ESTE CAMPO NO VA SIEMPRE, al reves que `perdidas`, y se declara
    # aqui en vez de dejarlo a la vista de quien lo lea: el CASO POSITIVO de
    # esta operacion es que los tres planes sellados en las vueltas 63 y 64 se
    # regeneren IDENTICOS con el generador de hoy, salvo la fecha. Un campo
    # nuevo presente siempre, aunque vacio, MUEVE ESOS TRES FICHEROS y rompe el
    # caso positivo: la marca nueva no puede mover el camino viejo. Y no hay
    # ambiguedad que un campo vacio resolviera, porque cero viajes es cero
    # lineas y la guarda (v) ya cae en ROJO si un viaje se queda sin la suya:
    # el campo ausente aqui significa "ninguna pieza viaja por otra", medido,
    # no "el plan no lo dice".
    if lineas_de_viaje:
        acto["lineas_de_viaje"] = dict(lineas_de_viaje)
    plan = {
        "operacion": a.id_op,
        # EL ROTULO NO REPITE EL ID: el ejecutor imprime los dos campos, y
        # repetirlo publicaba OP-M-03-I . OP-M-03-I en la cabecera.
        "rotulo": spec["titulo"],
        # LA FECHA SE MIDE, NO SE TECLEA.
        "fecha": datetime.date.today().isoformat(),
        "estado": "SELLADO",
        "contrato_de_perdidas": CONTRATO_DE_PERDIDAS,
        "vuelta": a.vuelta,
        "tramo": "NO ES UN TRAMO: es la fusion de mesa %s" % a.id_op,
        # TODO LO QUE SIGUE SE COPIA VERBATIM DE LA FICHA, no se redacta aqui.
        "ficha_tipo": op.get("tipo"),
        "ficha_fecha_corte": op.get("fecha_corte"),
        "ficha_adjudicacion": op.get("adjudicacion"),
        "ficha_preservar": op.get("preservar"),
        "ficha_verificacion": op.get("verificacion"),
        "ficha_evidencia": op.get("evidencia"),
        "ficha_nota": op.get("nota"),
        "ficha_depende_de": op.get("depende_de"),
        "ficha_bloquea_a": op.get("bloquea_a"),
        "simulacion_de_hoy": spec.get("simulacion_de_hoy"),
        "actos": [acto],
        "declarados_y_no_fundidos": [],
    }
    prefijo = a.prefijo or ("PLAN_V%d_" % a.vuelta)
    destino = os.path.join(SALIDA, "%s%s.json" % (prefijo, a.id_op.replace("-", "")))
    if a.simular:
        print()
        print("  MODO SIMULAR: no se escribe el plan.")
    else:
        io.open(destino, "w", encoding="utf-8", newline=NL).write(
            json.dumps(plan, ensure_ascii=False, indent=1) + NL)
        print()
        print("  plan escrito: %s" % os.path.relpath(destino, RAIZ))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
