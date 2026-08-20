# -*- coding: utf-8 -*-
"""censo_de_plantillas_talladas.py . CENSA LAS PLANTILLAS DE SALIDA DE LOS
INSTRUMENTOS DE NOMBRE ESTABLE BUSCANDO CIFRAS TALLADAS.

NOMBRE ESTABLE, y no lleva vuelta ni tramo ni lote: la vuelta entra por --vuelta
solo para rotular la salida, y el censo se puede re-correr cualquier dia. Es la
vara del acta 58, pregunta 4, la misma con la que nacieron
abrir_tramo_de_opu01.py, tallar_perdidas_del_plan.py y generar_plan_del_lote.py.

POR QUE NACE. El acta 62, pregunta 1 (linea 16171 de docs/loop/ACTA_AUDITOR.md),
contesta que las plantillas de los instrumentos estables NO piden vara nueva
porque LA REGLA 1 YA LAS CUBRE POR EXTENSION CITABLE: EL INSTRUMENTO MANDA dice
que toda cifra publicada se lee de la salida del instrumento corrido en esta
vuelta, asi que UNA PLANTILLA CON CIFRAS TALLADAS HACE DECIR AL INSTRUMENTO
CIFRAS QUE NO MIDIO, o sea viola la regla CADA VEZ QUE CORRE. Y lo que esa misma
respuesta encarga NO es doctrina sino MEDICION: este censo. La averia que lo
motiva es la de la vuelta 62, cazada al simular: registrar_cierre_de_tramo.py,
de nombre estable, llevaba TRES bloques de plantilla con las cifras del tramo 5.

ES ESTRICTAMENTE DE SOLO LECTURA. No escribe un script, ni un nodo, ni un plan.

--------------------------------------------------------------------------
LA VARA, ESCRITA ENTERA PARA QUE SE PUEDA DISCUTIR
--------------------------------------------------------------------------

1. QUE FICHERO ENTRA. Los .py de scripts/loop cuyo nombre NO lleva marca de
   corrida. Las marcas son seis y van impresas con su regla: el prefijo _ (los
   ficheros de contenido de una vuelta), vuelta<N>, v<N>_, acta<N>, tramo<N> y
   lote<X>. Un nombre que dice tramo o lote SIN numero (dossier_del_tramo.py,
   generar_plan_del_lote.py) es ESTABLE: lo que descalifica es el ordinal, no la
   palabra. La lista de excluidos se imprime contada, y con --excluidos entera.

2. QUE LITERAL ENTRA. Solo los que LLEGAN A LA SALIDA, y la ruta se imprime:
     print      . argumento de print(...)
     write      . argumento de .write(...) o de .writelines(...)
     format     . operando de un porciento, o argumento de .format(...), que
                  acaba impreso o escrito
     constante  . valor de cadena dentro de un dict o una lista asignados a un
                  NOMBRE EN MAYUSCULAS del modulo. Es la ruta de la CABECERA de
                  un plan sellado: no pasa por print, pero se publica igual.
   Un literal que solo vive en el docstring, en un comentario o en una variable
   interna NO entra: el docstring no es salida medida.

3. QUE CUENTA COMO CIFRA TALLADA, Y LA VARA ES DE INCLUSION, NO DE EXCLUSION.
   Sobre el literal se borran primero las marcas de formato porque sus digitos
   son ancho de campo y no medicion. En lo que queda, un grupo de digitos entra
   SOLO SI HACE DE CANTIDAD, y hacer de cantidad tiene cuatro formas medibles:
     a) el digito va DELANTE de un sustantivo de medida: 21 actos, 848 lineas,
        42 combinaciones, 34 vivos
     b) el sustantivo de medida va delante y el digito detras de dos puntos o de
        un igual: actos: 21
     c) el digito forma pareja con otro: 21 de 21, 6 contra 4, 0 / 50
     d) el digito lleva su unidad pegada: 16 por ciento
   TODO LO DEMAS ES CITA Y NO CUENTA, y esa es la mitad que hace util al censo:
   tramo 3, acto 23, vuelta 54, TABLA 2, PASO 1, CAMINO 2, guarda 1B, fase 04,
   acta 51, puestos 30 a 50. LA VARA AL REVES (buscar digitos y descartar citas)
   se probo primero y dio ONCE TALLADOS de quince, casi todos citas: una vara que
   marca a casi todo el mundo no separa a nadie.

   LO QUE NO ENTRA EN EL VEREDICTO PERO SE IMPRIME IGUAL: los digitos que
   sobreviven a las exclusiones de cita pero NO hacen de cantidad salen en la
   lista DEBIL del paso 4, contados por fichero. No fijan veredicto, y estan ahi
   para que nadie tenga que fiarse de que la vara no se dejo nada.

4. EL VEREDICTO POR FICHERO, que es lo que el encargo pide:
     TALLADO      . le sobrevive al menos una CANTIDAD, con su linea citada
     DECLARA FALTA. no le sobrevive ninguno Y ADEMAS trae al menos un literal que
                    declara la ausencia de su insumo: es la forma debida que el
                    acta 62 prescribe, armar del insumo o DECLARAR su falta
     MEDIDO       . no le sobrevive ninguno y no necesita declarar nada porque
                    todas las cifras de su salida entran por argumento

5. LO QUE ESTE CENSO NO HACE, dicho para que nadie le pida lo que no da: NO
   adjudica cuales de los TALLADOS hay que corregir. Un TALLADO en un fichero que
   no va a volver a correr miente en un papel muerto; uno en un fichero vivo
   miente la proxima vez. Esa adjudicacion es del reporte, no del instrumento.

Uso:
  python scripts/loop/censo_de_plantillas_talladas.py --vuelta 63
  python scripts/loop/censo_de_plantillas_talladas.py --vuelta 63 --excluidos
  python scripts/loop/censo_de_plantillas_talladas.py --vuelta 63 --raiz scripts/loop

exit 0 si el censo corre; exit 1 si algun fichero no se pudo leer o parsear.
"""
import argparse
import ast
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)

# 1. LAS SEIS MARCAS DE CORRIDA, cada una con su nombre para imprimirla.
MARCAS = (
    (r"^_", "prefijo _ (fichero de contenido de una vuelta)"),
    (r"vuelta\d+", "vuelta<N> en el nombre"),
    (r"v\d+_", "v<N>_ en el nombre"),
    (r"acta\d+", "acta<N> en el nombre"),
    (r"tramo\d+", "tramo<N> en el nombre"),
    (r"lote[_-]?[a-z0-9](?![a-z])", "lote<X> en el nombre"),
)

# 3a. LAS MARCAS DE FORMATO, que se borran antes de buscar digitos.
FORMATO = (
    re.compile(r"%[-+ #0]*[\d.*]*[hlL]?[diouxXeEfFgGcrsa%]"),
    re.compile(r"\{[^{}]*\}"),
)

# 3b. LOS DESCARTES, cada uno con su motivo. Se prueban sobre la ventana previa
#     al grupo de digitos y sobre el propio token que lo contiene.
DESCARTES_PREVIOS = (
    (r"\blineas?\s+\*{0,2}$", "numero de LINEA citada"),
    (r"\bP\.\s*$", "punto del BANCO DEL PLAN"),
    (r"\bacta\s+$", "numero de ACTA"),
    (r"\bvueltas?\s+$", "numero de VUELTA"),
    (r"\bbanco\s+$", "punto del BANCO"),
    (r"\bseccion\s+$", "numero de SECCION"),
    (r"\bpunto\s+$", "numero de PUNTO"),
    (r"\bregla\s+$", "numero de REGLA"),
    (r"\bpregunta\s+$", "numero de PREGUNTA"),
    (r"\bfila\s+$", "numero de FILA citada"),
    (r"\bpuesto\s+$", "numero de PUESTO citado"),
    (r"\bcanon\s+$", "punto del CANON"),
    (r"\bago\s+$", "ano de una FECHA"),
    (r"\bde\s+20$", "ano de una FECHA"),
    (r"\bv$", "numero de VERSION de un contrato"),
    (r"\bversion\s+$", "numero de VERSION"),
)
DESCARTES_TOKEN = (
    (r"\.(py|json|jsonl|txt|md)\b", "nombre de FICHERO"),
    (r"/", "RUTA de fichero"),
    (r"^OP-", "id de OPERACION"),
    (r"opu\d+", "id de OPERACION en minuscula"),
    (r"^\d{4}-\d{2}-\d{2}", "FECHA ISO"),
    (r"^v\d+$", "numero de VERSION"),
    (r"^P\.\d", "punto del BANCO DEL PLAN"),
    (r"^\d+[a-z]$", "ordinal con letra: rotulo de guarda o de canon"),
)
# 4. LAS DECLARACIONES DE FALTA.
FALTA = (
    r"SIN NUMERO", r"no se pudo leer", r"no existe la salida", r"no existe el",
    r"sin insumo", r"NO LO DICE", r"no trae el", r"no se pudo",
)
DIGITOS = re.compile(r"\d+")
TOKEN = re.compile(r"\S+")

# 3. LOS SUSTANTIVOS DE MEDIDA. Es la lista que convierte un digito en CANTIDAD.
#    Va escrita entera y no derivada, para que se pueda discutir palabra a palabra.
MEDIDAS = (
    "acto", "actos", "nodo", "nodos", "vivo", "vivos", "deprecado", "deprecados",
    "fichero", "ficheros", "pieza", "piezas", "perdida", "perdidas", "paso",
    "pasos", "condicion", "condiciones", "arista", "aristas", "duplicada",
    "duplicadas", "colision", "colisiones", "combinacion", "combinaciones",
    "grupo", "grupos", "entrada", "entradas", "enlace", "enlaces", "linea",
    "lineas", "id", "ids", "miembro", "miembros", "semilla", "semillas",
    "puente", "puentes", "inciso", "incisos", "fundido", "fundidos", "declarado",
    "declarados", "mirado", "mirados", "absorbido", "absorbidos", "superviviente",
    "supervivientes", "par", "pares", "veredicto", "veredictos", "hallazgo",
    "hallazgos", "fila", "filas", "columna", "columnas", "caracteres", "bytes",
    "barridos", "muerto", "muertos", "mueren", "descalces", "huecos", "olvidos",
    "auto-aristas", "redirecciones", "operaciones", "etiquetas", "assets",
)
CANTIDAD = (
    (re.compile(r"\d+\s+(?:%s)\b" % "|".join(MEDIDAS), re.I), "digito DELANTE de un sustantivo de medida"),
    (re.compile(r"(?:%s)\s*[:=]\s*\d+" % "|".join(MEDIDAS), re.I), "sustantivo de medida y el digito tras dos puntos"),
    (re.compile(r"\d+\s*(?:de|contra|/|sobre)\s*\d+", re.I), "pareja de cifras"),
    (re.compile(r"\d+\s+por\s+ciento", re.I), "cifra con su unidad"),
)


def marca_de_corrida(nombre):
    for patron, etiqueta in MARCAS:
        if re.search(patron, nombre):
            return etiqueta
    return None


def rutas_a_la_salida(arbol):
    """Devuelve {id(nodo_constante): ruta} para los literales que LLEGAN a la salida."""
    padres = {}
    for n in ast.walk(arbol):
        for h in ast.iter_child_nodes(n):
            padres[id(h)] = n

    def marcar(nodo, ruta, acc):
        for x in ast.walk(nodo):
            if isinstance(x, ast.Constant) and isinstance(x.value, str):
                acc.setdefault(id(x), ruta)

    acc = {}
    for n in ast.walk(arbol):
        if isinstance(n, ast.Call):
            f = n.func
            if isinstance(f, ast.Name) and f.id == "print":
                for a in list(n.args) + [k.value for k in n.keywords]:
                    marcar(a, "print", acc)
            elif isinstance(f, ast.Attribute) and f.attr in ("write", "writelines"):
                for a in n.args:
                    marcar(a, "write", acc)
            elif isinstance(f, ast.Attribute) and f.attr == "format":
                marcar(f.value, "format", acc)
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mod):
            p = padres.get(id(n))
            while isinstance(p, (ast.BinOp, ast.Tuple)):
                p = padres.get(id(p))
            if isinstance(p, ast.Call):
                f = p.func
                va = ((isinstance(f, ast.Name) and f.id == "print")
                      or (isinstance(f, ast.Attribute) and f.attr in ("write", "writelines")))
                if va:
                    marcar(n.left, "format", acc)
        if isinstance(n, ast.Assign):
            nombres = [t.id for t in n.targets if isinstance(t, ast.Name)]
            if any(x.isupper() for x in nombres) and isinstance(n.value, (ast.Dict, ast.List, ast.Tuple)):
                marcar(n.value, "constante", acc)
    return acc


def descartar(literal, ini):
    """Devuelve el motivo del descarte, o None si el grupo de digitos SOBREVIVE."""
    previo = literal[:ini]
    for patron, motivo in DESCARTES_PREVIOS:
        if re.search(patron, previo, re.I):
            return motivo
    tok = ""
    for m in TOKEN.finditer(literal):
        if m.start() <= ini < m.end():
            tok = m.group(0)
            break
    for patron, motivo in DESCARTES_TOKEN:
        if re.search(patron, tok, re.I):
            return motivo
    return None


def censar_fichero(ruta, nombre):
    src = io.open(ruta, encoding="utf-8").read()
    arbol = ast.parse(src, filename=nombre)
    rutas = rutas_a_la_salida(arbol)
    docstrings = set()
    for n in ast.walk(arbol):
        if isinstance(n, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            d = ast.get_docstring(n, clean=False)
            if d is not None and n.body and isinstance(n.body[0], ast.Expr):
                docstrings.add(id(n.body[0].value))
    cantidades, debiles, descartados, declara = [], [], [], []
    for n in ast.walk(arbol):
        if not (isinstance(n, ast.Constant) and isinstance(n.value, str)):
            continue
        if id(n) in docstrings or id(n) not in rutas:
            continue
        lit = n.value
        for patron in FALTA:
            if re.search(patron, lit, re.I):
                declara.append((n.lineno, lit))
                break
        limpio = lit
        for rx in FORMATO:
            limpio = rx.sub(" ", limpio)
        tramos = []
        for rx, etq in CANTIDAD:
            for mm in rx.finditer(limpio):
                tramos.append((mm.start(), mm.end(), etq))
        for m in DIGITOS.finditer(limpio):
            fila = [n.lineno, rutas[id(n)], m.group(0),
                    limpio[max(0, m.start() - 46):m.end() + 34].replace(NL, " "), ""]
            motivo = descartar(limpio, m.start())
            if motivo:
                fila[4] = motivo
                descartados.append(fila)
                continue
            forma = [e for i, j, e in tramos if i <= m.start() < j]
            if forma:
                fila[4] = forma[0]
                cantidades.append(fila)
            else:
                fila[4] = "no hace de cantidad"
                debiles.append(fila)
    return cantidades, debiles, descartados, declara


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, default=None)
    ap.add_argument("--raiz", default="scripts/loop")
    ap.add_argument("--excluidos", action="store_true",
                    help="imprime tambien la lista entera de ficheros excluidos")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    base = os.path.join(RAIZ, a.raiz.replace("/", os.sep))
    print("=" * 78)
    print("CENSO DE PLANTILLAS TALLADAS EN LOS INSTRUMENTOS DE NOMBRE ESTABLE")
    if a.vuelta:
        print("  corrido en la vuelta %d" % a.vuelta)
    print("  raiz: %s" % a.raiz)
    print("=" * 78)
    print()

    estables, excluidos = [], []
    for nombre in sorted(os.listdir(base)):
        if not nombre.endswith(".py"):
            continue
        etq = marca_de_corrida(nombre)
        if etq:
            excluidos.append((nombre, etq))
        else:
            estables.append((nombre, etq))

    print("PASO 1: QUIEN ENTRA")
    print("  .py en la raiz                 : %d" % (len(estables) + len(excluidos)))
    print("  EXCLUIDOS por marca de corrida : %d" % len(excluidos))
    if a.excluidos:
        for nombre, etq in excluidos:
            print("     %-52s %s" % (nombre, etq))
    else:
        print("     (con --excluidos se imprime la lista entera con su marca)")
    print("  DE NOMBRE ESTABLE, y son los que se censan: %d" % len(estables))
    for nombre, _ in estables:
        print("     %s" % nombre)
    print()

    fallos = []
    fichas = []
    for nombre, _ in estables:
        ruta = os.path.join(base, nombre)
        try:
            can, deb, desc, decl = censar_fichero(ruta, nombre)
        except Exception as e:
            fallos.append("%s: %s" % (nombre, e))
            continue
        if can:
            veredicto = "TALLADO"
        elif decl:
            veredicto = "DECLARA FALTA"
        else:
            veredicto = "MEDIDO"
        fichas.append((nombre, veredicto, can, deb, desc, decl))

    print("PASO 2: EL VEREDICTO POR FICHERO")
    print()
    print("  %-46s %-14s %7s %7s %7s %7s"
          % ("fichero", "veredicto", "cantid.", "debil", "cita", "falta"))
    print("  " + "-" * 94)
    for nombre, veredicto, can, deb, desc, decl in fichas:
        print("  %-46s %-14s %7d %7d %7d %7d"
              % (nombre, veredicto, len(can), len(deb), len(desc), len(decl)))
    cuenta = {}
    for f in fichas:
        cuenta[f[1]] = cuenta.get(f[1], 0) + 1
    print()
    print("  RESUMEN: %s" % ("   ".join("%s %d" % (k, cuenta[k]) for k in sorted(cuenta))))
    print()

    print("PASO 3: LOS TALLADOS, CON SU LINEA CITADA")
    print()
    hay = False
    for nombre, veredicto, can, deb, desc, decl in fichas:
        if veredicto != "TALLADO":
            continue
        hay = True
        print("  --- %s   (%d cantidades talladas)" % (nombre, len(can)))
        for fila in can:
            print("      linea %-5d ruta %-10s cifra %-6s %-46s"
                  % (fila[0], fila[1], fila[2], fila[4]))
            print("            ...%s..." % fila[3])
        print()
    if not hay:
        print("  NINGUNO. CERO TALLADOS EN LOS %d INSTRUMENTOS DE NOMBRE ESTABLE," % len(fichas))
        print("  y esa ausencia se publica igual que se habria publicado un hallazgo.")
        print()

    print("PASO 4: LA LISTA DEBIL, que NO fija veredicto y se publica igual")
    print("  (digitos que pasan las exclusiones de cita pero NO hacen de cantidad)")
    print()
    for nombre, veredicto, can, deb, desc, decl in fichas:
        if not deb:
            continue
        print("  --- %s (%d)" % (nombre, len(deb)))
        for fila in deb:
            print("      linea %-5d cifra %-6s ...%s..." % (fila[0], fila[2], fila[3]))
        print()

    print("PASO 5: LOS DESCARTES POR CITA, CON SU MOTIVO (la vara, vista trabajar)")
    print()
    for nombre, veredicto, can, deb, desc, decl in fichas:
        if not desc:
            continue
        print("  --- %s (%d descartes)" % (nombre, len(desc)))
        for fila in desc:
            print("      linea %-5d cifra %-6s %-40s ...%s..."
                  % (fila[0], fila[2], fila[4], fila[3]))
        print()

    print("PASO 6: LAS DECLARACIONES DE FALTA, que son la forma debida")
    print()
    for nombre, veredicto, can, deb, desc, decl in fichas:
        if not decl:
            continue
        print("  --- %s (%d)" % (nombre, len(decl)))
        for lineno, lit in decl:
            print("      linea %-5d %s" % (lineno, lit.replace(NL, " ")[:110]))
        print()

    if fallos:
        print("ROJO, %d fichero(s) no se pudieron censar:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
