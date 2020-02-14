#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # loop over weights
        # find the item in the hash-table with that weight
        # the first number exsists
            # 
    for i,w in enumerate(weights):
        first = hash_table_retrieve(ht, limit-w)
        print(f"first{first}")
        if first is not None:
            second = i
            print(f"second{second}")
            if first > second:
                return (first, second)
            else:
                return (second, first)       
        hash_table_insert(ht,w,i)
    # hash_table_retrieve(ht,)
    #item1 + item2 == limit
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
