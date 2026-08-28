# -*- coding: utf-8 -*-
r"""verificar_vuelco_de_veredicto.py . LA GUARDA DEL VUELCO DE VEREDICTO
(TAREA 2 de la vuelta 109, acta de la vuelta 108, seccion "EL BARRIDO DEL
TRAMO 2 VUELCA DOS VEREDICTOS REGISTRADOS Y NO DECLARA NINGUNO"). Nombre
estable, SIN numero de vuelta (como verificar_cobertura_bolsa_tres_vias.py
y contar_cierre_efectivo.py): no se clona cada vuelta.

POR QUE NACE. El acta de la vuelta 108 cruzo a mano los seis ficheros de
veredicto puesto a puesto y hallo que el 87 y el 91 cambiaron de SATELITE
(vuelta 105, docs/loop/SALIDA_V105_TAREA4_3_RE_BARRIDO.txt) a OBJETO
(vuelta 108, docs/loop/SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md) sin que
ninguna fila lo dijera, ni siquiera marcada DISCUTIBLE. Los otros tres
vuelcos de la historia (109, 123, 145) SI se declararon, dos de ellos por
el propio ejecutor, dentro de la fila o de la linea de resumen del fichero
que los revierte. La caida fue de HABITO, no de instrumento: nadie habia
escrito la guarda que lo exige. Esta es esa guarda (adjudicacion por
extension de EJECUTOR.md, "LA TABLA SE CUENTA DE SU FICHERO": si el habito
de declarar el vuelco se puede caer, la declaracion la tiene que exigir un
instrumento, no la memoria del que escribe la fila).

QUE HACE. (1) Recorre los MISMOS seis ficheros que
verificar_cobertura_bolsa_tres_vias.FICHEROS_VEREDICTO (se IMPORTA esa
constante, no se vuelve a teclear: una lista que se copia es una lista que
se desincroniza). (2) De cada fichero extrae, para CADA puesto, el
veredicto (OBJETO / SATELITE / NO_OBJETO) Y el texto de su fila o bloque
(para buscar la declaracion despues). (3) Para cada puesto que aparece en
DOS O MAS ficheros, si el veredicto no es el mismo en todos, es un VUELCO:
se reporta el fichero y veredicto del lado MAS VIEJO contra el lado MAS
NUEVO (orden cronologico = el orden de FICHEROS_VEREDICTO, que ya va de
la vuelta 105 a la 108). (4) Por cada vuelco, comprueba si el fichero MAS
NUEVO lo DECLARA.

COMO SE RECONOCE LA DECLARACION (leido de los tres vuelcos reales que SI
la traen, antes de decidir el patron, como pide el encargo):
  - 123 (docs/loop/SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md, fila 24):
    "OBJETO (ya barrido SATELITE en la vuelta 106 y SOSTENIDO tras lectura
    entera, ...)" -- el veredicto VIEJO (SATELITE) Y la vuelta vieja (106)
    viven DENTRO de la propia fila del puesto.
  - 145 (mismo fichero, fila 31): "OBJETO (...; revertido a RESUELTA por
    TAREA 3 de esta vuelta, correccion_v107)" -- no repite la palabra
    SATELITE, pero "revertido" y "correccion_v107" son la marca de que
    el puesto tenia una direccion o veredicto previo que esta fila cambia.
  - 109 (mismo fichero, fila 19): la fila SOLO dice "va a lectura entera,
    docs/loop/SALIDA_V107_TAREA4_1_2_LECTURA_ENTERA_109.md", sin nombrar
    ni el veredicto viejo (OBJETO) ni la vuelta (106). La declaracion vive
    DOS LINEAS MAS ABAJO, en el resumen del mismo fichero (linea 36):
    "SATELITE: 1 (109, nuevo hallazgo de esta vuelta)". Restringir la
    busqueda a la fila exacta del puesto habria dejado al 109 en ROJO
    pese a estar declarado: por eso la busqueda cubre TODA LINEA DEL
    FICHERO que mencione el puesto como palabra suelta (\b<puesto>\b), no
    solo su fila de tabla o bloque.

EL PATRON ACEPTADO, por tanto: el vuelco esta DECLARADO si, entre TODAS las
lineas del fichero mas nuevo que mencionan el puesto como palabra suelta,
alguna contiene (a) el veredicto VIEJO como palabra suelta, o (b) "vuelta
<N>" con N la vuelta del fichero mas viejo, o (c) una de las frases de
declaracion que los tres casos reales ya usan: "nuevo hallazgo", "ya
barrido", "sostenido", "revertido", "correccion_v". Ninguna de estas frases
aparece en ningun lugar del fichero de la vuelta 108 (TRAMO2) que mencione
el 87 o el 91 (comprobado a mano antes de escribir esta lista): las dos
filas son SOLO su propia razon gramatical, sin rastro de que el puesto ya
tuviera otro veredicto. Vuelco declarado: pasa. Vuelco mudo: ROJO EXIT 1
nombrando el puesto.

USO:
  python scripts/loop/verificar_vuelco_de_veredicto.py

CASO POSITIVO (vuelta 109, docs/loop/SALIDA_V109_TAREA2_3_CASO_POSITIVO.txt):
CINCO vuelcos (87, 91, 109, 123, 145); 109, 123 y 145 DECLARADOS; ROJO EXIT 1
nombrando 87 y 91.

CASO ROJO POR MUTACION (vuelta 109,
docs/loop/SALIDA_V109_TAREA2_4_CASO_ROJO_MUTACION.txt): sobre una COPIA de
docs/loop/SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md con la frase "ya barrido
SATELITE en la vuelta 106 y SOSTENIDO tras lectura entera" borrada de la
fila del 123 (dejando solo la razon gramatical), puesta EN EL LUGAR del
fichero real vía `verificar(overrides=...)`: el 123 tiene que pasar de
DECLARADO a MUDO. Si sigue DECLARADO con la frase quitada, el instrumento
no esta leyendo la declaracion de verdad, esta adivinando.

--- LA GUARDA APRENDE A VER EL VOLTEO EN SU PROPIO SITIO (TAREA 2, vuelta
110, acta de la vuelta 109, "LA GUARDA QUE TE ENCARGUE NO VE EL CASO QUE
LA HIZO NACER") ---

POR QUE NACE. El diseno de la vuelta 109 solo cruzaba los seis ficheros
ENTRE SI (primer vs ultimo puesto que aparece en dos o mas ficheros de
HOY). El 87 volteo de OBJETO (nacido en el commit cd00fef8, vuelta 108) a
SATELITE (commit b31f1857, vuelta 109), LOS DOS DENTRO DEL MISMO FICHERO
docs/loop/SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md: como el 87 tambien
aparece en SALIDA_V105_TAREA4_3_RE_BARRIDO.txt con SATELITE, el cruce
entre ficheros de HOY ve SATELITE (105) contra SATELITE (108, hoy) -- IGUAL
-- y el volteo intermedio desaparece sin dejar rastro. La memoria de que
paso por OBJETO vive solo en la prosa aditiva de la fila, que ningun
instrumento leia.

QUE HACE, DE MAS. `vuelcos_en_sitio()` lee, para cada uno de los seis
ficheros de FICHEROS_VEREDICTO, su HISTORIA EN GIT completa (`git log
--format=%H --reverse -- <ruta>`, del commit mas viejo al mas nuevo) y el
contenido de cada commit (`git show <commit>:<ruta>`). Para cada puesto que
el fichero trae HOY, compara la cadena [primer commit que lo trae, ...,
commit mas nuevo, HOY] con la MISMA funcion que ya cruzaba ficheros
(`_detectar_y_declarar`, extraida del cruce para no duplicar la regla):
si el primero y el ultimo (HOY) difieren, VUELCO EN SITIO; si coinciden
pero algo intermedio no, OSCILACION (ver TAREA 4). La exigencia de
declaracion es la MISMA `esta_declarado()` de siempre: no hay un segundo
criterio para el sitio.

Ficheros con un solo commit en su historia (los otros cinco, hoy) no
pueden voltear en su sitio y se descartan sin costo.

CASO POSITIVO (vuelta 110, docs/loop/SALIDA_V110_TAREA2_3_CASO_POSITIVO.txt,
sobre el estado real de HOY, sin mutacion): el 87 aparece como VUELCO EN
SITIO, OBJETO (commit cd00fef8) -> SATELITE (HOY), DECLARADO (su fila trae
"volcado a OBJETO en esta misma fila" y "CORRECCION_V109"); los cuatro de
cruce (91, 109, 123, 145) siguen apareciendo y DECLARADOS. VERDE EXIT 0.

CASOS ROJOS POR MUTACION, LAS DOS COPIAS SON DEL AUDITOR (vuelta 109) y SE
QUEDAN COMMITEADAS (TAREA 2.6, vuelta 110):
docs/loop/_auditor_v109_mut/tramo2_sin_decl_87.md (la declaracion del
volteo del 87 borrada entera, solo la razon gramatical) tiene que dar ROJO
EXIT 1 nombrando el 87 (en sitio, MUDO);
docs/loop/_auditor_v109_mut/tramo2_sin_decl_91.md (la declaracion del 91
borrada) tiene que SEGUIR dando ROJO EXIT 1 nombrando el 91 (cruce, MUDO),
igual que antes de esta tarea: el remedio del sitio no apaga la deteccion
de cruce que ya funcionaba.
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
from verificar_cobertura_bolsa_tres_vias import FICHEROS_VEREDICTO  # noqa: E402

RE_BLOQUE_CABECERA = re.compile(r"^--- PUESTO (\d+) ---")
RE_BLOQUE_VEREDICTO = re.compile(r"VEREDICTO:\s*(OBJETO|SATELITE|NO_OBJETO)\b")
RE_TABLA_FILA = re.compile(r"^(\d+)\s*\|.*\|\s*(OBJETO|SATELITE|NO_OBJETO)\b")
RE_NOMBRE_VUELTA = re.compile(r"_V(\d+)_")

FRASES_DECLARACION = ["nuevo hallazgo", "ya barrido", "sostenido", "revertido", "correccion_v"]


def vuelta_de(nombre, fallos):
    m = RE_NOMBRE_VUELTA.search(nombre)
    if not m:
        fallos.append("%s: no se pudo leer el numero de vuelta de su nombre" % nombre)
        return None
    return int(m.group(1))


def extraer_bloque(texto):
    """puesto -> veredicto, para el formato 'bloque' (--- PUESTO N ---)."""
    out = {}
    puesto_actual = None
    for linea in texto.splitlines():
        m = RE_BLOQUE_CABECERA.match(linea)
        if m:
            puesto_actual = int(m.group(1))
            continue
        if linea.strip() == "":
            puesto_actual = None
            continue
        if puesto_actual is not None:
            mv = RE_BLOQUE_VEREDICTO.search(linea)
            if mv:
                out[puesto_actual] = mv.group(1)
                puesto_actual = None
    return out


def extraer_tabla(texto):
    """puesto -> veredicto, para el formato 'tabla' (N | ... | PALABRA)."""
    out = {}
    for linea in texto.splitlines():
        m = RE_TABLA_FILA.match(linea)
        if m:
            out[int(m.group(1))] = m.group(2)
    return out


def leer_ficheros(ficheros, overrides, fallos):
    """Devuelve lista de (nombre, vuelta, texto, {puesto: veredicto}), en el
    MISMO orden que `ficheros` (que ya va de la vuelta mas vieja a la mas
    nueva). `overrides` (nombre -> ruta alterna) es SOLO para la prueba de
    mutacion: nunca se usa en una corrida real."""
    salida = []
    for nombre, formato in ficheros:
        ruta = (overrides or {}).get(nombre) or os.path.join(LOOP, nombre)
        if not os.path.exists(ruta):
            fallos.append("no existe %s (declarado en FICHEROS_VEREDICTO)" % nombre)
            continue
        texto = io.open(ruta, encoding="utf-8").read()
        if formato == "bloque":
            veredictos = extraer_bloque(texto)
        elif formato == "tabla":
            veredictos = extraer_tabla(texto)
        else:
            fallos.append("%s: formato %r desconocido" % (nombre, formato))
            continue
        v = vuelta_de(nombre, fallos)
        salida.append((nombre, v, texto, veredictos))
    return salida


def lineas_que_mencionan(texto, puesto):
    patron = re.compile(r"\b%d\b" % puesto)
    return [linea for linea in texto.splitlines() if patron.search(linea)]


def esta_declarado(contexto, veredicto_viejo, vuelta_vieja):
    if re.search(r"\b%s\b" % veredicto_viejo, contexto):
        return True
    if vuelta_vieja is not None and re.search(r"vuelta\s+%d\b" % vuelta_vieja, contexto, re.IGNORECASE):
        return True
    bajo = contexto.lower()
    return any(frase in bajo for frase in FRASES_DECLARACION)


def _git(args, fallos, contexto):
    try:
        r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True, check=True)
        return r.stdout.decode("utf-8", errors="replace")
    except Exception as e:
        fallos.append("no se pudo correr git %s (%s): %s" % (" ".join(args), contexto, e))
        return None


def commits_de_fichero(nombre, fallos):
    """Commits que tocan docs/loop/<nombre>, del MAS VIEJO al MAS NUEVO
    (TAREA 2, vuelta 110: 'aprende a leer la HISTORIA EN GIT')."""
    rel = "docs/loop/%s" % nombre
    out = _git(["log", "--format=%H", "--reverse", "--", rel], fallos, "historia de %s" % nombre)
    if out is None:
        return []
    return [h for h in out.splitlines() if h.strip()]


def vuelta_de_commit(commit, fallos):
    """Vuelve la vuelta declarada en la PRIMERA linea del mensaje del commit
    ('VUELTA N, ...' o 'VUELTA N.'), igual patron que usan los mensajes de
    esta campana. None si no se puede leer: esta_declarado() ya sabe tratar
    una vuelta_vieja en None (solo deja de tener ese sub-criterio)."""
    out = _git(["log", "-1", "--format=%s", commit], fallos, "mensaje de %s" % commit[:8])
    if out is None:
        return None
    m = re.search(r"VUELTA\s+(\d+)", out, re.IGNORECASE)
    return int(m.group(1)) if m else None


def veredictos_de_commit(nombre, commit, formato, fallos):
    rel = "docs/loop/%s" % nombre
    try:
        r = subprocess.run(["git", "show", "%s:%s" % (commit, rel)], cwd=RAIZ,
                           capture_output=True, check=True)
        texto = r.stdout.decode("utf-8", errors="replace")
    except Exception as e:
        fallos.append("no se pudo leer %s en el commit %s: %s" % (nombre, commit[:8], e))
        return {}
    if formato == "bloque":
        return extraer_bloque(texto)
    elif formato == "tabla":
        return extraer_tabla(texto)
    fallos.append("%s: formato %r desconocido" % (nombre, formato))
    return {}


def _detectar_y_declarar(puesto, apariciones, texto_referencia, tipo):
    """Nucleo COMPARTIDO por el cruce entre ficheros y el volteo en sitio
    (TAREA 2, vuelta 110): una sola regla para las dos preguntas, como pide
    el encargo ('si el patron te sirve para el cruce, te sirve para el
    sitio'). `apariciones`: lista CRONOLOGICA de (etiqueta, vuelta_o_None,
    veredicto); la ULTIMA es siempre HOY. Devuelve un dict de vuelco o None.

    Si el primero y el ultimo COINCIDEN pero algo intermedio no, ya no se
    descarta en silencio (TAREA 4, vuelta 110: 'un caso que el codigo se
    salta sin decirlo es un caso que nadie sabe que existe'): se reporta
    como 'oscilacion', con la MISMA exigencia de declaracion."""
    if len(apariciones) < 2:
        return None
    vs = set(v for _, _, v in apariciones)
    if len(vs) < 2:
        return None
    nombre_viejo, vuelta_vieja, veredicto_viejo = apariciones[0]
    nombre_nuevo, vuelta_nueva, veredicto_nuevo = apariciones[-1]
    contexto = "\n".join(lineas_que_mencionan(texto_referencia, puesto))
    if veredicto_viejo == veredicto_nuevo:
        intermedio = next(((n, v, ver) for n, v, ver in apariciones[1:-1] if ver != veredicto_viejo), None)
        if intermedio is None:
            return None
        n_int, v_int, ver_int = intermedio
        declarado = esta_declarado(contexto, ver_int, v_int)
        return {
            "puesto": puesto, "tipo": "oscilacion",
            "nombre_viejo": n_int, "vuelta_vieja": v_int, "veredicto_viejo": ver_int,
            "nombre_nuevo": nombre_nuevo, "vuelta_nueva": vuelta_nueva, "veredicto_nuevo": veredicto_nuevo,
            "declarado": declarado,
        }
    declarado = esta_declarado(contexto, veredicto_viejo, vuelta_vieja)
    return {
        "puesto": puesto, "tipo": tipo,
        "nombre_viejo": nombre_viejo, "vuelta_vieja": vuelta_vieja, "veredicto_viejo": veredicto_viejo,
        "nombre_nuevo": nombre_nuevo, "vuelta_nueva": vuelta_nueva, "veredicto_nuevo": veredicto_nuevo,
        "declarado": declarado,
    }


def vuelcos_en_sitio(ficheros, lados, fallos):
    """TAREA 2 (vuelta 110): el volteo EN SU SITIO, dentro de un mismo
    fichero, entre su historia de commits y HOY. Ficheros con un solo
    commit no pueden voltear en su sitio: se descartan sin leer nada mas."""
    out = []
    lados_por_nombre = {n: (t, v) for n, _v, t, v in lados}
    for nombre, formato in ficheros:
        commits = commits_de_fichero(nombre, fallos)
        if len(commits) < 2:
            continue
        texto_hoy, veredictos_hoy = lados_por_nombre.get(nombre, (None, {}))
        if texto_hoy is None:
            continue
        apariciones_por_puesto = {}
        for commit in commits:
            v_commit = vuelta_de_commit(commit, fallos)
            for puesto, veredicto in veredictos_de_commit(nombre, commit, formato, fallos).items():
                apariciones_por_puesto.setdefault(puesto, []).append((commit[:8], v_commit, veredicto))
        for puesto, veredicto_hoy in veredictos_hoy.items():
            apariciones = list(apariciones_por_puesto.get(puesto, []))
            if not apariciones:
                continue
            apariciones.append((nombre, vuelta_de(nombre, fallos), veredicto_hoy))
            vuelco = _detectar_y_declarar(puesto, apariciones, texto_hoy, "en_sitio")
            if vuelco:
                out.append(vuelco)
    return out


def verificar(overrides=None):
    fallos = []
    lados = leer_ficheros(FICHEROS_VEREDICTO, overrides, fallos)
    if fallos:
        return fallos, None

    # historia[puesto] = [(nombre, vuelta, veredicto), ...] en orden cronologico
    historia = {}
    for nombre, vuelta, _texto, veredictos in lados:
        for puesto, veredicto in veredictos.items():
            historia.setdefault(puesto, []).append((nombre, vuelta, veredicto))

    vuelcos = []
    for puesto in sorted(historia):
        apariciones = historia[puesto]
        nombre_nuevo = apariciones[-1][0]
        texto_nuevo = next(t for n, _v, t, _vs in lados if n == nombre_nuevo)
        vuelco = _detectar_y_declarar(puesto, apariciones, texto_nuevo, "cruce")
        if vuelco:
            vuelcos.append(vuelco)

    vuelcos.extend(vuelcos_en_sitio(FICHEROS_VEREDICTO, lados, fallos))
    if fallos:
        return fallos, None

    vuelcos.sort(key=lambda v: (v["puesto"], 0 if v["tipo"] == "cruce" else 1))
    return fallos, vuelcos


def main():
    fallos, vuelcos = verificar()
    if fallos:
        print("ROJO, %d cosa(s) no cuadran, NO SE CUENTA NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("FICHEROS DE ENTRADA (declarados en FICHEROS_VEREDICTO, %d, reusada de "
          "verificar_cobertura_bolsa_tres_vias.py):" % len(FICHEROS_VEREDICTO))
    for nombre, formato in FICHEROS_VEREDICTO:
        print("   %s (%s)" % (nombre, formato))
    print()
    print("VUELCOS DE VEREDICTO HALLADOS: %d" % len(vuelcos))
    etiqueta_tipo = {"cruce": "CRUCE", "en_sitio": "EN SITIO", "oscilacion": "OSCILACION"}
    mudos = []
    for v in vuelcos:
        estado = "DECLARADO" if v["declarado"] else "MUDO"
        if v["tipo"] == "en_sitio":
            print("   %d [%s]: %s (%s, commit %s) -> %s (%s, HOY) -- %s"
                  % (v["puesto"], etiqueta_tipo[v["tipo"]], v["veredicto_viejo"], v["nombre_nuevo"],
                     v["nombre_viejo"], v["veredicto_nuevo"], v["nombre_nuevo"], estado))
        else:
            print("   %d [%s]: %s (%s, vuelta %s) -> %s (%s, vuelta %s) -- %s"
                  % (v["puesto"], etiqueta_tipo[v["tipo"]], v["veredicto_viejo"], v["nombre_viejo"], v["vuelta_vieja"],
                     v["veredicto_nuevo"], v["nombre_nuevo"], v["vuelta_nueva"], estado))
        if not v["declarado"]:
            mudos.append("%d[%s]" % (v["puesto"], v["tipo"]))

    if mudos:
        print("\nROJO: %d vuelco(s) MUDO(s), nombrados: %s"
              % (len(mudos), ", ".join(mudos)))
        return 1

    print("\nVERDE: todos los vuelcos hallados estan declarados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
