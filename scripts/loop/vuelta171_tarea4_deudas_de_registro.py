# -*- coding: utf-8 -*-
r"""vuelta171_tarea4_deudas_de_registro.py . TAREA 4 DE LA VUELTA 171
(adjudicaciones 6.4 y 6.11 del acta 170).

4.a EL AGUJERO DEL `R.38`, POR EL CARRIL DEL BANCO `9.10`. La entrada `R.38` de
`docs/PENDIENTES.md`, escrita por la vuelta 169, afirma que *"el arnes hermano
lo prueba por mutacion en vez de afirmarlo"*, y ese arnes NO EXISTE: la vuelta
169 no escribio el suyo. La frase vieja QUEDA ENTERA Y TACHADA y debajo va la
correccion fechada con su medicion pegada. Ni una palabra se borra.

  QUE SE TACHA Y QUE NO, Y SE DICE PORQUE IMPORTA: la oracion de la que forma
  parte empieza diciendo *"Lo que lo impide es el espacio final del patron"*, y
  ESO ES CIERTO y sigue siendolo. Lo falso es la clausula que viene detras. Se
  tacha la clausula falsa ENTERA y se deja la parte cierta en pie: tachar
  tambien lo cierto seria enterrar una afirmacion buena para tapar una mala.

4.b EL `81` DE `docs/plan/00_INDICE.md`, POR EL CARRIL DEL BANCO `9.21`. La
celda publica 81 lecturas dirigidas hechas con corte 19 ago 2026 y el mismo
instrumento mide otra cosa hoy. NO ES UNA MENTIRA: lleva su corte escrito. Se le
adosa la cifra de hoy POR ADICION, sin tocar una letra de lo viejo.

  Y VA DESPUES DE LA TAREA 2, como el encargo manda, porque el contador es el
  mismo instrumento que la TAREA 2 limpia. La TAREA 2 movio los cinco borradores
  y dejo una PARADA declarada, pero esa parada afecta al UNIVERSO (el mayor
  nombrado), NO a las HECHAS: las hechas dan la misma cifra en los cuatro cortes
  medidos hoy, y esta celda habla de las hechas.

  LO QUE NO SE TOCA Y SE DICE POR QUE: la fila de al lado, *"lecturas dirigidas
  encargadas y sin hacer"*, publica CERO con su corte y hoy el barrido halla
  otra cosa. ESA CIFRA DE HOY ESTA CONTAMINADA por las dos fuentes que la TAREA
  2 midio, asi que adosarla seria meter una cifra envenenada en una pagina del
  plan. Se declara en el reporte y no se escribe.

NINGUNA CIFRA SE TECLEA: la nomina de arneses sale de un barrido de
`scripts/loop/`, la cifra de hechas sale de correr el contador en esta vuelta, y
la fecha sale del reloj del sistema.

USO:  python scripts/loop/vuelta171_tarea4_deudas_de_registro.py
"""
import datetime
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PENDIENTES = os.path.join(RAIZ, "docs", "PENDIENTES.md")
INDICE = os.path.join(RAIZ, "docs", "plan", "00_INDICE.md")
CONTADOR = os.path.join("scripts", "loop", "vuelta48_contar_ld.py")

MESES = {1: "ene", 2: "feb", 3: "mar", 4: "abr", 5: "may", 6: "jun", 7: "jul",
         8: "ago", 9: "sep", 10: "oct", 11: "nov", 12: "dic"}

FALSA = ("y el arnes hermano lo\nprueba por mutacion en vez de afirmarlo.")
ANCLA_INDICE = "| lecturas dirigidas **hechas** | **65** |"


def hoy():
    d = datetime.datetime.now()
    return "%d %s %d" % (d.day, MESES[d.month], d.year)


def main():
    print("=" * 78)
    print("VUELTA 171, TAREA 4: LAS DOS DEUDAS DE REGISTRO")
    print("=" * 78)
    print("")
    fecha = hoy()
    print("   fecha de corte de todo lo que esta vuelta escribe aqui, leida del")
    print("   reloj del sistema y no tecleada: %s" % fecha)
    print("")
    rojos = []

    # ------------------------------------------------------------------- 4.a
    print("A) 4.a EL AGUJERO DEL R.38, MEDIDO ANTES DE ESCRIBIR")
    texto = io.open(PENDIENTES, encoding="utf-8").read().replace("\r\n", "\n")
    lineas = texto.split("\n")
    ini = [i for i, l in enumerate(lineas, 1) if l.startswith("## R.38.")]
    if len(ini) != 1:
        print("   PARADA: la cabecera de R.38 aparece %d veces." % len(ini))
        return 1
    sig = [i for i, l in enumerate(lineas, 1)
           if i > ini[0] and re.match(r"^## R\.\d+\.", l)]
    fin = min(sig) - 1 if sig else len(lineas)
    print("   R.38 acotado: docs/PENDIENTES.md, lineas %d a %d" % (ini[0], fin))
    cuerpo = "\n".join(lineas[ini[0] - 1:fin])
    print("   CIFRA veces que la clausula falsa aparece DENTRO de R.38: %d"
          % cuerpo.count(FALSA))
    print("   CIFRA veces que aparece en el fichero ENTERO: %d" % texto.count(FALSA))
    if cuerpo.count(FALSA) != 1:
        rojos.append("la clausula falsa no aparece exactamente una vez dentro de R.38")
    if texto.count(FALSA) != 1:
        rojos.append("la clausula falsa aparece %d veces en el fichero entero: "
                     "no se toca a ciegas" % texto.count(FALSA))

    print("   LA MEDICION QUE SOSTIENE LA CORRECCION, corrida en esta vuelta:")
    arneses = sorted(f for f in os.listdir(os.path.join(RAIZ, "scripts", "loop"))
                     if "mutacion_registro" in f)
    vueltas = []
    for f in arneses:
        m = re.match(r"vuelta(\d+)_", f)
        if m:
            vueltas.append(int(m.group(1)))
    print("      ls scripts/loop/ | grep mutacion_registro -> %d ficheros" % len(arneses))
    for f in arneses:
        print("         %s" % f)
    print("      vueltas representadas: %s" % ", ".join(str(v) for v in vueltas))
    print("      ¿existe el de la vuelta 169?: %s" % ("SI" if 169 in vueltas else "NO"))
    if 169 in vueltas:
        rojos.append("el arnes de la 169 SI existe: la correccion de esta tarea "
                     "estaria de mas y no se escribe")
    print("")

    # ------------------------------------------------------------------- 4.b
    print("B) 4.b LA CELDA DEL 00_INDICE, MEDIDA ANTES DE ESCRIBIR")
    indice = io.open(INDICE, encoding="utf-8").read().replace("\r\n", "\n")
    filas = [(i, l) for i, l in enumerate(indice.split("\n"), 1)
             if l.startswith(ANCLA_INDICE)]
    print("   CIFRA filas que empiezan por el ancla de la celda: %d" % len(filas))
    if len(filas) != 1:
        rojos.append("la fila de 'lecturas dirigidas hechas' no aparece una sola vez")
        n_fila, fila = 0, ""
    else:
        n_fila, fila = filas[0]
        print("   docs/plan/00_INDICE.md:%d" % n_fila)
        m81 = re.search(r"exit 0\): (\d+)\*\*", fila)
        print("   la cifra vieja que la celda publica: %s" % (m81.group(1) if m81 else "(no legible)"))
        print("   el corte que la celda declara: %s"
              % ("19 ago 2026" if "19 ago 2026" in fila else "(no legible)"))
        if not m81 or "19 ago 2026" not in fila:
            rojos.append("la celda no trae la cifra vieja o su corte de forma legible")

    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, CONTADOR], cwd=RAIZ, capture_output=True, env=env)
    sal = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    io.open(os.path.join(RAIZ, "docs", "loop", "SALIDA_V171_T4B_CONTAR_LD.txt"),
            "w", encoding="utf-8", newline="\n").write(sal)
    mh = re.search(r"HECHAS \(ids distintos con seccion propia\):\s*(\d+)", sal)
    ms = re.search(r"numeros nombrados sin seccion propia:\s*(\d+)", sal)
    print("   el contador, corrido en esta vuelta (exit %d):" % r.returncode)
    print("      lecturas dirigidas HECHAS hoy: %s" % (mh.group(1) if mh else "(no legible)"))
    print("      nombradas sin seccion hoy:     %s (CONTAMINADA, ver TAREA 2)"
          % (ms.group(1) if ms else "(no legible)"))
    if not mh or r.returncode != 0:
        rojos.append("el contador no da una cifra de hechas legible o no sale en 0")
    print("")

    if rojos:
        print("ROJO, %d motivo(s), y NO se escribe nada:" % len(rojos))
        for x in rojos:
            print("   " + x)
        return 1

    hechas_hoy = int(mh.group(1))
    vieja = int(m81.group(1))

    # ---------------------------------------------------------------- ESCRIBE
    print("C) SE ESCRIBE 4.a")
    correccion = (
        "~~" + FALSA + "~~\n\n"
        "**CORRECCION DECLARADA (vuelta 171, TAREA 4.a, %s), POR EL CARRIL DEL BANCO\n"
        "`9.10` Y SIN BORRAR LA FRASE DE ARRIBA, que se queda entera y tachada porque\n"
        "una correccion que tapa lo que corrige no se puede auditar.** La primera mitad\n"
        "de esa oracion es CIERTA y se deja en pie: lo que impide que `6.1` se coma a\n"
        "`6.10` es, en efecto, el espacio final del patron. **LO FALSO ES LA CLAUSULA\n"
        "TACHADA: cuando esta entrada se escribio, EL ARNES HERMANO NO EXISTIA.** La\n"
        "vuelta 169 escribio su registrador (`vuelta169_tarea1_registrar_acta168.py`)\n"
        "**sin `prueba_de_mutacion`**, asi que no habia nada que la bateria pudiera\n"
        "correr y la afirmacion no tenia respaldo.\n\n"
        "**LA MEDICION, CORRIDA EN LA VUELTA 171 Y PEGADA AQUI**\n"
        "(`ls scripts/loop/ | grep mutacion_registro`, %d ficheros): existen los de las\n"
        "vueltas %s. **NO EXISTE NINGUNO DE LA VUELTA 169**, y el hueco entre el 168 y\n"
        "el 170 se ve a simple vista en la propia nomina.\n\n"
        "**QUIEN LO TRAJO Y QUIEN LO CORRIGE, PORQUE LAS DOS COSAS CUENTAN:** lo hallo\n"
        "el ejecutor de la vuelta 170 y lo trajo como su discutible `D.8` **sin\n"
        "corregirlo**, con el argumento de que no era suyo; la adjudicacion `6.4` del\n"
        "acta 170 dice que *\"no es mio y el encargo no me manda tocarlo\" no vale para\n"
        "una afirmacion falsa en la serie de registros*, porque **la serie es una sola y\n"
        "la lee todo el que venga detras**. Traerlo estuvo bien; dejarlo, no.\n\n"
        "**Y LO QUE ESTA CORRECCION NO HACE:** no toca el `R.39` ni el `R.40`, que usan\n"
        "la misma frase y en los que **si** es cierta (`vuelta170_tarea1a_mutacion_"
        "registro.py` y `vuelta171_tarea1a_mutacion_registro.py` existen y salen en\n"
        "verde); y no mueve ninguna cifra de ninguna otra entrada de la serie.\n"
        % (fecha, len(arneses), ", ".join(str(v) for v in vueltas)))
    texto2 = texto.replace(FALSA, correccion, 1)
    io.open(PENDIENTES, "w", encoding="utf-8", newline="\n").write(texto2)
    print("   escrito en docs/PENDIENTES.md: %d bytes -> %d bytes"
          % (len(texto.encode("utf-8")), len(texto2.encode("utf-8"))))
    print("")

    print("D) SE ESCRIBE 4.b")
    adosado = (
        " **Y LA CIFRA DE HOY, ADOSADA POR `9.21` EN LA VUELTA 171 (%s) Y SIN TOCAR "
        "UNA LETRA DE LO VIEJO: %d.** Misma vara y MISMO INSTRUMENTO, "
        "`scripts/loop/vuelta48_contar_ld.py`, corrido en esa vuelta "
        "([`../loop/SALIDA_V171_T4B_CONTAR_LD.txt`](../loop/SALIDA_V171_T4B_CONTAR_LD.txt), "
        "exit 0). **El %d no se borra ni se corrige: era exacto a su corte del 19 ago "
        "2026**, y la diferencia con el de hoy es de **%d** lectura, escrita entre las "
        "dos fechas. **Y la fila de abajo NO recibe la cifra de hoy, y se dice por que:** "
        "su barrido esta contaminado por dos ficheros que la TAREA 2 de la vuelta 171 "
        "midio y nombro, asi que su cifra de hoy no se publica en una pagina del plan "
        "hasta que eso se resuelva. |"
        % (fecha, hechas_hoy, vieja, hechas_hoy - vieja))
    nueva_fila = fila.rstrip()
    if not nueva_fila.endswith("|"):
        print("   PARADA: la fila no termina en barra vertical.")
        return 1
    nueva_fila = nueva_fila[:-1].rstrip() + adosado
    indice2 = indice.replace(fila, nueva_fila, 1)
    io.open(INDICE, "w", encoding="utf-8", newline="\n").write(indice2)
    print("   escrito en docs/plan/00_INDICE.md:%d" % n_fila)
    print("   %d bytes -> %d bytes"
          % (len(indice.encode("utf-8")), len(indice2.encode("utf-8"))))
    print("")

    # -------------------------------------------------------------- RELECTURA
    print("E) SE RELEE DEL DISCO, QUE ES LA PRIMERA DE LAS DOS COMPROBACIONES")
    p2 = io.open(PENDIENTES, encoding="utf-8").read().replace("\r\n", "\n")
    i2 = io.open(INDICE, encoding="utf-8").read().replace("\r\n", "\n")
    casos = [
        ("la frase falsa sigue ENTERA en el fichero", FALSA in p2, True),
        ("y sigue apareciendo una sola vez", p2.count(FALSA), 1),
        ("y ahora esta TACHADA", ("~~" + FALSA + "~~") in p2, True),
        ("la correccion lleva su fecha", ("vuelta 171, TAREA 4.a, %s" % fecha) in p2, True),
        ("la correccion dice que el arnes de la 169 no existe",
         "NO EXISTE NINGUNO DE LA VUELTA 169" in p2, True),
        ("la nomina de arneses esta pegada", "%d ficheros" % len(arneses) in p2, True),
        ("la cifra vieja del indice sigue entera", "exit 0): %d**" % vieja in i2, True),
        ("y ahora lleva la de hoy al lado", "SIN TOCAR UNA LETRA DE LO VIEJO: %d.**"
         % hechas_hoy in i2, True),
        ("la fila de encargadas sin hacer NO se toco",
         i2.count("misma corrida: CERO, y la cifra vieja aguanta."), 1),
        ("y no se le colo la cifra contaminada",
         "SIN TOCAR UNA LETRA DE LO VIEJO: %s.**" % (ms.group(1) if ms else "x") in i2,
         False),
    ]
    mal = 0
    for nombre, real, esperado in casos:
        ok = real == esperado
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            mal += 1
    print("   CIFRA comprobaciones: %d | fallan: %d" % (len(casos), mal))
    print("")
    if mal:
        print("ROJO: el fichero escrito no cumple %d de sus propias guardas." % mal)
        return 1
    print("VERDE: las dos deudas quedan pagadas por adicion, sin borrar una letra.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
