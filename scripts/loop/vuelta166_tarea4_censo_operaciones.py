# -*- coding: utf-8 -*-
r"""vuelta166_tarea4_censo_operaciones.py . TAREA 4 de la vuelta 166.

EL MAPA REAL DEL ULTIMO TRAMO, Y ES LA CORRECCION DE LA CAIDA 1 DEL AUDITOR
(adjudicacion 5.13 del acta 165).

QUE MIDE. El reparto de `docs/plan/OPERACIONES.jsonl` POR ESTADO y POR FASE, y
cuantas de las que quedan sin hacer NO tienen dependencias declaradas.

ES UN CENSO, NO UN PASE. Este instrumento NO CAMBIA NINGUN ESTADO y no escribe
en `docs/plan/OPERACIONES.jsonl`: solo lee e imprime. La letra del encargo es
literal: *"NO CAMBIES NINGUN ESTADO EN ESTA TAREA: es un censo, no un pase."*

POR QUE NACE. El acta 164, adjudicacion 6.10, publico que de las 71 operaciones
**67 estaban en HECHA y CUATRO en LISTA**, y con esa cifra dibujo el mapa del
"ultimo tramo de la fase III". El acta 165 la declara FALSA en su caida 1 y da
29 y 42. AQUI SE MIDE DE NUEVO, con instrumento propio del ejecutor, y MANDA
ESTA MEDICION: la cifra del acta va como CONTRASTE y si difiere se declara.

Y SE MIDE SOBRE DOS ARBOLES, no sobre uno: el de HOY y el del propio acta 164
(`2c00a1c0`). Si las dos dan lo mismo, la cifra del acta 164 ya era falsa el dia
que se escribio y no es deriva del tiempo; si dan distinto, es deriva y se dice.
Esa distincion NO se hereda del acta: se mide.

TAMBIEN CUENTA LO QUE LA CAIDA 1 NOMBRA EN SU SEGUNDA MITAD: la frase de que
`OP-L-01` era la unica de las que quedan sin dependencias declaradas.

USO:  python scripts/loop/vuelta166_tarea4_censo_operaciones.py
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REL = "docs/plan/OPERACIONES.jsonl"
OPS = os.path.join(RAIZ, REL.replace("/", os.sep))
ARBOL_ACTA_164 = "2c00a1c0"

# EL CONTRASTE, COPIADO DEL ACTA Y MARCADO COMO CONTRASTE, NUNCA COMO FUENTE.
CONTRASTE_ACTA_164 = ("acta 164, adjudicacion 6.10", 67, 4)
CONTRASTE_ACTA_165 = ("acta 165, caida 1", 29, 42)
CONTRASTE_ENCARGO = {
    "00_CODIGO": (6, 1), "01_FUENTES": (7, 0), "02_DESTEJIDOS": (9, 0),
    "03_FUSIONES": (10, 6), "04_ENLACES": (4, 6), "05_SANEO": (0, 10),
    "06_MESAS": (0, 5), "07_ADUANA": (2, 0), "08_VERIFICACION": (0, 1),
    "09_LECTURAS_DIRIGIDAS": (3, 0), "10_INVENTARIO": (1, 0),
}


def fichas_de_texto(texto):
    return [json.loads(l) for l in texto.split("\n") if l.strip()]


def fichas_de_hoy():
    return fichas_de_texto(io.open(OPS, encoding="utf-8").read())


def fichas_de_git(arbol):
    r = subprocess.run(["git", "show", "%s:%s" % (arbol, REL)],
                       capture_output=True, cwd=RAIZ)
    if r.returncode != 0:
        return None
    return fichas_de_texto(r.stdout.decode("utf-8", "replace"))


def reparto(fichas):
    """(por_estado, por_fase, orden_de_fases). SIN CIFRA TECLEADA."""
    por_estado, por_fase = {}, {}
    fases = []
    for f in fichas:
        e, fa = f["estado"], f["fase"]
        por_estado[e] = por_estado.get(e, 0) + 1
        if fa not in por_fase:
            por_fase[fa] = {}
            fases.append(fa)
        por_fase[fa][e] = por_fase[fa].get(e, 0) + 1
    return por_estado, por_fase, sorted(fases)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 166, TAREA 4: EL CENSO DE OPERACIONES, POR ESTADO Y POR FASE")
    print("=" * 78)
    print("")
    print("ES UN CENSO Y NO UN PASE: este instrumento no escribe en")
    print("docs/plan/OPERACIONES.jsonl y no cambia ningun estado.")
    print("")

    hoy = fichas_de_hoy()
    print("A) EL FICHERO DE HOY")
    print("   %s" % REL)
    print("   CIFRA operaciones: %d" % len(hoy))
    est, fase, fases = reparto(hoy)
    estados = sorted(est)
    for e in estados:
        print("   CIFRA en %-8s %d" % (e + ":", est[e]))
    print("   la suma de los estados es el total: %s"
          % (sum(est.values()) == len(hoy)))
    print("")

    print("B) EL REPARTO POR FASE, ENTERO Y SIN RECORTAR")
    ancho = max(len(f) for f in fases)
    cab = "   %-*s | %s | total" % (ancho, "fase", " | ".join(
        "%-8s" % e for e in estados))
    print(cab)
    print("   " + "-" * (len(cab) - 3))
    for f in fases:
        fila = fase[f]
        print("   %-*s | %s | %d"
              % (ancho, f, " | ".join("%-8d" % fila.get(e, 0) for e in estados),
                 sum(fila.values())))
    print("   " + "-" * (len(cab) - 3))
    print("   %-*s | %s | %d"
          % (ancho, "TOTAL", " | ".join("%-8d" % est[e] for e in estados),
             sum(est.values())))
    print("   CIFRA fases distintas: %d" % len(fases))
    print("")

    print("C) EL MISMO CONTEO SOBRE EL ARBOL DEL ACTA 164, PARA SEPARAR")
    print("   UNA CIFRA FALSA DE UNA DERIVA DEL TIEMPO")
    viejo = fichas_de_git(ARBOL_ACTA_164)
    if viejo is None:
        print("   PARADA: no se pudo leer %s en %s." % (REL, ARBOL_ACTA_164))
        return 1
    est_v, _fv, _fs = reparto(viejo)
    print("   arbol %s (acta 164): %d operaciones" % (ARBOL_ACTA_164, len(viejo)))
    for e in sorted(est_v):
        print("      CIFRA en %-8s %d" % (e + ":", est_v[e]))
    igual = (est == est_v)
    print("   el reparto de HOY y el del arbol del acta 164 coinciden: %s" % igual)
    if igual:
        print("   VEREDICTO: la cifra del acta 164 NO es deriva del tiempo. Ya era")
        print("   falsa el dia que se escribio, y esto lo mide el ejecutor, no lo")
        print("   copia del acta 165.")
    else:
        print("   VEREDICTO: hay deriva entre los dos arboles y se declara sin")
        print("   resolverla copiando.")
    print("")

    print("D) LOS TRES CONTRASTES, CON SU FUENTE Y MARCADOS COMO CONTRASTE")
    sin_hacer = [e for e in estados if e != "HECHA"]
    n_hecha = est.get("HECHA", 0)
    n_resto = sum(est[e] for e in sin_hacer)
    for nombre, h, l in (CONTRASTE_ACTA_164, CONTRASTE_ACTA_165):
        print("   %-28s dice HECHA %d y no HECHA %d | mi medicion: %d y %d | %s"
              % (nombre, h, l, n_hecha, n_resto,
                 "COINCIDE" if (h, l) == (n_hecha, n_resto) else "DIFIERE"))
    print("")
    print("   EL CONTRASTE POR FASE QUE EL ENCARGO TRAE (LISTA/HECHA):")
    difieren = []
    for f in fases:
        mio = (fase[f].get("LISTA", 0), fase[f].get("HECHA", 0))
        suyo = CONTRASTE_ENCARGO.get(f)
        marca = "COINCIDE" if suyo == mio else "DIFIERE"
        if suyo != mio:
            difieren.append(f)
        print("      %-24s encargo %-8s | mio %-8s | %s"
              % (f, str(suyo), str(mio), marca))
    print("   CIFRA fases en que mi medicion DIFIERE del encargo: %d (%s)"
          % (len(difieren), ", ".join(difieren) or "ninguna"))
    print("   MANDA MI MEDICION. Si alguna difiere, queda declarada arriba.")
    print("")
    print("E) LAS QUE NO ESTAN HECHAS Y NO TIENEN DEPENDENCIAS DECLARADAS")
    print("   LA SEGUNDA MITAD DE LA CAIDA 1: el acta 164 dijo que OP-L-01 era la")
    print("   UNICA sin dependencias declaradas. Aqui se cuenta.")
    pendientes = [f for f in hoy if f["estado"] != "HECHA"]
    sin_dep = [f for f in pendientes if not (f.get("depende_de") or [])]
    con_dep = [f for f in pendientes if (f.get("depende_de") or [])]
    print("   CIFRA operaciones no HECHA: %d" % len(pendientes))
    print("   CIFRA de esas, SIN dependencias declaradas: %d" % len(sin_dep))
    print("   CIFRA de esas, CON dependencias declaradas: %d" % len(con_dep))
    print("   la suma cuadra: %s" % (len(sin_dep) + len(con_dep) == len(pendientes)))
    print("   LAS SIN DEPENDENCIAS, NOMBRADAS UNA POR UNA Y NO RESUMIDAS:")
    for f in sin_dep:
        print("      %-22s %-24s %-8s tipo %s"
              % (f["id_op"], f["fase"], f["estado"], f["tipo"][:28]))
    print("   VEREDICTO SOBRE LA FRASE DEL ACTA 164: OP-L-01 %s"
          % ("ES la unica sin dependencias declaradas"
             if len(sin_dep) == 1 and sin_dep[0]["id_op"] == "OP-L-01"
             else "NO es la unica: son %d, y van nombradas arriba" % len(sin_dep)))
    print("")

    print("F) Y LAS QUE SI TIENEN DEPENDENCIAS, CON SU CUENTA DE DEPENDENCIAS")
    print("   NO SE ADJUDICA SI ESTAN LIBRES O NO: se cuenta cuantas de sus")
    print("   dependencias declaradas estan HOY en HECHA, y ya. Decidir si una")
    print("   operacion 'puede correr' es una lectura, no un conteo.")
    estado_de = {f["id_op"]: f["estado"] for f in hoy}
    libres, trabadas, rotas = [], [], []
    for f in sorted(con_dep, key=lambda x: x["id_op"]):
        deps = f["depende_de"]
        hechas = [d for d in deps if estado_de.get(d) == "HECHA"]
        ausentes = [d for d in deps if d not in estado_de]
        if ausentes:
            rotas.append((f["id_op"], ausentes))
        if len(hechas) == len(deps):
            libres.append(f["id_op"])
        else:
            trabadas.append(f["id_op"])
        print("      %-22s %-24s deps %d, en HECHA %d%s"
              % (f["id_op"], f["fase"], len(deps), len(hechas),
                 ", NOMBRADAS Y NO EN EL FICHERO: %s" % ", ".join(ausentes)
                 if ausentes else ""))
    print("   CIFRA con TODAS sus dependencias en HECHA: %d" % len(libres))
    print("   CIFRA con alguna dependencia sin HECHA: %d" % len(trabadas))
    print("   CIFRA con alguna dependencia que NO existe en el fichero: %d"
          % len(rotas))
    print("")

    print("G) EL RESUMEN QUE EL REPORTE PUBLICA, PARA QUE NO SE TECLEE")
    print("   CIFRA operaciones: %d" % len(hoy))
    for e in estados:
        print("   CIFRA %s: %d" % (e, est[e]))
    print("   CIFRA no HECHA sin dependencias declaradas: %d" % len(sin_dep))
    print("   CIFRA no HECHA con todas sus dependencias en HECHA: %d" % len(libres))
    print("   CIFRA fases: %d" % len(fases))
    print("")
    print("H) LO QUE ESTA TAREA NO HIZO, DICHO ANTES DE QUE SE LEA COMO HECHO")
    print("   NINGUN ESTADO SE CAMBIA. Ninguna operacion se abre, se cierra ni se")
    print("   remite. Y NO SE DECLARA CUAL ES 'EL ULTIMO TRAMO': el acta 164 lo")
    print("   dibujo desde una cifra falsa, y dibujarlo otra vez desde la cifra")
    print("   buena seguiria siendo una decision de alcance que nadie encargo.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
