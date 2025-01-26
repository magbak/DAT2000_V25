from typing import Optional
from psycopg_pool import ConnectionPool

class MyBank:
    def __init__(self, connstr:str):
        self.pool = ConnectionPool(connstr)

    def __del__(self):
        self.pool.close()

    def init_db(self):
        #Bruk dette mønsteret også på de andre funksjonene
        with self.pool.connection() as conn:
            conn.execute(...)

    def add_customer(self, name:str, amount:float):
        pass

    def get_amount(self, name:str) -> Optional[float]:
        pass

    # Se "examples" her https://www.postgresql.org/docs/current/sql-update.html
    def transfer(self, src:str, trg:str, amount:float) -> bool:
        pass
