# -*- coding: utf-8 -*-
"""vuelta49_relectura_colisiones.py . CONSTRUYE EL LOTE DE LAS SEIS CORRECCIONES
DE LA RELECTURA CONJUNTA DE LAS TRES COLISIONES DE CLASE PREEXISTENTES.

POR QUE EXISTE, y no se teclea el lote a mano: la razon vieja tiene que quedar
ENTERA dentro de la razon nueva (docs/BANCO_DE_TEXTOS.md 9.10 y la regla de la
casa, una correccion que tapa lo que corrige no se puede auditar), y transcribir
a mano un parrafo de cuatro mil caracteres es exactamente donde nace una errata.
Este instrumento LEE la razon vieja del archivo y la pega por maquina, con la
misma formula que uso el precedente del par 233 (docs/plan/02_DESTEJIDOS.md
linea 3372, leida hoy): "LO QUE DECIA LA RAZON VIEJA, y se deja escrita ENTERA
para que la correccion se pueda auditar (copiada del archivo por maquina, no
transcrita): ... FIN DE LA RAZON VIEJA."

LO QUE ESTE INSTRUMENTO NO HACE: no decide. La cabecera de cada correccion va
escrita aqui, es la lectura del ejecutor de la vuelta 49, y se lee y se discute
como tal. Lo unico automatico es el pegado del texto viejo y su guarda.

GUARDA: tras construir, comprueba que la razon vieja aparece LITERAL dentro de
la nueva en las seis. Si falta una sola, aborta sin escribir el lote.

De solo lectura sobre el archivo de veredictos: escribe el LOTE, no el archivo.
El archivo lo escribe scripts/corregir_veredicto.py, que es el carril adjudicado
por el auditor (precedente del par 233).

Uso: python scripts/loop/vuelta49_relectura_colisiones.py --salida docs/loop/_lote_v49_colisiones.jsonl
"""
import argparse
import io
import json
import sys

VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"

# LAS SEIS CABECERAS. Cada una es la lectura del ejecutor de la vuelta 49, con
# las varas citadas y la medicion de hoy al lado.
CAB = {}

CAB[806] = ("D", """CORRECCION DECLARADA EL 19 ago 2026 (vuelta 49), POR RELECTURA CONJUNTA DEL PAR RESUELTO, ENCARGADA POR EL AUDITOR EN EL ACTA DE LA VUELTA 48 (TAREA 1.3). LA CLASE CAMBIA: DE B A D. EL PAR RESUELTO ES customer_development_modelo CONTRA voz_del_cliente_voc, y este puesto lo cargaba con B mientras el puesto 1261 lo cargaba con D: DOS CLASES PUBLICADAS SOBRE EL MISMO PAR. Medido hoy con el resolutor (P.1): este puesto se emitio contra enfoque_mercado_voc, que HOY ESTA DEPRECADO y cuya cadena de alias, leida de los ficheros, es enfoque_mercado_voc a voz_del_cliente_voc. EL MOTIVO DE LA CORRECCION ES EL QUE LA PROPIA RAZON VIEJA ESCRIBIO, Y SE CUMPLIO: la razon vieja dice con estas palabras que Queda B porque la familia de la voz del cliente ya lleva CINCO nodos vistos y uno de ellos, voz_del_cliente_voc, es costura confirmada que bloquea dos pares, y que no se puede decidir de a pares mientras el nodo grande de la familia siga sin operar. ESE B ERA UN B DE ESPERA Y LA ESPERA TERMINO: voz_del_cliente_voc esta operado (OP-F-04-COL) y hoy carga a enfoque_mercado_voc como alias, medido en el fichero. O sea que el B no envejecio por error de lectura sino porque se cumplio su propia condicion, y eso es lo que dice esta correccion. LO QUE LA RELECTURA MIDE CON LOS DOS TEXTOS VIVOS DELANTE, y confirma la D del 1261: customer_development_modelo despacha en UNA LINEA, su paso 2, Sal a hablar directamente con clientes potenciales, no te quedes esperando; voz_del_cliente_voc convierte esa linea en PROCEDIMIENTO y le anade la dimension que falta, observar en el entorno propio del cliente y no solo preguntar, acompanarlo donde usa el producto, complementar las entrevistas con observacion real, usar lo observado desde el inicio para disenar, y mantener contacto en ciclos cortos durante todo el desarrollo. Y LA FUSION AGRANDO LA SEPARACION EN VEZ DE ACERCARLOS, que es lo que decide: el paso 4 de hoy trae ademas la evaluacion preliminar de mercado y el analisis competitivo detallado de productos, precios y tecnologias, que es material que customer_development_modelo NO TIENE. La vara del banco 9.22 devuelve PROCEDIMIENTO EN UN SOLO SENTIDO, que es el caso corriente y no la figura: ahi hay madre e hijo, la vara del 9.6.1 se aplica UNA VEZ en la direccion que manda el 9.6.2 (que anade el hijo a la madre, nunca al reves) y el par CONTINUA. D. ARISTA, BUSCADA HOY EN LOS DOS SENTIDOS Y RESUELTA POR ALIAS: NO HAY NINGUNA, ni de customer_development_modelo a voz_del_cliente_voc ni al reves. QUEDA DECLARADA COMO ARISTA QUE FALTA PARA LA FASE 04, por el precedente de los pares 599 y 233 (docs/plan/02_DESTEJIDOS.md linea 3521, leida hoy): la relacion es de alimentacion y no de gemelos, y una alimentacion pide arista. LIMITE DE LA REGLA FAMILIA DECLARADA, verificado hoy contra docs/RACIMOS_MIEMBROS.jsonl con los ids resueltos: solo customer_development_modelo esta en la nomina del racimo Customer discovery salir a hablar con el cliente, y voz_del_cliente_voc no esta en ninguno, asi que la regla no aplica y el par se pelea normal. Libros distintos, Blank contra Cooper, medido hoy en el campo fuente.""")

CAB[1261] = ("D", """CORRECCION DECLARADA EL 19 ago 2026 (vuelta 49), POR RELECTURA CONJUNTA DEL PAR RESUELTO. LA CLASE NO CAMBIA: SIGUE D, Y ES LA QUE GANA LA COLISION. El puesto 806 cargaba B sobre este mismo par resuelto y queda corregido a D en la misma corrida; la colision de clase se resuelve a favor de esta lectura. LO QUE SI SE CORRIGE ES LA DESCRIPCION, Y ES UNA ENUMERACION QUE SE QUEDO CORTA: la razon vieja enumera el contenido de voz_del_cliente_voc SIN los dos pasos que llegaron despues con OP-F-04-COL al absorber enfoque_mercado_voc. Medido hoy en el fichero, el paso 4 del nodo vivo dice Haz una evaluacion preliminar de mercado y un analisis competitivo detallado de productos, precios y tecnologias antes de comprometer recursos importantes, y el paso 5 anade probar las primeras ideas de concepto con clientes reales antes del desarrollo formal. NINGUNA DE LAS DOS ESTABA EN LA ENUMERACION VIEJA. EL VEREDICTO NO SE MUEVE, Y SE DICE POR QUE: las dos piezas nuevas son material que customer_development_modelo NO TIENE, asi que agrandan la separacion en vez de acercarlos, y la propia razon vieja dejo escrita la vara que lo cubre, Este par es D y es invariante, quitar material no puede crear repeticion; anadir material que el otro no tiene tampoco. ARISTA, RE-BUSCADA HOY EN LOS DOS SENTIDOS Y RESUELTA POR ALIAS: SIGUE SIN HABER NINGUNA, y queda declarada como ARISTA QUE FALTA para la fase 04 por el precedente de los pares 599 y 233 (docs/plan/02_DESTEJIDOS.md linea 3521, leida hoy).""")

CAB[844] = ("D", """CORRECCION DECLARADA EL 19 ago 2026 (vuelta 49), POR RELECTURA CONJUNTA DEL PAR RESUELTO, ENCARGADA POR EL AUDITOR EN EL ACTA DE LA VUELTA 48 (TAREA 1.3). LA CLASE CAMBIA: DE A A D. EL PAR RESUELTO ES pensamiento_convergente_divergente CONTRA reglas_brainstorming, y este puesto lo cargaba con A mientras el puesto 585 lo cargaba con D: DOS CLASES PUBLICADAS SOBRE EL MISMO PAR. Medido hoy con el resolutor (P.1), LOS DOS NODOS DE ESTE PUESTO ESTAN DEPRECADOS y sus cadenas de alias, leidas de los ficheros, son brainstorming_divergente a reglas_brainstorming y generar_multiples_opciones a pensamiento_convergente_divergente. EL MOTIVO DE LA CORRECCION ES QUE LA VARA QUE PRODUJO LA A NO SOBREVIVE AL PAR RESUELTO, Y ES LA PROPIA RAZON VIEJA LA QUE LO DEJA COMPROBABLE: aquella A salio del segundo polo del banco 9.22, LINEA EN LOS DOS SENTIDOS, con estas palabras, lo que generar_multiples_opciones anade es el plazo, UNA LINEA; lo que brainstorming_divergente anade son la sala, la regla y el post-it, y los tres son LINEA. ESO ERA VERDAD DE AQUELLOS DOS NODOS PEQUENOS, DE TRES Y CUATRO PASOS, Y ES FALSO DE LOS DOS SUPERVIVIENTES, medido hoy paso a paso: los dos tienen SIETE pasos y lo que cada uno anade al otro YA NO ES LINEA SINO PROCEDIMIENTO, por la regla practica del informe 67.6 (es LINEA un puntero, una advertencia, un criterio suelto o una accion unica; es PROCEDIMIENTO un paso que obliga a varias decisiones dentro de si o que se repite en el tiempo). LO QUE ANADE reglas_brainstorming: el protocolo entero de la sesion, reunir en un espacio dedicado formando grupos con confianza mutua, definir un enunciado del problema centrado en la necesidad del cliente, establecer visibilizar y HACER CUMPLIR siete reglas, preparar al equipo con una inmersion previa de visita de campo o entrevistas, los post-its, y el calentamiento Silly Cow. LO QUE ANADE pensamiento_convergente_divergente: la disciplina de alternar, la metafora del embudo, alternar a conciencia y DE FORMA NO LINEAL entre investigacion de mercado, prototipado y generacion, matar a los hijos favoritos, y aceptar la ambiguedad. Ninguna de las dos listas cabe en una linea. NO ES LINEA EN LOS DOS SENTIDOS, ASI QUE NO ES A. Y LO QUE QUEDA ES EXACTAMENTE EL CORTE QUE EL PUESTO 585 ESCRIBIO Y VOLVIO A VERIFICAR POR P.5 EL 19 ago 2026: LA SESION CONTRA LA DISCIPLINA MENTAL, Y SON NIVELES DISTINTOS, un corte que las dos fusiones no debilitan sino que refuerzan, porque reglas_brainstorming absorbio ademas brainstorming_efectivo (mas sesion) y pensamiento_convergente_divergente absorbio ademas design_attitude_vs_decision_attitude (mas disciplina). D. UN DISCUTIBLE QUE SE MARCA EN VEZ DE ESCONDERSE, y va al reporte de la vuelta para que el auditor lo adjudique: se considero el PRIMER polo del 9.22, PROCEDIMIENTO EN LOS DOS SENTIDOS, clase C sano con figura, porque cada nodo expande con un procedimiento algo que el otro enuncia. SE DESCARTO POR LA COMPROBACION QUE EL PROPIO 9.22 PONE PARA SEPARARLO, si las dos direcciones apuntan a la MISMA linea no es la figura: las dos candidatas, el paso 7 de reglas_brainstorming y el paso 1 de pensamiento_convergente_divergente, son la MISMA linea, la fase de divergencia separada de la de seleccion, y la figura exige DOS lineas distintas. ARISTA: Y AQUI HAY UN CAMBIO CONTRA LO QUE EL 585 PUBLICO, DECLARADO EN VEZ DE CALLADO. El 585 escribio SIN ARISTA entre ellos, buscada hoy en los dos sentidos y resuelta por alias. HOY, con los ids resueltos, HAY ARISTA EN LOS DOS SENTIDOS: pensamiento_convergente_divergente tiene a reglas_brainstorming en sus siguientes y reglas_brainstorming lo tiene en sus previos. La arista no la puso nadie a mano: la heredaron los supervivientes al fundir. Que la haya NO mueve la clase, porque un par sano puede estar cableado y de hecho es lo deseable; lo que cambia es que este D NO DEJA ARISTA QUE FALTA, a diferencia de los pares 599 y 233. LIMITE DE LA REGLA FAMILIA DECLARADA, re-verificado hoy contra docs/RACIMOS_MIEMBROS.jsonl con los ids resueltos: solo reglas_brainstorming esta en la nomina del racimo Las reglas del brainstorming, y pensamiento_convergente_divergente no esta en ninguno, asi que la regla no aplica y el par se pelea normal. EL DEFECTO DE CAMPO DE LA FUENTE QUE LAS DOS RAZONES VIEJAS DENUNCIABAN, RE-MEDIDO HOY, YA NO EXISTE EN ESTE PAR y se dice: las dos grafias de Change by Design vivian en brainstorming_divergente y en generar_multiples_opciones, los dos hoy deprecados; los dos nodos vivos dicen Change by Design y Business Model Generation (Osterwalder), o sea LIBROS DISTINTOS DE VERDAD.""")

CAB[585] = ("D", """CORRECCION DECLARADA EL 19 ago 2026 (vuelta 49), POR RELECTURA CONJUNTA DEL PAR RESUELTO. LA CLASE NO CAMBIA: SIGUE D, Y ES LA QUE GANA LA COLISION. El puesto 844 cargaba A sobre este mismo par resuelto y queda corregido a D en la misma corrida; la colision se resuelve a favor de esta lectura, porque el corte que este puesto escribio, LA SESION CONTRA LA DISCIPLINA MENTAL Y SON NIVELES DISTINTOS, es el unico de los dos que sobrevive a las dos fusiones. LO QUE SI SE CORRIGE, Y ES UN HECHO PUBLICADO QUE HOY ES FALSO: esta razon dice SIN ARISTA entre ellos, buscada hoy en los dos sentidos y resuelta por alias. RE-MEDIDO HOY CON EL RESOLUTOR (P.1): HAY ARISTA EN LOS DOS SENTIDOS entre los ids vivos, pensamiento_convergente_divergente tiene a reglas_brainstorming en sus siguientes y reglas_brainstorming lo tiene en sus previos. Nadie la puso a mano: la heredaron los supervivientes al fundir, porque este puesto se emitio contra brainstorming_divergente, que hoy esta deprecado con alias a reglas_brainstorming. QUE HAYA ARISTA NO MUEVE LA CLASE, un par sano puede estar cableado y es lo deseable; lo que cambia es que este D NO DEJA ARISTA QUE FALTA para la fase 04, a diferencia de los pares 599 y 233. Y LA SEGUNDA COSA QUE SE CORRIGE ES EL NOMBRE Y EL TAMANO DEL LADO DE LA SESION: donde esta razon dice brainstorming_divergente con cuatro pasos, hoy hay reglas_brainstorming con SIETE, que ademas de la sala, las reglas, el generar sin filtrar y los post-its trae el enunciado del problema centrado en la necesidad del cliente, la inmersion previa y el Silly Cow. El corte no se debilita: se ensancha.""")

CAB[263] = ("D", """CORRECCION DECLARADA EL 19 ago 2026 (vuelta 49), POR RELECTURA CONJUNTA DEL PAR RESUELTO, ENCARGADA POR EL AUDITOR EN EL ACTA DE LA VUELTA 48 (TAREA 1.3). LA CLASE CAMBIA: DE B A D. EL PAR RESUELTO ES riesgo_titulos_inflados CONTRA seleccion_ceo_fundador, y este puesto lo cargaba con B mientras el puesto 1589 lo cargaba con D: DOS CLASES PUBLICADAS SOBRE EL MISMO PAR. Medido hoy con el resolutor (P.1): este puesto se emitio contra errores_comunes_asignacion_roles, que HOY ESTA DEPRECADO y cuya cadena de alias, leida del fichero, es errores_comunes_asignacion_roles a seleccion_ceo_fundador. LA SILUETA QUE ESTA RAZON DESCRIBE ES LA DE LA MADRE QUE RESUME Y EL HIJO QUE DESARROLLA, y esta razon la marco B por lo que el informe del cribado dice con estas palabras de esa silueta, hasta ahora se venia marcando B por no saber como leerla (docs/INTRA_DOMINIO_INFORME.md, la seccion de la regla de lectura, leida hoy). LA REGLA YA EXISTE Y ES LA QUE DECIDE: arista madre a hijo mas paso-resumen en la madre igual a JERARQUIA SANA; sin arista igual a DUPLICACION; madre que RE-DESARROLLA igual a DUPLICACION aunque haya arista. APLICADA AL PAR RESUELTO, CON LAS TRES COSAS MEDIDAS HOY. Primera, LA ARISTA: HAY, Y EN LOS DOS SENTIDOS, seleccion_ceo_fundador tiene a riesgo_titulos_inflados en sus siguientes y riesgo_titulos_inflados lo tiene en sus previos, resuelto por alias. Y ES UN CAMBIO CONTRA EL ESTADO EN QUE ESTA RAZON SE EMITIO, declarado en vez de callado: errores_comunes_asignacion_roles, el nodo contra el que se leyo, NO TENIA NI UNA ARISTA a riesgo_titulos_inflados en ninguno de los dos sentidos, medido hoy en su fichero, que sigue intacto. Segunda, EL PASO-RESUMEN: la madre resume, NO re-desarrolla. Su paso 4 dice y se cauteloso al asignar titulos C-level tempranamente, considerando el crecimiento futuro, que es UNA CLAUSULA dentro de un paso que trata de otra cosa, los roles alternativos para la persona de la idea. Tercera, LO QUE EL HIJO DESARROLLA Y LA MADRE NO DICE: titulos flexibles o provisionales mientras se empieza, y dejar claro entre los socios que los roles se van a revisar a medida que el negocio crezca, mas su entregable propio, una lista de titulos con clausula de revision futura. LA FUSION NO CREO LA DUPLICACION: LA CURO. Movio la linea-resumen del hijo a una madre que SI esta cableada con el, que es exactamente lo que la regla llama jerarquia sana. D. Los dos del mismo libro, The Founder's Dilemmas, medido hoy en el campo fuente. Ninguno de los dos esta en racimo declarado, verificado hoy contra docs/RACIMOS_MIEMBROS.jsonl con los ids resueltos, asi que la regla familia declarada no aplica.""")

CAB[1589] = ("D", """CORRECCION DECLARADA EL 19 ago 2026 (vuelta 49), POR RELECTURA CONJUNTA DEL PAR RESUELTO. LA CLASE NO CAMBIA: SIGUE D, Y ES LA QUE GANA LA COLISION. El puesto 263 cargaba B sobre este mismo par resuelto y queda corregido a D en la misma corrida. PERO EL MOTIVO DE ESTA D MURIO Y HAY QUE DECIRLO, PORQUE ES EL CASO MAS CLARO DE RAZON ENVEJECIDA DE LOS TRES: esta razon sostiene el D sobre una PRECISION DE NOMINA que la fusion se llevo por delante. Decia con estas palabras que la advertencia de ser cauteloso al asignar titulos de alto nivel temprano SI EXISTE en el catalogo, pero esta en errores_comunes_asignacion_roles, que es OTRO miembro del acto 4, y no en este nodo, y remataba, Este par se lee contra el miembro equivocado de esa familia y por eso sale sano. HOY ESO ES FALSO, MEDIDO EN EL FICHERO: errores_comunes_asignacion_roles esta DEPRECADO con alias a seleccion_ceo_fundador, y su paso 3 vive dentro del paso 4 del nodo vivo, que dice y se cauteloso al asignar titulos C-level tempranamente, considerando el crecimiento futuro. O sea que el par YA NO se lee contra el miembro equivocado: la advertencia ESTA en el nodo, y la clausula de escape que sostenia esta razon se la comio la propia fusion. TAMBIEN ES FALSO, POR LO MISMO, EL Ni un paso se solapa. EL VEREDICTO SE SOSTIENE IGUAL, PERO POR OTRA REGLA, Y ESA ES LA CORRECCION: la del informe del cribado para la silueta de la madre que resume y el hijo que desarrolla, arista madre a hijo mas paso-resumen en la madre igual a JERARQUIA SANA. Las tres cosas, medidas hoy. ARISTA: hay, y en los dos sentidos, resuelta por alias. PASO-RESUMEN: la madre RESUME y no re-desarrolla, porque lo unico que dice del asunto es una clausula dentro de un paso que trata de los roles alternativos. LO QUE EL HIJO ANADE Y LA MADRE NO DICE: los titulos flexibles o provisionales, la revision pactada de los roles entre socios, y su entregable propio con clausula de revision futura. La jerarquia no se rompe por arriba. D. Y SE DICE LO QUE INCOMODA: por la vara del 9.6.2, lo que el hijo anade a la madre son DOS LINEAS y no un procedimiento, que es la firma de REPITE y no la de CONTINUA. Lo que salva el D no es el tamano de lo que anade sino la regla de la silueta, que decide por la arista y por el paso-resumen y no por el conteo. QUEDA MARCADO COMO DISCUTIBLE EN EL REPORTE DE LA VUELTA para que el auditor lo adjudique.""")

VIEJA_ABRE = (" LO QUE DECIA LA RAZON VIEJA, y se deja escrita ENTERA para que la "
              "correccion se pueda auditar (copiada del archivo por maquina, no "
              "transcrita): ")
VIEJA_CIERRA = " FIN DE LA RAZON VIEJA."


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    idx = {r["puesto_intra"]: r for r in V}

    lote, fallos = [], []
    print("=" * 78)
    print("LOTE DE LAS SEIS CORRECCIONES, con la razon vieja pegada POR MAQUINA")
    print("=" * 78)
    for p in sorted(CAB):
        if p not in idx:
            fallos.append("el puesto %d no esta registrado" % p)
            continue
        vieja = idx[p]["razon"]
        clase_nueva, cab = CAB[p]
        nueva = cab.strip() + VIEJA_ABRE + vieja + VIEJA_CIERRA
        if vieja not in nueva:
            fallos.append("la razon vieja del %d NO quedo dentro de la nueva" % p)
        lote.append({"puesto": p, "clase": clase_nueva, "razon": nueva})
        print("  puesto %-5d %s -> %s | %-36s contra %s"
              % (p, idx[p]["clase"], clase_nueva, idx[p]["nodo_a"], idx[p]["nodo_b"]))
        print("      razon vieja %6d caracteres | razon nueva %6d | vieja DENTRO: %s"
              % (len(vieja), len(nueva), vieja in nueva))

    cambian = sum(1 for x in lote if idx[x["puesto"]]["clase"] != x["clase"])
    print()
    print("cambian de clase: %d de %d" % (cambian, len(lote)))
    if fallos:
        print()
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1
    io.open(a.salida, "w", encoding="utf-8", newline="\n").write(
        "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in lote))
    print("lote escrito: %s (%d lineas)" % (a.salida, len(lote)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
