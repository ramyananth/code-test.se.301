#This file has to be in the same folder as main.py (The server API) 
import os
import unittest
import json
 
from main import app, db
 
 
TEST_DB = 'test.db'
 
 
class TestBook(unittest.TestCase):
 
    #Testing for Database Connectivity

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:0911@127.0.0.1:5432/quant"
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        #self.TestBook = TestBook() 
        self.assertEqual(app.debug, False)
 
    #If Database is correctly connected, a status code 200 is returned

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        print("Database Testing:")
        self.assertEqual(response.status_code, 200)

    #def tearDown(self):
     #   pass

    # # Checking if table "employee" exists in the database and columns are correcctly returned

    # def table_exists(self):
    #     exists = False
    #     try:
    #         app = Flask(__name__)
    #         cors = CORS(app)
    #         app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:0911@127.0.0.1:5432/quant"
    #         db = SQLAlchemy(app)
    #         cur = db.cursor()
    #         cur.execute("select exists(select relname from pg_class where relname='" +employee+ "')")
    #         exists = cur.fetchone()[0]
    #         print(exists)
    #         cur.close()
    #     except psycopg2.Error as e:
    #         print(e)
    #     print("employee table exists?")
    #     self.assertEqual(exists,True)

    # #End point check if json is created and returned
    
    # def isjson(self):
    #     foo = {}
    #     foo['gummy'] = 'bear'
    #     ans = (json.dumps(foo)) 
    #     mylist = json.loads("[5,6,7]")
    #     self.assertEqual((ans,{"gummy": "bear"}) and (mylist,[5, 6, 7]))
     
 
if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
