# -*- coding: utf-8 -*-
"""vuelta159_tarea7b_marcar_las_dos_citas.py . TAREA 7 DE LA VUELTA 159, LA
MARCA.

DEJA ESCRITO JUNTO A LA FUNCION DE LA P3b EL VEREDICTO QUE LA BUSQUEDA EN LA
HISTORIA DEVOLVIO (adjudicacion 6.9 del acta 158). La 6.9 dice: "si aparece, se
nombra el productor y la ficha lo cita; si no aparece, la cita queda declarada
ARTEFACTO HUERFANO junto a la funcion". APARECIERON LOS DOS, asi que lo que se
escribe es el nombre de cada productor y por que ningun barrido anterior podia
hallarlo.

POR ADICION, como comentario inmediatamente debajo del docstring de
`p3b_caso_positivo` y DETRAS de los bloques que otras vueltas ya dejaron ahi.
Nada se borra. La aditividad se mide con `git diff --numstat` y se exige
BORRADOS 0.

ES IDEMPOTENTE por marca literal.

USO:  python scripts/loop/vuelta159_tarea7b_marcar_las_dos_citas.py
"""
import io
import os
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P3B = "scripts/loop/vuelta150_3_relectura_expediente.py"

MARCA = "VEREDICTO DE LA 6.9, VUELTA 159"

BLOQUE = """    # --- %s: LAS DOS SALIDAS SIN PRODUCTOR NO ERAN HUERFANAS. LOS
    # DOS PRODUCTORES ESTAN VIVOS, Y NINGUN BARRIDO ANTERIOR PODIA HALLARLOS ---
    #
    # REGISTRO POR ADICION. Nada de lo de arriba se borra ni se suaviza.
    #
    # LO QUE SE MIDIO (instrumento
    # `scripts/loop/vuelta159_tarea7_productores_en_la_historia.py`, salida
    # `docs/loop/SALIDA_V159_T7_PRODUCTORES.txt`, cuatro angulos corridos):
    #
    #   SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt lo produce
    #      scripts/loop/verificar_cobertura_bolsa_tres_vias.py
    #      (5 de 5 lineas casables salen de sus print)
    #   SALIDA_V136_3D_MUTACION.txt lo produce
    #      scripts/loop/verificar_fuente_canonico.py
    #      (1 de 1 linea casable sale de su print, la de AUTOPRUEBA VERIFICADA)
    #
    # POR QUE NINGUN BARRIDO ANTERIOR LOS ENCONTRO, Y ES LA PARTE UTIL: LOS DOS
    # PRODUCTORES IMPRIMEN POR STDOUT Y EL .txt ES UNA REDIRECCION DE SHELL. Por
    # eso ningun `.py` contiene el NOMBRE del fichero, que es lo que el barrido
    # de 998 `.py` de la vuelta 157 buscaba, y por eso tampoco contiene su TEXTO
    # LITERAL: en el fuente ese texto va CON MARCADORES DE FORMATO
    # ("FICHEROS DE ENTRADA (declarados en FICHEROS_VEREDICTO, %%d):"), asi que
    # buscar la linea YA INTERPOLADA no puede casar nunca. El angulo que si caza
    # es el de la CABECERA LITERAL: probar prefijos cada vez mas cortos hasta que
    # uno case.
    #
    # LA LECCION PARA ESTA FUNCION, QUE ES LO QUE JUSTIFICA ESCRIBIRLO AQUI: la
    # P3b se sostiene en que la salida citada EXISTA al corte, y eso sigue igual.
    # Lo que cambia es que ahora las dos citas tienen productor nombrado y la
    # ficha puede citarlo. NINGUNA DE LAS DOS ES ARTEFACTO HUERFANO.
    #
    # Y LA CAIDA PROPIA, DECLARADA: la PRIMERA corrida de aquel instrumento, con
    # solo tres angulos, publico las dos como ARTEFACTO HUERFANO. Era falso, y
    # lo era por defecto del instrumento. Queda escrito para que no se lea la
    # cifra buena sin la mala.
""" % MARCA


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def numstat(ruta_rel):
    r = subprocess.run(["git", "diff", "--numstat", "--", ruta_rel],
                       cwd=RAIZ, capture_output=True)
    linea = r.stdout.decode("utf-8", "replace").strip()
    if not linea:
        return 0, 0
    c = linea.split("\t")
    return int(c[0]), int(c[1])


def main():
    print("=" * 78)
    print("VUELTA 159, TAREA 7: LA MARCA JUNTO A LA FUNCION DE LA P3b")
    print("=" * 78)
    print("")
    ruta = os.path.join(RAIZ, P3B)
    texto = leer(ruta)
    if MARCA in texto:
        print("   YA ESTABA: la marca literal %r ya vive en %s" % (MARCA, P3B))
    else:
        i = texto.index("def p3b_caso_positivo(")
        ini = texto.index('"""', i)
        fin = texto.index('"""', ini + 3) + 3
        salto = texto.index("\n", fin) + 1
        while True:
            fl = texto.find("\n", salto)
            if fl < 0:
                break
            linea = texto[salto:fl]
            if linea.strip() == "" or linea.lstrip().startswith("#"):
                salto = fl + 1
                continue
            break
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(texto[:salto] + BLOQUE + texto[salto:])
        print("   ANADIDO: %d lineas al final de los comentarios de p3b_caso_positivo"
              % len(BLOQUE.splitlines()))
    print("")
    mas, menos = numstat(P3B)
    print("   ADITIVIDAD MEDIDA, git diff --numstat -- %s" % P3B)
    print("   CIFRA lineas anadidas: %d" % mas)
    print("   CIFRA lineas borradas: %d" % menos)
    assert menos == 0, "SE BORRO UNA LINEA: la aditividad esta rota"
    print("   CERO BORRADOS.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
