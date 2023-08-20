# coding: utf-8
from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status, HTTPException,
)

router = APIRouter()


@router.get(
    "/ws",
    responses={
        101: {"description": "WebSocket connection established"},
        426: {"description": "Upgrade Required"},
    },
    tags=["default"],
    summary="WebSocket connection for real-time order information",
    response_model_by_alias=True,
)
async def web_socket_connect(
) -> None:
    pass
