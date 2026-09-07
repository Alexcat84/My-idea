# -*- coding: utf-8 -*-
r"""_v201_t2_correccion_op_i_01.py . LA CORRECCION DECLARADA DE LA EVIDENCIA DE
`OP-I-01`, ESCRITA EN SU SEDE (TAREA 2 de la vuelta 201).

ADJUDICADA POR EL ACTA 199 EN SU `4.1`. NO ES PARADA y no hace falta decidir
nada nuevo.

PREFIJO DE GUION BAJO Y POR EL MISMO MOTIVO QUE SUS HERMANOS de esta vuelta: la
moratoria (`AUDITOR.md` 6.3) prohibe fabricar arneses, guardas y lectores nuevos,
y la adjudicacion `4.5` del acta 199 dice que un computo de una vuelta, con
prefijo de guion bajo, fuera del censo y fuera de la nomina, y que no vigila a
nadie, NO ES MAQUINARIA.

QUE CORRIGE, Y QUE NO. La ficha `OP-I-01` promete en su `evidencia`
*"INVENTARIO.jsonl, 323 entradas"* y en su `nota` un reparto de esas 323.
**LA CIFRA VIEJA NO ES UNA MENTIRA: viaja con su `fecha_corte`, 2026-08-11.** Lo
que envejecio es la evidencia. **El texto viejo se queda ENTERO Y SIN TACHAR** y
la correccion entra **POR ADICION**, como un elemento mas de la misma lista
`evidencia`, que es la via que la ficha gemela `OP-L-01` uso en la vuelta 166 y
que el acta 71, seccion 6, adjudicacion 3, adjudico **CON LAS PALABRAS NO ES
PARADA**. **NO SE ANADE NINGUNA CLAVE NUEVA DE ESQUEMA.**

NINGUNA DE LAS DOS CIFRAS SE TECLEA:
  . el recuento de hoy se hace AQUI, contando `docs/plan/INVENTARIO.jsonl`
    linea a linea y parseando cada una como JSON, y su salida se pega;
  . el 323 se LEE DE LA FICHA, con su linea en `docs/plan/OPERACIONES.jsonl` y
    su indice dentro de la lista `evidencia`.

Y NINGUN CAMPO `estado` SE MUEVE. La vara del trabajo pendiente es el
instrumento, nunca el campo `estado` (recuadro de `AUDITOR.md` 0, decision del
fundador del 4 sep 2026). Este computo CAE EN ROJO si al reescribir la ficha
cualquier clave distinta de `evidencia` cambia de valor.

CORRECCION DECLARADA DE ESTE MISMO FICHERO, HECHA EN ESTA MISMA VUELTA Y CON EL
MOTIVO MEDIDO. En su primera version la guarda del 323 corria DELANTE de la de
idempotencia, y la segunda corrida caia en ROJO diciendo *"el 323 no esta en
exactamente un elemento de `evidencia`"*. **Era cierto**: la propia correccion
CITA el 323 verbatim, asi que despues de escribirla hay DOS elementos con esa
cifra. **No escribia nada, que es lo que se queria, pero lo decia por el motivo
equivocado.** Ahora se sale por IDEMPOTENTE antes de mirar el 323.

USO:
  python scripts/loop/_v201_t2_correccion_op_i_01.py
  python scripts/loop/_v201_t2_correccion_op_i_01.py --escribir
"""
import argparse
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
INVENTARIO = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
ID_OP = "OP-I-01"
MARCA = "CORRECCION DECLARADA (2026-09-07, vuelta 201, TAREA 2)"


def contar_inventario(ruta=None):
    """EL RECUENTO DEL INVENTARIO, HECHO HOY Y NO HEREDADO. Devuelve
    (entradas, por_tipo, malas, bytes_disco, bytes_lf). Semi-pura: lo unico que
    toca disco es leer el fichero que se le pasa."""
    ruta = ruta or INVENTARIO
    crudo = io.open(ruta, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    lineas = [l for l in lf.decode("utf-8").split(NL) if l.strip()]
    por_tipo = {}
    malas = 0
    for l in lineas:
        try:
            d = json.loads(l)
        except Exception:                                    # noqa: BLE001
            malas += 1
            continue
        t = d.get("tipo", "(sin campo tipo)")
        por_tipo[t] = por_tipo.get(t, 0) + 1
    return len(lineas), por_tipo, malas, len(crudo), len(lf)


def linea_de_la_ficha(lineas, id_op=ID_OP):
    """LA LINEA 1-INDEXADA DE UNA FICHA EN `OPERACIONES.jsonl`. PURA: recibe las
    lineas ya leidas. Devuelve None si no hay exactamente un acierto."""
    aguja = chr(34) + "id_op" + chr(34) + ": " + chr(34) + id_op + chr(34)
    hits = [i for i, l in enumerate(lineas, 1) if l.strip() and aguja in l]
    return hits[0] if len(hits) == 1 else None


def elementos_con(lista, patron):
    """LOS INDICES 1-INDEXADOS DE LOS ELEMENTOS DE UNA LISTA QUE CASAN CON UN
    PATRON. PURA. Existe para poder CITAR la cifra vieja por su sitio en vez de
    teclearla."""
    pat = re.compile(patron)
    return [i for i, x in enumerate(lista, 1) if pat.search(str(x))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 201, TAREA 2 . LA CORRECCION DECLARADA DE LA EVIDENCIA DE %s" % ID_OP)
    w("adjudicada por el acta 199 en su 4.1. NO ES PARADA.")
    w("=" * 78)
    w("")

    w("A) EL RECUENTO DE HOY, HECHO AQUI Y NO HEREDADO")
    n, por_tipo, malas, bd, blf = contar_inventario()
    w("   docs/plan/INVENTARIO.jsonl: disco %d bytes | LF %d bytes" % (bd, blf))
    w("   CIFRA entradas (lineas no vacias): %d" % n)
    w("   CIFRA lineas que NO son JSON valido: %d" % malas)
    w("   EL REPARTO POR TIPO, RECONTADO HOY:")
    for t in sorted(por_tipo, key=lambda x: (-por_tipo[x], str(x))):
        w("      %-24s %d" % (t, por_tipo[t]))
    w("   SUMA DEL REPARTO: %d" % sum(por_tipo.values()))
    w("   LA SUMA CALZA CON LAS ENTRADAS: %s"
      % ("SI" if sum(por_tipo.values()) == n else "NO, y se declara"))
    w("")

    w("B) LA CIFRA VIEJA, LEIDA DE LA FICHA Y CITADA POR LINEA")
    crudo_ops = io.open(OPERACIONES, "rb").read()
    lf_ops = crudo_ops.replace(b"\r\n", b"\n")
    lineas_ops = lf_ops.decode("utf-8").split(NL)
    w("   docs/plan/OPERACIONES.jsonl: disco %d bytes | LF %d bytes"
      % (len(crudo_ops), len(lf_ops)))
    ln = linea_de_la_ficha(lineas_ops)
    w("   CIFRA lineas NO VACIAS: %d" % len([x for x in lineas_ops if x.strip()]))
    w("   LINEA DE LA FICHA %s: %s" % (ID_OP, ln))
    if ln is None:
        w("   ROJO: la ficha no aparece exactamente una vez. NO SE ESCRIBE NADA.")
        print(NL.join(L))
        return 1
    d = json.loads(lineas_ops[ln - 1])
    ev = d.get("evidencia", [])
    # LA GUARDA DE IDEMPOTENCIA VA ANTES QUE LA DEL 323, Y ESO ES UNA CORRECCION
    # MEDIDA DE ESTE MISMO FICHERO EN ESTA MISMA VUELTA, NO UN ORDEN CASUAL. En
    # la primera version la comprobacion del 323 corria delante, y en la segunda
    # corrida caia en ROJO diciendo "el 323 no esta en exactamente un elemento":
    # era CIERTO, porque LA PROPIA CORRECCION CITA el 323 verbatim, asi que
    # despues de escribirla hay DOS elementos con esa cifra. NO ESCRIBIA NADA,
    # que es lo que se queria, PERO LO DECIA POR EL MOTIVO EQUIVOCADO, y un
    # instrumento que acierta por el motivo equivocado es exactamente lo que la
    # casa no acepta. Aqui se sale por IDEMPOTENTE antes de mirar el 323.
    if any(MARCA in str(x) for x in ev):
        w("   LA MARCA %r YA ESTA en `evidencia`: la correccion se escribio en" % MARCA)
        w("   una corrida anterior. IDEMPOTENTE, NO SE ESCRIBE NADA, y se sale")
        w("   AQUI, antes de la guarda del 323, porque la propia correccion CITA")
        w("   el 323 verbatim y esa guarda caeria por el motivo equivocado.")
        w("   CIFRA elementos de `evidencia` al entrar: %d" % len(ev))
        w("   crecimiento en disco: 0 bytes")
        w("")
        w("FIN")
        salida = NL.join(L) + NL
        print(salida)
        io.open(os.path.join(LOOP, "SALIDA_V201_T2_CORRECCION_OP_I_01.txt"), "w",
                encoding="utf-8", newline=NL).write(salida)
        return 0
    w("   fecha_corte de la ficha: %r" % d.get("fecha_corte"))
    w("   estado de la ficha (SE LEE, NO SE MUEVE): %r" % d.get("estado"))
    w("   CIFRA elementos de `evidencia`: %d" % len(ev))
    for i, x in enumerate(ev, 1):
        w("      evidencia[%d]: %s" % (i, x))
    idx = elementos_con(ev, r"\b323\b")
    w("   CIFRA elementos de `evidencia` que traen el 323: %d, indices %s"
      % (len(idx), ", ".join(str(x) for x in idx) or "(ninguno)"))
    if len(idx) != 1:
        w("   ROJO: el 323 no esta en exactamente un elemento de `evidencia`.")
        w("   NO SE ESCRIBE NADA: la cifra vieja se cita, no se busca a ojo.")
        print(NL.join(L))
        return 1
    viejo = ev[idx[0] - 1]
    w("   LA CIFRA VIEJA, CITADA: linea %d de docs/plan/OPERACIONES.jsonl,"
      % ln)
    w("      `evidencia` elemento %d: %r" % (idx[0], viejo))
    m323 = re.search(r"\b(\d+)\s+entradas\b", str(viejo))
    vieja = m323.group(1) if m323 else None
    w("   CIFRA leida de ese elemento (no tecleada): %s" % vieja)
    if vieja is None:
        w("   ROJO: no se pudo leer la cifra del elemento. NO SE TECLEA una.")
        print(NL.join(L))
        return 1
    en_nota = "323" in str(d.get("nota") or "")
    w("   el 323 aparece TAMBIEN en el campo `nota`: %s"
      % ("SI" if en_nota else "NO"))
    w("")

    w("C) LA CORRECCION, COMPUESTA CON LAS DOS CIFRAS Y SUS DOS FECHAS DE CORTE")
    reparto_hoy = ", ".join(
        "%d %s" % (por_tipo[t], t)
        for t in sorted(por_tipo, key=lambda x: (-por_tipo[x], str(x))))
    correccion = (
        "%s, POR EL CARRIL DEL BANCO 9.10 Y CON EL TEXTO VIEJO ENTERO ARRIBA, "
        "SIN TACHARLO Y SIN CLAVE NUEVA DE ESQUEMA (es un elemento mas de esta "
        "misma lista evidencia, que es la via que la ficha gemela OP-L-01 uso en "
        "la vuelta 166 para su clausula equivalente y que el acta 71, seccion 6, "
        "adjudicacion 3, adjudico CON LAS PALABRAS NO ES PARADA). LO QUE SE "
        "CORRIGE es la clausula que en esta lista dice, verbatim: '%s'. "
        "LA CIFRA VIEJA NO ES UNA MENTIRA Y NO SE RETIRA: viaja con la "
        "fecha_corte de esta ficha, %s, y con esa fecha era cierta. LO QUE "
        "ENVEJECIO ES LA EVIDENCIA. MEDIDO HOY, CON FECHA DE CORTE 2026-09-07 y "
        "contando el fichero linea a linea en la vuelta 201 con "
        "scripts/loop/_v201_t2_correccion_op_i_01.py: docs/plan/INVENTARIO.jsonl "
        "tiene %d entradas (lineas no vacias), 0 lineas que no sean JSON valido, "
        "%d bytes en disco y %d normalizados a LF. EL REPARTO POR TIPO, "
        "RECONTADO HOY Y NO COPIADO DE NINGUNA ACTA: %s, que suma %d. "
        "EL REPARTO DE LA CIFRA VIEJA SIGUE ESCRITO EN EL CAMPO nota DE ESTA "
        "MISMA FICHA Y NO SE TOCA. NINGUN CAMPO estado SE MUEVE con esta "
        "correccion: la vara del trabajo pendiente es el instrumento y nunca el "
        "campo estado (recuadro de AUDITOR.md 0, decision del fundador del 4 sep "
        "2026)."
        % (MARCA, viejo, d.get("fecha_corte"), n, bd, blf, reparto_hoy,
           sum(por_tipo.values())))
    w("   CIFRA caracteres de la correccion: %d" % len(correccion))
    w("   CIFRA guiones largos y medios: %d"
      % (correccion.count(chr(8212)) + correccion.count(chr(8211))))
    w("   LAS DOS CIFRAS CON SU FECHA DE CORTE CADA UNA (banco 9.21):")
    w("      %s entradas con corte %s (la de la ficha)" % (vieja, d.get("fecha_corte")))
    w("      %d entradas con corte 2026-09-07 (la de hoy)" % n)
    w("")
    w("   EL TEXTO DE LA CORRECCION, ENTERO:")
    for trozo in [correccion[i:i + 76] for i in range(0, len(correccion), 76)]:
        w("   | " + trozo)
    w("")

    w("D) LA IDEMPOTENCIA Y LA GUARDA DE QUE NADA MAS SE MUEVE")
    ya = any(MARCA in str(x) for x in ev)
    w("   la marca %r ya esta en `evidencia`: %s" % (MARCA, "SI" if ya else "NO"))
    nuevo = dict(d)
    nuevo["evidencia"] = list(ev) + [correccion]
    cambian = [k for k in set(list(d) + list(nuevo))
               if k != "evidencia" and d.get(k) != nuevo.get(k)]
    w("   CIFRA claves distintas de `evidencia` que cambian de valor: %d  %s"
      % (len(cambian), ", ".join(sorted(cambian)) or "(ninguna)"))
    w("   CIFRA claves de la ficha antes: %d | despues: %d" % (len(d), len(nuevo)))
    w("   MISMAS CLAVES Y EN EL MISMO ORDEN: %s"
      % ("SI" if list(d) == list(nuevo) else "NO, y se declara"))
    w("   CIFRA elementos de `evidencia` antes: %d | despues: %d"
      % (len(ev), len(nuevo["evidencia"])))
    w("   LOS %d VIEJOS SIGUEN IDENTICOS Y EN SU ORDEN: %s"
      % (len(ev), "SI" if nuevo["evidencia"][:len(ev)] == list(ev) else "NO"))
    if cambian:
        w("   ROJO: alguna clave distinta de `evidencia` se movio. NO SE ESCRIBE.")
        print(NL.join(L))
        return 1
    w("")

    w("E) LA ESCRITURA")
    if a.escribir and not ya:
        linea_nueva = json.dumps(nuevo, ensure_ascii=False)
        todas = list(lineas_ops)
        todas[ln - 1] = linea_nueva
        io.open(OPERACIONES, "w", encoding="utf-8",
                newline=NL).write(NL.join(todas))
        w("   ESCRITA: la linea %d de docs/plan/OPERACIONES.jsonl" % ln)
    elif a.escribir:
        w("   NO SE ESCRIBE: la correccion ya estaba. IDEMPOTENTE.")
    else:
        w("   MODO MEDICION: no se escribe nada.")
    despues = io.open(OPERACIONES, "rb").read()
    w("   docs/plan/OPERACIONES.jsonl al salir: disco %d bytes | LF %d bytes"
      % (len(despues), len(despues.replace(b"\r\n", b"\n"))))
    w("   crecimiento en disco: %d bytes" % (len(despues) - len(crudo_ops)))
    lineas_fin = despues.replace(b"\r\n", b"\n").decode("utf-8").split(NL)
    w("   CIFRA lineas NO VACIAS al salir: %d"
      % len([x for x in lineas_fin if x.strip()]))
    malas_fin = 0
    for x in lineas_fin:
        if not x.strip():
            continue
        try:
            json.loads(x)
        except Exception:                                    # noqa: BLE001
            malas_fin += 1
    w("   CIFRA lineas que NO son JSON valido al salir: %d" % malas_fin)
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V201_T2_CORRECCION_OP_I_01.txt"), "w",
            encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
