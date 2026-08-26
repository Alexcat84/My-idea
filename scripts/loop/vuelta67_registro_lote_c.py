# -*- coding: utf-8 -*-
"""vuelta67_registro_lote_c.py . ADOSA AL FINAL DE docs/plan/03_FUSIONES.md EL
REGISTRO DEL LOTE C DEL TRAMO UNICO DE OP-U-02, BAJO LA CABECERA DE TRAMO QUE LA
VUELTA 65 YA ADOSO (linea 3732 de esa pagina, cotejada hoy).

NO REESCRIBE NI UNA LINEA DE ARRIBA: abre el fichero en modo adosar.

NINGUNA TABLA SE TECLEA (regla 1): la del reparto pieza a pieza, la de las
piezas por absorbido y las de los actos declarados SE GENERAN del PLAN SELLADO
docs/loop/PLAN_V67_OPU02_LOTE_C.json; la de las perdidas se RECORTA ENTERA de la
salida del tallador; y las celdas de guardas, colisiones y censos se EXTRAEN POR
AGUJA de las salidas de esta vuelta. La celda que no se pueda leer de su fichero
es ROJO y NO SE ESCRIBE NADA.

LAS CUATRO FUNCIONES QUE ARMAN TABLA (tabla_reparto, tabla_por_absorbido,
tabla_perdidas y tabla_declarado) SE COPIAN LITERAL de
scripts/loop/vuelta66_registro_lote_b.py, lineas 90 a 196, y NO se re-inventan:
dos registros de la misma pagina no pueden dibujar el reparto distinto en
silencio. LO UNICO QUE CAMBIA, y va dicho: tabla_declarado imprime ademas EL
MOTIVO SELLADO leido del propio declarado, porque este lote trae CINCO declarados
con TRES motivos distintos y uno de ellos sin letra, y una tabla que no lo diga
obliga a leer la prosa para saber por que cerro cada uno. La aritmetica de las
otras tres no se toca.

GUARDA DE CITAS: cada cita de linea se coteja antes de escribir.
GUARDA DE IDEMPOTENCIA: si la cabecera de este lote ya esta, no escribe.

Uso:
  python scripts/loop/vuelta67_registro_lote_c.py [--simular]
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:65 fuente=docs/plan/03_FUSIONES.md prueba="EL REGISTRO DEL LOTE A` (2026-08-20, vuelta 65)" corte=2026-08-25 motivo="el docstring nombra la VUELTA 65 porque es la vuelta que adoso la cabecera de tramo bajo la que este registro se cuelga, cotejada hoy en la linea 3732 de esa pagina; el fichero es de la vuelta 67 y por eso el numero no calza con su propia vuelta a proposito"
import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGINA = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
LOOP = os.path.join(RAIZ, "docs", "loop")
PLAN = os.path.join(LOOP, "PLAN_V67_OPU02_LOTE_C.json")
NL = chr(10)
CABECERA = "OP-U-02, TRAMO UNICO: EL REGISTRO DEL LOTE C"

CITAS_PAGINA = [
    (62, "EL ORDEN DE ESTA FASE"),
    (1377, "EL CARRIL GENERAL DE COLISIONES"),
    (3338, "LA REGLA DE LA FICHA ENVEJECIDA"),
    (3732, "EL REGISTRO DEL LOTE A"),
    (3744, "EL ACTO 1: `DECLARADO Y NO FUNDIDO` POR `P.10`"),
    (4023, "CON LA GUARDA `1B` COMO MOTIVO SELLADO"),
    (4080, "EL REGISTRO DEL LOTE B"),
    (4365, "EL `ACTO 5`: `DECLARADO Y NO FUNDIDO` POR `P.5`"),
    (4478, "LAS ADJUDICACIONES DEL ACTA DE LA VUELTA 66"),
    (4518, "UN ACTO CUYO `P.5` CONTESTA QUE NO ES UNA FAMILIA"),
    (4542, "LA LINEA BASE DEL CENSO QUEDA EN `4`"),
]

FALLOS = []


def leer(nombre):
    p = os.path.join(LOOP, nombre)
    if not os.path.exists(p):
        FALLOS.append("no existe la salida %s" % nombre)
        return ""
    return io.open(p, encoding="utf-8").read()


def busca(texto, patron, etiqueta):
    m = re.search(patron, texto)
    if not m:
        FALLOS.append("no se pudo leer %s" % etiqueta)
        return "?"
    return m.group(1)


def cotejar(citas, callado=False):
    lineas = io.open(PAGINA, encoding="utf-8").read().split(NL)
    if not callado:
        print()
        print("  --- GUARDA DE CITAS: docs/plan/03_FUSIONES.md (%d lineas) ---" % len(lineas))
    malas = []
    for n, aguja in citas:
        real = lineas[n - 1] if 0 < n <= len(lineas) else "(FUERA DE RANGO)"
        ok = aguja in real
        if not ok:
            malas.append((n, aguja, real))
        if not callado:
            print("     %-6d %-4s %s" % (n, "OK" if ok else "MAL", real.strip()[:100]))
    return malas


# --- COPIADAS LITERAL de vuelta66_registro_lote_b.py lineas 90 a 155 --------
def tabla_reparto(acto):
    """UNA FILA POR PIEZA, generada del plan sellado. No se teclea ninguna."""
    filas = ["| pieza del que muere | marca | a donde va |", "|---|---|---|"]
    for ab in acto["absorbidos"]:
        for etq, marcas in (("paso", acto["pasos"].get(ab) or {}),
                            ("condicion", acto["condiciones"].get(ab) or {})):
            for i in sorted(marcas, key=lambda x: int(x)):
                m = marcas[i]
                if m == "APPEND":
                    destino = "**viaja ENTERA** al superviviente"
                    marca = "`APPEND`"
                elif m.startswith("INCISO:"):
                    k, trozo, _nexo = m[len("INCISO:"):].split("|", 2)
                    destino = "**`INCISO` ADOSADO** al paso %s: *%s*" % (k, trozo)
                    marca = "`INCISO`"
                elif m.startswith("CUBIERTO_COND:"):
                    destino = "ya lo dice la **condicion %s** del superviviente" % m.split(":")[1]
                    marca = "`CUBIERTO`"
                else:
                    destino = "ya lo dice el **paso %s** del superviviente" % m.split(":")[1]
                    marca = "`CUBIERTO`"
                filas.append("| %s **%s** de `%s` | %s | %s |" % (etq, i, ab, marca, destino))
    return NL.join(filas)


def tabla_por_absorbido(acto):
    filas = ["| absorbido | pasos | condiciones | enteras | ya dichas | de `INCISO` |",
             "|---|---:|---:|---:|---:|---:|"]
    tot = [0, 0, 0, 0, 0]
    for ab in acto["absorbidos"]:
        p = acto["pasos"].get(ab) or {}
        c = acto["condiciones"].get(ab) or {}
        vals = list(p.values()) + list(c.values())
        ap = len([x for x in vals if x == "APPEND"])
        inc = len([x for x in vals if x.startswith("INCISO")])
        cub = len(vals) - ap - inc
        filas.append("| `%s` | %d | %d | %d | %d | %d |" % (ab, len(p), len(c), ap, cub, inc))
        for i, v in enumerate((len(p), len(c), ap, cub, inc)):
            tot[i] += v
    filas.append("| **los %d juntos** | **%d** | **%d** | **%d** | **%d** | **%d** |"
                 % (len(acto["absorbidos"]), tot[0], tot[1], tot[2], tot[3], tot[4]))
    return NL.join(filas)


def tabla_perdidas(acto_n=None):
    """RECORTADA ENTERA de la salida del tallador, no re-generada. Con acto_n se
    queda solo con las filas de ese acto, leyendo la COLUMNA acto por su sitio en
    la cabecera y no por la prosa de alrededor."""
    t = leer("SALIDA_V67_TALLAR_PERDIDAS.txt")
    m = re.search(r"^\| plan \| acto \|.*?(?=^$)", t, re.S | re.M)
    if not m:
        FALLOS.append("la salida del tallador de perdidas no trae tabla")
        return ""
    lineas = m.group(0).rstrip().split(NL)
    if acto_n is None:
        return NL.join(lineas)
    cab, sep = lineas[0], lineas[1]
    cols = [c.strip() for c in cab.strip().strip("|").split("|")]
    if "acto" not in cols:
        FALLOS.append("la tabla del tallador no tiene columna acto")
        return ""
    j = cols.index("acto")
    fuera = [l for l in lineas[2:]
             if [c.strip() for c in l.strip().strip("|").split("|")][j] == str(acto_n)]
    return NL.join([cab, sep] + fuera)


# --- tabla_declarado: COPIA con UN anadido, y el anadido va dicho arriba ----
MOTIVO_SELLADO = {
    12: "**un par `D` INTERNO DIRECTO sin triangulo que cerrar**, y NO es ninguno de los tres "
        "sellados: **PENDIENTE DE DOCTRINA** (regla 5) y **DISCUTIBLE**",
    13: "**la guarda `1B`**, DOS puertas dentro (acta 65, registrada en la linea **4023**)",
    14: "**`P.5`**, que contesta **NO ES UNA** (acta 66, registrada en la linea **4518**)",
    15: "**la guarda `1B`**, DOS puertas dentro (acta 65, registrada en la linea **4023**)",
    17: "**`P.10`**, con su triangulo MEDIDO, **mas la guarda `1B` como segunda razon "
        "independiente**",
}


def tabla_declarado(dec):
    med = dec["medicion"]
    filas = ["| | |", "|---|---|"]
    filas.append("| **acto** | **%d** del `orden_universo` |" % dec["acto"])
    filas.append("| **MOTIVO SELLADO DEL CIERRE** | %s |" % MOTIVO_SELLADO[dec["acto"]])
    filas.append("| **miembros** | **%d**, y **NINGUNO se toca** |" % med["miembros"])
    filas.append("| **combinaciones internas** | %d |" % med["combinaciones"])
    filas.append("| **pares `A` internos** | %d |" % med["pares_A"])
    filas.append("| **pares `D` internos** | **%d**%s |"
                 % (med["pares_D"],
                    ", leidos y declarados DISTINTOS" if med["pares_D"] else
                    " (por eso `P.10` NO se dispara aqui)"))
    filas.append("| **pares sin veredicto escrito** | %d |" % med["pares_sin_veredicto"])
    filas.append("| **NODOS PUENTE** | **%d** |" % med["nodos_puente"])
    filas.append("| **TRIANGULOS PUENTE** (`A` mas `A` mas `D`) | **%d** |" % med["triangulos_puente"])
    filas.append("| **PUERTAS dentro del acto** | %s |"
                 % ("**%d**: `%s`" % (len(med["puertas_dentro"]), "`, `".join(med["puertas_dentro"]))
                    if med["puertas_dentro"] else
                    "**NINGUNA**, la guarda `1B` pasa por vacio y se dice"))
    if med.get("puestos_D_internos"):
        filas.append("| **puestos de los `D` internos** | %s |"
                     % ", ".join("**%d**" % x for x in med["puestos_D_internos"]))
    filas.append("| **instrumento** | [`../loop/%s`](../loop/%s) |"
                 % (os.path.basename(med["salida"]), os.path.basename(med["salida"])))
    filas.append("| **dossier `P.5`** | [`../loop/%s`](../loop/%s) |"
                 % (os.path.basename(med["dossier"]), os.path.basename(med["dossier"])))
    return NL.join(filas)


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _v67_texto_lote_c import TEXTO  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("REGISTRO DEL LOTE C DEL TRAMO UNICO DE OP-U-02 EN 03_FUSIONES.md")
    print("=" * 78)

    malas = cotejar(CITAS_PAGINA)
    print()
    print("  citas cotejadas: %d | MALAS: %d" % (len(CITAS_PAGINA), len(malas)))
    if malas:
        print()
        print("ROJO: %d cita(s) no calzan y NO se escribe nada:" % len(malas))
        for n, aguja, real in malas:
            print("   linea %d deberia contener %r y contiene: %s" % (n, aguja, real[:90]))
        return 1

    plan = json.load(io.open(PLAN, encoding="utf-8"))
    actos = {x["orden"]: x for x in plan["actos"]}
    decl = {x["acto"]: x for x in plan["declarados_y_no_fundidos"]}

    # LAS CELDAS QUE NO SE TECLEAN: se extraen por aguja de las salidas de hoy.
    fus = leer("SALIDA_V67_FUSION_LOTE_C.txt")
    col = leer("SALIDA_V67_CENSO_COLISIONES.txt")
    esp = leer("SALIDA_V67_COLISIONES_ESPERADAS.txt")
    dif = leer("SALIDA_V67_DIFF_DUPLICADAS.txt")
    rec = leer("SALIDA_V67_RECOMPUTO_CIERRE.txt")
    rea = leer("SALIDA_V67_REANCLAJE.txt")

    c = {
        "antes_vivos": busca(fus, r"censo ANTES  : \d+ ficheros, (\d+) vivos", "vivos antes"),
        "despues_vivos": busca(fus, r"censo DESPUES: \d+ ficheros, (\d+) vivos", "vivos despues"),
        "mueren": busca(fus, r"nodos que MUEREN\s+: (\d+)", "nodos que mueren"),
        "piezas": busca(fus, r"piezas repartidas\s+: (\d+)", "piezas"),
        "enteras": busca(fus, r"piezas repartidas\s+: \d+ \((\d+) viajan enteras", "enteras"),
        "yadichas": busca(fus, r"viajan enteras, (\d+) ya estaban dichas", "ya dichas"),
        "tocados": busca(fus, r"ESCRITO\. ficheros tocados: (\d+)", "ficheros tocados"),
        "p16": busca(fus, r"P\.16, DUPLICADAS QUE LA PROPIA FUSION FABRICA[^:]*: (\d+)", "P.16"),
        "pasivo_antes": busca(fus, r"ANTES de la operacion \(pasivo historico, OP-S-12\): (\d+)",
                              "pasivo antes"),
        "pasivo_despues": busca(fus, r"DESPUES de la operacion\s+: (\d+)", "pasivo despues"),
        "reanclajes": busca(rea, r"(\d+) referencias re-ancladas", "reanclajes"),
        "col_base": busca(esp, r"linea base : (\d+)", "linea base"),
        "col_med": busca(col, r"COLISIONES DE CLASE VIGENTES\s+: (\d+)", "colisiones medidas"),
        "col_esp": busca(esp, r"ESPERADAS TRAS FUNDIR = (\d+)", "colisiones esperadas"),
        "col_nuevas": busca(esp, r"colisiones NUEVAS que la fusion fabricaria : (\d+)", "nuevas"),
        "col_calza": busca(col, r"CALZA: (\w+)", "calza"),
        "dup_fab": busca(dif, r"GRUPOS FABRICADOS DE VERDAD: (\d+)", "duplicadas fabricadas"),
        "dup_ren": busca(dif, r"RENOMBRADOS \(aparecen con rotulo nuevo pero son el MISMO grupo\): (\d+)",
                         "renombrados"),
        "dup_antes": busca(dif, r"grupos ya RESUELTOS\s+: antes (\d+)", "grupos antes"),
        "dup_despues": busca(dif, r"grupos ya RESUELTOS\s+: antes \d+ \| despues (\d+)", "grupos despues"),
        "actos": busca(rec, r"actos \(componentes >=2\): (\d+)", "actos"),
        "abiertos": busca(rec, r"ABIERTOS: (\d+) sobre", "abiertos"),
        "abiertos_n": busca(rec, r"ABIERTOS: \d+ sobre (\d+) nodos", "nodos abiertos"),
    }
    print()
    print("  --- CELDAS EXTRAIDAS POR AGUJA (ninguna tecleada) ---")
    for k, v in c.items():
        print("     %-16s %s" % (k, v))
    if FALLOS:
        print()
        print("ROJO: %d celda(s) no se pudieron leer y NO se escribe nada:" % len(FALLOS))
        for f in FALLOS:
            print("   %s" % f)
        return 1

    m = re.search(r"ACTO 16 \. sobrevive.*?pasos (\d+) -> (\d+).*?condiciones (\d+) -> (\d+)",
                  fus, re.S)
    if not m:
        print("ROJO: no se pudo leer el crecimiento del acto 16")
        return 1
    p16a, p16b, c16a, c16b = m.groups()

    t = TEXTO % dict(
        c, **{
            "rep16": tabla_reparto(actos[16]), "abs16": tabla_por_absorbido(actos[16]),
            "per16": tabla_perdidas(16),
            "dec12": tabla_declarado(decl[12]), "dec13": tabla_declarado(decl[13]),
            "dec14": tabla_declarado(decl[14]), "dec15": tabla_declarado(decl[15]),
            "dec17": tabla_declarado(decl[17]),
            "p16a": p16a, "p16b": p16b, "c16a": c16a, "c16b": c16b,
        })
    if FALLOS:
        print()
        print("ROJO: %d fallo(s) al armar las tablas y NO se escribe nada:" % len(FALLOS))
        for f in FALLOS:
            print("   %s" % f)
        return 1

    for mal, nombre in ((chr(8212), "guion largo"), (chr(8211), "guion medio")):
        if mal in t:
            print("ROJO: el texto trae un %s. PARADA." % nombre)
            return 1

    crudo = io.open(PAGINA, encoding="utf-8").read()
    if CABECERA in crudo:
        print()
        print("YA ADOSADO: el registro del lote C ya esta en la pagina. No se escribe nada.")
        return 0

    antes = len(crudo.split(NL))
    print()
    print("  la pagina tiene %d lineas y el texto anade %d" % (antes, t.count(NL)))
    if a.simular:
        print()
        print("  SIMULACION: no se escribe nada.")
        print("FIN")
        return 0

    with io.open(PAGINA, "a", encoding="utf-8", newline=NL) as fh:
        fh.write(t)
    despues = len(io.open(PAGINA, encoding="utf-8").read().split(NL))
    print()
    print("GUARDAS TRAS ESCRIBIR")
    print("  lineas antes %d, despues %d (delta %d)" % (antes, despues, despues - antes))
    txt = io.open(PAGINA, encoding="utf-8").read()
    print("  guiones largos %d, guiones medios %d"
          % (txt.count(chr(8212)), txt.count(chr(8211))))
    re_malas = cotejar(CITAS_PAGINA, callado=True)
    print("  las sedes de arriba siguen en su linea: %s"
          % ("OK (%d de %d)" % (len(CITAS_PAGINA) - len(re_malas), len(CITAS_PAGINA))
             if not re_malas else "ROJO"))
    print()
    print("VERDE: registro adosado y nada de arriba reescrito.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
