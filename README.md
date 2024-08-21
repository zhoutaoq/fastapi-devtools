## fastapi-devtools
### Description
- fastapi + poetry web project

### Environmental preparation

- python >= 3.8

### Quick start

- pip install  
```shell
pip install fastapi
pip install poetry
```
```markdown
You need to add the storage path of poetry to your system's environment variables
```


- lib install
```shell
cd fastapi-devtools
poetry add fastapi
poetry install
```

- start service
```shell
poetry run uvicorn main:app --port 8000 --reload
```


