# -*- coding: utf-8 -*-
r"""_v192_parche_lector.py . ANADE AL LECTOR DE COTEJOS VIEJOS LA DEDUPLICACION
POR PUESTO Y EL COTEJO CONTRA LOS SEIS DE LA VUELTA 191.

POR QUE, Y ESTA MEDIDO: `_auditor_v191_cotejo_ciega.txt` sacaba **39 filas sobre
30 puestos distintos**, porque ese fichero lista cada discrepancia DOS VECES, una
en su tabla y otra en su bloque de detalle. Sin deduplicar, el lector habria
publicado un denominador de 30 al lado de 39 filas, **que es una cifra falsa de
las que esta casa caza**. Se cazo mirando la salida antes de publicarla.
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(RAIZ, "scripts", "loop", "lector_de_cotejos_viejos.py")
NL = chr(10)

VIEJO_LEER = '''def leer(ruta):
    """UN FICHERO, LEIDO CON TODOS LOS PARSEADORES. Devuelve un dict."""
    texto = io.open(ruta, encoding="utf-8", errors="replace").read()
    porp = filas_por_parseador(texto)
    cual = mejor_parseador(porp)
    filas = porp.get(cual, []) if cual else []
    n, de_donde = denominador_de(texto, filas)'''

NUEVO_LEER = '''def deduplicar(filas):
    """(FILAS SIN REPETIR, CUANTAS SE QUITARON). PURA, y conserva el orden.

    POR QUE HACE FALTA, Y ESTA MEDIDO: `_auditor_v191_cotejo_ciega.txt` lista
    **cada discrepancia DOS VECES**, una en su tabla y otra en su bloque de
    detalle, y el parseador sacaba **39 filas sobre 30 puestos distintos**. Sin
    esto, el lector habria publicado un denominador de 30 al lado de 39 filas,
    **que es exactamente la especie de cifra falsa que todo esto viene a
    evitar**. Se queda la PRIMERA aparicion de cada puesto y se cuenta cuantas se
    quitaron, **porque una fila descartada en silencio es una cifra que nadie
    puede cotejar**."""
    vistos = set()
    salida = []
    quitadas = 0
    for f in filas:
        if f[0] in vistos:
            quitadas += 1
            continue
        vistos.add(f[0])
        salida.append(f)
    return salida, quitadas


def leer(ruta):
    """UN FICHERO, LEIDO CON TODOS LOS PARSEADORES. Devuelve un dict."""
    texto = io.open(ruta, encoding="utf-8", errors="replace").read()
    porp = filas_por_parseador(texto)
    cual = mejor_parseador(porp)
    crudas = porp.get(cual, []) if cual else []
    filas, quitadas = deduplicar(crudas)
    n, de_donde = denominador_de(texto, filas)'''

VIEJO_DICT = '''        "n_filas": len(filas),
        "n_con_clases": len(con_clases),'''
NUEVO_DICT = '''        "n_filas": len(filas),
        "n_crudas": len(crudas),
        "n_duplicadas": quitadas,
        "n_con_clases": len(con_clases),'''

VIEJO_B = '''            w("   RECUPERA %-52s %s: %d filas con clases, denominador %s (%s)"
              % (n, r["cual"], r["n_con_clases"], r["denominador"], r["de_donde"]))'''
NUEVO_B = '''            w("   RECUPERA %-52s %s: %d filas con clases, denominador %s (%s)"
              % (n, r["cual"], r["n_con_clases"], r["denominador"], r["de_donde"]))
            if r["n_duplicadas"]:
                w("            (y %d fila(s) repetida(s) quitada(s): el fichero "
                  "lista %d en total)" % (r["n_duplicadas"], r["n_crudas"]))
            if r["denominador"] and r["n_con_clases"] > r["denominador"]:
                w("            AVISO: mas filas (%d) que denominador (%d). Se "
                  "publica y no se tapa." % (r["n_con_clases"], r["denominador"]))'''

VIEJO_D = '''    w("D) LAS DOS CIFRAS, PUBLICADAS JUNTAS, QUE ES LO QUE EL ENCARGO PIDE")
    w("   ANTES  (regla de la TAREA 5 de la vuelta 191): 6 de 43")
    w("   DESPUES (este lector):                         %d de %d"
      % (len(recuperados), len(cands)))'''

NUEVO_D = '''    w("D) EL COTEJO CONTRA LOS SEIS DE LA VUELTA 191, POR NOMBRE Y NO POR CIFRA")
    w("   (se leen de docs/loop/SALIDA_V191_T5_MARCA_CONTRA_DIFICULTAD.txt, que")
    w("    es su fichero, y no de la memoria)")
    prev = os.path.join(LOOP, "SALIDA_V191_T5_MARCA_CONTRA_DIFICULTAD.txt")
    seis, antes_cands = [], None
    if os.path.exists(prev):
        tp = io.open(prev, encoding="utf-8", errors="replace").read()
        for l in tp.replace(chr(13) + NL, NL).split(NL):
            ls = l.strip()
            if ls.startswith("ENTRA "):
                seis.append(ls.split()[1])
            m = re.match(r"^CIFRA candidatos:\\s*(\\d+)$", ls)
            if m:
                antes_cands = int(m.group(1))
    w("   CIFRA que entraban por la regla de la 191: %d" % len(seis))
    for n in seis:
        w("      %s" % n)
    w("   CIFRA candidatos que la 191 midio: %s" % antes_cands)
    nombres_rec = set(r["nombre"] for r in recuperados)
    siguen = [n for n in seis if n in nombres_rec]
    salen = [n for n in seis if n not in nombres_rec]
    nuevos = sorted(nombres_rec - set(seis))
    w("   SIGUEN DENTRO: %d (%s)" % (len(siguen), ", ".join(siguen) or "ninguno"))
    w("   SALEN: %d (%s)" % (len(salen), ", ".join(salen) or "ninguno"))
    w("      y salen porque este lector es MAS ESTRECHO, no mas ancho: exige las")
    w("      DOS clases Y el denominador, y la regla de la 191 se conformaba con")
    w("      el puesto de una discrepancia.")
    w("   ENTRAN QUE NO ESTABAN: %d (%s)"
      % (len(nuevos), ", ".join(nuevos) or "ninguno"))
    w("")
    w("E) LAS DOS CIFRAS, PUBLICADAS JUNTAS, QUE ES LO QUE EL ENCARGO PIDE")
    w("   ANTES  (regla de la TAREA 5 de la vuelta 191): %s de %s"
      % (len(seis), antes_cands))
    w("   DESPUES (este lector):                         %d de %d"
      % (len(recuperados), len(cands)))
    w("   Y EL DENOMINADOR DE LAS DOS CIFRAS NO ES EL MISMO, Y ESO SE DICE EN VEZ")
    w("   DE ESCONDERSE: la 191 midio sobre %s candidatos y hoy hay %d, porque"
      % (antes_cands, len(cands)))
    w("   ESTA MISMA VUELTA ha escrito ficheros con COTEJO en el nombre. De los")
    nacidos = [n for n in cands if "V192" in n.upper() or "v192" in n]
    w("   %d candidatos de hoy, %d nacieron en esta vuelta: %s"
      % (len(cands), len(nacidos), ", ".join(nacidos) or "ninguno"))
    w("   SIN ELLOS, el lector recupera %d de %d, que es la cifra comparable"
      % (len([r for r in recuperados if r["nombre"] not in nacidos]),
         len([c for c in cands if c not in nacidos])))'''

VIEJO_E = '''    w("E) LO QUE ESTA MEDICION NO HACE, Y ES EL RESTO DEL ENCARGO")'''
NUEVO_E = '''    w("F) LO QUE ESTA MEDICION NO HACE, Y ES EL RESTO DEL ENCARGO")'''


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    t = io.open(P, encoding="utf-8").read().replace(chr(13) + NL, NL)
    antes = len(t.encode("utf-8"))
    for nombre, viejo, nuevo in (("deduplicar + leer", VIEJO_LEER, NUEVO_LEER),
                                 ("el dict de leer", VIEJO_DICT, NUEVO_DICT),
                                 ("el aviso del bloque B", VIEJO_B, NUEVO_B),
                                 ("el cotejo contra los seis", VIEJO_D, NUEVO_D),
                                 ("la letra del ultimo bloque", VIEJO_E, NUEVO_E)):
        if nuevo in t:
            print("   YA ESTABA: %s" % nombre)
            continue
        if viejo not in t:
            print("   ROJO: no se encuentra el ancla de %s." % nombre)
            return 1
        t = t.replace(viejo, nuevo, 1)
        print("   aplicado: %s" % nombre)
    io.open(P, "w", encoding="utf-8", newline=NL).write(t)
    print("   lector_de_cotejos_viejos.py pasa de %d a %d bytes en disco"
          % (antes, len(t.encode("utf-8"))))
    import py_compile
    py_compile.compile(P, doraise=True)
    print("   COMPILA")
    return 0


if __name__ == "__main__":
    sys.exit(main())
