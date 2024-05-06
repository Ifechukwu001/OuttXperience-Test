# OuttXperience Test

## Objective:
Your task is to develop a simple CRUD (Create, Read, Update, Delete) application using FastAPI and SQLAlchemy. This application will manage a database of books.

## Setup
- To run the application locally, ensure your computer has the following installed:
    - Python (3.9+)
    - Docker (Optional, to build a container)

- If you satisfy the above requirements, then clone this repository
    ```bash
        git clone https://github.com/Ifechukwu001/OuttXperience-Test.git ifechukwu001
    ```

- Change your directory
    ```bash
        cd ifechukwu001
    ```

- Create a virtual environment and  activate it.
    ```bash
        python -m venv venv
        source venv/bin/activate
    ```

- Install all dependency packages.
    ```bash
        pip install -U pip
        pip install -r requirements.txt
    ```

- Run the FastApi dev server
    ```bash
        fastapi dev src/app/main.py
    ```

## Tests

The tests are created using the pytest library and located in the tests module.

To run the tests (ensure that requirements are installed as shown in [setup](#setup))
```bash
    pytest -v
```

## Container

An image can be created for the application from the Dockerfile. 

To build the image, from the root of the repository run the command (docker must be installed):
```bash
    docker build -t ifechukwu001:v1 .
```

