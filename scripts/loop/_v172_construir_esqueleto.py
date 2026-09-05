# -*- coding: utf-8 -*-
r"""_v172_construir_esqueleto.py . ANDAMIO DE UN SOLO USO DE LA VUELTA 172.

CONSTRUYE `scripts/loop/vuelta172_esqueleto_reporte.py` como CLON DECLARADO de
`vuelta171_esqueleto_reporte.py`, desde el original y en un solo acto, con sus
assert de cuantas apariciones espera cada sustitucion.

LO QUE CAMBIA, Y LO SEGUNDO ES UN ARREGLO MEDIDO, NO UN CAPRICHO:

  A. el numero de vuelta y las cinco filas de tarea, que son las de ESTE
     encargo.

  B. EL PATRON DEL ACTA DEJA DE SER UNA SOLA FORMA. El clon de la 171 buscaba
     el commit del acta con la cadena "ACTA DE LA VUELTA 170 DEL AUDITOR", una
     sola forma. EL ASUNTO DEL COMMIT DEL ACTA 171 ES "ACTA DEL AUDITOR,
     VUELTA 171: ...", que es LA OTRA forma del titulo, la que nacio en la
     vuelta 106. Con una sola forma el esqueleto de la 172 caeria en ROJO por
     cero aciertos, y la cifra no seria falsa pero la vuelta no abriria.
     `tallar_cabecera_reporte.py` YA tiene las DOS formas escritas en
     `commit_apertura_desde_git`, asi que aqui se usan las dos y no se estrena
     ninguna. La regla de "exactamente UN acierto" no se toca.

  C. el rotulo del paso 0, que en la 171 decia "TAREA 5.a de esta misma vuelta"
     porque el archivador nacio alli. Aqui ya no es de esta vuelta.

USO:  python scripts/loop/_v172_construir_esqueleto.py
"""
import io
import os
import py_compile

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
ORIGEN = os.path.join(LOOP, "vuelta171_esqueleto_reporte.py")
DESTINO = os.path.join(LOOP, "vuelta172_esqueleto_reporte.py")

CAMBIOS = 0

TAREAS = '''TAREAS = [
    ("1", "BLOQUEANTE Y VA PRIMERA. EL CIERRE QUE FALTA Y LOS REGISTROS (1.a el reporte de la 171 CERRADO con la cabecera tallada pegada, sus cuatro discutibles y su caida sin suavizar, y la seccion 9 diciendo que la bateria NO corrio; 1.b el acta 171 y sus adjudicaciones 6.1 a 6.12 al `R.41` con su arnes de mutacion del registro; 1.c el archivador para la 171 y este esqueleto)"),
    ("2", "BLOQUEANTE PARA LA 3. SE DESENVENENA EL CONTADOR Y SE CORRIGE EL `R.40` (adjudicaciones 6.1 y 6.3): 2.a `docs/loop/reportes/REPORTE_V<N>.md` entra en los narrativos del bucle POR PATRON, con su caso positivo por mutacion; 2.b la afirmacion falsa del `R.40` corregida por el carril del `9.10` con el reparto recomputado; 2.c el contador otra vez, con la atribucion fichero a fichero y linea a linea"),
    ("3", "LA NUMERACION `LD`, QUE AHORA SI SE ESCRIBE (adjudicacion 6.2): las 16 filas de la segunda tanda de `docs/plan/LECTURAS_DIRIGIDAS.md` ganan `LD-139` a `LD-154` POR ADICION PURA, con los numeros COMPUTADOS y con dos guardas que tienen que caer por mutacion; y despues la fila de `docs/plan/00_INDICE.md` recibe su cifra de hoy por `9.21` (adjudicacion 6.10)"),
    ("4", "LOS TRES ARNESES Y LA BATERIA (adjudicaciones 6.4 y 6.5), Y EL ORDEN ES OBLIGATORIO: 4.a el caso `F` de `vuelta171_tarea5a_mutacion_enchufe.py` refundado sobre SUJETO CONGELADO; 4.b los tres arneses de la 171 dentro de la nomina de `verificar_mutaciones_viejas.py`; 4.c la bateria corrida ENTERA Y SOLA al cierre, con su salida en la seccion 9"),
    ("5", "EL CIERRE DEL REPORTE DEJA DE SER UN PASO A MANO (adjudicacion 6.6): nace `scripts/loop/cerrar_reporte.py`, de nombre estable y sin numero de vuelta, que pega la cabecera, anexa el cuerpo, escribe el veredicto y CAE EN ROJO si al terminar falta cualquiera de las cuatro piezas. Con su caso positivo por mutacion, y esta vuelta se cierra con el"),
]'''

BUSQUEDA_VIEJA = [
    'actas, anclado = TALLADOR.buscar_acta(filas_log, [re.compile("^" + re.escape(PATRON_ACTA))])',
]

BUSQUEDA_NUEVA = [
    '# LAS DOS FORMAS DEL TITULO DEL ACTA, Y NO UNA (vuelta 172). El clon de la 171',
    '# buscaba una sola cadena. El asunto del commit del acta 171 es "ACTA DEL',
    '# AUDITOR, VUELTA 171: ...", que es LA OTRA forma, la nacida en la vuelta 106,',
    '# asi que con una sola forma esto daria CERO aciertos y el esqueleto no',
    '# abriria. Las dos formas ya estan escritas en',
    '# tallar_cabecera_reporte.py:commit_apertura_desde_git y aqui se usan esas,',
    '# sin estrenar ninguna. La exigencia de EXACTAMENTE UN acierto no se toca.',
    'actas, anclado = TALLADOR.buscar_acta(filas_log, PATRONES_ACTA)',
]


def rep(t, viejo, nuevo, veces=1):
    global CAMBIOS
    n = t.count(viejo)
    assert n == veces, "esperaba %d de %r, hay %d" % (veces, viejo[:70], n)
    CAMBIOS += n
    return t.replace(viejo, nuevo)


def main():
    t = io.open(ORIGEN, encoding="utf-8").read().replace(chr(13) + NL, NL)

    t = rep(t, 'r"""vuelta171_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA' + NL +
            'VUELTA 171, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS CINCO TAREAS ENCARGADAS.',
            'r"""vuelta172_esqueleto_reporte.py . ABRE docs/loop/REPORTE.md AL EMPEZAR LA' + NL +
            'VUELTA 172, CON EL ESQUELETO Y LAS FILAS VACIAS DE LAS CINCO TAREAS ENCARGADAS.' + NL + NL +
            'CLON DECLARADO de scripts/loop/vuelta171_esqueleto_reporte.py, construido desde' + NL +
            'el original por scripts/loop/_v172_construir_esqueleto.py. Cambia el numero de' + NL +
            'vuelta, las cinco filas de tarea y LA BUSQUEDA DEL ACTA, que pasa de una sola' + NL +
            'forma del titulo a las DOS que tallar_cabecera_reporte.py ya tenia escritas: el' + NL +
            'asunto del commit del acta 171 empieza por "ACTA DEL AUDITOR, VUELTA 171", que' + NL +
            'es la forma nacida en la vuelta 106, y con una sola forma esto daria cero' + NL +
            'aciertos. NO SE ESTRENA NINGUN PATRON y la exigencia de UN SOLO acierto queda.')

    t = rep(t, 'VUELTA = 171' + NL +
            'PATRON_ACTA = "ACTA DE LA VUELTA %d DEL AUDITOR" % (VUELTA - 1)',
            'VUELTA = 172' + NL +
            '# LAS DOS FORMAS DEL TITULO, COPIADAS DE tallar_cabecera_reporte.py:920-921.' + NL +
            'PATRONES_ACTA = [' + NL +
            '    re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR" % (VUELTA - 1)),' + NL +
            '    re.compile(r"^ACTA DEL AUDITOR,\\s*VUELTA %d" % (VUELTA - 1)),' + NL +
            ']' + NL +
            'PATRON_ACTA = "ACTA DE LA VUELTA %d DEL AUDITOR o ACTA DEL AUDITOR, VUELTA %d" % (' + NL +
            '    VUELTA - 1, VUELTA - 1)')

    i = t.index("TAREAS = [")
    j = t.index("]", t.index('5.c el barrido MEDIDO')) + 1
    t = t[:i] + TAREAS + t[j:]

    t = rep(t, NL.join(BUSQUEDA_VIEJA), NL.join(BUSQUEDA_NUEVA))

    t = rep(t, '> **Y EL ESQUELETO YA NO PUEDE PISAR UN REPORTE SIN ARCHIVAR** (TAREA 5.a de esta' + NL +
            '> misma vuelta): su paso 0 corre el archivador y **se niega a escribir** si el' + NL +
            '> reporte anterior no esta guardado byte a byte. Esta corrida lo paso en verde' + NL +
            '> contra `docs/loop/reportes/REPORTE_V%(ant)d.md`.',
            '> **Y EL ESQUELETO YA NO PUEDE PISAR UN REPORTE SIN ARCHIVAR** (guarda nacida en' + NL +
            '> la TAREA 5.a de la vuelta 171): su paso 0 corre el archivador y **se niega a' + NL +
            '> escribir** si el reporte anterior no esta guardado byte a byte. **Y esa guarda' + NL +
            '> YA MORDIO en la vuelta siguiente a la que nacio**: corrida en modo solo' + NL +
            '> comprobacion al abrir esta vuelta, dijo ROJO por su clausula (d), porque el' + NL +
            '> `REPORTE.md` del arbol era el de la 171 sin cerrar. Esta corrida lo paso en' + NL +
            '> verde contra `docs/loop/reportes/REPORTE_V%(ant)d.md` **solo despues de que la' + NL +
            '> TAREA 1.a cerrara ese reporte**.')

    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(t)
    py_compile.compile(DESTINO, doraise=True)
    print("CONSTRUIDO: %s" % os.path.relpath(DESTINO, RAIZ).replace(os.sep, "/"))
    print("CIFRA sustituciones con assert: %d (mas la tabla de TAREAS)" % CAMBIOS)
    print("COMPILA: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
