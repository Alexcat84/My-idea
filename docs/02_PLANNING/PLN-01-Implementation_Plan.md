# Diagnóstico y Plan de Construcción: "La Telaraña del Emprendedor"

¡Confirmado! La carpeta del *I Ching* y todo su contenido ha sido eliminada. El proyecto lateral fue un éxito, pero ahora toda nuestra atención vuelve a la aplicación principal. 

Tu visión es brillante: un embudo que toma el caos de una idea cruda, la pasa por un filtro de psicología cognitiva (Wallas), y luego usa una telaraña interactiva (grafos) para guiar al usuario a través de un laberinto de decisiones, entregando al final un plan de ejecución impecable basado en la literatura empresarial más avanzada del mundo, pero presentado con la simplicidad de una receta de café.

A continuación, presento el diagnóstico de la base actual y el plan para hacer esto realidad.

## 1. Diagnóstico: ¿Qué tenemos y qué hizo la API de Claude?

**Lo que la API de Claude ya construyó (La Base de Datos):**
- **El Dataset de Nodos:** Claude leyó la biblioteca base (The Lean Startup, Business Model Generation, Change by Design, The Art of Thought, PMBOK, etc.) y la fragmentó magistralmente. 
- En la carpeta `dataset/nodos/` tenemos cientos de archivos `.json`. Cada archivo representa un "nodo de conocimiento" aislado.
- **Estructura Interna:** Cada JSON tiene `fase_proyecto`, `titulo_concepto`, `resumen_teorico`, `pasos_accionables`, `condiciones_activacion`, y lo más importante: **`nodos_previos`** y **`nodos_siguientes`**. 
- **Conclusión del Diagnóstico:** Tenemos el cerebro crudo. Claude logró estructurar el conocimiento de densos libros de texto en una red teórica de acciones y prerrequisitos lista para usarse.

## 2. ¿Qué falta por hacer? (Los Vacíos Actuales)

La telaraña existe en archivos sueltos, pero aún no "cobra vida". Nos faltan 4 pilares fundamentales:

1. **Curar la Telaraña (Graph Curation):** Como los enlaces (`nodos_siguientes`) fueron generados por IA libro por libro, es matemáticamente seguro que tenemos **enlaces rotos** (nodos apuntando a archivos que no existen) y **nodos huérfanos** (que no conectan con nada). Necesitamos un script para sanear el grafo.
2. **El Filtro Psicológico de Entrada:** Necesitamos diseñar el "Cuestionario Raíz" inicial basado en la psicología (ej. *The Art of Thought* de Graham Wallas). Esto evaluará en qué etapa mental está la idea (Preparación, Incubación, Iluminación o Verificación) para saber exactamente por qué "puerta" (nodo) debe entrar a la telaraña.
3. **El Motor Conversacional:** La lógica en código que agarra el nodo actual, lee las `condiciones_activacion`, le hace una pregunta simple al usuario y, según su respuesta, desbloquea el camino hacia el siguiente nodo.
4. **La Interfaz Web (Magia Visual):** Una aplicación web moderna, hermosa y minimalista. Sin dashboards complejos. Solo una interfaz tipo "paso a paso" donde el usuario chatea con el sistema, respondiendo preguntas simples.

---

## Propuesta de Implementación y Fases

### Fase 1: Saneamiento del Dataset (Backend)
- Crear un script validador (`fix_spiderweb.py`) que barra todos los archivos JSON.
- Identificar y eliminar/corregir enlaces rotos en `nodos_siguientes` y `nodos_previos`.
- Compilar todo en un único grafo centralizado (`master_graph.json`) optimizado para búsquedas rápidas.

### Fase 2: Diseño del Filtro Raíz y Lógica de Ruta
- Diseñar el cuestionario psicológico inicial en base a Graham Wallas.
- Escribir la lógica de ruteo que recorre el grafo de forma dinámica. El sistema evaluará los nodos adyacentes y le dará al usuario opciones en lenguaje natural.
- Algoritmo ensamblador: Al final del recorrido, el sistema concatenará los `pasos_accionables` de todos los nodos visitados y usará un LLM para redactar la "Receta de Café" final (el plan de acción estructurado).

### Fase 3: Desarrollo de la Aplicación Web (Frontend)
- Inicializar un proyecto con **Vite + React**.
- **Estética:** Fiel a las reglas de diseño premium (glassmorphism, animaciones suaves, tipografía elegante de Google Fonts).
- **UX:** Flujo de pantalla completa tipo Typeform o ChatGPT, donde el usuario interactúa pregunta por pregunta sin fricción cognitiva.
