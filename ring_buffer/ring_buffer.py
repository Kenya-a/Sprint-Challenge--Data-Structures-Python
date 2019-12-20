from doubly_linked_list import DoublyLinkedList
 

 # When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element.

 #`append` method adds elements to the buffer. 
 
 # The `get` method, which is provided, returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity == self.storage.length:
            self.storage.remove_from_head()
        self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.storage.head

        while current_node is not None:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
