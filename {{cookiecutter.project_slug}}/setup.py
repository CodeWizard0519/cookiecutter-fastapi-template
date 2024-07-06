from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_slug }}",
    version="0.1.0",
    author="{{ cookiecutter.author_name }}",
    packages=find_packages(),
    install_requires=[
        "fastapi=={{ cookiecutter.fastapi_version }}",
        "uvicorn[standard]==0.13.4",
        "pandas==1.2.4"
    ],
)
