# -*- coding: utf-8 -*-
"""_v199_parche_t1b_arnes197.py . PARCHE DE UN SOLO USO sobre el arnes de la
TAREA 2 de la vuelta 197, para que su sandbox aisle TAMBIEN los sellos y para
anadirle el caso que la mitad `1.b` de la vuelta 199 hace nacer. NINGUN esperado
se afloja y ningun escenario se quita: se anade uno."""
import io
import os

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
p = os.path.join(RAIZ, "scripts", "loop",
                 "vuelta197_tarea2_mutacion_orden_del_turno.py")
s = io.open(p, encoding="utf-8").read()


def sub(v, n):
    global s
    assert s.count(v) == 1, (s.count(v), v[:80])
    s = s.replace(v, n)


# 1. EL SANDBOX SE COMPLETA: `AP.LOOP` TAMBIEN SE REDIRIGE.
sub('''    tmp = tempfile.mkdtemp(prefix="v197_orden_turno_")
    ruta_original = AP.RUTA_DEL_TURNO
    try:
        AP.RUTA_DEL_TURNO = os.path.join(tmp, "_TURNO_DEL_AUDITOR.json")
        ok &= _caso(w, "AP.RUTA_DEL_TURNO ya NO apunta a la sede de verdad",
                    AP.RUTA_DEL_TURNO == ruta_original, False)''',
    '''    tmp = tempfile.mkdtemp(prefix="v197_orden_turno_")
    ruta_original = AP.RUTA_DEL_TURNO
    loop_original = AP.LOOP
    try:
        AP.RUTA_DEL_TURNO = os.path.join(tmp, "_TURNO_DEL_AUDITOR.json")
        # EL SANDBOX SE COMPLETA EN LA VUELTA 199, TAREA 1.b, Y SE DECLARA.
        # Este arnes prometia en su docstring *"TODO SOBRE UN TEMPORAL"*, y era
        # verdad a medias: `AP.LOOP` seguia apuntando a `docs/loop/` de verdad.
        # Mientras `puede_leer_reporte()` solo mirara el disco CON `vuelta`, eso
        # no se notaba. Desde que la 199 la hace mirar el disco TAMBIEN SIN
        # `vuelta`, una llamada a secas dentro de este arnes leia los sellos
        # REALES de la sede. Se redirige, y con eso la promesa del docstring pasa
        # a ser cierta.
        AP.LOOP = tmp
        ok &= _caso(w, "AP.RUTA_DEL_TURNO ya NO apunta a la sede de verdad",
                    AP.RUTA_DEL_TURNO == ruta_original, False)
        ok &= _caso(w, "y AP.LOOP tampoco apunta a docs/loop de verdad",
                    AP.LOOP == loop_original, False)
        vacio = os.path.join(tmp, "sin_sellos")
        os.makedirs(vacio)''')

# 2. EL CASO QUE LA `1.b` HACE NACER, ANADIDO Y NO SUSTITUIDO.
sub('''        AP.olvidar_todo()
        ok &= _caso(w, "SIN sello: SI puede leer el reporte, y eso no se prohibe",
                    AP.puede_leer_reporte()[0], True)''',
    '''        AP.olvidar_todo()
        # EL CASO ORIGINAL DE LA 197, CON SU PREMISA HECHA CIERTA. Decia
        # *"SIN sello: SI puede leer"*, y su premisa era que el turno no tuviera
        # sello. Desde la 199 *sin sello* significa SIN SELLO EN NINGUN SITIO, ni
        # en memoria ni en disco, asi que se mide contra un directorio SIN
        # SELLOS. **Es la mitad que impide que la guarda sea una pared**, y sigue
        # entera: lo que cambia es donde se mira, no lo que se espera.
        ok &= _caso(w, "SIN sello EN NINGUN SITIO: SI puede leer, y no se prohibe",
                    AP.puede_leer_reporte(base=vacio)[0], True)
        # Y EL CASO QUE LA VUELTA 199 HACE NACER, ANADIDO Y NO SUSTITUIDO: sin
        # sello en MEMORIA pero CON el sello EN DISCO, la guarda YA MUERDE. Antes
        # de la 199 esta misma llamada devolvia True, y por ahi se le escapo el
        # sujeto al auditor de la 198.
        ok &= _caso(w, "SIN sello en memoria pero CON sello EN DISCO: ya NO puede",
                    AP.puede_leer_reporte()[0], False)''')

# 3. LA RESTAURACION DE `AP.LOOP`, EN EL MISMO SITIO QUE LA DE LA RUTA.
sub('''        AP.olvidar_todo()
        AP.RUTA_DEL_TURNO = ruta_original
        shutil.rmtree(tmp, ignore_errors=True)''',
    '''        AP.olvidar_todo()
        AP.RUTA_DEL_TURNO = ruta_original
        AP.LOOP = loop_original
        shutil.rmtree(tmp, ignore_errors=True)''')

sub('''        ok &= _caso(w, "y AP.RUTA_DEL_TURNO vuelve a su sede",
                    AP.RUTA_DEL_TURNO == ruta_original, True)''',
    '''        ok &= _caso(w, "y AP.RUTA_DEL_TURNO vuelve a su sede",
                    AP.RUTA_DEL_TURNO == ruta_original, True)
        ok &= _caso(w, "y AP.LOOP vuelve a docs/loop de verdad",
                    AP.LOOP == loop_original, True)''')

io.open(p, "w", encoding="utf-8", newline=NL).write(s)
print("PARCHEADO: %s" % p)
