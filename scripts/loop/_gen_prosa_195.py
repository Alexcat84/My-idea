# -*- coding: utf-8 -*-
"""SEGUNDO PASO DEL GENERADOR DE UN SOLO USO: cambia LA PROSA DEL ENCABEZADO del
esqueleto de la 195, que el clon trae todavia con el regimen de la 194 (vuelta de
bateria, TRES sub-tareas). Se borra al cerrar la vuelta."""
import io

p = 'scripts/loop/vuelta195_esqueleto_reporte.py'
src = io.open(p, encoding='utf-8').read()

ini = src.index('> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA')
fin = src.index('**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**')

nueva = '''> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta%(v)d_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA NO ES VUELTA DE BATERIA.** `AUDITOR.md` 6.1, decision del fundador del 5
> sep 2026: la bateria corre **CADA CINCO VUELTAS** en una vuelta propia **que no
> lleva nada mas**, **la 194 la corrio entera por sus diez tramos** y **la proxima
> cae en la 199**. **La seccion 9 de este reporte cierra con el HUECO DECLARADO Y
> MEDIDO** por el carril de la TAREA 1.b de la vuelta 173, con su medicion, su
> atribucion y su corrida. **Un hueco declarado no es un hueco escondido.**
>
> **VAN CUATRO SUB-TAREAS Y DOS SON BLOQUEANTES.** El tope de CINCO esta ganado y
> **la cifra se conto del instrumento en esta vuelta**, no se heredo: el bloque `E`
> del sello de apertura corrio `scripts/loop/vuelta%(ant2)d_racha_de_cierres.py`
> sobre el inventario ENTERO. `AUDITOR.md` 6.2 pedia DOS vueltas seguidas cerrando
> su propio reporte con `cerrar_reporte.py`.
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. Esas eran las dos caidas `C.1` y
> `C.2` que el reporte de la 194 se declaro en su seccion 8.1, heredadas dos
> vueltas seguidas por clonar el bloque sin leer esa seccion, que es lo que su
> propia `C.3` nombraba como causa. **Aqui se leyo la seccion 8.1 ANTES de clonar.**
> **El desfase de calibrado se midio DENTRO del bloque de apertura y ANTES de la
> primera operacion.**
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina**, ni **la bateria entera**, que no es su
> vuelta y cae en la 199. **Y siguen fuera, nombradas para que la 196 no las
> redescubra:** el desfase de `PATRONES_ACTA`, **que el encargo de la 195 pasa
> EXPRESAMENTE a la 196 y EN PRIMER LUGAR DE LA COLA**, con su motivo dicho (las
> cuatro de hoy atacan causas y esa es cosmetica de cabecera); la fila de credito
> del acta con su rotulo arreglado **en el instrumento que la talla**; la guarda de
> codigo del hallazgo `5.3` del acta 194 (mensajes de commit sin clases por puesto
> ni reparto de ciega), **que a mano YA FUNCIONA Y ESTA MEDIDO** y cuya guarda
> durable sigue pendiente; `acumulan()` que lea la tabla o que declare en su salida
> que no es la sede; el cotejo de clon declarado que separa sentencia de codigo de
> cambio de texto; la excepcion que publica siempre su lista; la medicion del censo
> de arneses con carril de mutacion sin fichero propio; las ocho actas sin entrada
> propia en la serie (173 a 180), medidas y no arregladas; que el campo `evidencia`
> de `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE MUEVE: sigue
> en `LISTA`**; y **QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO**, nombrado y medido
> y **no resuelto, porque mover una clase es del RECOMPUTO**.
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**.

'''

src = src[:ini] + nueva + src[fin:]

# LA CABECERA DE LA SECCION 1 CUENTA CUATRO TAREAS, NO TRES.
src = src.replace('## 1. LAS TRES TAREAS DEL ENCARGO, Y SU ESTADO',
                  '## 1. LAS CUATRO TAREAS DEL ENCARGO, Y SU ESTADO')

# LA NOTA DEL DESFASE DE LA SECCION 0 APUNTA A LA 196, NO A LA 195.
viejo = ('  reporte de la 184, adjudicado a favor con reparacion encargada por la `5.2` del\n'
         '  acta 185, **y el acta 193 lo dejo expresamente DESPUES de la bateria de la 194:\n'
         '  la 195 es el sitio, y el encargo de esta vuelta lo repite**. Lo que si se puede')
nuevo = ('  reporte de la 184, adjudicado a favor con reparacion encargada por la `5.2` del\n'
         '  acta 185, **y el encargo de esta vuelta lo pasa EXPRESAMENTE a la 196 y EN\n'
         '  PRIMER LUGAR DE LA COLA**, con su motivo dicho. Lo que si se puede')
assert viejo in src
src = src.replace(viejo, nuevo)

io.open(p, 'w', encoding='utf-8', newline='\n').write(src)
print("PROSA CAMBIADA (%d bytes)" % len(src.encode('utf-8')))
