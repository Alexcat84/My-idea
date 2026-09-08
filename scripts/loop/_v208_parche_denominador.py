# -*- coding: utf-8 -*-
r"""_v208_parche_denominador.py . PONE LAS DOS CONVENCIONES DEL DENOMINADOR EN
`_v208_t2_denominador.py`, EN VEZ DE PUBLICAR SOLO LA RESUELTA.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3). Se guarda en vez de aplicarse a mano para
que el cambio quede auditable y no como una edicion sin registro.

POR QUE HACE FALTA, Y VA MEDIDO: la primera corrida de mi computo contaba SOLO
los miembros TRAS RESOLVER, que es lo que `P.1` manda para todo conteo que toque
ids, y sobre la JUNTA ASESORA eso da **2 miembros y 1 par posible**, no 4 y 6.
No es un fallo del resolutor: `identificar_junta_asesores` resuelve hoy a
`identificar_consejo_asesores` y `formalize_advisory_board` a
`formalizar_junta_asesora`, o sea que la campana FUNDIO dos de los cuatro
DESPUES de la `fecha_corte` de la ficha. Es HUELLA DE FUSION, que es como la
propia ficha `OP-L-01` llama a este mismo fenomeno.

LAS DOS FUENTES QUE SE COTEJAN (la tabla viva y la mesa) CUENTAN EN LITERAL, con
los ids tal como estan escritos, y por eso el cotejo va contra la convencion
LITERAL. LA RESUELTA SE PUBLICA AL LADO Y NO SUSTITUYE A NADIE. Ninguna se elige
en silencio.
"""
import io
import sys

RUTA = "scripts/loop/_v208_t2_denominador.py"

PARCHES = []

PARCHES.append(('''        distintos = sorted(set(resueltos))
        n = len(distintos)
        posibles = n * (n - 1) // 2
        w("   CIFRA miembros DISTINTOS TRAS RESOLVER: %d" % n)
        w("   CIFRA miembros que NO existen en el grafo: %d (%s)"
          % (len(fuera), ", ".join(fuera) or "ninguno"))
        w("   CIFRA PARES POSIBLES RECOMPUTADOS, n por (n menos 1) partido por 2: %d"
          % posibles)
        w("   los %d pares, enumerados:" % posibles)
        for u, v in itertools.combinations(distintos, 2):
            w("      %s contra %s" % (u, v))
        resultados[etiqueta] = dict(miembros=miembros, resueltos=distintos,
                                    n=n, posibles=posibles, sec=(ini, fin),
                                    fuera=fuera)
        w("")''', '''        # LAS DOS CONVENCIONES DEL DENOMINADOR, Y NINGUNA SE ELIGE EN SILENCIO.
        # LITERAL: los ids TAL COMO LA NOMINA LOS ESCRIBE, que es el universo que
        # habia en la fecha_corte de la ficha y el que las dos fuentes publican.
        # RESUELTA: los mismos ids pasados por el resolutor, que es lo que P.1
        # manda para todo conteo que toque ids. Cuando las dos dan lo mismo se
        # dice; cuando no, la diferencia es HUELLA DE FUSION y se nombra.
        literales = sorted(set(x for x, _ln in miembros))
        n_lit = len(literales)
        pos_lit = n_lit * (n_lit - 1) // 2
        distintos = sorted(set(resueltos))
        n = len(distintos)
        posibles = n * (n - 1) // 2
        fundidos = [(x, resolver(mapa, x)) for x, _ln in miembros
                    if resolver(mapa, x) != x]
        w("   CIFRA miembros DISTINTOS EN LITERAL: %d" % n_lit)
        w("   CIFRA PARES POSIBLES EN LITERAL: %d" % pos_lit)
        w("   CIFRA miembros DISTINTOS TRAS RESOLVER: %d" % n)
        w("   CIFRA PARES POSIBLES TRAS RESOLVER: %d" % posibles)
        w("   CIFRA miembros que NO existen en el grafo: %d (%s)"
          % (len(fuera), ", ".join(fuera) or "ninguno"))
        w("   CIFRA miembros que HOY RESUELVEN A OTRO NODO, o sea HUELLA DE"
          " FUSION: %d" % len(fundidos))
        for x, r in fundidos:
            w("      %s  ->  %s" % (x, r))
        w("   LAS DOS CONVENCIONES DAN LO MISMO: %s"
          % ("SI" if pos_lit == posibles else
             "NO, y la diferencia se declara en vez de elegir una en silencio"))
        w("   los %d pares EN LITERAL, enumerados:" % pos_lit)
        for u, v in itertools.combinations(literales, 2):
            w("      %s contra %s" % (u, v))
        w("   los %d pares TRAS RESOLVER, enumerados:" % posibles)
        for u, v in itertools.combinations(distintos, 2):
            w("      %s contra %s" % (u, v))
        resultados[etiqueta] = dict(miembros=miembros, resueltos=distintos,
                                    n=n, posibles=posibles, sec=(ini, fin),
                                    fuera=fuera, literales=literales,
                                    n_lit=n_lit, pos_lit=pos_lit,
                                    fundidos=fundidos)
        w("")'''))

PARCHES.append(('''        ok_t = (tabla_pos == r["posibles"])
        ok_m = (mesa_pos == r["posibles"])
        ver = ("LAS TRES CALZAN" if (ok_t and ok_m) else
               ("LA TABLA CALZA, LA MESA NO" if ok_t else
                ("LA MESA CALZA, LA TABLA NO" if ok_m else "NO CALZA NINGUNA")))
        veredictos[etiqueta] = dict(recomputado=r["posibles"], tabla=tabla_pos,
                                    mesa=mesa_pos, veredicto=ver,
                                    fila_mesa=fila_mesa, fila_tabla=ln)
        w("   %-22s %-14s %-14s %-14s %s"
          % (etiqueta, r["posibles"], tabla_pos, mesa_pos, ver))''', '''        # SE COTEJA CONTRA LA CONVENCION LITERAL, QUE ES LA QUE LAS DOS FUENTES
        # USAN: sus columnas cuentan los ids TAL COMO ESTAN ESCRITOS. La resuelta
        # va al lado y no sustituye a nadie.
        ok_t = (tabla_pos == r["pos_lit"])
        ok_m = (mesa_pos == r["pos_lit"])
        ver = ("LAS TRES CALZAN" if (ok_t and ok_m) else
               ("LA TABLA CALZA, LA MESA NO" if ok_t else
                ("LA MESA CALZA, LA TABLA NO" if ok_m else "NO CALZA NINGUNA")))
        veredictos[etiqueta] = dict(recomputado=r["pos_lit"],
                                    recomputado_res=r["posibles"],
                                    tabla=tabla_pos,
                                    mesa=mesa_pos, veredicto=ver,
                                    fila_mesa=fila_mesa, fila_tabla=ln)
        w("   %-22s %-14s %-14s %-14s %s"
          % (etiqueta, r["pos_lit"], tabla_pos, mesa_pos, ver))
        w("   %-22s (tras resolver da %d, y esa cifra NO se coteja contra las"
          " dos fuentes porque ellas cuentan en literal)"
          % ("", r["posibles"]))'''))

PARCHES.append(('''        celdas = [c.strip() for c in ls_ban[SEDES_TABLA[etiqueta] - 1].split("|")]
        leidos_tabla = int(re.sub(r"[^0-9]", "", celdas[5]))
        w("   CIFRA leidos que la tabla viva publica hoy: %d" % leidos_tabla)
        w("   CIFRA leidos DESPUES de sumar las lecturas dirigidas de la mesa:"
          " %d mas %d = %d" % (leidos_tabla, len(dentro), leidos_tabla + len(dentro)))
        w("   CIFRA PARES POSIBLES RECOMPUTADOS: %d" % r["posibles"])
        completa = (leidos_tabla + len(dentro)) >= r["posibles"]
        w("   COBERTURA SOBRE EL DENOMINADOR RECOMPUTADO: %d de %d -> %s"
          % (leidos_tabla + len(dentro), r["posibles"],
             "COMPLETA" if completa else "INCOMPLETA, o sea PROVISIONAL (banco 9.26)"))
        veredictos[etiqueta].update(leidos_tabla=leidos_tabla,
                                    ld_dentro=len(dentro),
                                    leidos_nuevos=leidos_tabla + len(dentro),
                                    completa=completa,
                                    lds=[d[0] for d in dentro])
        w("")''', '''        celdas = [c.strip() for c in ls_ban[SEDES_TABLA[etiqueta] - 1].split("|")]
        leidos_tabla = int(re.sub(r"[^0-9]", "", celdas[5]))
        en_a_tabla = int(re.sub(r"[^0-9]", "", celdas[6]))
        nuevas_a = len([1 for _ld, _x, _y, cl, _rx, _ry in dentro
                        if cl.strip().startswith("A")])
        w("   CIFRA leidos que la tabla viva publica hoy: %d" % leidos_tabla)
        w("   CIFRA en A que la tabla viva publica hoy: %d" % en_a_tabla)
        w("   CIFRA de esas lecturas dirigidas que son de clase A: %d" % nuevas_a)
        w("   CIFRA leidos DESPUES de sumar las lecturas dirigidas de la mesa:"
          " %d mas %d = %d" % (leidos_tabla, len(dentro), leidos_tabla + len(dentro)))
        w("   CIFRA en A DESPUES: %d mas %d = %d"
          % (en_a_tabla, nuevas_a, en_a_tabla + nuevas_a))
        w("   CIFRA PARES POSIBLES RECOMPUTADOS EN LITERAL: %d" % r["pos_lit"])
        completa = (leidos_tabla + len(dentro)) >= r["pos_lit"]
        w("   COBERTURA SOBRE EL DENOMINADOR RECOMPUTADO EN LITERAL: %d de %d,"
          " o sea %s"
          % (leidos_tabla + len(dentro), r["pos_lit"],
             "COMPLETA" if completa else "INCOMPLETA, o sea PROVISIONAL (banco 9.26)"))
        w("   LO QUE LA MESA DECLARA PARA ESTA NOMINA:")
        w("      %s" % ls_lec[SEDES_MESA[etiqueta] - 1].strip()[:180])
        w("   MI COBERTURA Y LA DE LA MESA DICEN LO MISMO: %s"
          % ("SI" if completa else
             "NO. La mesa declara cobertura COMPLETA y sobre el denominador "
             "recomputado NO lo es. LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE "
             "COPIANDO."))
        veredictos[etiqueta].update(leidos_tabla=leidos_tabla,
                                    en_a_tabla=en_a_tabla,
                                    nuevas_a=nuevas_a,
                                    en_a_nuevo=en_a_tabla + nuevas_a,
                                    ld_dentro=len(dentro),
                                    leidos_nuevos=leidos_tabla + len(dentro),
                                    completa=completa,
                                    lds=[d[0] for d in dentro])
        w("")'''))

PARCHES.append(('''        w("| %s | %d | %d | %d | %s | %d | %d | %d de %d, %s |"
          % (etiqueta, r["n"], r["posibles"], v["tabla"], v["mesa"],
             v["leidos_tabla"], v["leidos_nuevos"], v["leidos_nuevos"],
             r["posibles"],
             "COMPLETA" if v["completa"] else "INCOMPLETA (PROVISIONAL)"))''', '''        w("| %s | %d | %d | %d | %s | %d | %d | %d de %d, %s |"
          % (etiqueta, r["n_lit"], r["pos_lit"], v["tabla"], v["mesa"],
             v["leidos_tabla"], v["leidos_nuevos"], v["leidos_nuevos"],
             r["pos_lit"],
             "COMPLETA" if v["completa"] else "INCOMPLETA (PROVISIONAL)"))'''))

PARCHES.append(('''    w("| nomina | miembros recomputados | posibles recomputados | posibles segun la tabla viva | posibles segun la mesa | leidos hoy | mas las LD | cobertura sobre el denominador recomputado |")''', '''    w("| nomina | miembros recomputados EN LITERAL | posibles recomputados EN LITERAL | posibles segun la tabla viva | posibles segun la mesa | leidos hoy | mas las LD | cobertura sobre el denominador recomputado |")'''))

PARCHES.append(('''    w("")
    w("FIN")
    salida = NL.join(L) + NL''', '''    w("")
    w("Y LA SEGUNDA CONVENCION, LA RESUELTA, QUE NO SUSTITUYE A LA DE ARRIBA:")
    w("| nomina | miembros tras resolver | posibles tras resolver | miembros que HOY resuelven a otro nodo |")
    for etiqueta in ("junta asesora", "seleccion de canal"):
        r = resultados.get(etiqueta)
        if not r:
            continue
        w("| %s | %d | %d | %d (%s) |"
          % (etiqueta, r["n"], r["posibles"], len(r["fundidos"]),
             "; ".join("%s a %s" % (x, y) for x, y in r["fundidos"]) or "ninguno"))
    w("")
    w("FIN")
    salida = NL.join(L) + NL'''))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    t = io.open(RUTA, encoding="utf-8").read()
    for i, (viejo, nuevo) in enumerate(PARCHES, 1):
        n = t.count(viejo)
        print("   parche %d: el trozo viejo aparece %d vez(ces) (se exige 1)"
              % (i, n))
        if n != 1:
            print("ROJO: no se escribe nada.")
            return 1
        t = t.replace(viejo, nuevo)
    io.open(RUTA, "w", encoding="utf-8", newline=chr(10)).write(t)
    print("VERDE: %s queda parcheado, %d bytes." % (RUTA, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
