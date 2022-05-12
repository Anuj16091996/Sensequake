# Importing Database Connection
from .Config import DAO

# Storing Connection in a variable
connection = DAO.databaseconnection()


class CitiesCollection:
    @staticmethod
    # Returning all the collection values whose,
    # name is not equal to value of parameter
    def city_name_not_contain(cityName):
        if connection is not None:
            cities = connection["cities"]
            cities_not_equal = connection['newCities']
            cities_not_equal.drop()
            value = cities.find({'name': {'$ne': cityName}})
            for val in value:
                cities_not_equal.update_one({'_id': val['_id']}, {'$set': {'name': val['name']}}, upsert=True)

            return cities_not_equal.find({})

        else:
            #  If the port is not working
            return None
