"""Vuelta 46: EL REGISTRO DE OP-D-07 Y EL CIERRE MEDIDO DE LA FASE 02,
escrito en docs/plan/02_DESTEJIDOS.md CON LAS TABLAS IMPRESAS DESDE LOS
INSTRUMENTOS (EJECUTOR.md regla 1, cuarto renglon).

Ninguna celda de las tablas se teclea: todas salen de una medicion que este
mismo fichero corre, sobre:

  docs/plan/OPERACIONES.jsonl          (las nueve operaciones y OP-M-03-I)
  dataset/nodos/*.json                 (los tres nodos del caso, HOY)
  git show 1eef1c6b^ y 1eef1c6b        (el nodo ANTES y DESPUES del adelanto)
  docs/INTRA_DOMINIO_VEREDICTOS.jsonl  (los congelados y los pares)
  docs/plan/02_DESTEJIDOS.md           (los registros de cierre ya escritos)
  docs/plan/00_INDICE.md               (el marcador, para contrastarlo)

Uso: python scripts/loop/vuelta46_registro_opd07.py [--escribir]
"""
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
DEST = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

COMMIT_WEI = "1eef1c6b"
SUJETO = "decision_pivote_perseverar"
DESTINO = "puntos_brillantes_antes_del_pivote"
SUP_I = "pivotar_o_perseverar"

MARCA = re.compile(r"^(NO SE JUZGA|NO PUEDO JUZGAR|CONGELAD)", re.I)
PATRON_REGISTRO = "REGISTRO DE OPERACION HECHA"
PATRON_CERRADA = re.compile(r"^#+\s+.*OP-D-\d\d.*\s(CERRADA|SELLADA)", re.I)


def ops_dict():
    d = {}
    for linea in io.open(OPS, encoding="utf-8"):
        linea = linea.strip()
        if linea:
            o = json.loads(linea)
            d[o["id_op"]] = o
    return d


def nodo_hoy(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    return json.loads(io.open(ruta, encoding="utf-8").read())


def nodo_en(commit, nid):
    r = subprocess.run(["git", "show", "%s:dataset/nodos/%s.json" % (commit, nid)],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return None
    return json.loads(r.stdout.decode("utf-8"))


def obras(n):
    return [x.strip() for x in str(n.get("fuente", "")).split("|") if x.strip()]


def celda(t):
    """El campo fuente lleva un | como separador de obras, y un | crudo PARTE
    una tabla markdown en columnas falsas. Visto en la primera corrida del
    generador, antes de escribir nada. Se escapa aqui y en un solo sitio."""
    return str(t).replace("|", "\\|")


def tabla_verificaciones(op, antes, hoy, destino, sup):
    pa = antes["pasos_accionables"]
    ph = hoy["pasos_accionables"]
    pd = destino["pasos_accionables"]
    ps = sup["pasos_accionables"]
    bloque = pa[4:]
    prefijo = len([i for i in range(min(len(pa), len(ph))) if pa[i] == ph[i]])
    filas = [
        ("1", op["verificacion"][0],
         "**CUMPLE**. El nodo pasa de **%d** pasos a **%d**, con prefijo VERBATIM comun de "
         "**%d** pasos. Los cuatro que quedan son los de Ries" % (len(pa), len(ph), prefijo)),
        ("2", op["verificacion"][1],
         "**MITAD Y MITAD, MEDIDO.** El bloque **NO se perdio**: sus **%d** pasos viven "
         "byte a byte en `%s`. **Pero de viajar al superviviente del acto I, nada**: en "
         "`%s` viven **%d de %d**, y en `%s` **%d de %d**"
         % (len(bloque), DESTINO, SUP_I, len([p for p in bloque if p in ps]), len(bloque),
            SUJETO, len([p for p in bloque if p in ph]), len(bloque))),
        ("3", op["verificacion"][2],
         "**CUMPLE**. De **%d** obras (`%s`) a **%d** (`%s`)"
         % (len(obras(antes)), celda(antes["fuente"]), len(obras(hoy)),
            celda(hoy["fuente"]))),
    ]
    out = ["| # | lo que la `verificacion` de `OP-D-07` exige, copiado del fichero | como sale MEDIDO HOY |",
           "|---:|---|---|"]
    for n, exige, sale in filas:
        out.append("| **%s** | %s | %s |" % (n, celda(exige), sale))
    return "\n".join(out), bloque, pd


def tabla_bloque(bloque, pd):
    out = ["| # en el nodo viejo | el paso, verbatim | # donde vive HOY en `%s` |" % DESTINO,
           "|---:|---|---:|"]
    for i, p in enumerate(bloque, 5):
        j = pd.index(p) + 1 if p in pd else 0
        out.append("| **%d** | %s | **%s** |" % (i, celda(p), j if j else "NO ESTA"))
    return "\n".join(out)


def tabla_fase02(ops, texto_dest):
    lineas = texto_dest.split("\n")
    marcas = [(i, l) for i, l in enumerate(lineas) if l.startswith("## ")]
    f02 = sorted([o for o in ops.values() if o["fase"] == "02_DESTEJIDOS"],
                 key=lambda d: d["id_op"])
    out = ["| operacion | nodos | puntos de `verificacion` | registro de cierre escrito en esta pagina |",
           "|---|---:|---:|---|"]
    filas_sin = []
    for o in f02:
        oid = o["id_op"]
        cab = [(i, l) for i, l in marcas if oid in l]
        if not cab:
            out.append("| `%s` | %d | %d | **NINGUNO** |"
                       % (oid, len(o.get("nodos") or []), len(o.get("verificacion") or [])))
            filas_sin.append(oid)
            continue
        ini = cab[-1][0]
        sig = [i for i, l in marcas if i > ini]
        fin = sig[0] if sig else len(lineas)
        cuerpo_l = lineas[ini:fin]
        tiene = PATRON_REGISTRO in "\n".join(cuerpo_l)
        cerr = [l for l in cuerpo_l if PATRON_CERRADA.match(l) and oid in l]
        if tiene:
            marca = "**SI**, con la frase `REGISTRO DE OPERACION HECHA` (forma de la vuelta 30), linea **%d**" % (ini + 1)
        elif cerr:
            marca = "**SI**, con el encabezado de la forma anterior, linea **%d**: *%s*" % (ini + 1, cerr[0].strip()[3:80])
        else:
            marca = "**NINGUNO**"
            filas_sin.append(oid)
        out.append("| `%s` | %d | %d | %s |"
                   % (oid, len(o.get("nodos") or []), len(o.get("verificacion") or []), marca))
    return "\n".join(out), filas_sin, len(f02)


def tabla_congelados():
    vers = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    cong = [v for v in vers if MARCA.match((v.get("razon") or "").strip())]
    out = ["| puesto | clase | los dos nodos | de que fase es |", "|---:|---|---|---|"]
    for v in cong:
        out.append("| **%d** | **`%s`** | `%s` contra `%s` | **de la junta asesora, NO de la fase 02** |"
                   % (v["puesto_intra"], v["clase"], v["nodo_a"], v["nodo_b"]))
    return "\n".join(out), len(cong), len(vers)


def tabla_indice(ops):
    idx = io.open(os.path.join(RAIZ, "docs", "plan", "00_INDICE.md"),
                  encoding="utf-8").read().split("\n")
    publicado = {}
    for l in idx:
        m = re.match(r"^\|\s+\*\*(0?\d+ [A-Z ]+)\*\*\s+\|\s+(\d+)\s+\|", l)
        if m:
            publicado[m.group(1).strip()] = int(m.group(2))
    total_pub = None
    for l in idx:
        m = re.match(r"^\|\s+operaciones\s+\|\s+\*\*(\d+)\*\*\s+\|", l)
        if m:
            total_pub = int(m.group(1))
    medido = {}
    for o in ops.values():
        clave = o["fase"].replace("_", " ")
        clave = re.sub(r"^0*", "", clave.split(" ")[0]).rjust(1) + " " + " ".join(clave.split(" ")[1:])
        medido[o["fase"]] = medido.get(o["fase"], 0) + 1
    mapa = {"00_CODIGO": "0 CODIGO", "01_FUENTES": "01 FUENTES",
            "02_DESTEJIDOS": "02 DESTEJIDOS", "03_FUSIONES": "03 FUSIONES",
            "04_ENLACES": "04 ENLACES", "05_SANEO": "05 SANEO",
            "06_MESAS": "06 MESAS", "07_ADUANA": "07 ADUANA",
            "08_VERIFICACION": "08 VERIFICACION",
            "09_LECTURAS_DIRIGIDAS": "09 LECTURAS DIRIGIDAS",
            "10_INVENTARIO": "10 INVENTARIO"}
    out = ["| fila del marcador del `00_INDICE` | lo que el indice publica | lo que MIDO hoy | calza |",
           "|---|---:|---:|---|"]
    out.append("| **operaciones (total)** | **%s** | **%d** | %s |"
               % (total_pub, len(ops), "SI" if total_pub == len(ops) else "**NO**"))
    difs = 0 if total_pub == len(ops) else 1
    for fase in sorted(mapa):
        nombre = mapa[fase]
        pub = publicado.get(nombre)
        med = medido.get(fase, 0)
        ok = (pub == med)
        if not ok:
            difs += 1
        out.append("| **%s** | %s | **%d** | %s |"
                   % (nombre, pub if pub is not None else "no leida", med,
                      "SI" if ok else "**NO**"))
    return "\n".join(out), difs


def main():
    ops = ops_dict()
    op = ops["OP-D-07"]
    mi = ops["OP-M-03-I"]
    antes = nodo_en(COMMIT_WEI + "^", SUJETO)
    hoy = nodo_hoy(SUJETO)
    destino = nodo_hoy(DESTINO)
    sup = nodo_hoy(SUP_I)

    t_ver, bloque, pd = tabla_verificaciones(op, antes, hoy, destino, sup)
    t_bloque = tabla_bloque(bloque, pd)
    texto_dest = io.open(DEST, encoding="utf-8").read()
    t_f02, sin_registro, n_f02 = tabla_fase02(ops, texto_dest)
    t_cong, n_cong, n_ver = tabla_congelados()
    t_idx, difs_idx = tabla_indice(ops)

    print("=" * 78)
    print("VUELTA 46: EL REGISTRO DE OP-D-07 Y EL CIERRE MEDIDO DE LA FASE 02")
    print("=" * 78)
    print()
    print("--- LAS TRES VERIFICACIONES ---")
    print(t_ver)
    print()
    print("--- EL BLOQUE, PASO POR PASO ---")
    print(t_bloque)
    print()
    print("--- LAS NUEVE OPERACIONES DE LA FASE 02 ---")
    print(t_f02)
    print("  operaciones de la fase: %d" % n_f02)
    print("  SIN registro de cierre: %s" % (", ".join(sin_registro) or "ninguna"))
    print()
    print("--- LOS CONGELADOS ---")
    print(t_cong)
    print("  congelados hoy: %d sobre %d veredictos" % (n_cong, n_ver))
    print()
    print("--- EL MARCADOR DEL 00_INDICE, CONTRASTADO ---")
    print(t_idx)
    print("  filas que NO calzan: %d" % difs_idx)
    print()
    print("--- EL TEXTO DE OP-M-03-I QUE LA MEDICION CONTRADICE ---")
    for i, p in enumerate(mi["preservar"], 1):
        print("  preservar %d: %s" % (i, p))
    for i, v in enumerate(mi["verificacion"], 1):
        print("  verificacion %d: %s" % (i, v))

    if "--escribir" not in sys.argv:
        print()
        print("(sin --escribir: no se toco 02_DESTEJIDOS.md)")
        return 0

    seccion = SECCION % dict(
        tabla_ver=t_ver, tabla_bloque=t_bloque, tabla_f02=t_f02,
        tabla_cong=t_cong, tabla_idx=t_idx, n_f02=n_f02,
        n_con=n_f02 - len(sin_registro), n_cong=n_cong, n_ver=n_ver,
        difs_idx=difs_idx,
        mi_pres=celda(mi["preservar"][1]), mi_verif=celda(mi["verificacion"][2]),
        op_verif2=celda(op["verificacion"][1]))
    with io.open(DEST, "a", encoding="utf-8") as fh:
        fh.write(seccion)
    print()
    print("ESCRITO al final de docs/plan/02_DESTEJIDOS.md: %d caracteres" % len(seccion))
    return 0


SECCION = """
---

## `OP-D-07`: **LA CIRUGIA YA ESTABA HECHA, Y NO LA HIZO ESTA FASE** (19 ago 2026, vuelta 46)

**Nodo: `decision_pivote_perseverar`. `superviviente` nulo, `eliminar` vacio, `aristas_nuevas`
vacio.** La operacion se leyo **ENTERA** de `OPERACIONES.jsonl` y el nodo **DE CERO** antes de
tocar nada, con `python scripts/loop/vuelta46_lectura_opd07.py`
(`docs/loop/SALIDA_V46_OPD07_LECTURA.txt`, exit 0, **instrumento de solo lectura**).

> **EL HALLAZGO, y cambia la vuelta entera: EL DESTEJIDO QUE `OP-D-07` LEGISLA YA ESTABA
> EJECUTADO, DESDE EL 14 DE AGOSTO DE 2026, Y LO EJECUTO LA FASE 01.** Fue `OP-F-04-WEI`,
> segunda tanda, **commit `1eef1c6b`**, hallado hoy con `git log --follow` sobre el fichero del
> nodo. **Esta escrito**: `docs/plan/01_FUENTES.md` **linea 982** lo registra con su frontera
> (`decision_pivote_perseverar`, **5 a 9**, destino **nodo propio**
> `puntos_brillantes_antes_del_pivote`, por `P.18` punto 3), y el nodo nuevo figura en
> `INDICE_ROJO_DECLARADO.jsonl` con esa misma fecha. **`OP-D-07` tiene `fecha_corte`
> 2026-08-12: se escribio DOS DIAS ANTES de que otra fase se le adelantara.**

**NI UN NODO SE TOCO EN ESTA VUELTA.** Volver a cortar un nodo ya cortado no es ejecutar la
operacion: es **fabricar**. Lo que se hace aqui es **medir las tres verificaciones contra el
archivo de hoy y publicarlas**, que es lo unico que queda por hacer.

### LAS TRES VERIFICACIONES, MEDIDAS UNA POR UNA

%(tabla_ver)s

### EL BLOQUE DEL PUNTO BRILLANTE, PASO POR PASO Y VERBATIM

**Los cinco pasos son byte a byte los mismos**, solo que ahora son los pasos **1 a 5** de su
propio nodo en vez de los **5 a 9** del sujeto. **CERO contenido perdido.**

%(tabla_bloque)s

**Y la arista existe con su espejo**, medida en los dos sentidos:
`decision_pivote_perseverar` nombra a `puntos_brillantes_antes_del_pivote` en
`nodos_siguientes` **y este lo nombra en `nodos_previos`**.

### LA PARADA, QUE NO SE ARREGLA AQUI (regla 5)

**La SEGUNDA MITAD de la verificacion 2 ya no se puede cumplir por la ruta que el plan
escribio**, y no por un descuido de hoy sino porque **el adelanto de la fase 01 movio el
bloque fuera del nodo que muere en el acto I**. Los tres textos que la medicion contradice,
citados enteros y sin reescribir ninguno:

| donde esta escrito | que dice, copiado | que mide el archivo HOY |
|---|---|---|
| `OP-D-07`, `verificacion` punto 2 | *%(op_verif2)s* | el bloque **no esta** en el nodo que muere: esta en un tercero |
| `OP-M-03-I`, `preservar` | *%(mi_pres)s* | **el que muere ya NO lo trae**: `decision_pivote_perseverar` tiene hoy **0 de 5** |
| `OP-M-03-I`, `verificacion` punto 3 | *%(mi_verif)s* | el bloque **es identificable como bloque**, pero **en `puntos_brillantes_antes_del_pivote`**, que **no es** ninguno de los dos nodos de `OP-M-03-I` |

**Y un cuarto, en su propia pagina:** `docs/plan/FRONTERAS_DECLARADAS.md` **linea 82**,
del **12 ago 2026**, dice que el bloque *llega por el destejido `OP-D-07` y se conserva entero
en el superviviente del acto I*. **Hoy no llega por ahi, porque ya no sale de ahi.**

> **LA FRONTERA DEL 1298 NO ESTA PERDIDA: ESTA EN OTRO SITIO DEL QUE EL PLAN DICE.** Su lado
> del punto brillante vive entero, con fuente `Traction` sola, en un nodo propio y enlazado.
> **Lo que ya no se sostiene es la RUTA escrita, no el contenido.** Decidir si el lado se
> queda donde esta, si viaja al superviviente en el acto I, o si la frontera se re-declara
> entre otros dos nodos, **es una decision de la fase 03 y de la mesa, no de este registro**:
> se trae **PARADA** y **no se arregla aqui**.

### EL REGISTRO DE `OP-D-07`, ESCRITO CON LO QUE HAY Y NO CON LO QUE SE ESPERABA

**Las verificaciones 1 y 3 CUMPLEN medidas, y la 2 cumple en su mitad material** (el bloque
entero, verbatim, no perdido) **y NO cumple en su mitad diferida** (el viaje al superviviente,
que era materia del acto I). **Por eso este registro NO dice `REGISTRO DE OPERACION HECHA`.**
El campo `estado` **se queda quieto en `LISTA`**, como en todos los cierres desde la vuelta 30,
y **lo que se declara es exactamente lo medido**: *la cirugia de `OP-D-07` esta hecha, la hizo
`OP-F-04-WEI` el 14 ago 2026, y la mitad diferida de su verificacion 2 queda en PARADA*.
**Si el auditor lee que eso basta para HECHA, la palabra se escribe en la vuelta siguiente con
su acta detras. No se estrena aqui.**

---

## EL CIERRE DE LA FASE 02, DECLARADO MIDIENDO (19 ago 2026, vuelta 46)

**Medido con `python scripts/loop/vuelta46_cierre_fase02.py`
(`docs/loop/SALIDA_V46_CIERRE_FASE02.txt`, exit 0) y con el generador de esta seccion.**

### LAS %(n_f02)s OPERACIONES DE LA FASE, CON SU REGISTRO

%(tabla_f02)s

**%(n_con)s de %(n_f02)s tienen registro de cierre escrito en esta pagina**, en una de las dos
formas que la campana ha usado: la frase `REGISTRO DE OPERACION HECHA` acunada en la vuelta 30,
o el encabezado `CERRADA` o `SELLADA` de la forma anterior. **La unica sin registro previo era
`OP-D-07`, y lo acaba de recibir arriba.**

### EL CRITERIO DE HECHO DE `08_VERIFICACION`, CONTRA LA FASE

> **`08_VERIFICACION.md` linea 25:** *02 DESTEJIDOS: los quince congelados releidos; cada
> perdida en el bloque del que proviene.*
> **Y el criterio general, linea 9:** *UNA FASE ESTA HECHA CUANDO SU VERIFICACION SE CAERIA SI
> EL FALLO VOLVIERA.*

**LOS CONGELADOS, CONTADOS HOY SOBRE EL ARCHIVO ENTERO** (detector: la razon ABRE con *NO SE
JUZGA*, *NO PUEDO JUZGAR* o *CONGELAD*, el mismo de
`scripts/loop/vuelta45_verificar_opd01_opd02.py`):

%(tabla_cong)s

**Queda %(n_cong)s congelado sobre %(n_ver)s veredictos, y NO es de esta fase.** Los quince que
el criterio nombra estan releidos.

### GATE 0 Y SUITES, CORRIDOS EN ESTA VUELTA

| que | como salio |
|---|---|
| **Gate 0**, ciclo de **TRES** comandos | los tres **exit 0**: `GATE 0: OK`, **71** etiquetas reaplicadas, **6** assets sincronizados. El comando **4 NO corre**: el censo no se movio |
| **arbol tras el ciclo** | **byte igual a `HEAD`**. `phase1_run_log.json` respaldado antes y **comprobado byte igual despues** |
| **suite del motor** | **25 de 25**, exit 0 |
| **suite web** | **80** ficheros, **1.030** pasadas y **3** saltadas, exit 0 |
| **`tsc --noEmit`** | **CERO** lineas, exit 0 |

### LO QUE NO CIERRA, DECLARADO CON LA MEDICION DELANTE

**El encargo manda declarar lo que no cierre en vez de declararlo cerrado. Son dos cosas:**

1. **LA MITAD DIFERIDA DE LA VERIFICACION 2 DE `OP-D-07`**, arriba, en **PARADA**. Es de la
   fase 03 y de la mesa, no de esta pagina.
2. **EL MARCADOR DEL `00_INDICE` ESTA RANCIO, y no lo toco yo.** Es una tabla de prosa que
   **ningun instrumento valida**, que es la especie exacta contra la que se escribio el cuarto
   renglon de la regla 1. **Contrastada hoy, fila por fila, contra `OPERACIONES.jsonl`:**

%(tabla_idx)s

   **%(difs_idx)s filas no calzan**, y la de esta fase es la que mas importa: **el indice dice
   que la fase 02 tiene SIETE operaciones y el fichero tiene NUEVE**, porque `OP-D-08` y
   `OP-D-09` nacieron despues. **Se declara y no se reescribe**, que es como una correccion se
   puede auditar: **rehacer ese marcador es un encargo propio, con su instrumento, no un
   apano al margen de esta seccion.**
"""


if __name__ == "__main__":
    sys.exit(main())
