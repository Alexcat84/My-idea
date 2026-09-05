# -*- coding: utf-8 -*-
r"""_v172_parche_contador.py . ANDAMIO DE UN SOLO USO DE LA VUELTA 172, TAREA 2.a.

METE `docs/loop/reportes/REPORTE_V<N>.md` EN LA LISTA DE NARRATIVOS DEL BUCLE de
`scripts/loop/vuelta48_contar_ld.py`, POR PATRON DE LA CARPETA DE ARCHIVO Y NO
POR EL NOMBRE DE UNA VUELTA (adjudicacion 6.1 del acta 171).

Y SACA LA DECISION DE EXCLUIR A UNA FUNCION PURA, `motivo_de_exclusion(rel)`,
porque hoy vive dentro del bucle de `main()` y **ahi no hay nada que un arnes
pueda llamar**. Una guarda que no se puede llamar no se puede probar por
mutacion, y `EJECUTOR.md` 1 exige la prueba de mutacion. `main()` pasa a llamar
a esa funcion: UNA SOLA FUENTE, no dos copias del criterio.

Cada sustitucion lleva su `assert`. Si el contador cambia debajo, esto CAE.

USO:  python scripts/loop/_v172_parche_contador.py
"""
import io
import os
import py_compile

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "scripts", "loop", "vuelta48_contar_ld.py")

BLOQUE_NUEVO = '''# EL ARCHIVO DE LOS REPORTES (correccion declarada 4, vuelta 172, TAREA 2.a;
# adjudicacion 6.1 del acta 171). `docs/loop/reportes/REPORTE_V<N>.md` NO SE
# PARECE al reporte: ES el reporte, guardado bajo otro nombre por
# `archivar_reporte.py`. Lo probo el sha256 de la vuelta 171, identico byte a
# byte al blob de `docs/loop/REPORTE.md` en `ca55afd8`. Sin esta linea, cada
# vuelta que archiva su reporte le mete al universo todos los numeros de `LD`
# que ese reporte NARRABA, y el instrumento vuelve a leerse a si mismo por la
# puerta de atras, que es la misma caida de las correcciones 1 y 2.
#
# ES UN PATRON Y NO UNA LISTA DE NOMBRES, a proposito: si aqui pusiera
# `REPORTE_V171.md`, dentro de tres vueltas habria que volver a tocar esto y
# nadie se acordaria. El patron cubre la carpeta de archivo entera y SOLO esa.
#
# LO QUE ESTO NO ES: no es la guarda general sobre ficheros nuevos bajo `docs/`
# que el acta 170 reservo al fundador en su seccion 7.3. Esa sigue siendo suya.
RE_ARCHIVO_DEL_REPORTE = re.compile(r"^docs/loop/reportes/REPORTE_V\\d+\\.md$")


def motivo_de_exclusion(rel):
    """POR QUE UN FICHERO NO ENTRA EN EL UNIVERSO. Devuelve la etiqueta del
    motivo, o None si el fichero SI cuenta.

    PURA A PROPOSITO (vuelta 172, TAREA 2.a): antes este criterio vivia dentro
    del bucle de `main()` y no habia nada que un arnes pudiera llamar, asi que
    no se podia probar por mutacion. Ahora `main()` llama aqui y no hay dos
    copias del criterio.

    `rel` es la ruta relativa a la raiz, con barra unix."""
    nombre = rel.rsplit("/", 1)[-1]
    if nombre.startswith("SALIDA_"):
        return "SALIDA"
    if rel in NARRATIVOS_DEL_BUCLE:
        return "NARRATIVO"
    if RE_ARCHIVO_DEL_REPORTE.match(rel):
        return "NARRATIVO"
    if RE_ARNES.match(rel):
        return "ARNES"
    return None
'''

MAIN_VIEJO = [
    '            if f.startswith("SALIDA_"):',
    '                excluidos.append(rel_f)',
    '                continue',
    '            if rel_f in NARRATIVOS_DEL_BUCLE:',
    '                excluidos_narrativos.append(rel_f)',
    '                continue',
    '            if RE_ARNES.match(rel_f):',
    '                excluidos_arnes.append(rel_f)',
    '                continue',
]

MAIN_NUEVO = [
    '            # UNA SOLA FUENTE DEL CRITERIO: la funcion pura de arriba, que es',
    '            # la que el arnes de mutacion llama (vuelta 172, TAREA 2.a).',
    '            motivo = motivo_de_exclusion(rel_f)',
    '            if motivo == "SALIDA":',
    '                excluidos.append(rel_f)',
    '                continue',
    '            if motivo == "NARRATIVO":',
    '                excluidos_narrativos.append(rel_f)',
    '                continue',
    '            if motivo == "ARNES":',
    '                excluidos_arnes.append(rel_f)',
    '                continue',
]


def main():
    t = io.open(RUTA, encoding="utf-8").read().replace(chr(13) + NL, NL)

    ancla = 'RE_ID = re.compile(r"LD-(\\d+)")'
    assert t.count(ancla) == 1, "el ancla RE_ID no aparece una sola vez"
    t = t.replace(ancla, BLOQUE_NUEVO + NL + ancla)

    viejo, nuevo = NL.join(MAIN_VIEJO), NL.join(MAIN_NUEVO)
    assert t.count(viejo) == 1, "el bloque de exclusiones de main() no calza"
    t = t.replace(viejo, nuevo)

    # La correccion declarada, en el docstring, sin borrar las tres viejas.
    ancla_doc = 'LA VARA, escrita para poder discutirla: quedan EXCLUIDOS los ficheros'
    assert t.count(ancla_doc) == 1
    correccion = (
        'CORRECCION DECLARADA 4 (vuelta 172, TAREA 2.a; adjudicacion 6.1 del acta 171).' + NL +
        'EL ARCHIVO DE LOS REPORTES ES EL REPORTE. Desde que `archivar_reporte.py` guarda' + NL +
        'cada reporte en `docs/loop/reportes/REPORTE_V<N>.md`, ese fichero entraba en el' + NL +
        'universo y le metia TODOS los numeros de `LD` que el reporte narraba. Medido en' + NL +
        'la vuelta 171: el sha256 de `docs/loop/reportes/REPORTE_V170.md` es identico byte' + NL +
        'a byte al blob de `docs/loop/REPORTE.md` en `ca55afd8`, o sea que el instrumento' + NL +
        'contaba como encargo un fichero que ya excluye por NARRATIVO DEL BUCLE, solo que' + NL +
        'con otro nombre. Entra por PATRON de la carpeta de archivo, no por el nombre de' + NL +
        'una vuelta, para que no haya que volver a tocarlo cada tres vueltas. NO es la' + NL +
        'guarda general sobre ficheros nuevos bajo `docs/`, que el acta 170 reservo al' + NL +
        'fundador.' + NL + NL)
    t = t.replace(ancla_doc, correccion + ancla_doc)

    io.open(RUTA, "w", encoding="utf-8", newline=NL).write(t)
    py_compile.compile(RUTA, doraise=True)
    print("PARCHEADO: scripts/loop/vuelta48_contar_ld.py")
    print("COMPILA: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
