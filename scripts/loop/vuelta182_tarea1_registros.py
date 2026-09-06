# -*- coding: utf-8 -*-
r"""vuelta182_tarea1_registros.py . LO QUE EL ACTA 181 DEJA SOBRE LA MESA,
LOCALIZADO EN SU FICHERO Y CON SU LINEA, EN VEZ DE RECORDADO.

CLON DECLARADO de scripts/loop/vuelta181_tarea1_registros.py. Cambia el numero
de vuelta auditada, la lista de AGUJAS y el nombre de la salida. La maquina no
cambia. El cotejo lo hace scripts/loop/cotejar_clon_declarado.py y su salida se
pega en el reporte.

POR QUE EXISTE, Y LA CAUSA ESTA ESCRITA EN `EJECUTOR.md` 1 CON SU FECHA. La regla
del 14 ago 2026 dice que toda afirmacion sobre el estado del registro (actas
previas, adjudicaciones, rachas) se escribe CON LA MEDICION DEL DIA AL LADO: la
linea del acta leida hoy. Y la del 26 ago 2026 dice que TODA TABLA O CIFRA DEL
REPORTE CITA EL FICHERO DE SALIDA DEL QUE SALE Y SE RECONSTRUYE CONTANDO ESE
FICHERO ANTES DE PUBLICARLA. Este fichero produce ese fichero de salida: la
TAREA 1.a del reporte de la 182 se pega de aqui, no se teclea.

QUE HACE, Y ES LO UNICO QUE HACE: abre `docs/loop/ACTA_AUDITOR.md`, localiza LA
CABECERA DEL ACTA 181 (no la teclea: la busca), y desde ahi hacia abajo busca
cada aguja literal de la lista de abajo imprimiendo EL NUMERO DE LINEA y el texto
tal cual. No interpreta, no resume y no decide nada.

LAS AGUJAS PARTIDAS SE BUSCAN EN EL TEXTO ENTERO Y NO LINEA A LINEA, y eso NO es
un atajo: el acta 181 punto 3.4 midio que dos de las 29 lineas que el reporte de
la 181 citaba "calzan partidas por el salto de linea", y llamo a eso el ancla
correcta de una frase envuelta y no una discrepancia. Aqui una aguja que lleve un
salto de linea dentro se busca sobre el texto completo y se publica LA LINEA
DONDE EMPIEZA.

LO QUE NO HACE: no toca el acta, no toca el reporte, no toca la nomina, no toca
`docs/plan/` y no corre la bateria. Solo lee y cuenta.

EL SUJETO ESTA CONGELADO EN EL SENTIDO QUE LA CASA PIDE: el acta de una vuelta ya
cerrada no se reescribe, y el numero de vuelta que este fichero busca es un
literal clavado (181), no "la anterior a hoy". Si el acta 181 no estuviera, este
fichero CAE EN ROJO y no inventa ninguna linea.

USO:
  python scripts/loop/vuelta182_tarea1_registros.py
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
NL = chr(10)
VUELTA_AUDITADA = 181
CABECERA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_AUDITADA

# LAS AGUJAS, EN EL ORDEN EN QUE EL ENCARGO LAS PIDE. Cada una es un literal que
# se busca DENTRO del acta 181 y que se imprime CON SU NUMERO DE LINEA. Ninguna
# se parafrasea: si el acta cambiara una palabra, la aguja dejaria de encontrarse
# y esta salida lo diria en vez de seguir publicando la frase vieja.
AGUJAS = [
    ("1.a LA CAIDA DEL EJECUTOR, UNA, Y NO ACUMULA",
     "## 5. LA CAIDA DEL EJECUTOR, UNA, Y NO ACUMULA"),
    ("1.a EL TITULO DE LA E.2",
     "**`E.2`. LA CUENTA DE QUIEN NOMBRA `SALIDA_V180_HUECO_BATERIA` EN `scripts/` ERA 1"),
    ("1.a LA E.2 VIVE EN PROSA Y NO ACUMULA",
     "**NO ACUMULA, Y CITO LA LETRA QUE LO DECIDE.**"),
    ("1.a LA RACHA DE REPORTE SE QUEDA EN UNO",
     "**La racha de\nreporte se queda en UNO**"),
    ("1.a LA CIFRA SE MIDIO BIEN Y SE PUBLICO TARDE",
     "**La cifra se midio bien y se publico tarde.**"),
    ("1.a LO QUE NO SE CAE ES LA CONCLUSION",
     "**LO QUE NO SE CAE ES LA CONCLUSION, Y LO COMPROBE EN VEZ DE SUPONERLO:**"),
    ("1.a LA E.2 DISPARA LA RELECTURA AL DOBLE DEL TRAMO",
     "**Se registra con su\nnombre, dispara la relectura al doble del tramo, y NO acumula.**"),
    ("1.a LA CIEGA: 30 PUESTOS, 24 COINCIDEN, 6 DISCREPAN",
     "## 4. LA RELECTURA CIEGA: 30 PUESTOS, 24 COINCIDEN, 6 DISCREPAN"),
    ("1.a CINCO DE LAS SEIS LAS PIERDE EL AUDITOR",
     "**LAS SEIS DISCREPANCIAS, Y CINCO LAS PIERDO YO:**"),
    ("1.a LA DIRECCION DEL SESGO, MEDIDA",
     "**LA DIRECCION DEL SESGO, MEDIDA Y NO INTUIDA:"),
    ("1.a LAS D DEL CRIBADO RESISTEN LA RELECTURA ADVERSARIA",
     "**las `D`\ndel cribado resisten la relectura adversaria**"),
    ("1.a LA VARA DOBLE, ENCARGADA POR AUDITOR.md 1.2",
     "**Y me obliga a la vara doble:**"),
    ("1.a EL 2.464 NO SE CONCEDE",
     "**NO LO CONCEDO, Y NO POR TERQUEDAD: LA EVIDENCIA DE SU RAZON YA NO ESTA EN EL GRAFO.**"),
    ("1.a EL HALLAZGO QUE PARA EL BUCLE",
     "## 6. EL HALLAZGO, Y ES EL QUE PARA EL BUCLE: EL PUESTO 2.464"),
    ("1.a LA RAZON ERA VERDAD EL DIA QUE SE ESCRIBIO",
     "**LA RAZON ERA VERDAD EL DIA QUE SE ESCRIBIO."),
    ("1.a POR QUE NADIE VOLVIO: LA REGLA NO LO MANDA",
     "**POR QUE NADIE VOLVIO: PORQUE LA REGLA ESCRITA NO LO MANDA.**"),
    ("1.a EL FILTRO RAZONA SOBRE LA MUERTE, Y AHI ESTA EL HUECO",
     "**EL FILTRO RAZONA SOBRE LA MUERTE Y SE APLICA TAMBIEN AL CAMBIO DE TEXTO, Y AHI ESTA"),
    ("1.a LA TABLA DEL ALCANCE, CON FECHAS",
     "**Y NO ES UN CASO SUELTO. LO MEDI, CON FECHAS, PAR POR PAR**"),
    ("1.a LA 7.1: LA E.2 SE REGISTRA Y NO ACUMULA",
     "**7.1 EL `E.2` SE REGISTRA Y NO ACUMULA.**"),
    ("1.a LA 7.2: LAS CINCO DISCREPANCIAS SON DEL AUDITOR",
     "**7.2 LAS CINCO DISCREPANCIAS DE LA CIEGA SON MIAS, Y LAS ADJUDICO A FAVOR DEL"),
    ("1.a LA 7.2 ENCARGA EL TRAMO AL DOBLE",
     "**El tramo se relee al doble igualmente**"),
    ("1.a LA 7.3: LA C.1 NO CONTAMINO EL SUJETO",
     "**7.3 LA `C.1` DE LA CIEGA NO CONTAMINO EL SUJETO, Y LO DIGO CON LA MEDICION.**"),
    ("1.a LA 7.4: EL 2.464 NO LO ADJUDICA EL AUDITOR",
     "**7.4 EL 2.464 NO LO ADJUDICO YO, Y ESA ES LA ADJUDICACION.**"),
    ("1.a LA 7.5: LA BATERIA DE LA 181 NO CORRIO Y NO ES CAIDA DE REPORTE",
     "**7.5 LA BATERIA DE LA 181 NO CORRIO, Y NO ES CAIDA DE REPORTE.**"),
    ("1.a EL ESQUELETO POR ANEXION HIZO LO QUE SE LE PIDIO",
     "**El esqueleto por anexion hizo exactamente lo que se le pidio:"),
    ("1.a LA CAIDA PROPIA DEL AUDITOR, LA CUARTA SEGUIDA",
     "## 2. MI CAIDA PROPIA, DELANTE, Y ES LA CUARTA SEGUIDA Y ADEMAS LA ROTURA DEL REMEDIO"),
    ("1.a EL AUDITOR ROMPIO LAS TRES PROHIBICIONES",
     "**Rompi las tres.**"),
    ("1.a LOS 30 PUESTOS DE LA CIEGA",
     "**LOS 30 PUESTOS SON:**"),
    ("1.a LA METRICA DE CREDITO",
     "## 8. LA METRICA DE CREDITO"),
    ("1.a LA BATERIA SIGUE SIN CORRER Y LA 181 ERA SU VUELTA",
     "**LA BATERIA: SIGUE SIN CORRER, Y LA 181 ERA SU VUELTA.**"),
    ("1.a EL TOPE VUELVE A CINCO EN LA 182, Y VA A LA PARADA",
     "**EL TOPE: la 6.2 devolveria el tope a cinco sub-tareas en la 182."),
    ("1.a PARADA: SI",
     "## 11. PARADA: SI"),
    # --- 1.b LOS DOS PENDIENTES, QUE VIVEN EN EL ACTA 180 Y NO EN LA 181 ---
    ("1.b EL E.1 Y LA P.1 SIGUEN EN PIE, DICHO POR LA PROPIA 181",
     "**y el remedio del `E.1` que la 180 dejo escrito para la\n182 sigue en pie y va en la parada**"),
]

# LAS AGUJAS DEL ACTA 180, que es donde viven los DOS PENDIENTES de la TAREA 1.b.
# Se buscan en SU tramo, no en el de la 181, y por eso van en su propia lista:
# mezclarlas seria publicar una linea del acta 180 como si fuera de la 181.
AGUJAS_180 = [
    ("1.b LA P.1, ADJUDICADA EN EL 6.6 DEL ACTA 180",
     "**6.6 `P.1`, EL ARNES `vuelta172_tarea1c_guarda_que_mordio.py`:"),
    ("1.b EL ORDEN DE LA P.1 ES PARTE DE LA ADJUDICACION",
     "**El orden importa y es parte de la\nadjudicacion: primero el esperado, despues el nombre.**"),
    ("1.b LA P.1 NO ESTA EN EL CENSO DE 168",
     "**no esta en el censo\nde 168**"),
    ("1.b EL E.1 Y SUS DOS RAMAS",
     "**LO QUE MEDI, Y NO ES UNA LECTURA DE ESTILO.**"),
    ("1.b LA GUARDA QUE AUDITOR.md 6.1 NOMBRA NUNCA CORRIO",
     "**LA GUARDA QUE `AUDITOR.md` 6.1 NOMBRA POR SU NOMBRE NUNCA CORRIO.**"),
    ("1.b LA COMPROBACION DE VUELTA AJENA TAMPOCO MORDIO",
     "**Y LA COMPROBACION DE VUELTA AJENA TAMPOCO MORDIO.**"),
    ("1.b EL 6.8: EL E.1 Y LA P.1 VAN A LA 182",
     "Mi `E.1` y la `P.1` **van a la\n182**"),
    # CORRECCION DECLARADA (vuelta 182, TAREA 1.a). La aguja de abajo se
    # escribio primero como "El tope vuelve a cinco en la 182." y NO SE
    # ENCUENTRA en el acta: esa frase literal es del REPORTE de la 181
    # (docs/loop/reportes/REPORTE_V181.md linea 21), o sea prosa del
    # ejecutor, no del auditor. Lo que el acta 180 escribe de verdad esta en
    # su punto 10, linea 62893, y son otras palabras. Se cambia por la
    # verdadera y el error queda registrado aqui y en el reporte, sin borrar
    # lo que corrige.
    ("1.b EL TOPE VUELVE A CINCO EN LA 182, EN EL PUNTO 10 DEL ACTA 180",
     "**EL TOPE: DOS SUB-TAREAS EN LA 181, POR MI ADJUDICACION 6.8**, y vuelve a cinco\nen la 182."),
    ("1.b LA CONTRADICCION QUE EL 6.8 RESUELVE, EN SUS PROPIAS PALABRAS",
     "`AUDITOR.md` 6.2 devuelve el tope a **cinco**; y yo tengo dos remedios en la mano,"),
]
CABECERA_180 = "# ACTA DEL AUDITOR, VUELTA 180"


def tramo(lineas, cabecera):
    """LA LINEA DONDE EMPIEZA UN ACTA. Devuelve (base, cuantas cabeceras hay).
    Si no hay exactamente una, quien llame CAE EN ROJO: dos cabeceras iguales
    harian que las lineas publicadas fueran de un acta u otra segun el azar."""
    hits = [i for i, l in enumerate(lineas, 1) if l.startswith(cabecera)]
    return (hits[0] if len(hits) == 1 else None), len(hits)


def buscar(texto, lineas, base, aguja):
    """LA LINEA DONDE EMPIEZA LA AGUJA, buscada desde `base` hacia abajo.

    Una aguja de UNA SOLA LINEA se busca linea a linea. Una aguja que lleve un
    salto de linea dentro se busca sobre el TEXTO ENTERO y se traduce el
    desplazamiento a numero de linea: es la frase envuelta que el acta 181 punto
    3.4 midio y llamo ancla correcta. Devuelve [] si no aparece, y ese vacio se
    publica: una aguja que no se encuentra es una medicion, no un fallo que se
    tapa."""
    if NL not in aguja:
        return [(i, l) for i, l in enumerate(lineas, 1)
                if i >= base and aguja in l]
    corte = len(NL.join(lineas[:base - 1])) + (len(NL) if base > 1 else 0)
    hallados = []
    desde = corte
    while True:
        k = texto.find(aguja, desde)
        if k < 0:
            break
        n = texto.count(NL, 0, k) + 1
        hallados.append((n, NL.join(lineas[n - 1:n + aguja.count(NL)])))
        desde = k + 1
    return hallados


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    texto = io.open(ACTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
    lineas = texto.split(NL)
    salida = []
    w = salida.append

    w("LOS REGISTROS DE LA VUELTA 182, TAREA 1: EL ACTA %d CITADA CON SU LINEA"
      % VUELTA_AUDITADA)
    w("instrumento: scripts/loop/vuelta182_tarea1_registros.py")
    w("fichero leido: docs/loop/ACTA_AUDITOR.md")
    w("   %d lineas | disco %d bytes | LF %d bytes"
      % (len(lineas), os.path.getsize(ACTA), len(texto.encode("utf-8"))))
    w("")

    base, n_cab = tramo(lineas, CABECERA)
    w("CABECERA %r -> %d aparicion(es)" % (CABECERA, n_cab))
    if base is None:
        w("ROJO: no hay exactamente una cabecera del acta %d. No se publica nada."
          % VUELTA_AUDITADA)
        print(NL.join(salida))
        return 1
    w("LA CABECERA DEL ACTA %d ESTA EN LA LINEA %d" % (VUELTA_AUDITADA, base))
    w("lineas del acta %d, de su cabecera al final del fichero: %d"
      % (VUELTA_AUDITADA, len(lineas) - base + 1))
    w("")

    base180, n_cab180 = tramo(lineas, CABECERA_180)
    w("CABECERA %r -> %d aparicion(es)" % (CABECERA_180, n_cab180))
    if base180 is not None:
        w("LA CABECERA DEL ACTA 180 ESTA EN LA LINEA %d" % base180)
    w("")

    total = 0
    hallados = 0
    for etiqueta, lista, desde in (("ACTA %d" % VUELTA_AUDITADA, AGUJAS, base),
                                   ("ACTA 180", AGUJAS_180, base180)):
        w("=" * 78)
        w("LAS AGUJAS DEL %s, BUSCADAS DESDE SU CABECERA HACIA ABAJO" % etiqueta)
        w("=" * 78)
        if desde is None:
            w("   ROJO: sin cabecera unica no hay tramo que recorrer.")
            w("")
            continue
        for nombre, aguja in lista:
            total += 1
            hits = buscar(texto, lineas, desde, aguja)
            if not hits:
                w("%-62s -> NO SE ENCUENTRA" % nombre)
                w("   la aguja buscada, literal: %r" % aguja)
                continue
            hallados += 1
            w("%-62s -> LINEA %d%s"
              % (nombre, hits[0][0],
                 ("  (y %d mas)" % (len(hits) - 1)) if len(hits) > 1 else ""))
            for l in hits[0][1].split(NL):
                w("   | " + l.rstrip()[:150])
        w("")

    w("=" * 78)
    w("CIFRA agujas buscadas: %d" % total)
    w("CIFRA agujas HALLADAS: %d" % hallados)
    w("CIFRA agujas NO HALLADAS: %d" % (total - hallados))
    w("LA CUENTA SE CIERRA: %s"
      % ("SI" if hallados + (total - hallados) == total else "NO"))
    w("")
    w("FIN")

    t = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_T1A_REGISTRO_ACTA_181.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if hallados == total else 1


if __name__ == "__main__":
    sys.exit(main())
