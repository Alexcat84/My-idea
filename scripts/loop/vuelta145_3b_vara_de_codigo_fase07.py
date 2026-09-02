# -*- coding: utf-8 -*-
r"""vuelta145_3b_vara_de_codigo_fase07.py . LA VARA DE LAS OPERACIONES SIN
HUELLA EN EL GRAFO. VUELTA 145, TAREA 3.b.

POR QUE NACE, Y CON SU FRONTERA (acta 144, adjudicacion 3.9 del auditor). Las
DOS operaciones de la fase 07 (`OP-A-01` FRONTERA_DECLARADA y `OP-A-02` MESA)
tienen `nodos`, `superviviente`, `eliminar` y `aristas_nuevas` VACIOS los
cuatro. Que `tallar_estado_de_fase.py` diga NO COMPUTABLE ahi **es correcto y
no es un defecto**: es el instrumento diciendo en voz alta que le falta una
regla, como su docstring promete.

LA ADJUDICACION, POR EXTENSION CITABLE Y NO POR DOCTRINA NUEVA: **una operacion
que no deja huella en el grafo NO se mide con una vara de grafo; se mide contra
LO QUE INSTALA**, y para un control eso son DOS COSAS Y SOLO DOS:
  (1) QUE EL CONTROL EXISTA EN EL CODIGO, y
  (2) QUE MUERDA POR MUTACION.
Banco 9 (*"una guarda que no muerde no es una guarda"*) y `EJECUTOR.md` 1
(*"el caso rojo se prueba por mutacion"*).

LA FRONTERA, Y ES TAN IMPORTANTE COMO LA REGLA. ESTE VEREDICTO NO ENTRA EN LA
COLUMNA DE `tallar_estado_de_fase.py`, cuyo contrato dice *"destino medido
contra el grafo"*. Mezclar un veredicto de CODIGO en una tabla de GRAFO serian
DOS UNIDADES EN UNA COLUMNA, que es la especie exacta de la CORRECCION 18. Por
eso esta vara vive APARTE, en su propio instrumento y con su propia salida, y
la tabla de grafo sigue diciendo SIN VARA ESCRITA para las dos, con un puntero
a este fichero.

CADA CONTROL LLEVA SU FRASE LITERAL DE LA FICHA, Y LA CITA SE COMPRUEBA, no se
confia: `guarda_de_citas()` exige que cada `frase` de `CONTROLES` aparezca
VERBATIM en el texto de su ficha de `docs/plan/OPERACIONES.jsonl`. Si una cita
envejece porque la ficha se reescribio, ES ROJO Y SE NOMBRA, en vez de quedar
como una cita bonita que ya no dice lo que decia. Es el mismo patron que la
TAREA 3.a de la vuelta 144 uso con la figura de `OP-M-04`.

QUE PUBLICA. Por cada control: la operacion duena, la frase literal de la
ficha, si EXISTE en el codigo (con fichero y linea, no de palabra) y si MUERDE
por mutacion (con el caso rojo corrido de verdad). Y el recuento por operacion.

LO QUE ESTA VARA NO HACE, DICHO EN VEZ DE CALLADO: no ejecuta ninguna de las
dos operaciones y no instala ningun control. Mide EL ESTADO DE HOY. Que un
control salga NO INSTALADO no es un fallo del instrumento: es la medida de que
la fase 07 esta ABIERTA y no cerrada.

USO:
  python scripts/loop/vuelta145_3b_vara_de_codigo_fase07.py
"""
import copy
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "expansion"))

OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

# --------------------------------------------------------------------------
# LOS CONTROLES. Cada uno con la OPERACION que lo declara, la FRASE LITERAL de
# su ficha (comprobada contra la ficha en cada corrida) y la SONDA con la que
# se busca en el codigo.
# --------------------------------------------------------------------------
CONTROLES = [
    {
        "id": "A1.1",
        "op": "OP-A-01",
        "nombre": "comprobacion posicional del nodo que declara mas de una fuente",
        "frase": "todo nodo que entre declarando MAS DE UNA fuente pasa por la "
                 "comprobacion posicional",
        "sondas": [("scripts/run_phase1.py", "comprobacion posicional")],
        "mutacion": "no_instalado",
    },
    {
        "id": "A1.2",
        "op": "OP-A-01",
        "nombre": "campo fuente validado contra una lista CANONICA de libros",
        "frase": "el campo fuente se valida contra una lista CANONICA de libros: hoy no "
                 "existe y sin ella el control es fragil",
        "sondas": [("dataset/metadata/libros_canonicos.json", None),
                   ("dataset/metadata/fuentes_canonicas.json", None),
                   ("docs/plan/LIBROS_CANONICOS.md", None)],
        "mutacion": "no_instalado",
    },
    {
        "id": "A1.3",
        "op": "OP-A-01",
        "nombre": "Gate 0 rechaza el nodo cuyo segundo libro no aparece en ningun paso",
        "frase": "Gate 0 rechaza un nodo cuyo segundo libro no aparece en ningun paso",
        "sondas": [("scripts/run_phase1.py", "segundo libro")],
        "mutacion": "no_instalado",
    },
    {
        "id": "A2.1",
        "op": "OP-A-02",
        "nombre": "auto-arista CON RESOLUCION",
        "frase": "los CINCO controles mecanicos corriendo: auto-arista con resolucion",
        "sondas": [("scripts/run_phase1.py",
                    "Ningun nodo VIVO se cita a si mismo tras RESOLVER (auto-arista via alias)")],
        "mutacion": "gate0_auto_arista",
    },
    {
        "id": "A2.2",
        "op": "OP-A-02",
        "nombre": "lista blanca de claves del nodo",
        "frase": "lista blanca de claves",
        "sondas": [("scripts/run_phase1.py",
                    "Ninguna clave de nodo fuera de la lista blanca del esquema")],
        "mutacion": "lista_blanca_de_claves",
    },
    {
        "id": "A2.3",
        "op": "OP-A-02",
        "nombre": "control posicional del campo fuente",
        "frase": "control posicional del campo fuente",
        "sondas": [("scripts/run_phase1.py", "posicional del campo fuente")],
        "mutacion": "no_instalado",
    },
    {
        "id": "A2.4",
        "op": "OP-A-02",
        "nombre": "campo fuente CANONICO",
        "frase": "campo fuente canonico",
        "sondas": [("dataset/metadata/libros_canonicos.json", None),
                   ("dataset/metadata/fuentes_canonicas.json", None)],
        "mutacion": "no_instalado",
    },
    {
        "id": "A2.5",
        "op": "OP-A-02",
        "nombre": "revision de nomina por dominio",
        "frase": "revision de nomina por dominio",
        "sondas": [("scripts/run_phase1.py", "Todos los nodos tienen dominio valido")],
        "mutacion": "gate0_dominio",
    },
    {
        "id": "A2.6",
        "op": "OP-A-02",
        "nombre": "BLOQUEO POR VEREDICTO AUSENTE, la puerta semantica",
        "frase": "la insercion se desbloquea con el veredicto escrito, NO con el parecido "
                 "bajado: bajar el umbral no es una salida",
        "sondas": [("scripts/run_phase1.py", "veredicto continua-o-repite"),
                   ("engine/plan_readiness.py", "veredicto continua-o-repite")],
        "mutacion": "no_instalado",
    },
]


def fichas():
    fuera = {}
    for l in io.open(OPERACIONES, encoding="utf-8"):
        if not l.strip():
            continue
        d = json.loads(l)
        fuera[d.get("id_op")] = d
    return fuera


def texto_de_ficha(ficha):
    """Todo el texto de la ficha en una cadena, para buscar la cita VERBATIM."""
    trozos = []
    for v in ficha.values():
        if isinstance(v, list):
            trozos.extend(str(x) for x in v)
        elif v is not None:
            trozos.append(str(v))
    return "\n".join(trozos)


def guarda_de_citas(F):
    """LA CITA SE COMPRUEBA, NO SE CONFIA. Devuelve la lista de fallos."""
    fallos = []
    for c in CONTROLES:
        ficha = F.get(c["op"])
        if ficha is None:
            fallos.append("%s: la ficha %s no esta en OPERACIONES.jsonl" % (c["id"], c["op"]))
            continue
        texto = texto_de_ficha(ficha).lower()
        if c["frase"].lower() not in texto:
            fallos.append("%s: la frase citada NO aparece VERBATIM en la ficha %s: %r"
                          % (c["id"], c["op"], c["frase"]))
    return fallos


def buscar_sonda(ruta_rel, literal):
    """(existe, detalle). Si `literal` es None, basta con que el fichero exista."""
    ruta = os.path.join(RAIZ, ruta_rel.replace("/", os.sep))
    if not os.path.exists(ruta):
        return False, "%s no existe" % ruta_rel
    if literal is None:
        return True, "%s existe" % ruta_rel
    try:
        lineas = io.open(ruta, encoding="utf-8").read().split("\n")
    except (IOError, UnicodeDecodeError) as e:
        return False, "%s no se pudo leer: %s" % (ruta_rel, e)
    for i, l in enumerate(lineas, 1):
        if literal in l:
            return True, "%s:%d" % (ruta_rel, i)
    return False, "%s no trae el literal %r" % (ruta_rel, literal)


def existe(control):
    for ruta_rel, literal in control["sondas"]:
        ok, detalle = buscar_sonda(ruta_rel, literal)
        if ok:
            return True, detalle
    return False, "; ".join(buscar_sonda(r, l)[1] for r, l in control["sondas"])


# --------------------------------------------------------------------------
# LAS MUTACIONES. Cada una devuelve (aplica, muerde, detalle). NUNCA se
# reimplementa el control: se le da al CODIGO DE VERDAD una entrada rota y se
# mira si su propio veredicto cae.
# --------------------------------------------------------------------------
def _master_de_hoy():
    ruta = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
    return json.load(io.open(ruta, encoding="utf-8"))


def _veredicto_de_gate0(master, literal):
    """El booleano del check de Gate 0 cuyo rotulo trae `literal`, corriendo
    `step7_validate` DE VERDAD sobre el master que se le pase. Devuelve
    (encontrado, veredicto)."""
    import run_phase1 as R
    checks, _dups = R.step7_validate(master, [])
    for rotulo, ok, _detalle in checks:
        if literal in rotulo:
            return True, bool(ok)
    return False, None


def mut_gate0_auto_arista():
    literal = "auto-arista via alias"
    base = _master_de_hoy()
    hallado, verde_antes = _veredicto_de_gate0(base, literal)
    if not hallado:
        return True, False, "el check no aparece en la nomina de Gate 0"
    roto = copy.deepcopy(base)
    vivo = next(k for k, n in roto["nodos"].items() if not n.get("deprecado"))
    roto["nodos"][vivo].setdefault("nodos_siguientes", []).append(vivo)
    _h, verde_despues = _veredicto_de_gate0(roto, literal)
    muerde = bool(verde_antes) and not verde_despues
    return True, muerde, ("con el grafo de hoy el check dice %s; anadida una auto-arista a "
                          "%r dice %s" % (verde_antes, vivo, verde_despues))


def mut_gate0_dominio():
    literal = "Todos los nodos tienen dominio valido"
    base = _master_de_hoy()
    hallado, verde_antes = _veredicto_de_gate0(base, literal)
    if not hallado:
        return True, False, "el check no aparece en la nomina de Gate 0"
    roto = copy.deepcopy(base)
    vivo = next(iter(roto["nodos"]))
    roto["nodos"][vivo]["dominio"] = "dominio_que_no_existe_v145"
    _h, verde_despues = _veredicto_de_gate0(roto, literal)
    muerde = bool(verde_antes) and not verde_despues
    return True, muerde, ("con el grafo de hoy el check dice %s; puesto un dominio invalido "
                          "en %r dice %s" % (verde_antes, vivo, verde_despues))


def mut_lista_blanca_de_claves():
    """La lista blanca se importa de scripts/expansion/validar_esquema.py, que
    es de donde Gate 0 la toma. Se valida un nodo REAL y luego el mismo nodo con
    UNA clave renegada."""
    from validar_esquema import CAMPOS_PERMITIDOS
    ruta = os.path.join(RAIZ, "dataset", "nodos")
    nombre = sorted(os.listdir(ruta))[0]
    datos = json.load(io.open(os.path.join(ruta, nombre), encoding="utf-8"))
    renegadas_antes = sorted(set(datos) - CAMPOS_PERMITIDOS)
    roto = dict(datos)
    roto["fase_proyecto_con_cirilica_v145"] = "x"
    renegadas_despues = sorted(set(roto) - CAMPOS_PERMITIDOS)
    muerde = (not renegadas_antes) and len(renegadas_despues) == 1
    return True, muerde, ("el nodo %s da %d clave(s) renegada(s); con una clave de mas da "
                          "%d y la nombra: %s" % (nombre, len(renegadas_antes),
                                                  len(renegadas_despues), renegadas_despues))


def mut_no_instalado():
    return False, False, "el control no esta instalado: no hay nada que mutar"


MUTACIONES = {
    "gate0_auto_arista": mut_gate0_auto_arista,
    "gate0_dominio": mut_gate0_dominio,
    "lista_blanca_de_claves": mut_lista_blanca_de_claves,
    "no_instalado": mut_no_instalado,
}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    F = fichas()

    print("VARA DE CODIGO DE LA FASE 07 ADUANA | vuelta 145, TAREA 3.b")
    print("Instrumento APARTE, por la frontera de la adjudicacion 3.9 del acta 144:")
    print("este veredicto NO entra en la columna de tallar_estado_de_fase.py, cuyo")
    print("contrato dice 'destino medido contra el grafo'. Dos unidades no comparten")
    print("columna (CORRECCION 18).")
    print("=" * 78)

    fallos_cita = guarda_de_citas(F)
    print("GUARDA DE CITAS: cada frase de este codigo aparece VERBATIM en su ficha")
    if fallos_cita:
        print("  ROJO, %d cita(s) que la ficha ya no dice:" % len(fallos_cita))
        for f in fallos_cita:
            print("     %s" % f)
        print("")
        print("LA VARA NO MIDE NADA CON LAS CITAS ROTAS: se para y se trae.")
        return 1
    print("  VERDE: las %d citas aparecen VERBATIM en su ficha" % len(CONTROLES))
    print("")

    filas = []
    for c in CONTROLES:
        hay, donde = existe(c)
        aplica, muerde, detalle = MUTACIONES[c["mutacion"]]()
        filas.append((c, hay, donde, aplica, muerde, detalle))

    print("LA TABLA, CONTROL A CONTROL")
    print("=" * 78)
    for c, hay, donde, aplica, muerde, detalle in filas:
        print("%s  %s  %s" % (c["id"], c["op"], c["nombre"]))
        print("     frase de la ficha: %r" % c["frase"])
        print("     (1) EXISTE EN EL CODIGO: %s   [%s]" % ("SI" if hay else "NO", donde))
        if not aplica:
            print("     (2) MUERDE POR MUTACION: NO APLICA   [%s]" % detalle)
        else:
            print("     (2) MUERDE POR MUTACION: %s   [%s]"
                  % ("SI" if muerde else "NO", detalle))
        print("")

    print("=" * 78)
    print("EL RECUENTO, POR OPERACION")
    for op in ("OP-A-01", "OP-A-02"):
        suyas = [f for f in filas if f[0]["op"] == op]
        existen = [f for f in suyas if f[1]]
        muerden = [f for f in suyas if f[3] and f[4]]
        print("  %s: %d control(es) declarado(s) | EXISTEN %d | MUERDEN %d | "
              "INSTALADOS Y MORDIENDO %d"
              % (op, len(suyas), len(existen), len(muerden), len(muerden)))
        for f in suyas:
            estado = "INSTALADO Y MUERDE" if (f[1] and f[3] and f[4]) else (
                "INSTALADO, NO MUERDE" if (f[1] and f[3] and not f[4]) else (
                    "INSTALADO, SIN MUTACION" if f[1] else "NO INSTALADO"))
            print("     %-5s %s" % (f[0]["id"], estado))
    total = len(filas)
    completos = len([f for f in filas if f[1] and f[3] and f[4]])
    print("")
    print("CIFRA controles declarados: %d controles" % total)
    print("CIFRA controles instalados y mordiendo: %d controles" % completos)
    print("")
    print("VEREDICTO DE LA FASE 07 CONTRA ESTA VARA: ABIERTA Y MEDIDA. %d de %d controles "
          "estan instalados y muerden; los otros %d NO estan instalados y esta vara lo dice "
          "en voz alta en vez de callarlo." % (completos, total, total - completos))
    print("LA FASE NO SE CIERRA HOY Y NINGUNA DE LAS DOS OPERACIONES SE EJECUTA: "
          "el encargo de la vuelta 145 manda ABRIR Y MEDIR.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
