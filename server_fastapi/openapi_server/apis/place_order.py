# coding: utf-8
import asyncio
import random
import uuid
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
from pydantic_core import ValidationError

from apis.get_order import get_order
from models.error import Error
from models.order_input import OrderInput
from models.order_output import OrderOutput
from sqlite.db_conn import connect_orders_db

router = APIRouter()


@router.post(
    "/orders",
    responses={
        201: {"model": OrderOutput, "description": "Order placed"},
        400: {"model": Error, "description": "Invalid input"},
    },
    tags=["default"],
    summary="Place a new order",
    response_model_by_alias=True,
)
async def place_order(
    order_input: OrderInput = Body(None, description="Order information"),
) -> OrderOutput:
    await asyncio.sleep(random.uniform(0.1, 1))

    stoks = f'"{order_input.stoks}"' if order_input.stoks is not None else 'Null'
    quantity = f'"{order_input.quantity}"' if order_input.quantity is not None else 'Null'
    try:
        order_id = str(uuid.uuid4())
        async with connect_orders_db() as db:
            await db.execute(
                'INSERT INTO orders("id", "stoks", "quantity")'
                f'VALUES("{order_id}", {stoks}, {quantity})'
            )  # TODO: use ORM, f.e. SqlAlchemy
            await db.commit()

            return await get_order(order_id)
    except ValidationError:
        raise HTTPException(status_code=400, detail=f"Invalid input")

