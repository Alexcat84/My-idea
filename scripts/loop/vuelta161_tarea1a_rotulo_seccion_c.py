# -*- coding: utf-8 -*-
"""vuelta161_tarea1a_rotulo_seccion_c.py . CAIDA PROPIA DE LA VUELTA 161,
CAZADA LEYENDO MI PROPIA SALIDA ANTES DE COMMITEARLA, Y SU REMEDIO.

QUE PASO. La TAREA 1.a cambio quien manda en la nomina principal de
`vuelta159_tarea5_alcance_p16.py`: antes mandaba la LECTURA B (contiene el
patron) y desde el arreglo manda la CLASIFICACION POR CONTENIDO. Pero el rotulo
impreso encima de esa nomina se quedo como estaba y sigue diciendo
"C) LA NOMINA PRINCIPAL (lectura B), UNA A UNA". Leida la salida
`docs/loop/SALIDA_V161_T1A_ALCANCE_DESPUES.txt`, ese rotulo MIENTE sobre su
propia fuente: la lectura B da DIECISIETE y la lista que imprime debajo tiene
DOCE. Es una celda de rotulo tecleada que ya no describe lo que hay debajo, que
es la especie exacta que EJECUTOR.md 1 persigue.

EL REMEDIO: el rotulo dice de donde sale la nomina. La linea vieja no se borra,
queda TACHADA Y LEGIBLE en el comentario de encima, como las otras cuatro.

USO:  python scripts/loop/vuelta161_tarea1a_rotulo_seccion_c.py
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DESTINO = os.path.join(RAIZ, "scripts", "loop", "vuelta159_tarea5_alcance_p16.py")
MARCA = "ROTULO DE LA SECCION C (vuelta 161, TAREA 1.a)"

VIEJO = '    print("C) LA NOMINA PRINCIPAL (lectura B), UNA A UNA")'
NUEVO = ('    # ROTULO DE LA SECCION C (vuelta 161, TAREA 1.a). Linea vieja TACHADA Y\n'
         '    # LEGIBLE, no borrada. Decia "lectura B" cuando la nomina de debajo ya\n'
         '    # no sale de la lectura B sino de la clasificacion por contenido: la\n'
         '    # lectura B da 17 y la lista tiene 12.\n'
         '    #     ~~print("C) LA NOMINA PRINCIPAL (lectura B), UNA A UNA")~~\n'
         '    print("C) LA NOMINA PRINCIPAL (clase ALCANCE de la seccion E), UNA A UNA")')


MARCA_2 = "ROTULO DE LA CIFRA DE LA SECCION C (vuelta 161, TAREA 1.a)"

VIEJO_2 = '    print("   CIFRA ficheros con el patron: %d" % len(principal))'
NUEVO_2 = ('    # ROTULO DE LA CIFRA DE LA SECCION C (vuelta 161, TAREA 1.a). Linea vieja\n'
           '    # TACHADA Y LEGIBLE, no borrada. Decia "ficheros con el patron" y contaba\n'
           '    # la nomina del ALCANCE: chocaba de frente con la seccion E, que publica\n'
           '    # 17 con ese mismo rotulo. Los que contienen el patron son 17; los del\n'
           '    # alcance son 12.\n'
           '    #     ~~print("   CIFRA ficheros con el patron: %d" % len(principal))~~\n'
           '    print("   CIFRA ficheros en el alcance: %d" % len(principal))')

EDICIONES = [
    (MARCA, VIEJO, NUEVO,
     '~~print("C) LA NOMINA PRINCIPAL (lectura B), UNA A UNA")~~'),
    (MARCA_2, VIEJO_2, NUEVO_2,
     '~~print("   CIFRA ficheros con el patron: %d" % len(principal))~~'),
]


def main():
    aplicadas = 0
    saltadas = 0
    for marca, viejo, nuevo, tachada in EDICIONES:
        texto = io.open(DESTINO, encoding="utf-8").read()
        if marca in texto:
            print("YA ESTABA, se salta: %s" % marca)
            saltadas += 1
            continue
        n = texto.count(viejo)
        print("CIFRA veces que aparece el texto viejo de '%s': %d" % (marca, n))
        if n != 1:
            print("PARADA: tiene que aparecer exactamente UNA. No se escribe nada.")
            return 1
        with io.open(DESTINO, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(texto.replace(viejo, nuevo, 1))
        if tachada not in io.open(DESTINO, encoding="utf-8").read():
            print("ROJO: la linea vieja no quedo tachada y legible: %s" % tachada)
            return 1
        print("   aplicada, y la linea vieja queda tachada y legible")
        aplicadas += 1
    print("CIFRA ediciones aplicadas: %d" % aplicadas)
    print("CIFRA ediciones ya escritas de antes: %d" % saltadas)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
