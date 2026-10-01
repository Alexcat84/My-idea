# Próximos pasos tras la auditoría final

**Para quién:** el fundador y la sesión que retome el trabajo con una suscripción normal, después de que se cancele Max
(jueves 8 oct 2026). Una suscripción normal no aguanta oleadas de veinte lectores. Por eso aquí solo queda trabajo que
se hace con pocas llamadas o con saldo propio.

**Estado de este documento:** borrador del 30 sep 2026. Se cierra antes de que se agote la cuota del jueves 8, con el
resultado de la etapa 1, de la medida 2 y de la etapa 2 (sección 5).

## 1. Qué gasta cada cosa

| Paso | Qué gasta | Cuánto |
|---|---|---|
| Re-embebido con Voyage | saldo de Voyage, no la suscripción | menos de 0,05 USD |
| Corrida final | **saldo de la API de Anthropic**, no la suscripción | unos 8,5 a 11,5 USD (`docs/producto/CORRIDA_FINAL.md`) |
| Copia de las reglas a la forja | una sesión corta de Claude Code, sin agentes de lectura | poco |
| Lo que la auditoría deje abierto | depende: ver sección 5 | |

El orden importa: el índice de vectores y la caché viajan dentro del despliegue. Primero se re-embebe, después se
despliega y al final se corre la corrida.

## 2. Re-embebido con Voyage (una sola pasada)

Decisión del fundador: Voyage corre una sola vez, al final del remedio, con todos los nodos corregidos. Las tandas de
la auditoría final (`docs/saneamiento/tandas/final-*.json` y `procedencia-*.json`) cambiaron el texto de unos 2.444
nodos vivos. Las constancias CASA no cambian el texto y no se re-embeben.

1. Pon `VOYAGE_API_KEY` en el `.env` raíz. Lo retiras al terminar.
2. Prueba en seco. No llama a nadie y dice cuántos nodos haría:

   ```
   python scripts/auditoria_final/reembeber.py docs/saneamiento/tandas/final-*.json docs/saneamiento/tandas/procedencia-*.json
   ```

3. La pasada de verdad: la misma línea con `--yes` al final.
4. `python scripts/sync_assets_web.py`, las dos suites (`PYTHONIOENCODING=utf-8 python engine/run_all_tests.py` y
   `cd web && npx vitest run`), commit y despliegue.

**Si el script dice "NO SE ESCRIBE":** comprueba que el índice queda coherente y, si algo falla, no escribe nada. Esto
es lo que comprueba:
- todo nodo vivo tiene vector;
- no hay ids duplicados;
- todos los vectores tienen la misma dimensión;
- solo cambian los vectores pedidos;
- cada vector nuevo queda más cerca de su vector viejo que de cualquier otro.

Esa última comprobación se pensó para correcciones de voz. Una corrección de fondo puede acercar un nodo a un vecino
casi gemelo. Si falla solo por eso, el script nombra los nodos. Se miran a mano y se decide: o la corrección cambió de
qué trata el nodo (y hay que revisarla), o el nodo y su vecino son gemelos (y va a la mesa de duplicados). No se afloja
la comprobación para que pase.

## 3. Corrida final (saldo de la API)

Está entera en `docs/producto/CORRIDA_FINAL.md`, con su lista de comprobación, sus créditos, su coste y la consulta
que compara la app con el saldo:
- paso A: completar la caché;
- paso B: prueba de coherencia, con 33 recorridos;
- paso C: vuelo completo.

Lo que añade la auditoría:
- Va **después** del re-embebido y de su despliegue.
- La regla dura D1 vale también aquí. Si una respuesta de la IA nombra un libro, un autor, "los estudios" o insinúa
  un origen, es un fallo que se anota con su sesión. `REGLA_SIN_FUENTES` va en toda llamada
  (`web/lib/reglaSinFuentes.ts`).
- El aviso de vigencia ya no lleva año: "Verifica la norma vigente en tu país: estas reglas cambian con el tiempo".

## 4. Copia de las reglas a la forja

La forja (`forja-nodos`) convierte libros en nodos para packs futuros. Tiene que limpiar con la misma vara que el
catálogo, para que un pack nuevo no traiga de vuelta lo que la auditoría quitó.

1. **Las guardas como datos:** copiar `dataset/metadata/guardas_contenido.json` (con su versión) al sitio donde la
   forja lo lee.
2. **Las reglas duras D1, D2 y D3 y la política C32** de `docs/REGLAS_DE_LA_CASA.md` entran al
   `docs/BANCO_DE_REGLAS.md` de la forja como reglas nuevas, con su fecha y su regla madre en My-idea. El banco se
   corrige añadiendo debajo, nunca tapando:
   - D1: ningún origen visible;
   - D2: ninguna copia fiel;
   - D3: ningún nodo vivo se retira;
   - C32: devolver el sentido y el término preciso, nunca un pasaje palabra por palabra.
3. **Las pautas de procedencia** (el prefijo "Sugerencia de My Idea" y las atribuciones genéricas, en once idiomas)
   viven hoy en `web/lib/procedencia.test.ts`. Para que la forja las use, primero pasan a `guardas_contenido.json`
   (prueba en rojo primero, versión nueva) y después se copian.
4. En la forja, su gate rechaza un candidato que las incumpla. Su prueba va en rojo primero.

## 5. Lo que deja abierta la auditoría

Se completa al cierre de la semana. Esto es lo previsto:

- **Etapa 1:** cerrada con su riesgo residual declarado (Wilson 95 %) en `docs/ACTA_SANEAMIENTO_FINAL.md`, sección 9.9.
- **Medida 2** (semilla 20261010): con el criterio de copias fieles (U14), y la ortografía y los calcos exigidos solo
  en los campos que el cliente ve crudos.
- **Etapa 2,** si cupo: retraducción a los diez idiomas de cada etiqueta corregida, con su huella de vigencia.
- **A mejora continua, con su ficha:** la ortografía y los calcos del resumen, las condiciones y el título.
- **Decisión del fundador o de un abogado:** la licencia de IDEO.org (CC BY-NC-ND 3.0) frente a la regla D1 y al uso
  comercial. No se retiró nada.
