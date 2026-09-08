# -*- coding: utf-8 -*-
r"""_v212_t1b_escribir.py . LA CORRECCION DECLARADA DEL PUESTO 730, VUELTA 212.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo y fuera de la
nomina (congelada en 135). Moratoria de AUDITOR.md 6.3.

NO ARRANCA SOLO: exige que `_v212_t1b_puesto_730.py` haya salido en EXITCODE 0
en esta misma vuelta, o sea que la medicion CONFIRME. Si su salida no existe o
no dice CONFIRMA: SI, este fichero no escribe.

EL CARRIL ES EL DEL BANCO 9.10 Y LA REGLA 8 DE EJECUTOR.md: correccion
DECLARADA, con EL TEXTO VIEJO ENTERO ENCIMA Y SIN TACHAR, y el marcador
RECOMPUTADO con `apertura_del_auditor.marcador()` antes y despues, NUNCA restado
a mano.

EL ORDEN NO SE ALTERA: SIMULACION SOBRE COPIA EN MEMORIA, CASO ROJO POR
MUTACION, y SOLO SI LOS DOS PASAN, ESCRITURA.
"""
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))

import apertura_del_auditor as AP                       # noqa: E402
from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402
from _v211_apertura import shas                         # noqa: E402

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
ARCHIVO = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
RUTA = os.path.join(RAIZ, ARCHIVO.replace("/", os.sep))
PUESTO = 730
CLASE_VIEJA = "A"
CLASE_NUEVA = "D"
SALIDA_MEDICION = os.path.join(RAIZ, "docs", "loop",
                               "SALIDA_V%d_T1B_PUESTO_730.txt" % VUELTA)

CORRECCION = (
    " CORRECCION DECLARADA, relectura conjunta del ejecutor y el auditor en la "
    "vuelta 212 (8 sep 2026): ESTE PUESTO ESTABA EN A Y PASA A D. EL TEXTO VIEJO "
    "QUEDA ENTERO ENCIMA Y SIN TACHAR, porque una correccion que tapa lo que "
    "corrige no se puede auditar. LO QUE CAMBIA NO ES LA LECTURA DEL PAR, que ya "
    "estaba escrita arriba y se sostiene entera, SINO QUE LA REGLA QUE LA DEJABA "
    "SIN RESOLVER YA ESTA RESUELTA: la RATIFICACION del banco 9.6.1 del 12 ago "
    "2026, EL CERO ENTRA EN LA REGLA, dice que cero enlazados es el caso extremo "
    "del mitad-o-menos, que sin ni un hermano enlazado no hay mayoria de la que "
    "tirar, y que entonces la silueta no dice nada y MANDA EL CONTENIDO. La "
    "propia razon de arriba se declaraba a si misma sostenida por la lectura "
    "vieja y anunciaba que por contenido SERIA D: aqui no se cambia de lectura, "
    "se aplica la que el fundador ratifico. "
    "VERIFICADO CONTRA EL GRAFO EN LA VUELTA 212 Y NO CONTRA NINGUN ACTA, "
    "resolviendo a nodo vivo: la madre colaboracion_cadena_suministro tiene UNA "
    "arista de salida, a optimizacion_tecnologia_cadena_suministro, y UNA de "
    "entrada, de sales_operations_planning, y no enlaza a NINGUNO de sus dos "
    "hijos de paso, efecto_bullwhip y compartir_datos_cadena_suministro: CERO DE "
    "DOS. Mirada antes LA FORMA, que es lo que obliga el caveat de la familia "
    "encadenada: ninguno de los dos hijos es alcanzable desde la madre por "
    "aristas de salida hasta tres saltos, asi que no hay cadena que rescate la "
    "silueta y se cuentan los radios. "
    "APLICADA LA VARA EN LA DIRECCION DEL 9.6.2, que pregunta QUE ANADE EL HIJO "
    "A LA MADRE y nunca al reves: quitados los pasos 1 y 2 de la madre, que son "
    "el paso 1 del hijo, al hijo le quedan CINCO de sus seis pasos, el coste en "
    "produccion y en programacion de la operacion, el coste en transporte, "
    "envios y recepcion, cuanto inventario de seguridad hace falta y cuanto "
    "cuesta mantenerlo, cuanto se pierde en ventas por rotura de stock, y la "
    "regla de decision que usa esos cuatro numeros para decidir si vale la pena "
    "invertir. Por la vara del informe 67.6 eso es PROCEDIMIENTO y no LINEA: "
    "cuatro computos de coste sobre bases distintas, cada uno con decisiones "
    "dentro de si y repetido en el tiempo, mas la decision que se alimenta de "
    "los cuatro. CONTINUA, o sea D. Los entregables lo confirman: el del hijo es "
    "un calculo de cuanto cuesta que sirve para decidir la inversion, y el de la "
    "madre es un grafico mas un acuerdo. "
    "Y POR EL OTRO LADO, que no decide pero se mide: a la madre le quedan sus "
    "pasos 3, 4 y 5, determinar su posicion en la cadena, establecer acuerdos de "
    "intercambio de datos y POS, y construir el sistema barato de visibilidad "
    "compartida, que tambien es procedimiento. PROCEDIMIENTO EN LOS DOS LADOS es "
    "par SANO por el 9.6.3, que es otra manera de decir que no es duplicacion. "
    "LA MEDICION ENTERA, con su caso rojo por mutacion del contador de silueta "
    "corrido ANTES de escribir, en docs/loop/SALIDA_V212_T1B_PUESTO_730.txt. "
    "Marcador recomputado con apertura_del_auditor.marcador() antes y despues, "
    "nunca restado a mano."
)

OUT = []


def di(s=""):
    OUT.append(s)


def sede(cuando):
    m = medir_en_disco(RAIZ, ARCHIVO)
    sd, sl = shas(ARCHIVO)
    igual = "COINCIDEN" if m[0] == m[1] else "NO COINCIDEN"
    di("CIFRA sede %s %s: %d bytes en disco y %d normalizado a LF (%s), "
       "sha256 disco %s y sha256 LF %s" % (ARCHIVO, cuando, m[0], m[1], igual, sd, sl))
    return sd, sl


def juzgar(lineas_viejas, lineas_nuevas, clase_esperada, exigir_texto_viejo=True):
    """LA GUARDA. PURA: recibe las dos listas de lineas y devuelve (fallos, informe).
    No lee ni escribe disco, y por eso se la puede correr sobre una copia mutada."""
    inf = []
    fallos = 0

    viejas = [l for l in lineas_viejas if l.strip()]
    nuevas = [l for l in lineas_nuevas if l.strip()]
    inf.append("   filas antes %d, filas despues %d (se exige que sean iguales)"
               % (len(viejas), len(nuevas)))
    if len(viejas) != len(nuevas):
        fallos += 1

    distintas = [i for i in range(min(len(viejas), len(nuevas)))
                 if viejas[i] != nuevas[i]]
    inf.append("   lineas distintas: %d (se exige 1)" % len(distintas))
    if len(distintas) != 1:
        fallos += 1
        return fallos, inf

    i = distintas[0]
    a = json.loads(viejas[i])
    b = json.loads(nuevas[i])
    inf.append("   la linea distinta es el puesto %s (se exige %d)"
               % (b.get("puesto_intra"), PUESTO))
    if b.get("puesto_intra") != PUESTO or a.get("puesto_intra") != PUESTO:
        fallos += 1

    cambiados = sorted(k for k in set(list(a) + list(b)) if a.get(k) != b.get(k))
    inf.append("   campos que cambian: %s (se exigen exactamente clase y razon)"
               % (", ".join(cambiados) or "ninguno"))
    if cambiados != ["clase", "razon"]:
        fallos += 1

    inf.append("   clase antes %r, clase despues %r (se exige %r y %r)"
               % (a.get("clase"), b.get("clase"), CLASE_VIEJA, clase_esperada))
    if a.get("clase") != CLASE_VIEJA or b.get("clase") != clase_esperada:
        fallos += 1

    entero = (b.get("razon") or "").startswith(a.get("razon") or "")
    inf.append("   el texto viejo esta ENTERO Y ENCIMA (la razon nueva empieza por la "
               "vieja, byte a byte): %s" % ("SI" if entero else "NO"))
    if exigir_texto_viejo and not entero:
        fallos += 1

    largos = (b.get("razon") or "").count(chr(8212))
    medios = (b.get("razon") or "").count(chr(8211))
    inf.append("   guiones largos %d, guiones medios %d (se exige 0 y 0)"
               % (largos, medios))
    if largos or medios:
        fallos += 1

    return fallos, inf


def main():
    di("=" * 78)
    di("TAREA 1.b DE LA VUELTA %d. LA ESCRITURA DE LA CORRECCION DEL PUESTO %d."
       % (VUELTA, PUESTO))
    di("=" * 78)
    di("")

    di("## 0. LA PUERTA: SIN MEDICION QUE CONFIRME, ESTE FICHERO NO ESCRIBE")
    if not os.path.isfile(SALIDA_MEDICION):
        di("ROJO: no existe %s. No se escribe nada." % SALIDA_MEDICION)
        return 1
    med = io.open(SALIDA_MEDICION, encoding="utf-8").read()
    bytes_med = os.path.getsize(SALIDA_MEDICION)
    confirma = "CONFIRMA: SI" in med
    di("CIFRA bytes de la salida de la medicion: %d" % bytes_med)
    di("CIFRA la medicion dice CONFIRMA: SI: %s" % ("SI" if confirma else "NO"))
    if not confirma or bytes_med == 0:
        di("ROJO: la medicion no confirma o esta vacia. No se escribe nada.")
        return 1
    di("")

    di("## 1. LA ENTRADA")
    raw = io.open(RUTA, encoding="utf-8", newline="").read()
    lineas = raw.split(NL)
    filas = [json.loads(l) for l in lineas if l.strip()]
    di("CIFRA filas AL ENTRAR: %d" % len(filas))
    sd0, sl0 = sede("AL ENTRAR")
    m0 = AP.marcador()
    di("CIFRA marcador AL ENTRAR, con apertura_del_auditor.marcador(): %d filas; %s"
       % (m0["filas"], ", ".join("%s %d" % (k, m0["por_clase"][k])
                                 for k in sorted(m0["por_clase"]))))
    di("")

    idx = [i for i, l in enumerate(lineas)
           if l.strip() and json.loads(l).get("puesto_intra") == PUESTO]
    di("CIFRA indices de linea con el puesto %d: %d (se exige 1) -> %s"
       % (PUESTO, len(idx), idx))
    if len(idx) != 1:
        di("ROJO: el puesto no es unico.")
        return 1
    i = idx[0]
    fila = json.loads(lineas[i])
    di("CIFRA round-trip de json.dumps sobre la fila vieja identico a su linea: %s"
       % ("SI" if json.dumps(fila, ensure_ascii=False) == lineas[i] else "NO"))
    if json.dumps(fila, ensure_ascii=False) != lineas[i]:
        di("ROJO: la serializacion de la casa no reproduce la linea. No se escribe.")
        return 1
    di("")

    # ==================================================================
    # 2. LA SIMULACION SOBRE COPIA EN MEMORIA
    # ==================================================================
    di("## 2. LA SIMULACION SOBRE COPIA EN MEMORIA, ANTES DE TOCAR EL DISCO")
    nueva = dict(fila)
    nueva["clase"] = CLASE_NUEVA
    nueva["razon"] = fila["razon"] + CORRECCION
    lineas_sim = list(lineas)
    lineas_sim[i] = json.dumps(nueva, ensure_ascii=False)
    di("CIFRA bytes de la razon vieja %d, de la razon nueva %d, de lo anadido %d"
       % (len(fila["razon"].encode("utf-8")),
          len(nueva["razon"].encode("utf-8")),
          len(CORRECCION.encode("utf-8"))))
    fallos, inf = juzgar(lineas, lineas_sim, CLASE_NUEVA)
    for l in inf:
        di(l)
    di("CIFRA fallos de la simulacion: %d (se exige 0)" % fallos)
    di("")

    marc_sim = {}
    for l in lineas_sim:
        if not l.strip():
            continue
        c = json.loads(l)["clase"]
        marc_sim[c] = marc_sim.get(c, 0) + 1
    di("CIFRA marcador SIMULADO sobre la copia en memoria: %d filas; %s"
       % (sum(marc_sim.values()),
          ", ".join("%s %d" % (k, marc_sim[k]) for k in sorted(marc_sim))))
    di("CIFRA el simulado mueve exactamente una A a una D contra el de entrada: %s"
       % ("SI" if (marc_sim.get("A") == m0["por_clase"]["A"] - 1
                   and marc_sim.get("D") == m0["por_clase"]["D"] + 1
                   and sum(marc_sim.values()) == m0["filas"]) else "NO"))
    di("")

    # ==================================================================
    # 3. EL CASO ROJO POR MUTACION
    # ==================================================================
    di("## 3. EL CASO ROJO POR MUTACION, CORRIDO ANTES DE ESCRIBIR NADA")
    di("(EJECUTOR.md 1: ningun assert se publica como prueba sin haber corrido su")
    di("prueba de mutacion. Se muta LA ESCRITURA, no el valor esperado, y se exige")
    di("que la MISMA guarda que acaba de decir VERDE diga ROJO.)")
    di("")
    rojos = []

    # MUTANTE 1: la correccion TAPA el texto viejo en vez de ir encima.
    m1 = list(lineas)
    f1 = dict(fila)
    f1["clase"] = CLASE_NUEVA
    f1["razon"] = CORRECCION.strip()
    m1[i] = json.dumps(f1, ensure_ascii=False)
    n1, i1 = juzgar(lineas, m1, CLASE_NUEVA)
    di("MUTANTE 1, la correccion TAPA el texto viejo: fallos %d (se exige >0)" % n1)
    for l in i1:
        di("  " + l)
    rojos.append(n1 > 0)
    di("")

    # MUTANTE 2: se toca una segunda fila ademas de la del 730.
    m2 = list(lineas_sim)
    otra = [k for k, l in enumerate(lineas)
            if l.strip() and json.loads(l).get("puesto_intra") == 731][0]
    f2 = json.loads(m2[otra])
    f2["razon"] = f2["razon"] + " (toque de mentira del mutante 2)"
    m2[otra] = json.dumps(f2, ensure_ascii=False)
    n2, i2 = juzgar(lineas, m2, CLASE_NUEVA)
    di("MUTANTE 2, se toca ademas la fila del 731: fallos %d (se exige >0)" % n2)
    for l in i2:
        di("  " + l)
    rojos.append(n2 > 0)
    di("")

    # MUTANTE 3: se cambia la clase a una que la vara no devuelve.
    m3 = list(lineas)
    f3 = dict(fila)
    f3["clase"] = "B"
    f3["razon"] = fila["razon"] + CORRECCION
    m3[i] = json.dumps(f3, ensure_ascii=False)
    n3, i3 = juzgar(lineas, m3, CLASE_NUEVA)
    di("MUTANTE 3, la clase escrita es B y no la D que la vara devuelve: fallos %d "
       "(se exige >0)" % n3)
    for l in i3:
        di("  " + l)
    rojos.append(n3 > 0)
    di("")

    # MUTANTE 4: se toca un campo que no se puede tocar.
    m4 = list(lineas)
    f4 = dict(fila)
    f4["clase"] = CLASE_NUEVA
    f4["razon"] = fila["razon"] + CORRECCION
    f4["clave"] = 0.9999
    m4[i] = json.dumps(f4, ensure_ascii=False)
    n4, i4 = juzgar(lineas, m4, CLASE_NUEVA)
    di("MUTANTE 4, ademas de clase y razon se mueve el campo clave: fallos %d "
       "(se exige >0)" % n4)
    for l in i4:
        di("  " + l)
    rojos.append(n4 > 0)
    di("")

    di("CIFRA mutantes corridos: %d. CIFRA mutantes que CAEN en rojo: %d "
       "(se exige que caigan todos)" % (len(rojos), len([x for x in rojos if x])))
    di("EL CASO ROJO %s"
       % ("SE COMPORTA: la guarda dice VERDE sobre lo correcto y ROJO sobre las "
          "cuatro escrituras equivocadas."
          if all(rojos) else
          "NO SE COMPORTA, Y ESO INVALIDA LA GUARDA. NO SE ESCRIBE."))
    di("")

    if fallos or not all(rojos):
        di("ROJO: NO SE ESCRIBE NADA. El archivo del disco queda intacto.")
        return 1

    # ==================================================================
    # 4. LA ESCRITURA
    # ==================================================================
    di("## 4. LA ESCRITURA, QUE SOLO LLEGA AQUI CON LA SIMULACION EN VERDE Y LOS")
    di("   CUATRO MUTANTES EN ROJO")
    texto_nuevo = NL.join(lineas_sim)
    io.open(RUTA, "w", encoding="utf-8", newline="").write(texto_nuevo)
    di("ESCRITO %s" % ARCHIVO)
    di("")

    di("## 5. LA SALIDA, RELEIDA DEL DISCO LINEA A LINEA")
    raw2 = io.open(RUTA, encoding="utf-8", newline="").read()
    lineas2 = raw2.split(NL)
    filas2 = [json.loads(l) for l in lineas2 if l.strip()]
    di("CIFRA filas AL SALIR: %d (se exige %d)" % (len(filas2), len(filas)))
    di("CIFRA lo escrito es identico a lo juzgado: %s"
       % ("SI" if raw2 == texto_nuevo else "NO"))
    fallos2, inf2 = juzgar(lineas, lineas2, CLASE_NUEVA)
    for l in inf2:
        di(l)
    di("CIFRA fallos de la guarda SOBRE EL DISCO: %d (se exige 0)" % fallos2)
    sd1, sl1 = sede("AL SALIR")
    di("CIFRA el sha256 cambia entre entrada y salida: %s (se exige SI)"
       % ("SI" if sd1 != sd0 else "NO"))
    m1m = AP.marcador()
    di("CIFRA marcador AL SALIR, con apertura_del_auditor.marcador(): %d filas; %s"
       % (m1m["filas"], ", ".join("%s %d" % (k, m1m["por_clase"][k])
                                  for k in sorted(m1m["por_clase"]))))
    di("CIFRA el marcador del disco calza con el que la simulacion predijo: %s"
       % ("SI" if m1m["por_clase"] == marc_sim and m1m["filas"] == sum(marc_sim.values())
          else "NO"))
    fila2 = [f for f in filas2 if f["puesto_intra"] == PUESTO][0]
    di("CIFRA clase del %d AL SALIR: %s" % (PUESTO, fila2["clase"]))
    di("CIFRA bytes de la razon del %d AL SALIR: %d"
       % (PUESTO, len(fila2["razon"].encode("utf-8"))))
    ruta_marc, _ = AP.sellar_marcador("%d_T1B" % VUELTA)
    di("CIFRA salida sellada del marcador: %s (%d bytes)"
       % (os.path.relpath(ruta_marc, RAIZ).replace(os.sep, "/"),
          os.path.getsize(ruta_marc)))
    ok = (fallos2 == 0 and raw2 == texto_nuevo and sd1 != sd0
          and len(filas2) == len(filas))
    di("")
    di("VERDE: la correccion del %d queda DECLARADA, con el texto viejo entero "
       "encima." % PUESTO if ok else "ROJO: la salida no calza con lo juzgado.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    codigo = main()
    texto = NL.join(OUT) + NL
    io.open(os.path.join(RAIZ, "docs", "loop",
                         "SALIDA_V%d_T1B_ESCRIBIR.txt" % VUELTA),
            "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    sys.stdout.write("EXITCODE: %d%s" % (codigo, NL))
    sys.exit(codigo)
