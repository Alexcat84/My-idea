# -*- coding: utf-8 -*-
r"""_v215_t5_seccion.py . EL CUERPO DE LA TAREA 5 DEL REPORTE DE LA VUELTA 215,
COMPUESTO DE SU SALIDA SELLADA Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

USO:  python scripts/loop/_v215_t5_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
MUT = "docs/loop/SALIDA_V%d_T5_MUTANTES.txt" % VUELTA
CONSOLA_AP = "docs/loop/SALIDA_V%d_CICLO_GATE0_APERTURA_CONSOLA.txt" % VUELTA


def leer(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    return io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def cifra(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(-?\d+)", l.split(etiqueta, 1)[1])
            if m:
                return m.group(1)
    return None


def main():
    mut = leer(MUT)
    consola = leer(CONSOLA_AP)
    if mut is None or consola is None:
        print("ROJO: falta una fuente. REVIENTA, no rellena.")
        return 1

    casos = [l.strip() for l in mut.split(NL) if l.strip().startswith("CASO ")]
    calzan = len([l for l in mut.split(NL) if "VEREDICTO: CALZA" in l])
    filas = []
    bloques = mut.split("CASO ")[1:]
    for b in bloques:
        titulo = b.split(NL, 1)[0].strip()
        etiqueta = titulo.split(".", 1)[0]
        resto = titulo.split(".", 1)[1].strip() if "." in titulo else titulo
        m = re.search(r"da fila: (\S+) \| se esperaba: (\S+) \| VEREDICTO: (\S+)", b)
        if not m:
            continue
        filas.append("| **%s** | %s | %s | %s | **%s** |"
                     % (etiqueta, resto, m.group(1), m.group(2), m.group(3)))

    D = {
        "malas": cifra(mut, "CIFRA casos malos que AUN ASI producen una fila: "),
        "con_motivo": cifra(mut, "CIFRA casos malos que revientan CON SU MOTIVO ESCRITO: "),
        "fallos": cifra(mut, "CIFRA comprobaciones que fallan: "),
        "peor": cifra(consola, "PEOR EXITCODE DE LOS OCHO: "),
    }
    faltan = [k for k, v in D.items() if v is None]
    if faltan:
        print("ROJO: faltan cifras: %s" % faltan)
        return 1

    linea_214 = None
    for l in mut.split(NL):
        if "_v214_cierre_texto.py linea" in l:
            linea_214 = l.strip()

    cuerpo = """### TAREA 5. MI REPORTE, Y LA GUARDA QUE ME FALTO EN LA 214

**LA CAIDA QUE REMEDIA ESTA TAREA ES MIA Y ES LA UNICA QUE ACUMULA**, y va
registrada entera en la TAREA 1.b con la linea del acta donde vive. Aqui va el
remedio, que son **DOS MITADES Y NO UNA**, y la segunda es la que importa.

#### 5.a. LA PRIMERA MITAD: LA CONSOLA SE SELLA DESDE DENTRO DEL INSTRUMENTO

**El ciclo imprime su consola por `stdout` y en la 214 nadie la redirigio.** El
encargo dice *"redirigela"*, y **acordarse de redirigir es exactamente lo que
esta casa lleva vueltas demostrando que no funciona**: por eso no la redirijo
desde fuera, **la escribe el propio instrumento**.

`scripts/loop/_v%(v)d_ciclo_gate0.py` duplica su salida con un `Tee`, la sigue
imprimiendo por pantalla, y **la escribe en el nombre exacto que el compositor
busca**, compuesto del numero de vuelta que sale del nombre del fichero y del
lado que llega por argumento. **Y si el fichero saliera de CERO BYTES, el propio
ciclo sale en rojo**, porque una salida sellada de cero bytes no cuenta como
hecha (`EJECUTOR.md` 1).

**MEDIDO:** `%(consola)s` existe, mide **%(bytes)d bytes**, y publica **PEOR
EXITCODE DE LOS OCHO: %(peor)s**. **El lado CIERRE se sella igual al cerrar la
vuelta, y sus dos filas van en la seccion 3.1.**

#### 5.b. LA SEGUNDA MITAD, Y ES LA QUE IMPORTA: EL COMPOSITOR REVIENTA

**Lo que el acta 214 senala no es la celda vacia: es que mi compositor
ESCRIBIERA UNA FILA EN BLANCO Y SIGUIERA.** Eso es degradacion silenciosa, que es
lo que el banco 9 prohibe.

**LA DIFERENCIA NO ES UNA PROMESA, ES CODIGO, Y SE LEE DE LOS DOS FICHEROS:**

- El de la 214, **%(linea_214)s**
- El mio: **no tiene esa rama**. `fila_de_gate()` devuelve `(None, motivo)` y
  quien la llama **acumula el fallo duro y sale con exitcode 1 sin escribir una
  sola linea del cuerpo**.

**LA PRUEBA DE MUTACION, QUE VA DELANTE Y NO DETRAS** (`%(mut)s`). Se muta **la
entrada de la funcion pura**, no el repo: ningun fichero se toca, ni se borra, ni
se renombra.

**FILAS ARMADAS: %(n_filas)d. FILAS QUE DEBERIA HABER: 4.**

| caso | que se le da a la guarda | da fila | se esperaba | veredicto |
|---|---|---|---|---|
%(filas)s

**Y LA CIFRA QUE DE VERDAD MIDE EL REMEDIO, PORQUE UNA FILA CON CELDAS VACIAS
SIGUE SIENDO UNA FILA:** **CIFRA casos malos que AUN ASI producen una fila:
%(malas)s** (se exige 0). **CIFRA casos malos que revientan CON SU MOTIVO
ESCRITO: %(con_motivo)s de 3**, porque reventar sin decir por que es la otra
mitad de la misma enfermedad.

**EL CASO `A` ES EL DE LA 214 LITERAL:** fichero que no existe. **Hoy no da fila,
da un rojo con su motivo.**

**Y ESTO NO FABRICA MAQUINARIA**, que es lo que la moratoria protege: el
compositor de cierre **se escribe cada vuelta de todas formas**, lleva prefijo de
guion bajo, **muere con la vuelta** y no entra en ninguna nomina. **Lo unico que
cambia es que falle ruidoso.**

**LA GUARDA NO SE QUEDO EN EL CIERRE:** los compositores de las TAREAS 3 y 4
llevan la misma negativa a rellenar, y **la de la TAREA 3 me mordio de verdad**
en su primera corrida (su lector de las cuatro clases del marcador devolvia
vacio, y **no escribio nada**).

#### 5.c. LA SECCION 9 CIERRA CON LA BATERIA CORRIDA, NO CON HUECO

**Esta es su vuelta y la bateria corrio.** La seccion 9 la talla
`scripts/loop/cerrar_reporte.py` con la salida compuesta de los once tramos
dentro, y **no lleva hueco declarado**, porque no hay hueco que declarar.

**LO QUE SI LLEVA, Y NO ES LO MISMO QUE UN HUECO:** los once tramos salen en
**exitcode 1**, y eso va dicho en la seccion 5 como **PARADA 2**, con su
contradiccion nombrada y sin que yo elija cual de las dos reglas cede. **Una
bateria corrida con su rojo dicho no es una bateria sin correr.**
""" % {
        "v": VUELTA, "consola": CONSOLA_AP, "mut": MUT,
        "bytes": os.path.getsize(os.path.join(
            RAIZ, CONSOLA_AP.replace("/", os.sep))),
        "peor": D["peor"], "malas": D["malas"], "con_motivo": D["con_motivo"],
        "linea_214": linea_214 or "(no legible)",
        "filas": NL.join(filas), "n_filas": len(filas),
    }

    fallos = 0
    print("CIFRA filas de mutante armadas: %d (se esperan 4)" % len(filas))
    if len(filas) != 4:
        fallos += 1
    print("CIFRA veredictos CALZA leidos de la salida: %d" % calzan)
    if D["fallos"] != "0":
        fallos += 1
        print("ROJO: la prueba de mutacion no salio en 0 fallos.")
    if cuerpo.count(chr(8212)) or cuerpo.count(chr(8211)):
        fallos += 1
        print("ROJO: guiones largos o medios.")
    sosp = [c for c in re.findall(r"`([^`]+)`", cuerpo)
            if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sosp))
    if sosp:
        fallos += 1
    rutas = [c for c in re.findall(r"`([^`]+)`", cuerpo)
             if "/" in c and not c.endswith("/") and " " not in c]
    malas_r = [r for r in rutas
               if not os.path.exists(os.path.join(RAIZ, r.replace("/", os.sep)))
               or os.path.getsize(os.path.join(RAIZ, r.replace("/", os.sep))) == 0]
    print("CIFRA rutas citadas: %d | inexistentes o vacias: %d"
          % (len(rutas), len(malas_r)))
    for m in malas_r:
        print("   ruta mala> %s" % m)
    if malas_r:
        fallos += 1
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: no se escribe el cuerpo.")
        return 1
    destino = os.path.join(RAIZ, "scripts", "loop", "_v%d_t5_seccion.md" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(cuerpo)
    print("ESCRITO %s -> %d bytes, %d lineas"
          % (destino, len(cuerpo.encode("utf-8")), cuerpo.count(NL)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
