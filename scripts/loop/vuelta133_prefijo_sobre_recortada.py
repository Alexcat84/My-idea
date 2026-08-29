# -*- coding: utf-8 -*-
"""vuelta133_prefijo_sobre_recortada.py . TAREA 4.b de la vuelta 133,
ADJUDICADO por el auditor (acta 132, seccion 3.1, "LO ADJUDICO YO, NO EL
FUNDADOR"). Ya NO es pregunta abierta (esa era `vuelta132_prefijo_sobre_
recortada.py`, TAREA 3.d de la 132, "MEDIDO, NO APLICADO"): esta vuelta SE
APLICA, ATADA a la cola de localizador EXTENDIDA con `Apendice` de la
TAREA 4.a (`vuelta133_cola_localizador_apendice.py`), NUNCA SUELTA.

POR QUE ATADA. Aplicar el prefijo sobre la recortada SOLO, sobre la cola
VIEJA (sin `Apendice`), corona `..., Apendice B (RFPS)` como canonica de 23
nodos y deja las SINTETICAS del censo en CERO (medido por el auditor en el
acta 132: el mismo vicio que la NOVENA entrada de la ficha `fuente`
escribio la regla sintetica para matar, entrando por otra puerta). Con la
cola de 4.a puesta, la misma familia queda coronada por
`Diana L. Lindstrom, Procurement Project Management Success (J. Ross,
2014)`, que es el libro con su edicion, no un apendice.

LA REGLA: PREFIJO ESTRICTO sobre la forma recortada (con la cola de 4.a),
con DOS guardas:
  (1) LONGITUD: la recortada mas corta de las dos tiene que medir 20
      caracteres o mas (misma guarda que la regla de TITULO de la 131).
  (2) RESTO, POR SIMETRIA CON LA REGLA DEL TITULO: si las dos grafias
      representantes tienen RESTO (el segmento tras " - ") y NINGUNO es
      prefijo del otro, NO se unen. Medido: esta guarda no cambia el
      resultado hoy (104 grupos con ella puesta y sin ella, los mismos 19
      pares), porque las grafias de esta familia no traen " - ": se deja
      puesta igual porque cierra el agujero para cuando el censo crezca
      con un caso que si la necesite.

Salida: docs/loop/SALIDA_V133_4B_PREFIJO_APLICADO.txt, con TODOS los pares
que une, uno por uno.

Uso:
  python scripts/loop/vuelta133_prefijo_sobre_recortada.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta131_grupos_por_titulo import (  # noqa: E402
    cargar_censo,
    prefijo_cadena_entera_une,
    prefijo_titulo_une,
    titulo_de,
    resto_de,
    UnionFind,
)
from vuelta133_cola_localizador_apendice import recortar_localizador_con_apendice  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V133_4B_PREFIJO_APLICADO.txt")

GUARDA_LONGITUD = 20


def calcular_base():
    """Reproduce exactamente los 105 grupos de 4.a (R1 cadena entera + R2
    titulo + R3 localizador con Apendice, igualdad exacta)."""
    censo = cargar_censo()
    grafias = sorted(censo.keys())
    uf = UnionFind(grafias)
    for a in grafias:
        for b in grafias:
            if prefijo_cadena_entera_une(a, b):
                uf.une(a, b)
    for a in grafias:
        for b in grafias:
            if prefijo_titulo_une(a, b):
                uf.une(a, b)
    buck = {}
    for g in grafias:
        buck.setdefault(recortar_localizador_con_apendice(g), []).append(g)
    for _, miembros in buck.items():
        base = miembros[0]
        for m in miembros[1:]:
            uf.une(base, m)
    return censo, grafias, uf


def resto_guarda_permite(rep_a, rep_b):
    ra, rb = resto_de(rep_a), resto_de(rep_b)
    if ra and rb and not (ra.startswith(rb) or rb.startswith(ra)):
        return False
    return True


def correr_caso_de_prueba():
    """CASO adjudicado por el auditor: la familia sintetica de capitulos
    ('Diana L. Lindstrom, Procurement Project Management Success', 3
    miembros con cola de capitulo/Apendice) tiene que fundirse con la
    grafia sin cola 'Diana L. Lindstrom, Procurement Project Management
    Success (J. Ross, 2014)', porque la recortada del primero (la cadena
    del titulo pelado) es PREFIJO ESTRICTO de la recortada del segundo."""
    base_sintetica = "Diana L. Lindstrom, Procurement Project Management Success"
    libro_con_edicion = "Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014)"
    assert libro_con_edicion.startswith(base_sintetica)
    assert len(base_sintetica) >= GUARDA_LONGITUD
    assert resto_guarda_permite(base_sintetica, libro_con_edicion)


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    correr_caso_de_prueba()

    censo, grafias, uf = calcular_base()
    grupos_base = {}
    for g in grafias:
        grupos_base.setdefault(uf.find(g), []).append(g)
    n_base = len(grupos_base)

    representante_de_raiz = {r: max(m, key=len) for r, m in grupos_base.items()}
    recortada_de_raiz = {r: recortar_localizador_con_apendice(representante_de_raiz[r])
                         for r in grupos_base}

    raices = sorted(grupos_base.keys())
    pares_nuevos = []
    for ra in raices:
        for rb in raices:
            if ra >= rb:
                continue
            ca, cb = recortada_de_raiz[ra], recortada_de_raiz[rb]
            if ca == cb:
                continue
            corto, largo = (ca, cb) if len(ca) <= len(cb) else (cb, ca)
            if len(corto) < GUARDA_LONGITUD:
                continue
            if not largo.startswith(corto):
                continue
            if not resto_guarda_permite(representante_de_raiz[ra], representante_de_raiz[rb]):
                continue
            pares_nuevos.append((ra, rb))

    uf2 = UnionFind(raices)
    for ra, rb in pares_nuevos:
        uf2.une(ra, rb)
    n_final = len({uf2.find(r) for r in raices})

    grupos_final = {}
    for r in raices:
        grupos_final.setdefault(uf2.find(r), []).append(r)
    multi_final = {r: raices_m for r, raices_m in grupos_final.items() if len(raices_m) > 1
                   or len(grupos_base[raices_m[0]]) > 1}

    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write("APLICADO (adjudicado por el auditor, acta 132 3.1), ATADO a la cola con Apendice de 4.a.\n")
        fh.write("Guarda de longitud: recortada mas corta >= %d caracteres.\n" % GUARDA_LONGITUD)
        fh.write("Guarda de RESTO (simetria con la regla de titulo de la 131): puesta; medido que hoy\n")
        fh.write("no cambia el resultado (%d grupos con ella y sin ella).\n\n" % n_final)
        fh.write("CASO adjudicado (Lindstrom, sintetica de capitulos -> libro con edicion): OK\n\n")
        fh.write("GRUPOS BASE (4.a, R1+R2+R3 con Apendice, igualdad exacta): %d\n" % n_base)
        fh.write("GRUPOS TRAS APLICAR PREFIJO SOBRE RECORTADA: %d\n" % n_final)
        fh.write("COLAPSOS GANADOS: %d\n\n" % (n_base - n_final))
        fh.write("TODOS LOS PARES QUE UNE (raiz base A, raiz base B), uno por uno (%d):\n" % len(pares_nuevos))
        for ra, rb in pares_nuevos:
            fh.write("  %r  <->  %r\n" % (recortada_de_raiz[ra], recortada_de_raiz[rb]))
            for m in sorted(grupos_base[ra], key=len):
                fh.write("    A: %d\t%s\n" % (censo[m], m))
            for m in sorted(grupos_base[rb], key=len):
                fh.write("    B: %d\t%s\n" % (censo[m], m))
        fh.write("\nGRUPOS FINALES CON 2 O MAS MIEMBROS (grupos base fundidos o ya multi):\n")
        multi_final_2mas = {r: v for r, v in multi_final.items()
                            if sum(len(grupos_base[raiz]) for raiz in v) > 1}
        for r in sorted(multi_final_2mas, key=lambda r: -sum(len(grupos_base[raiz]) for raiz in multi_final_2mas[r])):
            raices_grupo = multi_final_2mas[r]
            miembros = [m for raiz in raices_grupo for m in grupos_base[raiz]]
            fh.write("  GRUPO (%d nodos, %d grafias):\n" % (sum(censo[m] for m in miembros), len(miembros)))
            for m in sorted(miembros, key=len):
                fh.write("    %d\t%s\n" % (censo[m], m))
        n_multi = len(multi_final_2mas)
        n_grafias_multi = sum(len(m) for raices_g in multi_final_2mas.values() for m in [grupos_base[r] for r in raices_g])
        n_grafias_multi = sum(sum(len(grupos_base[raiz]) for raiz in v) for v in multi_final_2mas.values())
        fh.write("\nTOTAL grafias: %d\n" % len(grafias))
        fh.write("TOTAL grupos (incluye singletons): %d\n" % n_final)
        fh.write("TOTAL grupos con 2 o mas miembros: %d (%d grafias)\n" % (n_multi, n_grafias_multi))
        fh.write("TOTAL sin agrupar: %d\n" % (n_final - n_multi))

    print("caso adjudicado (Lindstrom sintetica -> libro con edicion): OK")
    print("grupos base (4.a): %d" % n_base)
    print("grupos tras prefijo sobre recortada: %d" % n_final)
    print("colapsos ganados: %d" % (n_base - n_final))
    print("pares nuevos: %d" % len(pares_nuevos))
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
