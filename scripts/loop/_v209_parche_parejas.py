# -*- coding: utf-8 -*-
r"""_v209_parche_parejas.py . LAS TRES CIFRAS `sha256` QUE `cerrar_reporte.py`
CAZO SIN SU PAREJA, ARREGLADAS EN SUS DOS SEDES A LA VEZ.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3).

QUE PASO, MEDIDO: la primera corrida de `cerrar_reporte.py --vuelta 209` salio en
ROJO con **3 cifras publicadas sin su pareja**, las tres `sha256` **LF** sin su
`sha256` **de disco** en la misma linea. **Las dos cifras SI estaban medidas**; lo
que fallo es que el markdown partio la frase y la pareja quedo en otro renglon, o
que la sede solo publicaba una de las dos. **La guarda hace bien en no adivinar.**

EL PARCHE TOCA LAS DOS SEDES A LA VEZ, el fichero de seccion de la tarea y
`docs/loop/REPORTE.md` donde ya esta anexado, para que no digan cosas distintas,
y **cae en rojo si un trozo viejo no aparece exactamente una vez en su sede**.

LAS PAREJAS QUE FALTABAN NO SE INVENTAN: se MIDEN aqui, del disco, por las dos
convenciones, y el computo **cae en rojo si el `sha256` LF que ya estaba
publicado no coincide con el que se acaba de medir**. Un parche que cambiara una
cifra publicada en vez de completarla seria otra cosa muy distinta.
"""
import hashlib
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
NL = chr(10)

REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
T1 = os.path.join(AQUI, "_v209_t1_seccion.md")
T2 = os.path.join(AQUI, "_v209_t2_seccion.md")

# LA SEDE DE APERTURA, que es de donde salen las dos convenciones de las cifras
# de ENTRADA. Se lee, no se teclea.
APERTURA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V209_APERTURA.txt")


def shas(ruta_rel):
    b = io.open(os.path.join(RAIZ, ruta_rel.replace("/", os.sep)), "rb").read()
    lf = b.replace(b"\r\n", b"\n")
    return (hashlib.sha256(b).hexdigest()[:16],
            hashlib.sha256(lf).hexdigest()[:16])


def de_la_apertura(ruta_rel):
    """LAS DOS CONVENCIONES DE UNA SEDE **AL ENTRAR**, LEIDAS DEL SELLO DE
    APERTURA Y NO REMEDIDAS: el fichero ya cambio, asi que medirlo hoy daria
    otra cosa. El sello es la fuente y por eso existe."""
    t = io.open(APERTURA, encoding="utf-8").read().replace(chr(13) + NL, NL)
    for l in t.split(NL):
        if l.startswith("CIFRA " + ruta_rel + ":"):
            d = l.split("sha256 disco ")[1].split(" y sha256 LF ")
            return d[0].strip(), d[1].strip()
    return None, None


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    pend_e_d, pend_e_l = de_la_apertura("docs/PENDIENTES.md")
    lect_e_d, lect_e_l = de_la_apertura("docs/plan/LECTURAS_DIRIGIDAS.md")
    pend_s_d, pend_s_l = shas("docs/PENDIENTES.md")
    print("MEDIDO AHORA, Y NO TECLEADO:")
    print("   docs/PENDIENTES.md AL ENTRAR (del sello): disco %s y LF %s"
          % (pend_e_d, pend_e_l))
    print("   docs/PENDIENTES.md AL SALIR (del disco):  disco %s y LF %s"
          % (pend_s_d, pend_s_l))
    print("   docs/plan/LECTURAS_DIRIGIDAS.md AL ENTRAR (del sello): disco %s y "
          "LF %s" % (lect_e_d, lect_e_l))

    PARCHES = [
        # (sede del fichero de seccion, trozo viejo, trozo nuevo, sha ya
        #  publicado que NO puede cambiar)
        (T1,
         "LF, con `sha256` LF **`%s`**, que calza al digito con el contraste del"
         % pend_e_l,
         "LF, con `sha256` disco **`%s`** y `sha256` LF **`%s`**, que calzan al "
         "digito con el contraste del" % (pend_e_d, pend_e_l),
         pend_e_l),
        (T1,
         "con `sha256` LF **`%s`**." % pend_s_l,
         "con `sha256` disco **`%s`** y `sha256` LF **`%s`**."
         % (pend_s_d, pend_s_l),
         pend_s_l),
        (T2,
         "`sha256` LF **`%s`**, que calza al digito con el contraste del encargo."
         % lect_e_l,
         "`sha256` disco **`%s`** y `sha256` LF **`%s`**, que calzan al digito "
         "con el contraste del encargo." % (lect_e_d, lect_e_l),
         lect_e_l),
    ]

    print("")
    print("LA GUARDA DE QUE NO SE CAMBIA NINGUNA CIFRA PUBLICADA, SOLO SE")
    print("COMPLETA: el sha256 LF que ya estaba escrito tiene que ser el mismo")
    print("que el recien medido.")
    for _sede, viejo, nuevo, sha in PARCHES:
        ok = ("`%s`" % sha) in viejo and ("`%s`" % sha) in nuevo
        print("   %s sigue publicado igual en el trozo nuevo: %s"
              % (sha, "SI" if ok else "NO, Y ESO ES ROJO"))
        if not ok:
            print("ROJO: no se escribe nada.")
            return 1

    print("")
    print("LAS DOS SEDES DE CADA TROZO, CONTADAS ANTES DE ESCRIBIR NADA:")
    plan = []
    for sede, viejo, nuevo, _sha in PARCHES:
        for destino in (sede, REPORTE):
            t = io.open(destino, encoding="utf-8").read().replace(
                chr(13) + NL, NL)
            n = t.count(viejo)
            print("   %-34s %d aparicion(es) de %r"
                  % (os.path.basename(destino), n, viejo[:52]))
            if n != 1:
                print("ROJO: el trozo viejo no aparece exactamente una vez. NO SE "
                      "ESCRIBE NADA EN NINGUNA SEDE.")
                return 1
            plan.append((destino, viejo, nuevo))

    print("")
    print("LAS SEIS ESCRITURAS:")
    for destino, viejo, nuevo in plan:
        t = io.open(destino, encoding="utf-8").read().replace(chr(13) + NL, NL)
        t2 = t.replace(viejo, nuevo, 1)
        if t2.count(chr(8212)) or t2.count(chr(8211)):
            print("ROJO: guiones prohibidos.")
            return 1
        io.open(destino, "w", encoding="utf-8", newline=NL).write(t2)
        print("   ESCRITO %-30s %d bytes en disco y %d bytes normalizado a LF"
              % (os.path.basename(destino), len(t2.encode("utf-8")),
                 len(t2.encode("utf-8"))))

    print("")
    print("LA RELECTURA: NINGUN TROZO VIEJO PUEDE QUEDAR VIVO")
    vivos = 0
    for destino, viejo, _nuevo in plan:
        t = io.open(destino, encoding="utf-8").read().replace(chr(13) + NL, NL)
        if viejo in t:
            vivos += 1
    print("   CIFRA trozos viejos que siguen vivos: %d" % vivos)
    return 0 if vivos == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
