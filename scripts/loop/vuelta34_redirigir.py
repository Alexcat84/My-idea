# -*- coding: utf-8 -*-
"""vuelta34_redirigir.py - REHACE la redireccion de OP-D-02 que el Gate 0 deshizo.

QUE ARREGLA, y no es una reparacion de nodo: es la SEGUNDA MITAD de una
operacion ya ejecutada. La fusion de la vuelta 33 redirigio a los tres nodos
vivos que nombraban a `enfoque_mercado_voc` hacia `voz_del_cliente_voc`, y la
simetrizacion del Gate 0 le devolvio el id del muerto a los tres (caida 6.1 del
reporte de la vuelta 33, publicada en rojo). Con la decision del fundador del 15
ago 2026 aplicada al paso 5, el Gate ya no lo devuelve; falta quitar lo que
alcanzo a escribir.

MODO DE CIERRE (EJECUTOR.md regla 4): esto NO es una reparacion de nodo. No toca
texto, ni pasos, ni condiciones, ni fuentes. Toca EXCLUSIVAMENTE la lista de
aristas de tres nodos, y solo para quitar un id que la operacion ya habia
quitado una vez.

LAS GUARDAS, escritas para caer:
  1. el absorbido tiene que estar DEPRECADO (si no, esto no es una redireccion)
  2. el superviviente tiene que estar VIVO
  3. en cada sitio del que se quita el absorbido, el superviviente TIENE QUE
     ESTAR YA: si no, la redireccion perderia una arista en vez de moverla
  4. no se toca ninguna lista donde el absorbido no aparezca
  5. no se toca NINGUN campo que no sea `nodos_previos` o `nodos_siguientes`
  6. despues de escribir, se relee del disco y se comprueba

Uso:
  python scripts/loop/vuelta34_redirigir.py            (simulacion, no escribe)
  python scripts/loop/vuelta34_redirigir.py --aplicar
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")

ABSORBIDO = "enfoque_mercado_voc"
SUPERVIVIENTE = "voz_del_cliente_voc"


def ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def leer(nid):
    return json.load(io.open(ruta(nid), encoding="utf-8"))


def main():
    aplicar = "--aplicar" in sys.argv
    print("REDIRECCION DE %s HACIA %s" % (ABSORBIDO, SUPERVIVIENTE))
    print("=" * 78)

    a = leer(ABSORBIDO)
    s = leer(SUPERVIVIENTE)
    if not a.get("deprecado"):
        print("ABORTA (guarda 1): %s no esta deprecado." % ABSORBIDO)
        return 1
    if s.get("deprecado"):
        print("ABORTA (guarda 2): %s esta deprecado." % SUPERVIVIENTE)
        return 1
    print("guarda 1 OK: %s esta deprecado" % ABSORBIDO)
    print("guarda 2 OK: %s esta vivo" % SUPERVIVIENTE)

    sitios = []
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        nid = nombre[:-5]
        if nid == ABSORBIDO:
            continue
        d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
        if d.get("deprecado"):
            continue
        for campo in CAMPOS:
            if ABSORBIDO in (d.get(campo) or []):
                sitios.append((nid, campo, list(d.get(campo) or [])))

    if not sitios:
        print("\nNADA QUE HACER: ningun nodo vivo nombra a %s." % ABSORBIDO)
        return 0

    print("\nSITIOS VIVOS QUE LO NOMBRAN: %d" % len(sitios))
    for nid, campo, lista in sitios:
        ok3 = SUPERVIVIENTE in lista
        print("  %-40s %-18s %s" % (nid, campo, lista))
        print("      guarda 3 (%s ya presente): %s" % (SUPERVIVIENTE, "OK" if ok3 else "CAE"))
        if not ok3:
            print("ABORTA (guarda 3): quitar el absorbido aqui PERDERIA la arista.")
            return 1

    if not aplicar:
        print("\n(simulacion: sin --aplicar no se escribe nada)")
        return 0

    tocados = 0
    for nid, campo, lista in sitios:
        d = leer(nid)
        antes = json.dumps(d, ensure_ascii=False, sort_keys=True)
        nueva = [x for x in (d.get(campo) or []) if x != ABSORBIDO]
        d[campo] = nueva
        # guarda 5: lo unico que puede diferir es ese campo
        b = json.loads(antes)
        b[campo] = nueva
        if json.dumps(b, ensure_ascii=False, sort_keys=True) != json.dumps(d, ensure_ascii=False, sort_keys=True):
            print("ABORTA (guarda 5): el nodo %s cambiaria en mas de un campo." % nid)
            return 1
        with io.open(ruta(nid), "w", encoding="utf-8") as fh:
            json.dump(d, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        tocados += 1
        print("  ESCRITO %-40s %-18s -> %s" % (nid, campo, nueva))

    print("\nRELECTURA DEL DISCO (guarda 6)")
    quedan = []
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
        if d["node_id"] == ABSORBIDO or d.get("deprecado"):
            continue
        for campo in CAMPOS:
            if ABSORBIDO in (d.get(campo) or []):
                quedan.append((d["node_id"], campo))
    print("  nodos tocados: %d" % tocados)
    print("  sitios VIVOS que aun nombran a %s: %d %s" % (ABSORBIDO, len(quedan), quedan))
    a2 = leer(ABSORBIDO)
    print("  cableado del ARCHIVO, intacto: previos %s | siguientes %s"
          % (a2.get("nodos_previos"), a2.get("nodos_siguientes")))
    print("  sus pasos siguen siendo %d" % len(a2.get("pasos_accionables") or []))
    return 0 if not quedan else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
