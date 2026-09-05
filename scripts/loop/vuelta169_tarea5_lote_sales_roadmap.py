# -*- coding: utf-8 -*-
r"""vuelta169_tarea5_lote_sales_roadmap.py . EL LOTE DE SALES ROADMAP, Y LO QUE
LA MEDICION ENCONTRO DEBAJO (TAREA 5 de la vuelta 169, adjudicacion 6.7).

LO QUE EL ENCARGO SUPONE Y LO QUE LA MEDICION DICE, Y NO SE RESUELVE COPIANDO.
El encargo manda leer *"cinco pares"* del lote de sales roadmap con estas
palabras: *"YO NO LOS LEI Y NO LES PUSE CLASE"*, y la ficha de `OP-L-02` lo
sostiene, porque su nota dice todavia *"NO se leyeron los 5 de sales roadmap"*.
**MEDIDO HOY: LOS CINCO ESTAN LEIDOS DESDE EL 14 ago 2026**, como `LD-66` a
`LD-70`, y viven en `docs/plan/LD_SALES_ROADMAP.md`. Es la misma especie que la
parada de la vuelta 167 sobre `OP-C-01` (*"no se puede ejecutar porque esta
ejecutada"*) y que la `6.6` del acta 168 sobre las dos `OP-M-02`: **CUMPLIDO POR
CONSUNCION.**

CUATRO SEDES INDEPENDIENTES LO DICEN, Y LAS CUATRO SE LEEN AQUI EN VEZ DE
CITARSE DE MEMORIA:
  1. `docs/plan/LD_SALES_ROADMAP.md`, las cinco cabeceras `LD-66` a `LD-70`.
  2. `docs/plan/LECTURAS_DIRIGIDAS.md`, su tabla del universo, donde el `5`
     pendiente esta TACHADO y puesto a `0`.
  3. `docs/plan/INVENTARIO.jsonl`, la entrada `acto`
     `customer_validation_sales_roadmap`, cuya cobertura dice `15 de 15` citando
     `LD-66 a LD-70` por el carril del 9.10.
  4. `docs/plan/INVENTARIO.jsonl`, la entrada `racimo` `el sales roadmap`, lo
     mismo.

Y LA QUINTA, QUE ES LA QUE NO ES UNA CITA: **LA RELECTURA A CIEGAS.** El ejecutor
de esta vuelta clasifico los cinco pares por su cuenta, con la vara del banco
`9.6.1` y sus precisiones `9.6.2` y `9.6.3` mas `P.11`, LEIDAS EN SU FUENTE, y
con los diez veredictos de cola delante, **ANTES de abrir `LD_SALES_ROADMAP.md`**.
Las cinco clases estan escritas abajo en `CIEGA_DEL_EJECUTOR` y este instrumento
las cotea contra las cinco del archivo.

NO HAY CASO ROJO AUTOMATICO PARA LA CIEGA, Y SE DECLARA EN VEZ DE FABRICARSE UNO
(`EJECUTOR.md` 1, "EL CASO ROJO SE PRUEBA POR MUTACION"): `CIEGA_DEL_EJECUTOR` es
una TABLA A MANO, escrita por el que lee, y no hay nada que mutar en ella que
pruebe nada. Lo que SI se puede tumbar, y se tumba, es la LECTURA del archivo:
si `LD_SALES_ROADMAP.md` cambiara sus clases, el cotejo caeria. Fabricar un
assert que se aprobara solo seria la caida 2 de la vuelta 89.

USO:
  python scripts/loop/vuelta169_tarea5_lote_sales_roadmap.py
  python scripts/loop/vuelta169_tarea5_lote_sales_roadmap.py --aplicar
"""
import collections
import io
import itertools
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
LD_SALES = os.path.join(PLAN, "LD_SALES_ROADMAP.md")
LECTURAS = os.path.join(PLAN, "LECTURAS_DIRIGIDAS.md")
INVENTARIO = os.path.join(PLAN, "INVENTARIO.jsonl")
OPERACIONES = os.path.join(PLAN, "OPERACIONES.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
MJS = os.path.join(RAIZ, "scripts", "vuelta16_generar_actos.mjs")
FICHA = "OP-L-02"

# LA CIEGA DEL EJECUTOR DE LA VUELTA 169. Escrita ANTES de abrir
# docs/plan/LD_SALES_ROADMAP.md, con la vara del banco 9.6.1 y sus precisiones
# 9.6.2 (la vara tiene direccion) y 9.6.3 (el tamano del solape no decide), mas
# P.11 (una advertencia es linea, no procedimiento), LEIDAS EN SU FUENTE y no de
# memoria, y con los DIEZ veredictos de cola de esta nomina delante.
# LOS DOS QUE NO RESOLVIERON LIMPIO VAN MARCADOS: son los pares 3 y 4, y el
# motivo de cada uno esta escrito. Se marcan ANTES de saber si se acierta.
CIEGA_DEL_EJECUTOR = {
    ("customer_validation_sales_roadmap", "estrategia_de_ventas"): (
        "D", False,
        "La ECONOMIA de la venta contra el MAPA de acceso, y es el mismo par que "
        "el puesto 872 ya resolvio con el otro nodo de mapa. Fuera del solape hay "
        "PROCEDIMIENTO a los dos lados: presupuesto, conteo de llamadas y prueba "
        "con ordenes reales a un lado; nivel de entrada, orden de contacto y guion "
        "al otro. Por 9.6.3, procedimiento en los dos lados es SANO."),
    ("customer_validation_sales_roadmap", "sales_roadmap"): (
        "D", False,
        "Misma especie que el 872 y el 1023. Lo compartido es quien decide, UNA "
        "linea. Fuera del solape: la economia de la validacion a un lado, el orden "
        "de contacto y el mensaje por rol al otro. Procedimiento en los dos lados."),
    ("estrategia_de_ventas", "hoja_de_ruta_de_ventas"): (
        "A", True,
        "DISCUTIBLE. Los dos son madres del mismo mapa de acceso y comparten dos de "
        "sus pasos. Lo que queda fuera del solape son LINEAS en los dos lados: nivel "
        "de entrada, guion y saboteadores a un lado (y una advertencia es LINEA por "
        "P.11); mapas actualizados, mapa de acceso y plan de implementacion al otro, "
        "y los dos ultimos son procedimientos NOMBRADOS en una linea que tienen nodo "
        "propio. Nada de eso es procedimiento del nodo. REPITE. Se marca porque "
        "dude: leido al reves parecia que hoja_de_ruta traia procedimiento, y solo "
        "P.11 lo resuelve."),
    ("estrategia_de_ventas", "refinar_sales_roadmap"): (
        "D", True,
        "DISCUTIBLE, y es el que mas me costo. Fuera del solape hay procedimiento a "
        "los dos lados: el diagrama de flujo, la validacion repetida en varias "
        "cuentas y el uso como prueba al contratar a un lado; el conteo de firmantes "
        "y el orden de contacto con guion por persona al otro. Por 9.6.3, SANO. "
        "Ademas los dos tienen ARISTA entre si (refinar es previo de estrategia), o "
        "sea que el grafo ya los trata como secuencia y no como duplicado. Se marca "
        "porque si sale D crea un triangulo A mas A mas D con los puestos 192 y 966 "
        "y convierte a sales_roadmap en NODO PUENTE por P.10."),
    ("estrategia_de_ventas", "sales_roadmap_vs_sales_force"): (
        "D", False,
        "El contenido del mapa contra la condicion de contratacion, que es EXACTAMENTE "
        "la relacion que los puestos 1306 y 1330 ya resolvieron con los otros dos "
        "nodos de contenido. Misma vara, mismo resultado."),
}

PAT_LD = re.compile(
    r"^#{1,4}\s+`(LD-\d+)`\s*\.\s*`([a-z0-9_]+)`\s+contra\s+`([a-z0-9_]+)`\s*\.\s*\*\*([A-Z ]+)\*\*",
    re.M)


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    aplicar = "--aplicar" in sys.argv
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 169, TAREA 5: EL LOTE DE SALES ROADMAP, Y LO QUE HAY DEBAJO")
    print("=" * 78)
    print("")

    print("A) LA NOMINA SE PARSEA DE SU FICHERO, NO SE TECLEA")
    texto = io.open(MJS, encoding="utf-8").read()
    m = re.search(r"const NOMINAS_OP_L_02 = \[(.*?)\n\];", texto, re.S)
    if not m:
        print("   ROJO: no se encuentra NOMINAS_OP_L_02.")
        return 1
    filas = re.findall(r"\[([^\]]*)\]", m.group(1))
    nominas = [re.findall(r'"([a-z0-9_]+)"', f) for f in filas]
    mem = nominas[0]
    print("   scripts/vuelta16_generar_actos.mjs, NOMINAS_OP_L_02: %d nominas" % len(nominas))
    print("   la PRIMERA, que es el lote del encargo: %d miembros" % len(mem))
    for x in mem:
        print("      %s" % x)
    print("")

    print("B) LOS PARES, CON EL RESOLUTOR DELANTE (P.1), Y LA COLA CONTADA")
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x, visto=None):
        visto = visto or set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    vivos = sorted({res(x) for x in mem})
    pares = [tuple(sorted(p)) for p in itertools.combinations(vivos, 2)]
    V = cargar(VEREDICTOS)
    cola = {}
    for r in V:
        cola[tuple(sorted((res(r["nodo_a"]), res(r["nodo_b"])))) ] = (r["clase"], r["puesto_intra"])
    en_cola = [p for p in pares if p in cola]
    sin_cola = [p for p in pares if p not in cola]
    print("   miembros escritos %d, vivos tras resolver %d, colapsados por alias %d"
          % (len(mem), len(vivos), len(mem) - len(vivos)))
    print("   CIFRA pares posibles: %d" % len(pares))
    print("   CIFRA con veredicto DE COLA: %d" % len(en_cola))
    print("   CIFRA SIN veredicto de cola: %d" % len(sin_cola))
    for p in sorted(en_cola, key=lambda q: cola[q][1]):
        print("      puesto %-5s %s  %s contra %s" % (cola[p][1], cola[p][0], p[0], p[1]))
    for p in sin_cola:
        print("      SIN COLA: %s contra %s" % p)
    print("")

    print("C) LAS CINCO SEDES QUE DICEN QUE EL LOTE YA ESTA LEIDO, LEIDAS HOY")
    t_ld = io.open(LD_SALES, encoding="utf-8").read()
    hallados = PAT_LD.findall(t_ld)
    print("   1. docs/plan/LD_SALES_ROADMAP.md: %d cabeceras LD" % len(hallados))
    for ld, a, b, clase in hallados:
        print("      %s  %-2s  %s contra %s" % (ld, clase.strip(), a, b))
    t_lec = io.open(LECTURAS, encoding="utf-8").read()
    fila = [l for l in t_lec.split("\n") if l.startswith("| sales roadmap |")]
    print("   2. docs/plan/LECTURAS_DIRIGIDAS.md, su fila del universo:")
    for l in fila:
        print("      %s" % l.strip())
    inv = cargar(INVENTARIO)
    for tipo, nombre in (("acto", "customer_validation_sales_roadmap"),
                         ("racimo", "el sales roadmap")):
        e = [x for x in inv if x["tipo"] == tipo and x["nombre"] == nombre]
        n = 3 if tipo == "acto" else 4
        print("   %d. docs/plan/INVENTARIO.jsonl, %s `%s`:" % (n, tipo, nombre))
        if not e:
            print("      NO EXISTE")
            continue
        print("      cobertura: %s" % e[0].get("cobertura"))
    print("")

    print("D) LA CIEGA DEL EJECUTOR CONTRA EL ARCHIVO, COTEJADA PAR A PAR")
    print("   (las cinco clases de la ciega se escribieron ANTES de abrir")
    print("    docs/plan/LD_SALES_ROADMAP.md; los discutibles van marcados)")
    print("")
    del_archivo = {}
    for ld, a, b, clase in hallados:
        del_archivo[tuple(sorted((a, b)))] = (clase.strip(), ld)
    print("   | par | ciega del ejecutor | el archivo | coincide | marcado DISCUTIBLE |")
    print("   |---|:-:|:-:|:-:|:-:|")
    coinciden = 0
    faltan = []
    for par, (clase_mia, discutible, _razon) in sorted(CIEGA_DEL_EJECUTOR.items()):
        clave = tuple(sorted(par))
        arch = del_archivo.get(clave)
        if arch is None:
            faltan.append(clave)
            print("   | `%s` contra `%s` | %s | NO ESTA | NO | %s |"
                  % (par[0], par[1], clase_mia, "SI" if discutible else "no"))
            continue
        ok = (arch[0] == clase_mia)
        coinciden += 1 if ok else 0
        print("   | `%s` contra `%s` | %s | %s (%s) | %s | %s |"
              % (par[0], par[1], clase_mia, arch[0], arch[1],
                 "SI" if ok else "NO", "SI" if discutible else "no"))
    print("")
    print("   CIFRA pares de la ciega: %d" % len(CIEGA_DEL_EJECUTOR))
    print("   CIFRA que el archivo trae: %d" % len(del_archivo))
    print("   CIFRA que COINCIDEN: %d de %d" % (coinciden, len(CIEGA_DEL_EJECUTOR)))
    print("   CIFRA marcados DISCUTIBLE por el ejecutor: %d"
          % sum(1 for _c, d, _r in CIEGA_DEL_EJECUTOR.values() if d))
    if faltan:
        print("   CIFRA de la ciega que el archivo NO trae: %d %s" % (len(faltan), faltan))
    saldo_mio = collections.Counter(c for c, _d, _r in CIEGA_DEL_EJECUTOR.values())
    saldo_arch = collections.Counter(c for c, _ld in del_archivo.values())
    print("   saldo de la ciega:   %s" % dict(sorted(saldo_mio.items())))
    print("   saldo del archivo:   %s" % dict(sorted(saldo_arch.items())))
    print("")
    print("   NO HAY CASO ROJO AUTOMATICO PARA LA CIEGA, Y SE DECLARA: la tabla")
    print("   CIEGA_DEL_EJECUTOR es a mano y no hay nada que mutar en ella. Lo que si")
    print("   cae es este cotejo, si el archivo cambiara sus clases.")
    print("")

    print("E) LAS RAZONES DE LA CIEGA, UNA POR UNA")
    for par, (clase, discutible, razon) in sorted(CIEGA_DEL_EJECUTOR.items()):
        print("   %s contra %s -> %s%s"
              % (par[0], par[1], clase, "  [DISCUTIBLE]" if discutible else ""))
        print("      %s" % razon)
    print("")

    print("F) LOS PUENTES DE P.10 QUE LA COBERTURA COMPLETA DEJA VER")
    clase_de = {}
    for p in en_cola:
        clase_de[p] = cola[p][0]
    for (a, b), (clase, _ld) in del_archivo.items():
        clase_de[tuple(sorted((res(a), res(b))))] = clase
    puentes = []
    for nodo in vivos:
        aes = [o for o in vivos if o != nodo
               and clase_de.get(tuple(sorted((nodo, o))), "").startswith("A")]
        for x, y in itertools.combinations(sorted(aes), 2):
            if clase_de.get(tuple(sorted((x, y)))) == "D":
                puentes.append((nodo, x, y))
    print("   P.10: un nodo con A hacia dos nodos que entre si dan D.")
    print("   CIFRA puentes en esta nomina: %d" % len(puentes))
    for n, x, y in puentes:
        print("      puente `%s` sobre (`%s` , `%s`)" % (n, x, y))
    print("   LO QUE ESTO SIGNIFICA, con la letra de P.10 delante: la componente NO")
    print("   se funde hasta que ese triangulo se cierre, y P.10 dice que un puente")
    print("   SOLO SE VE MIRANDO LA COMPONENTE ENTERA. Cerrar la cobertura es")
    print("   exactamente lo que permite verlos.")
    print("")

    if not aplicar:
        print("MODO MEDICION: la ficha NO se toca. Corre con --aplicar para escribir.")
        print("FIN")
        return 0

    fichas = cargar(OPERACIONES)
    idx = [i for i, f in enumerate(fichas) if f.get("id_op") == FICHA]
    if len(idx) != 1:
        print("ROJO: %s aparece %d veces." % (FICHA, len(idx)))
        return 1
    ficha = fichas[idx[0]]
    nota = ficha.get("nota") or ""
    VIEJA = "NO se leyeron los 5 de sales roadmap, y el motivo se escribe"
    print("G) LA FRASE QUE HAY QUE CORREGIR, BUSCADA EN LA FICHA")
    print("   aparece %d veces" % nota.count(VIEJA))
    if nota.count(VIEJA) != 1:
        print("   ROJO: no aparece exactamente una vez. No se escribe.")
        return 1
    nueva = (
        "~~%s~~ CORRECCION DECLARADA (2026-09-04, vuelta 169, TAREA 5 del encargo, "
        "adjudicacion 6.7 del acta 168), POR EL CARRIL DEL BANCO 9.10 Y CON LA FRASE "
        "VIEJA TACHADA Y ENTERA ARRIBA. LOS CINCO SE LEYERON el 14 ago 2026 como LD-66 "
        "a LD-70, y viven en docs/plan/LD_SALES_ROADMAP.md con su razon una por una. "
        "SALDO: 1 A y 4 D. La cobertura de esa nomina paso de 10 de 15 a 15 de 15 y su "
        "deuda de P.5 quedo en CERO. CUATRO SEDES INDEPENDIENTES LO DICEN Y LAS CUATRO "
        "se leyeron hoy: las cinco cabeceras de LD_SALES_ROADMAP.md; la fila del "
        "universo de LECTURAS_DIRIGIDAS.md, donde el 5 pendiente esta TACHADO y puesto "
        "a 0; y las dos entradas de INVENTARIO.jsonl (el acto "
        "customer_validation_sales_roadmap y el racimo 'el sales roadmap'), las dos con "
        "cobertura 15 de 15 citando LD-66 a LD-70. ESTA FRASE ERA CIERTA EL DIA QUE SE "
        "ESCRIBIO y dejo de serlo tres dias despues; lo que la vuelta 169 corrige no es "
        "una mentira, es una nota que no siguio a su sujeto. Y SE MIDIO ADEMAS LO QUE "
        "NADIE HABIA MEDIDO: las SEIS nominas de esta ficha tienen HOY cobertura "
        "COMPLETA, cero pares sin veredicto en ninguna sede, con el resolutor delante "
        "(docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt). LO QUE ESTA CORRECCION NO "
        "HACE: no mueve ni un veredicto, no toca docs/INTRA_DOMINIO_VEREDICTOS.jsonl, "
        "no toca ni un nodo y no cambia el estado ni las dependencias de ninguna ficha. "
        "Ver docs/loop/SALIDA_V169_T5_LOTE_SALES_ROADMAP.txt" % VIEJA)
    nota_nueva = nota.replace(VIEJA, nueva, 1)
    f2 = dict(ficha)
    f2["nota"] = nota_nueva
    print("   CIFRA caracteres antes: %d | despues: %d" % (len(nota), len(nota_nueva)))
    print("   la frase vieja sigue dentro, TACHADA: %s" % (("~~%s~~" % VIEJA) in nota_nueva))
    movidos = [k for k in ficha if k != "nota" and ficha[k] != f2.get(k)]
    print("   CIFRA campos movidos ademas de `nota`: %d %s" % (len(movidos), movidos))
    if len(f2) != len(ficha) or movidos or ("~~%s~~" % VIEJA) not in nota_nueva:
        print("   ROJO: se movio algo que no era la nota.")
        return 1
    lineas = [l for l in io.open(OPERACIONES, encoding="utf-8") if l.strip()]
    lineas[idx[0]] = json.dumps(f2, ensure_ascii=False) + "\n"
    io.open(OPERACIONES, "w", encoding="utf-8", newline="\n").writelines(lineas)
    despues = cargar(OPERACIONES)
    print("H) ESCRITO Y RECONTADO")
    print("   CIFRA fichas antes: %d | despues: %d" % (len(fichas), len(despues)))
    print("   estado de la ficha, sin mover: %r" % despues[idx[0]].get("estado"))
    print("")
    print("VERDE: la nota de %s corregida por adicion, cero palabras viejas borradas."
          % FICHA)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
