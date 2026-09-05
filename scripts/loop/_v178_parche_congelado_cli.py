# -*- coding: utf-8 -*-
r"""_v178_parche_congelado_cli.py . EL CARRIL DE LINEA DE COMANDOS DE LA GUARDA
DEL SUJETO CONGELADO (vuelta 178, TAREA 1.e).

ES UN PARCHE, NO CODIGO VIVO: empieza por guion bajo. Cada sustitucion lleva su
`assert`.
"""
import io
import os

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R = os.path.join(RAIZ, "scripts", "loop", "verificar_mutaciones_viejas.py")

t = io.open(R, encoding="utf-8").read().replace(chr(13) + NL, NL)
PARES = []

PARES.append(('''    ap.add_argument("--tramo", type=int, default=None,''',
'''    ap.add_argument("--sujeto-congelado", dest="sujeto_congelado",
                    action="store_true",
                    help="vuelta 178, TAREA 1.e: LA GUARDA DEL SUJETO CONGELADO. "
                         "Clasifica la nomina entera y CAE EN ROJO si alguna "
                         "entrada tiene SUJETO VIVO o queda NO DECIDIBLE. Corre "
                         "SOLA: no corre ningun arnes y no toca la nomina.")
    ap.add_argument("--tramo", type=int, default=None,'''))

PARES.append(('''    if a.mutar_nomina:
        return prueba_de_la_nomina()''',
'''    if a.mutar_nomina:
        return prueba_de_la_nomina()

    if a.sujeto_congelado:
        return informe_del_sujeto_congelado()'''))

INFORME = '''def informe_del_sujeto_congelado():
    """LA GUARDA DEL SUJETO CONGELADO, CORRIDA Y PUBLICADA (vuelta 178, TAREA
    1.e). NO corre ningun arnes, NO toca la nomina y NO reescribe nada:
    clasifica y publica.

    CAE EN ROJO si alguna entrada de la nomina sale `SUJETO VIVO` o `NO
    DECIDIBLE`. Un `NO DECIDIBLE` es rojo a proposito: la regla de la vuelta 145
    exige sujeto congelado, y un arnes que no deja claro cual es el suyo NO
    demuestra que lo cumpla. La salida verde de una guarda que no pudo mirar es
    exactamente lo que esta casa persigue."""
    print("=" * 78)
    print("LA GUARDA DEL SUJETO CONGELADO (vuelta 178, TAREA 1.e)")
    print("=" * 78)
    print("")
    print("LA REGLA, CITADA Y NO PARAFRASEADA, del docstring de este mismo fichero:")
    print("   'UNA MUTACION ENTRA EN LA VUELTA SIGUIENTE A LA QUE NACE, Y SOLO SI SU")
    print("   SUJETO ESTA CONGELADO' (vuelta 145), y desde la 148 'LO QUE ESTA REGLA")
    print("   EXIGE ES SUJETO CONGELADO. EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL")
    print("   FIN'. Existe desde la 145 y hasta hoy era una frase.")
    print("")
    print("COMO SE MIDE: por la huella que el sujeto deja EN EL CODIGO del arnes.")
    print("   huellas de CONGELADO (en el texto entero): %s"
          % ", ".join(HUELLAS_DE_CONGELADO))
    print("   huellas de VIVO (SOLO en la maquina, sin el docstring de modulo): %s"
          % ", ".join(HUELLAS_DE_VIVO))
    print("   y si trae LAS DOS, la guarda NO ADIVINA: pide que el propio arnes lo")
    print("   declare con el literal %r, y sin esa declaracion sale NO DECIDIBLE."
          % MARCA_DECLARA_CONGELADO)
    print("")

    filas = anclaje_de_la_nomina()
    cuenta = {}
    for _n, v, _c, _vv in filas:
        cuenta[v] = cuenta.get(v, 0) + 1
    print("EL REPARTO, CONTADO DE LA NOMINA VIVA")
    print("| veredicto | entradas |")
    print("|---|---|")
    for v in ("CONGELADO", "CASO DECLARADO", "SUJETO VIVO", "NO DECIDIBLE"):
        print("| %s | %d |" % (v, cuenta.get(v, 0)))
    print("| **total** | **%d** |" % len(filas))
    print("")

    malas = guarda_del_sujeto_congelado()
    print("LAS QUE NO CUMPLEN, UNA A UNA")
    if not malas:
        print("   (ninguna)")
    for nombre, veredicto, vive in malas:
        print("   %-14s %-52s abre: %s"
              % (veredicto, nombre, ", ".join(vive) or "(nada)"))
    print("   CIFRA entradas que no cumplen la regla: %d" % len(malas))
    print("")

    if malas:
        print("ROJO DE LA GUARDA DEL SUJETO CONGELADO: %d entrada(s) de %d no")
        print("demuestran tener sujeto congelado. La regla existe desde la vuelta")
        print("145 y esta es la primera vez que se mide, asi que este rojo NO es una")
        print("regresion: es el estado que la frase tapaba.")
        print("FIN")
        return 1
    print("VERDE DE LA GUARDA DEL SUJETO CONGELADO: las %d entradas de la nomina")
    print("demuestran sujeto congelado o son caso declarado.")
    print("FIN")
    return 0


def main():'''

PARES.append(("def main():", INFORME))

for viejo, nuevo in PARES:
    assert viejo in t, "NO ESTA: " + viejo[:70]
    t = t.replace(viejo, nuevo, 1)

io.open(R, "w", encoding="utf-8", newline=NL).write(t)
print("PARCHES APLICADOS: %d" % len(PARES))
