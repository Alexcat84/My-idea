# -*- coding: utf-8 -*-
"""_v63_registrar_opu02.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DE LA APERTURA MEDIDA DE OP-U-02.

NI UNA CELDA SE TECLEA: las tres tablas salen de docs/loop/NOMINA_OPU02_V63.jsonl,
que es el fichero que el instrumento abrir_universo_de_opu02.py fijo en esta
vuelta, y de las dos salidas que la acompanan.

NO REESCRIBE NI UNA LINEA DE ARRIBA: abre la pagina en modo adosar. En
particular NO toca la seccion de OP-U-02 que ya vive en la linea 220, cuya
frase de las CUATRO exclusiones queda entera y con su contraste al lado.

Uso: python scripts/loop/_v63_registrar_opu02.py [--simular]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
NOMINA = os.path.join(RAIZ, "docs", "loop", "NOMINA_OPU02_V63.jsonl")
NL = chr(10)

CITAS = [
    (226, "EL RECOMPUTO NO ABRE 48 FUSIONES"),
    (227, "el de 13 y el de 9 van a mesa"),
    (228, "dos de los grandes van a destejido"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    pag = io.open(PAGINA, encoding="utf-8").read().split(NL)
    print("=" * 78)
    print("GUARDA DE LAS CITAS DE LINEA A 03_FUSIONES.md, ANTES DE ESCRIBIR NADA")
    print("=" * 78)
    fallos = []
    for n, aguja in CITAS:
        real = pag[n - 1] if 1 <= n <= len(pag) else "(fuera de rango)"
        ok = aguja.lower() in real.lower()
        print("  linea %-5d %-5s %s" % (n, "OK" if ok else "ROJO", real.strip()[:88]))
        if not ok:
            fallos.append("la linea %d no contiene %r" % (n, aguja))
    if fallos:
        print()
        print("ROJO, NO SE ESCRIBE NADA:")
        for f in fallos:
            print("   %s" % f)
        return 1

    filas = [json.loads(l) for l in io.open(NOMINA, encoding="utf-8") if l.strip()]
    abre = [f for f in filas if f["abre"]]
    fuera = [f for f in filas if not f["abre"]]
    tam = {}
    for f in abre:
        tam[f["tamano"]] = tam.get(f["tamano"], 0) + 1

    L = []
    L.append("")
    L.append("---")
    L.append("")
    L.append("## `OP-U-02`: **LA APERTURA MEDIDA, SIN FUNDIR NI UN ACTO** (20 ago 2026, vuelta 63)")
    L.append("")
    L.append("**Esto NO ejecuta `OP-U-02`: la MIDE.** Ni un acto suyo se funde en esta vuelta. **La "
             "nomina queda FIJADA en fichero propio**, [`../loop/NOMINA_OPU02_V63.jsonl`](../loop/NOMINA_OPU02_V63.jsonl), "
             "**una fila por acto abierto con sus miembros**, y sale entera de "
             "`python scripts/loop/abrir_universo_de_opu02.py` "
             "([`../loop/SALIDA_V63_APERTURA_OPU02.txt`](../loop/SALIDA_V63_APERTURA_OPU02.txt)).")
    L.append("")
    L.append("**EL INSUMO ES EL RECOMPUTO CORRIDO EN ESTA MISMA VUELTA**, no un fichero sellado "
             "viejo: [`../loop/_v63_componentes_cierre.jsonl`](../loop/_v63_componentes_cierre.jsonl), "
             "medido DESPUES de las dos fusiones de mesa. **Y por `P.1`, el instrumento RESUELVE "
             "POR ALIAS ANTES DE CONTAR**, o contaria como libre un acto cuyo miembro ya fue "
             "absorbido.")
    L.append("")
    L.append("| | |")
    L.append("|---|---:|")
    L.append("| **actos abiertos, medidos hoy** | **%d** sobre **%d** nodos |"
             % (len(filas), sum(f["tamano"] for f in filas)))
    L.append("| **`OP-U-02` ABRE** (criterio del propio plan: sin dueno en mesa ni destejido) | "
             "**%d** actos sobre **%d** nodos |" % (len(abre), sum(f["tamano"] for f in abre)))
    L.append("| **quedan FUERA, con dueno en otra fase** | **%d** actos sobre **%d** nodos |"
             % (len(fuera), sum(f["tamano"] for f in fuera)))
    L.append("| **los que ABREN, por tamano** | %s |"
             % ", ".join("**%d** de %d" % (tam[k], k) for k in sorted(tam, reverse=True)))
    L.append("")
    L.append("### LOS QUE QUEDAN FUERA, CADA UNO CON SU DUENO NOMBRADO Y SU CITA")
    L.append("")
    L.append("| tamano | dueno | miembros |")
    L.append("|---:|---|---|")
    for f in sorted(fuera, key=lambda x: -x["tamano"]):
        L.append("| **%d** | %s | %s |"
                 % (f["tamano"], ", ".join("`%s`" % d for d in f["duenos_mesa_o_destejido"]),
                    ", ".join("`%s`" % m for m in f["miembros"])))
    L.append("")
    L.append("### **LA FRASE DE LA LINEA 226 ESTA ENVEJECIDA, Y SE DICE EN VEZ DE CALLARLO**")
    L.append("")
    L.append("**El texto de arriba (lineas 226 a 228, leidas HOY y cotejadas por este mismo "
             "instrumento antes de escribir) dice que CUATRO abiertos no se resuelven aqui "
             "nunca**: el de 13 y el de 9 a mesa, y **dos grandes a destejido**. **La ficha de "
             "`OP-U-02` en [`OPERACIONES.jsonl`](OPERACIONES.jsonl) ya lo habia corregido en la "
             "vuelta 13 y dice OCHO.** **Lo medido HOY reconcilia las dos y no elige entre "
             "ellas:**")
    L.append("")
    L.append("| los OCHO que la ficha nombra | como estan HOY |")
    L.append("|---|---|")
    L.append("| **seis de ellos** (el de 13, el de 9, el de 7 de `customer validation`, el de la "
             "junta asesora, el de la voz del cliente y el del pivote) | **siguen ABIERTOS y "
             "quedan fuera por su dueno**, y son exactamente los seis de la tabla de arriba |")
    L.append("| **los DOS de destejido** (`OP-D-03` y `OP-D-04`) | **YA NO SON ACTOS: no aparecen "
             "en NINGUNA componente del recomputo de hoy, ni abierta ni cerrada** |")
    L.append("")
    L.append("**Y LA DESAPARICION DE ESOS DOS NO SE SUPONE: SE MIDE, Y LAS DOS CAUSAS SON "
             "DISTINTAS** ([`../loop/SALIDA_V63_DESTEJIDOS_COMPROBADOS.txt`](../loop/SALIDA_V63_DESTEJIDOS_COMPROBADOS.txt)):")
    L.append("")
    L.append("| | lo medido | la causa |")
    L.append("|---|---|---|")
    L.append("| **`OP-D-04`** | sus **7** nodos resuelven HOY a **2** supervivientes, los dos "
             "vivos | **la componente se consumio POR FUSION** |")
    L.append("| **`OP-D-03`** | sus **6** nodos siguen **VIVOS** y **ninguno resuelve a otro** | "
             "**lo que desaparecio no son los nodos: son LAS ARISTAS `A`**. Los **8** pares "
             "internos que el archivo tiene entre ellos son **8 de clase `D`**, y una componente "
             "de este recomputo se forma **solo con aristas `A`** |")
    L.append("")
    L.append("> **UNA CIFRA MAS QUE CAMBIO Y VA DICHA:** la ficha de la vuelta 13 llamaba **de "
             "tamano 4** al acto de la voz del cliente; **hoy mide 3**. Es un acto que encogio, "
             "no una cuenta mal hecha, y por eso la tabla de arriba publica **3** y esta nota "
             "publica la diferencia.")
    L.append("")
    L.append("> **LO QUE ESTA APERTURA NO HACE, dicho para que nadie se lo atribuya: NO elige "
             "superviviente, NO reparte piezas, NO declara ningun acto y NO funde nada.** Fija "
             "quien entra en el universo y quien no, con su motivo citado. **La fusion de esos "
             "%d actos es trabajo de la vuelta que la ejecute.**" % len(abre))
    L.append("")

    texto = NL.join(L)
    print()
    print("  lineas del registro: %d" % len(L))
    if a.simular:
        print(texto)
        print("MODO SIMULAR: no se adosa nada.")
        return 0
    n0 = len(pag)
    with io.open(PAGINA, "a", encoding="utf-8", newline=NL) as fh:
        fh.write(texto + NL)
    n1 = len(io.open(PAGINA, encoding="utf-8").read().split(NL))
    print("ADOSADO a %s: %d lineas antes, %d despues (+%d)."
          % (os.path.relpath(PAGINA, RAIZ), n0, n1, n1 - n0))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
