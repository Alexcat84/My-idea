# -*- coding: utf-8 -*-
r"""vuelta169_tarea2_reanclar_retrato.py . RE ANCLA EL ARNES DEL RETRATO
(TAREA 2 de la vuelta 169, adjudicacion 6.2 del acta 168).

QUE ARREGLA, Y NO SE ARREGLA AFLOJANDO NADA. El arnes
`scripts/loop/vuelta166_tarea3_mutacion_retrato.py` salio en ROJO en la bateria
de la vuelta 168 con `NO MORDIO`, 3 casos de 23. La causa medida por el acta 168
(su 4.2) es que el arnes tiene DOS anclas clavadas al texto vivo:

  (a) el valor esperado de dos de sus casos era la CONSTANTE LITERAL
      "TRECE VECES", mientras que el valor real se COMPUTA de la cadena de
      tachadas. La vuelta 167 anadio una tachada por el carril del banco 9.10,
      el computo paso a CATORCE y la constante se quedo en TRECE.
  (b) la mutacion `t.replace("DOCE VECES,", "DOS VECES,", 1)` buscaba un literal
      que el documento vivo YA NO TIENE. El replace no encontraba nada, la fila
      NO se mutaba, y el caso que esperaba que la guarda CAYERA recibia CUADRA.
      ESE ES EL MODO DE FALLO QUE DEJO LA GUARDA MUDA: una mutacion que no muta
      no prueba nada, y sin una guarda que lo detecte nadie se entera.

LA VARA ES LA MISMA QUE LA CASA USO EN EL 3.b DE LA VUELTA 168: EL NUMERO
CAMBIA, EL FILO NO. Los dos casos siguen siendo igualdades exactas y siguen
cayendo si la cadena y la palabra se desincronizan; lo que deja de estar clavado
es el numeral concreto de esta semana.

LO QUE ESTE PARCHE ANADE, Y ES LA MITAD QUE FALTABA: un caso nuevo,
`B_la_mutacion_MUERDE_el_texto_vivo`, que CAE si el replace no cambia nada.

LO QUE ESTE PARCHE NO HACE: no toca ni una comprobacion del arnes, no quita
ningun caso, no cambia el documento `docs/plan/RECOMPUTO_3388.md` y no toca el
modulo `vuelta166_tarea3_retrato_de_las_a.py`.

TERCER RETOQUE, DECLARADO Y NO ENCARGADO POR NOMBRE: el rotulo del caso
`C_las_doce_tachadas_viejas_sobreviven` teclea DOCE cuando su propia cifra sale
de `len(tach)`, que hoy vale 13. Es la MISMA especie que (a), no afloja ninguna
comprobacion (solo el rotulo) y se declara en el reporte como retoque de rotulo.

USO:
  python scripts/loop/vuelta169_tarea2_reanclar_retrato.py            (parchea)
  python scripts/loop/vuelta169_tarea2_reanclar_retrato.py --comprobar (solo mide)
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARNES = os.path.join(RAIZ, "scripts", "loop", "vuelta166_tarea3_mutacion_retrato.py")

# CADA SUSTITUCION ES (viejo, nuevo, rotulo). Si un `viejo` no aparece EXACTAMENTE
# UNA VEZ, el parche PARA y no escribe nada: un parche que no encuentra su sujeto
# es la misma enfermedad que este parche viene a curar.
CAMBIOS = [
    (
        '    casos.append(("B_con_%d_tachadas_el_siguiente_es_TRECE" % cuantas,\n'
        '                  despues_p, "TRECE VECES"))\n',
        '    # (2.a) RE ANCLADO EN LA VUELTA 169, adjudicacion 6.2 del acta 168.\n'
        '    # LA PALABRA ESPERADA SALE DEL COMPUTO, igual que `cuantas`, y NO de una\n'
        '    # constante tecleada. Antes decia, literal: despues_p, "TRECE VECES", y\n'
        '    # el 4 sep 2026 la vuelta 167 anadio una tachada por el carril del 9.10:\n'
        '    # el computo paso a CATORCE, la constante se quedo en TRECE y el caso\n'
        '    # empezo a fallar por su valor esperado y no por su sujeto. EL FILO NO SE\n'
        '    # AFLOJA: despues_p sigue saliendo de T.cuadrar_contador y el esperado\n'
        '    # de T.CARDINAL leido con `cuantas`, que son DOS caminos distintos; si\n'
        '    # cuadrar_contador volviera a leer la palabra escrita en vez de contar\n'
        '    # la cadena, este caso CAE.\n'
        '    siguiente = T.CARDINAL[cuantas + 1]\n'
        '    casos.append(("B_con_%d_tachadas_el_siguiente_es_%s"\n'
        '                  % (cuantas, siguiente.split()[0]), despues_p, siguiente))\n',
        "(2.a) primer caso: la constante sale del computo",
    ),
    (
        '    mutada = t.replace("DOCE VECES,", "DOS VECES,", 1)\n',
        '    # (2.b) RE ANCLADO EN LA VUELTA 169, adjudicacion 6.2 del acta 168.\n'
        '    # LA MUTACION DEJA DE ESTAR CLAVADA AL TEXTO VIVO. Antes decia, literal:\n'
        '    # t.replace("DOCE VECES,", "DOS VECES,", 1), y el dia que la fila crecio\n'
        '    # ese literal dejo de existir: el replace no encontraba nada, la fila no se\n'
        '    # mutaba y el caso que espera que la guarda CAIGA recibia CUADRA. Ahora se\n'
        '    # muta LA PALABRA QUE EL PROPIO INSTRUMENTO ACABA DE LEER, y la palabra\n'
        '    # falsa sale de T.CARDINAL eligiendo una DISTINTA de la viva.\n'
        '    m_viva = T.PAT_CONTADOR.search(t.split("|")[2])\n'
        '    palabra_viva = "%s %s" % (m_viva.group(2), m_viva.group(3))\n'
        '    palabra_falsa = T.CARDINAL[2] if palabra_viva != T.CARDINAL[2] else T.CARDINAL[3]\n'
        '    mutada = t.replace(palabra_viva + ",", palabra_falsa + ",", 1)\n'
        '    # Y LA GUARDA QUE FALTABA, que es la que dejaba muda a la de abajo:\n'
        '    # si el replace no cambia NADA, este caso CAE y el arnes sale en rojo, en\n'
        '    # vez de seguir corriendo sobre una fila sin mutar.\n'
        '    casos.append(("B_la_mutacion_MUERDE_el_texto_vivo", mutada != t, True))\n',
        "(2.b) la mutacion muta lo que acaba de leer, con guarda que cae",
    ),
    (
        '    casos.append(("B_mutar_la_palabra_no_mueve_el_computo", despues2, "TRECE VECES"))\n',
        '    # (2.a, segundo caso) MISMO RE ANCLAJE. Antes decia, literal:\n'
        '    # despues2, "TRECE VECES". El esperado sale de `cm`, que es la cadena\n'
        '    # contada SOBRE LA FILA YA MUTADA: si la mutacion de la palabra tocara la\n'
        '    # cadena sin querer, `cm` cambiaria y este caso CAE.\n'
        '    casos.append(("B_mutar_la_palabra_no_mueve_el_computo",\n'
        '                  despues2, T.CARDINAL[cm + 1]))\n',
        "(2.a) segundo caso: la constante sale del computo",
    ),
    (
        '    print("   se MUTA la palabra a DOS VECES sin tocar la cadena")\n',
        '    print("   se MUTA la palabra viva %r a %r sin tocar la cadena"\n'
        '          % (palabra_viva, palabra_falsa))\n',
        "(2.b) el rotulo impreso sale del computo",
    ),
    (
        '    casos.append(("C_las_doce_tachadas_viejas_sobreviven", sobreviven, len(tach)))\n',
        '    # RETOQUE DE ROTULO DECLARADO EN LA VUELTA 169 (no encargado por nombre,\n'
        '    # declarado en el reporte): el rotulo tecleaba DOCE y su propia cifra sale\n'
        '    # de len(tach), que hoy vale 13. Ninguna comprobacion cambia.\n'
        '    casos.append(("C_las_%d_tachadas_viejas_sobreviven" % len(tach),\n'
        '                  sobreviven, len(tach)))\n',
        "rotulo de C: el numeral sale de len(tach)",
    ),
]

# LOS LITERALES QUE NO PUEDEN DESAPARECER DEL FICHERO: el carril del banco 9.10
# exige que ninguna palabra vieja se borre, y aqui las palabras viejas son los
# tres literales que este parche desclava. Siguen citados en los comentarios.
LITERALES_VIEJOS = ['"TRECE VECES"', 'DOCE VECES,', 'DOS VECES,']


def main():
    solo_medir = "--comprobar" in sys.argv
    texto = io.open(ARNES, encoding="utf-8", newline="").read()
    print("=" * 78)
    print("VUELTA 169, TAREA 2: RE ANCLAJE DE vuelta166_tarea3_mutacion_retrato.py")
    print("=" * 78)
    print("")
    print("A) EL SUJETO, MEDIDO ANTES DE TOCARLO")
    print("   ruta: scripts/loop/vuelta166_tarea3_mutacion_retrato.py")
    print("   CIFRA bytes antes: %d" % len(texto.encode("utf-8")))
    print("   CIFRA lineas antes: %d" % texto.count("\n"))
    print("")

    print("B) CADA SUSTITUCION SE BUSCA, Y SI NO APARECE EXACTAMENTE UNA VEZ, PARA")
    fallos = []
    for viejo, _nuevo, rotulo in CAMBIOS:
        n = texto.count(viejo)
        print("   %-58s apariciones: %d" % (rotulo, n))
        if n != 1:
            fallos.append("%s aparece %d veces" % (rotulo, n))
    if fallos:
        print("")
        print("ROJO, NO SE ESCRIBE NADA:")
        for f in fallos:
            print("   " + f)
        return 1
    print("   CIFRA sustituciones localizadas: %d de %d" % (len(CAMBIOS), len(CAMBIOS)))
    print("")

    nuevo_texto = texto
    for viejo, nuevo, _rotulo in CAMBIOS:
        nuevo_texto = nuevo_texto.replace(viejo, nuevo, 1)

    print("C) NINGUNA PALABRA VIEJA SE BORRA, COMPROBADO Y NO AFIRMADO")
    for lit in LITERALES_VIEJOS:
        print("   el literal %-16s sigue en el fichero: %s" % (lit, lit in nuevo_texto))
    quedan = [lit for lit in LITERALES_VIEJOS if lit not in nuevo_texto]
    if quedan:
        print("   ROJO: estos literales desaparecieron del fichero: %s" % quedan)
        return 1
    print("")

    print("D) EL FICHERO SOLO CRECE Y SIGUE COMPILANDO")
    print("   CIFRA bytes despues: %d" % len(nuevo_texto.encode("utf-8")))
    print("   CIFRA lineas despues: %d" % nuevo_texto.count("\n"))
    print("   crece y no encoge: %s" % (len(nuevo_texto) > len(texto)))
    try:
        compile(nuevo_texto, ARNES, "exec")
        print("   compile() del texto nuevo: OK")
    except SyntaxError as e:
        print("   ROJO: el texto nuevo no compila: %s" % e)
        return 1
    print("")

    if solo_medir:
        print("MODO --comprobar: NO se escribe.")
        return 0

    io.open(ARNES, "w", encoding="utf-8", newline="").write(nuevo_texto)
    print("ESCRITO: scripts/loop/vuelta166_tarea3_mutacion_retrato.py")
    print("VERDE: las %d sustituciones aplicadas, ninguna comprobacion quitada."
          % len(CAMBIOS))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
