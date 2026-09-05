# -*- coding: utf-8 -*-
r"""_auditor_v178_ciega.py . AISLA EL SUJETO DE LA CIEGA DE LA AUDITORIA 178
USANDO LAS FUNCIONES PURAS DE `aislador_de_ciega.py`, NO UNA COPIA DE ELLAS.

POR QUE EXISTE Y NO USO EL LANZADOR TAL CUAL: el aislador elige por dominio,
clase, banda, rango o muestra, y NO POR LISTA DE PUESTOS. Los discutibles
marcados del reporte de la 177 (D.1, D.7 y los cinco triangulos de la seccion
2.f) apuntan a DOCE puestos sueltos y dispersos, de 334 a 1374. Un rango
`--desde 334 --hasta 1374` traeria mil pares y no seria el sujeto marcado.

QUE CONSERVO ENTERO, que es lo que importa: la LISTA BLANCA `CAMPOS_CIEGOS`,
el constructor `texto_ciego`, el `texto_destape` y sobre todo la GUARDA DE
FUGA `fugas()`. Si el destape se cuela, no escribo ninguno de los dos.

El `--excluir`/`--puestos` que le falta al lanzador ya esta contado como
pendiente en la 1.g del reporte de la 177. Esto no lo sustituye.
"""
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aislador_de_ciega as A

# LOS DOCE DEL AREA MARCADA: todos los puestos que la TAREA 2 del reporte 177
# cita como lados de sus formas y de sus cinco triangulos.
MARCADOS = [334, 394, 404, 451, 460, 530, 787, 863, 878, 1030, 1121, 1374]
# Y CUATRO DE FUERA DEL MARCADO, por muestra con semilla, para que la regla del
# credito (una discrepancia FUERA del marcado baja el credito de la tanda)
# tenga donde morder. Semilla 178.
FUERA = 4

def main():
    sys.stdout.reconfigure(encoding="utf-8")
    criterio = ("los 12 puestos que la TAREA 2 del reporte 177 cita como lados "
                "de sus tres formas y sus cinco triangulos (334 394 404 451 460 "
                "530 787 863 878 1030 1121 1374), mas 4 pares de FUERA del "
                "marcado por muestra con semilla 178")
    filas = A.cargar_filas()
    print("CIFRA filas del archivo: %d" % len(filas))
    porp = dict((f.get("puesto_intra"), f) for f in filas)
    sel = [porp[p] for p in MARCADOS if p in porp]
    faltan = [p for p in MARCADOS if p not in porp]
    print("CIFRA marcados encontrados: %d de %d" % (len(sel), len(MARCADOS)))
    if faltan:
        print("   puestos marcados que NO estan en el archivo: %s" % faltan)
    resto = [f for f in filas if f.get("puesto_intra") not in set(MARCADOS)]
    import random
    fuera = sorted(random.Random(178).sample(resto, FUERA),
                   key=lambda f: f.get("puesto_intra", 0))
    print("CIFRA de fuera del marcado: %d -> puestos %s"
          % (len(fuera), [f.get("puesto_intra") for f in fuera]))
    todos = sorted(sel + fuera, key=lambda f: f.get("puesto_intra", 0))
    print("CIFRA pares elegidos: %d" % len(todos))
    pasos = A.cargar_pasos()
    ciego = A.texto_ciego(todos, pasos, criterio)
    destape = A.texto_destape(todos, criterio)
    esc = A.fugas(ciego, todos)
    print("CIFRA fugas del destape en la salida ciega: %d" % len(esc))
    if esc:
        print("ROJO: el destape se cuela. No escribo nada.")
        for p, c in esc:
            print("   puesto %s campo %s" % (p, c))
        return 1
    io.open("docs/loop/_auditor_v178_ciega.txt", "w", encoding="utf-8", newline="\n").write(ciego)
    io.open("docs/loop/_auditor_v178_destape.txt", "w", encoding="utf-8", newline="\n").write(destape)
    print("VERDE. ciega %d bytes, destape %d bytes (NO ABRIR)"
          % (len(ciego.encode("utf-8")), len(destape.encode("utf-8"))))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
