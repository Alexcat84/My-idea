# -*- coding: utf-8 -*-
"""VUELTA 79, TAREA 2 punto 4: CASO POSITIVO OBLIGATORIO del modo --fase04 del
tallador. Talla la cabecera de la VUELTA 78 con las salidas SALIDA_V78_* que ya
estan en el repo (importando lado_fase04 del propio tallador, sin duplicar su
extraccion) y la coteja, cifra por cifra, contra el texto del
docs/loop/REPORTE.md de la vuelta 78 ARCHIVADO en el commit 0ea71f3a.

POR QUE NO SE USA --comparar PARA ESTO: --comparar coteja contra una tabla de
TRES columnas ("| etiqueta | apertura | cierre |"), que es el formato que el
propio tallador imprime. El REPORTE.md de la vuelta 78 es justo el ejemplar
del problema que la TAREA 2 vino a resolver: sus cifras estaban TECLEADAS en
DOS tablas de prosa de DOS columnas (seccion 0 apertura, seccion 5 cierre), no
en una tabla de tres columnas. Pedirle a --comparar que lea ese formato viejo
daria CERO filas encontradas (AUSENTE en las siete), que no es lo mismo que
"distinta": es un choque de FORMA, no de DATO. Este script hace la
comparacion de DATO que el encargo pide, leyendo el texto exacto del
REPORTE.md archivado con sus propios patrones, seccion por seccion.

USO:
  python scripts/loop/vuelta79_tarea2_caso_positivo.py
"""
import re
import subprocess
import sys

sys.path.insert(0, "scripts/loop")
import tallar_cabecera_reporte as t


def texto_en_commit(commit, ruta):
    r = subprocess.run(["git", "show", "%s:%s" % (commit, ruta)], capture_output=True)
    return r.stdout.decode("utf-8")


def campo(texto, patron, etiqueta, resultados_fallidos):
    m = re.search(patron, texto)
    if not m:
        resultados_fallidos.append(etiqueta)
        return None
    return m.group(1)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    texto = texto_en_commit("0ea71f3a", "docs/loop/REPORTE.md")
    corte = texto.index("## 5. EL CIERRE")
    texto_ap = texto[:corte]
    texto_ci = texto[corte:texto.index("## 6.")]

    fallos = []
    ap = t.lado_fase04(78, "APERTURA", fallos, con_miles=True)
    ci = t.lado_fase04(78, "CIERRE", fallos, con_miles=True)
    if fallos:
        print("ROJO: el propio tallador no pudo leer sus salidas:")
        for f in fallos:
            print("  " + f)
        return 1

    sin_patron = []
    resultados = []

    def cotejar(etiqueta, tallada, texto_fuente, patron, solo_cifras=False):
        vieja = campo(texto_fuente, patron, etiqueta, sin_patron)
        if vieja is None:
            resultados.append((etiqueta, tallada, "NO ENCONTRADO", False))
            return
        if solo_cifras:
            # Las cifras del texto ARCHIVADO tienen que estar TODAS presentes
            # en las cifras del tallador (que puede citar ademas totales
            # derivados, p.ej. vitest "80 passed (80)", que el archivado no
            # repite pero no contradice).
            num_viejas = set(re.findall(r"\d+", str(vieja).replace(".", "")))
            num_talladas = set(re.findall(r"\d+", str(tallada).replace(".", "")))
            ok = num_viejas.issubset(num_talladas)
        else:
            ok = (str(vieja).replace(".", "").lower() == str(tallada).replace(".", "").lower())
        resultados.append((etiqueta, tallada, vieja, ok))

    # --- SECCION 0, LA APERTURA ---
    cotejar("censo nodos (apertura)", ap["nodos"], texto_ap, r"grafo: ([\d\.]+) nodos,")
    cotejar("censo vivos (apertura)", ap["vivos"], texto_ap, r"grafo: [\d\.]+ nodos, ([\d\.]+) vivos,")
    cotejar("censo deprecados (apertura)", ap["deprecados"], texto_ap, r"vivos, ([\d\.]+) deprecados \|")
    cotejar("nodos_siguientes (apertura)", ap["sig"], texto_ap, r"`nodos_siguientes` en `57863182`\s*\|\s*\*\*([\d\.]+)\*\*")
    cotejar("nodos_previos (apertura)", ap["prev"], texto_ap, r"`nodos_previos` en `57863182`\s*\|\s*\*\*([\d\.]+)\*\*")
    cotejar("suma (apertura)", ap["suma"], texto_ap, r"\| suma\s*\|\s*\*\*([\d\.]+)\*\*\s*\|")
    cotejar("union (apertura)", ap["union"], texto_ap, r"union dirigida unica\s*\|\s*\*\*([\d\.]+)\*\*")
    cotejar("motor (apertura)", ap["motor"], texto_ap, r"`python engine/run_all_tests\.py`:\s*\*\*(\d+/\d+)\*\*")
    cotejar("web ficheros+tests (apertura)", ap["web_ficheros"] + " / " + ap["web_tests"], texto_ap,
            r"desde `web/`:\s*\*\*([\d\.]+ ficheros, [\d\.]+ pasadas, \d+ saltadas)\*\*", solo_cifras=True)
    cotejar("tsc (apertura)", ap["tsc"], texto_ap, r"desde `web/`:\s*\*\*(exitcode 0, cero lineas)\*\*")
    cotejar("Gate0 (apertura)", "%s auto-aristas %s duplicadas %s divergentes %s"
            % (ap["gate_veredicto"], ap["auto_aristas"], ap["dup_titulo"], ap["divergentes"]),
            texto_ap, r"Gate 0 \| (OK \(ciclo de tres, auto-aristas 0, duplicadas 0, divergentes 0\))", solo_cifras=True)

    # --- SECCION 5, EL CIERRE ---
    cotejar("censo (cierre, sin cambio)", "%s nodos, %s vivos, %s deprecados" % (ci["nodos"], ci["vivos"], ci["deprecados"]),
            texto_ci, r"grafo: ([\d\.]+ nodos, [\d\.]+ vivos, [\d\.]+ deprecados) \(sin cambio")
    cotejar("nodos_siguientes (cierre)", ci["sig"], texto_ci, r"`nodos_siguientes`\s*\|\s*\*\*([\d\.]+)\*\*")
    cotejar("nodos_previos (cierre)", ci["prev"], texto_ci, r"`nodos_previos`\s*\|\s*\*\*([\d\.]+)\*\*")
    cotejar("suma (cierre)", ci["suma"], texto_ci, r"\| suma\s*\|\s*\*\*([\d\.]+)\*\*\s*\|")
    cotejar("union (cierre)", ci["union"], texto_ci, r"union dirigida unica\s*\|\s*\*\*([\d\.]+)\*\*")
    cotejar("Gate0 (cierre)", "%s auto-aristas %s duplicadas %s divergentes %s"
            % (ci["gate_veredicto"], ci["auto_aristas"], ci["dup_titulo"], ci["divergentes"]),
            texto_ci, r"Gate 0 \| (OK, ciclo de tres, auto-aristas 0, duplicadas 0, divergentes 0)", solo_cifras=True)
    cotejar("motor (cierre)", ci["motor"], texto_ci, r"motor\s*\|\s*(\d+/\d+)\s*\(")
    cotejar("web (cierre)", "%s / %s" % (ci["web_ficheros"], ci["web_tests"]), texto_ci,
            r"web \(corrido desde `web/`\)\s*\|\s*([\d\.]+ ficheros, [\d\.]+ pasadas, \d+ saltadas)", solo_cifras=True)
    cotejar("tsc (cierre)", ci["tsc"], texto_ci, r"tsc \(corrido desde `web/`\)\s*\|\s*(EXITCODE 0, cero lineas)")
    cotejar("marcador A (cierre)", ci["marcador_A"], texto_ci, r"marcador del cribado\s*\|\s*A (\d+),")
    cotejar("marcador B (cierre)", ci["marcador_B"], texto_ci, r"marcador del cribado\s*\|\s*A \d+, B (\d+),")
    cotejar("marcador C (cierre)", ci["marcador_C"], texto_ci, r"marcador del cribado\s*\|\s*A \d+, B \d+, C (\d+),")
    cotejar("marcador D (cierre)", ci["marcador_D"], texto_ci, r"marcador del cribado\s*\|\s*A \d+, B \d+, C \d+, D ([\d\.]+),")
    cotejar("marcador n (cierre)", ci["marcador_n"], texto_ci, r"marcador del cribado\s*\|.*?\bn ([\d\.]+)\b")

    print("=" * 78)
    print("CASO POSITIVO: tallador --fase04 --vuelta 78 CONTRA REPORTE.md archivado en 0ea71f3a")
    print("=" * 78)
    todo_ok = True
    for etiqueta, tallada, vieja, ok in resultados:
        estado = "IGUAL" if ok else "DISTINTA"
        if not ok:
            todo_ok = False
        print("  %-38s | tallador: %-42s | archivado: %-42s | %s" % (etiqueta, tallada, vieja, estado))
    print()
    if sin_patron:
        print("SIN PATRON (no se pudo buscar en el archivado): %s" % ", ".join(sin_patron))
        todo_ok = False
    print("RESULTADO: %s" % ("TODAS IGUALES" if todo_ok else "HAY DIFERENCIAS, PARAR Y TRAER"))
    return 0 if todo_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
