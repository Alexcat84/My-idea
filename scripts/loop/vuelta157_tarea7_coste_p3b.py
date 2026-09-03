# -*- coding: utf-8 -*-
"""vuelta157_tarea7_coste_p3b.py . TAREA 7 DE LA VUELTA 157.

EL COSTE DE LAS NUEVE SALIDAS DE LA P3b, MEDIDO UNA VEZ Y NO ADIVINADO
(adjudicacion 6.7 del acta 157).

QUE DECIDE ESTE INSTRUMENTO Y QUE NO. NO mete nada en
`verificar_mutaciones_viejas.py`: meter nueve scripts mas en cada cierre es una
decision de coste por vuelta que NO es del ejecutor. Lo que hace es CORRER LAS
NUEVE UNA VEZ, cronometrarlas por script, sellar su salida, decir si cada una
todavia MUERDE y publicar cuanto anadirian al cierre de cada vuelta.

LA NOMINA DE LAS NUEVE SALE DE UN COMPUTO, NO DE UNA LISTA TECLEADA: se leen las
fichas de `docs/plan/OPERACIONES.jsonl` con el MISMO patron de la P3b (extraido
del fichero que lo define, como hizo la vuelta 156) y se quedan las citas que la
bateria NO cubre por nombre.

Y AQUI HAY UN HALLAZGO QUE LA VUELTA 156 NO PODIA VER, PORQUE SOLO CONTABA:
LA CORRESPONDENCIA SALIDA-SCRIPT NO ES MECANICA. `SALIDA_V96_TAREA3_MUTACION.txt`
NO la escribe `vuelta96_tarea3_mutacion.py` (que no existe) sino
`vuelta96_tarea3_prueba_mutacion.py`. O sea que la regla de nombre que la 156
declaro como su limite NO SOLO SOBRE ESTIMA EL HUECO: es que ni siquiera sirve
para ENCONTRAR al productor. Por eso aqui el productor SE BUSCA POR EL TEXTO QUE
IMPRIME:

  para cada salida se toman sus lineas mas largas y menos genericas, y se busca
  cual de los `.py` del repo trae ESA LINEA como literal. La primera linea que
  senale a EXACTAMENTE UN script gana. Si ninguna desambigua, la salida se
  publica como PRODUCTOR AMBIGUO o NO ENCONTRADO, y NO SE ADIVINA.

CADA CORRIDA SE MIDE ENTERA: exit code, segundos cronometrados, y LOS FICHEROS
QUE ESCRIBE EN docs/loop/, computados por mtime igual que hace la bateria. Eso
ultimo importa para la decision: un script que re escribe salidas selladas
tendria que entrar con su cotejo de reproducibilidad, no a secas.

USO:  python scripts/loop/vuelta157_tarea7_coste_p3b.py
"""
import io
import json
import os
import re
import subprocess
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import verificar_mutaciones_viejas as B  # noqa: E402

OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
LOOP = os.path.join(RAIZ, "docs", "loop")
SCRIPTS = os.path.join(RAIZ, "scripts")

SEPARADOR = re.compile(r"^[=\-_ ]*$")


def patron_de_la_p3b():
    fuente = io.open(os.path.join(RAIZ, "scripts", "loop",
                                  "vuelta150_3_relectura_expediente.py"),
                     encoding="utf-8").read()
    marca = "PATRON_CASO_POSITIVO = re.compile("
    i = fuente.index(marca)
    j = fuente.index(chr(10) + chr(10), i)
    entorno = {"re": re}
    exec(fuente[i:j], entorno)
    return entorno["PATRON_CASO_POSITIVO"]


PATRON_CASO_POSITIVO = patron_de_la_p3b()


def citas_de(f):
    partes = []
    for k in ("verificacion", "evidencia"):
        v = f.get(k)
        partes += v if isinstance(v, list) else [str(v or "")]
    for k in ("nota", "adjudicacion"):
        partes.append(str(f.get(k) or ""))
    return sorted(set(PATRON_CASO_POSITIVO.findall(" ".join(partes))))


def normalizar_salida(nombre):
    n = nombre.lower()
    if n.startswith("salida_"):
        n = n[len("salida_"):]
    if n.endswith(".txt"):
        n = n[:-4]
    return n


def todos_los_py():
    out = []
    for base, dirs, files in os.walk(SCRIPTS):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for n in sorted(files):
            if n.endswith(".py"):
                out.append(os.path.join(base, n))
    return out


def buscar_productor(salida, fuentes):
    """El script que IMPRIME esa salida, buscado por su propio texto."""
    ruta = os.path.join(LOOP, salida)
    if not os.path.exists(ruta):
        return None, "LA SALIDA NO ESTA EN EL ARBOL", []
    lineas = io.open(ruta, encoding="utf-8", errors="replace").read().splitlines()
    cand = [l.strip() for l in lineas
            if len(l.strip()) >= 40 and not SEPARADOR.match(l.strip())]
    cand.sort(key=len, reverse=True)
    for l in cand[:40]:
        golpes = [r for r, txt in fuentes.items() if l in txt]
        if len(golpes) == 1:
            return golpes[0], "POR SU TEXTO", [l]
        if len(golpes) > 1:
            continue
    for l in cand[:40]:
        golpes = [r for r, txt in fuentes.items() if l in txt]
        if len(golpes) > 1:
            return None, "PRODUCTOR AMBIGUO (%d candidatos)" % len(golpes), golpes
    return None, "PRODUCTOR NO ENCONTRADO", []


def estado_txt():
    out = {}
    for n in sorted(os.listdir(LOOP)):
        if n.endswith(".txt") and os.path.isfile(os.path.join(LOOP, n)):
            out[n] = os.stat(os.path.join(LOOP, n)).st_mtime_ns
    return out


def main():
    F = [json.loads(x) for x in io.open(OPS, encoding="utf-8") if x.strip()]
    stems = {s[:-3].lower() for s, _a in B.VIEJAS}

    print("=" * 100)
    print("VUELTA 157, TAREA 7: EL COSTE DE LAS NUEVE SALIDAS DE LA P3b, CRONOMETRADO")
    print("=" * 100)
    print("")

    nueve, por_ficha = [], []
    for f in sorted(F, key=lambda x: x["id_op"]):
        cit = [c for c in citas_de(f) if os.path.exists(os.path.join(LOOP, c))]
        no = [c for c in cit if normalizar_salida(c) not in stems]
        if no:
            por_ficha.append((f["id_op"], no))
            nueve += no
    nueve = sorted(set(nueve))
    print("A) LA NOMINA, RECOMPUTADA DEL EXPEDIENTE (no tecleada)")
    print("   CIFRA fichas con al menos una cita que la bateria no cubre: %d" % len(por_ficha))
    for id_op, cs in por_ficha:
        print("      %-10s %s" % (id_op, ", ".join(cs)))
    print("   CIFRA salidas distintas sin respaldo en la bateria: %d" % len(nueve))
    print("")

    print("B) EL PRODUCTOR DE CADA UNA, BUSCADO POR SU PROPIO TEXTO")
    fuentes = {}
    for r in todos_los_py():
        try:
            fuentes[r] = io.open(r, encoding="utf-8", errors="replace").read()
        except OSError:
            pass
    print("   CIFRA ficheros .py barridos: %d" % len(fuentes))
    plan = []
    for s in nueve:
        ruta, como, extra = buscar_productor(s, fuentes)
        rel = os.path.relpath(ruta, RAIZ).replace("\\", "/") if ruta else "(ninguno)"
        print("   %-42s %s" % (s, rel))
        print("        %s" % como)
        if ruta is None and extra:
            for g in extra[:4]:
                print("          candidato: %s" % os.path.relpath(g, RAIZ).replace("\\", "/"))
        plan.append((s, ruta, como))
    hallados = [p for p in plan if p[1]]
    print("   CIFRA salidas con productor identificado: %d de %d" % (len(hallados), len(nueve)))
    print("")

    print("C) LAS CORRIDAS, UNA VEZ CADA UNA Y CRONOMETRADAS")
    print("   %-42s %-6s %-9s %s" % ("script", "exit", "segundos", "muerde"))
    filas, total = [], 0.0
    for s, ruta, _c in plan:
        if not ruta:
            print("   %-42s %-6s %-9s %s" % (os.path.basename(s), "-", "-", "SIN PRODUCTOR"))
            filas.append((s, None, None, None, []))
            continue
        rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
        antes = estado_txt()
        t0 = time.time()
        r = subprocess.run([sys.executable, rel], cwd=RAIZ, capture_output=True)
        seg = time.time() - t0
        total += seg
        despues = estado_txt()
        escritos = sorted(n for n, mt in despues.items()
                          if n not in antes or antes[n] != mt)
        muerde = "SI" if r.returncode == 0 else "NO (exit %d)" % r.returncode
        print("   %-42s %-6d %-9.2f %s" % (os.path.basename(rel), r.returncode, seg, muerde))
        if escritos:
            print("        escribe en docs/loop/: %s" % ", ".join(escritos))
        else:
            print("        escribe en docs/loop/: nada")
        primera = ""
        for l in r.stdout.decode("utf-8", "replace").splitlines():
            if l.strip():
                primera = l.strip()[:120]
                break
        if primera:
            print("        primera linea: %s" % primera)
        if r.returncode != 0:
            # LA QUE NO MUERDE SE EXPLICA, NO SE DEJA EN UN NUMERO. Se pegan sus
            # ultimas lineas utiles, que es donde estos scripts ponen su veredicto.
            utiles = [l.rstrip() for l in r.stdout.decode("utf-8", "replace").splitlines()
                      if l.strip()]
            for l in utiles[-3:]:
                print("        veredicto: %s" % l.strip()[:150])
        filas.append((s, rel, r.returncode, seg, escritos))
    print("")

    corridas = [f for f in filas if f[2] is not None]
    muerden = [f for f in corridas if f[2] == 0]
    escriben = [f for f in corridas if f[4]]
    print("D) EL COSTE, QUE ES LO QUE EL ACTA PIDE TENER DELANTE")
    print("   CIFRA salidas de la P3b sin respaldo en la bateria: %d" % len(nueve))
    print("   CIFRA de esas con productor identificado y corrido: %d" % len(corridas))
    print("   CIFRA de las corridas que TODAVIA MUERDEN (exit 0): %d" % len(muerden))
    print("   CIFRA de las corridas que ESCRIBEN en docs/loop/: %d" % len(escriben))
    print("   CIFRA segundos de UNA corrida de todas: %.2f segundos" % total)
    print("   CIFRA segundos que anadirian al cierre de cada vuelta: %.2f segundos"
          % (total * 2))
    print("      (la bateria corre CADA mutacion DOS VECES para cotejar que su salida")
    print("       sellada se repite, asi que el coste de entrada es el doble del de una")
    print("       corrida suelta. La cifra de arriba ya lleva ese doble.)")
    print("")
    print("E) LO QUE ESTA TAREA NO HACE, Y SE DICE")
    print("   NO mete ninguna de estas en verificar_mutaciones_viejas.py. La cifra se")
    print("   publica y se trae. Y mientras no entren, la P3b de esas fichas queda")
    print("   declarada JUNTO A LA FUNCION como PROXY SIN RESPALDO EFECTIVO, que es lo")
    print("   que la TAREA 1 de esta vuelta ya escribio con la adjudicacion 6.7.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
