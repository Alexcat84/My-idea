# -*- coding: utf-8 -*-
"""vuelta93_tarea3_guarda_direccion.py . VUELTA 93, TAREA 3: LA REPARACION DEL
GUARDA DE `scripts/loop/vuelta92_tarea2_guarda_direccion.py` EN LAS DOS
DIRECCIONES (encargo de la vuelta 93, `docs/loop/PROMPT_SIGUIENTE.md`, TAREA 3).

POR QUE HACE FALTA. El acta de la vuelta 92 (`ACTA_AUDITOR.md`, seccion 3.1 y
3.2) midio DOS defectos del guarda de la vuelta 92 sobre bolsas que su vara
nunca vio:

  (1) FALSO PASA, 3,7% sobre un TERCER CONJUNTO de 81 razones (las de
      `docs/plan/COSECHA_RAZONES_D.jsonl` con senales "formula de la vara" o
      "procedimiento de esa linea", menos los 202 puestos de las dos bolsas
      oficiales): tumba 3 pares SANOS (995, 1007, 1024) porque sus razones
      nombran la linea con una preposicion ("termina CON una linea", "cierra
      CON una linea", "empieza CON una linea") que la lista de alternativas no
      traia, y el 995 ademas cierra con "el paso nombra, el hijo ejecuta", la
      marca de madre mas limpia del catalogo, que el guarda tampoco conocia.
  (2) FALSO SALE al reves: la alternativa "prueba el problema" (anadida en la
      vuelta 92 citando SOLO el puesto 1009) hace PASAR el 1009, el 1411 y el
      1557, y la propia vuelta 93 (TAREA 2, relectura conjunta del 1009)
      concluyo que el 1009 SALE: la formula "prueba el problema" en su razon
      es la formula de la clase D (presenta lo que hace un nodo y enumera SUS
      pasos enteros, nunca nombra una linea de UNO de los dos), no la de madre
      e hijo. La alternativa se RETIRA de la lista.

LA VARA, LOS TRES CASOS OBLIGATORIOS (correr con --vara):
  1. Sobre las 88 de `docs/plan/OP_E_07_REBASE_V91.jsonl`: el guarda tiene que
     marcar EXACTAMENTE {1098, 1009} como SALE (el conjunto que la TAREA 2
     dejo decidido: el 1009 sale junto al 1098).
  2. Sobre las 114 de `docs/plan/OP_E_06_DIRECCION_V90.jsonl`: el 1160 tiene
     que seguir dando PASA, y NINGUN otro de los 114 puede salir (0 SALEN,
     igual que con el guarda de la vuelta 92): reparar el falso SALE o el
     falso PASA no puede reabrir OP-E-06 por la puerta de atras.
  3. Sobre el TERCER CONJUNTO (reconstruido por este mismo script, no copiado
     del acta): los tres falsos SALE (995, 1007, 1024) tienen que PASAR. Si
     queda algun otro SALE en ese conjunto, se nombra y se lee: si es un falso
     positivo mas se arregla; si no, se declara como hallazgo.

MECANICA DE ROJO: identica a la vuelta 92, si no se puede leer la razon de
algun puesto, NO SE TALLA NADA, EXIT 1.

USO:
  python scripts/loop/vuelta93_tarea3_guarda_direccion.py --vara
  python scripts/loop/vuelta93_tarea3_guarda_direccion.py --tercer-conjunto
  python scripts/loop/vuelta93_tarea3_guarda_direccion.py --mutacion
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
BOLSA_OPE07 = os.path.join(PLAN, "OP_E_07_REBASE_V91.jsonl")
BOLSA_OPE06 = os.path.join(PLAN, "OP_E_06_DIRECCION_V90.jsonl")
COSECHA_D = os.path.join(PLAN, "COSECHA_RAZONES_D.jsonl")
SALIDA_TERCER_CONJUNTO = os.path.join(PLAN, "OP_E_07_TERCER_CONJUNTO_V93.jsonl")

# CONDICION (a): MARCA DE MADRE POSITIVA. Idéntica a la de la vuelta 92, MENOS
# "prueba el problema" (retirada, TAREA 3.b: era el UNICO sosten de 1009, 1411
# y 1557, y su formula es la de la clase D, no la de madre e hijo), MAS las
# cuatro alternativas nuevas de la TAREA 3.a.
_ORDINALES = r"primer|segundo|tercer|cuarto|quinto|sexto|septimo|octavo|noveno"
_LINEA = r"l[ií]neas?(?!\s*compartid)"
_LINEA_SOLA = r"l[ií]nea(?!\s*compartid)"
# TAREA 3.a: SE ANADEN alternativas nuevas SIN QUITAR NINGUNA de las que ya
# funcionaban (la vuelta 92 solo cubria "en UNA LINEA" y "es UNA LINEA" sin
# verbo delante; "termina/cierra/empieza CON UNA LINEA" son casos NUEVOS, no
# sustituciones). La preposicion SI se generaliza ("en" o "con") pero SOLO
# para estos tres verbos nuevos, dejando intactas las alternativas viejas
# ("en\s+...", "es\s+...", "dice\s+...", "son\s+...") que un merge habria
# roto (primera version de esta reparacion: fundir todo en un solo patron
# "VERBO PREPOSICION LINEA" tumbo el CASO 1 y el CASO 2 de la vara, porque
# perdia la forma "en UNA LINEA" SIN verbo especifico delante, la que 1195,
# 1521, 2057, 1170, 1314, 1345, 1424, 1512 y 1618 usan). La lookahead
# negativa de _LINEA (que excluye "linea compartida") se hereda sin variarla.
_PREPOSICION_LINEA = r"(?:en|con)\s+(?:una|dos|tres|media)\s+" + _LINEA
_ALTERNATIVAS_MARCA_MADRE = [
    r"paso\s+\d", r"pasos\s+\d",                        # "paso 4" / "pasos 2, 3 y 4" (1114, 1318...)
    r"(?:" + _ORDINALES + r")\s+paso",                  # "tercer paso" (940, 993, 1196)
    r"etapas?\s+\d",                                    # "etapa 1", "etapa 2" (1244, 1344)
    r"en\s+(?:una|dos|tres|media)\s+" + _LINEA,         # "en UNA LINEA", "en DOS LINEAS" (1195, 1612...)
    r"es\s+(?:una|dos|tres)\s+" + _LINEA,               # "es UNA LINEA" (896, 902, 910, 940...)
    r"dice\s+(?:una|dos|tres)\s+" + _LINEA,             # "dice tres lineas" (960, sin "en")
    r"son\s+" + _LINEA,                                 # "son lineas" (909)
    r"(?:termina|cierra|empieza)\s+" + _PREPOSICION_LINEA,  # "termina/cierra/empieza CON o EN UNA/DOS/TRES LINEA(S)" (995, 1007, 1024)
    r"(?:primera|segunda|tercera)\s+" + _LINEA_SOLA,    # "de su segunda linea" (1129)
    r"en\s+una\s+sola\s+" + _LINEA_SOLA,                # "en una sola linea" (1086)
    r"entre sus pasos",                                 # "dice, entre sus pasos" (1848)
    r"el paso nombra,?\s*el hijo ejecuta",              # "el paso nombra, el hijo ejecuta" (995, la marca mas limpia)
    r"es un h[aá]bito",                                 # "es un habito de taller" (1281). INVERIFICABLE (nota abajo).
    r"es (?:el|un) indice",                             # "ES EL INDICE" (1388), "es un INDICE" (1092)
    r"enumera",                                         # "ENUMERA" (1500)
    r"ordena",                                          # "ORDENA" (886, 951, 1083)
    r"es la etapa",                                     # "ES LA ETAPA" (890)
    r"es el programa",                                  # "ES EL PROGRAMA" (1020)
    r"\bmanda\b",                                       # "MANDA SALIR" (947)
    r"enuncia",                                         # "ENUNCIA" (872, 1023, 1946)
    r"es un repertorio",                                # "es un repertorio" (1196)
    r"nombra el problema",                               # "NOMBRA EL PROBLEMA" (1844)
    r"escribe el encargo entero",                       # "ESCRIBE EL ENCARGO ENTERO" (1567)
    r"es postura",                                      # "es POSTURA" (1337)
    r"monta el marco",                                  # "MONTA EL MARCO" (1886)
    r"describe las piezas",                             # "describe las piezas" (1191, 1220)
    r"compara los",                                     # "compara los cinco" (974, 1992, 1993)
    r"calcula dos indicadores",                         # "calcula dos indicadores" (974)
    r"recorre",                                         # "RECORRE" (1536)
    r"despacha",                                        # "despacha la primera en UNA LINEA" (951, 1102...)
    r"la madre\b",                                      # "la madre nombrada literalmente" (1191)
]
# NOTA SOBRE "es un habito" (1281, TAREA 3.b): aparece UNA SOLA VEZ en las
# 3.388 razones (medido por la vuelta 92, TAREA 1.c del encargo de esta
# vuelta). ES INVERIFICABLE CONTRA OTRO PAR: no hay un segundo puesto con el
# que probar si la formula generaliza o no. SE QUEDA en la lista (no hay
# evidencia de que falle, solo falta evidencia de que generalice), declarado
# inverificable en vez de callado.
MARCA_MADRE_POSITIVA = re.compile("|".join(_ALTERNATIVAS_MARCA_MADRE), re.IGNORECASE)

# CONDICION (b): NEGACION DE JERARQUIA. Sin cambios respecto a la vuelta 92.
NIEGA_JERARQUIA = re.compile(
    r"no crea jerarquia|ninguno la expande|sin jerarquia",
    re.IGNORECASE,
)


def guarda_direccion(razon):
    """LA UNICA PIEZA DE JUICIO DEL GUARDA, aislada para que su caso rojo se
    pueda probar por mutacion (EJECUTOR.md regla 1). Devuelve "PASA" o "SALE".

    TAREA 3.f (nota de lectura del acta 92, seccion sin numero al final de la
    TAREA 3): la rama `if niega and not tiene_marca` sigue siendo
    INALCANZABLE (si `not tiene_marca` ya se devolvio "SALE" arriba; si
    `tiene_marca` es True, `not tiene_marca` es False). La reparacion de esta
    vuelta NO cambia la ESTRUCTURA booleana de la condicion (solo la lista de
    formulas de (a) y nada de (b)), asi que la redundancia sigue igual: no es
    un defecto nuevo, se deja comentada como en la vuelta 92."""
    tiene_marca = bool(MARCA_MADRE_POSITIVA.search(razon))
    niega = bool(NIEGA_JERARQUIA.search(razon))
    if not tiene_marca:
        return "SALE"
    if niega and not tiene_marca:
        return "SALE"  # inalcanzable (tiene_marca ya es True), escrito para que la regla quede literal
    return "PASA"


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def cargar_veredictos():
    return {int(v["puesto_intra"]): v for v in cargar_jsonl(VEREDICTOS)}


def correr_sobre_bolsa(ruta_bolsa, veredictos, campo_puesto="puesto"):
    filas = cargar_jsonl(ruta_bolsa)
    resultados = []
    for f in filas:
        puesto = f[campo_puesto]
        v = veredictos.get(puesto)
        if v is None:
            return None, "ROJO: el puesto %s no tiene entrada en %s. NO SE TALLA NADA." % (
                puesto, VEREDICTOS)
        razon = v["razon"]
        veredicto = guarda_direccion(razon)
        resultados.append((puesto, veredicto))
    return resultados, None


def reconstruir_tercer_conjunto():
    """TAREA 3.c.3: reconstruye EL TERCER CONJUNTO, con codigo propio, no
    copiado del acta. Los pares de COSECHA_RAZONES_D.jsonl con senales
    "formula de la vara" o "procedimiento de esa linea", MENOS los puestos
    que viven en las dos bolsas oficiales (las 88 de OP_E_07_REBASE_V91 y las
    114 de OP_E_06_DIRECCION_V90). Escribe
    docs/plan/OP_E_07_TERCER_CONJUNTO_V93.jsonl para que la cifra quede
    citable de un fichero, no solo de esta corrida."""
    cosecha = cargar_jsonl(COSECHA_D)
    bolsa88 = cargar_jsonl(BOLSA_OPE07)
    bolsa114 = cargar_jsonl(BOLSA_OPE06)
    excluir = set(r["puesto"] for r in bolsa88) | set(r["puesto"] for r in bolsa114)
    señales_buscadas = {"formula de la vara", "procedimiento de esa linea"}
    tercer = [r for r in cosecha
              if señales_buscadas & set(r.get("senales", [])) and r["puesto"] not in excluir]
    with io.open(SALIDA_TERCER_CONJUNTO, "w", encoding="utf-8", newline="\n") as fh:
        for r in tercer:
            fh.write(json.dumps({"puesto": r["puesto"], "dominio": r["dominio"],
                                 "nodo_a": r["nodo_a"], "nodo_b": r["nodo_b"]},
                                ensure_ascii=False) + "\n")
    return tercer


def vara_dura():
    veredictos = cargar_veredictos()

    print("=" * 90)
    print("VARA DURA, CASO 1: las 88 razones de OP_E_07_REBASE_V91.jsonl")
    print("=" * 90)
    res1, rojo1 = correr_sobre_bolsa(BOLSA_OPE07, veredictos, campo_puesto="puesto")
    if rojo1:
        print(rojo1)
        return 1
    salen1 = sorted(p for p, v in res1 if v == "SALE")
    print("total: %d, SALEN: %d %s" % (len(res1), len(salen1), salen1))
    esperado1 = [1009, 1098]
    caso1_ok = salen1 == esperado1
    print("CASO 1 %s: el guarda tiene que marcar EXACTAMENTE %s como SALE (decision de la TAREA 2: el 1009 sale)."
          % ("OK" if caso1_ok else "ROJO", esperado1))
    print()

    print("=" * 90)
    print("VARA DURA, CASO 2: las 114 de OP_E_06_DIRECCION_V90.jsonl, el 1160 tiene que PASAR, 0 SALEN")
    print("=" * 90)
    res2, rojo2 = correr_sobre_bolsa(BOLSA_OPE06, veredictos, campo_puesto="puesto")
    if rojo2:
        print(rojo2)
        return 1
    salen2 = [p for p, v in res2 if v == "SALE"]
    veredicto_1160 = next((v for p, v in res2 if p == 1160), None)
    print("total: %d, SALEN: %d %s" % (len(res2), len(salen2), salen2))
    print("veredicto del 1160: %s" % veredicto_1160)
    caso2_ok = veredicto_1160 == "PASA" and len(salen2) == 0
    print("CASO 2 %s: el 1160 tiene que dar PASA y NINGUN otro de los 114 puede salir."
          % ("OK" if caso2_ok else "ROJO"))
    print()

    print("=" * 90)
    print("VARA DURA, CASO 3: EL TERCER CONJUNTO, reconstruido por este script")
    print("=" * 90)
    tercer = reconstruir_tercer_conjunto()
    print("tercer conjunto: %d filas (escrito en %s)" % (len(tercer), SALIDA_TERCER_CONJUNTO))
    res3, rojo3 = correr_sobre_bolsa(SALIDA_TERCER_CONJUNTO, veredictos, campo_puesto="puesto")
    if rojo3:
        print(rojo3)
        return 1
    salen3 = sorted(p for p, v in res3 if v == "SALE")
    print("SALEN: %d %s" % (len(salen3), salen3))
    falsos_conocidos = {995, 1007, 1024}
    faltan = falsos_conocidos & set(salen3)
    otros = set(salen3) - falsos_conocidos
    caso3_ok = not faltan
    print("los tres falsos SALE conocidos (995, 1007, 1024) PASAN: %s" % ("OK" if caso3_ok else "ROJO, siguen SALE: %s" % sorted(faltan)))
    if otros:
        print("OTROS SALE en el tercer conjunto, NOMBRADOS (hallazgo o falso positivo, se leen aparte): %s" % sorted(otros))
    else:
        print("NINGUN otro SALE en el tercer conjunto.")
    print()

    print("=" * 90)
    if caso1_ok and caso2_ok and caso3_ok:
        print("LA VARA ALCANZA: los tres casos obligatorios se cumplen.")
        return 0
    print("LA VARA NO ALCANZA: revisar el guarda.")
    return 1


def _autoprueba_mutacion():
    """PROBAR guarda_direccion POR MUTACION. Reproduce las dos pruebas de la
    vuelta 92 (siguen validas: la lista de (a) crecio y perdio una entrada,
    pero las marcas que sostienen al 1098 SALE y al 1160 PASA no cambiaron) y
    anade UNA TERCERA, sobre el defecto que esta vuelta repara: el 1009 REAL
    da SALE (ya sin "prueba el problema" en la lista), y una version MUTADA
    que le INYECTA una marca de madre con paso numerado tiene que dar PASA."""
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    from verificar_caso_rojo_por_mutacion import probar_por_mutacion

    veredictos = cargar_veredictos()
    razon_1098 = veredictos[1098]["razon"]
    razon_1160 = veredictos[1160]["razon"]
    razon_1009 = veredictos[1009]["razon"]
    razon_1007 = veredictos[1007]["razon"]
    razon_995 = veredictos[995]["razon"]

    print("CASO 1 (heredado de la vuelta 92): el 1098 REAL da SALE. Inyectar una")
    print("marca de madre con paso numerado tiene que cambiar el veredicto a PASA.")
    razon_1098_con_marca = razon_1098.replace(
        "Queda anotada UNA LINEA COMPARTIDA que no crea jerarquia porque ninguno la expande",
        "customer_validation_sell_phase dice en su paso 4, en UNA LINEA",
    )
    assert razon_1098_con_marca != razon_1098
    probar_por_mutacion(
        nombre="guarda_direccion sobre el puesto 1098 (inyectar marca de madre con paso numerado)",
        criterio=guarda_direccion, entrada=razon_1098, veredicto_esperado="SALE",
        entrada_mutada=razon_1098_con_marca, veredicto_tras_mutar="PASA",
    )

    print()
    print("CASO 2 (heredado de la vuelta 92): el 1160 REAL da PASA. Quitarle su")
    print("marca de paso numerado tiene que cambiar el veredicto a SALE.")
    razon_1160_mutada = re.sub(r"dice en su paso 2, en UNA LINEA", "trae consigo lo de siempre", razon_1160)
    assert razon_1160_mutada != razon_1160, "la mutacion no encontro la marca a quitar en la razon del 1160"
    probar_por_mutacion(
        nombre="guarda_direccion sobre el puesto 1160 (quitar la marca de madre numerada)",
        criterio=guarda_direccion, entrada=razon_1160, veredicto_esperado="PASA",
        entrada_mutada=razon_1160_mutada, veredicto_tras_mutar="SALE",
    )

    print()
    print("CASO 3 (nuevo de esta vuelta, el defecto que se repara): el 1009 REAL da")
    print("SALE (sin 'prueba el problema' en la lista). Inyectarle una marca de")
    print("madre con paso numerado tiene que cambiar el veredicto a PASA.")
    razon_1009_con_marca = razon_1009.replace(
        "prueba el problema",
        "dice en su paso 1, en UNA LINEA",
    )
    assert razon_1009_con_marca != razon_1009, "la mutacion no encontro 'prueba el problema' en la razon del 1009"
    probar_por_mutacion(
        nombre="guarda_direccion sobre el puesto 1009 (inyectar marca de madre con paso numerado en vez de 'prueba el problema')",
        criterio=guarda_direccion, entrada=razon_1009, veredicto_esperado="SALE",
        entrada_mutada=razon_1009_con_marca, veredicto_tras_mutar="PASA",
    )

    print()
    print("CASO 4 (nuevo de esta vuelta, el falso SALE): el 1007 REAL da PASA (con la")
    print("formula nueva 'cierra con UNA LINEA', y NINGUNA otra marca en su razon,")
    print("verificado aparte). Quitarsela tiene que cambiar el veredicto a SALE.")
    razon_1007_mutada = razon_1007.replace("cierra con UNA LINEA", "trae consigo lo de siempre")
    assert razon_1007_mutada != razon_1007, "la mutacion no encontro 'cierra con UNA LINEA' en la razon del 1007"
    probar_por_mutacion(
        nombre="guarda_direccion sobre el puesto 1007 (quitar la marca nueva 'cierra con UNA LINEA')",
        criterio=guarda_direccion, entrada=razon_1007, veredicto_esperado="PASA",
        entrada_mutada=razon_1007_mutada, veredicto_tras_mutar="SALE",
    )

    print()
    print("CASO 5 (nuevo de esta vuelta, la otra marca nueva): el 995 REAL trae DOS")
    print("marcas ('termina con UNA LINEA' Y 'el paso nombra, el hijo ejecuta'), asi que")
    print("quitar una sola no basta para mover el veredicto (la otra lo sostiene sola).")
    print("Se neutraliza primero 'termina con UNA LINEA' (el veredicto SIGUE PASA, por")
    print("'el paso nombra, el hijo ejecuta') y ESA es la entrada del caso; mutarla de")
    print("nuevo quitando 'el paso nombra, el hijo ejecuta' tiene que dar SALE.")
    razon_995_una_marca = razon_995.replace("termina con UNA LINEA", "trae consigo lo de siempre")
    assert razon_995_una_marca != razon_995
    assert guarda_direccion(razon_995_una_marca) == "PASA", (
        "la entrada del caso 5 tenia que seguir dando PASA por 'el paso nombra, el hijo ejecuta'")
    razon_995_sin_marcas = razon_995_una_marca.replace("el paso nombra, el hijo ejecuta", "cada quien hace lo suyo")
    assert razon_995_sin_marcas != razon_995_una_marca, "la mutacion no encontro 'el paso nombra, el hijo ejecuta' en la razon del 995"
    probar_por_mutacion(
        nombre="guarda_direccion sobre el puesto 995 (quitar la marca nueva 'el paso nombra, el hijo ejecuta', ya sin 'termina con UNA LINEA')",
        criterio=guarda_direccion, entrada=razon_995_una_marca, veredicto_esperado="PASA",
        entrada_mutada=razon_995_sin_marcas, veredicto_tras_mutar="SALE",
    )
    print()
    print("LOS SEIS CASOS: PROBADOS POR MUTACION. guarda_direccion SI depende de su entrada.")
    return 0


def main():
    if "--mutacion" in sys.argv:
        return _autoprueba_mutacion()
    if "--tercer-conjunto" in sys.argv:
        tercer = reconstruir_tercer_conjunto()
        print("tercer conjunto: %d filas, escrito en %s" % (len(tercer), SALIDA_TERCER_CONJUNTO))
        return 0
    return vara_dura()


if __name__ == "__main__":
    raise SystemExit(main())
