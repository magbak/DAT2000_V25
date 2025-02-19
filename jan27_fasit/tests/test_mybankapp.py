import pytest
#PyCharm sliter litt med denne importen fordi vi har en subfolder, men pytest kjører fint..
from mybankapp import MyBank
from psycopg import connect

CONNSTR = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"

@pytest.fixture(scope='function')
def mybank() -> MyBank:
    # Vi gjør dette for å starte med blanke ark hver gang
    with connect(CONNSTR) as connection:
        connection.execute("DROP TABLE IF EXISTS funds")
    m = MyBank(CONNSTR)
    m.init_db()
    print("Initialization done")
    return m


def test_mybankapp_add_customer(mybank):
    mybank.add_customer("Ola", 1000.0)
    assert mybank.get_amount("Ola") == 1000.0

def test_transfer(mybank):
    mybank.add_customer("Ola", 750.0)
    mybank.add_customer("Kari", 100.0)
    result = mybank.transfer("Ola", "Kari", 500.0)
    # Legg til asserts som sjekker at dette gikk riktig gjennom her!