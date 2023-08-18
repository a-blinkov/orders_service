import contextlib
from sqlite3 import OperationalError

import sys
import aiosqlite
import asyncio
import logging

from aiosqlite import Connection

from models.order_input import OrderInput

logger = logging.getLogger('sqlite')
hdlr = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


@contextlib.asynccontextmanager
async def connect_orders_db() -> Connection:
    async with aiosqlite.connect("orders.db") as db:
        try:
            await db.execute(
                """
                CREATE TABLE orders (
                unique_id integer primary key autoincrement, id string, stoks string, quantity float, status string
                )
                """
            )
        except OperationalError as error:
            logger.info(f'Fetched exception during table creation: {error}')
        db.row_factory = aiosqlite.Row
        yield db


if __name__ == '__main__':
    async def connect():
        async with connect_orders_db() as db:
            await db.execute(
                """
                INSERT INTO orders ('stoks', 'quantity')
                VALUES ('EURRUB', 1.23)
                """
            )
            await db.commit()
            res = await db.execute(
                """
                SELECT * FROM orders
                """
            )
            res = await res.fetchall()
        print([dict(result) for result in res])
    asyncio.run(connect())