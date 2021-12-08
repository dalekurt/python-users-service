import copy
from collections import defaultdict
from typing import Any, DefaultDict, Dict, Optional

from fastapi import APIRouter, Request
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html

custom_openapi: DefaultDict[str, Optional[Dict[str, Any]]] = defaultdict(lambda: None)


def create_versioning_docs(router: APIRouter) -> None:
    prefix = router.prefix

    @router.get("/openapi.json", include_in_schema=False, name=f"{prefix}_openapi")
    async def get_openapi_json(request: Request):
        global custom_openapi
        version = request.url.path.strip("/").split("/")[0]
        if custom_openapi[version] is None:
            custom_openapi[version] = copy.deepcopy(request.app.openapi())

            # Remove other version tags on openapi schema.
            for path in custom_openapi[version]["paths"].copy():
                if not path.startswith(f"/{version}"):
                    del custom_openapi[version]["paths"][path]

        return custom_openapi[version]

    @router.get("/docs", include_in_schema=False, name=f"{prefix}_swagger")
    async def get_swagger(request: Request):
        return get_swagger_ui_html(
            openapi_url=f"{prefix}/openapi.json",
            title=request.app.title + " - Swagger UI",
        )

    @router.get("/redoc", include_in_schema=False, name=f"{prefix}_redoc")
    async def redoc_html(request: Request):
        return get_redoc_html(
            openapi_url=f"{prefix}/openapi.json", title=request.app.title + " - ReDoc"
        )
