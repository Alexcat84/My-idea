# -*- coding: utf-8 -*-
r"""vuelta182_tarea4_entrar_a_la_cola.py . LAS `D` QUE EL INSTRUMENTO NOMBRA
ENTRAN A LA COLA DE RELECTURA POST FUSION, Y SE DECLARA EL TRAMO.

QUE HACE, Y ES LO UNICO QUE HACE: lee
`docs/loop/SALIDA_V182_T3_COLA.json`, que es lo que produjo el instrumento de la
TAREA 3, y **anade una seccion nueva a `docs/plan/08_VERIFICACION.md`** con la
fila de cada `D` nombrada y con el tramo declarado. **La tabla se genera del
fichero, no se teclea** (`EJECUTOR.md` 1, LA TABLA SE IMPRIME, NO SE TECLEA).

LO QUE NO HACE, Y ES LA MITAD QUE IMPORTA: **NO relee ningun par, NO cambia
ninguna clase y NO toca el archivo de veredictos.** El encargo lo dice con estas
palabras: *"En esta vuelta se entra a la cola y se declara el tramo; no se releen
543 pares, que es justo lo que la decision evita"*.

Y NO BORRA NADA. La lista del 12 ago 2026 se queda entera donde esta; esto es una
seccion NUEVA debajo, con su fecha y su procedencia, porque una correccion que
tapa lo que corrige no se puede auditar (`EJECUTOR.md` 8).

SOBRE `verificar_mapas_destejido.py`: `EJECUTOR.md` 1 lo exige para **toda tabla
de particion (fila = destino, origenes, motivo)**. La tabla de esta cola **no es
de particion**: sus filas son `par | clase | que le pasa | tras que operacion`, no
hay destino ni origenes, y no reparte nada. **Se dice en vez de correr un
instrumento sobre una tabla que no es la suya y publicar un verde que no
significa nada.**

USO:
  python scripts/loop/vuelta182_tarea4_entrar_a_la_cola.py --simular
  python scripts/loop/vuelta182_tarea4_entrar_a_la_cola.py
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
COLA_JSON = os.path.join(LOOP, "SALIDA_V182_T3_COLA.json")
SALIDA_T3 = os.path.join(LOOP, "SALIDA_V182_T3_DIFERENCIADOR.txt")
PLAN = os.path.join(RAIZ, "docs", "plan", "08_VERIFICACION.md")
NL = chr(10)

ANCLA = "### LOS SIETE DEL PIVOTE NO ENTRAN, y hay que decir por que"
MARCA = "### LA ENTRADA POR EL DIFERENCIADOR MOVIDO (5 sep 2026, vuelta 182)"


def armar(filas, cifras):
    p = []
    w = p.append
    w(MARCA)
    w("")
    w("**Procedencia, y ninguna cifra de esta seccion esta tecleada:** la produjo")
    w("`scripts/loop/vuelta182_tarea3_diferenciador_movido.py`, su salida entera vive")
    w("en `docs/loop/SALIDA_V182_T3_DIFERENCIADOR.txt` (**%d bytes**) y la lista en"
      % cifras["bytes_salida"])
    w("crudo en `docs/loop/SALIDA_V182_T3_COLA.json` (**%d bytes**). Esta seccion la"
      % cifras["bytes_json"])
    w("escribe `scripts/loop/vuelta182_tarea4_entrar_a_la_cola.py` leyendo ese JSON.")
    w("")
    w("**LAS TRES CONDICIONES DE LA LESION EXACTA, Y LA CRIBA QUE HACEN, CONTADA:**")
    w("")
    w("| condicion | cuantas `D` la pasan |")
    w("|---|---:|")
    w("| todas las `D` del archivo | **%d** |" % cifras["d_totales"])
    w("| 1. su razon **declara** un diferenciador | **%d** |" % cifras["declaran"])
    w("| 2. y hoy el otro nodo **si lo tiene** | **%d** |" % cifras["con_lesion"])
    w("| 3. y el paso **entra despues** del veredicto | **%d** |" % cifras["confirmadas"])
    w("")
    w("**Una `D` cuya razon no declara ningun diferenciador no puede tener un")
    w("diferenciador movido**, y por eso la primera criba es la que mas quita: no es")
    w("una comodidad, es que no hay nada que se le haya movido debajo.")
    w("")
    if not filas:
        w("**NINGUNA `D` PASA LAS TRES CONDICIONES.** La lista de esta seccion queda")
        w("vacia y se dice, en vez de rellenarla.")
        return NL.join(p) + NL
    w("**LA LISTA, EN LA MISMA FORMA QUE LA DEL 12 AGO 2026:**")
    w("")
    w("| par | clase | que le pasa | tras que operacion |")
    w("|---:|---|---|---|")
    for f in filas:
        w("| **%d** | **%s** | el diferenciador declarado de su razon **esta hoy en "
          "los pasos de `%s`** (paso %s, cobertura %.2f) | fusion del **%s**, "
          "posterior a su veredicto del **%s** |"
          % (f["puesto"], f["clase"], f["carece"], f["indice_paso"],
             f["cobertura"], f.get("fecha_paso") or "(sin fechar)",
             f.get("fecha_veredicto") or "(sin fechar)"))
    w("")
    n = len(filas)
    w("**EL TRAMO, DECLARADO AQUI Y NO IMPROVISADO DESPUES.** %s se relee%s"
      % ("Esta unica `D`" if n == 1 else "Estas %d `D`" % n, "" if n == 1 else "n"))
    w("**por tramos en las vueltas siguientes**, no en la que las encola: la vuelta")
    w("182 **entra a la cola y declara el tramo**, que es literalmente lo que su")
    w("encargo manda. **TRAMO 1 y unico con lo medido hoy: %s de arriba**,"
      % ("el unico par" if n == 1 else "los %d pares" % n))
    w("y se relee **entero o no cuenta**. Si el instrumento volviera a correr y")
    w("nombrara mas, cada nuevo grupo abre **su propio tramo con su fecha**, para que")
    w("un tramo cerrado no se pueda reabrir por la puerta de atras.")
    w("")
    w("**LO QUE PASA CON LO QUE SE RELEA es lo que ya dice esta pagina** unas lineas")
    w("mas abajo, en *QUE PASA CON LO QUE SE RELEA*, y **no se cambia ni una letra**:")
    w("si sale `A` entra en la fusion que le corresponda y su perdida se nombra")
    w("antes; si sale `D` se queda; si sale `B` otra vez va a la lista de decisiones")
    w("del inventario final. **Esta cola no estrena ningun destino nuevo.**")
    w("")
    w("**Y LAS `A` NO ENTRAN AQUI, CON SU CENSO DELANTE:** **%d** `A` en el archivo,"
      % cifras["a_total"])
    w("de ellas **%d ejecutadas** (uno de sus dos nodos ya no esta en el grafo) y"
      % cifras["a_ejec"])
    w("**%d pendientes** (los dos siguen vivos). De las pendientes, **%d tienen hoy"
      % (cifras["a_pend"], cifras["a_rancias"]))
    w("su diferenciador declarado en el otro nodo** y quedan **marcadas RANCIAS por")
    w("`P.5`**, que es la regla que ya existe: su vigencia se comprueba **antes de")
    w("ejecutar**. **No se encolan**, por la PREGUNTA 2 de la decision del fundador.")
    w("Son los puestos **%s**." % cifras["rancias"])
    return NL.join(p) + NL


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("VUELTA 182, TAREA 4: LAS D NOMBRADAS ENTRAN A LA COLA")
    w("")

    for r in (COLA_JSON, SALIDA_T3, PLAN):
        w("   %-58s %s"
          % (os.path.relpath(r, RAIZ).replace(os.sep, "/"),
             ("%d bytes" % os.path.getsize(r)) if os.path.exists(r) else "NO EXISTE"))
        if not os.path.exists(r) or os.path.getsize(r) == 0:
            w("ROJO: falta una prueba o mide cero bytes. No se escribe nada.")
            print(NL.join(L))
            return 1
    w("")

    filas = json.load(io.open(COLA_JSON, encoding="utf-8"))
    texto_t3 = io.open(SALIDA_T3, encoding="utf-8").read().replace(chr(13) + NL, NL)

    def cifra(aguja):
        for l in texto_t3.split(NL):
            if aguja in l:
                return int(l.rsplit(":", 1)[1].strip())
        return -1

    cifras = {
        "d_totales": cifra("CIFRA D totales"),
        "declaran": cifra("CIFRA D que declaran diferenciador"),
        "con_lesion": cifra("CIFRA D con LESION EXACTA (condiciones 1 y 2)"),
        "confirmadas": cifra("CIFRA D con las TRES condiciones"),
        "bytes_salida": os.path.getsize(SALIDA_T3),
        "bytes_json": os.path.getsize(COLA_JSON),
    }
    rancias = [l.rsplit(" ", 1)[1] for l in texto_t3.split(NL)
               if "RANCIA POR P.5: puesto" in l]
    cifras["rancias"] = ", ".join(rancias)
    cifras["a_total"] = cifra("CIFRA A")
    cifras["a_ejec"] = cifra("CIFRA A EJECUTADAS (uno de los dos nodos ya no esta en el grafo)")
    cifras["a_pend"] = cifra("CIFRA A PENDIENTES (los dos nodos siguen vivos)")
    cifras["a_rancias"] = len(rancias)

    w("A) LAS CIFRAS, LEIDAS DE LA SALIDA DE LA TAREA 3 Y NO TECLEADAS")
    for k in ("d_totales", "declaran", "con_lesion", "confirmadas",
              "a_total", "a_ejec", "a_pend", "a_rancias"):
        w("   %-12s -> %s" % (k, cifras[k]))
    w("   filas del JSON de la cola: %d" % len(filas))
    w("   los puestos que entran: %s"
      % (", ".join(str(f["puesto"]) for f in filas) or "(ninguno)"))
    if len(filas) != cifras["confirmadas"]:
        w("   ROJO: el JSON trae %d filas y la salida dice %d. No se escribe nada."
          % (len(filas), cifras["confirmadas"]))
        print(NL.join(L))
        return 1
    w("   EL JSON Y LA SALIDA CALZAN.")
    w("")

    seccion = armar(filas, cifras)
    w("B) LA SECCION ARMADA: %d bytes | %d lineas"
      % (len(seccion.encode("utf-8")), seccion.count(NL)))
    w("   guiones largos o medios: %d"
      % (seccion.count(chr(8212)) + seccion.count(chr(8211))))
    w("")

    plano = io.open(PLAN, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("C) LA SEDE, ANTES: %d bytes | %d lineas"
      % (len(plano.encode("utf-8")), plano.count(NL)))
    if MARCA in plano:
        w("   LA SECCION YA ESTA: no se duplica. IDEMPOTENTE.")
        print(NL.join(L))
        return 0
    if ANCLA not in plano:
        w("   ROJO: no se encuentra el ancla %r" % ANCLA)
        print(NL.join(L))
        return 1
    nuevo = plano.replace(ANCLA, seccion + NL + ANCLA, 1)
    w("   LA SEDE, DESPUES: %d bytes | %d lineas"
      % (len(nuevo.encode("utf-8")), nuevo.count(NL)))
    w("   CRECE EN: %d bytes"
      % (len(nuevo.encode("utf-8")) - len(plano.encode("utf-8"))))
    w("   NADA SE BORRA: la lista del 12 ago sigue entera. Lineas que desaparecen: %d"
      % len([l for l in plano.split(NL) if l not in nuevo.split(NL)]))
    w("")
    if a.simular:
        w("D) MODO --simular: NO se escribe en docs/plan/08_VERIFICACION.md")
        w("")
        w("LA SECCION, ENTERA:")
        for l in seccion.split(NL):
            w("   | " + l)
    else:
        io.open(PLAN, "w", encoding="utf-8", newline=NL).write(nuevo)
        rele = io.open(PLAN, encoding="utf-8").read().replace(chr(13) + NL, NL)
        w("D) ESCRITA EN docs/plan/08_VERIFICACION.md")
        w("   RELEIDA DEL DISCO, la seccion esta byte a byte: %s"
          % ("SI" if seccion.rstrip(NL) in rele else "NO"))
        w("   disco %d bytes" % os.path.getsize(PLAN))
        w("   la lista del 12 ago sigue: %s"
          % ("SI" if "### LA LISTA, barrida el 12 ago 2026" in rele else "NO"))
        w("   el ancla sigue: %s" % ("SI" if ANCLA in rele else "NO"))

    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_T4_COLA.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
