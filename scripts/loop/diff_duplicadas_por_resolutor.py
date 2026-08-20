# -*- coding: utf-8 -*-
"""diff_duplicadas_por_resolutor.py . DIFF DEL CENSO DE DUPLICADAS ENTRE DOS
CORTES, CON EL NODO Y EL DESTINO RESUELTOS POR EL ALIAS DE HOY.

NOMBRE ESTABLE A PROPOSITO: la vuelta entra por los dos cortes que se comparan,
asi que este fichero no se clona.

POR QUE NACE, y el motivo esta MEDIDO, no razonado. La guarda de duplicadas
fabricadas se venia corriendo con codigo suelto dentro de la vuelta, comparando
la terna cruda (nodo, campo, destino) de docs/plan/ARISTAS_DUPLICADAS.jsonl
entre dos cortes. Esa comparacion TIENE UN FALSO POSITIVO ESTRUCTURAL: cuando la
fusion renombra el destino de un grupo (porque el destino era el absorbido y
pasa a ser el superviviente), el MISMO grupo desaparece con un rotulo y aparece
con otro, y el diff crudo lo publica como GRUPO NUEVO FABRICADO.

  LA VUELTA 59 YA SE TOPO CON ESTO y lo resolvio A MANO: su reporte dice que de
  los 5 grupos que aparecian, LOS 5 ERAN LOS MISMOS 5 QUE DESAPARECIAN CON OTRO
  ROTULO, y los nombro uno a uno. Funciono, pero el emparejamiento lo hizo el
  ojo. La vuelta 60 volvio a caer en el mismo sitio con un solo ejemplar
  (control_mantener_ganancias | nodos_siguientes, cuyo destino paso de
  pdsa_shewhart_cycle a ciclo_shewhart_pdsa) y lo publico como fabricado antes
  de verificarlo contra el grafo. AQUEL EMPAREJAMIENTO A MANO ES LO QUE ESTE
  INSTRUMENTO HACE POR MAQUINA.

QUE HACE, y es lo unico que hace: resuelve el NODO y el DESTINO de cada grupo
por la cadena de alias del arbol de HOY antes de comparar. Dos grupos que solo
se distinguen por el rotulo del destino colapsan en uno y dejan de contarse como
aparicion y desaparicion.

LO QUE NO DECIDE: no dice si una duplicada es legitima ni la retira. Solo separa
LAS FABRICADAS DE VERDAD de las renombradas. La retirada es de P.16
(retirar_duplicada_por_resolutor.py antes de fundir) o de
retirar_entrada_redundante.py despues.

DE SOLO LECTURA ENTERA: lee dos ficheros y el arbol de nodos, e imprime.

USO:
  python scripts/loop/diff_duplicadas_por_resolutor.py --antes <hash>:docs/plan/ARISTAS_DUPLICADAS.jsonl --despues docs/plan/ARISTAS_DUPLICADAS.jsonl
  python scripts/loop/diff_duplicadas_por_resolutor.py --antes A.jsonl --despues B.jsonl --etiqueta "lote C contra lote B"

Un argumento con dos puntos se lee de git (git show); sin dos puntos, del disco.

SALIDA: exit 1 si hay grupos FABRICADOS; exit 0 si no.
"""
import argparse
import glob
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def mapa_alias():
    """alias -> quien lo reclama, leido del arbol de HOY."""
    m = {}
    for f in glob.glob(os.path.join(NODOS, "*.json")):
        o = json.load(io.open(f, encoding="utf-8"))
        nid = os.path.basename(f)[:-5]
        for a in (o.get("ids_alias") or []):
            m[a] = nid
    return m


def hacer_resolver(m):
    def res(x):
        visto = set()
        while x in m and x not in visto:
            visto.add(x)
            x = m[x]
        return x
    return res


def leer(ref):
    if ":" in ref and not os.path.exists(os.path.join(RAIZ, ref)):
        return subprocess.check_output(["git", "show", ref], cwd=RAIZ).decode("utf-8", "replace")
    ruta = ref if os.path.isabs(ref) else os.path.join(RAIZ, ref)
    return io.open(ruta, encoding="utf-8").read()


def grupos(texto, res):
    crudos, resueltos = {}, {}
    for l in texto.splitlines():
        if not l.strip():
            continue
        r = json.loads(l)
        clave_cruda = (r["nodo"], r["campo"], r["destino"])
        clave = (res(r["nodo"]), r["campo"], res(r["destino"]))
        crudos[clave_cruda] = clave
        resueltos.setdefault(clave, []).append(clave_cruda)
    return crudos, resueltos


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--antes", required=True)
    p.add_argument("--despues", required=True)
    p.add_argument("--etiqueta", default=None)
    a = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    res = hacer_resolver(mapa_alias())
    cr_a, ra = grupos(leer(a.antes), res)
    cr_b, rb = grupos(leer(a.despues), res)

    print("=" * 78)
    print("DIFF DEL CENSO DE DUPLICADAS, CON NODO Y DESTINO RESUELTOS POR EL ALIAS")
    if a.etiqueta:
        print("  %s" % a.etiqueta)
    print("  antes  : %s" % a.antes)
    print("  despues: %s" % a.despues)
    print("=" * 78)
    print()
    print("  grupos por rotulo CRUDO   : antes %d | despues %d" % (len(cr_a), len(cr_b)))
    print("  grupos ya RESUELTOS       : antes %d | despues %d" % (len(ra), len(rb)))
    print()

    crudo_nuevos = set(cr_b) - set(cr_a)
    fabricados = sorted(set(rb) - set(ra))
    ido = sorted(set(ra) - set(rb))

    renombrados = [k for k in crudo_nuevos if cr_b[k] not in fabricados]
    print("  RENOMBRADOS (aparecen con rotulo nuevo pero son el MISMO grupo): %d" % len(renombrados))
    for k in sorted(renombrados):
        print("     %s | %s | %s   -> resuelve a %s" % (k[0], k[1], k[2], cr_b[k][2]))
    print()
    print("  GRUPOS FABRICADOS DE VERDAD: %d" % len(fabricados))
    for k in fabricados:
        print("     FABRICADO %s | %s | %s" % k)
    print()
    print("  grupos que DESAPARECEN: %d" % len(ido))
    for k in ido:
        print("     %s | %s | %s" % k)
    print()
    if fabricados:
        print("  ROJO: esta fusion fabrica %d grupo(s) de duplicadas." % len(fabricados))
        return 1
    print("  VERDE: CERO grupos fabricados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
