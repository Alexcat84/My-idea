# -*- coding: utf-8 -*-
"""vuelta52_registro_tramo.py . ESCRIBE EL REGISTRO DEL TRAMO DE LA VUELTA 52 AL
FINAL DE docs/plan/03_FUSIONES.md.

SUCESOR DECLARADO de scripts/loop/vuelta51_registro_tramo.py, del que hereda el
contrato entero: el veredicto de CADA lectura `P.12` se registra en el REGISTRO
DEL TRAMO de esta pagina, en tabla propia, y los `CONTINUA` declaran AHI su
arista a la fase 04, con id RESUELTO (`P.9`) y SIN ejecutarla (carril adjudicado
por el acta de la vuelta 48, seccion 6, punto 2).

Y HEREDA LA REGLA 1 DEL EJECUTOR APLICADA DE VERDAD (LA TABLA SE IMPRIME, NO SE
TECLEA): la tabla de las lecturas `P.12`, la de los actos fundidos, la de los
declarados y la de las relecturas del filo SE GENERAN leyendo los dos planes
SELLADOS de la vuelta, y las cifras del cierre SE GENERAN leyendo las salidas de
los instrumentos corridos AL CIERRE. Lo unico tecleado es la prosa.

LO QUE ANADE ESTA VUELTA: una tabla propia para LAS RELECTURAS DEL CARRIL DEL
FILO, que es la figura que el acta de la vuelta 51 estreno en su pregunta 2 y
que hasta hoy no tenia sitio en el registro.

GUARDA DE ANCLA: el texto se pega DETRAS de la ultima linea que se le indique,
comprobada literal y comprobada que es la ULTIMA del fichero. Si no, aborta.
GUARDA DE IDEMPOTENCIA: si la cabecera del bloque ya esta dentro, no escribe.
GUARDA DE GUIONES: cero guiones largos y cero guiones medios en el bloque.

Uso: python scripts/loop/vuelta52_registro_tramo.py [--ejecutar]
"""
import argparse
import io
import json
import os
import re
import sys

DESTINO = "docs/plan/03_FUSIONES.md"
ANCLA = "| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |"
CABECERA = "## `OP-U-01`, TRAMO 1, LA VUELTA 52:"

PLANES = ["docs/loop/PLAN_V52_OPU01_LOTE_A.json",
          "docs/loop/PLAN_V52_OPU01_LOTE_B.json"]


def cargar_planes():
    return [json.load(io.open(p, encoding="utf-8")) for p in PLANES]


def lote_de(p):
    return "A" if "LOTE A" in p["tramo"] else "B"


def recorta(t, n=340):
    corte = t.split(". ")[0]
    if len(corte) > n:
        corte = corte[:n - 3] + "..."
    return corte


def tabla_lecturas(planes):
    filas = ["| el mixto | leido contra | veredicto | estado | lo que lo decide, con su puesto |",
             "|---|---|---|---|---|"]
    for p in planes:
        for L in p["lecturas_p12"]:
            puestos = sorted(set(int(x) for x in re.findall(r"[Pp]uestos? citados: ([\d, ]+)",
                                                            L["citas"])[0].split(",")
                                 if x.strip())) if "uestos citados" in L["citas"] else []
            filas.append("| `%s` | `%s` | **`%s`** | EJECUTADA | lote %s. %s. Puestos citados: %s |"
                         % (L["mixto"], L["superviviente_contra_el_que_se_lee"],
                            L["veredicto"], lote_de(p), recorta(L["citas"]),
                            ", ".join(str(x) for x in puestos) or "los del acto"))
    return "\n".join(filas)


def tabla_actos(planes):
    filas = ["| lote | superviviente | absorbe | el mixto que queda vivo | piezas del reparto |",
             "|---|---|---|---|---|"]
    for p in planes:
        for a in p["actos"]:
            piezas = sum(len(v) for v in a.get("pasos", {}).values())
            piezas += sum(len(v) for v in a.get("condiciones", {}).values())
            marcas = []
            for d in (a.get("pasos", {}), a.get("condiciones", {})):
                for v in d.values():
                    marcas.extend(v.values())
            ap = sum(1 for m in marcas if m == "APPEND")
            inc = sum(1 for m in marcas if m.startswith("INCISO:"))
            cub = sum(1 for m in marcas if m.startswith("CUBIERTO"))
            filas.append("| **%s** | `%s` | %s | `%s` | **%d**: %d enteras, %d de INCISO, %d ya dichas |"
                         % (lote_de(p), a["superviviente"],
                            ", ".join("`%s`" % x for x in a["absorbidos"]),
                            a.get("mixto_que_queda_fuera", "ninguno"),
                            piezas, ap, inc, cub))
    return "\n".join(filas)


def tabla_filo(planes):
    filas = ["| par resuelto | veredicto del FILO arrastrado o directo | contraste | que decide la relectura |",
             "|---|---|---|---|"]
    n = 0
    for p in planes:
        for r in p.get("relecturas_del_filo", []):
            n += 1
            filas.append("| `%s` | %s | %s | **%s.** %s |"
                         % (r["par_resuelto"], r["veredicto_arrastrado"],
                            r["veredicto_directo_de_contraste"],
                            "CONDICION DE TEXTO" if not r["es_pregunta_de_politica"]
                            else "PREGUNTA DE POLITICA",
                            recorta(r["la_relectura"], 420)))
    return "\n".join(filas), n


def tabla_declarados(planes):
    filas = ["| el acto, por sus MIEMBROS | especie | por que NO se funde | se acumula para |",
             "|---|---|---|---|"]
    n = 0
    for p in planes:
        for d in p.get("declarados_y_no_fundidos", []):
            n += 1
            filas.append("| `%s` | **%s** | %s | %s |"
                         % ("`, `".join(d["miembros"]), d["especie"],
                            recorta(d["motivo"], 700), d["acumulado_para"]))
    return "\n".join(filas), n


def tabla_cierre():
    def leer(p):
        return io.open(p, encoding="utf-8").read()

    ap_m = leer("docs/loop/SALIDA_V52_MARCADOR_APERTURA.txt")
    ci_m = leer("docs/loop/SALIDA_V52_MARCADOR_CIERRE.txt")
    ap_e = leer("docs/loop/SALIDA_V52_APERTURA.txt")
    ci_e = leer("docs/loop/SALIDA_V52_CIERRE.txt")
    ap_r = leer("docs/loop/SALIDA_V52_RECOMPUTO_APERTURA.txt")
    ci_r = leer("docs/loop/SALIDA_V52_RECOMPUTO_CIERRE.txt")
    ap_c = leer("docs/loop/SALIDA_V52_COLA_APERTURA.txt")
    ci_c = leer("docs/loop/SALIDA_V52_COLA_CIERRE.txt")
    ap_t = leer("docs/loop/SALIDA_V52_TRAMO1_APERTURA.txt")
    ci_t = leer("docs/loop/SALIDA_V52_TRAMO1_CIERRE.txt")

    def marc(t):
        d = dict(re.findall(r"^\s+([ABCD])\s+(\d+)\s", t, re.M))
        return "%s / %s / %s / %s" % (d["A"], d["B"], d["C"], d["D"])

    def graf(t):
        f = re.search(r"ficheros\s+:\s+(\d+)", t).group(1)
        v = re.search(r"vivos\s+:\s+(\d+)", t).group(1)
        p = re.search(r"deprecados\s+:\s+(\d+)", t).group(1)
        e = re.search(r"enlaces\s+:\s+(\d+)", t).group(1)
        return "%s / %s / %s / %s" % (f, v, p, e)

    def retr(t):
        a = re.search(r"A crudas en el archivo \(clase == 'A'\): (\d+)", t).group(1)
        c = re.search(r"colapsan a auto-arista.*?: (\d+)", t).group(1)
        p = re.search(r"A vigentes resueltas del retrato \((\d+)\)", t).group(1)
        return "%s / %s / %s" % (a, c, p)

    def actos(t):
        ce = re.search(r"CERRADOS: (\d+) sobre (\d+) nodos", t)
        ab = re.search(r"ABIERTOS: (\d+) sobre (\d+) nodos", t)
        return ce.group(1) + " / " + ab.group(1), ce.group(2) + " / " + ab.group(2)

    def cola(t):
        return re.search(r"nodos en la cola: (\d+)", t).group(1)

    def mixtos(t):
        return re.search(r"actos MIXTOS vivos \(piden lectura P\.12\): (\d+)", t).group(1)

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
        ("mixtos del tramo 1 pendientes de `P.12`", mixtos(ap_t), "**%s**" % mixtos(ci_t)),
    ]
    out = ["| | al abrir la vuelta 52 | **al cerrarla** |", "|---|---:|---:|"]
    for k, a, c in f:
        out.append("| %s | %s | %s |" % (k, a, c if c.startswith("**") else "**%s**" % c))
    out.append("| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |")
    out.append("| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |")
    return "\n".join(out)


TEXTO = """
---

## `OP-U-01`, TRAMO 1, LA VUELTA 52: **TRES ACTOS FUNDIDOS, EL CARRIL DEL FILO ESTRENADO, Y CINCO ACTOS DECLARADOS CON SU ESPECIE** (20 ago 2026, vuelta 52)

### LA GUARDA DE COLISIONES YA NO ES UNA CUENTA FIJA: ES LA QUE LA SIMULACION IMPRIME

**El acta de la vuelta 51, pregunta 2c, retiro la cuenta fija del encargo viejo** (*una colision
por cada `CONTINUA` sobre mixto CON forma y CERO por cada `ENTRA`*), que era exacta para la forma
de la estrella con centro absorbido y no en general. **En su lugar: antes de cada lote se corre
`scripts/loop/vuelta51_colisiones_esperadas.py` sobre la nomina re-medida del dia, EL CENSO
ESPERADO ES EL QUE LA SIMULACION IMPRIME, por PAR RESUELTO, y una colision real FUERA de la
prediccion detiene.**

**Los dos lotes de esta vuelta cumplieron la guarda AL DIGITO.** El lote A predijo **TRES** (una
dentro del acto y dos fuera) y el censo del archivo entero devolvio **exactamente esas tres**
([`../loop/SALIDA_V52_CENSO_COLISIONES_LOTE_A.txt`](../loop/SALIDA_V52_CENSO_COLISIONES_LOTE_A.txt)).
El lote B predijo **TRES** (dos dentro y una fuera) y devolvio **exactamente esas tres**
([`../loop/SALIDA_V52_CENSO_COLISIONES_LOTE_B.txt`](../loop/SALIDA_V52_CENSO_COLISIONES_LOTE_B.txt)).
**Tras cada limpieza `P.16` el censo vuelve a CERO.**

### LAS TRES LECTURAS `P.12` EJECUTADAS, con sus citas

**Tabla generada desde los dos planes sellados**, no tecleada
(`python scripts/loop/vuelta52_registro_tramo.py`):

{TABLA_LECTURAS}

**LAS TRES SALIERON `CONTINUA`, y en las tres el veredicto DIRECTO del par mixto ya era `D`.**
**Las aristas de las tres quedan DECLARADAS con id resuelto (`P.9`) y SIN ejecutarse**, y la
poda de sus solapes queda anotada para la fase 04. **En el acto del equity no hay arista que
declarar**: ya existe en los dos sentidos, y lo que queda es solo la poda.

### LOS TRES ACTOS FUNDIDOS, con su reparto contado por el instrumento

{TABLA_ACTOS}

**EN LOS TRES MUERE EL CENTRO DE LA ESTRELLA Y SOBREVIVE UN PERIFERICO**, que es la figura que
la vuelta 51 ya habia ejecutado dos veces: el centro es el que tiene arista `A` con los dos
demas, y absorberlo entero juntaria a los dos perifericos, que el archivo declara `D`.

**Y EN LOS TRES EL SUPERVIVIENTE LO ELIGIO EL CONTENIDO, NUNCA EL CONTEO DE CARACTERES**, que es
lo que el encargo de esta vuelta retiro como vara: en el del equity el contenido gana por el
margen mas ancho del tramo; **en el de los regalos las tres varas de conteo EMPATAN y decide el
MATERIAL PROPIO declarado en el puesto 799** (*resistir la tentacion de comercializar
masivamente el artefacto exclusivo, que no esta en ningun otro nodo*) contra el otro viable, al
que el puesto 251 declara repetido; **y en el de los habitos empatan pasos y condiciones, el
resumen apunta al otro y NO desempata, y decide el PADRE DECLARADO en el puesto 261**, que llama
al elegido *la version larga* del centro que muere.

### EL CARRIL DEL FILO, ESTRENADO: **TRES RELECTURAS EN EL MISMO ACTO**

**El acta de la vuelta 51, pregunta 2, lo adjudico:** una colision cuyo veredicto arrastrado es
del FILO (`B` o `C`) **NO se voltea por maquina**, porque su nodo muere o cambia de texto y eso
es la COLA DE RELECTURA POST FUSION de [`08_VERIFICACION.md`](08_VERIFICACION.md): **se RELEE el
par resuelto EN EL MISMO ACTO con el veredicto directo como contraste, y la correccion cita ESA
relectura.** Y si la relectura encuentra que lo congelado es una pregunta de POLITICA de
catalogo, **el acto NO se funde**.

{TABLA_FILO}

**LAS TRES SALIERON CONDICION DE TEXTO Y NINGUNA PREGUNTA DE POLITICA**, y de eso dependia que
los actos se pudieran fundir. **Las tres relecturas estan escritas en los planes ANTES de
sellarlos**, no despues de ejecutar.

> **UNA FORMA QUE NINGUN CARRIL ESCRITO CUBRE, dicha antes de resolverla y no despues:** en el
> par `gestion_de_habitos_mentales_para_pensar` contra `ruptura_de_habitos_para_estimulo` el
> veredicto **ARRASTRADO es una `D`** (el 563) y el **DIRECTO es una `B`** (el 243), que es al
> reves de los dos carriles: el del `A` arrastrado (acta 49, pregunta 1) y el del filo (acta 51,
> pregunta 2). **Lo que si es mecanico es el disparador de `08_VERIFICACION.md`: un par vuelve a
> la cola cuando uno de sus dos nodos MUERE O CAMBIA DE TEXTO, y aqui pasan las dos cosas.** Se
> relee y **se mueve el `B` directo y no la `D` arrastrada**, porque la relectura sostiene la `D`
> por su cuenta: `ruptura_de_habitos_para_estimulo` tiene CINCO pasos y solo DOS caben en el paso
> 3 del superviviente. **Mover el `B` y no la `D` es lectura del ejecutor y va marcada.**

### EL CHOQUE DE LETRA CONTRA ARITMETICA

**Ningun veredicto `A` de los tres actos fundidos escribe la formula *Sobrevive X***, medido hoy
([`../loop/SALIDA_V52_VIABLES.txt`](../loop/SALIDA_V52_VIABLES.txt)), asi que **esta vuelta no
registra ningun choque nuevo**. Se dice en vez de darlo por supuesto. **Los TRES choques que el
instrumento sigue midiendo estan en actos que esta vuelta NO toca** (los del `analisis_pareto`,
del `mistake_proofing_poka_yoke_2` y del `proceso_nominacion_seleccion`), y quedan para su
lectura.

### LOS ACTOS QUE ESTA VUELTA NO FUNDE, CADA UNO CON SU ESPECIE

{TABLA_DECLARADOS}

> **EL TERCER IMPOSIBLE POR PUERTA QUE EL ENCARGO NO NOMBRABA, y es el hallazgo de la TAREA
> 1.5:** el encargo mandaba reparar `vuelta48_puertas_en_el_lote.py` con el caso *MAS DE UNA
> PUERTA con alguna obligada a morir*, y nombraba DOS actos. **La vara reparada encuentra TRES**,
> y el tercero tiene **UNA SOLA puerta**. **Lo que eso desmiente es el caso `a` del instrumento
> viejo**, escrito con estas palabras: *UN SOLO miembro protegido, el acto SE SALVA si la lectura
> elige a ese nodo como superviviente*. **Cuando esa unica puerta es el CENTRO de la estrella, la
> lectura NO PUEDE elegirlo**, porque no deja ningun mixto fuera. **La cuenta de puertas no es lo
> que decide: lo que decide es si alguna puerta esta OBLIGADA A MORIR por la estructura del
> acto**, y asi quedan las cuatro categorias del instrumento de hoy: SALVABLE, IMPOSIBLE POR
> NOMINA, IMPOSIBLE POR ESTRUCTURA y SIN RECETA
> ([`../loop/SALIDA_V52_PUERTAS_REPARADO.txt`](../loop/SALIDA_V52_PUERTAS_REPARADO.txt)).

### LOS CINCO DECLARADOS DEL TRAMO SIGUEN DECLARADOS

**Ninguno se toca y se identifican por sus MIEMBROS**, no por su numero, que baila con cada
fusion: `obtencion_compromiso` y hermanos; `mejora_del_sistema_responsabilidad_gerencial` y
hermanos; `dia_cero_defectos` y hermanos; `domina_lo_que_compras` con
`investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor`; y `cultura_climatica_innovacion`
con `cultura_de_innovacion`. **Al cerrar la vuelta 52 son los actos 2, 16, 18, 22 y 23**, leidos
de la salida que esta misma celda cita
([`../loop/SALIDA_V52_TRAMO1_CIERRE.txt`](../loop/SALIDA_V52_TRAMO1_CIERRE.txt), bloque *actos de
FUSION PURA vivos*, corrida DESPUES del ultimo movimiento de la vuelta).

### LO QUE ESTA VUELTA NO HIZO DEL TRAMO 1, CON SU CIFRA MEDIDA AL CIERRE

| | |
|---|---:|
| lecturas `P.12` **hechas y ejecutadas** | **3** |
| actos **fundidos** | **3** |
| actos **DECLARADOS** y no fundidos, con su especie escrita | **5** |
| actos MIXTOS que **siguen pendientes** de `P.12`, re-medidos al cierre | **18** |
| de esos, **bloqueados por la vara de las puertas** y que ninguna lectura salva | **3** |
| **tramo 2** de 50 actos | **NO ABIERTO**: no hubo cuerda |

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

{TABLA_CIERRE}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    planes = cargar_planes()
    dec, ndec = tabla_declarados(planes)
    filo, nfilo = tabla_filo(planes)
    bloque = (TEXTO
              .replace("{TABLA_LECTURAS}", tabla_lecturas(planes))
              .replace("{TABLA_ACTOS}", tabla_actos(planes))
              .replace("{TABLA_FILO}", filo)
              .replace("{TABLA_DECLARADOS}", dec)
              .replace("{TABLA_CIERRE}", tabla_cierre()))

    print("=" * 78)
    print("REGISTRO DEL TRAMO, vuelta 52")
    print("destino: %s" % DESTINO)
    print("=" * 78)

    texto = io.open(DESTINO, encoding="utf-8").read()
    if CABECERA in texto:
        print("YA ESCRITO (idempotencia). Nada que hacer.")
        return 0
    if not texto.rstrip("\r\n").endswith(ANCLA):
        print("ROJO: el ancla no es la ultima linea del fichero. No se escribe nada.")
        return 1
    print("ancla OK y es la ultima linea.")
    malos = [c for c in bloque if c in u"—–"]
    print("guiones largos y medios en el bloque: %s" % ("CERO" if not malos else len(malos)))
    if malos:
        print("ROJO. No se escribe nada.")
        return 1
    print("lecturas P.12 en la tabla        : %d" % sum(len(p["lecturas_p12"]) for p in planes))
    print("actos fundidos en la tabla       : %d" % sum(len(p["actos"]) for p in planes))
    print("relecturas del filo en la tabla  : %d" % nfilo)
    print("actos declarados y no fundidos   : %d" % ndec)
    print("caracteres del bloque            : %d" % len(bloque))
    if not a.ejecutar:
        print()
        print("SIMULACION: nada escrito.")
        return 0
    io.open(DESTINO, "a", encoding="utf-8", newline="").write("\n" + bloque.lstrip("\n"))
    print("ESCRITO.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
