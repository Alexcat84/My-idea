# -*- coding: utf-8 -*-
"""vuelta52_colision_fabricada.py . CONSTRUYE EL LOTE DE LAS CORRECCIONES `P.16`
DE LAS COLISIONES QUE EL LOTE A DE LA VUELTA 52 FABRICA.

SUCESOR DECLARADO de scripts/loop/vuelta51_colision_fabricada.py, del que hereda
el contrato entero: la razon vieja tiene que quedar ENTERA dentro de la razon
nueva (banco 9.10 y la regla de la casa, una correccion que tapa lo que corrige
no se puede auditar), y se PEGA POR MAQUINA leyendola del archivo, porque
transcribir a mano un parrafo de miles de caracteres es donde nace una errata.

LA NOVEDAD DE ESTE LOTE, y es la que el acta de la vuelta 51 adjudico en su
pregunta 2: HAY DOS CARRILES Y NO UNO.

  CARRIL DEL A ARRASTRADO (el de siempre): el veredicto arrastrado es `A`, se
  voltea a la clase del veredicto DIRECTO del par resuelto, citandolo como
  relectura conjunta. Es el puesto 502 de este lote.

  CARRIL DEL FILO (nuevo): el veredicto arrastrado es `B` o `C`. NO se voltea
  por maquina. Su nodo muere o cambia de texto, asi que es la COLA DE RELECTURA
  POST FUSION de docs/plan/08_VERIFICACION.md, que admite exactamente `B` y `C`
  y por el motivo escrito alli: lo que se mueve es lo que estaba en el filo. Se
  RELEE el par resuelto EN EL MISMO ACTO con el veredicto directo como
  contraste, y la correccion cita ESA relectura, no la maquina. Son los puestos
  266 (`B`) y 246 (`C`) de este lote. Las dos relecturas estan escritas ANTES de
  sellar en docs/loop/PLAN_V52_OPU01_LOTE_A.json, campo relecturas_del_filo, y
  las dos salieron CONDICION DE TEXTO: si alguna hubiera salido PREGUNTA DE
  POLITICA de catalogo, el acto NO se habria fundido y se habria declarado para
  la mesa.

De solo lectura sobre el archivo de veredictos: escribe el LOTE, no el archivo.
El archivo lo escribe scripts/corregir_veredicto.py, que es el carril adjudicado.

Uso: python scripts/loop/vuelta52_colision_fabricada.py --salida docs/loop/_lote_v52_lote_a.jsonl
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

QUE_PASO = (
    "CORRECCION DECLARADA EL 20 ago 2026 (vuelta 52), Y LA COLISION QUE LA OBLIGA LA "
    "FABRICO ESTA MISMA VUELTA: SE DICE ASI EN VEZ DE PRESENTARLA COMO HALLAZGO. QUE "
    "PASO, en orden. La fusion de la PARTE A del acto 2 de OP-U-01 sobre la nomina de la "
    "apertura de esta vuelta (la familia del REPARTO DE EQUITY, adjudicada para "
    "ejecutarse por el acta de la vuelta 51, pregunta 2) depreco split_igual_vs_desigual "
    "con alias a criterios_equity_split, que es el superviviente elegido por CONTENIDO "
    "con el margen mas ancho del tramo y sin empate en ninguna vara: OCHO pasos contra "
    "cuatro, TRES condiciones contra dos, 1.134 caracteres de resumen contra 586 y "
    "cableado de 20 contra 4 (docs/loop/SALIDA_V52_DOSSIER_01_26.txt, acto 2). Ninguno "
    "de los tres miembros del acto es puerta, asi que la guarda 1B paso POR VACIO "
    "(docs/loop/SALIDA_V52_PUERTAS_REPARADO.txt). Las TRES colisiones que la fusion "
    "fabrica estaban PREDICHAS ANTES DE TOCAR UN NODO por "
    "scripts/loop/vuelta51_colisiones_esperadas.py sobre el archivo entero "
    "(docs/loop/SALIDA_V52_COLISIONES_ESPERADAS.txt), y el censo real tras ejecutar "
    "devolvio EXACTAMENTE ESAS TRES, ni una mas "
    "(docs/loop/SALIDA_V52_CENSO_COLISIONES_LOTE_A.txt). ")

FIN = (
    " P.16, QUIEN FABRICA LIMPIA, en el mismo acto y sin aplazar. El marcador queda "
    "recomputado en la misma vuelta y el barrido 9.10 corrido sobre toda tabla vigente "
    "que cite la clase, el marcador o el retrato, despues del ultimo movimiento de la "
    "vuelta.")

CAB = {}

# ---------------------------------------------------------------- CARRIL DEL A
CAB[502] = ("D", (
    QUE_PASO +
    "LA CLASE CAMBIA: DE A A D, POR EL CARRIL DEL A ARRASTRADO, que es el que el acta de "
    "la vuelta 49 adjudico en su pregunta 1 y las vueltas 50 y 51 usaron igual. Este "
    "puesto, emitido contra split_igual_vs_desigual, RESUELVE desde la fusion al par "
    "criterios_equity_split contra teoria_equidad_split_equity, que es exactamente el par "
    "del puesto 871, que es D. DOS VEREDICTOS, UN PAR RESUELTO, DOS CLASES: colision de "
    "clase. LA LECTURA P.12 ES LA RELECTURA CONJUNTA DE ESTE A, porque este A se emitio "
    "contra un nodo que hoy no existe solo, y se hizo con los textos vivos delante. LO "
    "QUE MIDE: el A de este puesto era verdad de split_igual_vs_desigual, un nodo de "
    "CUATRO pasos y UNA condicion que el propio puesto 188 llama LA VERSION CORTA del "
    "largo. El nodo vivo de hoy tiene NUEVE pasos y TRES condiciones y es el checklist "
    "entero de COMO se reparte: listar las contribuciones pasadas de cada fundador, "
    "documentar el capital exacto que aporta cada uno, calcular el costo de oportunidad, "
    "estimar las contribuciones futuras segun experiencia y dedicacion, considerar la "
    "prima de idea de diez a quince puntos, discutir motivaciones y tolerancia al "
    "conflicto, ajustar proporcionalmente por dedicacion, registrar por escrito la logica, "
    "y no cerrar el acuerdo con un apreton de manos rapido. Contra ESE nodo, "
    "teoria_equidad_split_equity no repite: lo suyo es LA PREGUNTA PREVIA, decidir si el "
    "equipo opera bajo logica social o de negocio segun sus relaciones previas, aceptar el "
    "reparto igualitario con su coste si es social, disenar el proporcional si es de "
    "negocio, y evaluar el riesgo de la asimetria entre contribucion real y equity si se "
    "elige la logica equivocada. El checklist SUPONE YA ELEGIDA la logica de negocio; el "
    "otro es el que la elige. P.12 lo llama CONTINUA: enlace mas poda del solape, no "
    "fusion. D. Y ES LA MISMA LECTURA QUE EL PROPIO 871 YA HABIA ESCRITO POR EL OTRO LADO, "
    "con estas palabras: EL SEGUNDO ES LA PREGUNTA PREVIA DEL PRIMERO Y NO ESTA CONTENIDO "
    "EN EL. La arista que P.12 manda declarar YA EXISTE en los dos sentidos, asi que aqui "
    "no queda arista que declarar sino solo la poda del solape para la fase 04." + FIN))

# ------------------------------------------------------------- CARRIL DEL FILO
CAB[266] = ("D", (
    QUE_PASO +
    "LA CLASE CAMBIA: DE B A D, Y NO POR MAQUINA. Este puesto es del FILO y va por el "
    "CARRIL DEL FILO que el acta de la vuelta 51 adjudico en su pregunta 2: un B cuyo "
    "nodo muere entra en LA COLA DE RELECTURA POST FUSION de docs/plan/08_VERIFICACION.md, "
    "que admite exactamente B y C, y se RELEE EN EL MISMO ACTO con el veredicto directo "
    "como contraste. Este puesto, emitido contra split_igual_vs_desigual, RESUELVE desde "
    "la fusion al par criterios_equity_split contra reparto_inicial_equity, que es "
    "exactamente el par del puesto 754, que es D. LA RELECTURA, hecha con los dos textos "
    "vivos delante y ANTES de sellar el plan "
    "(docs/loop/PLAN_V52_OPU01_LOTE_A.json, campo relecturas_del_filo): "
    "criterios_equity_split son NUEVE pasos que responden CON QUE SE DECIDE el reparto, y "
    "reparto_inicial_equity son CUATRO pasos que responden CUANDO Y COMO SE CIERRA, "
    "esperar a que la estrategia y el equipo se estabilicen antes de cerrar el reparto "
    "final, usar una plantilla estructurada tipo UpDown para conversarlo, escribir los "
    "acuerdos, y DEJAR SIEMPRE UNA PARTE AJUSTABLE, vesting o clausulas de recompra, nunca "
    "fijo para siempre. Esa ultima linea es doctrina propia del par y NO existe en "
    "criterios_equity_split, verificado paso a paso sobre el fichero. El unico roce real "
    "es dejarlo por escrito, que es lo mismo que el veredicto DIRECTO 754 llama EL UNICO "
    "ROCE y por lo que lo clasifica D. LA DUDA DE ESTE B NACIO CONTRA EL NODO CORTO, cuyos "
    "cuatro pasos el puesto 188 declara dentro de los ocho del largo: contra el texto "
    "completo la distincion CRITERIOS contra PROCESO queda limpia y la duda se cierra. Y "
    "SE DICE LO QUE NO ES, porque de eso dependia que el acto se fundiera: NO ES UNA "
    "PREGUNTA DE POLITICA DE CATALOGO. Este B no pregunta si el catalogo quiere un "
    "procedimiento con dos contextos o dos nodos; nombra una diferencia de contenido, y la "
    "diferencia sobrevive medida. Si hubiera sido politica, el acto NO se habria fundido y "
    "se habria declarado para la mesa. D." + FIN))

CAB[246] = ("D", (
    QUE_PASO +
    "LA CLASE CAMBIA: DE C A D, Y NO POR MAQUINA. Este puesto es del FILO y va por el "
    "CARRIL DEL FILO que el acta de la vuelta 51 adjudico en su pregunta 2, el mismo que "
    "el 266 de este lote. Este puesto, emitido contra split_igual_vs_desigual, RESUELVE "
    "desde la fusion al par criterios_equity_split contra timing_equity_split, que es "
    "exactamente el par del puesto 688, que es D. LA RELECTURA, hecha con los dos textos "
    "vivos delante y ANTES de sellar el plan "
    "(docs/loop/PLAN_V52_OPU01_LOTE_A.json, campo relecturas_del_filo): "
    "timing_equity_split son cuatro pasos que responden CUANDO, hablarlo ahora o esperar a "
    "tener mas informacion sobre las contribuciones reales, fijar un momento claro como "
    "antes de levantar la primera ronda si se espera, pesar el riesgo de perder a un "
    "cofundador valioso por no ofrecerle equity pronto, y evitar dejar la negociacion para "
    "cuando ya exista una valoracion externa porque eleva la tension. "
    "criterios_equity_split responde COMO, con los nueve pasos del checklist. ES LA MISMA "
    "LECTURA QUE ESTE PROPIO PUESTO ESCRIBIO EN SU RAZON VIEJA (como repartir contra "
    "cuando repartirlo, objetos distintos, sano), y el veredicto DIRECTO 688 lo dice con "
    "esas palabras: es la misma lectura que dio el puesto 246. LO QUE HABIA QUE COMPROBAR "
    "ANTES DE VOLTEAR, porque un C no congela solo una clase: la FIGURA que este puesto "
    "registro, el RACIMO NUEVO del reparto de equity, YA ESTA REGISTRADA Y REMEDIDA A SEIS "
    "MIEMBROS, y los dos veredictos directos del racimo (688 y 754) la citan como FAMILIA "
    "DECLARADA. No queda ningun registro pendiente que la fusion se lleve por delante, y "
    "por eso la relectura sale CONDICION DE TEXTO y no PREGUNTA DE POLITICA. D." + FIN))


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
        nueva = cabecera + " " + FORMULA + vieja + " FIN DE LA RAZON VIEJA."
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
    print("carriles: 1 por el CARRIL DEL A (502) y 2 por el CARRIL DEL FILO (266 B, 246 C)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
