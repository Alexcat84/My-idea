# Hallazgos, pila 3 (lote 4): cacería sobre las capturas de la app viva

Defectos y derivas reales vistos en los 20 PNG del encargo. Sin rediseños:
solo lo que la app debería corregir o el fundador decidir.

## H1 · "digitos" sin tilde en la activación con app

En `23_cuenta_qr_desktop.png`, el paso 2 dice "Escribe el código de 6 digitos".
Falta la tilde: **dígitos**. Es exactamente la familia de faltas del lote 3;
el detector de acentos debería cazarla en el copy de /cuenta.

## H2 · El marcador del rescate tiene 13 X para un código de 12

En `24_desafio_rescate_desktop.png` y `24_desafio_rescate_mobile.png` el campo
muestra 13 marcas X. Los códigos de rescate de `23_cuenta_rescates` tienen 12
caracteres hex. Una X sobra; el canon 24 usa 12 exactas.

## H3 · Colisión de layout al confirmar borrado de idea en 380

En `23_cuenta_borrar_idea_mobile.png` la confirmación inline se monta sobre la
fila: el nombre de la idea desaparece y la fecha ("19 jul 2026") se parte
detrás de "¿Borrarla para siempre?". En el canon 23 la confirmación baja a su
propia línea bajo el nombre en 380: el título nunca se tapa.

## H4 · Guion largo en el copy del no invitado

En `15v2_login_no_invitado` la app dice "escríbele a quien te compartió el
enlace — guardamos tu lugar con gusto". La ley de voz es cero guiones largos.
El canon 15 v2 propone copy sin guion y con la lista única de las dos puertas.

## H5 · La marca del nav va en minúscula: "My idea"

Las capturas de /cuenta muestran "My idea" (i minúscula) en el nav, mientras
el login y el canon completo dicen "My Idea". Una marca, una grafía.

## H6 · "Tus Números, por dentro" cambió de vocabulario en la app

`07v3_potenciadores_packs` dice "3 escenarios: prudente, esperado y optimista"
y "8 unidades al mes". El canon (14 y 19, la vara de los dos veredictos) dice
**Pesimista / Base / Techo de capacidad** y habla de ventas. Si el fundador
renombró los escenarios, hay que propagarlo a 14 y 19 con decisión explícita;
si no, la app derivó.

## H7 · En 07v3 desaparecieron piezas que nadie decidió matar

En la captura ya no están ni la tabla "Lo que cuesta cada cosa" ni el chip
verde "cortesía de bienvenida" del saldo, y el chip de los mundos dice
"Preview gratis" en vez de "Explóralo gratis". El encargo solo decidió el
catálogo de packs. El canon 07 v3 conserva esas piezas tal cual el lote 3;
confirmar si su ausencia en la app es decisión o regresión.
