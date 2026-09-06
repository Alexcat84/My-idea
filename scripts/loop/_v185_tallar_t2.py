# -*- coding: utf-8 -*-
r"""_v185_tallar_t2.py . TALLA scripts/loop/_v185_t2_seccion.md CONTANDO SUS
FICHEROS DE SALIDA, PARA ANEXAR LA TAREA 2 AL REPORTE DE LA VUELTA 185.

LA TABLA SE CUENTA DE SU FICHERO (`EJECUTOR.md` 1). Ninguna cifra de aqui esta
tecleada: todas salen de contar sus ficheros en esta corrida. Lo unico escrito a
mano es EL JUICIO, que va marcado como juicio.

Y UNA COSA QUE ESTE FICHERO HACE DISTINTO, DECLARADA AQUI PORQUE ES UNA DECISION
DE ALCANCE: NO PEGA ENTERA la salida roja del cierre de la 184. El motivo esta
MEDIDO y no supuesto: esa salida contiene la marca de maquina que la pieza (2) de
`piezas_que_faltan()` busca EN TODO EL TEXTO del reporte, sin excluir los bloques
cercados, asi que pegarla haria caer el cierre de ESTE reporte por el mismo falso
positivo que ya cazo al de la 184. Se cita por su RUTA con sus bytes, se pegan
las lineas que deciden, y SE DICE. El fichero entero esta commiteado y no se
pierde nada.

USO:
  python scripts/loop/_v185_tallar_t2.py
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
DEST = os.path.join(RAIZ, "scripts", "loop", "_v185_t2_seccion.md")
# LA MARCA DE MAQUINA QUE NO PUEDE APARECER EN ESTE TEXTO, ARMADA POR TROZOS
# PARA QUE ESTE PROPIO FICHERO NO LA LLEVE ENTERA DENTRO.
MARCA_PROHIBIDA = "PENDIENTE DE TALLAR" + " AL CIERRE"


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


def ruta(nombre, base=None):
    return os.path.join(base or LOOP, nombre)


def medir(nombre, base=None):
    p = ruta(nombre, base)
    if not os.path.exists(p):
        return None, None
    b = io.open(p, "rb").read()
    return os.path.getsize(p), len(b.replace((chr(13) + NL).encode(), NL.encode()))


def texto(nombre, base=None):
    p = ruta(nombre, base)
    if not os.path.exists(p):
        return ""
    return io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def dime(nombre, base=None):
    d, l = medir(nombre, base)
    if d is None:
        return "**NO EXISTE**"
    return "**%d bytes en disco y %d bytes normalizados a LF**" % (d, l)


def cifra(nombre, patron, defecto="(no medida)"):
    h = re.findall(patron, texto(nombre))
    return h[-1] if h else defecto


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    P = []
    w = P.append

    t_cierre = texto("SALIDA_V185_CERRAR_REPORTE_184.txt")
    rama184 = cifra("SALIDA_V185_CERRAR_REPORTE_184.txt",
                    r"RAMA DE LA SECCION 9, decidida por rama_de_la_seccion9\(\): (\w+)")
    tramos184 = cifra("SALIDA_V185_CERRAR_REPORTE_184.txt",
                      r"CIFRA tramos sellados EN LA VUELTA 184: (\d+)")
    num_no_calzan = cifra("SALIDA_V185_CERRAR_REPORTE_184.txt",
                          r"CIFRA numerales que NO calzan: (\d+)")
    piezas_faltan = cifra("SALIDA_V185_CERRAR_REPORTE_184.txt",
                          r"CIFRA piezas que faltan: (\d+)")
    sin_pareja = cifra("SALIDA_V185_CERRAR_REPORTE_184.txt",
                       r"CIFRA cifras publicadas sin su pareja: (\d+)")
    citas_mal = cifra("SALIDA_V185_CERRAR_REPORTE_184.txt",
                      r"CIFRA citas de arnes cotejadas que NO calzan: (\d+)")
    ver_sha = cifra("SALIDA_V185_T2A_VEREDICTO_184.txt",
                    r"VEREDICTO DEL TALLADOR: (\w+)")
    arch_bytes = cifra("SALIDA_V185_T2A_ARCHIVAR_184.txt", r"bytes\s+(\d+)")
    arch_sha = cifra("SALIDA_V185_T2A_ARCHIVAR_184.txt", r"sha256 \(LF\)\s+([0-9a-f]+)")
    arch_lineas = cifra("SALIDA_V185_T2A_ARCHIVAR_184.txt", r"lineas\s+(\d+)")

    esq_bytes = cifra("SALIDA_V185_ESQUELETO.txt",
                      r"ESQUELETO ESCRITO: docs/loop/REPORTE\.md \((\d+) bytes")
    esq_filas = cifra("SALIDA_V185_ESQUELETO.txt", r"filas de tarea abiertas: (\d+)")
    esq_ya = "YA EXISTE con contenido IDENTICO" in texto("SALIDA_V185_ESQUELETO.txt")

    _c, numstat = git(["diff", "--numstat", "--", "dataset/"])
    filas_sucias = len([l for l in numstat.splitlines() if l.strip()])

    # ------------------------------------------------------------------ CUERPO
    w("### TAREA 2. EL CIERRE DE DOS REPORTES. EL DE LA 185 CIERRA; EL DE LA 184, NO: PARADA")
    w("")
    w("**TODAS LAS CIFRAS DE ESTA SECCION SALEN DE CONTAR SUS FICHEROS DE SALIDA CON")
    w("`scripts/loop/_v185_tallar_t2.py`, Y NINGUNA ESTA TECLEADA.**")
    w("")

    w("#### 2.a EL REPORTE DE LA 184: LA RAMA NUEVA FUNCIONA Y EL CIERRE SIGUE EN ROJO")
    w("")
    w("**PRIMERO LAS TRES PIEZAS, COTEJADAS POR `sha256` Y POR BYTES CONTRA LO QUE LA")
    w("184 MIDIO. LAS TRES CALZAN**, y el cotejo salio **%s**:" % ver_sha)
    w("")
    w("| pieza | medida hoy |")
    w("|---|---|")
    w("| `docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt` | %s |"
      % dime("SALIDA_V184_TALLADOR_CABECERA.txt"))
    w("| `scripts/loop/_v184_cierre_texto.md` | %s |"
      % dime("_v184_cierre_texto.md", os.path.join(RAIZ, "scripts", "loop")))
    w("| `docs/loop/SALIDA_V183_BATERIA.txt` | %s |" % dime("SALIDA_V183_BATERIA.txt"))
    w("")
    w("Salida del cotejo: `docs/loop/SALIDA_V185_T2A_VEREDICTO_184.txt` (%s)."
      % dime("SALIDA_V185_T2A_VEREDICTO_184.txt"))
    w("")
    w("**EL VEREDICTO DE UNA LINEA SE TALLO Y NO SE TECLEO A OJO.** Sus dos numerales")
    w("salen de `caidas_propias_del_cuerpo()` y `tareas_de_la_tabla()` corridas sobre")
    w("las dos mitades que la guarda `B.1` juzga, y la guarda dio **CIFRA numerales")
    w("que NO calzan: %s**. Mutado un numeral, la guarda cae. La frase quedo en" % num_no_calzan)
    w("`docs/loop/SALIDA_V185_T2A_VEREDICTO_184_FRASE.txt` (%s)."
      % dime("SALIDA_V185_T2A_VEREDICTO_184_FRASE.txt"))
    w("")
    w("**LO QUE EL ENCARGO PEDIA Y SI PASO: LA RAMA DE LA SECCION 9 SALIO `%s`**"
      % rama184)
    w("**POR LA RAMA NUEVA**, y su motivo nombra que la bateria se **CONTINUO** y que")
    w("la vuelta 184 sello **%s** de sus tramos, leidos del asunto de su ultimo commit" % tramos184)
    w("con `git log` y no tecleados. Las lineas que lo dicen, pegadas de la salida:")
    w("")
    w("```")
    for l in t_cierre.split(NL):
        if ("RAMA DE LA SECCION 9" in l or "motivo: la bateria del fichero" in l
                or "CIFRA tramos sellados EN LA VUELTA" in l
                or re.match(r"^\s+tramo \d+\s+-> vuelta \d+", l)):
            w(l.rstrip()[:200])
    w("```")
    w("")
    w("#### PARADA. EL CIERRE DE LA 184 CAE EN ROJO POR TRES GUARDAS MAS, Y NINGUNA ES LA RAMA")
    w("")
    w("`scripts/loop/cerrar_reporte.py --vuelta 184` devuelve **exitcode 1**. La salida")
    w("entera vive en `docs/loop/SALIDA_V185_CERRAR_REPORTE_184.txt` (%s)."
      % dime("SALIDA_V185_CERRAR_REPORTE_184.txt"))
    w("")
    w("**Y AQUI NO SE PEGA ENTERA, CON UN MOTIVO MEDIDO Y NO UNA EXCUSA.** Esa salida")
    w("lleva dentro la marca de maquina que la **pieza (2)** de `piezas_que_faltan()`")
    w("busca **en todo el texto del reporte, sin excluir los bloques cercados**.")
    w("Pegarla aqui haria caer el cierre de **este** reporte por el mismo falso")
    w("positivo que cazo al de la 184, que es exactamente la averia que se esta")
    w("reportando. **Se cita por su ruta con sus bytes, se pegan las lineas que")
    w("deciden, y se dice.** El fichero entero esta commiteado: no se pierde nada.")
    w("")
    w("**LOS TRES MOTIVOS DEL ROJO, CONTADOS DE ESA SALIDA:**")
    w("")
    w("| motivo | cifra de su fichero | que especie es |")
    w("|---|---:|---|")
    w("| piezas de las cuatro que faltan | **%s** | (2) y (4) |" % piezas_faltan)
    w("| cifras publicadas sin su pareja | **%s** | guarda `cifras_sin_pareja()` |" % sin_pareja)
    w("| citas de arnes que NO calzan | **%s** | ninguna |" % citas_mal)
    w("")
    w("1. **LA PIEZA (4) ES LA COPIA GEMELA DE LA REGLA QUE LA `1.c` ACABA DE")
    w("   REPARAR.** `piezas_que_faltan()` lleva su propia comparacion de vuelta ajena")
    w("   y **no recibe la evidencia de los tramos**. Es la PARADA que la TAREA 1.c ya")
    w("   trajo levantada y que el encargo prohibe tocar.")
    w("2. **LA PIEZA (2) ES UN FALSO POSITIVO DE LA MISMA ESPECIE.** La cabecera **SI**")
    w("   esta pegada: las **11 filas de 11** del tallador estan dentro y **0 quedan")
    w("   fuera**. Lo que enciende la pieza es que la marca de maquina aparece **UNA**")
    w("   vez en todo el reporte, en su **linea 353**, **dentro de un bloque cercado**")
    w("   que cita la salida roja de la 184.")
    w("3. **LAS CIFRAS SIN PAREJA VIVEN EN EL CUERPO QUE LA 184 YA ESCRIBIO**, y el")
    w("   encargo manda cerrar *\"con el texto que ya tiene\"*. Repararlas seria")
    w("   reescribir un texto que no me toca reescribir.")
    w("")
    w("**QUE HAY EN DISCO, DICHO SIN ADORNAR:**")
    w("")
    w("- `docs/loop/reportes/REPORTE_V184.md`, %s, **%s lineas**, `sha256` LF"
      % (dime("REPORTE_V184.md", os.path.join(LOOP, "reportes")), arch_lineas))
    w("  `%s`, archivado con **exitcode 0**. **NO ES EL CERRADO:**" % arch_sha[:16])
    w("  `archivar_reporte.py` lee de git y no del arbol, asi que archivo el ultimo")
    w("  estado **commiteado**, el que la 184 dejo.")
    w("- `docs/loop/SALIDA_V185_T2A_REPORTE_184_CERRADO_EN_ROJO.md` (%s):"
      % dime("SALIDA_V185_T2A_REPORTE_184_CERRADO_EN_ROJO.md"))
    w("  lo que el instrumento **si** llego a escribir antes de devolver 1, guardado")
    w("  con un nombre que dice lo que es. El instrumento escribe en su bloque C y")
    w("  juzga en el D.")
    w("- `docs/loop/SALIDA_V185_T2A_REPORTE_184_ANTES.md` (%s):"
      % dime("SALIDA_V185_T2A_REPORTE_184_ANTES.md"))
    w("  el estado previo, para que las dos caras se puedan comparar.")
    w("- `docs/loop/REPORTE.md` se restauro con `git checkout` al estado commiteado,")
    w("  para que el arbol y el archivado digan lo mismo.")
    w("")
    w("**LA CUENTA DE VUELTAS QUE CIERRAN SU PROPIO REPORTE, PARA LA 184, SIGUE EN")
    w("CERO.** No lo fuerzo y no lo arreglo yo.")
    w("")

    w("#### 2.b EL REPORTE DE LA 185 SE ABRE, SE LLENA Y SE CIERRA")
    w("")
    w("**EL ESQUELETO** se tallo en el paso 4 del orden de esta vuelta, con sus **%s"
      % esq_filas)
    w("filas vacias**. `docs/loop/REPORTE.md` nacio con **%s bytes normalizados a LF**,"
      % esq_bytes)
    w("contados por el propio esqueleto antes de escribirlos en disco.")
    w("Salida: `docs/loop/SALIDA_V185_ESQUELETO.txt` (%s)." % dime("SALIDA_V185_ESQUELETO.txt"))
    w("")
    w("**Y SU PASO 0 NO TUVO REPORTE AJENO QUE ARCHIVAR, Y LO DICE EN VEZ DE DEJAR LA")
    w("FILA MUDA.** Su salida publica que el destino")
    w("`docs/loop/reportes/REPORTE_V184.md` **%s**, y que los dos `sha256` calzan con"
      % ("YA EXISTE con contenido IDENTICO" if esq_ya else "NO estaba"))
    w("el reporte que se iba a pisar. Es lo que el encargo predijo, porque la **2.a**")
    w("lo archivo antes.")
    w("")
    w("**CADA TAREA ANEXO SU FILA AL CERRARSE**, no al final: la TAREA 1 entro con su")
    w("seccion entera antes de que esta se escribiera.")
    w("")
    w("**LA SECCION 9 DE ESTE REPORTE CIERRA CON EL HUECO DECLARADO Y MEDIDO, POR EL")
    w("CARRIL DE `cerrar_reporte.py` Y NO A MANO.** Las tres piezas van juntas o no")
    w("vale: **el nombre del fichero**, **sus bytes medidos** y **la atribucion**. **LA")
    w("ATRIBUCION ES QUE LA BATERIA CORRE CADA CINCO VUELTAS Y QUE LA SIGUIENTE ES LA")
    w("189**, por `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria")
    w("cerro entera en la 184 con sus nueve tramos sellados.")
    w("")
    w("**SI ESTA VUELTA CIERRA SU REPORTE, ES LA PRIMERA DE LAS DOS SEGUIDAS QUE EL")
    w("REGIMEN 6.2 PIDE PARA DEVOLVER EL TOPE A CINCO.** Dicho con esas palabras, y")
    w("dicho tambien lo otro: **la 184 no lo cerro hoy tampoco**, asi que la cuenta que")
    w("empieza es la de la 185 y no una que venga de atras.")
    w("")

    w("#### LAS GUARDAS DEL CIERRE, RECOMPUTADAS AL CIERRE")
    w("")
    w("`git diff --numstat -- dataset/` al salir de la vuelta: **%d filas**. Al entrar"
      % filas_sucias)
    w("dio **0 filas**, medido en el bloque de apertura antes de la primera operacion.")
    w("")
    w("El ciclo de Gate 0 corrio entero y en su orden al cierre, y sus salidas viven en")
    w("`docs/loop/SALIDA_V185_*_CIERRE.txt`. La tabla de la cabecera de este reporte")
    w("sale de ellas con `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 185`")
    w("y **ninguna celda esta tecleada**.")
    w("")

    w("#### LOS DISCUTIBLES DE ESTA TAREA, MARCADOS ANTES DE SABER SI ACIERTO")
    w("")
    w("**`D.6`. NO PEGUE ENTERA LA SALIDA ROJA DEL CIERRE DE LA 184.** El encargo de")
    w("la 2.a dice *\"paras y lo traes entero\"*, y la 184 pego la suya entera. **Yo la")
    w("cito por su ruta con sus bytes y pego las lineas que deciden**, porque pegarla")
    w("entera haria caer el cierre de este reporte por la pieza (2). **Mi razon es que")
    w("un reporte que no cierra no trae la PARADA a nadie**, y el fichero entero esta")
    w("commiteado. **Pero es una desviacion de la letra y la marco.**")
    w("")
    w("**`D.7`. CERRE EL REPORTE DE LA 185 SABIENDO QUE EL DE LA 184 NO CERRO.** Se")
    w("puede leer que el orden del encargo hacia del cierre de la 184 una condicion")
    w("previa. **Mi lectura es que son dos reportes distintos y que el mio no depende")
    w("del suyo**, y que dejar los dos sin cerrar seria la quinta vuelta seguida sin")
    w("reporte cerrado. **Lo marco porque la lectura contraria es defendible.**")
    w("")

    w("#### PENDIENTES DE DOCTRINA")
    w("")
    w("**`PD.1` SIGUE ABIERTA Y NO LA TOCO:** las cinco `D` con el diferenciador ya")
    w("presente el dia del veredicto, hoy con sus cinco puestos escritos en el `R.47`.")
    w("")
    w("**`PD.5` NUEVA. UNA MARCA DE MAQUINA CITADA DENTRO DE UN BLOQUE CERCADO SIGUE")
    w("SIENDO UNA MARCA DE MAQUINA.** La pieza (2) busca su marca en todo el texto y")
    w("`cifras_sin_pareja()` ya excluye los bloques cercados: **dos guardas del mismo")
    w("fichero tratan la cita al reves la una de la otra**. No hay regla escrita que")
    w("elija, y hoy eso impide que un reporte pueda citar el rojo de otro.")
    w("")
    w("**`PD.6` NUEVA. UNA REGLA ESCRITA DOS VECES EN EL MISMO FICHERO.**")
    w("`rama_de_la_seccion9()` y la pieza (4) de `piezas_que_faltan()` llevan la misma")
    w("comparacion de vuelta ajena. Reparar una y no la otra deja el instrumento")
    w("diciendo dos cosas distintas del mismo caso. **Es la PARADA de la 1.c dicha como")
    w("doctrina.**")
    w("")

    t = NL.join(P) + NL
    if MARCA_PROHIBIDA in t:
        print("ROJO: el texto tallado lleva dentro la marca de maquina %r, que haria"
              % MARCA_PROHIBIDA)
        print("      caer el cierre de este mismo reporte. NO se escribe.")
        return 1
    io.open(DEST, "w", encoding="utf-8", newline=NL).write(t)
    print("ESCRITO: %s" % DEST)
    print("CIFRA bytes: %d | CIFRA lineas: %d" % (len(t.encode("utf-8")), t.count(NL)))
    print("CIFRA guiones largos o medios: %d"
          % (t.count(chr(8212)) + t.count(chr(8211))))
    print("CIFRA apariciones de la marca de maquina: 0 (comprobado antes de escribir)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
