# -*- coding: utf-8 -*-
r"""vuelta195_tarea3f_bateria_de_lo_tocado.py . LA BATERIA CORRIDA **SOLO SOBRE LO
QUE LA VUELTA 195 TOCO**, para comprobar que el rojo que se ataco se apago
(TAREA 3.f).

**ESTO NO ES LA BATERIA Y NO SE PUEDE CITAR COMO SI LO FUERA.** `AUDITOR.md` 6.1
fija que la bateria corre CADA CINCO VUELTAS en una vuelta propia que no lleva
nada mas, **la 194 la corrio entera por sus diez tramos y la proxima cae en la
199**. Esto es OTRA COSA: una corrida ACOTADA a los arneses que esta vuelta
modifico o anadio, que es lo que el encargo pide con esas palabras (*"CORRE LA
BATERIA SOLO SOBRE LO QUE TOCASTE"*, *"NO corras la bateria entera"*).

**LA LISTA DE LO TOCADO NO SE TECLEA A OJO: se computa de git**, con
`git diff --name-only <apertura>..HEAD` filtrado por el censo de arneses, y
ADEMAS se cotejan contra ella los nombres que la propia TAREA 3 dice haber
tocado. **Las dos listas se publican y su diferencia se nombra**; si la de git
trae alguno que la tarea no declara, se corre igual.

LO QUE SI SE MIDE ENTERO, PORQUE ES LO QUE EL ENCARGO MANDA PUBLICAR:
  . la CIFRA de arneses del censo que se quedan FUERA de la nomina, y su lista;
  . la CIFRA de entradas de la nomina SIN SUJETO CONGELADO, y su lista;
  . la CIFRA de entradas que el censo NO VE.
**Las tres se leen de las funciones del propio modulo, sobre el repo de hoy, y no
de esta corrida acotada.** Si alguna no es cero, se dice con su numero y su lista
en vez de redondearla.

LA DOBLE CORRIDA NO SE AFLOJA: cada arnes se corre DOS VECES con
`correr_dos_veces()`, que es el cotejo de reproducibilidad de la vuelta 141.

Y `dataset/` SE MIDE AL ENTRAR Y AL SALIR, mas la sede del turno del auditor, que
es la que un arnes de esta lista rompio en la 194 y que la 194 arreglo.

USO:
  python scripts/loop/vuelta195_tarea3f_bateria_de_lo_tocado.py
"""
import hashlib
import io
import os
import subprocess
import sys
import time

NL = chr(10)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as B   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
SALIDA = os.path.join(LOOP, "SALIDA_V195_T3F_BATERIA_DE_LO_TOCADO.txt")
TURNO = "docs/loop/_TURNO_DEL_AUDITOR.json"

# EL COMMIT DE APERTURA DE ESTA VUELTA, leido del sello y no tecleado.
SELLO_HEAD = os.path.join(LOOP, "SALIDA_V195_HEAD_APERTURA.txt")

# LO QUE LA TAREA 3 Y LA TAREA 4 DICEN HABER TOCADO. Va escrito aqui para poder
# COTEJARLO contra lo que git dice, no para sustituirlo.
DECLARADOS_POR_LA_TAREA = [
    # 3.d, el que no mordia
    "vuelta172_tarea5_mutacion_cierre.py",
    # 3.c, los cuatro que reciben su declaracion de sujeto congelado
    "vuelta186_tarea2c_mutacion_cierre_tardio.py",
    "vuelta187_tarea4_mutacion_dos_convenciones.py",
    "vuelta188_tarea4_mutacion_cobertura_parejas.py",
    "vuelta193_tarea4e_mutacion_sello_entre_procesos.py",
    # 3.a, los seis que entran en la nomina
    "vuelta191_tarea3_mutacion_lineas.py",
    "vuelta191_tarea4_mutacion_veredicto.py",
    "vuelta191_tarea6_mutacion_bloque_tallado.py",
    "vuelta192_tarea4_mutacion_cuarta_puerta.py",
    "vuelta194_tarea2c_mutacion_sede_del_turno.py",
    # 3.g y 4.c, los dos que nacen hoy
    "vuelta195_tarea3g_mutacion_nomina_enchufada.py",
    "vuelta195_tarea4c_mutacion_componer_rojo.py",
]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def sha_de(rel):
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(ruta):
        return None
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (len(datos), len(lf), hashlib.sha256(lf).hexdigest())


def tocados_segun_git(head_apertura):
    """LOS ARNESES DEL CENSO QUE CAMBIARON DESDE LA APERTURA. Semi-pura: lo unico
    que hace es preguntarle a git y filtrar por el censo.

    SE PREGUNTA A GIT Y NO SE TECLEA, que es la unica forma de que la lista no
    dependa de que alguien se acuerde de anadir un nombre."""
    c, salida = git(["diff", "--name-only", "%s..HEAD" % head_apertura,
                     "--", "scripts/loop/"])
    if c != 0:
        return None
    censo = set(B.arneses_del_directorio())
    nombres = set()
    for l in salida.splitlines():
        base = os.path.basename(l.strip())
        if base in censo:
            nombres.add(base)
    # Y LOS NO COMMITEADOS TODAVIA, que en esta vuelta son los que nacen hoy.
    c2, sal2 = git(["status", "--porcelain", "--", "scripts/loop/"])
    if c2 == 0:
        for l in sal2.splitlines():
            base = os.path.basename(l.strip().split(" ", 1)[-1].strip())
            if base in censo:
                nombres.add(base)
    return sorted(nombres)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 195, TAREA 3.f: LA BATERIA CORRIDA SOLO SOBRE LO QUE ESTA VUELTA")
    w("TOCO. NO ES LA BATERIA ENTERA Y NO SE CITA COMO TAL.")
    w("=" * 78)
    w("LA CADENCIA, LEIDA DE AUDITOR.md 6.1 Y NO DE MEMORIA: la bateria corre")
    w("CADA CINCO VUELTAS en una vuelta propia que no lleva nada mas; la 194 la")
    w("corrio entera por sus diez tramos y la proxima cae en la 199.")
    w("")

    w("A) EL ESTADO AL ENTRAR, MEDIDO Y NO SUPUESTO")
    c, numstat = git(["diff", "--numstat", "--", "dataset/"])
    filas_entrada = [l for l in numstat.splitlines() if l.strip()]
    w("   CIFRA filas de `git diff --numstat -- dataset/` AL ENTRAR: %d"
      % len(filas_entrada))
    turno_entrada = sha_de(TURNO)
    w("   %s al entrar: %s" % (TURNO,
                               "%d bytes, sha256 LF %s"
                               % (turno_entrada[0], turno_entrada[2][:16])
                               if turno_entrada else "NO EXISTE"))
    head_ap = io.open(SELLO_HEAD, encoding="utf-8").read().strip()
    w("   HEAD de apertura, leido del sello y no tecleado: %s" % head_ap[:12])
    w("")

    w("B) LO QUE SE TOCO, COMPUTADO DE GIT Y COTEJADO CONTRA LO DECLARADO")
    de_git = tocados_segun_git(head_ap)
    if de_git is None:
        w("   ROJO: git no pudo dar la lista. NO SE TECLEA UNA.")
        print(NL.join(L))
        return 1
    w("   CIFRA arneses tocados segun git: %d" % len(de_git))
    for n in de_git:
        w("      %s" % n)
    w("   CIFRA arneses que la TAREA declara haber tocado: %d"
      % len(DECLARADOS_POR_LA_TAREA))
    solo_git = sorted(set(de_git) - set(DECLARADOS_POR_LA_TAREA))
    solo_dec = sorted(set(DECLARADOS_POR_LA_TAREA) - set(de_git))
    w("   en git y NO declarados por la tarea: %s"
      % (", ".join(solo_git) or "(ninguno)"))
    w("   declarados por la tarea y NO en git: %s"
      % (", ".join(solo_dec) or "(ninguno)"))
    w("   SE CORRE LA UNION DE LAS DOS, que es el lado prudente: si git ve uno")
    w("   que la tarea no declara, se corre igual.")
    lista = sorted(set(de_git) | set(DECLARADOS_POR_LA_TAREA))
    w("   CIFRA arneses que se van a correr: %d" % len(lista))
    w("")

    w("C) LAS TRES CIFRAS QUE EL ENCARGO MANDA PUBLICAR, SOBRE EL REPO DE HOY")
    w("   (no salen de esta corrida acotada: salen de las funciones del modulo)")
    _ult, faltan = B.arneses_que_faltan()
    invisibles = B.nomina_invisible_al_censo()
    sin_congelar = B.guarda_del_sujeto_congelado()
    w("   CIFRA entradas de la nomina: %d" % len(B.VIEJAS))
    w("   CIFRA arneses que el censo reconoce: %d" % len(B.arneses_del_directorio()))
    w("   CIFRA arneses DEL CENSO que se quedan FUERA de la nomina: %d" % len(faltan))
    for n in faltan:
        w("      FUERA DE LA NOMINA: %s" % n)
    if not faltan:
        w("      (ninguno)")
    w("   CIFRA entradas de la nomina SIN SUJETO CONGELADO: %d" % len(sin_congelar))
    for fila in sin_congelar:
        w("      SIN SUJETO CONGELADO: %s" % (fila,))
    if not sin_congelar:
        w("      (ninguna)")
    w("   CIFRA entradas de la nomina que el censo NO VE: %d" % len(invisibles))
    for n in invisibles:
        w("      INVISIBLE AL CENSO: %s" % n)
    if not invisibles:
        w("      (ninguna)")
    w("")

    w("D) LA CORRIDA ACOTADA, CADA ARNES DOS VECES (cotejo de la vuelta 141)")
    w("   LA MAQUINA ES LA DE LA BATERIA Y NO UNA COPIA: `correr_dos_veces()`")
    w("   sobre `DOCS_LOOP`, `clasificar()`, y la exencion de CASO DECLARADO con")
    w("   sus TRES condiciones (codigo declarado, estado NO MORDIO y LA MARCA")
    w("   dentro de la salida). Una copia de esa logica aqui diria manana otra")
    w("   cosa que la bateria.")
    w("")
    w("   %-52s %-6s %-16s %s" % ("arnes", "exit", "estado", "segundos"))
    perdidas, no_mordio, no_reprod, declarados = [], [], [], []
    t0 = time.monotonic()
    for nombre in lista:
        t_uno = time.monotonic()
        codigo, salida1, _escritos, inestables, _ruido = B.correr_dos_veces(
            nombre, B.DOCS_LOOP)
        estado = B.clasificar(codigo, salida1)
        declarado = B.CASOS_DECLARADOS.get(nombre)
        if (declarado and codigo == declarado[0] and estado == "NO MORDIO"
                and declarado[2] in salida1):
            estado = "CASO DECLARADO"
        if inestables:
            estado = "NO REPRODUCIBLE"
        w("   %-52s %-6s %-16s %.1f"
          % (nombre, codigo, estado, time.monotonic() - t_uno))
        if estado not in ("OK", "CASO DECLARADO"):
            w("        %s" % B.primera_linea_util(salida1))
        if estado == "ANCLA PERDIDA":
            perdidas.append(nombre)
        elif estado == "NO MORDIO":
            no_mordio.append(nombre)
        elif estado == "CASO DECLARADO":
            declarados.append(nombre)
        elif estado == "NO REPRODUCIBLE":
            no_reprod.append(nombre)
    minutos = (time.monotonic() - t0) / 60.0
    w("")
    w("   EL RELOJ, MEDIDO Y NO ESTIMADO: %.1f minutos de duracion monotona"
      % minutos)
    w("")

    w("E) LO QUE ESTA CORRIDA ACOTADA ENCUENTRA")
    w("   CIFRA arneses corridos: %d" % len(lista))
    w("   ANCLA PERDIDA  : %d (%s)"
      % (len(perdidas), ", ".join(perdidas) or "ninguna"))
    w("   NO MORDIO      : %d (%s)"
      % (len(no_mordio), ", ".join(no_mordio) or "ninguno"))
    w("   CASO DECLARADO : %d (%s)"
      % (len(declarados), ", ".join(declarados) or "ninguno"))
    w("   SIN REPRODUCIR : %d (%s)"
      % (len(no_reprod), ", ".join(no_reprod) or "ninguno"))
    w("")

    w("F) EL ESTADO AL SALIR, REMEDIDO Y NO SUPUESTO")
    c, numstat2 = git(["diff", "--numstat", "--", "dataset/"])
    filas_salida = [l for l in numstat2.splitlines() if l.strip()]
    w("   CIFRA filas de `git diff --numstat -- dataset/` AL SALIR: %d"
      % len(filas_salida))
    for l in filas_salida[:20]:
        w("      " + l)
    turno_salida = sha_de(TURNO)
    w("   %s al salir: %s" % (TURNO,
                              "%d bytes, sha256 LF %s"
                              % (turno_salida[0], turno_salida[2][:16])
                              if turno_salida else "NO EXISTE"))
    turno_igual = (turno_entrada == turno_salida)
    w("   LA SEDE DEL TURNO NO SE MOVIO: %s" % ("SI" if turno_igual else "NO"))
    w("   (es la que `vuelta192_tarea4_mutacion_cuarta_puerta.py` borraba antes de")
    w("    que la 194 lo arreglara, y por eso se remide aqui en vez de creerlo)")
    w("")

    w("G) EL VEREDICTO DE ESTA CORRIDA ACOTADA, Y SU ALCANCE")
    hay_rojo = bool(perdidas or no_mordio or no_reprod or faltan or invisibles
                    or sin_congelar)
    separada = B.guarda_del_sujeto_congelado_separada()
    clase = B.clase_del_rojo(perdidas, no_mordio, no_reprod, faltan, invisibles,
                             separada)
    w("   hay rojo: %s" % hay_rojo)
    w("   CLASE DEL VEREDICTO: %s | CIFRA exitcode: %d"
      % (clase, B.CODIGO_DE_LA_CLASE[clase]))
    w("   Y SU ALCANCE, DICHO PARA QUE NO SE CITE DE MAS: esto mide LOS %d"
      % len(lista))
    w("   ARNESES QUE ESTA VUELTA TOCO, no los %d de la nomina. La bateria entera"
      % len(B.VIEJAS))
    w("   cae en la 199 por la cadencia de AUDITOR.md 6.1.")
    w("")
    w("FIN")

    t = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)"
          % (os.path.relpath(SALIDA, RAIZ).replace("\\", "/"),
             len(t.encode("utf-8"))))
    return 0 if not hay_rojo and turno_igual else 1


if __name__ == "__main__":
    sys.exit(main())
