# -*- coding: utf-8 -*-
r"""_v185_parche_arnes_apertura.py . LA REPARACION DE LA TAREA 1.b DE LA VUELTA
185, APLICADA CON NOMBRE PARA QUE SE PUEDA AUDITAR.

QUE REPARA, Y EL DIAGNOSTICO ESTA MEDIDO DOS VECES (por el ejecutor de la 184 en
`docs/loop/SALIDA_V183_BATERIA_TRAMO_9.txt` y por el auditor en el punto 3.5 del
acta 185, y coinciden): `scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py`
sale `exit 0` y sus catorce casos pasan; lo unico que falla es que ESCRIBE EN SU
SALIDA SELLADA UN DATO QUE CAMBIA SOLO, el sufijo del `mkdtemp` de la linea 124,
que se cuela por las lineas 134 y 154. La bateria compara byte a byte las dos
corridas y lo caza.

QUE HACE, Y NADA MAS QUE ESTO:
  1. Anade la funcion PURA `sin_temporal(linea, tmp)`.
  2. La aplica en las dos lineas `w("      | " + l[:130])` ANTES del recorte,
     nunca despues: recortar primero puede partir la ruta por la mitad y dejar
     media sin normalizar.
  3. NO TOCA LO QUE EL ARNES PRUEBA. Sus catorce casos siguen siendo los mismos,
     no se afloja ningun esperado y no se le quita ningun escenario.

ESTE PARCHE ES IDEMPOTENTE: si la reparacion ya esta puesta, lo dice y no
escribe.

USO:
  python scripts/loop/_v185_parche_arnes_apertura.py
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SUJETO = os.path.join(RAIZ, "scripts", "loop",
                      "vuelta182_tarea2_mutacion_apertura_auditor.py")
NL = chr(10)

MARCA = "def sin_temporal("

NOTA_DOCSTRING = '''
LA REPARACION DE LA VUELTA 185, TAREA 1.b, DECLARADA AQUI Y NO ESCONDIDA. Este
arnes salia `exit 0` y sus catorce casos pasaban, pero ESCRIBIA EN SU SALIDA
SELLADA UN DATO QUE CAMBIA SOLO: el sufijo aleatorio del `mkdtemp` se colaba en
el informe de `sellar()` que los bloques C y D pegan, y la doble corrida de la
bateria, que compara byte a byte, lo cazaba. Tres lineas de diferencia, las 53,
54 y 55 de su salida, y nada mas. La reparacion es `sin_temporal()`, PURA, que
sustituye TODAS las formas de esa ruta por el literal `<TEMPORAL>` ANTES del
recorte a 130 caracteres: recortar primero partiria la ruta por la mitad y
dejaria media sin normalizar. LO QUE ESTE ARNES PRUEBA NO SE TOCO: los catorce
casos son los mismos, ningun esperado se afloja y ningun escenario se quita.
ESTA REPARACION REESCRIBE `docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt`
con `<TEMPORAL>` dentro, y eso es esperado y se dice. Su arnes propio es
`scripts/loop/vuelta185_tarea1b_mutacion_sin_temporal.py`.
'''

FUNCION = '''

# LA MARCA QUE SUSTITUYE A LA RUTA DEL TEMPORAL. Es un literal y no una cadena
# vacia a proposito: borrar la ruta dejaria la linea muda sobre el hecho de que
# ahi habia una ruta, y esta casa prefiere que se vea el hueco.
MARCA_TEMPORAL = "<TEMPORAL>"


def sin_temporal(linea, tmp):
    """LA RUTA DEL TEMPORAL, SUSTITUIDA POR `<TEMPORAL>` EN TODAS SUS FORMAS.
    PURA: recibe dos cadenas y devuelve una, no lee ni escribe nada, y por eso
    su arnes la puede tumbar caso por caso sin tocar el repo.

    LAS CUATRO FORMAS QUE CUBRE, y las cuatro hacen falta porque el informe de
    `sellar()` no promete ninguna en concreto:
      - LA ABSOLUTA, tal cual la devuelve `mkdtemp`.
      - LA RELATIVA CON BARRA NORMAL, que es la que salio de verdad en las
        lineas 53 a 55 de la salida sellada.
      - LA RELATIVA CON BARRA INVERTIDA, que es la que `os.path.relpath`
        devuelve en Windows antes de que nadie la normalice.
      - EL NOMBRE BASE SUELTO del directorio, que es la unica forma que sigue
        cazando el sufijo aleatorio venga la ruta de donde venga.

    SE SUSTITUYE DE LA MAS LARGA A LA MAS CORTA. Si el nombre base se cambiara
    antes que la ruta que lo contiene, la ruta quedaria a medias y la linea
    seguiria siendo distinta entre dos corridas, que es justo lo que esto viene
    a impedir.

    Y NO NORMALIZA DE MAS: una linea que no lleve ninguna de las cuatro formas
    dentro sale IDENTICA, byte a byte."""
    if not tmp or not linea:
        return linea
    abso = os.path.abspath(tmp)
    formas = []
    for cruda in (tmp, abso, os.path.normpath(tmp)):
        formas.append(cruda)
        formas.append(cruda.replace(chr(92), "/"))
        formas.append(cruda.replace("/", chr(92)))
    try:
        rela = os.path.relpath(abso)
        formas.append(rela)
        formas.append(rela.replace(chr(92), "/"))
        formas.append(rela.replace("/", chr(92)))
    except ValueError:
        pass
    formas.append(os.path.basename(os.path.normpath(tmp)))
    for forma in sorted({f for f in formas if f}, key=len, reverse=True):
        linea = linea.replace(forma, MARCA_TEMPORAL)
    return linea

'''

VIEJA = 'w("      | " + l[:130])'
NUEVA = 'w("      | " + sin_temporal(l, tmp)[:130])'


def main():
    texto = io.open(SUJETO, encoding="utf-8").read().replace(chr(13) + NL, NL)
    if MARCA in texto:
        print("YA ESTA PUESTA: %r aparece en el sujeto. No se escribe nada." % MARCA)
        return 0
    cuantas = texto.count(VIEJA)
    print("CIFRA apariciones de %r antes del parche: %d" % (VIEJA, cuantas))
    if cuantas != 2:
        raise SystemExit("ROJO: se esperaban 2 apariciones y hay %d. No se toca "
                         "nada." % cuantas)
    # 1. LA NOTA EN EL DOCSTRING, ANTES DEL BLOQUE `USO:`
    ancla = NL + "USO:" + NL
    if ancla not in texto:
        raise SystemExit("ROJO: no encuentro el bloque USO: del docstring.")
    texto = texto.replace(ancla, NOTA_DOCSTRING + ancla, 1)
    # 2. LA FUNCION, DETRAS DE LA CONSTANTE NL
    ancla2 = 'NL = chr(10)' + NL
    if ancla2 not in texto:
        raise SystemExit("ROJO: no encuentro la constante NL del sujeto.")
    texto = texto.replace(ancla2, ancla2 + FUNCION, 1)
    # 3. LAS DOS LINEAS, CON LA NORMALIZACION ANTES DEL RECORTE
    texto = texto.replace(VIEJA, NUEVA)
    io.open(SUJETO, "w", encoding="utf-8", newline=NL).write(texto)
    print("ESCRITO: %s" % SUJETO)
    de_nuevo = io.open(SUJETO, encoding="utf-8").read().replace(chr(13) + NL, NL)
    print("CIFRA apariciones de %r despues: %d" % (NUEVA, de_nuevo.count(NUEVA)))
    print("CIFRA apariciones de la vieja despues: %d" % de_nuevo.count(VIEJA))
    print("CIFRA lineas: %d | CIFRA bytes: %d"
          % (de_nuevo.count(NL), len(de_nuevo.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
