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
