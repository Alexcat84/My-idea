# -*- coding: utf-8 -*-
r"""vuelta197_tarea2b_cerrar_turno_197.py . EL TURNO DEL AUDITOR DE LA VUELTA 197,
CERRADO POR SU CARRIL, Y LA REPARACION DE UNA CAIDA MIA DECLARADA.

DOS COSAS A LA VEZ, Y LAS DOS VAN DICHAS ANTES DE HACER NADA:

1. **LO QUE ESTE FICHERO HACE POR ENCARGO.** La TAREA 2.b de la vuelta 197 anade
   `cerrar_turno()` a `scripts/loop/apertura_del_auditor.py`, y el hallazgo `5.4`
   del acta 197 dice que **el fichero del turno no se limpia al cerrar**, con lo
   que el auditor de la 198 lo heredaria sucio y **tendria que borrarlo para poder
   sellar**. El encargo dice que el carril cierre el turno *"al declarar las
   clases (o al escribir el acta)"*. El auditor de la 197 **ya declaro sus clases
   y ya escribio su acta**, asi que aqui se cierra por la segunda via.

2. **LO QUE ESTE FICHERO REPARA, Y ES UNA CAIDA MIA.** La primera version de
   `scripts/loop/vuelta197_tarea2_mutacion_orden_del_turno.py` restauraba
   `AP.RUTA_DEL_TURNO` a su sede **ANTES** de llamar a `AP.olvidar_todo()`, y
   `olvidar_todo()` **BORRA el fichero del turno**. El arnes se llevo por delante
   `docs/loop/_TURNO_DEL_AUDITOR.json`, que media **329 bytes** con `sha256` LF
   `7203f39fd7f5a54f`, medido en el bloque de apertura de esta vuelta ANTES de la
   primera operacion y sellado en `docs/loop/SALIDA_V197_APERTURA.txt`, bloque
   `D.1`. **Lo cazo el ultimo caso del propio arnes**, el que mide la sede antes y
   despues y CAE SI CAMBIA, y el orden de esas dos lineas ya esta corregido con su
   motivo escrito al lado.

**EL ESTADO NO SE INVENTA: SE RECONSTRUYE DE LA MEDICION SELLADA.** El bloque
`D.1` del sello de apertura publica el contenido literal cercado del fichero, y la
ruta de las clases sale de la corrida de `--estado` de esta misma vuelta. Todo lo
que este fichero escribe esta en esas dos fuentes, **y el fichero reconstruido NO
se hace pasar por el original**: se escribe CERRADO, que es lo que el carril hace,
y con su motivo dentro.

**LO QUE NO SE TOCA:** el sello en disco `SELLO_APERTURA_AUDITOR_V197.json`, que
sigue donde estaba y como estaba, y la guarda `b` de `sellar()`, que lo mira.

USO:
  python scripts/loop/vuelta197_tarea2b_cerrar_turno_197.py
"""
import hashlib
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apertura_del_auditor as AP   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
SALIDA = os.path.join(LOOP, "SALIDA_V197_T2B_CIERRE_DEL_TURNO_197.txt")

VUELTA = "197"
# LOS TRES DATOS DEL TURNO DE LA 197, LEIDOS DEL SELLO DE APERTURA DE ESTA VUELTA
# Y DE LA CORRIDA DE --estado, NO INVENTADOS.
BITACORA_197 = ["git log", "git status", "REPORTE.md", "veredictos"]
CLASES_197 = "docs/loop/_auditor_v197_mis_clases.txt"
BYTES_ANTES_SELLADOS = 329
SHA_ANTES_SELLADO = "7203f39fd7f5a54f"


def medir(ruta):
    if not os.path.isfile(ruta):
        return (False, 0, "")
    d = io.open(ruta, "rb").read()
    return (True, len(d), hashlib.sha256(d.replace(b"\r\n", b"\n")).hexdigest())


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 197, TAREA 2.b: EL TURNO DEL AUDITOR 197, CERRADO POR SU CARRIL")
    w("=" * 78)
    w("")

    w("A) EL ESTADO DEL FICHERO AL ENTRAR, MEDIDO Y NO SUPUESTO")
    ruta = AP.RUTA_DEL_TURNO
    antes = medir(ruta)
    w("   %s" % os.path.relpath(ruta, RAIZ).replace(os.sep, "/"))
    w("   %s" % ("EXISTE, %d bytes, sha256 LF %s" % (antes[1], antes[2][:16])
                 if antes[0] else "NO EXISTE"))
    w("")

    w("B) LO QUE EL SELLO DE APERTURA DE ESTA VUELTA MIDIO, ANTES DE QUE YO")
    w("   TOCARA NADA (docs/loop/SALIDA_V197_APERTURA.txt, bloque D.1)")
    w("   bytes: %d | sha256 LF: %s" % (BYTES_ANTES_SELLADOS, SHA_ANTES_SELLADO))
    w("   bitacora que traia: %s" % ", ".join(BITACORA_197))
    w("   clases declaradas en: %s" % CLASES_197)
    w("   CAIDA MIA, DECLARADA: la primera version de mi arnes de la TAREA 2")
    w("   restauro AP.RUTA_DEL_TURNO ANTES de llamar a olvidar_todo(), y")
    w("   olvidar_todo() BORRA el fichero del turno. Este fichero se llevo por")
    w("   delante la sede de verdad. LO CAZO EL PROPIO ARNES, en su ultimo caso,")
    w("   el que mide la sede antes y despues y CAE SI CAMBIA. El orden de esas")
    w("   dos lineas ya esta corregido con su motivo escrito al lado.")
    w("   EL FICHERO QUE ESTE INSTRUMENTO ESCRIBE NO SE HACE PASAR POR EL")
    w("   ORIGINAL: se escribe CERRADO, que es lo que el carril de la TAREA 2.b")
    w("   hace, y lleva su motivo dentro.")
    w("")

    w("C) EL SELLO EN DISCO, QUE NO SE TOCA NI AQUI NI EN NINGUNA PARTE")
    sello = AP.sello_en_disco(VUELTA)
    w("   sello_en_disco(%s) -> %s" % (VUELTA, sello or "(no existe)"))
    if sello:
        m = medir(sello)
        w("   %d bytes | sha256 LF %s" % (m[1], m[2][:16]))
    w("   LA GUARDA `b` DE sellar() SIGUE MIRANDO ESTE FICHERO, y este fichero")
    w("   no cambia. Cerrar el turno NO borra el sello.")
    w("")

    w("D) EL CIERRE, POR EL CARRIL Y NO A MANO")
    AP._reiniciar_memoria()
    AP._BITACORA.extend(BITACORA_197)
    AP._SELLADO.update({"hecho": True, "ruta": sello, "vuelta": VUELTA})
    AP._CLASES.update({"escritas": True, "ruta": CLASES_197})
    w("   estado montado antes de cerrar, de las dos fuentes selladas:")
    w("      bitacora: %s" % ", ".join(AP.bitacora()))
    w("      sellado:  %r" % (dict(AP._SELLADO),))
    w("      clases:   %r" % (dict(AP._CLASES),))
    ok, informe = AP.cerrar_turno(
        "el auditor de la 197 declaro sus clases y escribio su acta; el turno se "
        "cierra por el carril de la TAREA 2.b de la vuelta 197. El fichero "
        "anterior lo borro un arnes mio y esa caida va declarada en "
        "SALIDA_V197_T2B_CIERRE_DEL_TURNO_197.txt",
        vuelta=VUELTA, ruta_clases=CLASES_197)
    for l in informe:
        w("   " + l)
    w("   VEREDICTO DEL CIERRE: %s" % ("VERDE" if ok else "ROJO"))
    w("")

    w("E) EL FICHERO AL SALIR, RELEIDO DEL DISCO")
    despues = medir(ruta)
    w("   %s" % ("EXISTE, %d bytes, sha256 LF %s" % (despues[1], despues[2][:16])
                 if despues[0] else "NO EXISTE"))
    d = json.load(io.open(ruta, encoding="utf-8"))
    w("   vivo.abierto: %r" % ((d.get("vivo") or {}).get("abierto"),))
    w("   vueltas en `cerrados`: %s" % ", ".join(sorted(d.get("cerrados") or {})))
    w("   bitacora guardada dentro del cierre, como constancia: %s"
      % ", ".join((d.get("cerrados") or {}).get(VUELTA, {}).get("bitacora") or []))
    w("")

    w("F) LA PRUEBA DE QUE UN TURNO NUEVO EMPIEZA LIMPIO SIN BORRAR NADA")
    AP._reiniciar_memoria()
    cargo = AP._cargar_turno()
    w("   _cargar_turno() devuelve: %r (False = no hay turno VIVO que cargar)"
      % cargo)
    w("   bitacora tras cargar: %s" % (", ".join(AP.bitacora()) or "(vacia)"))
    puede, motivo = AP.puede_sellar()
    w("   PUEDE SELLAR: %s" % ("SI" if puede else "NO"))
    w("      motivo: %s" % motivo)
    w("   el fichero del turno SIGUE EN DISCO: %s"
      % ("SI, %d bytes" % os.path.getsize(ruta) if os.path.exists(ruta) else "NO"))
    w("   vueltas cerradas que el turno nuevo VE: %s"
      % (", ".join(sorted(AP.cerrados())) or "(ninguna)"))
    puede_leer, motivo_leer = AP.puede_leer_reporte(vuelta=VUELTA)
    w("   PUEDE LEER REPORTE.md para la vuelta %s: %s" % (VUELTA,
                                                          "SI" if puede_leer else "NO"))
    w("      motivo: %s" % motivo_leer)
    w("")
    veredicto = puede and not cargo and not AP.bitacora() and os.path.exists(ruta)
    w("VEREDICTO: %s" % ("VERDE" if veredicto else "ROJO"))
    t = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (SALIDA, len(t.encode("utf-8"))))
    return 0 if veredicto else 1


if __name__ == "__main__":
    sys.exit(main())
