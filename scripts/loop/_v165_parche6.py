# -*- coding: utf-8 -*-
"""Parche 6: el barrido del indice semantico pasa a ser un BARRIDO EXHAUSTIVO
sellado en la forma de la casa (marca, PREGUNTA, UNIVERSO, CARDINAL, las dos
piernas y sus lineas CIFRA con unidad), que es lo que
verificar_ausencias_del_reporte.py y verificar_cifras_del_reporte.py saben
cotejar. Trabajo, no instrumento."""
import io

p = "scripts/loop/vuelta165_tarea5_estado_nuevo.py"
s = io.open(p, encoding="utf-8").read()

viejo = '''    print("")
    print("   BARRIDO EXHAUSTIVO: el repo entero, buscando cualquier fichero que se")
    print("   llame como el que el script declara, para que la frase 'no existe en")
    print("   ninguna otra sede' no sea una busqueda negativa sin barrido detras")
    print("   (EJECUTOR.md 9: una busqueda negativa no se puede citar).")
    encontrados = []
    for base, dirs, ficheros in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in ("node_modules", ".git", ".next")]
        if nombre in ficheros:
            encontrados.append(os.path.relpath(os.path.join(base, nombre), RAIZ)
                               .replace(os.sep, "/"))
    for rel in sorted(encontrados):
        print("      %s" % rel)
    print("   CIFRA ficheros llamados %s en TODO el repo: %d"
          % (nombre, len(encontrados)))'''

nuevo = '''    print("")
    # EL BARRIDO VA SELLADO EN LA FORMA DE LA CASA, con sus DOS PIERNAS, porque
    # una busqueda negativa no se puede citar (EJECUTOR.md 9) y porque la frase
    # "no existe en ninguna otra sede" es una afirmacion de AUSENCIA.
    universo, por_nombre, por_contenido, no_leidos = [], [], [], 0
    for base, dirs, ficheros in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in ("node_modules", ".git", ".next",
                                                "__pycache__")]
        for f in ficheros:
            ruta = os.path.join(base, f)
            rel = os.path.relpath(ruta, RAIZ).replace(os.sep, "/")
            universo.append(rel)
            if f == nombre:
                por_nombre.append(rel)
    # LA SEGUNDA PIERNA, POR CONTENIDO: quien DECLARA la ruta del indice en su
    # texto. Se mira solo lo que es texto y cabe en memoria; lo que no se puede
    # decodificar se CUENTA y no se cuela como "sin coincidencia".
    marca = "semantic_index"
    for rel in universo:
        if not rel.endswith((".py", ".ts", ".tsx", ".js", ".json", ".md", ".txt")):
            continue
        if rel.endswith(nombre):
            continue
        try:
            texto = io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                            encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            no_leidos += 1
            continue
        if marca in texto:
            por_contenido.append(rel)
    print("BARRIDO EXHAUSTIVO")
    print("  PREGUNTA: existe el indice semantico en alguna sede que no sea la que")
    print("  sync_assets_web.py declara, o es esa la unica")
    print("  UNIVERSO: os.walk del repo entero ACOTADO a todo menos node_modules,")
    print("  .git, .next y __pycache__")
    print("  CARDINAL: %d" % len(universo))
    print("  POR NOMBRE: %s | %d ficheros con coincidencia" % (nombre, len(por_nombre)))
    for rel in sorted(por_nombre):
        print("      %s  [nombre]" % rel)
    print("  POR CONTENIDO: %s | %d ficheros con coincidencia"
          % (marca, len(por_contenido)))
    for rel in sorted(por_contenido)[:12]:
        print("      %s  [contenido]" % rel)
    if len(por_contenido) > 12:
        print("      ... y %d mas" % (len(por_contenido) - 12))
    print("  NO DECODIFICABLES (mirados y no leidos, NO cuentan como sin "
          "coincidencia): %d" % no_leidos)
    print("  VEREDICTO: %s" % ("UNA SOLA SEDE" if len(por_nombre) == 1
                               else "MAS DE UNA SEDE"))
    print("CIFRA ficheros del universo: %d ficheros" % len(universo))
    print("CIFRA sedes del indice halladas por nombre: %d ficheros" % len(por_nombre))
    print("CIFRA ficheros que solo lo nombran, sin serlo: %d ficheros"
          % len(por_contenido))'''

assert viejo in s
s = s.replace(viejo, nuevo, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("parche 6 aplicado al instrumento de la TAREA 5")
