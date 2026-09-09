# -*- coding: utf-8 -*-
r"""_v220_gen_cierre_integral.py . COMPONE scripts/loop/_v220_cierre_integral.py
A PARTIR DEL DE LA 219.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3).

POR QUE SE COMPONE Y NO SE IMPORTA, DICHO ANTES DE HACERLO Y CON EL MISMO MOTIVO
QUE LA 219 ESCRIBIO. El de la 219 se podria importar y solo cambiarle los datos,
que seria la via de IMPORTAR NO ES CLONAR. NO SIRVE AQUI, y el motivo es de
ATRIBUCION y no de comodidad: ese instrumento lleva la palabra "218" COSIDA A LA
PROSA DE SU PROPIA SALIDA (la columna de contraste se rotula "la 218", en tres
sitios). Importarlo dejaria una salida sellada que atribuye a la 218 unas cifras
que quien las publico fue la 219. Publicar una cifra con la atribucion
equivocada es exactamente lo que EJECUTOR.md 8 prohibe.

QUE SE CONSERVA Y QUE SE CAMBIA, PARA QUE SE PUEDA AUDITAR SIN LEER LOS DOS
FICHEROS: se conserva ENTERA la mecanica (las nueve mediciones, sus guardas y su
sellado). Se cambian CUATRO cosas y este compositor las CUENTA y las imprime:
  1. el docstring;
  2. MOVIDA_A_PROPOSITO, que esta vuelta deja VACIO tambien, porque la bateria
     restaura lo que toca y sus once tramos lo comprueban en su PASO 5;
  3. CONTRASTE_218, que pasa a CONTRASTE_219 con las cifras que la 219 publico
     en docs/loop/SALIDA_V219_CIERRE_INTEGRAL.txt y SIN movimiento esperado;
  4. las tres frases de main() que rotulan la columna de contraste.
"""
import io
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))

src = io.open(os.path.join(AQUI, "_v219_cierre_integral.py"),
              encoding="utf-8").read().replace(chr(13) + chr(10), chr(10))
cambios = []

# --- 1. el docstring ------------------------------------------------------
i0 = src.index('r"""')
i1 = src.index('"""', i0 + 4) + 3
DOC = chr(10).join([
    'r"""_v220_cierre_integral.py . EL CIERRE INTEGRAL DE LA VUELTA 220, MEDIDO.',
    '',
    'COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).',
    '',
    'NO ES UNA TAREA DEL ENCARGO: el encargo de esta vuelta trae DOS tareas, el',
    'registro y la bateria. Esto es el cierre que EJECUTOR.md exige de toda vuelta,',
    'y por eso sus cifras van en la seccion 3 del reporte y no en la tabla de tareas.',
    '',
    'QUE MIDE, Y TODO SE LEE DE FICHEROS DE SALIDA QUE YA EXISTEN EN DISCO:',
    '  . el ciclo entero de Gate 0 por los DOS lados, con sus DIECIOCHO salidas',
    '    selladas y sus dos consolas, que el propio ciclo escribio;',
    '  . las TRES suites solas, cada una con su exitcode y sus bytes;',
    '  . el marcador y el censo, recomputados cada uno con su comando;',
    '  . las sedes que la vuelta pudo mover, cotejadas por sha256 entre la apertura',
    '    y el cierre;',
    '  . la moratoria: cuantos ficheros escribio esta vuelta en el arbol de scripts',
    '    y cuantos llevan el prefijo que le toca.',
    '',
    'LA DIFERENCIA CON LA 219, DICHA ANTES DE MEDIR Y NO DESCUBIERTA DESPUES. Aquella',
    'vuelta era LECTURA de punta a punta. ESTA CORRE LA BATERIA ENTERA, y la bateria',
    'SI toca ficheros mientras corre: sus arneses escriben y restauran. Aun asi',
    'MOVIDA_A_PROPOSITO va VACIO, y no por descuido: cada uno de los once tramos',
    'comprueba en su PASO 5 que git diff --numstat sobre dataset/ da CERO filas al',
    'salir, y las once comprobaciones salieron limpias. CUALQUIER sede que se mueva',
    'aqui es ROJO.',
    '',
    'Y LA COLUMNA DE CONTRASTE ES LO QUE LA 219 PUBLICO, no lo que mi encargo dice: mi',
    'encargo de esta vuelta NO trae cifras de marcador ni de censo (EJECUTOR.md 2, el',
    'instrumento manda y una cifra vieja se cita como contraste, nunca como fuente).',
    '',
    'USO:  python scripts/loop/_v220_cierre_integral.py',
    '"""',
])
src = src[:i0] + DOC + src[i1:]
cambios.append("el docstring")

# --- 2. MOVIDA_A_PROPOSITO, que sigue vacio pero con el motivo de ESTA vuelta -
j0 = src.index("MOVIDA_A_PROPOSITO = {")
j1 = src.index("}" + chr(10), j0) + 2
MOV = chr(10).join([
    "MOVIDA_A_PROPOSITO = {",
    "    # VACIO A PROPOSITO Y DECLARADO. La TAREA 1 de la 220 es LECTURA,",
    "    # MEDICION y REGISTRO. La TAREA 2 corre la bateria entera, cuyos",
    "    # arneses SI escriben mientras corren, pero cada uno de los once",
    "    # tramos comprueba en su PASO 5 que git diff --numstat sobre dataset/",
    "    # da CERO filas al salir. Ninguna sede de esta lista se mueve a",
    "    # proposito, y CUALQUIERA que se mueva es ROJO, sin excepcion",
    "    # declarada.",
    "}",
    "",
])
src = src[:j0] + MOV + src[j1:]
cambios.append("MOVIDA_A_PROPOSITO, que sigue vacio y con el motivo de la 220")

# --- 3. la columna de contraste ------------------------------------------
k0 = src.index("CONTRASTE_218 = [")
k1 = src.index("]" + chr(10), k0) + 2
CIFRAS = [("marcador n", "3388"), ("marcador A", "550"), ("marcador B", "71"),
          ("marcador C", "5"), ("marcador D", "2762"),
          ("marcador huecos", "0"), ("censo nodos", "3853"),
          ("censo vivos", "3169"), ("censo deprecados", "684"),
          ("aristas siguientes", "8780"), ("aristas previos", "8740"),
          ("aristas suma", "17520"), ("aristas union", "9914")]
CON = chr(10).join(
    ["# LO QUE LA 219 PUBLICO EN docs/loop/SALIDA_V219_CIERRE_INTEGRAL.txt,",
     "# CITADO COMO CONTRASTE Y NO COMO FUENTE (EJECUTOR.md 2). NINGUNA lleva",
     "# movimiento esperado, porque esta vuelta no mueve ninguna.",
     "CONTRASTE_219 = ["]
    + ["    (%r, %r, None)," % (a, b) for a, b in CIFRAS]
    + ["]", ""])
src = src[:k0] + CON + src[k1:]
cambios.append("CONTRASTE_218 pasa a CONTRASTE_219 con las 13 cifras de la 219")

# --- 4. las frases que rotulan la columna --------------------------------
antes = src.count("CONTRASTE_218") + src.count("la 218")
src = src.replace("CONTRASTE_218", "CONTRASTE_219")
src = src.replace("LAS QUE LA 218 PUBLICO", "LAS QUE LA 219 PUBLICO")
src = src.replace("LO QUE LA 218 PUBLICO", "LO QUE LA 219 PUBLICO")
src = src.replace("la 218 %-8s", "la 219 %-8s")
cambios.append("las frases que rotulan la columna de contraste")

destino = os.path.join(AQUI, "_v220_cierre_integral.py")
io.open(destino, "w", encoding="utf-8", newline=chr(10)).write(src)
print("COMPUESTO %s -> %d bytes" % (os.path.basename(destino),
                                    len(src.encode("utf-8"))))
print("CIFRA cosas cambiadas: %d | CIFRA que este compositor declara: 4"
      % len(cambios))
for c in cambios:
    print("   cambio> %s" % c)
print("CIFRA menciones de la 218 que quedan en el compuesto: %d | CIFRA que se "
      "exige: 0" % len(re.findall(r"CONTRASTE_218|la 218 ", src)))
print("CIFRA guiones largos en el compuesto: %d | CIFRA guiones medios: %d"
      % (src.count(chr(8212)), src.count(chr(8211))))
