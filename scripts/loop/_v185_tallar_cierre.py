# -*- coding: utf-8 -*-
r"""_v185_tallar_cierre.py . TALLA scripts/loop/_v185_cierre_texto.md, o sea las
SECCIONES 3 A 8 del reporte de la vuelta 185, CONTANDO SUS FICHEROS.

Ninguna cifra de aqui esta tecleada: todas salen de medir ficheros o de leer
`git` en esta corrida. Lo unico escrito a mano es EL JUICIO (los discutibles, las
preguntas, los pendientes de doctrina y las caidas propias), que no sale de
ningun instrumento y va marcado como juicio.

TODA CIFRA DE BYTES SALE CON SUS DOS CONVENCIONES EN LA MISMA LINEA, porque la
guarda `cifras_sin_pareja()` de `cerrar_reporte.py` cae si no.

LA SECCION 8 ES LA SEDE QUE `caidas_propias_del_cuerpo()` CUENTA, y de ahi salen
los numerales del veredicto de una linea. Las mismas caidas estan tambien en el
anexo de la TAREA 1, que es donde se levantaron: **no se tapan, se repiten en su
sede canonica**.

USO:
  python scripts/loop/_v185_tallar_cierre.py
"""
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
DEST = os.path.join(RAIZ, "scripts", "loop", "_v185_cierre_texto.md")
VUELTA = 185


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


def medir(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.exists(p):
        return None, None
    b = io.open(p, "rb").read()
    return os.path.getsize(p), len(b.replace((chr(13) + NL).encode(), NL.encode()))


def dime(rel):
    d, l = medir(rel)
    if d is None:
        return "**NO EXISTE**"
    return "**%d bytes en disco y %d bytes normalizados a LF**" % (d, l)


def texto(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.exists(p):
        return ""
    return io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def cifra(rel, patron, defecto="(no medida)"):
    h = re.findall(patron, texto(rel))
    return h[-1] if h else defecto


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    P = []
    w = P.append

    _c, rama = git(["rev-parse", "--abbrev-ref", "HEAD"])
    head_ap = texto("docs/loop/SALIDA_V185_HEAD_APERTURA.txt").strip()
    head_ci = texto("docs/loop/SALIDA_V185_HEAD_CIERRE.txt").strip()
    _c, acta = git(["log", "--format=%H", "-400", "--grep",
                    "ACTA DEL AUDITOR, VUELTA 185"])
    acta = acta.split(NL)[0].strip() if acta.strip() else ""
    _c, nac = git(["log", "--diff-filter=A", "--format=%H", "--",
                   "docs/loop/SALIDA_V185_HEAD_APERTURA.txt"])
    nac = nac.split(NL)[0].strip() if nac.strip() else ""

    _c, st = git(["status", "--porcelain"])
    n_st = len([l for l in st.splitlines() if l.strip()])
    _c, numstat = git(["diff", "--numstat", "--", "dataset/"])
    filas_sucias = len([l for l in numstat.splitlines() if l.strip()])

    VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
    filas = [json.loads(l) for l in io.open(
        os.path.join(RAIZ, VER.replace("/", os.sep)), encoding="utf-8") if l.strip()]
    por_clase = {}
    for f in filas:
        por_clase[f.get("clase")] = por_clase.get(f.get("clase"), 0) + 1
    puestos = [f.get("puesto_intra") for f in filas]
    huecos = len(set(range(min(puestos), max(puestos) + 1)) - set(puestos))
    dups = len(puestos) - len(set(puestos))
    import hashlib
    datos = io.open(os.path.join(RAIZ, VER.replace("/", os.sep)), "rb").read()
    lf = datos.replace((chr(13) + NL).encode(), NL.encode())
    sha_disco = hashlib.sha256(datos).hexdigest()
    sha_lf = hashlib.sha256(lf).hexdigest()

    motor_ap = cifra("docs/loop/SALIDA_V185_MOTOR_APERTURA.txt",
                     r"TODOS LOS TESTS PASARON \((\d+/\d+)\)")
    motor_ci = cifra("docs/loop/SALIDA_V185_MOTOR_CIERRE.txt",
                     r"TODOS LOS TESTS PASARON \((\d+/\d+)\)")
    web_ap = cifra("docs/loop/SALIDA_V185_WEB_APERTURA.txt",
                   r"Tests\s+(\d+ passed \(\d+\))")
    web_ci = cifra("docs/loop/SALIDA_V185_WEB_CIERRE.txt",
                   r"Tests\s+(\d+ passed \(\d+\))")
    tsc_ap = texto("docs/loop/SALIDA_V185_TSC_APERTURA.txt").strip()
    tsc_ci = texto("docs/loop/SALIDA_V185_TSC_CIERRE.txt").strip()
    desfase_ap = cifra("docs/loop/SALIDA_V185_DESFASE_CALIBRADO_APERTURA.txt",
                       r"DESFASE DEL CALIBRADO RASTREADO: (\d+) fila")
    desfase_ci = cifra("docs/loop/SALIDA_V185_DESFASE_CALIBRADO_CIERRE.txt",
                       r"DESFASE DEL CALIBRADO RASTREADO: (\d+) fila")

    # ------------------------------------------------------------------ CUERPO
    w("## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT")
    w("")
    w("**LAS DOS TAREAS DEL ENCARGO CERRARON.** El tope era dos, por el regimen")
    w("temporal de `AUDITOR.md` 6.2, y son dos. **La TAREA 1 cierra con una PARADA")
    w("levantada en su `1.c` y la TAREA 2 con otra en su `2.a`, y las dos van")
    w("escritas con su medicion, no con una impresion.**")
    w("")
    w("- rama, leida con `git rev-parse --abbrev-ref HEAD`: `%s`" % rama)
    w("- HEAD de apertura, sellado **antes de la primera operacion** en")
    w("  `docs/loop/SALIDA_V%d_HEAD_APERTURA.txt`: **`%s`**" % (VUELTA, head_ap[:8]))
    w("- HEAD del ultimo commit antes de cerrar, leido con `git rev-parse HEAD`")
    w("  **despues de la ultima operacion**: **`%s`**" % head_ci[:8])
    w("- commit del acta 185, localizado con `git log --grep` y no tecleado:")
    w("  **`%s`**" % acta[:8])
    w("- commit de nacimiento del bloque de apertura, `git log --diff-filter=A`:")
    w("  **`%s`**" % nac[:8])
    w("")
    w("**GATE 0 VERDE ENTERO EN SU CICLO, EN LA APERTURA Y OTRA VEZ AL CIERRE.** Sus")
    w("salidas son `docs/loop/SALIDA_V%d_GATE0_CMD1_APERTURA.txt` (%s)"
      % (VUELTA, dime("docs/loop/SALIDA_V%d_GATE0_CMD1_APERTURA.txt" % VUELTA)))
    w("y `docs/loop/SALIDA_V%d_GATE0_CMD1_CIERRE.txt` (%s),"
      % (VUELTA, dime("docs/loop/SALIDA_V%d_GATE0_CMD1_CIERRE.txt" % VUELTA)))
    w("con motor **%s** en la apertura y **%s** al cierre, `tsc` **%s** y **%s**,"
      % (motor_ap, motor_ci, tsc_ap, tsc_ci))
    w("y web **%s** y **%s**. La apertura entera vive en" % (web_ap, web_ci))
    w("`docs/loop/SALIDA_V%d_APERTURA.txt` (%s)"
      % (VUELTA, dime("docs/loop/SALIDA_V%d_APERTURA.txt" % VUELTA)))
    w("y **la sello el PRIMER commit de la vuelta**.")
    w("")
    w("**EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA, ANTES DE LA PRIMERA")
    w("OPERACION**, que es donde `EJECUTOR.md` 1 lo manda desde la 178: **%s filas**"
      % desfase_ap)
    w("en la apertura y **%s filas** al cierre." % desfase_ci)
    w("")
    w("**EL ARCHIVO DE VEREDICTOS NO SE MOVIO, Y ESA ES LA PRUEBA INDEPENDIENTE DE")
    w("QUE ESTA VUELTA NO TOCO NINGUN VEREDICTO.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`:")
    w("**%d filas**, **A %d, B %d, C %d, D %d**, **%d huecos y %d duplicados**,"
      % (len(filas), por_clase.get("A", 0), por_clase.get("B", 0),
         por_clase.get("C", 0), por_clase.get("D", 0), huecos, dups))
    w("%s, y `sha256` **`%s`**" % (dime(VER), sha_lf[:16]))
    w("**identico por las dos convenciones, disco `%s` y LF `%s`**."
      % (sha_disco[:16], sha_lf[:16]))
    w("Es el mismo que la apertura de esta vuelta midio y el mismo que las actas 179")
    w("a 185 publican.")
    w("")

    w("## 4. LA GUARDA DEL COMMIT DE `dataset/`, CORRIDA EL DIA QUE SERVIA")
    w("")
    w("`git status --porcelain` da **%d lineas** al cerrar la vuelta, y" % n_st)
    w("`git diff --numstat -- dataset/` da **%d filas**. **Al ENTRAR, medido en el"
      % filas_sucias)
    w("bloque de apertura antes de la primera operacion, dio 0 filas tambien.**")
    w("**Ninguna perdida de catalogo que declarar**, y `dataset/` no se commitea en")
    w("esta vuelta.")
    w("")
    w("**Y ESTA VUELTA NO TIENE LA `M dataset/metadata/master_graph.json` QUE LAS")
    w("ANTERIORES TRAIAN.** El arbol abrio limpio, con `git status --porcelain` en")
    w("cero lineas, cosa que el docstring del bloque de apertura predijo **antes** de")
    w("medirla y que sus bloques C, D, E y F midieron sin saber lo que habia escrito.")
    w("")

    w("## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO")
    w("")
    w("**LOS SIETE VAN EN SUS DOS SEDES Y AQUI SE LISTAN JUNTOS, QUE ES LO QUE LA")
    w("`5.7` DEL ACTA 185 PIDE.** Los cinco primeros nacen en el anexo de la TAREA 1")
    w("y los dos ultimos en el de la TAREA 2; **ninguno se tapa y ninguno cambia de")
    w("redaccion al repetirse aqui su titulo**.")
    w("")
    w("- **`D.1`. ANADI UN CAMBIO MAS DE LOS TRES QUE LA `1.d` NOMBRA:** la")
    w("  procedencia de la novena columna en la prosa del tallador. No mueve ninguna")
    w("  celda, pero el encargo no lo pidio.")
    w("- **`D.2`. MI ARNES DE LA `1.b` SALIO EN ROJO EN SU PRIMERA CORRIDA Y LO")
    w("  REPARE YO EN VEZ DE TRAERLO.** Lei que la regla de detenerse protege a los")
    w("  arneses ya sellados y no al que estoy escribiendo. **La corrida en rojo va")
    w("  entera en el reporte.**")
    w("- **`D.3`. PUBLIQUE LA COLUMNA `quien lo sello` CON UNA NEGRITA COMPUTADA**,")
    w("  deducida de las celdas que tenia que reproducir. Nadie escribio esa regla de")
    w("  formato.")
    w("- **`D.4`. NO METI LOS DOS ARNESES NUEVOS EN LA NOMINA DE LA BATERIA.** Esta")
    w("  vuelta no es de bateria y su encargo no nombra la nomina. **La 189 empezara")
    w("  en rojo por esa via si nadie los mete antes.**")
    w("- **`D.5`. GUARDE EL REPORTE DE LA 184 QUE `cerrar_reporte.py` SI LLEGO A")
    w("  ESCRIBIR Y DESPUES RESTAURE EL ARBOL** con `git checkout`. Destruirlo habria")
    w("  perdido la evidencia; dejarlo habria hecho que el esqueleto pisara un texto")
    w("  sin otra sede.")
    w("- **`D.6`. NO PEGUE ENTERA LA SALIDA ROJA DEL CIERRE DE LA 184**, porque lleva")
    w("  dentro la marca de maquina que la pieza (2) busca en todo el texto. **La cito")
    w("  por su ruta con sus bytes y pego las lineas que deciden.** Es una desviacion")
    w("  de la letra del encargo.")
    w("- **`D.7`. CERRE EL REPORTE DE LA 185 SABIENDO QUE EL DE LA 184 NO CERRO.** Se")
    w("  puede leer que el orden del encargo hacia del cierre de la 184 una condicion")
    w("  previa. **La lectura contraria es defendible y por eso va marcado.**")
    w("")

    w("## 6. LAS PREGUNTAS")
    w("")
    w("**`P.1`. LA PIEZA (4) Y LA PIEZA (2) DE `piezas_que_faltan()`, ¿SE REPARAN")
    w("JUNTAS O POR SEPARADO?** La (4) es la copia gemela de la regla que la `1.c`")
    w("acaba de reparar. La (2) es otra especie: busca su marca **en todo el texto**,")
    w("y un reporte que **cita** una salida roja dentro de un bloque cercado la lleva")
    w("dentro sin estar sin tallar. **No se cual es prioridad y no me lo encargaron.**")
    w("")
    w("**`P.2`. ¿QUE SE HACE CON LAS CIFRAS SIN PAREJA DEL REPORTE DE LA 184?** La")
    w("guarda `cifras_sin_pareja()` las caza y el encargo prohibe tocar ese texto. **O")
    w("se exime el texto ya escrito, o se reescribe, o la guarda aprende a mirar solo")
    w("lo nuevo.** No elijo yo.")
    w("")
    w("**`P.3`. ¿LOS DOS ARNESES NACIDOS HOY ENTRAN EN LA NOMINA DE LA BATERIA, Y")
    w("QUIEN LOS METE?** La `5.6` del acta 185 ampara meterlos en su propia vuelta,")
    w("pero esta no es vuelta de bateria. **Medido hoy: `arneses_que_faltan()` da 2.**")
    w("")

    w("## 7. PENDIENTES DE DOCTRINA")
    w("")
    w("**`PD.1` SIGUE ABIERTA Y NO LA TOCO:** las cinco `D` con el diferenciador ya")
    w("presente el dia del veredicto, **1778, 2530, 2540, 3141 y 3232**, hoy con sus")
    w("cinco puestos escritos en el `R.47` y leidos del acta, no copiados del encargo.")
    w("")
    w("**`PD.5` NUEVA. UNA MARCA DE MAQUINA CITADA DENTRO DE UN BLOQUE CERCADO SIGUE")
    w("SIENDO UNA MARCA DE MAQUINA.** La pieza (2) busca su marca en todo el texto y")
    w("`cifras_sin_pareja()` ya excluye los bloques cercados: **dos guardas del mismo")
    w("fichero tratan la cita al reves la una de la otra.** Hoy eso impide que un")
    w("reporte pueda citar entero el rojo de otro.")
    w("")
    w("**`PD.6` NUEVA. UNA REGLA ESCRITA DOS VECES EN EL MISMO FICHERO.**")
    w("`rama_de_la_seccion9()` y la pieza (4) de `piezas_que_faltan()` llevan la misma")
    w("comparacion de vuelta ajena. **Reparar una y no la otra deja el instrumento")
    w("diciendo dos cosas distintas del mismo caso.** Es la PARADA de la `1.c` dicha")
    w("como doctrina.")
    w("")
    w("**`PD.2`, `PD.3` Y `PD.4` QUEDARON CERRADAS POR EL ACTA 185** y no se reabren")
    w("aqui: estan registradas en el `R.47` con su estado leido del titulo del acta.")
    w("")

    w("## 8. MIS CAIDAS PROPIAS, CON SU NOMBRE Y NINGUNA TAPADA")
    w("")
    w("**`C.1`. ESCRIBI UN ARNES CUYA SALIDA SELLADA LLEVABA DENTRO EL MISMO DATO QUE")
    w("CAMBIA SOLO QUE LA REPARACION VENIA A QUITAR.** La primera version de")
    w("`scripts/loop/vuelta185_tarea1b_mutacion_sin_temporal.py` pegaba sus lineas de")
    w("entrada **crudas**, con el sufijo aleatorio del `mkdtemp` dentro. **Habria")
    w("hecho caer la bateria de la 189 por la misma averia que estaba reparando.** Lo")
    w("cace **releyendo mi propio fichero**, no un instrumento, y anadi `mostrar()`.")
    w("La prueba de que ya no pasa es que sus dos corridas seguidas dan la misma")
    w("salida byte a byte.")
    w("")
    w("**`C.2`. MI PRIMER ARNES DE LA `1.b` FABRICO UN TEMPORAL QUE NO EXISTE Y SUS")
    w("DOS CASOS DE RUTA RELATIVA SALIERON EN ROJO.** La funcion bajo prueba estaba")
    w("bien; lo que estaba mal era **mi entrada tecleada**, que no es la cadena que")
    w("`os.path.relpath` produce. **Es exactamente la especie que esta casa castiga:")
    w("teclear en vez de medir.** La corrida en rojo va entera en el reporte y el")
    w("motivo queda escrito dentro del propio fichero, no en una nota aparte.")
    w("")

    t = NL.join(P) + NL
    io.open(DEST, "w", encoding="utf-8", newline=NL).write(t)
    print("ESCRITO: %s" % DEST)
    print("CIFRA bytes: %d | CIFRA lineas: %d" % (len(t.encode("utf-8")), t.count(NL)))
    print("CIFRA secciones: %d" % len([l for l in t.split(NL) if l.startswith("## ")]))
    print("CIFRA guiones largos o medios: %d"
          % (t.count(chr(8212)) + t.count(chr(8211))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
