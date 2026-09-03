# -*- coding: utf-8 -*-
"""huella_de_contenido.py . LA HUELLA DE CONTENIDO DEL CHECK DE P.16.

NACE EN LA TAREA 3 DE LA VUELTA 160, POR LA ADJUDICACION 6.1 DEL ACTA 159 (que
fija el alcance en DOCE ficheros y la vara en la lectura B) Y POR LA 6.7 DEL ACTA
158, QUE ES LA QUE DESCRIBE EL DEFECTO.

EL DEFECTO, EN LA LETRA DE LA 6.7: el docstring de los doce dice que comprueban
que `dataset/` y `docs/plan/` NO SE TOCAN NI UNA VEZ, o sea CONTENIDO; y el
instrumento con que lo comprueban es `git status --porcelain`, que ademas de
contenido ve DOS COSAS QUE NO SON SUYAS:

  ANCLA 1, EL FIN DE LINEA. `git status` compara el arbol de trabajo contra el
  indice PASANDO POR LA CONVERSION de `core.autocrlf`. Un fichero cuyo contenido
  nadie toco puede aparecer modificado por su estado de fin de linea. En este
  repo no es hipotetico: cada `git add` de esta campana imprime la advertencia
  "LF will be replaced by CRLF the next time Git touches it".

  ANCLA 2, LA SUCIEDAD ANTERIOR AL ARRANQUE. `git status` ve TODO lo que este
  sucio, lo haya ensuciado el script o no. Si el arbol venia sucio de antes, el
  check acusa al script de una escritura que no hizo. Un rojo que nombra al
  culpable equivocado es MEDIA GUARDA (adjudicacion 6.9 del acta 157).

EL REMEDIO, QUE ES LO QUE ESTE MODULO HACE: una HUELLA DE CONTENIDO tomada ANTES
y DESPUES de las mutaciones DENTRO DEL PROPIO SCRIPT, y COMPARADA CONSIGO MISMA.

  - Las dos anclas mueren juntas y por el mismo motivo: LA HUELLA NUNCA MIRA A
    GIT. Se lee el disco y se compara el disco contra el disco.
  - EL FIN DE LINEA: se hashean LOS BYTES CRUDOS, sin normalizar. Se declara por
    que, porque la decision contraria seria defendible y no es la que se toma:
    normalizar taparia una mutacion que cambiara SOLO los fines de linea, y esa
    tambien es una escritura. Como las dos tomas ocurren en la misma corrida y
    sobre el mismo arbol de trabajo, la conversion de `core.autocrlf` (que pasa
    en el checkout, fuera de la corrida) no puede meterse entre las dos.
  - LA SUCIEDAD ANTERIOR: si el arbol venia sucio, viene sucio en LAS DOS tomas
    y la huella sale igual. Solo cae si el script ESCRIBIO.

QUE MIDE, EXACTAMENTE: sha256 sobre la secuencia ordenada de (ruta relativa con
barras normales, bytes del fichero) de todos los ficheros bajo los prefijos que
se le pasen. El orden es determinista (`sorted` de directorios y de ficheros) y
la ruta entra en el hash, asi que RENOMBRAR tambien cae, no solo editar. Se
devuelve tambien el CONTEO de ficheros, para que un borrado se pueda nombrar en
el rojo en vez de aparecer solo como un hash distinto.

QUE NO PUEDE VER, Y SE DICE EN VEZ DE CALLARLO: un fichero escrito y devuelto a
su contenido exacto ANTES de la segunda toma. La huella es una guarda de ESTADO
FINAL, no un rastro de escrituras. La comprobacion vieja de `git status` tenia
la misma ceguera, asi que el remedio no la introduce.

ESTE MODULO NO CONTIENE EL PATRON LITERAL DEL CHECK DE P.16, Y ES A PROPOSITO:
si lo contuviera se sumaria al alcance de los DOCE y la nomina de la 6.1 pasaria
a trece sin que nadie anadiera un check. Por eso lee el disco con `os.walk` y no
invoca a git ni una vez.

USO desde uno de los doce:
    import huella_de_contenido as HC
    antes = HC.huella("dataset/", "docs/plan/")      # ANTES de mutar
    ...
    despues = HC.huella("dataset/", "docs/plan/")    # DESPUES de mutar
    ok, linea = HC.comparar(antes, despues, "dataset/", "docs/plan/")
"""
import hashlib
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def huella(*prefijos):
    """Devuelve (hexdigest, numero de ficheros) del CONTENIDO de todo lo que
    cuelga de PREFIJOS, leido del disco y sin pasar por git.

    Un prefijo que no existe cuenta CERO ficheros y no revienta: los doce
    scripts usan pathspecs distintos y alguno puede apuntar a algo que en un
    arbol dado no este. Eso se ve en el conteo, que es parte de la huella."""
    h = hashlib.sha256()
    n = 0
    for prefijo in prefijos:
        base = os.path.join(RAIZ, prefijo.replace("/", os.sep))
        if not os.path.isdir(base):
            continue
        for raiz, dirs, ficheros in os.walk(base):
            dirs.sort()
            for f in sorted(ficheros):
                ruta = os.path.join(raiz, f)
                rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
                h.update(rel.encode("utf-8"))
                h.update(b"\x00")
                with open(ruta, "rb") as fh:
                    h.update(fh.read())
                h.update(b"\x00")
                n += 1
    return h.hexdigest(), n


def comparar(antes, despues, *prefijos):
    """Devuelve (ok, linea_para_imprimir). OK es True solo si el hash Y el
    conteo son identicos. La linea nombra QUE cambio, para que el rojo no
    obligue a adivinar."""
    rutas = " ".join(prefijos)
    if antes == despues:
        return True, ("P.16 huella de CONTENIDO de %s IDENTICA antes y despues: "
                      "sha256 %s sobre %d fichero(s). NO SE MIRO A GIT: el disco "
                      "se compara contra el disco." % (rutas, antes[0][:16], antes[1]))
    if antes[1] != despues[1]:
        return False, ("P.16 ROJO: el numero de ficheros bajo %s cambio, de %d a "
                       "%d. Alguna mutacion creo o borro ficheros y no los "
                       "devolvio." % (rutas, antes[1], despues[1]))
    return False, ("P.16 ROJO: el CONTENIDO de %s cambio con el mismo numero de "
                   "ficheros (%d): sha256 antes %s, sha256 despues %s. Alguna "
                   "mutacion escribio y no deshizo."
                   % (rutas, antes[1], antes[0][:16], despues[0][:16]))
