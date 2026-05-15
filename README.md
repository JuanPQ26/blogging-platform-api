# Blogging Platform API

Este es un proyecto base que utiliza **FastAPI** con **SQLModel** y **SQLite**, administrado con **uv** para la gestión de dependencias.

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- [Python](https://www.python.org/) 3.13+
- [uv](https://github.com/nikita-skobov/uv_management)

## Instalación

Clona el repositorio y entra en la carpeta del proyecto:

```bash
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo
```

Instala las dependencias con uv:

```bash
uv sync
```

## Ejecución del servidor

Para iniciar el servidor de desarrollo de FastAPI, usa el siguiente comando:

```bash
uv run uvicorn blogging_platform_api:app --reload
```

El servidor estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

La documentación interactiva de la API está en:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Despliegue

Para ejecutar el servidor en producción, usa:

```bash
uv run uvicorn blogging_platform_api:app --host 0.0.0.0 --port 8000 --workers 4
```