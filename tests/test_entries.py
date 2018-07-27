import unittest
import json

# fix import errors
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import app

app = app.create_app()
app.config.from_object('config.TestingConfig')



class EntryTests(unittest.TestCase):
    """Tests functionality of the API"""


    def setUp(self):
        self.app = app.test_client()
        self.entry = json.dumps({"user_id" : "007"})
        self.todo = json.dumps({"to-do" : "Going to cinema with my friends"})
        self.existing_diary = self.app.post('/api/v1/entries', data=self.entry, content_type='application/json')
        
    def test_get_all_entries(self):
        response = self.app.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)

    def test_successful_entries_creation(self):
        data = json.dumps({"user_id" : "010", "to-do" : "swimming"})
        response = self.app.post('/api/v1/entries', data=data, content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result.get("user_id"), None)
        self.assertEqual(result.get("to-do"), "swimming")
        self.assertEqual(response.status_code, 201)

    def test_entry_creation_existing_number(self):
        data = json.dumps({"user_id" :"020", "to-do": "to watch a game"})
        response = self.app.post('/api/v1/entries', data=data, content_type='application/json') # pylint: disable=W0612
        response2 = self.app.post('/api/v1/entries', data=data, content_type='application/json')
        result = json.loads(response2.data)
        self.assertEqual(result.get("message"), 'entry with that id already exists')

    def test_create_empty_entry(self):
        data = json.dumps({ "entry" : "........."})
        response = self.app.post('/api/v1/entries', data=data, content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result.get("message"), {'user_id': 'kindly provide a valid id'})


    def test_create_menu_invalid_entry(self):
        data = json.dumps({"d": "one hundred"})
        response = self.app.post('/api/v1/entries', data=data, content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result.get("message"), {'user_id': 'kindly provide a valid id'})

    def test_get_one_entry(self):
        response = self.app.get('/api/v1/entries/1')
        self.assertEqual(response.status_code, 200)

    def test_getting_non_existing_entry(self):
        response = self.app.get('/api/v1/entries/57')
        self.assertEqual(response.status_code, 404)

    def test_successful_update(self):
        data = json.dumps({"user_id" : "1", "to-do" : "swimming"})
        response = self.app.put('/api/v1/entries/1', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_updating_non_existing_entry(self):
        response = self.app.put('/api/v1/entry/57')
        self.assertEqual(response.status_code, 404)


    def test_good_deletion(self):
        response = self.app.delete('/api/v1/entries/1')
        self.assertEqual(response.status_code, 200)
        

  
if __name__ == '__main__':
    unittest.main()

