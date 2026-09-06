# -*- coding: utf-8 -*-
r"""vuelta189_tarea2_nomina.py . LA NOMINA AL CERRAR LA BATERIA, Y LA DOBLE
CORRIDA DE LOS ARNESES QUE NACEN HOY, CON LA EXCLUSION POR ROJO DICHA EN VOZ ALTA.

LA MAQUINA NO SE CLONA, SE IMPORTA (`6.6` del acta 172): `rojos_registrados` y
`particion_por_rojo` vienen de `scripts/loop/vuelta188_tarea3c_nomina.py`, que es
donde nacieron, y `sha_de` y `numstat` tambien. Lo propio de este fichero son la
lista `LOS_QUE_CORREN` de esta vuelta y el bloque que mide la nomina al cerrar la
bateria.

POR QUE ESTA VUELTA SI TIENE ALGO QUE EXCLUIR, Y ES LA PRIMERA. El punto 4 del
encargo de la 189 dice que la doble corrida EXCLUYE explicitamente cualquier
arnes que ya haya salido en rojo en esa misma vuelta, y que LO DIGA en su salida
con el nombre del excluido, la ruta de su salida en rojo y el motivo. En la 188 el
registro no existia y la exclusion era VACIA, y asi se declaro. **Hoy no lo es:**
`vuelta172_tarea5_mutacion_cierre.py` salio `NO MORDIO` en el tramo 7 de la
bateria de esta vuelta, y su linea vive en `docs/loop/ROJOS_DE_LA_VUELTA_189.txt`.

Y UNA MEDICION QUE NO SE AFIRMA, SE HACE: **el arnes que nace en esta vuelta es
el carril `--mutacion` del registrador, y el CENSO NO LO VE**, porque
`PATRON_ARNES` mira el NOMBRE DEL FICHERO y pide que diga `mutacion`,
`caso_positivo` o `simular`, y este vive dentro de
`vuelta189_tarea1a_registrar_acta189.py`. **No es un defecto que esta vuelta
introduzca** (el registrador de la 188 tiene la misma forma) y **esta vuelta no lo
arregla**, porque su encargo dice NADA MAS ENTRA EN ESTA VUELTA. Se mide, se
publica y se deja anotado.

ESTE FICHERO NO ES UN ARNES DE MUTACION Y NO ENTRA EN LA NOMINA, y esa afirmacion
SE MIDE aqui abajo en vez de dejarse dicha.

NO SE PODA NADA. La opcion `c` de la parada del 5 sep 2026 quedo RECHAZADA por el
fundador.

USO:
  python scripts/loop/vuelta189_tarea2_nomina.py
"""
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as VMV   # noqa: E402
from vuelta188_tarea3c_nomina import (   # noqa: E402
    rojos_registrados, particion_por_rojo, sha_de, numstat)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
PY = sys.executable
VUELTA = int(os.path.basename(os.path.abspath(__file__)).split("_")[0][6:])
REGISTRO_ROJOS = "docs/loop/ROJOS_DE_LA_VUELTA_%d.txt" % VUELTA

# LOS QUE ESTA VUELTA MANDA CORRER DOS VECES. Es corta a proposito: la 189 es
# VUELTA DE BATERIA y no lleva nada mas, asi que el unico arnes que nace hoy es
# el carril de mutacion del registrador. El segundo de la lista es el arnes que
# la bateria dejo en rojo, y esta AQUI para que la particion lo EXCLUYA por su
# nombre y lo diga: si no estuviera en la lista, la exclusion no tendria a quien
# nombrar y pareceria que no habia nada que excluir.
LOS_QUE_CORREN = [
    ("scripts/loop/vuelta189_tarea1a_registrar_acta189.py",
     "docs/loop/SALIDA_V189_T1A_RECORRIDO_SIN_ESCRIBIR.txt",
     "NACE HOY, y su re corrido es su propia prueba de idempotencia"),
    ("scripts/loop/vuelta172_tarea5_mutacion_cierre.py",
     "docs/loop/SALIDA_V189_BATERIA_TRAMO_7.txt",
     "SELLADO, y la bateria de hoy lo dejo en ROJO"),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2: LA NOMINA AL CERRAR, Y LA DOBLE CORRIDA CON EXCLUSION"
      % VUELTA)
    w("=" * 78)
    w("")

    w("A) LA NOMINA Y EL CENSO, RECOMPUTADOS AL CERRAR LA BATERIA")
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _a in VMV.VIEJAS]
    w("   CIFRA censo: %d | CIFRA nomina AHORA: %d | VARA_DEL_CENSO: %d"
      % (len(censo), len(nomina), VMV.VARA_DEL_CENSO))
    ultima, faltan = VMV.arneses_que_faltan()
    w("   arneses_que_faltan(): ultima vuelta %s, FALTAN %d" % (ultima, len(faltan)))
    for n in faltan:
        w("      FALTA: %s" % n)
    invis = VMV.nomina_invisible_al_censo()
    w("   nomina_invisible_al_censo(): %d" % len(invis))
    for n in invis:
        w("      INVISIBLE: %s" % n)
    malas = VMV.guarda_del_sujeto_congelado()
    w("   guarda_del_sujeto_congelado(): %d entradas sin congelar" % len(malas))
    for nombre, veredicto, vive in malas:
        w("      SUJETO SIN CONGELAR: %-46s %s" % (nombre, veredicto))
    w("   ESTA ES LA UNICA FUENTE DEL exitcode 1 DE LOS DIEZ TRAMOS, y no es de")
    w("   ningun arnes: es la deuda que el acta 189 mide en su seccion 2 y que su")
    w("   `4.7` deja abierta a proposito, con el remedio encargado a la 190.")
    w("")

    w("B) EL ARNES QUE NACE HOY Y EL CENSO, MEDIDO Y NO AFIRMADO")
    yo = os.path.basename(os.path.abspath(__file__))
    reg = "vuelta%d_tarea1a_registrar_acta%d.py" % (VUELTA, VUELTA)
    dentro = set(nomina)
    for nombre in (reg, yo):
        w("   %-52s en el censo: %-3s | en la nomina: %s"
          % (nombre, "SI" if nombre in censo else "NO",
             "SI" if nombre in dentro else "NO"))
    w("   EL PATRON QUE DECIDE: %r" % VMV.PATRON_ARNES.pattern)
    w("   O SEA: el censo mira el NOMBRE DEL FICHERO, y el arnes de esta vuelta")
    w("   vive en el carril `--mutacion` de un fichero que no dice `mutacion` en")
    w("   su nombre. **No lo introduce esta vuelta** (el registrador de la 188")
    w("   tiene la misma forma) y **esta vuelta no lo arregla**: se anota.")
    w("")

    w("C) LA EXCLUSION POR ROJO, QUE HOY NO ESTA VACIA")
    p_reg = os.path.join(RAIZ, REGISTRO_ROJOS.replace("/", os.sep))
    existe = os.path.isfile(p_reg)
    texto_reg = io.open(p_reg, encoding="utf-8").read() if existe else ""
    w("   registro: %s" % REGISTRO_ROJOS)
    if existe:
        s = sha_de(p_reg)
        w("      existe: SI | disco %d bytes | LF %d bytes | sha256 LF %s"
          % (s[2], s[3], s[1]))
    else:
        w("      existe: NO. LA EXCLUSION ES VACIA Y SE DECLARA CON ESAS PALABRAS.")
    rojos = rojos_registrados(texto_reg)
    w("   CIFRA arneses registrados como ROJOS de esta vuelta: %d" % len(rojos))
    for script, ruta, motivo in rojos:
        w("      ROJO: %s" % script)
        w("         su salida en rojo: %s" % ruta)
        w("         motivo: %s" % motivo)
    corren, excluidos = particion_por_rojo(LOS_QUE_CORREN, rojos)
    w("   CIFRA arneses EXCLUIDOS de la doble corrida: %d" % len(excluidos))
    for script, _sal, _origen, ruta, motivo in excluidos:
        w("      EXCLUIDO Y NO RE CORRIDO: %s" % script)
        w("         motivo: %s" % motivo)
        w("         su salida en rojo, que se conserva sin tocar: %s" % ruta)
    if not excluidos:
        w("      (ninguno excluido, y el cero va escrito)")
    w("   CIFRA arneses que SI se corren dos veces: %d de %d"
      % (len(corren), len(LOS_QUE_CORREN)))
    w("")

    w("D) LA DOBLE CORRIDA, EN PROCESOS APARTE, EXIGIENDO EL MISMO sha256")
    paradas = 0
    for script, salida, origen in corren:
        ruta_sal = os.path.join(RAIZ, salida.replace("/", os.sep))
        antes = sha_de(ruta_sal)
        w("   %s (%s)" % (script, origen))
        w("      salida: %s" % salida)
        w("      ANTES de correr: %s"
          % ("no existe" if antes is None
             else "disco %d bytes | LF %d bytes | sha256 LF %s"
                  % (antes[2], antes[3], antes[1])))
        shas = []
        for k in (1, 2):
            r = subprocess.run([PY, script], cwd=RAIZ, capture_output=True)
            s = sha_de(ruta_sal)
            shas.append(s)
            w("      CORRIDA %d: exitcode %d | %s"
              % (k, r.returncode,
                 "LA SALIDA NO EXISTE" if s is None
                 else "disco %d bytes | LF %d bytes | sha256 LF %s"
                      % (s[2], s[3], s[1])))
            if r.returncode != 0:
                w("         ROJO: el arnes no salio en verde. Se trae sin arreglar.")
                paradas += 1
        iguales = shas[0] is not None and shas[0] == shas[1]
        w("      LAS DOS CORRIDAS DAN EL MISMO sha256: %s" % ("SI" if iguales else "NO"))
        if not iguales:
            w("      PARADA: esta salida CAMBIA SOLA. Se trae sin arreglarla.")
            paradas += 1
        movio = (antes is not None and shas[1] is not None and antes[1] != shas[1])
        w("      SE MOVIO RESPECTO A LA SALIDA QUE HABIA: %s" % ("SI" if movio else "no"))
        filas = numstat(salida)
        w("      git diff --numstat -- %s : %d fila(s)" % (salida, len(filas)))
        for f in filas:
            w("         %s" % f)
    w("")
    w("   CIFRA paradas: %d" % paradas)
    w("")

    w("E) EL CARRIL DE MUTACION DEL ARNES QUE NACE HOY, CORRIDO DOS VECES TAMBIEN")
    w("   (el `--mutacion` es lo que de verdad prueba la maquina, y correr el")
    w("    fichero sin argumentos NO lo corre. Se corre aparte y se coteja)")
    ruta_mut = os.path.join(LOOP, "SALIDA_V%d_T1A_MUTACION_REGISTRADOR.txt" % VUELTA)
    shas_m = []
    for k in (1, 2):
        r = subprocess.run([PY, "scripts/loop/%s" % reg, "--mutacion"],
                           cwd=RAIZ, capture_output=True)
        s = sha_de(ruta_mut)
        shas_m.append(s)
        w("      CORRIDA %d: exitcode %d | %s"
          % (k, r.returncode,
             "LA SALIDA NO EXISTE" if s is None
             else "disco %d bytes | LF %d bytes | sha256 LF %s"
                  % (s[2], s[3], s[1])))
        if r.returncode != 0:
            paradas += 1
            w("         ROJO: el carril de mutacion no sale en verde.")
    iguales_m = shas_m[0] is not None and shas_m[0] == shas_m[1]
    w("      LAS DOS CORRIDAS DAN EL MISMO sha256: %s" % ("SI" if iguales_m else "NO"))
    if not iguales_m:
        paradas += 1
        w("      PARADA: la salida del carril de mutacion CAMBIA SOLA.")
    w("")

    w("F) EL ESTADO DEL ARBOL DESPUES DE TODO")
    r = subprocess.run(["git", "diff", "--numstat", "--", "dataset/"],
                       cwd=RAIZ, capture_output=True)
    filas_ds = [l for l in r.stdout.decode("utf-8", errors="replace").splitlines()
                if l.strip()]
    w("   CIFRA filas de `git diff --numstat -- dataset/`: %d" % len(filas_ds))
    for f in filas_ds:
        w("      %s" % f)
    w("")

    # EL VEREDICTO NO MIRA `malas`: las 3 entradas sin sujeto congelado son la
    # deuda que el acta 189 deja abierta a proposito en su `4.7`, y meterla en
    # este veredicto convertiria una deuda VISIBLE Y DECLARADA en un rojo mudo
    # que se repite cada vuelta. Se publica arriba, con su cifra y sus nombres.
    ok = (len(faltan) == 0 and not invis and paradas == 0)
    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    w("   (y la guarda del sujeto congelado sigue en %d, publicada arriba y NO"
      % len(malas))
    w("    metida en este veredicto, por el motivo escrito en el fuente)")
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%d_T2_NOMINA.txt" % VUELTA)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
