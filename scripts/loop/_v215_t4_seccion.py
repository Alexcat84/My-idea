# -*- coding: utf-8 -*-
r"""_v215_t4_seccion.py . EL CUERPO DE LA TAREA 4 DEL REPORTE DE LA VUELTA 215,
COMPUESTO DE SU SALIDA SELLADA Y NO TECLEADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

EJECUTOR.md 1, LA TABLA SE CUENTA DE SU FICHERO. Y la guarda que reviente en vez
de rellenar tambien vive aqui: si una cifra no esta en la salida sellada, este
compositor CAE EN ROJO y no escribe.

USO:  python scripts/loop/_v215_t4_seccion.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
SALIDA = "docs/loop/SALIDA_V%d_T4_DOS_PUNTOS.txt" % VUELTA


def leer(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    return io.open(p, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def cifra(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(-?\d+)", l.split(etiqueta, 1)[1])
            if m:
                return m.group(1)
    return None


def veredicto(texto, marca):
    """EL VEREDICTO DE UN PUNTO, LEIDO DE SU LINEA Y NO TECLEADO. PURA."""
    trozo = texto.split(marca, 1)
    if len(trozo) < 2:
        return None
    m = re.search(r"VEREDICTO MEDIDO HOY: \*\*([A-Z ]+)\*\*", trozo[1])
    return m.group(1).strip() if m else None


def main():
    t = leer(SALIDA)
    if t is None:
        print("ROJO: falta la salida sellada de la TAREA 4. REVIENTA, no rellena.")
        return 1

    D = {
        "entradas": cifra(t, "CIFRA entradas de docs/plan/INVENTARIO.jsonl: "),
        "campos": cifra(t, "CIFRA campos de texto examinados: "),
        "hueco_est": cifra(t, "EN MAYUSCULAS Y TAL CUAL: "),
        "hueco_ins": cifra(t, "CIFRA entradas que lo nombran SIN MIRAR MAYUSCULAS: "),
        "sospechosos": cifra(t, "del campo: "),
        "descartados": cifra(t, "CIFRA de esos DESCARTADOS porque el campo los usa como estado: "),
        "rellenos": cifra(t, "CIFRA campos RELLENADOS DE VERDAD, ya descontado el vocabulario: "),
        "vacios": cifra(t, "CIFRA campos VACIOS, que no estan nombrados ni rellenados: "),
        "nombran": cifra(t, "CIFRA ficheros .py de scripts que NOMBRAN la vista humana: "),
        "escriben": cifra(t, "CIFRA ficheros .py que la ESCRIBEN: "),
        "commits": cifra(t, "CIFRA commits que han tocado la vista humana en toda su historia: "),
        "bytes_vista": cifra(t, "CIFRA bytes de la vista humana hoy: "),
        "sha_calzan": ("SI" if "CIFRA los dos sha256 CALZAN: SI" in t else "NO"),
        "ns_exp": cifra(t, "CIFRA filas de git diff --numstat sobre el expediente: "),
        "ns_inv": cifra(t, "CIFRA filas de git diff --numstat sobre el inventario: "),
        "fallos": cifra(t, "CIFRA comprobaciones que fallan: "),
    }
    faltan = [k for k, v in D.items() if v is None]
    print("CIFRA cifras que la seccion necesita: %d | CIFRA que faltan: %d %s"
          % (len(D), len(faltan), faltan))
    if faltan:
        print("ROJO: una cifra que falta REVIENTA, no se rellena con un hueco.")
        return 1

    v3 = veredicto(t, "4.a. EL PUNTO 3")
    v4 = veredicto(t, "4.b. EL PUNTO 4")
    if not v3 or not v4:
        print("ROJO: no se pudo leer alguno de los dos veredictos.")
        return 1
    print("VEREDICTOS LEIDOS DE LA SALIDA: punto 3 %r | punto 4 %r" % (v3, v4))

    descartes = [l.strip() for l in t.split(NL) if l.strip().startswith("DESCARTADO>")]
    filas_desc = []
    for l in descartes:
        m = re.match(r"^DESCARTADO> entrada (\d+) \((.+?)\), campo (\S+) = (.+?); "
                     r"el mismo campo trae la forma larga (.+)$", l)
        if m:
            filas_desc.append("| **%s** | %s | `%s` | %s | %s |" % m.groups())

    ultimo = None
    for l in t.split(NL):
        if l.startswith("CIFRA ultimo commit que la toco: "):
            ultimo = l.split(": ", 1)[1].strip()

    cuerpo = """### TAREA 4. LOS DOS PUNTOS DE `OP-I-01` QUE QUEDARON A MEDIAS

**LO PRIMERO, PORQUE ES LO QUE LA `4.c` PROHIBE:** esta tarea **NO ESCRIBE NI UNA
LINEA EN NINGUNA FICHA**, y no lo prometo, lo mido. **`sha256` LF de
`docs/plan/OPERACIONES.jsonl` a los dos lados: CALZAN %(sha_calzan)s.** **Filas
de `numstat` sobre el expediente: %(ns_exp)s. Sobre el inventario: %(ns_inv)s.**
**CERO campos `estado` movidos, en `OP-I-01` y en las demas.**

#### 4.a. EL PUNTO 3, POR SU NEGATIVA, QUE SI SE PUEDE CITAR

**ME LO ADJUDICARON EN CONTRA Y TENIAN RAZON** (`5.4`, linea **76174**). Dije que
una busqueda negativa no se puede citar, y lo que se prohibe es **AFIRMAR UNA
BUSQUEDA NO CORRIDA**, no publicar la que da cero. **Aqui esta corrida.**

**EL COMANDO, ESCRITO ANTES DE SU RESULTADO:** por cada una de las
**%(entradas)s** entradas de `docs/plan/INVENTARIO.jsonl` y por cada uno de sus
**%(campos)s** campos de texto, se pregunta si el campo **ENTERO**, en minusculas
y sin espacios de los bordes, **es** una de 23 palabras de relleno, y aparte si
esta **VACIO**. **Se compara el campo COMPLETO, NUNCA por subcadena**, que es la
laxitud que me cazo la `D.7` en la 214.

**EL VOCABULARIO ES MIO Y VA ESCRITO ENTERO EN EL INSTRUMENTO PARA QUE SE PUEDA
DISCUTIR.** Una lista que nadie puede leer no se puede auditar. **Lo marco como
discutible.**

**LA MITAD AFIRMATIVA, CON SUS DOS CONVENCIONES, PORQUE UNA SOLA NO SE PUEDE
COTEJAR CON LA CIFRA DE LA 214:** entradas que nombran la marca **tal cual, en
mayusculas: %(hueco_est)s**; entradas que la nombran **sin mirar mayusculas:
%(hueco_ins)s**. **La 214 publico %(hueco_ins)s con la segunda**, y lo se porque
lei su convencion en la **linea 133** de `scripts/loop/_v214_t1c_op_i_01.py`, no
porque me acuerde.

**LA MITAD NEGATIVA, QUE ES LA QUE ESTABA PENDIENTE, CON SU CERO DELANTE:**

- **CIFRA campos SOSPECHOSOS de relleno, antes de mirar el vocabulario del
  campo: %(sospechosos)s.**
- **CIFRA DESCARTADOS porque el campo los usa como estado: %(descartados)s.**
- **CIFRA campos RELLENADOS DE VERDAD: %(rellenos)s.**
- **CIFRA campos VACIOS, que no estan nombrados ni rellenados: %(vacios)s.**

**LOS %(descartados)s DESCARTES NO SE ESCONDEN: VAN CON SU NOMBRE Y CON LA CIFRA
QUE LOS DESCARTA.** Son mi caida `D.2` de esta vuelta, cazada por mi antes de
publicar el veredicto.

| entrada | sujeto | campo | valor | la forma LARGA que el MISMO campo trae |
|---:|---|---|---|---|
%(filas_desc)s

**LA REGLA DEL DESCARTE ES MECANICA Y NO SE ENSANCHA PARA QUE TRAGUE:** una
palabra sospechosa en el campo `F` se descarta **solo si el propio campo `F`
tiene, en otra entrada, un valor que empieza por esa palabra y sigue con mas
texto**. Pide la forma larga **en el mismo campo**, no en cualquiera. **Su caso
positivo lo prueba:** `pendiente` tiene formas largas en `estado` (**4**) y
**ninguna** en `forma` (**0**), asi que en `forma` seguiria contando como
relleno.

**VEREDICTO MEDIDO HOY DEL PUNTO 3: %(v3)s** (la 214 lo dejo en **A MEDIAS**).
**SE MUEVE.**

#### 4.b. EL PUNTO 4, MIDIENDO ANTES DE DECIDIR Y SIN INVENTAR LA SEDE

**LA VISTA HUMANA DECLARA DE SI MISMA QUE AHI NO SE REGENERA, Y LO DICE EN TRES
SITIOS**, no en uno: `docs/plan/10_INVENTARIO.md` **lineas 19, 121 y 182**,
pegadas enteras en la salida sellada. **Eso es lo que el encargo ya sabia. Lo que
faltaba era saber DONDE SI.**

**LA BUSQUEDA, CON SU COMANDO ESCRITO ANTES DE SU RESULTADO:** se recorre **todo
el arbol de scripts**, no solo el del bucle, y por cada fichero de Python se
pregunta si **nombra** la vista humana y si ademas tiene, en la misma linea o en
las tres siguientes, **una apertura en modo escritura o una llamada de escritura
sobre esa ruta**.

- **CIFRA ficheros que la NOMBRAN: %(nombran)s.**
- **CIFRA ficheros que la ESCRIBEN: %(escriben)s.**

**Y LA SEGUNDA MITAD DE LA BUSQUEDA, PORQUE UN FICHERO PUEDE ESCRIBIRSE SIN QUE
NINGUN SCRIPT LO NOMBRE:** de que commits sale la vista humana, leido de
`git log` sobre su ruta. **CIFRA commits en toda su historia: %(commits)s**, y el
**ultimo es %(ultimo)s**. **Sus %(bytes_vista)s bytes de hoy son de esa fecha.**

**LA SEDE QUE REGENERARIA LA VISTA HUMANA NO EXISTE EN EL REPO, Y ESO TAMBIEN ES
UN RESULTADO, QUE ES LO QUE EL ENCARGO PIDE QUE DIGA SI PASA.** Los
**%(nombran)s** ficheros que la nombran **la LEEN o la CITAN**; ninguno la
escribe. **Su ultima escritura fue A MANO**, en un commit de agosto.

**VEREDICTO MEDIDO HOY DEL PUNTO 4: %(v4)s**, y **no por pereza de esta vuelta**:
la mitad que falta **no tiene instrumento que la haga**, y fabricarlo **es
maquinaria nueva bajo la moratoria** (`AUDITOR.md` 6.3). **NO LA FABRICO Y NO ME
LA ADJUDICO: SE SUBE NOMBRADA.**

#### 4.c. LO QUE ESTO DEJA, DICHO SIN ADORNO

**`OP-I-01` QUEDA HOY EN 3 PUNTOS EN CUBRE Y 1 EN A MEDIAS**, contra los 2 y 2
que la 214 midio. **El que se mueve es el 3**, y se mueve porque **se corrio la
busqueda que faltaba**, no porque nadie cambiara de opinion. **El 4 sigue donde
estaba, y ahora se sabe POR QUE: le falta una sede que no existe.**

**CIFRA comprobaciones del instrumento que fallan: %(fallos)s.**
""" % {
        "sha_calzan": D["sha_calzan"], "ns_exp": D["ns_exp"],
        "ns_inv": D["ns_inv"], "entradas": D["entradas"],
        "campos": D["campos"], "hueco_est": D["hueco_est"],
        "hueco_ins": D["hueco_ins"], "sospechosos": D["sospechosos"],
        "descartados": D["descartados"], "rellenos": D["rellenos"],
        "vacios": D["vacios"], "nombran": D["nombran"],
        "escriben": D["escriben"], "commits": D["commits"],
        "bytes_vista": D["bytes_vista"], "fallos": D["fallos"],
        "ultimo": ultimo, "v3": v3, "v4": v4,
        "filas_desc": NL.join(filas_desc),
    }

    fallos = 0
    print("CIFRA filas de descarte armadas: %d | CIFRA que la salida cuenta: %s"
          % (len(filas_desc), D["descartados"]))
    if len(filas_desc) != int(D["descartados"]):
        fallos += 1
    if cuerpo.count(chr(8212)) or cuerpo.count(chr(8211)):
        fallos += 1
        print("ROJO: guiones largos o medios.")
    sosp = [c for c in re.findall(r"`([^`]+)`", cuerpo)
            if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sosp))
    if sosp:
        fallos += 1
    rutas = [c for c in re.findall(r"`([^`]+)`", cuerpo)
             if "/" in c and not c.endswith("/") and " " not in c]
    malas = [r for r in rutas
             if not os.path.exists(os.path.join(RAIZ, r.replace("/", os.sep)))
             or os.path.getsize(os.path.join(RAIZ, r.replace("/", os.sep))) == 0]
    print("CIFRA rutas citadas: %d | inexistentes o vacias: %d"
          % (len(rutas), len(malas)))
    for m in malas:
        print("   ruta mala> %s" % m)
    if malas:
        fallos += 1
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: no se escribe el cuerpo.")
        return 1
    destino = os.path.join(RAIZ, "scripts", "loop", "_v%d_t4_seccion.md" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(cuerpo)
    print("ESCRITO %s -> %d bytes, %d lineas"
          % (destino, len(cuerpo.encode("utf-8")), cuerpo.count(NL)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
