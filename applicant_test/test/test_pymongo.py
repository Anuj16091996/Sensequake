import sys

# To join a path to Model Package
import pymongo
from bson import ObjectId

sys.path.append("..")  # added!
from applicant_test.Model import Config
from applicant_test.Model import citiesCollection
from applicant_test.Model import roadsCollection
from applicant_test.Controller import citiescontroller
import unittest


class TestFunction(unittest.TestCase):

    # to check whether port is working or not
    def test_port_connection(self):
        result = Config.DAO.databaseconnection()
        self.assertNotEqual(result, None)

    # To check city_name_not_contain return a Cursor type
    def test_city_name(self):
        fake_data = "value"
        result = citiesCollection.CitiesCollection.city_name_not_contain(fake_data)
        self.assertEqual(type(result), pymongo.cursor.Cursor)

    # To check if the lenght of pymongo Cursor is more than 0
    def test_road_lenght(self):
        result = citiesCollection.CitiesCollection.road_length()
        status = False
        if (len(list(result)) > 0):
            status = True
        self.assertTrue(status)

    # To check the return should be int
    def test_count_island(self):
        result = roadsCollection.RoadsCollection.count_number_of_island()
        self.assertEqual(int, type(result))

    # To check the return shoudld be a list
    def test_power_line(self):
        fakeData = [
            {'_id': ObjectId('626ae05c6dbc50607b424466'), 'name': 'Montreal',
             'endpoints': [ObjectId('626ae05c6dbc50607b42444e'), ObjectId('626ae05c6dbc50607b424435')],
             'length': 7.530818644847088},
            {'_id': ObjectId('626ae05c6dbc50607b42445a'), 'name': 'Rome',
             'endpoints': [ObjectId('626ae05c6dbc50607b424447'), ObjectId('626ae05c6dbc50607b42443b')],
             'length': 484.49198718371304}
        ]
        result = citiescontroller.check_minimum_length(fakeData)
        self.assertEqual(type(result), list)
