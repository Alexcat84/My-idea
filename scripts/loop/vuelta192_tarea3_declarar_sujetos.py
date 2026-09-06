# -*- coding: utf-8 -*-
r"""vuelta192_tarea3_declarar_sujetos.py . LOS DOS `SUJETO VIVO` DE LA VUELTA 191,
ARREGLADOS CADA UNO POR SU CARRIL, PORQUE NO SON EL MISMO CASO.

ES LA PIEZA `b` DE LA TAREA 3, sobre el hallazgo `5.1` del acta 192. La `4.4` del
acta 191 adjudico que `SUJETO VIVO` es **FALLO y no deuda**, asi que dejarlos como
estan no es una opcion. **Pero los dos no son el mismo caso, y tratarlos igual
seria tapar la diferencia en vez de medirla:**

  1. `vuelta191_tarea3_arreglar_lineas.py` es un **FALSO POSITIVO DE LA GUARDA**,
     y esta medido: sus SEIS apariciones de `REPORTE.md` en la maquina estan
     TODAS **dentro de literales de cadena que son PATRONES DE PARCHEO**, o sea el
     texto que ese fichero busca y sustituye DENTRO DE OTROS SCRIPTS cuyos `print`
     mencionan el reporte. **El fichero no abre `docs/loop/REPORTE.md` en ninguna
     linea**, y este instrumento lo comprueba antes de declarar nada. Su carril es
     **la declaracion en el propio arnes** (`MARCA_DECLARA_CONGELADO`), que es
     exactamente para lo que existe.

  2. `vuelta191_tarea1a_registrar_acta191.py` **TIENE EL SUJETO VIVO DE VERDAD**:
     su linea `ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")` y su
     `os.path.getsize(ACTA)` abren el acta VIVA, porque un registrador **tiene que
     leer el acta de hoy**: congelarlo lo romperia. **Declararlo CONGELADO seria
     mentir**, y esa mentira es peor que el fallo. Su carril es el otro que la
     casa tiene: **escribir el motivo**, para que pase de `SUJETO VIVO` (FALLO) a
     `NO DECIDIBLE CON MOTIVO ESCRITO` (DEUDA DECLARADA). Y para que el veredicto
     pueda ser `NO DECIDIBLE` hace falta una huella de congelado que sea **VERDAD
     Y UTIL, no un literal puesto para enganar a la guarda**: se le anade que
     PUBLIQUE EL `sha256` DEL ACTA QUE ACABA DE LEER. Con eso, una corrida suya
     que lea otra acta se puede detectar, que es justo lo que "congelar" quiere
     decir en espiritu.

**LO QUE NO SE HACE, Y ES LA MITAD QUE IMPORTA: NO SE LE PONE A NADIE UNA HUELLA
DE CONGELADO QUE NO SEA CIERTA.** Escribir `SUJETO CONGELADO` en un fichero cuyo
sujeto esta vivo apaga la guarda sin arreglar nada, y esa es exactamente la
enfermedad que la guarda vino a curar.

LO QUE ESTE FICHERO NO HACE: **no corre ninguno de los dos arneses.** El anclaje
se decide leyendo el TEXTO, y correrlos pisaria salidas selladas de la 191. No se
toca la nomina, no se poda, no se adelanta y no se le anade nada.

USO:
  python scripts/loop/vuelta192_tarea3_declarar_sujetos.py --simular
  python scripts/loop/vuelta192_tarea3_declarar_sujetos.py
"""
import argparse
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as VMV   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
DIR = os.path.join(RAIZ, "scripts", "loop")
NL = chr(10)

FALSO_POSITIVO = "vuelta191_tarea3_arreglar_lineas.py"
SUJETO_DE_VERDAD = "vuelta191_tarea1a_registrar_acta191.py"

# --- LO QUE SE LE ANADE AL FALSO POSITIVO -----------------------------------
ANCLA_FP = "CAMBIOS = ["
BLOQUE_FP = '''# --- DECLARACION DE SUJETO, ANADIDA EN LA VUELTA 192 (TAREA 3.b) -------------
#
# SUJETO CONGELADO. Este fichero salia `SUJETO VIVO` en
# `guarda_del_sujeto_congelado_separada()` por SEIS apariciones del literal
# `REPORTE.md` en su maquina, y LAS SEIS ESTAN DENTRO DE LOS LITERALES DE
# `CAMBIOS`, que son PATRONES DE PARCHEO: el texto que este fichero BUSCA Y
# SUSTITUYE dentro de OTROS scripts cuyos `print` mencionan el reporte.
#
# ESTE FICHERO NO ABRE `docs/loop/REPORTE.md` EN NINGUNA LINEA, y se puede
# comprobar: sus unicas aperturas son sobre `ruta`, que sale de los nombres de
# `CAMBIOS`, y sobre su propia `SALIDA`. La declaracion va aqui, con su
# evidencia, en vez de ensanchar la huella de la guarda: una huella mas estrecha
# dejaria de ver casos de verdad, y el precio de un falso positivo es una linea
# como esta.
#
# Lo declara la vuelta 192 y lo mide `scripts/loop/vuelta192_tarea3_declarar_sujetos.py`.

'''

# --- LO QUE SE LE ANADE AL QUE TIENE EL SUJETO VIVO DE VERDAD ---------------
ANCLA_IMPORT = "import argparse\nimport io\n"
NUEVO_IMPORT = "import argparse\nimport hashlib\nimport io\n"

ANCLA_MEDIDA = ('    w("   docs/loop/ACTA_AUDITOR.md -> disco %d bytes" '
                '% os.path.getsize(ACTA))')
NUEVA_MEDIDA = '''    # EL SUJETO DE ESTE INSTRUMENTO ESTA VIVO A PROPOSITO Y AQUI SE DICE POR QUE
    # (vuelta 192, TAREA 3.b). Un registrador TIENE que leer el acta de hoy:
    # congelarlo lo romperia. Lo que si se puede, y es lo que se hace desde esta
    # linea, es PUBLICAR EL `sha256` DE LO QUE ACABA DE LEER, para que una corrida
    # que lea otra acta se pueda detectar. NO SE TOCA el acta: se abre en lectura.
    _datos_acta = io.open(ACTA, "rb").read()
    _lf_acta = _datos_acta.replace(b"\\r\\n", b"\\n")
    w("   docs/loop/ACTA_AUDITOR.md -> disco %d bytes | LF %d bytes"
      % (len(_datos_acta), len(_lf_acta)))
    w("   sha256 LF del acta leida: %s" % hashlib.sha256(_lf_acta).hexdigest())'''

# LOS MOTIVOS QUE SE ESCRIBEN AL LADO DE CADA LINEA DE SUJETO VIVO. La clave es
# el literal EXACTO de la linea del fichero; el valor, el comentario que se le
# pone JUSTO ENCIMA. `motivo_del_sujeto_vivo()` pide una marca en la ventana de
# tres lineas de CADA aparicion, y por eso van una a una y no en un bloque.
MOTIVOS = [
    ('ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")',
     '# NO SE TOCA: el acta se abre SOLO EN LECTURA y su sha256 se publica.',
     "antes"),
    ('        p.append("  - **`%s` (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). '
     'FAMILIA: %s. "',
     '    # NO SE TOCA: es una CITA de la linea del acta dentro del texto de la entrada.',
     "antes"),
    ('        p.append("  - `docs/loop/ACTA_AUDITOR.md:%d`: %s" % (ln, txt))',
     '    # NO SE TOCA: es una CITA de la linea del acta dentro del texto de la entrada.',
     "antes"),
    ('        p.append("  - **`%s` (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). '
     'VIA: %s.** %s."',
     '    # NO SE TOCA: es una CITA de la linea del acta dentro del texto de la entrada.',
     "antes"),
    ('    w("   acta %d: docs/loop/ACTA_AUDITOR.md, lineas %d a %d"',
     '    # NO SE TOCA: se publica el tramo leido; el acta no se escribe.',
     "antes"),
    # ESTA VA DESPUES Y NO ANTES, Y LA RAZON ES DE SINTAXIS: la linea de la
    # huella es la CONTINUACION de un literal de cadena dentro de un diccionario,
    # y un comentario delante de ella es un error de sintaxis. Detras si es legal,
    # y la ventana de tres lineas de `motivo_del_sujeto_vivo()` la alcanza igual.
    ('            "vuelta no escribe ni una linea de `docs/plan/OPERACIONES.jsonl`.**"),',
     '    # NO SE TOCA ni una linea de OPERACIONES.jsonl: es texto de la glosa.',
     "despues"),
]


def anclaje(nombre):
    t = VMV.texto_del_arnes(nombre, DIR)
    v, c, vv = VMV.anclaje_de(t)
    tiene, ev = VMV.motivo_del_sujeto_vivo(t)
    return v, c, vv, tiene, ev


def insertar_motivos(texto, motivos):
    """EL COMENTARIO DE MOTIVO, INSERTADO EN **TODAS** LAS APARICIONES DE CADA
    LINEA Y NO SOLO EN LA PRIMERA. PURA. Devuelve `(texto, aplicados, faltan)`.

    POR QUE VA LINEA A LINEA Y NO CON `replace`, Y ESTA MEDIDO: el registrador
    tiene la linea `p.append("  - \`docs/loop/ACTA_AUDITOR.md:%d\`: %s" ...)`
    **DOS VECES**, y un `replace(..., 1)` deja la segunda sin marca. Con una sola
    sin marca, `motivo_del_sujeto_vivo()` devuelve False para el fichero entero,
    porque exige la marca en TODAS las apariciones. **Se cazo simulando, antes de
    escribir nada.**

    Es IDEMPOTENTE: si la linea de al lado ya es la marca, no se vuelve a poner."""
    lineas = texto.split(NL)
    aplicados, faltan = [], []
    for viejo, comentario, donde in motivos:
        objetivo = viejo.split(NL)[0] if NL in viejo else viejo
        sangria = " " * (len(objetivo) - len(objetivo.lstrip()))
        marca = sangria + comentario.strip()
        puestas = 0
        i = 0
        while i < len(lineas):
            if lineas[i] != objetivo:
                i += 1
                continue
            vecina = lineas[i - 1] if donde == "antes" and i > 0 else (
                lineas[i + 1] if donde == "despues" and i + 1 < len(lineas) else None)
            if vecina == marca:
                i += 1
                continue
            corte = i if donde == "antes" else i + 1
            lineas.insert(corte, marca)
            puestas += 1
            i += 2
        if puestas == 0 and objetivo not in lineas:
            faltan.append(objetivo[:70])
        else:
            aplicados.append((objetivo[:60],
                              "%d aparicion(es)" % puestas if puestas
                              else "YA ESTABAN"))
    return NL.join(lineas), aplicados, faltan


def aplicar(texto, cambios):
    """(texto_nuevo, aplicados, no_hallados). PURA."""
    aplicados, faltan = [], []
    for viejo, nuevo in cambios:
        if viejo not in texto:
            faltan.append(viejo[:70])
            continue
        if nuevo in texto:
            aplicados.append((viejo[:60], "YA ESTABA"))
            continue
        texto = texto.replace(viejo, nuevo, 1)
        aplicados.append((viejo[:60], "aplicado"))
    return texto, aplicados, faltan


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 192, TAREA 3.b: LOS DOS `SUJETO VIVO`, CADA UNO POR SU CARRIL")
    w("=" * 78)
    w("")

    w("A) EL ANCLAJE DE LOS DOS, ANTES DE TOCAR NADA")
    antes = {}
    for n in (FALSO_POSITIVO, SUJETO_DE_VERDAD):
        v, c, vv, tiene, _ev = anclaje(n)
        antes[n] = v
        w("   %-46s %-14s congela=%s vive=%s motivo=%s"
          % (n, v, c or "[]", vv, "SI" if tiene else "no"))
    w("")

    w("B) LA COMPROBACION QUE SOSTIENE LA DECLARACION DEL FALSO POSITIVO")
    w("   (no se declara nada sin medirlo: se cuentan las aperturas de fichero)")
    p_fp = os.path.join(DIR, FALSO_POSITIVO)
    t_fp = io.open(p_fp, encoding="utf-8").read().replace(chr(13) + NL, NL)
    aperturas = [(i, l.strip()) for i, l in enumerate(t_fp.split(NL), 1)
                 if re.search(r"\bio\.open\(|(?<![.\w])open\(", l)]
    w("   CIFRA aperturas de fichero en %s: %d" % (FALSO_POSITIVO, len(aperturas)))
    for i, l in aperturas:
        w("      linea %-5d %s" % (i, l[:110]))
    abre_reporte = [(i, l) for i, l in aperturas if "REPORTE.md" in l]
    w("   CIFRA de esas aperturas que nombran REPORTE.md: %d" % len(abre_reporte))
    if abre_reporte:
        w("   PARADA: el fichero SI abre el reporte y la declaracion seria falsa.")
        print(NL.join(L))
        return 1
    w("   NINGUNA APERTURA NOMBRA EL REPORTE: la declaracion es cierta.")
    w("")

    w("C) LA COMPROBACION QUE SOSTIENE EL OTRO CARRIL")
    p_sv = os.path.join(DIR, SUJETO_DE_VERDAD)
    t_sv = io.open(p_sv, encoding="utf-8").read().replace(chr(13) + NL, NL)
    ap_sv = [(i, l.strip()) for i, l in enumerate(t_sv.split(NL), 1)
             if re.search(r"\bio\.open\(", l) and "ACTA" in l]
    w("   CIFRA aperturas de %s que nombran ACTA: %d"
      % (SUJETO_DE_VERDAD, len(ap_sv)))
    for i, l in ap_sv:
        w("      linea %-5d %s" % (i, l[:110]))
    getsize = [(i, l.strip()) for i, l in enumerate(t_sv.split(NL), 1)
               if "getsize(ACTA)" in l]
    for i, l in getsize:
        w("      linea %-5d %s" % (i, l[:110]))
    if not ap_sv and not getsize:
        w("   PARADA: no se encuentra donde abre el acta, y sin eso la declaracion")
        w("   de que su sujeto esta vivo DE VERDAD no se sostiene.")
        print(NL.join(L))
        return 1
    w("   EL SUJETO ESTA VIVO DE VERDAD: declararlo CONGELADO seria mentir.")
    w("")

    w("D) LOS CAMBIOS, APLICADOS UNO A UNO")
    nuevo_fp, ap1, falta1 = aplicar(t_fp, [(ANCLA_FP, BLOQUE_FP + ANCLA_FP)])
    cambios_sv = [(ANCLA_IMPORT, NUEVO_IMPORT), (ANCLA_MEDIDA, NUEVA_MEDIDA)]
    paso1_sv, ap2a, falta2a = aplicar(t_sv, cambios_sv)
    nuevo_sv, ap2b, falta2b = insertar_motivos(paso1_sv, MOTIVOS)
    ap2 = ap2a + ap2b
    falta2 = falta2a + falta2b
    for nombre, aps, falt in ((FALSO_POSITIVO, ap1, falta1),
                              (SUJETO_DE_VERDAD, ap2, falta2)):
        w("   %s" % nombre)
        for viejo, estado in aps:
            w("      %-8s %s" % (estado, viejo))
        for f in falt:
            w("      NO HALLADO %s" % f)
    if falta1 or falta2:
        w("   PARADA: hay anclas que no se encuentran. No se escribe nada, porque")
        w("   un parche a medias deja el fichero peor que antes.")
        print(NL.join(L))
        return 1
    w("")

    if a.simular:
        w("E) MODO --simular: NO SE ESCRIBE NADA.")
        w("   %s pasaria de %d a %d bytes en disco"
          % (FALSO_POSITIVO, len(t_fp.encode("utf-8")),
             len(nuevo_fp.encode("utf-8"))))
        w("   %s pasaria de %d a %d bytes en disco"
          % (SUJETO_DE_VERDAD, len(t_sv.encode("utf-8")),
             len(nuevo_sv.encode("utf-8"))))
        v1 = VMV.anclaje_de(nuevo_fp)
        v2 = VMV.anclaje_de(nuevo_sv)
        m2 = VMV.motivo_del_sujeto_vivo(nuevo_sv)
        w("   ANCLAJE QUE SALDRIA, computado sobre el texto nuevo SIN escribirlo:")
        w("      %-46s %s -> %s" % (FALSO_POSITIVO, antes[FALSO_POSITIVO], v1[0]))
        w("      %-46s %s -> %s (motivo escrito: %s)"
          % (SUJETO_DE_VERDAD, antes[SUJETO_DE_VERDAD], v2[0],
             "SI" if m2[0] else "no"))
        print(NL.join(L))
        return 0

    io.open(p_fp, "w", encoding="utf-8", newline=NL).write(nuevo_fp)
    io.open(p_sv, "w", encoding="utf-8", newline=NL).write(nuevo_sv)
    w("E) ESCRITOS, Y RELEIDOS DEL DISCO PARA COMPROBARLO")
    w("   %s -> disco %d bytes | LF %d bytes"
      % (FALSO_POSITIVO, os.path.getsize(p_fp),
         len(io.open(p_fp, "rb").read().replace(b"\r\n", b"\n"))))
    w("   %s -> disco %d bytes | LF %d bytes"
      % (SUJETO_DE_VERDAD, os.path.getsize(p_sv),
         len(io.open(p_sv, "rb").read().replace(b"\r\n", b"\n"))))
    w("")
    w("F) LOS DOS COMPILAN, QUE ES LO MINIMO ANTES DE DARLOS POR ARREGLADOS")
    import py_compile
    for p in (p_fp, p_sv):
        try:
            py_compile.compile(p, doraise=True)
            w("   %s -> COMPILA" % os.path.basename(p))
        except Exception as e:
            w("   %s -> NO COMPILA: %r" % (os.path.basename(p), e))
            print(NL.join(L))
            return 1
    w("")
    w("G) EL ANCLAJE, REMEDIDO DEL DISCO Y NO SUPUESTO")
    for n in (FALSO_POSITIVO, SUJETO_DE_VERDAD):
        v, c, vv, tiene, ev = anclaje(n)
        w("   %-46s %s -> %s" % (n, antes[n], v))
        w("      congela=%s" % (c or "[]"))
        w("      vive=%s" % (vv or "[]"))
        w("      motivo escrito en TODAS sus apariciones: %s"
          % ("SI" if tiene else "no"))
        for ln, h, marcas in ev:
            w("         linea %-5d huella %-32s marcas: %s"
              % (ln, h, ", ".join(marcas) or "(NINGUNA)"))
    w("")
    w("H) NINGUNO DE LOS DOS SE HA CORRIDO, Y SE DICE POR QUE: correrlos pisaria")
    w("   salidas selladas de la vuelta 191. El anclaje se decide leyendo el")
    w("   TEXTO, y eso es lo que se ha hecho.")
    w("")
    w("FIN")
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V192_T3_DECLARAR_SUJETOS.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V192_T3_DECLARAR_SUJETOS.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
