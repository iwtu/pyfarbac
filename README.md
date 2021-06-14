# Python FastAPI pydantic Bug
This git repo should demonstrate reported [bug](https://github.com/samuelcolvin/pydantic/issues/2907).

## Description

`RBACBase` class inherits from `pydantic.BaseModel` and adds its own `root_validator`. Classes (models) who inherits from `RBACBase` should use the `root_validator` validator. 

`RBACBase` validator filters out model attributes based on role. It means that I return always the same model from the same route (endpoint) but base on user's role not all attributes are visisble to the user.

Roles and attributes can be read/store from/to a config file. 

## Version:
 - Python 3.8
 - FastAPI 0.63.0
 - pydantic 1.8.1
 
## How I run FastAPI
`gunicorn -k uvicorn.workers.UvicornWorker --bind localhost:9000 pyfarbac.main:app`
