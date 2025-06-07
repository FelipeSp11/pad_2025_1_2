# Proyecto PAD: Automatización de Extracción e Ingesta de Datos con DevOps

## 📝 Autores

* **León Felipe Sánchez Palacio**

## 📚 Descripción del Proyecto

Este proyecto forma parte de la asignatura de Programación para Análisis de Datos (PAD) y tiene como objetivo principal demostrar un flujo de trabajo DevOps completo y automatizado para la extracción y gestión de datos. La aplicación desarrollada extrae información de una página web específica (referente a precios históricos del oro), procesa los datos y los persiste en una base de datos local. Todo el proceso está encapsulado en contenedores Docker y orquestado mediante un pipeline de Integración Continua y Despliegue Continuo (CI/CD) implementado con GitHub Actions.

Se hace énfasis en las siguientes prácticas:
* **Control de Versiones:** Gestión robusta del código fuente utilizando Git y GitHub.
* **Contenerización:** Empaquetado de la aplicación en imágenes Docker para asegurar la portabilidad y la consistencia del entorno.
* **CI/CD:** Automatización de la construcción, prueba y despliegue de la aplicación a través de GitHub Actions.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje de Programación:** Python 3.9+
* **Librerías Python:**
    * `BeautifulSoup4`: Para el web scraping.
    * `pandas`: Para la manipulación y análisis de datos.
    * Otras librerías
* **Contenerización:** Docker
* **Control de Versiones:** Git
* **Plataforma de Repositorio:** GitHub
* **CI/CD:** GitHub Actions


## 📁 Estructura del Repositorio

El repositorio está organizado de la siguiente manera:
├── .github/                 # Configuraciones de GitHub
│   └── workflows/           # Workflows de GitHub Actions para CI/CD
│       └── accionables.yml  # Definición del pipeline CI/CD
├── src/                     # Código fuente de la aplicación
│   └── edu_pad/             # Paquete principal de la aplicación
│       ├── init.py
│       ├── database.py      # Módulo para la interacción con la base de datos
│       ├── main_extractor.py # Script principal para la extracción y procesamiento de datos
│       ├── main_ingesta.py   # Script principal para la ingesta de datos
│       └── static/          # Archivos estáticos, como CSVs y DBs
│           ├── csv/         # Directorio para archivos CSV (input/output)
│           └── db/          # Directorio para archivos de base de datos
├── Dockerfile               # Definición de la imagen Docker de la aplicación
├── requirements.txt         # Dependencias de Python
└── README.md                # Este archivo

## 🚀 Flujo de Trabajo DevOps Implementado

El corazón de este proyecto es su pipeline de CI/CD, que automatiza el ciclo de vida del software desde el desarrollo hasta el despliegue.

### 1. Control de Versiones (Git & GitHub)

* Utilizamos un flujo de trabajo de Git basado en ramas, donde `main` es la rama principal que representa la versión estable y desplegable del código.
* Cada nueva funcionalidad o corrección se desarrolla en una rama separada.
* Los `pull requests` se utilizan para revisar y fusionar el código en la rama `main`, garantizando la calidad y la colaboración.

### 2. Contenerización (Docker)

* **Dockerfile:** El `Dockerfile` en la raíz del repositorio define cómo construir la imagen Docker de la aplicación. Esta imagen incluye Python, todas las dependencias necesarias y el código fuente del proyecto. Esto asegura que el entorno de ejecución de la aplicación sea idéntico en desarrollo y en el pipeline de CI/CD.
* **Imagen `contenedor`:** Se construye una imagen Docker con el nombre `contenedor`  que encapsula toda la lógica de extracción e ingesta de datos.

### 3. Pipeline de CI/CD (GitHub Actions)

El archivo `.github/workflows/docker.yml` define el pipeline de CI/CD que se activa automáticamente con cada `push` a la rama `main`.

**Pasos del Workflow:**

1.  **`name: Paso 5 - Ejecutar ingesta`**: (Ajusta el nombre del paso principal si tu workflow tiene más funcionalidades o está enfocado en `extractor` o `ingesta`).
2.  **`on: push: branches: [main]`**: El workflow se dispara automáticamente cada vez que se realiza un `push` a la rama `main`.
3.  **`jobs: build: runs-on: ubuntu-latest`**: El pipeline se ejecuta en un ambiente Linux (ubuntu-latest).
4.  **`steps:`**:
    * **`Checkout repo`**: Clona el repositorio en el runner de GitHub Actions.
    * **Configuración del Entorno Docker:**
        * (Opcional, si tu Dockerfile es complejo o si necesitas construir la imagen en el workflow): Se podría añadir un paso `docker build -t contenedor .` aquí para construir la imagen antes de ejecutarla.
    * **Ejecución de Módulos Python en Docker:**
        * Los scripts `main_extractor.py` y `main_ingesta.py` se ejecutan dentro del contenedor Docker. Esto asegura que la aplicación se ejecute en un ambiente aislado y reproducible, con todas las dependencias preinstaladas en la imagen.
        * **Mapeo de Volúmenes:** Se utilizan volúmenes (`-v`) para persistir datos y permitir la comunicación entre el host (el runner de GitHub Actions) y el contenedor.
            * `-v "${{ github.workspace }}/static/csv":/src/edu_pad/static/csv`: Mapea la carpeta `static/csv` del repositorio a `/src/edu_pad/static/csv` dentro del contenedor. Esto permite que el script `main_ingesta.py` lea el `data_webdb.csv` (generado previamente por `main_extractor.py` o existente en el repo) y que `main_extractor.py` guarde su salida.
            * `-v "${{ github.workspace }}/static/db":/src/edu_pad/static/db`: Mapea la carpeta `static/db` del repositorio a `/src/edu_pad/static/db` dentro del contenedor, asegurando que la base de datos sea accesible y que los cambios se persistan.
        * **Comando de Ejecución:** `contenedor python -m edu_pad.main_ingesta` (o `edu_pad.main_extractor` para el otro paso). Este comando le dice a Docker que use la imagen `contenedor` y ejecute el módulo Python especificado.

5.  **Despliegue Continuo (Sincronización de Artefactos):**
    * `stefanzweifel/git-auto-commit-action@v4`: Esta acción automáticamente hace un commit y push de los cambios. Esto simula un despliegue continuo de los datos procesados en el propio repositorio.

## 🚀 Cómo Ejecutar el Proyecto (Localmente)

Para ejecutar este proyecto localmente fuera del pipeline de CI/CD:

### Prerequisitos

* Docker Desktop (o Docker Engine) instalado y en ejecución.
* Python 3.9+ instalado.
* Git instalado.

### Pasos

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/FelipeSp11/pad_2025_1_2.git](https://github.com/FelipeSp11/pad_2025_1_2.git)
    cd pad_2025_1_2
    ```

2.  **Construir la imagen Docker:**
    ```bash
    docker build -t contenedor .
    ```
    Esto creará una imagen Docker llamada `contenedor` a partir de tu `Dockerfile`.

3.  **Ejecutar el proceso de Extracción (Extractor):**
    Asegúrate de que la carpeta `static/csv` exista en tu directorio local.
    ```bash
    mkdir -p static/csv static/db
    docker run --rm \
    -v "$(pwd)/static/csv":/src/edu_pad/static/csv \
    -v "$(pwd)/static/db":/src/edu_pad/static/db \
    contenedor python -m edu_pad.main_extractor
    ```
    Este comando ejecutará el `main_extractor.py` dentro del contenedor. El archivo `data_webdb.csv` (y otros que `extractor` genere) se guardará en tu carpeta `static/csv` local.

4.  **Ejecutar el proceso de Ingesta (Ingesta):**
    Asegúrate de que el `data_webdb.csv` exista en `static/csv` y que la carpeta `static/db` esté lista.
    ```bash
    docker run --rm \
    -v "$(pwd)/static/csv":/src/edu_pad/static/csv \
    -v "$(pwd)/static/db":/src/edu_pad/static/db \
    contenedor python -m edu_pad.main_ingesta
    ```
    Este comando ejecutará el `main_ingesta.py`, leyendo el CSV y procesando los datos en la base de datos.


  
## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles. (Crea un archivo LICENSE si no lo tienes).

---