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

from apis.get_order import get_order
from models.error import Error
from sqlite.db_conn import connect_orders_db

router = APIRouter()


@router.delete(
    "/orders/{orderId}",
    responses={
        204: {"description": "Order canceled"},
        404: {"model": Error, "description": "Order not found"},
    },
    tags=["default"],
    summary="Cancel an order",
    response_model_by_alias=True,
)
async def cancel_order(
    orderId: str = Path(description=""),
) -> None:
    async with connect_orders_db() as db:
        await get_order(orderId)
        await db.execute(
            f"""
                DELETE FROM orders
                WHERE id = "{orderId}" 
            """
        )
        await db.commit()
