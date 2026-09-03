# -*- coding: utf-8 -*-
"""vuelta161_tarea1c_escribir_p52.py . TAREA 1.c DE LA VUELTA 161, LA ESCRITURA.

ESCRIBE `P.5.2 LA SEGUNDA LECTURA INDEPENDIENTE` EN `docs/plan/BANCO_DEL_PLAN.md`,
JUNTO A `P.5` Y A `P.5.1`, POR ADICION PURA: se inserta ANTES de la cabecera de
`P.6` y no se borra ni una linea de nada.

NINGUNA CIFRA SE TECLEA (EJECUTOR.md 1, "LA TABLA SE IMPRIME, NO SE TECLEA" y
"LA TABLA SE CUENTA DE SU FICHERO"): las cifras se EXTRAEN por expresion regular
de `docs/loop/SALIDA_V161_T1C_SEGUNDA_LECTURA.txt`, que es la salida del
instrumento que las midio, y si alguna no se puede leer este script PARA sin
escribir nada.

ES IDEMPOTENTE: si `P.5.2` ya esta, no lo duplica.

USO:  python scripts/loop/vuelta161_tarea1c_escribir_p52.py
"""
import io
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BANCO = os.path.join(RAIZ, "docs", "plan", "BANCO_DEL_PLAN.md")
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V161_T1C_SEGUNDA_LECTURA.txt")
ANCLA = "## P.6 EL TEMA SE LEE, EL ACTO SE COMPUTA"
MARCA = "## P.5.2 LA SEGUNDA LECTURA INDEPENDIENTE"


def busca(texto, patron, etiqueta, fallos):
    m = re.search(patron, texto)
    if not m:
        fallos.append(etiqueta)
        return None
    return m.group(1)


def main():
    fallos = []
    banco = io.open(BANCO, encoding="utf-8").read()
    if MARCA in banco:
        print("YA ESTABA: P.5.2 vive en el banco. No se toca.")
        print("CIFRA secciones escritas: 0")
        return 0
    if not os.path.exists(SALIDA):
        print("PARADA: no existe %s. Sin fichero que contar no se publica tabla."
              % SALIDA)
        return 1
    s = io.open(SALIDA, encoding="utf-8").read()

    ld = busca(s, r"CIFRA filas de LECTURA_DIRIGIDA: (\d+)", "ld", fallos)
    una = busca(s, r"CIFRA con AL MENOS UNA segunda lectura independiente: (\d+)",
                "al menos una", fallos)
    dos = busca(s, r"CIFRA con DOS O MAS: (\d+)", "dos o mas", fallos)
    cero = busca(s, r"CIFRA con NINGUNA: (\d+)", "ninguna", fallos)
    actos = busca(s, r"CIFRA total de actos sobre filas: (\d+)", "actos", fallos)
    tipos = busca(s, r"CIFRA actos distintos \(tipo, vuelta\): (\d+)", "tipos", fallos)
    nombran = busca(s, r"CIFRA razones que NOMBRAN al auditor en prosa: (\d+)",
                    "nombran", fallos)
    if fallos:
        print("PARADA: no se pudieron leer estas celdas de la salida: %s"
              % ", ".join(fallos))
        print("No se escribe nada.")
        return 1

    # La tabla de actos se pega ENTERA de su fichero, no se reescribe.
    bloque_actos = []
    for linea in s.split("\n"):
        if re.match(r"^\s{3}(TRAMO_AL_DOBLE|SEGUNDA_PASADA|RELECTURA_CONJUNTA|RELECTURA)\s",
                    linea):
            bloque_actos.append(linea.strip())
    if not bloque_actos:
        print("PARADA: la tabla de actos no se pudo leer del fichero.")
        return 1

    texto = u"""## P.5.2 LA SEGUNDA LECTURA INDEPENDIENTE: **LA QUE DEJA MARCA CONTABLE**

**Escrita el 3 sep 2026, en la vuelta 161, por encargo expreso del fundador
(TAREA 1.c) y sobre la tercera deuda que el auditor midio en la parada de la
vuelta 160** (`docs/loop/paradas/2026-09-03-credito-vara-movil.md`). Va **junto a
`P.5` y a `P.5.1`** y lleva su numero para no renumerar nada.

**POR QUE NACE, Y NO ES POR EL NUMERO.** El acta 158 publico **84**, el acta 160
midio **82**, y las dos son honestas: **no median lo mismo, porque la definicion
nunca se escribio.** El propio auditor lo dejo dicho: *"No copio esa cifra ni la
mia encima de la suya: lo que falta es la definicion, no el numero."*

### LAS TRES COSAS QUE ESTA REGLA DICE

> **(1) QUE MARCA CUENTA.** Cuenta la marca escrita **en el campo `razon` de la
> fila del registro** (`docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl`), anadida por
> adicion, que dice **DOS cosas**: que es una **RELECTURA** (no la lectura que
> abrio la fila) y **EN QUE VUELTA** se hizo.
>
> **NO cuentan**, y se dice por que: la marca de la lectura que **ABRE** la fila
> (`LOTE 1 DE LA VUELTA 157`, `LOTE 2 DE LA VUELTA 159`), porque una primera
> lectura no es una segunda; ni las ediciones de **mantenimiento**
> (`UNIFICACION DEL CAMPO cita`, `ADJUDICACION 6.x DEL ACTA N`), porque **no
> vuelven a los nodos**.
>
> **(2) QUIEN PUEDE FIRMARLA.** **La firma la da LA VUELTA, no la persona.**
> Cuenta la relectura hecha en una **vuelta posterior** a la que publico la
> clase, y **pueden firmarla las dos plumas**: el ejecutor (segunda pasada, tramo
> al doble, relectura conjunta) y el auditor (ciega). **Pero solo cuenta la que
> deja su marca en el registro.** Una lectura que no deja marca **no es
> contable**: no porque no haya ocurrido, sino porque **una cifra que no se puede
> recomputar de un fichero no es una cifra** (`EJECUTOR.md` 2).
>
> **(3) UNA RELECTURA CONJUNTA CUENTA UNA SOLA VEZ.** Aunque la pidan dos plumas
> y aunque deje dos marcas, es **UN acto de lectura sobre UN par**. Se computa
> metiendo los actos en un **conjunto** de pares `(tipo, vuelta)`, asi que dos
> marcas del mismo acto sobre la misma fila **colapsan solas**.

### LA CONSECUENCIA QUE ESTA REGLA IMPONE, Y ES LA QUE ARREGLA EL BAILE

**QUIEN RELEE, ESCRIBE SU MARCA EN EL REGISTRO.** Medido hoy: **__NOMBRAN__**
razones nombran al auditor en prosa, y su relectura **ciega** vive en su acta y
en `docs/loop/_auditor_v*_ciega*`, **no aqui**. Por eso una cifra contada del
registro la pierde y por eso las dos cifras viejas no cuadraban. **La regla no
cambia lo que se lee: cambia donde queda escrito.**

### LA CIFRA, RECOMPUTADA POR ESTA DEFINICION

**Corte: 3 sep 2026. Autor: ejecutor de la vuelta 161. Instrumento:
`scripts/loop/vuelta161_tarea1c_segunda_lectura.py`. Fichero de salida:
`docs/loop/SALIDA_V161_T1C_SEGUNDA_LECTURA.txt`.** Ninguna celda esta tecleada:
todas se extraen de ese fichero.

| | cifra |
|---|---:|
| pares de `LECTURA_DIRIGIDA` en el registro | __LD__ |
| **con AL MENOS UNA segunda lectura independiente** | **__UNA__** |
| con DOS O MAS | __DOS__ |
| con NINGUNA | __CERO__ |
| actos de relectura contados sobre filas | __ACTOS__ |
| actos distintos `(tipo, vuelta)` | __TIPOS__ |

**Los actos, pegados enteros de su fichero:**

```
__BLOQUE__
```

### LAS DOS CIFRAS VIEJAS, TACHADAS AL LADO Y NO BORRADAS

**`EJECUTOR.md` 8: una correccion que tapa lo que corrige no se puede auditar.**
Ninguna de las dos se borra y **ninguna se escribe encima de la otra**:

| cifra | autor | corte | cita | que media |
|---:|---|---|---|---|
| ~~**84**~~ | auditor, acta 158 | 3 sep 2026 | `docs/loop/ACTA_AUDITOR.md:52411` | acumulado que **sumaba dos libros**: 65 heredadas de las actas mas las 19 ciegas del propio auditor |
| ~~**82**~~ | auditor, acta 160 | 3 sep 2026 | `docs/loop/ACTA_AUDITOR.md:53172` | pares cuya razon lleva **dos bloques anadidos**, incluidos los de mantenimiento |

**Las dos eran fieles a lo que cada una media. Lo que faltaba era decir que se
mide.**

---

"""
    texto = (texto.replace("__LD__", ld).replace("__UNA__", una)
             .replace("__DOS__", dos).replace("__CERO__", cero)
             .replace("__ACTOS__", actos).replace("__TIPOS__", tipos)
             .replace("__NOMBRAN__", nombran)
             .replace("__BLOQUE__", "\n".join(bloque_actos)))

    if ANCLA not in banco:
        print("PARADA: no se encuentra el ancla %r en el banco." % ANCLA)
        return 1
    nuevo = banco.replace(ANCLA, texto + ANCLA, 1)
    with io.open(BANCO, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(nuevo)

    print("P.5.2 ESCRITA EN docs/plan/BANCO_DEL_PLAN.md, por adicion, antes de P.6")
    print("CIFRA secciones escritas: 1")
    print("")
    print("LAS CELDAS, LEIDAS DE %s:" % os.path.relpath(SALIDA, RAIZ).replace("\\", "/"))
    for etiqueta, valor in (("pares de LECTURA_DIRIGIDA", ld),
                            ("con AL MENOS UNA", una),
                            ("con DOS O MAS", dos),
                            ("con NINGUNA", cero),
                            ("actos sobre filas", actos),
                            ("actos distintos", tipos),
                            ("razones que nombran al auditor", nombran)):
        print("   %-34s %s" % (etiqueta, valor))
    print("")
    print("LA ADITIVIDAD SE MIDE, NO SE PROMETE:")
    r = subprocess.run(["git", "diff", "--numstat", "--",
                        "docs/plan/BANCO_DEL_PLAN.md"],
                       cwd=RAIZ, capture_output=True, text=True)
    print("   git diff --numstat: %s" % r.stdout.strip())
    borrados = None
    for linea in r.stdout.strip().split("\n"):
        partes = linea.split("\t")
        if len(partes) >= 2 and partes[1].isdigit():
            borrados = int(partes[1])
    print("   CIFRA borrados en el banco: %s" % borrados)
    if borrados != 0:
        print("   ROJO: la escritura tenia que ser ADICION PURA y hay borrados.")
        return 1
    print("   VERDE: adicion pura, cero borrados.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
