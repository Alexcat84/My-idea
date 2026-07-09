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
