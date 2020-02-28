from doubly_linked_list import DoublyLinkedList

# Ring buffer is a FIFO data structure. Meaning that as
# data moves through it, it starts at the head and moves towards a tail.
# once it reaches the tail new data overwrites the old data.
# since the DLL was given to us, use that functionality.
# using a DLL makes it somewhat similar to an LRU cache.
# In reality you would probably have to create a circular linked list.
# our implementation doesn't need to do that, though. Thankfully.


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # does the buffer contain anything?
        if self.storage.length < self.capacity:
            self.storage.add_to_head(item)
            self.current = self.storage.tail
        elif self.current is self.storage.tail:
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            self.current = self.current.prev
        elif self.current is self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.tail
        else:
            self.current.insert_after(item)
            self.current.delete()
            self.current = self.current.prev
        


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_node = self.storage.head
        while self.current is not None:
            list_buffer_contents.insert(0, current_node.value)
            if current_node.next is None:
                break
            else:
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
