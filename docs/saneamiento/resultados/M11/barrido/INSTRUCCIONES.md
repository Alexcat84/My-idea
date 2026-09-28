# BARRIDO FINAL DE CALCOS (limpieza M11, 28 sep 2026)

Tu entrada (`barrido/entrada.json`) trae textos YA LIMPIOS del pack del mundo 11 de My Idea (app en espanol para
emprendedores) donde un patron detecto uno de estos terminos. Decide en cada uno si ES el calco y, si lo es, escribe el
texto nuevo con el cambio MINIMO:

| Termino | Cuando es calco | Queda |
|---|---|---|
| "a que se parece (el exito, un gran resultado...)" | calco de "what X looks like" | "como es", "como seria" (ajusta la concordancia) |
| "abastecer / abastecimiento (de candidatos, del flujo)" | calco de "sourcing" | "captar candidatos", "captacion de candidatos" |
| "por delante" | SOLO cuando significa "up front" (de antemano, desde el principio: "explicar por delante", "aclara por delante", "hecha por delante", "planifica por delante") | "de antemano", "desde el principio", "antes" |
| "por delante" | NO es calco en "tienes por delante tres meses", "con seis meses por delante", "las opciones que hay por delante", "poner X por delante de Y" (delante de, antes que) | se queda |
| "que suban la voz / que la bajen" | traduce "pipe up / pipe down" (hablar mas o menos, no volumen) | "que hablen mas / que hablen menos" |
| "ensenar mejora" | "ensenar" por "mostrar" | "demostrar mejora" |

Voz de la casa: espanol con tildes, tu, sin guiones largos o medios, sin "se espera", "se recomienda", "se debe", "su
equipo", "el equipo de". Un resumen_teorico sigue midiendo de 400 a 600 caracteres (cuentalos con un script). No cambies
nada mas del texto.

Salida `barrido/propuestas.json` en UTF-8: {"cambios": [{"node_id","campo","indice","texto_anterior" (exacto),
"texto_nuevo","veredicto":"VOZ","motivos":["ingles"|"voz_de_la_casa"],"fragmentos":[trozos exactos del anterior que salen],
"termino"}], "sin_cambio": [{"node_id","campo","indice","por_que"}]}, con cada elemento de la entrada en una de las dos listas.
