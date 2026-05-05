# Playwright SauceDemo Automation

Automatización simple de una app web de prueba usando **Python + Playwright + Pytest**.

Este proyecto automatiza un flujo básico de compra en la página de práctica [Sauce Demo](https://www.saucedemo.com/).

## Objetivo del proyecto

Demostrar un uso inicial de Playwright para automatización web end-to-end.

El flujo automatizado realiza:

1. Apertura de la página Sauce Demo.
2. Login con credenciales válidas.
3. Validación de ingreso correcto.
4. Agregado de producto al carrito.
5. Proceso de checkout.
6. Finalización de compra.
7. Generación de evidencia mediante screenshot.

## Tecnologías utilizadas

- Python
- Playwright
- Pytest
- Chromium

## Estructura del proyecto

```text
playwright-saucedemo-automation/
├── evidence/
│   └── screenshots/
│       └── compra_exitosa.png
├── tests/
│   └── test_compra_exitosa_saucedemo.py
├── .gitignore
├── README.md
└── requirements.txt

```

Instalación

Crear y activar entorno virtual:

python3 -m venv venv
source venv/bin/activate

Instalar dependencias:

pip install -r requirements.txt

Instalar navegador Chromium para Playwright:

playwright install chromium
Ejecución de la prueba

Ejecutar la prueba mostrando el navegador:

pytest tests/test_compra_exitosa_saucedemo.py --headed --browser chromium

Ejecutar la prueba sin mostrar el navegador:

pytest tests/test_compra_exitosa_saucedemo.py --browser chromium


## Ejecución automática con GitHub Actions

Este proyecto incluye un workflow de GitHub Actions para ejecutar la prueba automatizada cada vez que se suben cambios a la rama `main`.

El workflow realiza los siguientes pasos:

1. Descarga el código del repositorio.
2. Configura Python.
3. Instala las dependencias del proyecto.
4. Instala Chromium para Playwright.
5. Ejecuta la prueba automatizada.
6. Guarda la evidencia generada como artifact.

El archivo del workflow se encuentra en:


.github/workflows/playwright-tests.yml


Evidencia generada


Al finalizar correctamente la prueba, se genera una captura en:

evidence/screenshots/compra_exitosa.png
Resultado esperado

La prueba debe finalizar con:

1 passed

Y debe validar el mensaje final:

Thank you for your order!
Aprendizaje demostrado

Este proyecto demuestra conocimientos iniciales en:

Automatización web end-to-end.
Uso de locators en Playwright.
Validaciones con assertions.
Organización básica de proyecto Python.
Generación de evidencia para pruebas QA.
Preparación de repositorio técnico para GitHub.
Autor

Ricardo Tapia