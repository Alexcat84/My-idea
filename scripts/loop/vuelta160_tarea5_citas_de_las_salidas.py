# -*- coding: utf-8 -*-
"""vuelta160_tarea5_citas_de_las_salidas.py . TAREA 5 DE LA VUELTA 160.

RECOMPUTA LAS CUATRO CITAS DE LAS DOS SALIDAS ANTES DE ESCRIBIR NADA, que es lo
que el encargo manda con esta letra: SI NO TE DAN CUATRO, PARAS Y LO DICES.

QUE SE RECOMPUTA. La adjudicacion 6.6 del acta 159 dice que las fichas de
`SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt` y de `SALIDA_V136_3D_MUTACION.txt` NO
se reescriben, porque las CUATRO citas que las nombran YA nombran a su productor.
El auditor lo midio en `docs/loop/_auditor_v159_productores.txt` y aqui se
recomputa con instrumento propio y sin creerle la cifra.

LA VARA DE LA CITA, DECLARADA ANTES DE CONTAR: una CITA es una linea de
`docs/plan/` o de `docs/PENDIENTES.md` que nombre el fichero de salida. Y una
cita NOMBRA A SU PRODUCTOR si el nombre del `.py` que la produce aparece EN LA
MISMA LINEA o en la VECINDAD DE DOS LINEAS a cada lado, que es la vara del
auditor y el motivo esta escrito en su acta: en `docs/PENDIENTES.md` el nombre
del productor esta dos lineas mas arriba dentro del MISMO PARENTESIS, partido
por el ancho de columna. LA VECINDAD SE PUBLICA JUNTO A CADA CITA para que se
pueda ver que no se estiro para que saliera.

LOS DOS PARES SALIDA-PRODUCTOR, que no se teclean como resultado sino como
SUJETO de la busqueda:
    SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt  <-  verificar_cobertura_bolsa_tres_vias.py
    SALIDA_V136_3D_MUTACION.txt             <-  verificar_fuente_canonico.py

Y LA LECCION QUE ESTA TAREA DEJA ESCRITA, que es lo unico que la 6.6 manda
anadir: EL ANGULO BARATO ERA LEER LA FICHA QUE CITA LA SALIDA. Ni el barrido de
998 `.py` de la vuelta 157 ni los cuatro angulos de la vuelta 159 lo miraron, y
el productor llevaba meses escrito al lado. Esa leccion la escribio la TAREA 1
de esta vuelta junto a la funcion de la P3b, dentro del bloque de la 6.6; ESTE
INSTRUMENTO ES LA MEDICION QUE LA SOSTIENE, y si la medicion no diera cuatro,
la TAREA 1 habria escrito una cifra falsa y ESO ES LO QUE ESTE FICHERO PARA.

UNA COSA QUE SE DECLARA EN VEZ DE CALLARSE, SOBRE EL ORDEN: el encargo manda la
TAREA 1 primero y manda recomputar ANTES de escribir. Las dos cosas no caben a
la vez, porque el bloque de la 6.6 va dentro de la TAREA 1. Se resolvio
escribiendo el bloque en la TAREA 1 y CORRIENDO ESTA MEDICION DESPUES, con la
regla de que si no da cuatro se para y se revierte el bloque. Da cuatro o no da:
lo que se publica es lo que salga.

USO:  python scripts/loop/vuelta160_tarea5_citas_de_las_salidas.py
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PARES = (
    ("SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt", "verificar_cobertura_bolsa_tres_vias.py"),
    ("SALIDA_V136_3D_MUTACION.txt", "verificar_fuente_canonico.py"),
)

VECINDAD = 2


def ficheros_a_barrer():
    """docs/plan/ entero mas docs/PENDIENTES.md, que son las dos sedes que la
    5.1 del acta 159 nombra."""
    rutas = []
    base = os.path.join(RAIZ, "docs", "plan")
    for raiz, dirs, ficheros in os.walk(base):
        dirs.sort()
        for f in sorted(ficheros):
            rutas.append(os.path.join(raiz, f))
    rutas.append(os.path.join(RAIZ, "docs", "PENDIENTES.md"))
    return rutas


def main():
    print("=" * 78)
    print("VUELTA 160, TAREA 5: LAS CUATRO CITAS DE LAS DOS SALIDAS, RECOMPUTADAS")
    print("=" * 78)
    print("")
    print("VARA DECLARADA ANTES DE CONTAR: cita = linea de docs/plan/ o de")
    print("docs/PENDIENTES.md que nombre el fichero de salida. NOMBRA A SU")
    print("PRODUCTOR si el .py aparece en la MISMA linea o en la vecindad de %d"
          % VECINDAD)
    print("lineas a cada lado. La vecindad se imprime junto a cada cita.")
    print("")

    rutas = ficheros_a_barrer()
    print("CIFRA ficheros barridos: %d" % len(rutas))
    print("")

    total = 0
    con_productor = 0
    sin_productor = []
    for salida, productor in PARES:
        print("-" * 78)
        print("SALIDA: %s" % salida)
        print("PRODUCTOR BUSCADO: %s" % productor)
        print("-" * 78)
        n_salida = 0
        for ruta in rutas:
            try:
                lineas = io.open(ruta, encoding="utf-8").read().splitlines()
            except (IOError, UnicodeDecodeError):
                continue
            for i, linea in enumerate(lineas):
                if salida not in linea:
                    continue
                n_salida += 1
                total += 1
                rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
                ini = max(0, i - VECINDAD)
                fin = min(len(lineas), i + VECINDAD + 1)
                ventana = "\n".join(lineas[ini:fin])
                en_linea = productor in linea
                en_ventana = productor in ventana
                if en_ventana:
                    con_productor += 1
                else:
                    sin_productor.append((rel, i + 1, salida))
                donde = ("EN LA MISMA LINEA" if en_linea
                         else ("EN LA VECINDAD" if en_ventana else "NO APARECE"))
                print("")
                print("   CITA %s:%d   productor %s" % (rel, i + 1, donde))
                for j in range(ini, fin):
                    marca = ">>" if j == i else "  "
                    print("      %s %5d | %s" % (marca, j + 1, lineas[j][:150]))
        print("")
        print("   CIFRA citas de %s: %d" % (salida, n_salida))
        print("")

    print("=" * 78)
    print("CIFRA citas halladas en total: %d" % total)
    print("CIFRA de ellas que NOMBRAN a su productor: %d" % con_productor)
    print("CIFRA de ellas SIN productor a la vista: %d" % len(sin_productor))
    for rel, n, salida in sin_productor:
        print("   %s:%d (%s)" % (rel, n, salida))
    print("CIFRA que el acta 159 declara en su 5.1: 4 citas, las 4 con productor")
    print("CIFRA fichas que hay que reescribir: %d" % len(sin_productor))
    print("")

    if total != 4:
        print("PARADA, POR MANDATO LITERAL DEL ENCARGO: la cuenta no da cuatro, da")
        print("%d. NO se escribe la leccion y el bloque de la 6.6 que la TAREA 1" % total)
        print("dejo escrito QUEDA EN FALSO y hay que revertirlo.")
        print("FIN")
        return 1
    if sin_productor:
        print("PARADA: las cuatro estan, pero alguna NO nombra a su productor, y")
        print("la 6.6 se adjudico sobre que las cuatro lo nombran.")
        print("FIN")
        return 1
    print("REPRODUCE AL DIGITO: CUATRO CITAS Y LAS CUATRO NOMBRAN A SU PRODUCTOR.")
    print("La 6.6 se sostiene: LAS FICHAS NO SE REESCRIBEN, cifra 0, y lo que va")
    print("escrito junto a la funcion de la P3b es solo la leccion del angulo")
    print("barato, que la TAREA 1 ya dejo puesta por adicion.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
