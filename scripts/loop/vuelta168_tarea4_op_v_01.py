# -*- coding: utf-8 -*-
r"""vuelta168_tarea4_op_v_01.py . TAREA 4 de la vuelta 168.

RESUELVE `OP-V-01` POR GIT, COMO MANDA EL PUNTO 5 DE LA DECISION DEL FUNDADOR
DEL 4 SEP 2026, Y ADOSA A SU FICHA LA PRUEBA POR CITA.

QUE ESTABA ABIERTO. El hallazgo 4.4 del acta 167 midio que `OP-V-01` esta en
`HECHA` sin ninguna de las tres pruebas del instrumento del expediente, y
declaro con todas sus letras lo que NO habia verificado: *"cual es el commit que
movio ese estado y cuando"*. La decision 5 lo cierra por git: se busca el
commit; si es el cierre de la fase 08, la ficha lleva la prueba por cita; **sin
prueba, la ficha vuelve a pendiente.**

LO QUE ESTE INSTRUMENTO NO DA POR BUENO. El encargo de la 168 nombra `e966d896`
y dice lo que ese commit contiene, pero tambien ordena *"VERIFICALO TU TAMBIEN
antes de escribirlo"*. Asi que aqui NADA se acepta del encargo: el hash se
localiza SOLO, recorriendo `git log` sobre `docs/plan/OPERACIONES.jsonl` y
comparando la ficha ANTES y DESPUES de cada commit hasta encontrar el que cambia
el campo `estado`. El hash del encargo entra unicamente como CONTRASTE, y si no
coincide con el medido, el instrumento PARA.

Y LOS CINCO PUNTOS TRANSVERSALES TAMPOCO SE COPIAN: se buscan uno por uno, por
su marca propia, en el CUERPO DEL MENSAJE del commit medido. Si alguno no esta,
el instrumento PARA y la ficha vuelve a pendiente, que es lo que la decision
manda.

LO QUE SE ESCRIBE, Y ES CORTO A PROPOSITO: la ficha YA TRAE los cinco puntos y
la corrida K, porque los escribio el propio commit del fundador. Lo que NO
traia, y es justo lo que el acta 167 declaro sin verificar, es QUE COMMIT movio
el estado. Eso es lo que esta nota adosa, por el carril del banco 9.10 y sin
tocar una palabra de lo anterior.

Y ADOSA ALGO MAS, QUE ES LO QUE IMPIDE QUE ESTA NOTA SEA UN FALSO VERDE: LA
FICHA SIGUE SIN CALZAR CON EL INSTRUMENTO, Y LA NOTA LO DICE. Escribir la prueba
por cita NO hace que `vuelta150_3_relectura_expediente.py` cambie de veredicto,
y no se toca el instrumento para que lo haga: sus tres pruebas son grafo, codigo
vivo y huella en git con rutas `dataset/`, `web/` o `engine/`, y `e966d896` toca
`docs/` y `examples/`. **La prueba por cita es una CUARTA via que la decision
del fundador autoriza para esta ficha, no una de las tres.** Callar eso seria
exactamente la degradacion silenciosa del canon 9 del banco.

IDEMPOTENTE: si la marca ya vive en la ficha, no escribe y lo dice.

USO:
  python scripts/loop/vuelta168_tarea4_op_v_01.py
  python scripts/loop/vuelta168_tarea4_op_v_01.py --mutar
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
FICHA = "OP-V-01"
MARCA = "PRUEBA POR CITA DEL COMMIT QUE MOVIO EL ESTADO (4 sep 2026, vuelta 168, TAREA 4"
HASH_DEL_ENCARGO = "e966d896"

# LOS CINCO PUNTOS, CADA UNO CON LA MARCA POR LA QUE SE BUSCA EN EL CUERPO DEL
# COMMIT. No se buscan por su numero de orden: se buscan por su contenido, para
# que reordenarlos no los haga desaparecer.
PUNTOS = [
    ("1 Gate 0 con su ciclo entero y 26 en OK", ("GATE 0 VERDE", "26 en OK")),
    ("2 las tres suites", ("motor 25/25", "1.040 pasadas", "tsc exitcode 0")),
    ("3 el vuelo completo 16 de 16", ("16 de 16", "corrida K")),
    ("4 la prueba de rumbos sin deriva", ("PRUEBA DE RUMBOS", "SIN DERIVA")),
    ("5 el reindexado con sus dos sellos", ("d70adc1d", "42223fcc")),
]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def ficha_en(ref):
    """La ficha OP-V-01 tal como esta en el arbol de `ref`, o None."""
    c, texto = git(["show", "%s:docs/plan/OPERACIONES.jsonl" % ref])
    if c != 0:
        return None
    for l in texto.splitlines():
        l = l.strip()
        if not l:
            continue
        try:
            d = json.loads(l)
        except ValueError:
            continue
        if d.get("id_op") == FICHA:
            return d
    return None


def commit_que_movio_el_estado():
    """EL COMMIT SE BUSCA, NO SE RECIBE. Recorre los commits que tocan
    OPERACIONES.jsonl, del mas nuevo al mas viejo, y devuelve el primero cuyo
    `estado` de OP-V-01 difiere del de su padre. Devuelve
    (hash, asunto, cuerpo, estado_antes, estado_despues) o (None, error)."""
    c, log = git(["log", "--format=%H", "--", "docs/plan/OPERACIONES.jsonl"])
    if c != 0:
        return None, "PARADA: git log sobre OPERACIONES.jsonl fallo."
    hallados = []
    for h in log.split():
        d = ficha_en(h)
        p = ficha_en(h + "^")
        if d is None:
            continue
        antes = p.get("estado") if p else None
        if antes != d.get("estado"):
            hallados.append((h, antes, d.get("estado")))
    # EL NACIMIENTO NO ES UN MOVIMIENTO, Y DISTINGUIRLOS NO ES AFLOJAR LA VARA:
    # es medir lo que se pregunta. El primer commit que escribe la ficha aparece
    # como None -> LISTA, y llamar a eso "mover el estado" haria que la cifra
    # publicada dijera DOS donde el hecho es UNO. Los dos se cuentan y los dos se
    # publican, cada uno con su nombre.
    nacimientos = [x for x in hallados if x[1] is None]
    movimientos = [x for x in hallados if x[1] is not None]
    if not movimientos:
        return None, "PARADA: ningun commit mueve el estado de %s." % FICHA
    h, antes, despues = movimientos[0]
    c, asunto = git(["log", "-1", "--format=%s", h])
    c2, cuerpo = git(["log", "-1", "--format=%B", h])
    return (h, asunto.strip(), cuerpo, antes, despues, movimientos, nacimientos), None


def puntos_presentes(cuerpo):
    """LOS CINCO PUNTOS, BUSCADOS EN EL CUERPO Y NO SUPUESTOS. Devuelve la lista
    de (rotulo, presente, marcas_que_faltan)."""
    fuera = []
    for rotulo, marcas in PUNTOS:
        faltan = [m for m in marcas if m not in cuerpo]
        fuera.append((rotulo, not faltan, faltan))
    return fuera


def texto_de_la_nota(h, asunto, antes, despues, cuantos_movimientos):
    return (
        " %s). "
        "LA DECISION 5 DEL FUNDADOR DEL 4 SEP 2026 PEDIA BUSCAR POR GIT EL COMMIT QUE "
        "MOVIO ESTE ESTADO, porque el hallazgo 4.4 del acta 167 declaro no haberlo "
        "hecho. Buscado y medido en la vuelta 168, recorriendo los commits que tocan "
        "docs/plan/OPERACIONES.jsonl y comparando esta ficha contra la de su padre: "
        "EL UNICO COMMIT QUE MUEVE EL ESTADO DE %s ES %s, '%s', y lo mueve de %s a "
        "%s. Movimientos de estado hallados en toda la historia de esta ficha: %d. "
        "LOS CINCO PUNTOS TRANSVERSALES ESTAN EN EL CUERPO DE ESE COMMIT, buscados "
        "uno por uno por su marca propia y no por su orden: Gate 0 con su ciclo "
        "entero y 26 en OK; las tres suites (motor 25/25, web 1.040 pasadas, tsc "
        "exitcode 0); el vuelo completo 16 de 16 en la corrida K; la prueba de rumbos "
        "SIN DERIVA; y el reindexado con sus sellos d70adc1d y 42223fcc. LA PRUEBA "
        "EXISTE Y POR ESO LA FICHA NO VUELVE A PENDIENTE. "
        "Y LO QUE ESTA NOTA NO HACE, DICHO PARA QUE NADIE LO LEA COMO UN VERDE QUE NO "
        "ES: escribirla NO cambia el veredicto de "
        "scripts/loop/vuelta150_3_relectura_expediente.py, que sigue midiendo esta "
        "ficha como HECHA SIN NINGUNA PRUEBA, y el instrumento NO se toca para que "
        "cambie. Sus tres pruebas son grafo, codigo vivo y huella en git con rutas "
        "dataset/, web/ o engine/, y %s toca docs/ y examples/. LA PRUEBA POR CITA ES "
        "UNA CUARTA VIA QUE LA DECISION DEL FUNDADOR AUTORIZA PARA ESTA FICHA, NO UNA "
        "DE LAS TRES, y la discrepancia entre el estado y la vara del instrumento "
        "queda DECLARADA en vez de resuelta copiando."
        % (MARCA, FICHA, h[:8], asunto, antes, despues, cuantos_movimientos, h[:8]))


def main():
    print("=" * 78)
    print("VUELTA 168, TAREA 4: OP-V-01 RESUELTA POR GIT (decision 5 del fundador)")
    print("=" * 78)
    print("")

    print("A) EL COMMIT SE BUSCA POR GIT, NO SE RECIBE DEL ENCARGO")
    par, err = commit_que_movio_el_estado()
    if err:
        print("   " + err)
        print("   LA FICHA VUELVE A PENDIENTE, que es lo que la decision manda.")
        return 1
    h, asunto, cuerpo, antes, despues, todos, nacimientos = par
    print("   CIFRA commits que MUEVEN el estado de %s (el nacimiento no cuenta): %d"
          % (FICHA, len(todos)))
    for hh, aa, dd in todos:
        print("      %s  %s -> %s" % (hh[:8], aa, dd))
    print("   CIFRA commits que la HACEN NACER (None -> algo), contados aparte: %d"
          % len(nacimientos))
    for hh, aa, dd in nacimientos:
        print("      %s  (nace) -> %s" % (hh[:8], dd))
    print("   EL QUE LO MOVIO A SU ESTADO DE HOY: %s" % h[:8])
    print("   asunto: %s" % asunto[:110])
    print("")

    print("B) EL HASH DEL ENCARGO, COMO CONTRASTE Y NO COMO FUENTE")
    print("   el encargo de la 168 nombra: %s" % HASH_DEL_ENCARGO)
    print("   yo mido:                     %s" % h[:8])
    coincide = h.startswith(HASH_DEL_ENCARGO)
    print("   COINCIDEN: %s" % ("SI" if coincide else "NO. MANDA LO MEDIDO Y SE DECLARA."))
    if not coincide:
        print("   PARADA: el encargo y la medicion discrepan. No se escribe nada.")
        return 1
    print("")

    print("C) LOS CINCO PUNTOS, BUSCADOS EN EL CUERPO DEL COMMIT MEDIDO")
    filas = puntos_presentes(cuerpo)
    for rotulo, ok, faltan in filas:
        print("   %-46s %s%s" % (rotulo, "PRESENTE" if ok else "FALTA",
                                 "" if ok else "  (%s)" % ", ".join(faltan)))
    n_ok = len([1 for _r, ok, _f in filas if ok])
    print("   CIFRA puntos presentes: %d de %d" % (n_ok, len(PUNTOS)))
    if n_ok != len(PUNTOS):
        print("   PARADA: el commit no dice lo que el encargo dice que dice.")
        print("   LA FICHA VUELVE A PENDIENTE, que es lo que la decision manda.")
        return 1
    print("")

    print("D) LA FICHA DE HOY, Y LO QUE YA TRAE")
    lineas = io.open(OPS, encoding="utf-8").read().split("\n")
    idx = [i for i, l in enumerate(lineas)
           if l.strip() and json.loads(l).get("id_op") == FICHA]
    if len(idx) != 1:
        print("   PARADA: %s aparece %d veces en el fichero." % (FICHA, len(idx)))
        return 1
    i = idx[0]
    d = json.loads(lineas[i])
    nota_vieja = d.get("nota") or ""
    print("   docs/plan/OPERACIONES.jsonl, linea %d" % (i + 1))
    print("   estado de hoy: %s" % d.get("estado"))
    print("   CIFRA caracteres de la nota ANTES: %d" % len(nota_vieja))
    print("   la nota YA trae la corrida K:      %s" % ("SI" if "corrida K" in nota_vieja else "NO"))
    print("   la nota YA trae los dos sellos:    %s"
          % ("SI" if ("d70adc1d" in nota_vieja and "42223fcc" in nota_vieja) else "NO"))
    print("   la nota trae el HASH del commit:   %s"
          % ("SI" if h[:8] in nota_vieja else "NO, y eso es lo que esta tarea adosa"))
    if MARCA in nota_vieja:
        print("YA ESTABA: la nota de esta tarea vive en la ficha. No se toca.")
        print("CIFRA fichas escritas: 0")
        return 0
    print("")

    print("E) LO ESCRITO, POR ADICION Y SIN BORRAR UNA PALABRA")
    d["nota"] = nota_vieja + texto_de_la_nota(h, asunto, antes, despues, len(todos))
    lineas[i] = json.dumps(d, ensure_ascii=False)
    io.open(OPS, "w", encoding="utf-8", newline="\n").write("\n".join(lineas))

    relee = [json.loads(l) for l in io.open(OPS, encoding="utf-8").read().split("\n")
             if l.strip()]
    nueva = [x for x in relee if x.get("id_op") == FICHA][0]
    print("   CIFRA fichas en el fichero DESPUES: %d (antes: %d)"
          % (len(relee), len([l for l in lineas if l.strip()])))
    print("   CIFRA claves de la ficha: %d (el esquema no crece)" % len(nueva))
    print("   el estado NO se movio: %s" % nueva.get("estado"))
    print("   la nota vieja sigue ENTERA dentro de la nueva: %s"
          % ("SI" if nota_vieja in (nueva.get("nota") or "") else "NO"))
    if nota_vieja not in (nueva.get("nota") or ""):
        print("   PARADA: se perdio texto viejo.")
        return 1
    print("   CIFRA caracteres de la nota DESPUES: %d" % len(nueva.get("nota") or ""))
    print("   CIFRA caracteres anadidos: %d"
          % (len(nueva.get("nota") or "") - len(nota_vieja)))
    print("   CIFRA fichas escritas: 1")
    print("")
    print("VERDE: OP-V-01 lleva la prueba por cita y NO vuelve a pendiente.")
    return 0


# ---------------------------------------------------------------------------
# CASO POSITIVO POR MUTACION (EJECUTOR.md 1). Sujetos: cuerpos de commit
# FABRICADOS en memoria mas el commit REAL, que es un commit fijo de la
# historia. Cero escrituras.
# ---------------------------------------------------------------------------

def prueba_de_mutacion():
    print("=" * 78)
    print("VUELTA 168, TAREA 4: CASO POSITIVO POR MUTACION DE LA PRUEBA POR CITA")
    print("=" * 78)
    print("")
    casos = []

    print("A) LOS CINCO PUNTOS SE BUSCAN Y NO SE SUPONEN")
    entero = ("GATE 0 VERDE ... 26 en OK ... motor 25/25 ... 1.040 pasadas ... "
              "tsc exitcode 0 ... 16 de 16 ... corrida K ... PRUEBA DE RUMBOS ... "
              "SIN DERIVA ... d70adc1d ... 42223fcc")
    sujetos = [
        ("un cuerpo que trae los cinco", entero, 5),
        ("le quito los dos sellos", entero.replace("42223fcc", "xxx"), 4),
        ("le quito ademas SIN DERIVA", entero.replace("42223fcc", "xxx")
         .replace("SIN DERIVA", "con deriva"), 3),
        ("un cuerpo vacio", "", 0),
        ("un cuerpo que habla de otra cosa", "cerre la fase y todo verde", 0),
    ]
    for rotulo, cuerpo, esperado in sujetos:
        n = len([1 for _r, ok, _f in puntos_presentes(cuerpo) if ok])
        print("   %-42s -> %d de 5" % (rotulo[:42], n))
        casos.append(("A_%s" % rotulo.replace(" ", "_")[:36], n, esperado))
    print("")

    print("B) EL COMMIT REAL, BUSCADO POR GIT HOY")
    par, err = commit_que_movio_el_estado()
    if err:
        print("   " + err)
        return 1
    h, asunto, cuerpo, antes, despues, todos, nacimientos = par
    print("   hash medido: %s" % h[:8])
    print("   %s -> %s" % (antes, despues))
    print("   puntos presentes en su cuerpo: %d de 5"
          % len([1 for _r, ok, _f in puntos_presentes(cuerpo) if ok]))
    casos.append(("B_el_hash_medido_empieza_por_e966d896",
                  h.startswith(HASH_DEL_ENCARGO), True))
    casos.append(("B_lo_mueve_de_LISTA_a_HECHA", "%s->%s" % (antes, despues),
                  "LISTA->HECHA"))
    # PRIMERA CORRIDA DE ESTE ARNES: puse 1 y salio 2, y no era la ficha, era mi
    # vara: contaba el NACIMIENTO (None -> LISTA, en c891b3ff) como movimiento.
    # Se declara y se arregla EN LA FUENTE separando las dos poblaciones, que es
    # mas exacto que antes, no mas laxo. Las dos cifras se publican.
    casos.append(("B_es_el_UNICO_movimiento_de_estado", len(todos), 1))
    casos.append(("B_y_tiene_UN_solo_nacimiento", len(nacimientos), 1))
    casos.append(("B_el_nacimiento_no_es_el_mismo_commit_que_el_movimiento",
                  nacimientos[0][0] == todos[0][0], False))
    casos.append(("B_su_cuerpo_trae_los_cinco_puntos",
                  len([1 for _r, ok, _f in puntos_presentes(cuerpo) if ok]), 5))
    print("")

    print("C) LA NOTA CAMBIA SI CAMBIA LA MEDICION")
    n1 = texto_de_la_nota(h, asunto, antes, despues, len(todos))
    n2 = texto_de_la_nota("0" * 40, asunto, "HECHA", "LISTA", 3)
    casos.append(("C_la_nota_no_es_la_misma_con_otro_commit", n1 == n2, False))
    casos.append(("C_la_nota_real_nombra_el_hash_medido", h[:8] in n1, True))
    casos.append(("C_la_nota_real_dice_LISTA_a_HECHA", "de LISTA a HECHA" in n1, True))
    casos.append(("C_la_nota_declara_que_el_instrumento_sigue_rojo",
                  "HECHA SIN NINGUNA PRUEBA" in n1, True))
    casos.append(("C_y_declara_que_NO_toca_el_instrumento",
                  "NO se toca para que cambie" in n1, True))
    print("   la nota real nombra %s y declara que el instrumento sigue rojo" % h[:8])
    print("")

    print("D) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-54s %s   (real=%r esperado=%r)"
              % (nombre[:54], "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("E) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        mutado = (not esperado) if isinstance(esperado, bool) else (
            esperado + 1 if isinstance(esperado, int) else str(esperado) + "_mutado")
        cae = (real != mutado)
        print("   %-54s %s   (esperado mutado=%r)"
              % (nombre[:54], "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if "--mutar" in sys.argv:
        sys.exit(prueba_de_mutacion())
    sys.exit(main())
