#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length # allocating memory for the route list

    """
    YOUR CODE HERE
    """
    #loop through the list of tickets
    for t in tickets:
            hash_table_insert(hashtable, t.source, t.destination)
        # add tickets to the hash table (you have to add something to the table to get something back duh)
        # source will be the key, destination will be the value
        # if source = "None"
        # if t.source == "NONE":
        #     # then add it to the first index of the route
        #     route[0] = hash_table_retrieve(hashtable, t.source)

    # create the rest of the list by looping through the full length of the new list starting at the second index
    for i in range(length):
        if i == 0:
            source = "NONE"
        # # if the source is the same as the destination of the previous route
            # route[i] = hash_table_retrieve(hashtable, source)
        else:
            source = route[i-1]
        # retrieve the tickets from the hash table and add it to the route at the current idex
        route[i] = hash_table_retrieve(hashtable, source)
    
    return route[:-1]