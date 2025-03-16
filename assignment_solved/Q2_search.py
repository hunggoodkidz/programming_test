#!/usr/bin/env python3

class Node:
    """
    A simple Node class for the linked list in each bucket.
    Stores (key, value) and a pointer to the next node.
    """
    def __init__(self, key, value, nxt=None):
        self.key = key
        self.value = value
        self.next = nxt

class SeparateChainingHashST:
    """
    A Separate Chaining Hash Table that uses a linked list for each bucket.
    Instead of computing a hash function, it relies on a pre-computed hash index
    for each key (passed in when inserting).
    """
    def __init__(self, M):
        """
        Initialize the hash table with M buckets, each pointing to None.
        """
        self.M = M
        self.st = [None] * M  # st[i] will be the head of a linked list

    def put(self, key, hash_index, value):
        """
        Insert (key, value) into the chain at st[hash_index].
        If the key already exists, update its value.
        """
        head = self.st[hash_index]
        current = head

        # Traverse the linked list to see if key already exists
        while current is not None:
            if current.key == key:
                # Key found -> update value
                current.value = value
                return
            current = current.next

        # Key not found -> insert a new node at the head of the chain
        new_node = Node(key, value, head)
        self.st[hash_index] = new_node

    def get(self, key):
        """
        Retrieve the value for the given key by searching *all* buckets.
        (We do this because we don't have a built-in hash function here
         to compute which bucket to search directly.)
        Returns -1 if the key is not found.
        """
        for i in range(self.M):
            current = self.st[i]
            while current is not None:
                if current.key == key:
                    return current.value
                current = current.next
        return -1  # Key not found

    def print_chains(self):
        """
        Utility function to print out the contents of each chain.
        Useful for debugging.
        """
        for i in range(self.M):
            print(f"Chain {i}:", end=" ")
            current = self.st[i]
            while current is not None:
                print(f"({current.key}, {current.value}) ->", end=" ")
                current = current.next
            print("Null")  # Changed from "None" to "Null"

def search_demo():
    # 5 (hash indices range from 0 to 4).
    sch = SeparateChainingHashST(5)

    # Data: (key, hash, value)
    data = [
        ("S", 2, 0),  ("E", 0, 1),  ("A", 0, 2),  ("R", 4, 3),
        ("C", 4, 4),  ("H", 4, 5),  ("E", 0, 6),  ("X", 2, 7),
        ("A", 0, 8),  ("M", 4, 9),  ("P", 3, 10), ("L", 3, 11),
        ("E", 0, 12)
    ]

    # Insert all entries into the hash table
    for key, h, val in data:
        sch.put(key, h, val)

    # Print the final chain structure
    print("Final chain structure:")
    sch.print_chains()

if __name__ == "__main__":
    search_demo()
