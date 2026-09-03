# -*- coding: utf-8 -*-
"""vuelta161_tarea2_cierre_p52.py . CIERRE DE LA TAREA 2 SOBRE `P.5.2`.

POR QUE EXISTE, Y ES UNA REGLA Y NO UN CAPRICHO. `EJECUTOR.md` 1: **EL ESTADO AL
CIERRE SE MIDE AL CIERRE**, y toda cifra que la propia vuelta pudo mover se
RECOMPUTA al cierre. La TAREA 1.c de esta vuelta publico en `P.5.2` la cifra de
segundas lecturas independientes medida ANTES de la TAREA 2; la TAREA 2 escribio
CATORCE marcas nuevas de relectura, o sea que movio esa misma cifra. Dejar la
cifra de la apertura publicada en el banco seria exactamente la caida de la
vuelta 28 (medir temprano y publicar tarde sin remedir).

SE ANADE, NO SE SUSTITUYE: la cifra de apertura se queda entera con su corte y
su bloque, y debajo va la del cierre con el suyo. Una correccion que tapa lo que
corrige no se puede auditar (`EJECUTOR.md` 8).

NINGUNA CELDA SE TECLEA: se extraen de
`docs/loop/SALIDA_V161_T2_SEGUNDA_LECTURA_CIERRE.txt`.

USO:  python scripts/loop/vuelta161_tarea2_cierre_p52.py
"""
import io
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BANCO = os.path.join(RAIZ, "docs", "plan", "BANCO_DEL_PLAN.md")
SALIDA = os.path.join(RAIZ, "docs", "loop",
                      "SALIDA_V161_T2_SEGUNDA_LECTURA_CIERRE.txt")
ANCLA = "### LAS DOS CIFRAS VIEJAS, TACHADAS AL LADO Y NO BORRADAS"
MARCA = "### LA MISMA CIFRA, RECOMPUTADA AL CIERRE DE LA VUELTA 161"


def busca(texto, patron, etiqueta, fallos):
    m = re.search(patron, texto)
    if not m:
        fallos.append(etiqueta)
        return None
    return m.group(1)


def main():
    banco = io.open(BANCO, encoding="utf-8").read()
    if MARCA in banco:
        print("YA ESTABA: la medicion de cierre vive en P.5.2. No se toca.")
        print("CIFRA bloques escritos: 0")
        return 0
    if not os.path.exists(SALIDA):
        print("PARADA: no existe %s." % SALIDA)
        return 1
    s = io.open(SALIDA, encoding="utf-8").read()
    fallos = []
    una = busca(s, r"CIFRA con AL MENOS UNA segunda lectura independiente: (\d+)",
                "al menos una", fallos)
    dos = busca(s, r"CIFRA con DOS O MAS: (\d+)", "dos o mas", fallos)
    cero = busca(s, r"CIFRA con NINGUNA: (\d+)", "ninguna", fallos)
    actos = busca(s, r"CIFRA total de actos sobre filas: (\d+)", "actos", fallos)
    tipos = busca(s, r"CIFRA actos distintos \(tipo, vuelta\): (\d+)", "tipos", fallos)
    if fallos:
        print("PARADA: celdas no leidas: %s. No se escribe nada." % ", ".join(fallos))
        return 1
    nuevos = []
    for linea in s.split("\n"):
        if re.match(r"^\s{3}(TRAMO_DE_LAS_C|TRAMO_AL_DOBLE|SEGUNDA_PASADA|"
                    r"RELECTURA_CONJUNTA|RELECTURA)\s", linea):
            nuevos.append(linea.strip())
    if not nuevos:
        print("PARADA: la tabla de actos no se pudo leer del fichero.")
        return 1

    texto = u"""### LA MISMA CIFRA, RECOMPUTADA AL CIERRE DE LA VUELTA 161

**`EJECUTOR.md` 1: el estado al cierre se mide al cierre.** La cifra de arriba se
midio ANTES de la TAREA 2 de esta misma vuelta, y la TAREA 2 escribio **CATORCE
marcas nuevas** de relectura sobre las catorce que estaban en `C`. **La cifra de
apertura NO se borra ni se sustituye**: se queda entera con su corte y esta se
anade debajo con el suyo.

**Corte: 3 sep 2026, AL CIERRE de la vuelta 161. Autor: ejecutor de la vuelta
161. Fichero de salida: `docs/loop/SALIDA_V161_T2_SEGUNDA_LECTURA_CIERRE.txt`.**

| | apertura de la vuelta 161 | **cierre de la vuelta 161** |
|---|---:|---:|
| con AL MENOS UNA segunda lectura independiente | 85 | **__UNA__** |
| con DOS O MAS | 0 | **__DOS__** |
| con NINGUNA | 37 | **__CERO__** |
| actos de relectura contados sobre filas | 85 | **__ACTOS__** |
| actos distintos `(tipo, vuelta)` | 6 | **__TIPOS__** |

**Los actos al cierre, pegados enteros de su fichero:**

```
__NUEVOS__
```

**Y LA FORMA NUEVA SE DECLARA:** la marca que la TAREA 2 escribe,
`RELECTURA DEL TRAMO DE LAS CATORCE EN C, VUELTA 161`, cumple las dos condiciones
de esta regla (dice que es una relectura y dice en que vuelta) y se anadio a
`FORMAS_QUE_CUENTAN` del contador **en la misma vuelta que la escribio**. Una
definicion que no contara la lectura del dia en que nace naceria desfasada.

"""
    texto = (texto.replace("__UNA__", una).replace("__DOS__", dos)
             .replace("__CERO__", cero).replace("__ACTOS__", actos)
             .replace("__TIPOS__", tipos)
             .replace("__NUEVOS__", "\n".join(nuevos)))

    if ANCLA not in banco:
        print("PARADA: no se encuentra el ancla en el banco.")
        return 1
    with io.open(BANCO, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(banco.replace(ANCLA, texto + ANCLA, 1))

    print("MEDICION DE CIERRE ANADIDA A P.5.2, por adicion")
    print("   con AL MENOS UNA : 85 (apertura) -> %s (cierre)" % una)
    print("   con DOS O MAS    : 0 (apertura) -> %s (cierre)" % dos)
    print("   con NINGUNA      : 37 (apertura) -> %s (cierre)" % cero)
    print("   actos sobre filas: 85 (apertura) -> %s (cierre)" % actos)
    print("   actos distintos  : 6 (apertura) -> %s (cierre)" % tipos)
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
        print("   ROJO: tenia que ser adicion pura.")
        return 1
    print("   VERDE: adicion pura, cero borrados.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
