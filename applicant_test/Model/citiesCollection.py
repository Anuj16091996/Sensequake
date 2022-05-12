# Importing Database Connection
from .Config import DAO

# Storing Connection in a variable
connection = DAO.databaseconnection()


class CitiesCollection:
    @staticmethod
    # Returning all the collection values whose,
    # name is not equal to value of parameter
    def city_name_not_contain(cityName):
        # to check if port is working
        if connection is not None:
            # making a connection to cities
            cities = connection["cities"]
            # creating new collection newCIties/ and once its created accessing new collection
            # to save values
            cities_not_equal = connection['newCities']
            # dropping all the collection values
            cities_not_equal.drop()
            # find all the values as per condition of query
            value = cities.find({'name': {'$ne': cityName}})
            # saving that value in newcities collection
            for val in value:
                cities_not_equal.update_one({'_id': val['_id']}, {'$set': {'name': val['name']}}, upsert=True)

            # returning newCities collection
            return cities_not_equal.find({})

        else:
            #  If the port is not working
            return None

    # What i understood is that the city whose name is hello, and length less than 0
    # should not be in collection and the id of those cities who name is hello should not in
    # endpoints
    @staticmethod
    def power_liner():
        # Checking if port is working
        if connection is not None:
            # Making a connection
            cities = connection["newCities"]

            #  Joining two collection
            query_solution = cities.aggregate([
                {
                    # joining newcities collection with road on id through enpoints
                    '$lookup': {
                        'from': 'roads',
                        'localField': '_id',
                        'foreignField': 'endpoints',
                        'as': 'powerdetails'
                    }
                }
                # #  To add all field values in a collection
                , {
                    '$replaceRoot': {'newRoot': {'$mergeObjects': [{'$arrayElemAt': ["$powerdetails", 0]}, "$$ROOT"]}}
                },

                # To initialize only fields.
                {
                    "$project":
                        {
                            'powerdetails': 0,

                        }
                },

                #  Filtering where endpoints are not connected to any city
                #  and length is not null
                {"$match": {"endpoints": {'$exists': 'true', '$ne': 'null'}}},
                {"$match": {"length": {'$exists': 'true', '$ne': 'null'}}},
            ])
            return query_solution
        else:
            return None
