# -*- coding: utf-8 -*-
r"""vuelta186_rutas_del_reporte.py . TODA RUTA PUBLICADA EN docs/loop/REPORTE.md,
COMPROBADA UNA A UNA, CON SUS DOS CONVENCIONES DE BYTES.

POR QUE EXISTE. `EJECUTOR.md` 1, letra del 5 sep 2026, LA RUTA QUE PROMETE PRUEBA
ES CIFRA: *"una ruta publicada como evidencia de una corrida cuenta como CIFRA
PUBLICADA en su sede, y si apunta a un fichero inexistente o de CERO BYTES es
CAIDA DE CIFRA. Antes de escribir una ruta como prueba, se comprueba que el
fichero existe y que no esta vacio."*

Y PUBLICA LAS DOS CONVENCIONES DE CADA RUTA A PROPOSITO. La `P.2` del fundador
manda bytes exactos y nunca redondeados, y esta casa escribe las dos
convenciones; un fichero cuya salida se redirigio por la consola lleva `CRLF` en
disco, asi que su cifra de LF NO es la misma. **La caida propia `C.1` de esta
vuelta salio justamente de aqui.**

EL HUECO DECLARADO NO ES UNA CAIDA, Y SE SEPARA EN VEZ DE MEZCLARSE. Cuando la
vuelta no es de bateria, la seccion 9 declara el hueco NOMBRANDO el fichero que no
existe. Esa ruta es la unica que puede faltar sin ser rojo, y el acta 185 y el acta
186 lo leen asi. Aqui va contada aparte, con su nombre.

USO:
  python scripts/loop/vuelta186_rutas_del_reporte.py
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
REPORTE = os.path.join(LOOP, "REPORTE.md")
PATRON_RUTA = re.compile(
    r"`((?:docs|scripts|dataset|engine|web|paradas)/[A-Za-z0-9_./-]+)`")


def rutas_del_texto(texto):
    """LAS RUTAS DISTINTAS QUE UN TEXTO PUBLICA ENTRE COMILLAS INVERSAS. PURA."""
    return sorted(set(PATRON_RUTA.findall(texto.replace(chr(13) + NL, NL))))


def dos_convenciones(datos):
    """LAS DOS CIFRAS DE BYTES DE UN CONTENIDO: la de DISCO y la normalizada a
    LF. PURA: recibe los bytes crudos y no lee ni escribe nada.

    SE SEPARO A UNA FUNCION EN LA VUELTA 187, TAREA 4, Y SE DICE POR QUE. Esta
    medicion vivia dentro del bucle de `main()` de este mismo fichero, asi que la
    guarda nueva de `cerrar_reporte.py` no la podia llamar y habria tenido que
    escribir una TERCERA copia de dos lineas que ya existian. **Una sede, dos
    llamadores, y NO un tercero.** La conducta de `main()` no cambia: llama aqui
    y saca exactamente las mismas dos cifras que sacaba antes."""
    return len(datos), len(datos.replace(chr(13).encode() + chr(10).encode(), chr(10).encode()))


def medir_en_disco(raiz, ruta):
    """LAS DOS CONVENCIONES DE UNA RUTA RELATIVA, LEIDAS DEL DISCO, o `None` si
    el fichero no existe. **ES EL UNICO SITIO QUE TOCA DISCO PARA ESTO**, y por
    eso la guarda de `cerrar_reporte.py` puede ser PURA: recibe un mapa que este
    lector le llena.

    Devuelve `(bytes_disco, bytes_lf)` o `None`. **Un fichero que no existe
    devuelve `None` y NO cero**: cero seria una cifra, y la ausencia no lo es."""
    p = os.path.join(raiz, ruta.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    return dos_convenciones(io.open(p, "rb").read())


def hueco_declarado(texto):
    """LA RUTA DEL FICHERO DE BATERIA QUE LA SECCION 9 DECLARA COMO HUECO, o None.
    PURA: se lee de la propia seccion 9 y no se teclea."""
    if (NL + "## 9.") not in texto:
        return None
    seccion9 = texto[texto.index(NL + "## 9."):]
    if "HUECO DECLARADO Y MEDIDO" not in seccion9:
        return None
    m = re.search(r"\*\*EL NOMBRE DEL FICHERO:\*\*\s*`([^`]+)`", seccion9)
    return m.group(1) if m else None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    texto = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    rutas = rutas_del_texto(texto)
    hueco = hueco_declarado(texto)
    L = ["TODA RUTA PUBLICADA EN docs/loop/REPORTE.md, COMPROBADA UNA A UNA",
         "(vuelta 186; EJECUTOR.md 1, LA RUTA QUE PROMETE PRUEBA ES CIFRA)", "",
         "CIFRA rutas distintas halladas en el reporte: %d" % len(rutas),
         "RUTA DEL HUECO DECLARADO, leida de la seccion 9 y no tecleada: %s"
         % (hueco or "(ninguna: esta vuelta no declara hueco)"), ""]
    malas = 0
    for r in rutas:
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        if not os.path.exists(p):
            if hueco and r == hueco:
                L.append("   HUECO      %-62s NO EXISTE, y NO ES CAIDA: es el "
                         "hueco que la seccion 9 declara" % r)
            else:
                L.append("   NO EXISTE  %-62s" % r)
                malas += 1
            continue
        bd, bl = dos_convenciones(io.open(p, "rb").read())
        if bd == 0:
            malas += 1
            L.append("   CERO BYTES %-62s" % r)
            continue
        L.append("   OK         %-62s disco %8d bytes | LF %8d bytes%s"
                 % (r, bd, bl,
                    "" if bd == bl else "   <-- DISCO distinto de LF"))
    distintas = len([1 for r in rutas
                     if os.path.exists(os.path.join(RAIZ, r.replace("/", os.sep)))
                     and io.open(os.path.join(RAIZ, r.replace("/", os.sep)),
                                 "rb").read()
                     != io.open(os.path.join(RAIZ, r.replace("/", os.sep)),
                                "rb").read().replace(b"\r\n", b"\n")])
    L += ["",
          "CIFRA rutas en que la cifra de disco NO es la de LF: %d" % distintas,
          "CIFRA rutas que NO existen o miden cero bytes, SIN CONTAR el hueco "
          "declarado: %d" % malas,
          "VEREDICTO: %s" % ("VERDE" if malas == 0 else "ROJO")]
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V186_RUTAS_DEL_REPORTE.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if malas == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
