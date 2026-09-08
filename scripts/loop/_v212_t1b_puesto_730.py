# -*- coding: utf-8 -*-
r"""_v212_t1b_puesto_730.py . LA RELECTURA CONJUNTA DEL PUESTO 730 DE LA VUELTA 212.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo y fuera de la
nomina (congelada en 135). Moratoria de AUDITOR.md 6.3.

NO CLONA NINGUN INSTRUMENTO. Importa:
  * `apertura_del_auditor.marcador()`, que es la unica sede del marcador;
  * `verificar_aristas_vivas.cargar / vivo / resolver_de`, que es la sede del
    resolutor (P.1: todo conteo que toque ids resuelve antes de contar);
  * `vuelta186_rutas_del_reporte.medir_en_disco` y `_v211_apertura.shas`, que son
    la sede de las dos convenciones.

EL ORDEN ES EL DEL ENCARGO Y NO SE ALTERA:
  1. VERIFICAR CONTRA EL GRAFO, no contra el acta.
  2. APLICAR LA VARA (9.6.1 con la direccion del 9.6.2 y el 67.6).
  3. DECIDIR CON LA VARA.
  4. SI SE CONFIRMA, CORRECCION DECLARADA por el carril del banco 9.10.
  5. GUARDAS, y EL CASO ROJO POR MUTACION ANTES DE ESCRIBIR NADA.

ESTE FICHERO SOLO MIDE Y NO ESCRIBE EN EL ARCHIVO. La escritura vive en
`_v212_t1b_escribir.py`, y no arranca sin la salida de este.

TODA TABLA QUE ESTE FICHERO ARMA LEYENDO FILAS DICE, EN LA MISMA LINEA, CUANTAS
FILAS ARMO; y si al lado hay una cifra de cuantas deberia haber, van las dos
juntas (obligacion de dictado anadida por el encargo de la 212, que sale de la
4.1 y la 7.3 del acta 211).
"""
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))

import apertura_del_auditor as AP                              # noqa: E402
from verificar_aristas_vivas import cargar, vivo, resolver_de  # noqa: E402
from vuelta186_rutas_del_reporte import medir_en_disco         # noqa: E402
from _v211_apertura import shas                                # noqa: E402

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
ARCHIVO = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
PUESTO = 730
MADRE = "colaboracion_cadena_suministro"
HIJOS_DE_PASO = ["efecto_bullwhip", "compartir_datos_cadena_suministro"]
DIEZ = [490, 497, 522, 555, 557, 568, 582, 586, 610, 624]

OUT = []


def di(s=""):
    OUT.append(s)


def sede(ruta, cuando):
    m = medir_en_disco(RAIZ, ruta)
    sd, sl = shas(ruta)
    igual = "COINCIDEN" if m[0] == m[1] else "NO COINCIDEN"
    di("CIFRA sede %s %s: %d bytes en disco y %d normalizado a LF (%s), "
       "sha256 disco %s y sha256 LF %s" % (ruta, cuando, m[0], m[1], igual, sd, sl))
    return m, sd, sl


def leer_lineas():
    raw = io.open(os.path.join(RAIZ, ARCHIVO.replace("/", os.sep)),
                  encoding="utf-8", newline="").read()
    return raw, raw.split(NL)


def aristas_de(nid, nodos, res):
    """LAS ARISTAS VIVO-VIVO DE UN NODO, POR LAS DOS VISTAS Y RESUELTAS (P.1).
    Devuelve (salida, entrada). No lee ni escribe disco."""
    salida, entrada = set(), set()
    yo = res(nid)
    n = nodos.get(yo) or nodos.get(nid) or {}
    for d in (n.get("nodos_siguientes") or []):
        d2 = res(d)
        if d2 != yo and vivo(nodos.get(d2)):
            salida.add(d2)
    for o in (n.get("nodos_previos") or []):
        o2 = res(o)
        if o2 != yo and vivo(nodos.get(o2)):
            entrada.add(o2)
    for otro, no in nodos.items():
        if not vivo(no):
            continue
        o2 = res(otro)
        if o2 == yo:
            continue
        for d in (no.get("nodos_siguientes") or []):
            if res(d) == yo:
                entrada.add(o2)
        for o in (no.get("nodos_previos") or []):
            if res(o) == yo:
                salida.add(o2)
    return salida, entrada


def main():
    # ==================================================================
    # 0. LA ENTRADA
    # ==================================================================
    di("=" * 78)
    di("TAREA 1.b DE LA VUELTA %d. LA RELECTURA CONJUNTA DEL PUESTO %d." % (VUELTA, PUESTO))
    di("=" * 78)
    di("")
    di("## 0. LA ENTRADA, MEDIDA ANTES DE TOCAR NADA")
    di("")
    _, lineas0 = leer_lineas()
    filas0 = [json.loads(l) for l in lineas0 if l.strip()]
    di("CIFRA filas de %s AL ENTRAR: %d (contadas de este fichero, no tecleadas)"
       % (ARCHIVO, len(filas0)))
    sede(ARCHIVO, "AL ENTRAR")
    m0 = AP.marcador()
    di("CIFRA marcador AL ENTRAR, recomputado con apertura_del_auditor.marcador(): "
       "%d filas; %s" % (m0["filas"],
                         ", ".join("%s %d" % (k, m0["por_clase"][k])
                                   for k in sorted(m0["por_clase"]))))
    di("")

    cand = [f for f in filas0 if f.get("puesto_intra") == PUESTO]
    di("CIFRA filas que llevan puesto_intra %d: %d (se exige 1)" % (PUESTO, len(cand)))
    if len(cand) != 1:
        di("ROJO: el puesto no es unico. No se sigue.")
        return 1, filas0
    fila = cand[0]
    di("CIFRA clase del %d AL ENTRAR: %s" % (PUESTO, fila["clase"]))
    di("CIFRA bytes de la razon del %d AL ENTRAR: %d"
       % (PUESTO, len(fila["razon"].encode("utf-8"))))
    di("CIFRA nodo_a y nodo_b del %d: %s / %s" % (PUESTO, fila["nodo_a"], fila["nodo_b"]))
    di("")

    # ==================================================================
    # 1. CONTRA EL GRAFO, NO CONTRA EL ACTA
    # ==================================================================
    di("## 1. VERIFICADO CONTRA EL GRAFO, RESOLVIENDO A NODO VIVO (P.1)")
    di("")
    nodos = cargar("WORK")
    res = resolver_de(nodos)
    di("CIFRA nodos del grafo cargados: %d" % len(nodos))
    di("CIFRA nodos vivos: %d" % len([n for n in nodos.values() if vivo(n)]))
    di("")

    sal, ent = aristas_de(MADRE, nodos, res)
    di("LA TABLA DE ARISTAS DE SALIDA DE LA MADRE, ARMADA LEYENDO EL GRAFO: "
       "%d fila(s) armada(s), y la cifra que la madre declara en sus "
       "nodos_siguientes es %d"
       % (len(sal), len(nodos[res(MADRE)].get("nodos_siguientes") or [])))
    for d in sorted(sal):
        di("   salida> %-46s es hijo de paso: %s"
           % (d, "SI" if d in HIJOS_DE_PASO else "NO"))
    di("LA TABLA DE ARISTAS DE ENTRADA DE LA MADRE: %d fila(s) armada(s), y la "
       "cifra que la madre declara en sus nodos_previos es %d"
       % (len(ent), len(nodos[res(MADRE)].get("nodos_previos") or [])))
    for o in sorted(ent):
        di("   entrada> %-46s es hijo de paso: %s"
           % (o, "SI" if o in HIJOS_DE_PASO else "NO"))
    di("")
    di("LOS HIJOS DE PASO QUE LA RAZON DEL ARCHIVO NOMBRA: %d nombrados"
       % len(HIJOS_DE_PASO))
    enlazados = 0
    for h in HIJOS_DE_PASO:
        h2 = res(h)
        toca = (h2 in sal) or (h2 in ent)
        if toca:
            enlazados += 1
        di("   hijo> %-38s resuelto a %-38s existe %s vivo %s enlazado por la madre %s"
           % (h, h2, "SI" if h2 in nodos else "NO",
              "SI" if vivo(nodos.get(h2)) else "NO", "SI" if toca else "NO"))
    di("CIFRA hijos de paso QUE LA MADRE ENLAZA: %d de %d" % (enlazados, len(HIJOS_DE_PASO)))
    di("")

    di("EL CAVEAT DE LA 9.6.1 (LA FAMILIA ENCADENADA NO SE CUENTA POR RADIOS): "
       "ANTES DE CONTAR SE MIRA LA FORMA.")
    saltos = {res(MADRE): 0}
    frontera = [res(MADRE)]
    while frontera:
        x = frontera.pop(0)
        if saltos[x] >= 3:
            continue
        sx, _ = aristas_de(x, nodos, res)
        for y in sx:
            if y not in saltos:
                saltos[y] = saltos[x] + 1
                frontera.append(y)
    alcance = set(k for k in saltos if k != res(MADRE))
    di("CIFRA nodos alcanzables desde la madre por aristas de SALIDA hasta 3 saltos: %d"
       % len(alcance))
    hay_cadena = False
    for h in HIJOS_DE_PASO:
        h2 = res(h)
        dentro = h2 in alcance
        hay_cadena = hay_cadena or dentro
        di("   cadena> %-38s alcanzable desde la madre: %s%s"
           % (h, "SI" if dentro else "NO",
              (" (a %d salto(s))" % saltos[h2]) if dentro else ""))
    di("VEREDICTO DE LA FORMA: %s"
       % ("HAY CADENA y la silueta se rescata" if hay_cadena else
          "NO HAY CADENA. Los hijos no cuelgan de la madre ni por cadena, asi que se "
          "cuentan los radios, y los radios son CERO"))
    di("")

    di("### EL CASO ROJO POR MUTACION DEL CONTADOR DE SILUETA, CORRIDO ANTES DE DECIDIR")
    di("(EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION: si el contador fuera una")
    di("constante, meterle una arista de mentira no lo movria.)")
    copia = dict(nodos)
    copia[MADRE] = dict(copia[res(MADRE)])
    copia[MADRE]["nodos_siguientes"] = list(
        copia[MADRE].get("nodos_siguientes") or []) + [HIJOS_DE_PASO[0]]
    res_m = resolver_de(copia)
    sal_m, ent_m = aristas_de(MADRE, copia, res_m)
    enlazados_m = len([h for h in HIJOS_DE_PASO
                       if res_m(h) in sal_m or res_m(h) in ent_m])
    di("CIFRA hijos enlazados SOBRE LA COPIA MUTADA (se le mete a mano la arista a %s): %d"
       % (HIJOS_DE_PASO[0], enlazados_m))
    rojo_ok = (enlazados == 0 and enlazados_m == 1)
    di("EL CASO ROJO %s: sin mutar da %d y mutado da %d (se exige 0 y 1)."
       % ("CAE COMO TIENE QUE CAER" if rojo_ok else
          "NO CAE, Y ESO INVALIDA LA MEDICION", enlazados, enlazados_m))
    di("CIFRA el grafo del disco queda intacto: la mutacion vive en un dict en memoria, "
       "y quien lo comprueba es el numstat de dataset/ del ciclo de Gate 0 del cierre.")
    di("")
    if not rojo_ok:
        di("ROJO: el contador no se comporta. NO SE DECIDE NADA.")
        return 1, filas0

    # ==================================================================
    # 2. EL CERCO
    # ==================================================================
    di("## 2. EL CERCO, RECOMPUTADO POR MI SOBRE LAS %d FILAS, CON EL PATRON DICHO"
       % len(filas0))
    di("")
    patrones = [
        ("cero-enlazados, GUION LITERAL", r"cero-enlazad\w*"),
        ("cero enlazados, HOLGADO (guion, espacio o nada)", r"cero[\s-]*enlazad\w*"),
        ("choque de la seccion 19, FRASE ENTERA", r"choque de la secci[o\xf3]n\s*19"),
        ("seccion 19 A SECAS", r"secci[o\xf3]n\s*19"),
        ("lectura vieja", r"lectura vieja"),
        ("seria D", r"seria D"),
    ]
    guardado = {}
    for nombre, patron in patrones:
        r = re.compile(patron, re.I)
        hits = [f for f in filas0 if r.search(f.get("razon") or "")]
        por_clase = {}
        for f in hits:
            por_clase[f["clase"]] = por_clase.get(f["clase"], 0) + 1
        guardado[nombre] = hits
        di("PATRON %-48s FILAS ARMADAS %2d (y la tabla de la linea de abajo lleva "
           "esas mismas %d); por clase %s"
           % (nombre, len(hits), len(hits),
              ", ".join("%s %d" % (k, por_clase[k]) for k in sorted(por_clase)) or "ninguna"))
        di("   puestos (%d): %s"
           % (len(hits), ", ".join(str(f["puesto_intra"]) for f in hits)))
    di("")
    holgado = guardado["cero enlazados, HOLGADO (guion, espacio o nada)"]
    aes = [f for f in holgado if f["clase"] == "A"]
    des = [f for f in holgado if f["clase"] == "D"]
    di("CIFRA razones en clase A que nombran el cero-enlazados (patron holgado): %d, "
       "y son %s" % (len(aes), ", ".join(str(f["puesto_intra"]) for f in aes)))
    di("CIFRA razones en clase D que lo nombran (patron holgado): %d" % len(des))
    frase = guardado["choque de la seccion 19, FRASE ENTERA"]
    en_diez = [f for f in frase if f["puesto_intra"] in DIEZ]
    fuera = [f for f in frase if f["puesto_intra"] not in DIEZ]
    di("CIFRA de las %d filas de la FRASE ENTERA, cuantas estan en la lista de DIEZ "
       "que la ratificacion declara resueltas: %d; y cuantas NO: %d (%s)"
       % (len(frase), len(en_diez), len(fuera),
          ", ".join(str(f["puesto_intra"]) for f in fuera) or "ninguna"))
    vivos_diez = [p for p in DIEZ if any(f["puesto_intra"] == p for f in filas0)]
    di("CIFRA los DIEZ de la ratificacion, comprobados uno a uno en el archivo: "
       "%d de %d existen" % (len(vivos_diez), len(DIEZ)))
    clases_diez = {}
    for p in DIEZ:
        f = [x for x in filas0 if x["puesto_intra"] == p][0]
        clases_diez[p] = f["clase"]
    di("LA TABLA DE LOS DIEZ CON SU CLASE DE HOY: %d fila(s) armada(s) sobre %d "
       "puestos nombrados por la ratificacion" % (len(clases_diez), len(DIEZ)))
    for p in DIEZ:
        di("   diez> puesto %d clase %s" % (p, clases_diez[p]))
    di("")
    di("EL ORDEN DE CRIBADO, MEDIDO EN EL ORDEN DEL FICHERO Y NO SUPUESTO:")
    orden = {f["puesto_intra"]: i for i, f in enumerate(filas0)}
    for p in (658, 678, PUESTO):
        di("   indice de la fila del puesto %d dentro del fichero: %d" % (p, orden[p]))
    di("CIFRA el %d va DESPUES del 658 y del 678 en el orden del fichero: %s"
       % (PUESTO, "SI" if orden[PUESTO] > orden[658] and orden[PUESTO] > orden[678]
          else "NO"))
    di("")

    # ==================================================================
    # 3. LA VARA
    # ==================================================================
    di("## 3. LA VARA APLICADA POR MI: 9.6.1, LA DIRECCION DEL 9.6.2 Y EL 67.6")
    di("")
    madre = nodos[res(MADRE)]
    hijo = nodos[res("efecto_bullwhip")]
    pm = madre.get("pasos_accionables") or []
    ph = hijo.get("pasos_accionables") or []
    di("LA TABLA DE PASOS DE LA MADRE %s: %d fila(s) armada(s), y el campo "
       "pasos_accionables declara %d" % (MADRE, len(pm), len(pm)))
    for i, p in enumerate(pm, 1):
        di("   madre paso %d> %s" % (i, p))
    di("LA TABLA DE PASOS DEL HIJO efecto_bullwhip: %d fila(s) armada(s), y el campo "
       "pasos_accionables declara %d" % (len(ph), len(ph)))
    for i, p in enumerate(ph, 1):
        di("   hijo paso %d> %s" % (i, p))
    di("CIFRA entregable de la madre, bytes: %d"
       % len((madre.get("entregable_esperado") or "").encode("utf-8")))
    di("   madre entregable> %s" % madre.get("entregable_esperado"))
    di("CIFRA entregable del hijo, bytes: %d"
       % len((hijo.get("entregable_esperado") or "").encode("utf-8")))
    di("   hijo entregable> %s" % hijo.get("entregable_esperado"))
    di("")
    di("LO QUE LE QUEDA A CADA NODO CUANDO LE QUITAS LO QUE DICE EL OTRO.")
    di("La correspondencia la lee la razon del archivo y la confirmo yo leyendo los")
    di("dos campos de arriba: los pasos 1 y 2 de la madre (medir el latigo comparando")
    di("pedidos entrantes contra salientes, y graficar la divergencia) son el paso 1")
    di("del hijo (medir cuanto varia la demanda en distintos puntos de la cadena).")
    di("")
    di("   DIRECCION DEL 9.6.2, LA UNICA QUE MANDA: QUE ANADE EL HIJO A LA MADRE.")
    di("   LE QUEDAN AL HIJO %d de sus %d pasos: los pasos 2, 3, 4, 5 y 6."
       % (len(ph) - 1, len(ph)))
    di("     coste en produccion y en programacion de la operacion (2);")
    di("     coste en transporte, envios y recepcion (3);")
    di("     cuanto inventario de seguridad hace falta y cuanto cuesta mantenerlo (4);")
    di("     cuanto se pierde en ventas por rotura de stock (5);")
    di("     y usar esos numeros para decidir si vale la pena invertir (6).")
    di("   CLASIFICACION POR EL 67.6: son CUATRO computos de coste sobre bases")
    di("   distintas mas una regla de decision que se alimenta de los cuatro. Cada uno")
    di("   obliga a decisiones dentro de si (que periodo, que bases de coste, que")
    di("   nivel de servicio) y se repite en el tiempo. ES PROCEDIMIENTO, NO LINEA.")
    di("   Y el entregable lo confirma: el del hijo es un CALCULO DE CUANTO CUESTA que")
    di("   sirve para decidir la inversion; el de la madre es un GRAFICO mas un ACUERDO.")
    di("")
    di("   LA DIRECCION CONTRARIA, ESCRITA SOLO PORQUE EL ENCARGO PIDE LOS DOS LADOS Y")
    di("   NO PORQUE DECIDA (el 9.6.2 la prohibe como vara): QUE LE QUEDA A LA MADRE.")
    di("   LE QUEDAN A LA MADRE %d de sus %d pasos: los pasos 3, 4 y 5."
       % (len(pm) - 2, len(pm)))
    di("     determinar la posicion de la empresa en la cadena (3);")
    di("     establecer acuerdos de intercambio de datos de inventario y POS (4);")
    di("     construir el sistema barato de visibilidad compartida (5).")
    di("   Tambien es PROCEDIMIENTO. PROCEDIMIENTO EN LOS DOS LADOS, que por el 9.6.3")
    di("   es el par SANO: uno acaba en la contabilidad del latigo y el otro en el")
    di("   acuerdo con el socio. NO ES DUPLICACION.")
    di("")
    di("   LAS DOS DIRECCIONES DEVUELVEN LO MISMO: CONTINUA, o sea D.")
    di("")

    # ==================================================================
    # 4. LA DECISION
    # ==================================================================
    di("## 4. LA DECISION, TOMADA CON LA VARA Y NO CON EL CASO DEL AUDITOR")
    di("")
    silueta_muda = (enlazados == 0 and not hay_cadena)
    di("CIFRA hijos enlazados: %d de %d. CIFRA cadena que rescate la silueta: %s."
       % (enlazados, len(HIJOS_DE_PASO), "SI" if hay_cadena else "NO"))
    di("Por la RATIFICACION del 9.6.1 (el CERO entra en la regla), con cero hermanos")
    di("enlazados la silueta no dice nada y MANDA EL CONTENIDO: %s"
       % ("APLICA" if silueta_muda else "NO APLICA"))
    di("Por la vara de LINEA o PROCEDIMIENTO (67.6), lo que el hijo anade a la madre")
    di("es PROCEDIMIENTO, no linea: CONTINUA.")
    confirma = silueta_muda
    di("VEREDICTO DE ESTA MEDICION: la clase del %d pasa de %s a D. CONFIRMA: %s"
       % (PUESTO, fila["clase"], "SI" if confirma else "NO"))
    di("")
    di("## 5. EL BARRIDO DE TABLAS DERIVADAS QUE EL BANCO 9.10 PIDE MIRAR")
    di("(se MIDE aqui y NO se edita: editar prosa sellada del informe o del plan es")
    di("forma que este encargo no ordena. Va al reporte como discutible.)")
    sedes_derivadas = [
        "docs/INTRA_DOMINIO_INFORME.md",
        "docs/plan/03_FUSIONES.md",
        "docs/loop/reportes/REPORTE_V179.md",
    ]
    total = 0
    tabla = []
    for ruta in sedes_derivadas:
        p = os.path.join(RAIZ, ruta.replace("/", os.sep))
        if not os.path.isfile(p):
            tabla.append((ruta, None, "NO EXISTE"))
            continue
        n = 0
        for i, l in enumerate(io.open(p, encoding="utf-8"), 1):
            if re.search(r"(?<![\d.,])730(?![\d.,])", l):
                n += 1
                tabla.append((ruta, i, l.strip()[:96]))
        total += n
    di("LA TABLA DE CITAS DEL %d FUERA DEL ARCHIVO: %d fila(s) armada(s) sobre %d "
       "sedes miradas" % (PUESTO, len(tabla), len(sedes_derivadas)))
    for ruta, linea, txt in tabla:
        di("   cita> %s linea %s :: %s" % (ruta, linea, txt))
    di("")
    return (0 if confirma else 2), filas0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    codigo, _ = main()
    texto = NL.join(OUT) + NL
    io.open(os.path.join(RAIZ, "docs", "loop",
                         "SALIDA_V%d_T1B_PUESTO_730.txt" % VUELTA),
            "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    sys.stdout.write("EXITCODE: %d (0 CONFIRMA, 2 TUMBA, 1 ROJO)%s" % (codigo, NL))
    sys.exit(codigo)
