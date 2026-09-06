# -*- coding: utf-8 -*-
r"""vuelta192_tarea4_mutacion_cuarta_puerta.py . EL CASO POSITIVO POR MUTACION DE
LA CUARTA PUERTA DEL SELLO DE LA APERTURA DEL AUDITOR.

ES LA PIEZA `c` DE LA TAREA 4 DE LA VUELTA 192, sobre el hallazgo `5.2` del acta
192. **CAE si la cuarta puerta se quita**, y eso se prueba quitandola de verdad
sobre el modulo cargado y comprobando que la comprobacion deja de morder.

SUJETO CONGELADO. Este arnes NO abre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` del
repo: fabrica su propio archivo, su propia ciega y su propio sello en un
directorio temporal con `tempfile.mkdtemp`, y los retira al terminar (`P.16`,
quien fabrica limpia). El literal del archivo vivo aparece aqui solo como NOMBRE,
y NO SE TOCA ninguna fila de nada.

QUE PRUEBA, UNA A UNA:

  A. Con el sello escrito, `leer_veredictos()` **tapa `clase` y `razon` de los
     puestos sellados y NO tapa los demas**.
  B. `marcador()` cuenta por clase sobre el archivo entero **sin destapar nada**.
  C. `declarar_clases_escritas()` **CAE EN ROJO** si antes hubo un destape.
  D. Sin destape previo, **declara en verde**, y despues del verde el destape ya
     no quema.
  E. LA MUTACION DE VERDAD: **si se le quita el toque de destape a
     `leer_veredictos()`, la comprobacion deja de caer**, y ese es el agujero que
     esta puerta tapa.
  F. LA SEGUNDA MUTACION: **si `CAMPOS_QUE_DESTAPAN` se queda vacio, el tapado
     deja de tapar**.

USO:
  python scripts/loop/vuelta192_tarea4_mutacion_cuarta_puerta.py
"""
import hashlib
import io
import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apertura_del_auditor as AP   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
SALIDA = os.path.join(LOOP, "SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt")

SELLADOS = [11, 22, 33]
OTROS = [44, 55]


def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    w("   %-64s %s" % (nombre, "VERDE" if ok else "ROJO"))
    if not ok:
        w("      esperado: %r" % (esperado,))
        w("      obtenido: %r" % (obtenido,))
    return ok


def _fabricar(tmp):
    """EL ARCHIVO, LA CIEGA Y EL SELLO, FABRICADOS CON LAS CIFRAS SABIDAS."""
    archivo = os.path.join(tmp, "veredictos.jsonl")
    with io.open(archivo, "w", encoding="utf-8", newline=NL) as f:
        for p in SELLADOS:
            f.write(json.dumps({"puesto_intra": p, "clase": "A",
                                "razon": "la razon del %d" % p}) + NL)
        for p in OTROS:
            f.write(json.dumps({"puesto_intra": p, "clase": "D",
                                "razon": "la razon del %d" % p}) + NL)
    ciega = os.path.join(tmp, "ciega.txt")
    io.open(ciega, "w", encoding="utf-8", newline=NL).write(
        NL.join("puesto_intra: %d" % p for p in SELLADOS) + NL)
    sello = os.path.join(tmp, "SELLO.json")
    io.open(sello, "w", encoding="utf-8", newline=NL).write(
        json.dumps({"vuelta": "PRUEBA", "ciega": ciega}, ensure_ascii=False) + NL)
    clases = os.path.join(tmp, "mis_clases.txt")
    io.open(clases, "w", encoding="utf-8", newline=NL).write("mis clases" + NL)
    return archivo, ciega, sello, clases


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("VUELTA 192, TAREA 4.c: CASO POSITIVO POR MUTACION DE LA CUARTA PUERTA")
    w("=" * 78)
    w("")
    w("SUJETO CONGELADO: el archivo, la ciega y el sello se FABRICAN en un")
    w("directorio temporal con las cifras sabidas por construccion. Este arnes NO")
    w("abre el archivo de veredictos del repo y NO SE TOCA ninguna fila.")
    w("   puestos SELLADOS del sujeto fabricado: %s"
      % ", ".join(str(x) for x in SELLADOS))
    w("   puestos NO sellados: %s" % ", ".join(str(x) for x in OTROS))
    w("")

    tmp = tempfile.mkdtemp(prefix="cuarta_puerta_")
    # ---------------------------------------------------------------------
    # ANADIDO EN LA VUELTA 194, TAREA 2.a. HALLAZGO `5.1` DEL ACTA 194, CORRIDO
    # Y NO DEDUCIDO EN docs/loop/_auditor_v194_cuarta_puerta_rota.txt.
    #
    # ESTE ARNES LLAMA A `AP.olvidar_todo()` OCHO VECES CONTRA EL MODULO REAL Y
    # NUNCA REDIRIGIA `AP.RUTA_DEL_TURNO`. La TAREA 4.a de la vuelta 193 le
    # anadio a `olvidar_todo()` el `os.remove(RUTA_DEL_TURNO)`, y con eso este
    # arnes pasaba a BORRAR EL TURNO VIVO DEL AUDITOR EN SU SEDE DE VERDAD, sin
    # avisar y sin caer: exitcode 0 con el fichero borrado.
    #
    # EL MECANISMO NO ES NUEVO NI ES MIO: el comentario de `RUTA_DEL_TURNO` en
    # `apertura_del_auditor.py` dice que la variable es de modulo "PARA QUE LOS
    # ARNESES LO PUEDAN REDIRIGIR A UN TEMPORAL", y el arnes de la 193 ya lo hace
    # en su linea 45. Lo que faltaba era hacerlo aqui.
    #
    # Y NO BASTA CON REDIRIGIR: LA SEDE DE VERDAD SE MIDE ANTES Y DESPUES, y este
    # arnes CAE EN ROJO si cambia. Un arnes que promete no tocar algo y no lo
    # comprueba es exactamente lo que dejo pasar este agujero.
    TURNO_REAL = os.path.join(LOOP, "_TURNO_DEL_AUDITOR.json")

    def _medir_turno_real():
        """(existe, bytes, sha256) DE LA SEDE DE VERDAD. Semi-pura: solo lee."""
        if not os.path.isfile(TURNO_REAL):
            return (False, 0, "")
        datos = io.open(TURNO_REAL, "rb").read()
        return (True, len(datos), hashlib.sha256(datos).hexdigest())

    turno_antes = _medir_turno_real()
    ruta_del_turno_original = AP.RUTA_DEL_TURNO
    AP.RUTA_DEL_TURNO = os.path.join(tmp, "_TURNO_DEL_AUDITOR.json")
    # ---------------------------------------------------------------------
    try:
        archivo, ciega, sello, clases = _fabricar(tmp)

        w("0) LA SEDE DE VERDAD DEL TURNO, REDIRIGIDA ANTES DEL PRIMER OLVIDO")
        w("   (ANADIDO EN LA 194, TAREA 2.a, por el hallazgo `5.1` del acta 194)")
        ok &= _caso(w, "AP.RUTA_DEL_TURNO ya NO apunta a docs/loop/",
                    AP.RUTA_DEL_TURNO == ruta_del_turno_original, False)
        ok &= _caso(w, "y apunta DENTRO del temporal de este arnes",
                    os.path.dirname(AP.RUTA_DEL_TURNO) == tmp, True)
        w("   la sede de verdad al entrar: %s"
          % ("EXISTE" if turno_antes[0] else "NO EXISTE"))
        w("")

        w("A) CON EL SELLO ESCRITO, `leer_veredictos()` TAPA EL SUJETO Y NADA MAS")
        AP.olvidar_todo()
        AP._SELLADO["hecho"] = True
        AP._SELLADO["ruta"] = sello
        ok &= _caso(w, "los puestos sellados se leen DEL SELLO y no se teclean",
                    AP.puestos_sellados(sello), SELLADOS)
        filas = AP.leer_veredictos(ruta=archivo, ruta_sello=sello)
        por_p = {f["puesto_intra"]: f for f in filas}
        ok &= _caso(w, "se devuelven las cinco filas", len(filas), 5)
        ok &= _caso(w, "la clase de un SELLADO sale tapada",
                    por_p[SELLADOS[0]]["clase"], AP.TAPADO)
        ok &= _caso(w, "la razon de un SELLADO sale tapada",
                    por_p[SELLADOS[0]]["razon"], AP.TAPADO)
        ok &= _caso(w, "la clase de un NO sellado NO se tapa",
                    por_p[OTROS[0]]["clase"], "D")
        ok &= _caso(w, "y el toque apuntado es el de lectura, no el de destape",
                    AP.bitacora(), [AP.TOQUE_VEREDICTOS])
        ok &= _caso(w, "destapes apuntados", len(AP.destapes_antes_de_las_clases()), 0)
        w("")

        w("B) `marcador()` CUENTA SOBRE EL ARCHIVO ENTERO Y NO DESTAPA NADA")
        AP.olvidar_todo()
        AP._SELLADO["hecho"] = True
        AP._SELLADO["ruta"] = sello
        m = AP.marcador(ruta=archivo)
        ok &= _caso(w, "cuenta las cinco filas", m["filas"], 5)
        ok &= _caso(w, "y las reparte por clase sin mirar ninguna en particular",
                    m["por_clase"], {"A": 3, "D": 2})
        ok &= _caso(w, "no apunta ningun destape",
                    len(AP.destapes_antes_de_las_clases()), 0)
        ok &= _caso(w, "asi que las clases se pueden declarar despues del marcador",
                    AP.puede_declarar_clases()[0], True)
        w("")

        w("C) EL CASO QUE TIENE QUE CAER: DESTAPAR ANTES DE ESCRIBIR LAS CLASES")
        AP.olvidar_todo()
        AP._SELLADO["hecho"] = True
        AP._SELLADO["ruta"] = sello
        crudas = AP.leer_veredictos(destapar_sujeto=True, ruta=archivo,
                                    ruta_sello=sello)
        ok &= _caso(w, "destapando SI se ve la razon del sujeto",
                    [f for f in crudas
                     if f["puesto_intra"] == SELLADOS[0]][0]["razon"],
                    "la razon del %d" % SELLADOS[0])
        ok &= _caso(w, "y queda apuntado como destape",
                    AP.destapes_antes_de_las_clases(), [AP.TOQUE_DESTAPE])
        ok &= _caso(w, "PUEDE DECLARAR LAS CLASES: NO",
                    AP.puede_declarar_clases()[0], False)
        okd, inf = AP.declarar_clases_escritas(clases)
        ok &= _caso(w, "declarar_clases_escritas() CAE EN ROJO", okd, False)
        ok &= _caso(w, "y NO marca nada", AP._CLASES["escritas"], False)
        for l in inf:
            w("      | " + l)
        w("")

        w("D) SIN DESTAPE PREVIO, DECLARA EN VERDE, Y DESPUES YA NO QUEMA")
        AP.olvidar_todo()
        AP._SELLADO["hecho"] = True
        AP._SELLADO["ruta"] = sello
        AP.leer_veredictos(ruta=archivo, ruta_sello=sello)
        okd2, _inf2 = AP.declarar_clases_escritas(clases)
        ok &= _caso(w, "declarar_clases_escritas() sale VERDE", okd2, True)
        ok &= _caso(w, "y queda marcado", AP._CLASES["escritas"], True)
        AP.leer_veredictos(destapar_sujeto=True, ruta=archivo, ruta_sello=sello)
        ok &= _caso(w, "un destape POSTERIOR ya no puede cambiar lo declarado",
                    AP._CLASES["escritas"], True)
        ok &= _caso(w, "y declarar dos veces no se puede",
                    AP.declarar_clases_escritas(clases)[0], False)
        w("")

        w("E) LA MUTACION DE VERDAD: SE LE QUITA LA CUARTA PUERTA Y TIENE QUE")
        w("   DEJAR DE CAER. Se sustituye `leer_veredictos` por una version SIN")
        w("   el apunte de destape, que es exactamente el codigo de antes de esta")
        w("   vuelta, y se comprueba que la comprobacion se vuelve ciega.")
        original = AP.leer_veredictos

        def sin_cuarta_puerta(destapar_sujeto=False, ruta=None, ruta_sello=None):
            p = ruta or os.path.join(RAIZ, AP.ARCHIVO_DE_VEREDICTOS)
            return [json.loads(l) for l in io.open(p, encoding="utf-8")
                    if l.strip()]
        try:
            AP.leer_veredictos = sin_cuarta_puerta
            AP.olvidar_todo()
            AP._SELLADO["hecho"] = True
            AP._SELLADO["ruta"] = sello
            crudas2 = AP.leer_veredictos(destapar_sujeto=True, ruta=archivo,
                                         ruta_sello=sello)
            ok &= _caso(w, "sin la puerta, el sujeto se ve igual",
                        [f for f in crudas2
                         if f["puesto_intra"] == SELLADOS[0]][0]["razon"],
                        "la razon del %d" % SELLADOS[0])
            ok &= _caso(w, "PERO NO QUEDA APUNTADO NINGUN DESTAPE",
                        len(AP.destapes_antes_de_las_clases()), 0)
            ok &= _caso(w, "Y LA COMPROBACION DEJA DE CAER: declara en verde",
                        AP.declarar_clases_escritas(clases)[0], True)
            w("      ESO ES EL AGUJERO, Y ES EL QUE ESTA PUERTA TAPA: el sujeto se")
            w("      quema exactamente igual y el sello sigue saliendo verde.")
        finally:
            AP.leer_veredictos = original
        ok &= _caso(w, "la funcion original queda restaurada",
                    AP.leer_veredictos is original, True)
        w("")

        w("F) LA SEGUNDA MUTACION: SI `CAMPOS_QUE_DESTAPAN` SE QUEDA VACIO, EL")
        w("   TAPADO DEJA DE TAPAR")
        originales = AP.CAMPOS_QUE_DESTAPAN
        try:
            AP.CAMPOS_QUE_DESTAPAN = ()
            AP.olvidar_todo()
            AP._SELLADO["hecho"] = True
            AP._SELLADO["ruta"] = sello
            filas3 = AP.leer_veredictos(ruta=archivo, ruta_sello=sello)
            p3 = {f["puesto_intra"]: f for f in filas3}
            ok &= _caso(w, "sin campos, la razon del sujeto NO se tapa",
                        p3[SELLADOS[0]]["razon"],
                        "la razon del %d" % SELLADOS[0])
        finally:
            AP.CAMPOS_QUE_DESTAPAN = originales
        ok &= _caso(w, "los campos quedan restaurados",
                    AP.CAMPOS_QUE_DESTAPAN, ("clase", "razon"))
        w("")

        w("G) LO QUE ESTA GUARDA NO PUEDE HACER, PROBADO Y NO SOLO ESCRITO:")
        w("   abrir el fichero POR FUERA de estas funciones no apunta nada.")
        AP.olvidar_todo()
        AP._SELLADO["hecho"] = True
        AP._SELLADO["ruta"] = sello
        _por_fuera = [json.loads(l) for l in io.open(archivo, encoding="utf-8")
                      if l.strip()]
        ok &= _caso(w, "leido a mano: la bitacora sigue vacia", AP.bitacora(), [])
        ok &= _caso(w, "y las clases se pueden declarar igual",
                    AP.puede_declarar_clases()[0], True)
        w("      POR ESO EL DOCSTRING LO DICE: ninguna guarda de este repo puede")
        w("      impedirlo. Lo que si puede es que quien se la salte lo haga a")
        w("      sabiendas, y que la declaracion no se pueda escribir despues.")
        w("")
    finally:
        AP.olvidar_todo()
        AP.RUTA_DEL_TURNO = ruta_del_turno_original
        shutil.rmtree(tmp, ignore_errors=True)
        w("H) EL DIRECTORIO FABRICADO SE RETIRA (P.16, quien fabrica limpia)")
        ok &= _caso(w, "el temporal quedo retirado", os.path.exists(tmp), False)
        ok &= _caso(w, "y AP.RUTA_DEL_TURNO queda restaurada a su sede",
                    AP.RUTA_DEL_TURNO, ruta_del_turno_original)
        w("")

        w("I) LA SEDE DE VERDAD DEL TURNO, REMEDIDA (ANADIDO EN LA 194, TAREA 2.a)")
        w("   LO QUE SE COMPRUEBA NO ES QUE EL FICHERO NO EXISTA: es QUE ESTE")
        w("   ARNES NO LO TOCO. Un turno de auditor vivo lo tiene puesto, y exigir")
        w("   su ausencia seria pedir que no haya auditor.")
        turno_despues = _medir_turno_real()
        w("   al entrar: %s | al salir: %s"
          % ("EXISTE, %d bytes" % turno_antes[1] if turno_antes[0] else "NO EXISTE",
             "EXISTE, %d bytes" % turno_despues[1] if turno_despues[0] else "NO EXISTE"))
        w("   sha256 al entrar: %s" % (turno_antes[2][:16] or "(no hay fichero)"))
        w("   sha256 al salir:  %s" % (turno_despues[2][:16] or "(no hay fichero)"))
        ok &= _caso(w, "la sede de verdad NO CAMBIO (existencia, bytes y sha256)",
                    turno_despues, turno_antes)
        w("")

    w("CIFRA casos: los de arriba. VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
