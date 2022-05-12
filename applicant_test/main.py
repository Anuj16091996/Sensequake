# todo: implement the thing
from Model.roadsCollection import RoadsCollection
from Model.citiesCollection import CitiesCollection

# Query for cities collection whose name not equal hello
nameNotContain = CitiesCollection.city_name_not_contain("hello")
# Error validation if database is not working
# Debug to check query value
# if nameNotContain is not None:
#     for position in nameNotContain:
#         print(position)


# Query for roads that have length greater than 0 and connect cities
cities_detail = RoadsCollection.city_length()
# Error validation if database is not working
# Debug to check query value

# if nameNotContain is not None:
#     for position in cities_detail:
#         print(position)


number_of_island = RoadsCollection.count_number_of_island()
# Number of islands
print("the number of islands would be", number_of_island)
