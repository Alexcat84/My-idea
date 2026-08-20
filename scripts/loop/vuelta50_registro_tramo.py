# -*- coding: utf-8 -*-
"""vuelta50_registro_tramo.py . ESCRIBE EL REGISTRO DEL TRAMO DE LA VUELTA 50 AL
FINAL DE docs/plan/03_FUSIONES.md.

SUCESOR DECLARADO de scripts/loop/vuelta49_registro_tramo.py, del que hereda el
contrato entero: el veredicto de CADA lectura `P.12` se registra en el REGISTRO
DEL TRAMO de esta pagina, en tabla propia, y los `CONTINUA` declaran AHI su
arista a la fase 04, con id RESUELTO (`P.9`) y SIN ejecutarla. Es el carril
adjudicado por el auditor (acta de la vuelta 48, seccion 6, punto 2).

LO QUE CAMBIA: el registro se escribe POR BLOQUES y no de una sola vez, porque
esta vuelta tiene un encargo largo y la regla 6 del EJECUTOR.md manda commitear
por tramo para que nada dependa de que la sesion aguante. Cada bloque trae su
propia ANCLA y su propia GUARDA DE IDEMPOTENCIA.

GUARDA DE ANCLA: el texto se pega DETRAS de la ultima linea que se le indique,
comprobada literal. Si esa linea no esta o no es la ultima del fichero, aborta.
GUARDA DE IDEMPOTENCIA: si la cabecera del bloque ya esta dentro, no escribe.

Uso: python scripts/loop/vuelta50_registro_tramo.py --bloque apertura [--ejecutar]
"""
import argparse
import io
import sys

DESTINO = "docs/plan/03_FUSIONES.md"

BLOQUES = {}

# ---------------------------------------------------------------------------
BLOQUES["apertura"] = {
    "ancla": "| duplicadas tras resolver **NUEVAS** / auto-aristas **NUEVAS** | | **CERO** / **CERO** |",
    "cabecera": "## `OP-U-01`, TRAMO 1, LA VUELTA 50:",
    "texto": """
---

## `OP-U-01`, TRAMO 1, LA VUELTA 50: **EL BARRIDO QUE LA VUELTA 49 NO CORRIO AL CERRAR, Y UN ALIAS QUE NO SE IZO** (19 ago 2026, vuelta 50)

### LO PRIMERO DE LA VUELTA, PORQUE ES UNA CAIDA DE CIFRA PUBLICADA Y NO UN TRAMITE

**La vuelta 49 movio el marcador y el retrato DESPUES de correr su barrido `9.10`** (el volteo
del puesto **305** por `P.16` y las tres fusiones de su TAREA 2) **y no volvio a barrer al
cerrar.** El acta de la vuelta 49, seccion 3, lo nombra como caida de cifra publicada del
ejecutor, FUERA de sus discutibles marcados. **Las cinco celdas quedan corregidas hoy con
tachado, fecha y motivo**, y las cifras salen de dos instrumentos corridos EN ESTA VUELTA y de
ningun acta:

| la celda | decia | **hoy, medido en esta vuelta** | el instrumento |
|---|---:|---:|---|
| [`../INTRA_DOMINIO_INFORME.md`](../INTRA_DOMINIO_INFORME.md) apendice **100.1**, fila `A` | 574 | **573** | `scripts/recomputar_marcador.py 3388` |
| el mismo apendice, fila `D` | 2.729 | **2.730** | el mismo |
| [`RECOMPUTO_3388.md`](RECOMPUTO_3388.md) fila **246**, `A` crudas | 574 | **573** | `scripts/plan/recomputo_3388.py` |
| la fila **247**, colapsos a auto-arista | 41 | **48** | el mismo |
| la fila **248**, pares distintos del retrato | 533 | **525** | el mismo |
| la fila **1079**, total de `A` de la tabla por dominio | 574 | **573** | `recomputar_marcador.py` |
| el checkpoint **ii** de la fila **528** | 533 igual a 533 | **525 igual a 525, sigue OK** | `recomputo_3388.py`, seccion final |

**Y LA CIFRA 41 NO ERA UN ERROR DE LECTURA, QUE ES LO QUE LA HACE INTERESANTE:** era el corte de
la TAREA 1.3 de la vuelta 49, tomado ANTES de las tres fusiones de su propia TAREA 2. **Los
siete que faltaban son la huella de esas tres fusiones**, que es exactamente lo que la propia
fila ya explicaba de las 41. Una fila puede explicar bien su cifra y traer la cifra vieja.

> **LA REGLA QUE ESTO DEJA, y ya esta adjudicada** (acta de la vuelta 49, seccion 5, pregunta 5,
> por extension del banco `9.10`): **quien mueve una clase o funde un acto corre el barrido ANTES
> DE CERRAR LA VUELTA**, sobre toda tabla vigente que cite la clase, el marcador o el retrato.
> Barrer al destapar y barrer al mover son la misma regla vista de los dos lados.

### EL INSTRUMENTO DEL BARRIDO TENIA LA MISMA AVERIA QUE PERSEGUIA, Y SE DICE

**Medido antes de escribir una linea del sucesor:** `scripts/loop/vuelta49_barrido_910.py` acepta
`--viejo` **pero no lo usa para buscar**. Sus dos expresiones regulares estan clavadas a `583` y
`2709`, las cifras del marcador de la vuelta 14, y `--viejo` solo cambia la cabecera que imprime.
Corrido hoy con `--viejo 574,77,8,2729` devuelve 22 candidatos, **y los devuelve porque esas
celdas arrastran el 583 en su cadena de tachados, no porque sepa buscar el 574**
([`../loop/SALIDA_V50_BARRIDO_910_INSTRUMENTO_VIEJO.txt`](../loop/SALIDA_V50_BARRIDO_910_INSTRUMENTO_VIEJO.txt)).
**Una celda nueva escrita hoy con la cifra vigente y sin cadena de tachados le seria invisible.**
El sucesor `scripts/loop/vuelta50_barrido_910.py` busca de verdad lo que se le pide, conserva la
familia legado del 583 y anade la familia del RETRATO, que ningun barrido anterior miraba: **con
el, las siete celdas de arriba salen solas**
([`../loop/SALIDA_V50_BARRIDO_910_A.txt`](../loop/SALIDA_V50_BARRIDO_910_A.txt)).

### EL ALIAS QUE NO SE IZO AL SUPERVIVIENTE (`modelo_spin_2`)

**Una linea de registro y ningun dato tocado**, que es lo que el encargo manda. Al fundir la
parte A del acto 1 en la vuelta 49, el absorbido `modelo_spin` cargaba a su vez el alias
`modelo_spin_2` y **ese alias NO se izo a `modelo_spin_preguntas`**. Medido hoy con
`scripts/loop/vuelta50_alias_durmiente.py`
([`../loop/SALIDA_V50_ALIAS_DURMIENTE.txt`](../loop/SALIDA_V50_ALIAS_DURMIENTE.txt)), y con un
filo mas que la observacion del acta: **por el resolutor de la casa (`P.1`, que construye el mapa
de alias SOLO con nodos vivos) `modelo_spin_2` NO RESUELVE EN ABSOLUTO**; solo llega por la
cadena ancha `modelo_spin_2` a `modelo_spin` **[DEPRECADO]** a `modelo_spin_preguntas`. **CERO
referencias en aristas y CERO en veredictos**: nadie lo pisa hoy. **Es pasivo de la especie
`OP-S-12` y queda nombrado para esa operacion**, no se repara aqui.
""",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bloque", required=True, choices=sorted(BLOQUES))
    ap.add_argument("--ejecutar", action="store_true")
    args = ap.parse_args()
    b = BLOQUES[args.bloque]

    texto = io.open(DESTINO, encoding="utf-8").read()

    print("=" * 78)
    print("REGISTRO DEL TRAMO, vuelta 50, bloque: %s" % args.bloque)
    print("destino: %s" % DESTINO)
    print("=" * 78)

    if b["cabecera"] in texto:
        print("YA ESCRITO (idempotencia): la cabecera del bloque ya esta dentro.")
        return 0

    ancla = b["ancla"]
    if texto.count(ancla) != 1:
        print("ROJO: el ancla aparece %d veces, tiene que aparecer UNA." % texto.count(ancla))
        return 1
    if not texto.rstrip("\n").endswith(ancla):
        print("ROJO: el ancla no es la ULTIMA linea del fichero. No se escribe nada.")
        print("      ultima linea: %r" % texto.rstrip("\n").splitlines()[-1][:120])
        return 1

    nuevo = texto.rstrip("\n") + "\n" + b["texto"]
    print("ancla OK y es la ultima linea. Se anaden %d caracteres."
          % (len(nuevo) - len(texto)))
    for mal, nombre in (("—", "guion largo"), ("–", "guion medio")):
        if mal in b["texto"]:
            print("ROJO: el bloque trae un %s." % nombre)
            return 1
    print("guiones largos y medios en el bloque: CERO")

    if not args.ejecutar:
        print("SIMULACION: nada escrito.")
        return 0
    io.open(DESTINO, "w", encoding="utf-8", newline="").write(nuevo)
    print("ESCRITO.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
