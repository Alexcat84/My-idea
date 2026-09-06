# -*- coding: utf-8 -*-
r"""vuelta190_tarea2_nomina.py . LA NOMINA CON LA GUARDA DEL SUJETO CONGELADO DE
VUELTA EN EL VEREDICTO, Y CON LA DEUDA SEPARADA DEL FALLO.

QUIEN LO ENCARGA, Y ES EL UNICO DISCUTIBLE QUE EL ACTA 190 TUMBA. La `4.6`:
*"dejar `guarda_del_sujeto_congelado()` FUERA DEL VEREDICTO. EN CONTRA, Y ES EL
UNICO QUE TUMBO"*. El `D.5` de la 189 la saco del veredicto de
`scripts/loop/vuelta189_tarea2_nomina.py` con un motivo real (un rojo que enrojece
cada vuelta entrena a mirarlo con desgana), pero **publicar los tres nombres
arriba y cerrar en verde deja sin sintoma al que solo mire el veredicto**, y eso
es convertir una deuda visible en una exencion.

LA MAQUINA NO SE CLONA, SE IMPORTA (`6.6` del acta 172): `rojos_registrados`,
`particion_por_rojo`, `sha_de` y `numstat` vienen de
`scripts/loop/vuelta188_tarea3c_nomina.py`, que es donde nacieron. La separacion y
la clase del veredicto vienen de `verificar_mutaciones_viejas.py`, donde la TAREA
2.a de esta vuelta las escribio.

QUE CAMBIA RESPECTO AL DE LA 189, Y SON DOS COSAS QUE VAN JUNTAS:

  (a) SE PUBLICAN LAS DOS CIFRAS DE LA DEUDA, CON SUS NOMBRES. Hoy "3 entradas sin
      congelar" no distingue una DEUDA (un arnes que EXPLICA por que nombra el
      sujeto vivo) de una DECISION SIN EXPLICAR. Es la `P.1` que el acta 189 dejo
      encargada en su `4.7`.

  (b) LA GUARDA VUELVE AL VEREDICTO, Y EL VEREDICTO DICE DE QUE ESPECIE ES SU
      ROJO. `VERDE`, `ROJO POR FALLO` o `ROJO POR DEUDA DECLARADA`, con exitcode
      0, 1 y 2. **Los dos rojos siguen siendo rojos y los dos siguen siendo
      distintos de cero: no se afloja ninguna guarda.**

NO SE CORRE LA BATERIA. La 189 la corrio entera y por `AUDITOR.md` 6.1 la
siguiente cae en la 194. Aqui se mide la nomina y se corre la doble corrida de los
arneses que nacen HOY, nada mas.

NO SE PODA NADA. La opcion `c` de la parada del 5 sep 2026 quedo RECHAZADA por el
fundador.

USO:
  python scripts/loop/vuelta190_tarea2_nomina.py
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

# LOS QUE ESTA VUELTA MANDA CORRER DOS VECES AQUI: el arnes que NACE EN ESTA
# TAREA. La bateria NO se corre, asi que esta lista no lleva ningun sellado viejo.
# EL ARNES DE LA TAREA 3 NO ESTA AQUI A PROPOSITO, y se dice por que: su doble
# corrida vive en su propia tarea, y meterlo aqui obligaria a re escribir esta
# salida sellada cuando la TAREA 3 cierre, que es exactamente la especie que la
# `4.9` del acta 190 manda dejar de hacer.
LOS_QUE_CORREN = [
    ("scripts/loop/vuelta190_tarea2b_mutacion_deuda_y_fallo.py",
     "docs/loop/SALIDA_V190_T2B_MUTACION_DEUDA_Y_FALLO.txt",
     "NACE HOY, TAREA 2: la deuda separada del fallo y la guarda enchufada"),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2: LA NOMINA CON LA GUARDA DE VUELTA EN EL VEREDICTO"
      % VUELTA)
    w("=" * 78)
    w("")

    w("A) LA NOMINA Y EL CENSO, RECOMPUTADOS AHORA")
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
    w("")

    w("B) LA GUARDA DEL SUJETO CONGELADO, SIN SEPARAR Y SEPARADA")
    malas = VMV.guarda_del_sujeto_congelado()
    w("   guarda_del_sujeto_congelado(): %d entradas sin congelar" % len(malas))
    for nombre, veredicto, vive in malas:
        w("      SUJETO SIN CONGELAR: %-46s %s" % (nombre, veredicto))
    w("   ESO ES LO QUE SE PUBLICABA HASTA HOY, Y NO DISTINGUE UNA DEUDA DE UNA")
    w("   DECISION. La `P.1` del acta 189, en su `4.7`, pedia separarlas.")
    w("")
    w("   LA VARA DEL MOTIVO ESCRITO, DECLARADA ANTES DE MEDIR:")
    w("      marcas literales (%d): %s"
      % (len(VMV.MARCAS_DE_MOTIVO), ", ".join(VMV.MARCAS_DE_MOTIVO)))
    w("      ventana: +/- %d lineas sobre LA MAQUINA (sin docstring de modulo)"
      % VMV.VENTANA_DE_MOTIVO)
    w("      regla: TODAS las apariciones con marca -> MOTIVO ESCRITO; ALGUNA sin")
    w("             marca -> SIN MOTIVO ESCRITO. El lado seguro es ese.")
    sep = VMV.guarda_del_sujeto_congelado_separada()
    for clave, etiqueta in (
            ("sujeto_vivo", "SUJETO VIVO (es FALLO, no deuda)"),
            ("con_motivo", "NO DECIDIBLE CON MOTIVO ESCRITO (deuda declarada)"),
            ("sin_motivo", "NO DECIDIBLE SIN MOTIVO ESCRITO (deuda sin declarar)")):
        w("   CIFRA %s: %d" % (etiqueta, len(sep[clave])))
        for nombre, _v, _vv, evidencia in sep[clave]:
            w("      %s" % nombre)
            for ln, h, marcas in evidencia:
                w("         linea %-5d huella %-32s marcas: %s"
                  % (ln, h, ", ".join(marcas) or "(NINGUNA)"))
        if not sep[clave]:
            w("      (ninguna, y el cero va escrito)")
    suma = sum(len(sep[k]) for k in sep)
    w("   LA SUMA DE LAS TRES ES %d Y LA GUARDA SIN SEPARAR DA %d: %s"
      % (suma, len(malas), "CALZA" if suma == len(malas) else "NO CALZA"))
    w("   Y NO SE EXIME A NADIE: las tres listas cuentan para el veredicto.")
    w("")

    w("C) LA EXCLUSION POR ROJO")
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
        w("      (esta vuelta NO corre la bateria, asi que ningun arnes ha salido")
        w("       en rojo por ella. El cero va escrito, no omitido)")
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
    if not excluidos:
        w("      (ninguno excluido, y el cero va escrito)")
    w("   CIFRA arneses que SI se corren dos veces: %d de %d"
      % (len(corren), len(LOS_QUE_CORREN)))
    w("")

    w("D) LA DOBLE CORRIDA, EN PROCESOS APARTE, EXIGIENDO EL MISMO sha256")
    paradas = 0
    caidos = []
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
                caidos.append(script)
        iguales = shas[0] is not None and shas[0] == shas[1]
        w("      LAS DOS CORRIDAS DAN EL MISMO sha256: %s" % ("SI" if iguales else "NO"))
        if not iguales:
            w("      PARADA: esta salida CAMBIA SOLA. Se trae sin arreglarla.")
            paradas += 1
            caidos.append(script)
        filas = numstat(salida)
        w("      git diff --numstat -- %s : %d fila(s)" % (salida, len(filas)))
    w("")
    w("   CIFRA paradas: %d" % paradas)
    w("")

    w("E) EL ESTADO DEL ARBOL DESPUES DE TODO")
    r = subprocess.run(["git", "diff", "--numstat", "--", "dataset/"],
                       cwd=RAIZ, capture_output=True)
    filas_ds = [l for l in r.stdout.decode("utf-8", errors="replace").splitlines()
                if l.strip()]
    w("   CIFRA filas de `git diff --numstat -- dataset/`: %d" % len(filas_ds))
    for f in filas_ds:
        w("      %s" % f)
    w("")

    # EL VEREDICTO MIRA LA GUARDA, Y ESA ES LA `4.6` DEL ACTA 190 EJECUTADA. El
    # `D.5` de la 189 la saco de aqui; el acta lo tumba. Y no vuelve como estaba:
    # vuelve SEPARADA, para que el rojo diga de que especie es sin dejar de ser
    # rojo.
    clase = VMV.clase_del_rojo([], caidos, [], faltan, invis, sep)
    codigo = VMV.CODIGO_DE_LA_CLASE[clase]
    w("F) EL VEREDICTO, CON LA GUARDA DENTRO Y CON SU ESPECIE DICHA")
    w("   piezas de FALLO: %d arneses caidos, %d fuera de la nomina, %d invisibles"
      % (len(caidos), len(faltan), len(invis)))
    w("      y %d SUJETO VIVO, que cuenta como fallo y no como deuda"
      % len(sep["sujeto_vivo"]))
    w("   piezas de DEUDA DECLARADA: %d con motivo escrito, %d sin motivo escrito"
      % (len(sep["con_motivo"]), len(sep["sin_motivo"])))
    w("   LA PRECEDENCIA VA ESCRITA: EL FALLO GANA. Publicar deuda habiendo un")
    w("   arnes caido seria la misma degradacion silenciosa, pero al reves.")
    w("")
    w("   Y AQUI VA LA COMPARACION QUE HACE VISIBLE LO QUE LA `4.6` ARREGLA:")
    vacia = {"sujeto_vivo": [], "con_motivo": [], "sin_motivo": []}
    clase_sin = VMV.clase_del_rojo([], caidos, [], faltan, invis, vacia)
    w("      CON la guarda DENTRO del veredicto (hoy): %s, exitcode %d"
      % (clase, codigo))
    w("      SIN la guarda, que es lo que el `D.5` de la 189 hacia: %s, exitcode %d"
      % (clase_sin, VMV.CODIGO_DE_LA_CLASE[clase_sin]))
    w("      LAS DOS SON DISTINTAS: %s. Si fueran iguales, la guarda no estaria"
      % ("SI" if clase != clase_sin else "NO"))
    w("      enchufada y esto no probaria nada.")
    w("")
    w("VEREDICTO: %s" % clase)
    w("CIFRA exitcode: %d" % codigo)
    w("   (%s. Los dos rojos siguen siendo distintos de cero: no se afloja nada)"
      % ("y sigue siendo ROJO" if codigo else "verde"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%d_T2_NOMINA.txt" % VUELTA)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return codigo


if __name__ == "__main__":
    sys.exit(main())
