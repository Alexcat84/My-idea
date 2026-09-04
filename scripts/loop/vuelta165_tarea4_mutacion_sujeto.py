# -*- coding: utf-8 -*-
r"""vuelta165_tarea4_mutacion_sujeto.py . CASO POSITIVO POR MUTACION DEL
CLASIFICADOR DE SUJETO (TAREA 4 de la vuelta 165; adjudicaciones 6.5 y 6.6 del
acta 164).

POR QUE HACE FALTA. La TAREA 4 publica un veredicto por arnes (SUJETO VIVO,
SUJETO CONGELADO, NO DECIDIBLE) y de ese veredicto depende quien ENTRA en la
nomina de la bateria. `EJECUTOR.md` 1 lo dice con nombre desde el 29 ago 2026:
NINGUN caso rojo se publica como prueba sin haber corrido antes su prueba de
mutacion, y un veredicto que sea una constante literal no puede caer nunca.
Aqui NADA es constante: los veredictos salen de correr `clasificar_literal()`,
`senales()` y `clasificar()` sobre fuentes FABRICADAS, y la segunda pasada muta
cada esperado y exige que el caso CAIGA.

QUE COMPRUEBA, EN SUS CUATRO BLOQUES:
  A) el despojo de docstrings: una fuente que solo NOMBRA un artefacto vivo en
     su prosa NO puede clasificarse como sujeto vivo. Sin esto, la mitad de los
     41 saldria viva por hablar de si misma.
  B) la tabla, literal por literal, sobre los dos lados y sobre el neutro.
  C) el orden de precedencia: la MEDICION manda sobre la LECTURA. Un arnes que
     hoy sale ROJO es SUJETO VIVO aunque su fuente parezca congelada.
  D) la puerta de entrada: solo entra SUJETO CONGELADO, y ni NO DECIDIBLE ni
     SUJETO VIVO entran.

SUJETO: fuentes de mentira escritas en un temporal. P.16, quien fabrica limpia.

USO:  python scripts/loop/vuelta165_tarea4_mutacion_sujeto.py
"""
import io
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta165_tarea4_sujeto_de_los_41 as T   # noqa: E402


def prueba():
    print("=" * 78)
    print("VUELTA 165, TAREA 4: CASO POSITIVO POR MUTACION DEL CLASIFICADOR DE SUJETO")
    print("=" * 78)
    print("")
    casos = []

    print("A) EL DESPOJO DE DOCSTRINGS: HABLAR DE UN ARTEFACTO NO ES TOCARLO")
    solo_prosa = (
        '"""Este arnes EXPLICA que docs/loop/REPORTE.md se sobrescribe cada\n'
        'vuelta y que dataset/metadata/master_graph.json es el grafo vivo.\n'
        'No abre ninguno de los dos."""\n'
        'import io\n'
        'x = 1\n')
    codigo, _av = T.codigo_sin_docstrings(solo_prosa)
    lits = T.literales_de_ruta(codigo)
    print("   fuente que SOLO habla de dos artefactos vivos en su docstring")
    print("   CIFRA literales de ruta que quedan tras el despojo: %d" % len(lits))
    casos.append(("A_la_prosa_no_deja_literales", len(lits), 0))
    con_codigo = solo_prosa + 'f = io.open("docs/loop/REPORTE.md")\n'
    lits2 = T.literales_de_ruta(T.codigo_sin_docstrings(con_codigo)[0])
    print("   la misma fuente, pero ABRIENDO el fichero: %d literal(es)" % len(lits2))
    casos.append(("A_el_codigo_si_deja_literal", len(lits2), 1))
    print("")

    print("B) LA TABLA, LITERAL POR LITERAL")
    tabla = [
        ("docs/loop/REPORTE.md", "VIVO"),
        ("docs/loop/ACTA_AUDITOR.md", "VIVO"),
        ("dataset/metadata/master_graph.json", "VIVO"),
        ("verificar_mutaciones_viejas.py", "VIVO"),
        ("tallar_cabecera_reporte.py", "VIVO"),
        ("SUJETO_FIJO_V135_2E_REPORTE_134.md", "CONGELADO"),
        ("SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md", "CONGELADO"),
        ("vuelta115_guardas_cierre.py", "CONGELADO"),
        ("_v115_mut_z_copia.py", "CONGELADO"),
        ("web/package.json", "NEUTRO"),
    ]
    for literal, esperado in tabla:
        clase, motivo = T.clasificar_literal(literal)
        print("   %-46s -> %-10s (%s)" % (literal, clase, motivo[:52]))
        casos.append(("B_%s" % literal.replace("/", "_").replace(".", "_"),
                      clase, esperado))
    print("")

    tmp = tempfile.mkdtemp(prefix="v165_sujeto_")
    guardado = T.LOOP_SCRIPTS
    try:
        T.LOOP_SCRIPTS = tmp
        fuentes = {
            "arnes_vivo.py": 'import io\nio.open("docs/loop/REPORTE.md")\n',
            "arnes_congelado.py": 'import io\nio.open("SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md")\n',
            "arnes_sin_artefacto.py": 'x = [1, 2, 3]\nprint(sum(x))\n',
            "arnes_neutro.py": 'import io\nio.open("web/package.json")\n',
            "arnes_git_vivo.py": 'import subprocess\nsubprocess.run(["git", "rev-parse", "HEAD"])\n',
            "arnes_git_congelado.py": 'import subprocess\nsubprocess.run(["git", "show", "abc1234:x.md"])\n',
        }
        for nombre, texto in fuentes.items():
            io.open(os.path.join(tmp, nombre), "w", encoding="utf-8").write(texto)

        print("C) EL VEREDICTO SOBRE FUENTES FABRICADAS, Y LA PRECEDENCIA")
        esperados = {
            "arnes_vivo.py": "SUJETO VIVO",
            "arnes_congelado.py": "SUJETO CONGELADO",
            "arnes_sin_artefacto.py": "SUJETO CONGELADO",
            "arnes_neutro.py": "NO DECIDIBLE",
            "arnes_git_vivo.py": "SUJETO VIVO",
            "arnes_git_congelado.py": "SUJETO CONGELADO",
        }
        for nombre in sorted(fuentes):
            vi, co, ne, _av = T.senales(nombre)
            ver, mot = T.clasificar("OK", vi, co, ne)
            print("   %-26s verde hoy -> %-18s (%s)" % (nombre, ver, mot[:44]))
            casos.append(("C_verde_%s" % nombre.replace(".", "_"), ver,
                          esperados[nombre]))
        print("")
        print("   Y LA PRECEDENCIA: LA MEDICION MANDA SOBRE LA LECTURA.")
        for estado in ("ANCLA PERDIDA", "NO MORDIO"):
            vi, co, ne, _av = T.senales("arnes_congelado.py")
            ver, mot = T.clasificar(estado, vi, co, ne)
            print("   arnes_congelado.py con estado %-14s -> %s" % (estado, ver))
            casos.append(("C_precedencia_%s" % estado.replace(" ", "_"),
                          ver, "SUJETO VIVO"))
        vi, co, ne, _av = T.senales("arnes_sin_artefacto.py")
        ver, _m = T.clasificar("NO MORDIO", vi, co, ne)
        casos.append(("C_precedencia_sobre_el_sin_artefacto", ver, "SUJETO VIVO"))
        print("")

        print("D) LA PUERTA DE ENTRADA: SOLO ENTRA SUJETO CONGELADO")
        entran, fuera = [], []
        for nombre in sorted(fuentes):
            vi, co, ne, _av = T.senales(nombre)
            ver, _m = T.clasificar("OK", vi, co, ne)
            (entran if ver == "SUJETO CONGELADO" else fuera).append(nombre)
        print("   ENTRAN: %s" % ", ".join(entran))
        print("   NO ENTRAN: %s" % ", ".join(fuera))
        casos.append(("D_entran_solo_los_congelados", len(entran), 3))
        casos.append(("D_el_neutro_no_entra", "arnes_neutro.py" in entran, False))
        casos.append(("D_el_vivo_no_entra", "arnes_vivo.py" in entran, False))
        print("")
    finally:
        T.LOOP_SCRIPTS = guardado
        shutil.rmtree(tmp, ignore_errors=True)
        print("   P.16: el temporal se retira. Existe todavia: %s" % os.path.exists(tmp))
        print("")

    print("E) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-56s %s   (real=%r esperado=%r)"
              % (nombre[:56], "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("F) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        else:
            mutado = str(esperado) + "_MUTADO"
        cae = (real != mutado)
        print("   %-56s %s   (esperado mutado=%r)"
              % (nombre[:56], "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(prueba())
