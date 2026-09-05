# -*- coding: utf-8 -*-
r"""vuelta179_tarea4_juzgar_sujeto.py . LAS ENTRADAS QUE LA GUARDA DEL SUJETO
CONGELADO SENALA, JUZGADAS UNA A UNA Y CON SU PRUEBA.

TAREA 4 de la vuelta 179. **NO ARREGLA NINGUN ARNES Y NO CABLEA NADA.** Lee,
juzga y escribe `docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl`. El cableado de la
guarda al rojo global de la bateria se decide con los veredictos delante, que es
lo que el encargo manda: primero se juzgan, despues se cablea, y no al reves.

LA PREGUNTA QUE DECIDE, Y ES LA DEL ENCARGO: el arnes **de verdad ABRE un fichero
vivo de la campana**, o **lo NOMBRA sin abrirlo**.

COMO SE RESPONDE, Y ES MECANICO, NO A OJO. Se parsea el arnes con `ast` y se
buscan las llamadas que LEEN de disco (`open`, `io.open`, `json.load`,
`read_text`, `read_bytes`, `Path`, `subprocess.run` y `subprocess.check_output`).
De cada una se toma su trozo de codigo fuente entero con `ast.get_source_segment`
y se mira si dentro aparece la huella de un fichero vivo. Y SE RESUELVEN LAS
ASIGNACIONES SIMPLES: si el arnes hace `RUTA = os.path.join(RAIZ, "docs", "loop",
"REPORTE.md")` y despues `io.open(RUTA)`, eso ABRE, aunque la huella no este
escrita dentro del parentesis de la llamada.

QUE NO PUEDE ESTE METODO, Y SE DICE EN VEZ DE PRESUMIR: no sigue la huella a
traves de funciones ni de modulos importados. Una entrada que salga NOMBRA SIN
ABRIR y cuyo arnes llame a un tercero que si abre se escaparia. Por eso cada fila
publica LAS LINEAS EXACTAS donde aparece la huella, para que se pueda mirar.

LO QUE ESTE FICHERO NO HACE: no toca la nomina, no borra nada de ella
(`AUDITOR.md` 6.1), no arregla ningun arnes y no cambia el rojo de la bateria.

USO:
  python scripts/loop/vuelta179_tarea4_juzgar_sujeto.py
  python scripts/loop/vuelta179_tarea4_juzgar_sujeto.py --solo-mirar
"""
import argparse
import ast
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as VMV   # noqa: E402

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
SALIDA = os.path.join(RAIZ, "docs", "plan", "SUJETO_CONGELADO_VEREDICTOS.jsonl")

LECTORAS = ("open", "load", "read_text", "read_bytes", "read", "Path",
            "run", "check_output", "readlines", "iglob", "glob",
            "copy", "copyfile", "copytree")

# LO QUE CONVIERTE UNA LECTURA EN LECTURA DE SUJETO CONGELADO, y es estrecho a
# proposito. Leer `git show <sha>:docs/loop/REPORTE.md` NO es leer el REPORTE.md
# vivo: es leer un blob clavado por su huella, que no se mueve nunca mas. La
# primera version de este instrumento no lo distinguia y clasificaba
# `vuelta135_2e_mutacion_1.py` como ABRE FICHERO VIVO teniendo el sha delante.
#
# NO ENTRAN AQUI `tmp` NI `tempfile`: copiar el fichero VIVO a un temporal SI lo
# lee, y el resultado sigue dependiendo de lo que el fichero vivo diga hoy.
PATRON_SHA_CLAVADO = re.compile(r"\b[0-9a-f]{8,40}\b\s*(?::|\"\s*\+)")
MARCAS_DE_CLAVADO = ("cat-file", "SUJETO_FIJO", "SUJETO CONGELADO")


def llamadas_que_leen(arbol, fuente):
    """[(linea, trozo_de_codigo)] de toda llamada que lee de disco. PURA."""
    salida = []
    for n in ast.walk(arbol):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        nombre = f.attr if isinstance(f, ast.Attribute) else (
            f.id if isinstance(f, ast.Name) else "")
        if nombre not in LECTORAS:
            continue
        trozo = ast.get_source_segment(fuente, n) or ""
        salida.append((n.lineno, trozo))
    return salida


def asignaciones(arbol, fuente):
    """{nombre: trozo del valor asignado}. PURA. Solo asignaciones simples de
    nivel de modulo o de funcion a un unico nombre, que es la forma en que estos
    arneses declaran sus rutas."""
    mapa = {}
    for n in ast.walk(arbol):
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            mapa[n.targets[0].id] = ast.get_source_segment(fuente, n.value) or ""
    return mapa


def esta_clavado(trozo):
    """SI ESE TROZO DE CODIGO LEE UN SUJETO CLAVADO Y NO EL FICHERO VIVO. PURA.

    Un `git show <sha>:ruta` o un `git cat-file` sobre un blob leen algo que no
    se mueve; leerlo NO es leer el fichero vivo, y confundirlos acusa a un arnes
    que hace justo lo que la regla pide."""
    if any(m in trozo for m in MARCAS_DE_CLAVADO):
        return True
    return bool(PATRON_SHA_CLAVADO.search(trozo))


def abre_de_verdad(fuente, huellas):
    """(ABRE_O_NO, [(linea, huella, trozo, clavado)]). PURA: recibe el texto y la
    lista de huellas de fichero vivo."""
    try:
        arbol = ast.parse(fuente)
    except SyntaxError as e:
        return None, [(getattr(e, "lineno", 0), "(no parsea)", str(e))]
    mapa = asignaciones(arbol, fuente)
    pruebas = []
    for linea, trozo in llamadas_que_leen(arbol, fuente):
        # LA HUELLA DENTRO DEL PROPIO TROZO DE LA LLAMADA.
        for h in huellas:
            if h in trozo:
                pruebas.append((linea, h, trozo.replace(NL, " ")[:160],
                                esta_clavado(trozo)))
        # O DENTRO DE LO QUE SE LE ASIGNO A UN NOMBRE QUE LA LLAMADA USA.
        for nombre, valor in mapa.items():
            if not nombre or nombre not in trozo:
                continue
            for h in huellas:
                if h in valor and not any(p[1] == h and p[0] == linea for p in pruebas):
                    pruebas.append((linea, h,
                                    ("%s -> %s | %s" % (nombre, valor, trozo)
                                     ).replace(NL, " ")[:160],
                                    esta_clavado(valor + " " + trozo)))
    vivas = [p for p in pruebas if not p[3]]
    return bool(vivas), pruebas


def lineas_con_huella(fuente, huellas):
    """[(numero, huella, linea)] de TODA aparicion de una huella en el texto,
    abra o no. PURA. Es lo que se publica para que el ojo pueda mirar donde el
    metodo mecanico no llega."""
    salida = []
    for i, l in enumerate(fuente.split(NL), 1):
        for h in huellas:
            if h in l:
                salida.append((i, h, l.strip()[:120]))
    return salida


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-mirar", dest="solo_mirar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    p = print

    p("=" * 78)
    p("LAS DEL SUJETO CONGELADO, JUZGADAS UNA A UNA (vuelta 179, TAREA 4)")
    p("=" * 78)
    p("")

    head = VMV.corte_de_git()
    malas = VMV.guarda_del_sujeto_congelado()
    p("A) LO QUE LA GUARDA SENALA HOY, CON SU CORTE")
    p("   CORTE: HEAD %s" % head)
    p("   CIFRA entradas de la nomina: %s"
      % VMV.sello_de_corte(len(VMV.VIEJAS), head))
    p("   CIFRA entradas que la guarda senala: %d" % len(malas))
    cuenta = {}
    for _n, v, _vv in malas:
        cuenta[v] = cuenta.get(v, 0) + 1
    for v in sorted(cuenta):
        p("   CIFRA %-14s: %d" % (v, cuenta[v]))
    p("")
    p("   Y HAY QUE DECIR QUE ESTA CIFRA SE MOVIO DENTRO DE ESTA MISMA VUELTA.")
    p("   El encargo habla de QUINCE, y quince eran al abrir. La TAREA 1.c metio")
    p("   cinco arneses en la nomina y por eso el denominador y el numerador son")
    p("   otros. LAS DOS CIFRAS SON VERDADERAS Y CADA UNA LLEVA SU CORTE, que es")
    p("   exactamente para lo que la TAREA 1.d cableo el sello.")
    p("")

    p("B) CADA UNA, JUZGADA CON SU PRUEBA MECANICA")
    filas = []
    for nombre, veredicto_guarda, vive in malas:
        ruta = os.path.join(LOOP, nombre)
        fuente = io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL) \
            if os.path.exists(ruta) else ""
        abre, pruebas = abre_de_verdad(fuente, vive)
        todas = lineas_con_huella(fuente, vive)
        vivas = [q for q in pruebas if len(q) > 3 and not q[3]]
        clavadas = [q for q in pruebas if len(q) > 3 and q[3]]
        declarado = nombre in VMV.CASOS_DECLARADOS
        if declarado:
            mio = "CASO DECLARADO"
        elif abre:
            mio = "ABRE FICHERO VIVO"
        elif clavadas:
            mio = "ABRE UN SUJETO YA CLAVADO"
        else:
            mio = "LO NOMBRA SIN ABRIRLO"
        p("")
        p("   %-46s guarda: %-14s -> %s" % (nombre, veredicto_guarda, mio))
        p("      ficheros vivos que la guarda le atribuye: %s" % ", ".join(vive))
        p("      CIFRA apariciones de esas huellas en el texto: %d" % len(todas))
        p("      CIFRA llamadas que LEEN de disco con una huella dentro: %d" % len(pruebas))
        p("      CIFRA de esas que leen el fichero VIVO: %d" % len(vivas))
        p("      CIFRA de esas que leen un blob CLAVADO por su sha: %d" % len(clavadas))
        for linea, h, trozo, clav in pruebas[:4]:
            p("         %s linea %d | %s | %s"
              % ("CLAVADA" if clav else "PRUEBA ", linea, h, trozo))
        if not pruebas:
            for linea, h, texto in todas[:4]:
                p("         SOLO LA NOMBRA, linea %d | %s | %s" % (linea, h, texto))
        filas.append({
            "id": "SUJETO-CONGELADO", "vuelta": 179, "fecha": "2026-09-05",
            "arnes": nombre,
            "veredicto_de_la_guarda": veredicto_guarda,
            "veredicto_de_la_lectura": mio,
            "ficheros_vivos_atribuidos": list(vive),
            "cifra_apariciones_en_el_texto": len(todas),
            "cifra_llamadas_que_leen_con_huella": len(pruebas),
            "cifra_lecturas_del_fichero_vivo": len(vivas),
            "cifra_lecturas_de_blob_clavado": len(clavadas),
            "evidencia": [{"linea": l, "huella": h, "codigo": c,
                           "lee_un_blob_clavado": bool(cl)}
                          for l, h, c, cl in pruebas],
            "apariciones": [{"linea": l, "huella": h, "texto": t} for l, h, t in todas],
            "que_haria_falta":
                ("congelarle el sujeto: fabricarlo en un temporal, clavarlo por "
                 "sha256 o leerlo de un blob de git" if mio == "ABRE FICHERO VIVO"
                 else ("nada: esta exento por CASOS_DECLARADOS"
                       if mio == "CASO DECLARADO"
                       else ("nada de fondo: YA lee un sujeto clavado por su sha. "
                             "Lo unico que le falta es DECLARARLO con el literal que "
                             "la guarda busca, para que deje de salir NO DECIDIBLE"
                             if mio == "ABRE UN SUJETO YA CLAVADO"
                             else "que el propio arnes DECLARE su sujeto congelado, "
                                  "que es lo unico que le falta: no abre nada vivo"))),
            "arreglado_en_esta_vuelta": False,
            "nota": "El encargo de la vuelta 179 prohibe arreglar arneses y prohibe "
                    "cablear esta guarda al rojo global de la bateria. Se juzga y se "
                    "escribe. NADA se borra de la nomina (AUDITOR.md 6.1).",
        })
    p("")

    p("C) EL REPARTO DE MI LECTURA, CONTRA EL DE LA GUARDA")
    mio_cuenta = {}
    for f in filas:
        mio_cuenta[f["veredicto_de_la_lectura"]] = \
            mio_cuenta.get(f["veredicto_de_la_lectura"], 0) + 1
    p("| veredicto de la lectura | arneses |")
    p("|---|---:|")
    for k in sorted(mio_cuenta):
        p("| %s | **%d** |" % (k, mio_cuenta[k]))
    p("| **total** | **%d** |" % sum(mio_cuenta.values()))
    p("   LA RESTA: %d = %d, y las que la guarda senala son %d. CALZA: %s"
      % (sum(mio_cuenta.values()), len(filas), len(malas),
         "SI" if sum(mio_cuenta.values()) == len(malas) else "NO"))
    p("")

    p("D) EL CRUCE, QUE ES LO QUE DICE SI LA GUARDA ACIERTA")
    cruce = {}
    for f in filas:
        k = (f["veredicto_de_la_guarda"], f["veredicto_de_la_lectura"])
        cruce[k] = cruce.get(k, 0) + 1
    p("| la guarda dice | la lectura dice | arneses |")
    p("|---|---|---:|")
    for k in sorted(cruce):
        p("| %s | %s | **%d** |" % (k[0], k[1], cruce[k]))
    p("")

    if a.solo_mirar:
        p("   --solo-mirar: NO se escribe el registro.")
        return 0

    with io.open(SALIDA, "w", encoding="utf-8", newline=NL) as fh:
        for f in filas:
            fh.write(json.dumps(f, ensure_ascii=False) + NL)
    crudo = io.open(SALIDA, "rb").read()
    p("E) EL REGISTRO PROPIO, ESCRITO")
    p("   docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl")
    p("   CIFRA filas: %d" % len(filas))
    p("   CIFRA bytes en disco: %d | bytes normalizados a LF: %d"
      % (os.path.getsize(SALIDA), len(crudo.replace(chr(13).encode(), b""))))
    p("")

    p("F) LO QUE **NO** SE HIZO, Y ES TAN PARTE DEL ENCARGO COMO LO QUE SI")
    p("   NINGUN ARNES SE ARREGLO en esta vuelta: 0 ficheros de scripts/loop/")
    p("   tocados por este instrumento.")
    p("   LA GUARDA NO SE CABLEO al rojo global de la bateria: sigue corriendo")
    p("   sola en su carril con --sujeto-congelado.")
    p("   NADA SE BORRO DE LA NOMINA: sigue teniendo %s entradas."
      % VMV.sello_de_corte(len(VMV.VIEJAS), head))
    p("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
