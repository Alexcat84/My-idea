# -*- coding: utf-8 -*-
r"""_v183b_pegar_estado_de_salida.py . EL ESTADO DEL ARBOL AL SALIR DE ESTA
SESION, TALLADO DE SUS FICHEROS DE SALIDA Y PEGADO EN EL REPORTE.

POR QUE NO ES LA CABECERA DEL CIERRE, Y ES IMPORTANTE QUE NO LO SEA. La vuelta
183 no cierra en esta sesion: su bateria paro en el TRAMO 5 DE 9. La tabla de
APERTURA y CIERRE del reporte la talla `scripts/loop/tallar_cabecera_reporte.py`
y su hueco **se queda como esta**, porque una columna de cierre medida por una
sesion que no cierra es la caida de la vuelta 28 (medir temprano y publicar
tarde). Lo que este bloque publica es otra cosa y se llama por su nombre: **el
arbol que esta sesion deja**, medido DESPUES de su ultima operacion.

NINGUNA CELDA SE TECLEA (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO):
cada una se lee de su `docs/loop/SALIDA_V183B_*_SALIDA.txt` y el bloque dice de
cual. Si una salida falta o no se puede leer, la celda sale como NO SE PUDO LEER
y no se rellena con nada.

SE INSERTA JUSTO DESPUES DE `<!-- FIN ANEXO DE TAREAS -->`, que es donde termina
lo que esta sesion escribio y antes de donde `cerrar_reporte.py` anadira el
cuerpo del cierre el dia que la vuelta cierre. Es idempotente: si el bloque ya
esta, no lo duplica.

USO:
  python scripts/loop/_v183b_pegar_estado_de_salida.py
"""
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
REPORTE = os.path.join(LOOP, "REPORTE.md")
FIN_ANEXO = "<!-- FIN ANEXO DE TAREAS -->"
MARCA = "<!-- ESTADO DE SALIDA DE LA SESION -->"
FIN_MARCA = "<!-- FIN ESTADO DE SALIDA DE LA SESION -->"


def leer(nombre):
    ruta = os.path.join(LOOP, "SALIDA_V183B_%s_SALIDA.txt" % nombre)
    if not os.path.exists(ruta):
        return None, ruta
    return io.open(ruta, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL), ruta


def celda(nombre, patron, grupo=1):
    """LA CELDA, LEIDA DE SU FICHERO. Devuelve (valor, fichero)."""
    texto, ruta = leer(nombre)
    base = os.path.basename(ruta)
    if texto is None:
        return "NO SE PUDO LEER: no existe %s" % base, base
    m = re.search(patron, texto, re.MULTILINE)
    if not m:
        return "NO SE PUDO LEER en %s" % base, base
    return m.group(grupo).strip(), base


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    filas = []
    for etiqueta, nombre, patron in (
            ("HEAD tras la ultima operacion", "HEAD", r"^([0-9a-f]{40})"),
            ("Gate 0, veredicto", "GATE0_CMD1", r"^(GATE 0: .+)$"),
            ("Gate 0, exitcode", "GATE0_CMD1", r"^EXITCODE: (\d+)"),
            ("etiquetas de cara, exitcode", "CICLO_ETIQUETAS", r"^EXITCODE: (\d+)"),
            ("sync de assets, exitcode", "CICLO_SYNC", r"^EXITCODE: (\d+)"),
            ("conteo de aristas", "CONTEO", r"^\s*(WORK \| nodos .+)$"),
            ("filas en el calibrado", "DESFASE_CALIBRADO",
             r"^FILAS EN EL CALIBRADO: (\d+)"),
            ("desfase del calibrado rastreado", "DESFASE_CALIBRADO",
             r"^DESFASE DEL CALIBRADO RASTREADO: (\d+ fila\(s\))"),
            ("motor", "MOTOR", r"^(TODOS LOS TESTS PASARON \([^)]+\)\.)"),
            ("tsc", "TSC", r"^EXIT=(\d+)"),
            ("web, ficheros de test", "WEB", r"Test Files\s+(.+)$"),
            ("web, tests", "WEB", r"^\s+Tests\s+(.+)$"),
            ("git diff --numstat -- dataset/", "NUMSTAT_DATASET",
             r"^CIFRA filas: (\d+)")):
        valor, base = celda(nombre, patron)
        filas.append((etiqueta, valor, base))

    bloque = [MARCA]
    bloque.append("")
    bloque.append("## EL ARBOL QUE ESTA SESION DEJA, MEDIDO DESPUES DE SU ULTIMA OPERACION")
    bloque.append("")
    bloque.append("**ESTO NO ES LA CABECERA DEL CIERRE Y NO OCUPA SU HUECO.** La vuelta 183 **no")
    bloque.append("cierra aqui**: su bateria paro en el TRAMO 5 DE 9 y sin la composicion de los")
    bloque.append("nueve `scripts/loop/cerrar_reporte.py` no puede cerrarla. La tabla de APERTURA y")
    bloque.append("CIERRE sigue **PENDIENTE DE TALLAR AL CIERRE**, y publicar una columna de cierre")
    bloque.append("medida por una sesion que no cierra seria la caida de la vuelta 28. Lo que esta")
    bloque.append("tabla dice es otra cosa: **en que estado queda el arbol**.")
    bloque.append("")
    bloque.append("Tallada por `scripts/loop/_v183b_pegar_estado_de_salida.py`; **cada celda se lee")
    bloque.append("del fichero que la columna nombra y ninguna esta tecleada**.")
    bloque.append("")
    bloque.append("| que se mide | lo que dice | de que fichero sale |")
    bloque.append("|---|---|---|")
    for etiqueta, valor, base in filas:
        bloque.append("| %s | **%s** | `docs/loop/%s` |" % (etiqueta, valor, base))
    bloque.append("")
    bloque.append("**LA COMPARACION CON LA APERTURA, QUE ES LO QUE DA SENTIDO A LA CIFRA:** el")
    bloque.append("bloque de apertura de esta sesion (`docs/loop/SALIDA_V183B_APERTURA.txt` y sus")
    bloque.append("hermanas) midio lo mismo antes de la primera operacion. **Quien audite tiene los")
    bloque.append("dos juegos de ficheros en disco y puede restarlos sin creerle a nadie.**")
    bloque.append("")
    bloque.append("### CORRECCION DECLARADA SOBRE LA CABECERA DE ESTE REPORTE, Y NO SE BORRA LO QUE CORRIGE")
    bloque.append("")
    bloque.append("El bloque que abre este reporte, escrito por el esqueleto de la primera sesion de")
    bloque.append("la 183, dice con estas palabras: *\"La seccion 9 de este reporte lleva la bateria")
    bloque.append("entera dentro, no un hueco: esta vez si es su vuelta\"*. **Esa frase se queda")
    bloque.append("escrita y hoy es falsa, medido:** la bateria esta en **5 de 9** tramos con salida")
    bloque.append("sellada no vacia, el TRAMO 5 salio en **ROJO**, y `docs/loop/SALIDA_V183_BATERIA.txt`")
    bloque.append("**no existe**. La seccion 9 de este reporte **sigue sin escribirse**, y quien la")
    bloque.append("escriba tendra que decidir entre la corrida entera y el hueco declarado, que son")
    bloque.append("las dos ramas que `scripts/loop/cerrar_reporte.py` admite. **Una correccion que")
    bloque.append("tapa lo que corrige no se puede auditar** (`EJECUTOR.md` 8), asi que la promesa")
    bloque.append("de la cabecera queda donde estaba y esta linea dice lo que de verdad paso.")
    bloque.append("")
    bloque.append(FIN_MARCA)
    texto_bloque = NL.join(bloque)

    texto = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    if MARCA in texto:
        i = texto.index(MARCA)
        j = texto.index(FIN_MARCA) + len(FIN_MARCA)
        texto = texto[:i] + texto_bloque + texto[j:]
        print("EL BLOQUE YA ESTABA: se reemplaza entero, no se duplica.")
    else:
        if texto.count(FIN_ANEXO) != 1:
            print("ROJO: la marca %r aparece %d veces."
                  % (FIN_ANEXO, texto.count(FIN_ANEXO)))
            return 1
        texto = texto.replace(FIN_ANEXO, FIN_ANEXO + NL + NL + texto_bloque, 1)
    io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(texto)
    de_nuevo = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    for etiqueta, valor, base in filas:
        print("   %-34s %-46s %s" % (etiqueta, valor[:46], base))
    print("")
    print("ESCRITO: docs/loop/REPORTE.md (%d bytes LF, %d saltos de linea)"
          % (len(de_nuevo.encode("utf-8")), de_nuevo.count(NL)))
    print("guiones largos o medios en el reporte: %d"
          % (de_nuevo.count(chr(8212)) + de_nuevo.count(chr(8211))))
    print("celdas que NO se pudieron leer: %d"
          % len([1 for _e, v, _b in filas if v.startswith("NO SE PUDO LEER")]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
