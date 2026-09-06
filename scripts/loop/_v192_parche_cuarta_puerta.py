# -*- coding: utf-8 -*-
r"""_v192_parche_cuarta_puerta.py . EL PARCHE QUE ANADE LA CUARTA PUERTA A
scripts/loop/apertura_del_auditor.py (vuelta 192, TAREA 4.a y 4.b).

NO SE CLONA EL FICHERO: se le anade. `apertura_del_auditor.py` tiene nombre
estable y sin numero de vuelta, como sus hermanos, y la pieza `d` del encargo lo
dice con esas palabras. Este parche es de un solo uso y es IDEMPOTENTE: si las
anclas ya estan aplicadas, no vuelve a escribir.
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(RAIZ, "scripts", "loop", "apertura_del_auditor.py")
NL = chr(10)
Q3 = '"' * 3

BLOQUE = '''# --------------------------------------------------- LA CUARTA PUERTA (v192)
def puestos_sellados(ruta_sello=None):
    @@Q@@LOS PUESTOS QUE EL SELLO DE ESTE TURNO ELIGIO. Devuelve una lista de
    enteros, VACIA si todavia no hay sello.

    NO SE TECLEAN NI SE PASAN POR ARGUMENTO: se leen del propio sello, que nombra
    la ciega, y de la ciega, que lista sus `puesto_intra`. **El sujeto de la
    cuarta puerta lo define el sello y nadie mas**, que es lo que impide elegirlo
    despues de mirar.@@Q@@
    ruta = ruta_sello or _SELLADO["ruta"]
    if not ruta or not os.path.exists(ruta):
        return []
    try:
        sello = json.load(io.open(ruta, encoding="utf-8"))
    except Exception:
        return []
    rel = sello.get("ciega")
    if not rel:
        return []
    p = rel if os.path.isabs(rel) else os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.exists(p):
        return []
    texto = io.open(p, encoding="utf-8", errors="replace").read()
    return sorted(set(int(x) for x in
                      re.findall(r"puesto_intra[^0-9]{0,12}(\\d+)", texto)))


def leer_veredictos(destapar_sujeto=False, ruta=None, ruta_sello=None):
    @@Q@@EL ARCHIVO DE VEREDICTOS, Y APUNTA SU TOQUE. **ES LA CUARTA PUERTA.**

    Devuelve la lista de filas. Con `destapar_sujeto=False`, que es lo normal,
    **las filas de los puestos sellados salen con `clase` y `razon` TAPADAS**: se
    pueden contar, se pueden cruzar por `puesto_intra`, y no se puede ver lo que
    la ciega esconde. Con `destapar_sujeto=True` salen enteras **y se apunta un
    toque distinto**, el de destape, que es el que hace caer
    `declarar_clases_escritas()` si viene antes.

    Apunta SIEMPRE un toque, incluso tapando, porque un turno tiene derecho a
    saber cuantas veces se abrio el archivo.@@Q@@
    apuntar(TOQUE_DESTAPE if destapar_sujeto else TOQUE_VEREDICTOS)
    p = ruta or os.path.join(RAIZ, ARCHIVO_DE_VEREDICTOS.replace("/", os.sep))
    filas = [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]
    if destapar_sujeto:
        return filas
    sellados = set(puestos_sellados(ruta_sello))
    if not sellados:
        return filas
    tapadas = []
    for f in filas:
        if f.get("puesto_intra") in sellados:
            f = dict(f)
            for campo in CAMPOS_QUE_DESTAPAN:
                if campo in f:
                    f[campo] = TAPADO
        tapadas.append(f)
    return tapadas


def marcador(ruta=None):
    @@Q@@EL RECUENTO POR CLASE SOBRE EL ARCHIVO ENTERO. Devuelve un dict.

    **NO DESTAPA NADA Y POR ESO NO HACE FALTA PEDIRLO:** un agregado de miles de
    filas no dice la clase de ninguna. Existe para que la cuarta puerta no
    estorbe lo que el acta SI tiene que hacer, que es recomputar el marcador
    ANTES de escribir sus clases.@@Q@@
    apuntar(TOQUE_VEREDICTOS)
    p = ruta or os.path.join(RAIZ, ARCHIVO_DE_VEREDICTOS.replace("/", os.sep))
    filas = [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]
    por_clase = {}
    for f in filas:
        por_clase[f.get("clase")] = por_clase.get(f.get("clase"), 0) + 1
    return {"filas": len(filas), "por_clase": por_clase}


def destapes_antes_de_las_clases():
    @@Q@@LOS TOQUES DE DESTAPE QUE LA BITACORA TRAE. PURA sobre el estado del
    modulo, y es la funcion que `puede_declarar_clases()` consulta.

    Va separada por el mismo motivo que `toques_prohibidos()`: **la decision se
    puede probar sin escribir un solo fichero.**@@Q@@
    return [t for t in _BITACORA if t == TOQUE_DESTAPE]


def puede_declarar_clases():
    @@Q@@(SI_PUEDE, MOTIVO). PURA sobre el estado del modulo.

    **ESTA ES LA FUNCION QUE EL ARNES TUMBA.** Cae si el turno destapo el sujeto
    antes de escribir sus clases: unas clases escritas DESPUES de ver el archivo
    no prueban nada, que es exactamente lo mismo que dice `puede_sellar()` sobre
    el sello.@@Q@@
    malos = destapes_antes_de_las_clases()
    if malos:
        return False, ("el turno destapo `clase` o `razon` de los puestos "
                       "SELLADOS %d vez(ces) ANTES de escribir sus clases. EL "
                       "SUJETO YA SE QUEMO, y unas clases escritas ahora no "
                       "probarian nada." % len(malos))
    if _CLASES["escritas"]:
        return False, "este turno ya declaro sus clases: no se declaran dos veces"
    if not _SELLADO["hecho"]:
        return False, ("este turno no ha sellado. Sin sello no hay sujeto, y sin "
                       "sujeto no hay clases que declarar")
    return True, "la bitacora esta limpia de destapes y el sello esta escrito"


def declarar_clases_escritas(ruta_clases):
    @@Q@@MARCA QUE LAS CLASES DEL AUDITOR ESTAN ESCRITAS. Devuelve (ok, informe).

    **CAE EN ROJO Y NO MARCA NADA** si `puede_declarar_clases()` dice que no. Es
    el gemelo exacto de `sellar()`: alli el rojo era no poder sellar; aqui es no
    poder declarar, **y a partir de aqui destapar el sujeto ya no quema nada**,
    porque las clases ya estan escritas.@@Q@@
    informe = []
    w = informe.append
    ok, motivo = puede_declarar_clases()
    w("PUEDE DECLARAR LAS CLASES: %s" % ("SI" if ok else "NO"))
    w("   motivo: %s" % motivo)
    w("   bitacora del turno hasta ahora: %s"
      % (", ".join(bitacora()) if bitacora() else "(vacia)"))
    w("   destapes apuntados: %d" % len(destapes_antes_de_las_clases()))
    if not ok:
        w("ROJO: NO se marca nada. La ciega de este turno NO se puede citar.")
        return False, informe
    if not os.path.exists(ruta_clases):
        w("ROJO: %s no existe. Unas clases que no estan escritas no se declaran."
          % ruta_clases)
        return False, informe
    _CLASES["escritas"] = True
    _CLASES["ruta"] = ruta_clases
    w("CLASES DECLARADAS: %s (%d bytes)"
      % (ruta_clases, os.path.getsize(ruta_clases)))
    w("   desde aqui, destapar el sujeto ya no quema nada.")
    return True, informe


def main():
    ap = argparse.ArgumentParser()'''.replace("@@Q@@", Q3)

ANCLA = "def main():" + NL + "    ap = argparse.ArgumentParser()"

VIEJO_ESTADO = '''    if a.estado:
        ok, motivo = puede_sellar()
        print("   bitacora: %s" % (", ".join(bitacora()) or "(vacia)"))
        print("   PUEDE SELLAR: %s (%s)" % ("SI" if ok else "NO", motivo))
        return 0'''

NUEVO_ESTADO = '''    if a.estado:
        ok, motivo = puede_sellar()
        print("   bitacora: %s" % (", ".join(bitacora()) or "(vacia)"))
        print("   PUEDE SELLAR: %s (%s)" % ("SI" if ok else "NO", motivo))
        ok2, motivo2 = puede_declarar_clases()
        print("   LA CUARTA PUERTA: %s" % ARCHIVO_DE_VEREDICTOS)
        print("      campos que destapan: %s"
              % ", ".join(repr(c) for c in CAMPOS_QUE_DESTAPAN))
        print("      destapes apuntados: %d" % len(destapes_antes_de_las_clases()))
        print("   PUEDE DECLARAR LAS CLASES: %s (%s)"
              % ("SI" if ok2 else "NO", motivo2))
        return 0'''

VIEJO_CAB = '''    print("   LOS TRES PROHIBIDOS ANTES DEL SELLO: %s"
          % ", ".join(repr(p) for p in PROHIBIDOS_ANTES_DEL_SELLO))'''

NUEVO_CAB = '''    print("   LOS TRES PROHIBIDOS ANTES DEL SELLO: %s"
          % ", ".join(repr(p) for p in PROHIBIDOS_ANTES_DEL_SELLO))
    print("   Y LA CUARTA PUERTA, ANTES DE LAS CLASES: %s, campos %s"
          % (ARCHIVO_DE_VEREDICTOS,
             ", ".join(repr(c) for c in CAMPOS_QUE_DESTAPAN)))'''

VIEJO_IMP = "import json" + NL + "import os" + NL + "import subprocess"
NUEVO_IMP = "import json" + NL + "import os" + NL + "import re" + NL + "import subprocess"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    t = io.open(P, encoding="utf-8").read().replace(chr(13) + NL, NL)
    antes = len(t.encode("utf-8"))
    cambios = [("el bloque de la cuarta puerta", ANCLA, BLOQUE),
               ("el --estado", VIEJO_ESTADO, NUEVO_ESTADO),
               ("la cabecera del main", VIEJO_CAB, NUEVO_CAB),
               ("el import de re", VIEJO_IMP, NUEVO_IMP)]
    for nombre, viejo, nuevo in cambios:
        if nuevo in t:
            print("   YA ESTABA: %s" % nombre)
            continue
        if viejo not in t:
            print("   ROJO: no se encuentra el ancla de %s. No se escribe nada."
                  % nombre)
            return 1
        t = t.replace(viejo, nuevo, 1)
        print("   aplicado: %s" % nombre)
    io.open(P, "w", encoding="utf-8", newline=NL).write(t)
    print("   apertura_del_auditor.py pasa de %d a %d bytes en disco"
          % (antes, len(t.encode("utf-8"))))
    import py_compile
    py_compile.compile(P, doraise=True)
    print("   COMPILA")
    return 0


if __name__ == "__main__":
    sys.exit(main())
