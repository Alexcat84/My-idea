# -*- coding: utf-8 -*-
"""VUELTA 19, TAREA 2.B: las TRES figuras que faltaban, nombradas.

ESCRIBE en docs/plan/INVENTARIO.jsonl y NADA MAS. Tres entradas tocadas, las
tres de forma ADITIVA al final de su campo nota:

  SUBCONJUNTO ESTRICTO                    -> los 23 nombrados y verificados
  LA FIRMA POSICIONAL DEL INJERTO (P.2)   -> las dos sedes, con punteros verificados
  EL PASO DE OFICIO                       -> los tres declarados por su nombre

Toda cifra sale de scripts/loop/vuelta19_figuras.py, corrido en esta vuelta.
El script comprueba antes de escribir que las 668 lineas restantes quedan
identicas byte a byte y que solo cambia la clave nota. Si algo no cuadra, ABORTA.
"""
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[2]
INV = RAIZ / "docs" / "plan" / "INVENTARIO.jsonl"

CRITERIO = (
    " CRITERIO DE EJEMPLAR, el de la vuelta 18 y CONFIRMADO por el acta de la vuelta 18 "
    "(seccion 3, adjudicacion 1): un ejemplar es una instancia DECLARADA POR ESCRITO (en "
    "docs/INTRA_DOMINIO_INFORME.md, en docs/BANCO_DE_TEXTOS.md, en un expediente, en una "
    "lectura dirigida o en la razon del propio veredicto), no cualquier par que calce con "
    "la forma."
)

SUBCONJUNTO = (
    " EJEMPLARES NOMBRADOS EL 14 ago 2026 (vuelta 19), adicion declarada, nada borrado. "
    "LAS 23 QUE EL CAMPO cobertura DECLARA SON EXACTAMENTE LAS 23 RAZONES DEL ARCHIVO QUE "
    "TRAEN LA ETIQUETA SUBCONJUNTO ESTRICTO EN MAYUSCULAS, y no es una coincidencia "
    "elegida: la aritmetica del informe reproduce exacta sobre ese conjunto. LOS 23 "
    "PUESTOS, verificados uno por uno en esta vuelta contra "
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl con scripts/loop/vuelta19_figuras.py (que el "
    "puesto existe, con clase A y entre esos dos nodos), CERO FALLOS y LOS 23 EN A. En "
    "core: 1182 desarrollo_en_espiral con design_test_repeat, 1332 "
    "metodo_valor_presente_neto con valor_presente, y 1573 design_test_repeat con "
    "design_thinking_proceso. En entrega: 1601 y 1602, los dos del mismo nodo "
    "calcular_peso_dimensional_antes_cotizar, contra medir_paquete_redondeando_hacia_arriba "
    "y contra conocer_limites_peso_tamano_courier. En environmental: 1776 "
    "evitar_greenwashing con evitar_greenwashing_2, 1783 critica_eco_eficiencia con "
    "eco_eficiencia_critica, 1794 critica_al_pib_como_metrica con "
    "critica_del_pib_como_metrica_de_progreso, y 1811 liderazgo_ceo_sostenibilidad con "
    "vision_alineacion_sostenibilidad. En exportacion, siete: 1943 "
    "export_administration_regulations con regulaciones_exportacion_ear, 1947 "
    "seguro_de_carga_transporte con seguro_exportacion, 1952 "
    "incoterms_reglas_comerciales_internacionales con terminos_de_venta_incoterms, 1966 y "
    "1967, los dos de enfoque_paso_a_paso_investigacion_mercado, contra "
    "screening_mercados_potenciales y contra evaluacion_mercados_objetivo, 2022 "
    "licenciamiento_tecnologico con proteccion_propiedad_intelectual_internacional, y 2043 "
    "consejos_distrito_exportacion_dec con uso_del_us_commercial_service. En franquicias, "
    "siete: 2072 gestion_terminacion_franquiciado con terminacion_franquiciado_causas, 2074 "
    "y 2075, los dos de cinco_categorias_costos_franquicia, contra "
    "estimacion_inversion_inicial_franquiciador y contra costos_preparacion_franquicia, 2076 "
    "y 2090, los dos de contratar_abogado_especializado_franquicias, contra "
    "eleccion_abogado_franquicias y contra contratar_abogado_franquicias, 2079 "
    "estrategia_multicanal_expansion con franquicia_mas_crecimiento_corporativo_hibrido, y "
    "2087 sitio_web_captura_leads con sitio_web_franquicia. LA ARITMETICA DEL INFORME, "
    "REPRODUCIDA CON INSTRUMENTO EN VEZ DE CITADA: docs/INTRA_DOMINIO_INFORME.md declara de "
    "12 ejemplares a 23, con once nuevos en el tramo (1966, 1967, 2022, 2043, 2072, 2074, "
    "2075, 2076, 2079, 2087 y 2090). Medido hoy: los puestos con la etiqueta anteriores a "
    "ese tramo son DOCE y los once nuevos son esos once, todos con la etiqueta. Doce mas "
    "once, 23. ES LA FIGURA DOMINANTE DE DOS DOMINIOS: siete de los 23 son de exportacion y "
    "siete de franquicias. DISCREPANCIA DECLARADA Y NO ARREGLADA, y el campo cobertura no se "
    "toca: el puesto 511, disenar_tests_pass_fail contra diseno_experimentos_pass_fail, A, "
    "esta DECLARADO POR ESCRITO como subconjunto estricto en el informe, en la tabla de la "
    "tanda R30, con estas palabras: NADA. Es un subconjunto estricto; y ademas las razones "
    "de los puestos 1783 y 1943 lo citan por su numero dentro de la nomina corriente de la "
    "figura. Pero su propia razon NO trae la etiqueta. O sea que el 23 cuenta ETIQUETAS y no "
    "INSTANCIAS DECLARADAS: contando instancias declaradas por escrito son 24. La cifra "
    "vieja se queda como esta y la diferencia queda escrita al lado."
)

FIRMA = (
    " SEDES NOMBRADAS EL 14 ago 2026 (vuelta 19), adicion declarada, nada borrado. NO SE "
    "COPIA LA NOMINA ENTERA AQUI, que es larga: se nombra DONDE VIVE, y los punteros van "
    "verificados con instrumento propio en esta vuelta, scripts/loop/vuelta19_figuras.py "
    "sobre dataset/metadata/master_graph.json. DONDE VIVEN LOS 67 CANDIDATOS: "
    "docs/plan/10_INVENTARIO.md, seccion LAS FUENTES, ya normalizadas, tabla LOS SEIS QUE "
    "APORTAN INJERTOS. Reproducida celda por celda en esta vuelta y calza entera: Hugos 107 "
    "en primera o unica posicion y 21 en segunda o posterior; Coleman 68 y 15; Horowitz 88 y "
    "14; Weinberg 67 y 13; Rackham 47 y 4; Mollick 47 y 3. La columna de segunda posicion "
    "suma 70 contando por libro, y los NODOS DISTINTOS son 67, porque TRES nodos declaran "
    "dos de los seis libros a la vez: metas_vs_proposito (Horowitz y Coleman), "
    "viral_loop_marketing (Coleman y Weinberg) y principio_calidad_mvp (Horowitz y Hugos). "
    "Y los 67 salen tambien por la via corta y dan el mismo conjunto exacto: los nodos vivos "
    "del grafo cuyo campo fuente trae mas de un libro son 67. DONDE VIVE LA NOMINA DE LOS "
    "43: docs/plan/01_FUENTES.md, seccion LA TANDA DE LOS INJERTOS: leidos los 43, del 11 "
    "ago 2026, con su saldo (46 declaraciones, 43 nodos distintos, 43 confirmados, cero "
    "arrastre), su tabla de evidencia por grupo (Coleman 15, Horowitz 13, Weinberg 13, "
    "Rackham 4) y las cuatro decisiones de fuente que salen de ella, OP-F-04-COL, "
    "OP-F-04-HOR, OP-F-04-WEI y OP-F-04-RAC. LOS EJEMPLARES CITABLES POR NODO, los DIEZ "
    "verificados en esta vuelta contra el grafo (vivos, y con segundo libro en su campo "
    "fuente): los cuatro con su corte exacto escrito, uno por libro, "
    "five_whys_inversion_proporcional (pasos 1 a 5 contra 6 a 9, bloque de Rackham), "
    "voz_del_cliente_voc (1 a 5 contra 6 a 10, Coleman), background_startup_vs_corporativo "
    "(1 a 4 contra 5 a 9, Horowitz) y enfoque_motor_unico_crecimiento (1 a 4 contra 5 a 9, "
    "Weinberg); los tres que el propio doc separa porque no son un simple apendice, "
    "viral_loop_marketing (tres libros y 30 pasos), coeficiente_viral (16 pasos) y "
    "decision_de_vender_startup (tres grafias y 34 pasos, con Horowitz declarado dos veces); "
    "y los tres de Mollick de OP-F-02, future_scenarios_planning, gut_check y "
    "brainstorming_divergente. LOS 21 DE HUGOS ESTAN NOMBRADOS UNO A UNO en "
    "docs/plan/BANCO_DEL_PLAN.md, ficha P.2, y por eso no se copian aqui. DOS DISCREPANCIAS "
    "DECLARADAS Y NO ARREGLADAS, y el campo cobertura no se toca. PRIMERA: la nomina de la "
    "tanda de los cuatro libros mide CUARENTA Y CUATRO nodos distintos con mi instrumento y "
    "el doc publica 43. La diferencia entera esta en Horowitz, que en la tabla de sede de "
    "10_INVENTARIO.md figura con 14 en segunda posicion y en la tabla de grupos de "
    "01_FUENTES.md con 13; con 14 salen 44 nodos distintos y con 13 salen 43. CUAL DE LOS 14 "
    "QUEDA FUERA NO SE PUEDE DECIR, porque la nomina de los 13 no esta escrita en ninguna "
    "parte: del grupo solo hay conteos. SEGUNDA: 01_FUENTES.md explica el paso de 46 "
    "declaraciones a 43 nodos nombrando tres solapes, y uno de los tres es "
    "decision_de_vender_startup por declarar Horowitz dos veces con dos grafias. Medido hoy, "
    "ese caso NO reduce esa cuenta, porque un nodo que declara el mismo libro dos veces "
    "sigue siendo un nodo y un libro; y los nodos que si declaran DOS libros distintos de "
    "los cuatro son solo DOS, metas_vs_proposito y viral_loop_marketing. Las dos cifras "
    "viejas quedan intactas, con su discrepancia al lado."
)

OFICIO_2 = (
    " EJEMPLARES NOMBRADOS EL 14 ago 2026 (vuelta 19), adicion declarada, nada borrado, y "
    "con la cota ya corregida arriba. LOS EJEMPLARES DECLARADOS POR ESCRITO SON TRES, Y "
    "ESTABAN EN EL SITIO DONDE LA VUELTA 18 NO MIRO: en la razon de los propios veredictos, "
    "que nombran la figura POR SU NOMBRE. Localizados y verificados en esta vuelta con "
    "scripts/loop/vuelta19_figuras.py. PUESTO 2045, D, barreras_comerciales_no_arancelarias "
    "contra import_regulations_foreign_governments: su razon dice comparten el paso de "
    "oficio del dominio, y define la figura entera, preguntarle a la oficina de comercio "
    "exterior propia antes de entrar a un mercado, que en este dominio es el primer paso de "
    "media docena de nodos y por si solo no decide ninguna clase. PUESTO 2054, D, "
    "export_administration_regulations contra import_regulations_foreign_governments: lo "
    "compartido es el paso de oficio del dominio, preguntarle al servicio comercial, ni un "
    "paso mas se solapa. PUESTO 2070, D, barreras_comerciales_no_arancelarias contra "
    "export_administration_regulations: lo compartido es el paso de oficio del dominio, ni "
    "un paso mas se solapa. LOS TRES SON D, LOS TRES DE exportacion, y se apoyan en TRES "
    "nodos, barreras_comerciales_no_arancelarias, export_administration_regulations e "
    "import_regulations_foreign_governments, los tres verificados vivos en el grafo y "
    "ninguno deprecado. EL 2045 ES LA SEDE DE LA FRASE media docena: es el unico puesto del "
    "archivo que la trae. LOS SEIS NODOS DE LA COTA Y LOS DIEZ PARES, renombrados aqui con "
    "la cota ya corregida a 141 vivos y verificados en esta vuelta: los nodos son "
    "barreras_comerciales_no_arancelarias (paso 1), desmitificacion_barreras_exportacion "
    "(paso 2), ecosistema_global_emprendimiento_gee (paso 1), investigacion_empresa_extranjera "
    "(pasos 4 y 5), programas_ex_im_bank (paso 6) y resolucion_problemas_de_pago (paso 2), "
    "los seis vivos; y los diez pares del dominio que tocan a alguno de los seis, "
    "verificados contra el archivo, son 1963 A, 1984 A, 1989 D, 2007 D, 2011 D, 2013 D, 2026 "
    "D, 2045 D, 2047 D y 2070 D. LA HEURISTICA DE LA VUELTA 18 CALLA DE MENOS, Y AHORA CON "
    "CIFRA EN VEZ DE CON AVISO: su lista de pistas trae la cadena us commercial service SIN "
    "PUNTOS, y el grafo escribe U.S. Commercial Service, asi que esa cadena no casa nunca. "
    "Recontado sobre los MISMOS 141 vivos, cambiando solo esa cadena por commercial service, "
    "la cota pasa de 6 nodos a 26, de 2 nodos con la linea en su PASO 1 a 7, y de 10 pares "
    "tocados a 40. LA PRUEBA DE QUE ESTO NO ES UNA DEFINICION MAS ANCHA SINO UN FALLO DE LA "
    "CADENA: de los tres nodos que sostienen los tres ejemplares DECLARADOS, dos no "
    "aparecian en la cota de seis, y uno de esos dos, "
    "import_regulations_foreign_governments, trae la linea en su PASO 1, Consultar con el "
    "U.S. Commercial Service antes de exportar a un nuevo pais. LAS DOS CIFRAS QUEDAN "
    "ESCRITAS CON SU CRITERIO AL LADO Y NINGUNA SE BORRA: 6 de 141 con las pistas de la "
    "vuelta 18, y 26 de 141 con la cadena corregida. Y LA SEGUNDA SE ACERCA A LO DECLARADO "
    "DONDE LA PRIMERA NO LLEGABA: el 2045 dice el PRIMER paso de media docena de nodos, y "
    "los nodos que traen la linea en su paso 1 son SIETE con la cadena corregida y eran DOS "
    "con la vieja. EL CAMPO cobertura, que dice medio dominio exportacion, SIGUE SIN "
    "TOCARSE: medido hoy son 26 nodos de 141 vivos y 40 pares de 130."
)


def serializar(obj, modelo):
    """Reserializa respetando el estilo de separadores de la linea original."""
    compacto = '", "' not in modelo and '": ' not in modelo
    if compacto:
        return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return json.dumps(obj, ensure_ascii=False)


def buscar(objs, tipo, nombre):
    idx = [i for i, e in enumerate(objs)
           if e.get("tipo") == tipo and e.get("nombre") == nombre]
    if len(idx) != 1:
        print("ABORTA: %s %s aparece %d veces" % (tipo, nombre, len(idx)))
        sys.exit(1)
    return idx[0]


def main():
    lineas = [l for l in INV.read_text(encoding="utf-8").splitlines() if l.strip()]
    objs = [json.loads(l) for l in lineas]
    print("entradas leidas: %d" % len(objs))

    plan = [("SUBCONJUNTO ESTRICTO", SUBCONJUNTO + CRITERIO),
            ("LA FIRMA POSICIONAL DEL INJERTO (P.2)", FIRMA + CRITERIO),
            ("EL PASO DE OFICIO", OFICIO_2)]

    tocadas = set()
    for nombre, adicion in plan:
        i = buscar(objs, "figura", nombre)
        if i in tocadas:
            print("ABORTA: la linea %d se toca dos veces" % (i + 1))
            sys.exit(1)
        tocadas.add(i)
        viejo = dict(objs[i])
        objs[i]["nota"] = viejo["nota"] + adicion
        if not objs[i]["nota"].startswith(viejo["nota"]):
            print("ABORTA: la adicion en %s no es aditiva" % nombre)
            sys.exit(1)
        resto_v = {k: v for k, v in viejo.items() if k != "nota"}
        resto_n = {k: v for k, v in objs[i].items() if k != "nota"}
        if resto_v != resto_n:
            print("ABORTA: cambio otra clave en %s" % nombre)
            sys.exit(1)
        print("  linea %-4d figura  %-42s nota +%d caracteres" % (
            i + 1, nombre, len(adicion)))

    finales = [serializar(e, lineas[i]) for i, e in enumerate(objs)]
    intactas = sum(1 for i in range(len(objs)) if finales[i] == lineas[i])
    print("  lineas byte a byte identicas: %d de %d, tocadas %d" % (
        intactas, len(objs), len(objs) - intactas))
    if intactas != len(objs) - len(plan):
        print("ABORTA: %d intactas y deberian ser %d" % (
            intactas, len(objs) - len(plan)))
        sys.exit(1)

    salida = "\n".join(finales) + "\n"
    INV.write_text(salida, encoding="utf-8", newline="\n")
    print("ESCRITO: %s" % INV)
    prohibidos = (chr(8212), chr(8211))  # guion largo y guion medio
    for mal in prohibidos:
        if mal in salida:
            print("AVISO: hay guion largo o medio en la salida")
            return 1
    print("cero guiones largos y cero guiones medios en el archivo entero")
    return 0


if __name__ == "__main__":
    sys.exit(main())
