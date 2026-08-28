# -*- coding: utf-8 -*-
"""vuelta113_tarea2_6_barrido_talladores.py . BARRIDO 2.7 REHECHO ENTERO
(TAREA 2.6 de la vuelta 113, encargo del auditor sobre el acta de la vuelta
112, "TU SEGUNDA ES DE EXPEDIENTE: EL BARRIDO 2.7 DICE 'NINGUNO OMITIDO DE LA
LISTA' Y OMITE").

POR QUE NACE. El barrido de la vuelta 112
(docs/loop/SALIDA_V112_TAREA2_7_BARRIDO_TALLADORES.txt) declaraba tres
busquedas (RE_CITA, el patron de extension entre backticks, y
"LOOP = os.path.join(" en scripts/loop/*.py) pero solo construyo su lista a
mano a partir de las dos primeras: la tercera busqueda, corrida por el
auditor, devuelve 57 ficheros, de los que abrir_tramo_de_opu01.py,
caso_positivo_del_contrato_de_perdidas.py y registrar_cierre_de_tramo.py NO
aparecian nombrados ni descartados en ninguna parte. "Ninguno omitido de la
lista" era una promesa que la propia busqueda desmentia.

QUE HACE, DISTINTO DEL BARRIDO VIEJO: CORRE LAS TRES BUSQUEDAS DE VERDAD (con
re.search sobre el texto de cada scripts/loop/*.py, mismo criterio que grep),
construye la UNION de los tres resultados (no solo el de una), y clasifica
CADA fichero de esa union, sin excepcion, en uno de cuatro grupos, con su
motivo. Ningun fichero se despacha por conteo solo: los 45 historicos
tambien se nombran, uno por uno, para que "45 historicos" dej de ser una
cifra sin lista detras.

GRUPOS:
  A. PARSEA CITAS DE PROSA (RE_CITA, dos formas posibles: nombre pelado o con
     docs/loop/ delante). La unica familia con el boquete que motivo la
     TAREA 2.1/2.7 de la vuelta 112.
  B. VIVOS, NOMBRES FIJOS CONSTRUIDOS POR CODIGO (constante, listdir, glob
     sobre el propio arbol, o argumento de linea de comandos): nunca reciben
     una cita de prosa con dos formas posibles, asi que no pueden tener el
     boquete de la familia A.
  C. HISTORICOS DE UN SOLO USO (nombre con prefijo vuelta<N>_ o _v<N>_):
     instrumentos de una vuelta ya cerrada, mismo mecanismo de nombres fijos
     que B, agrupados aparte solo porque ya no se invocan en el ciclo vivo.
  D. FUERA DE ALCANCE (declarado con su motivo): resuelven algo que NO es una
     cita de fichero contra docs/loop (numero de linea de un acta, o token de
     plantilla contra una raiz que se pasa por argumento).

USO:
  python scripts/loop/vuelta113_tarea2_6_barrido_talladores.py
"""
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP_DIR = os.path.join(RAIZ, "scripts", "loop")

RE_RE_CITA = re.compile(r"RE_CITA")
RE_EXT_PATTERN = re.compile(r"txt\|md")
RE_LOOP_JOIN = re.compile(r"LOOP = os\.path\.join\(")

# TAREA 2.6: clasificacion declarada A MANO, con su motivo, leida del codigo
# de cada fichero (no inferida solo del nombre). El nombre solo decide el
# grupo C (historico) frente a B (vivo); DENTRO de cada grupo la pertenencia
# se verifico leyendo el fichero.
FAMILIA_A = {"tallar_cifras_de_antes.py", "tallar_veredictos_reporte.py"}
FUERA_DE_ALCANCE = {
    "censo_de_plantillas_talladas.py":
        "trae el patron de extension (txt|md) pero para CLASIFICAR tokens "
        "dentro de una plantilla generica; su raiz es --raiz (argumento de "
        "linea de comandos), no LOOP/docs/loop. No es de esta familia.",
}
# los 12 constructores/registradores de acta (RE_CITA casa "lineas **N** a
# **M**", citas de NUMERO DE LINEA dentro de un acta, no nombres de fichero)
ACTA_BUILDERS_MOTIVO = ("RE_CITA casa \"lineas **N** a **M**\" (cita de NUMERO DE "
                        "LINEA dentro de un acta), no un nombre de fichero. "
                        "Instrumento historico de un solo uso, cerrado, sin "
                        "relacion con la familia A.")
for _n in ("_v70_construir_registrador_acta.py", "_v71_construir_registrador_acta.py",
           "_v72_construir_registrador_acta.py", "_v73_construir_registrador_acta.py",
           "_v74_construir_registrador_acta.py", "vuelta68_registrar_acta67.py",
           "vuelta69_registrar_acta68.py", "vuelta70_registrar_acta69.py",
           "vuelta71_registrar_acta70.py", "vuelta72_registrar_acta71.py",
           "vuelta73_registrar_acta72.py", "vuelta74_registrar_acta73.py"):
    FUERA_DE_ALCANCE[_n] = ACTA_BUILDERS_MOTIVO

MOTIVO_VIVO = {
    "abrir_tramo_de_opu01.py": "nombre construido por codigo (V48 = os.path.join(LOOP, "
        "\"RECOMPUTO_V48_COMPONENTES.jsonl\"), linea 83; ruta = os.path.join(LOOP, nombre) "
        "linea 113, nombre viene de una lista/constante interna, no de una cita de prosa).",
    "caso_positivo_de_fusion_de_mesa.py": "rutas de script constantes (GENERADOR/FUNDIDOR, "
        "lineas 59-60) y ruta = os.path.join(LOOP, nombre + \".py\") linea 71, nombre "
        "siempre pelado, construido por codigo.",
    "caso_positivo_del_contrato_de_perdidas.py": "rutas fijas constantes (TMP_PLAN, "
        "TMP_SIN_CAMPO, TRAMO, lineas 57-59), nunca una cita de prosa.",
    "censar_alcance_de_la_vara.py": "reusa FICHEROS_VEREDICTO (lista constante) via import; "
        "ruta = os.path.join(LOOP, nombre) linea 78, nombre siempre pelado.",
    "registrar_cierre_de_tramo.py": "define LOOP (linea 54) pero NO lo usa para resolver "
        "ninguna cita de prosa (cero usos de os.path.join(LOOP, ...) en el resto del "
        "fichero): es un ESCRITOR de rutas construidas por codigo, no un lector de citas.",
    "tallar_cabecera_reporte.py": "leer()/leer_opcional() (lineas 441 y 579) y la ruta del "
        "tsc (linea 682): nombre SIEMPRE construido con \"SALIDA_V%d_...\" por codigo, "
        "nunca parseado de una cita en prosa.",
    "tallar_perdidas_del_plan.py": "rutas.append(os.path.join(LOOP, a.prefijo % (a.vuelta, "
        "L))) linea 143: nombre construido con vuelta/tramo por codigo.",
    "tallar_planes_del_tramo.py": "cand = os.path.join(LOOP, \"%s%s.json\" % (pref, L)) "
        "linea 209: nombre construido con vuelta/tramo por codigo.",
    "verificar_apertura_sellada.py": "glob(SALIDA_V<vuelta>_*_APERTURA.txt) linea 198 sobre "
        "el propio arbol de trabajo, y ruta = os.path.join(LOOP, nombre) linea 264 con "
        "nombre = basename real de ese glob: nunca una cita en prosa.",
    "verificar_cobertura_bolsa_tres_vias.py": "ruta = os.path.join(LOOP, nombre) linea 107, "
        "nombre viene de FICHEROS_VEREDICTO (lista constante, siempre pelada).",
    "verificar_vuelco_de_veredicto.py": "ruta = ... or os.path.join(LOOP, nombre) linea 191, "
        "nombre viene de FICHEROS_VEREDICTO (misma lista constante).",
}


PROPIO_NOMBRE = os.path.basename(os.path.abspath(__file__))


def buscar(patron):
    """Excluye PROPIO_NOMBRE del barrido: este mismo fichero CITA, en su
    docstring y en sus print(), las tres cadenas literales que busca (RE_CITA,
    'txt|md', 'LOOP = os.path.join('), asi que sin esta exclusion se
    envenenaria a si mismo en las tres busquedas (la misma trampa que
    verificar_apertura_sellada.py ya documenta para su propia prueba de
    mutacion: 'LA GUARDA QUE SE ENVENENA SOLA')."""
    hallados = []
    for nombre in sorted(os.listdir(LOOP_DIR)):
        if not nombre.endswith(".py") or nombre == PROPIO_NOMBRE:
            continue
        ruta = os.path.join(LOOP_DIR, nombre)
        with open(ruta, encoding="utf-8", errors="replace") as f:
            texto = f.read()
        if patron.search(texto):
            hallados.append(nombre)
    return hallados


def main():
    lista_re_cita = buscar(RE_RE_CITA)
    lista_ext = buscar(RE_EXT_PATTERN)
    lista_loop = buscar(RE_LOOP_JOIN)

    print("BARRIDO 2.7 REHECHO ENTERO (TAREA 2.6, vuelta 113). Las tres busquedas, corridas de")
    print("verdad, cada una con su recuento; la union se clasifica entera, sin excepcion.")
    print()
    print("1. RE_CITA en scripts/loop/*.py: %d ficheros" % len(lista_re_cita))
    print("2. patron de extension 'txt|md' entre backticks: %d ficheros" % len(lista_ext))
    print("3. 'LOOP = os.path.join(' en scripts/loop/*.py: %d ficheros" % len(lista_loop))
    print()

    union = sorted(set(lista_re_cita) | set(lista_ext) | set(lista_loop))
    print("UNION de las tres busquedas: %d ficheros. Clasificados TODOS, sin excepcion:" % len(union))
    print()

    set_loop = set(lista_loop)
    grupo_a, grupo_b, grupo_c, grupo_d = [], [], [], []
    for nombre in union:
        if nombre in FAMILIA_A:
            grupo_a.append(nombre)
        elif nombre in FUERA_DE_ALCANCE:
            grupo_d.append(nombre)
        elif nombre in set_loop and (nombre.startswith("vuelta") or nombre.startswith("_v")):
            grupo_c.append(nombre)
        elif nombre in set_loop:
            grupo_b.append(nombre)
        else:
            raise SystemExit("ROJO: %s no encaja en ningun grupo, no se clasifica a ciegas" % nombre)

    print("--- GRUPO A: PARSEA CITAS DE PROSA (%d) ---" % len(grupo_a))
    for n in grupo_a:
        extra = " -- EL HERMANO SANO, resuelve las dos formas desde antes" if n == "tallar_veredictos_reporte.py" \
            else " -- corregido en la TAREA 2.1 de la vuelta 112 (resolver_cita, linea 172)"
        print("   %s%s" % (n, extra))
    print()

    print("--- GRUPO B: VIVOS, NOMBRES FIJOS CONSTRUIDOS POR CODIGO (%d) ---" % len(grupo_b))
    for n in grupo_b:
        print("   %s: %s" % (n, MOTIVO_VIVO.get(n, "(motivo pendiente de anotar)")))
    print()

    print("--- GRUPO C: HISTORICOS DE UN SOLO USO, NOMBRES FIJOS (%d) ---" % len(grupo_c))
    for n in grupo_c:
        print("   %s" % n)
    print()

    print("--- GRUPO D: FUERA DE ALCANCE, DECLARADO CON SU MOTIVO (%d) ---" % len(grupo_d))
    for n in grupo_d:
        print("   %s: %s" % (n, FUERA_DE_ALCANCE[n]))
    print()

    total = len(grupo_a) + len(grupo_b) + len(grupo_c) + len(grupo_d)
    print("TOTAL clasificado: %d (A %d + B %d + C %d + D %d) == union %d: %s"
          % (total, len(grupo_a), len(grupo_b), len(grupo_c), len(grupo_d), len(union),
             "CUADRA" if total == len(union) else "NO CUADRA, ROJO"))

    print()
    print("LOS TRES PREVIAMENTE NO NOMBRADOS NI DESCARTADOS (acta 112): abrir_tramo_de_opu01.py,")
    print("caso_positivo_del_contrato_de_perdidas.py y registrar_cierre_de_tramo.py -- los tres")
    print("estan ahora en GRUPO B, arriba, con su linea.")

    return 0 if total == len(union) else 1


if __name__ == "__main__":
    raise SystemExit(main())
