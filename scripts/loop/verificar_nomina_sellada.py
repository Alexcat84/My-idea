# -*- coding: utf-8 -*-
r"""verificar_nomina_sellada.py . LA GUARDA DE LA NOMINA DE LA ADUANA (TAREA
3.d de la vuelta 147). NOMBRE ESTABLE, SIN NUMERO DE VUELTA, como
`verificar_apertura_sellada.py`, `verificar_fuente_canonico.py` y
`verificar_ausencias_del_reporte.py`.

POR QUE NACE. Es el DISCUTIBLE 5 del reporte de la vuelta 146 convertido en
codigo, adjudicado A FAVOR CON RESERVA SERIA por el auditor (acta 146, 3.5). La
nomina `dataset/metadata/aduana_fuente_multiple.json` lleva dentro su propia
advertencia escrita, *"Re-sellar esta nomina es RE-ADJUDICAR. No se regenera
para hacer callar a Gate 0"*, Y ESO ERA UNA REGLA SIN GUARDA, o sea la misma
especie que la caida 4.2 de la casa del acta 145: una regla que se puede citar y
romper a la vez es prosa.

EL ATAQUE CONCRETO QUE ESTO IMPIDE, escrito para que se vea que no es abstracto.
Alguien anade manana un nodo vivo con DOS libros. Gate 0 cae, porque ese nodo no
esta en la nomina adjudicada. Bastaba con volver a correr
`scripts/loop/vuelta146_3b_sellar_nomina_aduana.py`: la nomina se regenera con
el nodo dentro, Gate 0 vuelve a verde, Y NADIE SE ENTERA, porque el `numstat` de
`dataset/` de una vuelta cualquiera trae cientos de filas y una mas no se ve. La
aduana quedaria abierta por el procedimiento exacto que existe para cerrarla.

EL CRITERIO, ELEGIDO AQUI Y DECLARADO. LA NOMINA NO PUEDE MOVERSE EN SILENCIO.
Se compara la nomina DEL ARBOL DE TRABAJO contra la nomina DE `HEAD`, y si
difieren en algo (una entrada que entra, una que sale, o una lista de
declaraciones que cambia), EL CAMBIO TIENE QUE ESTAR DECLARADO EN
`docs/loop/REPORTE.md`, y declarado significa DOS cosas a la vez:

  (1) la marca literal `RE-SELLADO DE LA NOMINA DE LA ADUANA`, que es la
      declaracion explicita de que la vuelta sabe lo que hizo; y
  (2) CADA `node_id` afectado, nombrado verbatim en el reporte, uno a uno.

Sin las dos, ROJO NOMBRANDO LO QUE CAMBIO Y NO SE DECLARO. Con las dos, VERDE:
la guarda NO impide re-sellar, impide re-sellar CALLANDO.

POR QUE EL SUJETO DE CONTRASTE ES `HEAD` Y NO EL COMMIT DE NACIMIENTO. Porque lo
que se vigila es el MOVIMIENTO, no la identidad con el origen: una nomina que
crece legitimamente a lo largo de vueltas, cada vez declarada, es correcta, y
anclarla a su nacimiento la volveria inmovible y obligaria a ensanchar la guarda
al primer cambio bueno. Anclada a `HEAD`, cada movimiento se declara EN LA
VUELTA QUE LO HACE, que es donde se puede auditar.

LA FRONTERA, PORQUE ES LO QUE MAS FACIL SE LEE DE MAS. ESTA GUARDA NO JUZGA SI
LA NOMINA NUEVA ES BUENA. No lee un nodo, no adjudica un reparto y no dice si un
segundo libro esta bien puesto: eso es lectura humana y esta guarda no la
sustituye. Lo unico que consigue es que RE-ADJUDICAR SEA UN ACTO VISIBLE. Y NO
SUSTITUYE A LA COMPROBACION POSICIONAL: aquella mide LOS NODOS contra la nomina,
y esta protege LA NOMINA contra la que aquella mide. Son dos unidades y por eso
son dos checks (CORRECCION 18).

FALLA RUIDOSO Y NUNCA EN SILENCIO (banco 9). Si `git` no responde, si `HEAD` no
trae el fichero, o si el reporte no se puede leer, ESO ES ROJO con su motivo
escrito, jamas un verde por no haber podido mirar.

DONDE CORRE. CABLEADA A GATE 0 (`scripts/run_phase1.py`, `step7_validate`), que
es el unico sitio donde "nada impide" se convierte en "algo lo impide". Es el
mismo cableado que la vuelta 146 hizo con `verificar_fuente_canonico.py` para el
control A2.4, y por la misma razon: una guarda que nadie corre es prosa.

--- CERRADA POR EL LADO DEL COMMIT (TAREA 2.1, vuelta 148) ---

POR QUE NACE. La caida 4.4.a del acta 147, que el auditor probo con su segunda
mutacion: ESTA GUARDA ERA CIEGA AL MOVIMIENTO QUE LLEGA YA COMMITEADO. Comparaba
el arbol de trabajo contra `HEAD`, asi que bastaba con COMMITEAR el re-sellado
para que los dos lados dijeran lo mismo y la guarda no viera nada. El ataque que
el docstring de arriba describe seguia abierto entero: se regenera la nomina, se
commitea, y a partir de ese instante no hay diferencia que mirar. Y el hook
tampoco lo cubre, porque solo corre las suites, no Gate 0.

EL SUJETO NUEVO, Y NO NECESITA QUE NADIE LE PASE EL NUMERO DE VUELTA. Ademas de
`HEAD`, se compara contra EL ANCLA DE LA VUELTA: el commit del acta mas reciente
de la rama (mensaje que empieza por "ACTA DE LA VUELTA N DEL AUDITOR" o "ACTA
DEL AUDITOR, VUELTA N", los dos patrones que ya usan
`verificar_apertura_sellada.py` y `tallar_cabecera_reporte.py`). TODO lo que hay
despues de ese commit es la vuelta en curso, asi que cualquier movimiento de la
nomina hecho DURANTE la vuelta queda a la vista, se haya commiteado o no.

LAS DOS COMPARACIONES SE QUEDAN, PORQUE CONTESTAN COSAS DISTINTAS: contra el
ANCLA, "se movio la nomina en algun momento de esta vuelta"; contra `HEAD`, "hay
un movimiento sin commitear ahora mismo". La exigencia de declararlo cae sobre
LA UNION de las dos, y el reporte tiene que nombrar cada `node_id` de la union.

SI NO HAY ANCLA, ES ROJO. Una rama sin ningun commit de acta no permite saber
donde empieza la vuelta, y esta guarda no da verdes por no haber podido mirar
(banco 9).

PRUEBA DE MUTACION (obligatoria, `EJECUTOR.md` 1, SOBRE VARIABLE COMPUTADA Y
NUNCA SOBRE UN LITERAL, y con `dataset/` identico antes y despues):
`scripts/loop/vuelta147_3d_mutacion_nomina.py` y, para el lado del commit,
`scripts/loop/vuelta148_2a_mutacion_nomina_commiteada.py`, que reproduce el
agujero exacto (arbol y `HEAD` IDENTICOS y movidos los dos) y comprueba que
ahora CAE.

USO:
  python scripts/loop/verificar_nomina_sellada.py
"""
import io
import json
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_NOMINA_REL = "dataset/metadata/aduana_fuente_multiple.json"
RUTA_NOMINA = os.path.join(RAIZ, RUTA_NOMINA_REL.replace("/", os.sep))
RUTA_REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")

MARCA_DECLARACION = "RE-SELLADO DE LA NOMINA DE LA ADUANA"


def _adjudicados(texto):
    """{node_id: [declaraciones en orden]} de un JSON de nomina."""
    d = json.loads(texto)
    return dict((x["node_id"], list(x["fuente"])) for x in d.get("adjudicados", []))


PATRONES_ACTA = (
    "ACTA DE LA VUELTA ",
    "ACTA DEL AUDITOR, VUELTA ",
)


def ancla_de_la_vuelta():
    """EL COMMIT DONDE EMPIEZA LA VUELTA EN CURSO: el acta mas reciente de la
    rama. Devuelve (hash, asunto) o (None, motivo). No hace falta pasarle el
    numero de vuelta: el acta mas reciente ES el limite, se llame como se
    llame."""
    # Separador: un espacio. El hash no lleva espacios, asi que partir por el
    # primero es exacto, y evita meter un caracter de control en el fuente.
    r = subprocess.run(["git", "log", "--pretty=format:%H %s"], cwd=RAIZ,
                       capture_output=True)
    if r.returncode != 0:
        return None, "git log no respondio"
    for linea in r.stdout.decode("utf-8", "replace").splitlines():
        if " " not in linea:
            continue
        h, asunto = linea.split(" ", 1)
        if any(asunto.startswith(p) for p in PATRONES_ACTA):
            return h, asunto
    return None, "la rama no trae ningun commit de acta: no se sabe donde empieza la vuelta"


def nomina_en(ref):
    """La nomina TAL COMO ESTA COMMITEADA en la ref dada."""
    r = subprocess.run(["git", "show", "%s:%s" % (ref, RUTA_NOMINA_REL)], cwd=RAIZ,
                       capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8")


def nomina_de_head():
    """La nomina TAL COMO ESTA COMMITEADA EN `HEAD`. Se lee de git y no de una
    copia (`EJECUTOR.md`, LA IDENTIDAD SE LEE DE GIT)."""
    r = subprocess.run(["git", "show", "HEAD:%s" % RUTA_NOMINA_REL], cwd=RAIZ,
                       capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8")


def diferencias(hoy, head):
    """(entran, salen, cambian) por `node_id`. Listas ordenadas, para que la
    salida sea reproducible y citable."""
    entran = sorted(set(hoy) - set(head))
    salen = sorted(set(head) - set(hoy))
    cambian = sorted(n for n in (set(hoy) & set(head)) if hoy[n] != head[n])
    return entran, salen, cambian


def verificar(texto_hoy=None, texto_head=None, texto_reporte=None, texto_ancla=None):
    """(ok, fallos, detalle). Los tres textos son INYECTABLES a proposito: la
    prueba de mutacion los pasa MUTADOS EN MEMORIA y asi no escribe ni un byte
    en `dataset/` (EJECUTOR.md 1, la mutacion va sobre variable computada y no
    sobre un literal; P.16, quien fabrica limpia, y aqui no hay nada que
    limpiar porque no se fabrica nada en disco)."""
    fallos = []

    if texto_hoy is None:
        if not os.path.exists(RUTA_NOMINA):
            return False, ["%s no existe en el arbol de trabajo: sin nomina el control "
                           "posicional no mide nada" % RUTA_NOMINA_REL], {}
        texto_hoy = io.open(RUTA_NOMINA, encoding="utf-8").read()
    if texto_head is None:
        texto_head = nomina_de_head()
        if texto_head is None:
            return False, ["no se pudo leer HEAD:%s con git show: la guarda NO puede "
                           "comprobar si la nomina se movio, y eso es ROJO y nunca un "
                           "verde por no haber podido mirar" % RUTA_NOMINA_REL], {}
    # EL LADO DEL COMMIT (vuelta 148, TAREA 2.1). Sin esto, commitear el
    # re-sellado bastaba para que arbol y HEAD dijeran lo mismo y la guarda no
    # viera nada: el agujero que la segunda mutacion del auditor encontro.
    ancla_hash = None
    if texto_ancla is None:
        ancla_hash, asunto = ancla_de_la_vuelta()
        if ancla_hash is None:
            return False, ["no se pudo fijar el ancla de la vuelta (%s): sin ella no se "
                           "puede ver un movimiento que llegue YA COMMITEADO, y eso es ROJO "
                           "y nunca un verde por no haber podido mirar" % asunto], {}
        texto_ancla = nomina_en(ancla_hash)
        if texto_ancla is None:
            return False, ["no se pudo leer %s:%s con git show: la guarda NO puede comprobar "
                           "si la nomina se movio durante la vuelta"
                           % (ancla_hash[:8], RUTA_NOMINA_REL)], {}
    try:
        hoy = _adjudicados(texto_hoy)
        head = _adjudicados(texto_head)
        ancla = _adjudicados(texto_ancla)
    except (ValueError, KeyError, TypeError) as e:
        return False, ["no se pudo interpretar la nomina (%s): %s"
                       % (RUTA_NOMINA_REL, e)], {}

    # DOS COMPARACIONES QUE CONTESTAN COSAS DISTINTAS, Y LA EXIGENCIA CAE SOBRE
    # LA UNION: contra HEAD, "hay un movimiento sin commitear ahora"; contra el
    # ancla, "se movio la nomina en algun momento de esta vuelta".
    e_head, s_head, c_head = diferencias(hoy, head)
    e_ancla, s_ancla, c_ancla = diferencias(hoy, ancla)
    entran = sorted(set(e_head) | set(e_ancla))
    salen = sorted(set(s_head) | set(s_ancla))
    cambian = sorted(set(c_head) | set(c_ancla))
    detalle = {"en_head": len(head), "hoy": len(hoy), "en_ancla": len(ancla),
               "ancla": (ancla_hash[:8] if ancla_hash else "inyectada"),
               "entran": entran, "salen": salen, "cambian": cambian,
               "solo_contra_ancla": sorted((set(e_ancla) | set(s_ancla) | set(c_ancla))
                                           - (set(e_head) | set(s_head) | set(c_head)))}
    if not (entran or salen or cambian):
        return True, [], detalle

    if texto_reporte is None:
        if not os.path.exists(RUTA_REPORTE):
            return False, ["la nomina se movio y no existe %s donde declararlo"
                           % RUTA_REPORTE], detalle
        texto_reporte = io.open(RUTA_REPORTE, encoding="utf-8").read()

    if MARCA_DECLARACION not in texto_reporte:
        solo_ancla = detalle["solo_contra_ancla"]
        coletilla = ""
        if solo_ancla:
            coletilla = (" ATENCION: %d de ellos NO se ven contra HEAD y solo aparecen "
                         "contra el ancla de la vuelta (%s), o sea que LLEGARON YA "
                         "COMMITEADOS: %s" % (len(solo_ancla), detalle["ancla"],
                                              ", ".join(solo_ancla[:5])))
        fallos.append("la nomina se movio (%d entran, %d salen, %d cambian) y el reporte NO "
                      "trae la marca %r: re-sellar la nomina es RE-ADJUDICAR y no puede "
                      "hacerse callando.%s" % (len(entran), len(salen), len(cambian),
                                               MARCA_DECLARACION, coletilla))
    for rotulo, cuales in (("entra", entran), ("sale", salen), ("cambia", cambian)):
        for nid in cuales:
            if nid not in texto_reporte:
                fallos.append("%s %s en la nomina y el reporte NO lo nombra" % (nid, rotulo))
    return (not fallos), fallos, detalle


def main():
    ok, fallos, detalle = verificar()
    if not ok:
        print("ROJO EXIT 1, la nomina de la aduana se movio sin declararse (%d cosa(s) no "
              "cuadran):" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("VERDE EXIT 0: la nomina de la aduana no se movio en silencio.")
    print("   entradas en el ancla de la vuelta (%s): %d | en HEAD: %d | hoy: %d"
          % (detalle.get("ancla"), detalle.get("en_ancla", -1), detalle["en_head"],
             detalle["hoy"]))
    print("   entran: %d | salen: %d | cambian: %d"
          % (len(detalle["entran"]), len(detalle["salen"]), len(detalle["cambian"])))
    for rotulo in ("entran", "salen", "cambian"):
        for nid in detalle[rotulo]:
            print("      %s: %s (declarado en el reporte)" % (rotulo, nid))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
