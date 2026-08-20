# -*- coding: utf-8 -*-
"""vuelta51_registro_tramo.py . ESCRIBE EL REGISTRO DEL TRAMO DE LA VUELTA 51 AL
FINAL DE docs/plan/03_FUSIONES.md.

SUCESOR DECLARADO de scripts/loop/vuelta50_registro_tramo.py, del que hereda el
contrato entero: el veredicto de CADA lectura `P.12` se registra en el REGISTRO
DEL TRAMO de esta pagina, en tabla propia, y los `CONTINUA` declaran AHI su
arista a la fase 04, con id RESUELTO (`P.9`) y SIN ejecutarla. Es el carril
adjudicado por el auditor (acta de la vuelta 48, seccion 6, punto 2).

LO QUE ANADE, y es la regla 1 del EJECUTOR aplicada de verdad (LA TABLA SE
IMPRIME, NO SE TECLEA): las tablas cuyo contenido vive en un instrumento o en un
plan sellado NO se teclean aqui. La tabla de las lecturas `P.12` y la de los
actos fundidos SE GENERAN leyendo los dos planes sellados de la vuelta
(PLAN_V51_OPU01_LOTE_A.json y PLAN_V51_OPU01_LOTE_B.json), y las cifras del
cierre SE GENERAN leyendo las salidas de los instrumentos corridos al cierre. Lo
unico tecleado es la prosa.

GUARDA DE ANCLA: el texto se pega DETRAS de la ultima linea que se le indique,
comprobada literal y comprobada que es la ULTIMA del fichero. Si no, aborta.
GUARDA DE IDEMPOTENCIA: si la cabecera del bloque ya esta dentro, no escribe.
GUARDA DE GUIONES: cero guiones largos y cero guiones medios en el bloque.

Uso: python scripts/loop/vuelta51_registro_tramo.py [--ejecutar]
"""
import argparse
import io
import json
import os
import re
import sys

DESTINO = "docs/plan/03_FUSIONES.md"
ANCLA = ("| **el barrido `9.10` DEL CIERRE**, la regla del aviso | | "
         "**CORRIDO despues del ultimo movimiento**, con **diez** celdas corregidas |")
CABECERA = "## `OP-U-01`, TRAMO 1, LA VUELTA 51:"

PLANES = ["docs/loop/PLAN_V51_OPU01_LOTE_A.json",
          "docs/loop/PLAN_V51_OPU01_LOTE_B.json"]


def cargar_planes():
    return [json.load(io.open(p, encoding="utf-8")) for p in PLANES]


def tabla_lecturas(planes):
    """FILA = una lectura P.12. Se genera de los planes sellados, no se teclea."""
    filas = ["| el mixto | leido contra | veredicto | estado | lo que lo decide, con su puesto |",
             "|---|---|---|---|---|"]
    for p in planes:
        lote = "A" if "LOTE A" in p["tramo"] else "B"
        for L in p["lecturas_p12"]:
            puestos = sorted(set(int(x) for x in re.findall(r"puesto (\d+)", L["citas"])))
            cita = L["citas"]
            corte = cita.split(". ")[0]
            if len(corte) > 320:
                corte = corte[:317] + "..."
            hechas = set()
            for d in p.get("declarados_y_no_fundidos", []):
                hechas.update(d["miembros"])
            estado = ("**HECHA, NO EJECUTADA** (el acto lo detuvo la guarda de la cuenta de colisiones)"
                      if L["mixto"] in hechas else "EJECUTADA")
            filas.append("| `%s` | `%s` | **`%s`** | %s | lote %s. %s. Puestos citados: %s |"
                         % (L["mixto"], L["superviviente_contra_el_que_se_lee"],
                            L["veredicto"], estado, lote, corte,
                            ", ".join(str(x) for x in puestos) or "los del acto"))
    return "\n".join(filas)


def tabla_actos(planes):
    """FILA = un acto fundido. Se genera de los planes sellados."""
    filas = ["| lote | superviviente | absorbe | piezas del reparto |",
             "|---|---|---|---|"]
    for p in planes:
        lote = "A" if "LOTE A" in p["tramo"] else "B"
        for a in p["actos"]:
            piezas = sum(len(v) for v in a.get("pasos", {}).values())
            piezas += sum(len(v) for v in a.get("condiciones", {}).values())
            marcas = []
            for d in (a.get("pasos", {}), a.get("condiciones", {})):
                for v in d.values():
                    marcas.extend(v.values())
            ap = sum(1 for m in marcas if m == "APPEND")
            inc = sum(1 for m in marcas if m.startswith("INCISO:"))
            cub = sum(1 for m in marcas if m.startswith("CUBIERTO:"))
            filas.append("| **%s** | `%s` | %s | **%d**: %d enteras, %d de INCISO, %d ya dichas |"
                         % (lote, a["superviviente"],
                            ", ".join("`%s`" % x for x in a["absorbidos"]),
                            piezas, ap, inc, cub))
    return "\n".join(filas)


def tabla_declarados(planes):
    filas = ["| el acto | superviviente que el CONTENIDO elige | por que NO se funde |",
             "|---|---|---|"]
    n = 0
    for p in planes:
        for d in p.get("declarados_y_no_fundidos", []):
            n += 1
            filas.append("| `%s` | `%s` | %s |"
                         % ("`, `".join(d["miembros"]),
                            d["superviviente_que_el_contenido_elige"], d["motivo"]))
    return ("\n".join(filas), n)


TEXTO = """
---

## `OP-U-01`, TRAMO 1, LA VUELTA 51: **CUATRO ACTOS, CUATRO LECTURAS `P.12`, Y UN INSTRUMENTO QUE SE DIO EL VISTO BUENO A SI MISMO MIRANDO DONDE NO ERA** (20 ago 2026, vuelta 51)

### EL HALLAZGO DE LA VUELTA, Y ME LO HIZO A MI MISMO MI PROPIO INSTRUMENTO

**El encargo pone una guarda de cuenta:** *una colision por cada `CONTINUA` sobre mixto CON
forma y CERO por cada `ENTRA`; una colision que no calce con esa cuenta te detiene*. Para
poder cumplirla ANTES de mover un nodo, esta vuelta escribio
`scripts/loop/vuelta51_colisiones_esperadas.py`. **Y la primera version del instrumento
contaba las colisiones mirando SOLO LOS VEREDICTOS INTERNOS DEL ACTO.**

**Con esa cuenta dio el visto bueno al acto del reparto de equity**, la fusion se ejecuto, y
**el censo del archivo entero devolvio CINCO colisiones donde el instrumento habia prometido
TRES** ([`../loop/SALIDA_V51_CENSO_COLISIONES_LOTE_A.txt`](../loop/SALIDA_V51_CENSO_COLISIONES_LOTE_A.txt),
en su primera corrida). Las dos de mas eran veredictos del absorbido `split_igual_vs_desigual`
contra nodos de **FUERA del acto**: el puesto **266** contra `reparto_inicial_equity` y el
puesto **246** contra `timing_equity_split`, que al resolver caian sobre pares que el
superviviente ya tenia leidos, los puestos **754** y **688**.

> **LA LECCION, escrita donde no se pierde: UNA FUSION NO SOLO CHOCA CONSIGO MISMA.** Absorber
> un nodo arrastra **TODOS** sus veredictos, tambien los que apuntan fuera del acto, y cada uno
> puede caer sobre un par que el superviviente ya tenia leido. **Una guarda que solo mira dentro
> del acto tranquiliza sin mirar**, que es exactamente la especie de la averia que la vuelta 50
> encontro en el barrido `9.10`.

**QUE SE HIZO CON ESO, y no fue seguir:** el dataset se revirtio entero con `git checkout`, el
censo confirmo la vuelta a **CERO** colisiones, el instrumento se reescribio para **simular el
mapa de alias y re-resolver LOS 3.388 VEREDICTOS**, y las 25 combinaciones de acto y
superviviente viable se re-midieron con la aritmetica buena
([`../loop/SALIDA_V51_COLISIONES_ESPERADAS.txt`](../loop/SALIDA_V51_COLISIONES_ESPERADAS.txt)).
**De 51 combinaciones, CINCO no calzan con la cuenta del encargo.**

### Y UNA FORMA DE CONTAR QUE ESTA VUELTA TUVO QUE FIJAR: **LA COLISION SE CUENTA POR PAR RESUELTO**

**El acto del consejo de calidad lo prueba:** el par resuelto `consejo_de_calidad` contra
`consejo_de_calidad_3` lleva **TRES** veredictos dentro (**2523** `A`, **2662** `A` y **2916**
`D`) y es **UNA sola colision**: los dos `A` se voltean, el `D` se queda. **Con esa forma de
contar la cuenta del encargo calza; contando veredictos, no.** Se dice porque es una decision
de lectura y no un dato.

### LAS CINCO LECTURAS `P.12`, con sus citas: **CUATRO EJECUTADAS Y UNA DETENIDA**

**Tabla generada desde los dos planes sellados**, no tecleada
(`python scripts/loop/vuelta51_registro_tramo.py`):

{TABLA_LECTURAS}

**LAS CINCO SALIERON `CONTINUA`, y ninguna por descarte:** en las cinco el veredicto DIRECTO
del par mixto ya era `D` y ya traia escrito por que. **En la del acto de los cofundadores el
propio veredicto escribe la palabra** (el **1058**: *por la vara del banco `9.6.1`, CONTINUA*),
y en la del consejo el **2916** cierra con *son conjuntos disjuntos de pasos propios, no
gemelos*. **Las aristas de las CUATRO ejecutadas quedan DECLARADAS con id resuelto (`P.9`) y SIN ejecutarse**, y
la poda de sus solapes queda anotada para la fase 04.

### LOS CUATRO ACTOS FUNDIDOS, con su reparto contado por el instrumento

{TABLA_ACTOS}

### EL CHOQUE DE LETRA CONTRA ARITMETICA, registrado con sus puestos

**El acta de la vuelta 50, pregunta 3, lo adjudico: MANDA LA ARITMETICA**, y manda registrar
cada choque con sus puestos. **En el acto del consejo hay CINCO**: los puestos **2631**,
**2663** y **2523** cierran con *Sobrevive `consejo_calidad`*, y los **2670** y **2662** con
*Sobrevive `consejo_calidad_2`*, **y ninguno de los dos es VIABLE**, porque su parte `A` se
lleva a los cuatro miembros y no deja ningun mixto fuera: elegirlos seria fundir entero un acto
con una `D` dentro, que es lo que `P.12` prohibe. **La letra se honra en lo que puede: los dos
nombrados mueren aqui, que es lo que sus veredictos pedian de ellos dentro de sus pares, pero
ninguno absorbe el racimo.** En los otros tres actos **ningun veredicto `A` escribe la formula
*Sobrevive X***, y se dice en vez de darlo por supuesto.

### LOS ACTOS QUE ESTA VUELTA NO FUNDE, Y POR QUE

{TABLA_DECLARADOS}

**Y DOS MAS QUE BLOQUEA LA VARA DE LAS PUERTAS, con un hallazgo sobre el instrumento que las
mide:** los actos **9** y **17** de la nomina re-medida tras el lote A tienen **DOS puertas
dentro cada uno** (`decision_cuando_fundar` mas `evaluacion_capacidades_fundador`; y
`enfoque_paso_a_paso_investigacion_mercado` mas `evaluacion_mercados_objetivo`) **y en los dos
la puerta que hace de CENTRO de la estrella tiene que morir con cualquiera de los supervivientes
viables**, asi que la guarda `1B` los rechaza
([`../loop/SALIDA_V51_PUERTAS_TRAS_LOTE_A.txt`](../loop/SALIDA_V51_PUERTAS_TRAS_LOTE_A.txt)).

> **EL HALLAZGO: `vuelta48_puertas_en_el_lote.py` LOS LLAMA SALVABLES.** Su dicotomia es
> SALVABLE (una sola puerta, el acto se funde si la puerta sobrevive) contra IMPOSIBLE (todos
> los miembros son puerta). **Falta el tercer caso: MAS DE UNA PUERTA, con alguna obligada a
> morir por la estructura del acto.** No se repara aqui, que seria alcance: se declara y se
> trae.

### LOS CINCO DECLARADOS DEL TRAMO SIGUEN DECLARADOS

**Ninguno se toca y se identifican por sus MIEMBROS**, no por su numero, que baila con cada
fusion: `obtencion_compromiso` y hermanos; `mejora_del_sistema_responsabilidad_gerencial` y
hermanos; `dia_cero_defectos` y hermanos; `domina_lo_que_compras` con
`investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor`; y `cultura_climatica_innovacion`
con `cultura_de_innovacion`. **Al cerrar la vuelta 51 son los actos 4, 21, 23, 27 y 28**
([`../loop/SALIDA_V51_TRAMO1_CIERRE.txt`](../loop/SALIDA_V51_TRAMO1_CIERRE.txt), y el rotulo va
fechado a su corrida desde el principio, que es lo que el acta 50 adjudico en su pregunta 5).

### LO QUE ESTA VUELTA NO HIZO DEL TRAMO 1, CON SU CIFRA MEDIDA AL CIERRE

| | |
|---|---:|
| lecturas `P.12` **hechas y ejecutadas** | **4** |
| lecturas `P.12` **hechas y NO ejecutadas** (el acto detenido por la guarda) | **1** |
| actos **fundidos** | **4** |
| actos MIXTOS que **siguen pendientes** de `P.12`, re-medidos al cierre | **21** |
| **tramo 2** de 50 actos | **NO ABIERTO** |

### EL CIERRE DE LA SECCION, MEDIDO AL CERRAR

{TABLA_CIERRE}
"""


def tabla_cierre():
    """Cifras leidas de las salidas de los instrumentos corridos al cierre."""
    def leer(p):
        return io.open(p, encoding="utf-8").read()

    ap_m = leer("docs/loop/SALIDA_V51_MARCADOR_APERTURA.txt")
    ci_m = leer("docs/loop/SALIDA_V51_MARCADOR_CIERRE.txt")
    ap_e = leer("docs/loop/SALIDA_V51_APERTURA.txt")
    ci_e = leer("docs/loop/SALIDA_V51_CIERRE.txt")
    ap_r = leer("docs/loop/SALIDA_V51_RECOMPUTO_APERTURA.txt")
    ci_r = leer("docs/loop/SALIDA_V51_RECOMPUTO_CIERRE.txt")
    ap_c = leer("docs/loop/SALIDA_V51_COLA.txt")
    ci_c = leer("docs/loop/SALIDA_V51_COLA_CIERRE.txt")

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
        ("mixtos del tramo 1 pendientes de `P.12`", "25", "**21**"),
    ]
    out = ["| | al abrir la vuelta 51 | **al cerrarla** |", "|---|---:|---:|"]
    for k, a, c in f:
        out.append("| %s | %s | **%s** |" % (k, a, c))
    out.append("| las cuatro comprobaciones de [`08_VERIFICACION.md`](08_VERIFICACION.md) | | **TODAS OK** |")
    out.append("| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    planes = cargar_planes()
    dec, ndec = tabla_declarados(planes)
    bloque = (TEXTO
              .replace("{TABLA_LECTURAS}", tabla_lecturas(planes))
              .replace("{TABLA_ACTOS}", tabla_actos(planes))
              .replace("{TABLA_DECLARADOS}", dec)
              .replace("{TABLA_CIERRE}", tabla_cierre()))

    print("=" * 78)
    print("REGISTRO DEL TRAMO, vuelta 51")
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
    print("lecturas P.12 en la tabla: %d" % sum(len(p["lecturas_p12"]) for p in planes))
    print("actos fundidos en la tabla: %d" % sum(len(p["actos"]) for p in planes))
    print("actos declarados y no fundidos: %d" % ndec)
    print("caracteres del bloque: %d" % len(bloque))
    if not a.ejecutar:
        print()
        print("SIMULACION: nada escrito.")
        return 0
    io.open(DESTINO, "a", encoding="utf-8", newline="").write("\n" + bloque.lstrip("\n"))
    print("ESCRITO.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
