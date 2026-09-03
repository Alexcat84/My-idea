# -*- coding: utf-8 -*-
"""vuelta159_tarea2a_relectura_conjunta.py . TAREA 2.a DE LA VUELTA 159.

LAS TRES EN DISPUTA, LEIDAS CONTRA LOS NODOS Y DECIDIDAS CON LA VARA (acta 158,
adjudicacion 6.4). El auditor escribio su caso en las secciones 3 y 3.1 del acta
158 y dijo con todas sus letras que no lo decide su pluma: MI LECTURA NO ES LA
VARA, EL NODO LO ES. Lo que se publica aqui es lo que se midio contra los nodos,
con el dossier `docs/loop/SALIDA_V159_T2A_DOSSIER.txt` delante.

LA VARA ES LA 6.4 DEL ACTA 157 CON LA CORRECCION DE LA 6.3 DEL ACTA 158:

    SE PUEDEN NOMBRAR DOS LINEAS DISTINTAS, UNA EN CADA NODO, Y DECIR QUE
    PROCEDIMIENTO DEL OTRO NODO EXPANDE CADA UNA?

y ESO ES UN EXISTENCIAL: un par que colapsa descarta ESE PAR, no el nodo. Por
eso cada razon de descarte de esta tarea dice TAMBIEN que ningun otro par
sostiene la figura y NOMBRA el par mas fuerte que se descarto.

EL RESULTADO, ADELANTADO AQUI PARA QUE SE VEA QUE NO ES UN SI A TODO:
  `LD-OPC05-005`  D vuelve a C  : el auditor tiene razon y era caida de la 157.
  `LD-OPC05-027`  C pasa a D    : el auditor tiene razon.
  `LD-OPC05-122`  C pasa a D    : el auditor tiene razon, y con eso se revocan
                                  la 6.4 del acta 155 y la lectura del lote 1 de
                                  la vuelta 157, que la sostuvieron las dos.

LAS GUARDAS SON LAS DE LA 2.d Y VIVEN EN `vuelta159_motor_veredictos.py`, que es
la fuente unica: frontera con sha256 de `dataset/`, censo y aristas antes y
despues, `n` en 3.388, prefijo intacto en las 154 razones, ningun par movido y
ninguna clase a `A`.

USO:  python scripts/loop/vuelta159_tarea2a_relectura_conjunta.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta159_motor_veredictos as motor  # noqa: E402

MARCA = "RELECTURA CONJUNTA DE LA VUELTA 159"


def cabeza(vieja, nueva):
    if nueva != vieja:
        return ("  [CORRECCION DECLARADA, %s (2026-09-03), ANADIDA SIN BORRAR "
                "NADA DE LO ANTERIOR: LA CLASE PASA DE %s A %s. " % (MARCA, vieja, nueva))
    return ("  [%s (2026-09-03), ANADIDA SIN BORRAR NADA DE LO ANTERIOR: LA "
            "CLASE SE QUEDA EN %s. " % (MARCA, vieja))


def nota_md(vieja, nueva, motivo):
    if nueva != vieja:
        return ("CORRECCION DECLARADA (vuelta 159, RELECTURA CONJUNTA): la clase "
                "pasa de ~~%s~~ a %s. %s." % (vieja, nueva, motivo[:260]))
    return ("RELECTURA CONJUNTA (vuelta 159): la clase SE SOSTIENE en %s y su "
            "caso queda escrito en la razon del registro de citas." % vieja)


V = {
    "LD-OPC05-005": ("C",
        "LA CLASE VUELVE DE D A C Y ES CORRECCION DE UN VEREDICTO MIO DE LA "
        "VUELTA 157, NO DE UNA CIFRA DEL AUDITOR. Verificado contra los dos "
        "nodos con el dossier de esta vuelta. LO QUE LA 157 MIDIO BIEN Y SE "
        "SOSTIENE: el par que tomo (paso 1 de aim_of_leadership, identificar "
        "quien esta fuera de lo esperado, contra el paso 13 de "
        "causas_comunes_vs_especiales, dar seguimiento y apoyo a quienes caen "
        "fuera de las tolerancias del grupo) SI COLAPSA en la misma linea. LO "
        "QUE LA 157 HIZO MAL, Y ES EXACTAMENTE LA LECCION DE LA 6.3 DEL ACTA "
        "158: descartar UN par no descarta la figura, porque la pregunta de la "
        "6.4 es un EXISTENCIAL. HAY OTRO PAR Y SOSTIENE LA C. LINEA 1, en "
        "aim_of_leadership, paso 2: INVESTIGAR LAS CAUSAS DE RAIZ DEL SISTEMA "
        "que afectan el desempeno general; la expanden los quince pasos de "
        "causas_comunes_vs_especiales, que son literalmente su como se hace "
        "(recopilar los datos en orden cronologico y no como distribucion "
        "agregada, graficar y calcular los limites, aplicar reglas de senal, "
        "LISTAR LAS CAUSAS COMUNES PROPIAS DE TU SISTEMA de diseno, materiales, "
        "instruccion y condiciones, y redisenar el proceso en vez de sancionar "
        "al individuo). LINEA 2, en causas_comunes_vs_especiales, paso 13: DAR "
        "SEGUIMIENTO Y APOYO A QUIENES CAEN FUERA DE LAS TOLERANCIAS DEL GRUPO; "
        "la expanden los pasos 1, 3 y 5 de aim_of_leadership (identificar con "
        "datos o criterio quien esta fuera de lo esperado, disenar formas de "
        "ayuda individual o de reconocimiento segun corresponda, y estudiar a "
        "quienes tienen desempeno excepcional para replicar sus metodos). SON "
        "DOS LINEAS DISTINTAS, UNA EN CADA NODO, CADA UNA EXPANDIDA POR UN "
        "PROCEDIMIENTO DEL OTRO, Y NINGUNO ES LA MADRE. El caso lo trajo el "
        "auditor en la seccion 3.1 del acta 158; lo que aqui se publica es la "
        "verificacion contra los nodos, no su prosa. Dossier en "
        "docs/loop/SALIDA_V159_T2A_DOSSIER.txt"),

    "LD-OPC05-027": ("D",
        "LA CLASE PASA DE C A D Y CORRIGE MI PROPIA LECTURA DEL LOTE 1 DE LA "
        "VUELTA 157, QUE LA SOSTUVO EN C. Verificado contra los dos nodos. LA "
        "IDA SE SOSTIENE: el paso 1 de metodologia_spin_selling (diagnosticar "
        "si tu venta es pequena o grande) lo expanden los pasos 1 a 3 de "
        "cierre_segun_complejidad_venta, que clasifican por valor, "
        "sofisticacion, relacion posventa, ciclo, monto y visibilidad, y "
        "ramifican el tratamiento. LA VUELTA NO SE SOSTIENE, Y BAJO LA 6.3 DEL "
        "ACTA 158 SE RECORRIO EL ESPACIO ENTERO ANTES DE DECIRLO: NINGUNA LINEA "
        "DE cierre_segun_complejidad_venta ESTA EXPANDIDA POR UN PROCEDIMIENTO "
        "DE metodologia_spin_selling. EL PAR MAS FUERTE QUE SE DESCARTA es el "
        "paso 3 de cierre (minimizar el uso de tecnicas de cierre y enfocar el "
        "esfuerzo en las etapas de indagacion SPIN) contra los pasos 2 y 3 de "
        "SPIN: el paso 2 REPITE la linea en vez de expandirla (abandonar el "
        "enfoque en cierres agresivos y manejo de objeciones) y el paso 3 "
        "APLAZA el como a capitulos posteriores, que es remision y no "
        "procedimiento. EL SEGUNDO MAS FUERTE, TAMBIEN DESCARTADO Y POR OTRO "
        "MOTIVO: el paso 4 de SPIN (medir el impacto de la investigacion "
        "mejorada) contra el paso 6 de cierre (medir tiempo de transaccion y "
        "tasa de exito antes y despues), que si es expansion pero es OTRA VEZ "
        "UNA LINEA DE SPIN EXPANDIDA POR CIERRE, o sea LA MISMA DIRECCION, y la "
        "figura pide las dos. Los cuatro pasos de SPIN son diagnostico, "
        "decision, remision y cifra de resultado: ninguno procedimenta una "
        "linea de cierre. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA, "
        "que es el tercer caso del 9.22. El auditor dio D a ciegas en el acta "
        "158 y su lectura coincide con esta"),

    "LD-OPC05-122": ("D",
        "LA CLASE PASA DE C A D, Y CON ESTO SE REVOCAN DOS ADJUDICACIONES QUE "
        "LA SOSTUVIERON: LA 6.4 DEL ACTA 155 Y MI PROPIA LECTURA DEL LOTE 1 DE "
        "LA VUELTA 157. Verificado contra los dos nodos. LA VUELTA SE SOSTIENE: "
        "el paso 4 de error_proofing_servicio (simplificar el trabajo para "
        "reducir la posibilidad de error humano) lo expanden los seis pasos de "
        "metodologia_6s (sacar lo que no se necesita, ordenar herramientas y "
        "materiales, limpiar, estandarizar el habito, sostener la disciplina). "
        "LA IDA NO SE SOSTIENE: el paso 6 de 6S es SAFETY, revisa e integra "
        "practicas seguras en cada etapa de tu trabajo, o sea SEGURIDAD "
        "OCUPACIONAL, y error_proofing_servicio es PREVENCION DE ERROR EN "
        "PROCESOS DE SERVICIO; sus diez pasos hablan de actividades propensas a "
        "error, eliminacion, sustitucion, simplificacion, deteccion temprana, "
        "mitigacion de impacto, los cinco principios, dispositivos fisicos o "
        "logicos y validacion antes de escalar, y NINGUNO EJECUTA integrar "
        "practicas seguras. Materia distinta, no expansion. Y LA RAZON VIEJA SE "
        "DELATABA SOLA: decia que el paso 6 de 6S NOMBRA la seguridad y no la "
        "procedimenta, y NOMBRAR SIN PROCEDIMENTAR ES LO QUE LA 6.4 EXCLUYE. "
        "BAJO LA 6.3 DEL ACTA 158 SE RECORRIO EL ESPACIO ENTERO: NINGUNA OTRA "
        "LINEA DE metodologia_6s ESTA EXPANDIDA POR UN PROCEDIMIENTO DE "
        "error_proofing_servicio. EL PAR MAS FUERTE QUE SE DESCARTA es el paso "
        "1 de 6S (Sort, elimina de tu area de trabajo todo lo que no necesites) "
        "contra el paso 2 de error proofing (evaluar si la actividad puede "
        "eliminarse completamente): suenan igual y no lo son, porque uno elimina "
        "OBJETOS del puesto de trabajo y el otro elimina ACTIVIDADES del "
        "proceso, y sujeto distinto es la definicion de D y no de C. UNA SOLA "
        "DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),
}


def main():
    return motor.aplicar(
        "VUELTA 159, TAREA 2.a: LAS TRES EN DISPUTA, RELECTURA CONJUNTA",
        V, MARCA, cabeza, nota_md, ids_esperados=list(V))


if __name__ == "__main__":
    raise SystemExit(main())
