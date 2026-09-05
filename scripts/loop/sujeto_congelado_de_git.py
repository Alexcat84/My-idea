# -*- coding: utf-8 -*-
r"""sujeto_congelado_de_git.py . UN SUJETO CONGELADO SE LEE DE UN BLOB DE GIT
CLAVADO Y SE COMPRUEBA POR SU sha256, NO SE COPIA DEL FICHERO VIVO.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como sus hermanos
`cotejar_clon_declarado.py`, `paso0_archivar_anterior.py`,
`archivar_reporte.py`, `anexar_tarea_al_reporte.py`, `cerrar_reporte.py`,
`backlog_l03_resuelto.py` y `guarda_commit_dataset.py`: lo llama cualquier arnes
que necesite congelar su sujeto, y NO SE CLONA.

POR QUE NACE, Y LA CAUSA ESTA MEDIDA (vuelta 180, TAREA 2.b; adjudicacion 7.8
del acta 179). La guarda del sujeto congelado salia en ROJO con **17 entradas de
103**, y de esas diecisiete **cuatro abrian de verdad un fichero que la campana
mueve cada vuelta**. Un arnes anclado a un fichero vivo es la especie del
`banco 9`: hoy pasa, manana falla, y nadie sabe si fallo porque la maquina se
rompio o porque el fichero cambio. **El de la vuelta 160 es el ejemplar**: copia
el fichero vivo a un temporal en cada corrida, asi que PARECE congelado y no lo
es, porque lo que copia cambia.

LOS DOS CANDADOS, Y HACEN FALTA LOS DOS:

  1. EL BLOB VA CLAVADO POR SU COMMIT Y SU RUTA (`git cat-file -p <commit>:<ruta>`),
     que es el mismo patron que `scripts/loop/vuelta135_2e_mutacion_1.py` ya usa
     y que el propio juez de la 179 reconoce como sujeto clavado.
  2. Y EL CONTENIDO SE COMPRUEBA POR `sha256` CONTRA EL VALOR QUE EL ARNES
     DECLARA. Sin este segundo candado, cambiar el commit del pin por
     descuido pasaria en silencio. Con el, **CAE EN ROJO nombrando los dos
     sha256**, el esperado y el medido.

LO QUE ESTE FICHERO NO HACE: no escribe nada, no toca el arbol de trabajo y no
adivina ningun pin. Si el blob no esta o el `sha256` no calza, **levanta
`SujetoNoCongelado` con las dos cifras dentro**, y quien lo llame decide si eso
es su rojo. Fallar ruidoso, no mentir calladito.

USO (desde un arnes):
  import sujeto_congelado_de_git as SC
  TEXTO = SC.texto_del_blob(COMMIT, "docs/plan/LECTURAS_DIRIGIDAS.md", SHA)
"""
import hashlib
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class SujetoNoCongelado(Exception):
    """El blob no esta, o su contenido no es el que el arnes declaro."""


def bytes_del_blob(commit, ruta):
    """LOS BYTES CRUDOS DEL BLOB `commit:ruta`, leidos de git y no del arbol.

    Levanta `SujetoNoCongelado` si git no lo entrega."""
    r = subprocess.run(["git", "cat-file", "-p", "%s:%s" % (commit, ruta)],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SujetoNoCongelado(
            "git no entrega el blob %s:%s (exit %d). %s"
            % (commit, ruta, r.returncode,
               r.stderr.decode("utf-8", errors="replace").strip()[:200]))
    return r.stdout


def sha256_de(datos):
    """El sha256 de unos bytes, normalizados a LF. PURA.

    NORMALIZADO A PROPOSITO: este repo tiene `core.autocrlf=true`, y la
    convencion de fin de linea del sistema operativo no es un cambio de
    contenido. Es la misma normalizacion que usa `estado_de()` de
    `scripts/loop/verificar_mutaciones_viejas.py`."""
    return hashlib.sha256(
        datos.replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()


def texto_del_blob(commit, ruta, sha_esperado=None, codificacion="utf-8"):
    """EL TEXTO DEL BLOB CLAVADO, con su `sha256` comprobado si se declara.

    Devuelve el texto normalizado a LF. Levanta `SujetoNoCongelado` con LAS DOS
    cifras dentro si el `sha256` no calza: el esperado y el medido."""
    crudo = bytes_del_blob(commit, ruta)
    medido = sha256_de(crudo)
    if sha_esperado is not None and medido != sha_esperado:
        raise SujetoNoCongelado(
            "el blob %s:%s no trae el contenido declarado. sha256 esperado %s, "
            "medido %s" % (commit, ruta, sha_esperado, medido))
    return crudo.decode(codificacion, errors="replace").replace("\r\n", "\n")


def volcar_blob(commit, ruta, destino, sha_esperado=None):
    """ESCRIBE EL BLOB CLAVADO EN `destino` y devuelve su `sha256` medido.

    Es lo que un arnes usa en vez de `shutil.copy` del fichero vivo: el destino
    es siempre un temporal del propio arnes, y lo que se vuelca no se mueve."""
    crudo = bytes_del_blob(commit, ruta)
    medido = sha256_de(crudo)
    if sha_esperado is not None and medido != sha_esperado:
        raise SujetoNoCongelado(
            "el blob %s:%s no trae el contenido declarado. sha256 esperado %s, "
            "medido %s" % (commit, ruta, sha_esperado, medido))
    with open(destino, "wb") as f:
        f.write(crudo)
    return medido
