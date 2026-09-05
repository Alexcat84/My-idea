# -*- coding: utf-8 -*-
"""verificar_mutaciones_viejas.py . LAS MUTACIONES VIEJAS, EN EL CICLO DE
CIERRE DE CADA VUELTA, Y ANCLA PERDIDA CUENTA COMO ROJO.

LA NOMINA VIVE EN `VIEJAS` Y CRECE: nacio con CUATRO, en la vuelta 140 paso a
CINCO con `vuelta139_2b_mutaciones.py` (cuyo bloque (iii) tenia un ancla movil,
TAREA 2.c, acta 139 caida 4.2) y en la vuelta 142 pasa a SIETE con
`vuelta140_2a_mutaciones.py` y `vuelta141_2_mutaciones.py` (TAREA 2.d; acta 141
caida 4.3: "VIEJAS sigue en cinco y no incluye ni las de la 140 ni las de la
141, cuando su propio docstring dice que una mutacion sin sujeto es ROJO"). La
cifra del rotulo se computa de `VIEJAS`, no se teclea, para que anadir una no
deje una frase mintiendo detras; su prueba de mutacion es
scripts/loop/vuelta142_2d_mutacion_bateria.py, que quita un script de la nomina
EN MEMORIA y exige que la cifra del rotulo baje sola.

CASO DECLARADO (vuelta 142, TAREA 2.d): un exit distinto de cero CONOCIDO,
MEDIDO Y PUBLICADO en su vuelta deja de contarse como NO MORDIO, pero se imprime
con su motivo entero y SOLO si la salida trae su MARCA OBLIGATORIA. Ver
`CASOS_DECLARADOS`. Es lo contrario de una lista de exclusiones: la exencion es
de UN fallo concreto, y el dia que el script falle por otra cosa vuelve a caer
en ROJO.

NOMBRE ESTABLE, SIN NUMERO DE VUELTA, como verificar_apertura_sellada.py y
tallar_cabecera_reporte.py: se corre igual en toda vuelta y no se clona.

POR QUE NACE (encargo de la vuelta 138, TAREA 2.b, ultimo parrafo: "LA GUARDA
PARA QUE NO VUELVA A PASAR: las cuatro mutaciones viejas entran en el ciclo de
cierre de cada vuelta, y a partir de que esten re-ancladas, ANCLA PERDIDA cuenta
como ROJO"). Tres de las cuatro (vuelta135_2e_mutacion_1, _2 y _3) estaban
ancladas a un literal de docs/loop/REPORTE.md, que se sobreescribe cada vuelta:
desde la 135 caian con "ROJO PREVIO" sin llegar a probar nada, y nadie lo
midio hasta la mutacion D de la vuelta 137. La 2.b de la vuelta 138 las
re-anclo a docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md, un sujeto propio y
congelado que ellas mismas cotejan contra el blob del acta 134 en cada corrida.

LA DIFERENCIA CON LA MUTACION D DE LA VUELTA 137, dicha con todas sus letras:
aquella distinguia LA GUARDA NO MORDIO (fallo de verdad) de ANCLA PERDIDA (la
mutacion no llega a correr), y hacia BIEN en distinguirlas, porque entonces las
tres estaban desancladas y contarlo como fallo de la guarda habria sido mentir
en la otra direccion. DESDE QUE ESTAN RE-ANCLADAS ESA DISTINCION SE ACABA: una
mutacion que no encuentra su sujeto es una guarda que no mide, y aqui es ROJO.

LA COLETILLA DE LA VUELTA 145 (CORRECCION 22; acta 144, caidas 4.4 a 4.6 de la
casa, LAS TRES DE LA MISMA ENFERMEDAD, EL SUJETO VIVO). La regla de entrada de
arriba se queda corta y se completa.

  LA LETRA DE LA 145 A LA 148, QUE NO SE BORRA: "UNA MUTACION ENTRA EN LA VUELTA
  SIGUIENTE A LA QUE NACE, Y SOLO SI SU SUJETO ESTA CONGELADO."

  LA LETRA DESDE LA VUELTA 148 (TAREA 2.5, sobre la adjudicacion 3.5 del acta
  147): LO QUE ESTA REGLA EXIGE ES SUJETO CONGELADO. EL PLAZO DE UNA VUELTA ERA
  EL MEDIO, NO EL FIN. Se escribio "en la vuelta siguiente" porque esperar una
  vuelta era la forma comoda de comprobar que el verde de una mutacion
  SOBREVIVIA a que su propia vuelta escribiera el reporte; pero lo que hace
  falta no es que pase el tiempo, es que EL SUJETO NO SE MUEVA. Una mutacion
  anclada a un fichero congelado y cotejado contra un blob de git ya cumple el
  fin el mismo dia que nace, y hacerla esperar una vuelta no la hace mas
  segura: solo la hace mas tarde. Una anclada a un fichero VIVO no cumple el
  fin ni esperando diez vueltas, porque el sujeto se le mueve debajo igual.
  POR ESO LA CONDICION DE ENTRADA ES EL SUJETO CONGELADO, Y EL PLAZO DEJA DE
  SER REQUISITO. La que no pueda tener sujeto congelado entra como CASO
  DECLARADO, igual que antes.

  QUE NO CAMBIA, PARA QUE NADIE LEA DE MAS: no se afloja ni una comprobacion.
  Una mutacion con sujeto vivo sigue sin poder entrar, ANCLA PERDIDA sigue
  siendo ROJO, y los CASOS DECLARADOS siguen necesitando su marca. Lo unico que
  se cae es un plazo que nunca fue lo que protegia. Medido en la vuelta 145
sobre el arbol limpio de la apertura, esta bateria daba ROJO con NO MORDIO 1,
`vuelta144_2d_mutacion_cobertura.py`, cuyo sujeto era el `docs/loop/REPORTE.md`
VIVO: estaba verde cuando se corrio y roja en cuanto se escribio el reporte de
esa misma vuelta. Un sujeto vivo hace que el verde de una vuelta no sobreviva a
la vuelta. La que no pueda tener sujeto congelado entra como CASO DECLARADO,
con su exit esperado y su motivo escrito en el propio fichero, como ya hacen
`vuelta135_2e_mutacion_3.py` y `vuelta140_2a_mutaciones.py`.

QUE COMPRUEBA. Corre TODAS las de `VIEJAS` (la cifra sale de len(VIEJAS), nunca
tecleada; en la vuelta 144 pasaron de SIETE a TRECE, y en la 145 de TRECE a
DIECINUEVE) y exige EXIT 0 de
cada una, salvo los CASOS DECLARADOS de arriba. Clasifica:
  OK             . exit 0, la mutacion corrio y mordio.
  ANCLA PERDIDA  . la salida trae "ROJO PREVIO": el sujeto no esta o no es el
                   que la mutacion espera. ROJO.
  NO MORDIO      . exit distinto de 0 sin "ROJO PREVIO": la guarda que la
                   mutacion prueba dejo de morder. ROJO.
  CASO DECLARADO . (TAREA 2.d, vuelta 142) exit distinto de 0 QUE COINCIDE con el
                   declarado en CASOS_DECLARADOS Y cuya salida trae la marca
                   obligatoria de esa entrada. NO es rojo, y se imprime con su
                   motivo entero para que se vea.
  NO REPRODUCIBLE. (TAREA 2.f, vuelta 141) la mutacion se corre DOS VECES
                   seguidas y alguna de las salidas selladas que escribe sale
                   DISTINTA entre las dos. ROJO, nombrando el fichero y la
                   primera linea que cambia. Una salida sellada que no se
                   repite no prueba nada.

PRUEBA DE MUTACION (EJECUTOR regla 1, sobre una variable QUE EL CODIGO COMPUTA):
--mutar-ancla fabrica una copia del sujeto fijo CON EL ANCLA ARRANCADA en un
directorio temporal, apunta alli las tres re-ancladas con --sujeto, y exige que
las tres salgan clasificadas como ANCLA PERDIDA y que el veredicto sea ROJO. La
variable del veredicto es la lista `perdidas`, construida leyendo la salida real
de cada proceso; no hay ningun literal comparado consigo mismo. P.16, QUIEN
FABRICA LIMPIA: la copia temporal se retira siempre.

USO:
  python scripts/loop/verificar_mutaciones_viejas.py
  python scripts/loop/verificar_mutaciones_viejas.py --mutar-ancla
  python scripts/loop/verificar_mutaciones_viejas.py --mutar-reproducibilidad

--- ADJUDICACION 6.9 DEL ACTA 157 (3 sep 2026): ESTA GUARDA ATRIBUIA SUS ROJOS
AL SCRIPT EQUIVOCADO, Y SE CINE A LOS FICHEROS QUE CADA SCRIPT ESCRIBE ---

CORRECCION DECLARADA POR ADICION. Nada de lo escrito arriba se borra: el cotejo
de reproducibilidad de la TAREA 2.f de la vuelta 141 sigue siendo lo que esta
bateria hace, y sigue siendo necesario.

COMO SE DESCUBRIO, Y LO DESCUBRIO EL AUDITOR CAYENDO EL (acta 157, caida 2 y
seccion 5.3). Corrio esta bateria CON SUS PROPIOS INSTRUMENTOS CORRIENDO AL
LADO, despues de haberle escrito al ejecutor que se corre SOLA. Salio ROJO
exit 1 con DOS "salidas selladas que NO SE REPITEN", acusando a
`vuelta144_2b_mutacion_giro.py` y a `vuelta147_2c_mutacion_vitalidad.py` por
`_auditor_v157_p3b.txt` y `_auditor_v157_tachado.txt`, DOS FICHEROS SUYOS QUE
NINGUNO DE LOS DOS SCRIPTS ESCRIBE: la propia salida decia de los dos "salidas
selladas que escribe: ninguna". Re corrida sola: VERDE. Las dos corridas quedan
selladas en `docs/loop/_auditor_v157_mutaciones.txt` (la roja) y
`_auditor_v157_mutaciones2.txt` (la verde) para poder reproducir el escenario.

EL DEFECTO, EN UNA LINEA: `correr_dos_veces` computaba `inestables` sobre
`set(tras1) | set(tras2)`, o sea SOBRE EL DIRECTORIO ENTERO, y le colgaba a un
script cualquier fichero que apareciera o cambiara mientras el corria. FALLA
RUIDOSO, QUE ESTA BIEN, PERO NOMBRA AL CULPABLE EQUIVOCADO, Y UN ROJO QUE NOMBRA
AL SCRIPT EQUIVOCADO ES UN ROJO QUE NO SE PUEDE SEGUIR: eso es media guarda.

LO QUE SE ADJUDICA, POR EXTENSION DEL BANCO 9 Y SIN DOCTRINA NUEVA:
  (a) LA COMPROBACION DE REPRODUCIBILIDAD SE CINE A `escritos`, que es la lista
      de ficheros que ESE script escribio en su primera corrida, y que esta
      guarda YA COMPUTA Y YA PUBLICA ("salidas selladas que escribe (computadas,
      no tecleadas)"). Ningun fichero fuera de esa lista puede poner a un script
      en NO REPRODUCIBLE.
  (b) LO QUE APAREZCA O CAMBIE EN `docs/loop/` Y NO SEA DE NADIE NO SE CALLA: se
      reporta APARTE, con su nombre, bajo el rotulo RUIDO DE CONCURRENCIA, y NO
      ENCIENDE EL ROJO DE NINGUN SCRIPT. Callarlo seria la caida contraria.
  (c) EL ROJO SE QUEDA INTACTO PARA LO QUE SI ES SUYO: si un fichero que el
      script escribe cambia entre dos corridas, sigue siendo NO REPRODUCIBLE y
      sigue siendo exit 1.

SU CASO POSITIVO POR MUTACION YA EXISTIA ANTES QUE LA CORRECCION, que es lo mas
limpio que le puede pasar a una guarda: es la corrida roja del auditor. Se
reproduce con `scripts/loop/vuelta157_tarea5c_mutacion_ruido.py`, salida
`docs/loop/SALIDA_V157_T5C_MUTACION_RUIDO.txt`, que exige las dos mitades: que
la version VIEJA de `correr_dos_veces` siga saliendo ROJA sobre ese escenario y
que la NUEVA salga VERDE nombrando el ruido aparte. Y LAS 23 SIGUEN SIENDO 23.

--- EL CRONOMETRO (VUELTA 164, TAREA 2.a; ADJUDICACION 6.8 DEL ACTA 163) ---

CORRECCION DECLARADA POR ADICION: no se borra nada de lo de arriba, no se quita
ni una comprobacion y NO SE RECORTA LA NOMINA para que corra antes.

POR QUE NACE. En la vuelta 163 esta nomina paso de 23 a 51 entradas, y cada
entrada se corre DOS VECES por el cotejo de reproducibilidad de la TAREA 2.f de
la vuelta 141: la bateria hace mas del doble de trabajo que su cifra sugiere. El
auditor la lanzo DOS VECES en la 163 y no termino ninguna; la primera la corto un
`timeout 900` SIN UNA SOLA LINEA DE VEREDICTO, y dentro hay arneses de 38
segundos (acta 163, seccion 5.3). Una guarda que el ciclo de cierre corre en cada
vuelta y que puede tardar veinte minutos NECESITA SU RELOJ PUBLICADO, o el
siguiente que la lance la matara creyendo que colgo, y matarla no es un rojo: es
no haberla medido.

QUE PUBLICA, Y TODO COMPUTADO DE `reloj`, NADA TECLEADO: el tiempo de CADA arnes
en su propia fila, el TIEMPO TOTAL en segundos y en minutos, el mas lento, el mas
rapido, la mediana, cuantos pasan de 30 segundos y los diez mas lentos en orden.
Se mide con `time.perf_counter`, que es monotono, y no con la hora del reloj.

QUE NO CAMBIA: ni un veredicto. El cronometro solo imprime.
"""
import argparse
import ast
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
DOCS_LOOP = os.path.join(RAIZ, "docs", "loop")
SUJETO_FIJO = os.path.join(DOCS_LOOP, "SUJETO_FIJO_V135_2E_REPORTE_134.md")


def corte_de_git():
    """EL COMMIT EN QUE SE ESTA MIDIENDO, LEIDO DE GIT EN ESTA CORRIDA.

    Devuelve los doce primeros caracteres del HEAD, o `(no medible)` si git no
    responde. NO ES PURA: es la unica pieza del corte que toca git, y por eso va
    separada de `sello_de_corte()`, que si lo es y por eso se puede tumbar en un
    arnes sin llamar a ningun proceso."""
    try:
        r = subprocess.run(["git", "rev-parse", "HEAD"], cwd=RAIZ, capture_output=True)
        h = r.stdout.decode("utf-8", errors="replace").strip()
        return h[:12] if len(h) == 40 else "(no medible)"
    except Exception:
        return "(no medible)"


def sello_de_corte(denominador, head, que="nomina contada en esta corrida"):
    """UNA CIFRA QUE SE MUEVE DENTRO DE LA VUELTA, SIEMPRE CON SU CORTE PEGADO.
    PURA: recibe la cifra, el head y QUE se esta contando, y devuelve el texto
    que se imprime.

    EL TERCER PARAMETRO NACE EN LA VUELTA 180 (TAREA 3; hallazgo del fundador
    medido en la seccion 6 del acta 179, adjudicado por `banco 9.21` y por el
    punto 7.2 del acta 178). Hasta hoy este sello decia `nomina` con esa palabra
    clavada, porque la nomina era la unica cifra que sabiamos que se movia
    dentro de la vuelta. **NO ES LA UNICA:** la tabla de tramos de
    `scripts/loop/backlog_l03_resuelto.py` se movio dentro de la 179, de
    `6/29/8` y `34/44/10` a `14/39/18` y `26/34/0`, y las dos mediciones eran
    verdaderas. Con la palabra clavada, cablear este sello en la tabla de tramos
    habria escrito la palabra `nomina` sobre una cifra que no es la nomina, o
    sea una etiqueta falsa; con el parametro, cada sede dice QUE cuenta.

    EL VALOR POR DEFECTO CONSERVA A SUS LLAMADORES VIEJOS byte a byte, y eso se
    comprueba: `scripts/loop/vuelta179_tarea1d_mutacion_corte.py` no cambia ni
    una linea y sigue pasando.

    POR QUE EXISTE, Y EL MOTIVO ESTA MEDIDO (vuelta 179, TAREA 1.d; adjudicacion
    7.2 del acta del auditor de la vuelta 178, por `banco 9.21`). La 178 publico
    `15 de 92` **siendo verdad cuando lo midio**, y al cerrar esa misma vuelta el
    denominador era 98, porque LA NOMINA CRECE DENTRO DE LA PROPIA VUELTA que la
    esta contando. Una cifra de la nomina sin corte no se puede cotejar con
    nada: no se sabe contra que denominador se midio.

    CABLEADO DONDE SE GENERA LA CIFRA, NO EN UNA FRASE, que es la letra exacta
    del encargo. Quien imprima un denominador de la nomina llama a esto y no
    teclea el numero suelto."""
    return "%d (corte: HEAD %s, %s)" % (denominador, head, que)

# Las CUATRO. La primera fabrica su propio reporte y nunca estuvo anclada a
# REPORTE.md, por eso no admite --sujeto y no entra en la prueba del ancla.
VIEJAS = [
    ("vuelta133_tarea2e_mutacion_cifras.py", False),
    ("vuelta135_2e_mutacion_1.py", True),
    ("vuelta135_2e_mutacion_2.py", True),
    ("vuelta135_2e_mutacion_3.py", True),
    # QUINTA, ANADIDA EN LA VUELTA 140 (TAREA 2.c, acta 139 caida 4.2). Su
    # bloque (iii) tenia un ANCLA MOVIL (`git log -1 -- REPORTE.md`) y la
    # reparacion la clava por hash con su sha256. Entra en esta bateria
    # justamente para que, SI EL ANCLA SE VUELVE A PERDER, salga como ANCLA
    # PERDIDA y no como verde. No admite --sujeto: fabrica los suyos.
    ("vuelta139_2b_mutaciones.py", False),
    # SEXTA Y SEPTIMA, ANADIDAS EN LA VUELTA 142 (TAREA 2.d; acta 141, caida
    # 4.3 de la casa: "VIEJAS sigue en cinco y no incluye ni las de la 140 ni
    # las de la 141, cuando su propio docstring dice que una mutacion sin
    # sujeto es ROJO"). Ninguna admite --sujeto: las dos fabrican los suyos EN
    # MEMORIA. La cifra del rotulo se sigue computando de len(VIEJAS).
    ("vuelta140_2a_mutaciones.py", False),
    ("vuelta141_2_mutaciones.py", False),
    # DE LA OCTAVA A LA DECIMOTERCERA, ANADIDAS EN LA VUELTA 144 (TAREA 2.c;
    # acta 143, adjudicacion 3.6, discutible 6 del ejecutor CONCEDIDO: "VIEJAS
    # tiene 7 entradas y las tres de esta vuelta no estan").
    #
    # LA REGLA QUE QUEDA, Y SE ESCRIBE AQUI PARA QUE NO HAGA FALTA VOLVER A
    # ADJUDICARLA: UNA MUTACION ENTRA EN ESTA BATERIA EN LA VUELTA SIGUIENTE A
    # LA QUE NACE, NO MAS TARDE. Una mutacion que nace, muerde una vez y no
    # entra en la bateria deja de medir desde el dia siguiente, y nadie se
    # entera hasta que un acta lo cuenta a mano.
    #
    # Las TRES de la vuelta 143:
    ("vuelta143_2a_mutaciones.py", False),
    ("vuelta143_2b_mutacion_bateria.py", False),
    ("vuelta143_2c_mutacion_positivo.py", False),
    # Y LAS TRES QUE NACEN HOY, en esta misma vuelta 144, por la regla de
    # arriba aplicada a si misma: entran el dia que nacen y no se esperan una
    # vuelta mas. Ninguna admite --sujeto: las tres fabrican los suyos EN
    # MEMORIA y con cero escrituras.
    ("vuelta144_2a_mutaciones.py", False),
    ("vuelta144_2b_mutacion_giro.py", False),
    ("vuelta144_2d_mutacion_cobertura.py", False),
    # DE LA DECIMOCUARTA A LA DECIMONOVENA, ANADIDAS EN LA VUELTA 145 (TAREA
    # 2.b), por la MISMA regla de arriba, ahora con la coletilla que la
    # CORRECCION 22 le pone: UNA MUTACION ENTRA EN ESTA BATERIA EN LA VUELTA
    # SIGUIENTE A LA QUE NACE, Y SOLO SI SU SUJETO ESTA CONGELADO. La que no
    # pueda tenerlo entra como CASO DECLARADO, con su exit esperado y su
    # motivo escrito en el propio fichero.
    #
    # LAS TRES QUE NACIERON EN LA TAREA 3 DE LA VUELTA 144 y que la 2.c de esa
    # vuelta no llego a meter. `vuelta144_3b_mutacion_negativa.py` entra CON
    # SUJETO CONGELADO y no como caso declarado: su pre-estado se monta de un
    # ref de git computado (ver su propio docstring), y asi vuelve a morder 3
    # de 3 en vez de quedar excusada.
    ("vuelta144_3a_mutaciones.py", False),
    ("vuelta144_3b_mutacion_negativa.py", False),
    ("vuelta144_3c_caso_positivo_1190.py", False),
    # Y LAS TRES QUE NACEN HOY, en esta misma vuelta 145. Las tres eligen su
    # sujeto POR COMPUTO y ninguna toma el arbol vivo: la 2.a lee un ref de
    # git, la 2.b parchea guardas en memoria y la 2.c fabrica su ficha rota.
    ("vuelta145_2a_mutacion_ancla_unica.py", False),
    ("vuelta145_2b_mutacion_arneses.py", False),
    ("vuelta145_2c_mutacion_censo.py", False),
    # LA VIGESIMA, ANADIDA EN LA VUELTA 146 (TAREA 2.e), por la MISMA regla con
    # la coletilla de la CORRECCION 22: entra el dia que nace y CON SUJETO
    # CONGELADO. Su caso que manda, el (A), corre la guarda de ausencias sobre
    # `a9b638ba:docs/loop/REPORTE.md`, el reporte de la vuelta 145 TAL COMO SE
    # COMMITEO, leido con `git show`: no es un sujeto fabricado para la ocasion,
    # es el texto que fallo. Los otros tres se fabrican EN TEMPORAL y se borran
    # siempre (P.16). No admite --sujeto.
    ("vuelta146_2b_mutacion_ausencias.py", False),
    # LA VIGESIMOPRIMERA, ANADIDA EN LA VUELTA 147 (TAREA 2.f), por la MISMA
    # regla con la coletilla de la CORRECCION 22: entra el dia que nace y CON
    # SUJETO CONGELADO. Sus dos casos rojos corren sobre refs de git COMPUTADOS
    # (el commit de nacimiento de `SALIDA_V146_3E_BARRIDO_UMBRAL.txt` y el
    # ultimo commit que toco `docs/loop/REPORTE.md` antes del HEAD de apertura
    # de la 147), no sobre el arbol vivo y sin un solo hash tecleado. Su caso
    # verde y sus dos mutaciones se corren EN VIVO y se limpian solas (P.16):
    # no hay artefacto que pueda envejecer.
    ("vuelta147_2c_mutacion_vitalidad.py", False),
    # LA VIGESIMOSEGUNDA Y LA VIGESIMOTERCERA, ANADIDAS TAMBIEN EN LA VUELTA 147
    # (TAREAS 3.d y 3.e), por la MISMA regla y con la misma coletilla. NINGUNA
    # DE LAS DOS PUEDE ENVEJECER POR EL CAMINO QUE LA CORRECCION 22 CURO, y no
    # porque se les haya congelado un fichero sino porque NO LEEN NINGUNO QUE
    # PUEDA MOVERSE A SUS ESPALDAS: las dos eligen su sujeto POR COMPUTO sobre
    # el estado de hoy (la entrada del medio de la nomina real; la pareja viva
    # de mayor coseno de su dominio) y las dos mutan COPIAS EN MEMORIA. Las dos
    # comprueban ademas `git status --porcelain -- dataset/` a los dos lados y
    # exigen que sea IDENTICO, asi que su verde no puede venir de haber tocado
    # el dataset.
    ("vuelta147_3d_mutacion_nomina.py", False),
    ("vuelta147_3e_simular_a26.py", False),
    # --- DE LA VIGESIMOCUARTA EN ADELANTE, ANADIDAS EN LA VUELTA 163 (TAREA 2;
    # ADJUDICACION 6.8 DEL ACTA 162) --------------------------------------
    #
    # POR QUE ENTRAN TODAS DE GOLPE, Y NO ES UN CAPRICHO: LA NOMINA LLEVABA
    # QUINCE VUELTAS CONGELADA. Medido en el acta 162 (seccion 5.1) y
    # recomputado en la vuelta 163 (`docs/loop/SALIDA_V163_T2_CENSO_POST147.txt`):
    # la nomina tenia 23 entradas, su ultima vuelta representada era la 147, y en
    # `scripts/loop/` habia 84 arneses de mutacion de los cuales VEINTIDOS
    # nacieron despues de la 147 y ninguno entro. La regla que lo prohibe estaba
    # escrita aqui mismo desde la vuelta 144 y nadie la miro: "UNA MUTACION ENTRA
    # EN ESTA BATERIA EN LA VUELTA SIGUIENTE A LA QUE NACE, NO MAS TARDE".
    #
    # Y NO ERA TEORICO: CUATRO DABAN ROJO DENTRO DEL AGUJERO. Los cuatro se
    # arreglaron EN LA FUENTE en esta misma vuelta, cada uno con su diagnostico
    # medido y ninguno en verde alegado ni borrado:
    #   - `vuelta148_0d_mutacion_corredor.py`: llevaba roto desde la vuelta 154,
    #     cuando `intrusos_del_corredor` paso de devolver UNA lista a devolver
    #     DOS. Reventaba al desempaquetar.
    #   - `vuelta157_tarea4b_mutacion_tachado.py`: nacio caducado en su propio
    #     commit `5ebac882`, el mismo que tacho las celdas que el arnes exigia
    #     limpias. Reescrito para computar su sujeto y su clase esperada.
    #   - `vuelta160_tarea6b_mutacion_puerta.py`: su contraprueba sacaba la
    #     guarda vieja de `git show HEAD:`, o sea el remedio comparado consigo
    #     mismo desde el commit siguiente al suyo. Anclado a un ref FIJO.
    #   - `vuelta162_tarea1a_mutacion_serie.py`: sus esperados estaban clavados a
    #     un estado que su propio commit cambio. Reescrito a DELTAS.
    #
    # UNA NOTA QUE NO SE CALLA, PORQUE CALLARLA SERIA LO CONTRARIO DEL BANCO 9:
    # `vuelta154_tarea2d_mutacion_guarda.py` SALIO ROJO UNA VEZ y no se ha
    # reproducido. Las dos corridas del lote estan selladas
    # (`SALIDA_V163_T2_CENSO_POST147.txt` con cinco rojos y `..._SEGUNDA.txt` con
    # cuatro) y la medicion del intermitente esta en
    # `docs/loop/SALIDA_V163_T2_FLAKE_154.txt`. Entra igual, y entra con esta
    # nota: INTERMITENTE NO REPRODUCIDO no es lo mismo que sano.
    ("vuelta148_0d_mutacion_corredor.py", False),
    ("vuelta148_1a_mutacion_embebido.py", False),
    ("vuelta148_2a_mutacion_nomina_commiteada.py", False),
    ("vuelta148_2b_mutacion_cifras_conjunto.py", False),
    ("vuelta148_2c_mutacion_vara_parada.py", False),
    ("vuelta148_2d_mutacion_exencion.py", False),
    ("vuelta150_5c_mutacion_ciclo.py", False),
    ("vuelta154_tarea2d_mutacion_guarda.py", False),
    ("vuelta154_tarea6_mutacion_corredor.py", False),
    ("vuelta156_tarea4b_mutacion_tallador.py", False),
    ("vuelta156_tarea5d_mutacion_corredor.py", False),
    ("vuelta157_tarea4b_mutacion_tachado.py", False),
    ("vuelta157_tarea5c_mutacion_ruido.py", False),
    ("vuelta157_tarea6b_mutacion_re_sellado.py", False),
    ("vuelta159_tarea6c_mutacion_exencion.py", False),
    ("vuelta160_tarea6b_mutacion_puerta.py", False),
    ("vuelta160_tarea7c_mutacion_guarda_cita.py", False),
    ("vuelta161_tarea1a_mutacion_alcance.py", False),
    ("vuelta162_tarea1a_mutacion_serie.py", False),
    ("vuelta162_tarea2a_mutacion_puerta.py", False),
    ("vuelta162_tarea2b_mutacion_excepcion.py", False),
    ("vuelta162_tarea3_mutacion_fila.py", False),
    # Y LAS QUE NACEN HOY, EN LA VUELTA 163, por la misma regla aplicada a si
    # misma, que es lo que la vuelta 144 hizo con las suyas: entran el dia que
    # nacen y no se esperan una vuelta mas. Ninguna admite `--sujeto`: todas
    # eligen su sujeto por computo o sobre commits fijos de la historia, y
    # ninguna escribe en `docs/loop/`.
    ("vuelta163_tarea1b_mutacion_relectura.py", False),
    ("vuelta163_tarea1c_mutacion_tramo.py", False),
    ("vuelta163_tarea2_mutacion_nomina.py", False),
    ("vuelta163_tarea4a_mutacion_cobertura.py", False),
    ("vuelta163_tarea4b_mutacion_re_sellado.py", False),
    ("vuelta163_tarea5a_mutacion_contador.py", False),
    # Y LAS QUE NACEN EN LA VUELTA 164, por la misma regla aplicada a si misma:
    # entran el dia que nacen y no se esperan una vuelta mas. Ninguna admite
    # `--sujeto`, ninguna escribe en `docs/loop/` y las dos eligen su sujeto por
    # computo o lo fabrican en memoria, asi que ninguna puede caducar por el
    # camino que la CORRECCION 22 curo.
    #   - `164_tarea1`: actas de mentira como listas de lineas y series de
    #     mentira como listas de tuplas; sus esperados que podrian caducar son
    #     DELTAS (anadir una entrada mueve el libre EXACTAMENTE uno).
    #   - `164_tarea4`: el grafo, el banco y el registro de HOY, y el estado del
    #     registro medido como DELTA contra lo que el acta 163 midio al abrir la
    #     vuelta, no como estado clavado.
    ("vuelta164_tarea1_mutacion_registro.py", False),
    ("vuelta164_tarea4_mutacion_005.py", False),
    # Y LAS QUE NACEN EN LA VUELTA 165, por la misma regla aplicada a si misma:
    # entran el dia que nacen. Ninguna admite `--sujeto`, ninguna escribe en
    # `docs/loop/` y las dos fabrican su sujeto en memoria, asi que ninguna
    # puede caducar por el camino que la CORRECCION 22 curo.
    #   - `165_tarea1`: actas de mentira como listas de lineas; su cifra de
    #     caidas se COMPUTA del acta fabricada, no se clava.
    #   - `165_tarea2`: nominas y directorios de mentira; mide el patron VIEJO
    #     contra el NUEVO sobre el mismo sujeto, asi que su rojo es el del
    #     agujero real y CAE si alguien devuelve el patron a su forma vieja.
    #   - `165_tarea4`: fuentes de mentira escritas en un temporal; clasifica y
    #     muta sus esperados. No lee ningun artefacto vivo del repo.
    ("vuelta165_tarea1_mutacion_registro.py", False),
    ("vuelta165_tarea2_mutacion_censo.py", False),
    ("vuelta165_tarea4_mutacion_sujeto.py", False),
    #   - `165_tarea6`: mapas de alias y veredictos fabricados en memoria mas
    #     la ficha de OP-L-01 leida hoy, cuyas cifras se miden como PRESENCIA
    #     del numeral y como DESIGUALDAD, nunca como estado clavado.
    ("vuelta165_tarea6_mutacion_op_l_01.py", False),
    # --- LOS SEIS DE LAS VUELTAS 166 Y 167, QUE ENTRAN EN LA VUELTA 168
    #     (TAREA 3.a; hallazgo 4.5 del acta 167, decision del fundador 4) ------
    #
    # POR QUE ESTABAN FUERA, Y NO ES UN DESCUIDO SUELTO SINO EL MISMO AGUJERO DE
    # LA VUELTA 163 ABIERTO OTRA VEZ: la bateria no se corrio ni en la 166 ni en
    # la 167 (las dos dejaron su fichero de salida en CERO BYTES), y la unica
    # guarda que vigila esto es `vuelta163_tarea2_mutacion_nomina.py`, que vive
    # DENTRO de la bateria. Dos vueltas sin correrla bastaron para que la nomina
    # se quedara atras sola. El acta 167 lo midio: 6 arneses posteriores a la
    # 165 fuera de la nomina, y su arnes centinela dando `NO MORDIO` con real 6
    # y esperado 0, que era el propio agujero cantando.
    #
    # LOS SEIS ENTRAN POR LA REGLA DE SIEMPRE, Y LA REGLA ES EL SUJETO
    # CONGELADO, NO EL CALENDARIO. Ninguno admite `--sujeto`, ninguno escribe en
    # `docs/loop/` y ninguno se ancla a un fichero vivo que pueda moverseles
    # debajo:
    #   - `166_tarea1`: actas y series de mentira en memoria; sus cifras son
    #     conteos del sujeto fabricado y deltas, no estados clavados.
    #   - `166_tarea2`: la ficha de OP-L-01 leida hoy, medida por PRESENCIA de
    #     numeral y por DESIGUALDAD, mas mapas fabricados en memoria.
    #   - `166_tarea3`: el retrato medido sobre copias en memoria; la fila que
    #     valia cero se comprueba como delta de la resta.
    #   - `166_tarea6`: la guarda estrechada, con su sujeto fabricado.
    #   - `167_tarea1`: actas de mentira como listas de lineas; la concordancia
    #     del titulo se computa de los conteos.
    #   - `167_tarea3`: copia mutada del recomputo en memoria; su rojo es el de
    #     la comprobacion `ii` y CAE si alguien devuelve el ultimo gana.
    ("vuelta166_tarea1_mutacion_registro.py", False),
    ("vuelta166_tarea2_mutacion_correccion.py", False),
    ("vuelta166_tarea3_mutacion_retrato.py", False),
    ("vuelta166_tarea6_mutacion_guarda.py", False),
    ("vuelta167_tarea1_mutacion_registro.py", False),
    ("vuelta167_tarea3_mutacion_ii.py", False),
    # Y LOS QUE NACEN HOY, EN LA VUELTA 168, por la misma regla aplicada a si
    # misma: entran el dia que nacen y no se esperan una vuelta mas. Meterlos
    # ahora es ademas lo unico que impide repetir el agujero que esta misma
    # TAREA 3 esta cerrando. Los tres eligen su sujeto por computo o lo fabrican
    # en memoria, ninguno admite `--sujeto` y ninguno escribe en `docs/loop/`:
    #   - `168_tarea1_mutacion_registro`: actas de mentira en memoria mas el
    #     acta 167 real; la linea del fundador se computa del reparto.
    #   - `168_tarea1_mutacion_nota`: mediciones fabricadas en memoria mas los
    #     blobs del commit del acta 167, que es un commit FIJO de la historia.
    #   - `168_tarea2_mutacion_reconstructor`: corredores fabricados en memoria
    #     mas los corredores reales de las vueltas 166 y 167, delimitados por
    #     commits de acta que ya no se mueven.
    ("vuelta168_tarea1_mutacion_registro.py", False),
    ("vuelta168_tarea1_mutacion_nota.py", False),
    ("vuelta168_tarea2_mutacion_reconstructor.py", False),
    #   - `168_tarea4_mutacion_op_v_01`: cuerpos de commit fabricados en memoria
    #     mas el commit del cierre de la fase 08, que es un commit FIJO de la
    #     historia. Nace DESPUES de la primera corrida de la bateria de esta
    #     vuelta y por eso la bateria se RE CORRE ENTERA al cierre: una nomina
    #     que crece despues de la corrida que la mide deja la corrida coja, y eso
    #     es justo el agujero que esta TAREA 3 cerro.
    ("vuelta168_tarea4_mutacion_op_v_01.py", False),
    # ANADIDO EN LA VUELTA 169 (TAREA 2). Su sujeto son celdas FABRICADAS EN
    # MEMORIA y el fichero del arnes hermano ya commiteado: CONGELADO, que es la
    # condicion de entrada desde la letra de la vuelta 148. La propia guarda de
    # abajo lo reclamo en la corrida 2 de esta vuelta, con estas palabras: "1
    # arnes(es) de mutacion nacidos despues de la vuelta 168 se quedan FUERA".
    ("vuelta169_tarea2_mutacion_reanclaje.py", False),
    # ANADIDOS EN LA VUELTA 170 (TAREAS 1.a y 2.a). LOS DOS ENTRAN EL MISMO DIA
    # QUE NACEN Y NO ES UN ATAJO: la condicion de entrada desde la vuelta 148 es
    # SUJETO CONGELADO, no el plazo, y los dos lo cumplen.
    #   - `170_tarea1a_mutacion_registro`: actas de mentira fabricadas EN MEMORIA
    #     mas el acta 169, que ya esta cerrada y firmada. Cuando el auditor
    #     escriba el acta 170, el acotado de este instrumento seguira delimitando
    #     la 169 por su cabecera siguiente y sus dos conteos (12 y 3) no se
    #     mueven. Y NACE PORQUE FALTABA: la vuelta 169 no escribio el suyo, medido
    #     con `ls scripts/loop/ | grep mutacion_registro` (existen los de las
    #     vueltas 164, 165, 166, 167 y 168; no existe el de la 169).
    #   - `170_tarea2a_mutacion_aislador`: filas y mapa de pasos fabricados EN
    #     MEMORIA. No lee ni el archivo de veredictos ni el grafo, asi que no hay
    #     nada que se le pueda mover debajo. CERO escrituras.
    ("vuelta170_tarea1a_mutacion_registro.py", False),
    ("vuelta170_tarea2a_mutacion_aislador.py", False),
    # --- LOS CINCO PRE 148 QUE ENTRAN, Y ENTRAN MEDIDOS (vuelta 165, TAREA 4;
    #     adjudicaciones 6.5 y 6.6 del acta 164) --------------------------------
    #
    # NO ENTRAN POR SER VIEJOS NI SE QUEDAN FUERA POR SERLO. La regla de entrada
    # NO habla del calendario: exige SUJETO CONGELADO ("EL PLAZO DE UNA VUELTA
    # ERA EL MEDIO, NO EL FIN", letra de la vuelta 148, arriba en este mismo
    # fichero). Asi que se midio el sujeto de LOS 41 uno por uno, con las dos
    # mitades, y salen CINCO congelados y 36 vivos. Salida:
    # `docs/loop/SALIDA_V165_T4_SUJETO_41.txt` (primera pasada) y
    # `docs/loop/SALIDA_V165_T4_SUJETO_41_TRANSITIVO.txt` (la que manda, con la
    # transitividad ya arreglada). NINGUNO entra en bloque y NINGUNO se descarta
    # en bloque.
    #
    # SU TIEMPO, PUBLICADO AL LADO, QUE ES LO QUE LA 6.6 EXIGE. Medido hoy, una
    # corrida cada uno: 109 en 12,3s; 112 en 0,1s; 113 en 0,1s; 98 en 0,1s; 99 en
    # 0,1s. TOTAL 12,7s una corrida, 25,4s las dos que esta bateria hace por su
    # cotejo de reproducibilidad. Los 36 que se quedan fuera costarian 1.094,1s
    # mas, y por eso importa que el criterio sea el sujeto y no la antiguedad.
    ("vuelta98_tarea4_prueba_mutacion.py", False),
    ("vuelta99_tarea3_prueba_mutacion.py", False),
    ("vuelta109_tarea2_4_prueba_mutacion.py", False),
    ("vuelta112_tarea2_6_mutacion_u_censo_dos_reglas.py", False),
    ("vuelta113_tarea2_mutacion_tsc.py", False),
    # --- LOS TRES DE LA VUELTA 171, QUE ENTRAN EN LA 172 (TAREA 4.b;
    #     adjudicacion 6.5 del acta 171) -----------------------------------------
    #
    # POR QUE ENTRAN AHORA Y NO ANTES: la regla escrita mas arriba en este mismo
    # fichero dice que una mutacion entra en la vuelta SIGUIENTE a la que nace, no
    # mas tarde. La vuelta 171 escribio TRES arneses y no metio ninguno; su propia
    # funcion pura `arneses_que_faltan()` devolvia 3, la nomina tenia 75 entradas y
    # su ultima vuelta representada era la 170. El propio codigo dice que eso es
    # ROJO.
    #
    # EL ORDEN FUE OBLIGATORIO Y NO ES CAPRICHO: el tercero de los tres,
    # `vuelta171_tarea5a_mutacion_enchufe.py`, salia EXIT 1 hasta la TAREA 4.a de
    # esta vuelta, porque su caso `F` miraba EL ARBOL VIVO. Meterlo antes de
    # refundarlo habria sido meter un rojo DENTRO de la bateria. Refundado sobre
    # sujeto congelado da 15 casos, 15 pasan y 15 caen
    # (`docs/loop/SALIDA_V172_T4A_ENCHUFE_DESPUES.txt`).
    #
    # LOS TRES CON SUJETO CONGELADO, que es la condicion desde la vuelta 148:
    #   . `vuelta171_mutacion_busqueda_acta.py`: filas de `git log` fabricadas.
    #   . `vuelta171_tarea1a_mutacion_registro.py`: actas de mentira en memoria mas
    #     el acta 170, que ya esta cerrada y firmada.
    #   . `vuelta171_tarea5a_mutacion_enchufe.py`: reportes fabricados en un
    #     temporal, ya sin el arbol vivo dentro.
    # Ninguno admite `--sujeto`: los tres fabrican los suyos.
    ("vuelta171_mutacion_busqueda_acta.py", False),
    ("vuelta171_tarea1a_mutacion_registro.py", False),
    ("vuelta171_tarea5a_mutacion_enchufe.py", False),
    # --- LOS CUATRO DE LA VUELTA 172, QUE ENTRAN EN LA 173 (TAREA 1.a;
    #     adjudicacion 6.4 del acta 172) ----------------------------------------
    #
    # POR QUE ENTRAN AHORA: la regla escrita mas arriba en este mismo fichero dice
    # que una mutacion entra en la vuelta SIGUIENTE a la que nace, no mas tarde. Al
    # abrir la vuelta 173 la funcion pura `arneses_que_faltan()` devolvia CUATRO y
    # la ultima vuelta representada en la nomina era la 171, con 78 entradas
    # (`docs/loop/SALIDA_V173_APERTURA.txt`, bloque H.4). El propio codigo dice que
    # eso es ROJO.
    #
    # NO METEN NINGUN ROJO, Y ESTA MEDIDO ANTES DE METERLOS: el auditor los corrio
    # los cuatro en su acta de la vuelta 172 (43 de 43, 27 de 27, 24 de 24 y 17 de
    # 17), y esta misma vuelta los vuelve a correr uno a uno antes del parche
    # (`docs/loop/SALIDA_V173_T1A_ANTES.txt`) y dentro de la bateria despues
    # (`docs/loop/SALIDA_V173_BATERIA.txt`).
    #
    # LOS CUATRO CON SUJETO CONGELADO, que es la condicion desde la vuelta 148, y
    # ninguno admite `--sujeto`: los cuatro fabrican los suyos.
    #   . `vuelta172_tarea1b_mutacion_registro.py`: actas de mentira en memoria mas
    #     el acta 171, ya cerrada y firmada.
    #   . `vuelta172_tarea2a_mutacion_exclusion.py`: nombres de fichero fabricados
    #     como cadenas, sin tocar la carpeta de archivo.
    #   . `vuelta172_tarea3_mutacion_numeracion.py`: mapas de hechas fabricados.
    #   . `vuelta172_tarea5_mutacion_cierre.py`: un reporte cerrado de mentira, en
    #     memoria, al que se le quitan las cuatro piezas una a una.
    ("vuelta172_tarea1b_mutacion_registro.py", False),
    ("vuelta172_tarea2a_mutacion_exclusion.py", False),
    ("vuelta172_tarea3_mutacion_numeracion.py", False),
    ("vuelta172_tarea5_mutacion_cierre.py", False),
    # --- LOS CINCO DE LAS VUELTAS 173 Y 174, QUE ENTRAN EN LA 175 (TAREA 1;
    #     adjudicacion del acta del auditor de la vuelta 174) ------------------
    #
    # POR QUE ENTRAN AHORA, Y POR QUE SON CINCO Y NO UNO: la regla escrita mas
    # arriba en este mismo fichero dice que una mutacion entra en la vuelta
    # SIGUIENTE a la que nace, no mas tarde. Las vueltas 173 y 174 pasaron sin
    # vuelta de bateria (la 173 murio antes de su reporte; la 174 cerro con el
    # HUECO DECLARADO Y MEDIDO que el regimen 6.1 de AUDITOR.md le permite), asi
    # que la deuda se acumulo. Al abrir la vuelta 175, la funcion pura
    # `arneses_que_faltan()` devolvia CINCO y la ultima vuelta representada en la
    # nomina era la 172, con 82 entradas y 149 arneses en el directorio
    # (`docs/loop/SALIDA_V175_APERTURA.txt`, bloque H.5). El propio codigo dice
    # que eso es ROJO.
    #
    # LA NOMINA NO SE PODA, CRECE: podarla es lo que la casa reserva al fundador
    # (AUDITOR.md 6.1, opcion c RECHAZADA). Meter estos cinco sube el reloj de la
    # bateria y eso esta contado y publicado, no escondido.
    #
    # NO METEN NINGUN ROJO, Y ESTA MEDIDO ANTES DE METERLOS: esta misma vuelta
    # corrio los cinco UNO A UNO antes del parche y los cinco salieron exit 0 con
    # todos sus casos verdes (24 de 24, 26 de 26, 19 de 19, 22 de 22 y 34 de 34,
    # `docs/loop/SALIDA_V175_T1A_ANTES.txt`), y despues del parche vuelven a
    # correr DENTRO de la bateria, con su doble corrida
    # (`docs/loop/SALIDA_V175_BATERIA.txt`).
    #
    # LOS CINCO CON SUJETO CONGELADO, que es la condicion desde la vuelta 148, y
    # ninguno admite `--sujeto`: los cinco fabrican los suyos (medido en el
    # bloque H.6 de la apertura de esta vuelta, no supuesto).
    #   . `vuelta173_tarea1b_mutacion_hueco.py`: reportes cerrados de mentira en
    #     memoria, para la conducta nueva del HUECO DECLARADO Y MEDIDO.
    #   . `vuelta174_tarea1a_mutacion_44.py`: textos de clausula fabricados, para
    #     las guardas de `corregir()`.
    #   . `vuelta174_tarea1b_mutacion_esqueleto.py`: cabeceras de reporte
    #     fabricadas como cadenas, para `vuelta_del_reporte_del_arbol()`.
    #   . `vuelta174_tarea1b_mutacion_sellar.py`: filas de tabla fabricadas, para
    #     las guardas de `sellar()`.
    #   . `vuelta174_tarea2b_mutacion_confirmar.py`: glosas fabricadas, para las
    #     guardas del confirmador del R.41.
    ("vuelta173_tarea1b_mutacion_hueco.py", False),
    ("vuelta174_tarea1a_mutacion_44.py", False),
    ("vuelta174_tarea1b_mutacion_esqueleto.py", False),
    ("vuelta174_tarea1b_mutacion_sellar.py", False),
    ("vuelta174_tarea2b_mutacion_confirmar.py", False),
    # --- EL DE LA 176, QUE ENTRA EN SU MISMA VUELTA (TAREA 1.c) --------------
    #
    # POR QUE HOY Y NO EN LA 177, con la letra de este mismo fichero delante: la
    # regla desde la vuelta 148 (TAREA 2.5, adjudicacion 3.5 del acta 147) dice
    # que LO QUE SE EXIGE ES SUJETO CONGELADO y que EL PLAZO DE UNA VUELTA ERA EL
    # MEDIO, NO EL FIN. `vuelta176_tarea1c_mutacion_tramos.py` no tiene ancla
    # sobre ningun fichero vivo: llama a la funcion PURA `reparto_en_tramos()`
    # con nominas FABRICADAS en memoria, asi que su sujeto no se le puede mover
    # debajo y esperar una vuelta no lo haria mas seguro, solo mas tarde.
    #
    # Y SI NO ENTRARA HOY, ESTA MISMA BATERIA SALDRIA EN ROJO Y CON RAZON:
    # `arneses_que_faltan()` lo veria como un arnes de la vuelta 176, posterior a
    # la ultima vuelta representada, y se quejaria de que se queda fuera.
    #
    # QUE PRUEBA: que el reparto de la bateria en tramos conserva la nomina
    # ENTERA, en su orden, sin perder ni repetir ni una entrada. Su invariante NO
    # es vacio, y eso se demuestra en vez de afirmarse: el arnes le pasa TRES
    # repartos rotos a proposito (uno que pierde, uno que repite y uno que
    # desordena) y exige que los cace LOS TRES, en 4 escenarios cada uno.
    #
    # LA NOMINA NO SE PODA, CRECE (AUDITOR.md 6.1, opcion c RECHAZADA): con esta
    # entrada pasa de 87 a 88, y el reloj que eso suma se cuenta y se publica.
    ("vuelta176_tarea1c_mutacion_tramos.py", False),
    # VUELTA 177, TAREA 1.b. EL CASO POSITIVO POR MUTACION DEL ESPERADO
    # COMPUTADO. Su sujeto es el caso `H_el_texto_nombra_TODOS_los_hallazgos`
    # del arnes que salio EN ROJO en la bateria de la 176, y que la adjudicacion
    # 7.7 del acta 176 mando arreglar COMPUTANDO EL ESPERADO. Lo que este arnes
    # prueba es lo que un esperado computado puede perder: que siga MORDIENDO.
    # Le rompe el TEXTO por tres sitios (un hallazgo de menos, uno de mas y
    # ninguno) SIN TOCARLE EL ESPERADO, y exige que caiga las tres veces.
    #
    # SUJETO CONGELADO POR LA REGLA DEL PROPIO FICHERO DESDE LA VUELTA 148
    # (adjudicacion 3.5 del acta 147: "LO QUE ESTA REGLA EXIGE ES SUJETO
    # CONGELADO. EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL FIN"), y aqui hay que
    # decirlo con cuidado porque el sujeto de este arnes SI se mueve: el texto
    # sale de la medicion viva. Lo que NO se mueve es LA FORMA de la comparacion,
    # que es lo que este arnes fija, y por eso sus tres mutaciones se computan de
    # la medicion de cada dia en vez de contra un numero. El dia que el registro
    # crezca de 11 a 12, este arnes sigue valiendo sin tocarlo. Es la misma
    # doctrina que obligo a corregir a su sujeto.
    #
    # LA NOMINA NO SE PODA, CRECE (AUDITOR.md 6.1, opcion c RECHAZADA): con esta
    # entrada pasa de 88 a 89, y el reloj que eso suma se cuenta y se publica.
    ("vuelta177_tarea1b_mutacion_esperado_vivo.py", False),
    # VUELTA 177, TAREAS 1.d Y 1.e. Los otros dos arneses de esta misma vuelta.
    #
    # Y SE ANADEN A MANO PORQUE `arneses_que_faltan()` NO LOS VE, QUE ES UN
    # HALLAZGO Y NO UN TRAMITE. Medido en la vuelta 177: con la entrada de la
    # 1.b ya dentro, la ultima vuelta representada en la nomina pasa a ser 177,
    # y esa funcion solo mira los arneses de vuelta ESTRICTAMENTE POSTERIOR a la
    # ultima representada. Resultado: los dos ficheros de abajo existian, el
    # censo los veia, y `arneses_que_faltan()` devolvia LISTA VACIA. O sea que
    # EL PRIMER ARNES DE UNA VUELTA CIEGA A LOS DEMAS ARNESES DE SU MISMA
    # VUELTA. No se toca aqui: se mide, se declara y se sube en el reporte, que
    # es lo que EJECUTOR.md 5 manda cuando algo no tiene regla escrita.
    ("vuelta177_tarea1d_mutacion_cotejo.py", False),
    ("vuelta177_tarea1e_mutacion_correcciones_chicas.py", False),
    # VUELTA 177, TAREA 1.f. El tope de tramo POR MINUTOS, computado del reloj
    # medido de la corrida anterior en vez de elegido a ojo (acta 176, 7.3).
    # Su caso mas duro es el del RELOJ DESIGUAL: se le da un tramo carisimo
    # entre varios baratos, que es la forma exacta del reloj de la 176, y se
    # exige que el tamano salga del CARO y no del promedio. Con el promedio, el
    # tramo de 15,9 minutos volveria a pasar y mas gordo.
    #
    # LA NOMINA CRECE DE 91 A 92 con esta entrada.
    ("vuelta177_tarea1f_mutacion_tope_minutos.py", False),
    # VUELTA 178, LOS CUATRO ARNESES DE LA TAREA 1, Y ENTRAN EN SU MISMA VUELTA
    # POR LA LETRA DE LA 148 (un arnes entra en la nomina; la condicion es
    # SUJETO CONGELADO, no plazo) mas el acta 176 punto 7.2, que acepto que
    # entre en su misma vuelta. LOS CUATRO TIENEN SUJETO CONGELADO Y LO
    # DECLARAN EN SU DOCSTRING: los cuatro fabrican lo que miden en memoria o
    # en un temporal que retiran, y ninguno abre un fichero vivo de la campana.
    #
    # Y ESTA VEZ NO SE ANADEN A MANO A CIEGAS. La 177 los anadio a mano porque
    # `arneses_que_faltan()` no los veia; en esta misma vuelta esa ceguera
    # queda arreglada (TAREA 1.b, LA VARA DEL CENSO), asi que la funcion los
    # nombro ella sola antes de que se escribieran estas cuatro lineas.
    #
    # LA NOMINA CRECE DE 92 A 96, y NINGUNA SE PODA.
    ("vuelta178_tarea1b_mutacion_hermano.py", False),
    ("vuelta178_tarea1c_mutacion_ast.py", False),
    ("vuelta178_tarea1d_mutacion_puestos.py", False),
    ("vuelta178_tarea1e_mutacion_higiene.py", False),
    # VUELTA 178, TAREA 2.e. El resolutor de `P.1` puesto por encima del backlog
    # de OP-L-03, probado sobre un MAPA DE ALIAS FABRICADO y no sobre el vivo:
    # contra el vivo, cualquier fusion nueva moveria sus cifras y el arnes
    # saldria rojo sin que nada estuviera roto. Su caso que manda es el del
    # alias en los dos sentidos, y en su PRIMERA corrida tumbo un defecto real
    # del instrumento que probaba: contaba los pares ESCRITOS y no los
    # RESUELTOS, y por eso contaba dos veces el mismo par.
    #
    # LA NOMINA CRECE DE 96 A 97.
    ("vuelta178_tarea2_mutacion_resolutor.py", False),
    # VUELTA 178, TAREA 4.c. La columna CONSUMIDA de la vara del fundador,
    # probada sobre un EXPEDIENTE FABRICADO: ni `docs/plan/OPERACIONES.jsonl` ni
    # `dataset/nodos/` ni el grafo se leen para decidir ningun caso. Su caso que
    # manda es el del alias en los dos sentidos, igual que el de la 2.e, y su
    # primera corrida tambien tumbo un defecto real: la atribucion se buscaba en
    # la PRIMERA ventana y devolvia lista vacia teniendo la respuesta escrita
    # unos cientos de caracteres mas abajo en la misma nota.
    #
    # LA NOMINA CRECE DE 97 A 98.
    ("vuelta178_tarea4_mutacion_consumidas.py", False),
    # ------------------------------------------------------------- VUELTA 179
    # LOS DOS QUE LA VARA ARREGLADA DE LA 178 DESTAPO, Y ENTRAN AQUI PORQUE LA
    # REGLA DE ESTE MISMO FICHERO LO MANDA DESDE LA VUELTA 148 y porque la
    # nomina NO SE PODA (`AUDITOR.md` 6.1). Los dos existen en disco, los dos
    # son del censo, ninguno es anterior a la vara, y `arneses_que_faltan()` los
    # nombra desde que la 178 le quito la ceguera de los hermanos. Entran ANTES
    # de la 181 para que el rojo que la 178 anuncio no llegue a existir.
    ("vuelta150_2d_simular_op_c_05.py", False),
    ("vuelta160_tarea3b_caso_positivo.py", False),
    # VUELTA 179, TAREA 1.b. EL CASO POSITIVO DE LA GUARDA DE LA CITA DE ARNES,
    # que es la operacion de codigo de la escalada de `AUDITOR.md` 1.2. Prueba
    # `citas_de_arnes_que_no_calzan()`, `emparejar_citas()` y
    # `cifra_propia_del_arnes()`, todas PURAS y con un lector fabricado: NADA
    # SALE DEL REPO en ningun caso. Su caso que manda es el del encargo, 16
    # contra 18 en ROJO y 18 contra 18 en VERDE, y su primera corrida sobre el
    # sujeto real tumbo un defecto propio: la guarda inventaba un rojo en la
    # linea 189 de `REPORTE_V178.md` porque solo veia la palabra `casos`.
    ("vuelta179_tarea1b_mutacion_citas.py", False),
    # VUELTA 179, TAREA 3. LOS TRIANGULOS PARTIDOS POR SU FUENTE, sobre un
    # REGISTRO FABRICADO: ni `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` ni
    # `docs/plan/OP_L_03_TRIANGULOS.jsonl` se leen para decidir ningun caso.
    ("vuelta179_tarea3_mutacion_triangulos.py", False),
    # VUELTA 179, TAREA 1.d. EL CORTE DEL DENOMINADOR, cableado donde se genera
    # la cifra y no en una frase (adjudicacion 7.2 del acta 178, por `banco
    # 9.21`). `sello_de_corte()` es PURA y recibe el head, para que este arnes
    # pueda tumbarla sin llamar a git.
    #
    # LA NOMINA CRECE DE 98 A 103.
    ("vuelta179_tarea1d_mutacion_corte.py", False),
    # VUELTA 180, TAREA 1.b. LA ETIQUETA DE FUENTE QUE LEE LA VUELTA DE LA
    # FILA (adjudicacion 7.7 del acta 179). El literal clavado en la vuelta
    # 177 atribuia a la 177 cinco lecturas de la 179, contra `EJECUTOR.md` 8.
    # Su sujeto es un registro FABRICADO en un temporal con DOS vueltas
    # distintas: un registro de una sola vuelta no puede cazar esto, porque
    # con una sola vuelta el literal acierta por casualidad. No admite
    # --sujeto: fabrica el suyo.
    #
    # LA NOMINA CRECE DE 103 A 104.
    ("vuelta180_tarea1b_mutacion_etiqueta.py", False),
    # VUELTA 180, TAREA 2.c. EL CABLEADO DE LA GUARDA DEL SUJETO CONGELADO
    # AL ROJO GLOBAL (adjudicacion 7.8 del acta 179). Prueba por mutacion que
    # la pieza esta ENCHUFADA: su pieza sola enciende el rojo, y la condicion
    # VIEJA sobre el mismo escenario NO lo enciende. Su sujeto es un
    # directorio de arneses de mentira fabricado en un temporal y una nomina
    # fabricada, las dos por parametro. No admite --sujeto.
    #
    # LA NOMINA CRECE DE 104 A 105.
    ("vuelta180_tarea2c_mutacion_cableado.py", False),
    # VUELTA 180, TAREA 3. EL CORTE DE LA TABLA DE TRAMOS (hallazgo del
    # fundador, seccion 6 del acta 179, por `banco 9.21` y el punto 7.2 del
    # acta 178). Prueba que la misma tabla medida en dos cortes no se
    # confunde, que la misma cifra con dos cortes distintos tampoco, y que
    # dos cosas distintas del mismo tamano y del mismo corte tampoco, que es
    # la confusion que aparece al sacar el sello fuera de la nomina. Su
    # sujeto son tres funciones puras y unos literales fabricados: no toca
    # git, no lee ficheros y no corre nada. No admite --sujeto.
    #
    # LA NOMINA CRECE DE 105 A 106.
    ("vuelta180_tarea3_mutacion_corte_de_tramos.py", False),
    # VUELTA 180, TAREA 4. LAS DOS PENDIENTES BARATAS, que son la misma
    # especie: texto que describe una maquina. (a) El dia FABRICADO en que
    # las dos preguntas del paso 0 no coinciden, que en corrida no se ve
    # nunca porque casi siempre coinciden; (b) el dia FABRICADO en que la
    # fuente del clon desaparece, que estaba declarado en el docstring del
    # esqueleto desde la 174 y seguia sin instrumento. Todo sobre ficheros
    # fabricados en un temporal: no toca ningun fichero de la campana. No
    # admite --sujeto.
    #
    # LA NOMINA CRECE DE 106 A 107.
    ("vuelta180_tarea4_mutacion_texto_y_clon.py", False),
    # VUELTA 180, TAREA 5. EL BACKLOG DE OP-L-02 CON LA VARA RESUELTA. Prueba
    # que el resolutor de P.1 esta puesto de verdad y que los pares se cuentan
    # RESUELTOS y no ESCRITOS, que es la trampa que mordio a
    # backlog_l02_resuelto.py en su primera corrida y que su propia guarda de
    # restas cazo. Todo el material va fabricado: mapa de alias, grafo,
    # veredictos y lecturas dirigidas. No lee el archivo ni dataset/ ni
    # docs/plan/. No admite --sujeto.
    #
    # LA NOMINA CRECE DE 107 A 108.
    ("vuelta180_tarea5_mutacion_backlog_l02.py", False),
]

# CASOS DECLARADOS: exit distinto de 0 QUE NO ES UN FALLO DE LA GUARDA, con su
# motivo escrito y su fecha. Se separan de NO MORDIO porque son cosas
# CONOCIDAS, MEDIDAS Y PUBLICADAS en su vuelta, no sorpresas; pero NO se
# esconden: la bateria los imprime uno a uno con su motivo entero, y si alguno
# dejara de dar su codigo declarado, vuelve a caer como NO MORDIO.
#
# EL LIMITE, DICHO PARA QUE NO SE ABUSE: aqui SOLO entra un caso cuyo diagnostico
# esta escrito y medido en su acta o su reporte. Un rojo sin acta detras no se
# declara: se arregla o se trae como PARADA.
#
# CADA ENTRADA ES (exit_declarado, motivo, MARCA_OBLIGATORIA). La exencion solo
# vale si la salida del script TRAE ESA MARCA: si el script empieza a fallar por
# OTRA razon, la marca no aparece y vuelve a caer como NO MORDIO. La exencion es
# de UN fallo concreto, nunca del script.
CASOS_DECLARADOS = {
    "vuelta140_2a_mutaciones.py": (
        2,
        "su bloque (iii), el caso positivo sobre la fase 05, sale NO CALZA y esta "
        "DECLARADO desde la vuelta 140: el auditor lo reconocio como caida SUYA de "
        "encargo (acta 140, 4.5, 'EL AUDITOR ELIGIO MAL EL SUJETO CONGELADO'). "
        "OP-S-05, OP-S-08, OP-S-11 y OP-S-12 tienen HUELLA DE GRAFO IDENTICA (los "
        "cuatro campos vacios) y lo unico que las separa es `estado`, que el encargo "
        "prohibe mirar: NINGUNA VARA DE GRAFO PUEDE SEPARARLAS. Los bloques (i) y "
        "(ii) SI muerden y son los que esta bateria vigila.",
        "VEREDICTO (iii): NO CALZA"),
    "vuelta135_2e_mutacion_3.py": (
        1,
        "su SUJETO FIJO es el REPORTE.md de la vuelta 134, congelado por banco 9.10, y "
        "ES ANTERIOR A LOS DELIMITADORES DE CABECERA TALLADA. Medido en esta vuelta: "
        "grep -c 'CABECERA TALLADA' docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md da 0, y "
        "sobre docs/loop/REPORTE.md da 3. La ampliacion del vocabulario de la TAREA 2.a "
        "(vuelta 142) hace que la guarda vea ahora la celda '3 fila(s)' del desfase del "
        "calibrado, que EN UN REPORTE MODERNO vive DENTRO de la cabecera delimitada y "
        "queda recortada antes de parsear, y en este sujeto no, porque las marcas no "
        "existian aun. LAS DOS CIFRAS QUE ESTA MUTACION PRUEBA SI COTEJAN (la salida "
        "publica '2 POR ETIQUETA'): lo que cae es una tercera, ajena al caso. El sujeto "
        "NO se retoca, porque su valor es estar congelado.",
        "NO TIENE CONVENCION MECANICA DE CONTEO"),
}

# EL ANCLA QUE SE ARRANCA en --mutar-ancla. Es el literal que las tres buscan.
ANCLAS = ["118 grafias (sin instrumento)", "54 grupos (sin instrumento)"]


# EL CORTACIRCUITOS (vuelta 140, 2.c). Ver el docstring: `vuelta139_2b_mutaciones.py`
# corre esta bateria dentro de su bloque (ii), y esta bateria corre ese script
# desde la vuelta 140. Sin esta marca los dos se llaman sin fondo. Es ruidosa:
# el hijo DICE en su salida que omite el sub-caso por recursion.
MARCA_RECURSION = "LOOP_BATERIA_EN_CURSO"


# --- LA GUARDA SE MIRA A SI MISMA (vuelta 163, TAREA 2; adjudicacion 6.8 del
#     acta 162) --------------------------------------------------------------
#
# POR QUE NACE, Y LA CAUSA ESTA MEDIDA: EL AGUJERO SE ABRIO POR NO MIRAR. Esta
# bateria corria sus 23 y salia VERDE mientras 22 arneses nacidos despues de la
# vuelta 147 se quedaban fuera, y NADA en este fichero lo notaba. Seis actas
# seguidas publicaron "la bateria de las 23, VERDE" sin cruzar nunca esa nomina
# contra los arneses que nacian (acta 162, seccion 2, caida 2 del auditor). Un
# verde que cuenta 23 de 45 no es un verde: es un verde que no mira.
#
# QUE COMPRUEBA: que NINGUN arnes de mutacion de `scripts/loop/` POSTERIOR a la
# ultima vuelta representada en `VIEJAS` se quede fuera de `VIEJAS`. Si lo hay,
# ROJO CON SU LISTA ENTERA, no con un resumen.
#
# LAS DOS CIFRAS SE COMPUTAN, NINGUNA SE TECLEA: la nomina sale de `VIEJAS` y el
# censo del propio directorio. El dia que se anada un arnes, esta comprobacion lo
# ve sin que nadie edite una lista.
#
# POR QUE "POSTERIOR" Y NO "TODOS": porque la regla que esta guarda lleva escrita
# dentro nace en la vuelta 144 y NO DICE si alcanza a lo anterior. Los 41 arneses
# anteriores a la 148 que estan fuera se MIDEN aparte (vuelta 163, TAREA 5.b,
# `docs/loop/SALIDA_V163_T5B_PREVIOS.txt`) y NO se meten aqui por cuenta propia:
# con esa cifra delante decide quien tiene que decidir. Ensanchar la vara sin
# adjudicacion seria exactamente lo que la congelacion de `P.5.1` prohibe en su
# terreno.
# EL PUNTO CIEGO DEL CENSO, ARREGLADO EN LA FUENTE (vuelta 165, TAREA 2;
# adjudicacion 6.3 del acta 164, sobre su hallazgo 5.1).
#
# QUE ESTABA MAL, MEDIDO Y NO SUPUESTO. El patron era
# `^vuelta(\d+).*mutacion.*\.py$`: EXIGIA la palabra `mutacion` en el nombre.
# Medido por el auditor importando estas mismas funciones, y recomputado en la
# vuelta 165 antes de tocar nada: 92 arneses veia el censo, 53 entradas tiene
# la nomina, y DOS DE ESAS 53 EL CENSO NO LAS VEIA, aunque existen en disco:
# `vuelta144_3c_caso_positivo_1190.py` y `vuelta147_3e_simular_a26.py`.
#
# POR QUE NO ERA COSMETICO. `arneses_que_faltan()` es quien produce el VERDE de
# abajo, y ese verde SOLO cubria a los que se llamaran `mutacion`. El dia que
# naciera un arnes llamado como esos dos, la guarda habria dicho que no falta
# ninguno SIN HABERLO MIRADO. Es la especie que esta campana lleva cazando:
# una guarda cuya frase promete mas de lo que su patron mide.
#
# LAS DOS SALIDAS QUE LA 6.3 ADMITE SE TOMAN LAS DOS, PORQUE NINGUNA SOLA
# BASTA:
#
#   (a) EL PATRON CUBRE LO QUE LA NOMINA YA CONTIENE. `FAMILIAS_DE_ARNES` no se
#       invento: se LEYO de los nombres que la nomina real ya trae (`mutacion`,
#       `caso_positivo`, `simular`), y el arnes de mutacion COMPRUEBA que
#       ninguna familia declarada sobre. `caso_rojo` estuvo declarada un rato y
#       el arnes la TUMBO en su primera corrida: existe un
#       `vuelta88_tarea3_caso_rojo.py` en el directorio, pero NO en la nomina,
#       o sea que declararla era invento mio y no lectura. Con el patron
#       ensanchado, las
#       53 entradas de la nomina son visibles al censo: la cifra de invisibles
#       pasa de 2 a 0, y esta medida, no afirmada.
#
#   (b) LA FRASE DEL VERDE SE ESTRECHA PARA DECIR A QUE UNIVERSO SE REFIERE.
#       Ensanchar el patron mueve la frontera, no la borra: un arnes con un
#       nombre de una familia QUINTA seguiria siendo invisible. Asi que el
#       verde del cierre deja de decir "NINGUN arnes" a secas y NOMBRA las
#       familias que reconoce.
#
# Y ENCIMA VA EL INVARIANTE QUE FALTABA, QUE ES LO QUE IMPIDE QUE ESTO SE
# REPITA CON UNA FAMILIA QUE HOY NO EXISTE: `nomina_invisible_al_censo()`. UN
# CENSO QUE NO PUEDE VER SU PROPIA NOMINA ESTA CIEGO, Y ESO ES ROJO. El dia que
# alguien meta en `VIEJAS` un arnes con un nombre que este patron no reconoce,
# esta guarda PARA EN ROJO con su lista entera en vez de salir verde sin mirar.
# Esa es la unica de las tres que no caduca cuando aparezca la familia quinta.
#
# CASO POSITIVO POR MUTACION: `scripts/loop/vuelta165_tarea2_mutacion_censo.py`.
# CAE si alguien devuelve el patron a su forma vieja.
FAMILIAS_DE_ARNES = ("mutacion", "caso_positivo", "simular")
PATRON_ARNES = re.compile(
    r"^vuelta(\d+).*(?:%s).*\.py$" % "|".join(FAMILIAS_DE_ARNES))
PATRON_ARNES_VIEJO = re.compile(r"^vuelta(\d+).*mutacion.*\.py$")

# LA VARA DEL CENSO, EXPLICITA Y CON SU MOTIVO (vuelta 178, TAREA 1.b;
# adjudicacion del acta 177 punto 7.10, sobre el `PD.1` del reporte 177).
#
# QUE ERA ANTES Y POR QUE ESTABA MAL. Hasta esta vuelta la vara del censo no
# tenia nombre: vivia IMPLICITA dentro de un `>` de `arneses_que_faltan()`, que
# solo reclamaba arneses de vuelta ESTRICTAMENTE POSTERIOR a la ultima
# representada en la nomina. Ese filtro es el equivocado, y la prueba es de la
# vuelta 177: con la entrada de la 177 ya dentro de la nomina, la funcion dijo
# que NO FALTABA NINGUNO cuando faltaban CUATRO ARNESES DE LA PROPIA 177. Los
# hermanos de la misma vuelta que la ultima de la nomina eran invisibles por
# construccion, y hubo que anadirlos a mano.
#
# QUE ES AHORA, Y ES LO QUE LA REGLA ESCRITA DE ESTE MISMO FICHERO YA DECIA. La
# letra desde la vuelta 148 (TAREA 2.5, sobre la adjudicacion 3.5 del acta 147)
# dice que UN ARNES ENTRA EN LA NOMINA y que la condicion es SUJETO CONGELADO,
# no plazo; y el acta 176, punto 7.2, acepto que entre EN SU MISMA VUELTA. Con
# eso, la pregunta correcta no es "es posterior a la nomina" sino ESTA EN EL
# CENSO Y NO ESTA EN LA NOMINA.
#
# Y POR QUE LA VARA ES 148 Y NO CERO. Porque todo lo anterior a la 148 YA SE
# MIDIO Y YA SE ADJUDICO FUERA, y reclamarlo aqui seria moverle la vara a otro:
# `scripts/loop/vuelta164_tarea5_medir_pre148.py` (TAREA 5 de la vuelta 164,
# adjudicacion 6.9 del acta 163) midio con esa misma frontera, `CORTE = 148`, y
# su primer punto dice literalmente "NINGUNO ENTRA EN VIEJAS" y "NO SE AFIRMA
# QUE LA REGLA LES ALCANCE". Ensanchar la vara hacia atras sin adjudicacion
# nueva seria legislar. LA VARA SE DEJA EXPLICITA Y PARAMETRIZABLE para que su
# caso positivo por mutacion pueda moverla sin tocar este fichero.
VARA_DEL_CENSO = 148


# LA REGLA DEL SUJETO CONGELADO DEJA DE SER UNA FRASE (vuelta 178, TAREA 1.e;
# `PD.2` del reporte 176, adjudicado a favor del ejecutor en el acta 176 punto
# 7.9 con destino esta vuelta).
#
# LA REGLA EXISTE DESDE LA VUELTA 145 Y SIGUE ESCRITA ARRIBA, palabra por
# palabra: una mutacion entra en la nomina SOLO SI SU SUJETO ESTA CONGELADO, y
# la que no pueda tenerlo entra como CASO DECLARADO. Lo que NO existia es nada
# que la hiciera cumplir: la nomina admitia arneses anclados a ficheros vivos y
# nadie lo veia hasta que el registro crecia lo bastante. El rojo del tramo 6 de
# la vuelta 176 fue exactamente eso.
#
# QUE MIDE, Y ES SOBRE EL TEXTO DEL PROPIO ARNES. Un sujeto congelado deja
# HUELLA EN EL CODIGO que lo lee, y esa huella es de una de estas formas:
# fabrica su sujeto en un temporal, se hace una copia en memoria, lee un blob de
# git clavado, o apunta a un fichero `SUJETO_FIJO_*` commiteado. Un sujeto vivo
# tambien deja huella: abre por su nombre uno de los ficheros que la campana
# mueve cada vuelta.
#
# LA CLASIFICACION ES DE TRES ESTADOS Y NO DE DOS, y esa es la parte honesta: si
# un arnes trae LAS DOS huellas, esta guarda NO ADIVINA cual manda. Pide que el
# propio arnes lo declare con el literal `SUJETO CONGELADO` en su texto, que es
# lo que la casa ya escribe en los que lo tienen. Sin esa declaracion el
# veredicto es NO DECIDIBLE, y NO DECIDIBLE no es verde.
#
# LO QUE ESTA GUARDA NO HACE: no poda la nomina, no reescribe ningun arnes y no
# decide si un arnes vale. Clasifica y publica.

HUELLAS_DE_CONGELADO = (
    "SUJETO_FIJO",       # un fichero congelado y commiteado en docs/loop/
    "tempfile",          # fabrica su propio sujeto y lo retira (P.16)
    "mkdtemp",
    "deepcopy",          # copia en memoria, el original no se toca
    "git show",          # blob de git, que no se mueve
    "cat-file",
    "sha256",            # sujeto clavado por su huella de contenido
    "SUJETO CONGELADO",  # lo declara el propio arnes
)

HUELLAS_DE_VIVO = (
    "REPORTE.md",
    "INTRA_DOMINIO_VEREDICTOS.jsonl",
    "OPERACIONES.jsonl",
    "master_graph.json",
    "ACTA_AUDITOR.md",
    "LECTURAS_DIRIGIDAS.md",
)

MARCA_DECLARA_CONGELADO = "SUJETO CONGELADO"


def texto_del_arnes(nombre, directorio=None):
    """EL TEXTO DE UN ARNES, o cadena vacia si no esta. Lo unico de esta familia
    que toca disco, y se aisla aqui para que el resto sea puro."""
    ruta = os.path.join(directorio or LOOP, nombre)
    if not os.path.isfile(ruta):
        return ""
    return io.open(ruta, encoding="utf-8", errors="replace").read().replace(
        chr(13) + chr(10), chr(10))


def sin_docstring_de_modulo(texto):
    """EL TEXTO DEL ARNES SIN SU DOCSTRING DE MODULO. PURA.

    HACE FALTA Y NO ES UN ADORNO: los docstrings de esta casa son largos y
    NOMBRAN los ficheros de los que hablan. Buscar `REPORTE.md` en el texto
    entero marca como SUJETO VIVO a arneses cuyo docstring solo CUENTA que su
    sujeto es una copia congelada del reporte de otra vuelta. La huella de
    sujeto vivo tiene que buscarse EN LA MAQUINA, que es la que abre ficheros.

    Si el fichero no parsea se devuelve el texto entero, y eso es lo prudente:
    ante la duda, la guarda mira MAS y no menos."""
    try:
        arbol = ast.parse(texto)
    except (SyntaxError, ValueError):
        return texto
    if not arbol.body:
        return texto
    n0 = arbol.body[0]
    es_doc = (isinstance(n0, ast.Expr) and isinstance(n0.value, ast.Constant)
              and isinstance(n0.value.value, str))
    if not es_doc:
        return texto
    lineas = texto.split(chr(10))
    fin = (n0.end_lineno or n0.lineno)
    return chr(10).join(lineas[fin:])


def anclaje_de(texto, declarado=False):
    """EL VEREDICTO DE ANCLAJE DE UN ARNES, LEIDO DE SU TEXTO. PURA.

    Devuelve (veredicto, huellas_de_congelado, huellas_de_vivo). El veredicto es
    uno de: CASO DECLARADO, CONGELADO, SUJETO VIVO, NO DECIDIBLE.

    `declarado` dice si el arnes esta en `CASOS_DECLARADOS`, que es la exencion
    que la regla de la vuelta 145 ya preveia y la unica que hay."""
    # LA HUELLA DE CONGELADO SE BUSCA EN EL TEXTO ENTERO, porque una de ellas
    # (`SUJETO CONGELADO`) es una DECLARACION y vive en el docstring por
    # definicion. LA HUELLA DE SUJETO VIVO SE BUSCA SOLO EN LA MAQUINA, porque
    # un docstring que NOMBRA un fichero no lo abre.
    maquina = sin_docstring_de_modulo(texto)
    congela = [h for h in HUELLAS_DE_CONGELADO if h in texto]
    vive = [h for h in HUELLAS_DE_VIVO if h in maquina]
    if declarado:
        return "CASO DECLARADO", congela, vive
    if congela and not vive:
        return "CONGELADO", congela, vive
    if vive and not congela:
        return "SUJETO VIVO", congela, vive
    if congela and vive:
        if MARCA_DECLARA_CONGELADO in texto:
            return "CONGELADO", congela, vive
        return "NO DECIDIBLE", congela, vive
    return "CONGELADO", congela, vive


def anclaje_de_la_nomina(nomina=None, directorio=None, declarados=None):
    """[(nombre, veredicto, congela, vive)] para toda la nomina, en su orden.

    Semi-pura: lo unico que toca disco es leer los ficheros, y `directorio` va
    por parametro para que su caso positivo por mutacion pueda apuntarla a uno
    fabricado."""
    entradas = nomina if nomina is not None else VIEJAS
    dec = CASOS_DECLARADOS if declarados is None else declarados
    salida = []
    for nombre, _admite in entradas:
        texto = texto_del_arnes(nombre, directorio)
        v, c, vv = anclaje_de(texto, declarado=(nombre in dec))
        salida.append((nombre, v, c, vv))
    return salida


def guarda_del_sujeto_congelado(nomina=None, directorio=None, declarados=None):
    """LOS QUE NO CUMPLEN LA REGLA. Devuelve [(nombre, veredicto, vive)].

    Solo `SUJETO VIVO` y `NO DECIDIBLE` cuentan: un `CASO DECLARADO` esta exento
    por la propia regla, y un `CONGELADO` la cumple."""
    return [(n, v, vv)
            for n, v, _c, vv in anclaje_de_la_nomina(nomina, directorio, declarados)
            if v in ("SUJETO VIVO", "NO DECIDIBLE")]


def vuelta_de(nombre):
    m = re.match(r"^vuelta(\d+)", nombre)
    return int(m.group(1)) if m else None


def arneses_del_directorio(directorio=None):
    """Los arneses de mutacion que existen HOY. PURA salvo por leer el
    directorio, y con `directorio` por parametro para que el caso por mutacion
    pueda apuntarla a uno fabricado sin tocar el repo."""
    base = directorio or LOOP
    return sorted(n for n in os.listdir(base) if PATRON_ARNES.match(n))


def nomina_invisible_al_censo(nomina=None, patron=None):
    """LAS ENTRADAS DE LA NOMINA QUE EL CENSO NO PUEDE VER (vuelta 165, TAREA 2).

    ES EL INVARIANTE QUE FALTABA Y EL UNICO QUE NO CADUCA. Un censo que no
    reconoce los nombres de su propia nomina esta ciego sobre su propio
    universo, y entonces `arneses_que_faltan()` puede salir en verde sin haber
    mirado. Aqui eso deja de poder pasar en silencio: si esta lista no esta
    vacia, la corrida es ROJA.

    PURA a proposito, con `nomina` y `patron` por parametro, para que su caso
    rojo se pruebe por mutacion sin tocar este fichero ni el disco."""
    nombres = [s for s, _admite in (nomina if nomina is not None else VIEJAS)]
    pat = patron or PATRON_ARNES
    return sorted(n for n in nombres if not pat.match(n))


def arneses_que_faltan(nomina=None, directorio=None, vara=None):
    """(ultima_vuelta_de_la_nomina, los_que_faltan). PURA a proposito: recibe la
    nomina, el directorio y la vara, para que su caso rojo se pueda probar por
    mutacion sin tocar ni este fichero ni el disco.

    EL FILTRO, DESDE LA VUELTA 178: ESTA EN EL CENSO Y NO ESTA EN LA NOMINA,
    menos los anteriores a `VARA_DEL_CENSO`. El filtro viejo ("vuelta
    estrictamente posterior a la ultima de la nomina") era ciego a los hermanos
    de la misma vuelta, y esa ceguera esta MEDIDA en la vuelta 177: dijo que no
    faltaba ninguno cuando faltaban cuatro de esa misma vuelta.

    `ultima` SE SIGUE DEVOLVIENDO porque la bateria la publica, pero YA NO
    DECIDE NADA: es informativa. Quien decide es la vara, y por eso la vara
    tiene nombre, valor y motivo escrito arriba, en vez de estar escondida en un
    signo de comparacion."""
    nombres = [s for s, _admite in (nomina if nomina is not None else VIEJAS)]
    vueltas = [v for v in (vuelta_de(n) for n in nombres) if v is not None]
    ultima = max(vueltas) if vueltas else None
    v = VARA_DEL_CENSO if vara is None else vara
    dentro = set(nombres)
    fuera = [n for n in arneses_del_directorio(directorio)
             if n not in dentro and (vuelta_de(n) or 0) >= v]
    return ultima, sorted(fuera)


def prueba_de_la_nomina():
    """CASO POSITIVO POR MUTACION DE LA MIRADA SOBRE SI MISMA (vuelta 163,
    TAREA 2). Todo sobre un directorio FABRICADO en un temporal y una nomina
    FABRICADA: ni este fichero ni `scripts/loop/` se tocan. P.16, quien fabrica
    limpia.

    NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: los cinco salen de correr
    `arneses_que_faltan` sobre escenarios distintos, y la segunda pasada muta el
    valor esperado de cada uno y exige que CAIGA."""
    print("=" * 78)
    print("PRUEBA DE MUTACION DE LA MIRADA DE LA NOMINA SOBRE SI MISMA")
    print("(vuelta 163, TAREA 2; adjudicacion 6.8 del acta 162)")
    print("=" * 78)
    print("")
    tmp = tempfile.mkdtemp(prefix="v163_nomina_")
    casos = []
    try:
        for nombre in ("vuelta100_tarea1_mutacion_vieja.py",
                       "vuelta110_tarea2_mutacion_dentro.py",
                       "vuelta120_tarea3_mutacion_fuera.py",
                       "vuelta121_tarea4_mutacion_tambien_fuera.py",
                       "vuelta115_tarea9_un_script_cualquiera.py"):
            io.open(os.path.join(tmp, nombre), "w", encoding="utf-8").write("# de mentira" + chr(10))
        nomina = [("vuelta100_tarea1_mutacion_vieja.py", False),
                  ("vuelta110_tarea2_mutacion_dentro.py", False)]

        print("A) EL DIRECTORIO FABRICADO Y LA NOMINA FABRICADA")
        print("   ficheros: %s" % ", ".join(sorted(os.listdir(tmp))))
        print("   nomina:   %s" % ", ".join(n for n, _a in nomina))
        censo = arneses_del_directorio(tmp)
        print("   CIFRA arneses que el censo reconoce: %d (%s)" % (len(censo), ", ".join(censo)))
        casos.append(("el_censo_no_cuenta_lo_que_no_es_arnes", len(censo), 4))
        print("")

        print("B) LA MIRADA, CON DOS FUERA DE LA NOMINA")
        print("   (LA VARA VA EXPLICITA EN CADA LLAMADA DESDE LA VUELTA 178: este")
        print("   directorio es de mentira y sus vueltas son de mentira, asi que la")
        print("   vara real, %d, no le vale. Pasarla a mano es lo que la hace"
              % VARA_DEL_CENSO)
        print("   auditable; antes vivia escondida en un signo de comparacion)")
        ultima, faltan = arneses_que_faltan(nomina, tmp, vara=0)
        print("   ultima vuelta de la nomina: %s" % ultima)
        print("   CIFRA que faltan: %d (%s)" % (len(faltan), ", ".join(faltan)))
        casos.append(("la_ultima_vuelta_se_computa_de_la_nomina", ultima, 110))
        casos.append(("y_ve_LOS_DOS_que_faltan", faltan,
                      ["vuelta120_tarea3_mutacion_fuera.py",
                       "vuelta121_tarea4_mutacion_tambien_fuera.py"]))
        print("")

        print("C) SI ENTRAN EN LA NOMINA, DEJA DE FALTAR NADIE")
        completa = nomina + [("vuelta120_tarea3_mutacion_fuera.py", False),
                             ("vuelta121_tarea4_mutacion_tambien_fuera.py", False)]
        _u2, faltan2 = arneses_que_faltan(completa, tmp, vara=0)
        print("   CIFRA que faltan tras meterlos: %d" % len(faltan2))
        casos.append(("metidos_en_la_nomina_ya_no_faltan", len(faltan2), 0))
        print("")

        print("D) LOS ANTERIORES A LA VARA DEL CENSO NO SE RECLAMAN, Y SE DICE POR QUE")
        print("   (CAMBIA EN LA VUELTA 178, Y NO SE BORRA DE QUE IBA. La version")
        print("   vieja de este caso protegia a los anteriores a LA ULTIMA VUELTA DE")
        print("   LA NOMINA, que es justo el filtro que la 178 tumba por ciego. Lo")
        print("   que de verdad protege a los viejos es LA VARA DEL CENSO, que tiene")
        print("   nombre y motivo: la 164 los midio con CORTE = 148 y los adjudico")
        print("   fuera. Aqui la vara se pone en 121 sobre el directorio fabricado")
        print("   para probar la MISMA conducta con la palanca correcta)")
        solo_una = [("vuelta120_tarea3_mutacion_fuera.py", False),
                    ("vuelta121_tarea4_mutacion_tambien_fuera.py", False)]
        _u3, faltan3 = arneses_que_faltan(solo_una, tmp, vara=120)
        print("   con la vara en 120, faltan: %d (%s)"
              % (len(faltan3), ", ".join(faltan3) or "ninguno"))
        casos.append(("los_anteriores_a_la_vara_no_se_reclaman", len(faltan3), 0))
        print("")

        print("D.2) Y LOS HERMANOS DE LA MISMA VUELTA QUE LA ULTIMA DE LA NOMINA")
        print("     SI SE RECLAMAN, QUE ES LO QUE LA 177 DEMOSTRO QUE FALTABA")
        io.open(os.path.join(tmp, "vuelta110_tarea9_mutacion_hermana.py"), "w",
                encoding="utf-8").write("# de mentira" + chr(10))
        _u4, faltan4 = arneses_que_faltan(nomina, tmp, vara=0)
        print("     la nomina llega a la vuelta 110 y hay un arnes de la 110 fuera")
        print("     CIFRA que faltan ahora: %d (%s)" % (len(faltan4), ", ".join(faltan4)))
        casos.append(("ve_al_hermano_de_la_misma_vuelta",
                      "vuelta110_tarea9_mutacion_hermana.py" in faltan4, True))
        os.remove(os.path.join(tmp, "vuelta110_tarea9_mutacion_hermana.py"))
        print("")

        print("E) Y SOBRE EL REPO DE VERDAD, HOY")
        print("   (EL CASO SE RE-FUNDA EN LA VUELTA 178, Y SE DICE POR QUE. El caso")
        print("   viejo exigia que en el repo de hoy no faltara NINGUNO, y eso era")
        print("   una expectativa sobre el estado del repo, no sobre la conducta de")
        print("   la funcion: el dia que falte uno de verdad, ese caso cae sin que")
        print("   nada este roto. El caso nuevo comprueba LO QUE LA FUNCION HACE,")
        print("   re-derivando su resultado por conjuntos SIN LLAMARLA, que es lo")
        print("   unico que un caso puede comprobar de una funcion)")
        ultima_real, faltan_real = arneses_que_faltan()
        censo_real = arneses_del_directorio()
        dentro_real = {s for s, _a in VIEJAS}
        derivado = sorted(n for n in censo_real
                          if n not in dentro_real
                          and (vuelta_de(n) or 0) >= VARA_DEL_CENSO)
        print("   ultima vuelta de la nomina real: %s" % ultima_real)
        print("   vara del censo: %d" % VARA_DEL_CENSO)
        print("   CIFRA que la funcion dice que faltan: %d (%s)"
              % (len(faltan_real), ", ".join(faltan_real) or "ninguno"))
        print("   CIFRA re-derivada aqui por conjuntos, sin llamarla: %d"
              % len(derivado))
        casos.append(("la_funcion_calza_con_su_re_derivacion", faltan_real, derivado))
        casos.append(("la_nomina_entera_es_visible_al_censo",
                      len(nomina_invisible_al_censo()), 0))
        print("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print("   P.16: el temporal se retira. Existe todavia: %s" % os.path.exists(tmp))
        print("")

    print("F) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-46s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")
    print("G) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, list):
            mutado = esperado + ["vuelta999_de_mentira_mutacion.py"]
        else:
            mutado = esperado + 1
        cae = (real != mutado)
        print("   %-46s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    print("   CIFRA casos que CAEN: %d de %d" % (caen, len(casos)))
    print("")
    if fallos or caen != len(casos):
        print("ROJO DE LA MUTACION: la mirada sobre si misma no se comporta.")
        print("FIN")
        return 1
    print("VERDE DE LA MUTACION: %d casos, los %d pasan y los %d CAEN al mutarles el "
          "valor esperado. La mirada VE los que faltan, deja de verlos cuando entran, "
          "NO reclama los anteriores a LA VARA DEL CENSO (%d), SI VE al hermano de la "
          "misma vuelta que la ultima de la nomina, y sobre el repo de hoy su "
          "resultado calza byte a byte con su re-derivacion por conjuntos."
          % (len(casos), len(casos), len(casos), VARA_DEL_CENSO))
    print("FIN")
    return 0


def correr(script, sujeto=None, base=None):
    cmd = [sys.executable, os.path.join(base or LOOP, script)]
    if sujeto:
        cmd += ["--sujeto", sujeto]
    entorno = dict(os.environ)
    entorno[MARCA_RECURSION] = "1"
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=RAIZ, env=entorno)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


# ------------- LA SALIDA SELLADA TIENE QUE REPETIRSE (TAREA 2.f, vuelta 141)
#
# POR QUE NACE (acta de la vuelta 140, caida 4.2 del ejecutor). El auditor
# corrio esta bateria y `docs/loop/SALIDA_V135_2E_MUTACION_3.txt`, que es una
# SALIDA SELLADA y commiteada, CAMBIO SOLO: traia el nombre de un fichero
# temporal con sufijo aleatorio (`REPORTE_134_MUTACION3_xffen9vd.md` paso a
# `_xv7o8hyj`). Una salida sellada que no se repite no prueba nada, y esta
# bateria la daba por VERDE porque solo miraba el exit code.
#
# QUE COMPRUEBA DE MAS: cada mutacion vieja se corre DOS VECES SEGUIDAS y se
# comparan los ficheros que ESCRIBE. Los ficheros escritos NO SE TECLEAN: se
# computan mirando cuales cambiaron de sha256 respecto del estado de partida.
# Si alguno difiere entre la primera y la segunda corrida, es ROJO nombrandolo
# y nombrando la primera linea que difiere.


def estado_de(directorio):
    """Por cada .txt del directorio, (mtime_ns, sha256 NORMALIZADO).

    EL FICHERO ESCRITO SE DETECTA POR mtime, NO POR HASH, y el motivo importa:
    una salida sellada que se reescribe con el MISMO contenido no cambia de
    hash, y detectarla por hash la dejaria fuera de la lista de "las que
    escribe". Eso convertiria la lista en una que solo ve los ficheros rotos,
    justo al reves de lo que hace falta. El hash se guarda al lado, que es lo
    que decide si es reproducible.

    El sha256 va NORMALIZADO (CRLF y CR sueltos a LF): este repo tiene
    core.autocrlf=true y la convencion de fin de linea del sistema operativo no
    es un cambio de contenido."""
    salida = {}
    for nombre in sorted(os.listdir(directorio)):
        if not nombre.endswith(".txt"):
            continue
        ruta = os.path.join(directorio, nombre)
        if not os.path.isfile(ruta):
            continue
        with io.open(ruta, "rb") as f:
            datos = f.read().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        salida[nombre] = (os.stat(ruta).st_mtime_ns, hashlib.sha256(datos).hexdigest())
    return salida


def primera_linea_distinta(ruta_a_texto_1, ruta_a_texto_2):
    a = ruta_a_texto_1.splitlines()
    b = ruta_a_texto_2.splitlines()
    for i in range(max(len(a), len(b))):
        la = a[i] if i < len(a) else "(no hay linea)"
        lb = b[i] if i < len(b) else "(no hay linea)"
        if la != lb:
            return i + 1, la[:160], lb[:160]
    return None, None, None


def _cambios_entre_corridas(directorio, tras1, tras2, textos1, nombres):
    """Los ficheros de `nombres` cuyo CONTENIDO cambio entre la corrida 1 y la
    2, con la primera linea que difiere. Se usa dos veces: para los que el
    script escribe y para el ruido que no es de nadie."""
    salida = []
    for n in sorted(nombres):
        if tras1.get(n, (None, None))[1] == tras2.get(n, (None, None))[1]:
            continue
        texto2 = ""
        ruta = os.path.join(directorio, n)
        if os.path.isfile(ruta):
            with io.open(ruta, encoding="utf-8", errors="replace") as f:
                texto2 = f.read()
        num, la, lb = primera_linea_distinta(textos1.get(n, ""), texto2)
        salida.append((n, num, la, lb))
    return salida


def correr_dos_veces(script, directorio, sujeto=None, base=None, cenir=True):
    """Devuelve (codigo, salida, escritos, inestables, ruido). Las listas se
    COMPUTAN del directorio, nunca se teclean: `escritos` son los .txt cuyo
    mtime se movio en la primera corrida, `inestables` los ficheros QUE ESE
    SCRIPT ESCRIBE que cambiaron de CONTENIDO entre la primera y la segunda, y
    `ruido` los que cambiaron o aparecieron SIN SER DE NADIE.

    --- CORRECCION DECLARADA (vuelta 157, TAREA 5, adjudicacion 6.9 del acta
    157): LA COMPROBACION SE CINE A LOS FICHEROS QUE CADA SCRIPT ESCRIBE ---

    LO QUE ESTA FUNCION HACIA ANTES, escrito aqui en vez de borrado: computaba
    `inestables` recorriendo `sorted(set(tras1) | set(tras2))`, o sea EL
    DIRECTORIO ENTERO, y le colgaba a un script CUALQUIER fichero que apareciera
    o cambiara mientras el corria. El auditor lo demostro cayendo el (acta 157,
    caida 2 y seccion 5.3): corrio la bateria con sus instrumentos al lado y
    salio ROJO acusando a `vuelta144_2b_mutacion_giro.py` y a
    `vuelta147_2c_mutacion_vitalidad.py` por dos ficheros SUYOS que ninguno de
    los dos escribe, y la propia salida decia de los dos "salidas selladas que
    escribe: ninguna".

    LO QUE HACE AHORA: `inestables` SOLO puede contener ficheros de `escritos`,
    que es la lista que esta guarda ya computaba y ya publicaba. Lo que cambia y
    no es de nadie sale en `ruido`, se reporta APARTE y CON SU NOMBRE, y NO
    enciende el rojo de ningun script. Callarlo seria la caida contraria: falla
    ruidoso sigue vigente, lo que se arregla es A QUIEN SE NOMBRA.

    `cenir=False` reproduce EL COMPORTAMIENTO VIEJO, y existe SOLO para que
    `scripts/loop/vuelta157_tarea5c_mutacion_ruido.py` pueda probar por mutacion
    que la version vieja SIGUE saliendo roja sobre el mismo escenario. En el
    ciclo de cierre nadie lo pasa."""
    antes = estado_de(directorio)
    codigo, salida = correr(script, sujeto, base)
    tras1 = estado_de(directorio)
    escritos, textos1 = [], {}
    for n, (mt, _sha) in sorted(tras1.items()):
        if n not in antes or antes[n][0] != mt:
            escritos.append(n)
            with io.open(os.path.join(directorio, n), encoding="utf-8", errors="replace") as f:
                textos1[n] = f.read()
    correr(script, sujeto, base)
    tras2 = estado_de(directorio)
    todos = set(tras1) | set(tras2)
    suyos = set(escritos)
    if not cenir:
        # EL COMPORTAMIENTO VIEJO, entero, para el caso por mutacion.
        return (codigo, salida, escritos,
                _cambios_entre_corridas(directorio, tras1, tras2, textos1, todos), [])
    inestables = _cambios_entre_corridas(directorio, tras1, tras2, textos1, todos & suyos)
    ruido = _cambios_entre_corridas(directorio, tras1, tras2, textos1, todos - suyos)
    return codigo, salida, escritos, inestables, ruido


def clasificar(codigo, salida):
    if codigo == 0:
        return "OK"
    if "ROJO PREVIO" in salida:
        return "ANCLA PERDIDA"
    return "NO MORDIO"


def primera_linea_util(salida):
    for l in salida.splitlines():
        if l.strip():
            return l.strip()[:150]
    return "(sin salida)"


# LA PRUEBA DE MUTACION DEL COTEJO DE REPRODUCIBILIDAD (TAREA 2.f, vuelta 141).
# Fabrica DOS scripts de mentira en un directorio temporal: uno que escribe una
# salida con un valor ALEATORIO dentro y otro que escribe una salida FIJA. El
# cotejo tiene que marcar el primero como inestable y el segundo como estable.
# Ninguno de los dos toca docs/loop: escriben en el mismo directorio temporal,
# que es el que se vigila. P.16, QUIEN FABRICA LIMPIA.
SCRIPT_INESTABLE = r"""# -*- coding: utf-8 -*-
import io, os, uuid
d = os.path.dirname(os.path.abspath(__file__))
io.open(os.path.join(d, "SALIDA_DE_MENTIRA.txt"), "w", encoding="utf-8", newline="\n").write(
    "linea estable\nsufijo aleatorio: %s\n" % uuid.uuid4().hex)
"""

SCRIPT_ESTABLE = r"""# -*- coding: utf-8 -*-
import io, os
d = os.path.dirname(os.path.abspath(__file__))
io.open(os.path.join(d, "SALIDA_DE_MENTIRA.txt"), "w", encoding="utf-8", newline="\n").write(
    "linea estable\nsufijo fijo: siempre el mismo\n")
"""


def prueba_de_reproducibilidad():
    """Devuelve el exit code. Cada comprobacion compara una variable COMPUTADA
    por correr_dos_veces (la lista `inestables`), nunca un literal."""
    print("=" * 78)
    print("PRUEBA DE MUTACION DEL COTEJO DE REPRODUCIBILIDAD (TAREA 2.f, vuelta 141)")
    print("=" * 78)
    tmp = tempfile.mkdtemp(prefix="v141_2f_")
    resultados = []
    try:
        for nombre, fuente, esperado_inestable in (
                ("script_inestable.py", SCRIPT_INESTABLE, True),
                ("script_estable.py", SCRIPT_ESTABLE, False)):
            io.open(os.path.join(tmp, nombre), "w", encoding="utf-8").write(fuente)
            _c, _s, escritos, inestables, _r = correr_dos_veces(nombre, tmp, base=tmp)
            hay = bool(inestables)
            ok = (hay == esperado_inestable)
            resultados.append((nombre, hay, esperado_inestable, ok))
            print("  %-22s escribe %s | inestable=%s (esperado %s)  %s"
                  % (nombre, ", ".join(escritos) or "nada", hay, esperado_inestable,
                     "VERDE" if ok else "ROJO"))
            for n, num, la, lb in inestables:
                print("       %s, linea %s" % (n, num))
                print("          corrida 1: %s" % la)
                print("          corrida 2: %s" % lb)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print("  P.16: el directorio temporal se retira. Existe todavia: %s" % os.path.exists(tmp))

    print("")
    print("  Y AHORA SE MUTA EL ESPERADO DE CADA UNA y se re-evalua contra el MISMO")
    print("  valor obtenido: la que siga verde no puede fallar nunca.")
    no_caen = [n for n, hay, esp, _ok in resultados if hay == (not esp)]
    print("  comprobaciones: %d | verdes: %d | caen con el esperado mutado: %d"
          % (len(resultados), sum(1 for r in resultados if r[3]),
             len(resultados) - len(no_caen)))
    for n in no_caen:
        print("     NO CAE con el esperado mutado: %s" % n)
    print("")
    if all(r[3] for r in resultados) and not no_caen:
        print("VERDE DE LA MUTACION: el cotejo marca la salida aleatoria como NO")
        print("REPRODUCIBLE y deja pasar la fija, y las dos comprobaciones caen al")
        print("mutarles el esperado.")
        print("FIN")
        return 0
    print("ROJO DE LA MUTACION: el cotejo de reproducibilidad no se comporta.")
    print("FIN")
    return 1


# EL TOPE DE MINUTOS POR TRAMO (vuelta 177, TAREA 1.f; adjudicacion 7.3 del acta
# 176, que contesta el `D.3` y la `P.3` a la vez). ESTA ESCRITO AQUI Y NO SE
# ELIGE EN CADA VUELTA, que es lo que el auditor encargo con estas palabras: "el
# reparto se hara por TOPE DE MINUTOS, no por tope de entradas, y el tamano se
# computara del reloj medido de la corrida anterior".
#
# POR QUE 10 Y NO OTRO, DICHO PARA QUE SE PUEDA DISCUTIR CON LOS NUMEROS
# DELANTE, QUE SON LOS DE LA CORRIDA DE LA 176: nueve tramos, 31,9 minutos en
# total, el mas corto 1,1 y EL MAS LARGO 15,9. Un tope de 10 deja fuera ese
# 15,9, que es el unico tramo que de verdad dolio, y no parte en pedazos los
# ocho que ya cabian. Es un numero de juicio y va MARCADO COMO DISCUTIBLE en el
# reporte de la 177: lo que NO es de juicio es que el tamano se compute en vez
# de elegirse.
TOPE_DE_MINUTOS_POR_TRAMO = 10.0

PATRON_DURACION = re.compile(r"DURACION DEL TRAMO \(monotona, minutos\):\s*([\d.]+)")
PATRON_ENTRADAS = re.compile(r"CIFRA entradas de ESTE tramo:\s*(\d+)")


def reloj_de_la_corrida(texto):
    """EL RELOJ MEDIDO DE UNA CORRIDA ANTERIOR, LEIDO DE SU SALIDA. PURA.

    Recibe el TEXTO de un `SALIDA_V<N>_BATERIA.txt` y devuelve la lista de
    (entradas_del_tramo, minutos_del_tramo), en el orden en que aparecen. Lista
    vacia si el texto no trae ninguno de los dos marcadores, y eso ES el
    resultado: no se inventa un reloj.

    LOS DOS MARCADORES VIENEN DE SITIOS DISTINTOS Y SE EMPAREJAN POR ORDEN: las
    entradas las imprime esta misma bateria al abrir cada tramo y la duracion la
    imprime el lanzador al cerrarlo. Si no salen los mismos de cada uno, se
    devuelve lo que se pueda emparejar y se declara: emparejar de mas seria
    inventar un tramo."""
    entradas = [int(x) for x in PATRON_ENTRADAS.findall(texto)]
    minutos = [float(x) for x in PATRON_DURACION.findall(texto)]
    return list(zip(entradas, minutos))


def minutos_por_entrada(reloj):
    """EL COSTE POR ENTRADA, EN MINUTOS, Y ES EL MAXIMO Y NO LA MEDIA. PURA.
    Devuelve None si el reloj esta vacio o no tiene ningun tramo con entradas.

    POR QUE EL MAXIMO, QUE ES LA MITAD ENTERA DE ESTA CORRECCION. La media de la
    corrida de la 176 es 31,9 minutos entre 89 entradas, o sea 0,36 minutos por
    entrada; con la media, un tope de 10 minutos daria tramos de 27 entradas y
    EL TRAMO QUE TARDO 15,9 MINUTOS VOLVERIA A PASAR, mas gordo. El coste por
    entrada NO es uniforme: en esa misma corrida va de 0,11 a 1,59 minutos por
    entrada, catorce veces mas caro el peor que el mejor. LA VARA QUE SIRVE PARA
    NO PASARSE DE UN TOPE ES LA DEL PEOR CASO OBSERVADO, no la del caso medio.
    Es exactamente el argumento del auditor en el 7.3: "ese 15,9 contra los 4,3
    es justamente por que el numero de entradas no es la vara buena"."""
    costes = [m / e for e, m in reloj if e > 0]
    return max(costes) if costes else None


def tamano_por_minutos(reloj, tope=TOPE_DE_MINUTOS_POR_TRAMO, por_defecto=10):
    """EL TAMANO DE TRAMO, COMPUTADO DEL RELOJ MEDIDO Y NO ELEGIDO A OJO. PURA.

    Devuelve (tamano, motivo). Si no hay reloj del que computarlo devuelve el
    `por_defecto` CON SU MOTIVO ESCRITO, en vez de fingir que lo computo: una
    cifra por defecto que se disfraza de medicion es peor que una cifra elegida.

    NUNCA DEVUELVE MENOS DE 1: un tramo de cero entradas no reparte nada y
    dejaria la nomina sin correr, que es la unica cosa que la letra del fundador
    del 5 sep no permite tocar."""
    coste = minutos_por_entrada(reloj)
    if coste is None or coste <= 0:
        return por_defecto, ("SIN RELOJ QUE LEER: no se computo nada y se usa el "
                             "por defecto %d, dicho en voz alta" % por_defecto)
    tamano = max(1, int(tope / coste))
    return tamano, ("COMPUTADO: tope %.1f minutos / %.4f minutos por entrada "
                    "(el MAXIMO de %d tramo(s) medidos, no la media) = %d entradas"
                    % (tope, coste, len(reloj), tamano))


def reparto_en_tramos(nomina, tamano, reloj=None,
                      tope=TOPE_DE_MINUTOS_POR_TRAMO):
    """LA NOMINA REPARTIDA EN TRAMOS DE A LO SUMO `tamano` ENTRADAS.

    PURA: recibe la lista y el tamano, y no lee ni escribe nada. Devuelve una
    lista de listas. La union de los tramos, en orden, ES la nomina entera y en
    su mismo orden: no se cae ni se repite ninguna entrada, y eso es lo que su
    caso positivo por mutacion comprueba sobre nominas fabricadas.

    POR QUE EXISTE (vuelta 176, TAREA 1.c). La vuelta 175 murio DENTRO de la
    bateria y la causa esta medida: 87 entradas, cada una corrida DOS VECES, son
    un bloque indivisible de entre 57 y 75 minutos. LO QUE SE PARTE ES EL BOCADO,
    NO LA BATERIA: la letra del fundador del 5 sep 2026 fija CUATRO cosas (la
    cadencia de cada cinco, la soledad de la vuelta, la integridad de la corrida
    y la prohibicion de podar la nomina) y partir la corrida en tramos DENTRO de
    una misma vuelta no toca ninguna de las cuatro. Cada entrada sigue corriendo,
    y sigue corriendo dos veces.

    LO QUE UN TRAMO NO AFLOJA, Y ES LA PARTE QUE IMPORTA: la mirada de la nomina
    sobre si misma (`arneses_que_faltan()` y `nomina_invisible_al_censo()`) sigue
    corriendo SOBRE LA NOMINA ENTERA en cada tramo, y sigue encendiendo el rojo.
    Lo unico que el tramo recorta es CUANTAS ENTRADAS SE EJECUTAN en esta
    corrida, y por eso el verde de un tramo se publica como VERDE PARCIAL y dice
    a que entradas se refiere, una por una."""
    if tamano is None:
        # EL CARRIL DEL TOPE DE MINUTOS (vuelta 177, TAREA 1.f). Con `tamano` a
        # None el tamano NO SE ELIGE: se computa del reloj que se le pase. Es
        # opcional a proposito, para que las 89 llamadas viejas que pasan un
        # numero sigan llamandolo igual y sus arneses no se muevan.
        tamano, _motivo = tamano_por_minutos(reloj or [], tope)
    if tamano < 1:
        raise ValueError("el tamano de tramo tiene que ser 1 o mas, y llego %r"
                         % tamano)
    return [list(nomina[i:i + tamano]) for i in range(0, len(nomina), tamano)]


def hay_rojo_al_cierre(perdidas, no_mordio, no_reprod, faltan, invisibles, malas):
    """SI LA BATERIA CIERRA EN ROJO, DECIDIDO EN UN SOLO SITIO. PURA.

    POR QUE ES UNA FUNCION Y NO UN `if` suelto (vuelta 180, TAREA 2.c). La
    condicion del rojo global vivia dentro de `main()`, o sea que la unica forma
    de probar que una guarda nueva ESTA CABLEADA era correr la bateria entera y
    ver el color. Con la condicion aqui, su caso positivo por mutacion puede
    quitarle una pieza a la vez y comprobar que EL ROJO SE APAGA, que es la
    unica forma de demostrar que esa pieza estaba enchufada.

    Las seis piezas son listas: si alguna no esta vacia, hay rojo."""
    return bool(perdidas or no_mordio or no_reprod or faltan or invisibles or malas)


def informe_del_sujeto_congelado():
    """LA GUARDA DEL SUJETO CONGELADO, CORRIDA Y PUBLICADA (vuelta 178, TAREA
    1.e). NO corre ningun arnes, NO toca la nomina y NO reescribe nada:
    clasifica y publica.

    CAE EN ROJO si alguna entrada de la nomina sale `SUJETO VIVO` o `NO
    DECIDIBLE`. Un `NO DECIDIBLE` es rojo a proposito: la regla de la vuelta 145
    exige sujeto congelado, y un arnes que no deja claro cual es el suyo NO
    demuestra que lo cumpla. La salida verde de una guarda que no pudo mirar es
    exactamente lo que esta casa persigue."""
    print("=" * 78)
    print("LA GUARDA DEL SUJETO CONGELADO (vuelta 178, TAREA 1.e)")
    print("=" * 78)
    print("")
    print("LA REGLA, CITADA Y NO PARAFRASEADA, del docstring de este mismo fichero:")
    print("   'UNA MUTACION ENTRA EN LA VUELTA SIGUIENTE A LA QUE NACE, Y SOLO SI SU")
    print("   SUJETO ESTA CONGELADO' (vuelta 145), y desde la 148 'LO QUE ESTA REGLA")
    print("   EXIGE ES SUJETO CONGELADO. EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL")
    print("   FIN'. Existe desde la 145 y hasta hoy era una frase.")
    print("")
    print("COMO SE MIDE: por la huella que el sujeto deja EN EL CODIGO del arnes.")
    print("   huellas de CONGELADO (en el texto entero): %s"
          % ", ".join(HUELLAS_DE_CONGELADO))
    print("   huellas de VIVO (SOLO en la maquina, sin el docstring de modulo): %s"
          % ", ".join(HUELLAS_DE_VIVO))
    print("   y si trae LAS DOS, la guarda NO ADIVINA: pide que el propio arnes lo")
    print("   declare con el literal %r, y sin esa declaracion sale NO DECIDIBLE."
          % MARCA_DECLARA_CONGELADO)
    print("")

    filas = anclaje_de_la_nomina()
    cuenta = {}
    for _n, v, _c, _vv in filas:
        cuenta[v] = cuenta.get(v, 0) + 1
    print("EL REPARTO, CONTADO DE LA NOMINA VIVA")
    print("| veredicto | entradas |")
    print("|---|---|")
    for v in ("CONGELADO", "CASO DECLARADO", "SUJETO VIVO", "NO DECIDIBLE"):
        print("| %s | %d |" % (v, cuenta.get(v, 0)))
    print("| **total** | **%s** |" % sello_de_corte(len(filas), corte_de_git()))
    print("")

    malas = guarda_del_sujeto_congelado()
    print("LAS QUE NO CUMPLEN, UNA A UNA")
    if not malas:
        print("   (ninguna)")
    for nombre, veredicto, vive in malas:
        print("   %-14s %-52s abre: %s"
              % (veredicto, nombre, ", ".join(vive) or "(nada)"))
    print("   CIFRA entradas que no cumplen la regla: %d" % len(malas))
    print("")

    if malas:
        print("ROJO DE LA GUARDA DEL SUJETO CONGELADO: %d entrada(s) de %s no"
              % (len(malas), sello_de_corte(len(filas), corte_de_git())))
        print("demuestran tener sujeto congelado. La regla existe desde la vuelta")
        print("145 y esta es la primera vez que se mide, asi que este rojo NO es una")
        print("regresion: es el estado que la frase tapaba.")
        print("FIN")
        return 1
    print("VERDE DE LA GUARDA DEL SUJETO CONGELADO: las %s entradas de la nomina"
          % sello_de_corte(len(filas), corte_de_git()))
    print("demuestran sujeto congelado o son caso declarado.")
    print("FIN")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutar-ancla", dest="mutar", action="store_true")
    ap.add_argument("--mutar-nomina", dest="mutar_nomina", action="store_true",
                    help="vuelta 163, TAREA 2: prueba de mutacion de la mirada de "
                         "la nomina sobre si misma, sobre un directorio fabricado")
    ap.add_argument("--mutar-reproducibilidad", dest="mutar_repro", action="store_true",
                    help="TAREA 2.f (vuelta 141): prueba de mutacion del cotejo de "
                         "reproducibilidad, sobre dos scripts de mentira fabricados")
    ap.add_argument("--sujeto-congelado", dest="sujeto_congelado",
                    action="store_true",
                    help="vuelta 178, TAREA 1.e: LA GUARDA DEL SUJETO CONGELADO. "
                         "Clasifica la nomina entera y CAE EN ROJO si alguna "
                         "entrada tiene SUJETO VIVO o queda NO DECIDIBLE. Corre "
                         "SOLA: no corre ningun arnes y no toca la nomina.")
    ap.add_argument("--tramo", type=int, default=None,
                    help="vuelta 176, TAREA 1.c: corre SOLO el tramo numero N "
                         "(empezando en 1) del reparto de la nomina. Sin esta "
                         "opcion se corre la nomina ENTERA, como siempre.")
    ap.add_argument("--tamano-tramo", dest="tamano_tramo", type=int, default=10,
                    help="entradas por tramo. El numero de tramos NO se teclea: "
                         "se computa de la nomina y de este tamano.")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    # UN TRAMO NO SE MEZCLA CON NINGUN MODO DE MUTACION, Y SE NIEGA EN VEZ DE
    # APANARSELO. Los tres modos de mutacion comprueban la nomina ENTERA contra
    # lo que esperan (el `--mutar-ancla` exige que caigan las re-ancladas, que
    # son 3 de las 87), y correrlos sobre un pedazo daria un rojo de mentira.
    if a.tramo is not None and (a.mutar or a.mutar_nomina or a.mutar_repro):
        print("ROJO: --tramo no se mezcla con ningun modo de mutacion. Los modos de")
        print("      mutacion juzgan la nomina ENTERA, y sobre un pedazo darian un")
        print("      rojo de mentira. Corre el modo de mutacion sin --tramo.")
        return 1

    if a.mutar_repro:
        return prueba_de_reproducibilidad()

    if a.mutar_nomina:
        return prueba_de_la_nomina()

    if a.sujeto_congelado:
        return informe_del_sujeto_congelado()

    print("=" * 78)
    print("LAS %d MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO." % len(VIEJAS))
    if a.mutar:
        print("MODO MUTACION: sujeto con el ancla arrancada. TIENE QUE DAR ROJO.")
    print("=" * 78)

    # LA GUARDA SE MIRA A SI MISMA ANTES DE MEDIR NADA (vuelta 163, TAREA 2).
    # Va PRIMERO a proposito: si la nomina esta incompleta, el resto de esta
    # salida es un verde sobre una parte, y eso es lo que hay que ver arriba y
    # no enterrado al final.
    ultima_de_la_nomina, faltan_en_la_nomina = arneses_que_faltan()
    invisibles_al_abrir = nomina_invisible_al_censo()
    print("")
    print("  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)")
    print("  CIFRA entradas en la nomina: %s"
          % sello_de_corte(len(VIEJAS), corte_de_git()))
    print("  CIFRA arneses en scripts/loop/ que el censo reconoce: %d"
          % len(arneses_del_directorio()))
    print("  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros")
    print("  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en %s."
          % ", ".join(FAMILIAS_DE_ARNES))
    print("  CIFRA entradas de la nomina que el censo NO VE: %d, de %s"
          % (len(invisibles_al_abrir), sello_de_corte(len(VIEJAS), corte_de_git())))
    for n in invisibles_al_abrir:
        print("      INVISIBLE AL CENSO: %s" % n)
    print("  CIFRA ultima vuelta representada en la nomina: %s (INFORMATIVA desde la"
          " vuelta 178: ya no decide)" % ultima_de_la_nomina)
    print("  LA VARA DEL CENSO, que es la que decide: %d (vuelta 178, TAREA 1.b)"
          % VARA_DEL_CENSO)
    print("  CIFRA arneses DEL CENSO, no anteriores a la vara, que se quedan FUERA "
          "de la nomina: %d" % len(faltan_en_la_nomina))
    for n in faltan_en_la_nomina:
        print("      FUERA DE LA NOMINA: %s" % n)
    if not faltan_en_la_nomina:
        print("      (ninguno)")
    print("")

    # EL TRAMO (vuelta 176, TAREA 1.c). VA DESPUES DE LA MIRADA DE LA NOMINA
    # SOBRE SI MISMA A PROPOSITO: esa mirada NO se reparte, corre entera en cada
    # tramo y sigue encendiendo el rojo. Lo unico que el tramo reparte es cuantas
    # entradas se EJECUTAN aqui. NINGUNA CIFRA SE TECLEA: el numero de tramos
    # sale de la nomina y del tamano.
    tramos = reparto_en_tramos(VIEJAS, a.tamano_tramo)
    if a.tramo is None:
        a_correr = list(VIEJAS)
        print("  SIN --tramo: SE CORRE LA NOMINA ENTERA, como siempre.")
        print("  CIFRA entradas que se van a ejecutar en esta corrida: %d" % len(a_correr))
    else:
        if not (1 <= a.tramo <= len(tramos)):
            print("ROJO: se pidio el tramo %d y el reparto de esta nomina (%d entradas "
                  "de %d en %d) solo tiene %d tramos."
                  % (a.tramo, len(VIEJAS), a.tamano_tramo, a.tamano_tramo, len(tramos)))
            return 1
        a_correr = tramos[a.tramo - 1]
        print("  EL REPARTO EN TRAMOS (vuelta 176, TAREA 1.c). LO QUE SE PARTE ES EL")
        print("  BOCADO, NO LA BATERIA: cada entrada sigue corriendo y sigue corriendo")
        print("  DOS VECES, y la mirada de la nomina sobre si misma de aqui arriba")
        print("  corre ENTERA en este tramo y sigue encendiendo el rojo.")
        print("  CIFRA nomina entera: %s"
              % sello_de_corte(len(VIEJAS), corte_de_git()))
        print("  CIFRA tamano de tramo: %d" % a.tamano_tramo)
        print("  CIFRA tramos del reparto (computada, no tecleada): %d" % len(tramos))
        print("  CIFRA TRAMO QUE SE CORRE: %d de %d" % (a.tramo, len(tramos)))
        print("  CIFRA entradas de ESTE tramo: %d" % len(a_correr))
        print("  CIFRA suma de las entradas de TODOS los tramos: %d"
              % sum(len(t) for t in tramos))
        for s, _admite in a_correr:
            print("      ENTRADA DEL TRAMO: %s" % s)
    print("")

    sujeto = None
    tmp = None
    try:
        if a.mutar:
            if not os.path.exists(SUJETO_FIJO):
                print("ROJO: no existe el sujeto fijo %s." % SUJETO_FIJO)
                return 1
            tmp = tempfile.mkdtemp(prefix="ancla_arrancada_")
            texto = io.open(SUJETO_FIJO, encoding="utf-8").read()
            arrancadas = 0
            for ancla in ANCLAS:
                if ancla in texto:
                    texto = texto.replace(ancla, "CIFRA ARRANCADA POR LA PRUEBA DE MUTACION")
                    arrancadas += 1
            print("  anclas arrancadas de la copia: %d de %d" % (arrancadas, len(ANCLAS)))
            if arrancadas != len(ANCLAS):
                print("ROJO: el sujeto fijo no traia las %d anclas. PARADA." % len(ANCLAS))
                return 1
            sujeto = os.path.join(tmp, "SUJETO_CON_EL_ANCLA_ARRANCADA.md")
            io.open(sujeto, "w", encoding="utf-8", newline="\n").write(texto)
            print("  copia con el ancla arrancada: %s" % sujeto)

        filas = []
        inestables_todas = []
        ruido_todo = []
        # EL CRONOMETRO (vuelta 164, TAREA 2.a; adjudicacion 6.8 del acta 163).
        # POR QUE NACE: esta nomina paso de 23 a 51 entradas en la vuelta 163 y
        # cada entrada se corre DOS VECES (el cotejo de reproducibilidad de la
        # TAREA 2.f de la 141), o sea que la bateria hace mas del doble de
        # trabajo que su cifra sugiere. El auditor la lanzo dos veces en la 163
        # y no termino: la primera la corto un `timeout 900` SIN UNA SOLA LINEA
        # DE VEREDICTO. Una guarda que el cierre corre en cada vuelta y que
        # puede tardar veinte minutos necesita su reloj publicado, o el
        # siguiente que la lance la matara creyendo que colgo. Se mide con
        # `time.perf_counter`, que es monotono, y NO con la hora del reloj.
        reloj = {}
        t0 = time.perf_counter()
        for script, admite_sujeto in a_correr:
            t_uno = time.perf_counter()
            usar = sujeto if (a.mutar and admite_sujeto) else None
            if a.mutar:
                # En modo mutacion el sujeto es una copia con el ancla arrancada:
                # lo que se prueba es el ANCLA, no la reproducibilidad.
                codigo, salida = correr(script, usar)
                escritos, inestables, ruido = [], [], []
            else:
                codigo, salida, escritos, inestables, ruido = correr_dos_veces(
                    script, DOCS_LOOP, usar)
                for nombre, num, la, lb in ruido:
                    # ADJUDICACION 6.9 DEL ACTA 157, PUNTO (b): lo que cambia en
                    # docs/loop/ y NO ES DE NADIE no se calla y no se le cuelga a
                    # nadie. Se acumula aqui y se publica APARTE, con su nombre.
                    ruido_todo.append((script, nombre, num, la, lb))
            estado = clasificar(codigo, salida)
            # CASO DECLARADO (TAREA 2.d, vuelta 142): un exit conocido, medido y
            # publicado en su vuelta deja de contarse como NO MORDIO, PERO SE
            # IMPRIME CON SU MOTIVO ENTERO. Si el codigo deja de ser el
            # declarado, vuelve a caer como NO MORDIO: la exencion es de UN
            # codigo concreto, no del script.
            declarado = CASOS_DECLARADOS.get(script)
            if (declarado and codigo == declarado[0] and estado == "NO MORDIO"
                    and declarado[2] in salida):
                estado = "CASO DECLARADO"
            if inestables:
                estado = "NO REPRODUCIBLE"
                for nombre, num, la, lb in inestables:
                    inestables_todas.append((script, nombre, num, la, lb))
            reloj[script] = time.perf_counter() - t_uno
            filas.append((script, codigo, estado, primera_linea_util(salida), escritos))
        total_segundos = time.perf_counter() - t0
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)
            print("  P.16: la copia temporal se retira. Existe todavia: %s" % os.path.exists(tmp))

    print("")
    for script, codigo, estado, prim, escritos in filas:
        print("  %-38s exit %d  %-16s %7.1fs"
              % (script, codigo, estado, reloj.get(script, 0.0)))
        if not a.mutar:
            print("      salidas selladas que escribe (computadas, no tecleadas): %s"
                  % (", ".join(escritos) or "ninguna"))
        if estado not in ("OK",):
            print("      %s" % prim)

    # EL CRONOMETRO SE PUBLICA (vuelta 164, TAREA 2.a; adjudicacion 6.8 del acta
    # 163). Todas las cifras se COMPUTAN de `reloj`, ninguna se teclea, para que
    # el dia que la nomina crezca no quede una frase mintiendo detras.
    print("")
    print("  EL CRONOMETRO (adjudicacion 6.8 del acta 163)")
    print("  CIFRA arneses cronometrados: %d" % len(reloj))
    print("  CIFRA TIEMPO TOTAL de la bateria, en segundos: %.1f" % total_segundos)
    print("  CIFRA TIEMPO TOTAL de la bateria, en minutos: %.1f" % (total_segundos / 60.0))
    if reloj:
        orden = sorted(reloj.items(), key=lambda kv: -kv[1])
        print("  CIFRA arnes MAS LENTO: %s con %.1fs" % (orden[0][0], orden[0][1]))
        print("  CIFRA arnes MAS RAPIDO: %s con %.1fs" % (orden[-1][0], orden[-1][1]))
        print("  CIFRA mediana por arnes, en segundos: %.1f"
              % sorted(reloj.values())[len(reloj) // 2])
        print("  CIFRA arneses que pasan de 30 segundos: %d"
              % len([v for v in reloj.values() if v > 30]))
        print("  LOS DIEZ MAS LENTOS, DE MAS A MENOS:")
        for nombre, seg in orden[:10]:
            print("      %-42s %7.1fs" % (nombre, seg))
        print("  AVISO DE RELOJ: cada entrada se corre DOS VECES (el cotejo de")
        print("  reproducibilidad de la TAREA 2.f de la vuelta 141), asi que el tiempo")
        print("  de cada arnes YA INCLUYE sus dos corridas. Quien la lance tiene que")
        print("  darle al menos este total con holgura: matarla antes NO es un rojo,")
        print("  es no haberla medido.")

    perdidas = [s for s, _, e, _, _ in filas if e == "ANCLA PERDIDA"]
    no_mordio = [s for s, _, e, _, _ in filas if e == "NO MORDIO"]
    no_reprod = [s for s, _, e, _, _ in filas if e == "NO REPRODUCIBLE"]
    print("")
    print("  ANCLA PERDIDA  : %d (%s)" % (len(perdidas), ", ".join(perdidas) or "ninguna"))
    print("  NO MORDIO      : %d (%s)" % (len(no_mordio), ", ".join(no_mordio) or "ninguna"))
    print("  NO REPRODUCIBLE: %d (%s)" % (len(no_reprod), ", ".join(no_reprod) or "ninguna"))
    declarados = [s for s, _, e, _, _ in filas if e == "CASO DECLARADO"]
    print("  CASO DECLARADO : %d (%s)" % (len(declarados), ", ".join(declarados) or "ninguna"))
    for s in declarados:
        print("      %s, exit declarado %d, marca obligatoria %r:"
              % (s, CASOS_DECLARADOS[s][0], CASOS_DECLARADOS[s][2]))
        print("         %s" % CASOS_DECLARADOS[s][1])
    for script, nombre, num, la, lb in inestables_todas:
        print("      %s: %s cambia SOLO entre dos corridas, linea %s" % (script, nombre, num))
        print("         corrida 1: %s" % la)
        print("         corrida 2: %s" % lb)

    # ADJUDICACION 6.9 DEL ACTA 157, PUNTO (b). EL RUIDO DE CONCURRENCIA SE
    # PUBLICA APARTE Y CON SU NOMBRE, Y NO ENCIENDE EL ROJO DE NADIE. La cuenta
    # se computa de `ruido_todo`, no se teclea, para que el dia que crezca no
    # deje una frase mintiendo detras.
    sueltos = sorted({n for _s, n, _num, _a, _b in ruido_todo})
    print("  RUIDO DE CONCURRENCIA: %d fichero(s) (%s)"
          % (len(sueltos), ", ".join(sueltos) or "ninguno"))
    if sueltos:
        print("      cambian en docs/loop/ mientras la bateria corre y NO LOS ESCRIBE")
        print("      NINGUN script de la nomina. NO son de nadie y NO son rojo de nadie:")
        print("      son la senal de que esta bateria se corrio con algo al lado, y por")
        print("      regla de la casa SE CORRE SOLA.")
        for script, nombre, num, la, lb in ruido_todo:
            print("      aparecio durante %s: %s, linea %s" % (script, nombre, num))

    if a.mutar:
        esperadas = [s for s, admite in VIEJAS if admite]
        bien = sorted(perdidas) == sorted(esperadas)
        print("")
        if bien:
            print("VERDE DE LA MUTACION: las %d re-ancladas caen como ANCLA PERDIDA cuando se"
                  % len(esperadas))
            print("les arranca el ancla, y el veredicto de esta guarda seria ROJO.")
            print("FIN")
            return 0
        print("ROJO DE LA MUTACION: se esperaban %d ANCLA PERDIDA (%s) y salieron %d (%s)."
              % (len(esperadas), ", ".join(esperadas), len(perdidas), ", ".join(perdidas)))
        print("FIN")
        return 1

    # LA MIRADA SOBRE SI MISMA CUENTA PARA EL ROJO (adjudicacion 6.8 del acta
    # 162). Se recomputa AQUI, al cierre de la corrida, y no se hereda de la
    # cabecera: el estado al cierre se mide al cierre.
    _ultima, faltan_al_cierre = arneses_que_faltan()
    invisibles_al_cierre = nomina_invisible_al_censo()
    # LA GUARDA DEL SUJETO CONGELADO ENTRA AL ROJO GLOBAL (vuelta 180, TAREA 2.c;
    # adjudicacion 7.8 del acta 179). NACIO EN LA VUELTA 178 CORRIENDO SOLA, con
    # --sujeto-congelado, y por eso nadie la miraba en el ciclo de cierre.
    #
    # Y NO SE CABLEO ANTES A PROPOSITO, que es la parte que importa: al abrir la
    # 180 esta guarda daba 17 de 103. Cablearla ese dia habria puesto la bateria
    # de la 181 en un ROJO PERMANENTE, y un rojo permanente es un rojo que todo
    # el mundo aprende a ignorar, o sea degradacion silenciosa del `banco 9`. EL
    # ORDEN FUE: los trece declararon (TAREA 2.a), los cuatro se congelaron
    # (TAREA 2.b), la guarda dio 0, Y SOLO ENTONCES se cablea.
    #
    # SE RECOMPUTA AQUI, AL CIERRE, y no se hereda de ninguna cifra de arriba:
    # el estado al cierre se mide al cierre.
    malas_al_cierre = guarda_del_sujeto_congelado()
    print("  CIFRA arneses DEL CENSO, no anteriores a la vara %d, que se quedan "
          "FUERA de la nomina (recomputado al cierre): %d"
          % (VARA_DEL_CENSO, len(faltan_al_cierre)))
    for n in faltan_al_cierre:
        print("      FUERA DE LA NOMINA: %s" % n)
    print("  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): "
          "%d, de %s"
          % (len(invisibles_al_cierre), sello_de_corte(len(VIEJAS), corte_de_git())))
    for n in invisibles_al_cierre:
        print("      INVISIBLE AL CENSO: %s" % n)
    print("  CIFRA entradas cuyo SUJETO NO ESTA CONGELADO (recomputado al cierre): "
          "%d, de %s"
          % (len(malas_al_cierre), sello_de_corte(len(VIEJAS), corte_de_git())))
    for nombre, veredicto, vive in malas_al_cierre:
        print("      SUJETO SIN CONGELAR: %-42s %-14s abre %s"
              % (nombre, veredicto, ", ".join(vive) or "(ninguno)"))
    if not malas_al_cierre:
        print("      (ninguna)")

    if hay_rojo_al_cierre(perdidas, no_mordio, no_reprod, faltan_al_cierre,
                          invisibles_al_cierre, malas_al_cierre):
        print("")
        if invisibles_al_cierre:
            print("ROJO: %d entrada(s) de esta nomina tienen un nombre que el censo de "
                  "este mismo fichero NO RECONOCE, asi que `arneses_que_faltan()` no "
                  "puede haber mirado su familia y su verde no cubriria lo que dice. "
                  "Ensancha FAMILIAS_DE_ARNES o renombra el arnes. La lista entera: %s"
                  % (len(invisibles_al_cierre), ", ".join(invisibles_al_cierre)))
        if faltan_al_cierre:
            print("ROJO: %d arnes(es) que el censo VE y que la nomina NO tiene, "
                  "nacidos en la vuelta %d o despues, se quedan FUERA. La regla "
                  "escrita en este mismo fichero desde la vuelta 148 dice que UN "
                  "ARNES ENTRA EN LA NOMINA, y el acta 176 punto 7.2 acepto que "
                  "entre EN SU MISMA VUELTA. La lista entera: %s"
                  % (len(faltan_al_cierre), VARA_DEL_CENSO,
                     ", ".join(faltan_al_cierre)))
        if malas_al_cierre:
            print("ROJO: %d entrada(s) de la nomina NO tienen su sujeto congelado. La "
                  "regla es de la vuelta 145 y su condicion la fijo la 148: una "
                  "mutacion entra en la nomina SOLO SI SU SUJETO ESTA CONGELADO, y "
                  "la que no pueda tenerlo entra como CASO DECLARADO. Un arnes "
                  "anclado a un fichero que la campana mueve cada vuelta no mide su "
                  "maquina, mide el dia. La lista entera: %s"
                  % (len(malas_al_cierre),
                     ", ".join(n for n, _v, _vv in malas_al_cierre)))
        if perdidas or no_mordio or no_reprod:
            print("ROJO: %d con el ancla perdida, %d que no mordieron y %d cuya salida "
                  "sellada NO SE REPITE." % (len(perdidas), len(no_mordio), len(no_reprod)))
        print("FIN")
        return 1
    print("")
    # EL VERDE DE UN TRAMO ES UN VERDE PARCIAL Y LO DICE CON ESAS PALABRAS
    # (vuelta 176, TAREA 1.c). NO puede usar la frase de abajo, porque esa dice
    # "las N mutaciones viejas corren y muerden" y en un tramo NO han corrido
    # todas. Un verde que dijera de mas seria exactamente la especie de caida
    # que la casa lleva persiguiendo desde la vuelta 74.
    if a.tramo is not None:
        print("VERDE PARCIAL DEL TRAMO %d DE %d: las %d entradas DE ESTE TRAMO corren, "
              "muerden y sus salidas selladas salen IDENTICAS en dos corridas "
              "seguidas. LAS OTRAS %d ENTRADAS DE LA NOMINA NO SE HAN CORRIDO AQUI, y "
              "este verde NO dice nada de ellas: lo dira la composicion de los %d "
              "tramos. Lo que SI cubre entero este tramo es la mirada de la nomina "
              "sobre si misma: sus %d entradas son TODAS visibles al censo, TODAS "
              "tienen su sujeto congelado y NINGUN "
              "fichero de scripts/loop/ con nombre `vuelta<N>...<familia>...py` "
              "(familias: %s) de la vuelta %d o posterior se queda fuera de la nomina."
              % (a.tramo, len(tramos), len(filas), len(VIEJAS) - len(filas),
                 len(tramos), len(VIEJAS), ", ".join(FAMILIAS_DE_ARNES),
                 VARA_DEL_CENSO))
        print("FIN")
        return 0

    # LA FRASE DEL VERDE DICE EXACTAMENTE A QUE UNIVERSO SE REFIERE (vuelta 165,
    # TAREA 2, salida (b) de la adjudicacion 6.3 del acta 164). Antes decia
    # "NINGUN arnes posterior" a secas, y solo miraba a los que se llamaran
    # `mutacion`. Ahora NOMBRA las familias que el censo reconoce y declara,
    # ademas, que la nomina entera es visible al censo, que es la comprobacion
    # que impide que este verde vuelva a ser un verde que no mira.
    print("VERDE: las %d mutaciones viejas corren, muerden, sus salidas selladas "
          "salen IDENTICAS en dos corridas seguidas, las %d entradas de la nomina "
          "son TODAS visibles al censo, TODAS tienen su SUJETO CONGELADO desde la "
          "vuelta 180, y NINGUN fichero de scripts/loop/ con nombre "
          "`vuelta<N>...<familia>...py` (familias: %s) de la vuelta %d o posterior se "
          "queda fuera de la nomina. Un arnes con un nombre de OTRA familia seguiria "
          "sin verse, y por eso la comprobacion de visibilidad de la nomina es ROJO. "
          "Los anteriores a la vara %d NO se reclaman, y el motivo esta escrito donde "
          "la vara: la 164 los midio y los adjudico fuera."
          % (len(filas), len(VIEJAS), ", ".join(FAMILIAS_DE_ARNES), VARA_DEL_CENSO,
             VARA_DEL_CENSO))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
