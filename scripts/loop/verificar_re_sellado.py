# -*- coding: utf-8 -*-
"""verificar_re_sellado.py . NO SE PROHIBE RE SELLAR: SE PROHIBE RE SELLAR EN
SILENCIO (adjudicacion 6.10 del acta 157, vuelta 157, TAREA 6).

NOMBRE ESTABLE, SIN NUMERO DE VUELTA, como `verificar_apertura_sellada.py`,
`verificar_mutaciones_viejas.py` y `tallar_cabecera_reporte.py`: se corre igual
en toda vuelta y no se clona.

DE DONDE NACE, Y NACE DE UNA CAIDA DE REPORTE DEL EJECUTOR. La caida 4 del
reporte de la vuelta 156 remataba con "las cifras no cambiaron: lo que cambio
fue la columna", y el auditor lo desmintio con `git diff 92d29d23^ 92d29d23`
sobre los propios ficheros del ejecutor: el re sellado movio
`SALIDA_V156_T4C_CIFRAS.txt` de "salidas selladas 52" a 55 y de "con un nombre
de fase que CALZA: 50" a 53, y `SALIDA_V156_T3A_FIGURA_DELGADA.txt` de
{"C": 121, "D": 1} a {"C": 119, "D": 3}. Ninguna cifra PUBLICADA era falsa,
porque el reporte pega las lineas finales. Lo falso era la afirmacion sobre el
EFECTO de la propia correccion: lo que no movio cifras fue dedentar, lo que las
movio fue re correr mas tarde.

QUE COMPRUEBA, Y TODO COMPUTADO:
  1. Saca de `docs/loop/REPORTE.md` los nombres `SALIDA_*.txt` que el reporte
     CITA. No se teclean: se leen del reporte con un patron.
  2. Para cada uno busca EL COMMIT DE SU TAREA, que es el primer commit que lo
     ANADIO (`git log --diff-filter=A`), leido de git y no tecleado.
  3. Compara ese blob contra el de HEAD. Si son iguales, no hay nada que
     declarar y la fila sale LIMPIA.
  4. Si cambio, COMPUTA el `numstat` entre las dos versiones y LA LISTA DE
     LINEAS `CIFRA` CUYO VALOR CAMBIO, y EXIGE que el reporte lo declare con
     esa linea exacta:

         RE SELLADO DECLARADO: <fichero> numstat +A/-B, lineas CIFRA con valor
         cambiado: N (<nombres>)

     Si cambio y el reporte no trae esa linea, es ROJO CON SU NOMBRE.

POR QUE LA LINEA ES LITERAL Y NO UN PARRAFO LIBRE: porque una narracion no se
puede cotejar. La guarda computa A, B, N y los nombres, y el reporte tiene que
traer LO QUE LA GUARDA COMPUTO. Es la misma disciplina de
`tallar_cabecera_reporte.py`: la celda que no sale de un instrumento no se
escribe.

LO QUE ESTA GUARDA NO HACE, Y SE DICE: no prohibe re sellar y no juzga si el re
sellado estuvo bien. Solo exige que quede DICHO, con su numstat y sus cifras
movidas. Un fichero que el reporte cita y que todavia no esta committeado se
declara SIN COMMIT DE TAREA y no puede ser rojo: no hay dos versiones que
comparar.

EL LIMITE DE ESTA VARA, DECLARADO ANTES DE QUE NADIE LO DESCUBRA, y medido sobre
el propio caso del auditor: SOLO VE LINEAS CON LA CONVENCION `CIFRA <nombre>:
<valor>`. Corrida sobre `SALIDA_V156_T4C_CIFRAS.txt`, esta guarda computa UNA
linea CIFRA movida ("CIFRA salidas selladas del tallador"), mientras que el
auditor nombro DOS cambios en ese fichero: aquel y "con un nombre de fase que
CALZA: 50 a 53", que NO lleva el rotulo `CIFRA` y por eso esta vara no lo
alcanza. LO QUE ESTA GUARDA GARANTIZA NO ES QUE SE VEAN TODAS LAS CIFRAS
MOVIDAS: es que UN FICHERO QUE CAMBIO NO PASE EN SILENCIO, porque el `numstat`
si cuenta el fichero entero y el rojo salta igual aunque ninguna linea `CIFRA`
se mueva. La cobertura de la lista de cifras crece sola el dia que mas lineas
lleven su rotulo.

PRUEBA DE MUTACION: `scripts/loop/vuelta157_tarea6b_mutacion_re_sellado.py`,
salida `docs/loop/SALIDA_V157_T6B_MUTACION_RE_SELLADO.txt`.

USO:
  python scripts/loop/verificar_re_sellado.py
  python scripts/loop/verificar_re_sellado.py --reporte docs/loop/REPORTE.md

--- ADJUDICACION 6.8 DEL ACTA 158 (3 sep 2026): ESTA GUARDA NO PUEDE ACUSAR A SU
PROPIA SALIDA ---

CORRECCION DECLARADA POR ADICION. Nada de lo escrito arriba se borra.

EL HECHO, MEDIDO POR EL AUDITOR CORRIENDO ESTA GUARDA (acta 158, seccion 5.2):
sobre el reporte en HEAD sale ROJO exit 1 acusando
`SALIDA_V157_T9_CIFRAS_REPORTE.txt` y `SALIDA_V157_T9_RE_SELLADO.txt`, y lo
verifico con `git diff --numstat b166ab47 HEAD` (2 y 2 sobre el primero, 24 y 22
sobre el segundo).

Y EL MOTIVO ES DE CONSTRUCCION, NO DE DICTADO: esta guarda compara cada salida
citada contra su commit de tarea, y EL COMMIT QUE PUBLICA EL REPORTE RE ESCRIBE
NECESARIAMENTE la salida de esta misma guarda y la del verificador de cifras,
porque las dos se re corren sobre el reporte final. NINGUN REPORTE PUEDE DEJARLA
VERDE EN HEAD. Exigir al ejecutor una afirmacion que expira al commitearla seria
exigir lo imposible, y el acta lo dice con esas palabras: NO ES CAIDA SUYA.

EL REMEDIO ADJUDICADO: esta guarda EXIME de la comparacion los ficheros que ella
misma y el verificador de cifras escriben sobre el reporte final (o compara
contra el commit del reporte en vez de contra HEAD), Y PUBLICA ESA EXENCION COMO
LINEA COMPUTADA CON LOS NOMBRES EXENTOS. Una exencion que no se imprime es un
agujero; una que se imprime es una vara con su limite dicho. Con su caso
positivo por mutacion: un fichero de tarea NORMAL re sellado y no declarado
TIENE QUE SEGUIR SALIENDO ROJO.
"""
import argparse
import io
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE_POR_DEFECTO = "docs/loop/REPORTE.md"

PATRON_SALIDA = re.compile(r"\bSALIDA_[A-Z0-9_]+\.txt\b")
# Una linea CIFRA es la convencion de la casa: `CIFRA <nombre>: <valor>`. Se
# parte en NOMBRE y VALOR para poder decir si cambio EL VALOR y no solo la
# columna, que es justo la distincion que la caida 4 de la vuelta 156 borro.
PATRON_CIFRA = re.compile(r"^\s*(CIFRA\s+.*?):\s*(.*)$")

PLANTILLA = ("RE SELLADO DECLARADO: %s numstat +%d/-%d, lineas CIFRA con valor "
             "cambiado: %d (%s)")


def git(*args):
    r = subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def commit_de_su_tarea(ruta_rel):
    """El PRIMER commit que anadio el fichero. Leido de git, nunca tecleado."""
    codigo, salida = git("log", "--format=%H", "--diff-filter=A", "--", ruta_rel)
    if codigo:
        return None
    hashes = [x.strip() for x in salida.splitlines() if x.strip()]
    return hashes[-1] if hashes else None


def blob(ref, ruta_rel):
    codigo, salida = git("show", "%s:%s" % (ref, ruta_rel))
    return None if codigo else salida


def cifras_de(texto):
    """dict NOMBRE -> VALOR de las lineas CIFRA. El nombre se normaliza en
    espacios para que DEDENTAR o re alinear NO cuente como cambio de valor: esa
    distincion es el corazon de esta guarda."""
    out = {}
    for linea in (texto or "").splitlines():
        m = PATRON_CIFRA.match(linea)
        if m:
            out[" ".join(m.group(1).split())] = " ".join(m.group(2).split())
    return out


def numstat_entre(a, b, ruta_rel):
    codigo, salida = git("diff", "--numstat", a, b, "--", ruta_rel)
    if codigo or not salida.strip():
        return 0, 0
    campos = salida.strip().splitlines()[0].split("\t")
    try:
        return int(campos[0]), int(campos[1])
    except ValueError:
        return 0, 0


def analizar(ruta_rel):
    """Devuelve el estado de UN fichero. Todo computado."""
    tarea = commit_de_su_tarea(ruta_rel)
    if not tarea:
        return {"fichero": ruta_rel, "estado": "SIN COMMIT DE TAREA"}
    viejo = blob(tarea, ruta_rel)
    nuevo = blob("HEAD", ruta_rel)
    if nuevo is None:
        return {"fichero": ruta_rel, "estado": "NO ESTA EN HEAD", "tarea": tarea}
    norm = lambda t: (t or "").replace("\r\n", "\n").replace("\r", "\n")
    if norm(viejo) == norm(nuevo):
        return {"fichero": ruta_rel, "estado": "SIN RE SELLAR", "tarea": tarea}
    ca, cb = cifras_de(viejo), cifras_de(nuevo)
    movidas = sorted(k for k in set(ca) | set(cb) if ca.get(k) != cb.get(k))
    mas, menos = numstat_entre(tarea, "HEAD", ruta_rel)
    return {"fichero": ruta_rel, "estado": "RE SELLADO", "tarea": tarea,
            "mas": mas, "menos": menos, "movidas": movidas,
            "antes": ca, "despues": cb,
            "linea": PLANTILLA % (os.path.basename(ruta_rel), mas, menos,
                                  len(movidas), ", ".join(movidas) or "ninguna")}


# --- LA EXENCION DE LA 6.8 DEL ACTA 158, POR NOMBRE Y DECLARADA ---
#
# QUE SE EXIME Y POR QUE. Esta guarda y `verificar_cifras_del_reporte.py` se
# CORREN SOBRE EL REPORTE FINAL, asi que el commit que publica ese reporte re
# escribe necesariamente sus dos salidas. Ningun reporte puede dejarlas verdes
# en HEAD, y exigir una afirmacion que expira al commitearla es exigir lo
# imposible (acta 158, seccion 5.2 y adjudicacion 6.8).
#
# POR QUE POR SUFIJO DE NOMBRE Y NO POR UNA NOMINA CERRADA: la nomina fija
# tendria que re escribirse cada vuelta, porque los nombres llevan el numero de
# vuelta dentro (`SALIDA_V157_T9_RE_SELLADO.txt`, `SALIDA_V159_T9_RE_SELLADO.txt`).
# El sufijo `_RE_SELLADO.txt` y `_CIFRAS_REPORTE.txt` queda RESERVADO desde hoy
# para las salidas de estas dos guardas sobre el reporte final, por convencion,
# igual que `verificar_apertura_sellada.py` reservo la palabra `MUTACION` en la
# vuelta 102. Ninguna salida de tarea normal necesita esos sufijos.
#
# QUE NO HACE ESTA EXENCION, Y SE DICE: NO calla al fichero exento. Se sigue
# analizando, se sigue imprimiendo con su estado y su numstat, y ademas se
# imprime UNA LINEA COMPUTADA CON LOS NOMBRES EXENTOS. Lo unico que la exencion
# quita es que cuenten para el ROJO. Una exencion que no se imprime es un
# agujero; una que se imprime es una vara con su limite dicho.
PATRON_EXENTO = re.compile(r"_(RE_SELLADO|CIFRAS_REPORTE)\.txt$")

# Y LA EXENCION SE ESTRECHA ANTES DE PUBLICARSE, POR UN AGUJERO QUE LA PRIMERA
# CORRIDA DE ESTA MISMA VUELTA ENSENO Y QUE SE DECLARA EN VEZ DE TAPARSE. Con
# solo el sufijo, el patron tambien eximia a
# `SALIDA_V157_T6B_MUTACION_RE_SELLADO.txt`, que NO es la salida de esta guarda
# sobre el reporte final sino la salida de su PRUEBA DE MUTACION. Hoy ese
# fichero esta SIN RE SELLAR y la exencion no cambiaba ningun veredicto, pero
# una exencion mas ancha de lo que su motivo justifica es un agujero esperando.
# Se descarta la palabra `MUTACION`, que ya es palabra reservada de las salidas
# de prueba en esta casa desde la vuelta 102 (ver
# `verificar_apertura_sellada.py`, "la guarda que se envenena sola").
PATRON_NO_EXENTO = re.compile(r"MUTACION")


def es_exento(ruta_rel):
    base = os.path.basename(ruta_rel)
    if PATRON_NO_EXENTO.search(base):
        return False
    return bool(PATRON_EXENTO.search(base))


def exentos_de(filas):
    """Las filas exentas POR CONSTRUCCION. Funcion propia para que el caso por
    mutacion ejerza este codigo y no una copia."""
    return [f for f in filas if es_exento(f["fichero"])]


def linea_de_exencion(filas):
    """LA LINEA COMPUTADA que la 6.8 exige publicar, con los nombres."""
    ex = exentos_de(filas)
    return ("EXENCION POR CONSTRUCCION (adjudicacion 6.8 del acta 158): %d "
            "fichero(s) exento(s) del rojo, por ser la salida de esta guarda o "
            "del verificador de cifras sobre el reporte final: %s"
            % (len(ex), ", ".join(sorted(os.path.basename(f["fichero"]) for f in ex))
               or "ninguno"))


def las_que_faltan(filas, texto):
    """Las filas RE SELLADO cuya linea computada NO esta en el texto del
    reporte. Es EL veredicto de esta guarda, y vive en una funcion propia para
    que el caso por mutacion ejerza EXACTAMENTE este codigo y no una copia.

    CORRECCION DECLARADA (vuelta 159, adjudicacion 6.8 del acta 158): se anade
    la condicion `not es_exento(...)`. La version anterior de esta linea era
    `f["estado"] == "RE SELLADO" and f["linea"] not in texto`, sin la exencion,
    y se escribe aqui entera para que la correccion se pueda auditar sin ir a
    git."""
    return [f for f in filas
            if f["estado"] == "RE SELLADO"
            and not es_exento(f["fichero"])
            and f["linea"] not in texto]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reporte", default=REPORTE_POR_DEFECTO)
    a = ap.parse_args()

    ruta_reporte = os.path.join(RAIZ, a.reporte)
    if not os.path.exists(ruta_reporte):
        print("ROJO PREVIO: no existe %s" % a.reporte)
        print("FIN")
        return 1
    texto = io.open(ruta_reporte, encoding="utf-8").read()

    print("=" * 78)
    print("VERIFICAR RE SELLADO: TODA SALIDA_* QUE EL REPORTE CITE Y QUE HAYA CAMBIADO")
    print("DESPUES DEL COMMIT DE SU TAREA TIENE QUE IR DECLARADA")
    print("=" * 78)
    print("  reporte: %s" % a.reporte)

    citados = sorted(set(PATRON_SALIDA.findall(texto)))
    print("  CIFRA salidas selladas que el reporte cita: %d" % len(citados))
    print("")

    filas = [analizar("docs/loop/%s" % n) for n in citados]
    por_estado = {}
    for f in filas:
        por_estado[f["estado"]] = por_estado.get(f["estado"], 0) + 1

    sin_declarar = las_que_faltan(filas, texto)
    faltan = {f["fichero"] for f in sin_declarar}
    for f in filas:
        print("  %-46s %s" % (os.path.basename(f["fichero"]), f["estado"]))
        if f["estado"] != "RE SELLADO":
            continue
        print("      commit de su tarea : %s" % f["tarea"][:12])
        print("      numstat contra HEAD: +%d/-%d" % (f["mas"], f["menos"]))
        print("      CIFRA lineas CIFRA cuyo VALOR cambio: %d" % len(f["movidas"]))
        for k in f["movidas"]:
            print("         %s: %r -> %r"
                  % (k, f["antes"].get(k, "(no estaba)"), f["despues"].get(k, "(ya no esta)")))
        if f["fichero"] not in faltan:
            print("      DECLARADO EN EL REPORTE: SI, con la linea que esta guarda computo")
        else:
            print("      DECLARADO EN EL REPORTE: NO")
            print("      la linea que falta, LITERAL:")
            print("         %s" % f["linea"])

    print("")
    print("  CIFRA por estado: %s"
          % ", ".join("%s %d" % (k, v) for k, v in sorted(por_estado.items())))
    exentos = exentos_de(filas)
    exentos_re = [f for f in exentos if f["estado"] == "RE SELLADO"]
    print("  CIFRA salidas EXENTAS por construccion: %d" % len(exentos))
    print("  CIFRA de esas exentas que ademas estan RE SELLADAS: %d" % len(exentos_re))
    print("  %s" % linea_de_exencion(filas))
    for f in exentos_re:
        print("      %s: RE SELLADO, numstat +%d/-%d, lineas CIFRA movidas %d"
              % (os.path.basename(f["fichero"]), f["mas"], f["menos"],
                 len(f["movidas"])))
    print("  CIFRA re selladas SIN declarar en el reporte: %d" % len(sin_declarar))
    print("")
    if sin_declarar:
        print("ROJO: %d salida(s) sellada(s) cambiaron despues del commit de su tarea y el"
              % len(sin_declarar))
        print("reporte no lo declara: %s"
              % ", ".join(os.path.basename(f["fichero"]) for f in sin_declarar))
        print("No se prohibe re sellar. Se prohibe re sellar EN SILENCIO.")
        print("FIN")
        return 1
    print("VERDE: ninguna salida sellada citada por el reporte cambio en silencio.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
