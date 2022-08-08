import psycopg2
from breeze_connect import BreezeConnect


class Neo4j:
    def __init__(self):
        self.app = None
        self.conn = None
        self.breeze = None

    def init_app(self, app):
        self.app = app
        self.connect()
        self.initbreeze()
        

    def connect(self):
        if not self.conn:
            self.conn = psycopg2.connect(user="postgres",
                                        password="password123",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")     
        return self.conn

    def initbreeze(self):
        if not self.breeze:
            self.breeze = BreezeConnect(api_key = "16)3W5i10$108kn5W16153162~t339j0")
        cursor = self.conn.cursor()
        cursor.execute("SELECT apisession from mp.session;")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
        print(record[0])
        cursor.close
        self.breeze.generate_session(api_secret="_35993o671I841=378H5831560O67*77", 
                                     session_token=record[0])

    def get_db(self):
        if not self.breeze:
            self.connect()
            self.initbreeze()
        return self.breeze

neo4j = Neo4j()