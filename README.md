# Coordinación del nodo Koinos

[Repositorio público](https://github.com/pgarciagon/koinos_legacy_node)

## Objetivo

Este proyecto sirve como coordinador de las mejoras y actualizaciones del software base necesario para ejecutar nodos productores en Koinos.

Centraliza el análisis, las propuestas, las decisiones y el seguimiento de cambios que puedan afectar a varios repositorios del nodo. El punto de partida es el conjunto de servicios que se lanza mediante Docker.

## Referencias principales

- [Organización pública Koinos](https://github.com/koinos): reúne los repositorios del ecosistema; no es un único repositorio de código.
- [koinos/koinos](https://github.com/koinos/koinos): repositorio integrador para lanzar los servicios de Koinos mediante Docker.

## Documentación de funcionamiento

La [documentación pública de arquitectura de Koinos](https://github.com/koinos/koinos-docs/tree/master/docs/architecture) describe los microservicios y la comunicación interna. El [inventario de este proyecto](docs/inventory/2026-09-30-inventario.md) registra las versiones concretas revisadas.

El entorno local conserva referencias técnicas adicionales y una comparación con el proyecto privado Knodel en `LOCAL_REFERENCES.md` y `docs/comparisons/`. Estos archivos no forman parte del repositorio público.

## Forma de trabajo

1. Identificar el problema o la actualización y los componentes afectados.
2. Documentar el análisis y la propuesta antes de implementar.
3. Realizar los cambios en los repositorios correspondientes y registrar aquí sus referencias.
4. Verificar la compatibilidad entre componentes y el comportamiento del nodo con pruebas adecuadas al cambio.
5. Registrar resultados, limitaciones y pasos necesarios para su adopción.

## Estado del proyecto

Propósito establecido el 28 de septiembre de 2026. El 30 de septiembre se completó el [inventario de componentes, versiones y dependencias](docs/inventory/2026-09-30-inventario.md) del despliegue Docker, con evidencias de GitHub y Docker Hub.

El análisis identifica 12 servicios y propone primeras mejoras de reproducibilidad, salud operativa, construcción y soporte ARM64. Recomienda como primera contribución acotada al integrador validar el conjunto de versiones y evitar la selección silenciosa de `latest`; destaca también una PR de memoria WASM en `chain` para revisión prioritaria.

Las mejoras están propuestas. La verificación realizada comprende código, metadatos de imágenes y resolución de Compose; todavía no se han ejecutado builds ni pruebas de un nodo. Los repositorios públicos de referencia se conservan en `upstream/`, excluido de Git.

El arreglo de replay de estado [chain #861](https://github.com/koinos/koinos-chain/pull/861) ya está incluido en legacy chain `v1.5.2`. Las investigaciones sobre mejoras futuras se documentarán con fuentes públicas y una distinción explícita entre propuesta, implementación y validación.

Los extractos de fuentes y manifiestos upstream conservan sus licencias originales; véase [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
