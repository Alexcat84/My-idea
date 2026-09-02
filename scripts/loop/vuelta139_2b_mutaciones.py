# -*- coding: utf-8 -*-
"""vuelta139_2b_mutaciones.py . LAS GUARDAS (i), (ii) Y (iii) DE LA OPERACION
2.b DE LA VUELTA 139: LA GUARDA DE CIFRAS DEJA DE SER CIEGA A LAS TABLAS.

EL DEFECTO QUE SE REPARA, medido por el auditor y no opinado (acta de la vuelta
138, caida 4.5): `quitar_bloques_cubiertos()` prometia en su docstring quitar
"la tabla de cabecera", en singular, y su implementacion DESCARTABA TODA LINEA
QUE EMPEZARA POR BARRA VERTICAL. Sobre el reporte de la 138: 26 cifras de
numero mas unidad en el fichero entero, 10 que la guarda veia, 16 que se
perdian por vivir en una fila de tabla. Y la linea publicada,
`COBERTURA: 10 cotejadas / 0 exentas / 10 cifras`, se lee como cobertura llena.

QUE PRUEBA, con las palabras del encargo:
  (i)   MUTACION: una fila de tabla con una cifra de numero mas unidad que NO
        cuadra con su fichero de salida tiene que dar ROJO. HOY PASA
        INVISIBLE; esa es la prueba de que la reparacion muerde. Se corre la
        MISMA fila por la guarda VIEJA (sacada de git, no reescrita a mano) y
        por la NUEVA, y se ensenan los dos veredictos.
  (ii)  CASO POSITIVO sobre un sujeto CONGELADO, nunca sobre
        docs/loop/REPORTE.md, que se sobreescribe cada vuelta. El sujeto es
        docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md, el mismo que monto la
        2.b de la vuelta 138, y su sha256 se coteja contra el blob del acta
        134 EN CADA CORRIDA antes de medir nada.
  (iii) LA CIFRA COMPUTADA: la guarda reparada corrida contra el REPORTE DE LA
        VUELTA 138 TAL COMO ESTA EN GIT (blob, no el fichero de hoy, que esta
        vuelta sobreescribe), y se publica CUANTAS CIFRAS VE AHORA contra las
        10 de antes. AVISO DEL ENCARGO: casi seguro dara ROJO, porque las
        cifras de tabla nunca se citaron. ESO ES EL EXITO, NO EL FALLO. Lo que
        se hace con los rojos es CITARLOS, jamas debilitar la guarda ni borrar
        la tabla.

Y DE PROPINA, la guarda del delimitador, que sin caso no se prueba sola:
  (iv)  CON las dos marcas, se quita EXACTAMENTE el bloque delimitado y ni una
        fila mas; SIN ellas no se quita nada; con UNA SOLA es ROJO ruidoso
        (ValueError) en vez de adivinar donde acaba el bloque.

LA VARA DE LA GUARDA VIEJA SE SACA DE GIT, NO SE RETECLEA: se lee el blob de
scripts/loop/verificar_cifras_del_reporte.py en el commit del acta de la vuelta
138 (e8cf1552, el ultimo antes de esta reparacion), se escribe en un temporal y
se importa desde alli. Comparar contra una copia tecleada a mano de "lo que
hacia antes" mediria mi memoria, no el codigo viejo.

P.16, QUIEN FABRICA LIMPIA: el temporal se borra siempre, y NI UN FICHERO
SELLADO DE OTRA VUELTA SE TOCA (leccion de la caida 4.2 del acta 137).

USO:
  python scripts/loop/vuelta139_2b_mutaciones.py
"""
import contextlib
import hashlib
import importlib.util
import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
LOOP_SCRIPTS = os.path.join(RAIZ, "scripts", "loop")

GUARDA_REL = "scripts/loop/verificar_cifras_del_reporte.py"
# EL COMMIT DEL ACTA DE LA VUELTA 138: el ultimo arbol en el que la guarda
# todavia era ciega a las tablas. No se teclea el hash a ciegas: se resuelve por
# el ASUNTO del commit, con git, y se imprime.
ASUNTO_ACTA_138 = "ACTA DE LA VUELTA 138 DEL AUDITOR"

SUJETO_FIJO = "SUJETO_FIJO_V135_2E_REPORTE_134.md"
# El blob del que sale el sujeto congelado, ya declarado por la 2.b de la vuelta
# 138: docs/loop/REPORTE.md en el commit del acta de la vuelta 134.
BLOB_DEL_SUJETO = "e12e4c36:docs/loop/REPORTE.md"

REPORTE_REL = "docs/loop/REPORTE.md"


class SalidaCapturable(io.StringIO):
    def reconfigure(self, **kw):
        return None


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO: git %s fallo: %s"
                         % (" ".join(args), r.stderr.decode("utf-8", "replace").strip()))
    return r.stdout


def commit_por_asunto(asunto):
    out = git(["log", "--pretty=format:%H\x01%s"]).decode("utf-8")
    hallados = [l.split("\x01", 1)[0] for l in out.splitlines()
                if "\x01" in l and l.split("\x01", 1)[1].startswith(asunto)]
    if len(hallados) != 1:
        raise SystemExit("ROJO: %d commit(s) con el asunto %r, se esperaba 1"
                         % (len(hallados), asunto))
    return hallados[0]


def normalizar(datos):
    return datos.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def sha256_normalizado(datos):
    return hashlib.sha256(normalizar(datos)).hexdigest()


def importar_de_ruta(nombre, ruta):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = mod
    spec.loader.exec_module(mod)
    return mod


def correr_guarda(mod, ruta_reporte):
    """Corre el main() de una guarda contra un reporte. Devuelve (codigo,
    texto)."""
    argv = [getattr(mod, "__file__", "guarda"), "--reporte", ruta_reporte]
    buf = SalidaCapturable()
    viejo = sys.argv
    sys.argv = argv
    try:
        with contextlib.redirect_stdout(buf):
            codigo = mod.main()
    finally:
        sys.argv = viejo
    return codigo, buf.getvalue()


def cifras_vistas(mod, ruta_reporte):
    """LA CIFRA COMPUTADA: cuantos pares (numero, unidad) llega a VER la guarda,
    o sea el `total_cifras` que su propia verificar() devuelve. No se parsea la
    linea de COBERTURA: se llama a la funcion y se lee su tercer valor de
    retorno, que es el mismo dato antes de imprimirse."""
    _fallos, _cot, _ex, total = mod.verificar(ruta_reporte)
    return total


def contar_filas_de_tabla(texto):
    return sum(1 for l in texto.split("\n") if l.strip().startswith("|"))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("GUARDAS (i), (ii), (iii) Y (iv) DE LA OPERACION 2.b, VUELTA 139")
    print("LA GUARDA DE CIFRAS DEJA DE SER CIEGA A LAS TABLAS")
    print("=" * 78)

    veredictos = []
    tmp = tempfile.mkdtemp(prefix="v139_2b_")
    try:
        # ------------------------------------------------------------------
        # LA GUARDA NUEVA (la del arbol de hoy) Y LA VIEJA (sacada de git).
        # ------------------------------------------------------------------
        acta138 = commit_por_asunto(ASUNTO_ACTA_138)
        print("  commit del acta 138, resuelto por su asunto: %s" % acta138[:8])
        blob_viejo = git(["show", "%s:%s" % (acta138, GUARDA_REL)])
        ruta_vieja = os.path.join(tmp, "guarda_vieja.py")
        io.open(ruta_vieja, "wb").write(blob_viejo)
        print("  guarda VIEJA sacada de git: %d bytes, sha256 %s"
              % (len(blob_viejo), sha256_normalizado(blob_viejo)[:16]))

        sys.path.insert(0, LOOP_SCRIPTS)
        nueva = importar_de_ruta("guarda_nueva_v139", os.path.join(RAIZ, GUARDA_REL))
        vieja = importar_de_ruta("guarda_vieja_v138", ruta_vieja)
        print("  las DOS guardas importadas, la de hoy y la del acta 138.")

        # ------------------------------------------------------------------
        # (ii) EL SUJETO CONGELADO, con su sha256 cotejado ANTES de medir.
        # ------------------------------------------------------------------
        print("")
        print("-" * 78)
        print("(ii) EL SUJETO CONGELADO Y SU IDENTIDAD, cotejada en esta corrida.")
        ruta_sujeto = os.path.join(LOOP, SUJETO_FIJO)
        if not os.path.exists(ruta_sujeto):
            print("    ROJO PREVIO: no existe %s" % SUJETO_FIJO)
            return 1
        datos_sujeto = io.open(ruta_sujeto, "rb").read()
        datos_blob = git(["show", BLOB_DEL_SUJETO])
        h_sujeto = sha256_normalizado(datos_sujeto)
        h_blob = sha256_normalizado(datos_blob)
        print("    %s : sha256 %s" % (SUJETO_FIJO, h_sujeto))
        print("    %s : sha256 %s" % (BLOB_DEL_SUJETO, h_blob))
        identidad_ok = (h_sujeto == h_blob)
        print("    identicos byte a byte (normalizando fin de linea): %s" % identidad_ok)
        if not identidad_ok:
            print("    ROJO PREVIO: el sujeto congelado ya no es el blob que dice ser.")
            return 1

        print("")
        print("    CASO POSITIVO SOBRE EL SUJETO CONGELADO, las dos guardas:")
        cod_v_suj, txt_v_suj = correr_guarda(vieja, ruta_sujeto)
        cod_n_suj, txt_n_suj = correr_guarda(nueva, ruta_sujeto)
        vistas_v_suj = cifras_vistas(vieja, ruta_sujeto)
        vistas_n_suj = cifras_vistas(nueva, ruta_sujeto)
        filas_suj = contar_filas_de_tabla(datos_sujeto.decode("utf-8"))
        print("       filas de tabla en el sujeto            : %d" % filas_suj)
        print("       cifras que VE la guarda VIEJA          : %d (exit %d)"
              % (vistas_v_suj, cod_v_suj))
        print("       cifras que VE la guarda NUEVA          : %d (exit %d)"
              % (vistas_n_suj, cod_n_suj))
        for l in txt_n_suj.splitlines():
            if l.startswith("COBERTURA:"):
                print("       %s" % l)

        # LA PROPIEDAD QUE SE PRUEBA ES LA MONOTONIA, y se dice por que esa y no
        # "ve mas": la reparacion quita ESTRICTAMENTE MENOS texto que la version
        # vieja (antes, toda linea que empezara por barra vertical; ahora, solo
        # el bloque delimitado, y nada si no hay marcas). De ahi se sigue que la
        # nueva NUNCA puede ver menos cifras que la vieja sobre el mismo sujeto.
        # Que sobre ESTE sujeto vea las MISMAS 4 no es un fallo de la
        # reparacion: es que sus 12 filas de tabla no traen ni un par (numero,
        # unidad) del vocabulario cerrado, y eso se mide aqui abajo en vez de
        # suponerse.
        ok_ii = vistas_n_suj >= vistas_v_suj
        print("    MONOTONIA (la nueva nunca ve menos que la vieja): %s" % ok_ii)
        cifras_en_filas = 0
        for l in datos_sujeto.decode("utf-8").split("\n"):
            if l.strip().startswith("|"):
                cifras_en_filas += len(nueva.PATRON_NUMERO_UNIDAD.findall(l))
        print("    pares (numero, unidad) que viven en las %d filas de tabla de este"
              % filas_suj)
        print("    sujeto, contados con el patron de la propia guarda: %d" % cifras_en_filas)
        print("    POR ESO las dos ven %d: aqui no habia nada que la ceguera tapara."
              % vistas_n_suj)

        # Y LO QUE SI CAMBIA, DECLARADO Y NO ESCONDIDO: el VEREDICTO.
        print("")
        print("    LO QUE SI CAMBIA EN ESTE SUJETO, Y SE DECLARA: EL VEREDICTO.")
        print("       la VIEJA da exit %d, la NUEVA da exit %d." % (cod_v_suj, cod_n_suj))
        print("       No es que la nueva vea mas cifras: es que al dejar de borrar las")
        print("       filas de tabla, la VENTANA AMPLIA de la exencion (iii) cambia de")
        print("       vecinos, y dos `(sin instrumento)` del reporte de la 134 dejan de")
        print("       ser legales porque su ventana SI cita un fichero. Es el ramal")
        print("       (xix) mordiendo mas, no menos: una exencion que escribe el")
        print("       auditado no es una exencion. Los dos fallos, enteros:")
        for l in txt_n_suj.splitlines():
            if l.strip().startswith("linea "):
                print("          %s" % l.strip())

        # EL POSITIVO DURO, y es el que impide que esto sea una tautologia: LAS
        # CUATRO MUTACIONES VIEJAS, ancladas a este mismo sujeto congelado,
        # TIENEN QUE SEGUIR MORDIENDO con la guarda reparada. Se corre la guarda
        # de la casa, no una copia.
        print("")
        print("    EL POSITIVO DURO: las CUATRO mutaciones viejas, ancladas a este mismo")
        print("    sujeto congelado, corridas con la guarda reparada.")
        r = subprocess.run(
            [sys.executable, os.path.join(LOOP_SCRIPTS, "verificar_mutaciones_viejas.py")],
            cwd=RAIZ, capture_output=True, text=True)
        for l in r.stdout.splitlines():
            if l.strip():
                print("       %s" % l.rstrip())
        cuatro_ok = (r.returncode == 0)
        print("       exit de verificar_mutaciones_viejas.py: %d" % r.returncode)

        veredictos.append(("(ii.a) identidad del sujeto congelado",
                           "VERDE, sha256 identico al blob"))
        veredictos.append(("(ii.b) monotonia, la nueva nunca ve menos",
                           "VERDE, %d -> %d cifras" % (vistas_v_suj, vistas_n_suj)
                           if ok_ii else
                           "ROJO, vieja %d y nueva %d" % (vistas_v_suj, vistas_n_suj)))
        veredictos.append(("(ii.c) las 4 mutaciones viejas siguen mordiendo",
                           "VERDE, exit 0" if cuatro_ok else
                           "ROJO, exit %d" % r.returncode))

        # ------------------------------------------------------------------
        # (i) LA MUTACION: una fila de tabla con una cifra que NO cuadra.
        # ------------------------------------------------------------------
        print("")
        print("-" * 78)
        print("(i) MUTACION: una FILA DE TABLA con una cifra que NO cuadra con su fichero.")
        # El fichero de salida contra el que se coteja es uno REAL de esta misma
        # vuelta, ya sellado y commiteado, y la cifra se calcula de el: la buena
        # es la que el propio fichero tiene, y la mala es esa mas uno. Ninguna
        # de las dos es un literal tecleado.
        fichero_testigo = "SALIDA_V139_CONTEO_APERTURA.txt"
        contenido_testigo = io.open(os.path.join(LOOP, fichero_testigo),
                                    encoding="utf-8").read()
        buenas = nueva.contar_lineas(contenido_testigo)
        malas = buenas + 1
        print("    fichero testigo: `%s`" % fichero_testigo)
        print("    lineas que el fichero tiene de verdad (contadas por la guarda): %d" % buenas)
        print("    la fila de tabla dira %d lineas, que es una de mas: %d" % (malas, malas))

        cuerpo_mut = "\n".join([
            "# SUJETO DE LA MUTACION (i) DE LA 2.b, VUELTA 139",
            "",
            "Este sujeto lo fabrica scripts/loop/vuelta139_2b_mutaciones.py en un",
            "temporal y se borra al terminar (P.16). No es ningun reporte real.",
            "",
            "| medida | valor | fichero |",
            "|---|---|---|",
            "| el conteo de la apertura | %d lineas | `%s` |" % (malas, fichero_testigo),
            "",
        ])
        ruta_mut = os.path.join(tmp, "sujeto_mutado.md")
        io.open(ruta_mut, "w", encoding="utf-8", newline="\n").write(cuerpo_mut)

        cod_v, txt_v = correr_guarda(vieja, ruta_mut)
        cod_n, txt_n = correr_guarda(nueva, ruta_mut)
        vistas_v = cifras_vistas(vieja, ruta_mut)
        vistas_n = cifras_vistas(nueva, ruta_mut)
        print("")
        print("    GUARDA VIEJA (blob de %s): exit %d, cifras vistas %d"
              % (acta138[:8], cod_v, vistas_v))
        for l in txt_v.splitlines():
            print("       %s" % l)
        print("")
        print("    GUARDA NUEVA (arbol de hoy): exit %d, cifras vistas %d"
              % (cod_n, vistas_n))
        for l in txt_n.splitlines():
            print("       %s" % l)
        ok_i = (cod_v == 0 and vistas_v == 0 and cod_n != 0 and vistas_n == 1)
        print("")
        print("    LA VIEJA LA DEJA PASAR INVISIBLE (exit 0, cero cifras vistas) y")
        print("    LA NUEVA CAE EN ROJO nombrandola: %s" % ok_i)
        veredictos.append(("(i) fila de tabla con cifra que no cuadra",
                           "VERDE, vieja exit %d ve %d / nueva exit %d ve %d"
                           % (cod_v, vistas_v, cod_n, vistas_n) if ok_i else
                           "ROJO, vieja exit %d ve %d / nueva exit %d ve %d"
                           % (cod_v, vistas_v, cod_n, vistas_n)))

        # ------------------------------------------------------------------
        # (iii) EL REPORTE DE LA 138 TAL COMO ESTA EN GIT.
        # ------------------------------------------------------------------
        print("")
        print("-" * 78)
        print("(iii) EL REPORTE DE LA VUELTA 138, TAL COMO ESTA EN GIT.")
        commit_reporte = git(["log", "-1", "--pretty=format:%H", "--",
                              REPORTE_REL]).decode("utf-8").strip()
        datos_138 = git(["show", "%s:%s" % (commit_reporte, REPORTE_REL)])
        ruta_138 = os.path.join(tmp, "reporte_138.md")
        io.open(ruta_138, "wb").write(datos_138)
        texto_138 = normalizar(datos_138).decode("utf-8")
        print("    blob leido de %s (ultimo commit que toca %s)"
              % (commit_reporte[:8], REPORTE_REL))
        print("    filas de tabla en el reporte de la 138: %d"
              % contar_filas_de_tabla(texto_138))

        vistas_v138 = cifras_vistas(vieja, ruta_138)
        vistas_n138 = cifras_vistas(nueva, ruta_138)
        cod_v138, txt_v138 = correr_guarda(vieja, ruta_138)
        cod_n138, txt_n138 = correr_guarda(nueva, ruta_138)
        print("")
        print("    CIFRAS QUE VE LA GUARDA VIEJA : %d   (exit %d)" % (vistas_v138, cod_v138))
        print("    CIFRAS QUE VE LA GUARDA NUEVA : %d   (exit %d)" % (vistas_n138, cod_n138))
        print("    CIFRAS QUE LA CEGUERA PERDIA  : %d" % (vistas_n138 - vistas_v138))
        for l in txt_v138.splitlines():
            if l.startswith("COBERTURA:"):
                print("    COBERTURA de la VIEJA: %s" % l[len("COBERTURA:"):].strip())
        for l in txt_n138.splitlines():
            if l.startswith("COBERTURA:"):
                print("    COBERTURA de la NUEVA: %s" % l[len("COBERTURA:"):].strip())
        print("")
        print("    LOS ROJOS DE LA GUARDA NUEVA SOBRE EL REPORTE DE LA 138, CITADOS")
        print("    ENTEROS Y NO RESUMIDOS. El encargo lo dice con estas palabras:")
        print("    \"casi seguro dara ROJO, porque las cifras de tabla nunca se")
        print("    citaron. ESO ES EL EXITO, NO EL FALLO. Lo que se hace con los")
        print("    rojos es CITARLOS, jamas debilitar la guarda ni borrar la tabla.\"")
        for l in txt_n138.splitlines():
            print("       %s" % l)
        ok_iii = vistas_n138 > vistas_v138
        veredictos.append(("(iii) el reporte de la 138, cifras vistas",
                           "VERDE, %d -> %d (%d que la ceguera perdia)"
                           % (vistas_v138, vistas_n138, vistas_n138 - vistas_v138)
                           if ok_iii else
                           "ROJO, vieja %d y nueva %d" % (vistas_v138, vistas_n138)))

        # ------------------------------------------------------------------
        # (iv) EL DELIMITADOR.
        # ------------------------------------------------------------------
        print("")
        print("-" * 78)
        print("(iv) EL DELIMITADOR DE LA CABECERA TALLADA.")
        cabecera = "\n".join([
            nueva.MARCA_CABECERA_ABRE,
            "",
            "| medida | apertura | cierre |",
            "|---|---|---|",
            "| censo | 3853 nodos | 3853 nodos |",
            "",
            nueva.MARCA_CABECERA_CIERRA,
        ])
        cuerpo_otro = "\n".join([
            "",
            "| otra tabla, que NO es la cabecera | valor |",
            "|---|---|",
            "| una fila que la guarda SI tiene que ver | 7 grupos |",
            "",
        ])
        con_marcas = cabecera + "\n" + cuerpo_otro
        sin_marcas = con_marcas.replace(nueva.MARCA_CABECERA_ABRE, "").replace(
            nueva.MARCA_CABECERA_CIERRA, "")

        filas_totales = contar_filas_de_tabla(con_marcas)
        filas_cabecera = contar_filas_de_tabla(cabecera)
        quitado_con = nueva.quitar_bloques_cubiertos(con_marcas)
        quitado_sin = nueva.quitar_bloques_cubiertos(sin_marcas)
        filas_tras_con = contar_filas_de_tabla(quitado_con)
        filas_tras_sin = contar_filas_de_tabla(quitado_sin)
        print("    filas de tabla en el sujeto           : %d" % filas_totales)
        print("    de ellas, dentro de la cabecera       : %d" % filas_cabecera)
        print("    CON las dos marcas, filas que quedan  : %d (se esperaban %d)"
              % (filas_tras_con, filas_totales - filas_cabecera))
        print("    SIN las marcas, filas que quedan      : %d (se esperaban %d, TODAS)"
              % (filas_tras_sin, filas_totales))
        ok_iv_a = (filas_tras_con == filas_totales - filas_cabecera)
        ok_iv_b = (filas_tras_sin == filas_totales)

        print("")
        print("    CON UNA SOLA MARCA: tiene que ser ROJO RUIDOSO, no adivinar.")
        solo_abre = con_marcas.replace(nueva.MARCA_CABECERA_CIERRA, "")
        solo_cierra = con_marcas.replace(nueva.MARCA_CABECERA_ABRE, "")
        ok_iv_c = True
        for etq, sujeto in (("solo la de abrir", solo_abre), ("solo la de cerrar", solo_cierra)):
            try:
                nueva.quitar_bloques_cubiertos(sujeto)
                print("       %-20s NO levanto error: ROJO" % etq)
                ok_iv_c = False
            except ValueError as e:
                print("       %-20s ValueError: %s" % (etq, e))
        veredictos.append(("(iv) el delimitador quita solo lo delimitado",
                           "VERDE" if ok_iv_a else "ROJO, quedaron %d" % filas_tras_con))
        veredictos.append(("(iv) sin marcas no quita nada",
                           "VERDE" if ok_iv_b else "ROJO, quedaron %d" % filas_tras_sin))
        veredictos.append(("(iv) con una sola marca, ROJO ruidoso",
                           "VERDE" if ok_iv_c else "ROJO, no levanto error"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print("")
        print("  temporal retirado (P.16): %s" % (not os.path.exists(tmp)))

    print("")
    print("=" * 78)
    for nombre, v in veredictos:
        print("  %-46s %s" % (nombre, v))
    malos = [v for _, v in veredictos if v.startswith("ROJO")]
    if malos:
        print("ROJO: %d de %d casos no se sostienen." % (len(malos), len(veredictos)))
        print("FIN")
        return 1
    print("VERDE: los %d casos de la 2.b se sostienen." % len(veredictos))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
