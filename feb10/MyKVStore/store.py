from typing import List, Tuple


class Store:
    def __init__(self, table:List[Tuple[str,str]]):
        self.table = table
        #Jeg hjelper deg med dette..
        self.table.sort(key=lambda x: x[0])
        # self.sparse_index = ????

    def get_naive(self, k:str):
        # Skriv koden din her!!!
        return None

    def create_sparse_index(self):
        my_range = [i for i in range(len(self.table)) if i%100==0]
        sparse_index = []
        #Skriv koden din her!!!
        return sparse_index

    def get_interval(self, k:str):
        last = 0
        next = None
        for (n, i) in self.sparse_index:
            #Skriv koden din her
            pass
        if next == None:
            next = len(self.table)
        return (last, next)

    def get_indexed(self, k:str):
        (last,next) = self.get_interval(k)
        for (n,v) in self.table[last:next]:
            #skriv svaret ditt her
            pass

        return None