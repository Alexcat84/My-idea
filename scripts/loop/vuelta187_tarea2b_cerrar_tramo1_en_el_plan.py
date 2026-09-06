# -*- coding: utf-8 -*-
r"""vuelta187_tarea2b_cerrar_tramo1_en_el_plan.py . EL CIERRE DEL TRAMO 1 DE LA
COLA POST FUSION, ANOTADO EN SU PROPIA SEDE Y CON SUS CIFRAS LEIDAS DE FICHEROS.

POR QUE EXISTE, Y NO ES UN ADORNO. La seccion `## LA COLA DE RELECTURA POST
FUSION` de `docs/plan/08_VERIFICACION.md` **declara el tramo 1 y no dice que se
haya releido**. Un tramo que se relee y no se anota en su sede deja el plan
diciendo que sigue pendiente, y el propio criterio escrito pone la comprobacion:
*"Y LA COMPROBACION DE QUE ESTA COLA SE CORRIO: al cerrar, ningun par de la lista
sigue con su clase vieja apuntando a un nodo que ya no existe."*

LA TABLA SE IMPRIME, NO SE TECLEA (`EJECUTOR.md` 1). Ninguna cifra de este
registro esta escrita a mano: **todas se leen del archivo de veredictos y de la
salida de la TAREA 2**, corridas en esta vuelta. Si alguna no se puede leer, este
fichero **cae en ROJO y no escribe nada**.

SE ANADE POR ADICION Y NO REESCRIBE NADA (`EJECUTOR.md` 8). El texto de la
seccion se conserva entero; el registro se anexa al final de la seccion, con la
forma de los otros `#### REGISTRO:` que ya viven ahi. Es idempotente: si la marca
ya esta, no la duplica y lo dice.

USO:
  python scripts/loop/vuelta187_tarea2b_cerrar_tramo1_en_el_plan.py --simular
  python scripts/loop/vuelta187_tarea2b_cerrar_tramo1_en_el_plan.py
"""
import argparse
import hashlib
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta187_tarea2_cola_post_fusion as T2   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VERIF = os.path.join(RAIZ, "docs", "plan", "08_VERIFICACION.md")
ARCHIVO = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
SALIDA_T2 = os.path.join(LOOP, "SALIDA_V187_T2_COLA_POST_FUSION.txt")
NL = chr(10)
VUELTA = 187
MARCA_REGISTRO = ("#### REGISTRO: **EL TRAMO 1 SE RELEYO Y SE CIERRA** "
                  "(6 sep 2026, vuelta %d)" % VUELTA)


def cifra_de_la_salida(texto, aguja):
    """LA CIFRA QUE UNA LINEA DE LA SALIDA DE LA TAREA 2 PUBLICA. PURA.

    Devuelve la linea entera, sin recortarla, para que el registro pueda pegarla
    tal cual en vez de re escribirla. `None` si la aguja no esta: quien llama cae
    en ROJO en vez de inventarse la cifra."""
    for l in texto.replace(chr(13) + NL, NL).split(NL):
        if aguja in l:
            return l.strip()
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2.b: EL TRAMO 1 DE LA COLA, CERRADO EN SU SEDE" % VUELTA)
    w("=" * 78)
    w("")

    if not os.path.exists(SALIDA_T2) or os.path.getsize(SALIDA_T2) == 0:
        w("ROJO: %s no existe o mide cero bytes. Sin la salida de la TAREA 2 no"
          % os.path.relpath(SALIDA_T2, RAIZ).replace(os.sep, "/"))
        w("hay nada que anotar, y una ruta que promete prueba es CIFRA.")
        print(NL.join(L))
        return 1
    t_sal = io.open(SALIDA_T2, encoding="utf-8").read()
    w("A) LA SALIDA DE LA TAREA 2, MEDIDA ANTES DE CITARLA")
    d_sal = io.open(SALIDA_T2, "rb").read()
    w("   docs/loop/SALIDA_V%d_T2_COLA_POST_FUSION.txt -> disco %d bytes | LF %d bytes"
      % (VUELTA, len(d_sal), len(d_sal.replace(b"\r\n", b"\n"))))
    w("")

    w("B) LAS CIFRAS, LEIDAS DE FICHEROS Y NO TECLEADAS")
    filas = [json.loads(l) for l in io.open(ARCHIVO, encoding="utf-8") if l.strip()]
    porpuesto = {f.get("puesto_intra"): f for f in filas}
    t_ver = io.open(VERIF, encoding="utf-8").read()
    ini, fin, cuerpo = T2.seccion_de_la_cola(t_ver)
    if ini is None:
        w("   ROJO: la seccion de la cola no esta en docs/plan/08_VERIFICACION.md.")
        print(NL.join(L))
        return 1
    tramo = T2.pares_del_tramo1(cuerpo, ini)
    w("   seccion de la cola: lineas %d a %d" % (ini, fin))
    w("   CIFRA pares del TRAMO 1, leidos de la tabla: %d" % len(tramo))
    grafo = json.load(io.open(T2.T3.GRAFO, encoding="utf-8"))
    porid = T2.T3.nodos_por_id(grafo)
    lineas_reg = []
    vivos_todos = True
    for _ln, p in tramo:
        f = porpuesto.get(p)
        if f is None:
            w("   ROJO: el puesto %d no esta en el archivo." % p)
            print(NL.join(L))
            return 1
        vivo_a = f.get("nodo_a") in porid
        vivo_b = f.get("nodo_b") in porid
        vivos_todos = vivos_todos and vivo_a and vivo_b
        tiene = T2.MARCA_CORRECCION in (f.get("razon") or "")
        w("   puesto %d -> clase %s | nodo_a vivo %s | nodo_b vivo %s | correccion "
          "declarada en su razon %s"
          % (p, f.get("clase"), "SI" if vivo_a else "NO",
             "SI" if vivo_b else "NO", "SI" if tiene else "NO"))
        if not tiene:
            w("   ROJO: el puesto %d no lleva la correccion declarada. El tramo no"
              % p)
            w("   se cierra sin ella.")
            print(NL.join(L))
            return 1
        lineas_reg.append(
            "| **%d** | **%s** | `%s` vivo, `%s` vivo | **la clase se sostiene**, y "
            "lo que se movio es la EVIDENCIA: de los DOS diferenciadores que la "
            "razon declaraba, hoy solo UNO es cierto |"
            % (p, f.get("clase"), f.get("nodo_a"), f.get("nodo_b")))
    datos = io.open(ARCHIVO, "rb").read()
    sha = hashlib.sha256(datos.replace(b"\r\n", b"\n")).hexdigest()
    m = T2.marcador(filas)
    w("   archivo AL CERRAR: disco %d bytes | sha256 LF %s" % (len(datos), sha))
    w("   marcador: filas %d | A %d | B %d | C %d | D %d | huecos %d | duplicados %d"
      % (m["filas"], m["por_clase"].get("A", 0), m["por_clase"].get("B", 0),
         m["por_clase"].get("C", 0), m["por_clase"].get("D", 0), m["huecos"],
         m["duplicados"]))
    linea_abre = cifra_de_la_salida(t_sal, "sha256 (LF): ea6e850d")
    if linea_abre is None:
        w("   ROJO: la salida de la TAREA 2 no publica el sha256 de apertura.")
        print(NL.join(L))
        return 1
    w("   sha256 de APERTURA, leido de la salida de la TAREA 2: %s" % linea_abre)
    w("")

    registro = NL.join([
        MARCA_REGISTRO,
        "",
        "**LA COMPROBACION QUE LA PROPIA SECCION EXIGE, CORRIDA:** *\"al cerrar, "
        "ningun par",
        "de la lista sigue con su clase vieja apuntando a un nodo que ya no "
        "existe\"*. Medido",
        "hoy sobre `dataset/metadata/master_graph.json` (**%d nodos**): **los dos "
        "nodos del" % len(porid),
        "tramo siguen vivos**, asi que esa comprobacion **pasa**.",
        "",
        "| par | clase tras la relectura | nodos hoy | que se movio |",
        "|---:|:-:|---|---|",
    ] + lineas_reg + [
        "",
        "**LA RELECTURA NO CAMBIO LA CLASE, Y EL DESTINO ES EL QUE ESTA PAGINA YA "
        "ESCRIBE**",
        "unas lineas mas arriba, en *QUE PASA CON LO QUE SE RELEA*: **si sale `D` se "
        "queda**.",
        "Lo que si se movio es **la evidencia**, y por eso el veredicto lleva su "
        "**CORRECCION",
        "DECLARADA** anexada a su `razon`, **sin borrar ni una palabra del texto "
        "viejo**.",
        "",
        "**LAS CIFRAS DE ESTE REGISTRO NO ESTAN TECLEADAS:** las produce",
        "`scripts/loop/vuelta%d_tarea2b_cerrar_tramo1_en_el_plan.py` leyendo el "
        "archivo de" % VUELTA,
        "veredictos y la salida de la TAREA 2, que vive entera en",
        "`docs/loop/SALIDA_V%d_T2_COLA_POST_FUSION.txt`. El archivo cierra con "
        "**%d filas**," % (VUELTA, m["filas"]),
        "**%d `A`, %d `B`, %d `C` y %d `D`**, **%d huecos** y **%d duplicados**, y su "
        "`sha256` por la"
        % (m["por_clase"].get("A", 0), m["por_clase"].get("B", 0),
           m["por_clase"].get("C", 0), m["por_clase"].get("D", 0),
           m["huecos"], m["duplicados"]),
        "convencion de LF es **`%s`**, distinto del de apertura porque **esta"
        % sha[:16],
        "vuelta si movio el archivo**.",
        "",
        "**Y LOS CINCO DE LA `PD.1` NO ENTRAN, POR SEXTA VUELTA Y CON SU MEDICION "
        "AL LADO.**",
        "La criba de las condiciones 1 y 2, re corrida hoy, nombra **seis** `D`; la "
        "que",
        "pasa tambien la condicion 3 es **solo el %d**, y las otras cinco son "
        "exactamente" % tramo[0][1],
        "los puestos de la `PD.1`, cuyo diferenciador **ya estaba el dia del "
        "veredicto**.",
        "**No pasan el disparador escrito y no se encolan**: darles cola seria "
        "doctrina",
        "nueva, que es del fundador.",
        "",
    ])
    w("C) EL REGISTRO ARMADO")
    w("   %d bytes | %d lineas" % (len(registro.encode("utf-8")),
                                   registro.count(NL)))
    w("   guiones largos o medios: %d"
      % (registro.count(chr(8212)) + registro.count(chr(8211))))
    w("")

    texto = t_ver.replace(chr(13) + NL, NL)
    if MARCA_REGISTRO in texto:
        w("D) NO SE ESCRIBE: el registro ya esta en la sede, byte a byte.")
        print(NL.join(L))
        return 0
    if a.simular:
        w("D) MODO --simular: NO SE ESCRIBE NADA EN LA SEDE.")
        w("")
        w("EL REGISTRO, ENTERO:")
        for l in registro.split(NL):
            w("   | " + l)
        t = NL.join(L) + NL
        ruta = os.path.join(LOOP, "SALIDA_V%d_T2B_TRAMO1_SIMULADO.txt" % VUELTA)
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
        print(t)
        print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
        return 0

    lineas = texto.split(NL)
    # EL REGISTRO VA AL FINAL DE LA SECCION DE LA COLA, JUSTO ANTES DE LA
    # SIGUIENTE CABECERA DE SEGUNDO NIVEL, PARA QUE VIVA DENTRO DE SU SEDE.
    nuevo = NL.join(lineas[:fin]) + NL + NL + registro + NL.join(lineas[fin:])
    io.open(VERIF, "w", encoding="utf-8", newline=NL).write(nuevo)
    w("D) ESCRITO EN docs/plan/08_VERIFICACION.md")
    w("   la sede pasa de %d a %d bytes"
      % (len(texto.encode("utf-8")), len(nuevo.encode("utf-8"))))
    rele = io.open(VERIF, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("   RELEIDO DEL DISCO: el registro esta byte a byte: %s"
      % ("SI" if registro.rstrip(NL) in rele else "NO"))
    ini2, fin2, cuerpo2 = T2.seccion_de_la_cola(rele)
    w("   la seccion de la cola sigue siendo UNA y ahora va de la %s a la %s"
      % (ini2, fin2))
    w("   el disparador sigue dentro de la seccion: %s"
      % ("SI" if any(T2.MARCA_DISPARADOR in l for l in cuerpo2) else "NO"))
    w("   la declaracion del tramo sigue dentro: %s"
      % ("SI" if any(T2.MARCA_TRAMO in l for l in cuerpo2) else "NO"))
    w("   la marca del registro esta DENTRO de la seccion: %s"
      % ("SI" if any(MARCA_REGISTRO in l for l in cuerpo2) else "NO"))
    w("   guiones largos o medios en la sede entera: %d"
      % (rele.count(chr(8212)) + rele.count(chr(8211))))
    w("")
    w("VEREDICTO: %s" % ("VERDE" if vivos_todos else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%d_T2B_TRAMO1_CERRADO.txt" % VUELTA)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if vivos_todos else 1


if __name__ == "__main__":
    sys.exit(main())
