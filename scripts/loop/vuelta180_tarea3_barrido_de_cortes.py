# -*- coding: utf-8 -*-
r"""vuelta180_tarea3_barrido_de_cortes.py . EL BARRIDO: TODA CIFRA DE LOS DOS
INSTRUMENTOS, DICIENDO CUAL SE PUEDE MOVER DENTRO DE UNA VUELTA Y CUAL LLEVA SU
CORTE.

TAREA 3 de la vuelta 180, segunda mitad. SOLO LECTURA: corre los dos
instrumentos, lee sus salidas y no escribe nada mas que su propio informe.

LOS DOS INSTRUMENTOS BARRIDOS son `scripts/loop/backlog_l03_resuelto.py` y
`scripts/loop/vuelta179_tarea2_cobertura_final.py`, que son los dos que el
encargo nombra.

QUE ES "QUE SE PUEDE MOVER DENTRO DE UNA VUELTA", DICHO ANTES DE CLASIFICAR NADA
para que no se pueda elegir despues: una cifra SE MUEVE si depende de un fichero
que **la propia campana escribe mientras la vuelta corre**
(`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `docs/plan/OP_L_03_LECTURAS.jsonl`,
`dataset/`). NO se mueve si sale del corte sellado en la vuelta 15, que es de
donde el instrumento viejo saca sus actos y sus pares.

**Y AQUI VA LA DECLARACION QUE `EJECUTOR.md` 1 EXIGE, con su letra del 29 ago:
LA COLUMNA "SE MUEVE" ES UNA CLASIFICACION A MANO Y NO UNA MEDICION.** No hay
manera de medir dentro de una sola corrida si una cifra se movera en la
siguiente, asi que **NO HAY CASO ROJO AUTOMATICO PARA ESA COLUMNA**, y se dice en
vez de fabricar uno que se apruebe solo. Cada fila lleva escrito de que fichero
depende, que es el dato del que sale la clasificacion y se puede discutir.

LO QUE SI ES MECANICO Y SI PUEDE CAER EN ROJO, y son cuatro cosas:

  1. **CADA CIFRA DECLARADA APARECE HOY EN LA SALIDA.** Si un instrumento deja de
     publicar una cifra que esta tabla nombra, la tabla estaria describiendo algo
     que ya no existe, y eso es ROJO.
  2. **CADA CIFRA DECLARADA COMO QUE SE MUEVE LLEVA SU CORTE PEGADO EN LA MISMA
     LINEA.** Es la comprobacion que esta tarea vino a poner.
  3. **CADA CIFRA DECLARADA COMO QUE NO SE MUEVE LO DICE EN SU LINEA**, en vez de
     callarlo. Una cifra sin corte y sin explicacion es indistinguible de una
     cifra a la que se le olvido el corte.
  4. **NINGUNA CIFRA DE LA SALIDA SE ESCAPA DE LA TABLA.** Se recogen todas las
     lineas que publican una cifra y se comprueba que cada una la cubre alguna
     fila declarada. Sin esto, la tabla podria quedarse corta en silencio.

USO:
  python scripts/loop/vuelta180_tarea3_barrido_de_cortes.py
"""
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
NL = chr(10)

SE_MUEVE = "SE MUEVE"
NO_SE_MUEVE = "NO SE MUEVE"

# LA TABLA DECLARADA. Cada fila: (instrumento, aguja que la localiza en la
# salida, si se mueve, de que fichero depende). LA AGUJA ES UN TROZO LITERAL DE
# LA LINEA, para que la tabla no pueda hablar de una cifra que ya no se imprime.
DECLARADAS = [
    # --------------------------------------------- backlog_l03_resuelto.py
    ("backlog_l03_resuelto.py", "CIFRA actos que su LISTA DECLARADA trae",
     NO_SE_MUEVE, "la salida del instrumento viejo, corte sellado en la vuelta 15"),
    ("backlog_l03_resuelto.py", "CIFRA pares que el instrumento da, sumados de su lista",
     NO_SE_MUEVE, "la salida del instrumento viejo, corte sellado en la vuelta 15"),
    ("backlog_l03_resuelto.py", "CIFRA ficheros de dataset/nodos/ leidos",
     SE_MUEVE, "dataset/nodos/"),
    ("backlog_l03_resuelto.py", "CIFRA alias del mapa",
     SE_MUEVE, "dataset/nodos/"),
    ("backlog_l03_resuelto.py", "CIFRA nodos del grafo",
     SE_MUEVE, "dataset/metadata/master_graph.json"),
    ("backlog_l03_resuelto.py", "CIFRA nodos VIVOS (deprecado falso)",
     SE_MUEVE, "dataset/metadata/master_graph.json"),
    ("backlog_l03_resuelto.py", "CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
     SE_MUEVE, "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"),
    ("backlog_l03_resuelto.py", "CIFRA pares distintos tras resolver",
     SE_MUEVE, "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"),
    ("backlog_l03_resuelto.py", "CIFRA actos medidos",
     NO_SE_MUEVE, "la salida del instrumento viejo, corte sellado en la vuelta 15"),
    ("backlog_l03_resuelto.py", "CIFRA actos donde los dos caminos CALZAN",
     SE_MUEVE, "dataset/ contra el resolutor"),
    ("backlog_l03_resuelto.py", "CIFRA actos donde NO calzan",
     SE_MUEVE, "dataset/ contra el resolutor"),
    ("backlog_l03_resuelto.py", "| actos que el instrumento da |",
     NO_SE_MUEVE, "la salida del instrumento viejo, corte sellado en la vuelta 15"),
    ("backlog_l03_resuelto.py", "| pares POSIBLES entre los miembros escritos |",
     NO_SE_MUEVE, "la salida del instrumento viejo, corte sellado en la vuelta 15"),
    ("backlog_l03_resuelto.py", "| PARES QUE EL INSTRUMENTO DA",
     NO_SE_MUEVE, "la salida del instrumento viejo, corte sellado en la vuelta 15"),
    ("backlog_l03_resuelto.py", "| pares DISUELTOS",
     SE_MUEVE, "dataset/nodos/, por el resolutor"),
    ("backlog_l03_resuelto.py", "| pares que YA TIENEN VEREDICTO",
     SE_MUEVE, "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"),
    ("backlog_l03_resuelto.py", "| PARES REALES",
     SE_MUEVE, "docs/INTRA_DOMINIO_VEREDICTOS.jsonl y dataset/"),
    ("backlog_l03_resuelto.py", "| actos SIN NINGUN PAR REAL |",
     SE_MUEVE, "docs/INTRA_DOMINIO_VEREDICTOS.jsonl y dataset/"),
    ("backlog_l03_resuelto.py", "CIFRA actos que el registro dice leidos",
     SE_MUEVE, "docs/plan/OP_L_03_LECTURAS.jsonl"),
    ("backlog_l03_resuelto.py", "CIFRA de esos que el instrumento sigue dando",
     SE_MUEVE, "docs/plan/OP_L_03_LECTURAS.jsonl"),
    ("backlog_l03_resuelto.py", "| YA LEIDOS (la 177) |",
     SE_MUEVE, "docs/plan/OP_L_03_LECTURAS.jsonl, LA FILA QUE SE MOVIO EN LA 179"),
    ("backlog_l03_resuelto.py", "| SIN LEER |",
     SE_MUEVE, "docs/plan/OP_L_03_LECTURAS.jsonl, LA FILA QUE SE MOVIO EN LA 179"),
    ("backlog_l03_resuelto.py", "| **todos** |",
     SE_MUEVE, "docs/INTRA_DOMINIO_VEREDICTOS.jsonl y dataset/"),
    # ------------------------------------ vuelta179_tarea2_cobertura_final.py
    ("vuelta179_tarea2_cobertura_final.py",
     "CIFRA ficheros de dataset/nodos/ leidos por el resolutor",
     SE_MUEVE, "dataset/nodos/"),
    ("vuelta179_tarea2_cobertura_final.py", "CIFRA actos que el instrumento da",
     NO_SE_MUEVE, "la salida del instrumento viejo, corte sellado en la vuelta 15"),
    ("vuelta179_tarea2_cobertura_final.py",
     "CIFRA filas de docs/plan/OP_L_03_LECTURAS.jsonl",
     SE_MUEVE, "docs/plan/OP_L_03_LECTURAS.jsonl"),
    ("vuelta179_tarea2_cobertura_final.py", "CIFRA de esas filas escritas por la vuelta",
     SE_MUEVE, "docs/plan/OP_L_03_LECTURAS.jsonl"),
    ("vuelta179_tarea2_cobertura_final.py", "CIFRA pares con clase escrita por la vuelta",
     SE_MUEVE, "docs/plan/OP_L_03_LECTURAS.jsonl"),
    ("vuelta179_tarea2_cobertura_final.py",
     "CIFRA pares distintos con clase escrita, en total",
     SE_MUEVE, "docs/plan/OP_L_03_LECTURAS.jsonl"),
    ("vuelta179_tarea2_cobertura_final.py", "CIFRA pares reales en todo el backlog",
     SE_MUEVE, "docs/INTRA_DOMINIO_VEREDICTOS.jsonl y dataset/"),
    ("vuelta179_tarea2_cobertura_final.py", "CIFRA de esos CON lectura escrita en su acto",
     SE_MUEVE, "docs/plan/OP_L_03_LECTURAS.jsonl"),
    ("vuelta179_tarea2_cobertura_final.py", "CIFRA de esos SIN lectura",
     SE_MUEVE, "docs/plan/OP_L_03_LECTURAS.jsonl"),
]

# LAS LINEAS QUE PUBLICAN UNA CIFRA. Son las que empiezan por CIFRA y las filas
# de tabla con un numero en negrita. Todo lo demas es prosa.
PATRON_CIFRA = re.compile(r"^\s*CIFRA\b")
PATRON_FILA = re.compile(r"^\s*\|.*\*\*\d")

# LAS LINEAS QUE PUBLICAN UNA CIFRA Y NO SON DE NADIE: cabeceras de tabla y
# lineas de detalle por acto, que no son cifras agregadas sino su desglose.
EXENTAS = (
    "| acto (primer miembro) |",
    "|---",
    "LA MISMA TABLA, CON EL SELLO ENTERO",
    "LA RESTA:",
    "LO QUE SOBRA, EN CRUDO",
)


def correr(nombre):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, os.path.join(AQUI, nombre)],
                       cwd=RAIZ, capture_output=True, env=env)
    return r.returncode, (r.stdout.decode("utf-8", errors="replace")
                          + r.stderr.decode("utf-8", errors="replace"))


def lineas_de_cifra(salida):
    """LAS LINEAS QUE PUBLICAN UNA CIFRA AGREGADA. PURA."""
    fuera = []
    for l in salida.split(NL):
        if not (PATRON_CIFRA.match(l) or PATRON_FILA.match(l)):
            continue
        if any(e in l for e in EXENTAS):
            continue
        if re.match(r"^\s*\|\s*`", l):     # detalle por acto: empieza por un id
            continue
        fuera.append(l.rstrip())
    return fuera


def lleva_corte(linea):
    """SI ESA LINEA TRAE SU CORTE PEGADO. PURA."""
    return "corte:" in linea or "HEAD " in linea


def dice_que_no_se_mueve(linea):
    """SI ESA LINEA DICE, EN SU PROPIO TEXTO, QUE NO SE MUEVE. PURA."""
    return ("NO se mueve" in linea or "no, sale del" in linea
            or "no, sale de la" in linea)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    p("=" * 78)
    p("EL BARRIDO DE CORTES DE LOS DOS INSTRUMENTOS (vuelta 180, TAREA 3)")
    p("=" * 78)
    p("")

    salidas, fallos = {}, []
    for nombre in sorted({i for i, _a, _m, _d in DECLARADAS}):
        codigo, salida = correr(nombre)
        salidas[nombre] = salida
        p("   corrido: %-44s exit %d, %d lineas"
          % (nombre, codigo, salida.count(NL)))
        if codigo != 0:
            fallos.append("%s sale con exit %d" % (nombre, codigo))
    p("")

    p("A) LA TABLA DEL BARRIDO, FILA A FILA")
    p("")
    p("| instrumento | cifra | se mueve dentro de una vuelta | de que depende | lleva su corte |")
    p("|---|---|---|---|---|")
    cubiertas = set()
    for instrumento, aguja, mueve, depende in DECLARADAS:
        hits = [l for l in lineas_de_cifra(salidas[instrumento]) if aguja in l]
        for h in hits:
            cubiertas.add((instrumento, h))
        if not hits:
            estado = "**NO APARECE HOY**"
            fallos.append("%s: la cifra %r ya no se publica" % (instrumento, aguja))
        elif mueve == SE_MUEVE:
            todas = all(lleva_corte(h) for h in hits)
            estado = "**SI**" if todas else "**NO, Y DEBERIA**"
            if not todas:
                fallos.append("%s: la cifra %r SE MUEVE y NO lleva su corte"
                              % (instrumento, aguja))
        else:
            todas = all(dice_que_no_se_mueve(h) or lleva_corte(h) for h in hits)
            estado = "no le hace falta, y lo dice" if todas else "**NO LO DICE**"
            if not todas:
                fallos.append("%s: la cifra %r NO se mueve y no lo dice en su linea"
                              % (instrumento, aguja))
        p("| `%s` | %s | %s | `%s` | %s |"
          % (instrumento, aguja[:56], mueve, depende, estado))
    p("")

    p("B) NINGUNA CIFRA SE ESCAPA DE LA TABLA, COMPROBADO Y NO PROMETIDO")
    total_lineas = 0
    for instrumento in sorted(salidas):
        todas = lineas_de_cifra(salidas[instrumento])
        total_lineas += len(todas)
        sueltas = [l for l in todas if (instrumento, l) not in cubiertas]
        p("   %-44s CIFRA lineas de cifra: %d | sin cubrir: %d"
          % (instrumento, len(todas), len(sueltas)))
        for l in sueltas:
            p("      SIN CUBRIR: %s" % l.strip()[:150])
            fallos.append("%s: linea de cifra sin cubrir: %s"
                          % (instrumento, l.strip()[:90]))
    p("")

    p("C) EL RECUENTO")
    n_mueven = sum(1 for _i, _a, m, _d in DECLARADAS if m == SE_MUEVE)
    p("   CIFRA filas declaradas: %d" % len(DECLARADAS))
    p("   CIFRA de esas que SE MUEVEN dentro de una vuelta: %d" % n_mueven)
    p("   CIFRA de esas que NO se mueven: %d" % (len(DECLARADAS) - n_mueven))
    p("   CIFRA lineas de cifra en las dos salidas: %d" % total_lineas)
    p("   CIFRA fallos: %d" % len(fallos))
    p("")
    p("   Y SE REPITE LA DECLARACION, QUE NO ES UN ADORNO: la columna")
    p("   'se mueve dentro de una vuelta' es UNA CLASIFICACION A MANO. NO HAY")
    p("   CASO ROJO AUTOMATICO PARA ESA COLUMNA y no se fabrica uno que se")
    p("   apruebe solo. Lo que si es mecanico son las cuatro comprobaciones de")
    p("   arriba, y esas si caen.")
    p("")

    if fallos:
        p("ROJO: %d fallo(s)." % len(fallos))
        for f in fallos:
            p("   " + f)
        p("FIN")
        return 1
    p("VERDE: las %d cifras declaradas se publican hoy, las %d que se mueven "
      "llevan su corte pegado en la misma linea, las %d que no se mueven lo dicen "
      "en su propia linea, y ninguna de las %d lineas de cifra de las dos salidas "
      "se queda fuera de la tabla."
      % (len(DECLARADAS), n_mueven, len(DECLARADAS) - n_mueven, total_lineas))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
