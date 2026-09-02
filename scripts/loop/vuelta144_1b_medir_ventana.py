# -*- coding: utf-8 -*-
"""vuelta144_1b_medir_ventana.py . ARNES PROPIO DEL EJECUTOR, vuelta 144.

Mide, SIN COPIAR LA MEDICION DEL AUDITOR, los dos agujeros que el acta 143
adjudica a la ventana de la excepcion del 9.22 en
scripts/loop/tallar_estado_de_fase.py:pares_exceptuados_de.

QUE MIDE, TODO EN MEMORIA Y CON CERO ESCRITURAS:
  (i)   cuantos pares salen con la ficha de OP-E-04 TAL CUAL;
  (ii)  cuantos salen quitando el literal de CIERRE de la linea de la
        verificacion 5, y CUAL par entra de mas;
  (iii) en que posiciones aparece el literal de APERTURA en esa misma linea, y
        en cual de ellas ancla el codigo de hoy (bajo.find toma la primera).

Cero escrituras: la ficha se copia en memoria y el fichero de disco no se toca.

LOS DOS LITERALES VAN CLAVADOS AQUI, NO LEIDOS DE `T` (decision de la vuelta
144, para que esta medicion siga REPRODUCIENDO): este arnes mide el ESTADO
ANTERIOR a la reparacion de la TAREA 2.a, cuando la ventana se delimitaba con
"doble linea" y "y escalera". La 2.a los sustituye por la formula canonica; si
el arnes los leyera de `T`, dejaria de medir el defecto que documenta y su
salida commiteada no reproduciria. Tambien lleva SU PROPIA copia de la lectura
vieja (`_ventana_vieja`), por lo mismo.
"""
import io
import json
import os
import re
import sys

# Los dos literales TAL COMO ESTABAN hasta la vuelta 143 incluida.
ABRE_VIEJA = "doble linea"
CIERRA_VIEJA = "y escalera"

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import tallar_estado_de_fase as T  # noqa: E402

OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")


def ficha(id_op):
    for l in io.open(OPS, encoding="utf-8"):
        l = l.strip()
        if not l:
            continue
        o = json.loads(l)
        if o.get("id_op") == id_op:
            return o
    raise SystemExit("ROJO: no esta la ficha " + id_op)


def resolver_del_grafo():
    """El resolutor de alias que la vara usa (P.1, EJECUTOR.md 9)."""
    return T.resolver_de(T.cargar_grafo("WORK"))


def _ventana_vieja(op, resolver, fallos):
    """LA LECTURA TAL COMO ESTABA HASTA LA VUELTA 143, copiada aqui para que
    este arnes siga midiendo el defecto que documenta despues de que la TAREA
    2.a lo repare. Es el codigo de `T.pares_exceptuados_de` de la 143, con sus
    dos literales viejos y con su `else linea[ini:]` intacto."""
    disparo = None
    for i, linea in enumerate(op.get("verificacion") or []):
        bajo = (linea or "").lower()
        for f in T.FRASES_EXCEPCION_PAR:
            if f in bajo:
                disparo = (i, f, linea or "", bajo)
                break
        if disparo:
            break
    if disparo is None:
        return set(), None, []
    i, frase, linea, bajo = disparo
    cita = "verificacion %d: %s" % (i, frase)
    ini = bajo.find(ABRE_VIEJA)
    if ini < 0:
        fallos.append("%s: no trae el literal '%s'" % (op.get("id_op"), ABRE_VIEJA))
        return set(), cita, []
    fin = bajo.find(CIERRA_VIEJA, ini)
    ventana = linea[ini:fin] if fin > ini else linea[ini:]
    mapa_ld = T._pares_por_ld(op)
    crudos = []
    sueltos = []
    for n in T.PATRON_LD.findall(ventana):
        ld = "LD-%s" % n
        if ld in mapa_ld:
            crudos.extend(mapa_ld[ld])
        else:
            sueltos.append(ld)
    crudos.extend(T.PATRON_ARISTA.findall(ventana))
    if sueltos:
        fallos.append("%s: la excepcion nombra %s y su aristas_nuevas no lo trae"
                      % (op.get("id_op"), ", ".join(sorted(set(sueltos)))))
    conjunto = set()
    for o, d in crudos:
        ro, rd = resolver(o), resolver(d)
        if ro != rd:
            conjunto.add(frozenset((ro, rd)))
    if not conjunto:
        fallos.append("%s: dispara la excepcion y no se saca ni un par" % op.get("id_op"))
        return set(), cita, []
    return conjunto, cita, sorted(" <-> ".join(sorted(par)) for par in conjunto)


def nomina(conjunto):
    return sorted(" <-> ".join(sorted(p)) for p in conjunto)


def main():
    op = ficha("OP-E-04")
    resolver = resolver_del_grafo()

    # Localizo POR COMPUTO la linea que dispara, no por indice tecleado.
    idx = None
    for i, linea in enumerate(op.get("verificacion") or []):
        if any(f in (linea or "").lower() for f in T.FRASES_EXCEPCION_PAR):
            idx = i
            break
    if idx is None:
        raise SystemExit("ROJO: OP-E-04 no dispara la excepcion")
    linea = op["verificacion"][idx]
    bajo = linea.lower()
    print("LA LINEA QUE DISPARA: verificacion %d, %d caracteres" % (idx, len(linea)))
    print("")

    # (i) LA FICHA TAL CUAL.
    fallos = []
    conj, cita, nom = _ventana_vieja(op, resolver, fallos)
    print("(i) FICHA TAL CUAL: %d par(es), %d fallo(s)" % (len(conj), len(fallos)))
    for x in nom:
        print("      %s" % x)
    for f in fallos:
        print("      FALLO: %s" % f)
    print("")

    # (ii) QUITADO EL LITERAL DE CIERRE, en memoria.
    #      Se quita del texto real de la linea, respetando su caja.
    m = re.search(re.escape(CIERRA_VIEJA), bajo)
    if not m:
        raise SystemExit("ROJO: la linea no trae el literal de cierre")
    pos_cierre = m.start()
    print("    posicion del literal de cierre '%s': %d" % (CIERRA_VIEJA, pos_cierre))
    op_sin_cierre = json.loads(json.dumps(op))
    op_sin_cierre["verificacion"][idx] = linea[:pos_cierre] + linea[pos_cierre + len(CIERRA_VIEJA):]
    fallos2 = []
    conj2, _, nom2 = _ventana_vieja(op_sin_cierre, resolver, fallos2)
    print("(ii) SIN EL LITERAL DE CIERRE: %d par(es), %d fallo(s)" % (len(conj2), len(fallos2)))
    for x in nom2:
        print("      %s" % x)
    for f in fallos2:
        print("      FALLO: %s" % f)
    entran = conj2 - conj
    salen = conj - conj2
    print("    ENTRAN DE MAS: %d -- %s" % (len(entran), ", ".join(nomina(entran)) or "ninguno"))
    print("    SE PIERDEN:    %d -- %s" % (len(salen), ", ".join(nomina(salen)) or "ninguno"))
    print("")

    # (iii) POSICIONES DEL LITERAL DE APERTURA.
    pos = [m.start() for m in re.finditer(re.escape(ABRE_VIEJA), bajo)]
    print("(iii) EL LITERAL DE APERTURA '%s' aparece %d vez/veces, en %s"
          % (ABRE_VIEJA, len(pos), pos))
    ancla = bajo.find(ABRE_VIEJA)
    print("      EL CODIGO DE HOY ANCLA EN: %d (bajo.find, la PRIMERA)" % ancla)
    if len(pos) > 1:
        print("      DISTANCIA HASTA LA ULTIMA: %d caracteres" % (pos[-1] - pos[0]))
        print("      LO QUE LA VENTANA SE TRAGA DE MAS (de %d a %d):" % (pos[0], pos[-1]))
        print("        %s" % linea[pos[0]:pos[-1]])
    print("")

    # LO QUE LA VENTANA DE HOY LEE DE VERDAD.
    fin = bajo.find(CIERRA_VIEJA, ancla)
    ventana = linea[ancla:fin] if fin > ancla else linea[ancla:]
    print("LA VENTANA REAL DE HOY: [%d, %d), %d caracteres" % (ancla, fin, len(ventana)))
    print("  %s" % ventana)
    print("")
    print("LDs DENTRO DE LA VENTANA REAL DE HOY: %s" % sorted(set(T.PATRON_LD.findall(ventana))))
    ventana_intencion = linea[pos[-1]:fin] if fin > pos[-1] else linea[pos[-1]:]
    print("LDs DENTRO DE LA VENTANA QUE EL COMENTARIO DESCRIBE (ancla en %d): %s"
          % (pos[-1], sorted(set(T.PATRON_LD.findall(ventana_intencion)))))
    print("")
    # POR QUE HOY SALE BIEN: el tramo tragado de mas no aporta ni un LD ni una
    # flecha. Se mide, no se supone.
    tragado = linea[pos[0]:pos[-1]]
    print("EL TRAMO TRAGADO DE MAS: %d caracteres, de %d a %d" % (len(tragado), pos[0], pos[-1]))
    print("  LDs dentro:     %s" % sorted(set(T.PATRON_LD.findall(tragado))))
    print("  flechas dentro: %s" % T.PATRON_ARISTA.findall(tragado))
    print("  VEREDICTO: %s" % ("hoy no aporta nada, por eso la cifra no se mueve"
                               if not T.PATRON_LD.findall(tragado) and not T.PATRON_ARISTA.findall(tragado)
                               else "APORTA, la cifra SI se mueve"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
