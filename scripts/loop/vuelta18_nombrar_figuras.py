# -*- coding: utf-8 -*-
"""VUELTA 18, TAREA 2.B: nombra los ejemplares en el campo `nota` de las figuras
de docs/plan/INVENTARIO.jsonl.

ADITIVO Y SOLO EL CAMPO `nota`. Ninguna otra clave se toca en ninguna entrada, y
ninguna entrada que no sea una de las once nombradas aqui cambia un byte. El
script lo comprueba antes de escribir y aborta si no se cumple.

Las cifras de los textos salen de scripts/loop/vuelta18_figuras.py corrido en
esta vuelta; ninguna se copia de una nota vieja.
"""
import io
import json

RUTA = "docs/plan/INVENTARIO.jsonl"

CRITERIO = (
    "CRITERIO DE EJEMPLAR DE LA VUELTA 18, escrito para que se pueda discutir: un "
    "ejemplar es una instancia DECLARADA POR ESCRITO (en docs/INTRA_DOMINIO_INFORME.md, "
    "en docs/BANCO_DE_TEXTOS.md, en un expediente o en una lectura dirigida), no "
    "cualquier par que calce con la forma. Cada puesto citado aqui esta verificado en "
    "esta vuelta contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl con "
    "scripts/loop/vuelta18_figuras.py: existe, con esa clase y entre esos dos nodos."
)

CABECERA = " EJEMPLARES NOMBRADOS EL 14 ago 2026 (vuelta 18), adicion declarada, nada borrado. "

ADICIONES = {
    "LA VARA EN LOS DOS SENTIDOS (9.22)": (
        "LOS CINCO, y calzan con los dos polos declarados. PRIMER POLO (procedimiento en "
        "los dos sentidos sobre dos lineas distintas: sanos, clase C, ENLACE MUTUO), TRES: "
        "puesto 1077 C, diseno_landing_page contra herramientas_de_activacion_web, el "
        "primero del archivo; puesto 1240 C, diversidad_vs_homogeneidad_equipo contra "
        "prueba_antes_de_comprometerse, y este con el enlace mutuo YA PUESTO en el grafo; y "
        "LD-02, channels_hypothesis_physical contra channels_hypothesis_web_mobile, que su "
        "propia lectura cierra con \"CONTINUA en los dos sentidos, banco 9.22\" y que es "
        "ademas el tercer ejemplar de EL ESQUELETO COMPARTIDO. SEGUNDO POLO (linea en los "
        "dos sentidos: repiten, clase A, FUSION), DOS, los dos de franquicias: puesto 2080 "
        "A, proceso_llamada_inicial_venta contra proceso_primera_llamada, seis pasos de "
        "siete en el mismo orden; y puesto 2105 A, comprender_definicion_legal_franquicia "
        "contra marco_name_system_fee. Y EL CONTRASTE QUE FIJA EL LIMITE, que no es "
        "ejemplar y por eso se nombra aparte: puesto 2091 D, "
        "presupuesto_marketing_leads_franquicia contra presupuesto_publicidad_franquicia, "
        "preguntado tambien en los dos sentidos y devuelve PROCEDIMIENTO por los dos. "
        "MEDIDO EN ESTA VUELTA: los C de todo el archivo son SIETE, y solo 1077 y 1240 son "
        "de esta figura. Los cinco verifican, cero fallos."
    ),
    "ESTRELLA (9.23)": (
        "OCHO NOMBRADAS Y VERIFICADAS con las DOS cuentas que el banco 9.23 exige (radios "
        "con el centro todos A, y al menos un par entre perifericos leido y ninguno A). "
        "(1) pass/fail, centro diseno_experimentos_pass_fail, radios 467, 511 y 639, "
        "perifericos 636 D y 1346 D. (2) scorecard, centro scoring_model_scorecard, radios "
        "184 y 820, periferico 1201 D. (3) los regalos, centro "
        "regalos_estrategicos_sorpresa, radios 251 y 799, periferico 1348 D. (4) la fase de "
        "diseno, centro fase_diseno_prototipado_modelos, radios 507 y 641, periferico 572 "
        "D. (5) el peso dimensional, centro calcular_peso_dimensional_antes_cotizar, radios "
        "1601 y 1602, periferico 1609 D, la primera fuera del nucleo. (6) investigacion de "
        "mercados, centro enfoque_paso_a_paso_investigacion_mercado, radios 1966 y 1967, "
        "periferico 1972 D. (7) el abogado, INVERTIDA porque el centro es el corto, centro "
        "contratar_abogado_especializado_franquicias, radios 2076 y 2090, periferico 2086 "
        "D. (8) los costos de franquicia, clasica, centro cinco_categorias_costos_franquicia, "
        "radios 2074 y 2075, periferico 2092 D. LAS OCHO VERIFICAN, CERO FALLOS. "
        "DISCREPANCIA DECLARADA Y NO ARREGLADA: el campo cobertura dice NUEVE y la lectura "
        "de esta vuelta solo pudo localizar OCHO declaradas por escrito; la novena no se "
        "encontro y la cifra del campo NO se toca. El candidato mas probable es "
        "tecnologias_disruptivas_oportunidad (dos A, puestos 505 y 513), y NO se cuenta "
        "como ejemplar a proposito: su par entre perifericos NUNCA ENTRO A LA COLA, o sea "
        "que le falta la segunda cuenta, y el propio 9.23 dice que sin ella no se puede "
        "llamar estrella. SEGUNDA MEDICION, para que la cifra se lea bien: la misma forma "
        "contada A MAQUINA sobre las 3.388 lineas da 33 centros que calzan con las dos "
        "cuentas. Los 33 no son ejemplares: son candidatos. La diferencia entre 8 y 33 es "
        "de definicion, no de medicion."
    ),
    "TRIANGULO ABIERTO": (
        "LOS DOS, verificados par por par. (1) LOS MERCADOS DE VARIOS LADOS: "
        "mercados_multilaterales, multi_sided_market_channel y "
        "optimizacion_mercado_multilado, sus tres pares leidos y los tres D, puestos 1497, "
        "1509 y 1558. El informe lo declaro asi al cerrarlo: un mapa, un calculo y una "
        "ejecucion, y ninguno sobra. (2) EL PROCESO A TRES ALTURAS: customer_validation, "
        "customer_development_process y customer_development_modelo, sus tres pares leidos "
        "y los tres D, puestos 377, 854 y 855. El informe lo declaro asi: tres nodos "
        "contando el mismo proceso a tres alturas, ninguno enlazado con el hijo, y los tres "
        "pares sanos; el problema no es que repitan, es que nadie sabe cual preside. LOS "
        "SEIS PUESTOS VERIFICAN, CERO FALLOS. MEDICION QUE ACOMPANA Y QUE HAY QUE DECLARAR: "
        "la forma mecanica, o sea trios con sus tres pares leidos y los tres en D, da 1.773 "
        "al corte 3.388 y daba 1.354 ya al corte 2.117. Los declarados son DOS. La figura "
        "no es la forma: es la forma MAS la lectura de que la fuente partio un mismo tema "
        "en tres cortes reales, y eso no lo decide un contador."
    ),
    "EL ESQUELETO COMPARTIDO": (
        "LOS TRES. (1) puesto 2001 D, customs_bonded_warehouses contra foreign_trade_zones: "
        "el esqueleto comun son dos lineas, evaluar si conviene y contactar a la oficina que "
        "lo administra; en el almacen la mercancia solo espera y en la zona se le puede "
        "trabajar encima. (2) puesto 2011 D, financiamiento_sba_exportacion contra "
        "programas_ex_im_bank: mismo esqueleto, capital de trabajo y consulta al servicio "
        "comercial; uno pasa por un prestamista privado y el otro es el banco. (3) LD-02, "
        "channels_hypothesis_physical contra channels_hypothesis_web_mobile, cuya propia "
        "lectura lo dice con estas palabras: ES EL ESQUELETO COMPARTIDO, figura de los "
        "puestos 2001 y 2011, misma forma y contenido distinto por el medio. EL TERCERO ES "
        "UNA LECTURA DIRIGIDA Y NO UN PUESTO, y por eso ningun grep sobre el archivo de "
        "veredictos lo iba a encontrar nunca: no esta ahi. Los dos puestos verifican."
    ),
    "LAS DOS ADUANAS": (
        "LOS CINCO, todos de exportacion y todos D, verificados uno por uno: puesto 2008, "
        "import_regulations_foreign_governments contra licencia_exportacion_regulaciones; "
        "puesto 2013, barreras_comerciales_no_arancelarias contra "
        "licencia_exportacion_regulaciones; puesto 2037, documentacion_exportacion contra "
        "licencia_exportacion_regulaciones; puesto 2054, export_administration_regulations "
        "contra import_regulations_foreign_governments; y puesto 2070, "
        "barreras_comerciales_no_arancelarias contra export_administration_regulations. LOS "
        "CINCO VERIFICAN, CERO FALLOS. Y LA FORMA SE VE MEJOR CON LOS NODOS DELANTE QUE CON "
        "LA CUENTA: los cinco pares se reparten entre CUATRO nodos, dos de la regla ajena "
        "(import_regulations_foreign_governments y barreras_comerciales_no_arancelarias) y "
        "dos de la propia (licencia_exportacion_regulaciones y "
        "export_administration_regulations). La asimetria declarada, contra la regla ajena "
        "hay recurso y contra la propia no, vive en esos cuatro nodos."
    ),
    "LA BIFURCACION": (
        "LOS DOS, y los dos cuelgan del mismo nodo: certificados_genericos_de_origen, que "
        "en su paso 1 manda confirmar que el producto NO califica para ningun tratado, o "
        "sea que empieza declarando que no es el otro. Puesto 2030 D, contra "
        "autocertificacion_del_exportador; y puesto 2050 D, contra "
        "certificacion_origen_producto. LOS DOS VERIFICAN. LA FRONTERA MAS LIMPIA QUE DIO "
        "EL EJERCICIO, y es limpia por donde esta escrita: dentro del propio nodo, no en un "
        "registro externo. AVISO PARA QUIEN BUSQUE ESTA FIGURA CON UN CONTADOR: la palabra "
        "bifurcacion aparece en la razon de un solo puesto del archivo, el 2198, y ese NO "
        "es ninguno de los dos ejemplares."
    ),
    "LOS DOS PARES QUE NO SE CRUZAN": (
        "EL UNICO EJEMPLAR, con sus cuatro nodos y sus cuatro puestos, todo de cobro "
        "bancario en exportacion. LAS DOS PAREJAS GEMELAS, las dos A: puesto 1942, "
        "carta_de_credito_letter_of_credit contra letters_of_credit; y puesto 1969, "
        "documentary_collections contra letra_de_cambio_bill_of_exchange. LOS DOS CRUCES "
        "ENTRE PAREJAS, los dos D: puesto 2034, carta_de_credito_letter_of_credit contra "
        "letra_de_cambio_bill_of_exchange; y puesto 2059, letra_de_cambio_bill_of_exchange "
        "contra letters_of_credit. LOS CUATRO VERIFICAN. POR QUE ES UN EJEMPLAR Y NO "
        "CUATRO: la figura es la relacion entre las dos parejas, no cada par por separado, "
        "y por eso el campo cobertura dice UNO donde hay cuatro puestos. Es la forma de un "
        "catalogo SANO con dos instrumentos distintos: la duplicacion esta dentro de cada "
        "pareja y no entre ellas."
    ),
    "LA A DE BLOQUE (P.4)": (
        "EL EJEMPLAR Y EL CONTRAEJEMPLO, y los dos son LECTURAS DIRIGIDAS, no puestos del "
        "cribado: por eso ningun barrido sobre docs/INTRA_DOMINIO_VEREDICTOS.jsonl los "
        "encuentra. EJEMPLAR: LD-06, project_close_out contra reunion_conclusion_proyecto. "
        "project_close_out declara fuente DOBLE, verificado hoy contra el grafo: A Project "
        "Manager's Book of Forms de Snyder MAS Never Lose a Customer Again de Coleman. Sus "
        "pasos 1 a 5 son el cierre formal de proyecto y sus pasos 6 a 11 son el bloque de "
        "Coleman, que repite con el otro nodo casi paso por paso, incluida la misma cifra de "
        "tres meses de monitoreo posterior. CONTRAEJEMPLO: LD-07, el MISMO bloque injertado "
        "contra el OTRO nodo de Coleman, y sale D. Lo que el contraejemplo prueba, y es por "
        "lo que va al lado del ejemplar: que un nodo lleve un injerto no significa que "
        "repita con todo su libro de origen. Repite con uno, y hay que leer cual. DONDE SE "
        "BUSCAN LAS DEMAS, escrito en P.4: la firma de P.2 las levanta, y son los 67 nodos "
        "de fuente doble del catalogo."
    ),
    "LA COLA DEL DOMINIO SE AGOTA POR DENTRO (9.27)": (
        "LOS TRES DOMINIOS MEDIDOS SON environmental, exportacion y franquicias, y aqui van "
        "REMEDIDOS EN ESTA VUELTA sobre el archivo cerrado en 3.388, con el criterio de "
        "corte declarado: tercios por numero de pares (n dividido entre 3) sobre el orden de "
        "puesto dentro del dominio. environmental, puestos 1772 a 1941, 170 pares: 32,1 por "
        "ciento, 12,5 y 6,9, cierre 17,1. exportacion, puestos 1942 a 2071, 130 pares: 30,2, "
        "2,3 y 2,3, cierre 11,5. franquicias, puestos 2072 a 2219, 148 pares: "
        "20,4, 4,1 y 12,0, cierre 12,2.DOS BAJAN Y EL TERCERO YA NO: la figura se "
        "escribio el 11 ago 2026 con franquicias ABIERTO y 32 pares leidos, dando 66,7 por "
        "ciento en su primer tercio y 0,0 en el ultimo; hoy el dominio esta CERRADO con 148 "
        "pares y su ultimo tercio SUBE a 12,0. DISCREPANCIA DECLARADA Y NO ARREGLADA: la "
        "cifra vieja no se toca, porque era correcta para su corte y para los 32 pares sobre "
        "los que se midio. Lo que la remedicion dice es que el tercer ejemplar de esta figura "
        "SE MIDIO ABIERTO, que es exactamente el error que la propia figura advierte: un "
        "dominio a medio leer no describe al dominio. LA FIGURA SIGUE EN PIE EN SUS DOS "
        "PRIMEROS DOMINIOS, y su tercero necesita releerse con el dominio ya cerrado."
    ),
    "cobrar una A sin fundir": (
        "EL EJEMPLAR, con su puesto: la A del PUESTO 488, gestion_de_portafolio_gates_go_kill "
        "contra sistema_gates_go_kill, verificada hoy en el archivo. El nodo que se queda "
        "fuera de la fusion y cobra su A por poda es gestion_de_portafolio_gates_go_kill, ya "
        "escrito en el campo miembros; la operacion que lo ejecuta es OP-M-01-SEXTO, ya "
        "escrita en el campo operaciones; y sus DOS A se cobran en la poda mientras sus TRES "
        "D son el motivo de que el nodo viva. LA SEGUNDA A DEL MISMO NODO, para que la cuenta "
        "de dos cuadre y no haya que buscarla: esta dentro del acto de seis de gates, y el "
        "par que la acompana del otro lado del triangulo es el puesto 801, "
        "requisitos_gates_con_dientes contra sistema_gates_go_kill, tambien A y tambien "
        "verificado hoy."
    ),
    "EL PASO DE OFICIO": (
        "ACOTADA EL 14 ago 2026 (vuelta 18), NO NOMBRADA TODAVIA, y se dice en ese orden a "
        "proposito: el encargo de esta vuelta pedia medir cuantos son y donde estan, no "
        "cerrarla. MEDIDO con scripts/loop/vuelta18_figuras.py sobre "
        "dataset/metadata/master_graph.json y sobre las 3.388 lineas del archivo: el dominio "
        "exportacion tiene 158 NODOS VIVOS y 130 pares leidos. La linea generica de acudir a "
        "la oficina aparece en algun paso de SEIS de esos 158 nodos, que son "
        "barreras_comerciales_no_arancelarias (paso 1), desmitificacion_barreras_exportacion "
        "(paso 2), ecosistema_global_emprendimiento_gee (paso 1), "
        "investigacion_empresa_extranjera (pasos 4 y 5), programas_ex_im_bank (paso 6) y "
        "resolucion_problemas_de_pago (paso 2). DOS de los seis la traen en su PASO 1. Y los "
        "pares del dominio donde al menos uno de los dos lados la trae son DIEZ de los 130. "
        "EL SEIS CONFIRMA LA MEDIA DOCENA que esta nota ya declaraba, y ese es el unico "
        "numero de esta figura que estaba escrito. LO QUE LA MEDICION NO CONFIRMA, y se "
        "declara sin arreglar el campo: el campo cobertura dice medio dominio exportacion, y "
        "medido son 6 nodos de 158 y 10 pares de 130. La cifra vieja no se toca. CRITERIO DE "
        "LA MEDICION, declarado porque decide el resultado: es una HEURISTICA DE PALABRAS "
        "sobre una lista corta de formas de nombrar la oficina, no una lectura de los 158 "
        "nodos. Por eso es una COTA y un AVISO ORIENTATIVO, no un veredicto: puede callar de "
        "menos si un nodo lo dice con otras palabras. NOMBRAR SUS EJEMPLARES SIGUE PENDIENTE."
    ),
}


def main():
    with io.open(RUTA, encoding="utf-8") as fh:
        lineas = fh.read().split("\n")

    salida = []
    tocadas = []
    vistos = set()
    for i, linea in enumerate(lineas):
        if not linea.strip():
            salida.append(linea)
            continue
        d = json.loads(linea)
        nombre = d.get("nombre")
        if d.get("tipo") == "figura" and nombre in ADICIONES:
            if CABECERA.strip() in d["nota"]:
                print("YA ESTABA PUESTA en:", nombre)
                salida.append(linea)
                continue
            antes = {k: v for k, v in d.items() if k != "nota"}
            d["nota"] = d["nota"] + CABECERA + ADICIONES[nombre] + " " + CRITERIO
            despues = {k: v for k, v in d.items() if k != "nota"}
            assert antes == despues, nombre
            salida.append(json.dumps(d, ensure_ascii=False))
            tocadas.append((i + 1, nombre))
            vistos.add(nombre)
        else:
            salida.append(linea)

    faltan = set(ADICIONES) - vistos
    if faltan:
        raise SystemExit("NO SE ENCONTRARON ESTAS FIGURAS: %s" % sorted(faltan))

    identicas = sum(1 for a, b in zip(lineas, salida) if a == b)
    print("lineas del archivo : %d" % len([l for l in lineas if l.strip()]))
    print("lineas tocadas     : %d" % len(tocadas))
    for n, nombre in tocadas:
        print("   linea %-4d %s" % (n, nombre))
    print("lineas identicas   : %d" % identicas)
    assert identicas == len(lineas) - len(tocadas)

    with io.open(RUTA, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(salida))

    with io.open(RUTA, encoding="utf-8") as fh:
        rel = [json.loads(l) for l in fh if l.strip()]
    print("entradas tras escribir: %d" % len(rel))
    figs = [e for e in rel if e.get("tipo") == "figura"]
    print("figuras: %d" % len(figs))
    for e in figs:
        if e["nombre"] in ADICIONES:
            print("   %-48s nota de %d caracteres" % (e["nombre"], len(e["nota"])))


if __name__ == "__main__":
    main()
