# -*- coding: utf-8 -*-
"""vuelta72_correccion_ficha_opl03.py . LA CORRECCION DECLARADA DE LA CLAUSULA DE
LA ERA DEL PAR EN LA VERIFICACION DE LA FICHA DE OP-L-03 (docs/plan/OPERACIONES.jsonl).

TAREA 1 del encargo de la vuelta 72, adjudicacion 3 del acta 71. NADA DEL GRAFO
SE TOCA: la correccion es DE REGISTRO. Ni un nodo, ni un alias, ni un campo del
catalogo. Ni un veredicto, ni el marcador.

QUE SE CORRIGE. La ficha de OP-L-03 lleva en su lista `verificacion` la clausula,
VERBATIM:

    ningun acto se funde con un par interno sin veredicto

UNA MEDICION QUE VA DELANTE DE TODO Y QUE NO SE HEREDA DEL ACTA, porque la regla
2 del ejecutor manda declarar la discrepancia en vez de resolverla copiando: el
acta 71 llama a esta clausula LA MISMA frase que el acta 65 adjudico para
OP-U-02. EN SUSTANCIA LO ES, y por eso la adjudicacion vale; AL BYTE NO LO ES, y
por eso este instrumento cita la de OP-L-03 y no la de OP-U-02. La de OP-U-02,
medida hoy por este mismo instrumento sobre el fichero, dice:

    el acto se leyo ENTERO antes de fundirse: cero pares internos sin veredicto

Las dos dicen LA MISMA REGLA con otras palabras (una en voz pasiva sobre la
lectura, la otra en voz activa sobre la fusion), y las dos fueron escritas en la
era en que la componente era el par. La diferencia de bytes se MIDE aqui y se
imprime, y el instrumento cae en ROJO si la de OP-L-03 no esta verbatim: no se
corrige lo que no se pudo leer, y menos citando la letra de otra ficha.

POR QUE PIDE CORRECCION. Se escribio EN LA ERA EN QUE LA COMPONENTE ERA EL PAR:
en OP-U-01 los actos eran de tamano DOS y puro A, asi que "ningun acto se funde
con un par interno sin veredicto" era TRIVIALMENTE CIERTA y no pedia nada. Los
actos de OP-U-02 van de 3 a 15 miembros y solo entraron a la cola los pares que
la semejanza PROPUSO: LEIDA A LA LETRA HOY, la clausula anularia los 47 actos
del tramo unico, incluida la parte ya ejecutada y verificada por el auditor a lo
largo de siete actas. Y ESTA FICHA MANDA SOBRE EL TRAMO: las entradas tipo acto
del tramo unico nombran OP-L-03 junto a OP-U-02, medido por el auditor en el
acta 71 y por el ejecutor en la seccion 5 del reporte de la vuelta 71.

EL CARRIL, Y NO SE ESTRENA NINGUNO. Banco 9.10 (correccion declarada: el texto
viejo no se borra, la vara nueva se escribe al lado), que es EL MISMO que la
ficha de OP-U-02 uso en la vuelta 66 para su clausula gemela, y EL MISMO que
aquella ficha ya habia usado en su campo `evidencia` en la vuelta 48. Y NO SE
ESTRENA CLAVE NUEVA DE ESQUEMA: la correccion va como UN ELEMENTO MAS de la
lista `verificacion`, que es el campo que ya contiene la clausula corregida. El
esquema de OPERACIONES.jsonl es un pendiente de doctrina heredado (acta 55,
cierre; acta 64, D7) y estrenar clave en una de las 71 fichas seria decidirlo de
tapadillo.

EL TEXTO VIEJO NO SE BORRA: una correccion que tapa lo que corrige no se puede
auditar (regla 8 de EJECUTOR.md). La clausula vieja se queda donde esta, en su
sitio de la lista, y la correccion se adosa detras citandola verbatim.

LAS GUARDAS, y ninguna tiene rama por defecto:
  1. si la clausula vieja NO esta verbatim en la ficha, es ROJO y no se escribe
     nada;
  2. la clausula gemela de OP-U-02 se MIDE tambien, y su correccion de la vuelta
     66 se comprueba PRESENTE: si no estuviera, esta correccion estaria citando
     un precedente que no existe y eso es ROJO;
  3. si la marca ya esta, no se escribe nada (idempotente);
  4. tras escribir se re-lee el fichero entero: MISMO numero de fichas, MISMAS
     claves en todas ellas (ni una nueva, ni una perdida), la clausula vieja
     SIGUE dentro de OP-L-03, y ninguna otra ficha cambia ni un byte;
  5. cero guiones largos y cero guiones medios en lo escrito.

DE ESCRITURA SOLO SOBRE docs/plan/OPERACIONES.jsonl.

Uso: python scripts/loop/vuelta72_correccion_ficha_opl03.py [--escribir]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
NL = chr(10)

ID = "OP-L-03"
GEMELA_ID = "OP-U-02"
CAMPO = "verificacion"
MARCA = "CORRECCION DECLARADA (2026-08-26, vuelta 72, TAREA 1 del encargo)"

# LA CLAUSULA VIEJA DE OP-L-03, VERBATIM. Si esta cadena no aparece TAL CUAL en
# la lista, el instrumento cae en ROJO: la correccion se apoya en poder citarla.
VIEJA = "ningun acto se funde con un par interno sin veredicto"

# LA CLAUSULA GEMELA DE OP-U-02, VERBATIM, y su marca de correccion de la vuelta
# 66. Se miden las dos para que el precedente que esta correccion cita quede
# COMPROBADO y no supuesto.
GEMELA = "el acto se leyo ENTERO antes de fundirse: cero pares internos sin veredicto"
MARCA_GEMELA = "CORRECCION DECLARADA (2026-08-20, vuelta 66, TAREA 1.b del encargo)"

NUEVA = (
    MARCA + ", POR EL CARRIL DEL BANCO 9.10 Y CON EL TEXTO VIEJO ENTERO ARRIBA, SIN "
    "TACHARLO Y SIN CLAVE NUEVA DE ESQUEMA (es un elemento mas de esta misma lista "
    "verificacion, que es la via que la ficha gemela de OP-U-02 uso en la vuelta 66 "
    "para su clausula equivalente y la que aquella ficha ya habia usado en su "
    "evidencia en la vuelta 48). LO QUE SE CORRIGE es la clausula que en esta lista "
    "dice, verbatim: '" + VIEJA + "'. SE ESCRIBIO EN LA ERA EN QUE LA COMPONENTE ERA "
    "EL PAR: en OP-U-01 los actos eran de tamano DOS y puro A, asi que esa clausula "
    "era TRIVIALMENTE CIERTA y no pedia nada. Los actos de OP-U-02 van de 3 a 15 "
    "miembros y a la cola del cribado solo entraron los pares que la semejanza "
    "PROPUSO, no todas las combinaciones: leida a la letra hoy, la clausula anularia "
    "los 47 actos del tramo unico, incluida la parte ya ejecutada y verificada por el "
    "auditor. Y ESTA FICHA MANDA SOBRE ESE TRAMO: las entradas tipo acto del tramo "
    "unico nombran OP-L-03 junto a OP-U-02. LA VARA NUEVA, EN SUS CUATRO MITADES Y "
    "TODAS CITABLES, QUE SON LAS MISMAS CUATRO QUE EL ACTA 65 DIO PARA LA CLAUSULA "
    "GEMELA. PRIMERA, QUE ES LEIDO ENTERO: por P.5 y su correccion de alcance del 15 "
    "ago 2026 (decision del fundador), la lectura debida es la del ACTO ENTERO, o sea "
    "SUS TEXTOS y la pregunta de si es UNA familia o DOS contestada sobre texto "
    "estable; no es la lectura de todas las combinaciones de pares, que seria un re "
    "cribado que ninguna operacion escribio y que nadie adjudico. SEGUNDA, QUE ES UN "
    "PAR SIN LEER: es el que esta EN COLA Y SIN VEREDICTO, y el recomputo de OP-U-02 "
    "(scripts/plan/recomputo_3388.py, verificado por el auditor en el acta de la "
    "vuelta 11) lo cuenta en su campo en_cola_sin_leer APARTE de fuera_de_cola; los "
    "47 actos del tramo traen CERO en en_cola_sin_leer. Un par SIN VEREDICTO ESCRITO "
    "que nunca entro a la cola NO es lectura pendiente: es propuesta que la semejanza "
    "nunca hizo. TERCERA, QUE ES LO QUE BLOQUEA UNA FUSION: el TRIANGULO A mas A mas "
    "D MEDIDO de P.10 (que es mecanico y esta definido sobre veredictos escritos), y "
    "la GUARDA 1B cuando el acto no se puede fundir sin absorber una puerta; en los "
    "dos casos el acto cierra DECLARADO Y NO FUNDIDO con motivo sellado, y NO se "
    "improvisan fusiones parciales. CUARTA, EL UNIVERSO: el tramo unico se fijo en la "
    "vuelta 64 con los 47 ABIERTOS como universo de fusion, verificado por acta, y "
    "los encargos de las vueltas 65 a 72 mandaron fundir su prefijo: la lectura "
    "contraria anularia la operacion entera que el plan sello. ADJUDICADO POR EL "
    "AUDITOR EN EL ACTA DE LA VUELTA 71, seccion 6, adjudicacion 3, CON LAS PALABRAS "
    "NO ES PARADA, por remision expresa al acta de la vuelta 65, seccion 5, pendiente "
    "1, que dio esas mismas cuatro varas para la clausula gemela de OP-U-02 y encargo "
    "aquella correccion por este mismo carril. UNA DIFERENCIA MEDIDA Y NO CALLADA: el "
    "acta 71 llama a las dos clausulas LA MISMA frase, y EN SUSTANCIA lo son (la "
    "misma regla en voz pasiva sobre la lectura y en voz activa sobre la fusion), "
    "pero AL BYTE NO son identicas; la de OP-U-02 dice, verbatim: '" + GEMELA + "'. "
    "Por eso esta correccion cita la letra de ESTA ficha y no la de aquella. LO QUE "
    "ESTA CORRECCION NO HACE: no toca ni un nodo, no cambia el estado ni las "
    "dependencias de esta ficha ni de ninguna otra, y no autoriza ninguna lectura "
    "nueva."
)


def cargar():
    filas = []
    for n, l in enumerate(io.open(OPS, encoding="utf-8"), 1):
        s = l.strip()
        if not s:
            filas.append((n, None, l))
            continue
        filas.append((n, json.loads(s), l))
    return filas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("CORRECCION DECLARADA DE LA CLAUSULA DE LA ERA DEL PAR EN LA VERIFICACION DE %s" % ID)
    print("=" * 78)

    for mal, nombre in ((chr(8212), "guion largo"), (chr(8211), "guion medio")):
        if mal in NUEVA:
            print("ROJO: el texto trae un %s. PARADA." % nombre)
            return 1

    filas = cargar()
    fichas = [(n, r) for n, r, _ in filas if r is not None]
    print()
    print("  fichas leidas          : %d" % len(fichas))
    claves_antes = {r.get("id_op"): sorted(r.keys()) for _, r in fichas}
    n_claves = sorted({len(v) for v in claves_antes.values()})
    print("  claves por ficha       : %s" % n_claves)

    diana = [(n, r) for n, r in fichas if r.get("id_op") == ID]
    if len(diana) != 1:
        print("ROJO: %d fichas con id_op %s. PARADA." % (len(diana), ID))
        return 1
    linea, ficha = diana[0]
    print("  ficha %s en la linea : %d" % (ID, linea))

    lista = ficha.get(CAMPO)
    if not isinstance(lista, list):
        print("ROJO: el campo %s no es una lista. PARADA." % CAMPO)
        return 1
    print("  elementos de %s : %d" % (CAMPO, len(lista)))

    # GUARDA 1: la clausula vieja se cita porque se pudo leer.
    exactos = [i for i, x in enumerate(lista) if x == VIEJA]
    print()
    print("  --- GUARDA DE LA CITA VERBATIM ---")
    print("     buscada : %s" % VIEJA)
    if len(exactos) != 1:
        print("     ROJO: aparece %d veces (se esperaba 1). NO se escribe nada." % len(exactos))
        return 1
    print("     hallada : elemento %d de %d, IDENTICA al byte" % (exactos[0] + 1, len(lista)))

    # GUARDA 2: EL PRECEDENTE SE COMPRUEBA, NO SE SUPONE. La clausula gemela de
    # OP-U-02 y su correccion de la vuelta 66 tienen que estar los dos.
    print()
    print("  --- GUARDA DEL PRECEDENTE QUE ESTA CORRECCION CITA (%s) ---" % GEMELA_ID)
    gem = [r for _, r in fichas if r.get("id_op") == GEMELA_ID]
    if len(gem) != 1:
        print("     ROJO: %d fichas con id_op %s. PARADA." % (len(gem), GEMELA_ID))
        return 1
    lista_gem = gem[0].get(CAMPO) or []
    hay_gemela = GEMELA in lista_gem
    hay_correccion = any(MARCA_GEMELA in x for x in lista_gem)
    print("     la clausula gemela sigue verbatim en %s   : %s"
          % (GEMELA_ID, "OK" if hay_gemela else "ROJO"))
    print("     la correccion de la vuelta 66 esta aplicada : %s"
          % ("OK" if hay_correccion else "ROJO"))
    if not (hay_gemela and hay_correccion):
        print("     ROJO: el precedente citado no se pudo medir. NO se escribe nada.")
        return 1
    # LA DIFERENCIA DE BYTES, MEDIDA E IMPRESA, no heredada del acta.
    print("     las dos clausulas son identicas al byte     : %s (medido)"
          % ("SI" if VIEJA == GEMELA else "NO"))
    print("     la de %s : %s" % (ID, VIEJA))
    print("     la de %s : %s" % (GEMELA_ID, GEMELA))

    # GUARDA 3: idempotencia.
    if any(MARCA in x for x in lista):
        print()
        print("YA ESCRITA: la correccion de la vuelta 72 ya esta en la ficha. No se escribe nada.")
        return 0

    print()
    print("  la correccion anade 1 elemento a %s (%d caracteres) y NO borra ninguno"
          % (CAMPO, len(NUEVA)))
    if not a.escribir:
        print()
        print("  SIMULACION (sin --escribir): no se toca el fichero.")
        print("FIN")
        return 0

    nuevas_lineas = []
    for n, r, cruda in filas:
        if r is not None and r.get("id_op") == ID:
            r[CAMPO] = list(r[CAMPO]) + [NUEVA]
            nuevas_lineas.append(json.dumps(r, ensure_ascii=False) + NL)
        else:
            nuevas_lineas.append(cruda if cruda.endswith(NL) else cruda + NL)
    with io.open(OPS, "w", encoding="utf-8", newline="") as fh:
        fh.write("".join(nuevas_lineas))

    # GUARDA 4: se re-lee entero.
    print()
    print("GUARDAS TRAS ESCRIBIR")
    filas2 = cargar()
    fichas2 = [(n, r) for n, r, _ in filas2 if r is not None]
    print("  fichas antes %d, despues %d" % (len(fichas), len(fichas2)))
    claves_despues = {r.get("id_op"): sorted(r.keys()) for _, r in fichas2}
    iguales = claves_antes == claves_despues
    print("  las claves de las %d fichas son las MISMAS: %s"
          % (len(fichas2), "OK" if iguales else "ROJO"))
    d = [r for _, r in fichas2 if r.get("id_op") == ID][0]
    print("  la clausula vieja SIGUE en la ficha, verbatim: %s"
          % ("OK" if VIEJA in d[CAMPO] else "ROJO"))
    print("  elementos de %s: %d antes, %d despues" % (CAMPO, len(lista), len(d[CAMPO])))
    otras_antes = {r.get("id_op"): json.dumps(r, sort_keys=True, ensure_ascii=False)
                   for _, r in fichas if r.get("id_op") != ID}
    otras_despues = {r.get("id_op"): json.dumps(r, sort_keys=True, ensure_ascii=False)
                     for _, r in fichas2 if r.get("id_op") != ID}
    movidas = [k for k in otras_antes if otras_antes[k] != otras_despues.get(k)]
    print("  otras fichas movidas: %d %s" % (len(movidas), "OK" if not movidas else movidas))
    ok = iguales and VIEJA in d[CAMPO] and not movidas and len(fichas) == len(fichas2)
    print()
    print("VERDE" if ok else "ROJO")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
