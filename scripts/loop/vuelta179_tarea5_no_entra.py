# -*- coding: utf-8 -*-
r"""vuelta179_tarea5_no_entra.py . LO QUE NO ENTRA EN ESTA VUELTA Y NO SE PIERDE,
MEDIDO UNA A UNA.

TAREA 5 de la vuelta 179. SOLO LECTURA: no toca ninguna de las cinco.

POR QUE SE MIDE Y NO SOLO SE NOMBRA (`EJECUTOR.md` 1, del 5 sep 2026, LA RUTA QUE
PROMETE PRUEBA ES CIFRA): una ruta publicada como evidencia cuenta como CIFRA
PUBLICADA en su sede, y si apunta a un fichero inexistente o de CERO BYTES es
CAIDA DE CIFRA. Nombrar cinco pendientes sin comprobar que sus sedes existen es
prometer cinco pruebas sin mirar ninguna.

LAS CINCO SON LAS DEL ENCARGO Y NO SE ELIGEN AQUI. Cada una trae su sede, la
aguja que la localiza dentro de esa sede, y sus bytes por las DOS convenciones
mientras la del fundador no este fijada (que es, ella misma, la quinta).

USO:
  python scripts/loop/vuelta179_tarea5_no_entra.py
"""
import io
import os
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# (numero, nombre, sede, aguja que la localiza dentro de la sede)
LAS_CINCO = [
    (1, "LA SEGUNDA SEDE DE LA CLAUSULA 4.4",
     "docs/loop/reportes/REPORTE_V172.md", "4.4"),
    (2, "EL DOCSTRING DEL PASO 0, QUE HABLA DE LA VUELTA ANTERIOR",
     # LA AGUJA SE CORRIGIO EN ESTA MISMA CORRIDA. La primera version buscaba
     # "VUELTA ANTERIOR" en mayusculas y no aparecia; el docstring lo dice en
     # minusculas, "la vuelta anterior", en su linea 25. El instrumento salio en
     # ROJO nombrando la aguja que fallaba, que es lo que se le pide.
     "scripts/loop/paso0_archivar_anterior.py", "vuelta anterior"),
    (3, "LA GUARDA QUE FALTA EN LA DEPENDENCIA DEL D.4 DE LA 174",
     "scripts/loop/vuelta179_esqueleto_reporte.py", "CLON DECLARADO"),
    (4, "EL GRANO DEL TOPE DE 10 MINUTOS",
     "scripts/loop/verificar_mutaciones_viejas.py", "10 minutos"),
    (5, "LA CONVENCION DE BYTES, QUE ES DEL FUNDADOR",
     "docs/loop/AUDITOR.md", "bytes"),
]


def bytes_de_git(ruta):
    r = subprocess.run(["git", "cat-file", "-s", "HEAD:" + ruta],
                       cwd=RAIZ, capture_output=True)
    o = r.stdout.decode("utf-8", errors="replace").strip()
    return int(o) if r.returncode == 0 and o.isdigit() else None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    p("=" * 78)
    p("LO QUE NO ENTRA Y NO SE PIERDE (vuelta 179, TAREA 5)")
    p("=" * 78)
    p("")
    p("NINGUNA DE LAS CINCO SE TOCA AQUI. Se mide su sede para que la promesa de")
    p("prueba no sea una ruta que no existe.")
    p("")

    filas = []
    rojos = []
    for n, nombre, sede, aguja in LAS_CINCO:
        ruta = os.path.join(RAIZ, sede.replace("/", os.sep))
        existe = os.path.exists(ruta)
        disco = os.path.getsize(ruta) if existe else -1
        texto = io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL) \
            if existe else ""
        lf = len(texto.encode("utf-8"))
        g = bytes_de_git(sede)
        golpes = [i for i, l in enumerate(texto.split(NL), 1) if aguja in l]
        p("%d. %s" % (n, nombre))
        p("   sede: %s" % sede)
        p("   existe: %s" % ("SI" if existe else "NO"))
        p("   CIFRA bytes en disco: %s | bytes normalizados a LF: %s | bytes en git: %s"
          % (disco if existe else "(no existe)", lf if existe else "(no existe)",
             g if g is not None else "NO ESTA EN HEAD"))
        p("   aguja: %r | CIFRA lineas de la sede que la traen: %d" % (aguja, len(golpes)))
        for i in golpes[:3]:
            p("      LINEA %d: %s" % (i, texto.split(NL)[i - 1].strip()[:110]))
        if not existe:
            rojos.append("la sede de la %d NO EXISTE: %s" % (n, sede))
        elif disco == 0:
            rojos.append("la sede de la %d mide CERO BYTES: %s" % (n, sede))
        elif not golpes:
            rojos.append("la aguja %r de la %d no aparece en su sede %s"
                         % (aguja, n, sede))
        p("")
        filas.append((n, existe, disco, lf, g, len(golpes)))

    p("LA TABLA, PARA PEGARLA ENTERA")
    p("| que no entra | sede | existe | bytes en disco | bytes en LF | lineas que la traen |")
    p("|---|---|---|---:|---:|---:|")
    for (n, nombre, sede, _a), (_n, existe, disco, lf, _g, golpes) in zip(LAS_CINCO, filas):
        p("| %d. %s | `%s` | %s | %d | %d | %d |"
          % (n, nombre.split(",")[0][:52], sede, "SI" if existe else "**NO**",
             max(disco, 0), lf, golpes))
    p("")
    p("CIFRA de las cinco cuya sede EXISTE: %d" % sum(1 for f in filas if f[1]))
    p("CIFRA de las cinco cuya sede mide CERO BYTES: %d"
      % sum(1 for f in filas if f[1] and f[2] == 0))
    p("CIFRA de las cinco cuya aguja NO aparece en su sede: %d"
      % sum(1 for f in filas if f[5] == 0))
    p("")

    if rojos:
        p("ROJO, %d motivo(s):" % len(rojos))
        for r in rojos:
            p("   " + r)
        p("FIN")
        return 1
    p("VERDE: las cinco tienen sede, ninguna mide cero bytes y las cinco agujas")
    p("aparecen. Ninguna se toco.")
    p("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
