# Importing Database Connection


from .Config import DAO

# Storing Connection in a variable
connection = DAO.databaseconnection()


class RoadsCollection:

    # return all collection whose road connect two cities
    @staticmethod
    def city_length():
        if connection is not None:
            roads = connection["roads"]
            query_solution = roads.aggregate([
                # Concatenating two collection in one collection to return;
                {
                    '$lookup': {
                        'from': 'cities',
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
                            'cityDetails': 0,

                        }
                },

            ])

            return query_solution
        else:
            return None

    # function concatenate two collections,
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
                        'from': 'citiescontroller.py',
                        'localField': 'endpoints',
                        'foreignField': '_id',
                        'as': 'cityDetails'
                    }
                }

            ])

            return len(list(query_solution))
        else:
            return None
