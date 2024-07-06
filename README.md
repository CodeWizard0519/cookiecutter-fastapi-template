# cookiecutter-fastapi-template
Template for AIML OPS Project with FastAPI

    cookiecutter cookiecutter-fastapi-template

How this template created ?

    mkdir -p cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/api/endpoints
    mkdir -p cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/core
    mkdir -p cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/models
    mkdir -p cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/schemas
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/api/__init__.py
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/api/endpoints/__init__.py
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/api/endpoints/health.py
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/api/endpoints/predict.py
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/core/__init__.py
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/core/config.py
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/models/__init__.py
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/schemas/__init__.py
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/schemas/health.py
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/schemas/predict.py
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/main.py
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/app/requirements.txt
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/.env
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/.gitignore
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/README.md
    touch cookiecutter-fastapi-template/{{cookiecutter.project_slug}}/setup.py
