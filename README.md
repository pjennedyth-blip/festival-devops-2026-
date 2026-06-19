[![Validación del Proyecto](https://github.com/pjennedyth-blip/festival-devops-2026-/actions/workflows/ci.yml/badge.svg)](https://github.com/pjennedyth-blip/festival-devops-2026-/actions/workflows/ci.yml)


# Festival DevOps Music Fest

## Descripción

Proyecto desarrollado para la gestión del Festival DevOps Music Fest. Incluye un frontend y un backend, además de un flujo de Integración Continua (CI) mediante GitHub Actions para validar automáticamente la estructura del proyecto.

## Estructura del proyecto

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── frontend/
│   ├── index.html
│   └── css/
│       └── style.css
├── backend/
│   └── js/
│       └── script.js
├── docker-compose.yml
└── README.md
```

## Tecnologías utilizadas

* HTML
* CSS
* Python
* Flask
* Docker
* Docker Compose
* Git
* GitHub
* GitHub Actions

## Docker

Se utilizaron Dockerfiles para crear las imágenes del frontend y backend.

## Docker Compose

Se utilizó Docker Compose para ejecutar los servicios del proyecto de manera conjunta.

## Git

Se utilizó Git para el control de versiones mediante commits, ramas y merges.

## GitHub

Se utilizó GitHub como repositorio remoto para almacenar y compartir el proyecto.

## Integración Continua (CI)

El proyecto utiliza GitHub Actions para ejecutar un workflow de validación automáticamente en cada **Push** y **Pull Request**.

El workflow verifica que existan los siguientes archivos:

* `frontend/index.html`
* `frontend/css/style.css`
* `backend/js/script.js`
* `README.md`

Si alguno de estos archivos no existe, la ejecución del workflow finaliza con error.

## Autor

* Tu nombre
* Junio 2026
