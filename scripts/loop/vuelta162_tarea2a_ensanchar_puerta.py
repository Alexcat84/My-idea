# -*- coding: utf-8 -*-
r"""vuelta162_tarea2a_ensanchar_puerta.py . TAREA 2.a de la vuelta 162.

Aplica sobre scripts/loop/verificar_apertura_sellada.py la ADJUDICACION 6.5 DEL
ACTA 161: la puerta del corredor despues de una parada. El instrumento es un
parche escrito y corrido UNA vez, y queda como rastro (no se vuelve a correr:
sus anclas ya no estan). Todo lo que anade va comentado dentro de la guarda.
"""
import io

RUTA = "scripts/loop/verificar_apertura_sellada.py"

BLOQUE_FUNCIONES = r'''# --- ADJUDICACION 6.5 DEL ACTA 161 (3 sep 2026): LA PUERTA DEL CORREDOR TRAS UNA
# PARADA, QUE HASTA HOY ERA INALCANZABLE POR CONSTRUCCION ---------------------
#
# REGISTRO POR ADICION. Nada de lo escrito arriba se borra: el veredicto de las
# vueltas 156 a 161 se dio con la puerta tal como estaba, y taparlo impediria
# auditarlo.
#
# EL HECHO, MEDIDO Y NO ALEGADO (reporte de la vuelta 161, seccion 2.1; acta
# 161, seccion 6.5). La 6.8 del acta 155 fijo la vara: el encargo se lee DEL
# COMMIT DEL ACTA. Tras una PARADA, la seccion 4 de AUDITOR.md manda al auditor
# dejar `docs/loop/PROMPT_SIGUIENTE.md` VACIO y escribir `PARA_ALEXIS.md`. Las
# dos reglas juntas dejan a la vuelta que reanuda sin encargo del que leer
# rotulo: `git show ed234154:docs/loop/PROMPT_SIGUIENTE.md` no imprime nada, y
# esta guarda lo decia ella misma ("rotulo ... en ese encargo: NO"). Resultado
# medido: `--vuelta 161` ROJA por las diez salidas, con el commit de la DECISION
# DEL FUNDADOR (`d3482b11`) como unico intruso. La puerta no estaba cerrada por
# criterio: estaba cerrada POR CONSTRUCCION.
#
# QUIEN LA ENSANCHA Y POR QUE PUEDE. La regla que bloquea es la 6.8 del acta
# 155, adjudicacion DEL AUDITOR y no decision del fundador; por AUDITOR.md 2 le
# toca a el resolver el choque que ella misma creo con la seccion 4. El punto
# (ii) de la 6.8 pide que el encargo se lea de UN COMMIT y no del arbol de
# trabajo, para que el veredicto de la vuelta N sea el mismo dentro de diez
# vueltas; un commit anterior a la apertura cumple ese proposito igual que el
# del acta.
#
# LO QUE SE ADJUDICA:
#   (a) LA FIRMA DE LA PARADA, Y SOLO ELLA, ABRE ESTA PUERTA: el commit del acta
#       trae `PROMPT_SIGUIENTE.md` VACIO y `PARA_ALEXIS.md` ESCRITO. El ejecutor
#       no puede fabricarla porque el acta es del auditor.
#   (b) CON ESA FIRMA, el encargo se lee del PRIMER commit posterior al acta que
#       ESCRIBA `PROMPT_SIGUIENTE.md` dentro del corredor.
#   (c) SI HUBIERA MAS DE UN COMMIT ASI, ROJO. Dos portadores es ambiguo, y esta
#       casa prefiere el rojo a elegir por su cuenta.
#   (d) EL MECANISMO DEL ROTULO NO CAMBIA EN NADA: sin el literal
#       `HASHES ADMITIDOS EN EL CORREDOR DE ESTA VUELTA:` no entra nada, y un
#       hash citado de paso sigue sin entrar.
#   (e) EL PORTADOR DEL ENCARGO NO ES INTRUSO, Y ESTO ES LO QUE DE VERDAD
#       ENSANCHA LA PUERTA. Se dice con todas sus letras porque es la parte que
#       la letra de (b) sola NO da, y se dice ANTES de saber si acierta: medido
#       hoy, el encargo de la vuelta 161 (`d3482b11`) NO trae el rotulo, asi que
#       leerlo de ahi admite CERO hashes y `--vuelta 161` seguiria ROJA. El
#       portador queda fuera del censo de intrusos porque HACE EL PAPEL DEL
#       ACTA: es el commit que ABRE la vuelta, y el corredor siempre se midio
#       desde el commit que la abre (el rango es `acta..nacimiento`, con el acta
#       EXCLUIDA). Sin (e), la vara de aceptacion que el encargo de la vuelta
#       162 fija ("--vuelta 161 TIENE QUE DAR VERDE") es inalcanzable. QUEDA
#       MARCADO COMO DISCUTIBLE en el reporte de la vuelta 162.
#   (f) TODO LO DEMAS DEL CORREDOR SE SIGUE JUZGANDO IGUAL: sale del censo EL
#       PORTADOR, no el resto. Un commit del ejecutor delante de la apertura
#       sigue siendo ROJO, con firma de parada o sin ella.
#   (g) NINGUN VEREDICTO VIEJO SE MUEVE, y no se alega: se comprueba corriendo
#       la guarda vieja contra la nueva sobre las vueltas 156, 158, 159, 160,
#       161 y 162 (`docs/loop/SALIDA_V162_T2A_VIEJA.txt` contra
#       `docs/loop/SALIDA_V162_T2A_NUEVA.txt`, cotejadas por
#       `scripts/loop/vuelta162_tarea2a_cotejo_veredictos.py`).

RUTA_DEL_ENCARGO = "docs/loop/PROMPT_SIGUIENTE.md"
RUTA_DE_LA_PARADA = "docs/loop/PARA_ALEXIS.md"


def contenido_en_commit(commit, ruta):
    """El contenido de `ruta` en `commit`, o None si ese commit no lo trae.
    None y cadena vacia NO son lo mismo aqui, y esa diferencia es justo la que
    la firma de la parada necesita: el acta 160 SI trae el fichero del encargo,
    con cero bytes."""
    r = subprocess.run(["git", "show", "%s:%s" % (commit, ruta)],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8", "replace")


def es_firma_de_parada(texto_encargo, texto_para_alexis):
    """PURA A PROPOSITO (recibe los dos contenidos ya leidos, para que el caso
    por mutacion pueda fabricarlos en memoria sin tocar git ni el disco).

    LA FIRMA, LITERAL: el commit del acta TRAE `PROMPT_SIGUIENTE.md` y esta
    VACIO, y TRAE `PARA_ALEXIS.md` y esta ESCRITO. Un fichero AUSENTE no es un
    fichero vacio y no cuenta: se exige que el acta lo TRAIGA, que es lo que la
    adjudicacion dice con sus palabras."""
    encargo_vacio = texto_encargo is not None and texto_encargo.strip() == ""
    alexis_escrito = texto_para_alexis is not None and texto_para_alexis.strip() != ""
    return encargo_vacio and alexis_escrito


def portadores_del_encargo(corredor):
    """PURA A PROPOSITO: recibe el corredor ya leido, [(hash, asunto, [rutas])],
    y devuelve los commits que ESCRIBEN `PROMPT_SIGUIENTE.md`, en orden
    CRONOLOGICO (el corredor viene de `git log`, o sea del mas nuevo al mas
    viejo, y aqui se invierte para que el primero de la lista sea el PRIMERO
    POSTERIOR AL ACTA, que es el que la adjudicacion nombra).

    Lista de mas de uno significa ROJO por ambiguo; lo decide el llamador."""
    hallados = [h for h, _asunto, rutas in corredor if RUTA_DEL_ENCARGO in rutas]
    hallados.reverse()
    return hallados


def sin_el_portador(corredor, portador):
    """El corredor sin el commit que lleva el encargo. PURA. `portador` None
    devuelve el corredor tal cual, o sea que sin firma de parada no cambia
    nada."""
    if portador is None:
        return corredor, None
    resto, fuera = [], None
    for fila in corredor:
        if fila[0] == portador:
            fuera = fila
        else:
            resto.append(fila)
    return resto, fuera


PATRON_HASH = re.compile(r"\b[0-9a-f]{7,40}\b")
'''

ANCLA_FUNCIONES = 'PATRON_HASH = re.compile(r"\\b[0-9a-f]{7,40}\\b")\n'

# ---------------------------------------------------------------------------
ANCLA_ESTADO = """    texto_encargo = texto_del_encargo_en_el_acta(acta)
    admitidos, literales_citados, hay_rotulo = hashes_admitidos_por_el_encargo(
        texto_encargo, fallos=None)
    admitidos_del_corredor = {}
"""

NUEVO_ESTADO = """    texto_encargo = texto_del_encargo_en_el_acta(acta)
    admitidos, literales_citados, hay_rotulo = hashes_admitidos_por_el_encargo(
        texto_encargo, fallos=None)
    admitidos_del_corredor = {}
    # ADJUDICACION 6.5 DEL ACTA 161: LA FIRMA DE LA PARADA SE MIDE UNA SOLA VEZ,
    # del commit del acta, que es lo unico que hace falta para saber SI esta
    # puerta se abre. CON QUIEN se abre (el portador del encargo) depende del
    # corredor, y por eso se resuelve abajo, dentro de la rama que ya lo mide.
    hay_parada = es_firma_de_parada(
        contenido_en_commit(acta, RUTA_DEL_ENCARGO),
        contenido_en_commit(acta, RUTA_DE_LA_PARADA))
    fuente_del_encargo = acta          # por defecto, la vara de la 6.8: el acta
    portadores_vistos = {}             # nacido_en -> (hash, asunto, rutas)
"""

# ---------------------------------------------------------------------------
ANCLA_RAMA = """            else:
                intrusos, admitidos_aqui = intrusos_del_corredor(corredor, admitidos)
                if admitidos_aqui:
"""

NUEVA_RAMA = """            else:
                # ADJUDICACION 6.5 DEL ACTA 161. Con firma de parada, y SOLO con
                # ella, el encargo se lee del PRIMER commit del corredor que
                # escriba PROMPT_SIGUIENTE.md, y ese commit HACE EL PAPEL DEL
                # ACTA: sale del censo de intrusos porque es el que ABRE la
                # vuelta. Sin firma de parada, `hay_parada` es False y nada de
                # esto corre: el corredor se juzga exactamente como antes.
                corredor_juzgado = corredor
                if hay_parada:
                    portadores = portadores_del_encargo(corredor)
                    if len(portadores) > 1:
                        fallos.append(
                            "el acta %s trae la firma de una parada (encargo vacio y "
                            "PARA_ALEXIS escrito) y en el corredor hasta %s hay %d commits "
                            "que escriben %s (%s): AMBIGUO, no se elige por cuenta propia "
                            "(adjudicacion 6.5 del acta 161, punto c)"
                            % (acta[:8], nacido_en[:8], len(portadores), RUTA_DEL_ENCARGO,
                               ", ".join(h[:8] for h in portadores)))
                    elif len(portadores) == 1:
                        fuente_del_encargo = portadores[0]
                        texto_tras_parada = texto_del_encargo_en_el_acta(fuente_del_encargo)
                        (admitidos, literales_citados,
                         hay_rotulo) = hashes_admitidos_por_el_encargo(
                            texto_tras_parada, fallos=None)
                        corredor_juzgado, portador_fila = sin_el_portador(
                            corredor, fuente_del_encargo)
                        if portador_fila is not None:
                            portadores_vistos[nacido_en] = portador_fila
                intrusos, admitidos_aqui = intrusos_del_corredor(corredor_juzgado, admitidos)
                if admitidos_aqui:
"""

# ---------------------------------------------------------------------------
ANCLA_DECLARADOS = """                else:
                    declarados[nacido_en] = corredor
"""

NUEVO_DECLARADOS = """                else:
                    declarados[nacido_en] = corredor_juzgado
"""

# ---------------------------------------------------------------------------
ANCLA_RETORNO = """    return (fallos, detalle, declarados, admitidos_del_corredor, literales_citados,
            hay_rotulo, acta)
"""

NUEVO_RETORNO = """    return (fallos, detalle, declarados, admitidos_del_corredor, literales_citados,
            hay_rotulo, acta, hay_parada, fuente_del_encargo, portadores_vistos)
"""

# ---------------------------------------------------------------------------
ANCLA_VACIO = '''    def _vacio(acta_hallada):
        """La tupla de las salidas tempranas, con el `acta` que ya se sepa."""
        return ([], {}, {}, [], False, acta_hallada)
'''

NUEVO_VACIO = '''    def _vacio(acta_hallada):
        """La tupla de las salidas tempranas, con el `acta` que ya se sepa.

        ADJUDICACION 6.5 DEL ACTA 161: la tupla crece en tres huecos (firma de
        parada, fuente del encargo y portadores vistos) y las salidas tempranas
        los rellenan con lo que de verdad saben, que en las tres es "no se
        llego a medir". La linea vieja queda TACHADA Y LEGIBLE porque el
        veredicto de las vueltas 159 a 161 se dio con ella:
            ~~return ([], {}, {}, [], False, acta_hallada)~~
        """
        return ([], {}, {}, [], False, acta_hallada, False, acta_hallada, {})
'''

# ---------------------------------------------------------------------------
ANCLA_MAIN = """    (fallos, detalle, declarados, admitidos_corredor, literales,
     hay_rotulo, acta) = verificar(a.vuelta)
    # LA PUERTA HABLA SIEMPRE, salga verde o rojo (banco 9, fallar ruidoso): se
    # dice DE DONDE se leyo el encargo, SI traia el rotulo y QUE admitio.
    print("PUERTA DEL CORREDOR (adjudicacion 6.8 del acta 155): el encargo se lee del "
          "COMMIT DEL ACTA %s, no del arbol de trabajo." % (acta[:8] if acta else "(no hallado)"))
"""

NUEVO_MAIN = """    (fallos, detalle, declarados, admitidos_corredor, literales,
     hay_rotulo, acta, hay_parada, fuente_encargo, portadores) = verificar(a.vuelta)
    # LA PUERTA HABLA SIEMPRE, salga verde o rojo (banco 9, fallar ruidoso): se
    # dice DE DONDE se leyo el encargo, SI traia el rotulo y QUE admitio.
    if hay_parada:
        print("FIRMA DE PARADA EN EL ACTA %s (adjudicacion 6.5 del acta 161): el acta trae "
              "%s VACIO y %s ESCRITO."
              % (acta[:8] if acta else "(no hallado)", RUTA_DEL_ENCARGO, RUTA_DE_LA_PARADA))
    if fuente_encargo and acta and fuente_encargo != acta:
        print("PUERTA DEL CORREDOR (adjudicacion 6.5 del acta 161): el encargo se lee del "
              "COMMIT %s, PORTADOR DEL ENCARGO tras la parada, y no del acta %s, que lo trae "
              "vacio. Sigue siendo UN COMMIT y no el arbol de trabajo."
              % (fuente_encargo[:8], acta[:8]))
    else:
        print("PUERTA DEL CORREDOR (adjudicacion 6.8 del acta 155): el encargo se lee del "
              "COMMIT DEL ACTA %s, no del arbol de trabajo." % (acta[:8] if acta else "(no hallado)"))
"""

# ---------------------------------------------------------------------------
ANCLA_PORTADOR_IMPRESO = """    for nacido_en, adms in sorted(admitidos_corredor.items()):
"""

NUEVO_PORTADOR_IMPRESO = """    # EL PORTADOR NO SE CALLA NUNCA (banco 9): si un commit salio del censo de
    # intrusos por ser el que trae el encargo, se dice cual, que toca y ante que
    # apertura. Un commit fuera del censo en silencio seria peor que el rojo.
    for nacido_en, fila in sorted(portadores.items()):
        h, asunto, rutas = fila
        print("   PORTADOR DEL ENCARGO TRAS LA PARADA, fuera del censo de intrusos por la "
              "adjudicacion 6.5 del acta 161 (hace el papel del acta: es el commit que ABRE "
              "la vuelta): %s ('%s') toca %d ruta(s) (%s), delante de la apertura nacida en %s"
              % (h[:8], asunto[:70], len(rutas), ", ".join(rutas), nacido_en[:8]))
    for nacido_en, adms in sorted(admitidos_corredor.items()):
"""

PARCHES = [
    ("funciones nuevas", ANCLA_FUNCIONES, BLOQUE_FUNCIONES),
    ("estado de la firma", ANCLA_ESTADO, NUEVO_ESTADO),
    ("rama del corredor", ANCLA_RAMA, NUEVA_RAMA),
    ("corredor declarado", ANCLA_DECLARADOS, NUEVO_DECLARADOS),
    ("tupla de retorno", ANCLA_RETORNO, NUEVO_RETORNO),
    ("tupla vacia", ANCLA_VACIO, NUEVO_VACIO),
    ("cabecera de main", ANCLA_MAIN, NUEVO_MAIN),
    ("impresion del portador", ANCLA_PORTADOR_IMPRESO, NUEVO_PORTADOR_IMPRESO),
]


def main():
    s = io.open(RUTA, encoding="utf-8").read()
    for nombre, ancla, nuevo in PARCHES:
        n = s.count(ancla)
        if n != 1:
            raise SystemExit("ROJO: el ancla %r aparece %d veces (se esperaba 1)" % (nombre, n))
        s = s.replace(ancla, nuevo, 1)
        print("  aplicado: %s" % nombre)
    io.open(RUTA, "w", encoding="utf-8", newline="\n").write(s)
    print("VERDE: %d parches aplicados sobre %s" % (len(PARCHES), RUTA))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
