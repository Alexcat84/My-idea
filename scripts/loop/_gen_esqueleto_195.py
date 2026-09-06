# -*- coding: utf-8 -*-
"""GENERADOR DE UN SOLO USO del esqueleto de la vuelta 195, escrito aparte para
que el clon se vea como lo que es: una transformacion declarada del fichero de la
194 con tres cambios nombrados (docstring, VUELTA y TAREAS). Se borra al cerrar
la vuelta; su producto es scripts/loop/vuelta195_esqueleto_reporte.py."""
import io

src = io.open('scripts/loop/vuelta194_esqueleto_reporte.py', encoding='utf-8').read()

# ------------------------------------------------ 1. EL DOCSTRING
ini = src.index('r"""')
fin = src.index('"""', ini + 4) + 3
doc_nuevo = r'''r"""vuelta195_esqueleto_reporte.py . EL ESQUELETO DEL REPORTE DE LA VUELTA 195,
TALLADO EN LA APERTURA Y EN SU PROPIO COMMIT PARA QUE UNA VUELTA CORTADA DEJE
REPORTE PARCIAL Y NO VACIO.

CLON DECLARADO de scripts/loop/vuelta194_esqueleto_reporte.py. Cambia el numero
de vuelta, la lista TAREAS (que sube de TRES filas a CUATRO), este docstring y el
bloque de prosa del encabezado, porque ESTA VUELTA NO ES DE BATERIA.

Y LA SECCION 8.1 DE LA FUENTE SE LEYO ANTES DE CLONAR, que es lo que su propia
`C.3` reclamaba: un clon declarado hereda tambien los defectos declarados de su
fuente. Los dos defectos que aquella seccion nombra viven en el BLOQUE DE
APERTURA y no aqui, y estan arreglados en scripts/loop/vuelta195_apertura.py.

ESTA VUELTA NO ES DE BATERIA (AUDITOR.md 6.1, decision del fundador del 5 sep
2026): la bateria corre CADA CINCO VUELTAS en una vuelta propia QUE NO LLEVA NADA
MAS, la 194 la corrio entera por sus diez tramos y la proxima cae en la 199. Su
seccion 9 cierra con EL HUECO DECLARADO Y MEDIDO por el carril de la TAREA 1.b de
la vuelta 173, con su medicion, su atribucion y su corrida.

LA FUNCION PURA VA CLONADA A PROPOSITO, Y SE DECLARA:
vuelta_del_reporte_del_arbol esta copiada de vuelta174_esqueleto_reporte.py en
vez de importada, y la guarda que CAE EN ROJO si esa fuente desaparece la
escribio la TAREA 4.b de la vuelta 180: corre aqui como PASO 0.0.

LO QUE ESTE FICHERO NO HACE: no talla la tabla de comprobaciones. Esa la talla
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 195 AL CIERRE.

LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1): rama por
git rev-parse --abbrev-ref HEAD; commit del acta por las DOS formas del titulo y
en las DOS pasadas de TALLADOR.buscar_acta; HEAD de apertura leido de
docs/loop/SALIDA_V195_HEAD_APERTURA.txt, sellado antes de la primera operacion;
commit de nacimiento del bloque de apertura por git log --diff-filter=A. Si
alguno no se puede leer o es ambiguo, el esqueleto CAE EN ROJO y no escribe nada.

EL DESFASE DE PATRONES_ACTA NO SE REPARA AQUI, Y ES DECISION DEL AUDITOR Y NO UN
OLVIDO MIO: apunta al acta de VUELTA - 1 y el acta que ORDENA esta vuelta es la
195. El encargo de la 195 lo pasa EXPRESAMENTE a la 196 y EN PRIMER LUGAR DE LA
COLA, con su motivo escrito: las cuatro sub-tareas de hoy atacan causas y esta es
cosmetica de cabecera. LA CIFRA DEL ORDINAL SIGUE LLEVANDO SU FECHA DE CORTE, por
banco 9.21.

USO:
  python scripts/loop/vuelta195_esqueleto_reporte.py
"""'''
src = src[:ini] + doc_nuevo + src[fin:]

# ------------------------------------------------ 2. LA CONSTANTE
src = src.replace('VUELTA = 194', 'VUELTA = 195', 1)

# ------------------------------------------------ 3. LAS TAREAS
ini = src.index('TAREAS = [')
fin = src.index('\n]\n', ini) + 3
t1 = ('LOS REGISTROS. BLOQUEANTE. El acta 195 entra en la serie con el numero que '
      'devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado. La '
      'entrada registra, y cada cifra se cuenta del cuerpo acotado del acta: LAS '
      'DIEZ ADJUDICACIONES `4.1` a `4.10`, y LAS DIEZ A FAVOR (siete son los '
      'discutibles `D.1` a `D.7` del reporte de la 194 y las tres restantes son '
      'las preguntas `P.1`, `P.2` y `P.3`, dos contestadas por extension citable '
      'con la cita comprobada contra su fichero), CERO EN CONTRA y es la QUINTA '
      'acta seguida; LOS TRES HALLAZGOS DE LA SECCION 5 que no salen de ningun '
      'discutible (`5.1` la fila de credito del acta 194 que rotula mal su cifra, '
      '`5.2` el rojo de la bateria que SI es reparable, `5.3` `--componer` que '
      'publica VERDE sobre diez tramos rojos); CERO CAIDAS DEL EJECUTOR EN LA '
      'VUELTA 194, de cifra publicada y de reporte, con LA RACHA DE REPORTE '
      'VUELTA A CERO desde el 1 que dejo el acta 194, y SIN ESCALADA QUE '
      'ENCARGAR, dicho expresamente para que no se lea como olvido; UNA CAIDA '
      'PROPIA DEL AUDITOR, `C.1`, DE METODO (leer `clase` y `razon` del archivo '
      'con `json` a mano en vez de por `AP.marcador()` y `AP.leer_veredictos()`, '
      'que es la cuarta puerta y ya ofrecia las dos cosas sin coste), con el '
      'sujeto NO quemado y probado DESPUES por la propia puerta: 30 de 30 '
      'sellados vuelven TAPADOS y 0 destapes apuntados; LA METRICA DE CREDITO de '
      'la seccion 7 con sus cifras, incluida la fila de puestos (30 aislados, 30 '
      'cotejados, CERO QUEMADOS, que es la diferencia con la 194 y se debe a que '
      'los mensajes de commit del ejecutor ya no publican clases por puesto: ESO '
      'FUNCIONO); y LA FILA DE CAIDAS PROPIAS PARTIDA EN DOS, las que ACUMULAN y '
      'el total del cuerpo, que es el remedio del hallazgo `5.1` aplicado por el '
      'auditor a su propia tabla. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se '
      'prueba re corriendolo, con la sede medida en bytes antes y despues')
t2 = ('LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. BLOQUEANTE, Y ES DEUDA SUYA '
      'QUE PAGA EL EJECUTOR CON EL INSTRUMENTO. `AUDITOR.md` 1.2: dos '
      'discrepancias del auditor cayeron FUERA de su marcado, `654` y `719`, asi '
      'que EL CREDITO DE SU TANDA BAJA Y EL TRAMO SE RELEE AL DOBLE. El tramo y '
      'el doble estan CERRADOS DESDE ANTES, computados y no tecleados, en '
      '`docs/loop/_auditor_v195_doble_para_la_196.txt`, para que no se elijan '
      'despues de mirar. (a) `vecinos()` SE IMPORTA de '
      '`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y NO se copia, con '
      '`evitar` cargado de TODO lo consumido y contado de sus ficheros; el solape '
      'con el tramo y con el universo tiene que salir CERO POR CONSTRUCCION, no '
      'por suerte. (b) LEER LOS 60 A CIEGAS, tramo y doble, con '
      '`aislador_de_ciega.py`, y escribir las clases ANTES de abrir el destape. '
      '(c) LA VARA ES `docs/BANCO_DE_TEXTOS.md` `9.6.1`, citada por numero y no '
      'parafraseada, Y CON EL ERROR DEL AUDITOR PUESTO: la vara de '
      'contenido-manda es EL SUELO, NO EL TECHO, y antes de aplicarla se pregunta '
      'si el par pertenece a una familia con REGLA PROPIA ya fijada, porque '
      'entonces manda la especifica (el `719` se perdio por no preguntarlo: hay '
      'regla fijada en el puesto `595` con el `580` de precedente vivo). (d) NO '
      'SALTARSE LA `B`: el auditor emitio CERO `B` en 30 pares y el archivo tenia '
      'una, el `654`. (e) PUBLICAR EL COTEJO con sus cifras (cuantos coinciden, '
      'cuantos discrepan, y cuales caen dentro y fuera del marcado), con los '
      'discutibles marcados ANTES de saber si se acierta')
t3 = ('EL ROJO DE LA BATERIA, ATACADO EN SU CAUSA. Es el hallazgo `5.2` del acta '
      '195 y la adjudicacion de la pregunta `P.2` del reporte de la 194. LO '
      'RESERVADO AL FUNDADOR ES PODAR LA NOMINA, NO HACERLA CRECER: la opcion '
      '`c` que rechazo el 5 sep 2026 era JUBILAR ARNESES VIEJOS, que es lo '
      'contrario de anadir, y el NO TOQUES LA NOMINA de los encargos anteriores '
      'se escribio para VUELTAS DE BATERIA y contra LA PODA. (a) LOS SEIS QUE EL '
      'CENSO VE Y LA NOMINA NO TIENE ENTRAN EN LA NOMINA, cada uno CON SU SUJETO '
      'CONGELADO y cotejado contra su blob de git, RECONTADOS del instrumento al '
      'empezar. (b) EL QUE NO PUEDA TENER SUJETO CONGELADO ENTRA COMO CASO '
      'DECLARADO, con su marca. (c) LAS TRES ENTRADAS SIN SUJETO CONGELADO que ya '
      'estan dentro (`vuelta186_tarea2c_mutacion_cierre_tardio.py`, '
      '`vuelta187_tarea4_mutacion_dos_convenciones.py`, '
      '`vuelta188_tarea4_mutacion_cobertura_parejas.py`, las tres ancladas a '
      '`REPORTE.md` VIVO) se resuelven POR LA MISMA REGLA: o se les congela el '
      'sujeto, o pasan a CASO DECLARADO con su marca. (d) '
      '`vuelta172_tarea5_mutacion_cierre.py` NO MUERDE desde la 189: se arregla '
      'para que caiga cuando tiene que caer, o se declara rota con su motivo '
      'medido. (e) NO SE PODA NADA: la nomina solo crece. (f) AL CERRAR, LA '
      'BATERIA SOLO SOBRE LO QUE SE TOCO, para comprobar que el rojo atacado se '
      'apago, PUBLICANDO LA CIFRA de arneses fuera de la nomina y de entradas sin '
      'sujeto congelado, y NO la bateria entera, que no es su vuelta. (g) CON SU '
      'CASO POSITIVO POR MUTACION, que pruebe lo que falla hoy: que la mirada de '
      'la nomina sobre si misma CAIGA cuando un arnes que el censo ve se queda '
      'fuera de la nomina sin ser caso declarado')
t4 = ('`--componer` DEJA DE PUBLICAR VERDE SOBRE DIEZ ROJOS. Es el hallazgo `5.3` '
      'del acta 195 y la otra mitad de la pregunta `P.3` del reporte de la 194: '
      '`SALIDA_V194_BATERIA_COMPUESTA.txt` termina en VERDE, los 10 tramos '
      'cubren la nomina entera, con exitcode 0, mientras los diez tramos traen '
      '`CLASE DEL VEREDICTO: ROJO POR FALLO` y exitcode 1. Es cierto EN LO QUE '
      'MIDE, la cobertura, y enganoso EN LO QUE PARECE DECIR, el estado de la '
      'bateria; banco `9.1`, el instrumento debe caerse en vez de mentir. (a) '
      '`--componer` PROPAGA EL PEOR VEREDICTO DE LOS TRAMOS a su propio exitcode '
      'y a su linea final: cobertura entera y algun tramo en rojo NO es VERDE. '
      '(b) LAS DOS COSAS SE SIGUEN DICIENDO POR SEPARADO, la cobertura con su '
      'cifra y el veredicto con la suya, porque que propague el rojo no puede '
      'borrar que la cobertura estaba completa. (c) CON SU CASO POSITIVO POR '
      'MUTACION, con la salida de la 194 de sujeto congelado, que es el caso '
      'real: diez tramos rojos con cobertura 127 de 127 tienen que dar ROJO')
bloque = 'TAREAS = [\n'
for n, t in (("1", t1), ("2", t2), ("3", t3), ("4", t4)):
    bloque += '    ("%s", %r),\n' % (n, t)
bloque += ']\n'
src = src[:ini] + bloque + src[fin:]

io.open('scripts/loop/vuelta195_esqueleto_reporte.py', 'w',
        encoding='utf-8', newline='\n').write(src)
print("ESCRITO scripts/loop/vuelta195_esqueleto_reporte.py (%d bytes)"
      % len(src.encode('utf-8')))
