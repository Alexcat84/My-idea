# -*- coding: utf-8 -*-
"""VUELTA 20, TAREA 1: los registros que caen en docs/plan/INVENTARIO.jsonl.

ESCRIBE en docs/plan/INVENTARIO.jsonl y NADA MAS. TRES entradas tocadas:

  racimo "el sales roadmap"              -> cobertura, estado y nota (TAREA 1.2)
  figura EL PASO DE OFICIO               -> nota, la cota regenerada (TAREA 1.3)
  figura LA FIRMA POSICIONAL DEL INJERTO -> nota, el desenlace de Horowitz (1.4)

Las tres correcciones son ADITIVAS: lo nuevo al frente y el texto viejo entero
detras en los campos cortos, y adicion al final en las notas. El script
comprueba antes de escribir que las 668 lineas restantes quedan identicas byte a
byte, que ninguna clave aparece ni desaparece, y que cada valor nuevo contiene
al viejo. Si algo no cuadra, ABORTA sin escribir.

TODA CIFRA DE ESTE SCRIPT SALE DE UN INSTRUMENTO CORRIDO EN ESTA VUELTA:
scripts/loop/vuelta20_medir.py para la cota de EL PASO DE OFICIO (26 nodos de
141 vivos, 7 con la linea en su paso 1, 40 pares de 130, contra 6, 2 y 10 de la
cadena de la vuelta 18), y scripts/loop/vuelta20_horowitz.py para la tanda de
los cuatro libros (44 nodos distintos, Horowitz 14). Ninguna se copio de una
nota vieja ni del reporte de la vuelta 19.
"""
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[2]
INV = RAIZ / "docs" / "plan" / "INVENTARIO.jsonl"

# ---------------------------------------------------------------- TAREA 1.2
RACIMO_COBERTURA = (
    "15 de 15 (LD-66 a LD-70, 14 ago 2026, vuelta 20). El texto viejo de este campo, "
    "sin tocar: 10 de 15")
RACIMO_ESTADO = (
    "repite, cobertura COMPLETA (14 ago 2026, vuelta 20, por LD-66 a LD-70; la FORMA "
    "sigue MEZCLADO y NO se toca). El texto viejo de este campo, sin tocar: repite, "
    "cobertura INCOMPLETA")
RACIMO_NOTA = (
    ". CORRECCION ADITIVA 14 ago 2026 (vuelta 20), adjudicada por el acta de la vuelta "
    "19, seccion 4, pregunta 2, y nada borrado. EL MOTIVO: esta entrada mide LA MISMA "
    "NOMINA de seis nodos que la entrada de tipo acto customer_validation_sales_roadmap, "
    "que desde la vuelta 19 dice 15 de 15 pares leidos y acto CERRADO; dos sedes vivas "
    "que cuentan lo mismo NO PUEDEN DIFERIR SIN AVISO, y esta lo hacia a ocho lineas de "
    "la otra. Los cinco pares que faltaban se leyeron como LD-66 a LD-70 en "
    "docs/plan/LD_SALES_ROADMAP.md, y los cinco quedan verificados en esta vuelta con "
    "scripts/loop/vuelta20_medir.py: los quince pares posibles de la nomina son diez en "
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl mas los cinco de las dirigidas. LO QUE NO CAMBIA: "
    "la FORMA sigue MEZCLADO, porque las cinco lecturas cerraron cobertura y no movieron "
    "la clase, tal como el motivo tachado de LECTURAS_DIRIGIDAS.md ya anticipaba. LO QUE "
    "NO SE TOCA Y POR QUE: docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl sigue diciendo 10 de "
    "15 y ABIERTO, y esta bien que lo diga, porque es una FOTO DEL CIERRE TRANSITIVO AL "
    "CORTE 3.388 y no recoge lecturas dirigidas POR DISENO; su leyenda esta escrita en la "
    "seccion 4 de la TAREA (vuelta 19) de docs/plan/RECOMPUTO_3388.md, y quien cite la "
    "deuda 329 tiene que decir de que sede sale")

# ---------------------------------------------------------------- TAREA 1.3
OFICIO_COTA = (
    " LA COTA, REGENERADA EL 14 ago 2026 (vuelta 20), adjudicada por el acta de la vuelta "
    "19, secciones 3.3 y 4.4, adicion declarada y NINGUNA CIFRA BORRADA. LA COTA VIGENTE "
    "PASA A SER LA DE LA CADENA CORREGIDA, remedida en esta vuelta con "
    "scripts/loop/vuelta20_medir.py sobre dataset/metadata/master_graph.json y "
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl: 26 NODOS DE 141 VIVOS del dominio exportacion, 7 "
    "CON LA LINEA EN SU PASO 1, y 40 PARES DE 130. SU CRITERIO, escrito al lado: son las "
    "pistas de la vuelta 18 con la cadena us commercial service REEMPLAZADA POR commercial "
    "service, porque el grafo escribe U.S. Commercial Service con puntos y la cadena vieja "
    "no casa NUNCA, cero nodos. LA COTA VIEJA QUEDA COMO CONTRASTE, con su criterio y sin "
    "tocarse: 6 nodos de 141 vivos, 2 con la linea en su paso 1 y 10 pares de 130, medidos "
    "con las pistas de la vuelta 18 tal como estaban. LAS DOS SE REMIDIERON HOY Y LAS DOS "
    "REPRODUCEN. POR QUE LA VIGENTE ES LA CORREGIDA Y NO ES UNA DEFINICION MAS ANCHA: de "
    "los tres nodos que sostienen los tres ejemplares DECLARADOS POR ESCRITO, dos quedaban "
    "fuera de la cota vieja, y uno de esos dos, import_regulations_foreign_governments, "
    "trae la linea en su PASO 1 con estas palabras, Consultar con el U.S. Commercial "
    "Service antes de exportar a un nuevo pais; y el puesto 2045, que es la sede de la "
    "frase el PRIMER paso de media docena de nodos, calza con los 7 de la corregida donde "
    "los 2 de la vieja no llegaban. Es el mismo trato que recibio la caida 2 de la vuelta "
    "18, el instrumento que no filtraba deprecado: instrumento mal calibrado, cifra "
    "regenerada con correccion declarada, cero doctrina nueva. EL CAMPO cobertura, que dice "
    "medio dominio exportacion, SIGUE SIN TOCARSE.")

# ---------------------------------------------------------------- TAREA 1.4
FIRMA_HOROWITZ = (
    " EL DESENLACE DE HOROWITZ, 14 ago 2026 (vuelta 20), adjudicado por el acta de la "
    "vuelta 19, seccion 4, pregunta 3, MANDA EL GRAFO, adicion breve y nada borrado. LA "
    "PRIMERA DISCREPANCIA DECLARADA ARRIBA QUEDA RESUELTA A FAVOR DE LA MEDICION Y CON LA "
    "CIFRA VIEJA INTACTA: la tanda de los cuatro libros son 44 NODOS DISTINTOS y el grupo "
    "de Horowitz son 14, no 13, medidos hoy con scripts/loop/vuelta20_horowitz.py sobre "
    "dataset/metadata/master_graph.json; 46 declaraciones menos DOS solapes de nodos "
    "(metas_vs_proposito con Horowitz y Coleman, viral_loop_marketing con Coleman y "
    "Weinberg) son 44, y el tercer solape que docs/plan/01_FUENTES.md nombraba, "
    "decision_de_vender_startup, es de DECLARACIONES y no reduce nodos, porque un nodo que "
    "declara el mismo libro dos veces con dos grafias sigue siendo un nodo y un libro. EL "
    "CABO QUE LA MEDICION SOLA NO SALDABA, SALDADO: la nomina de los 14 esta IMPRESA desde "
    "el grafo en docs/plan/01_FUENTES.md, seccion CORRECCION DECLARADA, 14 ago 2026 "
    "(vuelta 20), con la forma verificada uno por uno, y el saldo va en DOS MITADES QUE NO "
    "DICEN LO MISMO. POR PRESENCIA DEL MATERIAL, 44 DE 44 CONFIRMADOS: en los catorce el "
    "bloque del libro declarado en segunda posicion esta presente y con la frontera "
    "visible, asi que sea cual sea el catorceavo que la nomina de 13 dejaba fuera, esta "
    "verificado. POR LA FORMA ESTRICTA, 12 DE 14, Y LOS DOS QUE NO LA TIENEN VAN NOMBRADOS: "
    "en metas_vs_proposito y principio_calidad_mvp el bloque de Horowitz esta pegado y se "
    "ve, pero queda EN MEDIO, porque cada uno declara un TERCER libro despues (Coleman y "
    "Hugos) y es ese tercer bloque el que cierra los pasos. Y LOS DOS INSTRUMENTOS DAN EL "
    "MISMO CORTE, como en voz_del_cliente_voc: sin leer un solo paso, la POSICION del libro "
    "en el campo fuente separa a los mismos dos, porque un libro que no ocupa la ultima "
    "posicion declarada no puede tener el bloque final; medidas sobre los 44, las "
    "declaraciones fuera de la ultima posicion son TRES, esas dos mas viral_loop_marketing "
    "con Coleman, que ya estaba apartado. docs/plan/10_INVENTARIO.md NO SE TOCA: su 14 es "
    "el correcto, y era 01_FUENTES.md el que iba corto.")


def serializar(obj, modelo):
    """Reserializa respetando el estilo de separadores de la linea original."""
    compacto = '", "' not in modelo and '": ' not in modelo
    if compacto:
        return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return json.dumps(obj, ensure_ascii=False)


def buscar(objs, tipo, nombre):
    idx = [i for i, e in enumerate(objs)
           if e.get("tipo") == tipo and e.get("nombre") == nombre]
    if len(idx) != 1:
        print("ABORTA: %s %s aparece %d veces" % (tipo, nombre, len(idx)))
        sys.exit(1)
    return idx[0]


def main():
    lineas = [l for l in INV.read_text(encoding="utf-8").splitlines() if l.strip()]
    objs = [json.loads(l) for l in lineas]
    print("entradas leidas: %d" % len(objs))

    # cada plan es (tipo, nombre, {campo: (modo, texto)}); modo delante o detras
    PLAN = [
        ("racimo", "el sales roadmap", {
            "cobertura": ("delante", RACIMO_COBERTURA),
            "estado": ("delante", RACIMO_ESTADO),
            "nota": ("detras", RACIMO_NOTA)}),
        ("figura", "EL PASO DE OFICIO", {"nota": ("detras", OFICIO_COTA)}),
        ("figura", "LA FIRMA POSICIONAL DEL INJERTO (P.2)",
         {"nota": ("detras", FIRMA_HOROWITZ)}),
    ]

    tocadas = set()
    for tipo, nombre, campos in PLAN:
        i = buscar(objs, tipo, nombre)
        if i in tocadas:
            print("ABORTA: la linea %d se toca dos veces" % (i + 1))
            sys.exit(1)
        tocadas.add(i)
        viejo = dict(objs[i])
        for campo, (modo, texto) in campos.items():
            v = viejo[campo]
            nuevo = texto if modo == "delante" else v + texto
            if v not in nuevo:
                print("ABORTA: %s / %s no conserva el texto viejo entero" % (nombre, campo))
                sys.exit(1)
            if modo == "detras" and not nuevo.startswith(v):
                print("ABORTA: %s / %s no es adicion al final" % (nombre, campo))
                sys.exit(1)
            if modo == "delante" and not nuevo.endswith(v):
                print("ABORTA: %s / %s no deja el viejo entero detras" % (nombre, campo))
                sys.exit(1)
            objs[i][campo] = nuevo
        if set(viejo) != set(objs[i]):
            print("ABORTA: cambia el juego de claves en %s" % nombre)
            sys.exit(1)
        intactos = {k: v for k, v in viejo.items() if k not in campos}
        if intactos != {k: v for k, v in objs[i].items() if k not in campos}:
            print("ABORTA: cambio una clave no planeada en %s" % nombre)
            sys.exit(1)
        print("  linea %-4d %-7s %-42s campos %s" % (
            i + 1, tipo, nombre, sorted(campos)))

    finales = [serializar(e, lineas[i]) for i, e in enumerate(objs)]
    intactas = sum(1 for i in range(len(objs)) if finales[i] == lineas[i])
    print("  lineas byte a byte identicas: %d de %d, tocadas %d" % (
        intactas, len(objs), len(objs) - intactas))
    if intactas != len(objs) - len(PLAN):
        print("ABORTA: %d intactas y deberian ser %d" % (
            intactas, len(objs) - len(PLAN)))
        sys.exit(1)

    salida = "\n".join(finales) + "\n"
    INV.write_text(salida, encoding="utf-8", newline="\n")
    print("ESCRITO: %s" % INV)
    for mal in (chr(8212), chr(8211)):
        if mal in salida:
            print("AVISO: hay guion largo o medio en la salida")
            return 1
    print("cero guiones largos y cero guiones medios en el archivo entero")
    return 0


if __name__ == "__main__":
    sys.exit(main())
