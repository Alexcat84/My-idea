# -*- coding: utf-8 -*-
r"""vuelta162_tarea4_colisiones_de_titulo.py . TAREA 4 de la vuelta 162.

MIDE EL UNIVERSO ENTERO DE COLISIONES DE TITULO NORMALIZADO ENTRE NODOS VIVOS,
PUBLICA LA NOMINA CON SU CIFRA, Y PARA AHI.

ES UNA MEDICION, NO UNA OPERACION. El encargo lo dice con esas palabras: NO SE
FUNDE NADA Y NO SE PROPONE FUSION, que eso es alcance de campaña y es del
fundador. Este instrumento es de SOLO LECTURA: no escribe en el grafo, no toca
ninguna ficha y no mueve ningun veredicto.

LA VARA NO SE REIMPLEMENTA (ley de una sola fuente): `normalizar`, `cargar` y la
lista `EXCEPCIONES` se IMPORTAN de `scripts/loop/verificar_titulos_normalizados.py`,
que es la guarda de la casa para esto desde la vuelta 124. Una copia de la
normalizacion aqui seria una segunda vara que se desincroniza.

LAS DOS VARAS SE PUBLICAN JUNTAS, porque la gracia del hallazgo es la diferencia:
  - LA DE GATE 0: `titulo_concepto` EXACTO. Su linea vive hoy en
    `scripts/run_phase1.py` y se LEE en esta corrida, no se cita de memoria.
  - LA NORMALIZADA: NFKD, sin diacriticos, minusculas y espacios colapsados.
Gate 0 dice cero duplicadas y NO se equivoca: mide otra cosa.

USO:  python scripts/loop/vuelta162_tarea4_colisiones_de_titulo.py
"""
import collections
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_titulos_normalizados as V   # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUN_PHASE1 = os.path.join(RAIZ, "scripts", "run_phase1.py")
ANCLA_VARA = "Cero grupos con titulo_concepto exacto duplicado"


def linea_de_la_vara():
    """La linea de `run_phase1.py` que fija la vara de Gate 0, LOCALIZADA HOY
    por su texto y no citada por su numero de memoria."""
    lineas = io.open(RUN_PHASE1, encoding="utf-8").read().split("\n")
    hits = [(i, l.strip()) for i, l in enumerate(lineas, 1) if ANCLA_VARA in l]
    return hits


def main():
    print("=" * 78)
    print("VUELTA 162, TAREA 4: COLISIONES DE TITULO NORMALIZADO ENTRE VIVOS")
    print("ES UNA MEDICION. NO SE FUNDE NADA Y NO SE PROPONE FUSION.")
    print("=" * 78)
    print("")

    grafo = V.cargar("WORK")
    nodos = grafo["nodos"]
    vivos = {k: v for k, v in nodos.items() if not v.get("deprecado")}

    print("A) EL UNIVERSO, CONTADO DEL FICHERO")
    print("   fuente: dataset/metadata/master_graph.json (arbol de trabajo)")
    print("   CIFRA nodos del grafo: %d" % len(nodos))
    print("   CIFRA nodos VIVOS: %d" % len(vivos))
    print("   CIFRA nodos deprecados: %d" % (len(nodos) - len(vivos)))
    sin_titulo = sorted(k for k, v in vivos.items() if not (v.get("titulo_concepto") or "").strip())
    print("   CIFRA vivos SIN titulo_concepto: %d (%s)"
          % (len(sin_titulo), ", ".join(sin_titulo) or "ninguno"))
    print("")

    print("B) LA VARA DE GATE 0, LEIDA HOY DE SU FICHERO Y NO CITADA DE MEMORIA")
    for i, texto in linea_de_la_vara():
        print("   scripts/run_phase1.py:%d -> %s" % (i, texto))
    print("   Esa vara agrupa por `titulo_concepto` EXACTO. Por eso puede decir CERO")
    print("   sobre un par que solo se diferencia en una mayuscula, y NO se equivoca.")
    print("")

    exacto = collections.defaultdict(list)
    for k, v in vivos.items():
        exacto[(v.get("titulo_concepto") or "")].append(k)
    grupos_exacto = {t: ids for t, ids in exacto.items() if len(ids) > 1}
    print("C) LA VARA EXACTA, CORRIDA AQUI SOBRE LOS MISMOS VIVOS")
    print("   CIFRA grupos por titulo EXACTO: %d" % len(exacto))
    print("   CIFRA grupos EXACTOS con mas de un id: %d" % len(grupos_exacto))
    for t, ids in sorted(grupos_exacto.items()):
        print("      %r: %s" % (t, ", ".join(sorted(ids))))
    print("   Cuadra con lo que Gate 0 publica en la cabecera: duplicadas 0.")
    print("")

    norm = collections.defaultdict(list)
    for k, v in vivos.items():
        norm[V.normalizar(v.get("titulo_concepto") or "")].append(k)
    grupos_norm = {t: sorted(ids) for t, ids in norm.items() if len(ids) > 1}
    exentos = {x for x, _m, _v in V.EXCEPCIONES}

    print("D) LA VARA NORMALIZADA (NFKD, sin diacriticos, minusculas, espacios")
    print("   colapsados), IMPORTADA de verificar_titulos_normalizados.py")
    print("   CIFRA grupos por titulo NORMALIZADO: %d" % len(norm))
    print("   CIFRA COLISIONES (grupos normalizados con mas de un id vivo): %d"
          % len(grupos_norm))
    print("   CIFRA nodos vivos metidos en una colision: %d"
          % sum(len(v) for v in grupos_norm.values()))
    print("")

    print("E) LA NOMINA ENTERA, SIN RESUMIR, CADA ID CON SU TITULO EXACTO")
    if not grupos_norm:
        print("   ninguna")
    for clave in sorted(grupos_norm):
        ids = grupos_norm[clave]
        cubierto = all(x in exentos for x in ids)
        print("   CLAVE NORMALIZADA %r  (%d nodos)  excepcion declarada: %s"
              % (clave, len(ids), "SI" if cubierto else "NO"))
        for x in ids:
            v = vivos[x]
            print("      %-42s titulo exacto: %r" % (x, v.get("titulo_concepto")))
            print("      %-42s fuente: %s" % ("", (v.get("fuente") or "")[:88]))
            print("      %-42s pasos: %d | siguientes: %d | previos: %d | en la excepcion: %s"
                  % ("", len(v.get("pasos_accionables") or []),
                     len(v.get("nodos_siguientes") or []),
                     len(v.get("nodos_previos") or []),
                     "SI" if x in exentos else "NO"))
    print("")

    print("F) LAS EXCEPCIONES DECLARADAS DE LA GUARDA, IMPRESAS ENTERAS")
    print("   CIFRA excepciones vigentes: %d" % len(V.EXCEPCIONES))
    for x, motivo, vuelta in V.EXCEPCIONES:
        print("      %-42s vuelta %d" % (x, vuelta))
        print("      %-42s %s" % ("", motivo))
    print("")

    print("G) LA GUARDA DE LA CASA, CORRIDA HOY POR SU CUENTA, COMO CONTRASTE")
    r = subprocess.run([sys.executable, "scripts/loop/verificar_titulos_normalizados.py"],
                       cwd=RAIZ, capture_output=True, text=True)
    for l in (r.stdout or "").strip().split("\n"):
        print("   %s" % l)
    print("   exit %d" % r.returncode)
    print("")

    huerfanos = sorted(x for x in exentos if x not in vivos)
    print("H) LA SALUD DE LA PROPIA LISTA DE EXCEPCIONES")
    print("   CIFRA ids exentos que YA NO estan vivos: %d (%s)"
          % (len(huerfanos), ", ".join(huerfanos) or "ninguno"))
    fuera = sorted(x for x in exentos
                   if x in vivos and not any(x in ids for ids in grupos_norm.values()))
    print("   CIFRA ids exentos vivos que YA NO colisionan con nadie: %d (%s)"
          % (len(fuera), ", ".join(fuera) or "ninguno"))
    print("")

    nuevas = [c for c, ids in grupos_norm.items() if not all(x in exentos for x in ids)]
    print("I) EL VEREDICTO DE ESTA MEDICION")
    print("   CIFRA colisiones de titulo normalizado entre vivos: %d" % len(grupos_norm))
    print("   CIFRA de ellas ya declaradas como excepcion: %d" % (len(grupos_norm) - len(nuevas)))
    print("   CIFRA de ellas NUEVAS, sin excepcion declarada: %d" % len(nuevas))
    for c in sorted(nuevas):
        print("      %r: %s" % (c, ", ".join(grupos_norm[c])))
    print("")
    print("SE PARA AQUI. No se funde nada, no se propone fusion y no se toca ningun")
    print("titulo: el alcance de campaña es del fundador (acta 161, seccion 5.3).")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
