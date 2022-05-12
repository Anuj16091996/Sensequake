# Importing Database Connection


from .Config import DAO

# Storing Connection in a variable
connection = DAO.databaseconnection()


class RoadsCollection:

    # What i understood is that the city whose name is hello, and length less than 0
    # should not be in collection
    @staticmethod
    def city_length():
        roads = connection["roads"]

        query_solution = roads.aggregate([
            # Filtering out all the values in roads collection
            # length is less than 0
            {"$match": {"length": {"$gt": 0}}},

            # Concatenating two collection in one collection to return;
            {
                '$lookup': {
                    'from': 'newCities',
                    'localField': 'endpoints',
                    'foreignField': '_id',
                    'as': 'cityDetails'
                }
            }
            #  To add all values in a collection
            , {
                '$replaceRoot': {'newRoot': {'$mergeObjects': [{'$arrayElemAt': ["$cityDetails", 0]}, "$$ROOT"]}}
            },

            # To initialize only fields.
            {
                "$project":
                    {
                        'cityDetails': 0
                    }
            },
            # # Filtering where city name is not equal to given condition
            {"$match": {"name": {'$exists': 'true', '$ne': 'null'}}},

        ])

        return query_solution

    # This function will concatenate two collections,
    # and based on the end points of travelling between those cites
    # it will return the length of a cursor
    @staticmethod
    def count_number_of_island():
        if connection is not None:
            roads = connection["roads"]
            query_solution = roads.aggregate([
            # Concatenating two collection in to one collection to return;

                {
                    '$lookup': {
                        'from': 'cities',
                        'localField': 'endpoints',
                        'foreignField': '_id',
                        'as': 'cityDetails'
                    }
                }

            ])

            return len(list(query_solution))
