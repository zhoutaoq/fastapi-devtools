## fastapi-devtools
### Description
- fastapi + poetry web project

### Quick start

- pip install  
```shell
pip install fastapi
pip install poetry
```

- init project
```shell
poetry new fastapi-devtools
cd fastapi-devtools
poetry init
poetry add fastapi
poetry install
```

- start service
```shell
poetry run uvicorn main:app --port 7000 --reload
```


