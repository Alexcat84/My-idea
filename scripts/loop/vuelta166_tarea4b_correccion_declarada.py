# -*- coding: utf-8 -*-
r"""vuelta166_tarea4b_correccion_declarada.py . TAREA 4 de la vuelta 166,
segunda mitad: LA CORRECCION DECLARADA DE LA CIFRA FALSA, ESCRITA DONDE LA
CIFRA VIAJO.

QUE CORRIGE. El acta 164, adjudicacion 6.10, publico *"de las 71 operaciones,
67 estan en HECHA y CUATRO en LISTA"* y de ahi dibujo el mapa del ultimo tramo
de la fase III. Esa cifra viajo a `docs/PENDIENTES.md` dentro de la entrada
`R.34`, en la glosa que dice *"la unica de las cuatro en LISTA sin dependencias
declaradas"*. LA LINEA SE LOCALIZA MIDIENDO EL FICHERO, no se teclea.

COMO CORRIGE, Y ES LA REGLA Y NO UNA PREFERENCIA (`EJECUTOR.md` 8): **NO SE
BORRA NI UNA LETRA de `R.34`.** La correccion entra POR ADICION, con la linea
vieja CITADA entera y la cifra de hoy al lado.

LA TABLA NO SE TECLEA (`EJECUTOR.md` 1, "LA TABLA SE CUENTA DE SU FICHERO"): se
LEE del fichero de salida `docs/loop/SALIDA_V166_T4_CENSO_OPERACIONES.txt`, que
es el que el censo produjo, y se pega entera. Si ese fichero no existe o su
tabla no se puede leer, este instrumento PARA y no escribe nada.

IDEMPOTENTE: si el bloque ya esta, no escribe.

USO:
  python scripts/loop/vuelta166_tarea4b_correccion_declarada.py            (mide, NO escribe)
  python scripts/loop/vuelta166_tarea4b_correccion_declarada.py --aplicar  (mide y escribe)
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V166_T4_CENSO_OPERACIONES.txt")

MARCA = "**CORRECCION DECLARADA DE LA CIFRA DE OPERACIONES (4 sep 2026, vuelta 166"
AGUJA = "la unica de las cuatro en `LISTA` sin dependencias declaradas"


def tabla_del_fichero():
    """LA TABLA SE CUENTA DE SU FICHERO. Devuelve (filas, total, resumen) o None."""
    if not os.path.exists(SALIDA):
        return None
    texto = io.open(SALIDA, encoding="utf-8").read()
    filas = re.findall(r"^   (\d\d_[A-Z_]+)\s+\| (\d+)\s+\| (\d+)\s+\| (\d+)$",
                       texto, re.M)
    total = re.search(r"^   TOTAL\s+\| (\d+)\s+\| (\d+)\s+\| (\d+)$", texto, re.M)
    resumen = {}
    for clave, patron in (
            ("operaciones", r"^   CIFRA operaciones: (\d+)$"),
            ("hecha", r"^   CIFRA HECHA: (\d+)$"),
            ("lista", r"^   CIFRA LISTA: (\d+)$"),
            ("sin_dep", r"^   CIFRA no HECHA sin dependencias declaradas: (\d+)$"),
            ("libres", r"^   CIFRA no HECHA con todas sus dependencias en HECHA: (\d+)$"),
            ("fases", r"^   CIFRA fases: (\d+)$")):
        m = re.search(patron, texto, re.M)
        if not m:
            return None
        resumen[clave] = int(m.group(1))
    sin_dep = re.findall(r"^      (OP-[A-Z0-9-]+)\s+(\d\d_[A-Z_]+)\s+LISTA", texto, re.M)
    if not filas or not total:
        return None
    return filas, total.groups(), resumen, sin_dep


def bloque(filas, total, resumen, sin_dep, n_aguja, linea_aguja):
    tabla = ["| fase | `HECHA` | `LISTA` | total |", "|---|---:|---:|---:|"]
    for f, h, l, t in filas:
        tabla.append("| `%s` | %s | %s | %s |" % (f, h, l, t))
    tabla.append("| **TOTAL** | **%s** | **%s** | **%s** |" % total)
    nombres = ", ".join("`%s`" % o for o, _f in sin_dep)
    return (
        "\n"
        "%s, TAREA 4; adjudicacion 5.13 del acta 165 y su caida 1).**\n"
        "**QUE SE CORRIGE Y DONDE VIAJO.** El acta 164, adjudicacion 6.10, publico\n"
        "*\"de las 71 operaciones, 67 estan en `HECHA` y CUATRO en `LISTA`\"* y con esa\n"
        "cifra dibujo el mapa del ultimo tramo de la fase III. **Esa cifra viajo a este\n"
        "mismo fichero**, dentro de la entrada `R.34`, en la linea **%d**, que dice hoy,\n"
        "citada entera y sin recortar:\n"
        "\n"
        "> *\"%s\"*\n"
        "\n"
        "**NO SE BORRA NI UNA LETRA DE `R.34`** (`EJECUTOR.md` 8: una correccion que tapa\n"
        "lo que corrige no se puede auditar). La entrada vieja se queda entera con su\n"
        "cifra; **lo que manda desde aqui es la medicion de hoy.**\n"
        "\n"
        "**LA CIFRA DE HOY, MEDIDA POR EL EJECUTOR CON INSTRUMENTO PROPIO** sobre\n"
        "`docs/plan/OPERACIONES.jsonl` (`python scripts/loop/vuelta166_tarea4_censo_operaciones.py`,\n"
        "salida en [`loop/SALIDA_V166_T4_CENSO_OPERACIONES.txt`](loop/SALIDA_V166_T4_CENSO_OPERACIONES.txt)),\n"
        "**corte 4 sep 2026**: **%d operaciones, %d en `HECHA` y %d en `LISTA`.**\n"
        "**LA TABLA NO ESTA TECLEADA: se lee de ese fichero de salida y se pega entera.**\n"
        "\n"
        "%s\n"
        "\n"
        "**Y NO ES DERIVA DEL TIEMPO, Y ESO TAMBIEN SE MIDE EN VEZ DE HEREDARSE:** el\n"
        "mismo conteo corrido sobre el arbol del propio acta 164 (`git show\n"
        "2c00a1c0:docs/plan/OPERACIONES.jsonl`) da **las mismas %d y %d**. La cifra del\n"
        "acta 164 **ya era falsa el dia que se escribio.**\n"
        "\n"
        "**LA SEGUNDA MITAD DE LA MISMA CAIDA, CORREGIDA EN EL MISMO ACTO.** La glosa\n"
        "citada arriba llama a `OP-L-01` *\"la unica de las cuatro en `LISTA` sin\n"
        "dependencias declaradas\"*. **Medido hoy: de las %d que no estan en `HECHA`, %d\n"
        "no tienen dependencias declaradas, no una.** Van **NOMBRADAS Y NO RESUMIDAS**,\n"
        "que es como se publica una poblacion: %s. Y de las %d que si las tienen, **%d\n"
        "tienen TODAS sus dependencias en `HECHA` hoy**, contado y no adjudicado: decidir\n"
        "si una operacion *puede correr* es una lectura, no un conteo.\n"
        "\n"
        "**LO QUE ESTA CORRECCION NO HACE, dicho antes de que se lea como hecho:**\n"
        "**ningun estado se cambia** (la TAREA 4 es un censo, no un pase), ninguna\n"
        "operacion se abre ni se cierra, y **no se vuelve a dibujar cual es el ultimo\n"
        "tramo de la fase III**: el acta 164 lo dibujo desde una cifra falsa, y\n"
        "redibujarlo desde la cifra buena seguiria siendo una decision de alcance que\n"
        "nadie encargo.\n"
        % (MARCA, n_aguja, linea_aguja.strip(), resumen["operaciones"],
           resumen["hecha"], resumen["lista"], "\n".join(tabla),
           resumen["hecha"], resumen["lista"],
           resumen["operaciones"] - resumen["hecha"], resumen["sin_dep"], nombres,
           resumen["operaciones"] - resumen["hecha"] - resumen["sin_dep"],
           resumen["libres"]))


def main(aplicar):
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 166, TAREA 4b: LA CORRECCION DECLARADA, DONDE LA CIFRA VIAJO")
    print("=" * 78)
    print("")

    print("A) LA TABLA, LEIDA DE SU FICHERO DE SALIDA Y NO TECLEADA")
    leido = tabla_del_fichero()
    if leido is None:
        print("   PARADA: no se pudo leer la tabla de %s." % SALIDA)
        print("   SI NO HAY FICHERO QUE CONTAR, LA TABLA NO SE PUBLICA.")
        return 1
    filas, total, resumen, sin_dep = leido
    print("   fichero: docs/loop/SALIDA_V166_T4_CENSO_OPERACIONES.txt")
    print("   CIFRA filas de fase leidas: %d" % len(filas))
    print("   CIFRA total leido: HECHA %s, LISTA %s, total %s" % total)
    for k in sorted(resumen):
        print("   CIFRA %-12s %d" % (k + ":", resumen[k]))
    print("   CIFRA operaciones sin dependencias, nombradas: %d" % len(sin_dep))
    suma = sum(int(t) for _f, _h, _l, t in filas)
    print("   la suma de las filas es el total: %s (%d contra %s)"
          % (suma == int(total[2]), suma, total[2]))
    if suma != int(total[2]) or len(sin_dep) != resumen["sin_dep"]:
        print("   PARADA: la tabla leida no cuadra consigo misma.")
        return 1
    print("")
    texto = io.open(SEDE, encoding="utf-8").read()
    lineas = texto.split("\n")
    print("B) LA IDEMPOTENCIA, COMPROBADA ANTES QUE NADA Y NO DESPUES")
    print("   EL ORDEN IMPORTA Y SE DICE POR QUE, porque la primera version de")
    print("   este instrumento lo tenia al reves y NO ERA IDEMPOTENTE: el bloque")
    print("   que el mismo escribe CITA la frase que luego busca, asi que en la")
    print("   segunda corrida la frase aparecia DOS veces y el instrumento paraba")
    print("   diciendo que la linea era ambigua. Una guarda que se dispara con su")
    print("   propia escritura no mide el fichero: se mide a si misma.")
    if MARCA in texto:
        print("   YA ESTABA: el bloque de la correccion vive en el fichero.")
        print("   CIFRA bloques escritos: 0")
        return 0
    print("   la marca no esta: se puede seguir.")
    print("")

    print("C) LA LINEA DONDE LA CIFRA VIAJO, LOCALIZADA Y NO TECLEADA")
    agujas = [i for i, l in enumerate(lineas, 1) if AGUJA in l]
    print("   CIFRA veces que la frase de la cifra falsa aparece: %d" % len(agujas))
    for i in agujas:
        print("      docs/PENDIENTES.md:%d" % i)
    if len(agujas) != 1:
        print("   PARADA: la frase no es unica. No se cita una linea ambigua.")
        return 1
    n_aguja = agujas[0]
    print("   la linea, entera:")
    print("      %s" % lineas[n_aguja - 1].strip()[:200])
    print("")

    b = bloque(filas, total, resumen, sin_dep, n_aguja, lineas[n_aguja - 1])
    nuevo = texto + b
    print("D) LAS GUARDAS, SOBRE EL TEXTO NUEVO SIN ESCRIBIRLO")
    guardas = [
        ("1_es_adicion_pura_el_texto_viejo_entero_esta_dentro",
         nuevo.startswith(texto), True),
        ("2_R_34_no_pierde_una_letra", lineas[n_aguja - 1] in nuevo, True),
        ("3_la_cifra_vieja_del_acta_164_se_cita_y_no_se_borra",
         "67 estan en `HECHA` y CUATRO en `LISTA`" in nuevo, True),
        ("4_la_tabla_pegada_lleva_todas_las_fases_medidas",
         sum(1 for f, _h, _l, _t in filas if ("| `%s` |" % f) in b), len(filas)),
        ("5_las_sin_dependencias_van_nombradas",
         sum(1 for o, _f in sin_dep if ("`%s`" % o) in b), len(sin_dep)),
        ("6_cero_guiones_largos_y_medios",
         b.count("\u2014") + b.count("\u2013"), 0),
    ]
    malos = 0
    for nombre, real, esp in guardas:
        ok = real == esp
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esp))
        if not ok:
            malos += 1
    if malos:
        print("   PARADA: la simulacion falla. NO SE ESCRIBE NADA.")
        return 1
    print("")

    print("E) EL BLOQUE ENTERO, PARA QUE NADA ENTRE SIN LEERSE")
    print(b)
    if not aplicar:
        print("F) NO SE ESCRIBE (falta --aplicar)")
        return 0
    with io.open(SEDE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(nuevo)
    print("F) ESCRITO")
    t2 = io.open(SEDE, encoding="utf-8").read()
    print("   CIFRA lineas antes: %d | despues: %d"
          % (len(lineas), len(t2.split("\n"))))
    print("   el bloque esta: %s" % (MARCA in t2))
    print("   la linea de R.34 sigue entera: %s" % (lineas[n_aguja - 1] in t2))
    print("   FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main("--aplicar" in sys.argv))
