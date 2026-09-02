# -*- coding: utf-8 -*-
r"""vuelta146_1c_cifras_ficha_op_a_01.py . Instrumento propio del ejecutor,
vuelta 146, TAREA 1.c (CORRECCION 24) y TAREA 3.f (la truncacion a 31).

QUE MIDE Y CONTRA QUE. Las SEIS cifras que la ficha de `OP-A-01` publica con
`fecha_corte 2026-08-11`, recomputadas sobre el grafo de SU CORTE y sobre el de
HOY, para poder decir CUALES REPRODUCEN Y CUALES NO sin tocar el texto de la
ficha (`EJECUTOR.md` 8: una correccion que tapa lo que corrige no se puede
auditar). Las seis, con el literal de la ficha al lado:

  (1) "3.521 nodos vivos"                        -> vivos del ref
  (2) "67 con mas de un libro"                   -> nodos vivos cuyo campo
      `fuente` trae MAS DE UNA declaracion
  (3) "70 declaraciones en segunda posicion o posterior" -> suma, sobre nodos
      vivos, de las declaraciones de indice >= 1
  (4) "Hugos aparece con DOS grafias"            -> grafias distintas del autor
  (5) "Horowitz con TRES"                        -> grafias distintas del autor
  (6) "sin normalizar el recorte da 23 y 16 donde el canonico da 21 y 14" ->
      nodos que declaran al autor, contados SIN normalizar (cualquier grafia) y
      contados SOLO con la grafia canonica (la mas larga del autor)

LA UNIDAD DE (6) NO ESTA ESCRITA EN LA FICHA, asi que NO SE ADIVINA: se
imprimen las CUATRO lecturas construibles (sobre todos los nodos vivos y sobre
el recorte, es decir los vivos con mas de un libro) y el reporte declara cual
reproduce y cual no. Es la leccion de la caida 4.7 del acta 144: una cifra sin
unidad nombrada es una cifra que no se puede cotejar.

EL SEPARADOR DE DECLARACIONES es ` | ` (barra vertical con espacios), medido y
argumentado en `scripts/loop/vuelta130_censo_fuente.py` y escrito en la cabecera
de `docs/plan/OP_S_11_MAPEO_PROPUESTO.md`. El `;` NO separa declaraciones: separa
AUTORES del mismo libro (el caso vivo: `Out of the Crisis, Reissue - Deming, W.
Edwards; Cahill, Kev`).

EL BARRIDO DE LA TRUNCACION (TAREA 3.f). Sobre las grafias DISTINTAS del campo
`fuente` del ref, busca las parejas TITULO-PREFIJO CON EL MISMO AUTOR: se parte
cada grafia por el separador ` - ` en (titulo, autor); una pareja entra si los
DOS tienen autor, el autor es IDENTICO y un titulo es PREFIJO ESTRICTO del otro.
Por cada pareja publica la longitud de los dos titulos y cuantos nodos VIVOS y
DEPRECADOS usa cada grafia. NO TOCA NADA: mide y declara.

POR QUE ESA REGLA Y NO OTRA, dicho para que se pueda discutir: una pareja donde
UNO de los dos NO trae autor (`The Hard Thing About Hard Things` a secas contra
`The Hard Thing About Hard Things - Ben Horowitz`) NO es una truncacion de
campo, es una grafia sin autor; y una pareja con el MISMO titulo y el autor
distinto (`The Field Guide to Understandin - Dekker, Sidney` contra el mismo con
`;` al final) es un sufijo de autor, no un recorte de titulo. Las dos especies se
CUENTAN APARTE y se publican, para que la afirmacion "hay exactamente N" diga de
que N habla.

USO:
  python scripts/loop/vuelta146_1c_cifras_ficha_op_a_01.py 0e5e0c60 WORK
"""
import io
import json
import subprocess
import sys

SEP = " | "
AUTORES = ("Hugos", "Horowitz")


def cargar(ref):
    if ref == "WORK":
        with io.open("dataset/metadata/master_graph.json", encoding="utf-8") as f:
            return json.load(f)
    b = subprocess.run(["git", "show", "%s:dataset/metadata/master_graph.json" % ref],
                       capture_output=True)
    if b.returncode != 0:
        raise SystemExit("ROJO: no se pudo leer %s" % ref)
    return json.loads(b.stdout.decode("utf-8"))


def declaraciones(nodo):
    f = nodo.get("fuente")
    if not f or not isinstance(f, str):
        return []
    return [d.strip() for d in f.split(SEP) if d.strip()]


def partir(grafia):
    """(titulo, autor) por el separador ' - '; autor None si no lo trae. Se
    parte por la PRIMERA ocurrencia, que es como el catalogo la escribe."""
    if " - " not in grafia:
        return grafia, None
    t, a = grafia.split(" - ", 1)
    return t.strip(), a.strip()


def medir(ref):
    G = cargar(ref)["nodos"]
    vivos = [n for n in G.values() if not n.get("deprecado")]
    con_mas_de_uno = [n for n in vivos if len(declaraciones(n)) > 1]
    segunda_o_posterior = sum(max(0, len(declaraciones(n)) - 1) for n in vivos)

    graf_todos, graf_vivos = {}, {}
    usos_vivos, usos_depre = {}, {}
    for n in G.values():
        for d in declaraciones(n):
            graf_todos[d] = graf_todos.get(d, 0) + 1
            if n.get("deprecado"):
                usos_depre[d] = usos_depre.get(d, 0) + 1
            else:
                usos_vivos[d] = usos_vivos.get(d, 0) + 1
                graf_vivos[d] = graf_vivos.get(d, 0) + 1

    por_autor = {}
    for a in AUTORES:
        gt = sorted(g for g in graf_todos if a in g)
        gv = sorted(g for g in graf_vivos if a in g)
        canonica = max(gt, key=len) if gt else None

        def cuenta(pool, solo_canonica, autor=a, canon=canonica):
            k = 0
            for n in pool:
                ds = declaraciones(n)
                if solo_canonica:
                    if canon is not None and canon in ds:
                        k += 1
                else:
                    if any(autor in d for d in ds):
                        k += 1
            return k

        por_autor[a] = {
            "grafias_todos": gt, "grafias_vivos": gv, "canonica": canonica,
            "vivos_sin_normalizar": cuenta(vivos, False),
            "vivos_canonica": cuenta(vivos, True),
            "recorte_sin_normalizar": cuenta(con_mas_de_uno, False),
            "recorte_canonica": cuenta(con_mas_de_uno, True),
        }

    distintas = sorted(graf_todos)
    prefijo_mismo_autor, prefijo_sin_autor, mismo_titulo_otro_autor = [], [], []
    for i, x in enumerate(distintas):
        tx, ax = partir(x)
        for y in distintas[i + 1:]:
            ty, ay = partir(y)
            corto, largo = (tx, ty) if len(tx) < len(ty) else (ty, tx)
            es_prefijo = corto != largo and largo.startswith(corto)
            if es_prefijo and ax is not None and ay is not None and ax == ay:
                prefijo_mismo_autor.append((x, y))
            elif es_prefijo and (ax is None) != (ay is None):
                prefijo_sin_autor.append((x, y))
            elif tx == ty and ax != ay:
                mismo_titulo_otro_autor.append((x, y))

    # EL CENSO DE TITULOS DE LONGITUD EXACTA 31 (vuelta 146, TAREA 3.f). El
    # barrido por PAREJAS de arriba solo puede ver una truncacion cuando la
    # forma LARGA tambien vive en el catalogo; una grafia recortada cuyo
    # original nadie escribio nunca es invisible para el. Este censo mira la
    # otra cara de la misma pregunta y no depende de que haya pareja: cuantas
    # grafias distintas tienen el TITULO de longitud exactamente 31, que es la
    # firma del recorte de campo. Se publica APARTE y no se suma a las parejas:
    # son dos unidades distintas (CORRECCION 18, dos unidades no comparten
    # columna).
    titulos_31 = []
    for g in distintas:
        t, _ = partir(g)
        if len(t) == 31:
            titulos_31.append(g)

    return {
        "titulos_31": titulos_31,
        "ref": ref, "nodos": len(G), "vivos": len(vivos),
        "con_mas_de_uno": len(con_mas_de_uno),
        "segunda_o_posterior": segunda_o_posterior,
        "grafias_distintas_todos": len(graf_todos),
        "grafias_distintas_vivos": len(graf_vivos),
        "por_autor": por_autor,
        "prefijo_mismo_autor": prefijo_mismo_autor,
        "prefijo_sin_autor": prefijo_sin_autor,
        "mismo_titulo_otro_autor": mismo_titulo_otro_autor,
        "usos_vivos": usos_vivos, "usos_depre": usos_depre,
    }


def imprimir(m):
    print("=" * 78)
    print("REF: %s  (nodos %d, vivos %d)" % (m["ref"], m["nodos"], m["vivos"]))
    print("(1) nodos vivos: %d                     [ficha OP-A-01, corte 11 ago: 3521]" % m["vivos"])
    print("(2) nodos vivos con MAS DE UN libro: %d [ficha: 67]" % m["con_mas_de_uno"])
    print("(3) declaraciones en 2.a posicion o posterior: %d [ficha: 70]" % m["segunda_o_posterior"])
    print("    grafias distintas del campo fuente: %d (todos) / %d (vivos)"
          % (m["grafias_distintas_todos"], m["grafias_distintas_vivos"]))
    for a in AUTORES:
        d = m["por_autor"][a]
        esperado = "2" if a == "Hugos" else "3"
        print("  %s: %d grafias TODOS LOS NODOS / %d grafias SOLO VIVOS  [ficha: %s]"
              % (a, len(d["grafias_todos"]), len(d["grafias_vivos"]), esperado))
        for g in d["grafias_todos"]:
            print("      %r  vivos=%d depre=%d" % (g, m["usos_vivos"].get(g, 0), m["usos_depre"].get(g, 0)))
        print("      canonica (la mas larga): %r" % d["canonica"])
        print("      nodos que lo declaran, VIVOS:   sin normalizar %d / solo canonica %d"
              % (d["vivos_sin_normalizar"], d["vivos_canonica"]))
        print("      nodos que lo declaran, RECORTE: sin normalizar %d / solo canonica %d"
              % (d["recorte_sin_normalizar"], d["recorte_canonica"]))
    print("  [ficha, cifra (6): sin normalizar 23 y 16, canonico 21 y 14]")
    print("BARRIDO DE LA TRUNCACION (parejas titulo-prefijo con el MISMO autor):")
    for x, y in m["prefijo_mismo_autor"]:
        tx, _ = partir(x)
        ty, _ = partir(y)
        print("   %r [titulo %d car] vivos=%d depre=%d"
              % (x, len(tx), m["usos_vivos"].get(x, 0), m["usos_depre"].get(x, 0)))
        print("   %r [titulo %d car] vivos=%d depre=%d"
              % (y, len(ty), m["usos_vivos"].get(y, 0), m["usos_depre"].get(y, 0)))
    print("   OTRAS ESPECIES, CONTADAS APARTE Y NO SUMADAS:")
    for rot, lst in (("titulo-prefijo pero UNO SIN AUTOR", m["prefijo_sin_autor"]),
                     ("mismo titulo y AUTOR distinto", m["mismo_titulo_otro_autor"])):
        print("     %s: %d" % (rot, len(lst)))
        for x, y in lst:
            print("        %r  /  %r" % (x, y))
    print("   CENSO APARTE, TITULOS DE LONGITUD EXACTA 31 (la firma del recorte de campo,")
    print("   se vea o no la forma larga en el catalogo):")
    for g in m["titulos_31"]:
        print("      %r  vivos=%d depre=%d" % (g, m["usos_vivos"].get(g, 0), m["usos_depre"].get(g, 0)))
    print("CIFRA nodos vivos %s: %d nodos" % (m["ref"], m["vivos"]))
    print("CIFRA grafias con titulo de 31 caracteres %s: %d grafias" % (m["ref"], len(m["titulos_31"])))
    print("CIFRA nodos con mas de un libro %s: %d nodos" % (m["ref"], m["con_mas_de_uno"]))
    print("CIFRA declaraciones en segunda posicion o posterior %s: %d lineas"
          % (m["ref"], m["segunda_o_posterior"]))
    print("CIFRA grafias distintas del campo fuente %s: %d grafias"
          % (m["ref"], m["grafias_distintas_todos"]))
    for a in AUTORES:
        d = m["por_autor"][a]
        print("CIFRA grafias de %s todos los nodos %s: %d grafias" % (a, m["ref"], len(d["grafias_todos"])))
        print("CIFRA grafias de %s solo vivos %s: %d grafias" % (a, m["ref"], len(d["grafias_vivos"])))
    print("CIFRA parejas titulo-prefijo con el mismo autor %s: %d pares"
          % (m["ref"], len(m["prefijo_mismo_autor"])))


def main():
    refs = sys.argv[1:] or ["WORK"]
    for r in refs:
        imprimir(medir(r))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
