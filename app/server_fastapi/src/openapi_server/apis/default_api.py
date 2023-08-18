# # coding: utf-8
# import uuid
# from typing import Dict, List  # noqa: F401
#
# from fastapi import (  # noqa: F401
#     APIRouter,
#     Body,
#     Cookie,
#     Depends,
#     Form,
#     Header,
#     Path,
#     Query,
#     Response,
#     Security,
#     status, HTTPException,
# )
# from pydantic_core import ValidationError
#
# from models.error import Error
# from models.order_input import OrderInput
# from models.order_output import OrderOutput
# from sqlite.db_conn import connect_orders_db
#
# router = APIRouter()
#
#
# @router.delete(
#     "/orders/{orderId}",
#     responses={
#         204: {"description": "Order canceled"},
#         404: {"model": Error, "description": "Order not found"},
#     },
#     tags=["default"],
#     summary="Cancel an order",
#     response_model_by_alias=True,
# )
# async def cancel_order(
#     orderId: str = Path(description=""),
# ) -> None:
#     async with connect_orders_db() as db:
#         result = await db.execute(
#             f"""
#                 SELECT * FROM orders
#                 WHERE id = "{orderId}"
#             """
#         )
#         result = await result.fetchall()
#         if not result:
#             raise HTTPException(status_code=404, detail="Order not found")
#
#         await db.execute(
#             f"""
#                 DELETE FROM orders
#                 WHERE id = "{orderId}"
#             """
#         )
#         await db.commit()
#
#
# @router.get(
#     "/orders/{orderId}",
#     responses={
#         200: {"model": OrderOutput, "description": "Order found"},
#         404: {"model": Error, "description": "Order not found"},
#     },
#     tags=["default"],
#     summary="Retrieve a specific order",
#     response_model_by_alias=True,
# )
# async def get_order(
#     orderId: str = Path(description=""),
# ) -> OrderOutput:
#     async with connect_orders_db() as db:
#         result = await db.execute(
#             f"""
#                 SELECT * FROM orders
#                 WHERE id = "{orderId}"
#             """
#         )
#         result = await result.fetchall()
#         if not result:
#             raise HTTPException(status_code=404, detail="Order not found")
#     return [OrderOutput.from_dict(dict(db_order_data)) for db_order_data in result][0]
#
#
# @router.get(
#     "/orders",
#     responses={
#         200: {"model": List[OrderOutput], "description": "A list of orders"},
#     },
#     tags=["default"],
#     summary="Retrieve all orders",
#     response_model_by_alias=True,
# )
# async def get_orders(
# ) -> List[OrderOutput]:
#     async with connect_orders_db() as db:
#         result = await db.execute(
#             "SELECT * FROM orders"
#         )
#         result = await result.fetchall()
#     return [OrderOutput.from_dict(dict(db_order_data)) for db_order_data in result]
#
#
# @router.post(
#     "/orders",
#     responses={
#         201: {"model": OrderOutput, "description": "Order placed"},
#         400: {"model": Error, "description": "Invalid input"},
#     },
#     tags=["default"],
#     summary="Place a new order",
#     response_model_by_alias=True,
# )
# async def place_order(
#     order_input: OrderInput = Body(None, description="Order information"),
# ) -> OrderOutput:
#     stoks = f'"{order_input.stoks}"' if order_input.stoks else 'Null'
#     quantity = f'"{order_input.quantity}"' if order_input.quantity else 'Null'
#     try:
#         order_id = str(uuid.uuid4())
#         async with connect_orders_db() as db:
#             await db.execute(
#                 'INSERT INTO orders("id", "stoks", "quantity")'
#                 f'VALUES("{order_id}", {stoks}, {quantity})'
#             )  # TODO: use ORM, f.e. SqlAlchemy
#             await db.commit()
#
#             return await get_order(order_id)
#     except ValidationError:
#         raise HTTPException(status_code=400, detail=f"Invalid input")
#
#
# @router.get(
#     "/ws",
#     responses={
#         101: {"description": "WebSocket connection established"},
#         426: {"description": "Upgrade Required"},
#     },
#     tags=["default"],
#     summary="WebSocket connection for real-time order information",
#     response_model_by_alias=True,
# )
# async def web_socket_connect(
# ) -> None:
#     pass
