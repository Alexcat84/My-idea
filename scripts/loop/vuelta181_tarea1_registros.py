# -*- coding: utf-8 -*-
r"""vuelta181_tarea1_registros.py . LO QUE EL ACTA 180 DEJA SOBRE LA MESA,
LOCALIZADO EN SU FICHERO Y CON SU LINEA, EN VEZ DE RECORDADO.

POR QUE EXISTE, Y LA CAUSA ESTA ESCRITA EN `EJECUTOR.md` 1 CON SU FECHA. La
regla del 14 ago 2026 dice que toda afirmacion sobre el estado del registro
(actas previas, adjudicaciones, rachas) se escribe CON LA MEDICION DEL DIA AL
LADO: la linea del acta leida hoy. Y la regla del 26 ago 2026 dice que TODA
TABLA O CIFRA DEL REPORTE CITA EL FICHERO DE SALIDA DEL QUE SALE Y SE
RECONSTRUYE CONTANDO ESE FICHERO ANTES DE PUBLICARLA. Este fichero produce ese
fichero de salida: la TAREA 1 del reporte de la 181 se pega de aqui, no se
teclea.

QUE HACE, Y ES LO UNICO QUE HACE: abre `docs/loop/ACTA_AUDITOR.md`, localiza LA
CABECERA DEL ACTA 180 (no la teclea: la busca), y desde ahi hacia abajo busca
cada aguja literal de la lista de abajo imprimiendo EL NUMERO DE LINEA y el
texto tal cual. No interpreta, no resume y no decide nada.

LO QUE NO HACE: no toca el acta, no toca el reporte, no toca la nomina, no toca
`docs/plan/` y no corre la bateria. Solo lee y cuenta.

EL SUJETO ESTA CONGELADO EN EL SENTIDO QUE LA CASA PIDE: el acta de una vuelta
ya cerrada no se reescribe, y el numero de vuelta que este fichero busca es un
literal clavado (180), no "la anterior a hoy". Si el acta 180 no estuviera, este
fichero CAE EN ROJO y no inventa ninguna linea.

USO:
  python scripts/loop/vuelta181_tarea1_registros.py
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
NL = chr(10)
VUELTA_AUDITADA = 180
CABECERA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_AUDITADA

# LAS AGUJAS, EN EL ORDEN EN QUE EL ENCARGO LAS PIDE. Cada una es un literal
# que se busca DENTRO del acta 180 y que se imprime CON SU NUMERO DE LINEA.
# Ninguna se parafrasea: si el acta cambiara una palabra, la aguja dejaria de
# encontrarse y esta salida lo diria en vez de seguir publicando la frase vieja.
AGUJAS = [
    ("1.a LA CAIDA E.1, Y ACUMULA",
     "## 5. LA CAIDA DEL EJECUTOR, UNA, Y ACUMULA"),
    ("1.a EL TITULO DE LA E.1",
     "**`E.1`. LA CABECERA DE LA SECCION 9 AFIRMA QUE LA BATERIA CORRIO ENTERA Y SOLA"),
    ("1.a LA RACHA PASA DE CERO A UNO",
     "**ACUMULA. La racha de reporte pasa de CERO a UNO.**"),
    ("1.a LA CAUSA MEDIDA: EL FICHERO DEL HUECO SI EXISTE",
     "**`SALIDA_V180_HUECO_BATERIA.txt`, que SI existe (1.484 bytes, 21 lineas)**"),
    ("1.a LA GUARDA QUE NO CORRIO",
     "**LA GUARDA QUE `AUDITOR.md` 6.1 NOMBRA POR SU NOMBRE NUNCA CORRIO.**"),
    ("1.a LA COMPROBACION DE VUELTA AJENA TAMPOCO MORDIO",
     "**Y LA COMPROBACION DE VUELTA AJENA TAMPOCO MORDIO.**"),
    ("1.a NO ES CAIDA DE CIFRA PUBLICADA",
     "**NO ES CAIDA DE CIFRA\nPUBLICADA Y NO ES PARADA.**"),
    ("1.a LA FILA DE CIFRA PUBLICADA EN LA METRICA",
     "| caidas del ejecutor que ACUMULAN por cifra publicada | **0** |"),
    ("1.a LA FILA DE REPORTE EN LA METRICA",
     "| caidas del ejecutor de reporte | **1** (`E.1`, en cabecera) |"),
    ("1.a LA ESCALADA NO SE DISPARA",
     "**LA ESCALADA NO SE DISPARA Y LO DIGO CON LA CUENTA DELANTE:**"),
    ("1.a D.1 ADJUDICADO A FAVOR, Y EL ERROR ERA DEL ENCARGO",
     "**6.1 `D.1`, QUE `vuelta174_tarea1b_mutacion_esqueleto.py` NO ABRE NINGUN FICHERO"),
    ("1.a D.1, LA CAIDA ES DEL AUDITOR",
     "es **una caida de mi encargo, no suya**"),
    ("1.a D.2 ADJUDICADO A FAVOR",
     "**6.2 `D.2`, LA SEGUNDA COLUMNA DE REALES DE `OP-L-02`: HACIA FALTA"),
    ("1.a D.3 ADJUDICADO A FAVOR",
     "**6.3 `D.3`, QUE LA COLUMNA DE SI UNA CIFRA SE MUEVE DENTRO DE UNA VUELTA NO PUEDE"),
    ("1.a D.4 ADJUDICADO A FAVOR",
     "**6.4 `D.4`, RETIRAR `docs/loop/reportes/REPORTE_V180.md`: CORRECTO"),
    ("1.a D.5 ADJUDICADO A FAVOR",
     "**6.5 `D.5`, `sujeto_congelado_de_git.py` CON NOMBRE ESTABLE Y COMPARTIDO POR TRES"),
    ("1.a LA CAIDA PROPIA DEL AUDITOR, LA TERCERA SEGUIDA",
     "## 2. MI CAIDA PROPIA, DELANTE, Y ES LA TERCERA SEGUIDA DE LA MISMA ESPECIE"),
    ("1.a EL REMEDIO QUE ATA AL AUDITOR DE LA 181",
     "> **TAREA BLOQUEANTE DEL AUDITOR DE LA 181, ANTES DE SU PRIMER COMANDO:**"),
    ("1.b LA P.1 QUEDA ADJUDICADA EN EL 6.6",
     "**6.6 `P.1`, EL ARNES `vuelta172_tarea1c_guarda_que_mordio.py`:"),
    ("1.b LA P.1 NO SE ENCARGA EN LA 181",
     "**NO se encarga en la 181**,"),
    ("1.b EL ALCANCE DE LA 181, ADJUDICACION 6.8",
     "**6.8 EL ALCANCE DE LA VUELTA 181, Y ES ADJUDICACION PORQUE HAY DOS REGLAS"),
    ("1.b LAS DOS SUB-TAREAS Y NADA DE PLAN AL LADO",
     "**DOS sub-tareas: los registros y la bateria"),
    ("1.b EL E.1 Y LA P.1 VAN A LA 182",
     "**van a la\n182**"),
    ("1.b LA CADENCIA: LA PROXIMA ES LA 181",
     "**LA BATERIA: LA PROXIMA ES LA 181, Y ES LA VUELTA QUE VIENE.**"),
    ("1.b EL TOPE: DOS EN LA 181 Y CINCO EN LA 182",
     "**EL TOPE: DOS SUB-TAREAS EN LA 181, POR MI ADJUDICACION 6.8**"),
    ("1.b PARADA: NO",
     "## 11. PARADA: NO"),
]

# LO QUE EL ENCARGO AFIRMA Y ESTE FICHERO NO DA POR BUENO SIN MIRAR. Cada par es
# (lo que el encargo dice, la aguja que lo sostendria). Si la aguja no aparece,
# la salida lo dice y NO se publica la afirmacion.
NO_HAY = [
    ("NO HAY NINGUNA CORRECCION DECLARADA QUE ARRASTRAR",
     "CORRECCION DECLARADA"),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if not os.path.exists(ACTA):
        print("ROJO: no existe %s. No hay acta que citar." % ACTA)
        return 1
    crudo = io.open(ACTA, "rb").read()
    texto = crudo.decode("utf-8").replace(chr(13) + NL, NL)
    lineas = texto.split(NL)

    print("=" * 78)
    print("LO QUE EL ACTA %d DEJA SOBRE LA MESA, CITADO CON SU LINEA" % VUELTA_AUDITADA)
    print("=" * 78)
    print("")
    print("   fichero leido: docs/loop/ACTA_AUDITOR.md")
    print("   CIFRA lineas del fichero entero: %d" % len(lineas))
    print("   CIFRA bytes en disco: %d | bytes normalizados a LF: %d"
          % (os.path.getsize(ACTA), len(texto.encode("utf-8"))))
    print("")

    inicio = None
    for i, l in enumerate(lineas, 1):
        if l.startswith(CABECERA):
            inicio = i
    if inicio is None:
        print("ROJO: no se encuentra la cabecera %r. No se cita nada." % CABECERA)
        return 1
    print("   CABECERA DEL ACTA %d, LOCALIZADA Y NO TECLEADA: LINEA %d"
          % (VUELTA_AUDITADA, inicio))
    print("      %s" % lineas[inicio - 1].strip())
    print("   CIFRA lineas del acta %d (de su cabecera al final del fichero): %d"
          % (VUELTA_AUDITADA, len(lineas) - inicio + 1))
    print("")

    cuerpo = NL.join(lineas[inicio - 1:])
    print("A) LAS AGUJAS, UNA A UNA, CON SU LINEA EN EL FICHERO")
    print("")
    print("| que sostiene | linea | texto del acta, tal cual |")
    print("|---|---:|---|")
    encontradas = 0
    perdidas = []
    for etiqueta, aguja in AGUJAS:
        if aguja not in cuerpo:
            perdidas.append((etiqueta, aguja))
            print("| %s | (no esta) | AGUJA NO ENCONTRADA: %s |"
                  % (etiqueta, repr(aguja)[:90]))
            continue
        encontradas += 1
        # LA LINEA SE CUENTA DEL FICHERO: se mide cuantos saltos de linea hay
        # antes del primer caracter de la aguja, y se suma el desplazamiento de
        # la cabecera. Nada se teclea.
        pos = cuerpo.index(aguja)
        num = inicio + cuerpo[:pos].count(NL)
        primera = aguja.split(NL, 1)[0]
        print("| %s | %d | %s |" % (etiqueta, num, primera.replace("|", " ")[:150]))
    print("")
    print("   CIFRA agujas buscadas: %d" % len(AGUJAS))
    print("   CIFRA agujas ENCONTRADAS: %d" % encontradas)
    print("   CIFRA agujas NO ENCONTRADAS: %d" % len(perdidas))
    for etiqueta, aguja in perdidas:
        print("      PERDIDA: %s -> %s" % (etiqueta, repr(aguja)[:120]))
    print("")

    print("B) LO QUE EL ENCARGO AFIRMA POR AUSENCIA, COMPROBADO Y NO SUPUESTO")
    print("   (EJECUTOR.md 9: una busqueda negativa no se puede citar sin")
    print("    re-verificarla. Aqui se cuenta la aguja dentro del acta 180)")
    for afirmacion, aguja in NO_HAY:
        n = cuerpo.count(aguja)
        print("   %-52s -> apariciones de %r en el acta %d: %d"
              % (afirmacion, aguja, VUELTA_AUDITADA, n))
    print("")

    print("C) LAS ADJUDICACIONES DE LA SECCION 6, CONTADAS DEL FICHERO")
    n_adj = 0
    for i, l in enumerate(lineas[inicio - 1:], inicio):
        if l.startswith("**6.") and "`" in l or (l.startswith("**6.") and " " in l[:8]):
            pass
    for k in range(1, 10):
        marca = "**6.%d " % k
        if marca in cuerpo:
            pos = cuerpo.index(marca)
            num = inicio + cuerpo[:pos].count(NL)
            n_adj += 1
            print("   6.%d -> LINEA %d" % (k, num))
    print("   CIFRA adjudicaciones 6.x localizadas: %d" % n_adj)
    print("")

    print("D) EL VEREDICTO DE ESTE INSTRUMENTO")
    if perdidas:
        print("   ROJO: %d aguja(s) del acta no se encuentran. Lo que sostienen NO SE")
        print("         PUBLICA, y se dice cual falta en vez de escribirla de memoria."
              % ())
        print("FIN")
        return 1
    print("   VERDE: las %d agujas estan en el acta %d y cada una lleva su linea"
          % (len(AGUJAS), VUELTA_AUDITADA))
    print("   contada de este mismo fichero. La TAREA 1 del reporte se pega de aqui.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
