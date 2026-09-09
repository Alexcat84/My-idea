# -*- coding: utf-8 -*-
r"""_v215_t4_dos_puntos.py . LOS DOS PUNTOS QUE OP-I-01 DEJO EN A MEDIAS,
MEDIDOS Y NO CERRADOS A OJO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3). No
vigila nada, no entra en ninguna nomina y muere con la vuelta.

QUE NO HACE, Y ES LO PRIMERO: NO ESCRIBE NI UNA LINEA EN NINGUNA FICHA. No toca
docs/plan/OPERACIONES.jsonl, y menos el campo estado (TAREA 4.c). Solo mide y
publica, y la guarda del final comprueba el sha256 del expediente a los dos
lados para probarlo en vez de prometerlo.

EL PUNTO 3, POR SU NEGATIVA (adjudicacion 5.4 del acta 214, linea 76174). La
vuelta 214 dijo que una busqueda negativa no se puede citar y el auditor lo
adjudico CONTRA el ejecutor: lo que AUDITOR.md 2 prohibe es AFIRMAR UNA BUSQUEDA
NO CORRIDA, no publicar la que da cero. Aqui se CORRE la busqueda y se publica
su cero CON EL COMANDO DELANTE.

  QUE SE BUSCA, Y LA ELECCION ES MIA Y SE DICE. La clausula pide que todo hueco
  vaya NOMBRADO y NUNCA RELLENADO. Un hueco RELLENADO es un campo que, en vez de
  decir que no hay dato, trae un relleno que no es dato: por eso la busqueda es
  el VOCABULARIO DE RELLENO de abajo, mas los campos VACIOS, que no estan
  nombrados ni tampoco rellenados y por eso se cuentan aparte. EL VOCABULARIO ES
  MIO Y VA ESCRITO PARA QUE SE PUEDA DISCUTIR: una lista que nadie puede leer no
  se puede auditar.

EL PUNTO 4, MIDIENDO ANTES DE DECIDIR (adjudicacion 5.5, linea 76183). NO SE
INVENTA LA SEDE: se busca en TODO el arbol de scripts quien ESCRIBE la vista
humana, y el resultado se publica sea cual sea, incluido que no exista.

USO:  python scripts/loop/_v215_t4_dos_puntos.py
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INV = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
VISTA = os.path.join(RAIZ, "docs", "plan", "10_INVENTARIO.md")
EXPEDIENTE = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

# EL VOCABULARIO DE RELLENO. ES MIO Y SE DICE QUE LO ES. Un relleno es un texto
# que ocupa el sitio de un dato sin serlo. Se compara sobre el campo ENTERO,
# normalizado a minusculas y sin espacios de los bordes, NUNCA por subcadena:
# buscar "-" dentro de un texto daria que si en casi cualquier campo, y esa es
# la especie de sonda mas laxa que su clausula que me cazo la D.7 en la 214.
RELLENOS = ("n/a", "na", "tbd", "todo", "xxx", "???", "?", "-", "--", "...",
            "por definir", "por completar", "pendiente", "sin datos",
            "sin dato", "no disponible", "placeholder", "lorem ipsum",
            "por determinar", "desconocido", "ninguno", "null", "none")

# LA MARCA QUE LA CLAUSULA PIDE, LEIDA DE LA PROPIA VISTA HUMANA Y NO INVENTADA:
# "se escribe como HUECO NOMBRADO, no se rellena".
MARCA_HUECO = "HUECO"


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def sha(ruta):
    b = io.open(ruta, "rb").read()
    return hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16]


def entradas():
    fuera = []
    for l in io.open(INV, encoding="utf-8"):
        l = l.strip()
        if l:
            fuera.append(json.loads(l))
    return fuera


def es_relleno(valor):
    """UN CAMPO ES RELLENO SI SU TEXTO ENTERO ES UNO DEL VOCABULARIO. PURA.
    Se compara el campo COMPLETO, nunca por subcadena."""
    if not isinstance(valor, str):
        return False
    return valor.strip().lower() in RELLENOS


def es_vacio(valor):
    """UN CAMPO VACIO NO ESTA NOMBRADO NI RELLENADO. PURA."""
    return isinstance(valor, str) and valor.strip() == ""


def vocabulario_del_campo(datos, campo):
    """TODOS LOS VALORES DISTINTOS QUE UN CAMPO TIENE EN EL FICHERO. PURA."""
    return sorted({str(e[campo]).strip() for e in datos if campo in e})


def es_del_vocabulario(datos, campo, valor):
    """UNA PALABRA SOSPECHOSA NO ES RELLENO SI EL PROPIO CAMPO LA USA COMO
    ESTADO, Y ESO SE MIDE, NO SE OPINA. PURA.

    CORRECCION DECLARADA DE ESTA VUELTA (caida `D.2` de la 215), Y NO TAPA LO
    QUE CORRIGE. La primera corrida de esta sonda conto SEIS campos de relleno,
    los seis con el valor 'pendiente' en el campo `estado`, y publicaba por eso
    un NO CUBRE. ERA UNA ALARMA FALSA DE LA MISMA ESPECIE QUE LA `D.7` DE LA
    214: la sonda era MAS LAXA QUE SU CLAUSULA. En `estado`, 'pendiente' NO
    ocupa el sitio de un dato: ES el dato, porque ese campo tiene vocabulario
    propio de estados.

    LA PRUEBA NO ES MI OPINION, ES UNA CIFRA: el mismo campo trae, en otras
    entradas, la forma LARGA de ese mismo estado ('pendiente, se resuelve por
    continua o repite'), o sea que la corta es la misma palabra abreviada.

    LA REGLA, MECANICA: una palabra sospechosa en el campo F se descarta como
    relleno si el propio campo F tiene, en OTRA entrada, un valor que EMPIEZA
    por esa palabra y sigue con mas texto. Si no lo tiene, sigue contando como
    relleno. LA REGLA NO SE ENSANCHA PARA QUE TRAGUE: pide la forma larga en el
    MISMO campo, no en cualquiera."""
    corto = str(valor).strip().lower()
    largas = [v for v in vocabulario_del_campo(datos, campo)
              if v.lower() != corto and v.lower().startswith(corto)
              and len(v) > len(corto)]
    return largas


def main():
    sha_exp_antes = sha(EXPEDIENTE)
    fallos = 0
    print("=" * 78)
    print("VUELTA 215, TAREA 4. LOS DOS PUNTOS DE OP-I-01 QUE QUEDARON A MEDIAS")
    print("=" * 78)
    print("SHA256 LF DE docs/plan/OPERACIONES.jsonl AL ENTRAR: %s" % sha_exp_antes)
    print("")

    # ------------------------------------------------------------- PUNTO 3
    print("=" * 78)
    print("4.a. EL PUNTO 3, POR SU NEGATIVA, CORRIDA Y CON SU CERO DELANTE")
    print("=" * 78)
    print("LA CLAUSULA, PEGADA DE LA VISTA HUMANA Y NO PARAFRASEADA:")
    vista = io.open(VISTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
    for i, l in enumerate(vista.split(NL), 1):
        if "HUECO NOMBRADO" in l:
            print("   docs/plan/10_INVENTARIO.md linea %d: %s" % (i, l.strip()))
    print("")
    print("EL COMANDO DE LA BUSQUEDA, ESCRITO ANTES DE SU RESULTADO:")
    print("   por cada entrada de docs/plan/INVENTARIO.jsonl y por cada uno de")
    print("   sus campos de texto, se pregunta si el campo ENTERO, en")
    print("   minusculas y sin espacios de los bordes, es una de estas %d"
          % len(RELLENOS))
    print("   palabras de relleno, y aparte si esta VACIO:")
    print("   VOCABULARIO: %s" % ", ".join(RELLENOS))
    print("")
    datos = entradas()
    rellenos, descartados, vacios = [], [], []
    con_hueco_may, con_hueco_ins = 0, 0
    for k, e in enumerate(datos, 1):
        if any(MARCA_HUECO in str(v) for v in e.values()):
            con_hueco_may += 1
        if any(MARCA_HUECO in str(v).upper() for v in e.values()):
            con_hueco_ins += 1
        for campo, valor in e.items():
            if es_relleno(valor):
                largas = es_del_vocabulario(datos, campo, valor)
                destino = descartados if largas else rellenos
                destino.append((k, e.get("nombre", "(sin nombre)"), campo,
                                valor, largas))
            if es_vacio(valor):
                vacios.append((k, e.get("nombre", "(sin nombre)"), campo))
    print("CIFRA entradas de docs/plan/INVENTARIO.jsonl: %d" % len(datos))
    print("CIFRA campos de texto examinados: %d"
          % sum(1 for e in datos for v in e.values() if isinstance(v, str)))
    print("LAS DOS CONVENCIONES DE CONTAR LA MARCA, LAS DOS ESCRITAS PORQUE UNA")
    print("SOLA NO SE PUEDE COTEJAR CON LA CIFRA DE LA 214:")
    print("CIFRA entradas que nombran %r EN MAYUSCULAS Y TAL CUAL: %d"
          % (MARCA_HUECO, con_hueco_may))
    print("CIFRA entradas que lo nombran SIN MIRAR MAYUSCULAS: %d"
          % con_hueco_ins)
    print("   (la vuelta 214 publico 119 con la segunda convencion, la de "
          ".upper(), leida hoy en la linea 133 de "
          "scripts/loop/_v214_t1c_op_i_01.py)")
    print("CIFRA campos SOSPECHOSOS de relleno, antes de mirar el vocabulario "
          "del campo: %d" % (len(rellenos) + len(descartados)))
    print("CIFRA de esos DESCARTADOS porque el campo los usa como estado: %d"
          % len(descartados))
    for k, nombre, campo, valor, largas in descartados[:20]:
        print("   DESCARTADO> entrada %d (%s), campo %s = %r; el mismo campo "
              "trae la forma larga %r" % (k, nombre, campo, valor, largas[0]))
    print("CIFRA campos RELLENADOS DE VERDAD, ya descontado el vocabulario: %d"
          % len(rellenos))
    for k, nombre, campo, valor, _ in rellenos[:20]:
        print("   RELLENO> entrada %d (%s), campo %s = %r" % (k, nombre, campo, valor))
    print("CIFRA campos VACIOS, que no estan nombrados ni rellenados: %d"
          % len(vacios))
    for k, nombre, campo in vacios[:20]:
        print("   VACIO> entrada %d (%s), campo %s" % (k, nombre, campo))
    print("")
    print("EL CASO POSITIVO DE ESTA BUSQUEDA, PORQUE UN CERO QUE NO PUEDE SALIR")
    print("DISTINTO DE CERO NO ES UNA BUSQUEDA (EJECUTOR.md 1, EL CASO ROJO SE")
    print("PRUEBA POR MUTACION). Se le mete a la sonda una entrada FABRICADA EN")
    print("MEMORIA, que NO se escribe en ningun fichero, con un campo de relleno")
    print("y otro vacio, y se comprueba que los caza:")
    fabricada = {"nombre": "ENTRADA FABRICADA EN MEMORIA", "forma": "TBD",
                 "cobertura": "   ", "nota": "esto si es un dato"}
    cazados_r = [c for c, v in fabricada.items() if es_relleno(v)]
    cazados_v = [c for c, v in fabricada.items() if es_vacio(v)]
    print("   CIFRA campos de relleno cazados en la fabricada: %d %s (se exige 1)"
          % (len(cazados_r), cazados_r))
    print("   CIFRA campos vacios cazados en la fabricada: %d %s (se exige 1)"
          % (len(cazados_v), cazados_v))
    if len(cazados_r) != 1 or len(cazados_v) != 1:
        fallos += 1
        print("   ROJO: la sonda no caza lo que dice cazar.")
    print("   Y EL CASO QUE PRUEBA QUE NO ES DEMASIADO LAXA: un campo que")
    print("   CONTIENE un guion dentro de un texto normal NO se cuenta.")
    print("   es_relleno('cribado intra, 155 de 155 pares - CERRADO') = %s "
          "(se exige False)"
          % es_relleno("cribado intra, 155 de 155 pares - CERRADO"))
    if es_relleno("cribado intra, 155 de 155 pares - CERRADO"):
        fallos += 1
    print("   Y EL TERCERO, QUE ES EL QUE PRUEBA LA CORRECCION `D.2`: la regla")
    print("   del vocabulario tiene que DESCARTAR 'pendiente' en el campo estado")
    print("   Y NO DESCARTARLO en un campo que no trae su forma larga.")
    en_estado = es_del_vocabulario(datos, "estado", "pendiente")
    en_forma = es_del_vocabulario(datos, "forma", "pendiente")
    print("   formas largas de 'pendiente' en el campo estado: %d (se exige "
          "al menos 1)" % len(en_estado))
    print("   formas largas de 'pendiente' en el campo forma:  %d (se exige 0)"
          % len(en_forma))
    if not en_estado or en_forma:
        fallos += 1
        print("   ROJO: la regla del vocabulario no separa los dos casos.")
    print("")
    total_malos = len(rellenos) + len(vacios)
    print("EL VEREDICTO DEL PUNTO 3, MEDIDO Y NO OPINADO")
    print("   LA MITAD AFIRMATIVA: el hueco SI se nombra, en %d entradas por la"
          % con_hueco_ins)
    print("   convencion de la 214 y en %d por la estricta." % con_hueco_may)
    print("   LA MITAD NEGATIVA, YA NO PENDIENTE: CIFRA huecos RELLENADOS en vez")
    print("   de nombrados: %d (rellenos %d mas vacios %d)."
          % (total_malos, len(rellenos), len(vacios)))
    veredicto_3 = "CUBRE" if total_malos == 0 else "NO CUBRE"
    print("   VEREDICTO MEDIDO HOY: **%s**" % veredicto_3)
    print("   VEREDICTO DE LA VUELTA 214, COMO CONTRASTE: **A MEDIAS**")
    print("   SE MUEVE: %s" % ("SI, de A MEDIAS a %s" % veredicto_3
                               if veredicto_3 != "A MEDIAS" else "NO"))
    print("")

    # ------------------------------------------------------------- PUNTO 4
    print("=" * 78)
    print("4.b. EL PUNTO 4: SE BUSCA LA SEDE ANTES DE DECIDIR, NO SE INVENTA")
    print("=" * 78)
    print("LO QUE LA VISTA HUMANA DECLARA DE SI MISMA, PEGADO Y CON SU LINEA:")
    for i, l in enumerate(vista.split(NL), 1):
        if "NO SE REGENERA AQUI" in l.upper():
            print("   docs/plan/10_INVENTARIO.md linea %d: %s" % (i, l.strip()))
    print("")
    print("LA BUSQUEDA, CON SU COMANDO ESCRITO ANTES DE SU RESULTADO:")
    print("   se recorre TODO scripts/ (no solo el arbol del bucle) y por cada")
    print("   fichero .py se pregunta si NOMBRA 10_INVENTARIO.md y si ADEMAS")
    print("   tiene, en la misma linea o en las tres siguientes, una apertura en")
    print("   modo escritura o una llamada de escritura sobre esa ruta.")
    print("")
    nombran, escriben = [], []
    for base, _, ficheros in os.walk(os.path.join(RAIZ, "scripts")):
        for f in sorted(ficheros):
            if not f.endswith(".py"):
                continue
            p = os.path.join(base, f)
            rel = os.path.relpath(p, RAIZ).replace(os.sep, "/")
            try:
                t = io.open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            lineas = t.replace(chr(13) + NL, NL).split(NL)
            toca = False
            for i, l in enumerate(lineas):
                if "10_INVENTARIO" not in l:
                    continue
                toca = True
                ventana = NL.join(lineas[i:i + 4])
                if re.search(r'open\([^)]*10_INVENTARIO[^)]*["\']w|'
                             r'10_INVENTARIO[^)]*\)[^)]*\.write\(|'
                             r'escribir\([^)]*10_INVENTARIO', ventana):
                    escriben.append((rel, i + 1, l.strip()[:90]))
            if toca:
                nombran.append(rel)
    print("CIFRA ficheros .py de scripts que NOMBRAN la vista humana: %d"
          % len(nombran))
    print("CIFRA ficheros .py que la ESCRIBEN: %d" % len(escriben))
    for rel, i, l in escriben:
        print("   ESCRIBE> %s linea %d: %s" % (rel, i, l))
    if not escriben:
        print("   (ninguno: la busqueda da CERO, y ese cero es el resultado)")
    print("")
    print("LA SEGUNDA MITAD DE LA BUSQUEDA, PORQUE UN FICHERO PUEDE ESCRIBIRSE")
    print("SIN QUE NINGUN SCRIPT LO NOMBRE: DE QUE COMMITS SALE LA VISTA HUMANA,")
    print("LEIDO DE git log SOBRE SU RUTA Y NO TECLEADO.")
    _, log = git(["log", "--format=%h|%ad|%s", "--date=short", "--",
                  "docs/plan/10_INVENTARIO.md"])
    commits = [l for l in log.replace(chr(13) + NL, NL).split(NL) if l.strip()]
    print("CIFRA commits que han tocado la vista humana en toda su historia: %d"
          % len(commits))
    for c in commits[:6]:
        print("   COMMIT> %s" % c[:120])
    print("")
    _, ultimo = git(["log", "-1", "--format=%h %ad", "--date=short", "--",
                     "docs/plan/10_INVENTARIO.md"])
    print("CIFRA ultimo commit que la toco: %s" % ultimo.strip())
    print("CIFRA bytes de la vista humana hoy: %d" % os.path.getsize(VISTA))
    print("CIFRA bytes de docs/plan/INVENTARIO.jsonl hoy: %d"
          % os.path.getsize(INV))
    print("")
    print("EL VEREDICTO DEL PUNTO 4, MEDIDO Y NO OPINADO")
    print("   LA MITAD QUE SI: el archivo fuente se recomputo, y hoy tiene %d"
          % len(datos))
    print("   entradas al corte de 3388.")
    print("   LA MITAD QUE FALTA: regenerar la vista humana.")
    print("   LA SEDE QUE LA REGENERARIA: CIFRA instrumentos que la escriben: %d."
          % len(escriben))
    if not escriben:
        print("   NO EXISTE EN EL REPO, Y ESO TAMBIEN ES UN RESULTADO: la vista")
        print("   humana no la regenera ningun instrumento porque NINGUNO LA")
        print("   ESCRIBE. Los %d ficheros que la nombran la LEEN o la citan."
              % len(nombran))
        print("   Su ultima escritura fue a mano, en el commit de arriba.")
        veredicto_4 = "A MEDIAS"
        print("   VEREDICTO MEDIDO HOY: **%s**, y no por pereza de esta vuelta:"
              % veredicto_4)
        print("   la mitad que falta NO TIENE INSTRUMENTO QUE LA HAGA, y")
        print("   fabricarlo es maquinaria nueva bajo la moratoria (AUDITOR.md")
        print("   6.3). SE SUBE NOMBRADO.")
    else:
        veredicto_4 = "A MEDIAS"
        print("   VEREDICTO MEDIDO HOY: **%s**. La sede existe y esta nombrada"
              % veredicto_4)
        print("   arriba; correrla no es de esta vuelta.")
    print("   VEREDICTO DE LA VUELTA 214, COMO CONTRASTE: **A MEDIAS**")
    print("   SE MUEVE: NO, calza con el contraste")
    print("")

    # ------------------------------------------------------------- GUARDA
    print("=" * 78)
    print("LA GUARDA DE LA 4.c: QUE NO SE MOVIO NINGUN CAMPO estado")
    print("=" * 78)
    sha_exp_despues = sha(EXPEDIENTE)
    print("SHA256 LF DE docs/plan/OPERACIONES.jsonl AL SALIR: %s" % sha_exp_despues)
    print("CIFRA los dos sha256 CALZAN: %s (se exige SI)"
          % ("SI" if sha_exp_antes == sha_exp_despues else "NO"))
    if sha_exp_antes != sha_exp_despues:
        fallos += 1
    _, ns = git(["diff", "--numstat", "--", "docs/plan/OPERACIONES.jsonl"])
    filas = [l for l in ns.replace(chr(13) + NL, NL).split(NL) if l.strip()]
    print("CIFRA filas de git diff --numstat sobre el expediente: %d (se exige 0)"
          % len(filas))
    if filas:
        fallos += 1
    _, ns2 = git(["diff", "--numstat", "--", "docs/plan/INVENTARIO.jsonl"])
    filas2 = [l for l in ns2.replace(chr(13) + NL, NL).split(NL) if l.strip()]
    print("CIFRA filas de git diff --numstat sobre el inventario: %d (se exige 0)"
          % len(filas2))
    if filas2:
        fallos += 1
    print("")
    print("EL REPARTO DE LOS DOS PUNTOS, DESPUES DE ESTA VUELTA")
    print("   PUNTO 3: %s (era A MEDIAS)" % veredicto_3)
    print("   PUNTO 4: %s (era A MEDIAS)" % veredicto_4)
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO.")
        return 1
    print("VERDE: los dos puntos quedan medidos y dichos, y ningun campo estado "
          "se movio.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
