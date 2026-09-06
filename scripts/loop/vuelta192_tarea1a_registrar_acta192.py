# -*- coding: utf-8 -*-
r"""vuelta192_tarea1a_registrar_acta192.py . EL ACTA 192 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA, Y ESTE REGISTRADOR SIGUE SIENDO IDEMPOTENTE.

LA MAQUINA NO SE CLONA, SE IMPORTA, y eso lo adjudico la `6.6` del acta 172 como
correcto y obligatorio. De la cadena de registradores se importa todo lo que ya
existe: `titulo_de_la_negrita`, `claves_de_adjudicacion`, `claves_entrecomilladas`,
`cuenta_por_patron`, `actas_sin_entrada`, `PALABRA_CON_CERO`, los patrones de
caida, **la idempotencia entera** (`marcas_del_acta` y `entradas_que_registran`
del registrador de la 189), del registrador de la 190 `cuerpo_del_acta`,
`rango_de_seccion`, `parrafos_con_negrita`, `caidas_en_linea`,
`familia_de_la_adjudicacion`, `_normalizar`, `fila_de_la_metrica` y
`secciones_del_acta`, y del registrador de la 191 `caidas_por_numeral`,
`piezas_de_la_fila`, `numeral_de_la_fila`, `hallazgos_que_la_tabla_nombra` y
`filas_de_la_metrica`.

**LO PROPIO DE ESTE FICHERO SON LAS TRES COSAS QUE EL ACTA 192 ESTRENA**, y las
tres salen de correr la maquinaria heredada sobre el acta 192 y ver donde se
rompe, no de suponerlas. La corrida esta en el bloque `D` y en el bloque `F` de
la salida, con sus cifras:

  1) LAS TRES PREGUNTAS SE CONTESTAN CON TRES MARCAS QUE EL VOCABULARIO NO TIENE.
     `4.8` cierra en `NO MUEVE NINGUNA DEL EJECUTOR, Y MUEVE UNA MIA`, `4.9` en
     `SI, Y LO ENCARGO` y `4.10` en `LA CONTRADICCION SE RESUELVE CON LAS REGLAS
     DE CORRECCION QUE YA HAY, ASI QUE NO ES PARADA`. **Ninguna de las nueve
     marcas heredadas las ve**: corridas con el vocabulario de la 191 las TRES
     salen `SIN DECIR` y este instrumento haria PARADA sobre un acta
     perfectamente legible. Las tres se anaden LITERALES, **las nueve heredadas
     se conservan aunque hoy no muerdan**, y **la PARADA por `SIN DECIR` se
     conserva entera**.

  2) LAS CAIDAS PROPIAS DEL AUDITOR VIVEN EN PARRAFOS CUYA NEGRITA ES LA PROPIA
     CLAVE, NO UNA FRASE DE ATRIBUCION. La seccion 6 del acta 192 abre el lote
     del auditor con `**MIAS: DOS, Y UNA ES DE CIFRA PUBLICADA.**` y despues
     dedica UN PARRAFO A CADA UNA, abiertos por `**`C.1` (DE CIFRA PUBLICADA...)**`
     y `**`C.2` (DE METODO)...**`. **`caidas_en_linea()` de la 190 saca sobre esa
     seccion `(2, 0, 2)`**, o sea CERO del auditor y DOS huerfanas, y su guarda
     `if not c_aud` para. El remedio es `caidas_por_lead_heredado()`: **un parrafo
     cuya negrita ES una clave HEREDA el dueno del ultimo parrafo de atribucion**,
     y **la atribucion la siguen haciendo las mismas marcas de siempre**,
     importadas y no reescritas. Una clave sin lead previo sigue saliendo
     HUERFANA y quien llama sigue haciendo PARADA.

  3) LAS CAIDAS DEL EJECUTOR VIENEN EN UN RANGO, NO ENUMERADAS. El acta escribe
     `Declara seis (`C.1` a `C.6`)`, o sea DOS claves literales para SEIS caidas.
     Contar claves distintas da **2** donde el acta declara **6**, y esa cifra
     falsa no la caza ninguna guarda heredada. `expandir_rangos_de_clave()` lee
     el rango y publica **las dos cifras**, y quien decide es **el numeral de la
     fila de la tabla de credito**, leido de ella y no tecleado: si el rango
     expandido no calza con el numeral, PARADA.

LO QUE NO SE VUELVE A PROBAR, Y SE DICE CON SU FICHERO EN VEZ DE RE FABRICARLO:
el CERO de adjudicaciones `EN CONTRA`. El encargo de esta vuelta lo dice con esas
palabras (*"no vuelvas a probarlo por mutacion si el arnes de la 191 ya lo cubre,
y si lo cubre, DILO CON SU FICHERO"*), y lo cubre: el arnes de la 191 fabrica un
acta que SI lleva un `EN CONTRA` y exige que la cuenta lo vea. Su fichero es
`docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt`, y este instrumento LO MIDE
en vez de creerlo: comprueba que existe, que no mide cero bytes y que su
veredicto es verde, y publica sus bytes por las dos convenciones. **Lo que si
lleva caso positivo por mutacion propio son las TRES cosas de arriba**, que son
nuevas.

LA PARADA SE CONSERVA ENTERA: un estado, una atribucion o una cuenta que este
registrador no sepa leer sigue siendo PARADA, y no se resuelve a ojo.

LO QUE ESTE FICHERO NO HACE: no toca el acta, no toca el reporte, no toca
`docs/plan/` salvo para LEER, no corre la bateria, no toca ninguna guarda de la
nomina, no toca la nomina y no escribe ningun veredicto. Escribe UNA entrada en
UNA sede, y si el acta ya esta registrada, NO escribe nada.

USO:
  python scripts/loop/vuelta192_tarea1a_registrar_acta192.py
  python scripts/loop/vuelta192_tarea1a_registrar_acta192.py --simular
  python scripts/loop/vuelta192_tarea1a_registrar_acta192.py --mutacion
"""
import argparse
import hashlib
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402
from vuelta172_tarea1_registrar_acta171 import titulo_de_la_negrita   # noqa: E402
from vuelta182_tarea1a_registrar_acta181 import (   # noqa: E402
    claves_de_adjudicacion, cuenta_por_patron)
from vuelta183_tarea1a_registrar_acta182 import actas_sin_entrada   # noqa: E402
from vuelta184_tarea1a_registrar_acta184 import claves_entrecomilladas   # noqa: E402
from vuelta186_tarea1a_registrar_acta186 import (   # noqa: E402
    PALABRA_CON_CERO, PAT_CAIDA_AUDITOR_A, PAT_CAIDA_EJECUTOR_VIEJO,
    PAT_CAIDA_REPORTE, PAT_P_DEL_TITULO)
from vuelta187_tarea1a_registrar_acta187 import PAT_CAIDA_C   # noqa: E402
from vuelta188_tarea1a_registrar_acta188 import PAT_CAIDA_C_ESPACIO   # noqa: E402
from vuelta189_tarea1a_registrar_acta189 import (   # noqa: E402
    marcas_del_acta, entradas_que_registran, caidas_por_seccion)
from vuelta190_tarea1a_registrar_acta190 import (   # noqa: E402
    cuerpo_del_acta, rango_de_seccion, parrafos_con_negrita, caidas_en_linea,
    familia_de_la_adjudicacion, fila_de_la_metrica, secciones_del_acta,
    _normalizar, _lista, PAT_C_EN_LINEA,
    MARCAS_LEAD_EJECUTOR, MARCAS_LEAD_AUDITOR, MARCAS_CERO_DE_CUENTA,
    MARCAS_CERO_DE_RACHA)
from vuelta191_tarea1a_registrar_acta191 import (   # noqa: E402
    caidas_por_numeral, piezas_de_la_fila, numeral_de_la_fila,
    hallazgos_que_la_tabla_nombra, filas_de_la_metrica, PAT_CLAVE_NUMERAL,
    MARCA_EN_CONTRA, MARCA_A_FAVOR, MARCA_MITAD_BARATA,
    MARCA_ENCARGADA_BLOQUEANTE, MARCA_EXTENSION_CITABLE,
    MARCA_CUENTA_COMO_CORRIDO, MARCA_PRIMERO_SE_MIDE, MARCA_SE_RESTAURA,
    MARCA_CADUCA, AGUJA_FILA_FUERA, AGUJA_FILA_CAIDAS_AUDITOR,
    AGUJA_FILA_CAIDAS_METODO, AGUJA_FILA_PUESTOS, NOTA_DE_PUESTOS)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 192
VUELTA_QUE_ESCRIBE = 192
SUFIJO_QUE_ESCRIBE = "192"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "4."
PREFIJO_HALLAZGO = "5."
SECCION_DE_LOS_HALLAZGOS = 5
SECCION_DE_LAS_CAIDAS = 6
SECCION_DE_LA_METRICA = 7

# LAS TRES MARCAS QUE EL ACTA 192 ESTRENA, LITERALES DE SUS TRES PREGUNTAS. Van
# antes que las heredadas SOLO en el orden de busqueda de las preguntas: `EN
# CONTRA` y `A FAVOR` siguen yendo primero, y en ese orden, porque un titulo que
# tumba una cosa tiene que salir EN CONTRA aunque despues diga otra cosa.
MARCA_NO_MUEVE_RACHA = "NO MUEVE NINGUNA DEL EJECUTOR"
MARCA_SI_Y_LO_ENCARGO = "SI, Y LO ENCARGO"
MARCA_SE_RESUELVE_SOLA = "SE RESUELVE CON LAS REGLAS DE CORRECCION QUE YA HAY"

# LAS ESPECIES DE CAIDA PROPIA, LEIDAS DEL PARRAFO Y NO SUPUESTAS.
MARCA_ESPECIE_METODO = "DE METODO"
MARCA_ESPECIE_CIFRA = "DE CIFRA PUBLICADA"

# LA CLAVE `C.n` ENTRECOMILLADA, QUE ES COMO EL ACTA 192 NOMBRA SUS CAIDAS. Se
# vuelve a la clave `C.n` porque el acta 192 SI las usa; el patron `N.M` de la
# 191 se corre igual y SU CIFRA SE PUBLICA.
PAT_CLAVE_C = re.compile(r"`C\.(\d+)`")
# EL RANGO, QUE ES LO QUE ESTA ACTA ESTRENA: "`C.1` a `C.6`".
PAT_RANGO_C = re.compile(r"`C\.(\d+)`\s*a\s*`C\.(\d+)`")

# EL ARNES DE LA 191 QUE YA CUBRE EL CERO DE `EN CONTRA`, NOMBRADO PARA MEDIRLO
# EN VEZ DE RE FABRICAR SU CASO.
ARNES_QUE_YA_CUBRE = "docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt"


def estado_de_la_adjudicacion(titulo):
    """EL ESTADO DE UNA ADJUDICACION, LEIDO DE SU TITULO LITERAL. PURA.

    NO SE TECLEA NINGUNO: se busca en el titulo, EN ESTE ORDEN, `EN CONTRA`,
    `A FAVOR`, despues las TRES marcas nuevas del acta 192 y detras las SIETE
    heredadas de la 190 y la 191. **Si un titulo no dijera ninguna, el estado
    sale `SIN DECIR` y quien llama hace PARADA en vez de suponer.**

    `EN CONTRA` VA LA PRIMERA A PROPOSITO, Y SE QUEDA AUNQUE ESTA ACTA NO TENGA
    NINGUNA: un titulo que tumbara una cosa y adjudicara a favor de otra tiene
    que salir EN CONTRA, porque lo que hay que hacer sale de lo que se tumba."""
    alto = titulo.upper()
    if MARCA_EN_CONTRA in alto:
        return "EN CONTRA"
    if MARCA_A_FAVOR in alto:
        return "A FAVOR"
    if MARCA_NO_MUEVE_RACHA in alto:
        return "CONTESTADA: NO MUEVE RACHA DEL EJECUTOR Y MUEVE UNA DEL AUDITOR"
    if MARCA_SI_Y_LO_ENCARGO in alto:
        return "CONTESTADA QUE SI Y ENCARGADA"
    if MARCA_SE_RESUELVE_SOLA in alto:
        return "CONTESTADA: SE RESUELVE CON LAS REGLAS EXISTENTES, NO ES PARADA"
    if MARCA_MITAD_BARATA in alto:
        return "CONTESTADA A MEDIAS, LA MITAD BARATA ADJUDICADA"
    if MARCA_ENCARGADA_BLOQUEANTE in alto:
        return "CONTESTADA Y ENCARGADA COMO BLOQUEANTE"
    if MARCA_EXTENSION_CITABLE in alto:
        return "CONTESTADA A FAVOR POR EXTENSION CITABLE"
    if MARCA_CUENTA_COMO_CORRIDO in alto:
        return "CONTESTADA Y ENCARGADA"
    if MARCA_PRIMERO_SE_MIDE in alto:
        return "CONTESTADA Y ENCARGADA CON MEDICION PREVIA"
    if MARCA_SE_RESTAURA in alto:
        return "CONTESTADA Y ENCARGADA"
    if MARCA_CADUCA in alto:
        return "REGLA CUMPLIDA QUE CADUCA"
    return "SIN DECIR"


# EL VOCABULARIO VIEJO, PARA PODER PUBLICAR CUANTOS SALDRIAN `SIN DECIR` CON EL.
VOCABULARIO_HEREDADO = (MARCA_EN_CONTRA, MARCA_A_FAVOR, MARCA_MITAD_BARATA,
                        MARCA_ENCARGADA_BLOQUEANTE, MARCA_EXTENSION_CITABLE,
                        MARCA_CUENTA_COMO_CORRIDO, MARCA_PRIMERO_SE_MIDE,
                        MARCA_SE_RESTAURA, MARCA_CADUCA)


def expandir_rangos_de_clave(texto, patron_rango=None, patron_clave=None):
    """LAS CLAVES `C.n` DE UN TEXTO, CON SUS RANGOS EXPANDIDOS. PURA.

    Devuelve `(literales, expandidas)`, las dos como listas ordenadas de enteros.

    POR QUE EXISTE, Y ES UNA MEDICION Y NO UNA SOSPECHA: la seccion 6 del acta
    192 escribe `Declara seis (`C.1` a `C.6`)`. Contar CLAVES DISTINTAS da **2**
    donde el acta declara **6**, y ninguna guarda heredada caza esa cifra falsa
    porque las dos claves existen de verdad. Aqui se leen las dos cosas y **se
    publican las dos**, que es lo que esta casa hace con los BYTES y con las
    LINEAS.

    UN RANGO AL REVES (`C.6` a `C.1`) NO SE ADIVINA: se deja como las dos claves
    literales que es, sin expandir, y quien llama vera que la cuenta no calza con
    el numeral y hara PARADA."""
    pr = patron_rango if patron_rango is not None else PAT_RANGO_C
    pc = patron_clave if patron_clave is not None else PAT_CLAVE_C
    literales = sorted(set(int(x) for x in pc.findall(texto)))
    expandidas = set(literales)
    for a, b in pr.findall(texto):
        a, b = int(a), int(b)
        if a <= b:
            expandidas |= set(range(a, b + 1))
    return literales, sorted(expandidas)


def caidas_por_lead_heredado(lineas, ini, fin, marcas_eje=None, marcas_aud=None,
                             marcas_cero_cuenta=None, patron=None):
    """LAS CAIDAS `C.n`, REPARTIDAS POR LA NEGRITA QUE ATRIBUYE, CON HERENCIA DEL
    ULTIMO LEAD. Devuelve (del_ejecutor, del_auditor, huerfanas). PURA.

    Cada elemento es (linea_del_parrafo, clave, negrita, heredado).

    POR QUE HACE FALTA, Y ESTA MEDIDO EN EL BLOQUE F DE LA SALIDA: la seccion 6
    del acta 192 abre el lote del auditor con `**MIAS: DOS, Y UNA ES DE CIFRA
    PUBLICADA.**` y despues dedica **un parrafo a cada caida**, cuya negrita es
    LA PROPIA CLAVE y no una frase de atribucion. `caidas_en_linea()` de la 190
    saca `(2, 0, 2)` sobre esa seccion: cero del auditor y dos huerfanas, y su
    guarda `if not c_aud` PARA sobre un acta que declara las dos con toda
    claridad.

    LO QUE NO CAMBIA, Y ES LA MITAD QUE IMPORTA: **la atribucion la siguen
    haciendo las mismas marcas de siempre**, importadas de la 190 y no
    reescritas, y el cero de CUENTA sigue neutralizando. Lo unico nuevo es que un
    parrafo SIN marca de atribucion propia **hereda el dueno del ultimo parrafo
    que si la tenia**. Un parrafo con claves y SIN lead previo sigue saliendo
    HUERFANO, y quien llama sigue haciendo PARADA: la herencia no inventa duenos,
    solo continua el que el acta ya escribio."""
    m_eje = tuple(marcas_eje) if marcas_eje is not None else MARCAS_LEAD_EJECUTOR
    m_aud = tuple(marcas_aud) if marcas_aud is not None else MARCAS_LEAD_AUDITOR
    m_cc = (tuple(marcas_cero_cuenta) if marcas_cero_cuenta is not None
            else MARCAS_CERO_DE_CUENTA)
    pat = patron if patron is not None else PAT_CLAVE_C
    eje, aud, huerfanas = [], [], []
    dueno = None
    for a, _b, negrita, texto in parrafos_con_negrita(lineas, ini, fin):
        alta = negrita.upper()
        es_cero_de_cuenta = any(x in alta for x in m_cc)
        propio = None
        if any(x in alta for x in m_eje) and not es_cero_de_cuenta:
            propio = "eje"
        elif any(x in alta for x in m_aud):
            propio = "aud"
        if propio is not None:
            dueno = propio
        heredado = propio is None
        claves = sorted(set(int(x) for x in pat.findall(texto)))
        if not claves:
            continue
        actual = propio if propio is not None else dueno
        destino = {"eje": eje, "aud": aud}.get(actual, huerfanas)
        for k in claves:
            destino.append((a, "C.%d" % k, negrita, heredado))
    return eje, aud, huerfanas


def especie_de_la_caida(texto, marcas=None):
    """LAS ESPECIES QUE UN PARRAFO DE CAIDA DECLARA, LEIDAS Y NO SUPUESTAS. PURA.

    Devuelve la lista de marcas halladas, en el orden en que se le pasan. Un
    parrafo que no declare ninguna devuelve la lista vacia y quien llama decide:
    aqui, PARADA, porque el encargo pide la especie de cada una."""
    ms = tuple(marcas) if marcas is not None else (MARCA_ESPECIE_CIFRA,
                                                   MARCA_ESPECIE_METODO)
    alto = texto.upper()
    return [m for m in ms if m in alto]


def titulo_de_la_entrada(n_adj, n_hall, n_preg, n_cai_aud, n_cai_eje):
    """El titulo, con sus CINCO numerales COMPUTADOS y no tecleados, y con la
    concordancia dentro del computo. El CERO entra por `PALABRA_CON_CERO`
    importado, y va en plural porque en castellano el cero es plural."""
    def trozo(n, sing, plur):
        if n == 1:
            return "la %s" % sing
        return "las %s %s" % (PALABRA_CON_CERO[n], plur)

    def trozo_m(n, sing, plur):
        if n == 1:
            return "el %s" % sing
        return "los %s %s" % (PALABRA_CON_CERO[n], plur)
    return ("Registro de %s, %s, %s, %s del auditor y %s del ejecutor "
            "del acta de la vuelta %d"
            % (trozo(n_adj, "adjudicacion numerada", "adjudicaciones numeradas"),
               trozo_m(n_hall, "hallazgo de la seccion 5",
                       "hallazgos de la seccion 5"),
               trozo(n_preg, "pregunta contestada", "preguntas contestadas"),
               trozo(n_cai_aud, "caida propia", "caidas propias"),
               trozo(n_cai_eje, "caida", "caidas"),
               VUELTA_DEL_ACTA))


VIA = {
    "4.1": "SIN TOCAR NADA",
    "4.2": "SIN TOCAR NADA",
    "4.3": "SIN TOCAR NADA",
    "4.4": "SIN TOCAR NADA",
    "4.5": "EJECUTADA EN LA TAREA 2",
    "4.6": "SIN TOCAR NADA",
    "4.7": "SIN TOCAR NADA, Y SU REPARACION VA DESPUES DE LA 194",
    "4.8": "REGISTRADA AQUI, Y NO MUEVE NINGUNA RACHA DEL EJECUTOR",
    "4.9": "ES LA TAREA 5 DE ESTA VUELTA",
    "4.10": "REGISTRADA AQUI COMO CORRECCION DECLARADA DEL AUDITOR",
    "5.1": "ES LA TAREA 3 DE ESTA VUELTA",
    "5.2": "ES LA TAREA 4 DE ESTA VUELTA",
    "5.3": "SIN TOCAR NADA, Y LA TAREA 5 NO RE MIDE LA MARCA",
}

QUE_HACE_ESTA_VUELTA = {
    "4.1": ("SE ACATA SIN TOCAR NADA. Que el numeral de la fila decida cuantos "
            "hallazgos cuentan queda a favor, y el motivo que el acta da es el "
            "que esta vuelta hereda: **la ceguera va escrita en la propia "
            "entrada**, porque el numeral dice cuantos y no cuales. **Esta "
            "vuelta vuelve a correr esa misma vara sobre el acta 192 y publica "
            "las dos vias**, el numeral y el cotejo por subcadena, sin elegir a "
            "ojo."),
    "4.2": ("SE ACATA SIN TOCAR NADA. Comparar la nota `SOLAPE TOTAL` en "
            "mayusculas queda a favor, y el acta subraya que **es aflojar una "
            "guarda DESPUES de que mordiera**, que es la forma que esta casa "
            "vigila. **Esta vuelta no la afloja mas**: sigue publicando el "
            "literal que el acta trae y las dos comparaciones, TAL CUAL y en "
            "mayusculas."),
    "4.3": ("SE ACATA SIN TOCAR NADA, Y CON ELLA QUEDA CONTESTADO EL `PD.1` POR "
            "EXTENSION CITABLE. Tocar el codigo de doce instrumentos de vueltas "
            "cerradas queda a favor porque **lo que la regla protege son los "
            "NUMEROS publicados y las SALIDAS SELLADAS**, y las dos se "
            "respetaron. **Esta vuelta hereda la distincion y la aplica en su "
            "TAREA 3**, que toca dos arneses de la 191 que **no estan en la "
            "nomina** y **no reescribe ninguna cifra publicada**."),
    "4.4": ("SE ACATA SIN TOCAR NADA, Y ES LA QUE ORDENA LA TAREA 5. Que la "
            "regla unica y estrecha dejara fuera tres cotejos de ciega queda a "
            "favor **y el acta dice que era la unica honrada**: ensanchar la "
            "regla despues de ver el resultado es elegir el universo por el "
            "resultado. **Esta vuelta NO ensancha la regla: cambia el FORMATO de "
            "lo que se escribe de aqui en adelante**, que es la unica via que no "
            "elige el universo mirando el resultado."),
    "4.5": ("SE ACATA Y SE EJECUTA EN LA TAREA 2 DE ESTA VUELTA. Que el ejecutor "
            "no se auto encargara la relectura al doble queda a favor, **y el "
            "auditor la encarga el mismo en esta acta**, ahora con DOS motivos: "
            "el `2832` cayo fuera de los dudosos marcados de **los dos "
            "lectores** y en **dos tandas seguidas**."),
    "4.6": ("SE ACATA SIN TOCAR NADA. Publicar la cifra del detector como el "
            "tamano del asunto queda a favor **por una razon de forma y no de "
            "fondo**: las tres cegueras van escritas en la propia salida del "
            "censo, antes de su primera cifra. **Una cifra que publica su suelo "
            "y lo llama suelo no engana a nadie**, y esta vuelta aplica la misma "
            "regla en todas sus tablas."),
    "4.7": ("SE ACATA SIN TOCAR NADA, Y SU REPARACION QUEDA EXPRESAMENTE DESPUES "
            "DE LA 194. Cambiar una guarda del cerrador durante su propio cierre "
            "queda a favor, y el acta lo midio en vez de creerlo: el bloque "
            "exento es copia verbatim, `--comparar` lo vigila byte a byte, y la "
            "cobertura no se perdio sino que se movio a una guarda mas estrecha. "
            "**Y le da la razon en lo que NO hizo:** arreglar el desfase de "
            "`PATRONES_ACTA` toca `tallar_cabecera_reporte.py`, que cuatro "
            "entradas de la nomina nombran, **y moverlo antes de la bateria de "
            "la 194 pone en riesgo una corrida por algo que no es un fallo**. "
            "**Esta vuelta no lo toca, y su reporte declara el desfase sin "
            "teclear su ordinal.**"),
    "4.8": ("REGISTRADA AQUI. La pregunta `P.1` queda contestada: que la etiqueta "
            "del veredicto mordiera dos veces **no mueve ninguna racha del "
            "ejecutor** (sigue siendo defecto del cerrador, que existe para "
            "cazar justo eso y no lo cazo) **y si mueve una del auditor**, "
            "porque la cifra falsa la publico el en la `5.2` de su propia acta "
            "191. **Esta vuelta la registra y no la discute:** la caida es del "
            "auditor y va en su seccion 6 con su nombre."),
    "4.9": ("CONTESTADA QUE SI Y ES LA TAREA 5 DE ESTA VUELTA. Que el cotejo de "
            "ciega deba pasar a un formato unico queda contestado que si **y sin "
            "doctrina nueva**: la disciplina del dictado ya dice que una medicion "
            "se hace sobre un universo declarado, y la TAREA 5 de la 191 midio "
            "que el universo se queda en **6 de 43 ficheros por formato y no por "
            "fondo**. **Esta vuelta escribe el formato y mide cuantos recupera, "
            "y NO re mide la marca contra la dificultad**: elegir el universo y "
            "sacar la conclusion en el mismo acto es lo que el encargo prohibe."),
    "4.10": ("REGISTRADA AQUI COMO CORRECCION DECLARADA DEL AUDITOR, Y NO ES "
             "PARADA. El acta resuelve el `P.3` y el `PD.2` juntos: **la letra de "
             "la parada exige que la contradiccion NO se resuelva con las reglas "
             "existentes, y esta se resuelve**, porque es una correccion "
             "declarada de manual. **La cifra vieja no se borra, el reporte "
             "cerrado no se reescribe, y el corte nuevo va al lado con su "
             "fecha.** **Esta vuelta no reescribe ni el acta 191 ni ningun "
             "reporte archivado.**"),
    "5.1": ("HALLAZGO DEL AUDITOR FUERA DE LO QUE EL REPORTE MARCA, Y ES LA TAREA "
            "3 DE ESTA VUELTA, BLOQUEANTE POR LA BATERIA DE LA 194. Dos arneses "
            "de la propia vuelta 191 salen `SUJETO VIVO` y entran en la nomina a "
            "la vuelta siguiente, **y la `4.4` del acta 191 ya adjudico que eso "
            "es FALLO y no deuda**. La confirmacion empirica la trae el propio "
            "acta: dos salidas selladas no reprodujeron byte a byte. **Se arregla "
            "ANTES de la bateria, no dentro**, porque una salida que no reproduce "
            "por sujeto vivo convierte una corrida legitima en un rojo que nadie "
            "sabra leer."),
    "5.2": ("HALLAZGO DEL AUDITOR FUERA DE LO QUE EL REPORTE MARCA, LEVANTADO "
            "CONTRA SI MISMO, Y ES LA TAREA 4 DE ESTA VUELTA. El sello guarda "
            "tres puertas (`git log`, `git status` y `REPORTE.md`) **y el sujeto "
            "de la ciega no vive en ninguna de las tres**: vive en las razones y "
            "las clases del archivo de veredictos. **El remedio no puede ser que "
            "el auditor se acuerde**, que es justo la enfermedad que el fichero "
            "vino a curar. **Esta vuelta le anade la cuarta puerta al fichero de "
            "nombre estable, sin clonarlo.**"),
    "5.3": ("SE ACATA SIN TOCAR NADA, Y LA TAREA 5 NO RE MIDE LA MARCA. Que una "
            "de las tres discrepancias del auditor lleve `DISCUTIBLE MARCADO` es "
            "**el segundo dato independiente que apunta en la misma direccion** "
            "que el `+7,40` que midio la TAREA 5 de la 191, **y el acta no lo "
            "escribe como tendencia**, que es lo correcto con tres casos. **El "
            "encargo de esta vuelta prohibe expresamente re medir la marca aqui:** "
            "el universo nuevo se usa cuando este medido y declarado, no en el "
            "mismo acto en que se construye."),
}


def armar_entrada(numero, titulo, medido):
    """LA ENTRADA ENTERA. PURA: recibe todo lo ya medido en un diccionario y no
    lee ni escribe nada."""
    m = medido
    p = []
    p.append("## R.%d. %s" % (numero, titulo))
    p.append("")
    p.append("(Acta del auditor, vuelta %d, secciones %s; escrito en la vuelta %d,"
             % (VUELTA_DEL_ACTA, _lista(m["secciones"]), VUELTA_QUE_ESCRIBE))
    p.append("TAREA 1.)")
    p.append("")
    p.append("Por adicion, como `R.21` a `R.53`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.53`. Salida:")
    p.append("`docs/loop/SALIDA_V%s_T1A_REGISTRO_R%d.txt`."
             % (SUFIJO_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 1 EN CURSO Y LAS TAREAS 2 A 5 SIN")
    p.append("EMPEZAR, ASI QUE SUS GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA NO HA")
    p.append("PASADO.** Es la forma que la `6.4` del acta 172 adjudico como correcta.")
    p.append("")
    p.append("**Y LOS CINCO NUMERALES DEL TITULO TAMPOCO ESTAN TECLEADOS:** se cuentan del")
    p.append("acta acotada (lineas %d a %d) y de ahi sale el numeral en palabra, incluida"
             % (m["inicio"], m["fin"]))
    p.append("la concordancia. **%d adjudicaciones numeradas (`4.1` a `4.%d`, todas en la"
             % (m["n_adj"], m["n_adj"]))
    p.append("seccion 4), %d hallazgos numerados en la seccion 5, %d preguntas contestadas"
             % (m["n_hall"], m["n_preg"]))
    p.append("DENTRO de las adjudicaciones, %d caidas propias del auditor y %d caidas del"
             % (m["n_aud"], m["n_eje"]))
    p.append("ejecutor.**")
    p.append("")
    p.append("**LA FORMA DE LOS NUMERALES SE MIDE CON LOS DOS PATRONES Y LAS DOS CIFRAS SE")
    p.append("PUBLICAN.** Corrido sobre esta acta, **el patron entrecomillado (el del acta")
    p.append("188) da %d y el suelto (el del acta 189) da %d**. **Ninguno de los dos se"
             % (m["n_entrecomillado"], m["n_adj"]))
    p.append("ensancha: se corren los dos y se dice lo que dan.**")
    p.append("")
    p.append("**EL CERO DE `EN CONTRA` SE REPITE POR SEGUNDA ACTA SEGUIDA, Y ESTA VEZ NO SE")
    p.append("VUELVE A PROBAR POR MUTACION: SE DICE CON SU FICHERO.** De las %d que nombran"
             % m["n_adj"])
    p.append("un `D.n` o un `P.n`, **%d son discutibles del ejecutor y los %d van A FAVOR**;"
             % (m["n_discutibles"], m["n_a_favor_discutibles"]))
    p.append("**EN CONTRA salen %d**. El encargo de esta vuelta lo dice con esas palabras:"
             % m["n_en_contra_discutibles"])
    p.append("si el arnes de la 191 ya lo cubre, se dice con su fichero en vez de re")
    p.append("fabricarlo. **Y ese fichero se MIDE aqui en vez de creerse:**")
    p.append("`%s`," % ARNES_QUE_YA_CUBRE)
    p.append("`disco %d bytes | LF %d bytes`, y su veredicto leido del propio fichero es"
             % (m["arnes_disco"], m["arnes_lf"]))
    p.append("**%s**. La guarda vieja de la 190 (`if not en_contra: PARADA`) corrida sobre"
             % m["arnes_veredicto"])
    p.append("el acta %d: **%s**. Aqui el cero es un RESULTADO, y **lo que sigue parando es"
             % (VUELTA_DEL_ACTA, "PARARIA" if m["vieja_pararia"] else "no pararia"))
    p.append("lo que de verdad no se puede leer**: un discutible cuyo estado no sea NI a")
    p.append("favor NI en contra, que hoy son **%d**." % m["n_discutibles_sin_sentido"])
    p.append("")
    p.append("**LO PRIMERO QUE ESTA ACTA ESTRENA: LAS TRES PREGUNTAS SE CONTESTAN CON TRES")
    p.append("MARCAS QUE EL VOCABULARIO NO TENIA.** Corrido con el vocabulario heredado y")
    p.append("nada mas (las nueve marcas de la 190 y la 191), **%d titulo(s) saldrian `SIN"
             % m["n_sin_decir_vieja"])
    p.append("DECIR`** y este instrumento haria PARADA sobre un acta perfectamente legible.")
    p.append("Las tres se anaden LITERALES (`%s`, `%s` y" % (MARCA_NO_MUEVE_RACHA,
                                                             MARCA_SI_Y_LO_ENCARGO))
    p.append("`%s`), **las nueve heredadas se conservan aunque hoy no muerdan**"
             % MARCA_SE_RESUELVE_SOLA)
    p.append("(estrechar el vocabulario a lo que el acta de hoy usa haria parar la proxima")
    p.append("que las use) y **la PARADA por `SIN DECIR` se conserva entera**.")
    p.append("")
    p.append("**LAS %s ADJUDICACIONES NUMERADAS, CON SU LINEA EN EL ACTA LEIDA HOY.** El"
             % PALABRA_CON_CERO[m["n_adj"]].upper())
    p.append("titulo de cada una es LITERAL del fichero; la glosa que sigue es prosa del")
    p.append("ejecutor y va marcada como tal.")
    p.append("")
    for clave, familia, estado, ln, tit in m["adjudicaciones"]:
        p.append("  - **`%s` (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). FAMILIA: %s. "
                 "ESTADO: %s. VIA: %s.** Titulo" % (clave, ln, familia, estado,
                                                    VIA.get(clave, "(sin via)")))
        p.append("    literal del acta: *\"%s\"*" % tit)
        p.append("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA.get(clave, "(sin glosa)"))
    p.append("")
    p.append("**LOS `D.n` DEL REPORTE DE LA 191 VAN CON SU ORDEN MEDIDO Y NO SUPUESTO.** El")
    p.append("encargo avisa de que en ese reporte el `D.7` va escrito ANTES del `D.6`, y")
    p.append("eso **no se cree: se mide, y con DOS varas, porque no dan lo mismo**.")
    p.append("")
    p.append("  - **VARA A, LA MENCION SUELTA** (el primer sitio del fichero donde aparece")
    p.append("    la clave, sea prosa, tabla o titulo): %s."
             % (", ".join("`D.%s` en la linea %d" % (k, ln)
                          for k, ln in m["orden_suelto"]) or "(ninguno)"))
    p.append("    **El aviso del encargo por esta vara: %s.**"
             % ("CALZA" if m["d7_suelto"] else "NO CALZA"))
    p.append("  - **VARA B, EL TITULO DEL DISCUTIBLE** (la linea que EMPIEZA por la clave en")
    p.append("    negrita, que es donde el reporte declara cada uno): %s."
             % (", ".join("`D.%s` en la linea %d" % (k, ln)
                          for k, ln in m["orden_dn"]) or "(ninguno)"))
    p.append("    **El aviso del encargo por esta vara: %s.**"
             % ("CALZA" if m["d7_antes_del_d6"] else "NO CALZA"))
    p.append("")
    p.append("**LA QUE CONTESTA A LA PREGUNTA DEL ENCARGO ES LA B**, porque el encargo habla")
    p.append("de como estan ESCRITOS los discutibles y no de donde se les nombra de pasada.")
    p.append("**La vara A no puede ordenar dos claves que comparten renglon**, y en ese")
    p.append("reporte `D.1` y `D.6` se nombran en la misma linea de la tabla de tareas.")
    p.append("**Las dos se publican y no se elige la que conviene.** Y esto NO cambia")
    p.append("ninguna cuenta: las adjudicaciones se leen del acta por su clave `4.n`, no por")
    p.append("el orden en que el reporte escribio sus discutibles.")
    p.append("")
    p.append("**LAS %s PREGUNTAS ESTAN CONTESTADAS Y NO TIENEN SECCION PROPIA:** viven"
             % PALABRA_CON_CERO[m["n_preg"]].upper())
    p.append("DENTRO de las adjudicaciones, como en las actas 189, 190 y 191. **Cuales son")
    p.append("NO se teclea:** son las %d cuyo titulo nombra un `P.n`, y son **%s**."
             % (m["n_preg"],
                ", ".join("`%s` que nombra `%s`" % (c, pn) for c, pn in m["preguntas"])))
    p.append("")
    p.append("**LOS %s HALLAZGOS DE LA SECCION 5, Y LOS %s CUENTAN COMO HALLAZGO FUERA DEL"
             % (PALABRA_CON_CERO[m["n_hall"]].upper(),
                PALABRA_CON_CERO[m["n_fuera"]].upper()))
    p.append("MARCADO. CUANTOS NO SE TECLEA:** quien decide es **el numeral de la propia")
    p.append("fila de la tabla de credito**, leido de ella, que dice **%d**, y la seccion"
             % m["numeral_fila"])
    p.append("tiene **%d** claves `5.n`. El cotejo por subcadena queda al lado como lo que"
             % m["n_hall"])
    p.append("es, **una medicion mas debil**: partiendo el parentesis por `;` da **%d**"
             % m["n_piezas_pyc"])
    p.append("pieza(s) y casa con **%d**; partiendo tambien por `,` da **%d** piezas y casa"
             % (m["n_casan_pyc"], m["n_piezas"]))
    p.append("con **%d**. La fila, leida del fichero:" % len(m["hall_nombrados"]))
    p.append("")
    for ln, txt in m["fila_fuera"]:
        p.append("  - `docs/loop/ACTA_AUDITOR.md:%d`: %s" % (ln, txt))
    p.append("")
    p.append("  Las piezas que salen de su parentesis partiendo por `;` y por `,`: %s."
             % (", ".join("*%s*" % x for x in m["piezas_fuera"]) or "(ninguna)"))
    p.append("")
    for clave, ln, tit in m["hallazgos"]:
        marca = ("**la subcadena de la fila SI lo nombra**"
                 if clave in m["claves_nombradas"] else
                 "la subcadena de la fila NO lo nombra, y aun asi cuenta, porque "
                 "quien decide es el numeral")
        p.append("  - **`%s` (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). VIA: %s.** %s."
                 % (clave, ln, VIA.get(clave, "(sin via)"), marca))
        p.append("    Titulo literal del acta: *\"%s\"*" % tit)
        p.append("    **QUE HACE ESTA VUELTA CON EL (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA.get(clave, "(sin glosa)"))
    p.append("")
    p.append("**LAS CAIDAS: %s DEL AUDITOR Y %s DEL EJECUTOR, Y AQUI VAN LAS OTRAS DOS"
             % (PALABRA_CON_CERO[m["n_aud"]].upper(),
                PALABRA_CON_CERO[m["n_eje"]].upper()))
    p.append("COSAS QUE ESTA ACTA ESTRENA.**")
    p.append("")
    p.append("**LA SEGUNDA: LAS CAIDAS PROPIAS DEL AUDITOR VIVEN EN PARRAFOS CUYA NEGRITA")
    p.append("ES LA PROPIA CLAVE.** El acta abre el lote con `%s` y despues"
             % m["negrita_aud_lead"])
    p.append("dedica **un parrafo a cada una**, abiertos por la clave y no por una frase de")
    p.append("atribucion. **`caidas_en_linea()` de la 190 saca sobre esta seccion (%d, %d,"
             % (m["v190_eje"], m["v190_aud"]))
    p.append("%d)**: cero del auditor y dos huerfanas, y su guarda `if not c_aud` PARA. La"
             % m["v190_huerf"])
    p.append("maquina de la 189 saca **(%d, %d, %d)** y la de la 191, que cuenta la clave"
             % (m["v189_eje"], m["v189_aud"], m["v189_huerf"]))
    p.append("`N.M`, saca **(%d, %d, %d)**. **El remedio es `caidas_por_lead_heredado()`:"
             % (m["v191_eje"], m["v191_aud"], m["v191_huerf"]))
    p.append("un parrafo cuya negrita ES una clave HEREDA el dueno del ultimo parrafo de")
    p.append("atribucion**, y la atribucion la siguen haciendo las mismas marcas de siempre,")
    p.append("importadas y no reescritas. Con eso el reparto sale **ejecutor %d, auditor %d,"
             % (m["n_eje_literal"], m["n_aud"]))
    p.append("huerfanas %d**, y **%d de las del auditor entraron POR HERENCIA**, dicho para"
             % (m["n_huerf"], m["n_aud_heredadas"]))
    p.append("que se pueda discutir. **La herencia no inventa duenos: un parrafo con claves")
    p.append("y sin lead previo sigue saliendo HUERFANO y sigue haciendo PARADA.**")
    p.append("")
    p.append("**LA TERCERA: LAS CAIDAS DEL EJECUTOR VIENEN EN UN RANGO Y NO ENUMERADAS.**")
    p.append("El acta escribe su lote como un rango, o sea **%d claves literales** para"
             % m["n_eje_literal"])
    p.append("**%d caidas**. Contar claves distintas daria **%d** donde el acta declara"
             % (m["n_eje"], m["n_eje_literal"]))
    p.append("**%d**, y esa cifra falsa **no la caza ninguna guarda heredada**, porque las"
             % m["n_eje"])
    p.append("dos claves existen de verdad. `expandir_rangos_de_clave()` lee el rango y")
    p.append("publica **las dos cifras**; y quien decide es **el numeral de la fila de la")
    p.append("tabla de credito**, leido de ella y no tecleado, que dice **%d**. Si el rango"
             % m["numeral_metodo"])
    p.append("expandido no calzara con el numeral, esto seria PARADA.")
    p.append("")
    p.append("**LA ESPECIE DE CADA CAIDA PROPIA SE LEE DEL PARRAFO Y NO SE SUPONE**, que es")
    p.append("lo que el encargo pide al decir que las dos van escritas como dos y ninguna")
    p.append("se omite:")
    p.append("")
    for clave, ln, especies in m["especies_aud"]:
        p.append("  - **`%s`** (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). Especies que su"
                 % (clave, ln))
        p.append("    parrafo declara, literales: %s."
                 % (", ".join("`%s`" % e for e in especies) or "**NINGUNA**"))
    p.append("")
    p.append("**Y EL CERO DEL EJECUTOR SIGUE SIENDO UN CERO DE RACHA Y NO DE CUENTA.** La")
    p.append("negrita que lo declara es literal del acta: `%s`. Declara cero"
             % m["negrita_eje"])
    p.append("caidas QUE ACUMULEN y **en el mismo parrafo declara %d de metodo**. Tratado"
             % m["n_eje"])
    p.append("como cero de CUENTA, el reparto del ejecutor sale **%d**, o sea que"
             % m["cero_confundido_eje"])
    p.append("confundirlas borraria **%d** clave(s) de la cuenta."
             % (m["n_eje_literal"] - m["cero_confundido_eje"]))
    p.append("")
    p.append("**LA METRICA DE CREDITO DE LA SECCION %d, PEGADA ENTERA DEL FICHERO Y NO"
             % SECCION_DE_LA_METRICA)
    p.append("RESUMIDA.** Son **%d** filas de datos, contadas y no tecleadas:" % m["n_filas7"])
    p.append("")
    for ln, txt in m["filas7"]:
        p.append("  - `docs/loop/ACTA_AUDITOR.md:%d`: %s" % (ln, txt))
    p.append("")
    p.append("**Y LA FILA DE PUESTOS VA CON SU NOTA, QUE ES LO QUE EL ENCARGO MANDA")
    p.append("REGISTRAR:** **30 aislados y 28 cotejados**, y los 28 son **SOLAPE TOTAL a")
    p.append("proposito, o sea control y NO cobertura nueva**. El literal que el acta")
    p.append("escribe de verdad, leido y no parafraseado, es `%s`; comparado TAL CUAL"
             % m["nota_literal"])
    p.append("contra el `%s` del encargo da **%s**, y comparado en mayusculas da"
             % (NOTA_DE_PUESTOS, "SI" if m["nota_exacta"] else "NO"))
    p.append("**%s**. **Las dos cifras se publican**, y es la `4.2` de esta misma acta la"
             % ("SI" if m["nota_de_puestos"] else "NO"))
    p.append("que adjudico esa comparacion. **Si las palabras no estuvieran, este")
    p.append("instrumento haria PARADA**, porque el encargo pide esa nota y una nota que no")
    p.append("esta no se parafrasea.")
    p.append("")
    p.append("**LA DEUDA DE LA SERIE, REMEDIDA AQUI EN VEZ DE HEREDARSE DEL `R.53`:**")
    p.append("")
    faltan, bajo, alto = m["salto"]
    p.append("  - **SALTO DE %d REGISTROS EN LA SERIE: las actas %s no tienen"
             % (len(faltan), ("%d a %d" % (min(faltan), max(faltan))) if faltan
                else "(ninguna)"))
    p.append("    entrada propia.** Sus dos extremos, contados por")
    p.append("    `scripts/loop/serie_de_registros.py` y no tecleados: **`R.%s` cubre el"
             % (bajo[0] if bajo else "?"))
    p.append("    acta %s** y **`R.%s` cubre el acta %s**. **No se rellenan aqui:**"
             % (bajo[1] if bajo else "?", alto[0] if alto else "?",
                alto[1] if alto else "?"))
    p.append("    el encargo de esta vuelta las deja EXPRESAMENTE fuera, medidas y no")
    p.append("    arregladas.")
    p.append("")
    p.append("**Y ESTA ENTRADA LA ESCRIBE UN REGISTRADOR IDEMPOTENTE, Y LA IDEMPOTENCIA NO")
    p.append("SE RE ESCRIBE: SE IMPORTA DEL DE LA 189, QUE ES DONDE NACIO.** La comprobacion")
    p.append("es **por el acta y no por el numero**, con las marcas literales `%s` y `%s`,"
             % marcas_del_acta(VUELTA_DEL_ACTA))
    p.append("y **en LAS DOS SEDES**. Antes de escribir esta entrada, esas marcas aparecian")
    p.append("en **%d linea(s)**." % m["ya_registrada"])
    p.append("")
    p.append("**LO QUE ESTA ENTRADA NO REGISTRA, DICHO PARA QUE NO SE BUSQUE:** no registra")
    p.append("el desfase de `PATRONES_ACTA` arreglado (va DESPUES de la 194 por la `4.7`),")
    p.append("ni `acumulan()` leyendo la tabla, ni el cotejo de clon declarado que separa,")
    p.append("ni la excepcion que publica siempre su lista, ni la medicion del censo de")
    p.append("arneses con carril de mutacion sin fichero propio, ni las ocho actas sin")
    p.append("entrada propia rellenadas, ni el exitcode 2 propagado a `--componer`, ni el")
    p.append("estado de `OP-L-02` movido: **el encargo de esta vuelta las nombra una a una")
    p.append("como fuera**. **Y no se poda la nomina de la bateria**, que es la opcion `c`")
    p.append("que el fundador RECHAZO el 5 sep 2026, **ni se corre la bateria**, que cae en")
    p.append("la 194.")
    return NL.join(p) + NL


# ---------------------------------------------------------------- LA MUTACION
def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    w("   %-62s %s" % (nombre, "VERDE" if ok else "ROJO"))
    if not ok:
        w("      esperado: %r" % (esperado,))
        w("      obtenido: %r" % (obtenido,))
    return ok


def _seccion_fabricada(negrita_lead_aud, claves_aud, negrita_eje, texto_eje):
    """UNA SECCION 6 FABRICADA, PARA TUMBAR LAS DOS MAQUINAS NUEVAS. PURA."""
    l = ["## 6. LAS CAIDAS", ""]
    l.append("**%s** %s" % (negrita_eje, texto_eje))
    l.append("")
    l.append("**%s**" % negrita_lead_aud)
    l.append("")
    for k in claves_aud:
        l.append("**`%s` (DE METODO). UN PARRAFO PROPIO.** Su cuerpo." % k)
        l.append("")
    return l


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION DE LAS TRES COSAS NUEVAS. No toca el repo.

    LO QUE NO PRUEBA AQUI, Y SE DICE: el cero de `EN CONTRA` NO se vuelve a
    fabricar. Su caso vive en el arnes de la 191 y este fichero lo MIDE en el
    bloque D de la corrida normal, con sus bytes por las dos convenciones."""
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("VUELTA %d, TAREA 1: CASO POSITIVO POR MUTACION DE LAS TRES COSAS NUEVAS"
      % VUELTA_QUE_ESCRIBE)
    w("=" * 78)
    w("")
    w("LO QUE SE PRUEBA, Y POR QUE ESTE ES EL CASO QUE PUEDE CAER: las tres")
    w("maquinas nuevas se corren sobre textos FABRICADOS con la cifra sabida, y el")
    w("valor esperado NO es una constante literal igual a la obtenida: cada caso")
    w("compara contra la cifra que el texto fabricado lleva DENTRO por")
    w("construccion, y el caso de mutacion cambia el texto y exige que CAIGA.")
    w("")

    w("A) `estado_de_la_adjudicacion` CON LAS TRES MARCAS NUEVAS")
    for marca, esperado in ((MARCA_NO_MUEVE_RACHA,
                             "CONTESTADA: NO MUEVE RACHA DEL EJECUTOR Y MUEVE UNA DEL AUDITOR"),
                            (MARCA_SI_Y_LO_ENCARGO, "CONTESTADA QUE SI Y ENCARGADA"),
                            (MARCA_SE_RESUELVE_SOLA,
                             "CONTESTADA: SE RESUELVE CON LAS REGLAS EXISTENTES, NO ES PARADA")):
        titulo = "4.9 `P.9`, una pregunta cualquiera. %s." % marca
        ok &= _caso(w, "titulo con %r" % marca[:34],
                    estado_de_la_adjudicacion(titulo), esperado)
    w("   LA MUTACION: si la marca se le quita al titulo, el estado TIENE que caer")
    w("   a SIN DECIR, que es lo que hace PARAR al instrumento.")
    for marca in (MARCA_NO_MUEVE_RACHA, MARCA_SI_Y_LO_ENCARGO, MARCA_SE_RESUELVE_SOLA):
        titulo = "4.9 `P.9`, una pregunta cualquiera. LA MARCA BORRADA."
        ok &= _caso(w, "sin %r -> SIN DECIR" % marca[:30],
                    estado_de_la_adjudicacion(titulo), "SIN DECIR")
    w("   Y `EN CONTRA` SIGUE GANANDO AUNQUE EL TITULO TRAIGA UNA MARCA NUEVA:")
    ok &= _caso(w, "EN CONTRA gana a la marca nueva",
                estado_de_la_adjudicacion("4.9 `P.9`, algo. EN CONTRA. %s."
                                          % MARCA_SI_Y_LO_ENCARGO),
                "EN CONTRA")
    w("")

    w("B) `expandir_rangos_de_clave` SOBRE UN RANGO FABRICADO")
    texto = "Declara seis (`C.1` a `C.6`), las seis de metodo. La `C.6` la cazo."
    lit, exp = expandir_rangos_de_clave(texto)
    ok &= _caso(w, "claves literales del texto fabricado", lit, [1, 6])
    ok &= _caso(w, "claves con el rango expandido", exp, [1, 2, 3, 4, 5, 6])
    w("   LA MUTACION 1: sin el rango, expandir tiene que dar LO MISMO que")
    w("   literales, que es la cifra falsa que esta maquina existe para cazar.")
    lit2, exp2 = expandir_rangos_de_clave("Declara seis (`C.1`, `C.6`).")
    ok &= _caso(w, "sin rango, literales y expandidas coinciden", lit2 == exp2, True)
    ok &= _caso(w, "sin rango, la cuenta cae de 6 a 2", len(exp2), 2)
    w("   LA MUTACION 2: un rango AL REVES no se adivina, y se queda sin expandir.")
    lit3, exp3 = expandir_rangos_de_clave("Declara (`C.6` a `C.1`).")
    ok &= _caso(w, "rango al reves NO se expande", exp3, [1, 6])
    w("")

    w("C) `caidas_por_lead_heredado` SOBRE UNA SECCION FABRICADA")
    lineas = _seccion_fabricada("MIAS: DOS, Y UNA ES DE CIFRA PUBLICADA.",
                                ["C.1", "C.2"],
                                "DEL EJECUTOR: CERO QUE ACUMULEN.",
                                "Declara seis (`C.1` a `C.6`).")
    eje, aud, huerf = caidas_por_lead_heredado(lineas, 1, len(lineas))
    ok &= _caso(w, "del ejecutor (claves literales del rango)", len(eje), 2)
    ok &= _caso(w, "del auditor, POR HERENCIA del lead MIAS", len(aud), 2)
    ok &= _caso(w, "huerfanas", len(huerf), 0)
    ok &= _caso(w, "las dos del auditor entran heredadas",
                [h for _l, _k, _n, h in aud], [True, True])
    w("   LA MUTACION 1: la maquina de la 190 sobre ESTA MISMA seccion tiene que")
    w("   sacar CERO del auditor, que es el fallo que esto viene a arreglar.")
    v190 = caidas_en_linea(lineas, 1, len(lineas))
    ok &= _caso(w, "caidas_en_linea() de la 190: auditor", len(v190[1]), 0)
    ok &= _caso(w, "caidas_en_linea() de la 190: huerfanas", len(v190[2]), 2)
    w("   LA MUTACION 2: SI SE QUITA EL LEAD `MIAS`, las dos del auditor TIENEN")
    w("   que caer a HUERFANAS. La herencia no inventa duenos.")
    lineas2 = _seccion_fabricada("UN PARRAFO QUE NO ATRIBUYE NADA.",
                                 ["C.1", "C.2"],
                                 "OTRO PARRAFO QUE TAMPOCO ATRIBUYE.",
                                 "Declara seis (`C.1` a `C.6`).")
    eje2, aud2, huerf2 = caidas_por_lead_heredado(lineas2, 1, len(lineas2))
    ok &= _caso(w, "sin lead: del auditor", len(aud2), 0)
    ok &= _caso(w, "sin lead: del ejecutor", len(eje2), 0)
    ok &= _caso(w, "sin lead: HUERFANAS (lo que hace PARAR)", len(huerf2), 4)
    w("   LA MUTACION 3: si el lead del ejecutor fuera un cero DE CUENTA y no de")
    w("   RACHA, sus claves TIENEN que dejar de contarsele.")
    eje3, aud3, huerf3 = caidas_por_lead_heredado(
        lineas, 1, len(lineas),
        marcas_cero_cuenta=(MARCAS_CERO_DE_CUENTA + MARCAS_CERO_DE_RACHA))
    ok &= _caso(w, "cero de cuenta: del ejecutor cae a 0", len(eje3), 0)
    w("")

    w("D) `especie_de_la_caida` LEE LA ESPECIE Y NO LA SUPONE")
    ok &= _caso(w, "parrafo con DE CIFRA PUBLICADA y DE METODO",
                especie_de_la_caida("`C.1` (DE CIFRA PUBLICADA). Y ADEMAS DE METODO."),
                [MARCA_ESPECIE_CIFRA, MARCA_ESPECIE_METODO])
    ok &= _caso(w, "parrafo solo con DE METODO",
                especie_de_la_caida("`C.2` (DE METODO). Nada mas."),
                [MARCA_ESPECIE_METODO])
    w("   LA MUTACION: un parrafo SIN especie tiene que dar la lista VACIA, que es")
    w("   lo que hace PARAR al instrumento.")
    ok &= _caso(w, "parrafo sin ninguna especie",
                especie_de_la_caida("`C.3` sin decir de que especie es."), [])
    w("")

    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_MUTACION_REGISTRADOR.txt"
                        % SUFIJO_QUE_ESCRIBE)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if ok else 1


# ------------------------------------------------------------------ LA MEDIDA
def _medir():
    """LA PRIMERA MITAD DE main(): acotar el acta y contar. Devuelve o bien un
    entero (codigo de salida, cuando hay PARADA) o bien la tupla (salida, medido).

    TODA CIFRA SALE DE AQUI Y NINGUNA DEL ENCARGO. Donde el encargo o el acta
    publican una, se computa la propia y **se publican las dos**."""
    salida = []
    w = salida.append
    w("=" * 78)
    w("VUELTA %d, TAREA 1: EL ACTA %d ENTERA, REGISTRADA"
      % (VUELTA_QUE_ESCRIBE, VUELTA_DEL_ACTA))
    w("=" * 78)
    w("")

    lineas, rango, err = cuerpo_del_acta(None, CABECERA_ACTA)
    if err:
        w(err)
        print(NL.join(salida))
        return 1
    inicio, fin = rango
    w("A) EL CUERPO DEL ACTA, ACOTADO ANTES DE CONTAR NADA")
    w("   acta %d: docs/loop/ACTA_AUDITOR.md, lineas %d a %d"
      % (VUELTA_DEL_ACTA, inicio, fin))
    w("   por `fin - inicio + 1` da %d lineas" % (fin - inicio + 1))
    w("   docs/loop/ACTA_AUDITOR.md -> disco %d bytes" % os.path.getsize(ACTA))
    secciones = secciones_del_acta(lineas, inicio, fin)
    w("   SECCIONES `## n.` DEL ACTA, LEIDAS Y NO TECLEADAS: %s" % _lista(secciones))
    w("")

    w("B) LA IDEMPOTENCIA, COMPROBADA ANTES DE MEDIR NADA MAS Y POR EL ACTA")
    w("   (la maquina se IMPORTA del registrador de la 189: `marcas_del_acta` y")
    w("    `entradas_que_registran`. No se re escribe una copia)")
    sedes = {}
    for ruta in SERIE.SEDES:
        rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
        sedes[rel] = io.open(ruta, encoding="utf-8", errors="replace").read()
    marca_t, marca_c = marcas_del_acta(VUELTA_DEL_ACTA)
    w("   las DOS sedes que se miran: %s" % ", ".join(sorted(sedes)))
    w("   las DOS marcas literales, computadas de la vuelta y no tecleadas:")
    w("      %r" % marca_t)
    w("      %r" % marca_c)
    ya = entradas_que_registran(VUELTA_DEL_ACTA, sedes)
    w("   CIFRA lineas que ya registran el acta %d: %d" % (VUELTA_DEL_ACTA, len(ya)))
    for r, i, mk, t in ya:
        w("      %s:%d %r" % (r, i, t[:100]))
    w("   CIFRA bytes de docs/PENDIENTES.md ANTES de tocar nada: %d"
      % os.path.getsize(SEDE))
    w("")

    w("C) LAS ADJUDICACIONES, CONTADAS CON LOS DOS PATRONES Y NO TECLEADAS")
    claves = claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_ADJ)
    entrecomilladas = claves_entrecomilladas(lineas, inicio, fin, PREFIJO_ADJ)
    w("   patron SIN comillas inversas -> %d" % len(claves))
    for clave, cuantas in claves:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    w("   patron CON comillas inversas (el del acta 188) -> %d" % len(entrecomilladas))
    dobles = [c for c, n in claves if n != 1]
    if dobles:
        w("   PARADA: hay claves repetidas dentro del acta: %s" % ", ".join(dobles))
        print(NL.join(salida))
        return 1
    if not claves:
        w("   PARADA: ningun patron encuentra adjudicaciones y el acta 192 declara")
        w("   diez. No se escribe una entrada con cero.")
        print(NL.join(salida))
        return 1
    w("")

    w("D) EL TITULO LITERAL DE CADA ADJUDICACION, SU FAMILIA Y SU ESTADO")
    w("   (EL VOCABULARIO LLEVA LAS TRES MARCAS NUEVAS DEL ACTA 192 Y CONSERVA LAS")
    w("    NUEVE HEREDADAS. `EN CONTRA` sigue buscandose PRIMERO aunque hoy no")
    w("    muerda)")
    adjudicaciones = []
    n_sin_decir_vieja = 0
    for clave, _n in claves:
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, err2 = titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err2:
            w("   %s -> %s" % (clave, err2))
            print(NL.join(salida))
            return 1
        ln, tit = res
        if not any(v in tit.upper() for v in VOCABULARIO_HEREDADO):
            n_sin_decir_vieja += 1
        adjudicaciones.append((clave, familia_de_la_adjudicacion(tit),
                               estado_de_la_adjudicacion(tit), ln, tit))
        w("   %-5s linea %-6d [%s / %s]" % (clave, ln, adjudicaciones[-1][1],
                                            adjudicaciones[-1][2]))
        w("         %s" % tit[:150])
    sin_decir = [c for c, _f, e, _l, _t in adjudicaciones if e == "SIN DECIR"]
    if sin_decir:
        w("   PARADA: %s esta en un estado que este registrador NO SABE LEER."
          % ", ".join(sin_decir))
        print(NL.join(salida))
        return 1
    w("   CON EL VOCABULARIO HEREDADO Y NADA MAS, saldrian SIN DECIR: %d"
      % n_sin_decir_vieja)
    discutibles = [a for a in adjudicaciones if a[1] == "DISCUTIBLE"]
    preguntas = [a for a in adjudicaciones if a[1] == "PREGUNTA"]
    otras = [a for a in adjudicaciones if a[1] == "OTRA"]
    a_favor = [a for a in discutibles if a[2] == "A FAVOR"]
    en_contra = [a for a in discutibles if a[2] == "EN CONTRA"]
    w("   REPARTO POR FAMILIA: discutibles %d | preguntas %d | otras %d"
      % (len(discutibles), len(preguntas), len(otras)))
    w("   DE LOS DISCUTIBLES: A FAVOR %d | EN CONTRA %d | otro estado %d"
      % (len(a_favor), len(en_contra),
         len(discutibles) - len(a_favor) - len(en_contra)))
    sin_sentido = [a for a in discutibles if a[2] not in ("A FAVOR", "EN CONTRA")]
    if sin_sentido:
        w("   PARADA: hay %d discutible(s) cuyo estado no es ni A FAVOR ni EN CONTRA:"
          % len(sin_sentido))
        for a in sin_sentido:
            w("      %s -> %s" % (a[0], a[4][:120]))
        print(NL.join(salida))
        return 1
    w("   EL CERO DE `EN CONTRA` ES UN RESULTADO Y NO UNA PARADA. La guarda VIEJA")
    w("   de la 190 (`if not en_contra: PARADA`) corrida sobre esta acta: %s"
      % ("PARARIA" if not en_contra else "no pararia"))
    w("   Y NO SE VUELVE A FABRICAR SU CASO: EL ARNES DE LA 191 YA LO CUBRE, Y AQUI")
    w("   SE MIDE SU FICHERO EN VEZ DE CREERLO.")
    p_arnes = os.path.join(RAIZ, ARNES_QUE_YA_CUBRE.replace("/", os.sep))
    if not os.path.exists(p_arnes):
        w("   PARADA: %s NO EXISTE. Una ruta que promete prueba y no existe es"
          % ARNES_QUE_YA_CUBRE)
        w("   CAIDA DE CIFRA (EJECUTOR.md 1), y no se cita.")
        print(NL.join(salida))
        return 1
    datos_arnes = io.open(p_arnes, "rb").read()
    lf_arnes = datos_arnes.replace(b"\r\n", b"\n")
    t_arnes = lf_arnes.decode("utf-8", errors="replace")
    ver_arnes = [l.strip() for l in t_arnes.split(NL) if l.strip().startswith("VEREDICTO")]
    w("   %s -> disco %d bytes | LF %d bytes"
      % (ARNES_QUE_YA_CUBRE, len(datos_arnes), len(lf_arnes)))
    w("   sha256 LF: %s" % hashlib.sha256(lf_arnes).hexdigest())
    w("   su veredicto, leido del propio fichero: %r"
      % (ver_arnes[0] if ver_arnes else "(sin linea de veredicto)"))
    w("   la aguja `EN CONTRA` aparece %d vez(ces) en el arnes"
      % t_arnes.upper().count("EN CONTRA"))
    if len(datos_arnes) == 0 or not ver_arnes or "VERDE" not in ver_arnes[0]:
        w("   PARADA: el arnes que se cita como cobertura mide cero bytes o no sale")
        w("   verde. Una ruta que promete prueba sobre un vacio es CAIDA DE CIFRA.")
        print(NL.join(salida))
        return 1
    if not preguntas:
        w("   PARADA: ninguna adjudicacion nombra un `P.n` y el acta 192 declara TRES")
        w("   preguntas contestadas. No se escribe una lista vacia.")
        print(NL.join(salida))
        return 1
    w("")

    w("D.1) EL ORDEN DE LOS `D.n` EN EL REPORTE DE LA 191, MEDIDO Y NO CREIDO")
    w("   (el encargo avisa de que el `D.7` va escrito ANTES del `D.6`)")
    w("   SE MIDE CON DOS VARAS Y SE PUBLICAN LAS DOS, porque no dan lo mismo:")
    w("      VARA A, MENCION SUELTA: el primer sitio del fichero donde aparece la")
    w("         clave, sea en prosa, en una tabla o en un titulo.")
    w("      VARA B, TITULO DEL DISCUTIBLE: la linea que EMPIEZA por la clave en")
    w("         negrita, que es donde el reporte declara cada discutible.")
    w("      LA QUE CONTESTA AL ENCARGO ES LA B: el encargo habla de como estan")
    w("         ESCRITOS los discutibles, no de donde se les nombra de pasada.")
    r191 = os.path.join(LOOP, "reportes", "REPORTE_V191.md")
    orden_dn = []
    orden_suelto = []
    if os.path.exists(r191):
        t191 = io.open(r191, encoding="utf-8", errors="replace").read().replace(
            chr(13) + NL, NL)
        sueltos_v, titulos_v = {}, {}
        pat_titulo = re.compile(r"^\*\*`D\.(\d+)`")
        for i, l in enumerate(t191.split(NL), 1):
            for mm in re.finditer(r"`D\.(\d+)`", l):
                sueltos_v.setdefault(mm.group(1), i)
            mt = pat_titulo.match(l)
            if mt:
                titulos_v.setdefault(mt.group(1), i)
        orden_suelto = sorted(sueltos_v.items(), key=lambda kv: kv[1])
        orden_dn = sorted(titulos_v.items(), key=lambda kv: kv[1])
        w("   VARA A (mencion suelta): %s"
          % ", ".join("D.%s@%d" % (k, ln) for k, ln in orden_suelto))
        w("   VARA B (titulo del discutible): %s"
          % ", ".join("D.%s@%d" % (k, ln) for k, ln in orden_dn))
    else:
        w("   NO EXISTE docs/loop/reportes/REPORTE_V191.md")
    pos_s = dict(orden_suelto)
    pos = dict(orden_dn)
    d7_suelto = ("7" in pos_s and "6" in pos_s and pos_s["7"] < pos_s["6"])
    d7_antes = ("7" in pos and "6" in pos and pos["7"] < pos["6"])
    w("   EL AVISO DEL ENCARGO (`D.7` antes que `D.6`) POR LA VARA A: %s"
      % ("CALZA" if d7_suelto else "NO CALZA"))
    w("   EL AVISO DEL ENCARGO (`D.7` antes que `D.6`) POR LA VARA B: %s"
      % ("CALZA" if d7_antes else "NO CALZA"))
    w("   LAS DOS SE PUBLICAN Y NO SE ELIGE LA QUE CONVIENE: la vara A mete en la")
    w("   cuenta la tabla de tareas de la cabecera, donde `D.1` y `D.6` se nombran")
    w("   en la misma linea, y por eso no puede ordenar dos claves que comparten")
    w("   renglon. LA VARA B ES LA QUE RESPONDE A LA PREGUNTA QUE EL ENCARGO HACE.")
    w("   (y esto NO cambia ninguna cuenta: las adjudicaciones se leen del acta por")
    w("    su clave `4.n`, no por el orden del reporte)")
    w("")

    w("E) LOS HALLAZGOS DE LA SECCION %d, Y CUANTOS CUENTAN FUERA DEL MARCADO"
      % SECCION_DE_LOS_HALLAZGOS)
    claves_h = claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_HALLAZGO)
    hallazgos = []
    for clave, _n in claves_h:
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, err3 = titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err3:
            w("   %s -> %s" % (clave, err3))
            print(NL.join(salida))
            return 1
        hallazgos.append((clave, res[0], res[1]))
        w("   %-5s linea %-6d %s" % (clave, res[0], res[1][:120]))
    if not hallazgos:
        w("   PARADA: la seccion %d no trae ninguna clave `5.n`."
          % SECCION_DE_LOS_HALLAZGOS)
        print(NL.join(salida))
        return 1
    fila_fuera = fila_de_la_metrica(lineas, inicio, fin, AGUJA_FILA_FUERA)
    for ln, txt in fila_fuera:
        w("   LA FILA QUE DECIDE (linea %d): %s" % (ln, txt))
    if len(fila_fuera) != 1:
        w("   PARADA: la fila %r aparece %d veces en la tabla de credito."
          % (AGUJA_FILA_FUERA, len(fila_fuera)))
        print(NL.join(salida))
        return 1
    n1, s1, piezas_pyc = hallazgos_que_la_tabla_nombra(hallazgos, fila_fuera[0][1],
                                                       separadores=(";",))
    nombrados, sueltos, piezas = hallazgos_que_la_tabla_nombra(hallazgos,
                                                               fila_fuera[0][1])
    w("   PARTIENDO SOLO POR `;` (la maquina de la 190): %d pieza(s), casan %d"
      % (len(piezas_pyc), len(n1)))
    w("      %s" % ", ".join(repr(x) for x in piezas_pyc))
    w("   PARTIENDO POR `;` Y POR `,`: %d pieza(s), casan %d"
      % (len(piezas), len(nombrados)))
    w("      %s" % ", ".join(repr(x) for x in piezas))
    for clave, ln, tit, casan in nombrados:
        w("      %s (linea %d) casa por %s"
          % (clave, ln, ", ".join(repr(x) for x in casan)))
    w("   LOS QUE LA SUBCADENA NO NOMBRA: %d (%s)"
      % (len(sueltos), ", ".join(c for c, _l, _t in sueltos) or "ninguno"))
    numeral = numeral_de_la_fila(fila_fuera[0][1])
    w("   EL NUMERAL DE LA PROPIA FILA, LEIDO Y NO TECLEADO: %s" % numeral)
    if numeral is None:
        w("   PARADA: la fila no trae cifra en su celda. Una cifra que no se puede")
        w("   leer no se inventa.")
        print(NL.join(salida))
        return 1
    if numeral == len(hallazgos):
        n_fuera = len(hallazgos)
        w("   EL NUMERAL CALZA CON LAS CLAVES `5.n` DE LA SECCION (%d = %d), asi que"
          % (numeral, len(hallazgos)))
        w("   los %d cuentan fuera del marcado. El cotejo por subcadena queda al lado"
          % n_fuera)
        w("   como lo que es: una medicion mas debil, que solo resuelve %d de %d."
          % (len(nombrados), len(hallazgos)))
    elif numeral == len(nombrados):
        n_fuera = len(nombrados)
        w("   EL NUMERAL CALZA CON LOS QUE LA SUBCADENA NOMBRA (%d), y son esos."
          % numeral)
    else:
        w("   PARADA: el numeral dice %d, las claves `5.n` son %d y la subcadena"
          % (numeral, len(hallazgos)))
        w("   nombra %d. Ninguna de las dos vias resuelve, y no se elige a ojo."
          % len(nombrados))
        print(NL.join(salida))
        return 1
    w("")

    w("F) LAS CAIDAS. AQUI ES DONDE SE ROMPEN LAS MAQUINAS HEREDADAS, Y SE MIDE")
    r6 = rango_de_seccion(lineas, inicio, fin, SECCION_DE_LAS_CAIDAS)
    if r6 is None:
        w("   PARADA: el acta no tiene seccion %d." % SECCION_DE_LAS_CAIDAS)
        print(NL.join(salida))
        return 1
    ini6, fin6 = r6
    cabecera6 = lineas[ini6 - 1].strip()
    w("   la seccion %d va de la linea %d a la %d"
      % (SECCION_DE_LAS_CAIDAS, ini6, fin6))
    w("   SU CABECERA, LITERAL: %r" % cabecera6)
    n_c_crudo = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_C)
    n_c_espacio = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_C_ESPACIO)
    l_aud_a = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_A)
    l_rep = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_REPORTE)
    l_eje_v = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_EJECUTOR_VIEJO)
    texto6 = " ".join(lineas[ini6 - 1:fin6])
    n_c_en_linea_s6 = len(set(PAT_C_EN_LINEA.findall(texto6)))
    w("   patron `C.n` EN LINEA (el de la 190) sobre la seccion 6: %d"
      % n_c_en_linea_s6)
    w("   patron `C.n` de cabeza de linea de la 187 sobre el acta: %d" % len(n_c_crudo))
    w("   patron `C.n` de cabeza de linea de la 188 sobre el acta: %d" % len(n_c_espacio))
    w("   patron `A.n` de cabecera de tercer nivel (acta 185): %d" % len(l_aud_a))
    w("   patron `R.n` de caida de reporte: %d" % len(l_rep))
    w("   patron `E.n` de las actas 182 y 184: %d" % len(l_eje_v))
    v190 = caidas_en_linea(lineas, ini6, fin6)
    v189 = caidas_por_seccion(lineas, ini6, fin6)
    v191 = caidas_por_numeral(lineas, ini6, fin6)
    w("   LAS TRES MAQUINAS VIEJAS SOBRE ESTA SECCION, QUE ES DONDE SE ROMPEN:")
    w("      caidas_en_linea() de la 190: ejecutor %d | auditor %d | huerfanas %d"
      % (len(v190[0]), len(v190[1]), len(v190[2])))
    w("      caidas_por_seccion() de la 189: ejecutor %d | auditor %d | huerfanas %d"
      % (len(v189[0]), len(v189[1]), len(v189[2])))
    w("      caidas_por_numeral() de la 191: ejecutor %d | auditor %d | huerfanas %d"
      % (len(v191[0]), len(v191[1]), len(v191[2])))
    for ln, k, neg in v190[2]:
        w("         la 190 deja HUERFANA la %s bajo la negrita %r" % (k, neg[:70]))
    c_eje, c_aud, huerfanas = caidas_por_lead_heredado(lineas, ini6, fin6)
    w("   CON LA MAQUINA DE ESTA VUELTA (clave `C.n` + lead heredado):")
    w("      DEL EJECUTOR: %d clave(s) literal(es)" % len(c_eje))
    for ln, k, neg, her in c_eje:
        w("         %s en el parrafo de la linea %d, heredada: %s, bajo %r"
          % (k, ln, her, neg[:60]))
    w("      DEL AUDITOR: %d" % len(c_aud))
    for ln, k, neg, her in c_aud:
        w("         %s en el parrafo de la linea %d, heredada: %s, bajo %r"
          % (k, ln, her, neg[:60]))
    w("      HUERFANAS: %d" % len(huerfanas))
    for ln, k, neg, her in huerfanas:
        w("         %s en el parrafo de la linea %d, bajo %r" % (k, ln, neg[:70]))
    if huerfanas:
        w("   PARADA: hay %d caida(s) en un parrafo cuya negrita no dice de quien"
          % len(huerfanas))
        w("   son y sin lead previo que heredar. Una caida sin dueno no se reparte")
        w("   a ojo.")
        print(NL.join(salida))
        return 1
    if not c_aud:
        w("   PARADA: no se encuentra ninguna caida propia del auditor y el acta 192")
        w("   declara DOS, escritas como dos y ninguna omitida.")
        print(NL.join(salida))
        return 1
    parrafos6 = parrafos_con_negrita(lineas, ini6, fin6)
    negrita_eje = c_eje[0][2] if c_eje else ""
    lead_aud = ""
    for _a, _b, neg, _t in parrafos6:
        if any(x in neg.upper() for x in MARCAS_LEAD_AUDITOR):
            lead_aud = neg
            break
    w("   la negrita del lead del auditor, literal: %r" % lead_aud)
    w("   la negrita del lead del ejecutor, literal: %r" % negrita_eje)
    w("")
    w("   EL RANGO DEL EJECUTOR, EXPANDIDO Y NO CONTADO POR CLAVES DISTINTAS:")
    texto_eje = ""
    for _a, _b, neg, txt in parrafos6:
        if any(x in neg.upper() for x in MARCAS_LEAD_EJECUTOR):
            texto_eje = txt
            break
    lit_eje, exp_eje = expandir_rangos_de_clave(texto_eje)
    w("      claves LITERALES del parrafo del ejecutor: %d (%s)"
      % (len(lit_eje), ", ".join("C.%d" % x for x in lit_eje) or "ninguna"))
    w("      claves con el RANGO EXPANDIDO: %d (%s)"
      % (len(exp_eje), ", ".join("C.%d" % x for x in exp_eje) or "ninguna"))
    fila_metodo = fila_de_la_metrica(lineas, inicio, fin, AGUJA_FILA_CAIDAS_METODO)
    fila_aud = fila_de_la_metrica(lineas, inicio, fin, AGUJA_FILA_CAIDAS_AUDITOR)
    for ln, txt in fila_aud + fila_metodo:
        w("      POR LA TABLA (linea %d): %s" % (ln, txt))
    if not fila_aud or not fila_metodo:
        w("   PARADA: la tabla de credito no trae alguna de las dos filas de caidas.")
        print(NL.join(salida))
        return 1
    numeral_metodo = numeral_de_la_fila(fila_metodo[0][1])
    numeral_aud = numeral_de_la_fila(fila_aud[0][1])
    w("      EL NUMERAL DE LA FILA DE METODO, LEIDO Y NO TECLEADO: %s" % numeral_metodo)
    w("      EL NUMERAL DE LA FILA DE CAIDAS PROPIAS, LEIDO: %s" % numeral_aud)
    if numeral_metodo is None or numeral_aud is None:
        w("   PARADA: una de las dos filas no trae cifra legible en su celda.")
        print(NL.join(salida))
        return 1
    if len(exp_eje) != numeral_metodo:
        w("   PARADA: el rango expandido da %d y el numeral de la fila dice %d."
          % (len(exp_eje), numeral_metodo))
        w("   No se elige a ojo cual de las dos vale.")
        print(NL.join(salida))
        return 1
    w("      EL RANGO EXPANDIDO CALZA CON EL NUMERAL DE LA FILA (%d = %d)."
      % (len(exp_eje), numeral_metodo))
    if len(c_aud) != numeral_aud:
        w("   PARADA: el auditor declara %d caidas propias por parrafo y su fila de"
          % len(c_aud))
        w("   la tabla dice %d." % numeral_aud)
        print(NL.join(salida))
        return 1
    w("      LAS CAIDAS PROPIAS DEL AUDITOR CALZAN CON SU FILA (%d = %d)."
      % (len(c_aud), numeral_aud))
    w("")
    w("   LA ESPECIE DE CADA CAIDA PROPIA, LEIDA DEL PARRAFO Y NO SUPUESTA:")
    especies_aud = []
    for a, _b, neg, txt in parrafos6:
        ks = sorted(set(int(x) for x in PAT_CLAVE_C.findall(neg)))
        if not ks:
            continue
        esp = especie_de_la_caida(txt)
        for k in ks:
            especies_aud.append(("C.%d" % k, a, esp))
        w("      %s (linea %d) -> %s"
          % (", ".join("C.%d" % k for k in ks), a,
             ", ".join(esp) or "NINGUNA"))
    sin_especie = [x for x in especies_aud if not x[2]]
    if not especies_aud or sin_especie:
        w("   PARADA: hay %d caida(s) propia(s) sin especie declarada en su parrafo."
          % len(sin_especie))
        print(NL.join(salida))
        return 1
    con_cifra = [x for x in especies_aud if MARCA_ESPECIE_CIFRA in x[2]]
    w("      CIFRA de las propias que son %r: %d (%s)"
      % (MARCA_ESPECIE_CIFRA, len(con_cifra),
         ", ".join(k for k, _l, _e in con_cifra) or "ninguna"))
    if not con_cifra:
        w("   PARADA: el encargo dice que UNA de las dos caidas propias es DE CIFRA")
        w("   PUBLICADA, y ningun parrafo lo declara. No se supone.")
        print(NL.join(salida))
        return 1
    confundido = caidas_por_lead_heredado(
        lineas, ini6, fin6,
        marcas_cero_cuenta=(MARCAS_CERO_DE_CUENTA + MARCAS_CERO_DE_RACHA))
    w("   TRATANDO EL CERO DE RACHA COMO CERO DE CUENTA: ejecutor %d | auditor %d"
      % (len(confundido[0]), len(confundido[1])))
    w("   O SEA QUE CONFUNDIRLAS BORRARIA %d CLAVE(S) DE LA CUENTA."
      % (len(c_eje) - len(confundido[0])))
    n_metodo = len([1 for _a, _b, _n, t in parrafos6
                    if MARCA_ESPECIE_METODO in t.upper()])
    w("   la marca de especie %r aparece en %d de los %d parrafos de la seccion"
      % (MARCA_ESPECIE_METODO, n_metodo, len(parrafos6)))
    if not n_metodo:
        w("   PARADA: ningun parrafo declara la especie de las caidas.")
        print(NL.join(salida))
        return 1
    w("")

    w("G) LA METRICA DE CREDITO DE LA SECCION %d, ENTERA" % SECCION_DE_LA_METRICA)
    r7 = rango_de_seccion(lineas, inicio, fin, SECCION_DE_LA_METRICA)
    if r7 is None:
        w("   PARADA: el acta no tiene seccion %d." % SECCION_DE_LA_METRICA)
        print(NL.join(salida))
        return 1
    filas7 = filas_de_la_metrica(lineas, r7[0], r7[1])
    w("   la seccion %d va de la linea %d a la %d"
      % (SECCION_DE_LA_METRICA, r7[0], r7[1]))
    w("   CIFRA filas de datos: %d" % len(filas7))
    for ln, txt in filas7:
        w("      LINEA %-6d %s" % (ln, txt))
    if not filas7:
        w("   PARADA: la tabla de credito no trae ninguna fila de datos.")
        print(NL.join(salida))
        return 1
    fila_p = fila_de_la_metrica(lineas, inicio, fin, AGUJA_FILA_PUESTOS)
    w("   LA FILA DE PUESTOS, QUE EL ENCARGO MANDA REGISTRAR CON SU NOTA: %d"
      % len(fila_p))
    for ln, txt in fila_p:
        w("      LINEA %-6d %s" % (ln, txt))
    nota_exacta = bool(fila_p) and NOTA_DE_PUESTOS in fila_p[0][1]
    nota = bool(fila_p) and NOTA_DE_PUESTOS in fila_p[0][1].upper()
    literal = ""
    if fila_p:
        mm = re.search(r"(?i)(solape\s+total)", fila_p[0][1])
        literal = mm.group(1) if mm else ""
    w("   el literal %r aparece TAL CUAL en la fila de puestos: %s"
      % (NOTA_DE_PUESTOS, "SI" if nota_exacta else "NO"))
    w("   comparado en mayusculas: %s" % ("SI" if nota else "NO"))
    w("   LO QUE EL ACTA ESCRIBE DE VERDAD, LEIDO Y NO PARAFRASEADO: %r" % literal)
    if not nota:
        w("   PARADA: el encargo pide registrar la fila de puestos CON SU NOTA de")
        w("   solape total, y la fila no la trae. Una nota que no esta no se")
        w("   parafrasea.")
        print(NL.join(salida))
        return 1
    w("")

    w("H) EL NUMERO DE LA ENTRADA, QUE NO SE TECLEA")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    w("   serie recomputada de sus dos sedes: %d entradas" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SERIE.colisiones(halladas)), len(SERIE.huecos(halladas))))
    w("   SIGUIENTE LIBRE: R.%d" % numero)
    w("   el encargo adelanta R.54 -> %s"
      % ("CALZA" if numero == 54 else "NO CALZA, y la discrepancia se declara"))
    w("")

    w("I) LA DEUDA DE LA SERIE, REMEDIDA AQUI Y NO HEREDADA")
    salto = actas_sin_entrada(halladas, 173, VUELTA_DEL_ACTA - 1)
    faltan, bajo, alto = salto
    w("   tramo mirado: actas 173 a %d" % (VUELTA_DEL_ACTA - 1))
    w("   CIFRA actas SIN entrada propia en la serie: %d" % len(faltan))
    w("   LAS QUE FALTAN: %s" % (", ".join(str(x) for x in faltan) or "(ninguna)"))
    w("   EXTREMO BAJO: %s"
      % ("R.%d cubre el acta %d" % bajo if bajo else "(ninguno)"))
    w("   EXTREMO ALTO: %s"
      % ("R.%d cubre el acta %d" % alto if alto else "(ninguno)"))
    w("   el encargo dice OCHO (173 a 180) -> %s"
      % ("CALZA" if len(faltan) == 8 else "NO CALZA, y la discrepancia se declara"))
    w("")

    medido = {
        "inicio": inicio, "fin": fin, "secciones": secciones,
        "n_adj": len(claves), "n_entrecomillado": len(entrecomilladas),
        "adjudicaciones": adjudicaciones,
        "n_discutibles": len(discutibles), "n_preg": len(preguntas),
        "n_otras": len(otras), "n_a_favor_discutibles": len(a_favor),
        "n_en_contra_discutibles": len(en_contra),
        "n_discutibles_sin_sentido": len(sin_sentido),
        "vieja_pararia": not en_contra,
        "n_sin_decir_vieja": n_sin_decir_vieja,
        "arnes_disco": len(datos_arnes), "arnes_lf": len(lf_arnes),
        "arnes_veredicto": ver_arnes[0] if ver_arnes else "",
        "orden_dn": orden_dn, "d7_antes_del_d6": d7_antes,
        "orden_suelto": orden_suelto, "d7_suelto": d7_suelto,
        "preguntas": [(c, PAT_P_DEL_TITULO.search(t).group(0).strip("`"))
                      for c, _f, _e, _l, t in preguntas],
        "hallazgos": hallazgos, "n_hall": len(hallazgos),
        "hall_nombrados": nombrados,
        "claves_nombradas": set(c for c, _l, _t, _k in nombrados),
        "piezas_fuera": piezas, "fila_fuera": fila_fuera,
        "n_piezas": len(piezas), "n_piezas_pyc": len(piezas_pyc),
        "n_casan_pyc": len(n1), "numeral_fila": numeral, "n_fuera": n_fuera,
        "cabecera_seccion6": cabecera6,
        "c_eje": c_eje, "c_aud": c_aud,
        "n_eje_literal": len(c_eje), "n_eje": len(exp_eje),
        "n_aud": len(c_aud), "n_huerf": len(huerfanas),
        "n_aud_heredadas": len([1 for _l, _k, _n, h in c_aud if h]),
        "negrita_eje": negrita_eje, "negrita_aud_lead": lead_aud,
        "especies_aud": especies_aud,
        "v190_eje": len(v190[0]), "v190_aud": len(v190[1]),
        "v190_huerf": len(v190[2]),
        "v189_eje": len(v189[0]), "v189_aud": len(v189[1]),
        "v189_huerf": len(v189[2]),
        "v191_eje": len(v191[0]), "v191_aud": len(v191[1]),
        "v191_huerf": len(v191[2]),
        "numeral_metodo": numeral_metodo, "numeral_aud": numeral_aud,
        "cero_confundido_eje": len(confundido[0]),
        "n_parrafos_metodo": n_metodo, "n_parrafos6": len(parrafos6),
        "n_c_crudo": len(n_c_crudo), "n_c_espacio": len(n_c_espacio),
        "n_c_en_linea_s6": n_c_en_linea_s6,
        "filas7": filas7, "n_filas7": len(filas7),
        "fila_puestos": fila_p, "nota_de_puestos": nota,
        "nota_exacta": nota_exacta, "nota_literal": literal,
        "fila_aud": fila_aud, "fila_metodo": fila_metodo,
        "salto": salto, "numero": numero, "ya_registrada": len(ya),
        "sedes": sedes,
    }
    return salida, medido


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true",
                    help="mide y arma la entrada, pero NO escribe en la sede")
    ap.add_argument("--mutacion", action="store_true",
                    help="corre el caso positivo por mutacion y no toca nada")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    if a.mutacion:
        return prueba_de_mutacion()

    medido = _medir()
    if isinstance(medido, int):
        return medido
    salida, m = medido
    w = salida.append

    w("J) EL TITULO, CON SUS CINCO NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(m["n_adj"], m["n_hall"], m["n_preg"],
                                  m["n_aud"], m["n_eje"])
    w("   %s" % titulo)
    w("")

    numero = m["numero"]
    entrada = armar_entrada(numero, titulo, m)
    w("K) LA ENTRADA ARMADA")
    w("   %d bytes | %d lineas por count(NL) | %d por len(split(NL))"
      % (len(entrada.encode("utf-8")), entrada.count(NL), len(entrada.split(NL))))
    w("   guiones largos o medios en la entrada: %d"
      % (entrada.count(chr(8212)) + entrada.count(chr(8211))))
    w("")

    texto_sede = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    if a.simular:
        w("L) MODO --simular: NO SE ESCRIBE NADA EN LA SEDE.")
        w("")
        w("LA ENTRADA, ENTERA:")
        for l in entrada.split(NL):
            w("   | " + l)
    elif m["ya_registrada"]:
        w("L) NO SE ESCRIBE NADA, Y ESTA ES LA IDEMPOTENCIA HACIENDO SU TRABAJO.")
        w("   el acta %d YA TIENE ENTRADA en la serie: %d linea(s) la nombran."
          % (VUELTA_DEL_ACTA, m["ya_registrada"]))
        w("   NO se escribe una entrada nueva y NO se consume el numero R.%d." % numero)
        w("   docs/PENDIENTES.md sigue en %d bytes." % os.path.getsize(SEDE))
    else:
        nuevo = texto_sede.rstrip(NL) + NL + NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("L) ESCRITA EN docs/PENDIENTES.md")
        w("   la sede pasa de %d a %d bytes"
          % (len(texto_sede.encode("utf-8")), len(nuevo.encode("utf-8"))))
        rele = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
        w("   RELEIDA DEL DISCO: la entrada esta byte a byte: %s"
          % ("SI" if entrada.rstrip(NL) in rele else "NO"))
        de_nuevo = SERIE.entradas()
        w("   SERIE RECOMPUTADA DESPUES DE ESCRIBIR: %d entradas, siguiente libre R.%d"
          % (len(de_nuevo), SERIE.siguiente_libre(de_nuevo)))
        w("   CIFRA colisiones: %d | CIFRA huecos: %d"
          % (len(SERIE.colisiones(de_nuevo)), len(SERIE.huecos(de_nuevo))))
        sedes2 = {}
        for ruta in SERIE.SEDES:
            rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
            sedes2[rel] = io.open(ruta, encoding="utf-8", errors="replace").read()
        w("   Y LA IDEMPOTENCIA, REMEDIDA DESPUES DE ESCRIBIR: el acta %d aparece en"
          % VUELTA_DEL_ACTA)
        w("   %d linea(s), asi que un RE CORRIDO de este instrumento no escribiria"
          % len(entradas_que_registran(VUELTA_DEL_ACTA, sedes2)))
        w("   nada.")
    w("")
    t = NL.join(salida) + NL
    if a.simular:
        nombre = "SALIDA_V%s_T1A_SIMULACION.txt" % SUFIJO_QUE_ESCRIBE
    elif m["ya_registrada"]:
        nombre = "SALIDA_V%s_T1A_RECORRIDO_SIN_ESCRIBIR.txt" % SUFIJO_QUE_ESCRIBE
    else:
        nombre = "SALIDA_V%s_T1A_REGISTRO_R%d.txt" % (SUFIJO_QUE_ESCRIBE, numero)
    ruta = os.path.join(LOOP, nombre)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
