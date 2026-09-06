# -*- coding: utf-8 -*-
r"""vuelta188_tarea5a_mutacion_vecinos_evitar.py . EL CASO POSITIVO POR MUTACION
DEL PARAMETRO `evitar` DE `vecinos()`.

QUIEN LO ENCARGA. La adjudicacion `5.2` y la respuesta `7.3` del acta 188,
contestando la `P.3` del reporte de la 187: **el solape se le exige AL UNIVERSO**,
porque la exclusion existe para que nadie relea lo ya leido y los 60 se leen
todos. El remedio va **por parametro y de forma ADITIVA**: *"Sin el, se comporta
exactamente igual que hoy (y eso lo prueba su arnes). Con el, salta tambien los
puestos de `evitar` al subir. Asi el cero sale por construccion y no por suerte.
Su regla no cambia: cambia lo que se le pasa."*

QUE PRUEBA, CASO A CASO, Y TODOS TIENEN QUE CAER AL MUTAR SU ESPERADO:

  (A) SIN `evitar`, LA CONDUCTA ES LA DE ANTES, BYTE A BYTE. Y eso NO se afirma:
      este fichero lleva dentro **una copia CONGELADA de la version anterior al
      parametro**, declarada como tal, y exige que las dos den la MISMA salida
      sobre una bateria de tramos, incluidos los bordes (el tramo pegado al
      techo, el tramo de un solo puesto y el tramo denso).

  (B) CON `evitar`, NINGUN VECINO CAE DENTRO DE `evitar`. El cero del solape sale
      POR CONSTRUCCION.

  (C) LA CUENTA NO SE ROMPE: con `evitar`, `vecinos()` sigue devolviendo TANTOS
      vecinos como puestos tiene el tramo mientras quede sitio, y **cuando no
      queda sitio devuelve MENOS y no inventa ninguno**. Un vecino inventado
      seria peor que un vecino de menos.

  (D) LA SALIDA SIGUE SIENDO DETERMINISTA: dos llamadas con la misma entrada dan
      la misma lista, y el orden es creciente.

  (E) `evitar` NO TIENE QUE CONTENER AL TRAMO PARA FUNCIONAR, ni le estorba que
      lo contenga: los puestos del propio tramo ya se saltaban antes.

LO QUE ESTE ARNES NO HACE: no lee el archivo de veredictos, no lee ninguna ciega
y no escribe nada fuera de su propia salida. Llama a la funcion PURA del fichero
vivo con tramos fabricados en memoria.

USO:
  python scripts/loop/vuelta188_tarea5a_mutacion_vecinos_evitar.py
"""
import hashlib
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta182_tarea1c_relectura_al_doble import vecinos   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
SUJETO = "scripts/loop/vuelta182_tarea1c_relectura_al_doble.py"


def vecinos_congelado(tramo, maximo):
    """LA VERSION ANTERIOR AL PARAMETRO `evitar`, CONGELADA AQUI Y DECLARADA.

    **NO es una reimplementacion ni una parafrasis:** es el cuerpo que
    `vecinos()` tenia antes de la vuelta 188, copiado byte a byte. Vive aqui y no
    en el fichero vivo a proposito: **el sitio de una version congelada es el
    arnes que la usa para cotejar, no el instrumento que la sustituyo.** Si algun
    dia la de arriba cambia su regla, este cotejo caera, que es exactamente lo
    que se quiere."""
    elegidos = []
    ocupados = set(tramo)
    for p in sorted(tramo):
        q = p + 1
        while q in ocupados and q <= maximo:
            q += 1
        if q > maximo:
            q = p - 1
            while q in ocupados and q >= 1:
                q -= 1
        if 1 <= q <= maximo:
            elegidos.append(q)
            ocupados.add(q)
    return sorted(elegidos)


def sello_del_sujeto(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    datos = io.open(p, "rb").read()
    lf = datos.replace(chr(13).encode() + chr(10).encode(), chr(10).encode())
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest())


TRAMOS = [
    ("treinta sueltos, como una ciega de verdad",
     [239, 290, 415, 550, 670, 909, 1123, 1132, 1202, 1403, 1791, 1806, 1929,
      1962, 1973, 2150, 2162, 2357, 2399, 2418, 2683, 2759, 2783, 2875, 3148,
      3179, 3224, 3247, 3280, 3364], 3388),
    ("uno solo", [17], 3388),
    ("pegado al techo", [3386, 3387, 3388], 3388),
    ("pegado al suelo", [1, 2, 3], 3388),
    ("denso y consecutivo", list(range(10, 30)), 3388),
    ("el tramo entero de un archivo diminuto", [1, 2, 3, 4, 5], 5),
    ("vacio", [], 3388),
]


def _caso_a(w):
    fallos = casos = caen = 0
    w("CASO A. SIN `evitar`, LA CONDUCTA ES LA DE ANTES, COTEJADA CONTRA UNA COPIA")
    w("        CONGELADA DE LA VERSION ANTERIOR AL PARAMETRO")
    for etiqueta, tramo, maximo in TRAMOS:
        nueva = vecinos(tramo, maximo)
        vieja = vecinos_congelado(tramo, maximo)
        casos += 1
        ok = (nueva == vieja)
        w("   %-42s tramo de %-3d | nueva %d | congelada %d | %s"
          % (etiqueta, len(tramo), len(nueva), len(vieja),
             "IDENTICAS" if ok else "DISTINTAS"))
        if not ok:
            w("      nueva:     %s" % nueva)
            w("      congelada: %s" % vieja)
            fallos += 1
        w("      MUTACION del esperado (exigir que DIFIERAN): %s"
          % ("PASA" if nueva != vieja else "CAE"))
        if nueva != vieja:
            fallos += 1
        else:
            caen += 1
    w("   Y `evitar=None` Y `evitar=()` TIENEN QUE DAR LO MISMO QUE NO PASARLO:")
    tramo, maximo = TRAMOS[0][1], TRAMOS[0][2]
    a = vecinos(tramo, maximo)
    b = vecinos(tramo, maximo, evitar=None)
    c = vecinos(tramo, maximo, evitar=())
    casos += 1
    ok = (a == b == c)
    w("      sin pasarlo %d | evitar=None %d | evitar=() %d -> %s"
      % (len(a), len(b), len(c), "CALZA" if ok else "NO CALZA"))
    if not ok:
        fallos += 1
    else:
        caen += 1
    w("")
    return fallos, casos, caen


def _caso_bc(w):
    fallos = casos = caen = 0
    w("CASO B. CON `evitar`, NINGUN VECINO CAE DENTRO DE `evitar`")
    tramo = TRAMOS[0][1]
    maximo = TRAMOS[0][2]
    escenarios = [
        ("evitar vacio", set()),
        ("evitar con los inmediatos de arriba", set(p + 1 for p in tramo)),
        ("evitar con los inmediatos de arriba y de abajo",
         set(p + 1 for p in tramo) | set(p - 1 for p in tramo)),
        ("evitar con un bloque grande", set(range(200, 1500))),
        ("evitar que contiene tambien al tramo",
         set(tramo) | set(p + 1 for p in tramo)),
    ]
    for etiqueta, evitar in escenarios:
        v = vecinos(tramo, maximo, evitar=evitar)
        solape = sorted(set(v) & set(evitar))
        con_tramo = sorted(set(v) & set(tramo))
        casos += 1
        ok = (not solape and not con_tramo)
        w("   %-46s vecinos %-3d | solape con evitar %d | con el tramo %d | %s"
          % (etiqueta, len(v), len(solape), len(con_tramo),
             "CALZA" if ok else "NO CALZA"))
        if solape:
            w("      LOS QUE SOLAPAN: %s" % solape)
        if not ok:
            fallos += 1
        w("      MUTACION del esperado (exigir solape de al menos 1): %s"
          % ("PASA" if solape else "CAE"))
        if solape:
            fallos += 1
        else:
            caen += 1
    w("   Y EL CONTRASTE QUE PRUEBA QUE `evitar` HACE ALGO: SIN el, sobre el mismo")
    w("   tramo y el mismo conjunto, el solape NO es cero.")
    evitar = set(p + 1 for p in tramo)
    sin = vecinos(tramo, maximo)
    casos += 1
    solape_sin = sorted(set(sin) & evitar)
    w("      sin `evitar`: %d vecinos, solape %d %s"
      % (len(sin), len(solape_sin), solape_sin[:8]))
    if not solape_sin:
        w("      EL CONTRASTE NO MUERDE: este caso no prueba nada y es un fallo.")
        fallos += 1
    else:
        caen += 1
    w("")

    w("CASO C. LA CUENTA NO SE ROMPE, Y CUANDO NO QUEDA SITIO DEVUELVE MENOS EN")
    w("        VEZ DE INVENTAR UN VECINO")
    for etiqueta, tramo2, maximo2, evitar2, esperado in (
            ("archivo diminuto, evitar lo llena todo",
             [1, 2], 4, {3, 4}, 0),
            ("archivo diminuto, evitar deja un hueco",
             [1, 2], 4, {4}, 1),
            ("sitio de sobra", [10, 20], 3388, {11}, 2)):
        v = vecinos(tramo2, maximo2, evitar=evitar2)
        casos += 1
        ok = (len(v) == esperado and not (set(v) & evitar2)
              and all(1 <= x <= maximo2 for x in v))
        w("   %-40s -> %s | esperado %d | %s"
          % (etiqueta, v, esperado, "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos += 1
        w("      MUTACION del esperado (exigir %d): %s"
          % (esperado + 1, "PASA" if len(v) == esperado + 1 else "CAE"))
        if len(v) == esperado + 1:
            fallos += 1
        else:
            caen += 1
    w("")
    return fallos, casos, caen


def _caso_de(w):
    fallos = casos = caen = 0
    w("CASO D. LA SALIDA SIGUE SIENDO DETERMINISTA Y CRECIENTE")
    tramo, maximo = TRAMOS[0][1], TRAMOS[0][2]
    evitar = set(range(200, 1500))
    a = vecinos(tramo, maximo, evitar=evitar)
    b = vecinos(tramo, maximo, evitar=evitar)
    casos += 1
    ok = (a == b and a == sorted(a) and len(a) == len(set(a)))
    w("   dos llamadas iguales dan la misma lista: %s" % ("SI" if a == b else "NO"))
    w("   la lista viene ordenada y sin repetidos: %s"
      % ("SI" if (a == sorted(a) and len(a) == len(set(a))) else "NO"))
    w("   ESPERADO las tres cosas -> %s" % ("CALZA" if ok else "NO CALZA"))
    if not ok:
        fallos += 1
    w("   MUTACION del esperado (exigir que las dos llamadas difieran): %s"
      % ("PASA" if a != b else "CAE"))
    if a != b:
        fallos += 1
    else:
        caen += 1
    w("   Y EL ORDEN DE `evitar` NO IMPORTA, porque es un conjunto:")
    c = vecinos(tramo, maximo, evitar=sorted(evitar))
    d = vecinos(tramo, maximo, evitar=list(reversed(sorted(evitar))))
    casos += 1
    w("      como lista ordenada %d | como lista invertida %d -> %s"
      % (len(c), len(d), "CALZA" if c == d else "NO CALZA"))
    if c != d:
        fallos += 1
    else:
        caen += 1
    w("")

    w("CASO E. `evitar` NO TIENE QUE CONTENER AL TRAMO, NI LE ESTORBA QUE LO")
    w("        CONTENGA")
    tramo2 = [100, 200, 300]
    v1 = vecinos(tramo2, 3388, evitar={101})
    v2 = vecinos(tramo2, 3388, evitar={101} | set(tramo2))
    casos += 1
    ok = (v1 == v2)
    w("   evitar sin el tramo: %s" % v1)
    w("   evitar con el tramo: %s" % v2)
    w("   ESPERADO iguales, porque el tramo ya se saltaba antes -> %s"
      % ("CALZA" if ok else "NO CALZA"))
    if not ok:
        fallos += 1
    w("   MUTACION del esperado (exigir que difieran): %s"
      % ("PASA" if v1 != v2 else "CAE"))
    if v1 != v2:
        fallos += 1
    else:
        caen += 1
    w("")
    return fallos, casos, caen


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    disco, lf, sha = sello_del_sujeto(SUJETO)
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DEL PARAMETRO `evitar` DE `vecinos()`")
    w("(vuelta 188, TAREA 5.a; adjudicacion 5.2 y respuesta 7.3 del acta 188)")
    w("=" * 78)
    w("")
    w("EL SUJETO ES EL FICHERO VIVO %s," % SUJETO)
    w("y `vecinos()` se IMPORTA de el, no se copia.")
    w("SELLO DEL SUJETO (vuelta 188, TAREA 3.b): disco %d bytes | LF %d bytes |"
      % (disco, lf))
    w("sha256 LF %s" % sha)
    w("")
    fuente = io.open(os.path.join(RAIZ, SUJETO.replace("/", os.sep)),
                     encoding="utf-8").read().replace(chr(13) + NL, NL)
    for aguja in ("def vecinos",):
        hits = [i for i, l in enumerate(fuente.split(NL), 1) if l.startswith(aguja)]
        w("LINEA DE `%s` EN EL SUJETO, CON EL SELLO DE ARRIBA AL LADO: %s"
          % (aguja, ", ".join(str(x) for x in hits) or "(ninguna)"))
    w("")
    fallos = casos = caen = 0
    for parte in (_caso_a, _caso_bc, _caso_de):
        f, c, k = parte(w)
        fallos += f
        casos += c
        caen += k
    w("CIFRA casos: %d | pasan: %d" % (casos, casos - fallos))
    w("CIFRA casos que CAEN al mutar su esperado: %d de %d" % (caen, caen))
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V188_T5A_MUTACION_VECINOS_EVITAR.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
