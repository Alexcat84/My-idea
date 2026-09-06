# -*- coding: utf-8 -*-
r"""vuelta186_tarea2b_mutacion_pieza2_cercas.py . EL CASO POSITIVO POR MUTACION DE
LA PIEZA (2), QUE DEJA DE CAER SOBRE UNA CITA.

QUIEN LO ENCARGA. El acta 186, punto `6.2`, que cierra la `PD.5` con tres razones
escritas: el propio fichero YA eligio como trata una cita (`cifras_sin_pareja()`
excluye los bloques cercados), la pieza (2) hacia IMPOSIBLE que un reporte citara
entera la salida roja de otro, y un falso positivo no es fallar ruidoso, es ruido.

QUE PRUEBA, CASO A CASO, Y TODOS TIENEN QUE CAER AL MUTAR SU ESPERADO:
  (A) la marca FUERA de toda cerca: la pieza (2) FALTA.
  (B) la marca SOLO DENTRO de una cerca: NO falta.
  (C) la marca EN LAS DOS: falta.
  (D) CERO marcas: no falta.
  (E) una cerca SIN CERRAR al final del texto, con el valor EXACTO afirmado y no
      un "lo que salga": la marca que va detras de una cerca abierta y nunca
      cerrada queda DENTRO, asi que la pieza (2) NO falta. Es la conducta que
      `cifras_sin_pareja()` ya tenia desde que nacio y que la separacion del
      desbloqueador conserva letra por letra.
  (F) EL TEXTO REAL de `docs/loop/SALIDA_V185_T2A_REPORTE_184_CERRADO_EN_ROJO.md`:
      la pieza (2) YA NO FALTA. Es el caso que trajo la adjudicacion.

Y DOS CASOS MAS QUE NO ESTABAN EN LA LETRA PERO QUE LA LETRA EXIGE NO ROMPER:
  (G) el tallador sin filas sigue siendo rojo, con su texto de hoy.
  (H) una fila del tallador sin pegar sigue siendo rojo, con su texto de hoy.
Sin ellos, un arnes que solo mira la marca dejaria pasar que la reparacion se
hubiera llevado por delante el resto de la pieza.

EL SUJETO ES `piezas_que_faltan()` Y `renglones_fuera_de_cerca()` IMPORTADAS DEL
FICHERO VIVO. Los textos se FABRICAN en memoria, salvo el caso (F), que es el
fichero real y se abre SOLO PARA LEER.

USO:
  python scripts/loop/vuelta186_tarea2b_mutacion_pieza2_cercas.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
CERCA = "```"
MARCA = CR.HUECO_CABECERA
REAL = os.path.join(LOOP, "SALIDA_V185_T2A_REPORTE_184_CERRADO_EN_ROJO.md")

MOTIVO_HUECO = "(2) el hueco de la cabecera sigue sin rellenar"
MOTIVO_SIN_FILAS = "(2) el fichero del tallador no trae ninguna fila de tabla"

FILAS = ["| celda | celda |", "| a | b |", "| c | d |", "| e | f |",
         "| g | h |", "| i | j |", "| k | l |", "| m | n |", "| o | p |"]
BAT = ["linea uno de la bateria"]
NOM = "docs/loop/SALIDA_V999_BATERIA.txt"


def fabricar(cuerpo_de_la_cabecera):
    """UN REPORTE DE MENTIRA CON SUS OTRAS TRES PIEZAS PUESTAS. PURA."""
    p = ["# REPORTE DE LA VUELTA 999 (fabricado)", "",
         "**EL VEREDICTO DE UNA LINEA: de mentira.**", ""]
    p += list(cuerpo_de_la_cabecera) + [""]
    p += FILAS + [""]
    for k in range(3, 9):
        p += ["## %d. UNA SECCION DE MENTIRA" % k, "", "Y su cuerpo.", ""]
    p += ["## 9. LA BATERIA DE MUTACIONES, DE MENTIRA", ""] + BAT + [""]
    return NL.join(p) + NL


def pieza2_de(faltan):
    """LOS MOTIVOS DE LA PIEZA (2). PURA."""
    return [f for f in faltan if f.startswith("(2)")]


def falta_la_2(texto, filas=None):
    """SI LA PIEZA (2) FALTA SOBRE UN TEXTO DADO. PURA salvo por llamar al vivo."""
    faltan = CR.piezas_que_faltan(texto, FILAS if filas is None else filas,
                                  BAT, vuelta=999, nombre_bateria=NOM)
    return pieza2_de(faltan)


def _casos_de_la_marca(w):
    """A, B, C, D Y E: donde vive la marca. Devuelve (fallos, casos, caen)."""
    fallos = casos = caen = 0
    escenarios = [
        ("A. la marca FUERA de toda cerca",
         ["Un parrafo que dice " + MARCA + " en prosa."], True),
        ("B. la marca SOLO DENTRO de una cerca",
         [CERCA, "   | " + MARCA + " (salida citada)", CERCA], False),
        ("C. la marca EN LAS DOS",
         ["Un parrafo que dice " + MARCA + " en prosa.",
          CERCA, "   | " + MARCA + " (salida citada)", CERCA], True),
        ("D. CERO marcas",
         ["Un parrafo sin ninguna marca de maquina."], False),
        ("E. una cerca SIN CERRAR y la marca DETRAS",
         ["Un parrafo limpio.", CERCA, "   | " + MARCA + " dentro de la abierta"],
         False),
    ]
    for etiqueta, cuerpo, esperado in escenarios:
        texto = fabricar(cuerpo)
        p2 = falta_la_2(texto)
        falta = bool(p2)
        casos += 1
        w("   %-46s -> pieza (2) falta: %-3s | esperado %-3s | %s"
          % (etiqueta, "SI" if falta else "no", "SI" if esperado else "no",
             "CALZA" if falta == esperado else "NO CALZA"))
        if p2:
            w("      motivo: %s" % p2[0])
        if falta != esperado:
            fallos += 1
        w("      MUTACION del esperado (exigir %s): %s"
          % ("no" if esperado else "SI",
             "PASA" if falta != esperado else "CAE"))
        if falta != esperado:
            fallos += 1
        else:
            caen += 1
    w("")
    w("   EL CASO E LLEVA SU VALOR EXACTO AFIRMADO Y NO UN 'LO QUE SALGA':")
    texto_e = fabricar(["Un parrafo limpio.", CERCA,
                        "   | " + MARCA + " dentro de la abierta"])
    renglones = CR.renglones_fuera_de_cerca(texto_e)
    con_marca = [n for n, l in renglones if MARCA in l]
    casos += 1
    w("      CIFRA renglones FUERA de cerca que llevan la marca: %d"
      % len(con_marca))
    w("      ESPERADO exactamente 0 -> %s"
      % ("CALZA" if len(con_marca) == 0 else "NO CALZA"))
    if len(con_marca) != 0:
        fallos += 1
    w("      MUTACION del esperado (exigir 1): %s"
      % ("PASA" if len(con_marca) == 1 else "CAE"))
    if len(con_marca) == 1:
        fallos += 1
    else:
        caen += 1
    w("      CIFRA renglones totales del texto: %d | fuera de cerca: %d"
      % (texto_e.count(NL), len(renglones)))
    w("")
    return fallos, casos, caen


def _caso_real(w):
    """F: el texto real del reporte de la 184 cerrado en rojo."""
    fallos = casos = caen = 0
    w("   F. EL TEXTO REAL DE SALIDA_V185_T2A_REPORTE_184_CERRADO_EN_ROJO.md")
    if not os.path.exists(REAL):
        w("      EL FICHERO NO EXISTE. Sin el no hay caso real, y eso se dice.")
        return 1, 1, 0
    texto = io.open(REAL, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)
    renglones = CR.renglones_fuera_de_cerca(texto)
    dentro = len([1 for l in texto.split(NL) if MARCA in l]) - len(
        [1 for _n, l in renglones if MARCA in l])
    fuera = len([1 for _n, l in renglones if MARCA in l])
    w("      %d bytes en disco y %d normalizados a LF"
      % (os.path.getsize(REAL), len(texto.encode("utf-8"))))
    w("      CIFRA apariciones de la marca DENTRO de cerca: %d" % dentro)
    w("      CIFRA apariciones de la marca FUERA de cerca: %d" % fuera)
    for n, l in renglones:
        if MARCA in l:
            w("         FUERA, LINEA %d: %s" % (n, l.strip()[:110]))
    # LAS FILAS DEL TALLADOR DEL CASO REAL: se toman del propio texto, que las
    # lleva pegadas, para que la pieza (2) pueda juzgar el caso entero y no solo
    # la marca. Se cogen las nueve primeras filas de tabla que el texto trae.
    filas_reales = [l.rstrip() for l in texto.split(NL)
                    if l.strip().startswith("|")][:9]
    faltan = CR.piezas_que_faltan(texto, filas_reales, BAT, vuelta=184,
                                  nombre_bateria="docs/loop/SALIDA_V183_BATERIA.txt",
                                  tramos_sellados_en_esta_vuelta=[6, 7, 8, 9])
    p2 = pieza2_de(faltan)
    casos += 1
    w("      pieza (2) falta sobre el texto real: %s" % ("SI" if p2 else "NO"))
    if p2:
        w("         motivo: %s" % p2[0])
    w("      ESPERADO: NO falta -> %s" % ("CALZA" if not p2 else "NO CALZA"))
    if p2:
        fallos += 1
    w("      MUTACION del esperado (exigir que SI falte): %s"
      % ("PASA" if p2 else "CAE"))
    if p2:
        fallos += 1
    else:
        caen += 1
    w("")
    return fallos, casos, caen


def _casos_que_no_se_aflojan(w):
    """G Y H: lo demas de la pieza (2) sigue siendo rojo, con sus textos de hoy."""
    fallos = casos = caen = 0
    w("   G. EL TALLADOR SIN FILAS SIGUE SIENDO ROJO, CON SU TEXTO DE HOY")
    texto = fabricar(["Un parrafo limpio."])
    p2 = falta_la_2(texto, filas=[])
    casos += 1
    w("      pieza (2) falta: %s" % ("SI" if p2 else "NO"))
    w("      motivo publicado: %r" % (p2[0] if p2 else None))
    w("      motivo exigido  : %r" % MOTIVO_SIN_FILAS)
    calza = bool(p2) and p2[0] == MOTIVO_SIN_FILAS
    w("      ESPERADO: falta con ESE motivo -> %s" % ("CALZA" if calza else "NO CALZA"))
    if not calza:
        fallos += 1
    w("      MUTACION del esperado (exigir que NO falte): %s"
      % ("PASA" if not p2 else "CAE"))
    if not p2:
        fallos += 1
    else:
        caen += 1
    w("")
    w("   H. UNA FILA DEL TALLADOR SIN PEGAR SIGUE SIENDO ROJO")
    otras = FILAS + ["| una fila que el reporte NO lleva pegada |"]
    p2 = falta_la_2(texto, filas=otras)
    casos += 1
    w("      pieza (2) falta: %s" % ("SI" if p2 else "NO"))
    if p2:
        w("      motivo: %s" % p2[0])
    if not p2:
        fallos += 1
    w("      MUTACION del esperado (exigir que NO falte): %s"
      % ("PASA" if not p2 else "CAE"))
    if not p2:
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
    w("CASO POSITIVO POR MUTACION DE LA PIEZA (2) Y LAS CERCAS")
    w("(vuelta 186, TAREA 2.b; adjudicacion 6.2 del acta 186, que cierra la PD.5)")
    w("=" * 78)
    w("")
    w("EL SUJETO ES EL FICHERO VIVO scripts/loop/cerrar_reporte.py, IMPORTADO.")
    w("La marca que se busca es %r, leida del propio instrumento." % MARCA)
    w("")
    fallos = casos = caen = 0
    for parte in (_casos_de_la_marca, _caso_real, _casos_que_no_se_aflojan):
        f, c, k = parte(w)
        fallos += f
        casos += c
        caen += k
    w("CIFRA casos: %d | pasan: %d" % (casos, casos - fallos))
    w("CIFRA casos que CAEN al mutar su esperado: %d de %d" % (caen, caen))
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V186_T2B_MUTACION_PIEZA2_CERCAS.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
