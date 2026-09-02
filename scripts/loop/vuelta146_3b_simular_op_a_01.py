# -*- coding: utf-8 -*-
r"""vuelta146_3b_simular_op_a_01.py . LA SIMULACION PREVIA DE `OP-A-01`
(TAREA 3.b de la vuelta 146), SOBRE COPIA EN MEMORIA Y CON CERO ESCRITURAS.

POR QUE VA PRIMERO. El encargo lo pide con esas palabras ("CON SIMULACION
PREVIA SOBRE COPIA EN MEMORIA, CASO POSITIVO Y CASO ROJO POR MUTACION SOBRE UNA
VARIABLE QUE EL CODIGO COMPUTE, nunca sobre un literal"). Se mide lo que los
controles dirian ANTES de cablearlos, para que cablearlos no pueda ser una
sorpresa.

EL ALCANCE, Y NI UNA COSA MAS. La `verificacion` de `OP-A-01` tiene TRES
entradas y son estas tres, citadas verbatim de `docs/plan/OPERACIONES.jsonl`:

  (1) "todo nodo que entre declarando MAS DE UNA fuente pasa por la
      comprobacion posicional"
  (2) "el campo fuente se valida contra una lista CANONICA de libros: hoy no
      existe y sin ella el control es fragil"
  (3) "Gate 0 rechaza un nodo cuyo segundo libro no aparece en ningun paso"

QUE ES LA COMPROBACION POSICIONAL, y no se inventa: `BANCO_DEL_PLAN.md` P.2,
"el orden dentro del campo `fuente` lleva informacion: el primero es de donde
salio el nodo, y lo que viene detras es lo que se le pego". La `nota` de la
ficha dice para que le sirve a la aduana: "el plan repara 67 nodos una vez; la
aduana impide que entre el sesenta y ocho, y para eso le basta con mirar el
ORDEN del campo fuente, que es lo mas barato que se puede mirar".

COMO SE HACE MECANICO, ESCRITO ANTES DE CORRERLO:

  (1) NOMINA ADJUDICADA. Todo nodo vivo que declare MAS DE UNA fuente tiene que
      estar en `dataset/metadata/aduana_fuente_multiple.json` Y CON LA MISMA
      LISTA DE DECLARACIONES. Un nodo nuevo que entre con dos libros sin
      adjudicar es ROJO, y anadirle en silencio un segundo libro a un nodo ya
      adjudicado tambien, porque la lista se coteja entera y en orden. Eso es
      exactamente "impedir que entre el sesenta y ocho".
  (2) No se reimplementa nada: se llama a `verificar_fuente_canonico.verificar`,
      que es el criterio de HECHO de la fase 08 y ya existe. Dos versiones de la
      misma comprobacion serian la averia que esta campana persigue.
  (3) SE INSTALA LA MITAD SANA Y SE DICE CUAL ES LA OTRA. Un nodo que declara
      mas de un libro y NO TIENE NI UN `pasos_accionables` no puede tener un
      paso donde aparezca su segundo libro: ese caso es mecanico, no admite
      juicio y no puede dar un falso rojo. LA OTRA MITAD (decidir si el
      MATERIAL de un paso concreto viene del segundo libro) PIDE UNA
      ATRIBUCION POR PASO QUE EL ESQUEMA NO TIENE: los pasos son texto libre
      sin campo de fuente. NO SE ADIVINA (`EJECUTOR.md` 11) y NO SE FABRICA UNA
      HEURISTICA DE PARECIDO que decidiria por semejanza lo que solo decide una
      lectura. Queda PENDIENTE DE DOCTRINA, dicho en voz alta aqui, en la vara
      y en el reporte, y respaldado por un barrido exhaustivo sellado.

USO:
  python scripts/loop/vuelta146_3b_simular_op_a_01.py
"""
import glob
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
NOMINA = os.path.join(RAIZ, "dataset", "metadata", "aduana_fuente_multiple.json")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verificar_fuente_canonico import verificar as verificar_canonico  # noqa: E402

SEP = " | "


def cargar_vivos():
    """(id, declaraciones, tiene_pasos) de cada nodo vivo. Copia en memoria: no
    se escribe una sola letra en disco."""
    out = []
    for p in sorted(glob.glob(os.path.join(NODOS, "*.json"))):
        d = json.loads(io.open(p, encoding="utf-8").read())
        if d.get("deprecado"):
            continue
        nid = d.get("node_id") or os.path.splitext(os.path.basename(p))[0]
        f = d.get("fuente")
        ds = [x.strip() for x in str(f).split(SEP) if x.strip()] if isinstance(f, str) else []
        out.append((nid, ds, bool(d.get("pasos_accionables"))))
    return out


def cargar_nomina():
    if not os.path.exists(NOMINA):
        return None
    d = json.loads(io.open(NOMINA, encoding="utf-8").read())
    return {x["node_id"]: list(x["fuente"]) for x in d.get("adjudicados", [])}


def control_posicional(vivos, nomina):
    """(1) La comprobacion posicional. Devuelve la lista de incumplimientos:
    (id, motivo). Si `nomina` es None todavia no esta cableada y se devuelve el
    censo de candidatos, que es lo que la simulacion quiere ver primero."""
    multiples = [(nid, ds) for nid, ds, _ in vivos if len(ds) > 1]
    if nomina is None:
        return multiples, None
    fallos = []
    for nid, ds in multiples:
        if nid not in nomina:
            fallos.append((nid, "declara %d fuentes y NO esta en la nomina adjudicada" % len(ds)))
        elif nomina[nid] != ds:
            fallos.append((nid, "declara %r y la nomina adjudicada dice %r" % (ds, nomina[nid])))
    return multiples, fallos


def control_segundo_libro(vivos):
    """(3), la mitad sana: un nodo con mas de un libro y sin ni un paso no
    puede tener un paso donde aparezca su segundo libro."""
    return [nid for nid, ds, tiene in vivos if len(ds) > 1 and not tiene]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    vivos = cargar_vivos()
    nomina = cargar_nomina()

    print("SIMULACION DE OP-A-01 SOBRE COPIA EN MEMORIA | vuelta 146, TAREA 3.b")
    print("=" * 78)
    print("nodos vivos leidos: %d" % len(vivos))

    multiples, fallos = control_posicional(vivos, nomina)
    print("")
    print("(1) COMPROBACION POSICIONAL (P.2: el orden del campo fuente lleva informacion)")
    print("  nodos vivos que declaran MAS DE UNA fuente: %d" % len(multiples))
    for nid, ds in multiples:
        print("     %s" % nid)
        for i, x in enumerate(ds):
            print("        [%d] %s" % (i, x))
    if nomina is None:
        print("  NOMINA ADJUDICADA: todavia NO existe %s" % os.path.relpath(NOMINA, RAIZ))
        print("  -> el control diria ROJO sobre los %d de arriba hasta que se selle la nomina"
              % len(multiples))
    else:
        print("  NOMINA ADJUDICADA: %d nodo(s) en %s" % (len(nomina), os.path.relpath(NOMINA, RAIZ)))
        print("  incumplimientos: %d" % len(fallos))
        for nid, motivo in fallos:
            print("     %s: %s" % (nid, motivo))

    ok_canon, incump = verificar_canonico()
    print("")
    print("(2) CAMPO FUENTE CONTRA LA LISTA CANONICA (se reusa verificar_fuente_canonico)")
    print("  veredicto: %s | incumplimientos: %d" % ("VERDE" if ok_canon else "ROJO", len(incump)))
    for nid, g, m in incump[:10]:
        print("     %s: %r %s" % (nid, g, m))

    sin_pasos = control_segundo_libro(vivos)
    print("")
    print("(3) EL SEGUNDO LIBRO NO APARECE EN NINGUN PASO, MITAD SANA")
    print("  nodos con mas de un libro y CERO pasos_accionables: %d" % len(sin_pasos))
    for nid in sin_pasos:
        print("     %s" % nid)
    print("  LA OTRA MITAD NO SE INSTALA Y SE DICE POR QUE: atribuir el MATERIAL de un")
    print("  paso a un libro pide una atribucion POR PASO que el esquema no tiene.")
    print("  PENDIENTE DE DOCTRINA, no adivinada.")

    print("")
    print("CIFRA nodos vivos con mas de una fuente: %d nodos" % len(multiples))
    print("CIFRA nodos con mas de un libro y sin pasos: %d nodos" % len(sin_pasos))
    print("CIFRA incumplimientos canonicos: %d nodos" % len(incump))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
