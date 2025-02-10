import pytest
import random
from MyKVStore import Store

@pytest.fixture(scope="function")
def store():
    table = [(f"MyKey{str(i).rjust(5, "0")}", f"MyValue{i%1000}") for i in range(100_000)]
    random.shuffle(table)
    return Store(table)

def test_get_naive_has_method(store):
    assert "get_naive" in dir(store), "Method 'get_naive' not found."

def test_get_naive_1(store):
    assert store.get_naive("MyKey00000") == "MyValue0"

def test_get_naive_2(store):
    assert store.get_naive("MyKey01000") == "MyValue0"

def test_get_naive_3(store):
    assert store.get_naive("MyKey01001") == "MyValue1"

def test_get_naive_4(store):
    assert store.get_naive("MyKey99999") == "MyValue999"

def test_get_naive_5(store):
    assert store.get_naive("MyKey100000") is None

def test_create_sparse_index_has_method(store):
    assert "create_sparse_index" in dir(store), "Method 'create_sparse_index' not found."

def test_create_sparse_index_1(store):
    sparse = store.create_sparse_index()
    assert (store.table[0][0],0) == sparse[0]

def test_create_sparse_index_2(store):
    assert (store.table[100][0],100) == store.sparse_index[1]

def test_create_sparse_index_3(store):
    assert (store.table[99900][0],99900) == store.sparse_index[999]

def test_get_interval_1(store):
    assert store.get_interval("MyKey00000") == (0,100)

def test_get_interval_2(store):
    assert store.get_interval("MyKey01000") == (1000,1100)

def test_get_interval_3(store):
    assert store.get_interval("MyKey01001") == (1000,1100)

def test_get_interval_4(store):
    assert store.get_interval("MyKey99999") == (99900, 100000)

def test_get_interval_5(store):
    assert store.get_interval("MyKey999999") == (99900, 100000)

def test_get_indexed_1(store):
    assert store.get_indexed("MyKey00000") == "MyValue0"

def test_get_indexed_2(store):
    assert store.get_indexed("MyKey01000") == "MyValue0"

def test_get_indexed_3(store):
    assert store.get_indexed("MyKey01001") == "MyValue1"

def test_get_indexed_4(store):
    assert store.get_indexed("MyKey99999") == "MyValue999"

def test_get_indexed_5(store):
    assert store.get_indexed("MyKey100000") is None