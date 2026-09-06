# -*- coding: utf-8 -*-
r"""vuelta188_tarea3c_nomina.py . LA NOMINA AL CERRAR, Y LA DOBLE CORRIDA QUE
YA NO RE CORRE UN ARNES QUE SALIO EN ROJO EN ESTA MISMA VUELTA.

CLON DECLARADO de `scripts/loop/vuelta187_tarea5a_nomina.py`. Cambia la lista de
arneses, el nombre de la salida, las glosas, y ANADE la exclusion por rojo de la
`C.3`. El cotejo del clon lo hace `scripts/loop/cotejar_clon_declarado.py` y su
salida se pega en el reporte con lo que salga: AQUI NO SE AFIRMA QUE NINGUN DIFF
SALGA VACIO.

QUIEN ENCARGA LA EXCLUSION Y CON QUE PALABRAS. La `C.3` del acta 188, que el
auditor levanto y el ejecutor no trajo. La letra rota es la del encargo
permanente sobre un arnes YA SELLADO que cae en rojo: *"te detienes ahi, lo traes
con su salida entera, **sin re-correrlo** y sin arreglarlo"*. En la vuelta 187
`vuelta186_tarea2c_mutacion_cierre_tardio.py` cayo en rojo y **se corrio DOS
VECES MAS** dentro de la doble corrida de la 5.a. **Y no hubo choque de ordenes**:
la 5.a pide *"corre cada arnes NUEVO dos veces"*, y ese arnes no era nuevo.

EL REMEDIO, Y SU MITAD QUE IMPORTA. La doble corrida **excluye explicitamente
cualquier arnes que ya haya salido en rojo en esa misma vuelta**, y **LO DICE EN
SU SALIDA** con el nombre del excluido y el motivo. **Una exclusion muda seria
peor que el problema**, porque un arnes que no corre y no se nombra parece un
arnes que corrio.

DE DONDE SALEN LOS ROJOS, Y NO SE TECLEAN. De un REGISTRO en disco,
`docs/loop/ROJOS_DE_LA_VUELTA_<N>.txt`, una linea por arnes con la forma
`script | ruta de su salida en rojo | motivo`. **Si el fichero no existe, la
exclusion es VACIA y eso tambien se declara**, con esas palabras, en vez de
callarse: un cero que no se publica no se puede auditar.

Y LA LETRA QUE EL ACTA 188 ADJUDICA EN SU `5.3`, ESCRITA AQUI PARA QUE NO SE
RE LITIGUE: **un arnes sellado en rojo detiene AL ARNES, no a la vuelta**; la
vuelta se cierra con la parada declarada.

ESTE FICHERO NO ES UN ARNES DE MUTACION Y NO ENTRA EN LA NOMINA, y esa afirmacion
SE MIDE aqui abajo en vez de dejarse dicha.

NO SE PODA NADA. La opcion `c` de la parada del 5 sep 2026 quedo RECHAZADA por el
fundador. Aqui la nomina CRECE.

USO:
  python scripts/loop/vuelta188_tarea3c_nomina.py
"""
import hashlib
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as VMV   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
PY = sys.executable
VUELTA = 188
REGISTRO_ROJOS = "docs/loop/ROJOS_DE_LA_VUELTA_%d.txt" % VUELTA

LOS_QUE_CORREN = [
    ("scripts/loop/vuelta188_tarea2_mutacion_pata_documental.py",
     "docs/loop/SALIDA_V188_T2_MUTACION_PATA_DOCUMENTAL.txt", "NACE HOY"),
    ("scripts/loop/vuelta188_tarea3c_mutacion_exclusion_por_rojo.py",
     "docs/loop/SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt", "NACE HOY"),
    ("scripts/loop/vuelta188_tarea4_mutacion_cobertura_parejas.py",
     "docs/loop/SALIDA_V188_T4_MUTACION_COBERTURA_PAREJAS.txt", "NACE HOY"),
    ("scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py",
     "docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt",
     "de la 186, REESCRITO HOY por el acta 188 punto 7.1"),
    ("scripts/loop/vuelta186_tarea2a_mutacion_pieza4.py",
     "docs/loop/SALIDA_V186_T2A_MUTACION_PIEZA4.txt",
     "de la 186, TOCADO HOY por la TAREA 3.b"),
]


def rojos_registrados(texto):
    """LOS ARNESES QUE YA SALIERON EN ROJO EN ESTA VUELTA, LEIDOS DEL REGISTRO.

    Devuelve [(script, ruta_de_su_salida, motivo)]. **PURA**: recibe el texto y
    no lee ni escribe nada, para que su caso rojo se pueda tumbar sobre registros
    fabricados en memoria sin tocar el disco.

    Las lineas vacias y las que empiezan por almohadilla se saltan, para que el
    registro pueda llevar su propia cabecera explicativa. Una linea que no traiga
    sus tres campos separados por barra sale con motivo `(sin motivo declarado)`,
    y quien llama la trata igual que a las demas: **el arnes se excluye
    igualmente, porque no correrlo es lo prudente, pero la salida dice que su
    motivo no estaba escrito.**"""
    salida = []
    for linea in (texto or "").replace(chr(13) + NL, NL).split(NL):
        l = linea.strip()
        if not l or l.startswith("#"):
            continue
        trozos = [x.strip() for x in l.split("|")]
        script = trozos[0]
        ruta = trozos[1] if len(trozos) > 1 and trozos[1] else "(sin salida declarada)"
        motivo = trozos[2] if len(trozos) > 2 and trozos[2] else "(sin motivo declarado)"
        salida.append((script, ruta, motivo))
    return salida


def particion_por_rojo(los_que_corren, rojos):
    """LA DOBLE CORRIDA, PARTIDA EN DOS: los que se corren y los EXCLUIDOS.

    Devuelve (corren, excluidos), donde `excluidos` es
    [(script, salida, origen, ruta_del_rojo, motivo)]. **PURA.**

    LA COMPARACION ES POR NOMBRE DE FICHERO Y NO POR RUTA COMPLETA, a proposito:
    el registro puede escribir la ruta con barras de un sistema o de otro, y un
    arnes que se salva de la exclusion por una barra seria exactamente la
    especie de descuido que esta funcion existe para impedir."""
    por_base = {}
    for script, ruta, motivo in rojos:
        por_base[os.path.basename(script.replace("\\", "/"))] = (ruta, motivo)
    corren, excluidos = [], []
    for script, salida, origen in los_que_corren:
        base = os.path.basename(script.replace("\\", "/"))
        if base in por_base:
            ruta, motivo = por_base[base]
            excluidos.append((script, salida, origen, ruta, motivo))
        else:
            corren.append((script, salida, origen))
    return corren, excluidos


def sha_de(ruta):
    """LAS DOS CONVENCIONES Y LOS DOS sha256 DE UN FICHERO, o None si no esta."""
    if not os.path.isfile(ruta):
        return None
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(chr(13).encode() + chr(10).encode(), chr(10).encode())
    return (hashlib.sha256(datos).hexdigest(), hashlib.sha256(lf).hexdigest(),
            len(datos), len(lf))


def numstat(ruta_rel):
    """LAS FILAS DE `git diff --numstat` DE UNA RUTA, contadas."""
    r = subprocess.run(["git", "diff", "--numstat", "--", ruta_rel],
                       cwd=RAIZ, capture_output=True)
    return [l for l in r.stdout.decode("utf-8", errors="replace").splitlines()
            if l.strip()]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 3.c: LA NOMINA, Y LA DOBLE CORRIDA CON EXCLUSION POR ROJO"
      % VUELTA)
    w("=" * 78)
    w("")

    w("A) LA NOMINA Y EL CENSO, RECOMPUTADOS AL CERRAR")
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
    dentro = set(nomina)
    n_dentro = 0
    w("   LOS QUE ESTA VUELTA MANDA CORRER, COMPROBADOS DENTRO DE LA NOMINA:")
    for script, _sal, origen in LOS_QUE_CORREN:
        base = os.path.basename(script)
        esta = base in dentro
        n_dentro += 1 if esta else 0
        w("      %-56s %-42s en la nomina: %s"
          % (base, origen, "SI" if esta else "NO"))
    w("   CIFRA de esos que estan dentro: %d de %d" % (n_dentro, len(LOS_QUE_CORREN)))
    w("   Y ESTE FICHERO NO ENTRA EN LA NOMINA, Y SE MIDE EN VEZ DE DECIRSE:")
    yo = os.path.basename(os.path.abspath(__file__))
    w("      %s esta en el censo de arneses: %s" % (yo, "SI" if yo in censo else "NO"))
    w("      %s esta en la nomina: %s" % (yo, "SI" if yo in dentro else "NO"))
    w("")

    w("B) LA EXCLUSION POR ROJO, QUE ES LA `C.3` DEL ACTA 188")
    w("   (la letra rota decia `sin re-correrlo`, y en la 187 un arnes sellado en")
    w("    rojo se corrio DOS VECES MAS dentro de la doble corrida. Aqui la doble")
    w("    corrida los EXCLUYE y LO DICE: una exclusion muda seria peor)")
    p_reg = os.path.join(RAIZ, REGISTRO_ROJOS.replace("/", os.sep))
    existe = os.path.isfile(p_reg)
    texto_reg = io.open(p_reg, encoding="utf-8").read() if existe else ""
    w("   registro: %s" % REGISTRO_ROJOS)
    if existe:
        s = sha_de(p_reg)
        w("      existe: SI | disco %d bytes | LF %d bytes | sha256 LF %s"
          % (s[2], s[3], s[1]))
    else:
        w("      existe: NO. **LA EXCLUSION ES VACIA Y SE DECLARA CON ESAS")
        w("      PALABRAS**: ningun arnes sellado ha salido en rojo en esta vuelta,")
        w("      asi que no hay nada que excluir. Un cero que no se publica no se")
        w("      puede auditar.")
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

    w("C) LA DOBLE CORRIDA, EN PROCESOS APARTE, EXIGIENDO EL MISMO sha256")
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

    w("D) EL ESTADO DEL ARBOL DESPUES DE LA DOBLE CORRIDA")
    r = subprocess.run(["git", "diff", "--numstat", "--", "dataset/"],
                       cwd=RAIZ, capture_output=True)
    filas_ds = [l for l in r.stdout.decode("utf-8", errors="replace").splitlines()
                if l.strip()]
    w("   CIFRA filas de `git diff --numstat -- dataset/`: %d" % len(filas_ds))
    for f in filas_ds:
        w("      %s" % f)
    w("")

    ok = (len(faltan) == 0 and not invis and not malas
          and n_dentro == len(LOS_QUE_CORREN) and paradas == 0)
    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%d_T3C_NOMINA.txt" % VUELTA)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
