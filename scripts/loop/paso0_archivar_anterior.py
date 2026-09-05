# -*- coding: utf-8 -*-
r"""paso0_archivar_anterior.py . EL PASO 0 DEL ESQUELETO DEL REPORTE: EL
ARCHIVADOR ENCHUFADO, Y LA NEGATIVA A ESCRIBIR SI **EL REPORTE QUE SE VA A
PISAR** NO ESTA ARCHIVADO.

--- CORRECCION DECLARADA (vuelta 180, TAREA 4.a). EL TEXTO MENTIA SOBRE SU
    PROPIA MAQUINA, Y LA MAQUINA ESTABA BIEN ---

LO QUE ESTE DOCSTRING DECIA, ESCRITO AQUI Y NO BORRADO (`EJECUTOR.md` 8, una
correccion que tapa lo que corrige no se puede auditar):

    "EL ARCHIVADOR ENCHUFADO, Y LA NEGATIVA A ESCRIBIR SI EL REPORTE ANTERIOR
     NO ESTA ARCHIVADO."
    "(a) el archivador no sale VERDE para la vuelta anterior; o"
    "    ok, informe = PASO0.exigir_archivado(N - 1)"

POR QUE ESTABA MAL. Desde la vuelta 174 el esqueleto **no pregunta por
`VUELTA - 1`**: lee el numero de la cabecera del `REPORTE.md` que hay en el
arbol, con `vuelta_del_reporte_del_arbol()`, y le pasa **ese** numero a esta
funcion. O sea que esta guarda responde por **el reporte que se va a pisar**, que
es lo unico que importa, y su texto seguia describiendo la pregunta vieja. Las
dos coinciden **casi siempre** y por eso la mentira no molestaba a nadie: solo
difieren el dia en que una vuelta se corta sin archivar, que es exactamente el
dia en que esta guarda tiene que servir.

EL PARAMETRO SE LLAMA HOY `vuelta_del_reporte_a_pisar`, y antes se llamaba
`vuelta_anterior`. Un nombre de parametro es texto que describe la maquina, y
ese tambien mentia.

QUE NO CAMBIA: **la maquina, ni un byte**. Todos los llamadores pasan el numero
en posicion, no por nombre, y siguen pasando lo mismo.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como `archivar_reporte.py`,
`serie_de_registros.py` y `tallar_cabecera_reporte.py`: el esqueleto de cada
vuelta lo IMPORTA y le pasa su numero. NO se clona por vuelta, para que el
enchufe no pueda quedarse en una vuelta y perderse en la siguiente.

POR QUE NACE (adjudicacion 6.6 del acta 170, que resuelve el `D.2` del reporte
de la 170). La adjudicacion 6.4 del acta 169 le dio nombre de fichero a una sede
que solo tenia hash, y nacio `scripts/loop/archivar_reporte.py`. Pero **un
archivador que hay que acordarse de correr no cierra ese agujero, lo aplaza**.
Y la vuelta 170 acaba de demostrar de que va: **el esqueleto sobreescribe
`docs/loop/REPORTE.md` sin preguntar**, y si el reporte anterior no esta
archivado, lo unico que queda de el es el commit que lo llevaba. Peor: si ese
commit NO EXISTE (que es exactamente lo que paso en la 170, cuyo cierre no se
commiteo), el esqueleto de la vuelta siguiente **destruye texto que no esta en
ningun sitio**.

LA GUARDA, Y ES LA QUE PUEDE CAER, escrita como canon de fallar ruidoso del
banco (seccion 9): el esqueleto NO ESCRIBE si

  (a) el archivador no sale VERDE para la vuelta que se le pide; o
  (b) el fichero archivado `docs/loop/reportes/REPORTE_V<N>.md` no existe; o
  (c) su primera linea no es la cabecera `# REPORTE DE LA VUELTA <N>`; o
  (d) EL QUE DE VERDAD IMPORTA: el `docs/loop/REPORTE.md` que se va a PISAR no
      esta guardado byte a byte en ese archivo. Se cotejan los dos sha256. Si el
      arbol de trabajo trae texto que el archivo no tiene, ese texto se perderia
      al escribir el esqueleto, y por eso se para.

La (d) es la clausula que convierte esto en una guarda y no en un recordatorio:
las tres primeras se pueden cumplir con un archivo VIEJO, y solo la cuarta mira
lo que se va a destruir.

PURO SALVO POR LEER: todos los caminos son parametros, para que el caso positivo
por mutacion pueda apuntar la guarda a copias de trabajo sin tocar el repo y sin
escribir nada.

USO (desde el esqueleto de la vuelta N). SE LE PASA EL NUMERO DEL REPORTE QUE SE
VA A PISAR, LEIDO DE SU PROPIA CABECERA, Y NO `N - 1`:
    import paso0_archivar_anterior as PASO0
    ok, informe = PASO0.exigir_archivado(vuelta_del_reporte_del_arbol(texto))
    for l in informe:
        print(l)
    if not ok:
        sys.exit(1)
"""
import hashlib
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
DIR_ARCHIVO = os.path.join(RAIZ, "docs", "loop", "reportes")
ARCHIVADOR = os.path.join(RAIZ, "scripts", "loop", "archivar_reporte.py")


def sha(texto):
    return hashlib.sha256(texto.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def correr_archivador(vuelta):
    """Llama a archivar_reporte.py. Devuelve (exitcode, salida)."""
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, ARCHIVADOR, "--vuelta", str(vuelta)],
                       cwd=RAIZ, capture_output=True, env=env)
    return r.returncode, (r.stdout.decode("utf-8", errors="replace")
                          + r.stderr.decode("utf-8", errors="replace"))


def exigir_archivado(vuelta_del_reporte_a_pisar, ruta_reporte=None,
                     dir_archivo=None, ejecutar_archivador=True):
    """EL PASO 0. Devuelve (ok, informe), donde informe es una lista de lineas.

    EL PRIMER PARAMETRO ES EL NUMERO DEL REPORTE QUE SE VA A PISAR, no el de la
    vuelta anterior. Se llamo `vuelta_del_reporte_a_pisar` hasta la vuelta 180 y ese nombre
    describia mal lo que la maquina hace desde la 174.

    NO ESCRIBE NADA por si mismo: lo unico que escribe es el archivador, y solo
    cuando `ejecutar_archivador` es cierto. Con `ejecutar_archivador=False` la
    guarda se limita a COMPROBAR, que es como la corre su caso por mutacion."""
    ruta_reporte = ruta_reporte or RUTA_REPORTE
    dir_archivo = dir_archivo or DIR_ARCHIVO
    informe = []
    w = informe.append
    motivos = []

    w("PASO 0. EL ARCHIVADOR, ENCHUFADO (adjudicacion 6.6 del acta 170)")
    w("   el esqueleto va a PISAR %s"
      % os.path.relpath(ruta_reporte, RAIZ).replace(os.sep, "/"))

    if ejecutar_archivador:
        c, sal = correr_archivador(vuelta_del_reporte_a_pisar)
        w("   archivar_reporte.py --vuelta %d -> EXIT %d" % (vuelta_del_reporte_a_pisar, c))
        for l in sal.splitlines():
            if l.strip():
                w("      | " + l.rstrip())
        if c != 0:
            motivos.append("(a) el archivador NO sale verde para la vuelta %d"
                           % vuelta_del_reporte_a_pisar)
    else:
        w("   archivar_reporte.py NO se lanza (modo solo comprobacion)")

    destino = os.path.join(dir_archivo, "REPORTE_V%d.md" % vuelta_del_reporte_a_pisar)
    rel_destino = os.path.relpath(destino, RAIZ).replace(os.sep, "/")
    if not os.path.exists(destino):
        motivos.append("(b) no existe el archivo %s" % rel_destino)
        w("   %s -> NO EXISTE" % rel_destino)
        return (False, informe + _cierre(motivos, w))
    archivado = io.open(destino, encoding="utf-8").read()
    w("   %s -> %d bytes, sha256 %s"
      % (rel_destino, len(archivado.replace("\r\n", "\n").encode("utf-8")),
         sha(archivado)[:16]))

    primera = archivado.replace("\r\n", "\n").split("\n", 1)[0]
    m = re.match(r"^#\s*REPORTE DE LA VUELTA\s+(\d+)\b", primera)
    if not m:
        motivos.append("(c) la primera linea del archivo no es una cabecera de reporte")
    elif int(m.group(1)) != vuelta_del_reporte_a_pisar:
        motivos.append("(c) el archivo %s lleva el reporte de la VUELTA %s"
                       % (rel_destino, m.group(1)))
    w("   vuelta leida de la cabecera del archivo: %s"
      % (m.group(1) if m else "(no es cabecera)"))

    if not os.path.exists(ruta_reporte):
        w("   el reporte del arbol NO EXISTE: no hay nada que pisar")
    else:
        vivo = io.open(ruta_reporte, encoding="utf-8").read()
        w("   el reporte que se va a pisar -> %d bytes, sha256 %s"
          % (len(vivo.replace("\r\n", "\n").encode("utf-8")), sha(vivo)[:16]))
        if sha(vivo) != sha(archivado):
            motivos.append(
                "(d) EL TEXTO QUE SE VA A PISAR NO ESTA GUARDADO: el REPORTE.md del "
                "arbol (sha256 %s) NO ES el archivado en %s (sha256 %s). Escribir el "
                "esqueleto encima perderia ese texto."
                % (sha(vivo)[:16], rel_destino, sha(archivado)[:16]))
        else:
            w("   LOS DOS sha256 CALZAN: lo que se va a pisar ya esta guardado")

    return (not motivos, informe + _cierre(motivos, w))


def _cierre(motivos, w):
    cola = []
    if motivos:
        cola.append("   ROJO, %d motivo(s). EL ESQUELETO NO ESCRIBE:" % len(motivos))
        for m in motivos:
            cola.append("      " + m)
    else:
        cola.append("   VERDE: el reporte anterior esta archivado y lo que se va a")
        cola.append("   pisar esta guardado byte a byte. El esqueleto puede escribir.")
    return cola


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    v = int(sys.argv[1]) if len(sys.argv) > 1 else 170
    ok, inf = exigir_archivado(v)
    for l in inf:
        print(l)
    sys.exit(0 if ok else 1)
