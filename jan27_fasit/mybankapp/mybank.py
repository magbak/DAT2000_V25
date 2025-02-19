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
            conn.execute("""
                CREATE TABLE funds (
                    name varchar(255),
                    amount float8
                )
                """)

    def add_customer(self, name:str, amount:float):
        with self.pool.connection() as conn:
            conn.execute("""
                INSERT INTO funds (name, amount) VALUES (%s, %s)
                """, (name, amount))

    def get_amount(self, name:str) -> Optional[float]:
        with self.pool.connection() as conn:
            res = conn.execute("""
                SELECT amount from funds WHERE name = %s
                """, (name,))
            amount = res.fetchone()
            if amount is None:
                return None
            else:
                return amount[0]

    # Se "examples" her https://www.postgresql.org/docs/current/sql-update.html
    def transfer(self, src:str, trg:str, amount:float) -> bool:
        # Ooops! This code should be implemented with transactions!
        # Todo later in the semester
        amount_src = self.get_amount(src)
        if amount_src is None:
            return False
        # Src må ha dekning på konto:
        elif amount_src < amount:
            return False

        amount_trg = self.get_amount(trg)
        if amount_trg is None:
            return False

        with self.pool.connection() as conn:
            # Nå tapper vi src sin konto for amount.
            new_amount_src = amount_src - amount
            conn.execute("""
                UPDATE funds SET amount = %s WHERE name = %s
                """, (new_amount_src, src))

            new_amount_trg = amount_trg + amount
            # Nå setter vi inn pengene hos trg
            conn.execute("""
                UPDATE funds SET amount = %s WHERE name = %s
                """, (new_amount_trg, trg))

        return True