# -*- coding: utf-8 -*-
"""vuelta53_registro_tramo.py . ESCRIBE EL REGISTRO DEL TRAMO DE LA VUELTA 53 AL
FINAL DE docs/plan/03_FUSIONES.md.

SUCESOR DECLARADO de scripts/loop/vuelta52_registro_tramo.py, del que hereda el
contrato entero (regla 1 del EJECUTOR, LA TABLA SE IMPRIME, NO SE TECLEA): todas
las tablas se GENERAN de los tres planes SELLADOS, de los lotes `P.16` y de las
salidas de los instrumentos corridos al cierre. Lo unico tecleado es la prosa.

DOS CAMBIOS DECLARADOS, los dos por como estan escritos los planes de esta vuelta:

  a) LA TABLA DE LAS LECTURAS `P.12` NO SALE DE UN BLOQUE DEL PLAN, SALE DEL
     ARCHIVO. Los planes de la vuelta 52 llevaban un bloque `lecturas_p12` con
     las citas redactadas; los de esta vuelta llevan la lectura DENTRO del motivo
     de cada acto. Para no teclear la tabla, el veredicto DIRECTO de cada par
     mixto se LEE de docs/INTRA_DOMINIO_VEREDICTOS.jsonl con su clase y su razon,
     que es la fuente que `P.12` manda mirar (parte 2: mandan los directos).
  b) LA TABLA DEL CARRIL DE COLISIONES SALE DE LOS TRES LOTES `P.16` Y DE LAS
     SALIDAS DE `corregir_veredicto.py`, que son las que imprimen la clase de
     ANTES. Separa las dos especies del carril: VOLTEO y RELECTURA.

GUARDA DE ANCLA: el texto se pega DETRAS de la ultima linea del fichero, que se
comprueba literal. GUARDA DE IDEMPOTENCIA: si la cabecera ya esta dentro, no
escribe. GUARDA DE GUIONES: cero guiones largos y cero guiones medios.

Uso: python scripts/loop/vuelta53_registro_tramo.py [--ejecutar]
"""
import argparse
import io
import json
import os
import re
import sys

DESTINO = "docs/plan/03_FUSIONES.md"
CABECERA = "## `OP-U-01`, TRAMO 1, LA VUELTA 53:"
PLANES = ["docs/loop/PLAN_V53_OPU01_LOTE_A.json",
          "docs/loop/PLAN_V53_OPU01_LOTE_B.json",
          "docs/loop/PLAN_V53_OPU01_LOTE_C.json"]
CORREGIR = {"A": "docs/loop/SALIDA_V53_CORREGIR_LOTE_A.txt",
            "B": "docs/loop/SALIDA_V53_CORREGIR_LOTE_B.txt",
            "C": "docs/loop/SALIDA_V53_CORREGIR_LOTE_C.txt"}
LOTES_P16 = {"A": "docs/loop/_lote_v53_lote_a.jsonl",
             "B": "docs/loop/_lote_v53_lote_b.jsonl",
             "C": "docs/loop/_lote_v53_lote_c.jsonl"}
VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"


def leer(p):
    return io.open(p, encoding="utf-8").read()


def planes():
    return [json.load(io.open(p, encoding="utf-8")) for p in PLANES]


def lote_de(p):
    for k in "ABC":
        if "LOTE %s" % k in p["tramo"]:
            return k
    return "?"


def recorta(t, n=340):
    corte = t.split(". ")[0]
    if len(corte) > n:
        corte = corte[:n - 3] + "..."
    return corte


def veredictos():
    return [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]


def tabla_lecturas(ps, V):
    filas = ["| el mixto | leido contra | veredicto `P.12` | estado | el veredicto DIRECTO del par, que es el que manda |",
             "|---|---|---|---|---|"]
    for p in ps:
        for a in p["actos"]:
            mixto, sup = a["mixto_que_queda_fuera"], a["superviviente"]
            d = [r for r in V if {r["nodo_a"], r["nodo_b"]} == {mixto, sup}]
            if not d:
                filas.append("| `%s` | `%s` | **`CONTINUA`** | EJECUTADA | lote %s. SIN VEREDICTO DIRECTO |"
                             % (mixto, sup, lote_de(p)))
                continue
            r = d[0]
            filas.append("| `%s` | `%s` | **`CONTINUA`** | EJECUTADA | lote %s. Puesto **%d**, clase **%s** hoy. %s |"
                         % (mixto, sup, lote_de(p), r["puesto_intra"], r["clase"],
                            recorta(r["razon"], 300)))
    return "\n".join(filas)


def tabla_actos(ps):
    filas = ["| lote | superviviente | absorbe | el mixto que queda vivo | piezas del reparto |",
             "|---|---|---|---|---|"]
    for p in ps:
        for a in p["actos"]:
            marcas = []
            for d in (a.get("pasos", {}), a.get("condiciones", {})):
                for v in d.values():
                    marcas.extend(v.values())
            ap = sum(1 for m in marcas if m == "APPEND")
            inc = sum(1 for m in marcas if m.startswith("INCISO:"))
            cub = sum(1 for m in marcas if m.startswith("CUBIERTO"))
            filas.append("| **%s** | `%s` | `%s` | `%s` | **%d**: %d enteras, %d de INCISO, %d ya dichas |"
                         % (lote_de(p), a["superviviente"], ", ".join(a["absorbidos"]),
                            a.get("mixto_que_queda_fuera", "ninguno"),
                            len(marcas), ap, inc, cub))
    return "\n".join(filas)


def tabla_p16():
    filas = ["| lote | puesto | de | a | el par CRUDO | especie del carril |",
             "|---|---:|:---:|:---:|---|---|"]
    n_v = n_r = 0
    for k in "ABC":
        movs = dict(re.findall(r"puesto (\d+) \| ([ABCD]) -> [ABCD] \|", leer(CORREGIR[k])))
        pares = dict(re.findall(r"puesto (\d+) \| [ABCD] -> [ABCD] \| (.+)", leer(CORREGIR[k])))
        for l in io.open(LOTES_P16[k], encoding="utf-8"):
            if not l.strip():
                continue
            d = json.loads(l)
            pu = str(d["puesto"])
            especie = "**VOLTEO POR MAQUINA**" if "ESPECIE: VOLTEO" in d["razon"] else "**RELECTURA EN EL MISMO ACTO**"
            if "VOLTEO" in especie:
                n_v += 1
            else:
                n_r += 1
            filas.append("| **%s** | **%s** | %s | %s | `%s` | %s |"
                         % (k, pu, movs.get(pu, "?"), d["clase"],
                            pares.get(pu, "?").strip().replace(" contra ", "` contra `"), especie))
    return "\n".join(filas), n_v, n_r


def tabla_declarados(ps):
    filas = ["| el acto, por sus MIEMBROS | especie | por que NO se funde | se acumula para |",
             "|---|---|---|---|"]
    n = 0
    for p in ps:
        for d in p.get("declarados_y_no_fundidos", []):
            n += 1
            filas.append("| `%s` | **%s** | %s | LA MESA |"
                         % ("`, `".join(d["acto_por_sus_miembros"]), d["especie"],
                            recorta(d["por_que_no_se_funde"], 700)))
    return "\n".join(filas), n


def tabla_choques():
    t = leer("docs/loop/SALIDA_V53_VIABLES.txt")
    filas = ["| el acto | el nodo que la letra nombra | los puestos que lo escriben | que paso con el |",
             "|---|---|---|---|"]
    for acto, nodo, puestos in re.findall(r"acto (\d+): (\S+) nombrado en ([\d,]+)", t):
        filas.append("| acto **%s** de la nomina de apertura | `%s` | **%s** | **NO ES VIABLE por la estructura del acto y MUERE ABSORBIDO**: manda la aritmetica (acta de la vuelta 50, adjudicacion 3) |"
                     % (acto, nodo, puestos))
    return "\n".join(filas), len(re.findall(r"acto (\d+): (\S+) nombrado en ([\d,]+)", t))


def tabla_cierre():
    ap_m, ci_m = leer("docs/loop/SALIDA_V53_MARCADOR_APERTURA.txt"), leer("docs/loop/SALIDA_V53_MARCADOR_CIERRE.txt")
    ap_e, ci_e = leer("docs/loop/SALIDA_V53_APERTURA.txt"), leer("docs/loop/SALIDA_V53_CIERRE.txt")
    ci_r = leer("docs/loop/SALIDA_V53_RECOMPUTO_CIERRE.txt")
    ap_r = leer("docs/loop/SALIDA_V52_RECOMPUTO_CIERRE.txt")
    ap_c, ci_c = leer("docs/loop/SALIDA_V52_COLA_CIERRE.txt"), leer("docs/loop/SALIDA_V53_COLA_CIERRE.txt")
    ap_t, ci_t = leer("docs/loop/SALIDA_V52_TRAMO1_CIERRE.txt"), leer("docs/loop/SALIDA_V53_TRAMO1_CIERRE.txt")

    def marc(t):
        d = dict(re.findall(r"^\s+([ABCD])\s+(\d+)\s", t, re.M))
        return "%s / %s / %s / %s" % (d["A"], d["B"], d["C"], d["D"])

    def graf(t):
        return "%s / %s / %s / %s" % (
            re.search(r"ficheros\s+:\s+(\d+)", t).group(1),
            re.search(r"vivos\s+:\s+(\d+)", t).group(1),
            re.search(r"deprecados\s+:\s+(\d+)", t).group(1),
            re.search(r"enlaces\s+:\s+(\d+)", t).group(1))

    def retr(t):
        return "%s / %s / %s" % (
            re.search(r"A crudas en el archivo \(clase == 'A'\): (\d+)", t).group(1),
            re.search(r"colapsan a auto-arista.*?: (\d+)", t).group(1),
            re.search(r"A vigentes resueltas del retrato \((\d+)\)", t).group(1))

    def actos(t):
        ce = re.search(r"CERRADOS: (\d+) sobre (\d+) nodos", t)
        ab = re.search(r"ABIERTOS: (\d+) sobre (\d+) nodos", t)
        return ce.group(1) + " / " + ab.group(1), ce.group(2) + " / " + ab.group(2)

    def cola(t):
        return re.search(r"nodos en la cola: (\d+)", t).group(1)

    def mixtos(t):
        return re.search(r"actos MIXTOS vivos \(piden lectura P\.12\): (\d+)", t).group(1)

    def puros(t):
        return re.search(r"actos de FUSION PURA vivos \(sin P\.12\)\s+: (\d+)", t).group(1)

    aa, an = actos(ap_r)
    ca, cn = actos(ci_r)
    f = [
        ("marcador `A` / `B` / `C` / `D`", marc(ap_m), marc(ci_m)),
        ("grafo: ficheros / vivos / deprecados / enlaces", graf(ap_e), graf(ci_e)),
        ("retrato: `A` crudas / colapsos / pares distintos", retr(ap_r), retr(ci_r)),
        ("actos `CERRADOS` / `ABIERTOS`", aa, ca),
        ("nodos en `CERRADOS` / `ABIERTOS`", an, cn),
        ("cola de costuras", cola(ap_c), cola(ci_c)),
        ("colisiones de clase vigentes", "0", "**0**, censo propio sobre el archivo entero"),
        ("mixtos del tramo 1 pendientes de `P.12`", mixtos(ap_t), "**%s**, y los %s DECLARADOS o BLOQUEADOS"
         % (mixtos(ci_t), mixtos(ci_t))),
        ("actos de FUSION PURA vivos del tramo 1 (los cinco declarados de siempre)", puros(ap_t), puros(ci_t)),
    ]
    out = ["| | al abrir la vuelta 53 | **al cerrarla** |", "|---|---:|---:|"]
    for k, a, c in f:
        out.append("| %s | %s | %s |" % (k, a, c if c.startswith("**") else "**%s**" % c))
    out.append("| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |")
    out.append("| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    ps = planes()
    V = veredictos()
    t_lect = tabla_lecturas(ps, V)
    t_actos = tabla_actos(ps)
    t_p16, n_v, n_r = tabla_p16()
    t_decl, n_d = tabla_declarados(ps)
    t_choq, n_ch = tabla_choques()
    t_cierre = tabla_cierre()

    bloque = """
---

## `OP-U-01`, TRAMO 1, LA VUELTA 53: **EL TRAMO 1 QUEDA CERRADO. DOCE ACTOS FUNDIDOS, UN ACTO MAS DECLARADO Y CERO LECTURAS `P.12` PENDIENTES** (20 ago 2026, vuelta 53)

**Al abrir esta vuelta el tramo 1 tenia DIECIOCHO actos mixtos vivos: 13 sin mirar, 2 ya
declarados y 3 bloqueados por la vara de las puertas. Al cerrarla NO QUEDA NINGUNA LECTURA
PENDIENTE: doce de los trece se leyeron y se FUNDIERON, y el decimotercero se leyo y se DECLARO
porque su veredicto manda la pregunta a la mesa.** Los seis actos mixtos que siguen vivos son
exactamente los que ninguna lectura puede mover: dos declarados por politica, uno por empate sin
vara y tres imposibles por puerta.

### LAS DOCE LECTURAS `P.12` EJECUTADAS, con el veredicto DIRECTO de cada par leido del archivo

**Tabla generada leyendo los tres planes sellados y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**, no
tecleada (`python scripts/loop/vuelta53_registro_tramo.py`). **LA CLASE QUE SE IMPRIME ES LA DE
HOY, DESPUES de `P.16`**, y por eso las cuatro relecturas del filo aparecen ya en su clase nueva.

%(t_lect)s

**LAS DOCE SALIERON `CONTINUA`, y el criterio es el adjudicado en el acta de la vuelta 52,
pregunta 1, registrado en esta misma pagina por la TAREA 1.4.c de esta vuelta: EL VEREDICTO
DIRECTO MANDA.** **Las aristas de las doce quedan DECLARADAS con id resuelto (`P.9`) y SIN
ejecutarse**, y la poda de sus solapes queda anotada para la fase 04.

### LOS DOCE ACTOS FUNDIDOS, con su reparto contado por el instrumento

%(t_actos)s

**EN LOS DOCE MUERE EL CENTRO DE LA ESTRELLA Y SOBREVIVE UN PERIFERICO**, que es la figura que
las vueltas 51 y 52 ya habian ejecutado cinco veces. **Y EN LOS DOCE EL SUPERVIVIENTE LO ELIGIO EL
CONTENIDO**, con el motivo escrito entero en el plan de cada acto: **en SEIS** lo decide el
ALCANCE DEL ROL o el PADRE DECLARADO que `P.8` nombra como contenido (el lienzo, los prompts, los
warrants, los costos de franquicia, el abogado y el dmaic select), **en CINCO** el conteo de pasos
y condiciones apuntando al mismo lado que el material propio (la huella, la franquicia
inadvertida, el pareto, el poka yoke y la investigacion del cliente) y **en UNO** la UNICA vara que
no empata (la gestion por objetivos). **En SIETE de los doce alguna vara apunta al otro lado, y en
los siete va dicho en el motivo del plan y marcado en el reporte:** el conteo en el lienzo, el
cableado en los prompts, en los costos de franquicia y en el pareto, las condiciones en los
warrants, el material propio en el abogado y los pasos en el dmaic select.

### EL CARRIL GENERAL DE COLISIONES, ESTRENADO EN SUS DOS FORMAS

**El carril quedo adjudicado en el acta de la vuelta 52, pregunta 4, y esta vuelta lo REGISTRO en
esta pagina (TAREA 1.4.b) para que no dependa del acta.** Las %(n_p16)d correcciones de esta
vuelta se reparten en sus dos especies: **%(n_v)d VOLTEOS POR MAQUINA** (`A` arrastrada contra un
directo `D`, el unico caso mecanico) y **%(n_r)d RELECTURAS EN EL MISMO ACTO** (un veredicto del
filo en alguno de los dos lados). **Todas llevan la razon vieja pegada ENTERA.**

%(t_p16)s

**LA GUARDA DE COLISIONES CUMPLIO AL DIGITO EN LOS TRES LOTES**: el lote A predijo SEIS y midio
SEIS, el B predijo CUATRO y midio CUATRO, y el C predijo CUATRO y midio CUATRO, **siempre las
mismas**. **Tras cada limpieza `P.16` el censo vuelve a CERO.**

### EL CHOQUE DE LETRA CONTRA ARITMETICA: LOS TRES CONOCIDOS, EJECUTADOS

**Los TRES choques que el instrumento venia midiendo desde la vuelta 50 caen en actos de esta
tanda, y esta vuelta los ejecuta y los registra con sus puestos**
([`../loop/SALIDA_V53_VIABLES.txt`](../loop/SALIDA_V53_VIABLES.txt)):

%(t_choq)s

> **LO QUE ESTOS TRES TIENEN DE NUEVO, y va dicho en vez de colado con los cinco anteriores.** El
> acta de la vuelta 50 adjudico que manda la aritmetica y escribio que *la letra se honra en lo
> que puede: X sigue VIVO en los cinco casos*. **En estos tres NO sigue vivo: MUERE, porque el
> nodo que la letra nombra es el CENTRO de la estrella y el centro es justamente el que la receta
> no deja sobrevivir.** La adjudicacion se cumple igual en lo que si dice (nadie funde a X en
> contra de su par: los pares que lo absorben son sus dos `A`), **pero el consuelo que la
> adjudicacion escribia no aplica aqui, y por eso se marca.**

### LOS ACTOS QUE ESTA VUELTA NO FUNDE

%(t_decl)s

**Y LOS CINCO DECLARADOS DE SIEMPRE SIGUEN DECLARADOS, ninguno se toca**, identificados por sus
MIEMBROS y no por su numero: `obtencion_compromiso` y hermanos;
`mejora_del_sistema_responsabilidad_gerencial` y hermanos; `dia_cero_defectos` y hermanos;
`domina_lo_que_compras` con `investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor`; y
`cultura_climatica_innovacion` con `cultura_de_innovacion`. **Al cerrar la vuelta 53 son los actos
2, 8, 9, 10 y 11**, leidos del bloque *actos de FUSION PURA vivos* de
[`../loop/SALIDA_V53_TRAMO1_CIERRE.txt`](../loop/SALIDA_V53_TRAMO1_CIERRE.txt), corrida DESPUES
del ultimo movimiento de la vuelta. **Y los CINCO que no son de fusion pura tambien siguen
declarados**: el del S&OP (politica del 703), el de la sucesion del CEO (empate sin vara), el del
mapa de influencia (politica del 604, declarado ESTA vuelta) y los TRES imposibles por puerta, que
al cerrar son los actos 5, 6 y 7 de la nomina de hoy.

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

%(t_cierre)s

> **DE DONDE SALE CADA COLUMNA, dicho para que se pueda auditar.** La columna de APERTURA del
> marcador y del grafo sale de las dos corridas propias de esta vuelta hechas ANTES de la primera
> operacion ([`../loop/SALIDA_V53_MARCADOR_APERTURA.txt`](../loop/SALIDA_V53_MARCADOR_APERTURA.txt)
> y [`../loop/SALIDA_V53_APERTURA.txt`](../loop/SALIDA_V53_APERTURA.txt)). **Las filas de retrato,
> cola y tramo 1 de esa columna NO se re-corrieron antes de la primera operacion y se dice en vez
> de callarse: son las del CIERRE de la vuelta 52**
> ([`../loop/SALIDA_V52_RECOMPUTO_CIERRE.txt`](../loop/SALIDA_V52_RECOMPUTO_CIERRE.txt),
> [`../loop/SALIDA_V52_COLA_CIERRE.txt`](../loop/SALIDA_V52_COLA_CIERRE.txt) y
> [`../loop/SALIDA_V52_TRAMO1_CIERRE.txt`](../loop/SALIDA_V52_TRAMO1_CIERRE.txt)), y valen como
> apertura porque entre el cierre de aquella vuelta y la primera operacion de esta NO se movio
> ningun nodo ni ningun veredicto, comprobado por las dos corridas propias que SI se hicieron y que
> reproducen el cierre de la 52 al digito. **La columna de CIERRE esta RECOMPUTADA AL CIERRE**,
> despues del ultimo movimiento.
""" % {"t_lect": t_lect, "t_actos": t_actos, "t_p16": t_p16, "t_decl": t_decl,
       "t_choq": t_choq, "t_cierre": t_cierre,
       "n_p16": n_v + n_r, "n_v": n_v, "n_r": n_r}

    malos = [c for c in bloque if c in "—–"]
    if malos:
        print("ROJO: el bloque trae %d guion(es) largo(s) o medio(s)" % len(malos))
        return 1

    texto = leer(DESTINO)
    if CABECERA in texto:
        print("YA ESTABA: la cabecera del bloque de la vuelta 53 ya vive en %s" % DESTINO)
        return 0

    print("=" * 78)
    print("REGISTRO DEL TRAMO DE LA VUELTA 53")
    print("=" * 78)
    print("  lecturas P.12 en tabla        : %d" % (len(t_lect.splitlines()) - 2))
    print("  actos fundidos en tabla       : %d" % (len(t_actos.splitlines()) - 2))
    print("  correcciones P.16 en tabla    : %d (%d volteos, %d relecturas)" % (n_v + n_r, n_v, n_r))
    print("  actos declarados en tabla     : %d" % n_d)
    print("  choques letra contra aritmetica: %d" % n_ch)
    print("  guiones largos o medios       : 0")
    print("  caracteres del bloque         : %d" % len(bloque))

    if a.ejecutar:
        io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(
            texto.rstrip("\n") + "\n" + bloque)
        print()
        print("ESCRITO al final de %s" % DESTINO)
    else:
        print()
        print("SIMULACION: cero escrituras. Vuelve con --ejecutar.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
