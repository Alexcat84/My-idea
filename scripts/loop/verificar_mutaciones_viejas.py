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


def arneses_que_faltan(nomina=None, directorio=None):
    """(ultima_vuelta_de_la_nomina, los_que_faltan). PURA a proposito: recibe la
    nomina y el directorio, para que su caso rojo se pueda probar por mutacion
    sin tocar ni este fichero ni el disco."""
    nombres = [s for s, _admite in (nomina if nomina is not None else VIEJAS)]
    vueltas = [v for v in (vuelta_de(n) for n in nombres) if v is not None]
    if not vueltas:
        return None, []
    ultima = max(vueltas)
    dentro = set(nombres)
    fuera = [n for n in arneses_del_directorio(directorio)
             if n not in dentro and (vuelta_de(n) or 0) > ultima]
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
        ultima, faltan = arneses_que_faltan(nomina, tmp)
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
        _u2, faltan2 = arneses_que_faltan(completa, tmp)
        print("   CIFRA que faltan tras meterlos: %d" % len(faltan2))
        casos.append(("metidos_en_la_nomina_ya_no_faltan", len(faltan2), 0))
        print("")

        print("D) LOS ANTERIORES A LA ULTIMA VUELTA NO SE RECLAMAN, Y SE DICE POR QUE")
        print("   (la regla de esta bateria nace en la vuelta 144 y no dice si")
        print("   alcanza a lo anterior: ensancharla sin adjudicacion seria")
        print("   moverle la vara a nadie)")
        solo_una = [("vuelta120_tarea3_mutacion_fuera.py", False),
                    ("vuelta121_tarea4_mutacion_tambien_fuera.py", False)]
        _u3, faltan3 = arneses_que_faltan(solo_una, tmp)
        print("   con la nomina en la vuelta 121, faltan: %d (%s)"
              % (len(faltan3), ", ".join(faltan3) or "ninguno"))
        casos.append(("los_anteriores_no_se_reclaman", len(faltan3), 0))
        print("")

        print("E) Y SOBRE EL REPO DE VERDAD, HOY")
        ultima_real, faltan_real = arneses_que_faltan()
        print("   ultima vuelta de la nomina real: %s" % ultima_real)
        print("   CIFRA que faltan de verdad: %d (%s)"
              % (len(faltan_real), ", ".join(faltan_real) or "ninguno"))
        casos.append(("en_el_repo_de_hoy_no_falta_ninguno", len(faltan_real), 0))
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
          "no reclama los anteriores a su vara, y sobre el repo de hoy no falta "
          "ninguno." % (len(casos), len(casos), len(casos)))
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutar-ancla", dest="mutar", action="store_true")
    ap.add_argument("--mutar-nomina", dest="mutar_nomina", action="store_true",
                    help="vuelta 163, TAREA 2: prueba de mutacion de la mirada de "
                         "la nomina sobre si misma, sobre un directorio fabricado")
    ap.add_argument("--mutar-reproducibilidad", dest="mutar_repro", action="store_true",
                    help="TAREA 2.f (vuelta 141): prueba de mutacion del cotejo de "
                         "reproducibilidad, sobre dos scripts de mentira fabricados")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    if a.mutar_repro:
        return prueba_de_reproducibilidad()

    if a.mutar_nomina:
        return prueba_de_la_nomina()

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
    print("  CIFRA entradas en la nomina: %d" % len(VIEJAS))
    print("  CIFRA arneses en scripts/loop/ que el censo reconoce: %d"
          % len(arneses_del_directorio()))
    print("  EL UNIVERSO DEL CENSO, NOMBRADO (vuelta 165, TAREA 2): ficheros")
    print("  `vuelta<N>...<familia>...py` de scripts/loop/, con familia en %s."
          % ", ".join(FAMILIAS_DE_ARNES))
    print("  CIFRA entradas de la nomina que el censo NO VE: %d" % len(invisibles_al_abrir))
    for n in invisibles_al_abrir:
        print("      INVISIBLE AL CENSO: %s" % n)
    print("  CIFRA ultima vuelta representada en la nomina: %s" % ultima_de_la_nomina)
    print("  CIFRA arneses POSTERIORES a esa vuelta que se quedan FUERA: %d"
          % len(faltan_en_la_nomina))
    for n in faltan_en_la_nomina:
        print("      FUERA DE LA NOMINA: %s" % n)
    if not faltan_en_la_nomina:
        print("      (ninguno)")
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
        for script, admite_sujeto in VIEJAS:
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
    print("  CIFRA arneses POSTERIORES a la nomina que se quedan FUERA (recomputado "
          "al cierre): %d" % len(faltan_al_cierre))
    for n in faltan_al_cierre:
        print("      FUERA DE LA NOMINA: %s" % n)
    print("  CIFRA entradas de la nomina que el censo NO VE (recomputado al cierre): "
          "%d" % len(invisibles_al_cierre))
    for n in invisibles_al_cierre:
        print("      INVISIBLE AL CENSO: %s" % n)

    if perdidas or no_mordio or no_reprod or faltan_al_cierre or invisibles_al_cierre:
        print("")
        if invisibles_al_cierre:
            print("ROJO: %d entrada(s) de esta nomina tienen un nombre que el censo de "
                  "este mismo fichero NO RECONOCE, asi que `arneses_que_faltan()` no "
                  "puede haber mirado su familia y su verde no cubriria lo que dice. "
                  "Ensancha FAMILIAS_DE_ARNES o renombra el arnes. La lista entera: %s"
                  % (len(invisibles_al_cierre), ", ".join(invisibles_al_cierre)))
        if faltan_al_cierre:
            print("ROJO: %d arnes(es) de mutacion nacidos despues de la vuelta %s se "
                  "quedan FUERA de esta nomina, y la regla escrita en este mismo "
                  "fichero dice que una mutacion entra en la vuelta SIGUIENTE a la que "
                  "nace, no mas tarde. La lista entera: %s"
                  % (len(faltan_al_cierre), _ultima, ", ".join(faltan_al_cierre)))
        if perdidas or no_mordio or no_reprod:
            print("ROJO: %d con el ancla perdida, %d que no mordieron y %d cuya salida "
                  "sellada NO SE REPITE." % (len(perdidas), len(no_mordio), len(no_reprod)))
        print("FIN")
        return 1
    print("")
    # LA FRASE DEL VERDE DICE EXACTAMENTE A QUE UNIVERSO SE REFIERE (vuelta 165,
    # TAREA 2, salida (b) de la adjudicacion 6.3 del acta 164). Antes decia
    # "NINGUN arnes posterior" a secas, y solo miraba a los que se llamaran
    # `mutacion`. Ahora NOMBRA las familias que el censo reconoce y declara,
    # ademas, que la nomina entera es visible al censo, que es la comprobacion
    # que impide que este verde vuelva a ser un verde que no mira.
    print("VERDE: las %d mutaciones viejas corren, muerden, sus salidas selladas "
          "salen IDENTICAS en dos corridas seguidas, las %d entradas de la nomina "
          "son TODAS visibles al censo, y NINGUN fichero de scripts/loop/ con nombre "
          "`vuelta<N>...<familia>...py` (familias: %s) posterior a la vuelta %s se "
          "queda fuera de la nomina. Un arnes con un nombre de OTRA familia seguiria "
          "sin verse, y por eso la comprobacion de visibilidad de la nomina es ROJO."
          % (len(filas), len(VIEJAS), ", ".join(FAMILIAS_DE_ARNES), _ultima))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
