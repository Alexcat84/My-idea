# -*- coding: utf-8 -*-
r"""barrer_ausencia.py . EL INSTRUMENTO DEL BARRIDO EXHAUSTIVO (TAREA 2 de la
vuelta 146, la ESCALADA de `AUDITOR.md` 1.2 disparada por la racha de reporte
llegando a DOS, acta de la vuelta 145).

NOMBRE ESTABLE, SIN NUMERO DE VUELTA, como `verificar_apertura_sellada.py`,
`tallar_cabecera_reporte.py` y `verificar_mutaciones_viejas.py`: se corre igual
en toda vuelta y no se clona.

POR QUE NACE. `verificar_ausencias_del_reporte.py` (su hermana, la guarda)
exige que toda AFIRMACION DE AUSENCIA del reporte venga respaldada por un
BARRIDO EXHAUSTIVO COMPUTADO sellado en una salida. Una guarda que exige algo
que nadie sabe producir no es una guarda, es un muro: este instrumento es lo
que hace que la exigencia se pueda cumplir, y por eso nace en la misma tarea.

QUE ES UN BARRIDO EXHAUSTIVO, ESCRITO AQUI Y NO ADIVINADO. Un recorrido del
UNIVERSO ENTERO de donde la cosa podria estar, con su universo y su cardinal
publicados. Para ficheros del repositorio son DOS PIERNAS y las dos son
obligatorias:

  (1) POR NOMBRE, sobre `git ls-files` (el universo entero de lo versionado, no
      el arbol de trabajo: un fichero sin versionar no es del repositorio).
  (2) POR CONTENIDO, sobre ESE MISMO universo. Esta es la pierna que faltaba el
      dia de la caida: la vuelta 145 miro TRES RUTAS TECLEADAS A MANO y
      concluyo que la lista canonica de libros no existia. Existia, y se llama
      `docs/plan/OP_S_11_MAPEO_PROPUESTO.md`. Una busqueda por nombre NO PUEDE
      hallar un fichero que se llama por su operacion duena; una por contenido
      SI. Por eso la guarda hermana no acepta un barrido de una sola pierna.

EL SELLO QUE IMPRIME, y es el contrato que la guarda hermana lee (si se cambia
una de estas cinco lineas hay que cambiarlo en las dos, y por eso viven aqui
escritas y no adivinadas):

  BARRIDO EXHAUSTIVO
    PREGUNTA: <la ausencia que este barrido respalda, en una linea>
    UNIVERSO: <de donde sale el universo>
    CARDINAL: <n>
    POR CONTENIDO: <patron> | <n> ficheros con coincidencia
    VEREDICTO: HALLADO / NO HALLADO

`PREGUNTA:` es obligatoria a proposito: obliga al barrido a decir QUE ausencia
respalda, para que un reporte no pueda apoyar una ausencia en el barrido del
vecino sin que se vea.

LA FRONTERA, Y ES LA MISMA QUE LA DE LA GUARDA: este instrumento NO decide si
lo que se busca "deberia" existir ni si su ausencia es buena o mala. Recorre el
universo, dice lo que encuentra y sella. El VEREDICTO que imprime es un HECHO
MEDIDO (hay o no hay coincidencias), nunca un juicio.

USO:
  python scripts/loop/barrer_ausencia.py \
      --pregunta "existe una lista canonica de libros con sus alias" \
      --nombre "libros_canonicos|fuentes_canonicas|LIBROS_CANONICOS" \
      --contenido "grafia|canonica propuesta" \
      --candidato dataset/metadata/libros_canonicos.json

`--candidato` se puede repetir: son las rutas que alguien miraria a mano. NO
son el barrido; se imprimen APARTE, bajo su propio rotulo, justamente para que
se vea la diferencia entre mirar tres nombres y recorrer el universo.

--- LA SEXTA PIEZA DEL SELLO: LA VITALIDAD DE LOS PATRONES DE CONTENIDO
    (TAREA 2.b de la vuelta 147, la ESCALADA DE LA ESCALADA) ---

POR QUE NACE, Y ES LA CAIDA 4.2 DEL ACTA 146. La vuelta 146 corrio ESTE
instrumento para preguntar si el umbral de la cola tenia numero. El sello salio
con SUS CINCO PIEZAS COMPLETAS y la guarda hermana lo aprobo. Y la afirmacion
que respaldaba era FALSA: el umbral existe, se llama `UMBRAL_SEMANTICO = 0.78`
(y `UMBRAL_TITULO = 80`) en `scripts/intra_dominio.py`, un fichero QUE ESTABA
DENTRO DEL UNIVERSO BARRIDO. El barrido no lo vio porque su pierna POR CONTENIDO
era `UMBRAL_DE_LA_COLA|UMBRAL_COLA|umbral_de_la_cola`: TRES IDENTIFICADORES QUE
NADIE HABIA ESCRITO NUNCA, ni ahi ni en ningun otro sitio del repositorio.

EL AGUJERO, DICHO EN UNA LINEA: un sello que certifica una pierna por contenido
de nombres adivinados certifica EL METODO EXACTO QUE LA CORRECCION 23 PROHIBE,
un nivel mas abajo. La 23 mato "mirar tres rutas a mano"; esto es "buscar tres
palabras a mano", y la unica diferencia es que la segunda pasa por un
instrumento.

EL CRITERIO, ELEGIDO AQUI Y DECLARADO (`AUDITOR.md` dejaba la eleccion abierta y
fijaba solo lo que tiene que conseguir): SE PARTE EL PATRON DE CONTENIDO EN SUS
ALTERNATIVAS DE PRIMER NIVEL (los `|` que no estan dentro de parentesis ni de
clase de caracteres) Y SE CUENTA, PARA CADA UNA, EN CUANTOS FICHEROS DEL
UNIVERSO APARECE. Una alternativa con CERO apariciones EN TODO EL UNIVERSO es
una ALTERNATIVA MUERTA: nadie escribio nunca eso, en ninguna parte. El sello
publica la cuenta, alternativa por alternativa:

    VITALIDAD DE LOS PATRONES DE CONTENIDO: <vivas> de <total> alternativas
        aparecen en el universo

Y LA GUARDA HERMANA RECHAZA UN BARRIDO CUYAS ALTERNATIVAS DE CONTENIDO ESTEN
TODAS MUERTAS. El motivo, escrito: si CADA cadena que buscaste no aparece NI UNA
VEZ en el universo entero, tu barrido no puede distinguir "la cosa no existe" de
"adivine mal el nombre". No es que el resultado sea sospechoso: es que la
medicion NO TIENE PODER PARA RESPONDER LA PREGUNTA, y una medicion sin poder no
respalda una ausencia.

QUE PASA CON EL CASO BUENO, para que se vea que el criterio no es un muro: el
mismo barrido del umbral REHECHO con `umbral|similitud` como contenido tiene sus
DOS alternativas VIVAS y halla `scripts/intra_dominio.py`. La pierna que busca
EL CONCEPTO sobrevive; la que busca nombres inventados, no.

EL LIMITE, DICHO EN VOZ ALTA Y NO ESCONDIDO (`EJECUTOR.md` 8): esto NO prueba
que el patron sea el bueno. Un patron `umbral_de_la_cola|de` pasaria, porque
`de` esta vivo, y no habria buscado el concepto. Lo que el criterio consigue es
exactamente lo que se le pidio y ni un milimetro mas: QUE UN BARRIDO CUYA PIERNA
POR CONTENIDO SOLO BUSQUE IDENTIFICADORES QUE NO EXISTEN EN EL UNIVERSO NO PUEDA
RESPALDAR UNA AUSENCIA. Queda MARCADO COMO DISCUTIBLE en el reporte de la vuelta
147, no zanjado.

LA PARTICION DEL PATRON, con su limitacion escrita: `alternativas_de` corta por
`|` a profundidad cero de parentesis y fuera de `[...]`, respetando la barra
invertida. NO es un parser de expresiones regulares completo; para los patrones
que esta campana escribe (alternancias planas de palabras e identificadores) es
exacto, y para uno que no sepa partir devuelve el patron ENTERO como unica
alternativa, que es el lado seguro: un patron entero vivo pasa, y uno entero
muerto cae.
"""
import argparse
import io
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MARCA = "BARRIDO EXHAUSTIVO"
EXTENSIONES_DE_TEXTO = (".md", ".py", ".txt", ".json", ".jsonl", ".ts", ".tsx",
                        ".js", ".jsx", ".yml", ".yaml", ".css", ".html", ".sql")


def universo(prefijos=None, ref=None):
    """El universo entero de lo versionado en la rama actual. Se lee de git y
    no del arbol de trabajo (`EJECUTOR.md`, LA IDENTIDAD SE LEE DE GIT).

    `ref` (vuelta 147, TAREA 2.c) lee el universo DE ESE COMMIT en vez del de
    hoy. Nace de un falso verde medido: al juzgar el sello congelado del
    barrido del umbral de la vuelta 146 sobre el arbol de HOY, sus tres
    identificadores muertos salian VIVOS, porque el docstring que documenta la
    caida los escribe. UN SELLO SE JUZGA CONTRA EL UNIVERSO QUE DECLARO, EN EL
    COMMIT EN QUE SE SELLO; medirlo contra el arbol de hoy es la misma especie
    que la sonda contada como instalacion.

    `prefijos` ACOTA el universo por ruta, y SOLO se usa cuando la pregunta lo
    pide de verdad: "esta este control instalado EN EL CODIGO" tiene por
    universo el codigo, no el repositorio entero, y meter en el universo los
    ficheros de salida que citan el literal como SONDA daria coincidencias que
    no son instalaciones. EL RECORTE NO SE ESCONDE: se imprime en la linea
    `UNIVERSO:` del sello y el `CARDINAL:` es el del universo YA acotado, para
    que quien lea sepa exactamente sobre que se barrio."""
    if ref:
        orden = ["git", "ls-tree", "-r", "--name-only", ref]
    else:
        orden = ["git", "ls-files"]
    r = subprocess.run(orden, cwd=RAIZ, capture_output=True, text=True, check=True)
    rutas = [l for l in r.stdout.splitlines() if l.strip()]
    if prefijos:
        rutas = [x for x in rutas if any(x.startswith(p) for p in prefijos)]
    return rutas


def por_nombre(rutas, patron):
    rx = re.compile(patron, re.IGNORECASE)
    return [r for r in rutas if rx.search(os.path.basename(r))]


def contenidos(rutas, ref=None):
    """Genera (ruta, texto) de los ficheros de TEXTO del universo, del arbol de
    trabajo (`ref` None) o del arbol de un commit. Los ilegibles se devuelven
    con texto None: un fichero que no se pudo mirar NO es un fichero sin
    coincidencia (banco 9, fallar ruidoso).

    UN SOLO LECTOR PARA LAS DOS PIERNAS Y PARA LA VITALIDAD, y un solo motor de
    expresiones regulares (`re` de Python) en los tres sitios: si la vitalidad
    se midiera con `git grep` y la pierna con `re`, las dos podrian discrepar
    en silencio, que es la averia que el chequeo de gemelos vino a curar.

    Con `ref`, los blobs se sacan en UNA sola llamada a `git cat-file --batch`
    y no una por fichero."""
    candidatas = [r for r in rutas if r.lower().endswith(EXTENSIONES_DE_TEXTO)]
    if ref is None:
        for r in candidatas:
            ruta = os.path.join(RAIZ, r)
            if not os.path.exists(ruta):
                continue
            try:
                with io.open(ruta, encoding="utf-8") as f:
                    yield r, f.read()
            except (UnicodeDecodeError, OSError):
                yield r, None
        return

    peticion = "".join("%s:%s\n" % (ref, r) for r in candidatas)
    p = subprocess.Popen(["git", "cat-file", "--batch"], cwd=RAIZ,
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    salida, _ = p.communicate(peticion.encode("utf-8"))
    pos = 0
    for r in candidatas:
        fin = salida.find(b"\n", pos)
        if fin == -1:
            break
        cabecera = salida[pos:fin].decode("utf-8", "replace")
        pos = fin + 1
        partes = cabecera.split()
        if len(partes) < 3 or partes[1] != "blob":
            # 'missing' u otra cosa: el fichero no esta en ese arbol.
            continue
        tam = int(partes[2])
        crudo = salida[pos:pos + tam]
        pos += tam + 1
        try:
            yield r, crudo.decode("utf-8")
        except UnicodeDecodeError:
            yield r, None


def por_contenido(rutas, patron, ref=None):
    """Recorre el MISMO universo leyendo cada fichero de texto."""
    rx = re.compile(patron, re.IGNORECASE)
    aciertos, ilegibles = [], []
    for r, texto in contenidos(rutas, ref):
        if texto is None:
            ilegibles.append(r)
            continue
        if rx.search(texto):
            aciertos.append(r)
    return aciertos, ilegibles


# --- LA SEXTA PIEZA DEL SELLO (vuelta 147, TAREA 2.b). Contrato compartido con
# verificar_ausencias_del_reporte.py: si se cambia esta linea hay que cambiarla
# en las dos, y por eso el ROTULO vive aqui, escrito una sola vez, y la guarda
# lo importa de este modulo en vez de reteclearlo.
ROTULO_VITALIDAD = "VITALIDAD DE LOS PATRONES DE CONTENIDO"


def alternativas_de(patron):
    """Parte un patron de contenido en sus ALTERNATIVAS DE PRIMER NIVEL: los
    `|` que no estan dentro de parentesis ni de una clase `[...]`, respetando
    la barra invertida. Ver el docstring, LA PARTICION DEL PATRON: no es un
    parser completo de expresiones regulares, y ante cualquier cosa que no sepa
    partir devuelve el patron ENTERO como unica alternativa, que es el lado
    seguro."""
    piezas, actual = [], []
    hondura, en_clase, escapado = 0, False, False
    for ch in patron:
        if escapado:
            actual.append(ch)
            escapado = False
            continue
        if ch == "\\":
            actual.append(ch)
            escapado = True
            continue
        if en_clase:
            actual.append(ch)
            if ch == "]":
                en_clase = False
            continue
        if ch == "[":
            en_clase = True
            actual.append(ch)
            continue
        if ch == "(":
            hondura += 1
            actual.append(ch)
            continue
        if ch == ")":
            hondura -= 1
            actual.append(ch)
            continue
        if ch == "|" and hondura == 0:
            piezas.append("".join(actual))
            actual = []
            continue
        actual.append(ch)
    piezas.append("".join(actual))
    limpias = [p.strip() for p in piezas if p.strip()]
    if not limpias or hondura != 0 or en_clase or escapado:
        return [patron]
    return limpias


def vitalidad_de_contenido(rutas, patron, ref=None):
    """Para CADA alternativa de primer nivel del patron, en cuantos ficheros
    del universo aparece. Una alternativa con CERO es una ALTERNATIVA MUERTA:
    nadie escribio nunca eso en ninguna parte del universo, y un barrido cuyas
    alternativas esten TODAS muertas no puede distinguir "la cosa no existe" de
    "adivine mal el nombre".

    UNA SOLA PASADA sobre el universo, probando todas las alternativas por
    fichero: leer el universo una vez por alternativa multiplicaria el coste
    sin cambiar el resultado.

    Devuelve [(alternativa, n_ficheros), ...] en el orden del patron."""
    alts = alternativas_de(patron)
    compiladas = []
    for a in alts:
        try:
            compiladas.append((a, re.compile(a, re.IGNORECASE)))
        except re.error:
            # Una alternativa que no compila sola NO se cuenta como muerta a la
            # ligera: se marca con None y se publica aparte, porque "no se pudo
            # mirar" no es "no aparece" (banco 9, fallar ruidoso).
            compiladas.append((a, None))
    cuenta = dict((a, 0) for a in alts)
    rotas = set(a for a, rx in compiladas if rx is None)
    for _r, texto in contenidos(rutas, ref):
        if texto is None:
            continue
        for a, rx in compiladas:
            if rx is not None and rx.search(texto):
                cuenta[a] += 1
    return [(a, (None if a in rotas else cuenta[a])) for a in alts]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pregunta", required=True)
    ap.add_argument("--nombre", required=True, help="regex sobre el NOMBRE de fichero")
    ap.add_argument("--contenido", required=True, help="regex sobre el CONTENIDO")
    ap.add_argument("--candidato", action="append", default=[],
                    help="ruta que alguien miraria a mano; se imprime APARTE")
    ap.add_argument("--universo-prefijo", action="append", default=[], dest="prefijos",
                    help="acota el universo por prefijo de ruta; se declara en el sello")
    # LA SONDA NO ES UNA INSTALACION (misma especie que "la guarda que se
    # envenena sola" de verificar_apertura_sellada.py). Un barrido que busca el
    # literal de un control SE ENCUENTRA A SI MISMO en el instrumento que lo
    # sonda, y contarlo seria publicar como instalado un control que solo
    # existe dentro de la vara que pregunta por el. Las exclusiones NO se
    # esconden: se imprimen en el sello, una a una, con su motivo al lado en el
    # reporte que las use.
    ap.add_argument("--excluir", action="append", default=[],
                    help="ruta excluida del universo por ser SONDA y no instalacion; "
                         "se declara entera en el sello")
    a = ap.parse_args()

    rutas = [r for r in universo(a.prefijos) if r not in set(a.excluir)]
    nom = por_nombre(rutas, a.nombre)
    con, ilegibles = por_contenido(rutas, a.contenido)
    todos = sorted(set(nom) | set(con))

    print(MARCA)
    print("  PREGUNTA: %s" % a.pregunta)
    print("  UNIVERSO: git ls-files de la rama actual%s"
          % (" ACOTADO a %s" % ", ".join(a.prefijos) if a.prefijos
             else " (todo lo versionado, sin acotar)"))
    print("  CARDINAL: %d" % len(rutas))
    print("  EXCLUIDOS POR SER SONDA Y NO INSTALACION (declarados, no escondidos): %d"
          % len(a.excluir))
    for x in a.excluir:
        print("      %s" % x)
    print("  POR NOMBRE: %s | %d ficheros con coincidencia" % (a.nombre, len(nom)))
    print("  POR CONTENIDO: %s | %d ficheros con coincidencia" % (a.contenido, len(con)))
    # LA SEXTA PIEZA (vuelta 147, TAREA 2.b): la vitalidad, alternativa por
    # alternativa. Se imprime SIEMPRE, tambien cuando todas estan vivas, porque
    # un dato que solo aparece cuando hay problema no se puede auditar.
    vit = vitalidad_de_contenido(rutas, a.contenido)
    vivas = [x for x in vit if x[1] not in (None, 0)]
    print("  %s: %d de %d alternativas aparecen en el universo"
          % (ROTULO_VITALIDAD, len(vivas), len(vit)))
    for alt, n in vit:
        if n is None:
            estado = "NO COMPILA SOLA (no se pudo mirar, NO es una muerta)"
        elif n == 0:
            estado = "MUERTA: cero apariciones en todo el universo"
        else:
            estado = "viva"
        print("      %-46s -> %-6s %s"
              % (alt, "?" if n is None else str(n), estado))
    print("  NO DECODIFICABLES (mirados y no leidos, NO cuentan como sin coincidencia): %d"
          % len(ilegibles))
    for r in ilegibles[:20]:
        print("      %s" % r)
    print("  VEREDICTO: %s" % ("HALLADO" if todos else "NO HALLADO"))
    print("  LOS QUE COINCIDEN (union de las dos piernas): %d" % len(todos))
    for r in todos[:60]:
        marcas = []
        if r in nom:
            marcas.append("nombre")
        if r in con:
            marcas.append("contenido")
        print("      %s  [%s]" % (r, " y ".join(marcas)))
    if len(todos) > 60:
        print("      ... y %d mas" % (len(todos) - 60))

    if a.candidato:
        print("  RUTAS CANDIDATAS MIRADAS A MANO (NO SON EL BARRIDO, van aparte):")
        for c in a.candidato:
            print("      %s -> %s" % (c, "EXISTE" if c in set(rutas) else "NO EXISTE"))
    # LAS CIFRAS SE PUBLICAN EN FORMA CONTABLE (vuelta 146, 4.c). Sin estas
    # lineas `CIFRA`, un reporte que pegue el sello no puede cotejar sus
    # numeros con `verificar_cifras_del_reporte.py`, que para las unidades sin
    # convencion mecanica SOLO sabe leer una linea `CIFRA <etiqueta>: <n>
    # <unidad>`. Se anaden las DOS PIERNAS por separado porque son la pareja
    # que sostiene o tumba una afirmacion de ausencia: la de contenido en cero
    # es lo que respalda un NO HALLADO.
    print("CIFRA ficheros del universo: %d ficheros" % len(rutas))
    print("CIFRA ficheros que coinciden por nombre: %d ficheros" % len(nom))
    print("CIFRA ficheros que coinciden por contenido: %d ficheros" % len(con))
    print("CIFRA alternativas de contenido vivas: %d alternativas" % len(vivas))
    print("CIFRA alternativas de contenido en total: %d alternativas" % len(vit))
    print("CIFRA ficheros que coinciden: %d ficheros" % len(todos))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
