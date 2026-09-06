# -*- coding: utf-8 -*-
r"""vuelta195_tarea2e_cotejo.py . EL COTEJO DE LA TAREA 2.e: MIS SESENTA CLASES
CONTRA LAS DEL ARCHIVO, CON LAS CIFRAS CONTADAS DE SUS FICHEROS.

QUE COTEJA, Y CONTRA QUE:
  . MIS CLASES salen de `docs/loop/SALIDA_V195_T2_MIS_CLASES.txt`, sellado y
    COMMITEADO ANTES de que el destape se abriera. El commit que lo lleva es la
    prueba del orden, y este fichero lo NOMBRA leyendolo de git.
  . LAS DEL ARCHIVO salen del destape `docs/loop/SALIDA_V195_T2_DESTAPE.txt`,
    que escribio `aislador_de_ciega.py` en la misma corrida que la ciega.

EL COTEJO SE PUBLICA DOS VECES, Y ESO NO ES ADORNO:
  . SOBRE LOS 60.
  . SOBRE LOS 58 QUE LLEGARON LIMPIOS. El encargo de esta vuelta publica en el
    cuerpo de su TAREA 2 la clase del archivo de DOS de mis puestos, el `654` y
    el `719`, asi que yo la lei antes de leer el par. Un acierto sobre un par
    cuya respuesta venia escrita en el encargo NO ES UN ACIERTO DE LECTURA, y
    contarlo como tal inflaria mi credito.

Y EL REPARTO DENTRO Y FUERA DEL MARCADO, que es lo que `AUDITOR.md` 1.2 usa para
decidir si un tramo se relee al doble: una discrepancia DENTRO de los discutibles
marcados es un aviso que el lector se puso el; una discrepancia FUERA es la que
baja el credito de la tanda.

NINGUNA CIFRA SE TECLEA: las tres listas (mis clases, las del archivo, mis
discutibles) se extraen por expresion regular de sus ficheros y se cuentan.

LO QUE ESTE FICHERO NO HACE: no toca `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y no
mueve ninguna clase. Si de la relectura sale una correccion, SE DECLARA Y SE
TRAE.

USO:
  python scripts/loop/vuelta195_tarea2e_cotejo.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
VUELTA = 195

MIS_CLASES = "docs/loop/SALIDA_V195_T2_MIS_CLASES.txt"
DESTAPE = "docs/loop/SALIDA_V195_T2_DESTAPE.txt"
CIEGA = "docs/loop/SALIDA_V195_T2_CIEGA.txt"
TRAMO = "docs/loop/_auditor_v195_ciega_blind.txt"

# LOS DOS QUE EL ENCARGO REVELO EN SU PROPIO CUERPO. Van aqui como constante
# porque son el SUJETO de la segunda cuenta, y su motivo esta escrito arriba.
PRE_REVELADOS = [654, 719]

PAT_MIA = re.compile(r"^(\d+)\s+([ABCD])\s+([TD])\s", re.M)
PAT_PUESTO_DESTAPE = re.compile(r"^puesto_intra:\s*(\d+)\s*$", re.M)
PAT_CLASE_DESTAPE = re.compile(r"^clase:\s*([ABCD])\s*$", re.M)
PAT_PUESTO_CIEGA = re.compile(r"puesto_intra[^0-9]{0,12}(\d+)")


def sha_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    datos = io.open(p, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest())


def texto(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    return io.open(p, encoding="utf-8", errors="replace").read()


def mis_clases(t):
    """{puesto: (clase, mitad)} DE MI FICHERO SELLADO. PURA: recibe el texto."""
    return dict((int(p), (c, m)) for p, c, m in PAT_MIA.findall(t))


def mis_discutibles(t):
    """LOS PUESTOS QUE MI FICHERO MARCA COMO DISCUTIBLES. PURA.

    SE LEEN DE LA TABLA Y NO DE LA LISTA DEL FINAL, a proposito: la marca vive
    pegada a la fila que la merece, y una lista aparte se puede desincronizar de
    la tabla sin que nadie lo note. La lista del final se cuenta TAMBIEN y las
    dos cifras se publican; si no calzan, se dice.

    CORRECCION DECLARADA, Y EL CODIGO VIEJO SE NOMBRA EN VEZ DE BORRARSE. La
    primera version partia el texto ENTERO por las filas, asi que EL BLOQUE DE LA
    ULTIMA FILA LLEGABA HASTA EL FIN DEL FICHERO y se tragaba la seccion titulada
    MIS DISCUTIBLES, que lleva esa palabra en su titulo. Resultado medido: la
    ultima fila (el puesto 3331) salia marcada sin estarlo, y la cuenta daba OCHO
    donde la lista del final dice SIETE. La cazo la propia guarda de este fichero,
    que publica las dos cifras y dice si calzan, y por eso la caida se ve en vez
    de pasar. AQUI LA TABLA SE ACOTA por su cabecera de cierre antes de partirla."""
    corte = t.find("MI REPARTO, CONTADO DE LA TABLA DE ARRIBA")
    tabla = t[:corte] if corte > 0 else t
    salida = set()
    bloques = re.split(r"^(\d+)\s+[ABCD]\s+[TD]\s", tabla, flags=re.M)
    # bloques = [cabecera, puesto1, cuerpo1, puesto2, cuerpo2, ...]
    for i in range(1, len(bloques) - 1, 2):
        if "DISCUTIBLE" in bloques[i + 1]:
            salida.add(int(bloques[i]))
    return salida


def clases_del_destape(t):
    """{puesto: clase} DEL DESTAPE. PURA.

    Los dos patrones se emparejan POR ORDEN, que es como el aislador los
    escribe: un `puesto_intra:` y debajo su `clase:`. Si las dos listas no miden
    lo mismo, quien llama lo ve y para."""
    puestos = [int(x) for x in PAT_PUESTO_DESTAPE.findall(t)]
    clases = PAT_CLASE_DESTAPE.findall(t)
    if len(puestos) != len(clases):
        return None, (len(puestos), len(clases))
    return dict(zip(puestos, clases)), (len(puestos), len(clases))


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


def tabla_de_reparto(mias, suyas, puestos):
    """(coinciden, discrepan) sobre el subconjunto `puestos`. PURA."""
    coinciden = sorted(p for p in puestos if mias[p][0] == suyas[p])
    discrepan = sorted(p for p in puestos if mias[p][0] != suyas[p])
    return coinciden, discrepan


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2.e: EL COTEJO DE LOS SESENTA, CON SUS CIFRAS" % VUELTA)
    w("=" * 78)
    w("")

    w("A) EL ORDEN, LEIDO DE GIT Y NO AFIRMADO")
    w("   Lo unico que hace que este cotejo valga es que mis clases se sellaran")
    w("   ANTES de que el destape se abriera. Eso no se dice: se lee de git.")
    for rel in (MIS_CLASES, DESTAPE, CIEGA):
        c, nace = git(["log", "--diff-filter=A", "--format=%h %ad %s",
                       "--date=iso", "--", rel])
        prim = nace.splitlines()[0] if nace.strip() else "(sin commit de alta)"
        m = sha_de(rel)
        w("   %s" % rel)
        w("      nacio en: %s" % prim[:120])
        w("      disco %d bytes | LF %d bytes | sha256 LF %s"
          % (m[0], m[1], m[2][:16]) if m else "      NO EXISTE")
    w("")

    w("B) LAS TRES LISTAS, CONTADAS DE SUS FICHEROS Y NO TECLEADAS")
    t_mias = texto(MIS_CLASES)
    t_dest = texto(DESTAPE)
    mias = mis_clases(t_mias)
    suyas, cuenta = clases_del_destape(t_dest)
    w("   CIFRA filas de clase en %s: %d" % (MIS_CLASES, len(mias)))
    w("   CIFRA puestos y clases en el destape: %d y %d" % cuenta)
    if suyas is None:
        w("   PARADA: el destape no empareja puestos con clases. No se cuenta nada.")
        print(NL.join(L))
        return 1
    w("   CIFRA filas del destape: %d" % len(suyas))
    tramo = sorted(set(int(x) for x in
                       PAT_PUESTO_CIEGA.findall(texto(TRAMO))))
    w("   CIFRA puestos del tramo, contados de %s: %d" % (TRAMO, len(tramo)))
    faltan = sorted(set(suyas) - set(mias))
    sobran = sorted(set(mias) - set(suyas))
    w("   puestos del destape que YO NO CLASIFIQUE: %s"
      % (", ".join(str(x) for x in faltan) or "(ninguno)"))
    w("   puestos que YO CLASIFIQUE y el destape no trae: %s"
      % (", ".join(str(x) for x in sobran) or "(ninguno)"))
    if faltan or sobran:
        w("   PARADA: las dos listas no cubren el mismo conjunto.")
        print(NL.join(L))
        return 1
    dentro_tramo = sorted(p for p in mias if p in set(tramo))
    w("   CIFRA de mis 60 que son del tramo: %d | vecinos: %d"
      % (len(dentro_tramo), len(mias) - len(dentro_tramo)))
    mal_rotulados = sorted(p for p in mias
                           if (mias[p][1] == "T") != (p in set(tramo)))
    w("   CIFRA filas con la columna T/D mal rotulada: %d" % len(mal_rotulados))
    w("")

    w("C) MI REPARTO Y EL DEL ARCHIVO, LOS DOS CONTADOS")
    for etiqueta, fuente in (("MIO", dict((p, c) for p, (c, _m) in mias.items())),
                             ("DEL ARCHIVO", suyas)):
        cuentas = {}
        for c in fuente.values():
            cuentas[c] = cuentas.get(c, 0) + 1
        w("   %-12s %s (total %d)"
          % (etiqueta,
             " | ".join("%s %d" % (k, cuentas.get(k, 0)) for k in "ABCD"),
             sum(cuentas.values())))
    w("")

    w("D) EL COTEJO SOBRE LOS 60")
    todos = sorted(mias)
    coinciden, discrepan = tabla_de_reparto(mias, suyas, todos)
    w("   CIFRA coinciden: %d de %d" % (len(coinciden), len(todos)))
    w("   CIFRA discrepan: %d de %d" % (len(discrepan), len(todos)))
    w("   LAS DISCREPANCIAS, UNA A UNA, CON MI CLASE Y LA DEL ARCHIVO:")
    disc = mis_discutibles(t_mias)
    for p in discrepan:
        w("      puesto %-6d yo %s | archivo %s | %s | %s"
          % (p, mias[p][0], suyas[p],
             "TRAMO" if mias[p][1] == "T" else "vecino",
             "DENTRO de mi marcado" if p in disc else "FUERA de mi marcado"))
    if not discrepan:
        w("      (ninguna)")
    w("")

    w("E) MIS DISCUTIBLES, LEIDOS DE LA TABLA Y NO DE LA LISTA DEL FINAL")
    w("   CIFRA discutibles marcados en la tabla: %d" % len(disc))
    w("   LOS PUESTOS: %s" % ", ".join(str(x) for x in sorted(disc)))
    m_lista = re.search(r"Son SIETE:\s*([0-9,\s y]+)\.", t_mias)
    lista_final = sorted(int(x) for x in
                         re.findall(r"\d+", m_lista.group(1))) if m_lista else []
    w("   CIFRA discutibles en la lista del final del fichero: %d" % len(lista_final))
    w("   LAS DOS LISTAS SON LA MISMA: %s"
      % ("SI" if sorted(disc) == lista_final else
         "NO, y se publica la de la tabla, que es la que vive pegada a su fila"))
    acertados = sorted(p for p in disc if mias[p][0] == suyas[p])
    fallados = sorted(p for p in disc if mias[p][0] != suyas[p])
    w("   de mis discutibles, ACERTE %d y FALLE %d"
      % (len(acertados), len(fallados)))
    w("      acertados: %s" % (", ".join(str(x) for x in acertados) or "(ninguno)"))
    w("      fallados:  %s" % (", ".join(str(x) for x in fallados) or "(ninguno)"))
    fuera = sorted(p for p in discrepan if p not in disc)
    w("   DISCREPANCIAS FUERA DE MI MARCADO: %d" % len(fuera))
    w("      %s" % (", ".join(str(x) for x in fuera) or "(ninguna)"))
    w("   AUDITOR.md 1.2: una discrepancia FUERA del marcado baja el credito de")
    w("   la tanda y su tramo se relee al doble. LA CIFRA DE ARRIBA ES LA QUE")
    w("   DECIDE ESO, y se publica salga lo que salga.")
    w("")

    w("F) EL SEGUNDO COTEJO, SOBRE LOS 58 QUE LLEGARON LIMPIOS")
    w("   LOS DOS QUE SE QUITAN Y POR QUE: el encargo de esta vuelta publica en")
    w("   el cuerpo de su TAREA 2 la clase del archivo de estos dos puestos, asi")
    w("   que yo la lei antes de leer el par. UN ACIERTO SOBRE UN PAR CUYA")
    w("   RESPUESTA VENIA ESCRITA EN EL ENCARGO NO ES UN ACIERTO DE LECTURA.")
    for p in PRE_REVELADOS:
        w("      puesto %-6d yo %s | archivo %s | %s"
          % (p, mias[p][0], suyas[p],
             "CALZA" if mias[p][0] == suyas[p] else "NO CALZA"))
    limpios = [p for p in todos if p not in PRE_REVELADOS]
    c2, d2 = tabla_de_reparto(mias, suyas, limpios)
    w("   CIFRA puestos limpios: %d" % len(limpios))
    w("   CIFRA coinciden: %d de %d" % (len(c2), len(limpios)))
    w("   CIFRA discrepan: %d de %d" % (len(d2), len(limpios)))
    fuera2 = sorted(p for p in d2 if p not in disc)
    w("   discrepancias FUERA de mi marcado, sobre los limpios: %d" % len(fuera2))
    w("      %s" % (", ".join(str(x) for x in fuera2) or "(ninguna)"))
    w("")

    w("G) LA CLASE `B`, QUE ES LO QUE EL ENCARGO PEDIA QUE NO SE PERDIERA")
    mias_b = sorted(p for p in mias if mias[p][0] == "B")
    suyas_b = sorted(p for p in suyas if suyas[p] == "B")
    w("   CIFRA `B` que YO emito: %d -> %s"
      % (len(mias_b), ", ".join(str(x) for x in mias_b) or "(ninguna)"))
    w("   CIFRA `B` que el ARCHIVO tiene en estos 60: %d -> %s"
      % (len(suyas_b), ", ".join(str(x) for x in suyas_b) or "(ninguna)"))
    w("   `B` que acierto (mia y suya): %s"
      % (", ".join(str(x) for x in sorted(set(mias_b) & set(suyas_b)))
         or "(ninguna)"))
    w("   `B` que el archivo tiene y yo NO vi: %s"
      % (", ".join(str(x) for x in sorted(set(suyas_b) - set(mias_b)))
         or "(ninguna)"))
    w("   `B` que yo emito y el archivo NO tiene: %s"
      % (", ".join(str(x) for x in sorted(set(mias_b) - set(suyas_b)))
         or "(ninguna)"))
    w("   EL CONTRASTE MEDIDO, Y NO ES UN ADORNO: el auditor emitio CERO `B` en")
    w("   sus 30 y el archivo tenia una. Lo de arriba es lo que yo emiti.")
    w("")

    w("H) EL ARCHIVO NO SE TOCA")
    a = sha_de("docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
    w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> disco %d | LF %d | sha256 LF %s"
      % (a[0], a[1], a[2][:16]))
    w("   ESTE COTEJO NO MUEVE NINGUNA CLASE. Si de aqui sale una correccion,")
    w("   se declara y se trae, y quien la aplica es el RECOMPUTO.")
    w("")
    w("FIN")

    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%d_T2E_COTEJO.txt" % VUELTA)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
