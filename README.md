# API-Template-Python
A Python based API Template built on FastAPI framework for ML and AI applications.

## Set Environment (Anaconda)
```
conda create -n api python=3.11.4
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

## Test Coverage
```
---------- coverage: platform win32, python 3.11.4-final-0 -----------
Name                                              Stmts   Miss  Cover
---------------------------------------------------------------------
src\api\__init__.py                                   0      0   100%
src\api\config.py                                    12      0   100%
src\api\events\__init__.py                            0      0   100%
src\api\events\shutdown.py                            5      2    60%
src\api\events\startup.py                             5      2    60%
src\api\loggers\__init__.py                           0      0   100%
src\api\loggers\custom_logger.py                     19      3    84%
src\api\loggers\handlers\__init__.py                  0      0   100%
src\api\loggers\handlers\get_console_handler.py       9      0   100%
src\api\loggers\handlers\get_file_handler.py          8      0   100%
src\api\middlewares\__init__.py                       0      0   100%
src\api\middlewares\process_time_middleware.py       10      0   100%
src\api\middlewares\request_id_middleware.py         11      0   100%
src\api\routers\__init__.py                           0      0   100%
src\api\routers\home.py                               5      0   100%
src\api\routers\metadata.py                           7      0   100%
src\api\routers\sample_router.py                     11      3    73%
src\api\schemas\__init__.py                           0      0   100%
src\api\schemas\input_schema.py                       7      0   100%
src\api\schemas\output_schema.py                      6      0   100%
src\api\services\__init__.py                          0      0   100%
src\api\services\get_full_name.py                     3      2    33%
src\api\utils\__init__.py                             0      0   100%
src\api\utils\generate_output.py                      9      6    33%
src\api\utils\modify_request_validator.py            10      3    70%
src\api\utils\modify_response_validator.py           10      3    70%
src\api\utils\object_to_dict.py                       8      6    25%
src\main.py                                          20      0   100%
---------------------------------------------------------------------
TOTAL                                               175     30    83%

=================== 6 passed, 12 warnings in 0.75s ====================
```
