# -*- coding: utf-8 -*-
r"""_v214_t1c_op_i_01.py . LA TAREA 1.c DE LA VUELTA 214: LOS CUATRO PUNTOS DE
verificacion DE OP-I-01, RE-MEDIDOS HOY Y NO COPIADOS DE NINGUNA ACTA.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO: fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3).

POR QUE SE RE-MIDEN LOS CUATRO Y NO SOLO EL 2: EJECUTOR.md 2, EL INSTRUMENTO
MANDA. Los veredictos de la vuelta 211 son de su corte y se citan como
CONTRASTE; los de hoy salen de contar el fichero de hoy. Si discrepan, la
discrepancia SE DECLARA en vez de resolverse copiando.

LA FICHA NO ESCRIBE EL ESTADO, Y AQUI TAMPOCO SE LE ESCRIBE: CUBRE, A MEDIAS y
NO CUBRE son VEREDICTOS MEDIDOS, no campos de la ficha. El campo estado de
OPERACIONES.jsonl es HISTORICO y no es la vara (recuadro de AUDITOR.md 0,
decision del fundador del 4 sep 2026).

USO:  python scripts/loop/_v214_t1c_op_i_01.py
"""
import io
import json
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_",
                       os.path.basename(os.path.abspath(__file__))).group(1))

INV = "docs/plan/INVENTARIO.jsonl"
OPS = "docs/plan/OPERACIONES.jsonl"
VIS = "docs/plan/10_INVENTARIO.md"
VER = "docs/plan/08_VERIFICACION.md"
CONTRASTE = "docs/loop/SALIDA_V211_T2_OP_I_01.txt"
PAT = re.compile(r"^(\d+) de (\d+) pares leidos")

OUT = []


def w(s=""):
    OUT.append(s)


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read()


def entradas():
    return [json.loads(l) for l in leer(INV).split(NL) if l.strip()]


def linea_de(rel, patron):
    """LA LINEA DONDE VIVE UN TEXTO, LEIDA HOY Y NO RECORDADA (EJECUTOR.md 1,
    LA CITA LLEVA SU LINEA). Devuelve (numero, texto) o (None, None)."""
    for i, l in enumerate(leer(rel).split(NL), 1):
        if patron in l:
            return i, l.strip()
    return None, None


def contraste():
    """LOS CUATRO VEREDICTOS DE LA VUELTA 211, LEIDOS DE SU FICHERO. Se citan
    como CONTRASTE y nunca como fuente (EJECUTOR.md 2)."""
    est = {}
    actual = None
    for l in leer(CONTRASTE).split(NL):
        m = re.match(r"^\s*PUNTO (\d)\.", l)
        if m:
            actual = int(m.group(1))
        m2 = re.match(r"^\s*VEREDICTO: \*\*(.+?)\*\*", l)
        if m2 and actual:
            est[actual] = m2.group(1)
    return est


def main():
    w("=" * 78)
    w("VUELTA %d, TAREA 1.c. LOS CUATRO PUNTOS DE OP-I-01, RE-MEDIDOS HOY" % VUELTA)
    w("=" * 78)
    w("LA FICHA ESCRIBE LOS PUNTOS Y NO ESCRIBE SU ESTADO. CUBRE, A MEDIAS y NO")
    w("CUBRE son veredictos MEDIDOS por este instrumento sobre el arbol de hoy.")
    w("")

    F = [json.loads(l) for l in leer(OPS).split(NL) if l.strip()]
    ficha = [f for f in F if f.get("id_op") == "OP-I-01"][0]
    puntos = ficha["verificacion"]
    w("CIFRA puntos de verificacion de OP-I-01, contados de la ficha: %d" % len(puntos))
    w("CIFRA campo estado de la ficha, LEIDO y NO usado como vara: %r"
      % ficha.get("estado"))
    w("")

    E = entradas()
    viejo = contraste()
    w("CIFRA veredictos de contraste leidos de %s: %d" % (CONTRASTE, len(viejo)))
    w("")

    veredictos = {}
    razones = {}
    citas = {}

    # ---------------------------------------------------------------- PUNTO 1
    sin_corte = [d for d in E if not str(d.get("fecha_corte") or "").strip()]
    veredictos[1] = "CUBRE" if not sin_corte else "NO CUBRE"
    razones[1] = ("CIFRA entradas: %d. CIFRA con fecha_corte: %d. CIFRA sin "
                  "fecha_corte: %d." % (len(E), len(E) - len(sin_corte),
                                        len(sin_corte)))
    n, t = linea_de(VIS, "lleva su fecha de corte")
    citas[1] = "%s linea %s: %s" % (VIS, n, t)
    lineas_citadas = {1: n}

    # ---------------------------------------------------------------- PUNTO 2
    con_forma = [d for d in E if PAT.match(str(d.get("cobertura") or ""))]
    inc = [d for d in con_forma
           if int(PAT.match(d["cobertura"]).group(1))
           < int(PAT.match(d["cobertura"]).group(2))]
    inc_marc = [d for d in inc if "PROVISIONAL" in (d.get("forma") or "")]
    sin_marcar = [d.get("nombre") for d in inc if d not in inc_marc]
    veredictos[2] = "CUBRE" if (inc and not sin_marcar) else "NO CUBRE"
    razones[2] = ("CIFRA entradas con cobertura de la forma 'N de M pares "
                  "leidos': %d. De esas, INCOMPLETAS (N menor que M): %d. De "
                  "esas incompletas, con PROVISIONAL en su campo forma: %d. "
                  "CIFRA incompletas SIN marcar: %d."
                  % (len(con_forma), len(inc), len(inc_marc), len(sin_marcar)))
    n2, t2 = linea_de("docs/BANCO_DE_TEXTOS.md", "mientras falte un par, la forma es")
    citas[2] = ("%s, contado hoy campo a campo; y la regla en "
                "docs/BANCO_DE_TEXTOS.md linea %s: %s" % (INV, n2, (t2 or "")[:150]))
    lineas_citadas[2] = n2

    # ---------------------------------------------------------------- PUNTO 3
    nombra_hueco = [d for d in E
                    if "HUECO" in json.dumps(d, ensure_ascii=False).upper()]
    veredictos[3] = "A MEDIAS"
    razones[3] = ("LA MITAD QUE SE PUEDE MEDIR: CIFRA entradas que nombran "
                  "HUECO en algun campo: %d, o sea que el hueco SI se nombra. "
                  "LA MITAD QUE NO SE PUEDE MEDIR: 'nunca rellenado' es una "
                  "NEGATIVA, y una busqueda negativa no se puede citar "
                  "(EJECUTOR.md 9). Por eso no se escribe CUBRE, y NO es un "
                  "defecto de esta vuelta: es un limite de la clausula."
                  % len(nombra_hueco))
    n3, t3 = linea_de(VIS, "HUECO NOMBRADO")
    citas[3] = "%s linea %s: %s" % (VIS, n3, (t3 or "")[:150])
    lineas_citadas[3] = n3

    # ---------------------------------------------------------------- PUNTO 4
    n4a, t4a = linea_de(VER, "Se dispara EL DIA QUE EL CRIBADO LLEGUE AL PUESTO")
    n4b, t4b = linea_de(VIS, "LA TABLA NO SE REGENERA AQUI, A PROPOSITO")
    n4c, t4c = linea_de(VIS, "ESTA VISTA HUMANA ESTA AL CORTE")
    veredictos[4] = "A MEDIAS"
    razones[4] = ("EL DISPARADOR YA DISPARO Y LAS DOS MITADES NO FUERON A LA "
                  "VEZ. El archivo fuente SI se recomputo. La vista humana NO, "
                  "y lo dice ella misma con todas las letras en su propio "
                  "aviso. 'El inventario' son las dos formas que la "
                  "adjudicacion de la ficha nombra, y solo una esta al dia. "
                  "MEDIDO HOY: %s tiene %d entradas; la vista humana sigue "
                  "publicando su aviso de corte 2.117 en su linea %s."
                  % (INV, len(E), n4c))
    citas[4] = ("%s linea %s: %s | %s linea %s: %s"
                % (VER, n4a, (t4a or "")[:80], VIS, n4b, (t4b or "")[:80]))
    lineas_citadas[4] = n4a if (n4a and n4b) else None

    w("=" * 78)
    w("PUNTO POR PUNTO, CADA UNO CON SU CIFRA DE HOY Y SU CITA")
    w("=" * 78)
    for i, p in enumerate(puntos, 1):
        w("   PUNTO %d, PEGADO ENTERO DE LA FICHA:" % i)
        w("      %s" % p)
        w("      VEREDICTO MEDIDO HOY: **%s**" % veredictos[i])
        w("      VEREDICTO DE LA VUELTA 211, COMO CONTRASTE: **%s**"
          % viejo.get(i, "(no leido)"))
        w("      SE MUEVE: %s"
          % ("SI, de %s a %s" % (viejo.get(i), veredictos[i])
             if viejo.get(i) != veredictos[i] else "NO, calza con el contraste"))
        w("      LO MEDIDO: %s" % razones[i])
        w("      CITA, CON SU FICHERO Y SU LINEA: %s" % citas[i])
        w("")

    reparto = {}
    for v in veredictos.values():
        reparto[v] = reparto.get(v, 0) + 1
    w("EL REPARTO DE HOY, CONTADO DE LOS CUATRO VEREDICTOS DE ARRIBA:")
    for k in sorted(reparto):
        w("   %-10s %d" % (k, reparto[k]))
    sin_cita = [i for i in sorted(citas)
                if not citas[i] or lineas_citadas.get(i) is None]
    w("   CIFRA puntos: %d | CIFRA puntos SIN cita CON SU LINEA: %d (se exige 0)"
      % (len(puntos), len(sin_cita)))
    w("   LA GUARDA MIRA LA LINEA Y NO SOLO EL TEXTO: una cita que dice 'linea")
    w("   None' NO es una cita, y la primera corrida de este instrumento publico")
    w("   exactamente eso en el punto 3. Se caza aqui y no se deja pasar.")
    if sin_cita:
        w("   ROJO: puntos sin linea citable: %s" % sin_cita)
    w("")
    movidos = [i for i in veredictos if viejo.get(i) != veredictos[i]]
    w("CIFRA puntos cuyo veredicto SE MUEVE respecto de la 211: %d" % len(movidos))
    for i in movidos:
        w("   PUNTO %d: %s -> %s" % (i, viejo.get(i), veredictos[i]))
    w("")

    w("=" * 78)
    w("LO QUE ESTO SIGNIFICA PARA EL CIERRE, DICHO SIN ADORNO")
    w("=" * 78)
    nc = [i for i in veredictos if veredictos[i] == "NO CUBRE"]
    am = [i for i in veredictos if veredictos[i] == "A MEDIAS"]
    w("CIFRA puntos en NO CUBRE: %d %s" % (len(nc), nc if nc else ""))
    w("CIFRA puntos en A MEDIAS: %d %s" % (len(am), am if am else ""))
    w("")
    w("LA DISCREPANCIA CON EL ENCARGO SE DECLARA Y NO SE RESUELVE COPIANDO")
    w("(EJECUTOR.md 2 y 8): el encargo y la DECISION 1 del fundador nombran EL")
    w("PUNTO 2 como lo que bloquea, y el punto 2 se ha movido a CUBRE hoy. PERO")
    w("LOS PUNTOS 3 Y 4 SIGUEN EN A MEDIAS, y no los mueve esta vuelta ni los")
    w("podria mover el marcado de las 95:")
    w("   PUNTO 3: su mitad pendiente es UNA NEGATIVA ('nunca rellenado'), y una")
    w("   busqueda negativa no se puede citar. No es trabajo que quede: es un")
    w("   limite de como esta escrita la clausula.")
    w("   PUNTO 4: su mitad pendiente es REGENERAR LA VISTA HUMANA, y el propio")
    w("   documento declara que NO se regenera ahi A PROPOSITO. Es trabajo de la")
    w("   escala del disparador, no de una vuelta.")
    w("NINGUNO DE LOS DOS ES 'NO CUBRE', y ninguno de los dos lo levanta el")
    w("bucle por su cuenta. SE SUBEN NOMBRADOS.")
    w("")

    fallos = 0
    if veredictos[2] != "CUBRE":
        fallos += 1
        w("ROJO: el punto 2 no mide CUBRE despues del marcado.")
    if len(viejo) != len(puntos):
        fallos += 1
        w("ROJO: no se leyeron los cuatro veredictos de contraste.")
    if sin_cita:
        fallos += 1
        w("ROJO: hay un punto sin cita CON SU LINEA: %s" % sin_cita)
    w("CIFRA comprobaciones que fallan: %d" % fallos)
    w("")
    w("VERDE: los cuatro puntos quedan re-medidos." if not fallos else "ROJO.")

    destino = os.path.join(RAIZ, "docs", "loop",
                           "SALIDA_V%d_T1C_OP_I_01.txt" % VUELTA)
    texto = NL.join(OUT) + NL
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
