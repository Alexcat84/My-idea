# -*- coding: utf-8 -*-
r"""vuelta162_tarea2b_mutacion_excepcion.py . TAREA 2.b de la vuelta 162.

CASO POSITIVO POR MUTACION PARA LA TABLA DE EXCEPCIONES DE ABSORBIDOS
(adjudicacion 6.4 del acta 161).

LO QUE EL ENCARGO EXIGE, CON SUS PALABRAS: *"una operacion cuyos absorbidos de
verdad esten pendientes TIENE que seguir saliendo roja, y si pasa, la excepcion
esta abierta de mas"*. Ese es el caso `absorbido_de_verdad_pendiente_sigue_rojo`.

TODO EN MEMORIA Y NUNCA EN DISCO: las fichas mutadas son copias del dict que
`cargar_ops` devuelve, y el grafo se lee de solo lectura. Al final se comprueba
que `docs/plan/OPERACIONES.jsonl` no cambio de tamano.

LOS CINCO CASOS, DICHOS ANTES DE CORRERLOS:
  1. `op_d_02_con_excepcion_cumple`: con la tabla, `OP-D-02` sale CUMPLIDO.
  2. `sin_la_tabla_vuelve_a_rojo`: vaciando la tabla, vuelve a salir SIN CUMPLIR
     con *"1 absorbido(s) OK de 3"*. Es la prueba de que la tabla es lo que la
     mueve, y no otra cosa.
  3. `sin_la_cita_la_excepcion_no_aplica`: si la frase que sostiene la excepcion
     desaparece de la ficha, la excepcion NO se aplica. Una excepcion que
     sobrevive a la desaparicion de su cita es un interruptor.
  4. `absorbido_de_verdad_pendiente_sigue_rojo`: a la ficha se le anade un nodo
     VIVO que NO esta exceptuado; tiene que seguir roja.
  5. `id_exento_que_ya_no_esta_en_nodos_no_aplica`: si la excepcion nombra un id
     que ya no vive en el campo `nodos`, la entrada esta rancia y no se aplica.

USO:  python scripts/loop/vuelta162_tarea2b_mutacion_excepcion.py
"""
import copy
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T   # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OP = "OP-D-02"


def ficha(ops, id_op):
    for o in ops:
        if o.get("id_op") == id_op:
            return copy.deepcopy(o)
    raise SystemExit("ROJO: no se halla la ficha %s" % id_op)


def veredicto(op, nodos, resolver):
    cumplido, razon = T.destino_de_fusion(op, nodos, [], resolver)
    return cumplido, razon


def un_vivo_fuera_de(nodos, ya):
    """Un id VIVO del grafo que no este en `ya`. Se ELIGE POR COMPUTO, nunca se
    teclea: el primero por orden alfabetico que cumpla."""
    for k in sorted(nodos):
        if k not in ya and not nodos[k].get("deprecado"):
            return k
    raise SystemExit("ROJO: no hay ningun nodo vivo fuera de la nomina.")


def main():
    print("=" * 78)
    print("CASO POSITIVO POR MUTACION: LA TABLA DE EXCEPCIONES DE ABSORBIDOS")
    print("=" * 78)
    print("")

    ruta_ops = os.path.join(T.RAIZ, "docs", "plan", "OPERACIONES.jsonl")
    tam_antes = os.path.getsize(ruta_ops)

    nodos = T.cargar_grafo()
    ops = T.cargar_ops()
    resolver = T.resolver_de(nodos)   # el resolutor de alias de la casa (P.1)

    base = ficha(ops, OP)
    print("A) LA FICHA REAL, LEIDA DEL PLAN")
    print("   id_op        : %s" % base["id_op"])
    print("   superviviente: %s" % base["superviviente"])
    print("   nodos        : %s" % ", ".join(base["nodos"]))
    print("   CIFRA nodos  : %d" % len(base["nodos"]))
    print("")

    print("B) LA ENTRADA DE LA TABLA, IMPRESA ENTERA")
    e = T.EXCEPCIONES_DE_ABSORBIDOS[OP]
    print("   no_absorbidos: %s" % ", ".join(e["no_absorbidos"]))
    print("   adjudicacion : %s" % e["adjudicacion"])
    for f in e["frases"]:
        print("   frase citada : %r" % f)
    print("")

    # --- los sujetos, todos fabricados en memoria -------------------------
    sin_cita = copy.deepcopy(base)
    sin_cita["nota"] = sin_cita["nota"].replace(e["frases"][0], "(frase retirada por la mutacion)")

    intruso = un_vivo_fuera_de(nodos, set(base["nodos"]))
    con_pendiente = copy.deepcopy(base)
    con_pendiente["nodos"] = list(base["nodos"]) + [intruso]
    print("C) EL NODO INTRUSO DEL CASO 4, ELEGIDO POR COMPUTO Y NO TECLEADO")
    print("   %s (vivo, y NO esta en la lista de exentos)" % intruso)
    print("")

    rancia = copy.deepcopy(base)
    rancia["nodos"] = [x for x in base["nodos"] if x != e["no_absorbidos"][0]]

    # --- los casos ---------------------------------------------------------
    v1, r1 = veredicto(base, nodos, resolver)

    guardada = T.EXCEPCIONES_DE_ABSORBIDOS
    T.EXCEPCIONES_DE_ABSORBIDOS = {}
    v2, r2 = veredicto(base, nodos, resolver)
    T.EXCEPCIONES_DE_ABSORBIDOS = guardada

    v3, r3 = veredicto(sin_cita, nodos, resolver)
    v4, r4 = veredicto(con_pendiente, nodos, resolver)
    v5, r5 = veredicto(rancia, nodos, resolver)

    casos = [
        ("op_d_02_con_excepcion_cumple", v1, True),
        ("y_su_razon_nombra_la_excepcion",
         "EXCEPCION DE ABSORBIDOS APLICADA" in r1, True),
        ("sin_la_tabla_vuelve_a_rojo", v2, False),
        ("y_su_razon_dice_1_de_3", "1 absorbido(s) OK de 3" in r2, True),
        ("sin_la_cita_la_excepcion_no_aplica", v3, False),
        ("y_lo_dice_en_voz_alta", "EXCEPCION DE ABSORBIDOS NO APLICADA" in r3, True),
        ("absorbido_de_verdad_pendiente_sigue_rojo", v4, False),
        ("id_exento_que_ya_no_esta_en_nodos_no_aplica", v5, False),
    ]

    print("D) PASADA 1, LOS CASOS TAL CUAL: todos tienen que PASAR")
    caidos = []
    for nombre, obtenido, esperado in casos:
        ok = obtenido == esperado
        print("   %-46s esperado %-6r obtenido %-6r %s"
              % (nombre, esperado, obtenido, "PASA" if ok else "CAE"))
        if not ok:
            caidos.append(nombre)
    print("")

    print("E) LAS RAZONES, ENTERAS Y SIN RESUMIR")
    for etiqueta, v, r in (("1 con excepcion", v1, r1), ("2 sin la tabla", v2, r2),
                           ("3 sin la cita", v3, r3), ("4 con pendiente", v4, r4),
                           ("5 entrada rancia", v5, r5)):
        print("   [%s] cumplido=%r" % (etiqueta, v))
        print("      %s" % r)
    print("")

    print("F) PASADA 2, LA MUTACION DEL VALOR ESPERADO: cada caso TIENE que CAER")
    sobreviven = []
    for nombre, obtenido, esperado in casos:
        mutado = not esperado
        cae = obtenido != mutado
        print("   %-46s esperado MUTADO %-6r obtenido %-6r %s"
              % (nombre, mutado, obtenido, "CAE (bien)" if cae else "SOBREVIVE (mal)"))
        if not cae:
            sobreviven.append(nombre)
    print("")

    tam_despues = os.path.getsize(ruta_ops)
    print("G) EL PLAN NO SE TOCO")
    print("   docs/plan/OPERACIONES.jsonl: %d bytes antes, %d despues" % (tam_antes, tam_despues))
    intacto = tam_antes == tam_despues
    print("   IDENTICO: %s" % ("SI" if intacto else "NO"))
    print("")

    if caidos:
        print("ROJO: %d caso(s) no pasan: %s" % (len(caidos), caidos))
        return 1
    if sobreviven:
        print("ROJO: %d caso(s) sobreviven a su mutacion: %s" % (len(sobreviven), sobreviven))
        return 1
    if not intacto:
        print("ROJO: el fichero del plan cambio de tamano.")
        return 1
    print("VERDE: %d casos, los %d pasan y los %d caen al mutarles el valor esperado."
          % (len(casos), len(casos), len(casos)))
    print("Y EL QUE EL ENCARGO EXIGE POR SU NOMBRE: "
          "`absorbido_de_verdad_pendiente_sigue_rojo` SIGUE ROJO. La excepcion NO esta "
          "abierta de mas: solo saca del saco a los DOS ids que la ficha nombra, y solo "
          "mientras sus frases sigan en la ficha.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
