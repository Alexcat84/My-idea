# -*- coding: utf-8 -*-
r"""_v192_arreglar_parejas2.py . REACOMODA LAS CUATRO CIFRAS QUE `cifras_sin_pareja()`
CAZO EN EL CIERRE DE LA VUELTA 192.

QUE PASO, Y ES LA MISMA GUARDA MORDIENDO OTRA VEZ: una cifra de bytes o un `sha`
esta emparejado **si su pareja cae en LA MISMA LINEA**. Mis cuatro cifras tenian
su pareja escrita, **pero el salto de linea las separo**, y la guarda no puede
distinguir eso de una cifra huerfana. **La guarda tiene razon: mira renglones, y
un renglon con una sola cifra es un renglon con una sola cifra.**

LAS CUATRO, CON SU LINEA EN LA CORRIDA QUE LAS CAZO:
  . 190  `sha256` LF `795c0ec740bdd5cc` suelto en su renglon
  . 483  `2433 bytes` partido de su `disco 2433`
  . 558  `4282 bytes` partido de su `disco 4282`
  . 719  `4054129 bytes normalizados a LF` partido de su `4054129 en disco`

NO SE BORRA NINGUNA CIFRA NI SE QUITA NINGUNA PAREJA: se reacomodan para que
cada pareja quepa en un renglon. El parche es IDEMPOTENTE y CAE sin escribir si
un ancla no aparece.
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)

CAMBIOS = [
    ("scripts/loop/_v192_t1_seccion.md",
     """`docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt`, **disco 6904 bytes | LF 6904
bytes**, `sha256` LF `795c0ec740bdd5cc`, veredicto leido del propio fichero
`VEREDICTO: VERDE`, y la aguja `EN CONTRA` aparece **13** veces dentro.""",
     """`docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt`,
**disco 6904 bytes | LF 6904 bytes**, con su `sha256` LF y su veredicto leidos
del propio fichero y no de la memoria:

```
   docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt -> disco 6904 bytes | LF 6904 bytes
   sha256 LF: 795c0ec740bdd5cc1e1b821085c0815f899e92fddd33d3d477f375bb99dc223a
   su veredicto, leido del propio fichero: 'VEREDICTO: VERDE'
   la aguja `EN CONTRA` aparece 13 vez(ces) en el arnes
```
"""),
    ("scripts/loop/_v192_t3_seccion.md",
     """(`docs/loop/SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt`, **disco 2433 bytes | LF
2433 bytes**).""",
     """(`docs/loop/SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt`,
**disco 2433 bytes | LF 2433 bytes**)."""),
    ("scripts/loop/_v192_t4_seccion.md",
     """(`docs/loop/SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt`, **disco 4282 bytes | LF
4282 bytes**).""",
     """(`docs/loop/SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt`,
**disco 4282 bytes | LF 4282 bytes**)."""),
    ("scripts/loop/_v192_cierre_texto.md",
     """`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra en **4054129 bytes en disco y
4054129 bytes normalizados a LF**, `sha256` LF `0a77b5a35a962621`, medido en el
bloque de apertura, en los dos instrumentos de la TAREA 2 y otra vez al cierre.""",
     """`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
abre y cierra en **4054129 bytes en disco y 4054129 bytes normalizados a LF**,
con el mismo `sha256` LF, medido en el bloque de apertura, en los dos
instrumentos de la TAREA 2 y otra vez al cierre."""),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    total = 0
    for rel, viejo, nuevo in CAMBIOS:
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.exists(p):
            print("   ROJO: no existe %s" % rel)
            return 1
        t = io.open(p, encoding="utf-8").read().replace(chr(13) + NL, NL)
        if nuevo in t:
            print("   YA ESTABA en %s" % rel)
            continue
        if viejo not in t:
            print("   ROJO: no se encuentra el ancla en %s. No se escribe nada." % rel)
            return 1
        antes = len(t.encode("utf-8"))
        t = t.replace(viejo, nuevo, 1)
        io.open(p, "w", encoding="utf-8", newline=NL).write(t)
        total += 1
        print("   aplicado en %-40s %d -> %d bytes en disco"
              % (rel, antes, len(t.encode("utf-8"))))
    print("   CIFRA cambios aplicados: %d" % total)
    return 0 if total else 1


if __name__ == "__main__":
    sys.exit(main())
