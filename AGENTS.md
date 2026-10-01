# AGENTS.md — reglas de proceso para este repo

Reglas que se ganaron por un incidente real, no por precaución teórica.
Cada una lleva su origen para que quede claro por qué existe.

## Tests numéricos: el cálculo canónico se escribe antes que el assert

**Regla:** toda función nueva de `engine/calculadora.py` (o cualquier
módulo determinista de cálculo) requiere que su escenario canónico de
prueba se calcule primero A MANO — en el prompt de la tarea o en un
comentario dentro del test — y el assert se escribe contra ESE cálculo
manual, nunca contra lo que la función ya devuelve.

**Por qué:** en el hotfix v2.1.1, `escenarios_capacidad` tenía un bug real
(`ingreso_perdido_estimado` multiplicaba unidades no atendidas por
*margen* en vez de *precio*, subestimando 5x el costo de oportunidad de
una sobredemanda). El test original pasaba porque su assert
(`ingreso_perdido_estimado == 170`) fue escrito leyendo la salida de la
función, no calculando el escenario de forma independiente — el test
verificaba que la implementación fuera consistente consigo misma, no que
fuera correcta. Es el equivalente numérico de escribir el criterio de
aceptación después de ver el resultado: no prueba nada.

**Cómo aplicarla:** antes de escribir `assert resultado == X`, escribe en
un comentario el cálculo manual completo, paso a paso, con las mismas
cifras del escenario de prueba (ej. `costo = 8 + 4×15 = 68`). El valor `X`
del assert sale de ese comentario, no de correr la función y copiar lo
que imprimió. Si el cálculo manual y la función no coinciden, el bug está
en la función — nunca ajustes el cálculo manual para que coincida con la
función.

## Ningún test puede cambiar de veredicto según secretos ambientales

**Regla:** ningún test de ninguno de los dos motores (`engine/test_*.py`,
`web/**/*.test.ts`) puede pasar o fallar dependiendo de si hay secretos
reales en el ambiente (`.env`, API keys). Un test que mockea una llamada
(`pm.llamar_claude = ...`, un cliente falso) debe garantizar que el mock
se ejercite siempre — si el código de producción tiene una guardia tipo
`if not API_KEY: return None` antes de llegar al mock, el test debe
neutralizar esa guardia explícitamente (ej. `pm.API_KEY = "test-fake-key"`),
no asumir que el ambiente donde corre ya tiene la key real. Excepción
explícita: un test puede `skip` (no fallar ni pasar con un resultado
falso) cuando depende de una API real y no quiere mock — ese es un modo
distinto y declarado (`describe.runIf(...)`), no un veredicto oculto.

**Por qué:** en el Hotfix v2.2.2, `test_reporte_tipo_oferta.py` parecía
fallar (`AssertionError: producto_fisico`) tanto en clones limpios como en
una bisección contra un commit anterior — una auditoría concluyó que era
un bug real de persistencia del guardián GIGO, semanas en rojo sin que
nadie lo notara. Era un falso positivo: `_clasificar_oferta` tiene
`if not API_KEY: return None, None` antes de invocar `llamar_claude`, así
que sin `.env` el mock del test nunca se ejecutaba y la reclasificación
nunca disparaba — el código de producción siempre fue correcto. El
"bug" solo existía en el ambiente de prueba, no en el producto, y sobrevivió
sin ser detectado porque nada obligaba a correr los tests sin secretos.

**Cómo aplicarla:** al escribir un test que mockea una llamada a IA,
verifica primero (grep la función real) si existe alguna guardia
`if API_KEY` / `if not API_KEY` entre la entrada de la función y la
llamada mockeada. Si existe, neutralízala explícitamente en el test.
Verifica corriendo el test en un clon sin `.env` antes de darlo por
bueno, no solo en tu propio ambiente de desarrollo.

## Ningún commit con alguna de las dos suites en rojo

**Regla:** antes de cualquier commit, ambas suites deben pasar en verde:
`pnpm vitest run` (dentro de `web/`) y `python engine/run_all_tests.py`
(corredor único que descubre y corre todo `engine/test_*.py`, sale con
código != 0 si algo falla). Verificar ambas es parte del ritual de cierre
de cualquier tarea, no un paso opcional.

**Por qué:** el lado Python nunca tuvo un corredor único — los tests eran
scripts sueltos que se corrían a mano, uno por uno. Así es como
`test_reporte_tipo_oferta.py` pudo estar roto (bajo la causa de la regla
anterior) sin que nadie lo supiera: no había un solo comando cuyo exit
code pudiera fallar un CI o bloquear un commit. El lado web ya tenía este
control (`vitest` como portero implacable); el lado Python no.

## Ninguna credencial en archivos versionados, ni siquiera de desarrollo

**Regla:** ningún archivo trackeado por git puede contener contraseñas,
API keys, tokens ni ningún otro secreto — tampoco los "de desarrollo"
("es solo el dev user local" no es excepción). Los secretos viven en el
`.env` raíz (ignorado por git) y el código los lee del entorno, fallando
con un mensaje claro si faltan. Una credencial que llegó a estar
committeada se considera QUEMADA: se rota inmediatamente, no basta con
borrarla del archivo (queda en el historial de git para siempre).

**Por qué:** en la Fase 3.2, la contraseña del dev user de los arneses
de prueba vivió committeada en `scripts/setup_dev_user.py` y
`web/scripts/_shared/http.ts`. Combinada con la anon key de Supabase
(pública por diseño: viaja en el bundle del navegador), cualquiera con
acceso al historial del repo podía loguearse como ese usuario en el
deployment real — con cuota exenta, además, hasta el hotfix que apagó la
exención en producción. El review de seguridad automático lo marcó; la
cura completa fue mover la contraseña a `VUELO_DEV_PASSWORD` en el
entorno Y rotarla en Supabase Auth (`scripts/setup_dev_user.py` ahora
rota en vez de solo crear).

**Cómo aplicarla:** antes de commitear, si un valor da acceso a algo
(login, API, storage), va al `.env` y el código lo lee con
`os.environ` / `process.env` + fallo explícito si falta. Al detectar un
secreto ya committeado: (1) sacarlo del código, (2) rotarlo en el
servicio de origen, (3) verificar que el flujo sigue vivo con el valor
nuevo — en ese orden, el mismo día.

## Ningún libro ni autor llega al cliente; las fuentes son metadato interno

**Regla (REGLA ESTRICTA del fundador, 26 sep 2026):** ningún título de libro ni
nombre de autor como FUENTE llega a nada que vea el cliente: ni a una pantalla,
ni a un documento, ni a un correo, ni a una respuesta de la IA. Las fuentes
viven SOLO en metadatos internos: el campo `fuente` de cada nodo, su
`fuentes_internas` (todos los libros de los que viene, fusiones incluidas), el
registro `correcciones`, `dataset/metadata/fuentes_canonicas.json`,
`vigencia.json` y el inventario interno `docs/internos/INVENTARIO_FUENTES.md`.
Un método se nombra y se explica (los cinco porqués, el ciclo PDCA, el diagrama de
Ishikawa) y, si tiene nombre neutro, se usa ese (D5 de REGLAS_DE_LA_CASA, 1 oct 2026); una cita a un autor o a un libro como
fuente ("según Blank", "en su libro") no, y si aparece en el texto de un nodo
sale por corrección declarada (veredicto ATRIBUCION de
`scripts/fidelidad/aplicar_correcciones.py`), sin cambiar el sentido.

**Por qué:** el 26 sep 2026 el aviso de vigencia salió a producción como
"Según [libro], [año]", dictado por la auditoría del hilo. El fundador lo
corrigió el mismo día: el producto habla por sí mismo; lo que respalda cada
nodo es trabajo interno, no bibliografía que se le recita al cliente. Y lo
interno no viaja al navegador (decisión del 27 sep 2026): antes de esa fecha
la copia del grafo en web/ llevaba `fuente`, las correcciones con sus citas y la
procedencia de las fusiones, y las instrucciones de la IA iban en el paquete
del navegador.

**Cómo aplicarla:**
- En las SUPERFICIES DE NAVEGACIÓN (el riel del árbol, el cintillo de la
  tarjeta, cualquier lista de nodos) y en todo texto de cara al cliente, un
  nodo se nombra por su `etiqueta_arbol` (4-5 palabras, segunda persona). El
  helper único es `etiquetaArbol(nid, graph)` en `web/lib/engine/graph.ts`.
  El `titulo_concepto` NO se pinta en ninguna parte (no hay "detalle con su
  fuente"): es material interno para la IA, y no se modifica por doctrina.
  La opción de emergencia y el plan sin IA también van por la etiqueta.
- La IA recibe en TODA llamada el bloque fijo `REGLA_SIN_FUENTES`
  (`web/lib/reglaSinFuentes.ts`), que `bloquesDeSistema` pone después del
  prompt cacheado. Ninguna llamada arma su sistema por otro camino.
- Lo que se copia a web/ es la VISTA WEB de cada asset
  (`scripts/sync_assets_web.py`): sin `fuente`, `fuentes_internas`,
  `correcciones` ni `merged_originals`; vigencia solo con el año; jurisdicción
  solo con país y clase. Un componente de cliente jamás importa el grafo, las
  instrucciones de la IA ni las listas curadas.
- Guardas: la GUARDA ÚNICA DE PROCEDENCIA `web/lib/procedencia.test.ts` (desde
  el 30 sep 2026 junta las cuatro que había: ningún título en un texto de cara al
  cliente, nada interno en los assets ni en el paquete del cliente, la regla en
  toda llamada a la IA, ningún aviso que revele el origen; y añade el prefijo de
  procedencia, las atribuciones genéricas y los once idiomas) y
  `engine/test_fuentes_internas.py` (`fuentes_internas` completas y al día).
- Un libro nuevo entra a `fuentes_canonicas.json` con sus títulos antes que su
  primer nodo; una fusión nueva corre `python scripts/fuentes_internas.py`.

## Los precios viven en precios.ts; nada más los define (ni canon, ni comentarios)

**El principio (palabra del fundador):** *el crédito paga el trabajo del motor.
Toda acción que invoca la API para pensar cobra su precio de catálogo; el cálculo
determinístico y el registro de avance son gratis, siempre.*

**Regla:** la única fuente de verdad de los precios (créditos por concepto)
es `web/lib/precios.ts` — respaldada por el canon de cobro de
`docs/FLUJO_TRACKING.md §5` y los seis puntos de la ETAPA 2. **Nada más define un
precio:** ni el canon visual (`docs/diseno-canon/`, sus mockups y su
`REGLAS_Y_TOKENS.md`), ni **un comentario de código**. Todos ellos **reflejan**
`precios.ts`; jamás lo contradicen. Cualquier divergencia —un mockup, un
comentario, una nota— se resuelve **a favor de `precios.ts`** y se corrige la
fuente divergente; si viene de una entrega de diseño, se reporta como **errata**,
no como cambio de política.

**Por qué:** en la adopción del canon 2.0 (2026-07-17), la tabla de créditos de
Design (`REGLAS_Y_TOKENS.md §3`) decía "Seguimiento core: Gratis (es el bucle
del viaje principal)". Nadie autorizó ese cambio: `precios.ts` dice
`seguimiento: 2` y `FLUJO_TRACKING §5` dice "2 core / 2 mundo". Un mockup no es
una decisión de negocio; dejar que un HTML redefina un precio por descuido es
cómo una política se cambia sin que nadie la cambie. (El mismo error se había
colado en un comentario de `follow/route.ts` y en `FLUJO_TRACKING §9` en la Fase
4.2 — mi drift, propagado a Design al entregarle ese documento; las tres
corregidas a la vez. Un comentario o una nota que contradice `precios.ts` no es
una segunda opinión: es un bug, y gana `precios.ts`.)

**Cómo aplicarla:** antes de versionar cualquier entrega de canon, además del
chequeo de acentos (`web/scripts/chequeo_acentos_canon.ts`), coteja toda cifra de
precio del `REGLAS_Y_TOKENS.md` contra `precios.ts`. Si difieren, corrige el
canon en la adopción, deja una nota de adopción citando `precios.ts`, y avísale
a Design para que su próxima entrega venga alineada de origen. Ninguna ruta
hardcodea números: leen de `precios.ts` / `packs_catalog.json`.

## Bridge: el nombre de proyecto es `i-have-an-idea`, sin excepción

**Regla:** en toda llamada a los tools `bridge_*` (`bridge_list_pending`,
`bridge_read_brief`, `bridge_save_result`, `bridge_review`), el argumento
`project` es literalmente `i-have-an-idea`. Nunca `I have an idea`, nunca el
nombre de la carpeta, nunca una variante con mayúsculas o espacios.

**Por qué:** el puente enruta por el string `project`, y ese string es el nombre
de una carpeta bajo `C:\Users\AlexDesk\Bridge\`. La carpeta de este repo se
llama `I have an idea` (con espacios), así que la deducción natural — usar el
nombre del directorio — crea un buzón *distinto* al que escribe el chat. El
fallo es silencioso y de los peores: el chat deposita briefs sin error, y Code
responde "no hay nada pendiente" indefinidamente, cada uno mirando su propia
carpeta. No hay ningún síntoma que delate el desajuste.

**Cómo aplicarla:** usa la constante tal cual. Si `bridge_list_pending` devuelve
vacío pero el usuario asegura haber mandado un brief, la primera hipótesis es un
`project` mal escrito, no un brief perdido: comprueba qué carpetas existen bajo
`C:\Users\AlexDesk\Bridge\` antes de dar nada por perdido.
