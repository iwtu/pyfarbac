from fastapi import APIRouter

router = APIRouter()

from .foo import router as foo_router
router.include_router(
    foo_router,
    prefix="/foo"
)