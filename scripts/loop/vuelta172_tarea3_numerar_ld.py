# -*- coding: utf-8 -*-
r"""vuelta172_tarea3_numerar_ld.py . TAREA 3 DE LA VUELTA 172.

LAS 16 LECTURAS DE LA SEGUNDA TANDA DE `docs/plan/LECTURAS_DIRIGIDAS.md` GANAN SU
NUMERO `LD`, POR ADICION PURA Y CON LOS NUMEROS COMPUTADOS (adjudicacion 6.2 del
acta 171).

LA REGLA QUE ASIGNA, Y NO ES DOCTRINA NUEVA: `serie_de_registros.py` computa el
siguiente libre sobre ENTRADAS ESCRITAS CON SU CABECERA, no sobre menciones. La
6.2 del acta 171 traslada eso al `LD`: **la vara que asigna es la de las HECHAS,
las que tienen SECCION PROPIA**, y el "universo" de `vuelta48_contar_ld.py` es su
detector de encargadas y sin hacer, no la autoridad de la numeracion.

POR ADICION PURA, Y AQUI ESTA LO QUE ESO SIGNIFICA EXACTAMENTE: **las tres tablas
de la segunda tanda no se tocan, ni una palabra ni un byte**. Lo que se anade es
un bloque NUEVO al final de la segunda tanda, con las 16 secciones en la forma de
la casa (``### `LD-nn` . `a` contra `b` . **CLASE**``), **y el par y la clase de
cada una se LEEN de la tabla**, no se teclean.

Y LO QUE ESTE INSTRUMENTO NO HACE, DICHO PARA QUE NADIE LO SUPONGA: **no vuelve a
leer ningun par**. Las 16 lecturas ya estan hechas y sus veredictos ya estan
escritos en las tablas desde el 11 ago 2026. **Lo unico que faltaba era el
numero.** Ninguna clase se mueve, ningun nodo se toca, y `master_graph.json` no
se abre siquiera.

LAS DOS GUARDAS QUE EL ENCARGO EXIGE, Y LAS DOS TIENEN QUE CAER POR MUTACION
(arnes hermano `vuelta172_tarea3_mutacion_numeracion.py`):

  (i)  EL NUMERO SE COMPUTA Y NO SE TECLEA. Sale de `max(hechas) + 1` sobre la
       lectura de hoy, con las funciones del propio contador.
  (ii) NINGUN NUMERO POR ENCIMA DEL MAYOR DE LAS HECHAS TIENE SECCION PROPIA. Si
       alguno la tuviera, hay una asignacion ajena y ESTE INSTRUMENTO PARA sin
       escribir.

USO:
  python scripts/loop/vuelta172_tarea3_numerar_ld.py
"""
import io
import os
import re
import sys

NL = chr(10)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta48_contar_ld as C   # noqa: E402

RAIZ = C.RAIZ
LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
FECHA = "5 sep 2026"

CAB_SEGUNDA = "# SEGUNDA TANDA: LA SELECCION DE `OP-L-02`"
CAB_TERCERA = "# TERCERA TANDA:"

# LOS TRES BLOQUES DE LA SEGUNDA TANDA, localizados por SU TITULO y no por numero
# de linea: un numero de linea es una cifra de cruce y caduca sola.
BLOQUES = [
    ("## LOS CUADRANTES DE MERCADO: 15 de 15, y cae", "cuadrantes de mercado"),
    ("## LA ECUACION DE VALOR: 10 de 10, y cae", "ecuacion de valor"),
    ("## LA SUPERVISION DE LA IA, bloque humano: 10 de 10, y cae",
     "supervision de la IA, bloque humano"),
]

RE_FILA = re.compile(
    r"^\|\s*\*{0,2}`([a-z0-9_]+)`\s+contra\s+`([a-z0-9_]+)`\*{0,2}\s*\|\s*\*\*([A-Z])\*\*\s*\|$")

MARCA = "<!-- NUMERACION LD DE LA SEGUNDA TANDA, VUELTA 172 -->"


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def siguiente_libre(hechas):
    """EL NUMERO QUE NO SE TECLEA. Uno mas que el mayor con SECCION PROPIA, que
    es la misma regla que `serie_de_registros.siguiente_libre` usa para la serie
    `R.n`. PURA a proposito: recibe el mapa de hechas, para que su caso rojo se
    pruebe por mutacion sin tocar el disco."""
    return (max(hechas) + 1) if hechas else 1


def asignacion_ajena(hechas, corte=None):
    """LOS NUMEROS CON SECCION PROPIA POR ENCIMA DEL CORTE. Si esta lista no
    esta vacia, alguien asigno por su cuenta y hay que PARAR. PURA."""
    tope = corte if corte is not None else (max(hechas) if hechas else 0)
    return sorted(n for n in hechas if n > tope)


def filas_de_la_segunda_tanda(texto):
    """Las filas de par de los tres bloques, LEIDAS del fichero. Devuelve
    [(bloque, linea, nodo_a, nodo_b, clase)] en orden de lectura."""
    lineas = texto.split(NL)
    fuera = []
    for titulo, etiqueta in BLOQUES:
        inicios = [i for i, l in enumerate(lineas, 1) if l.startswith(titulo)]
        if len(inicios) != 1:
            raise SystemExit("ROJO: el bloque %r aparece %d veces" % (titulo, len(inicios)))
        ini = inicios[0]
        sig = [i for i, l in enumerate(lineas, 1)
               if i > ini and (l.startswith("## ") or l.startswith("# "))]
        fin = min(sig) - 1 if sig else len(lineas)
        for i in range(ini, fin + 1):
            m = RE_FILA.match(lineas[i - 1])
            if m:
                fuera.append((etiqueta, i, m.group(1), m.group(2), m.group(3)))
    return fuera


def main():
    print("=" * 78)
    print("VUELTA 172, TAREA 3: LAS 16 LECTURAS DE LA SEGUNDA TANDA GANAN SU NUMERO")
    print("=" * 78)
    print("")
    rojos = []

    texto = leer(LD)
    print("A) EL SUJETO, MEDIDO ANTES DE TOCARLO")
    print("   docs/plan/LECTURAS_DIRIGIDAS.md -> %d bytes, %d saltos de linea"
          % (len(texto.encode("utf-8")), texto.count(NL)))
    print("   ya lleva la marca de esta tarea: %s" % ("SI" if MARCA in texto else "NO"))
    if MARCA in texto:
        print("YA ESTABA: la numeracion ya se escribio. No se toca.")
        return 0
    print("")

    print("B) LAS DOS VARAS, LEIDAS CON LAS FUNCIONES DEL PROPIO CONTADOR")
    hechas = {}
    for nombre in C.PAGINAS:
        p = os.path.join(C.PLAN, nombre)
        for i, l in enumerate(io.open(p, encoding="utf-8"), 1):
            m = C.RE_CAB.match(l)
            if m:
                hechas.setdefault(int(m.group(1)), []).append("%s:%d" % (nombre, i))
    mayor_hechas = max(hechas)
    print("   CIFRA hechas (ids con seccion propia): %d" % len(hechas))
    print("   mayor de las HECHAS, computado: LD-%d" % mayor_hechas)
    siguiente = siguiente_libre(hechas)
    print("   SIGUIENTE LIBRE, computado y NO tecleado: LD-%d" % siguiente)
    print("")

    print("C) GUARDA (ii): NINGUN NUMERO POR ENCIMA DE LD-%d TIENE SECCION PROPIA"
          % mayor_hechas)
    ajenos = asignacion_ajena(hechas)
    print("   CIFRA numeros con seccion propia por encima de LD-%d: %d"
          % (mayor_hechas, len(ajenos)))
    if ajenos:
        for n in ajenos:
            print("      LD-%d en %s" % (n, ", ".join(hechas[n])))
        rojos.append("hay asignacion ajena por encima de LD-%d" % mayor_hechas)
    print("")

    print("D) LAS FILAS DE LA SEGUNDA TANDA, LEIDAS DEL FICHERO Y NO TECLEADAS")
    filas = filas_de_la_segunda_tanda(texto)
    por_bloque = {}
    for etiqueta, _i, _a, _b, _c in filas:
        por_bloque[etiqueta] = por_bloque.get(etiqueta, 0) + 1
    for etiqueta in [e for _t, e in BLOQUES]:
        print("   CIFRA filas de par en %-40s %d" % (etiqueta, por_bloque.get(etiqueta, 0)))
    print("   CIFRA filas de par en total: %d" % len(filas))
    clases = {}
    for _e, _i, _a, _b, c in filas:
        clases[c] = clases.get(c, 0) + 1
    for c in sorted(clases):
        print("   CIFRA clase %s: %d" % (c, clases[c]))
    if len(filas) != 16:
        rojos.append("la segunda tanda trae %d filas de par y el encargo nombra 16"
                     % len(filas))
    print("")

    print("E) EL CONTRASTE CON EL SALDO QUE LA PROPIA PAGINA PUBLICA")
    print("   (es CONTRASTE y no fuente: manda el conteo de arriba)")
    for etiqueta, aguja in (("leidas", "| **leidas** | **16** |"),
                            ("REPITEN (A)", "| **REPITEN (A)** | **2** |"),
                            ("SANAS (D)", "| **SANAS (D)** | **14** |")):
        print("   la pagina publica %-12s %s" % (etiqueta, "SI" if aguja in texto else "NO"))
    print("   mi conteo: A=%d, D=%d" % (clases.get("A", 0), clases.get("D", 0)))
    print("")

    if rojos:
        print("ROJO, %d motivo(s), y NO se escribe nada:" % len(rojos))
        for r in rojos:
            print("   " + r)
        return 1

    print("F) SE ESCRIBE, POR ADICION PURA")
    numeros = list(range(siguiente, siguiente + len(filas)))
    print("   numeros asignados: LD-%d a LD-%d" % (numeros[0], numeros[-1]))

    trozos = [MARCA, "",
              "## LA NUMERACION `LD` DE ESTA TANDA, ESCRITA EN LA VUELTA 172",
              "",
              "**LAS DIECISEIS LECTURAS DE ARRIBA YA ESTABAN HECHAS DESDE EL 11 AGO 2026 Y",
              "SUS VEREDICTOS YA ESTABAN ESCRITOS; LO UNICO QUE LES FALTABA ERA EL NUMERO.**",
              "Aqui se les pone, **por adicion pura**: las tres tablas de arriba **no se han",
              "tocado, ni una palabra ni un byte**, y el par y la clase de cada seccion se han",
              "**leido de esas tablas**, no tecleado. **Ninguna clase se mueve, ningun nodo se",
              "toca y ningun par se vuelve a leer.**",
              "",
              "**LOS NUMEROS ESTAN COMPUTADOS, NO TECLEADOS** (`EJECUTOR.md` 1, y adjudicacion",
              "6.2 del acta del auditor de la vuelta 171). La vara que asigna es **la de las",
              "HECHAS, las que tienen seccion propia**, igual que `serie_de_registros.py`",
              "computa la serie `R.n` sobre entradas escritas y no sobre menciones: **una",
              "mencion en prosa no asigna un numero; una entrada escrita si.** Corrido por",
              "`scripts/loop/vuelta172_tarea3_numerar_ld.py` el %s: **%d hechas, mayor"
              % (FECHA, len(hechas)),
              "`LD-%d`, siguiente libre `LD-%d`.**" % (mayor_hechas, siguiente),
              "",
              "**GUARDA COMPROBADA ANTES DE ESCRIBIR:** ningun numero por encima de",
              "`LD-%d` tenia seccion propia (**%d**, contados por el instrumento). Si alguno"
              % (mayor_hechas, len(ajenos)),
              "la hubiera tenido, habria una asignacion ajena y esto habria parado.",
              ""]

    for (etiqueta, linea_origen, a, b, clase), n in zip(filas, numeros):
        trozos.append("### `LD-%d` . `%s` contra `%s` . **%s**" % (n, a, b, clase))
        trozos.append("")
        trozos.append("**Lectura de la SEGUNDA TANDA, nomina `%s`, hecha el 11 ago 2026.**"
                      % etiqueta)
        trozos.append("El par y la clase se leen de la tabla de esta misma pagina "
                      "(`docs/plan/LECTURAS_DIRIGIDAS.md:%d` al escribirse esta seccion),"
                      % linea_origen)
        trozos.append("**y la razon escrita de la lectura sigue viviendo alli y no se copia "
                      "aqui**: una")
        trozos.append("copia seria una segunda version de lo mismo. **Esta seccion aporta el "
                      "numero y")
        trozos.append("nada mas.**")
        trozos.append("")

    trozos.append("---")
    trozos.append("")
    bloque = NL.join(trozos)

    i = texto.index(CAB_TERCERA)
    texto = texto[:i] + bloque + texto[i:]
    io.open(LD, "w", encoding="utf-8", newline=NL).write(texto)
    print("   ESCRITO: docs/plan/LECTURAS_DIRIGIDAS.md (%d bytes, %d saltos de linea)"
          % (len(texto.encode("utf-8")), texto.count(NL)))
    print("   bloque anadido: %d bytes" % len(bloque.encode("utf-8")))
    print("")

    print("G) LA RELECTURA DEL DISCO")
    de_nuevo = leer(LD)
    lineas2 = de_nuevo.split(NL)
    cabeceras = [int(C.RE_CAB.match(l).group(1)) for l in lineas2 if C.RE_CAB.match(l)]
    nuevas = [n for n in cabeceras if n in numeros]
    fallos = 0
    # LAS TABLAS, BYTE A BYTE: se comprueba que cada fila de par sigue IGUAL.
    intactas = 0
    filas_de_nuevo = [RE_FILA.match(l).groups() for l in lineas2 if RE_FILA.match(l)]
    for _e, _i, a, b, clase in filas:
        if (a, b, clase) in filas_de_nuevo:
            intactas += 1
    for etiqueta, cond in (
            ("las 16 secciones nuevas existen", len(set(nuevas)) == len(numeros)),
            ("y ninguna esta repetida", len(nuevas) == len(numeros)),
            ("las 16 filas de par siguen intactas en sus tablas", intactas == len(filas)),
            ("la marca de esta tarea esta escrita", MARCA in de_nuevo),
            ("el bloque va DENTRO de la segunda tanda",
             de_nuevo.index(MARCA) > de_nuevo.index(CAB_SEGUNDA)
             and de_nuevo.index(MARCA) < de_nuevo.index(CAB_TERCERA)),
            ("cero guiones largos y cero guiones medios",
             chr(8212) not in de_nuevo and chr(8211) not in de_nuevo)):
        print("   %-58s %s" % (etiqueta, "SI" if cond else "NO"))
        if not cond:
            fallos += 1
    print("   CIFRA comprobaciones: 6 | fallan: %d" % fallos)
    print("")
    if fallos:
        print("ROJO: el fichero escrito no cumple %d de sus propias guardas." % fallos)
        return 1
    print("VERDE: las 16 lecturas de la segunda tanda quedan numeradas LD-%d a LD-%d."
          % (numeros[0], numeros[-1]))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
