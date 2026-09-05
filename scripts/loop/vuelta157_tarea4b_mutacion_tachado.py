# -*- coding: utf-8 -*-
"""vuelta157_tarea4b_mutacion_tachado.py . TAREA 4.b DE LA VUELTA 157.

EL CASO POSITIVO POR MUTACION DEL LECTOR ENSANCHADO (adjudicacion 6.8 del acta
157). Prueba las TRES cosas que el encargo pide, y las tres sobre el LECTOR DE
VERDAD, importado de `scripts/loop/vuelta152_registro_de_citas_opc05.py`, no
sobre una copia del patron tecleada aqui:

  (A) CON EL LECTOR VIEJO LA FILA TACHADA DESAPARECE. Se tacha EN MEMORIA la
      celda de clase de la fila 97 (`D` pasa a `~~C~~ D`) y se exige que el par
      juran_rcca_metodo <-> viaje_diagnostico_remedial NO ESTE en lo que el
      patron viejo recoge.
  (B) CON EL LECTOR NUEVO LA FILA APARECE CON LA CLASE BUENA, o sea con la
      ULTIMA clase escrita en la celda, que es D.
  (C) EL CONTEO DE PARES DEL REGISTRO SALE IDENTICO ANTES Y DESPUES SOBRE EL
      FICHERO SIN TACHAR. Si se mueve, esto sale ROJO y el encargo manda parar:
      ensanchar el patron no puede cambiar lo que se lee de un fichero que
      todavia no tiene un solo tachado.

EL FICHERO DEL REPO NO SE TOCA. Todo pasa sobre el texto en memoria, que es la
unica forma de probar el lector viejo sin romper Gate 0 de verdad.

LA PRUEBA DE MUTACION DE ESTE MISMO CASO (regla del ejecutor, 29 ago 2026, EL
CASO ROJO SE PRUEBA POR MUTACION): con `--mutar` se le da la vuelta al valor
esperado de (A) (se exige que el lector VIEJO conserve la fila tachada) y esta
guarda tiene que CAER en ROJO con exit 1. Ninguno de los veredictos de aqui es
una constante literal: los tres salen de correr el lector.

--- CORRECCION DECLARADA (vuelta 163, TAREA 2; adjudicacion 6.8 del acta 162) ---

ESTE ARNES NACIO CADUCADO DENTRO DE SU PROPIO COMMIT, igual que el de la TAREA
1.a de la vuelta 162, y por la misma causa: SUS VALORES ESPERADOS ESTABAN
CLAVADOS. Medido con git: el fichero nace en `5ebac882`, que es EXACTAMENTE el
commit *"VUELTA 157, TAREA 4: EL LECTOR SE ENSANCHA Y LAS TRES FILAS RECIBEN SU
TACHADO"*, o sea el commit que TACHO las celdas. El arnes exigia que la fila 97
viniera con la celda LIMPIA (`| D |`) para poder tacharla en memoria, y su
propio commit se la dejo tachada (`| ~~C~~ D |`). Desde el dia siguiente sale
`ROJO PREVIO: la fila 97 no viene con la celda limpia esperada`, que es la
especie del banco 9: verde y mal, y despues rojo y mudo.

LO QUE SE ARREGLA, Y ES LA MISMA MEDICINA QUE LA TAREA 3 DE ESTA VUELTA: LOS
ESPERADOS SE COMPUTAN DEL ESTADO DEL DIA Y LO QUE SE PRUEBA ES EL DELTA.

  - LA FILA SUJETO SE ELIGE POR COMPUTO, no se teclea: la PRIMERA fila de
    lectura dirigida cuya celda de clase venga TACHADA hoy. Si hoy no hubiera
    ninguna tachada, se elige la primera limpia y se le tacha la celda EN
    MEMORIA: el delta es el mismo en los dos sentidos.
  - LOS DOS TEXTOS SE FABRICAN EN MEMORIA: `SIN TACHAR` normaliza TODAS las
    celdas tachadas del fichero a su ultima clase, y `TACHADO` es el que trae la
    fila sujeto con su tachado. Antes se usaba el fichero del repo como si fuera
    el texto limpio, y eso solo era cierto el dia anterior al tachado.
  - LA CLASE ESPERADA EN (B) NO ES `D`: es LA ULTIMA CLASE ESCRITA en la celda
    de la fila sujeto, leida de la celda. Un literal ahi es lo que caduco.

EL DELTA QUE PRUEBA, invariante al numero de fila y a la clase que toque: con la
celda tachada el lector VIEJO PIERDE la fila y el NUEVO la conserva con su
ultima clase; y sobre el texto SIN TACHAR los dos leen exactamente lo mismo.

EL FICHERO DEL REPO SIGUE SIN TOCARSE: todo pasa en memoria.

SUJETO CONGELADO (vuelta 180, TAREA 2.b): el texto de `docs/plan/LECTURAS_DIRIGIDAS.md`
ya NO se lee del fichero vivo. Se lee de un BLOB DE GIT CLAVADO por su commit y
se comprueba por su `sha256` declarado, con `sujeto_congelado_de_git.py`. Lo que
habia antes queda escrito aqui y no se borra: `io.open(LD).read()` sobre la ruta
viva, que es lo que hacia que este arnes se moviera con el fichero. El delta que
prueba es el mismo; lo que cambia es que ahora no puede cambiar solo.

USO:  python scripts/loop/vuelta157_tarea4b_mutacion_tachado.py
      python scripts/loop/vuelta157_tarea4b_mutacion_tachado.py --mutar
"""
import argparse
import importlib.util
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sujeto_congelado_de_git as SC   # noqa: E402

LECTOR = os.path.join(RAIZ, "scripts", "loop", "vuelta152_registro_de_citas_opc05.py")

# EL SUJETO, CONGELADO EN LA VUELTA 180 (TAREA 2.b; adjudicacion 7.8 del acta
# 179). Hasta hoy este arnes leia el fichero VIVO, y por eso su resultado se
# movia con el: la guarda del sujeto congelado lo cazaba como SUJETO VIVO. Ahora
# lee un BLOB DE GIT CLAVADO por su commit y comprobado por su sha256, asi que su
# resultado no depende de lo que el fichero vivo diga hoy.
RUTA_LD = "docs/plan/LECTURAS_DIRIGIDAS.md"
COMMIT_LD = "24bd395b0cde6f81780454bb110d4a4fbb7f3d6f"
SHA_LD = "dda1cdd67042c733765d801d9745a1ed3b653aca7afc38b8a872c056dd524813"

# LA FILA DE LA QUE NACIO ESTE ARNES, CONSERVADA COMO CONTRASTE Y NO COMO VARA.
# No se borra (EJECUTOR.md 8: una correccion que tapa lo que corrige no se puede
# auditar), pero YA NO DECIDE NADA: la fila sujeto se elige por computo.
PAR_97_HISTORICO = ("juran_rcca_metodo", "viaje_diagnostico_remedial")

# LA CELDA DE CLASE DE UNA FILA DE LECTURA DIRIGIDA, con su parte tachada y su
# clase vigente separadas. Es el mismo vocabulario del lector nuevo.
PATRON_CELDA = re.compile(
    r"(\|\s*([a-z0-9_]+)\s*<->\s*([a-z0-9_]+)\s*\|\s*)((?:~~[A-Z]+~~\s*)*)([A-Z]+)(\s*\|)")


def cargar_lector():
    """Importa el lector de verdad. `vuelta152_registro_de_citas_opc05.py` llama
    a `main()` al final del modulo, asi que se le tapa la salida y se le deja un
    `sys.argv` limpio: lo que interesa son sus funciones y sus dos patrones, no
    su informe."""
    spec = importlib.util.spec_from_file_location("lector_opc05", LECTOR)
    mod = importlib.util.module_from_spec(spec)
    argv, salida = sys.argv, sys.stdout
    sys.argv = [LECTOR]
    sys.stdout = io.StringIO()
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.argv, sys.stdout = argv, salida
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutar", action="store_true",
                    help="le da la vuelta al valor esperado de (A): tiene que salir ROJO")
    a = ap.parse_args()

    print("=" * 78)
    print("VUELTA 157, TAREA 4.b: CASO POSITIVO POR MUTACION DEL LECTOR ENSANCHADO")
    print("=" * 78)
    print("")

    mod = cargar_lector()
    N = mod.cargar("WORK")
    r = mod.hacer_resolver(N)
    print("  lector importado de: %s" % os.path.relpath(LECTOR, RAIZ).replace("\\", "/"))
    print("  patron VIEJO: %s" % mod.PATRON_FILA_LD_VIEJO.pattern[-64:])
    print("  patron NUEVO: %s" % mod.PATRON_FILA_LD.pattern[-64:])
    print("")

    texto = SC.texto_del_blob(COMMIT_LD, RUTA_LD, SHA_LD)
    print("  EL SUJETO VA CONGELADO Y SE COMPRUEBA, NO SE PROMETE")
    print("    blob clavado: %s:%s" % (COMMIT_LD[:12], RUTA_LD))
    print("    sha256 declarado y comprobado: %s" % SHA_LD)
    print("    bytes del blob (normalizado a LF): %d" % len(texto.encode("utf-8")))
    print("")
    celdas = [(m, m.group(2), m.group(3), m.group(4).strip(), m.group(5))
              for m in PATRON_CELDA.finditer(texto)]
    tachadas = [c for c in celdas if c[3]]
    print("  EL SUJETO SE ELIGE POR COMPUTO, NO SE TECLEA")
    print("    CIFRA celdas de clase de lectura dirigida en el fichero: %d" % len(celdas))
    print("    CIFRA de esas que vienen TACHADAS hoy: %d" % len(tachadas))
    if not celdas:
        print("ROJO PREVIO: el fichero no trae ninguna fila de lectura dirigida.")
        print("FIN")
        return 1

    # SIN TACHAR: todas las celdas normalizadas a su clase vigente. Antes se
    # usaba el fichero del repo como si fuera el texto limpio, y eso solo era
    # cierto el dia anterior al tachado.
    sin_tachar = PATRON_CELDA.sub(lambda m: m.group(1) + m.group(5) + m.group(6), texto)

    if tachadas:
        m, a_id, b_id, tach, vigente = tachadas[0]
        origen = "primera fila TACHADA del fichero de hoy"
        tachado = texto
    else:
        m, a_id, b_id, tach, vigente = celdas[0]
        origen = "primera fila LIMPIA, tachada EN MEMORIA (hoy no hay ninguna tachada)"
        tachado = texto[:m.start()] + m.group(1) + "~~%s~~ %s" % (vigente, vigente)             + m.group(6) + texto[m.end():]
    print("    SUJETO: %s <-> %s  | celda %r | %s"
          % (a_id, b_id, (tach + vigente).strip(), origen))
    print("    CLASE ESPERADA EN (B), LEIDA DE LA CELDA Y NO TECLEADA: %r" % vigente)
    print("    fila historica de la que nacio este arnes (contraste, no vara): %s <-> %s"
          % PAR_97_HISTORICO)
    print("")

    limpio_viejo = mod.citas_de_lectura_dirigida_de_texto(sin_tachar, r, mod.PATRON_FILA_LD_VIEJO)
    limpio_nuevo = mod.citas_de_lectura_dirigida_de_texto(sin_tachar, r, mod.PATRON_FILA_LD)
    tach_viejo = mod.citas_de_lectura_dirigida_de_texto(tachado, r, mod.PATRON_FILA_LD_VIEJO)
    tach_nuevo = mod.citas_de_lectura_dirigida_de_texto(tachado, r, mod.PATRON_FILA_LD)

    clave = tuple(sorted((r(a_id), r(b_id))))

    print("(C) EL CONTEO SOBRE EL TEXTO SIN TACHAR, QUE ES LO QUE NO SE PUEDE MOVER")
    print("    CIFRA pares que recoge el lector VIEJO: %d" % len(limpio_viejo))
    print("    CIFRA pares que recoge el lector NUEVO: %d" % len(limpio_nuevo))
    mismas_claves = set(limpio_viejo) == set(limpio_nuevo)
    mismas_clases = all(limpio_viejo[k]["clase"] == limpio_nuevo[k]["clase"]
                        for k in limpio_viejo if k in limpio_nuevo)
    print("    mismas claves: %s | mismas clases: %s" % (mismas_claves, mismas_clases))
    conteo_ok = (len(limpio_viejo) == len(limpio_nuevo)) and mismas_claves and mismas_clases
    print("    VEREDICTO (C): %s" % ("IDENTICO" if conteo_ok else "SE MOVIO"))
    print("")

    print("(A) EL LECTOR VIEJO SOBRE LA FILA SUJETO TACHADA")
    a_viejo_pierde = clave not in tach_viejo
    print("    CIFRA pares que recoge el lector VIEJO sobre el texto tachado: %d"
          % len(tach_viejo))
    print("    la fila sujeto esta en lo que recoge el VIEJO: %s" % (clave in tach_viejo))
    print("    coincidencias del patron VIEJO en la fila sujeto: %d"
          % (1 if clave in tach_viejo else 0))
    print("    VEREDICTO (A): %s" % ("LA FILA DESAPARECE" if a_viejo_pierde else "LA CONSERVA"))
    print("")

    print("(B) EL LECTOR NUEVO SOBRE LA MISMA FILA SUJETO TACHADA")
    clase_nueva = tach_nuevo.get(clave, {}).get("clase")
    b_ok = clave in tach_nuevo and clase_nueva == vigente
    print("    CIFRA pares que recoge el lector NUEVO sobre el texto tachado: %d"
          % len(tach_nuevo))
    print("    la fila sujeto esta en lo que recoge el NUEVO: %s" % (clave in tach_nuevo))
    print("    clase que le asigna (la ULTIMA escrita en la celda): %r" % clase_nueva)
    print("    VEREDICTO (B): %s" % ("APARECE CON LA CLASE BUENA" if b_ok else "NO APARECE BIEN"))
    print("")

    esperado_a = True
    if a.mutar:
        esperado_a = False
        print("  MUTACION ACTIVA: se le da la vuelta al valor esperado de (A). Ahora se")
        print("  exige que el lector VIEJO CONSERVE la fila tachada, que es falso, y este")
        print("  caso tiene que CAER. Si no cae, el caso no probaba nada.")
        print("")

    bien = (a_viejo_pierde == esperado_a) and b_ok and conteo_ok
    print("  (A) esperado %s, medido %s" % (esperado_a, a_viejo_pierde))
    print("  (B) esperado True, medido %s" % b_ok)
    print("  (C) esperado True, medido %s" % conteo_ok)
    print("")
    if bien:
        print("VERDE: el lector viejo pierde la fila tachada, el nuevo la recupera con")
        print("la clase %r leida de la celda, y el conteo sobre el texto sin tachar no se"
              % vigente)
        print("mueve.")
        print("FIN")
        return 0
    print("ROJO: alguna de las tres condiciones no se cumple.")
    print("FIN")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
