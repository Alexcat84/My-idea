# -*- coding: utf-8 -*-
"""vuelta50_colision_fabricada.py . CONSTRUYE EL LOTE DE LAS CORRECCIONES `P.16`
DE LAS COLISIONES QUE LAS FUSIONES DE ESTA VUELTA FABRICAN.

SUCESOR DECLARADO de scripts/loop/vuelta49_relectura_colisiones.py, del que
hereda el contrato entero y el motivo por el que existe: la razon vieja tiene que
quedar ENTERA dentro de la razon nueva (banco 9.10 y la regla de la casa, una
correccion que tapa lo que corrige no se puede auditar), y transcribir a mano un
parrafo de miles de caracteres es exactamente donde nace una errata. Este
instrumento LEE la razon vieja del archivo y la pega POR MAQUINA, con la formula
del precedente del par 233 (docs/plan/02_DESTEJIDOS.md linea 3372).

LA DIFERENCIA CON EL DE LA VUELTA 49, y es de origen y no de forma: alli las tres
colisiones eran PREEXISTENTES y la relectura conjunta era un encargo del auditor.
Aqui las colisiones LAS FABRICA LA PROPIA FUSION DE ESTA VUELTA, y `P.16` obliga
a que quien fabrica limpie EN EL MISMO ACTO. El carril quedo adjudicado en el
acta de la vuelta 49, pregunta 1: la lectura `P.12` ES la relectura conjunta del
`A` viejo, porque ese `A` se emitio contra un nodo que ya no existe solo.

LO QUE ESTE INSTRUMENTO NO HACE: no decide. La cabecera de cada correccion va
escrita aqui, es la lectura del ejecutor, y se lee y se discute como tal. Lo unico
automatico es el pegado del texto viejo y su guarda.

GUARDA: tras construir, comprueba que la razon vieja aparece LITERAL dentro de la
nueva en TODAS. Si falta una sola, aborta sin escribir el lote.

De solo lectura sobre el archivo de veredictos: escribe el LOTE, no el archivo.
El archivo lo escribe scripts/corregir_veredicto.py, que es el carril adjudicado.

Uso: python scripts/loop/vuelta50_colision_fabricada.py --salida docs/loop/_lote_v50_acto1.jsonl
"""
import argparse
import io
import json
import sys

VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"

COMUN = (
    "CORRECCION DECLARADA EL 19 ago 2026 (vuelta 50), Y LA COLISION QUE LA OBLIGA "
    "LA FABRICO ESTA MISMA VUELTA: SE DICE ASI EN VEZ DE PRESENTARLA COMO HALLAZGO. "
    "LA CLASE CAMBIA: DE A A D. QUE PASO, en orden. La fusion de la PARTE A del acto "
    "1 de OP-U-01 sobre la nomina de hoy (el RACIMO DE LA DERIVA, forma de ESTRELLA "
    "medida en docs/loop/SALIDA_V50_FORMA_MIXTOS.txt) depreco drift_hacia_el_fallo_2 "
    "con alias a normalizacion_de_la_desviacion, que es el superviviente elegido por "
    "CONTENIDO (seis pasos contra cuatro, cuatro condiciones contra dos, y el resumen "
    "mas largo de los cuatro miembros del acto), y que el propio veredicto A del par, "
    "el 2237, ya nombraba con la formula Sobrevive normalizacion_de_la_desviacion. ")

FIN = (
    " Y LA SALIDA NO PIDE DOCTRINA NUEVA, con el carril adjudicado por el auditor en "
    "el acta de la vuelta 49, pregunta 1: LA LECTURA P.12 ES LA RELECTURA CONJUNTA DE "
    "ESTE A, porque este A se emitio contra un nodo que hoy no existe solo, y la "
    "lectura se hizo con los textos vivos delante y esta escrita en el registro del "
    "tramo de docs/plan/03_FUSIONES.md. P.16, QUIEN FABRICA LIMPIA, en el mismo acto y "
    "sin aplazar. El marcador queda recomputado en la misma vuelta y el barrido 9.10 "
    "corrido sobre toda tabla vigente que cite la clase, el marcador o el retrato, que "
    "es la pata que a la vuelta 49 le falto.")

CAB = {}

CAB[2222] = ("D", COMUN + (
    "Desde ese momento este puesto, emitido contra drift_hacia_el_fallo_2, RESUELVE al "
    "par deriva_hacia_el_fallo contra normalizacion_de_la_desviacion, que es "
    "exactamente el par del puesto 2275, que es D. DOS VEREDICTOS, UN PAR RESUELTO, DOS "
    "CLASES: colision de clase, medida hoy con resolutor propio "
    "(docs/loop/SALIDA_V50_CENSO_COLISIONES_ACTO1.txt). LO QUE LA LECTURA P.12 MIDE CON "
    "LOS DOS TEXTOS VIVOS DELANTE, y es lo que decide: el A de este puesto era verdad de "
    "drift_hacia_el_fallo_2, un nodo de CUATRO pasos del que su propio veredicto dice que "
    "dos son los de deriva_hacia_el_fallo y que le quedan DOS LINEAS PROPIAS. El nodo "
    "vivo de hoy tiene OCHO pasos y SEIS condiciones y trae el procedimiento entero de "
    "frenar la normalizacion: los puntos de control periodicos en el calendario, el test "
    "del lenguaje con que se minimiza un riesgo creciente, la revision de si los criterios "
    "de riesgo aceptable se relajaron sin que nadie lo decidiera, y la revision externa que "
    "el puesto 2275 llama la unica linea del racimo que admite que desde dentro no se ve. "
    "Contra ESE nodo, deriva_hacia_el_fallo no repite: aporta LA TEORIA ESTRUCTURAL, como "
    "los sistemas complejos y FUERTEMENTE ACOPLADOS elevan el riesgo de fallo aunque nadie "
    "se equivoque, y la lectura de la exploracion organizacional en busca de eficiencia "
    "contra los limites de seguridad. Eso no es un paso del procedimiento del otro: es un "
    "marco analitico entero que el otro no menciona. La vara del banco 9.22 devuelve "
    "PROCEDIMIENTOS DISTINTOS SOBRE LA MISMA IDEA, que es el caso corriente y no la figura, "
    "y P.12 lo llama CONTINUA: enlace mas poda del solape, no fusion. D."))

CAB[2226] = ("D", COMUN + (
    "Desde ese momento este puesto, emitido contra drift_hacia_el_fallo_2, RESUELVE al "
    "par drift_hacia_el_fallo contra normalizacion_de_la_desviacion, que es exactamente "
    "el par del puesto 2394, que es D. DOS VEREDICTOS, UN PAR RESUELTO, DOS CLASES: "
    "colision de clase, medida hoy con resolutor propio "
    "(docs/loop/SALIDA_V50_CENSO_COLISIONES_ACTO1.txt). LO QUE LA LECTURA P.12 MIDE CON "
    "LOS DOS TEXTOS VIVOS DELANTE: el A de este puesto era verdad de "
    "drift_hacia_el_fallo_2, un nodo de CUATRO pasos del que su propio veredicto dice que "
    "TRES son los de drift_hacia_el_fallo y que le queda UNA linea propia. El nodo vivo de "
    "hoy tiene OCHO pasos y SEIS condiciones. Contra ESE nodo, drift_hacia_el_fallo no "
    "repite: el puesto 2394 reparte los dos con dos verbos y esas palabras, drift VIGILA y "
    "normalizacion FRENA, y nombra lo propio de drift que el otro no tiene, MONITOREAR LA "
    "BRECHA ENTRE PROCEDIMIENTO ESCRITO Y PRACTICA REAL DE FORMA SISTEMATICA Y NO SOLO "
    "CUANDO HAY ACCIDENTES, y CUESTIONAR SI EL EXITO RECIENTE ES SEGURIDAD REAL O SOLO "
    "AUSENCIA DE CONSECUENCIAS HASTA AHORA, que es la trampa central de la deriva. Dos "
    "procedimientos distintos sobre la misma idea: P.12 lo llama CONTINUA, enlace mas poda "
    "del solape, no fusion. D."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por = {r["puesto_intra"]: r for r in V}

    FORMULA = ("LO QUE DECIA LA RAZON VIEJA, y se deja escrita ENTERA para que la "
               "correccion se pueda auditar (copiada del archivo por maquina, no "
               "transcrita): ")

    filas, fallos = [], 0
    for n in sorted(CAB):
        clase, cabecera = CAB[n]
        if n not in por:
            print("ROJO: el puesto %d no esta registrado." % n)
            fallos += 1
            continue
        vieja = por[n]["razon"]
        nueva = cabecera + FIN + " " + FORMULA + vieja + " FIN DE LA RAZON VIEJA."
        if vieja not in nueva:
            print("ROJO: la razon vieja del %d no quedo literal dentro de la nueva." % n)
            fallos += 1
            continue
        print("puesto %d | %s -> %s | %s contra %s | razon %d a %d caracteres"
              % (n, por[n]["clase"], clase, por[n]["nodo_a"], por[n]["nodo_b"],
                 len(vieja), len(nueva)))
        filas.append({"puesto": n, "clase": clase, "razon": nueva})

    if fallos:
        print()
        print("ABORTA: %d en rojo. El lote NO se escribe." % fallos)
        return 1

    with io.open(a.salida, "w", encoding="utf-8", newline="\n") as f:
        for x in filas:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    print()
    print("LOTE ESCRITO: %s (%d filas)" % (a.salida, len(filas)))
    print("La guarda paso en las %d: la razon vieja vive LITERAL dentro de la nueva."
          % len(filas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
