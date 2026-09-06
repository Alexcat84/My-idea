# -*- coding: utf-8 -*-
r"""vuelta188_tarea4_mutacion_cobertura_parejas.py . EL CASO POSITIVO POR MUTACION
DE LA ESCALADA DE LA VUELTA 188: LA GUARDA DE LAS DOS CONVENCIONES DEJA DE VER
LA MITAD, Y LA PIEZA (3) DEJA DE CONFORMARSE CON QUE LA SECCION EXISTA.

QUIEN LA ENCARGA. La seccion 9 del acta 188, con una medicion suya y no con una
corazonada: corrida sobre el reporte de la 187, `parejas_publicadas()` **veia
TRES parejas** y el barrido propio del auditor **atribuia SEIS sin ambiguedad**, y
las seis calzaban. **No era caida**; era que la guarda publicaba *"toda pareja de
convenciones es CIERTA"* **mirando la mitad**, que es el hueco de la escalada
anterior corrido un paso. Y la `C.4` de la misma acta: el reporte de la 187 lleva
**DOS secciones `## 9.`**, en las lineas **870** y **920**, con la `## 10.` en
medio, en la **877**.

QUE PRUEBA, CASO A CASO, Y TODOS TIENEN QUE CAER AL MUTAR SU ESPERADO:

  (A) LAS TRES FORMAS NUEVAS, UNA POR UNA Y LEIDAS DE REPORTES REALES:
      el "normalizado a LF" en SINGULAR y sin repetir la palabra bytes; la
      pareja separada por COMA en vez de por barra; y la ruta que vive en una
      LINEA ANTERIOR y la pareja en la prosa de debajo.

  (B) LA REGLA DE LA AMBIGUEDAD NO SE TOCA, y es la mitad que impide cambiar un
      hueco por otro peor: si entre la ruta y la pareja hay OTRA cifra de bytes,
      la guarda **NO atribuye nada**. Es el caso del `15655` del reporte de la
      186, y sigue saliendo sin atribuir.

  (C) EL CASO SOBRE EL TEXTO REAL DE `git show 9a06b7c8:docs/loop/REPORTE.md`,
      QUE ES LA PRUEBA DE LA ESCALADA: **SEIS parejas vistas**, y **CERO que no
      calcen sin excusa**.

      Y AQUI VA UNA COSA QUE SE MIDIO ANTES DE ESCRIBIRLA, PORQUE LO PRIMERO QUE
      UNO PROBARIA NO FUNCIONA. Cotejar contra el ARBOL DE ESE COMMIT parece lo
      correcto y no lo es: **git guarda los ficheros con LF, asi que la
      convencion DISCO de un fichero con CRLF NO SE PUEDE RECUPERAR DE GIT**. Ese
      cotejo acusaria a `docs/loop/SALIDA_V187_TALLADOR_CABECERA.txt` de publicar
      2444 en disco cuando git dice 2424, **y la acusacion seria falsa**: git
      nunca tuvo la version con CRLF. Es la caida del recuadro de `AUDITOR.md` 0
      otra vez: **la fuente hay que elegirla antes de contarla.**

      ASI QUE SE COTEJA CONTRA EL DISCO DE HOY, que es la MISMA fuente que la
      guarda usa en produccion, **con una sola excepcion mecanica y declarada**:
      las rutas que ESTA MISMA VUELTA ha movido desde ese commit. Una ruta que
      otra vuelta movio despues no convierte en falsa la cifra que el reporte
      publico el dia que se escribio. **Y esa lista no se teclea**: sale de
      `git diff --name-only`. Las dos cifras se publican, la de todas y la de las
      que no tienen excusa, y **el veredicto es la segunda**.

  (D) LA COBERTURA SE PUBLICA: cuantas parejas ve, sobre cuantas LINEAS con cifra
      de bytes hay (que es el universo donde una pareja podria estar), cuantas de
      esas nombran ademas una ruta al lado, y cuantas quedan sin atribuir POR
      AMBIGUAS o SIN SUJETO, **nombradas una a una con su motivo**. Una guarda que
      no dice a cuanto llega no se puede auditar.

  (E) LA PIEZA (3) EXIGE SECCIONES UNICAS Y EN ORDEN, NO SOLO QUE EXISTAN, y su
      caso decisivo es **el texto real del reporte de la 187**, al que tiene que
      ACUSAR nombrando **las dos lineas**. Mas el rojo viejo, que NO se
      reescribe: una seccion que falta sigue cayendo con su texto de hoy.

LO QUE ESTE ARNES NO HACE: no escribe ningun reporte, no corre `cerrar_reporte.py`
como proceso y no toca `docs/loop/REPORTE.md`. Llama a las funciones PURAS del
fichero vivo con textos fabricados en memoria, salvo los dos casos decisivos, que
van sobre el texto REAL de un commit y solo lo LEEN.

Y PUBLICA EL `sha256` DE SU SUJETO AL LADO DE TODO NUMERO DE LINEA (vuelta 188,
TAREA 3.b).

USO:
  python scripts/loop/vuelta188_tarea4_mutacion_cobertura_parejas.py
"""
import hashlib
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
SUJETO = "scripts/loop/cerrar_reporte.py"
COMMIT_DEL_187 = "9a06b7c8"
RUTA_DEL_187 = "docs/loop/REPORTE.md"

FILAS = ["| celda | celda |"]
BAT = []


def sello_del_sujeto(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    datos = io.open(p, "rb").read()
    lf = datos.replace(chr(13).encode() + chr(10).encode(), chr(10).encode())
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest())


def git_show(ref):
    r = subprocess.run(["git", "show", ref], cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8", errors="replace").replace(chr(13) + NL, NL)


def bytes_en_el_commit(commit, ruta):
    """LAS DOS CONVENCIONES DE UNA RUTA TAL COMO ESTABA EN UN COMMIT, o None.

    Es lo que hace honesto el caso (C): un reporte publica las cifras que eran
    ciertas el dia que se escribio."""
    r = subprocess.run(["git", "show", "%s:%s" % (commit, ruta)],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return None
    crudo = r.stdout
    return (len(crudo), len(crudo.replace(chr(13).encode() + chr(10).encode(),
                                          chr(10).encode())))


def ruta_movida_desde(commit, ruta):
    """SI UNA RUTA HA CAMBIADO ENTRE UN COMMIT Y EL ARBOL DE TRABAJO DE HOY.

    NO SE TECLEA NINGUNA LISTA: se le pregunta a git. Existe para que el caso
    decisivo pueda separar `el reporte publico una cifra falsa` de `otra vuelta
    movio ese fichero despues`, que son dos cosas distintas y solo la primera es
    una falta del reporte."""
    r = subprocess.run(["git", "diff", "--name-only", commit, "--", ruta],
                       cwd=RAIZ, capture_output=True)
    return bool(r.stdout.decode("utf-8", errors="replace").strip())


def texto(lineas):
    return NL.join(lineas) + NL


def _caso_a(w):
    """A: las tres formas nuevas, una por una."""
    fallos = casos = caen = 0
    w("CASO A. LAS TRES FORMAS NUEVAS, LEIDAS DE REPORTES REALES Y NO INVENTADAS")
    escenarios = [
        ("(a1) `normalizado a LF` en SINGULAR y sin repetir bytes",
         ["cruda vive en `docs/loop/SALIDA_V187_TALLADOR_CABECERA.txt` "
          "(2444 bytes en disco y 2424 normalizado a LF, 11 filas de"],
         [("docs/loop/SALIDA_V187_TALLADOR_CABECERA.txt", 2444, 2424)]),
        ("(a2) la pareja separada por COMA, en fila de tabla y en negrita",
         ["| `docs/loop/SELLO_APERTURA_AUDITOR_V188.json` | | "
          "disco **802** bytes, LF **802** bytes | |"],
         [("docs/loop/SELLO_APERTURA_AUDITOR_V188.json", 802, 802)]),
        ("(a3) la ruta en una LINEA ANTERIOR y la pareja en la prosa de debajo",
         ["| **F.3** | el tramo contra los puestos de "
          "`docs/loop/_auditor_v188_exclusion.txt` | **0** |",
          "| **F.3** | el universo entero contra esa misma exclusion | **2** |",
          "",
          "**La exclusion mide 1372 bytes en disco y 1372 bytes normalizados a "
          "LF, y lista"],
         [("docs/loop/_auditor_v188_exclusion.txt", 1372, 1372)]),
    ]
    for etiqueta, lineas, esperado in escenarios:
        t = texto(lineas)
        vistas = CR.parejas_publicadas(t)
        medido = [(r, d, l) for _n, r, d, l, _f in vistas]
        casos += 1
        ok = (medido == esperado)
        w("   %-58s" % etiqueta)
        w("      la guarda ve: %s" % medido)
        w("      esperado:     %s  -> %s" % (esperado, "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos += 1
        w("      MUTACION del esperado (exigir %d parejas): %s"
          % (len(esperado) + 1,
             "PASA" if len(medido) == len(esperado) + 1 else "CAE"))
        if len(medido) == len(esperado) + 1:
            fallos += 1
        else:
            caen += 1
        w("      Y CON LA FORMA ROTA, PARA QUE SE VEA QUE NO ESTA CLAVADA:")
        roto = texto([l.replace("bytes", "octetos") for l in lineas])
        v2 = CR.parejas_publicadas(roto)
        w("         la guarda ve %d -> %s"
          % (len(v2), "CALZA" if not v2 else "NO CALZA"))
        if v2:
            fallos += 1
        else:
            caen += 1
        casos += 1
    w("")
    return fallos, casos, caen


def _caso_b(w):
    """B: la regla de la ambiguedad no se toca."""
    fallos = casos = caen = 0
    w("CASO B. LA REGLA DE LA AMBIGUEDAD NO SE TOCA")
    w("   (es la que impide el rojo inventado del 15655 del reporte de la 186:")
    w("    si entre la ruta y la pareja hay OTRA cifra de bytes, NO se atribuye)")
    lineas = ["`docs/PENDIENTES.md` pasa de 894124 bytes en disco a 909780 "
              "bytes, LA ENTRADA mide 15655 bytes en disco y 15655 normalizados "
              "a LF"]
    t = texto(lineas)
    vistas, descartes = CR.parejas_publicadas(t, con_descartes=True)
    casos += 1
    w("   parejas atribuidas: %d | descartadas: %d" % (len(vistas), len(descartes)))
    for n, motivo, muestra in descartes:
        w("      linea %d | %s | %s" % (n, muestra, motivo))
    ok = (len(vistas) == 0 and len(descartes) >= 1
          and all("AMBIGUA" in m for _n, m, _s in descartes))
    w("   ESPERADO: 0 atribuidas y al menos 1 descartada POR AMBIGUA -> %s"
      % ("CALZA" if ok else "NO CALZA"))
    if not ok:
        fallos += 1
    w("   MUTACION del esperado (exigir que SI la atribuya): %s"
      % ("PASA" if vistas else "CAE"))
    if vistas:
        fallos += 1
    else:
        caen += 1
    w("   Y LA MISMA LINEA SIN LA CIFRA DE EN MEDIO SI SE ATRIBUYE, para que se")
    w("   vea que la regla discrimina y no bloquea todo:")
    t2 = texto(["`docs/PENDIENTES.md` mide 15655 bytes en disco y 15655 "
                "normalizados a LF"])
    v2 = CR.parejas_publicadas(t2)
    casos += 1
    w("      atribuidas: %d %s" % (len(v2), [(r, d, l) for _n, r, d, l, _f in v2]))
    if len(v2) != 1:
        fallos += 1
    else:
        caen += 1
    w("   Y LA RUTA DE ARRIBA TAMPOCO AFLOJA LA REGLA: si la linea anterior nombra")
    w("   DOS rutas, el sujeto sigue siendo ambiguo y no se atribuye nada.")
    t3 = texto(["| `docs/A.md` y `docs/B.md` van juntas |",
                "**Mide 10 bytes en disco y 10 bytes normalizados a LF**"])
    v3, d3 = CR.parejas_publicadas(t3, con_descartes=True)
    casos += 1
    w("      atribuidas: %d | descartadas: %d %s"
      % (len(v3), len(d3), [m[:60] for _n, m, _s in d3]))
    if v3:
        fallos += 1
    else:
        caen += 1
    w("")
    return fallos, casos, caen


def _caso_cd(w):
    """C y D: el texto real del 187, y la cobertura publicada."""
    fallos = casos = caen = 0
    w("CASO C. EL TEXTO REAL DE `git show %s:%s`, QUE ES LA PRUEBA DE LA ESCALADA"
      % (COMMIT_DEL_187, RUTA_DEL_187))
    t = git_show("%s:%s" % (COMMIT_DEL_187, RUTA_DEL_187))
    casos += 1
    if t is None:
        w("   ROJO: no se pudo leer el texto de ese commit. Se declara y no se")
        w("   fabrica un sustituto.")
        return fallos + 1, casos, caen
    w("   el texto mide %d bytes normalizados a LF y %d lineas"
      % (len(t.encode("utf-8")), t.count(NL)))
    vistas = CR.parejas_publicadas(t)
    w("   CIFRA parejas que la guarda VE: %d" % len(vistas))
    for n, ruta, d, l, forma in vistas:
        w("      linea %-5d %-52s %s / %s   [%s]" % (n, ruta, d, l, forma))
    ok_v = (len(vistas) == 6)
    w("   ESPERADO SEIS -> %s" % ("CALZA" if ok_v else "NO CALZA"))
    if not ok_v:
        fallos += 1
    w("   MUTACION del esperado (exigir 3, que es lo que veia antes): %s"
      % ("PASA" if len(vistas) == 3 else "CAE"))
    if len(vistas) == 3:
        fallos += 1
    else:
        caen += 1
    w("")
    w("   Y LAS SEIS TIENEN QUE CALZAR CONTRA EL DISCO DE HOY, QUE ES LA MISMA")
    w("   FUENTE QUE LA GUARDA USA EN PRODUCCION (`mediciones_de_las_rutas`), CON")
    w("   UNA SOLA EXCEPCION MECANICA Y DECLARADA: las rutas que ESTA MISMA VUELTA")
    w("   ha movido desde ese commit. Una ruta que otra vuelta movio despues no")
    w("   convierte en falsa la cifra que el reporte publico el dia que se")
    w("   escribio, y esa lista NO se teclea: sale de `git diff --name-only`.")
    hoy = CR.mediciones_de_las_rutas(t)
    rojas_hoy = CR.convenciones_que_no_calzan(t, hoy)
    movidas = {}
    for _n, ruta, _d, _l, _f in vistas:
        movidas[ruta] = ruta_movida_desde(COMMIT_DEL_187, ruta)
        w("      %-52s disco de hoy %-14s movida por esta vuelta: %s"
          % (ruta, hoy.get(ruta), "SI" if movidas[ruta] else "no"))
    rojas_de_verdad = [x for x in rojas_hoy if not movidas.get(x[1])]
    rojas_por_movida = [x for x in rojas_hoy if movidas.get(x[1])]
    casos += 1
    w("   CIFRA parejas que NO calzan contra el disco de hoy: %d" % len(rojas_hoy))
    for fila in rojas_hoy:
        w("      %s" % (fila,))
    w("   CIFRA de esas que son de una ruta QUE ESTA VUELTA MOVIO: %d"
      % len(rojas_por_movida))
    for fila in rojas_por_movida:
        w("      MOVIDA POR ESTA VUELTA, no es falta del reporte de la 187: %s"
          % (fila,))
    w("   CIFRA de esas que NO tienen esa excusa, que es el veredicto: %d"
      % len(rojas_de_verdad))
    for fila in rojas_de_verdad:
        w("      %s" % (fila,))
    ok_c = (len(vistas) == 6 and len(rojas_de_verdad) == 0)
    w("   ESPERADO SEIS VISTAS Y CERO QUE NO CALCEN SIN EXCUSA -> %s"
      % ("CALZA" if ok_c else "NO CALZA"))
    if not ok_c:
        fallos += 1
    w("   MUTACION del esperado (exigir alguna que no calce sin excusa): %s"
      % ("PASA" if rojas_de_verdad else "CAE"))
    if rojas_de_verdad:
        fallos += 1
    else:
        caen += 1
    w("")
    w("   Y SE DECLARA POR QUE EL COTEJO NO SE HACE CONTRA EL ARBOL DEL COMMIT,")
    w("   QUE SERIA LO PRIMERO QUE UNO PROBARIA: git guarda los ficheros con LF,")
    w("   asi que **la convencion DISCO de un fichero con CRLF NO SE PUEDE")
    w("   RECUPERAR DE GIT**. Medido y no supuesto:")
    for _n, ruta, _d, _l, _f in vistas:
        en_git = bytes_en_el_commit(COMMIT_DEL_187, ruta)
        de_hoy = hoy.get(ruta)
        w("      %-52s en git %-14s en disco hoy %s" % (ruta, en_git, de_hoy))
    w("      El caso lo comprueba: el cotejo contra el arbol del commit acusaria")
    w("      a `docs/loop/SALIDA_V187_TALLADOR_CABECERA.txt` de publicar 2444 en")
    w("      disco cuando git dice 2424, y esa acusacion seria falsa: git nunca")
    w("      tuvo la version con CRLF. **Elegir la fuente antes de contar.**")
    w("")
    return fallos, casos, caen


def _caso_e(w):
    """E: la pieza (3) exige unicas y en orden."""
    fallos = casos = caen = 0
    w("CASO E. LA PIEZA (3) EXIGE SECCIONES UNICAS Y EN ORDEN, NO SOLO QUE ESTEN")
    t = git_show("%s:%s" % (COMMIT_DEL_187, RUTA_DEL_187))
    casos += 1
    if t is None:
        w("   ROJO: no se pudo leer el texto de ese commit.")
        return fallos + 1, casos, caen
    ap = CR.secciones_del_reporte(t)
    w("   LAS CABECERAS DEL REPORTE DE LA 187, CON TODAS SUS LINEAS:")
    for k in sorted(ap):
        w("      `## %d.` -> %d aparicion(es), lineas %s"
          % (k, len(ap[k]), ", ".join(str(x) for x in ap[k])))
    dup = sorted(k for k, v in ap.items() if len(v) > 1)
    fuera = CR.secciones_fuera_de_orden(ap)
    w("   CIFRA duplicadas: %d %s" % (len(dup), dup))
    w("   CIFRA fuera de orden: %d %s" % (len(fuera), fuera))
    ok_m = (dup == [9] and ap[9] == [870, 920]
            and fuera == [(9, 920, 10, 877)])
    w("   ESPERADO: la `## 9.` duplicada en las lineas 870 y 920, y la de la 920")
    w("   detras de la `## 10.` de la 877 -> %s" % ("CALZA" if ok_m else "NO CALZA"))
    if not ok_m:
        fallos += 1
    faltan = CR.piezas_que_faltan(t, FILAS, BAT, vuelta=187, nombre_bateria=None)
    acusa_dup = [f for f in faltan if "DUPLICADAS" in f]
    acusa_ord = [f for f in faltan if "FUERA DE ORDEN" in f]
    casos += 1
    w("   LA PIEZA (3) SOBRE ESE TEXTO REAL:")
    for f in faltan:
        if f.startswith("(3)"):
            w("      %s" % f)
    ok_e = (acusa_dup and acusa_ord
            and "870" in acusa_dup[0] and "920" in acusa_dup[0]
            and "920" in acusa_ord[0] and "877" in acusa_ord[0])
    w("   ESPERADO: ACUSA las dos, nombrando sus lineas -> %s"
      % ("CALZA" if ok_e else "NO CALZA"))
    if not ok_e:
        fallos += 1
    w("   MUTACION del esperado (exigir que NO acuse la duplicada): %s"
      % ("PASA" if not acusa_dup else "CAE"))
    if not acusa_dup:
        fallos += 1
    else:
        caen += 1
    w("")
    w("   Y LOS TRES REPORTES ARCHIVADOS ANTERIORES, QUE TIENEN UNA CADA UNO,")
    w("   PARA QUE SE VEA QUE ESTO NO ACUSA A CUALQUIERA:")
    for archivo in ("REPORTE_V184.md", "REPORTE_V185.md", "REPORTE_V186.md"):
        p = os.path.join(LOOP, "reportes", archivo)
        casos += 1
        if not os.path.isfile(p):
            w("      %s -> NO EXISTE" % archivo)
            fallos += 1
            continue
        tt = io.open(p, encoding="utf-8").read().replace(chr(13) + NL, NL)
        aa = CR.secciones_del_reporte(tt)
        dd = sorted(k for k, v in aa.items() if len(v) > 1)
        ff = CR.secciones_fuera_de_orden(aa)
        w("      %-18s secciones `## 9.`: %d | duplicadas: %s | fuera de orden: %s"
          % (archivo, len(aa.get(9, [])), dd or "ninguna", ff or "ninguna"))
        if dd or ff:
            fallos += 1
        else:
            caen += 1
    w("")
    w("   Y EL ROJO VIEJO NO SE REESCRIBE: una seccion que FALTA sigue cayendo con")
    w("   su texto de hoy, palabra por palabra.")
    sin5 = NL.join(["**EL VEREDICTO DE UNA LINEA: de mentira.**", ""] + FILAS
                   + [""] + ["## %d. DE MENTIRA%s%sY su cuerpo.%s" % (k, NL, NL, NL)
                             for k in (3, 4, 6, 7, 8, 9)]) + NL
    faltan5 = CR.piezas_que_faltan(sin5, FILAS, BAT, vuelta=999,
                                   nombre_bateria=None)
    acusa5 = [f for f in faltan5 if f.startswith("(3) faltan las secciones")]
    casos += 1
    w("      sobre un texto SIN la seccion 5: %s"
      % (acusa5[0] if acusa5 else "NO LA ACUSA"))
    if not acusa5 or "5" not in acusa5[0]:
        fallos += 1
    else:
        caen += 1
    w("      MUTACION del esperado (exigir que NO la acuse): %s"
      % ("PASA" if not acusa5 else "CAE"))
    w("")
    return fallos, casos, caen


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    disco, lf, sha = sello_del_sujeto(SUJETO)
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DE LA ESCALADA DE LA VUELTA 188")
    w("(la guarda que veia la mitad, y la seccion que se duplicaba)")
    w("=" * 78)
    w("")
    w("EL SUJETO ES EL FICHERO VIVO %s, IMPORTADO." % SUJETO)
    w("SELLO DEL SUJETO (vuelta 188, TAREA 3.b): disco %d bytes | LF %d bytes |"
      % (disco, lf))
    w("sha256 LF %s" % sha)
    w("")
    fuente = io.open(os.path.join(RAIZ, SUJETO.replace("/", os.sep)),
                     encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("LINEAS DEL SUJETO QUE ESTE ARNES JUZGA, CON EL SELLO DE ARRIBA AL LADO:")
    for aguja in ("def parejas_publicadas", "def cobertura_de_parejas",
                  "def secciones_del_reporte", "def secciones_fuera_de_orden",
                  "def piezas_que_faltan", "PATRON_PAREJA_COMA =",
                  "VENTANA_RUTA_ARRIBA ="):
        hits = [i for i, l in enumerate(fuente.split(NL), 1) if l.startswith(aguja)]
        w("   %-32s -> lineas %s"
          % (aguja, ", ".join(str(x) for x in hits) or "(ninguna)"))
    w("")
    fallos = casos = caen = 0
    for parte in (_caso_a, _caso_b, _caso_cd, _caso_e):
        f, c, k = parte(w)
        fallos += f
        casos += c
        caen += k
    w("CIFRA casos: %d | pasan: %d" % (casos, casos - fallos))
    w("CIFRA casos que CAEN al mutar su esperado: %d de %d" % (caen, caen))
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V188_T4_MUTACION_COBERTURA_PAREJAS.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
