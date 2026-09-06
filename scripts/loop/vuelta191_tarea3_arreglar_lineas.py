# -*- coding: utf-8 -*-
r"""vuelta191_tarea3_arreglar_lineas.py . EL ARREGLO DE LOS DOCE INSTRUMENTOS QUE
PUBLICABAN UNA SOLA CIFRA DE LINEAS POR LA CONVENCION QUE NO CALZA CON `wc -l`.

QUE ARREGLA, Y NO ES UNA LISTA ESCOGIDA A OJO: **es exactamente la lista que
saca `scripts/loop/dos_convenciones_de_lineas.py` en su bloque `B`**, corrido
ANTES de tocar nada. La medicion va primero y el arreglo despues, que es lo que
el encargo pide con esas palabras y la misma disciplina que la `P.2` del acta 190.

QUE HACE CON CADA SITIO. Lo deja publicando **LA PAREJA**, con la que calza con
`wc -l` nombrada dentro de la propia frase. La otra salida que la vara admite
(publicar solo la que calza, diciendolo) tambien valdria; se elige la pareja
porque es lo que la casa ya hace con los BYTES y porque **no borra la cifra
vieja**: quien lea un reporte cerrado que diga 2231 encuentra el 2231 al lado del
2230 y entiende la discrepancia sin tener que adivinarla.

LO QUE NO TOCA, Y LAS TRES RAZONES VAN MEDIDAS Y NO SUPUESTAS:

  . **NINGUN REPORTE CERRADO.** Un reporte cerrado no se reescribe. Aqui se
    cambia lo que los instrumentos IMPRIMIRIAN si se volvieran a correr, no lo
    que ya publicaron.
  . **NINGUNA ENTRADA DE LA NOMINA DE LA BATERIA.** Se comprueba contra
    `verificar_mutaciones_viejas.VIEJAS`, corrido aqui: un arnes de la nomina se
    re corre y su salida se compara byte a byte, asi que cambiar lo que imprime
    pondria la bateria de la 194 en rojo por un cambio que no es un fallo. Si
    alguno de los doce estuviera en la nomina, **este fichero lo salta y lo
    declara**.
  . **NINGUN SITIO YA CORREGIDO CON `- 1`**, que es la correccion declarada del
    propio detector: `len(t.split(NL)) - 1` ya calza.

CADA CAMBIO ES UNA PAREJA LITERAL `(viejo, nuevo)` y **el viejo tiene que
aparecer EXACTAMENTE UNA VEZ** en su fichero. Si aparece cero veces o dos, el
fichero NO se toca y sale en rojo: un reemplazo que no sabe donde cae no se hace.

USO:
  python scripts/loop/vuelta191_tarea3_arreglar_lineas.py --simular
  python scripts/loop/vuelta191_tarea3_arreglar_lineas.py
"""
import argparse
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dos_convenciones_de_lineas as DC   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
NL = chr(10)
SALIDA = "docs/loop/SALIDA_V191_T3_ARREGLO.txt"

# LA FRASE DE LA CASA, PEGADA IGUAL EN LOS TRECE SITIOS PARA QUE SE PUEDA COTEJAR
# DE UN GREP. `wc -l` va nombrado DENTRO de la frase: ese es el punto entero.
_PAR = "%d lineas por count(NL), que calza con wc -l, y %d por len(split(NL))"

CAMBIOS = [
    ("_v145_cuerpo_reporte.py", [
        ('print("escrito docs/loop/REPORTE.md, %d lineas" % len(texto.split("\\n")))',
         'print("escrito docs/loop/REPORTE.md, ' + _PAR + '"\n'
         '      % (texto.count("\\n"), len(texto.split("\\n"))))'),
    ]),
    ("_v63_construir_fundidor.py", [
        ('print("  lineas del ancestro: %d" % len(fuente.split(NL)))',
         'print("  lineas del ancestro: ' + _PAR + '"\n'
         '          % (fuente.count(NL), len(fuente.split(NL))))'),
        ('print("ESCRITO: %s (%d lineas)" % (os.path.relpath(DESTINO, RAIZ), len(salida.split(NL))))',
         'print("ESCRITO: %s (' + _PAR + ')"\n'
         '          % (os.path.relpath(DESTINO, RAIZ), salida.count(NL),\n'
         '             len(salida.split(NL))))'),
    ]),
    ("vuelta162_tarea6_escribir_reporte.py", [
        ('    n = len(texto.split("\\n"))\n'
         '    print("   CIFRA lineas del reporte escrito: %d" % n)',
         '    n = len(texto.split("\\n"))\n'
         '    print("   CIFRA lineas del reporte escrito: ' + _PAR + '"\n'
         '          % (texto.count("\\n"), n))'),
    ]),
    ("vuelta164_tarea7_escribir_reporte.py", [
        ('print("REPORTE.md escrito: %d lineas" % len(texto.split("\\n")))',
         'print("REPORTE.md escrito: ' + _PAR + '"\n'
         '          % (texto.count("\\n"), len(texto.split("\\n"))))'),
    ]),
    ("vuelta165_tarea7_escribir_reporte.py", [
        ('    print("   docs/loop/REPORTE.md, %d lineas, %d bytes"\n'
         '          % (len(final.split("\\n")), len(final.encode("utf-8"))))',
         '    print("   docs/loop/REPORTE.md, ' + _PAR + ', %d bytes"\n'
         '          % (final.count("\\n"), len(final.split("\\n")),\n'
         '             len(final.encode("utf-8"))))'),
    ]),
    ("vuelta166_tarea3b_motivo.py", [
        ('    print("   CIFRA lineas antes: %d | despues: %d"\n'
         '          % (len(lineas), len(t2.split("\\n"))))',
         '    print("   CIFRA lineas antes: %d por len(split(NL)) | despues: ' + _PAR + '"\n'
         '          % (len(lineas), t2.count("\\n"), len(t2.split("\\n"))))'),
    ]),
    ("vuelta166_tarea4b_correccion_declarada.py", [
        ('    print("   CIFRA lineas antes: %d | despues: %d"\n'
         '          % (len(lineas), len(t2.split("\\n"))))',
         '    print("   CIFRA lineas antes: %d por len(split(NL)) | despues: ' + _PAR + '"\n'
         '          % (len(lineas), t2.count("\\n"), len(t2.split("\\n"))))'),
    ]),
    ("vuelta166_tarea5b_frontera_ld07.py", [
        ('    print("   CIFRA lineas antes: %d | despues: %d"\n'
         '          % (len(lineas), len(t2.split("\\n"))))',
         '    print("   CIFRA lineas antes: %d por len(split(NL)) | despues: ' + _PAR + '"\n'
         '          % (len(lineas), t2.count("\\n"), len(t2.split("\\n"))))'),
    ]),
    ("vuelta168_tarea1_adosar_nota_r36.py", [
        ('print("   CIFRA lineas del fichero DESPUES: %d" % len(relee.split("\\n")))',
         'print("   CIFRA lineas del fichero DESPUES: ' + _PAR + '"\n'
         '          % (relee.count("\\n"), len(relee.split("\\n"))))'),
        ('print("   CIFRA lineas anadidas: %d" % (len(relee.split("\\n")) - largo_antes))',
         'print("   CIFRA lineas anadidas: %d (la resta cancela el uno de mas de\\n'
         '   len(split(NL)), porque largo_antes se conto igual)"\n'
         '          % (len(relee.split("\\n")) - largo_antes))'),
    ]),
    ("vuelta182_tarea1b_remedio_e1.py", [
        ('    w("   ANTES: %d lineas | disco %d bytes | LF %d bytes"\n'
         '      % (len(t.split(NL)), os.path.getsize(CER), len(t.encode("utf-8"))))',
         '    w("   ANTES: ' + _PAR + ' | disco %d bytes | LF %d bytes"\n'
         '      % (t.count(NL), len(t.split(NL)), os.path.getsize(CER),\n'
         '         len(t.encode("utf-8"))))'),
        ('    w("   DESPUES: %d lineas | LF %d bytes"\n'
         '      % (len(nuevo.split(NL)), len(nuevo.encode("utf-8"))))',
         '    w("   DESPUES: ' + _PAR + ' | LF %d bytes"\n'
         '      % (nuevo.count(NL), len(nuevo.split(NL)),\n'
         '         len(nuevo.encode("utf-8"))))'),
    ]),
    ("vuelta47_marcador_indice.py", [
        ('    print("  bloque leido: %d lineas, acotado al marcador VIGENTE" %\n'
         '          len(bloque.split("\\n")))',
         '    print("  bloque leido: ' + _PAR + ', acotado al marcador VIGENTE"\n'
         '          % (bloque.count("\\n"), len(bloque.split("\\n"))))'),
    ]),
    ("vuelta65_caso_positivo_generador.py", [
        ('print("     %-10s exit %d | %d lineas" % (etq, cod, len(s.split(NL))))',
         'print("     %-10s exit %d | ' + _PAR + '"\n'
         '              % (etq, cod, s.count(NL), len(s.split(NL))))'),
    ]),
]


def nomina():
    """LOS NOMBRES DE LA NOMINA DE LA BATERIA, LEIDOS DEL INSTRUMENTO Y NO
    TECLEADOS. Devuelve un conjunto, o None si no se pudo leer."""
    try:
        import verificar_mutaciones_viejas as VMV
    except Exception:
        return None
    n = set()
    for e in VMV.VIEJAS:
        if isinstance(e, str):
            n.add(e)
        elif isinstance(e, (tuple, list)) and e:
            n.add(e[0])
        elif isinstance(e, dict):
            n.add(e.get("nombre") or e.get("fichero"))
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true",
                    help="mide y dice que haria, pero NO escribe")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    rojos = []
    w("=" * 78)
    w("VUELTA 191, TAREA 3: EL ARREGLO DE LAS DOS CONVENCIONES DE `lineas`")
    w("=" * 78)
    w("")

    w("A) LA MEDICION VA PRIMERO, Y LA LISTA SALE DE ELLA Y NO DE MI")
    filas = DC.censo(LOOP)
    en_rojo = [n for n, v, _s in filas if v == DC.ROJO]
    w("   CIFRA ficheros .py censados: %d" % len(filas))
    w("   CIFRA en ROJO ANTES de tocar nada: %d" % len(en_rojo))
    for n in en_rojo:
        w("      %s" % n)
    mios = [n for n, _c in CAMBIOS]
    w("   CIFRA ficheros que este arreglo nombra: %d" % len(mios))
    faltan = [n for n in en_rojo if n not in mios]
    sobran = [n for n in mios if n not in en_rojo]
    w("   EN ROJO Y NO NOMBRADOS AQUI: %d (%s)"
      % (len(faltan), ", ".join(faltan) or "ninguno"))
    w("   NOMBRADOS AQUI Y NO EN ROJO: %d (%s)"
      % (len(sobran), ", ".join(sobran) or "ninguno"))
    # LA IDEMPOTENCIA, Y ES UNA CORRECCION DECLARADA DE ESTE INSTRUMENTO. Su
    # primera version salia en ROJO al RE CORRERSE, porque despues de arreglar
    # los doce el censo ya no los saca y la lista dejaba de calzar. Un arreglo
    # que se acusa a si mismo de haber funcionado no sirve de guarda. Un fichero
    # nombrado que YA lleva la frase de la pareja esta ARREGLADO, no descuadrado.
    ya_arreglados = []
    descuadrados = []
    for n in sobran:
        ruta = os.path.join(LOOP, n)
        c = io.open(ruta, encoding="utf-8", errors="replace").read() if os.path.isfile(ruta) else ""
        (ya_arreglados if _PAR in c else descuadrados).append(n)
    w("   DE ESOS, YA ARREGLADOS (llevan la frase de la pareja): %d (%s)"
      % (len(ya_arreglados), ", ".join(ya_arreglados) or "ninguno"))
    w("   DE ESOS, DESCUADRADOS DE VERDAD: %d (%s)"
      % (len(descuadrados), ", ".join(descuadrados) or "ninguno"))
    if faltan or descuadrados:
        rojos.append("la lista del arreglo no calza con la del censo")
    w("")

    w("B) LA NOMINA DE LA BATERIA, LEIDA DEL INSTRUMENTO, PARA NO PISAR UNA")
    w("   SALIDA SELLADA QUE SE COMPARA BYTE A BYTE")
    nom = nomina()
    if nom is None:
        w("   NO SE PUDO LEER LA NOMINA. PARADA: no se toca nada a ciegas.")
        rojos.append("no se pudo leer la nomina de la bateria")
    else:
        w("   CIFRA entradas de la nomina: %d" % len(nom))
        chocan = [n for n in mios if n in nom]
        w("   CIFRA de los que este arreglo nombra que estan en la nomina: %d (%s)"
          % (len(chocan), ", ".join(chocan) or "ninguno"))
        for n in chocan:
            w("      SE SALTA Y SE DECLARA: %s" % n)
    if rojos:
        w("")
        w("ROJO, %d motivo(s), y NO se toca ningun fichero:" % len(rojos))
        for r in rojos:
            w("   " + r)
        texto = NL.join(L) + NL
        io.open(os.path.join(RAIZ, SALIDA.replace("/", os.sep)), "w",
                encoding="utf-8", newline=NL).write(texto)
        print(texto)
        return 1
    w("")

    w("C) LOS CAMBIOS, UNO A UNO, CON SU CUENTA DE APARICIONES")
    tocados = 0
    sitios = 0
    for nombre, pares in CAMBIOS:
        ruta = os.path.join(LOOP, nombre)
        if nom is not None and nombre in nom:
            w("   %s -> SALTADO por estar en la nomina" % nombre)
            continue
        if not os.path.isfile(ruta):
            w("   %s -> NO EXISTE" % nombre)
            rojos.append("no existe %s" % nombre)
            continue
        codigo = io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)
        if _PAR in codigo:
            # LA IDEMPOTENCIA OTRA VEZ, Y AQUI ES DONDE DE VERDAD MUERDE: re
            # corrido, el viejo ya no esta en ninguno de los doce, y sin esta
            # rama este instrumento se acusaria de no encontrar lo que el mismo
            # arreglo. **Un arreglo que se declara roto por haber funcionado no
            # sirve de guarda.**
            w("   %-46s YA ARREGLADO: lleva la frase de la pareja, no se toca"
              % nombre)
            continue
        nuevo = codigo
        ok = True
        for viejo, reemplazo in pares:
            n = nuevo.count(viejo)
            w("   %-46s el viejo aparece %d vez(ces)" % (nombre, n))
            if n != 1:
                w("      NO SE TOCA: un reemplazo que no sabe donde cae no se hace.")
                w("      viejo buscado: %r" % viejo[:100])
                rojos.append("%s: el viejo aparece %d veces" % (nombre, n))
                ok = False
                continue
            nuevo = nuevo.replace(viejo, reemplazo)
            sitios += 1
        if not ok or nuevo == codigo:
            continue
        if a.simular:
            w("   %s -> --simular: NO se escribe (%d -> %d bytes)"
              % (nombre, len(codigo.encode("utf-8")), len(nuevo.encode("utf-8"))))
        else:
            io.open(ruta, "w", encoding="utf-8", newline=NL).write(nuevo)
            w("   %s -> ESCRITO (%d -> %d bytes)"
              % (nombre, len(codigo.encode("utf-8")), len(nuevo.encode("utf-8"))))
        tocados += 1
    w("   CIFRA ficheros tocados: %d | CIFRA sitios reemplazados: %d"
      % (tocados, sitios))
    w("")

    w("D) LA COMPROBACION, RECORRIENDO EL CENSO DESPUES")
    filas2 = DC.censo(LOOP)
    en_rojo2 = [n for n, v, _s in filas2 if v == DC.ROJO]
    w("   CIFRA en ROJO DESPUES: %d" % len(en_rojo2))
    for n in en_rojo2:
        w("      %s" % n)
    w("")

    w("E) Y CADA FICHERO TOCADO SIGUE COMPILANDO, QUE NO SE DA POR SUPUESTO")
    w("   (se compila EN MEMORIA con `compile(...)` y no con `py_compile`: en")
    w("    Windows `os.devnull` es `nul`, que no es un fichero regular, y")
    w("    `py_compile` cae con FileExistsError sobre codigo perfectamente sano.")
    w("    Es una CORRECCION DECLARADA de este mismo instrumento: su primera")
    w("    corrida saco los doce en NO COMPILA y ninguno estaba roto)")
    malos = []
    for nombre, _p in CAMBIOS:
        ruta = os.path.join(LOOP, nombre)
        if not os.path.isfile(ruta):
            continue
        try:
            fuente = io.open(ruta, encoding="utf-8").read()
            compile(fuente, ruta, "exec")
            w("   %-46s compila" % nombre)
        except Exception as e:
            w("   %-46s NO COMPILA: %r" % (nombre, e))
            malos.append(nombre)
    w("   CIFRA que no compilan: %d" % len(malos))
    w("")

    if rojos or malos or (not a.simular and en_rojo2):
        w("VEREDICTO: ROJO")
        codigo_salida = 1
    else:
        w("VEREDICTO: VERDE")
        codigo_salida = 0
    texto = NL.join(L) + NL
    io.open(os.path.join(RAIZ, SALIDA.replace("/", os.sep)), "w",
            encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)" % (SALIDA, len(texto.encode("utf-8"))))
    return codigo_salida


if __name__ == "__main__":
    sys.exit(main())
