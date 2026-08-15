# Parche de un solo uso: las huellas del sellador se escribieron sin acentos y el
# texto de los pasos SI los lleva. Se corrigen aqui para que la guarda del
# sellador compare contra el texto real del grafo. Queda en el repo como registro.
import io

RUTA = "scripts/loop/vuelta31_sellar_col.py"
PARES = [
    ('"no se pierda informacion ni calidez"', '"no se pierda información ni calidez"'),
    ('"entre la compra y el dia 100"', '"entre la compra y el día 100"'),
    ('"simbolo o recordatorio del cliente"', '"símbolo o recordatorio del cliente"'),
    ('"silla vacia representando al cliente"', '"silla vacía representando al cliente"'),
    ('"sistema unificado de gestion de cuentas"', '"sistema unificado de gestión de cuentas"'),
    ('"premian solo adquisicion"', '"premian solo adquisición"'),
    ('"metricas de exito definidas en el kickoff"', '"métricas de éxito definidas en el kickoff"'),
    ('"rituales o simbolos que representen"', '"rituales o símbolos que representen"'),
    ('"momento de iniciacion publico"', '"momento de iniciación público"'),
    ('"autoservicio y autosanacion"', '"autoservicio y autosanación"'),
]

s = io.open(RUTA, encoding="utf-8").read()
n = 0
for a, b in PARES:
    if a not in s:
        print("NO ENCONTRADA: %s" % a)
        continue
    s = s.replace(a, b, 1)
    n += 1
io.open(RUTA, "w", encoding="utf-8", newline="").write(s)
print("huellas corregidas: %d de %d" % (n, len(PARES)))
