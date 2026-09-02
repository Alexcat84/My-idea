# -*- coding: utf-8 -*-
r"""vuelta147_2c_mutacion_vitalidad.py . LA PRUEBA DE MUTACION DE LA ESCALADA
DE LA ESCALADA (TAREAS 2.c y 2.d de la vuelta 147).

QUE PRUEBA. La vuelta 146 construyo `verificar_ausencias_del_reporte.py` y
`barrer_ausencia.py`, y el auditor comprobo con mutaciones propias que MUERDEN.
Lo que la caida 4.2 del acta 146 demostro es que NO ALCANZAN: un barrido puede
traer el sello completo y tener una pierna POR CONTENIDO de TRES IDENTIFICADORES
QUE NADIE ESCRIBIO NUNCA, y entonces el sello certifica el metodo exacto que la
CORRECCION 23 prohibe, un nivel mas abajo. La vuelta 147 anade LA SEXTA PIEZA
del sello (la VITALIDAD de la pierna por contenido) y OCHO FORMULAS al
vocabulario de ausencia. Este arnes prueba las dos cosas.

NINGUN VEREDICTO ES UN LITERAL COMPARADO CONSIGO MISMO (`EJECUTOR.md` 1, caida 2
de la vuelta 89): todos salen de leer la SALIDA REAL del proceso.

TODOS LOS SUJETOS SON CONGELADOS O COMPUTADOS, NINGUNO ES EL ARBOL VIVO
(CORRECCION 22), Y NINGUN REF SE TECLEA (`EJECUTOR.md`, LA IDENTIDAD SE LEE DE
GIT):

  (A) CASO ROJO, EL QUE MANDA (TAREA 2.c). El sello del barrido del umbral de la
      vuelta 146, `docs/loop/SALIDA_V146_3E_BARRIDO_UMBRAL.txt`, CONGELADO EN SU
      COMMIT DE NACIMIENTO, que se computa con `git log --diff-filter=A` y no se
      teclea. Tiene que salir EXIT 1 nombrando SUS TRES ALTERNATIVAS MUERTAS.
      Es el barrido que respaldo la afirmacion falsa; si saliera verde sobre el,
      la ampliacion no sirve y este arnes lo dice en vez de aflojarla.

      Y LA MEDICION SE HACE CONTRA EL ARBOL DE SU PROPIO COMMIT, no contra el de
      hoy, por una razon medida dentro de esta misma vuelta: sobre el arbol de
      HOY los tres identificadores salen VIVOS, porque el docstring que documenta
      la caida los escribe. Un sello se juzga contra el universo que declaro.

  (B) CASO ROJO DEL VOCABULARIO (TAREA 2.c, segunda mitad). La guarda con el
      vocabulario ampliado, sobre el `docs/loop/REPORTE.md` de la vuelta 146
      CONGELADO POR REF, tiene que salir EXIT 1 y tiene que NOMBRAR LA FRASE DE
      LA PREGUNTA 2, la que llevaba dentro la afirmacion falsa del umbral. El
      ref se computa: el ultimo commit que toco ese fichero ANTES del HEAD de
      apertura de esta vuelta, leido de `SALIDA_V147_HEAD_APERTURA.txt`.

  (C) CASO VERDE (TAREA 2.d). Sin el, (A) solo probaria que el instrumento sabe
      decir rojo. El barrido del umbral REHECHO, con la pierna por contenido
      buscando EL CONCEPTO (`umbral|similitud`) en vez de tres constantes
      inventadas, tiene que hallar `scripts/intra_dominio.py` y su sello tiene
      que salir VERDE. SE CORRE EN VIVO dentro del arnes en vez de leer un
      fichero commiteado: asi no hay artefacto que envejecer, y lo que se
      comprueba es que la pierna que busca el concepto SIGUE teniendo poder hoy.

  (D) LA MUTACION QUE PRUEBA EL CAMINO DE LA RECOMPUTACION, sobre VARIABLE
      COMPUTADA y nunca sobre un literal. Se toma la salida REAL de (C) y se le
      sustituye SOLO el patron de la pierna por contenido por TRES TOKENS
      ELEGIDOS POR COMPUTO Y VERIFICADOS AUSENTES del universo (se derivan del
      sha256 de la propia salida y el arnes MIDE que no aparecen; si alguno
      apareciera, ROJO PREVIO en vez de seguir). Se le quita ademas la linea de
      vitalidad, para forzar el camino de la recomputacion. Tiene que salir
      EXIT 1 nombrandolos. CONTRAPRUEBA DENTRO DEL MISMO CASO: el mismo texto
      sin la linea de vitalidad pero CON el patron bueno tiene que salir EXIT 0.

  (E) LA MUTACION QUE PRUEBA EL CAMINO DE LA LINEA DECLARADA. El mismo texto de
      (C) con su linea de vitalidad reescrita a cero vivas tiene que salir EXIT
      1; con su linea intacta, EXIT 0. La cifra de la mutacion se COMPUTA de la
      propia linea leida (se lee "<v> de <t>" y se escribe "0 de <t>"), no se
      teclea.

QUIEN FABRICA, LIMPIA (P.16): los sujetos de (D) y (E) se escriben en temporales
y se borran siempre, tambien si el arnes revienta. Los de (A) y (B) no se
fabrican: se leen de git.

USO:
  python scripts/loop/vuelta147_2c_mutacion_vitalidad.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_ausencias_del_reporte.py")
BARRIDO = os.path.join(RAIZ, "scripts", "loop", "barrer_ausencia.py")

SELLO_UMBRAL_146 = "docs/loop/SALIDA_V146_3E_BARRIDO_UMBRAL.txt"
REPORTE = "docs/loop/REPORTE.md"
HEAD_APERTURA = os.path.join(LOOP, "SALIDA_V147_HEAD_APERTURA.txt")

# La AGUJA de (B): la cabecera de la PREGUNTA 2 del reporte de la 146, la frase
# que el acta 146 nombra en su caida 4.2. NO es el veredicto de nada: es lo que
# se busca DENTRO de la salida real del proceso.
AGUJA_PREGUNTA_2 = "EL UMBRAL DE LA COLA NO TIENE NUMERO EN NINGUNA PARTE"
# El fichero que la pierna por contenido buena TIENE que hallar en (C).
AGUJA_INTRA = "scripts/intra_dominio.py"


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("ROJO PREVIO: git %s fallo: %s" % (" ".join(args), r.stderr.strip()))
    return r.stdout


def correr(argumentos):
    """Corre un instrumento y devuelve (exit, salida). Nada se compara con un
    literal: lo que se juzga es ESTO."""
    r = subprocess.run([sys.executable] + argumentos, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace") + r.stderr.decode("utf-8", "replace")


def ref_de_nacimiento(ruta):
    """El commit que ANADE el fichero, computado de git. Nunca tecleado."""
    salida = [h for h in git(["log", "--diff-filter=A", "--format=%H", "--", ruta]).splitlines()
              if h.strip()]
    if len(salida) != 1:
        raise SystemExit("ROJO PREVIO: %s tiene %d commits que lo anaden, se esperaba 1"
                         % (ruta, len(salida)))
    return salida[0]


def ref_del_reporte_146():
    """El ultimo commit que toco docs/loop/REPORTE.md ANTES del HEAD de apertura
    de esta vuelta. El HEAD de apertura se lee de su propio sello, no se
    teclea, y de ahi sale el reporte de la vuelta anterior."""
    if not os.path.exists(HEAD_APERTURA):
        raise SystemExit("ROJO PREVIO: no existe %s, sin el no se puede computar el ref"
                         % HEAD_APERTURA)
    head = io.open(HEAD_APERTURA, encoding="utf-8").read().strip()
    if not re.match(r"^[0-9a-f]{40}$", head):
        raise SystemExit("ROJO PREVIO: %s no trae un hash de 40 caracteres" % HEAD_APERTURA)
    salida = [h for h in git(["log", "-1", "--format=%H", head, "--", REPORTE]).splitlines()
              if h.strip()]
    if len(salida) != 1:
        raise SystemExit("ROJO PREVIO: no se pudo computar el ultimo commit de %s antes de %s"
                         % (REPORTE, head[:8]))
    return salida[0]


def tokens_muertos_por_computo(semilla):
    """TRES tokens derivados del sha256 de la salida real, NUNCA tecleados y
    NUNCA escritos en este fichero (escribirlos aqui los volveria vivos, que es
    exactamente el falso verde que esta vuelta midio)."""
    h = hashlib.sha256(semilla.encode("utf-8")).hexdigest()
    return ["zq%s" % h[0:12], "zq%s" % h[12:24], "zq%s" % h[24:36]]


def escribir_temporal(texto):
    fd, ruta = tempfile.mkstemp(suffix=".txt", prefix="v147_2c_")
    with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    return ruta


def main():
    resultados = []

    # --- (A) EL CASO ROJO QUE MANDA, SOBRE SUJETO CONGELADO ---
    ref_sello = ref_de_nacimiento(SELLO_UMBRAL_146)
    cod, sal = correr([GUARDA, "--sello", SELLO_UMBRAL_146, "--sello-ref", ref_sello])
    muertos_nombrados = all(t in sal for t in
                            ("UMBRAL_DE_LA_COLA", "UMBRAL_COLA", "umbral_de_la_cola"))
    ok_a = cod == 1 and "ROJO" in sal and muertos_nombrados
    resultados.append(("A el sello del umbral de la 146 (congelado en %s) sale ROJO"
                       % ref_sello[:8], ok_a, sal.strip().splitlines()[-1][:200]))

    # --- (B) EL CASO ROJO DEL VOCABULARIO AMPLIADO, SOBRE SUJETO CONGELADO ---
    ref_rep = ref_del_reporte_146()
    cod, sal = correr([GUARDA, "--ref", ref_rep])
    ok_b = cod == 1 and AGUJA_PREGUNTA_2 in sal
    linea_b = next((l for l in sal.splitlines() if AGUJA_PREGUNTA_2 in l), "(no nombrada)")
    resultados.append(("B la guarda ampliada sobre el reporte de la 146 (congelado en %s) "
                       "nombra la PREGUNTA 2" % ref_rep[:8], ok_b, linea_b.strip()[:200]))

    # --- (C) EL CASO VERDE, CORRIDO EN VIVO ---
    cod, sal_c = correr([BARRIDO,
                         "--pregunta", "existe en el codigo una constante que fije el UMBRAL "
                                       "de la cola semantica en un valor numerico",
                         "--nombre", "umbral|cola|intra",
                         "--contenido", "umbral|similitud",
                         "--universo-prefijo", "scripts/",
                         "--universo-prefijo", "engine/",
                         "--universo-prefijo", "web/"])
    halla_intra = AGUJA_INTRA in sal_c
    ruta_c = escribir_temporal(sal_c)
    try:
        cod_c, sal_cj = correr([GUARDA, "--sello", ruta_c])
        ok_c = cod == 0 and halla_intra and cod_c == 0
        resultados.append(("C el barrido rehecho por CONCEPTO halla %s y su sello sale VERDE"
                           % AGUJA_INTRA, ok_c, sal_cj.strip().splitlines()[-1][:200]))

        # --- (D) MUTACION DEL PATRON, CAMINO DE LA RECOMPUTACION ---
        muertos = tokens_muertos_por_computo(sal_c)
        cod_v, sal_v = correr([BARRIDO, "--pregunta", "verificacion de que los tokens de la "
                                                      "mutacion estan de verdad ausentes",
                               "--nombre", "no_existe_este_nombre_de_fichero",
                               "--contenido", "|".join(muertos),
                               "--universo-prefijo", "scripts/",
                               "--universo-prefijo", "engine/",
                               "--universo-prefijo", "web/"])
        m_vit = re.search(r"^\s*VITALIDAD[^:]*:\s*(\d+) de (\d+)", sal_v, re.MULTILINE)
        if not m_vit or int(m_vit.group(1)) != 0:
            print("ROJO PREVIO: los tokens elegidos por computo NO estan ausentes del "
                  "universo, la mutacion no probaria nada")
            return 2

        # Se quita la linea de vitalidad Y su desglose (las lineas ` alt -> n
        # estado` que van justo debajo), para forzar el camino de la
        # RECOMPUTACION en vez del de la linea declarada.
        sin_vit_lineas, saltando = [], False
        for linea in sal_c.splitlines():
            if "VITALIDAD DE LOS PATRONES DE CONTENIDO" in linea:
                saltando = True
                continue
            if saltando and re.match(r"^\s{6}\S.*\s->\s", linea):
                continue
            saltando = False
            sin_vit_lineas.append(linea)
        sin_vit = "\n".join(sin_vit_lineas)
        # EL PATRON ENTERO, y no hasta el primer `|`: el propio patron trae `|`
        # dentro (es una alternancia), asi que un corte perezoso dejaria viva la
        # segunda alternativa y la mutacion no probaria nada. Se ancla al sufijo
        # contable que el sello imprime SIEMPRE.
        mutado, cuantas = re.subn(
            r"^(\s*POR CONTENIDO:\s*)(.*)(\s\|\s\d+ ficheros con coincidencia\s*)$",
            lambda m: m.group(1) + "|".join(muertos) + m.group(3),
            sin_vit, count=1, flags=re.MULTILINE)
        if cuantas != 1:
            print("ROJO PREVIO: no se pudo sustituir el patron de la pierna por contenido")
            return 2
        if mutado == sin_vit:
            print("ROJO PREVIO: la mutacion no cambio nada, no hay nada que probar")
            return 2
        ruta_d = escribir_temporal(mutado)
        ruta_d0 = escribir_temporal(sin_vit)
        try:
            cod_d, sal_d = correr([GUARDA, "--sello", ruta_d])
            cod_d0, sal_d0 = correr([GUARDA, "--sello", ruta_d0])
            ok_d = (cod_d == 1 and all(t in sal_d for t in muertos)
                    and cod_d0 == 0)
            resultados.append(("D patron mutado a tokens muertos por computo: ROJO por "
                               "RECOMPUTACION; con el patron bueno y sin linea: VERDE",
                               ok_d, "mutado exit %d / contraprueba exit %d" % (cod_d, cod_d0)))
        finally:
            for r_ in (ruta_d, ruta_d0):
                if os.path.exists(r_):
                    os.remove(r_)

        # --- (E) MUTACION DE LA LINEA DECLARADA ---
        m = re.search(r"^(\s*VITALIDAD DE LOS PATRONES DE CONTENIDO:\s*)(\d+)( de )(\d+)",
                      sal_c, re.MULTILINE)
        if not m:
            print("ROJO PREVIO: la salida de (C) no trae linea de vitalidad que mutar")
            return 2
        mutado_e = sal_c[:m.start()] + m.group(1) + "0" + m.group(3) + m.group(4) + \
            sal_c[m.end():]
        ruta_e = escribir_temporal(mutado_e)
        try:
            cod_e, sal_e = correr([GUARDA, "--sello", ruta_e])
            ok_e = cod_e == 1 and "ENTERAMENTE MUERTA" in sal_e
            resultados.append(("E linea de vitalidad mutada a cero vivas (cifra computada de "
                               "la propia linea): ROJO por la linea DECLARADA", ok_e,
                               sal_e.strip().splitlines()[-1][:200]))
        finally:
            if os.path.exists(ruta_e):
                os.remove(ruta_e)
    finally:
        if os.path.exists(ruta_c):
            os.remove(ruta_c)

    print("PRUEBA DE MUTACION DE LA VITALIDAD Y DEL VOCABULARIO AMPLIADO (vuelta 147, 2.c y 2.d)")
    print("")
    for rotulo, ok, detalle in resultados:
        print("  %-100s %s" % (rotulo, "OK" if ok else "NO MORDIO"))
        print("      %s" % detalle)
    muerden = sum(1 for _, ok, _ in resultados if ok)
    print("")
    print("CASOS QUE MUERDEN: %d de %d" % (muerden, len(resultados)))
    print("CIFRA casos que muerden: %d casos" % muerden)
    print("CIFRA casos del arnes: %d casos" % len(resultados))
    return 0 if muerden == len(resultados) else 1


if __name__ == "__main__":
    raise SystemExit(main())
