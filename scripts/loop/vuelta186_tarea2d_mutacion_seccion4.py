# -*- coding: utf-8 -*-
r"""vuelta186_tarea2d_mutacion_seccion4.py . EL CASO POSITIVO POR MUTACION DE LA
GUARDA QUE COTEJA LA SECCION 4 DEL REPORTE CONTRA LA APERTURA SELLADA.

QUIEN LA ENCARGA, Y NO ES UNA MEJORA. `AUDITOR.md` 1.2 obliga a encargar la
escalada cuando la racha de caidas de reporte llega a dos, y el acta 186 la deja
en dos y la encarga en su seccion 9: *"la `R.1` de hoy y la cifra no verificable
de las 15 lineas son LA MISMA ENFERMEDAD: cifras del estado del arbol tecleadas
en la prosa del cierre en vez de leidas de la apertura sellada"*.

QUE PRUEBA, CASO A CASO, Y TODOS TIENEN QUE CAER AL MUTAR SU ESPERADO:
  (A) LAS DOS CIFRAS CALZANDO: verde, sin ningun motivo.
  (B) LA DE STATUS MUTADA: rojo, Y EL MOTIVO LA NOMBRA, con las dos cifras y las
      dos sedes.
  (C) LA DE NUMSTAT MUTADA: rojo.
  (D) LA SECCION 4 SIN AFIRMAR NINGUNA DE LAS DOS: rojo, Y CON SU PROPIO TEXTO.
      Una cifra ausente y una cifra que calza NO son lo mismo, y una guarda que
      se pusiera verde ante el silencio seria peor que no tenerla.
  (E) LA APERTURA QUE NO PUBLICA UNA DE LAS DOS: rojo. Sin vara no hay cotejo.
  (F) EL CASO REAL DE LA `R.1`, sobre los FICHEROS REALES de la vuelta 185:
      `docs/loop/reportes/REPORTE_V185.md` y `docs/loop/SALIDA_V185_APERTURA.txt`.
      SE EXIGE QUE LA GUARDA LA HUBIERA CAZADO. **Si no caza el caso que la trajo,
      no sirve**, y por eso este caso no es opcional.
  (G) EL SALTO DE RENGLON: la `R.1` esta escrita con el marcador al final de una
      linea y el `cero` al principio de la siguiente. Se prueba que la guarda
      cruza ese salto, porque una que no lo cruzara se comeria la mitad del caso
      que la trajo.

LOS TEXTOS SE FABRICAN EN MEMORIA salvo en el caso (F), que abre los dos ficheros
reales SOLO PARA LEER. Este arnes no escribe ningun reporte y no toca
`docs/loop/REPORTE.md`.

USO:
  python scripts/loop/vuelta186_tarea2d_mutacion_seccion4.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
REP185 = os.path.join(LOOP, "reportes", "REPORTE_V185.md")
NOM_FALSA = "docs/loop/SALIDA_V999_APERTURA.txt"


def apertura_fabricada(status=1, numstat=0, sin_status=False, sin_numstat=False):
    """UNA APERTURA DE MENTIRA CON LAS DOS ETIQUETAS EXACTAS. PURA."""
    L = ["SELLO DE APERTURA DE LA VUELTA 999, fabricado.", "",
         "=== C. git status --porcelain ENTERO ==="]
    if not sin_status:
        L.append("CIFRA lineas de status: %d" % status)
    L += ["", "=== E. DIFF REAL EN BYTES ==="]
    if not sin_numstat:
        L.append("CIFRA filas de `git diff --numstat -- dataset/` AL ENTRAR: %d"
                 % numstat)
    L.append("")
    return NL.join(L) + NL


def reporte_fabricado(cuerpo_de_la_4):
    """UN REPORTE DE MENTIRA CON SU SECCION 4. PURA."""
    L = ["# REPORTE DE LA VUELTA 999 (fabricado)", "",
         "## 3. UNA SECCION CUALQUIERA", "", "Y su cuerpo.", "",
         "## 4. LA GUARDA DEL COMMIT DE `dataset/`, DE MENTIRA", ""]
    L += list(cuerpo_de_la_4)
    L += ["", "## 5. OTRA SECCION", "", "Y su cuerpo.", ""]
    return NL.join(L) + NL


PROSA_BUENA = [
    "`git status --porcelain` da **1 linea** al abrir, medida en el bloque de",
    "apertura antes de la primera operacion, y",
    "`git diff --numstat -- dataset/` da **0 filas** AL ENTRAR.",
]
PROSA_PARTIDA = [
    "El arbol abrio limpio, con `git status --porcelain` en",
    "una linea, cosa que el docstring predijo antes de medirla.",
    "Y `git diff --numstat -- dataset/` da **0 filas**.",
]
PROSA_MUDA = [
    "Ninguna perdida de catalogo que declarar, y `dataset/` no se commitea en",
    "esta vuelta. Aqui no se afirma ninguna cifra del estado del arbol.",
]
PROSA_CERCADA = [
    "La cifra va pegada del instrumento y no tecleada:", "",
    "```",
    "CIFRA lineas de status: 1",
    "`git status --porcelain` da 99 lineas segun esta cita",
    "```", "",
]


def _casos_fabricados(w):
    """A, B, C, D, E Y G, todos sobre textos fabricados en memoria."""
    fallos = casos = caen = 0
    ap = apertura_fabricada(status=1, numstat=0)
    escenarios = [
        ("A. las dos cifras calzando", reporte_fabricado(PROSA_BUENA), ap, 0, None),
        ("B. la de status MUTADA (la apertura dice 7)",
         reporte_fabricado(PROSA_BUENA), apertura_fabricada(status=7, numstat=0),
         1, "CIFRA lineas de status"),
        ("C. la de numstat MUTADA (la apertura dice 4)",
         reporte_fabricado(PROSA_BUENA), apertura_fabricada(status=1, numstat=4),
         1, "numstat"),
        ("D. la seccion 4 sin afirmar NINGUNA",
         reporte_fabricado(PROSA_MUDA), ap, 2, "NO AFIRMA NADA"),
        ("E. la apertura sin publicar la de status",
         reporte_fabricado(PROSA_BUENA), apertura_fabricada(sin_status=True),
         1, "NO publica"),
        ("G. la frase partida en dos renglones (la forma de la R.1)",
         reporte_fabricado(PROSA_PARTIDA), ap, 0, None),
        ("G.1 la misma frase partida, con la apertura en 9",
         reporte_fabricado(PROSA_PARTIDA), apertura_fabricada(status=9, numstat=0),
         1, "CIFRA lineas de status"),
        ("G.2 la cifra citada DENTRO de una cerca no cuenta",
         reporte_fabricado(PROSA_CERCADA + PROSA_BUENA), ap, 0, None),
    ]
    for etiqueta, rep, apt, esperado, aguja in escenarios:
        motivos = CR.seccion4_que_no_calza(rep, apt, NOM_FALSA)
        casos += 1
        w("   %-52s -> %d motivo(s) | esperado %d | %s"
          % (etiqueta, len(motivos), esperado,
             "CALZA" if len(motivos) == esperado else "NO CALZA"))
        for m in motivos:
            w("      | " + m[:150])
        if len(motivos) != esperado:
            fallos += 1
        if aguja is not None:
            nombra = any(aguja in m for m in motivos)
            w("      el motivo NOMBRA %r: %s" % (aguja, "SI" if nombra else "NO"))
            if not nombra:
                fallos += 1
        w("      MUTACION del esperado (exigir %d motivos): %s"
          % (esperado + 1, "PASA" if len(motivos) == esperado + 1 else "CAE"))
        if len(motivos) == esperado + 1:
            fallos += 1
        else:
            caen += 1
    w("")
    w("   Y LAS DOS SEDES VAN NOMBRADAS EN EL MOTIVO DE LA DISCREPANCIA:")
    motivos = CR.seccion4_que_no_calza(reporte_fabricado(PROSA_BUENA),
                                       apertura_fabricada(status=7, numstat=0),
                                       NOM_FALSA)
    casos += 1
    las_dos = bool(motivos) and ("SEDE DEL REPORTE" in motivos[0]
                                 and "SEDE DE LA APERTURA" in motivos[0]
                                 and NOM_FALSA in motivos[0])
    w("      el motivo nombra las DOS sedes: %s" % ("SI" if las_dos else "NO"))
    w("      motivo entero: %s" % (motivos[0] if motivos else "(ninguno)"))
    if not las_dos:
        fallos += 1
    w("      MUTACION del esperado (exigir que NO las nombre): %s"
      % ("PASA" if not las_dos else "CAE"))
    if las_dos:
        caen += 1
    else:
        fallos += 1
    w("")
    return fallos, casos, caen


def _caso_real(w):
    """F: los ficheros REALES de la 185. Si no caza la R.1, no sirve."""
    fallos = casos = caen = 0
    w("   F. EL CASO REAL DE LA `R.1`, SOBRE LOS FICHEROS REALES DE LA 185")
    w("      (si esta guarda no caza el caso que la trajo, no sirve)")
    if not os.path.exists(REP185):
        w("      docs/loop/reportes/REPORTE_V185.md NO EXISTE. Sin el no hay caso")
        w("      real, y eso se dice en vez de fabricar uno.")
        return 1, 1, 0
    rep = io.open(REP185, encoding="utf-8", errors="replace").read()
    nombre_ap, texto_ap = CR.lector_de_la_apertura(185)
    w("      reporte: docs/loop/reportes/REPORTE_V185.md, %d bytes en disco y %d "
      "normalizados a LF"
      % (os.path.getsize(REP185),
         len(rep.replace(chr(13) + NL, NL).encode("utf-8"))))
    if texto_ap is None:
        w("      %s NO EXISTE. Sin la apertura sellada no hay vara." % nombre_ap)
        return 1, 1, 0
    w("      apertura: %s, %d bytes en disco y %d normalizados a LF"
      % (nombre_ap,
         os.path.getsize(os.path.join(RAIZ, nombre_ap.replace("/", os.sep))),
         len(texto_ap.encode("utf-8"))))
    vara = CR.cifras_de_la_apertura(texto_ap)
    w("      LO QUE LA APERTURA SELLADA DE LA 185 PUBLICA:")
    w("         CIFRA lineas de status: %s" % vara["status"])
    w("         CIFRA filas de numstat AL ENTRAR: %s" % vara["numstat"])
    afirma = CR.cifras_que_afirma_la_seccion4(rep)
    w("      LO QUE LA SECCION 4 DEL REPORTE DE LA 185 AFIRMA:")
    for especie in ("status", "numstat"):
        for n, valor, renglon in afirma[especie]:
            w("         %-8s -> %d, linea %d: %s" % (especie, valor, n, renglon[:88]))
        if not afirma[especie]:
            w("         %-8s -> (no afirma nada)" % especie)
    motivos = CR.seccion4_que_no_calza(rep, texto_ap, nombre_ap)
    casos += 1
    w("      CIFRA motivos en rojo sobre el caso real: %d" % len(motivos))
    for m in motivos:
        w("         | " + m[:160])
    caza = len(motivos) >= 1 and any("CIFRA lineas de status" in m for m in motivos)
    w("      LA GUARDA HUBIERA CAZADO LA R.1: %s" % ("SI" if caza else "NO"))
    if not caza:
        fallos += 1
    w("      MUTACION del esperado (exigir 0 motivos, o sea que NO la cazara): %s"
      % ("PASA" if not motivos else "CAE"))
    if not motivos:
        fallos += 1
    else:
        caen += 1
    w("      Y LA DE numstat DE ESE MISMO REPORTE SI CALZA, que es lo que hace")
    w("      que este caso no sea un rojo indiscriminado:")
    casos += 1
    solo_numstat = [m for m in motivos if "numstat" in m]
    w("         motivos que nombran numstat: %d" % len(solo_numstat))
    w("         ESPERADO 0 -> %s" % ("CALZA" if not solo_numstat else "NO CALZA"))
    if solo_numstat:
        fallos += 1
    w("         MUTACION del esperado (exigir 1): %s"
      % ("PASA" if len(solo_numstat) == 1 else "CAE"))
    if len(solo_numstat) == 1:
        fallos += 1
    else:
        caen += 1
    w("")
    return fallos, casos, caen


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DE LA GUARDA DE LA SECCION 4")
    w("(vuelta 186, TAREA 2.d; escalada de AUDITOR.md 1.2 contra la R.1 del")
    w("acta 186, con la racha de reporte en dos)")
    w("=" * 78)
    w("")
    w("EL SUJETO ES EL FICHERO VIVO scripts/loop/cerrar_reporte.py, IMPORTADO.")
    w("")
    fallos = casos = caen = 0
    for parte in (_casos_fabricados, _caso_real):
        f, c, k = parte(w)
        fallos += f
        casos += c
        caen += k
    w("CIFRA casos: %d | pasan: %d" % (casos, casos - fallos))
    w("CIFRA casos que CAEN al mutar su esperado: %d de %d" % (caen, caen))
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V186_T2D_MUTACION_SECCION4.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
