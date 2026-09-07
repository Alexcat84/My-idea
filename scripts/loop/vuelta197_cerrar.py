# -*- coding: utf-8 -*-
r"""vuelta197_cerrar.py . LA LLAMADA A cerrar_reporte.py DE LA VUELTA 197, CON SUS
CUATRO PIEZAS Y SU ATRIBUCION DE HUECO EN UN SOLO SITIO.

EXISTE PARA QUE LA ORDEN NO SE TECLEE EN UNA TERMINAL Y SE PIERDA: la atribucion
del hueco es un texto largo con cifras dentro, y una cifra que se teclea en una
linea de comandos no queda en ningun sitio que se pueda auditar.

Y AQUI ES DONDE LA TAREA 4.a SE VE EN EL REPORTE: la frase del censo y la nomina
va CON SU VARA Y CON LAS DOS CIFRAS, que es lo que la adjudicacion `4.7` del acta
197 encarga.

USO:
  python scripts/loop/vuelta197_cerrar.py
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PY = sys.executable

VEREDICTO = (
    "LAS CUATRO TAREAS CERRADAS: R.59 escrita con siete lectores nuevos que "
    "salvan seis paradas, el orden del turno del auditor ya es codigo con 49 de "
    "49 en verde, 207 de 224 en la mitad limpia de una ciega de 240 que vuelve a "
    "doblar el tramo por once discrepancias fuera de un marcado que no existe "
    "por debajo del 2662, y las dos cifras sin vara ya viajan con la suya, con el "
    "tope del austero medido por tres varas y 5.1 veces por encima."
)

ATRIBUCION = (
    "NADIE la corrio, y NO tocaba: por AUDITOR.md 6.1, decision del fundador del "
    "5 sep 2026, la bateria de mutaciones corre CADA CINCO VUELTAS en una vuelta "
    "propia que NO LLEVA NADA MAS. La 194 la corrio ENTERA por sus DIEZ tramos y "
    "por esa cadencia LA SIGUIENTE VUELTA DE BATERIA ES LA 199. Esta vuelta NO es "
    "de bateria: su encargo se lo dice con esas palabras en su cuarta linea, su "
    "sello de apertura lo escribe en el bloque I y ese mismo bloque mide CERO "
    "ficheros SALIDA_V197_BATERIA_TRAMO_N.txt en disco al entrar, sobre 38 "
    "selladas de bateria que si hay en docs/loop/ repartidas entre las vueltas "
    "176, 183, 189 y 194. El fichero docs/loop/SALIDA_V197_BATERIA.txt NO "
    "EXISTE y por eso mide cero, y esa medicion va aqui CON SU NOMBRE en vez de "
    "callarse: un hueco declarado no es un hueco escondido. "
    "Y LO QUE ESTA VUELTA SI MIDIO DEL RADIO DE LA BATERIA, sin correrla, Y "
    "AHORA CON SU VARA AL LADO, que es la TAREA 4.a y la adjudicacion 4.7 del "
    "acta 197: la nomina de verificar_mutaciones_viejas.py entra y sale en 135 "
    "entradas con CASOS_DECLARADOS en 2; el censo reconoce 195 arneses; LA VARA "
    "DEL CENSO VALE 148 y decide, y CON ESA VARA hay 0 arneses del censo fuera "
    "de la nomina, pero SIN VARA hay 60, y las dos cifras se publican juntas "
    "porque un 0 solo al lado de un censo de 195 y una nomina de 135 se lee como "
    "cobertura total del censo y es cobertura desde la vara para arriba; hay "
    "ademas 0 entradas invisibles al censo y 0 entradas sin sujeto congelado. "
    "Todo leido del instrumento en el bloque F del sello de apertura, que ahora "
    "mide LAS DOS y lista los diez primeros de los 60. NO SE PODO NI UNA ENTRADA. "
    "Y UNA COSA MAS QUE ESTA VUELTA MIDIO Y NO REPARO, porque no esta encargada: "
    "de 5 arneses de la nomina que tocan apertura_del_auditor.py, 1 BORRA la sede "
    "del turno del auditor cada vez que corre, medido con una corrida en "
    "SALIDA_V197_T2_QUIEN_BORRA_LA_SEDE.txt y preguntado en la seccion 6."
)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    cmd = [PY, "scripts/loop/cerrar_reporte.py",
           "--vuelta", "197",
           "--cuerpo", "scripts/loop/_v197_cierre_texto.md",
           "--tallador", "docs/loop/SALIDA_V197_TALLADOR_CABECERA.txt",
           "--bateria", "docs/loop/SALIDA_V197_BATERIA.txt",
           "--veredicto", VEREDICTO,
           "--hueco-atribucion", ATRIBUCION]
    r = subprocess.run(cmd, cwd=RAIZ, env=env)
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
