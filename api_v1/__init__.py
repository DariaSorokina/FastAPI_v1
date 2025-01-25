from fastapi import APIRouter

from .products.views import router as products_router
from .acters.views import router as acter_router
from .posters.views import router as poster_router
from .tickets.views import router as ticket_router
from .show.views import router as show_router

router = APIRouter()
router.include_router(router=products_router, prefix="/products")
router.include_router(router=acter_router, prefix="/acters")
router.include_router(router=poster_router, prefix="/poster")
router.include_router(router=ticket_router, prefix="/ticket")
router.include_router(router=show_router, prefix="/show")