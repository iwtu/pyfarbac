from fastapi import APIRouter
from ..models.foo import OutputFoo
from ..models.rbac import set_context_role

router = APIRouter()

@router.get("/", response_model=OutputFoo)
async def get():
    print(f"Real fullname: {OutputFoo.__module__}.{OutputFoo.__name__}")
    set_context_role("arole")
    response = {
        "f1" : 42,
        "f2" : "f2 of OutputFoo"
    }

    return response