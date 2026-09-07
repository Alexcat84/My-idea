# -*- coding: utf-8 -*-
r"""vuelta197_tarea3c_cotejo.py . EL COTEJO DE MIS 240 CLASES CONTRA EL ARCHIVO,
CORRIDO DESPUES DE QUE MIS CLASES ESTEN SELLADAS EN GIT.

LO QUE PUBLICA, Y CADA CIFRA SALE DE UN FICHERO QUE SE CUENTA AQUI:

  . cuantos COINCIDEN y cuantos DISCREPAN, sobre los 240 y sobre los LIMPIOS;
  . el reparto por clase, el mio y el del archivo, sobre los dos conjuntos;
  . cuales discrepancias caen DENTRO y cuales FUERA del marcado del archivo,
    con el literal `DISCUTIBLE MARCADO` contado de la razon de cada puesto;
  . y EL REPARTO DEL MARCADO POR PUESTO, que el hallazgo `5.2` del acta 197
    obliga a publicar en vez de deducir.

LOS QUEMADOS SE LEEN Y SU CLASE SE PUBLICA IGUAL: lo que sale es el CREDITO, no
la lectura. Son los CATORCE sellados en el sujeto MAS los DOS declarados en el
fichero de clases (`654` y `1077`), y esos dos se cuentan aparte para que se vea
lo que costaron.

USO:
  python scripts/loop/vuelta197_tarea3c_cotejo.py
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta197_tarea3_relectura_al_doble import QUEMADOS   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

ARCHIVO = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
MIS_CLASES = os.path.join(LOOP, "SALIDA_V197_T3_MIS_CLASES.txt")
SALIDA = os.path.join(LOOP, "SALIDA_V197_T3_COTEJO.txt")

# LOS DOS QUEMADOS QUE SE DECLARARON EN EL FICHERO DE CLASES Y NO EN EL SUJETO.
# Van aparte a proposito: llegaron TARDE y su cifra tiene que poder verse sola.
QUEMADOS_TARDIOS = {
    654: "su clase de archivo llego por la lista QUEMADOS de "
         "vuelta196_tarea2_relectura_al_doble.py, leida al clonar el fichero",
    1077: "es el EJEMPLAR del banco 9.22, que el encargo manda citar, y el banco "
          "lo nombra con su clase y con sus dos nodos",
}
LITERAL_MARCADO = "DISCUTIBLE MARCADO"
CORTE_DEL_HALLAZGO = 2662


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 197, TAREA 3: EL COTEJO DE LOS 240 CONTRA EL ARCHIVO")
    w("=" * 78)
    w("")

    texto = io.open(MIS_CLASES, encoding="utf-8").read()
    mias = {}
    for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([ABCD])\s*\|", texto, re.M):
        mias[int(m.group(1))] = m.group(2)
    w("A) MIS CLASES, LEIDAS DE SU FICHERO SELLADO Y NO DE MI MEMORIA")
    w("   %s (%d bytes)" % ("docs/loop/SALIDA_V197_T3_MIS_CLASES.txt",
                            os.path.getsize(MIS_CLASES)))
    w("   CIFRA clases leidas: %d" % len(mias))
    if len(mias) != 240:
        w("   PARADA: se esperaban 240 y se leyeron %d." % len(mias))
        print(NL.join(L))
        return 1
    w("")

    filas = {}
    for l in io.open(ARCHIVO, encoding="utf-8"):
        if l.strip():
            f = json.loads(l)
            filas[f.get("puesto_intra")] = f
    w("B) EL ARCHIVO, LEIDO EN MODO LECTURA")
    w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> %d filas" % len(filas))
    w("")

    quemados = dict(QUEMADOS)
    quemados.update(QUEMADOS_TARDIOS)
    universo = sorted(mias)
    limpios = [p for p in universo if p not in quemados]
    w("C) LOS QUEMADOS, QUE SE LEEN IGUAL PERO NO ENTRAN AL CREDITO")
    w("   CIFRA quemados SELLADOS EN EL SUJETO, antes de leer: %d" % len(QUEMADOS))
    w("   CIFRA quemados DECLARADOS TARDE, en el fichero de clases: %d"
      % len(QUEMADOS_TARDIOS))
    for k in sorted(QUEMADOS_TARDIOS):
        w("      %d: %s" % (k, QUEMADOS_TARDIOS[k]))
    w("   CIFRA quemados en total: %d" % len(quemados))
    w("   CIFRA puestos LIMPIOS, que son los que dan credito: %d" % len(limpios))
    w("")

    def reparto(conj, cual):
        d = {"A": 0, "B": 0, "C": 0, "D": 0, "(sin clase)": 0}
        for p in conj:
            c = (mias[p] if cual == "mia" else (filas.get(p, {}).get("clase")))
            d[c if c in d else "(sin clase)"] += 1
        return d

    def marcado(p):
        return LITERAL_MARCADO in (filas.get(p, {}).get("razon") or "").upper()

    coinciden = [p for p in universo if mias[p] == filas.get(p, {}).get("clase")]
    discrepan = [p for p in universo if mias[p] != filas.get(p, {}).get("clase")]
    coin_l = [p for p in limpios if mias[p] == filas.get(p, {}).get("clase")]
    disc_l = [p for p in limpios if mias[p] != filas.get(p, {}).get("clase")]
    quem = sorted(quemados)
    coin_q = [p for p in quem if mias[p] == filas.get(p, {}).get("clase")]

    w("D) EL COTEJO, Y LA CIFRA QUE MANDA ES LA DE LOS LIMPIOS")
    w("")
    w("| sobre que se mide | coinciden | discrepan |")
    w("|---|---:|---:|")
    w("| los %d enteros | %d de %d | %d |"
      % (len(universo), len(coinciden), len(universo), len(discrepan)))
    w("| **los %d LIMPIOS, y es la cifra que manda** | **%d de %d** | **%d** |"
      % (len(limpios), len(coin_l), len(limpios), len(disc_l)))
    w("| solo los %d quemados, fuera del credito | %d de %d | %d |"
      % (len(quem), len(coin_q), len(quem), len(quem) - len(coin_q)))
    w("")
    ra_u, rb_u = reparto(universo, "mia"), reparto(universo, "arch")
    ra_l, rb_l = reparto(limpios, "mia"), reparto(limpios, "arch")
    w("| | mio | del archivo |")
    w("|---|---|---|")
    w("| sobre los %d | A %d, B %d, C %d, D %d | A %d, B %d, C %d, D %d |"
      % (len(universo), ra_u["A"], ra_u["B"], ra_u["C"], ra_u["D"],
         rb_u["A"], rb_u["B"], rb_u["C"], rb_u["D"]))
    w("| sobre los %d limpios | A %d, B %d, C %d, D %d | A %d, B %d, C %d, D %d |"
      % (len(limpios), ra_l["A"], ra_l["B"], ra_l["C"], ra_l["D"],
         rb_l["A"], rb_l["B"], rb_l["C"], rb_l["D"]))
    w("")

    w("E) LAS DISCREPANCIAS, UNA POR UNA, CON SU MARCADO")
    w("")
    w("| puesto | mia | archivo | limpio | marcado |")
    w("|---:|:---:|:---:|:---:|:---:|")
    for p in discrepan:
        w("| %d | %s | %s | %s | %s |"
          % (p, mias[p], filas.get(p, {}).get("clase"),
             "SI" if p not in quemados else "NO, quemado",
             "DENTRO" if marcado(p) else "FUERA"))
    w("")
    dentro = [p for p in disc_l if marcado(p)]
    fuera = [p for p in disc_l if not marcado(p)]
    w("   CIFRA discrepancias LIMPIAS: %d" % len(disc_l))
    w("   CIFRA DENTRO del marcado: %d -> %s"
      % (len(dentro), ", ".join(str(x) for x in dentro) or "(ninguna)"))
    w("   CIFRA FUERA del marcado: %d -> %s"
      % (len(fuera), ", ".join(str(x) for x in fuera) or "(ninguna)"))
    w("   AUDITOR.md 1.2: si alguna cae FUERA del marcado, el credito de esta")
    w("   tanda BAJA y el tramo se relee AL DOBLE en la vuelta siguiente.")
    w("")

    w("F) EL REPARTO DEL MARCADO, QUE EL HALLAZGO `5.2` OBLIGA A PUBLICAR")
    marcados = [p for p in universo if marcado(p)]
    arriba = [p for p in marcados if p >= CORTE_DEL_HALLAZGO]
    abajo = [p for p in marcados if p < CORTE_DEL_HALLAZGO]
    alto = [p for p in universo if p >= CORTE_DEL_HALLAZGO]
    bajo = [p for p in universo if p < CORTE_DEL_HALLAZGO]
    w("   CIFRA de los %d que llevan %r en su razon: %d"
      % (len(universo), LITERAL_MARCADO, len(marcados)))
    w("   del %d PARA ARRIBA: %d marcados de %d puestos"
      % (CORTE_DEL_HALLAZGO, len(arriba), len(alto)))
    w("   por DEBAJO del %d : %d marcados de %d puestos"
      % (CORTE_DEL_HALLAZGO, len(abajo), len(bajo)))
    w("   EL REPARTO SALE COMO EL DEL AUDITOR (todo arriba, cero abajo): %s"
      % ("SI" if not abajo and arriba else "NO"))
    w("   LO QUE ESO SIGNIFICA, DICHO Y NO DEDUCIDO: la metrica de dentro-o-fuera")
    w("   del marcado NO ES COMPARABLE ENTRE TRAMOS del archivo, porque el archivo")
    w("   no marca nada por debajo del %d. Una discrepancia en el tramo bajo cae"
      % CORTE_DEL_HALLAZGO)
    w("   FUERA por construccion, no por ser peor.")
    w("")

    w("G) LOS QUEMADOS, CON SU CLASE PUBLICADA IGUAL")
    w("")
    w("| puesto | mia | archivo | calza | de donde venia quemado |")
    w("|---:|:---:|:---:|:---:|---|")
    for p in quem:
        origen = quemados[p]
        w("| %d | %s | %s | %s | %s |"
          % (p, mias[p], filas.get(p, {}).get("clase"),
             "SI" if mias[p] == filas.get(p, {}).get("clase") else "NO",
             origen[:96]))
    w("")
    w("H) EL ARCHIVO NO SE TOCO: este fichero lo abre en modo lectura y no escribe")
    w("   ni una fila.")
    w("")
    w("FIN DEL COTEJO")
    t = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (SALIDA, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
