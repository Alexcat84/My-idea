#!/bin/sh
# vuelta191_rehacer.sh . REHACE EL REPORTE DE LA VUELTA 191 DESDE SU ESQUELETO Y
# SUS CINCO SECCIONES, EN UNA SOLA ORDEN Y REPETIBLE.
#
# POR QUE EXISTE, Y LA CAUSA ES DE ESTA MISMA VUELTA: el cierre saco 22 cifras de
# bytes publicadas SIN SU PAREJA, y arreglarlas obliga a re escribir las
# secciones y a volver a montar el reporte entero. Hacerlo a mano son ocho
# ordenes largas con sus estados y sus pruebas tecleados; tecleados en cada
# intento, la orden NO SE PUEDE REPETIR IGUAL, y una orden que no se puede
# repetir no se puede auditar.
#
# QUE HACE, EN ESTE ORDEN:
#   1. devuelve docs/loop/REPORTE.md a lo que git lleva en HEAD, EN LF y con
#      `git show`, NUNCA con `git checkout --`: la 5.3 del acta 191 midio que
#      `git checkout --` lo devuelve en CRLF y cambia los bytes publicados;
#   2. corre el esqueleto con --rehacer, que exige que lo que se va a pisar sea
#      el reporte de ESTA vuelta y este commiteado sin cambios en el arbol;
#   3. anexa las CINCO tareas con su estado y sus pruebas.
#
# LO QUE NO HACE: no cierra el reporte. Eso es de scripts/loop/vuelta191_cerrar.sh.
#
# USO:
#   sh scripts/loop/vuelta191_rehacer.sh

set -e

python - <<'PY'
import io, subprocess, hashlib
r = subprocess.run(["git", "show", "HEAD:docs/loop/REPORTE.md"], capture_output=True)
assert r.returncode == 0, r.stderr[:200]
blob = r.stdout.decode("utf-8").replace("\r\n", "\n")
io.open("docs/loop/REPORTE.md", "w", encoding="utf-8", newline="\n").write(blob)
d = io.open("docs/loop/REPORTE.md", "rb").read()
lf = d.replace(b"\r\n", b"\n")
print("PASO 1. REPORTE.md devuelto a HEAD EN LF: disco %d bytes | LF %d bytes | sha256 LF %s"
      % (len(d), len(lf), hashlib.sha256(lf).hexdigest()[:16]))
PY

python scripts/loop/vuelta191_esqueleto_reporte.py --rehacer

python scripts/loop/anexar_tarea_al_reporte.py --tarea 1 \
  --estado "CERRADA EN VERDE" \
  --pruebas '`SALIDA_V191_T1A_REGISTRO_R53.txt`, `SALIDA_V191_T1A_RECORRIDO_SIN_ESCRIBIR.txt`, `SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt`, `SALIDA_V191_T1A_SIMULACION.txt`' \
  --cuerpo scripts/loop/_v191_t1_seccion.md

python scripts/loop/anexar_tarea_al_reporte.py --tarea 2 \
  --estado "CERRADA, CON UNA DISCREPANCIA FUERA DEL MARCADO TRAIDA ENTERA" \
  --pruebas '`SALIDA_V191_T2_AISLAMIENTO.txt`, `SALIDA_V191_T2_CIEGA.txt`, `SALIDA_V191_T2_MIS_CLASES.txt`, `SALIDA_V191_T2_DESTAPE.txt`, `SALIDA_V191_T2_COTEJO.txt`' \
  --cuerpo scripts/loop/_v191_t2_seccion.md

python scripts/loop/anexar_tarea_al_reporte.py --tarea 3 \
  --estado "CERRADA EN VERDE" \
  --pruebas '`SALIDA_V191_T3_CENSO_ANTES.txt`, `SALIDA_V191_T3_CENSO_DESPUES.txt`, `SALIDA_V191_T3_ARREGLO.txt`, `SALIDA_V191_T3_MUTACION_LINEAS.txt`' \
  --cuerpo scripts/loop/_v191_t3_seccion.md

python scripts/loop/anexar_tarea_al_reporte.py --tarea 4 \
  --estado "CERRADA EN VERDE, CON UNA PARADA DECLARADA" \
  --pruebas '`SALIDA_V191_T4_MUTACION_VEREDICTO.txt`, `SALIDA_V191_APERTURA.txt` bloque `H.5`' \
  --cuerpo scripts/loop/_v191_t4_seccion.md

python scripts/loop/anexar_tarea_al_reporte.py --tarea 5 \
  --estado "CERRADA: LAS TRES CIFRAS ESTAN Y NO ALCANZAN PARA CONCLUIR" \
  --pruebas '`SALIDA_V191_T5_MARCA_CONTRA_DIFICULTAD.txt`, `SALIDA_V191_T2_COTEJO.txt`' \
  --cuerpo scripts/loop/_v191_t5_seccion.md
