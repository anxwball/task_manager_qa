# Task Manager QA

## Introducción

**Task Manager QA** es un mini-producto académico desarrollado para aplicar principios básicos de **calidad de software** durante el ciclo de vida de un sistema sencillo de gestión de tareas.

El proyecto se desarrolla en Python y utiliza SQLAlchemy como capa de persistencia. Su propósito no se limita a construir una agenda de tareas funcional, sino a demostrar un proceso básico de aseguramiento de calidad basado en:

* definición de requisitos verificables;
* implementación incremental;
* pruebas automatizadas;
* aislamiento del entorno de pruebas;
* control de versiones;
* trazabilidad de cambios;
* revisión mediante checklist;
* análisis crítico del uso de inteligencia artificial.

El proyecto forma parte del taller **“Introducción a la Calidad en el Desarrollo de Software: de la teoría a la práctica”**, cuya metodología se fundamenta en Aprendizaje Basado en Proyectos (ABP) y Aula Invertida.

> **Contexto de trabajo:** la actividad académica establece equipos de dos estudiantes para la fase práctica. Esta implementación está siendo desarrollada individualmente, por lo que el repositorio refleja un único flujo de desarrollo y no pretende representar una colaboración inexistente.

---

## 1. Propósito del proyecto

El propósito del proyecto es construir progresivamente una agenda de tareas y utilizarla como caso práctico para demostrar que la calidad de software debe evaluarse mediante **evidencia verificable**, no únicamente mediante la ejecución satisfactoria de un escenario.

El proyecto busca responder tres preguntas:

1. **¿Qué debe hacer el sistema?**
2. **¿Cómo se puede demostrar que lo hace correctamente?**
3. **¿Qué evidencia permite sostener que una implementación tiene un nivel aceptable de calidad?**

La estrategia adoptada es incremental:

> **Requisito → Implementación → Prueba → Evidencia → Revisión → Mejora**

---

## 2. Alcance

### Alcance funcional previsto

El producto final tendrá como objetivo proporcionar una agenda sencilla de tareas con operaciones básicas de gestión:

* creación de tareas;
* consulta de tareas;
* actualización de tareas;
* eliminación de tareas;
* validación de entradas;
* persistencia de información.

Estas funcionalidades constituyen el **objetivo del producto**, pero no deben interpretarse como funcionalidades actualmente implementadas.

### Alcance de calidad

El proyecto también contempla:

* pruebas automatizadas mediante `pytest`;
* base de datos aislada para pruebas;
* pruebas de escenarios válidos e inválidos;
* verificación de persistencia;
* verificación del aislamiento entre pruebas;
* control de versiones mediante Git/GitHub;
* trazabilidad mediante `CHANGELOG.md`;
* validaciones mediante `pre-commit`;
* automatización del versionado mediante `python-semantic-release`;
* documentación de evidencias;
* revisión crítica de propuestas generadas mediante IA.

---

## 3. Estado actual del proyecto

El proyecto se encuentra en una **fase inicial de infraestructura y aseguramiento de calidad**.

### Implementado

Actualmente se encuentran implementados:

* configuración mediante `DATABASE_URL`;
* carga de variables de entorno mediante `python-dotenv`;
* creación del engine de SQLAlchemy;
* `SessionLocal`;
* base declarativa de SQLAlchemy;
* gestión contextual de sesiones;
* creación y eliminación de tablas;
* entorno de pruebas independiente mediante SQLite en memoria;
* fixture de sesión para pruebas;
* rollback al finalizar las pruebas;
* prueba automatizada de conexión a la base de datos;
* configuración de `pytest`;
* configuración de `pre-commit`;
* control de versiones con Git/GitHub;
* `CHANGELOG.md`;
* configuración de `python-semantic-release`;
* workflow de GitHub Actions para releases.

### Pendiente

Todavía se encuentran pendientes:

* modelo de dominio `Task`;
* operaciones CRUD;
* repositorio de tareas;
* interfaz de usuario/CLI funcional;
* validaciones de negocio;
* pruebas funcionales de tareas;
* pruebas de persistencia;
* pruebas de actualización y eliminación;
* pruebas de casos límite;
* demostración automatizada del aislamiento entre pruebas;
* consolidación de la evidencia final.

Los archivos destinados a estas responsabilidades ya existen en la estructura del proyecto, pero algunos todavía no contienen implementación.

---

## 4. Requisitos del sistema

Los requisitos se han reducido a un conjunto mínimo que pueda evolucionar junto con el producto y convertirse posteriormente en casos de prueba automatizados.

### 4.1 Requisitos funcionales

| ID        | Requisito                                                                                       | Criterio de aceptación                                                                                                                            | Estado    |
| --------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| **RF-01** | El sistema deberá permitir crear una tarea con los datos obligatorios definidos por el dominio. | Al proporcionar datos válidos, se crea una tarea y se genera un identificador persistente. Los datos almacenados coinciden con los suministrados. | Pendiente |
| **RF-02** | El sistema deberá permitir consultar una tarea existente mediante su identificador.             | Una tarea previamente creada puede recuperarse mediante su ID y devuelve los datos almacenados correspondientes.                                  | Pendiente |
| **RF-03** | El sistema deberá permitir modificar y eliminar una tarea existente.                            | Una actualización modifica únicamente los datos esperados y una eliminación hace que la tarea deje de estar disponible mediante consulta.         | Pendiente |

Estos requisitos se han elegido deliberadamente porque permiten construir posteriormente pruebas unitarias/integración con `pytest` sin requerir una interfaz gráfica ni infraestructura externa.

### 4.2 Requisitos no funcionales

| ID         | Requisito                                                                                                                           | Criterio de aceptación                                                                                                                                 | Estado                                            |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| **RNF-01** | Las pruebas deberán ejecutarse sobre un entorno de persistencia aislado del entorno de desarrollo.                                  | La suite de pruebas utiliza SQLite en memoria y no requiere una base de datos persistente externa para ejecutarse.                                     | Implementado parcialmente                         |
| **RNF-02** | La configuración de persistencia deberá poder modificarse mediante configuración externa sin modificar el código de acceso a datos. | El origen de la base de datos se obtiene mediante `DATABASE_URL`; cambiar esta variable permite seleccionar otra URL de conexión.                      | Implementado                                      |
| **RNF-03** | Las pruebas deberán ser reproducibles y no depender del estado generado por pruebas anteriores.                                     | Cada prueba obtiene una sesión independiente y la suite debe demostrar mediante pruebas que los datos creados en un caso no están disponibles en otro. | Infraestructura implementada; evidencia pendiente |

### Relación entre requisitos y pruebas

La intención es que cada requisito relevante pueda relacionarse con evidencia:

```text
RF-01 → test_create_task
RF-02 → test_get_task
RF-03 → test_update_task / test_delete_task

RNF-01 → test_database_isolation
RNF-02 → test_database_configuration
RNF-03 → test_test_isolation
```

La existencia de un nombre de prueba en esta sección representa el **objetivo de verificación**, no una afirmación de que dichos tests ya existan.

---

## 5. Arquitectura actual

La estructura actual separa el código de aplicación de las pruebas:

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

La responsabilidad prevista de cada componente es:

| Componente      | Responsabilidad                              |
| --------------- | -------------------------------------------- |
| `settings.py`   | Configuración externa de la aplicación       |
| `database.py`   | Engine, sesiones y metadatos de persistencia |
| `models.py`     | Modelos de dominio/persistencia              |
| `repository.py` | Operaciones de acceso a datos                |
| `cli.py`        | Interacción mediante línea de comandos       |
| `main.py`       | Punto de entrada                             |
| `tests/`        | Verificación automatizada                    |
| `conftest.py`   | Fixtures y configuración común de pruebas    |

Actualmente esta separación constituye parcialmente una **estructura objetivo**: no todos los componentes contienen todavía lógica funcional.

---

## 6. Estrategia de pruebas

El proyecto utiliza **pytest** como framework de pruebas.

El entorno de pruebas utiliza:

```text
SQLite en memoria
        ↓
test_engine
        ↓
fixture db_session
        ↓
prueba individual
        ↓
rollback
```

La configuración existente crea un engine exclusivo para pruebas sobre `sqlite:///:memory:` y proporciona una sesión por prueba. Al finalizar, la sesión se cierra y la transacción se revierte.

### Prueba actualmente implementada

Existe una prueba de conectividad:

```python
def test_database_connection(test_engine):
    with test_engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1
```

Esta prueba demuestra que el engine destinado al entorno de pruebas puede establecer una conexión y ejecutar una operación SQL básica.

### Lo que esta prueba no demuestra

La prueba anterior **no demuestra**:

* que exista el modelo `Task`;
* que las tareas puedan crearse;
* que puedan recuperarse;
* que puedan actualizarse;
* que puedan eliminarse;
* que las validaciones funcionen;
* que el aislamiento entre pruebas esté efectivamente verificado.

Por esta razón, la calidad del producto debe evaluarse incrementalmente.

---

## 7. Plan de casos de prueba

| ID             | Caso                                                | Tipo          | Estado       |
| -------------- | --------------------------------------------------- | ------------- | ------------ |
| **TC-DB-01**   | Establecer conexión con la base de datos de pruebas | Integración   | Implementado |
| **TC-DB-02**   | Crear tablas del modelo                             | Integración   | Pendiente    |
| **TC-TASK-01** | Crear tarea válida                                  | Funcional     | Pendiente    |
| **TC-TASK-02** | Rechazar datos obligatorios inválidos               | Validación    | Pendiente    |
| **TC-TASK-03** | Consultar tarea existente                           | Funcional     | Pendiente    |
| **TC-TASK-04** | Consultar tarea inexistente                         | Límite/Error  | Pendiente    |
| **TC-TASK-05** | Actualizar tarea existente                          | Funcional     | Pendiente    |
| **TC-TASK-06** | Eliminar tarea existente                            | Funcional     | Pendiente    |
| **TC-TASK-07** | Verificar persistencia de una tarea                 | Integración   | Pendiente    |
| **TC-ISO-01**  | Verificar aislamiento entre pruebas                 | Integración   | Pendiente    |
| **TC-CONF-01** | Verificar configuración mediante `DATABASE_URL`     | Configuración | Pendiente    |

---

## 8. Checklist de calidad

La checklist se utiliza como mecanismo de control antes de considerar terminado un incremento.

### 8.1 Requisitos

* [ ] El requisito está definido de forma clara y verificable.
* [ ] El requisito tiene un criterio de aceptación.
* [ ] El comportamiento esperado puede convertirse en al menos un caso de prueba.
* [ ] No se documentan como implementadas funcionalidades que solamente están planificadas.

### 8.2 Implementación

* [ ] La funcionalidad implementada corresponde al requisito definido.
* [ ] La lógica de persistencia está separada de la interacción con el usuario.
* [ ] Los errores esperados tienen un comportamiento definido.
* [ ] Las entradas inválidas relevantes están contempladas.
* [ ] La implementación no introduce dependencias innecesarias del entorno local.

### 8.3 Pruebas automatizadas

* [x] `pytest` está configurado.
* [x] Existe una suite de pruebas separada del código de producción.
* [x] Existe un entorno de base de datos específico para pruebas.
* [x] Existe una prueba automatizada de conectividad.
* [ ] Cada funcionalidad implementada tiene al menos una prueba correspondiente.
* [ ] Existen pruebas para escenarios válidos.
* [ ] Existen pruebas para escenarios inválidos.
* [ ] Existen pruebas para casos límite relevantes.
* [ ] Existe evidencia automatizada de aislamiento entre pruebas.
* [ ] La suite completa puede ejecutarse mediante `pytest`.

### 8.4 Persistencia

* [x] La conexión se configura mediante `DATABASE_URL`.
* [x] SQLAlchemy administra el acceso a la base de datos.
* [x] Las pruebas utilizan SQLite en memoria.
* [x] Las pruebas utilizan sesiones independientes.
* [ ] La creación del modelo está cubierta por pruebas.
* [ ] La creación de una tarea está cubierta por pruebas.
* [ ] La recuperación de una tarea está cubierta por pruebas.
* [ ] La actualización de una tarea está cubierta por pruebas.
* [ ] La eliminación de una tarea está cubierta por pruebas.

### 8.5 Reproducibilidad

* [x] Las pruebas no requieren la base de datos de desarrollo.
* [x] Existe una fixture específica para el entorno de pruebas.
* [ ] Una prueba puede ejecutarse independientemente de las demás.
* [ ] El orden de ejecución de las pruebas no afecta sus resultados.
* [ ] Se demuestra mediante `pytest` que los datos de una prueba no contaminan otra.

### 8.6 Control de versiones y trazabilidad

* [x] El proyecto utiliza Git.
* [x] El repositorio está alojado en GitHub.
* [x] Existe `CHANGELOG.md`.
* [x] El proyecto utiliza versionado automatizado mediante Semantic Release.
* [x] Existe un workflow de GitHub Actions para releases.
* [x] Se utilizan validaciones `pre-commit`.
* [ ] Los cambios funcionales relevantes están asociados a pruebas.
* [ ] Los defectos encontrados durante las pruebas quedan reflejados en el historial de cambios.

El `CHANGELOG.md` actual registra cambios de configuración de base de datos, pruebas y CI, incluyendo la prueba de conexión añadida en la versión `1.1.0`.

---

## 9. Evidencia de calidad

La evidencia del proyecto se divide en cuatro categorías.

### Evidencia técnica

* código fuente;
* pruebas automatizadas;
* resultados de `pytest`;
* configuración del entorno de pruebas.

### Evidencia de proceso

* commits;
* historial de cambios;
* `CHANGELOG.md`;
* configuración de `pre-commit`;
* workflow de GitHub Actions.

### Evidencia documental

* requisitos;
* criterios de aceptación;
* casos de prueba;
* checklist;
* README.

### Evidencia crítica

* análisis de propuestas generadas mediante IA;
* decisiones de aceptación, modificación o rechazo;
* identificación de limitaciones;
* reflexión sobre calidad y responsabilidad profesional.

La IA puede contribuir a generar candidatos para casos de prueba o checklists, pero la evidencia final debe provenir del **análisis del estudiante y del comportamiento real del sistema**.

---

## 10. Uso crítico de inteligencia artificial

La IA se considera una herramienta de apoyo al proceso de calidad, no un sustituto de la evaluación técnica.

Puede utilizarse para:

* proponer requisitos;
* sugerir casos de prueba;
* identificar casos límite;
* generar una checklist inicial;
* sugerir métricas;
* detectar posibles defectos.

Sin embargo, cada propuesta debe contrastarse con:

1. los requisitos reales;
2. la implementación existente;
3. la arquitectura del proyecto;
4. los resultados de las pruebas;
5. el objetivo académico.

Una propuesta generada por IA que no corresponde al comportamiento real del sistema no constituye evidencia de calidad.

---

## 11. Control de versiones

GitHub constituye parte de la evidencia del proceso de desarrollo.

El proyecto utiliza:

* Git;
* GitHub;
* Conventional Commits mediante `pre-commit`;
* `CHANGELOG.md`;
* `python-semantic-release`;
* GitHub Actions.

La configuración actual del proyecto declara la versión `1.1.0` y utiliza Semantic Release para automatizar el versionado y la generación de releases.

El workflow de release se ejecuta sobre `main` y utiliza `uv` para instalar las dependencias antes de ejecutar Semantic Release.

---

## 12. Tecnologías utilizadas

| Tecnología              | Propósito                                   |
| ----------------------- | ------------------------------------------- |
| Python 3.14+            | Lenguaje de programación                    |
| SQLAlchemy 2.x          | Persistencia y ORM                          |
| SQLite                  | Base de datos de pruebas                    |
| pytest                  | Pruebas automatizadas                       |
| uv                      | Gestión de entorno y dependencias           |
| python-dotenv           | Configuración mediante variables de entorno |
| pre-commit              | Validaciones previas a commits              |
| Git                     | Control de versiones                        |
| GitHub                  | Repositorio y trazabilidad                  |
| python-semantic-release | Versionado y releases                       |
| GitHub Actions          | Automatización                              |

Las versiones y dependencias declaradas se encuentran en `pyproject.toml`.

---

## 13. Roadmap de implementación

El desarrollo restante se organizará en incrementos pequeños y verificables.

### Incremento 1 — Dominio

1. Definir el modelo `Task`.
2. Definir los atributos obligatorios.
3. Crear las restricciones relevantes.
4. Crear pruebas del modelo.

### Incremento 2 — Persistencia

1. Implementar el repositorio.
2. Implementar creación.
3. Implementar consulta.
4. Implementar actualización.
5. Implementar eliminación.
6. Crear pruebas de persistencia.

### Incremento 3 — Validación

1. Identificar entradas inválidas.
2. Implementar validaciones.
3. Añadir casos límite.
4. Añadir pruebas negativas.

### Incremento 4 — Aislamiento y reproducibilidad

1. Completar fixtures.
2. Verificar rollback.
3. Crear prueba explícita de aislamiento.
4. Ejecutar la suite completa.

### Incremento 5 — Evidencia

1. Ejecutar `pytest -v`.
2. Completar la checklist.
3. Registrar defectos encontrados.
4. Registrar cambios relevantes.
5. Consolidar evidencia para el informe académico.
6. Elaborar la reflexión final.

---

## 14. Criterio para considerar terminado un incremento

Un incremento no se considerará terminado únicamente porque el código funcione manualmente.

Debe cumplir como mínimo:

```text
Requisito definido
       ↓
Implementación
       ↓
Caso de prueba
       ↓
pytest PASS
       ↓
Checklist revisada
       ↓
Cambio registrado
```

Esto permite transformar la calidad de una afirmación subjetiva en un proceso respaldado por evidencia.

---

## 15. Limitaciones actuales

El proyecto todavía presenta limitaciones importantes:

* la agenda de tareas aún no está implementada;
* el modelo de dominio está pendiente;
* las operaciones CRUD están pendientes;
* las pruebas funcionales están pendientes;
* la prueba de conexión constituye actualmente la principal evidencia automatizada;
* el aislamiento de sesiones está implementado como infraestructura, pero todavía requiere una prueba que demuestre su comportamiento;
* no existe todavía una métrica de cobertura suficientemente representativa para utilizarla como evidencia principal.

Estas limitaciones no se ocultan en la documentación. Constituyen el estado real del producto y determinan el trabajo restante.

---

## 16. Reflexión sobre calidad

El proyecto utiliza una agenda de tareas sencilla como vehículo para demostrar un principio más general:

> **Un software que funciona no necesariamente es un software cuya calidad haya sido demostrada.**

Una implementación puede ejecutar correctamente el escenario esperado y aun así presentar problemas de validación, persistencia, aislamiento, mantenibilidad o comportamiento ante errores.

Por ello, el objetivo de este proyecto no es únicamente terminar una agenda de tareas. El objetivo es construir un proceso mínimo mediante el cual cada comportamiento importante pueda relacionarse con un requisito y una evidencia de verificación.

Esta perspectiva también tiene una dimensión profesional y ética. En sistemas reales, los defectos pueden provocar pérdida de información, decisiones incorrectas, interrupciones operativas o impactos económicos. La responsabilidad del desarrollador no termina cuando el programa "funciona"; también implica conocer sus límites y disponer de evidencia razonable sobre su comportamiento.

---

## 17. Estado resumido

| Área                            | Estado       |
| ------------------------------- | ------------ |
| Configuración del proyecto      | Implementado |
| Persistencia base               | Implementado |
| Entorno de pruebas              | Implementado |
| Prueba de conexión              | Implementado |
| Modelo de tareas                | Pendiente    |
| CRUD                            | Pendiente    |
| Validaciones                    | Pendiente    |
| Pruebas funcionales             | Pendiente    |
| Prueba explícita de aislamiento | Pendiente    |
| Checklist                       | Definida     |
| Control de versiones            | Implementado |
| Changelog                       | Implementado |
| Semantic Release                | Configurado  |
| GitHub Actions                  | Configurado  |
| Evidencia final del taller      | Pendiente    |

---

## 18. Conclusión

**Task Manager QA** representa una implementación incremental de un pequeño sistema de gestión de tareas acompañada por prácticas iniciales de aseguramiento de calidad.

El estado actual demuestra que ya existe una base técnica para desarrollar y verificar el producto: configuración externa, persistencia mediante SQLAlchemy, entorno aislado de pruebas, `pytest`, control de versiones y automatización de releases.

El siguiente objetivo no es agregar complejidad innecesaria, sino utilizar esta infraestructura para implementar progresivamente el dominio de tareas y convertir cada funcionalidad en **comportamiento verificable mediante pruebas automatizadas**.

El resultado esperado es un mini-producto en el que pueda demostrarse no solamente que el software funciona, sino **qué requisitos cumple, cómo fueron verificados y qué evidencia respalda las conclusiones de calidad**.
