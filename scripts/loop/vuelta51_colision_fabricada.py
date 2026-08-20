# -*- coding: utf-8 -*-
"""vuelta51_colision_fabricada.py . CONSTRUYE EL LOTE DE LAS CORRECCIONES `P.16`
DE LAS COLISIONES QUE EL LOTE A DE ESTA VUELTA FABRICA.

SUCESOR DECLARADO de scripts/loop/vuelta50_colision_fabricada.py, del que hereda
el contrato entero: la razon vieja tiene que quedar ENTERA dentro de la razon
nueva (banco 9.10 y la regla de la casa, una correccion que tapa lo que corrige
no se puede auditar), y se PEGA POR MAQUINA leyendola del archivo, porque
transcribir a mano un parrafo de miles de caracteres es donde nace una errata.

EL CARRIL, adjudicado en el acta de la vuelta 49, pregunta 1, y usado igual en la
vuelta 50: LA LECTURA `P.12` ES LA RELECTURA CONJUNTA DEL `A` VIEJO, porque ese
`A` se emitio contra un nodo que hoy no existe solo. Aqui vale sin estirar nada:
los dos puestos que se voltean son veredictos contra un absorbido, y el par que
resuelven es exactamente el par que la lectura `P.12` de este lote leyo.

LO QUE ESTE INSTRUMENTO NO HACE: no decide. La cabecera de cada correccion va
escrita aqui, es la lectura del ejecutor, y se lee y se discute como tal.

GUARDA: tras construir, comprueba que la razon vieja aparece LITERAL dentro de la
nueva en TODAS. Si falta una sola, aborta sin escribir el lote.

De solo lectura sobre el archivo de veredictos: escribe el LOTE, no el archivo.
El archivo lo escribe scripts/corregir_veredicto.py, que es el carril adjudicado.

Uso: python scripts/loop/vuelta51_colision_fabricada.py --salida docs/loop/_lote_v51_lote_a.jsonl
"""
import argparse
import io
import json
import sys

VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"

FIN = (
    " Y LA SALIDA NO PIDE DOCTRINA NUEVA, con el carril adjudicado por el auditor en "
    "el acta de la vuelta 49, pregunta 1, y usado igual en la vuelta 50: LA LECTURA "
    "P.12 ES LA RELECTURA CONJUNTA DE ESTE A, porque este A se emitio contra un nodo "
    "que hoy no existe solo, y la lectura se hizo con los textos vivos delante y esta "
    "escrita en el registro del tramo de docs/plan/03_FUSIONES.md. P.16, QUIEN FABRICA "
    "LIMPIA, en el mismo acto y sin aplazar. El marcador queda recomputado en la misma "
    "vuelta y el barrido 9.10 corrido sobre toda tabla vigente que cite la clase, el "
    "marcador o el retrato, despues del ultimo movimiento de la vuelta.")

CAB = {}

CAB[2426] = ("D", (
    "CORRECCION DECLARADA EL 20 ago 2026 (vuelta 51), Y LA COLISION QUE LA OBLIGA LA "
    "FABRICO ESTA MISMA VUELTA: SE DICE ASI EN VEZ DE PRESENTARLA COMO HALLAZGO. LA "
    "CLASE CAMBIA: DE A A D. QUE PASO, en orden. La fusion de la PARTE A del acto 1 de "
    "OP-U-01 sobre la nomina de la apertura de esta vuelta (la familia accion_correctiva "
    "de quality) depreco accion_correctiva_5 y accion_correctiva_6 con alias a "
    "accion_correctiva_sistematica, que es el superviviente elegido por CONTENIDO con el "
    "veredicto DIRECTO del par mas disputado a favor: el puesto 2431 leyo los dos textos "
    "y cierra con Sobrevive accion_correctiva_sistematica, y nombra lo que solo el "
    "elegido trae, la cadencia de tres niveles con entregas explicitas, el grupo de "
    "trabajo puntual con regla de disolucion y ordenar por gravedad. Desde ese momento "
    "este puesto, emitido contra accion_correctiva_6, RESUELVE al par "
    "accion_correctiva_crosby contra accion_correctiva_sistematica, que es exactamente "
    "el par del puesto 2805, que es D, y cae ademas junto al puesto 2496, tambien D, que "
    "es el mismo par por el otro absorbido. TRES VEREDICTOS, UN PAR RESUELTO, DOS "
    "CLASES: colision de clase, medida con resolutor propio sobre el archivo entero "
    "(docs/loop/SALIDA_V51_CENSO_COLISIONES_LOTE_A.txt). LO QUE LA LECTURA P.12 MIDE CON "
    "LOS DOS TEXTOS VIVOS DELANTE, y es lo que decide: el A de este puesto era verdad de "
    "accion_correctiva_6, un nodo de CUATRO pasos y DOS condiciones del que su propio "
    "veredicto dice, con estas palabras, que NO LE QUEDA NI UNA LINEA PROPIA frente a "
    "accion_correctiva_crosby. El nodo vivo de hoy tiene NUEVE pasos y CINCO condiciones "
    "y trae el aparato de seguimiento entero: la ficha por problema con que paso, que tan "
    "grave es, por que paso, quien se encarga y para cuando; la escalada de la revision "
    "diaria a la semanal y de ahi a una mensual que decide si amerita esfuerzo dedicado; "
    "el grupo de trabajo puntual con responsable claro y regla de disolucion; ordenar por "
    "gravedad; la escalada a un NIVEL DE DECISION SUPERIOR para que los problemas no se "
    "acepten como normales; y verificar que la accion implementada haya ELIMINADO el "
    "problema. Contra ESE nodo, accion_correctiva_crosby no repite: lo suyo es UN CANAL "
    "DE DETECCION que el otro da por dado, investigar las causas raiz CONSULTANDO "
    "DIRECTAMENTE AL PERSONAL OPERATIVO, AUDITORIAS INDEPENDIENTES PERIODICAS POR "
    "DEPARTAMENTO, documentar en REPORTES FORMALES DE INGENIERIA DE CALIDAD y planes de "
    "accion POR DEPARTAMENTO RESPONSABLE. Eso no es un paso del procedimiento del otro: "
    "es de donde salen los problemas. P.12 lo llama CONTINUA: enlace mas poda del "
    "solape, no fusion. D. Y EL ARCHIVO YA CORTABA POR ESTA MISMA LINEA ANTES DE LA "
    "FUSION, que es lo que vuelve la correccion previsible y no oportunista: el puesto "
    "2496, accion_correctiva_5 contra accion_correctiva_crosby, ya era D, sano, ARISTA "
    "QUE FALTA, y el 2805 lo repite con su relectura conjunta escrita."))

CAB[820] = ("D", (
    "CORRECCION DECLARADA EL 20 ago 2026 (vuelta 51), Y LA COLISION QUE LA OBLIGA LA "
    "FABRICO ESTA MISMA VUELTA: SE DICE ASI EN VEZ DE PRESENTARLA COMO HALLAZGO. LA "
    "CLASE CAMBIA: DE A A D. QUE PASO, en orden. La fusion de la PARTE A del acto 4 de "
    "OP-U-01 sobre la nomina de la apertura de esta vuelta (la familia del SCORECARD, "
    "RACIMO EN ESTRELLA del banco 9.23 que el propio puesto 1201 declara cerrada) "
    "depreco scoring_model_scorecard, el CENTRO de la estrella, con alias a "
    "scorecard_de_seleccion_de_proyectos, que es el superviviente elegido por CONTENIDO "
    "sin empate en ninguna vara: tres condiciones contra dos, resumen de 424 caracteres "
    "contra 373 y cableado de 8 contra 6, y ademas es el que deja VIVA la puerta del "
    "acto, scorecards_criterios_gate, que es semilla o extremo de puente aprobado "
    "(docs/loop/SALIDA_V51_PUERTAS_APERTURA.txt). Desde ese momento este puesto, emitido "
    "contra scoring_model_scorecard, RESUELVE al par scorecard_de_seleccion_de_proyectos "
    "contra scorecards_criterios_gate, que es exactamente el par del puesto 1201, que es "
    "D. DOS VEREDICTOS, UN PAR RESUELTO, DOS CLASES: colision de clase, medida con "
    "resolutor propio sobre el archivo entero "
    "(docs/loop/SALIDA_V51_CENSO_COLISIONES_LOTE_A.txt). LO QUE LA LECTURA P.12 MIDE CON "
    "LOS DOS TEXTOS VIVOS DELANTE: el A de este puesto era verdad de "
    "scoring_model_scorecard, el nodo mas GENERICO de los tres, el que dice como se "
    "construye y se usa un puntaje sin decir en que momento del proceso. El nodo vivo de "
    "hoy tiene SEIS pasos y SEIS condiciones y es explicitamente el instrumento de "
    "ORDENAR LA CARTERA: define los seis criterios, decide como puntuar, evalua cada "
    "proyecto activo, COMPARA LOS PUNTAJES ENTRE PROYECTOS para decidir donde invertir "
    "primero, revisa la lista con lo aprendido, y usa un scorecard distinto segun el tipo "
    "de proyecto. Contra ESE nodo, scorecards_criterios_gate no repite: lo suyo es UN "
    "RITUAL DE PUERTA entero, aplicar la tabla en las puertas tempranas 1, 2 y 3, pedir "
    "la AUTOEVALUACION DEL EQUIPO ANTES DE LA REUNION para evitar el sesgo del que "
    "presenta, COMPARAR LAS PUNTUACIONES DEL EQUIPO CONTRA LAS DE QUIENES DECIDEN y "
    "discutir las diferencias en la mesa, e integrar valor presente neto, valor comercial "
    "esperado y plazo de recuperacion. Uno compara PROYECTOS ENTRE SI; el otro enfrenta "
    "DOS LECTURAS DEL MISMO PROYECTO. P.12 lo llama CONTINUA: enlace mas poda del solape, "
    "no fusion. D. Y ES LA MISMA LECTURA QUE EL PROPIO 1201 YA HABIA ESCRITO POR EL OTRO "
    "LADO, con estas palabras: EL INSTRUMENTO ES EL MISMO Y EL MOMENTO Y EL RITUAL NO SE "
    "TOCAN. Lo que la fusion cambia no es la lectura del par: es que ahora hay un solo "
    "par resuelto donde habia dos, y las dos clases no caben."))


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
        if u"—" in nueva or u"–" in nueva:
            print("ROJO: guion largo o medio en la razon nueva del %d." % n)
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
    print("guiones largos y medios en las razones nuevas: CERO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
