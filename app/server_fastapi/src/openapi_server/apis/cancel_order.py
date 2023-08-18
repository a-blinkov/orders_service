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
        result = await db.execute(
            f"""
                SELECT * FROM orders
                WHERE id = "{orderId}" 
            """
        )
        result = await result.fetchall()
        if not result:
            raise HTTPException(status_code=404, detail="Order not found")

        await db.execute(
            f"""
                DELETE FROM orders
                WHERE id = "{orderId}" 
            """
        )
        await db.commit()
