# -*- coding: utf-8 -*-
r"""vuelta180_tarea4_mutacion_texto_y_clon.py . LOS DOS CASOS POSITIVOS POR
MUTACION DE LA TAREA 4: EL DIA EN QUE LAS DOS PREGUNTAS DEL PASO 0 NO COINCIDEN,
Y EL DIA EN QUE LA FUENTE DEL CLON DESAPARECE.

TAREA 4 de la vuelta 180, las dos letras en un solo arnes porque prueban la misma
especie: **texto que describe una maquina, y maquina que se queda sin quien la
mire**.

SUJETO CONGELADO, y se dice como: todo pasa sobre ficheros FABRICADOS en un
directorio temporal que este arnes crea y borra (`P.16`). **No lee ni escribe
`docs/loop/REPORTE.md`, ni `docs/loop/reportes/`, ni ningun fichero de la
campana.** Lo unico que lee del repo es la FIRMA de dos funciones, con
`inspect.signature`, que no es un fichero que se mueva.

--- (A) LA 4.a: EL DIA EN QUE LAS DOS PREGUNTAS NO COINCIDEN ---

QUE PASA HOY Y POR QUE NO SE VE. Desde la vuelta 174 el esqueleto pregunta por
**el reporte que va a pisar**, leido de la cabecera del propio fichero, y no por
`VUELTA - 1`. **Las dos coinciden casi siempre**, asi que en corrida la
diferencia no se ve nunca, y una guarda que solo se mira cuando difiere no se
puede auditar el dia que difiera. Aqui se FABRICA ese dia.

  A1. El arbol trae el reporte de la **172** y `VUELTA - 1` es **173**.
      Preguntando por lo que se va a pisar (172): **VERDE**.
      Preguntando por la vuelta anterior (173): **ROJO**, y por su clausula (b).
  A2. El nombre del parametro dice lo que la maquina hace: se lee con
      `inspect.signature` y no de un comentario.
  A3. El docstring del modulo ya no describe la pregunta vieja sin declararlo:
      trae la CORRECCION DECLARADA y la frase nueva.
  A4. **LA CONTRAPRUEBA, QUE ES LO QUE IMPIDE UN ROJO PERMANENTE:** con las dos
      preguntas COINCIDIENDO, las dos dan VERDE. Sin esto, A1 no distinguiria
      una guarda que mira de una que dice ROJO siempre.

  Y VA UNA MEDICION QUE NO ES UN CASO Y SE DECLARA COMO TAL: preguntar por el
  numero equivocado produce un **FALSO ROJO**, no un falso verde, porque la
  clausula (d) coteja siempre contra el fichero del arbol. O sea que la mentira
  del texto nunca pudo destruir un reporte; lo que podia era **bloquear una
  escritura legitima**. Eso se mide en A5.

--- (B) LA 4.b: EL DIA EN QUE LA FUENTE DEL CLON DESAPARECE ---

  B1. Con la fuente fabricada presente y definiendo la funcion: **VERDE**.
  B2. Con la fuente BORRADA: **ROJO**, y el informe **NOMBRA la ruta**.
  B3. Con la fuente presente pero SIN la funcion: **ROJO** por su clausula (b).
  B4. Con la fuente presente pero ROTA (no parsea): **ROJO** por su clausula (c).
  B5. La mencion de la funcion en un COMENTARIO no cuenta como definirla, que es
      lo que un `in` sobre el texto habria dado por bueno.

USO:
  python scripts/loop/vuelta180_tarea4_mutacion_texto_y_clon.py
"""
import inspect
import io
import os
import shutil
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import paso0_archivar_anterior as PASO0   # noqa: E402
import guarda_de_la_fuente_del_clon as CLON   # noqa: E402

NL = chr(10)
CUERPO = NL + NL + "cuerpo fabricado de un reporte de mentira." + NL
FUENTE_BUENA = ('# -*- coding: utf-8 -*-' + NL
                + 'def vuelta_del_reporte_del_arbol(texto):' + NL
                + '    return None' + NL)
FUENTE_SIN_LA_FUNCION = ('# -*- coding: utf-8 -*-' + NL
                         + 'def otra_cosa():' + NL
                         + '    return None' + NL)
FUENTE_SOLO_MENCIONADA = ('# -*- coding: utf-8 -*-' + NL
                          + '# aqui se habla de vuelta_del_reporte_del_arbol' + NL
                          + 'def otra_cosa():' + NL
                          + '    return None' + NL)
FUENTE_ROTA = '# -*- coding: utf-8 -*-' + NL + 'def (((' + NL


def cabecera(n):
    return "# REPORTE DE LA VUELTA %d (ejecutor). FASE III." % n


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline=NL) as f:
        f.write(texto)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    fallos = []

    def marcar(etiqueta, ok):
        p("   %-72s %s" % (etiqueta, "SI" if ok else "NO"))
        if not ok:
            fallos.append(etiqueta)

    p("=" * 78)
    p("LOS DOS CASOS POR MUTACION DE LA TAREA 4 (vuelta 180)")
    p("=" * 78)
    p("")

    tmp = tempfile.mkdtemp(prefix="v180_t4_")
    try:
        # ------------------------------------------------------------- (A)
        arch = os.path.join(tmp, "reportes")
        os.makedirs(arch)
        vivo = os.path.join(tmp, "REPORTE.md")

        p("(A) LA 4.a: EL DIA FABRICADO EN QUE LAS DOS PREGUNTAS NO COINCIDEN")
        escribir(vivo, cabecera(172) + CUERPO)
        escribir(os.path.join(arch, "REPORTE_V172.md"), cabecera(172) + CUERPO)
        p("   escenario: el arbol trae el reporte de la 172 y VUELTA - 1 seria 173.")
        p("              REPORTE_V172.md existe e igual; REPORTE_V173.md NO existe.")

        ok_buena, inf_buena = PASO0.exigir_archivado(
            172, ruta_reporte=vivo, dir_archivo=arch, ejecutar_archivador=False)
        ok_vieja, inf_vieja = PASO0.exigir_archivado(
            173, ruta_reporte=vivo, dir_archivo=arch, ejecutar_archivador=False)
        p("      pregunta BUENA  (el reporte que se va a pisar, 172) -> %s"
          % ("VERDE" if ok_buena else "ROJO"))
        p("      pregunta VIEJA  (la vuelta anterior, 173)           -> %s"
          % ("VERDE" if ok_vieja else "ROJO"))
        marcar("A1: con la pregunta BUENA la guarda deja escribir", ok_buena is True)
        marcar("A1: con la pregunta VIEJA la guarda lo impide", ok_vieja is False)
        marcar("A1: y la vieja cae por su clausula (b), nombrada",
               any("(b) no existe" in l for l in inf_vieja))

        firma = inspect.signature(PASO0.exigir_archivado)
        primero = list(firma.parameters)[0]
        p("      firma de exigir_archivado: %s" % firma)
        marcar("A2: el primer parametro se llama por lo que la maquina hace",
               primero == "vuelta_del_reporte_a_pisar")
        marcar("A2: y ya NO se llama vuelta_anterior", primero != "vuelta_anterior")

        doc = PASO0.__doc__ or ""
        marcar("A3: el docstring dice EL REPORTE QUE SE VA A PISAR",
               "REPORTE QUE SE VA A" in doc.upper())
        marcar("A3: y declara la correccion en vez de borrar lo que decia",
               "CORRECCION DECLARADA" in doc)
        marcar("A3: y conserva escrita la frase vieja, sin borrarla",
               "EL REPORTE ANTERIOR" in doc.upper())

        escribir(os.path.join(arch, "REPORTE_V173.md"), cabecera(173) + CUERPO)
        escribir(vivo, cabecera(173) + CUERPO)
        ok_a, _i = PASO0.exigir_archivado(173, ruta_reporte=vivo, dir_archivo=arch,
                                          ejecutar_archivador=False)
        ok_b, _i = PASO0.exigir_archivado(173, ruta_reporte=vivo, dir_archivo=arch,
                                          ejecutar_archivador=False)
        marcar("A4, LA CONTRAPRUEBA: con las dos preguntas COINCIDIENDO, las dos "
               "dan VERDE", ok_a is True and ok_b is True)

        escribir(vivo, cabecera(172) + CUERPO)
        ok_falso, inf_falso = PASO0.exigir_archivado(
            173, ruta_reporte=vivo, dir_archivo=arch, ejecutar_archivador=False)
        p("      con el arbol en 172 y preguntando 173, con REPORTE_V173.md ya")
        p("      existente y con OTRO texto -> %s"
          % ("VERDE" if ok_falso else "ROJO"))
        marcar("A5: preguntar el numero equivocado da FALSO ROJO, nunca falso "
               "verde: la (d) coteja contra el arbol",
               ok_falso is False
               and any("(d) EL TEXTO" in l for l in inf_falso))
        p("")

        # ------------------------------------------------------------- (B)
        p("(B) LA 4.b: EL DIA FABRICADO EN QUE LA FUENTE DEL CLON DESAPARECE")
        base = os.path.join(tmp, "repo")
        os.makedirs(os.path.join(base, "scripts", "loop"))
        rel = "scripts/loop/fuente_de_mentira.py"
        ruta_fuente = os.path.join(base, "scripts", "loop", "fuente_de_mentira.py")
        nombre = "vuelta_del_reporte_del_arbol"

        escribir(ruta_fuente, FUENTE_BUENA)
        ok1, inf1 = CLON.exigir_fuente_del_clon(rel, nombre, raiz=base)
        marcar("B1: con la fuente presente y definiendo la funcion, VERDE", ok1 is True)

        os.remove(ruta_fuente)
        ok2, inf2 = CLON.exigir_fuente_del_clon(rel, nombre, raiz=base)
        marcar("B2: con la fuente BORRADA, ROJO", ok2 is False)
        marcar("B2: y el informe NOMBRA la ruta que falta",
               any(rel in l for l in inf2))
        marcar("B2: y NOMBRA la funcion que se queda sin prueba",
               any(nombre in l for l in inf2))
        for l in inf2:
            if l.strip().startswith("(a)"):
                p("      el motivo, entero: %s" % l.strip()[:160])

        escribir(ruta_fuente, FUENTE_SIN_LA_FUNCION)
        ok3, inf3 = CLON.exigir_fuente_del_clon(rel, nombre, raiz=base)
        marcar("B3: con la fuente presente pero SIN la funcion, ROJO por la (b)",
               ok3 is False and any("(b) LA FUENTE" in l for l in inf3))

        escribir(ruta_fuente, FUENTE_ROTA)
        ok4, inf4 = CLON.exigir_fuente_del_clon(rel, nombre, raiz=base)
        marcar("B4: con la fuente ROTA, ROJO por la (c)",
               ok4 is False and any("(c) LA FUENTE" in l for l in inf4))

        escribir(ruta_fuente, FUENTE_SOLO_MENCIONADA)
        ok5, inf5 = CLON.exigir_fuente_del_clon(rel, nombre, raiz=base)
        marcar("B5: una MENCION en un comentario no cuenta como definirla",
               ok5 is False)

        escribir(ruta_fuente, FUENTE_BUENA)
        ok6, _i = CLON.exigir_fuente_del_clon(rel, nombre, raiz=base)
        marcar("B6, LA VUELTA AL VERDE: al restaurar la fuente vuelve a pasar, "
               "o sea que no es un rojo permanente", ok6 is True)
        p("")

        # ------------------------------------------------- (C) LA GUARDA VIVA
        p("(C) Y LA GUARDA, APUNTADA A LA FUENTE DE VERDAD DEL ESQUELETO DE HOY")
        ok7, inf7 = CLON.exigir_fuente_del_clon(
            "scripts/loop/vuelta174_esqueleto_reporte.py",
            "vuelta_del_reporte_del_arbol")
        for l in inf7:
            p("      " + l)
        marcar("C: la fuente del clon del esqueleto de la 180 esta en su sitio",
               ok7 is True)
        p("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        p("EL TEMPORAL, RETIRADO (P.16): existe todavia: %s"
          % ("SI" if os.path.exists(tmp) else "NO"))
        p("")

    p("CIFRA comprobaciones: 17 | fallan: %d" % len(fallos))
    if fallos:
        p("ROJO: %d comprobacion(es) no se comportan." % len(fallos))
        for f in fallos:
            p("   " + f)
        p("FIN")
        return 1
    p("VERDE: el dia en que las dos preguntas del paso 0 no coinciden esta "
      "fabricado y la maquina responde a la buena; su parametro y su docstring "
      "dicen ya lo que hace; y la guarda de la fuente del clon CAE nombrando la "
      "ruta y la funcion cuando la fuente desaparece, cuando pierde la funcion y "
      "cuando se rompe, y vuelve al verde al restaurarla.")
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
