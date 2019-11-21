import psycopg2

class ProdutoBanco:

    def __init__(self):
        self.connection = psicopg.connect(
            dbname ='produto',
            user ='admin', 
            password ='123', 
            host ='localhost', 
            port = '5432')