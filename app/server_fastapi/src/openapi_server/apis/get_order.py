# coding: utf-8
import asyncio
import random
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
from models.order_output import OrderOutput
from sqlite.db_conn import connect_orders_db

router = APIRouter()



@router.get(
    "/orders/{orderId}",
    responses={
        200: {"model": OrderOutput, "description": "Order found"},
        404: {"model": Error, "description": "Order not found"},
    },
    tags=["default"],
    summary="Retrieve a specific order",
    response_model_by_alias=True,
)
async def get_order(
    orderId: str = Path(description=""),
) -> OrderOutput:
    await asyncio.sleep(random.uniform(0.1, 1))
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
    return [OrderOutput.from_dict(dict(db_order_data)) for db_order_data in result][0]

