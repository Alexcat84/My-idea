# -*- coding: utf-8 -*-
"""barrido_titulos_tallados.py . CENSA LAS CONSTANTES DE TRAMO Y DE VUELTA
TALLADAS A MANO EN LOS TITULOS DE LOS INSTRUMENTOS DEL BUCLE.

NOMBRE ESTABLE A PROPOSITO, y por la vara que este mismo barrido persigue: no
lleva numero de vuelta, la vuelta se pasa con --vuelta y el barrido no talla
ninguna cifra en su propio titulo. Si se clonara cada vuelta seria un ejemplar
de la especie que caza.

POR QUE NACE (acta 58, pregunta 3, contestada POR BARRIDO y llevada al encargo):
dos ejemplares de la misma especie cazados por tropiezo en dos vueltas seguidas
no son casualidad, son una poblacion sin censar. Los dos ejemplares, que son la
CALIBRACION de este instrumento y no un adorno del docstring:

  1. scripts/loop/vuelta56_varas_tramo3.py, linea 101:
     print("EL CUADRO DE VARAS DE LOS %d ACTOS DEL TRAMO 3 (vuelta 54)" ...)
     El instrumento recibe el fichero del tramo por --tramo, asi que se le puede
     apuntar a cualquier tramo, pero el titulo dice TRAMO 3 y vuelta 54 pase lo
     que pase. La vuelta 58 lo corrio sobre el tramo 5 y el titulo mintio.
  2. scripts/loop/vuelta57_tramo4_nomina.py, linea 193:
     print("EL ABRIDOR DEL TRAMO %d DE OP-U-01 (vuelta 57)" % TRAMO)
     La vuelta 58 copio este fichero para abrir el tramo 5 y la copia heredo el
     "(vuelta 57)" tallado. Se cazo CORRIENDOLO, no leyendolo.

LAS TRES CLASES, y cada una se decide MIDIENDO, no opinando:

  ROJO, PUEDE MENTIR: el numero esta tallado en el titulo Y el instrumento
    recibe su sujeto POR ARGUMENTO (--tramo, --vuelta, --nomina, --plan,
    --fichero, --entrada, --corte). Se le puede apuntar a otro sujeto y el
    titulo no se entera. Es la especie del ejemplar 1.
  AMBAR, NO CALZA: el numero tallado no coincide con ningun numero de la MISMA
    especie que el propio fichero declare, sea en su nombre (vueltaNN_, _vNN_,
    tramoN) o en la ruta fija que lee (TRAMO4_V57, PLAN_V57, SALIDA_V58). LA
    MAQUINA NO DECIDE QUE ES: puede NOMBRAR UN ANCESTRO a proposito ("sucesor
    del de la vuelta 55"), que es procedencia y no envejece nunca, o puede ser
    una CITA ENVEJECIDA como la del ejemplar 2, la copia que heredo la vuelta
    del ancestro. El barrido lista las dos juntas y DICE que no las separa; el
    ojo las separa leyendo la linea. Un barrido que fingiera resolverlo por
    regla estaria inventando doctrina.
  CENSO, SELLO FIJO: el numero esta tallado pero calza con lo que el fichero
    declara de si mismo y no hay argumento que lo repunte. El titulo nombra su
    propio sujeto fijo y no puede mentir sin que alguien reescriba el fichero.
    NO ES DEUDA HOY: es el censo para la vuelta que lo toque.

  ROTULADO, EL AMBAR YA TRIADO (anadido el 21 ago 2026, vuelta 61, TAREA 1, por
    el carril del banco 9.10 y por la via del rotulo con vigente= de la vuelta 58):
    un AMBAR deja de ser deuda cuando el fichero lleva un ROTULO que DECLARA que
    especie es, Y EL ROTULO SE COTEJA POR MAQUINA EN CADA CORRIDA. No es un
    silenciador: es una declaracion con guarda, y la guarda prefiere ROJO a
    callar. Dos especies, cada una con su cotejo:

      ROTULO titulo especie=SELLO_FIJO sujeto=tramo:2 corte=<fecha> motivo=<texto>
        El fichero declara que su sujeto es ESE tramo, que es justo lo que su
        nombre no dice y por lo que el AMBAR salio. SE COTEJA: el numero tallado
        tiene que ser el declarado, y el fichero NO puede recibir esa especie por
        argumento. Si manana alguien le anade --tramo, el rotulo cae en ROJO. O
        sea: un instrumento repuntable NO se puede silenciar con este rotulo.

      ROTULO titulo especie=PROCEDENCIA cita=vuelta:40 fuente=<ruta> prueba=<literal> corte=<fecha>
        El numero NOMBRA UN ANCESTRO o un sujeto ajeno a proposito (el acta de la
        vuelta 40, la propuesta de la 35, el instrumento del que se copio la
        aritmetica), y por eso no envejece. SE COTEJA: la fuente citada tiene que
        EXISTIR y contener el literal de prueba. Si el ancestro desaparece o se
        renombra, el rotulo cae en ROJO.

    UN ROTULO QUE NO CASA CON NINGUN AMBAR VIVO ES ROJO (rotulo huerfano): asi un
    rotulo no se queda de adorno cuando el titulo que cubria ya se corrigio.
    LAS LINEAS DE ROTULO NO SE BARREN NI CUENTAN COMO DECLARACION DEL FICHERO:
    se recortan del texto antes de medir, para que el rotulo no mueva la
    clasificacion de los demas numeros del mismo fichero.

VERDE es no salir: el numero llega por %s alimentado de un argumento o de una
medicion (a.vuelta, la clave orden_tramoN leida del fichero), que es la via ya
estrenada por tallar_cabecera_reporte.py y por vuelta58_varas_tramo.py.

QUE MIRA, y solo eso (el encargo: "sus cabeceras y sus print de titulo"):
  CABECERA: el primer bloque del docstring del modulo, hasta la primera linea en
    blanco. Es la linea de titulo del instrumento. La prosa de mas abajo NO se
    barre: un docstring que cuenta lo que le paso a la vuelta 56 no es un
    titulo, y barrerlo llenaria el censo de ruido.
  PRINTS DE TITULO: los print que caen dentro de un bloque de banda (entre dos
    print de "=" * N o "-" * N separados por 5 posiciones o menos), mas el print
    que sigue inmediatamente a una banda. No se barre ningun otro print.

INDIRECCION DE UN PASO, medida y no supuesta: si el titulo trae %s y el %s se
alimenta de un NOMBRE ligado a un literal en el nivel del modulo (TRAMO = 5),
el numero SIGUE siendo tallado a mano, solo que un renglon mas arriba, y se
marca INDIRECTO con la linea de la asignacion. Si el %s se alimenta de un
atributo del espacio de argumentos o de una llamada, es VERDE.

DE SOLO LECTURA ENTERA: abre ficheros, los parsea e imprime. No escribe ni un
byte en ninguna parte.

USO:
  python scripts/loop/barrido_titulos_tallados.py
  python scripts/loop/barrido_titulos_tallados.py --vuelta 59
  python scripts/loop/barrido_titulos_tallados.py --raiz scripts/loop --todo

Sin --todo imprime los ROJO y los AMBAR uno a uno y el CENSO agrupado; con
--todo imprime tambien la ficha de cada CENSO. La cuenta de ficheros barridos,
verdes y con hallazgo va SIEMPRE, para que el barrido no pueda publicar un cero
sin decir sobre cuantos.

SALIDA: exit 1 si hay ROJO o AMBAR; exit 0 si solo hay CENSO o nada.
"""
import argparse
import ast
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Los sitios donde viven los instrumentos del bucle. El encargo pide
# scripts/loop/*.py COMO MINIMO; los otros tres entran porque el bucle los corre
# con la misma frecuencia y la especie no distingue de carpeta.
RAICES = ["scripts/loop", "scripts/plan", "scripts", "docs/loop"]

# Los argumentos que REPUNTAN el sujeto del instrumento. No entra --lote (elige
# un subconjunto del mismo sujeto) ni --simular ni --salida (no cambian lo
# medido). Cada especie tiene los suyos: --vuelta repunta la vuelta y no el
# tramo, y al reves.
REPUNTAN = {
    "tramo": ("--tramo", "--nomina", "--plan", "--fichero", "--entrada", "--corte", "--grafo", "--veredictos"),
    "vuelta": ("--vuelta",),
}

# El numero tallado, en el literal del titulo. El \s+ cruza el salto de linea a
# proposito: en las cabeceras el numero cae partido ("PARA EL TRAMO\n4 DE").
RE_TALLA = re.compile(r"(?i)\b(tramo|vuelta)\s+(\d+)\b")

# Lo que el fichero DECLARA de si mismo, por su nombre y por las rutas fijas que
# lee. De aqui sale el AMBAR: el titulo contra lo que el propio fichero dice.
DECLARAN = [
    (re.compile(r"(?i)vuelta(\d+)"), [("vuelta", 1)]),
    # LA FORMA CORTA, que la primera corrida de este barrido se dejaba fuera y
    # le costo cuatro AMBAR falsos: _v40_patch_costuras.py y auditor_v52_*.py
    # SI declaran su vuelta, solo que abreviada. Medido, no supuesto.
    (re.compile(r"(?i)(?:^|_)v(\d+)(?:_|$)"), [("vuelta", 1)]),
    (re.compile(r"(?i)tramo(\d+)_v(\d+)"), [("tramo", 1), ("vuelta", 2)]),
    (re.compile(r"(?i)\btramo(\d+)\b"), [("tramo", 1)]),
    (re.compile(r"(?i)\b(?:PLAN|SALIDA|RECOMPUTO)_V(\d+)"), [("vuelta", 1)]),
]


# EL ROTULO DEL TITULO, la via de la vuelta 58 (ROTULO puesto=... vigente=...)
# traida a esta especie. Una linea, clave=valor, y el valor puede ir entre
# comillas cuando lleva espacios.
RE_ROTULO = re.compile(r"ROTULO\s+titulo\s+(.+)$")
RE_CAMPO = re.compile(r"(\w+)=(\"[^\"]*\"|'[^']*'|\S+)")


# LOS DOS FICHEROS QUE HABLAN LA GRAMATICA DEL ROTULO NO SE BARREN POR ROTULOS, y
# los dos motivos estan MEDIDOS, no supuestos:
#   1. este mismo barrido lleva la gramatica escrita en su docstring con dos
#      ejemplos, y la primera corrida del cotejo los leyo como rotulos de verdad y
#      publico DOS huerfanos ROJO que no existen;
#   2. scripts/loop/triage_ambar_titulos.py ARMA las lineas de rotulo, asi que al
#      vaciarlas se le vaciaron dos lineas de codigo y el fichero salio ILEGIBLE
#      ("unmatched ')'", linea 198) en la corrida que siguio al triage.
# Es la piedra que _v50_contraste_contar_ld_v49 ya dejo escrita: un instrumento que
# se lee a si mismo se da la razon solo. LA EXCEPCION ES DE ROTULOS Y DE NADA MAS:
# los dos ficheros se barren enteros por sus titulos, como todos los demas.
QUE_HABLAN_LA_GRAMATICA = (
    os.path.join("scripts", "loop", "barrido_titulos_tallados.py"),
    os.path.join("scripts", "loop", "triage_ambar_titulos.py"),
)


def habla_la_gramatica(ruta_rel):
    normal = ruta_rel.replace("/", os.sep)
    return any(normal.endswith(x) for x in QUE_HABLAN_LA_GRAMATICA)


def rotulos_del_fichero(fuente, ruta_rel=""):
    """Los ROTULO del fichero, en orden, con su numero de linea."""
    if habla_la_gramatica(ruta_rel):
        return []
    out = []
    for i, linea in enumerate(fuente.splitlines(), 1):
        m = RE_ROTULO.search(linea)
        if not m:
            continue
        campos = {}
        for k, v in RE_CAMPO.findall(m.group(1)):
            campos[k] = v[1:-1] if v[:1] in ("\"", "'") else v
        campos["_linea"] = i
        campos["_casado"] = False
        out.append(campos)
    return out


def sin_rotulos(fuente):
    """El texto del fichero con sus lineas de rotulo EN BLANCO. Se mide sobre esto
    para que un rotulo no se declare a si mismo ni mueva la clase de los otros
    numeros del fichero.

    SE VACIAN, NO SE QUITAN, y la diferencia no es de estilo: quitarlas correria
    hacia arriba el numero de linea de todo lo que venga despues, y el barrido
    publica la linea de cada print. Un rotulo puesto encima de un print habria
    movido la linea que el propio barrido cita."""
    return chr(10).join("" if RE_ROTULO.search(l) else l for l in fuente.splitlines())


def parte_sujeto(valor):
    """'tramo:2' o 'vuelta:40' partido en (especie, numero); (None, None) si no."""
    if not valor or ":" not in valor:
        return None, None
    especie, _, numero = valor.partition(":")
    especie = especie.strip().lower()
    if especie not in ("tramo", "vuelta") or not numero.strip().isdigit():
        return None, None
    return especie, int(numero.strip())


def cotejar_rotulo(rot, hallazgo, fuente):
    """Devuelve (clase, motivo) para un AMBAR que tiene rotulo. La guarda prefiere
    ROJO a callar: si el rotulo no se puede comprobar, no absuelve."""
    especie_rot = (rot.get("especie") or "").upper()
    if especie_rot == "SELLO_FIJO":
        e, n = parte_sujeto(rot.get("sujeto"))
        if e is None:
            return "ROJO", "el rotulo de la linea %d no declara un sujeto legible (sujeto=tramo:N)" % rot["_linea"]
        if e != hallazgo["especie"] or n != hallazgo["numero"]:
            return "ROJO", ("el rotulo de la linea %d declara sujeto %s %d y el titulo dice %s %d"
                            % (rot["_linea"], e, n, hallazgo["especie"], hallazgo["numero"]))
        op = repunta(fuente, hallazgo["especie"])
        if op:
            return "ROJO", ("el rotulo de la linea %d declara SELLO_FIJO pero el fichero recibe el "
                            "sujeto por %s: un instrumento repuntable no se sella" % (rot["_linea"], op))
        return "ROTULADO", ("SELLO_FIJO cotejado: el fichero declara %s %d como su sujeto y no recibe "
                            "esa especie por argumento (rotulo de la linea %d, corte %s)"
                            % (e, n, rot["_linea"], rot.get("corte", "sin corte")))
    if especie_rot == "PROCEDENCIA":
        e, n = parte_sujeto(rot.get("cita"))
        if e is None:
            return "ROJO", "el rotulo de la linea %d no declara una cita legible (cita=vuelta:N)" % rot["_linea"]
        if e != hallazgo["especie"] or n != hallazgo["numero"]:
            return "ROJO", ("el rotulo de la linea %d cita %s %d y el titulo dice %s %d"
                            % (rot["_linea"], e, n, hallazgo["especie"], hallazgo["numero"]))
        ruta = rot.get("fuente") or ""
        prueba = rot.get("prueba") or ""
        abs_ruta = os.path.join(RAIZ, ruta.replace("/", os.sep))
        if not ruta or not os.path.exists(abs_ruta):
            return "ROJO", ("el rotulo de la linea %d nombra la fuente %r y esa ruta NO EXISTE"
                            % (rot["_linea"], ruta))
        if not prueba:
            return "ROJO", "el rotulo de la linea %d no trae literal de prueba" % rot["_linea"]
        try:
            texto = io.open(abs_ruta, encoding="utf-8", errors="replace").read()
        except OSError as e2:
            return "ROJO", "el rotulo de la linea %d no pudo leer %s (%s)" % (rot["_linea"], ruta, e2)
        if prueba not in texto:
            return "ROJO", ("el rotulo de la linea %d dice que %s contiene %r y HOY no lo contiene"
                            % (rot["_linea"], ruta, prueba))
        return "ROTULADO", ("PROCEDENCIA cotejada: %s %d nombra un ancestro que existe (%s contiene %r; "
                            "rotulo de la linea %d, corte %s)"
                            % (e, n, ruta, prueba, rot["_linea"], rot.get("corte", "sin corte")))
    return "ROJO", ("el rotulo de la linea %d declara la especie %r, que este barrido no coteja"
                    % (rot["_linea"], rot.get("especie")))


def es_banda(nodo):
    """print("=" * 78) y sus parientes: la banda que abre y cierra el titulo."""
    if len(nodo.args) != 1 or nodo.keywords:
        return False
    a = nodo.args[0]
    if isinstance(a, ast.BinOp) and isinstance(a.op, ast.Mult):
        for lado in (a.left, a.right):
            if isinstance(lado, ast.Constant) and isinstance(lado.value, str):
                if lado.value and set(lado.value) <= set("=-*_ "):
                    return True
        return False
    if isinstance(a, ast.Constant) and isinstance(a.value, str):
        v = a.value.strip()
        return len(v) >= 20 and set(v) <= set("=-*_")
    return False


def prints_del_modulo(arbol):
    """Los print del fichero EN ORDEN DE APARICION, con si son banda o no."""
    fuera = []
    for nodo in ast.walk(arbol):
        if isinstance(nodo, ast.Call) and isinstance(nodo.func, ast.Name) and nodo.func.id == "print":
            fuera.append(nodo)
    fuera.sort(key=lambda n: (n.lineno, n.col_offset))
    return [(n, es_banda(n)) for n in fuera]


def prints_de_titulo(secuencia):
    """Los que caen ESTRICTAMENTE ENTRE dos bandas separadas por 5 posiciones o
    menos, que es la figura banda/titulo/[subtitulo]/banda de la casa.

    NO vale "el print que sigue a una banda": esa regla, que la primera corrida
    de este barrido llevaba, mete el cuerpo del informe que empieza DESPUES de
    la banda de cierre, y me dio tres falsos (vuelta54_ejemplares_estrella.py
    lineas 80 y 81, vuelta19_fase2.py linea 50, que son lineas de leyenda y no
    titulos). Los dos ejemplares de calibracion siguen cazandose con la regla
    estricta: el del cuadro de varas tiene las bandas a distancia 2 y el del
    abridor a distancia 3."""
    titulo = []
    bandas = [i for i, (_, b) in enumerate(secuencia) if b]
    dentro = set()
    for k in range(len(bandas) - 1):
        i, j = bandas[k], bandas[k + 1]
        if j - i > 4:
            continue
        # EL print() VACIO CIERRA EL TITULO, y es la figura de la casa: banda,
        # titulo, banda, VACIO, cuerpo. Sin esta condicion, dos bloques de banda
        # cercanos se tragan el cuerpo que hay en medio y salen falsos: es lo
        # que me paso con vuelta54_ejemplares_estrella.py lineas 80 y 81, que
        # son leyenda del informe y no titulo.
        if any(not secuencia[m][0].args for m in range(i + 1, j)):
            continue
        dentro.update(range(i + 1, j))
    for i in sorted(dentro):
        nodo, banda = secuencia[i]
        if not banda:
            titulo.append(nodo)
    return titulo


def constantes_del_modulo(arbol):
    """NOMBRE = <literal> en el nivel del modulo. Es la indireccion de un paso."""
    out = {}
    for nodo in arbol.body:
        if isinstance(nodo, ast.Assign) and isinstance(nodo.value, ast.Constant):
            if isinstance(nodo.value.value, (int, str)):
                for destino in nodo.targets:
                    if isinstance(destino, ast.Name):
                        out[destino.id] = (nodo.value.value, nodo.lineno)
    return out


def literales(nodo):
    """Todas las cadenas literales que cuelgan de este print."""
    out = []
    for x in ast.walk(nodo):
        if isinstance(x, ast.Constant) and isinstance(x.value, str):
            out.append(x.value)
    return out


def nombres_alimentadores(nodo):
    """Los NOMBRES que alimentan los %s de este print. Un atributo (a.vuelta) o
    una llamada no son nombre: esos son la via verde y no se devuelven."""
    out = []
    for x in ast.walk(nodo):
        if isinstance(x, ast.BinOp) and isinstance(x.op, ast.Mod):
            for y in ast.walk(x.right):
                if isinstance(y, ast.Name):
                    out.append(y.id)
    return out


def declarados(nombre_rel, fuente):
    """Lo que el fichero declara de si mismo: numeros por especie, del nombre y
    de las rutas fijas que su codigo cita."""
    out = {"tramo": set(), "vuelta": set()}
    campos = [os.path.basename(nombre_rel)]
    campos += re.findall(r"[A-Za-z0-9_]*(?:TRAMO|PLAN|SALIDA|RECOMPUTO)[A-Za-z0-9_]*", fuente)
    for campo in campos:
        for rx, pares in DECLARAN:
            for m in rx.finditer(campo):
                for especie, grupo in pares:
                    out[especie].add(int(m.group(grupo)))
    return out


def repunta(fuente, especie):
    """El instrumento recibe ESA especie por argumento?"""
    for opcion in REPUNTAN[especie]:
        if ('add_argument("%s"' % opcion) in fuente or ("add_argument('%s'" % opcion) in fuente:
            return opcion
    return None


def clasificar(especie, numero, fuente, dec):
    op = repunta(fuente, especie)
    if op:
        return "ROJO", "recibe el sujeto por %s y el titulo no se entera" % op
    vistos = dec[especie]
    if vistos and numero not in vistos:
        return "AMBAR", ("el fichero declara %s %s y el titulo dice %d. EL BARRIDO NO DECIDE "
                         "cual de las dos cosas es: un numero que no calza o NOMBRA UN ANCESTRO "
                         "a proposito (procedencia, y entonces no envejece) o ES UNA CITA "
                         "ENVEJECIDA. Eso lo separa el ojo, no la maquina" % (
                             especie, "/".join(str(x) for x in sorted(vistos)), numero))
    if not vistos:
        return "AMBAR", ("nada en el fichero declara un %s: el numero no tiene con que cotejarse, "
                         "asi que ni se confirma ni se desmiente por maquina" % especie)
    return "CENSO", "calza con el %s %d que el fichero declara y no hay argumento que lo repunte" % (
        especie, sorted(vistos)[0])


def barrer(ruta_abs, ruta_rel):
    crudo = io.open(ruta_abs, encoding="utf-8").read()
    # LOS ROTULOS SE APARTAN ANTES DE MEDIR: un rotulo no declara nada del fichero
    # ni cambia la clase de los demas numeros. Se leen del crudo y se miden aparte.
    rotulos = rotulos_del_fichero(crudo, ruta_rel)
    fuente = crudo if habla_la_gramatica(ruta_rel) else sin_rotulos(crudo)
    try:
        arbol = ast.parse(fuente)
    except SyntaxError as e:
        return [{"clase": "ILEGIBLE", "linea": e.lineno or 0, "sede": "el fichero",
                 "texto": str(e), "especie": "", "numero": 0, "motivo": "no parsea"}]
    dec = declarados(ruta_rel, fuente)
    consts = constantes_del_modulo(arbol)
    hallazgos = []

    doc = ast.get_docstring(arbol) or ""
    cabecera = doc.split("\n\n")[0] if doc else ""
    for m in RE_TALLA.finditer(cabecera):
        especie, numero = m.group(1).lower(), int(m.group(2))
        clase, motivo = clasificar(especie, numero, fuente, dec)
        hallazgos.append({"clase": clase, "linea": 1, "sede": "CABECERA",
                          "texto": " ".join(m.group(0).split()), "especie": especie,
                          "numero": numero, "motivo": motivo})

    for nodo in prints_de_titulo(prints_del_modulo(arbol)):
        for cadena in literales(nodo):
            for m in RE_TALLA.finditer(cadena):
                especie, numero = m.group(1).lower(), int(m.group(2))
                clase, motivo = clasificar(especie, numero, fuente, dec)
                hallazgos.append({"clase": clase, "linea": nodo.lineno, "sede": "PRINT",
                                  "texto": " ".join(m.group(0).split()), "especie": especie,
                                  "numero": numero, "motivo": motivo})
        for nombre in nombres_alimentadores(nodo):
            if nombre not in consts:
                continue
            valor, linea_const = consts[nombre]
            especie = "tramo" if re.match(r"(?i)^tramo", nombre) else (
                "vuelta" if re.match(r"(?i)^vuelta", nombre) else None)
            if especie is None or not isinstance(valor, int):
                continue
            clase, motivo = clasificar(especie, valor, fuente, dec)
            hallazgos.append({"clase": clase, "linea": nodo.lineno, "sede": "PRINT INDIRECTO",
                              "texto": "%s = %d (linea %d)" % (nombre, valor, linea_const),
                              "especie": especie, "numero": valor,
                              "motivo": motivo + "; el numero es literal un renglon mas arriba"})

    # EL COTEJO DE LOS ROTULOS, al final y solo sobre los AMBAR: un rotulo no
    # puede tocar un ROJO ni un CENSO, solo triar un AMBAR que ya salio.
    for h in hallazgos:
        if h["clase"] != "AMBAR":
            continue
        for rot in rotulos:
            e_rot, n_rot = parte_sujeto(rot.get("sujeto") or rot.get("cita"))
            if e_rot != h["especie"] or n_rot != h["numero"]:
                continue
            rot["_casado"] = True
            h["clase"], h["motivo"] = cotejar_rotulo(rot, h, fuente)
            break
    for rot in rotulos:
        if rot["_casado"]:
            continue
        hallazgos.append({"clase": "ROJO", "linea": rot["_linea"], "sede": "ROTULO HUERFANO",
                          "texto": "especie=%s sujeto/cita=%s" % (rot.get("especie"),
                                                                 rot.get("sujeto") or rot.get("cita")),
                          "especie": "", "numero": 0,
                          "motivo": "el rotulo no casa con ningun AMBAR vivo de este fichero: o el "
                                    "titulo que cubria ya se corrigio, o el rotulo esta mal escrito"})
    return hallazgos


def ficheros(raices):
    out = []
    for r in raices:
        base = os.path.join(RAIZ, r.replace("/", os.sep))
        if not os.path.isdir(base):
            continue
        for nombre in sorted(os.listdir(base)):
            if not nombre.endswith(".py"):
                continue
            rel = (r + "/" + nombre)
            if r == "docs/loop" and not nombre.startswith("_auditor"):
                continue
            out.append((os.path.join(base, nombre), rel))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", action="append", default=None,
                    help="carpeta a barrer, repetible. Por defecto las cuatro del bucle.")
    ap.add_argument("--vuelta", type=int, default=None,
                    help="solo para el titulo de esta salida; no cambia nada de lo medido")
    ap.add_argument("--todo", action="store_true", help="imprime tambien la ficha de cada CENSO")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    raices = a.raiz or RAICES
    lista = ficheros(raices)

    print("=" * 100)
    print("BARRIDO DE TITULOS TALLADOS A MANO EN LOS INSTRUMENTOS DEL BUCLE%s"
          % ("" if a.vuelta is None else " (vuelta %d)" % a.vuelta))
    print("  carpetas barridas: %s" % ", ".join(raices))
    print("  ficheros barridos: %d" % len(lista))
    print("=" * 100)
    print()

    todos = []
    con_hallazgo = 0
    for ruta_abs, rel in lista:
        h = barrer(ruta_abs, rel)
        if h:
            con_hallazgo += 1
        for x in h:
            x["fichero"] = rel
            todos.append(x)

    orden = {"ILEGIBLE": 0, "ROJO": 1, "AMBAR": 2, "ROTULADO": 3, "CENSO": 4}
    for clase in ("ILEGIBLE", "ROJO", "AMBAR"):
        grupo = [x for x in todos if x["clase"] == clase]
        print("--- %s: %d ---" % (clase, len(grupo)))
        if not grupo:
            print("    ninguno")
        for x in sorted(grupo, key=lambda y: (y["fichero"], y["linea"])):
            print("    %s:%d  [%s]  %r" % (x["fichero"], x["linea"], x["sede"], x["texto"]))
            print("        %s" % x["motivo"])
        print()

    rotulados = [x for x in todos if x["clase"] == "ROTULADO"]
    print("--- ROTULADO (AMBAR YA TRIADO, con el rotulo cotejado en esta corrida): %d en %d ficheros ---"
          % (len(rotulados), len({x["fichero"] for x in rotulados})))
    if not rotulados:
        print("    ninguno")
    for x in sorted(rotulados, key=lambda y: (y["fichero"], y["linea"])):
        print("    %s:%d  [%s]  %r" % (x["fichero"], x["linea"], x["sede"], x["texto"]))
        print("        %s" % x["motivo"])
    print()

    censo = [x for x in todos if x["clase"] == "CENSO"]
    print("--- CENSO (SELLO FIJO), para las vueltas que los toquen: %d en %d ficheros ---"
          % (len(censo), len({x["fichero"] for x in censo})))
    if a.todo:
        for x in sorted(censo, key=lambda y: (y["fichero"], y["linea"])):
            print("    %s:%d  [%s]  %r" % (x["fichero"], x["linea"], x["sede"], x["texto"]))
    else:
        for fichero in sorted({x["fichero"] for x in censo}):
            marcas = [x for x in censo if x["fichero"] == fichero]
            print("    %-52s %s" % (fichero, ", ".join(
                "%s %d (linea %d)" % (m["especie"], m["numero"], m["linea"])
                for m in sorted(marcas, key=lambda y: y["linea"]))))
    print()

    cuenta = {c: len([x for x in todos if x["clase"] == c]) for c in orden}
    print("RESUMEN: %d ficheros barridos, %d con hallazgo, %d limpios | ROJO %d, AMBAR %d, ROTULADO %d, CENSO %d, ILEGIBLE %d"
          % (len(lista), con_hallazgo, len(lista) - con_hallazgo,
             cuenta["ROJO"], cuenta["AMBAR"], cuenta["ROTULADO"], cuenta["CENSO"], cuenta["ILEGIBLE"]))
    print("FIN")
    return 1 if (cuenta["ROJO"] or cuenta["AMBAR"] or cuenta["ILEGIBLE"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
