# -*- coding: utf-8 -*-
r"""vuelta191_tarea5_marca_contra_dificultad.py . LA MARCA `DISCUTIBLE MARCADO`
CONTRA LA DIFICULTAD MEDIDA, SOBRE TODA LA HISTORIA DE CIEGAS QUE SE PUEDE LEER
DE FICHEROS DEL REPO.

ESTO ES UNA MEDICION Y NO UN ARREGLO, Y LA LINEA ES DEL ENCARGO: **no se escribe
ni una fila de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.** Ponerle la marca a ocho
razones sobre una muestra de treinta seria editar datos publicados, y eso ni lo
adjudica el auditor ni lo hace esta vuelta. El archivo se abre en LECTURA y su
`sha256` se mide al entrar y al salir.

--- EL UNIVERSO SE DECLARA ANTES DE CONTAR, Y ESA ES LA MITAD DEL ENCARGO ---

**UN UNIVERSO ELEGIDO DESPUES DE VER EL RESULTADO NO SIRVE**, asi que las dos
reglas van escritas aqui, en el codigo, antes de la primera cuenta:

  REGLA 1, LOS CANDIDATOS. Son los ficheros `.txt` y `.md` de `docs/loop/` cuyo
  NOMBRE contiene `COTEJO`, en cualquier caja. Es la forma con que esta casa
  nombra sus cotejos de ciega. **Y para que la eleccion del nombre tambien se
  pueda auditar**, se publica ADEMAS la lista de ficheros de `docs/loop/` que
  contienen la palabra `DISCREPA` y que esta regla de nombre deja fuera: si esa
  lista trae algo importante, se ve.

  REGLA 2, LA LEGIBILIDAD. Un candidato ENTRA si y solo si trae al menos una
  linea que contenga **a la vez** un numero y la palabra `DISCREPA` como palabra
  entera (`\bDISCREPA\b`, que NO casa con `DISCREPAN` ni con `DISCREPANCIAS`), y
  de esa linea se toma **el primer numero** como puesto. El puesto ademas tiene
  que EXISTIR en el archivo. **Cualquier otro formato queda FUERA y se nombra**,
  aunque sea un cotejo de ciega de verdad: eso es lo que significa "no legible
  con una regla unica", y la casa tiene al menos seis formatos distintos de
  cotejo.

LO QUE ESTA MEDICION NO PUEDE HACER, DICHO ANTES DE PUBLICAR SU CIFRA. **No
recupera el DENOMINADOR**: varios de los ficheros que entran solo listan las
discrepancias y no los aciertos, asi que "cuantos puestos se leyeron en total" no
sale de la misma regla. Se publica lo que si sale y se dice que lo otro no sale.

LAS TRES CIFRAS QUE EL ENCARGO PIDE, JUNTAS O NINGUNA:
  1. cuantos puestos han tumbado alguna vez a un lector,
  2. cuantos de esos llevan `DISCUTIBLE MARCADO` en su razon,
  3. cual es la tasa de la marca en el archivo entero, para poder comparar.

USO:
  python scripts/loop/vuelta191_tarea5_marca_contra_dificultad.py
"""
import hashlib
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
SALIDA = os.path.join(LOOP, "SALIDA_V191_T5_MARCA_CONTRA_DIFICULTAD.txt")
ARCHIVO = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
MARCA = "DISCUTIBLE MARCADO"

# LAS DOS REGLAS, EN CODIGO Y NO EN PROSA.
NOMBRE_CANDIDATO = "COTEJO"
PAT_DISCREPA = re.compile(r"\bDISCREPA\b")
PAT_NUMERO = re.compile(r"\d+")
# LA MISMA REGLA PARA EL LADO CONTRARIO, QUE HACE FALTA PARA PODER DECIR CUANTOS
# SE LEYERON EN LOS FICHEROS DONDE SI SE PUEDE.
PAT_COINCIDE = re.compile(r"\bCOINCIDE\b")


def sha_de(ruta):
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return len(datos), len(lf), hashlib.sha256(lf).hexdigest()


def puestos_de_un_fichero(texto, validos):
    """LOS PUESTOS QUE UN FICHERO DECLARA DISCREPANTES Y COINCIDENTES, POR LA
    REGLA 2. PURA. Devuelve `(discrepan, coinciden, rechazadas)`.

    `rechazadas` son las lineas que traian `DISCREPA` y cuyo primer numero NO es
    un puesto del archivo: se cuentan y se publican en vez de tirarse, porque una
    linea descartada en silencio es una cifra que nadie puede cotejar."""
    disc, coin, rech = set(), set(), []
    for linea in texto.replace(chr(13) + NL, NL).split(NL):
        hay_d = bool(PAT_DISCREPA.search(linea))
        hay_c = bool(PAT_COINCIDE.search(linea))
        if not (hay_d or hay_c):
            continue
        nums = PAT_NUMERO.findall(linea)
        if not nums:
            if hay_d:
                rech.append((linea.strip()[:110], "sin ningun numero"))
            continue
        p = int(nums[0])
        if p not in validos:
            if hay_d:
                rech.append((linea.strip()[:110],
                             "su primer numero (%d) no es un puesto del archivo" % p))
            continue
        if hay_d:
            disc.add(p)
        elif hay_c:
            coin.add(p)
    return disc, coin, rech


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 191, TAREA 5: LA MARCA `DISCUTIBLE MARCADO` CONTRA LA DIFICULTAD")
    w("MEDIDA, SOBRE TODA LA HISTORIA DE CIEGAS QUE SE PUEDE LEER DEL REPO")
    w("=" * 78)
    w("")

    w("0) LAS DOS REGLAS DEL UNIVERSO, ESCRITAS ANTES DE LA PRIMERA CUENTA")
    w("   REGLA 1, CANDIDATOS: ficheros .txt y .md de docs/loop/ cuyo NOMBRE")
    w("      contiene %r en cualquier caja." % NOMBRE_CANDIDATO)
    w("   REGLA 2, LEGIBILIDAD: un candidato ENTRA si trae al menos una linea con")
    w("      un numero Y la palabra DISCREPA como palabra entera (no casa con")
    w("      DISCREPAN ni con DISCREPANCIAS), y su primer numero es un puesto que")
    w("      existe en el archivo. Cualquier otro formato queda FUERA y se nombra.")
    w("   Y LO QUE ESTA MEDICION NO PUEDE: recuperar el DENOMINADOR. Varios de los")
    w("      ficheros que entran SOLO listan discrepancias, asi que 'cuantos se")
    w("      leyeron en total' no sale de la misma regla. Se dice en vez de")
    w("      estimarse.")
    w("")

    w("A) EL ARCHIVO, MEDIDO AL ENTRAR Y ABIERTO SOLO EN LECTURA")
    bd, bl, sh = sha_de(ARCHIVO)
    w("   docs/INTRA_DOMINIO_VEREDICTOS.jsonl -> disco %d bytes | LF %d bytes" % (bd, bl))
    w("   sha256 LF: %s" % sh)
    filas = [json.loads(l) for l in io.open(ARCHIVO, encoding="utf-8") if l.strip()]
    por_puesto = {}
    for f in filas:
        por_puesto[f.get("puesto_intra")] = f
    validos = set(por_puesto)
    w("   CIFRA filas: %d | MIN %d | MAX %d"
      % (len(filas), min(validos), max(validos)))
    con_marca = set(p for p, f in por_puesto.items()
                    if MARCA in str(f.get("razon", "")))
    w("   CIFRA filas con %r en su razon: %d" % (MARCA, len(con_marca)))
    tasa_archivo = len(con_marca) / float(len(filas))
    w("   TASA DE LA MARCA EN EL ARCHIVO ENTERO: %.4f (%.2f por ciento)"
      % (tasa_archivo, 100.0 * tasa_archivo))
    w("")

    w("B) LOS CANDIDATOS POR LA REGLA 1, NOMBRADOS UNO A UNO")
    candidatos = []
    for nombre in sorted(os.listdir(LOOP)):
        if not nombre.lower().endswith((".txt", ".md")):
            continue
        if NOMBRE_CANDIDATO not in nombre.upper():
            continue
        candidatos.append(nombre)
    w("   CIFRA candidatos: %d" % len(candidatos))
    for n in candidatos:
        w("      %-52s %8d bytes" % (n, os.path.getsize(os.path.join(LOOP, n))))
    w("")

    w("C) LA REGLA DE NOMBRE, AUDITADA: LOS FICHEROS DE docs/loop/ QUE DICEN")
    w("   `DISCREPA` Y QUE LA REGLA 1 DEJA FUERA")
    fuera_del_nombre = []
    for nombre in sorted(os.listdir(LOOP)):
        if not nombre.lower().endswith((".txt", ".md")):
            continue
        if NOMBRE_CANDIDATO in nombre.upper():
            continue
        ruta = os.path.join(LOOP, nombre)
        if not os.path.isfile(ruta):
            continue
        t = io.open(ruta, encoding="utf-8", errors="replace").read()
        if PAT_DISCREPA.search(t):
            fuera_del_nombre.append((nombre, len(PAT_DISCREPA.findall(t))))
    w("   CIFRA ficheros que dicen DISCREPA y no llevan COTEJO en el nombre: %d"
      % len(fuera_del_nombre))
    for n, c in fuera_del_nombre:
        w("      %-52s %4d apariciones de DISCREPA" % (n, c))
    w("   (van nombrados para que la eleccion del candidato tambien se pueda")
    w("    discutir. NO entran: la regla 1 es la que es y no se ensancha despues")
    w("    de mirar)")
    w("")

    w("D) LA REGLA 2 SOBRE CADA CANDIDATO: QUIEN ENTRA Y QUIEN NO")
    entran = []
    fuera = []
    todas_disc = set()
    todas_coin = set()
    rechazadas_total = 0
    for nombre in candidatos:
        ruta = os.path.join(LOOP, nombre)
        t = io.open(ruta, encoding="utf-8", errors="replace").read()
        disc, coin, rech = puestos_de_un_fichero(t, validos)
        rechazadas_total += len(rech)
        if disc:
            entran.append((nombre, disc, coin, rech))
            todas_disc |= disc
            todas_coin |= coin
            w("   ENTRA %-50s %3d discrepantes | %3d coincidentes | %d lineas rechazadas"
              % (nombre, len(disc), len(coin), len(rech)))
        else:
            motivo = ("no trae ninguna linea legible por la regla 2"
                      if not rech else
                      "trae %d linea(s) con DISCREPA pero ninguna legible" % len(rech))
            fuera.append((nombre, motivo))
    w("")
    w("   LOS QUE QUEDAN FUERA, NOMBRADOS CON SU MOTIVO:")
    for n, m in fuera:
        w("      %-52s %s" % (n, m))
    w("")
    w("   CIFRA candidatos: %d" % len(candidatos))
    w("   CIFRA QUE ENTRAN: %d" % len(entran))
    w("   CIFRA QUE QUEDAN FUERA: %d" % len(fuera))
    w("   CIFRA lineas con DISCREPA rechazadas por no ser un puesto: %d"
      % rechazadas_total)
    for nombre, _d, _c, rech in entran:
        for linea, motivo in rech[:4]:
            w("      rechazada en %s: %s (%s)" % (nombre, linea, motivo))
    w("")

    w("E) LAS TRES CIFRAS QUE EL ENCARGO PIDE, JUNTAS")
    n_tumban = len(todas_disc)
    tumban_con_marca = sorted(todas_disc & con_marca)
    w("   1. CIFRA puestos que han TUMBADO alguna vez a un lector: %d" % n_tumban)
    w("      %s" % ", ".join(str(x) for x in sorted(todas_disc)))
    w("   2. CIFRA de esos que llevan %r: %d" % (MARCA, len(tumban_con_marca)))
    w("      %s" % (", ".join(str(x) for x in tumban_con_marca) or "(ninguno)"))
    w("   3. TASA DE LA MARCA EN EL ARCHIVO ENTERO: %d de %d = %.4f (%.2f por ciento)"
      % (len(con_marca), len(filas), tasa_archivo, 100.0 * tasa_archivo))
    if n_tumban:
        tasa_tumban = len(tumban_con_marca) / float(n_tumban)
        w("   Y LA COMPARACION, QUE ES PARA LO QUE SIRVEN LAS TRES:")
        w("      tasa de la marca entre los que TUMBAN: %.4f (%.2f por ciento)"
          % (tasa_tumban, 100.0 * tasa_tumban))
        w("      tasa de la marca en el ARCHIVO ENTERO: %.4f (%.2f por ciento)"
          % (tasa_archivo, 100.0 * tasa_archivo))
        w("      diferencia en puntos porcentuales: %+.2f"
          % (100.0 * (tasa_tumban - tasa_archivo)))
    w("")

    w("F) EL DENOMINADOR, HASTA DONDE LA REGLA LO DEJA VER")
    w("   CIFRA puestos declarados COINCIDENTES por la misma regla: %d"
      % len(todas_coin))
    leidos = todas_disc | todas_coin
    w("   CIFRA puestos leidos que la regla SI recupera (disc + coin): %d"
      % len(leidos))
    w("   ficheros que entran y NO declaran ningun coincidente (solo listan las")
    w("   discrepancias), o sea donde el denominador NO se recupera:")
    sin_coin = [n for n, d, c, _r in entran if not c]
    for n in sin_coin:
        w("      %s" % n)
    w("   CIFRA de esos: %d de %d" % (len(sin_coin), len(entran)))
    w("")

    w("G) EL TAMANO DE LA MUESTRA, DICHO EN VOZ ALTA ANTES DE CUALQUIER GLOSA")
    w("   %d puestos que tumbaron a un lector, sobre un archivo de %d filas."
      % (n_tumban, len(filas)))
    w("   Eso es el %.2f por ciento del archivo."
      % (100.0 * n_tumban / float(len(filas))))
    if n_tumban < 60:
        w("   NO ALCANZA PARA CONCLUIR, Y ESO ES UN RESULTADO Y SE ESCRIBE COMO")
        w("   TAL. Con %d casos, una diferencia de tasas no distingue una" % n_tumban)
        w("   tendencia de un accidente de muestreo, y esta medicion NO afirma")
        w("   ninguna. Lo que si queda es la CIFRA, el UNIVERSO y la REGLA, para")
        w("   que la proxima vuelta que quiera concluir sepa de donde parte.")
    else:
        w("   La muestra pasa de 60 casos. Aun asi esta salida NO saca ninguna")
        w("   conclusion: eso es del auditor y del fundador, no del instrumento.")
    w("")

    w("H) EL ARCHIVO, REMEDIDO AL SALIR. NO SE ESCRIBIO NI UNA FILA.")
    bd2, bl2, sh2 = sha_de(ARCHIVO)
    w("   disco %d bytes | LF %d bytes | sha256 LF %s" % (bd2, bl2, sh2))
    w("   IDENTICO AL DE LA ENTRADA: %s"
      % ("SI" if (bd, bl, sh) == (bd2, bl2, sh2) else "NO"))
    w("")
    w("FIN")

    texto = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: docs/loop/SALIDA_V191_T5_MARCA_CONTRA_DIFICULTAD.txt (%d bytes)"
          % len(texto.encode("utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
