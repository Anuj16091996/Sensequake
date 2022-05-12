def check_minimum_length(Cursor):
    # Initializing empty array to add a minimum
    # length to traverse between cities with less length taken
    power_line = []

    # iterating values fetch object element
    for pos in Cursor:
        # if the length of a power line is empty
        # its gonna append with the first object to element
        if len(power_line) == 0:
            power_line.append(pos)
        # if there is a object in power line,
        # this will check the length of the city name by
        # comparing the city name key and and if name key are same, next step
        # is to check length
        else:
            # To get updated length of power_line
            length = len(power_line)
            # at which position its checking the length
            position = 0
            for element in power_line:
                # Check the key Cursor Command key-: name is equal to element key name
                if pos["name"] == element["name"]:
                    # to check if  key Cursor Command key-: length is less than element length
                    if pos["length"] < element["length"]:
                        # will remove the exiting object from a specific position
                        power_line.pop(position)
                        # will add object at a position where it was being remove on previous step
                        power_line.insert(position, pos)
                        # after adding the element, it will break the loop and continue traversing to next object
                        # if exits
                        break

                    else:
                        # if element does length condition
                        break


                else:
                    # updating the position relative to element
                    position = position + 1
                    # if the position and length are same, it will add
                    # it will add value power_line and break the loop
                    if position == length:
                        power_line.append(pos)
                        break
    # returning the list
    return power_line
