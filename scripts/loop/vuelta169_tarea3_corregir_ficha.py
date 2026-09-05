# -*- coding: utf-8 -*-
r"""vuelta169_tarea3_corregir_ficha.py . LA CORRECCION DE LA NOTA DE `OP-I-01`
POR EL CARRIL DEL BANCO 9.10 (TAREA 3.b y 3.c de la vuelta 169).

QUE CORRIGE, Y NO LO RESUELVE COPIANDO. La nota de la ficha declara, verbatim:
*"Al corte 3.388, docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl mide TRESCIENTOS
TREINTA Y CINCO actos (335), verificado por conteo directo de lineas del archivo
(280 CERRADOS, 55 ABIERTOS)"*. **Contado hoy ese mismo fichero: 332 lineas, 278
CERRADOS y 54 ABIERTOS.** La cifra vieja se TACHA y se queda ENTERA; la nueva se
pone al lado con su corte; y la nota fechada explica de donde viene la bajada.

Y ANADE LO QUE LA 3.b MANDA DECLARAR Y NO RECOMPUTAR: `familia_de_ids`, `figura`,
`defecto` y `dominio`, con su cifra de hoy y con la frase de que el disparador de
`08_VERIFICACION` no las alcanza (su paso 4 nombra *"cada racimo y cada acto"* y
nada mas).

Y TRAE UNA TERCERA COSA QUE EL ENCARGO NO ANTICIPA Y QUE NO SE CALLA: correr
`scripts/plan/recomputo_3388.py` HOY sobre el grafo vivo da **47 componentes**,
no 332. No es que el fichero sellado este mal: es que **la campana FUNDIO** desde
que se sello, y cada acto fundido convierte sus pares `A` internos en
auto-aristas que dejan de formar componente. La aritmetica lo sostiene sola y va
escrita en la nota.

EL CONTADOR, Y SE DICE LA VERDAD SOBRE EL. La fila de los colapsos de
`RECOMPUTO_3388.md` lleva un contador mecanico `[CORREGIDA N VECES]` que se cuadra
en el mismo acto. **ESTA NOTA NO TIENE ESA CONVENCION**: sus correcciones previas
se escribieron en prosa, sin contador. Asi que aqui el ordinal se COMPUTA contando
las marcas de correccion que la nota ya trae, y se DECLARA que se computo asi y
que la nota no tenia contador previo. Inventar un contador retroactivo seria
reescribir historia; no ponerlo seria dejar la cadena sin contar.

CERO CAMPOS NUEVOS DE ESQUEMA: se escribe DENTRO del campo `nota` que ya existe,
como hicieron las correcciones de las vueltas 14, 15, 16 y 17 de esta misma ficha.

USO:
  python scripts/loop/vuelta169_tarea3_corregir_ficha.py
  python scripts/loop/vuelta169_tarea3_corregir_ficha.py --comprobar
"""
import collections
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
INVENTARIO = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
COMPONENTES = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388_COMPONENTES.jsonl")
# La corrida de HOY, escrita por scripts/loop/vuelta169_tarea3_op_i_01.py. Su ruta
# es configurable por el mismo motivo que alli: mientras la bateria de mutaciones
# corre, nada nuevo aparece en docs/loop/.
RECOMPUTO_HOY = os.environ.get(
    "V169_RECOMPUTO_SALIDA",
    os.path.join(RAIZ, "docs", "loop", "RECOMPUTO_V169.jsonl"))
# LA SALIDA DE LA MEDICION 3.a. Las cuatro cifras del re medido (vigentes, las que
# calzan, las que difieren y las que no tienen componente) SE CUENTAN DE ESTE
# FICHERO y no se teclean: EJECUTOR.md 1, "LA TABLA SE CUENTA DE SU FICHERO".
SALIDA_3A = os.environ.get(
    "V169_SALIDA_T3",
    os.path.join(RAIZ, "docs", "loop", "SALIDA_V169_T3_OP_I_01.txt"))

FICHA = "OP-I-01"
VIEJA = ("Al corte 3.388, docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl mide "
         "TRESCIENTOS TREINTA Y CINCO actos (335), verificado por conteo directo "
         "de lineas del archivo (280 CERRADOS, 55 ABIERTOS).")

ORDINAL = {1: "PRIMERA", 2: "SEGUNDA", 3: "TERCERA", 4: "CUARTA", 5: "QUINTA",
           6: "SEXTA", 7: "SEPTIMA", 8: "OCTAVA", 9: "NOVENA", 10: "DECIMA",
           11: "UNDECIMA", 12: "DUODECIMA", 13: "DECIMOTERCERA"}

# LAS MARCAS DE CORRECCION QUE ESTA NOTA YA TRAE. Se cuentan, no se teclean, y se
# listan aqui para que el conteo sea auditable en vez de magico.
MARCAS = ("CORRECCION DECLARADA", "ETIQUETA CORREGIDA", "CORREGIDO EN LA VUELTA",
          "RECOMPUTO EJECUTADO", "REGENERACION APROBADA",
          "HUECO NOMBRADO Y REGISTRADO")


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    solo_medir = "--comprobar" in sys.argv
    print("=" * 78)
    print("VUELTA 169, TAREA 3.b y 3.c: LA NOTA DE OP-I-01, CORREGIDA POR EL 9.10")
    print("=" * 78)
    print("")

    lineas = [l for l in io.open(OPERACIONES, encoding="utf-8") if l.strip()]
    fichas = [json.loads(l) for l in lineas]
    idx = [i for i, f in enumerate(fichas) if f.get("id_op") == FICHA]
    if len(idx) != 1:
        print("ROJO: %s aparece %d veces en OPERACIONES.jsonl" % (FICHA, len(idx)))
        return 1
    i = idx[0]
    ficha = fichas[i]
    nota = ficha.get("nota") or ""

    print("A) EL SUJETO, MEDIDO ANTES DE TOCARLO")
    print("   fichas en docs/plan/OPERACIONES.jsonl: %d" % len(fichas))
    print("   %s vive en la linea %d" % (FICHA, i + 1))
    print("   CIFRA claves de la ficha: %d" % len(ficha))
    print("   CIFRA caracteres de la nota: %d" % len(nota))
    print("   la frase vieja aparece EXACTAMENTE una vez: %s" % (nota.count(VIEJA) == 1))
    if nota.count(VIEJA) != 1:
        print("   ROJO: la frase que hay que tachar aparece %d veces. No se escribe."
              % nota.count(VIEJA))
        return 1
    print("")

    print("B) LAS CIFRAS DE HOY, CONTADAS DE SUS FICHEROS")
    comps = cargar(COMPONENTES)
    est = collections.Counter(c.get("estado") for c in comps)
    inv = cargar(INVENTARIO)
    por_tipo = collections.Counter(x.get("tipo") for x in inv)
    actos_vig = sum(1 for x in inv
                    if x.get("tipo") == "acto" and x.get("fecha_corte") == "2026-08-13")
    print("   docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl: %d lineas, %d CERRADO, %d ABIERTO"
          % (len(comps), est["CERRADO"], est["ABIERTO"]))
    print("   docs/plan/INVENTARIO.jsonl: %d entradas, %d actos vigentes al corte 2026-08-13"
          % (len(inv), actos_vig))
    for t in ("familia_de_ids", "figura", "defecto", "dominio"):
        print("   fuera del disparador: %-15s %d" % (t, por_tipo[t]))
    fuera = sum(por_tipo[t] for t in ("familia_de_ids", "figura", "defecto", "dominio"))
    print("   CIFRA total fuera del disparador: %d de %d" % (fuera, len(inv)))
    # LAS TRES CIFRAS DE LA CORRIDA DE HOY NO SE TECLEAN: SE CUENTAN DE SU FICHERO.
    # Si el fichero no esta, este instrumento PARA en vez de escribir un numeral
    # de memoria, que es exactamente la especie que la vuelta 168 costo.
    if not os.path.exists(RECOMPUTO_HOY):
        print("   ROJO: no existe %s. Corre antes scripts/loop/vuelta169_tarea3_op_i_01.py"
              % RECOMPUTO_HOY)
        return 1
    hoy = cargar(RECOMPUTO_HOY)
    est_hoy = collections.Counter(c.get("estado") for c in hoy)
    n_hoy, cer_hoy, abi_hoy = len(hoy), est_hoy["CERRADO"], est_hoy["ABIERTO"]
    print("   corrida de HOY (%s): %d componentes, %d CERRADO, %d ABIERTO"
          % (os.path.basename(RECOMPUTO_HOY), n_hoy, cer_hoy, abi_hoy))
    if not os.path.exists(SALIDA_3A):
        print("   ROJO: no existe %s. La 3.a no se puede citar de memoria." % SALIDA_3A)
        return 1
    sal = io.open(SALIDA_3A, encoding="utf-8").read()
    def cifra(patron):
        m = re.search(patron, sal)
        return int(m.group(1)) if m else None
    n_vig = cifra(r"CIFRA entradas vigentes re medidas: (\d+)")
    n_cal = cifra(r"CIFRA cuyas CIFRAS de cobertura calzan con su componente de hoy: (\d+)")
    n_dif = cifra(r"CIFRA cuyas CIFRAS de cobertura DIFIEREN de las de hoy: (\d+)")
    n_sin = cifra(r"CIFRA sin componente en el fichero sellado: (\d+)")
    print("   la 3.a, contada de %s: %s vigentes, %s calzan, %s difieren, %s sin componente"
          % (os.path.basename(SALIDA_3A), n_vig, n_cal, n_dif, n_sin))
    if None in (n_vig, n_cal, n_dif, n_sin):
        print("   ROJO: alguna de las cuatro cifras de la 3.a no se pudo leer.")
        return 1
    if n_cal + n_dif + n_sin != n_vig:
        print("   ROJO: las tres partes no suman el total: %d + %d + %d != %d"
              % (n_cal, n_dif, n_sin, n_vig))
        return 1
    print("   y las tres partes SUMAN el total: %d + %d + %d = %d"
          % (n_cal, n_dif, n_sin, n_vig))
    print("")

    print("C) EL ORDINAL, CONTADO DE LAS MARCAS QUE LA NOTA YA TRAE")
    cuenta = 0
    for m in MARCAS:
        n = nota.count(m)
        print("   %-30s %d" % (m, n))
        cuenta += n
    ordinal = ORDINAL[cuenta + 1]
    print("   CIFRA marcas de correccion contadas: %d" % cuenta)
    print("   ORDINAL de la que se escribe hoy, computado y no tecleado: %s" % ordinal)
    print("")

    nueva = (
        "~~%s~~ "
        "%s CORRECCION DECLARADA DE ESTA MISMA NOTA (4 sep 2026, vuelta 169, TAREA 3, "
        "por la adjudicacion 6.4 del acta 168 y por el carril del banco 9.10). "
        "EL ORDINAL NO ESTA TECLEADO: sale de contar las marcas de correccion que esta "
        "nota ya traia (%d), y SE DECLARA QUE ESTA NOTA NO TIENE CONTADOR MECANICO como "
        "la fila de los colapsos de RECOMPUTO_3388.md; sus correcciones previas se "
        "escribieron en prosa. Inventarle un contador retroactivo seria reescribir "
        "historia. LA CIFRA VIEJA QUEDA TACHADA Y ENTERA ARRIBA, NO SE BORRA. "
        "CONTADO HOY, linea a linea, sobre el MISMO fichero que la frase vieja nombra: "
        "docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl mide %d LINEAS, %d CERRADOS y %d "
        "ABIERTOS. La bajada de 335 a %d NO es un error de la cifra vieja: es de su "
        "corte, y esta trazada en el reporte de la vuelta 168 sobre los cuatro puntos "
        "en que la cifra baja (7f4ec6d9 335, 7cec9ecc 334, 97552714 333, 70878328 332), "
        "con la subida intermedia 78ea7799 334, 801c59f9 335, c8c4e0b3 334 anadida en "
        "la vuelta 169. "
        "Y SE SEPARA UNA COSA QUE LA FRASE VIEJA MEZCLABA: los %d actos SI existen, pero "
        "en docs/plan/INVENTARIO.jsonl, que hoy trae %d entradas de tipo acto con "
        "fecha_corte 2026-08-13. Lo que mide %d es el fichero de componentes. La frase "
        "vieja atribuia al fichero de componentes una cifra que es del inventario. "
        "TERCERA MEDICION, LA QUE NADIE HABIA CORRIDO Y QUE ESTA VUELTA CORRE: "
        "scripts/plan/recomputo_3388.py, ejecutado HOY sobre el grafo vivo, da %d "
        "COMPONENTES (%d CERRADO, %d ABIERTO), no %d. NO ES QUE EL FICHERO SELLADO ESTE "
        "MAL: es que la campana FUNDIO desde que se sello, y cada acto fundido convierte "
        "sus pares A internos en auto-aristas que dejan de formar componente. La "
        "aritmetica lo sostiene sola y se escribe entera: el paso 1 de hoy mide 551 A "
        "crudas, 398 que colapsan a auto-arista tras resolver y 149 pares distintos en "
        "el retrato; al corte en que se sello el fichero los colapsos eran 207 y los "
        "pares distintos 344. De 344 pares distintos salen 332 componentes; de 149 salen "
        "%d. LAS TRES CIFRAS SON CIERTAS Y CADA UNA ES DE SU CORTE, y por eso ninguna se "
        "copia encima de otra. "
        "(3.b) LO QUE EL DISPARADOR NO ALCANZA, DECLARADO Y NO RECOMPUTADO: el paso 4 "
        "de docs/plan/08_VERIFICACION.md (linea 397, leida hoy) dice 'cada racimo y cada "
        "acto se re-mide con su cobertura al lado (banco 9.26), usando las componentes "
        "del paso 3', y NO NOMBRA NADA MAS. Quedan por tanto FUERA de esta clausula, con "
        "su cifra de hoy y sin recomputar: familia_de_ids %d, figura %d, defecto %d y "
        "dominio %d, o sea %d de las %d entradas del inventario. NO SE INVENTAN Y NO SE "
        "RELLENAN, que es lo que la clausula 3 de esta misma ficha manda para todo hueco. "
        "(3.a) LO QUE SI SE RE MIDIO, y su resultado esta en "
        "docs/loop/SALIDA_V169_T3_OP_I_01.txt: las %d entradas VIGENTES de tipo acto y "
        "racimo, re medidas sobre las componentes del paso 3 con el resolutor delante "
        "por P.1. %d CALZAN en sus cifras de cobertura, %d difieren con motivo medido "
        "y %d no tienen componente en el fichero sellado. Y SE DICE QUE ES VIGENTE, "
        "porque partirlo por fecha_corte estaba MAL y se corrigio antes de publicar: la "
        "vara es la marca SUPERADA, que llevan los 221 actos viejos uno a uno y NINGUN "
        "racimo; partir por la fecha dejaba fuera once racimos del corte 2026-08-11 que "
        "NO estan superados. LO QUE ESTA CORRECCION NO HACE: "
        "no borra ninguna cifra vieja, no toca ni un nodo, no mueve el estado ni las "
        "dependencias de esta ficha ni de ninguna otra, no regenera el inventario y no "
        "autoriza ninguna lectura nueva."
        % (VIEJA, ordinal, cuenta, len(comps), est["CERRADO"], est["ABIERTO"],
           len(comps), actos_vig, actos_vig, len(comps),
           n_hoy, cer_hoy, abi_hoy, len(comps), n_hoy,
           por_tipo["familia_de_ids"], por_tipo["figura"], por_tipo["defecto"],
           por_tipo["dominio"], fuera, len(inv),
           n_vig, n_cal, n_dif, n_sin))

    nota_nueva = nota.replace(VIEJA, nueva, 1)

    print("D) LA NOTA SOLO CRECE, Y LO VIEJO SIGUE DENTRO")
    print("   CIFRA caracteres antes: %d" % len(nota))
    print("   CIFRA caracteres despues: %d" % len(nota_nueva))
    print("   crece y no encoge: %s" % (len(nota_nueva) > len(nota)))
    print("   la frase vieja sigue dentro, TACHADA: %s" % (("~~%s~~" % VIEJA) in nota_nueva))
    trozos_viejos = ["323 ENTRADAS: 221 actos", "EL TOTAL REAL NO ES 450: es 671",
                     "construccion_de_leverage", "HUECO NOMBRADO Y REGISTRADO EN LA VUELTA 17"]
    for t in trozos_viejos:
        print("   sigue dentro %-46s: %s" % ("'" + t[:42] + "'", t in nota_nueva))
    perdidos = [t for t in trozos_viejos if t not in nota_nueva]
    if perdidos or ("~~%s~~" % VIEJA) not in nota_nueva:
        print("   ROJO: se perdio texto viejo.")
        return 1
    print("")

    ficha_nueva = dict(ficha)
    ficha_nueva["nota"] = nota_nueva
    print("E) EL ESQUEMA NO CRECE Y NADA MAS SE MUEVE")
    print("   CIFRA claves antes: %d | despues: %d" % (len(ficha), len(ficha_nueva)))
    print("   estado antes: %r | despues: %r" % (ficha.get("estado"), ficha_nueva.get("estado")))
    print("   depende_de antes: %r | despues: %r"
          % (ficha.get("depende_de"), ficha_nueva.get("depende_de")))
    movidos = [k for k in ficha if k != "nota" and ficha[k] != ficha_nueva.get(k)]
    print("   CIFRA campos movidos ademas de `nota`: %d %s" % (len(movidos), movidos))
    if len(ficha_nueva) != len(ficha) or movidos:
        print("   ROJO: se movio algo que no era la nota.")
        return 1
    print("")

    if solo_medir:
        print("MODO --comprobar: NO se escribe.")
        return 0

    lineas[i] = json.dumps(ficha_nueva, ensure_ascii=False) + "\n"
    io.open(OPERACIONES, "w", encoding="utf-8", newline="\n").writelines(lineas)
    despues = cargar(OPERACIONES)
    print("F) ESCRITO, Y RECONTADO DESPUES DE ESCRIBIR")
    print("   CIFRA fichas antes: %d | despues: %d" % (len(fichas), len(despues)))
    print("   la ficha %s sigue en la linea %d: %s"
          % (FICHA, i + 1, despues[i].get("id_op") == FICHA))
    print("   CIFRA caracteres de la nota en disco: %d" % len(despues[i]["nota"]))
    if len(despues) != len(fichas) or despues[i].get("id_op") != FICHA:
        print("   ROJO: el fichero cambio de forma.")
        return 1
    print("")
    print("VERDE: la nota de %s corregida por adicion, cero palabras viejas borradas."
          % FICHA)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
