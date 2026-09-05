# -*- coding: utf-8 -*-
r"""vuelta169_tarea2_mutacion_reanclaje.py . CASO POSITIVO POR MUTACION DEL RE
ANCLAJE DEL ARNES DEL RETRATO (TAREA 2 de la vuelta 169), CON NOMBRE DE ARNES
para que la bateria lo vea (invoca cada arnes SIN ARGUMENTOS).

POR QUE HACE FALTA, Y NO ES BUROCRACIA. `EJECUTOR.md` 1, "EL CASO ROJO SE PRUEBA
POR MUTACION": ningun assert, guarda o caso rojo se publica como prueba sin haber
corrido antes su prueba de mutacion. La TAREA 2 acaba de re anclar dos casos y de
anadir una guarda nueva; si esa guarda no cae cuando debe caer, el re anclaje es
un adorno y la bateria volvera a salir verde sobre nada.

SU SUJETO ESTA CONGELADO, que es la condicion de entrada de la nomina (coletilla
de la vuelta 145, letra desde la 148): NO lee `docs/plan/RECOMPUTO_3388.md`, que
es el documento VIVO y se mueve cada vez que la campana corrige una fila. Fabrica
sus propias celdas EN MEMORIA con la forma que `T.PAT_CONTADOR` espera, y las
tres guardas se prueban sobre esas. CERO ESCRITURAS.

LAS TRES COSAS QUE PRUEBA, Y CADA UNA ES UNA MITAD DEL ARREGLO:

  (A) LA CONSTANTE SALE DEL COMPUTO Y SIGUE TENIENDO FILO. El re anclaje cambio
      el esperado de `"TRECE VECES"` a `T.CARDINAL[cuantas + 1]`. Si eso fuera
      una tautologia, el caso no podria caer nunca y seria justo la caida de la
      vuelta 89 (un caso rojo que se aprueba solo). NO LO ES, y aqui se
      demuestra: el REAL sale de `T.cuadrar_contador` y el ESPERADO de
      `T.CARDINAL` leido con la cadena contada, que son DOS caminos. Se fabrica
      un `cuadrar_contador` ROTO que hace lo que la caida historica hacia (LEER
      LA PALABRA ESCRITA en vez de contar la cadena) y se exige que el caso CAIGA.

  (B) LA GUARDA NUEVA CAE CUANDO EL REPLACE NO MUERDE. Se reproduce el modo de
      fallo exacto de la vuelta 168: un `replace` clavado a un literal que la
      celda ya no tiene. Se exige que la guarda `mutada != t` de FALSE, o sea que
      el caso CAIGA.

  (C) Y LA VERSION NUEVA SI MUERDE SOBRE LA MISMA CELDA. Sin esta mitad, (B)
      pasaria igual con un arreglo que no arregla nada.

USO:  python scripts/loop/vuelta169_tarea2_mutacion_reanclaje.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta166_tarea3_retrato_de_las_a as T   # noqa: E402

ARNES = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "vuelta166_tarea3_mutacion_retrato.py")


def celda_fabricada(n_tachadas, palabra):
    """Una fila con la forma que PAT_CONTADOR y anatomia esperan, fabricada EN
    MEMORIA. Las cifras tachadas son de mentira a proposito: lo que se prueba es
    el contador, no el retrato."""
    # DOS COLUMNAS Y NO TRES: `anatomia` y `cuadrar_contador` leen `split("|")[2]`,
    # que en una fila de la casa es la SEGUNDA celda. Una fila fabricada con una
    # columna de mas pondria la cadena donde el instrumento no mira, y la prueba
    # saldria verde sobre una celda vacia. Cazado corriendo esta prueba, no supuesto.
    tach = " ".join("~~**%d**~~" % (10 + i) for i in range(n_tachadas))
    orden = " ".join("~~%s~~" % T.CARDINAL[i].split()[0] for i in range(1, n_tachadas))
    return ("| fila de mentira | %s **999** **[CORREGIDA %s%s, motivo de mentira]** |"
            % (tach, (orden + " ") if orden else "", palabra))


def cuadrar_contador_ROTO(celda, correcciones_ya):
    """LA CAIDA HISTORICA, REPRODUCIDA A PROPOSITO: lee la palabra ESCRITA en vez
    de contar la cadena. Es lo que el comentario de `cuadrar_contador` dice que
    NO se puede hacer, y lo que este arnes existe para poder tumbar."""
    m = T.PAT_CONTADOR.search(celda)
    if not m:
        return celda, None, T.CARDINAL[correcciones_ya + 1]
    vivo = "%s %s" % (m.group(2), m.group(3))
    return celda, vivo, vivo


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 169, TAREA 2: CASO POSITIVO POR MUTACION DEL RE ANCLAJE")
    print("=" * 78)
    print("")

    antes_arnes = io.open(ARNES, encoding="utf-8", newline="").read()
    casos = []

    print("A) EL RE ANCLAJE ESTA EN EL FICHERO, Y LO VIEJO SIGUE CITADO")
    for lit, rotulo in ((' T.CARDINAL[cuantas + 1]', "el esperado sale del computo"),
                        ('T.CARDINAL[cm + 1]', "y el segundo caso tambien"),
                        ('B_la_mutacion_MUERDE_el_texto_vivo', "la guarda nueva existe"),
                        ('palabra_viva = ', "la palabra viva se lee del texto"),
                        ('"TRECE VECES"', "la constante vieja sigue citada"),
                        ('DOCE VECES,', "el literal viejo sigue citado")):
        hay = lit in antes_arnes
        print("   %-38s %s" % (rotulo, hay))
        casos.append(("A_%s" % rotulo.replace(" ", "_"), hay, True))
    print("")

    print("B) (A) LA CONSTANTE SALE DEL COMPUTO Y NO ES UNA TAUTOLOGIA")
    for n in (12, 13, 14):
        celda = celda_fabricada(n, T.CARDINAL[n])
        _t, _viva, cuantas = T.anatomia(celda)
        _c, _antes, despues_bueno = T.cuadrar_contador(celda.split("|")[2], cuantas)
        esperado = T.CARDINAL[cuantas + 1]
        _c2, _a2, despues_roto = cuadrar_contador_ROTO(celda.split("|")[2], cuantas)
        print("   con %d tachadas y la palabra %-14s -> cadena contada %d"
              % (n, T.CARDINAL[n], cuantas))
        print("      el bueno computa %-16s y el esperado es %-16s -> PASA: %s"
              % (despues_bueno, esperado, despues_bueno == esperado))
        print("      el ROTO devuelve  %-16s -> el caso CAE: %s"
              % (despues_roto, despues_roto != esperado))
        casos.append(("B_%d_la_cadena_manda_y_el_caso_pasa" % n,
                      despues_bueno, esperado))
        casos.append(("B_%d_con_cuadrar_contador_ROTO_el_caso_CAE" % n,
                      despues_roto != esperado, True))
        casos.append(("B_%d_la_cadena_contada_no_es_la_palabra_escrita" % n,
                      cuantas, n))
    print("")

    print("C) (B) LA GUARDA NUEVA CAE CUANDO EL REPLACE NO MUERDE")
    celda = celda_fabricada(13, T.CARDINAL[13])
    literal_muerto = "%s," % T.CARDINAL[12]      # 'DOCE VECES,', el clavado viejo
    mutada_vieja = celda.replace(literal_muerto, "%s," % T.CARDINAL[2], 1)
    print("   la celda de mentira lleva la palabra %r" % T.CARDINAL[13])
    print("   el replace CLAVADO busca %r, que la celda no tiene" % literal_muerto)
    print("   la celda cambia: %s" % (mutada_vieja != celda))
    print("   la guarda nueva (mutada != t) da %s y el caso espera True: CAE %s"
          % (mutada_vieja != celda, (mutada_vieja != celda) is False))
    casos.append(("C_el_replace_clavado_NO_muta", mutada_vieja != celda, False))
    casos.append(("C_y_por_eso_la_guarda_nueva_CAE",
                  (mutada_vieja != celda) is False, True))
    print("")

    print("D) (C) Y LA VERSION NUEVA SI MUERDE SOBRE LA MISMA CELDA")
    m_viva = T.PAT_CONTADOR.search(celda.split("|")[2])
    palabra_viva = "%s %s" % (m_viva.group(2), m_viva.group(3))
    palabra_falsa = T.CARDINAL[2] if palabra_viva != T.CARDINAL[2] else T.CARDINAL[3]
    mutada_nueva = celda.replace(palabra_viva + ",", palabra_falsa + ",", 1)
    print("   la palabra viva se lee del texto: %r" % palabra_viva)
    print("   se muta a %r" % palabra_falsa)
    print("   la celda cambia: %s" % (mutada_nueva != celda))
    _t2, _v2, cm = T.anatomia(mutada_nueva)
    print("   y la CADENA no se movio: %d tachadas antes y %d despues"
          % (13, cm))
    casos.append(("D_la_version_nueva_SI_muta", mutada_nueva != celda, True))
    casos.append(("D_y_no_toca_la_cadena", cm, 13))
    casos.append(("D_la_palabra_viva_se_leyo_y_no_se_teclo",
                  palabra_viva, T.CARDINAL[13]))
    print("")

    print("E) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-56s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("F) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        else:
            mutado = str(esperado) + "_mutado"
        cae = (real != mutado)
        print("   %-56s %s" % (nombre, "CAE" if cae else "NO CAE"))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    print("G) Y SE COMPRUEBA QUE ESTA PRUEBA NO ESCRIBIO NADA")
    despues_arnes = io.open(ARNES, encoding="utf-8", newline="").read()
    igual = (antes_arnes == despues_arnes)
    print("   el arnes hermano sigue identico byte a byte: %s" % igual)
    if not igual:
        print("   ROJO: la prueba de mutacion escribio.")
        return 1
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
