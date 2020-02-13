import unittest 
from app import rating, app
from flask import Flask


class SearchTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass    

    assert rating(0, 0, 0, 0, 0) == 0, "Not rated yet"
    assert rating(1, 1, 1, 1, 1) == 3, "Recipe is rated (Average)"
    
    
class WebTests(unittest.TestCase):
    
    def setUp(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.client = app.test_client()

    def tearDown(self):
        pass 

    def find_recipe_page_found(self):
        response = app.test_client(self).get('/find_recipe', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "find_recipe returned status code %s should be 200" % str(response.status_code)) 


    def one_recipe_page_found(self):
        response = app.test_client(self).get('/one_recipe/5e3f7590dfba92f0c4687f3c', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "one_recipe returned status code %s should be 200" % str(response.status_code))
        

    def search_recipe_page_found(self):
        response = app.test_client(self).get('/search_recipe', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "search_recipe returned status code %s should be 200" % str(response.status_code))


    def sign_up_page_found(self):
        response = app.test_client(self).get('/sign_up', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "display_results returned status code %s should be 200" % str(response.status_code)) 


    def sign_in_page_found(self):
        response = app.test_client(self).get('/sign_in', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "sign_in returned status code %s should be 200" % str(response.status_code))  

    def one_my_recipe_page_found(self):
        response = app.test_client(self).get('/one_my_recipe/5e40917776aadd8a75acd01f', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "one_my_recipe returned status code %s should be 200" % str(response.status_code))  

    def add_recipe_page_found(self):
        response = app.test_client(self).get('/add_recipe', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "index page returned status code %s should be 200" % str(response.status_code))  

    def edit_recipe_page_found(self):
        response = app.test_client(self).get('/edit_recipe/5e40917776aadd8a75acd01f', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "edit_recipe returned status code %s should be 200" % str(response.status_code))  
    
    def home_page_found(self):
        response = app.test_client(self).get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "find_recipe status code %s should be 200" % str(response.status_code))  
         

if __name__=="__main__":
    unittest.main()