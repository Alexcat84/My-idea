# -*- coding: utf-8 -*-
"""vuelta156_tarea8_cifras_derivadas.py . TAREA 8 DE LA VUELTA 156, APOYO.

POR QUE EXISTE. `verificar_cifras_del_reporte.py` exige que toda cifra del
reporte con una unidad del vocabulario cerrado se pueda COTEJAR contra una linea
`CIFRA <etiqueta>: <n> <unidad>` del fichero que la cifra cita. Tres cifras que
este reporte publica viven en salidas que NO imprimen linea `CIFRA`, porque son
salidas de guardas que no la escriben:

  - la linea del check de `OP-C-05` de Gate 0, que dice cuantos pares tienen cita
    y cuantos quedan fuera de la vara por fuente deprecada;
  - la linea VERDE de `verificar_apertura_sellada.py`, que dice cuantos ficheros
    de apertura nombra;
  - la linea VERDE de `verificar_cifras_del_plan.py`, que dice cuantos pares
    examino.

QUE HACE ESTE INSTRUMENTO, Y LO QUE NO HACE. NO recomputa nada y NO inventa
nada: LEE LAS SALIDAS SELLADAS DE ESTA VUELTA, CUENTA SOBRE ELLAS y publica las
lineas `CIFRA` que faltaban, citando literalmente la linea de la que sale cada
una. Es la letra de EJECUTOR.md 1: "toda tabla o cifra del reporte cita el
fichero de salida del que sale, y se reconstruye CONTANDO ESE FICHERO antes de
publicarla".

SI UNA LINEA NO ESTA, CAE EN ROJO. No hay camino por el que este fichero
publique una cifra que no haya leido.

USO:  python scripts/loop/vuelta156_tarea8_cifras_derivadas.py
"""
import io
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")


def linea_con(fichero, trozo):
    ruta = os.path.join(LOOP, fichero)
    if not os.path.exists(ruta):
        raise SystemExit("ROJO: no existe docs/loop/%s" % fichero)
    for linea in io.open(ruta, encoding="utf-8", errors="replace"):
        if trozo in linea:
            return linea.rstrip()
    raise SystemExit("ROJO: docs/loop/%s no trae ninguna linea con %r" % (fichero, trozo))


def main():
    print("=" * 100)
    print("VUELTA 156, TAREA 8 (APOYO): LAS CIFRAS QUE SUS GUARDAS NO PUBLICAN COMO `CIFRA`,")
    print("CONTADAS DE LAS SALIDAS SELLADAS DE ESTA VUELTA")
    print("=" * 100)
    print("")

    # ---------------------------------------------------------------- OP-C-05
    f1 = "SALIDA_V156_T1B_CICLO_Y_GUARDA.txt"
    l1 = linea_con(f1, "OP-C-05: todo par bidireccional")
    print("FUENTE 1: docs/loop/%s" % f1)
    print("LINEA LEIDA, LITERAL:")
    print("   %s" % l1)
    m_con = re.search(r"(\d+) par\(es\) bidireccional\(es\) tras resolver, (\d+) con cita, "
                      r"(\d+) SIN CITA", l1)
    if not m_con:
        raise SystemExit("ROJO: la linea de OP-C-05 no tiene la forma esperada")
    total, con, sin = (int(x) for x in m_con.groups())
    m_fuera = re.search(r"camino A: (\d+) par\(es\) mas", l1)
    if not m_fuera:
        raise SystemExit("ROJO: la linea de OP-C-05 no publica el hueco de fuente deprecada")
    fuera = int(m_fuera.group(1))
    nombrados = re.findall(r"'([a-z0-9_]+ <-> [a-z0-9_]+)'", l1)
    print("")
    print("   comprobado contando la propia linea: los pares nombrados uno a uno son %d"
          % len(nombrados))
    for x in nombrados:
        print("      %s" % x)
    if len(nombrados) != fuera:
        raise SystemExit("ROJO: la linea dice %d fuera de la vara y nombra %d"
                         % (fuera, len(nombrados)))
    print("")
    print("CIFRA pares bidireccionales CITADOS: %d par(es)" % con)
    print("CIFRA pares bidireccionales HUERFANOS: %d par(es)" % sin)
    print("CIFRA pares EXCLUIDOS por declarante deprecado: %d par(es)" % fuera)
    print("CIFRA pares del universo ENSANCHADO: %d par(es)"
          % (total + fuera))
    print("")

    # ------------------------------------------------- guardas del cierre
    f2 = "SALIDA_V156_T9_GUARDAS_CIERRE.txt"
    l2 = linea_con(f2, "VERDE: los 10 ficheros")
    l3 = linea_con(f2, "ROJO, apertura de la vuelta 100")
    l4 = linea_con(f2, "VERDE EXIT 0:")
    print("FUENTE 2: docs/loop/%s" % f2)
    print("LINEAS LEIDAS, LITERALES:")
    print("   %s" % l2)
    print("   %s" % l3)
    print("   %s" % l4)
    nacidos = 0
    for linea in io.open(os.path.join(LOOP, f2), encoding="utf-8", errors="replace"):
        if " -- nacido en " in linea:
            nacidos += 1
    m2 = re.search(r"los (\d+) ficheros", l2)
    if not m2 or int(m2.group(1)) != nacidos:
        raise SystemExit("ROJO: la guarda dice %s ficheros y el fichero lista %d"
                         % (m2.group(1) if m2 else "?", nacidos))
    m4 = re.search(r"VERDE EXIT 0: (\d+) pares", l4)
    if not m4:
        raise SystemExit("ROJO: la guarda del plan no publica su numero de pares")
    print("")
    print("   comprobado contando el fichero: lineas ' -- nacido en ' = %d" % nacidos)
    print("")
    print("CIFRA ficheros de apertura sellados de la vuelta 156: %d fichero(s)" % nacidos)
    print("CIFRA pares examinados por la guarda de cifras del plan: %d par(es)"
          % int(m4.group(1)))
    # ------------------------------------------------- la tabla por fase
    f3 = "SALIDA_V156_T9_TABLA_POR_FASE.txt"
    l5 = linea_con(f3, "CIFRA filas de la tabla por fase en VERDE:")
    l6 = linea_con(f3, "CIFRA filas de la tabla por fase en VERDE PARCIAL:")
    l7 = linea_con(f3, "CIFRA filas de la tabla por fase en NO CUMPLE:")
    print("FUENTE 3: docs/loop/%s" % f3)
    print("LINEAS LEIDAS, LITERALES:")
    for x in (l5, l6, l7):
        print("   %s" % x)
    def _n(linea):
        m = re.search(r": (\d+) filas", linea)
        if not m:
            raise SystemExit("ROJO: no se pudo leer el numero de %r" % linea)
        return int(m.group(1))
    v, vp, nc = _n(l5), _n(l6), _n(l7)
    print("")
    print("   LAS ETIQUETAS SE REESCRIBEN AQUI PARA QUE SEAN DISTINGUIBLES, y se dice")
    print("   por que: 'en VERDE' y 'en VERDE PARCIAL' comparten todas sus palabras")
    print("   utiles, asi que la guarda del reporte no puede saber de cual se habla.")
    print("   Los numeros son los mismos; lo unico que cambia es el rotulo.")
    print("")
    print("CIFRA filas de la tabla por fase ENTERAS: %d fila(s)" % v)
    print("CIFRA filas de la tabla por fase A MEDIAS: %d fila(s)" % vp)
    print("CIFRA filas de la tabla por fase INCUMPLIDAS: %d fila(s)" % nc)
    print("")
    print("=" * 100)
    print("NINGUNA DE ESTAS CIFRAS SE TECLEA: las seis salen de las cuatro lineas literales")
    print("de arriba, y las dos que se pueden contar aparte (los pares nombrados y las")
    print("lineas de nacimiento) se cuentan y se exige que cuadren, o esto cae en ROJO.")
    print("=" * 100)
    return 0


raise SystemExit(main())
