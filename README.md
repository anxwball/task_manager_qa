# Task Manager QA

Mini-proyecto académico de **Calidad de Software** orientado al desarrollo incremental de una agenda de tareas y a la aplicación de prácticas básicas de aseguramiento de la calidad.

El proyecto utiliza Python y SQLAlchemy y mantiene una estructura preparada para separar la lógica de aplicación, persistencia y pruebas. El objetivo principal no es únicamente obtener un software que funcione, sino establecer evidencia verificable de que los componentes implementados cumplen los comportamientos esperados.

> **Contexto académico:** este repositorio se utiliza como evidencia práctica para un taller de Calidad de Software basado en Aprendizaje Basado en Proyectos (ABP). La actividad está planteada para equipos de dos personas; en esta entrega el trabajo se desarrolla individualmente.

## Objetivos

- Construir un prototipo sencillo de gestión de tareas.
- Aplicar pruebas automatizadas sobre los componentes desarrollados.
- Utilizar una base de datos aislada para las pruebas.
- Mantener trazabilidad mediante control de versiones.
- Documentar evidencias de calidad y resultados de las pruebas.
- Reflexionar sobre la diferencia entre que un software **funcione** y que funcione **con calidad**.

## Alcance actual

El repositorio se encuentra en una etapa incremental. Actualmente se ha establecido la infraestructura inicial de persistencia y pruebas:

- Configuración de conexión a base de datos mediante `DATABASE_URL`.
- Integración con SQLAlchemy.
- Creación y eliminación de tablas mediante una base declarativa.
- Gestión contextual de sesiones de base de datos.
- Entorno de pruebas independiente utilizando SQLite en memoria.
- Prueba automatizada inicial de conectividad a la base de datos.
- Configuración de `pytest` como framework de pruebas.
- Control de versiones mediante Git/GitHub.
- Registro de cambios mediante `CHANGELOG.md`.

La funcionalidad completa de agenda de tareas se incorporará de forma incremental; por ello, este README distingue entre la infraestructura existente y los objetivos de calidad del producto final, evitando presentar como implementadas funcionalidades que todavía no existen.

## Metodología de trabajo

### Aprendizaje Basado en Proyectos (ABP)

El repositorio funciona como un mini-producto sobre el cual se aplican prácticas de calidad durante el desarrollo. Cada incremento debe producir código funcional acompañado, cuando corresponda, de pruebas y evidencia.

### Aula Invertida

La aplicación práctica se complementa con revisión previa de conceptos relacionados con calidad de software, pruebas, control de versiones y criterios de aceptación.

### Uso crítico de IA

La IA puede utilizarse como apoyo para:

- Proponer casos de prueba.
- Generar una checklist inicial de calidad.
- Sugerir métricas o escenarios de prueba.
- Identificar posibles casos límite.

Las propuestas generadas por IA no se consideran evidencia por sí mismas. Deben ser revisadas, adaptadas y justificadas de acuerdo con el comportamiento real del sistema.

## Estrategia de calidad

La estrategia se organiza alrededor de cuatro elementos:

1. **Requisitos y comportamiento esperado**: definir qué debe hacer cada funcionalidad.
2. **Casos de prueba**: comprobar comportamientos normales, límites y entradas inválidas cuando sean aplicables.
3. **Checklist de calidad**: revisar aspectos técnicos y de proceso antes de considerar terminado un incremento.
4. **Evidencias**: conservar resultados de pruebas, decisiones y cambios realizados en el repositorio.

### Principio de calidad

> Que una aplicación ejecute correctamente un escenario no demuestra por sí solo que el software tenga calidad.

La calidad se evalúa considerando, además del funcionamiento, aspectos como validación, mantenibilidad, trazabilidad, pruebas reproducibles y comportamiento ante condiciones no ideales.

## Pruebas

El proyecto utiliza **pytest** y dispone de un entorno de base de datos separado del entorno de desarrollo.

Las pruebas utilizan SQLite en memoria (`sqlite:///:memory:`), lo que permite ejecutar los casos de prueba sin depender de una base de datos persistente externa. Cada prueba recibe una sesión aislada y se realiza rollback al finalizar.

### Prueba implementada

Actualmente existe una prueba de conectividad que ejecuta `SELECT 1` sobre el engine destinado a pruebas y verifica que la conexión responda correctamente.

### Ejecución

Con las dependencias de desarrollo instaladas:

```bash
pytest
```

Para una salida más detallada:

```bash
pytest -v
```

## Casos de prueba previstos

A medida que se implemente la agenda de tareas, los casos se ampliarán como mínimo hacia las siguientes categorías:

| Categoría | Ejemplo |
|---|---|
| Caso válido | Crear una tarea con datos correctos |
| Campo obligatorio | Intentar crear una tarea sin título |
| Límites | Título vacío o con longitud máxima permitida |
| Persistencia | Crear una tarea y comprobar que pueda recuperarse |
| Actualización | Modificar los datos de una tarea existente |
| Eliminación | Eliminar una tarea existente |
| Identificador inexistente | Consultar, actualizar o eliminar una tarea que no existe |
| Aislamiento | Verificar que una prueba no contamine otra |

Estos casos representan el plan de pruebas del producto y no deben interpretarse como funcionalidades ya implementadas.

## Checklist de calidad

La checklist se utilizará como mecanismo de revisión antes de cerrar cada incremento.

- [ ] La funcionalidad tiene un comportamiento esperado claramente definido.
- [ ] Los casos de prueba cubren el escenario principal.
- [ ] Se consideran entradas inválidas o casos límite relevantes.
- [ ] Las pruebas son reproducibles.
- [ ] Las pruebas no dependen de datos persistentes del entorno de desarrollo.
- [ ] El código mantiene una separación razonable de responsabilidades.
- [ ] Los cambios relevantes quedan registrados en Git.
- [ ] La evidencia de las pruebas puede ser consultada.
- [ ] Las propuestas generadas con IA fueron revisadas críticamente.
- [ ] No se declara como implementada una funcionalidad que todavía no existe.

## Estructura del proyecto

```text
.
├── .github/
│   └── workflows/
│       └── release.yml
├── src/
│   ├── cli.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── repository.py
│   └── settings.py
├── tests/
│   ├── conftest.py
│   ├── test_database.py
│   └── test_tasks.py
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── pyproject.toml
└── uv.lock
```

La separación entre `src/` y `tests/` permite mantener el código de producción independiente del código utilizado para verificarlo.

## Tecnologías y herramientas

- **Python 3.14+**
- **SQLAlchemy 2.x** para acceso y configuración de persistencia.
- **SQLite** como base de datos utilizada en el entorno de pruebas.
- **pytest** para pruebas automatizadas.
- **uv** para gestión de dependencias y entorno de desarrollo.
- **Git / GitHub** para control de versiones y trazabilidad.
- **pre-commit** para verificaciones previas a los commits.
- **python-semantic-release** para automatización de versiones y releases.

La versión y dependencias declaradas del proyecto se encuentran en `pyproject.toml`.

## Control de versiones

GitHub constituye parte de la evidencia del proceso de calidad. Los cambios se mantienen mediante commits y el proyecto cuenta con un `CHANGELOG.md` generado a partir del historial de cambios.

La versión actual declarada en el proyecto es **1.1.0**.

El historial disponible registra, entre otros cambios, la configuración de la base de datos, la incorporación de la prueba de conexión y ajustes de configuración del proyecto.

## Evidencias del taller

Las evidencias de calidad deben mantenerse asociadas al proyecto y pueden incluir:

- Resultados de ejecución de `pytest`.
- Casos de prueba diseñados.
- Checklist de calidad completada.
- Capturas o registros de resultados cuando sean requeridos por la actividad.
- Commits relevantes del desarrollo.
- Cambios derivados de defectos encontrados durante las pruebas.
- Reflexión sobre las propuestas generadas con IA y cuáles fueron aceptadas, modificadas o descartadas.

## Reflexión ética y profesional

La calidad del software también tiene una dimensión ética y profesional. Un defecto puede afectar desde la pérdida de información hasta decisiones incorrectas de usuarios o procesos dependientes del sistema.

Por esta razón, probar software no debe reducirse a demostrar que el caso feliz funciona. El desarrollador debe considerar qué puede fallar, qué impacto tendría el fallo y qué evidencia existe para sostener que una funcionalidad fue verificada.

En sistemas de mayor criticidad, esta responsabilidad aumenta: una decisión de implementación o una prueba insuficiente puede trasladar riesgos técnicos a personas y organizaciones que dependen del software.

## Limitaciones actuales

Este repositorio corresponde a un prototipo académico en desarrollo. Entre las limitaciones actuales se encuentran:

- La funcionalidad de gestión de tareas todavía no está completamente implementada.
- La cobertura de pruebas es todavía limitada.
- No se presenta una métrica de cobertura como evidencia hasta contar con una base de código y pruebas suficientemente representativa.
- La checklist y los casos de prueba deberán evolucionar junto con la implementación.

Estas limitaciones forman parte del estado actual del proyecto y constituyen oportunidades de mejora para los siguientes incrementos.

## Próximos incrementos

1. Implementar el modelo de dominio de tareas.
2. Implementar las operaciones básicas de persistencia.
3. Añadir los casos de prueba correspondientes.
4. Validar entradas y escenarios límite.
5. Ejecutar y documentar la batería de pruebas.
6. Revisar la checklist de calidad.
7. Consolidar las evidencias del taller.
8. Elaborar la reflexión final sobre calidad, uso de IA y responsabilidad profesional.

## Propósito académico

Este proyecto busca demostrar un proceso básico de aseguramiento de calidad aplicado a un producto pequeño: **definir comportamiento, implementar, probar, revisar evidencia y mejorar**.

El resultado esperado no es solamente una agenda de tareas funcional, sino un pequeño producto cuyo proceso de construcción pueda ser inspeccionado y defendido mediante evidencia técnica.
