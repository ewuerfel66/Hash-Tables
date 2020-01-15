# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # Get an index
        index = self._hash_mod(key)

        # None
        if self.storage[index] is None:
            # Create LinkedPair
            new_kvp = LinkedPair(key, value)
            # Insert at that index
            self.storage[index] = new_kvp
            return

        # Not None
        elif self.storage[index]:
            # Store old pair
            temp = self.storage[index]

            # Add New
            self.storage[index] = LinkedPair(key, value)

            # Set old pair as next
            self.storage[index].next = temp


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # Get the index
        index = self._hash_mod(key)
        cur = self.storage[index]

        if cur:
            if cur.key == key:
                cur.value = None
            else:
                while cur.next is not None:
                    cur = cur.next
                    if cur.key == key:
                        cur.value = None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Get an index
        index = self._hash_mod(key)
        cur = self.storage[index]

        if cur:
            if cur.key == key:
                return cur.value
            else:
                while cur.next is not None:
                    cur = cur.next
                    if cur.key == key:
                        return cur.value

                return None

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # Save data in a temporary object
        temp = self.storage

        # Change capacity & reset storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        # Insert each one in the temp
        for kvp in temp:
            if kvp:
                self.insert(kvp.key, kvp.value)
                while kvp.next is not None:
                    kvp = kvp.next
                    self.insert(kvp.key, kvp.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
