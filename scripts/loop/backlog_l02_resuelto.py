#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""backlog_l02_resuelto.py . EL BACKLOG DE `OP-L-02` CON EL RESOLUTOR DE `P.1`
POR ENCIMA, Y LAS DOS COLUMNAS AL LADO.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, hermano de `backlog_l03_resuelto.py`, y
por el mismo motivo: se invoca cada vez que alguien quiere saber cuanto queda de
`OP-L-02`, y NO SE CLONA.

SOLO LECTURA. **No escribe nodos, ni veredictos, ni operaciones, ni la ficha, ni
el marcador, ni lee un solo par.** Imprime. La TAREA 5 de la vuelta 180 dice con
esas palabras: *"MIDE `OP-L-02` CON LA MISMA VARA RESUELTA QUE CERRO `OP-L-03`, Y
NO LEAS NI UN PAR"*.

QUE NO TOCA, Y ES LA PRIMERA REGLA DE ESTE FICHERO. Ni
`scripts/vuelta16_generar_actos.mjs`, que es donde vive la constante
`NOMINAS_OP_L_02` que la ficha cita, ni
`scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py`, que es el instrumento que
la lee. Este fichero **importa el parser de aquel y lo corre**, que es la forma
de no citarlo de memoria (`EJECUTOR.md` 2).

LAS DOS COLUMNAS VAN SIEMPRE LAS DOS Y LA VIEJA NO SE BORRA (`banco 9.10`): lo
que el instrumento da y lo que queda resuelto.

LOS DOS CAMINOS VAN SIEMPRE LOS DOS (`EJECUTOR.md` 9):

  CAMINO 1, EL RESOLUTOR DE `P.1`: `mapa_de_alias()` de
  `scripts/loop/vuelta166_tarea2_correccion_op_l_01.py`. Un miembro esta VIVO si
  se resuelve a si mismo.

  CAMINO 2, EL CAMPO `deprecado` DEL GRAFO: un miembro esta VIVO si el grafo lo
  tiene y su `deprecado` es falso.

CAE EN ROJO (exit 1) SI LOS DOS CAMINOS NO CALZAN EN ALGUNA NOMINA, NOMBRANDOLA.

QUE ES UN PAR REAL, DICHO ANTES DE CONTARLO para que no se pueda elegir despues,
y **aqui son DOS definiciones y se publican LAS DOS**, porque `OP-L-02` tiene DOS
sedes de clase y `OP-L-03` solo tenia una:

  REAL CONTRA EL ARCHIVO: de las parejas de miembros de la nomina se descartan
  (1) las que tras resolver tienen los DOS EXTREMOS EN EL MISMO NODO y (2) las
  que YA TIENEN VEREDICTO en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, buscado por
  el par RESUELTO (`P.1`, sin excepcion). **Es la definicion literal del
  encargo**, y es la que `backlog_l03_resuelto.py` usa.

  REAL CONTRA LAS DOS SEDES: lo mismo, descartando ademas las que tienen
  **LECTURA DIRIGIDA** escrita en `docs/plan/*.md`. Una lectura dirigida NO entra
  en la cola y NO mueve el marcador, pero **el par esta leido**, y contarlo como
  trabajo pendiente seria mandar a releer lo ya leido.

  LAS DOS SE PUBLICAN. La primera es la que el encargo pide; la segunda es la que
  dice cuanto queda DE VERDAD, y sin las dos al lado la cifra enganaria en un
  sentido o en el otro.

EL TRAMO, DEFINIDO ANTES DE REPARTIR NADA: una nomina esta **YA MIRADA** si
alguno de sus pares tiene lectura dirigida escrita, y **SIN MIRAR** si ninguno.
El criterio se lee del fichero, no se teclea una lista.

Y CADA CIFRA QUE SE PUEDE MOVER DENTRO DE UNA VUELTA LLEVA SU CORTE PEGADO, por
la TAREA 3 de esta misma vuelta.

USO:
  python scripts/loop/backlog_l02_resuelto.py
"""
import io
import json
import os
import sys
from itertools import combinations

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import vuelta166_tarea2_correccion_op_l_01 as T   # noqa: E402
import backlog_l03_resuelto as B   # noqa: E402
import verificar_mutaciones_viejas as VMV   # noqa: E402
import vuelta169_tarea5_cobertura_op_l_02 as VIEJO   # noqa: E402

NL = chr(10)
PLAN = os.path.join(RAIZ, "docs", "plan")
sello = VMV.sello_de_corte

# LA CIFRA VIEJA DE LA FICHA, CONSERVADA COMO CONTRASTE Y NO COMO FUENTE
# (`EJECUTOR.md` 2). Se lee de la propia ficha en la corrida, no se teclea aqui.
FICHA = os.path.join(PLAN, "OPERACIONES.jsonl")


def lecturas_dirigidas(mapa):
    """{frozenset(par resuelto): (clase, fichero)} de TODAS las sedes de lectura
    dirigida de docs/plan/. Usa los DOS patrones del instrumento de la 169, el de
    cabecera y el de fila de tabla, importados de el y no re-escritos aqui."""
    salida = {}
    for nombre in sorted(os.listdir(PLAN)):
        if not nombre.endswith(".md"):
            continue
        texto = io.open(os.path.join(PLAN, nombre), encoding="utf-8",
                        errors="replace").read()
        for _num, a, b, clase in VIEJO.PAT_LD.findall(texto):
            k = frozenset((T.resolver(mapa, a), T.resolver(mapa, b)))
            if len(k) == 2:
                salida.setdefault(k, (clase.strip(), nombre))
        for a, b, clase in VIEJO.PAT_LD_TABLA.findall(texto):
            k = frozenset((T.resolver(mapa, a), T.resolver(mapa, b)))
            if len(k) == 2:
                salida.setdefault(k, (clase.strip(), nombre))
    return salida


def medir_nomina(miembros, mapa, vivos_grafo, idx, dirigidas):
    """LA MEDICION DE UNA NOMINA, PURA. Devuelve un dict.

    PURA a proposito: recibe el mapa de alias, el diccionario de vivos, el indice
    de veredictos y el de lecturas dirigidas, para que se le pueda pasar material
    fabricado sin tocar el repo."""
    resueltos = dict((m, T.resolver(mapa, m)) for m in miembros)
    vivos_res = sorted({v for v in resueltos.values()})
    vivos_gra = sorted({m for m in miembros if vivos_grafo.get(m, False)})
    calzan = (len(vivos_res) == len(vivos_gra))

    disueltos, con_veredicto, con_dirigida = [], [], []
    reales_archivo, reales_dos, reales_con_dirigida = [], [], []
    vistos = set()
    for a, b in combinations(sorted(miembros), 2):
        ra, rb = resueltos[a], resueltos[b]
        if ra == rb:
            disueltos.append((a, b, ra))
            continue
        clave = frozenset((ra, rb))
        if clave in vistos:
            continue
        vistos.add(clave)
        en_archivo = clave in idx
        en_dirigida = clave in dirigidas
        if en_archivo:
            con_veredicto.append((a, b))
        if en_dirigida:
            con_dirigida.append((a, b, dirigidas[clave][0], dirigidas[clave][1]))
        if not en_archivo:
            reales_archivo.append((a, b))
        if not en_archivo and not en_dirigida:
            reales_dos.append((a, b))
        if not en_archivo and en_dirigida:
            reales_con_dirigida.append((a, b))
    return {
        "miembros": sorted(miembros),
        "cifra_miembros": len(miembros),
        "cifra_vivos_por_resolutor": len(vivos_res),
        "vivos_por_resolutor": vivos_res,
        "cifra_vivos_por_grafo": len(vivos_gra),
        "vivos_por_grafo": vivos_gra,
        "los_dos_caminos_calzan": calzan,
        "cifra_pares_del_instrumento": len(list(combinations(miembros, 2))),
        "cifra_pares_distintos_tras_resolver": len(vistos),
        "cifra_pares_disueltos": len(disueltos),
        "cifra_pares_con_veredicto": len(con_veredicto),
        "cifra_pares_con_dirigida": len(con_dirigida),
        "cifra_reales_contra_el_archivo": len(reales_archivo),
        "cifra_reales_contra_las_dos_sedes": len(reales_dos),
        "cifra_reales_que_ADEMAS_tienen_dirigida": len(reales_con_dirigida),
        "reales_contra_el_archivo": reales_archivo,
        "reales_contra_las_dos_sedes": reales_dos,
        "con_dirigida": con_dirigida,
    }


def cifra_vieja_de_la_ficha():
    """LA LINEA DE `evidencia` DE LA FICHA, LEIDA DE LA FICHA. No se teclea."""
    for l in io.open(FICHA, encoding="utf-8"):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get("id_op") == "OP-L-02":
            return d.get("evidencia") or [], d.get("fecha_corte"), d.get("estado")
    return [], None, None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    corte = VMV.corte_de_git()

    p("=" * 78)
    p("EL BACKLOG DE OP-L-02, CON EL RESOLUTOR DE P.1 POR ENCIMA")
    p("=" * 78)
    p("")
    p("   EL CORTE DE TODA ESTA CORRIDA: HEAD %s" % corte)
    p("   NO SE LEE NI UN PAR, NO SE ESCRIBE NINGUN VEREDICTO, NO SE TOCA EL")
    p("   MARCADOR Y NO SE TOCA EL ESTADO DE NINGUNA FICHA.")
    p("")

    p("A) EL INSTRUMENTO VIEJO, CORRIDO POR DENTRO Y NO CITADO DE MEMORIA")
    p("   la nomina vive en scripts/vuelta16_generar_actos.mjs, constante")
    p("   NOMINAS_OP_L_02, y se PARSEA con leer_nominas() de")
    p("   scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py, importado. NI UNO NI")
    p("   OTRO SE TOCAN.")
    nominas = VIEJO.leer_nominas()
    p("   CIFRA nominas que la constante trae: %d (NO se mueve dentro de una "
      "vuelta: sale de una constante sellada)" % len(nominas))
    total_instrumento = sum(len(list(combinations(n, 2))) for n in nominas)
    p("   CIFRA PARES QUE EL INSTRUMENTO DA, sumados de sus nominas: %d (NO se "
      "mueve dentro de una vuelta: sale de la misma constante)" % total_instrumento)
    for i, n in enumerate(nominas, 1):
        p("      NOMINA %d: %-46s %d miembros, %d pares"
          % (i, n[0], len(n), len(list(combinations(n, 2)))))
    p("")

    p("A.1) LA CIFRA VIEJA DE LA FICHA, COMO CONTRASTE Y NUNCA COMO FUENTE")
    p("     (EJECUTOR.md 2: una nota vieja no es fuente de una cifra nueva. Se")
    p("     cita, y si discrepa de la medicion de hoy la discrepancia SE DECLARA)")
    ev, fecha, estado = cifra_vieja_de_la_ficha()
    for l in ev:
        p("     evidencia de la ficha: %s" % l)
    p("     fecha_corte de la ficha: %s | estado de la ficha: %s" % (fecha, estado))
    p("     LA DISCREPANCIA, DECLARADA Y NO RESUELTA COPIANDO: la evidencia de la")
    p("     ficha mide OTRO UNIVERSO, los pares FUERA DE COLA de todo el dominio,")
    p("     y esta corrida mide LAS SEIS NOMINAS que la constante declara. Las dos")
    p("     cifras son verdaderas y no son la misma pregunta.")
    p("     Y EL ESTADO DE LA FICHA NO ES LA VARA (TAREA 5 del encargo): la vara")
    p("     es la salida de scripts/loop/vuelta150_3_relectura_expediente.py.")
    p("")

    p("B) EL RESOLUTOR, EL GRAFO Y LAS DOS SEDES DE CLASE, PUESTOS ANTES DE CONTAR")
    mapa, n_nodos = T.mapa_de_alias()
    vivos_grafo = B.vivos_por_grafo()
    filas_v = T.veredictos()
    idx = B.veredictos_por_par(mapa)
    dirigidas = lecturas_dirigidas(mapa)
    p("   CIFRA ficheros de dataset/nodos/ leidos: %s"
      % sello(n_nodos, corte, "ficheros de dataset/nodos/ contados en esta corrida"))
    p("   CIFRA alias del mapa: %s"
      % sello(len(mapa), corte, "alias del resolutor contados en esta corrida"))
    p("   CIFRA nodos del grafo: %s"
      % sello(len(vivos_grafo), corte, "nodos del grafo contados en esta corrida"))
    p("   CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %s"
      % sello(len(filas_v), corte, "filas del archivo contadas en esta corrida"))
    p("   CIFRA pares distintos con veredicto tras resolver: %s"
      % sello(len(idx), corte, "pares con veredicto contados en esta corrida"))
    p("   CIFRA pares distintos con LECTURA DIRIGIDA tras resolver: %s"
      % sello(len(dirigidas), corte, "pares con lectura dirigida contados en esta corrida"))
    p("")

    p("C) LA MEDICION, NOMINA POR NOMINA Y CON LAS DOS COLUMNAS AL LADO")
    p("   EL CORTE DE ESTA TABLA, CABLEADO DONDE SE GENERA: HEAD %s" % corte)
    p("")
    p("| nomina (primer miembro) | miembros | vivos resolutor | vivos grafo | calzan | "
      "pares del instrumento | disueltos | con veredicto | con dirigida | REALES contra el archivo | "
      "REALES contra las dos sedes |")
    p("|---|---|---|---|---|---|---|---|---|---|---|")
    medidas = []
    for n in nominas:
        m = medir_nomina(n, mapa, vivos_grafo, idx, dirigidas)
        medidas.append((n[0], m))
        p("| `%s` | %d | %d | %d | %s | %d | %d | %d | %d | **%d** | **%d** |"
          % (n[0], m["cifra_miembros"], m["cifra_vivos_por_resolutor"],
             m["cifra_vivos_por_grafo"],
             "SI" if m["los_dos_caminos_calzan"] else "**NO**",
             m["cifra_pares_del_instrumento"], m["cifra_pares_disueltos"],
             m["cifra_pares_con_veredicto"], m["cifra_pares_con_dirigida"],
             m["cifra_reales_contra_el_archivo"],
             m["cifra_reales_contra_las_dos_sedes"]))
    p("")

    no_calzan = [(n, m) for n, m in medidas if not m["los_dos_caminos_calzan"]]
    p("D) LOS DOS CAMINOS, COTEJADOS NOMINA POR NOMINA")
    p("   CIFRA nominas medidas: %d" % len(medidas))
    p("   CIFRA nominas donde los dos caminos CALZAN: %s"
      % sello(sum(1 for _n, m in medidas if m["los_dos_caminos_calzan"]), corte,
              "nominas donde los dos caminos calzan contadas en esta corrida"))
    p("   CIFRA nominas donde NO calzan: %s"
      % sello(len(no_calzan), corte, "nominas donde no calzan contadas en esta corrida"))
    for nombre, m in no_calzan:
        p("      NO CALZAN en `%s`: resolutor dice %d vivos (%s) y el grafo dice %d (%s)"
          % (nombre, m["cifra_vivos_por_resolutor"], ", ".join(m["vivos_por_resolutor"]),
             m["cifra_vivos_por_grafo"], ", ".join(m["vivos_por_grafo"])))
    p("")

    ins = sum(m["cifra_pares_del_instrumento"] for _n, m in medidas)
    dis = sum(m["cifra_pares_disueltos"] for _n, m in medidas)
    con = sum(m["cifra_pares_con_veredicto"] for _n, m in medidas)
    dir_ = sum(m["cifra_pares_con_dirigida"] for _n, m in medidas)
    rea_a = sum(m["cifra_reales_contra_el_archivo"] for _n, m in medidas)
    rea_2 = sum(m["cifra_reales_contra_las_dos_sedes"] for _n, m in medidas)
    rea_d = sum(m["cifra_reales_que_ADEMAS_tienen_dirigida"] for _n, m in medidas)
    distintos = sum(m["cifra_pares_distintos_tras_resolver"] for _n, m in medidas)
    p("E) EL TOTAL, CON LAS DOS COLUMNAS Y SIN BORRAR LA VIEJA")
    p("")
    p("| cifra | valor | se mueve dentro de una vuelta |")
    p("|---|---|---|")
    p("| nominas que el instrumento da | **%d** | no, sale de una constante sellada |"
      % len(medidas))
    p("| PARES QUE EL INSTRUMENTO DA (la cifra vieja, que no se borra) | **%d** | no, sale de la misma constante |"
      % ins)
    p("| pares DISUELTOS (los dos extremos en el mismo nodo tras resolver) | **%s** | SI, depende del resolutor de dataset/ |"
      % sello(dis, corte, "pares disueltos contados en esta corrida"))
    p("| pares DISTINTOS tras resolver (dos escritos pueden ser UNO) | **%s** | SI, depende del resolutor de dataset/ |"
      % sello(distintos, corte, "pares distintos tras resolver contados en esta corrida"))
    p("| pares que YA TIENEN VEREDICTO en el archivo, por el par RESUELTO | **%s** | SI, depende de docs/INTRA_DOMINIO_VEREDICTOS.jsonl |"
      % sello(con, corte, "pares con veredicto contados en esta corrida"))
    p("| pares con LECTURA DIRIGIDA escrita | **%s** | SI, depende de docs/plan/*.md |"
      % sello(dir_, corte, "pares con lectura dirigida contados en esta corrida"))
    p("| PARES REALES contra el archivo (la definicion literal del encargo) | **%s** | SI, es la resta |"
      % sello(rea_a, corte, "pares reales contra el archivo contados en esta corrida"))
    p("| PARES REALES contra las DOS sedes (lo que queda de verdad) | **%s** | SI, es la resta |"
      % sello(rea_2, corte, "pares reales contra las dos sedes contados en esta corrida"))
    p("")
    p("   LAS RESTAS, COMPROBADAS, Y VAN EN TRES PASOS PORQUE HACEN FALTA TRES.")
    p("   EL PASO DEL MEDIO ES EL QUE LA PRIMERA CORRIDA DE ESTE INSTRUMENTO SE")
    p("   COMIO, Y SU PROPIA GUARDA LO CAZO: dos parejas de miembros ESCRITAS")
    p("   distintas pueden resolver AL MISMO par, y entonces hay UNA lectura que")
    p("   hacer y no dos. Restar sobre los pares escritos, sin colapsar primero,")
    p("   no cuadra nunca. Es la misma trampa que backlog_l03_resuelto.py declara")
    p("   en su medir_acto(), y aqui volvio a morder.")
    p("   PASO 1: del instrumento %d, menos %d disueltos, quedan %d ESCRITOS."
      % (ins, dis, ins - dis))
    p("   PASO 2: de esos %d escritos, los DISTINTOS tras resolver son %d, o sea "
      "%d duplicados que colapsan." % (ins - dis, distintos, ins - dis - distintos))
    p("   PASO 3: de los %d distintos, %d ya tienen veredicto y quedan %d."
      % (distintos, con, distintos - con))
    p("   Y los REALES contra el archivo medidos son %d. CALZA: %s"
      % (rea_a, "SI" if distintos - con == rea_a else "NO"))
    p("   PASO 4: de esos %d reales, %d tienen ADEMAS lectura dirigida escrita, y "
      "quedan %d." % (rea_a, rea_d, rea_a - rea_d))
    p("   Y los REALES contra las dos sedes medidos son %d. CALZA: %s"
      % (rea_2, "SI" if rea_a - rea_d == rea_2 else "NO"))
    resta_ok = (distintos - con == rea_a) and (rea_a - rea_d == rea_2)
    p("")

    p("F) EL REPARTO POR TRAMO, CON SU CORTE PEGADO")
    p("   EL CRITERIO, DICHO ANTES DE REPARTIR: una nomina esta YA MIRADA si")
    p("   alguno de sus pares tiene LECTURA DIRIGIDA escrita, y SIN MIRAR si")
    p("   ninguno. No se teclea ninguna lista: se lee de docs/plan/*.md.")
    p("   EL CORTE DE ESTA TABLA, CABLEADO DONDE SE GENERA: HEAD %s" % corte)
    p("")
    p("| tramo | nominas | pares del instrumento | reales contra el archivo | "
      "reales contra las dos sedes | corte |")
    p("|---|---|---|---|---|---|")
    for etiqueta, filtro in (("YA MIRADAS", True), ("SIN MIRAR", False)):
        sub = [(n, m) for n, m in medidas
               if (m["cifra_pares_con_dirigida"] > 0) == filtro]
        p("| %s | **%d** | **%d** | **%d** | **%d** | HEAD %s |"
          % (etiqueta, len(sub),
             sum(m["cifra_pares_del_instrumento"] for _n, m in sub),
             sum(m["cifra_reales_contra_el_archivo"] for _n, m in sub),
             sum(m["cifra_reales_contra_las_dos_sedes"] for _n, m in sub), corte))
    p("| **todas** | **%d** | **%d** | **%d** | **%d** | HEAD %s |"
      % (len(medidas), ins, rea_a, rea_2, corte))
    p("")

    p("G) LOS CINCO PARES DE SALES ROADMAP, NOMBRADOS Y DEJADOS")
    p("   docs/plan/LECTURAS_DIRIGIDAS.md los deja expresamente como DECISION")
    p("   REVOCABLE DEL FUNDADOR, y el punto 8 del acta 179 los sube. AQUI NO SE")
    p("   TOCAN: se nombran para que no se pierdan, y se dice de que fichero salen.")
    cinco = [(k, v) for k, v in dirigidas.items()
             if v[1] == "LD_SALES_ROADMAP.md"]
    p("   CIFRA pares con lectura dirigida en LD_SALES_ROADMAP.md: %s"
      % sello(len(cinco), corte, "pares de sales roadmap contados en esta corrida"))
    for k, v in sorted(cinco, key=lambda kv: sorted(kv[0])):
        a, b = sorted(k)
        p("      `%s` contra `%s` | clase %s | sede %s" % (a, b, v[0], v[1]))
    p("")

    p("H) LO QUE ESTA CORRIDA NO HIZO, DICHO Y NO INSINUADO")
    p("   pares leidos: 0. veredictos escritos: 0. filas anadidas al archivo: 0.")
    p("   marcador tocado: no. estado de fichas tocado: no. nodos tocados: 0.")
    p("")

    if no_calzan:
        p("ROJO: los dos caminos NO CALZAN en %d nomina(s), nombradas arriba. Una "
          "cifra agregada sobre una nomina donde el resolutor y el grafo se "
          "contradicen no vale nada." % len(no_calzan))
        p("FIN")
        return 1
    if not resta_ok:
        p("ROJO: las restas no calzan, y una cifra que no cuadra con sus partes no "
          "se publica.")
        p("FIN")
        return 1
    p("VERDE: los dos caminos calzan en las %d nominas medidas. El instrumento "
      "viejo da %d pares y quedan %d reales contra el archivo y %d contra las dos "
      "sedes, con %d disueltos, %d ya con veredicto y %d con lectura dirigida. "
      "LAS DOS COLUMNAS VAN LAS DOS Y LA VIEJA NO SE BORRA. NI UN PAR LEIDO."
      % (len(medidas), ins, rea_a, rea_2, dis, con, dir_))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
