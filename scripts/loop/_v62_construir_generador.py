# -*- coding: utf-8 -*-
"""_v62_construir_generador.py . ARMA scripts/loop/generar_plan_del_lote.py
COPIANDO LA MAQUINA DEL ANCESTRO POR EXTRACCION, NO A MANO.

NO ES UN INSTRUMENTO DE MEDIDA: es el andamio que evita que la copia se retecleé.
Toma las lineas 387 a 621 de scripts/loop/vuelta59_planes.py (la maquina entera:
cargar_jsonl, puertas, sin_acentos, extraer_verbatim y main), le aplica los CUATRO
cambios declarados en la cabecera del sucesor, y escribe el fichero. Cada
replace lleva su assert de UNA sola aparicion: si el ancestro cambiara, esto cae
en rojo en vez de escribir un sucesor mudo.
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANC = os.path.join(RAIZ, "scripts", "loop", "vuelta59_planes.py")
DEST = os.path.join(RAIZ, "scripts", "loop", "generar_plan_del_lote.py")

maq = "\n".join(io.open(ANC, encoding="utf-8").read().split("\n")[386:621])


def cambio(texto, viejo, nuevo):
    assert texto.count(viejo) == 1, ("no casa una sola vez", viejo[:60], texto.count(viejo))
    return texto.replace(viejo, nuevo)


# --- CAMBIO 1: el contenido editorial entra por --contenido ---
maq = cambio(
    maq,
    '    ap.add_argument("--lote", required=True)',
    '    ap.add_argument("--lote", required=True)\n'
    '    ap.add_argument("--contenido", required=True,\n'
    '                    help="modulo del contenido editorial del lote, por ejemplo _v62_lote_a")')

maq = cambio(
    maq,
    '    lote = LOTES[a.lote]',
    '    # CAMBIO 1 DECLARADO: EL CONTENIDO EDITORIAL NO VIVE EN ESTE FICHERO. El\n'
    '    # ancestro llevaba el lote A del tramo 5 escrito dentro y los otros dos por\n'
    '    # import TALLADO. Aqui el modulo entra por --contenido y este generador no\n'
    '    # conoce ningun tramo ni ningun lote: un cambio de TEXTO y uno de ARITMETICA\n'
    '    # no se pueden pisar en el mismo diff.\n'
    '    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\n'
    '    mod = __import__(a.contenido)\n'
    '    lotes = {k[len("LOTE_"):]: getattr(mod, k) for k in dir(mod) if k.startswith("LOTE_")}\n'
    '    if a.lote not in lotes:\n'
    '        print("ROJO: el modulo %s no trae el lote %s (trae %s). PARADA."\n'
    '              % (a.contenido, a.lote, sorted(lotes)))\n'
    '        return 1\n'
    '    lote = lotes[a.lote]')

# --- CAMBIO 2: el campo perdidas va SIEMPRE ---
maq = cambio(
    maq,
    '            "nota_del_reparto": spec["nota"],\n        })',
    '            "nota_del_reparto": spec["nota"],\n'
    '            # CAMBIO 2 DECLARADO: EL CAMPO perdidas VA SIEMPRE, aunque vacio.\n'
    '            # Es la mitad util del contrato CAMPO PROPIO v1: LISTA VACIA es una\n'
    '            # DECLARACION de cero perdidas y CAMPO AUSENTE es que el plan NO LO\n'
    '            # DICE. El ancestro no tenia campo y la perdida vivia solo en la\n'
    '            # prosa, que es la averia que el acta 60 dejo nombrada.\n'
    '            "perdidas": list(spec.get("perdidas") or []),\n'
    '        })')

# --- CAMBIO 3: la guarda que crece, declarada y sometida ---
maq = cambio(
    maq,
    '        sobra_p = set(spec["pasos"]) - {str(i) for i in range(1, len(pa) + 1)}',
    '        # CAMBIO 3 DECLARADO, GUARDA QUE CRECE Y VA MARCADA DISCUTIBLE (acta 61,\n'
    '        # D2 y pregunta 2: una guarda puede crecer en un sucesor declarado SI va\n'
    '        # enumerada en el docstring y marcada discutible). Las perdidas se validan\n'
    '        # AQUI, al SELLAR, y no solo despues en el tallador: especie fuera de las\n'
    '        # tres escritas, o clave que falta, es ROJO y el plan NO SE ESCRIBE.\n'
    '        for p_ in (spec.get("perdidas") or []):\n'
    '            faltan_ = [k for k in CLAVES_DE_PERDIDA if k not in p_]\n'
    '            if faltan_:\n'
    '                fallos.append("acto %d: a una perdida le faltan las claves %s"\n'
    '                              % (n, ", ".join(faltan_)))\n'
    '            elif p_["especie"] not in ESPECIES_DE_PERDIDA:\n'
    '                fallos.append("acto %d: especie de perdida desconocida %r. Las escritas son: %s"\n'
    '                              % (n, p_["especie"], ", ".join(ESPECIES_DE_PERDIDA)))\n'
    '        sobra_p = set(spec["pasos"]) - {str(i) for i in range(1, len(pa) + 1)}')

# --- CAMBIO 4: la raiz declara el contrato, y el resumen imprime las perdidas ---
maq = cambio(
    maq,
    '    plan = dict(CABECERA)\n    plan["vuelta"] = a.vuelta',
    '    plan = dict(CABECERA)\n'
    '    # CAMBIO 4 DECLARADO: LA RAIZ DECLARA EL CONTRATO. Sin esta linea el tallador\n'
    '    # nuevo se niega a leer por campo y exige --por-token con todas sus letras:\n'
    '    # el modo no se elige en silencio.\n'
    '    plan["contrato_de_perdidas"] = CONTRATO_DE_PERDIDAS\n'
    '    plan["vuelta"] = a.vuelta')

maq = cambio(
    maq,
    '    print("     TOTAL del lote %s: piezas %d (enteras %d, ya dichas %d, de INCISO %d)"\n'
    '          % (a.lote, sum(tot.values()), tot["APPEND"], tot["CUBIERTO"], tot["INCISO"]))',
    '    print("     TOTAL del lote %s: piezas %d (enteras %d, ya dichas %d, de INCISO %d)"\n'
    '          % (a.lote, sum(tot.values()), tot["APPEND"], tot["CUBIERTO"], tot["INCISO"]))\n'
    '    per_tot = sum(len(x["perdidas"]) for x in actos)\n'
    '    con_per = len([x for x in actos if x["perdidas"]])\n'
    '    print()\n'
    '    print("  LAS PERDIDAS SELLADAS EN CAMPO PROPIO (contrato %s):" % CONTRATO_DE_PERDIDAS)\n'
    '    print("     actos con el campo perdidas presente: %d de %d (el campo va SIEMPRE)"\n'
    '          % (len(actos), len(actos)))\n'
    '    print("     actos que DECLARAN cero perdidas    : %d" % (len(actos) - con_per))\n'
    '    print("     actos con al menos una perdida      : %d" % con_per)\n'
    '    print("     perdidas selladas, en total         : %d" % per_tot)\n'
    '    for x in actos:\n'
    '        for p_ in x["perdidas"]:\n'
    '            print("        acto %-3d %-22s %s" % (x["orden"], p_["especie"], p_["que"]))')

CABECERA_TXT = io.open(
    os.path.join(RAIZ, "scripts", "loop", "_v62_cabecera_generador.txt"),
    encoding="utf-8").read()

io.open(DEST, "w", encoding="utf-8", newline="\n").write(
    CABECERA_TXT + maq + "\n    raise SystemExit(main())\n")
print("escrito %s" % os.path.relpath(DEST, RAIZ))
