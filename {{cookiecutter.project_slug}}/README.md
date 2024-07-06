# {{ cookiecutter.project_name }}

## Setup

1. Create a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

2. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

4. Open your browser at `http://127.0.0.1:8000/docs` to see the API documentation.
