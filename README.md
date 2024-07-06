# Cookiecutter FastAPI Template for AIML OPS Projects

## Introduction

This template helps you quickly set up a FastAPI project tailored for AIML operations (AIML OPS). Follow the steps below to create a robust project structure.

## Project Structure

### Creating the Directory Structure

Use the following commands to set up the initial directory structure for your FastAPI project:

```bash
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
```

### Explanation of Key Files

- `app/api/endpoints/health.py`: Endpoint for health checks.
- `app/api/endpoints/predict.py`: Endpoint for model predictions.
- `app/core/config.py`: Configuration settings for the application.
- `app/schemas/health.py`: Pydantic models for health check responses.
- `app/schemas/predict.py`: Pydantic models for prediction requests and responses.
- `app/main.py`: Main application entry point.
- `app/requirements.txt`: List of dependencies.
- `.env`: Environment variables.
- `.gitignore`: Files and directories to ignore in Git.
- `README.md`: Project documentation.
- `setup.py`: Script for setting up the project.

## Running Cookiecutter

To generate the project structure with Cookiecutter, run the following command:

```bash
cookiecutter cookiecutter-fastapi-template
```

This command will prompt you for the project details and generate the project directory structure accordingly.

## Python Environment Setup Script

This script sets up a Python environment on both macOS and Windows. It installs Python (if not already installed), creates a virtual environment, and installs some common packages.

### Prerequisites

- Ensure `curl` and `wget` are installed on your system for downloading files.
- For Windows, PowerShell must be available.

### Script Files

#### macOS/Linux (`setup_env.sh`)

```bash
#!/bin/bash

# Check for Homebrew, install if not found
if ! command -v brew &> /dev/null
then
    echo "Homebrew not found, installing..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Check for Python, install if not found
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found, installing..."
    brew install python
fi

# Create a virtual environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install common packages
pip install numpy pandas scikit-learn fastapi uvicorn

echo "Setup complete. To activate the virtual environment, run 'source venv/bin/activate'."
```

#### Windows (`setup_env.ps1`)

```powershell
# Check for Chocolatey, install if not found
if (-Not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Output "Chocolatey not found, installing..."
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
}

# Check for Python, install if not found
if (-Not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Output "Python not found, installing..."
    choco install python -y
    refreshenv
}

# Create a virtual environment
if (-Not (Test-Path -Path "venv")) {
    python -m venv venv
    Write-Output "Virtual environment created."
} else {
    Write-Output "Virtual environment already exists."
}

# Activate the virtual environment
& .\venv\Scripts\Activate

# Upgrade pip
pip install --upgrade pip

# Install common packages
pip install numpy pandas scikit-learn fastapi uvicorn

Write-Output "Setup complete. To activate the virtual environment, run '.\venv\Scripts\Activate'."
```

### Running the Script

#### On macOS/Linux:
1. Save the script as `setup_env.sh`.
2. Make the script executable:
   ```bash
   chmod +x setup_env.sh
   ```
3. Run the script:
   ```bash
   ./setup_env.sh
   ```

#### On Windows:
1. Save the script as `setup_env.ps1`.
2. Open PowerShell with administrative privileges.
3. Run the script:
   ```powershell
   .\setup_env.ps1
   ```

This script ensures Python and the necessary packages are installed, and it creates and activates a virtual environment for your projects.