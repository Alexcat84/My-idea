# -*- coding: utf-8 -*-
"""vuelta66_correccion_ficha_opu02.py . LA CORRECCION DECLARADA DE LA CLAUSULA DE
LA ERA DEL PAR EN LA VERIFICACION DE LA FICHA DE OP-U-02 (docs/plan/OPERACIONES.jsonl).

TAREA 1.b del encargo de la vuelta 66. NADA DEL GRAFO SE TOCA: la correccion es
DE REGISTRO. Ni un nodo, ni un alias, ni un campo del catalogo.

QUE SE CORRIGE Y POR QUE. La ficha de OP-U-02 lleva en su lista `verificacion`
la clausula, VERBATIM:

    el acto se leyo ENTERO antes de fundirse: cero pares internos sin veredicto

Esa frase se escribio EN LA ERA EN QUE LA COMPONENTE ERA EL PAR: en OP-U-01 los
actos eran de tamano DOS y puro A, asi que "cero pares internos sin veredicto"
era TRIVIALMENTE CIERTA y no pedia nada. Los actos de OP-U-02 van de 3 a 15
miembros y solo entraron a la cola los pares que la semejanza propuso: LEIDA A
LA LETRA HOY, la clausula anularia los 47 actos del tramo unico, incluida la
parte que la vuelta 65 ya ejecuto y el auditor ya verifico. El acta de la vuelta
65 la declara EN DIVERGENCIA (linea 17273) y ENCARGA su correccion declarada.

EL CARRIL, Y NO SE ESTRENA NINGUNO. Banco 9.10 (correccion declarada: el texto
viejo no se borra, la vara nueva se escribe al lado), que es EL MISMO que esta
MISMA ficha ya uso en su campo `evidencia` en la vuelta 48 ("CORRECCION
DECLARADA (vuelta 48, 19 ago 2026), por el carril del banco 9.10 y con el texto
viejo entero delante"). Y NO SE ESTRENA CLAVE NUEVA DE ESQUEMA: la correccion
va como UN ELEMENTO MAS de la lista `verificacion`, que es el campo que ya
contiene la clausula corregida. El esquema de OPERACIONES.jsonl es un pendiente
de doctrina heredado (acta 55, cierre; acta 64, D7) y estrenar clave en una de
las 71 fichas seria decidirlo de tapadillo.

EL TEXTO VIEJO NO SE BORRA: una correccion que tapa lo que corrige no se puede
auditar (regla 8 de EJECUTOR.md). La clausula vieja se queda donde esta, en su
sitio de la lista, y la correccion se adosa detras citandola verbatim.

LAS GUARDAS, y ninguna tiene rama por defecto:
  1. si la clausula vieja NO esta verbatim en la ficha, es ROJO y no se escribe
     nada: no se corrige lo que no se pudo leer;
  2. si la marca ya esta, no se escribe nada (idempotente);
  3. tras escribir se re-lee el fichero entero: MISMO numero de fichas, MISMAS
     claves en todas ellas (ni una nueva, ni una perdida), la clausula vieja
     SIGUE dentro de OP-U-02, y ninguna otra ficha cambia ni un byte;
  4. cero guiones largos y cero guiones medios en lo escrito.

DE ESCRITURA SOLO SOBRE docs/plan/OPERACIONES.jsonl.

Uso: python scripts/loop/vuelta66_correccion_ficha_opu02.py [--escribir]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
NL = chr(10)

ID = "OP-U-02"
CAMPO = "verificacion"
MARCA = "CORRECCION DECLARADA (2026-08-20, vuelta 66, TAREA 1.b del encargo)"

# LA CLAUSULA VIEJA, VERBATIM. Si esta cadena no aparece TAL CUAL en la lista,
# el instrumento cae en ROJO: la correccion se apoya en poder citarla.
VIEJA = "el acto se leyo ENTERO antes de fundirse: cero pares internos sin veredicto"

NUEVA = (
    MARCA + ", POR EL CARRIL DEL BANCO 9.10 Y CON EL TEXTO VIEJO ENTERO ARRIBA, SIN "
    "TACHARLO Y SIN CLAVE NUEVA DE ESQUEMA (es un elemento mas de esta misma lista "
    "verificacion, que es la via que esta ficha ya uso en su evidencia en la vuelta 48). "
    "LO QUE SE CORRIGE es la clausula que en esta lista dice, verbatim: '" + VIEJA + "'. "
    "SE ESCRIBIO EN LA ERA EN QUE LA COMPONENTE ERA EL PAR: en OP-U-01 los actos eran de "
    "tamano DOS y puro A, asi que cero pares internos sin veredicto era TRIVIALMENTE "
    "CIERTA. Los actos de OP-U-02 van de 3 a 15 miembros y a la cola del cribado solo "
    "entraron los pares que la semejanza PROPUSO, no todas las combinaciones: leida a la "
    "letra hoy, la clausula anularia los 47 actos del tramo unico, incluida la parte ya "
    "ejecutada y verificada por el auditor. LA VARA NUEVA, EN SUS TRES MITADES Y TODAS "
    "CITABLES. PRIMERA, QUE ES LEIDO ENTERO: por P.5 y su correccion de alcance del 15 ago "
    "2026 (decision del fundador), la lectura debida es la del ACTO ENTERO, o sea SUS "
    "TEXTOS y la pregunta de si es UNA familia o DOS contestada sobre texto estable; no es "
    "la lectura de todas las combinaciones de pares, que seria un re cribado que ninguna "
    "operacion escribio y que nadie adjudico. SEGUNDA, QUE ES UN PAR SIN LEER: es el que "
    "esta EN COLA Y SIN VEREDICTO, y el recomputo de esta misma operacion "
    "(scripts/plan/recomputo_3388.py, verificado por el auditor en el acta de la vuelta 11) "
    "lo cuenta en su campo en_cola_sin_leer APARTE de fuera_de_cola; los 47 actos del tramo "
    "traen CERO en en_cola_sin_leer. Un par SIN VEREDICTO ESCRITO que nunca entro a la cola "
    "NO es lectura pendiente: es propuesta que la semejanza nunca hizo. TERCERA, QUE ES LO "
    "QUE BLOQUEA UNA FUSION: el TRIANGULO A mas A mas D MEDIDO de P.10 (que es mecanico y "
    "esta definido sobre veredictos escritos), y la GUARDA 1B cuando el acto no se puede "
    "fundir sin absorber una puerta; en los dos casos el acto cierra DECLARADO Y NO FUNDIDO "
    "con motivo sellado, y NO se improvisan fusiones parciales. ADJUDICADO POR EL AUDITOR "
    "EN EL ACTA DE LA VUELTA 65, seccion 5, pregunta 1 (docs/loop/ACTA_AUDITOR.md linea "
    "17255, con la divergencia declarada en la 17273), por extension de cuatro letras "
    "vigentes y sin doctrina nueva, y registrado en docs/plan/03_FUSIONES.md en la seccion "
    "de las adjudicaciones del acta 65, apartado b). LO QUE ESTA CORRECCION NO HACE: no "
    "toca ni un nodo, no cambia el estado ni las dependencias de esta ficha ni de ninguna "
    "otra, y no autoriza ninguna lectura nueva."
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

    # GUARDA 2: idempotencia.
    if any(MARCA in x for x in lista):
        print()
        print("YA ESCRITA: la correccion de la vuelta 66 ya esta en la ficha. No se escribe nada.")
        return 0

    print()
    print("  la correccion anade 1 elemento a %s (%d caracteres) y NO borra ninguno"
          % (CAMPO, len(NUEVA)))
    if not a.escribir:
        print()
        print("  SIMULACION (sin --escribir): no se toca el fichero.")
        print("FIN")
        return 0

    crudo_antes = io.open(OPS, encoding="utf-8").read()
    nuevas_lineas = []
    for n, r, cruda in filas:
        if r is not None and r.get("id_op") == ID:
            r[CAMPO] = list(r[CAMPO]) + [NUEVA]
            nuevas_lineas.append(json.dumps(r, ensure_ascii=False) + NL)
        else:
            nuevas_lineas.append(cruda if cruda.endswith(NL) else cruda + NL)
    with io.open(OPS, "w", encoding="utf-8", newline="") as fh:
        fh.write("".join(nuevas_lineas))

    # GUARDA 3: se re-lee entero.
    print()
    print("GUARDAS TRAS ESCRIBIR")
    filas2 = cargar()
    fichas2 = [(n, r) for n, r, _ in filas2 if r is not None]
    print("  fichas antes %d, despues %d" % (len(fichas), len(fichas2)))
    claves_despues = {r.get("id_op"): sorted(r.keys()) for _, r in fichas2}
    iguales = claves_antes == claves_despues
    print("  las claves de las %d fichas son las MISMAS: %s"
          % (len(fichas2), "OK" if iguales else "ROJO"))
    d = dict(fichas2)[linea] if linea in dict(fichas2) else None
    d = [r for _, r in fichas2 if r.get("id_op") == ID][0]
    print("  la clausula vieja SIGUE en la ficha, verbatim: %s"
          % ("OK" if VIEJA in d[CAMPO] else "ROJO"))
    print("  elementos de %s: %d antes, %d despues" % (CAMPO, len(lista), len(d[CAMPO])))
    otras_antes = {r.get("id_op"): json.dumps(r, sort_keys=True, ensure_ascii=False)
                   for _, r in fichas if r.get("id_op") != ID}
    otras_despues = {r.get("id_op"): json.dumps(r, sort_keys=True, ensure_ascii=False)
                     for _, r in fichas2 if r.get("id_op") != ID}
    print("  las otras %d fichas quedan IDENTICAS: %s"
          % (len(otras_antes), "OK" if otras_antes == otras_despues else "ROJO"))
    crudo = io.open(OPS, encoding="utf-8").read()
    print("  guiones largos %d, guiones medios %d"
          % (crudo.count(chr(8212)), crudo.count(chr(8211))))
    print("  estado y dependencias de la ficha, sin tocar: estado=%s depende_de=%s"
          % (d.get("estado"), d.get("depende_de")))
    if not iguales or VIEJA not in d[CAMPO] or otras_antes != otras_despues:
        io.open(OPS, "w", encoding="utf-8", newline="").write(crudo_antes)
        print()
        print("ROJO: una guarda no paso. El fichero se restauro tal cual estaba.")
        return 1
    print()
    print("VERDE: correccion declarada escrita, texto viejo intacto y esquema sin estrenar clave.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
