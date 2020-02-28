# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # plan:
        # if value is less than current_node, move it to the left.
        # If it's greater move it to the right.
        current_node = self
        new_sub_tree = None
        while True:
            # if current node is greater than or equal we want the value to go to the left
            if value < current_node.value and current_node.left is not None:
                current_node = current_node.left
            # if value is greater than or equal we want it to goto the right
            elif value >= current_node.value and current_node.right is not None:
                current_node = current_node.right
            # if current node is greater than or equal value and there is no left
            # sub_tree, create one
            elif value < current_node.value and current_node.left is None:
                current_node.left = BinarySearchTree(value)
                new_sub_tree = current_node.left
                break
            # if value is greater than current node or equal and there is no right
            # sub_tree, create one
            elif value >= current_node.value and current_node.right is None:
                current_node.right = BinarySearchTree(value)
                new_sub_tree = current_node.right
                break
        return new_sub_tree
    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current_node = self
        # plan:
        # the current value the target?
        # if it's not set the value to the left or right based on whether the target
        # is greater or less than the current value
        # move through the tree until it is found?
        while True:
            if target == current_node.value:
                return True
            elif target != current_node.value and current_node.left is None:
                return False
            elif target != current_node.value and current_node.right is None:
                return False
            elif target < current_node.value and current_node.left is not None:
                current_node = current_node.left
            elif target > current_node.value and current_node.right is not None:
                current_node = current_node.right

    # Return the maximum value found in the tree
    def get_max(self):
        # use the get max method from DLL in Queue and stack?
        # why does this only work with self.right?
        # answer from lecture: because the right tree is bigger than the root node.
        if self.right:
            return self.right.get_max() # THIS IS RECURSIVE
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # seems like recursion is necessary here.
        # what does this actually want?
        # visit every node.
        # call cb on all right and all left
        # cb(self.value) --> root
        # if self.left:
        # self.left.for_each(cb)
        # if self.right
        # self.right.for_each(cb)
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.value)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.value)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # need to use a queue here
        # traverse in layers -> 4 -> 1, 5 -> 2, 6 
        # iterative
        start = Queue()
        start.enqueue(node)
        current = start.dequeue()

        while current:
            print(current.value)
            if current.right:
                start.enqueue(current.right)
            if current.left:
                start.enqueue(current.left)
            if start.size > 0:
                current = start.dequeue()
            else:
                break


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # need to use a stack
        # traverse in branches 2 -> left: 1, 2, 0 -> right: 3, 4, 5
        # recursive or iterative
        # create an instance of a stack
        start = Stack()
        start.push(node)

        while start.len() > 0:
            traverse = start.pop()
            print(traverse.value)
            if traverse.right:
                start.push(traverse.right)
            if traverse.left:
                start.push(traverse.left)





    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self.value)
        if self.right:
            self.right.pre_order_dft(self.value)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # preorder, but self.value is at the end?
        if self.left:
            self.left.post_order_dft(self.value)
        if self.right:
            self.right.post_order_dft(self.value)
        print(self.value)


# new_tree = BinarySearchTree(5)
# new_tree.insert(10)
# new_tree.insert(4)
# new_tree.insert(1)
# new_tree.insert(9)
# new_tree.insert(80)
# new_tree.in_order_print(new_tree)