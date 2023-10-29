# API-Template-Python
A Python based API Template built on FastAPI framework for ML and AI applications.

## Set Environment (Anaconda)
```
conda create -n api python=3.11.5
conda activate api
cd API-Template-Python
pip install -r .\requirements.txt
```

## Run API
```
cd API-Template-Python\src
uvicorn main:app
```

## Test & Coverage
```
cd API-Template-Python
pytest --cov=src
```

## Terminate All Python Processses
```
taskkill /f /im python.exe
```
