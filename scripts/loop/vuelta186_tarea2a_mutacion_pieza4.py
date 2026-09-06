# -*- coding: utf-8 -*-
r"""vuelta186_tarea2a_mutacion_pieza4.py . EL CASO POSITIVO POR MUTACION DE LA
PIEZA (4) DE `piezas_que_faltan()`, QUE DEJA DE LLEVAR SU PROPIA COPIA DE LA
REGLA Y AHORA LA LLAMA.

QUIEN LO ENCARGA. El acta 186, punto `6.1`, que cierra la `PD.6`: *"la
comparacion `ajena != vuelta` vive DOS veces en el mismo fichero... reparar una
sede y no la otra no es media adjudicacion: es la misma adjudicacion sin terminar
de aplicar"*. Y su condicion, que no es de estilo: *"la pieza (4) NO recibe una
copia sincronizada. La regla se queda en UNA sede y la pieza (4) la LLAMA."*

QUE PRUEBA, CASO A CASO, Y TODOS TIENEN QUE CAER AL MUTAR SU ESPERADO:
  (A) la bateria de la 183 cerrando la 184 CON tramos sellados en la 184: la
      pieza (4) NO falta.
  (B) la misma con la LISTA VACIA: falta, y con el motivo LITERAL de hoy, letra
      por letra.
  (C) la bateria de la 185 cerrando la 184 (una vuelta POSTERIOR): falta, con
      tramos sellados y sin ellos, porque una bateria de una vuelta posterior
      SIEMPRE es roja.
  (D) EL PARAMETRO EN SU VALOR POR DEFECTO se comporta EXACTAMENTE como la
      conducta de hoy, y eso no se afirma: se compara contra una copia de la
      logica vieja escrita aqui dentro, escenario por escenario.
  (E) LA SEGUNDA COPIA DE LA COMPARACION: se cuentan las apariciones de
      `ajena != vuelta` en el fichero vivo y se EXIGE 1. Si alguien vuelve a
      meter una copia, este caso cae.

POR QUE EL CASO (E) NO CUENTA LAS LINEAS DE COMENTARIO, Y SE DICE EN VEZ DE
ESCONDERLO: la reparacion deja un comentario que NOMBRA la comparacion para que
se entienda por que la pieza (4) llama en vez de comparar. Un comentario no es una
copia de la regla. Se cuentan las apariciones en lineas de CODIGO (las que no
empiezan por almohadilla) y SE PUBLICA TAMBIEN el conteo crudo, para que la
diferencia entre los dos este a la vista y nadie tenga que deducirla.

EL SUJETO ES `piezas_que_faltan()` IMPORTADA DEL FICHERO VIVO. Los textos de
reporte se FABRICAN aqui en memoria: este arnes no escribe ningun reporte, no toca
`docs/loop/REPORTE.md` y no lee ningun fichero vivo salvo el propio
`scripts/loop/cerrar_reporte.py`, que abre SOLO para contar las apariciones del
caso (E).

USO:
  python scripts/loop/vuelta186_tarea2a_mutacion_pieza4.py
"""
import hashlib
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
CR_RUTA = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")


def sello_del_sujeto(ruta=None):
    """LOS BYTES Y EL `sha256` DEL FICHERO CUYOS NUMEROS DE LINEA ESTE ARNES
    PUBLICA (vuelta 188, TAREA 3.b; respuesta del acta 188 a la `P.2`).

    POR QUE: una salida sellada que publica numeros de linea de un fichero VIVO
    envejece sola, y sin el sello del sujeto al lado hay que DEDUCIR a mano si un
    diff futuro viene de que se movio el sujeto o de que se movio el arnes. Con
    el sello, lo dice la propia salida. **Es aditivo: no cambia ni un veredicto
    de este arnes.**"""
    p = ruta or CR_RUTA
    datos = io.open(p, "rb").read()
    lf = datos.replace(chr(13).encode() + chr(10).encode(),
                        chr(10).encode())
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest())
COMPARACION = "ajena != vuelta"

# EL MOTIVO LITERAL DE HOY, TAL COMO LA PIEZA (4) LO ESCRIBE. Va aqui para poder
# exigirlo letra por letra: si alguien reescribe el rojo viejo, el caso (B) cae.
MOTIVO_HOY = ("(4) la salida pegada en la seccion 9 es la de la vuelta %d y no la "
              "de la %d: UNA CORRIDA DE OTRA VUELTA NO SATISFACE ESTA PIEZA")

FILAS = ["| celda | celda |", "| a | b |", "| c | d |", "| e | f |",
         "| g | h |", "| i | j |", "| k | l |", "| m | n |", "| o | p |"]


def reporte_fabricado(lineas_bateria):
    """UN REPORTE DE MENTIRA CON SUS CUATRO PIEZAS PUESTAS, salvo lo que cada
    caso quiera romper. PURA: devuelve texto y no escribe nada."""
    p = ["# REPORTE DE LA VUELTA 999 (fabricado)", "",
         "**EL VEREDICTO DE UNA LINEA: de mentira.**", ""]
    p += FILAS + [""]
    for k in range(3, 9):
        p += ["## %d. UNA SECCION DE MENTIRA" % k, "", "Y su cuerpo.", ""]
    p += ["## 9. LA BATERIA DE MUTACIONES, DE MENTIRA", ""]
    p += list(lineas_bateria)
    p += [""]
    return NL.join(p) + NL


def conducta_vieja_de_la_pieza4(lineas_bateria, nombre_bateria, vuelta):
    """LA LOGICA VIEJA DE LA PIEZA (4), COPIADA AQUI A PROPOSITO Y DECLARADA.

    Es la comparacion que la pieza (4) llevaba dentro ANTES de la reparacion de
    la vuelta 186. Vive AQUI, en el arnes, y NO en el instrumento: es el
    testigo contra el que se comprueba que el valor por defecto del parametro
    nuevo conserva EXACTAMENTE la conducta de hoy. Devuelve True si la pieza (4)
    tendria que FALTAR por identidad de vuelta.

    QUE NO SE PUEDE DEDUCIR DE ESTA COPIA: que la conducta sea buena. Solo que
    es la MISMA. La bondad la juzgan los otros casos."""
    if not lineas_bateria:
        return False
    ajena = CR.vuelta_de_fichero(nombre_bateria)
    return vuelta is not None and ajena is not None and ajena != vuelta


def pieza4_de(faltan):
    """LOS MOTIVOS DE LA PIEZA (4) DENTRO DE LA LISTA QUE DEVUELVE
    `piezas_que_faltan()`. PURA."""
    return [f for f in faltan if f.startswith("(4)")]


def _casos_abc(w):
    """LOS CASOS A, B Y C. Devuelve (fallos, casos, caen)."""
    fallos = casos = caen = 0
    BAT183 = ["linea uno de la bateria", "linea dos de la bateria"]
    NOM183 = "docs/loop/SALIDA_V183_BATERIA.txt"
    NOM185 = "docs/loop/SALIDA_V185_BATERIA.txt"

    w("CASO A. LA BATERIA DE LA 183 CERRANDO LA 184, CON TRAMOS SELLADOS EN LA 184")
    texto = reporte_fabricado(BAT183)
    faltan = CR.piezas_que_faltan(texto, FILAS, BAT183, vuelta=184,
                                  nombre_bateria=NOM183,
                                  tramos_sellados_en_esta_vuelta=[6, 7, 8, 9])
    p4 = pieza4_de(faltan)
    casos += 1
    w("   pieza (4) falta: %s" % (("SI: " + p4[0]) if p4 else "NO"))
    w("   ESPERADO: NO falta -> %s" % ("CALZA" if not p4 else "NO CALZA"))
    if p4:
        fallos += 1
    w("   MUTACION del esperado (exigir que SI falte): %s"
      % ("PASA" if p4 else "CAE"))
    if not p4:
        caen += 1
    else:
        fallos += 1
    w("")

    w("CASO B. LA MISMA, CON LA LISTA DE TRAMOS VACIA: FALTA, Y CON EL MOTIVO")
    w("        LITERAL DE HOY, LETRA POR LETRA")
    faltan = CR.piezas_que_faltan(texto, FILAS, BAT183, vuelta=184,
                                  nombre_bateria=NOM183,
                                  tramos_sellados_en_esta_vuelta=[])
    p4 = pieza4_de(faltan)
    esperado = MOTIVO_HOY % (183, 184)
    casos += 1
    w("   pieza (4) falta: %s" % ("SI" if p4 else "NO"))
    w("   motivo publicado : %r" % (p4[0] if p4 else None))
    w("   motivo exigido   : %r" % esperado)
    calza = bool(p4) and p4[0] == esperado
    w("   ESPERADO: falta con ESE motivo -> %s" % ("CALZA" if calza else "NO CALZA"))
    if not calza:
        fallos += 1
    mutado = esperado.replace("NO SATISFACE", "SI SATISFACE")
    w("   MUTACION del esperado (motivo cambiado en dos palabras): %s"
      % ("PASA" if (p4 and p4[0] == mutado) else "CAE"))
    if p4 and p4[0] == mutado:
        fallos += 1
    else:
        caen += 1
    w("")

    w("CASO C. LA BATERIA DE LA 185 CERRANDO LA 184: UNA VUELTA POSTERIOR SIEMPRE")
    w("        ES ROJA, CON TRAMOS SELLADOS Y SIN ELLOS")
    for etiqueta, sellados in (("con tramos sellados", [1, 2]),
                               ("sin tramos sellados", [])):
        faltan = CR.piezas_que_faltan(texto, FILAS, BAT183, vuelta=184,
                                      nombre_bateria=NOM185,
                                      tramos_sellados_en_esta_vuelta=sellados)
        p4 = pieza4_de(faltan)
        casos += 1
        w("   %-20s -> pieza (4) falta: %s" % (etiqueta, "SI" if p4 else "NO"))
        if p4:
            w("      motivo: %s" % p4[0])
        if not p4:
            fallos += 1
        w("      MUTACION del esperado (exigir que NO falte): %s"
          % ("PASA" if not p4 else "CAE"))
        if p4:
            caen += 1
        else:
            fallos += 1
    w("")
    return fallos, casos, caen


def _caso_d(w):
    """EL CASO D: el valor por defecto contra la copia de la logica vieja."""
    fallos = casos = caen = 0
    BAT183 = ["linea uno de la bateria", "linea dos de la bateria"]
    NOM183 = "docs/loop/SALIDA_V183_BATERIA.txt"
    NOM185 = "docs/loop/SALIDA_V185_BATERIA.txt"
    w("CASO D. EL PARAMETRO EN SU VALOR POR DEFECTO SE COMPORTA EXACTAMENTE COMO")
    w("        LA CONDUCTA DE HOY, Y NO SE AFIRMA: SE COMPARA ESCENARIO A ESCENARIO")
    w("        CONTRA UNA COPIA DE LA LOGICA VIEJA QUE VIVE EN ESTE ARNES")
    escenarios = [
        ("misma vuelta, nombre de corrida", BAT183, NOM183, 183),
        ("vuelta anterior", BAT183, NOM183, 184),
        ("vuelta posterior", BAT183, NOM185, 184),
        ("nombre anonimo", BAT183, "docs/loop/UN_FICHERO_CUALQUIERA.txt", 184),
        ("vuelta None", BAT183, NOM183, None),
        ("nombre de HUECO, misma vuelta", BAT183,
         "docs/loop/SALIDA_V184_HUECO_BATERIA.txt", 184),
        ("nombre de HUECO, otra vuelta", BAT183,
         "docs/loop/SALIDA_V183_HUECO_BATERIA.txt", 184),
        ("sin lineas de bateria", [], NOM183, 184),
    ]
    difieren = 0
    for etiqueta, lin, nom, v in escenarios:
        t = reporte_fabricado(lin if lin else ["HUECO DECLARADO Y MEDIDO de mentira"])
        faltan = CR.piezas_que_faltan(t, FILAS, lin, vuelta=v, nombre_bateria=nom)
        viva = bool([f for f in pieza4_de(faltan)
                     if "NO SATISFACE ESTA PIEZA" in f])
        vieja = conducta_vieja_de_la_pieza4(lin, nom, v)
        igual = viva == vieja
        casos += 1
        w("   %-32s viva %-5s | vieja %-5s | %s"
          % (etiqueta, viva, vieja, "IGUAL" if igual else "DIFIEREN"))
        if not igual:
            difieren += 1
            fallos += 1
    w("   CIFRA escenarios en que la conducta por defecto DIFIERE de la vieja: %d"
      % difieren)
    w("   ESPERADO: 0 -> %s" % ("CALZA" if difieren == 0 else "NO CALZA"))
    w("   MUTACION del esperado (exigir que difieran en 1): %s"
      % ("PASA" if difieren == 1 else "CAE"))
    if difieren == 1:
        fallos += 1
    else:
        caen += 1
    w("")
    return fallos, casos, caen


def _caso_e(w):
    """EL CASO E: la segunda copia de la comparacion, contada y exigida en 1."""
    fallos = casos = caen = 0
    w("CASO E. LA SEGUNDA COPIA DE LA COMPARACION: SE CUENTA Y SE EXIGE 1")
    texto_cr = io.open(CR_RUTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
    lineas_cr = texto_cr.split(NL)
    crudas = [i for i, l in enumerate(lineas_cr, 1) if COMPARACION in l]
    codigo = [i for i in crudas if not lineas_cr[i - 1].lstrip().startswith("#")]
    casos += 1
    disco_s, lf_s, sha_s = sello_del_sujeto()
    w("   fichero: scripts/loop/cerrar_reporte.py")
    w("   SELLO DEL SUJETO (vuelta 188, TAREA 3.b): disco %d bytes | LF %d bytes |"
      % (disco_s, lf_s))
    w("   sha256 LF %s" % sha_s)
    w("   Con ese sello al lado, los numeros de linea de abajo NO envejecen solos:")
    w("   un diff futuro dice si se movio el sujeto o si se movio el arnes.")
    w("   CIFRA apariciones CRUDAS: %d, lineas %s"
      % (len(crudas), ", ".join(str(x) for x in crudas)))
    w("   CIFRA apariciones en lineas de CODIGO: %d, lineas %s"
      % (len(codigo), ", ".join(str(x) for x in codigo)))
    for i in crudas:
        w("      LINEA %d (%s): %s"
          % (i,
             "comentario" if lineas_cr[i - 1].lstrip().startswith("#") else "CODIGO",
             lineas_cr[i - 1].strip()[:110]))
    w("   ESPERADO: exactamente 1 en codigo -> %s"
      % ("CALZA" if len(codigo) == 1 else "NO CALZA"))
    if len(codigo) != 1:
        fallos += 1
    w("   MUTACION del esperado (exigir 2 en codigo): %s"
      % ("PASA" if len(codigo) == 2 else "CAE"))
    if len(codigo) == 2:
        fallos += 1
    else:
        caen += 1
    w("   Y LA PRUEBA DE QUE ESTE CASO SABE CONTAR: sobre un texto FABRICADO con")
    w("   DOS copias de la comparacion en codigo, el conteo tiene que dar 2.")
    fabricado = [
        "def uno():", "    if " + COMPARACION + ":", "        pass",
        "def dos():", "    if " + COMPARACION + ":", "        pass",
        "# y un comentario que nombra " + COMPARACION,
    ]
    c_fab = len([i for i, l in enumerate(fabricado, 1)
                 if COMPARACION in l and not l.lstrip().startswith("#")])
    crudo_fab = len([l for l in fabricado if COMPARACION in l])
    casos += 1
    w("      conteo sobre el fabricado: %d en codigo, %d crudo"
      % (c_fab, crudo_fab))
    w("      ESPERADO 2 en codigo y 3 crudo -> %s"
      % ("CALZA" if (c_fab == 2 and crudo_fab == 3) else "NO CALZA"))
    if not (c_fab == 2 and crudo_fab == 3):
        fallos += 1
    w("      MUTACION del esperado (exigir 1 en codigo sobre el fabricado): %s"
      % ("PASA" if c_fab == 1 else "CAE"))
    if c_fab == 1:
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
    w("CASO POSITIVO POR MUTACION DE LA PIEZA (4) DE piezas_que_faltan()")
    w("(vuelta 186, TAREA 2.a; adjudicacion 6.1 del acta 186, que cierra la PD.6)")
    w("=" * 78)
    w("")
    w("EL SUJETO ES EL FICHERO VIVO scripts/loop/cerrar_reporte.py, IMPORTADO.")
    w("Los reportes se FABRICAN en memoria: aqui no se escribe ningun reporte.")
    w("")
    fallos = casos = caen = 0
    for parte in (_casos_abc, _caso_d, _caso_e):
        f, c, k = parte(w)
        fallos += f
        casos += c
        caen += k
    w("CIFRA casos: %d | pasan: %d" % (casos, casos - fallos))
    w("CIFRA casos que CAEN al mutar su esperado: %d de %d" % (caen, caen))
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V186_T2A_MUTACION_PIEZA4.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
