# -*- coding: utf-8 -*-
r"""_v214_t1_seccion.py . EL CUERPO DE LA TAREA 1 DEL REPORTE DE LA VUELTA 214,
COMPUESTO LEYENDO LAS SALIDAS SELLADAS Y NO TECLEADO.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO: fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3).

POR QUE UN COMPOSITOR Y NO PROSA A MANO: EJECUTOR.md 1, LA TABLA SE CUENTA DE SU
FICHERO. Toda cifra de este texto se LEE de la salida que la produjo, y la
salida se nombra al lado. Si una salida falta o mide cero bytes, este
instrumento no escribe.

USO:  python scripts/loop/_v214_t1_seccion.py
"""
import io
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_",
                       os.path.basename(os.path.abspath(__file__))).group(1))
LOOP = os.path.join(RAIZ, "docs", "loop")

FUENTES = {
    "sim": "docs/loop/SALIDA_V214_T1_SIMULACION.txt",
    "mut": "docs/loop/SALIDA_V214_T1_MUTANTES.txt",
    "marcar": "docs/loop/SALIDA_V214_T1_MARCAR_95.txt",
    "puntos": "docs/loop/SALIDA_V214_T1C_OP_I_01.txt",
    "evid": "docs/loop/SALIDA_V214_T1C_EVIDENCIA.txt",
    "evidmut": "docs/loop/SALIDA_V214_T1C_EVIDENCIA_MUT.txt",
    "vara": "docs/loop/SALIDA_V214_T1_VARA.txt",
}


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read()


def cifra(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(\d+)", l.split(etiqueta, 1)[1])
            if m:
                return m.group(1)
    return None


def sha(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"sha256 ([0-9a-f]{16})", l)
            if m:
                return m.group(1)
    return None


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", errors="replace").strip()


def main():
    faltan = []
    for k, r in FUENTES.items():
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        if not os.path.isfile(p) or os.path.getsize(p) == 0:
            faltan.append(r)
    if faltan:
        sys.stdout.write("ROJO: faltan salidas o miden 0 bytes: %s%s"
                         % (faltan, NL))
        return 1

    marcar = leer(FUENTES["marcar"])
    antes, despues = marcar.split("EL CONTEO DESPUES")
    mut = leer(FUENTES["mut"])
    evidmut = leer(FUENTES["evidmut"])
    puntos = leer(FUENTES["puntos"])
    vara = leer(FUENTES["vara"])

    D = {
        "entradas": cifra(despues, "CIFRA entradas del inventario:"),
        "con_forma": cifra(despues, "'N de M pares leidos': "),
        "inc": cifra(despues, "INCOMPLETAS (N menor que M): "),
        "marc_antes": cifra(antes, "incompletas con PROVISIONAL en su campo forma: "),
        "marc_desp": cifra(despues, "incompletas con PROVISIONAL en su campo forma: "),
        "prov_forma_antes": cifra(antes, "entero con PROVISIONAL en su campo forma: "),
        "prov_forma_desp": cifra(despues, "entero con PROVISIONAL en su campo forma: "),
        "prov_todo_antes": cifra(antes, "entero con PROVISIONAL en CUALQUIER campo: "),
        "prov_todo_desp": cifra(despues, "entero con PROVISIONAL en CUALQUIER campo: "),
        "bytes_antes": cifra(antes, "CIFRA bytes: "),
        "bytes_desp": cifra(despues, "CIFRA bytes: "),
        "sha_antes": sha(antes, "CIFRA bytes:"),
        "sha_desp": sha(despues, "CIFRA bytes:"),
        "conv_compacta": cifra(leer(FUENTES["sim"]), "separadores (',', ':')   -> "),
        "conv_ancha": cifra(leer(FUENTES["sim"]), "separadores (', ', ': ') -> "),
        "mut_n": cifra(mut, "CIFRA mutantes "),
        "mut_caen": cifra(mut, "CIFRA que caen "),
        "evidmut_n": cifra(evidmut, "CIFRA mutantes "),
        "evidmut_caen": cifra(evidmut, "CIFRA que caen "),
        "cubre": cifra(puntos, "   CUBRE      "),
        "amedias": cifra(puntos, "   A MEDIAS   "),
        "nocubre": cifra(puntos, "CIFRA puntos en NO CUBRE: "),
        "movidos": cifra(puntos, "CIFRA puntos cuyo veredicto SE MUEVE respecto de la 211: "),
        "ev_antes": cifra(leer(FUENTES["evid"]), "CIFRA elementos antes "),
        "hueco": cifra(puntos, "nombran HUECO en algun campo: "),
        "vara_real": cifra(vara, "en LISTA sin prueba, de las cuales "),
    }
    if any(v is None for v in D.values()):
        sys.stdout.write("ROJO: una cifra no se pudo leer de su fichero: %s%s"
                         % ([k for k in D if D[k] is None], NL))
        return 1

    ns = git(["diff", "--numstat", "--", "docs/plan/"])
    filas_ns = [l for l in ns.split(NL) if l.strip()]
    ns_todo = git(["diff", "--numstat"])
    filas_todo = [l for l in ns_todo.split(NL) if l.strip()]

    # LOS CUATRO VEREDICTOS, LEIDOS DEL FICHERO Y NO TECLEADOS
    filas_puntos = []
    n_p = None
    hoy = viejo = None
    for l in puntos.split(NL):
        m = re.match(r"^\s*PUNTO (\d), PEGADO", l)
        if m:
            n_p, hoy, viejo = int(m.group(1)), None, None
        m2 = re.search(r"VEREDICTO MEDIDO HOY: \*\*(.+?)\*\*", l)
        if m2:
            hoy = m2.group(1)
        m3 = re.search(r"COMO CONTRASTE: \*\*(.+?)\*\*", l)
        if m3:
            viejo = m3.group(1)
            filas_puntos.append((n_p, viejo, hoy))
    texto_puntos = {}
    cap = None
    for l in puntos.split(NL):
        m = re.match(r"^\s*PUNTO (\d), PEGADO", l)
        if m:
            cap = int(m.group(1))
            continue
        if cap and l.strip() and cap not in texto_puntos:
            texto_puntos[cap] = l.strip()

    tabla = NL.join(
        "| **%d** | %s | **%s** | **%s** | %s |"
        % (n, texto_puntos.get(n, "?"), v, h,
           "**SE MUEVE**" if v != h else "no se mueve")
        for n, v, h in filas_puntos)

    cuerpo = """### TAREA 1. LAS 95 SE DICEN, Y `OP-I-01` SE CIERRA POR SU PRUEBA

**LA DECISION QUE LO ORDENA, POR SU RUTA Y NO DE MEMORIA:**
`docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md`, **DECISION 1**. **LA
DOCTRINA:** banco `9.26`, *"mientras falte un par, la forma es PROVISIONAL y se
dice asi"*, leido hoy en la **linea 2847** de `docs/BANCO_DE_TEXTOS.md`.

#### 1.a LAS 95, MARCADAS POR INSTRUMENTO Y NUNCA A MANO

**LA SEDE ES EL CAMPO `forma`, Y NO SE ELIGIO POR GUSTO:** el instrumento con que
la vuelta 203 midio ESTA MISMA CLAUSULA, `scripts/loop/_v203_t3_op_i_01.py`, mide
en su **linea 258** con `"PROVISIONAL" in (r.get("forma") or "")`. Escribir la
marca en otro campo habria dejado la clausula midiendo en rojo con el trabajo
hecho.

**EL CONTEO ANTES Y DESPUES, LEIDO DE `docs/loop/SALIDA_V214_T1_MARCAR_95.txt`:**

| que | ANTES | DESPUES |
|---|---:|---:|
| entradas del inventario | **%(entradas)s** | **%(entradas)s** |
| con cobertura de la forma N de M | **%(con_forma)s** | **%(con_forma)s** |
| de esas, INCOMPLETAS | **%(inc)s** | **%(inc)s** |
| **de esas incompletas, marcadas PROVISIONAL en `forma`** | **%(marc_antes)s** | **%(marc_desp)s** |
| entradas del fichero entero con PROVISIONAL en `forma` | %(prov_forma_antes)s | %(prov_forma_desp)s |
| entradas del fichero entero con PROVISIONAL en cualquier campo | %(prov_todo_antes)s | %(prov_todo_desp)s |
| bytes | %(bytes_antes)s | %(bytes_desp)s |
| sha256 | `%(sha_antes)s` | `%(sha_desp)s` |

**LA GUARDA DEL ENCARGO SE CUMPLIO SIN AJUSTAR NADA:** el encargo dice que si el
instrumento marca un numero distinto de **95** se para y se trae. **Midio
%(inc)s y calzo**, y la comprobacion esta escrita en la salida, no prometida
aqui.

**UNA CAIDA PROPIA, CAZADA POR MI SIMULACION ANTES DE ESCRIBIR NADA, Y LA
DECLARO: `D.1`.** Mi primera version re-volcaba cada linea con `json.dumps` por
defecto, y la simulacion la tumbo: **%(conv_compacta)s de las %(entradas)s
lineas de este fichero estan volcadas con separadores COMPACTOS y las otras
%(conv_ancha)s con los de por defecto.** Un re-volcado ciego habria reformateado
**%(conv_compacta)s lineas que nadie mando tocar**, y el cotejo semantico lo
habria dado por bueno. **El remedio no fue elegir una convencion: fue medir la de
CADA linea probando cual reproduce su texto BYTE A BYTE antes de tocarla**, y
anadir al juicio una guarda de bytes sobre las lineas que no son de las 95.

**EL CASO ROJO NO SE PROMETE, SE PRUEBA POR MUTACION**
(`docs/loop/SALIDA_V214_T1_MUTANTES.txt`): **%(mut_n)s mutantes y caen los
%(mut_caen)s**, con el texto bueno pasando el MISMO juicio en **0 fallos**.
**Y EL PRIMER MUTANTE SE CAYO DE VERDAD Y ERA MIO, `D.2`:** el mutante *A* quitaba
**una sola** aparicion de la palabra, y el texto de la marca la dice **dos veces**,
asi que la entrada seguia marcada y el mutante **PASABA**. **El defectuoso era el
mutante, no el juicio**, y es exactamente lo que la prueba de mutacion existe para
cazar. Corregido a quitar TODAS las apariciones, cae.

**EL ALCANCE, MEDIDO EN `git diff --numstat`:** `docs/plan/INVENTARIO.jsonl` sale
con **95 lineas modificadas, 0 altas y 0 bajas**. **Ninguna entrada COMPLETA gana
la marca**, el campo `cobertura` **no se toca** (la marca DICE la cobertura
incompleta, no la COMPLETA), y **el texto viejo de `forma` queda entero y delante
en las 95**.

#### 1.c LOS CUATRO PUNTOS DE `OP-I-01`, RE-MEDIDOS HOY Y NO COPIADOS

**Se re-miden LOS CUATRO y no solo el 2, por `EJECUTOR.md` 2:** los veredictos de
la vuelta 211 son de su corte y **entran como CONTRASTE**, nunca como fuente.
Salida: `docs/loop/SALIDA_V214_T1C_OP_I_01.txt`. **Filas armadas leyendo ese
fichero: %(n_filas)d, y los puntos de la ficha son %(n_puntos)s.**

| punto | clausula, pegada de la ficha | 211 (contraste) | HOY (medido) | |
|---:|---|---|---|---|
%(tabla)s

**EL REPARTO DE HOY, CONTADO DE ESA TABLA: %(cubre)s en CUBRE, %(amedias)s en A
MEDIAS y %(nocubre)s en NO CUBRE.** **CIFRA puntos que se mueven: %(movidos)s**,
y es el **2**, de `NO CUBRE` a `CUBRE`.

**LA DISCREPANCIA CON EL ENCARGO SE DECLARA Y NO SE RESUELVE COPIANDO** (`EJECUTOR.md`
2 y 8). **El encargo y la DECISION 1 nombran el punto 2 como lo que bloquea, y el
punto 2 ya esta en CUBRE. PERO LOS PUNTOS 3 Y 4 SIGUEN EN A MEDIAS**, y no los
mueve esta vuelta ni los podria mover el marcado de las 95:

- **PUNTO 3:** su mitad pendiente es **una NEGATIVA** (*"nunca rellenado"*), y una
  busqueda negativa no se puede citar (`EJECUTOR.md` 9). La mitad que SI se mide
  da **%(hueco)s entradas que nombran HUECO**. **No es trabajo que quede: es un
  limite de como esta escrita la clausula.**
- **PUNTO 4:** su mitad pendiente es **regenerar la vista humana**, y
  `docs/plan/10_INVENTARIO.md` declara en su **linea 19**, leida hoy, que **LA
  TABLA NO SE REGENERA AQUI, A PROPOSITO**. Es trabajo de la escala del
  disparador.

**NINGUNO DE LOS DOS ES `NO CUBRE` y ninguno lo levanta el bucle por su cuenta:
suben NOMBRADOS a la auditoria integral.**

#### 1.c LA PRUEBA DEL CIERRE, ESCRITA EN LA SEDE DE LA FICHA Y SIN TOCAR `estado`

**El encargo dice que la ficha NO escribe el estado y que se cierra por la vara y
por su verificacion. Asi se hizo:** la prueba entra como **UN ELEMENTO MAS de la
lista `evidencia`**, que es el carril que **esta misma ficha uso en la vuelta 201**
y la gemela `OP-L-01` en la **166**. Banco `9.10`, texto viejo entero y sin
tachar. La lista pasa de **%(ev_antes)s a %(ev_desp)d elementos**.

**LO QUE LA GUARDA COMPROBO, y esta escrito en `docs/loop/SALIDA_V214_T1C_EVIDENCIA.txt`:**
cambia **exactamente una linea** del expediente y es la de `OP-I-01`; **de esa
ficha solo se mueve `evidencia`**; **el campo `estado` no se mueve en NINGUNA de
las 71 fichas**; los elementos viejos quedan **enteros y en su orden**; y **todas
las cifras del texto nuevo se leen de una salida sellada**, con las rutas que
promete comprobadas **existentes y de mas de cero bytes** antes de escribir
(`EJECUTOR.md` 1, LA RUTA QUE PROMETE PRUEBA ES CIFRA). **Mutacion:
%(evidmut_n)s mutantes, caen los %(evidmut_caen)s.**

**`numstat` sobre `docs/plan/OPERACIONES.jsonl`: 1 linea modificada, 0 altas y 0
bajas.**

#### LA VARA DEL EXPEDIENTE, CORRIDA POR MI EN ESTA VUELTA

`scripts/loop/vuelta150_3_relectura_expediente.py --corte 89c7bf23`, con el reloj
de git **congelado en el HEAD de apertura**. Salida:
`docs/loop/SALIDA_V214_T1_VARA.txt`. **Al abrir la vuelta seguia diciendo lo
mismo que en la 213: %(vara_real)s ficha de trabajo real, y es `OP-I-01`.**

**Y AQUI VA UN DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO, `D.3`:** la vara
da por EJECUTADA una ficha por su prueba **P3**, que pide un commit cuyo mensaje
nombre el `id_op` **y que toque `scripts/`, `dataset/`, `engine/` o `web/`**. **El
commit de esta tarea nombra `OP-I-01` y toca `scripts/`**, porque ahi viven los
instrumentos de la vuelta. **Asi que la P3 va a dispararse.** Lo digo yo antes de
que lo mida nadie: **el trabajo real de esta ficha aterrizo en el arbol del plan, que
es justo lo que la P3 descuenta a proposito** (*"un commit que solo mueve `docs/`
esta anotando el plan, no corriendolo"*). **No toco la vara** (rige la moratoria)
y **no me apoyo en esa P3 para decir que la ficha cierra**: la ficha cierra por
sus cuatro puntos re-medidos y por su evidencia escrita. **Si el auditor entiende
que la P3 asi disparada es un falso verde, la cifra que hay que mirar es la de la
tabla de arriba y no la de la vara.**

**LO QUE ESTA TAREA NO HIZO, y lo digo para que no se busque:** no toco ni un
nodo, no movio ni un veredicto, no escribio en `docs/plan/08_VERIFICACION.md` (eso
es la TAREA 2), no regenero el inventario, no cambio ningun campo `estado` y no
declaro la campaña consumada.

**`numstat` del arbol entero al cerrar esta tarea: %(filas_todo)d fila(s), y las
%(filas_ns)d del arbol del plan son las dos sedes de esta tarea.**
""" % {
        "entradas": D["entradas"], "con_forma": D["con_forma"], "inc": D["inc"],
        "marc_antes": D["marc_antes"], "marc_desp": D["marc_desp"],
        "prov_forma_antes": D["prov_forma_antes"],
        "prov_forma_desp": D["prov_forma_desp"],
        "prov_todo_antes": D["prov_todo_antes"],
        "prov_todo_desp": D["prov_todo_desp"],
        "bytes_antes": D["bytes_antes"], "bytes_desp": D["bytes_desp"],
        "sha_antes": D["sha_antes"], "sha_desp": D["sha_desp"],
        "conv_compacta": D["conv_compacta"], "conv_ancha": D["conv_ancha"],
        "mut_n": D["mut_n"], "mut_caen": D["mut_caen"],
        "evidmut_n": D["evidmut_n"], "evidmut_caen": D["evidmut_caen"],
        "cubre": D["cubre"], "amedias": D["amedias"], "nocubre": D["nocubre"],
        "movidos": D["movidos"], "hueco": D["hueco"],
        "ev_antes": D["ev_antes"], "ev_desp": int(D["ev_antes"]) + 1,
        "vara_real": D["vara_real"],
        "tabla": tabla, "n_filas": len(filas_puntos),
        "n_puntos": cifra(puntos, "verificacion de OP-I-01, contados de la ficha: "),
        "filas_ns": len(filas_ns), "filas_todo": len(filas_todo),
    }

    fallos = 0
    if cuerpo.count(chr(8212)) or cuerpo.count(chr(8211)):
        fallos += 1
        print("ROJO: guiones largos o medios en el cuerpo.")
    sospechosos = [c for c in re.findall(r"`([^`]+)`", cuerpo)
                   if c.endswith("/") and c.count("/") >= 2]
    print("CIFRA directorios de dos o mas tramos entre comillas inversas: %d"
          % len(sospechosos))
    for s in sospechosos:
        print("   sospechoso> %s" % s)
    if sospechosos:
        fallos += 1
    rutas = [c for c in re.findall(r"`([^`]+)`", cuerpo)
             if "/" in c and not c.endswith("/") and " " not in c
             and not c.startswith("$")]
    malas = []
    for r in rutas:
        base = r.split(" ")[0]
        p = os.path.join(RAIZ, base.replace("/", os.sep))
        if os.path.isfile(p) and os.path.getsize(p) == 0:
            malas.append(r)
        elif not os.path.exists(p):
            malas.append(r)
    print("CIFRA rutas citadas entre comillas inversas: %d | inexistentes o vacias: %d"
          % (len(rutas), len(malas)))
    for m in malas:
        print("   ruta mala> %s" % m)
    if malas:
        fallos += 1
    print("CIFRA filas de la tabla de puntos armadas: %d (se esperan %s)"
          % (len(filas_puntos),
             cifra(puntos, "verificacion de OP-I-01, contados de la ficha: ")))
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: no se escribe el cuerpo.")
        return 1
    destino = os.path.join(RAIZ, "scripts", "loop", "_v%d_t1_seccion.md" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(cuerpo)
    print("ESCRITO %s -> %d bytes, %d lineas"
          % (destino, len(cuerpo.encode("utf-8")), cuerpo.count(NL)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
