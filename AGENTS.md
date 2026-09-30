# Contexto del proyecto

Leer `README.md` antes de iniciar trabajo en este directorio.

Este proyecto coordina mejoras y actualizaciones del software base para ejecutar nodos productores de Koinos. Las referencias principales son la organización https://github.com/koinos y el repositorio integrador Docker https://github.com/koinos/koinos.

## Continuidad del trabajo

- Mantener aquí el análisis, las decisiones y las referencias a cambios en los repositorios afectados.
- Antes de modificar software, identificar el repositorio, la versión y las dependencias relevantes; comprobar su estado actual.
- Documentar el análisis en Markdown antes de implementar una mejora.
- Distinguir propuestas, implementaciones, pruebas y despliegues efectivos al comunicar el estado.
- El propósito general del proyecto no constituye por sí solo una instrucción para desplegar cambios en nodos productores.

## Punto de continuación

- Consultar las referencias públicas del README. Si existe `LOCAL_REFERENCES.md`, contiene referencias del entorno local excluidas de Git, incluyendo documentación adicional de Knodel.
- Mantener fuera de la publicación los archivos locales y los análisis que dependan de información de proyectos privados. Al reutilizar documentación histórica, verificar opciones y datos contra la versión objetivo.
- Inventario inicial: `docs/inventory/2026-09-30-inventario.md`; evidencias en `docs/inventory/evidence/`.
- Los clones de `upstream/` son referencias públicas independientes. Leer sus instrucciones propias antes de modificar software allí.
- El inventario propone validar versiones y evitar el fallback silencioso a `latest` como primera contribución acotada al integrador; la PR chain #862 merece investigación prioritaria. Ambas siguen pendientes de implementación o validación en este proyecto.
- Para cualquier actualización, distinguir tags Git, releases, digests Docker y versiones de un nodo efectivamente instalado. Refrescar datos públicos antes de seleccionar artefactos.
