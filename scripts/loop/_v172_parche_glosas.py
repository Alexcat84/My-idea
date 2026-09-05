# -*- coding: utf-8 -*-
r"""_v172_parche_glosas.py . ANDAMIO DE UN SOLO USO DE LA VUELTA 172, TAREA 1.b.

Sustituye los dos diccionarios de glosa del clon
`vuelta172_tarea1_registrar_acta171.py` por los de la vuelta 172. Vive en
`scripts/loop/` y NO bajo `docs/`, que es la leccion medida de las vueltas 170 y
171: un borrador bajo `docs/` envenena a `vuelta48_contar_ld.py`.

USO:  python scripts/loop/_v172_parche_glosas.py
"""
import io
import os
import py_compile

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "scripts", "loop", "vuelta172_tarea1_registrar_acta171.py")

QUE_HACE = '''QUE_HACE_ESTA_VUELTA = {
    "6.1": ("VA A EJECUTARSE EN LA TAREA 2.a DE ESTA VUELTA, Y AL ESCRIBIR ESTA LINEA "
            "TODAVIA NO HA CORRIDO. `docs/loop/reportes/REPORTE_V<N>.md` entra en la "
            "lista de narrativos del bucle de `vuelta48_contar_ld.py`, POR PATRON de la "
            "carpeta de archivo y no por el nombre de una vuelta, o dentro de tres "
            "vueltas hay que volver a tocarla. No es doctrina nueva ni es la guarda "
            "general sobre ficheros bajo `docs/` que el acta 170 reservo al fundador: "
            "es la exclusion que el instrumento YA TIENE para `REPORTE.md`, aplicada a "
            "un fichero que no se le parece sino que ES EL MISMO, y lo prueba el sha256 "
            "identico al blob de `ca55afd8`. Con su caso positivo por mutacion, que "
            "tiene que CAER si alguien la estrecha o si el archivo vuelve a contar."),
    "6.2": ("VA A EJECUTARSE EN LA TAREA 3 DE ESTA VUELTA, Y AL ESCRIBIR ESTA LINEA "
            "TODAVIA NO HA CORRIDO. La vara que asigna un numero es la de las ENTRADAS "
            "ESCRITAS, las que tienen seccion propia, y eso lo dice el codigo de "
            "`serie_de_registros.py`, que computa el siguiente libre sobre las cabeceras "
            "escritas y no sobre las menciones. Una mencion en prosa no asigna un "
            "numero; una entrada escrita si. Las 16 filas de la segunda tanda de "
            "`docs/plan/LECTURAS_DIRIGIDAS.md` ganan `LD-139` a `LD-154` por ADICION "
            "PURA, con los numeros COMPUTADOS y sin tocar una palabra de su texto, y "
            "con dos guardas que tienen que caer por mutacion: que el numero se compute "
            "y no se teclee, y que NINGUN numero por encima de `LD-138` tenga seccion "
            "propia. Si alguno la tuviera, hay una asignacion ajena y esta vuelta PARA."),
    "6.3": ("VA A EJECUTARSE EN LA TAREA 2.b DE ESTA VUELTA, Y AL ESCRIBIR ESTA LINEA "
            "TODAVIA NO HA CORRIDO. Y ES LA ADJUDICACION QUE HA CAMBIADO LA FORMA DE "
            "ESTA ENTRADA: dice que el `R.40` publica 'VIA: EJECUTADA' y 'EJECUTADA, "
            "TAREA 3 de esta vuelta' sobre una tarea que no se corrio. Se corrige por "
            "el carril del banco `9.10`, la frase vieja ENTERA Y TACHADA, la correccion "
            "fechada debajo con la medicion pegada, y el reparto por via RECOMPUTADO "
            "POR INSTRUMENTO. No se toca la glosa de la 6.2 del `R.40`, que describe "
            "bien lo que paso, parada incluida."),
    "6.4": ("VA A EJECUTARSE EN LA TAREA 4.a DE ESTA VUELTA, Y AL ESCRIBIR ESTA LINEA "
            "TODAVIA NO HA CORRIDO. El caso `F` de "
            "`vuelta171_tarea5a_mutacion_enchufe.py` se refunda sobre SUJETO CONGELADO: "
            "hoy mira el arbol vivo y por eso da EXIT 1, y era cierto solo durante los "
            "minutos entre archivar la 170 y pisar `REPORTE.md`. El escenario se fabrica "
            "en un temporal como hacen sus otros nueve casos, y el arnes tiene que salir "
            "verde HOY y seguir verde dentro de diez vueltas. La cifra que el reporte de "
            "la 171 publico ('10 casos, 10 pasan, 10 caen') era cierta cuando se corrio "
            "y no se retira: lo que no se sostiene es el arnes."),
    "6.5": ("VA A EJECUTARSE EN LA TAREA 4.b DE ESTA VUELTA, Y AL ESCRIBIR ESTA LINEA "
            "TODAVIA NO HA CORRIDO. Los tres arneses de la 171 "
            "(`vuelta171_mutacion_busqueda_acta.py`, "
            "`vuelta171_tarea1a_mutacion_registro.py` y "
            "`vuelta171_tarea5a_mutacion_enchufe.py`) entran en la nomina de "
            "`verificar_mutaciones_viejas.py`. EL ORDEN ES OBLIGATORIO Y NO ES "
            "CAPRICHO: primero la 6.4 y despues la nomina, o se mete un rojo dentro de "
            "la bateria."),
    "6.6": ("VA A EJECUTARSE EN LA TAREA 5 DE ESTA VUELTA, Y AL ESCRIBIR ESTA LINEA "
            "TODAVIA NO HA CORRIDO. Nace `scripts/loop/cerrar_reporte.py`, de nombre "
            "estable y sin numero de vuelta como sus hermanos, y hace en UN SOLO ACTO "
            "lo que `vuelta171_tarea1b_cerrar_reporte_170.py` ya sabia hacer: pega la "
            "cabecera tallada, anexa el cuerpo, escribe el veredicto y RELEE DEL DISCO. "
            "Cae en ROJO si al terminar falta cualquiera de las cuatro piezas. ESTA "
            "VUELTA SE CIERRA CON EL, que es la unica forma de saber si sirve."),
    "6.7": ("SE ACATA SIN TOCAR NADA. La adjudicacion da por correcto el `D.1` de la "
            "vuelta 171 (medir la apertura antes de todo, invirtiendo el orden del "
            "encargo) y dice que la regla es permanente. Esta vuelta la ha vuelto a "
            "aplicar igual, con la misma desviacion declarada en el commit de su bloque "
            "de apertura, y no reabre nada."),
    "6.8": ("SE ACATA SIN TOCAR NADA. El `D.2` (adaptar el patron de caidas) queda "
            "adjudicado como correcto y ademas probado. Esta vuelta hereda el patron "
            "TAL CUAL, sin ensancharlo ni una letra, y vuelve a publicar el conteo con "
            "el patron viejo al lado para que se vea que no se afloja."),
    "6.9": ("SE ACATA SIN TOCAR NADA. El `D.3` (tachar solo la clausula falsa y dejar "
            "en pie la parte cierta de la oracion) queda adjudicado como correcto. La "
            "correccion del `R.40` que esta vuelta escribe en la TAREA 2.b usa ese "
            "mismo criterio, que es la unica forma de acatarlo que significa algo."),
    "6.10": ("VA A EJECUTARSE EN LA TAREA 3 DE ESTA VUELTA, EN SU SEGUNDA MITAD, Y AL "
             "ESCRIBIR ESTA LINEA TODAVIA NO HA CORRIDO. El `D.4` era correcto cuando "
             "se declaro y hoy deja de hacer falta: con la 6.1 y la 6.2 la cifra deja "
             "de estar contaminada, asi que la fila 'lecturas dirigidas encargadas y "
             "sin hacer' de `docs/plan/00_INDICE.md` recibe su cifra de hoy por `9.21`, "
             "por adicion, sin tocar la letra vieja y con la atribucion delante. Se "
             "hace DESPUES de la TAREA 2, porque una cifra medida sobre un instrumento "
             "envenenado no se publica."),
    "6.11": ("SE ACATA SIN TOCAR NADA. La `CAIDA 1` del ejecutor de la 171 (los '345 "
             "nodos') queda adjudicada como bien declarada y sin mover ninguna cifra. "
             "Esta vuelta la ha escrito con su nombre en la seccion 8 del reporte de la "
             "171 al cerrarlo, sin suavizarla, y no la reabre."),
    "6.12": ("SE ACATA SIN TOCAR NADA. La correccion al `D.5` de la vuelta 170 "
             "(`REPITE` no aparece en ninguna de las 672 entradas) queda confirmada por "
             "el recomputo del auditor, el hallazgo de fondo se sostiene y la palabra "
             "`FUNDIDA` se queda. Esta vuelta no toca el inventario y no reabre nada: "
             "la cita en el cierre del reporte de la 171 y sigue."),
}
'''

CAIDAS = '''QUE_HACE_CON_LA_CAIDA = {
    "CAIDA 1": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. El auditor aislo la ciega DESPUES de "
                "correr Gate 0, la vara y las siete verificaciones de tarea, cuando la "
                "regla escrita en `aislador_de_ciega.py` dice que el sujeto se aisla "
                "ANTES del primer comando de verificacion. El propio auditor da la "
                "consecuencia entera y acotada: de todos esos comandos solo uno "
                "imprimio el registro completo de un par, y ese par no esta entre los "
                "seis. LO QUE ENSENA, Y ES LO QUE ESTA VUELTA SE LLEVA: una regla de "
                "ORDEN no se cumple midiendo despues si te quemaste."),
    "CAIDA 2": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. Un contador casero del auditor llamo a "
                "una funcion que no existe en `verificar_mutaciones_viejas.py`, se "
                "trago el resultado vacio y dijo 'nomina invisible al censo: 75 "
                "entradas', que habria sido un rojo enorme y falso. No se publico. ES "
                "LA MISMA `P.1` DE SIEMPRE y esta vuelta la aplica: cuando la TAREA 1.a "
                "necesito saber cuantos arneses faltan en la nomina, llamo a la funcion "
                "pura del propio instrumento, `arneses_que_faltan()`, y no escribio un "
                "contador al lado."),
    "CAIDA 3": ("SE REGISTRA CON SU NOMBRE Y NO ACUMULA PARA NINGUNA RACHA DEL "
                "EJECUTOR, porque no es suya. El auditor tecleo de memoria la forma del "
                "fichero de veredictos (`puesto` en vez de `puesto_intra`) y su primer "
                "recomputo del marcador revento. Ninguna cifra salio de ahi. El propio "
                "acta dice que van dos actas seguidas con el mismo vicio, y esta vuelta "
                "lo anota sin comentar de mas: es el vicio que la campana persigue, "
                "mire quien mire."),
}
'''


def main():
    t = io.open(RUTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
    i = t.index("QUE_HACE_ESTA_VUELTA = {")
    j = t.index("QUE_HACE_CON_LA_CAIDA = {")
    k = t.index(NL + "def cuerpo_del_acta():")
    t = t[:i] + QUE_HACE + NL + CAIDAS + t[k:]
    io.open(RUTA, "w", encoding="utf-8", newline=NL).write(t)
    py_compile.compile(RUTA, doraise=True)
    print("GLOSAS SUSTITUIDAS Y COMPILA OK")
    print("CIFRA claves 6.n con glosa: %d" % t.count('    "6.'))
    print("CIFRA claves CAIDA con glosa: %d" % t.count('    "CAIDA '))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
