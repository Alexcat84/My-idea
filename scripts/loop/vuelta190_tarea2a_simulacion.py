# -*- coding: utf-8 -*-
r"""vuelta190_tarea2a_simulacion.py . LA SIMULACION PREVIA DE LA TAREA 2, SOBRE
COPIA EN MEMORIA Y ANTES DE TOCAR UNA SOLA LINEA DE
`scripts/loop/verificar_mutaciones_viejas.py`.

POR QUE EXISTE: la guarda de la casa dice **simulacion previa sobre copia en
memoria** antes de cambiar un instrumento. Este fichero NO escribe en
`scripts/loop/`, NO toca la nomina y NO cambia ningun veredicto: lee los textos de
los arneses **a memoria**, corre sobre ellos el PROTOTIPO de la separacion que la
TAREA 2.a va a meter en el fuente, y publica **lo que saldria**. Si lo que sale
aqui no es lo que el encargo espera, la TAREA 2 se replantea antes de tocar nada.

LO QUE SIMULA, Y SON LAS DOS MITADES DE LA TAREA:

  (a) LA SEPARACION. Hoy `guarda_del_sujeto_congelado()` devuelve **3 entradas sin
      congelar** y punto: no distingue una DEUDA (un arnes que explica por que
      nombra el sujeto vivo) de una DECISION SIN EXPLICAR. El encargo dice, con
      todas las letras, **mide cuantas de las tres traen motivo escrito, no lo
      supongas**. Aqui se mide.

  (b) EL VEREDICTO. Se computa lo que diria el instrumento de la nomina en los
      tres escenarios: con la guarda FUERA (que es lo que el `D.5` de la 189 hizo
      y el acta 190 tumbo en su `4.6`), con la guarda DENTRO sin separar (un rojo
      que no dice de que es), y con la guarda DENTRO Y SEPARADA, que es lo que se
      va a construir.

QUE ES `MOTIVO ESCRITO`, DICHO ANTES DE MEDIR PARA QUE NO SE AJUSTE A LO QUE
CONVENGA. Un `NO DECIDIBLE` sale asi porque su texto trae huellas de las DOS
especies: de sujeto congelado y de sujeto vivo. La pregunta que la `P.1` deja
abierta es si esa mezcla esta EXPLICADA o no. La vara: **por CADA aparicion de una
huella de vivo EN LA MAQUINA** (el fichero sin su docstring de modulo, que es
donde la guarda ya mira), se abre una ventana de +/- `VENTANA` lineas y se busca
una de las marcas literales de la casa que dicen que ese sujeto no es el fichero
de hoy. **Si TODAS las apariciones tienen su marca, la entrada trae MOTIVO
ESCRITO; si ALGUNA no la tiene, NO lo trae.** El lado seguro es ese: una apertura
del fichero vivo sin explicar es deuda, no decision.

USO:
  python scripts/loop/vuelta190_tarea2a_simulacion.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as VMV   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

# EL PROTOTIPO DE LO QUE VA AL FUENTE. Las marcas son LITERALES DE LA CASA: las
# cuatro primeras son formas de nombrar un sujeto que no se mueve (un blob de
# git, un objeto por su hash, un fichero congelado, una huella de contenido) y
# las dos ultimas son la declaracion expresa de que no se toca.
MARCAS_DE_MOTIVO = ("GIT SHOW", "CAT-FILE", "COMMIT", "SUJETO_FIJO", "SHA256",
                    "NO SE TOCA", "NO SE ESCRIBE")
VENTANA_DE_MOTIVO = 3


def motivo_del_sujeto_vivo(texto, marcas=None, ventana=None, huellas=None):
    """SI UN ARNES EXPLICA POR QUE NOMBRA EL SUJETO VIVO. PURA.

    Devuelve (tiene_motivo, evidencia), con evidencia como
    [(linea, huella, marcas_halladas)] sobre LA MAQUINA (sin el docstring de
    modulo), que es donde la guarda ya mira.

    `tiene_motivo` es True solo si TODAS las apariciones traen marca. Si no hay
    ninguna aparicion, devuelve (False, []) y quien llama decide: sin apariciones
    la pregunta no se plantea."""
    m = tuple(marcas) if marcas is not None else MARCAS_DE_MOTIVO
    v = VENTANA_DE_MOTIVO if ventana is None else ventana
    hs = tuple(huellas) if huellas is not None else VMV.HUELLAS_DE_VIVO
    maquina = VMV.sin_docstring_de_modulo(texto).split(NL)
    evidencia = []
    for i, linea in enumerate(maquina, 1):
        for h in hs:
            if h not in linea:
                continue
            a = max(1, i - v)
            b = min(len(maquina), i + v)
            ventana_texto = NL.join(maquina[a - 1:b]).upper()
            halladas = [x for x in m if x in ventana_texto]
            evidencia.append((i, h, halladas))
    if not evidencia:
        return False, []
    return all(bool(h) for _l, _hu, h in evidencia), evidencia


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 190, TAREA 2.a: SIMULACION PREVIA SOBRE COPIA EN MEMORIA")
    w("=" * 78)
    w("")
    w("ESTE FICHERO NO ESCRIBE EN scripts/loop/ Y NO TOCA LA NOMINA. Lee los")
    w("textos de los arneses A MEMORIA y corre sobre ellos el PROTOTIPO de la")
    w("separacion. El fuente sigue como estaba cuando esto corre.")
    w("")

    w("A) EL ESTADO DE HOY, MEDIDO Y NO RECORDADO")
    fuente = os.path.join(RAIZ, "scripts", "loop", "verificar_mutaciones_viejas.py")
    datos = io.open(fuente, "rb").read()
    w("   scripts/loop/verificar_mutaciones_viejas.py -> disco %d bytes | LF %d bytes"
      % (len(datos), len(datos.replace(b"\r\n", b"\n"))))
    w("   CIFRA nomina: %d | VARA_DEL_CENSO: %d" % (len(VMV.VIEJAS), VMV.VARA_DEL_CENSO))
    malas = VMV.guarda_del_sujeto_congelado()
    w("   guarda_del_sujeto_congelado() HOY: %d entradas" % len(malas))
    for nombre, veredicto, vive in malas:
        w("      %-14s %-52s abre: %s" % (veredicto, nombre, ", ".join(vive)))
    w("   SU FIRMA: tuplas de %d campos. NO trae ninguna cifra de motivo escrito,"
      % (len(malas[0]) if malas else -1))
    w("   asi que una deuda y una decision salen exactamente iguales.")
    w("   arneses_que_faltan(): %s" % (VMV.arneses_que_faltan(),))
    w("   nomina_invisible_al_censo(): %s" % (VMV.nomina_invisible_al_censo(),))
    w("")

    w("B) LA VARA DEL MOTIVO ESCRITO, DECLARADA ANTES DE MEDIR")
    w("   marcas literales (%d): %s" % (len(MARCAS_DE_MOTIVO),
                                        ", ".join(repr(x) for x in MARCAS_DE_MOTIVO)))
    w("   ventana: +/- %d lineas sobre LA MAQUINA (sin el docstring de modulo)"
      % VENTANA_DE_MOTIVO)
    w("   huellas de vivo que se buscan: %s" % ", ".join(VMV.HUELLAS_DE_VIVO))
    w("   regla: TODAS las apariciones con marca -> MOTIVO ESCRITO. ALGUNA sin")
    w("   marca -> SIN MOTIVO ESCRITO. El lado seguro es ese.")
    w("")

    w("C) LA SEPARACION, CORRIDA SOBRE LOS TEXTOS EN MEMORIA")
    con_motivo, sin_motivo = [], []
    for nombre, veredicto, vive in malas:
        texto = VMV.texto_del_arnes(nombre)
        tiene, evidencia = motivo_del_sujeto_vivo(texto)
        w("   %s" % nombre)
        w("      veredicto de la guarda: %s | abre: %s" % (veredicto, ", ".join(vive)))
        w("      apariciones de una huella de vivo EN LA MAQUINA: %d" % len(evidencia))
        for ln, h, marcas in evidencia:
            w("         linea %-5d huella %-34s marcas en su ventana: %s"
              % (ln, h, ", ".join(marcas) or "(NINGUNA)"))
        w("      MOTIVO ESCRITO: %s" % ("SI" if tiene else "NO"))
        (con_motivo if tiene else sin_motivo).append(nombre)
    w("")
    w("   CIFRA `NO DECIDIBLE` CON MOTIVO ESCRITO: %d" % len(con_motivo))
    for n in con_motivo:
        w("      %s" % n)
    w("   CIFRA `NO DECIDIBLE` SIN MOTIVO ESCRITO: %d" % len(sin_motivo))
    for n in sin_motivo:
        w("      %s" % n)
    if not sin_motivo:
        w("      (ninguna, y el cero va escrito)")
    w("")

    w("D) EL PROTOTIPO CAE SOBRE UN ARNES FABRICADO QUE NO EXPLICA NADA")
    w("   (si la vara no distinguiera, no serviria de vara. Aqui se prueba antes")
    w("    de meterla en el fuente)")
    fabricado_sin = (chr(34) * 3 + "Un arnes de mentira." + chr(34) * 3 + NL
                     + "import io" + NL
                     + "t = io.open('docs/loop/REPORTE.md').read()" + NL
                     + "print(len(t))" + NL)
    fabricado_con = (chr(34) * 3 + "Otro arnes de mentira." + chr(34) * 3 + NL
                     + "import subprocess" + NL
                     + "COMMIT = 'abc1234'" + NL
                     + "r = subprocess.run(['git', 'show', COMMIT + ':docs/loop/REPORTE.md'])" + NL)
    for etiqueta, txt, esperado in (("fabricado SIN explicacion", fabricado_sin, False),
                                    ("fabricado CON git show y COMMIT", fabricado_con, True)):
        tiene, ev = motivo_del_sujeto_vivo(txt)
        w("   %-34s -> MOTIVO ESCRITO %-3s (esperado %-3s) -> %s"
          % (etiqueta, "SI" if tiene else "NO", "SI" if esperado else "NO",
             "PASA" if tiene == esperado else "CAE"))
        for ln, h, marcas in ev:
            w("      linea %d, huella %s, marcas: %s" % (ln, h, ", ".join(marcas) or "(NINGUNA)"))
    w("")

    w("E) LOS TRES VEREDICTOS QUE SE PUEDEN ESCRIBIR, COMPUTADOS SOBRE LO MEDIDO")
    _u, faltan = VMV.arneses_que_faltan()
    invis = VMV.nomina_invisible_al_censo()
    hay_fallo = bool(faltan or invis)
    w("   piezas de FALLO en este momento (censo y nomina): faltan %d, invisibles %d"
      % (len(faltan), len(invis)))
    w("   piezas de DEUDA en este momento: %d con motivo, %d sin motivo"
      % (len(con_motivo), len(sin_motivo)))
    w("")
    w("   (1) CON LA GUARDA FUERA DEL VEREDICTO, que es lo que el `D.5` de la 189")
    w("       hizo y el acta 190 TUMBA en su `4.6`:")
    w("          VEREDICTO: %s" % ("ROJO" if hay_fallo else "VERDE"))
    w("          y las %d entradas sin congelar quedan publicadas arriba y FUERA"
      % len(malas))
    w("          del veredicto. Quien mire solo el veredicto NO TIENE SINTOMA.")
    w("   (2) CON LA GUARDA DENTRO PERO SIN SEPARAR, que es como estaba antes:")
    w("          VEREDICTO: %s" % ("ROJO" if (hay_fallo or malas) else "VERDE"))
    w("          pero el rojo NO DICE DE QUE ES: un arnes caido y una deuda")
    w("          declarada salen con el mismo color y el mismo exitcode.")
    w("   (3) CON LA GUARDA DENTRO Y SEPARADA, que es lo que la TAREA 2 construye:")
    clase = ("ROJO POR FALLO" if hay_fallo else
             ("ROJO POR DEUDA DECLARADA" if malas else "VERDE"))
    w("          VEREDICTO: %s" % clase)
    w("          con %d de deuda (%d con motivo escrito, %d sin) y %d de fallo."
      % (len(malas), len(con_motivo), len(sin_motivo),
         len(faltan) + len(invis)))
    w("          SIGUE SIENDO ROJO. No se afloja nada: lo que cambia es que el")
    w("          rojo dice de que especie es.")
    w("")

    w("F) EL ARBOL, DESPUES DE ESTA SIMULACION")
    import subprocess
    r = subprocess.run(["git", "status", "--porcelain", "--",
                        "scripts/loop/verificar_mutaciones_viejas.py"],
                       cwd=RAIZ, capture_output=True)
    filas = [l for l in r.stdout.decode("utf-8", errors="replace").splitlines()
             if l.strip()]
    w("   git status sobre el fuente que se va a tocar: %d fila(s) %s"
      % (len(filas), filas))
    w("   O SEA: la simulacion NO lo ha tocado, que es lo que tenia que probar.")
    w("")

    texto = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V190_T2A_SIMULACION.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(texto.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
