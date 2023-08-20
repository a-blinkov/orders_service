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

from models.order_output import OrderOutput
from sqlite.db_conn import connect_orders_db

router = APIRouter()


@router.get(
    "/orders",
    responses={
        200: {"model": List[OrderOutput], "description": "A list of orders"},
    },
    tags=["default"],
    summary="Retrieve all orders",
    response_model_by_alias=True,
)
async def get_orders(
) -> List[OrderOutput]:
    await asyncio.sleep(random.uniform(0.1, 1))
    async with connect_orders_db() as db:
        result = await db.execute(
            "SELECT * FROM orders"
        )
        result = await result.fetchall()
    return [OrderOutput.from_dict(dict(db_order_data)) for db_order_data in result]
