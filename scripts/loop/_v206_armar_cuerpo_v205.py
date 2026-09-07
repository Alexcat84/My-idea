# -*- coding: utf-8 -*-
r"""_v206_armar_cuerpo_v205.py . COMPUTO DE LA VUELTA 206, NO MAQUINARIA.

Prefijo de guion bajo: fuera del censo y fuera de la nomina (congelada en 135),
no anade guarda ni lector que se quede vigilando y muere con la vuelta.

QUE HACE: arma el CUERPO DEL CIERRE de la vuelta 205 a partir del borrador que
aquella vuelta dejo escrito (`scripts/loop/_v205_cierre_texto.md`), rellenando
sus tres huecos CON EL CONTENIDO DE FICHEROS DE SALIDA y no tecleando ninguna
celda, y anexando las dos CORRECCIONES DECLARADAS que mi medicion de hoy obliga.

LA CORRECCION NO BORRA EL TEXTO VIEJO (`EJECUTOR.md` 8, "una correccion que tapa
lo que corrige no se puede auditar"): el parrafo original se queda entero donde
esta, y debajo va la correccion con la medicion del dia.
"""
import hashlib
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

BORRADOR = os.path.join(AQUI, "_v205_cierre_texto.md")
DESTINO = os.path.join(AQUI, "_v206_cierre_texto_v205.md")
TABLA = os.path.join(LOOP, "SALIDA_V205_TABLA_TRAMOS.txt")
NUMSTAT = os.path.join(LOOP, "SALIDA_V206_NUMSTAT_V205.txt")


def leer(p):
    return io.open(p, encoding="utf-8", errors="replace").read().replace(chr(13) + NL, NL)


def medidas(p):
    b = io.open(p, "rb").read()
    lf = b.replace(b"\r\n", b"\n")
    return len(b), len(lf), hashlib.sha256(lf).hexdigest()[:16]


CORRECCION_35 = """
**CORRECCION DECLARADA, HECHA EN LA VUELTA 206 AL CERRAR ESTE REPORTE, Y EL
TEXTO VIEJO SE QUEDA ENTERO ARRIBA** (`EJECUTOR.md` 8, "una correccion que tapa
lo que corrige no se puede auditar").

**LO QUE EL PARRAFO DE ARRIBA AFIRMA Y NO ES CIERTO:** que el desglose de la
linea `CIFRA de FALLO` es "identico en los once" con **0 que no mordieron**, y
que "NINGUNA DE LAS 135 ENTRADAS DE LA NOMINA FALLA".

**LO QUE MIDO YO HOY, CONTANDO LOS ONCE FICHEROS SELLADOS UNO A UNO**, con
`python scripts/loop/_v206_medir_no_mordio.py`, salida cruda en
`docs/loop/SALIDA_V206_NO_MORDIO.txt` (4151 bytes en disco y 4103 normalizado a
LF, sha256 LF `cffa5cd0724d0427`):

- **CIFRA familias distintas de la linea `CIFRA de FALLO` entre los once: 3**, no
  una. Las tres se diferencian SOLO en el segundo sumando: **0**, **1** y **2**
  que no mordieron.
- **CIFRA entradas de la nomina que NO MORDIERON en la bateria de la 205: 5**,
  repartidas en **4** tramos, y son estas cinco, con su tramo y su `exit`:

| tramo | entrada de la nomina que NO MORDIO | `exit` que publico |
|---|---|---:|
| 3 | `vuelta160_tarea6b_mutacion_puerta.py` | 3221225794 |
| 4 | `vuelta163_tarea4b_mutacion_re_sellado.py` | 1 |
| 5 | `vuelta165_tarea6_mutacion_op_l_01.py` | 1 |
| 5 | `vuelta166_tarea6_mutacion_guarda.py` | 1 |
| 9 | `vuelta185_tarea1c_mutacion_bateria_continuada.py` | 1 |

- **`ANCLA PERDIDA` y `NO REPRODUCIBLE` SI dan 0 en los once**, y eso del parrafo
  viejo SI se sostiene con la medicion de hoy.

**ESTO NO LO ARREGLO YO Y SUBE COMO PARADA EN EL REPORTE DE LA VUELTA 206**, por
`EJECUTOR.md` 5: contradice una cifra publicada con su corte, la adjudicacion
`5.3` del acta 205, que dice que los once tramos salen rojos "por una sola
causa". Medido, las causas del rojo son **dos**: los **2** arneses del censo que
la nomina congelada no admite, y estas **5** entradas que no mordieron.
"""

CORRECCION_82 = """
**CORRECCION DECLARADA, HECHA EN LA VUELTA 206 AL CERRAR ESTE REPORTE, Y EL
TEXTO VIEJO SE QUEDA ENTERO ARRIBA** (`EJECUTOR.md` 8).

**LO QUE LA `D.2` Y LA `C.1` AFIRMAN Y SE QUEDA CORTO:** dicen que el ciclo de
Gate 0 de apertura "lo corri tarde". Medido hoy: en el arbol del cierre de la
vuelta 205 **no habia NI UNO** de los seis ficheros que el tallador lee para la
columna de apertura, o sea que ese ciclo **no se corrio tarde: no se corrio**.
`git log --all -- docs/loop/SALIDA_V205_GATE0_CMD1_APERTURA.txt` no encontro
ninguna aparicion, y el rechazo sellado de aquella vuelta,
`docs/loop/SALIDA_V205_TALLADOR_RECHAZO.txt`, lo nombra en su primera linea de
celdas.

**QUIEN LOS ESCRIBIO Y CUANDO, DICHO SIN ADORNO:** los escribi **yo, el ejecutor
de la vuelta 206**, corriendo `python scripts/loop/_v205_ciclo_gate0.py APERTURA`
en mi propio turno, **8 de 8 comandos en `EXITCODE 0`**, con la salida en
`docs/loop/SALIDA_V206_CICLO_V205_APERTURA.txt`.

**POR QUE ESOS VALORES SIGUEN SIENDO LOS DE LA APERTURA DE LA 205, Y ES UNA
MEDICION Y NO UNA PROMESA:** `git diff --numstat e66bf67d..HEAD` sobre
`dataset/`, `web/` y `engine/` da **0 filas**, o sea que los tres arboles que ese
ciclo mide son **byte a byte** los que habia en el HEAD de apertura de la 205. Y
el propio ciclo lo confirma por otro camino: los nueve ficheros que escribio hoy
miden exactamente lo mismo que los que el auditor sello en el cierre de la 205
(**4790**, **7928**, **574**, **140**, **168**, **498**, **1131**, **7** y
**336** bytes).

**DONDE ME PUEDO ESTAR EQUIVOCANDO, Y VA MARCADO COMO DISCUTIBLE EN EL REPORTE
DE LA 206:** la letra de `EJECUTOR.md` 1 dice que la apertura se mide antes de la
primera operacion, y **no dice** "o despues, si puedes probar que nada se movio".
Si el auditor lee la letra estrecha, la columna de apertura de la cabecera de
este reporte es una **reconstruccion** y no una medicion de aquel momento, y asi
queda dicho aqui en vez de esconderse detras de una tabla tallada.
"""


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    texto = leer(BORRADOR)
    tabla = leer(TABLA).strip(NL)
    numstat = leer(NUMSTAT).strip(NL)
    bd, bl, sh = medidas(TABLA)

    print("EL CUERPO DEL CIERRE DE LA 205, ARMADO DE SUS FICHEROS")
    print("=" * 78)
    print("  borrador de partida: %s"
          % os.path.relpath(BORRADOR, RAIZ).replace(os.sep, "/"))
    print("  CIFRA bytes del borrador: %d en disco y %d normalizado a LF"
          % medidas(BORRADOR)[:2])

    huecos = ["BYTES_TABLA_AQUI", "TABLA_TRAMOS_AQUI", "NUMSTAT_AQUI"]
    for h in huecos:
        print("  CIFRA apariciones del hueco %-18s %d" % (h, texto.count(h)))
        if texto.count(h) != 1:
            print("ROJO: el hueco %s no aparece exactamente una vez." % h)
            return 1

    texto = texto.replace(
        "BYTES_TABLA_AQUI",
        "**%d** bytes en disco y **%d** normalizado a LF, sha256 LF `%s`"
        % (bd, bl, sh))
    texto = texto.replace("TABLA_TRAMOS_AQUI", tabla)
    texto = texto.replace("NUMSTAT_AQUI", numstat)

    ancla35 = NL + "### 3.6 LOS DOS CASOS DECLARADOS"
    if texto.count(ancla35) != 1:
        print("ROJO: no encuentro exactamente un ancla para la correccion de la 3.5.")
        return 1
    texto = texto.replace(ancla35,
                          NL + CORRECCION_35.strip(NL) + NL + NL + ancla35.lstrip(NL))

    ancla82 = NL + "## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE"
    if texto.count(ancla82) != 1:
        print("ROJO: no encuentro exactamente un ancla para la correccion de la 8.")
        return 1
    texto = texto.replace(ancla82,
                          NL + CORRECCION_82.strip(NL) + NL + NL + ancla82.lstrip(NL))

    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto.rstrip(NL) + NL)
    d, l, s = medidas(DESTINO)
    print("")
    print("  ESCRITO: %s" % os.path.relpath(DESTINO, RAIZ).replace(os.sep, "/"))
    print("  CIFRA bytes del cuerpo armado: %d en disco y %d normalizado a LF" % (d, l))
    print("  CIFRA sha256 LF del cuerpo armado: %s" % s)
    print("  CIFRA huecos que quedan sin rellenar: %d"
          % sum(texto.count(h) for h in huecos))
    print("  CIFRA guiones largos: %d | CIFRA guiones medios: %d"
          % (texto.count(chr(8212)), texto.count(chr(8211))))
    secciones = [x for x in texto.split(NL) if x.startswith("## ")]
    print("  CIFRA secciones de primer nivel: %d" % len(secciones))
    for x in secciones:
        print("      %s" % x[:80])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
