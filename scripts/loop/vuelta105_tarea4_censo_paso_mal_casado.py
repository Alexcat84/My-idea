# -*- coding: utf-8 -*-
r"""vuelta105_tarea4_censo_paso_mal_casado.py . VUELTA 105, TAREA 4.2: EL
CENSO DE LA ESPECIE DEL 46 (encargo del auditor, acta de la vuelta 104,
seccion "Y EL 46 NO ES DISENO, ES INSTRUMENTO").

QUE MIDE. Barre la `razon` de las CUATRO filas de OP-E-03
(`docs/plan/OP_E_03_LECTURA_TRAMO{1,2,3,4}_V9{6,7,8,9}.jsonl`) buscando la
NOTA DE PASO MAL CASADO: el patron literal "el barrido cas[o|a] el paso N",
donde N es el numero del paso que el barrido cito, seguido en la misma razon
de una correccion a un paso DISTINTO (la especie exacta del par 46, "el
barrido caso el paso 1 y el hijo ejecuta en realidad el paso 2"). NO busca
"FALSO AMIGO" ni "casado por el objeto no la accion" ni ninguna otra especie
de discrepancia: esas son razones de por que la DIRECCION no se sostiene,
no de que el NUMERO DE PASO citado este mal.

SALIDA: una linea por puesto encontrado, con tramo, puesto_tramo, madre,
hijo y el fragmento literal de la razon que dispara el patron. Exit 0
siempre (es censo, no guarda): la mecanica de ROJO vive en el consumidor
(vuelta105_tarea4_re_barrido_satelite.py), que se niega a emitir veredicto
sobre un puesto que este censo nombra.

USO:
  python scripts/loop/vuelta105_tarea4_censo_paso_mal_casado.py
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMOS = [
    ("tramo1", os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl")),
    ("tramo2", os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl")),
    ("tramo3", os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO3_V98.jsonl")),
    ("tramo4", os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO4_V99.jsonl")),
]

RE_PASO_MAL_CASADO = re.compile(r"el barrido cas\w* el paso\s*\d+", re.IGNORECASE)


def nota_paso_mal_casado(razon):
    """Devuelve el fragmento (30 caracteres antes, 150 despues) si RAZON trae
    la nota de paso mal casado; None si no la trae."""
    m = RE_PASO_MAL_CASADO.search(razon or "")
    if not m:
        return None
    ini = max(0, m.start() - 30)
    fin = min(len(razon), m.end() + 150)
    return razon[ini:fin].strip()


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    filas = []
    for tramo, ruta in TRAMOS:
        for f in cargar(ruta):
            frag = nota_paso_mal_casado(f.get("razon", ""))
            if frag is not None:
                filas.append((tramo, f["puesto_tramo"], f["madre_de_la_bolsa"],
                             f["hijo_de_la_bolsa"], frag))

    print("=" * 100)
    print("CENSO DE LA ESPECIE DEL 46 (nota de paso mal casado) EN LOS CUATRO TRAMOS DE OP-E-03")
    print("=" * 100)
    print("patron: %r" % RE_PASO_MAL_CASADO.pattern)
    print()
    print("%d puesto(s) con la nota:" % len(filas))
    for tramo, puesto, madre, hijo, frag in filas:
        print()
        print("--- %s, puesto %d --- %s -> %s" % (tramo, puesto, madre, hijo))
        print("  razon (fragmento): %s" % frag)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
