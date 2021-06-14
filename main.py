from fastapi import FastAPI

app = FastAPI(debug=False)

from .routers.router import router as rrouter

app.include_router(
    rrouter,
    prefix="/api",
    tags=["FOO"]
)

import pydantic
print(pydantic.utils.version_info())
