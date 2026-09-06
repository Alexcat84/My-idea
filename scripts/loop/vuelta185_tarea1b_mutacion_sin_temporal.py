# -*- coding: utf-8 -*-
r"""vuelta185_tarea1b_mutacion_sin_temporal.py . EL ARNES DE LA REPARACION DE LA
TAREA 1.b: LA SALIDA SELLADA DE
`scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py` DEJA DE CAMBIAR
SOLA.

QUE PRUEBA, EN DOS MITADES QUE FALLAN POR SEPARADO:

  MITAD A, SOBRE LA FUNCION PURA `sin_temporal()`. Un caso por cada forma de la
  ruta del temporal (absoluta, relativa con barra normal, relativa con barra
  invertida y nombre base suelto), MAS un caso que exige que una linea SIN
  NINGUNA RUTA salga IDENTICA, byte a byte, para que la funcion no normalice de
  mas. TODOS TIENEN QUE CAER AL MUTAR SU ESPERADO, y la mutacion se corre y se
  publica caso por caso.

  MITAD B, LA DE VERDAD. Corre el arnes reparado DOS VECES, cada una EN UN
  PROCESO APARTE, y exige que el `sha256` de
  `docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt` sea EL MISMO despues
  de las dos, y que LAS DOS CORRIDAS SALGAN `exit 0`. Si la normalizacion se
  quitara, esta mitad cae.

LO QUE ESTE ARNES NO PUEDE PROBAR, Y SE DICE EN VEZ DE DARLO POR HECHO: la
reparacion NO se verifica contra la bateria, porque la 185 NO ES VUELTA DE
BATERIA (`AUDITOR.md` 6.1: corre cada cinco vueltas y la siguiente es la 189).
LA PRUEBA DE ESTA VUELTA ES LA DOBLE CORRIDA DE LA MITAD B; LA PRUEBA
DEFINITIVA SERA LA BATERIA DE LA 189.

Y SE DECLARA LO QUE ESTE ARNES ENSUCIA: correr el sujeto REESCRIBE su salida
sellada, `docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt`. El fichero
que queda en disco al terminar es el de la forma REPARADA, con `<TEMPORAL>`
dentro. Es esperado y se dice, no se disimula.

NINGUNA COMPARACION DE AQUI ES ENTRE DOS CONSTANTES LITERALES: todos los
veredictos salen de llamar a la funcion de verdad o de medir el fichero de
verdad.

USO:
  python scripts/loop/vuelta185_tarea1b_mutacion_sin_temporal.py
"""
import hashlib
import io
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta182_tarea2_mutacion_apertura_auditor as SUJETO   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
BARRA_INV = chr(92)
PY = sys.executable
RUTA_SUJETO = "scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py"
RUTA_SALIDA = os.path.join(LOOP, "SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt")
DESTINO = os.path.join(LOOP, "SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt")

MARCA = "<TEMPORAL>"

# UN TEMPORAL DE VERDAD, FABRICADO Y RETIRADO (`P.16`, quien fabrica limpia). Se
# fabrica de verdad y no se teclea POR UNA MEDICION, no por gusto: la primera
# version de este arnes usaba un temporal INVENTADO bajo un `C:\Users\quien\...`
# que no existe, y sus dos casos de ruta relativa SALIERON EN ROJO. No porque la
# funcion estuviera mal, sino porque `os.path.relpath` de un temporal inventado
# no es la cadena que yo habia tecleado como entrada. LO QUE PASABA ANTES NO SE
# BORRA, SE CUENTA: esa corrida en rojo esta en el reporte con su salida entera.
TMP = tempfile.mkdtemp(prefix="v185_arnes_sin_temporal_")
BASE = os.path.basename(TMP)


def mostrar(linea):
    """LA LINEA DE ENTRADA, PREPARADA PARA PEGARLA EN LA SALIDA SELLADA SIN
    METERLE DENTRO EL SUFIJO ALEATORIO. PURA.

    POR QUE EXISTE, Y ES LA MISMA AVERIA QUE ESTE ARNES REPARA: las entradas de
    la mitad A llevan la ruta del temporal DENTRO, que es de lo que tratan, y
    pegarlas crudas dejaria en esta salida sellada un dato que cambia solo. Seria
    escribir la averia dentro de su propio remedio. Se sustituye SOLO el nombre
    base por `<BASE>`, y la forma de la ruta se conserva para que se siga viendo
    que caso es cual."""
    return linea.replace(BASE, "<BASE>")


def sha(ruta):
    if not os.path.exists(ruta):
        return None, None
    datos = io.open(ruta, "rb").read()
    return hashlib.sha256(datos).hexdigest(), len(datos)


def casos_de_la_mitad_a():
    """LOS CASOS DE LA FUNCION PURA. Cada uno es (nombre, linea de entrada,
    salida esperada). El esperado es lo unico escrito a mano; la salida SALE de
    llamar a `sin_temporal()` de verdad.

    LAS ENTRADAS SE FABRICAN CON LAS MISMAS FORMAS QUE EL INFORME DE `sellar()`
    produce de verdad, y por eso el temporal es real: la forma relativa que salio
    en las lineas 53 a 55 de la salida sellada es `os.path.relpath` desde la raiz
    del repo, y sobre un temporal inventado esa cadena seria otra."""
    absoluta = os.path.abspath(TMP)
    rela = os.path.relpath(absoluta)
    rel_barra = rela.replace(BARRA_INV, "/")
    rel_inv = rela.replace("/", BARRA_INV)
    return [
        ("LA ABSOLUTA, tal cual la devuelve mkdtemp",
         "SELLO ESCRITO: " + absoluta + BARRA_INV + "SELLO.json (582 bytes)",
         "SELLO ESCRITO: " + MARCA + BARRA_INV + "SELLO.json (582 bytes)"),
        ("LA RELATIVA CON BARRA NORMAL, la que salio de verdad en la linea 53",
         "   ciega   " + rel_barra + "/_auditor_ciega_blind.txt -> 3823 bytes",
         "   ciega   " + MARCA + "/_auditor_ciega_blind.txt -> 3823 bytes"),
        ("LA RELATIVA CON BARRA INVERTIDA",
         "   destape " + rel_inv + BARRA_INV + "_reveal.txt -> 2273 bytes",
         "   destape " + MARCA + BARRA_INV + "_reveal.txt -> 2273 bytes"),
        ("EL NOMBRE BASE SUELTO, sin ninguna carpeta delante",
         "temporal borrado: " + BASE + " (True)",
         "temporal borrado: " + MARCA + " (True)"),
        ("UNA LINEA SIN NINGUNA RUTA: TIENE QUE SALIR IDENTICA",
         "   sellar() devuelve: True, y no hay ninguna ruta en esta linea",
         "   sellar() devuelve: True, y no hay ninguna ruta en esta linea"),
        ("UNA LINEA CON OTRO TEMPORAL QUE NO ES EL SUYO: NO SE TOCA",
         "   ciega   ../../Temp/v182_apertura_OTRO/_blind.txt -> 1 bytes",
         "   ciega   ../../Temp/v182_apertura_OTRO/_blind.txt -> 1 bytes"),
        # EL LIMITE DE LA FUNCION, DECLARADO COMO CASO EN VEZ DE ESCONDIDO. Una
        # ruta relativa a OTRO sitio que no es el directorio de trabajo NO se
        # sustituye entera: se le va el nombre base y le queda el prefijo. Y ESO
        # BASTA PARA LO QUE ESTA GUARDA EXISTE, porque el prefijo es fijo y lo
        # unico que cambiaba entre dos corridas era el sufijo aleatorio. Se
        # afirma el valor exacto, no un "no es lo de antes".
        ("EL LIMITE: UNA RELATIVA A OTRO SITIO PIERDE SOLO EL NOMBRE BASE, Y ESO"
         " YA ES DETERMINISTA",
         "   ciega   ../../otro/sitio/" + BASE + "/_blind.txt -> 3823 bytes",
         "   ciega   ../../otro/sitio/" + MARCA + "/_blind.txt -> 3823 bytes"),
    ]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    fallos = 0
    w("ARNES DE LA REPARACION DE LA TAREA 1.b DE LA VUELTA 185")
    w("sujeto vivo: %s" % RUTA_SUJETO)
    w("")

    if not hasattr(SUJETO, "sin_temporal"):
        w("ROJO: el sujeto NO tiene sin_temporal(). La reparacion no esta puesta,")
        w("      y este arnes no puede probar nada.")
        t = NL.join(L) + NL
        io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(t)
        print(t)
        return 1

    w("MITAD A. LA FUNCION PURA sin_temporal(), CASO POR CASO")
    w("   el temporal es REAL y se fabrica con mkdtemp, como el sujeto, para que")
    w("   la forma relativa de las entradas sea la que sellar() produce de verdad.")
    w("   SU NOMBRE NO SE PUBLICA AQUI: cambia en cada corrida, y esta salida no")
    w("   puede llevar dentro el mismo dato que cambia solo que se viene a quitar.")
    w("")
    casos = casos_de_la_mitad_a()
    for nombre, entrada, esperado in casos:
        medido = SUJETO.sin_temporal(entrada, TMP)
        ok = medido == esperado
        if not ok:
            fallos += 1
        w("   %s" % nombre)
        w("      entrada : %s" % mostrar(entrada)[:150])
        w("      medido  : %s" % medido[:150])
        w("      esperado: %s" % esperado[:150])
        w("      -> %s" % ("CALZA" if ok else "NO CALZA"))
    w("")
    w("   CIFRA casos de la mitad A: %d" % len(casos))
    w("   CIFRA que CALZAN: %d" % (len(casos) - fallos))
    w("   CIFRA que NO CALZAN: %d" % fallos)
    w("")

    w("   LA MUTACION DEL ESPERADO, CASO POR CASO, QUE ES LO QUE PRUEBA QUE ESTOS")
    w("   CASOS PUEDEN CAER. El esperado mutado es el bueno con una letra mas")
    w("   pegada al final: si el caso pasara igual, no estaria comparando nada.")
    n_caen = 0
    for nombre, entrada, esperado in casos:
        medido = SUJETO.sin_temporal(entrada, TMP)
        mutado = esperado + "X"
        cae = medido != mutado
        if cae:
            n_caen += 1
        else:
            fallos += 1
        w("      %-62s con el esperado MUTADO -> %s"
          % (nombre[:62], "CAE" if cae else "PASA, Y NO DEBERIA"))
    w("   CIFRA casos que CAEN al mutar su esperado: %d de %d" % (n_caen, len(casos)))
    if n_caen != len(casos):
        w("   ROJO: no todos los casos caen al mutar su esperado.")
    w("")

    w("   LA SEGUNDA MUTACION DE LA MITAD A: QUE LA FUNCION NO NORMALICE DE MAS.")
    w("   Se le pasa un temporal VACIO y una linea con una ruta dentro, y la linea")
    w("   tiene que salir IDENTICA porque no hay nada que sustituir.")
    entrada_x = "   ciega   ../../Temp/" + BASE + "/_blind.txt -> 3823 bytes"
    w("      la linea de prueba, con el nombre base tapado para no meterlo aqui:")
    w("      %s" % mostrar(entrada_x))
    sin_tmp = SUJETO.sin_temporal(entrada_x, "")
    ok_x = sin_tmp == entrada_x
    w("      con tmp vacio, la linea sale identica: %s" % ("SI" if ok_x else "NO"))
    w("      y con el tmp de verdad, la misma linea cambia: %s"
      % ("SI" if SUJETO.sin_temporal(entrada_x, TMP) != entrada_x else "NO"))
    if not ok_x or SUJETO.sin_temporal(entrada_x, TMP) == entrada_x:
        fallos += 1
    w("")

    w("MITAD B. LA DOBLE CORRIDA DEL ARNES REPARADO, EN DOS PROCESOS APARTE")
    w("   (es la misma vara que la bateria usa: byte a byte entre dos corridas)")
    w("   SE DECLARA LO QUE ESTO ENSUCIA: cada corrida REESCRIBE")
    w("   docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt. El fichero que")
    w("   queda al terminar es el de la forma REPARADA, con <TEMPORAL> dentro.")
    w("")
    antes_sha, antes_bytes = sha(RUTA_SALIDA)
    w("   ANTES DE LAS DOS CORRIDAS: %s bytes, sha256 %s"
      % (antes_bytes, (antes_sha or "(no existe)")[:64]))
    medidas = []
    for k in (1, 2):
        env = dict(os.environ)
        env["PYTHONIOENCODING"] = "utf-8"
        r = subprocess.run([PY, RUTA_SUJETO], cwd=RAIZ, capture_output=True, env=env)
        s, b = sha(RUTA_SALIDA)
        medidas.append((r.returncode, s, b))
        w("   CORRIDA %d -> exitcode %d | %s bytes | sha256 %s"
          % (k, r.returncode, b, (s or "(no existe)")[:64]))
    w("")
    exitcodes = [c for c, _s, _b in medidas]
    shas = [s for _c, s, _b in medidas]
    bytes_ = [b for _c, _s, b in medidas]
    ok_exit = all(c == 0 for c in exitcodes)
    ok_sha = shas[0] is not None and shas[0] == shas[1]
    w("   LAS DOS CORRIDAS SALEN exit 0: %s (%s)"
      % ("SI" if ok_exit else "NO", exitcodes))
    w("   EL sha256 ES EL MISMO DESPUES DE LAS DOS: %s" % ("SI" if ok_sha else "NO"))
    w("   LOS BYTES SON LOS MISMOS: %s (%s)"
      % ("SI" if bytes_[0] == bytes_[1] else "NO", bytes_))
    if not ok_exit:
        fallos += 1
    if not ok_sha:
        fallos += 1
    w("")
    texto_salida = io.open(RUTA_SALIDA, encoding="utf-8", errors="replace").read()
    n_marca = texto_salida.count(MARCA)
    n_prefijo = texto_salida.count("v182_apertura_")
    w("   LA SALIDA SELLADA, CONTADA DE SU PROPIO FICHERO DESPUES DE LAS DOS:")
    w("      CIFRA apariciones de %r: %d" % (MARCA, n_marca))
    w("      CIFRA apariciones de 'v182_apertura_' (el prefijo del mkdtemp): %d"
      % n_prefijo)
    if n_marca == 0:
        w("      ROJO: la marca no aparece, o sea que la normalizacion no corrio.")
        fallos += 1
    w("")
    w("   LAS LINEAS 53, 54 Y 55, QUE ERAN LAS QUE CAMBIABAN SOLAS, PEGADAS:")
    lineas_salida = texto_salida.replace(chr(13) + NL, NL).split(NL)
    for k in (53, 54, 55):
        if k <= len(lineas_salida):
            w("      LINEA %d: %s" % (k, lineas_salida[k - 1].rstrip()[:150]))
    w("")
    w("LO QUE ESTE ARNES NO PRUEBA, DICHO EN VEZ DE DARLO POR HECHO: la reparacion")
    w("NO se verifica contra la bateria, porque la 185 no es vuelta de bateria")
    w("(AUDITOR.md 6.1: corre cada cinco vueltas y la siguiente es la 189). La")
    w("prueba de esta vuelta es la doble corrida de arriba; la prueba definitiva")
    w("sera la bateria de la 189.")
    w("")
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))

    w("")
    w("EL TEMPORAL FABRICADO POR ESTE ARNES SE RETIRA (`P.16`, quien fabrica")
    w("limpia). Su nombre base no se publica: cambia en cada corrida y publicarlo")
    w("seria meter en esta salida el mismo dato que cambia solo que la reparacion")
    w("viene a quitar.")

    t = NL.join(L) + NL
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (DESTINO, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    try:
        codigo = main()
    finally:
        shutil.rmtree(TMP, ignore_errors=True)
    sys.exit(codigo)
