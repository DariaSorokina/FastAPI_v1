from contextlib import asynccontextmanager

import uvicorn
from fastapi.openapi.utils import get_openapi

from core.config import settings
from core.models import Base, db_helper
from api_v1 import router as router_v1

from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    #async with db_helper.engine.begin() as conn:
        #await conn.run_sync(Base.metadata.create_all)
        #print("База готова к работе")
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)
    #     print("Очистка базы")
    yield


app = FastAPI(lifespan=lifespan, docs_url=None, redoc_url=None)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="https://unpkg.com/redoc@next/bundles/redoc.standalone.js",
    )


def my_schema():
    openapi_schema = get_openapi(
        title="Распределенные информационные системы",
        version="1.0",
        routes=app.routes,
    )
    openapi_schema["info"] = {
        "title": "Распределенные информационные системы",
        "version": "1.0",
        "description": "Задание выполнила Сорокина Дарья Борисовна, студент группы: Z3410МК"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = my_schema


@app.get("/users/{id}")
def users(id):
    return {"user_id": id}
