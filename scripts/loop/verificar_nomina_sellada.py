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

PRUEBA DE MUTACION (obligatoria, `EJECUTOR.md` 1, SOBRE VARIABLE COMPUTADA Y
NUNCA SOBRE UN LITERAL, y con `dataset/` identico antes y despues):
`scripts/loop/vuelta147_3d_mutacion_nomina.py`.

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


def verificar(texto_hoy=None, texto_head=None, texto_reporte=None):
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
    try:
        hoy = _adjudicados(texto_hoy)
        head = _adjudicados(texto_head)
    except (ValueError, KeyError, TypeError) as e:
        return False, ["no se pudo interpretar la nomina (%s): %s"
                       % (RUTA_NOMINA_REL, e)], {}

    entran, salen, cambian = diferencias(hoy, head)
    detalle = {"en_head": len(head), "hoy": len(hoy),
               "entran": entran, "salen": salen, "cambian": cambian}
    if not (entran or salen or cambian):
        return True, [], detalle

    if texto_reporte is None:
        if not os.path.exists(RUTA_REPORTE):
            return False, ["la nomina se movio y no existe %s donde declararlo"
                           % RUTA_REPORTE], detalle
        texto_reporte = io.open(RUTA_REPORTE, encoding="utf-8").read()

    if MARCA_DECLARACION not in texto_reporte:
        fallos.append("la nomina se movio (%d entran, %d salen, %d cambian) y el reporte NO "
                      "trae la marca %r: re-sellar la nomina es RE-ADJUDICAR y no puede "
                      "hacerse callando" % (len(entran), len(salen), len(cambian),
                                            MARCA_DECLARACION))
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
    print("   entradas en HEAD: %d | entradas hoy: %d" % (detalle["en_head"], detalle["hoy"]))
    print("   entran: %d | salen: %d | cambian: %d"
          % (len(detalle["entran"]), len(detalle["salen"]), len(detalle["cambian"])))
    for rotulo in ("entran", "salen", "cambian"):
        for nid in detalle[rotulo]:
            print("      %s: %s (declarado en el reporte)" % (rotulo, nid))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
