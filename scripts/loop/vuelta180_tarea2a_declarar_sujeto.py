# -*- coding: utf-8 -*-
r"""vuelta180_tarea2a_declarar_sujeto.py . LOS TRECE QUE NO ABREN NADA VIVO
DECLARAN SU SUJETO, UNA LINEA POR ARNES Y NI UNA MAS.

TAREA 2.a de la vuelta 180.

QUE HACE, Y ES DELIBERADAMENTE POCO. A los trece arneses que el registro
`docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl` clasifica como `LO NOMBRA SIN
ABRIRLO` (once) o `ABRE UN SUJETO YA CLAVADO` (dos) **les falta DECLARARLO, no
arreglarlo**, y eso lo dice su propio campo `que_haria_falta`. Este fichero les
anade **UNA SOLA LINEA** dentro de su docstring de modulo, con el literal que la
guarda del sujeto congelado busca, y **no toca ninguna otra linea de ninguno de
los trece**.

POR QUE DENTRO DEL DOCSTRING Y NO EN EL CODIGO. `anclaje_de()` de
`scripts/loop/verificar_mutaciones_viejas.py` busca las HUELLAS DE CONGELADO **en
el texto entero** y las HUELLAS DE SUJETO VIVO **solo en la maquina**, o sea en el
fichero sin su docstring de modulo. Una declaracion vive en el docstring por
definicion, y ponerla ahi garantiza que **la maquina no cambia en ninguno de los
trece**.

LA LINEA NO ES LA MISMA PARA TODOS, Y SE COMPONE DE SU PROPIA FILA DEL REGISTRO:
el fichero vivo que cada uno nombra, y sus cifras de lecturas, salen del registro
que la 179 escribio y verifico el fundador, no de una lista tecleada aqui.

LA GUARDA DE ESTE FICHERO, POR SI SE VUELVE A CORRER: si un arnes YA trae el
literal, **NO SE LE ANADE OTRA VEZ** y se dice. Correrlo dos veces no duplica
nada.

DONDE CAE EN ROJO, Y NO SIGUE EN SILENCIO:
  . si el registro no existe o no trae exactamente los trece esperados;
  . si un arnes del registro no esta en disco;
  . si un fichero no tiene docstring de modulo (no habria donde declarar);
  . si tras escribir, el fichero no parsea o su MAQUINA cambio en un solo byte.

USO:
  python scripts/loop/vuelta180_tarea2a_declarar_sujeto.py
  python scripts/loop/vuelta180_tarea2a_declarar_sujeto.py --solo-mirar
"""
import argparse
import ast
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import verificar_mutaciones_viejas as VMV   # noqa: E402
import json   # noqa: E402

NL = chr(10)
REGISTRO = os.path.join(RAIZ, "docs", "plan", "SUJETO_CONGELADO_VEREDICTOS.jsonl")
MARCA = "SUJETO CONGELADO"
LOS_QUE_DECLARAN = ("LO NOMBRA SIN ABRIRLO", "ABRE UN SUJETO YA CLAVADO")


def filas_del_registro(ruta=None):
    """Las filas del registro de la 179. Lo unico que lee de docs/plan/."""
    r = ruta or REGISTRO
    return [json.loads(l) for l in io.open(r, encoding="utf-8") if l.strip()]


def linea_de_declaracion(fila):
    """LA LINEA QUE SE LE ANADE A ESE ARNES, COMPUESTA DE SU PROPIA FILA. PURA.

    Devuelve una sola linea, sin salto, con el literal que la guarda busca."""
    vivos = ", ".join("`%s`" % v for v in (fila.get("ficheros_vivos_atribuidos") or [])) \
        or "(ninguno)"
    if fila.get("veredicto_de_la_lectura") == "ABRE UN SUJETO YA CLAVADO":
        cuerpo = ("lee %s de un BLOB DE GIT CLAVADO por su sha, no del fichero vivo "
                  "(%d lectura(s) de blob clavado y %d del fichero vivo, medidas fila "
                  "a fila en docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl)"
                  % (vivos, fila.get("cifra_lecturas_de_blob_clavado") or 0,
                     fila.get("cifra_lecturas_del_fichero_vivo") or 0))
    else:
        cuerpo = ("NOMBRA %s en su texto pero NO LO ABRE (%d apariciones en el texto, "
                  "%d llamadas que lo lean y %d lecturas del fichero vivo, medidas fila "
                  "a fila en docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl)"
                  % (vivos, fila.get("cifra_apariciones_en_el_texto") or 0,
                     fila.get("cifra_llamadas_que_leen_con_huella") or 0,
                     fila.get("cifra_lecturas_del_fichero_vivo") or 0))
    return ("%s (declarado en la vuelta 180, TAREA 2.a): este arnes %s, asi que su "
            "resultado no depende de lo que ese fichero diga hoy." % (MARCA, cuerpo))


def fin_del_docstring(texto):
    """EL NUMERO DE LINEA (1 based) DONDE CIERRA EL DOCSTRING DE MODULO, o None.
    PURA: recibe el texto y no toca disco."""
    try:
        arbol = ast.parse(texto)
    except (SyntaxError, ValueError):
        return None
    if not arbol.body:
        return None
    n0 = arbol.body[0]
    es_doc = (isinstance(n0, ast.Expr) and isinstance(n0.value, ast.Constant)
              and isinstance(n0.value.value, str))
    return (n0.end_lineno or n0.lineno) if es_doc else None


def con_la_declaracion(texto, linea):
    """EL TEXTO CON LA LINEA METIDA JUSTO ANTES DEL CIERRE DEL DOCSTRING. PURA.

    Devuelve (texto_nuevo, motivo). `motivo` es None si se pudo."""
    if MARCA in texto:
        return texto, "YA LO DECLARA, no se toca"
    fin = fin_del_docstring(texto)
    if fin is None:
        return texto, "no tiene docstring de modulo"
    lineas = texto.split(NL)
    lineas.insert(fin - 1, linea)
    return NL.join(lineas), None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-mirar", dest="solo_mirar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    p = print

    p("=" * 78)
    p("LOS TRECE QUE NO ABREN NADA VIVO DECLARAN SU SUJETO (vuelta 180, 2.a)")
    p("=" * 78)
    p("")

    filas = filas_del_registro()
    elegidos = [f for f in filas if f.get("veredicto_de_la_lectura") in LOS_QUE_DECLARAN]
    p("A) A QUIEN LE TOCA, LEIDO DEL REGISTRO Y NO TECLEADO")
    p("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl -> %d filas" % len(filas))
    for v in LOS_QUE_DECLARAN:
        p("   CIFRA con veredicto_de_la_lectura %-28s: %d"
          % (repr(v), sum(1 for f in filas if f.get("veredicto_de_la_lectura") == v)))
    p("   CIFRA que declaran en esta tarea: %d" % len(elegidos))
    p("")

    if len(elegidos) != 13:
        p("ROJO: se esperaban 13 y el registro da %d. No se toca nada." % len(elegidos))
        p("FIN")
        return 1

    p("B) LA LINEA DE CADA UNO, COMPUESTA DE SU PROPIA FILA")
    fallos, tocados, ya = [], [], []
    for f in filas:
        if f not in elegidos:
            continue
        nombre = f["arnes"]
        ruta = os.path.join(AQUI, nombre)
        if not os.path.exists(ruta):
            fallos.append("%s NO ESTA EN DISCO" % nombre)
            continue
        texto = io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)
        maquina_antes = VMV.sin_docstring_de_modulo(texto)
        linea = linea_de_declaracion(f)
        nuevo, motivo = con_la_declaracion(texto, linea)
        p("")
        p("   %s" % nombre)
        p("      %s" % linea[:400])
        if motivo:
            p("      -> %s" % motivo)
            if "YA LO DECLARA" in motivo:
                ya.append(nombre)
            else:
                fallos.append("%s: %s" % (nombre, motivo))
            continue
        p("      lineas antes: %d | lineas despues: %d | anadidas: %d"
          % (texto.count(NL), nuevo.count(NL), nuevo.count(NL) - texto.count(NL)))
        if nuevo.count(NL) - texto.count(NL) != 1:
            fallos.append("%s: se anadio mas de una linea" % nombre)
            continue
        if a.solo_mirar:
            p("      (--solo-mirar: no se escribe)")
            continue
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(nuevo)
        de_nuevo = io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)
        try:
            ast.parse(de_nuevo)
            parsea = True
        except (SyntaxError, ValueError):
            parsea = False
        maquina_despues = VMV.sin_docstring_de_modulo(de_nuevo)
        p("      parsea tras escribir: %s" % ("SI" if parsea else "NO"))
        p("      LA MAQUINA NO CAMBIO: %s"
          % ("SI" if maquina_antes == maquina_despues else "NO"))
        p("      trae ya el literal %r: %s" % (MARCA, "SI" if MARCA in de_nuevo else "NO"))
        if not parsea:
            fallos.append("%s: no parsea tras escribir" % nombre)
        if maquina_antes != maquina_despues:
            fallos.append("%s: LA MAQUINA CAMBIO" % nombre)
        if MARCA not in de_nuevo:
            fallos.append("%s: el literal no quedo escrito" % nombre)
        tocados.append(nombre)
    p("")

    p("C) EL RECUENTO")
    p("   CIFRA arneses tocados: %d" % len(tocados))
    p("   CIFRA que ya lo declaraban y no se tocan: %d" % len(ya))
    p("   CIFRA fallos: %d" % len(fallos))
    for f in fallos:
        p("      " + f)
    p("")

    if fallos:
        p("ROJO: %d fallo(s)." % len(fallos))
        p("FIN")
        return 1
    p("VERDE: los %d arneses que no abren nada vivo declaran su sujeto con UNA "
      "linea cada uno, dentro de su docstring, y LA MAQUINA DE LOS %d NO CAMBIO "
      "EN NINGUN BYTE, comprobado con sin_docstring_de_modulo() antes y despues."
      % (len(tocados) + len(ya), len(tocados)))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
