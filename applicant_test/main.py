# todo: implement the thing
from Model.roadsCollection import RoadsCollection
from Model.citiesCollection import CitiesCollection
from Controller.citiescontroller import check_minimum_length

# Query for cities collection whose name not equal hello
nameNotContain = CitiesCollection.city_name_not_contain("hello")
# Error validation if database is not working
# Debug to check query value
# if nameNotContain is not None:
#     for position in nameNotContain:
#         print(position)


# Query for roads that have length greater than 0 and connect two cities
# exclude the one in A) collection.
cities_detail = CitiesCollection.road_length()
# Error validation if database is not working
# Debug to check query value

# if nameNotContain is not None:
#     for position in cities_detail:
#         print(position)

# Query for counting number of islands
number_of_island = RoadsCollection.count_number_of_island()
# validation in console
# print("the number of islands would be", number_of_island)

# Query for Power lines
power_lines = RoadsCollection.power_liner()
if power_lines is not None:
    minimum_length = check_minimum_length(power_lines)
# Error validation if database is not working
# Debug to check query value

# if nameNotContain is not None:
#     for position in minimum_length:
#         print(position)
