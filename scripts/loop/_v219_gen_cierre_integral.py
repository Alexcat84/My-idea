# -*- coding: utf-8 -*-
r"""_v219_gen_cierre_integral.py . COMPONE scripts/loop/_v219_cierre_integral.py
A PARTIR DEL DE LA 218.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3).

POR QUE SE COMPONE Y NO SE IMPORTA, DICHO ANTES DE HACERLO. El de la 218 se
podria importar y solo cambiarle los datos, y esa seria la via de IMPORTAR NO ES
CLONAR. NO SIRVE AQUI, y el motivo es de ATRIBUCION y no de comodidad: ese
instrumento lleva la palabra "217" COSIDA A LA PROSA DE SU PROPIA SALIDA (la
columna de contraste se rotula "la 217"), y la columna que ESTA vuelta le da es
LO QUE LA 218 PUBLICO. Importarlo dejaria una salida sellada que atribuye a la
217 unas cifras de la 218, y dos de esas cifras (la B y la D del marcador)
CAMBIARON entre las dos actas. Publicar una cifra con la atribucion equivocada
es exactamente lo que EJECUTOR.md 8 prohibe.

QUE SE CONSERVA Y QUE SE CAMBIA, PARA QUE SE PUEDA AUDITAR SIN LEER LOS DOS
FICHEROS: se conserva ENTERA la mecanica (las nueve mediciones, sus guardas y su
sellado). Se cambian CUATRO cosas y este compositor las CUENTA y las imprime:
  1. el docstring;
  2. MOVIDA_A_PROPOSITO, que esta vuelta deja VACIO porque no mueve NINGUNA sede;
  3. CONTRASTE_217, que pasa a CONTRASTE_218 con las cifras que la 218 publico y
     SIN ningun movimiento esperado;
  4. las tres frases de main() que rotulan la columna de contraste.
"""
import io
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))

src = io.open(os.path.join(AQUI, "_v218_cierre_integral.py"),
              encoding="utf-8").read().replace(chr(13) + chr(10), chr(10))
cambios = []

# --- 1. el docstring ------------------------------------------------------
i0 = src.index('r"""')
i1 = src.index('"""', i0 + 4) + 3
DOC = '\n'.join([
    'r"""_v219_cierre_integral.py . EL CIERRE INTEGRAL DE LA VUELTA 219, MEDIDO.',
    '',
    'COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).',
    '',
    'NO ES UNA TAREA DEL ENCARGO: el encargo de esta vuelta trae DOS tareas y las dos',
    'son lectura. Esto es el cierre que EJECUTOR.md exige de toda vuelta, y por eso',
    'sus cifras van en la seccion 3 del reporte y no en la tabla de tareas.',
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
    'LA DIFERENCIA CON LA 218, DICHA ANTES DE MEDIR Y NO DESCUBIERTA DESPUES. Aquella',
    'vuelta movia DOS cifras del marcador y UNA sede a proposito, y las declaraba por',
    'adelantado. ESTA VUELTA NO MUEVE NINGUNA: sus dos tareas son lectura, medicion y',
    'registro, y no escriben ni en el plan ni en el grafo ni en el registro del',
    'cribado. Por eso MOVIDA_A_PROPOSITO va VACIO y las trece cifras del contraste van',
    'SIN movimiento esperado: CUALQUIERA que se mueva es ROJO.',
    '',
    'Y LA COLUMNA DE CONTRASTE ES LO QUE LA 218 PUBLICO, no lo que mi encargo dice: mi',
    'encargo de esta vuelta NO trae cifras de marcador ni de censo (EJECUTOR.md 2, el',
    'instrumento manda y una cifra vieja se cita como contraste, nunca como fuente).',
    '',
    'USO:  python scripts/loop/_v219_cierre_integral.py',
    '"""',
])
src = src[:i0] + DOC + src[i1:]
cambios.append("docstring")

# --- 2. MOVIDA_A_PROPOSITO ------------------------------------------------
j0 = src.index("MOVIDA_A_PROPOSITO = {")
j1 = src.index("}\n", j0) + 2
MOV = ('MOVIDA_A_PROPOSITO = {\n'
       '    # VACIO A PROPOSITO Y DECLARADO: las dos tareas de la 219 son\n'
       '    # LECTURA, MEDICION y REGISTRO. Ninguna escribe en el plan, ni en\n'
       '    # el grafo, ni en docs/INTRA_DOMINIO_VEREDICTOS.jsonl. CUALQUIER\n'
       '    # sede que se mueva es ROJO, sin excepcion declarada.\n'
       '}\n')
src = src[:j0] + MOV + src[j1:]
cambios.append("MOVIDA_A_PROPOSITO")

# --- 3. la tabla de contraste --------------------------------------------
k0 = src.index("# LO QUE LA 217 PUBLICO")
k1 = src.index("]\n", k0) + 2
CON = '\n'.join([
    '# LO QUE LA 218 PUBLICO, CITADO COMO CONTRASTE Y NO COMO FUENTE (EJECUTOR.md 2).',
    '# NINGUNA lleva movimiento esperado, porque esta vuelta no mueve ninguna.',
    'CONTRASTE_218 = [',
    '    ("marcador n", "3388", None),',
    '    ("marcador A", "550", None),',
    '    ("marcador B", "71", None),',
    '    ("marcador C", "5", None),',
    '    ("marcador D", "2762", None),',
    '    ("marcador huecos", "0", None),',
    '    ("censo nodos", "3853", None),',
    '    ("censo vivos", "3169", None),',
    '    ("censo deprecados", "684", None),',
    '    ("aristas siguientes", "8780", None),',
    '    ("aristas previos", "8740", None),',
    '    ("aristas suma", "17520", None),',
    '    ("aristas union", "9914", None),',
    ']',
    '',
])
src = src[:k0] + CON + src[k1:]
cambios.append("CONTRASTE_218")

# --- 4. las frases de main() que rotulan la columna -----------------------
PARES = [
    ('w("3.5. LAS CIFRAS, COTEJADAS CONTRA LAS QUE LA 217 PUBLICO, Y NO COPIADAS")',
     'w("3.5. LAS CIFRAS, COTEJADAS CONTRA LAS QUE LA 218 PUBLICO, Y NO COPIADAS")'),
    ('vuelta NO trae cifras de marcador ni de censo. Es LO QUE LA 217 PUBLICO, "',
     'vuelta NO trae cifras de marcador ni de censo. Es LO QUE LA 218 PUBLICO, "'),
    ('    w("   Y LOS DOS MOVIMIENTOS ESPERADOS VAN ESCRITOS ANTES DE MEDIRLOS, no "\n'
     '      "descubiertos despues.")',
     '    w("   Y ESTA VUELTA NO DECLARA NINGUN MOVIMIENTO ESPERADO, porque no mueve "\n'
     '      "nada: las TRECE tienen que quedarse quietas y cualquiera que se mueva es "\n'
     '      "ROJO.")'),
    ('   COTEJO %-22s | LA MIA %-8s | la 217 %-8s | esperado %-46s | %s',
     '   COTEJO %-22s | LA MIA %-8s | la 218 %-8s | esperado %-46s | %s'),
    ('for etiqueta, suya, movimiento in CONTRASTE_217:',
     'for etiqueta, suya, movimiento in CONTRASTE_218:'),
    ('% (len(CONTRASTE_217), descuadres))',
     '% (len(CONTRASTE_218), descuadres))'),
]
for viejo, nuevo in PARES:
    if src.count(viejo) != 1:
        raise SystemExit("ROJO: el fragmento %r aparece %d vez(ces) y se exige 1."
                         % (viejo[:60], src.count(viejo)))
    src = src.replace(viejo, nuevo)
    cambios.append("frase: " + viejo[:52])

destino = os.path.join(AQUI, "_v219_cierre_integral.py")
io.open(destino, "w", encoding="utf-8", newline="\n").write(src)
print("COMPUESTO %s -> %d bytes" % (os.path.basename(destino),
                                    len(src.encode("utf-8"))))
print("CIFRA piezas cambiadas: %d | CIFRA que este compositor declara: %d"
      % (len(cambios), 3 + len(PARES)))
for c in cambios:
    print("   cambiado> %s" % c)
sobra = re.findall(r"\b217\b", src)
print("CIFRA apariciones del numero 217 que quedan en el compuesto: %d | CIFRA "
      "que deberia haber: 0" % len(sobra))
if sobra:
    raise SystemExit("ROJO: el compuesto todavia atribuye algo a la 217.")
print("VERDE: el cierre integral de la 219 queda compuesto y sin atribuciones "
      "a la 217.")
