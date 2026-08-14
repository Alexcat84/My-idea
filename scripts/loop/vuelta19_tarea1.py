# -*- coding: utf-8 -*-
"""VUELTA 19, TAREA 1: los cinco registros de las adjudicaciones de la vuelta 18.

ESCRIBE en docs/plan/INVENTARIO.jsonl y NADA MAS. Cinco entradas tocadas:

  1.1 figura LA BIFURCACION          -> correccion declarada del aviso del contador
  1.2 figura EL PASO DE OFICIO       -> correccion declarada de los 158 NODOS VIVOS
  1.3 figura ESTRELLA (9.23)         -> registro de la novena, mas el puntero cruzado
  1.4 acto customer_validation_...   -> cobertura, estado y nota, patron de las 221
  1.5 figura nodo puente             -> el puntero cruzado de vuelta

TODAS LAS ADICIONES SON ADITIVAS: ningun texto viejo se borra. El script comprueba
antes de escribir que las 666 lineas restantes quedan identicas byte a byte y que
en cada entrada tocada solo cambian las claves declaradas. Si algo no cuadra,
ABORTA sin escribir.
"""
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[2]
INV = RAIZ / "docs" / "plan" / "INVENTARIO.jsonl"

# --------------------------------------------------------------------- 1.1
BIFURCACION = (
    " CORRECCION DECLARADA EL 14 ago 2026 (vuelta 19), por la caida 1 del acta de la "
    "vuelta 18: EL AVISO DEL CONTADOR DE ARRIBA ES FALSO, Y LA FRASE VIEJA SE QUEDA "
    "ENTERA PARA QUE LA CORRECCION SE PUEDA AUDITAR. Remedido en esta vuelta con "
    "instrumento propio, scripts/loop/vuelta19_medir.py sobre "
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl: la palabra bifurcacion aparece en la razon de "
    "SIETE puestos, que son 1054, 1106, 2030, 2050, 2147, 2198 y 2478, y DOS DE ESOS "
    "SIETE SON LOS EJEMPLARES DE ESTA FIGURA: la razon del 2030 arranca La bifurcacion "
    "del origen y la del 2050 arranca La bifurcacion del origen otra vez. Lo unico "
    "exclusivo del 2198 es la forma en MAYUSCULAS: BIFURCACION en mayusculas aparece en "
    "una sola razon del archivo y es la suya. LA LECCION, ENDEREZADA: un contador SI "
    "encuentra estos dos ejemplares, porque los dos traen la palabra en su razon; lo que "
    "un contador no da es la FIGURA, porque de los siete puestos que traen la palabra "
    "solo dos son ejemplares, y los otros cinco la usan en otro sentido (el 2147 y el "
    "2198 llaman bifurcacion a las dos ramas de una alternativa, que es otra cosa). La "
    "cifra vieja no se borra: queda arriba, con esta correccion al lado."
)

# --------------------------------------------------------------------- 1.2
OFICIO_1 = (
    " CORRECCION DECLARADA EL 14 ago 2026 (vuelta 19), por la caida 2 del acta de la "
    "vuelta 18: LOS 158 NODOS VIVOS DE ARRIBA ESTAN MAL MEDIDOS, Y LA CIFRA VIEJA SE "
    "QUEDA ENTERA. El instrumento de la vuelta 18 no filtro deprecado. Remedido en esta "
    "vuelta con instrumento propio, scripts/loop/vuelta19_medir.py sobre "
    "dataset/metadata/master_graph.json: el dominio exportacion tiene 158 nodos EN EL "
    "GRAFO, de los cuales 17 estan deprecado, y los VIVOS son 141, que es exactamente la "
    "cifra que la entrada de tipo dominio de este mismo inventario ya publica, nodos "
    "vivos 141. LA COTA CORREGIDA ES 6 DE 141 VIVOS. La cota se reconto en esta vuelta "
    "sobre los 141 y da los mismos SEIS nodos, ninguno de ellos deprecado; y los DIEZ "
    "pares de 130 tampoco cambian. Lo que cambia es el denominador, y por eso la cota "
    "pasa de 6 de 158 a 6 de 141."
)

# --------------------------------------------------------------------- 1.3
ESTRELLA_NOVENA = (
    " LA NOVENA, REGISTRADA EL 14 ago 2026 (vuelta 19), Y CON ELLA LA COBERTURA 9 QUEDA "
    "VERIFICADA 9 DE 9. La frase de arriba que dice que la novena no se encontro recibe "
    "aqui su CORRECCION DECLARADA, con fecha, y no se borra. (9) tecnologias "
    "disruptivas, centro tecnologias_disruptivas_oportunidad, radios 505 A con "
    "evaluacion_tecnologias_disruptivas y 513 A con explotacion_tecnologias_disruptivas. "
    "PRIMERA CUENTA DE 9.23, medida en esta vuelta con scripts/loop/vuelta19_medir.py: "
    "los dos unicos pares del archivo que tocan al centro son el 505 y el 513, y los dos "
    "son A. SEDE DE LA DECLARACION, citada tras verificarla yo mismo contra el archivo y "
    "no de memoria: docs/INTRA_DOMINIO_INFORME.md, seccion 513: y de paso, un racimo de "
    "tres que la cola NO PUEDE cerrar, que dice con estas palabras Otra estrella, y esta "
    "con el centro leido por los dos lados. SEGUNDA CUENTA DE 9.23, y aqui esta la "
    "correccion que importa: el par entre los dos perifericos NUNCA ENTRO A LA COLA, que "
    "es cierto y esta medido, PERO SI ESTA LEIDO desde el 11 ago 2026 como lectura "
    "dirigida. Es LD-04 de docs/plan/LECTURAS_DIRIGIDAS.md, "
    "evaluacion_tecnologias_disruptivas contra explotacion_tecnologias_disruptivas, "
    "clase D, y ese mismo LD-04 ya declaraba por escrito es una ESTRELLA del banco 9.23, "
    "con centro y dos periferios. LA RELECTURA INDEPENDIENTE DE ESTA VUELTA llego a la "
    "misma D por su cuenta y esta entera, con los nodos impresos y la razon, en "
    "docs/plan/LD_ESTRELLA_DISRUPTIVAS.md; alli va tambien declarado el limite de esa "
    "concordancia, que no fue una relectura ciega. LAS DOS CUENTAS ESTAN, ASI QUE LA "
    "NOVENA ES EJEMPLAR: las estrellas verificadas pasan de OCHO a NUEVE y el campo "
    "cobertura, que dice 9, queda CONFIRMADO en vez de discrepante. LO QUE ESTO CORRIGE, "
    "sin tapar nada: la busqueda de la vuelta 18 no fallo en encontrar el centro, fallo "
    "en buscar la segunda cuenta en un solo sitio, el archivo de veredictos, cuando el "
    "propio reporte de la vuelta 18 ya habia escrito que dos de las trece figuras tienen "
    "ejemplares que viven en LECTURAS DIRIGIDAS y no en el archivo. Esta es la tercera."
)

PUNTERO_ESTRELLA = (
    " PUNTERO CRUZADO CON LA ENTRADA nodo puente, anadido el 14 ago 2026 (vuelta 19) por "
    "la adjudicacion del pendiente de doctrina 2 de la vuelta 18: la forma mecanica de "
    "la estrella de DOS radios (un centro con A a dos perifericos que entre si no son A) "
    "y la del nodo puente (el que tiene A con dos nodos que entre si son D) COINCIDEN, y "
    "que sean dos entradas no es un error del inventario. LO QUE LAS SEPARA ES LA "
    "CONSECUENCIA, y la consecuencia es parte de la figura: la estrella dice arreglese "
    "por separado, sin mesa, porque son N decisiones independientes que se pueden tomar "
    "una a una; el puente dice cuidado, puede que sean DOS FAMILIAS pegadas por el, y el "
    "cierre transitivo no lo distingue. VEASE la entrada de tipo figura con nombre nodo "
    "puente, que trae el puntero de vuelta a esta. NINGUNA ABSORBE A LA OTRA Y NINGUNA SE "
    "CUENTA DOS VECES: un mismo nodo puede levantar las dos lecturas, como "
    "sales_roadmap_vs_sales_force, que es estrella por los puestos 319 y 918 con "
    "periferico 1023 y es a la vez el puente del acto customer_validation_sales_roadmap."
)

# --------------------------------------------------------------------- 1.5
PUNTERO_PUENTE = (
    " PUNTERO CRUZADO CON LA ENTRADA ESTRELLA (9.23), anadido el 14 ago 2026 (vuelta 19) "
    "por la adjudicacion del pendiente de doctrina 2 de la vuelta 18: la forma mecanica "
    "de esta figura (un nodo con A a dos nodos que entre si son D) y la de la estrella de "
    "DOS radios (un centro con A a dos perifericos que entre si no son A) COINCIDEN, y "
    "que sean dos entradas no es un error del inventario. LO QUE LAS SEPARA ES LA "
    "CONSECUENCIA, y la consecuencia es parte de la figura: esta entrada dice cuidado, "
    "puede que sean DOS FAMILIAS pegadas por el nodo, y manda mirar la componente entera; "
    "la estrella dice arreglese por separado, sin mesa, porque son N decisiones "
    "independientes. VEASE la entrada de tipo figura con nombre ESTRELLA (9.23), que trae "
    "el puntero de vuelta a esta. NINGUNA ABSORBE A LA OTRA Y NINGUNA SE CUENTA DOS "
    "VECES: un mismo nodo puede levantar las dos lecturas, como "
    "sales_roadmap_vs_sales_force, que es estrella por los puestos 319 y 918 con "
    "periferico 1023 y es a la vez el puente del acto customer_validation_sales_roadmap."
)

# --------------------------------------------------------------------- 1.4
ACTO_COBERTURA = (
    "15 de 15 pares leidos; 0 en cola; 0 fuera de cola (LD-66 a LD-70, 14 ago 2026). "
    "El texto viejo de este campo, sin tocar: "
)
ACTO_ESTADO = (
    "repite, acto CERRADO (14 ago 2026, vuelta 19, por LD-66 a LD-70). "
    "El texto viejo de este campo, sin tocar: "
)
ACTO_NOTA = (
    "tamano 6. YA NO PUEDE CRECER: 0 en cola y 0 fuera de cola (14 ago 2026, vuelta 19). "
    "CERRADO POR LAS CINCO LECTURAS DIRIGIDAS LD-66 a LD-70 de "
    "docs/plan/LD_SALES_ROADMAP.md, que leyeron los cinco pares que faltaban entre los "
    "seis miembros: la cobertura pasa de 10 de 15 a 15 de 15 y el estado de ABIERTO a "
    "CERRADO. Remedido en esta vuelta con instrumento propio: de los 15 pares posibles, "
    "10 estan en el archivo con 6 A (192, 200, 255, 319, 918 y 966) y 4 D (872, 1023, "
    "1306 y 1330), y los 5 que faltaban son exactamente los de LD-66 a LD-70, con 1 A "
    "(LD-68) y 4 D. El acto queda con 7 A y 8 D de sus 15. LO NUEVO VA AL FRENTE Y EL "
    "TEXTO VIEJO SIGUE ENTERO DEBAJO, con el patron de las 221 superadas. DOS CANDIDATOS "
    "QUE SALEN DE ESAS LECTURAS Y QUE NO SON HECHOS: los decide el recomputo de fusiones "
    "por P.5 y P.8 cuando abra este acto, no esta entrada, y ninguna operacion LISTA los "
    "recoge hoy. CANDIDATO A PARTICION: por la letra de 9.24 el acto es UNO, y ya lo era "
    "con las seis A del archivo solas, pero por la FORMA son un NUCLEO DE CUATRO "
    "(sales_roadmap, hoja_de_ruta_de_ventas, refinar_sales_roadmap y estrategia_de_ventas, "
    "con 5 de sus 6 pares en A) mas una COLA DE DOS (customer_validation_sales_roadmap y "
    "sales_roadmap_vs_sales_force, su unico par en A), cosidos por la costura del 918 mas "
    "el 319, las dos por el mismo nodo. CANDIDATO CONDICIONADO A FORASTERO: "
    "customer_validation_sales_roadmap, el nodo que le da NOMBRE al acto, tiene cuatro D "
    "contra el nucleo (872, 1023, LD-66 y LD-67), su unica A hacia la cola (319) y sus "
    "seis aristas apuntando todas fuera del acto, medido en esta vuelta. LA CONDICION, "
    "escrita porque los dos candidatos NO son independientes: SI EL ACTO SE PARTE, ESE "
    "NODO DEJA DE SER FORASTERO, porque pasa a ser la mitad de su propia familia de dos. "
    "Puntero a la evidencia: docs/plan/LD_SALES_ROADMAP.md, y la entrada de tipo figura "
    "con nombre el forastero por cableado, que trae el mismo candidato con la misma "
    "condicion. EL TEXTO VIEJO DE ESTE CAMPO, SIN TOCAR: "
)


def leer():
    lineas = [l for l in INV.read_text(encoding="utf-8").splitlines() if l.strip()]
    objs = [json.loads(l) for l in lineas]
    return lineas, objs


def serializar(obj, modelo):
    """Reserializa respetando el estilo de separadores de la linea original.

    El archivo tiene DOS estilos conviviendo: las 335 filas de acto vigente van
    compactas y las otras 336 con espacio detras de la coma y de los dos puntos.
    Si se reserializa todo con el mismo estilo, 335 lineas cambian sin que nadie
    las haya tocado y el diff deja de ser auditable.
    """
    compacto = '", "' not in modelo and '": ' not in modelo
    if compacto:
        return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return json.dumps(obj, ensure_ascii=False)


def buscar(objs, tipo, nombre):
    idx = [i for i, e in enumerate(objs)
           if e.get("tipo") == tipo and e.get("nombre") == nombre
           and "superada" not in (e.get("estado") or "").lower()]
    if len(idx) != 1:
        print("ABORTA: %s %s aparece %d veces" % (tipo, nombre, len(idx)))
        sys.exit(1)
    return idx[0]


def main():
    lineas, objs = leer()
    print("entradas leidas: %d" % len(objs))
    original = [json.dumps(e, ensure_ascii=False, sort_keys=True) for e in objs]

    plan = []

    i = buscar(objs, "figura", "LA BIFURCACION")
    plan.append((i, {"nota": objs[i]["nota"] + BIFURCACION}))

    i = buscar(objs, "figura", "EL PASO DE OFICIO")
    plan.append((i, {"nota": objs[i]["nota"] + OFICIO_1}))

    i = buscar(objs, "figura", "ESTRELLA (9.23)")
    plan.append((i, {"nota": objs[i]["nota"] + ESTRELLA_NOVENA + PUNTERO_ESTRELLA}))

    i = buscar(objs, "figura", "nodo puente")
    plan.append((i, {"nota": objs[i]["nota"] + PUNTERO_PUENTE}))

    i = buscar(objs, "acto", "customer_validation_sales_roadmap")
    plan.append((i, {"cobertura": ACTO_COBERTURA + objs[i]["cobertura"],
                     "estado": ACTO_ESTADO + objs[i]["estado"],
                     "nota": ACTO_NOTA + objs[i]["nota"]}))

    tocadas = set()
    for i, cambios in plan:
        if i in tocadas:
            print("ABORTA: la linea %d se toca dos veces" % (i + 1))
            sys.exit(1)
        tocadas.add(i)
        viejo = dict(objs[i])
        for k, v in cambios.items():
            if k not in viejo:
                print("ABORTA: la clave %s no existe en la linea %d" % (k, i + 1))
                sys.exit(1)
            if not v.startswith(viejo[k]) and not v.endswith(viejo[k]):
                print("ABORTA: el cambio en %s de la linea %d NO es aditivo" % (k, i + 1))
                sys.exit(1)
            objs[i][k] = v
        resto_viejo = {k: v for k, v in viejo.items() if k not in cambios}
        resto_nuevo = {k: v for k, v in objs[i].items() if k not in cambios}
        if resto_viejo != resto_nuevo:
            print("ABORTA: cambio otra clave en la linea %d" % (i + 1))
            sys.exit(1)
        print("  linea %-4d %-14s %-46s claves %s" % (
            i + 1, objs[i]["tipo"], objs[i]["nombre"], sorted(cambios)))

    nuevo = [json.dumps(e, ensure_ascii=False, sort_keys=True) for e in objs]
    iguales = sum(1 for a, b in zip(original, nuevo) if a == b)
    print("  entradas identicas: %d de %d, tocadas %d" % (
        iguales, len(objs), len(objs) - iguales))
    if len(objs) - iguales != len(plan):
        print("ABORTA: cambiaron %d y el plan eran %d" % (len(objs) - iguales, len(plan)))
        sys.exit(1)

    finales = [serializar(e, lineas[i]) for i, e in enumerate(objs)]
    intactas = sum(1 for i in range(len(objs)) if finales[i] == lineas[i])
    print("  lineas byte a byte identicas: %d de %d" % (intactas, len(objs)))
    if intactas != len(objs) - len(plan):
        print("ABORTA: %d lineas intactas y deberian ser %d" % (
            intactas, len(objs) - len(plan)))
        sys.exit(1)

    salida = "\n".join(finales) + "\n"
    INV.write_text(salida, encoding="utf-8", newline="\n")
    print("ESCRITO: %s" % INV)
    for mal in ("—", "–"):
        if mal in salida:
            print("AVISO: hay guion largo o medio en la salida")
            return 1
    print("cero guiones largos y cero guiones medios en el archivo entero")
    return 0


if __name__ == "__main__":
    sys.exit(main())
