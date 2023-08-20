import contextlib
import logging
import sys
from sqlite3 import OperationalError

import aiosqlite
from aiosqlite import Connection

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
