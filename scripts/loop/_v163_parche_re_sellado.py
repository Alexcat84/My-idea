# -*- coding: utf-8 -*-
"""_v163_parche_re_sellado.py . El parche de la TAREA 4.b sobre
verificar_re_sellado.py, escrito como fichero para que quede auditable lo que se
inserto y donde. Se corre una sola vez; es idempotente (si ya esta, no hace
nada)."""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(RAIZ, "scripts", "loop", "verificar_re_sellado.py")

BLOQUE = '''# --- ADJUDICACION 6.7 DEL ACTA 162 (3 sep 2026): EL AGUJERO POR CONSTRUCCION,
#     TAPADO (vuelta 163, TAREA 4.b) -----------------------------------------
#
# REGISTRO POR ADICION. NADA DE LO ESCRITO ARRIBA SE BORRA Y EL CAMINO VIEJO NO
# SE TOCA: sigue midiendo, exactamente igual, las salidas QUE EL REPORTE CITA
# contra el commit de su tarea.
#
# EL HECHO, MEDIDO (acta 162, seccion 5.4). La TAREA 3 de la vuelta 162 re sello
# `docs/loop/SALIDA_V135_2E_MUTACION_1.txt`, `_2` y `_3` con +2/-1 cada una en el
# commit `ab974bca`, legitimamente y como consecuencia mecanica de una guarda
# nueva, PERO SIN DECLARARLO. Esta guarda salio VERDE y NO PODIA VERLAS: solo
# mira lo que el reporte CITA, y a esas no las citaba nadie. No fue trampa del
# ejecutor; fue un agujero de la vara.
#
# LO QUE SE ANADE: un SEGUNDO CAMINO, independiente del primero. Contra EL
# COMMIT DE APERTURA DE LA VUELTA se listan TODAS las `docs/loop/SALIDA_*`
# MODIFICADAS (status `M`, no las nuevas: una salida que NACE no es un re
# sellado), y LA QUE NO ESTE NOMBRADA EN EL REPORTE SALE EN ROJO CON SU NOMBRE.
#
# POR QUE BASTA CON QUE ESTE NOMBRADA, Y NO SE PIDE AQUI UNA LINEA LITERAL:
# porque nombrarla LA CONVIERTE EN CITADA, y entonces EL CAMINO VIEJO la recoge
# y le exige su linea computada con su numstat y sus cifras movidas. Los dos
# caminos se componen en vez de pedir dos declaraciones distintas de lo mismo:
# el segundo DESCUBRE, el primero EXIGE LA FORMA.
#
# LA APERTURA NO SE TECLEA: se lee de git como el commit que ANADIO
# `docs/loop/SALIDA_V<N>_HEAD_APERTURA.txt`, que es la misma vara que usa
# `verificar_apertura_sellada.py`. Y `<N>` tampoco se teclea si no se pasa: se
# computa como el mayor `V<N>` con sello de apertura en el arbol.
#
# LA EXENCION POR CONSTRUCCION DE LA 6.8 DEL ACTA 158 VALE IGUAL AQUI, y por el
# mismo motivo: la salida de esta guarda y la del verificador de cifras las re
# escribe el commit que publica el reporte.
PATRON_SELLO_APERTURA = re.compile(r"^SALIDA_V(\\d+)_HEAD_APERTURA\\.txt$")


def vuelta_del_arbol():
    """El numero de vuelta MAYOR con sello de apertura en `docs/loop/`. No se
    teclea: se computa del propio directorio."""
    numeros = []
    for nombre in os.listdir(os.path.join(RAIZ, "docs", "loop")):
        m = PATRON_SELLO_APERTURA.match(nombre)
        if m:
            numeros.append(int(m.group(1)))
    return max(numeros) if numeros else None


def commit_de_apertura(vuelta):
    """El commit que ANADIO el sello de apertura de esa vuelta, leido de git."""
    if vuelta is None:
        return None
    return commit_de_su_tarea("docs/loop/SALIDA_V%d_HEAD_APERTURA.txt" % vuelta)


def salidas_modificadas_desde(apertura, hasta=None):
    """Las `docs/loop/SALIDA_*` con status `M` entre la apertura y EL ARBOL DE
    TRABAJO (o hasta `hasta`, que existe para que el caso por mutacion pueda
    apuntar a un par de commits historicos sin tocar nada).

    Se compara contra el arbol y no contra HEAD a proposito: esta guarda se
    corre ANTES del commit que publica el reporte, y mirar solo HEAD dejaria
    fuera justo lo que se acaba de re sellar."""
    if not apertura:
        return []
    args = ["diff", "--name-status", apertura]
    if hasta:
        args.append(hasta)
    args += ["--", "docs/loop/"]
    codigo, salida = git(*args)
    if codigo:
        return []
    fuera = []
    for linea in salida.splitlines():
        campos = linea.split("\\t")
        if len(campos) < 2 or not campos[0].startswith("M"):
            continue
        ruta = campos[-1].strip()
        base = os.path.basename(ruta)
        if not base.startswith("SALIDA_") or not base.endswith(".txt"):
            continue
        if es_exento(ruta):
            continue
        fuera.append(ruta)
    return sorted(set(fuera))


def no_declaradas(modificadas, texto):
    """Las modificadas cuyo NOMBRE no aparece en el reporte. Vive en su propia
    funcion para que el caso por mutacion ejerza ESTE codigo y no una copia."""
    return [r for r in modificadas if os.path.basename(r) not in texto]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reporte", default=REPORTE_POR_DEFECTO)
    ap.add_argument("--vuelta", type=int, default=None,
                    help="vuelta cuya apertura es la referencia del camino nuevo "
                         "(adjudicacion 6.7 del acta 162). Si no se pasa, se "
                         "computa la mayor del arbol.")
    a = ap.parse_args()
'''

VIEJO_MAIN = '''def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reporte", default=REPORTE_POR_DEFECTO)
    a = ap.parse_args()
'''

VIEJO_2 = '''    print("  CIFRA re selladas SIN declarar en el reporte: %d" % len(sin_declarar))
    print("")
    if sin_declarar:'''

NUEVO_2 = '''    print("  CIFRA re selladas SIN declarar en el reporte: %d" % len(sin_declarar))
    print("")

    # --- EL CAMINO NUEVO (adjudicacion 6.7 del acta 162). El viejo ya termino
    # arriba y no se toca: esto se SUMA.
    print("=" * 78)
    print("CAMINO NUEVO (adjudicacion 6.7 del acta 162): TODA docs/loop/SALIDA_*")
    print("MODIFICADA DESDE LA APERTURA DE LA VUELTA, LA CITE EL REPORTE O NO")
    print("=" * 78)
    vuelta = a.vuelta if a.vuelta is not None else vuelta_del_arbol()
    apertura = commit_de_apertura(vuelta)
    print("  vuelta tomada (%s): %s"
          % ("del argumento" if a.vuelta is not None else "computada del arbol", vuelta))
    print("  commit de apertura, leido de git --diff-filter=A y no tecleado: %s"
          % (apertura[:12] if apertura else "NO HALLADO"))
    if not apertura:
        print("  ROJO: sin commit de apertura este camino no puede medir nada, y")
        print("  callarlo seria el agujero que la 6.7 vino a tapar.")
        print("FIN")
        return 1
    modificadas = salidas_modificadas_desde(apertura)
    print("  CIFRA docs/loop/SALIDA_* MODIFICADAS desde la apertura: %d" % len(modificadas))
    for r in modificadas:
        print("      %s" % os.path.basename(r))
    faltan_nombre = no_declaradas(modificadas, texto)
    print("  CIFRA de esas que el reporte NO nombra: %d" % len(faltan_nombre))
    for r in faltan_nombre:
        print("      SIN DECLARAR: %s" % os.path.basename(r))
    print("  (una salida que NACE en esta vuelta no cuenta: nacer no es re sellar)")
    print("")

    if faltan_nombre:
        print("ROJO (camino nuevo): %d salida(s) sellada(s) cambiaron desde la apertura"
              % len(faltan_nombre))
        print("de la vuelta y el reporte NO LAS NOMBRA: %s"
              % ", ".join(os.path.basename(r) for r in faltan_nombre))
        print("Nombrarlas las devuelve al camino viejo, que les exigira su linea")
        print("computada con su numstat y sus cifras movidas.")
    if sin_declarar:'''

VIEJO_3 = '''        print("No se prohibe re sellar. Se prohibe re sellar EN SILENCIO.")
        print("FIN")
        return 1
    print("VERDE: ninguna salida sellada citada por el reporte cambio en silencio.")
    print("FIN")
    return 0'''

NUEVO_3 = '''        print("No se prohibe re sellar. Se prohibe re sellar EN SILENCIO.")
        print("FIN")
        return 1
    if faltan_nombre:
        print("No se prohibe re sellar. Se prohibe re sellar EN SILENCIO.")
        print("FIN")
        return 1
    print("VERDE: ninguna salida sellada citada por el reporte cambio en silencio, y")
    print("ninguna docs/loop/SALIDA_* modificada desde la apertura se quedo sin")
    print("nombrar.")
    print("FIN")
    return 0'''


def main():
    s = io.open(P, encoding="utf-8").read()
    if "CAMINO NUEVO (adjudicacion 6.7 del acta 162)" in s:
        print("YA ESTABA: el camino nuevo ya vive en verificar_re_sellado.py.")
        return 0
    for viejo in (VIEJO_MAIN, VIEJO_2, VIEJO_3):
        if viejo not in s:
            print("PARADA: no se halla el trozo que hay que sustituir:")
            print(viejo[:80])
            return 1
    s = s.replace(VIEJO_MAIN, BLOQUE)
    s = s.replace(VIEJO_2, NUEVO_2)
    s = s.replace(VIEJO_3, NUEVO_3)
    io.open(P, "w", encoding="utf-8", newline="\n").write(s)
    print("VERDE: camino nuevo insertado en scripts/loop/verificar_re_sellado.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
