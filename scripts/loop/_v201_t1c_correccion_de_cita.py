# -*- coding: utf-8 -*-
r"""_v201_t1c_correccion_de_cita.py . LA CORRECCION DE CITA DE LA TAREA 1.c DE
LA VUELTA 201, ESCRITA EN SU SEDE.

PREFIJO DE GUION BAJO Y POR EL MISMO MOTIVO QUE SUS HERMANOS: la moratoria de
maquinaria (`AUDITOR.md` 6.3) prohibe fabricar arneses, guardas y lectores
nuevos, y la adjudicacion `4.5` del acta 199 dice que un computo de una vuelta,
con prefijo de guion bajo, fuera del censo y fuera de la nomina, y que no vigila
a nadie, NO ES MAQUINARIA. Este fichero es eso: PONE UNA LINEA en un fichero y
mide lo que pone.

QUE CORRIGE, Y NO ES CAIDA. La seccion 8 de `docs/loop/reportes/REPORTE_V200.md`
sostiene su PARADA `1` diciendo que **`AUDITOR.md` 0** dice que cuando una guarda
contradice una decision escrita del fundador, la que se corrige es la guarda.
**Esas palabras no estan en `AUDITOR.md`**: son del **acta 185, punto `6.2`**,
derivadas de la jerarquia que `AUDITOR.md` 0 si establece. **No se cobra**: es la
forma en que la casa lo cita desde el acta 185.

LAS DOS MEDICIONES QUE LA SOSTIENEN SE HACEN AQUI Y NO SE HEREDAN:
  . cuantas lineas de `docs/loop/AUDITOR.md` traen el literal (se espera 0);
  . en que linea de `docs/loop/ACTA_AUDITOR.md` esta, y si esa linea cae DENTRO
    del cuerpo del acta 185 y por debajo de la cabecera de su punto `6.2`.
Si cualquiera de las dos no sale como la correccion afirma, NO SE ESCRIBE NADA:
una correccion que no se puede medir no se publica.

EL TEXTO VIEJO NO SE TOCA (banco `9.10` mas `EJECUTOR.md` 8): el aviso se ANADE
detras del parrafo, en UNA LINEA, y el parrafo se queda entero y sin tachar.

USO:
  python scripts/loop/_v201_t1c_correccion_de_cita.py
  python scripts/loop/_v201_t1c_correccion_de_cita.py --escribir
"""
import argparse
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

SEDE = os.path.join(LOOP, "reportes", "REPORTE_V200.md")
AUDITOR = os.path.join(LOOP, "AUDITOR.md")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")

# EL LITERAL QUE SE BUSCA EN LOS DOS FICHEROS. Es un trozo corto a proposito:
# cuanto mas largo, mas facil es que no case por una coma y que la medicion salga
# 0 por el motivo equivocado.
LITERAL = "se corrige es la guarda"
# EL ANCLA DEL PARRAFO EN LA SEDE. Es la ultima linea del parrafo de la PARADA 1.
ANCLA = "escribe como PARADA y no se arregla.**"
MARCA = "AVISO DE CITA (vuelta 201, TAREA 1.c)"


def medir_en(ruta, literal=LITERAL):
    """LAS LINEAS DE UN FICHERO QUE TRAEN EL LITERAL, 1-indexadas. Semi-pura:
    lo unico que toca disco es leer."""
    if not os.path.isfile(ruta):
        return None, []
    t = io.open(ruta, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    lineas = t.split(NL)
    return lineas, [i + 1 for i, l in enumerate(lineas) if literal in l]


def cota_del_acta(lineas, vuelta):
    """LA COTA DE UN ACTA, COMPUTADA DE SUS CABECERAS. Devuelve (ini, fin) o
    None. PURA: recibe las lineas ya leidas."""
    pat = re.compile(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA %d\b" % vuelta)
    hits = [i for i, l in enumerate(lineas, 1) if pat.match(l)]
    if len(hits) != 1:
        return None
    ini = hits[0]
    sig = [i for i, l in enumerate(lineas, 1)
           if i > ini and re.match(r"^#\s+ACTA\b", l)]
    return ini, ((sig[0] - 1) if sig else len(lineas))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 201, TAREA 1.c . LA CORRECCION DE CITA EN SU SEDE")
    w("=" * 78)
    w("")
    w("A) LA SEDE, MEDIDA AL ENTRAR")
    if not os.path.isfile(SEDE):
        w("   ROJO: NO EXISTE %s" % SEDE)
        print(NL.join(L))
        return 1
    crudo = io.open(SEDE, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    w("   docs/loop/reportes/REPORTE_V200.md: disco %d bytes | LF %d bytes"
      % (len(crudo), len(lf)))
    lineas_sede = lf.decode("utf-8").split(NL)
    w("   CIFRA lineas por split(NL): %d | por count(NL): %d"
      % (len(lineas_sede), lf.decode("utf-8").count(NL)))
    hs8 = [i + 1 for i, l in enumerate(lineas_sede) if re.match(r"^##\s*8\b", l)]
    w("   cabecera de la seccion 8: %d acierto(s), linea(s) %s"
      % (len(hs8), ", ".join(str(x) for x in hs8) or "(ninguna)"))
    anclas = [i + 1 for i, l in enumerate(lineas_sede) if ANCLA in l]
    w("   el ancla %r: %d acierto(s), linea(s) %s"
      % (ANCLA, len(anclas), ", ".join(str(x) for x in anclas) or "(ninguna)"))
    w("")

    w("B) LA MEDICION QUE SOSTIENE LA CORRECCION, HECHA AQUI Y NO HEREDADA")
    _la, en_auditor = medir_en(AUDITOR)
    lineas_acta, en_acta = medir_en(ACTA)
    w("   CIFRA lineas de docs/loop/AUDITOR.md con %r: %d  %s"
      % (LITERAL, len(en_auditor),
         ", ".join(str(x) for x in en_auditor) or "(ninguna)"))
    w("   CIFRA lineas de docs/loop/ACTA_AUDITOR.md con %r: %d  %s"
      % (LITERAL, len(en_acta),
         ", ".join(str(x) for x in en_acta) or "(ninguna)"))
    cota185 = cota_del_acta(lineas_acta, 185)
    w("   COTA del acta 185, computada de sus cabeceras: %s" % (cota185,))
    if cota185 is None:
        w("   ROJO: la cabecera del acta 185 no aparece exactamente una vez.")
        print(NL.join(L))
        return 1
    i185, f185 = cota185
    dentro = [x for x in en_acta if i185 <= x <= f185]
    w("   CIFRA de esas lineas que caen DENTRO del acta 185 (%d a %d): %d  %s"
      % (i185, f185, len(dentro),
         ", ".join(str(x) for x in dentro) or "(ninguna)"))
    cab62 = [j for j in range(i185, f185 + 1)
             if lineas_acta[j - 1].startswith("**`6.2`")]
    w("   cabecera del punto `6.2` DENTRO del acta 185: %d acierto(s), %s"
      % (len(cab62), ", ".join(str(x) for x in cab62) or "(ninguna)"))
    bajo62 = [x for x in dentro if cab62 and x > cab62[0]]
    w("   CIFRA de esas lineas que caen POR DEBAJO de la cabecera del `6.2`: %d"
      % len(bajo62))
    for x in dentro:
        w("      linea %d: %s" % (x, lineas_acta[x - 1].strip()))
    w("")

    w("C) LAS TRES CONDICIONES DE LA CORRECCION")
    cond = [
        ("el literal NO esta en AUDITOR.md", len(en_auditor) == 0),
        ("el literal SI esta en ACTA_AUDITOR.md", len(en_acta) >= 1),
        ("al menos una de esas lineas cae bajo el `6.2` del acta 185",
         len(bajo62) >= 1),
        ("el ancla del parrafo aparece exactamente una vez", len(anclas) == 1),
    ]
    for nombre, ok in cond:
        w("   %-58s %s" % (nombre, "SI" if ok else "NO"))
    if not all(ok for _n, ok in cond):
        w("   ROJO: alguna condicion no se cumple. NO SE ESCRIBE NADA: una")
        w("   correccion que no se puede medir no se publica.")
        print(NL.join(L))
        return 1
    w("")

    linea_cita = bajo62[0]
    aviso = ("> **%s. LA REGLA SE CITA, NO SE PARAFRASEA (banco `9.5.0`).** El "
             "parrafo de arriba se queda ENTERO Y SIN TACHAR, y esta linea solo "
             "corrige DE DONDE sale su regla: las palabras *\"Cuando una guarda "
             "contradice una decision del fundador, la que se corrige es la "
             "guarda\"* **no estan en `AUDITOR.md`** (medido en la vuelta 201 con "
             "`scripts/loop/_v201_t1c_correccion_de_cita.py`: **%d lineas** de "
             "`docs/loop/AUDITOR.md` traen el literal `%s`), sino en el **acta "
             "185, punto `6.2`**, en la **linea %d** de `docs/loop/ACTA_AUDITOR.md`, "
             "dentro del cuerpo del acta 185 acotado hoy en las lineas %d a %d y "
             "por debajo de la cabecera de su `6.2` en la linea %d; y de ahi "
             "salen derivadas de la jerarquia que `AUDITOR.md` 0 SI establece. "
             "**No es caida y no se cobra:** es la forma en que la casa lo cita "
             "desde el acta 185."
             % (MARCA, len(en_auditor), LITERAL, linea_cita, i185, f185,
                cab62[0]))
    w("D) EL AVISO, DE UNA LINEA, COMPUESTO Y MEDIDO")
    w("   CIFRA caracteres del aviso: %d" % len(aviso))
    w("   CIFRA lineas del aviso: %d" % (aviso.count(NL) + 1))
    w("   CIFRA guiones largos y medios en el aviso: %d"
      % (aviso.count(chr(8212)) + aviso.count(chr(8211))))
    w("")

    w("E) LA IDEMPOTENCIA Y LA ESCRITURA")
    texto = lf.decode("utf-8")
    ya = MARCA in texto
    w("   la marca %r ya esta en la sede: %s" % (MARCA, "SI" if ya else "NO"))
    if a.escribir and not ya:
        j = anclas[0]
        nuevas = lineas_sede[:j] + ["", aviso] + lineas_sede[j:]
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(NL.join(nuevas))
        w("   ESCRITO: el aviso queda en la linea %d, detras del parrafo" % (j + 2))
    elif a.escribir:
        w("   NO SE ESCRIBE: el aviso ya estaba. IDEMPOTENTE.")
    else:
        w("   MODO MEDICION: no se escribe nada.")
    despues = io.open(SEDE, "rb").read()
    w("   sede al salir: disco %d bytes | LF %d bytes"
      % (len(despues), len(despues.replace(b"\r\n", b"\n"))))
    w("   crecimiento en disco: %d bytes" % (len(despues) - len(crudo)))
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V201_T1C_CORRECCION_DE_CITA.txt"), "w",
            encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
