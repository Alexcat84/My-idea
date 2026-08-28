import json

CORR = {
    21: {
        "campo_corregido": "direccion_leida",
        "valor_anterior": "build_measure_learn -> value_proposition_canvas",
        "valor_nuevo": None,
        "cita_corregida": "banco 9.6.2 (test de reconocimiento, senal de entregables)",
        "razon": (
            "CORRECCION DECLARADA (vuelta 105, TAREA 4.4, lectura entera a ciegas de los SATELITE de "
            "la TAREA 4.3). El texto viejo de razon y direccion_leida NO SE BORRA. Leidos hoy los dos "
            "nodos enteros y el banco 9.6.2 y 9.6.3 enteros. El paso 0 de la madre (\"Generar una "
            "hipotesis clara a partir de los Canvas de Value Proposition y Business Model\") usa el "
            "Value Proposition Canvas como INSUMO ya construido (complemento de origen, 'a partir de "
            "X') para el acto de GENERAR UNA HIPOTESIS; el hijo value_proposition_canvas describe en "
            "cambio como CONSTRUIR ese canvas (descargar plantilla, dibujar Customer Profile y Value "
            "Map, iterar hasta el Fit, comunicar y usar como scoreboard): es el procedimiento que "
            "PRODUCE el insumo, no el acto de generar una hipotesis a partir de el. Primer brazo del "
            "9.6.2 falla. La senal de entregables lo confirma: la madre entrega 'un ciclo completo "
            "documentado de Build-Measure-Learn con hipotesis, artefacto de prueba, metricas y "
            "aprendizajes' (el ciclo completo); el hijo entrega 'Canvas completo con Customer Profile "
            "y Value Map mapeados' (un insumo previo, no el ciclo ni la hipotesis). La madre conserva "
            "materia propia intacta: pasos 1 (construir el artefacto), 2 (medir) y 3 (aprender). "
            "SE MUEVE: el par pasa de DIRECCION AFIRMADA a NO RESUELTA. Clase D no cambia."
        ),
    },
    38: {
        "campo_corregido": "direccion_leida",
        "valor_anterior": "obtencion_compromiso -> enfoque_etapa_investigacion",
        "valor_nuevo": None,
        "cita_corregida": "banco 9.6.2 (test de reconocimiento, senal de entregables)",
        "razon": (
            "CORRECCION DECLARADA (vuelta 105, TAREA 4.4, lectura entera a ciegas de los SATELITE de "
            "la TAREA 4.3). El texto viejo de razon y direccion_leida NO SE BORRA. Leidos hoy los dos "
            "nodos enteros y el banco 9.6.2 y 9.6.3 enteros. El paso 4 de la madre (\"Pon tu esfuerzo "
            "de mejora en las etapas de investigacion Y demostracion de capacidad, no en el cierre\") "
            "nombra DOS etapas como destino del esfuerzo; el hijo enfoque_etapa_investigacion cubre "
            "SOLO la etapa de investigacion, y su propia tesis (\"si el vendedor desarrolla necesidades "
            "genuinas... las etapas de Demostracion de Capacidad y Obtencion de Compromiso fluyen "
            "naturalmente\") argumenta EXPLICITAMENTE que no hace falta invertir esfuerzo en "
            "demostracion, lo contrario de lo que el paso pide para esa mitad. Primer brazo del 9.6.2 "
            "falla: el hijo no cabe entero dentro del destino nombrado por el paso. La senal de "
            "entregables lo confirma: la madre entrega 'una lista clara de que cuenta como avance "
            "valido en CADA ETAPA de tu proceso de venta' (las cuatro etapas); el hijo entrega 'una "
            "checklist de planificacion de llamada... con metricas de tiempo dedicado a cada etapa', "
            "centrada en preguntas, no en avances validos. Los dos nodos comparten precursor comun "
            "(cuatro_etapas_llamada_de_ventas) sin que uno sea hijo del otro: 9.6.3, procedimiento "
            "propio a cada lado dentro del mismo libro (SPIN Selling), SANO. La madre conserva materia "
            "propia intacta: pasos 1 (objetivo de avance), 2 (evitar cierre de presion) y 3 (medir por "
            "avances). SE MUEVE: el par pasa de DIRECCION AFIRMADA a NO RESUELTA. Clase D no cambia."
        ),
    },
    66: {
        "campo_corregido": "direccion_leida",
        "valor_anterior": "cultura_justa_3 -> cultura_de_aprendizaje",
        "valor_nuevo": None,
        "cita_corregida": "banco 9.6.2 (test de reconocimiento, senal de entregables) y 9.6.3 (raiz comun, SANO)",
        "razon": (
            "CORRECCION DECLARADA (vuelta 105, TAREA 4.4, lectura entera a ciegas de los SATELITE de "
            "la TAREA 4.3). El texto viejo de razon y direccion_leida NO SE BORRA. Leidos hoy los dos "
            "nodos enteros y el banco 9.6.2 y 9.6.3 enteros. El paso 3 de la madre (\"Balancear la "
            "necesidad de accountability CON la proteccion al aprendizaje organizacional\") pide un "
            "acto de EQUILIBRIO entre dos fuerzas en tension (accountability y aprendizaje); el hijo "
            "cultura_de_aprendizaje (establecer mecanismos de analisis de datos, definir procesos de "
            "reforma, medir efectividad, institucionalizar la revision) desarrolla SOLO el lado del "
            "aprendizaje, sin una sola linea sobre accountability, sanciones o la tension entre los "
            "dos: no desarrolla el acto de balancear, solo el tema de uno de los dos platillos. Primer "
            "brazo del 9.6.2 falla. Ademas los dos nodos son de LIBROS DISTINTOS (Dekker vs Reason) y "
            "cultura_de_aprendizaje declara a 'cultura_justa' (componente hermano, no cultura_justa_3) "
            "entre sus nodos_previos: son DOS COMPONENTES PARES del modelo de cultura de seguridad de "
            "Reason (reporte, justicia, flexibilidad, aprendizaje), no madre e hijo por este paso. La "
            "senal de entregables lo confirma: la madre entrega una 'politica de cultura justa... con "
            "protocolos de segundas victimas y criterios de accountability'; el hijo entrega un "
            "'proceso institucionalizado de revision y aplicacion de lecciones aprendidas', sin "
            "relacion con accountability. 9.6.3: raiz comun (cultura de seguridad organizacional), "
            "procedimiento propio a cada lado, SANO. La madre conserva materia propia intacta: pasos "
            "1 (politicas de reporte sin penalizar), 2 (apoyo a segundas victimas) y 4 (criterios de "
            "conducta sancionable). SE MUEVE: el par pasa de DIRECCION AFIRMADA a NO RESUELTA. Clase "
            "D no cambia."
        ),
    },
}


def main():
    with open("docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl", encoding="utf-8") as f:
        t1 = [json.loads(l) for l in f if l.strip()]
    with open("docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl", encoding="utf-8") as f:
        t2 = [json.loads(l) for l in f if l.strip()]

    tocadas = []
    for fila in t1:
        if fila["puesto_tramo"] in (21, 38):
            fila["correccion_v105"] = CORR[fila["puesto_tramo"]]
            tocadas.append(fila["puesto_tramo"])
    for fila in t2:
        if fila["puesto_tramo"] == 66:
            fila["correccion_v105"] = CORR[66]
            tocadas.append(66)

    assert sorted(tocadas) == [21, 38, 66], tocadas

    with open("docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for fila in t1:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")
    with open("docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for fila in t2:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

    print("tocadas:", tocadas)


if __name__ == "__main__":
    main()
